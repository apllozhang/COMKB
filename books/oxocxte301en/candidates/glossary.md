# 术语/缩写/产品名候选 — OXO Connect Advanced (OXOCXTE301EN Ed18)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 62 条（六类：concept 27 / role 5 / subscription 5 / product 11 / protocol 9 / resource 5）。DDI、RSL、NMC、CTI、ADL、RPN、PLI、GSM、HAN（书中只给 Home Area Network）等缩写书中未给全称或未中文注明的，full_name 如实省略或只录原文展开，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: OMC
  category: concept
  source_pages: p23-32 及全书
  source_quote: |
    "Make a connection to the system with OMC in Expert mode with server authentication … Choose 'Expert' menu … Use LAN/WAN connection" (p28)
  definition: |
    OXO 的 Windows 管理工具：Expert 模式经 LAN/WAN 连接并做服务器认证；对象树覆盖 Hardware and Limits、Numbering、External Lines、Subscribers、Voice Processing、ACD-SCR Services、Multiple Automated Attendant、Security、System Miscellaneous 等；内置 Webdiag 入口与 MLAA 图形树编辑器；兼容老版本 FTP 传输（p300）。
  alias_or_related: 与 g33 Webdiag、g46 LoLa 配套；首连参数见 p28
  tags: [concept, management-tool]

- id: g02
  term: ARS (Automatic Route Selection)
  category: concept
  source_pages: p194-205
  source_quote: |
    "During call routing, the ARS (Automatic Route Selection) provides: • An automatic selection of the optimal route (Trunk Group) according to the dialed number and the time of the call (optional) • An overflow to another route if the most appropriate one is busy or out of service"
  definition: |
    自动选路：按被叫号码（与可选时段）自动选中继组，饱和/故障溢出；对用户透明；适用任何中继组（公/私）、呼叫（语音/数据）、接入（模拟/数字/IP）与拨号方式；三表协作（编号计划→ARS 表→中继组列表），兼做号码变换（加/吸收/替换/透明）。
  alias_or_related: Internal ARS（g03）为其反转用法；ARS 表字段见 p196
  tags: [concept, routing]

- id: g03
  term: Internal ARS
  category: concept
  source_pages: p225-231
  source_quote: |
    "Aim of the internal ARS • Allows us to manage several destinations for a single DDI according to days an time ranges"
  definition: |
    用 ARS 机制把一个入站 DDI 按日组+时段路由到不同内部目的地（分机/寻线组消息）；实现技法=虚拟 Provider+Local 索引中继组列表+Substitute 替换为分机号（替换前缀随后在内部编号计划分析）。
  alias_or_related: Day Groups/Hours/Providers-Destinations 屏（p204/231）
  tags: [concept, routing, ddi]

- id: g04
  term: Entity（多实体）
  category: concept
  source_pages: p242-248
  source_quote: |
    "Sharing an OXO Connect between 4 companies • The system supports 4 Entities … Call restriction between user of different company … Attendant Group • Common for all entity • No call restriction" (p243-244)
  definition: |
    系统内最多 4 个逻辑公司：每实体独立 MoH（保持方实体决定播放哪个，每段 ≤10 分钟）、可选实体间呼叫禁止（连带限制立即/忙转、RSL 键、个人代接、文本/语音邮箱）；话务员组全实体公共且不受限；计费小票含实体信息。
  alias_or_related: 伪多公司（g05）为其扩展用法
  tags: [concept, multi-tenant]

- id: g05
  term: Pseudo multi-company（伪多公司）
  category: concept
  source_pages: p249-251
  source_quote: |
    "Two companies want to share an OXO Connect for their calls management … Each company will be able to dial the same main trunk group prefix … Each company will take their own external lines to avoid problems according to metering bills" (p249)
  definition: |
    两家公司共享一台 OXO：用流量分担链路类别配对（话机类别=本公司中继组类别）+流量分担矩阵直线+ARS 透明线实现"同一外拨前缀、各走各的外线、账单分离"；外拨占线以 Char 字符（1/2）在话机显示确认。
  alias_or_related: 依赖 g04 实体隔离与 ARS（g02）
  tags: [concept, multi-company]

- id: g06
  term: Multiset / Twinset
  category: concept
  source_pages: p184-189
  source_quote: |
    "the association of two or three sets (wired or mobile) for the same user • One primary set and a maximum of two secondary sets … Usually composed of 2 sets, a primary wired one and a secondary mobile DECT • Called Twinset" (p185)
  definition: |
    同一用户 2-3 台话机（1 主+最多 2 副）：共享主站目录号与服务级别、忙态联动；副站可用自己目录号收话、继承主站 14 项功能；常见形态主有线+副 DECT 即 Twinset。注意与 Rainbow 侧同名概念（虚拟副站）不同物。
  alias_or_related: MLTSETRING 控制空闲副站来话铃型（p188）
  tags: [concept, terminals]

- id: g07
  term: Hot Desking (HDP / HDU)
  category: concept
  source_pages: p173-177
  source_quote: |
    "allowing any Hot Desking User (HDU) to use any Hot Desking Position (HDP) in the company • The employees retrieve from a 'free' desk phone their personal environment and associated functionalities" (p174)
  definition: |
    共享话机资源：HDU（用户）在任意 HDP（位子）登录（前缀 683/682 或软键）取回个人环境（VM/呼叫日志/IM/路由规则/键配置等）；容量 200+200；监督经 Webdiag 与 OMC 双通道，可强制注销。
  alias_or_related: 计费与抢占规则见 p174-175
  tags: [concept, mobility]

- id: g08
  term: Nomadic mode（游牧模式）
  category: concept
  source_pages: p465-468
  source_quote: |
    "A nomadic set is a set used to substitute the local one. It can be any type of set but mostly a cellular phone … The local set can be either physical or virtual" (p465)
  definition: |
    游牧话机（多为手机）替代本地话机（本地可物理可虚拟——虚拟=只有系统内号码的远程工作者）；经 VMU 远程定制选项 6 激活/停用/改目的地；CLI 按主叫身份规则发送；计费小票含游牧信息。SIP 话机不支持。
  alias_or_related: 远程替代（g09）共用远程接入体系
  tags: [concept, mobility]

