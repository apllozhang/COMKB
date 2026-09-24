# 原则/清单/规则/公式/数值口径候选 — Rainbow Hub (RAINXTE101EN Sprint 170 Ed16)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号、号段）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: Hub 合规定位四条：GDPR、ISO 27001、欧洲托管、不受 CLOUD Act/US PATRIOT Act 约束
  type: principle
  source_pages: p5
  source_chapter: OVERVIEW / What is Rainbow Hub
  source_quote: |
    "Security and confidentiality • Compliance with GDPR data protection rules • ALE is ISO 27001
    certified, a certification governing requirements for information security, cybersecurity, and
    privacy protection. • Rainbow is a cloud solution created and hosted in Europe (for European
    customers), not subject to the CLOUD Act or the US PATRIOT Act." (p5)
  summary: |
    Hub 的合规卖点是四件套：符合 GDPR 数据保护规则；ALE 持 ISO 27001 认证（信息安全/网络安全/隐私保护）；
    面向欧洲客户在 Europe 创建并托管；不受美国 CLOUD Act 与 US PATRIOT Act 管辖。另配合商务定位：全 OPEX
    按用户订阅、开源架构可集成现有系统。给欧洲客户讲数据主权时按此四条口径。
  conditions: 面向 European customers 的表述；非欧洲区域托管口径书内未展开
  tags: [principle, compliance, gdpr, positioning]

- id: p02
  title: Hub 功能清单硬数字：日历无限、IVR 3 级无限量、组 50 人、话务台 10 路、录音存 2 个月、经理配 N 助理
  type: metric
  source_pages: p8
  source_chapter: OVERVIEW / Rainbow Hub features
  source_quote: |
    "WELCOME SERVICES • Calendars, in unlimited number • Customizable Voice Guides • Automated attendant
    (3 levels max), unlimited number / HUNT GROUPS (Max 50 users/group) ... 'Administrator' role, 'Agent'
    role / ATTENDANT CONSOLE • 10 simultaneous calls – Full softphone / COMMUNICATIONS RECORDINGS • Line,
    Group • Unlimited cloud storage, 2 months / MANAGER / ASSISTANT • 1 Manager – 1 to N assistants"
    (p8)
  summary: |
    概览页数字口径（与后文各章一致）：日历无限个；语音引导可定制；自动话务员最多 3 级、数量无限；hunt
    group 每组最多 50 用户；话务台 10 路并发、全软话机；通信录音按线/组，云存储无限量但只保留 2 个月；
    经理-助理 1 经理配 1..N 助理。
  conditions: "Example - Non-exhaustive list"（p8 自注）；全量以 help.openrainbow.com Features List 为准
  tags: [metric, features, capacity]

- id: p03
  title: Voice 四档订阅组合与话机适配矩阵（Hub 命名体系）
  type: principle
  source_pages: p9, p67
  source_chapter: OVERVIEW / Rainbow Hub user subscriptions & SUBSCRIPTIONS in brief
  source_quote: |
    "VOICE ENTERPRISE The preferred subscription for digital businesses • Telephony on PC/smartphone/
    telephone • Supervision Group interception • Collaboration • Video conferencing / VOICE ATTENDANT ...
    Voice Enterprise + attendant console • Computer telephony only / VOICE PHONE Telephony only •
    Telephony on device or DECT phones only / VOICE BUSINESS ... Telephony on PC/smartphone/telephone •
    Call pickup • Collaboration" (p9)
    "Voice Attendant ... All Voice Enterprise features plus the Attendant Console available on the PC
    Rainbow application. This subscription does not support hardphones. — Devices: PC only" (p67)
  summary: |
    四档逻辑：Voice Phone（仅硬话机/DECT 上的话务，无 Rainbow 应用）→ Voice Business（PC/手机/话机三端
    话务+代接+协作）→ Voice Enterprise（Business 全量+监督代接+视频会议至 120 与会者/49 路视频）→
    Voice Attendant（Enterprise 全量+PC 话务台；不支持硬话机，设备列 PC only）。与混合云命名（Business/
    Enterprise/Attendant）的差异是全部加 Voice 前缀且多出 Voice Phone 档。选型按"端形态+是否要话务台/
    视频会议"对号。
  conditions: Compatible TEAMS 标注见于订阅图（p9）
  tags: [principle, subscription, licensing, naming]

- id: p04
  title: 网络前提以官方 Network Requirements 文章为准（唯一 URL）；文档含更新流程说明与版本变更注
  type: checklist
  source_pages: p37, p41
  source_chapter: NETWORK PREREQUISITES
  source_quote: |
    "Find all the network requirements on the Rainbow support site • Use the following URL to get all the
    information and updates needed to implement Rainbow Hybrid and Rainbow Hub https://help.openrainbow.
    com/hc/en-us/articles/23942019777170-Check-Rainbow-Network-Requirements" (p37)
    "This document details: The ports and protocols used by the Rainbow collaboration, Rainbow hybrid and
    Rainbow Hub solutions • Operating principles and flows • Detailed list of ports and protocols •
    Rainbow domains and associated IP addresses • Bandwidth requirements • Configuration of corporate
    network elements DNS, Proxy, Firewall..." (p41)
  summary: |
    上线前动作：打开固定 URL 的支持文章（Hybrid 与 Hub 通用），拿到：基础设施更新流程说明、上一版
    《Rainbow Network Requirements – Edxx.pdf》以来的变更注（p39：新增公网 IP 与服务器）、协作/混合话音/
    Hub 三块端口协议摘要、两份 PDF（通用版与健康数据托管版）。PDF 正文覆盖端口协议、运行原理与流量、域名
    IP 清单、带宽要求、企业网 DNS/代理/防火墙配置。本教材只给指针，端口表在设备章有一份摘录（见 p34）。
  conditions: 文档按 Edition 迭代，实施前取最新版
  tags: [checklist, network, prerequisites]

- id: p05
  title: Rainbow Pilot 用途：现场连通性 + 按 Collaboration/Conferencing/Hybrid/Hub 用法配比评估承载
  type: rule
  source_pages: p43, p136
  source_chapter: NETWORK PREREQUISITES / Rainbow Pilot & 设备网络要求章
  source_quote: |
    "RAINBOW PILOT allows you to assess your Rainbow connectivity from your location, and the capacity of
    a given location to handle a population of Rainbow users characterized by a flexible mix of usages
    between Collaboration, Conferencing, Hybrid or Hub telephony. • Link: https://pilot.openrainbow.com/
    home" (p43)
    "Use Rainbow Pilot to carry out all the necessary tests to determine whether the network is correct."
    (p136)
  summary: |
    Pilot 是官方在线评估工具（pilot.openrainbow.com/home）：从客户现场测 Rainbow 连通性，并按协作/会议/
    混合话音/Hub 话音的用法配比评估站点可承载用户规模。设备部署章再次点名：判断网络是否合格要做全套
    Pilot 测试。部分测试分区在教材截图中标注 To come（p44）——以工具当时实际分区为准。
  conditions: 售前/勘测工具，不能替代防火墙放行清单
  tags: [rule, pilot, connectivity, capacity, presales]

- id: p06
  title: 建公司前先查重；一个用户不能同时属于两家公司
  type: rule
  source_pages: p48
  source_chapter: RAINBOW HUB COMPANIES / What is a company
  source_quote: |
    "Before you start a company: • Check that the target company does not exist in Rainbow. • To avoid
    possible duplicates, enter the name of the future company in the search bar • A user cannot be part
    of 2 different companies" (p48)
  summary: |
    两条硬规则：(1) 建司前在搜索栏查名防重复；(2) Rainbow 账号以邮箱为身份，一人不能同时是两家公司的成员。
    同公司用户可自由互加联系人看在场与资料；公司间可见性由 Visibility 控制。
  conditions: 全版本通用
  tags: [rule, company]

- id: p07
  title: BP 专属动作四项：Cloud PBX 声明激活、付费订阅、终端声明、电话线加装/携转
  type: rule
  source_pages: p49
  source_chapter: RAINBOW HUB COMPANIES / 2 types of companies
  source_quote: |
    "Most administration operations can be performed by both the Business Partner and the customer
    administrator. However, the following actions can only be performed by the BP: • Declaration &
    activation of a Cloud PBX (or traditional PBX) • Opening of paid subscriptions • Declaration of
    terminals (Deskphones or DECT) • Addition or portability of telephone lines • The customer's
    integration partner must be either a 'DR' or an 'IR'." (p49)
  summary: |
    权责切分：多数管理操作 BP 与客户管理员都可行，但四项 BP 独占——①声明并激活 Cloud PBX（或传统 PBX）；
    ②开通付费订阅；③声明终端（话机或 DECT）；④电话线加装或携转。EC 公司有且只能挂靠一个 BP；客户集成
    伙伴必须是 DR 或 IR（名字显示在 My company/Dashboard）。比混合云教材多出终端声明与电话线两项——Hub
    交付中 BP 卡位更重。客户管理员"点不出"这四类入口属于权限设计，不是故障。
  conditions: 需 BP/经销商账号；经销链 ALE→VAD/DR/IR→EC（p49 层级图）
  tags: [rule, bp, company, licensing]

- id: p08
  title: 公司关键要素分区（信息/成员/订阅/Cloud PBX/群组/管理面）
  type: checklist
  source_pages: p50
  source_chapter: RAINBOW HUB COMPANIES / Key elements of a company
  source_quote: |
    "Informations • Address • Logo, banner • Time zone • … / Members • Personal routines • Telephony •
    Subscriptions • Rights • Tags / Subscriptions • Cloud PBX • Public numbers • Devices • Associated
    with members • Welcome services • calendars ... / Groups • Extensions (members) • DECT SIP •
    Manager/assistant • Supervision • Emergency • Attendant • Business Directory • Analytics • History •
    Alarms • Settings • Visibility • Authentication • Support" (p50)
  summary: |
    公司对象图五组：信息（地址/Logo 横幅/时区…）；成员（例行程序/话务/订阅/权限/标签）；订阅与话务资源
    （Cloud PBX/公网号/设备及成员关联/欢迎服务/日历、语音提示/自动话务员）；群组（成员分机/DECT SIP/
    经理助理/监督/紧急/话务台）；管理面（企业目录/分析/历史/告警/设置-可见性-认证/支持）。开户与交接验收
    按此清单逐块核对。
  conditions: 无
  tags: [checklist, company, inventory]

