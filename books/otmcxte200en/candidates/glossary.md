# 术语/缩写/产品名候选 — OpenTouch Message Center Starter (OTMCXTE200EN R2.6 Issue 08)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 46 条（concept 15 / role 4 / subscription 2 / product 11 / protocol 8 / resource 6）。PRS/VPIM/ICE/OMS/BPWS/ALUID/OTID/OAM&P 等缩写书中未给全称的，full_name 字段如实省略，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: OTMC (OpenTouch Message Center)
  full_name: OpenTouch Message Center（书中展开）
  category: concept
  source_pages: p5-6, p13, p48
  source_quote: |
    "The OpenTouch™ Message Center is a stand-alone voice mail system installed on a single server, including
    automated attendant capabilities • The OpenTouch™ Message Center is specifically addressed to Connection
    users of an OmniPCX Enterprise • OTMC package replaces former 46xx/ 8440 messaging solutions" (p5)
  definition: |
    本书主角：单服务器独立语音邮件系统（定义含自动话务员能力），专门服务 OmniPCX Enterprise 的 Connection
    用户，取代 46xx/8440 旧信箱方案。纯语音邮件架构：消息存 OTMC 服务器或 SAN；访问通道 TUI（任意话机）、
    GUI（Premium Deskphone 8xx8 / Smart Deskphone 8088）、IMAP 邮件客户端。运行于 SUSE Linux Enterprise。
  alias_or_related: OTMC server + License server（p13 架构）；配置经 OmniVista 8770（p12）
  tags: [concept, core, voicemail]

- id: g02
  term: OTMC-V
  category: concept
  source_pages: p15, p24, p58
  source_quote: |
    "OpenTouch Message center software package dedicated to virtualized environment is called OTMC-V • OTMC-V
    can be proposed with either OXE or OXE-V • OTMC-V can be virtualized with VMware ESXi" (p15)
  definition: |
    面向虚拟化环境的 OTMC 软件包：可搭配 OXE 或 OXE-V，跑在 VMware ESXi 虚机上；支持 vMotion 与 VMware DRS
    （手动/半自动），同主机可多实例、可混跑 ALE/第三方应用虚机；限制与功能与非虚拟化版完全相同。许可绑定
    从 ALUID 改为 USB dongle（p16）。
  alias_or_related: 实验虚机规格见 p58（实验口径，生产看 MyPortal 安装手册）
  tags: [concept, virtualization, otmc-v]

- id: g03
  term: Connection user
  category: concept
  source_pages: p5, p109-112
  source_quote: |
    "The OpenTouch™ Message Center is specifically addressed to Connection users of an OmniPCX Enterprise" (p5)
    "OT applications: None; means that this OXE user has no access to OT applications such 'one number',
    'conferencing', 'OTC PC'…" (p112)
  definition: |
    OTMC 的目标用户类型：OXE 上的 Connection 类用户。建户时 OT applications=None 口径表示该 OXE 用户不用
    OpenTouch 套件应用（one number/会议/OTC PC 等），但仍然可以有 OTMC 语音邮箱——信箱业务与 OT 套件应用
    是两条独立的许可线。
  alias_or_related: 话机许可族对照见 g22（L316/L317 为 Connection 类话机许可）
  tags: [concept, users, licensing]

- id: g04
  term: Voice mail profile
  category: concept
  source_pages: p121, p126-127, p139, p146-152
  source_quote: |
    "Voice mailbox profiles that allow the administration of voice mail features shared by pools of Connection
    users. … By default, three voice mail profiles are created for OTMC • simplified, classic and advanced •
    You can create your owns" (p121)
    "Before validating the mailbox creation, it's mandatory to assign a profile to the voice mailbox" (p139)
  definition: |
    信箱批控模板：管理员用 profile 成池地控制信箱行为（Answer only/直拨回叫/受限访问/zero-out 等）、容量与
    期限（配额/问候与留言时长/新旧留言保留天数/IMAP 可达）与 TUI 密码管理策略。默认四个：Advanced/Classic/
    Simplified（LS 专用）+ Standard（UM 专用）；可自建。信箱创建时必须挂 profile 才能保存。
  alias_or_related: 参数逐项表见 principle p14；分配入口 = Voicemail box 的 Configuration 页签（p152）
  tags: [concept, profile, core]

- id: g05
  term: Local Storage (voicemail)
  category: concept
  source_pages: p137, p147, p169, p180
  source_quote: |
    "A voicemail system is created by default in OpenTouch and is based on Local Storage configuration." (p137)
    "This feature is provided to the following voice mail users: • Local Storage • Unified Messaging (UM) with
    Microsoft Exchange, Lotus Domino, or Gmail" (p169)
  definition: |
    语音邮件两种类型之一：留言存 OTMC 本地（默认语音邮件系统 defaultVmLS 即此类型）。通知增值功能里 wav
    附件、My Messaging 链接、回呼留言主、满箱/近满提醒为 LS 专属（p180 矩阵）；管理界面不按类型隐藏这些
    选项，但对 UM 用户无效（p190）。
  alias_or_related: 对照 g06 UM；defaultVmsLS（VMS 名称）
  tags: [concept, voicemail, storage]

- id: g06
  term: Unified Messaging (UM)
  full_name: Unified Messaging（书中展开）
  category: concept
  source_pages: p126, p147, p169
  source_quote: |
    "Unified Messaging (UM) with Microsoft Exchange, Lotus Domino, or Gmail" (p169)
    "'Standard' profile is dedicated to Unified Messaging." (p147)
  definition: |
    语音邮件另一种类型：留言落到统一消息后端（书中点名 Microsoft Exchange、Lotus Domino、Gmail）。profile
    类型选 UM 时对应 Standard 默认模板。UM 用户只有基础邮件/短信通知，LS 专属的通知增值（附件/链接/满箱）
    不可用；书内无任何 UM 落地配置步骤（仅支持性声明）。
  alias_or_related: 对照 g05 Local Storage；Voice mail profile 的 Type 取值（local storage, UM，p148）
  tags: [concept, voicemail, um]

