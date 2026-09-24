# 术语/缩写/产品名候选 — Rainbow Hub (RAINXTE101EN Sprint 170 Ed16)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 70 条（任务要求全量提取：概念 29 + 角色 6 + 订阅 8 + 产品 11 + 协议 8 + 资源 8）。IPEI/CAT-iq/DTMF/MOS/IVR/DECT/SRTP 等缩写书中未给全称，full_name 字段如实省略，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: Rainbow Hub
  category: concept
  source_pages: p5-9
  source_quote: |
    "Rainbow Hub is the public version of the Rainbow platform. It allows users to migrate completely to
    the cloud thanks to a telephony system based entirely on softphone technology. ... FULL CLOUD Solution"
    (p5)
  definition: |
    Rainbow 平台的公有云版本（本书主角）：电话服务全部托管在云侧 Cloud PBX，以纯软话机技术实现"完全上云"，
    客户侧不再部署 PBX。卖点四件套——易部署（无现场 PBX、单平台管全部服务、软话机+物理 SIP 话机直连云）、
    合规（GDPR/ISO 27001/欧洲托管/不受 CLOUD Act）、全 OPEX 按用户订阅、开放架构可集成现有系统。
    与 Rainbow 混合云（连客户已有 PBX）为并列的两条产品线（p6）。
  alias_or_related: UCaaS（p4）；对照 Rainbow hybrid cloud（RAINXTE001EN 主题）；资源入口见 g63-g67
  tags: [concept, platform, core, cloud]

- id: g02
  term: Cloud PBX
  category: concept
  source_pages: p78-83, p100-104
  source_quote: |
    "The Cloud PBX is a soft SIP PBX used to: • Connect ALE and generic SIP devices (e.g. Doorphone,
    third-party DECT SIP , analog/SIP box...). • Connect a public SIP provider via a trunk to make
    external calls. • Manage telephony features • Number of call channels: unlimited • Number of telephone
    lines: unlimited ... One Rainbow company = one and only one CloudPBX" (p78)
  definition: |
    Hub 的话务核心（软 SIP PBX，云端托管）：连接 ALE 与通用 SIP 设备、经一条外部 SIP trunk 接公共运营商、
    承载全部话务特性。硬约束：一公司有且只有一个 Cloud PBX、一 Cloud PBX 只挂一条 trunk（g55）；通道与线数
    无上限。配置面：声明（名称/类型/语音引导语言/trunk/编号计划）、Call settings（溢出/闭锁/主叫 ID/紧急/
    单复线/录音提示/转移类型）、公网号码管理。声明为 BP 专属，且要求公司先有 Voice 订阅。
  alias_or_related: 声明入口 Administration/…/Comm. Servers（p100）；对应关系与前提见 n10/n11
  tags: [concept, cloud-pbx, core, telephony]

- id: g03
  term: Company
  category: concept
  source_pages: p48-55, p71-75
  source_quote: |
    "To ease collaboration between colleagues in the same company, users are gathered within the same
    Company. • Main features are only available to users who are members of a Company, and it is therefore
    a key concept in Rainbow. ... A user cannot be part of 2 different companies" (p48)
  definition: |
    Rainbow/Hub 的用户组织单元与核心概念：主功能仅对公司成员开放；成员=邮箱身份、一人只属一家公司；建司前
    要搜索查重。分 Reseller/BP 公司与 End-customer 公司两级（g30/g33），EC 公司必须挂在唯一一个 BP 名下。
    建司必填：名称、国家、时区（强制，p73）、邮址、网站、可见性、联系人等，可自定义 Logo 与横幅。
  alias_or_related: 可见性见 g04；建司流程见 c01；公司关键要素分区 p50
  tags: [concept, tenant, company]

- id: g04
  term: Visibility
  category: concept
  source_pages: p53
  source_quote: |
    "PUBLIC: a user from another company can see and invite members of your company… CLOSED : a user from
    another company cannot see the members of your company, but he can invite them via their email
    address. Your users can't see users outside their company, but they can invite them via their email
    address. ISOLATED : a user from another company cannot see the members of your company, and cannot
    invite them." (p53)
  definition: |
    公司对外可见性四级（PUBLIC/PRIVATE/CLOSED/ISOLATED），可在 company settings 改。Hub 场景官方"高度
    推荐"CLOSED——目录搜索只见同事与企业目录条目而非整个 Rainbow 社区；ISOLATED 不推荐（用户无法被外部
    组织邀请进 bubble 会议）。成员个人另有可见性设置（Same as company/none/public/private…，p168/p194）。
  alias_or_related: bubble 见 g27；实验公司统一 Closed（p72）
  tags: [concept, privacy, company]

- id: g05
  term: SSO
  full_name: Single Sign-On（书中以 SSO* 脚注展开，p54）
  category: concept
  source_pages: p54
  source_quote: |
    "you can enable single sign-on (SSO) with your Azure Active Directory, or with your corporate AD
    (ADFS). SSO can be enabled for your entire company, or only for certain users. The administrator must
    have an 'Enterprise' service level … Azure AD - SAML Azure AD - OIDC ADFS - SAML … Google Workspace –
    OIDC" (p54)
  definition: |
    公司级单点登录：标准组合四种——Azure AD(SAML/OIDC)、ADFS(SAML)、Google Workspace(OIDC，Hub 教材新增)；
    可全公司或部分用户启用，一家公司可并存多种认证方式按用户指定；配置管理员须 Enterprise 级。基于标准
    协议的其他 IdP（Shibboleth/RSA/LemonLDAP/OKTA/CAS APEREO/Ping Identity）须 ALE 确认。
  alias_or_related: 与 g06 TOTP、复杂密码并列的三类认证方式；配置手册在支持站点（书中指针）
  tags: [concept, auth, sso]

- id: g06
  term: TOTP
  full_name: Time-based One Time Password（书中直接展开）
  category: concept
  source_pages: p54
  source_quote: |
    "Authentication with TOTP (Time-based One Time Password. Users need a third-party authentication
    application (Google Authenticator, Microsoft Authenticator, Authy). This method applies to all types
    of users but is particularly recommended for the administrators" (p54)
  definition: |
    Rainbow 原生认证第二模式（另一种是 ≥12 位复杂密码传统认证）：需手机第三方验证器 App；全员可用，管理员
    账号特别推荐。注意 TOTP 在本书另有第二处用法：设备 debug 会话的一次性口令（p142/p335，登录名 admin、
    密码 one-time use only (TOTP)）——同词两义，排障文档里按上下文区分。
  alias_or_related: 设备侧一次性口令见 n24；MFA-TOTP 配置参考支持站点文章
  tags: [concept, auth, mfa, security]

- id: g07
  term: RCC
  full_name: Remote Call Control（书中展开）
  category: concept
  source_pages: p112
  source_quote: |
    "SOFTPHONE AND DESKPHONE ... RCC* — *RCC: Remote Call Control, supervision and control of the desk
    phone from the application. Outgoing calls from the desk phone, softphone or mobile" (p112)
  definition: |
    软+硬双端用户模式下，Rainbow 应用对物理话机的远程监督与控制（来话可选话机或软话机呈现，去话三端任发）。
    与混合云教材语境不同：在 Hub 里 RCC 是"话机伴随"的常规形态而非"无网关中间态"；纯软话机用户只有
    Computer（互联网呼叫）一种模式（p111），不涉及 RCC。Generic SIP 设备明确无 RCC（p117）。
  alias_or_related: 终端三形态见 f07；Generic SIP 限制见 n18
  tags: [concept, telephony, mode, devices]

- id: g08
  term: Zero Touch
  category: concept
  source_pages: p106, p134-139, p151-152
  source_quote: |
    "Myriad phones enable complete 'zero touch' management, as well as synchronization between the user
    and his fixed phone." (p106)
    "Designed for Zero-Touch deployment. Centrally configured and managed via Rainbow administration
    interface. Only one physical SIP device per user account" (p134)
  definition: |
    ALE 终端（Myriad/ALE-2/DECT）的零接触部署机制：按 MAC（话机/基站）或 IPEI（手持机）在管理端注册并
    关联成员后，设备自动从云取配置与固件；集中配置与管理全在 Rainbow 管理界面。红线：每用户一台物理 SIP
    设备、DHCP option 43/66/67 会破坏机制、LAN 内 PBX 的 TFTP 抢先、禁用设备自带 web 页配置（详见 n21/n22）。
  alias_or_related: 流程见 f10/f13；端口前提见 g 系 p32（principle）；Generic SIP 无此机制
  tags: [concept, provisioning, devices, core]

