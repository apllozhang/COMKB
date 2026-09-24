# 术语/缩写/产品名候选 — Rainbow OXO Connect (RAINXTE001EN Ed13)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 62 条（超出预估 30-45，因任务要求全量提取，订阅 8 种与经销角色 5 个均单列）。DDI/ARS/UTL/OMC/FTR/REX/ESR 等缩写书中未给全称，full_name 字段如实省略，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: Rainbow
  category: concept
  source_pages: p29-31, p84
  source_quote: |
    "Rainbow is a Cloud-based collaboration application (UCaaS) offering chat services, audio / video calls,
    screen and file sharing, contact management, phone presence…etc. In a Hybrid cloud approach, Rainbow
    integrates with OXO Connect and OmniPCX Enterprise, as well as third-party PBXs. It is also a CPaaS open
    communication platform with a set of APIs…" (p29)
  definition: |
    ALE 的云协作平台，本书中是"宿主平台"角色：UCaaS（协作/云话音）与 CPaaS（开放 API）双重定位；
    在混合云模式下集成 OXO Connect（本书主线）与 OXE/第三方 PBX。本书场景里 Rainbow 侧提供公司、
    订阅、成员账户体系与客户端（PC App/Web/移动），PBX 侧保留呼叫控制。
  alias_or_related: UCaaS、CPaaS、Hybrid cloud（均并入本条）；web.openrainbow.com 为网页客户端入口（p84）；developers.openrainbow.com 为 CPaaS 门户（见 g58）
  tags: [concept, platform, ucaas, cpaas]

- id: g02
  term: Company
  category: concept
  source_pages: p47-48, p54
  source_quote: |
    "To ease collaboration between colleagues in the same company, users are gathered within the same Company.
    • Main features are only available to users who are members of a Company, and it is therefore a key concept
    in Rainbow. • Reseller Companies have special rights • End customer companies are created by a Reseller …
    A user cannot be part of 2 different companies." (p47)
  definition: |
    Rainbow 的用户组织单元，核心概念：主功能仅对公司成员开放；用户不可同时属于两家公司。
    分 Reseller/BP 公司与 End Customer 公司两级，EC 公司由 Reseller 创建并必须挂在唯一一个 BP 下。
    创建前要先搜索查重。
  alias_or_related: Reseller/BP Company（g20）、End-customer Company（g24）
  tags: [concept, tenant]

- id: g03
  term: Visibility
  category: concept
  source_pages: p52
  source_quote: |
    "PUBLIC: a user from another company can see and invite members of your company… PRIVATE: … CLOSED: a user
    from another company cannot see the members of your company, but he can invite them via their email address.
    Your users can't see users outside their company, but they can invite them via their email address.
    ISOLATED: a user from another company cannot see the members of your company and cannot invite them…"
    "Get into the habit of systematically setting the 'closed' mode… This 'isolated' mode is not recommended…
    your users will no longer be able to be invited to conferences (bubbles) external to your organization." (p52)
  definition: |
    公司对外可见性四级（PUBLIC/PRIVATE/CLOSED/ISOLATED），在 company settings 中可改。作者明确推荐：
    建公司时默认设 CLOSED（适合绝大多数客户）；不推荐 ISOLATED——代价是用户无法被组织外部的
    会议（bubble）邀请。成员个人另有 Visibility 设置（same as company/none/public/private…，p96）。
  alias_or_related: bubble = 书中对 Rainbow 会议/群聊的口语提法，仅 p52 一处，未定义
  tags: [concept, privacy]

- id: g04
  term: SSO
  full_name: Single Sign-On（书中以 SSO* 脚注展开）
  category: concept
  source_pages: p53, p241
  source_quote: |
    "you can enable single sign-on (SSO*) with your Azure Active Directory, or with your corporate AD (ADFS).
    SSO can be enabled for your entire company, or only for certain users. The administrator must have an
    'Enterprise' service level … Azure AD - SAML / Azure AD - OIDC / ADFS - SAML … other methods are possible,
    subject to ALE confirmation, when they are based on standard protocols. For example, with SAML V2 :
    Shibboleth, RSA, … and with OIDC : LemonLDAP, OKTA, CAS APEREO, Ping Identity, …" (p53)
  definition: |
    公司级单点登录：支持 Azure AD（SAML 或 OIDC 两种协议）与本地 AD（ADFS-SAML），可全公司启用或
    仅部分用户；前提是管理员持 Enterprise 订阅。基于标准协议的其他 IdP 需 ALE 确认。
    Teams 集成实验中亦示范用 Microsoft 凭据 SSO 登录 Rainbow（p241），且注明 SSO 非连接器必需。
  alias_or_related: SAML、OIDC、ADFS（认证协议/网关，并入本条，不单列）；与 g05 TOTP 并列的两类认证方式
  tags: [concept, auth]

- id: g05
  term: TOTP
  full_name: Time-based One Time Password（书中直接展开）
  category: concept
  source_pages: p53
  source_quote: |
    "Authentication with TOTP (Time-based One Time Password) Users need a third-party authentication application
    (Google Authenticator, Microsoft Authenticator, Authy). This method applies to all types of users but is
    particularly recommended for the administrators." (p53)
  definition: |
    Rainbow 原生认证的第二种模式（另一种是 12 位复杂密码传统认证）：需第三方验证器 App，
    特别推荐给管理员使用。MFATOTP 设置参考文章见 p53 引用链接。
  alias_or_related: 与 g04 SSO 并列；书中称 "Rainbow's native authentication"
  tags: [concept, auth, mfa]

- id: g06
  term: RCC
  full_name: Remote Call Control（书中展开）
  category: concept
  source_pages: p6, p110, p112, p116
  source_quote: |
    "At this step, Rainbow users can only supervise their extension: RCC mode (Remote Call Control)
    • Supervision of DeskPhones by the Rainbow application (Pick up, hang up, transfer)
    • Audio is exclusively managed by the deskphone." (p6)
    "Without a WebRTC gateway, the audio will be exclusively managed on the phone." (p112)
  definition: |
    OXO 分机关联到 Rainbow 账户后、但尚未部署 WebRTC 网关时的工作模式：Rainbow 客户端只能"监督"
    话机（接听/挂断/转移），音频完全留在话机上。本书定位其为无网关阶段的正常形态，是下一个实验
    （WebRTC 网关）的前置基线。验证法：呼出选 "Office phone" 路由（p116）。
  alias_or_related: 与完整模式（WebRTC 网关部署后可全路由）对照；分机关联入口 = My company/Telephony
  tags: [concept, telephony, mode]

- id: g07
  term: WebRTC Gateway
  category: concept
  source_pages: p117-123, p126, p129, p141, p146-147
  source_quote: |
    "The WebRTC Gateway brings voice interoperability between Rainbow Clients and PBX ecosystem.
    • This enables an audio media relationship between Rainbow applications and devices of a PBX connected
    to Rainbow • Audio between Rainbow clients / any phones / Off-net • Unified multi-devices experience." (p118)
    "Communication flows between the WebRTC GW and Rainbow over the internet are secured with HTTPS and SRTP." (p126)
  definition: |
    全书核心设备：Rainbow 客户端与 PBX 生态间的语音互操作网关，只建立"音频媒体"关系——呼叫控制始终
    在 PBX。三种承载拓扑：OCE 集成（R3.2+）、OCE Front End（专用 IPBox）、外部虚拟机（ESXi）或 Mini PC
    （NUC）。书中口径：集成与 FE 记为 Internal/"External on OCE Front-End"，外部 VM/NUC 记为 External
    （p121-122、p133）；容量上限见 g32-g34 与 p147 容量表。R4.0.020.002 起支持从 Rainbow 侧自动配置。
  alias_or_related: 内部 GW = OCE 集成；外部 GW = FE / NUC / ESXi VM；WebRTC 为其底层技术（不单列）
  tags: [concept, gateway, telephony, core]

