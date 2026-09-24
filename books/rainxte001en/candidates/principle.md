# 原则/清单/规则/公式/数值口径候选 — Rainbow OXO Connect (RAINXTE001EN Ed13)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: Rainbow 共 8 种订阅，定位与计费方式各不相同
  type: metric
  source_pages: p33
  source_chapter: Rainbow overview / Subscription plans
  source_quote: |
    "Rainbow Essential This free option is available to anyone who wants to try Rainbow for an
    unlimited period (no SLA). The Essential subscription can also be blended with any premium
    subscription" (p33)
    "Rainbow Enterprise Conference ... packages the Rainbow Enterprise service plan with unlimited
    phone conferencing minutes. The Rainbow Enterprise Conference user subscription is pre-paid
    yearly in advance (twelve months)." (p33)
    "Rainbow Conference An optional service proposed as a 'pay-as-you-go' model for phone (PSTN)
    conferencing with a price-perminute/per-connection. The organizer ... can be a Rainbow
    Essential (freemium) user, or premium user" (p33)
    "Rainbow Connect The per-user subscription addresses users of any Customer Relationship
    Management (CRM) application." (p33)
    "Rainbow Room An optional per-room subscription proposed for meeting rooms equipped with
    large screens" (p33)
  summary: |
    8 种订阅：Essential（免费、无限期试用、无 SLA，可与付费订阅混用）、Business（按用户）、
    Enterprise（Business 全部 + 多方视频会议 + 扩展文件存储 + O365/Google Suite 集成）、
    Attendant（话务台专用订阅：排队呼叫列表 + 监督控制台）、Enterprise Conference（Enterprise
    + 无限电话会议分钟数，按年预付 12 个月）、Conference（按分钟/按连接的 pay-as-you-go，
    组织者可以是免费用户）、Connect（CRM 连接器，按用户）、Room（按会议室）。选型决策：
    电话/话务台看 Business/Enterprise/Attendant；会议室场景用 Room；CRM 用 Connect。
  conditions: Ed13 / R6.3 时代的订阅目录；细节以 Features List（help.openrainbow.com）为准
  tags: [metric, licensing, subscription]

- id: p02
  title: 网络前提以官方 Network Requirements 文档为准，连通性与容量用 Rainbow Pilot 评估
  type: checklist
  source_pages: p36, p40, p42
  source_chapter: Network requirements
  source_quote: |
    "This page contains: ... A summary of port/protocol requirements for: Rainbow collaboration,
    Rainbow hybrid telephony, Rainbow Hub ; 2 PDF files" (p36)
    "This document details: The ports and protocols used by the Rainbow collaboration, Rainbow
    hybrid and Rainbow Hub solutions ... Rainbow domains and associated IP addresses, Bandwidth
    requirements, Configuration of corporate network elements DNS, Proxy, Firewall..." (p40)
    "RAINBOW PILOT allows you to assess your Rainbow connectivity from your location, and the
    capacity of a given location to handle a population of Rainbow users characterized by a
    flexible mix of usages between Collaboration, Conferencing, Hybrid or Hub telephony." (p42)
  summary: |
    上线前动作清单：查 help.openrainbow.com 的 "Check Rainbow Network Requirements" 文章（含
    端口/协议汇总：协作、混合话音、Hub 三块 + 两份 PDF：Network Requirements、Health data
    hosting；含域名与 IP 清单、带宽要求、企业网 DNS/Proxy/防火墙配置要求）；再用
    pilot.openrainbow.com 按协作/会议/混合话音/Hub 的用户配比评估站点承载能力。
  conditions: 书中只给指针，端口与帶寽数值在书外 PDF；生产化必须取最新版文档
  tags: [checklist, network]

- id: p03
  title: 建公司前先查重；一个用户不能同时属于两家公司
  type: rule
  source_pages: p47
  source_chapter: Introducing the companies
  source_quote: |
    "Before you start a company • Check that the target company does not exist in Rainbow. • To
    avoid possible duplicates, enter the name of the future company in the search bar • A user
    cannot be part of 2 different companies" (p47)
  summary: |
    两条硬规则：(1) 创建公司前必须在搜索栏查名，防止重复建司；(2) Rainbow 账号以邮箱为身份，
    一个人不能同时是两家公司的成员——规划多客户、多组织归属时要先决定唯一归属。
  conditions: 全版本通用；账号身份=邮箱地址（p91）
  tags: [rule, company]

- id: p04
  title: BP 专属权限只有两项；EC 公司与且仅与一个 BP 挂靠；集成伙伴须为 DR 或 IR
  type: rule
  source_pages: p48
  source_chapter: Introducing the companies / 2 types of companies
  source_quote: |
    "However, the following actions can only be performed by the BP: • Declaration & PBX •
    Opening of paid subscriptions • The customer's integration partner must be either a 'DR' or
    an 'IR'. Its name appears in the 'My company / Dashboard' screen." (p48)
    "To be managed by a BP, an 'EC' company must be attached to the company of this BP (one and
    only one attachment)." (p48)
  summary: |
    渠道角色分 DR（Direct Reseller）/ IR（Indirect Reseller）/ VAD（Value Added Distributor）/
    EC（End Customer）。多数管理操作 BP 和客户管理员都能做，但只有 BP 能做两件事：申报与创建
    PBX（Declaration & PBX）、开通付费订阅。EC 公司必须挂靠到某个 BP（且只能挂一家）。这决定了
    权责切分：客户管理员发现无法建 PBX/开订阅时，属于正常设计而非故障。
  conditions: 需持 BP/经销商账号才能执行这两项操作
  tags: [rule, company, licensing]

- id: p05
  title: 公司可见性四级（PUBLIC/PRIVATE/CLOSED/ISOLATED）行为定义与选型建议
  type: principle
  source_pages: p52
  source_chapter: Introducing the companies / Privacy & visibility
  source_quote: |
    "PUBLIC: a user from another company can see and invite members of your company. Your users
    can see and invite users outside their company.
    PRIVATE: a user from another company cannot see members of your company, but he can invite
    them via their email address. Your users can see and invite users outside their company.
    CLOSED : a user from another company cannot see the members of your company, but he can
    invite them via their email address. Your users can't see users outside their company, but
    they can invite them via their email address.
    ISOLATED : a user from another company cannot see the members of your company and cannot
    invite them. Your users can't see users outside their company, and they can't invite" (p52)
    "Get into the habit of systematically setting the 'closed' mode as soon as you create a
    Rainbow company. This is ideal for the vast majority of customers." (p52)
    "This 'isolated' mode is not recommended as it is very restrictive. Please check the impacts
    ... In particular, your users will no longer be able to be invited to conferences (bubbles)
    external to your organization." (p52)
  summary: |
    四级行为矩阵（外部人能否看见你 / 能否邀请你 × 你的用户能否看见外部 / 能否邀请外部）：
    PUBLIC 双向可见可邀；PRIVATE 外部看不见但可凭邮箱邀请、你的用户不受限；CLOSED 双向都
    看不见、但双方都能凭邮箱邀请；ISOLATED 双向完全隔离。选型原则：拿不准就建司即设 CLOSED
    （适合绝大多数客户）；ISOLATED 不推荐——代价是用户无法被外部组织邀请进 bubble 会议。
  conditions: 可见性可在 company settings 中事后修改
  tags: [principle, visibility, company]

- id: p06
  title: SSO 方式清单：Azure AD(SAML/OIDC)、ADFS(SAML)；配置 SSO 的管理员须有 Enterprise 服务等级
  type: checklist
  source_pages: p53
  source_chapter: Introducing the companies / SSO & Authentication method
  source_quote: |
    "you can enable single sign-on (SSO*) with your Azure Active Directory, or with your
    corporate AD (ADFS). ... Azure AD - SAML Azure AD - OIDC ADFS - SAML
    The administrator must have an 'Enterprise' service level
    You can set up several authentication methods within your company, and decide which users
    need to use which method." (p53)
    "NB : other methods are possible, subject to ALE confirmation, when they are based on
    standard protocols. For example, with SAML V2 : Shibboleth, RSA, … and with OIDC : LemonLDAP,
    OKTA, CAS APEREO, Ping Identity, …" (p53)
  summary: |
    标准 SSO 组合三种：Azure AD-SAML、Azure AD-OIDC、ADFS-SAML。前置条件：执行配置的管理员
    账号须为 Enterprise 服务等级。SSO 可全公司启用或仅对部分用户启用；一家公司可并存多种认证
    方式并按用户指定。非列表内的 IdP（Shibboleth、RSA、LemonLDAP、OKTA、CAS、Ping Identity 等）
    基于标准协议时须先取得 ALE 确认。
  conditions: SSO 具体配置走支持站点的技术手册（书中只给指针）；依赖客户已有 Azure AD/ADFS
  tags: [checklist, security, sso]

