# 术语/缩写/产品名候选 — OmniPCX Enterprise SIP (ENTPXTE403EN R101.1 MD4 Ed12)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 55 条。SEPLOS、ARS、NPD、NOE、ABC-F、DPNSS、REX、PCS、CAC、CSTA、MLA、DSPP、OT/OTSBC、SBC 部分缩写等书中未给全称者，full_name 字段如实省略或仅引原文拼写，不做外部补全。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: SIP
  full_name: Session Initiation Protocol（书中展开）
  category: concept
  source_pages: p45-54
  source_quote: |
    "SIP: Session Initiation Protocol ... IETF Standard: RFC 3261 ... Establish, maintain, modify and
    terminate multimedia sessions ... Media negotiation (codecs) but not the transport" (p45)
    "Elements of the SIP world are identified by SIP Uniform Resource Locators (URLs) similar to
    e-mail addresses" (p48)
  definition: |
    本书的"主课语言"：应用层信令协议（TCP/UDP、IPv4/v6、RFC 3261），负责多媒体会话的建立/维持/修改
    /终止与媒体协商；媒体传输归 RTP，媒体特征由 SDP 描述；元素以 SIP URL 标识；信令可加 TLS。书中
    所有排障都落到"读 SIP 报文"这一技能上。
  alias_or_related: SIP URL、SDP（并入相关条）；对照 g02 SEPLOS / g03 SIP Device
  tags: [concept, sip, protocol]

- id: g02
  term: SEPLOS (SIP Extension)
  full_name: SIP End Point Level of Services（书中展开）
  category: concept
  source_pages: p66-74, p80
  source_quote: |
    "SEPLOS mode (SIP End Point Level of Services) • The SIP sets operating in SEPLOS mode are
    considered by the phone application as internal sets" (p66)
    "Set type: SIP Extension • With 2 multiline keys created automatically • Sub type: Default,
    ALE-300, …, ALES Desktop, … • DM profile specified" (p73)
  definition: |
    SIP 用户两形态之一：电话应用把这类终端当"内部话机"，享受前缀/后缀业务、多线（自动两条 multiline
    键）、寻线组/代接组、SIP MESSAGE 显示 CS 信息、原生加密、RCC 增强等；管理靠 子型+DM profile。
    sipdict 中 type=3。
  alias_or_related: 对照 g03 SIP Device；限制清单见 counter-example n02/n53
  tags: [concept, seplos, sip-extension]

- id: g03
  term: SIP Device
  category: concept
  source_pages: p66-68, p75-78, p84-94
  source_quote: |
    "SIP Devices • SIP sets are considered by the phone application as part of a remote subnetwork
    • This operating mode requires to configure: A subnetwork and the trunk group associated to this
    subnetwork, before declaring SIP sets" (p66)
    "Set type: SIP device" (p77)
  definition: |
    另一形态：被电话应用视为"远端子网的一部分"，须经 私网+私有 SIP 中继组+本地 SIP 网关 三件套才能
    建；服务缩水（无前缀/后缀、无酒店、无 CTI、无坐席、不入组）。典型对象：会议话机、视频设备、
    门禁（doorcam）。sipdict 中 type=2。
  alias_or_related: 对照 g02 SEPLOS；限制清单见 n02
  tags: [concept, sip-device]

- id: g04
  term: SIP Gateway (local)
  category: concept
  source_pages: p57, p86, p91
  source_quote: |
    "SIP Gateway • The SIP gateway acts as an interface between the Call Handling and SIP proxy
    server" (p57)
    "SIP/ SIP Gateway->Review/Modify ... SIP Proxy Port Number: 5060" (p86)
  definition: |
    OXE 本地 SIP 网关：呼叫处理与 SIP 代理之间的接口，参数含 子网/中继组/角色 IP/主机名/端口
    5060（TLS 5061、MTLS 6261）/订阅时长/会话计时器/DNS 域名/SDP in 18x/CAC。是 SEPLOS 与
    SIP Device 共同的地基组件。
  alias_or_related: 六组件之一；sipgateway 命令输出其全景
  tags: [concept, sip-gateway, architecture]

- id: g05
  term: SIP Dictionary
  category: concept
  source_pages: p57, p88, p92
  source_quote: |
    "SIP Dictionary • Provides translation between PCX directory number and SIP URLs" (p57)
    "SIP DICTIONNARY, dim = 128, nb records = 1" (p92)
  definition: |
    PCX 分机号 ↔ SIP URL 的翻译表（容量 128 条记录口径见命令输出），重名用户（同姓名不同分机）时用
    alias 区分（DUPONT1/DUPONT2 例）。sipdict -l 查看条目（Type 2=Device、3=Extension）。
  alias_or_related: 与 g07 Location Server / g06 Proxy Server 协同完成寻址
  tags: [concept, dictionary]

- id: g06
  term: Proxy Server / Registrar Server / Location Server
  category: concept
  source_pages: p51-53, p57, p87-88
  source_quote: |
    "SIP Proxy • SIP messages routing • Controlling permissions • Possible interpretation and
    rewriting of SIP messages" (p51)
    "Registrar Server • In charge of collecting SIP terminal registration requests, and then of
    transmitting the data to the SIP location server • Location Server • Provides IP address from
    SIP URL" (p57)
  definition: |
    OXE SIP 三服务器（同栖 sipmotor 进程域）：Proxy（网内消息路由/权限/改写；参数含 Digest 认证、
    realm、防隔离框架）；Registrar（收注册、租期上下限 1800/86400s）；Location（URL→IP 注册库，
    sipregister 转储其内容）。B2BUA/Redirect Server/SBC/Gateway 为通用角色（p51），OXE 内主要以
    External SIP Gateway 声明对端。
  alias_or_related: sipmotor = SIP 引擎进程名（p57/p93）
  tags: [concept, proxy, registrar, location]

- id: g07
  term: Spatial redundancy / Internal name resolver
  category: concept
  source_pages: p58-59
  source_quote: |
    "Two different IP addresses are used for the role addressing • The 'node name' should be used to
    reach the SIP server • Management via the netadmin tool • This node name is resolved by the DNS
    feature implemented on the OmniPCX Enterprise: The internal name resolver" (p58)
  definition: |
    空间冗余接入机制：每台 CS 有物理 IP 与角色（role）IP；客户端一律用节点名（FQDN=节点名+域名）；
    OXE 内部域名解析器（netadmin 激活）+ 客户 DNS 委托，保证"只有 Main 以主用角色 IP 应答"。是冗余
    场景下 DM URL、SIP 注册统一的解析底座。
  alias_or_related: FQDN 构成规则见 p170；空间冗余下 DM URL 必须 FQDN（n10）
  tags: [concept, redundancy, dns]

