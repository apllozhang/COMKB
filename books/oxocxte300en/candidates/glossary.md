# 术语/缩写/产品名候选 — OXO Connect Starter (OXOCXTE300EN Ed16)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 46 条，按 concept / role / subscription / product / protocol / resource 六类组织。
> 缩写全称纪律：书中未给全称的一律不填 full_name（OMC/HSL/ARS/UTL 之外的板卡缩写等），不采信外部知识；书中给出展开的（FTR/MSDB/eMMC/NUC/SBC/CE/CLIR/TOTP 等）如实登记并附页码。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: OXO Connect / OXO Connect Evolution (OCE)
  category: concept
  source_pages: p24-26, p30
  source_quote: |
    "OXO Connect is a phone system for Enterprises and Hotels with up to 300 users" (p24)
    "IP Pure IP – 300 users … OXO Connect Evolution … Hybrid TDM/IP - 300 users … OXO Connect
    (PowerCPU-EE) … OXO Connect Compact TDM" (p26)
  definition: |
    ALE 面向 ≤300 用户企业与酒店的通信套件家族：OXO Connect Evolution（OCE）=纯 IP 的 IPBox 硬件
    平台；OXO Connect（PowerCPU-EE）=混合 TDM/IP，机箱分 Compact/Small/Large；另有 Compact 纯 TDM
    形态。支持 LAN/WLAN/IP DECT 接入、Rainbow 混合云、证书认证（RSA 2048/4096 位）。
  alias_or_related: OCE；OCO（p218 出现、书内未展开，与 OCE 并列于 Cloud Connect 语境，推断指 OXO
    Connect 平台侧）
  tags: [concept, product-family]

- id: g02
  term: FTR
  full_name: First Time Registration（书中展开，p57）
  category: concept
  source_pages: p57-62, p375-376
  source_quote: |
    "First startup registration (FTR*) … *FTR = First Time Registration" (p57)
    "Installation of the OCE Front-End is automated with the FTR procedure • FTR provides the OCE
    Front-End license and upgrades the OCE release (≥ R4.0 MD) if necessary" (p375)
  definition: |
    OCE 首次注册流程：经 ETH1 网页（192.168.94.246）以 installer 登录，强制设新密码，录入 IP/
    代理/DNS 与三参考值（Partner fleet/Sub-fleet/Installation reference），注册 Cloud Connect 并
    自动下载许可、更新系统；OCE-FE 场景下 FTR 自动给许可并按需升级版本。
  alias_or_related: Cloud Connect（g03）；FTR 完成状态属 Cloud Connect Data（p323）
  tags: [concept, ftr, cloud]

- id: g03
  term: Cloud Connect
  category: concept
  source_pages: p51-53, p62, p323
  source_quote: |
    "OXO Connect Cloud Connect solution: • Auto registration on Cloud Connect Standard Solution:
    • On-site management with OMC" (p51)
    "Cloud Connect: The system becomes accessible remotely via OXO Connectivity and the Fleet
    Dashboard" (p62)
  definition: |
    云托管交付路线：开箱即插即用（IP 配置+Installation Id）→ 自动连云 → 软件与许可自动下载 → 远程/
    现场管理（防火墙友好）→ 机队级 Web 分析与资产 → 云端自动更新。冷复位数据分类中 Cloud Connect
    Data 含激活状态/FTR 完成状态/服务器 URL/一次性与最终账户密码。
  alias_or_related: Fleet Dashboard（g19）；与 Standard（OMC 现场装 .msl/.csl）二选一
  tags: [concept, cloud, deployment]

- id: g04
  term: ETH1（服务口）
  category: concept
  source_pages: p31, p57, p200
  source_quote: |
    "ETH1: For Instant Management access on site (DHCP , DNS)" (p31)
    "Eth1 is configured with a fixed IP address and an active DHCP server … Using string
    "myipbox.ale" in the URL or in OMC directly connects to the server … Eth1 MUST not be connect
    on the LAN" (p57)
  definition: |
    OCE 第二网口，专用于现场即时管理：固定 IP 192.168.94.246/24、自带 DHCP（.247-.254，租期 2h）
    与 DNS；域名 myipbox.ale 直连；仅允许配 ETH0 参数与 Webdiag 诊断（installer/operator/
    manufacturer 身份），不允许用户应用。安全边界：不得接 LAN、不能访问 Eth0 侧 LAN、可禁用、IP
    冲突自动禁用；ISP SIP 也可直连此口实现双子网隔离。
  alias_or_related: 与 ETH0（LAN+PoE，承载全部服务）成对
  tags: [concept, oce, eth1]

- id: g05
  term: OMC
  category: concept
  source_pages: p63-71
  source_quote: |
    "The OMC welcome screen proposes different management modes … Expert: Access to the system
    configuration manually or by wizard" (p65)
    "OMC checks system certificate to authenticate the server that it connects to" (p68)
  definition: |
    OXO 的 Windows 管理软件（书中未展开缩写全称）：六类入口（Data Collection and Tools/
    Installation Typical/Modification Typical/Multi site/Expert）；连接方式 V24 串口/modem 回拨/
    LAN-WAN；承载密码管理、软件钥匙导入、数据备份恢复、软件下载、复位、Webdiag 入口等全功能。
    首连默认 IP 192.168.92.246、密码 pbxk1064（实验口径）。
  alias_or_related: Webdiag（g44）；DBAdapter（g20）；安装向导/修改向导（f44）
  tags: [concept, omc, management]

