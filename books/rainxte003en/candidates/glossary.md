# 术语/缩写/产品名候选 — Rainbow OmniPCX Enterprise (RAINXTE003EN Ed12)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 66 条（concept 25 / role 9 / subscription 8 / product 8 / protocol 7 / resource 9，见各分区）。CSTA/OMS/ITSP/NPD/ESR 等缩写书中未给全称，full_name 字段如实省略，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: Rainbow
  category: concept
  source_pages: p20-23
  source_quote: |
    "Rainbow is a Cloud-based collaboration application (UCaaS) offering chat services, audio / video calls,
    screen and file sharing, contact management, phone presence…etc. In a Hybrid cloud approach, Rainbow
    integrates with OXO Connect and OmniPCX Enterprise, as well as third-party PBXs. It is also a CPaaS open
    communication platform with a set of APIs…" (p20)
  definition: |
    ALE 的云协作平台，本书中是"宿主平台"角色：UCaaS（协作/云话音）与 CPaaS（开放 API）双重定位；混合云
    模式下集成 OmniPCX Enterprise（本书主线）/OXO/第三方 PBX。提供公司、订阅、成员账户体系与客户端
    （PC App/Web/移动），PBX 侧保留呼叫控制。
  alias_or_related: web.openrainbow.com 为网页客户端入口（p61）；developers.openrainbow.com 为 CPaaS 门户（p21）
  tags: [concept, platform, ucaas, cpaas]

- id: g02
  term: Company
  category: concept
  source_pages: p38-39
  source_quote: |
    "To ease collaboration between colleagues in the same company, users are gathered within the same
    Company. • Main features are only available to users who are members of a Company, and it is therefore
    a key concept in Rainbow. … A user cannot be part of 2 different companies." (p38)
  definition: |
    Rainbow 的用户组织单元，核心概念：主功能仅对公司成员开放；用户不可同时属于两家公司；建司前先搜索
    查重。分 Reseller/BP 公司与 End Customer 公司两级，EC 公司由 Reseller 创建并必须挂在唯一一个 BP 下。
  alias_or_related: Reseller/BP Company 与 BP 角色（g26）、End-customer Company 与 EC 角色（g32）
  tags: [concept, tenant]

- id: g03
  term: Visibility
  category: concept
  source_pages: p43, p96
  source_quote: |
    "PUBLIC: a user from another company can see and invite members of your company… CLOSED: … ISOLATED: a
    user from another company cannot see the members of your company and cannot invite them… Get into the
    habit of systematically setting the 'closed' mode… This 'isolated' mode is not recommended…" (p43)
  definition: |
    公司对外可见性四级（PUBLIC/PRIVATE/CLOSED/ISOLATED），company settings 可改。作者明确推荐：建司
    默认 CLOSED；不推荐 ISOLATED——代价是无法被外部 bubble 邀请。成员个人另有 Visibility（same as
    company/none/public/private…，p96）。
  alias_or_related: bubble = 书中对 Rainbow 会议/群聊的口语提法，仅 p43 一处，未定义
  tags: [concept, privacy]

- id: g04
  term: SSO
  full_name: Single Sign On（书中以 SSO* 脚注展开）
  category: concept
  source_pages: p44
  source_quote: |
    "you can enable single sign-on (SSO*) with your Azure Active Directory, or with your corporate AD
    (ADFS). … Azure AD - SAML / Azure AD - OIDC / ADFS - SAML … other methods are possible, subject to ALE
    confirmation, when they are based on standard protocols. For example, with SAML V2 : Shibboleth, RSA,
    … and with OIDC : LemonLDAP, OKTA, CAS APEREO, Ping Identity, …" (p44)
  definition: |
    公司级单点登录：支持 Azure AD（SAML 或 OIDC 两种协议）与本地 AD（ADFS-SAML），可全公司启用或仅部分
    用户；前提是管理员持 Enterprise 订阅。Teams 集成实验示范用 Microsoft 凭据 SSO 登录 Rainbow（p304），
    且注明 SSO 非连接器必需。
  alias_or_related: SAML、OIDC、ADFS（协议/网关，并入本条）；与 g05 TOTP 并列
  tags: [concept, auth]

- id: g05
  term: TOTP
  full_name: Time-based One Time Password（书中直接展开）
  category: concept
  source_pages: p44
  source_quote: |
    "Authentication with TOTP (Time-based One Time Password) Users need a third-party authentication
    application (Google Authenticator, Microsoft Authenticator, Authy). This method applies to all types of
    users but is particularly recommended for the administrators." (p44)
  definition: |
    Rainbow 原生认证的第二种模式（另一种是 12 位复杂密码传统认证）：需第三方验证器 App，特别推荐给
    管理员。MFATOTP 设置参考文章见 p44 引用链接。
  alias_or_related: 与 g04 SSO 并列；书中称 "Rainbow's native authentication"
  tags: [concept, auth, mfa]

- id: g06
  term: RCC
  full_name: Remote Call Control（书中展开）
  category: concept
  source_pages: p109-110, p129
  source_quote: |
    "Rainbow Essential license • Allows only to control your physical device via the Rainbow application
    (RCC mode = Remote Call Control) • Call routing is not possible • Calls are received/made via the
    physical extension" (p109)
    "Possible actions • RCC of deskphone for incoming and outgoing calls: • Use of OXE devices for voice" (p110)
  definition: |
    OXE 分机关联 Rainbow 账户后（无论有无网关）的基本模式：Rainbow 客户端"监督"话机（接听/挂断/转移），
    音频走 OXE 设备。Essential 订阅只有此能力且不能改路由；配 REX/tandem 后（Business/Enterprise）解锁
    外部路由。验证法见 c05 五项测试。
  alias_or_related: DECT 特例下 Virtual UA 不可 RCC（g14 关联 p139）
  tags: [concept, telephony, mode]

- id: g07
  term: Remote Extension
  full_name: Remote Extension（缩写 REX，书中两处并用）
  category: concept
  source_pages: p111-113, p123
  source_quote: |
    "A Remote Extension (REX) is a special type of device that allows OXE to reroute calls to an external
    resource … OXE takes this technical resource during the establishment of the call in a pool of
    equipment dedicated to this use … The Ghost Z resource is released at the end of the conversation." (p111)
    "Set Type Remote extension … It is interesting to use a numbering plan like :prefix<main set's QMCDU>.
    E.g. 21<QMCDU>" (p123)
  definition: |
    OXE 特殊终端设备类型：让 OXE 把呼叫转往 REX 中定义的外部号码。REX 工位多用途（Rainbow、OT、Remote
    Agent…），Rainbow 场景下它是"呼叫路由载体"——Rainbow agent 按用户路由选择自动改写 REX 内容；编号
    建议用 21<主号 QMCDU> 形成子计划。
  alias_or_related: 与 g08 Ghost Z 配对使用；OXE 网络的其他 REX 用途（OT/Remote Agent）书中仅点名
  tags: [concept, telephony, rex, routing]