- id: g07
  term: Visual Voice Mail (VVM)
  full_name: Visual Voice Mail（书中展开）
  category: concept
  source_pages: p122, p140, p149
  source_quote: |
    "Visual Voice Mail (VVM) access" (p122)
    "Request password for visual voicemail access on set: If selected (default value), the Visual Voice Mail
    (VVM) access requires password entry. This forces users to enter their TUI password to access the VVM and
    avoids having to lock device to secure the messages received." (p140)
  definition: |
    话机上的可视化语音信箱：Premium Deskphone 8xx8 与 Smart Deskphone 8088 经信封键（envelope key）直达
    （p8，新留言时消息键闪烁）。访问默认要求输 TUI 密码（用户级"Request password for visual voicemail access
    on set"默认选中）——不用锁整机也能保护留言。
  alias_or_related: TUI 密码见 g08；GUI 显示并发上限 5000 用户（p18）
  tags: [concept, vvm, phones]

- id: g08
  term: TUI / GUI password
  category: concept
  source_pages: p10, p130, p135, p142, p149
  source_quote: |
    "TUI password rules • Minimum TUI password size • TUI Password history length • TUI Password Validity
    Period • Maximum TUI logon failures • Locked period after Maximum logon failures reached" (p10)
    "Telephonic User Interface (TUI)" (p142/188 展开)
  definition: |
    信箱的两套用户密码：TUI（Telephonic User Interface，书中展开）密码用于话机语音信箱菜单与可视化信箱；
    GUI 密码用于网页（My Profile/MyMessaging）。TUI 密码策略五参数（最小长度/历史长度/有效期/最大失败次数/
    锁定时长）由管理员定义，默认值在 feature list（书外）；TUI 密码管理档位由 profile 控制（p149）。
  alias_or_related: 密码重置与 Force TUI password change（p135）；与话机 set secret code（默认 0000，p113/p116）
    是两套体系
  tags: [concept, passwords, tui]

- id: g09
  term: MWI (Message Waiting Indicator)
  full_name: Message Waiting Indicator（书中展开）
  category: concept
  source_pages: p171, p199
  source_quote: |
    "MWI: Message Waiting Indicator … MWI on the phone set is not synchronized when reading the email" (p171)
    "Voice message deposit … MWI notification … LED blinking" (p199)
  definition: |
    留言等待指示：新留言落箱时话机 LED 闪亮。邮件通知场景下读邮件不会灭灯（机制性不同步，非故障）；wav
    附件邮件可配"Deactivate MWI notification"（LS 用户，p190）。
  alias_or_related: IMAP 访问链路图中的 MWI notification（p199）
  tags: [concept, mwi, notification]

- id: g10
  term: Resurrection (method)
  category: concept
  source_pages: p113-115
  source_quote: |
    "The resurrection method is used when no physical address is allocated to the set … (shelf address=255,
    board address=255, equipment address=255). Resurrection consists in dialing the phone directory number &
    the password ('0000' by default) directly, from the set" (p113)
  definition: |
    数字/模拟话机的动态寻址法：话机处于无物理地址空态（255/255/255）时，在话机上直拨分机号+密码（默认
    0000），系统自动把真实物理地址（机架-板-位）绑给用户。也用于移机：配合 In/Out of Service 前缀先释放旧
    地址再在新位置重绑（前缀用 ednump –l XXX 查询）。
  alias_or_related: IP 话机无物理地址（恒 255/255/255，p115）；备选法 = 空闲地址表（System > Free addresses）
  tags: [concept, phones, addressing]

- id: g11
  term: General announcement
  category: concept
  source_pages: p210-223, p225-227
  source_quote: |
    "The general announcement allows customers to record and play a message to internal or external callers"
    (p212)
    "Only one general announcement can be recorded at a time. • Any new recording will overwrite the previous
    one. • Max duration: 5 minutes" (p223)
  definition: |
    企业广播：在留言落箱（外呼/内呼）与信箱查询前播放的公司级公告，用于品牌强化（企业铃音/配音）与信息
    通告。管理员定播报范围（三选可多选）并授权用户；授权用户经 TUI 增强菜单选项 6 录制/试听/停用，或经
    wav 文件部署（general_announcement.wav，CCITT A-law 8bits 8kHz mono）。硬限制：单条/覆盖/≤5 分钟。
  alias_or_related: 播报类型入口 = TUI global configuration（p225）；AA 废弃选项见 counter-example n19
  tags: [concept, announcement, branding]

- id: g12
  term: bics.conf
  category: concept
  source_pages: p79, p92
  source_quote: |
    "All post-installation settings are saved on a file called 'bics.conf'." (p79)
    "OTMC information can be found in the file bics.conf on the OTMC server: [otuser@otmc ~]$ more
    /var/data/bics/bics.conf" (p92)
  definition: |
    OTMC 站点配置账本：post-installation wizard 的全部设置落盘于此（/var/data/bics/bics.conf），含主机名/域
    与 ICE 三账户（otAdmin/otProfile/otuser 及加密口令）——8770 声明 OTMC 时的对账单。
  alias_or_related: ICE_* 参数前缀（ICE_USERNAME/ICE_USERPASSWORD/ICE_TEMPLATEUSERNAME/ICE_MAINTENANCEUSERNAME，
    p92；ICE 缩写未展开）
  tags: [concept, configuration, declaration]

