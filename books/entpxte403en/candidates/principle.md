# 原则/清单/规则/公式/数值口径候选 — OmniPCX Enterprise SIP (ENTPXTE403EN R101.1 MD4 Ed12)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，实验环境给定值（IP、密码、账号、分机号）均标注"实验口径"，生产化需替换。数字均逐格对照原文。

```yaml
- id: p01
  title: SIP 协议基础规格——RFC 3261、TCP/UDP、IPv4/v6、应用层、TLS 可选
  type: metric
  source_pages: p45, p48
  source_chapter: SIP FUNCTIONALITY OVERVIEW / Introduction
  source_quote: |
    "SIP: Session Initiation Protocol • Protocol TCP/IP • TCP or UDP • IPv4 or IPv6 • IETF Standard:
    RFC 3261 • Application layer • Role • Establish, maintain, modify and terminate multimedia
    sessions • Voice • Video" (p45)
    "SIP is only in charge of initiating a dialog between interlocutors and of negotiating
    communication parameters, particularly those concerning the media involved (audio, video) ...
    Media characteristics are described by the SDP" (p48)
  summary: |
    口径五条：传输可用 TCP 或 UDP；网络可用 IPv4 或 IPv6；标准为 IETF RFC 3261；位于应用层；职责
    是建立/维持/修改/终止多媒体会话（语音、视频），只做媒体协商（编解码）不做媒体传输，媒体特征由
    SDP 描述（RTP 端口、RTCP 端口、音视频编解码），信令可用 TLS 保护。
  conditions: 全版本通用
  tags: [metric, sip, rfc3261]

- id: p02
  title: SIP 响应码速查表——1xx~6xx 及书中点名的具体码
  type: checklist
  source_pages: p50
  source_chapter: SIP PRINCIPLE / SIP Messages (Answers)
  source_quote: |
    "1xx Informational (transaction in progress). Trying(100),Ringing(180),… 2xx Success ... Ok(200)
    3xx Forward ... 4xx Client Failure Responses Bad request (400), Forbidden(403),Not found(404),
    Not acceptable(406), Busy here(488),… 5xx Server Failure Responses Server Internal error(500),
    Bad gateway(502),Service unavailable(503),.. 6xx Global Failure Responses Busy Everywhere(600),
    Decline(603)" (p50)
  summary: |
    六类响应：1xx 临时（100 Trying、180 Ringing）；2xx 成功（200 OK）；3xx 转发/重定向；4xx 客户端
    失败（400、403、404、406、488）；5xx 服务器失败（500、502、503）；6xx 全局失败（600、603）。
    全书排障高频码：403（一号多机互斥、认证失败）、488（法线不匹配拒媒体）、401（DM 配置文件待认证）。
  conditions: 无版本前提
  tags: [checklist, sip, response-codes]

- id: p03
  title: SIP 产品软件锁三件——177/345/430 分别管用户/扩展/软终端
  type: metric
  source_pages: p67
  source_chapter: SIP USERS / Introduction
  source_quote: |
    "3 software locks for the SIP users • 177: defines the number of SIP users (device and extension)
    • 345: defines only the number of SIP extensions • 430: defines the number of SIP softphones
    (ALE-S)" (p67)
  summary: |
    三把软件锁：177 计 SIP 用户总数（SIP Device 与 SIP Extension 合计）；345 只计 SEPLOS（SIP
    Extension）数量；430 只计 SIP 软终端（ALE-S）数量。容量报价与开通核查按此三分账。
  conditions: 具体可配数量取决于站点许可
  tags: [metric, licensing, locks]

- id: p04
  title: OXE 用户容量上限表——IP/TDM/模拟/S0/REX/SIP 六维 + 15000 用户/20000 设备
  type: metric
  source_pages: p68
  source_chapter: SIP PRODUCT LIMIT / Users number
  source_quote: |
    "IP Max = 15000 Include IP user + IPDSP + Fictive users / TDM Max = 5000 / Analogique Max = 5000 /
    S0 Max = 1000 / Remote Extension Max = 9000 / SIP Max = 15000 ... Maximum 15000 Users (Single
    device, or Main of multi devices) Maximum 20000 devices" (p68)
  summary: |
    逐项上限：IP 用户 15000（含 IP 用户+IPDSP+虚拟用户）；TDM 5000；模拟 5000；S0 1000；远程分机
    （Remote Extension）9000；SIP 15000。总量口径：最多 15000 用户（单设备或多终端的主设备）、最多
    20000 设备；图中另有一处 "Maximum 5000" 标注（其在原图中归属对象无法从文本层完全辨认，照录备查）。
  conditions: 上限随许可与硬件代次可能变化，生产以 CC 许可文件为准
  tags: [metric, capacity, limits]

- id: p05
  title: 私有 SIP 中继组容量公式——2 接入=62 通道；上限 992 TS（32×31）；MINI SIP 2=4
  type: metric
  source_pages: p86, p363
  source_chapter: Private SIP Trunk Group / SIP trunk groups status
  source_quote: |
    "SIP Access number: up to 992 TS per SIP TG (maximum 32 virtual accesses * 31 TS) They must be
    allocated by pair (2, 4, …..) Used to define the number of simultaneous SIP communications
    2 accesses = 62 communications" (p86)
    "Trunk Group type SIP: 2 accesses provide 62 channels Trunk Group type MINI SIP: 2 accesses
    provide 4 channels" (p363)
  summary: |
    换算公式：SIP 型中继组 2 个虚拟接入 = 62 路并发通信；单组上限 992 TS（32 接入 × 31 TS）；接入
    必须成对分配（2、4、…）。MINI SIP 型 2 接入仅 4 通道。中继组 TS 只是信令层面的占位，SIP 流量
    并不真占 TS（p86 notes：SEPLOS 呼叫不占 TS，SIP Device 呼叫占）。
  conditions: 修改接入数必须重启系统才生效（另见 counter-example）
  tags: [metric, capacity, trunk-group, formula]

- id: p06
  title: 本地 SIP 网关标准参数口径——端口 5060/5061/6261、订阅时长、会话计时器、SDP in 18x、CAC
  type: metric
  source_pages: p86-87, p91
  source_chapter: Local SIP gateway
  source_quote: |
    "SIP Proxy Port Number 5060 ... SIP Subscribe Min Duration 1800 ... SIP Subscribe Max Duration
    86400 ... Session Timer 1800 Min Session Timer 900 Session Timer Method + UPDATE ... SDP in 18x
    True CAC SIP-SIP False" (p86)
    "TLS Port Number : 5061 MTLS Port Number : 6261 ... Payload : 101 Support G722 : 1 Overflow
    license Threshold : 80" (p91)
  summary: |
    标准值逐格：代理端口 5060（非标客户端才改）；TLS 5061；MTLS 6261；订阅最短 1800s（30 分钟）/
    最长 86400s（24 小时）（约束通知、转移等订阅服务的时长）；会话计时器 1800s（CS 发 Keep alive 的
    周期），最小可接受 900s（可配范围 90s~86400s），方法默认 UPDATE（可改 RE-INVITE）；SDP in 18x
    默认 True；CAC SIP-SIP 默认 False；DTMF payload 101；G722 支持开；许可溢出门限 80。DNS 本地域名
    用于判定来话归属（同域查注册库，异域走 DNS 解析）。
  conditions: 初始超时/T2/TLS 计时器等默认值勿动，除非研发或支持指定（p87 note）
  tags: [metric, sip-gateway, parameters]

- id: p07
  title: SIP 代理防隔离与隔离参数——框架 3 秒/50 条、隔离 1800 秒、降级模式 TTL 1800
  type: metric
  source_pages: p87-88
  source_chapter: SIP Proxy
  source_quote: |
    "Framework Period 3 Framework Nb Message By Period 50 Framework Quarantine Period 1800 ...
    Degraded mode Time To Live 1800 ... If set to 0, when OXE moves to degraded mode, the restart of
    sipmotor process is immediate. Otherwise ... depends on the value of this timer (until
    7200s/default: 1800)" (p87)
    "A SIP equipment that sends more than 50 messages in 3 seconds is automatically added in this
    dynamic list. It stays in the list 30' (according to the value of the quarantine parameters
    defined in the proxy)" (p88)
  source_quote_note: 自动隔离数值另见 p227/p251 notes（ALES 章复述）
  summary: |
    三组数字：①隔离触发——3 秒内 >50 条消息（即 Framework period 3s × Nb message 50 条）自动进隔离
    名单，滞留 1800s（30 分钟），期间报文直接丢弃；②降级模式 TTL 默认 1800s（0=立即重启 sipmotor，
    上限 7200s）；③代理计时器默认：SIP initial time-out 500、T2 4000、DNS Timer overflow 5000、
    Timer TLS 30、INVITE 重传 3 次。ALES 部署必须把 Framework 两参数配好（3s/50）以免软终端被误隔离。
  conditions: 递归搜索（Recursive search）参数"暂未使用"
  tags: [metric, proxy, quarantine, dos]

- id: p08
  title: SIP 注册器租期边界——最短 1800 秒（30 分钟）/最长 86400 秒（24 小时）
  type: metric
  source_pages: p88
  source_chapter: SIP Registrar
  source_quote: |
    "SIP Min Expiration Date 1800 SIP Max Expiration Date 86400 ... SIP Min Expiration Date : 30Min
    by default SIP Max Expiration Date: 24H by default. These parameters define the registration time
    limits of the sip users on the registrar database" (p88)
  summary: |
    注册租期上下限：最短 1800 秒（30 分钟）、最长 86400 秒（24 小时），即终端 REGISTER 请求里的
    Expires 值被钳制在该区间（教材原理页示例 3600s=1 小时合法）。注册到期未续或注销则终端 out of
    service、注册库 IP 置 0.0.0.0（p80）。
  conditions: 与 SIP 订阅时长（p06 的 Subscribe Min/Max）是两套独立参数
  tags: [metric, registrar, expires]

- id: p09
  title: SEPLOS（SIP Extension）限制清单——九种"不能当"与依赖终端本体的功能
  type: checklist
  source_pages: p72, p74
  source_chapter: SEPLOS MODE / Features & Phone classes of service
  source_quote: |
    "Restrictions • A SIP set can't be declared as: Boss/secretary set • Night forwarding set •
    Attendant • Attendant assistant • Alarm set" (p72)
    "If the terminal is not compatible with the 'Message' method (answer message '405: method not
    allowed') ... it may be required to de-activate this feature for a better display" (p74)
  summary: |
    两条清单：①不能声明为——老板/秘书组、夜间呼转组、话务员、话务员助理、告警话机；②依赖终端应用
    本体、OXE 管不到的——重拨列表、按名呼叫、高级功能、可编程键、话机监督、多终端、酒店（8008 房间
    话机）、CSTA 监督、代接组、寻线组、CCD 坐席（ALES on PC）。另：CS 信息显示走 SIP MESSAGE，
    终端不支持时会回 405 method not allowed，需按机型关闭该特性（UTF-8/CS information 参数）。
  conditions: 详细功能等级以 OXE Features List 为准
  tags: [checklist, seplos, restrictions]

- id: p10
  title: SIP Device 限制清单——五不带（前缀后缀/酒店/CSTA/坐席/组）
  type: checklist
  source_pages: p78
  source_chapter: SIP DEVICE MODE / Restrictions
  source_quote: |
    "Cannot use prefixes/suffixes to activate PCX phone services • Cannot be a 'hotel' set • Cannot
    be supervised by CSTA (therefore, one cannot use the Computer Telephony Integration (CTI)
    mechanisms of the PCX) • Cannot be a call center agent • SIP set cannot belong to • A group of
    sets • A pick-up group • A Manager/Assistant configuration" (p78)
  summary: |
    五条硬限制：不能用前缀/后缀激活 PCX 业务；不能当酒店话机；不能被 CSTA 监督（即用不了 PCX 的
    CTI 机制）；不能当呼叫中心坐席；不能加入任何话机组/代接组/经理-助理配置。可用能力：进出呼叫、
    咨询呼叫、会议、转移、留言通知（依终端能力）、专用闭锁、账户票据、信箱、视频呼叫。
  conditions: 开通前提=子网+中继组+本地网关（结构性要求）
  tags: [checklist, sip-device, restrictions]

- id: p11
  title: ALE 话机功能矩阵（SIP 模式）——ALE-2/3 与 ALE-30/ALE-x00 两张表逐格
  type: metric
  source_pages: p99, p104
  source_chapter: ALE-2/ALE-3 DESKPHONES & ESSENTIAL & ENTERPRISE — Compatibilities and features
  source_quote: |
    "Features in SIP mode ALE-2 ALE-3 Local call logs 1000 ✓ ... Programmable keys 8 12 SIP+
    Supervision & Call Pickup  (supervisor role)  (supervisor role) SIP+ Hunting group ✓ (*) ✓ (*)"
    (p99)
    "Features ALE-30 ALE-X00 ... Local contact management 100 ... Programmable keys 120 SIP+
    Supervision & Call Pickup ✓ SIP+ Hunting group ✓ (*)" (p104)
  summary: |
    两表逐格：ALE-2——本地呼叫日志 1000 条、无视频、可编程键 8、监督/代接仅监督员角色、寻线组支持
    但降级（仅进出组与来电显示）；ALE-3——同表但可编程键 12、本地日志 ✓（表中数值列标注为 1000 与 ✓
    的具体分布以原文两列为准）。ALE-30/ALE-x00——视频呼叫列在 ALE-x00 为 ✓（表中以空白/✓ 区分）、
    本地联系人 100、可编程键 120、监督与代接 ✓、寻线组 ✓(*) 同样降级。(*) 含义=支持但服务降级
    （组进出、呼叫显示）。公共口径：Business 模式（无话务员/坐席/酒店）、支持 OXE 冗余（含空间）与/
    或 PCS、OXE DM 与 8770 DM 兼容；ALE-2/3 与 ALE-30/x00 原生加密（SIP TLS、SRTP）。
  conditions: "✓/空白"两列矩阵在纯文本层有并列歧义，引用时以原文双列为准；ALE-2/3 无视频
  tags: [metric, terminals, feature-matrix]

- id: p12
  title: SIP 模式相对 NOE 模式不支持清单——按机型分层
  type: checklist
  source_pages: p105, p121
  source_chapter: Not supported features compared to NOE mode / ALE SOFTPHONE – FEATURES NOT SUPPORTED
  source_quote: |
    "Not supported feature on Essential Business range (ALE-30) • Remote connection through VPN client
    • Interface customization (through skinify) • Common features • Hotel mode • Manager assistant •
    Multi-Line appearance (MLA) • Not supported feature on Enterprise Business range • Audio Hub •
    Remote connection through VPN client • Interface customization (through skinify)" (p105)
    "Hotel mode • Manager assistant • Multi-Line appearance (MLA) • Deployment in a client virtualized
    environment – VDI or RDS" (p121)
  summary: |
    清单：ALE-30 不支持 VPN 客户端远程与 skinify 界面定制；ALE-x00 额外不支持 Audio Hub（VPN 与
    skinify 同缺）；ALE-30 与 x00 共同不支持酒店模式、话务员助理（Manager assistant）、多线呈现 MLA。
    ALES 软终端不支持：酒店、话务员助理、MLA、客户端虚拟化环境部署（VDI 或 RDS）。
  conditions: 以 OXE Features List 为最终口径
  tags: [checklist, limitations, terminals, ales]

- id: p13
  title: ALES 内部认证密码强化规则——14 位/2 字符含 1 大写/2 数字/1 特殊/禁 4 连/前 5 不重复
  type: rule
  source_pages: p114
  source_chapter: ALE SOFTPHONE – INTERNAL AUTHENTICATION / Password hardening rules
  source_quote: |
    "14 characters minimum with - at least 2 characters (1 upper case mandatory) - at least 2 digits
    - at least 1 special character amongst ~!@#$%^&*()_+=`{}|[]\:\";'<>?,./ • Must not contain 4 or
    more consecutive or identical characters • Must be different from the last 5 used passwords."
    (p114)
  summary: |
    六条硬规则（密码质量检查由 Nginx 执行）：长度 ≥14；至少 2 个字母（其中 1 个大写强制）；至少 2 个
    数字；至少 1 个特殊字符（集合 ~!@#$%^&*()_+=`{}|[]\:";'<>?,./）；不得含 4 个及以上连续或相同
    字符；不得与前 5 次用过的密码重复。内部认证密码加密后存于 OXE 本地专用文件——不入 MAO 数据库、
    不入 remanents，双机冗余时动态同步，并纳入备份/恢复（p113）。
  conditions: 外部 LDAP 认证时 OXE 侧密码字段不要求；切本地须给每个用户配密码
  tags: [rule, security, password, ales]

