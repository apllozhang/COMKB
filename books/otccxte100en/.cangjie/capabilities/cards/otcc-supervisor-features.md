# 座席班长特性配置（退出类型/监听强插/通用转发/PG 关闭/多线/事务码）

## R — 原文依据

> "Unavailable type Enter the number of unavailable types you want to enable (i.e. 2) … Display Unavailable type 1 Enter the name … (i.e. Tea)"（p307）
> "Function Enter the ACD function (i.e. ACD Listening) … Mnemo … (i.e. Help Agent)"（p313）
> "Listen The supervisor listens … Agent is notified … if the parameter Show Supervisor Listening is set to 'True' (default=False in France and Germany)"（p315）
> "Transaction Code Dialing Timer … (the unit is 100ms). The minimum value allowed is 10."（p343）
> "Only calls assigned to type codes Business appear in the EXCEL statistics."（p344）

出处：OTCCXTE100EN p265-303（讲义）, p304-347（How-To）。

## I — 自述

班长特性围绕可编程键（Progr.Keys）与 PG/CCD 参数展开，六件事覆盖日常管控：

- 退出类型：每 PG 最多 9 种不可用类型供统计（Tea/Lunch 等），OXE 侧 UNAVAILABLE TYPE PARAMETERS 定义，IPDSP 退出键可见选项（p307）
- 监听与强插：班长 Help Agent 键响应座席求助后三选——Listen（旁听，座席侧提示受 Show Supervisor Listening 控制，法/德默认 False）、Restrictive（受限强插，仅座席闻声）、Intrusion（三方强插会议）；另可输座席号选 Permanent 永久监控（p313-315）
- 通用转发 pilot 四种激活：话机键（+密码）、CCS 界面 Set to FWD、日历到点切换、按规则（by rule）（c10）
- PG 关闭键：Closing PG + DN（留空则按键手选组），关闭后 Normal_WQ 方向关、溢出/重定向开（c10）
- 多线座席：Multi-line 键 + ACD line 键；ACD 呼叫优先接入、私人通话被保持（先登出班长才能改键）（c10）
- 事务码/业务码：事务码 1-15 位只存通话记录；业务码 1-3 位进 Excel 统计（上限 1000 个）；摘码窗口 Timer 单位 100ms、最小 10（p293/p343-344/n36）

## A1 — 书中案例

**班长特性实验**（p304-347）：

1. PG 31800 定义两种退出类型 Tea/Lunch，IPDSP 退出键出现两选项
2. 班长话机 Progr.Keys>2 设 ACD Listening（Mnemo=Help Agent）
3. 公网来话 Agent1 应答后按 Help 键：班长选 Listen/Restrictive/Intrusion 三态分别验证
4. Permanent 监控：Help 键输 31500 选 Permanent，此后座席状态变化班长可见
5. 通用转发：话机键挂 pilot 31600 + 关闭地址 31010，按键+密码激活，来话转 31010
6. 日历激活法：周一 09:00 Nor / 17:00 Fwd，把 Fwd 时间改成"当前+5 分钟"观察自动切换
7. PG 关闭键挂 31800：按键后 Navigator 显示 Normal_WQ 方向关、Overflow/Redirection 开
8. 事务码：pilot 摘码 Timer=100（10 秒）、位数 3、Business Code=Yes，挂机后输 123 报 Code registered

## A2 — 未来触发

使用情境：质检要旁听强插；座席求助键没配；下班一键把 pilot 切走；给班长配"优选组"不生效（归体系卡）；报表要按业务分类（业务码）；跨国部署旁听提示合规。

语言信号：退出类型 / unavailable type / 监听 / listening / 强插 / intrusion / 通用转发 / general forwarding / Closing PG / multi-line / 事务码 / business code / 100ms / Show Supervisor Listening。

与相邻能力区分：登录登出与挂组 → 座席班长体系能力；wrap-up 计时行为 → 对象调优能力；转发期间听什么指南归语音指南能力；业务码报表呈现归监控与统计能力。

## E — 可执行步骤

输入契约：座席班长已登入、管控需求清单（退出类型集、监听策略、转发去向、码类型）、合规口径已确认（旁听提示）。

1. 定义退出类型：OXE PG 31800 的 UNAVAILABLE TYPE PARAMETERS 设类型数与名称。完成标准：IPDSP 退出键可见全部类型
2. 配班长监听键：Progr.Keys 设 ACD Listening，三态（Listen/Restrictive/Intrusion）逐一验证。完成标准：旁听与强插行为符合预期且提示口径与市场参数一致
3. 按需开 Permanent：输座席号选永久监控。完成标准：座席退出/忙状态班长实时可见
4. 配通用转发：先配 pilot 关闭地址，再按场景选四种激活法之一。完成标准：激活后 Navigator 显示 GF 态、来话走关闭地址
5. 配 PG 关闭键与多线键：先登出班长再改键。完成标准：关闭后流量走溢出/重定向；ACD 呼叫可打断保持中的私人通话
6. 配事务码：pilot 摘码 Timer（100ms 单位）、位数、Business Code 属性。完成标准：挂机后摘码成功且业务码进 Excel

判停点：

- 旁听无提示音/无提示消息 → 查 Show Supervisor Listening（法/德库默认 False），跨国部署先核合规（n25）
- 摘码窗口"只有 1 秒" → Timer 单位是 100ms，填 10 才是 10 秒（n36）
- 报表里看不到码记录 → 15 位事务码不进统计，只有 1-3 位 Business 码进 Excel（n36）
- 班长改键改不了 → 多线配置前必须先登出班长（c10 步骤）
- 手册附录的 67/66 前缀（Manual Hold/Park）→ 原书明令 DO NOT PROCEED，仅知识参考（n06）

输出契约：座席班长管控能力集（退出类型/监听/转发/关闭/多线/码）+ 行为验证与合规口径记录。

## B — 边界

- Show Supervisor Listening、Recordable Voice Guides、ABC Local Call Allowed 等默认值随目标库/国家不同，跨市场部署逐一核对（n25/n26）
- 监听与强插的合规要求（是否强制提示）按当地法规确认，书外事项（n25）
- 事务码进 CCA/CRM 等外部系统的集成在书外（n41）；业务码上限 1000 个（p478）
- 实验值（Tea/Lunch、密码 0000、码 123）为实验口径
- 模拟话机全靠前缀操作；Annex 前缀步骤仅供参考不可执行（n06）