- id: g08
  term: Ghost Z
  category: concept
  source_pages: p111, p122
  source_quote: |
    "To work, each REX needs an internal technical equipment called Ghost Z (dedicated to the 'Remote
    Extension' function) • The Ghost Z devices pool is the maximum number of concurrent calls being made
    • The Ghost Z resource is released at the end of the conversation" (p111)
    "A ghost device is required per simultaneous call to a REX. … Ghost Z Checked • Ghost Z Feature Remote
    extension" (p122)
  definition: |
    REX 功能专用的 OXE 内部技术资源：每路 REX 并发呼叫占一个 Ghost Z，通话结束释放；池大小=REX 并发
    上限。创建参数：目录号建议用字母开头（如 DB1000）、Set Type=Analog、机架/板卡/设备地址 255、
    Facilities 勾 Ghost Z + Feature=Remote extension。
  alias_or_related: 数量规划与 g61 TBE067 sizing 联动（推算 OXE 压缩器）
  tags: [concept, telephony, resource]

- id: g09
  term: Tandem
  category: concept
  source_pages: p112-113, p125
  source_quote: |
    "OmniPCX Enterprise Configuration • Remote extensions • Ghost Z • Remote extension per user • Tandem
    management • Main: Deskphone • Secondary: REX … Main Secondary REX/VT" (p113)
    "Tandem Directory Number Enter the directory number of the secondary set (Rex) • Main set in the
    tandem Checked … Configuration is done on one device: the main one." (p125)
  definition: |
    OXE 主/副站成对结构：主站=Deskphone、副站=REX；两端必须 multi-line（≥2 线）；配置只在主站做、自动
    同步副站。与"nomadic"模式同构（路由到手机/家庭/其他号）。书内强调 Call Routing is not a Forwarding。
  alias_or_related: 4059EE 关联话机禁 multi-line（反例 n20）；DECT 场景用 Virtual UA 替代直接 tandem（n14）
  tags: [concept, telephony, tandem]

- id: g10
  term: Multi-line
  category: concept
  source_pages: p124
  source_quote: |
    "Configure at least 2 multi-lines on each Barkley's extensions (main set and rex): • 31000 • 2131000 …
    Multi-lines are required on extensions part of a tandem." (p124)
  definition: |
    OXE 话机/软终端的多线配置（Users/Prog. Keys 页签：空闲键、功能 Multi-line、目录号=本机号、助记名
    如 L1）：tandem 成员分机的强制前提；同时决定话务台挂起呼叫容量（OXE REX 最多 10 路）。
  alias_or_related: mono QMCDU 术语在菜单中出现（p124 "manage multi-lines (mono QMCDU)"，未定义）
  tags: [concept, telephony, oxe]

- id: g11
  term: Rainbow number
  category: concept
  source_pages: p91, p142
  source_quote: |
    "Once the association done, a new field is displayed, the Rainbow number. … It will be automatically
    configured in Remote Extension number by the Rainbow agent (e.g. BBB10070254106463346) when the user
    selects 'computer' as routing from his Rainbow client (PC or smartphone)." (p91)
  definition: |
    分机关联后 Rainbow 界面出现的 17 位技术编号（BBB 开头 + 数字）：用户选 "computer" 路由时由 Rainbow
    agent 自动写入 OXE 侧 REX 的 Remote Extension number，经 BBB ARS 前缀路由进 WebRTC 网关。排障用
    remotesets 查看（ExtNbr 字段）。
  alias_or_related: 前缀 BBB 见 g17；示例 BBB10070254106463346 为书中示例值
  tags: [concept, routing, webrtc-gateway]

- id: g12
  term: WebRTC Gateway
  category: concept
  source_pages: p133-136
  source_quote: |
    "A software component located in a customer's premises that runs on a virtual machine. Use of the
    WebRTC Gateway requires a BUSINESS or ENTERPRISE subscription for a member … Enabling internal and
    external communications between Rainbow clients, extensions and resources of the PBX (trunk groups,
    voicemail, public numbers, etc.)" (p133)
  definition: |
    全书核心组件：客户 premises 的 Debian VM（OVF 由 ALE 交付），打通 Rainbow 客户端与 OXE 分机/资源
    （trunk group、话务、留言、公号）的语音互通，提供 one-number 多终端体验；媒体流 Rainbow 客户端
    —WebRTC→网关—SIP/RTP→OXE，云间加密。呼叫控制始终在 PBX。版本前提 OXE ≥12.1 MD4/12.2。
  alias_or_related: 池化形态见 g13；部署配置见 case c07；OXE 配套见 case c09
  tags: [concept, gateway, telephony, core]

- id: g13
  term: Shared and scalable WebRTC Gateway (pool)
  category: concept
  source_pages: p146-150
  source_quote: |
    "Allows multiple OXEs to share the same WebRTC gateway pool • Increase capacity for simultaneous calls
    • Resilience in the event of a WebRTC failure, guaranteeing applicative High Availability capabilities
    • Geographical high availability is supported" (p147)
  definition: |
    规模化网关架构：多 OXE 共享网关池（推荐按 OXE 集群推进），靠 ARS 溢出分流——网关满载回 SIP 406 Not
    Acceptable 触发下一条路由；每 OXE 每网关一条 SIP trunk/外部 SIP 网关，各节点 ARS 管理需相似；亦
    支持 OXE 网络（多节点）池化。每 OXE 网关复制仅超高流量（书中示例 ≥5000 用户/OXE）才划算。
  alias_or_related: 溢出规则见 principle p19；容量见 g61 与 principle p20
  tags: [concept, gateway, pool, ha]

- id: g14
  term: Virtual UA
  category: concept
  source_pages: p139
  source_quote: |
    "It is necessary to create a Virtual UA type device which will be set in multi-devices configuration
    with the DECT and the REX • The Virtual UA becomes the main device of the tandem and usually requires
    the DECT device to be recreated … It is not possible to control the Virtual UA device in RCC." (p139)
  definition: |
    DECT-only 用户接入 Rainbow 路由的替代设备类型：因 DECT 不能与 REX 直接 tandem（OXE 管理限制），建
    Virtual UA 与 DECT+REX 做 multi-devices，Virtual UA 任 tandem 主设备（通常需重建 DECT）；代价是
    Virtual UA 不能被 RCC 控制。
  alias_or_related: 书中未展开 UA 全称
  tags: [concept, dect, rex]