- id: g06
  term: Data Collection（数据采集）
  category: concept
  source_pages: p43, p65
  source_quote: |
    "Data collection gathers customer needs, information on its ecosystem and the functionalities
    to be implemented. Bring all the documents and software to perform the installation, such as
    licenses, software version, OMC, technical documentation … etc" (p43)
    "Data Collection executes a Data Collection wizard, do not require to be connected to an OXO
    Connect" (p65)
  definition: |
    交付起点：采集客户需求、生态信息（IP/密码/编号/组/呼入呼出/Rainbow 前提）与待实现功能清单；
    OMC 的 Data Collection 向导可不连系统离线跑，产出的采集库经 Installation Typical 载入系统。
  alias_or_related: Installation wizard（f44）；BOOK_OVERVIEW task-01
  tags: [concept, planning, data-collection]

- id: g07
  term: Auto-Provisioning（自动配置）
  category: concept
  source_pages: p88, p107, p118, p455
  source_quote: |
    "Enable « auto provision » in the Subscribers/Base stations list to allow IP devices to register
    onto the OXO Connect" (p107)
    "IMPORTANT: Don't forget to activate Auto-Provisioning in the menu of the Subscribers/
    Basestations List." (p455)
  definition: |
    OMC/Subscribers BaseStations list 里的开关：允许 IP 终端（话机/xBS/8328 体系话机）注册到 OXO
    并自动分配目录号码；新 IP 话机默认配置下不自动上线（p88），必须开此开关（可临时启用）。教材
    三处 IMPORTANT/法文注强调"别忘开"。
  alias_or_related: DHCP 池（OMC/Hardware and limits/LAN/IP Configuration/DHCP）；与 WebRTC 网关
    "自动配置"（Reseller 发起，g27）是两回事
  tags: [concept, provisioning, terminal]

- id: g08
  term: Dynamic Routing（动态路由）
  category: concept
  source_pages: p90, p164-166
  source_quote: |
    "Phone set behavior on unanswered call • Allows to forward automatically an incoming call
    (internal or external), according two levels and two timers." (p164)
    "Dynamic Routing cascading is supported for subscribers and Hunting groups • Maximum value
    allowed: 5" (p166)
  definition: |
    久叫不应的两级两计时框架：T1→LEVEL1 目的地（hunt group/分机/集体缩位）、T2→话务台（General
    level=活动话务台组，可带 General bell）；AA 复选决定是否经自动话务员；apply diversion 是一切
    转移的总开关；级联支持分机与 hunt group、系统上限 5 级。出厂默认 12s 转信箱、话务台呼叫 24s
    转组 8。
  alias_or_related: Attendant group（g09）；Voice mail（g18）
  tags: [concept, routing, diversion]

- id: g09
  term: Attendant group（话务台组）
  category: concept
  source_pages: p254-255, p264
  source_quote: |
    "OMC/ Attendant groups1. Creating attendant groups Available items in attendant group Phone
    sets Message General bell Voicemail ports (Auto. attendant) Remote access" (p255)
    "An attendant group is always in parallel mode." (p264)
  definition: |
    呼入分发的容器：成员可为分机、MSG1-20 欢迎消息、General bell、VM 端口（拼自动话务员）、远程接
    入；组永远并行（齐振）模式。默认话务台自动编入组 1/2 与默认组 8；经 Time Ranges 按时段切换活动
    组，Normal/Restricted 双 DDI 计划支撑日夜切换。
  alias_or_related: Time Ranges（c15）；Normal/Restricted（g11）；Rainbow Supervision group（g24）
    是另一体系
  tags: [concept, incoming-calls, attendant]

- id: g10
  term: DDI / Base
  category: concept
  source_pages: p46, p128-130, p134
  source_quote: |
    "Public numbering – DDI numbers • Subscribers: 41100 to 41199 • Attendant: 41100" (p46)
    "DDI number 41100 – Base 100 … Directory number 100 – Base 100 … Private directory number 8800
    – Base 100" (p128)
  definition: |
    DDI=公共编号计划中映射到内线分机的直拨号（书中未展开缩写全称）；Base=内外映射基数：DDI 41100
    base 100 ↔ 分机 100，私网号 8800 base 100 同理。前缀功能的 Base 语义固定（Pick-up 族 0-3、
    Forwarding 族 0-10），取值域 0-2199。安装号=主系统 DDI 号去首位录入。
  alias_or_related: Installation number（g12）；多 DDI 段发送规则受 DDIonPRI 控制（p279）
  tags: [concept, numbering, ddi]

- id: g11
  term: Normal / Restricted mode（正常/受限模式）
  category: concept
  source_pages: p254, p277-278
  source_quote: |
    "The normal / restricted mode is used for INCOMING calls distribution • 2 DDI numbering plans •
    One for normal mode, another for restricted mode" (p254)
    "The system uses restricted LC values for traffic sharing, barring and collective speed dial
    access If the restricted mode is activated … By default the users don't follow the time range
    state." (p277)
  definition: |
    系统级日夜双模：呼入走两套 DDI 计划、呼出走两套 LC 值（traffic sharing/barring/集体缩位接入）。
    激活手段：话务台 N/R 键（手动）或 Time Ranges（自动）；用户级豁免权两枚（Inhibition time
    ranges/Inhibition flag），默认用户不跟随时段状态。
  alias_or_related: Traffic sharing（g13）；Barring（g12）
  tags: [concept, day-night, mode]