- id: g08
  term: DM (Device Management) / DM profile
  category: concept
  source_pages: p144-153
  source_quote: |
    "'DM' application is in charge to provide to the SIP equipment's their configuration file and
    their binaries • 'DM' can be hosted either on the OmniPCX Enterprise or on the OmniVista 8770"
    (p71)
    "A SIP DM profile is assigned to each SIP user. The DM profile will adapt to the sub type of
    device to generate a compatible configuration file of settings" (p152)
  definition: |
    SIP 设备管理：向 SIP 终端下发配置文件与二进制的模块；OXE 自 N1 起自带（SIP DM on OXE），此前由
    OmniVista 8770 承担。DM profile 是按子型适配的参数模板（默认 0、上限 100），修改即对该 profile
    全部设备重生成配置并发 NOTIFY。管理开关=系统参数 "Device Management in 8770"。
  alias_or_related: 配置文件命名/下载认证见 g09；OXE/8770 分界见 counter-example n08
  tags: [concept, dm, provisioning]

- id: g09
  term: CTL
  category: concept
  source_pages: p151, p166, p171, p402, p408
  source_quote: |
    "Switch the device in factory configuration (to take into account the new OXE CTL)" (p151)
    "A CTL including another OXE's certificate than the default (generic) one must be used ... CTL
    directory: '/DHS3/data/mao/DM/VHE8082'" (p166)
    "200 OK (CTL file = RP CA cert, SBC CA cert,…)" (p402)
  definition: |
    话机侧证书信任列表文件（含 RP/SBC 的 CA 证书等），由 OXE DM 生成下发（目录 /usr3/mao/DM/VHE8082/
    或 /DHS3/data/mao/DM/VHE8082，文件 ctl_VHE8082、ict8000ctl.pem）。定制 OXE 证书后必须带新 CTL；
    远程话机经 RP 或 EDS 获取 CTL 完成信任链。
  alias_or_related: 与 g33 内部 PKI / g47 信任链条目联动
  tags: [concept, ctl, certificate]

- id: g10
  term: ALES-DUID
  category: concept
  source_pages: p115-117
  source_quote: |
    "a unique identifier (ALES-DUID) is sent by each ALES in any SIP request (RFC4122) • OXE stores,
    on the first REGISTER, the Directory Number / ALES-DUID association to monitor any attempt of
    parallel login" (p115)
  definition: |
    ALES 软终端在每条 SIP 请求里携带的唯一设备标识（RFC4122 UUID 口径）：OXE 以 分机号↔DUID 绑定实现
    一号多机互斥——非 REGISTER 消息带不同 DUID 即 403 Forbidden（Warning 399 Multiple Logins），可
    force 抢占，通话中禁抢，跨设备类型不互斥。
  alias_or_related: 行为细节见 counter-example n19
  tags: [concept, ales-duid, multi-login]

- id: g11
  term: Quarantine（隔离）
  category: concept
  source_pages: p87-88, p94, p227
  source_quote: |
    "A SIP equipment that sends more than 50 messages in 3 seconds is automatically added in this
    dynamic list. It stays in the list 30'" (p88)
    "Quarantined address: messages issue from these addresses are dropped automatically" (p88)
  definition: |
    SIP 代理的防攻击动态名单：3 秒 >50 条自动隔离 30 分钟（报文直接丢弃）；手工名单走 SIP/Quarantined
    IP Addresses，自动名单看 /usr4/tmp/sipalarm.log（f003 告警）；高频合法设备用 Trusted IP 白名单
    豁免。ALES 靠代理 Framework 参数（3s/50 条）避免误伤。
  alias_or_related: 规则细节见 principle p07
  tags: [concept, quarantine, security]

- id: g12
  term: ARS
  category: concept
  source_pages: p355-358, p332
  source_quote: |
    "Warning ARS IS REQUIRED TO USE SIP TRUNK GROUP WITH AN EXTERNAL SIP GATEWAY" (p355)
    "SIP trunk group choice according to the ARS Table ... Calling/Called number built according to
    the NPD of the TG" (p332)
  definition: |
    出局选路引擎：前缀（外线 0→逻辑判别器）→ 中继组关联外部网关 → ARS 路由表（删位/加位号码变换）→
    基于时间的路由清单（决定路由顺序）→ 实际判别器规则（位数）；逻辑↔实际判别器映射挂 entity（按
    部门差异化出局）。用外部网关的 SIP 中继组必须配 ARS。
  alias_or_related: 判别器=discriminator；变换规则见 principle p36
  tags: [concept, ars, routing]

- id: g13
  term: NPD / DID translation
  category: concept
  source_pages: p41, p359-361
  source_quote: |
    "The DID translation of your system must match your POD number." (p41)
    "Numbering Plan Description (NPD) ... Calling Numbering plan ident. NPI/TON ISDN International
    ... Default number (num. inst. sup) Enter the first DID number of your system" (p360)
  definition: |
    双向号码治理：DID 翻译把外线号段映射回内线（进向振铃定位），NPD 定义主/被叫号码计划（NPI/TON、
    国际标识）与默认号码（出向拼格式）；中继组 NPD 选择器绑定两者；回拨翻译表把显示号码整理成可回拨
    形式（A33→去 3 加 00）。
  alias_or_related: 回拨翻译（callback translator）并入本条
  tags: [concept, did, npd, numbering]

- id: g14
  term: Dual partition / Force Download NOE-SIP
  category: concept
  source_pages: p155, p187-194
  source_quote: |
    "For dual stack Deskphones, it is possible to switch the type of the device from NOE to SIP and
    vice versa" (p154)
    "Phone COS • Force download NOE/SIP: Yes/no" (p188)
  definition: |
    ALE-300/400/500/ALE-30 双栈双分区机制：话机同时持有 NOE 与 SIP 两套二进制，切换=换分区重启；
    Phone COS 参数 "Force Download NOE/SIP"=YES 时对侧二进制后台预载（快切），NO 则切换现场下载。
    R200 前出厂仅 NOE 分区。
  alias_or_related: 版本分界与耗时见 principle p27；切换限制见 n13/n14
  tags: [concept, dual-partition]

- id: g15
  term: Multi-devices
  category: concept
  source_pages: p134-137, p140
  source_quote: |
    "Main and Secondary (1 to 4) ... All devices ring in parallel on incoming call • An outgoing call
    initiated on any device is seen as a user call" (p134)
    "This feature is based on RFC3326 – 'The Reason Header Field ...' ... the 'Reason' is defined as
    'call completed elsewhere'" (p136)
  definition: |
    多终端组网：纯 SIP 型 1 主+最多 4 副（建议话机当主；ALES Windows/Mobile 各限一台）；混合型
    NOE 话机+DECT+ALES 最多 3 台（Virtual UA/REX/MIPT 不支持）。来话并振、任一终端外呼算用户呼叫；
    已接来电经 RFC3326 Reason 头（call completed elsewhere）同步，其他终端不计未接。
  alias_or_related: 寻线组联动行为见 p140；限制见 n23
  tags: [concept, multi-devices]