- id: g13
  term: My Profile / MyMessaging
  category: concept
  source_pages: p11, p130, p153-166
  source_quote: |
    "Web interface for messages – My Messaging • Web interface for user options – My Profile" (p11)
    "Application available via a web browser using the following URL • https://<OpenTouch Messaging Center
    FQDN>" (p156) • "https://<OpenTouch Messaging Center FQDN/MyMessaging>" (p165)
  definition: |
    OTMC 两个用户自助 Web 应用：My Profile（URL=OTMC FQDN 根路径）管个人设置——语言/时区、personal assistant
    联系人与电话号码、信箱选项与问候激活、TUI 与 My Profile 密码、SMTP/SMS 通知；MyMessaging（URL=FQDN/
    MyMessaging 或经 My Profile 进入）在网页管理留言（列表/优先级/主叫/时长，PC 或话机播放）。登录用 GUI
    账号。
  alias_or_related: 通知参数可见性按管理员授权（p191 Note）
  tags: [concept, web-clients, self-service]

- id: g14
  term: High Availability (HA)
  category: concept
  source_pages: p74
  source_quote: |
    "High Availability Parameters … Install the system without high availability. … Enable: Checked if high
    availability has to be deployed. In this case, a secondary sever is required and post-installation wizard
    has to be run at the same time."
  definition: |
    OTMC 的高可用部署模式：post-install 向导 HA 页二选一（默认 Disable）。启用需副服务器且两台同时跑向导；
    HA 完整配置在"专门章节"（本书不含，属后续课程内容）。Starter 范围内只要求知道开关位置与前置条件。
  alias_or_related: DNS 清单中的冗余口径（无冗余/本地冗余/空间冗余，p73）是 OXE 侧概念，与 HA 配套
  tags: [concept, ha]

- id: g15
  term: Automated Attendant (AA) / VAA
  category: concept
  source_pages: p5, p225
  source_quote: |
    "…a stand-alone voice mail system installed on a single server, including automated attendant capabilities" (p5)
    "THE FIELD 'IS PLAYED FOR CALLS THAT ARRIVE ON AA' WAS USED WHEN THE AUTOMATED ATTENDANT WAS EMBEEDED IN
    THE OPENTOUCH SERVER. IT WILL HAVE NO IMPACT IN CASE OF (EXTERNAL) VAA SOLUTION USE FOR EXAMPLE." (p225)
  definition: |
    自动话务员：OTMC 产品定义中附带的能力（p5），但本书无任何 AA 配置内容。p225 揭示历史：OT 服务器曾内嵌
    AA（general announcement 播报选项第四项 "arrive on AA" 即此遗产，现已废弃）；如今外置 VAA 方案（VAA
    缩写书中未展开）下该选项无效。
  alias_or_related: 播报类型有效选项只剩三个（p225）
  tags: [concept, aa, legacy]

# ── 二、角色/账户 (role) ──

- id: g16
  term: otAdmin / otProfile / otuser（ICE 三账户）
  category: role
  source_pages: p75, p92-94, p100, p144
  source_quote: |
    "ICE_USERNAME='otAdmin' … Used by 8770 Configuration application to configure the OTMC server.
    ICE_TEMPLATEUSERNAME='otProfile' Used by 8770 server to retrieve and manage user profiles on OTMC
    ICE_MAINTENANCEUSERNAME='otuser' … Used by 8770 Maintenance application for OTMC backup and restore
    operations. Also used to access the OTMC via SSH." (p92)
  definition: |
    post-install 向导定义、登记在 bics.conf 的三个功能账户：otAdmin=8770 配置应用连 OTMC（全权管理，也用于
    WBM 登录）；otProfile=8770 取用/管理用户模板（受限权）；otuser=8770 维护应用做备份恢复 + SSH/SFTP 登录
    （非 OTMC 管理员，密码经 root 跑 /usr/bin/musett.sh 重置）。实验口令：Admin-8770 / Admin-T1 /
    maintenanceuser（实验口径）。
  alias_or_related: root/maintenance/administrator/profile/SNMP 五账户定义见 principle p03；otAdmin 密码丢失走
    WBM（p93）
  tags: [role, accounts, declaration]

- id: g17
  term: adfexc
  category: role
  source_pages: p87, p99
  source_quote: |
    "FTP Username / FTP Password: adfexc — Enter adfexc password (adfexc by default). This is the OXE FTP
    login and password used for data retrieval." (p87)
  definition: |
    OXE 的 FTP 账户（默认用户名/密码均为 adfexc）：8770 声明 OXE 时填写，用于数据提取（data retrieval）；
    OTMC 拓扑中声明 OXE 时同样要填（p99）。
  alias_or_related: 默认口令属实验/出厂口径，生产必须替换
  tags: [role, accounts, oxe]

- id: g18
  term: mtcl
  category: role
  source_pages: p118
  source_quote: |
    "On the CS : login as 'mtcl' • Command spadmin • Choice: 'Display active file'" (p118)
  definition: |
    OXE 呼叫服务器（CS）的维护登录账户：用它跑 spadmin 命令查看激活许可文件的用户许可计数（左=已用/右=可用），
    是话机许可核查的第二条路（第一条在 8770 的 Software package 过滤）。
  alias_or_related: spadmin 输出对照 L173/174/176/177/316/317（principle p11）
  tags: [role, accounts, licensing]

- id: g19
  term: Greeting Manager(s)
  category: role
  source_pages: p128, p144-145
  source_quote: |
    "Solution : Greetings Management Web Interface for Administrators / Greeting Managers • Manage all existing
    greeting types per user • Activate a greeting for a user • Delete existing / Download existing / Upload new
    greeting files • Number of greeting managers is not limited" (p128)
  definition: |
    问候语集中管理角色/网页（Greetings Management Web Interface）：可管理所有用户的全部问候语类型——激活、
    删除、下载、上传；数量不设上限。入口：8770 选 OT 节点右键 WBM → Users and devices/Voice mail greetings
    management（需再次认证，otAdmin 登录）。
  alias_or_related: 专业问候语来源 = OpenTouch MS/BE/MC 录音棚（p128 图示）
  tags: [role, greetings, admin]

