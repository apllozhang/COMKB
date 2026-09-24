# 原则/清单/规则/公式/数值口径候选 — Rainbow OmniPCX Enterprise (RAINXTE003EN Ed12)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: Rainbow 共 8 种订阅，定位与计费方式各不相同
  type: metric
  source_pages: p24
  source_chapter: Rainbow overview / Subscription plans
  source_quote: |
    "Rainbow Essential This free option is available to anyone who wants to try Rainbow for an unlimited
    period (no SLA). … Rainbow Enterprise Conference … is pre-paid yearly in advance (twelve months)." (p24)
    "Rainbow Conference An optional service proposed as a 'pay-as-you-go' model for phone (PSTN)
    conferencing with a price-perminute/per-connection. The organizer … can be a Rainbow Essential
    (freemium) user, or premium user" (p24)
  summary: |
    8 种订阅：Essential（免费、无限期试用、无 SLA，可与付费订阅混用）、Business（按用户）、
    Enterprise（Business 全部 + 多方视频会议 + 扩展文件存储 + O365/Google Suite 集成）、
    Attendant（话务台专用：排队呼叫列表 + 监督控制台）、Enterprise Conference（Enterprise + 无限电话
    会议分钟，按年预付 12 个月）、Conference（按分钟/按连接的 pay-as-you-go，组织者可以是免费用户）、
    Connect（CRM 连接器，按用户）、Room（按会议室，需额外硬件）。选型决策：电话/话务台看
    Business/Enterprise/Attendant；会议室用 Room；CRM 用 Connect。
  conditions: Ed12 / R101.1 时代的订阅目录；细节以 Features List（help.openrainbow.com）为准
  tags: [metric, licensing, subscription]

- id: p02
  title: 网络前提以官方 Network Requirements 文档为准，连通性与容量用 Rainbow Pilot 评估
  type: checklist
  source_pages: p27, p31, p33
  source_chapter: Network requirements / Rainbow Pilot
  source_quote: |
    "This page contains: … A summary of port/protocol requirements for: Rainbow collaboration, Rainbow
    hybrid telephony, Rainbow Hub ; 2 PDF files" (p27)
    "RAINBOW PILOT allows you to assess your Rainbow connectivity from your location, and the capacity of
    a given location to handle a population of Rainbow users characterized by a flexible mix of usages
    between Collaboration, Conferencing, Hybrid or Hub telephony." (p33)
  summary: |
    上线前动作清单：查 help.openrainbow.com 的 "Check Rainbow Network Requirements" 文章（含端口/协议
    汇总：协作、混合话音、Hub 三块 + 两份 PDF：Network Requirements、Health data hosting；含域名与 IP
    清单、带宽要求、企业网 DNS/Proxy/防火墙配置要求）；再用 pilot.openrainbow.com 按协作/会议/混合话音
    /Hub 的用户配比评估站点承载能力。
  conditions: 书中只给指针，端口与帶寽数值在书外 PDF；生产化必须取最新版文档
  tags: [checklist, network]

- id: p03
  title: 建公司前先查重；一个用户不能同时属于两家公司
  type: rule
  source_pages: p38
  source_chapter: Introducing the companies
  source_quote: |
    "Before you start a company • Check that the target company does not exist in Rainbow. • To avoid
    possible duplicates, enter the name of the future company in the search bar • A user cannot be part of
    2 different companies" (p38)
  summary: |
    两条硬规则：(1) 创建公司前必须在搜索栏查名，防止重复建司；(2) Rainbow 账号以邮箱为身份，一个人
    不能同时是两家公司的成员——规划多客户、多组织归属时要先决定唯一归属。
  conditions: 全版本通用；账号身份=邮箱地址（p95）
  tags: [rule, company]

- id: p04
  title: BP 专属权限只有两项；EC 公司与且仅与一个 BP 挂靠；集成伙伴须为 DR 或 IR
  type: rule
  source_pages: p39
  source_chapter: Introducing the companies / 2 types of companies
  source_quote: |
    "However, the following actions can only be performed by the BP: • Declaration & PBX • Opening of paid
    subscriptions • The customer's integration partner must be either a 'DR' or an 'IR'. Its name appears
    in the 'My company / Dashboard' screen." (p39)
    "To be managed by a BP, an 'EC' company must be attached to the company of this BP (one and only one
    attachment)." (p39)
  summary: |
    渠道角色分 DR（Direct Reseller）/ IR（Indirect Reseller）/ VAD（Value Added Distributor）/ EC（End
    Customer）。多数管理操作 BP 和客户管理员都能做，但只有 BP 能做两件事：申报与创建 PBX、开通付费
    订阅。EC 公司必须挂靠到某个 BP（且只能挂一家）。这决定权责切分：客户管理员发现无法建 PBX/开
    订阅时，属于正常设计而非故障。
  conditions: 需持 BP/经销商账号才能执行这两项操作
  tags: [rule, company, licensing]