- id: g16
  term: Supervision key / Set supervision
  category: concept
  source_pages: p130-133
  source_quote: |
    "Supervision is configured by creating a supervision key for the supervisor." (p130)
    "Feature based on NOTIFY message ... OXE sends supervisees list information and their call
    status" (p132)
  definition: |
    SIP 侧监督机制：管理员给监督员配 Set Supervision 键（键号/被监督分机/振铃模式/No Call/Mnemo），
    机制基于 SUBSCRIBE/NOTIFY（四态：available/ringing/busy/out of service），支持代接与按键直呼；
    Keep Alive 超时产生 510-513 事件码。
  alias_or_related: 与 OXE 的 CSTA 监督是两套（SIP Device 不被 CSTA 监督）
  tags: [concept, supervision]

- id: g17
  term: Hunting group
  category: concept
  source_pages: p138-141, p239
  source_quote: |
    "Hunting groups with circular, cyclical and parallel search type can be configured with SIP
    equipment's" (p138)
    "Groups/Hunt Group Create ... Search Type Cicular or sequential" (p239)
  definition: |
    寻线组三型：circular（循环）/cyclical（顺序）/parallel（并行）。顺序/循环组支持 SIP/NOE 混装与
    多终端入组（tandem 联动）；并行组不可混装、多终端不可入。组呼叫不可转移、呼转/DND 不参与分配、
    离服成员不参与分配但保持登录。
  alias_or_related: 实验建组见 case c07 步骤 10
  tags: [concept, hunting-group]

- id: g18
  term: RCC (on SIP)
  category: concept
  source_pages: p142
  source_quote: |
    "Remote Call Control (RCC) on SIP SEPLOS devices • Prerequisite: SIP devices must include 'hold,
    talk and refer' in SIP header ... Legacy basic RCC remains available for SIP devices that don't
    comply with this" (p142)
  definition: |
    SIP SEPLOS 设备上的远程呼叫控制三档：legacy basic（不合头条件老设备仍可用）、enhanced basic
    （Make call 免压缩资源，前提 Phone COS 开 "Optimize resource 3PCC call"）、advanced（通话中业务
    全集：hold/retrieve/consultation/broker/conference/attended transfer 等，三方会议电路在 IMG）。
  alias_or_related: 与 Rainbow 语境的 RCC 同名不同域（本书记 ICE type/OmniTouch 关联）
  tags: [concept, rcc, 3pcc]

- id: g19
  term: Early media / Alert-Info URN
  category: concept
  source_pages: p300-303, p289
  source_quote: |
    "Early media: Refers to media (e.g., audio and video) that is exchanged before a particular
    session is accepted by the called user" (p300)
    "Called party is Free • urn:alert:tone:free is added in 180 (without SDP) message sent to caller"
    (p303)
  definition: |
    会话应答前交换媒体（回铃音/语音指南）的机制：两形态——SDP in 180（网关参数 SDP in 18x=True 时
    18X 期占压缩资源）与 SDP in 183 Session Progress；无 SDP 的 180 用 Alert-Info URN
    （urn:alert:tone:free / urn:alert:tone:busy）告知主叫侧本地放音，节省压缩资源。
  alias_or_related: DTMF 三法与 183 开媒体见 p305（principle p32）
  tags: [concept, early-media, sdp]

- id: g20
  term: auto-discovery
  category: concept
  source_pages: p157-158, p183-184, p212
  source_quote: |
    "If the configuration file does not exist ... The OXE answers with '401' (authentication
    requested) • Auto-discovery mode is required" (p157)
    "the set will start in Auto-discovery mode requiring: The username: Directory number of the user
    • The password: Secret code from the user (by default 0000)" (p183)
  definition: |
    话机"零登记"入网方式：OXE 库里无该 MAC 的配置文件时，话机被 401 触发认证流程——提交 分机号+
    用户密码码（默认 0000）+MAC+机型（USER AGENT），OXE 校验后回写 MAC/子型、即时生成配置并发
    200 OK。ALES 无此机制（login 必须预建）。
  alias_or_related: 与 MAC 手工绑定二选一；细节见 principle p26
  tags: [concept, auto-discovery]

# ── 二、角色/账号 (role) ──

- id: g21
  term: mtcl / swinst / root（CS 系统账号）
  category: role
  source_pages: p62, p91-94, p169, p225, p238, p242
  source_quote: |
    "On the CS : login as 'mtcl' Enter 'netadmin -m' command" (p62)
    "Log as swinst Choice 2: Expert menu" (p225)
    "To configure auto-generated server certificates ... you must log on as 'root'" (p169)
  definition: |
    OXE 三个运维账号分工：mtcl=维护与查询（netadmin 只读/多数 CLI：sipregister/trkstat/sipgateway/
    sipdict/compvisu/motortrace/oxetrace/sipdump）；swinst=软件与系统管理菜单（Expert→System
    management：认证/账户/nginx 重配）；root=高权限（su 切换：PKI 证书生成、SSL 级别、check_ales_
    ldap、killall）。实验口令 Superuser2580*（实验口径）。
  alias_or_related: admin/Superuser 等其他实例口令见 p9 Settings 表（实验口径）
  tags: [role, accounts, cli]

- id: g22
  term: Supervisor / supervisee
  category: role
  source_pages: p130-131
  source_quote: |
    "ALE SoftPhone, ALE-30 and ALE-300/400/500 SIP Deskphones support OXE SIP Supervision (as
    supervisor) • Only SIP devices can be supervised by another SIP device."
  definition: |
    监督关系两端：监督员持监督键（至多 40 键）可监视状态/代接/直呼；被监督人（supervisee）状态经
    NOTIFY 推送。仅 SIP 设备可被 SIP 设备监督；iPhone 无监督端。
  alias_or_related: 事件码与容量见 principle p15
  tags: [role, supervision]

- id: g23
  term: UAC / UAS / B2BUA
  category: role
  source_pages: p51
  source_quote: |
    "UA: User Agent • UAC: User Agent Client -> element generating the SIP request (caller) • UAS:
    User Agent Server -> An element responding to a SIP request (called) ... B2BUA: Back-To-Back User
    Agent • Receives one request as a UAS and returns another as a UAC • Difference with a proxy: 2
    separate communications"
  definition: |
    SIP 实体角色三件：UAC=发请求方（主叫）、UAS=应答方（被叫）、B2BUA=两侧各扮一角且两段会话独立
    （与 proxy 的本质区别）。ITSP 侧的 SBC/网关常以 B2BUA 形态出现（书中 ITSP2 报文 Call-ID 带
    _b2b-1 踪迹）。
  alias_or_related: 其余角色（Redirect/Proxy/SBC）见 f09
  tags: [role, sip-entities]

