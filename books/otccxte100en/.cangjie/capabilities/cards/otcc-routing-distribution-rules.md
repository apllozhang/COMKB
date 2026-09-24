# 路由规则与分配规则全生命周期（方向/优先级/激活）

## R — 原文依据

> "A routing rule is managed to associate each pilot with waiting queues (30 rules max per pilot)"（p43）
> "Priorities value is from 0 to 9 • 0 is the highest priority • 9 is the lowest priority"（p44）
> "A call distribution rule (10 max) defines the distribution of the calls to the processing groups • A queue can have up to 50 possible distribution directions"（p54）
> "By default, the call distribution rule is deactivated. You must activate the rule from OXE management console."（p113）
> "Warning … BY DEFAULT, ALL DIRECTION RULES ARE CLOSED"（p117）

出处：OTCCXTE100EN p43-59, p98-120, p626-627。

## I — 自述

两级规则把矩阵连成活链路：路由规则连 pilot 与队列（每 pilot 最多 30 条、全局 1200 条），分配规则连队列与 PG（全局最多 10 条、每队列最多 50 个方向）。

优先级统一 0-9（0 最高、9 最低），三类平局规则各不相同（p01）：

- 路由方向同优先级 → 系统选 EWT 最低的队列
- 资源选择同优先级 → 选 PG 最长空闲时间（LIT）最大者
- 呼叫选择同优先级 → 选队首真实等待时间最长的呼叫

两条"默认关"是本书最高频事故源：

- 分配规则默认停用，且必须回 OXE Web Admin 勾 Active Rule 激活（CCS 日历激活是例外路径）（p113/n02）
- 所有方向默认关闭——分配点建好只是黄色连接点，须逐条进 Resource selection 勾 Direction 才变红/绿（p117/n01）

每条 pilot 规则含 Normal/Blocked/General Forward 三张表（对应 pilot 三态）+ 6 个 parking level（每级可放语音指南、IAA/IVR 地址或 EWT 表）（p45/f05）。

## A1 — 书中案例

**规则创建实验**（p98-120）：

1. 业务目标：Pilot1 常态走 Normal_WQ→Agent_PG，饱和走 Overflow_WQ→Forwarding_PG
2. CCS Call Flow mgt> Call Routing 选 Pilot1，Pilot rule 区 Create 建 Rule_0 并 Apply
3. 回 OXE Web Admin 的 Pilot 页核验 Rule_0 已应用到 31600/31601
4. Configurations> Pilot 给两个 pilot 加 Possible queues（Normal_WQ + 溢出/重定向队列）
5. Normal mode 页签勾启 Normal 方向；优先级 Normal_WQ 设 0、溢出队列设 9
6. Call Flow mgt> Call Distribution Create 建 Rule_0；回 OXE 勾 Active Rule 激活
7. Navigator 点黄色连接点建分配方向并勾 Direction 激活——连接点变红/绿即通

**验收判读**：acdsup 显示 OPN（pilot 正常态）；Agent_PG 因无座席登录仍为红色属预期（p120）。

## A2 — 未来触发

使用情境：配好矩阵但来话不通；改路由优先级；分配规则建完不生效；新增 PG 后方向没开；查"连好线不等于能通话"类工单；按日历切换规则。

语言信号：routing rule / distribution rule / Rule_0 / 优先级 / priority / Active Rule / Direction / Resource selection / Navigator 连接点 / parking level / EWT / LIT / 默认关闭。

与相邻能力区分：矩阵对象本身 → CCD 基础矩阵能力；方向的语音指南内容 → 语音指南能力；日历时间片配置细节归多语言与日历能力。

## E — 可执行步骤

输入契约：矩阵对象已建齐（pilot/队列/PG）、CCS 可登录、业务路由意图明确（常态/溢出/兜底各走哪条路）。

1. 建 pilot 规则：CCS Call Flow mgt> Call Routing 选 pilot → Create 规则 → Apply。完成标准：OXE 侧 Pilot 页可见规则已应用
2. 加路由方向：Configurations> Pilot 给 pilot 加 Possible queues。完成标准：Navigator 出现 pilot 与队列的连接
3. 激活路由方向并定优先级：Normal mode 页签勾方向、按业务定 0-9。完成标准：常态方向优先级数值最小
4. 建分配规则并激活：Call Distribution Create 后必须回 OXE Web Admin 勾 Active Rule。完成标准：OXE 侧规则状态为激活
5. 建并激活分配方向：给每个队列加 PG 方向，逐条勾 Direction 并 Save。完成标准：Navigator 连接点变红/绿（不再是黄色）
6. 端到端验证：来话走常态方向；制造饱和验证溢出方向。完成标准：acdsup 显示 OPN 且呼叫按意图落位

判停点：

- 矩阵齐全但呼叫不通 → 先查两个"默认关"：分配规则是否 OXE 侧激活、方向是否勾选（n01/n02）
- Navigator 连接点黄色 → 已建未激活，进 Resource selection 勾 Direction
- 同优先级裁决有争议 → 路由看 EWT、资源看 LIT、呼叫看真实等待；PLTR 缩写书中未展开（nr-10），不编造
- 新建 Closed_rule 类备用规则同样要回 OXE 激活（p626-627 节点名 .false 后缀即未激活）

输出契约：端到端可通活的路由链（pilot 方向 + 分配方向全部激活）+ 优先级表 + 激活记录。

## B — 边界

- 方向数上限：每 pilot 30 方向、全局 1200 路由规则、10 条分配规则、每队列 50 分配方向（p43/p54/p103，R10.16 口径）
- 分配规则激活的例外路径是 CCS 日历——日历配置细节归多语言与日历能力（p113）
- 优先级与 EWT 的联动（饱和判定、TSP 滞后）在 EWT 与排队体验卡展开；本卡只管方向与优先级
- 路由规则三张表（Normal/Blocked/General Forward）的指南内容配置与语音指南域重叠，细节归语音指南卡
- 实验 DN/优先级取值为实验口径；生产按业务 SLA 设计（话务建模在书外，n30/n41）