- id: p05
  title: 公司可见性四级（PUBLIC/PRIVATE/CLOSED/ISOLATED）行为定义与选型建议
  type: principle
  source_pages: p43
  source_chapter: Introducing the companies / Privacy & visibility
  source_quote: |
    "PUBLIC: a user from another company can see and invite members of your company. … CLOSED : a user from
    another company cannot see the members of your company, but he can invite them via their email address.
    Your users can't see users outside their company, but they can invite them via their email address.
    ISOLATED : a user from another company cannot see the members of your company and cannot invite them." (p43)
    "Get into the habit of systematically setting the 'closed' mode as soon as you create a Rainbow company.
    This is ideal for the vast majority of customers." (p43)
  summary: |
    四级行为矩阵（外部人能否看见/邀请你 × 你的用户能否看见/邀请外部）：PUBLIC 双向可见可邀；PRIVATE
    外部看不见但可凭邮箱邀请、你的用户不受限；CLOSED 双向都看不见、但双方都能凭邮箱邀请；ISOLATED
    双向完全隔离。选型原则：拿不准就建司即设 CLOSED（适合绝大多数客户）；ISOLATED 不推荐——代价是
    用户无法被外部组织邀请进 bubble 会议。
  conditions: 可见性可在 company settings 中事后修改
  tags: [principle, visibility, company]

- id: p06
  title: 服务级别硬门槛——SSO 需 Enterprise、AAD 导入需 Voice Enterprise、频道创建需 Enterprise
  type: rule
  source_pages: p44, p96, p52
  source_chapter: SSO & Authentication / Members Creation / Information Channels
  source_quote: |
    "The administrator must have an 'Enterprise' service level" (p44)
    "Import via Azure Active Directory is reserved for administrators with 'Voice Enterprise' service level" (p96)
    "Only users with an 'Enterprise' service level can create Information Channels." (p52)
  summary: |
    三处硬门槛：配置 SSO 的管理员必须是 Enterprise 级；Azure AD 批量导入/同步只对 Voice Enterprise 级
    管理员开放；信息频道只有 Enterprise 级用户能创建。另一处相关边界：列表之外的认证方式（其他
    SAML V2/OIDC 产品如 Shibboleth/OKTA 等）须经 ALE 确认（p44 NB）。操作前先核查操作者的订阅级别，
    别让低级别管理员白折腾。
  conditions: SSO/批量导入/频道创建操作前
  tags: [rule, licensing, sso, azure-ad, channel]

- id: p07
  title: 密码策略——至少 12 位，含至少 1 个大写、1 个数字、1 个特殊字符
  type: rule
  source_pages: p97, p98, p104
  source_chapter: Members creation / Bulk import / Security password & login
  source_quote: |
    "Via the email received, users will customize their password. (At least 12 characters and contain at
    least 1 uppercase, 1 number, and 1 special character)" (p97)
    "A password must be at least 12 characters long and contain at least 1 capital letter, 1 number and 1
    special character." (p104)
  summary: |
    平台级密码复杂度统一口径：≥12 字符 + ≥1 大写 + ≥1 数字 + ≥1 特殊字符；手工创建、邀请开户、CSV
    批量导入三处同样适用（SSO 场景 CSV 的 password 字段可留空，p98）。管理员改密时若用户在线会立即
    被登出——疑似账号被冒用时的应急处置手段（p104）。
  conditions: 全平台账户密码操作
  tags: [rule, security, password]

- id: p08
  title: 成员删除有 10 天宽限期；恢复后降级 Essential 且需重配
  type: rule
  source_pages: p103, p97
  source_chapter: Members deletion
  source_quote: |
    "When you delete a user, his or her status becomes 'Suspended' for a period of 10 days (called the
    'grace period') … the user's subscription was automatically removed. If you restore it, it will default
    to 'Essential' (free) mode, so you'll need to reallocate the appropriate license … It will also be
    necessary to reassign the user's telephone line." (p103)
    "If you get an error message about the e-mail address you wish to use, please check that it is not
    already the identifier of a user deleted less than 10 days ago (grace period)." (p97)
  summary: |
    删除成员后账号进入 10 天 "Suspended" 宽限：可恢复（误删）或等 10 天永久删除；恢复后订阅已清空、
    默认 Essential，需重新分配许可并重挂话机线。反向约束：10 天内用同一邮箱新建用户会报错（邮箱仍被
    已删用户占用）——报"邮箱不可用"先查 10 天内是否删过人。
  conditions: 成员删除/恢复/同名重建场景
  tags: [rule, members, lifecycle]

