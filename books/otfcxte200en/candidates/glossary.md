# 术语/缩写/产品名候选 — OpenTouch Fax Center Starter (OTFCXTE200EN R9.2 Ed04)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 55 条（六类全覆盖）。缩写纪律：书中给出全称的记 full_name（如 FoIP、NDR、IIS）；未给全称的一律不编造（如 CSID/DNIS/ANI/DDI/ARS/MLE/SMB/CSGD/MMC/BIRT/GDPR 等），definition 内注明"书中未展开"。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: OpenTouch Fax Center (OTFC)
  full_name: OpenTouch Fax Center
  category: concept
  source_pages: p1, p4-5
  source_quote: |
    "The OpenTouch Fax Center solution is a suite of powerful fax services which interact with the
    OmniPCX Enterprise (OXE) • Hardware agnostic • Installed on a dedicated server or virtual
    machine" (p4)
    "Server to Receive or Send Faxes • Web based administration and client-based administration •
    Active Directory® directory service/Microsoft Exchange integration • Fax Document
    Management..." (p5)
  definition: |
    本书主角：与 OmniPCX Enterprise 交互的传真服务套件，硬件无关，装在专用服务器或虚机上。
    能力面：收发传真服务器、Web+客户端双管理、AD/Exchange 集成、文档管理、出局转换（把文档转
    成传真发出）与入局分发（收传真送图片与信息到各目的地）、归档审计、安全合规（GDPR/HIPAA/
    FERPA/SOX 类法规语境，缩写书中未展开全称）。软件名中带 OpenTouch，与 ALE OpenTouch 通信
    套件同族（（推断）族谱关系，书中未明说）。
  alias_or_related: XM Fax / XMedius（安装目录与文件名中出现的血统名，见 g48 Interstar Technologies）；通信套件封面写 "Communication Suite for MLE"（MLE 未展开）
  tags: [concept, product-core]

- id: g02
  term: System
  category: concept
  source_pages: p22
  source_quote: |
    "System •Global management & system settings •Sites management" (p22)
  definition: |
    概念模型顶层：做全局管理与系统设置、管理所有站点。安装时选 "Create a new system" 即创建
    一个新系统（p49）。
  alias_or_related: 下一级是 Site（g03）
  tags: [concept, model]

- id: g03
  term: Site
  category: concept
  source_pages: p22-23
  source_quote: |
    "Site •Virtual Fax Server •Each site has its own set of users and settings. •Sites are
    isolated from each other. •One fax belongs to one and only one site." (p22)
    "A virtual fax server that shares system resources. Typically, a Site can be associated to a
    company, a branch or a department depending on the size of the organization (a single company
    can have several sites, one for each department...)" (p23)
  definition: |
    虚拟传真服务器：共享系统资源的逻辑分片。每个站点有自己的用户集与设置；站点间相互隔离；
    一份传真属于且仅属于一个站点。可对应公司/分支/部门——一个公司可拆多站点让各部门"各有
    一台传真机"。评估许可下最多 10 个站点（p52）。
  alias_or_related: 用户与设置挂在站点下；入局路由表/Profile/邮件通知 Profile 都以站点为命名空间（Sites ➤ Site ➤ Configuration ➤ …）
  tags: [concept, multi-tenancy]

- id: g04
  term: User
  category: concept
  source_pages: p23
  source_quote: |
    "User • Anyone who can use the system to send, receive and manage faxes. A user belongs to a
    Site and has an assigned faxing Profile. In OpenTouch Fax Center, a user is always identified
    by an SMTP Address." (p23)
  definition: |
    能用系统收发管理传真的人。三个绑定：属于一个 Site、有一个 faxing Profile、恒以 SMTP 地址
    （邮箱）为身份标识。内部用户建于 OTFC 可导出 CSV；AD 用户经 NT Account 属性反查 SMTP 地址
    登录（p100）。
  alias_or_related: 目录集成查询的起点就是用户 SMTP 地址（p194）
  tags: [concept, identity]

- id: g05
  term: Profile
  category: concept
  source_pages: p23, p118
  source_quote: |
    "A set of Attributes such as cover sheet information, organizational information (Site name
    and address, phone number, etc.); billing code information; fax priority, fax header and
    number of retries; security; and notification options and format. A Profile can be used for
    one or more users." (p23)
  definition: |
    用户策略模板：封面信息、组织信息（站点名/地址/电话）、计费码、传真优先级/报头/重试次数、
    安全（选项/覆盖策略/号码限制）、通知选项与格式的属性集合，可服务一个或多个用户。默认两档：
    Basic（正常优先级可发）与 No Faxing Rights（禁发）。限制组、邮件通知 Profile、公共电话簿、
    封页都经它下发到用户。
  alias_or_related: 管理路径 Sites ➤ Site ➤ Configuration ➤ Profile（p120）
  tags: [concept, policy]

- id: g06
  term: Directories Integration
  category: concept
  source_pages: p23, p194
  source_quote: |
    "A set of rules that tell the system how to query internal or external directories to find
    user Attributes. A pattern match is sent to the sender's SMTP Address." (p23)
    "OTFC has its own Internal Directory, but it can also interact with Active Directory or any
    other LDAP Directory. On a fresh install, the system is configured to by default use only the
    OpenTouch Fax Center Internal Directory." (p194)
  definition: |
    目录集成：一组规则，定义系统如何查询内部/外部目录找用户属性。系统查询总是从用户的 SMTP
    地址开始；NT Account 登录场景（SendFAX/Web 界面）会先由 NT 账号解析出 SMTP 地址。新装默认
    只用内部目录，可加 AD 或任意 LDAP 目录。
  alias_or_related: 查询结果联动 Site/Profile Lookup 表（g19/g20）；断连产生 SNMP trap（p196）
  tags: [concept, directory]

