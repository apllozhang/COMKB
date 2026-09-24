# 框架/流程/结构候选 — Rainbow Hub (RAINXTE101EN Sprint 170 Ed16)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、平台/界面分区。实验环境给定值（IP/账号/号码/号段）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——产品定位 → 云侧开户 → 端侧供给 → 话务能力域 → 运营
  type: flow
  source_pages: p3-351
  source_chapter: COURSE STRUCTURE（全书章节顺序）
  source_quote: |
    "Rainbow Hub is the public version of the Rainbow platform. It allows users to migrate completely to
    the cloud thanks to a telephony system based entirely on softphone technology." (p5)
    "MAIN STEPS IN COMPANY SETUP: Creation of the company 1 ... Assigning Subscriptions 2 ... Creation of
    the Cloud PBX 3 ... Assigning Public Numbers 4 ... Creation of physical SIP phones 5 ... Creation of
    company members 6 ... Features management 7" (p51)
  summary: |
    课程按十四段推进：①产品概览（Rainbow/Hub 定位、混合 vs 全云、订阅与话机谱系）；②培训实验环境（POD、
    MicroSIP、RLAB）；③网络前提（Network Requirements + Pilot）；④公司与管理体系；⑤订阅；⑥Cloud PBX
    （声明/号码/闭锁/trunk/带宽/多站点/术语）；⑦设备谱系与 Generic SIP；⑧设备安装/网络/维护；⑨DECT；
    ⑩成员与话务配置；⑪群组（hunt/manager-assistant/supervision/emergency+录音）；⑫欢迎服务全家桶与
    IVR；⑬多站点；⑭分析+维护+培训收尾。p51 的"公司搭建七步"是前半本书的组织轴，后半本书按话务能力域并列展开。
  conditions: 无特殊版本前提；⑪-⑬ 各章互相独立，可按项目形态取舍
  tags: [flow, course-structure, delivery-order, master-flow]

- id: f02
  title: Rainbow 两条产品线对照图——混合云 vs Rainbow Hub
  type: diagram
  source_pages: p6
  source_chapter: OVERVIEW / Rainbow solutions
  source_quote: |
    "Connects existing enterprise telephony systems to the Cloud — Rainbow hybrid cloud, BUSINESS,
    ENTERPRISE & ATTENDANT subscriptions / Rainbow Hub — With Voice BUSINESS, Voice ENTERPRISE & Voice
    ATTENDANT subscriptions — Host all communication and telephony services in the Cloud" (p6)
  summary: |
    一页双图：左侧混合云线——客户侧保留 Remote PABX（OXO NOE/SIP），经 WebRTC Gateway 接云，订阅名
    Business/Enterprise/Attendant，定位"把现有企业话务系统连上云"；右侧 Hub 线——客户侧无 PBX，话务
    全部托管 Cloud PBX，订阅名带 Voice 前缀（Voice Phone/Business/Enterprise/Attendant），定位"把全部
    通信与话务服务放进云"。选型第一步即分清客户走哪条线；本教材只覆盖右线。
  conditions: 混合云线细节在 RAINXTE001EN（WebRTC 网关、OCE 拓扑），本教材不展开
  tags: [diagram, product-line, positioning, subscription]

- id: f03
  title: Rainbow Hub 全景图——云平台四大区块与客户侧零设施
  type: diagram
  source_pages: p7
  source_chapter: OVERVIEW / Global view
  source_quote: |
    "Cloud Rainbow Infrastructure: SIP CARRIERS / COLLABORATIVE SERVICES / ZERO TOUCH PHONES
    PROVISIONING / TELEPHONY & WELCOME SERVICES ... No VPN — No SBC — Customer site: Remote and nomadic
    workers" (p7)
  summary: |
    全景图：云侧 Rainbow 基础设施分四块——SIP 运营商接入（附认证运营商清单链接）、协作服务、话机零接触
    供应、话务与欢迎服务；管理面为"伙伴与最终客户统一管理界面"；客户站点只剩远程/移动工作者，明确标注
    无需 VPN、无需 SBC。数据安全与完整性为横幅要素。这是 Hub "无客户侧话务硬件"卖点的图形化表述。
  conditions: 认证运营商清单见 help.openrainbow.com（书中链接）
  tags: [diagram, architecture, cloud, zero-touch]

- id: f04
  title: 公司搭建七步主流程（Company Setup，全书前半部的组织轴）
  type: flow
  source_pages: p51
  source_chapter: RAINBOW HUB COMPANIES / Main steps in company setup
  source_quote: |
    "1 Creation of the company — 2 Assigning Subscriptions (Subscribe to offers Voice Phone, Voice
    Business, Voice Enterprise, Voice Attendant for a given number of users) — 3 Creation of the Cloud
    PBX — 4 Assigning Public Numbers — 5 Creation of physical SIP phones — 6 Creation of company members
    (Assign • Login • A phone number • A subscription) — 7 Features management (Hunt groups, emergency,
    manager / assistant, supervision, attendant • Welcome services • Calendars • Voice prompts • Music
    on hold • Automated Attendants)" (p51)
  summary: |
    端到端七步：①创建公司；②开 Voice 订阅；③建 Cloud PBX；④分配公网号码；⑤创建物理 SIP 话机（终端
    声明）；⑥创建成员并同时分配登录、号码、订阅；⑦功能管理（群组/紧急/经理助理/监督/话务台、欢迎服务、
    日历、语音提示、MoH、IVR 等）。与 RAINXTE001EN 六步法的差异：PBX 从"传统 PBX 接入"换成"Cloud PBX
    声明"，且"公网号码分配"单列为第 4 步。步骤 ①-⑤ 为 BP 专属动作（p49），⑥-⑦ 客户管理员可做。
  conditions: 步骤 2 的 Voice 订阅是步骤 3 声明 Cloud PBX 的前置（p75 Warning）
  tags: [flow, company-setup, master-flow, seven-steps]