- id: g09
  term: Remote substitution（远程替代）
  category: concept
  source_pages: p469-471, p477-480
  source_quote: |
    "Remote Substitution DDI number:0201531050 + DTMF Code … #100 to #199 → 100 to 199 • #9 → to 9 Attendant" (p470)
  definition: |
    拨远程替代 DDI → 远程接入码 → 分机号 → 该分机密码 → 以该分机身份外呼；呼内部号加 # 前缀（#100-#199）经内部 ARS 回环。ACC 与远程 VM 接入共用同一密码菜单。
  alias_or_related: p383 ACC 两级控制
  tags: [concept, mobility]

- id: g10
  term: Account code
  category: concept
  source_pages: p93-95
  source_quote: |
    "An account code is used to charge the cost of an external communication to a clients' account or a project … This code is printed on the metering ticket … (250 max)" (p93)
  definition: |
    把外呼费用记到客户/项目账号的编码：打印在计费小票上；表上限 250、码 ≤16 位；可要求密码/身份识别/指定闭锁类别/小票掩码位数；经功能键或编号计划前缀输入。内部替代场景还把它当"权限钥匙"用。
  alias_or_related: Internal substitution（书中合并成一章，p96-101）
  tags: [concept, metering]

- id: g11
  term: OHL (OXO Connect Hotel Link) / AHL
  category: concept
  source_pages: p65
  source_quote: |
    "Hotel Link OHL (OXO Connect Hotel Link) • Office Link Driver • This driver offers a hotel link between OXO Connect and hotel applications compatible with AHL (Alcatel Hotel Link) • No SW license linked to OHL"
  definition: |
    经 Office Link Driver（V24 或 IP）把 OXO 与 AHL 兼容的酒店应用（PMS）对接：check-in/房号/语言/清扫状态/迷你吧/实时计量等全部由酒店软件操作；OHL 本身无软件 license；PMS 适配清单在 DSPP/hospitality ecosystem PDF。
  alias_or_related: 无 OHL 时前台话机内置 Hotel 功能键（p63）
  tags: [concept, hospitality]

- id: g12
  term: PMS (Property Management System)
  category: concept
  source_pages: p59, p65
  source_quote: |
    "A PMS is an application used in hotels to handle reservations, check-in, check out, billing, and guest database" (p59)
  definition: |
    酒店管理系统：管预订、入住/退房、账单与客史；在本书架构中经 OHL 驱动与 OXO 同步（须 AHL 兼容；兼容性查 DSPP 与 al-enterprise.com 的 hospitality-ecosystem PDF，2025-11 版）。
  alias_or_related: g11
  tags: [concept, hospitality]

- id: g13
  term: Automated Attendant (AA)
  category: concept
  source_pages: p405-421
  source_quote: |
    "The automatic attendant route the incoming calls, via a tree structure, towards the required service (Information Messages, Set, Hunting group…)" (p406)
  definition: |
    集成自动话务员：两棵树（白天 Normal/夜间 Restricted）、每树两级 100 节点、每级 10 选、4 语言；定制树与语音指南需 license；支持盲转/半监督（AATypTrf）、免费拨号（AAGrDialng/AAGrTransf）。
  alias_or_related: MLAA（g14）为其多树扩展
  tags: [concept, call-processing]

- id: g14
  term: MLAA (Multiple Automated Attendant)
  category: concept
  source_pages: p427-442
  source_quote: |
    "Integrated application, based on ACD engine … Incoming calls routed according to CLI/DID number … A maximum of 5 tree structures are manageable" (p428)
  definition: |
    基于 ACD 引擎的多树自动话务员：按 DID 和/或 CLI 路由来话到最多 5 棵树（3 级、每级 10 选、每树 4 语言）；动作八种；OMC 图形编辑器配置后传输到服务器；语音总量硬上限 12000 秒。
  alias_or_related: 端口与 ACD 共享 16（p431）
  tags: [concept, call-processing]

- id: g15
  term: SCR (Smart Call Routing)
  category: concept
  source_pages: p450-458
  source_quote: |
    "SCR is a feature for extending call routing capabilities • The routing mechanism is based on … CLI Number, DDI Number, DTMF Client Code and the Opening and closing time" (p451)
  definition: |
    智能路由：按 CLI/DDI/DTMF 客户码/开闭时间把来话路由到 ACD 组（带/不带客户码）、MLAA 组、本地/外部目的地；10000 条规则，编辑器内嵌 ACD 呼叫路由表；X 为通配符；错误时走备份目的地。
  alias_or_related: 客户码提示音 107-807.wav 与 ACD 共用
  tags: [concept, call-processing]

- id: g16
  term: Personal Assistant（个人助理）
  category: concept
  source_pages: p385-387
  source_quote: |
    "It is a mini–Automated Attendant for each subscriber offering different choices … 'Your correspondent does not answer, press 1 to leave a message …'" (p385)
  definition: |
    每订阅户的迷你自动话务员：预定义问候语+三个转接目的地（内部/外部/移动）+转话务员；半监督转接；系统开关 noteworthy PerAssAlwd（默认 00 禁用），可远程定制（选项 2）。
  alias_or_related: 远程定制菜单 p388
  tags: [concept, voicemail]

- id: g17
  term: Stations groups supervision（站群监督）
  category: concept
  source_pages: p111-115
  source_quote: |
    "Allows you to monitor multiple directory numbers simultaneously … the supervisor is notified by 3 ways • A pop-up display … • An audio tone … • The Groupware supervision key blinking" (p112)
  definition: |
    一台监督话机同时监控最多 8 个目录号：来话以 pop-up（默认 5 秒）+音调+键闪烁三路通知，可应答或关闭；监督方仅 DeskPhones；系统上限 50 键；private 呼叫不可监督。
  alias_or_related: TmpMenLTim/NotiAppTim 计时 noteworthy（p113）
  tags: [concept, groupware]