- id: g09
  term: Generic SIP device
  category: concept
  source_pages: p106, p114-123
  source_quote: |
    "A generic SIP device is a third-party SIP-compatible endpoint that can connect to Rainbow Hub.
    Examples of devices: Third-party SIP phones • Conference phones • Ata gateways • Audio doorphones •
    Dect base stations • Analog devices converted to SIP" (p116)
  definition: |
    可接入 Hub 的第三方 SIP 兼容终端（第三方话机/会议话机/ATA 网关/门铃/DECT base/模拟转 SIP）。定位为
    存量设备复用与特殊业务硬件的"补充手段"：全手工配置、无集中管理、无固件自动更新、无 RCC、仅基础 SIP
    话务；强制 TLS 1.2+SRTP（设备不支持时可关加密）、推荐 G711；ALE 不为大规模部署提供支持（详见 n18/n19）。
  alias_or_related: 配置要素（SIP 域/用户名/密码/证书链）见 c13；参考设备指南 p122
  tags: [concept, generic-sip, third-party]

- id: g10
  term: DID / DDI (public number)
  full_name: DID = Direct Inward Dialing（书中 p96 展开；DDI 为书中并用缩写，未单独展开）
  category: concept
  source_pages: p83-84, p95-96, p103-104
  source_quote: |
    "The term 'Direct Inward Dialing' (DID) is used in the world of corporate telephony. It defines
    whether a user/service ... can be reached directly via a public (external) number assigned to him/her
    personally." (p96)
    "DDI range = range of public numbers allocated to a company" (p95)
  definition: |
    公网直拨号码：分配给成员/组/话务台/欢迎服务（预通告）/IVR 的外线号码，让外部来话不经话务台直达；DDI
    段=分配给公司的公网号段。号码注入为集成伙伴职责、首个注入号默认为公司主号（n13）；外呼主叫 ID 可选
    用户公网号或公司号（p84/p102）。多站点下 DDI 地址登记（紧急定位）由 BP 向运营商申报（g20）。
  alias_or_related: 号码分配面见 p24（principle）；经理 DID 挂组级规则见 n38
  tags: [concept, numbering, did]

- id: g11
  term: Internal numbering plan
  category: concept
  source_pages: p95, p100-101
  source_quote: |
    "Internal numbering plan • Is a numbering system used in telecommunications to allocate telephone
    numbers used between employees within a company. • Internal numbers can be between 2 and 9 digits
    long ... It is possible to have numbers of different lengths • e.g. 100 to 120, 2000 to 2136, 756 to
    789" (p95)
  definition: |
    公司内线编号体系：2-9 位、可多长度混存（1xx/3xx/4xxxx/6xxxxx…）。在 Cloud PBX 声明时配置：出局前缀
    （0 或 9，国家相关）、成员号首位、号长（默认 3）、可混多段；"Optimized phone dialing" 可让话机免拨
    出局前缀（国家相关，需与 ALE 确认）。编号计划的"设计方法论"书内不讲（见 BOOK_OVERVIEW 批判）。
  alias_or_related: 拨号计划参数见 p22（principle）；出局前缀与紧急呼叫的交互见 g20
  tags: [concept, numbering, telephony]

- id: g12
  term: Traffic control (Barring)
  category: concept
  source_pages: p85-87, p93, p97
  source_quote: |
    "In addition to the existing traffic barring mechanisms, the admin is able to manage his own lists.
    •Each list contains a list of prefixes: •Whitelist: only dialed number starting with these prefixes
    are authorized for outbound calls •Blacklist: all dialed number starting with these prefixes are
    forbidden for outbound calls. These lists apply either to the entire company, or to specific users."
    (p85)
  definition: |
    呼出闭锁两层：公司级 Call settings 的允许/屏蔽档位（仅内线/国内+内线/国际+国内+内线；无/收费号/自定义
    清单，p82）+ 管理员自定义白/黑名单（按前缀、国际格式不带 + 或 00、可全公司或按用户，p85-86）；成员级
    在 Telephony 页签可查改（Same as company 覆盖机制，p195-196）。Barring 术语定义：按员工画像限制外呼
    （禁国际/移动/收费号等，p97）。
  alias_or_related: 紧急号码对受闭锁用户放行（g20）；格式规则见 p25（principle）
  tags: [concept, barring, security, telephony]

- id: g13
  term: Personal routines
  category: concept
  source_pages: p8, p173-174, p206
  source_quote: |
    "Members can set personal routines • Predefined and customizable scenarios allowing to modify
    simultaneously your presence, caller ID and forwarding status." (p173)
  definition: |
    个人例行程序：把在场状态、主叫 ID、呼叫设备、呼转与目的地、退组五类参数打包成一键场景；预置 At Work/
    Do Not Disturb/On Break/Out of office（p8）。示例脚本：DND→全部来话转助理；Out of office→转手机+在场
    Away。成员端（头像→Personal routines→Configure）与管理端均可配；话务台监督员也能改被监督成员的例行
    程序（p246）。
  alias_or_related: 机制见 f16；CSV 批量供应可带例行程序相关字段（成员模板）
  tags: [concept, routines, presence, forwarding]

- id: g14
  term: Key groups
  category: concept
  source_pages: p182-187
  source_quote: |
    "You can easily assign programmable keys to Cloud PBX desk phones and the Rainbow softphone
    application by creating key groups • For desk phones: supported keys include speed dial, supervision,
    call forwarding, audio hub functions… • For Rainbow app softphone: direct call keys are available."
    (p183)
  definition: |
    按键组：把可编程键（话机键：速拨/监督/呼转/Audio Hub；应用键：直呼键）打包成组、排序后批量分配给成员
    （应用键组与话机键组两个分配位）；批量供应 CSV 建用户时可用两列直接带组。成员级亦可单配（Prog keys
    页签：应用 Speed dial / 设备键 speed dial 或 supervision，目的地 member 或 group，p203-205）。
  alias_or_related: 机制见 f17；单配流程见 c06 步骤 5-6
  tags: [concept, keys, provisioning]

- id: g15
  term: Business Directory
  category: concept
  source_pages: p61, p179
  source_quote: |
    "you can create a 'Business Directory' containing the contacts of external companies or organizations
    that are useful to all your users, along with their phone numbers. • The quality of reception will be
    improved thanks to the caller identification during the call presentation" (p61)
  definition: |
    公司级外部联系人目录（补充 Azure AD 之外），存外部公司/组织联系人及号码，提升来话弹屏主叫识别。默认
    客户管理员管理、可委托非管理员；手工建或 CSV 批量导入（样例文件+导入报告）；LDAP 连接器可把 AD 联系人
    自动同步进来（g52）。CLOSED 可见性下目录搜索只出同事与该目录（p53）。
  alias_or_related: 对照成员目录（内部同事）；委托与导入规则见 p14（principle）
  tags: [concept, directory, caller-id]

- id: g16
  term: Information Channels
  category: concept
  source_pages: p62
  source_quote: |
    "Similar to news feeds, they allow to to distribute information to a range of users • Users can
    create, search and join a specific channel … Only users with an 'Enterprise' service level can create
    Information Channels. ... Members will not be able to unsubscribe." (p62，"allow to to" 为原文重复照录)
  definition: |
    公司信息频道（类新闻源）：先在 Roles 页签授权再创建，创建者须 Enterprise 服务等级；可建公司全员或指定
    成员自动订阅的强制频道（不可退订），也可建面向本公司+其他公司全体 Rainbow 用户的开放频道。
  alias_or_related: 强制订订边界见 n07；与 Teams 集成的"信息频道"无关
  tags: [concept, channel, admin]

- id: g17
  term: Grace period
  category: concept
  source_pages: p168, p176
  source_quote: |
    "When you delete a user, his or her status becomes 'Suspended' for a period of 10 days (called the
    'grace period') … Without any action from you, the account will be deleted after 10 days." (p176)
  definition: |
    成员删除的 10 天缓冲期：期间可恢复（误删）或彻底删除；不动作则 10 天后自动永久删除。恢复的代价：订阅
    已随删除回收、账号回落 Essential（免费）模式，须重新分配许可并重挂电话线；10 天内该邮箱不可复用于
    新建账号（p168 报错提示）。
  alias_or_related: 副作用全集见 n29
  tags: [concept, members, lifecycle]