- id: g08
  term: Free Rainbow in Twinset
  category: concept
  source_pages: p123, p155-157
  source_quote: |
    "Create a Multiset • The main station is the physical station • The secondary station is
    • Free Rainbow in Twinset from R6.0 • (Anydevice up to R5.2) … Secondary station from Release 6.0:
    The Free Rainbow in Twinset virtual terminal must be used in order to save an UTL license (UTL Bypass)." (p123)
  definition: |
    R6.0 起的 OXO 虚拟副站终端类型：有话机用户（Multiset 结构 = 物理主站 + 此虚拟副站）经它使用
    Rainbow 应用打电话，且不额外消耗 UTL 许可（UTL Bypass）。R5.2 及以前该副站位置用 Anydevice
    （跨版本语义差异，升级交付注意）。创建于 OMC/Subscribers list，并挂为主站的 secondary set（p157）。
  alias_or_related: Multiset = 主站+副站结构（并入本条）；对照 g09 Anydevice；许可影响见 g15 UTL
  tags: [concept, terminal, license]

- id: g09
  term: Anydevice
  category: concept
  source_pages: p123, p155-158, p169
  source_quote: |
    "In the case of a user with only Rainbow (without a physical station), create for this user only an
    Anydevice terminal. Note: Until Release 5.2 the AnyDevice equipment was also used as a secondary station
    in multiset." (p123)
    "REX on OXE (Up to 10 calls) - Any Device on OXO Connect (minimum R6 version Maximum 8 calls." (p169)
  definition: |
    纯软话机终端类型：用户无物理分机，全部通信经 Rainbow 应用（Client/Web/移动）管理，占 1 个 UTL。
    OXO 侧要求最低 R6 版本，作为话务台多线资源时最多 8 路（OXE 用 REX 可到 10 路）。注意版本语义：
    R5.2 前 Anydevice 曾兼作 Multiset 副站，R6.0 起副站位置改用 Free Rainbow in Twinset。
  alias_or_related: 对照 g08 Twinset（有话机用户）；REX = OXE 侧对应的多线资源，书中未展开全称
  tags: [concept, terminal, softphone]

- id: g10
  term: Supervision group
  category: concept
  source_pages: p164, p167-168, p178
  source_quote: |
    "In order to supervise the members of a company, users with the attendant subscription, and the supervised
    members must belong to a supervision group. Each supervision group includes • One or several supervisors:
    they must be granted an Attendant license to use the attendant console • The company members to supervise.
    Maximum number of supervision groups for a supervisor 5. Maximum number of users in a group (supervisors
    + supervised) 30." (p167)
  definition: |
    Rainbow 侧话务台监督组：监督员（必须持 Attendant 订阅）与被监督成员同组才能互相看见与代接。
    硬规格：每监督员最多 5 个组，每组（含监督员）最多 30 人。建组入口 = 公司管理端 Communication/
    Supervision（p178）。这是 Rainbow 平台概念，与 OXO PBX 侧的组无涉。
  alias_or_related: 对照 Mutual aid group（g11，动态进出型）；入口均为 Attendant console（g12）
  tags: [concept, attendant, supervision]

- id: g11
  term: Mutual aid supervision group
  category: concept
  source_pages: p170-173, p180-181
  source_quote: |
    "You can supervise two types of group. • Groups that are permanently affiliated to you • Groups that you
    can join on an ad hoc basis in one click at times. You can also temporarily integrate or exclude a
    supervised user… As supervisor, you will be notified of telephone calls intended for supervised users.
    • You can pickup calls. Works only for PBX calls, not for Rainbow softphone calls." (p171)
  definition: |
    互助型监督组：与"经典"监督组同法创建、Type 选 Mutual aid group（p180，另有 "Lock the last member"
    选项）。特点是成员关系动态——监督员可一键加入/退出组、可临时纳入/排除成员；代接仅对 PBX 电话
    呼叫有效（Rainbow 软话机呼叫不行），且被监督成员需有物理分机或 PBX 软话机（IPDSP/MicroSIP，p181）。
  alias_or_related: 对照 g10 Supervision group（固定成员型）；被监督上限 "Up to 4 calls supervised"（p172）
  tags: [concept, attendant, supervision]

- id: g12
  term: Attendant console
  category: concept
  source_pages: p162-166, p169, p175-179
  source_quote: |
    "Attendant console allows to • Supervise members' status - Presence and call control • Call queue
    management - Manage up to 10 calls for OXE - And up to 8 calls for OXO Connect • Manage calls for
    supervised members - Pick-up calls, call transfer, voicemail forwarding, forwarding status …
    An Attendant subscription is required for each member using this feature • Available on the Rainbow Web
    and Desktop applications • Attendant console not available on mobile." (p164)
  definition: |
    Rainbow 话务台（Web/Desktop 客户端，无移动端）：呼叫队列 + 被监督成员状态 supervision + 呼叫操作。
    OXO 队列 8 路 / OXE 10 路；话务员必须持 Attendant 订阅、有电话线与 VoIP 软话机能力，且话务功能
    仅在 PC 可用（话机/手机上均不可操作，p169）。三种显示密度 Normal/Small/Condensed（p166）。
  alias_or_related: 订阅前提见 g28 Rainbow Attendant；监督结构见 g10/g11；队列多线资源见 g09（Anydevice 8 路）
  tags: [concept, attendant, console]

- id: g13
  term: Rainbow number
  category: concept
  source_pages: p115, p233
  source_quote: |
    "Once the association done, a new field is displayed, the Rainbow number… This number will be retrieved
    later for WebRTC gateway use. It will be automatically configured in Remote Extension number by the
    Rainbow agent (e.g. BBB10070254106463346) when the user selects 'computer' as routing from his Rainbow
    client (PC or smartphone)." (p115; 同文重现于 p233)
  definition: |
    分机与 Rainbow 账户关联后自动出现的编号（形如 BBB 开头长串）：WebRTC 音频落地的隐藏配置项——
    用户把路由选成 "computer" 时由 Rainbow agent 自动写入 Remote Extension number，无需手工设置，
    但排障时要认识它。
  alias_or_related: 由 Rainbow agent 自动维护；出现时机 = My company/Telephony 关联分机后
  tags: [concept, telephony, config]

- id: g14
  term: PBXID & Activation code
  category: concept
  source_pages: p83-86, p134
  source_quote: |
    "Enter the Rainbow PABX-ID / Enter the Activation code / Click on Rainbow enabled … The Rainbow ID is
    generated by Rainbow. The activation code is generated by Rainbow. Domain name Leave the default value:
    openrainbow.com." (p86)
    "On the OXO, by entering an FTR, the PBXID and the activation code are initialized by default to
    'FleetRef-Installref', which allows the installer to prepare the equipment in advance in RB WebAdmin:
    the OXO will automatically connect to RB at the end of the FTR to FleetRef-Install_ID." (p134)
  definition: |
    OXO 接入 Rainbow 的双凭证：由 Rainbow 平台生成，可由经销商提供，或客户管理员在 My company/
    Communication 点开 PBX 查询后复制到 OMC/Cloud/Rainbow。域名保持默认 openrainbow.com。
    注意：FTR 时默认占位为 "FleetRef-Installref"，FE 场景两台 OXO（call server 与 Front-End）必须填
    同一 PBXID（p134）；正式接入前要替换占位值。
  alias_or_related: 不是 PBX 序列号；FE 场景双机同 ID 是易错点
  tags: [concept, credential, onboarding]