- id: g12
  term: Barring / Link Category (LC) / COS
  category: concept
  source_pages: p271-275
  source_quote: |
    "Traffic sharing link category The set is either allowed (authorized) or not allowed (forbidden)
    to seize a trunk group • Barring link category If allowed to seize a trunk group, the number
    dialed is either allowed (authorized) or not (forbidden)" (p271)
    "6 barring tables = 6 levels of barring" (p274)
  definition: |
    出局限制三层模型：Traffic sharing LC（能否占中继组，用户 COS×中继组 COS 查矩阵 +/空）→ Barring
    LC（用户经 Barring 矩阵定位用哪张闭锁表）→ Barring 表（6 张=6 级；前缀 Authorized/Forbidden、
    digit counter 控位数）。默认国际 00 全表 Forbidden；默认 LC normal=restricted=12。
  alias_or_related: Barring matrix（行 2 列 1=2 即用表 2 的读法）；COS=书中对链路类别值的称谓
  tags: [concept, barring, cos]

- id: g13
  term: Traffic Sharing Matrix（话务分担矩阵）
  category: concept
  source_pages: p273, p288
  source_quote: |
    "Connection point: « + »: Access from an extension set to a trunk group is authorized « Blank »:
    Access from an extension set to a trunk group is prohibited" (p273)
    "Find the intersection between Subscriber category (5) and trunk group category (12). The data
    "+" means YES" (p288)
  definition: |
    行=用户类别（Traffic sharing LC 值）、列=中继组类别（LC 值）的判定矩阵：交点 +=可占用、空白=
    禁止。授权方法=把用户 LC 改成与中继组 LC 交点为 + 的值（实验 5∩12=+），其余用户默认 12∩12=空。
  alias_or_related: Barring Matrix 同构（定位闭锁表）
  tags: [concept, matrix, traffic-sharing]

- id: g14
  term: Installation number（安装号）
  category: concept
  source_pages: p130, p204, p229
  source_quote: |
    "Installation number can also be entered at installation wizard • It is the main system DDI
    number • Enter the installation number without the first digit" (p130)
    "The default SIP numbering format is the canonical format • Canonical format is: + International
    code, Intercity code, Installation number + DID" (p204)
  definition: |
    主系统 DDI 号（运营商打给企业的总机号）；录入时去掉第 1 位；SIP 默认号码格式为规范格式（+国际
    码+城际码+安装号+DID）。实验口径 210P41000（P=POD 号）。
  alias_or_related: OMC\Numbering\Installation Numbers；SIP numbers format index（General 页签）
  tags: [concept, numbering]

- id: g15
  term: ARS
  category: concept
  source_pages: p220-222, p366
  source_quote: |
    "According to the SIP provider and its public SIP numbering formats, additional lines in the ARS
    call routing table must be created to cope with specific public phone numbers (e.g. short
    numbers or emergency numbers)" (p220)
    "Configuration of ARS table to route Rainbow calls" (p366)
  definition: |
    书中菜单名为 Automatic Routing Selection 的自动路由选择（缩写 ARS 书内未见逐词展开）：出局号码
    分析与路由表；Easy Connect 部署后要按国家补短号与紧急号码条目（法国典型四行：0 开头/紧急 emerg
    属性/3 开头/1 开头），WebRTC 网关自动配置也会自动写 Rainbow 呼叫路由行。
  alias_or_related: OMC/Numbering/Automatic Routing Selection/…；Emergency→Emergency Numbers 清单
  tags: [concept, routing, ars]

- id: g16
  term: SIP Trunk Profile / SIP Easy Connect
  category: concept
  source_pages: p216-219
  source_quote: |
    "Once a new SIP provider gets approved by the TSS, the configuration related to this provider is
    collected by ALE and put in a file called Profile, available on MyPortal" (p216)
    "SIP trunk easy setup thanks to an OXO Webpage • All technical configuration is done behind the
    scene (SIP trunk, SIP Gateway, SIP account, numbering, …)" (p218)
  definition: |
    Profile=已过 TSS 认证的运营商配置包（SPF 文件，含网关参数集/SIP Public Numbering 参数/VoIP
    全局参数子集/noteworthy 地址），经 OMC 导入导出（TC1994）；Easy Connect=Cloud Connected 系统
    （OCO/OCE）在 OXO 网页选 Profile、填少量参数即完成 SIP trunk 全套配置，后续修改走 OMC。
  alias_or_related: TC1284（运营商兼容清单与支持流程）；TC1994（Profile 导入导出）
  tags: [concept, sip-profile, easy-connect]

- id: g17
  term: Phreaking（盗打）
  category: concept
  source_pages: p326-329
  source_quote: |
    "The Phreaking is the name for the telephony system hacking When somebody hacks your PABX, the
    target is not your PABX, the target is your customer's wallet • The victims can loose more than
    20 K€ in one weekend" (p326)
  definition: |
    电话系统黑客行为的书内称谓：目标是客户钱包（一周末可损失 2 万欧以上），被盗线路卖给长途运营商
    或接高费率号，属有组织犯罪。防线：密码常识、按推荐配置、升级最新版、强制应用 TC1143。
  alias_or_related: TC1143_Security_Recommendations_for_OXO_Connect；Expert 文档 SECURITY 章
  tags: [concept, security, phreaking]

- id: g18
  term: Voice Mail（VMU）/General Mailbox
  category: concept
  source_pages: p183-189, p323
  source_quote: |
    "Voice mail box for each set • 2 accesses • 4 languages • 1 hour of stored messages" (p183)
    "The general mailbox is not attached to a set … The password of the general mailbox is the
    operator password" (p189)
    "User Data: • Voice mail (VMU)" (p323)
  definition: |
    CPU 集成语音信箱（VMU=书中 User Data 分类的 Voice mail 标识）：每话机一信箱、三态（Standard/
    Guest/Answer Only）；访问双模 APPLICATION（键/前缀，不占端口）与 CONNECTED（拨端口/组号，占
    端口走 DTMF）；General Mailbox 经自动话务员访问、只存消息由话务员转派、密码=话务员密码。
  alias_or_related: Message Screening/Conversation Recorder/AutoRec（c12）；hunt group 500=VM 端口组
  tags: [concept, voicemail]