- id: g18
  term: Cloud Connect (CCI)
  category: concept
  source_pages: p262-289
  source_quote: |
    "On-demand remote management of OXO Connect systems • VPN IP connectivity • System software update … Remote Access to customer system information • Licenses, hardware, devices, log…" (p263)
  definition: |
    ALE 云基础设施：OXO 主动发起永久 HTTPS+按需 VPN 双连接（免改防火墙规则）；承载舰队监控、Inventory、软件更新、远程 VPN 调试；注册自动、免 license、默认启用；门户=Business Store+Fleet Dashboard+OXO Connectivity。
  alias_or_related: g19/g20 两门户；SW 更新指示灯 p271
  tags: [concept, cloud]

- id: g19
  term: Fleet Dashboard
  category: concept
  source_pages: p267-268, p272, p276-280
  source_quote: |
    "The Fleet Dashboard portal allows you to: • Monitor your installed base • See your support contracts • Manage contracts" (p267)
  definition: |
    舰队门户（OXE 与 OXO 通用）：按客户/产品/版本看安装基础与 SA 合同、看 UTL/版本/最后紧急告警；Inventory 服务（许可证/终端/中继/机框，GDPR 匿名，数据每日刷新，OXE R12.2 MD1 与 OXO R3.0 起）；批量软件更新（advanced 权限）。
  alias_or_related: Inventory 数据经 Datalake 每日刷新（p276）
  tags: [concept, cloud]

- id: g20
  term: OXO Connectivity
  category: concept
  source_pages: p265-266, p273-275
  source_quote: |
    "VPN configuration … Watchdog, OMC reset… Hardware, Devices list, Counters, SIP gateways, Licenses … DSP statistics about SIP trunks, IP Phones… System operational, default passwords found… Logs about sessions, CC Operation" (p266)
  definition: |
    单系统云门户（可 standalone）：VPN 配置、Watchdog/OMC 复位、硬件设备许可清单、DSP 统计、默认密码检出、会话与 CC 操作日志、单台软件更新、SD 卡备份/恢复监控；系统定位用 CC-Prd-id（<R3.0）/CPU-id/客户参考。
  alias_or_related: g18
  tags: [concept, cloud]

- id: g21
  term: Noteworthy address
  category: concept
  source_pages: p574-578
  source_quote: |
    "The Memory Read/Write of Noteworthy addresses (also called labels or flag) are used to configure global parameters for the Server … 4 types of memory zones … Timer Labels • Debug Labels • Other Labels … Numeric Addresses (values in hex format)" (p575)
  definition: |
    服务器全局参数的内存读写地址（labels/flags）：timers/debug/other/numeric 四类；写错可致系统恶化、cold reset 复位、清单以 TC1398 为准。书内出现的实例：PerAssAlwd、DivRemCust、AATypTrf、MLTSETRING、TmpMenLTim、NotiAppTim、AutoPwdChk、VMUMaxTry、MLAA_MSG、sipphone_sess_tim、Auto_Reset。
  alias_or_related: 实例取值散见 principle.md（p26/p28-29/p48 等）；修改流程在 g47 Webdiag 与 OMC Memory Read/Write
  tags: [concept, tuning]

- id: g22
  term: DTLS (Datagram Transport Layer Security)
  category: concept
  source_pages: p359-364
  source_quote: |
    "Encryption of signaling channel for ALE VoIP devices (DTLS Datagram Transport Layer Security) … Up to 300 DTLS connections • License free … Available only with platform OXO Connect Evolution" (p360)
  definition: |
    ALE VoIP 话机信令通道加密（TLS 1.2）：语音包仍明文（非 SRTP）；仅 OCE；Generic（零触摸）与 Specific（锁定端点）两证书模式；跨系统移动话机需清 TrustList（三法）；DECT 空口加密另为一事（p364）。
  alias_or_related: 与 SIP TLS/SRTP（g38）分层
  tags: [concept, security]

- id: g23
  term: SIP Registrar / B2BUA
  category: concept
  source_pages: p140-141
  source_quote: |
    "Each time a SIP end-device connects, it is registered on a 'Registrar' server … OXO Connect is a Registrar for its SIP client" (p140)
    "The OXO Connect is a B2BUA Back-to-Back User Agent for the SIP calls" (p141)
  definition: |
    注册面：SIP 终端向 Registrar 注册（可 Digest 401 认证），位置服务器映射 SIP 地址↔IP；OXO 是自己 SIP 客户端的 Registrar。呼叫面：OXO 作 B2BUA 中转。注册失败入历史表 REGISTRATION_REJECT。
  alias_or_related: 端口 5059（p153）
  tags: [concept, sip]

- id: g24
  term: RTP Proxy / Direct RTP / Codec pass-through
  category: concept
  source_pages: p144-148
  source_quote: |
    "RTP proxy: when two calls legs are established using same codec and framing, packets are only routed by OXO. No compression/decompression is done. … Direct RTP: Media flows are established directly between the endpoints of the call. It is the most optimal solution" (p148)
  definition: |
    媒体三处理：DSP 通道（压缩解压）→RTP proxy（同编解码同 framing 仅路由，升容量降 CPU）→Direct RTP（端点直连最优）；编解码透传开关（话机侧/中继侧各自独立）决定是否限定 OXO 六编解码；TLS/SRTP 下 Direct RTP 不可用。
  alias_or_related: Proxy RTP Fixed ports（p146）
  tags: [concept, media]

