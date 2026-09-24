# 术语/缩写/产品名候选 — OmniVista 8770 目录管理 (8770XTE202EN Ed40)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 52 条（六类）。STAP/DDI/COS/WBM/NMC 等缩写书中未给全称，full_name 字段如实省略，不采信外部知识。页码为 PDF PAGE 标记口径。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: Company Directory (公司目录)
  category: concept
  source_pages: p32, p62
  source_quote: |
    "Store the company directory data with its geographical locations, departments and employees ...
    LDAP v3 directory • Data synchronization between the company directory and the communication servers" (p32)
    "The Company Directory takes into account the organization with its geographical locations,
    departments, offices and employees" (p62)
  definition: |
    8770 的核心数据资产：LDAP v3 目录，按地理/部门/员工存组织数据，与通信服务器同步，可经 ALE 客户端与标准
    LDAP v3 客户端访问，支持 LDIF 导入导出、AD 同步、双机复制。全书的操作对象。
  alias_or_related: Directory application（管理它的应用）；o=directoryroot 为其 LDAP 根
  tags: [concept, directory, ldap]

- id: g02
  term: Directory entry types（Organization / Termination）
  category: concept
  source_pages: p63
  source_quote: |
    "Tree structure made of Organization and Termination entries • Country • City • Company • Department
    —— Organization entries • Person • Group • Room —— Termination entries" (p63)
  definition: |
    目录条目两大类：组织类（Country/City/Company/Department）作树枝，终止类（Person/Group/Room）作叶子；
    地址簿（Address book）是独立于公司目录的组织类条目分支。
  alias_or_related: Address book（个人联系人分支，p62/179）；Room 条目可由人员转换而来（p109）
  tags: [concept, tree, entries]

- id: g03
  term: UID (User Identifier / User ID)
  full_name: User Identifier（书中展开）
  category: concept
  source_pages: p66, p74, p118-121
  source_quote: |
    "UID: First name + Last name • A UID is unique in the Company Directory" (p66)
    "User ID = first name + last name + extension. This method allows to avoid problem like homonymy" (p74)
  definition: |
    人员的唯一业务 key，目录内唯一；默认"名+姓"，可按 PCX 配置为"名+姓+分机号"防同名（只对自动创建生效）。
    Web 客户端显示的 Name 是"姓+名"。改姓名时要同步改 UID。
  alias_or_related: 与 g04 DN 构成目录寻址；uid 也是 LDAP 属性名（p67 DN 例）
  tags: [concept, identifier, uid]

- id: g04
  term: DN (Distinguished Name / Directory Name)
  full_name: Distinguished Name（书中展开，亦称 Directory Name）
  category: concept
  source_pages: p67, p436
  source_quote: |
    "Each entry is assigned a Distinguished Name (DN) or Directory Name ... uid=Duane Pitt, ou=Support dpt,
    o=Export ltd, l=Paris, c=fr, o=dgo, o=directoryroot ... TelephoneNumber=31000, Cn=TelephonicDevices,
    SubnetworkNodeNumber=101, SubnetworkNumber=1, NetworkNumber=1, o=nmc" (p67)
  definition: |
    条目在目录树中的唯一位置路径。两棵树两种模板：目录侧 uid=…,ou=…,l=…,c=…,o=…,o=directoryroot；配置侧
    TelephoneNumber=…,Cn=TelephonicDevices,…,o=nmc。LDAP 键：o=组织/c=国家/l=城市/ou=部门/uid=人。
  alias_or_related: g03 UID 是 DN 的人员级成分
  tags: [concept, dn, ldap]

- id: g05
  term: Primary link（主链接）
  category: concept
  source_pages: p69, p73-76
  source_quote: |
    "Primary link: 1 entry => 1 user, 1 user => 1 entry ... Name, first name and cost center name are
    identical • Only one primary link can be defined for each entry" (p69)
  definition: |
    人员↔OXE 用户的一对一绑定（姓名+名字+成本中心三项一致才匹配），每条目仅一条；手工建或 PCX 事件/同步自动建。
    姓名/名字修改必须经公司目录；自动创建重名即拒建告警。
  alias_or_related: 其余五类链接（g06-g09）都以主链接为根
  tags: [concept, links, primary]

- id: g06
  term: Multi-device link（多设备链接）
  category: concept
  source_pages: p69, p133-136
  source_quote: |
    "Multi-device link: 1 entry => n users, 1 user => 1 entry ... All sets of the multi-device user linked
    to the same entry in the Company directory • Automatically created after partial or complete OXE
    synchronization" (p69)
  definition: |
    一条人员条目挂多台话机（多设备用户），OXE 部分或完整同步后自动创建；也可经 Users 应用 Add a secondary set
    手工配置（实验 31105 IPDSP 挂 Pierre Williams）。
  alias_or_related: 与 g07 Secondary link 基数相同但来源与语义不同
  tags: [concept, links, multi-device]

- id: g07
  term: Secondary link（副链接）
  category: concept
  source_pages: p70, p128-130
  source_quote: |
    "Secondary link: 1 entry => n users, 1 user => 1 entry ... Allow an entry to be associated to a
    telephone extension with a different name (like DECT) • Cost centers are identical / name and first
    name are different" (p70)
  definition: |
    手工建的"一人多机"扩展（典型 DECT 副机）：异名同成本中心；建链瞬间副机成本中心被主链接 CC 覆盖（继承）。
  alias_or_related: Settings links… > Secondary link 页签
  tags: [concept, links, secondary, dect]

