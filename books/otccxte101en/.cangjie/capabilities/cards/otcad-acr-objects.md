# ACR 对象与技能体系（等待室、ACR/统计 Pilot、域/技能/呼叫档案、坐席技能）

## R — 原文依据

> "Waiting Rooms are needed in ACR & don't work in FIFO mode … Waiting Room & Waiting Queue CANNOT be open at the same time"（p71-72）
> "Applications/CCD/Skill/Skill Domain • Skill domain number: 2 … Applications/CCD/Skill/Call profile • Call profile number: 0 … Expertise level: 1 • Mandatory: True"（p120-122）
> "The ACR Pilot is blocked. If the Agent does not have any skill, the Waiting Room is blocked !"（p148）

出处：OTCCXTE101EN p71-92, p117-159。

## I — 自述

ACR 矩阵的对象链与双侧配置路径：

| 对象 | 路径（OXE WBM 侧） | 关键参数 |
|---|---|---|
| 处理组 | Applications > Processing Group | Type=Agent/IVR/Other/Remote/Rerouting |
| 等待室 | Applications > CCD > Queue（Type=Waiting room） | 方向 0-29、监控定时器、话务采样 5mn、最大等待（实验 3000）、振铃监控；与等待队列同规则互斥 |
| ACR Pilot | Applications > CCD > Pilot | 有等待室方向或挂激活规则即为 ACR Pilot |
| 统计 Pilot | Applications > CCD > Statistic pilot | 挂路由 Pilot、call tag、call priority（例 -1）、呼叫档案——客户实际拨的号 |
| 技能体系 | Applications > CCD > Skill > Skill Domain / Skill parameters / Call profile | 域 0-19（0/1 默认语言媒体）、技能 0-999（0-99 预定义）、等级 1-9、权重 1-20 |
| 坐席数据 | Applications > CCD > Operators data management | Skill set+激活标志；Manage skills=True 时坐席可从话机自开关技能 |

技能四层模型：域（权重 1-20）> 技能（名 1-16 字符/缩写 1-4 字符）> 等级（1 低-9 高）> 激活标志；坐席最多 50 技能、呼叫档案最多 7 属性。CCS 侧对应：Configurations > Advanced Call Routing > Skill（域 ID 自动分配）与 ACR Data 页（呼叫档案）；技能矩阵支持批量管理与导出/导入。

阻塞传导链：坐席全无（激活）技能 > 等待室阻塞 > ACR Pilot 阻塞；反之坐席带激活技能登录即打开（p154）。

## A1 — 书中案例

**ACR 对象部署七步**（p130-159，编号为实验口径）：

1. WBM 建附加处理组 Agent2_PG=31803（Type=Agent）
2. 建等待室 WaitingRoom=31704（Type=Waiting room）
3. 建 ACR Pilot=31603
4. 建统计 Pilot 31660（Car Insurance）与 31661（Home Insurance），路由 Pilot 均指 31603
5. CCS 配路由：Call Flow mgt > Call Routing 建 Rule_0 并 Apply，Normal 页启用 WaitingRoom
6. CCS 配分配：Queue and Waiting Room 给 31704 加两个坐席 PG，Call Distribution 勾通方向
7. 坐席附加 PG 并重新登录；技能三连（建域/技能、配呼叫档案、给坐席赋技能）后验证：技能赋给前 WR 阻塞、赋给后变绿；未挂脚本时呼叫落其他队列或 Pilot 闭锁数据

## A2 — 未来触发

使用情境：给客户从零建 ACR 矩阵；"等室有人等、坐席却闲着"类分配异常；新业务线要新呼叫档案；批量管理坐席技能。

语言信号：ACR / 等待室 / Waiting Room / ACR Pilot / 统计 Pilot / Statistic pilot / 技能域 / Skill Domain / 呼叫档案 / Call profile / 技能矩阵 / Skills Matrix / Operator data / 阻塞 / blocked / 动态组。

与相邻能力区分：列表怎么算出来的（算法口径）转 ISM 技能匹配卡；脚本编写与激活转 ASM 脚本卡（路由卡，深度在姊妹技能）；队列水位与互助方向转 Remote PG 卡。

## E — 可执行步骤

输入契约：业务到技能的映射表（域/技能/等级/权重）、坐席名单与分组、WBM+CCS 管理权。前置约束：ACD 前缀必须已建（n20）。

1. 建处理组与等待室（Type 选对，互斥规则记住）。完成标准：对象在 Navigator 可见
2. 建 ACR Pilot 与统计 Pilot（呼叫档案挂统计 Pilot）。完成标准：路由链 Pilot 入口就绪
3. CCS 接路由与分配方向并启用 Normal 模式。完成标准：规则 Apply 且方向勾通
4. 建域/技能/呼叫档案（CCS 或 WBM 双侧任一）。完成标准：档案属性 ≤7、区间合规
5. 给坐席赋技能并确认激活，需要时开自管理。完成标准：WR 由阻塞变绿
6. 验证：技能赋给前阻塞、赋给后打开；未挂脚本时呼叫按回落链处理。完成标准：三阶段验收通过

判停点：

- 第一通电话没人接 → 停，先看 WR 是否阻塞（n19），再查坐席登录与技能激活，最后才怀疑脚本
- 坐席有档案技能却拿不到等待室呼叫 → 停，查技能激活标志（n18：无档案坐席只服务等待队列）
- 客户问"域和权重怎么设计" → 停，配置可教，设计方法论在书外（n41），如实声明
- 组网环境要改/删技能 → 停，域与技能全网广播（n17），先全网评审引用

输出契约：ACR 矩阵对象清单（含编号方案）+ 技能体系表 + 三阶段验收记录。

## B — 边界

- 讲义示例号（31703/31650）与实验号（31704/31660）并存，照抄前核对现场配置（nr-02）
- 等待室与等待队列同规则互斥；等待室无资源选择优先级、非 FIFO（p71-72/p88）
- 技能设计方法论（划域/定权重/评等级）书外（n41）；容量上限（域 20/技能 1000/档案 7/坐席 50）为 R10.15 口径
- ABC 网络中域与技能广播（n17）：改名/删除影响全部节点
- 语音引导=迎宾+6 泊位、40 种语言（p82）；泊位级 EWT 表/IAA 地址/交互排队细节属讲义图示口径