- id: g25
  term: DECT Cluster（集群）
  category: concept
  source_pages: p506, p517
  source_quote: |
    "Cluster = DECT area where all base stations are synchronized together. Bases from any other cluster cannot be synchronized with any base on this cluster. The cluster membership is imposed by the OXO Connect" (p506)
  definition: |
    空口同步的基站组：切换（handover）只在集群内；站点（Site，地理位置，最多 20）下可含多集群（每站最多 8）；成员关系由 OXO 强加；Automatic 模式自动管集群选主/备主（推荐）。
  alias_or_related: 同步树、Relay xBS（p508/510-511）
  tags: [concept, dect]

- id: g26
  term: Site Survey Kit (SSK)
  category: concept
  source_pages: p529-534
  source_quote: |
    "A site survey is mandatory before of a product offer or before installation in order to determine the number and position of Dect base stations" (p530)
  definition: |
    DECT 站点勘测工具箱：2 台勘测专用 xBS（固件与生产不同）+8dBi 天线+充电宝+2 话机等；流程=装固件与国家频率→电池摆位→话机 site survey 测衰减→-72 dBm 划语音质量区→通话测音质；手册 8AL90874USAA。
  alias_or_related: PARK/DNR 实验值见 p531
  tags: [concept, dect]

- id: g27
  term: SUOTA
  category: concept
  source_pages: p526
  source_quote: |
    "Software Update Over The Air for DECT handsets (SUOTA) … Available through 8378 DECT IP-xBS and 8379 DECT IBS … Mode automatic/manual/off is configured via WebDIAG"
  definition: |
    DECT 话机空中软件升级：经 8378 IP-xBS/8379 IBS；自动/手动/关三模式（WebDIAG 配置）；并发 50、下载 4-8 小时、话务优先；swap 须充电座。仅 OCE 与 PowerCPU EE。
  alias_or_related: 适配话机 8214/8234/8244/8254/8262/8262EX
  tags: [concept, dect]

# ── 二、角色 (role) ──

- id: g28
  term: installer
  category: role
  source_pages: p28, p167, p560, p572
  source_quote: |
    "Login: installer • Password: see Installer password" (p167)
  definition: |
    OMC/Webdiag 的主管理角色：Webdiag 全功能调试、证书管理、抓包、DECT 管理、密码重置等均用 installer 登录；首连密码 pbxk1064（仅首连）；Console 口重置机制见 p325。
  alias_or_related: g29 operator、g30 manufacturer
  tags: [role, access]

- id: g29
  term: operator（话务员/操作员会话）
  category: role
  source_pages: p570
  source_quote: |
    "Through Operator session, it is possible •To upload music on hold for each entity •To supervise and log off Hot Desking phones sets and users •To check and unlock blocked user accounts"
  definition: |
    Webdiag/MMC 的操作员角色：上传各实体 MoH、监督并注销 Hot Desking、解锁被锁用户账户；MMC 话务员会话（Expert 菜单）还是 MLAA/AA/ACD 语音的录制入口。
  alias_or_related: g28/g30
  tags: [role, access]

- id: g30
  term: manufacturer
  category: role
  source_pages: p560, p568
  source_quote: |
    "Operator and Manufacturer sessions are also available" (p560)
  definition: |
    Webdiag 第三种会话（ALE 制造商/技术支持专用）：如 ID 页的内部系统标识（ID）即"技术支持管 OMC 制造商密码"时要提供的标识。
  alias_or_related: g28/g29
  tags: [role, access]

- id: g31
  term: Supervisor（监督者）
  category: role
  source_pages: p112, p114
  source_quote: |
    "When the supervised set receives a call, the supervisor is notified by 3 ways … The supervisor can answer the call or close the notification" (p112)
  definition: |
    站群监督中的监督方：仅限 DeskPhones 机型；配 Supervision Groupware 键（最多 8 号码）+Audio Signal Supervision 开关键；3 方会议/应用内/ACD 登录时不能应答通知。
  alias_or_related: SCR 场景另有 Supervisor Console license（p458）
  tags: [role, groupware]

- id: g32
  term: HDU / HDP
  category: role
  source_pages: p174-176
  source_quote: |
    "any Hot Desking User (HDU) to use any Hot Desking Position (HDP)" (p174)
  definition: |
    Hot Desking 的两个角色：HDU=共享用户（Add 时选 Hot Desking User 类型），HDP=共享话机位（空闲话机勾 Hot Desking set）；一 HDP 同时只容一 HDU，抢占自动注销前者。
  alias_or_related: g07
  tags: [role, mobility]

# ── 三、许可/订阅 (subscription) ──

- id: g33
  term: HDU 计费包
  category: subscription
  source_pages: p174
  source_quote: |
    "License required • Hot Desking User: 2 are free of charge, then by package of 50 • Max capacity: 200 Hot Desking Positions / 200 HD users"
  definition: |
    Hot Desking license 口径：HDU 前 2 个免费，之后按 50 一包；容量上限 200 HDP/200 HDU。
  alias_or_related: g07/g32
  tags: [subscription, licensing]

- id: g34
  term: IP-DECT 用户 license
  category: subscription
  source_pages: p495
  source_quote: |
    "Licenses • Licenses for IP-DECT users" (p495)
  definition: |
    IP-DECT 解决方案按用户上 license（TDM IBS 轨无此项说明）；DECT 用户总量上限 200（与 IBS 轨共享口径，p494-495）。
  alias_or_related: g25/g43
  tags: [subscription, dect]

- id: g35
  term: MLAA 树 license
  category: subscription
  source_pages: p428
  source_quote: |
    "Number of available trees are according to licenses • 1: Multiple automated attendant with 1 tree • 5: Multiple automated attendant with 5 trees"
  definition: |
    MLAA 按树数分档：1 树或 5 档树两档 license；树数、端口（与 ACD 共享 16）受其约束。
  alias_or_related: g14
  tags: [subscription, call-processing]

