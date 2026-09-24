# 术语/缩写/产品名候选 — OmniVista 8770 (8770XTE200EN Ed47)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 58 条，按 concept / role / subscription / product / protocol / resource 六类组织。DDI/TDS/MLE/GCS 等缩写书中未给全称，full_name 字段如实省略，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: OmniVista 8770
  category: concept
  source_pages: p5-6, p55
  source_quote: |
    "Centralized network management solution ... HTML interface for network administration
    management (Users, Configuration, Performance) ... The OmniVista 8770 Server must be installed
    on a dedicated server" (p5-6, p55)
  definition: |
    ALE 的集中网络管理解决方案（本书主题）：单台专用 Windows 服务器承载管理应用套件，经 thick client
    与 WBM 轻客户端对 OXE/OXO Connect/OpenTouch 做配置、用户、告警、报表、备份的统一管理。
  alias_or_related: OV8770（日志前缀）、NMC（服务与配置树根名）
  tags: [concept, platform]

- id: g02
  term: Node / Network / Subnetwork（配置树三级）
  category: concept
  source_pages: p111, p121-123, p658
  source_quote: |
    "CONFIGURATION TREE — NETWORK / PCX / HARDWARE / DEVICES & USERS / SUB-NETWORKS" (p111)
    "Subnetwork number must be equal to the OmniPCX Enterprise network number" (p122)
    "the OmniVista 8770 server converts it in a declaration node applying the following rule:
    (Subnetwork number X 100) + OXO Connect node number" (p658)
  definition: |
    Configuration 应用的被管对象树：Network（8770 侧自由编号）> Subnetwork（号须等于 OXE 网络号）>
    PCX 节点（OXE/OXO Connect/OpenTouch）；节点声明号 = 网络号（子网号）×100 + 节点号，是同步、
    告警、备份目录的组织主键。
  alias_or_related: Declaration node（8770Handle 许可核验的锚点，见 g30）
  tags: [concept, topology, numbering]

- id: g03
  term: Synchronization（Complete/Partial × Separate/Global）
  category: concept
  source_pages: p114, p125-126
  source_quote: |
    "Complete synchronization: Retrieve all technical data from the PCX ... Partial synchronization:
    Retrieve data changed since the last synchronization for the following entries: Users,
    Directory, Data terminals, Speed dial numbers, Remote users" (p114)
  definition: |
    从 PCX 检索技术数据的过程：Complete（全量）/Partial（五类条目增量、其余全取）× Separate（单
    节点）/Global（连带 OpenTouch）四种组合；OXE 侧变更经事件实时回传，无需重复同步。
  alias_or_related: Real Time Synchronization（事件联动）；Data Collection（同步时间与审计记录页签）
  tags: [concept, synchronization]

- id: g04
  term: Profile（OXE 用户档案）
  category: concept
  source_pages: p173-176, p183-186
  source_quote: |
    "WITH PROFILES: 1 – Profiles creation, 2 - Profile applied during user creation process: > Set
    of predefined options ready to be used" (p173)
    "Use profile with auto. recognition — To be enabled. This parameter allows creating a user from
    a profile." (p183)
  definition: |
    OXE 侧 Set Function=Profile 的特殊用户对象：预置 COS 等参数集，建户时引用即继承；生效前提是
    OXE 系统参数"Use profile with auto. recognition"启用，名称必须大写。
  alias_or_related: Key profile（可编程键预设，g05）；Profile 10（话务台简化配置权限档，g29 语境不同）
  tags: [concept, users, profiles]

- id: g05
  term: Key profile（键位档案）
  category: concept
  source_pages: p190-195
  source_quote: |
    "THE 'USE PROFILE WITH AUTOMATIC RECOGNITION' MUST BE SET IN ORDER TO MAKE THE KEY PROFILES
    WORK. ... TO RETRIEVE THE KEY PROFILE INFORMATION IN THE OMNIVISTA 8770, A SYNCHRONIZATION MUST
    BE LAUNCHED" (p190, p194)
  definition: |
    可编程键预设三层：set profile（机型+Profile 功能）> Progr. Keys（键位定义：Function/Content/Mnemo/
    Locked）> Profile Features（键功能关联：机型+Key Function+profile 号）；建户选 Key Profiles 自动
    配键；取回 8770 需同步。
  alias_or_related: Profile（g04）
  tags: [concept, users, keys]

- id: g06
  term: Meta profile（元档案）
  category: concept
  source_pages: p198-199, p204-207
  source_quote: |
    "Configured in the OmniVista 8770 and based on: OXE user profiles, OXE free numbers ranges ...
    OXE meta profiles are represented by the symbol in the tree structure" (p198-199)
    "The user directory number is the first available number from the free number range" (p207)
  definition: |
    8770 Users 应用再封装的建户模板：Meta profile 名 + OXE 节点 + 空闲号码段 + 设备类型 + OXE profile
    （可选）+ Key Profile（可选）；建户只填姓名即自动取段内首个空闲号并填满 OXE 属性。树中带专用图标。
  alias_or_related: Free Numbers Ranges List（OXE 侧号段，建后必须同步）
  tags: [concept, users, automation]

- id: g07
  term: Mass provisioning（批量开通）
  category: concept
  source_pages: p211-218, p246-252
  source_quote: |
    "Mass provisioning facility allows export and/or import users ... Optimized import for Rainbow
    users creation on ALE cloud ... Generation of template for mass users creation" (p213)
    "Mass provisioning file generated from thick client cannot be used in WebAdmin and vice-et-versa" (p250)
  definition: |
    经导出/导入文本文件（.txt/.csv）批量建户/改户/删户的机制：模板导出（XXXX=必填、NULL=自动）、
    action 语义（thick client 用 ADD/MODIFY/DELETE，WBM 用 +/-/#）；导出可计划、导入即时或计划；
    thick client 与 WBM 文件互不通用。
  alias_or_related: Rainbow users mass provisioning（OXE 数据导出→Rainbow 云建户→按 email+号码挂设备的
    三步流，p218）
  tags: [concept, users, mass-provisioning]