- id: p14
  title: 一号多机规则——同型互斥/跨型并存/force 抢占/通话中禁抢
  type: rule
  source_pages: p115-117
  source_chapter: ALE SOFTPHONE – USE SAME LOGIN ON DIFFERENT DEVICE
  source_quote: |
    "When a user attempts to log in while being already logged on the same type of device (PC or
    smartphone), he is prompted to confirm or cancel the login action • There is no impact if the
    user is already logged but on another type of device" (p115)
    "Any SIP message (different than REGISTER) from this Directory Number with a different ALES-DUID
    is rejected" (p115)
  summary: |
    四条规则：①互斥只发生在同型设备之间（PC 与 PC、手机与手机），跨型（PC 已登录再登 iPhone）无影响；
    ②被顶设备的一切非 REGISTER 请求都被 403 Forbidden + Warning 399 Multiple Logins 拒绝；③新设备
    端弹确认框，确认后以 force 属性重注册接管，旧设备被登出；④旧设备呼叫进行中，新设备登录即使带
    force 也被拒。机制载体是 RFC4122 的 ALES-DUID，随每条 SIP 请求携带。
  conditions: 仅 ALES 软终端适用
  tags: [rule, ales-duid, multi-login]

- id: p15
  title: 监督容量与事件码——30000 键/节点、40 键/监督员、事件 510~513
  type: metric
  source_pages: p130, p133
  source_chapter: SET SUPERVISION AND CALL PICK UP
  source_quote: |
    "Limit is 30000 supervision keys on one OXE node. A supervisor can have up to 40 supervision
    keys. Supervision is not available on ALE SoftPhone on iPhone." (p130)
    "In service incident: 511 for ALE deskphone or 3rd-party device and 513 for ALE softphone ...
    Out of service incident: 510 for ALE deskphone or 3rd-party device and 512 for ALE softphone"
    (p133)
  summary: |
    数值口径：每 OXE 节点最多 30000 个监督键；每监督员最多 40 个监督键；iPhone 端无监督。Keep Alive
    超时事件码：入服事件 511（ALE 话机/第三方设备）/513（ALES 软终端）；离服事件 510（话机/第三方）/
    512（ALES）。监督四态：available、ringing、busy、out of service。来话 toast+专属铃声仅 Windows
    PC 与 Android，多被监督人同振只弹最新一条。
  conditions: 仅 SIP 设备能被另一台 SIP 设备监督
  tags: [metric, supervision, incidents]

- id: p16
  title: 按名呼叫（OXE 电话簿）能力口径——48 条结果/16 并发请求/三字段/ALES 专属
  type: metric
  source_pages: p125
  source_chapter: DIRECTORY SEARCH – ACCESS TO OXE PHONE BOOK
  source_quote: |
    "Search based on last name (e.g. 'SM' for John Smith) or initials (e.g. 'J S' for John Smith) •
    Up to 48 entries are returned per search • The returned contact attributes are limited to first
    name, last name and directory number • Maximum 16 simultaneous requests can be handled by the
    call-by-name service" (p125)
  summary: |
    口径：检索姓氏缩写（SM）或姓名首字母（J S）；每次搜索最多返回 48 条；返回属性仅 名/姓/分机号
    三项；服务最多同时处理 16 个请求。适用边界：仅 ALES（PC/移动）；不可用于远程工作者（经 SBC/
    反代）；支持 OXE 冗余但 PCS 模式不可用；Enterprise/Essential SIP 话机后续版本才加。
  conditions: 无本地 LDAP 服务器且需集中目录时的替代方案
  tags: [metric, directory, call-by-name]

