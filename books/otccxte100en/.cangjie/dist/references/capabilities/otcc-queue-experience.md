# EWT 表与排队位置播报（518）

## R — 原文依据

> "EWT = Average wait x (Nb of calls in queue + 1)"（p47）
> "Parking Level … Guide N° / IVR in queue PG directory N° / IAA directory N° / EWT Table Threshold(1 to 6)"（p351）
> "Tree menus: 5 levels max • 4 choices max per level • 8 trees maxi • When an agent becomes free, the caller leaves the IAA menu"（p356）
> "The Variable Part is made of several voice messages that give the positions from 1 to 50 then by step of 5 up to 100."（p377）
> "The messages numbers are already created in the OXE (from 3226 to 4217)"（p379）

出处：OTCCXTE100EN p44-49, p348-357, p374-400。

## I — 自述

EWT（预期等待时间）是排队体验的中枢，公式：EWT = 平均等待 ×（队内呼叫数+1），平均等待按每队列 TSP 滚动计算；它同时是路由平局依据、饱和判据（EWT>最大等待时间）、播报分档依据（p02/g07）。

EWT 表（Configurations> EWT Tables）：每表 6 个阈值，每阈值=EWT 值+地址（仅 IAA 号或 CCIVR 号）+指南号；只能挂 normal 队列的 parking level（p351-352/f23）。

parking level 四种填充物：语音指南号 / 队内 IVR PG 号 / IAA 号 / EWT 表；下游资源空出时指南可被打断（cut auth）（p45/p365）。

518 排队位置指南（系统预置不可建改）：

- 结构：固定段（"You are in position"）+ 变量段（位次）+ 固定段（"in the waiting queue"）；固定段每语言一条，消息号 L1=3226/3227 起步进 2；变量段 L1 从 3258 起、每语言步进 60，至 4217
- 播报规则：位次 1-50 逐个精确播报、51-100 按 5 步进向上取整（63 位播 65）；Max position 上限 100，超限播 pilot 提示音直至位次回落；每次播报重算位次、第 6 级循环
- 语言回退链：呼叫语言未管理时回退默认语言；无默认语言则不播跳下一级；子消息缺失 → 播备份音（p15/n32）

IAA 菜树三重上限：5 层、每层 4 选项、8 棵树；座席一空闲，来电者即离开 IAA、播报可打断——不适合长内容（n35）。

## A1 — 书中案例

**EWT 三阈值实验**（p358-373）：

1. 建 720/721/722 三指南（"少于 10 秒"/"约 20 秒"/"超过 1 分钟"；原书"四条消息"实三条，见 nr-08）
2. 401 录三条消息并装板；vgstat 复核
3. CCS EWT Tables 建 Table[0]：阈值 1=10s/720、阈值 2=20s/721、阈值 3=60s/722，均勾 Cut Auth
4. 把 EWT 表挂到 Offer pilot 路由规则 Level[1]
5. Navigator 定制 Normal Queue 显示 Expected Waiting Time
6. 行为测试：PG idle wrap-up 拉到 300 秒制造排队，观察 EWT 跨阈值时播报切换（受 TSP 滞后影响，n30）

**518 位次实验**（p385-400）：

1. 518 指南页设语言与消息顺序（Fix1+Variable+Fix2）、Max position=2（实验口径）
2. 分配并录制变量段 3318="one"、3319="two" 与固定段 3228/3229
3. After-Sales 排分级：L2=518（1 次）夹在音乐与 684 之间
4. 三连测：第 1 通听"position 1"、第 2 通听"position 2"、第 3 通因超 Max position 只播提示音

## A2 — 未来触发

使用情境："让客户知道要等多久"；按等待时长播不同话术；"您排在第 N 位"；位次播到第几位合适；多语言站点位次播报；EWT 阈值不切换怀疑故障。

语言信号：EWT / Expected Waiting Time / 预期等待 / TSP / 饱和 / EWT table / 阈值 / parking level / cut auth / IAA / CCIVR / 518 / 排队位置 / position / Max position / 3226 / 4217 / 63 播 65。

与相邻能力区分：指南怎么录 → 语音指南能力；队列饱和参数（Maximum waiting time）→ 对象调优能力；路由平局用 EWT 归路由与分配规则能力。

## E — 可执行步骤

输入契约：排队话术分档与阈值已定、语言清单已核（nr-07）、518 预置资源完好。

1. 建分档指南：按阈值数建指南并录制装板（实验 720/721/722 三档）。完成标准：vgstat 全部选中
2. 建 EWT 表：6 阈值内逐档填 EWT 值+指南，勾 Cut Auth。完成标准：表保存且阈值升序合理
3. 挂表：pilot 路由规则 Additional 页把 EWT 表填入目标 parking level。完成标准：规则保存
4. 配位次播报（按需）：518 设语言、消息顺序与 Max position，录固定段/变量段并分配板位。完成标准：580 试听通过
5. 制造排队验证：长时间占用座席拉长队列，Navigator 看 EWT 值与所听档位对应。完成标准：跨阈值切换符合设计
6. 位次三连测：验证逐位、步进与超限三个场景。完成标准：第 3 通只闻提示音（Max position 内）

判停点：

- EWT 阈值切换"不及时" → TSP 滚动计算有滞后，勿用单通呼叫下结论，逐步调参（n30）
- 位次超上限听无限提示音 → Max position 上限 100，超限行为是设计而非故障（n32）
- 高位来电者无位次播报 → 语言回退链命中：未管理语言/无默认语言/缺子消息逐层查（n32）
- 要复杂菜单 → IAA 三重上限（5 层 4 选项 8 树）内解决，超出属 CCIVR 书外域（n35/n41）
- 自建同号 518 → 禁止，预置资源只录消息（n27）

输出契约：分档等待播报与位次播报的上线配置（EWT 表+parking level 编排+518 参数）+ 阈值切换与位次测试记录。

## B — 边界

- 位次上限 100、16 语言、消息 3226-4217 为系统预置口径（p377-379）
- EWT 表只能挂 normal 队列 parking level；IAA/CCIVR 地址二选一（p352）
- CCIVR 是外部语音服务器（书中拼写 Contact center Interactive Voice Record 属原文），部署在书外（n41）
- TSP/EWT 只给公式与调参口径，话务量→座席数规划方法书外（n30/n41）
- 实验阈值（10s/20s/60s）与 Max position=2 为实验口径