- id: g36
  term: SCR + Supervisor Console license
  category: subscription
  source_pages: p458
  source_quote: |
    "Licenses for SCR • +1 license for Supervisor Console"
  definition: |
    SCR 功能 license + 1 个监督台 license（SCR 日志从监督台出）。
  alias_or_related: g15
  tags: [subscription, call-processing]

- id: g37
  term: 免 license 功能清单
  category: subscription
  source_pages: p73, p316, p321, p360, p367, p375, p287
  source_quote: |
    "No license"（Call Accounting，p73/83）"No license needed"（自动密码检查 p316、订阅户密码管理 p321）"License free"（DTLS p360、TLS/SRTP p367）"OCE Front-End is free (only need the OCE-FE HW)"（p375）"The service does not require licenses."（Cloud Connect，p287）
  definition: |
    书内明确免 license 的能力：Call Accounting Time based、自动密码检查、订阅户密码管理、DTLS、OCE 原生 SIP TLS/SRTP、Cloud Connect 注册、OHL（无 SW license，p65）；OCE-FE 只需硬件。相对地，AA 树定制、MLAA、SCR、Hot Desking、IP-DECT 用户、PIMphony profile、多实体 MoH 均需 license。
  alias_or_related: 各 g 条目
  tags: [subscription, licensing]

# ── 四、产品 (product) ──

- id: g38
  term: OXO Connect Evolution (OCE)
  category: product
  source_pages: p13, p346, p360, p367
  source_quote: |
    "OXO Connect Evolution … IP address: 192.168.1.246"（实验拓扑，p13）
  definition: |
    OXO 的演进型平台：DTLS（p360）、SIP 中继 TLS/SRTP 原生（p367）、4K 证书重启项、公网 Server 证书等高级安全能力的主承载平台；实验采用 OCE。
  alias_or_related: OCO（g39）、OCE-FE（g40）
  tags: [product, platform]

- id: g39
  term: OXO Connect Office (OCO)
  category: product
  source_pages: p375
  source_quote: |
    "Provides SECURED SIP Trunk TLS SRTP for all OXO Connect Platforms •OCE (native) and also for OCO"
  definition: |
    OXO Connect 非演进平台（书内以 OCO 代称）：自身无原生 TLS/SRTP，经 OCE-FE SIP 代理获得加密中继能力。
  alias_or_related: g40
  tags: [product, platform]

- id: g40
  term: OCE Front-End (OCE FE)
  category: product
  source_pages: p375-378
  source_quote: |
    "OCE Front-End new SIP TRUNK TLS SRTP services … Implement a SIP proxy in OCE Front-End • used before only as external WebRTC gateway … License OCE Front-End is free (only need the OCE-FE HW)" (p375)
  definition: |
    OCE 前端设备：原为外部 WebRTC 网关角色，R6.x 起新增 SIP TLS/SRTP 代理角色（为 OCO 等平台转发安全中继）；无 PBX 能力；GW 与 PROXY 各 20 通话上限；license 免费（只需硬件）；OMC 非其供应必需（WebDIAG 配置）。
  alias_or_related: ETH0 必须、ETH1 当前不走 SIP（p378）
  tags: [product, platform]

- id: g41
  term: PowerCPU EE / IP Box
  category: product
  source_pages: p569, p585
  source_quote: |
    "It's possible to see the PowerCPU EE or IP Box startup with the V24 link … RJ45 Config port … V24 port parameters: 115200 8 N 1" (p569)
  definition: |
    OXO 的 CPU 板形态：PowerCPU/EE（LoLa 模式经 Dip switch Jumper 1-2 进入）与 IP Box（OCE 经电源键进 LoLa）；V24 config 口 115200 8N1 监视启动；SUOTA 仅限 OCE 与 PowerCPU EE（p526）。
  alias_or_related: g46 LoLa
  tags: [product, hardware]

- id: g42
  term: 8088 Smart DeskPhone
  category: product
  source_pages: p104-108
  source_quote: |
    "7 inch color display touch screen … Android 6.0.1 … Note: only 8088 >= v2 is supported on OXO" (p105)
  definition: |
    安卓高端话机：7 寸触摸屏、HD 摄像头版/无摄像头版、HDMI 1.4+双 USB2.0、PoE class3、BT4.1+BLE；WebView（企业页面）与 Private Store（APK 私有应用店，限制见 p107）；OXO 仅支持 v2+。
  alias_or_related: SIP(Linux)↔Android 切换（admin 密码 *tx8000#，p109-110）
  tags: [product, terminals]

- id: g43
  term: 8378 DECT IP-xBS / 8379 IBS / 8328
  category: product
  source_pages: p484-486, p494-495, p513
  source_quote: |
    "8378 DECT IP-xBS product range … PoE class 2 (6 Watt max) … 12 radio Slots, 11 communications" (p485)
    "8379 IBS DECT TDM base station … 3 models (indoor, outdoor, outdoor for external antennas)" (p484)
  definition: |
    DECT 基站三系：8378 IP-xBS（IP 接入：室内集成天线/室内外天线/室外三型；PoE class2 6W；12 时隙 11 并发；最多 80 台/200 手柄）；8379 IBS（TDM 接 UA 板，4070 IBS 演进，室内/室外/外天线室外三型，与 4070 可混用，每 IBS 6 并发，最多 60 台）；8328 SIP-DECT（单/双基站小分支方案：1 台 20 手柄 G711 10 并发，2 台 20 并发 G711/8 G729/8 G722+空口同步切换）。
  alias_or_related: 话机 8214/8234/8244/8254/8262/8262EX（p482）
  tags: [product, dect]

- id: g44
  term: 8158s / 8168s VoWLAN Handsets
  category: product
  source_pages: p549-552
  source_quote: |
    "8158s/8168s VoWLAN Handsets work only in NOE mode with OXO Connect System … Compatibility with Stellar APs … and also Aruba, Cisco, Extreme network, Zebra Technology, Aerohive, Xirrus, Fortinet WLAN Infrastructure" (p550)
  definition: |
    Wi-Fi 话机双档（8158s 入门/8168s 高端，书内亦写 MIPT 8158s/8168s）：仅 NOE 模式上 OXO；经 WinPDM+Desktop Programmer（USB cradle）部署；兼容 Stellar AP 与多家第三方 WLAN；OXO ≤R4.x 显示为 8118/8128。
  alias_or_related: TC2349（WinPDM Release Note）
  tags: [product, terminals]