- id: g15
  term: UTL
  category: concept
  source_pages: p123, p129, p156
  source_quote: |
    "Deskphone + Free Rainbow virtual terminal = 1 UTL • Anydevice only = 1 UTL" (p156)
    "Secondary station from Release 6.0: The Free Rainbow in Twinset virtual terminal must be used in order
    to save an UTL license (UTL Bypass)." (p123)
    "An OCE in front-end Mode is limited to WebRTC GW feature (No UTLs, etc…)" (p129)
  definition: |
    OXO 侧电话许可的计量单位（书中未展开全称）：有话机用户（Deskphone + Free Rainbow in Twinset 副站）
    与 Anydevice 纯软话机用户各占 1 个 UTL；Twinset 副站的意义就是 R6.0 起"不吃额外 UTL"（UTL Bypass）。
    OCE Front-End 模式下无 UTL 能力（仅限 WebRTC GW 功能）。
  alias_or_related: UTL Bypass（p123 术语）；创建终端的许可影响在 OMC/Subscribers list 配置时体现
  tags: [concept, license, oxo]

- id: g16
  term: FTR
  category: concept
  source_pages: p128, p130-131, p134
  source_quote: |
    "Installation of the OCE Front-End is automated with the FTR procedure • FTR provides the OCE Front-End
    license and upgrades the OCE release (≥ R4.0 MD) if necessary." (p130)
    "At the first connection to a brand new IPBox, an installer password must be defined … Define the product
    type 'Frontend WebRTC' … Enter the customer reference, IP parameters… FTR OK. This IPBox is now an OXO
    Connect FrontEnd WebRTC Gateway and ready to be associated to the OXO Connect customer call server." (p131)
  definition: |
    OXO 首次开箱流程（书中未展开全称）：全新 IPBox 首连（ETH1 DHCP，浏览器到 192.168.94.246）时定义
    安装员密码、产品类型（FE 场景选 'Frontend WebRTC'）、录客户参考与 IP 参数。FE 的免费专用许可由
    FTR 自动提供并按需升级系统版本；FTR 还会把 PBXID/激活码初始化为 "FleetRef-Installref" 占位（p134）。
  alias_or_related: 与 g34 OCE Front End 部署强绑定；Cloud Connect FTR 说法见 p128
  tags: [concept, deployment, oxo]

- id: g17
  term: Business Directory
  category: concept
  source_pages: p60
  source_quote: |
    "In addition to a Microsoft Azure Active Directory, you can create a 'Business Directory' containing the
    contacts of external companies or organizations that are useful to all your users, along with their phone
    numbers. • The quality of reception will be improved thanks to the caller identification during the call
    presentation." (p60)
  definition: |
    公司级外部联系人目录（补充 Azure AD 之外的外部公司/组织联系人），提升来电呈现时的主叫识别。
    默认客户管理员可管理，也可委托给非管理员用户；支持手工创建或 CSV 批量导入（附样例文件与导入报告）。
  alias_or_related: 与 Members 目录区分——本目录存外部联系人
  tags: [concept, directory, admin]

- id: g18
  term: Information Channels
  category: concept
  source_pages: p61
  source_quote: |
    "Similar to news feeds, they allow to distribute information to a range of users • Users can create,
    search and join a specific channel, allowing them to follow the news on a dedicated topic …
    Only users with an 'Enterprise' service level can create Information Channels." (p61)
  definition: |
    公司信息频道（类新闻源）：需先在 Roles 页签授权，仅 Enterprise 服务级别用户可创建；可建"全公司
    自动订阅且不可退订"的强制频道，也可跨公司开放加入。
  alias_or_related: 创建权限与 g27 Enterprise 订阅挂钩
  tags: [concept, channel, admin]

- id: g19
  term: Grace period
  category: concept
  source_pages: p93, p99
  source_quote: |
    "When you delete a user, his or her status becomes 'Suspended' for a period of 10 days (called the
    'grace period')… When deleted, the user's subscription was automatically removed. If you restore it,
    it will default to 'Essential' (free) mode, so you'll need to reallocate the appropriate license…"
    (p99)
  definition: |
    成员删除的 10 天缓冲期：期间可恢复（误删）或彻底删除；不动作则 10 天后自动永久删除。恢复后订阅
    已被回收、回落到 Essential 免费模式，需重新分配许可并重挂电话线。另注：10 天内被删账号的邮箱
    不能用于新建账号（p93 报错提示）。
  alias_or_related: 恢复后默认 g25 Essential 订阅
  tags: [concept, member, lifecycle]

# ── 二、经销体系角色 (role) ──

- id: g20
  term: BP
  full_name: ALE Business Partner（书中展开）
  category: role
  source_pages: p48, p57, p64, p121
  source_quote: |
    "ALE Business Partner (BP) … Most administration operations can be performed by both the Business Partner
    and the customer administrator. However, the following actions can only be performed by the BP:
    • Declaration & PBX • Opening of paid subscriptions." (p48)
    "Create PBXs & activate WebRTC gateways … Assign subscriptions to end-customer companies." (p57)
  definition: |
    ALE 业务伙伴（Reseller 公司）：独占两类操作——PBX 声明/创建、付费订阅开通；并负责给 EC 公司分配
    订阅、创建 PBX、激活 WebRTC 网关（自动配置"只能由 Reseller administrator 账户操作"，p121/p151）。
    BP 公司本身也是 Rainbow Company 的一种。
  alias_or_related: BP administrator = Reseller administrator（p57/p121 同义使用）；对比 g24 EC
  tags: [role, reseller, admin]

- id: g21
  term: DR
  full_name: Direct Reseller（书中展开）
  category: role
  source_pages: p48
  source_quote: |
    "The customer's integration partner must be either a 'DR' or an 'IR'." (p48)
  definition: |
    直接经销商：EC 客户的集成伙伴必须是 DR 或 IR 两种身份之一（经销层级中的一级）。
  alias_or_related: 与 g22 IR 同为集成伙伴合法身份；同表列出 BP/VAD/EC
  tags: [role, reseller]

- id: g22
  term: IR
  full_name: Indirect Reseller（书中展开）
  category: role
  source_pages: p48
  source_quote: |
    "ALE IR Indirect Reseller" (p48)
  definition: |
    间接经销商：EC 客户集成伙伴的另一种合法身份（与 DR 并列）；书中仅给出名称与层级关系，无更多操作细节。
  alias_or_related: 见 g21 DR、g20 BP、g23 VAD
  tags: [role, reseller]

- id: g23
  term: VAD
  full_name: Value Added Distributor（书中展开，法语标注 Grossiste）
  category: role
  source_pages: p48
  source_quote: |
    "VAD Value Added Distributor (Grossiste)" (p48)
  definition: |
    增值分销商：经销层级图中最靠近 ALE 的一级（p48 层级图 ALE → BP/DR/IR/VAD → EC）；书中仅列名，
    无专属操作说明。
  alias_or_related: 见 g20 BP、g21 DR、g22 IR
  tags: [role, distributor]

