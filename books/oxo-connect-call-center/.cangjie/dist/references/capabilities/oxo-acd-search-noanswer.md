# 坐席搜索模式选型与无应答处理（OXO Connect）

## R — 原文依据

> "Search mode • Fixed priority • Rotating priority • Longest idle period"（p95）
> "Validate the parameter Maximum ringing duration to 10 seconds. Make a call to the ACD No. Group 3 without any response ... the call is routed to extension 102 and extension 103 automatically swap to ''off duty'' status. ... Then the call will definitely stay on extension 101."（p110-111）

出处：OXOCXTE107EN p95（三模式）、p97（Priority order）、p109-111（对比实验与两档无应答行为）。

## I — 自述

"组内下一个电话给谁"由搜索模式决定，与另外两个概念**三层正交**：

1. **搜索模式（组内分配算法，三选一）**：
   - Fixed：严格按 rank，一号位永远先接
   - Rotating：轮转，接听机会均摊
   - Longest idle：谁闲得久谁先接，天然负载均衡
2. **rank（组内静态优先序）**：Fixed 模式依据它；多组坐席还有 Priority order（组间先服务谁的队列）
3. **无应答两档开关**（独立于模式）：
   - 仅设"最大振铃时长"（实验 10 秒）：超时转下一位，循环
   - 再启用"无应答自动移除"：超时未接的坐席**自动置 off duty**，呼叫继续走人，最终钉在最后一名在值坐席

## A1 — 书中案例

**三模式 + 两档无应答对比实验**（p109-111，厂商实验，含标准答案）

- 配置：组1 Fixed / 组2 Longest idle / 组3 Rotating（组3 rank：103(r1)/102(r2)/101(r3)）
- **实验 A**（仅振铃上限 10 秒）：呼组3 无人接，103 响 10s 转 102，102 响 10s 转 101，101 响 10s 回到 103 循环
- **实验 B**（再启用自动移除）：呼组3 无人接，103 响 10s 转 102 且 103 自动 off duty；102 响 10s 转 101 且 102 自动 off duty；呼叫钉在 101
- 教材要求三种模式都实测，并结合 rank 观察差异

## A2 — 未来触发

使用情境：

1. "电话总给同一个人接，想轮流"——Fixed 改 Rotating/Longest idle
2. "坐席怎么一个个变成 off duty 了"——自动移除的连锁效应
3. "响多久没人接才转下一个"——最大振铃时长
4. "既属 A 组又属 B 组，先接哪组"——Priority order 组间优先
5. "让最闲的人先接"——Longest idle 选型

语言信号：轮流接听 / 分配不均 / search mode / rotating / longest idle / fixed priority / 振铃超时 / 自动移除 / off duty 被签出 / rank。

与相邻能力区分：rank 的**初始配置**在基础搭建能力；坐席四态切换 → 签入签出能力；队列容量 → 队列管理能力。

## E — 可执行步骤

输入契约：话务分配偏好（公平/技能优先/负载均衡）、可接受振铃等待（秒）、无应答处置策略。缺偏好先询问，不替客户选。

1. **选型**：按偏好映射模式。完成标准：客户确认
2. **配置**：General parameters / "Group 1-4" tab → Search mode。完成标准：保存生效
3. **振铃上限**：同页 General tab → maximum ringing duration。完成标准：参数保存
4. **无应答策略决策**：启用自动移除前，向客户说明连锁效应（坐席逐个被 off duty）。完成标准：客户知情确认
5. **A/B 验证**：全坐席不接听，呼入观察——A 档循环振铃；B 档逐个 off duty 后钉在最后一人。完成标准：实测与所选档位一致
6. **rank 联动**：多组坐席核对 Priority order 与预期一致
7. **恢复**：验证后用 501 前缀或 Supervisor 台恢复误签出坐席

判停点：客户要求"无应答不影响坐席状态"→ 不启用自动移除，说明循环振铃的代价。

输出契约：模式选型说明书 + 振铃时长 + 开关状态 + 连锁效应告知记录 + 实测记录。

## B — 边界

- 自动移除是双刃剑：解决"无人接"的同时制造"坐席集体消失"次生故障——务必知情
- rank / 搜索模式 / Priority order 三者正交，混谈会导致"调了 rank 没效果"的误判
- 振铃时长是组级参数，不是坐席级
- 原书实验为三坐席小规模；大组的公平性表现需上线后按实际话务观察