- id: f05
  title: Cloud PBX 创建四步流——公司 → Voice 许可 → 声明 → 运营商开线
  type: flow
  source_pages: p80
  source_chapter: CLOUD PBX / Steps to create a Cloud PBX
  source_quote: |
    "CREATION OF THE COMPANY — A Rainbow company is always created in the same way, whether the
    communication server is traditional or in Full Cloud mode. / 'VOICE' LICENSE ALLOCATION — To be able
    to create a Cloud PBX as a communications server, you need at least a 'Voice' license. Without this,
    you'll only see traditional PBXs: OXO Connect, OmniPCX Enterprise, Third party PBX, etc. / CREATING
    THE CLOUD PBX / TELEPHONE LINES — Via the provider's order portal (channels, lines: portability or
    ordering new DIDs)" (p80)
  summary: |
    四步：①公司创建（与混合云同一套建司流程）；②分配 Voice 许可——没有 Voice 许可时界面里只看得到
    传统 PBX 类型，选不到 Cloud PBX；③声明 Cloud PBX（名称/类型/trunk/编号计划）；④电话线经运营商
    订购门户开通（通道、线路：携转或新订 DID）。步骤 ④ 完全在运营商/伙伴侧，本教材不展开。
  conditions: 步骤 2-3 为 BP 权限；步骤 4 依赖所选 traffic provider
  tags: [flow, cloud-pbx, creation, provisioning-order]

- id: f06
  title: Cloud PBX 能力分区图——话务/群组/欢迎服务三族
  type: structure
  source_pages: p78-79
  source_chapter: CLOUD PBX / Cloud PBX & Example of features
  source_quote: |
    "The Cloud PBX is a soft SIP PBX used to: • Connect ALE and generic SIP devices (e.g. Doorphone,
    third-party DECT SIP, analog/SIP box...). • Connect a public SIP provider via a trunk to make
    external calls. • Manage telephony features • Number of call channels: unlimited • Number of
    telephone lines: unlimited" (p78)
  summary: |
    Cloud PBX 向公司成员提供：Rainbow 用户与公网互打、话务组与自动话务员、软话机与话机设备集成、语音
    信箱、欢迎服务与日历、组话务。特性两族：话务特性（话机查通讯录、呼叫控制、第二路呼叫、转移、保持、
    代接、呼转溢出、N 方会议、来话录音、话机状态与 Rainbow 在场合并、多终端、单号同振）；其他特性
    （hunt/supervision/manager-assistant 组、闭锁、话务台、留言、欢迎服务与日历、可定制语音引导、IVR、
    紧急呼叫）。
  conditions: "Given as an example - Non-exhaustive list"（p79 原文自注）；全量以 Features List 为准
  tags: [structure, cloud-pbx, features, capability-map]

- id: f07
  title: 用户终端三形态结构——纯软话机 / 软+硬（RCC）/ 纯硬话机
  type: structure
  source_pages: p110-112
  source_chapter: RAINBOW HUB DEVICES RANGE / Types of devices for a user
  source_quote: |
    "SOFTPHONE — Only one mode: Computer (internet calls). Calls are received on Rainbow, PC and mobile
    clients." (p111)
    "SOFTPHONE AND DESKPHONE — Desk phone | Softphone: Computer (Internet calls) ... RCC* — *RCC: Remote
    Call Control, supervision and control of the desk phone from the application. Outgoing calls from
    the desk phone, softphone or mobile" (p112)
  summary: |
    终端形态三分：①纯软话机（Rainbow Client，PC 和/或智能手机，可选配话机）只有 Computer 一种模式
    （互联网呼叫）；②软+硬组合——来话按选择在话机或软话机呈现，应用对物理话机做 RCC 监督控制，去话
    可从话机、软话机或手机任一发起；③纯硬话机（Voice Phone 订阅档，p67：无 Rainbow 应用，仅话机/DECT）。
    该结构决定订阅选型与许可成本（对照 p67 订阅表）。
  conditions: "Note: in virtual classroom, there is no deskphones. Only softphone configuration."（p16）
  tags: [structure, devices, softphone, rcc, terminal-forms]

- id: f08
  title: Myriad/ALE 话机谱系与档次矩阵
  type: structure
  source_pages: p9, p106-107
  source_chapter: OVERVIEW / Rainbow Hub user subscriptions & DEVICES RANGE
  source_quote: |
    "Myriad range Deskphones: • M8 • M7s Pro • M7s • M5s • M3s / ALE range Deskphones: • ALE-300 •
    ALE-400 • ALE-500" (p9)
    "Myriad M7 | Myriad M5 | Myriad M3 | ALE-2 | DECT 8214 ... Screen Colour screen 3,5'' | 2,8'' | 1,6''
    ... Extension module EM200 For M3-M5-M7 desktop phones Colour screen, Up to 10 pages of 20 LED keys"
    (p107)
  summary: |
    话机两族五档：Myriad M7/M5/M3（彩屏 3.5"/2.8"/1.6"，M7 超宽频仅免提模式，M5/M7 支持 BT4.1 耳机与
    Audio Hub，EM200 扩展模块最多 10 页×20 LED 键）；入门 ALE-2 与 ALE-300/400/500；无线 DECT 8214
    （仅欧洲与亚洲）。Myriad 支持 zero-touch 与用户-话机同步（DND/呼转/全局目录搜索）。兼容第三方场景
    走 Generic SIP（门铃、传真、模拟网关等，p106）。
  conditions: "the descriptions on this site are generic and do not necessarily apply to the Rainbow Hub context"（p107 关于 aledevice.com 链接的自注）
  tags: [structure, devices, myriad, portfolio]

- id: f09
  title: Generic SIP 设备接入原则与部署三阶段（before/during/after）
  type: structure
  source_pages: p114-123
  source_chapter: GENERIC SIP DEVICES
  source_quote: |
    "Generic SIP devices: • No centralized configuration • Must be configured manually • No automatic
    firmware updates • No remote call control (RCC) • Basic SIP telephony services • Use the secure SIP
    protocol to communicate with Rainbow Hub. Required information: SIP domain • SIP username • SIP
    password • Rainbow server certificate chain" (p117)
    "Before deployment: Test interoperability, Validate codecs, Verify certificates / During: Enable
    TLS/SRTP, Document configurations, Verify firmware / After: Monitor SIP registration, Check audio
    quality, Collect logs" (p119)
  summary: |
    接入原则六条：无集中配置、纯手工、无固件自动更新、无 RCC、仅基础 SIP 话务、走安全 SIP；所需四要素
    （SIP 域、用户名、密码、Rainbow 服务器证书链）都从管理界面取。部署三阶段清单：部署前测互操作/编解码/
    证书，安装中开 TLS/SRTP/记录配置/核固件，部署后盯 SIP 注册/音质/收日志。配套：8 款参考设备配置指南
    （Yealink/Snom/Poly/Grandstream，p122）与"Setting up Rainbow Hub to interconnect third-party SIP
    extensions"支持文章（p117）。
  conditions: ALE 定性为"互补方案"，不为大规模第三方话机部署提供支持（p120）
  tags: [structure, generic-sip, third-party, principles, checklist]

