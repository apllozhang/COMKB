# ACD 呼入六场景排障（OXO Connect）

## R — 原文依据

> "Processes available: Process when agents are available / Process when all agents are busy / Process when the queue is full / Process when all standard ACD ports are busy / Process when all agents are logged out or ''off duty'' status / Process when the ACD group is closed"（p36）
> "First ACD incoming call will be transferred to a pre-defined number. Subsequent calls are either queued or routed to a deterrent message"（p97）
> "All standard ACD ports busy? ... Use of dedicated ports for dissuasion status"（p40）

出处：OXOCXTE107EN p36-42（六场景流程图）、p112-114（逐场景实验验证）。

## I — 自述

OXO 上的每一通 ACD 呼入，先过"营业时间测试"，OPEN 后按资源占用落入六种场景之一，每种场景的处理分支和出口都不同：①有空闲坐席——欢迎语后直接转坐席；②坐席全忙——进等待队列，先播消息 1，达到阈值插播预计等待/排名消息，循环播消息 2，来电者可按 `*` 键退出（转组邮箱或预定义号码）；③队列满——按"转接目的地 > 组邮箱 > 劝漏语音后释放"三级判定出口；④标准 ACD 端口全忙（≤16）——跳过队列直接进劝漏态（用专用端口），出口同③；⑤全员登出/off duty——**只有第一通**来电转预定义 Transfer number，后续来电路队或劝漏；⑥组关闭——播关闭语后释放，同样可改转接/邮箱。排障时先判定来电落在哪个场景，再去核对该场景的出口配置。

## A1 — 书中案例

**场景验证实验**（p112-114，厂商实验）：
- 队列实验：组1 坐席全忙时呼入 → "hear the welcome message 1 first then the waiting message 2 that is looped"；坐席一空闲，队首呼叫立即转出；按 `*` 退出后依次启用 "Place in group voice mailbox" 与 "Transfer to a number" 并逐一验证。
- 劝漏实验：组2 队列因子设 0.1（仅容 1 通）后连打两通 → 第一通入队，第二通播"坐席忙请稍后再拨"后释放；改用邮箱/转接出口再验。
- 关闭实验：组3 置关闭态呼入 → 播营业时间告知语后释放；逐一启用邮箱/转接出口再验。

## A2 — 未来触发

使用情境：
1. "客户打进来说响一声就断了"——劝漏态（队满或端口忙）。
2. "有时打得进来有时打不进来"——全员登出场景的"仅首呼转接"特征。
3. "下班时间还有人打进来听到奇怪提示"——关闭场景或时段配置错误。
4. "排队的人听到什么提示？能不能让他留言？"——队列出口配置。
5. "来电直接被挂但组里明明有空闲坐席"——查端口占用或 signalization mode。

语言信号：来电被挂断 / 排队 / 等待音乐 / 劝漏 / dissuasion / queue full / 没人接 / 留言 / 非工作时间 / call dropped / no answer。

与相邻能力区分：坐席侧"登录了却不接"→ 签入签出能力；队列长度数值怎么定 → 队列管理能力；本能力是"来话行为走向"的判定与出口配置。

## E — 可执行步骤

输入契约：故障现象描述（来电听到什么/何时发生）、组配置（时段/队列因子/出口现状）、发生时间点。缺现象细节先询问。

1. 判定营业时间测试结果：呼入时刻在组开放时段内吗？（General parameters 的时段表；Supervisor 是否强制 open/closed）。→ CLOSED 场景走第 6 步；OPEN 继续。
2. 判定坐席可用性：有 On duty 且已登录的坐席吗？全无 → 场景 5 走第 5 步。
3. 判定队列与端口：标准 ACD 端口（≤16，与 MLAA 共享）是否全忙？全忙 → 场景 4（直接劝漏，不经队列）。未全忙但队列已满（ceil(N×K)）→ 场景 3。
4. 场景 1/2（有坐席）：核对欢迎语与队列消息配置（General parameters → Call distribution / Call management 图标）；验证欢迎语先播、阈值消息正确插入、`*` 退出去向正确。完成标准：实呼行为与配置一致。
5. 场景 5（全员登出）：确认 Transfer number 已配置且符合预期（注意**只有第一通**被转，后续入队或劝漏——向客户解释该特性而非当作故障）。完成标准：用户理解行为或调整出口。
6. 场景 3/4/6 共用出口判定：Call distribution / Call management 中依次检查 "Transfer to a number" 与 "Place in group voice mailbox" 两选项；都没配 = 播语音后释放。完成标准：出口与客户需求一致并实呼验证。
7. 修复后回归：按原现象重演一次呼叫确认行为正确。

判停点：第 1 步发现时段配置与客户预期不符 → 转营业时段能力修正后重新判定；坐席侧异常（未登录/off duty）转签入签出能力。

输出契约：场景判定结论（六选一）+ 出口配置现状 + 修改项 + 实呼验证结果。

## B — 边界

- 队列长度与等待时间的**数值计算**不在本能力（队列管理能力）；本能力只管行为走向与出口。
- 坐席"显示忙却不接 ACD"是坐席子状态问题（Supervisor 监控能力），不是来话场景问题。
- 劝漏语音本身的录制/上传见语音定制能力。
- 组间溢出（本组队列 10 秒后溢到别组坐席）会让你误判场景——先确认是否存在坐席跨组与溢出配置（原书仅示意，配置入口待核，见 needs-review nr-01）。
- 原书为 RLAB 实验口径：生产环境还需排除中继侧问题（原书未覆盖）。