- id: g15
  term: Integrated Rainbow Agent
  category: concept
  source_pages: p67-68, p87
  source_quote: |
    "Allows connection of the OXE to Rainbow via • A PBX ID • An Activation Code … Rainbow Agent — OXE"
    (p68)
    "4503=rainbowagent: WebSocket (rainbowagent<->Rainbow) in service • 4505=XMPP link • 4509=CSTA link
    (CSTA server<->Rainbow) • 4507=Config link (PBX config<->Rainbow) • 4511=API_MGT link" (p87)
  definition: |
    OXE 内置云连接代理：用 PBXID+激活码启用（webadmin/mgr 的 Rainbow 菜单），承担与 Rainbow 云的五条
    链路（WebSocket/XMPP/CSTA/Config/API_MGT）；维护四抓手：incvisu 看链路、dhs3_init -R RAINBOWAGENT
    重启、checkCloudConfig.sh -rainbow 核查、/var/log/rainbowagent.log 日志。
  alias_or_related: OXO 版对应物为 OMC/Cloud/Rainbow 页面（RAINXTE001），OXE 用 webadmin
  tags: [concept, rainbow-agent, csta, connection]

- id: g16
  term: Attendant console (Rainbow)
  category: concept
  source_pages: p225-232
  source_quote: |
    "Attendant console allows to • Supervise members' status - Presence and call control • Call queue
    management - Manage up to 10 calls for OXE - And up to 8 calls for OXO Connect … An Attendant
    subscription is required for each member using this feature • Available on the Rainbow Web and
    Desktop applications • Attendant console not available on mobile." (p227)
  definition: |
    Rainbow 内嵌话务台（Web/Desktop）：监督组页签 + BLF 监督区 + 呼叫队列（OXE 10/OXO 8）+ 呼叫控制；
    可拦截被监督用户来话、强制/取消呼转；三种显示格式 Normal/Small/Condensed；仅 PC 端；话务员须有电话
    线与 VoIP 软终端能力；所有呼叫由 PBX 处理。
  alias_or_related: 与 4059EE（g45）是两套话务台；订阅见 g38
  tags: [concept, attendant, console]

- id: g17
  term: ARS prefix BBB
  category: concept
  source_pages: p137, p142, p184
  source_quote: |
    "Specific ARS prefix « BBB » for WebRTC Gateway: • Use of SIP trunk group to reach the WebRTC Gateway" (p142)
    "Manage the ARS prefix 'BBB' which will be used in the number automatically configured by Rainbow agent
    in the REX when 'computer' will be selected by the user for routing." (p184)
  definition: |
    WebRTC 网关专用 ARS 前缀：computer 路由时 Rainbow agent 写入 REX 的号码以 BBB 开头（17 位），经
    BBB 前缀→判别器→ARS route list→SIP trunk group 进网关。标准外部前缀（ARS…）走公共 trunk group——
    两条路由面勿混。菜单路径中 ARS 对应 Automatic Route Selection。
  alias_or_related: 判别器五元组见 principle p17；回调翻译表把 DEF 变换为 BBB（p187）
  tags: [concept, ars, routing, webrtc-gateway]

- id: g18
  term: Callback (translation)
  category: concept
  source_pages: p186-188
  source_quote: |
    "Realize the management providing PBX devices to perform callback using their call-log to Rainbow
    extensions. … Set Callback On Calling Device Yes … Digits to Add BBB" (p186-187)
  definition: |
    让 PBX 话机用通话记录回拨 Rainbow 分机的机制：CSTA 开关 + 外部回调翻译表（Basic Number=DEF、删 0
    位、追加 BBB）+ 专用实体（避免与存量回调翻译表互扰）+ 把网关专用 trunk group 挂到该实体。
  alias_or_related: 与 g17 BBB 前缀配套
  tags: [concept, callback, csta]

- id: g19
  term: Busy Lamp Field
  full_name: Busy Lamp Field（缩写 BLF，书中并用）
  category: concept
  source_pages: p199, p221-222
  source_quote: |
    "The 'Enable Busy Lamp Field' box must be checked in the 'General Settings' of the application … BLF
    Supervision of users" (p199)
    "Right click in the BLF pane. Then select 'Add item' … Select User … enter, the user's name and the
    extension number" (p222)
  definition: |
    4059EE（及 Rainbow 话务台）的用户监督面板：启用后在面板加用户即可看其状态；同时呈现 Rainbow 在场
    与电话状态两列（两者可不同，见反例 n21）。
  alias_or_related: Rainbow Attendant Console 的 BLF area（p228）
  tags: [concept, attendant, blf]

- id: g20
  term: Supervision group
  category: concept
  source_pages: p226, p230-231
  source_quote: |
    "In order to supervise the members of a company, users with the attendant subscription, and the
    supervised members must belong to a supervision group … Maximum number of supervision groups for a
    supervisor / Maximum number of users in a group (supervisors + supervised): 5 / 30" (p230)
  definition: |
    Rainbow 侧监督组织：监督员（需 Attendant 订阅）+被监督成员同组；监督员 ≤5 组、每组 ≤30 人；组内
    可拦截来话、强制/取消呼转；每页签一组、红点提示不可见组的来话、另有收藏页签。与 OXE 的 attendant
    group / Call Distribution Table 是两回事。
  alias_or_related: 互助变体见 g21
  tags: [concept, supervision]

- id: g21
  term: Mutual aid supervision group
  category: concept
  source_pages: p233-236
  source_quote: |
    "You can supervise two types of group. • Groups that are permanently affiliated to you • Groups that
    you can join on an ad hoc basis in one click … You can also temporarily integrate or exclude a
    supervised user. … Works only for PBX calls, not for Rainbow softphone calls" (p234)
  definition: |
    互助监督组：普通监督组之外的动态形态——一键 Join/Leave、监督员可临时纳入/排除被监督用户（补救忘
    记进组的用户）、同时最多监督 4 路、代接仅限 PBX 电话呼叫、可锁定最后一名成员；建法与普通组相同仅
    Type 不同，创建时定义双方 In/Out 权限。
  alias_or_related: 应用视图区分 Supervisor app 与 Member app（p235）
  tags: [concept, supervision, mutual-aid]

- id: g22
  term: Business Directory
  category: concept
  source_pages: p51
  source_quote: |
    "In addition to a Microsoft Azure Active Directory, you can create a 'Business Directory' containing
    the contacts of external companies or organizations that are useful to all your users, along with their
    phone numbers. • The quality of reception will be improved thanks to the caller identification" (p51)
  definition: |
    企业目录：Azure AD 之外的外部联系人库（含号码），改善来话主叫识别；管理权默认客户管理员、可委托给
    非管理员用户；手工创建或 CSV 批量导入（含样本文件与导入报告）。
  alias_or_related: 与 g26 Information Channel 同属公司管理面
  tags: [concept, directory]

