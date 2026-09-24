# CCD 基础矩阵创建与验证（pilot/队列/处理组/ACD 前缀）

## R — 原文依据

> "Select Translator> Prefix Plan> … Number Enter the ACD prefix number (i.e. 12). … The ACD prefix is mandatory prior to create the CCD matrix objects."（p66）
> "The Call Distribution is based on a matrix: Pilots … Call routing … Queue normal … Int. Overflow … Redirection … Processing groups (Resources)"（p23-24）
> "be shared among several Pilots (30 max) • serve several Processing Groups (50 max) • Queued calls are served FIFO"（p27）
> "Agent processing group • Made up of agent or supervisor sets … Voice guide processing group … Rerouting processing group … I.V.R processing group"（p29）
> "5 Control with command acdsup … A=agent group F=Forward group V=Voice guide processing group CLO= pilot closed"（p76-77）

出处：OTCCXTE100EN p22-29, p40, p63-77。

## I — 自述

五级矩阵是一切的地基：pilot（被叫部门）经路由进队列，队列经分配进处理组，PG 内选座席（f04）。

建矩阵前必须先建 ACD 前缀（实验 12），否则 CCD 对象建不了（p66）。

- 三类 PG：Agent（唯一承接 ACD 分发）、Forward（前转本机号码）、Voice Guide（播指南）；另有 Rerouting/IVR（p29）
- 三类队列：Normal（停车常）、Intelligent Overflow（智能溢出）、Redirection（兜底重定向）；每队列最多被 30 个 pilot 共享、服务 50 个 PG，FIFO（p27）
- 兼容硬约束：Voice Guide PG 只能接 Redirection 队列（p40）
- 实验基准矩阵：Agent_PG(31800)、Forwarding_PG(31801，前转 31010)、Voice_guide_PG(31802)；Normal_WQ(31700)、Overflow_WQ(31701)、Redirection_WQ(31702)；Pilot1(31600)、Pilot2(31601)（p64，实验口径）
- 验证抓手：mtcl 会话 acdsup 看矩阵——A=座席组、F=前转组、V=语音指南组、CLO=pilot 关闭、OPN=正常态（p76-77/p120）

## A1 — 书中案例

**基础矩阵创建实验**（p63-77）：

1. OXE Web Admin（https://192.168.1.3，mtcl 登录，实验口径）进 Translator 建前缀 12
2. 建 Agent_PG：Applications> CCD> Processing Group> Create，DN 31800、Type Agent
3. 建 Forwarding_PG：DN 31801、Type Forwarding、前转地址 31010
4. 建 Voice_guide_PG：DN 31802、Type Voice guide
5. 建三队列：Normal_WQ 31700、Overflow_WQ 31701、Redirection_WQ 31702（p71-73 字段表笔误见 nr-02，按 p64 目标矩阵录）
6. 建 Pilot1(31600)、Pilot2(31601)：Applications> CCD> Pilot> Create
7. PuTTY 开 mtcl SSH 会话执行 acdsup 复核矩阵对象与状态

**验收判读**：无座席登录、规则未建时 pilot 显示 CLO（关闭态）属预期；A/F/V 三类组出现即矩阵对象齐（p76-77）。

## A2 — 未来触发

使用情境：新装 OTCC Standard 从零建矩阵；矩阵对象增补（加队列/PG/pilot）；acdsup 输出判读；"pilot 是 CLO 正常吗"；队列/PG 类型选型。

语言信号：CCD 矩阵 / pilot / waiting queue / processing group / ACD prefix / Normal_WQ / Overflow_WQ / Redirection_WQ / acdsup / CLO / OPN / FIFO / 31800。

与相邻能力区分：建规则让矩阵活起来 → 路由与分配规则能力；建座席班长 → 座席班长体系能力；实验站点外呼打通归实验环境与链路能力（路由卡）。

## E — 可执行步骤

输入契约：OXE Web Admin 可登录、mtcl SSH 可达、目标编号段已定（生产按客户编号计划，实验为 31600/31700/31800 段）。

1. 建 ACD 前缀：Translator> Prefix Plan> Create，Number=前缀号（实验 12）、Local Features=ACD Prefixes。完成标准：保存成功且 COS 放行（Phone Features COS 启用 ACD Prefixes）
2. 建 PG 三件：Applications> CCD> Processing Group> Create 依次建 Agent/Forwarding/Voice guide 三组。完成标准：Forwarding 组前转地址已填、Voice guide 组留待挂指南
3. 建队列三件：Applications> CCD> Queue> Create 建 Normal/Intelligent Overflow/Redirection 三队列。完成标准：三个 DN 唯一且类型与名称对应（勿照抄 p71-73 字段表，见 nr-02）
4. 建 pilot：Applications> CCD> Pilot> Create 建业务 pilot。完成标准：pilot DN 在编号计划内、命名可辨识
5. mtcl 会话执行 acdsup 核对。完成标准：A/F/V 组与 pilot 状态行出现，判读字母与矩阵意图一致

判停点：

- acdsup 命令不存在或报错 → 按现场命令名为准（书中 acdsup/acdsetup 混用，见 nr-03），不要硬猜
- Processing Group 建不出来 → 先查 ACD 前缀是否已建、COS 是否放行（p66 前置）
- 队列类型选错（如 Voice Guide PG 想挂 Normal 队列）→ 兼容表不允许，改用 Redirection 队列或换 PG 类型
- 生产环境照抄实验 DN/前缀 → 判停，编号计划须按客户规范重排（实验口径红线）

输出契约：可路由的最小矩阵（3 PG + 3 队列 + pilot + ACD 前缀）+ acdsup 判读记录。

## B — 边界

- 全部 DN/前缀/口令为 RLAB 实验口径；生产按客户编号计划与安全基线替换（n19）
- IVR PG 依赖外部 CCivr 服务器，Rerouting PG 指向 ABC-F/公网——两者本书只点名不展开（n41）
- 队列 30 pilot/50 PG、pilot 三态等容量与状态语义是 R10.16 教材口径，扩容前对照当版 Feature list（p03）
- 本卡只建对象不建规则——矩阵建完 pilot 仍是 CLO，属正常（p76-77）
- acdsup 命令名书中两写（nr-03）；建队列表格笔误（nr-02）引用时按本卡口径