- id: g18
  term: Hunt group
  category: concept
  source_pages: p210-217, p233-235
  source_quote: |
    "A group allows to reach several phones (users) calling a single number. Incoming calls are routed
    according to the distribution type" (p210)
    "50 users per group ... One Internal number (mandatory) and one DDI number (facultative) can be define
    per group" (p212)
  definition: |
    呼叫组：一个号码达多个成员，分发三型 Parallel（同振）/Serial（顺序轮转）/Circular（循环轮转，轮转默认
    10 秒）；可带（g19）或不带等待队列；每组建/改时配溢出（8 种目的地）、录音档、锁末位成员、允许组管理员
    改 DDI；成员可跨组、可随时退组。组建时自动生成对应 bubble（g27）承载组留言与通话记录。有 Regular 与
    Attendant 两个子型（Subtype，p209/p234）。
  alias_or_related: 分类见 f18；参数全集见 p41（principle）；角色见 g34
  tags: [concept, groups, telephony, core]

- id: g19
  term: Waiting queue
  category: concept
  source_pages: p215-216
  source_quote: |
    "In a group WITH waiting queue • The caller is put on hold until an agent can handle the call ... the
    oldest call on hold is presented (first come, first served), after a 10 sec delay • If the waiting time
    exceeds the overflow time (adjustable from 10 to 900 sec), the call is overflowed" (p215)
  definition: |
    Hunt group 的可选排队机制：无队列组全员占线即溢出；有队列组先播"尽快接听"提示、按 FCFS 在 10 秒延迟后
    把最老来话派给空闲坐席，等待超时（10-900 秒可调）后按组策略溢出，可设"组空即立即溢出"。坐席与管理员
    可见实时队列状态（可接坐席数/进行中呼叫/排队数与最长等待，p216）。
  alias_or_related: 建组 Type 选 "hunt group with waiting queue"（p234）；队列规格见 p41（principle）
  tags: [concept, queue, hunt-group]

- id: g20
  term: Emergency numbers & Emergency group
  category: concept
  source_pages: p226-229, p238-242
  source_quote: |
    "Numbers automatically configured according to • Company country • Trunk group associated with the
    Cloud PBX. Allows calls to emergency numbers • Without dialing the outbound prefix ... Emergency
    numbers are reserved and cannot be changed." (p227)
    "Standard group of members tagged 'emergency group'. Only one emergency group. Active or not" (p228)
  definition: |
    紧急呼叫机制两件：号码表按公司国家+trunk 组自动配置（免出局前缀可拨、受闭锁用户放行、可录音、号码保留
    不可改不可占作内线）；紧急组=打了 emergency 标记的标准组（一公司唯一、激活后免前缀紧急呼叫路由进组而
    非外线，组员转公共紧急号须加前缀如 0112）。地理定位责任链：BP 购号时向运营商数据库登记 DID 地址、
    运营商判定 PSAP（g62），Rainbow 不管。
  alias_or_related: 创建两法差异见 n40；激活语义见 n39
  tags: [concept, emergency, compliance]

- id: g21
  term: Manager/Assistant group
  category: concept
  source_pages: p218-222, p236-237
  source_quote: |
    "Allow to an assistant to filter and take Manager's calls. ... This type of group is necessarily
    single-Manager. To create a multi-Manager group, it is necessary to create several groups (an
    assistant can belong to different groups)." (p219)
  definition: |
    经理-助理组：助理过滤并代接经理来话；必然单经理（多经理=建多组，助理跨组实现 1 助理管多经理）；溢出链
    经理→助理1→助理2；仅电话呼叫被筛（Rainbow 音视频不筛）；经理要被筛其 DID 必须配组级；组管理同 hunt
    group（内线/公网/录音/溢出/成员/提示音，溢出提示音 5-30 秒可定制）；组类型建组时 Type=Hunt Group、
    Subtype=Manager/Assistant。
  alias_or_related: 边界见 n38/n35；应用两视图（经理/助理）p220
  tags: [concept, groups, manager-assistant]

- id: g22
  term: Supervision group
  category: concept
  source_pages: p223-225, p247, p287
  source_quote: |
    "Members and supervisors are divided into groups ... Each supervision group includes • One or several
    supervisors : • Members to be supervised ... Limits: • 5 supervision tabs for one user • 30 members in
    a group (Supervisors + Supervisees) • A user can be a supervisor in up to 5 groups" (p224)
  definition: |
    监督组：监督员与被监督成员同组，支撑话务台监督/代接/转移与成员例行程序修改。监督员订阅分级：Voice
    Attendant 得完整话务台（含 10 路排队），Voice Business/Enterprise 只有监督-代接-转移。硬规格：每用户
    5 个监督页签、每组 30 人（监督员+被监督者合计）、一人最多任 5 组监督员。建组入口 Communication/
    Supervision（p287）。
  alias_or_related: 话务台见 g23；规格见 p43（principle）；设备限制见 n43
  tags: [concept, supervision, attendant]

- id: g23
  term: Attendant console
  category: concept
  source_pages: p164, p246, p284-289
  source_quote: |
    "ATTENDANT CONSOLE • 10 simultaneous calls – Full softphone • Supervision / pickup / Users routines
    modification" (p164)
    "Attendant Console allows to • Monitor the state of supervised members (presence and phone activity) •
    Manage calls for supervised members (call pickup and call transfer) Up to 10 calls on hold" (p246)
  definition: |
    PC 端话务台（Rainbow 应用，需 Voice Attendant 订阅）：监控被监督成员（在场+话务活动）、代接/转移、
    10 路保持、改成员例行程序；三档显示 Normal/small/condensed。硬约束：Voice Attendant 用户不能用手机端
    话务台、不能用话机（激活后话机关联被删）。相关联的 attendant group=话务组（Subtype=Attendant 的
    hunt group，成员须 Voice Attendant，可加预通告，p249）。
  alias_or_related: 订阅见 g41；监督结构见 g22；启用流程见 c10
  tags: [concept, attendant-console, telephony]

- id: g24
  term: Welcome service
  category: concept
  source_pages: p250-261, p277-283
  source_quote: |
    "Combination of a calendar and voice prompts to welcome your callers, to inform them of the closing of
    your offices or of a service" (p251)
    "One or several welcome services can be configured. Each of them is associated with a public number
    and has its own calendar to manage opening and closing days & hours." (p258)
  definition: |
    欢迎服务=日历+语音提示的组合体：绑一个公网号与一份日历；开时段播欢迎引导（pre-announcement）后路由到
    成员/带队列组/话务台/AA/直转留言；闭时段路由到闭店提示音/成员/组/外线/另一欢迎服务/AA；支持人工强制
    开/闭（forced 态、下个时段回 Auto）与定制时段提示（≤5 条、特殊日 ≤10 天）。日历必须先建；法定假日不
    预填。四件套关系见 f27。
  alias_or_related: 日历规则 p48（principle）；素材限制见 n45；配置见 c09
  tags: [concept, welcome-services, core]

- id: g25
  term: Automated attendant (IVR)
  category: concept
  source_pages: p265-275, p290-300
  source_quote: |
    "AUTOMATED ATTENDANT - IVR • Each IVR has a maximum of 3 levels, each allowing a DTMF selection from
    0 to 9. • The root menu contains 10 configurable entries. ... You can create as many IVRs as you like
    - there are no limits or licenses on this service" (p266)
  definition: |
    自动话务员：DTMF 自助路由（0-9、*、#），最多 3 级、根菜单 10 项，目的地可为组（带/不带队列）/成员/
    另一 IVR 菜单/欢迎服务；数量无限、无许可。两种入口——直挂公网号（7×24，可选 6 种溢出目的地）或经
    欢迎服务（受日历控制，IVR 不带 DID）。语音提示两模式：每菜单唯一提示（强烈推荐、建后不可改）或每选项
    +每动作分条录音。保密规则：来话显示默认名而非欢迎服务技术号。
  alias_or_related: 入口语义见 n46；规格见 p47（principle）；配置见 c11
  tags: [concept, ivr, aa, telephony]