- id: p17
  title: 可编程键口径——120 键 5 页×24、OXE 管键 #3~122、设备级 SIP Key 只能删不能改
  type: rule
  source_pages: p102, p103, p126
  source_chapter: Programmable keys / Centralization storage of SIP programmable keys
  source_quote: |
    "120 programmable keys organized in 5 pages of 24 keys" (p102)
    "Function of programmed keys ('SIP Key'), managed at device level, cannot be modified by the OXE
    administrator, but only deleted" (p103)
    "Concerns keys #3 to #122, as the first two keys are reserved for multiline function • Exception:
    only 8 keys on ALE-2 & 12 keys on ALE-3 can be defined in OXE Device Management (keys 1 & 2
    reserved for multiline function)" (p126)
  summary: |
    规则四条：①ALES/ALE-30/ALE-x00 最多 120 键（5 页 × 24）；②键 #1/#2 保留给 multiline，OXE 集中
    管理覆盖 #3~#122；③用户在终端上自配的 "SIP Key"（设备级）管理员不能改只能删；④特例——ALE-2 仅
    8 键、ALE-3 仅 12 键可进 OXE DM。多终端用户的按键经 SIP 配置文件同步（NOTIFY 通知取新文件）；
    ALE-2/3 与酒店话机暂不支持集中存储。编程途径两条：管理员经 DM，或用户在话机本地。
  conditions: 集中存储仅 Enterprise/Essential 话机 Business 模式
  tags: [rule, programmable-keys, dm]

- id: p18
  title: 寻线组行为规则——组呼叫不可转移、呼转/DND 不参与分配、离服不分配、前缀 480/481
  type: rule
  source_pages: p138-141, p239
  source_chapter: HUNTING GROUPS
  source_quote: |
    "Transfer the call is not possible on a group call. • Forward and Do Not Disturb are not
    considered in call distribution. • Out of service devices ... are not considered in call
    distribution but stay logged in the group." (p138)
    "Logon/Logoff using ALE-S GUI and prefixes (480 and 481 by default; their use is to be authorised
    in the users' phone features COS)" (p239)
  summary: |
    五条规则：①组呼叫不能转移；②呼转与 DND 不参与呼叫分配逻辑；③离服设备（ALES 未连、PC 待眠等）
    不参与分配但保留组内登录状态；④基础话机（ALE-2/3、8008）进出组走前缀，默认 480（进）/481（出），
    须在用户 Phone features COS 里授权；⑤混合规则——顺序/循环组可 SIP/NOE 混装且多终端可入，
    并行组不可混装且多终端不可入（首成员类型定调）。tandem 主机进出组会在全部副机上通知并可在任一副
    机操作。
  conditions: 480/481 为系统默认前缀，实际以编号计划为准
  tags: [rule, hunting-group, prefixes]

- id: p19
  title: DM profile 数量与分治规则——默认 0、上限 100、ALE-S/8008 一份、ALE-x 两份
  type: rule
  source_pages: p152
  source_chapter: DM PROFILE
  source_quote: |
    "ALE-S and 8008 are able to manage local and remote worker with the same profile • ALE-x devices
    need two profiles • Local worker (no sbc configured) • Remote worker (sbc configured) • ALE-S can
    support Video • By default, profile 0 is configured • Possibility to have up to 100 profiles"
    (p152)
  summary: |
    规则五条：①系统默认 profile 0；②最多可建 100 个 profile；③ALE-S 与 8008 本地/远程共用一个
    profile；④ALE-x（ALE-2/3/30/x00）需要两个——本地版（不配 SBC）与远程版（配 SBC）；⑤ALE-S 支持
    视频。修改 profile 会为该 profile 下全部设备重新生成配置文件并发 SIP NOTIFY。远程桌面专用参数
    （双 SBC/双 RP/备用 LDAP、DNS2 公共 DNS 如 8.8.8.8/1.1.1.1）见 p407 表。
  conditions: profile 必须先建后配用户（p452 warning）
  tags: [rule, dm-profile]

- id: p20
  title: NOE↔SIP 切换规则——仅本地/仅 OXE DM/保留特性/禁止六场景/须在服
  type: rule
  source_pages: p154-155
  source_chapter: TRIGGER FROM OXE THE SWITCH FROM NOE TO SIP
  source_quote: |
    "Only for local users on site (not the remote one) • Only if these users have the OXE CS as SIP
    DM (not 8770 SIP DM) ... NOE to SIP: ALE-30, ALE-300, ALE-400, ALE-500" (p154)
    "Restrictions: The device with manager/assistant keys can't switch • The switch is forbidden for
    desk sharing, ubiquity, automated attendant, user profile and ACD station" (p155)
  summary: |
    规则六条：①只对本地（非远程）用户；②只在 OXE CS 充当 SIP DM 时（8770 DM 不行）；③机型——NOE
    转 SIP 限 ALE-30/300/400/500，SIP 转 NOE 限这些子型的 SIP Extension；④切换保留话机特性（按键、
    COS 号、呼转号、entity 号、语音信箱等）；⑤六类禁止——带 manager/assistant 键的设备不能切，
    desk sharing、ubiquity、自动话务员、user profile、ACD 站禁止切换；⑥操作仅当话机 in service 时
    生效，离服时 OXE 侧改完仍须话机本地 MMI 补做；快切要求 Phone COS "Force Download NOE/SIP"=YES，
    =NO 时切换现场补下二进制（慢）。话机 MMI 无需手动改运行模式（OXE 触发足够）。
  conditions: 双栈机才可切换
  tags: [rule, noe-sip-switch, restrictions]

- id: p21
  title: DM 配置文件命名与路径规则——MAC 型与 login 型（含邮箱登录分支）
  type: rule
  source_pages: p156
  source_chapter: CONFIGURATION FILE GENERATION / STORAGE
  source_quote: |
    "Physical devices 8008 and ALE-x • The DM generated file is based on MAC address. Filename is:
    config.<mac>.xml in '/DHS3data/mao/DM/dmictouch' folder" (p156)
    "ALES-Desktop: Initial path of the file '/DHS3data/mao/DM/dmsoftphone/ALES-desktop' ... When
    login account isn't a mail address tree, filename is: __/<first character of user login dump in
    hexa>/conf_<user login dump in hexa>.xml ... When login account is a mail address tree, filename
    is: <domain of mail>/<first character of user mail address dump in hexa>/conf_<user mail address
    dump in hexa>.xml" (p156)
  summary: |
    命名公式：①物理话机（8008/ALE-x）——config.<mac>.xml，存 /DHS3data/mao/DM/dmictouch（示例
    config.00809fedecc6.xml）；②ALES 按 login——目录 /DHS3data/mao/DM/dmsoftphone/ALES-desktop 或
    ALES-mobile；login 非邮箱时路径为 __/<login 首字符十六进制>/conf_<login 十六进制>.xml（示例
    user34109 → __/75/conf_757365723334313039.xml）；login 是邮箱时为 <邮箱域>/<首字符十六进制>/
    conf_<邮箱十六进制>.xml（示例 user34122@gmail.com → gmail.com/75/conf_...xml）。生成前提：设备有
    MAC（话机）或 login（ALES）+ 子型。
  conditions: 生成后无备份——恢复数据库后须手工 "generate all configuration files"（p166）
  tags: [rule, dm, config-file, naming]

- id: p22
  title: 话机配置下载认证双通道——401 挑战（号码+PIN+MAC）与 mTLS 8443 强认证
  type: rule
  source_pages: p157, p159-160
  source_chapter: PRINCIPLE FOR DESKPHONES (8008 AND ALE-X)
  source_quote: |
    "The OXE answers with '401' (authentication requested) • Auto-discovery mode is required ... the
    device sends an authentication request to the OXE with login (phone number), password (user
    password), mac address and its device type (in 'USER AGENT' field)" (p157)
    "a new instance is launched on port 8443, dedicated to OXE DM, on which mTLS is mandatory ...
    Reverse proxy must add in a specific HTTP header the Deskphone's MAC address, retrieved from the
    device certificate CN attribute • X-Real-Mac header with the Deskphone's MAC address • X-Forward-
    For header with the Reverse proxy's IP address" (p159-160)
  summary: |
    两条认证通道：①传统——NGINX 443 无文件时回 401，话机以 分机号+用户密码+MAC+机型 认证，OXE 校验
    后回写 MAC/子型、即时生成配置再发 200 OK，否则 403（auto-discovery 依赖此通道）；②R101.1 起
    mTLS——443 收请求后 302 重定向到专设 8443 实例（专用 NGINX 实例，强双向证书），CS 校验话机证书并
    比对 MAC↔证书 CN；原有 401 通道保留；可独立于原生加密开启；远程场景由 RP 注入 X-Real-Mac（话机
    MAC）与 X-Forward-For（RP IP），且只有 CS 已知的 RP 才被允许带这些头。开关在 swinst "DM auth.
    with client cert"（2.Expert→6.System Management→7.Nginx configuration→2.Update configuration
    parameters），默认 Enabled。ALES 不适用（走 login/密码认证）。
  conditions: mTLS 为 OXE DM 演进特性（as of OXE R101.1）
  tags: [rule, mtls, authentication, dm]