# ── 三、产品/组件 (product) ──

- id: g24
  term: OmniPCX Enterprise (OXE)
  category: product
  source_pages: p1, p29-31, p56-59, p68
  source_quote: |
    "OMNIPCX ENTERPRISE - R101.1 MD4 SIP - EDITION 12 PARTICIPANT'S GUIDE" (p1)
    "The OmniPCX Enterprise is designed to support the Session Initiation Protocol (SIP) • SIP
    terminals integration in the PCX environment • Interconnection with SIP carriers, SIP
    applications" (p56)
  definition: |
    本书的宿主 PBX：ALE 企业级通信系统，本册教其 SIP 化——SIP 终端接入（SEPLOS/Device）、SIP 承载
    （运营商/应用）、SIP 设备管理、SBC 与远程办公。版本口径 R101.1 MD4（截图混 R100.0/R101.0/
    R101.1，见 n51）。
  alias_or_related: CS/Call Server/Communication Server 同指其呼叫服务器；OMS 为其管理服务器侧
  tags: [product, pbx, core]

- id: g25
  term: OMS CSA / OXE CSA
  category: product
  source_pages: p7, p9
  source_quote: |
    "OXE CSA ENTP_OXE_CSA_SIP csa (physical) csm (main) 192.168.1.1 192.168.1.3" (p9)
    "OMS CSA ENTP_OMS_CSA_CSB_NODE_1 192.168.1.13" (p9)
  definition: |
    实验两台核心虚机：OXE CSA=通信服务器（物理 IP 192.168.1.1，主用角色 IP 192.168.1.3，主机名
    csa/csm）；OMS CSA=管理服务器节点（192.168.1.13，同为 OMS 拓扑里的 Virtual GD4）。实验口径。
  alias_or_related: 账号表见 f02；csm/maincpu 别名见 /etc/hosts 输出（p350）
  tags: [product, lab-口径, vm]

- id: g26
  term: ALES (ALE SoftPhone)
  category: product
  source_pages: p106-121, p217-270
  source_quote: |
    "ALE SoftPhone is a SIP Softphone application for Windows PC, Android Smartphone, iPhone and IPad
    ... SIP+ from Omni PCX Enterprise Purple ... Compatibilities OXE DM only (not 8770 DM) OXE
    Purple only No OXO, no OXE <R100 Purple" (p107)
  definition: |
    ALE 软终端三平台（Windows/Android/iOS）：SIP+（Purple 起）、SBC/RP 或 VPN 远程、微软集成
    （Azure AD/Outlook/O365/LDAP）、寻线组/监督/CCD/多终端/按名呼叫/P2P 视频。管理仅 OXE DM；安装包
    ALESoftPhone-x.x.xxx.xxx.msi；移动端走 Play Store/App Store。
  alias_or_related: 子型名 ALES-desktop / ALES-mobile（用户 Sub type）
  tags: [product, ales, softphone]

- id: g27
  term: ALE-2 / ALE-3（Basic Deskphones）
  category: product
  source_pages: p70, p99, p172-186, p402, p412
  source_quote: |
    "ALE-2/ALE-3 DESKPHONES - OVERVIEW ALE SIP stack, in Business mode only (no attendant, no CC
    agent, no hotel) ... Native encryption (SIP TLS, SRTP) Remote access (RP/SBC, VPN)" (p99)
    "ALE-2, ALE-3 SIP basic Deskphones embed a VPN client ... only support OpenVPN, not IPSec VPN"
    (p412)
  definition: |
    基础型 SIP 话机：仅 Business 模式、原生加密、可远程（RP/SBC 或内嵌 VPN）；功能矩阵 1000 条本地
    日志、8/12 个可编程键（OXE DM 内）、监督仅监督员角色、寻线组降级。DHCP 类 ALE-2X（VCI
    aledevice）。不能 LAN↔WAN 动态搬迁（须先换专用 DM profile）。
  alias_or_related: 8008 为 Essential 档特例（Business&hotel）
  tags: [product, deskphone]

- id: g28
  term: ALE-30 / ALE-x00 (ALE-300/400/500)
  category: product
  source_pages: p100-105, p187-216
  source_quote: |
    "ALE-30 in SIP mode supports 1 EM-200 add-on module." (p100)
    "ALE-x00 Deskphones are NOE/SIP dual stack equipment" (p188)
  definition: |
    Essential 档 ALE-30（SIP 模式支持 1 个 EM-200 扩展模块，亦双栈）与企业档 ALE-300/400/500（双栈
    双分区、NOE↔SIP 可切、最多 3 个 ALE-120 扩展模块、ALE-108 无线/蓝牙）：SIP+（Purple 起）、新
    GUI（Dashboard/拖拽按键/音频选择器）、120 可编程键（5 页×24）、按键集中存储、监督/寻线组全量。
    DHCP 类 SIP80x8s（VCI ictouch.0）。
  alias_or_related: SIP 模式不支持清单（Audio Hub/VPN 客户端/skinify 等）见 p105
  tags: [product, deskphone]

- id: g29
  term: 8008 / 8008G / 8088
  category: product
  source_pages: p70, p98, p147
  source_quote: |
    "8008/8008G DESKPHONES - OVERVIEW ALE SIP stack, in Business & hotel mode (no attendant, no CC
    agent)" (p98)
    "Support existing SIP phones : 8088 Hotel or Huddle Room, 8008 ..." (p147)
  definition: |
    Essential 档 8008/8008G：Business+酒店模式（无话务员/坐席），可由 OXE DM 管理（与 ALE-x 同批）；
    8088（Huddle Room/酒店）仅 8770 DM 支持。8088 V3 出现在 SEPLOS 终端谱系图（SIP 或 NOE IP）。
  alias_or_related: 酒店模式在 SIP 侧的全系缺席见 n26
  tags: [product, deskphone]

- id: g30
  term: IPDSP (IP Desktop SoftPhone)
  full_name: IP Desktop Softphone（书中 p39 写法 IP DSP）
  category: product
  source_pages: p7, p16, p39-40, p113
  source_quote: |
    "Install and bring into service the IPDSP softphones as mentioned in the table below ... 'IPDSP'
    software is available in the NAS." (p39)
    "31000 Brad Barkley IP DSP Installed on PC Client 10" (p39)
  definition: |
    ALE 的 IP 桌面软话机：实验中替代物理话机（虚拟课堂无实物）；装机后在 Settings/Network 填 TFTP
    Server Main=OXE CS Main IP（192.168.1.3）。属 IP 用户计数的一部分（p68 容量口径）。
  alias_or_related: 对照 g31 MicroSIP（模拟公网/第三方）
  tags: [product, softphone, lab-口径]