- id: g26
  term: Sites
  category: concept
  source_pages: p92-93, p171, p301-316
  source_quote: |
    "Each site is associated with: • One or more members of the company • One or more public numbers ...
    Configure a default public number for a site ... Custom music on hold per site." (p303)
  definition: |
    多站点概念：单 Cloud PBX 下的逻辑分区——站点挂成员（成员 Information 的 Sites 字段）、公网号与可配号
    服务（组/欢迎服务/AA 经号码归属）；可设站点默认公网号（未配个人号的站点成员外呼显示站点号）与站点级
    音乐保持。不变量：内呼互通、组可跨站、欢迎服务/AA 与目录全公司共用、号码可兼任公司主号与站点主号、
    不强制全员挂站。
  alias_or_related: 结构图见 f30；参数规则见 p28（principle）；实验见 c12
  tags: [concept, multi-site, sites]

- id: g27
  term: Group bubble
  category: concept
  source_pages: p217
  source_quote: |
    "When a group is created, an exchange bubble is automatically created. It includes all the members of
    the group, in order to allow : • Instant messaging, file sharing • Conferences between group members •
    Management of the group's voice messages • Access to call logs." (p217)
  definition: |
    组协作空间：每个组建组时自动生成对应 bubble，含组内全员，用于群内 IM/文件/会议、组语音留言管理（留言
    自动以音频文件转入）与组通话记录查看；bubble 内全员权限相同。另在可见性语境中 bubble 一词也泛指
    Rainbow 会议/群聊（p53 "conferences (bubbles)"）。
  alias_or_related: 机制见 f22；ISOLATED 对外部 bubble 邀见的影响见 n05
  tags: [concept, bubble, collaboration]

- id: g28
  term: CDR
  full_name: Call Detail Record（书中展开，p318/p318 标题 "CALL DETAIL RECORD (CDR)"）
  category: concept
  source_pages: p318
  source_quote: |
    "They are generated (.csv) for all calls going through the Cloud PBX • Incoming, outgoing and internal
    calls are taken into account • Pure VoIP Rainbow audio/video call doesn't generate CDR ... Each month,
    the first, ALE provides Call Details Records in a file. Three ways for the partner to obtain these
    files • ALE pushes monthly mails with attached files • The BP retrieve manually ... • The BP retrieve
    automatically the files using REST APIs" (p318)
  definition: |
    话单：覆盖经 Cloud PBX 的入/出/内部呼叫（纯 Rainbow VoIP 呼叫不产生）；ALE 每月 1 日出文件，BP 经月度
    邮件/网页手工/REST API 三通道获取，用于计费（ALE 不计费不开票）。细节文档 TBE099（g68）。
  alias_or_related: 口径见 p49（principle）；边界见 n50
  tags: [concept, cdr, billing, analytics]

- id: g29
  term: MOS
  category: concept
  source_pages: p319, p328
  source_quote: |
    "VoIP call quality (MOS index), overall, or for a given user" (p319)
    "All calls (telephone or Internet) Quality tickets are collected at the end of a call (enabled by
    default). The MOS scores are integrated into the audio quality dashboards. ... Jitter: under 30ms the
    level is acceptable • RTT: latency must not exceed 150ms • Packet loss: must not exceed 1%" (p328)
  definition: |
    话音质量指数：每次呼叫结束自动采集质量票（默认启用），汇入音质量仪表盘，支撑逐用户排障与网络/防火墙
    问题定位；技术明细页可过滤。推荐阈值：抖动 <30ms、RTT ≤150ms、丢包 ≤1%。缩写未在书中展开全称。
  alias_or_related: 阈值口径见 p51（principle）
  tags: [concept, quality, mos, analytics]

# ── 二、角色 (role) ──

- id: g30
  term: BP (Reseller)
  full_name: ALE Business Partner（书中展开，p49）
  category: role
  source_pages: p48-49, p58, p65, p229
  source_quote: |
    "ALE Business Partner (BP) … Most administration operations can be performed by both the Business
    Partner and the customer administrator. However, the following actions can only be performed by the
    BP: • Declaration & activation of a Cloud PBX (or traditional PBX) • Opening of paid subscriptions •
    Declaration of terminals (Deskphones or DECT) • Addition or portability of telephone lines" (p49)
  definition: |
    ALE 业务伙伴（Reseller 公司）：Hub 交付的总承包角色——独占四项操作（Cloud PBX 声明激活/付费订阅/终端
    声明/电话线加装携转），按三步配置客户公司（建司→分订阅→配 Communication）；同时承担 PSTN 话务提供、
    客户管理与计费（p88/p318）、DID 地址登记（p229）。Reseller administrator=BP 管理员（p58 同义使用）。
  alias_or_related: 权责矩阵见 p13（principle）；对照 g33 EC；语音流量商务模式见 p26（principle）
  tags: [role, reseller, bp]

- id: g31
  term: DR / IR
  full_name: Direct Reseller / Indirect Reseller（书中展开，p49）
  category: role
  source_pages: p49
  source_quote: |
    "IR Indirect Reseller / DR Direct Reseller ... The customer's integration partner must be either a
    'DR' or an 'IR'. Its name appears in the 'My company / Dashboard' screen." (p49)
  definition: |
    直接/间接经销商：客户集成伙伴的两种合法身份（二选一），名字显示在 My company/Dashboard。书中仅给出
    名称与准入要求，无更多操作差异说明。
  alias_or_related: 见 g30 BP、g32 VAD、g33 EC
  tags: [role, reseller]

- id: g32
  term: VAD
  full_name: Value Added Distributor（书中展开，法语括注 wholesaler）
  category: role
  source_pages: p49
  source_quote: |
    "VAD Value Added Distributor (wholesaler)" (p49)
  definition: |
    增值分销商：经销层级图中最靠近 ALE 的一级（ALE → VAD/DR/IR → EC）。书中仅列名，无专属操作说明。
  alias_or_related: 见 g30/g31/g33
  tags: [role, distributor]

- id: g33
  term: EC (End Customer / customer administrator)
  full_name: End Customer（书中展开，p49）
  category: role
  source_pages: p49, p59-60, p72
  source_quote: |
    "CUSTOMER ADMINISTRATORROLES • Customer administrators can create/modify/delete a large number of
    parameters related to their own company, with the exception of : • Creation of the company •
    Allocating subscriptions to your company • Creation of the Cloud PBX • Create public numbers (DID) •
    Create extensions" (p59)
  definition: |
    最终客户公司（EC）：必须挂在唯一一个 BP 下。客户管理员（customer administrator）管本公司日常——公司
    资料、成员与用户声明、设备关联、组、专业目录、公共频道、欢迎服务、话务台、IVR 等；不能建公司/分订阅/
    建 Cloud PBX/建公网号/建分机（BP 专属）。实验中 aliceX 任客户管理员（p72）。
  alias_or_related: 对照 g30 BP；Roles 页签可配多管理员（p60）
  tags: [role, end-customer, admin]

- id: g34
  term: Agent / Administrator (group roles)
  category: role
  source_pages: p209, p212-214
  source_quote: |
    "Agent role / Administrator role — Receive group calls ◼ X ... Add or remove a member X ◼ ... Force
    open or close a group-related Welcome Service X ◼ ... Note that it is possible to give an «
    administrator » role to someone who does not take calls" (p214)
  definition: |
    组内两角色：Agent 接组来电、可改自己状态（withdrawn/active）；Administrator 管理组（加减成员、改公网号、
    改溢出模式与时长、黑名单增删、强制开关组关联欢迎服务、看统计、挂起/激活坐席）且也可接听（可双角色）。
    只授 Administrator 的人不接组来电，坐席侧视其为"永久已退组"。Attendant 组全员须 Voice Attendant 许可
    （g41）。
  alias_or_related: 权限矩阵见 f21；Manager/Assistant 组用另一对角色（g35）
  tags: [role, groups, hunt-group]