- id: g07
  term: Input / Output Attributes
  category: concept
  source_pages: p24
  source_quote: |
    "Input Attributes • Attributes used to locate a user in a directory. ; Output Attributes •
    Attributes yielded when the Directories Integration is queried with one or more input
    attributes such as Site Name, Profile Name or Personal Information." (p24)
  definition: |
    目录集成的一对属性：输入属性用于在目录中定位用户；输出属性是查询命中后返回的属性——站点名、
    Profile 名或个人信息。是 Lookup 表自动归类的数据来源。
  alias_or_related: Personal Information（g08）
  tags: [concept, directory]

- id: g08
  term: Personal Information
  category: concept
  source_pages: p24, p103
  source_quote: |
    "Personal Information • Refers to the personal Attributes of users (e.g. name, address, phone
    number, etc.)" (p24)
    "Specify personal information: • First name, last name, address... ; Define the phone number ;
    Define the fax number" (p103)
  definition: |
    用户的个人属性：姓名、地址、电话号码、传真号等，建内部用户时逐项填写。传真封页/报头的
    组织与个人信息即来源于 Profile 与用户设置。
  alias_or_related: 输出属性可返回个人信息（p24）
  tags: [concept, users]

- id: g09
  term: Notification
  category: concept
  source_pages: p24
  source_quote: |
    "Notifications • Are issued when: • A new fax is received. • An outbound fax is sent or has
    failed to send. • A broadcast (outbound fax to multiple recipients) is completed. • Can be of
    type: • Email, Printer or Folder" (p24)
  definition: |
    事件通知：新传真到达、外发成功/失败、广播完成三类事件触发；投递类型三种——Email、Printer、
    Folder。邮件通知的格式由 Mail Notification Profile 定义（每语言一份，经用户 Profile 关联）。
  alias_or_related: 排障查 ConfigManager.log 与 Smtp.log（p208）
  tags: [concept, notification]

- id: g10
  term: Outgoing Queue
  category: concept
  source_pages: p25
  source_quote: |
    "Outgoing Queue •Shows progress of faxes that are being sent. •Statuses: Preprocessing
    (converting documents and rendering coversheet), Delayed, Ready to Send, Sending, Waiting,
    Sent. •Faxes can be viewed (images and details) and cancelled." (p25)
  definition: |
    外发队列：正在发送中的传真进度视图，六状态（转换文档渲染封面/延迟/待发/发送中/等待/已发），
    可查看图像与详情、可取消。用户只见自己的，管理员见全部。
  alias_or_related: Web Client 界面对应 "Outgoing queue: Fax sent in transit"（p81）
  tags: [concept, queue]

- id: g11
  term: Outbound History / Inbound History
  category: concept
  source_pages: p25
  source_quote: |
    "Outbound History •Faxes that have been sent. •Statuses: Sent or Failed (cancelled, failed to
    reach destination, etc). •Faxes can be viewed (images and details) or resubmitted. ; Inbound
    History •Faxes that have been received. •Statuses: Received or Failed to receive (not all
    pages were transmitted). •Faxes can be viewed (images and details), rerouted and forwarded." (p25)
  definition: |
    两个历史视图：外发历史（已发传真，状态 Sent/Failed，可重提交）；入呼历史（已收传真，状态
    Received/Failed to receive 即页数不全，可重路由、转发）。与外发队列并称三视图。
  alias_or_related: Web Client 界面 Inbound history/Outbound 区（p81）
  tags: [concept, history]

- id: g12
  term: Broadcast
  category: concept
  source_pages: p28
  source_quote: |
    "Broadcasting is the distribution of a same fax to multiple recipients. Faxes in a broadcast
    share: • The same attachments • The same coversheet." (p28)
  definition: |
    广播：同一传真分发多个收件人；广播内各传真共享相同附件与相同封面。广播完成时可通知发起人
    （p10）。入口涵盖邮件、Webmail、SENDFAX XML 文件等提交方式。
  alias_or_related: Notification 事件之一"广播完成"
  tags: [concept, broadcast]

- id: g13
  term: 'FAX' address space
  category: concept
  source_pages: p164
  source_quote: |
    "The 'FAX' address space • Create a new send connector. • Associate the 'FAX' address space to
    this Connector and forward all mails to a smart host which corresponds to the fax server's
    SMTP Gateway. • Optionally, you can also associate a fax subdomain to this connector in the
    SMTP address space" (p164)
  definition: |
    Exchange 侧的地址空间：新建 Send Connector 关联 fax:* 并把邮件转发到智能主机（=传真服务器的
    SMTP 网关），可选再挂传真子域。它带来 Outlook 传真联系人、SendFAX Outlook/Exchange 模式、
    富文本与自定义表单属性传输等增强特性。SMTP connector 是许可特性。
  alias_or_related: 寻址语法 [FAX:号码]、[FAX:姓名@号码]、[FAX:/fn=/ln=/jobtitle=@号码]
  tags: [concept, exchange]

- id: g14
  term: First Time Setup Wizard
  category: concept
  source_pages: p50, p65-67
  source_quote: |
    "The role of the First Time Setup Wizard is to perform the minimal system configuration so
    that you can begin faxing immediately." (p67)
  definition: |
    首次安装向导：完成最小系统配置让人立刻能传真——建站点、QOS 0/0/240、默认 Profile 去 SMTP
    认证、CSID=站点名、建首用户、站点/系统路由表、告警通知、邮件中继、产出摘要存盘共 12 项。
    不用它可全部手工配或事后运行 FirstTimeSetup.exe。
  alias_or_related: 向导只呈现 Internal Database 与 AD 集成两种最常用用户配置（p50/p100）
  tags: [concept, ftw]