- id: g24
  term: EC
  full_name: End Customer（书中展开，法语标注 Client Final）
  category: role
  source_pages: p48, p58
  source_quote: |
    "To be managed by a BP, an 'EC' company must be attached to the company of this BP (one and only one
    attachment)." (p48)
    "END-CUSTOMER ADMINISTRATOR: Manages its own company … Assign subscriptions to users accounts …
    Associate users phones with their Rainbow accounts." (p58)
  definition: |
    最终客户（End-customer 公司）：必须挂在唯一一个 BP 公司下才能被其管理；EC 管理员管本公司成员、
    公司信息、给用户分配订阅、把话机关联到 Rainbow 账户，但无 PBX 声明与付费订阅开通权（BP 专属）。
  alias_or_related: 对比 g20 BP；EC 管理员可用 "Roles" 页签增配多名管理员（p59）
  tags: [role, end-customer, admin]

# ── 三、订阅计划 (subscription)，均定义于 p33 订阅表 ──

- id: g25
  term: Rainbow Essential
  category: subscription
  source_pages: p33, p99
  source_quote: |
    "Rainbow Essential This free option is available to anyone who wants to try Rainbow for an unlimited
    period (no SLA). The Essential subscription can also be blended with any premium subscription,
    optimizing the cost of the solution for the whole organization." (p33)
  definition: |
    免费订阅（无 SLA），可无限期试用，也能与任一付费订阅混用；但电话服务不可用（p65：电话服务必须
    Business/Enterprise/Attendant）。成员被删除后恢复时默认回落到 Essential（p99）。
  alias_or_related: freemium（p33 Conference 行用语）；电话功能对照 g26/g27/g28
  tags: [subscription, free]

- id: g26
  term: Rainbow Business
  category: subscription
  source_pages: p33, p65, p142, p208, p235
  source_quote: |
    "Rainbow Business The per-user subscription addresses individuals and teams who want to improve their
    daily communication, on or off-site, on-the-move, or as a productive remote worker." (p33)
    "Each user needs to be granted with either a Business or an Enterprise license" (p142, WebRTC 网关用户前提)
  definition: |
    按用户计费的付费订阅：电话服务的最低档（WebRTC 网关用户、Teams 集成用户均要求 Business 或
    Enterprise，p142/p208/p235）。话音/话务台能力的门槛档位。
  alias_or_related: 电话服务三档 g26/g27/g28 之一；Essential 无电话能力
  tags: [subscription, telephony]

- id: g27
  term: Rainbow Enterprise
  category: subscription
  source_pages: p33, p53, p61, p65, p92, p104
  source_quote: |
    "Rainbow Enterprise The per-user subscription includes all services from Rainbow Business, but with the
    addition of collaborative multi-party services with video conferencing and extended file storage.
    Integration into existing office tools such as Microsoft 0365 and Google Suite also forms part of this
    service plan." (p33)
  definition: |
    含 Business 全部服务 + 多方视频会议、扩展文件存储、Office 工具集成（原文写作 Microsoft 0365）。
    本书多处隐性门槛：SSO 设置要求管理员持 Enterprise（p53）、Information Channels 仅 Enterprise 可建
    （p61）、Azure AD 批量导入要求 "Voice Enterprise" 服务级别（p92）；实验中成员统一分配 Enterprise（p104）。
  alias_or_related: "Voice Enterprise"（p92）为其电话侧口径；对比 g26 Business
  tags: [subscription, telephony]

- id: g28
  term: Rainbow Attendant
  category: subscription
  source_pages: p33, p164, p175-177
  source_quote: |
    "Rainbow Attendant for Hybrid users requires a new specific subscription offer identified as 'Attendant'.
    The Rainbow Attendant console presents of a list of waiting calls, with the ability to dispatch the calls
    to other destinations. It also includes a supervision console that identifies groups of Rainbow users
    with the capability to see and pick up incoming calls." (p33)
  definition: |
    混合场景话务台专属订阅（Hybrid 用户专用）：解锁 Attendant console（等待队列 + 调度 + 监督代接）。
    每个使用话务台功能的成员都要持 Attendant 订阅（p164）；实验按 "Attendant Monthly" 开通、禁用
    Prepaid（p176）。持 Attendant 的用户即监督组中的 supervisor。
  alias_or_related: 解锁 g12 Attendant console 与 g10/g11 监督组
  tags: [subscription, attendant]

- id: g29
  term: Rainbow Enterprise Conference / Rainbow Conference
  category: subscription
  source_pages: p33
  source_quote: |
    "Rainbow Enterprise Conference This per-user subscription packages the Rainbow Enterprise service plan
    with unlimited phone conferencing minutes. The Rainbow Enterprise Conference user subscription is
    pre-paid yearly in advance (twelve months)." / "Rainbow Conference An optional service proposed as a
    'pay-as-you-go' model for phone (PSTN) conferencing with a price-per-minute/per-connection. The organizer
    of the meeting can be a Rainbow Essential (freemium) user, or premium user with Rainbow Business or
    Rainbow Enterprise subscriptions." (p33)
  definition: |
    会议类两档：Enterprise Conference = Enterprise 套餐 + 无限电话会议分钟数（按年预付 12 个月）；
    Conference = PSTN 电话会议按分钟/连接计费的按量可选服务（组织者可以是 Essential 免费用户）。
    两者并为一词条（同属会议计费家族）。
  alias_or_related: PSTN 见 g48
  tags: [subscription, conferencing]

- id: g30
  term: Rainbow Connect
  category: subscription
  source_pages: p33
  source_quote: |
    "Rainbow Connect The per-user subscription addresses users of any Customer Relationship Management (CRM)
    application. The integration of the Rainbow functionality is provided using a specific connector
    dedicated to the compatible CRM application." (p33)
  definition: |
    面向 CRM 应用用户的按用户订阅：通过各兼容 CRM 的专用连接器集成 Rainbow 功能。本书未展开任何
    连接器细节（仅 p33 一段定义）。
  alias_or_related: 与 Teams 集成（g57 相邻章节）无直接关系，勿混
  tags: [subscription, crm]

- id: g31
  term: Rainbow Room
  category: subscription
  source_pages: p33
  source_quote: |
    "Rainbow Room An optional per-room subscription proposed for meeting rooms equipped with large screens
    for communication and interaction with people inside and outside of the company. Additional hardware is
    required to equip the meeting room and ALE has audio and video hardware kits readily available." (p33)
  definition: |
    按会议室计费的可选订阅：配大屏会议室与公司内外人员通信互动；需额外硬件（ALE 提供音视频套件）。
    本书无部署细节。
  alias_or_related: 无
  tags: [subscription, room]

# ── 四、产品/组件名 (product) ──

- id: g32
  term: OXO Connect
  category: product
  source_pages: p29, p118, p129, p147
  source_quote: |
    "In a Hybrid cloud approach, Rainbow integrates with OXO Connect and OmniPCX Enterprise, as well as
    third-party PBXs." (p29)
    "Type of Rainbow GW … OXO Connect (Power CPU EE): Internal GW Not supported; External GW (NUC) 50 calls
    max.; OCE-FE GW 20 calls max." (p129)
  definition: |
    ALE 面向 SMB 的通信服务器（本书的宿主 PBX，书名主角）：保留呼叫控制与现场话音，经 PBXID+激活码
    接入 Rainbow。非 Evolution 形态的 CPU 为 Power CPU EE：不支持内部 GW 与 OCE-FE GW，仅支持外部
    NUC GW（50 通话）；Rainbow VoIP 用户上限 150（p147，对 OXO Connect 与 Evolution 同样适用）。
  alias_or_related: Power CPU EE = OXO Connect（非 Evolution）的 CPU 形态（并入本条）；对照 g45 OXE、g33 OCE
  tags: [product, pbx, smb]

