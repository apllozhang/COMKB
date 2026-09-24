# 术语/缩写/产品名候选 — OpenTouch Suite for MLE (OPENXTE300EN Ed10, R2.6.1)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 56 条（六类：concept 22 / role 4 / subscription 6 / product 12 / protocol 8 / resource 4，另含若干并入条目）。ALUID 外的缩写凡书中未给全称者，full_name 字段如实省略，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: OTMS (OpenTouch Multimedia Services)
  full_name: OpenTouch Multimedia Services（p115 横幅完整拼写）
  category: concept
  source_pages: p5, p115
  source_quote: |
    "OpenTouch™ Multimedia Services (OTMS) is dedicated to large market ... OTMS 5000 users max" (p5)
    "Product : OpenTouch™ Multimedia Services 2.6.1 Version : 18.0.100.003" (p115)
  definition: |
    本书的宿主产品：面向大市场的 OpenTouch 服务器套件，OTMS（物理一体机）与 OTMS-v/OT-v（虚拟化）两种
    形态，均上限 5000 用户。SSD 横幅口径为 2.6.1 / 18.0.100.003。
  alias_or_related: OTMS-v / OT-v（见 g02）；软件包 OS 为 SLES 12 SP5（p9）
  tags: [concept, otms, core]

- id: g02
  term: OTMS-v / OT-v
  category: concept
  source_pages: p8-9, p535, p555
  source_quote: |
    "OTMS-v ... Vmware ESXi ... OTMS VM ... OTMS-V up to 5000 users" (p8-9)
    "OT-V Backup of virtual machines: OpenTouch, OXE and OmniVista 8770 thanks to vSphere" (p535)
  definition: |
    OTMS 的虚拟化交付形态：ESXi/Hyper-V 上以一组虚机（OTMS VM、OXE VM、8770 VM、OMS VM、DCS VM、OTFC
    VM）承载；与物理 OTMS 同为 5000 用户。差异点：许可锚加密狗（非 ALUID）、备份要 NFS、无本地
    /var/backup。书内 OTMS-v 与 OT-v 混用同义。
  alias_or_related: 虚机清单见 framework f03；许可差异见 g17
  tags: [concept, virtualization]

- id: g03
  term: ICAS / ICM / AMS
  category: concept
  source_pages: p6-7, p541
  source_quote: |
    "Media Server characteristics (AMS) ● An audio video mixer (MCU) ... Voice Codec: G711 / G729 /G722
    Video Codec: H264" (p7)
    "Multi-media SIP Core functions (SIP server) ● SIP based communication server for SIP endpoints" (p7)
    "OpenTouch server databases backup of different components: ICAS (databases and voice messages)
    SIP SRV(databases) ACS (databases)" (p541)
  definition: |
    OT 服务器内三组件：AMS=媒体服务器（MCU、3-N 方会议、混音、放音、G711/G729/G722/H264）；ICM=多媒体
    SIP 核心（SIP server，即 ESS 接入 5260）；ICAS=即时通信与协作服务。备份章口径 ICAS 含数据库与语音
    消息。
  alias_or_related: AMS 的 SIP 服务器别名 Mule（g31）；ESS 见 g30
  tags: [concept, architecture]

- id: g04
  term: ACS / Stack
  category: concept
  source_pages: p7, p97, p541
  source_quote: |
    "The stack is the association of 2 (or more) ACS servers. Stack allows to have ACS backup and/or
    increase the accesses." (p97)
  definition: |
    ACS（Advanced Communication Server，向导 1.5 节填 Stack name 与 Node ID）：协作/应用服务器组件；
    stack=2 台以上 ACS 的组合，提供备份与扩接入。备份体系里 ACS 独立成库。
  alias_or_related: 改 OT/ACS 名会使既有会议全部重建（TC2149 2.8）
  tags: [concept, acs, stack]

- id: g05
  term: SOT (Software Orchestration Tool)
  full_name: Software Orchestration Tool（p53 完整拼写）
  category: concept
  source_pages: p46, p53-65
  source_quote: |
    "S.O.T. stands for « Software Orchestration Tool »; it is a solution to deploy ALE products
    (physical or virtualized)" (p53)
    "Concept based on a "enhanced PC-installer" tool running on a virtual machine" (p46)
  definition: |
    ALE 产品的自动化部署工具：以 ISO（内含 .ova）交付的虚机，自动挂载全部 ISO、含 hotfix 静默安装、
    PXE 启动目标机；standalone/hosted 两模式、default/Template Factory 两配置、easy/expert 两工作模式。
    一次只部署一台。
  alias_or_related: 补丁 sot-update zip 自 SOT 3.0；规格见 Delivery note
  tags: [concept, sot, deployment]

- id: g06
  term: Post-installation wizard
  category: concept
  source_pages: p48-50, p88-89
  source_quote: |
    "The OpenTouch server post installation (also called site installation) after software installation
    ... automatically started at first boot" (p48)
    "The post-installation proposes two modes: Installation from scratch or From an existing archive" (p89)
  definition: |
    OT 服务器软件装完首次开机自动启动的站点安装向导（=site installation），两模式：from scratch 十节配置
    或 restore from archive 备份恢复；完成后启动 OT 服务。
  alias_or_related: rehosting 复用同一向导（p563）
  tags: [concept, post-installation]

- id: g07
  term: ALUID
  category: concept
  source_pages: p131, p162
  source_quote: |
    "The ALUID is a unique 128 bits identifier based on hardware characteristics of the server. It can
    be retrieved by a tool, a command launched on the server: getaluid" (p131)
    "IN OPENTOUCH,ALUID IS THE ELEMENT USED IN CASE OF PHYSICAL SERVER DEPLOYMENT (OTMS, OTMC) TO
    CONTROL THE LICENSE." (p162)
  definition: |
    唯一 128 位硬件标识（getaluid 命令读取）：物理服务器（OTMS/OTMC）部署时 .ice 许可的锚定物；
    虚拟化部署不使用 ALUID，一律换加密狗。
  alias_or_related: final 许可文件名含 ALUID_xxx（p148）；对照 g17 加密狗
  tags: [concept, licensing]

