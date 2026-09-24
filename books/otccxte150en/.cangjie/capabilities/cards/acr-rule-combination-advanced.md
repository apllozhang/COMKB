# ACR 综合规则组合与高级构件（APPLY 语义、IDLE/COM、IQUEUE、LIST 变量、混合选呼）

## R — 原文依据

> "Single ACR Rules Have to be used alone in the APPLY instruction: LAST CALLED AGENT, REDIRECTION, REDISTRIBUTION, IVR • Combinable Rules: AUTHORIZED LIST, UNAUTHORIZED LIST, ISM, IDLE, COM"（p244）
> "When 2 “APPLY” instructions are encountered, the 1st one has no effect on the result sent back to the call handling • When only 1 “APPLY” instruction is used, the agent list of a rule is build according to the agent list of the previous rule"（p245）
> "Allows to overwrite the parking level management done in the routing rule • Up to 7 levels: Levels “1…6” • Level “Next”"（p249）
> "There are 16 automatic lists, indexed from 1 to 16 … The “agent” type list • The “skill” type list"（p258）

出处：OTCCXTE150EN p230-282。

## I — 自述

规则组合三法则与四个高级构件，是复杂业务脚本的工具箱：

1. **单用规则**（LCA/Redirection/Redistribution/IVR）必须独占 APPLY；**可组合规则**（Authorized/Unauthorized/ISM/IDLE/COM）可串接；IDLE 与 COM 互斥
2. **APPLY 数量决定语义**：仅 1 个 APPLY 时前规则输出=后规则输入（链式过滤，名单真正约束坐席）；两个及以上 APPLY 时各自独立，第一个的结果被丢弃（名单约束静默失效——全书最反直觉语义）
3. **IDLE/COM 排序**：IDLE 按 asm_ag_free_duration 分 PLTR/LIT 两语义；COM 按登录后服务呼叫数比率排，参数对它无影响
4. **IQUEUE**：脚本内覆写等待房间停放体验——1-6 级每级可配引导（号/掐断/时长/重播）、EWT 表或地址；NEXT 级在重选重跑而上一停放未播完时接管；未指定的级回落路由规则配置
5. **LIST 变量**：16 个 LIST[%1..16]，元素定类型——skill 型（供 ISM，超 7 技能截断：先删低级别可选再删低级别强制）与 agent 型（供名单规则，无上限）；"+"合并同技能取高级别，"-"移除元素
6. **其他构件**：CLEAR AGENT LIST 清空前列表重算；RULE_IVR 送 CCivr 资源组并可传档案；DISPLAY_AGENT 屏显四类取值（显式串/显示变量/自动变量/Call Tag 值）

呼叫选择统一排座次（CCD/ACR 混跑）：

| 次序 | 比什么 |
|---|---|
| 第一 | 呼叫选择优先级（0-9，0 最高） |
| 第二（默认 False） | 最低 ISM 成本，再看最长实际等待 |
| 第二（True） | 最长实际等待，再看最低 ISM 成本 |

ISM 成本三档：非 ISM 的 ACR 呼叫为 0；ISM 的 ACR 呼叫按档案计算（不低于 0）；等待队列里的普通 CCD 呼叫为无穷——这是 ACR 呼叫默认插队的机制本质。

## A1 — 书中案例

**1Apply 与 2Apply 对照（c10 步骤 3-4）**：

1. 脚本 1Apply：单 APPLY 写 RULE_AUTHORIZED_LIST 31501 31502 加 RULE_ISM
2. 坐席技能：31501 有 Car、31502 只有 Home、31500 有 Car 但不在名单
3. 呼 ACR Pilot：仅 31501 振铃（31500 技能匹配但被前列表过滤）
4. 脚本 2Apply：两个 APPLY 分写名单与 ISM
5. 同场景复测：31500 也被呼——名单结果未作为 ISM 输入，约束静默失效

**Addition 脚本（IQUEUE 加 CLEAR，c10 步骤 5）**：

1. 录停放引导 701-706 与 IQUEUE 专属引导 751-756、NEXT 757（实验口径）
2. 档案含 Home：ISM 加 IQUEUE，坐席全忙时客户听各级专属引导直到有坐席
3. 无 Home：第 1 序列转坐席 31500 并屏显 NO HOME、不可达停 12 秒
4. 第 2 序列 CLEAR_PREVIOUS_LIST 后走 LAST_CALLED_AGENT 重算
5. 分别呼两个统计 Pilot，Debugger 验证三条路径

**混合选呼两场景（c10 步骤 7-8）**：

1. 队列 31999700 优先级 9、房间 31999703 优先级 8：房间呼叫先被处理
2. 两处均改 9：默认按最低 ISM 成本；ACR Actual Waiting 置 TRUE 后按最长实际等待

## A2 — 未来触发

使用情境：名单加技能组合不生效；想让客户等待时听分级引导；坐席按空闲或话务量均匀分配；ACR 与普通 CCD 呼叫抢坐席；动态拼名单。

语言信号：APPLY / 单用规则 / 可组合规则 / IDLE / COM / IQUEUE / 停放级 / NEXT / LIST 变量 / CLEAR AGENT LIST / IVR 规则 / ISM 成本 / ACR Actual Waiting / 插队。

与相邻能力区分：单规则语法与调试，见 脚本编辑器能力；名单数据维护，见 名单规则卡（路由）；排序参数文件，见 脚本编辑器能力（LIT/PLTR 段）。

## E — 可执行步骤

输入契约：业务组合需求（哪些规则串联）、坐席技能与名单数据、引导录音资源（用 IQUEUE 时）。

1. 画组合草图：确认每个规则属单用还是可组合，IDLE 与 COM 不共存。完成标准：组合方案合法
2. 要求"名单约束技能"的必须写成单 APPLY 链式。完成标准：APPLY 数量与语义一致
3. 需要停放体验控制时配 IQUEUE 各级参数。完成标准：未指定级回落行为已确认
4. 动态名单用 agent 型 LIST 拼装后交名单规则。完成标准：Debugger 里 LIST 内容正确
5. 混跑站点核对呼叫选择优先级与 ACR Actual Waiting 口径。完成标准：两处配置与业务一致
6. Debugger 全路径验证：写对照实验（1Apply 与 2Apply 各测一遍）。完成标准：坐席命中与设计一致

判停点：

- 名单形同虚设 → 停，查 APPLY 数量，两个以上即失效，改单 APPLY
- 想同时按空闲和话务量排序 → 停，IDLE 与 COM 互斥，二选一
- ACR 呼叫持续插队普通来电 → 停，用优先级或 ACR Actual Waiting=TRUE 平衡并向客户讲清
- IQUEUE 引导未播完就被重选打断 → 正常，NEXT 级接管，配 NEXT 引导即可

输出契约：复合业务脚本 + 组合语义对照验证记录 + 混跑选呼口径。

## B — 边界

- 两 APPLY 第一个失效是产品语义（p245/p270 实验），版本升级也应以现场验证为准
- SET 指令（PRIORITY/RESELECTION_TIMEOUT）不占 APPLY（p25 条件）
- 语言偏好参与 ISM 成本计算的具体算法原书只给示例（成本 0/3），未给公式全貌
- 多语言引导与 CCivr 档案传递分别在多语言卡与 Call Tag 卡（路由）展开
- 引导号 701-706/751-757 等为实验口径；停放级基础管理仍在路由规则，IQUEUE 只做覆写