- id: g35
  term: Manager / Assistant (group roles)
  category: role
  source_pages: p218-220
  source_quote: |
    "The Manager can: • Receive calls • Be notified only • Activate/deactivate screening. The Assistant
    can: • Activate/deactivate call filtering of the manager • Pickup manager calls • Manage multiple
    managers" (p220)
  definition: |
    经理-助理组的应用角色：经理可接听/仅通知/开关筛选；助理可开关经理的呼叫筛选、代接经理来电、管理多个
    经理（跨多组实现）。任何有内线号+设备的成员都可任经理或助理。
  alias_or_related: 组结构见 g21；筛选边界见 n38
  tags: [role, groups, manager-assistant]

# ── 三、订阅计划 (subscription)，均定义于 p67 订阅总表 ──

- id: g36
  term: Voice Phone
  category: subscription
  source_pages: p9, p66-67
  source_quote: |
    "Voice Phone — Telephony on hardphone only — All telephony features from a hardphone without access to
    the Rainbow application. — Devices: Hardphone only (desktop or DECT)" (p67)
  definition: |
    纯硬话机订阅：话机/DECT 上的全部话务特性，无 Rainbow 应用访问。四档 Voice 订阅中唯一的"无软话机"档，
    适合会议室话机等场景。
  alias_or_related: 分配号码同样要求 Voice 订阅（p194 Warning 含本档）；对照 g37
  tags: [subscription, telephony]

- id: g37
  term: Voice Business
  category: subscription
  source_pages: p9, p67
  source_quote: |
    "Voice Business — Telephony on PC, smartphone, phone + calls interception + Collaboration — All
    enterprise telephony features from a hardware phone and/or the Rainbow application (PC and
    smartphone). Collaboration features ... group messaging, presence, files sharing." (p67)
  definition: |
    三端话务入门档：话机+Rainbow 应用（PC/手机）全部企业话务特性 + 代接（calls interception）+ 协作（群消息/
    在场/文件共享）。也是声明 Cloud PBX 的最低订阅门槛之一（p75：至少一条 Voice Business 或 Voice
    Enterprise）。
  alias_or_related: 对照 g38 Enterprise；监督权限分级见 g22
  tags: [subscription, telephony]

- id: g38
  term: Voice Enterprise
  category: subscription
  source_pages: p9, p67
  source_quote: |
    "Voice Enterprise — Voice Business + Videoconference + call supervision and pick-up — All Voice
    Business features plus call supervision and pick-up, and video conferencing features up to 120
    participants and 49 videos." (p67)
  definition: |
    Business 全量 + 监督代接 + 视频会议（至 120 与会者、49 路视频）。实验标配（每公司 4 条，p17）；AAD 批量
    导入要求的 "Voice Enterprise 服务等级" 即本档（p167）；监督员持本档有监督-代接-转移（无话务台排队，
    p224）。
  alias_or_related: 对照 g39 Attendant；实验口径见 n08
  tags: [subscription, telephony]

- id: g39
  term: Voice Attendant
  category: subscription
  source_pages: p9, p67, p246, p249, p285-286
  source_quote: |
    "Voice Attendant — Voice Enterprise + Attendant Console — All Voice Enterprise features plus the
    Attendant Console available on the PC Rainbow application. This subscription does not support
    hardphones. — Devices: PC only" (p67)
  definition: |
    话务台订阅：Enterprise 全量 + PC 端话务台；不支持硬话机（设备=PC only）。持本档的用户被锁在 PC：不能
    用手机端话务台模式、不能用话机，激活话务台后话机关联被删（n43）。Attendant group 全员须持本档（p249）；
    监督员持本档得完整话务台含 10 路排队（p224）。实验按 Monthly 开（p285）。
  alias_or_related: 话务台见 g23；监督组见 g22
  tags: [subscription, attendant]

- id: g40
  term: Voice Enterprise Dial-In Pack
  category: subscription
  source_pages: p67
  source_quote: |
    "Voice Enterprise Dial-In Pack — Voice Enterprise + PSTN conference with local numbers over 50
    countries — All Voice Enterprise features, plus conference calling for up to 120 participants, with
    local numbers available in over 50 countries." (p67)
  definition: |
    Enterprise 全量 + PSTN 电话会议（本地号码覆盖 50+ 国家、至 120 与会者）。书中仅此一处定义，无部署细节。
  alias_or_related: 与 g45 Rainbow Room 的会议场景分工：本档按用户、Room 按会议室
  tags: [subscription, conferencing]

- id: g41
  term: Rainbow Room
  category: subscription
  source_pages: p9, p67
  source_quote: |
    "Rainbow Room — Turn any meeting room into a conference room — Dedicated video-conferencing platform
    for conference rooms — Devices: Specific Android TV box" (p67)
  definition: |
    按会议室的订阅：把会议室变成视频会议室，专用视频会议平台，设备为特定 Android TV box。书中无部署细节
    （混合云教材的 Room 订阅含"额外硬件、ALE 提供音视频套件"表述，本版简化为 Android TV box 一行）。
  alias_or_related: 对照 g40 Dial-In Pack
  tags: [subscription, room]

- id: g42
  term: Rainbow Alert
  category: subscription
  source_pages: p67
  source_quote: |
    "Rainbow Alert — Alerting — Optional alerting service plan : bypass Rainbow « Do not Disturb »,
    persistent visual notifications and audio beeps, alert acknowledgment. — PC or smartphone" (p67)
  definition: |
    可选告警包：穿透"勿扰"、持续视觉通知+声音提示、告警确认（alert acknowledgment）；设备 PC 或手机。
    面向告警/安全通知场景的可选服务计划。书中无进一步细节。
  alias_or_related: 无
  tags: [subscription, alerting]

- id: g43
  term: CRM Connect
  category: subscription
  source_pages: p67
  source_quote: |
    "CRM Connect — Enrich your CRM with real-time communications — Make Web or telephone calls directly
    from your CRM system and keep a history of all telephone exchanges in your CRM. — PC only" (p67)
  definition: |
    CRM 集成订阅：从 CRM 系统直接网页/电话外呼，并把全部通话历史留存 CRM；设备 PC only。书中无连接器细节
    （勿与 Teams 集成混淆——Teams 集成不靠本订阅）。
  alias_or_related: 无
  tags: [subscription, crm]

# ── 四、产品/组件名 (product) ──

- id: g44
  term: Myriad M3 / M5 / M7 (+ EM200)
  category: product
  source_pages: p8-9, p106-108
  source_quote: |
    "Myriad M7 | Myriad M5 | Myriad M3 ... Screen Colour screen 3,5'' | 2,8'' | 1,6'' ... Extension module
    EM200 For M3-M5-M7 desktop phones Colour screen, Up to 10 pages of 20 LED keys" (p107)
  definition: |
    Hub 主力话机三档（zero-touch、与用户状态同步 DND/呼转/全局目录搜索，p106）：M7 旗舰（3.5" 彩屏、超宽频
    仅免提、BT4.1 耳机、Audio Hub、EM200 扩展最多 10 页×20 LED 键）；M5（2.8"）；M3（1.6"）。M 系 PoE
    class 2、USB-A/USB-C 端口、千兆 PC 口。概览页还列 M8/M7s Pro/M7s/M5s/M3s 与 ALE-300/400/500 谱系名
    （p9），参数表仅覆盖 M3/M5/M7。
  alias_or_related: 参数口径见 p30（principle）；外链说明不保证适用 Hub（n17）
  tags: [product, devices, myriad]

- id: g45
  term: ALE-2 (and ALE-300/400/500)
  category: product
  source_pages: p9, p107
  source_quote: |
    "ALE-2 — Entry level / Basic uses ... Port (headset, extension, wifi…) ... RJ9 ... Power supply ...
    PoE class 1" (p107)
  definition: |
    入门级话机（Entry level/Basic uses）：RJ9 端口、PoE class 1；亦列于 zero-touch 可用 SIP ALE 话机
    （p106）。谱系同族的 ALE-300/400/500 见订阅页话机区（p9）。
  alias_or_related: 对照 g44 Myriad；DECT 互补见 g46
  tags: [product, devices, entry-level]