- id: p23
  title: OpenSSL 安全级别三级口径——2/1/0 语义、R101.0 默认 2、改动必须重启
  type: rule
  source_pages: p161-162
  source_chapter: OPENSSL SECURITY LEVEL
  source_quote: |
    "With OXE R101.0 and the upgrade of OpenSSL component to v3.0, the SSL security level has been
    increased to '2', that implies that any certificate with a RSA key length lower than 2048 bits or
    with a SHA-1 signing algorithm is no longer accepted" (p161)
    "2 : any certificates with a RSA key length lower than 2048 bits or signed with an older algorithm
    than SHA2 are refused. • 1 : any certificates with a RSA key length lower than 1024 bits ... •
    0 : no restriction. • A reboot of the system is required after security level modification."
    (p162)
  summary: |
    规则：R101.0 起 OpenSSL 升 v3.0，安全级别默认 2——RSA<2048 位或 SHA-1（早于 SHA2 的签名算法）
    一律拒收；部分近年出厂 ALE 话机仍是 1K RSA 密钥或 SHA-1 默认证书，部署老话机需评估降级。三级
    语义：2=拒 <2048 位/非 SHA2；1=拒 <1024 位/非 SHA2；0=不限制（3 仅 ALE 内部测试用）。配置在
    netadmin（root）：11 Security → 6 SSL configuration → 3 SSL security level；cryptview 命令可查
    当前级别；改后必须重启系统。话机证书核查两条路：SSH 上 certificate info 命令；话机 MMI——
    Enterprise/Essential/8008 走 Security > Certificate > View Certificate，Basic（ALE-2/3）走
    Advanced Settings > View Certificate。
  conditions: 降级是权宜之计，安全敏感站点应换证书而非降级
  tags: [rule, openssl, certificates, security]

- id: p24
  title: 内部 PKI 证书生成参数口径——CC-suite-ID/通配 SAN/IP SAN/密钥 2048-4096（默认 4096）/CTL 产物
  type: metric
  source_pages: p169-171
  source_chapter: Customization of the certificate for OXE DM with the internal PKI
  source_quote: |
    "CC-suite-ID []:11111-11111-11111-11111 ... Enter the key size (Between 2048-4096, Default 4096)
    : 4096 ... Common Name(CN)=oxe.company.com Subject Alternative Name(SAN)=DNS:oxe.company.com
    DNS:*.company.com IP Address:192.168.1.3 DNS:192.168.1.3 IP Address:192.168.1.1 DNS:192.168.1.1"
    (p169)
    "(1)csa> cd /usr3/mao/DM/VHE8082/ ... ctl_VHE8082 ict8000ctl.pem" (p171)
  summary: |
    参数口径：CC-suite-ID 取自 OXE 许可文件（存在时自动作根 CA 的 CN，无需手输）；通配 DNS
    *.company.com 默认加（覆盖整域）；物理与角色 IP 写入 SAN 默认加；附加 SAN 默认不加；密钥长度
    2048-4096 默认 4096；示例有效期 20 年（Nov 13 2025 → Nov 8 2045）。产物四件：内部根 CA、CS 密钥
    对、CS CSR、CA 签发的 CS 证书；核验后重启 OXE；话机侧 CTL 文件落在 /usr3/mao/DM/VHE8082/
    （ctl_VHE8082、ict8000ctl.pem；另一处写作 /DHS3/data/mao/DM/VHE8082，p166，同物异写）。
  conditions: 安装默认证书只服务 WBM/HTTPS，不适配 SIP 客户端
  tags: [metric, pki, certificate, ctl]

- id: p25
  title: DHCP 类与 VCI 对照表——ALE-2X(aledevice)、SIP80x8s(ictouch.0)、NOE(alcatel.noe.0)
  type: metric
  source_pages: p181, p204, p214
  source_chapter: Classes (ALE-2/3 lab, ALE-x00 lab, DHCP trigger appendix)
  source_quote: |
    "ALE-2/ALE-3 devices belong to a DHCP class, named 'ALE-2X' and use a Vendor Class ID (VCI)
    called 'aledevice'" (p181)
    "ALE-x00 devices belong to a DHCP class, named 'SIP80x8s' (same as NOE3GEE terminals) and use a
    Vendor Class ID (VCI) called 'ictouch.0'" (p204)
    "A NOE equipment uses the Vendor Class ID (VCI) called 'alcatel.noe.0'. So, the class using this
    VCI must be updated ... A configuration file ('sipconfig.txt') has to be specified in the class."
    (p214)
  summary: |
    三类对照：①ALE-2/ALE-3 → DHCP 类 ALE-2X，VCI=aledevice；②ALE-x00 → 类 SIP80x8s（与 NOE3GEE
    终端同类），VCI=ictouch.0；③NOE 设备 → VCI=alcatel.noe.0——把该类的配置文件（boot file name）
    设为 sipconfig.txt 即可让属类话机开机自动切 SIP（无需 MMI）。TFTP Server URL：无冗余/本地冗余用
    https://<OXE Main IP>/dmictouch；空间冗余必须 https://<OXE FQDN>/dmictouch（DNS 可解）。外部
    DHCP 时须自建对应 VCI 类并用 option 66（ALE-2/3 与 ALE-x00 同 URL；NOE 自动切换用 option 67 带
    sipconfig.txt）。
  conditions: 类与 VCI 由 OXE 内部 DHCP 自动创建；外部 DHCP 须手工复刻
  tags: [metric, dhcp, vci, classes]

- id: p26
  title: auto-discovery 与设备默认口令口径——分机号+密码 0000、高级菜单 123456、DM admin 密码 2580
  type: metric
  source_pages: p183-184, p177, p212
  source_chapter: MAC address allocation / Auto-discovery mode / DM profile Advanced characteristics
  source_quote: |
    "The username: Directory number of the user • The password: Secret code from the user (by default
    0000)" (p183)
    "Press Enter' and fill in the default password '123456'" (p183)
    "Admin password: 2580 • SSH: Yes" (p177)
  summary: |
    口径三条：①auto-discovery 认证用户名=用户分机号，密码=用户密码（secret code），默认 0000（话机
    端弹窗录入，成功后 MAC 自动回写 OXE 库并即时生成配置）；②ALE-2/3 话机本地 Advanced setting 菜单
    默认口令 123456（网络模式切换、静态 IP、Auto Provision 均要先过这道；Web 界面 admin/123456）；
    ③实验 DM profile 的 Advanced 特性里 admin password=2580、SSH=Yes（实验口径）。MAC 手工绑定与
    auto-discovery 二选一：手工绑定则配置文件立即生成，不绑则走 auto-discovery。
  conditions: 全部为实验/默认口径，生产必须改
  tags: [metric, auto-discovery, passwords, lab-口径]

- id: p27
  title: 双分区与 Force Download 语义——R200 分界、首次下载 30 分钟、快切前提
  type: metric
  source_pages: p188, p191-194, p200
  source_chapter: ALE-300/400/500 DEVICES DUAL PARTITION
  source_quote: |
    "From the binary version R200, out-of-the-box Deskphones include both binaries (NOE and SIP) ...
    Before this R200 version, only NOE binaries are present on these Deskphones." (p188)
    "Download 'Download' message means that currently, the NOE set is downloading the SIP binaries in
    background mode (it can take up to 30 minutes the first time) ... 'Upgrade' message means that
    currently, the NOE set is installing the SIP binaries in background mode (it is quite quick, a
    couple of minutes)" (p200)
  summary: |
    口径：①版本分界 R200——之前出厂仅 NOE 分区，SIP 二进制要从 CS 下载；R200 起出厂双分区但版本未必
    最新；②Force Download NOE/SIP=YES 时对侧二进制后台预载（首次下载可达 30 分钟，安装数分钟，装完
    自动重启），此后 NOE↔SIP 切换为快切；③=NO 时对侧分区不动，切换现场才下载（明显变慢）；④NOE
    二进制的后台升级与该参数无关，总是执行。版本核对 MMI 路径：Menu/Settings/Phone/Local Menu/About/
    Software 或 Menu/Settings/Options/Version。
  conditions: Phone COS 菜单：NOE and SIP Extension/NOE and SIP COS/Phone COS
  tags: [metric, dual-partition, force-download]

- id: p28
  title: ALES 部署专属参数口径——Framework 3s/50 条防隔离、Android Keep Alive=NO、轮询 ≥21600s
  type: rule
  source_pages: p227, p251-253
  source_chapter: ALE SoftPhone / SIP proxy & SIP phone C.O.S. & DM profile
  source_quote: |
    "'Framework period' and 'Framework Nb Message by period' parameters are used to avoid the ALES
    client being put in quarantine by OXE for 30 min due to DoS attack detection." (p227)
    "Keep Alive NO. For ALES Mobile, this 'Keep Alive' option is mandatory to be set 'NO' to be
    compatible with the Push Notification mechanism" (p252)
    "Config update polling timer If the value is configured below 21600s, the notification mechanism
    for ALES Android client will not work properly." (p253)
  summary: |
    三条 ALES 专属规则：①SIP Proxy 的 Framework period=3s、Framework Nb Message By Period=50——不配
    好则 ALES 客户端会被 DoS 检测误隔离 30 分钟；②ALES Mobile（Android/iPhone）的 Phone COS 里
    Keep Alive 必须设 NO，否则推送通知机制不工作；③ALES Android 的 DM profile Config update polling
    timer 若配低于 21600 秒（6 小时），配置更新通知机制将失效。PC 版话机侧 Keep Alive 反而建议 Yes
    （尽快产生离线消息，p201）。
  conditions: TCP when long messages 建议勾选（远程工作者尤其）
  tags: [rule, ales, quarantine, push]

- id: p29
  title: DM profile 拨号规则参数口径——区号 33/国家 FR/外线前缀 0/例外 ;0/最小长度 10
  type: metric
  source_pages: p229, p253
  source_chapter: DM profile / Telephony Characteristics (Dialing rule)
  source_quote: |
    "Area code 33 Country Code(ISO-3166-2) FR External access prefix 0 Exception ;0 Minimal length to
    apply rule 10" (p229)
  summary: |
    实验口径五格：Area code=33；Country Code(ISO-3166-2)=FR；External access prefix=0；Exception=;0；
    Minimal length to apply rule=10。生产按客户所在国编号计划替换；该规则决定 ALES 终端把用户拨的
    号码规整为出向格式。
  conditions: 实验口径（法国编号计划）
  tags: [metric, dm-profile, dialing-rule, lab-口径]