- id: g08
  term: Fax link / Miscellaneous link（传真链接/杂项链接）
  category: concept
  source_pages: p70
  source_quote: |
    "Fax link: 1 entry => n user , 1 user => n entries • Allows one or several entries to be associated to
    a fax set • Cost centers are different ... Miscellaneous link: 1 entry => n users, 1 user => 1 entry •
    Allows an entry to be associated to another type of set/extension (data terminal, modem)" (p70)
  definition: |
    传真链接 n:n（传真机可多人共享，成本中心互不影响，传真号从 PCX 取回）；杂项链一条目挂数据终端/Modem 类
    非话音终端（异名同成本中心，CC 双向同步）。
  alias_or_related: 均为手工创建（p79）
  tags: [concept, links, fax, misc]

- id: g09
  term: Additional resources link（附加资源链接）
  category: concept
  source_pages: p71
  source_quote: |
    "Additional resources link: Same properties as Primary link ... Main OXE user keeps its first primary
    link with the person • Others OXE users' links placed on Additional resources link • Useful for
    migration of OmniVista 4760 persons with multiple Primary links with OXE users" (p71)
  definition: |
    与主链接同性质（姓名+CC）但可多条的链接：迁移 OmniVista 4760 人员（一人多主链）时，第一个 OXE 用户保留
    主链接、其余落到附加资源链。同步后自动或手工建。Users 应用不可见（主链接可见）。
  alias_or_related: 4760 迁移专用语义
  tags: [concept, links, migration]

- id: g10
  term: Automatic creation（自动创建）
  category: concept
  source_pages: p74-76, p99, p105-109
  source_quote: |
    "Directory entry automatically created in a specified location after the creation of PCX items • The
    person is linked to the PCX item via a primary link" (p74)
    "Create for users (OXE) / Limit to real users (OXE) / Create for user alias (OXE)" (p105)
  definition: |
    PCX 建/改用户事件到达 8770 后，在 Location 指定路径自动建人员并建主链接。受三层控制：全局 AutomaticCreation
    三开关、节点 Automatic creation+Location、事件前提（Process directory+Permanent IP connectivity）。
  alias_or_related: 与 g10b 同步（c01）、LDIF 管道并列的三条数据供给通道
  tags: [concept, automatic-creation, event]

- id: g11
  term: Confidentiality level（保密级别）
  category: concept
  source_pages: p209, p219
  source_quote: |
    "4 levels of confidentiality available • Entries with the confidentiality level 'Green' (default value)
    • ... 'Orange' • ... 'Red' • Administration 8770 is the most confidential level" (p209)
  definition: |
    挂在人员条目上的四级保密标记（Green 默认/Orange/Red/Administration 8770），决定匿名与认证会话在 Web 目录
    能看到哪些人与哪些属性；与管理员访问级别（g12）正交。
  alias_or_related: 与 g13 personal data 联合决定可见性
  tags: [concept, confidentiality]

- id: g12
  term: Access levels（应用访问级别）
  category: concept
  source_pages: p214-215
  source_quote: |
    "No Access / Partial Read / Total Read / Partial Modification / All —— Company Directory" (p214)
    "Partial View Orange List / Partial View Red List / Total View of Red List / Partial Modification of
    Web Directory / All —— Web Directory" (p215)
  definition: |
    Security 应用按应用授予的管理员权限档：Company Directory 五档、Web Directory 五档。与条目保密级别配合
    构成"谁在哪个入口能看到/改到什么"的完整矩阵。
  alias_or_related: 授予入口 nmc > 8770Applications > Company Directory / WebDirectory
  tags: [concept, access-level, security]

- id: g13
  term: Personal data（个人数据）
  category: concept
  source_pages: p210
  source_quote: |
    "A directory entry has 2 types of attributes • Non-personal (partial) data • Personal data • Home
    Telephone • Home Address • Car License • Employee Number • Password" (p210)
  definition: |
    五种个人属性：家庭电话/家庭住址/驾照/工号/密码；其余为非个人数据。匿名只见非个人数据，认证本人可额外看
    自己的个人数据。
  alias_or_related: Password 属性指人员 UID 密码（UID 认证用，p193）
  tags: [concept, privacy, attributes]

- id: g14
  term: Cost Center（成本中心）
  category: concept
  source_pages: p110, p80, p130-131
  source_quote: |
    "Cost Center ID Select a cost center ID (i.e. 0) / Cost Center Name Enter a cost center name (i.e. MKT)" (p110)
    "If cost center does not exist, PCX refuses the modification and generates an alarm" (p80)
  definition: |
    PCX 侧定义（Specific Telephone Services > 1 > Cost Center，ID+名字）的组织/计费归属；用户 Rights 页签按 ID
    绑定。链接间继承主线：副链继承主链接 CC，传真链不动。目录侧可改但 PCX 必须已存在同名 CC。
  alias_or_related: costcentername 为 LDAP 属性名（p540 LDIF 例）
  tags: [concept, cost-center]