- id: g08
  term: FlexLM
  category: concept
  source_pages: p131, p158-159, p162
  source_quote: |
    "The license mechanism is flex-lm based Whatever the OpenTouch, virtualized or not, the Flex-lm
    server can be local (on OpenTouch server) or external" (p131)
    "FlexLM Licensing Enabled Yes ... Flex Server Port 27000" (p158)
  definition: |
    Flex-lm 许可服务机制：服务可内嵌 OT 服务器或跑在外部独立虚机（端口 27000）；OXE 侧只用于校验
    Product ID（Use Flex License=No，容量仍看本地 .swk）；ALCFIRM 为其 vendor daemon。
  alias_or_related: lmutil 工具族（p162-164）；checkLicensing.sh（p178）
  tags: [concept, licensing, flexlm]

- id: g09
  term: Connection user (ACU)
  category: concept
  source_pages: p258, p264, p271
  source_quote: |
    "User has one or more OXE devices - Can have access to OpenTouch applications - Can have a voice
    mail box" (p258)
    "OpenTouch Connection ... ACU: Advanced Communication User" (p264, p271)
  definition: |
    挂 OXE 设备且被授予 OT 应用权的用户类型（User type=OXE + Applications=OT），即 Advanced
    Communication User；由三档案合成：OXE profile + OT profile（Category=ACU-OXE）+ 语音邮箱档案。
  alias_or_related: 对照 Directory user（g10）；OTC PC One 免费模式仍属 Connection user 画像
  tags: [concept, users]

- id: g10
  term: Directory user
  category: concept
  source_pages: p258, p267
  source_quote: |
    "This is a directory user - Without any node properties (no device and no applications) - Located
    in the 8770 Company directory for directory consultation only" (p258)
  definition: |
    User type=None 的纯目录用户：无设备无应用，仅进 8770 公司目录供查询。
  alias_or_related: 对照 g09 Connection user
  tags: [concept, users]

- id: g11
  term: OXE profile / OT profile / Voice mail profile（三档案）
  category: concept
  source_pages: p264-266, p274, p277
  source_quote: |
    "OXE profiles are: Optional for Connection Users creation ... Created thanks to OmniPCX Enterprise
    configuration tool It's a user with the "Set function" parameter set to "Profile"" (p265)
    "OT profiles are: Required to create Connection Users with OT rights ... Category Select: ACU-OXE" (p266, p277)
  definition: |
    建 Connection 用户的档案三件套：OXE profile（Set function=Profile 的特殊用户，A0000 式占号，定
    Entity/COS/VM 号）；OT profile（Users and devices/User/Profile，Category=ACU-OXE，Licenses 页勾
    Desktop/Voice mail/Conferencing 等权）；语音邮箱档案（Advanced/Classic/Simplified，g20）。
    OXE 档案实时同步 8770，OT 档案需手动完整同步。
  alias_or_related: Users 应用只能改档案（g12）
  tags: [concept, profiles]

- id: g12
  term: Users application（Users/Directory/Configuration/Alarms 四应用）
  category: concept
  source_pages: p256-261, p278
  source_quote: |
    "Unified interface whatever user's location ... Import/export user data (mass provisioning)
    Associate device to user" (p257)
    "Only profile modification is allowed via Users application." (p278)
  definition: |
    OmniVista 8770 的用户供给主界面：Users 页签（目录树+用户符号）、Profiles 页签、属性区；目录树只能在
    Directory 应用配置；权限边界=Users 应用只能改档案，建/删必须回 OXE/OT 配置工具。
  alias_or_related: nmc=Configuration 应用（p189）
  tags: [concept, omivista, users]

- id: g13
  term: bics.conf
  category: concept
  source_pages: p194, p545
  source_quote: |
    "OpenTouch information can be found in the file bics.conf on the OpenTouch server: HOST_NAME=
    "opentouch" ... ICE_USERNAME="otAdmin" ... ICE_MAINTENANCEUSERNAME="otuser"" (p194)
    "" bisc.conf" file updated according to backup storage settings" (p545)
  definition: |
    OT 服务器 /var/data/bics/bics.conf：主机名/域、OT 核心账户（otAdmin/otProfile/otuser）及口令密文的
    唯一出处；8770 声明 OT、备份存储配置（--storage）都读写它。
  alias_or_related: checkSystem.sh 校验 bics.conf 与系统一致性（p524）
  tags: [concept, config, accounts]

- id: g14
  term: UDAS
  category: concept
  source_pages: p223-224, p243
  source_quote: |
    "UDAS is a module that receives requests from phone client or software searching for contacts
    information stored on OpenTouch server" (p223)
    "all the search are made in the synchronized database (synchronized directories)" (p223)
  definition: |
    OT 侧联系人检索模块：把 OXE 话簿（OTS）、内部目录（ESS 用户）、外部 LDAP 三路数据源单向同步进
    PostgreSQL 同步库（LDAP sync/Internaldir sync/Phonebookdir 表），检索只查同步库；同步周期 ≥1 且禁 0。
  alias_or_related: 8770 作为 LDAP 源时 rehosting 改 FQDN（TC2149 3.7）
  tags: [concept, directory, udas]

- id: g15
  term: Dialing rule / DAS rule（两套规则）
  category: concept
  source_pages: p220-222, p225, p253
  source_quote: |
    "Dialing rule(s) are used to add automatically the outbound prefix when an external call (by name
    or number) is performed." (p220)
    "Note that « DAS Rules » are applied for Conference" (p221)
    "The call routing rules, called DAS rules, are applied to the user's dialed digits ... linked to a
    domain DAS rules are mandatory and are country dependant" (p253)
  definition: |
    两套独立的拨号规则：Dialing rule（OT 侧，自动加外呼前缀；按名呼打全客户端、按号呼打仅 OTC PC/Mobile）
    作用于一般外呼；DAS rule（会议服务器侧，按域配置的正则改写，强制且随国家不同）作用于 Conference 呼叫。
  alias_or_related: Phone formatting rules（g16）管号码格式识别
  tags: [concept, routing, rules]

- id: g16
  term: Phone formatting rules
  category: concept
  source_pages: p225, p254
  source_quote: |
    "Phone formatting rules To specify the format of internal numbers" (p225)
    "Extension Pattern /^\s*\+*[xX]?(\d{3,5})\s*$/ for a 5 digits length dialing plan ... also used for
    creation of the device(s) with auto-provisioning on Conference server side." (p254)
  definition: |
    会议服务器侧的号码格式化规则（Extension Pattern 正则，位数与拨号计划匹配）：用于分机拨号识别与会议
    服务器自动开通设备时的号码格式判定。
  alias_or_related: 与 g15 DAS rules 同在会议服务器管理台
  tags: [concept, formatting]