- id: g15
  term: Restriction group
  category: concept
  source_pages: p121
  source_quote: |
    "Restriction groups • A barring table could be linked to one/several user profile(s) • E.g.
    National only: International numbers are forbidden ; Associate the restriction group to a user
    profile" (p121)
  definition: |
    限制组：一张拦截（barring）表，可挂到一个或多个用户 Profile，控制外发号码范围——书中例
    "仅国内：禁国际号码"。这是传真侧的号码闭锁，与 OXE 语音侧闭锁是两套体系。
  alias_or_related: 入方向的拒收是站点级 Calling Number Restriction（g16）
  tags: [concept, barring]

- id: g16
  term: Calling Number Restriction
  category: concept
  source_pages: p122
  source_quote: |
    "To Block numbers directly from the administration interface for a site • Incoming calls are
    refused upfront during call setup • From Fax administration interface in the • Sites ->
    General Settings -> Calling Number restrictions" (p122)
  definition: |
    站点级来话号码限制：在管理界面按站点直接屏蔽号码，来话在呼叫建立阶段就被拒接（不耗传真
    资源）。路径：Sites ➤ General Settings ➤ Calling Number restrictions。与 Restriction group
    （出方向、挂 Profile）方向相反。
  alias_or_related: Restriction group（g15）
  tags: [concept, barring, inbound]

- id: g17
  term: Site Lookup table / Profile Lookup table
  category: concept
  source_pages: p198-200
  source_quote: |
    "Site & Profile Lookup tables ; Apply to external users ... A user who is not associated to
    any existing Site and any existing Profile is not allowed to use OTFC. Through these lookup
    tables it is possible to grant the faxing rights to some users" (p198)
    "Specific conditions can be created to apply a profile to users • These rules are based on
    the attributes provided by the directories integration • By default the profile applied to one
    user is specified in his settings: • It is the default rule: Use the Profile specified by
    Profile" (p199)
  definition: |
    两张外部用户自动归类表：Site Lookup 把用户按目录属性归到站点；Profile Lookup 把 Profile 按
    规则（可按邮箱/传真号/职务等任意字段过滤）指给用户——默认规则是"用用户设置里指定的
    Profile"。没被归到站点与 Profile 的外部用户不能用 OTFC。
  alias_or_related: 依赖 Directories Integration（g06）提供的属性
  tags: [concept, lookup]

- id: g18
  term: NT Account Lookup
  category: concept
  source_pages: p100, p201-203
  source_quote: |
    "The NT Account Lookup feature allows users to access the OpenTouch Fax Center the client
    applications without authentication. There are two ways to obtain this result: By using the
    Active Directory NT Account Lookup specific interface ; By configuring an LDAP Directory
    integration with specific NT parameters" (p201)
  definition: |
    NT 账号查询：让用户免认证使用 OTFC 客户端应用（Web Client 与 SendFAX 用 Windows 账号登录时
    经 NT Account 属性反查 SMTP 地址）。实现两路：AD NT Account Lookup 专用接口，或 LDAP 集成里
    配 samAccountName 搜索过滤器再加条件。
  alias_or_related: 配套 IIS 禁匿名+启 Windows 认证实现 Web 自动登录（p204）
  tags: [concept, nt-account, sso]

- id: g19
  term: MediaStore
  category: concept
  source_pages: p217, p223
  source_quote: |
    "Fax images and documents (MediaStore) • TIFF images of sent and received faxes. • Documents
    which composed outbound faxes. • Stored under the Data\MediaStore." (p217)
  definition: |
    传真媒体库：收发传真的 TIFF 图像与组成外发传真的原始文档，存于 Data\MediaStore。是备份三
    数据域之一；传真删除策略中"传真文档"就指这里的图像文件。
  alias_or_related: 与 MySQL 元数据层（g41）配对构成归档两层
  tags: [concept, storage, backup]

- id: g20
  term: Cover Sheet (.cse)
  category: concept
  source_pages: p92-96
  source_quote: |
    "Create and modify coversheets (.cse) files (proprietary format)" (p92)
    "Assign the new coversheet in user Profiles. Several coversheets can be associated to a
    profile" (p96)
  definition: |
    封面页：传真首页的版式文件，专有格式 .cse。经 Coversheet Editor 创建/修改（页面尺寸/分辨率/
    区域设置/注释），从服务器下载底稿、另存、经 Web 管理导入、最后挂到用户 Profile（一个 Profile
    可挂多张）。封面语言受安装语言影响。
  alias_or_related: 经 Profile 下发、仅管理员管理（p129）
  tags: [concept, coversheet]

# ── 二、角色 (role) ──

- id: g21
  term: System Administrator
  category: role
  source_pages: p77, p108, p110
  source_quote: |
    "System administrator: global administration of the systems and sites." (p77)
    "System administrators ; Manage the whole system • Can have multiple System Administrators" (p108)
    "Create new SYSTEM administrator It is recommended to create a backup administrator •
    Authentication based on internal server, AD and SAML" (p110)
  definition: |
    系统管理员：管理整个系统（全部站点），可设多名；认证基于内部服务器、AD 与 SAML。官方推荐
    另建一个备份管理员防锁死。日志大小/保留期等系统级配置只有 System Administrators 能改（p225）。
  alias_or_related: 对照 Site Administrator（g22）；登录界面分两栏（p113）
  tags: [role, admin]

- id: g22
  term: Site Administrator
  category: role
  source_pages: p77, p109, p111
  source_quote: |
    "Site administrator: manage only its own site" (p77)
    "Site administrators ; Has the right to configure a Site, not the whole system • i.e. Site:
    My Organization" (p109)
  definition: |
    站点管理员：只有权配置自己的站点（如实验站点 My Organization），不能动整个系统。建号四步
    （p111）。多租户/部门分权场景的角色。
  alias_or_related: 对照 System Administrator（g21）
  tags: [role, admin]