- id: p09
  title: 培训环境只许 Voice MONTHLY 订阅，禁用预付（Business 与 Attendant 两处警告）
  type: checklist
  source_pages: p57, p239
  source_chapter: Subscriptions / How-To Attendant console
  source_quote: |
    "During LAB Use ONLY Voice MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID!!!" (p57)
    "DON'T USE 'PREPAID' IN THE TRAINING" (p239)
  summary: |
    实验/培训环境只允许按月（MONTHLY）订阅，Voice 与 Attendant 两处都明令禁止预付（1/3/5 年
    PREPAID），否则实验许可无法按预期调整和回收。这是培训场景规则，生产环境预付是正常计费方式。
  conditions: RLAB/虚拟课堂实验环境
  tags: [checklist, training, licensing, subscription]

- id: p10
  title: Essential 订阅只能 RCC 不能改路由；路由能力需 Business/Enterprise
  type: rule
  source_pages: p109, p129
  source_chapter: OXE users with Rainbow / Remote extensions How-To subscription management
  source_quote: |
    "Rainbow Essential license • Allows only to control your physical device via the Rainbow application
    (RCC mode = Remote Call Control) • Call routing is not possible … Rainbow Business/Enterprise licenses
    • The physical device is set in tandem with a Remote Extension (REX) • Call routing is possible" (p109)
    "With an 'Essential' subscription, the user can only use RCC feature. He cannot modify his routing. To
    have access to routing possibilities (mobile, other number, …) he must have a Business or Enterprise
    subscription." (p129)
  summary: |
    订阅决定能力上限：Essential=RCC（监督话机）仅此而已；Business/Enterprise=话机与 REX 成 tandem、
    可路由到工作手机/家庭/个人手机/其他外部号。书内同时强调 "Call Routing is not a Forwarding"——路由
    与呼叫转发是两个机制。规划用户形态时先定订阅再定预期行为。
  conditions: 无网关阶段同样成立；WebRTC 网关使用也要求 Business/Enterprise（p133）
  tags: [rule, licensing, rcc, routing]

- id: p11
  title: 每路 REX 并发呼叫需一个 Ghost Z；目录号建议用字母优化拨号计划
  type: rule
  source_pages: p122
  source_chapter: Remote extensions How-To / Ghosts creation
  source_quote: |
    "A ghost device is required per simultaneous call to a REX." (p122)
    "Directory Number Enter the directory number. E.g. DB1000. Note: It is interesting to use letter (A,B,C,D)
    in the directory number to optimize the dialing plan" (p122)
  summary: |
    Ghost Z 数量=REX 并发呼叫上限（池大小即最大并发数，通话结束释放）。Ghost 创建参数：目录号如
    DB1000（用字母 A/B/C/D 开头可与普通号码计划区隔、优化拨号）、目录名 Ghost1、机架/板卡/设备地址
    255、Set Type=Analog、不可按名呼叫；Facilities 页签勾 Ghost Z + Ghost Z Feature=Remote extension。
  conditions: 参考 TC2462；容量联动 p151 sizing 工具
  tags: [rule, rex, ghost, capacity]

- id: p12
  title: Tandem 两端必须 multi-line（≥2 线）；配置只做在主站自动同步副站
  type: rule
  source_pages: p124-125, p139
  source_chapter: Remote extensions How-To / Tandem configuration
  source_quote: |
    "Multi-lines are required on extensions part of a tandem." (p124)
    "Configuration is done on one device: the main one. It will be automatically reported on the secondary
    one." (p125)
  summary: |
    组 tandem 的前置：主站（如 31000）与副站（REX 如 2131000）各配至少 2 条 multi-line（Users/Prog.
    Keys，Key 功能 Multi-line、目录号=本机号、助记名如 L1）。tandem 声明只在主站的 Assoc. Sets 页签做
    （填副站号+勾 Main set in the tandem）。特例提醒：4059EE 关联话机必须非 multi-line（p209）——同是
    OXE 话机，场景不同要求相反，别混。
  conditions: 参考 TC2462；DECT 特例见 n 系列条目
  tags: [rule, tandem, multi-line, rex]

