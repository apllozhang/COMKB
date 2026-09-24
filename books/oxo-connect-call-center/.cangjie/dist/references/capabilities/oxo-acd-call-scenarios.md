# ACD 呼入六场景排障（OXO Connect）

## R — 原文依据

> "Processes available: Process when agents are available / Process when all agents are busy / Process when the queue is full / Process when all standard ACD ports are busy / Process when all agents are logged out or ''off duty'' status / Process when the ACD group is closed"（p36）
> "First ACD incoming call will be transferred to a pre-defined number. Subsequent calls are either queued or routed to a deterrent message"（p97）

出处：OXOCXTE107EN p36-42（六场景流程图）、p112-114（逐场景实验验证）。

## I — 自述

每一通 ACD 呼入，引擎先测营业时间，OPEN 后按资源占用落进六场景——**每个场景出口独立可配**：

1. **坐席空闲**：欢迎语 → 直接转坐席
2. **坐席全忙**：进队列；先播消息 1，到阈值插播"预计等待/排名"，循环播消息 2；来电者按 `*` 自救（转邮箱或指定号码）
3. **队列满**：劝漏第一形态，出口三级判定——转号码 > 组邮箱 > 劝漏语音后释放
4. **端口全忙**（≤16，与 MLAA 共享）：跳过队列直接劝漏（第二形态），出口同上
5. **全员登出/off duty**：**只有第一通**转 Transfer number，后续排队或劝漏
6. **组关闭**：关闭语后释放，可改转接/邮箱

排障口诀：先归场景，再核对该场景的出口配置。

## A1 — 书中案例

**三组场景验证实验**（p112-114，厂商实验）

- **队列实验**（组1 坐席全忙时呼入）：
  - 现象：先听欢迎消息 1，再循环等待消息 2
  - 坐席一空闲 → 队首呼叫立即转出
  - 按 `*` 退出 → 依次启用 "Place in group voice mailbox" 与 "Transfer to a number" 并逐一验证
- **劝漏实验**（组2 队列因子 0.1，仅容 1 通，连打两通）：
  - 现象：第一通入队；第二通播"坐席忙请稍后再拨"后释放
  - 变体：改用邮箱出口或转接出口再各验一次
- **关闭实验**（组3 置关闭态呼入）：
  - 现象：播营业时间告知语后释放
  - 变体：逐一启用邮箱/转接出口再验

## A2 — 未来触发

使用情境：

1. "客户打进来说响一声就断了"——劝漏态（队满或端口忙）
2. "有时打得进来有时打不进来"——全员登出场景的"仅首呼转接"特征
3. "下班时间打进来听到奇怪提示"——关闭场景或时段配置错误
4. "排队的人听到什么？能不能留言？"——队列出口配置
5. "来电直接被挂但组里明明有空闲坐席"——查 ACD 端口占用或 signalization mode

语言信号：来电被挂断 / 排队 / 等待音乐 / 劝漏 / dissuasion / queue full / 没人接 / 留言 / 非工作时间 / call dropped / no answer。

与相邻能力区分：坐席侧"登录了却不接"→ 签入签出能力；队列长度数值怎么定 → 队列管理能力；本能力是"来话行为走向"的判定与出口配置。

## E — 可执行步骤

输入契约：故障现象（来电听到什么/何时发生）、组配置现状（时段/队列因子/出口）、发生时间点。缺现象细节先询问。

1. **判营业时间**：呼入时刻在开放时段内吗？（时段表；Supervisor 是否强制 open/closed）
   - CLOSED → 场景 6，跳第 6 步
   - OPEN → 继续
2. **判坐席可用性**：有 On duty 且已登录的坐席吗？
   - 全无 → 场景 5，跳第 5 步
   - 有 → 继续
3. **判队列与端口**：标准 ACD 端口全忙？（上限 16，与 MLAA 共享）
   - 全忙 → 场景 4
   - 未全忙但队列已满（ceil(N×K)）→ 场景 3
   - 有空位 → 场景 1/2
4. **场景 1/2 核对**：欢迎语与队列消息配置（Call distribution / Call management 图标）。完成标准：欢迎语先播、阈值消息正确、`*` 退出去向正确
5. **场景 5 核对**：Transfer number 已配置且去向正确；向客户说明"仅首呼转接"是特性不是故障。完成标准：行为与预期一致
6. **场景 3/4/6 出口判定**：Call management 中检查 "Transfer to a number" 与 "Place in group voice mailbox"；都没配 = 播语音后释放。完成标准：出口与客户需求一致
7. **回归**：按原现象重演呼叫确认修复

输出契约：场景判定结论（六选一）+ 出口配置现状 + 修改项 + 实呼验证结果。

## B — 边界

- 队列长度的数值计算不在本能力（队列管理能力）
- 坐席"显示忙却不接 ACD"是坐席子状态问题（Supervisor 监控能力）
- 组间溢出（队列 10 秒后溢到别组坐席，p96）会让你误判场景——先确认坐席是否跨组（溢出配置入口原书未写明，needs-review nr-01）
- 原书为 RLAB 实验口径：生产环境还需排除中继侧问题（原书未覆盖）
