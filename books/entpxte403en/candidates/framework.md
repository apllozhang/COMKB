# 框架/流程/结构候选 — OmniPCX Enterprise SIP (ENTPXTE403EN R101.1 MD4 Ed12)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、机制时序。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——环境地基 → 协议底座 → 终端侧 → 运维工具 → 出口（外线+远程）
  type: flow
  source_pages: p3-458（章节目录结构）
  source_chapter: 全书章节推进
  source_quote: |
    "SIP FUNCTIONALITY OVERVIEW ... Introduction / SIP principle / OXE SIP implementation" (p44)
    "SIP USERS ... Introduction / SIP Product limit / SEPLOS mode (SIP extension) / SIP device mode /
    Communication with a SIP end-point" (p65)
    "REMOTE WORKERS SOLUTIONS FOR SIP ALE EQUIPMENT'S" (p384)
  summary: |
    课程按九段推进：①实验环境（RLAB 全虚拟化 + 混合模式两版拓扑与账号表）；②SIP 运营商模拟器
    （ITSP1 直连、ITSP2 经 SBC）；③POD 准备实验（预配置核对、IPDSP、公网接入参数）；④SIP 协议
    机理与 OXE 实现（含域名定制实验）；⑤SIP 用户两形态（含 SIP Device 开通实验）；⑥ALE SIP 终端
    家族与 SIP 设备管理（证书 + ALE-2/3 + ALE-x00 双分区 + ALES PC + ALES Android 五个实验）；
    ⑦编解码协商与维护跟踪（compvisu + 四工具实验）；⑧外线与 SBC（OXE 侧接入实验 + OTSBC 部署
    实验）；⑨远程办公（OTSBC 内嵌反代实验 + ALES Remote Worker 实验）。主线是"内核 SIP 化 → 终端
    → 运维 → 出口"，也是 OXE 站点 SIP 化交付的推荐顺序。
  conditions: 无特殊版本前提；各实验的版本门槛见各自条目
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: RLAB 全虚拟化 POD 拓扑（RLAB only）——实例清单与账号表
  type: structure
  source_pages: p5-11
  source_chapter: TRAINING LAB ENVIRONMENT - FULLY VIRTUALIZED / Training platform & Settings
  source_quote: |
    "OXE CSA ENTP_OXE_CSA_SIP csa (physical) csm (main) 192.168.1.1 / 192.168.1.3 ... mtcl swinst root
    Superuser2580*" (p9)
    "PC CLIENT 10 ENTP_PC_CLIENT_10 client10 192.168.1.10 ... IPDSP 31000 ALES 31030" (p9)
    "REMOTE WORKER POD P ENTP_PC_OUT_PODP This instance is in the common resources area.
    podP-outside 10.20.30.2P" (p9)
  summary: |
    POD 网络分 LAN(192.168.1.x) 与 DMZ(192.168.2.x)，公共资源区 Subnet 0(10.20.30.x)。实例清单
    （全部实验口径）：OXE CSA 物理 192.168.1.1/主用 192.168.1.3（账号 mtcl/swinst/root，口令
    Superuser2580*）；OMS CSA 192.168.1.13（root/admin，Superuser2580*）；PC CLIENT 10
    192.168.1.10（IPDSP 31000 + ALES 31030）；PC CLIENT 11 192.168.1.11（IPDSP 31001 + ALES
    31031）；FlexLM 192.168.1.80（root/letacla1）；IT SERVER 192.168.1.252（NTP+LDAP，
    training/superuser）；SBC 192.168.1.105 / DMZ 192.168.2.205（Admin/Admin）；内部 DNS
    192.168.1.250；外部 DNS 10.20.30.250；SIP 模拟器 12.0.0.2；远程办公虚机 podP-outside
    10.20.30.2P（P=POD 号）。PC CLIENT 10 预装 2 个 MicroSIP 模拟公网号码；NAS 网络盘共享课件。
  conditions: 仅培训环境；混合模式下 PC CLIENT 11 不需要（p18），SBC 虚机延后启动（p36-37 note）
  tags: [structure, lab, rlab, topology, lab-口径]

- id: f03
  title: 混合模式 POD 拓扑（RLAB + 课堂设备）——物理话机接入结构
  type: diagram
  source_pages: p14-19
  source_chapter: TRAINING LAB ENVIRONMENT - HYBRID MODE / Training platform & Settings
  source_quote: |
    "RAP Classroom MIX484 GD4 ALE-30h 31020 ALE-500 31010 ALE-300 31011 ALE-20h 31012 POE Switch
    192.168.1.12" (p16)
    "CLASSROOM EQUIPMENT PC CLASSROOM client 192.168.1.9 ... ALES 31031 ; GD4 192.168.1.12
    admin root letacla1 mg4.ale" (p18)
  summary: |
    在 f02 基础上叠加课堂硬件：POE 交换机 192.168.1.12 下挂四部话机——ALE-500(31010)、ALE-300
    (31011)、ALE-20h(31012)（IP NOE，动态地址，DHCP 池 192.168.1.145-147）与 ALE-30h(31020，
    TDM/UA)；GD4 网关 192.168.1.12（账号 admin/root，口令 letacla1/mg4.ale，实验口径）；教室 PC
    192.168.1.9 跑 ALES 31031。物理话机让寻线组/监督/双分区实验可在真机上做。
  conditions: 仅混合模式课堂；虚拟课堂以 IPDSP/MicroSIP 替代物理话机
  tags: [diagram, lab, hybrid, classroom]

- id: f04
  title: ITSP1 SIP 运营商模拟器——直连拓扑与号码变换规则
  type: diagram
  source_pages: p22-27
  source_chapter: SIP CARRIER SIMULATOR / ITSP1
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... ITSP1 Public gateway public.itsp1.com
    10.20.30.50 ... SIP domain: sip.itsp1.fr / itsp1.fr" (p22)
    "Id: pbxP password: alcatel ... Public numbers: Id: publicP@itsp1.fr password: public" (p22)
    "Dialed number: 0110312345 Number sent by the PBX: +33110312345" (p24)
  summary: |
    ITSP1 两条腿：SIP 网关 gateway1.itsp1.com(10.20.30.51，PBX 注册账号 pbxP/alcatel)与公网网关
    public.itsp1.com(10.20.30.50，两个 MicroSIP 模拟 Public/Urgence 用户，主号 3321PN12345)。号码
    规则（PN=两位 POD 号）：紧急 112/15/17/18；国内 33{1-5}1PN12345；移动 3361PN/3371PN12345；
    国际(英国) 4421PN12345。呼出变换：0110312345→+33110312345、06→+336、004421→+4421。呼入：
    Node 1 安装号 3321PN、DDI 外线首号 41000、内线首号 31000、范围 500（31001 外线=3321PN41001）；
    Node 2 安装号 3311PN、41500/31500/500；节点间互打经 ITSP1 回环（0110341501 或 33110341501）。
  conditions: 实验口径（RLAB 专用）；生产运营商行为与模拟器有差异
  tags: [diagram, sip-trunk, simulator, numbering, lab-口径]

- id: f05
  title: ITSP2 模拟器——经 SBC 的第二条运营商腿
  type: diagram
  source_pages: p29-33
  source_chapter: ITSP2 / SIP SIMULATOR OVERVIEW - ITSP2 SIP GATEWAY
  source_quote: |
    "ITSP2 SIP Gateway gateway.itsp2.com 10.20.30.60 ... SIP domain: sip.itsp2.fr ... Id: podP
    password: alcatel" (p30)
    "PBX installation nb 3392PN ... Dialed number: 0920331002 or 33920331002" (p33)
  summary: |
    ITSP2 网关 gateway.itsp2.com(10.20.30.60)，SIP 域 sip.itsp2.fr/itsp2.fr，PBX 侧账号 podP
    (P=POD 号)/alcatel，路径经 SBC（拓扑图两端都画了 SBC）。号码口径：PBX 安装号 3392PN，DDI 外线
    首号 3392PN31000，示例 31002 外线=3392PN31002；呼出拨 0920331002 或全号。公网/紧急用户复用
    ITSP1 的 MicroSIP 注册。SBC 章的 DID 翻译按 33920x31000、范围 1000 配置（p359），两处书写
    风格不同但同属实验口径。
  conditions: 实验口径；SBC 实验前 OTSBC 未配置时外部网关不工作（p363 note）
  tags: [diagram, sip-trunk, sbc, simulator, lab-口径]

- id: f06
  title: POD 准备 How-To 流程——虚机启动 → 预配置核对 → 终端开通 → 公网接入
  type: flow
  source_pages: p35-42
  source_chapter: POD preparation (How-To)
  source_quote: |
    "OXE VMs used for this training are already configured (Database and Linux Data), such as:
    Software licenses are restored, SSH is enabled (mandatory since OXE Release N3) ..." (p38)
    "Registration ID pbxN (where N is your POD number) ... First external number 33210N41000
    ... First internal number 31000, Range Size 500" (p41)
  summary: |
    四段：①按模式启动虚机清单（SBC 虚机延后；混合模式不需要 PC CLIENT 11）；②核对预配置——许可
    已恢复、SSH 已启用（N3 起强制）、内部防火墙部分配置、NTP 192.168.1.252 与 FlexLM 192.168.1.80
    已声明、DHCP 池 192.168.1.145-147、机架/板卡在库（软件机架 3U/OMS/机架 4/虚拟 GD4 槽 0
    192.168.1.13/24，混合另有硬件机架 1U/机架 2/GD4 192.168.1.12 + MIX484 槽 1）；③用户表开通
    （虚拟模式 31000/31001 IPDSP；混合加 31010 ALE-500、31011 ALE-300、31012 ALE-20H、31020
    ALE-30H；IPDSP 的 Network 设置里 TFTP Server Main 填 192.168.1.3）；④公网接入——外部 SIP
    网关填 Registration ID=pbxN 与 Outgoing username=pbxN，DID 翻译器首外线 33210N41000/首内线
    31000/范围 500，随后拨测外呼。
  conditions: 预配置已由基线镜像完成（实验口径）；生产站点需按 Starter 课程从头做
  tags: [flow, lab, pod-preparation, menu-path]

