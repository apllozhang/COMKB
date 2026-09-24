# 术语/缩写/产品名候选 — OpenTouch Advanced (OPENXTE301EN Ed08, R2.6.1)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 58 条。MLE/OMS/OTMS/DISA/DDI/DTMF/TFTP 等缩写书中未给全称，full_name 字段如实省略，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: OpenTouch (server / OTMS)
  category: concept
  source_pages: p8, p170, p220
  source_quote: |
    "OPENTOUCH OPEN_OTMS_ADVANCED opentouch 192.168.1.50" (p8，实验实例表)
    "The OpenTouch server handles the voice messaging process and the company mail server/Gmail stores voice
    messages" (p170)
    "Mobility component integrated in OpenTouch server" (p79)
  definition: |
    与 OXE 配套的协作服务器：承载 ICAS 消息服务、ACS 协作会议、移动性组件、UDAS 目录与语音邮箱档案；
    呼叫控制仍在 OXE。实验实例名 OPEN_OTMS_ADVANCED（192.168.1.50，实验口径）。书内缩写 OTMS 未展开全称。
  alias_or_related: OT server；WebAdmin/WBM 为其管理界面（p313）；My Profile/My Messaging 为其用户应用（p210-211）
  tags: [concept, server, core]

- id: g02
  term: Connection user
  category: concept
  source_pages: p34, p44, p274
  source_quote: |
    "This service is dedicated to Connection users" (p34)
    "Modes / Where to use / Notes: Deskphone control ... Mobility mode (aka «Nomadic») ... Softphone mode" (p44)
    "Connection users cannot perform neither peer to peer video communications nor ad hoc video conferences:
    only scheduled video conferences" (p274)
  definition: |
    绑定 OXE 话机的 OT 用户类型（对应"业务话机是物理话机"），可享 Deskphone control / Nomadic /
    Softphone 三种操作模式；nomadic 服务专属于此类用户。注意其视频能力受限（仅预约会议），
    协作限制特性也只作用于 Connection 用户。
  alias_or_related: 对照 g03 Conversation user；g14 Connection user license
  tags: [concept, user-type]

- id: g03
  term: Conversation user
  category: concept
  source_pages: p79, p274
  source_quote: |
    "Same application for Conversation and Connection users" (p79)
  definition: |
    纯 OT 软用户类型（业务话机即 PC）：拥有点对点视频与 ad-hoc 视频会议能力（Connection 用户没有）；
    协作特性全开（"conversation users are always full collaborative users"，p291）。书内仅相对
    Connection user 提及，无独立定义页。
  alias_or_related: 对照 g02
  tags: [concept, user-type]

- id: g04
  term: Nomadic mode (Mobility mode)
  category: concept
  source_pages: p34-35, p44, p46
  source_quote: |
    "The 'Nomadic service' brings complete access to the OpenTouch phone features and other services offered by
    OTC PC application to remote workers" (p34)
    "Once nomadic mode is activated, the user phone set in the office is frozen and disabled. All audio is
    re-routed toward his multimedia computer or toward a physical phone set (cellular…)" (p34)
    "There are two different Nomadic modes available: 1/ Cellular mode ... 2/ VoIP mode" (p46)
  definition: |
    Connection 用户的移动模式：激活后办公话机冻结（frozen），音频改道到家庭/手机号（蜂窝，经 Ghost Z）或
    多媒体 PC（VoIP，经 Ghost Z + SIP 设备）；用户像在办公室一样使用电话服务应用。
    经 OTC PC 的 routing 窗口选"当前电话"激活。
  alias_or_related: Mobility mode（p44 同义）；两模式见 f04/f05
  tags: [concept, mobility, core]

- id: g05
  term: Ghost Z set
  category: concept
  source_pages: p39, p46-47, p51, p125
  source_quote: |
    "Pool of nomadic Ghost Z devices: Required whatever the nomadic mode used" (p39)
    "the incoming call is rerouted, thanks to a 'virtual ghost Z set', to another phone number" (p46)
    "Ghost Z sets are retained as busy throughout the connection and are only released when nomadic mode is
    disabled." (p47)
    "This number can start with the format B<Dir. No.> to avoid using a real number. Example given.: B31091" (p125)
  definition: |
    OXE 侧虚拟 Z 设备（Set Type Analog + Ghost Z feature）：nomadic 连接的改道枢纽——每路蜂窝连接占 1 个、
    每路 VoIP 连接占 1 个；连接期间保持 busy 直至关闭 nomadic；按池管理，并发数=池规模。
    远程扩展用途的 Ghost Z 目录号可用 B<号码> 占假号。nomadic（feature=Nomadic）与 RE（feature=Remote
    Extension）两种 feature 用途。
  alias_or_related: 池在 OT 侧经 OXE Resources（min/max）登记（p48）
  tags: [concept, ghost-z, capacity, core]

- id: g06
  term: Remote Extension (REX)
  category: concept
  source_pages: p92-94, p137
  source_quote: |
    "Remote extension • Remote extension itself • Speed dialing number • For automatic substitution" (p92)
    "Directory number Automatically configured (e.g.: 2131001) ... Set type Automatically set: Remote
    extension" (p137)
  definition: |
    OXE 侧远程扩展设备：OTC 智能手机在 OXE 的落地形态（Set type=Remote extension），配直达速拨号实现 DISA
    呼入时的自动替换；与主话机构成 Tandem。R2.6 起可直接作主设备（单设备）。书内未展开 REX 全称。
  alias_or_related: Remote extension number = 外线手机号前缀（例 #0306xxxxxxxx，p137）；对照 g05 Ghost Z
  tags: [concept, rex, smartphone]

- id: g07
  term: DISA
  category: concept
  source_pages: p92, p121-123, p137
  source_quote: |
    "Remote extension DISA prefix" (p92)
    "Remote extension DISA prefix ... Number Enter the prefix directory number (e.g.: 31280)" (p122)
    "Automatic DISA Substitution Without code" (p122)
    "Trunk group used in DISA Yes" (p123)
  definition: |
    远程扩展的公网呼入机制：DISA 前缀（实验 31280）经 DDI 翻译成公网号供手机侧回拨落地；速拨号触发自动替换
    （无需输入码，Without code）。需系统级+中继组级两级授权。书内未展开 DISA 全称。
  alias_or_related: 依赖 g06 RE 与 DDI 翻译表
  tags: [concept, disa, telephony]