- id: g23
  term: Reseller
  category: role
  source_pages: p52
  source_quote: |
    "To purchase and receive a license, you will need to provide your OpenTouch Fax Center
    reseller with your server physical (MAC) address." (p52)
  definition: |
    经销商：本书中唯一出场场景是许可采购——把传真服务器物理（MAC）地址提供给 reseller 换取正式
    许可文件。角色体系（与 OXE/Rainbow 侧 BP/DR/IR 类似的经销分级）本书未展开。
  alias_or_related: 许可导入见 p53（仅手工）
  tags: [role, licensing]

# ── 三、许可/订阅 (subscription) ──

- id: g24
  term: Default License (evaluation)
  category: subscription
  source_pages: p52
  source_quote: |
    "When installing OpenTouch Fax Center for the first time on a server, a default license is
    automatically • Installed for evaluation purposes, that: • Enables one instance of each
    component • Enables a total of two channels (FoIP and fax boards) in evaluation mode • Enables
    up to 10 sites with no time limit • Allows for 100 users • Applies a watermark on every fax
    page" (p52)
  definition: |
    出厂自动安装的评估许可：每组件 1 实例、FoIP+传真板卡合计 2 通道、最多 10 站点不限时、100
    用户、每页水印。用于评估；验收前换正式许可。
  alias_or_related: 许可控制两级=组件上限（users/sites/gateways/channels）+特性开关（p52）
  tags: [subscription, licensing]

- id: g25
  term: Licensed feature (SMTP connector)
  category: subscription
  source_pages: p158
  source_quote: |
    "SMTP connector is a licensed feature" (p158)
  definition: |
    许可特性示例：SMTP 连接器（Exchange 'FAX' 地址空间集成）受许可特性开关控制。含义：许可除
    数量上限外还管功能可用性——功能装上了但许可不含时不可用。其余许可特性清单未在本书展开。
  alias_or_related: 'FAX' address space（g13）
  tags: [subscription, licensing, smtp]

- id: g26
  term: License import
  category: subscription
  source_pages: p53
  source_quote: |
    "Import licenses ; Import license file manually only" (p53)
  definition: |
    许可导入：只能手工导入许可文件（无自动/在线激活通道）；采购前置动作是向经销商提供服务器
    MAC 地址。位置在 General settings 一带（p54 "Still in General settings Check info entered
    during installation / Password policy" 同章）。
  alias_or_related: Default License（g24）、Reseller（g23）
  tags: [subscription, licensing]

# ── 四、产品 (product) ──

- id: g27
  term: OmniPCX Enterprise (OXE)
  full_name: OmniPCX Enterprise
  category: product
  source_pages: p4, p7, p34
  source_quote: |
    "The OpenTouch Fax Center solution is a suite of powerful fax services which interact with the
    OmniPCX Enterprise (OXE)" (p4)
    "T38 / SIP connection to OmniPCX Enterprise" (p7)
  definition: |
    ALE 企业通信服务器（PBX）：OTFC 的话路对端。传真话路由 OXE 经 SIP/T.38（或 G.711 透传）接入，
    PSTN 侧模拟传真走 T.30；OXE 侧需配 SIP private trunk 与 SIP 网关（MGR 七步）；空间冗余时
    双呼叫服务器进 Peer List。互通细节参照 TC3048。
  alias_or_related: 生态图中的 CSGD 缩写出现在 OXE 侧（p34，书中未定义）
  tags: [product, pbx]

- id: g28
  term: OmniVista 8770
  full_name: OmniVista 8770 Network Management & Billing
  category: product
  source_pages: p11, p152, p212-213
  source_quote: |
    "Accounting Via OmniPCX Enterprise – OmniVista 8770" (p11)
    "Use MGR or Omnivista 8770 to manage" (p152)
    "8770 gets the accounting tickets from the OmniPCX Enterprise • Use reports in 8770 billing
    application to analyse telecommunications costs" (p212)
  definition: |
    ALE 网络管理与计费平台：两个出场角色——①传真计费（从 OXE 取计费票、出电信成本报表，票
    默认映射用户传真号）；②OXE SIP 网关的替代管理界面（与 MGR 命令行并列）。
  alias_or_related: Accounting 机制（p212-213）
  tags: [product, management, billing]

- id: g29
  term: SendFAX
  category: product
  source_pages: p83, p86-87
  source_quote: |
    "SendFAX is the fax interface for users with advanced faxing needs. •SendFAX configured in
    Outlook mode (i.e. to send the faxes through Outlook connected to Exchange) requires the use
    of a 'FAX' address space" (p86)
    "Permits users to send faxes •Preview the fax in real time •with Outlook •Access to
    phonebooks •Coverpage management •Attachment management •Fax options management •Allows to
    hide sensitive information with redact tool •Draw black boxes to hide information" (p86)
  definition: |
    Windows 发传真客户端（进阶用户向）：实时预览、Outlook 模式、电话簿、封面管理、附件管理、
    传真选项、redact 涂黑工具（画黑块遮敏感信息）。Outlook 模式依赖 Exchange 'FAX' 地址空间。
    界面分区：手工寻址字段/收件人/缩略图/传真预览（p87）。
  alias_or_related: Windows 客户端三件套之一；提交走 XML（p17 SendFAX XML）
  tags: [product, client]

- id: g30
  term: Web Fax Composer printer
  category: product
  source_pages: p83, p88-89
  source_quote: |
    "the Web Fax Composer Printer is installed on your pc, you can send faxes via the Web Client
    interface by printing documents from any Windows application ; User authentication is required" (p88)
    "faxes are sent via the Web Client interface" (p89)
  definition: |
    虚拟打印机客户端：装后从任意 Windows 应用"打印"即把文档经 Web Client 界面发传真；需要用户
    认证。适合已习惯打印流程的用户，免学习成本。
  alias_or_related: Windows 客户端三件套之一
  tags: [product, client, printer]