- id: g19
  term: Fleet Dashboard / OXO Connectivity
  category: concept
  source_pages: p62, p381
  source_quote: |
    "The system becomes accessible remotely via OXO Connectivity and the Fleet Dashboard" (p62)
    "In Fleet Dashboard & OXO Connectivity: - Identification of PABX/OCE-Front-End - Dynamic link to
    access the peer device with a single click 1 line per device with same root of install_id" (p381)
  definition: |
    Cloud Connect 的机队管理面：每设备一行（同 install_id 根）、识别 PBX/OCE-FE 配对、一键跳转对端
    设备；FTR 完成后系统即纳入远程管理。
  alias_or_related: MyPortal（BP 门户，软件/许可/文档下载入口）
  tags: [concept, cloud, fleet]

- id: g20
  term: DBAdapter
  category: concept
  source_pages: p306
  source_quote: |
    "DBAdapter is a software tool to convert database files saved with a previous version of OMC to
    the latest installed version • Install DBAdapterSetup.msi After DBAdapter installation, The OMC
    converts automatically an old backup when it open it • Conversion is transparent"
  definition: |
    OMC 跨版本数据库迁移工具（MyPortal 下载 DBAdapterSetup.msi）：安装后 OMC 打开旧备份自动透明转
    换；未安装时 OMC 打开旧库会提示安装。
  alias_or_related: OMC 备份 .cdb 文件（c17）
  tags: [concept, migration, omc]

- id: g21
  term: Warm / Cold / Factory Reset
  category: concept
  source_pages: p322-324
  source_quote: |
    "Warm reset • Allows to unlock hardware malfunction without losing the customer database …
    Factory Reset • Removes all the sub categories of data in cold reset and additionally it removes
    system logs • After Factory reset, system state is close to that of Lola installation" (p322)
  definition: |
    三档复位：Warm=重启不丢库；Cold=回默认配置（不勾子选项时保留 installer 密码/网络/管理旗标/
    Cloud Connect 参数）；Factory=Cold 全删之外再删系统日志、接近 Lola 出厂态。手动关机再开=warm
    reset。入口：话机 MMC 话务员会话或 OMC Expert。
  alias_or_related: Lola（书内未解释的出厂引导态称谓，p58 LOLA 模式）
  tags: [concept, reset]

# ── 二、角色 (role) ──

- id: g22
  term: Installer（安装员账户）
  category: role
  source_pages: p67, p81, p94, p349
  source_quote: |
    "To be authenticated, select the Installer mode, enter the password and press OK • Default IP
    Address: 192.168.92.246 • Default Password: pbxk1064 (First connection)" (p67)
    "Login: installer Password: enter installer pwd" (p349)
  definition: |
    七个系统管理账户之一（与 Attendant/Administrator/Download/NMC/ACD/Users 并列）：OMC Expert 连接、
    Webdiag、恢复（Auto-Connect for Restore）都用 installer 身份；首连密码 pbxk1064（实验口径、仅
    首次），首启强制改密。
  alias_or_related: Management Passwords 分类（p323）；密码规则 8 位三类字符（p94）
  tags: [role, installer, accounts]

- id: g23
  term: Reseller/BP Administrator 与 End-customer Administrator
  category: role
  source_pages: p338-340
  source_quote: |
    "RESELLER / BP ADMINISTRATOR … Create PBXs & activate WebRTC gateways … Assign subscriptions to
    end-customer companies" (p338)
    "END- CUSTOMER ADMINISTRATOR … Manage user accounts … View related PBXs … Associate users phones
    with their Rainbow accounts" (p339)
    "The "Roles" tab is used to assign administrative rights to the client company. • It is possible
    to have several administrators to manage the company." (p340)
  definition: |
    Rainbow 双管理员档案：BP 侧可看客户公司、建 PBX 并激活 WebRTC 网关、给 EC 分订阅；EC 侧管自己
    公司/用户/订阅分配/话机关联/仪表盘。客户管理员经 Roles 页签赋权、可多名。角色细目见
    help.openrainbow.com Features List/Administration。
  alias_or_related: WebRTC 自动配置仅 Reseller 账户可做（p396）；BOOK_OVERVIEW 术语表同条目
  tags: [role, rainbow, administrator]

- id: g24
  term: Supervisor / Supervisee（监督员与被监督成员）
  category: role
  source_pages: p409, p412, p417
  source_quote: |
    "Members & attendant must belong to the same supervision groups (administrator)" (p409)
    "One or several supervisors: they must be granted an Attendant license to use the attendant
    console • The company members to supervise" (p412)
    "The supervisor belongs to the group(s) he supervises" (p417)
  definition: |
    Rainbow 监督体系双角色：监督员须持 Attendant 订阅、每员至多 5 组；被监督成员与监督员同组、每组
    至多 30 人（两类合计）；互助组里监督员属于其监督的组、可临时纳排被监督用户、锁定成员不可退出。
  alias_or_related: Attendant console（g25）；Mutual aid group（g26）
  tags: [role, rainbow, supervision]

- id: g25
  term: Manager / Assistant（Secretary）（经理/秘书）
  category: role
  source_pages: p89, p140, p155
  source_quote: |
    "Manager/Assistant group (after having carried out an installation wizard) •Assistant: equipment
    2 •Manager: equipment 3 •Authorized stations: multiline sets" (p89)
    "An assistant screens calls for manager … RSL secretary • Screening • Secretary supervision" (p140)
  definition: |
    OXO 侧经理-秘书关系的双方：均须 multiline 话机（默认 Assistant=设备 2、Manager=设备 3）；互相
    持有对端 RSL 键、Screening 过滤键与监督键；向导跑过后才有默认组。
  alias_or_related: Manager-Secretary Relations 菜单（c10）
  tags: [role, manager-secretary]