- id: g08
  term: Tandem (twinset)
  category: concept
  source_pages: p92, p139
  source_quote: |
    "Tandem" (p92，对象清单)
    "A tandem (twinset) is configured between both the main desktop phone and the remote extension. ... To
    configure a tandem, both the desktop and remote extension must be multi-line devices. At least two lines,
    normally L1 and L2" (p139)
  definition: |
    主话机与远程扩展间由系统自动建立的绑定结构（twinset 多设备）：两端都必须是多线设备（至少 L1/L2），
    Tandem 目录号=RE 号码、主设备勾 Main set。
  alias_or_related: 自动创建对象之一（p94）
  tags: [concept, tandem, smartphone]

- id: g09
  term: Desksharing (DSU / DSS)
  category: concept
  source_pages: p59-61
  source_quote: |
    "OXE desksharing feature allows a connection user (called DSU: DeskSharing User) to use a physical set,
    called DSS (DeskSharing Set)." (p59)
    "An OXE user configured as 'DSU' doesn't have an associated device. It can log on a 'DSS' and use it until
    it released it" (p59)
  definition: |
    OXE 共享工位机制：DSU（共享用户，无绑定设备，虚拟 MAC=aa:bb+号码）凭前缀 600/601+密码登录/登出任意
    DSS（共享话机，真实 MAC）；支持 nomadic（登出态由 OTC PC 的 UA 软话机替代，不冻结任何话机）。
  alias_or_related: 前缀 600=Over Logon、601=Logoff（p64）；OTC PC 远程释放需 Desktop+Flex Office（p72）
  tags: [concept, desksharing, core]

- id: g10
  term: OTC (PC / Mobile / Web)
  category: concept
  source_pages: p79, p323, p341
  source_quote: |
    "OTC is based on OTC client installed on mobile device • Same application for Conversation and Connection
    users • Installed from markets: Google Play; App Store" (p79)
    "Alcatel-Lucent OpenTouch™ Conversation for WEB • Also called OTC WEB (short name) • Available for
    everyone" (p323)
  definition: |
    OpenTouch Conversation 客户端家族统称：OTC PC（桌面）、OTC Mobile（Android/iPhone 应用）、OTC Web
    （浏览器免装）。提供电话控制、目录、通话记录、VVM、在场、IM 等服务（p79 特性清单）。
  alias_or_related: Android 版名 OpenTouch Conversation、iPhone 版名 OpenTouch Conversation Plus（p143/p145）
  tags: [concept, client]

- id: g11
  term: DAS rules
  category: concept
  source_pages: p299, p301, p306
  source_quote: |
    "The call routing rules are called DAS rules. DAS rules are a set of up to 20 Unix regular expressions that
    are applied to the user's dialed digits. The rules are applied in order, one after the other, the output of
    each rule is the input to the next one." (p299)
    "The rules are linked to a domain" (p317)
  definition: |
    ACS 的呼叫路由规则：最多 20 条 Unix 正则，按序串行处理所拨号码（系统选项格式化之后）；按 Domain 配置、
    按国家定制。管理入口 Configuration → Advanced settings → Edit DAS rules。
  alias_or_related: 法国 10 条集见 principle p43；处理管线见 framework f15
  tags: [concept, das, dialplan, core]

- id: g12
  term: UDAS
  category: concept
  source_pages: p220-222
  source_quote: |
    "UDAS is a module that receives requests from client phone or software searching for contacts information
    stored on OpenTouch server • Client search requests are driven to UDAS using a web service implemented in
    Chameleon." (p220)
    "Dedicated to synchronize with external LDAP directories available in the company infrastructure • Used to
    manage 'call by name' feature" (p221)
  definition: |
    Universal Directory Access Service：把 OXE 电话簿、OT 内部目录、外部 LDAP 同步进 PostgreSQL 同步库的
    模块；所有客户端搜索查同步库而非源目录（单向同步）。支撑 call by name 与联系人卡展示。
  alias_or_related: 同步表 phonebookdir/internaldir/ldapdir/merged_directory（p223/p227）
  tags: [concept, udas, directory, core]

- id: g13
  term: Single Business Card (SBC)
  category: concept
  source_pages: p226, p252
  source_quote: |
    "Single Business Card (simplified to SBC) allows to merge information from several directories to avoid
    multiple responses to a search for the same user." (p226)
    "SYNCHRONIZATION ORDER DEFINES DATA PREVALENCE BETWEEN DIRECTORIES" (p252)
  definition: |
    UDAS 的目录合并机制：把多个目录合并为 merged_directory，同名联系人按权重（Synchronization Order）取值、
    按 Merge keys（至少姓+名）识别为同一人；照片同化（Avatar>LDAP>本地）依赖其开启。
    注意与 OTSBC（会话边界控制器）缩写撞车。
  alias_or_related: Merge keys 见 principle p22；对照 g41 OTSBC
  tags: [concept, sbc-merge, directory]

- id: g14
  term: Impersonation / Delegation
  category: concept
  source_pages: p189-190
  source_quote: |
    "Method C, impersonation, is more used when a service application needs to access multiple mailboxes and
    'act as' the mailbox owner. Impersonation is the best choice when you're dealing with multiple mailboxes"
    (p189)
    "Since the release 2.3 ... the OpenTouch server uses now impersonation method instead of delegation" (p189)
  definition: |
    OT 访问 Exchange 邮箱的两种授权模式：Delegation（逐邮箱委托，R2.2 前用，大流量有隐患）与 Impersonation
    （服务账号"扮演"邮箱所有者，R2.3 起 OT 标准方案，EMS 授 ApplicationImpersonation 角色）。
  alias_or_related: 特权账号见 g46 ICEaccess；实现参考 TC2391（p190）
  tags: [concept, um, exchange]

- id: g15
  term: Downstream / Upstream authentication
  category: concept
  source_pages: p418, p427
  source_quote: |
    "'Downstream authentication' means that the user has not been authenticated before the client sends a
    request to the OpenTouch server ... the server performs the authentication on the authentication service
    (which may be internal or external)" (p418)
    "'Upstream authentication' means that the OpenTouch server is not responsible for performing the
    authentication ... Kerberos, NTLM V2 are protocols that can be used" (p427)
  definition: |
    外部认证两方向：Downstream=OT 验证用户（LDAP/LDAPS/RADIUS 插件，DTA/JAAS 链）；Upstream=外部先验、OT
    验票据（Kerberos/NTLM V2，经 authenticationbasic/authenticationform 应用的 web.xml 模板启用）。
  alias_or_related: 内部认证源=DTA（g16）；级联规则见 counter-example n35/n36
  tags: [concept, authentication, core]