- id: g17
  term: Dongle (Aladdin USB dongle) / Dongle-ID
  category: concept
  source_pages: p98, p131, p162, p165, p173
  source_quote: |
    "For virtualized deployment, the ice license file is linked to a hardware dongle (Aladdin) plugged
    on the server Software locks are linked to this specific physical server thanks to the dongle-ID
    controlled by the flex-lm server" (p131)
    "USB DONGLE IS USED ONLY IN CASE OF VIRTUALIZATION." (p162)
  definition: |
    虚拟化许可的物理锚定物：Aladdin USB 加密狗插在承载 FlexLM 的宿主/虚机上，许可经 Dongle-ID 绑定；
    虚机要挂 USB Device（内嵌 FlexLM 先挂 USB Controller）。ID 用 lmutil lmhostid -flexid 读取。
  alias_or_related: 对照 g07 ALUID；外部虚拟化 FlexLM 只认加密狗（TC2149 2.3）
  tags: [concept, licensing, dongle]

- id: g18
  term: Local Storage voice mail (defaultVmsLS)
  category: concept
  source_pages: p304, p327, p366
  source_quote: |
    "Local storage voice mail OpenTouch integrated software voice mail system Voice messages are stored
    ... in wav format ... in an uncompressed format Readable from any IMAP client" (p304)
    "Type Check that the local storage voicemail is created by default." (p327)
  definition: |
    OT 内置软件语音邮件系统（默认实例名 defaultVmsLS，向导/出厂即建）：留言以未压缩 wav 存 OT 服务器目录、
    IMAP 可直读；wav 附件/箱满通知/My Messaging 链接/回呼等增强通知仅 LS 可用。UM（统一消息）是另一套、
    另一培训。
  alias_or_related: VMS=Topology 下的语音邮件系统对象（p240/327）；VM profile 见 g20
  tags: [concept, voice-mail]

- id: g19
  term: General announcement
  category: concept
  source_pages: p381-392
  source_quote: |
    "The general announcement allows customers to record and play a message to internal or external
    callers" (p381)
    "Only one general announcement can be recorded at a time. ... Max duration: 5 minutes" (p392)
  definition: |
    企业级通用公告：在留言/查听场景向主叫播放（播放时机由管理员多选）；授权用户可经 TUI 增强菜单 6 录/
    听/停用，或管理员放置固定名 wav（CCITT A-law 8kHz mono）。一次仅一条、覆盖式、5 分钟上限。
  alias_or_related: "arrive on AA" 选项已废弃（p394）
  tags: [concept, voice-mail, announcement]

- id: g20
  term: Voice mail profile（Advanced/Classic/Simplified/Standard）
  category: concept
  source_pages: p339-343
  source_quote: |
    "Profiles called "Advanced", "Classic" and "Simplified", dedicated to Local Storage. "Standard"
    profile is dedicated to Unified Messaging." (p339)
  definition: |
    邮箱行为模板：LS 型默认 Advanced/Classic/Simplified 三档，UM 型 Standard；四页签控制 Answer only、
    配额、保留天数、回呼、零出、TUI 口令管理、IMAP 访问等；建邮箱必须先选档案。
  alias_or_related: 建箱流程见 case c19
  tags: [concept, voice-mail, profile]

- id: g21
  term: Multi-devices（Twinset 多终端）
  category: concept
  source_pages: p438-439, p484-485
  source_quote: |
    "Up to 5 devices ... Only one remote extension Only one DECT" (p439)
    "Case 1: Primary set: NOE/ALE device Secondary device: NOE/ALE device Case 2: Primary set: NOE/ALE
    device Secondary device: OTC PC" (p484)
  definition: |
    OXE 多终端特性在 OT 语境的应用：一名 Connection 用户最多 5 台设备（主/副白名单见 principle p36），
    副站可为 NOE 话机或 OTC PC（SIP 分机）；配 Twinset get call / No ringing 前缀与 Ring all Secondary
    COS；VoIP 不冻结主话机。
  alias_or_related: 旧 Nomadic 方式仍支持但另册（p439/445）
  tags: [concept, multi-devices]

- id: g22
  term: Supervision group (OT)
  category: concept
  source_pages: p494-507
  source_quote: |
    "Each group is a set of 2 or more members of the same type (group of Conversation users or group of
    Connection users) 40 members maximum per group" (p497)
    "No link with OXE supervision feature (no management synchronization)" (p501)
  definition: |
    OT 侧监督组：同类型成员 2-40 人、角色 Supervisor/Supervised/双职；Regular/Collaboration 两工作模式；
    经 OTC PC/手机/TUI 前缀进出组；代接走 OXE Direct call pick-up（需 OXE 侧启用）；与 OXE 话机监督键
    无联动。上限 500 组、40 人/组、监督链 4000/6000。
  alias_or_related: Join or leave group 前缀（p239/511）
  tags: [concept, supervision]

- id: g23
  term: rehosting
  category: concept
  source_pages: p560-567, p579
  source_quote: |
    "The OpenTouch Re-hosting can be used if the installation was performed with temporary IP addresses
    and/or names" (p560)
    "TC 2149 for OTMS, OTMC, OXE & 8770 rehosting" (p561)
  definition: |
    用 ot-config.sh --rehost 向导改 OT 的 IP/主机名/FQDN/DNS/License server 的变更操作；风险与边界见
    counter-example n36/n37；OXE/8770/生态按 TC2149 矩阵收尾。
  alias_or_related: 隐藏选项 --suspend（换子网）；Clonezilla/TC1625 做镜像
  tags: [concept, rehosting]

- id: g24
  term: Maintenance Portal
  category: concept
  source_pages: p520-521, p526
  source_quote: |
    "The aim of the Maintenance Portal is to simplify, to the BP or any advanced OT administrator, the
    usage of maintenance commands ... Note: The Maintenance Portal also includes the AppGuard Control
    Center" (p520)
    "https://<OpenTouch server FQDN>:4448" (p521)
  definition: |
    维护命令的图形化门户（WebAdmin 进入或 :4448 直达）：识别/描述/执行维护操作，含 AppGuard Control
    Center 健康监控；normal/expert 两种显示模式；与 CLI 原始命令、otconsole.sh 菜单三通道同源。
  alias_or_related: otconsole.sh 自 R2.2（p519）
  tags: [concept, maintenance]