- id: p13
  title: 溢出三配置：主站故障溢副站、无应答溢 associate、计时器 100ms 步进
  type: checklist
  source_pages: p126-128
  source_chapter: Remote extensions How-To / Overflows configuration
  source_quote: |
    "Overflow to sec tandem if main OOS Checked … Forward if set is out of service Validated … Ring all
    its secondary if main oos Checked" (p126)
    "Overflow timer Enter the timer value (step of 100 ms). E.g. 150 for 15s … Overfl. on no answer to
    associate Validated (1) … Cancel Overfl. to associate Validated (1)" (p127)
  summary: |
    两级溢出清单：①主站失效时优先叫副站——系统参数 "Overflow to sec tandem if main OOS" 勾选 + 用户
    COS：Forward if set is out of service、Ring all its secondary if main oos、Remote Extension
    Activation/Deactivation（Activation/Deactivation 值控制用户能否自行启停 REX）；②主副都无应答时
    溢 associate（通常是留言信箱如 31499）——实体 Overflow timer（步进 100ms，150=15 秒）+ COS：Overflow
    on no answer to associate、Cancel Overflow to associate + 主设备 Associated Set No. 填 associate 号。
  conditions: 主副设备须同实体；COS 为 Phone Features COS
  tags: [checklist, overflow, rex, cos]

- id: p14
  title: 路由四案例矩阵——手机号配置决定 REX 内容与振铃终端
  type: metric
  source_pages: p116, p143
  source_chapter: Rainbow user with OXE phone and REX / Routing
  source_quote: |
    "Case 1: no mobile number set in user's profile -> Remote extension number is empty -> Only deskphone
    is ringing. Case 2: professional mobile is configured in user's profile -> REX number = professional
    mobile -> Deskphone and professional mobile are ringing. … Case 4: professional and personal mobiles
    are configured in user's profile -> REX number = professional mobile" (p116)
  summary: |
    固定决策表（选 Office phone 路由时）：Case 1 用户档案无手机号 → REX 为空、仅话机振铃；Case 2 配
    专业手机 → REX=专业手机、话机+专业手机同响；Case 3 配个人手机 → REX=个人手机、话机+个人手机同响；
    Case 4 两个都配 → REX 取专业手机、话机+专业手机同响（专业优先）。选 computer 路由时 REX 写 BBB 前
    缀 17 位 Rainbow number 走网关；选 mobile/home/other 时走公共 trunk。排障口诀：来话振铃不对，先查
    用户档案手机号字段与 REX 实际内容（remotesets 命令）。
  conditions: 路由 ≠ 呼叫转发；外部路由用 OXE 公网资源（p112）
  tags: [metric, routing, rex, matrix]

- id: p15
  title: WebRTC 网关硬前提：Business/Enterprise 订阅 + OXE ≥12.1 MD4/12.2 + PBX 先接入
  type: rule
  source_pages: p133, p135, p154
  source_chapter: WebRTC Gateway overview / Deploy How-To warning
  source_quote: |
    "Use of the WebRTC Gateway requires a BUSINESS or ENTERPRISE subscription for a member" (p133)
    "Require OXE release 12.1 MD4, 12.2 or later" (p135)
    "Warning • THE PBX MUST BE CONNECTED TO RAINBOW • USERS DECLARED IN THE RAINBOW COMPANY MUST HAVE
    THEIR OXE TELEPHONE NUMBER ASSOCIATED TO THEIR RAINBOW ACCOUNT" (p154)
  summary: |
    网关三重前提：①成员订阅 Business 或 Enterprise；②OXE 版本 12.1 MD4、12.2 或更高；③PBX 已连
    Rainbow 且用户已做分机关联（Telephony 页签选设备+分机）。三者缺一网关无意义——排障先核这三条。
  conditions: 版本号保留完整位数；RCC/Routing 阶段不要求网关
  tags: [rule, webrtc-gateway, prerequisite, version]

- id: p16
  title: OXE 侧 SIP 外部网关（Rainbow type）逐字段取值表
  type: metric
  source_pages: p181
  source_chapter: OXE configuration for WebRTC gateway use / 2.3 SIP External Gateway
  source_quote: |
    "SIP Port Number 5060 • Transport type UDP • Supervision timer 380 … Dynamic Payload type for DTMF 101
    • Gateway type Rainbow type • Trusted From header Checked (true) • Support Re-invite without SDP
    Checked (true) … Support G722 NO • Support G711 YES • Support G729 NO" (p181)
  summary: |
    网关对接的 OXE 侧参数基准（实验口径，照抄可复现）：ID 5、名 WebRTC Gateway、SIP Remote domain=网关
    IP 192.168.1.15、端口 5060/UDP、监督定时器 380、trunk group 5、SDP in 18x 不勾、最小认证 SIP None、
    Contact with IP 不勾、DTMF 动态载荷 101、Gateway type=Rainbow type、Trusted From header 勾、支持无
    SDP Re-invite 勾、CSTA U2U=NO、IP 域 0 或 -1（-1 即默认域 0）、编解码仅 G711（G722/G729 不支持）。
    生产站点改 IP 与编解码前先与网关侧能力核对。
  conditions: 实验口径；配套可信 IP 声明（2.2）与 TG（1.2）
  tags: [metric, sip, webrtc-gateway, configuration]