- id: g08
  term: Correlated / Uncorrelated alarm（相关/非相关告警）
  category: concept
  source_pages: p277, p327, p361
  source_quote: |
    "Correlated alarm: When the end of the problem can be detected by the PCX, the alarm is
    referred to as correlated ... Uncorrelated alarm: Correction must be performed manually" (p277)
    "Only correlative alarms are displayed" (p327)
  definition: |
    告警两大类：PCX 能检测问题结束的相关告警（自动清除，Topology 唯一显示类型）；不能检测的非相关
    告警（人工清除）。OXE R11.2 起 IP 话机状态事件 #386 不再可相关。
  alias_or_related: SNMP Filter 的 Correlation 条件（Equal/Different True/False）
  tags: [concept, alarms]

- id: g09
  term: Event（事件）
  category: concept
  source_pages: p275, p127
  source_quote: |
    "Events tree: Generated by the OmniPCX Enterprise. Gives information about object configuration
    and has no severity. Type of event: Object creation / Object deletion / Object modification" (p275)
  definition: |
    OXE 产生的对象级变更通知（创建/删除/修改），无严重级、不进告警处置流程；8770 收到事件即实时更新
    配置数据，是"实时同步"的载体；Alarms 应用 Event 页查看。
  alias_or_related: incident（OXE 侧故障事件号，如 2042/1125，进告警流程）
  tags: [concept, alarms, events]

- id: g10
  term: Job / Task / jobset（任务模型）
  category: concept
  source_pages: p463-464, p487
  source_quote: |
    "Job: Entity including one or more tasks performed simultaneously ... Task: Executable
    operation. OmniVista 8770 internal operation. External application" (p463)
    "When you add another Job, this one is called jobset. But it's only during its creation." (p487)
  definition: |
    Scheduler 任务模型：Task=可执行操作（内部或外部应用）；Job=同时执行的任务集合（Idle/Waiting/
    Running 三态）；Simple job=单任务 job、Synchronized task=挂入已有 job 的任务；新建子 job 的临时名
    jobset 刷新后变 Job；预定义 job（Daily/Weekly/8770 Data Backup/RTU Scheduled Reports）承担日常维护。
  alias_or_related: Purge job（用户组装的清除链，p494-501）
  tags: [concept, scheduler]

- id: g11
  term: RestoreContext.ini
  category: concept
  source_pages: p79, p509-510, p512
  source_quote: |
    "The file C:\8770\Restorecontext.ini contains the installation settings configured via the
    InstallShield wizard. It also gives a history of the upgrade performed" (p79)
    "Comparison of RestoreContext.ini files (current and the one from the backup) will exclude the
    hostname svNMCName and domain svDomain entries." (p512)
  definition: |
    安装设置存档与恢复校验文件：目录路径、端口（Apache 80/HTTPS 8443/LDAP 389/LDAPS 636/Wildfly
    8080）、计算机名（svNMCName）、DNS 后缀（svDomain）、成本中心开关（bCostCenter）、版本（nmcVersion/
    nmcInitialVersion）；恢复时与备份内副本比对（rehosting 时排除主机名与域两项），nmcVersion 决定
    备份可还原的版本。
  alias_or_related: Rehosting（g12）
  tags: [concept, backup, installation]

- id: g12
  term: Rehosting（换址恢复）
  category: concept
  source_pages: p509, p511-513
  source_quote: |
    "Restore the saved data using 8770 Maintenance application. Select the Restore databases with
    rehosting operation. After the database restoration, scripts are invoked to update the
    configuration of the 8770 server" (p511)
  definition: |
    带配置恢复的换址机制：改 IP 场景=备份→改 IP→rehosting 恢复（脚本更新配置）；改 FQDN 同机=卸载→
    改 FQDN→同参数重装；换机=同参数安装→rehosting 恢复。服务器设置（计算机名/DNS 后缀/IP）的统一
    后悔通道。
  alias_or_related: Restore with rehosting（Maintenance 应用操作名）
  tags: [concept, backup, migration]

- id: g13
  term: Access Profile（OXE 配置访问档案）
  category: concept
  source_pages: p377, p399-401
  source_quote: |
    "11 Access Profiles are available ... 0 YES Gives access to all objects, all attributes, and all
    actions ... 4 to 9 NO ... Rights available: Nothing / Read / Read-Write / All" (p399-400)
  definition: |
    控制账户在 Configuration 界面能看到/能动哪些 OXE 对象的档案：11 个编号（0 全量、1 expert、2 usual、
    3 用户管理、4-9 自定义、10 话务台简化配置）；每对象类四级权限+属性显隐+Actions 授权；全体 OXE
    共用一套，改后须删客户端本地 MIB 重载。
  alias_or_related: Simplified Configuration group（默认持 Profile 10 的预定义组）
  tags: [concept, security, access-profile]

- id: g14
  term: Management domain / System domain（管理域/系统域）
  category: concept
  source_pages: p14, p35, p377, p381
  source_quote: |
    "A domain gathers a set of PCX objects manageable by a 8770 administrator. By default, all PCX
    objects belong to system domain 0 ... For each 8770 administrator, it's possible to define
    access rights to a system domains (255 system domain max)" (p377-381)
  definition: |
    OXE 对象的分区管理单位：域=可管理的一组对象（用户/用户键/数据终端/话务组/PIN/电话簿/编号计划）；
    默认全部对象属系统域 0，最多 255 个系统域，可按域给管理员授权（如 ADMINNMC 全域全权、ALAN 域 0
    只读）。
  alias_or_related: Domains for management（WBM 的对应选项，需许可）
  tags: [concept, security, domains]

- id: g15
  term: MIB / Object Model（对象模型）
  category: concept
  source_pages: p139-140, p155, p402
  source_quote: |
    "Data exchange is based on a detailed description of the managed objects: the MIB (Management
    Information Base), also called 'Object Model'" (p139)
    "Download of the MIB at first connection and stored locally on Browser in a GMI/JSON format" (p155)
  definition: |
    OXE 管理对象的描述库：8770 与 OXE 间 CMISE 数据交换的基础；WBM 首连时以 GMI/JSON 存浏览器本地，
    thick client 存本机（Object Model Save 管理）；Access Profile 变更后须删本地 MIB 重载才生效。
  alias_or_related: Local backup（MIB/XML Schema 本地缓存，提升客户端请求性能，p140）
  tags: [concept, configuration, mib]