- id: g45
  term: ALE-2 / ALE-3
  category: product
  source_pages: p152
  source_quote: |
    "Differentiation ALE-2 ALE-3 … LCD B&W, 2.8"with Backlight / Color, 2.8" … Resolution 132x64 / 320x240 … Line Key 3 / 4 … SIP Account 2 / 4" (p152)
  definition: |
    入门 SIP 话机双档：ALE-2 黑白屏 3 线键 2 SIP 账号；ALE-3 彩屏 4 线键 4 SIP 账号+USB-A；均双千兆口 PoE class1、宽频手柄、即插即用（DHCP）与经 OXO 固件更新；编解码 G.711/G.729/G.722/OPUS/ILBC。
  alias_or_related: ALE-500/400（AudioHub 载体，p103）
  tags: [product, terminals]

- id: g46
  term: LoLa
  category: product
  source_pages: p582-591
  source_quote: |
    "Lola allows the complete loading of a PowerCPU or OCE • Loading of the call handling software • Loading of the application packages VoIP and ACD • Loading of the main and CTI software licenses" (p583)
  definition: |
    系统加载工具：完整装载呼叫处理软件+VoIP/ACD 应用包+主/CTI license，支持 Installation/Migration Mono CPU/Install-Restore 三类流程；话机数据（留言、NMC 工单）随之恢复，话机配置与语音提示须 OMC 单独保存；也是 installer 密码遗失时的现场兜底（p325）。
  alias_or_related: 交付文件 C:\Releasexxx；license 文件 .csl/.msl（p586）
  tags: [product, tooling]

- id: g47
  term: Webdiag
  category: product
  source_pages: p559-570
  source_quote: |
    "WebDiag is a debug tool • Accessible through OMC … Or through a web interface • https://192.168.92.246/services/webapp/" (p560)
  definition: |
    Web 调试/维护工具：三会话（installer/operator/manufacturer）；信息树 Start/Information/System/VoIP/DECT/Certificates/Services 七块；TCP Dump 抓包、SIP 状态、Hot Desking 监督、账户解锁、Cloud Connect/Rainbow 状态、MIB 下载、证书管理主接口。
  alias_or_related: OSC/PhD-relay 为 OMC 内另两调试工具（p554-558）
  tags: [product, tooling]

- id: g48
  term: ITSP1（SIP Carrier Simulator）
  category: product
  source_pages: p16-22
  source_quote: |
    "ITS1 ITSP1 Public Carrier SIP Simulator … SIP SIMULATOR OVERVIEW - ITSP1 WITH ONE SIP GATEWAY" (p17)
  definition: |
    RLAB 公共区的模拟运营商：SIP 网关 gateway1.itsp1.com（10.20.30.51）+公网网关 public.itsp1.com（10.20.30.50）；PBX 账号 pbxP/alcatel；Public/Urgence 两模拟用户；教学专用，所有取值为实验口径。
  alias_or_related: ITSP2 在图中提及但未展开（p17）
  tags: [product, lab]

# ── 五、协议 (protocol) ──

- id: g49
  term: SIP
  category: protocol
  source_pages: p140-141, p149, p153
  source_quote: |
    "REGISTER sip:192.168.92.246:5059 SIP/2.0 … Status-Line: SIP/2.0 401 Unauthorized … WWW-Authenticate: Digest … Status-Line: SIP/2.0 200 OK" (p140)
  definition: |
    书内 SIP 用法：REGISTER/Digest 认证注册（端口 5059）、B2BUA 呼叫模型、SIP Option 作私网网关监督协议（p217）、RFC 3325（网关 Identity，p49）、RFC 4028 会话计时器（p154）、SIPS URI 在 OCE-FE 不支持（p378）；默认传输 UDP。
  alias_or_related: g23/g24
  tags: [protocol, sip]

- id: g50
  term: TLS / SRTP
  category: protocol
  source_pages: p365-378
  source_quote: |
    "Carrier connectivity with TLS … TLS Authentication model: Server Provided Certificate Authentication or Mutual Authentication • Cryptographic suites: AES Counter Mode [128 and HMAC SHA1 80] [256 and HMAC SHA1 80] [128 and HMAC SHA1 32] [256 and HMAC SHA1 32]" (p367)
  definition: |
    中继加密组合：SIP-TLS（信令，端口 5061）+SRTP（媒体）；认证=服务器证书或双向；四套 AES-CTR 套件；拓扑 Hosted/Static NAT；OCE 原生或 OCE-FE 代理两实现。
  alias_or_related: g22 DTLS 只护信令（NOE 话机）
  tags: [protocol, security]

- id: g51
  term: DECT / GAP
  category: protocol
  source_pages: p499-501
  source_quote: |
    "The DECT and GAP standard is published by the ETSI … DECT: Digital Enhanced Cordless Telecommunications • Publication ETSI EN 300 175-1 to ETSI EN 300 175-8 • GAP: Generic Access Profile • Publication ETSI EN 300 444" (p499)
  definition: |
    数字无线标准：DECT（ETSI EN 300 175-1~-8）定义空中接口（FDMA/TDMA/TDD，10 载波×24 时隙，语音 ADPCM G726 32kbit/s）；GAP（ETSI EN 300 444）通用接入档案（注册/认证，AC 4 位码）；频段按地区四档（p501）。
  alias_or_related: g25 集群、g26 勘测
  tags: [protocol, dect]