- id: f07
  title: SIP 协议定位与协议栈结构——信令/媒体分层
  type: diagram
  source_pages: p45-48
  source_chapter: SIP FUNCTIONALITY OVERVIEW / Introduction & SIP principle
  source_quote: |
    "SIP: Session Initiation Protocol • Protocol TCP/IP • TCP or UDP • IPv4 or IPv6 • IETF Standard:
    RFC 3261 • Application layer ... Establish, maintain, modify and terminate multimedia sessions"
    (p45)
    "Media characteristics are described by the SDP (Session Description Protocol) • RTP port, RTCP
    port • Audio codecs, Video codec • SIP signaling can be protected by the TLS protocol" (p48)
  summary: |
    分层图：IP → TCP/UDP → 上层分两路——SIP（信令）与 RTP+编解码器（媒体）。SIP 职责五要素：用户
    位置、用户可用性、终端能力、会话建立、会话管理（转移等演进、上下文变更、加媒体如视频、结束）。
    SIP 语法贴近 HTTP/SMTP，元素用类邮箱的 SIP URL 标识；媒体特征由 SDP 描述（RTP/RTCP 端口、
    音视频编解码）；信令可用 TLS 保护。课程随后用完整 INVITE 报文（含 SDP：PCMA/PCMU/G729/OPUS/
    G722/telephone-event）落地讲解。
  conditions: 协议基础内容，无版本前提
  tags: [diagram, sip, protocol-stack, rfc3261]

- id: f08
  title: SIP 消息与响应码体系——请求十种 + 响应六类
  type: structure
  source_pages: p49-50
  source_chapter: SIP PRINCIPLE / SIP Messages
  source_quote: |
    "INVITE Message sent systematically by the client for any connection request ... REGISTER Message
    sent by an agent to indicate his actual address ... INFO Message generating DTMF tone for SIP
    requests" (p49)
    "1xx Informational ... Trying(100),Ringing(180) ... 4xx Client Failure Responses Bad request(400),
    Forbidden(403),Not found(404) ..." (p50)
  summary: |
    请求类型：INVITE（发起）、ACK（确认）、PRACK（临时响应确认）、BYE（结束通话、停 RTP）、CANCEL
    （取消建立中呼叫）、SUBSCRIBE/NOTIFY（事件订阅/通知，如新语音留言）、REGISTER（注册实际地址）、
    REFER（请求对方呼叫某地址，用于转移）、INFO（产生 DTMF）、UPDATE（会话参数更新与保活）。响应
    六类：1xx（100 Trying、180 Ringing）、2xx（200 OK）、3xx（重定向）、4xx（400/403/404/406/488）、
    5xx（500/502/503）、6xx（600 Busy Everywhere、603 Decline）。这是读懂全书 trace 的码表。
  conditions: 无版本前提
  tags: [structure, sip-messages, response-codes]

- id: f09
  title: SIP 实体角色图——注册/位置/代理/SBC/网关/B2BUA 八角色
  type: diagram
  source_pages: p51
  source_chapter: SIP PRINCIPLE / Possible roles of SIP entities
  source_quote: |
    "Registrar Server In charge of SIP UA registration ... SBC (Session Border Controller) Security
    element, Topology hiding, Required for NAT Traversal context for example ... B2BUA: Back-To-Back
    User Agent Receives one request as a UAS and returns another as a UAC. Difference with a proxy:
    2 separate communications" (p51)
  summary: |
    八个角色：Registrar Server（收注册、可鉴权、映射 IP↔SIP URI）；SIP Location Server（注册器更新
    的数据库，代理收 INVITE 时查询）；SBC（安全/拓扑隐藏/NAT 穿越/过滤）；Gateway（SIP 世界到 PSTN/
    模拟等的过渡）；UA（UAC 发请求=主叫 / UAS 应答=被叫）；SIP Proxy（消息路由、权限控制、可解释改写）；
    Redirect Server（以 3xx 应答的重定向服务器）；B2BUA（以 UAS 收请求、以 UAC 再发一个，与代理的
    区别是两段独立会话）。理解角色是后续排障定位"谁该回 403/488"的前提。
  conditions: 无版本前提
  tags: [diagram, sip-entities, sbc, proxy, b2bua]

- id: f10
  title: SIP 注册与呼叫建立时序——REGISTER 租期 + INVITE 五步
  type: flow
  source_pages: p52-54
  source_chapter: SIP PRINCIPLE / Registration & SIP call
  source_quote: |
    "Each time that a SIP client is started (Deskphone, Softphone), it sends a registration request to
    the registrar with a leased time value ... End of registration Leased time of 1H" (p52)
    "Example of a SIP session establishment through a SIP proxy Invite (user A SDP) 180 ringing
    (no SDP) 200 Ok (user B SDP) ACK ... BYE" (p53)
  summary: |
    注册机制：客户端启动发 REGISTER（示例 Expires:3600，即 1 小时租期，contact 行记录 IP:端口），
    停机发 Expires:0 注销；注册库形如 "Address of record: 31030 contact: sip:31030@192.168.1.10:5160,
    UDP, 2063 s"。呼叫时序（经代理）：INVITE(A 的 SDP) → 100 Trying → 180 Ringing(无 SDP) → 200 OK
    (B 的 SDP) → ACK → RTP 双向 → BYE/BYE/ACK 收尾。书中给出 31034(ALE-300) 呼 31000(IPDSP) 的
    全报文对照。
  conditions: 无版本前提；租期具体值由注册服务器 min/max 参数约束（见 p88）
  tags: [flow, sip-registration, call-flow, timing]

- id: f11
  title: OXE SIP 实现六组件架构——本地网关/字典/代理/注册器/位置/外部网关
  type: diagram
  source_pages: p56-57, p329
  source_chapter: OXE SIP IMPLEMENTATION / Architecture
  source_quote: |
    "SIP Gateway The SIP gateway acts as an interface between the Call Handling and SIP proxy server
    • SIP Dictionary Provides translation between PCX directory number and SIP URLs • Proxy Server
    Route the SIP messages within the network ... External SIP gateway Declaration of a remote
    proxy/gateway of an external SIP system (SIP carrier, voice mail, VAA,...)" (p57)
  summary: |
    六组件同栖于 sipmotor 进程域：①SIP Gateway（Call Handling 与 SIP 代理的接口）；②SIP Dictionary
    （PCX 号码↔SIP URL 翻译）；③Proxy Server（网内消息路由）；④Registrar Server（收终端注册并送位置
    服务器）；⑤Location Server（URL→IP）；⑥External SIP Gateway（外部 SIP 系统的远端代理/网关声明，
    挂 SIP 中继组）。全景图还画了 SIP 承载（SIP 承载商、Rainbow WebRTC 网关、SBC、VAA 语音自动话务员）
    与终端（NOE 话机、SIP 话机=SEPLOS、SIP 设备）。
  conditions: 组件参数化配置见 p85-88（SIP Device 实验）
  tags: [diagram, architecture, oxe, sipmotor]

- id: f12
  title: 空间冗余与内部域名解析机制——双 IP/节点名/DNS 委托
  type: flow
  source_pages: p58-59
  source_chapter: OXE SIP IMPLEMENTATION / SIP Functionality - Spatial redundancy
  source_quote: |
    "Two different IP addresses are used for the role addressing • The 'node name' should be used to
    reach the SIP server ... The server delegates the responsibility of resolving OmniPCX Enterprise
    FQDN to the OmniPCX Enterprise internal DNS server" (p58)
    "Only the main Communication Server replies to DNS requests by sending its main IP address" (p59)
  summary: |
    结构：每台 CS 有物理 IP 与角色 IP（示例 CPU-A 192.168.1.1/1.3，CPU-B 192.168.2.1/2.3），客户端
    一律用节点名 oxe.mycompany.com 接入。解析链：客户 DNS 把 OXE FQDN 委托给 OXE 内部域名解析器
    （netadmin 开启）→ 请求同时发两台 CS → 仅 Main 以其主用角色 IP 应答 → 客户端连到对的机器。管理
    工具为 netadmin。这套机制同时支撑 SIP 注册与 DM 下载（spatial redundancy 下 TFTP URL 必须用
    FQDN，见 p181/p204）。
  conditions: 需客户 DNS 服务器可配置委托；内部域名解析器仅解析节点名
  tags: [flow, redundancy, dns, node-name]

- id: f13
  title: OXE 域名管理路径——netadmin 菜单 19（查询/定制）与管理工具只读
  type: menu-path
  source_pages: p61-63
  source_chapter: OXE domain (How-To)
  source_quote: |
    "(1)csa> netadmin -m ... 19.1.OXE DOMAIN Management 1. 'View' 2. 'Create/Update' ...
    Enter OXE Domain to be configured (default is oxedomain.com) ? company.com" (p62-63)
    "Warning TO MODIFY THESE PARAMETERS, NETADMIN MENU MUST BE USED." (p62)
  summary: |
    路径：CS 上以 mtcl 登录 → netadmin -m（默认域名时先弹 IMPORTANT WARNING：请配置正式注册域名
    防证书错误）→ 19/1/1 View 查看（显示 OXE DOMAIN 与 OXE FQDN）或 19/1/2 Create/Update 输入新
    域名。只读核对走管理工具（mgr/WebAdmin）：SIP/SIP Gateway → Edit/Consult，看 Machine name-Host
    与 DNS local domain name 两字段；修改只能经 netadmin。FQDN = 节点名 + 域名（p170）。
  conditions: mtcl 账号；默认域名 oxedomain.com 会触发证书错误告警
  tags: [menu-path, netadmin, domain, fqdn]