- id: p09
  title: 可见性四级（PUBLIC/PRIVATE/CLOSED/ISOLATED）行为矩阵；Hub 场景官方力荐 CLOSED（目录搜索理由）
  type: principle
  source_pages: p53
  source_chapter: RAINBOW HUB COMPANIES / Privacy & visibility
  source_quote: |
    "CLOSED : a user from another company cannot see the members of your company, but he can invite them
    via their email address. Your users can't see users outside their company, but they can invite them
    via their email address." (p53)
    "This mode is highly recommended, especially in a Rainbow Hub setting. When performing directory
    searches, users will appreciate finding only their colleagues and entries in their Business Directory,
    and not the entire Rainbow community." (p53)
    "This 'isolated' mode is not recommended as it is very restrictive. ... your users will no longer be
    able to be invited to conferences (bubbles) external to your organization." (p53)
  summary: |
    四级行为矩阵：PUBLIC 双向可见可邀；PRIVATE 外部看不见但可凭邮箱邀请、你的用户不受限；CLOSED 双向都
    看不见、双方都能凭邮箱邀请；ISOLATED 双向完全隔离。Hub 语境新增一条力荐理由：CLOSED 下目录搜索只见
    同事与企业目录条目，不会搜出整个 Rainbow 社区。ISOLATED 不推荐——代价是无法被外部组织邀请进 bubble
    会议。可见性可在 company settings 事后改。
  conditions: 实验公司统一按 Closed 建（p72）
  tags: [principle, visibility, privacy, company]

- id: p10
  title: SSO 协议清单：Azure AD(SAML/OIDC)、ADFS(SAML)、Google Workspace(OIDC)；配置管理员须 Enterprise 级
  type: checklist
  source_pages: p54
  source_chapter: RAINBOW HUB COMPANIES / SSO & authentication method
  source_quote: |
    "you can enable single sign-on (SSO) with your Azure Active Directory, or with your corporate AD
    (ADFS). ... Azure AD - SAML / Azure AD - OIDC / ADFS - SAML / Google Workspace – OIDC ... The
    administrator must have an 'Enterprise' service level" (p54)
    "NB : other methods are possible, subject to ALE confirmation, when they are based on standard
    protocols. For example, with SAML V2 : Shibboleth, RSA, … and with OIDC : LemonLDAP, OKTA, CAS
    APEREO, Ping Identity, …" (p54)
  summary: |
    标准 SSO 四种：Azure AD-SAML、Azure AD-OIDC、ADFS-SAML、Google Workspace-OIDC（后者为 Hub 教材相对
    混合云教材的新增项）。前提：配置管理员持 Enterprise 服务等级。可全公司启用或仅部分用户，一家公司可
    并存多种认证方式按用户指定。列表外 IdP（SAML V2: Shibboleth/RSA；OIDC: LemonLDAP/OKTA/CAS APEREO/
    Ping Identity）基于标准协议时须 ALE 确认。SSO 具体配置用支持站点技术手册（书内给指针）。
  conditions: 依赖客户已有 Azure AD/ADFS/Google Workspace 基础设施
  tags: [checklist, sso, security]

- id: p11
  title: 密码复杂度硬规则：≥12 字符，至少 1 大写、1 数字、1 特殊字符（四处一致口径）
  type: rule
  source_pages: p54, p168, p169, p177
  source_chapter: SSO & authentication / Manual creation / Bulk import / Security
  source_quote: |
    "Traditional authentication with complex password (min 12 characters)." (p54)
    "(At least 12 characters and contain at least 1 uppercase, 1 number, and 1 special character)" (p168)
    "Passwords must be at least 12 characters long and contain at least 1 capital letter, 1 number and 1
    special character." (p169)
    "A password must be at least 12 characters long and contain at least 1 capital letter, 1 number and 1
    special character." (p177)
  summary: |
    全书四处一致的设密口径：长度 ≥12 字符，含至少 1 个大写、1 个数字、1 个特殊字符。原文未单列小写要求
    （12 字符长度实际隐含混合）。适用于邀请自设密码、CSV 批量导入、管理员改密等所有场景；SSO 场景 CSV
    密码列可留空（p169）。
  conditions: Rainbow 原生认证时适用
  tags: [rule, security, metric]

- id: p12
  title: TOTP 双因子需第三方验证器 App，全员可用、特别推荐管理员
  type: principle
  source_pages: p54
  source_chapter: RAINBOW HUB COMPANIES / SSO & authentication method
  source_quote: |
    "Authentication with TOTP (Time-based One Time Password. Users need a third-party authentication
    application (Google Authenticator, Microsoft Authenticator, Authy). This method applies to all types
    of users but is particularly recommended for the administrators" (p54)
  summary: |
    Rainbow 原生认证第二模式 TOTP 动态口令：依赖手机第三方验证器（Google Authenticator、Microsoft
    Authenticator、Authy）。全员可用，管理员账号尤其建议开启。MFA-TOTP 配置参考支持站点文章（书内给指针）。
  conditions: 与 p10 SSO、p11 复杂密码并列的第三种认证方式
  tags: [principle, security, mfa]

- id: p13
  title: Reseller vs Customer 管理员权责矩阵：五项 BP 独占创建 + 客户管理员日常面
  type: rule
  source_pages: p58-60
  source_chapter: ADMINISTRATOR ROLES
  source_quote: |
    "Some elements can only be created by the Reseller's administrator: • The company • Subscriptions •
    Cloud PBX • Public numbers (DID) • Extensions ... Configuration steps: 1. Creation of the client
    company 2. Allocate subscriptions to the company 3. Configuring the 'Communication' parameters
    (Creating the Cloud PBX • Language of voice guides • Associated trunk • Global settings • Configuring
    public numbers • Creating deskphones (MAC addresses))" (p58)
    "Customer administrators can create/modify/delete a large number of parameters related to their own
    company, with the exception of: • Creation of the company • Allocating subscriptions to your company
    • Creation of the Cloud PBX • Create public numbers (DID) • Create extensions" (p59)
    "The 'Roles' tab is used to assign administrative rights to the client company. • It is possible to
    have several administrators to manage the company." (p60)
  summary: |
    两级权责：Reseller 管理员按三步交付——建客户公司 → 给公司分配订阅 → 配 Communication 参数（Cloud
    PBX、语音引导语言、关联 trunk、全局设置、公网号、按 MAC 建话机）；独占创建五项：公司、订阅、Cloud
    PBX、公网号（DID）、分机。客户管理员做其余日常：公司资料、成员与用户声明、设备关联用户、组、专业
    目录、公共频道、欢迎服务、定制引导与音乐、话务台、IVR 等。Roles 页签授管理权、支持多管理员。
  conditions: p49 的"BP 四项专属"与本页"五项独占"口径互补：p58 从"可创建元素"角度又单列 Extensions
  tags: [rule, admin, roles, bp]

- id: p14
  title: 企业目录：默认客户管理员管理、可委托非管理员；手工或 CSV 导入并出报告；提升来电识别
  type: rule
  source_pages: p61
  source_chapter: ADMINISTRATOR ROLES / Business directory
  source_quote: |
    "In addition to a Microsoft Azure Active Directory, you can create a 'Business Directory' containing
    the contacts of external companies or organizations that are useful to all your users, along with
    their phone numbers. • The quality of reception will be improved thanks to the caller identification
    during the call presentation. By default, a customer administrator can manage the directory. You can
    delegate the management to other Rainbow users, who are not necessarily administrators" (p61)
  summary: |
    企业目录存外部公司/组织联系人及号码，改善来话弹屏主叫识别。默认客户管理员可管，可委托给非管理员用户；
    两步：开权限 → 手工创建或 CSV 批量导入（提供样例文件，导入后出报告）。LDAP 连接器也能把 AD 联系人
    自动同步进该目录（p179，见 p43）。
  conditions: 与成员目录（内部同事）相区分
  tags: [rule, directory, admin]

- id: p15
  title: 信息频道：仅 Enterprise 级可创建；强制订阅成员不可退订（公司全员/指定成员两种）
  type: rule
  source_pages: p62
  source_chapter: ADMINISTRATOR ROLES / Information channels
  source_quote: |
    "Only users with an 'Enterprise' service level can create Information Channels. ... Create chains with
    all Rainbow users (members of my company and other companies) / The members you choose in your company
    will automatically be subscribed to these channels. Members will not be able to unsubscribe. / All
    Rainbow members in your company will automatically subscribe to these channels. Members will not be
    able to unsubscribe." (p62)
  summary: |
    频道两步：Roles 页签授权 → 创建。门槛：创建者须 Enterprise 服务等级。强制订阅两种范围——公司全员自动
    订阅、或指定成员自动订阅，两种都不可退订。也有面向本公司+其他公司全体 Rainbow 用户的开放频道。推公司
    通告前先想清楚内容会长期维护，否则频道变成退不出去的骚扰源。
  conditions: 无
  tags: [rule, channel, admin]