# ── 三、许可项 (subscription) ──

- id: g20
  term: Voice mail 许可（Licenses 页签）
  category: subscription
  source_pages: p135, p141, p190
  source_quote: |
    "On Licenses tab … MyIC Business Communications: To be enabled. Voice mail: To be enabled. Messaging API:
    Optional." (p135)
    "Check that the users have the 'Voice mail' right enabled. … Voice mail: Enabled" (p141)
  definition: |
    OTMC 账户级三项许可开关：MyIC Business Communications（必须启用）、Voice mail（必须启用——没有它信箱
    不可用）、Messaging API（可选）。既有用户逐个核查 Licenses 页签是信箱排障第一步。
  alias_or_related: 用户通知另有 Right 类开关（Email/SMS notification right，p190-191）
  tags: [subscription, licensing, otmc]

- id: g21
  term: OXE 用户许可族（L173/L174/L176/L177/L316/L317）
  category: subscription
  source_pages: p117-118
  source_quote: |
    "'Analog users' for Z set (License 174) … 'Advanced reflexes users' for 8029 and 8039 (License 173) …
    'Connection reflexes users' 4019 (License 316) … 'Advanced IP users' for 8028, 8038 and 8068 (License 176)
    … 'Connection IP users' for 4008 and 4018 (License 317) … 'SIP users' for SEPLOS/SIP devices (License 177)" (p117)
  definition: |
    OXE 侧话机用户许可三族六类（TDM/IP/SIP）：L174 模拟（Z 设备）、L173 高级话务（80x9 系 UA 设备）、L316
    Connection 话务（4019）、L176 高级 IP（80x8 系）、L317 Connection IP（4008/4018）、L177 SIP（SEPLOS/SIP
    设备）。核查：8770 Software package 过滤或 mtcl+spadmin。
  alias_or_related: Connection user 概念见 g03；计数读数示例为实验口径（p118）
  tags: [subscription, licensing, oxe]

# ── 四、产品/组件名 (product) ──

- id: g22
  term: OmniPCX Enterprise (OXE / OXE-V)
  full_name: OmniPCX Enterprise（书中通篇使用）
  category: product
  source_pages: p5, p27, p83-108
  source_quote: |
    "The OpenTouch™ Message Center is specifically addressed to Connection users of an OmniPCX Enterprise" (p5)
    "OXE-V (virtual machine) • 'Physical' IP addressing: Host name: csa.company.com … Addressing by role (main
    CS): Host name: csm.company.com" (p27)
  definition: |
    ALE 企业级 PBX，OTMC 的宿主交换机（书名隐含主角的另一半）：OXE-V 为其虚机形态（物理地址 csa、main 角色
    地址 csm 双命名）。本书覆盖的 OXE 侧动作：声明准备（netadmin/节点号/实时同步）、SIP 对接（trunk/gateway
    5040/trusted/codec）、Connection 用户与话机开通。
  alias_or_related: 8770 中节点编号 = ABC×100+节点号（principle p08）；OXE CS/OXE Communication Server 同义
  tags: [product, pbx, core]

- id: g23
  term: OmniVista 8770 (8770-V)
  category: product
  source_pages: p12, p26, p83-101, p228-246
  source_quote: |
    "OTMC configuration is made through OmniVista 8770 • Same as OpenTouch, with a new node type and a new
    icon • Unified users management, Configuration, Alarms/topology, Performance, Backup/restore, …" (p12)
  definition: |
    ALE 网管/配置平台（虚机形态 8770-V）：OTMC 唯一的配置管理大脑（OTMC 是其中的新节点类型+新图标），统一
    用户管理、配置、告警/拓扑、性能、备份恢复。本书用它完成 OXE/OTMC 双向声明与同步、SIP/trunk 配置、用户
    创建、信箱与通知管理、备份恢复发起。安装物料需 8770 与 Windows 2008 R2 Server 许可键（p49，时代口径）。
  alias_or_related: 实验主机 nms.company.com=151.1.1.70（实验口径）；Configuration/Users/Maintenance 三应用
  tags: [product, management, core]

- id: g24
  term: OMS / OmniPCX Enterprise GD
  category: product
  source_pages: p22, p28, p31
  source_quote: |
    "OMS (virtual machine) • IP settings: Host name: oms.company.com • IP address: 151.1.1.13 • CS main
    address: 151.1.1.3" (p28)
    "OmniPCX Enterprise GD: gd.company.com = 151.1.1.12" (p31)
  definition: |
    实验拓扑中的两个组件：OMS（虚机，oms.company.com=151.1.1.13，指向 CS main 151.1.1.3）与 OmniPCX
    Enterprise GD（gd.company.com=151.1.1.12，仅出现在 DNS 主机名表）。两缩写书中均未展开全称、无任何配置
    或用途说明——引用时不得补全释义。
  alias_or_related: 实验拓扑见 f07
  tags: [product, lab, undefined]

- id: g25
  term: FlexLM server (FlexLM-V / flexlmd)
  category: product
  source_pages: p22, p25, p35, p42, p76-77, p82
  source_quote: |
    "The Flex-lm server can be embedded in the OTMC or installed on another server (which can be a virtual
    machine)." (p35)
    "service flexlmd stop … service flexlmd start … ./lmutil lmstat –a" (p82)
  definition: |
    flex-lm 许可服务器：可内嵌 OTMC、也可独立部署（可以是虚机 FlexLM-V）。管理 .ice 许可文件的加载（$LICENSES_HOME
    目录）；服务名 flexlmd；核验命令 $FLEXLM_HOME 下 ./lmutil lmstat –a。虚拟环境承载它的虚机必须挂 Aladdin
    USB dongle。
  alias_or_related: ALUID/dongle 绑定见 principle p05；$FLEXLM_HOME/$LICENSES_HOME 环境变量
  tags: [product, licensing]