# ── 二、角色 (role) ──

- id: g25
  term: BP (Business Partner)
  full_name: Business Partner（p9 展开）
  category: role
  source_pages: p9, p520, p602
  source_quote: |
    "Physical server provided by Business Partner or customer" (p9)
    "The aim of the Maintenance Portal is to simplify, to the BP or any advanced OT administrator ..." (p520)
  definition: |
    ALE 业务伙伴/渠道：物理硬件由 BP 或客户提供；Maintenance Portal 的目标用户即 BP 与高级 OT 管理员；
    提交 Service Request 前置相关认证（p602）。
  alias_or_related: AAPP=第三方应用认证（p602 提及，未展开全称）
  tags: [role, partner]

- id: g26
  term: Supervisor / Supervised（监督组角色）
  category: role
  source_pages: p497, p510
  source_quote: |
    "In a supervision group, each member is associated to a role which can be: Supervisor Supervised
    Or both" (p497)
    "Is Supervisor Check if user has to monitor other member(s) Is Supervised Check if user is
    supervised" (p510)
  definition: |
    OT 监督组内成员角色：Supervisor（看全组话务状态、收通知、可代接）、Supervised（被监督，可进出组）、
    或身兼两职；建组时逐人勾选 Is Supervisor/Is Supervised。
  alias_or_related: 无专用许可（p498）；OTC PC One 无监督
  tags: [role, supervision]

- id: g27
  term: otAdmin / otProfile / otuser（OT 三账户）
  category: role
  source_pages: p95-96, p194
  source_quote: |
    "Administrator Username Enter the username used by OmniVista 8770 to connect to the OpenTouch
    server with full administration rights ... Profile Username ... with restricted rights for
    template management ... Maintenance Username" (p96)
    "ICE_USERNAME="otAdmin" ... ICE_TEMPLATEUSERNAME="otProfile" ... ICE_MAINTENANCEUSERNAME="otuser"" (p194)
  definition: |
    OT 三个系统账户的分工：otAdmin=8770 配置 OT 用（全权）；otProfile=8770 取/管模板用（受限）；
    otuser=维护/备份恢复/SSH 登录用（Linux 账号）。向导页建，bics.conf 可查，WBM 可互改前两者口令。
  alias_or_related: 用户名禁用 admin/adminnmc/htuser（p95）
  tags: [role, accounts]

- id: g28
  term: mtcl / swinst / adfexc（OXE 三账户）
  category: role
  source_pages: p111, p117, p190, p201, p547
  source_quote: |
    "OmniPCX Enterprise mtcl mtcl swinst SoftInst adfexc adfexc" (p111)
    "Use the mtcl session in order to log in PuTTY session with the login "mtcl" and the password
    "mtcl"." (p117)
    "FTP Username/FTP Password adfexc Enter adfexc password (adfexc by default). This is the OXE FTP
    login and password used for data retrieval." (p190)
    "Using a swinst session under the mtcl account" (p547)
  definition: |
    OXE 侧三个经典账户：mtcl=维护命令行（netadmin/spadmin/swinst 入口）；swinst=软件安装/备份会话账号；
    adfexc=OXE 的 FTP 账号，供 8770/OT 拉取数据（声明节点时必填）。实验口令均为同名/SoftInst（实验口径）。
  alias_or_related: 8770 侧 adminnmc（g34）
  tags: [role, accounts, oxe]

# ── 三、订阅/许可 (subscription) ──

- id: g29
  term: Desktop right（Desktop license）
  category: subscription
  source_pages: p433, p445, p448, p467
  source_quote: |
    "OTC PC: full mode for Connection users with « Desktop » right (license) OTC PC One : Freemium mode
    for for Connection users without « Desktop » right" (p433)
    "Default use: RCC (Remote Call Control) Grant users the right to access the application (if not
    set, application will work as "OTC PC One")" (p445)
    "Desktop Select the check box to allow the user to access the application from a computer" (p467)
  definition: |
    OT profile Licenses 页的 Desktop 权：决定 OTC PC 以全量模式（RCC+VoIP+协作）还是 OTC PC One 免费模式
    运行；软电话/多终端副站场景必须勾选。
  alias_or_related: 全量模式=Universal client option（g30）叠加
  tags: [subscription, licensing, otc-pc]

- id: g30
  term: Universal client option / Conferencing option / Base Ct user license
  category: subscription
  source_pages: p448, p458-459
  source_quote: |
    "Without universal client option: Desktop right unchecked Reduced level of service" (p448)
    "OTC PC One (freemium) OTC PC (full featured) Licenses ... Base Ct user license + Universal client
    option + Conferencing option ... Outlook conference add-in / Office integration / Skype integration /
    Google mail" (p458)
    "Without desktop integration Add the Universal license to the concerned user No need to re-install
    the client software package" (p459)
  definition: |
    OTC 客户端许可阶梯：Base Ct user license（基础）→ +Conferencing option（解锁 Outlook 会议插件/预约
    会议管理）→ +Universal client option（解锁 Office/Skype 集成与全量 OTC PC）；升级加许可即切换模式，
    带桌面集成时需重跑 setup 部署扩展。
  alias_or_related: Google mail C2C 各档均含（p458）
  tags: [subscription, licensing]

- id: g31
  term: Unified management license（WPC）
  category: subscription
  source_pages: p290
  source_quote: |
    "Available from OmniVista 8770 3.2.8 with Unified management license"
  definition: |
    Web Provisioning Client 的许可前提：OmniVista 8770 3.2.8 起、须持 Unified management 许可方可使用。
  alias_or_related: 浏览器仅 Chrome ≥54（p292）
  tags: [subscription, licensing, wpc]

- id: g32
  term: .ice 许可文件（<OT license>.ice / <OXE license>.ice）
  category: subscription
  source_pages: p130, p148, p154, p158
  source_quote: |
    "OpenTouch license file: <OT license>.ice ... <OXE license>.ice if OXE-v (Flexlm control)" (p130)
    "ALUID_xxx_licenses.ice FLEXID_x-xxxxxxxx_license.ice SERVERMACADDRESS_ANY_license.ice" (p148)
    "License_release Examples: 10 for OpenTouchR2.4 11 for OpenTouchR2.5" (p154)
  definition: |
    FlexLM 体系的 OT/OXE-v 许可文件：内容含锚定物（ALUID/Dongle-ID/MAC）、OTID、Product ID（FEATURE 行），
    License_release 对应版本；Flexlm 启动时复制改名为 final_licenses 下的锚定名文件；OXE 的 .ice 另入
    final_licenses/oxes。
  alias_or_related: swk/sw8770 见 g33
  tags: [subscription, licensing]