- id: f14
  title: SEPLOS(SIP Extension) vs SIP Device 两形态对比结构
  type: structure
  source_pages: p66-68, p75-78
  source_chapter: SIP USERS / Introduction & SIP DEVICE MODE
  source_quote: |
    "SIP Extension • Multiline • Can use prefixes/suffixes to activate PCX phone services • Access to
    a large range of PCX phone services (camp on, consultation call, broker call, call forwarding,
    etc.) • Can belong to a pick-up or hunting group • Can be used as hotel dedicated set" (p67)
    "SIP device ... Mandatory to configure: The local SIP Gateway, A SIP trunk group, An adjacent
    subnetwork ... Cannot be supervised by CSTA (therefore, one cannot use the Computer Telephony
    Integration (CTI) mechanisms of the PCX)" (p67, p78)
  summary: |
    两形态结构化对比：SEPLOS=电话应用眼里的"内部话机"（自动两条 multiline 键、子型+DM profile 管理、
    前缀/后缀业务、寻线组/代接组/酒店话机、SIP MESSAGE 显示 CS 信息、原生加密、可参与 RCC 增强）；
    SIP Device=远端子网设备（会议话机/视频设备/门禁等，服务缩水：无前缀/后缀、无酒店、无 CSTA 监督、
    无呼叫中心坐席、不入组），开通硬前提是子网+关联中继组+本地 SIP 网关关联。选型即服务等级决策。
  conditions: 软件锁 177/345/430 与容量上限控制规模（数值见 principle 提取）
  tags: [structure, seplos, sip-device, comparison]

- id: f15
  title: SEPLOS 终端部署四步图——DHCP → DM 配置文件 → 二进制 → SIP 信令
  type: flow
  source_pages: p71
  source_chapter: SEPLOS MODE / Deployment
  source_quote: |
    "1 DHCP request. SIP Phone retrieves the device management application address 2 SIP Phone
    downloads its configuration file. The Device Management checks the MAC address in the https
    request. 3 SIP Deskphone downloads its binaries from the device management and performs a software
    update 4 SIP signaling establishment" (p71)
  summary: |
    四步链：①话机发 DHCP 请求拿到 DM 应用地址（外部 DHCP 用 option 66，或 OXE 内部 DHCP 类的 TFTP
    Server 地址）；②HTTPS 向 DM 拉配置文件（DM 按 MAC 核对）；③话机从 DM 拉二进制并升级（双栈机
    双分区各一份）；④SIP 信令建立（注册）。DM 可宿于 OXE 或 OmniVista 8770。这条链是后续三个开通
    实验（ALE-2/3、ALE-x00、ALES）共同的骨架。
  conditions: ALES 软终端无二进制下载步骤（OXE 不宿其 binaries，p163）
  tags: [flow, dm, deployment, dhcp]

- id: f16
  title: NOE↔SIP 终端互通流程——NOE 主叫 6 步 / SIP 主叫 7 步
  type: flow
  source_pages: p80-82
  source_chapter: COMMUNICATION WITH SIP END-POINTS
  source_quote: |
    "3. The SIP gateway consults the SIP dictionary to convert the number to an URL 4. An invite
    request is sent to the SIP Proxy with the URL provided by the dictionary 5. The SIP proxy server
    consults the SIP location server to find the current URL of the requested SIP set" (p81)
    "3. Identification of the SIP domain to know if the OXE is the recipient 4. The request URI is sent
    to the SIP Gateway 5. Call is routed to the Call Handling 6. Identification of the number received
    7. If the number exit, the set is rung" (p82)
  summary: |
    NOE 话机呼 SIP 话机六步：拨号 → 送本地 SIP 网关 → 查 SIP 字典换 URL → INVITE 发代理 → 代理查
    位置服务器 → 已注册则按注册 IP 转发。SIP 话机呼 NOE 七步：代理收到 → SIP 域名判定是否本机 →
    Request URI 送 SIP 网关 → 路由到 Call Handling → 号码识别 → 存在则振铃。注册状态即服务状态：
    注销或超时后 IP 置 0.0.0.0、终端 out of service（p80）。
  conditions: 域名判定依据本地网关的 OXE_Address/Machine Name/FQDN 拼接（p330 完整化）
  tags: [flow, interworking, dictionary, location-server]

- id: f17
  title: SIP Device 开通主线九节——私网→中继组→网关→代理→注册器→字典→隔离/信任→建户→验证
  type: flow
  source_pages: p84-94
  source_chapter: SIP Users (How-To) — "SIP device" user commissioning
  source_quote: |
    "Remember that a call from/to a 'SIP device' user requires the OXE local SIP gateway. So, in a
    first step, it is mandatory to configure the private SIP Trunk Group, the local SIP gateway, the
    SIP proxy…" (p85)
    "Users -> Create ... Set Type + SIP device ... SIP Passwd 12345" (p89)
  summary: |
    九节主线：①私网（Translator/Network Routing Table，选空闲号如 10，协议 ABC-F，勿占 ABC/VPN 号）；
    ②私有 SIP 中继组（Trunk Groups Create：T2 型、远端网络=私网号、T2 Specification=SIP；虚拟接入成
    对分配）；③本地 SIP 网关（SIP/SIP Gateway：子网/中继组/角色 IP/主机名/代理端口 5060/订阅时长/
    会话计时器/DNS 域名/SDP in 18x/CAC）；④SIP 代理（SIP/SIP Proxy：认证 Digest、隔离框架参数等）；
    ⑤注册服务器（SIP/SIP Registrar：到期上下限）；⑥SIP 字典（重名 alias 场景）；⑦隔离/信任 IP 清单；
    ⑧建户（31060，Set type=SIP device，SIP 密码）+ 防火墙信任主机；⑨MicroSIP 配置 + sipregister/
    trkstat 验证 + 内外呼测试。
  conditions: 系统级别只需一个私有 SIP 中继组(ABC)（p85 note）；改虚拟接入数须重启（p86 warning）
  tags: [flow, sip-device, commissioning, menu-path]

- id: f18
  title: SIP 用户维护命令族——sipgateway/trkstat/sipdict/sipregister/进程与隔离日志
  type: structure
  source_pages: p91-94, p236-238, p260-261
  source_chapter: SIP Users / Maintenance & ALE SoftPhone / Maintenance
  source_quote: |
    "Command sipgateway ... Proxy Port Number : 5060, TLS Port Number : 5061, MTLS Port Number :
    6261 ... Overflow license Threshold : 80" (p91)
    "The set 31060 is a SIP Device (type = 2). A user, whose set type is 'SIP Extension', has a
    'type = 3'." (p92)
    "IF REQUIRED, USE THE FOLLOWING COMMANDS TO REINITIALIZE THE PROCESSES - dhs3_init –R SIPMOTOR
    (RECOMMENDED) - killall sipmotor. WARNING: YOU HAVE TO BE LOGGED AS ROOT" (p93)
  summary: |
    六件套（mtcl 登录）：①sipgateway——本地网关全景（含 TLS 5061/MTLS 6261 端口、payload 101、
    G722 支持、许可溢出门限 80）+ 信任/隔离 IP 清单 + RW SBC LAN IP 清单；②trkstat <TG>——中继组
    62 路 TS 状态（SIP Device 呼叫占 TS，SEPLOS 不占）；③sipdict -l——字典表（type 2=Device、
    type 3=Extension）；④sipregister——注册库（AOR+contact+剩余租期）；⑤ps -edf | grep sipmotor
    ——进程检查（重启用 dhs3_init -R SIPMOTOR，root 才能 killall）；⑥自动隔离看 /usr4/tmp/
    sipalarm.log（f003 告警），手工隔离看 sipgateway 输出。ALES 章追加 csipsets（含 -d/-f）、
    csipview com、check_ales_ldap 三条。
  conditions: 命令均在 CS 上执行；隔离动态名单不在 sipgateway 手工清单里
  tags: [structure, maintenance, cli, troubleshooting]

- id: f19
  title: ALE SIP 终端家族谱系——话机四档 + 软终端 + 8008 特例
  type: structure
  source_pages: p70, p97-106
  source_chapter: ALE SIP EXTENSIONS / ALE SIP Deskphones
  source_quote: |
    "S I P E N T E R P R I S E D E S K P H O N E S ALE-2 Deskphone ... S I P S O F T P H O N E S
    ALES (Windows/Android/iOS) ... 8088 V3" (p70)
    "8008/8008G DESKPHONES - OVERVIEW ALE SIP stack, in Business & hotel mode (no attendant, no CC
    agent)" (p98)
  summary: |
    家族谱系：Enterprise（ALE-300/400/500，NOE/SIP 双栈，SIP+ from Purple，最多 3 个 ALE-120 扩展
    模块）；Essential（ALE-30，支持 1 个 EM-200）；Basic（ALE-2/ALE-3，仅 Business 模式，原生加密
    SIP TLS/SRTP）；Essential 8008/8008G（Business+酒店模式，无话务员/坐席）；8088（Huddle Room）；
    ALES 软终端（Windows/Android/iPhone）。各档功能矩阵（日志容量、可编程键数、视频、监督/寻线组
    等级）逐表对照，决定售前选型。GUI 新交互（Dashboard、拖拽按键、音频选择器）为 Enterprise/
    Essential SIP 模式独有。
  conditions: 不支持特性清单（酒店/话务员助理/MLA/VPN 客户端/Audio Hub/skinify）按档分层（p105）
  tags: [structure, terminals, deskphones, ales]

- id: f20
  title: ALES 界面分区与退出语义——九宫功能区 + 隐藏 vs 退出
  type: structure
  source_pages: p118-119
  source_chapter: ALE SOFTPHONE - GUI
  source_quote: |
    "Call logs / Programmable keys / Settings / My telephony status / Voice mail / Peripheral
    status/configuration / Global search (Local contact, OXE and corporate) / Contacts/Groups /
    Routing Dialpad" (p118)
    "Logout ... Quit ALES application: Right click on the icon in the task bar to quit the application
    => Receiving a phone call is no longer possible. Hide ALES application and put it in background =>
    Receiving a phone call is possible" (p119)
  summary: |
    主界面九区：呼叫日志、可编程键、设置、我的话务状态、语音信箱、外设状态/配置、全局搜索（本地
    联系人/OXE/企业目录）、联系人/分组、路由拨号盘。行为语义两条：窗口关闭/隐藏只是后台化，来话照收；
    任务栏图标右键 Quit 才是退出（此后不再收来话）。排障时用户"收不到电话"先查是不是 Quit 了。
  conditions: 无版本前提
  tags: [structure, ales, gui, behavior]