- id: g26
  term: Eco-System VM
  category: product
  source_pages: p29-31
  source_quote: |
    "Eco-System (virtual machine) … Functions: • DNS server • Exchange server • Active directory • LDAP server
    • DHCP server (for mobiles)" (p29)
  definition: |
    实验环境的基础设施一体机（eco.company.com=151.1.1.100，Windows Server，实验口径）：一台虚机承担 DNS、
    Exchange、Active Directory、LDAP、DHCP（移动用户）五个角色；预置六个域用户（alban/adams/adore/barkley/
    backman/boop，密码 1234，实验口径）。教材后续的邮件通知（SMTP=eco:25）、LDAP、AD 都靠它。纯教学基础设施。
  alias_or_related: DNS 域 company.com 的唯一权威服务器（p31）；SMTP 服务器声明指向它（p184 实验口径）
  tags: [product, lab, infrastructure]

- id: g27
  term: VMware ESXi / vSphere
  category: product
  source_pages: p15, p22-23, p55-56, p58-59
  source_quote: |
    "Based on a VMware ESXi server • virtualizes server storage & networking, allowing multiple applications
    to run in virtual machines on the same physical server • vSphere client: Client installed on a PC used to
    administrate virtual machines hosted on a ESXi server" (p55)
  definition: |
    OTMC-V 的指定虚拟化平台：ESXi 主机（实验 esxi.company.com=151.1.1.250，实验口径）+ PC 上的 vSphere 客户端
    管理。安装面：装 ESXi → 装 vSphere（可从 ESXi 服务器下载）→ 建虚机；BIOS 关超线程 + ESXi 电源策略 High
    performance 是两个调优点。支持边界见 n26（仅 vMotion/DRS）。
  alias_or_related: OTMC-V 见 g02；USB 设备经 vSphere 转给虚机（p77）
  tags: [product, virtualization, vmware]

- id: g28
  term: Aladdin USB dongle
  category: product
  source_pages: p14, p16, p35, p40, p76-77
  source_quote: |
    "For virtualized deployment, ice license file is linked to a hardware dongle (Aladdin) plugged on the
    server • Software locks are linked to this specific physical server thanks to the dongle -ID controlled
    by the flex-lm server." (p16)
  definition: |
    虚拟化部署的许可硬件锚点（Aladdin 品牌 USB 加密狗）：.ice 许可经 dongle-ID 绑定到插狗的物理服务器；虚拟
    环境下必须挂到承载 FlexLM 的虚机。非虚拟化 ALE 整机不带狗（ALUID 贴纸绑定）。
  alias_or_related: dongle-ID、OTID、alchostid.cfg（p40 虚拟化许可综合图，OTID/alchostid.cfg 未展开释义）
  tags: [product, licensing, dongle]

- id: g29
  term: Premium Deskphone 8xx8 / Smart Deskphone 8088
  category: product
  source_pages: p6, p8, p10, p18
  source_quote: |
    "Direct access to visual voicemail from envelope key • Premium Deskphones 8xx8, Smart Deskphone 8088" (p8)
    "5000 simultaneous users with GUI display on series 8 sets, Premium Deskphones 80x8 and Smart DeskPhone
    8088" (p18)
  definition: |
    支持 OTMC 图形化可视化信箱（GUI）的话机系列：Premium Deskphone 8028/8038/8068 等 8xx8 系与 Smart
    Deskphone 8088——信封键直达 VVM、支持问候语菜单（p132）。GUI 显示总量上限 5000 并发用户（经 PRS）。
    其余话机走 TUI。
  alias_or_related: VVM 见 g07；问候语话机 GUI 入口（p132）
  tags: [product, phones, vvm]

- id: g30
  term: SUSE Linux Enterprise Server
  category: product
  source_pages: p13, p48, p58, p60-63
  source_quote: |
    "The OpenTouch™ Message Center server runs on a SUSE Linux Enterprise operating system." (p13)
    "OS: SUSE Linux Enterprise Server 12 (64bits)" (p58)
  definition: |
    OTMC 底座操作系统（虚机规格 64 位 SUSE 12，实验口径）：引导 DVD 安装（约 25 分钟），三种安装模式
    （硬件 GUI/虚拟化/单分区）。root 默认密码 letacla1（首登强改）。管理动作经 GNOME 终端/控制台（service、
    setup.bin、CheckSystemLinux.sh 等）。
  alias_or_related: p52 "Red Hat installation" 为原文笔误（见 counter-example n25）；时区必须勾 System clock
    uses UTC（p62）
  tags: [product, os, suse]

- id: g31
  term: Chameleon / Scorpio
  category: product
  source_pages: p17, p185, p186, p192
  source_quote: |
    "Chameleon (EVS + FWK)" (p17 架构图)
    "Notifications are handled by 'Scorpio' component." (p185)
    "The following services can be checked, stopped, restarted: • chameleon … Example: service chameleond
    status • scorpio … Example: service scorpiod status" (p192)
  definition: |
    OTMC 两个软件组件（EVS/FWK 缩写未展开）：Chameleon=OT 框架组件（TUI 应用相关，通知模板重启生效对象、
    架构图成员）；Scorpio=通知处理组件（SMTP 邮件/短信的发出者）。排障：service chameleond/scorpiod status；
    日志 /logs/chameleon/chameleon/panda.log、/logs/journal/chameleon.log、/logs/journal/scorpio.log。
  alias_or_related: 通知模板升级需重启 chameleon（n12）
  tags: [product, components, troubleshooting]