- id: g33
  term: .swk / .sw8770 / nmc.license（OXE 与 8770 许可文件）
  category: subscription
  source_pages: p130-132, p151-152, p161
  source_quote: |
    "OmniPCX Enterprise license file: software.swk ... OXE software lock file ".swk" is encrypted using
    a proprietary algorithm Validity control is done on CPUID (physical server) or using Flexlm server
    (OXE-v) or also Cloud connect" (p130-132)
    "OmniVista 8770 license file (name: nmc.license): 8770 handle verified thanks to OXE .swk file" (p151)
  definition: |
    OXE 软件锁文件 <offer ID>.swk（专有加密；物理机 CPUID/OXE-v FlexLM/Cloud Connect 三种验证，容量口径
    的真正载体）；8770 许可 .sw8770 在 OT/Flex 服务器侧改名 nmc.license，其 8770 handle 须与 OXE .swk 内
    Handle 4760 对应（spadmin 选 2 读取）。
  alias_or_related: 8770 handle 亦可经 8770 客户端 Help/About 查看（p161）
  tags: [subscription, licensing]

- id: g34
  term: alchostid.cfg / OTID
  category: subscription
  source_pages: p136-145, p153
  source_quote: |
    "alchostid.cfg OTID" (p142-143 多处虚机图)
    "OpenTouch license files: alchostid.cfg <OT license>.ice OTID ... Dongle ID" (p153)
  definition: |
    OT-v/外部 FlexLM 场景的 OT 节流文件：记录 OTID（OT 实例 ID），与 .ice 内 OTID 对应；Flexlm 服务启动时
    生成于 $LICENSES_HOME。许可核查时要抄录 OTID/Dongle ID/OXE product ID 三要素。
  alias_or_related: OTEC 双 OT 各有 OT1/OT2 ID（p142）
  tags: [subscription, licensing]

# ── 四、产品/组件 (product) ──

- id: g35
  term: OXE (OmniPCX Enterprise) / OXE VM / OXE-v
  full_name: OmniPCX Enterprise（p6 完整拼写）
  category: product
  source_pages: p5-6, p51, p130, p186-192
  source_quote: |
    "OmniPCX Enterprise ... OXE call handling" (p5-6)
    "OXE installation or upgrade Release installation (S.O.T. can be used) License installation" (p51)
    "software.swk <OXE license>.ice if OXE-v (Flexlm control)" (p130)
  definition: |
    ALE 呼叫服务器（本套件的传统 PBX 侧）：物理或虚机形态（OXE VM；OXE-v 指虚机形态，许可可由 FlexLM 或
    Cloud Connect 控制）；在 8770 中声明（netadmin/mgr 前置+建树+同步）、SIP 打通 OT（trunk 10/外部网关
    10/11）。
  alias_or_related: csa/csm 双地址口径（p187）；spatial redundancy 见 TC1652
  tags: [product, pbx]

- id: g36
  term: OmniVista 8770 (8770 Server / nms)
  category: product
  source_pages: p5-6, p186-212, p289-301
  source_quote: |
    "OmniVista 8770 Server (OS Windows)" (p6)
    "Start "Configuration" application. nmc" (p189)
    "Web Provisioning Client ... Available from OmniVista 8770 3.2.8" (p290)
  definition: |
    套件的管理服务器（Windows OS，实验主机名 nms/192.168.1.70）：承载 Configuration（nmc）、Users、
    Directory、Alarms、Maintenance 等应用与 Web Provisioning Client；OXE 与 OT 节点都在此声明互挂；告警
    经 SNMP v3 汇聚于此。
  alias_or_related: 许可 .sw8770→nmc.license（g33）；DM 角色见 g40
  tags: [product, management]

- id: g37
  term: OMS
  category: concept
  source_pages: p8, p14, p33, p584
  source_quote: |
    "Racks are created in the OXE database. Here we need only the OMS." (p33)
    "Software Rack 3U (OMS) o Rack N° 4 o Virtual GD4 (slot 0) IP @: 192.168.1.13/24" (p33, 实验口径)
    "OMS / MGD / Int IP: Update OMS / Media Gateway / INT IP settings according new OXE IP configuration." (p584)
  definition: |
    OXE 的媒体网关子系统（书中未展开全称）：实验中以 Software Rack 3U 形式存在（Rack 4，Virtual GD4 挂
    192.168.1.13）；OXE 改址时 OMS/MGD 的内部 IP 也要同步改（TC2149 1.9）。
  alias_or_related: GD4=网关板卡形态（g38）
  tags: [product, oxe, media-gateway]

- id: g38
  term: GD4 / MIX484
  category: product
  source_pages: p22, p24, p33, p35
  source_quote: |
    "Virtual GD4 (slot 0) IP @: 192.168.1.13/24 ... Virtual GD4 MAC @: 00:50:56:01:01:13" (p33)
    "CLASSROOM EQUIPMENT ... GD4 192.168.1.12 ... admin root letacla1 mg4.ale" (p24, 实验口径)
    "Classroom MIX484 GD4 ALE-300 ALE-30h POE Switch" (p22)
  definition: |
    ALE 网关板卡/设备名：虚拟化形态 Virtual GD4（OMS 机架 slot 0）；混合教室用物理 GD4（192.168.1.12）与
    MIX484 机架、ALE-300/500/20h/30h 话机、POE Switch 组成教学端。书中未展开全称。
  alias_or_related: 808x 话机（CTL 重签用）另见 p427
  tags: [product, hardware, gateway]

- id: g39
  term: OTC PC / OTC PC One / OTC for MAC
  category: product
  source_pages: p432-459, p460-483
  source_quote: |
    "Alcatel-Lucent OpenTouch™ Conversation for PC Multimedia Softphone for visual interactive
    communications" (p432)
    "Same binary package as OTC PC / OTC Mac OTC PC starts in a "freemium mode"" (p448)
  definition: |
    OT 的 PC 软客户端家族：OTC PC（全量：RCC+VoIP+IM/共享/会议）、OTC PC One（同二进制的免费模式）、
    OTC for MAC（专用版；无桌面共享/桌面集成/VDI）。安装包自 OT 服务器 URL 分发，许可决定形态。
  alias_or_related: OTC Mobile=iPhone/Android（p305/438，本书不展开）；VDI 支持（p432/451）
  tags: [product, client]

