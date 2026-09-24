# 酒店与计费垂直方案（Hotel 模式、计费三通道、账号码与内部替代）

## R — 原文依据

> "OHL allows the synchronization with an Hotel application (PMS) … A PMS is an application used in hotels to handle reservations, check-in, check out, billing, and guest database"（p59）
> "Native Front Desk management on ALE DeskPhone, 4 simultaneous sessions … Room to room call barring … 300 sets (rooms + administrative telephone)"（p64）
> "The OXO Connect provides real time metering on IP network • Metering tickets are transmitted in the XML data format … TicketCollector.xml for current tickets"（p78-80）
> "When activated, AOC Pulse based is deactivated (no mix configuration) • No license"（p73/83）
> "The account codes are configured in the account code table (250 max)"（p93）
> "Example of dialing: the manager wants to substitute to his phone (101, pwd 142536) from the workshop phone 110, to call Australia • 66_101_142536_0+61 2 8306 0000"（p96）

出处：OXOCXTE301EN p57-101。

## I — 自述

酒店方案有两条路线，计费有三条通道，记账有一个编码体系，四者组成垂直整套：

**酒店双路线**（p57-68）：

| 路线 | 通道 | 容量/规格 | license |
|---|---|---|---|
| 有 PMS | OHL（Office Link Driver，V24 或 IP）对接 AHL 兼容酒店软件 | check-in 一步激活账单/DDI/邮箱/语言/密码/姓名 | OHL 无 SW license |
| 无 PMS | 前台 ALE DeskPhone 内置 Hotel 功能键 | 4 并发会话、300 话机、房对房闭锁、房态监控 | 无 |

**计费三通道**（p72-91）：

| 通道 | 机制 | 要点 |
|---|---|---|
| Hotel Metering | 货币/VAT/预付/耗尽切断/蜂鸣阈值/3 级 2 阈/脚注 ≤40 字符 | OMC/Metering/Metering |
| Call Accounting Time based | 无 AOC 中继按时长×呼型（国际/国内/本地）出脉冲 | 激活即停 AOC 脉冲（互斥）；免 license；首段起即计 |
| 输出通道 | IP：XML 小票（TicketCollector.xml / 归档 _X.xml）经 OLD 供外部计费应用；V24：打印字段+传输参数 | 全呼叫跟踪在订阅户 Counting 选 All Calls |

**账号码**（p93-95）：表上限 250 条、码最长 16 位；六字段=码/名称/密码要求/身份识别/闭锁类别/小票掩码（0-9、all、Default）；经功能键或编号计划前缀输入。**内部替代**（p96-101）：格式为 前缀 66 + 分机 + 分机密码 + 外拨号码；场景是“全部话机禁国际、仅经理放行”时任何话机可变成经理外呼——账号码在这里充当权限钥匙。

## A1 — 书中案例

**酒店模式部署实验**（p69-75，厂商实验）：

1. 冷复位后进 hotel 模式：OMC Installation Typical 的 Initial Installation Wizard (Hotel)。
2. Hotel Parameters 配 check-in 序列（Deposit/姓名/wake-up/DND/语言/闭锁密码）与默认项。
3. 计费参数：货币、VAT、预付金额、耗尽切断、蜂鸣阈值、3 级 2 阈、脚注（≤40 字符）。
4. Call Accounting Time based 按呼型（Int/Nat/Loc）定义脉冲秒数（激活后 AOC 停用）。
5. 旋转 DDI：客房 DDI 段配 Guest DDI unassigned/assigned（书例 8540 分配给 117 房）。
6. 房态：确认房态前缀（例 88）；Hotel key 查看 Terminal Class 与 Room status。

**Office Link Driver 实验**（p88-91，厂商实验）：

1. OMC Metering 勾选 External metering Activation IP。
2. PC 装 OLD 驱动（管理员身份），安装中选 Metering mode。
3. Configuration Application 填 OXO IP、管理员密码，TestConnection 后启动。
4. 打外呼生成计费小票。
5. 检查 TicketCollector.xml（C:\Users\Public\Public Documents）出现小票记录。