- id: f21
  title: 一号多机 ALES-DUID 互斥时序——注册记录/403 拒绝/force 抢占/通话中例外
  type: flow
  source_pages: p115-117
  source_chapter: ALE SOFTPHONE – USE SAME LOGIN ON DIFFERENT DEVICE
  source_quote: |
    "A given directory number (DN) is associated to a unique device at a time. To enforce this rule,
    a unique identifier (ALES-DUID) is sent by each ALES in any SIP request (RFC4122)" (p115)
    "REGISTER (ALES-DUID 2) 403 Forbidden Warning: 399 Multiple Logins ... REGISTER (ALES-DUID
    2;force) 200 OK ... In this case, the login request on ALES PC2 is rejected (even with the force
    attribute) Call is in progress" (p116-117)
  summary: |
    机制：每个分机号同一时刻唯一绑定一台设备；OXE 在首个 REGISTER 时记录 DN↔ALES-DUID。时序三分支：
    ①PC2 登录 → 403 + Warning 399 Multiple Logins → 用户端弹确认，选择后带 force 重注册 → 200 OK，
    PC1 被踢（其后续非 REGISTER 请求一律 403）；②已登录 iPhone 时再登 PC → 不受影响（跨设备类型
    不互斥）；③PC1 通话进行中 PC2 请求登录 → 即使 force 也被拒。该机制解释了"同一账号两台电脑
    打架"类工单。
  conditions: 仅同型设备（PC vs PC、手机 vs 手机）互斥
  tags: [flow, ales-duid, multi-login, sip-behavior]

- id: f22
  title: 监督与代接机制——SUBSCRIBE/NOTIFY 结构 + Keep Alive 事件码
  type: flow
  source_pages: p130-133
  source_chapter: SET SUPERVISION AND CALL PICK UP
  source_quote: |
    "Supervision is configured by creating a supervision key for the supervisor. Limit is 30000
    supervision keys on one OXE node. A supervisor can have up to 40 supervision keys." (p130)
    "In service incident: 511 for ALE deskphone or 3rd-party device and 513 for ALE softphone ...
    Out of service incident: 510 for ALE deskphone or 3rd-party device and 512 for ALE softphone"
    (p133)
  summary: |
    机制链：管理员给监督员配"Set Supervision"键（DM 配置文件含 B、C 被监督人）→ ALES 向 OXE 发
    SUBSCRIBE[B,C] → OXE 回被监督人清单与状态 → 状态变化以 NOTIFY 推送（四态：available/ringing/
    busy/out of service）。来话通知 toast+专属铃声（仅 Windows PC 与 Android；多个被监督人同振只显
    最新一个）。服务状态联动：Keep Alive（SIP OPTION 或 REGISTER）超时即判离服，产生事件码——入服
    511（话机/第三方）/513（ALES），离服 510/512，OXE 再 NOTIFY 给监督端。只有 SIP 设备能被另一台
    SIP 设备监督；iPhone 无监督。
  conditions: 容量 30000 键/节点、40 键/监督员（数值细节见 principle）
  tags: [flow, supervision, notify, incidents]

- id: f23
  title: 多终端两种组网结构——纯 SEPLOS 主备与 NOE/DECT 混合
  type: diagram
  source_pages: p134-137
  source_chapter: MULTI-DEVICES
  source_quote: |
    "Main and Secondary (1 to 4) ... In a configuration with a deskphone, it is recommended to have
    the deskphone as the main device ... Only one ALE SoftPhone for Windows and one ALE SoftPhone for
    Mobile within the multi-devices" (p134)
    "Second possibility: mixed multi-device configuration with a NOE deskphone and DECT • Limited to
    3 devices ... ** Virtual UA, REX and MIPT are not supported" (p135)
  summary: |
    两种组网：①纯 SIP 多终端——1 主 +1~4 副（话机/ALES PC/ALES 手机），建议话机当主；来话并振、
    任一终端外呼都算用户呼叫；②混合——NOE 话机 + DECT 手柄 + ALES（至多 3 设备；Virtual UA、REX、
    MIPT 不支持）。来话历史一致性：RFC3326 Reason 头（"call completed elsewhere"）随 CANCEL 通知
    其他终端，已接来电不再计入它机未接。Wireshark 抓包佐证。
  conditions: 主备关系影响寻线组行为（ tandem 联动见 p140）
  tags: [diagram, multi-devices, rfc3326]

- id: f24
  title: 寻线组三型与混装规则矩阵——circular/cyclical/parallel
  type: structure
  source_pages: p138-141
  source_chapter: HUNTING GROUPS / SEQUENTIAL AND CYCLICAL / PARALLEL
  source_quote: |
    "Hunting groups with circular, cyclical and parallel search type can be configured with SIP
    equipment's ... Note: From Basic Deskphones (ALE-2/ALE-3, 8008), the login/logout actions are
    performed using prefixes" (p138)
    "Mixed SIP/NOE configuration is NOT supported for parallel hunting group • Can contain only SIP
    devices or only NOE devices • Multi-devices CANNOT be part of such hunting group" (p141)
  summary: |
    规则矩阵：组呼叫不可转移；呼叫分配不理会呼转与 DND；离服成员不参与分配但保持登录。顺序/循环组
    支持 SIP/NOE 混装、多终端可入组（tandem 主机登入登出联动全部副机）；并行组不支持混装（首个成员
    类型定调：NOE 打头 SIP 不得入，SIP 打头 NOE 不得入）且多终端不得入组。进退组：ALES/ALE-30/
    ALE-x00 有图形开关，基础话机走前缀（默认 480/481，须在 Phone features COS 授权）。ALES 独享
    组/个人呼叫日志过滤与组来话提示（主叫 ID+组图标+组名）。
  conditions: 前缀 480/481 为默认值，实际以系统编号计划为准
  tags: [structure, hunting-group, matrix]

- id: f25
  title: RCC 能力分层——legacy basic / enhanced basic / advanced 三档
  type: structure
  source_pages: p142
  source_chapter: REMOTE CALL CONTROL
  source_quote: |
    "Prerequisite: SIP devices must include 'hold, talk and refer' in SIP header ... Enhanced basic
    RCC • Make call: no compressor required to establish the initial dialog with the SIP device
    Requires to activate 'Optimize resource 3PCC call' parameter in the SIP device phone COS" (p142)
  summary: |
    三档：①legacy basic RCC——不满足头条件的老设备仍可用；②enhanced basic RCC——Make call 不占压缩
    资源，前提在 SIP 设备 Phone COS 打开 "Optimize resource 3PCC call"；③advanced RCC——含通话中业务
    全集：Make/Answer/Hold/Retrieve/Consultation(enquiry)/Call waiting/Alternate(broker)/Reconnect/
    Conference(三方，conf 电路在 IMG)/End conference/Ringing Transfer(非监督转移)/Attended Transfer
    (监督转移)。适配机型：Enterprise、ALE-30、ALE-2、ALE-3、8008。
  conditions: advanced 各服务可用性还受终端能力与 RFC 实现影响
  tags: [structure, rcc, 3pcc, csta]

- id: f26
  title: SIP DM 选型结构——OXE DM vs 8770 DM 对比 + 三种部署拓扑
  type: structure
  source_pages: p146-150
  source_chapter: SIP DEVICE MANAGEMENT BY OXE / SIP DM: OXE VS 8770
  source_quote: |
    "Since OXE N1, the SIP device management can also be done directly on OXE ('SIP DM on OXE'
    feature) for local and remote SIP equipment's." (p146)
    "Choice of DM is done through an OXE system option ('Device Management in 8770') ... This option
    is not taken into account for ALES clients, which are only supported on OXE DM" (p148)
  summary: |
    选型结构：8770 DM 强在集中化（跨节点/跨网、用户与设备模板、即插即用、支持已停产 8001/8018/8028s/
    8088 酒店等）；OXE DM 强在安全（客户级证书）、按节点 DM profile、随 CS 冗余更韧、二进制自动更新
    与配置即时通知，但只支持 8008/ALES/ALE-2/3/30/x00。拓扑三分支：①存量 8770 迁移（混合：话机留
    8770、ALES 归 OXE）；②新装（话机二选一，ALES 恒归 OXE）；③开关 = 系统参数 "Device Management
    in 8770"（ALES 不受此参数影响）。
  conditions: 关闭 8770 DM 会删其配置文件，话机必须 reset flash（p174 warning）
  tags: [structure, dm, migration, topology]

- id: f27
  title: DM profile 体系与六块特性——默认 0、上限 100、按子型适配
  type: structure
  source_pages: p152-153
  source_chapter: DM PROFILE
  source_quote: |
    "A SIP DM profile is assigned to each SIP user. The DM profile will adapt to the sub type of
    device to generate a compatible configuration file of settings ... By default, profile 0 is
    configured. Possibility to have up to 100 profiles" (p152)
    "General characteristics • Set Emergency Number and LDAP server ... Advanced characteristics •
    Set Security parameters and Password / Video settings" (p153)
  summary: |
    体系：每 SIP 用户挂一个 profile，profile 按子型生成兼容配置文件；ALE-S 与 8008 本地/远程共用一个
    profile，ALE-x 系要两个（本地无 SBC、远程配 SBC）；改 profile 即为该 profile 全部设备重生成配置
    并发 SIP NOTIFY。六块特性：General（紧急号码、LDAP 目录搜索）；Device（音频/时间/DNS/SNTP/配置
    与升级轮询计时器）；Application（业务、O365 集成）；SIP（SIP 参数/端口/计时器/SBC/编解码清单）；
    Telephony（拨号规则/前缀/业务授权）；Advanced（安全与密码/视频）。
  conditions: profile 先建后配用户（p452 warning 重申）
  tags: [structure, dm-profile, parameters]