- id: g16
  term: DTA / Alcatel User ID / External login
  category: concept
  source_pages: p417, p421-424, p433
  source_quote: |
    "This server is the DTA (means 'DaTa Access; internal authentication database)" (p417)
    "the DTA computes an internal value named Alcatel User ID ... stored in a session cookie" (p424)
    "In the 8770, manage the 'external login' field for each user • Assign his account name managed in the LDAP
    directory" (p433)
  definition: |
    OT 认证三元组：DTA=内置认证数据库（默认认证源，外认失败时 Web 客户端级联回落）；Alcatel User ID=DTA 由
    匹配结果计算的内部标识（存会话 cookie）；External login=OT 用户上填写的"外部身份"字段，与 LDAP 的
    user.uid.attribute（AD 为 sAMAccountName）或 Radius login 匹配。
  alias_or_related: 全局唯一约束见 n40
  tags: [concept, authentication]

- id: g17
  term: Calendar presence / Calendar synchro
  category: concept
  source_pages: p386-392
  source_quote: |
    "Calendar information is an additional text message added next to the user presence status" (p387)
    "The main purpose of the OpenTouch/Exchange calendar synchronization is to perform actions to
    Create/Modify and Delete Exchange Calendar Appointment on the behalf of an OpenTouch user" (p390)
  definition: |
    两个日历特性：presence=Exchange 日历状态作为在场旁注文本（不改颜色码、自己看不到自己、FREE 仅名片
    显示）；synchro=OT↔Exchange 会议双向同步（Wireal/EWS，配置与 UM 同源）。本地存储邮箱另走 TC2558。
  alias_or_related: 状态优先级 OOO>Busy>Tentative>Working Elsewhere>Free（p389）；配置参考 TC2258
  tags: [concept, calendar]

- id: g18
  term: Fallback mode (DTMF)
  category: concept
  source_pages: p80, p89
  source_quote: |
    "No data connection • Fallback mode using DTMF" (p80)
    "Features provided in fallback mode based on DTMF over voice flow: Communication context: Make call &
    Release call • Voicemail • Routing (limited)" (p89)
  definition: |
    OTC Mobile 无数据连接时的降级模式：基于语音流上的 DTMF 按键，仅支持呼出/挂断、语音信箱、有限路由；
    Android 无 SIM 卡（纯 VoIP）场景无 fallback。
  alias_or_related: 双模设备的 GSM 倒换计时口径见 principle p08
  tags: [concept, mobile, dtmf]

# ── 二、许可/权限 (subscription，本书无云订阅，此组为 OT/OXE 许可与权限) ──

- id: g19
  term: Desktop (license)
  category: subscription
  source_pages: p46, p49, p54, p72, p340
  source_quote: |
    "a 'Desktop' license must be assigned to the user to be able to activate nomadic mode from OTC PC desktop
    client" (p46)
    "Desktop Must be enabled" (p49, p54)
    "Enable the following licenses ... Desktop • Flex Office" (p72)
  definition: |
    OT 基础客户端许可：nomadic（蜂窝/VoIP）激活、Desksharing 远程释放（与 Flex Office 配对）、协作/会议
    功能（与 Conferencing 配对，p340）的共同前提。
  alias_or_related: 与 g20-g22 组合使用
  tags: [subscription, license]

- id: g20
  term: Nomadic GSM / Nomadic SIP (rights)
  category: subscription
  source_pages: p47, p51, p49, p54
  source_quote: |
    "Assign the 'Nomadic GSM' right to the user" (p47)
    "Nomadic SIP Must be enabled" (p54)
  definition: |
    nomadic 两模式的专用权限（licenses 页签）：Nomadic GSM 开蜂窝模式、Nomadic SIP 开 VoIP 模式；
    均须与 Desktop 并用，VoIP 还以蜂窝配置为前提。
  alias_or_related: 见 principle p03
  tags: [subscription, license, nomadic]

- id: g21
  term: Off site mobility (right)
  category: subscription
  source_pages: p133, p136
  source_quote: |
    "'Off site mobility' right ... Off site mobility Checked" (p133)
    "Don't forget to assign the mobility right to the user." (p136)
  definition: |
    OTC 智能手机用户使用移动服务（手机经 OT 服务）的专用许可，设备关联后必须手动勾选，漏勾则手机侧不可用。
  alias_or_related: OT configuration → Licenses 页签
  tags: [subscription, license, smartphone]

- id: g22
  term: Conferencing / Voice mail / Flex Office / OT Applications (rights)
  category: subscription
  source_pages: p340, p204-206, p72
  source_quote: |
    "To be able to set up 'conference', and so to establish voice communications, the 'Conferencing' item has
    also to be validated" (p340)
    "Make sure that the 'voice mail' right is granted to the user" (p206)
    "Flex Office Enabled" (p72)
    "PLEASE ASSIGN THE RIGHT TO USE 'OT APPLICATIONS' TO THIS USER" (p72)
  definition: |
    其余功能许可：Conferencing（建会/通话，日历同步也要求每用户有会议许可，TC2258 p9）、Voice mail（留言
    功能）、Flex Office（Desksharing 远程释放，与 Desktop 配对）、OT Applications（OT 数据库未知用户的
    兜底权限）。
  alias_or_related: 均在 Licenses/权限页签配置
  tags: [subscription, license]

- id: g23
  term: Connection user license + universal connection client license + REX 资源
  category: subscription
  source_pages: p161
  source_quote: |
    "Cost • Deskphone: OXE deskphone (hardware + license) • Smartphone: hardware + … • Connection user license
    + universal connection client license + REX with needed resources (GhostZ, IP or/& DTMF resources ) • NFC
    tags" (p161)
  definition: |
    Extended Mobility 成本口径中的许可清单：Connection 用户许可 + universal connection client 许可 +
    REX 所需资源（GhostZ、IP 和/或 DTMF 资源）——售前算价的许可项清单。
  alias_or_related: 详见 principle p41
  tags: [subscription, licensing, cost]

# ── 三、产品/组件名 (product) ──

- id: g24
  term: OXE (OmniPCX Enterprise)
  category: product
  source_pages: p8, p29, p38
  source_quote: |
    "OXE OPEN_OXE_ADVANCED csa (physique) csm (principal)" (p8)
    "OmniPCX Enterprise Communication Server" (p38 架构图)
  definition: |
    ALE 企业级通信服务器（本书宿主 PBX）：保留呼叫控制、话机生态与编号计划；实验实例 OPEN_OXE_ADVANCED
    （csa/csm 双 CPU）。书内 p29 完整拼写 OmniPCX Enterprise。
  alias_or_related: 配置经 OmniVista 8770 的 OXE 配置窗口/配置工具
  tags: [product, pbx, core]