- id: g46
  term: DECT handsets 8214 / 8262
  category: product
  source_pages: p9, p107, p148-152, p163-164
  source_quote: |
    "The 8328 base station and 8214 handset set is an ideal internal mobility solution ... The 8262
    handset is recommended for demanding environment or lowe worker protection." (p149)
    "Register a new '8214 DECT Handset' or '8262 DECT Handset' with its IPEI number" (p152)
  definition: |
    两型 DECT 手持机：8214 办公/门店/车间移动（DECT 仅欧洲与亚洲供货，p9/p107）；8262（PTI）恶劣环境/
    独行工人保护。zero-touch 注册按 IPEI（g59）、关联到尚无物理终端的用户、挂到 8328/8368 基站。
  alias_or_related: "lowe" 为原文笔误照录；注册流程见 c04
  tags: [product, dect, mobility]

- id: g47
  term: 8328 SIP-DECT base station
  category: product
  source_pages: p148-149, p160-162
  source_quote: |
    "8328 SIP-DECT Single base station which permit a coverage with one or two base stations only. ...
    1 or 2 base stations/site • Up to 20 DECT handsets ... Range 50 to 300m ... Up to 20 handsets and 10
    simultaneous calls." (p148-149)
  definition: |
    单/双站 DECT 基站（含带脚座版）：小安装方案（办公室/门店/车间）1-2 站/点、最多 20 手持机、10 路并发；
    尺寸 95×93×24mm、以太网 10/100 PoE。Cell mode 建站时选 Mono 或 Dual；可经 CAT-iq（g60）对接本地告警
    服务器。
  alias_or_related: 对照 g48 8368；容量见 p35（principle）
  tags: [product, dect, base-station]

- id: g48
  term: 8368 SIP-DECT base station
  category: product
  source_pages: p148-151
  source_quote: |
    "8368 SIP-DECT Multi cell base station which permit a large coverage with one to 254 base stations ...
    Up to 254 base stations • Up to 40 handsets/base stations ... Up to 1000 handsets (40 per base
    station) • Up to 10 simultaneous calls per base station" (p148, p150)
  definition: |
    多站 DECT 基站：大安装方案最多 254 站、每站 40 手持机、全系统 1000 手持机、每站 10 路并发；室内型
    144×140×35mm 壁挂内置天线、室外型 365×210×65mm IP55 外置天线（均 10/100 PoE）。建站须录主站 IP
    （副站靠它通信）；8368 下副站上限 253 台（p151）；覆盖 50-300m、站间无缝切换。
  alias_or_related: 对照 g47；多站命名建议见 c04 步骤 2
  tags: [product, dect, base-station]

- id: g49
  term: OmniAccess Stellar (WiFi mobility)
  category: product
  source_pages: p153
  source_quote: |
    "ON-SITE MOBILITY - WIFI • Indoor/outdoor coverage • Shared voice/data infrastructure • Supports voice
    calls over Wifi ... Constantly evolving technology (Wifi 7) ... OmniAccess Stellar AP1301 WIFI access
    point" (p153)
  definition: |
    ALE 的 WiFi 现场移动方案（与 DECT 并列的移动路线）：语音/数据共用基础设施、标准与加固手机（含独行
    工人/扫码等业务功能）、全部 Rainbow 服务经 iOS/Android 应用可用；技术演进至 WiFi 7。示例 AP 为
    OmniAccess Stellar AP1301。书中仅一页概览，无部署细节。
  alias_or_related: 对照 DECT 两档（g47/g48）；DECT 方案介绍文档 TBE127（g68）
  tags: [product, wifi, mobility]

- id: g50
  term: MicroSIP
  category: product
  source_pages: p13, p20-22, p32-33
  source_quote: |
    "2 preconfigured MicroSIP softphones will be provided by the trainer (.zip file) • Unzip it • Launch
    .bat file: « Start public users.bat » • There is no installation" (p20)
  definition: |
    培训专用的第三方 SIP 软话机（公网用户模拟器）：讲师发 zip（免安装）、"Start public users.bat" 启动、
    按 POD 选账号；每 POD 两个（User A/B），公网号按 332982900P1/331409500P1/336050400P1/442056700P1 规则
    （p22），可测本地/国内/移动/国际闭锁。RLAB 客户机桌面预装，NAS 也提供。训后必须删除（n56）。
  alias_or_related: 实验口径；模拟器限制见 n56；纯教学基础设施
  tags: [product, lab, softphone]

- id: g51
  term: Rainbow Exporter
  category: product
  source_pages: p231
  source_quote: |
    "it is possible on request to implement 'Rainbow Exporter', which copies all recordings daily to
    Google Drive, or to a customer's own SFTP storage server, in addition to traditional Rainbow licenses
    (pricing on request)." (p231)
  definition: |
    录音归档选件：按日把全部录音拷贝到 Google Drive 或客户自有 SFTP 存储，服务超过平台 2 个月保留期的法定
    归档需求；在常规 Rainbow 许可之外另行计费（pricing on request）。
  alias_or_related: 录音保留与访问口径见 n42
  tags: [product, recording, archive]

- id: g52
  term: LDAP connector (AD synchronization)
  category: product
  source_pages: p167, p178-179
  source_quote: |
    "AD SYNCHRONIZATION (LDAP CONNECTOR) This connector can be installed freely at any customer's premises
    who wishes to have it. ... This connector offers a choice of three functions: 1 Automatic
    synchronization of Rainbow users ... 2 Automatic synchronization of AD contacts in the Rainbow
    Business Directory ... 3 Synchronize calendar presence with Exchange Server." (p179)
  definition: |
    装在客户侧 Windows server 的目录同步连接器（免费安装），三功能可自选：①Rainbow 用户自动同步（AD→
    Rainbow 单向、按所选周期建/改/删、仅同步持付费许可的用户）；②AD 联系人自动进企业目录；③与 Exchange
    Server 同步日历在场（等价于 161 版前 Exchange online/Office 365 功能，见 n55）。架构：LAN 内
    Windows server 进程 ↔ LDAP ↔ AD/Exchange。
  alias_or_related: 用户通道见 g 系成员五通道（f14）；版本语义见 n55
  tags: [product, ldap, directory, sync]

- id: g53
  term: MyPortal
  category: product
  source_pages: p342-343
  source_quote: |
    "Connect to MyPortal • Support > Service Request • Click on Create SR: • SR category= Rainbow • SR
    type = product support ... • Product Category = Rainbow Hub" (p342-343)
  definition: |
    ALE 客户服务门户（本版教材仅用于开 Service Request）：Support > Service Request > Create SR，两页
    表单（第一页类别/类型/严重级/主题/邮箱描述；第二页终端客户公司名、Product Category=Rainbow Hub、
    版本、详情、子类、Rainbow SIP trunk、发现来源、客户内部参考、联系人=Global welcome center）。ESR
    仅认证伙伴受理（n54）。
  alias_or_related: 对照混合云教材（MyPortal 兼作网关软件下载与 cookbook 入口——Hub 教材无此用途）
  tags: [product, portal, support]

- id: g54
  term: Emily BOT / Global Welcome Center
  category: product
  source_pages: p341
  source_quote: |
    "Support entry points can be: • Mail: support@openrainbow.com • Emily BOT • Global Welcome Center is
    the main point of contact for all ALE International Partners. • ALE.WelcomeCenter@al-enterprise.com •
    Or phone call" (p341)
  definition: |
    Rainbow 支持入口（与邮件/电话并列）：Emily BOT 为支持机器人；Global Welcome Center（ALE.WelcomeCenter@
    al-enterprise.com）是所有 ALE 国际伙伴的主 contact 点，也是 SR 表单里的联系人选项。无论哪个入口，
    ESR 只为认证 Rainbow Hub 的伙伴创建。
  alias_or_related: support@openrainbow.com、电话入口并入本条；认证前提见 n54
  tags: [product, support, bot]

# ── 五、协议与技术名 (protocol) ──

- id: g55
  term: SIP trunk
  category: protocol
  source_pages: p78, p80, p88, p100-101, p343
  source_quote: |
    "One CloudPBX = one and only one external SIP trunk (SIP provider). ... Find the list of certified
    providers on the Rainbow Help Center website." (p78)
    "External trunk Select a trunk group for public calls ... Only one trunk group can be associated to
    the Cloud PBX." (p101)
  definition: |
    Cloud PBX 到公共 SIP 运营商的中继：外部呼叫经它进出公网；硬约束一 PBX 一条 trunk；trunk 组在声明时
    选择（实验口径：ALE Training Carrier）；话务与计费由 BP/运营商承载（p88）；认证运营商清单在
    help.openrainbow.com。紧急号码表按国家+trunk 组自动配置（p227）。
  alias_or_related: 商务模式 bundled/separated 见 p26（principle）；SR 表单子类字段（p343）
  tags: [protocol, trunk, sip]