**账号码与内部替代实验**（p97-101，厂商实验）：

1. 建码 123456 名 CLIENT A、掩码 4（小票遮 4 位）。
2. 内部编号计划建前缀 69（Account code new）；用 IPDSP 打电话查小票。
3. 给 104 建可编程键 Account code new 并测试。
4. 内部替代：核对前缀 66（base 1000 指向账号码 1000 SUBSTITUTION）。
5. barring 表 3 删 00 禁止项，经理话机闭锁类别改 3（放行国际）。
6. 锁定话机拨 66-101-142536-0-0210x41100 以经理身份外呼成功（p101）。

## A2 — 未来触发

使用情境：旅馆/民宿/公寓上电话系统；前台要 check-in/check-out 和房态；客房电话计费与预付切断；没有 PMS 怎么办；外呼费用记到客户/项目账号；经理不在办公室要发国际长途；小票要遮号码位。

语言信号：酒店 / hotel / PMS / OHL / check-in / 入住 / 房态 / 房对房闭锁 / wake-up / 预付 / deposit / 计费 / metering / TicketCollector / 账号码 / account code / 内部替代 / substitution / 66 前缀。

与相邻能力区分：计费依赖的中继通道归 SIP 组网能力；小票经 OLD XML 给外部应用后如何入财务系统在书外；多实体分账场景（两公司共享系统）归多实体能力。

## E — 可执行步骤

输入契约：酒店规模（客房数/前台并发）、有无 PMS 及其 AHL 兼容性、币种与费率策略、记账对象清单。PMS 兼容性未知 → 判停先查 hospitality ecosystem PDF（DSPP）。

1. 选路线：有 AHL 兼容 PMS 走 OHL（V24/IP）；没有则用前台话机内置 Hotel 键。完成标准：路线成文
2. 进 hotel 模式：冷复位后跑 Wizard Hotel（默认 Business 模式，直接跑不生效）。完成标准：Hotel 参数可配
3. 配 Hotel Parameters：check-in 序列、Do at check-in、房态定时、默认语言/闭锁/wake-up、房对房闭锁。完成标准：参数落表
4. 配计费：Hotel Metering 全参数；无 AOC 中继启用 Call Accounting Time based（确认放弃 AOC）。完成标准：计费通道可用
5. 配输出：IP 走 OLD（装驱动、TestConnection、核 TicketCollector.xml）或 V24（传输参数）。完成标准：小票落地
6. 配旋转 DDI 与房态：Guest DDI unassigned/assigned；房态前缀与 Hotel key 字段核对。完成标准：入住流程走通
7. （记账需求）建账号码表 + 前缀/功能键入口；内部替代场景核对 66 前缀与闭锁配合。完成标准：小票带码、替代外呼通
8. 验证：试入住/退房、试呼计费小票、锁定话机替代外呼。完成标准：三场景闭环

判停点：

- 冷复位会清数据 → 生产改造前必须完整备份（n08：默认 Business 模式必须冷复位切 hotel）
- 已有 AOC 脉冲计费的站点 → 不要开 Call Accounting Time based（互斥，n09）
- 小票脚注超 40 字符、账号码超 250 条 → 超规格，裁需求
- PMS 不在兼容清单 → 停，先确认 DSPP/生态 PDF 或走无 PMS 路线

输出契约：酒店路线与参数记录 + 计费通道与小票样例 + 账号码表与替代场景测试结论。

## B — 边界

- 酒店容量口径：300 话机（客房+行政）、前台 4 并发会话（p64）；Multiset 支持 hotel 模式
- 脉冲须由语音运营商传输，否则需外部时长计费器（p72）；外部计费应用的入账逻辑在书外
- PMS 兼容清单以当期 hospitality ecosystem PDF 为准（书引 2025-11 版，跨版本交付需重新核对）
- 实验密码/分机号（142536 等）为实验口径；内部替代密码与远程接入码是两套体系，勿混配
- 退役/模式切换：冷复位不擦自签证书（n40，推断：净化需另行处理）