- id: g25
  term: OMS
  category: product
  source_pages: p8, p26, p28
  source_quote: |
    "OMS OPEN_OMS 192.168.1.13 root letacla1" (p8)
    "Racks are created in the OXE database. Here we need only the OMS. ... Software Rack 3U (OMS)" (p26)
  definition: |
    实验 POD 中的 OXE 组件（软件机架 3U，Virtual GD4 192.168.1.13）：Pod 配置核对的对象之一。
    书内未展开 OMS 全称，仅作组件名使用。
  alias_or_related: Rack N°4、Virtual GD4 slot 0（p26）
  tags: [product, lab]

- id: g26
  term: OmniVista 8770
  category: product
  source_pages: p8, p105, p123, p313
  source_quote: |
    "8770 OPEN_8770_ADVANCED nms 192.168.1.70 Administrator adminnmc Superuser Superuser01*" (p8)
    "In the OmniVista 8770 application, select the 'OpenTouch' configuration window" (p105)
  definition: |
    ALE 网管/配置平台（实验实例 nms，192.168.1.70）：全书配置操作的统一入口——OpenTouch 配置窗口、OXE
    配置窗口、Users 应用、Profiles 页签、WBM 跳转等均从其 Configuration 应用发起。书内未展开 8770 全称。
  alias_or_related: WebAdmin 账号 otAdmin/admin8770（实验口径，p313）
  tags: [product, management]

- id: g27
  term: OTSBC (OT SBC)
  category: product
  source_pages: p102, p105-107, p332
  source_quote: |
    "OTSBC declaration ... FQDN Enter the public FQDN of the OTSBC (e.g: ot-podX.company.com) Network type WAN
    Port 5261" (p105-106)
    "Declare the OTSBC for WebRTC use: otsbc-podx.company.com ... Port 8061" (p106)
    "Audio access through PSTN OR through OTSBC (if using Web RTC)" (p332)
  definition: |
    OpenTouch 会话边界控制器：远程 OTC 客户端的 SIP 注册（5261）与 WebRTC 音频（8061）入口，媒体段
    RTP/sRTP 7000-7499；iPhone+ 另需同 FQDN、5265 端口的专用 SBC 声明。注意与 Single Business Card（g13）
    缩写撞车。
  alias_or_related: iPhone+ SBC 见 framework f08
  tags: [product, sbc, security]

- id: g28
  term: Reverse Proxy (RP)
  category: product
  source_pages: p38, p104-105, p332
  source_quote: |
    "Connection through Reverse Proxy & SBC (if VoIP) or through VPN" (p38)
    "SystemServices/System services/Topology/Reverse proxy ... API public URL ... EVS public URL ... ACS public
    URL ... DMS public URL" (p105)
    "Https access through internet for data access (RP)" (p332)
  definition: |
    DMZ 中的反向代理（OTC Web 架构图示例 Blue Coat 或 NGINX，p332）：远程客户端的数据面 https 入口，
    四个公共 URL（API/EVS:8016/ACS/DMS）在 OT 拓扑里声明。
  alias_or_related: Kerberos 不支持经 RP（n38）
  tags: [product, remote-access]

- id: g29
  term: ACS (Advanced Communication Server)
  category: product
  source_pages: p109, p299, p313-314, p316
  source_quote: |
    "ACS (Advanced Communication Server) can be configured with rules to handle a broad range of call routing
    and dial plan requirements." (p299)
    "Welcome page of Conference server Administration Console" (p314)
    "Outbound SIP Proxy / Default Outbound SIP Proxy OpenTouch IP address ... Port 5260" (p316)
  definition: |
    OT 的协作会议组件（=会议服务器）：承载会议桥、DAS 规则、电话格式规则、SIP 代理（Outbound/Inbound 5260）、
    系统选项与会议管理台（Users and devices/Conference server）。
  alias_or_related: 管理台经 WebAdmin（otAdmin/admin8770，实验口径）
  tags: [product, conference, core]

- id: g30
  term: AMS (ALE International Media Server)
  category: product
  source_pages: p273, p296
  source_quote: |
    "This video MCU can be the ALE International Media Server (AMS): an internal video media server, included
    in the OpenTouch server" (p273)
    "AMS supports only the switched presence ('Active talker'): no continuous presence" (p273)
  definition: |
    OT 内置视频媒体服务器（MCU）：多方视频的混流点，仅支持 Active talker 切换画面；外部 Radvision MCU 与
    UVC LifeSize 已不再支持。Dial by URI 架构中经 5260 端口与 SIP 代理互连。
  alias_or_related: 端口见 principle p14
  tags: [product, video, mcu]

- id: g31
  term: DCS (Document Conversion Server)
  category: product
  source_pages: p344, p365-368
  source_quote: |
    "a DCS (Document Conversion Server) is mandatory" (p344)
    "the server, called DCS (Document Conversion Server), is necessary • MS Office documents format: ppt, pptx,
    doc, docx, xls, xlsx • The DCS server can be internal (part of the OpenTouch server), or external" (p365)
  definition: |
    会议文档演示的 Office 文档转换服务器：Basic 模式（无 DCS）只支持 pdf/图片；装 DCS 后 Office 文档可作
    presentation。形态：内部（OT 内 KVM 虚机）或外部（ESXi VM/物理机）。注意与实验环境里名为 DCS 的虚机
    （192.168.1.31）重名。
  alias_or_related: 安装步骤见 c18；兼容矩阵见 principle p35
  tags: [product, dcs, conference]

- id: g32
  term: Wireal (WireALL) / MASC
  category: product
  source_pages: p215, p391
  source_quote: |
    "MASC: Mail Access Server Component • Wireal: WireALL, manages interactions with Exchange ... service
    'name' restart where 'name' can be: mascd • wireald" (p215)
    "Link to Exchange Server managed by 'Wireal' component" (p391)
  definition: |
    UM/日历与 Exchange 交互的两个守护进程：MASC（邮件访问组件）与 Wireal（管理与 Exchange 的交互，日历
    同步也由它经 EWS 承担）。排障先看两服务状态与 logs/masc、logs/wireal。
  alias_or_related: 日历排障命令清单见 principle p46
  tags: [product, um, daemon]