- id: p07
  title: 密码复杂度硬规则：≥12 字符，且至少 1 个大写字母、1 个数字、1 个特殊字符
  type: rule
  source_pages: p53, p93, p94, p100
  source_chapter: SSO & Authentication / Manual creation / Bulk import / Security: password & login
  source_quote: |
    "Traditional Authentication by complex password (min 12 characters)." (p53)
    "(At least 12 characters and contain at least 1 uppercase, 1 number, and 1 special
    character)" (p93)
    "Passwords must be at least 12 characters long and contain at least 1 capital letter, 1
    number and 1 special character." (p94)
    "A password must be at least 12 characters long and contain at least 1 capital letter, 1
    number and 1 special character." (p100)
  summary: |
    原书四处一致的口径：长度 ≥12 字符，至少含 1 个大写字母（capital/uppercase）、1 个数字、
    1 个特殊字符。注意：原文只单列大写/数字/特殊字符三类要求，未单独要求小写字母（12 字符
    长度实际隐含混合字符）。适用于手动创建、邀请注册、CSV 批量导入、管理员改密等所有设密场景。
  conditions: Rainbow 原生认证（非 SSO）时适用；CSV 导入时若用 SSO 则密码字段可留空（p94）
  tags: [rule, security, metric]

- id: p08
  title: TOTP 双因子适用于全部用户，特别推荐给管理员；需第三方验证 App
  type: principle
  source_pages: p53
  source_chapter: Introducing the companies / SSO & Authentication method
  source_quote: |
    "Authentication with TOTP (Time-based One Time Password) Users need a third-party
    authentication application (Google Authenticator , Microsoft Authenticator , Authy). This
    method applies to all types of users but is particularly recommended for the administrators." (p53)
  summary: |
    Rainbow 原生认证的第二种方式是 TOTP 动态口令，依赖用户手机上的第三方验证应用（Google
    Authenticator、Microsoft Authenticator、Authy）。全员可用，管理员账号强制建议开启——管理员
    账号权限大，是被攻击的高价值目标。
  conditions: MFA-TOTP 配置以支持站点参考文章为准（书中给指针）
  tags: [principle, security]

- id: p09
  title: 管理权责分配：可设多名管理员；企业目录默认客户管理员管理、可委托给非管理员；信息频道仅 Enterprise 等级可创建
  type: rule
  source_pages: p59, p60, p61
  source_chapter: Administrators profiles
  source_quote: |
    "The 'Roles' tab is used to assign administrative rights to the client company. • It is
    possible to have several administrators to manage the company." (p59)
    "By default, a customer administrator can manage the directory. You can delegate the
    management to other Rainbow users, who are not necessarily administrators of the company." (p60)
    "Only users with an 'Enterprise' service level can create Information Channels." (p61)
    "All Rainbow members in your company will automatically subscribe to these channels. Members
    will not be able to unsubscribe." (p61)
  summary: |
    三条权责规则：(1) Roles 页签分配管理权限，一个公司可设多名管理员；(2) 企业目录（Business
    Directory，含外部联系人电话，改善来电识别）默认归客户管理员管，可委托给非管理员用户，
    支持手动建或 CSV 批量导入并出导入报告；(3) 信息频道（Information Channels）只有 Enterprise
    服务等级的用户能创建，且指定的强制频道成员自动订阅、不能退订——发公司通告时要想清楚。
  conditions: 频道可面向本公司全员自动订阅，或面向自选成员自动订阅（p61）
  tags: [rule, admin, directory]

- id: p10
  title: 订阅计费按用户计价，周期为月付或预付 1/3/5 年
  type: metric
  source_pages: p64
  source_chapter: Subscriptions
  source_quote: |
    "The price is per user and different subscription plans are possible:
    • Monthly
    • Prepaid 1, 3 or 5 years" (p64)
  summary: |
    计费口径：按用户（per user）计价；两种付费节奏：月付，或预付 1 年、3 年、5 年。
    商务报价与续费提醒按此口径排期。
  conditions: Enterprise Conference 订阅特殊：按年预付 12 个月（p33）
  tags: [metric, licensing, billing]

- id: p11
  title: 电话服务硬门槛：成员必须分配 Business / Enterprise / Attendant 订阅
  type: rule
  source_pages: p65
  source_chapter: Subscriptions
  source_quote: |
    "Subscriptions are first assigned to the client company. Then, these subscriptions are
    assigned to company members by the BP administrator or local administrator
    Each member must have a subscription to use telephony services
    • Business
    • Enterprise
    • Attendant" (p65)
  summary: |
    订阅流：先由 BP 开给客户公司（公司级池），再由 BP 管理员或本地管理员分配到成员。要用电话
    服务（话音/话务台），成员必须持有 Business、Enterprise 或 Attendant 之一；免费 Essential
    不能用电话服务。排障时"用户不能打电话"先查 Services 页签有没有订阅。
  conditions: 免费 Essential 仅协作功能
  tags: [rule, licensing, subscription]

- id: p12
  title: 实验口径：LAB 期间只允许用 Voice 月付订阅，禁止预付
  type: rule
  source_pages: p66, p176
  source_chapter: Subscriptions / Attendant lab
  source_quote: |
    "During LAB Use ONLY Voice MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID!!!" (p66)
    "Choose the subscription offer: Attendant Monthly — DON'T USE 'PREPAID' IN THE TRAINING" (p176)
  summary: |
    实验环境规则（实验口径）：培训/实验中所有订阅一律选 Monthly（含 Attendant Monthly），
    不买年付预付——避免污染培训账号的商务计费。此规则仅适用于 LAB，生产环境按客户商务选择。
  conditions: 仅 RLAB 培训环境
  tags: [rule, lab, licensing]

- id: p13
  title: OMC 首次连接规则：Expert 模式 + 服务器认证；首次登录专用密码；证书装入受信任根；每个客户密码必须不同；客户信息必填
  type: checklist
  source_pages: p70, p74, p75, p77, p78
  source_chapter: OMC Installation (How-To)
  source_quote: |
    "OXO Connect default IP address 192.168.92.246 ; Password 1st login: pbxk1064" (p70)
    "Make a connection to the system with OMC in Expert mode with server authentication ...
    Enter the default installer password pbxk1064 only used for the first connection" (p74)
    "In order to avoid displaying the security alert at each connection, you must install the
    certificate the 1st time. ... browse to, 'Trusted Root Certification Authorities'" (p75)
    "The passwords must be different for each customer! ... Passwords can be modified if
    necessary in OMC/Security menu" (p77)
    "Information marked with an * are mandatory." (p78)
  summary: |
    首连流程与规则：OMC 装在管理员 PC；连接选 Expert 菜单 + LAN/WAN + 勾选 Server
    authentication；首次登录用安装师密码 pbxk1064（实验口径/出厂默认，仅首次登录用）；安全
    警报时查看并安装证书到"受信任的根证书颁发机构"，之后不再弹警；随后必须为各账户定义密码，
    且每个客户的密码必须互不相同（后续可在 OMC/Security 改）；首次连接必须录入带 * 的客户
    信息（可顺带录入安装技师即供应商信息）。
  conditions: 出厂默认 IP 192.168.92.246 与首登密码 pbxk1064 为实验/默认口径，生产必须替换
  tags: [checklist, omc, security]

- id: p14
  title: 实验口径：OXO 与客户端 PC 的 IP 规划（改址参数全表）
  type: metric
  source_pages: p80, p81, p82
  source_chapter: OXO Connect IP settings modification (How-To)
  source_quote: |
    "Address IP: 192.168.1.246 ; Subnet mask: 255.255.255.0 ; Default router address:
    192.168.1.254 ; DNS 1 : 192.168.1.250 ; DNS 2 : 10.20.30.250 ; DHCP range : 192.168.1.30 to
    192.168.1.39 ; Restart OXO connect" (p80)
    "In the DHCP tab, define the IP addresses range for deskphones: Start: 192.168.1.30 End:
    192.168.1. 39" (p81)
    "Change the PC IP settings: IP Address: 192.168.1.10 ; Subnet mask: 255.255.255.0 ;
    Gateway: 192.168.1.254 ; DNS 1: 192.168.1.250 ; DNS 2: 10.20.30.250" (p82)
  summary: |
    实验口径（RLAB POD 环境，非生产值）：OXO 主 CPU 改为 192.168.1.246/24，网关
    192.168.1.254，DNS1 192.168.1.250、DNS2 10.20.30.250，话机 DHCP 池 192.168.1.30-39，改完
    重启 OXO；客户端 PC 改为 192.168.1.10/24。路径：OMC/Hardware and limits/Lan/IP
    configuration（Boards 页签填 Main CPU，LAN 页签填路由与掩码，DNS 页签，DHCP 页签）。
    生产化时按客户网段整体替换。
  conditions: 实验口径；OMC 操作后需重启 OXO 生效
  tags: [metric, lab, network]