- id: p30
  title: 编解码优先级与必选规则——高带宽六级序、低带宽二级序、G729+G711 必选、法线不匹配回 488
  type: rule
  source_pages: p273-274, p278, p280-281
  source_chapter: CODECS NEGOTIATION
  source_quote: |
    "If the parameter is set to false, the other G711 law codec is rejected by the OXE A SIP 488 'not
    acceptable here' message is returned" (p273)
    "User SIP profile contains a list of available codecs: up to 5 coders • G729 ... It's mandatory to
    choose this codec among the 5 preferred codecs • G711A / G711 mu (PCMA/PCMU) • At least one G711
    codec is mandatory among the 5 preferred codecs" (p278)
    "High bandwidth : OPUS SWB > OPUS WB > G.722 > G.711 > OPUS NB > G.729 • Low bandwidth : OPUS NB >
    G.729" (p281)
  summary: |
    规则五条：①优先级——高带宽：OPUS SWB > OPUS WB > G.722 > G.711 > OPUS NB > G.729；低带宽：OPUS
    NB > G.729；策略=能力与配置允许下选最高质量；②用户 SIP profile 最多 5 个编解码，G729 必须在列，
    且至少一份 G711（A 律或 μ 律按系统法线）；③系统法线随安装国家（FR→A、US→μ），Accept Mu and A
    law in SIP=False 时对侧法线的 G711 被 OXE 拒绝并回 SIP 488 not acceptable here；通话中编解码清单
    重排，带系统法线的 G711 恒排第一；④G722/OPUS 支持域三档（Network and local/Local only/Not
    available）是系统级总闸——系统关了，外部网关开了也没用；⑤外部网关四开关联动：Support OPUS 或
    G722=YES 时 Support G711 必须=YES（对接 GD/OMS 必须 G711）；G729 建议恒 YES，限带宽场景改在 IP
    域控制；远端也要在 SDP 里带这些编解码。
  conditions: G723 不支持（p277）
  tags: [rule, codecs, priority, sdp]

- id: p31
  title: IP 域带宽语义与设备编解码能力矩阵
  type: metric
  source_pages: p275-277
  source_chapter: IP DOMAIN ROLE / DEVICES CAPABILITIES
  source_quote: |
    "Extra domain bandwidth ->calls between 1 end-point of this domain and another belonging to a
    different domain • High bandwidth Or • Low bandwidth (recommended most of the time*) • Intra
    domain bandwidth ... High bandwidth (recommended most of the time)" (p275)
    "Support of OPUS SWB / WB / NB and G.722 • Enterprise Deskphones (NOE & SIP), IP Desktop
    SoftPhone, ALES, Rainbow Web RTC Gateway, SIP & ABC-F IP trunks, ABC-F network (Direct Link mode
    only)" (p276)
  summary: |
    带宽语义：域内（intra）建议高带宽；跨域（extra）多数场景建议低带宽；高带宽=OPUS SWB/OPUS WB/
    G722/G711/OPUS NB/G729 全可，低带宽=仅 OPUS NB 与 G729；域 0（默认域）通常双高。设备能力矩阵：
    OPUS SWB/WB/NB+G722——Enterprise 话机（NOE&SIP）、IPDSP、ALES、Rainbow WebRTC 网关、SIP 与
    ABC-F IP 中继、ABC-F 网（仅 Direct Link 模式）；OPUS WB/NB+G722（无 SWB）——Essential 话机、
    Basic 话机、OXE-MS（原文将 8058s/68s/78s 特例与 Essential 段并列：8058s/68s/78s(NOE) 支持 OPUS
    仅 SWB、G722 本地/网络口径按原文）；仅 G722（无 OPUS）——8008/18/28s、8088、80x8；G722 与 OPUS
    全不支持——GD3/GD4/INTIP3（G.711/G.729）、A4645（G.711）、IP DR-Link（G.711）、WLAN/DECT、ABC-F
    网（Hybrid Link 模式）。OXE-MS 是 OPUS/G722 媒体服务（转码/会议/语音指南）的必要资源。
  conditions: 原文 8058s 行排版密集，引用时以 p276 原文为准；第三方 SIP 可不支持 OPUS/G722（从设备清单禁用）
  tags: [metric, codecs, devices, ip-domain]

- id: p32
  title: SEPLOS 省资源行为规则——18x 无 SDP、本地放音、Alert-Info URN、DTMF 三法
  type: rule
  source_pages: p289, p303, p305
  source_chapter: SIP TRACES / Call flows & Phone features activation
  source_quote: |
    "no SDP in 18x message • When a SIP extension calls a free user, there is no more compressor used
    for: Dial tone, Ring back tone, End call tone • Services activation by suffixes still requires a
    compressor" (p289)
    "urn:alert:tone:free is added in 180 (without SDP) message sent to caller ... urn:alert:tone:busy
    is added in 180 (without SDP) message sent to caller" (p303)
    "the DTMF exchange can be done with three methods • 'Out of band' (RFC 4733) ... 'Info' ... 'In
    band' ... The configuration of the DTMF method is done via the DM profile" (p305)
  summary: |
    规则集：①18x 不带 SDP——拨号音/回铃音/结束音不再占压缩资源，SIP 扩展自己放音；②后缀类业务激活
    仍要压缩资源（以 DTMF INFO 或 RFC4733 载荷送后缀）；③Alert-Info URN——180(无 SDP) 里带
    urn:alert:tone:free（被叫空闲）或 urn:alert:tone:busy（多线部分忙），主叫本地出音；被叫全忙时：
    允许遇忙回拨则回 183（SDP 带压缩资源）播"Call back on busy set"语音指南，否则 SIP 扩展自己放忙
    音；④早媒体两形态——SDP in 180（外部网关参数 SDP in 18x=True 时 18X 期间占资源）与 SDP in 183
    （Session Progress）；⑤DTMF 三法——RFC4733（RTP 内载荷，SDP 协商）、INFO 消息（逐位 200 OK 确
    认）、带内（RTP 音频），方法在 DM profile 配置；前缀+信息类激活时 CS 以 183+SDP 开 RTP 收 DTMF
    并放语音指南。
  conditions: SDP in 18x 是外部/本地网关参数（p86），True 时 ISDN in-band 指南才能被 SIP 侧听见
  tags: [rule, seplos, rtp, alert-info, dtmf]

- id: p33
  title: motortrace 级别表——0~9 与 a/b 十二级语义全录
  type: metric
  source_pages: p288
  source_chapter: SIP TRACES / trace-level
  source_quote: |
    "trace-level: 0: No trace (only Alarm) 1: Basic trace N1 ... 2: Medium trace N2 (N1 | T_MOTOR)
    3: All traces N3 (N2 | T_AUTH | T_MEDIA | T_DEBUG | T_INTERNAL_DESTR | T_LOG | T_FW | T_DB | T_US)
    4: Medium trace + T_AUTH (authentication) 5: Medium trace + T_MEDIA (media) 6: All traces +
    T_DUPLI (replication) 7: Medium trace + T_DUPLI (replication) 8: All traces + T_TRANSPORT +
    T_ADNS 9: All traces + T_INTERNAL_STRUCT (stack internal structure) a: Medium trace +
    T_OPTIONS_OPTIM b: All traces + T_OPTIONS_OPTIM + T_INTERNAL_STRUCT" (p288)
  summary: |
    十二级全录：0=无跟踪（仅告警）；1=基本；2=中（N1+T_MOTOR）；3=全（N2+T_AUTH/T_MEDIA/T_DEBUG/
    T_INTERNAL_DESTR/T_LOG/T_FW/T_DB/T_US）；4=中+认证；5=中+媒体；6=全+复制；7=中+复制；8=全+
    传输+ADNS；9=全+栈内部结构；a=中+OPTIONS 优化；b=全+OPTIONS 优化+栈内部结构。 verbosity 位图
    示例：1→0003a004。选型经验（p313 tips）：1 信息最少、2 适合大流量观察、3 适合无流量时定向深挖。
  conditions: motortrace 命令后跟级别参数；Ctrl-C 停止
  tags: [metric, traces, motortrace]

- id: p34
  title: sipdump 网关资源口径——20 呼叫许可+30 TLS 许可示例读数
  type: metric
  source_pages: p322
  source_chapter: SIP traces and tools / sipdump menu option 1
  source_quote: |
    "Use of licences : Yes OT gateways allowed : No UCaaS mode : No Number of initial licenses : 20
    Number of available licences : 20 Number of initial Tls licenses : 30 Number of available Tls
    licences : 30 Main server : Yes Degraded mode allowed : Yes Degraded mode activated : No" (p322)
  summary: |
    实验读数逐格（sipdump 选项 1 输出，实验口径）：许可启用=Yes；OT 网关允许=No；UCaaS 模式=No；
    初始许可 20、可用 20；TLS 初始许可 30、可用 30；主服务器=Yes；允许降级模式=Yes、未激活=No。该
    读数同时是"看许可余量"的现场工具：可用数随并发呼叫消耗。另有 CMotorDegradedModeTimerContext 与
    呼叫计数（Number of Calls 8 / Active 1）等输出。
  conditions: 数值为实验站点配置，生产读数随许可而变
  tags: [metric, sipdump, licenses, lab-口径]