- id: p16
  title: 订阅两层流转与计费口径：先公司后成员；按用户计价，月付或预付 1/3/5 年
  type: metric
  source_pages: p65-66, p69
  source_chapter: SUBSCRIPTIONS
  source_quote: |
    "The BP administrator takes out subscriptions for his own company or those of his customers. ...
    The price is per user and different subscription plans are possible: • Monthly • Prepaid 1, 3 or 5
    years" (p65)
    "Subscriptions are first assigned to the client company. Then, these subscriptions are assigned to
    company members by the BP administrator or local administrator. Each member must have a Voice
    subscription to use telephony services: Voice Phone • Voice Business • Voice Enterprise • Voice
    Attendant" (p66)
    "Members are allocated when they are created or modified." (p69)
  summary: |
    流转两层：BP 给客户公司开订阅池 → BP 或本地管理员把订阅分配到成员（建户时或改户时）。计费按用户，
    月付或预付 1/3/5 年。电话服务硬门槛：成员必须持有 Voice 四档之一（纯软话机用户也要 Voice 订阅才能
    配号码）。
  conditions: 第一层为 BP 专属
  tags: [metric, subscription, billing]

- id: p17
  title: 订阅总表逐行：Voice Phone/Business/Enterprise/Attendant/Dial-In Pack/Room/Alert/CRM Connect（8 行）
  type: metric
  source_pages: p67
  source_chapter: SUBSCRIPTIONS / Subscriptions in brief
  source_quote: |
    "Voice Phone — Telephony on hardphone only — All telephony features from a hardphone without access to
    the Rainbow application. — Hardphone only (desktop or DECT) / Voice Enterprise — Voice Business +
    Videoconference + call supervision and pick-up — ... video conferencing features up to 120
    participants and 49 videos. / Voice Enterprise Dial-In Pack — Voice Enterprise + PSTN conference with
    local numbers over 50 countries — ... conference calling for up to 120 participants, with local
    numbers available in over 50 countries. / Rainbow Room — ... Specific Android TV box / Rainbow Alert
    — Optional alerting service plan : bypass Rainbow « Do not Disturb », persistent visual notifications
    and audio beeps, alert acknowledgment. — PC or smartphone / CRM Connect — Make Web or telephone calls
    directly from your CRM system and keep a history of all telephone exchanges in your CRM. — PC only"
    (p67)
  summary: |
    订阅表 8 行逐行要点：①Voice Phone——仅硬话机/DECT 上的全部话务特性，无 Rainbow 应用；②Voice
    Business——话机+Rainbow 应用（PC/手机）全部企业话务特性 + 协作（群消息/在场/文件共享）；③Voice
    Enterprise——Business 全量 + 监督代接 + 视频会议（至 120 与会者、49 路视频）；④Voice Attendant——
    Enterprise 全量 + PC 话务台，不支持硬话机（设备=PC only）；⑤Voice Enterprise Dial-In Pack——
    Enterprise + PSTN 会议本地号码覆盖 50+ 国家、至 120 与会者；⑥Rainbow Room——会议室专用视频会议平台，
    特定 Android TV box；⑦Rainbow Alert——可选告警包：穿透"勿扰"、持续视觉通知+声音提示+告警确认
    （PC 或手机）；⑧CRM Connect——从 CRM 直接网页/电话外呼并把通话历史留存 CRM（PC only）。
  conditions: "Find the detailed offers in the Features List / rainbow plans tab"（p67 指针）
  tags: [metric, subscription, licensing]

- id: p18
  title: 实验口径：培训只用 4 条 Voice Enterprise 月付订阅，禁止年付预付（三处警告）
  type: rule
  source_pages: p17, p68, p74
  source_chapter: TRAINING LAB / Subscriptions / How-To company
  source_quote: |
    "Use ONLY 4 Voice Entreprise MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID !!!" (p17)
    "During LAB Use ONLY Voice MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID!!!" (p68)
    "Assign 4 'Voice Enterprise MONTHLY' subscriptions to the customer company. DO NOT USE 'YEAR
    PREPAID' SUBSCRIPTIONS" (p74)
  summary: |
    实验口径（三处一致）：每公司仅开 4 条 Voice Enterprise MONTHLY，禁止 1/3/5 年预付——避免污染培训
    商务计费。生产环境预付是正常计费方式（p65），该规则仅适用 LAB。
  conditions: 仅 RLAB/虚拟课堂培训环境
  tags: [rule, lab, subscription]

- id: p19
  title: 公司时区强制规则：留言信箱与欢迎服务日历都基于公司时区（How-To Warning）
  type: rule
  source_pages: p73
  source_chapter: How-To Create a Rainbow Hub company / Company information
  source_quote: |
    "Warning It is MANDATORY to define the time zone of the company because the voicemail and the
    calendars of the welcome services are based on it." (p73)
  summary: |
    建司后补录公司信息（规模/行业/网站/时区等）时时区为强制项——语音信箱时间戳与欢迎服务日历都取公司时区。
    实验填 Europe/Paris。日历章（p255）重复此规则："The calendar refers to the company's time zone"。
    公司信息可由该公司管理员后续自行补全（Tips，p73）。
  conditions: 建司流程第 1.2 步；时区错了会影响留言时间与开闭时段判断
  tags: [rule, company, timezone, calendar]

- id: p20
  title: 声明 Cloud PBX 的硬前提：公司至少有一条 Voice Business 或 Voice Enterprise 订阅
  type: rule
  source_pages: p75, p80
  source_chapter: How-To company / Subscriptions management & CLOUD PBX / steps
  source_quote: |
    "Warning IN ORDER TO BE ABLE TO DECLARE A CLOUD PBX FOR THE COMPANY, AT LEAST ONE VOICE SUBSCRIPTION
    IS REQUIRED (VOICE BUSINESS OR VOICE ENTERPRISE)." (p75)
    "To be able to create a Cloud PBX as a communications server, you need at least a 'Voice' license.
    Without this, you'll only see traditional PBXs: OXO Connect, OmniPCX Enterprise, Third party PBX,
    etc." (p80)
  summary: |
    顺序硬约束：给公司声明 Cloud PBX 之前必须至少有一条 Voice 订阅（明确点名 Voice Business 或 Voice
    Enterprise）；没有 Voice 许可时建通信服务器界面里只出现传统 PBX 类型（OXO Connect/OXE/第三方），选不
    到 Cloud PBX。实验中先开 4 条 Voice Enterprise 月付再建 PBX（p74-75）。
  conditions: BP 权限动作（p49）
  tags: [rule, cloud-pbx, subscription, ordering]

- id: p21
  title: Cloud PBX 对应关系两条：一公司一 Cloud PBX；一 Cloud PBX 一外部 SIP trunk；通道与线数无上限
  type: rule
  source_pages: p78, p100-101
  source_chapter: CLOUD PBX / Cloud PBX & How-To declaration
  source_quote: |
    "One Rainbow company = one and only one CloudPBX. One CloudPBX = one and only one external SIP trunk
    (SIP provider). Find the list of certified providers on the Rainbow Help Center website." (p78)
    "Number of call channels: unlimited • Number of telephone lines: unlimited" (p78)
    "Only one Cloud PBX can be declared per customer company." (p100)
    "External trunk Select a trunk group for public calls in the list ... Only one trunk group can be
    associated to the Cloud PBX." (p101)
  summary: |
    拓扑三规则：①一家 Rainbow 公司有且只有一个 Cloud PBX；②一个 Cloud PBX 有且只能关联一条外部 SIP
    trunk（一个 SIP 运营商）；③呼叫通道数与电话线数无上限（由 trunk 侧承载）。认证运营商清单在
    help.openrainbow.com。多站点也遵守"一公司一 PBX"（p92）。
  conditions: 声明入口 Administration/My Customers/Customer companies/<公司>/Communication/Comm. Servers
  tags: [rule, cloud-pbx, sip-trunk, topology]

- id: p22
  title: 编号计划规则：内部 2-9 位可混长度（1xx/3xx/4xxxx…）；出局前缀 0 或 9（国家相关）；免前缀拨叫受国家限制
  type: rule
  source_pages: p81, p95, p101
  source_chapter: CLOUD PBX / Creation & Telephony terminology & How-To
  source_quote: |
    "Mandatory (0 to 9) — From 2 to 9 digits — From 2 to 4 digits — # * 1 to 9 — Several ranges are
    possible — One range only ... Once your Cloud PBX has been created, you'll be able to eliminate the
    need for outgoing prefix on telephone extensions (deskphones & DECT). ... This feature is country
    dependent, please check with ALE" (p81)
    "Internal numbers can be between 2 and 9 digits long, depending on the customer's requirements. • It
    is possible to have numbers of different lengths • e.g. 100 to 120, 2000 to 2136, 756 to 789" (p95)
    "Numbering plan: Outbound prefix Outbound prefix for external calls. Example: 0 or 9 — Prefixes
    Define the first digit of the members phone numbers prefix ... Number of digits Number of digits of
    the numbering plan. Keep here the default value: 3 ... You can mix several dialing plans if required:
    1xx, 3xx, 4xxxx, 6xxxxx…etc" (p101)
  summary: |
    编号计划口径：内部号 2-9 位、可多长度混存（如 100-120 与 2000-2136 共存）；创建 Cloud PBX 时定出局
    前缀（例 0 或 9，国家相关）、成员号首位前缀、号长（默认 3 位），拨号计划可混多段（1xx/3xx/4xxxx/
    6xxxxx）。"优化话机拨叫"选项可让话机/DECT 免拨出局前缀——该特性国家相关，需与 ALE 确认。实验配置：
    前缀 0、号长 3、段 1（100-199）与段 2（200-299）、闭锁无限制（p100）。
  conditions: 编号计划的"设计方法论"（如何为客户规划）书内不讲，只讲参数含义（见 BOOK_OVERVIEW 批判）
  tags: [rule, numbering, cloud-pbx]