- id: f10
  title: Zero-Touch 部署机制全链路——注册 → 关联 → 自动取配 → 注册态可视
  type: flow
  source_pages: p134-139
  source_chapter: DEVICES INSTALLATION AND NETWORK REQUIREMENTS
  source_quote: |
    "Devices registration is on based their MAC addresses: • MAC address configured by the administrator
    (Manual declaration of MAC addresses | Bulk import via csv file) • At the creation of the device • Or
    at the creation of the member. Each devices created must be associated with a member" (p135)
    "A Myriad device leaving the factory has a different software version ... The device will update
    itself once associated with a Rainbow Hub user. You may need to reboot your device several times ...
    (around 5 to 10 minutes)." (p137)
    "Check that a device is correctly registered: green dot in front of the name of the registered user,
    bottom left of the screen." (p136)
  summary: |
    机制链路：①管理员按 MAC 声明设备（建设备时或建成员时，手工或 CSV 批量；Generic SIP 也可批量导入）；
    ②设备必须关联到成员（每用户账号仅一台物理 SIP 设备，p134）；③设备上电后经 DHCP 自动取 IPv4 参数并
    连云取配置与固件（多次重启共 5-10 分钟）；④验收看屏：已注册用户名前绿点。异常面：DHCP option
    43/66/67 覆盖 zero-touch 指向、LAN 有 PBX 时 TFTP 抢先、未分配设备报 Config Failed（详见 n 系）。
  conditions: 仅 Myriad/ALE-2/DECT zero-touch 线适用；Generic SIP 无此机制
  tags: [flow, zero-touch, provisioning, myriad, mac]

- id: f11
  title: Generic SIP 手工配置主步骤与批量导入流
  type: flow
  source_pages: p124-131
  source_chapter: GENERIC SIP DEVICES / Manual configuration & Bulk import
  source_quote: |
    "MANUAL CONFIGURATION: MAIN STEPS • Create the device • Select the device type • Choose: « Generic
    SIP » • Settings Management • MAC address • SIP domain • SIP password • Certificates • Configure the
    SIP device" (p125)
    "BULK IMPORT • File import • Devices created • Link devices to Rainbow accounts (manually or via bulk
    import) • Configure SIP Devices ... Required settings • Action: create, update, delete • MAC address
    • Device type • SIP password – only for the Generic SIP devices" (p129)
  summary: |
    手工线三步：建设备选类型 Generic SIP → 管理设置（MAC、SIP 域、SIP 密码、证书——证书链在编辑设备页
    下载，p127）→ 在终端侧配网络与 SIP。批量线：下载模板 → 填 action/MAC/设备类型/SIP 密码（仅 Generic
    SIP 需要）→ 上传导出报告 → 设备建好后回连 Rainbow 账号 → 再到终端侧配置。模板同时覆盖 ALE 设备与
    Generic SIP，可建/改/删。
  conditions: 证书链下载入口 = 编辑设备页（p127）；导入后必须手工回连账号（p131）
  tags: [flow, generic-sip, manual-config, bulk-import, certificates]

- id: f12
  title: DECT 两档方案结构——8328 单/双站 vs 8368 多站
  type: structure
  source_pages: p147-150
  source_chapter: DECT MOBILITY
  source_quote: |
    "8328 SIP-DECT Single base station which permit a coverage with one or two base stations only. •
    8368 SIP-DECT Multi cell base station which permit a large coverage with one to 254 base stations"
    (p148)
    "8328 base stations and 8214 & 8262 handsets • 1 or 2 base stations/site • Up to 20 DECT handsets ...
    Up to 20 handsets and 10 simultaneous calls." (p149)
    "8368: Up to 254 base stations • Up to 40 handsets/base stations ... Up to 1000 handsets (40 per base
    station) • Up to 10 simultaneous calls per base station" (p150)
  summary: |
    两档：小安装用 8328（含带脚座版）——1-2 站/点、最多 20 手持机、10 路并发、尺寸 95×93×24mm、以太网
    10/100 PoE；大安装用 8368（室内 144×140×35mm 壁挂内置天线 / 室外 365×210×65mm IP55 外置天线）——
    最多 254 站、每站 40 手持机、全系统 1000 手持机、每站 10 路并发。覆盖半径均 50-300m，站间无缝切换。
    两档都支持经 CAT-iq 协议对接本地告警服务器（已验证 F24、Newvoice，Tamat 进行中）。手持机两型：8214
    办公型、8262（PTI）恶劣环境/独行工人型。
  conditions: DECT 8214 仅欧洲与亚洲供货（p9/p107）
  tags: [structure, dect, 8328, 8368, mobility]

- id: f13
  title: DECT Zero-Touch 管理流程——基站声明/终端 IPEI 注册/远端重启
  type: flow
  source_pages: p151-152
  source_chapter: DECT MOBILITY / Managing SIP-DECT infrastructure
  source_quote: |
    "Base stations 8328 or 8368 – Zero Touch: Create base stations with their MAC address. 8328 base
    station: mono or dual cell. 8368 base station: multi cell ... 8368 DECT base station only: an IP
    address is required to identify the main station. Secondary DECT stations need this address to
    communicate with the main station. Once a DECT base station is seen online, it can be restarted
    remotely." (p151)
    "DECT 8214 & 8262 terminals – Zero Touch: 1. Register a new '8214 DECT Handset' or '8262 DECT
    Handset' with its IPEI number 2. Associate it with an existing user who does not already have a
    physical terminal 3. Associate this terminal with the desired base station 4. The new terminal
    appears in the list in the 'Phones' tab" (p152)
  summary: |
    基站线：按 MAC 建站（8328 选 mono/dual，8368 选 multi）→ 8368 需录主站 IP（副站靠它找主站）→ 上线
    后可远端重启。终端线四步：按 IPEI 注册（选精确型号 8214/8262，不用 Generic SIP）→ 关联到尚无物理
    终端的用户 → 挂到指定基站 → 在 Phones 页签按类型过滤查看。副站创建条件：8328 已声明为 dual 且无副站，
    或 8368（上限 253 台以内）。
  conditions: 手工模式先装的基站不会自动转 zero-touch；同一客户可一站手工一站零接触，但每站点内方法要统一（p151）
  tags: [flow, dect, zero-touch, ipei, base-station]