- id: g40
  term: DM (Device Management server)
  category: product
  source_pages: p473, p489
  source_quote: |
    "The DM is in charge to provide to these SIP devices their SIP settings. Configuration files are
    created on OpenTouch server, in the folder: "/var/data/oamp/cms/DevicesDeployment/MYICPCSIP"" (p473)
    "Verify that OmniVista 8770 server is declared as the DM in the OpenTouch database ... /Eco system /
    IT server / Right click ... "Device management server" ... Port Keep default one (8080)" (p489)
  definition: |
    设备管理服务器：为 SIP 软设备（OTC PC 等）生成并下发 SIP 配置文件；实验中由 OmniVista 8770 充当
    （OT 侧 Eco system/IT server 建 DM 对象，端口 8080），文件生成于 8770 临时目录后推送 OT 的
    MYICPCSIP 目录。
  alias_or_related: 文件名=<分机>@<OT FQDN>（p473）
  tags: [product, provisioning, dm]

- id: g41
  term: OT SBC / Reverse Proxy（OTSBC / RP）
  category: product
  source_pages: p408-410, p444, p587
  source_quote: |
    "SBC (OT SBC) SIPS/TLS, SRTP supported using a SBC on the server side for external access only
    Reverse Proxy (integrated to OTSBC or not) Web services over HTTPS Consequence: VPN not required" (p444)
    "SBC installation: TC2257 or TC2639 depending on OT version and RP configuration" (p601)
  definition: |
    远程接入两件套：OT SBC（会话边界控制器，外部媒体的 SIPS/TLS+SRTP）与反向代理（Web 服务 HTTPS，可集成
    在 OTSBC 内）；证书可用泛域名一张撒三处或每服务器各签；细节在 TC2257/TC2639。
  alias_or_related: 端口 443/8016（p444 图；正文笔误 413，见 n41）
  tags: [product, security, sbc]

- id: g42
  term: Mule / ESS
  category: product
  source_pages: p215, p218, p232-233, p584
  source_quote: |
    "External gateway 2 To Mule (Media Server) Port 5040 ... External gateway 1 To ESS (SIP Server)
    port 5260" (p215)
    "The SIP server of the Media Server (called "mule") has to be declared as an external SIP gateway." (p232)
    "Enterprise SIP Server (ESS) is compatible with the following algorithms: G711, G722, G722.2, G729" (p218)
  definition: |
    OT 两个 SIP 服务器的别名：ESS（Enterprise SIP Server，即 ICM 的 SIP 核心）——用户/呼叫接入，端口 5260，
    不支持 G723；Mule（AMS 的 SIP 服务器）——语音邮件/AA 媒体接入，端口 5040，OXE 侧对应外部网关 11。
  alias_or_related: SIP proxy 用户 31700/31710（p252）
  tags: [product, sip, alias]

- id: g43
  term: IPDSP / MicroSIP / REX
  category: product
  source_pages: p16, p34, p112-113, p438-439
  source_quote: |
    "An IPDSP to be installed, it will be the main softphone to use directory number: 104."（RLAB 同族口径，
    本书 p34："Install and bring into service the IPDSP softphones ... 31000 Brad Barkley IP DSP"）
    "2 MicroSIP softphones are installed to simulate public numbers." (p17/25)
    "Only one remote extension" (p439)
  definition: |
    实验与多终端中的软话机/资源名：IPDSP（IP Desktop Softphone，ALE 软话机，实验主用 31000/31001，TFTP 指
    OXE 主 IP）；MicroSIP（第三方 SIP 软话机，PC Client 10 预装 2 个模拟公网号码）；REX=远端分机资源
    （多终端副站类型之一、每用户限 1，未展开全称）。
  alias_or_related: SIP(SEPLOS)/DSU/MIPT 等设备类型名（p439，未展开）
  tags: [product, softphone, lab]

- id: g44
  term: ITSP1 (SIP Carrier Simulator)
  category: product
  source_pages: p26-30
  source_quote: |
    "SIP Simulator overview - ITSP1 with one SIP Gateway ITSP1 SIP Gateway 1 gateway1.itsp1.com
    10.20.30.51" (p27)
    "Id: pbxP password: alcatel" (p27)
  definition: |
    培训专用 SIP 运营商模拟器（RLAB 公共区）：SIP 网关 gateway1.itsp1.com（账号 pbxP/alcatel）+公网网关
    public.itsp1.com（Public/Urgence 两用户由 MicroSIP 扮演）；号码规则含 POD 号 PN。纯教学基础设施。
  alias_or_related: ITSP2 仅拓扑图出现（p27）；OXE 侧注册参数见 case c01
  tags: [product, lab, sip]

- id: g45
  term: Clonezilla
  category: product
  source_pages: p564, p575, p585
  source_quote: |
    "Server disk image (Clonezilla, …): ... Clonezilla is a possibile example for OpenTouch operating on
    physical server Refer to TC1625 for more detail" (p564)
  definition: |
    开源磁盘镜像工具，教材推荐的物理 OT 服务器 rehosting 前整盘镜像手段（细节见 TC1625）；虚拟化改用
    VMware 快照/克隆/备份。
  alias_or_related: TC1625（g50）；"possibile" 为原文笔误
  tags: [product, backup]

- id: g46
  term: AppGuard Control Center
  category: product
  source_pages: p520
  source_quote: |
    "The Maintenance Portal also includes the AppGuard Control Center allowing to make easier the
    system health monitoring on OT"
  definition: |
    Maintenance Portal 内置的系统健康监控组件（书中仅此一处提及，未展开）。
  alias_or_related: 无
  tags: [product, monitoring]

# ── 五、协议/技术 (protocol) ──

- id: g47
  term: SIP / SIP Trunk / SIP External Gateway
  category: protocol
  source_pages: p226-234
  source_quote: |
    "Trunk Group Type Select "T2" type ... T2 Specification Select SIP" (p227)
    "SIP/ External Gateways Creation ... Gateway type ICE type" (p231)
  definition: |
    OT-OXE 间的话音承载协议栈：OXE 侧 T2 型 SIP trunk group（Q931 ABC-F）、本地 SIP 网关（5060）、两条
    外部网关（10→ESS 5260 / 11→Mule 5040）、trusted addresses、ICE type 网关与 CSTA User-to-User。
  alias_or_related: 100 REL、SDP in 18x、Supervision timer 380 等字段（p231-232）
  tags: [protocol, sip]