- id: g23
  term: Information Channel
  category: concept
  source_pages: p52
  source_quote: |
    "Similar to news feeds, they allow to to distribute information to a range of users. … Only users with
    an 'Enterprise' service level can create Information Channels. … Members will not be able to
    unsubscribe." (p52)
  definition: |
    信息频道（新闻推送）：创建者需 Enterprise 级；可对选中成员或全员强制订阅，且成员端不可退订。
  alias_or_related: 强制订订边界见反例 n09
  tags: [concept, channel]

- id: g24
  term: Grace period
  category: concept
  source_pages: p97, p103
  source_quote: |
    "his or her status becomes 'Suspended' for a period of 10 days (called the 'grace period')" (p103)
  definition: |
    成员删除后的 10 天宽限期：期间可恢复（误删）或等自动永久删除；期内同邮箱不能重建；恢复后订阅清空
    降 Essential、需重配许可与话机线。
  alias_or_related: 见 principle p08 与反例 n05
  tags: [concept, members, lifecycle]

- id: g25
  term: Rainbow Hub
  category: concept
  source_pages: p27, p31, p60, p250
  source_quote: |
    "A summary of port/protocol requirements for: Rainbow collaboration • Rainbow hybrid telephony •
    Rainbow Hub" (p27)
    "How to ✓ Declare a new members on Rainbow and assign their extension number"（How-To 页眉："Rainbow
    Hub — Rainbow accounts configuration and use"）(p60)
  definition: |
    Rainbow 的另一种部署/架构形态（与 Hybrid 并列），在网络要求文档、维护通知（按架构过滤）与 How-To
    页眉中出现；本书未展开其定义，端口与架构细节在 Network Requirements PDF。
  alias_or_related: Hybrid（本书主线形态）；Hub 架构细节属书外
  tags: [concept, architecture]

# ── 二、角色 (role) ──

- id: g26
  term: BP
  full_name: ALE Business Partner
  category: role
  source_pages: p39
  source_quote: |
    "ALE Business Partner (BP) … Reseller Companies have special rights • End customer companies are
    created by a Reseller" (p38-39)
  definition: |
    ALE 业务伙伴（经销商公司）：独享"申报与创建 PBX、开通付费订阅"两项权限；EC 公司必须挂靠且仅挂靠
    一个 BP。
  alias_or_related: BP 管理员见 g27
  tags: [role, reseller]

- id: g27
  term: BP administrator
  category: role
  source_pages: p48, p161
  source_quote: |
    "RESPELLER/BP ADMINISTRATORS: Has a view on the customers companies … Create PBXs & activate WebRTC
    gateways … Assign subscriptions to end-customer companies" (p48)
    "In Rainbow Administration, the WebRTC gateway option in PBX settings must be activated by the BP
    administrator." (p161)
  definition: |
    BP 公司的管理员账户：管自家与客户公司、给 EC 分订阅、建 PBX 并激活 WebRTC 网关、网关远程升级的
    操作者；实验中由讲师扮演。
  alias_or_related: 与 g28 客户管理员对照
  tags: [role, administrator]

- id: g28
  term: Customer administrator
  category: role
  source_pages: p49-50
  source_quote: |
    "END-CUSTOMER ADMINISTRATORS: Manages its own company … Manage user accounts … Assign subscriptions to
    users' accounts View related PBXs … Associate users phones with their Rainbow accounts" (p49)
    "The 'Roles' tab is used to assign administrative rights to the client company. It is possible to have
    several administrators to manage the company." (p50)
  definition: |
    最终客户公司管理员：管自家用户账户、公司信息、订阅分配、查看关联 PBX、把用户话机关联 Rainbow 账户、
    看 dashboard；无建 PBX/开订阅/激活网关权限（g07 反例）；可用 Roles 页签增设多名管理员并指派企业
    目录管理权。
  alias_or_related: 实验主账号 cCpP.admin@ale-training.com 即此角色（实验口径）
  tags: [role, administrator]

- id: g29
  term: DR
  full_name: Direct Reseller
  category: role
  source_pages: p39
  source_quote: |
    "ALE — IR Indirect Reseller — DR Direct Reseller — VAD Value Added Distributor (Grossiste) — EC End
    Customer (Client Final) … The customer's integration partner must be either a 'DR' or an 'IR'." (p39)
  definition: |
    直销经销商：客户集成伙伴的两类准入身份之一（另一为 IR）。
  alias_or_related: 经销链 ALE—VAD/DR/IR—EC
  tags: [role, reseller]

- id: g30
  term: IR
  full_name: Indirect Reseller
  category: role
  source_pages: p39
  source_quote: |
    "IR Indirect Reseller … The customer's integration partner must be either a 'DR' or an 'IR'." (p39)
  definition: |
    间接经销商：客户集成伙伴的两类准入身份之一。
  alias_or_related: 经销链 ALE—VAD/DR/IR—EC
  tags: [role, reseller]

- id: g31
  term: VAD
  full_name: Value Added Distributor（书中括注 Grossiste）
  category: role
  source_pages: p39
  source_quote: |
    "VAD Value Added Distributor (Grossiste)" (p39)
  definition: |
    增值分销商：经销链中间层。
  alias_or_related: 经销链 ALE—VAD/DR/IR—EC
  tags: [role, distributor]

- id: g32
  term: EC
  full_name: End Customer（书中括注 Client Final）
  category: role
  source_pages: p39
  source_quote: |
    "EC End Customer (Client Final) … To be managed by a BP, an 'EC' company must be attached to the
    company of this BP (one and only one attachment)." (p39)
  definition: |
    最终客户（公司）：由 Reseller 创建、唯一挂靠一个 BP；其管理员即 g28。
  alias_or_related: 公司创建六步流程见 f08
  tags: [role, end-customer]

- id: g33
  term: Supervisor
  category: role
  source_pages: p230, p236
  source_quote: |
    "Each supervision group includes • One or several supervisors: they must be granted an Attendant
    license to use the attendant console • The company members to supervise" (p230)
    "Define the supervisor role & In/Out permission for both profiles" (p236)
  definition: |
    监督员：持 Attendant 订阅、进监督组执行监督/代接的用户；最多属 5 个监督组；互助组中其 In/Out 权限
    建组时定义。
  alias_or_related: 被监督成员须有物理话机或 PBX 软终端（互助组场景，p244）
  tags: [role, supervision]