- id: p15
  title: PBXID 与激活码均由 Rainbow 平台生成；接入域名保持默认 openrainbow.com
  type: rule
  source_pages: p84, p85, p86
  source_chapter: Connect an OXO to Rainbow (How-To)
  source_quote: |
    "The credentials can be given to you by your reseller, who created the PBXs for your
    company. ... You can also find them on your own, by logging into Rainbow with your Rainbow
    client administrator account." (p84)
    "You will find here: PBXID, Activation code" (p85)
    "Domain name Leave the default value: openrainbow.com ; Rainbow PABX-ID The Rainbow ID is
    generated by Rainbow. ; Activation code The activation code is generated by Rainbow." (p86)
  summary: |
    双凭证获取两条路：经销商提供，或用客户管理员账号登录 Rainbow → My company → Communication
    → 选中 OXO 查看 PBXID 与 Activation code。填入 OMC/Cloud/Rainbow 并点 Rainbow enabled +
    Apply。域名保持默认 openrainbow.com 不要改。凭证不是 PBX 序列号，由平台生成。
  conditions: 实验账号 cCpP.admin@ale-training.com / Superuser-P*（实验口径）
  tags: [rule, onboarding]

- id: p16
  title: 接入状态验证口径：Webdiag 显示 "connected with final password"；系统日志查 ccrbagent.log
  type: rule
  source_pages: p88
  source_chapter: Connect an OXO to Rainbow / Maintenance
  source_quote: |
    "OMC /Tools /Webdiag /Services /Rainbow Status — Control the connection status: « connected
    with final password » ... The rainbow agent log file name is: ccrbagent.log" (p88)
  summary: |
    PBX-Rainbow 连接是否正常的判据：Webdiag 工具（登录 installer + 安装师密码）→ Services →
    Rainbow Status 应显示 "connected with final password"（还在用临时/默认口令连接说明没改密
    或没连上）；Rainbow agent 的系统日志文件名为 ccrbagent.log（System 页签/System Files/Log
    files 下载）。
  conditions: Webdiag 登录用 installer 账号
  tags: [rule, maintenance, troubleshooting]

- id: p17
  title: 成员创建四法：手动逐个、邮件邀请、CSV 批量导入、Azure AD 同步
  type: checklist
  source_pages: p92, p95
  source_chapter: Members of a Rainbow company
  source_quote: |
    "Members can be created: Manually • Creation one by one • By invitation • Via email address
    • In this case, it will be necessary to customize the account settings once it is created
    By bulk import • From .CSV file(UTF-8) • Microsoft Azure Active Directory • Also allows
    contact search" (p92)
    "Import via Azure Active Directory is reserved for administrators with 'Voice Enterprise'
    service level" (p92)
    "Bulk Import • Synchronization with AD for creating, editing, or deleting members • You need
    to associate your Azure Active Directory with your Rainbow company" (p95)
  summary: |
    四条路径：手动逐个建（信息最全）、邮件邀请（用户自注册，事后要补号码/订阅等设置，适合少量
    用户）、CSV 批量导入（UTF-8，可建/改/删）、Azure AD 同步（建/改/删 + 通讯录搜索，需先把
    Azure AD 关联到 Rainbow 公司）。权限边界：Azure AD 导入只留给 "Voice Enterprise" 服务等级的
    管理员；邀请创建的邮件发件人是 noreply@openrainbow。
  conditions: Azure AD 关联是管理员手动操作（Manual operation at your own initiative）
  tags: [checklist, member]

- id: p18
  title: CSV 批量导入规则：UTF-8 模板 + 设备按 MAC 绑定 + 同步报告 + SSO 时密码字段留空
  type: rule
  source_pages: p94
  source_chapter: Members of a Rainbow company / Bulk import
  source_quote: |
    "To create, modify and delete users ; Assign their devices (By MAC@) previously created ;
    To define global user parameters ... Click 'Download Sample File' to get a template. ...
    A synchronization report shows you the errors during the import. • If SSO authentication is
    used, the 'password' field in the CSV file does not need to be filled in." (p94)
  summary: |
    CSV 导入可批量建/改/删用户、给已建设备按 MAC 地址绑定、定义全局用户参数。操作要点：先下
    载样例模板（含必填/选填字段与格式），导入后看同步报告排查错误行；公司启用 SSO 时 CSV 的
    password 列留空即可。
  conditions: CSV 需 UTF-8 编码；由 BP 或客户管理员操作（p94）
  tags: [rule, member, checklist]

- id: p19
  title: 成员设置七大块：Information / Permissions / Telephony / Programmable keys / Services / Roles / Security
  type: checklist
  source_pages: p96
  source_chapter: Members of a Rainbow company / Member settings
  source_quote: |
    "Information •Identifier, last name, first name, language, country •Timezone: voicemail
    timestamp •Visibility ... •Tags ... Permissions •To grant the right to Rainbow features
    Telephony •Equipment: PBX of the company •Extension number and public number •Physical
    device associated (optional) •Telephony features and rights Programmable keys ... Services
    (subscription) •Business, Enterprise, attendant Roles •Administration: Yes/No, Business
    directory, Channels Security •Modify password, identifier & authentication method" (p96)
  summary: |
    成员配置清单七块（原书页面列出 7 项；全局上下文曾记为"八块"，以原文 7 块为准）：
    Information（含时区——影响留言时间戳；可见性；Tags 便于目录搜索）、Permissions、Telephony
    （设备选 PBX、分机号与公众号码、关联物理话机、电话特性）、Programmable keys（可建按键组
    批量套用到多个成员）、Services（订阅）、Roles（管理权/目录/频道）、Security（改密、改登录
    邮箱、改认证方式）。用户排障/开户按这 7 块逐项核对。
  conditions: 可见性可改为 same as company / none / public / private 等（p96）
  tags: [checklist, member]

- id: p20
  title: 删除成员有 10 天宽限期；恢复后订阅降为 Essential，须重新分配许可并重配话机
  type: rule
  source_pages: p99
  source_chapter: Members of a Rainbow company / Members deletion
  source_quote: |
    "When you delete a user, his or her status becomes 'Suspended' for a period of 10 days
    (called the 'grace period') ... Restore user if delete operation was an error • Permanently
    delete the user if you're sure. Without any action from you, the account will be deleted
    after 10 days" (p99)
    "When deleted, the user's subscription was automatically removed. If you restore it, it will
    default to 'Essential' (free) mode, so you'll need to reallocate the appropriate license to
    restore the user's service level. It will also be necessary to reassign the user's telephone
    line." (p99)
  summary: |
    删除规则：删除后账号进入 10 天 "Suspended" 宽限期，可恢复或彻底删除，10 天不处理则自动
    彻底删除。重要副作用：删除时订阅被自动回收；恢复后账号默认 Essential（免费）——必须重新
    分配合适订阅，并重新关联电话分机。关联邮箱报错（提示邮箱已被占用）时先查是不是 10 天内
    刚删的用户（p93）。
  conditions: 宽限期固定 10 天
  tags: [rule, member, metric]

- id: p21
  title: 管理员改密立即踢在线用户下线（防账号冒用）；改登录邮箱不丢账号历史
  type: rule
  source_pages: p100
  source_chapter: Members of a Rainbow company / Security: password & login
  source_quote: |
    "If the user is logged in at the time you make the password change, he/she will be logged
    out immediately. This is very useful if you suspect that a Rainbow account is being
    spoofed." (p100)
    "Change the login email if necessary, without losing the account history." (p100)
  summary: |
    Security 页签可做三件事：改密（遵守复杂度）、改登录邮箱（保留账号历史）、改认证方式。
    关键行为规则：改密的瞬间该用户若在线会被立即登出——这是处置"疑似账号被冒用"的标准手段，
    也意味着日常帮用户改密要提前告知会被踢下线。
  conditions: 全版本通用
  tags: [rule, security, member]

- id: p22
  title: RCC 模式能力边界：仅能监督话机（摘机/挂断/转移），音频完全留在话机
  type: rule
  source_pages: p6, p110, p112, p116
  source_chapter: Introducing the Members / Associate extension numbers
  source_quote: |
    "At this step, Rainbow users can only supervise their extension: RCC mode (Remote Call
    Control) • Supervision of DeskPhones by the Rainbow application (Pick up, hang up, transfer)
    • Audio is exclusively managed by the deskphone" (p6)
    "Once associated, members will be able to supervise their phone from Rainbow (unhook, hang
    up, transfer), this is the RCC (Remote Call Control) mode. Without a WebRTC gateway, the
    audio will be exclusively managed on the phone." (p112)
  summary: |
    PBX 接入 Rainbow 但未部署 WebRTC 网关时即为 RCC 模式：Rainbow 客户端可对绑定话机做接听、
    挂断、转移三类监督操作，音频全程走话机。这是"无网关时的正常形态"，要向客户明确说清不是
    故障。教材实验（p116）还验证：从 RCC 客户端呼叫"纯 Rainbow 用户"（无 OXO 分机）是否可行，
    作为网关价值的对照测试。
  conditions: 无 WebRTC 网关；用户已关联 OXO 分机
  tags: [rule, rcc, gateway]