- id: g15
  term: DDI translator（DDI 号码翻译器）
  category: concept
  source_pages: p257, p271
  source_quote: |
    "Any DDI translator • Allows OmniVista 8770 Server to distinguish DDI number from non DDI number ... •
    Manually defined in the PCX configuration • Can be linked to: A network (8770) / A sub-network (8770) /
    A PCX (8770) / An entity (OXE) / A DDI translator (OXE)" (p257)
    "Translator > 1 > External Numbering Plan > 1 > Default DID num. translator" (p268)
  definition: |
    PCX 侧定义的 DDI↔内线映射（首个外部号/首个内部号/范围大小，实验 33210N41000/31000/500）；8770 经同步取回，
    取回哪些由 PCX 页签 DID translation usage（Default/All/List to select/List to exclude）控制。是 ISDN 号
    构造与 Click to Call 的数据源。
  alias_or_related: ISDN Prefix list per DID Translator/Entity 可按翻译器/实体配专属前缀（p272）
  tags: [concept, ddi, translator, numbering]

- id: g16
  term: ISDN number / ISDN prefix（ISDN 号/ISDN 前缀）
  category: concept
  source_pages: p256-259
  source_quote: |
    "ISDN number = ISDN prefix + Entity installation number + Set directory number" (p258)
  definition: |
    8770 为人员自动构造的外部号码：前缀+实体安装号+话机号；DDI 话机的话机号被 DDI 号替换。前缀按 PCX/子网/
    翻译器/实体分配；改 PCX 数据后必须重新同步才更新。
  alias_or_related: internationalisdnnumber 为 LDAP 属性名（p540）
  tags: [concept, isdn, formula]

- id: g17
  term: STAP
  category: concept
  source_pages: p272-273, p283
  source_quote: |
    "STAP - Off hook: automatic call is authorized when the receiver is picked up. - Authorized: automatic
    call is authorized with or without picking up the receiver of a hands-free set. - Forbidden: automatic
    call is not authorized" (p272)
  definition: |
    用户级"自动呼叫"权限，三态 Off hook/Authorized/Forbidden，Configuration 应用用户 All 页签设置；SIP 话机
    不支持。Web 目录 Define associated station（分机+密码）绑定主叫话机后，点粗体号码即按 STAP 发起呼叫。
  alias_or_related: full_name 书中未展开，不编造
  tags: [concept, stap, click-to-call]

- id: g18
  term: Prefix rule（前缀规则）
  category: concept
  source_pages: p261-263, p276-278
  source_quote: |
    "Types of prefix rules • None • Rule for external call • Rule for call between network" (p261)
  definition: |
    8770 侧拨号改写规则：None 原样拨；外部呼叫规则=匹配头+删前缀+加前缀（迷你 ARS）；网间呼叫规则=选目标
    Network/Subnetwork+加中继组前缀。建在 Network/Subnetwork/PCX 层级，经 Administration 应用绑定到拨号属性。
  alias_or_related: PCX 自身的 ARS 与之独立；PCX 有 ARS 时 8770 单规则加 0 即可（p284）
  tags: [concept, prefix-rule, routing]

- id: g19
  term: Domain for management（管理域）
  category: concept
  source_pages: p429, p437-438
  source_quote: |
    "Possibility to split organization in several parts and manage them independently" (p429)
    "A domain name • ServicesDomain • Set of company directory levels defining the domain scope ... List of
    (local) admins having rights in the domain" (p438)
  definition: |
    域=名字+一组公司目录 DN 级别+本地管理员名单；可嵌套可多父；决定本地管理员的可见性与管理边界。需
    Domain Management+Directory 双许可，功能默认关闭需在 Security 应用激活。
  alias_or_related: 三用例：多站点/OXE 多租户 MCS/云端多公司（p430-432）
  tags: [concept, domains, delegation]

- id: g20
  term: Customized view（定制视图）
  category: concept
  source_pages: p446-448, p483-486
  source_quote: |
    "Selected settings displayed during user creation process handled by an administrator account •
    Predefined views available to ease user creation • Custom views to select the user settings to be set
    up" (p446)
  definition: |
    用户开户界面的字段显示模板：预定义视图（如 Default View/OXE User view）+ 自定义视图（基于预定义关字段，
    如 RennesView）；按管理员账户绑定，目的是简化本地管理员开户。Web 目录客户端的"用户参数"是另一层同名概念
    （p322），注意语境。
  alias_or_related: 与 Delegation 配合构成"减负开户"组合（c15）
  tags: [concept, customized-view, provisioning]

- id: g21
  term: Strict view（严格视图参数）
  category: concept
  source_pages: p454
  source_quote: |
    "Strict view parameter disabled (by default) • Person search can retrieve persons from domain D but
    also from parent domain(s) • Strict view parameter enabled • Person search can retrieve persons but
    strictly from domain D"
  definition: |
    域内人员经 Web 目录检索的范围开关：关=可查本域+父域；开=严格本域。默认关。
  alias_or_related: 域场景下 Web 目录匿名查询被禁（p453）
  tags: [concept, strict-view, search]