- id: g31
  term: MicroSIP
  category: product
  source_pages: p10, p19, p22-23, p90
  source_quote: |
    "On PC Client 10: 2 MicroSIP softphones are installed to simulate public numbers." (p10)
    "Configure and launch the 'MicroSIP' softphone. Don't forget to specify the user SIP password"
    (p90)
  definition: |
    第三方 SIP 软话机客户端：实验里既用于模拟 ITSP1 的公网/紧急用户（Public/Urgence 两档 profile），
    也用于当 SIP Device 终端（31060，填 SIP 密码注册）。其 SDP 编解码清单固定（对照 ALES 可配置）。
  alias_or_related: 纯教学基础设施
  tags: [product, softphone, lab-口径]

- id: g32
  term: OTSBC
  category: product
  source_pages: p336-345, p364-383, p421-449
  source_quote: |
    "Mediant SW> enable ... Welcome to AudioCodes CLI" (p345)
    "Welcome to AudioCodes CLI Username: Admin Password:" (p366)
  definition: |
    ALE 的会话边界控制器（AudioCodes Mediant 平台底座，缩写书中未展开）：SIP trunking 与远程办公
    两大场景的承载——NAT 穿越编解码转换消息/号码改写媒体加密，内嵌反向代理（≤500 远程用户）。部署
    OVF/ISO（MyPortal），CLI Admin/Admin（实验口径），Web 向导配置。
  alias_or_related: SBC 概念角色见 g23/f09；RP 功能见 g44
  tags: [product, sbc]

- id: g33
  term: Internal PKI（OXE 内部证书机构）
  category: product
  source_pages: p168-171
  source_quote: |
    "Activate the internal root CA, embedded in the OXE Create a self-signed root CA certificate
    Create a call server certificate, signed by the root CA" (p169)
  definition: |
    OXE 内嵌的证书机构能力：netadmin（root）→ 11/9/1 一键生成根 CA + CS 密钥对 + CSR + CS 证书
    （SAN 含 FQDN/通配/物理与角色 IP，密钥默认 4096 位），并产出话机用 CTL。安装默认证书只适配
    WBM/HTTPS，不适配 SIP 客户端——SIP 化必须走内部 PKI 或外部 CA 定制。
  alias_or_related: 外部 CA 同样支持；OpenSSL 安全级见 principle p23
  tags: [product, pki, certificate]

- id: g34
  term: EDS (Easy Deployment Server)
  full_name: Easy Deployment Server（书中展开）
  category: product
  source_pages: p401, p404-406
  source_quote: |
    "'EDS' is an ALE cloud server that allows the deployment of deskphones in remote worker
    situation • ALE EDS cloud service is hosted by Amazon Web Service data center in Paris, France"
    (p401)
    "FQDN hardcoded in phones: device.eds.al-enterprise.com" (p405)
  definition: |
    ALE 云端零touch 部署服务器（AWS 巴黎、冗余、加密）：出厂话机（无 DM URL）起步即联系它——切
    SIP 模式、下发 RP FQDN 与 RP 根证书（Profile 三要素：DM URL/证书/预配置区）。管理入口
    admin.eds.al-enterprise.com（开户 /register）。
  alias_or_related: 零touch 四限制见 n37；EDS GUI 见 p406
  tags: [product, eds, cloud]

- id: g35
  term: NGINX / NGINX PLUS
  category: product
  source_pages: p157-160, p165-166, p387
  source_quote: |
    "the device asks its configuration file to 'NGINX' server of the OXE" (p157)
    "If more, ALE recommends NGINX PLUS reverse proxy delivered by NGINX company, member of DSPP"
    (p387)
  definition: |
    两个角色：OXE 内嵌 NGINX 组件——Web 服务与 DM 下载通道（443；R101.1 起增设 8443 mTLS 实例；
    access.log 是 DM/二进制排障入口）；NGINX PLUS——>500 远程用户时 ALE 推荐的反向代理（DSPP 成员
    产品）。
  alias_or_related: swinst 可重配并重启 nginx（认证变更时）
  tags: [product, nginx, reverse-proxy]

- id: g36
  term: OmniVista 8770（8770 DM / 8770 Server / 8770 User）
  category: product
  source_pages: p71, p146-150, p174
  source_quote: |
    "'DM' can be hosted either on the OmniPCX Enterprise or on the OmniVista 8770" (p71)
    "Choice of DM is done through an OXE system option ('Device Management in 8770')" (p148)
  definition: |
    ALE 管理/应用平台，传统上承担 SIP 设备管理：8770 DM 集中管理跨节点话机（含已停产 8001/8018/
    8028s 与 8088 酒店）；OXE N1 起与 OXE DM 并存，开关=系统参数。关 8770 DM 会删其配置文件（n08）。
  alias_or_related: 混合拓扑=话机留 8770、ALES 归 OXE（p149）
  tags: [product, dm, management]

- id: g37
  term: OXE-MS（媒体资源）
  category: product
  source_pages: p276, p281
  source_quote: |
    "OXE-MS is required to provide media services (e.g., transcoding, conference, voice guides) with
    OPUS or G.722 codecs" (p276)
    "So, OXE-MS are ranked first in the list, as supporting OPUS and G.722" (p281)
  definition: |
    OPUS/G722 时代的媒体服务资源（转码/会议/语音指南的承载者）：编解码资源分配动态列表中被排最前
    （同域优先，跨域按负载）。全 OPUS/G722 组网必须核算其容量。
  alias_or_related: 对照不支持 G722/OPUS 的 GD3/GD4/INTIP3 等（p276）
  tags: [product, media, resources]

- id: g38
  term: GD4 / Virtual GD4 / MIX484
  category: product
  source_pages: p16, p38
  source_quote: |
    "Software Rack 3U (OMS) Rack N° 4 Virtual GD4 (slot 0) IP @: 192.168.1.13/24" (p38)
    "Hardware Rack 1U Rack N° 2 GD4 (slot 0) IP @: 192.168.1.12/24 ... MIX484 (slot1)" (p38)
  definition: |
    实验机架/板卡组件：软件机架 3U（OMS，机架 4）里的 Virtual GD4（192.168.1.13）；混合模式另有
    硬件机架 1U（机架 2）的 GD4（192.168.1.12）+ MIX484 板（供课堂物理话机）。GD 系编解码资源不支
    持 G722/OPUS（p276）。
  alias_or_related: 实验口径
  tags: [product, hardware, lab-口径]