- id: p23
  title: Rainbow number 由 Rainbow agent 在用户选 "computer" 路由时自动写入 Remote Extension number
  type: rule
  source_pages: p115, p233
  source_chapter: Associate extension numbers / Teams user configuration
  source_quote: |
    "The list of OXO Connect extension numbers is synchronized live with the Rainbow
    environment. Once the association done, a new field is displayed, the Rainbow number. ...
    This number will be retrieved later for WebRTC gateway use. It will be automatically
    configured in Remote Extension number by the Rainbow agent (e.g. BBB10070254106463346) when
    the user selects 'computer' as routing from his Rainbow client (PC or smartphone)." (p115)
  summary: |
    分机关联后界面会出现 Rainbow number 字段（形如 BBB10070254106463346）。它无需手工配置：
    用户在 Rainbow 客户端把路由选为 "computer" 时，Rainbow agent 自动把它写进 PBX 侧的
    Remote Extension number。OXO 分机列表与 Rainbow 环境实时同步。排障 WebRTC 音频落地时要
    知道这个隐藏配置项。
  conditions: 需已完成分机关联
  tags: [rule, rcc, gateway]

- id: p24
  title: WebRTC 网关的本质是音频媒体互通；部署前提是 PBX 已接入 Rainbow
  type: principle
  source_pages: p118, p120
  source_chapter: OXO Connect WebRTC Gateway
  source_quote: |
    "The WebRTC Gateway brings voice interoperability between Rainbow Clients and PBX ecosystem.
    • This enables an audio media relationship between Rainbow applications and devices of a
    PBX connected to Rainbow" (p118)
    "The WebRTC gateway requires an OXO Connect or OXO Connect Evolution ; Prerequisites the
    PBX must be connected to Rainbow" (p120)
  summary: |
    原则：网关解决的是"音频"不是"呼叫控制"——呼叫控制始终在 PBX，网关在 Rainbow 应用与 PBX
    设备之间建立音频媒体关系（统一多终端体验）。部署顺序硬前提：先连 PBX 到 Rainbow，再上
    网关；载体必须是 OXO Connect 或 OXO Connect Evolution（形态：OCE 集成 / OCE Front End /
    NUC 迷你机 / ESXi 虚机）。
  conditions: Rainbow Business/Enterprise 订阅用户（p118 部署需求页）
  tags: [principle, gateway, architecture]

- id: p25
  title: 自动配置版本前提 R4.0.020.002+；自动建 5 项、安装员仍需做 3-5 项（边界清单）
  type: rule
  source_pages: p121, p150
  source_chapter: OXO Connect WebRTC Gateway / Automatic configuration
  source_quote: |
    "The automatic configuration of the internal / external WebRTC gateway is available from
    system version R4.0.020.002" (p121)
    "Automatic configuration applies to versions greater than R4.0.020.002" (p150)
    "The following settings are managed automatically: • Activation of internal WebRTC gateway
    (OCE only) • Creation of WebRTC SIP gateway • Configuration of the SIP Account with the
    Rainbow PBX ID • Creation of VoIP accesses and trunk group • Configuration of ARS table to
    route Rainbow calls
    The following settings are still to be done by the installer as they are specific to each
    customer : • Connect PBX to Rainbow • Creation and association of the AnyDevice/Rainbow
    virtual terminals • Configuration of numbering plans and of the barring" (p121)
    "...• Installation & configuration of the external WebRTC virtual machine / Standalone PC
    ... • Activation of the WebRTC gateway" (p121, external 额外手工厂)
  summary: |
    版本门槛：内部/外部网关自动配置从 R4.0.020.002 起可用（p121 表述为 "from"，p150 实验手册
    表述为 "greater than"，取完整位数 R4.0.020.002）。自动完成的 5 项：内部网关激活（仅 OCE）、
    WebRTC SIP 网关创建、用 Rainbow PBXID 配置 SIP 账号、建 VoIP 接入与中继组、配 ARS 路由表。
    安装员仍要手工做的：连 PBX 到 Rainbow、创建并关联 AnyDevice/Rainbow 虚拟终端、编号计划与
    闭锁（barring）；外部拓扑还多了 VM/独立 PC 的安装配置和网关激活动作。编号计划与闭锁全书
    均未展开，属于"书外的最后一步"。
  conditions: 内部网关自动激活仅限 OCE（OXO Connect Evolution）
  tags: [rule, gateway, version, checklist]

- id: p26
  title: 网关激活/自动部署只能由 Rainbow Reseller（经销商）管理员账号操作
  type: rule
  source_pages: p121, p151
  source_chapter: Automatic configuration
  source_quote: |
    "Automatic deployment is managed from the Rainbow Reseller administrator account" (p121)
    "Automatic activation of the WebRTC gateway is performed by the trainer with a reseller
    administrator account ... He is the only authorized account to manage this service" (p151)
  summary: |
    权限规则：WebRTC 网关的激活与自动配置（编辑客户公司 PBX、选 Internal/External、定通道数）
    只有 Reseller 管理员账号有权执行——客户管理员只能查看连接状态。现场发现"没有激活网关的
    按钮"时，先确认登录身份是否为经销商管理员。
  conditions: FE（OCE Front End）自动配置同样在编辑客户公司 PBX 时启用（p122）
  tags: [rule, gateway, admin]

- id: p27
  title: 终端形态版本规则：Multiset 副站 R6.0 起用 Free Rainbow in Twinset（省 UTL）；R5.2 及以前用 Anydevice；纯 Rainbow 用户只建 Anydevice
  type: rule
  source_pages: p123
  source_chapter: OXO Connect WebRTC Gateway / Deployment steps
  source_quote: |
    "Create a Multiset • The main station is the physical station • The secondary station is •
    Free Rainbow in Twinset from R6.0 • (Anydevice up to R5.2)" (p123)
    "In the case of a user with only Rainbow (without a physical station), create for this user
    only an Anydevice terminal" (p123)
    "Note: Until Release 5.2 the AnyDevice equipment was also used as a secondary station in
    multiset" (p123)
    "Secondary station from Release 6.0: The Free Rainbow in Twinset virtual terminal must be
    used in order to save an UTL license (UTL Bypass)" (p123)
  summary: |
    无论哪种网关拓扑都要做的一步：给用户建终端。有物理话机的用户建 Multiset（主站=物理话机，
    副站=虚拟终端）：R6.0 起副站必须用 Free Rainbow in Twinset（UTL Bypass，省一个 UTL 许可）；
    R5.2 及以前副站用 Anydevice——跨版本升级交付时副站类型语义不同，要按系统版本选。没有物理
    话机的纯 Rainbow 用户只建一个 Anydevice 终端。配置细节参照 TC2479。
  conditions: 版本分界 R5.2 / R6.0；参照文档 TC2479（Rainbow WebRTC Gateway with OXO Connect）
  tags: [rule, gateway, version, licensing]

- id: p28
  title: 集成 WebRTC 网关从 R3.2 起：免 SIP trunk 许可（旁路）；此前须外部网关 + 私有 SIP trunk + 许可
  type: rule
  source_pages: p125
  source_chapter: WebRTC integrated to OXO Connect Evolution
  source_quote: |
    "Integrated WebRTC GW From R3.2 ... Same feature level as the external WebRTC GW topology ...
    No need for SIP trunk licenses (bypass) ... Before R3.2 External WebRTC GW Private SIP Trunk
    SIP Trunk Licenses needed ... Supported for OCE and OXO Connect • Supported topologies:
    Integrated and External ... SW upgrade via OXO management tool and Cloud Connect Update
    service" (p125)
  summary: |
    版本-许可规则：R3.2 起可用 OCE 集成网关，功能级别与外部网关拓扑相同，且免 SIP trunk 许可
    （bypass 旁路），经 OCE 管理工具配置维护、经 OXO 管理工具 + Cloud Connect Update 升级。
    R3.2 之前的做法是外部网关 + 私有 SIP trunk（要吃 SIP trunk 许可）。集成与外部两种拓扑在
    OCE 和 OXO Connect 上都支持。
  conditions: 集成网关仅 OCE（OXO Connect Evolution）可用（p129 矩阵中 Power CPU EE 不支持）
  tags: [rule, gateway, version, licensing]