- id: g22
  term: Replica（Master replica / Consumer replica）
  category: concept
  source_pages: p504-505
  source_quote: |
    "Master Replica • It is a read-write database that contains a master copy of the directory data ...
    Consumer Replica • It is a read-only database that contains a copy of the information held in the
    master replica" (p505)
  definition: |
    参与复制的 LDAP 分支副本：Master 可读写（供体，ID 手工 1-65534）；Consumer 只读（消费者，ID 固定 65535，
    写经 referral 转主）。每台 8770 最多 5 个副本，1 主最多 4 从。地址簿不可复制。
  alias_or_related: 与 g23 Referral、g24 Replication Agreement、Attribute set 构成复制四件套
  tags: [concept, replication, replica]

- id: g23
  term: Referral（写重定向）
  category: concept
  source_pages: p505-507
  source_quote: |
    "Referral • It is a mechanism for redirection between directory servers ... refers write requests to
    the master replica via a referral ... all updates performed in the consumer replica are redirected to
    the Master replica" (p505-507)
  definition: |
    Consumer 上的写操作自动转给 Master 执行的机制；但管理上强烈建议只在 Master 改——Consumer 本地改动在复制后
    消失（原书大写警告）。
  alias_or_related: 原书警示见 counter-example n36
  tags: [concept, referral, replication]

- id: g24
  term: Replication Agreement / Attribute set（复制协议/属性集）
  category: concept
  source_pages: p506, p511, p527-529
  source_quote: |
    "Replication Agreement • It is set of parameters defined in master server to configure and control the
    updates to the slave server" (p506)
    "Attribute Set is a group of attributes whose values can be replicated from the Master to the Slave" (p512)
    "Attribute set cannot be modified after the creation of the replication agreement." (p529)
  definition: |
    主服务器上的协议参数集：主副本配置/属性集/从机 Host:Port（LDAPS 不支持）/复制管理器密码/初始化与调度。
    属性集定义可复制属性组；建协议后不可改，要改只能删协议重建或改后 Initialize 全量。
  alias_or_related: Initialize=先清空 Consumer 再全量拷贝（p531）
  tags: [concept, replication-agreement, attribute-set]

- id: g25
  term: MSAD（Microsoft Active Directory）
  full_name: Microsoft Active Directory（书中明确 "MSAD stands for Microsoft Active Directory"）
  category: concept
  source_pages: p351-359, p369
  source_quote: |
    "MSAD stands for Microsoft Active Directory" (p369)
    "Persons creation from MSAD to 8770 directory • Update of directory attributes in both ways ... LDAP or
    LDAPS connection" (p353)
  definition: |
    本地部署的 Windows AD；8770 经专用账号（LDAP 389/LDAPS 636）做"一条映射+N 条规则"的双向属性同步，支持多台
    AD 服务器并行；另可装 MSAD 插件从 AD 右键开户。
  alias_or_related: Azure AD/Entra ID 为云侧平行能力（g26）
  tags: [concept, msad, active-directory]

- id: g26
  term: Azure AD（Microsoft Entra ID）
  category: concept
  source_pages: p360-361
  source_quote: |
    "Synchronization of Azure ID (renamed Microsoft Entra ID) tenant(s) with OV8770 company directory ...
    Azure AD is considered as the master node ... Microsoft Graph API, instead of LDAPS for MSAD ... No OXE
    users provisioning from Azure AD" (p360)
  definition: |
    云目录同步：Azure AD 恒为主节点，8770 作为应用经 Microsoft Graph API 拉取（无需管理员权限认证），支持
    Flat/Tree 与多域，可与 MSAD 并行；不 provision OXE 用户。四步配置：Azure 应用准备→租户信息→同步规则→
    属性映射。
  alias_or_related: 许可 Active Directory integration（与 MSAD 共用）；tree 模式另需 Directory 许可
  tags: [concept, azure-ad, entra-id, graph-api]

- id: g27
  term: Meta profile（元模板）
  category: concept
  source_pages: p363-364, p402-403
  source_quote: |
    "User creation is based on Meta profile" (p363)
    "Meta profile name / OXE node name / OXE free number range / Device type / OXE profile / Key Profiles /
    OXE SIP password rule / Cost center / OT applications" (p402-403)
  definition: |
    Users 应用 Profiles 页签定义的开户模板：OXE 节点+空闲号码段+话机类型+OXE profile(+COS) 组合；MSAD 插件按
    它一键开通用户，Directory number 留空自动取段内首个空闲号。
  alias_or_related: 前置：OXE profile（BASIC，含 COS 3/4/5）与 Free Numbers Ranges（31050-31059，需同步取回）
  tags: [concept, meta-profile, provisioning]

- id: g28
  term: LDIF（LDAP Data Interchange Format）
  full_name: LDAP Data Interchange Format（p85）/ LDAP Interchange Format（p540）
  category: concept
  source_pages: p85, p540
  source_quote: |
    "All or part of the database can be imported or exported in LDAP Data Interchange Format (LDIF) files ...
    Allows creating and modifying data • Does not remove data" (p85)
    "Importing LDIF files does not delete any entry • Attributes without values are not exported" (p540)
  definition: |
    LDAP 文本交换格式：8770 批量导入导出的通用管道（三范围 Entry/Sublevel/Branch × 本地/服务器）。导入永不删除
    ——删除靠 PurgeLdap 机制（misc10 标记+过滤器）。
  alias_or_related: CDPerson 为 8770 人员对象类（p540 LDIF 例、p381）
  tags: [concept, ldif, format]