- id: p23
  title: Call settings 默认值全表（溢出/邮件通知/闭锁/主叫 ID/紧急/呼转/单复线/录音提示/转移类型）
  type: metric
  source_pages: p82, p102-103
  source_chapter: CLOUD PBX / Call settings & How-To
  source_quote: |
    "Voice mail overflow: Busy/no reply call overflow Validate to overflow on the voicemail in case of no
    answer or choose no overflow ... Activate email sending - No email notification (By default) - Email
    notification with voice message (attachment) - Email notification only" (p102)
    "Emergency calls allowed on softphones — Checked (by default) ... Allow call forward to external
    destination — Check to allow forwarding to external numbers (Deactivated by default) ... Route
    internal calls through the external trunk — Deactivated by default ... Restricted to one call
    (monoline) — Check to switch to monoline instead of multiline (multiline by default) ... Announcement
    profile select the calls for which the voice prompt for call recording will be played: - None (by
    default)" (p102-103)
    "Transfer mode: Attended transfer / Blind transfer — Select transfer type" (p82)
  summary: |
    公司级呼叫设置默认口径：忙/无应答溢出到留言信箱（可关）；留言邮件通知默认"无邮件通知"（可选仅通知或
    带附件）；闭锁允许档位三级（仅内线 / 国内+内线 / 国际+国内+内线）+ 屏蔽档（无/收费号/自定义清单）；
    主叫 ID 策略选用户公网号或公司号、可允许成员自选；软话机紧急呼叫默认勾选；呼转外部目的地默认停用；
    内部呼叫经外部 trunk 路由默认停用；成员分发默认多线（multiline）；录音提示音默认 None；转移类型分
    协商转/盲转。
  conditions: 成员级设置可覆盖公司级（Same as company 选项，p195-196）
  tags: [metric, cloud-pbx, call-settings, defaults]

- id: p24
  title: 公网号码分配面与主号规则：号码可分给成员/组/话务台/欢迎服务/IVR；注入的第一个号码默认为公司主号
  type: rule
  source_pages: p83-84, p103-104
  source_chapter: CLOUD PBX / Public numbers & How-To
  source_quote: |
    "Public numbers are affected to • Company members • Hunting groups and attendant groups • Welcome
    services (Preannouncement) • Automated attendants • One of these number must be assigned as the
    company number ... The 1st number you inject is, by default, the main number of the installation. You
    can change it if necessary." (p83)
    "By default, the first number (or first number of the first range) will be affected as the main public
    number for the company. ... In case of creation of another number (or range of numbers) for this
    company, an option is available to change automatically the main public phone number of this company"
    (p104)
  summary: |
    号码面规则：DDI 号/号段分配给成员、hunt group 与话务台组、欢迎服务（预通告）、IVR；其中一个必须定
    为公司号码。首个注入的号码（或首段首个）默认成为公司主号，可改；再建新号/新段时有选项自动切换主号。
    号段创建：勾"Create a range of public numbers"+定段大小（实验 10，p103-104）。外呼主叫 ID 可选用户
    公网号或公司号（p84 示例：101 显示 0298131001、102 显示公司号 0298131000）。
  conditions: 号码由集成伙伴负责分配注入（p83 原注）；实验号段 02982967X0-X9 为实验口径
  tags: [rule, public-numbers, did, caller-id]

- id: p25
  title: 流量控制规则：白/黑名单按前缀、国际格式不带 + 或 00、可整公司或按用户生效
  type: rule
  source_pages: p85-87
  source_chapter: CLOUD PBX / Traffic control
  source_quote: |
    "In addition to the existing traffic barring mechanisms, the admin is able to manage his own lists.
    •Each list contains a list of prefixes: •Whitelist: only dialed number starting with these prefixes
    are authorized for outbound calls •Blacklist: all dialed number starting with these prefixes are
    forbidden for outbound calls. These lists apply either to the entire company, or to specific users."
    (p85)
    "Create the prefixes in international format, without '+' or '00' in front. For example, to ban all
    French premium rate numbers starting with 0825, enter '33825'." (p86)
  source_chapter_note: p87 为成员视图（Telephony 页签内的呼出闭锁）
  summary: |
    三条规则：①白名单=仅这些前缀开头的被叫可外呼，黑名单=这些前缀开头的一律禁呼；②清单可作用于全公司或
    指定用户；③前缀按国际格式录入、前头不带 + 或 00（禁法国 0825 收费号录 33825）。成员侧在 Telephony
    页签可查/配自己的呼出闭锁（p87）。
  conditions: 与既有闭锁机制（Allowed/Blocked calls 档位）叠加使用
  tags: [rule, barring, traffic-control, security]

- id: p26
  title: Hub 商务模式两分：bundled（一单一发票）vs separated（两单两票）；PSTN 服务不由 ALE Rainbow 团队订购管理
  type: principle
  source_pages: p88
  source_chapter: CLOUD PBX / Trunk SIP
  source_quote: |
    "Rainbow Hub offer is built jointly with a Business Partner/Traffic provider who is in charge to
    provide the voice traffic and manage the customer. PSTN service is not ordered nor managed by ALE
    Rainbow team. Depending on the capability of the Business Partner ... • A bundled offer where the
    customer: Signs a single contract including the 'Rainbow Hub' and the 'Voice traffic' with his partner
    and receives a single invoice. • A separated offer where the customer: Signs two contracts" (p88)
  summary: |
    商务原则：Hub 报价由 BP/话务伙伴联合构建——话务由伙伴提供、客户由伙伴管理；PSTN 服务不在 ALE Rainbow
    团队的订购与管理范围内。合同两型：bundled=Hub+话务一单一发票；separated=Hub 一单+运营商话务一单，
    两张发票。报价与合同设计时先问清走哪型。
  conditions: 认证运营商清单在 help.openrainbow.com（p78/p88 链接）
  tags: [principle, business-model, sip-trunk, pstn]

- id: p27
  title: 带宽估算口径：Rainbow 客户端信令可忽略、Opus 音频 80 kbps、VP8 视频 1.5 Mbps(720p30)、SIP 设备 G711 64 kbps；瓶颈在 SIP trunk 段
  type: metric
  source_pages: p90
  source_chapter: CLOUD PBX / Prerequisites
  source_quote: |
    "To size the needed outgoing network bandwidth, the following points must be considered: • Support of
    OPUS codec in PSTN calls from a Rainbow client. Flows Codec Typical Bandwidth (One way): Signalization
    of the Rainbow client NA Negligible / Audio & video media flow of the Rainbow client Opus for audio
    VP8 for video — 80 kbps / 1,5 Mbps (720p at 30 fps) / Signalization of the SIP device NA Negligible /
    Audio flow of the SIP device G711 64 kbps ... Bandwidth must be considered at this level [Premises—
    SIP trunk 段]" (p90)
  summary: |
    带宽四行表（单向）：Rainbow 客户端信令可忽略；客户端音视频 Opus 80 kbps / VP8 1.5 Mbps（720p/30fps）；
    SIP 设备信令可忽略；SIP 设备音频 G711 64 kbps。前提说明：PSTN 呼叫中 Rainbow 客户端支持 OPUS。带宽
    核算位置在客户 premises 到 SIP trunk 段（图中标注）。完整带宽要求仍以 Network Requirements 文档为准。
  conditions: 书内为指示性口径；生产按官方文档核算
  tags: [metric, bandwidth, codecs, network]

- id: p28
  title: 多站点参数规则：副站点用户禁改主叫、呈现公司号设 Not allowed；每站可配站点主号与站点 MoH
  type: rule
  source_pages: p92-93, p303-304
  source_chapter: CLOUD PBX / Multi-sites & MULTI-SITE CLOUD PBX
  source_quote: |
    "Note: here there is only one Rainbow company, and therefore only one Cloud PBX. Having an internal
    number range for each site makes it easier to find your way around the Rainbow administration, but
    it's not mandatory." (p92)
    "Select whether the user will be able to present the company number (set to 'Not allowed' for users
    outside the main site)." (p93)
    "When members linked to a site without an assigned public number make outgoing calls, the public
    number seen by the called party is the site's public number. • Custom music on hold per site." (p303)
  summary: |
    多站点参数四条：①仍是一公司一 Cloud PBX；②每站内部分机号段分段便于管理但非强制；③副站点用户在
    Telephony 页签单独管理——主叫改写权限与"呈现公司号"按需设（主站点之外的用户建议 Not allowed）；④站点
    默认公网号：未配个人号的站点成员外呼显示站点号；站点级 MoH 覆盖公司级。不变量见 f30。
  conditions: 全部 DDI 仍归公司号码池（All the company's DDI numbers are available，p93）
  tags: [rule, multi-site, caller-id, moh]

- id: p29
  title: 实验环境参数全表（账号/公司/号段/成员/MicroSIP/RLAB 网络）
  type: metric
  source_pages: p13-34
  source_chapter: TRAINING LAB ENVIRONMENT
  source_quote: |
    "POD1 Client-P1 0298296710 to 0298296719 0298296710" (p17)
    "POD1 alice1.rv1@ale-training.com ... 101 0298296711 X [Client Administrator]" (p18)
    "Local (Principal) 332982900P1 — National 331409500P1 — Mobiles 336050400P1 — International
    442056700P1" (p22)
    "Host name: Client1 • IP Address: 192.168.1.10 • Mask: 255.255.255.0 • Gateway: 192.168.1.254 • DNS
    Server 1: 192.168.1.250" (p34)
  summary: |
    实验口径速查：每 POD（1-6，特殊 8）一家公司 Client-PX（X=POD 号），BP 账号 bpX.rv1@ale-training.com
    （密码问讲师）；公司公网号段 02982967X0-X9（10 个号，X0 为主号）；4 名成员 alice/bob/carol/dave
    X.rv1@ale-training.com（内线 101-104、公网号 02982967X1-X4、密码 Superuser-P*（实验口径）、alice 任
    客户管理员）；培训邮箱 mail44.lwspanel.com（登录=邮箱、密码 PasswordP*，实验口径）；MicroSIP 公网号
    规则 332982900P1/331409500P1/336050400P1/442056700P1；RLAB 客户机 Client1 192.168.1.10/24、网关
    192.168.1.254、DNS 192.168.1.250、NAS 12.0.0.2。
  conditions: 全部为实验口径，生产按客户实情替换
  tags: [metric, lab, accounts, numbering]