- id: p29
  title: 网关与 Rainbow 之间的互联网流量用 HTTPS + SRTP 加密（集成与外部拓扑均适用）
  type: rule
  source_pages: p126
  source_chapter: WebRTC integrated to OXO Connect Evolution / Security
  source_quote: |
    "Communication flows between the WebRTC GW and Rainbow over the internet are secured with
    HTTPS and SRTP • This applies for external and integrated WebRTC GW topologies" (p126)
  summary: |
    安全基线：WebRTC 网关到 Rainbow 云的互联网通信全程 HTTPS（信令）+ SRTP（媒体），无论集成
    还是外部拓扑。做防火墙策略时按加密流量放行，不需要为媒体另开明文通道。
  conditions: 全拓扑通用
  tags: [rule, security, gateway]

- id: p30
  title: OCE Front End 网关前提：双端 ≥ R4.0 MD 强制；免费许可由 FTR 自动提供；无 PBX 能力；无需 OMC
  type: rule
  source_pages: p128, p129
  source_chapter: WebRTC gateway on OCE Front End
  source_quote: |
    "The release ≥ R4.0 MD must be installed on both the Front-End RGW and the OXO Connect call
    server" (p128)
    "The license is free and auto-provisioned (FTR) ... Release ≥ R4.0 MD is mandatory ... Full
    ALE solution, easy to buy (one order for OXO Connect and OCE Front-End)" (p128)
    "A specific free License provides the behavior WebRTC Gateway on OCE Front-End • An OCE in
    front-end Mode is limited to WebRTC GW feature (No UTLs, etc…) ... OCE Front-End does not
    provide PBX capabilities • OMC tool is not needed for OCE Front-End provisioning" (p129)
  summary: |
    OCE-FE 拓扑四条硬规则：(1) 前端 RGW 和 OXO Connect 呼叫服务器两端都必须 ≥ R4.0 MD；(2)
    Front End 专用许可免费且由 FTR（首次开箱）自动提供，开单时 OXO Connect + OCE Front-End 一张
    订单；(3) 前端模式只做 WebRTC 网关，不提供 PBX 能力（无 UTL 等）；(4) OCE-FE 供应不需要
    OMC 工具（管理走 Rainbow Admin + Cloud Connect）。安装维护流程与常规 OXO 相同（FTR、OXO
    Connectivity、OMC）。
  conditions: 网关运行在客户 LAN 的 IPBox 上，位于承载呼叫服务器的另一台 OXO Connect 之前
  tags: [rule, gateway, version]

- id: p31
  title: 网关类型 × 硬件容量矩阵：内部 GW 仅 IPBox（20 路）；外部 GW（NUC）双硬件均 50 路；OCE-FE 仅 Power CPU EE（20 路）
  type: metric
  source_pages: p129
  source_chapter: WebRTC gateway on OCE Front End
  source_quote: |
    "Type of Rainbow GW | OXO Connect (Power CPU EE) | OXO Connect evolution (IPBox)
    Internal GW | Not supported | 20 calls max.
    External GW (NUC) | 50 calls max. | 50 calls max.
    OCE-FE GW | 20 calls max. | Not supported" (p129)
  summary: |
    逐格转写：内部（集成）网关——Power CPU EE 不支持，IPBox 平台最多 20 路通话；外部网关
    （NUC 迷你机）——两种硬件都是最多 50 路通话；OCE-FE 网关——Power CPU EE 硬件最多 20 路，
    IPBox 不支持（有 IPBox 时直接用内部网关）。选型时按承载硬件对号入座。
  conditions: 硬件分 OXO Connect Power CPU EE 与 OXO Connect Evolution（IPBox）两类
  tags: [metric, capacity, gateway]

- id: p32
  title: OCE-FE 安装靠 FTR 自动化：浏览器进 192.168.94.246，产品类型选 Frontend WebRTC；配置变更后需 warm reset
  type: checklist
  source_pages: p130, p131, p132, p133
  source_chapter: WebRTC gateway on OCE Front End / Installation
  source_quote: |
    "Installation of the OCE Front-End is automated with the FTR procedure • FTR provides the
    OCE Front-End license and upgrades the OCE release (≥ R4.0 MD) if necessary ; Connect to the
    OCE Front-End ETH1 in DHCP mode • and start a Web browser to 192.168.94.246 ; At the first
    connection to a brand new IPBox, an installer password must be defined • Alcatel1 for
    example" (p130)
    "Define the product type 'Frontend WebRTC' ... Enter the customer reference, IP parameters…
    FTR OK" (p131)
    "A warm reset is necessary to take into account modification to Rainbow WebRTC Gateway on
    OCE Front-End" (p132)
    "For the type of WebRTC gateway select: External on OCE Front-End — External on OCE Front
    End 20 max" (p133)
  summary: |
    安装步骤：FTR 过程自动装 OCE-FE（自动给许可并把版本升到 ≥ R4.0 MD）；ETH1 DHCP 接入后
    浏览器访问 192.168.94.246；全新 IPBox 首连必须定义安装师密码（书中示例 Alcatel1，实验
    口径）；产品类型选 'Frontend WebRTC'，录客户参考号与 IP 参数，FTR 完成后即可与呼叫服务器
    关联。行为规则：对 OCE-FE 网关配置做修改后必须 warm reset 才生效；状态在 Settings 菜单和
    Webdiag 查看；Rainbow 侧网关类型选 "External on OCE Front End"，通道数上限 20。
  conditions: 192.168.94.246 为 FTR 阶段出厂地址（DHCP 模式）；首次密码示例为实验口径
  tags: [checklist, gateway, metric]

- id: p33
  title: OCE-FE 与呼叫服务器双机的 Rainbow PBXID 必须一致；FTR 默认占位 "FleetRef-Installref"；SIP 网关端口核验 5059
  type: rule
  source_pages: p134
  source_chapter: Rainbow WebRTC Gateway on OCE Front-End configuration (OMC)
  source_quote: |
    "The private SIP gateway is automatically created on the OXO Connect call server ; Verify
    port numbers to 5059 in the SIP Gateway parameters
    •On the OXO, by entering an FTR, the PBXID and the activation code are initialized by
    default to 'FleetRef-Installref', which allows the installer to prepare the equipment in
    advance in RB WebAdmin: the OXO will automatically connect to RB at the end of the FTR to
    FleetRef-Install_ID
    Rainbow PBXID must be the same in both OXO Connect, Front-End and call server
    Note: if the Rainbow company was already created put also the PbxId in both OXO
    e.g: PBX9a86-5916-b74a-436c-aec6-c08a-58b6-5bb0" (p134)
  summary: |
    OCE-FE 拓扑的三条配置规则：(1) 私有 SIP 网关会在 OXO Connect 呼叫服务器上自动创建，要在
    SIP Gateway 参数里核验端口到 5059；(2) Front-End 与呼叫服务器两台 OXO 的 Rainbow PBXID
    必须相同（Rainbow 公司已存在时同样要两台都填，PBXID 形如
    PBX9a86-5916-b74a-436c-aec6-c08a-58b6-5bb0）；(3) 出厂 FTR 时 PBXID 与激活码默认是占位符
    "FleetRef-Installref"，供安装员提前在 RB WebAdmin 预备设备，FTR 结束时 OXO 会自动连到
    FleetRef-Install_ID——正式接入前必须替换为平台生成的真实凭证。
  conditions: 适用 OCE-FE 拓扑；占位凭证是出厂态，不是正式接入凭证
  tags: [rule, gateway, onboarding]

- id: p34
  title: OCE-FE 开局场景多样，必须按 MyPortal 最新版《Rainbow WebRTC cookbook》执行
  type: rule
  source_pages: p137
  source_chapter: WebRTC gateway on OCE Front End
  source_quote: |
    "For this it is essential to follow the document 'Rainbow WebRTC cookbook' latest edition
    available on MyPortal ... The commissioning of an OCE-FE can be done with different
    scenarios: New complete installation, PBX + OCE-FE ; Adding OCE-FE to an existing PBX
    (PBX already existing in R4 / Existing PBX version lower than R4) ; Order made WITH or
    WITHOUT Partner fleet reference and Installation reference" (p137)
  summary: |
    规则：OCE-FE 开局至少三类场景（全新整装 PBX+FE、在现有 PBX 上加 FE——又分 PBX 已在 R4 或
    低于 R4、订单带或不带伙伴 fleet 参考/安装参考），每类流程不同，且书内只讲概览——实际开工
    必须以 MyPortal 上最新版《Rainbow WebRTC cookbook》为准。
  conditions: 文档在 MyPortal；书中明确"essential to follow"
  tags: [rule, gateway, checklist]