# ── 二、角色 (role) ──

- id: g29
  term: Administrator（Global / Local）
  category: role
  source_pages: p440, p441, p453
  source_quote: |
    "Create administrator accounts • By default, they are global administrator accounts • Global admins
    displayed in blue color" (p440)
    "Local admin: • Access to all persons from its domain only" (p453)
  definition: |
    Security 应用建的账户默认是全局管理员（列表蓝色显示）；进三个预定义组（Users Configuration / Users &
    Directory Configuration / Users & Customization Configuration）并关联域后成为本地管理员，只能看管自己域。
  alias_or_related: Delegation 开关允许本地管理员再建本地管理员（p479）
  tags: [role, administrator, domains]

- id: g30
  term: Directory administrator（目录管理员）
  category: role
  source_pages: p328, p346
  source_quote: |
    "Display customization icon ... Disabled: only administrator account (i.e. AdminNmc) can customize the
    default configuration of the Web Directory client used by all users" (p328)
    "The Edit option, that allows customizing the theme, is reserved to the Directory administrator." (p346)
  definition: |
    持 Web Directory/Company Directory 管理级访问级别的管理员：可改 Web 目录客户端全局默认参数、定制主题
    （Edit）、配置搜索过滤器/网格/详情页。实验中由 AdminNmc 扮演。
  alias_or_related: 与 g29 域管理员是两套维度（应用权限 vs 域边界）
  tags: [role, directory-admin]

- id: g31
  term: AdminNmc / adminnmc
  category: role
  source_pages: p93, p152, p479
  source_quote: |
    "Here are the credentials to connect to the OmniVista 8770 server Login: AdminNmc Password: Superuser01*" (p93)
  definition: |
    8770 出厂超级管理员账户（实验口令 Superuser01*，实验口径）：Web 客户端/WBM/Directory/Security 全应用最高
    权限，保密实验中作 All 级对照组，域实验中作全局管理员开委派。
  alias_or_related: DN 形态 uid=adminnmc, cn=Administrators, cn=8770 administration, o=nmc（p544 工具参数）
  tags: [role, adminnmc, lab]

- id: g32
  term: MSADadmin
  category: role
  source_pages: p369, p372-375
  source_quote: |
    "A MSAD administrator must be created in the Microsoft Active Directory server. This account will be
    used by the 8770 server to manage the Active Directory." (p369)
    "The user must belong to the domain admins group." (p373)
  definition: |
    AD 侧为 8770 同步专建的管理员账户：须入 Domain Admins 组、密码设不可改+永不过期；填入 8770 的 MSAD
    Access info（Username/Password）。
  alias_or_related: 与 g33 MSAD8770Admin 方向相反（一个 8770→AD，一个 AD→8770）
  tags: [role, msad, account]

- id: g33
  term: MSAD8770Admin
  category: role
  source_pages: p404, p407
  source_quote: |
    "MSAD8770Admin is an 8770 administrator account dedicated to MSAD Plug-in. Its password has been defined
    at OmniVista 8770 server installation." (p404)
    "8770_user_dn=uid=MSAD8770Admin,cn=Administrators,cn=8770 administration,o=nmc" (p407)
  definition: |
    8770 侧为 MSAD 插件专建的管理员账户（安装时设密）：改密后必须重启 NMC Java Service Definition 服务；其 DN
    与加密密码写进 8770MSADPlugin.properties 供 AD 侧插件回调建用户。
  alias_or_related: 插件日志 start8770webclient.log 排障
  tags: [role, msad-plugin, account]

- id: g34
  term: Replication manager / Directory manager（复制管理器/目录管理器）
  category: role
  source_pages: p506, p511, p521
  source_quote: |
    "Configuration of the replication manager's password (of the slave server) • By default, replication
    manager's password is identical to the directory manager's password • It can be modified through
    toolsOmnivista.exe" (p506/p511)
    "Enter the directory manager password ... By default, the replication password is the same as directory
    manager one (superuser)." (p521)
  definition: |
    LDAP 层账户：directory manager 管目录库；replication manager 供复制协议认证（默认密码=directory manager
    的 superuser，实验口径），用 toolsOmniVista.exe 的选项 6 单独修改。
  alias_or_related: 协议里填的是从机的复制管理器密码
  tags: [role, replication, ldap-account]

# ── 三、订阅/许可 (subscription) ──

- id: g35
  term: Directory license（目录许可）
  category: subscription
  source_pages: p458, p514, p360
  source_quote: |
    "If the OmniVista 8770 server is based on a MCS solution ..., Directory license will be provided by
    default." (p458)
    "Must have the directory license"（复制前提，p514）
    "Directory license is required in case of synchronization in tree mode"（Azure AD tree 模式，p360）
  definition: |
    公司目录功能许可：复制主从双机都必须要；Azure AD tree 模式同步也要；MCS 版默认自带。
  alias_or_related: 与 g36 Domain Management、g38 Active Directory integration 组合使用
  tags: [subscription, license, directory]