- id: p17
  title: 网关判别器固定口径——BBB 前缀 / Call Number 1 / Area 1 / 17 位 / schedule -1
  type: metric
  source_pages: p184-185
  source_chapter: OXE configuration for WebRTC gateway use / ARS prefix & Numbering discriminator
  source_quote: |
    "Manage the ARS prefix 'BBB' which will be used in the number automatically configured by Rainbow agent
    in the REX when 'computer' will be selected by the user for routing." (p184)
    "Call Number 1 … Area Number 1 … ARS Route List Number … 5 … Schedule number -1 (meaning default time
    based route list 1 will be used) • Number of Digits 17 (length of numbers managed by the Rainbow agent)" (p185)
  summary: |
    网关路由判别的固定五元组：ARS 前缀 BBB（Prefix Plan，挂含 Ghost Z 与用户的实体的逻辑判别器）→
    实判别器（如 5 号 "WebRTC Gateway"）→ 规则 Call Number 1 / Area Number 1 / ARS route list 号 /
    schedule -1（用默认时段路由表 1）/ 位数 17（Rainbow agent 管理的号码长度）。CDT 是 ARS 表用 SIP TG
    的前提（p182 Notes）。回程测试技巧：把 REX 里的 BBB 号设成缩位拨号，从 OXE 话机直拨验证到 Rainbow
    客户端（p188 Tips）。
  conditions: 前缀 BBB 与判别器号可按站点调整，但位数 17 与 -1 语义固定
  tags: [metric, ars, discriminator, routing, webrtc-gateway]

- id: p18
  title: 回调（Callback）三件套：CSTA 开关 + 翻译表 DEF→BBB + 专用实体
  type: checklist
  source_pages: p186-188
  source_chapter: OXE configuration for WebRTC gateway use / 4 Callback management
  source_quote: |
    "Set Callback On Calling Device Yes" (p186)
    "Basic Number DEF • No. Digits To Be Removed 0 • Digits to Add BBB" (p187)
    "The external callback translation table will be used by a specific entity (to avoid interactions with
    existing callback translation table) assigned to Rainbow Trunk Group." (p187)
  summary: |
    让 PBX 话机用通话记录回拨 Rainbow 分机的配置清单：①Applications/CSTA：Set Callback On Calling
    Device=Yes；②建外部回调翻译表（如 5 号，国家码 33 France）+ 规则：Basic Number=DEF、删除位数 0、
    追加 BBB（把号码变换成网关判别格式）；③建专用实体（如 50 号 "WebRTC Gateway"，External Callback
    Table=5）并把网关专用 SIP trunk group 挂到该实体——专用实体是为了不与存量回调翻译表互相干扰。
  conditions: 目标是"用话机 call-log 回拨 Rainbow 号"；实体与表号按站点规划
  tags: [checklist, callback, csta, webrtc-gateway]

- id: p19
  title: 网关流量上限与 406 溢出规则；参数为空则 SIP trunk 限制生效
  type: rule
  source_pages: p149
  source_chapter: Shared and scalable WebRTC gateway / ARS
  source_quote: |
    "The maximum traffic for each WebRTC is managed in the RAINBOW interface • It defines the number of
    simultaneous streams supported by the gateway. • If the traffic limit is reached, the gateway responds
    to a new request with a SIP message '406 - Not Acceptable'. • As a result, the OXE will overflow onto
    the next ARS route (WebRTC gateway). • If this parameter is empty, the SIP trunk limit will determine
    the overflow." (p149)
  summary: |
    池化溢出规则：每网关最大并发流在 Rainbow 界面（Rainbow/Communications/Equipments/编辑该 PBX）设定；
    满载时网关对新请求回 SIP 406 Not Acceptable，OXE 依 ARS 表声明顺序溢出到下一条路由；该参数留空时
    溢出由 SIP trunk 限制决定。前提：每个 OXE 节点对每个网关一条 SIP trunk/外部 SIP 网关，各节点 ARS
    管理需相似。图示示例值 400（实验口径示例）。
  conditions: 详见 TC2462；单网关硬上限 400 并发流（p151）
  tags: [rule, webrtc-gateway, pool, ars, overflow]