- id: p30
  title: 设备谱系数字：M7 3.5" 超宽频仅免提、M5 2.8"、M3 1.6"；EM200 扩展 10 页×20 键；PoE 等级与接口
  type: metric
  source_pages: p107
  source_chapter: DEVICES RANGE / ALE devices range
  source_quote: |
    "Audio: Super wideband quality x* x* x* [* Only in speakerphone mode] ... Bluetooth 4.1 headset
    connectivity x [M7] ... Screen Colour screen 3,5'' | 2,8'' | 1,6'' ... Extension module EM200 For
    M3-M5-M7 desktop phones Colour screen, Up to 10 pages of 20 LED keys ... Port (headset, extension,
    wifi…) USB-A/USB-C | USB-A/USB-C | USB-A/USB-C | RJ9 ... Power supply PoE class 2 | PoE class 2 | PoE
    class 2 | PoE class 1" (p107)
  summary: |
    话机参数锚点（Myriad M7/M5/M3 + ALE-2）：M7/M5/M3 超宽频仅免提模式（x*）；M7 独有 BT4.1 耳机；彩屏
    3.5"/2.8"/1.6"；M 系可用 EM200 扩展模块（彩屏、最多 10 页×20 LED 键，USB-A 连接）；M 系端口 USB-A/
    USB-C，ALE-2 为 RJ9；供电 M 系 PoE class 2、ALE-2 class 1；全部有千兆 PC 口（M 系与 ALE-2，图内 x 标注）。
  conditions: "the descriptions on this site are generic and do not necessarily apply to the Rainbow Hub context"（p107 对外链自注）；采购口径以产品目录为准
  tags: [metric, devices, myriad, hardware]

- id: p31
  title: Zero-Touch 技术红线：每用户仅一台物理 SIP 设备；DHCP option 43/66/67 会破坏 zero-touch；禁用设备自带 web 管理页配置
  type: rule
  source_pages: p134, p136-137
  source_chapter: DEVICES INSTALLATION / Myriad deskphones & Network requirements & First installation
  source_quote: |
    "Designed for Zero-Touch deployment. Centrally configured and managed via Rainbow administration
    interface. Only one physical SIP device per user account" (p134)
    "IMPORTANT The device can obtain its IPv4 parameters via DHCP (this is the simplest method). If the
    device receives a specific management URL in option 43, 66 or 67, Rainbow Hub's 'zero touch'
    mechanism will be broken, as the DHCP option will take precedence. It is recommended to disable these
    options in the DHCP server ... If it is not possible to disable them, the link distributed by the
    DHCP server should be: https://rdd.openrainbow.com" (p136)
    "Unless you have a very specific need (e.g. Static IP), you must never program the device via its own
    web admin (keys, etc.). Proper operation is only guaranteed by the 'zero touch' mechanism." (p137)
  summary: |
    zero-touch 三条红线：①每个用户账号只能有一台物理 SIP 设备；②DHCP option 43/66/67 会以优先级覆盖
    zero-touch 指向——必须在 DHCP 服务器上禁用；实在禁不了，下发的管理 URL 必须是 https://rdd.openrainbow.
    com；③除极特殊需求（如静态 IP）外，禁止用设备自带 web 管理页配按键等——正确运行只由 zero-touch 机制
    保证。设备按 MAC 关联成员后自动取配置与固件（约 5-10 分钟、可能多次重启，p137）。
  conditions: 适用 Myriad/ALE-2/DECT zero-touch 线；Generic SIP 无此机制
  tags: [rule, zero-touch, dhcp, provisioning]

- id: p32
  title: 设备网络端口表（逐行）：TCP 5061 / TCP 443 / UDP 30000-44999 / UDP 53 / UDP 123 / TCP 22 → *.openrainbow.com
  type: metric
  source_pages: p136
  source_chapter: DEVICES INSTALLATION / Network requirements
  source_quote: |
    "Protocole Port Usage Source Destination — TCP 5061 SIP over TLS SIP device *.openrainbow.com — TCP
    443 Config & APIs SIP device *.openrainbow.com — UDP 30000-44999 SRTP media SIP device; Rainbow
    softphones (web & thick client) *.openrainbow.com — UDP 53 DNS SIP device DNS server — UDP 123 NTP SIP
    device pool.ntp.org — TCP 22 SSH (si activé) SIP device" (p136)
  summary: |
    防火墙放行表逐行：TCP 5061（SIP over TLS，话机→*.openrainbow.com）；TCP 443（配置与 API）；UDP
    30000-44999（SRTP 媒体，来源含话机与 Rainbow 软话机 web/厚客户端）；UDP 53（DNS）；UDP 123（NTP，指向
    pool.ntp.org）；TCP 22（SSH，若启用）。前提不满足的五类故障：取不到软件版本、注册失败（No Service）、
    Rainbow Admin 配的功能键不下发、DND 不同步、未编程却出现 Headset 键。注册成功判据：屏上已注册用户名
    前绿点。
  conditions: 原文 "SSH (si activé)" 为法语残留（=若启用）；媒体段 UDP 30000-44999 需在防火墙特批
  tags: [metric, network, ports, firewall, devices]

- id: p33
  title: 设备首装两线：DHCP 自动线（5-10 分钟多次重启、TFTP 抢先禁忌、Config Failed）与静态 IP 线（出厂密码 123456、已配 Hub 设备须恢复出厂）
  type: checklist
  source_pages: p137-138
  source_chapter: DEVICES INSTALLATION / First installation DHCP & without DHCP
  source_quote: |
    "A Myriad device cannot start up in Cloud mode if a PBX is present on the LAN where the device is
    connected: TFTP will be given priority. A device that is not assigned to a user will not retrieve its
    configuration ('Config Failed' message during initialization), nor the firmware version specific to
    Rainbow Hub." (p137)
    "Enter in Menu, and «Advanced settings», «Network», «IP Config», «IPv4 settings». Factory password:
    123456. Same process if web admin : admin/123456 ... In the special case of a device already
    configured for Rainbow Hub: to access advanced settings and enter a Static IP, you need to perform a
    factory reset on the device (long press on the conf key)" (p138)
  summary: |
    DHCP 线四个要点：出厂软件版本与 Hub 所需不同，关联用户后自动升级（可能多次重启，约 5-10 分钟）；LAN
    内有 PBX 时 TFTP 抢先导致起不了 Cloud 模式；未分配用户的设备取不到配置（初始化报 Config Failed）也
    取不到 Hub 专用固件。静态线：菜单 Advanced settings → Network → IP Config → IPv4 settings（出厂密码
    123456，web 页同 admin/123456），填 IP/掩码/网关/DNS（8.8.8.8 或其他，DNS 必须可用）；已配过 Hub 的
    设备要先进"高级设置"必须长按 conf 键恢复出厂。
  conditions: 静态 IP/特定 VLAN 属特殊需求场景
  tags: [checklist, devices, installation, dhcp, static-ip]

- id: p34
  title: 设备维护口径：已注册设备禁直连；debug 会话 ≤15 分钟、admin+一次性 TOTP 口令；webadmin 报告需固件 ≥2.14.22、日志 24h 自动失效
  type: metric
  source_pages: p142-145
  source_chapter: DEVICES MAINTENANCE
  source_quote: |
    "Once a Myriad device is registered and active in the Rainbow Hub environment, it is impossible to
    connect to it, even if you know its IP address (for obvious security reasons). • As an administrator,
    you can activate a debug session, for a maximum duration of 15 minutes. ... The login is always
    'admin', but the password is one-time use only (TOTP)." (p142)
    "Enable device logs (Auto deactivation after 24h) ... Click on Get the device report to publish the
    device logs. Report available in the BP report admin section. require at least the the following
    firmware on the device: 2.14.22" (p144)
    "If necessary, the administrator can launch actions on the device: Debug • Restart the device • Reset
    to factory the device" (p145)
  summary: |
    维护四口径：①注册激活后的话机禁直接连接（即使知道 IP）；管理员可开 debug 会话，最长 15 分钟，登录名
    固定 admin、密码为一次性 TOTP；②设备日志两条路——话机本地（Log Level Debug → 起 pcap 抓包 → 复现 →
    Local Log Download 出 .tgz + 停 pcap 下载 → 恢复 Error 级，p143）与管理端 webadmin（编辑设备启用设备
    日志，24 小时自动失效，Get the device report 出报告进 BP report admin 区，要求设备固件至少 2.14.22）；
    ③远端维护动作三件：Debug/重启/恢复出厂；④web 抓包页含 Maintenance 区（改日志级别免重启、tcpdump、
    恢复出厂，p336）。
  conditions: 日志级别忘恢复 Debug 会导致设备行为异常带延迟（p143，详见 n 系）
  tags: [metric, maintenance, logs, debug, devices]

- id: p35
  title: DECT 容量与硬件数字：8328 双站 20 机 10 路；8368 254 站 40 机/站 1000 机；半径 50-300m；室外 IP55；CAT-iq 告警服务器 F24/Newvoice(+Tamat)
  type: metric
  source_pages: p148-150
  source_chapter: DECT MOBILITY
  source_quote: |
    "8328 ... • 1 or 2 base stations/site • Up to 20 DECT handsets ... Compact design • 95 x 93 x 24 mm
    ... • Network interface : Ethernet 10/100, PoE / Coverage • Range 50 to 300m ... Up to 20 handsets
    and 10 simultaneous calls." (p149)
    "8368: Up to 254 base stations • Up to 40 handsets/base stations ... Indoor DECT base station • 144 x
    140 x 35 mm ... Outdoor DECT base station • 365 x 210 x 65 mm ... • IP55 ... Up to 1000 handsets (40
    per base station) • Up to 10 simultaneous calls per base station" (p150)
    "The SIP-DECT 8328/8368 base station can communicate locally with an alarm server (CAT-iq protocol) :
    alarm escalation from a terminal to the server, sending of an alarm message from the server to the
    terminals. Validated servers: F24, Newvoice (+ in progress: Tamat)" (p149, p150)
  summary: |
    容量逐格：8328——1-2 站/点、≤20 手持机、10 路并发、95×93×24mm、以太网 10/100 PoE；8368——≤254 站、
    40 手持机/站、全系统 1000 手持机、10 路并发/站；室内 144×140×35mm 壁挂内置天线，室外 365×210×65mm
    IP55 外置天线；两档覆盖半径均 50-300m、站间无缝切换。告警对接：CAT-iq 协议本地告警服务器（终端上报告
    警、服务器下发告警消息），已验证 F24、Newvoice，Tamat 验证中。
  conditions: 手持机 8262（PTI）面向恶劣环境/独行工人保护（p149-150）
  tags: [metric, dect, capacity, hardware]