- id: g34
  term: 4059 attendant
  category: role
  source_pages: p208-211
  source_quote: |
    "Create a 4059 EE attendant — Attendant name: OP1 — Physical directory number: B0000 — Associated
    phone set: 31002 … The 4059 EE is declared as a 4059 IP" (p209)
  definition: |
    OXE 话务员：attendant group 内的坐席（4059 EE 应用 + 关联话机/IPDSP 承载话音）；有个人呼叫前缀
    （Indiv. Attendant Call，如 31401）与电话簿条目；系统参数控制其签退行为。
  alias_or_related: 话务组见 f17；与 g16 Rainbow 话务员是两条线
  tags: [role, attendant, oxe]

# ── 三、订阅 (subscription) ──

- id: g35
  term: Rainbow Essential
  category: subscription
  source_pages: p24, p109
  source_quote: |
    "This free option is available to anyone who wants to try Rainbow for an unlimited period (no SLA).
    The Essential subscription can also be blended with any premium subscription" (p24)
  definition: |
    免费订阅：无限期试用、无 SLA、可与付费混用；OXE 场景下只有 RCC、不能改路由。
  alias_or_related: 删除恢复后默认回落 Essential（p103）
  tags: [subscription, free]

- id: g36
  term: Rainbow Business
  category: subscription
  source_pages: p24, p298
  source_quote: |
    "The per-user subscription addresses individuals and teams who want to improve their daily
    communication, on or off-site, on-the-move, or as a productive remote worker." (p24)
  definition: |
    按用户付费订阅：电话服务门槛之一；WebRTC 网关与 Teams 集成的最低订阅档。
  alias_or_related: 与 Enterprise 同为网关/Teams 必备档（p133/p298）
  tags: [subscription, paid]

- id: g37
  term: Rainbow Enterprise
  category: subscription
  source_pages: p24
  source_quote: |
    "The per-user subscription includes all services from Rainbow Business, but with the addition of
    collaborative multi-party services with video conferencing and extended file storage. Integration into
    existing office tools such as Microsoft 0365 and Google Suite also forms part of this service plan." (p24)
  definition: |
    Business 全量 + 多方视频会议 + 扩展存储 + O365/Google Suite 集成；书中实验统一用例（管理员核验、
    成员分配、Teams 集成均示范 Enterprise）；SSO/AAD 导入/频道创建的管理员级别门槛也指向该档。
  alias_or_related: 注意 p96 写法为 "Voice Enterprise" 服务级别
  tags: [subscription, paid]

- id: g38
  term: Rainbow Attendant
  category: subscription
  source_pages: p24, p239-240
  source_quote: |
    "Rainbow Attendant for Hybrid users requires a new specific subscription offer identified as
    'Attendant'. The Rainbow Attendant console presents of a list of waiting calls, with the ability to
    dispatch the calls to other destinations." (p24)
    "Choose the subscription offer: Attendant Monthly. DON'T USE 'PREPAID' IN THE TRAINING" (p239)
  definition: |
    话务台专用订阅（按用户）：解锁 Rainbow 内嵌 Attendant console（排队+监督）；有 Monthly/Prepaid 两种
    offer；仅与 Rainbow 话务台相关、与 4059EE 无关。
  alias_or_related: 4059EE 不需要此订阅（n24）
  tags: [subscription, attendant]

- id: g39
  term: Rainbow Enterprise Conference
  category: subscription
  source_pages: p24
  source_quote: |
    "This per-user subscription packages the Rainbow Enterprise service plan with unlimited phone
    conferencing minutes. The Rainbow Enterprise Conference user subscription is pre-paid yearly in
    advance (twelve months)." (p24)
  definition: |
    Enterprise + 无限电话会议分钟；强制按年预付（12 个月）。
  alias_or_related: 培训环境禁预付（n03）
  tags: [subscription, conference]

- id: g40
  term: Rainbow Conference
  category: subscription
  source_pages: p24
  source_quote: |
    "An optional service proposed as a 'pay-as-you-go' model for phone (PSTN) conferencing with a
    price-perminute/per-connection. The organizer of the meeting can be a Rainbow Essential (freemium)
    user, or premium user" (p24)
  definition: |
    PSTN 电话会议按分钟/连接计费的可选包；组织者可以是免费用户——"免费也能开会"的正确口径。
  alias_or_related: 与 g39 的计费模型不同
  tags: [subscription, conference]

- id: g41
  term: Rainbow Connect
  category: subscription
  source_pages: p24
  source_quote: |
    "The per-user subscription addresses users of any Customer Relationship Management (CRM) application.
    The integration of the Rainbow functionality is provided using a specific connector dedicated to the
    compatible CRM application." (p24)
  definition: |
    CRM 集成订阅（按用户）：经专用连接器把 Rainbow 功能嵌入兼容 CRM；本书不展开。
  alias_or_related: 连接器细节在 CRM 集成文档
  tags: [subscription, crm]

- id: g42
  term: Rainbow Room
  category: subscription
  source_pages: p24
  source_quote: |
    "An optional per-room subscription proposed for meeting rooms equipped with large screens for
    communication and interaction with people inside and outside of the company. Additional hardware is
    required" (p24)
  definition: |
    会议室订阅（按房间）：大屏会议场景，需额外硬件（ALE 有音视频套件）。
  alias_or_related: 本书不展开
  tags: [subscription, room]

# ── 四、产品 (product) ──

- id: g43
  term: OmniPCX Enterprise
  full_name: OmniPCX Enterprise（缩写 OXE，书名页并用）
  category: product
  source_pages: p1, p67
  source_quote: |
    "OMNIPCX ENTERPRISE - EDITION 12" (p1)
    "The OXE must be connected to the Rainbow infrastructure in order to associate directory numbers with
    company members and use PBX resources." (p67)
  definition: |
    ALE 企业级 PBX，本书主角：内置 Rainbow Agent 接云；WBM（web）与 mgr 管理界面；netadmin 网络配置；
    本版要求 Edition 12 生态、网关功能需系统 12.1 MD4/12.2+。
  alias_or_related: 呼叫服务器缩写 CS（p73 "OXE CS Main IP @"）
  tags: [product, pbx, oxe]

- id: g44
  term: OMS
  category: product
  source_pages: p72, p180
  source_quote: |
    "Racks are created in the OXE database. Here we need only the OMS. … Software Rack 3U (OMS) Rack N° 4
    Virtual GD4 (slot 0) IP @: 192.168.1.13/24" (p72)
    "AN IP DOMAIN WITHOUT COMPRESSION BUT WITH COMPRESSION RESOURCES (GD/OMS) IS REQUIRED…" (p180)
  definition: |
    OXE 数据库中的软件机架实例（实验环境唯一需要的机架，Rack 4 上的 Virtual GD4，实验口径 IP
    192.168.1.13）；在网关 IP 域前提中被列为"压缩资源（GD/OMS）"。书中未展开 OMS/GD 全称。
  alias_or_related: 虚机实例名 ENTP_OMS_CSA_CSB_NODE1（p9，实验口径）
  tags: [product, oxe, lab]

