# 坐席搜索模式选型与无应答处理（OXO Connect）

## R — 原文依据

> "Search mode • Fixed priority • Rotating priority • Longest idle period"（p95）
> "Validate the parameter Maximum ringing duration to 10 seconds. Make a call to the ACD No. Group 3 without any response ... the call is routed to extension 102 and extension 103 automatically swap to ''off duty'' status. ... Then the call will definitely stay on extension 101."（p110-111）
> "Do not forget to take into account the priority of the agents defined in the previous exercise."（p109）

出处：OXOCXTE107EN p95（三模式）、p97（Priority order 组间优先）、p109-111（三种模式对比实验与两档无应答行为）。

## I — 自述

"组内下一个电话给谁"由搜索模式决定，三选一：Fixed——严格按 rank 顺序，一号位永远先接；Rotating——每次从上次接完的人轮转，接听机会均摊；Longest idle——谁空闲得久谁先接，天然按实际负载均衡。它与 rank 是正交的两层：rank 是"同组内的静态优先序"，Priority order 是"坐席同属多组时先服务哪个组的队列"。另有一个独立开关"最大振铃时长"（实验值 10 秒）：来话在某坐席振铃超时即按模式转下一位。再叠加"无应答自动移除"开关后行为质变——超时未接的坐席会被**自动置为 off duty**，呼叫继续走人，最终钉在最后一名在值坐席身上。这两个开关组合出两档完全不同的无应答行为，是"来电没人接/坐席怎么被自动签出了"类问题的判据。

## A1 — 书中案例

**三模式对比实验**（p109-111，厂商实验，含标准答案）：
- 配置：组1 Fixed、组2 Longest idle、组3 Rotating（沿用基础实验 rank：组3 为 103(r1)/102(r2)/101(r3)）。
- 实验 A（仅设最大振铃 10 秒）：呼组3 无人接 → 先响 103，10 秒转 102，再 10 秒转 101，再回 103，循环不落地。
- 实验 B（再启用自动移除）：呼组3 无人接 → 103 响 10 秒后呼叫转 102、**103 自动变 off duty**；102 再 10 秒转 101、102 变 off duty；最后呼叫停在 101。
- 教材要求三种模式都实测并对照 rank 观察差异。

## A2 — 未来触发

使用情境：
1. "电话老是给同一个人接，想轮流"——Fixed 改 Rotating/Longest idle。
2. "坐席怎么一个个变成 off duty 了？"——自动移除开关的连锁效应。
3. "响多久没人接才转下一个人？"——最大振铃时长。
4. "又属于 A 组又属于 B 组，先接哪组的电话？"——Priority order 组间优先。
5. "想让最闲的人先接"——Longest idle 选型。

语言信号：轮流接听 / 分配不均 / search mode / rotating / longest idle / fixed priority / 振铃超时 / 自动移除 / off duty 被签出 / rank。

与相邻能力区分：rank 与优先序的**初始配置**在基础搭建能力里（本能力做选型与行为验证）；坐席四态切换操作 → 签入签出能力；队列容量 → 队列管理能力。

## E — 可执行步骤

输入契约：客户的话务分配偏好（公平轮转/技能优先/负载均衡）、可接受的振铃等待（秒）、无应答坐席的处置策略（继续轮转还是自动签出）。缺偏好先询问，不要替客户选模式。

1. 选型：按偏好映射——要"一号位优先兜底"选 Fixed；要"机会均等"选 Rotating；要"谁闲谁接"选 Longest idle。完成标准：客户确认选型。
2. 配置：OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / "Group 1-4" tab → Search mode 选定。完成标准：保存生效。
3. 配置振铃上限：同页 General tab → "maximum ringing duration"（实验值 10 秒，按客户容忍度设定）。完成标准：参数已保存。
4. 决策无应答策略：启用 "Agents that do not answer are automatically removed" 前必须向客户说明连锁效应（未接坐席自动 off duty，极端时来电钉在最后一人）；不启用则仅循环轮转。完成标准：客户知情并确认。
5. 行为验证（A/B 两档各验一次）：全坐席配合不接听，呼入组观察——A 档应循环振铃；B 档应看到坐席逐个 off duty、呼叫最终钉在最后在值坐席。完成标准：实测与所选档位一致。
6. rank 联动检查：多组坐席场景下确认 Priority order（组间优先）与客户预期一致（先服务哪组的队列）。
7. 恢复被误签出的坐席：验证后用 501 前缀或 Supervisor 台把 off duty 坐席恢复 on duty。

判停点：客户要求"无应答不影响坐席状态"→ 不启用自动移除并说明循环振铃的代价（ caller 等待更久）。

输出契约：模式选型说明书（选型理由 + 振铃时长 + 自动移除开关状态 + 连锁效应告知记录）+ 实测记录。

## B — 边界

- 自动移除是把双刃剑：隔离"无人接"问题的同时会制造"坐席集体消失"的次生故障——务必让客户知情。
- rank/搜索模式/Priority order 三者正交，混谈会导致"调了 rank 没效果"的误判：rank 是组内静态序，搜索模式决定是否遵循它，Priority order 只管跨组队列服务顺序。
- 振铃时长为组级参数（General tab），不是坐席级。
- 原书实验在 RLAB 三坐席小规模下进行；大组的轮转与公平性表现（原书未验证）上线后需按实际话务观察。