- id: g31
  term: Print to Mail
  category: product
  source_pages: p83, p90
  source_quote: |
    "From any document, select the new virtual printer named 'Print to Mail' to send the document
    (TIFF) to Outlook, which can be then sent as: •Classical e-mail •Fax" (p90)
  definition: |
    虚拟打印机客户端：任意文档"打印"成 TIFF 交到 Outlook，再由用户决定作为普通邮件或传真发出。
    与 Web Fax Composer 的区别是落点在 Outlook 而非 Web 界面。
  alias_or_related: Windows 客户端三件套之一；走邮件服务器+Email connector 路径（p17）
  tags: [product, client, printer]

- id: g32
  term: Coversheet Editor
  category: product
  source_pages: p92-94
  source_quote: |
    "This application enables users and administrators to create their own cover sheets / modify
    existing ones ; Cover Sheet Settings •Page Size •Resolution •Local used for Date & Time
    formatting ... Create and modify coversheets (.cse) files (proprietary format) •Tiff Viewer:
    •A good tiff viewing application •Rotate, mirror pages •Insert annotations (text, images,
    drawings) • Available in 8 languages and 2 paper sizes" (p92)
  definition: |
    封面编辑器：创建/修改 .cse 封面文件的客户端应用；设置页面尺寸、分辨率、日期时间区域格式；
    内置 Tiff 查看器（旋转/镜像/插注释）；8 种语言 2 种纸张。位于 FaxCenter\Client 目录，可打开
    Samples 或从服务器下载的封页。
  alias_or_related: Cover Sheet (.cse)（g20）
  tags: [product, client, coversheet]

- id: g33
  term: MMC Snap-in
  category: product
  source_pages: p74-75, p83
  source_quote: |
    "MMC Snap-in application • Software installed with the Fax server. Can be also installed from
    client setup.exe wizard • Available in: C:\Program Files\Alcatel-Lucent Enterprise\FaxCenter\Client" (p74)
  definition: |
    管理控制台（MMC 缩写书中未展开全称，指微软管理控制台载体的管理单元形态——（推断）通用含义）：
    随传真服务器安装，也可从客户端安装包装；位于 FaxCenter\Client 目录。与 Web 管理页并称管理
    双入口。注意用户 CSV 导入/导出仅 Webadmin 有。
  alias_or_related: Web administration page（g34）
  tags: [product, admin]

- id: g34
  term: Web administration page (faxadmin)
  category: product
  source_pages: p74, p76, p95
  source_quote: |
    "Web administration page • To access: • Launch your Web browser • http://<ServerName_or_IP>/faxadmin
    or https://<ServerName>/faxadmin" (p74)
  definition: |
    Web 管理页：浏览器访问 http(s)://<服务器名或IP>/faxadmin 的管理界面；与 MMC 功能并列（双入口）
    且独占用户 CSV 导入导出、封页导入等操作（p95 封面导入、p104-105 用户 CSV）。
  alias_or_related: 认证与 MMC 相同（SMTP 地址或 Windows 认证，p77）
  tags: [product, admin, web]

- id: g35
  term: Web Client
  category: product
  source_pages: p79-81
  source_quote: |
    "Available from any web browser ... •Compliant with section 508 of the US Rehabilitation Act &
    European e-inclusion •HTTP/HTTPS support ... To access: • http://<ServerName_or_IP>/fax or
    https://<ServerName>/fax. User authentication is required" (p79-80)
  definition: |
    用户 Web 传真客户端：免安装、任意浏览器（举例 Firefox/Safari/Chrome）、HTTP/HTTPS、符合
    508 条款与欧洲 e-inclusion 无障碍要求。六区界面：Compose/Inbound history/Outbound/Outgoing
    queue/Manage faxes & contacts/Inbox。Web Fax Composer 打印机经它发传真。
  alias_or_related: 访问口径实验值 http://localhost/fax（p116）
  tags: [product, client, web]

- id: g36
  term: MySQL
  full_name: MySQL（关系数据库，书中以产品名使用）
  category: product
  source_pages: p29, p180, p217-218, p231
  source_quote: |
    "MySQL is used by the XMFaxArchive and XMCoConfig services of the OTFC. • MySQL is required as
    the back-end database server to store data and some configurations." (p29)
  definition: |
    OTFC 的后端数据库：XMFaxArchive 与 XMCoConfig 服务用，存数据与部分配置。承载传真元数据
    （收发记录）。备份时要单独停 mysql5 服务并整拷数据目录（实验口径路径 C:\Program
    Files\MySQL\MySQL Server 8.0\Data）。随第三方组件安装（安装向导"全选第三方软件"包含它）。
  alias_or_related: CompanyConfig 与 XmediusArchive 两个数据库在升级时不在自动备份内（p221）
  tags: [product, database]

- id: g37
  term: Microsoft Exchange
  full_name: Microsoft Exchange（书中版本语境 2019/2016/2013 与 Exchange online/O365）
  category: product
  source_pages: p5, p40, p164-170
  source_quote: |
    "Active Directory® directory service/Microsoft Exchange integration" (p5)
    "Microsoft Exchange gives access to additional faxing features. • SMTP connector management
    required" (p166)
  definition: |
    微软邮件服务器：OTFC 的增强集成对象——Outlook 传真联系人、SendFAX Outlook 模式、富文本/
    自定义表单属性传输都要 Exchange（任意 SMTP 服务器只能走基础邮件传真）。集成动作是建 'FAX'
    地址空间 Send Connector + 调 Receive Connector 放行通知。
  alias_or_related: Mail Notification Profile 勾 "Exchange integration"+Text（p126）
  tags: [product, mail]