- id: f14
  title: 成员创建四法（手动/邀请/CSV/AAD）+ LDAP 连接器第五通道
  type: structure
  source_pages: p167-170, p178-179
  source_chapter: COMPANY MEMBERS / Members creation & LDAP connector
  source_quote: |
    "Members can be created: Manually • Creation one by one • By invitation • Via email address ... By
    bulk import • From .CSV file (UTF-8) • Microsoft Azure Active Directory • Also allows contact search
    • LDAP" (p167)
    "This connector offers a choice of three functions: 1 Automatic synchronization of Rainbow users...
    2 Automatic synchronization of AD contacts in the Rainbow Business Directory ... 3 Synchronize
    calendar presence with Exchange Server." (p179)
  summary: |
    建户通道：①手动逐个（当场定全字段）；②邮件邀请（noreply@openrainbow 发信，用户自设密码后管理员补
    配）；③CSV 批量（UTF-8 模板，建/改/删、按 MAC 绑设备、SSO 时密码列留空）；④Azure AD（同步建/改/删
    + 通讯录搜索，需先把 AAD 关联到公司且限 Voice Enterprise 管理员，关联本身不触发自动供应）；⑤LDAP
    连接器（AD→Rainbow 单向用户同步、AD 联系人进企业目录、与 Exchange Server 同步日历在场——三项可自选）。
    相比混合云教材，Hub 新增 LDAP 项与"成员带 Sites 字段"（p171）。
  conditions: AAD 导入限 Voice Enterprise 服务等级（p167）；LDAP 连接器免费安装于客户侧 Windows server（p179）
  tags: [structure, members, csv, azure-ad, ldap]

- id: f15
  title: 成员设置分区——信息/权限/电话/可编程键/服务/角色/安全 七大块 + 标签/档案/Sites 横向项
  type: structure
  source_pages: p171-175
  source_chapter: COMPANY MEMBERS / Member settings & Tags / User profiles
  source_quote: |
    "Information •Identifier, last name, first name, language, country •Timezone: voicemail timestamp
    •Visibility ... •Tags ... •Sites: for a multisite company / Permissions ... Phone •Equipment: Cloud
    PBX of the company •Extension number and public number •Physical device associated (optional) ...
    Programmable keys ... Services (subscription) •Voice Business, Voice Enterprise, Voice attendant,
    Voice phone / Roles •Administration: Yes/No, Business directory, Channels / Security •Modify
    password, identifier & authentication method" (p171)
  summary: |
    成员编辑页七分区：Information（含时区——留言时间戳依据；可见性；标签；多站点公司的 Sites 字段）、
    Permissions、Phone（设备=Cloud PBX、内线/公网号、可选物理设备、话务特性）、Programmable keys（应用侧
    +话机侧）、Services（Voice 四档）、Roles（管理员/企业目录/频道）、Security。横向两项：Tags（手工或
    批量打标优化搜索）与 User Profiles（公司级定义、按用户定制的功能限制档案，p175）。总览口径"八块"=
    7 分区 + Tags/Profiles 横向项。
  conditions: 语音信箱在分配号码时自动开通，容量 30 分钟（p172）
  tags: [structure, member-settings, profiles, sites]

- id: f16
  title: 个人例行程序（Personal Routines）机制——一键切换五类参数
  type: structure
  source_pages: p173-174
  source_chapter: COMPANY MEMBERS / Personal routines
  source_quote: |
    "Predefined and customizable scenarios allowing to modify simultaneously your presence, caller ID and
    forwarding status. ... Change your status • Your caller ID • Device to make calls • Call forwarding
    and destination • Withdrawal from groups" (p173)
    "Set your personal routine as 'Do not disturb' to forward all incoming calls to your assistant. • If
    your personal routine 'Out of office' is enabled, all incoming calls are forwarded to your mobile
    phone and the presence is set to 'Away'" (p174)
  summary: |
    例行程序=场景包：把在场状态、主叫 ID、呼叫设备、呼转与目的地、退出组五类参数打包，一键启停（每参数
    可单独启停）。预置四场景：At Work / Do Not Disturb / On Break / Out of office（p8）。典型脚本：DND
    → 全部来话转助理；Out of office → 来话转手机+在场 Away。成员端（头像 → Personal routines →
    Configure）与管理端均可配。
  conditions: 参数可逐项启用/停用（Each choice can be enabled or disabled）
  tags: [structure, routines, presence, forwarding]

- id: f17
  title: 按键组（Key Groups）机制——话机键+应用键批量下发
  type: flow
  source_pages: p182-187
  source_chapter: COMPANY MEMBERS / Key groups & Mass provisioning
  source_quote: |
    "You can easily assign programmable keys to Cloud PBX desk phones and the Rainbow softphone
    application by creating key groups • For desk phones: supported keys include speed dial, supervision,
    call forwarding, audio hub functions… • For Rainbow app softphone: direct call keys are available."
    (p183)
    "Bulk provisioning allows you to associate previously created key groups when creating USER accounts.
    • 2 entries • Deskphones key groups • Softphone key groups" (p187)
  summary: |
    机制：先建键（话机键：速拨/监督/呼转/Audio Hub；应用键：直呼键）或先建组，把键勾进组并排序 → 编辑
    成员把"应用键组/话机键组"分配下去（p186 两个分配位）。批量供应联动：CSV 建用户时用两列（话机键组、
    软话机键组）直接带组，组名自动出现在模板注释行。价值是"一次配置、全队对齐"。
  conditions: 先建键或先建组均可（You may create keys before assigning them to a group OR create a group first）
  tags: [flow, key-groups, provisioning, softphone, deskphone]

- id: f18
  title: 四类组总览表（Regular/Attendant/Emergency/Manager-Assistant）
  type: structure
  source_pages: p209
  source_chapter: GROUPS OVERVIEW / The different types of groups
  source_quote: |
    "1 REGULAR — All classic cases of call taking in a team (after-sales service, hotline, order taking,
    etc...). With or without waiting queue | 2 ATTENDANT — Mutualize the reception, for example between
    different sites of a company | 3 EMERGENCY — Regulatory case ... 'security station' | 4 MANAGER /
    ASSISTANT — Manager wishing to delegate the management of its calls (filtering)" (p209)
    "Notes: All members must have a Voice Attendant license ... 1 Manager , 1 to N assistants" (p209)
  summary: |
    组四类：Regular（日常团队接听，可带/不带等待队列，分发 Parallel/Serial/Circular）；Attendant（多址
    共享前台，分发 Parallel，全员须 Voice Attendant 许可）；Emergency（监管场景安保站，法国 112）；，
    Manager/Assistant（经理委托过滤，分发 Serial，1 经理-1..N 助理）。溢出目的地统一为：语音提示/成员/
    hunt group/内线/公网号/AA/留言信箱。角色两维：Agent & Administrator（前三类）与 Manager/Assistant
    （第四类）；* 号注明 Manager/Assistant 的 Administrator 功能后续版本提供。
  conditions: 管理员可管组（溢出、DDI、加成员）并看全部话务统计（p209）
  tags: [structure, groups, taxonomy, hunt-group, attendant, emergency]