- id: g33
  term: OCE
  full_name: OXO Connect Evolution（书中 p19 完整拼写）
  category: product
  source_pages: p19, p118, p125-126, p129, p202
  source_quote: |
    "RAINBOW WebRTC Gateway integrated in OCE … Same feature level as the external WebRTC GW topology.
    Easy to configure and maintain via OCE management tools. SW upgrade via OXO management tool and Cloud
    Connect Update service. No need for SIP trunk licenses (bypass) • Supported for OCE and OXO Connect." (p125)
    "OCE Front-End does not provide PBX capabilities" (p129, 指运行于 OCE 硬件的 FE 模式)
  definition: |
    OXO Connect Evolution：R3.2 起内部集成 WebRTC 网关的 OXO 形态（硬件为 IPBox）。集成 GW 与外部 GW
    功能同级，经 OCE 管理工具维护、经 Cloud Connect Update 升级软件，且无需 SIP trunk 许可（bypass）。
    Teams 章节缩写 "OXO CE"（p202）同指。内部 GW 上限 20 通话（p129 表）。
  alias_or_related: 硬件名 IPBox（p128-129）；缩写 OXO CE（p202）；FE 模式见 g34
  tags: [product, pbx, gateway]

- id: g34
  term: OCE Front End (OXO Connect WebRTC Front End)
  category: product
  source_pages: p118, p127-137
  source_quote: |
    "The WebRTC gateway runs on an IPBox on the customer's LAN, in front of another OXO Connect which runs
    the customer Call Server. The release ≥ R4.0 MD must be installed on both the Front-End RGW and the OXO
    Connect call server … No dedicated software for Front-End (but specific license for free) … The license
    is free and auto-provisioned (FTR). Release ≥ R4.0 MD is mandatory." (p128)
    "A standard OXO Connect Evolution (HW and SW) is used… An OCE in front-end Mode is limited to WebRTC GW
    feature (No UTLs, etc…) … OCE Front-End does not provide PBX capabilities • OMC tool is not needed for
    OCE Front-End provisioning." (p129)
  definition: |
    第二种拓扑：一台标准 OCE（IPBox）放在客户 LAN、置于跑呼叫服务器的另一台 OXO Connect 之前，专职
    WebRTC 网关（无 PBX 能力、无 UTL）。免费专用许可由 FTR 自动供给；≥R4.0 MD 强制（FE 与 call server
    双侧）； provisioning 不需要 OMC；管理走 Rainbow Admin（激活/耦合）+ Cloud Connect（设备管理）。
    上限 20 通话（p129/p133）；修改 FE 配置后需 warm reset（p132）。
  alias_or_related: Rainbow 管理界面类型选项名 "External on OCE Front-End"（p133）；另一台 call server 见 g32
  tags: [product, gateway, frontend]

- id: g35
  term: NUC
  full_name: Next Unit of Computing（书中 p144 直接展开）
  category: product
  source_pages: p118, p143-145, p147
  source_quote: |
    "NUC: Next Unit of Computing … The Software package available on MyPortal contains the OVF files for
    VMWARE installation, and, an ISO file for installation on a mini PC." (p144)
  definition: |
    第三种拓扑的承载硬件（Mini PC）：外部 WebRTC 网关虚拟机装在 NUC 上，上限 50 通话（p147）。
    安装走 ISO（MyPortal 下载，RUFUS 做 U 盘启动，p145），其余步骤与 VMWare 部署相同。
  alias_or_related: 对照 ESXi VM 拓扑（p118/p141，同为外部 GW、同 50 通话）
  tags: [product, hardware, gateway]

- id: g36
  term: OMC
  category: product
  source_pages: p69-78, p86, p113, p129, p150, p154
  source_quote: |
    "Install OMC on the administrator PC. The OMC software can be found in the SOFTS OXO CONNECT directory
    on the PC desktop." (p70)
    "Make a connection to the system with OMC in Expert mode with server authentication … Enter the default
    installer password pbxk1064 only used for the first connection." (p74)
  definition: |
    OXO 的管理工具软件（书中未展开全称），装在管理员 PC 上：本书用它完成安装首连（Expert 模式 + 服务器
    认证 + 证书安装 + 改密 + 客户信息）、IP 规划修改、Cloud/Rainbow 接入（填 PBXID/激活码）、建 Twinset/
    Anydevice 终端、核验 WebRTC 网关激活等几乎所有 OXO 侧操作。注意：OCE Front-End 的 provisioning
    不需要 OMC（p129）。
  alias_or_related: 默认安装密码 pbxk1064 仅首次登录用（p74）；菜单路径如 OMC/Cloud/Rainbow、OMC/Tools/Webdiag
  tags: [product, management, oxo]

- id: g37
  term: Webdiag
  category: product
  source_pages: p83, p88, p132
  source_quote: |
    "OMC /Tools /Webdiag /Services /Rainbow Status. Control the connection status: 'connected with final
    password' … Login: installer. Password: enter installer pwd." (p88)
    "Front-End WebRTC CPU status can be checked • In menu Settings • In Webdiag tool." (p132)
  definition: |
    OXO 内置诊断工具（经 OMC/Tools 进入，installer 登录）：查 Rainbow 连接状态（正常态显示
    "connected with final password"）、查系统日志文件（含 ccrbagent.log）、查 FE WebRTC CPU 状态。
    是 PBX-Rainbow 接入排障的第一入口。
  alias_or_related: 日志文件见 g39 ccrbagent.log
  tags: [product, diagnostics, oxo]

- id: g38
  term: Cloud Connect
  category: product
  source_pages: p125, p129, p134, p136
  source_quote: |
    "SW upgrade via OXO management tool and Cloud Connect Update service" (p125)
    "The Rainbow WebRTC Gateway on OCE Front-End solution management • Rainbow Admin (for coupling the OXO
    to the company & WebRTC GW activation) • Cloud Connect (for OCE Front-End management)." (p129)
    "In Fleet Dashboard & OXO Connectivity: Identification of PABX/OCE-Front-End, Dynamic link to access the
    peer device with a single click. 1 line per device in Fleet Dashboard with same root of install_id." (p136)
  definition: |
    ALE 的云侧设备管理服务：负责 OCE Front-End 的设备管理（与 Rainbow Admin 分工，p129）、软件升级
    （Update service，p125）；其 Fleet Dashboard 与 OXO Connectivity 界面可识别 PABX/OCE-FE 并一键跳转
    对端设备（同一 install_id 根，p136）。RB WebAdmin 是其 Web 管理端（p134：FTR 占位凭证
    "FleetRef-Installref" 让安装员提前在 RB WebAdmin 备货，FTR 结束后 OXO 自动连到 FleetRef-Install_ID）。
  alias_or_related: RB WebAdmin、Fleet Dashboard、OXO Connectivity（均并入本条）
  tags: [product, cloud, management]

- id: g39
  term: ccrbagent.log
  category: product
  source_pages: p83, p88
  source_quote: |
    "System tab/ System Files/ Log files. The rainbow agent log file name is: ccrbagent.log …
    Login: installer. Password: enter installer pwd" (p88)
  definition: |
    OXO 上 Rainbow agent（负责 PBX-Rainbow 连接的代理）的日志文件名，经 Webdiag 的 System/System Files/
    Log files 获取（installer 登录），是接入排障的关键日志。
  alias_or_related: 与 g37 Webdiag 配套使用
  tags: [product, log, troubleshooting]