- id: g36
  term: Domain Management license（域管理许可）
  category: subscription
  source_pages: p435, p458
  source_quote: |
    "Required licenses • Domain Management • Directory" (p435)
    "But the Domain Management license is still required." (p458)
  definition: |
    管理域功能许可：MCS 版也不自带，永远要单独持有；缺它时 Security 应用里 8770DomainManagement 建不了域。
  alias_or_related: 核查入口 Help > About（p458）
  tags: [subscription, license, domains]

- id: g37
  term: Unified Management license（统一管理许可）
  category: subscription
  source_pages: p35
  source_quote: |
    "User provisioning and company directory levels management ... Available with Unified Management license
    • Zero footprint (light client)" (p35)
  definition: |
    8770 WBM Users 应用（用户供给+目录层级管理）所需许可；轻客户端零安装。
  alias_or_related: WBM Configuration/Performance 与 Manage My Phone 不在此列
  tags: [subscription, license, wbm]

- id: g38
  term: Active Directory integration license（AD 集成许可）
  category: subscription
  source_pages: p351, p360
  source_quote: |
    "A license is required to enable both features"（MSAD 同步与 AD 结构更新，p351）
    "Feature controlled by Active Directory integration license (already used for MSAD integration)"（Azure AD，p360）
  definition: |
    AD 集成能力总许可：同时控制 MSAD 双向同步/结构更新与 Azure AD 同步两个特性；tree 模式另叠加 Directory 许可。
  alias_or_related: 与 g35/g36 并列的第三张目录域许可
  tags: [subscription, license, msad]

- id: g39
  term: Company Directory license（公司目录树许可）
  category: subscription
  source_pages: p35
  source_quote: |
    "Management of the Company Directory tree structure (submitted to Company Directory license)" (p35)
  definition: |
    WBM Users 应用中管理公司目录树结构的许可（书内仅此一处提及，边界未展开，待与 8770 价目文档核对）。
  alias_or_related: 待确认：与 Directory license 的关系书中未说明
  tags: [subscription, license, tree]

# ── 四、产品 (product) ──

- id: g40
  term: OmniVista 8770
  category: product
  source_pages: p1, p4-40
  source_quote: |
    "OMNIVISTA 8770 - R5.2 DIRECTORY ADMINISTRATION - EDITION 40" (p1)
    "Centralized network management solution"（OXE/OXO/OXE 统管网管，p5）
  definition: |
    ALE 网管平台（本书 R5.2 口径）：四套件（Setup/Network/Reports/Directory）+WBM，可物理 appliance 或虚拟机
    部署；目录套件是本书主角。
  alias_or_related: 与 4760 的迁移关系见 g09 Additional resources link
  tags: [product, omnivista]

- id: g41
  term: OmniPCX Enterprise（OXE）
  category: product
  source_pages: p9, p88-98
  source_quote: |
    "OmniPCX Enterprise — OXE R12.2 to R12.4 ... OXE Purple R100 (N1) ... R101.2 (N5)" (p9)
    "Host name: csa ... Main name: csm ... Node name: oxe"（实验实例，p89）
  definition: |
    ALE 企业级 PBX：8770 目录的"数据源"与链接对端（用户/话机）。实验实例 csa/csm（192.168.1.1/1.3，节点 101），
    账号 adfexc（FTP 取数）/mtcl（维护），netadmin/siteid 做前置检查。
  alias_or_related: 与 OXO Connect/OCE、OpenTouch 同属可纳管 PCX（p9 兼容矩阵）
  tags: [product, oxe, pbx]

- id: g42
  term: OpenTouch（OT BE/MS/MC）
  category: product
  source_pages: p9, p97
  source_quote: |
    "OpenTouch BE / MS / MC — OT R2.4 to R2.6.1"（p9）
    "Separate: the selected OXE is synchronized / Global: the selected OXE and associated OpenTouch are
    synchronized."（p97）
  definition: |
    ALE 协作通信系列：可被 8770 纳管；同步的 Global 模式会连带同步关联 OpenTouch；MSAD 插件开户可选
    OT applications。
  alias_or_related: 本书无 OT 专属实验（OT applications=None，p403）
  tags: [product, opentouch]

- id: g43
  term: IP Desktop Softphone（IPDSP）
  category: product
  source_pages: p48, p111, p134-136, p274
  source_quote: |
    "1 IPDSP softphone • 31000"（实验实例，p48）
    "IP-Softphone Emulation Select YES to enable IP Desktop Softphone on user 31000" (p112)
  definition: |
    ALE 软话机：用户经 TSC IP User 选项开启 IP-Softphone Emulation 后绑定使用；实验中 31000（Jean Dupont）作
    Click to Call 主叫。多设备链实验中作为第二设备挂到 Pierre Williams（31105）。
  alias_or_related: MicroSIP 为实验用第三方 SIP 软话机（31001/31003/31004 及 Public 号，p48/p274）
  tags: [product, softphone, ipdsp]

- id: g44
  term: OmniVista 4760
  category: product
  source_pages: p71
  source_quote: |
    "Useful for migration of OmniVista 4760 persons with multiple Primary links with OXE users" (p71)
  definition: |
    上一代网管（4760）：其"一人多主链"的人员模型经 Additional resources link 迁移到 8770。本书仅此一处提及。
  alias_or_related: 迁移操作细节在书外
  tags: [product, 4760, migration]

