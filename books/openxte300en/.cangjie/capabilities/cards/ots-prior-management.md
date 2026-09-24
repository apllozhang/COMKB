# Prior management（号码段、前缀、拨号规则、UDAS、会议桥与 DAS）

## R — 原文依据

> "Range of numbers from 31000 to 31499 (including users, voice mail, attendants, …) are declared belonging to OXE."（p216）
> "Dialing rule(s) are used to add automatically the outbound prefix when an external call (by name or number) is performed."（p220）
> "SYNCHRONIZATION DATE, TIME AND PERIOD MUST BE SET. SYNCHRONIZATION PERIOD MUST BE EQUAL OR UPPER TO 1. ... NEVER SET PERIOD TO "0""（p243）
> "DAS rules are mandatory and are country dependant. The configuration proposed will be for France."（p253）
> "AFTER OT R2.1, CONFIGURATION OF THE ATENDANT PREFIX IS MANDATORY FOR THE START UP OF THE EXTENSIBLE SERVICES."（p238）

出处：OPENXTE300EN p213-254。

## I — 自述

Prior management 是拨打行为正确性的总闸，六块结构：号码段、前缀服务、语音邮件号、拨号规则、UDAS 目录同步、会议桥与 DAS 规则。

业务号码对照（书内口径，实验值）：

| 业务号 | 用途 | 承载/去向 |
|---|---|---|
| 31000-31499 | 用户/留言/话务台/缩位号 | OT 侧 Ranges 页签声明归属 OXE |
| 31200 | 语音邮件 TUI | OXE 侧走外部网关 11（Mule 5040） |
| 31250 / 31260 | 会议桥（英/法，每语言一条） | OXE 侧走外部网关 10（ESS 5260） |
| 31700 / 31710 | SIP proxy 用户 | 向导后自动生成，仅需核对 |

前缀服务（两侧同值原则）：转发/溢出/取消/话务台等前缀与 OXE 同名前缀取同值；教材给的 51/52/53/54/41/9 是法国默认示例，必须核对现场 OXE 值。硬规则：OT R2.1 起话务台前缀必配，否则可扩展服务起不来，补配后以 root 执行 service wireald restart。

拨号规则行为分层：按姓名呼打——所有客户端自动加外呼前缀；按号码呼打——仅 OTC PC 与 OTC Mobile（客户端下载规则文件），话机与视频设备必须手拨前缀；会议呼叫走 DAS Rules。参数：外呼前缀 0 或 9、最小长度=拨号计划长度+1、例外长度。

UDAS 同步机制：OXE 话簿、内部目录、外部 LDAP 三路数据源单向倾倒进 PostgreSQL 同步库，客户端检索只查同步库；同步日期、时间、周期必须都设置，周期至少 1（1=每天）、绝不能为 0。

DAS 规则（会议服务器侧）：强制且按国家定制；规则与域名绑定；声明顺序重要且多条可同时命中（例 1+2、4+6）；Phone Formatting Rules 的 Extension Pattern 正则位数须与拨号计划一致。

## A1 — 书中案例

**prior management 实验**（p235-254）：

1. OT 侧 OXE 声明的 Ranges 页签加号段：min 31000、max 31499。
2. Telephone Prefixes 按现场 OXE 值配转发、取消与话务台前缀。
3. 话务台前缀补配后以 root 重启可扩展服务（wireald）。
4. Topology/VMS 核 defaultVmsLS 类型为 Local Storage。
5. TUI application 把 Voice Mail 索引设为 31200。
6. OXE 侧 External Voice Mail 建 31200 走外部网关 11。
7. Dialing rule 1 配外呼前缀与最小长度（拨号计划长度加一）。
8. UDAS 两目录启用并设同步日期、时间、周期（至少 1）。
9. TUI application 核建 Conferencing 31250 并另建 31260。
10. OXE 侧对两个会议号各建一条 External Voice Mail 走外部网关 10。
11. 会议服务器管理台核 System options 与 SIP Proxies（出站代理 5260）。
12. DAS Rules 按本国拨号计划改写并保序录入十条法国口径。
13. Phone Formatting 正则按拨号计划位数核对（5 位计划口径）。

## A2 — 未来触发

使用情境：外呼要自动加 0；按名呼打能出去按号不行；目录查不到新同事；开会进不去会议桥；话务台相关服务起不来。

语言信号：号码段 / Ranges / 前缀 / prefix / 拨号规则 / dialing rule / UDAS / 目录同步 / 同步周期 / 31200 / 31250 / DAS rules / 会议桥 / conference / wireald / 格式化规则。

与相邻能力区分：承载层（trunk/外部网关）归节点声明与 SIP 能力；邮箱行为与通知归语音邮箱能力；监督组进出组前缀见监督组路由卡。

## E — 可执行步骤

输入契约：现场拨号计划（号段/位数/外呼前缀）；OXE 现行前缀表；国家制式（DAS 与格式规则按国改写）；目录源清单（OXE 话簿/内部/LDAP）。

1. 号码段：OT 侧 Ranges 覆盖 OXE 全部用户/留言/缩位/话务台号。完成标准：分机与 31200 均正确归 OXE
2. 前缀两侧同值核对；话务台前缀必配并重启 wireald。完成标准：可扩展服务正常启动
3. 语音邮件与会议号：TUI application 与 OXE External Voice Mail 成对配置。完成标准：进得留言与会议桥
4. 拨号规则：前缀、最小长度、例外长度三项。完成标准：按名/按号呼打行为符合 p221 分层表
5. UDAS：激活、周期至少 1、手动强同步一次。完成标准：检索命中新增数据
6. 会议服务器：System options、SIP Proxies、DAS、格式规则四项核对。完成标准：按本国制式就绪

判停点：

- 目录永远陈旧 → 同步周期被设 0 或日期时间没填；改至少 1 并强同步
- 会议呼出不通 → DAS rules 缺失或顺序错；按国家重排并整体复查
- 前缀照抄教材 51/52/53/54/41/9 → 法国口径示例，必须核对现场 OXE 值
- 话机按号呼打不自动加前缀 → 设计如此（仅 OTC PC/Mobile 自动），话机须手拨
- UM 型语音邮件号 → 本卡只管本地存储口径；UM 声明在另一培训（书外）

输出契约：号码路由设计落位清单 + UDAS 同步状态记录 + DAS/格式规则配置快照。

## B — 边界

- 实验口径（生产按现场拨号计划替换）：外呼前缀 0、最小长度 7、号段 31000-31499、DDI 首外线 33210N41000（N=POD 号）、首内线 31000、跨度 500。
- 教材默认法国制式（前缀值、国码 33、00/0 口径、DAS 十条）——非法国站点必须逐项本地化（n19/n21）。
- UDAS 检索只打 PostgreSQL 同步库，不直接查源目录；同步没配好目录就是旧的（p223）。
- 会议服务器管理走专用 WBM 界面，不经 8770 客户端（p246）。
- Dialing rule 与 DAS rule 是两套规则：前者管一般外呼，后者只管 Conference 侧（g15）。
- 邮件中继主机（Smart mail relay）等 System options 依赖客户邮件基础设施，值由客户提供。