- id: g40
  term: TURN
  category: product
  source_pages: p141
  source_quote: |
    "WebRTC Gateway configuration steps • Configure the Network settings (static or DHCP) • IP, NETMASK,
    GATEWAY and DNS • Add the OXO Connect IP@ and Rainbow PBXID • TURN server configuration according to
    site location." (p141)
  definition: |
    外部 WebRTC 网关（VM 部署）配置步骤中的一项：按站点位置配置 TURN 服务器。书中仅此一处提及，
    未展开部署细节（生产细节在书外文档）。
  alias_or_related: 书中仅出现于外部 GW VM 配置清单
  tags: [product, media, config]

- id: g41
  term: Emily BOT
  category: product
  source_pages: p191
  source_quote: |
    "Support entry points can be : • Mail : support@openrainbow.com • Emily BOT • Global Welcome Center is
    the main point of contact for all ALE International Partners. • ALE.WelcomeCenter@al-enterprise.com
    • Or phone call. The ESR will only be created if the partner is certified on Rainbow." (p191)
  definition: |
    Rainbow 支持入口之一（机器人）。完整的支持入口还包括邮箱 support@openrainbow.com、Global Welcome
    Center（ALE 国际伙伴总 contact 点）与电话；无论哪个入口，SR（服务请求）只有 Rainbow 认证伙伴
    才会被创建。
  alias_or_related: support@openrainbow.com、Global Welcome Center（并入本条）；开 SR 见 g57 MyPortal
  tags: [product, support, bot]

- id: g42
  term: MicroSIP
  category: product
  source_pages: p16, p113, p181
  source_quote: |
    "SIP Softphones are already preinstalled: • 4 MicroSIP softphones clients for internal users directory
    numbers: 100, 101, 102, 103 • 2 MicroSIP softphones to simulate public numbers." (p16)
  definition: |
    培训实验环境预装的软话机客户端（第三方 SIP 软话机）：实验 PC 上 4 个模拟内部分机 100-103、
    2 个模拟公网号码；在互助组实验中与 IPDSP 并列为 "PBX softphone"（p181）。纯教学基础设施。
  alias_or_related: 见 g43 IPDSP、g44 ITSP1
  tags: [product, lab, softphone]

- id: g43
  term: IPDSP
  full_name: IP Desktop Softphone（书中 p113 展开）
  category: product
  source_pages: p16, p112-113, p181
  source_quote: |
    "An IPDSP to be installed, it will be the main softphone to use directory number: 104." (p16)
    "In a V-Class, there are no physical phones. We will use the IP Desktop Softphone 104 that will be
    assigned to a Rainbow member and MicroSIP softphones to call the created members." (p113)
  definition: |
    ALE 的 IP 桌面软话机：实验中的主用软话机，占分机 104 并关联客户管理员 Rainbow 账户；虚拟课堂
    （V-Class）无物理话机时以它替代物理话机完成 RCC/虚拟终端实验。
  alias_or_related: 对照 g42 MicroSIP（预装辅助软话机）
  tags: [product, lab, softphone]

- id: g44
  term: ITSP1
  category: product
  source_pages: p21-26
  source_quote: |
    "SIP SIMULATOR OVERVIEW - ITSP1 WITH ONE SIP GATEWAY. ITSP1 SIP Gateway 1 gateway1.itsp1.com
    10.20.30.51 … SIP simulator is hosted in the RLAB common area." (p22)
  definition: |
    培训专用的 SIP 运营商模拟器（Public Carrier），托管在 RLAB 公共区：提供 SIP 网关
    （gateway1.itsp1.com）与公网网关（public.itsp1.com），模拟公网/国内/移动/国际/紧急号码
    （编号规则含 POD 号 PN）；OXO 侧按 ITSP1G1 网关参数 + pbxP 账号配置 SIP 中继。纯教学基础设施，
    生产行为（安全/编解码/号码格式）与真实 ITSP 有差异。
  alias_or_related: ITSP2 在拓扑图中出现（p22）但无配置细节
  tags: [product, lab, sip]

- id: g45
  term: OXE
  full_name: OmniPCX Enterprise（书中 p29 完整拼写）
  category: product
  source_pages: p29, p164, p169, p175, p202
  source_quote: |
    "Rainbow integrates with OXO Connect and OmniPCX Enterprise, as well as third-party PBXs." (p29)
    "Call queue management - Manage up to 10 calls for OXE - And up to 8 calls for OXO Connect" (p164)
    "REX on OXE (Up to 10 calls)" (p169)
  definition: |
    ALE 企业级 PBX（本书反复用作 OXO 的对照系）：Teams 集成与话务台章节的实验标题虽写 OXE，配置
    步骤与 OXO 一致；差异点在数值——OXE 话务队列 10 路（OXO 8 路）、REX 多线资源 10 路、话务台配置
    参考文档为 TC2462（OXO 为 TC2479）。
  alias_or_related: REX（p169，OXE 侧多线资源，未展开全称）；"OXE, OXO CE"（p202）CE=Connect Evolution
  tags: [product, pbx, enterprise]

# ── 五、协议与技术名 (protocol) ──

- id: g46
  term: SRTP / HTTPS
  category: protocol
  source_pages: p126, p197
  source_quote: |
    "Communication flows between the WebRTC GW and Rainbow over the internet are secured with HTTPS and
    SRTP • This applies for external and integrated WebRTC GW topologies." (p126)
  definition: |
    WebRTC 网关与 Rainbow 之间经互联网的通信加密方式：信令/管理走 HTTPS、音频媒体走 SRTP；对集成
    与外部两种拓扑一律适用。FE 拓扑图中 call server 侧也标 SIP+https（p128）。
  alias_or_related: 两个缩写书中均未展开全称
  tags: [protocol, security]

- id: g47
  term: SIP Trunk
  category: protocol
  source_pages: p22, p26, p125, p129, p193
  source_quote: |
    "SIP Trunk Group … SIP Gateway Name: ITSP1G1 … Registrar name: sip.itsp1.fr" (p22, p26)
    "SIP Trunk Licenses … Private SIP Trunk … No need for SIP trunk licenses (bypass)" (p125)
  definition: |
    PBX 到运营商/对端网关的 SIP 中继（实验中以 ITSP1 的 SIP Trunk Group 呈现）。许可要点：OCE 集成
    GW 拓扑无需 SIP trunk 许可（bypass），外接 GW 拓扑（R3.2 前）才需要；开 SR 时 "Rainbow SIP trunk"
    是子类别字段（p193）。
  alias_or_related: 与 g07 三拓扑的许可差异是 p125 的核心对比点
  tags: [protocol, trunk, license]

- id: g48
  term: PSTN
  category: protocol
  source_pages: p31, p33, p197
  source_quote: |
    "PSTN" (p31 全局图) / "phone (PSTN) conferencing with a price-per-minute/per-connection" (p33)
    "Public network PSTN/SIP Trunking" (p197)
  definition: |
    公共电话网：书中出现在 Rainbow 全局架构图（云话音出口）、Conference 订阅的计费对象、Teams 集成
    架构图（PBX 经 PSTN/SIP Trunking 出公网）。缩写未展开。
  alias_or_related: Off-net（p118，网外呼叫）同域概念
  tags: [protocol, network]