- id: p20
  title: 网关容量口径——单网关 400 并发流；TBE067 工具四输入推通道数与压缩器
  type: metric
  source_pages: p151
  source_chapter: Shared and scalable WebRTC gateway / SIZING
  source_quote: |
    "Available from OXE 101.0 MD3 and WebRTC 3.x • A WebRTC gateway supports up to 400 simultaneous streams." (p151)
    "An Excel tool is available in which key values must be entered • Total number of OXE users • The
    number of OXE users with a Rainbow client • The percentage of Rainbow client usage • The percentage of
    direct calls from a Rainbow client to a Rainbow client." (p151)
  summary: |
    容量三口径：①单网关上限 400 并发流（工具适用 OXE 101.0 MD3 / WebRTC 3.x 起）；②通道数由 TBE067
    Excel 工具估算，输入四值——OXE 用户总数、持 Rainbow 客户端用户数、Rainbow 客户端使用率、客户端间
    直呼占比（流量模型假设可调）；③由并发通道数再推算 OXE 压缩器数量。用户数与并发流是两个量纲，
    报容量时必须先声明口径。
  conditions: 工具本体在书外（TBE067_Rainbow - WebRTC Gateway Pres&Sizing - ed06l.zip）
  tags: [metric, sizing, capacity, formula]

- id: p21
  title: 池化选型——共享池为默认解，网关复制仅超高流量（≥5000 用户/OXE）合理
  type: principle
  source_pages: p147-148
  source_chapter: Shared and scalable WebRTC gateway / Optimization
  source_quote: |
    "Note: If traffic is high, WebRTC duplication per OXE can still be consistent. Example Number of users
    >= 5000 per OXE." (p148)
    "Note: This type of sharing, depending on the number of nodes, can make ARS management more complex.
    It is recommended to proceed by OXE cluster." (p148)
  summary: |
    两种抗灾/扩容配置的取舍原则：默认选共享 WebRTC 池（抗故障+增并发+省成本），按 OXE 集群推进以控制
    ARS 复杂度；仅当流量特别大（书中示例：每 OXE 用户数 ≥5000）时每 OXE 网关复制才划算。两种配置都
    基于 ARS overflow 机制（Load Sharing via OXE）。OXE 网络（多节点）架构同样支持网关池化。
  conditions: 每 OXE 每网关一条 SIP trunk 是共享池的硬要求（p149）
  tags: [principle, webrtc-gateway, pool, ha, sizing]

- id: p22
  title: 监督组规格——监督员 ≤5 组、每组 ≤30 人；队列 OXE 10/OXO 8；互助组监督 4 路
  type: metric
  source_pages: p227, p230, p232, p235
  source_chapter: Rainbow Attendant Console & Mutual aid supervision groups - Overview
  source_quote: |
    "Call queue management - Manage up to 10 calls for OXE - And up to 8 calls for OXO Connect" (p227)
    "Maximum number of supervision groups for a supervisor / Maximum number of users in a group
    (supervisors + supervised): 5 / 30" (p230)
    "Up to 4 calls supervised" (p235)
  summary: |
    监督/话务四组硬数字：①呼叫队列 OXE 10 路、OXO Connect 8 路；②监督员最多 5 个监督组；③每组（监督
    员+被监督合计）最多 30 人；④互助组同时最多监督 4 路呼叫。挂起呼叫数取决于话务员软电话线的
    multi-line 资源：OXE 用 REX 最多 10、OXO 用 Anydevice（最低 R6）最多 8。所有电话呼叫由 PBX 处理。
  conditions: Attendant 订阅每人必需；话务台功能仅 PC 端（thick client/web）
  tags: [metric, attendant, supervision, capacity]

- id: p23
  title: 互助组代接边界——仅限同 PBX 的电话呼叫，Rainbow 软终端呼叫不可代接
  type: rule
  source_pages: p234, p232
  source_chapter: Mutual aid supervision group / Miscellaneous
  source_quote: |
    "As supervisor, you will be notified of telephone calls intended for supervised users. • You can pickup
    calls. Works only for PBX calls, not for Rainbow softphone calls" (p234)
    "Interception is only possible if supervisors and supervisees are on the same PBX. Only phone calls can
    be intercepted." (p232)
  summary: |
    代接/拦截两条边界：①只对 PBX 电话呼叫有效，Rainbow 软终端（computer 路由）来的呼叫不能代接；
    ②监督员与被监督者必须在同一 PBX。附加行为：一键 Join/Leave、监督员可临时纳入/排除被监督用户
    （用户离开忘了进组的补救）、可锁定最后一名成员不可退出。
  conditions: 组类型（Mutual aid group）与双方 In/Out 权限在创建时定义
  tags: [rule, mutual-aid, pickup, boundary]