- id: g16
  term: PCX
  category: concept
  source_pages: p18, p114, p657
  source_quote: |
    "Declare and configure communication server networks from a central point ... Retrieve all
    technical data from the PCX" (p18, p114)
    "FTP password Enter the FTP password of the NMC account ... This account is used to retrieve the
    metering tickets from the OXO Connect" (p657)
  definition: |
    书中对被管通信服务器（Private eXchange？书中未展开全称）的通用称谓：OXE、OXO Connect、OpenTouch
    在 8770 语境下统称 PCX；节点声明、计费票提取、维护账号（mtcl）等均挂在 PCX 概念下。
  alias_or_related: PCX Administration & Supervision（Network 套件的功能分区名，p10）
  tags: [concept, pbx]

- id: g17
  term: MAO（OXE 管理操作体系）
  category: concept
  source_pages: p412, p427-428
  source_quote: |
    "1. Deactivate MAO (mao off) 2. Launch multitool SECURITY_ACCESS ... Perform some mao action
    (create, modify, delete) on your OXE from the Configuration application" (p412, p428)
    "/usr3/mao/mao_hist This file contains the list of mao action performed on the OXE" (p428)
  definition: |
    OXE 侧配置管理操作体系（书中未展开全称）：Configuration 界面对 OXE 的增删改即 mao action，审计
    落 /usr3/mao/ 三日志（mao_log_hist 连接、mao_hist 操作、mao_hdet 明细）；OXE 侧安全重置前需
    mao off 暂停该体系。
  alias_or_related: mao_hdet→list_fhdet.txt（rsh 转换的明细文本）
  tags: [concept, audit, oxe]

- id: g18
  term: MCS (Managed Communications Services)
  category: concept
  source_pages: p13
  source_quote: |
    "MCS* customers -> outsourced and remote OAMP performed by a service provider. * MCS : Managed
    Communications Services" (p13)
  definition: |
    托管通信服务客户形态：8770 的 OAMP（运行/管理/维护）外包给服务商远程执行；Administration 应用中
    有 MCS customers 列表配置。书中唯一一次展开的缩写。
  alias_or_related: OAMP（书中未展开全称）
  tags: [concept, managed-services]

# ── 二、角色/账号 (role) ──

- id: g19
  term: AdminNmc
  category: role
  source_pages: p74, p372, p390
  source_quote: |
    "The Application administrator login is AdminNmc. ... AdminNmc: Default access to connect to the
    server, Full administration access, AdminNmc member in all application with all rights" (p74, p372)
    "If AdminNmc account is locked, it must be unlocked using ToolsOmniVista.exe." (p390)
  definition: |
    8770 应用管理员主账号：安装时创建、初始与 directory manager 同密、首登强制改密；全应用全权的
    预定义账户；单登录限制与普通锁定流程对其不适用（锁定走 ToolsOmniVista 选项 4 或 WBM 邮件重置）。
  alias_or_related: Normal Administrators group（单登录豁免组）
  tags: [role, administrator]

- id: g20
  term: Alcatel4059
  category: role
  source_pages: p372
  source_quote: |
    "Alcatel4059: Dedicated for the attendant, Access to the directory" (p372)
  definition: |
    预定义账户：话务台专用，仅目录访问权。预定义账户四件套之一（另见 g19/g21/g22）。
  alias_or_related: Attendant（话务台）
  tags: [role, attendant]

- id: g21
  term: MSAD8770Admin
  category: role
  source_pages: p77, p372
  source_quote: |
    "MSAD8770Admin (used by the Active Directory Server to access and manage users in OmniVista
    8770 database) ... Dedicated for MSAD synchronization feature" (p77, p372)
  definition: |
    预定义服务账户：Microsoft Active Directory 同步专用——AD 侧用它访问并管理 8770 数据库中的用户，
    支撑 Directory 的 AD 集成选项。
  alias_or_related: MSAD 同步（Directory 应用附加选项，p32）
  tags: [role, service-account, ad]

- id: g22
  term: Thirdparty8770Admin
  category: role
  source_pages: p77, p180, p372
  source_quote: |
    "Thirdparty8770Admin (used by the API 8770 to provision users from a thirds party application)
    ... Dedicated for interaction with an external API development" (p77, p372)
  definition: |
    预定义服务账户：第三方应用经 8770 API（SOAP+SDK）开通用户时使用；API 体系基于 SOAP 协议，SDK 经
    DSPP（Developer and Solution Partner Program）获取。
  alias_or_related: API Provisioning（许可选项，g34）
  tags: [role, service-account, api]

- id: g23
  term: directory manager（cn=directory manager）
  category: role
  source_pages: p74, p77, p535, p315
  source_quote: |
    "The Directory manager login is directory manager. Fill in the directory manager password ...
    Do not modify the directory manager login or installation may fail." (p74, p77)
    "Please enter password of cn=directory manager : *********" (p315)
  definition: |
    LDAP 目录管理器账号：安装时设定密码（≥8 字符，实验口径 superuser），登录名固定不可改；ToolsOmniVista、
    DirManag 等底层工具的认证主体；密码只能经 ToolsOmniVista 选项 1→1→2 修改。
  alias_or_related: Admin（LDAP 目录管理员，与四个账户同初始密）
  tags: [role, ldap]

- id: g24
  term: dba
  category: role
  source_pages: p77, p529, p536
  source_quote: |
    "The 'Database administrator login' is dba (read only). The password is sql. It can be modified
    by the ToolsOmniVista.exe application." (p77)
    "HeidiSQL administrator: Consult SQL data from MariaDB. Login: dba, Password: sql (default)" (p529)
  definition: |
    MariaDB 数据库只读管理员：默认密码 sql（实验口径），HeidiSQL 直查数据库用；改密走 ToolsOmniVista。
    只读定位意味着数据变更不能靠它。
  alias_or_related: HeidiSQL / MariaDB（g40/g41）
  tags: [role, database]