- id: p35
  title: 外部 SIP 网关字段语义清单——Belonging/Remote domain、Registration ID、Pool、RFC3325、ICE type
  type: checklist
  source_pages: p353-354
  source_chapter: External SIP gateway (field notes)
  source_quote: |
    "SIP Remote domain: IP address or FQDN of the 'border element' on the provider side • Belonging
    Domain: The authentication domain is used to define a set of URLs for which the same
    authentication is required" (p354)
    "Pool Number: it is possible to specify the same index in 2 gateway that belong to the same
    provider. In this case in the ARS table it is necessary to create only one route with the first
    gateway and the CS will split the traffic between the gateways." (p354)
  summary: |
    字段语义清单：①Remote domain=运营商侧边界单元（SBC）的 IP/FQDN；②Belonging Domain=认证域（一组
    共用同一认证的 URL）；③Registration ID=注册时 From 头的 user 部分，注册 URL 为 Registration
    ID@Authentication Domain，频率由 Registration timer 定；④Registration ID P_Asserted：No=P-
    Asserted-ID 带主叫 DDI，Yes=带网关注册 ID；⑤SIP Outbound Proxy=须将发往边界单元的消息先送运营
    商代理时才填（追加 Route 头）；⑥Supervision timer=发 OPTIONS 探活周期（0=不监）；⑦公共中继组
    （ISDN all countries）只允许 Re-INVITE 直连 RTP（无转移、无溢出）；⑧Pool Number=同一运营商两网关
    同序号时，ARS 只建一条路由、CS 自动分流；⑨RFC 3325：远端支持 P-Asserted-Identity 时（出向）匿名
    场景 From=anonymous@anonymous.invalid，不支持时 From=号码@Belonging Domain；⑩Gateway type 默认
    Standard，OmniTouch 环境承载 OT 用户的网关须设 ICE type（启用 P-Alcatel-CSBU 与 P-CAC-ALU 私有
    头）；⑪SDP in 18x 决定 OXE 发出的 180 是否带 SDP。
  conditions: 每个运营商参数不同（p349 warning），以 TC2005 与运营商文档为准
  tags: [checklist, external-gateway, fields]

- id: p36
  title: ARS 配置规则——SIP 中继组必配 ARS、前缀/判别器/路由表/时间清单/entity 关联
  type: rule
  source_pages: p355-358
  source_chapter: Basic ARS configuration for SIP trunk group use
  source_quote: |
    "Warning ARS IS REQUIRED TO USE SIP TRUNK GROUP WITH AN EXTERNAL SIP GATEWAY" (p355)
    "No.Digits To Be Removed Specify the number of digits to remove. Here 1 to remove the '0' from
    the called number Digits To Add Specify the digits to add. In our case 33" (p356)
    "Warning HERE, IT IS NOT AS FOR THE REAL DISCRIMINATOR CONFIGURATION WITH THE ARS TABLE NUMBER, IT
    IS NOT POSSIBLE TO ASSOCIATE TO A LOGICAL DISCRIMINATOR A REAL DISCRIMINATOR NUMBER IF THIS LAST
    ONE IS NOT ALREADY EXISITING." (p358)
  summary: |
    规则链：①用外部网关的 SIP 中继组必须配 ARS（硬前提）；②链路四层——Prefix Plan（外线前缀 0 →
    逻辑判别器 0~7）→ 中继组（可直接关联外部网关，或经编号命令表）→ ARS 路由表（删位/加位变换：实验
    去 1 位"0"加"33"；被叫号源=Route；NPD 暂 255；Quality=Speech）→ 基于时间的路由清单（决定路由
    使用顺序；等待/停止成本限制默认 -1 不限）；③公共判别器规则（0 public）：呼叫号 0、区域 1（默认，
    不做闭锁）、ARS 表号、日程 -1、位数=国内拨号计划长度（实验 10）；④逻辑↔实际判别器映射挂 entity
    （用户默认 entity 1，可按部门给不同判别器）；⑤硬约束——entity 上只能关联"已存在"的实际判别器。
  conditions: 实验变换（去 0 加 33）为法国国内口径
  tags: [rule, ars, discriminator, numbering]

- id: p37
  title: DID/NPD/回拨翻译三件套参数——33920x31000/范围 1000/NPD 34 国际/A33 去 3 加 00
  type: metric
  source_pages: p359-361
  source_chapter: DID translation / NPD management / Callback translator
  source_quote: |
    "First External Number Enter the first DID number corresponding to your system, example: 33920131000
    for POD 1 ... Range Size Specify the size of the range. E.g. here: 1000 Unique Internal Number NO"
    (p359)
    "Description identifier Enter a number. Example here: 34 ... Calling Numbering plan ident. NPI/TON
    ISDN International ... Default number (num. inst. sup) Enter the first DID number of your system"
    (p360)
    "Basic Number A33 No. Digits To Be Removed 3 Digit To Add 00 -> first zero is for ARS prefix and
    the second for the '0' displayed in national numbers" (p361)
  summary: |
    三件参数（实验口径，POD 1 示例）：①DID 翻译器（ID 1；0 号为默认翻译器；模式 Default DID mode）：
    首外线 33920131000（POD x 为 33920x31000）、首内线 31000、范围 1000、Unique Internal Number=NO；
    ②NPD 34（public_operator_2）：主/被叫 NPI/TON=ISDN International、安装号源=None used、默认号源
    =NPD source、默认号=首 DID、被叫与主叫/连接 DID 标识均指向该翻译器；中继组 NPD 选择器：公共与
    专用 NPD ID=34、Management Mode=Normal；③回拨翻译（DEFAULT 表）：A33 → 删 3 位 → 加 00（第 1 个
    0 是 ARS 前缀，第 2 个是国内号显示的 0），让回拨显示 0xxxxxxxxx 且可回拨。
  conditions: POD 号替换 x；生产以运营商给的本局号段为准
  tags: [metric, did, npd, callback]

- id: p38
  title: OTSBC 编解码与操纵口径——向导默认 2 coder、域改写 itsp2.fr、Contact User=podX
  type: rule
  source_pages: p374-383
  source_chapter: OTSBC deployment / Manual configuration
  source_quote: |
    "In the INVITE message, from OXE to SBC, in the SDP, possible codecs are G722, G711 (PCMA) & G729
    ... In the INVITE message, from SBC to ITSP, in the SDP, possible codec is G711 (PCMA)" (p374)
    "Action Subject header.from.url.host Action Type Modify Action Value 'itsp2.fr'" (p377)
    "Put the login expected (podX) by the ITSP gateway in the field 'Contact User'" (p382)
  summary: |
    三条修正规则：①编解码——向导默认给 OXE 侧 IP 组只配 2 个 coder（仅 G711 PCMA 转发），须在 Allowed
    Audio Coders Groups 组 1 追加 G729 等（Apply+Save 生效）；②消息域——ITSP 不认 OXE IP 域，须建
    Message Manipulation Set（from.url.host 与 to.url.host → Modify 'itsp2.fr'）并绑到 ITSP IP Group
    的 Outbound Message Manipulation Set，Proxy Authorization 域随之正确；③注册——向导账号缺
    Contact User 时 REGISTER 的 from/to/contact 格式不对、来话无法路由；补 Contact User=podX（运营
    商期望的登录名）后 REGISTER 变 podX@itsp2.fr，来话打通；Action 菜单 Register 可立即注册。
  conditions: 值 itsp2.fr/podX 为实验口径；排障证据链以 Syslog 报文对照
  tags: [rule, ot-sbc, manipulation, registration]

- id: p39
  title: OTSBC 远程对象参数口径——SIP 接口 TLS 5261、媒体 6000 起、NAT 5261/6000-6399、Diffserv 40、DH 2048
  type: metric
  source_pages: p425-441
  source_chapter: OTSBC with embedded Reverse Proxy (How-To)
  source_quote: |
    "TLS Version TLSv1.1 and TLSv1.2 ... DH Key Size 2048" (p426)
    "TLS Port 5261 ... User Security Mode Accept Registred Users Enable Un-Authenticated
    Registrations Disable" (p438)
    "UDP Port Range Start 6000 Number of Media Session Legs ... E.g. : 100" (p439)
    "Source Start Port 5261 Source End Port 5261 Target IP Address ... 12.C.P2.105 ... Source Start
    Port 6000 Source End Port 6399" (p439-440)
    "Broken Connection Mode: Ignore SBC Media Security Mode: Secured Signalling Diffserv 40" (p441)
  summary: |
    逐格口径（实验）：TLS Context——TLSv1.1/1.2、DTLSv1.0/1.2、Cipher Server AES:RC4、Client
    ALL:!ADH、DH 2048；SIP Interface 3——WAN eth1、TLS 端口 5261、用户安全模式=Accept Registered
    Users、禁未认证注册；Media Realm——UDP 端口从 6000 起、媒体腿数示例 100；NAT 翻译两条——5261→
    5261 与 6000-6399，目标公网 IP=12.C.P2.105（C=class，P=POD）；IP Profile——Broken Connection
    Mode=Ignore、SBC 媒体安全=Secured、信令 Diffserv=40（OXE 侧既有 profile 为 Not secured、Ignore）；
    媒体安全全局 Enable + Mandatory + AES-CM-128-HMAC-SHA1-80；NAT Traversal=NAT Only if Necessary
    （媒体通道默认 10000）。RP 三件套——Upstream OXE_443（192.168.1.3:443，IP Hash）、Proxy Server
    （公网域名、eth1:443、TLS context、不验客户端证书）、Location（/DM/dmsoftphone/ 前缀 → HTTPS →
    OXE_443，出向 eth0）。
  conditions: 全部实验口径；生产公网 IP/FQDN 与端口按站点规划
  tags: [metric, ot-sbc, reverse-proxy, ports]

- id: p40
  title: 反代规模红线——≤500 远程用户用 OTSBC 内嵌 RP，更多用 NGINX PLUS（DSPP）
  type: rule
  source_pages: p387, p400
  source_chapter: REMOTE WORKERS / ALES - TOPOLOGY THROUGH SBC / SIP ALE DESKPHONES
  source_quote: |
    "For small configuration (<= 500 remote users), it is possible to use the OTSBC embedded Reverse
    Proxy • If more, ALE recommends NGINX PLUS reverse proxy delivered by NGINX company, member of
    DSPP" (p387)
  summary: |
    规模规则：远程用户 ≤500 可直接用 OTSBC 内嵌反向代理（一机双职能）；超过 500 ALE 推荐 NGINX 公司
    （DSPP 成员）的 NGINX PLUS 反向代理。两条远程路（RP/SBC 与 VPN）同样适用该分界；RP 与 SBC 功能可
    共用同一公网 IP/FQDN 或分设（p392 注）。
  conditions: 双 SBC 主动/主动高可用经 SIP DM profile 第二地址实现（p396）
  tags: [rule, reverse-proxy, capacity]