- id: g49
  term: DDI
  category: protocol
  source_pages: p25-26, p115
  source_quote: |
    "DDI table - First external nb 41100 … 41100 to 41199 base 100 DDI subscribers" (p25-26, 实验编号计划)
    "Public number DDI number associated with the user in the OXO Connect" (p115)
  definition: |
    直拨外线号码：OXO 的 DDI 表把外线号段映射到内部分机（实验用 41100-41199）；Rainbow 侧关联分机时
    的 "Public number" 字段即填该用户在 OXO 的 DDI 号。缩写未展开。
  alias_or_related: 实验号码规则见 p25（DDI 首末号 41100/41199）
  tags: [protocol, numbering]

- id: g50
  term: ARS
  category: protocol
  source_pages: p121, p150
  source_quote: |
    "Configuration of ARS table to route Rainbow calls … The following settings are managed automatically:
    … Creation of VoIP accesses and trunk group • Configuration of ARS table to route Rainbow calls." (p121)
  definition: |
    呼出路由选择表：WebRTC 网关自动配置的自动化范围之一（R4.0.020.002 起，内部/外部 GW 均自动建），
    用于把 Rainbow 呼叫路由出去；而编号计划与闭锁仍归安装员手工做。缩写未展开。
  alias_or_related: 自动配置边界清单 = 自动（网关激活/SIP 网关/SIP 账号/VoIP 接入与中继组/ARS）vs 手工（连 PBX/虚拟终端/编号计划/闭锁）
  tags: [protocol, routing]

- id: g51
  term: CSTA
  category: protocol
  source_pages: p202, p213
  source_quote: |
    "1 Dial '31000' from Dialpad or Call History … 2 MakeCall API … 3 MakeCall API (CSTA) OXE, OXO CE" (p202)
  definition: |
    Teams 集成中呼叫 PBX 内部分机时所用的计算机电话集成接口：Rainbow App 发起 MakeCall API，PBX 侧
    以 CSTA（计算机电话集成 API）落地。仅出现在 Teams 拨号流程图，缩写未展开。
  alias_or_related: 外线呼叫路径则经 g07 WebRTC Gateway（p203），两图对照记忆
  tags: [protocol, ctinteg, teams]

- id: g52
  term: DTMF
  category: protocol
  source_pages: p204, p220
  source_quote: |
    "During the call, the control panel on desktop allows to Mute, Send DTMF or End Call in one-click" (p204)
  definition: |
    双音多频（缩写未展开）：Teams 集成场景下从 Rainbow Desktop 控制面板在通话中一键发送 DTMF
    （如 IVR 按键）的能力点。
  alias_or_related: 与 Mute/End Call 并列的通话中操作
  tags: [protocol, teams]

# ── 六、网站与资源名 (resource) ──

- id: g53
  term: openrainbow.com (web.openrainbow.com)
  category: resource
  source_pages: p4, p84, p86, p103
  source_quote: |
    "Domain name Leave the default value: openrainbow.com" (p86, OMC/Cloud/Rainbow 域名字段)
    "Log in to the Rainbow interface … https://web.openrainbow.com" (p84, p103)
  definition: |
    Rainbow 平台默认域名：OXO 接入时 OMC 域名字段保持默认 openrainbow.com（勿改）；
    web.openrainbow.com 是网页版客户端入口（管理员与成员实验均从这里登录）。Rainbow 平台发信
    （邀请邮件）来自 noreply@openrainbow（p93）。
  alias_or_related: help/status/pilot/developers 为同域不同子域（g54/g55/g56/g58）
  tags: [resource, website, domain]

- id: g54
  term: help.openrainbow.com
  category: resource
  source_pages: p34, p36, p57, p65, p183
  source_quote: |
    "Many answers tou your questions are available on the Rainbow support website. Rainbow support
    https://help.openrainbow.com/" (p34, 'tou' 为原文笔误)
  definition: |
    Rainbow 支持站点（Help Center）：本书反复引用的文档源——网络要求文章（p36）、Features List/
    Administration 与 Rainbow plans 页签（p57/p65）、Help Desk Guide（排障指南，p183）都在这里。
  alias_or_related: Features List = 订阅与管理员角色的权威对照表（p57/p65 指定入口）
  tags: [resource, website, support]

- id: g55
  term: status.openrainbow.com
  category: resource
  source_pages: p186
  source_quote: |
    "A dedicated 'Operations' team constantly monitors the smooth running of the Rainbow platform (24/7).
    Nevertheless, in exceptional cases, a malfunction in our Data Centers may occur. In this case, you can
    be informed via the following specific site: … The button 'Get updates' allows… you can subscribe to
    alerts by different methods." (p186)
  definition: |
    Rainbow 云服务状态页：数据中心故障时的官方信息源；可经 "Get updates" 订阅告警并按主题/地理区域
    过滤（法国建议勾 WW/EMEA/DE）。配合管理端即将进行的计划维护公告使用（p187）。
  alias_or_related: 计划维护公告在管理端 "Operations" 区（p187），非本站
  tags: [resource, website, status]

- id: g56
  term: Rainbow Pilot
  category: resource
  source_pages: p41-44
  source_quote: |
    "RAINBOW PILOT allows you to assess your Rainbow connectivity from your location, and the capacity of a
    given location to handle a population of Rainbow users characterized by a flexible mix of usages between
    Collaboration, Conferencing, Hybrid or Hub telephony. • link: https://pilot.openrainbow.com/home" (p42)
  definition: |
    官方连通性与容量评估工具（pilot.openrainbow.com）：从客户现场测 Rainbow 连通性，并按协作/会议/
    混合话音/Hub 话音的用量组合评估站点可承载的 Rainbow 用户规模——售前勘测工具，与网络要求文档
    （g61）配合使用。
  alias_or_related: 用法组合口径含 "Hub telephony"（另见 g61 相关注）
  tags: [resource, tool, presales]

- id: g57
  term: MyPortal
  category: resource
  source_pages: p135, p137, p139, p144, p190-193
  source_quote: |
    "Connect to MyPortal • Support > Service Request • Click on Create SR: • SR category= Rainbow • SR type
    = product support • Severity • Subject • Mail + Description" (p192)
    "Details about Front-End mode configuration in document Rainbow WebRTC cookbook available on MyPortal" (p135)
  definition: |
    ALE 客户服务门户（ALE Customer Service Portal，p192 自称）：三条用途——下载 WebRTC 网关虚拟机
    （OVF/ISO，p139/p144）、查阅 Rainbow WebRTC cookbook（p135/p137）、开 Service Request（SR），
    需填 Rainbow 版本、SIP trunk 子类别等；前提是伙伴已过 Rainbow 认证（p191，ESR 才会创建）。
  alias_or_related: SR/ESR（服务请求，并入本条）；认证前提同 g41
  tags: [resource, portal, support]

- id: g58
  term: developers.openrainbow.com
  category: resource
  source_pages: p30
  source_quote: |
    "https://developers.openrainbow.com/" (p30, CPaaS 分区页脚)
  definition: |
    Rainbow CPaaS 开发者门户：与 p30 "Open APIs & SDK for easy business apps integration" 对应，
    是 Rainbow 作为通信平台开放 API/SDK 能力的入口。本书仅此一处引用。
  alias_or_related: 隶属 g01 Rainbow 的 CPaaS 定位
  tags: [resource, website, cpaas]

- id: g59
  term: TC2479
  category: resource
  source_pages: p123, p169
  source_quote: |
    "TC2479 Rainbow WebRTC Gateway with OXO Connect / OXO Connect Evolution" (p123, 拓扑部署步骤页引用)
    "Consult the technical communication for the OXE (TC2462) or OXO Connect (TC2479) for Rainbow
    configuration" (p169)
  definition: |
    OXO Connect 的官方技术文档（Technical Communication）：Rainbow WebRTC 网关与 OXO/OCE 集成的权威
    配置文档，本书拓扑决策与话务台章节均指向它；OXE 侧对应文档为 TC2462。
  alias_or_related: TC2462 = OXE 侧对应文档（并入本条）
  tags: [resource, document]