- id: f28
  title: 配置文件生成/存储/获取机制——MAC 与 login 双命名 + 401/mTLS 双认证
  type: flow
  source_pages: p156-160, p163-164
  source_chapter: CONFIGURATION FILE GENERATION / PRINCIPLE FOR DESKPHONES / PRINCIPLE FOR ALE SOFTPHONE
  source_quote: |
    "Physical devices 8008 and ALE-x • The DM generated file is based on MAC address. Filename is:
    config.<mac>.xml in '/DHS3data/mao/DM/dmictouch' folder" (p156)
    "a new instance is launched on port 8443, dedicated to OXE DM, on which mTLS is mandatory ...
    The MAC address received in the HTTPS request is verified against the one specified in the
    certificate common name (CN)" (p159)
  summary: |
    生成与存储：物理话机按 MAC（config.<mac>.xml，/DHS3data/mao/DM/dmictouch）；ALES 按 login
    （/DHS3data/mao/DM/dmsoftphone/ALES-desktop|ALES-mobile + hex 编码路径；login 为邮箱时按域分目录）。
    获取三通道：①文件已存在（MAC 已绑定）直接下发；②不存在 → 401 → 话机带 分机号+密码+MAC+机型
    （USER AGENT）认证 → OXE 回写 MAC/子型并即时生成 → 200 OK；③R101.1 起 mTLS 强下载认证——
    NGINX 443 收请求后 302 重定向到专设 8443 实例，强制双向证书校验（MAC↔证书 CN），原有 号码+PIN+
    MAC 认证保留；远程工作者场景由 RP 注入 X-Real-Mac / X-Forward-For 头。ALES 特例：无 binaries
    托管、无 auto-discovery、login 必须预建，配置请求带 login+密码+子型。
  conditions: 远程桌面 mTLS 经 swinst "DM auth. with client cert" 控制（默认 Enabled）
  tags: [flow, dm, mtls, nginx, config-file]

- id: f29
  title: 二进制管理机制——downbin 目录/版本比对/轮询升级
  type: flow
  source_pages: p165
  source_chapter: BINARIES
  source_quote: |
    "SIP binary files are delivered with OXE version. A specific parameter, available in the device
    DM configuration file, provides the path (in OXE) of the binary file 'DmEnetcfgUpgradeFile' field
    ... Binaries for all devices are stored in '/DHS3bin/downbin' folder" (p165)
  summary: |
    机制五点：①双栈话机 SIP 二进制随 OXE 版本交付，DM 配置文件字段 DmEnetcfgUpgradeFile 指明路径；
    ②全部二进制存 /DHS3bin/downbin；③设备经 NGINX 请求（日志含版本号 UA）；④设备先下文件头几个
    字节比版本，不同才全量下载；⑤升级按轮询信息执行——每天固定时刻一次，或设备重启时。ALES 不适用
    （无 binaries 托管）。排障可 grep nginx access.log 的 downbin 请求。
  conditions: 适用双栈 IP 话机；ALES 例外
  tags: [flow, binaries, downbin, upgrade]

- id: f30
  title: OXE DM 证书定制流程（内部 PKI）——根 CA → CS 证书 → CTL 产物
  type: flow
  source_pages: p168-171
  source_chapter: Customization of the certificate for OXE DM with the internal PKI (How-To)
  source_quote: |
    "By default, a certificate is generated at OXE installation for the HTTPs server for the usage of
    the WBM feature. However, it is not suitable for the SIP clients." (p169)
    "netadmin -m ... 11 : Security 9 : PKI Management 1 : CS Certificates And choice 1 : Create/Update
    CS certificates (Auto generated)" (p169)
  summary: |
    流程：root 登录 → netadmin -m → 11/9/1 → 选 1 自动生成：录入 CC-suite-ID（默认取自许可文件）、
    是否加通配 DNS *.company.com（默认 y）、是否把物理与角色 IP 写入 SAN（默认 y）、附加 SAN（默认
    n）、密钥长度（2048-4096，默认 4096）、国家/州/城市/组织 → 生成四件：内部根 CA、CS 密钥对、CS
    CSR、CA 签发的 CS 证书。核验：11/9/1/8 View（CA CN=CC-suite-ID，CS CN=oxe.company.com，SAN 含
    FQDN/通配/IP，示例有效期 20 年）；结束重启 OXE。产物核验：cd /usr3/mao/DM/VHE8082/ 下应见
    ctl_VHE8082 与 ict8000ctl.pem。
  conditions: 安装默认证书只适配 WBM，不适配 SIP 客户端；外部 CA 亦可替代内部 PKI
  tags: [flow, pki, certificate, ctl, menu-path]

- id: f31
  title: ALE-2/ALE-3 话机开通流程骨架——DM 激活 → 参数 → 建户 → DHCP → MAC
  type: flow
  source_pages: p172-186
  source_chapter: ALE-2/ALE-3 SIP Deskphone (How-To)
  source_quote: |
    "Activate the OXE Device Management module in the OXE database. To do it, you must disable the
    'Device Management in 8770' parameter." (p174)
    "ALE-2/ALE-3 devices belong to a DHCP class, named 'ALE-2X' and use a Vendor Class ID (VCI)
    called 'aledevice'" (p181)
  summary: |
    六段：①前提（FQDN 已建、证书已生成、CTL 在 usr3/mao/DM/VHE8082）与 DM 激活（WBM System/Other
    System Param. 关 "Device Management in 8770"）；②SIP Phone COS（Display call server information、
    3PCC 优化、NOTIFY 代 MESSAGE）；③DM profile（LDAP、DNS/SNTP、DTMF、SBC=No、话务特性、admin
    密码/SSH）；④建户（31033，SIP Extension，子型 ALE-2/ALE-3，DM profile 3，Phone COS 0）+ 防火墙
    信任主机；⑤部署——SSL 安全级按话机年龄决定是否降级、DHCP（启用 dhcpd、建范围 192.168.1.161-164、
    ALE-2X 类 TFTP URL https://<OXE Main IP|FQDN>/dmictouch、子网 DNS、Apply Modifications）；
    ⑥注册——话机置 DHCP 模式，MAC 手工绑定或 auto-discovery（分机号+密码默认 0000）。维护：sipregister/
    dmictouch 目录/nginx access.log（401 序列）/downbin。
  conditions: 实验口径地址；混合 8770 关闭将清空其配置文件（p174 warning）
  tags: [flow, ale-2-3, dhcp, auto-discovery, menu-path]

- id: f32
  title: ALE-x00 双分区切换状态图——Force Download 两态 × 切换时机
  type: flow
  source_pages: p188-194
  source_chapter: ALE -300/400/500 DEVICES DUAL PARTITION
  source_quote: |
    "From the binary version R200, out-of-the-box Deskphones include both binaries (NOE and SIP). But
    these are not necessarily the latest versions available on the CS" (p188)
    "If parameter is set to « Yes » ... As SIP binary was pre-loaded on the inactive partition, the
    switch is fast, and the device will restart directly in SIP mode" (p193-194)
  summary: |
    状态图：新机（<R200）首连只有 NOE 分区 → 后台升级 NOE（与参数无关）→ Force Download=NO 时对侧
    分区不动，切换 NOE→SIP 时现场下载 SIP 二进制（慢）；=YES 时后台预载对侧（SIP 1.00.07 例），切换
    即快切重启进 SIP。R200 起出厂双分区都在，但版本未必最新，仍建议 Force 预载。版本核对走 MMI
    （Menu/Settings/Phone/Local Menu/About/Software 或 Options/Version）。
  conditions: 双栈机（ALE-300/400/500、ALE-30）；首次 SIP 二进制下载可达 30 分钟（p200）
  tags: [flow, dual-partition, force-download, ale-x00]

- id: f33
  title: ALE-x00 SIP 化两条开通路径 + 三种模式切换触发
  type: structure
  source_pages: p196-216
  source_chapter: ALE-x00 Deskphone in SIP mode, using OXE SIP DM (How-To)
  source_quote: |
    "The commissioning of an ALE-x00 SIP station can be done in 2 ways: • Either switch an existing
    NOE user in SIP mode (see management step 7.1) • Either create from scratch a new SIP extension
    user in the OXE DB (see management step 7.2)" (p207)
    "A NOE equipment uses the Vendor Class ID (VCI) called 'alcatel.noe.0'. So, the class using this
    VCI must be updated, to allow an automatic switch from NOE to SIP ... A configuration file
    ('sipconfig.txt') has to be specified in the class." (p214)
  summary: |
    开通两路：①存量 NOE 用户切换——Users 选设备点 "Change NOE to SIP" → OK → 核对子型自动带出/
    补 DM profile/Phone COS；②全新建户（31034 Ellington Edgar，子型 ALE-300，DM profile 3，COS 0）
    → 话机强制 SIP 启动（上电按 "I" 或 "*#" → Software Infos → Run Mode=SIP）→ DHCP 模式 → MAC
    绑定或 auto-discovery。模式切换三触发：WBM 按钮（逐台）、DHCP 类触发（NOE 类 alcatel.noe.0 配
    sipconfig.txt 为 boot file，整机批切；外部 DHCP 用 option 67）、话机 MMI 手动（Settings →
    Advanced Settings → Maintenance → Run Mode → Switch；SIP→NOE 同路）。
  conditions: DHCP 触发法仅限"系统内无其他 NOE 设备"或外部 DHCP 可设专用用户类（p214 warning 前提）
  tags: [structure, ale-x00, noe-to-sip, dhcp-trigger, menu-path]