- id: p36
  title: Generic SIP 六条限制 + 安全基线（TLS 1.2+SRTP 强制、G711 推荐、防火墙三放行）+ ALE 不为大规模第三方话机兜底
  type: rule
  source_pages: p116-121
  source_chapter: GENERIC SIP DEVICES
  source_quote: |
    "Generic SIP devices: • No centralized configuration • Must be configured manually • No automatic
    firmware updates • No remote call control (RCC) • Basic SIP telephony services" (p117)
    "Mandatory security • TLS 1.2 minimum for signaling • SRTP enabled for the media stream • Encryption
    can be disabled if the device does not support it properly • Audio • G711 codec recommended •
    Connectivity • The firewall must allow: SIP signaling • RTP/SRTP Traffic • Internet access toward
    Rainbow services." (p118)
    "The intention behind this feature is not to support large-scale deployments of third-party SIP
    DeskPhones. However, it can be used to integrate existing devices when appropriate. ALE cannot
    provide support for such configurations" (p120)
  summary: |
    规则三组：①限制六条——无集中配置、全手工、无固件自动更新、无 RCC、仅基础 SIP 话务、协议生态互操作
    风险（p120 还列 CLI 显示、无统一在场、不能从 Rainbow 应用控话机、DND/呼转/BLF 键状态冲突）；②安全
    基线——信令 TLS 1.2 起步、媒体 SRTP（设备不支持时可关加密）、推荐 G711、防火墙放行 SIP 信令+RTP/
    SRTP+出网到 Rainbow；③立场——定位存量设备补充（门铃/传真/会议话机/ATA/DECT base，p116），不做大规模
    第三方话机部署、ALE 不提供支持（p120/121）。
  conditions: 8 款参考设备指南（Yealink CP925/T3、Snom D385/D335、Poly Edge B30/Trio C60、Grandstream
    GRP2603P/DP750+DP720/HT812，p122）；无官方互操作认证计划（p122）
  tags: [rule, generic-sip, security, limitations]

- id: p37
  title: 成员五通道与门槛：AAD 导入限 Voice Enterprise 管理员；LDAP 连接器免费、用户同步单向且只同步付费许可
  type: rule
  source_pages: p167, p170, p179
  source_chapter: COMPANY MEMBERS / Members creation & Azure AD & LDAP connector
  source_quote: |
    "Import via Azure Active Directory is reserved for administrators with 'Voice Enterprise' service
    level" (p167)
    "NB: the link you establish with your Azure Active Directory does not trigger automatic user
    provisioning (creation, modification, deletion). This remains a manual operation at your initiative,
    via a specific mass import (CSV file)." (p170)
    "This connector can be installed freely at any customer's premises who wishes to have it. ...
    Automatic synchronization of Rainbow users. Creation, modification, deletion, on a regular basis of
    your choice. • Unidirectionnel : AD to Rainbow. • Only users with a paid license are synchronized."
    (p179)
  summary: |
    门槛三则：①AAD 批量导入/同步只对 Voice Enterprise 服务等级管理员开放；②AAD 与公司的关联本身不触发
    自动供应——建/改/删仍是管理员主动经 CSV 批量导入做；③LDAP 连接器（AD Synchronization）免费安装在客户
    Windows server：三功能可自选——用户同步（AD→Rainbow 单向、按所选周期建/改/删、仅同步持付费许可的
    用户）、AD 联系人自动进企业目录、与 Exchange Server 同步日历在场（等价于 161 版之前 Exchange online/
    Office 365 已有功能）。
  conditions: CSV 需 UTF-8；SSO 时 CSV 密码列留空（p169）
  tags: [rule, members, azure-ad, ldap, licensing]

- id: p38
  title: 语音信箱开通与容量：分配号码即开通留言信箱，容量 30 分钟
  type: metric
  source_pages: p172
  source_chapter: COMPANY MEMBERS / User telephony settings
  source_quote: |
    "A voicemail box is assigned to the member as soon as a telephone number is assigned to him. 30min
    storage capacity" (p172)
  summary: |
    两条：成员一分到电话号码就自动配语音信箱；留言信箱容量 30 分钟。公司级溢出（忙/无应答转信箱、邮件
    通知档位）与成员级覆盖（Same as company/Yes/No）见 p23/p102。
  conditions: 无
  tags: [metric, voicemail]

- id: p39
  title: 删除成员 10 天宽限：恢复后回落 Essential 免费档，须重配订阅与电话线；10 天内邮箱不可复用
  type: rule
  source_pages: p176, p168
  source_chapter: COMPANY MEMBERS / Members deletion & Manual creation
  source_quote: |
    "When you delete a user, his or her status becomes 'Suspended' for a period of 10 days (called the
    'grace period'). When deleted, the user's subscription was automatically removed. If you restore it,
    it will default to 'Essential' (free) mode, so you'll need to reallocate the appropriate license ...
    It will also be necessary to reassign the user's telephone line. ... Without any action from you, the
    account will be deleted after 10 days." (p176)
    "If you get an error message about the e-mail address you wish to use, please check that it is not
    already the identifier of a user deleted less than 10 days ago (grace period)." (p168)
  summary: |
    删除规则：删后账号 Suspended 10 天（宽限期），可恢复或彻底删，不动作 10 天后自动永久删。恢复的代价：
    删除时订阅已自动回收，恢复后默认 Essential（免费）——要重新分订阅、重新挂电话线。副作用：10 天内被删
    账号的邮箱不能用于新建账号（p168 报错提示）。
  conditions: 宽限期固定 10 天
  tags: [rule, members, lifecycle]

- id: p40
  title: 管理员改密立即踢在线用户下线（防冒用）；改登录邮箱不丢账号历史
  type: rule
  source_pages: p177
  source_chapter: COMPANY MEMBERS / Security: password & login
  source_quote: |
    "If the user is logged in at the time you make the password change, he/she will be logged out
    immediately. This is very useful if you suspect that a Rainbow account is being spoofed. ... Change
    the login email if necessary, without losing the account history." (p177)
  summary: |
    Security 页签三操作：改密（守复杂度）、改登录邮箱（保留账号历史）、改认证方式。行为规则：改密瞬间该
    用户在线会话立即登出——处置疑似盗号的标准手段；日常批量改密要避开工作时间并提前告知。
  conditions: 全版本通用
  tags: [rule, security, members]

- id: p41
  title: Hunt group 参数组：50 人/组、一内线（必）+一 DDI（选）、轮转 10 秒、队列溢出 10-900 秒可调、FCFS 延迟 10 秒、组空即溢出选项
  type: metric
  source_pages: p211-215
  source_chapter: HUNT GROUPS / Services & Parameters & Waiting queues
  source_quote: |
    "50 users per group ... One Internal number (mandatory) and one DDI number (facultative) can be define
    per group ... A member/agent can step withdraw. Withdraw from Rainbow app or a prog. Key on the phone.
    ... Forbid the last member from withdrawing" (p212)
    "Choose distribution type: • Parallel • Serial, overflow after 10s • Circular, overflow after 10s ...
    Members • Limit: 50 members ... Immediate call overflow when the group is empty" (p213)
    "the oldest call on hold is presented (first come, first served), after a 10 sec delay • If the
    waiting time exceeds the overflow time (adjustable from 10 to 900 sec)" (p215)
  summary: |
    参数全集：每组上限 50 成员（成员可跨多组）；每组一内线号（必填）+一 DDI（选填）；Serial/Circular 轮转
    定时默认 10 秒；坐席可随时退组（应用内或话机可编程键），可设"禁止最后一名成员退组"；带队列组 FCFS 派
    号延迟 10 秒、溢出等待 10-900 秒可调、可设组空立即溢出；溢出目的地 8 种（留言/成员/语音提示/组/欢迎
    服务/内线/外线/AA）。呼叫录音可在组级开（p235：all/external/internal/none）。
  conditions: 图示页另标无队列组溢出默认 60 秒（p211，实验口径参考）
  tags: [metric, hunt-group, queue, capacity]

- id: p42
  title: Manager/Assistant 规则：单经理多助理、仅电话呼叫被筛、经理 DID 挂组级、溢出提示音 5-30 秒
  type: rule
  source_pages: p219-221
  source_chapter: MANAGERS/ASSISTANTS GROUPS
  source_quote: |
    "Only telephone calls are filtered. If Rainbow audio calls are allowed, they are not filtered. ...
    This type of group is necessarily single-Manager. To create a multi-Manager group, it is necessary to
    create several groups (an assistant can belong to different groups)." (p219)
    "The DID of the Manager who wants to be able to screen his calls must be assigned to the group level,
    and not to the manager. ... In the case of overflow to a Voice prompt, you can customize it to adapt
    the message to the situation. 5 to 30 sec" (p221)
  summary: |
    四条规则：①组必然单经理——多经理=建多组，助理可跨组（1 助理管多经理即此实现）；②只筛电话呼叫，
    Rainbow 音视频呼叫不筛；③经理要筛选自己来话，其 DID 必须配在组级而非经理个人名下；④溢出到语音提示
    可定制文案、时长 5-30 秒。组管理同 hunt group（内线/公网号/录音/溢出/成员/提示音）。应用角色：经理
    （接听/仅通知/开停筛选）、助理（开停筛选/代接/管多经理）。
  conditions: 组可作欢迎服务/AA/其他组溢出的目的地（p219）
  tags: [rule, manager-assistant, filtering, did]