- id: p24
  title: 4059EE 硬约束——只管话务不管话音；关联话机必须非 multi-line；Rainbow 在场≠电话在场
  type: rule
  source_pages: p209, p204, p221
  source_chapter: Call distribution and attendants How-To / 4059EE overview
  source_quote: |
    "The 4059 EE handles the specific functions of the attendant but not the voice. It is mandatory to
    associate a physical set (ALE series) or an IP Desktop Softphone." (p209)
    "WARNING: This extension must not be multi-line, as it will be associated to the 4059 IP attendant
    (multiline set is incompatible with 4059 IP attendant)" (p209)
    "Warning - Rainbow and phone status are two distinct things and can be different" (p204)
  summary: |
    三条 4059EE 硬约束：①4059EE 处理话务专项功能但不处理话音，必须关联一部物理话机（ALE 系列）或
    IPDSP（属性 "Associated phone set"），且 IPDSP 须先 in service 再从 4059EE 连接；②关联话机不能是
    multi-line（与 4059 IP 话务台不兼容——与 tandem 场景 p124 的 multi-line 要求正好相反）；③Rainbow
    在场状态与电话状态是两个独立信息，BLF 监督时两边可不同（书中设计了两条验证测试确认这一点）。
    另：Attendant 订阅只用于 Rainbow 内嵌话务台、与 4059EE 无关（p200）。
  conditions: 4059 系统参数两项（Close auto sign off / PC unregistered at logoff）语义见 c10
  tags: [rule, 4059ee, attendant, presence]

- id: p25
  title: Teams 集成三约束——工作站级、Desktop 硬依赖、权限收敛 Telephony
  type: checklist
  source_pages: p259, p271-272, p297, p302
  source_chapter: INTEGRATION WITH MICROSOFT TEAMS / user configuration How-To
  source_quote: |
    "The integration is done at the workstation level" (p259)
    "Rainbow desktop application is required and must be running" (p272)
    "it is better to apply a restrictive permission to users with Teams integration in order to forbid
    collaboration services from Rainbow … Select the required permission: Here 'Telephony'" (p297)
    "THE RAINBOW APPLICATION INTEGRATED INTO TEAMS REQUIRES THE INSTALLATION AND STARTUP OF THE RAINBOW
    DESKTOP APPLICATION ON THE PC." (p302)
  summary: |
    Teams 集成交付清单：①集成在工作站级（非租户级），逐用户配置；②Rainbow Desktop 必须安装且运行
    （缺它 Teams 内应用显示 "!" 图标）；③权限收敛：Rainbow 侧只授 Telephony 权限，协作服务交 Teams
    原生；④订阅必须 Business 或 Enterprise；⑤在场同步要单独激活（与 Office 365 共享信息），激活前
    两侧在场不一致属预期；⑥SSO 非连接器必需（p304 Important）。
  conditions: Teams 租户侧策略（应用权限策略/紧急呼叫/直接路由）在书外
  tags: [checklist, teams, integration, permissions]

- id: p26
  title: Rainbow agent 维护四抓手——incvisu 链路 / 重启 / 配置核查 / 日志
  type: checklist
  source_pages: p87-88
  source_chapter: OXE connection with Rainbow / 2 Maintenance
  source_quote: |
    "Use 'invisu' command … 4503=rainbowagent: WebSocket (rainbowagent<->Rainbow) in service … 4509=CSTA
    link (CSTA server<->Rainbow) in service" (p87)
    "(1)csa> dhs3_init -R RAINBOWAGENT … (1)csa> checkCloudConfig.sh -rainbow … (1)csa> more
    /var/log/rainbowagent.log" (p87-88)
  summary: |
    OXE 侧 Rainbow Agent 排障四抓手：①incvisu 看启动事件——五条链路事件码 4503 WebSocket / 4505 XMPP /
    4509 CSTA / 4507 Config / 4511 API_MGT 应全部 in service；②重启 agent：mtcl 账户执行 dhs3_init -R
    RAINBOWAGENT；③配置核查：checkCloudConfig.sh -rainbow（测 CCI 域名端口 openrainbow.com:443 与
    netadmin 代理）；④日志：/var/log/rainbowagent.log。接入排障顺序：先网络前提（nslookup/curl），再
    四抓手。
  conditions: mtcl 为 OXE 维护账户（实验口径）；日志示例版本 rainbowagent 6.0.1（书中样例值）
  tags: [checklist, rainbow-agent, maintenance, troubleshooting]

