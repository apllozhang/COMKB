# 协作会议（ACS 服务器配置、三类会议、角色权限、数据会议）

## R — 原文依据

> "The call routing rules are called DAS rules. DAS rules are a set of up to 20 Unix regular expressions ... applied in order ... the output of each rule is the input to the next one."（p299）
> "The conference access is granted through a 7 digits access code which is unique. A specific code is generated for leaders and another one for participants"（p266）
> "PARTICIPANTS CANNOT: Make presentations or share files • Invite other participant • Control the conference • End the conference call"（p270）
> "To upload a Microsoft Office file (doc, docx, ppt, pptx, xls, xlsx) as a presentation, a DCS (Document Conversion Server) is mandatory."（p344）

出处：OPENXTE301EN p264-362。

## I — 自述

会议能力按 ACS（会议服务器）组织，配置与使用分四块：

1. **桥号成对**：每语言一号——OXE 侧 External Voice Mail 建（例 31250 英/31260 法），OT 侧 TUI application 建对应条目（两端号码一致，配语言/邀请标签/可选 Dial in number）
2. **服务器四项设置**：系统选项（国际 00/国内 0/国家码 33/Smart mail relay/默认 Web 客户端 OTCWeb）、SIP 代理（Outbound 指向 OT IP:5260、Inbound Realm/Server/Port）、DAS 规则、电话格式规则（Extension Pattern 按分机位数）
3. **三类会议与角色**：ad-hoc（通话中加人即建）/ scheduled（预约，可配领导者开局等选项）/ reservationless（长期占用同一桥码）；7 位唯一访问码分领导者码与参与者码；领导者全功能、参与者受限（不可演示/邀请/控制/结束）；可选密码（音频 ≥5 位数字、在线 ≥5 字符）且不进邀请邮件
4. **使用侧**：OTC PC 预约（People/Documents/Passwords/Options）、Outlook 加载项免预约、One Touch 入会（邀请标签以 <*> 开头）、远程控制（Give/Take back control）、DTMF 控制（参与者 ##1/##3/##4，领导者 ##91/##92/##93）
5. **权限治理**：用户级两级禁用（Enable sharing off 或 Enable collaboration off），仅作用于 ad-hoc 与点对点会话，scheduled/reservationless 始终全量

文档规则：免 DCS 可演示 pdf/bmp/gif/jpg/jpeg/png；Office 六格式必须 DCS；presentation 参与者不可下载、attachment 可。

## A1 — 书中案例

**会议服务器配置与数据会议实验**（p308-362）：

1. OXE 建 31250（Conf-EN）与 31260（Conf-FR），External Gateway 指 SIP 网关
2. OT 侧 TUI application 改默认 Conferencing 条目并新建 FR 条目
3. 进会议服务器管理台核对系统选项（00/0/33、邮件中继、OTCWeb）
4. 核对 SIP 代理（Outbound=OT IP:5260、Inbound 三项、Users 自动出现）
5. Default 域录入法国 10 条 DAS 规则（顺序敏感）
6. 电话格式规则按 5 位分机计划填 Extension Pattern
7. OTC PC 预约会议：配名称/类型/时间/周期、加人与定角色、传文档、设密码
8. Outlook 验证 Include Conference 图标（加载项未激活时按 p349 处理）
9. 配 One Touch（Dial in number 规范格式、Label 以 <*> 开头、Toll-free 勾选）
10. 协作限制实验：对 Connection 用户先后关 sharing、collaboration 并观察 ad-hoc 会话变化

## A2 — 未来触发

使用情境：搭会议桥与邀请邮件；参会人能不能共享/录制；会议密码怎么给；One Touch 一键入会；要管住某些用户的协作能力；视频会议怎么入（SIP URI）。

语言信号：会议 / conference / ACS / 会议服务器 / 桥号 / TUI / 访问码 / access code / 领导者 / leader / DTMF / One Touch / toll-free / 协作限制 / Enable collaboration / DAS / Dial by URI。

与相邻能力区分：

- Office 文档演示不了 → DCS 能力（路由卡）
- 访客浏览器入会 → OTC Web 能力（路由卡）
- DAS 规则与证书的底层配置 → 远程接入能力
- 日历邀请同步 → 日历同步能力

## E — 可执行步骤

输入契约：语言清单（每语言一号）、分机位数、邮件服务器（Smart mail relay）、用户协作治理需求、MCU 形态（内置 AMS）。

1. 桥号两侧成对：OXE External Voice Mail 与 OT TUI application。完成标准：两端号码一致、邀请邮件含桥号
2. 服务器四项设置核对（系统选项/SIP 代理/DAS/格式规则）。完成标准：试拨号码格式正确
3. 授权用户：Desktop 与 Conferencing 许可。完成标准：用户可建会
4. 预约链路验证：OTC PC 建会发邀请、三端入会（PC/手机/浏览器）。完成标准：URL/桥号/SIP URI/访问码齐全
5. One Touch 与密码策略：Label 以 <*> 开头、密码不进邮件由领导者自行告知。完成标准：一键入会与密码行为符合预期
6. 治理策略：按用户配两级禁用并验证作用范围。完成标准：scheduled 不受影响、ad-hoc 生效

判停点：

- 需求要"多方同屏"（continuous presence）→ 内置 AMS 只支持 Active talker，且外部 Radvision/LifeSize 已淘汰，另寻方案
- Connection 用户要 p2p/临时视频 → 不支持（仅预约视频），先分清用户类型再谈需求
- 参会人没有密码 → 设计如此（密码不入邀请邮件），领导者另行告知；音频密码自动套用到录音
- 协作限制"不生效" → 查场景豁免：scheduled/reservationless 全量、S4B/Teams 集成与 OT networking 不可用

输出契约：会议服务器配置存档（四项设置+桥号）+ 角色权限与治理策略清单 + 端到端会议验证记录。

## B — 边界

- DAS 规则仅法国口径、顺序重要且可多条同中（改动前先理解整链，n08）
- 录制仅领导者发起、只录音频、开场结束有提示音，WAV 下载权限受限（p270 语境）
- OTC Web 端无录制/视频/白板等能力（见 OTC Web 路由卡）
- 会议号 31250/31260、访问码规则、otAdmin/admin8770 均为实验口径
- 视频终端兼容性与最新 MCU 支持以当期技术文档为准（书内已标 Radvision/LifeSize 淘汰）
