# ISM 技能匹配与排序口径（成本公式、子列表降级、PLTR/LIT、坐席列表容量）

## R — 原文依据

> "Mandatory Cost for an agent: • Cman = ((|Lag(s) - Lcall(s)|) * W(s)) … The lowest Cman determines the selected agent … When the Cman are equal, the algorithm selects the agent with the lowest Copt"（p171）
> "1st sub-list: « N » call attributes: with skill level of agent >= skill level of the call • After the timeout • 2nd sub-list: « N-1 » call attributes …"（p169）
> "asm_ag_free_duration=0 use of the rule "PLTR" … =1 in this case LIT (Longest Idle Time) is used … =2 LIT in case ASM in network"（p180）
> "LIT is not realy working. By default, the agent statistics are refreshed only every 5 min."（p215）

出处：OTCCXTE101EN p160-186, p209-220。

## I — 自述

ISM 是 ACR 最常用的规则子程序：按呼叫档案与坐席技能算出"最佳坐席列表"。匹配是三级漏斗：

1. **强制门槛**：坐席必须具备呼叫档案全部强制属性，且坐席等级 ≥ 呼叫要求等级，才进第 1 子列表
2. **逐级降级**：重选定时不中则生成第 2 子列表（N-1 项满足+1 项不满足），依次降到第 N 子列表（全不满足）
3. **同级排序**：先比 Cman（强制属性成本和）最小，同分比 Copt（可选属性成本和），再同分按 PLTR 或 LIT

两个成本公式（s 遍历属性，W 为域权重 1-20，等级 1-9）：

| 公式 | 求和范围 | 语义 |
|---|---|---|
| Cman = Σ(\|坐席等级-呼叫等级\| × 域权重) | 强制属性 | 最小者排第一 |
| Copt = Σ(\|坐席等级-呼叫等级\| × 域权重) | 可选属性 | Cman 同分时的决胜局 |

关键边界：坐席没有某可选技能时按等级 9 代入（最大差值惩罚，p186）。

排序参数与容量口径：

| 参数 | 取值 | 语义 |
|---|---|---|
| asm_ag_free_duration=0 | 默认 | PLTR（通话时长/登录时长，升序），统计期 5 分钟内排序不变 |
| asm_ag_free_duration=1 | 需 IDLE 积木块 | LIT 最久空闲优先 |
| asm_ag_free_duration=2 | 组网场景 | 网络 LIT（本地或网络坐席） |
| Number of ACR agent buffers | 20-400（RSI system parameters） | 坐席列表长度；ASM 默认最多返回 200 坐席 |
| 坐席统计刷新 | 默认 5 分钟 | 低话务时 LIT 形同"同一坐席每 5 分钟被叫一次" |

## A1 — 书中案例

**ISM 手算全例**（p182-186，4 域 5 坐席）：

1. 呼叫档案 Car_Call_Profile：Car L4 强制、French L3 强制、Paris L1 强制、Life insurance L1 可选、Client L1 可选
2. 强制筛选：Agent2 无 Car、Agent3 无 French 出局；Agent5 Car 等级低于要求只能进后续子列表
3. Agent1 Cman=(9-3)×1+(4-4)×4+(5-1)×2=14；Agent4 Cman=(5-3)×1+(5-4)×4+(5-1)×2=14
4. Cman 同分转 Copt：Agent1=(2-1)×4+9×3=31（无 Client 技能按 9 代入）；Agent4=(1-1)×4+(2-1)×3=3
5. 结论：Sub-List1=Agent4、Agent1；Sub-List2=Agent5（p186 原文验收）

**LIT 切换实验**（p215-220）：

1. nano /usr3/afe/parameters.cfg 把 asm_ag_free_duration 由 0 改 1，保存
2. dhs3_init -R MAIN_AFE 重启 AFE 进程使参数生效
3. 验证："Now the agent will be used one after the other based on LIT"（p219）

## A2 — 未来触发

使用情境：解释"为什么这个坐席先响"；给客户开"最久空闲优先"；评估坐席列表容量；核对 ACR 对象容量上限；低话务站点公平性验收。

语言信号：ISM / 技能匹配 / 成本 / Cman / Copt / 子列表 / 降级 / PLTR / LIT / 最久空闲 / asm_ag_free_duration / parameters.cfg / agent buffers / 容量上限 / 21 次 / 20-400 / 5 分钟。

与相邻能力区分：编写/调试脚本本体与 LCA 记忆路由转 ASM 脚本卡（路由入口，深度在姊妹技能）；建域/技能/呼叫档案的操作转 ACR 对象卡（路由卡）。

## E — 可执行步骤

输入契约：呼叫档案（属性/等级/强制可选清单）、候选坐席技能表、域权重表。缺档案或技能数据 → 先回 ACR 对象卡补齐数据基础。

1. 核对呼叫档案与坐席技能数据完整（等级 1-9、权重 1-20、强制/可选标志）。完成标准：每个属性可代入公式
2. 逐坐席算 Cman 并排序；同分坐席再算 Copt（无该可选技能按 9 代入）。完成标准：得到有序坐席列表
3. 需要最久空闲时：parameters.cfg 加 asm_ag_free_duration=1，脚本加 IDLE 积木块，重启 MAIN_AFE。完成标准：同分坐席按 LIT 轮转
4. 向客户交付前核对两条边界：统计 5 分钟刷新、列表缓冲 20-400/默认返回 200。完成标准：承诺与口径一致

判停点：

- 客户要求"呼叫级绝对公平轮转" → 停，5 分钟统计刷新决定了 LIT 达不到，评估调整统计周期属书外操作
- 坐席技能区间/权重超出 1-20、1-9 → 停，口径错误，回 ACR 对象卡核对数据模型
- 需要话务建模决定坐席数 → 停，书外能力，指向 Feature List 与话务历史数据

输出契约：可核算的坐席列表排序结论（含子列表划分）+ 排序参数配置记录 + 容量合规核对单。

## B — 边界

- "21 次重选上限"为实验观察口径（p214/p220/p245 三处并存，见 needs-review nr-05），不是调优建议值
- LIT 的 5 分钟统计刷新与 StatPeriod 调整为书外操作（p04/n08）；低话务下承诺逐呼叫公平不成立
- 技能域怎么划、权重怎么定：原书只教配置不教设计（n41），照实验建域上生产大概率失真
- 容量表（p77：域 20/技能 1000/档案属性 7/坐席技能 50 等）为 R10.15 口径，超限以当期 Feature List 为准
- 网络场景（asm_ag_free_duration=2）与 ACR 组网（调大 buffers）书中仅给方向，未给完整组网方案