- id: f34
  title: ALES 开通主线（PC/Android）——LDAP → 代理 → COS → DM profile → 建户 → 安装登录
  type: flow
  source_pages: p217-270
  source_chapter: ALE SoftPhone on PC / on Android (How-To)
  source_quote: |
    "Configure the SIP proxy to match the major requirements for ALES deployment ... Minimal
    authentication method SIP Digest, Framework period 3 (seconds), Framework Nb Message By Period
    50, TCP when long messages Checked (specially for remote workers)" (p227)
    "Keep Alive NO. For ALES Mobile, this 'Keep Alive' option is mandatory to be set 'NO' to be
    compatible with the Push Notification mechanism" (p252)
  summary: |
    七段：①外部 LDAP 认证（LDAPExplorerTool 探目录；swinst：Expert→System management→User's
    accounts management→User authentication→Configure LDAP authentication，参数 Realm/Hostname/
    Port 389/Scheme ldap:///Search Base DN/Login attribute uid/Bind DN/密码；再 Enable；nginx 重启
    提示）；②SIP 代理（SIP Digest + Framework 3s/50 条防隔离 + TCP 长消息勾选）；③SIP Phone COS
    （NOTIFY 代 MESSAGE；Android 版 Keep Alive 必须关闭以兼容推送）；④DM profile（LDAP 搜索映射
    givenname/sn/telephonenumber；Android 版 Config update polling timer ≥21600s；拨号规则；
    话务特性）；⑤建户（Set type=SIP extension，Sub type=ALES-desktop/ALES-mobile，Login=LDAP uid，
    密码留空）+ Facilities 勾 Dial by name + Phone COS；⑥装软件（msi：本地访问填 OXE 主 IP 或节点
    名；Android 走 Play Store，连 RAP SSID）→ 登录（实验口径 alcatel）→ 首连接受证书（可 GPO 预铺
    ROOT CA）；⑦维护六命令 + 寻线组/监督/视频三实验 + 切本地认证（先关 LDAP，配 Superuser1245*，
    首连改 Administrator2580!，实验口径）。
  conditions: 实验口令均为实验口径；视频实验在 Rlab 虚拟桌面不可测（Guacamole 不支持，p241 note）
  tags: [flow, ales, ldap, push, menu-path]

- id: f35
  title: swinst 认证管理菜单路径——LDAP/本地/OpenID 三入口与互斥切换
  type: menu-path
  source_pages: p225-226, p242-243
  source_chapter: ALE SoftPhone / Switch from external to local authentication
  source_quote: |
    "swinst menu Log as swinst Choice 2: Expert menu Choice 6: System management Choice 5: User's
    accounts management Choice 5: User authentication Choice 1: Configure LDAP authentication" (p225)
    "User Authentication menu 1 Configure LDAP authentication 2 Configure OpenID Connect
    authentication 3 Use local authentication" (p243)
  summary: |
    路径：CS 登录 swinst → 2 Expert menu → 6 System management → 5 User's accounts management →
    5 User authentication → 1 Configure LDAP authentication（2 Create/Modify LDAP server；3 Enable/
    Disable）或 3 Use local authentication；退出时提示动态重配并重启 nginx（答 y）。互斥规则：外部与
    本地先关后开（两处 Warning）；菜单里已有 OpenID Connect 配置入口（2），书中标注 planned（p163）。
    切本地后必须给每个 ALES 用户配密码（外部认证时该字段不要求）。
  conditions: 实验认证参数（192.168.1.252/389/uid/cn=admin...）为实验口径
  tags: [menu-path, swinst, authentication]

- id: f36
  title: 编解码协商决策链——系统 → 域 → DM → 终端 → 链路/网关 → 优先级排序
  type: flow
  source_pages: p272-281
  source_chapter: CODECS NEGOTIATION
  source_quote: |
    "Policy : select the codec with highest quality, depending on terminal capabilities and on
    configuration (system parameters, IP domain, SIP external gateway, Direct IP link) • High
    bandwidth : OPUS SWB > OPUS WB > G.722 > G.711 > OPUS NB > G.729 • Low bandwidth : OPUS NB >
    G.729" (p281)
    "Important: G711 is required for OPUS/G722 -> in case of connection to GD/OMS" (p280)
  summary: |
    决策链五层：①系统参数——法线（A/μ 随国家）、Accept Mu and A law in SIP（关则他法线来话回 488）、
    G722/OPUS 支持域三档（Network and local/Local only/Not available）；②IP 域——域内带宽（建议高）
    与跨域带宽（建议低；高=OPUS SWB/WB、G722、G711、OPUS NB、G729；低=仅 OPUS NB、G729）；③DM
    profile 与用户 SIP profile（≤5 编解码，G729 与一份 G711 必选）；④终端能力（设备能力矩阵见
    principle）；⑤网络呼叫看 Direct Link 两侧带宽一致、外线看外部网关四开关（OPUS/G722 开必须连带
    G711；对端 SDP 也要带）。最终按优先级选最高质量；资源分配优先取同域媒体资源，跨域按动态负载列表
    （OXE-MS 排最前，因支持 OPUS/G722）。
  conditions: G723 不支持；8058s/68s/78s(OPUS 仅 SWB) 等特例见设备矩阵
  tags: [flow, codecs, negotiation, priority]

- id: f37
  title: SEPLOS 业务激活三型与 DTMF 三法——前缀/前缀+信息/后缀 + 183 开媒体
  type: flow
  source_pages: p304-310
  source_chapter: SIP TRACES / Phone features activation
  source_quote: |
    "Use of a prefix only • Lock the phone set: dialing of the prefix (number 45) ... Group call
    pickup: dialing of the prefix (number 56) ... Use of a prefix with information • Immediate
    forward: dialing of the prefix (number 51) + destination directory number • Use of a suffix •
    Call back on busy phone: dialing of the suffix (number 5)" (p304)
    "When the 'Invite' message is sent with the prefix number corresponding to the phone facility,
    the Call Server sends a '183 Progress' message with an SDP to be able to open a RTP flux for: The
    broadcast of a voice guide ... The reception of the DTMF digits" (p305)
  summary: |
    业务激活三型：①纯前缀（锁机 45、组代接 56——INVITE 到 45/56@域名，488+CANCEL 收尾）；②前缀+
    信息（立即呼转 51+目标号；取消 41 等）；③后缀（遇忙回拨 5）。媒体机制：CS 以 183 Progress+SDP
    开 RTP 通道放语音指南并收 DTMF（DTMF 三法：RFC4733 载荷/INFO 消息/带内，方法在 DM profile 定；
    INFO 报文 Body Signal=N 逐位发送）。压缩资源只在此类场景被占用，常规呼叫全程直连 RTP。
  conditions: 前缀 45/56/51/41/5 为示例系统默认编号，实际以系统编号计划为准
  tags: [flow, prefixes, dtmf, voice-guide]

- id: f38
  title: SIP 跟踪工具箱结构——motortrace/traced、oxetrace、mtracer、sipdump 四工具
  type: structure
  source_pages: p288, p312-327
  source_chapter: MAINTENANCE & SIP TRACES / SIP traces and tools (How-To)
  source_quote: |
    "motortrace (v6.0.0) verbosity = 00000000 sipmotor trace-level set 1 (Basic trace)" (p288)
    "SIP Gateway resources menu 1 - Dump the gateway management datas ... 7 - Release a call ...
    11 - SIP traces filters 17 - Manage the stack resources number" (p321)
  summary: |
    四工具分工：①motortrace N + traced——轻量信令流（级别 0-b 可调：1 基本、2 大流量观察、3 定向深挖、
    4 +认证、5 +媒体、8 全部+传输+DNS 等），Ctrl-C 停；②oxetrace——问题导向菜单（7 问：Trunks?/
    Endpoint?/Audio?/Display?/Remote Extension(Rainbow)/Nomadic?/Attendant?/通用场景？+actdbg 过滤
    /tuner/tcpdump 开关/motortrace 级别），产出 /tmpd/<名>_<时间戳>/ 三目录并自动解码打包 zip，
    Filezilla sftp 取回，pcap 进 Wireshark（SIP 过滤、SDP、Telephony/VoIP Calls 流程图）；③mtracer
    ——应用级跟踪（tuner km / clear-traces / +cpl +cpu +at；actdbg csip=on；mtracer -a；收尾
    actdbg all=off + dhs3_init -R MTRACER）；④sipdump——网关资源与呼叫态（17 项菜单：许可/呼叫数/
    neqt 映射/呼叫清单/转储/强拆/订阅/过滤等；需双连接：菜单口+traced 口）。
  conditions: motortrace 级别表与 sipdump 菜单全项转写见 principle/case
  tags: [structure, traces, tools, troubleshooting]

- id: f39
  title: 外部网关进出呼叫判定流程——目的地三判 + 来源三判
  type: flow
  source_pages: p330-332
  source_chapter: CALLS WITH EXTERNAL SIP GATEWAY
  source_quote: |
    "FIRST STEP: The domain part of the 'ReqURI' matches with the OXE_Address parameter (Local
    Gateway) ... SECOND STEP: The P-Asserted-ID header is present, and its domain part matches with
    the RemoteDomain of an External Gateway" (p330)
  summary: |
    入向两步：第一步判定 OXE 是否终点——Request URI 域部分匹配本地网关的 OXE_Address / Machine
    Name / Machine Name+DNS 域名任一，是则送 Call Handling；第二步判定来源——依次查 P-Asserted-ID
    域 → (无 P-Asserted-ID 时) From 域 → Via 头域，匹配某外部网关 RemoteDomain 则归入其关联中继组，
    随后 DID 翻译换内线号振铃（8 步图）。出向六步：ARS 表选中继组+外部网关 → NPD 拼号码 → INVITE
    按外部网关声明构建（From=Belonging domain、To=Remote domain、P-Asserted-ID 默认同 From、
    Contact=OXE_Address 或 FQDN）→ 发网。
  conditions: 判定顺序固定；外部网关字段语义（Belonging/Remote domain、Registration ID 等）见 p354 notes
  tags: [flow, external-gateway, incoming, outgoing]