- id: p35
  title: 外部网关（VM/NUC）部署配置规则：网络四参数 + PBX 地址与 PBXID + TURN 按站点位置；用户需 Business/Enterprise 许可并关联话机
  type: checklist
  source_pages: p141, p142, p144, p145
  source_chapter: External WebRTC gateway - VM deployment / Mini PC
  source_quote: |
    "Configure the Network settings (static or DHCP) • IP , NETMASK, GATEWAY and DNS • Add the
    OXO Connect IP@ and Rainbow PBXID • TURN server configuration according to site location" (p141)
    "Select the option 'Activate the WebRTC gateway' for the company • Define an external
    gateway and the number of channels • The OXO Connect is managed automatically ... Each user
    needs to be granted with either a Business or an Enterprise license • And the Rainbow
    account must be associated to this user PBX phone" (p142)
    "The Software package available on MyPortal contains the OVF files for VMWARE installation,
    and, an ISO file for installation on a mini PC ... Whitelist (Available in the procedure)" (p144)
  summary: |
    VM（ESXi 部署 .ovf）与 NUC（ISO 装 USB 启动盘，可用 RUFUS 制作）步骤一致，配置四件事：
    网络参数（静态或 DHCP：IP/掩码/网关/DNS）、OXO Connect IP 地址与 Rainbow PBXID、TURN 服务器
    按站点位置配置（书内不展开）。Rainbow 管理侧：为公司激活网关、定义为外部网关并设通道数，
    OXO 侧自动管理。用户前提：每人 Business 或 Enterprise 许可 + Rainbow 账号已关联其 PBX 话机。
    防火墙白名单在安装手册中。
  conditions: 软件包从 MyPortal 下载；NUC=Next Unit of Computing
  tags: [checklist, gateway, deployment]

- id: p36
  title: 容量规划对照表：用户数 → 网关通道数（外部与集成/FE 两列，逐行）
  type: metric
  source_pages: p147
  source_chapter: Dimensioning
  source_quote: |
    "Number of Rainbow Users with VOIP Option | Number of trunk channels in Rainbow WebRTC GW &
    SIP trunk (recommended) | Number of Rainbow Users with VOIP Option
    External (OXO and OCE) | Integrated or Front End | Integrated (OCE)
    5    5/5    5
    10   7/7    10
    20   11/11  20
    30   15/15  30
    50   20/20  50
    70   27/NA  70(*)
    100  36/NA  100(*)
    150  50/NA  150(*)" (p147，原文为四列表格，斜杠分隔两列通道数)
  summary: |
    逐行转写（这是全书最易抄错的表）：
    | Rainbow VoIP 用户数 | 外部 GW 通道数(OXO & OCE) | 集成/FE GW 通道数 | (集成侧对应用户数) |
    | 5   | 5  | 5  | 5     |
    | 10  | 7  | 7  | 10    |
    | 20  | 11 | 11 | 20    |
    | 30  | 15 | 15 | 30    |
    | 50  | 20 | 20 | 50    |
    | 70  | 27 | NA | 70(*) |
    | 100 | 36 | NA | 100(*)|
    | 150 | 50 | NA | 150(*)|
    读法：外部网关按用户数线性增配通道（150 用户配 50 通道打满）；集成/FE 网关到 50 用户/20
    通道封顶，再往上通道列为 NA。带 (*) 的行：集成 OCE 的用户上限取决于所配通道数与用户话务
    量——表中值是按 20 通道配置的指示值，上限 150 仅在极低话务量下成立。售前/交付按此表报通
    道数，超 50 用户的 OCE 站点改用外部网关拓扑。
  conditions: 通道数同时对应 Rainbow WebRTC GW 与 SIP trunk 的推荐值；(*) 行为话务量相关的指示值
  tags: [metric, capacity, gateway]

- id: p37
  title: 硬上限三件套：外部 GW 最多 50 路通话；OCE 集成与 OCE-FE 最多 20 路；OXO Rainbow VoIP 用户上限已从 50 提到 150
  type: metric
  source_pages: p147
  source_chapter: Dimensioning
  source_quote: |
    "50 VoIP calls maximum if the WebRTC gateway is external on Mini PC or ESXi server
    20 VoIP calls maximum with OCE integrated WebRTC gateway or if the WebRTC gateway is
    external on OCE Front End
    •External WebRTC GW topology is also supported on OCE when more WebRTC channels are needed
    (max 50)
    Maximum of OXO users with Rainbow VoIP option increased from 50 to 150
    •Applies for both OXO Connect and OXO Connect evolution ... Maximum limit is 150 that is ok
    in case of very low traffic" (p147)
  summary: |
    三条硬上限：外部网关（迷你 PC 或 ESXi）最多 50 路 VoIP 通话；OCE 集成网关与 OCE Front End
    外部网关最多 20 路；OXO 用户的 Rainbow VoIP 选项上限从 50 提高到 150（OXO Connect 与 OXO
    Connect Evolution 都适用，且 150 上限只在极低话务量下成立）。溢出路径：OCE 需要更多通道时
    改用/加用外部网关拓扑（最多 50）。
  conditions: 上限单位为并发 VoIP 通话路数（channels/calls）
  tags: [metric, capacity, gateway]

- id: p38
  title: UTL 许可口径：Deskphone + Free Rainbow 虚拟副站 = 1 UTL；纯 Anydevice = 1 UTL
  type: metric
  source_pages: p156
  source_chapter: Configure Anydevice/Rainbow virtual terminals
  source_quote: |
    "Notes ­ Deskphone + Free Rainbow virtual terminal = 1 UTL ­ Anydevice only = 1 UTL" (p156)
  summary: |
    许可核算公式：有物理话机 + Rainbow 应用（Multiset：物理主站 + Free Rainbow in Twinset 虚拟
    副站）合计占 1 个 UTL；无物理话机的 Anydevice 纯软终端也占 1 个 UTL。Twinset 的价值就是
    UTL Bypass——R6.0 起副站不再额外吃许可（对照 p123）。报许可数量时按"每个电话用户 1 UTL"
    口径算。
  conditions: Free Rainbow in Twinset 从 R6.0 起（R5.2 前副站用 Anydevice，许可口径不同需核查 TC2479）
  tags: [metric, licensing, gateway]