- id: g32
  term: IMAP4 Front End (imap4fed)
  category: product
  source_pages: p208
  source_quote: |
    "System services/ Topology/ Physical servers/ OT component/ 'IMAP4 Front End' • Connection security: Check
    the security type … IMAP port: Filled in automatically according to the security type … DON'T FORGET TO
    RESTART THE IMAP FRONT-END SERVICE: service imap4fed restart" (p208)
  definition: |
    OTMC 的 IMAP 服务组件与配置入口（System services/Topology/Physical servers/OT component 下）：Connection
    security 定加密类型（默认 IMAPS+TLS），IMAP 端口按安全类型自动带出；改安全级要改端口并 service imap4fed
    restart。
  alias_or_related: 客户端匹配规则见 principle p20 / counter-example n14
  tags: [product, imap, component]

# ── 五、协议/技术名 (protocol) ──

- id: g33
  term: SIP trunk group (T2 / ABC-F / Bypass)
  category: protocol
  source_pages: p18, p103-104
  source_quote: |
    "Direct SIP trunk group between OXE and OTMC • Only one SIP trunk is supported towards the front node •
    The SIP trunk group Bypass is configured for all ports available independently of the number of users" (p18)
    "Trunk Group Type: Select 'T2' type … Q931 Signal variant: Select ABC-F • T2 Specification: Select SIP" (p103)
  definition: |
    OXE↔OTMC 的直连中继：全系统仅一条、指向 front node；类型 T2、T2 Specification=SIP、Q931 变体 ABC-F；
    Bypass 按全部可用端口配置（与用户数无关）；SIP 虚拟接入数默认 2。与出局运营商 SIP trunk 是两种东西。
  alias_or_related: 端口口径见 principle p09（5040/5060/2570）
  tags: [protocol, sip, trunk]

- id: g34
  term: PRS (Link)
  category: protocol
  source_pages: p17, p18, p99
  source_quote: |
    "PRS Link between each OXE for GUI display • 5000 simultaneous users with GUI display on series 8 sets …" (p18)
    "Port: 2570 (OXE PRS port number)" (p99)
  definition: |
    OXE 之间的链路（PRS 缩写书中未展开全称）：支撑 8 系话机上的语音信箱 GUI（可视化信箱）显示，容量 5000
    并发用户；OXE 侧端口 2570。OTMC 声明进 OTMC 拓扑时 OXE 参数里要填对该端口。
  alias_or_related: GUI 话机系列见 g29
  tags: [protocol, prs, gui]

- id: g35
  term: VPIM
  category: protocol
  source_pages: p20, p185
  source_quote: |
    "VPIM protocol supported • To interconnect OTMC entities • To interwork with 3rd party VM" (p20)
    "To declare the SMTP server for notification to this component, a route has to be declared in VPIM
    sesssion: System services/ Applications/ Messaging/ VPIM" (p185)
  definition: |
    语音消息组网协议（缩写未展开）：用于 OTMC 实体互联、与三方语音邮件（3rd party VM）互通。本书的第二重
    身份：SMTP 通知的服务器路由也在 Messaging/VPIM 里声明（域名/FQDN/端口）——配置 SMTP 时别找错菜单。
  alias_or_related: SMTP 服务器声明步骤见 c09；三方互通细节书外（n28）
  tags: [protocol, vpim, networking]

- id: g36
  term: SMTP / POP3 / IMAP4 / IMAPS
  category: protocol
  source_pages: p174, p197-198, p205-208
  source_quote: |
    "Email sending … SMTP protocol used for emails sending • POP3 and IMAP4 protocols for reception • POP3
    used to retrieve all received emails • IMAP4 used for direct consultation to mail server" (p197)
    "BY DEFAULT, IMAPS IS ENABLED ON OPENTOUCH SIDE WITH 'TLS' SECURITY" (p208)
  definition: |
    邮件协议族在本书的分工：SMTP=发信（通知发往外部 SMTP，OTMC 不提供）；POP3=全量下载收信（对照项）；
    IMAP4=直连服务器查阅不落地（OTMC 信箱的邮件客户端访问方式）；IMAPS=IMAP over TLS（OTMC 默认启用）。
    通知用的 SMTP 必须无认证无 TLS。
  alias_or_related: IMAP 客户端配置见 c10；START TLS/RFC 2595（p7，IMAP4 特性描述中引用）
  tags: [protocol, email, imap]

- id: g37
  term: G.711 / G.729
  category: protocol
  source_pages: p7, p108, p184
  source_quote: |
    "G.711, G.729 native support" (p7)
    "Compression type: G 729 • Multi. Algorithms for Compression: False" (p108)
    "Audio file format: AAC/.AAC, linear PCM 16bits/.wav, linear PCM 8bits/.wav, G.711 PCM/.wav" (p184)
  definition: |
    语音编解码：OTMC 原生支持 G.711 与 G.729（p7 特性）；OXE↔OTMC 对接实验把压缩算法定为 G.729、关多算法
    （p108）。通知附件音频格式另有四种（AAC/PCM16/PCM8/G.711 wav，p184），与通话编解码是两套口径。
  alias_or_related: general announcement wav 格式为 CCITT A-law 8bits 8kHz mono（p223，又一独立口径）
  tags: [protocol, codec]

- id: g38
  term: DPNSS prefix
  category: protocol
  source_pages: p108
  source_quote: |
    "3.2. DPNSS prefix … This prefix is used to optimize the transfers through trunk groups. … 3.3. Routing
    optimization: For considering the DPNSS prefix the routing optimization must be set to 'Yes'." (p108)
  definition: |
    经中继组优化转接用的前缀机制（DPNSS 缩写未展开）：在 Translator/Prefix plan 建条目（实验 D1234，实验
    口径），并必须把 Routing Optimisation 设为 Yes 才生效。
  alias_or_related: 与 SIP trunk 配置同章（c05 步骤 10-11）
  tags: [protocol, dpssn, routing]