- id: g45
  term: 4059 EE
  category: product
  source_pages: p198-213
  source_quote: |
    "By default, the 4059EE attendant console is used to monitor telephony equipment … The 4059 EE is
    declared as a 4059 IP … 4059EE_x.x.x.x.exe" (p199, p209, p212)
  definition: |
    OXE 传统话务台 PC 应用：OXE 里声明为 4059 IP 终端类型；只管话务功能不管话音（必须关联物理话机或
    IPDSP 且非 multi-line）；支持 Rainbow 集成（在场/搜索/IM/BLF/日历/标签搜索）；安装器含 Rainbow
    agent 可选项。
  alias_or_related: Attendant 订阅与其无关（n24）；设备地址格式 [话务员号]@[主机名]（最多 3 主机名）
  tags: [product, attendant, oxe]

- id: g46
  term: IPDSP
  full_name: IP Desktop Softphone（书中展开于 p212 标题 "Commissioning IP Desktop Softphone"；表中写 IP DSP）
  category: product
  source_pages: p10, p72, p209, p212
  source_quote: |
    "An IPDSP to install: 31000 … 2 MicroSIP softphones are installed to simulate public numbers." (p10)
    "31000 Alan Barkley IP DSP Main Installed on PC Client 10" (p72)
  definition: |
    ALE 软话机：实验中装于 PC Client 10/11（分机 31000/31001，实验口径），配置要点是 Settings →
    Network 填 TFTP 服务器（OXE CS 主 IP 192.168.1.3）；4059EE 的话音承载可关联 IPDSP。
  alias_or_related: TFTP = 书中仅以 TFTP server 提及，未展开全称
  tags: [product, softphone, lab]

- id: g47
  term: MicroSIP
  category: product
  source_pages: p10, p14-15
  source_quote: |
    "2 MicroSIP softphones are installed to simulate public numbers. … These numbers are simulated via 2
    MicroSIP clients registered on ITSP1 SIP public" (p10, p14)
  definition: |
    第三方软话机：实验中预装用于模拟公网/紧急号码（注册 ITSP1 公共网关）；互助监督组实验中也作为
    "PBX 软终端"入组（p244）。
  alias_or_related: 与 IPDSP 同为软终端但角色不同（模拟公号 vs 用户话机）
  tags: [product, softphone, simulator]

- id: g48
  term: Rainbow Pilot
  category: product
  source_pages: p32-36
  source_quote: |
    "RAINBOW PILOT allows you to assess your Rainbow connectivity from your location, and the capacity of
    a given location to handle a population of Rainbow users characterized by a flexible mix of usages
    between Collaboration, Conferencing, Hybrid or Hub telephony. • link: https://pilot.openrainbow.com/home" (p33)
  definition: |
    官方连通性与承载容量评估工具：测站点到 Rainbow 的连通性；按协作/会议/混合话音/Hub 用法配比评估
    可承载用户规模；部分测试分区标注 To come（随平台演进）。
  alias_or_related: 与 Network Requirements PDF 配合使用
  tags: [product, tool, presales]

- id: g49
  term: MyPortal
  category: product
  source_pages: p153-154, p174, p255
  source_quote: |
    "Download the WebRTC gateway from My Portal available in 'Taxonomy': OmniPCX Enterprise • OXO Connect
    • OXO Connect Evolution … Tips No matter the system you select, it is the same software" (p154)
    "MyPortal/ Portfolio explorer/ Cloud Communications/ Rainbow" (p174)
  definition: |
    ALE 伙伴门户：下载网关 VM（Taxonomy 下 OXE/OXO/OXO CE 同一软件）、TC2462、TBE067 工具、网关升级包
    （Portfolio explorer/Cloud Communications/Rainbow），以及开 SR（Support > Service Request）。
  alias_or_related: p153 标题出现 "BPWS"（未展开，按上下文与 MyPortal 同指下载入口）
  tags: [product, portal, myportal]

- id: g50
  term: WebRTC Gateway VM 组件（janus-gateway-mediapillar / otlitemediapillargateway / kamailio）
  category: product
  source_pages: p159, p162
  source_quote: |
    "Rainbow WebRTC Gateway version: 1.78.11-470 … - janus-gateway-mediapillar 1.77.6~… -
    otlitemediapillargateway 1.77.6~…" (p159)
    "3 services can be checked: otlitemediapillargateway • janus-gateway-mediapillar • kamailio … sudo
    service … status / restart" (p162)
  definition: |
    网关 VM（Debian 系）内可管理的三个服务：otlitemediapillargateway、janus-gateway-mediapillar、
    kamailio；排障时 sudo service <名> status/restart；版本与配置经 mpshow 查看（书中样例 1.78.11-470）。
  alias_or_related: 命令族见 g58；OS 为 Debian（p135）
  tags: [product, webrtc-gateway, service]

# ── 五、协议 (protocol) ──

- id: g51
  term: SIP Trunk Group (T2)
  category: protocol
  source_pages: p179
  source_quote: |
    "Create a SIP trunk group in order to reach the WebRTC Media Gateway. … Trunk Group IP 5 • Trunk Group
    Type T2 • Q931 Signal variant ISDN all countries • T2 Specification SIP" (p179)
  definition: |
    OXE 侧中继组：连 WebRTC 网关用 T2 类型、T2 Specification=SIP；ARS 表中引用 TG 需先建编号命令表
    （CDT）；回调场景把 TG 挂到专用实体。
  alias_or_related: SIP 为通用标准缩写，书中未展开全称
  tags: [protocol, sip, trunk]

- id: g52
  term: WebRTC (SIP/RTP)
  category: protocol
  source_pages: p133, p160
  source_quote: |
    "WebRTC Gateway — WebRTC SIP/RTP — Rainbow client … Example: Media flows between a Rainbow client and
    a deskphone" (p133)
  definition: |
    Rainbow 客户端与网关间的媒体/信令承载（WebRTC，转换成对 OXE 的 SIP/RTP）；云间媒体加密；网关侧 RTP
    端口范围默认 WRTRANGE=20000-29999、SIPRANGE=30000-39999（mpconfig 输出，p158）。
  alias_or_related: TURN_SERVER=GEOIP 为默认 STUN/TURN 口径
  tags: [protocol, webrtc, rtp]