# ── 三、订阅与许可 (subscription) ──

- id: g26
  term: Rainbow 订阅目录（Essential/Business/Enterprise/…）
  category: subscription
  source_pages: p335, p409
  source_quote: |
    "Rainbow Essential This free option is available to anyone who wants to try Rainbow for an
    unlimited period (no SLA). … Rainbow Enterprise Conference … pre-paid yearly in advance (twelve
    months)" (p335)
    "An Attendant subscription is required for each member using this feature" (p409)
  definition: |
    本书列出七种用户订阅：Essential（免费无 SLA、可与付费混用）、Business、Enterprise（Business 全
    量+多方视频+扩展存储+O365/Google Suite 集成）、Enterprise Conference（+无限电话会议分钟、按年
    预付 12 个月）、Conference（pay-as-you-go 按分钟/连接、组织者可免费用户）、Connect（CRM 连接
    器）、Room（按房间、需额外硬件）；话务台另需 Attendant 订阅（每使用成员一份）。电话功能要求
    Business/Enterprise（网关用户）或 Attendant（话务台）。
  alias_or_related: 与 RAINXTE001EN 的 8 种口径互补（其将 Attendant 单列）；计费形态 Monthly/Prepaid
    （p421）
  tags: [subscription, rainbow, licensing]

- id: g27
  term: UTL
  full_name: Universal Telephony License（书中 p28 商用提案图出现）
  category: subscription
  source_pages: p28, p101, p104, p368, p401
  source_quote: |
    "Universal Telephony License" (p28)
    "Requires an IPDSP licence = UTL" (p101)
    "Deskphone + Free Rainbow virtual terminal = 1 UTL • Anydevice only = 1 UTL" (p401)
  definition: |
    通用电话许可（计费单位）：IPDSP=1；模拟-SIP 网关每模拟口=1 UTL+1 Open SIP license；物理话机+
    Free Rainbow in Twinset 副站合计=1（UTL Bypass，R6.0 起）；纯 Anydevice=1。
  alias_or_related: Twinset（g28）；Software Assurance/Extended Capacity（p28 同图并列项）
  tags: [subscription, licensing, utl]

- id: g28
  term: Multiset / Free Rainbow in Twinset / Anydevice
  category: subscription
  source_pages: p358, p368, p400-401
  source_quote: |
    "Create a Multiset • The main station is the physical station • The secondary station is • Free
    Rainbow in Twinset from R6.0 • (Anydevice up to R5.2)" (p368)
    "Rainbow user only (Softphone and mobile mode), without a physical extension: … Requires an
    Anydevice terminal." (p400)
  definition: |
    WebRTC 网关用户的两种 OXO 终端形态：Multiset=物理主站+虚拟副站（R6.0 起副站用 Free Rainbow in
    Twinset 省 UTL；R5.2 及以前用 Anydevice）；Anydevice=纯软话机终端（无物理分机、全部通信经
    Rainbow 应用，OXO 侧最低 R6、至多 8 通话保持）。用户订阅须 Business 或 Enterprise（p387）。
  alias_or_related: 版本陷阱见 n27；UTL 口径见 g27
  tags: [subscription, twinset, anydevice, terminal-form]

- id: g29
  term: Software keys（.msl / .csl）
  category: subscription
  source_pages: p55, p71
  source_quote: |
    "Upload the 2 Licences in the OCE • .msl & .csl" (p55)
    "The software keys are linked to the Main CPU serial number … The main key f103f217.msl … The
    CTI key f103f217.csl … The Details button shows the services opened by the software keys." (p71)
  definition: |
    软件钥匙=与主 CPU 序列号绑定的许可文件：.msl 主钥匙+.csl CTI 钥匙，经 OMC/Modification typical/
    System/Software key 导入并 Apply；随客户库一起保存。Standard 路线手工导入；Cloud Connect 路线
    云端自动下发。
  alias_or_related: 换 CPU 需重新生成许可（p296）
  tags: [subscription, licensing, software-keys]

# ── 四、产品与硬件 (product) ──

- id: g30
  term: IPBox（OCE 硬件）
  category: product
  source_pages: p30-32
  source_quote: |
    "Micro USB Console port … 2 Ethernet ports ETH0: LAN & POE ETH1: For Instant Management access
    on site (DHCP , DNS) … SD card interface (rear side) Used for backup (optional)" (p31)
    "OCE can be installed as well as desktop, wall mounted or rack product (1/2 of 19" form factor,
    1U)" (p32)
  definition: |
    OXO Connect Evolution 的硬件盒：Micro USB 控制台、工厂 USB、RJ45 AFU、双以太网（ETH0=LAN+PoE、
    ETH1=现场管理）、电源键与双色 LED、背面 SD 卡槽（备份选件）；桌面/壁挂/机架（半宽 19" 1U）；
    零接触部署前提 OmniSwitch 侧开 PoE。
  alias_or_related: ETH1（g04）；SD 卡备份（p301-304）；IPBox 专属容量口径见 p374 表
  tags: [product, ipbox, oce]