- id: p43
  title: 监督/话务台规格：监督员分级权限（Attendant 含 10 路排队）；5 页签/30 人/5 组；Attendant 用户无话机无移动端
  type: metric
  source_pages: p224, p246
  source_chapter: SUPERVISION GROUPS & Attendant console
  source_quote: |
    "A supervisor must have one of the following levels of service: • Voice Attendant : Supervision-Pickup-
    Transfer & 10 Calls in queue • Voice Business & Enterprise : supervision-pickup-transfer. Limits: • 5
    supervision tabs for one user • 30 members in a group (Supervisors + Supervisees) • A user can be a
    supervisor in up to 5 groups" (p224)
    "Warning: Members with voice attendant subscriptions cannot use: • Attendant mode on the Rainbow
    mobile application • Their telephone set. If configured: the phone set association is deleted after
    activation of the attendant console." (p246)
  summary: |
    规格三组：①监督员订阅分级——Voice Attendant 得完整话务台（监督-代接-转移+10 路排队）；Voice
    Business/Enterprise 只有监督-代接-转移；②硬限制——每用户 5 个监督页签、每组（监督员+被监督者）30 人、
    一人最多当 5 组监督员；③Voice Attendant 用户设备限制——不能用手机端话务台、不能用话机，激活话务台后
    话机关联会被删除。话务台另可改被监督成员的例行程序、10 路保持、三档显示（Normal/small/condensed）。
  conditions: 话务台在 PC Rainbow 应用（p67：Voice Attendant 设备=PC only）
  tags: [metric, supervision, attendant-console, limits]

- id: p44
  title: 紧急号码规则：按国家+trunk 自动配置、免出局前缀、受闭锁用户也放行、号码保留不可改不可占作内线
  type: rule
  source_pages: p227-229
  source_chapter: SUPERVISION GROUPS / Emergency numbers & group & localization
  source_quote: |
    "Numbers automatically configured according to • Company country • Trunk group associated with the
    Cloud PBX. Allows calls to emergency numbers • Without dialing the outbound prefix. i.e. '9' • For
    users subject to external barring • Members with only authorized intra-PBX calls ... Emergency numbers
    are reserved and cannot be changed. You cannot assign them as internal numbers to users. For example,
    in a 3-digit numbering plan you cannot propose 112 in Europe" (p227)
    "Only one emergency group. Active or not • Activation made by the administrator (BP / customer) ...
    To transfer an emergency call to the public emergency number, emergency group members must dial the
    emergency number preceded by the external prefix (e.g. 0112)." (p228)
    "Rainbow doesn't manage DID location in this model where DIDs are managed by the Business Partner.
    Business Partners have to declare DID addresses into the SIP provider database ... Identification of
    the relevant Public-Safety Answering Point (PSAP) is under the responsibility of the SIP provider."
    (p229)
  summary: |
    规则五条：①紧急号码表按公司国家+Cloud PBX 关联的 trunk 组自动配置（国家缺失时联系 ALE 并提交该国监管
    号码表）；②免出局前缀可拨，且对受外呼闭锁（含仅内线）用户放行；③号码保留——不可改、不可占用作内线号
    （3 位编号计划里欧洲不能拿 112 当内线）；④唯一一个紧急组，激活后免前缀紧急呼叫路由到组而非外线，组员
    转公共紧急号要加前缀（例 0112）；⑤定位责任链——BP 购号时把 DID 地址登记进 SIP 运营商数据库，PSAP 判定
    由运营商负责，Rainbow 不管 DID 定位。紧急呼叫可录音（p227）。
  conditions: 紧急组=打了 emergency 标记的标准组，配置同 hunt group
  tags: [rule, emergency, compliance, psap]

- id: p45
  title: 录音存储与访问：保留 2 个月；Recordings 页签仅最终客户管理员可见；不占用户配额；Rainbow Exporter 付费按日归档到 Google Drive/SFTP
  type: metric
  source_pages: p231
  source_chapter: SUPERVISION GROUPS / Call recording
  source_quote: |
    "RECORDINGS ARE STORED FOR 2 MONTHS. The 'Recordings' tab is only accessible by the end-customer
    administrator of the solution, for confidentiality reasons. The storage of records does not impact the
    storage quota of users. Note: for customers with legal archiving needs beyond 2 months, it is
    possible on request to implement 'Rainbow Exporter', which copies all recordings daily to Google
    Drive, or to a customer's own SFTP storage server, in addition to traditional Rainbow licenses
    (pricing on request)." (p231)
  summary: |
    四条口径：保留 2 个月；Recordings 页签仅最终客户管理员可见（保密理由——BP 都看不到）；录音存储不占用户
    存储配额；超 2 个月归档走 Rainbow Exporter（按日全量拷贝到 Google Drive 或客户自有 SFTP），属另行付费
    的可选件（pricing on request）。
  conditions: 组级录音范围在组编辑页配（all/external/internal/none，p235）
  tags: [metric, recording, retention, compliance]

- id: p46
  title: 欢迎服务素材限制：语音提示文件 ≤4MB、问候 ≤120 秒、单用途最多 5 条引导；定制提示最多 5 条、特殊日最多 10 天
  type: metric
  source_pages: p260, p263-264
  source_chapter: WELCOME SERVICES / Custom prompts & Voice prompts
  source_quote: |
    "MAXIMUM : 5 — MAXIMUM : 10" (p260，定制语音引导页两处上限标注)
    "They can be replaced by customized voice prompts in wav, mp3, ogg,… formats ... Audio file must not
    exceed 4MB. greeting file must not exceed 120 seconds" (p263)
    "Multiple voice guides can be loaded for a single use (maximum: 5)." (p264)
  summary: |
    素材限制：自定义提示音支持 wav/mp3/ogg 等格式；音频文件 ≤4MB；问候文件 ≤120 秒；单一用途可挂多条
    引导但最多 5 条；欢迎服务的定制时段提示最多 5 条、特殊日最多 10 天（p260 两处 MAXIMUM 标注）。预置
    提示音按语言/国家提供（MoH、录音、目的态、日历、话务台、IVR、组等），可替换亦可回退默认。
  conditions: 播放方式可设循环或单次（p264）
  tags: [metric, voice-prompts, welcome-services]

- id: p47
  title: IVR 规格：3 级上限、根菜单 10 项 0-9、无数量与许可限制、"唯一提示"模式建后不可改；IVR 直挂 DDI 则 7×24
  type: rule
  source_pages: p266, p270
  source_chapter: WELCOME SERVICES / Automated attendant
  source_quote: |
    "Each IVR has a maximum of 3 levels, each allowing a DTMF selection from 0 to 9. • The root menu
    contains 10 configurable entries. ... An automated attendant can be reached via a dedicated public
    number or via a welcome service. • Direct call via DDI (in this case, the IVR is in service 24/7) ...
    You can create as many IVRs as you like - there are no limits or licenses on this service" (p266)
    "Menus with single voice prompts ... This option is highly recommended (cannot be changed later)."
    (p270)
  summary: |
    五条规格：①每 IVR 最多 3 级；②每级 DTMF 0-9、根菜单 10 项可配；③IVR 数量无限制、无许可（与话务台的
    Voice Attendant 订阅形成对照）；④两种入口——直挂公网号（DDI 直达即 7×24 服务）或经欢迎服务（受日历
    控制，此时 IVR 不带 DID）；⑤语音提示两模式——每菜单一条唯一提示（强烈推荐但创建后不可改）或每选项+
    每动作分条录音。
  conditions: 保密规则：来话显示默认名而非欢迎服务技术号（p269）
  tags: [rule, ivr, aa, limits]

- id: p48
  title: 日历规则：引用公司时区；法定假日不预填；特殊日时隙优先于常规日；可复制天与整历
  type: rule
  source_pages: p255-256
  source_chapter: WELCOME SERVICES / Calendars
  source_quote: |
    "You can set • As many calendars as you need • One or more opening time slots • Open 24/24 • Closed
    24/24 • Duplicate days • Duplicate calendars • Define as many specific days as needed. A calendar is
    based on a calendar which manages the opening and closing hours for each day of the week and the
    specific days of opening or closing. The calendar refers to the company's time zone" (p255)
    "Note: Public holidays are not pre-filled. ... Define special days (the schedules of these days will
    have priority over those of the usual days)." (p256)
  summary: |
    日历五条：数量不限；每天可多个开站时段（含 24 小时开/24 小时闭）；可复制天、复制整历；特殊日数量不限
    且其时隙优先于常规星期几；法定假日不预填——必须手工录（如圣诞，p278 实验）。日历引用公司时区（联动
    p73 时区强制规则）。
  conditions: 同一日历可被多个欢迎服务共用（p278）
  tags: [rule, calendar, welcome-services]

- id: p49
  title: CDR 口径：ALE 不计费不开票；入/出/内部呼叫出月度 .csv，纯 VoIP 呼叫不产生；每月 1 日提供；BP 三通道获取
  type: rule
  source_pages: p318
  source_chapter: ANALYTICS / Call detail record
  source_quote: |
    "ALE doesn't calculate the cost or invoice the public telephonic consumption. • This is ensured by
    the Business Partner providing the SIP trunk connectivity to the public network • However, the voice
    services provide the needed Call Detail Records (CDR) permitting this calculation. They are generated
    (.csv) for all calls going through the Cloud PBX • Incoming, outgoing and internal calls are taken
    into account • Pure VoIP Rainbow audio/video call doesn't generate CDR ... Each month, the first, ALE
    provides Call Details Records in a file. Three ways for the partner to obtain these files • ALE pushes
    monthly mails with attached files • The BP retrieve manually the files using his account through
    Rainbow web interface • The BP retrieve automatically the files using REST APIs. For details refer to
    the document TBE099_Rainbow Hub - Voice services" (p318)
  summary: |
    CDR 五条：①计费与开票由提供 SIP trunk 的 BP 负责，ALE 不做；②话单覆盖经 Cloud PBX 的入/出/内部呼叫；
    ③纯 Rainbow VoIP 音视频呼叫不产生 CDR；④每月 1 日 ALE 出话单文件；⑤BP 三通道获取——月度邮件附件/
    网页手工下载/REST API 自动拉取。细节见 TBE099_Rainbow Hub - Voice services 文档。
  conditions: 话单格式与字段在 TBE099（书外）
  tags: [rule, cdr, billing, analytics]