- id: g56
  term: TLS / SRTP
  category: protocol
  source_pages: p118, p136
  source_quote: |
    "Mandatory security • TLS 1.2 minimum for signaling • SRTP enabled for the media stream • Encryption
    can be disabled if the device does not support it properly" (p118)
    "TCP 5061 SIP over TLS ... UDP 30000-44999 SRTP media" (p136)
  definition: |
    终端-云加密基线：信令 TLS 1.2 起步（SIP over TLS 走 TCP 5061）、媒体 SRTP（UDP 30000-44999）；Generic
    SIP 场景设备不支持时可关加密（ALE 原生终端按端口表强制）。两个缩写书中均未展开全称。
  alias_or_related: 端口表见 p32（principle）；Generic SIP 安全基线见 p36（principle）
  tags: [protocol, security]

- id: g57
  term: OPUS / VP8 / G711 (codecs)
  category: protocol
  source_pages: p90, p118
  source_quote: |
    "Audio & video media flow of the Rainbow client — Opus for audio / VP8 for video — 80 kbps / 1,5 Mbps
    (720p at 30 fps) ... Audio flow of the SIP device — G711 — 64 kbps" (p90)
    "Audio • G711 codec recommended" (p118)
  definition: |
    编解码口径：Rainbow 客户端音频 Opus（80 kbps 单向）、视频 VP8（1.5 Mbps，720p/30fps）；SIP 设备音频
    G711（64 kbps），Generic SIP 推荐 G711。前提说明：PSTN 呼叫中 Rainbow 客户端支持 OPUS（p90）。带宽
    核算位置在客户侧到 SIP trunk 段。
  alias_or_related: 带宽表见 p27（principle）
  tags: [protocol, codecs, bandwidth]

- id: g58
  term: DTMF
  category: protocol
  source_pages: p251, p266, p323
  source_quote: |
    "Automated welcome of your callers and offer them DTMF choices to route them within your organization"
    (p251)
    "Each IVR has a maximum of 3 levels, each allowing a DTMF selection from 0 to 9." (p266)
  definition: |
    双音多频按键选择：IVR/自动话务员的核心交互——每级菜单 0-9（另支持 *、#，p269）选择路由；分析页的
    "取消呼叫"定义为主叫未输入任何 DTMF 选择（p323）。缩写未展开。
  alias_or_related: 见 g25 AA
  tags: [protocol, dtmf, ivr]

- id: g59
  term: IPEI
  category: protocol
  source_pages: p152, p163
  source_quote: |
    "Register a new '8214 DECT Handset' or '8262 DECT Handset' with its IPEI number" (p152)
    "Select - The type of device - Enter its IPEI - A description" (p163)
  definition: |
    DECT 手持机的注册标识（zero-touch 流程中与设备类型一起录入；对照物理话机/基站用 MAC 地址注册）。
    缩写未在书中展开全称，不采信外部补全。
  alias_or_related: 对照 g08 Zero Touch 的 MAC 注册线；实验见 c04
  tags: [protocol, dect, identifier]

- id: g60
  term: CAT-iq
  category: protocol
  source_pages: p149-150
  source_quote: |
    "The SIP-DECT 8328 base station can communicate locally with an alarm server (CAT-iq protocol) :
    alarm escalation from a terminal to the server, sending of an alarm message from the server to the
    terminals. Validated servers: F24, Newvoice (+ in progress: Tamat)" (p149)
  definition: |
    SIP-DECT 基站与本地告警服务器间的本地通信协议（8328/8368 均支持）：终端向服务器上报告警升级、服务器向
    终端下发告警消息。已验证告警服务器：F24、Newvoice（Tamat 验证中）。缩写未展开。
  alias_or_related: 见 g47/g48
  tags: [protocol, dect, alarm]

- id: g61
  term: PSTN
  category: protocol
  source_pages: p40, p67, p88, p318
  source_quote: |
    "PSTN service is not ordered nor managed by ALE Rainbow team" (p88)
  definition: |
    公共电话网：Hub 的公网话务经 Cloud PBX 的 SIP trunk 由 BP/运营商接入 PSTN；PSTN 服务的订购与管理不在
    ALE Rainbow 团队范围（p88）；公网话费计费同样归 BP（p318）。PSTN conference（g40 Dial-In Pack）的
    计费对象。缩写未展开。
  alias_or_related: 商务边界见 n14
  tags: [protocol, pstn, network]

- id: g62
  term: PSAP
  full_name: Public-Safety Answering Point（书中展开，p229）
  category: protocol
  source_pages: p229
  source_quote: |
    "Identification of the relevant Public-Safety Answering Point (PSAP) is under the responsibility of
    the SIP provider. • The SIP Provider must therefore route emergency calls to the right PSAP by
    fetching location info from his own database." (p229)
  definition: |
    公共安全应答点（紧急呼叫接警中心）：紧急呼叫定位链路的终点——SIP 运营商按自己数据库里的 DID 位置信息
    把呼叫路由到正确 PSAP；该判定责任在运营商，Rainbow 不管 DID 定位。
  alias_or_related: 责任链见 n41；紧急组见 g20
  tags: [protocol, emergency, psap]

# ── 六、网站与资源名 (resource) ──

- id: g63
  term: web.openrainbow.com / openrainbow.com
  category: resource
  source_pages: p4, p10, p13, p72, p288, p308
  source_quote: |
    "The management of Rainbow Hub companies is done via: • web.openrainbow.com" (p13)
    "Access to web.openrainbow.com website and logon with the 'BP administrator' account" (p72)
  definition: |
    Rainbow Hub 管理与使用入口：BP/客户管理员全流程（建司、Cloud PBX、成员、组、欢迎服务、多站点）与
    成员客户端（含话务台入口，p288）都在 web.openrainbow.com；官网 openrainbow.com（p10 Resources）。
    平台发信（邀请/enrollment）来自 noreply@openrainbow（p168）且可能被判 SPAM（n32）。
  alias_or_related: help/status/pilot/rdd 为同域不同子域（g64-g67）
  tags: [resource, website, portal]

- id: g64
  term: help.openrainbow.com
  category: resource
  source_pages: p8, p37, p67, p78, p331
  source_quote: |
    "Find all the features in the Features List available on the Rainbow Help Center website at
    help.openrainbow.com." (p8)
    "Find all the network requirements on the Rainbow support site • Use the following URL ...
    https://help.openrainbow.com/hc/en-us/articles/23942019777170-Check-Rainbow-Network-Requirements"
    (p37)
  definition: |
    Rainbow 支持站点（Help Center）：本书反复引用的文档源——Features List（p8/p67）、Network Requirements
    文章（固定 URL，p37）、认证运营商清单（p78）、Generic SIP 互接文章（p117）、Help Desk Guide（p331）。
    生产化的第一查询入口。
  alias_or_related: Features List = 订阅与功能的权威对照表
  tags: [resource, website, support]

- id: g65
  term: status.openrainbow.com
  category: resource
  source_pages: p338
  source_quote: |
    "A dedicated 'Operations' team constantly monitors the smooth running of the Rainbow platform (24/7).
    Nevertheless, in exceptional cases, a malfunction in our Data Centers may occur. In this case, you can
    be informed via the following specific site: ... status.openrainbow.com ... The button « Get updates »
    allows, if you wish, you can subscribe to alerts by different methods." (p338)
  definition: |
    云服务状态页：数据中心故障的官方信息源；"Get updates" 订阅告警、按主题与地理区域过滤（法国建议勾
    WW/EMEA & DE）。配套管理端内的计划维护公告（按地域与 Hybrid/Hub 架构过滤、颜色分级、多为晚间周末，
    p339）。
  alias_or_related: 计划维护公告在管理端（p339），非本站
  tags: [resource, website, status]