- id: g53
  term: CSTA
  category: protocol
  source_pages: p87, p186, p265
  source_quote: |
    "4509=rainbowagent: CSTA link (CSTA server<->Rainbow) in service" (p87)
    "Applications / CSTA … Set Callback On Calling Device Yes" (p186)
    "3 MakeCall API (CSTA)" (p265)
  definition: |
    Rainbow agent 与 OXE 呼叫服务器间的计算电话链路（五链路之一），也是 Teams 集成中"点拨分机→PBX 话机
    响"MakeCall API 的底层；Applications/CSTA 页签承载回调开关。书中未展开 CSTA 全称。
  alias_or_related: 4059EE 侧设备注册由 abcacom.exe 支撑（p212）
  tags: [protocol, csta]

- id: g54
  term: XMPP / WebSocket（Rainbow agent 链路）
  category: protocol
  source_pages: p87
  source_quote: |
    "4503=rainbowagent: WebSocket (rainbowagent<->Rainbow) in service • 4505=rainbowagent: XMPP link
    (rainbowagent<->Rainbow) in service" (p87)
  definition: |
    Rainbow agent 与云间五链路中的两条信令链路（事件码 4503/4505）；incvisu 输出全部 in service 为健康
    口径。两协议均为通用标准缩写，书中未展开全称。
  alias_or_related: 五链路全集见 g15
  tags: [protocol, rainbow-agent]

- id: g55
  term: SAML / OIDC
  category: protocol
  source_pages: p44
  source_quote: |
    "Azure AD - SAML … Azure AD - OIDC … ADFS - SAML … with SAML V2 : Shibboleth, RSA, … and with OIDC :
    LemonLDAP, OKTA, CAS APEREO, Ping Identity, …" (p44)
  definition: |
    SSO 的两类标准协议：Azure AD 可走 SAML 或 OIDC、ADFS 走 SAML；其他基于标准协议的 IdP 需 ALE 确认。
    书中未展开两缩写全称。
  alias_or_related: SSO 门槛见 n06
  tags: [protocol, sso, auth]

- id: g56
  term: STUN/TURN (GEOIP)
  category: protocol
  source_pages: p158, p160
  source_quote: |
    "TURN_SERVER='GEOIP'" (p158)
    "STUN/TURN test will be done using GEOIP config … GEOIP file not found, make sure RAINBOW connect test
    is OK … [FAILED]" (p160)
  definition: |
    网关 NAT 穿越（STUN/TURN）配置：默认 TURN_SERVER=GEOIP（按地理位置选 TURN）；mpcheck 的 STUN/TURN
    段依赖 GEOIP 文件，缺失时报 [FAILED] 而非网络故障；TURN 生产部署细节在书外。
  alias_or_related: 见反例 n17
  tags: [protocol, turn, nat]

- id: g57
  term: G.711 / G.722 / G.729（网关编解码口径）
  category: protocol
  source_pages: p181
  source_quote: |
    "Support G722 NO • Support G711 YES • Support G729 NO" (p181)
  definition: |
    OXE 侧 SIP 外部网关（Rainbow type）的编解码支持口径：仅 G711（实验口径取值）；另有 DTMF 动态载荷
    101、SDP in 18x 不勾等媒体参数。生产站点调整编解码前与网关能力核对。
  alias_or_related: UDI（Unrestricted Digital Information）为 ARS 路由质量字段（p183）
  tags: [protocol, codec, sip]

# ── 六、资源 (resource) ──

- id: g58
  term: mp 命令族（mpnetwork / mpconfig / mpshow / mpcheck / mpssh / mpupgrade）
  category: resource
  source_pages: p156-160, p164-166, p175
  source_quote: |
    "Configure the Network settings by using the command mpnetwork … mpconfig --PBX_DOMAIN=… --PBXID=… …
    Check the WebRTC configuration using the command: mpshow … mpcheck … 'mpssh on' … mpupgrade –now" (p156-166)
  definition: |
    网关 VM 的管理命令族：mpnetwork（IP/网关/DNS/主机名/NTP）、mpconfig（PBX 域名+PBXID）、mpshow（版本
    与全量配置）、mpcheck（八段连通性自检）、mpssh on/off（SSH 开关，供 WinSCP/粘贴 PBXID）、mpupgrade
    （手动升级，-now / -delay=30s）。登录账号 rainbow/Rainbow123（实验口径）。
  alias_or_related: sudo reboot / sudo halt 为配套开关机命令（p156-158）
  tags: [resource, webrtc-gateway, cli]

- id: g59
  term: OXE 维护命令族（incvisu / dhs3_init / checkCloudConfig.sh / sipextgw / lookars / motortrace /
    traced / multidevice / zdpost / remotesets）
  category: resource
  source_pages: p87-88, p191-195
  source_quote: |
    "(1)csa> incvisu … (1)csa> dhs3_init -R RAINBOWAGENT … (1)csa> checkCloudConfig.sh -rainbow" (p87)
    "(1)csa> sipextgw -l … (1)csa> lookars i … 101)xa001001>motortrace 3 … >traced … (1)csa> multidevice
    31000 … zdpost d 31000 … remotesets d 2131000" (p191-193)
  definition: |
    OXE 侧维护命令集（mtcl/维护账户，经 console 或 putty）：incvisu（启动事件与五链路）、dhs3_init -R
    RAINBOWAGENT（重启 agent）、checkCloudConfig.sh -rainbow（云连接核查）、sipextgw -l（外部 SIP 网关
    在服状态）、lookars i（ARS 交互验证）、motortrace 3 + traced（信令抓包，killall traced 停，重定向
    落盘）、multidevice/zdpost/remotesets（tandem/multi-device 与 REX 的 BBB 号核验）。
  alias_or_related: 输出中的 IP/号码/ExtNbr 均为实验样例；深排障见 n28
  tags: [resource, oxe, cli, maintenance]

- id: g60
  term: TC2462
  category: resource
  source_pages: p121, p149, p154, p162, p194, p232
  source_quote: |
    "Refer to TC2462" (p121)
    "Technical communication TC2462 – Configuration guide for Rainbow PBX integration with OmniPCX
    Enterprise" (p154)
  definition: |
    OXE-Rainbow 集成配置指南（Technical Communication）：远程延伸、共享网关、网关部署维护、话务台配置
    各章反复指向的生产级依据；MyPortal/伙伴链接获取。
  alias_or_related: OXO 版对应 TC2479（p232 提及）；维护补充文章见 VoIP calling Troubleshooting guide（p194）
  tags: [resource, documentation, tc2462]

- id: g61
  term: TBE067_Rainbow - WebRTC Gateway Pres&Sizing
  category: resource
  source_pages: p151
  source_quote: |
    "An Excel tool is available … This tool is available HERE — TBE067_Rainbow - WebRTC Gateway Pres&Sizing
    - ed06l.zip — ALE internal link HERE • Available from OXE 101.0 MD3 and WebRTC 3.x" (p151)
  definition: |
    网关容量估算 Excel 工具包（ed06l 版）：输入四值（OXE 用户总数/Rainbow 用户数/使用率/直呼占比）得
    并发通道数，再推 OXE 压缩器数；适用 OXE 101.0 MD3 / WebRTC 3.x 起；单网关 400 并发流上限。
  alias_or_related: 流程见 f16 与 principle p20
  tags: [resource, tool, sizing]