- id: g33
  term: APNS
  category: product
  source_pages: p97-98
  source_quote: |
    "All notifications from OpenTouch server to OTC iPhone are sent through Apple Push Notification Server
    (APNS). APNS is an Apple Cloud service" (p97)
    "APNS's certificate is shipped with OpenTouch server • Valid one year" (p98)
  definition: |
    苹果推送通知服务：OT→iPhone 通知的必经云（TCP 5223/2195/2196/443）；OT 随附 APNS 证书一年有效、
    每年需装专用 hotfix。自 OT R2.3.1 起。
  alias_or_related: 端口/证书口径见 principle p12
  tags: [product, push, iphone]

- id: g34
  term: kamailio-wasp / wspcfg
  category: product
  source_pages: p101, p147
  source_quote: |
    "kamailio-wasp: SIP proxy between SBC and OXE • wspcfg: service to provide configuration for kamailio" (p101)
    "Service Kamailio: service kamailio-wasp status|start|stop|restart ... Log files: /var/log/localmessages" (p147)
  definition: |
    iPhone "VoIP everywhere" 两个专用组件：kamailio-wasp（SBC 与 OXE 之间的 SIP 代理，缓冲 TCP INVITE）与
    wspcfg（给 kamailio 提供配置）。维护命令与日志路径见 p147。
  alias_or_related: Logzipper 包含两类日志（p147）
  tags: [product, sip-proxy, iphone]

- id: g35
  term: DCS (lab VM) / ECOSYSTEM
  category: product
  source_pages: p8, p113, p194
  source_quote: |
    "DCS OPEN_DCS dcs 192.168.1.31 Administrator superuser • ECOSYSTEM OPEN_ECOSYSTEM eco 192.168.1.100" (p8)
    "access to CA hosted on Eco system server: https://eco.company.com/CertSrv" (p113)
    "Open the 'Exchange Administrative Center' interface, on the ecosystem" (p186)
  definition: |
    实验 POD 的两台 Windows 服务器：DCS 虚机（dcs，192.168.1.31，与文档转换服务器重名，注意语境）与
    ECOSYSTEM（eco，192.168.1.100）——承载 Windows CA（CertSrv）、AD、Exchange 管理中心等企业侧角色。
    纯教学基础设施。
  alias_or_related: 账号均为 Administrator/superuser（实验口径）
  tags: [product, lab]

- id: g36
  term: IPDSP / MicroSIP
  category: product
  source_pages: p16, p26-27, p10
  source_quote: |
    "An IPDSP to be installed, it will be the main softphone to use directory number: 104." (RAINXTE 同族表述；
    本书 p26-27: "Install and bring into service the IPDSP softphones ... 31000 Brad Barkley IP DSP Main
    Installed on PC Client 10")
    "2 MicroSIP softphones are installed to simulate public numbers." (p10)
  definition: |
    实验软话机：IPDSP（ALE IP 桌面软话机，用户 31000/31001 分别装于 PC Client 10/11，TFTP 指向 OXE CS
    192.168.1.3）与 MicroSIP（预装 2 个模拟公网号码）。教学专用。
  alias_or_related: 混合模式下 31000/31001 要改为实机类型（p28）
  tags: [product, lab, softphone]

- id: g37
  term: ITSP1 (SIP Carrier Simulator)
  category: product
  source_pages: p19-23
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... ITSP1 Public gateway public.itsp1.com 10.20.30.50"
    (p20)
  definition: |
    培训专用 SIP 运营商模拟器（RLAB 公共区）：SIP 网关 gateway1.itsp1.com + 公网网关 public.itsp1.com，
    账号 pbxP/alcatel；ITSP2 仅在拓扑图出现无细节。生产行为与真实运营商有差异。
  alias_or_related: 号码规则见 principle p07
  tags: [product, lab, sip]

- id: g38
  term: PRS (Presentation Server)
  category: product
  source_pages: p232, p258
  source_quote: |
    "Presentation Server (PRS) is the mandatory access point to the Web applications able to deliver services
    over NOE compliant terminals ... It may be considered as the link between the telephonic world and the
    applications world" (p232)
    "make sure that the 'PRS' (Presentation server) is properly configured ... Select the 'Presentation server
    - opentouch'" (p258)
  definition: |
    NOE 终端 Web 应用的强制接入点（连接电话世界与应用世界）：话机 Home 页与 Communicate by name 应用的
    前提，在 Network/OXE CS 节点选 "Presentation server - opentouch"，必要时重启 prs/tomcat。
  alias_or_related: IP Touch 应用声明见 c15 步骤 8
  tags: [product, prs, deskphone]

- id: g39
  term: ICEaccess
  category: product
  source_pages: p180, p184-185, p196, p395
  source_quote: |
    "Create a user account – is used by the OpenTouch server to interact with the Exchange server" (p180)
    "Create 'ICEaccess' user in the Active Directory Login: ICEaccess Password: iceaccess" (p184)
  definition: |
    OT 访问 Exchange 邮箱的特权 AD 账号（实验名 ICEaccess/iceaccess，密码永不过期）：需配邮箱，
    授权走 Impersonation（新）或 Delegation（旧）。UM 与日历特性共同依赖。
  alias_or_related: 密码实验口径见 n49；实现参考 TC2391
  tags: [product, um, credentials]

- id: g40
  term: ice_kerb / ice_kerb.keytab / wbm_admin
  category: product
  source_pages: p436, p448, p452-454
  source_quote: |
    "Creation of a user account ('ice_kerb'), dedicated for OpenTouch, is mandatory" (p436)
    "The 'ice_kerb.keytab' file contains hashed OpenTouch Kerberos account and password ... using 'ktutil'
    command" (p448)
    "Let's assume that 'wbm_admin' is this administrator account." (p452)
  definition: |
    Kerberos 三件套账号：ice_kerb=AD 中 OT 专用的 Kerberos 服务账号（密码与 keytab 一致、不可改、永不过期、
    注册两条 SPN）；ice_kerb.keytab=ktutil 生成的哈希凭据文件（放 tomcat conf）；wbm_admin=Kerberos 启用后
    预留的 WBM 管理 AD 账号（External login 映射 + Delegate authentication）。
  alias_or_related: 配置四件套见 principle p27；锁死风险见 n37
  tags: [product, kerberos, credentials]

# ── 四、协议/技术名 (protocol) ──

- id: g41
  term: EWS (Exchange Web Services)
  category: protocol
  source_pages: p174, p196, p391
  source_quote: |
    "Exchange Web Services ... HTTPS" (p174 架构图)
    "Protocol Select 'Exchange Web services' ... Port ... 443 by default" (p196)
    "E.W.S ... OpenTouch server Wireal" (p391)
  definition: |
    OT 与 Exchange 的集成协议：UM 邮件存取、日历同步（Wireal 经 EWS）、通知（O365 场景的
    /ExchangeNotificationService URL 规则）都基于 EWS over HTTPS 443。
  alias_or_related: 邮件服务器声明必选项 Protocol=EWS
  tags: [protocol, exchange]

- id: g42
  term: LDAP / LDAPS / Radius
  category: protocol
  source_pages: p418, p425, p435, p459-460
  source_quote: |
    "External downstream authentication protocols can be LDAP/LDAPS (external LDAP server), Radius (external
    Radius server), or other on request" (p418)
    "Radius database ... 'External Login' (in OT DB) must match the Radius Login" (p425)
    "server.authenticator=pap" (p460)
  definition: |
    Downstream 外部认证两协议：LDAP/LDAPS（389/636，OT 插件经 user.uid.attribute 匹配 External login）、
    RADIUS（认证 1812/计费 1813，pap/chap 等 scheme，shared_secret 共享密钥）。分别由
    plugin_ldap.properties / plugin_radius.properties 配置。
  alias_or_related: 参数清单见 principle p25/p26
  tags: [protocol, authentication]