- id: g60
  term: Rainbow WebRTC cookbook
  category: resource
  source_pages: p135, p137
  source_quote: |
    "For this it is essential to follow the document 'Rainbow WebRTC cookbook' latest edition available on
    MyPortal. This document describes the specifics of the different use cases. The commissioning of an
    OCE-FE can be done with different scenarios: New complete installation PBX + OCE-FE / Adding OCE-FE to
    an existing PBX…" (p137)
  definition: |
    MyPortal 上的 WebRTC 网关落地手册（必须用最新版）：详述各用例差异（全新安装 PBX+OCE-FE、向既有
    PBX 加装 OCE-FE（含 R4 前旧版本情形）、有无 Partner fleet 参考下单等场景）。FE 配置细节以它为准。
  alias_or_related: 下载入口 = g57 MyPortal；"Link for ALE collaborators"（p135/p137，内部链接）
  tags: [resource, document, cookbook]

- id: g61
  term: Rainbow Network Requirements
  category: resource
  source_pages: p35-40
  source_quote: |
    "This document details: The ports and protocols used by the Rainbow collaboration, Rainbow hybrid and
    Rainbow Hub solutions • Operating principles and flows • Detailed list of ports and protocols • Rainbow
    domains and associated IP addresses • Bandwidth requirements • Configuration of corporate network
    elements • DNS, Proxy, Firewall..." (p40)
  definition: |
    官方网络要求文档（help.openrainbow.com 文章 + 两个 PDF，其一为健康数据托管版）：覆盖协作/混合
    话音/Hub 三方案的端口协议、域名 IP、带宽与防火墙/DNS/代理配置，并注明基础设施更新流程与版本
    变更说明——生产化的网络前提以它为准，本书只给指针。
  alias_or_related: Rainbow Hub 仅在本文档与 p42/p187 以名称出现，全书无定义（passing mention）
  tags: [resource, document, network]

- id: g62
  term: RLAB / POD
  category: resource
  source_pages: p9-19
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data
    center… RLAB environment POD n … POD 1 … Common resources: NAS (Softs, licenses,..), SIP Simulator.
    Pods are independent of each other • Pods have the same configuration • Pods have access to common
    resources." (p11)
  definition: |
    ALE 培训远程实验室（RLAB）：按 POD 划分的同构实验单元（每 POD 一台 Windows 11 Client PC VM +
    OXO Connect Evolution），POD 间互相独立、共享公共资源（NAS 软件许可库 + ITSP1 SIP 模拟器）。
    教学专用基础设施；实验网段 192.168.1.x，Client PC 192.168.1.10，OXO 192.168.1.246。
  alias_or_related: SIP Simulator = g44 ITSP1；Rlab portal 用户指南（p11 引用）
  tags: [resource, lab, training]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列候选术语逐条核对

说明：OVERVIEW 质量门自记"17 个术语"，但其术语表实际为 **16 行**（差额 1 无法对应，疑把"内部/外部/OCE-FE GW"计数为多行所致）。按 16 行逐条核对如下——

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| Rainbow | 正文有明确定义（p29） | g01 |
| Company | 有明确定义（p47-48） | g02 |
| Subscription | 有明确定义（p33 逐一定义 8 种 + p63-68 开通分配） | g25-g31（展开为 7 条） |
| RCC (Remote Call Control) | 有明确定义（p6/p112） | g06 |
| WebRTC Gateway | 有明确定义（p118） | g07 |
| 内部/外部/OCE-FE GW | 有明确定义（p118 拓扑 + p121-122 自动配置 + p129 容量对比表） | g07 / g33 / g34 / g35 |
| Free Rainbow in Twinset | 有明确定义（p123/p156-157） | g08 |
| Anydevice | 有明确定义（p123/p155-158/p169） | g09 |
| Rainbow number | 有明确定义（p115，p233 重现） | g13 |
| PBXID & Activation code | 有明确定义（p83-86/p134） | g14 |
| Supervision group | 有明确定义（p164/p167） | g10 |
| Mutual aid group | 有明确定义（p171/p173/p180） | g11 |
| Visibility 四级 | 有明确定义（p52） | g03 |
| Rainbow Pilot | 有明确定义（p42） | g56 |
| UTL | 有定义性用法（p123/p129/p156 许可口径），但全书未展开全称 | g15（full_name 已如实省略） |
| FTR | 有定义性用法（p128/p130-131/p134），但全书未展开全称 | g16（full_name 已如实省略） |

结论：**16 行全部"本书正文有明确定义"，无"仅 passing 提及需排除"项，无"书中实际未出现"项，无删除建议。** 下游建议以本表 62 条为术语基准（OVERVIEW 的"17 个"计数建议更正为 16 行）。

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：UCaaS/CPaaS（并入 g01）、SSO（g04）、TOTP（g05）、Business Directory（g17）、Information Channels（g18）、Grace period（g19）、Multiset（并入 g08）
- 角色：BP/DR/IR/VAD/EC（g20-g24，p48 一页全定义）
- 订阅计划名：Essential/Business/Enterprise/Attendant/Enterprise Conference/Conference/Connect/Room（g25-g31）
- 产品/组件：OXO Connect + Power CPU EE（g32）、OCE + IPBox + OXO CE（g33）、OCE Front End（g34）、NUC（g35）、OMC（g36）、Webdiag（g37）、Cloud Connect + RB WebAdmin + Fleet Dashboard（g38）、ccrbagent.log（g39）、TURN（g40）、Emily BOT（g41）、MicroSIP（g42）、IPDSP（g43）、ITSP1（g44）、OXE + REX（g45）
- 协议/技术：SRTP+HTTPS（g46）、SIP Trunk（g47）、PSTN（g48）、DDI（g49）、ARS（g50）、CSTA（g51）、DTMF（g52）
- 网站与资源：openrainbow.com/web.openrainbow.com（g53）、help.openrainbow.com（g54）、status.openrainbow.com（g55）、MyPortal + SR/ESR（g57）、developers.openrainbow.com（g58）、TC2479 + TC2462（g59）、Rainbow WebRTC cookbook（g60）、Rainbow Network Requirements（g61）、RLAB/POD（g62）

### 3. 仅 passing 提及、未单列条目的词（备查）

Rainbow Hub（p36/p42/p187，无定义，附于 g61）、bubble（p52，附于 g03）、REX（p169，附于 g09/g45）、Busy Lamp Field（p165，话务台界面区名）、RUFUS（p145，做启动 U 盘的第三方工具）、ESXi/OVF（p118/p141/p144，外部 GW 承载与镜像格式）、OXO Connectivity（p136，附于 g38）、Global Welcome Center 与 support@openrainbow.com（p191，附于 g41）、SR/ESR（p190-193，附于 g57）、noreply@openrainbow（p93，平台发信地址）、ITSP2（p22 拓扑图出现，无细节，附于 g44）。

### 4. 提取口径说明

- 所有定义只采信本书正文；UTL/OMC/FTR/DDI/ARS/CSTA/DTMF/PSTN/REX/ESR 等缩写书中未给全称，full_name 字段一律省略或标注"未展开"，不做外部补全。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准，引用均为原文摘录（p34 "tou"、p33 "0365" 为原文笔误，已注明）。