- id: g62
  term: SIP Carrier Simulator (ITSP1/ITSP2)
  category: resource
  source_pages: p13-18
  source_quote: |
    "ITSP1 ITSP1 — Public Carrier — SIP Simulator … ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 …
    ITSP2" (p14)
  definition: |
    RLAB 公共区的 SIP 运营商模拟器：ITSP1 提供注册网关（gateway1.itsp1.com，账号 pbxP/alcatel，SIP 域
    sip.itsp1.fr）与公网网关（public.itsp1.com，模拟 Public/Urgence 用户）；ITSP2 存在但本课程未用。
    号码规则与 DDI 表见 f03。ITSP 缩写书中未展开。
  alias_or_related: 全部账号/号码为实验口径
  tags: [resource, simulator, lab]

- id: g63
  term: RLAB (Remote Lab)
  category: resource
  source_pages: p3-11
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data
    center. … Pods are independent of each other … Pods have access to common resources" (p5)
  definition: |
    ALE 培训远程实验室：POD 池 + 公共资源区（NAS/SIP 模拟器/外部 DNS）；学员经 Rlab 门户连各虚机；每
    POD 六实例（OXE/OMS/FlexLM/WebRTC/两台 PC Client）。
  alias_or_related: 拓扑见 f02；IP/密码全表为实验口径（p9）
  tags: [resource, lab, rlab]

- id: g64
  term: status.openrainbow.com
  category: resource
  source_pages: p249-250
  source_quote: |
    "In this case, you can be informed via the following specific site: status.openrainbow.com … The button
    'Get updates' allows … you can subscribe to alerts by different methods." (p249)
  definition: |
    Rainbow 云状态页：数据中心故障时的官方通报渠道；Get updates 订阅告警（按主题/地域过滤，法国建议
    WW+EMEA+DE）；管理门户另有计划维护通知（按地域与架构 Hybrid/Hub 过滤、色标关键度）。
  alias_or_related: 见 f19 与反例 n29
  tags: [resource, status, maintenance]

- id: g65
  term: 培训邮箱 (mail44.lwspanel.com)
  category: resource
  source_pages: p63, p65, p76
  source_quote: |
    "you can consult the user's e-mail box: https://mail44.lwspanel.com/ … Username: e-mail address->
    cCpP.user1@ale-training.com … Password : PasswordP*" (p63)
  definition: |
    RLAB 专用 webmail：核收 Rainbow enrollment/邀请邮件；账号=邮箱地址、密码=PasswordP*（P=POD 号）；
    每轮实验前清理旧邮件。实验口径，生产无此物。
  alias_or_related: 邮件两坑见 n04
  tags: [resource, lab, email]

- id: g66
  term: Rainbow 支持入口（Help Desk Guide / Emily BOT / Global Welcome Center）
  category: resource
  source_pages: p246, p254
  source_quote: |
    "This link provides various sections for resolving customer issues, such as troubleshooting guides,
    finding logs, identifying network or application problems, how to report the issue to the ALE Rainbow
    Customer Care team…" (p246)
    "Support entry points can be : Mail : support@openrainbow.com • Emily BOT • Global Welcome Center …
    ALE.WelcomeCenter@al-enterprise.com" (p254)
  definition: |
    售后支持三入口 + 指南：help.openrainbow.com 的 Help Desk Guide（排障指南/找日志/定位问题/报障流
    程）；报障走 support@openrainbow.com、Emily BOT、Global Welcome Center 或电话——ESR 仅为 Rainbow
    认证伙伴创建；SR 字段清单见 principle p28。
  alias_or_related: status 页见 g64；用户侧上报见 n30
  tags: [resource, support]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 19 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 网络前提与 Pilot | 有 → g48（Pilot）、g25（Hub 概念） |
| task-02 公司体系 | 有 → g02（Company）、g03（Visibility）、g26-g32（角色链） |
| task-03 管理员权责/目录/频道 | 有 → g27/g28（管理员）、g22（企业目录）、g23（信息频道） |
| task-04 订阅开通与分配 | 有 → g35-g42（8 种订阅全列） |
| task-05 RLAB/OXE 实验环境 | 有 → g63（RLAB）、g62（SIP 模拟器）、g44（OMS）、g46（IPDSP）、g47（MicroSIP）、g65（培训邮箱） |
| task-06 DNS/代理配置 | 无术语条。纯操作内容，见 case c03 |
| task-07 OXE 接入 | 有 → g15（Integrated Rainbow Agent） |
| task-08 成员管理 | 有 → g24（Grace period） |
| task-09 分机关联与 RCC | 有 → g06（RCC）、g11（Rainbow number） |
| task-10 用户形态决策 | 有 → g06/g07/g09（RCC/REX/Tandem）、g14（Virtual UA） |
| task-11 远程延伸配置 | 有 → g07（REX）、g08（Ghost Z）、g09（Tandem）、g10（Multi-line） |
| task-12 网关部署 | 有 → g12（WebRTC Gateway）、g50（VM 组件）、g58（mp 命令族）、g56（STUN/TURN） |
| task-13 网关升级 | 有 → g58（mpupgrade 并入） |
| task-14 OXE 网关配置 | 有 → g17（BBB 前缀）、g51（SIP TG T2）、g57（编解码）、g18（Callback）、g59（维护命令族） |
| task-15 共享池与容量 | 有 → g13（共享池）、g61（TBE067） |
| task-16 4059EE 话务台 | 有 → g45（4059 EE）、g19（BLF）、g34（4059 attendant）、g53（CSTA） |
| task-17 Attendant/互助组 | 有 → g16（Attendant console）、g20（监督组）、g21（互助组）、g33（Supervisor）、g38（Attendant 订阅） |
| task-18 维护体系 | 有 → g64（状态页）、g66（支持入口） |
| task-19 Teams 集成 | 有 → g05（TOTP 无关）/缺 Teams 专属术语说明：Teams 双件套已并入 BOOK_OVERVIEW 术语表与 case c12-c14，本书 Teams 术语（Telephony Power App 等）为界面名，未单列条目 |

**统计**：66 条（concept 25 / role 9 / subscription 8 / product 8 / protocol 7 / resource 9）；19 项任务中 18 项有术语覆盖，task-06 为纯操作内容无术语条；Teams 集成术语（Telephony Power App / Rainbow Desktop 为产品界面名，架构见 f20）已由 framework 与 case 覆盖。