- id: g38
  term: BIRT Report Designer
  category: product
  source_pages: p226
  source_quote: |
    "It is possible to manage and customize the report templates by using the BIRT report designer
    •To install the BIRT report designer , unzip the .zip file found in the 3rd\birt folder of the
    OTFC installation package ; 31 reports are available" (p226)
  definition: |
    报表设计器：用来自定义 OTFC 的 31 个报表模板（BIRT 缩写书中未展开全称）。从安装包 3rd\birt
    目录下的 zip 解压安装。报表可含数值与图形，覆盖全系统/单用户、月/周/日、模块错误摘要。
  alias_or_related: Reports（p226-227）
  tags: [product, reporting]

# ── 五、协议 (protocol) ──

- id: g39
  term: FoIP
  full_name: Fax over IP（书中直接展开）
  category: protocol
  source_pages: p7
  source_quote: |
    "Fully software-based • Fax over IP • SIP/TCP and SIP/TLS • T38 / SIP connection to OmniPCX
    Enterprise" (p7)
  definition: |
    IP 传真：OTFC 的实现方式——全软件传真，话路走 SIP/TCP 或 SIP/TLS，经 T.38/SIP 连 OXE。
    与传统传真板卡（fax boards，许可语境出现）相对。
  alias_or_related: 许可通道口径 "FoIP and fax boards"（p52）
  tags: [protocol, foip]

- id: g40
  term: SIP
  category: protocol
  source_pages: p7, p142, p148-150
  source_quote: |
    "SIP/TCP and SIP/TLS • T38 / SIP connection to OmniPCX Enterprise" (p7)
    "SIP configuration • Local SIP UDP port: 5360 • Activate SIP message in log files (for
    maintenance) • SIP authentication" (p142)
  definition: |
    会话信令协议（全称书中未展开）：OTFC 与 OXE 间传真话路的信令。OTFC 侧监听 UDP 5360；支持
    SIP 认证；可激活 SIP 消息日志辅助维护；OXE 侧抓 SIP trace 用 motortrace/traced 命令。
  alias_or_related: SIP/TLS 在概览出现但配置路径未展开（见 counter-example n32）
  tags: [protocol, sip]

- id: g41
  term: T.38
  category: protocol
  source_pages: p7, p34, p181
  source_quote: |
    "Fax transmission protocol: • T.38 • Group 3 fax • speed of up to 14.4kbps" (p7)
    "Using the H.323/SIP (T .38/G.711) protocols ; A fax driver can handle multiple simultaneous
    fax calls" (p181)
  definition: |
    IP 传真实时传输协议（全称书中未展开，标准名 T.38）：OTFC 与 OXE 间的主传真通道，含 Group 3
    传真，最高 14.4kbps。FaxDriver 用 H.323/SIP（T.38/G.711）收发。
  alias_or_related: 对照 G.711 透传（g42）
  tags: [protocol, fax]

- id: g42
  term: G.711
  category: protocol
  source_pages: p7, p34, p181
  source_quote: |
    "• G.711 • Speed of up to 33.8kbps" (p7)
  definition: |
    语音编码透传传真（全称书中未展开，标准名 G.711）：把传真当语音流透传，速率最高 33.8kbps，
    比 T.38 快但对网络抖动更敏感（（推断）敏感性比较为电信常识，原文只给速率）。
  alias_or_related: T.38（g41）
  tags: [protocol, fax]

- id: g43
  term: T.30
  category: protocol
  source_pages: p34
  source_quote: |
    "T.30 ... Analog fax ... PSTN ... T.30" (p34)
  definition: |
    传统模拟传真协议（全称书中未展开，标准名 T.30）：PSTN 上模拟传真机使用的协议，在架构图中
    位于 OXE 的 PSTN 侧——OTFC 域内不用它，模拟传真经 OXE 网关转换。
  alias_or_related: T.37（g44）、T.38（g41）
  tags: [protocol, fax, analog]

- id: g44
  term: T.37
  category: protocol
  source_pages: p16, p34
  source_quote: |
    "T.37 capable LAN multifunction printer ▪From multifunction printers" (p16)
  definition: |
    存储转发传真协议（全称书中未展开，标准名 T.37）：本书场景指具备 T.37 能力的局域网多功能
    一体机（MFP）可直接向 OTFC 提交传真。
  alias_or_related: MFP（multifunction printer，p16 有英文全称）
  tags: [protocol, mfp]

- id: g45
  term: Group 3 fax
  category: protocol
  source_pages: p7
  source_quote: |
    "Fax transmission protocol: • T.38 • Group 3 fax • speed of up to 14.4kbps" (p7)
  definition: |
    三类传真标准（全称书中未展开，ITU G3 传真）：与 T.38 并列出现在传输协议清单，速率口径
    14.4kbps。
  alias_or_related: T.38（g41）
  tags: [protocol, fax]

- id: g46
  term: H.323
  category: protocol
  source_pages: p181
  source_quote: |
    "• Using the H.323/SIP (T .38/G.711) protocols" (p181)
  definition: |
    多媒体信令协议（全称书中未展开，标准名 H.323）：FaxDriver 收发传真支持的另一信令族，书中
    仅此一处提及，与 SIP 并列；未展开配置路径。
  alias_or_related: SIP（g40）
  tags: [protocol]