- id: g43
  term: Kerberos (KDC / TGT / SPN / keytab)
  category: protocol
  source_pages: p427, p429, p435-436, p451
  source_quote: |
    "Kerberos, NTLM V2 are protocols that can be used for this kind of external authentication" (p427)
    "KDC (Key Distribution Center) – Active Directory Domain Controller ... Authentication Service (AS) and
    Ticket Granting Service (TGS) ... [1] Request (TGT) [2] Service Ticket and Session Key" (p429)
    "'setspn –A HTTP/opentouch ice_kerb'" (p451)
  definition: |
    Upstream SSO 协议：用户 Windows 会话凭据 → AD 域控（KDC，AS/TGS）发 TGT/服务票据 → OT 用 keytab 验票
    识人 → External login 匹配 DTA 用户。NTLM V2 亦为 Upstream 可选协议（模板同机制）。
    深入参考 TC1623（p436）。
  alias_or_related: 配置流程见 c21；限制见 n38
  tags: [protocol, kerberos, sso]

- id: g44
  term: ARS (Automatic Route Selection) / Discriminator
  category: protocol
  source_pages: p92, p128, p140-141
  source_quote: |
    "ARS management • ARS table • Discriminitor" (p92)
    "Automatic Route Selection prefix Enter the ARS prefix used to reach the mobile number. Example: #0306" (p128)
    "Translator/Automatic Route Selection/ARS Route list ... Route 1 ... SIP device number • Route 2 ...
    external mobile number using public TG" (p141)
  definition: |
    OXE 呼出路由体系：ARS（菜单全文 Automatic Route Selection）按前缀+识别码（Discriminator）选路由；
    智能手机场景自动生成每用户一张 ARS 表（Route 1=SIP 设备 VoIP、Route 2=公网中继拨手机），识别码把逻辑
    ID 映射到物理 ID 并受公网 COS 闭锁约束。
  alias_or_related: 数值口径见 principle p11；DAS 是 ACS 侧的另一套路由体系（勿混）
  tags: [protocol, routing, ars]

- id: g45
  term: DDI / DID
  category: protocol
  source_pages: p23, p24, p122
  source_quote: |
    "DDI table - First external nb 41000 ... DDI table – First internal nb 31000 ... Range size 500" (p23)
    "2.4. DID Translation ... First external number 33210N41000" (p30)
    "Warning CHECK THAT THIS PREFIX IS TRANSLATED IN THE DDI TRANSLATION TABLE" (p122)
  definition: |
    外线直拨号码映射（书中 DDI/DID 混用，同一机制）：把外线号段映射到内线（实验 33210N41000 ↔ 31000，
    范围 500）；DISA 前缀必须能被 DDI 翻译表翻译。缩写未展开。
  alias_or_related: 实验号段见 principle p07
  tags: [protocol, numbering]

- id: g46
  term: SIP URI (Dial by URI)
  category: protocol
  source_pages: p279, p295-296
  source_quote: |
    "SIP URI" (p279 Details 页签)
    "For example: English: sip:31250@opentouch.company.com ... The device may have a programmable key to join
    the conference." (p295)
    "SIP proxy listening on default SIP port (5060)" (p296)
  definition: |
    会议的 SIP 拨叫入口：任意 LAN 内 H.264 SIP 设备拨会议 URI（sip:31250@opentouch.company.com）带音视频
    入会；ACS 的 SIP 代理监听 5060，组件间 5260。仅限 LAN 内设备。
  alias_or_related: 入口随邀请邮件按语言发放（p279）
  tags: [protocol, sip, conference]

- id: g47
  term: SIP TLS / SRTP / RTP
  category: protocol
  source_pages: p38, p332
  source_quote: |
    "SRTP • SIP TLS ... HTTPS" (p38 nomadic 架构图)
    "SIPS flow • SIP flow • SRTP flow • RTP flow" (p332 OTC Web 架构图)
  definition: |
    远程接入加密口径：信令 SIP TLS/SIPS、媒体 SRTP（WebRTC 路径）；本地网内为明文 SIP/RTP。防火墙按
    "外密内明"规划，OTSBC 为加解密边界。
  alias_or_related: 端口见 principle p14
  tags: [protocol, security]

- id: g48
  term: OAuth 2.0
  category: protocol
  source_pages: p181
  source_quote: |
    "Support of OAuth 2.0 protocol for authentication and authorization • Administration: Google Developer
    Console Google Apps Admin Console OpenTouch ... Create once: Unique Client ID • Private Key • Google
    service account mail@"
  definition: |
    Gmail 后端的认证授权协议：Google Developer Console 一次性建 Client ID/私钥/服务账号；OT 侧每系统配
    Gmail SMTP/IMAP 服务器与服务账号，每用户关联邮箱并由 OT 请求令牌存取。
  alias_or_related: Gmail 500 用户上限见 n18
  tags: [protocol, gmail, oauth]

- id: g49
  term: DTMF
  category: protocol
  source_pages: p89, p123, p271
  source_quote: |
    "Fallback mode using DTMF" (p80)
    "Remote extension parameters DTMF code sequences can be modified, if required." (p123)
    "Example of DTMF codes: ##1: Mute or un-mute your line ... ##92: Recording conference" (p271)
  definition: |
    双音多频：三处使用——OTC Mobile 无数据时的 fallback 控制通道、RE 参数中的 DTMF 序列、会议中的角色
    控制码（##1/##3/##4/##91/##92/##93）。缩写未展开。
  alias_or_related: 会议码表见 principle p16
  tags: [protocol, dtmf]