- id: p27
  title: WebRTC 网关排障清单——mpcheck 八段输出 + 三服务重启
  type: checklist
  source_pages: p160, p162
  source_chapter: Deploy WebRTC gateway How-To / 6 Troubleshooting
  source_quote: |
    "mpcheck … Network settings … Rainbow settings … DNS test openrainbow.com … Rainbow connect … Rainbow
    TLS check … STUN/TURN test will be done using GEOIP config … PBX_DOMAIN access … PBX_DOMAIN SIP OPTIONS
    … registration access" (p160)
    "3 services can be checked: otlitemediapillargateway • janus-gateway-mediapillar • kamailio … sudo
    service … status / restart" (p162)
  summary: |
    网关侧排障清单：①mpcheck 八段——Network settings、Rainbow settings、DNS test openrainbow.com、
    Rainbow connect（多 IP 逐个测）、Rainbow TLS check、STUN/TURN（GEOIP）、PBX_DOMAIN access（ping）、
    PBX_DOMAIN SIP OPTIONS（siptest -S -a<OXE> -d5060）+ registration access（traceroute）；注意 GEOIP
    文件缺失时 STUN/TURN 段显示 [FAILED]，先确认 Rainbow connect 段 OK（书中实验输出即如此，非必故障）；
    ②三服务状态/重启：otlitemediapillargateway、janus-gateway-mediapillar、kamailio（sudo service …
    status/restart）；③mpshow 看版本与全量配置（WRTRANGE 20000-29999 / SIPRANGE 30000-39999 /
    TURN_SERVER=GEOIP / RINGINGAUTO=true 为默认输出）；④更多维护信息在 VoIP calling Troubleshooting
    guide 与 TC2462（p194）。
  conditions: 网关账号 rainbow/Rainbow123 为实验口径；OXE 侧配套 sipextgw/lookars/traced 见 c09
  tags: [checklist, webrtc-gateway, maintenance, troubleshooting, mpcheck]

- id: p28
  title: SR 开通门槛与字段清单——仅认证伙伴可建；MyPortal 两页字段
  type: checklist
  source_pages: p254-256
  source_chapter: Maintenance / Open a service request
  source_quote: |
    "The ESR will only be created if the partner is certified on Rainbow" (p254)
    "SR category= Rainbow • SR type = product support • Severity • Subject • Mail + Description … End
    Customer Company Name • Product Category = Rainbow • Rainbow Version • Details • Subcategory • Rainbow
    SIP trunk • How found (Origin): Customer site, Beta, demo… • Customer Internal Ref" (p255-256)
  summary: |
    报障两条纪律：①入口是 support@openrainbow.com / Emily BOT / Global Welcome Center
    （ALE.WelcomeCenter@al-enterprise.com）/ 电话，但 ESR 只为持 Rainbow 认证的伙伴创建——没认证先补
    认证；②MyPortal（Support > Service Request > Create SR）两页字段要一次填全：category=Rainbow、
    type=product support、severity、subject、邮箱+描述、最终客户公司名、product category=Rainbow、
    Rainbow 版本、details、subcategory、Rainbow SIP trunk、how found（Customer site/Beta/demo…）、客户
    内部参考号。字段缺失会拖慢分派。
  conditions: MyPortal 账号需伙伴资质；描述里附 rainbowagent.log/mpcheck 输出可加速定位（工程经验）
  tags: [checklist, sr, support, myportal]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 19 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 网络前提与 Pilot | 有 → p02 |
| task-02 公司体系 | 有 → p03/p04/p05 |
| task-03 管理员权责/目录/频道 | 有 → p06（服务级别门槛） |
| task-04 订阅开通与分配 | 有 → p01（体系）、p09（实验口径） |
| task-05 RLAB/OXE 实验环境 | 无 principle 条。属环境给定值，见 case c02 与 framework f02/f03 |
| task-06 DNS/代理配置 | 无独立 principle 条。操作见 case c03；其"仅 agent 使用"边界入 n 系列 |
| task-07 OXE 接入 | 有 → p26（维护四抓手） |
| task-08 成员管理 | 有 → p07（密码策略）、p08（宽限期） |
| task-09 分机关联与 RCC | 有 → p10（Essential=RCC 规则） |
| task-10 用户形态决策 | 有 → p10、p14（路由四案例） |
| task-11 远程延伸配置 | 有 → p11（Ghost Z）、p12（tandem/multi-line）、p13（溢出） |
| task-12 网关部署 | 有 → p15（三重前提）、p27（排障清单） |
| task-13 网关升级 | 无 principle 条。操作序列见 case c08 |
| task-14 OXE 网关配置 | 有 → p16（SIP 网关取值表）、p17（判别器五元组）、p18（回调三件套） |
| task-15 共享池与容量 | 有 → p19（406 溢出）、p20（容量口径）、p21（池化选型） |
| task-16 4059EE 话务台 | 有 → p24（硬约束） |
| task-17 Attendant/互助组 | 有 → p22（规格数字）、p23（代接边界） |
| task-18 维护体系 | 有 → p28（SR 门槛与字段） |
| task-19 Teams 集成 | 有 → p25（三约束清单） |

**统计**：28 条（principle 4 / checklist 8 / rule 12 / metric 4）；19 项任务中 16 项有原则类条目覆盖，task-05/06/13 属操作序列型（case 覆盖）。