- id: p39
  title: 话务台排队容量：OXE 最多 10 路、OXO Connect 最多 8 路；保持呼叫数取决于副线资源（OXE REX 10 / OXO Anydevice 8，最低 R6）
  type: metric
  source_pages: p164, p169
  source_chapter: Attendant console
  source_quote: |
    "Call queue management - Manage up to 10 calls for OXE - And up to 8 calls for OXO Connect" (p164)
    "The number of calls that can be put on hold, depends on the multi-line resources assigned
    to the Attendant's softphone line: REX on OXE (Up to 10 calls) - Any Device on OXO Connect
    (minimum R6 version Maximum 8 calls" (p169)
  summary: |
    两组数字：Attendant 控制台的呼叫队列容量 OXE 10 路 / OXO Connect 8 路；话务员软电话线可
    保持的呼叫数由所配多线资源决定——OXE 用 REX（最多 10 路），OXO Connect 用 Any Device（最低
    R6 版本，最多 8 路）。售前按 PBX 类型报队列容量。
  conditions: OXO Connect 侧 Any Device 需最低 R6 版本
  tags: [metric, capacity, attendant]

- id: p40
  title: 话务台使用前提：每个使用成员须有 Attendant 订阅；仅 Web/Desktop 可用（手机不可）；话务员须有电话线 + VoIP 软电话能力
  type: rule
  source_pages: p164, p169
  source_chapter: Attendant console
  source_quote: |
    "Members & attendant must belong to the same supervision groups (administrator) ... An
    Attendant subscription is required for each member using this feature • Available on the
    Rainbow Web and Desktop applications • Attendant console not available on mobile. It
    delivers Business/Enterprise services. • An Attendant user must have a telephone line, as
    well as VoIP softphone capability" (p164)
    "The attendant may have a deskphone, but none of the functionalities are possible on the
    deskphone itself. • Same behaviour for a smartphone — Attendant features are only available
    on PC (thick client or web mode)" (p169)
  summary: |
    规则四条：(1) 被监督成员与话务员必须在同一监督组（管理员建）；(2) 每个使用话务台功能的
    成员都要分配 Attendant 订阅；(3) 话务台只在 Web 和 Desktop 客户端可用，手机端不可用——
    话务员即使有物理话机或智能手机，话务台功能也无法在其上操作，全部在 PC（客户端或网页）上；
    (4) 话务员必须有一条电话线并具备 VoIP 软电话能力。OXE 侧参照 TC2462，OXO 侧参照 TC2479。
  conditions: 话务台交付 Business/Enterprise 服务；OXE/OXO 均可用
  tags: [rule, attendant, licensing]

- id: p41
  title: 监督组规格：每监督员最多 5 个组；每组（监督员+被监督人合计）最多 30 人；监督员须 Attendant 许可
  type: metric
  source_pages: p167
  source_chapter: Supervision groups
  source_quote: |
    "In order to supervise the members of a company, users with the attendant subscription, and
    the supervised members must belong to a supervision group. Each supervision group includes •
    One or several supervisors: they must be granted an Attendant license to use the attendant
    console • The company members to supervise
    Maximum number of supervision groups for a supervisor | Maximum number of users in a group
    (supervisors + supervised) : 5 | 30" (p167)
  summary: |
    硬规格：一个监督员最多进 5 个监督组；一个组内监督员 + 被监督成员合计最多 30 人；组内可含
    多名监督员，凡用话务台的监督员都必须有 Attendant 许可。建组路径：客户公司 → Communication
    → Supervision → Create。组按页签呈现，未显示的组有呼叫时红点提示，可开音频通知，另有一个
    页签复现监督员收藏夹（p168）；可拦截被监督用户的来话、可强制/取消其转接（如转语音信箱）。
  conditions: 监督组是 Rainbow 侧概念，与 OXO ACD 组无关
  tags: [metric, capacity, attendant]

- id: p42
  title: 代接/拦截限制：仅当监督员与被监督人在同一 PBX；仅限电话呼叫（不含 Rainbow 软电话呼叫）
  type: rule
  source_pages: p169, p171
  source_chapter: Attendant console / Mutual aid supervision group
  source_quote: |
    "Interception is only possible if supervisors and supervisees are on the same PBX. Only
    phone calls can be intercepted." (p169)
    "As supervisor, you will be notified of telephone calls intended for supervised users. •
    You can pickup calls — Works only for PBX calls, not for Rainbow softphone calls" (p171)
  summary: |
    两条代接边界：(1) 拦截（代接）只在监督员与被监督人同属一个 PBX 时可行；(2) 只能代接 PBX
    话机呼叫，Rainbow 软电话呼叫不能代接。给客户设计互助/秘书场景时，跨 PBX 或纯软电话用户
    不在代接覆盖范围内。
  conditions: 监督/代接功能配置细节见 TC2462（OXE）/ TC2479（OXO Connect）
  tags: [rule, attendant]

- id: p43
  title: 互助监督组规则：一键进出、临时纳排成员、可锁定末位成员；监督应用最多 4 路来话
  type: rule
  source_pages: p171, p172, p173, p180, p181
  source_chapter: Mutual aid supervision groups
  source_quote: |
    "You can supervise two types of group. •Groups that are permanently affiliated to you
    •Groups that you can join on an ad hoc basis in one click at times. You can also temporarily
    integrate or exclude a supervised user." (p171)
    "Up to 4 calls supervised ... Join/leave the group — Locked: cannot leave" (p172)
    "Create a mutual aid supervision group in the same way as you create a « classic » one. •
    The type must be: Mutual aid group ... Define the supervisor role & In/Out permission for
    both profiles" (p173)
    "Type Mutual aid group ; Lock the last member Yes/no" (p180)
    "These members must have a physical extension or an associated PBX softphone (IPDSP or
    MicroSIP)." (p181)
  summary: |
    互助组与经典组建法相同，区别是 Type 选 "Mutual aid group"，并为监督员/成员两种角色分别定义
    进出（In/Out）权限。行为规则：监督员对两类组——长期归属组与可一键临时加入/退出组；可临时
    把某被监督成员纳入或排除（适合成员忘记进组就离开的情况）；建组时可设 "Lock the last
    member"（是/否），被锁定的成员不能退出组；监督应用界面同时最多监督 4 路来话。被监督成员
    必须有物理分机或已关联的 PBX 软电话（IPDSP/MicroSIP）。代接仍受 p42 的同 PBX/仅电话呼叫
    限制。
  conditions: 互助组代接同样仅限 PBX 电话呼叫（p171）
  tags: [rule, attendant]

- id: p44
  title: 用户问题上报与日志：用户端 "Report a problem"，集成商与管理员看到同一份报告
  type: rule
  source_pages: p184, p185
  source_chapter: Maintenance
  source_quote: |
    "Your users can report problems they encounter directly in their Rainbow interface ('Help
    and Support' menu, 'Report a problem'). When reporting, they indicate: • The date* and time
    of the incident • The description of the problem • Attachments ... • Agreement for the use
    of their logs by support ... The integrator partner has the same reports as the customer, so
    he can help with end user support. * In web mode, the date is not requested because the logs
    in a browser are short-lived." (p185)
    "Click on your avatar in the top left-hand corner of your Rainbow application, then on
    'About Rainbow'" (p184)
  summary: |
    运维规则：用户日志入口为头像 → About Rainbow → Open logs；用户可从 "Help and Support" 菜单
    直接上报问题（日期时间、描述、截图/视频等附件、同意支持使用日志）。管理员在公司管理界面
    查看所有用户的事件并可取事件日志；关键点：集成商伙伴能看到与客户完全相同的报告——可据此
    参与一线支持。网页端上报不要求填日期（浏览器日志存活期短）。
  conditions: 用户上报需勾选日志使用同意
  tags: [rule, maintenance]

- id: p45
  title: 云服务状态页 status.openrainbow.com：24/7 监控、可订阅告警并按主题/地域过滤；维护通知按地域与架构（Hybrid/Hub）推送
  type: rule
  source_pages: p186, p187
  source_chapter: Maintenance / Cloud service availability
  source_quote: |
    "A dedicated 'Operations' team constantly monitors the smooth running of the Rainbow
    platform (24/7). ... The button « Get updates » allows ... you can subscribe to alerts by
    different methods. ... If you subscribe to alerts, you can filter by relevant topics and/or
    geographical areas. For France, it is useful to tick WW, EMEA & DE." (p186)
    "Notifications consider your geographical location, as well as your architecture (Hybrid,
    Hub), so as not to display anything that doesn't concern you. ... (most operations are
    carried out in the evening, or over the weekend)" (p187)
  summary: |
    状态页规则：数据中心故障看 status.openrainbow.com；"Get updates" 可订阅告警，按主题与地理
    区域过滤（书中建议法国站点勾 WW、EMEA & DE）。管理门户的计划维护板块按你的地域与架构
    （Hybrid/Hub）过滤通知、用颜色区分关键/非关键影响，多数维护安排在晚间或周末——可据此
    提前通知用户。
  conditions: 告警订阅渠道多种（邮件等）
  tags: [rule, maintenance]

- id: p46
  title: 告警阈值可自定义（音质劣化/无音）；管理端操作全量入历史，可按类别/类型/日期过滤
  type: rule
  source_pages: p188, p189
  source_chapter: Maintenance / Alarms & History
  source_quote: |
    "You can set alarm thresholds to notify you of audio quality degradation and the absence of
    audio." (p188)
    "All administration operations are archived in a history at your disposal. • This is
    especially useful if several administrators are working in parallel, in order to check who
    did what, and when. • Different filters allow you to select the operations you are looking
    for (category, type of operation and date)." (p189)
  summary: |
    两条运维抓手：(1) 可设置告警阈值，在音频质量劣化和无音频两种情况发生时收到通知；(2) 所有
    管理操作都归档进操作历史（History of operations），多管理员并行时用来追溯"谁在什么时候做了
    什么"，支持按类别、操作类型、日期过滤。
  conditions: 告警阈值细节见书中链接文档
  tags: [rule, maintenance]

- id: p47
  title: SR 开具前提：伙伴必须持有 Rainbow 认证；入口为邮件/Emily BOT/Welcome Center/电话；MyPortal 建单字段清单
  type: rule
  source_pages: p191, p192, p193
  source_chapter: Maintenance / Open a Service Request
  source_quote: |
    "Support entry points can be : Mail : support@openrainbow.com • Emily BOT • Global Welcome
    Center is the main point of contact for all ALE International Partners.
    ALE.WelcomeCenter@al-enterprise.com • Or phone call
    The ESR will only be created if the partner is certified on Rainbow" (p191)
    "Connect to MyPortal • Support > Service Request • Click on Create SR: • SR category=
    Rainbow • SR type = product support • Severity • Subject • Mail + Description" (p192)
  summary: |
    规则：只有 Rainbow 认证伙伴提交的 ESR 才会被受理——交付团队要先完成认证。入口四种：
    support@openrainbow.com 邮件、Emily BOT、Global Welcome Center
    （ALE.WelcomeCenter@al-enterprise.com，ALE 国际伙伴主入口）、电话。MyPortal 建单要填：
    SR 类别=Rainbow、类型=product support、严重级、主题、邮箱+描述、终端客户公司名、产品类别
    =Rainbow、Rainbow 版本、详情、子类别、Rainbow SIP trunk、来源（客户现场/Beta/演示等）、
    客户内部参考号。
  conditions: 需 MyPortal 账号
  tags: [rule, maintenance, support]