- id: g45
  term: OmniVista 8770 Capacity Planning tool
  category: product
  source_pages: p8
  source_quote: |
    "OmniVista 8770 Capacity Planning tool V3.0 for a better sizing flexibility of virtual machines
    parameters" (p8)
  definition: |
    官方容量定型工具 V3.0：为虚拟机参数 sizing 用。本书仅总览提及。
  alias_or_related: 版本号 V3.0 为 Ed40 口径
  tags: [product, sizing]

- id: g46
  term: MindTerm / dirmanag.exe / toolsOmniVista.exe（服务器自带工具集）
  category: product
  source_pages: p96, p521, p555
  source_quote: |
    "The host name is used by MindTerm application to create the SSH public key on the OmniVista 8770
    server" (p96)
    "toolsOmniVista.exe ... Select the choice 6: LDAP Replication Manager password update" (p521)
    "YOU WILL HAVE TO CONNECT TO 8770 SERVER VIA DIRMANAG.EXE APPLICATION AND DELETE THE ROOT 'ABS'." (p555)
  definition: |
    8770 服务器三件内置工具：MindTerm（SSH 公钥建立，OXE 声明 Connectivity 用）；toolsOmniVista.exe（停服务/
    改 directory manager 与复制管理器密码）；dirmanag.exe（目录根级管理，LDIF 管道坏结构后的救援通道）。
  alias_or_related: CustomDict（词典定制工具，p287）与 dict 工具族同属服务器端附带程序
  tags: [product, tools, server]

# ── 五、协议 (protocol) ──

- id: g47
  term: LDAP v3 / LDAPS
  full_name: Lightweight Directory Access Protocol（p62 展开）；LDAPS 全称书中未展开（LDAP over SSL 语义由上下文给出）
  category: protocol
  source_pages: p7, p32, p353, p377, p511, p514
  source_quote: |
    "LDAP v3 directory • ... Access through ALE clients and standard LDAP v3 clients" (p32)
    "Port 389 or 636 if LDAPS option is selected. ... Is LDAPS Select this option to secure the LDAP access
    in encrypted form." (p376-377)
    "LDAPS is not supported for Replication" (p514)
  definition: |
    目录访问协议：8770 目录本体为 LDAP v3；对 MSAD 用 389 明文或 636 加密（LDAPS，需 AD 服务器装 AD CS 角色发
    证书）；目录复制不支持 LDAPS。_LDAP Client import_为架构图中的导入服务（p7）。
  alias_or_related: MSAD 声明的 Scope 例 o=Ale,o=directoryRoot（p376）
  tags: [protocol, ldap, ldaps]

- id: g48
  term: LDIF（数据交换，协议族格式）
  full_name: LDAP Data Interchange Format
  category: protocol
  source_pages: p85, p540-548
  source_quote: |
    "LDIF is the exchange format for LDAP server text files" (p85)
    "dn: uid=victor durand,ou=mkt,l=brest,c=fr,o=ale,o=directoryroot ... objectclass: CDPerson ..." (p540)
  definition: |
    LDAP 文本交换格式（dn/objectclass/属性行结构）：8770 图形界面导入导出与命令行工具（8770\bin 六件套）共用
    的数据载体；CDPerson 是 8770 人员的 objectclass。
  alias_or_related: 与 g28 概念条互补——此处记录其协议/格式属性
  tags: [protocol, ldif, format]

- id: g49
  term: Microsoft Graph API
  category: protocol
  source_pages: p360-361
  source_quote: |
    "Authentication towards Azure AD from OV8770 as an application which wants to use Microsoft Graph API,
    instead of LDAPS for MSAD (Authentication without administrator rights)" (p360)
    "Manage User.ReadWrite.All permission" (p361)
  definition: |
    Azure AD 同步的认证与数据通道：8770 注册为 Microsoft 应用（应用机密+User.ReadWrite.All 权限）经 Graph API
    拉取，替代 MSAD 的 LDAPS 直连；无需 AD 管理员账号。
  alias_or_related: 与 g26 Azure AD 配套
  tags: [protocol, graph-api, azure]

- id: g50
  term: SNMP / SMTP / CMISE / (S)FTP / Telnet/SSH / IPSec, Corba, TDS / HTTPS
  category: protocol
  source_pages: p7, p13-26
  source_quote: |
    "HTTPS, LDAP(S) / IPSec, Corba, TDS, LDAP(S) ... SMTP ... MariaDB (SQL) / LDAP ... CMISE, (S)FTP,
    Telnet/SSH, LDAP ... OMC (FTP, HTTPS) ... SNMP Hypervisor / SNMPv3" (p7)
  definition: |
    8770 架构协议清单（p7 一图）：Web/WBM 走 HTTPS；OXE 对接走 HTTPS+LDAP(S)+CMISE+(S)FTP+Telnet/SSH+LDAP；
    邮件通知走 SMTP；告警外送 SNMP（v3，SNMP Hypervisor 附加选项）；OXO 经 OMC FTP/HTTPS；存储 MariaDB(SQL)+
    LDAP；配置侧另有 IPSec/Corba/TDS。
  alias_or_related: SSH 22 端口验证法 netstat -an | grep :22（p91）
  tags: [protocol, architecture, snmp]