- id: g47
  term: SMTP
  category: protocol
  source_pages: p30, p157-161, p183
  source_quote: |
    "The XMSmtpGateway module, called SMTP Gateway, has the two usual basic functions of a mail
    server, allowing the Fax Server to: • Receive emails from OTFC users in order to convert them
    into faxes. • Send emails to OTFC users for notification purpose" (p157)
  definition: |
    简单邮件传输协议（全称书中未展开，通用标准名词）：OTFC 邮件侧的入口与出口——SMTP 网关监听
    25 端口收传真作业、发通知邮件；邮件可经邮件服务器/中继中转。
  alias_or_related: NDR (Non-Delivery Report)（p161 有全称）
  tags: [protocol, mail]

- id: g48
  term: LDAP
  category: protocol
  source_pages: p11, p135, p138-139, p194-197
  source_quote: |
    "Export users list • SNMP trap V2 • e.g. connection problem with an external LDAP directory" (p11)
    "The OpenTouch Fax Center Phone Books can be accessed through LDAP connection" (p135)
  definition: |
    目录访问协议（全称书中未展开，通用标准名词）：三处用途——①目录集成查外部用户（AD 为默认
    LDAP）；②电话簿 LDAP 访问（Enable LDAP Access）；③SNMP trap 上报连接问题。声明参数：端口
    389、Search base、属性映射。
  alias_or_related: Directories Integration（g06）、NT Account Lookup（g18）
  tags: [protocol, directory]

- id: g49
  term: DTMF
  category: protocol
  source_pages: p9, p209
  source_quote: |
    "Inbound routing methods •DNIS, CSID, ANI, DTMF" (p9)
    "Allows users to send or receive faxes with adding DTMF codes for additional numbering
    dialing. ... +33155667000 P 1234 ; P = Pause" (p209)
  definition: |
    双音多频信令（全称书中未展开，通用电信名词）：传真收发的补拨分机机制——目的地号码后加 P
    （暂停）与 DTMF 分机号；来话方向可激活语音提示让主叫键入分机。是四种入局路由方法之一。
  alias_or_related: DNIS/CSID/ANI（g50-g51）
  tags: [protocol, dtmf, routing]

- id: g50
  term: DNIS
  category: protocol
  source_pages: p9
  source_quote: |
    "Inbound routing methods •DNIS, CSID, ANI, DTMF" (p9)
  definition: |
    入局路由四法之一（全称书中未展开；通用电信含义为"被叫号码识别服务"——（推断）括注）。配合
    Incoming Routing Table 的 $did:?????$ 匹配来话被叫（DDI）号码。
  alias_or_related: $did:?????$（p207）；DDI（p205，全称未展开）
  tags: [protocol, routing]

- id: g51
  term: CSID / ANI
  category: protocol
  source_pages: p9, p67
  source_quote: |
    "Inbound routing methods •DNIS, CSID, ANI, DTMF" (p9)
    "Sets the CSID of the default profile to the Site name ... with CSID set to Site Name" (p67)
  definition: |
    两个主叫侧识别标识（全称书中未展开；通用电信含义 CSID=被叫方传真机标识/ANI=主叫号码识别
    ——（推断）括注）。CSID 在 OTFC 里还是可配属性：FTW 把默认 Profile 的 CSID 设为站点名，
    System 路由表也带 CSID=站点名——即本机对外出示的传真机身份。
  alias_or_related: DNIS（g50）、DTMF（g49）
  tags: [protocol, routing, identity]

# ── 六、资源 (resource) ──

- id: g52
  term: FaxCenter\Bin\Util folder (xmsc / FirstTimeSetup.exe)
  category: resource
  source_pages: p67, p188, p218, p231
  source_quote: |
    "the Administrator has the option to run this application at a later time from the Fax
    directory by executing the following file: [install_path]\Alcatel-Lucent
    Enterprise\FaxCenter\Bin\Util\FirstTimeSetup.exe" (p67)
    "All these commands can be executed from the <install_path>\FaxCenter\Bin\Util folder. •
    xmsc –ra ... xmsc –oa ... xmsc -aa" (p188)
  definition: |
    命令工具目录：传真安装目录下的 Bin\Util。两个工具：①xmsc——服务管理（-ra 重启全部、-oa
    停止全部、-aa 启动全部）；②FirstTimeSetup.exe——事后重跑首次安装向导。
  alias_or_related: 备份流程以 xmsc -oa 开头、xmsc -aa 收尾（p218/231-232）
  tags: [resource, tools, commands]

- id: g53
  term: Trace folder
  category: resource
  source_pages: p189, p225
  source_quote: |
    "Log files location: • C:\Program Files\Alcatel-Lucent Enterprise\FaxCenter\Trace" (p189)
    "Trace folder stores log files for all the OTFC services." (p225)
  definition: |
    日志目录：全部 OTFC 服务的日志所在（每组件一个专属日志文件）。默认单文件 20MB、归档保留
    15 天，满后 zip 压缩进 Archive 文件夹。排障高频落点：ConfigManager.log、Smtp.log。
  alias_or_related: SIP 日志激活与级别调整在管理界面（p190-191）
  tags: [resource, logs]

- id: g54
  term: ClientRedistribution folder
  category: resource
  source_pages: p84
  source_quote: |
    "A reduced client applications set including only independent applications usable by most of
    the users (no administration tools) is available through the installation files located in the
    ClientRedistribution folder" (p84)
  definition: |
    精简客户端包目录：发行介质内只含独立应用（无管理工具）的客户端安装文件，面向大多数最终
    用户批量分发（配 GPO/静默安装）。
  alias_or_related: Windows 客户端部署口径（p83）
  tags: [resource, clients, deployment]

- id: g55
  term: TC3048
  category: resource
  source_pages: p141, p147
  source_quote: |
    "To manage SIP connexion between the OTFC & OmniPCX Enterprise, you have to refer to the
    Technical Communication: • TC3048 • Manage SIP on OTFC side • Manage SIP on OmniPCX Enterprise
    side • Maintenance" (p141)
  definition: |
    ALE 技术通信文档（Technical Communication）编号 3048：OXE-OTFC SIP 互通的权威操作文档，
    覆盖 OTFC 侧 SIP、OXE 侧 SIP、维护三块。OXE 侧网关参数细节一律以它为准，本书只给 MGR 菜单
    序列骨架。
  alias_or_related: p147 "use the TC3048"
  tags: [resource, documentation]