- id: p48
  title: Teams 集成规则：工作站级集成；订阅须 Business/Enterprise；权限收敛为仅 Telephony
  type: rule
  source_pages: p196, p208, p234, p235
  source_chapter: Integration with Microsoft Teams
  source_quote: |
    "The integration is done at the workstation level" (p196)
    "User must have one of these subscriptions: • Business • Enterprise ; Permissions to limit
    Rainbow collaboration features as collaboration services will be provided natively by Teams
    itself" (p208)
    "As the user will use Teams for all collaboration services, Rainbow will only provide
    telephony integration services. So, it is better to apply a restrictive permission to users
    with Teams integration in order to forbid collaboration services from Rainbow. ... Assign
    the 'telephony' permission to the user." (p234)
    "For Rainbow integration with Teams, a Business or Enterprise subscription is required." (p235)
  summary: |
    三条设计规则：(1) 集成粒度是工作站级（workstation level），按台配置而非租户级；(2) 用户
    订阅必须 Business 或 Enterprise；(3) 权限建议收敛——协作服务（聊天/会议/文件）由 Teams 原生
    提供，Rainbow 侧只保留 "Telephony" 权限，把 Rainbow 协作功能禁掉，避免双入口混乱。
    Rainbow App in Teams 管电话功能（拨号盘/呼叫历史/留言/电话设置），Rainbow Desktop 管点击
    外呼（热键，如 F6）与单路呼叫控制。
  conditions: Teams 租户侧策略（应用权限策略等）在书外
  tags: [rule, teams, licensing]

- id: p49
  title: Teams 内 Rainbow App 依赖 Rainbow Desktop 应用在 PC 上安装并保持运行；SSO 非必需；权限同意两法
  type: rule
  source_pages: p207, p209, p226, p228, p239, p241
  source_chapter: Integration with Microsoft Teams
  source_quote: |
    "Rainbow App availability • Can be present by default in App store • Uploaded by the
    administrator if not present ... Permissions consent • Can be directly authorized by the
    administrator" (p207)
    "Rainbow desktop application is required and must be running" (p209)
    "This method is the simplest and most logical. The connection on Teams clients will be done
    without any message asking to accept the application's permissions." (p226)
    "It is then possible for the administrator to validate the permissions required not only for
    himself but for the entire organization by checking the specific option box." (p228)
    "THE RAINBOW APPLICATION INTEGRATED INTO TEAMS REQUIRES THE INSTALLATION AND STARTUP OF THE
    RAINBOW DESKTOP APPLICATION ON THE PC." (p239)
    "SSO is not required to use the Rainbow/Teams connector." (p241)
  summary: |
    部署规则：Teams 应用商店没有 Rainbow App 时管理员上传 zip 包添加，状态须为 Allowed 用户才能
    安装；应用强依赖 Rainbow Desktop 在同一 PC 上安装并运行（未运行时 Teams 内会提示 Start）。
    权限同意两条路：Teams 管理中心直接批准（推荐，用户端不再弹授权提示），或管理员首次登录
    应用时勾选"代表整个组织同意"。SSO 与连接器无依赖（配置了 SSO 时登录凭据复用，但不是前提）。
  conditions: 建议首次从管理员账号添加应用以便完成组织级同意（p239 Tips）
  tags: [rule, teams, deployment]

- id: p50
  title: Teams/Rainbow 在场同步经 Office 365 信息共享激活（日历/在场同步）
  type: rule
  source_pages: p242, p243, p244
  source_chapter: Integration with Microsoft Teams
  source_quote: |
    "For the moment, the calendar/presence synchronization is not set ... Teams presence
    information should be different from Rainbow presence one" (p242)
    "As here we especially want to activate the presence synchronization between Teams and
    Rainbow, we activate the sharing of information with Office 365. ... Synchronization is now
    active." (p243)
    "Rainbow presence status is now synchronized with Teams one" (p244)
  summary: |
    在场同步开关在 Teams 内 Rainbow App 的设置图标里：激活与 Office 365 的信息共享（选择用户
    账号）后，Teams 的在场状态变化同步到 Rainbow。激活前两边状态各自独立（书中先用改状态不
    同步做反证，再激活验证同步）。排障时若客户说"状态不同步"，先查 O365 共享是否激活。
  conditions: 依赖 O365 环境；属于 Rainbow App in Teams 内的每用户设置
  tags: [rule, teams, presence]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 18 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 核查网络前提并用 Pilot 评估 | 有 | p02 | 书内仅有文档指针与工具用途，端口/帶寬具体数值在书外 PDF（已在 conditions 注明） |
| task-02 | 规划创建公司体系（BP/EC、可见性、SSO/TOTP） | 有 | p03, p04, p05, p06, p07, p08 | 覆盖查重/一人一司、BP 专属权限、可见性四级、SSO 清单、密码复杂度、TOTP |
| task-03 | 管理员权责、企业目录、信息频道 | 有 | p09 | 多管理员、目录委托、频道 Enterprise 门槛与强制订阅 |
| task-04 | 开通并分配订阅（月付/预付） | 有 | p01, p10, p11, p12 | 8 种订阅、计费周期、电话订阅门槛、实验口径月付规则 |
| task-05 | 安装 OMC 并首次连接 | 有 | p13 | Expert 模式/证书/首登密码/每客户密码唯一/客户信息必填 |
| task-06 | 修改 OXO 与客户端 IP 规划 | 有 | p14 | 全套参数为实验口径，生产替换（已在条目标注） |
| task-07 | PBXID+激活码接入并验证 | 有 | p15, p16 | 凭证来源/域名默认值、Webdiag "connected with final password" 判据、ccrbagent.log |
| task-08 | 成员管理（四法、设置、删除宽限、密码） | 有 | p17, p18, p19, p20, p21, p07 | 创建四法、CSV 规则、设置七块、10 天宽限与恢复降级、改密踢下线、密码复杂度 |
| task-09 | 分机关联与 RCC 验证 | 有 | p22, p23 | RCC 能力边界（三类动作/音频在话机）、Rainbow number 自动写入规则 |
| task-10 | WebRTC 网关拓扑决策 | 有 | p24, p25, p26, p28, p30, p31, p34 | 网关本质与前提、自动配置边界与版本、Reseller 专属权、集成 GW R3.2、OCE-FE 前提、容量矩阵、cookbook 场景 |
| task-11 | 按拓扑部署网关 | 有 | p29, p32, p33, p35 | HTTPS/SRTP、OCE-FE FTR 安装与 warm reset、PBXID 双机一致/端口 5059、外部 VM/NUC 配置清单（TURN 细节在书外，已注明） |
| task-12 | 按容量表规划通道与上限 | 有 | p36, p37 | p147 表逐行转写 + 50/20/150 三条硬上限 |
| task-13 | 内部网关自动配置执行 | 有 | p25, p26 | 版本前提 R4.0.020.002、自动/手工边界、Reseller 账号操作（p149-154 流程性内容归流程提取器，此处收规则与数值） |
| task-14 | 虚拟终端配置与 UTL 影响 | 有 | p27, p38 | Twinset/Anydevice 版本语义（R5.2/R6.0 分界）、UTL 口径两条公式 |
| task-15 | Attendant 话务台与监督组 | 有 | p39, p40, p41 | 队列 10/8、REX 10 / Anydevice 8、订阅与平台限定、5 组/30 人规格 |
| task-16 | 互助监督组（进出/纳排/代接） | 有 | p42, p43 | 代接同 PBX 且仅电话呼叫、互助组动态进出/锁定/4 路监督 |
| task-17 | 维护体系运用 | 有 | p44, p45, p46, p47 | 用户日志与问题上报、status 页与告警订阅、告警阈值与操作历史、SR 认证前提与字段 |
| task-18 | Teams 集成全流程 | 有 | p48, p49, p50 | 工作站级/订阅门槛/权限收敛、Desktop 依赖与权限同意两法、O365 在场同步 |

**覆盖结论**：18/18 全部有对应条目，无缺口。两点口径说明：
1. task-01、task-11 中的生产化数值（端口、带宽、TURN、防火墙白名单）原书只给外部文档指针（Network Requirements PDF、Rainbow WebRTC cookbook、TC2479），本文件按"书内事实"如实标注为指针，未编造数值。
2. p147 容量表已逐格对照原文转写（外部列 5/7/11/15/20/27/36/50，集成列 5/7/11/15/20 后 NA）；原书密码规则原文仅要求"大写+数字+特殊字符"，未单列小写要求，提取忠实于原文而非任务描述中的转述。