- id: f19
  title: Hunt Group 三分发模式与轮转时序图
  type: diagram
  source_pages: p210-211
  source_chapter: HUNT GROUPS / Hunting groups
  source_quote: |
    "Serial — Calls are routed on the first member of the list if free… if no answer the next member will
    be called. / Circular — Users are ringed each in turn / Parallel — All members are called
    simultaneously ... If overflow 60 secondes by default / Rotation 10 s by default" (p210-211)
  summary: |
    三模式：Parallel（组内全员同振）；Serial（按列表顺序，首位空闲先振，无应答转下一位）；Circular（轮流
    振铃轮转）。时序参数：Serial/Circular 每轮 10 秒（Rotation 10 s by default）；溢出默认 60 秒（图示）。
    建组参数页进一步明确：轮转定时仅对 serial/circular 有效，默认 10 秒（p234）。
  conditions: 分发同时作用于软话机与话机（p212）
  tags: [diagram, hunt-group, distribution, timers]

- id: f20
  title: 等待队列机制——有/无队列行为对比与溢出参数
  type: flow
  source_pages: p215-216
  source_chapter: HUNT GROUPS / About waiting queues & Real-time queue status
  source_quote: |
    "In a group WITHOUT waiting queue: Callers are routed to overflow when all the agents are already on
    the line ... In a group WITH waiting queue: The caller is put on hold until an agent can handle the
    call ... the oldest call on hold is presented (first come, first served), after a 10 sec delay • If
    the waiting time exceeds the overflow time (adjustable from 10 to 900 sec), the call is overflowed
    according to the strategy defined at group level." (p215)
  summary: |
    队列两态：无队列组——全员占线即溢出（客户易流失）；有队列组——先播"尽快接听"提示，按 FCFS 在 10 秒
    延迟后把最老来话派给空闲坐席，等待超时可调上限（10-900 秒）后按组策略溢出（语音提示/成员/组/内线/
    公网号/AA/留言/欢迎服务），另有"组空即立即溢出"选项。实时状态可视化：可接听坐席数、进行中呼叫数
    （含最长时长）、排队数与最长等待，坐席与管理员均可见（p216）。
  conditions: 带队列组建法与不带相同（分发/坐席/管理员/溢出通用）
  tags: [flow, waiting-queue, overflow, fcfs]

- id: f21
  title: 组内角色权限表——Agent vs Administrator 能力矩阵
  type: structure
  source_pages: p214
  source_chapter: HUNT GROUPS / Roles in a group
  source_quote: |
    "Agent | Administrator — Receive group calls ◼ X ... View, download, share and delete group voice
    messages ◼ ◼ ... Putting an agent on hold, in activity X ◼ ... Add or remove a member X ◼ ... Force
    open or close a group-related Welcome Service X ◼" (p214)
  summary: |
    权限两极：Agent 只多"接收组呼叫"与"改自己状态（withdrawn/active）"两项独占；Administrator 拥有管理
    面（看/删组留言与通话记录、挂起/激活坐席、看统计、加减成员、改公网号、改溢出模式与时长、黑名单增删、
    强制开关组关联欢迎服务），不接组来电。非坐席管理员对坐席呈现为"永久 withdraw"。要点：可以给不接电话
    的人只授 Administrator。
  conditions: "the non-agent administrator is seen as being permanently withdrawed"（p214）
  tags: [structure, roles, agent, administrator, permission-matrix]

- id: f22
  title: 组语音信箱与协作 bubble 自动联动机制
  type: diagram
  source_pages: p217
  source_chapter: HUNT GROUPS / Voice mail
  source_quote: |
    "When a group is created, an exchange bubble is automatically created. It includes all the members of
    the group, in order to allow: • Instant messaging, file sharing • Conferences between group members •
    Management of the group's voice messages • Access to call logs. A voice message is automatically
    transferred to the corresponding bubble as an audio file." (p217)
  summary: |
    每建一个组自动生成一个对应 bubble（协作群）：组内全员在列，用于群内 IM/文件/会议、组语音留言管理与
    组通话记录查看；组留言自动以音频文件转入该 bubble；bubble 内全员权限相同。这是"话务组"与"协作空间"
    的绑定关系——删组建组都会联动 bubble 生命周期（联动细节书内未展开）。
  conditions: 组通话记录分"已处理/未接/已溢出"，存于组 bubble
  tags: [diagram, voicemail, bubble, group]

- id: f23
  title: Manager/Assistant 组结构与筛选边界图
  type: diagram
  source_pages: p218-221
  source_chapter: MANAGERS/ASSISTANTS GROUPS
  source_quote: |
    "Allow to an assistant to filter and take Manager's calls. ... Only telephone calls are filtered. If
    Rainbow audio calls are allowed, they are not filtered. / Overflow: Manager → Assistant 1 → Assistant
    2 ... This type of group is necessarily single-Manager. To create a multi-Manager group, it is
    necessary to create several groups" (p219)
    "The DID of the Manager who wants to be able to screen his calls must be assigned to the group level,
    and not to the manager." (p221)
  summary: |
    结构：单经理组（多经理=建多个组，助理可跨组）；溢出链 Manager→助理 1→助理 2；任何有内线号+设备的
    成员都可任经理或助理；组可作欢迎服务/AA/其他组溢出的目的地。筛选边界：只筛电话呼叫，Rainbow 音视频
    呼叫不筛。应用两视图：经理（接听/仅通知/开停筛选），助理（开停经理筛选/代接/管多个经理）。配置要点：
    想让经理筛选来话，经理 DID 必须配在组级而非经理个人；溢出到语音提示可定制文案，时长 5-30 秒（p221）。
  conditions: 组管理同 hunt group（内线/公网/录音/溢出/成员/提示音）
  tags: [diagram, manager-assistant, filtering, did]