- id: g31
  term: PowerCPU EE / MSDB / eMMC
  category: product
  source_pages: p35
  source_quote: |
    "Processor MPC8377 @ 800 MHz • DDR2 512 MB RAM running at 400 MHz • LAN Ethernet port
    10/100/1000 MB/s • 16VoIP resources (1 DSP TMS320C6421) • 2 Mbyte NOR Flash Memory for boot
    loader • eMMC flash Eprom available on MSDB daughter board • MSDB is by default equipped with a
    8GB eMMC flash memory • MSDB = Mass Storage Daughter Board • eMMC = Embedded Multi-Media Card" (p35)
  definition: |
    PowerCPU EE 主控板：MPC8377@800MHz、DDR2 512MB、千兆 LAN、16 VoIP 资源（1 片 TMS320C6421 DSP）、
    2MB NOR 引导；MSDB（Mass Storage Daughter Board）子板默认 8GB eMMC（Embedded Multi-Media
    Card）承载数据备份。
  alias_or_related: Armada 32/64（g32）；eMMC 移植需新 license（p296）
  tags: [product, powercpu, hardware]

- id: g32
  term: Armada 32 / Armada 64（VoIP 资源子板）
  category: product
  source_pages: p36-37
  source_quote: |
    "Armada 32 and Armada 64 (VoIP resources)" (p36)
    "The maximum number of DSP channels is extended from 60 to 76 when using the Armada 64" (p37)
  definition: |
    PowerCPU EE 的 VoIP 扩展子板：Armada 32 → 48 DSP 通道；Armada 64 → 60 多编解码 或 30
    G711/G729+46 G711 共 76。其它子板：AFU-1（通用铃/门铃/背景音乐/告警/扬声器）、HSL1/HSL2、
    Mini-Mix 2xT0+2Z（仅 Compact）。
  alias_or_related: DSP 通道表（p05/p37）
  tags: [product, armada, daughter-board]

- id: g33
  term: HSL / PowerMEX / 多机柜
  category: product
  source_pages: p36, p42
  source_quote: |
    "HSL1 or HSL2 (Module 1 and 2, connection to PowerMex)" (p36)
    "Up to 3 racks can be interconnected using HSL links • The HSL link connects the PowerCPU EE to
    the PowerMEX board • The maximum length between the master rack and the extension rack is
    5 meters" (p42)
  definition: |
    HSL（书内未展开全称）=主控到扩展机柜 PowerMEX 板的高速链路：最多 3 机柜互连、主柜到扩展柜最大
    5 米；启动监控按 HSL2→HSL1→主柜顺序检测（p437）。
  alias_or_related: 启动八步（f43）
  tags: [product, hsl, multi-cabinet]

- id: g34
  term: 接口板家族（UAI/MIX/AMIX/SLI16/APA8/DDI2/DDI4/BRA/PRA）
  category: product
  source_pages: p431-435
  source_quote: |
    "SLI16, DDI2, DDI4 Slots without any restrictions APA8 MIX, AMIX, UAI-16 Boards restrictions" (p431)
    "MIX: T0 trunks • A-MIX: APA trunks" (p433)
    "BRA, basic accesses T0 connections • Used for T0/DLT0 trunk connections … PRA, Primary accesses
    T2 connections • Only one port can be used at the same time" (p435)
  definition: |
    PowerCPU EE 机柜板卡：UAI-16（数字话机 UA+IBS DECT）、MIX/AMIX（数字话机/DECT/模拟话机 Z/中继，
    MIX=T0、A-MIX=APA）、SLI（模拟话机/传真/modem）、APA8（模拟中继）、DDI2/DDI4（无槽位限制）、
    BRA（T0/DLT0）、PRA（T2/DLT2，单端口同用）。缩写书内均未逐词展开。DLT0/DLT2 用于专网。
  alias_or_related: 主中继组自动收编第 1 块外部接入板第 1 设备（p93）
  tags: [product, boards, tdm]

- id: g35
  term: 话机家族（ALE-20/30/300/400/500、8039、8214/8234/8244/8254/8262、8158s/8168s、8088 v3、8135s）
  category: product
  source_pages: p97-103, p93
  source_quote: |
    "ALE-20 / 20h ALE-30 / 30h ALE-300 ALE-400 ALE-500 … ALE-2 8008-8G" (p97)
    "8262 8262 EX 8158s 8168s8254 8234 8244" (p97)
    "OmniTouch 8135s • SIP conference device • Up to 20 participants" (p103)
  definition: |
    终端全家桶：Essential 系（ALE-20/20h/30/30h，模拟口 UA/Fast Ethernet）、Enterprise 系（ALE-300/
    400/500，双千兆、彩色屏、键模块 ALE-120 级联 3 个/ALE-145）、Basic SIP（ALE-2 黑白/ALE-3 彩色）、
    数字混合（8068s/8078s/8038/8039——8039 为建议话务台机、8078s/8068s/8038/8039 可查版本）、DECT
    手柄（8214/8234/8244/8254/8262/8262EX）、WLAN（8158s/8168s）、会议（8088 v3、8135s SIP 会议 20
    人+ALE Unite App）。
  alias_or_related: 8039 默认话务台建议（p89）；菜单安装向导支持 8068s/8078s/8039（p440）
  tags: [product, deskphones]

- id: g36
  term: IPDSP / PIMphony / MicroSIP
  category: product
  source_pages: p10, p101-102
  source_quote: |
    "An IPDSP to be installed, it will be the main softphone to use directory number: 104" (p10)
    "IP Desktop SoftPhone (IPDSP) allows voice communications … Requires an IPDSP licence = UTL" (p101)
    "PIMphony is a Windows SoftPhone … PIMphony Basic (Free) •PIMphony Pro: screen pop •PIMphony
    Teams: workgroups •PIMphony Attendant" (p102)
  definition: |
    软话机三线：IPDSP（PC/平板/移动的 IP Desktop SoftPhone，1 UTL，实验主力分机 104）；PIMphony
    （Windows 软话机，Basic 免费/Pro 屏幕弹出/Teams 工作组/Attendant 话务台版，除 SIP 话机外可配合
    任何终端或纯 IP 版）；MicroSIP（实验环境预装的轻量 SIP 客户端，分机 100-103 与公共号模拟）。
  alias_or_related: 模拟-SIP 网关（g37）为模拟设备软化为 SIP 的反向路径
  tags: [product, softphone]