- id: g25
  term: installer（OXO 安装员账户）
  category: role
  source_pages: p649, p657, p663
  source_quote: |
    "The default Installer password is pbxk1064. It supposed that a cold reset with password
    reinitialazation of the OXO Connect has been applied previously. Otherwise, you must enter the
    Installer password you customized during the first OXO Connect installation (i.e. Alcatel1)" (p649)
    "Omc config password Enter the Installer password used to connect the OMC management tool" (p657)
  definition: |
    OXO Connect 的安装员级账户：OMC 首连与 8770 声明（Omc config password）的凭据；cold reset 后默认
    密码 pbxk1064（实验口径），首装时自定义（实验 Alcatel1）；OXO R10 起连接时强制改全部账户密码。
  alias_or_related: OMC（g39）
  tags: [role, oxo, installer]

- id: g26
  term: mtcl / adfexc / swinst（OXE 三大系统账户）
  category: role
  source_pages: p123, p573-574, p589
  source_quote: |
    "Username maintenance Enter the mtcl account name ... This is the OXE FTP login and password used
    for data retrieval." (p123, p123 处 adfexc)
    "Telnet or SSH to the OXE (login = mtcl, password = mtcl by default) ... FTP or SFTP (login =
    adfexc, password = adfexc by default) ... swinst password (SoftInst by default) — Mechanism until
    OXE N2" (p573)
  definition: |
    OXE 侧三个功能账户：mtcl=维护会话（telnet/SSH，bck 备份命令执行者）；adfexc=FTP/SFTP 数据提取
    （8770 声明的 FTP 账号、备份文件取回）；swinst=软件安装/备份恢复会话（bck 授权密码、恢复菜单执行
    主体）。N2 及以前有默认密码（mtcl/adfexc/SoftInst），N3 起必须已自定义。
  alias_or_related: OXE N2/N3 代际（g 系 version-trap）
  tags: [role, oxe, maintenance]

- id: g27
  term: ADM8770
  category: role
  source_pages: p669, p680, p696
  source_quote: |
    "Creation of a user account named ADM8770 with access rights on folders previously created ...
    Username Enter account in uppercase preceded with the following characters .\ (i.e. .\ADM8770)" (p669, p696)
  definition: |
    网络驱动器场景专用 Windows 账号：远程服务器（AD）与 8770 服务器（本地）同名同密；入
    Administrators 组、移出 Users 组、赋五项用户权利；作为 ExecdEx（报表）与 SaveRestore（备份恢复）
    两服务的运行账号（Nt account=.\ADM8770）。
  alias_or_related: ExecdEx / SaveRestore 服务（g56）
  tags: [role, windows, service-account]

- id: g28
  term: 预定义访问组（Accountants / Network experts / Simplified Configuration 等）
  category: role
  source_pages: p371, p386, p399, p404
  source_quote: |
    "Predefined access groups: Access to applications according to user role. Accounting manager,
    PCX administrator, etc. ... Add an account as a member of the group to inherit from the group
    access rights. An account can be a member of different groups" (p371)
    "Add Expert1 and Expert2 into the Network experts predefined group" (p404)
    "The Simplified Configuration group is assigned Profile 10" (p399)
  definition: |
    Security 应用按角色预置的权限组：成员继承组权限、多组权限取最高；书中点名 Accountants（计费）、
    Network experts（OXE 配置界面准入）、Simplified Configuration（持 Access Profile 10 的话务台简化
    配置）；组描述在嵌入式 Administrator Manual 第 15 章 Access Groups。
  alias_or_related: Customized group（自建组，g13/g14 联动）
  tags: [role, security, groups]

# ── 三、许可/订阅 (subscription) ──

- id: g29
  term: Start Pack PPU
  category: subscription
  source_pages: p598
  source_quote: |
    "Start Pack PPU: Included functionalities: Alarms, Metering and tracking, Unified management,
    Configuration application (not visible but included), Audit (not visible but included). Optional
    functionalities: Active Directory Integration, Manage My Phone, API Provisioning, Topology, SNMP
    Proxy" (p598)
  definition: |
    8770 基础许可包（PPU 计价）：含告警、计量跟踪、统一管理，Configuration 与 Audit 内含但界面不显
    示；可选加 AD 集成、Manage My Phone、API Provisioning、Topology、SNMP Proxy。
  alias_or_related: Full Pack PPU（g30）
  tags: [subscription, license, pack]

- id: g30
  term: Full Pack PPU
  category: subscription
  source_pages: p599
  source_quote: |
    "Full Pack PPU: Included the Start Pack PPU, with Performance, Company Directory. Options
    whatever selected pack: Ticket Collector, Security, Multi Domain (if Company Directory is
    selected)" (p599)
  definition: |
    完整许可包：Start Pack 全量 + Performance（VoIP 性能/话务分析）+ Company Directory（企业目录树）；
    任一包型均可加购 Ticket Collector、Security、Multi Domain（后者依赖 Company Directory）。
  alias_or_related: ACTIS quotation（出证体系）
  tags: [subscription, license, pack]

- id: g31
  term: 8770Handle / Declaration node lock（申报节点锁）
  category: subscription
  source_pages: p601, p604, p613
  source_quote: |
    "8770Handle: reference to the declaration node ... (1) Read 8770 handle (2) Search OXE having
    the 8770Handle in its OPS file (3) Tag the OXE found (4) Check periodically the declaration node" (p601, p604)
    "Handle 4760 = 123456AB" (p613)
  definition: |
    许可控制方法 #1：许可文件 [OXE AND ICE] 段的 8770Handle 与指定 OXE OPS 文件中的 Handle 比对
    （OXE 侧 spadmin 命令显示，如 Handle 4760=123456AB），License Server 周期核验申报节点在位。
  alias_or_related: spadmin（OXE 锁查询命令）；MAC/IP/ProductID/UUID 绑定（许可控制方法 #2）
  tags: [subscription, license, lock]

- id: g32
  term: Security key（许可安全档位 0-5）
  category: subscription
  source_pages: p603
  source_quote: |
    "Security key is a level of security based on 3 parameters: Secure IP connections ... Use of
    external authentication mechanism (e.g. Radius) ... Use of Public Key (not available anymore
    from release R5.0). Numeric values: 0: No security flows and no PKI ... 5: Security flows and
    full PKI feature" (p603)
  definition: |
    许可 [Modules] 段的特殊键：组合"加密流（部分 8770-OXE 流量）+外部认证（Radius）+PKI"三要素分
    0-5 档（偶数无加密流、奇数有；2-3 基础 PKI/EJBCA 简包装、4-5 完整 PKI/集成证书部署）；PKI 从
    R5.0 起不再可用。键值即 Security 应用的档位依据。
  alias_or_related: Radius Server（Administration 附加选项）
  tags: [subscription, license, security]