- id: f24
  title: Supervision 组与话务台结构——订阅门槛、5/30 规格、三种显示
  type: structure
  source_pages: p223-225, p245-247
  source_chapter: SUPERVISION GROUPS & WELCOME SERVICES / Attendant console
  source_quote: |
    "A supervisor must have one of the following levels of service: • Voice Attendant: Supervision-Pickup-
    Transfer & 10 Calls in queue • Voice Business & Enterprise: supervision-pickup-transfer. Limits: • 5
    supervision tabs for one user • 30 members in a group (Supervisors + Supervisees) • A user can be a
    supervisor in up to 5 groups" (p224)
    "Warning: Members with voice attendant subscriptions cannot use: • Attendant mode on the Rainbow
    mobile application • Their telephone set. If configured: the phone set association is deleted after
    activation of the attendant console." (p246)
  summary: |
    监督组结构：监督员+被监督成员同组，监督员订阅分级——Voice Attendant 可用完整话务台（监督-代接-转移
    +10 路排队），Voice Business/Enterprise 只有监督-代接-转移。规格：每用户 5 个监督页签、每组 30 人、
    每人最多当 5 组监督员。话务台能力：监控被监督成员（在场+话务活动）、代接/转移、10 路保持、改成员例行
    程序；三档显示 Normal/small/condensed。硬约束：Voice Attendant 用户不能用手机端话务台模式、不能用
    自己的话机——激活话务台后话机关联会被删除。
  conditions: 话务台需 Voice Attendant 订阅（p246）
  tags: [structure, supervision, attendant-console, limits]

- id: f25
  title: 紧急呼叫链路——免前缀直达组、0112 转外线、定位责任链
  type: diagram
  source_pages: p226-229
  source_chapter: SUPERVISION GROUPS / Emergency numbers & Emergency group & Localization
  source_quote: |
    "Allows calls to emergency numbers • Without dialing the outbound prefix. i.e. '9' • For users
    subject to external barring ... Emergency numbers are reserved and cannot be changed. You cannot
    assign them as internal numbers to users." (p227)
    "Active group -> Direct calls (without outbound prefix) to emergency numbers are routed to the group
    and not to the outside. To transfer an emergency call to the public emergency number, emergency group
    members must dial the emergency number preceded by the external prefix (e.g. 0112)." (p228)
    "Rainbow doesn't manage DID location in this model where DIDs are managed by the Business Partner.
    Business Partners have to declare DID addresses into the SIP provider database ... Identification of
    the relevant PSAP is under the responsibility of the SIP provider." (p229)
  summary: |
    三段链路：①号码面——紧急号码按公司国家+trunk 自动配置，免出局前缀可拨，且对受闭锁用户（仅内线）也
    放行，支持录音；号码保留不可改、不可占作内线号。②组面——唯一一个紧急组，激活后免前缀紧急呼叫改路由
    到组而非外线；组员转公共紧急号要加前缀（0112）。③定位面——架构图：BP 购号时把 DID 地址登记进 SIP
    运营商数据库，呼叫经 Rainbow SIP Edge 到运营商，由运营商把 DID 位置映射到正确 PSAP；Rainbow 不管
    DID 定位。
  conditions: 国家号码表缺失时联系 ALE Rainbow 团队并提交监管机构号码表（p227）
  tags: [diagram, emergency, psap, localization, compliance]

- id: f26
  title: 通话录音体系——触发面、存储与 Rainbow Exporter 归档
  type: structure
  source_pages: p230-231
  source_chapter: SUPERVISION GROUPS / Call recording
  source_quote: |
    "Retrieve recordings: Find in this tab all recordings automatically triggered on your members, groups
    or phone lines. RECORDINGS ARE STORED FOR 2 MONTHS. The 'Recordings' tab is only accessible by the
    end-customer administrator of the solution, for confidentiality reasons. ... for customers with legal
    archiving needs beyond 2 months, it is possible on request to implement 'Rainbow Exporter', which
    copies all recordings daily to Google Drive, or to a customer's own SFTP storage server" (p231)
  summary: |
    录音体系：触发面三层（成员/组/线路，组级在组建时按 all/external/internal/none 配置，p235）；Recordings
    页签汇总全部自动触发的录音；存储 2 个月、不占用户存储配额；访问仅限最终客户管理员（保密理由）。超期
    归档：Rainbow Exporter 按日全量拷贝到 Google Drive 或客户自有 SFTP，需另行购买（pricing on request）。
  conditions: 归档为可选付费项，合同与合规口径在书外
  tags: [structure, recording, retention, exporter]

- id: f27
  title: 欢迎服务四件套关系图——日历/语音提示/欢迎服务/IVR
  type: diagram
  source_pages: p250-252
  source_chapter: WELCOME SERVICES / Items of the welcome's services
  source_quote: |
    "A calendar makes it possible to define opening and closing days and hours which will be applicable
    upstream of a welcome service or an automated attendant / Voice prompts that will be played to your
    callers ... / Combination of a calendar and voice prompts to welcome your callers ... / Automated
    welcome of your callers and offer them DTMF choices to route them within your organization" (p251)
    "CALENDARS: Create/Modify/Delete — WELCOME SERVICES: Create/Modify/Delete — AUTO ATTENDANT:
    Create/Modify/Delete/Duplicate — VOICE PROMPTS: Menu management" (p252)
  summary: |
    四件套关系：日历定义开/闭时段（上游，供欢迎服务或 IVR 引用）；语音提示是播放给主叫的素材库；欢迎服务
    =日历+提示音的组合体（开/闭分别路由）；IVR=自动欢迎+DTMF 选择路由。管理动作：日历增删改、欢迎服务
    增删改、IVR 增删改+复制、语音提示菜单管理。两套管理步骤（p253）：无 IVR（载提示音→建日历→建欢迎服务
    →客户确认→测试）；带 IVR（载全部提示音→日历→欢迎服务→IVR 建管→确认→测试）。
  conditions: 日历必须先于欢迎服务创建（p259）
  tags: [diagram, welcome-services, calendar, ivr, voice-prompts]

- id: f28
  title: Welcome service 开/闭双路由图与强制开关
  type: diagram
  source_pages: p258-260
  source_chapter: WELCOME SERVICES / Welcome service
  source_quote: |
    "During opening hours, a welcome guide (pre-announcement) is played to the caller before routing him
    to the destination which may be: • A member • A group of members, with queue, attendant • An
    automated attendant • A direct transfer to the voicemail. During closing hours, incoming calls are
    routed to: • A closing voice prompt • A Member • A group of members with or without a waiting queue,
    attendant • An external number • A welcome service • An automated attendant" (p258)
    "It is possible to override predefined schedules and manually force the closure of a welcome service
    if necessary. ... The service that has been closed appears in 'forced' mode. At the next time slot,
    the mode returns to 'Auto'." (p259)
  summary: |
    来话入口是欢迎服务的公网号：先查日历——开时段播欢迎引导（pre-announcement）再路由到 成员/带队列组/
    话务台/AA/直转留言；闭时段路由到 闭店提示音/成员/组/外线号/另一欢迎服务/AA。人工强制：可提前闭店或
    强开，强制态显示 forced，下一时段自动回 Auto。特例（p260）：建好欢迎服务后出现"定制语音引导"按钮，
    可给特定时段/日期配专属提示（如午休、盘点），优先于日历——上限 5 条定制提示、10 个特殊日。
  conditions: 每个欢迎服务绑定一个公网号与一份日历（p258）
  tags: [diagram, welcome-service, routing, forced-mode]