- id: g37
  term: 模拟-SIP 网关（MEDIA5 4102 / C710 / C711）
  category: product
  source_pages: p104
  source_quote: |
    "3 models Analog-SIP Gateway in the catalog … Passerelle FXS MEDIA5 4102 MEDIA5 C710 MEDIA5
    C711 • Ports FXS (RJ-11) 2 4 8" (p104)
    "Requires one UTL + one Open SIP license per analog port … Appears in OMC as Open SIP Terminal" (p104)
  definition: |
    把模拟话机/传真接入 OCE 的 FXS 网关：4102（2 口）/C710（4 口）/C711（8 口），每模拟口 1 UTL+
    1 Open SIP license，OMC 中显示为 Open SIP 终端；部署指南在 MyPortal。
  alias_or_related: Open SIP Phone 终端类型（8214 声明同型，c25）
  tags: [product, fxs, gateway]

- id: g38
  term: 8378 IP-xBS / 8328 / IBS DECT
  category: product
  source_pages: p100, p117-122, p453-456
  source_quote: |
    "DECT base stations 8378 IP-xBS 8379 8328" (p100)
    "8378 DECT IP-xBS … PARI Dect Settings Enter the ARI number (11 digits in octal)" (p117-119)
    "8328 SIP-DECT SINGLE BASE SATION – System Guide" (p454)
  definition: |
    两条 DECT 路线：①IP-DECT xBS（8378，OXO 原生管理，ARI 绑定、GAP 注册、LED 六步）；②8328
    SIP-DECT 单基站（Web Admin 管理、SIP 接入 OXO、配 8214 手柄，细节见《8328 SIP-DECT SINGLE
    BASE STATION – System Guide》）；IBS 为另一 DECT 基站线（经 UAI/MIX 接入、ARI 与 IP-DECT 共用）。
  alias_or_related: ARI（p26 数值口径）；8214（g35）
  tags: [product, dect, base-station]

- id: g39
  term: Rainbow / Rainbow app
  category: product
  source_pages: p330-334, p346
  source_quote: |
    "Rainbow Is the cloud solution for team Collaboration and Unified Communications featuring phone
    and web calls, video conferencing, mobility, security and many APIs open to all developers" (p331)
    "The administrator can also use the Rainbow application installed on his PC to carry out the
    configuration/management operations of the company." (p346)
  definition: |
    ALE 云协作/UC 平台（UCaaS+CPaaS）：PC/Web/移动三客户端；Off-site mobility 的承载（p25）；管理
    操作（公司/成员/分机关联）可在 Web 或 PC 应用完成。本书中它是 OXO 的混合云对端。
  alias_or_related: web.openrainbow.com；hub.openrainbow.com；developers 入口见 CPaaS（p332）
  tags: [product, rainbow, platform]

# ── 五、协议与技术 (protocol) ──

- id: g40
  term: SIP / SIP Gateway / SIP Trunk Group
  category: protocol
  source_pages: p197-201, p208-214
  source_quote: |
    "This topology makes it possible to establish communications with all the equipment of network
    NGN" (p198)
    "OMC/External Lines/SIP/SIP Gateway/ • Create a new one • These infos are given to the client by
    the public provider" (p208)
  definition: |
    SIP=本书出局/对端互联的主协议（缩写全称书中未给出）：SIP Gateway 为 OXO 侧网关对象（九页签，
    f27）；SIP Trunk Group=中继组（Public 属性+通道数+Link-Cat）；注册与媒体参数（Registrar/
    Outbound Proxy/RTP Direct/带宽）由运营商提供。编解码与帧长口径见 p201。
  alias_or_related: TC1284/TC1994（g16、n43）；SIP 账户=认证三元组（Login/Password/Registered
    username，p214）
  tags: [protocol, sip, trunk]

- id: g41
  term: SBC / CE
  category: protocol
  source_pages: p198, p202
  source_quote: |
    "sbc.provider.com Session Border Controller … CE: Router/Firewall/NAT + SIP NAT" (p198)
    "CE: Customer Edge Router" (p202)
  definition: |
    运营商边界与会话控制组件：SBC（Session Border Controller，控制 SIP 会话边界）与 CE（Customer
    Edge Router，客户侧路由/防火墙/NAT+SIP NAT）；配套 Proxy（分发）/Registrar（注册认证）/
    Location（定位）/Gateway（SIP↔ISDN）。
  alias_or_related: 拓扑图（f26）；DNS A 记录指向（实验 192.168.1.250）
  tags: [protocol, sbc, topology]

- id: g42
  term: HTTPS / SRTP / TFTP / DHCP / DNS / NTP
  category: protocol
  source_pages: p14, p57, p108, p316, p371
  source_quote: |
    "This is due to the use of digital certificates (the IPDSP uses the HTTPS protocol)." (p14)
    "Communication flows between the WebRTC GW and Rainbow over the internet are secured with
    HTTPS and SRTP" (p371)
    "TFTP1: Enter the OXO Connect IP address 192.168.1.246" (p111)
  definition: |
    安全与基础设施协议在书内的角色：HTTPS=IPDSP 与 WebRTC 网关-Cloud 流的载体（证书时间敏感，n01）；
    SRTP=WebRTC 音频加密（与 HTTPS 并列，p371）；TFTP=IP 话机静态模式取配置（TFTP1 指向 .246）；
    DHCP=终端取址（OXO 内置服务器或外部）；DNS=域名解析（双 DNS 实验）；NTP=时间同步前提（p14/
    8328 NTP 设置）。
  alias_or_related: 证书管理在 Webdiag installer 会话（p69）
  tags: [protocol, security, infrastructure]