- id: g33
  term: Restricted mode（许可受限模式）
  category: subscription
  source_pages: p606
  source_quote: |
    "Alarms generated when the number of users is closed to the limit. When some license thresholds
    are exceeded, client runs in restricted mode: Only Directory and Configuration are accessible" (p606)
  definition: |
    用户数逼近上限产生告警；超限后 8770 客户端只剩 Directory 与 Configuration 两应用（用于删户回到
    限内），服务器不停机防数据丢失。许可用量可查 NMCLicServer_1.log 的百分比行。
  alias_or_related: NMCLicServer_1.log（g57）
  tags: [subscription, license, threshold]

- id: g34
  term: Unified Management / Company Directory license（WBM 解锁许可）
  category: subscription
  source_pages: p35, p227, p598
  source_quote: |
    "8770 WBM USERS APPLICATION ... Available with Unified Management license ... Management of the
    Company Directory tree structure (submitted to Company Directory license)" (p35)
  definition: |
    WBM Users 应用的解锁许可为 Unified Management；公司目录树管理另需 Company Directory 许可（亦为
    Full Pack 组成）。许可选项族还包括 Manage My Phone、API Provisioning、Topology、SNMP Proxy、
    Ticket Collector、Security、Multi Domain。
  alias_or_related: MMP 许可口径 20 OXE/100 并发（p268）
  tags: [subscription, license, wbm]

- id: g35
  term: OXO Connect accounting tickets（OXO 计费票锁）
  category: subscription
  source_pages: p608
  source_quote: |
    "Accounting: Yes / No. If yes: Default: no ticket. Possibility to increase the number of tickets
    by steps of 1000. 30 000 tickets maximum" (p608)
  definition: |
    OXO Connect 侧唯一许可锁：计费票数默认 0（开了计费也无数据），按 1000 步进扩容、上限 30000；
    告警与 OMC 无锁。对应 8770 许可 [Modules] 的 OXOVoIPTickets 键。
  alias_or_related: OXOVoIPTickets（p603 键名）
  tags: [subscription, license, oxo]

# ── 四、产品/工具 (product) ──

- id: g36
  term: OmniPCX Enterprise (OXE)
  category: product
  source_pages: p9, p109, p139
  source_quote: |
    "OmniPCX Enterprise OXE R12.2 to R12.4 ... CMIP/CMISE protocol used to exchange data between
    OmniVista 8770 Server and OmniPCX Enterprise" (p9, p139)
  definition: |
    ALE 大型企业话务服务器：8770 管理的主对象——CMIP/CMISE 配置、Telnet/SSH 维护、mao 审计、bck 备份；
    代次（Purple N1-N5）决定 8770 兼容版本。
  alias_or_related: OmniPCX 4400（8770 声明菜单中的历史名，Create > OmniPCX 4400/Enterprise）
  tags: [product, pbx]

- id: g37
  term: OXO Connect / OCE / OmniPCX Office
  category: product
  source_pages: p9, p19-20, p640, p653
  source_quote: |
    "OXO Connect / OCE R4.0 ... R5.2 to R6.2" (p9)
    "OXO Connect configuration is carried out by means of the Windows OMC (Office Management
    Console) application. Reminder: all the OXO configuration is done from the OMC application" (p139)
  definition: |
    ALE 中小企业话务系统（OCE=OXO Connect Evolution）：8770 经 OMC 代理纳管（配置本体在 OMC）；8770
    侧声明菜单名 OmniPCX Office；8770 提供监督、计费票提取、告警接收与 VoIP 报告。
  alias_or_related: OMC（g39）；OmniPCX Office（p653 亦作版本表述 "From OmniPCX Office R10"）
  tags: [product, pbx]

- id: g38
  term: OpenTouch (OT / OTMC)
  category: product
  source_pages: p9, p139, p114
  source_quote: |
    "OpenTouch BE / MS / MC OT R2.4 to R2.6.1" (p9)
    "The OpenTouch management for configuration happens through XML Web Services" (p139)
  definition: |
    ALE 协作话务平台（BE/MS/MC 三形态）：8770 经 XML Web Services 管理配置；同步时 Global 选项连带
    关联 OpenTouch；拓扑图支持 OT/OTMC 架构图形显示。
  alias_or_related: OTMC（Topology 中的 OTMC 节点显示，p330）
  tags: [product, pbx]

- id: g39
  term: OMC (Office Management Console)
  category: product
  source_pages: p20, p139, p644-648
  source_quote: |
    "OMC application must be installed on the 8770 server and on each 8770 client" (p20)
    "OMC: Office Management Console ... For a first installation, you must install Microsoft .NET
    Framework pack." (p139, p644)
  definition: |
    OXO Connect 的 Windows 配置工具（书中全称唯一展开处）：OXO 的全部配置在 OMC 完成；8770 服务器与
    每个 8770 客户端都需安装（8770 以在线/离线方式代开 OMC 会话）；安装需 .NET Framework、经 BP 网站
    分发。
  alias_or_related: Online/Offline mode（8770 内代开 OMC 会话，p663-665）
  tags: [product, oxo, tool]

- id: g40
  term: MariaDB / MySQL8770
  category: product
  source_pages: p7, p60, p529-531, p541
  source_quote: |
    "MariaDB (SQL) ... MariaDB Server & ODBC Driver Installation Process Step #1" (p7, p60)
    "Database location: Located in 8770\data\data ... .frm -> table definition, .ibd -> table data,
    .TRN -> trigger name, .TRG -> trigger parameters file" (p530)
  definition: |
    8770 的 SQL 数据库引擎：承载计费/VoIP/话务/告警/审计数据与报告（备份内容之一）；Windows 服务名
    MySQL8770（Automatic 启动）；数据文件在 8770\data\data；经 HeidiSQL（dba/sql，3306）直查。
  alias_or_related: HeidiSQL（g43）
  tags: [product, database]