- id: g66
  term: pilot.openrainbow.com (Rainbow Pilot)
  category: resource
  source_pages: p43-45, p136
  source_quote: |
    "RAINBOW PILOT allows you to assess your Rainbow connectivity from your location, and the capacity of
    a given location to handle a population of Rainbow users characterized by a flexible mix of usages
    between Collaboration, Conferencing, Hybrid or Hub telephony. • Link: https://pilot.openrainbow.com/
    home" (p43)
  definition: |
    官方连通性与承载评估工具：从客户现场测 Rainbow 连通性、按协作/会议/混合/Hub 话音用法配比评估站点承载；
    设备章要求"用 Pilot 做全套测试判断网络是否正确"（p136）。部分测试分区标注 To come（n02）。
  alias_or_related: 售前勘测工具，配合 Network Requirements 使用
  tags: [resource, tool, presales]

- id: g67
  term: rdd.openrainbow.com
  category: resource
  source_pages: p136
  source_quote: |
    "If the device receives a specific management URL in option 43, 66 or 67, Rainbow Hub's 'zero touch'
    mechanism will be broken, as the DHCP option will take precedence. ... If it is not possible to
    disable them, the link distributed by the DHCP server should be: https://rdd.openrainbow.com" (p136)
  definition: |
    零接触部署的管理 URL：DHCP 服务器无法禁用 option 43/66/67 时，下发的管理地址必须指向本域，才能保住
    zero-touch 机制。全书仅此一处出现。
  alias_or_related: 红线背景见 n21
  tags: [resource, url, zero-touch]

- id: g68
  term: TBE099 / TBE127
  category: resource
  source_pages: p154, p318
  source_quote: |
    "Click here for a presentation of the DECT solution for Rainbow Hub. ... TBE127" (p154)
    "For details refer to the document TBE099_Rainbow Hub - Voice services" (p318)
  definition: |
    两份 ALE 官方文档指针：TBE127=Rainbow Hub DECT 方案介绍（分伙伴/ALE 员工两个链接）；TBE099_Rainbow
    Hub - Voice services=话音服务细节文档（CDR 获取等）。书内只给名与链接，内容在外部。
  alias_or_related: CDR 细节见 g28；DECT 方案见 g47/g48
  tags: [resource, document]

- id: g69
  term: RLAB / POD (training lab)
  category: resource
  source_pages: p12-34, p192
  source_quote: |
    "A POD number is assigned to each trainee • POD: Training Environment Number ... Up to 6 trainees (8
    exceptional cases)" (p13)
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data
    center. 1 POD = 1 participant" (p27)
  definition: |
    培训实验基础设施：每学员一个 POD 号（1-6，特殊 8）对应一家训练公司（Client-PX）与号段；RLAB（Remote
    Lab）为数据中心托管虚机池（1 POD=1 参训者），仅在学员 PC 跑不了 MicroSIP 时使用——Windows 11 客户机
    Client1（192.168.1.10/24、网关 192.168.1.254、DNS 192.168.1.250，实验口径）、NAS 12.0.0.2。培训邮箱
    mail44.lwspanel.com（登录=邮箱、密码 PasswordP*，实验口径）用于完成邀请建户。
  alias_or_related: 账号号段规划见 p29/p53（principle）；模拟器限制见 n56
  tags: [resource, lab, training]

- id: g70
  term: ALE Knowledge Hub (enterprise-education.csod.com)
  category: resource
  source_pages: p347-351
  source_quote: |
    "Connect to ALE Knowledge Hub (https://enterprise-education.csod.com ) with your usual credentials ...
    Find a Course — Browse our catalog available on https://enterprise-education.csod.com/ to find your
    training path and course detail." (p347, p351)
  definition: |
    ALE 培训平台：完成结课评估（My Training → 搜课程参考号 → Evaluate）后下载培训证书；课程目录与学习
    路径入口。培训行政用途，非技术内容。
  alias_or_related: 评估流程 p345-350；反馈邮箱 training-services@al-enterprise.com（p351）
  tags: [resource, training, portal]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列术语（17 行）逐条核对

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| Rainbow Hub | 有明确定义（p5） | g01 |
| Cloud PBX | 有明确定义（p78） | g02 |
| Voice 四档订阅 | 有明确定义（p9/p67 逐一定义） | g36-g39（+扩展档 g40-g43） |
| BP（Reseller） | 有明确定义（p49/p58） | g30 |
| Zero Touch | 有明确定义（p106/p134-137） | g08 |
| RCC | 有明确定义（p112） | g07 |
| Generic SIP | 有明确定义（p116-120） | g09 |
| Hunt group | 有明确定义（p210-215） | g18（+g19 队列） |
| Waiting queue | 有明确定义（p215-216） | g19 |
| Emergency group | 有明确定义（p227-228） | g20（号码表并入） |
| Welcome service | 有明确定义（p251/p258） | g24 |
| Automated attendant (IVR) | 有明确定义（p266） | g25 |
| Personal routines | 有明确定义（p173-174） | g13 |
| Sites | 有明确定义（p301-304） | g26 |
| CDR | 有明确定义（p318） | g28 |
| MOS | 有定义性用法（p319/p328 阈值），未展开全称 | g29（full_name 如实省略） |
| Grace period | 有明确定义（p176） | g17 |

结论：**17 行全部"本书正文有明确定义或定义性用法"，无"仅 passing 提及需排除"项。** 下游建议以本表 70 条为术语基准。

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：Company（g03）、Visibility（g04）、SSO（g05）、TOTP（g06）、Generic SIP 已列、DID/DDI（g10）、Internal numbering plan（g11）、Traffic control/Barring（g12）、Key groups（g14）、Business Directory（g15）、Information Channels（g16）、Manager/Assistant group（g21）、Supervision group（g22）、Attendant console（g23）、Group bubble（g27）
- 角色：DR/IR（g31）、VAD（g32）、EC（g33）、Agent/Administrator（g34）、Manager/Assistant 角色（g35）
- 订阅：Voice Enterprise Dial-In Pack（g40）、Rainbow Room（g41→g41 为 Room，即 g41；Dial-In Pack 为 g40）、Rainbow Alert（g42）、CRM Connect（g43）
- 产品：Myriad M3/M5/M7+EM200（g44）、ALE-2（g45）、DECT 8214/8262（g46）、8328（g47）、8368（g48）、OmniAccess Stellar（g49）、MicroSIP（g50）、Rainbow Exporter（g51）、LDAP connector（g52）、MyPortal（g53）、Emily BOT/Global Welcome Center（g54）
- 协议：SIP trunk（g55）、TLS/SRTP（g56）、OPUS/VP8/G711（g57）、DTMF（g58）、IPEI（g59）、CAT-iq（g60）、PSTN（g61）、PSAP（g62）
- 资源：web.openrainbow.com（g63）、help.openrainbow.com（g64）、status.openrainbow.com（g65）、pilot.openrainbow.com（g66）、rdd.openrainbow.com（g67）、TBE099/TBE127（g68）、RLAB/POD（g69）、ALE Knowledge Hub（g70）

### 3. 仅 passing 提及、未单列条目的词（备查）

bubble（p53/g27 已并入）、DND = Do Not Disturb（p108，并入 g44 话机特性描述）、PoE = Power over Ethernet（p150 已展开，并入 g44/g47/g48）、ATA gateway（p116，并入 g09 例子）、PTI（p149/p150，8262 括注，并入 g46）、SBC/VPN（p7 "No VPN No SBC"，并入 g01 卖点描述）、IVR（g25 词条内，未展开全称）、RCF/RDD 之外的子域、EM20（p107 表格 "EM20 or EM200"，仅 EM200 展开）、pabx（无）、FTR/UTL/WebRTC 网关（本 Hub 教材无这些概念，属于 RAINXTE001EN 语系，勿混入）。

### 4. 提取口径说明

- 所有定义只采信本书正文；MOS/IVR/IPEI/CAT-iq/DTMF/DECT/SRTP/TLS/PSTN/SIP 等缩写书中未给全称的，full_name 一律省略或标"未展开"，不做外部补全（DID/CDR/PSAP/TOTP/SSO/DR/IR/VAD/EC/BP 书内有展开，已标注）。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准，引用均为原文摘录；原文笔误照录并注明（p62 "allow to to"、p107/p149 "lowe"、p144 "the the"、p179 "Unidirectionnel"/"Connecteur"、p192 "PLATEFORM"、p241 "BY DEFAUT"）。
- 同词两义提示：TOTP 既是认证方式（p54）也是设备 debug 一次性口令的机制标注（p142/p335），已在 g06 内说明。