- id: f29
  title: IVR 结构图——3 级菜单、0-9 选择、两种入口
  type: diagram
  source_pages: p265-271
  source_chapter: WELCOME SERVICES / Automated attendant
  source_quote: |
    "Each IVR has a maximum of 3 levels, each allowing a DTMF selection from 0 to 9. • The root menu
    contains 10 configurable entries. ... The destination can be either: A group with or without a queue,
    a member, another IVR menu, a welcome service. • Submenus are also available." (p266)
    "An automated attendant can be reached via a dedicated public number or via a welcome service. •
    Direct call via DDI (in this case, the IVR is in service 24/7) • Access via a welcome service with a
    calendar" (p266)
  summary: |
    IVR 结构：每级菜单 10 个 0-9 DTMF 入口（根菜单 10 项可配），最多 3 级，目的地可为组（带/不带队列）、
    成员、另一 IVR 菜单、欢迎服务，支持子菜单。两种入口：直挂公网号（DDI 直达，7×24 服务，可选溢出目的
    地 6 种：语音引导/内线/AA/欢迎服务/成员/组，p267）；经欢迎服务进入（日历控制，开时段进 IVR、闭时段走
    闭路由，此时 IVR 不带 DID，p268）。语音提示两模式（p270）：每菜单一条唯一提示（0-9 选项录进一个 wav，
    建时选定且事后不可改，官方"强烈推荐"）或每选项+每动作分别录音。无数量与许可限制（p266）。
  conditions: 保密规则：来话显示默认名而非欢迎服务技术号（p269）
  tags: [diagram, ivr, aa, dtmf, menus]

- id: f30
  title: 多站点结构图——单 Cloud PBX 下的站点逻辑分区
  type: diagram
  source_pages: p301-305
  source_chapter: MULTI-SITE CLOUD PBX
  source_quote: |
    "Each site is associated with: • One or more members of the company • One or more public numbers ...
    Configure a default public number for a site • When members linked to a site without an assigned
    public number make outgoing calls, the public number seen by the called party is the site's public
    number. • Custom music on hold per site." (p303)
    "Regardless of the multi-site configuration, the following functions remain unchanged within the
    company: • Internal calls are available between company members at different sites. • Members of a
    company belonging to a group ... may belong to different sites. • Welcome services/AA are common to
    all sites. ... The company directory is common to all sites." (p304)
  summary: |
    站点模型：一个公司仍只有一个 Cloud PBX；站点挂成员、公网号与服务（组/欢迎服务/AA 经公网号归属站点），
    可设站点默认公网号（未配个人号的站点成员外呼显示站点号）、站点级音乐保持、站点独立问候语配置。跨站点
    不变量：内呼互通、组成员可跨站、欢迎服务/AA 全公司共用（可经号码标识归属）、目录全站共用、一个号码可
    同时充当公司主号与站点主号、不强制所有号码/成员都挂站点。实施四步（p305）：建站点 → 分配用户 → 号码与
    服务关联 → 站点 MoH。
  conditions: 每站内部分机号段分段便于管理但非强制（p92）
  tags: [diagram, multi-site, sites, cloud-pbx]

- id: f31
  title: 分析体系结构——CDR 三通道、全局仪表盘、Voice/Groups/Quality 视图
  type: structure
  source_pages: p317-328
  source_chapter: ANALYTICS
  source_quote: |
    "They are generated (.csv) for all calls going through the Cloud PBX • Incoming, outgoing and internal
    calls are taken into account • Pure VoIP Rainbow audio/video call doesn't generate CDR ... Three ways
    for the partner to obtain these files • ALE pushes monthly mails with attached files • The BP retrieve
    manually the files using his account through Rainbow web interface • The BP retrieve automatically the
    files using REST APIs" (p318)
    "GLOBAL DASHBOARD ... Users (active, sleeping, inactive), adoption score, licenses • 1 to 1
    communications ... • Group communications (Bubbles & conferences) • Telephone calls ... • VoIP call
    quality (MOS index) ... • Terminals used" (p319)
  summary: |
    分析三视角：①CDR——月度 .csv 话单（入/出/内部呼叫，纯 VoIP 呼叫不产生），BP 经月度邮件/网页手工/
    REST API 三通道获取，用于计费（ALE 不计费不开票）；②仪表盘——全局（用户活跃/采纳分/许可、1对1、群组、
    电话、MOS、终端类型，近 7/30 天，可导 CSV）、Voice 页（呼入/呼出/内部 × 目的地 用户/组/欢迎/AA，周期
    最长 1 年；通话历史全过滤；欢迎服务统计最多 5 个；IVR 统计含取消呼叫与停留时长）、Groups 页（来话/接听/
    等待/时长四类×4 图，成员级统计可被公司管理员关闭；最多 5 组同屏；Hub 组报表集中 Reports 页签）、质量
    页（MOS 票据默认采集+技术明细）。③组报表中心化（p327）。
  conditions: 成员级统计关闭后服务器仍采集但组管理员无权查看（p325）
  tags: [structure, analytics, cdr, dashboard, mos]

- id: f32
  title: 维护支持体系八件套——日志/设备监督/连通性/上报/状态页/SR
  type: structure
  source_pages: p330-343
  source_chapter: MAINTENANCE
  source_quote: |
    "Click on your avatar in the top left-hand corner of your Rainbow application, then on About Rainbow
    and click on Save logs. A .zip file is created, send it to your support" (p332)
    "Your users can report problems they encounter directly in their Rainbow interface ('Help and
    Support' menu, 'Report a problem'). ... The integrator partner has the same reports as the customer,
    so he can help with end user support." (p337)
    "status.openrainbow.com ... The button « Get updates » allows, if you wish, you can subscribe to
    alerts by different methods." (p338)
  summary: |
    运维闭环八抓手：①Help Desk 指南（help.openrainbow.com，排障/找日志/报障入口）；②用户日志（头像 →
    About Rainbow → Save logs 出 .zip）；③设备监督（BP 管理端 Communication/Devices：连接状态、IP、端口、
    版本、开 debug、重启、恢复出厂）；④连通性核查（SIP 话机部署问题先查路由器协议支持；ALE SIP 终端不支
    持经 HTTP 代理穿越，p334）；⑤话机日志（管理端开 debug 会话 ≤15 分钟，admin+一次性 TOTP 口令登设备
    web 页取日志/tcpdump/复位）；⑥用户问题上报（Help and Support/Report a problem，集成商与客户同视角）；
    ⑦云状态页 status.openrainbow.com（Get updates 订阅，按主题/地域过滤，法国勾 WW/EMEA/DE）+ 计划维护
    公告（按地域与 Hybrid/Hub 架构过滤，多为晚间周末）；⑧SR（邮件/Emily BOT/Global Welcome Center/电话；
    仅认证 Rainbow Hub 伙伴建 ESR；MyPortal 两页表单）。
  conditions: ESR 前提=伙伴持 Rainbow Hub 认证（p341）
  tags: [structure, maintenance, logs, status-page, sr]