- id: g52
  term: LDAPS / StartTLS
  category: protocol
  source_pages: p332
  source_quote: |
    "Supports of both modes: LDAPS and StartTLS • LDAPS mode: LDAP over SSL/TLS. Default port is 636 • StartTLS mode … Default port is 389 (recommended mode, activated by default)"
  definition: |
    外部 LDAP 目录的两条加密通道：LDAPS（636）与 StartTLS（389，推荐默认）；证书校验 Mandatory（默认）/Optional 两级；非加密 LDAP 仍支持（迁移保留）。
  alias_or_related: 证书经 WebDiag Trust Store 导入
  tags: [protocol, security]

- id: g53
  term: HTTPS / 端口族（443 / 50443 / 5059 / 5061 / 7780 / 10443 / 11443 / 30443）
  category: protocol
  source_pages: p300, p346-356, p373
  source_quote: |
    "the exchanges between OMC and OXO Connect uses HTTPS protocol (port 443) … Port 50443 is dedicated to connections from the Internet" (p300)
  definition: |
    书内端口地图：443（OMC/Webdiag LAN HTTPS）、50443（互联网专用入口）、5059（SIP 话机注册/代理）、5061（SIP-TLS 信令）、7780（DTLS）、10443（Generic 话机部署证书）、11443（HAN Wi-Fi AP）、30443（Server certificate 场景）；加固后永久关闭端口 21/1721/5061/8729/8888/17069/23400（p337，启用 SIP-TLS 前需核对版本行为——推断）。
  alias_or_related: p24 端口铁律
  tags: [protocol, ports]

- id: g54
  term: XMPP
  category: protocol
  source_pages: p270
  source_quote: |
    "Cloud Connect (XMPP)"（更新链路图）
  definition: |
    Cloud Connect 软件更新链路中 OXO CC Update Agent 与 CC Update Service 之间的通信协议（更新指令通道）；二进制本身走 HTTPS 下载服务器。
  alias_or_related: g18/g19
  tags: [protocol, cloud]

- id: g55
  term: AOC (Advice Of Charge)
  category: protocol
  source_pages: p73, p82-83
  source_quote: |
    "Provide metering service for trunks that do not support AOC (advice of charge) … When activated, AOC Pulse based is deactivated (no mix configuration)" (p83)
  definition: |
    运营商侧计费脉冲信号：支持 AOC 的中继直接用其脉冲计费；不支持的用 Call Accounting Time based 按时长补——两者互斥不可混配；OCD（Outgoing Call Duration）为相关取值共享功能。
  alias_or_related: g12 计费结构
  tags: [protocol, metering]

- id: g56
  term: PKCS#10 / CSR
  category: protocol
  source_pages: p350, p352, p354-355
  source_quote: |
    "The most common format for CSRs is the PKCS #10 specification" (p350)
  definition: |
    证书签名请求：外部 PKI 签发路径的申请消息格式（WebDIAG 生成并下载，选 2048/4096 位，交外部 CA 签后导回安装）；Server/Public Server/DTLS 证书的外部签发均走此路径。
  alias_or_related: g47 证书四类
  tags: [protocol, certificate]

- id: g57
  term: V24
  category: protocol
  source_pages: p77, p84-87, p569
  source_quote: |
    "The metering device (printer or metering calculator) can be connected via IP • V24 is still possible" (p77)
    "V24 port parameters: 115200 8 N 1" (p569)
  definition: |
    串行接口通道：计费打印/外部计量系统可走 V24/CTI 接口模块（参数见 OMC/Metering/Metering Transmission Characteristics；详参 TC002_US.pdf，p297）；CPU 调试口亦为 V24（115200 8N1）。
  alias_or_related: g48 计费双通道之一
  tags: [protocol, serial]

# ── 六、资源/数值 (resource) ──

- id: g58
  term: 实验网络基线（IP/账号/号码）
  category: resource
  source_pages: p6, p12-13, p17, p21
  source_quote: |
    "Client PC … IP Address: 192.168.1.10 … OXO CONNECT EVOLUTION HARDWARE • IP address: 192.168.1.246" (p12-13)
    "Login: pbxP • Password: alcatel … 210P41000 Installation number • 41100 to 41199 base 100 DDI subscribers" (p21)
  definition: |
    实验口径总表：PC=192.168.1.10、OXO=192.168.1.246、网关=192.168.1.254、DNS1=192.168.1.250、DNS2=10.20.30.250、外部 DNS=10.20.30.250、模拟器 12.0.0.2；SIP 账号 pbxP/alcatel（P=POD 号 1-6）；安装号 210P41000、DDI 41100-41199（base 100）、话务台 41000（base 9）；公网号 33{1-5}1PN12345 等；紧急 112/15/17/18。
  alias_or_related: 生产化须全部替换；DHCP 池两处口径见 n56
  tags: [resource, lab, numbering]

- id: g59
  term: 出厂与实验口令表
  category: resource
  source_pages: p12, p24, p28, p55, p182, p302, p518, p572
  source_quote: |
    "administratorLogin superuserPassword"（Client PC，p12）
    "The Installer password is 'pbxk1064' when logging for the fisrt time" (p28)
    "Login = installer Password = Alcatel1 for example" (p55)
    "The default password is 'OMCAdmin'"（OMC 代理参数，p302）
    "Default login: admin and default password: 00!"（xBS 网页，p518）
  definition: |
    出厂/实验口令清单（全部实验口径，生产必改）：Client PC administrator/superuser；OMC 首连 pbxk1064；Webdiag installer（教室例 Alcatel1）；OMC 代理参数 OMCAdmin；xBS 网页 admin/00!；话机管理密码 8001/8008CE 等（p152）；模拟器 SIP 密码 alcatel；实验远程接入码 780911/615243；话机管理菜单 *tx8000#（8088）；DECT 服务菜单 *7378423*（=service）。
  alias_or_related: n48 console 重置开关
  tags: [resource, credentials]