- id: g48
  term: CSTA / DPNSS
  category: protocol
  source_pages: p231, p233-234
  source_quote: |
    "Support CSTA User-to-User Yes" (p231)
    "This prefix is used to optimize the transfers through trunk groups. ... Translator Prefix plan ...
    Local Features Pabx address in DPNSS ... Routing Optimisation Yes" (p233-234)
  definition: |
    两个未展开全称的协议名：CSTA（OT-OXE 间 User-to-User 信令支持，外部网关字段）；DPNSS（OXE 前缀计划里
    的 Pabx 地址口径，配合 Routing Optimisation=Yes 优化中继转接）。
  alias_or_related: 无
  tags: [protocol]

- id: g49
  term: IMAP4 / SMTP / VPIM
  category: protocol
  source_pages: p304-306, p313, p351, p360, p363, p370-371
  source_quote: |
    "Using an IMAP mailbox Voice messages presented to the user in a dedicated inbox" (p306)
    "IMAP 4 TLS IMAP 4 on SSL" (p313)
    "There is no SMTP server in the OpenTouch solution." (p360)
    "Notifications are handled by "Scorpio" component. To declare the SMTP server for notification to
    this component, a route has to be declared in VPIM sesssion" (p370-371)
  definition: |
    邮件三协议在 OT 语境的角色：IMAP4（收语音留言，TLS/SSL，前端服务 imap4fed）；SMTP（通知外发，OT 无内
    置、外部服务器无认证无 TLS）；VPIM（OT 内的消息路由会话——通知的 SMTP 路由也经 VPIM 声明；VPIM 全称
    Voice Profile for Internet Mail 见 p319 附近口径为语音邮件联网协议）。
  alias_or_related: "sesseion" 为原文笔误（p371）
  tags: [protocol, mail]

- id: g50
  term: SNMP v3（Inform/Trap、SHA/AES128）
  category: protocol
  source_pages: p205-209
  source_quote: |
    "SNMP version SNMP v.3 ... Notification type Inform" (p207)
    "SNMP authentication protocol SHA SNMP encryption protocol AES 128 SNMP security level V3
    authentication: privacy" (p208)
  definition: |
    OT→8770 告警协议口径：v3 用户认证 SHA、加密 AES 128、安全级 auth-privacy、通知类型 Inform（server 端
    口 162、agent 端口 161）、trap 过滤三档；8770 侧落盘 snmptrapd.conf。
  alias_or_related: MIB=ICEAlarmMgnt.mib（p208）
  tags: [protocol, snmp, alarms]

- id: g51
  term: PKCS7 / PKCS12 / CSR / CTL
  category: protocol
  source_pages: p404-407, p414, p417, p422, p427
  source_quote: |
    "OpenTouch server certificate import using WebAdmin: PKCS7: certificate (CSR was done on OT server)
    PKCS12 (protected by passphrase): certificate and private key (generated on CA)" (p404)
    "Certificate Signing Request using WebAdmin interface (this action will also generate private-public
    keys pair)" (p405)
    "Don't forget to sign the new CTL, by using a 808x device" (p427)
  definition: |
    证书技术四件套：CSR（证书签发请求，WebAdmin 生成时同时产生密钥对）；PKCS7（CSR 在 OT 侧做时的导入
    格式）；PKCS12（密钥对在 CA 侧生成时的带口令导入格式）；CTL（证书信任表，换自签证书后须用 808x 话机
    重签）。
  alias_or_related: Windows CA 流程见 case c24
  tags: [protocol, certificates, pki]

- id: g52
  term: PXE boot / OVF / OVA / vmdk
  category: protocol
  source_pages: p47, p57, p79-80, p141-145
  source_quote: |
    "Target machine to be booted on the network (PXE boot)" (p47)
    "The following procedure is given for an ovf (and vmdk) file importation. The principle is exactly
    the same for an ova file which is in fact a package containing the ovf and its associated vmdk
    files." (p80)
  definition: |
    虚拟化交付四术语：PXE（SOT 网络启动目标机的机制）；OVF/OVA/vmdk（虚机描述/打包/磁盘格式，SOT 可生成
    OVF，手动导入流程见 case c03）。书内未展开协议细节。
  alias_or_related: SOT ISO 内含 .ova（p54）
  tags: [protocol, virtualization]

- id: g53
  term: Kerberos / LDAP / RADIUS / TFTP
  category: protocol
  source_pages: p34, p325, p434, p583, p591
  source_quote: |
    "Single Sign On (SSO) via Kerberos" (p434)
    "External authentication (Radius, LDAP/LDAPS, Single Sign On)" (p325)
    "Don't forget to specify the TFTP server IP @ in the IP DSP settings." (p34)
    "Kerberos SSO is linked to OT FQDN in Active Directory and requires update in case OT of modification" (p591)
  definition: |
    认证与引导协议群：Kerberos（OTC PC 的 SSO；rehosting 改 OT FQDN 时 AD 里的 SPN 要同步改）；LDAP/LDAPS
    与 RADIUS（语音邮件 Web 与 OTC 客户端的外部认证）；TFTP（IPDSP 取配置）。书内均为用法级提及，未展开。
  alias_or_related: UDAS 的外部 LDAP 目录（g14）
  tags: [protocol, auth]

- id: g54
  term: G711 / G722 / G723 / G729 / H264（编解码族）
  category: protocol
  source_pages: p7, p201, p218, p233, p313
  source_quote: |
    "Voice Codec: G711 / G729 /G722 Video Codec: H264" (p7)
    "OXE call server is compatible with the following algorithms: G711, G723, G729 Enterprise SIP Server
    (ESS) ... G711, G722, G722.2, G729 Not compatible with G723" (p218)
  definition: |
    音视频编解码口径：AMS 媒体面 G711/G729/G722+H264；OXE 呼叫服务器 G711/G723/G729；ESS 不支持 G723；
    OT-OXE 互联 codec 两端一致（实验 G729）；IMAP 留言 G711。
  alias_or_related: Multi. Algorithms=False（p233）
  tags: [protocol, codec]

# ── 六、网站与资源 (resource) ──