- id: f33
  title: 培训实验环境结构——POD 体系、公网模拟与账号号码规划
  type: structure
  source_pages: p12-34
  source_chapter: TRAINING LAB ENVIRONMENT
  source_quote: |
    "Each trainee uses his own PC • A POD number is assigned to each trainee ... Up to 6 trainees (8
    exceptional cases) ... Cloud PBX Rainbow Hub ... A SIP carrier simulator* • 2 preconfigured MicroSIP
    softphones" (p13)
    "POD1 bp1.rv1@ale-training.com ... Client-P1 0298296710 to 0298296719 ... Use ONLY 4 Voice Entreprise
    MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID !!!" (p17)
    "PC trainee ... Host name: Client1 • IP Address: 192.168.1.10 ... Gateway: 192.168.1.254 • DNS
    Server 1: 192.168.1.250" (p34)
  summary: |
    实验环境三层：①学员自有 PC 装 2 个预配 MicroSIP（"Start public users.bat"启动、按 POD 选账号）扮公网
    用户，训练结束须删除；②每 POD 一家公司——BP 账号 bpX.rv1@ale-training.com 建公司 Client-PX（可见性
    Closed、时区 Europe/Paris），4 名成员 alice/bob/carol/dave X（内线 101-104，公网号 02982967X1-X4，
    alice 任客户管理员），公网号段 02982967X0-X9（X=POD 号）；③RLAB 远程实验室（可选项）：Windows 11
    客户端虚机（Client1，192.168.1.10/24，实验口径），网关 192.168.1.254、内部 DNS 192.168.1.250、NAS
    12.0.0.2。MicroSIP 公网号按 POD 规则：本地 332982900P1、国内 331409500P1、移动 336050400P1、国际
    442056700P1（p22）。模拟器限制：不能按公网号呼本公司成员（p13/p20 脚注）。
  conditions: 全部为实验口径；RLAB 仅在学员 PC 无法跑 MicroSIP 时使用（p25）
  tags: [structure, lab, pod, microsip, rlab]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-24）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 网络前提核查 + Pilot 评估 | 有 | f01（章节位） | 文档体系与工具用途属概念/数值类（见 principle/glossary），端口表结构在 n 系与 p 系 |
| task-02 | 公司体系创建 | 有 | f04（步骤1）, f33 | 七步主流程第 1 步 + 实验环境公司规划 |
| task-03 | 管理员权责、目录/频道 | 有 | f04（背景） | 权责矩阵为规则类（p 系）；目录/频道两步法在 principle.md p15/p16 详述 |
| task-04 | 订阅开通与分配 | 有 | f04（步骤2）, f02 | 七步第 2 步 + 两条产品线订阅命名差异 |
| task-05 | Cloud PBX 声明与配置 | 有 | f04, f05, f06 | 七步第 3 步 + 四步创建流 + 能力分区 |
| task-06 | 公网号码分配与主叫策略 | 有 | f04（步骤4） | 七步第 4 步；策略细节在 principle.md p26 |
| task-07 | 流量控制与闭锁 | 有（弱） | f06 | 框架层仅能力清单；参数细节在 principle.md p27 |
| task-08 | SIP trunk 商务与带宽 | 有（弱） | f03, f06 | 全景图 SIP carriers 区块 + trunk 归属；bundled/separated 细节在 principle.md p28 |
| task-09 | 多站点规划 | 有 | f30 | 站点模型全景 + 不变量清单 |
| task-10 | 成员管理 | 有 | f14, f15, f16, f17 | 五通道、七分区、例行程序、按键组 |
| task-11 | 设备部署 | 有 | f08, f10, f07 | 谱系 + zero-touch 全链路 + 终端三形态 |
| task-12 | 设备维护与日志 | 有 | f32 | 八件套中的设备监督/话机日志抓手 |
| task-13 | Generic SIP 接入 | 有 | f09, f11 | 接入原则三阶段 + 手工/批量配置流 |
| task-14 | DECT 部署 | 有 | f12, f13 | 两档方案结构 + zero-touch 管理流程 |
| task-15 | Hunt Group 与队列 | 有 | f18, f19, f20, f21, f22 | 组分类、分发模式、队列机制、角色矩阵、bubble 联动 |
| task-16 | Manager/Assistant | 有 | f18, f23 | 组分类 + 结构与筛选边界 |
| task-17 | 话务台与监督组 | 有 | f24 | 订阅分级、5/30 规格、话务台约束 |
| task-18 | 紧急号码与紧急组 | 有 | f25 | 三段链路（号码/组/定位） |
| task-19 | 录音与归档 | 有 | f26 | 触发面、2 个月、Exporter |
| task-20 | 欢迎服务全家桶 | 有 | f27, f28 | 四件套关系 + 开/闭路由与强制开关 |
| task-21 | IVR 配置 | 有 | f27, f29 | 四件套中的 IVR + 结构与两种入口 |
| task-22 | 多站点配置 | 有 | f30 | 站点模型与实施四步 |
| task-23 | 分析体系 | 有 | f31 | CDR/仪表盘/质量三视角结构 |
| task-24 | 维护支持体系 | 有 | f32 | 八件套结构 |

补充说明：
- f01（课程推进）、f02/f03（产品线与全景）、f33（实验环境）不直接对应单一 task，属全书主线与 BOOK_OVERVIEW 骨架 1-3 的框架底座；f04 七步主流程是 24 项任务的组织轴。
- 全部 24 项 task 均有框架类条目覆盖；task-07/08 在框架层仅能力锚点，参数与商务细节由 principle.md 承接（已注明）。
- 生产化边界提示（来自 BOOK_OVERVIEW 批判节）：网络端口/带宽指向 Network Requirements 文章；SIP trunk 商务与号码携转指向 BP/运营商；DID 紧急定位登记指向 SIP 运营商数据库；CDR 细节指向 TBE099。