- id: g60
  term: 系统容量快查表（各功能上限）
  category: resource
  source_pages: p64, p93, p114, p174, p185, p243, p248, p336, p407, p428, p440, p454, p494-495, p360
  source_quote: |
    "300 sets (rooms + administrative telephone) • Native Front Desk management on ALE DeskPhone, 4 simultaneous sessions" (p64)
    "The account codes are configured in the account code table (250 max)" (p93)
    "Number of supervision keys on the system, up to 50" (p114)
    "Rules available: 10 000" (p454)
    "Up to 80 DECT IP-xBS … 200 DECT handsets … 11 simultaneous calls per xBS" (p495)
  definition: |
    上限速查：酒店 300 话机/前台 4 并发会话；账号码表 250（码 16 位）；监督键 50（每键 8 号）；Hot Desking 200/200；实体 4（MoH 10 分钟/段）；个人问候 200 条/预告 20 条/消息 320 秒（多实体增强后）；紧急号码 100 条；AA 每树 2 级 100 节点、4 语言、语音端口 2-8；MLAA 5 树/3 级/16 端口共享/100 消息×4 语言/总量 12000 秒；SCR 10000 规则/10 计划/64 特殊日/8 VP；DECT 80 xBS 或 60 IBS/200 手柄/每 xBS 11 或每 IBS 6 并发；DTLS 300 连接；OCE-FE GW 与 PROXY 各 20 通话；网关 Media 带宽最少 5 通话。
  alias_or_related: 全局限制以 MyPortal《OXO Connect Global Limits》为准（p497）
  tags: [resource, capacity]

- id: g61
  term: 书外技术文档索引（TC 与官方资料）
  category: resource
  source_pages: p68, p297, p299, p323, p338, p499, p530, p552, p578, p497
  source_quote: |
    "Refer to the Technical Communication TC002_US.pdf" (p297)
    "consult the TC1143 … Security recommendations for OXO Connect" (p299)
    "Refer to the technical communication TC2249"（密码审计工具，p323）
    "TC1398 OXO Connect Noteworthy addresses" (p578)
    "TC2349 Release Note for WinPDM" (p552)
    "8AL90874USAA"（SSK 手册，p530）
  definition: |
    生产化必备书外资料：TC1143（安全建议）、TC1398（noteworthy 清单）、TC2249（密码审计工具）、TC002_US（V24 远程接入）、TC2349（WinPDM）、8AL90874USAA（DECT 工程规则与勘测手册）、OXO Connect Global Limits（MyPortal）、hospitality ecosystem PDF（2025-11，PMS 清单）、OXO Connect Cross compatibility（应用/板兼容）、DSPP 白名单（SIP 话机）、RAINWTE012（Rainbow 语音移动培训）、MyPortal IPDSP 文档链接（p464）。
  alias_or_related: n64
  tags: [resource, documentation]

- id: g62
  term: DECT 标识五件套（PARI/RFPI/PARK/PLI/IPUI）
  category: resource
  source_pages: p502
  source_quote: |
    "PARI: Primary Access Right Identifier, identification du PABX, composé de 31 bits ou 8 digits hexa décimal … RFPI: Radio Fixed Part Identifier … composé du PARI et du RPN … PARK: Portable Access Right Key … (codé sur 13 digits + 1 check digit) … PLI: Park Length Indicator (31 pour l'OXO Connect) … IPUI: International Portable User Identity … composé de 14 digits en octal"（p502，原注为法文）
  definition: |
    标识定义（原文法文注释的中译）：PARI=系统 DECT 安装 ID（31 位/8 位十六进制，OXO 全系统一个）；RFPI=xBS 标识（PARI+RPN）；PARK=话机侧系统标识（PLI+PARI，13+1 校验位）；PLI=31（OXO Connect）；IPUI=话机国际身份（EPROM 硬写，14 位八进制）。ARI 配置页（11 位八进制，p543）与 PARI 同源共用。
  alias_or_related: n35 唯一性警告
  tags: [resource, dect, identifiers]
```

## 任务覆盖自检（task ↔ id 映射）

| task_id | 覆盖 glossary 条目 |
|---|---|
| task-01 | g47（Webdiag 入口）、g59（口令表） |
| task-02 | g58（网络基线） |
| task-03 | g49（SIP）、g53（端口）、g48（ITSP1） |
| task-04 | g11、g12、g10 |
| task-05 | g55（AOC）、g57（V24） |
| task-06 | g10 |
| task-07 | g17、g31 |
| task-08 | —（PIMphony 概念在 framework f10；无独立术语条目，因 profiles 均为产品内档位） |
| task-09 | g23、g24、g45、g42 |
| task-10 | g47 |
| task-11 | g07、g32、g33 |
| task-12 | g06 |
| task-13 | g02、g49、g50 |
| task-14 | g03 |
| task-15 | g04、g05 |
| task-16/17 | g18、g19、g20、g54 |
| task-18 | g53、g57 |
| task-19 | —（Rainbow 目录同步为操作链路，framework f36 承载） |
| task-20 | g21、g52、g53、g59 |
| task-21 | g56 |
| task-22 | g22 |
| task-23 | g38、g39、g40、g50 |
| task-24 | g16 |
| task-25 | g13 |
| task-26 | g14、g35 |
| task-27 | g15、g36 |
| task-28 | g08、g09 |
| task-29 | g25、g26、g27、g43、g44、g51、g62、g34 |
| task-30 | g21、g29、g30、g28 |
| task-31 | g41、g46 |
| 通用 | g37（免 license 清单）、g58-g61（取值表与书外资料） |

自检结论：六类齐全（concept 27 / role 5 / subscription 5 / product 11 / protocol 9 / resource 5，合计 62 条）；缩写未给全称者（DDI、RSL、RPN、NMC、CTI、ADL、HAN 只给 Home Area Network 等）均如实处理，未编造全称；DECT/GAP、AOC、CSR/PKCS#10、DTLS、LDAPS 等书内有展开的按原文收录。