- id: f40
  title: OTSBC 定位与部署主步骤——SBC 五职能 + 四段部署
  type: structure
  source_pages: p336-345
  source_chapter: OTSBC FOR SIP TRUNKING
  source_quote: |
    "SBC: Session Border Controller • A device to protect and regulates IP communications flows
    ... NAT Traversal ... Quality of service and CAC ... Signaling conversion (protocol interworking)
    ... Codecs conversion" (p337)
    "OTSBC DEPLOYMENT MAIN STEPS • Virtual machine deployment • OVF template upload or fresh
    installation from iso file • IP settings • Web interface • Wizard use • Additional configuration"
    (p345)
  summary: |
    SBC 定位五职能：会话与媒体（RTP/SRTP）管理与安全、NAT 穿越地址翻译、QoS 与 CAC 拥塞限呼、信令
    转换（协议互通）、编解码转换与会话路由（Proxy ToIP）。SIP trunking 用例六动作：NAT 翻译、认证、
    SIP 消息适配、编解码适配、号码修改、加解密（示例：From 域改写、去 +、SDP 内设备 IP 换公网、
    G729/G711 两侧协商）。部署四段：VM（OVF 或 ISO，MyPortal 有软件）→ CLI 配 LAN 口（AudioCodes
    Mediant：Admin/Admin，network-if 0 设 192.168.1.105/24 GW 192.168.1.254，write + reload now）→
    Web 界面（默认 3 通道许可，可录 key）→ 向导 + 补充配置。DNS 双侧：公共 DNS 解外部 FQDN，内部
    DNS 解 OXE FQDN 与 SBC 内网 FQDN（NAT 配对）。
  conditions: 训练拓扑 OTSBC LAN 192.168.1.105 / DMZ 192.168.2.105 / NAT 12.C.P2.105（实验口径）
  tags: [structure, ot-sbc, sbc, deployment]

- id: f41
  title: OXE 侧 SBC 运营商接入配置主线——防火墙 → 系统参数 → TG → ExtGW → ARS → DID/NPD → 回拨
  type: flow
  source_pages: p347-363
  source_chapter: SIP Carrier access via SBC (How-To)
  source_quote: |
    "Warning ARS IS REQUIRED TO USE SIP TRUNK GROUP WITH AN EXTERNAL SIP GATEWAY" (p355)
    "First External Number Enter the first DID number corresponding to your system, example: 33920131000
    for POD 1" (p359)
  summary: |
    七段主线：①内部防火墙信任主机（root → netadmin 11/1/3/2：sbc 192.168.1.105；双机用 Copy set up
    同步；more /etc/hosts 核对）；②系统参数（法线 A/μ；Compression Parameters 里 G722/OPUS 支持域）；
    ③SIP 中继组（TG 2：T2、Q931 ISDN all countries、T2 Specification=SIP）；④外部 SIP 网关（3 号
    ITSP2_GW：Remote domain=SBC LAN 地址 192.168.1.105、5060/UDP、注册与凭据留空交 SBC、四编解码
    开关）；⑤ARS（前缀 0 → 逻辑判别器 0；TG 关联 ExtGW；ARS 路由表 9：去 1 位加 33；时间路由清单；
    0 公共判别器规则 10 位；entity 判别器选择器关联逻辑↔实际）；⑥DID 翻译（33920x31000、范围 1000）
    + NPD 34（ISDN International、默认号、双向 DID 标识）+ 中继组 NPD 选择器；⑦回拨翻译（DEFAULT 表
    加 A33：去 3 位加 00）。维护：sipextgw -l/-g 3、trkstat -r 2。
  conditions: 每个运营商参数不同，须按 TC2005 与运营商文档（p349 warning）；OTSBC 未配好前 ExtGW 不工作
  tags: [flow, sbc, ars, did, npd, menu-path]

- id: f42
  title: OTSBC 向导步骤结构——八屏配置流 + 重启换 HTTPS
  type: flow
  source_pages: p368-373
  source_chapter: OTSBC deployment / Wizard use
  source_quote: |
    "Select the template for the following case PBX: OXE, Generic SIP Trunk, 2 ports: LAN and WAN"
    (p369)
    "Warning AFTER THE REBOOT, AS SPECIFIED IN SYSTEM SETTINGS WITH THE WIZARD, THE SBC WILL USE
    HTTPS. AS IT IS FOR THE MOMENT A GENERIC CERTIFICATE, YOU HAVE TO ACCEPT IT TO ACCESS TO WEB
    INTERFACE" (p373)
  summary: |
    向导八屏：①WELCOME（模板可 Update from Remote Server）；②GENERAL SETUP（IP-PBX=ALE OXE +
    SIP-Trunk=Generic + 两口拓扑）；③SYSTEM（HTTPS/SSH、Syslog 发 192.168.1.10、NTP 10.20.30.250、
    时区）；④INTERFACES（LAN 192.168.1.105 / WAN 192.168.2.105 / NAT 公网 12.C.P2.105 / OAM=LAN）；
    ⑤IP-PBX（地址与 SIP 域=192.168.1.3）；⑥SIP TRUNK（gateway.itsp2.com + itsp2.fr）；⑦SIP ACCOUNT
    （Registration 型，用户 podx，密码 alcatel——实验口径；ITSP 认证由 SBC 代做）；⑧NUMBER
    MANIPULATION（出向去 +、入向加 +）→ SUMMARY（可 Save INI 或 Apply & Reset）。重启后须接受通用
    证书；向导产物全部可手工改。
  conditions: 实验口径地址与账号；生产按运营商参数调整
  tags: [flow, ot-sbc, wizard, menu-path]

- id: f43
  title: OTSBC 排障修正三步——编解码放行 → 消息域改写 → 注册 Contact User
  type: flow
  source_pages: p374-383
  source_chapter: OTSBC deployment / Manual configuration of parameters
  source_quote: |
    "SETUP / SIGNALING & MEDIA / CODERS & PROFILES / Allowed Audio Coders Groups Select the audio
    coders group used by OXE: 1 ... By default, only 2 coders were configured by the wizard." (p375)
    "Put the login expected (podX) by the ITSP gateway in the field 'Contact User'" (p382)
  summary: |
    实验"先失败后修"三连：①呼出单通 G711——向导只给了 2 个 coder；Allowed Audio Coders Groups 组 1
    点 New 加 G729（Apply+Save）；②呼出被 ITSP 拒——INVITE/REGISTER 的 From/Proxy Authorization 域
    是 OXE IP，ITSP 不认；Message Manipulations 建规则组 1（header.from.url.host / header.to.url.host
    → Modify 'itsp2.fr'），绑到 ITSP IP Group 的 Outbound Message Manipulation Set；③来话不通——
    SBC 未注册成功：Accounts 里给向导建的账号补 Contact User=podX，Action 菜单 Register 即时注册，
    REGISTER 变 podX@itsp2.fr 后来话打通。每步都以 Syslog 报文对照收口。
  conditions: 排障叙事为实验路径，生产按实际 ITSP 反馈定位
  tags: [flow, ot-sbc, troubleshooting, message-manipulation]

- id: f44
  title: 远程办公方案结构——ALES 两条路 + 话机两条路 + 原生加密
  type: structure
  source_pages: p384-420
  source_chapter: REMOTE WORKERS SOLUTIONS FOR SIP ALE EQUIPMENT'S
  source_quote: |
    "For small configuration (<= 500 remote users), it is possible to use the OTSBC embedded Reverse
    Proxy • If more, ALE recommends NGINX PLUS reverse proxy delivered by NGINX company, member of
    DSPP" (p387)
    "ALE-2, ALE-3 SIP basic Deskphones embed a VPN client ... ALE-2/ALE-3 only support OpenVPN, not
    IPSec VPN" (p412)
  summary: |
    方案矩阵：ALES 软终端——SBC/反代（三步：RP 拉 DM 配置→配置内含 SBC 地址 rpsbcX:5261→经 SBC 注册；
    ≤500 用户用 OTSBC 内嵌 RP，更多用 NGINX PLUS）或 VPN（第三方 VPN 客户端，ALE 不提供）。SIP 话机
    ——SBC/RP/EDS（话机靠证书被 RP/SBC/EDS 认证；两用例：LAN↔WAN 搬迁、EDS 零touch）或 VPN（仅
    ALE-2/3，内嵌 OpenVPN，TLS 认证+凭证+证书，EDS 可下发 VPN 配置；兼容网关清单见部署指南）。原生
    加密：OXE N4 起远程工人可开用户级加密（经 REGISTER Via 头里的 SBC IP 动态识别，传输模式不匹配也
    放行；新菜单最多登记 10 个 SBC LAN IP，自动进 SIP 信任主机）；四种拓扑决定 LAN 段 RTP 是否加密。
  conditions: DM profile 远程参数（双 SBC/双 RP/备用 LDAP）见 p407；证书四方信任链见 f46
  tags: [structure, remote-worker, sbc, rp, eds, vpn, encryption]

- id: f45
  title: 话机远程两用例时序——LAN→WAN 搬迁与 EDS 零touch
  type: flow
  source_pages: p400-406
  source_chapter: SIP ALE DESKPHONES - TOPOLOGY THROUGH SBC/RP/EDS
  source_quote: |
    "Phone uses the private OXE DM URL to try to retrieve SIP config file, which fails, and falls back
    using saved RP@" (p403)
    "Out of the box, boots in NOE mode, and contacts EDS since no DM URL provisioned (manual,DHCP
    opt,…) ... Mutual authentication with RP" (p404)
  summary: |
    用例 1（LAN→WAN）：LAN 起步时配置已含 RP FQDN/OTSBC FQDN/CTL/外部 DNS/LDAP → 到异地 DHCP 拿
    基础网参 → 私网 DM URL 拉配置失败 → 回退用已存 RP 地址 → 经 RP 取配置与 CTL → SIP TLS REGISTER
    经 SBC（话机证书认 SBC；SBC/OXE 以 SIP Digest 认话机）→ 双向 NOTIFY 识别（PBX identification/
    Phone identification）。用例 2（零touch）：出厂 NOE 起步、无 DM URL → 联系 EDS（FQDN 硬编码
    device.eds.al-enterprise.com）→ 切 SIP + 下发 RP FQDN 与 RP 根证书（Profile 里 URL=https://<RP
    域>/DM/dmictouch，可预配备用 RP）→ 重启进 SIP → 与 RP 双向证书认证 → 拉 DM 文件与 CTL → 经
    SBC 注册。ALE-x00/ALE-30 须双栈或已在 SIP；ALE-2/3 不能动态搬迁（须先切目标位置专用 DM profile）。
  conditions: 零touch 限制：无出向 HTTP 代理、无 802.1x、无 VLAN、暂无 Wi-Fi（p404）
  tags: [flow, eds, zero-touch, lan-wan, remote-worker]