- id: p50
  title: 分析口径：仪表盘 7/30 天可导 CSV；Voice 周期最长 1 年；欢迎服务统计 ≤5 个；组对比 ≤5 组；成员级统计可按组关闭
  type: metric
  source_pages: p319-326
  source_chapter: ANALYTICS / Global dashboard & Voice tab & Groups
  source_quote: |
    "To follow the evolution of your users' uses (adoption rate), either over the last 7 days or over the
    last 30 days. You can export the data in CSV format." (p319)
    "Choice of period (1 year maximum)" (p320)
    "Statistics for one or more Welcome services (max 5), over a period of your choice" (p322)
    "Analyse up to 5 groups in a single view, over a period of your choice" (p326)
    "For reasons of sensitivity specific to each country and/or customer, a company administrator may
    disable individual statistics for a specific group. When disabled, data is still collected at server
    level, but group administrators have no access to it." (p325)
  summary: |
    五条口径：全局仪表盘看近 7/30 天采纳率等指标、可导 CSV；Voice 页周期最长 1 年，可按呼向（内/入/出）×
    目的地（用户/组/欢迎/AA）过滤；欢迎服务统计一次最多 5 个服务（最忙日/时段/星期、开闭目的地话务量）；
    组分析一次最多 5 组同屏（来话/接听/等待/时长四类×各 4 图）；成员级统计可被公司管理员按组关闭（各国/
    客户敏感度差异），关闭后服务器仍采集但组管理员无权查看。IVR 统计含主叫停留时长（min/avg/max）与取消
    呼叫数（p323）。
  conditions: MOS 阈值见 p52
  tags: [metric, analytics, dashboard, privacy]

- id: p51
  title: MOS 质量票：呼叫结束默认采集；推荐阈值抖动<30ms、RTT≤150ms、丢包≤1%
  type: metric
  source_pages: p328
  source_chapter: ANALYTICS / Call quality technical data
  source_quote: |
    "All calls (telephone or Internet) Quality tickets are collected at the end of a call (enabled by
    default). The MOS scores are integrated into the audio quality dashboards. ... Reminder of recommended
    values: • Jitter: under 30ms the level is acceptable • RTT: latency must not exceed 150ms to ensure
    good quality • Packet loss: must not exceed 1%" (p328)
  summary: |
    质量三口径：所有呼叫（电话或互联网）结束即采集质量票（默认启用）；MOS 分并入音质量仪表盘，支撑逐用户
    排障与网络/防火墙问题定位；推荐阈值——抖动 <30ms 可接受、RTT ≤150ms 保好质量、丢包 ≤1%。
  conditions: 技术明细页可过滤精确定位
  tags: [metric, mos, quality, network]

- id: p52
  title: SR 受理前提：伙伴须持 Rainbow Hub 认证；入口四种；MyPortal 两页字段（Product Category=Rainbow Hub）
  type: rule
  source_pages: p341-343
  source_chapter: MAINTENANCE / Access to Rainbow support & Creating SR
  source_quote: |
    "Support entry points can be: • Mail: support@openrainbow.com • Emily BOT • Global Welcome Center is
    the main point of contact for all ALE International Partners. • ALE.WelcomeCenter@al-enterprise.com •
    Or phone call. The ESR will only be created if the partner is certified on Rainbow Hub." (p341)
    "Connect to MyPortal • Support > Service Request • Click on Create SR: • SR category= Rainbow • SR
    type = product support ... • Product Category = Rainbow Hub • Rainbow Version • Details • Sub
    category • Rainbow SIP trunk • How found (Origin): Customer site, Beta, demo… • Customer Internal Ref
    • Contact: Global welcome center" (p342-343)
  summary: |
    支持三则：①入口四种——support@openrainbow.com 邮件、Emily BOT、Global Welcome Center
    （ALE.WelcomeCenter@al-enterprise.com，ALE 国际伙伴主入口）、电话；ESR 只为认证 Rainbow Hub 的伙伴
    创建；②MyPortal 建单第一页：SR category=Rainbow、type=product support、严重级、主题、邮箱+描述；
    ③第二页：终端客户公司名、Product Category=Rainbow Hub（与混合云教材的 "=Rainbow" 不同）、Rainbow
    版本、详情、子类、Rainbow SIP trunk、发现来源（客户现场/Beta/演示）、客户内部参考号、联系人=Global
    welcome center。
  conditions: 需 MyPortal 账号
  tags: [rule, support, sr, certification]

- id: p53
  title: 实验账号与密码口径：BP/成员/培训邮箱三层账号（密码问讲师 / Superuser-P* / PasswordP*）
  type: metric
  source_pages: p17-18, p191-198
  source_chapter: TRAINING LAB & How-To members
  source_quote: |
    "Accounts Password — POD1 bp1.rv1@ale-training.com Ask to Trainer" (p17)
    "alice1.rv1@ale-training.com Ask to Trainer ... [实验中成员密码实际使用] Password: Superuser-P*"
    (p18, p191)
    "https://mail44.lwspanel.com/ — Login: userP.rv1@ale-training.com — Password: PasswordP*" (p192)
  summary: |
    实验口径三层账号：①BP 管理员 bpX.rv1@ale-training.com（表中密码"Ask to Trainer"）；②成员/客户管理
    员 alice/bob/carol/dave X.rv1@ale-training.com（实验步骤用 Superuser-P*）；③培训邮箱
    mail44.lwspanel.com（登录=邮箱、密码 PasswordP*）。收信注意平台邮件可能被判 SPAM（p192 警告）。生产
    化一律替换为客户实情。
  conditions: 全部为实验口径
  tags: [metric, lab, accounts]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 24 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 网络前提与 Pilot | 有 | p04, p05, p27 | 文档体系、Pilot 用途、带宽口径；设备端口表见 p32 |
| task-02 | 公司创建 | 有 | p01, p06, p09, p10, p11, p12, p19, p29 | 合规定位、查重/一人一司、可见性、SSO、密码、TOTP、时区强制 |
| task-03 | 管理员权责、目录/频道 | 有 | p13, p14, p15 | 权责矩阵、目录委托、频道门槛与强制订阅 |
| task-04 | 订阅开通分配 | 有 | p03, p16, p17, p18, p20 | 四档逻辑、两层流转、8 行订阅表、实验月付、声明前提 |
| task-05 | Cloud PBX 声明配置 | 有 | p20, p21, p22, p23 | 声明前提、一二一规则、编号计划、Call settings 默认值 |
| task-06 | 号码分配与主叫策略 | 有 | p24 | 分配面、主号规则、主叫 ID 两选 |
| task-07 | 流量控制与闭锁 | 有 | p25 | 白黑名单三条规则与格式 |
| task-08 | trunk 商务与带宽 | 有 | p26, p27, p04 | bundled/separated、带宽四行表 |
| task-09 | 多站点规划 | 有 | p28 | 站点参数四条 |
| task-10 | 成员管理 | 有 | p37, p38, p39, p40, p11, p29, p53 | AAD/LDAP 门槛、信箱 30 分钟、宽限期、改密踢人、密码、实验账号 |
| task-11 | 设备部署 | 有 | p30, p31, p32, p33 | 谱系数字、zero-touch 红线、端口表、首装两线 |
| task-12 | 设备维护日志 | 有 | p34 | debug 15 分钟/2.14.22/24h 口径 |
| task-13 | Generic SIP 接入 | 有 | p36 | 六限制+安全基线+立场 |
| task-14 | DECT 部署 | 有 | p35 | 容量与硬件逐格 |
| task-15 | Hunt Group 与队列 | 有 | p41 | 参数全集 |
| task-16 | Manager/Assistant | 有 | p42 | 四条规则 |
| task-17 | 话务台与监督组 | 有 | p43 | 分级权限、5/30/5、设备限制 |
| task-18 | 紧急号码与组 | 有 | p44 | 五条规则+责任链 |
| task-19 | 录音与归档 | 有 | p45 | 2 个月/仅客户管理员/Exporter |
| task-20 | 欢迎服务全家桶 | 有 | p46, p48, p19 | 素材限制、日历规则、时区联动 |
| task-21 | IVR 配置 | 有 | p47 | 五条规格 |
| task-22 | 多站点配置 | 有 | p28, p24 | 站点参数+号码池共用 |
| task-23 | 分析体系 | 有 | p49, p50, p51 | CDR、仪表盘口径、MOS 阈值 |
| task-24 | 维护支持体系 | 有 | p52 | SR 前提与字段 |

**覆盖结论**：24/24 全部有对应条目，无缺口。两点口径说明：
1. 生产化数值（完整端口/带宽/防火墙清单、DID 登记流程、CDR 字段、话机互操作测试）原书只给外部文档指针（Network Requirements 文章、TBE099、TBE127、支持文章），本文件按"书内事实"如实标注，未编造数值。
2. p67 订阅表、p136 端口表、p211-215 组参数、p148-150 DECT 容量均已逐格对照原文转写；实验值（p29/p53）全部标注"实验口径"；原文笔误照录并注明（p136 "si activé"、p144 "the the"、p179 "Unidirectionnel"）。