- id: p41
  title: 远程桌面 DM profile 参数表——双 SBC/双 RP/备用 LDAP/DNS2 公共
  type: metric
  source_pages: p407
  source_chapter: OXE DM Profile settings (specific parameters for remote worker)
  source_quote: |
    "DNS1 @IP of DNS on LAN ... DNS2 @IP of DNS on WAN (public DNS like 8.8.8.8, 1.1.1.1) ... SBC:
    SBC and LAN ... Outbound proxy address SBC1 FQDN ... Outbound proxy address2 SBC2 FQDN ...
    Reverse Proxy FQDN RP1 FQDN ... Reverse Proxy FQDN2 RP2 FQDN ... LDAP backup server URL Remote
    LDAPS FQDN:port ... ldaps://RP1_FQDN:636" (p407)
  summary: |
    参数表逐格：DNS1=LAN 的 DNS；DNS2=WAN 公共 DNS（如 8.8.8.8、1.1.1.1）；SNTP 留空时配置文件用
    OXE 节点 FQDN；SBC=SBC and LAN；Outbound proxy address/port=SBC1 FQDN 与其 SIP TLS 端口；address2/
    port2=SBC2（第二 SBC，主备或负载分半）；Reverse Proxy FQDN/FQDN2=RP1/RP2；LDAP server URL=本地
    LDAP(S) FQDN:端口（389/636）；LDAP backup server URL=ldaps://RP1_FQDN:636；LDAP backup2=
    ldaps://RP2_FQDN:636。ALE-S 与 8008 一个 profile 兼容本地/远程；ALE-x 系本地/远程各一份。
  conditions: 双 SBC 负载均衡也可用两份 profile 各管一半 ALES（p396）
  tags: [metric, dm-profile, remote-worker]

- id: p42
  title: EDS 零touch 服务口径——两域名、AWS 巴黎、Profile 三要素、四限制
  type: metric
  source_pages: p401, p404-405
  source_chapter: SIP ALE DESKPHONES - TOPOLOGY THROUGH SBC/RP/EDS
  source_quote: |
    "'EDS' is an ALE cloud server that allows the deployment of deskphones in remote worker situation
    • ALE EDS cloud service is hosted by Amazon Web Service data center in Paris, France • Redundant
    infrastructure • Secured: all data are encrypted" (p401)
    "Admin URL: https://admin.eds.al-enterprise.com • Request for account creation on :
    https://admin.eds.al-enterprise.com/register • FQDN hardcoded in phones:
    device.eds.al-enterprise.com" (p405)
    "Restrictions: • No outbound HTTP proxy • No network requiring 802.1x authentication or VLAN
    identifier • No Wi-Fi (yet)" (p404)
  summary: |
    口径：EDS=ALE 云端零touch 部署服务器，宿于 AWS 巴黎数据中心，冗余部署、数据全加密；管理入口
    admin.eds.al-enterprise.com（开户 /register），话机内硬编码 FQDN=device.eds.al-enterprise.com；
    话机按 MAC 预配并关联 Profile，Profile 三要素——URL=https://<RP 域名>/DM/dmictouch、Cert Name=
    RP 根证书（PEM 上传）、Pre-configure Area=强制 SIP 模式与可选备用 RP URL（RunMode=SIP、
    EdsEnetcfgDmBackupUrl）。零touch 四限制：无出向 HTTP 代理、无 802.1x 认证、无 VLAN 标识、暂无
    Wi-Fi。
  conditions: 适用 ALE-x00/ALE-30（双栈）与 ALE-2/3（恒 SIP 起步）
  tags: [metric, eds, zero-touch]

- id: p43
  title: 原生加密远程工人规则——N4 起放行、Via 头识别、10 个 SBC IP 上限
  type: rule
  source_pages: p414-415
  source_chapter: NATIVE ENCRYPTION & REMOTE WORKERS
  source_quote: |
    "Native encryption user parameter can be enabled on a remote worker (since OXE N4) • This ensures
    end-to-end encryption of the SIP device whatever its location" (p414)
    "The 'Via' header of the SIP Register message contains an IP address of SBC ... even if the
    user's native encryption configuration (TLS/TCP/UDP) does not correspond to the transport mode
    managed between the SBC and the OXE (TLS/UDP/TCP), the OXE authorizes the provisioning of this
    user • This was not the case before the OXE N4 version • a new management menu allows you to
    specify up to 10 LAN IP addresses of the SBCs ... These SBC IP addresses are automatically added
    to the SIP trusted host list" (p415)
  summary: |
    规则四条：①OXE N4 起远程工人可开原生加密用户参数（端到端加密，无论在场内场外）；②OXE 经 REGISTER
    Via 头中的 SBC IP 动态识别远程工人；③识别后即使用户加密传输模式（TLS/TCP/UDP）与 SBC-OXE 段模式
    不一致也放行（N4 之前不允许）；④新管理菜单最多登记 10 个 SBC 的 LAN IP，该清单不向其他 OXE 节点
    广播/审计，且自动加入 SIP 信任主机清单。LAN 段 SRTP 要求 OT-SBC 与 OXE 之间走 TLS 传输并开加密
    用户参数（四种拓扑的明/密组合见 p416-419）。
  conditions: 适用 ALES 与 Enterprise、Essential（仅 ALE-30）、Basic SIP 话机
  tags: [rule, encryption, remote-worker]

- id: p44
  title: VPN 远程边界——ALE-2/3 内嵌 OpenVPN（不支持 IPSec）、ALE 不提供客户端
  type: rule
  source_pages: p398, p412
  source_chapter: ALES - TOPOLOGY THROUGH VPN / SIP ALE BASIC DESKPHONES - TOPOLOGY THROUGH VPN
  source_quote: |
    "The solution is compliant with all VPN Gateways • A third-party VPN client is required to
    establish the VPN link • ALE doesn't provide any VPN client. • The level of security depends on
    the deployed VPN infrastructure" (p398)
    "ALE-2, ALE-3 SIP basic Deskphones embed a VPN client, allowing them to remotely connect to the
    OmniPCX enterprise through a VPN Gateway installed on customer premises • ALE-2/ALE-3 only
    support OpenVPN, not IPSec VPN • VPN tunnels are secured with TLS authentication, credentials and
    certificates • EDS server can provide VPN configuration" (p412)
  source_quote_note: 另见 p107 "Remote access through SBC/RP or VPN VPN client not provided"
  summary: |
    两条边界：①ALES 走 VPN——兼容所有 VPN 网关，但需第三方 VPN 客户端（ALE 不提供），安全水平取决于
    客户 VPN 基础设施；②ALE-2/ALE-3 话机内嵌 VPN 客户端（唯一内嵌机型），仅支持 OpenVPN 不支持
    IPSec，隧道以 TLS 认证+凭证+证书保护，EDS 可下发 VPN 配置；兼容 VPN 网关清单见 Server deployment
    Guide for Remote workers。
  conditions: VPN 话机与 SBC/RP 路二选一或并存，按站点网络约束定
  tags: [rule, vpn, ale-2-3]

- id: p45
  title: OTSBC 反代域名与位置 Location 口径——/DM/dmsoftphone/ 前缀转发、443 入 5261 注册
  type: rule
  source_pages: p433-435, p447-449
  source_chapter: OTSBC with embedded Reverse Proxy / HTTP Proxy Server & IP Routing
  source_quote: |
    "Domaine Name Enter the public domain name. Example in our case: rpsbcX.company.com ... HTTPS
    Listening Port 443 ... URL Pattern /DM/dmsoftphone/ URL Pattern Type Prefix Upstream Scheme HTTPS
    Upstream Group OXE_443 Upstream Path /DM/dmsoftphone/" (p434-435)
    "Condition Header.to.URL contains '192.168.1.105' ... When it is a call for the ITSP, 'header.to'
    is the SBC IP address - When it is a call at destination of a remote worker, 'header.to' is the
    registered address of the device" (p447)
  summary: |
    规则四条：①RP 监听 WAN 口 443，公网域名 rpsbcX.company.com；②只转发 /DM/dmsoftphone/ 前缀的
    HTTPS 请求到 OXE_443 上游组（192.168.1.3:443）同路径；③ITSP 与远程流量的区分靠 Message
    Condition——OXE 发往 ITSP 的呼叫 header.to=SBC IP（192.168.1.105），发往远程工人的 header.to=
    设备注册地址；现有 OXE→ITSP 的 IP-to-IP 路由挂上该条件，另建两条：OXE→All Users（远程）、
    RemoteUsers→OXE 组；④远程 IP 组绑操纵组 3（to/from/Refer-To/Referred-By 的 url.host 改写为
    'rpsbcX.company.com:5261'），OXE 组 2 追加反向规则（host 含 rpsbcX → 改 'oxe'）保证 OXE 侧域一致。
  conditions: 实验口径；生产替换域名/IP/端口
  tags: [rule, reverse-proxy, routing, manipulation]

- id: p46
  title: 终端互通与注册行为规则——注册即在服、IP 入库用于 CAC、超时置 0.0.0.0
  type: rule
  source_pages: p80
  source_chapter: COMMUNICATION WITH SIP END-POINTS / REGISTRATION OF THE USERS
  source_quote: |
    "The users is in/out of service according to its registration status on the registrar server • A
    SIP extension is in service only after it has registered ... The IP address is used to assign the
    SIP set to an IP Telephony Domain and to handle features, such as Call Admission Control (CAC)
    When a de-registration request is received or if the system does not detect SIP set presence
    after a timeout, the IP address of the corresponding SIP set is put to 0.0.0.0 and the SIP set is
    put out of service" (p80)
  summary: |
    三条行为规则：①SEPLOS/SIP 用户注册后才 in service，注销即 out of service；②注册 IP 同时写注册库
    与 OXE 库，用于 IP 电话域归属与 CAC（呼叫准入控制）等特性；③收到注销请求或 Keep Alive 超时未探活
    后，该终端 IP 置 0.0.0.0 并 out of service。核查命令 sipregister（注册库转储，含 AOR/contact/
    剩余租期）。
  conditions: "sipregister h" 查看帮助
  tags: [rule, registration, cac]