- id: g39
  term: FlexLM Server
  category: product
  source_pages: p7, p9, p38
  source_quote: |
    "FLEXLM SERVER ENTP_FLEXLM flex 192.168.1.80 255.255.255.0 192.168.1.254 root letacla1" (p9)
    "FlexLM Server (192.168.1.80) is declared" (p38)
  definition: |
    实验许可服务器（FlexLM 192.168.1.80，账号 root/letacla1，实验口径）：OXE 预配置已声明它；CC-
    suite-ID 等许可信息与其关联（证书生成时 CC-suite-ID 取自许可文件，p170）。
  alias_or_related: 许可读数现场核对见 sipdump（principle p34）
  tags: [product, licensing, lab-口径]

- id: g40
  term: LDAP Explorer Tool
  category: product
  source_pages: p219-224, p264-270
  source_quote: |
    "The software, ldapexplorertool.exe, is available in the NAS (see below), reachable from the PC
    client." (p219)
  definition: |
    实验用 LDAP 目录浏览器（NAS 提供）：File/Configurations 新建连接（Server IP、User DN=cn=admin,
    dc=aletraining,dc=com、Base DN=ou=users,dc=aletraining,dc=com、口令 superuser，实验口径），核对
    ALES 用户的 uid/telephoneNumber/cn/userPassword 属性——建 ALES 用户前核对 login 对应关系的
    可视化工具。
  alias_or_related: 生产排障用 check_ales_ldap 命令（root）
  tags: [product, ldap, lab-口径]

# ── 四、协议/技术 (protocol) ──

- id: g41
  term: SDP
  full_name: Session Description Protocol（书中展开）
  category: protocol
  source_pages: p48, p86, p289, p300-303
  source_quote: |
    "Media characteristics are described by the SDP (Session Description Protocol) • RTP port, RTCP
    port • Audio codecs , Video codec" (p48)
    "SDP in 18x: allows to send the SDP information in the 'ringing' frame instead of sending them
    only on the '200 OK' frame" (p87)
  definition: |
    媒体描述协议：在 SIP 信令里携带 RTP/RTCP 端口与编解码清单；SDP in 18x 参数决定 180 Ringing 是否
    带 SDP（早媒体与压缩资源占用的开关，True 时 ISDN in-band 指南可被 SIP 侧听到）。
  alias_or_related: 与 g19 Early media / g20 Alert-Info URN 配合
  tags: [protocol, sdp]

- id: g42
  term: RTP / RTCP / SRTP
  category: protocol
  source_pages: p45, p48, p99, p289, p337
  source_quote: |
    "Media negotiation (codecs) but not the transport ... SIP RTP Codecs"（协议栈图，p45）
    "Native encryption (SIP TLS, SRTP)" (p99)
    "Managing and securing SIP sessions and the media streams (audio and video) based on RTP or SRTP
    (encrypted media streams)" (p337)
  definition: |
    媒体传输与加密：RTP 承载音视频、RTCP 为其控制伴生协议；SRTP 为加密媒体流——SEPLOS 原生加密与
    SBC 媒体安全（AES-CM-128-HMAC-SHA1-80）的落点；SEPLOS 省资源设计目标是"直连 RTP 尽可能多"。
  alias_or_related: 两个缩写书中未展开全称（RTP 按惯例理解，未采信外部补全）
  tags: [protocol, rtp, srtp]

- id: g43
  term: TLS / SIPS / mTLS
  category: protocol
  source_pages: p48, p99, p159-160, p337, p408-410
  source_quote: |
    "SIP signaling can be protected by the TLS protocol" (p48)
    "to strengthen Deskphone authentication, mutual authentication (mTLS) is enabled during TLS
    handshake ... a new instance is launched on port 8443, dedicated to OXE DM, on which mTLS is
    mandatory" (p159)
  definition: |
    传输安全三件：TLS 保护 SIP 信令（TLS 端口 5061）；mTLS=双向证书认证（OXE DM 8443 下载、话机↔RP、
    话机↔EDS）；SIPS=信令加密的 SIP URI 形态（远程办公拓扑图中的 SIPS/SRTP 标注）。SBC 与 RP 的
    证书链必须进终端信任库（经 CTL/EDS）。
  alias_or_related: 缩写书中未逐一展开全称
  tags: [protocol, tls, mtls]

- id: g44
  term: Reverse Proxy（反向代理）
  category: protocol
  source_pages: p388-395, p421-435
  source_quote: |
    "Reverse Proxy Takes into account requests from Internet and forwards them to servers in an
    internal network ... Main advantages: Security and anonymity" (p388)
    "HTTPS Listening Port 443 ... URL Pattern /DM/dmsoftphone/" (p434-435)
  definition: |
    远程办公的入口组件：把互联网侧请求转发到内网（OXE DM），提供安全匿名、公网 IP 复用、隐藏内网
    FQDN/IP、代理层认证、URL 改写/封禁、负载均衡等；≤500 用户可用 OTSBC 内嵌实现（HTTP PROXY 菜单：
    Upstream Groups/HTTP Proxy Servers/HTTP Locations），更多用 NGINX PLUS。
  alias_or_related: 外部认证时 RP 与 OXE DM 须同源 LDAP（p395）
  tags: [protocol, reverse-proxy]

- id: g45
  term: NOE
  category: protocol
  source_pages: p39-40, p67, p135, p154
  source_quote: |
    "31010 Charles Cooper ALE-500 (IP NOE)" (p40)
    "Mixed SIP/NOE configuration is supported for sequential and cyclical hunting group" (p140)
  definition: |
    ALE 话机的传统 IP 协议栈（书中作为 SIP 的对照系与共存系，缩写未展开全称）：ALE-x00 为 NOE/SIP
    双栈、可互切；寻线组/多终端支持 NOE-SIP 混装（并行组除外）；NOE 设备用 VCI alcatel.noe.0。
  alias_or_related: 与 SIP 的选择即 g02/g03 形态决策的底层
  tags: [protocol, noe]

- id: g46
  term: ABC-F / DPNSS
  category: protocol
  source_pages: p85, p89, p276
  source_quote: |
    "Protocol type: must be ABC for the SIP trunk group used for the private traffic" (p85)
    "Local Features PCX address in DPNSS ... it is necessary to manage one different DPNSS prefix on
    each node of the ABC network" (p89)
  definition: |
    私网/网络侧协议域：ABC-F 为私网路由与私有 SIP 中继组的协议类型（编解码矩阵中 ABC-F IP 中继支持
    OPUS SWB 全档、Hybrid Link 模式不支持）；DPNSS 为节点间信令（转移优化前缀 A31999 挂 DPNSS PCX
    地址；每节点需不同前缀）。两缩写书中未展开全称。
  alias_or_related: Direct Link（直连链路）为 ABC-F 网的直连模式（编解码决策层之一）
  tags: [protocol, abc-f, dpnss]