- id: g41
  term: Oracle DSEE（SunONE）/ Directory Server
  category: product
  source_pages: p7, p32, p61, p528
  source_quote: |
    "Directory application: LDAP v3 directory ... Directory data import/export in LDIF ... License
    & data collection LDAP Oracle DSEE Directory Server" (p32, p61)
  definition: |
    8770 内嵌的 LDAP v3 目录服务器（安装目录 C:\8770\SunONE）：存公司目录/用户/设备目录；389/636
    端口；支持 LDIF 导入导出、AD 同步、双 8770 间目录复制；Windows 服务 Oracle Directory Server EE
    与控制中心（admin 登录）。
  alias_or_related: DirManag（g44）；LDIF（预定义 job 恢复介质）
  tags: [product, ldap, directory]

- id: g42
  term: Apache / Wildfly
  category: product
  source_pages: p7, p61, p542, p79
  source_quote: |
    "8770 Applications Open JRE embedded Apache/Wildfly servers ... Apache: HTTP Web server ...
    Wildfly: Application server" (p61, p542)
  definition: |
    8770 内嵌的两个服务端：Apache（HTTP Web 服务，端口 80，日志 Apache2\logs）与 Wildfly（应用服务
    器，端口 8080，TLS 切换时同步改其配置）；均由 NMC Service Manager 拉起。
  alias_or_related: Open JRE（内嵌 Java 运行时）
  tags: [product, server]

- id: g43
  term: HeidiSQL
  category: product
  source_pages: p529-531, p536-538
  source_quote: |
    "HeidiSQL administrator: Consult SQL data from MariaDB. Login: dba. Password: sql (default).
    Use ToolsOmniVista.exe to change it" (p529)
  definition: |
    随 MariaDB 10.5 提供的 SQL 图形客户端：Start > MariaDB 10.5 > HeidiSQL，TCP 127.0.0.1:3306、
    dba/sql 直查 nmc5 库（Query 页 SQL，表名自动补全）。
  alias_or_related: dba（g24）
  tags: [product, tool, sql]

- id: g44
  term: DirManag (Directory Management)
  category: product
  source_pages: p526-527, p535
  source_quote: |
    "DirManag LDAP browser: Consult and modify the LDAP data. Login: AdminNmc or directory manager ...
    Port number 389 (LDAPS is not supported)" (p526, p535)
  definition: |
    c:\8770\bin 下的 LDAP 树浏览/修改工具：389 明文口（不支持 LDAPS）、directory manager 或 adminnmc
    登录、改后 Ctrl+S 保存。
  alias_or_related: Directory Server Control Center（另一 LDAP 入口，admin 登录，p528）
  tags: [product, tool, ldap]

- id: g45
  term: ToolsOmniVista.exe
  category: product
  source_pages: p315, p389-396, p414, p529, p77
  source_quote: |
    "TOOLSOMNIVISTA ... 1 : Security / 2 : Certificate Management / 3 : Accounting Organization
    Update / 4 : SNMP / 5 : Management Domain / 0 : Quit" (p389)
  definition: |
    C:\8770\bin 下的服务器底层维护工具（命令行菜单）：密码更新（DB/LDAP/AdminNmc/管理员/复制管理器）、
    最低 SSL/TLS 版本、3DES 开关、SNMP 代理启停、证书管理、计费组织更新、管理域完整性检查；运行需停
    8770 服务，须按 0 正常退出。
  alias_or_related: PatchInstaller.exe（补丁安装，同目录族）；8770 Diagnostic（另一工具）
  tags: [product, tool, maintenance]

- id: g46
  term: 8770 Diagnostic
  category: product
  source_pages: p523-525, p533-534
  source_quote: |
    "8770 Diagnostic collects information and provides: An html file ... A compressed file (.zip)
    that can be transmitted to Alcatel-Lucent Enterprise support for diagnostic" (p523)
  definition: |
    服务器诊断采集工具（Start > OmniVista 8770 > Tools）：收集日志/RestoreContext.ini/服务状态/许可/
    hosts/计划任务信息，产出 C:\TS 下 HTML 与 zip（文件名 NMS_周几+月日）；交互/非交互两模式（非交互
    只需 LDAP 端口 389 + SQL 密码）。
  alias_or_related: SR 支持（zip 交 ALE 支持开诊断）
  tags: [product, tool, diagnostic]

- id: g47
  term: MindTerm
  category: product
  source_pages: p124, p133-134
  source_quote: |
    "The host name is used by the MindTerm application to create the SSH public key on the OmniVista
    8770 server for connection data on the OXE." (p124)
    "The public key is stored in the folder Users\Administrators\AppData\Roaming\MindTerm\hostkeys." (p134)
  definition: |
    8770 内嵌的 Java SSH/SFTP 客户端：Configuration 应用内 Connect 到 OXE 时承载加密会话；首次连接
    生成公钥（存 MindTerm\hostkeys）并可开 SFTP 文件传输（Plugins > SFTP File Transfer）。
  alias_or_related: SFTP（OXE 备份取回通道之一）
  tags: [product, ssh]

- id: g48
  term: ACTIS
  category: product
  source_pages: p595, p597-600
  source_quote: |
    "1 - The Actis application generates the 8770 license file (.sw8770 extension)" (p597)
    "ACTIS quotation: Start Pack PPU ... Full Pack PPU ... Reduced price packs" (p598-600)
  definition: |
    ALE 许可报价/出证应用：生成 <offer id>.sw8770 许可文件；报价结构=Start Pack/Full Pack PPU+选项+
    运营商专用的减价包（Security[Radius/IPsec/PKI 应用]、外部计量与 VoIP 应用等）。
  alias_or_related: nmc.license（g56）
  tags: [product, licensing]

- id: g49
  term: TrapReceiver / FlexLM / IPDSP / MicroSIP（实验工具族）
  category: product
  source_pages: p45, p47-48, p313
  source_quote: |
    "TrapReceiver application for Proxy SNMP purposes" (p48)
    "FLEXLM SERVER 8770_FLEXLM flex 192.168.1.80" (p47)
    "1 IPDSP softphone 31000 ... 2 MicroSIP softphones for OXE extension users ... 1 MicroSIP
    softphone for external call tests" (p48)
  definition: |
    RLAB 实验工具集（实验口径）：TrapReceiver（Client PC 上模拟 SNMP hypervisor 收 trap）；FlexLM
    服务器（192.168.1.80，root/letacla1）供许可；IPDSP（分机 31000 软话机）；MicroSIP×3（31001/31002/
    公网测试）。仅教学环境用，生产不涉及。
  alias_or_related: RLAB POD（g56 之外的实验环境概念，p43-45）
  tags: [product, lab]