- id: p47
  title: 用户 SIP profile 编解码五席规则与 MicroSIP 对照
  type: rule
  source_pages: p277-278
  source_chapter: DEVICES CAPABILITIES / Deskphone-softphone capabilities
  source_quote: |
    "The SIP end-point is configured/developed to propose a list of codecs ... List and order of
    proposed codecs in the SDP sent by the application depend on its parameters configuration List of
    proposed codecs in the SDP sent by the application is defined in the user SIP profile. Codecs
    order is fixed" (p277)
    "User SIP profile contains a list of available codecs: up to 5 coders ... Example with the
    default configuration" (p278)
  summary: |
    规则三条：①终端经 SDP 提报编解码清单——ALES 等 ALE 应用清单由其参数配置决定（顺序可调），MicroSIP
    类第三方清单由用户 SIP profile 定义且顺序固定；②用户 SIP profile 最多 5 个编解码（G729 与一份
    G711 必选，见 p30）；③第三方 SIP 可能不支持 OPUS/G722，应从设备编解码清单禁用而不是硬协商。
  conditions: G723 不支持
  tags: [rule, codecs, sip-profile]

- id: p48
  title: SBC 信任主机与防火墙联动规则——SBC/远程链路 LAN IP 必须进 CS 信任主机（/etc/hosts）
  type: rule
  source_pages: p90, p177, p349, p451
  source_chapter: SIP Users warning / SIP Carrier access via SBC / ALES Remote Worker warning
  source_quote: |
    "THE SIP DEVICE MUST BE DECLARED AS TRUSTED HOST IN THE CS INTERNAL FIREWALL (NETADMIN -M /
    SECURITY). SO, MAKE SURE THAT THE IP ADDRESS OF THIS DEVICE IS PRESENT IN THE HOST FILE
    (MORE /ETC/HOSTS)." (p90)
    "FOR REMOTE WORKERS PURPOSE, TO PERMIT MESSAGES EXCHANGE BETWEEN OTSBC AND OXE, OTSBC PRIVATE IP
    ADDRESS (LAN SIDE) MUST BE DECLARED AS CALL SERVER TRUSTED HOST." (p451)
  source_quote_note: SIP Extension 同款警告见 p177/p230；OXE 内部 DHCP 启用时其地址段自动入防火墙（p177 note）
  summary: |
    规则：一切"从网络侧向 CS 发 SIP/HTTPS 请求"的设备——SIP Device 话机、SIP Extension 话机、SBC
    （LAN 侧地址）、远程链路——都必须登记为 CS 内部防火墙信任主机（netadmin -m/Security → Restricted
    Access → Add trusted host），登记后自动写入 /etc/hosts（more /etc/hosts 核对）；双机系统用
    Copy set up 同步防火墙；OXE 内部 DHCP 启用时其地址范围自动入防火墙。漏配的典型症状是终端/网关
    完全无响应。
  conditions: Starter 课程主题，本教材多处回指
  tags: [rule, firewall, trusted-host]

- id: p49
  title: OXE 与 8770 DM 能力分界清单——OXE DM 仅支持 8008/ALES/ALE-2/3/30/x00
  type: rule
  source_pages: p147-148
  source_chapter: SIP DM: OXE VS 8770
  source_quote: |
    "8770 DM benefits: Centralized for all OXE nodes and OXE networks with User & device template ...
    Support existing SIP phones : 8088 Hotel or Huddle Room, 8008, ALE-x ... and also some other phone
    types, phased-out today (8001, 8018, 8028s…)" (p147)
    "OXE DM benefits: Higher security with customer base certificate ... Support only phones 8008,
    ALE SoftPhone and ALE-x (ALE-2, ALE-3, ALE-30, ALE-x00)" (p147)
    "This option is not taken into account for ALES clients, which are only supported on OXE DM"
    (p148)
  summary: |
    分界清单：OXE DM 只支持 8008、ALE SoftPhone、ALE-2/3/30/x00；8770 DM 额外支持 8088 酒店/Huddle
    Room 及已停产机型（8001/8018/8028s 等）——存量老话机必须留在 8770。ALES 只受 OXE DM 管理，与
    "Device Management in 8770" 参数无关（恒归 OXE）。开关语义：参数勾选=DM 在 8770；取消=DM 在 OXE。
    OXE DM 的附加优势：客户级证书更安全、按节点 DM profile、随 CS 复制更韧、二进制自动更新+配置修改
    即时通知、仍可配 8770 User 应用。
  conditions: 迁移混合拓扑=话机留 8770 + ALES 归 OXE（p149）
  tags: [rule, dm, 8770, migration]

- id: p50
  title: 编解码验证命令与读数口径——compvisu 输出四场景对照
  type: metric
  source_pages: p284-286
  source_chapter: Codecs (How-To) / compvisu
  source_quote: |
    "type term : IPT 8068s, mcdu=31000 <--> SIP, mcdu=31030 ... nbcomp / comp type : - / LIOE_IP-G722
    (83) <--> - / NOCOMP-G722 (80)" (p284)
    "nbcomp / comp type : - / NOCOMP-OPUS_WB (c0) <--> 0 / NOCOMP-OPUS_WB (c0)" (p285)
  summary: |
    读数口径（compvisu eqt all）：①SEPLOS 内呼 NOE IP 话机——G722（一侧 LIOE_IP-G722(83)、一侧
    NOCOMP-G722(80)，NOCOMP=无转码直通）；②经私有 SIP 中继组——G722 + ABC-F 中继参与；③SEPLOS 呼
    公网（ITSP2）——OPUS_WB 双侧 NOCOMP-OPUS_WB(c0)（公网 SIP 中继 + 外部网关 OPUS 开启）；④SIP
    Device 呼公网——G722 经公共与私有两条 SIP 中继组。结论规则：实际编解码由用户 SIP profile、系统
    参数、IP 域与外部网关开关共同决定，任何"音质/单向语音"工单先用 compvisu 定格实际算法。
  conditions: compvisu 为 mtcl 命令；eqt all 显示全部活动连接
  tags: [metric, codecs, compvisu, verification]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 20 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 准备实验/交付环境 | 部分 | p26（默认口令口径），p48（信任主机） | 账号表/IP 清单本身为实验口径，归 framework f02/f03；此处收口令与防火墙默认规则 |
| task-02 | 掌握运营商模拟器 | 无独立数值条目 | ——（f04/f05 承接） | 号码规则为实验口径的结构性内容，不构成通用原则 |
| task-03 | POD 预配置与外线打通 | 部分 | p36（DID/NPD 三件套），p35（网关字段语义） | pbxN 参数与 33210N41000 归 f06；通用字段语义在 p35 |
| task-04 | SIP 协议机理 | 有 | p01, p02, p08, p46 | 协议规格、响应码、租期边界、注册行为 |
| task-05 | OXE 域名与空间冗余 | 无独立数值条目 | ——（f12/f13 承接） | FQDN 构成规则已并入 f13 与 p24（CN/SAN） |
| task-06 | SEPLOS vs SIP Device 选型与容量 | 有 | p03, p04, p09, p10, p11 | 软件锁、容量上限、两形态限制清单、功能矩阵 |
| task-07 | SIP Device 开通 | 有 | p05, p06, p07, p08, p48 | 中继组容量公式、网关/代理/注册器参数、隔离规则 |
| task-08 | 终端家族选型 | 有 | p11, p12 | 两张功能矩阵表 + 不支持清单 |
| task-09 | ALES 认证设计 | 有 | p13, p14, p28, p35 | 密码强化、一号多机、防隔离参数、swinst（菜单在 framework f35） |
| task-10 | ALE SIP 特性配置 | 有 | p15, p16, p17, p18 | 监督容量与事件码、按名呼叫、可编程键、寻线组 |
| task-11 | SIP DM 选型与规划 | 有 | p19, p21, p25, p49 | profile 规则、配置文件命名、DHCP 类、OXE/8770 分界 |
| task-12 | OXE DM 证书定制 | 有 | p22, p23, p24 | mTLS 双通道、OpenSSL 三级、PKI 参数与 CTL |
| task-13 | ALE-2/3 话机开通 | 有 | p25, p26, p48 | DHCP 类/VCI、auto-discovery 口令、信任主机 |
| task-14 | ALE-x00 双分区与切换 | 有 | p20, p27 | 切换六规则、R200 分界与 Force Download 语义 |
| task-15 | ALES 软终端开通 | 有 | p13, p14, p28, p29 | 密码策略、互斥、专属参数、拨号规则五格 |
| task-16 | 编解码协商与验证 | 有 | p30, p31, p47, p50 | 优先级规则、域/设备矩阵、profile 五席、compvisu 读数 |
| task-17 | SIP 跟踪采集分析 | 有 | p33, p34, p32 | motortrace 级别表、sipdump 许可读数、SEPLOS 行为规则 |
| task-18 | 外部网关判定 + SBC 接入 | 有 | p35, p36, p37, p48 | 网关字段语义、ARS 规则、DID/NPD/回拨参数 |
| task-19 | OTSBC 部署调通 | 有 | p38, p39 | 排障三修正规则、远程对象参数口径 |
| task-20 | 远程办公规划与落地 | 有 | p40, p41, p42, p43, p44, p45 | 规模红线、DM profile 参数表、EDS 口径、加密规则、VPN 边界、反代路由规则 |

**覆盖结论**：20/20 全部有对应条目（task-02/05 以框架类承接为主，已注明原因）。三点口径说明：
1. p04 容量表中 "Maximum 5000" 一处归属对象在纯文本层不可辨，已照录并注明，未编造归属。
2. p11 功能矩阵中 "✓/空白" 双列在文本层存在并列歧义，条目内已注明以原文双列为准，未替原文补格子。
3. 所有口令类数值（Superuser2580*、alcatel、0000、123456、2580）均标"实验口径"；编解码优先级、992 TS、86400 等通用数值按原文完整位数转写。