- id: g47
  term: LDAP / LDAPS
  category: protocol
  source_pages: p110-111, p152, p225-226, p395
  source_quote: |
    "In that case, an external LDAP server is required to authenticate users • Configurated in the
    OXE swinst menu ldap / ldaps" (p110)
    "The reverse proxy and the OXE device management must have the same external LDAP server for
    their authentication." (p395)
  definition: |
    目录服务双用途：①ALES 登录认证（swinst 配置：主机/端口 389/636、Scheme ldap:///ldaps://、
    Search Base DN、Login attribute=uid、Bind DN/密码）；②目录搜索（DM profile 里配 LDAP URL 供
    话机/软终端查号）。远程办公时 RP 与 OXE DM 须指向同一外部 LDAP。
  alias_or_related: check_ales_ldap 为认证链路排障命令
  tags: [protocol, ldap]

- id: g48
  term: DTMF（三法）
  category: protocol
  source_pages: p305, p86
  source_quote: |
    "the DTMF exchange can be done with three methods • 'Out of band' (RFC 4733): each digit is sent
    in RTP flow with a specific payload negotiated with SDP • 'Info': each digit is sent in an 'info'
    message acknowledged by a '200 OK' • 'In band': each digit is sent inside the RTP flow ... The
    configuration of the DTMF method is done via the DM profile" (p305)
  definition: |
    双音多频传递三法：RFC4733（RTP 内载荷，SDP 协商 payload，如 101）、SIP INFO（逐位消息+200 OK
    确认）、带内（音频内）；方法在 DM profile 配置。业务前缀激活时 CS 以 183+SDP 开 RTP 收 DTMF。
  alias_or_related: SIP payload 101 为本地网关 DTMF 载荷默认（p91）
  tags: [protocol, dtmf]

- id: g49
  term: TFTP / DHCP option 66-67 / VCI
  category: protocol
  source_pages: p39, p151, p181-182, p204, p214
  source_quote: |
    "In case of external DHCP server, option 66 provides the DM URL (https://OXE Main IP @/dmictouch)"
    (p151)
    "ADD THE NEW DHCP OPTION 67 WITH THE 'SIPCONFIG.TXT' KEYWORD" (p214)
    "use a Vendor Class ID (VCI) called 'ictouch.0'" (p204)
  definition: |
    终端引导三件：TFTP Server 地址字段实为 DM 的 HTTPS URL（https://<OXE Main IP|FQDN>/dmictouch）；
    外部 DHCP 用 option 66 下发该 URL、option 67 下发 sipconfig.txt（NOE 批量切 SIP 的 boot file）；
    VCI（Vendor Class ID）区分终端族——aledevice（ALE-2/3）、ictouch.0（ALE-x00/SIP80x8s）、
    alcatel.noe.0（NOE）。
  alias_or_related: 类与 VCI 对照表见 principle p25
  tags: [protocol, dhcp, tftp, vci]

- id: g50
  term: CAC
  category: protocol
  source_pages: p80, p86, p337, p354
  source_quote: |
    "The IP address is used to assign the SIP set to an IP Telephony Domain and to handle features,
    such as Call Admission Control (CAC)" (p80)
    "CAC SIP-SIP: used to check or not the IP domain right in case of SIP to SIP calls" (p87)
  definition: |
    呼叫准入控制：注册 IP 决定终端归属的 IP 电话域（带宽档位随之确定）；本地网关的 CAC SIP-SIP 参数
    决定 SIP-SIP 呼叫是否校验 IP 域权限（开=只许域内算法定义的能力，禁 SDP 里的视频/数据）；SBC 侧
    亦有拥塞限呼。
  alias_or_related: 与 IP 域高/低带宽共同决定编解码（principle p31）
  tags: [protocol, cac]

- id: g51
  term: RFC 3261 / RFC 3325 / RFC 3326 / RFC 4122 / RFC 4733
  category: protocol
  source_pages: p45, p136, p115, p305, p354
  source_quote: |
    "IETF Standard: RFC 3261" (p45)
    "This feature is based on RFC3326 – 'The Reason Header Field for the Session Initiation Protocol
    (SIP)'" (p136)
    "a unique identifier (ALES-DUID) is sent by each ALES in any SIP request (RFC4122)" (p115)
    "'Out of band' (RFC 4733): each digit is sent in RTP flow" (p305)
    "RFC 3325 supported by the distant: P_Asserted_Identity supported (outgoing calls)" (p354)
  definition: |
    书中点名的五个 RFC：3261（SIP 基线）、3325（P-Asserted-Identity 私网扩展——外部网关按对端支持
    决定 From 匿名形态）、3326（Reason 头——多终端"他端已接"同步）、4122（UUID——ALES-DUID）、
    4733（RTP 电话事件载荷——DTMF out-of-band）。
  alias_or_related: 其余 RFC 书中未点名
  tags: [protocol, rfc]

# ── 五、实验资源 (resource) ──

- id: g52
  term: RLAB / POD
  category: resource
  source_pages: p5-9, p14-19
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a
    data center ... Pods are independent of each other Pods have the same configuration Pods have
    access to common resources" (p5)
    "Pod P (P is the POD number)" (p22)
  definition: |
    ALE 培训远程实验室：按 POD 划分的同构实验单元（全虚拟化或混合模式两种），POD 间独立、共享公共
    资源（NAS、SIP 模拟器、邮件服务器）；POD 号（N/PN/P）嵌入全部实验号码与账号。教学专用基础设施。
  alias_or_related: 拓扑与账号表见 f02/f03
  tags: [resource, lab, training]

- id: g53
  term: ITSP1 / ITSP2（SIP Carrier Simulator）
  category: resource
  source_pages: p21-34
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... SIP domain: sip.itsp1.fr" (p22)
    "ITSP2 SIP Gateway gateway.itsp2.com 10.20.30.60 ... SIP domain: sip.itsp2.fr" (p30)
  definition: |
    培训专用 SIP 运营商模拟器（RLAB 公共区托管）：ITSP1 直连腿（网关 10.20.30.51 + 公网网关
    10.20.30.50，账号 pbxP/alcatel，公网/紧急用户经 2 个 MicroSIP）；ITSP2 经 SBC 腿（网关
    10.20.30.60，账号 podP/alcatel，sip.itsp2.fr）。号码规则嵌 POD 号；与真实运营商行为有差异（n45）。
  alias_or_related: 号码变换规则见 f04/f05
  tags: [resource, simulator, lab-口径]

- id: g54
  term: ITServer（NTP & LDAP 服务器）
  category: resource
  source_pages: p7, p9, p110, p219
  source_quote: |
    "IT SERVER ENTP_ITSERVER itserver 192.168.1.252 ... training superuser NTP & LDAP Servers" (p9)
    "For the lab, we are going to use an Open LDAP server installed on a VM called 'ITServer'" (p219)
  definition: |
    实验基础设施机（192.168.1.252）：NTP 与 OpenLDAP 合一——OXE 预配置声明其为 NTP；ALES 外部认证与
    目录搜索均指向它（389 端口、Base DN ou=users,dc=aletraining,dc=com，实验口径）。DM profile 的
    SNTP 也指向它。
  alias_or_related: 生产中 NTP/LDAP 为独立工程（BOOK_OVERVIEW 批判）
  tags: [resource, lab-口径, ldap]