- id: g56
  term: SNMP V2 (traps)
  full_name: SNMP V2（书中协议名；trap 机制未展开全称）
  category: resource
  source_pages: p11, p196, p228
  source_quote: |
    "Export users list • SNMP trap V2 • e.g. connection problem with an external LDAP directory" (p11)
    "SNMP V2 Services • Component status changes •Incoming queue reaches max size •Site outbound
    quota reaches maximum size •Rasterization failure •Routing failure •XML file reading error
    •Driver transmission error •Partition detection •Channel initialization failure •Host monitor
    traps" (p228)
  definition: |
    监控上报通道：OTFC 以 SNMP V2 trap 对外发告警——组件状态变化、入呼队列满、站点出呼配额满、
    光栅化失败、路由失败、XML 读取错误、驱动发送错误、分区检测、通道初始化失败、主机监视
    （性能计数器/组件状态表/通道状态/远程心跳）；LDAP 断连也走 trap。
  alias_or_related: 网管平台由客户环境提供（书中未展开对接）
  tags: [resource, monitoring, snmp]

- id: g57
  term: Interstar Technologies (registry key)
  category: resource
  source_pages: p218, p231-232
  source_quote: |
    "Export the HKEY_LOCAL_MACHINE\SOFTWARE\Interstar Technologies key from Regedit to a .reg file" (p218)
  definition: |
    备份/恢复涉及的注册表键：HKEY_LOCAL_MACHINE\SOFTWARE\Interstar Technologies——OTFC 配置与
    状态的注册表落点。键名揭示产品血统：OTFC 前身是以色列 Interstar Technologies 的 XMedius
    传真产品线（升级章节的 xmedius.war、CompanyConfig/XmediusArchive 数据库名同源）（（推断）
    血统关系为键名与文件名的合理推断，书中未明说）。
  alias_or_related: xmedius.war（p221）、MediaStore（g19）
  tags: [resource, registry, backup]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-24）的术语类覆盖率

| task | 任务 | 术语类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 评估方案能力 | 有 | g01, g39-g46 | OTFC 定位与 FoIP/传真协议族 |
| task-02 | 规划部署架构 | 有 | g27 | OXE 对端角色 |
| task-03 | 准备宿主 | — | — | 无独立术语（IIS 角色为 Windows 概念，不单列） |
| task-04 | 安装软件 | 有 | g14, g36 | FTW、MySQL（第三方组件） |
| task-05 | 跑 FTW | 有 | g14 | First Time Setup Wizard |
| task-06 | 处理许可 | 有 | g23-g26 | Reseller、默认许可、许可特性、导入 |
| task-07 | 用户管理 | 有 | g04, g08, g18 | User/SMTP 身份、个人信息、NT Account |
| task-08 | 管理员 | 有 | g21, g22 | System/Site 两级 |
| task-09 | 客户端 | 有 | g29-g31, g33-g35, g54 | 四件套+双管理入口+Web Client+精简包 |
| task-10 | 封页 | 有 | g20, g32 | .cse 与编辑器 |
| task-11 | Profile | 有 | g05, g15-g17 | Profile、限制组、呼号限制 |
| task-12 | 电话簿 | 有 | g48 | LDAP 访问 |
| task-13 | OTFC 侧 SIP | 有 | g40 | SIP（UDP 5360） |
| task-14 | OXE 侧网关 | 有 | g27, g28 | OXE、8770（管理面） |
| task-15 | 抓包 | — | — | 命令类在 principle p31 |
| task-16 | 邮件集成 | 有 | g13, g25, g37, g47 | FAX 地址空间、许可特性、Exchange、SMTP |
| task-17 | 服务架构 | 有 | g36, g52, g53 | MySQL、Bin\Util、Trace |
| task-18 | 目录与路由 | 有 | g06, g07, g17, g18, g49-g51 | 目录集成、属性、Lookup、NT、路由四法 |
| task-19 | 计费 | 有 | g28 | 8770 计费角色 |
| task-20 | 备份恢复 | 有 | g19, g36, g57 | MediaStore、MySQL、注册表键 |
| task-21 | 升级 | 有 | g57 | xmedius 血统（升级陷阱在 counter-example n23） |
| task-22 | 删除策略 | 有 | g19 | MediaStore（记录/文档两类） |
| task-23 | 报表监控 | 有 | g38, g56 | BIRT、SNMP V2 |
| task-24 | 日志排障 | 有 | g53 | Trace 目录与两个日志文件名 |

**覆盖结论**：
1. 六类齐备：concept 20 条（g01-g20）、role 3 条（g21-g23）、subscription 3 条（g24-g26）、product 12 条（g27-g38）、protocol 13 条（g39-g51）、resource 6 条（g52-g57），共 57 条。
2. 缩写纪律执行情况：FoIP/NDR/IIS/MFP 等书内给出全称的已记 full_name；CSID/DNIS/ANI/DDI/ARS/MLE/SMB/CSGD/MMC/BIRT/NT/GDPR/HIPAA/FERPA/SOX/T.30/T.37/T.38/G.711/H.323/SNTP 类书内未展开的，full_name 留空或不写，定义内括注处均已标"（推断）"或"书中未展开"；g57 Interstar Technologies 血统与 g42 G.711 敏感性为推断，已标注。
3. 24 项 task 中 task-03/15 无独立术语（分别由 principle p09-p11、p31 承接），其余 22 项均有术语条目，无缺口。