- id: g43
  term: DECT / GAP / IPUI / IPEI / ARI
  category: protocol
  source_pages: p119-122, p463
  source_quote: |
    "Enter the ARI number (11 digits in octal)" (p119)
    "Click on GAP registration … Click Assign as soon as the IPUI appears" (p121-122)
    "The IPEI number is no longer the generic/default number (FFFFFFFFFF)" (p463)
  definition: |
    DECT 体系对象：ARI=系统级注册根号（11 位八进制、IBS 与 IP-DECT 共用）；GAP registration=8378
    体系话机注册动作（出现 IPUI 后 Assign）；IPEI=话机身份号（8328 体系，注册前默认 FFFFFFFFFF）。
    四个缩写书内均未逐词展开。
  alias_or_related: PARI Dect Settings 菜单（p119）；8328 AC 码（p462）
  tags: [protocol, dect, registration]

- id: g44
  term: Webdiag
  category: protocol
  source_pages: p69, p141, p172, p241, p349
  source_quote: |
    "In OXO Connect, the certificates management is done through Webdiag installer session" (p69)
    "The "Group withdrawal status" menu allows you to view all the phones withdrawn from their group
    • Path: Services / Group withdrawal status" (p141)
    "OMC /Tools /Webdiag /Services /Rainbow Status" (p349)
  definition: |
    内嵌诊断 Web 工具（installer 会话登录）：服务状态（Rainbow Status）、系统与日志文件
    （ccrbagent.log）、证书管理、组退状态、已转移话机清单、TCP Dump 抓包（选 SIP 过滤、自动生成
    文件可交技术支持）。ETH1 场景下仅允许诊断与改 ETH0 参数。
  alias_or_related: ccrbagent.log=Rainbow agent 日志（p349）
  tags: [protocol, diagnostics, webdiag]

# ── 六、资源与数值 (resource) ──

- id: g45
  term: 资源键家族（RGM / RSL / RSP / RSB / RSD / 监督键）
  category: resource
  source_pages: p161-163
  source_quote: |
    "General resources (RGM): • To manage incoming and outgoing , internal and external calls
    Dedicated resources (RSL, RSP , RSB, RSD): • Local call (RSL): to reach and monitor an internal
    number • Special Physical Access (RSP): to select and monitor an access to make an external call
    • Special trunk group (RSB): to select a trunk group to make an external call • DID call key
    (RSD): to monitor DID calls" (p161)
  definition: |
    multiline 话机的资源键：RGM=通用资源（收发内外呼叫）、RSL=本地（监视内线号）、RSP=特殊物理接入
    （选中继口外呼）、RSB=中继组（选中继组外呼）、RSD=DID 监视；另有监督键（监视某话机某类呼叫）。
    默认配比见键 profile 表（Single line 3 虚拟键/key system 2RGM+nRSP/PCX 2RGM+2RSB）。
  alias_or_related: 缩写字根书内未展开（法系产品惯例）；键三类总框架（f23）
  tags: [resource, keys, multiline]

- id: g46
  term: MSG1-20 / Music on Hold / 集体缩位（Collective Speed Dial）
  category: resource
  source_pages: p243-245, p247-250, p280
  source_quote: |
    "According to the Software keys, the system can have 4 to 20 audio messages The total length of
    the messages is 320 seconds" (p244)
    "Music source … Default Music: The standard system music … Tape: Music from an audio source …
    Recorded Music: custom audio file (with .wav extension)" (p248)
    "OMC/collective speed dial Subscribers list / Details / speed dial Access to collective speed
    dial directory … barring" (p280)
  definition: |
    站点级音频与拨号资源：MSG1-20=预公告/欢迎消息池（默认 4 条、许可 20、总长 320s 动态分配、五种
    用途）；MoH=保持音乐三源（默认乐/Tape 音频输入/录制 .wav）按 Entity 1-4；集体缩位=系统级缩位
    目录（OMC/collective speed dial，受闭锁约束；时段转移的目标常绑缩位号）。
  alias_or_related: .wav 格式硬约束（p247）；DISA 等五种消息用途（p245）
  tags: [resource, audio, speed-dial]
```

### 任务覆盖自检（task↔id 映射）
- task-01（采集）→g06；task-02（FTR/部署）→g02/g03/g19；task-03（OMC）→g05/g29/g22；task-04（IP）→g04/g42；task-05（话机）→g07/g42；task-06（DECT）→g38/g43；task-07（编号）→g10/g14；task-08（组）→g09/g25；task-09（用户功能）→g08/g45；task-10（信箱）→g18；task-11（SIP）→g40/g41/g16；task-12（消息）→g46；task-13（呼入）→g09/g11；task-14（出局）→g12/g13；task-15（备份）→g20/g21；task-16（软件下载）→g05/g20；task-17（复位）→g21；task-18（安全）→g17/g42/g44；task-19（接入 Rainbow）→g39/g22；task-20（成员/分机）→g23；task-21（网关）→g01/g28/g26；task-22（虚拟终端）→g27/g28；task-23（话务台）→g24/g26；task-24（向导）→g06/g05。46 条术语覆盖 24 个 task 的全部关键概念，无遗漏。