- id: g39
  term: CCITT A-law 8bits 8kHz mono
  category: protocol
  source_pages: p223, p227
  source_quote: |
    "The name must be 'general_announcement.wav' • Format: CCITT A-law 8bits 8kHz mono" (p223)
    "Notes: Format: CCITT A-law 8bits 8kHz mono" (p227)
  definition: |
    general announcement wav 文件的强制音频格式（两页一致）：CCITT A-law、8 位、8kHz、单声道；文件名固定
    general_announcement.wav。格式不符的 wav 无法用作广播（录音棚产出口径见 p128）。
  alias_or_related: 存放路径两处不一致见 n18
  tags: [protocol, audio, format]

- id: g40
  term: flex-lm / .ice / ALUID / OTID
  category: protocol
  source_pages: p16, p35-36, p40, p42
  source_quote: |
    "The license mechanism is flex-lm based. • OTMC license file: <license>.ice • …the ALUID is a unique 128
    bits identifier based on hardware characteristics of the server." (p35)
    "the encrypted ALUID can be retrieved the Operating Sytem installation using the command: /usr/bin/getaluid" (p36)
  definition: |
    许可技术栈：flex-lm=许可控制机制（缩写未展开）；.ice=OTMC/OXE 许可文件扩展名；ALUID=128 位硬件特征标识
    （定义给出、全称未展开；整机贴纸或 /usr/bin/getaluid 取加密值）；OTID=虚拟化综合图中出现的标识（p40，
    未展开释义）。许可文件装 $LICENSES_HOME，新文件要重启 flexlmd。
  alias_or_related: FlexLM/dongle 见 g25/g28；8770/OXE 许可文件（.swk/.zip/hardware.mao/nmc.license8770 等，
    p38/p40 综合图）
  tags: [protocol, licensing, identifiers]

# ── 六、文档/资源/路径 (resource) ──

- id: g41
  term: MyPortal / BPWS / Business Portal
  category: resource
  source_pages: p58, p50, p246
  source_quote: |
    "Follow the procedure described in the OTMC installation manual document 'otmc2.6.1_im_InstalManual_8AL90120USAH_1_en',
    available on MyPortal" (p58)
    "Download all software ISO files from the BPWS" (p50)
    "A technical communication (TC2024) … available on the Business Portal" (p246)
  definition: |
    ALE 三个资料入口名称（书中均未展开全称）：MyPortal=取 OTMC 安装手册（otmc2.6.1_im_InstalManual_8AL90120USAH_1_en
    第 6.2 章）；BPWS=取软件 ISO（安装介质来源）；Business Portal=取技术通报 TC2024。三者指向何站、如何取权
    限，书内未说明。
  alias_or_related: TC 文档见 g43
  tags: [resource, portal, documentation]

- id: g42
  term: Feature list / Product limits document
  category: resource
  source_pages: p10, p13, p48
  source_quote: |
    "Those values are defined by the administrator. Refer to the feature list for the default values." (p10)
    "Note: for hardware and software specifications refer to feature list and product limits document" (p13)
  definition: |
    两份权威外部文档：feature list（特性清单——TUI 密码策略默认值、硬件软件规格的指定出处）与 product limits
    document（产品上限）。OTMC 生产方案的规模与规格问题的最终依据，本书反复外指但不含其内容。
  alias_or_related: OpenTouch Capacity Planning Tool（p19，扩容评估工具，用法书外）
  tags: [resource, document, capacity]

- id: g43
  term: TC1652 / TC2024 / Quick Reference Guide
  category: resource
  source_pages: p105, p142, p246
  source_quote: |
    "THIS CONFIGURATION IS GIVEN IN THE TC1652" (p105)
    "All details about greetings are available on the Quick Reference Guide document in the chapter 'Managing
    your welcome greetings message'." (p142)
    "A technical communication (TC2024) … explains all implementation steps to deploy a NFS server on the 8770
    server" (p246)
  definition: |
    三份被外指的文档：TC1652（空间冗余 OXE 上为外置信箱声明 SIP 网关的专项配置）；TC2024（在 8770 上部署 NFS
    server 以回收 OTMC 备份的实施步骤，Business Portal 可取）；Quick Reference Guide（用户问候语管理细节，
    "Managing your welcome greetings message" 章）。
  alias_or_related: 触发条件见 counter-example n29（TC 类）；f18（QRG）
  tags: [resource, document, tc]

- id: g44
  term: /var/data 目录族
  category: resource
  source_pages: p42, p79, p82, p92, p185, p223, p227, p251, p256
  source_quote: |
    "$LICENSES_HOME (var/data/licenses)" (p42) • "/var/data/bics/bics.conf" (p92) •
    "$DATA_HOME/panda /notification4 ('/var/data/panda/notification4')" (p185) •
    "/var/data/general_announcement" (p223) 与 "/var/data/ics-group/general_announcement" (p227) •
    "'/var/data/ics-group/vms/ngvm3/'" (p256)
  definition: |
    OTMC 的 SUSE 侧关键路径一览：/var/data/licenses（=$LICENSES_HOME，许可文件）；/var/data/bics/bics.conf
    （站点配置账本）；/var/data/panda/notification4（通知模板，按语言 properties）；general_announcement 目录
    （GA wav，路径两处口径见 n18）；/var/data/ics-group/vms/ngvm3（statistics.properties 所在）；统计输出目录
    （实验口径 /var/data/ics-group/vms/statistics，需手工建）。日志在 /logs/...（p192）。
  alias_or_related: $DATA_HOME（p185 顶级变量）；8770 侧 C:\8770_ARC\OTBackup（p240）与 C:\8770\log（p88）
  tags: [resource, paths, linux]