# ── 六、资源 (resource) ──

- id: g51
  term: LdapAttributes.dict / LdapAttributes_user.dict / dict_user.zip（词典文件族）
  category: resource
  source_pages: p287, p299, p302, p309-310
  source_quote: |
    "Default translations are stored in the dictionaries LdapAttributes.dict ... Dictionary
    LdapAttributes_user.dict" (p287)
    "#3: update the archive 8770\Client\bin\dict_user.zip. This file will be downloaded by the 8770 clients
    to update their directory dictionaries" (p302)
  definition: |
    目录属性翻译词典族：源 LdapAttributes.dict（打开定制工具必选 C:\8770\Client\dict 下该文件）；用户词典
    LdapAttributes_user.dict（存 C:\8770\dict\user，只含被改属性）；客户端分发包 dict_user.zip（重连自动下载）。
    版本号在 Administration 应用 OmniVista 8770 页签，每保存自增。
  alias_or_related: 定制工具=CustomDict；语言字段如 English for US
  tags: [resource, dictionary, paths]

- id: g52
  term: 8770 服务器关键路径表（C:\8770\*）
  category: resource
  source_pages: p98, p165, p299, p302, p327, p406, p408, p412, p520, p521, p426
  source_quote: |
    "Log file C:\8770\log\ NMCSyncLdapPbx_1.log"（同步日志，p98）
    "C:\8770\Client\data\import"（服务器 LDIF 导出落盘，p165）
    "The .dict files are stored in the folder C:\8770\dict."（p299）
    "C:\8770\SunONE\sldap-8770\db\<replica_name>"（复制副本数据库，p520-521）
    "C:\8770\data\msadplugin\MSAD Server"（插件配置生成处，p406）
  definition: |
    路径速查：\log\NMCSyncLdapPbx_1.log=OXE 同步日志；\Client\data\import=服务器导出/导入缓冲；\dict 与
    \Client\dict=词典；\Locales\dict\user=本地化生成；\Client\bin\dict_user.zip=客户端词典包；
    \Client\Themes=主题（theme1=8770WBM，theme2=Custom，CSS）；\SunONE\sldap-8770\db\<replica>=复制副本库；
    \data\msadplugin\MSAD Server=8770MSADPlugin.properties。AD 侧：%LOCALAPPDATA%（安装文件中转）、
    C:\Program Files (x86)\Alcatel-lucent\8770MSADPlugin（插件安装）、%TMP%\start8770webclient.log（插件日志）、
    C:\Windows\System32\drivers\etc\hosts（DNS 替代）。SHARING 文件夹（8770_MAIL_SERVER 上）用于双虚机传文件。
  alias_or_related: 实验口径路径，生产按安装盘符调整
  tags: [resource, paths, filesystem]
```

---

## 任务覆盖自检（task↔id 映射）

| task | 关联术语条目 |
|---|---|
| task-01 OXE 注册同步 | g41 OXE、g50 协议、g52 路径（NMCSyncLdapPbx_1.log）、g46 MindTerm |
| task-02/03/04/05 自动创建 | g10 自动创建、g03 UID、g05 主链接、g14 成本中心 |
| task-06/07/08/09 链接与改名 | g05-g09 六类链接、g09 4760 迁移、g44 OmniVista 4760 |
| task-10 LDIF 导入导出 | g28/g48 LDIF、g52 路径 |
| task-11 Web 客户端 | g13 personal data、g30 Directory administrator |
| task-12 保密级别 | g11 保密级别、g12 访问级别、g13 |
| task-13 SIP 运营商 | g41 OXE（SIP 网关/翻译器上下文）、g15 DDI translator |
| task-14 Click to Call | g15 DDI、g16 ISDN、g17 STAP、g18 前缀规则 |
| task-15 词典定制 | g51 词典文件族、g46 CustomDict/dirmanag |
| task-16 客户端定制 | g51（Themes/dict_user.zip）、g30 |
| task-17 MSAD 声明 | g25 MSAD、g32 MSADadmin、g47 LDAP/LDAPS |
| task-18 MSAD 同步 | g25、g47、g14（CC 映射语境） |
| task-19 MSAD 插件 | g27 Meta profile、g33 MSAD8770Admin、g52 路径 |
| task-20 管理域 | g19 管理域、g29 管理员、g21 strict view、g35/g36 许可 |
| task-21 委派与定制视图 | g20 定制视图、g29 Delegation |
| task-22 目录复制 | g22-g24 复制三件套、g34 复制管理器、g35 Directory 许可 |
| task-23 LDIF 工具 | g46 dirmanag/toolsOmniVista、g28、g52 |
| 背景与平台 | g40 8770、g42 OpenTouch、g43 IPDSP/MicroSIP、g45 容量工具、g37/g38/g39 许可 |

六类分布：concept 28 / role 6 / subscription 5 / product 7 / protocol 4（合并同族协议）/ resource 2（词典族与路径表各为聚合条目）——总 52 个 id，全部出自原书文本，无外部编造；未展开缩写（STAP/DDI/COS/WBM/NMC/AHV 等）已如实标注。