- id: g50
  term: ALES-Desktop / ALES-Mobile
  category: product
  source_pages: p241, p250
  source_quote: |
    "ALES-Desktop and ALES-Mobile tabs available once selected. Included on the 4 Devices tabs
    maximum limit" (p241)
  definition: |
    WBM 建户时的 ALE 软终端形态页签（桌面端/移动端）：选中即出现、计入每用户 4 个设备页签上限。
  alias_or_related: OTC Smartphone / OTC PC（OpenTouch Connection 移动/PC 选项页签，p243-244）
  tags: [product, softphone, wbm]

- id: g51
  term: Manage My Phone (MMP)
  category: product
  source_pages: p6, p38, p261-268
  source_quote: |
    "8770 MANAGE MY PHONE: HTML interface for end-users to manage their phone set ... Access via an
    end-user login (email address) + password ... Activate your forward, reset your password" (p38)
  definition: |
    终端用户自助门户（https://<FQDN>:8443 > MANAGE MY PHONE）：呼转/免打扰/锁机/密码码重置/IP·TDM
    话机可编程键配置；需 MMP 许可（20 OXE/100 并发）；仅法语英语；图形视图限 80X8/40X8 与 80X9/40X9。
  alias_or_related: NMC Manage My Phone（NMC 内部服务名，p542）
  tags: [product, selfcare]

# ── 五、协议/接口 (protocol) ──

- id: g52
  term: CMIP / CMISE
  category: protocol
  source_pages: p7, p110, p139, p155
  source_quote: |
    "CMIP: Common Management Information Protocol. CMISE: Common Management Information Service.
    Data exchange is based on a detailed description of the managed objects: the MIB" (p139)
    "CMISE configuration ... CMISE on the fly ... Telnet or SSH (SSH mandatory from OXE R101)" (p110)
  definition: |
    8770 与 OXE 间的配置/事件交换协议族（Common Management Information Protocol/Service，全书唯二
    展开全称处）：配置下发与告警事件都走 CMISE；WBM 配置界面同协议、MIB 以 GMI/JSON 缓存浏览器。
  alias_or_related: NMC CMISE server（内部服务，p542）
  tags: [protocol, oxe]

- id: g53
  term: LDAP / LDAPS / LDIF
  category: protocol
  source_pages: p7, p32, p73, p502, p535
  source_quote: |
    "Select the default port for LDAP (ex. 389) and LDAPS (ex. 636)." (p73)
    "Directory data import/export in LDIF. LDIF mapping tools for mass provisioning" (p32)
  definition: |
    目录访问三件套：LDAP（389，DirManag 与内部同步用）/LDAPS（636，客户端登录口）；LDIF=目录数据
    交换格式（批量导入导出、预定义 job 恢复载体）。8770 客户端与服务器的管理会话走 LDAPS。
  alias_or_related: MSAD 同步（经 MSAD8770Admin）
  tags: [protocol, directory]

- id: g54
  term: SNMP v2c / v3（含 trap 162）
  category: protocol
  source_pages: p7, p282, p313-314
  source_quote: |
    "SNMP versions: SNMP v2c & V3 versions supported ... UDP 162 ... SNMP trap ... CMISE SNMP Proxy
    Hypervisor" (p282)
    "Authentication protocol Select the SNMP authentication protocol between SHA (default) or MD5 ...
    Encryption protocol ... DES (default) or AES128" (p314)
  definition: |
    8770 对外网管协议：SNMP Proxy 把 PBX/8770 事件转 trap 发 hypervisor（UDP 162）；v2c 免认证、v3 带
    SHA/MD5 认证+DES/AES128 加密；过滤按 Correlation/Diagnostic 条件。
  alias_or_related: SNMP Hypervisor（外部网管站，实验用 TrapReceiver 模拟）
  tags: [protocol, snmp]

- id: g55
  term: Telnet / SSH / SFTP / FTP / RSH / V24
  category: protocol
  source_pages: p7, p110, p124, p427, p572-574
  source_quote: |
    "Access to the nodes via Telnet, SSH or WBM session" (p18)
    "Execution of the backup via RSH (bck command) ... FTP or SFTP (login = adfexc ...)" (p572-573)
    "Client: Telnet, SSH, V24 ... Configuration Maintenance commands" (p419)
  definition: |
    OXE 维护通道族：Telnet/SSH（命令会话，OXE R101/N3 起 SSH 强制）、SFTP/FTP（数据与备份文件传输，
    adfexc）、RSH（备份 bck 命令的执行机制、mao_hdet 转换）、V24（串口，审计架构图中与 Telnet/SSH 并列
    的客户端通道）。
  alias_or_related: MindTerm（8770 侧 SSH 实现）
  tags: [protocol, transport]

- id: g56
  term: SOAP / API Provisioning / Corba / TDS / IPSec / Radius / SMTP
  category: protocol
  source_pages: p7, p14, p180, p272, p603
  source_quote: |
    "API CONFIGURATION: Based on SOAP* protocol and API framework hosted on OmniVista 8770 ...
    SOAP = Simple Object Access Protocol, SDK = Software Deployment Kit" (p180)
    "IPSec, Corba, TDS, LDAP(S) ... Corba for alarms notification ... Radius Server" (p7, p272, p14)
  definition: |
    外围协议群：SOAP（第三方开通 API 的协议，SDK 经 DSPP 分发）；Corba（告警通知总线，ORBacus Notify
    服务）；TDS/IPSec（架构图标注的协议流，书中未展开用途）；Radius（外部认证，Security 附加选项）；
    SMTP（告警邮件/报告邮件/密码重置码通道，默认 25）。
  alias_or_related: DSPP（Developer and Solution Partner Program，SDK 分发计划）
  tags: [protocol, api]

# ── 六、路径/端口/资源 (resource) ──