- id: g55
  term: BPWS / My Portal / TDL / eBusiness Portal
  category: resource
  source_pages: p42, p44, p168, p601
  source_quote: |
    "Download all software ISO files from the BPWS" (p42, p44)
    "Flexlm VM, ovf file is available on My Portal website." (p168)
    "OTMS 2.x Installation Manual: search for 8AL90512US* on ALE eBusiness Portal or browse TDL" (p601)
  definition: |
    ALE 交付资源入口群：BPWS（软件 ISO 下载门户）；My Portal（FlexLM 虚机 OVF 等）；ALE eBusiness Portal 与
    TDL（技术文档库，按 8AL90512US*/8AL90120US* 等编号检索安装手册）。四个名称书内并列使用、关系未展开。
  alias_or_related: Knowledge Hub（p2，eBook 平台）；enterprise-education.csod.com（p603，课程目录）
  tags: [resource, portal]

- id: g56
  term: TC2149 / TC1652 / TC2257 / TC2639 / TC1625（TC 文档族）
  category: resource
  source_pages: p231, p242, p561, p564, p579-602, p601
  source_quote: |
    "Technical Bulletin OpenTouch TC2149 ed.04 Release 2.3.1 and above OpenTouch : OTMS, OTMC, OXE, 8770
    Rehosting procedure" (p579)
    "IN CASE OF OXE WITH SPATIAL REDUNDANCY, TC1652 EXPLAINS THE REQUIRED MANAGEMENT." (p231)
    "Reverse Proxy installation: TC2257 or TC2639 depending on OT version and RP configuration" (p601)
    "Clonezilla ... Refer to TC1625 for more detail" (p564)
  definition: |
    本教材外引的 ALE 技术通报族（Technical Communication/Bulletin）：TC2149 ed.04（rehosting 全矩阵，
    R2.3.1+，本书附录全文收录）；TC1652（OXE spatial redundancy 的 SIP/语音邮件管理）；TC2257/TC2639
    （SBC/反向代理安装，按版本二选一）；TC1625（Clonezilla 磁盘镜像）。生产化的权威依据。
  alias_or_related: Quick Reference Guide（p333，问候语细节）；Features list & Product limits（p507）
  tags: [resource, document, tc]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列术语逐条核对

说明：OVERVIEW 术语表 16 行，逐条核对如下——

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| OTMS | 正文有明确定义（p5/p115） | g01 |
| OTMS-v / OT-v | 有（p8-9） | g02 |
| OXE | 有（p5-6/p51） | g35 |
| OmniVista 8770 | 有（p6/p186+） | g36 |
| ICAS / ICM / AMS | 有（p6-7） | g03 |
| SOT | 有（p46/p53） | g05 |
| ALUID | 有（p131/p162） | g07 |
| FlexLM | 有（p131/p158） | g08 |
| Post-installation wizard | 有（p48/p88-89） | g06 |
| bics.conf | 有（p194） | g13 |
| Connection user | 有（p258/p264） | g09 |
| Conversation user | 本书中仅零星提及（p51 "User profile for Conversation users"、p497 组类型、p292 WPC 限制），无正式定义——按"仅 passing 提及"处理，归入 g09 的 alias 备查，不单列 |
| UDAS | 有（p223） | g14 |
| DAS rule | 有（p221/p253） | g15 |
| Local Storage voice mail | 有（p304/p327） | g18 |
| OTC PC / OTC PC One | 有（p432-459） | g39 + g29/g30 |
| rehosting | 有（p560-567） | g23 |
| TC2149 | 有（p561/p579） | g56 |

结论：**16 行全部落地，无"书中未出现"项；Conversation user 无定义、按备查处理。**

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：ACS/Stack（g04）、Directory user（g10）、三档案（g11）、Users 应用（g12）、Dialing/DAS 两规则（g15）、Phone formatting（g16）、Dongle（g17）、defaultVmsLS（g18）、General announcement（g19）、VM profile（g20）、Multi-devices（g21）、Supervision group（g22）、Maintenance Portal（g24）、OMS（g37）
- 角色：BP（g25）、Supervisor/Supervised（g26）、OT 三账户（g27）、OXE 三账户（g28）
- 订阅：Desktop right（g29）、Universal/Conferencing/Base Ct（g30）、Unified management（g31）、.ice（g32）、.swk/.sw8770/nmc.license（g33）、alchostid.cfg/OTID（g34）
- 产品：GD4/MIX484（g38）、OTC 家族（g39）、DM（g40）、OT SBC/RP（g41）、Mule/ESS（g42）、IPDSP/MicroSIP/REX（g43）、ITSP1（g44）、Clonezilla（g45）、AppGuard（g46）
- 协议：SIP/trunk（g47）、CSTA/DPNSS（g48）、IMAP/SMTP/VPIM（g49）、SNMP v3（g50）、PKCS 族（g51）、PXE/OVF 族（g52）、认证协议群（g53）、编解码族（g54）
- 资源：BPWS/MyPortal/TDL（g55）、TC 族（g56）

### 3. 仅 passing 提及、未单列条目的词（备查）

Conversation user（无定义，附 g09）、AAPP（p602）、AppGuard（已单列 g46 但仅一处）、OTCP（p9 兼容性工具，附 g01）、Cloud Connect（p130/132 许可控制的并列选项，附 g08/g33）、OTC Web / My Teamwork（p225 邀请默认客户端选项）、My Messaging / My Profile（p306/320/336/377，Web 自助页，正文已述）、VMS（语音邮件系统对象，附 g18）、808x/8082/8088/8001/8038/68（话机型号，p427/p567）、MIPT/DSU/SEPLOS（设备类型缩写，p439 未展开）、ghost Z（Nomadic 资源名，p445）、8AL90512US*/8AL90120US*（手册编号，附 g55）、Knowledge Hub（p2）。

### 4. 提取口径说明

- 所有定义只采信本书正文；SOT/FlexLM/ALUID/DDI 之外，OMS、GD4、Mule、ESS、REX、MIPT、DSU、SEPLOS、OTCP、AAPP 等缩写书中未给全称者，full_name 一律省略，不做外部补全。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准，引用均为原文摘录；原文笔误（MOFIFICATION/APLLIED/OUTLLOK/EMBBEDED/sesseion/notifiy/possibile、IP 表 192.16.8.1.x、端口 413）已在 n41 与对应条目标注。
- 实验口径值（IP/口令/号码/档案名）已在条目内显式标注，不作为生产口径。