- id: g50
  term: NOE / IP-NOE
  category: protocol
  source_pages: p232-233, p258
  source_quote: |
    "Allows the openness to all the applications developed with the NOE XML grammar" (p232)
    "Telephony services (Phone book) ... IP-NOE signaling" (p232)
  definition: |
    ALE 话机与应用间的信令/应用协议族（NOE XML 语法）：PRS 面向 NOE 兼容终端交付 Web 应用；80x8 话机的
    Home 页与 Communicate by name 走 IP-NOE。缩写未展开。
  alias_or_related: 话机应用声明见 c15 步骤 8
  tags: [protocol, noe, deskphone]

# ── 五、网站与资源名 (resource) ──

- id: g51
  term: TC2341 / TC2391 / TC2258 / TC2558 / TC1623
  category: resource
  source_pages: p147, p190, p400, p395, p436
  source_quote: |
    "Deployment Guide for OTC smartphone in Voice over IP for Connection Users, please consult TC2341" (p147)
    "consult the TC2391: New_Unified_Messaging_implementation" (p190)
    "Technical Bulletin OpenTouch TC2258 ed.02 Release 2.3.1 and above — Calendar Presence & Calendar Synchro" (p400)
    "PLEASE HAVE A LOOK TO THE TECHNICAL DOCUMENTATION 'TC 2558'" (p395)
    "TC1623 : Single Sign-On Kerberos in-deep" (p436)
  definition: |
    本书引用的五份 ALE 技术通报（Technical Communication）：TC2341=OTC 智能手机 VoIP 部署指南；
    TC2391=新统一消息实现；TC2258（ed.02，2019）=日历在场与同步（整篇附录收录）；TC2558=本地存储邮箱的
    日历特性；TC1623=Kerberos SSO 深入。生产化的权威依据。
  alias_or_related: TC2258 附录含排障命令清单（principle p46）
  tags: [resource, document, tc]

- id: g52
  term: RLAB / POD / V-Class
  category: resource
  source_pages: p3-18
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data
    center." (p5)
    "Fully Virtualized (RLAB only, no classroom equipment) / Hybrid mode (RLAB + classroom equipment)" (p3, p11)
  definition: |
    ALE 培训远程实验室：POD 池（相互独立、同构、共享 NAS 与 SIP 模拟器），全书实验环境；V-Class=虚拟课堂
    形态。所有实验口径（IP/账号/号码）均绑定此环境。
  alias_or_related: 拓扑见 framework f02；设置表见 principle p06
  tags: [resource, lab, training]

- id: g53
  term: ot-podX / conf-podX / otsbc-podX 域名模板
  category: resource
  source_pages: p104-107, p109-111
  source_quote: |
    "https://ot-podX.company.com • https://ot-podX.company.com:8016 for EVS (notifications)" (p104)
    "conf-podx.company.com<->10.20.X.105 ... conf-podx.company.com<->192.168.1.55" (p109)
    "otsbc-podx.company.com" (p106)
  definition: |
    实验口径的公共域名模板（X=POD 号）：ot-podX=OT/OTSBC 公共 FQDN（外部 DNS 10.20.1/3/5/7/9/11.105）；
    conf-podX=会议服务专用 FQDN（公网指 RP、内网指 ACS 虚拟 IP 192.168.1.55，须入证书 SAN）；otsbc-podX=
    WebRTC SBC。生产按客户域名替换。
  alias_or_related: NAT/DNS 结构见 framework f09
  tags: [resource, dns, lab]

- id: g54
  term: enterprise-education.csod.com
  category: resource
  source_pages: p468
  source_quote: |
    "Browse our catalog available on https://enterprise-education.csod.com/ to find your training path and
    course detail." (p468)
  definition: |
    ALE 培训目录站点（书尾"Find a Course"）：查询培训路径与课程详情；反馈邮箱
    emea.education-services@al-enterprise.com（BREST）。非技术资源。
  alias_or_related: 无
  tags: [resource, training]

- id: g55
  term: ALE NFC Extended Mobility (Administration) / NFC Type 2 / 3BA27856AA
  category: resource
  source_pages: p159-160, p166-167
  source_quote: |
    "'ALE NFC Extended Mobility Administration' tool • Available on the Google market (Android R4.2 at
    minimum)" (p159)
    "ALE strongly recommends to take ALE NFC tags (Ref 3BA27856AA: NFC tag stickers x100) ... if they respect
    the reference 'NFC Type 2' • Their validation must be realized in this case by the Business Partner" (p160)
  definition: |
    NFC 标签生态：管理端工具（Google 市场，Android 4.2+）写/查标签；推荐 ALE 官方标签（Ref 3BA27856AA，
    100 张装），自购标签须为 NFC Type 2 且由 BP 验证。用户端触发由 OTC Mobile 完成。
  alias_or_related: QR 语法对照 principle p41
  tags: [resource, nfc, extended-mobility]

- id: g56
  term: FreeRADIUS.net 1.0.5
  category: resource
  source_pages: p462-467
  source_quote: |
    "double-click on the 'freeRADIUS.net-1.0.5-r0.0.5.exe' file ... copy the 'clients.conf', 'radiusd.conf'
    and 'users' files" (p463, p466)
  definition: |
    实验用 Windows 版 FreeRADIUS（第三方移植）：配置三文件（radiusd.conf 定 UDP 1812、users 定用户、
    clients.conf 定 OT 服务器与共享密钥 training）。纯实验工具，生产 RADIUS 另选企业级实现。
  alias_or_related: 参数对应 OT 侧 plugin_radius.properties（principle p26）
  tags: [resource, radius, lab]

- id: g57
  term: tsa_maintenance
  category: resource
  source_pages: p55-57
  source_quote: |
    "'tsa_maintenance' script is located in '/opt/Alcatel-Lucent/infra_services/ots/'" (p55)
    "100 -------------------- MENU PROTECTED by secret code ... (2998 is the secret code value)" (p56)
  definition: |
    OT 服务器上的 nomadic/Ghost 资源维护脚本（选项 20 dump Nomadic；受保护菜单 100/秘密码 2998 → 106 2998
    进 ACAPI control → 7 加载全部对象）。实验秘密码 2998。
  alias_or_related: 用法清单见 principle p47
  tags: [resource, tool, nomadic]