- id: g55
  term: MyPortal
  category: resource
  source_pages: p144-145（OTSBC/OVF 语境）, p405
  source_quote: |
    "On MyPortal web site, you can find the software for OTSBC deployment." (p365)
  definition: |
    ALE 客户服务门户（书中用于获取 OTSBC 部署软件等资源；缩写/全称书中未展开）。
  alias_or_related: 与远程办公部署指南（TC2957）同属支持资源体系
  tags: [resource, portal]

- id: g56
  term: TC2005 / TC2957（技术通报引用）
  category: resource
  source_pages: p349, p411
  source_quote: |
    "PLEASE CONSULT THE DOCUMENTS (TC 2005, AND ADDITIONAL ONE…) GIVEN BY ALE OR THE PUBLIC OPERATOR
    TO CONFIGURE THE SIP GATEWAY AS EACH OPERATOR HAS ITS OWN SPECIFIC PARAMETERS" (p349)
    "As described in 'TC2957 Quick steps deployment guide for ALE SoftPhone Remote Worker
    configuration'" (p411)
  definition: |
    书中点名的两份 ALE 技术文档：TC2005=运营商 SIP 网关参数依据（与运营商附加文档并列）；TC2957=
    ALE SoftPhone 远程工作者快速部署指南（OTSBC 侧 SIP/媒体配置以其为准）。生产化的两大外置依据。
  alias_or_related: 另有 Server deployment Guide for Remote workers（VPN 网关清单，p412）与 EDS user
    manual（p405）
  tags: [resource, document, tc-series]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列候选术语逐条核对

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| SIP | 有明确定义（p45-48） | g01 |
| SEPLOS (SIP Extension) | 有明确定义（p66） | g02 |
| SIP Device | 有明确定义（p66/p77） | g03 |
| DM / DM profile | 有明确定义（p71/p152） | g08 |
| CTL | 有定义性用法与产物（p151/p166/p171），缩写未展开全称 | g09（full_name 如实省略） |
| ALES | 有明确定义（p107） | g26 |
| ALES-DUID | 有明确定义（p115） | g10 |
| OTSBC (SBC) | 有明确定义（p336-338）；缩写未展开全称 | g32（full_name 如实省略） |
| EDS | 有明确定义（p401） | g34 |
| ARS | 有定义性用法与完整配置链（p355-358），缩写未展开全称 | g12（full_name 如实省略） |
| NPD / DID 翻译 | NPD 有全称（Numbering Plan Description，p360）；DID 缩写未展开 | g13 |
| 空间冗余 | 有明确定义（p58-59） | g07 |
| Quarantine | 有明确定义（p88） | g11 |
| ITSP1/ITSP2 | 有明确定义（p22/p30） | g53 |

结论：**14 行全部"本书正文有定义/用法锚点"，无"书中实际未出现"项；CTL/OTSBC/ARS/DID 四个缩写书中未给全称，已如实省略，未编造。**

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：SIP Gateway（g04）、SIP Dictionary（g05）、三服务器（g06）、Dual partition（g14）、Multi-devices（g15）、Supervision key（g16）、Hunting group（g17）、RCC（g18）、Early media/Alert-Info（g19）、auto-discovery（g20）
- 角色/账号：mtcl/swinst/root（g21）、supervisor/supervisee（g22）、UAC/UAS/B2BUA（g23）
- 产品：OXE（g24）、OXE CSA/OMS CSA（g25）、ALE-2/3（g27）、ALE-30/ALE-x00（g28）、8008/8088（g29）、IPDSP（g30）、MicroSIP（g31）、内部 PKI（g33）、NGINX/NGINX PLUS（g35）、OmniVista 8770（g36）、OXE-MS（g37）、GD4/MIX484（g38）、FlexLM（g39）、LDAP Explorer Tool（g40）
- 协议/技术：SDP（g41）、RTP/RTCP/SRTP（g42）、TLS/SIPS/mTLS（g43）、Reverse Proxy（g44）、NOE（g45）、ABC-F/DPNSS（g46）、LDAP/LDAPS（g47）、DTMF 三法（g48）、TFTP/DHCP option/VCI（g49）、CAC（g50）、五个 RFC（g51）
- 资源：RLAB/POD（g52）、ITServer（g54）、MyPortal（g55）、TC2005/TC2957（g56）

### 3. 仅 passing 提及、未单列条目的词（备查）

SIP URL（p48，并入 g01）、B2BUA/UAC/UAS（p51，g23 已单列角色条；Redirect/Proxy 角色并入 f09）、DSPP（p67/p387，开发者伙伴计划，仅两处提及未展开）、PCS（p98/p107/p125，仅出现在兼容性标注，未定义）、REX/Virtual UA/MIPT（p135，多终端不支持清单点名）、CCD（p72/p108，坐席能力点名）、OT（p354，OmniTouch 环境提法）、ICE type（p354，网关类型值）、P-Alcatel-CSBU / P-CAC-ALU（p48/p354，私有 SIP 头）、urn:alert:tone:free/busy（p303，并入 g19）、doorcam（p76，SIP Device 例）、EM-200/ALE-120/ALE-108（p100，扩展硬件点名）、EM-200 所属 ALE-30 口径见 g28、RUFUS/Filezilla/Wireshark（工具名，case 内出现）、Guacamole（p241，实验桌面限制）、AudioCodes Mediant（p345/p366，OTSBC 的 CLI 平台名，并入 g32）、Rainbow WebRTC Gateway（p56/p276，全景图与编解码矩阵点名，本书无展开）、Amazon Web Service（p401，EDS 宿主，并入 g34）、OpenVPN（p412，并入 n40/g27）、Enterprise-education.csod.com（p461，培训评估站，行政内容未入册）。

### 4. 提取口径说明

- 所有定义只采信本书正文；SEPLOS（书中给全称 SIP End Point Level of Services）、NPD（Numbering Plan Description）、EDS（Easy Deployment Server）、IPDSP（IP Desktop Softphone 拼写见 p39/p113）按原文收录；CTL、OTSBC、ARS、DID、NOE、ABC-F、DPNSS、REX、PCS、CAC、CSTA、MLA、DSPP、OT、TFTP 等书中未给全称者 full_name 省略，不做外部补全。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准；引用均为原文摘录（p358 "EXISITING"、p239 "Cicular" 等原文笔误保留并注明）。