- id: g45
  term: OpenTouch Suite for MLE / OT applications
  category: resource
  source_pages: p3, p14, p21, p112
  source_quote: |
    "Voice messaging dedicated commercial package is OT based and can evolve towards the full OT suite" (p14)
    "OT applications: None; means that this OXE user has no access to OT applications such 'one number',
    'conferencing', 'OTC PC'…" (p112)
  definition: |
    OpenTouch 套件语境：OTMC 是"OT based"的语音消息专用包，可演进到全 OpenTouch Suite for MLE（书眉章节名
    亦用此称）；OXE 用户级 "OT applications" 字段（None 口径）决定其能否用 OT 套件应用（one number/会议/
    OTC PC 等）——与是否拥有 OTMC 信箱无关。MLE 缩写书中未展开。
  alias_or_related: Connection user 见 g03
  tags: [resource, suite, naming]

- id: g46
  term: enterprise-education.csod.com（Find a Course）
  category: resource
  source_pages: p259
  source_quote: |
    "Browse our catalog available on https://enterprise-education.csod.com/ to find your training path and
    course detail." (p259)
  definition: |
    ALE 培训目录站点（书尾"Find a Course"）：查培训路径与课程详情的入口。培训反馈另给邮政地址（Brest）与
    邮箱 emea.education-services@al-enterprise.com。
  alias_or_related: 纯收尾页信息，无技术内容
  tags: [resource, training, website]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列候选术语逐条核对

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| OTMC | 正文有明确定义（p5） | g01 |
| Connection user | 有明确定义（p5/p112） | g03 |
| OTMC-V | 有明确定义（p15） | g02 |
| flex-lm / .ice / ALUID | flex-lm 与 .ice 有机制定义（p35）；ALUID 有定义、全称未展开（p35-36） | g40（ALUID 定义性用法，full_name 省略） |
| PRS | 仅有用途与端口描述（p18/p99），全称未展开 | g34（full_name 省略） |
| VPIM | 仅有用途描述（p20/p185），全称未展开 | g35（full_name 省略） |
| MWI | 有展开定义（p171） | g09 |
| TUI / GUI | TUI 有展开（p142）；GUI 未展开 | g08（GUI 全称省略） |
| VVM | 有展开定义（p122/p140） | g07 |
| Voice mail profile | 有明确定义（p121/p139） | g04 |
| Local Storage / UM | UM 有展开（p169）；LS 为类型名 | g05 / g06 |
| resurrection | 有明确定义（p113） | g10 |
| bics.conf | 有明确定义（p79/p92） | g12 |
| My Profile / MyMessaging | 有明确定义（p11/p156/p165） | g13 |
| Chameleon / Scorpio | 有组件与职责描述（p17/p185/p192），EVS/FWK 未展开 | g31 |
| general announcement | 有明确定义（p212/p223） | g11 |
| automated attendant (AA) | 有定义性表述与历史说明（p5/p225）；VAA 未展开 | g15 |

结论：OVERVIEW 术语表 19 行全部在本书正文有定义或定义性用法，无"仅 passing 提及需排除"项。

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：High Availability（g14）、AA/VAA（g15）
- 角色/账户：otAdmin/otProfile/otuser（g16）、adfexc（g17）、mtcl（g18）、Greeting Manager（g19）
- 许可项：Voice mail 许可三开关（g20）、OXE 用户许可族（g21）
- 产品/组件：OXE/OXE-V（g22）、OmniVista 8770（g23）、OMS/GD（g24，未展开释义）、FlexLM（g25）、Eco-System VM（g26）、ESXi/vSphere（g27）、Aladdin dongle（g28）、Premium Deskphone/8088（g29）、SUSE（g30）、Chameleon/Scorpio（g31）、IMAP4 Front End（g32）
- 协议/技术：SIP trunk group（g33）、PRS（g34）、VPIM（g35）、邮件协议族（g36）、G.711/G.729（g37）、DPNSS prefix（g38）、CCITT A-law 格式（g39）、许可标识族（g40）
- 文档/资源/路径：MyPortal/BPWS/Business Portal（g41）、Feature list/Product limits（g42）、TC1652/TC2024/QRG（g43）、/var/data 目录族（g44）、OpenTouch Suite for MLE/OT applications（g45）、培训目录站（g46）

### 3. 仅 passing 提及、未单列条目的词（备查）

- OTID、alchostid.cfg（p40 许可综合图，无释义，附于 g28/g40）
- ESS/ICS/ACS/FAX/MOH（p232 备份数据库组件名，无展开，附于 f23 上下文）
- ICE_*（bics.conf 参数前缀，附于 g12；"Gateway type ICE type"（p105）同前缀，附于 g14/f14）
- EVS/FWK（p17 架构图缩写，附于 g31）、OAM&P/UDA/MS（p17，附于 f03）
- SEPLOS（p117 话机名，附于 g21）、OTC PC / one number（p112 OT 应用举例，附于 g45/g03）
- RUFUS、D.S.T.（p71 夏令时展开）、START TLS / RFC 2595（p7，附于 g36）
- noreply 类地址无；SMTP 实验服务器 eco.company.com（附于 g26/g35）
- VAA（p225，未展开，附于 g15）

### 4. 提取口径说明

- 所有定义只采信本书正文；PRS、VPIM、ICE、OMS、GD、BPWS、ALUID（有定义无全称）、OTID、OAM&P、UDA、MS、EVS、FWK、MLE、DPNSS、VAA、flex-lm 等缩写书中未给全称，full_name 字段一律省略或注明"未展开"，不做外部补全。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准，引用均为原文摘录（p36 "Sytem"、p84 "MOFIFICATION"、p84 netmask 示例等为原文原样，已在 counter-example n17/n25 注明）。
- 实验口径值（IP/密码/账号/分机号/许可读数）均在相关条目标注"实验口径"。
```