- id: f46
  title: 远程办公证书四方信任链结构——话机/RP/SBC/OXE DM/EDS 五个信任库
  type: diagram
  source_pages: p408-410
  source_chapter: AUTHENTICATION ON REMOTE WORKER DEPLOYMENT (Summarize)
  source_quote: |
    "ALE Cloud Connect CA certificate is installed by default in the set's trust store (this CA has
    issued EDS's certificate) ... OT-SBC CA certificate must be imported in the OXE, so that OXE DM
    can included them in the CTL file" (p408)
  summary: |
    信任链五库：①话机信任库——默认含 ALE Cloud Connect CA（签发 EDS 证书）；SBC 与 RP 的 CA 链经
    OXE DM 的 CTL 下发（零touch 亦可由 EDS 给）；②RP 信任库——装 ALE Terminals RootCA/SubCAs（验
    话机出厂证书；话机侧 mTLS）；③OXE DM（经 RP 认证）——证书级；④OT SBC 信任库——装 OXE 加密网关
    RootCA/SubCA（加密拓扑用）；⑤EDS 信任库——默认装 ALE Terminals RootCA/SubCAs，并须导入 RP CA
    才能给零touch 话机放行。补充规则：话机↔SBC 是服务器证书认证 + SIP Digest 用户认证；话机↔RP 与
    话机↔EDS 是双向 TLS；若混合部署 ALES，RP 要按证书认话机、按 LDAP 认 ALES。
  conditions: 各库证书导入动作分散在 OXE/RP/EDS 三侧管理界面，书中给清单不逐步演示
  tags: [diagram, certificates, trust-store, remote-worker]

- id: f47
  title: OTSBC 内嵌反代配置主线——TLS context → RP 三件套 → SBC 六对象 → 操纵与路由
  type: flow
  source_pages: p421-449
  source_chapter: OTSBC with embedded Reverse Proxy for remote workers (How-To)
  source_quote: |
    "SETUP/IP NETWORK/HTTP PROXY/HTTP Proxy Servers ... URL Pattern /DM/dmsoftphone/ URL Pattern Type
    Prefix Upstream Scheme HTTPS Upstream Group OXE_443" (p434-435)
    "Create a message condition rule in order to make a difference for SIP traffic coming from OXE
    between the traffic at ITSP destination and remote workers destination." (p447)
  summary: |
    七段主线：①证书——新建 TLS Context（Remote_Workers：TLSv1.1/1.2、DH 2048），导 Root CA
    （ca-certgen），生成私钥+CSR（Subject=rpsbcX.company.com，SAN 可加 rp1/sbc1）→ 外部 CA 签发后
    Load Device Certificate；②RP 激活（HTTP Proxy application Enable + DNS，保存后必须重启）；③RP
    三件套——Upstream Group OXE_443（Host 192.168.1.3:443）+ Upstream Host + HTTP Proxy Server
    （RP_oxe_443：公网域名、WAN eth1:443、TLS Context、不验客户端证书）+ HTTP Location（/DM/
    dmsoftphone/ 前缀 → HTTPS → OXE_443，出向 eth0）；④SBC 媒体（Media Security Mandatory +
    AES-CM-128-HMAC-SHA1-80；NAT Only if Necessary）；⑤远程对象六件——SIP Interface 3（TLS 5261、
    Accept Registered Users）、Media Realm（6000 起 100 腿）、NAT 翻译（5261 与 6000-6399 → 公网
    12.C.P2.105）、IP Profile（Secured、Diffserv 40）、IP Group RemoteUsers（User 型 + TLS context +
    操纵组 3）、Classification（sipinterface3 + 目的地 rpsbcX → RemoteUsers）；⑥消息操纵——组 3 改
    to/from/Refer-To/Referred-By 的 url.host 为 'rpsbcX.company.com:5261'；OXE 组 2 追加条件规则
    （host 含 rpsbcX → 改 'oxe'）；⑦路由——Message Condition 'To ITSP'（header.to 含 SBC IP
    192.168.1.105）区分 ITSP 流量与远程流量；IP-to-IP 路由改挂条件，并加两条（OXE→All Users、
    RemoteUsers→OXE 组）。
  conditions: 公网 IP 12.C.P2.105（C=class，P=POD）为实验口径；RP 证书也可与 OTSBC 共用一张
  tags: [flow, reverse-proxy, ot-sbc, remote-worker, menu-path]

- id: f48
  title: ALES Remote Worker 配置与验证主线——DM profile(SBC) → 用户挂 profile → 异地登录
  type: flow
  source_pages: p450-458
  source_chapter: ALES Remote Worker (How-To)
  source_quote: |
    "Create a new DM profile for remote worker mode use: ID: 2, Name: Remote Workers, SBC: SBC and
    LAN, Outbound proxy and RP addresses: rpsbcX.company.com (X is the pod number), Outbound proxy
    port: 5261" (p451)
    "Using 'sipregister' command ... Address of record : 31030 contact : sip:FEU461-3-2-1@192.168.1.105,
    udp, 3543 s" (p458)
  summary: |
    四段：①前提——OTSBC LAN 地址已是 CS 信任主机（netadmin，同 SBC 接入实验）；②DM profile 2
    （SBC=SBC and LAN、outbound proxy 地址 rpsbcX.company.com、端口 5261、Reverse proxy FQDN 同址；
    其余沿用经典 ALES profile；也可并入默认 profile 0；部分用户远程时建议专用 profile）；③用户挂
    profile（Users/<user>/SIP → DM profile=2；warning：profile 必须先存在）；④验证——远程 PC
    （PODx-outside RDP，注意 RDP in RDP 别关错会话）装 ALES：Local access 填 oxe.company.com、
    Remote access 填 rpsbcX.company.com → 登录（eevans 等，alcatel，实验口径）→ sipregister 里远程
    用户 contact 显示经 SBC（sip:<SBC-trunk-id>@192.168.1.105）。
  conditions: 实验口径；本地/远程双地址是安装程序的两个入口字段
  tags: [flow, ales, remote-worker, dm-profile, menu-path]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-20）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 准备实验/交付环境 | 有 | f02, f03, f06 | 两版 POD 拓扑/账号表 + 准备流程骨架 |
| task-02 | 掌握运营商模拟器 | 有 | f04, f05 | ITSP1 直连与 ITSP2 经 SBC 结构及号码变换 |
| task-03 | POD 预配置收尾与外线打通 | 有 | f06 | 网关 POD 参数 + DID 翻译在流程第 4 段 |
| task-04 | 掌握 SIP 协议机理 | 有 | f07, f08, f09, f10 | 协议栈/消息码表/实体角色/注册与呼叫时序 |
| task-05 | OXE 域名与空间冗余 | 有 | f12, f13 | 冗余解析机制 + netadmin 19 路径 |
| task-06 | SEPLOS vs SIP Device 选型 | 有 | f14, f16 | 两形态对比结构 + 互通流程 |
| task-07 | SIP Device 开通 | 有 | f17, f18 | 九节主线 + 维护命令族 |
| task-08 | 终端家族选型 | 有 | f19 | 家族谱系与功能矩阵结构（数值在 principle） |
| task-09 | ALES 认证设计 | 有 | f34, f35 | 开通主线第 1 段 + swinst 菜单路径 |
| task-10 | ALE SIP 特性配置 | 有 | f20, f21, f22, f23, f24, f25 | GUI/一号多机/监督/多终端/寻线组/RCC 机制 |
| task-11 | SIP DM 选型与规划 | 有 | f26, f27, f28, f29 | OXE vs 8770、profile 体系、配置文件机制、二进制 |
| task-12 | OXE DM 证书定制 | 有 | f30 | 内部 PKI 流程与 CTL 产物 |
| task-13 | ALE-2/3 话机开通 | 有 | f31, f15 | 开通骨架 + SEPLOS 四步通用链 |
| task-14 | ALE-x00 双分区与切换 | 有 | f32, f33 | 切换状态图 + 两条开通路径与三触发 |
| task-15 | ALES 软终端开通 | 有 | f34, f35 | PC/Android 主线 + swinst 路径 |
| task-16 | 编解码协商与验证 | 有 | f36 | 五层决策链（compvisu 命令在 case/c09） |
| task-17 | SIP 跟踪采集与分析 | 有 | f38 | 四工具结构（菜单全项与级别表在 principle/case） |
| task-18 | 外部网关判定 + OXE 侧 SBC 接入 | 有 | f39, f41 | 进出判定流程 + 七段配置主线 |
| task-19 | OTSBC 部署调通 | 有 | f40, f42, f43 | SBC 定位 + 向导八屏 + 排障三步 |
| task-20 | 远程办公规划与落地 | 有 | f44, f45, f46, f47, f48 | 方案矩阵、两用例时序、证书信任链、反代主线、验证主线 |

补充说明：
- f01（课程主线）为 BOOK_OVERVIEW 骨架 1-9 的组织轴，不单独对应某 task。
- 全部 20 项 task 均有框架类条目覆盖，无空缺；逐格数值（锁号、上限、端口、级别表、容量）留待 principle 提取器，分步命令与验收问题留待 case 提取器。
- 生产化边界提示（来自 BOOK_OVERVIEW 批判节）：外线参数指向 TC2005 与运营商文档；远程办公指向 TC2957、EDS user manual、Server deployment Guide for Remote workers；功能矩阵指向 OXE Features List。