- id: g58
  term: My Profile / My Messaging
  category: resource
  source_pages: p210-211
  source_quote: |
    "Run the tool by using a browser, and enter as URL the OpenTouch server FQDN" (p210)
    "Run 'My Messaging' (URL= https://OT server FQDN/MyMessaging)" (p211)
  definition: |
    OT 用户自助 Web 应用：My Profile（OT 服务器 FQDN 直达）改邮箱行为与问候语（问候语须先用话机录制）；
    My Messaging（/MyMessaging）在电脑/话机上听、转语音留言。
  alias_or_related: 问候语限制见 n22
  tags: [resource, webapp, um]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列候选术语逐条核对

说明：OVERVIEW 术语表实际为 **22 行**（自检节记 22 个）。逐条核对如下——

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| OpenTouch (server/OTMS) | 正文有明确定义/实例表 | g01 |
| Connection user / Conversation user | 有明确定义（p34/p44/p274） | g02, g03 |
| Nomadic mode | 有明确定义（p34-35/p46） | g04 |
| Ghost Z set | 有明确定义（p39/p46-47） | g05 |
| REX (Remote Extension) | 有定义性用法（p92-94/p137），全称未展开 | g06（full_name 省略） |
| DISA | 有定义性用法（p92/p121-123），全称未展开 | g07（full_name 省略） |
| Tandem (twinset) | 有明确定义（p139） | g08 |
| Desksharing (DSU/DSS) | 有明确定义（p59-61） | g09 |
| OTC (PC/Mobile/Web) | 有明确定义（p79/p323） | g10 |
| OTSBC / SBC | 有明确定义（p105-107/p332） | g27（与 g13 SBC 撞名已注） |
| ACS (Advanced Communication Server) | 有明确定义（p299） | g29 |
| DAS rules | 有明确定义（p299） | g11 |
| UDAS | 有明确定义（p220，全称展开 Universal Directory Access Service） | g12 |
| SBC (Single Business Card) | 有明确定义（p226/p252） | g13 |
| UM (Unified Messaging) | 有明确定义（p170） | g14/g32 语境；UM 词条并入相关条目（Unified Messaging 无独立 g 条，机制由 g14 Impersonation、g32 Wireal/MASC、g39 ICEaccess、g41 EWS 覆盖，来源页 p170-178） |
| ICEaccess & Impersonation | 有明确定义（p180/p189） | g39, g14 |
| APNS | 有明确定义（p97 全称展开） | g33 |
| Extended Mobility | 有明确定义（p150） | g23（成本）、g55（NFC 生态）、n16/n17/n41（行为）；机制并入 principle p41/p42（来源页 p148-167） |
| DCS (Document Conversion Server) | 有明确定义（p365） | g31 |
| Calendar presence / synchro | 有明确定义（p386-392） | g17 |
| DTA | 有明确定义（p417 "means DaTa Access"） | g16 |
| Kerberos SSO (Upstream) | 有明确定义（p427/p429） | g43 |

结论：22 行全部"本书正文有明确定义或实例化出现"，无"仅 passing 提及需排除"项；Extended Mobility 与 UM 两个主题词条的机制细节分散在 principle/framework，已在 alias 字段交叉指引。

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：Conversation user（g03）、Fallback mode（g18）、Downstream/Upstream（g15）、DTA/Alcatel User ID/External login（g16）
- 许可：Desktop、Nomadic GSM/SIP、Off site mobility、Conferencing/Voice mail/Flex Office/OT Applications、Connection user license 组（g19-g23）
- 产品：OXE（g24）、OMS（g25）、OmniVista 8770（g26）、Reverse Proxy（g28）、AMS（g30）、Wireal/MASC（g32）、kamailio-wasp/wspcfg（g34）、DCS lab VM/ECOSYSTEM（g35）、IPDSP/MicroSIP（g36）、ITSP1（g37）、PRS（g38）、ice_kerb 三件套（g40）
- 协议：EWS（g41）、LDAP/LDAPS/Radius（g42）、Kerberos 族（g43）、ARS/Discriminator（g44）、DDI/DID（g45）、SIP URI（g46）、SIP TLS/SRTP/RTP（g47）、OAuth 2.0（g48）、DTMF（g49）、NOE（g50）
- 资源：TC 五件套（g51）、RLAB/POD/V-Class（g52）、域名模板（g53）、培训站点（g54）、NFC 生态（g55）、FreeRADIUS.net（g56）、tsa_maintenance（g57）、My Profile/My Messaging（g58）

### 3. 仅 passing 提及、未单列条目的词（备查）

MLE（封面/章节名 "OpenTouch Suite for MLE"，全书未展开，附于 g01 语境）、OTMS（同上，g01 alias）、VAD/DR/IR（本书未出现）、bubble/Hub（本书未出现）、SEPLOS（p96 提及旧方案组件名，附于 n43）、My IC Phone 8082 / 8088 Smart DeskPhone（p220 UDAS 客户端列表，附于 g12）、80x8/80x8s/80x9/8001/81x8/4135（p157/p172 话机型号清单，附于 p41 语境）、MIX484 GD4 / ALE-300/20h/30h/500（p15 课堂硬件，实验基础设施）、Squirrel/DM（p57 脚本参数，无解释）、LightLine（p55 菜单备注，无解释）、netadmin -m option 17（p52，OXE 节点名来源）、Blue Coat / NGINX（p332 RP 产品示例）、TightVNC（p372/p375 DCS 安装监控工具）、S.O.T.（p373 外部 DCS 部署工具，未展开）、Certisign / VeriSign（p112 外部 CA 示例）、Skype4B / Lotus Notes（p281/p417 第三方集成/客户端）、TightVNC 之外 – ITSP2（p20 拓扑图，无细节）。

### 4. 提取口径说明

- 所有定义只采信本书正文；MLE/OMS/OTMS/DISA/DDI/REX/DTMF/TFTP/NOE/UTL（本书未出现 UTL）等缩写书中未给全称者，full_name 一律省略，不做外部补全；书内给全称者（UDAS、ACS、APNS、AMS、EWS、DSU、DSS、SBC、MASC、KDC、TGT、SPN、EWS）如实记录。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准，引用均为原文摘录；原文笔误已注明（"192.16.8.1.1" p9、"APLLIED" p108、"syhchronization" p243、"Windows 2010" p371、"completly time" p155、"Drirectory number" p167）。
- 实验 IP/账号/密码/号码均已标注"实验口径"，集中于 principle p06/p07/p45 与 case 各条 conditions。