- id: g57
  term: 8770 关键目录与日志文件地图
  category: resource
  source_pages: p77-79, p126-128, p289, p305, p337, p433, p502, p516, p523, p548-553, p585, p617, p658
  source_quote: |
    "C:\8770\log\ NMCSyncLdapPbx_1.log ... C:\8770\log\NMCFaultManager_1.log" (p126-127)
    "The '*.sw8770' license file will be stored in the 8770\etc folder and will be renamed
    'nmc.license'" (p77)
    "https://nms.company.com/nmclog/ — /nmclog/ is a web alias pointing to log files" (p553)
  definition: |
    全书路径汇总：安装根 C:\8770（bin 工具/data 数据/dict 字典[ user\AlarmsReporting_user.dict]/etc
    许可[nmc.license]/install 补丁[patches、Patch_Installer.log、Patch_history.ini]/log 日志/
    Restorecontext.ini）；归档 C:\8770_ARC（8770Backup[YYYYMMDDHHMMSS]、OXEBackup\网\子网\节点\时间戳、
    OXO\data\网\子网\声明节点）；专用目录 C:\8770\data\alarms\scripts（告警脚本）、
    8770\data\topology\maps（地图 1100×793）、8770\data\scheduler（DailyJob/WeeklyJob.ldif）、
    8770\Client\data\audit（计划审计导出）、C:\TS（诊断输出）；关键日志 NMCSyncLdapPbx_1.log（同步）、
    NMCFaultManager_1.log（事件告警）、NMCSnmpAgent_1.log（SNMP）、NMCLicServer_1.log（许可用量）、
    NMCScheduler_1/2.log（任务，2×5MB 滚动）、OmniVista8770_report.log（安装）；Web 别名 /nmclog/。
  alias_or_related: 客户端侧 C:\Users\<账户>\nmc5_5.2.cfg（连接配置）
  tags: [resource, paths, logs]

- id: g58
  term: 8770 端口清单
  category: resource
  source_pages: p73, p79, p102, p254, p282, p536, p603
  source_quote: |
    "svPortApache=80, svPortHttps=8443, svServerPort=389, svPortLDAPS=636, svPortWildfly=8080" (p79)
    "Port for Trap Reception Port number used for trap reception (162 for example)" (p313)
  definition: |
    端口速查：80 Apache HTTP（不可改）/8443 HTTPS（WBM、不可改）/389 LDAP/636 LDAPS/8080 Wildfly/
    3306 MariaDB（HeidiSQL）/162 SNMP trap/25 SMTP 默认（自定义端口写法 server:port）/22 SSH & 23
    telnet（OXE 侧核验用）。
  alias_or_related: RestoreContext.ini 端口键（svPort*）
  tags: [resource, ports]

- id: g59
  term: RLAB 实验环境参数表（实验口径）
  category: resource
  source_pages: p45, p47-51, p97, p621, p643, p693-695
  source_quote: |
    "OXE 8770_OXE_SETUP csa (physical) csm (main) 192.168.1.1 192.168.1.3 ... OMNIVISTA 8770 SERVER
    8770_OV8770_SRV nms 192.168.1.70" (p47)
    "MAIN@: ... 151.1.1.246" (p643)
    "Mapp on drive Y, the folder \\151.1.1.100\REPORTS_ECO ... drive Z ... \\151.1.1.100\BACKUP_ECO" (p693)
  definition: |
    实验口径参数全集（生产禁止沿用）：主网段 192.168.1.x/24（网关 .254、内部 DNS .250）——OXE csa
    192.168.1.1/csm 192.168.1.3、GD/OMS 192.168.1.13、FlexLM 192.168.1.80、Client PC 192.168.1.10/
    192.168.1.11、8770 服务器 nms 192.168.1.70；OXO 章网段 151.1.1.x——OXO 151.1.1.246、ecosystem
    151.1.1.100（2019 章 DNS）；凭据：root/mtcl/swinst=Superuser2580*、AdminNmc 初始 superuser→
    Superuser01*、FlexLM root/letacla1、OXO Operator 密码 Letacla1、installer Alcatel1、NMC FTP
    Pbxnmc12、HeidiSQL dba/sql；预建用户 31000-31002；共享映射 Y:\Z:。
  alias_or_related: Console mode / Remote Desktop Connection（POD 两种接入，p51）
  tags: [resource, lab]

- id: g60
  term: WBM (Web-Based Management) / thick client / nmclog
  category: resource
  source_pages: p6, p11, p34-38, p151, p227, p254, p553
  source_quote: |
    "8770 WBM client ... Zero footprint (light client) ... Available with Unified Management license" (p35)
    "OmniVista 8770 thick client" (p10)
  definition: |
    两个管理界面口径：thick client（OmniVista 8770 客户端，Java/Zulu 运行，全功能四套件）；WBM=基于
    Web 的轻客户端（零安装，https://<FQDN>:8443，Users/Configuration/Performance/MMP 四应用，需
    Unified Management 许可）；nmclog=日志 Web 别名（https://<FQDN>/nmclog/，管理员凭据）。
  alias_or_related: Web Directory Client（匿名目录查询入口，p6）
  tags: [resource, interface]
```

## 任务覆盖自检（task ↔ id 映射）

| task_id | 相关 glossary 条目 |
|---|---|
| task-01/02 | g01、g11、g40、g41、g42、g57、g58、g59 |
| task-03 | g60 |
| task-04 | g02、g03、g16、g52 |
| task-05 | g47、g55 |
| task-06 | g15、g52 |
| task-07 | g04、g05 |
| task-08 | g06 |
| task-09 | g07、g53 |
| task-10 | g07、g50、g60 |
| task-11 | g25、g26、g37、g39、g59 |
| task-12 | g08、g09、g16 |
| task-13 | g08、g56 |
| task-14 | g54 |
| task-15/16 | g08、g02 |
| task-17 | g13、g14、g19、g23、g28、g32 |
| task-18 | g17 |
| task-19 | g56 |
| task-20 | g10 |
| task-21 | g10、g57 |
| task-22 | g11、g12 |
| task-23 | g44、g45、g46、g43、g24 |
| task-24 | g42、g45、g57 |
| task-25 | g26、g47、g55 |
| task-26 | g29、g30、g31、g32、g33、g35、g48 |
| task-27 | g27 |
| task-28 | g01、g04、g18、g34、g38、g51 |
