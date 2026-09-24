# 框架/流程/结构候选 — OpenTouch Advanced (OPENXTE301EN Ed08, R2.6.1)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、平台/界面分区。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——实验地基 → 移动性 → 消息/目录 → 协作 → 安全认证
  type: flow
  source_pages: p3-468
  source_chapter: 全书章节编排（每主题"讲义+How-To"配对）
  source_quote: |
    "OpenTouch - Advanced / Fully Virtualized (RLAB only, no classroom equipment) / Training lab environment" (p3)
    "OTC PC for Connection users in nomadic mode — How to Configure Nomadic Mode for Connection users" (p45)
    "Unified Messaging (Exchange server based) — How to Bring into service the Unified Messaging" (p182)
  summary: |
    全书 11 个主题域按依赖顺序推进：①RLAB 实验环境与 Pod 配置（p3-30，两套 How-To：环境说明 + Pod 配置）；②Nomadic 移动（p31-57，讲义 + How-To）；③Desksharing（p58-75）；④OTC 智能手机（p76-147，讲义 + 远程接入 How-To + 智能手机 How-To）；⑤Extended Mobility（p148-167）；⑥统一消息（p168-217）；⑦目录搜索 UDAS（p218-263）；⑧协作与会议（p264-362，讲义 + 会议服务器配置 How-To + 数据会议 How-To）；⑨DCS（p363-383）；⑩日历同步（p384-414，含 TC2258 附录）；⑪外部认证（p415-467，讲义 + LDAP/Kerberos/RADIUS/FreeRADIUS 四个 How-To）。这是实际交付项目的推荐顺序：先打通道（远程接入），再配终端（手机/nomadic），再接企业系统（邮件/目录/认证）。
  conditions: 无特殊版本前提；各章版本前提在对应条目标注
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: RLAB 实验 POD 两种拓扑——全虚拟化与混合课堂模式
  type: structure
  source_pages: p3-18
  source_chapter: OpenTouch Pod Configuration / Training lab environment
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data center." (p5)
    "Pods are independent of each other • Pods have the same configuration • Pods have access to common resources" (p5)
    "Hybrid mode (RLAB + classroom equipment)" (p11)
  summary: |
    POD 结构两层：POD 1..n 相互独立、配置相同；公共资源区（10.20.30.x）放 NAS（软件、许可）与 SIP 模拟器，外部 DNS 10.20.30.254。全虚拟化 POD（192.168.1.x 网段）含 8 台虚机：OXE（csa/csm，192.16.8.1.1/192.16.8.1.3，实验口径原文如此）、OMS（192.168.1.13）、OpenTouch/OTMS（192.168.1.50）、8770（nms，192.168.1.70）、DCS（192.168.1.31）、ECOSYSTEM（eco，192.168.1.100）、PC Client 10/11（192.168.1.10/11）；内部 DNS 192.168.1.254。混合模式增加课堂硬件（MIX484 GD4、ALE-300/20h/30h/500、POE Switch、PC Classroom 192.168.1.9、GD4 192.168.1.12），且用户 31000/31001 需从 IPDSP 改为实机类型。PC Client 10 预装 2 个 MicroSIP 模拟公网号码。
  conditions: 仅培训环境；所有 IP/账号为实验口径；混合模式用户设备类型要按课堂实机改
  tags: [structure, lab, rlab, topology]

- id: f03
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则
  type: diagram
  source_pages: p19-23
  source_chapter: SIP Carrier Simulator
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... ITSP1 Public gateway public.itsp1.com 10.20.30.50" (p20)
    "PBX (POD P) Id: pbxP password: alcatel ... SIP domain: sip.itsp1.fr" (p20)
    "The main number of the SIP user Public is 3321PN12345." (p21)
  summary: |
    模拟器扮演出局运营商：SIP 网关 gateway1.itsp1.com（10.20.30.51，PBX 注册账号 pbxP/alcatel，SIP 域 sip.itsp1.fr）+ 公网网关 public.itsp1.com（10.20.30.50，2 个 MicroSIP 模拟 Public/urgence 两 SIP 用户，域名 itsp1.fr）。号码规则：PN 为两位 POD 号；国内 3311PN12345/3321PN12345（主号）/3331PN12345/3341PN12345/3351PN12345，移动 3361PN12345/3371PN12345，国际（英国 44）4421PN12345，紧急 112/15/17/18；呼出变换示例：拨 0110312345 → 送出 +33110312345。呼入本 PBX：安装号 3321PN，DDI 表首外线 41000、首内线 31000、范围 500（31001 的外线号 = 3321PN41001）。OXE 侧按 Pod 配置 Registration ID/Outgoing username = pbxN、DID 翻译 First external = 33210N41000。
  conditions: 实验口径（RLAB 专用基础设施）；所有账号/号码为教学约定值
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f04
  title: Connection 用户三操作模式表与 Nomadic 双模式机制
  type: structure
  source_pages: p34-44
  source_chapter: Nomadic mode for Connection users / Definition → Summary table
  source_quote: |
    "The 'Nomadic service' brings complete access to the OpenTouch phone features and other services offered by OTC PC application to remote workers • This service is dedicated to Connection users" (p34)
    "When nomadic mode is activated, the user phone set in the office is frozen and disabled." (p34)
    "Modes / Where to use / Notes: Deskphone control (Office) / Mobility mode aka Nomadic (Anywhere) / Softphone mode (Anywhere)" (p44)
  summary: |
    Connection 用户三种操作模式：Deskphone control（办公室，PC 控制话机）、Mobility/Nomadic（任意地点，关联 PSTN 号或走 VoIP，办公话机冻结，编解码窄带 G.711u/a、G.729a、G.723 + 宽带 G.722.2）、Softphone（任意地点，PC 即话机）。Nomadic 双模式：cellular（蜂窝）——来话经"virtual ghost Z set"改道到任意号码（家庭/手机）；VoIP——经 Ghost Z 改道到多媒体 PC（SIP 信令）。激活入口：OTC PC "routing"窗口选"当前设备"（Route My Calls to: Personal computer / Home phone / Mobile…）。接入前提：反向代理、SBC、Edge 服务器或 VPN 等企业网 IP 通道。
  conditions: 需 Desktop 许可从 OTC PC 激活；VoIP 模式需 SIP 设备池；SIP survivability 不支持
  tags: [structure, nomadic, modes, ghost-z]

- id: f05
  title: Nomadic 资源池机制——Ghost Z 池与 SIP 设备池的定量关系
  type: diagram
  source_pages: p39, p47, p51
  source_chapter: Elements Required / Nomadic in cellular mode / Nomadic in VoIP mode
  source_quote: |
    "The system requires ONE Ghost Z set for each Nomadic connection ... Ghost Z sets are retained as busy throughout the connection and are only released when nomadic mode is disabled. Ghost Z sets are managed as pools of resources." (p47)
    "For each Nomadic SIP connection, the system requires: 1 SIP device ... 1 Ghost Z set" (p51)
  summary: |
    资源池定量结构：蜂窝模式每路连接 1 个 Ghost Z；VoIP 模式每路连接 1 个 Ghost Z + 1 个 SIP 设备（SIP 设备在整个会话期间被该用户占用）。两类资源都是"池"，在连接期间保持占用、关闭 nomadic 才释放——因此并发连接数=所需池规模，必须提前规划。Ghost Z 在 OXE 侧建（Users/ → general Ch. 页签，Set Type Analog + facilities 页签启用 Ghost Z feature=Nomadic），在 OT 侧登记范围（System services/Topology/OXE CS/OXE Resources：Z ghosts min/max value）；SIP 设备在 OXE 侧建（Set Type SIP device + SIP 页签参数）并在 OT 侧声明（OXE SIP Subscriber）。
  conditions: 池规模=最大并发 nomadic 连接数；VoIP 依赖 cellular 配置作为前提
  tags: [diagram, nomadic, capacity, pool, ghost-z]

- id: f06
  title: Desksharing 机制——DSU/DSS 结构与 OTC PC 增强
  type: diagram
  source_pages: p59-61
  source_chapter: Desksharing (lecture)
  source_quote: |
    "OXE desksharing feature allows a connection user (called DSU: DeskSharing User) to use a physical set, called DSS (DeskSharing Set). ... An OXE user configured as 'DSU' doesn't have an associated device" (p59)
    "Allow Connection user to remotely release the deskphone he is logged on from OTC PC (ex: away from office)" (p60)
    "In the case of desksharing (OOS deskphone), a software phoneset (UA) is started on OTC PC in replacement. No deskphone is frozen" (p61)
  summary: |
    机制三层：①OXE 侧 DSU/DSS——DSU 无绑定设备，凭前缀（600 登录/601 登出）+密码使用任意 DSS，直至释放；②OTC PC 远程释放——用户离开办公室也能从客户端释放 DSS，优化共享话机可用率；③nomadic 兼容——一般情况 nomadic 需要在服话机做底，desksharing 场景（话机已登出）由 OTC PC 上的软件话机（UA）替代，故不冻结任何话机；切换 nomadic 前必须先释放 DSS。限制：UA 软件不兼容 WAN（除非 VPN）、不兼容 OTC Mac。
  conditions: UA 仅限 OT 环境（OTC PC + 物理 DSS 并用场景）
  tags: [diagram, desksharing, dsu, dss]

- id: f07
  title: OTC 智能手机配置原理——9 对象清单与自动创建边界
  type: structure
  source_pages: p92-96
  source_chapter: OTC for smartphones / Configuration and installation main steps
  source_quote: |
    "OXE configuration principle is complex and specially for Wifi/dual mode: up to 9 objects have to be managed" (p92)
    "Automatic configuration of these objects when a Smartphone is associated to a Connection user in order to simplify administrator tasks: Remote extension / SIP device / Remote extension Number / Direct Speed Dialing Number / Discriminator Rule / ARS Route list / ARS Route SIP / ARS Route GSM / Tandem" (p94)
    "1-> Automatic creation of OXE objects 2-> Automatic association of REX device to user in OpenTouch" (p93)
  summary: |
    双模式智能手机最多涉及 9 个对象：OXE 侧——远程扩展 DISA 前缀、Ghost Z 池、远程扩展本身、速拨号（自动替换用）、SIP 设备、ARS 管理（ARS 表+识别码）、Tandem；OT 侧——Off site Mobility 权限、OTC 设备关联、远程扩展关联。管理员把手机关联到用户时系统自动创建 RE、SIP 设备、RE 号码、直达速拨号、识别码规则、ARS 路由列表/SIP/GSM、Tandem（p95 按模式给自动项矩阵：Mobile only/Wifi only/Dual mode 各列哪些对象自动建），管理员只需核验。OT 侧自动关联 RE 设备到用户。R2.6 变化：RE 可直接作主设备（单设备），不再需要 SEPLOS/SIP 扩展做"永不在服"的主机（p96）。
  conditions: 自动创建触发条件 = 在 Users 应用做"Associate SIP device → New → OTC Smartphone"
  tags: [structure, smartphone, auto-config, rex]

- id: f08
  title: iPhone/APNS 推送与 VoIP everywhere 架构（kamailio-wasp + wspcfg + 5265 SBC）
  type: diagram
  source_pages: p97-102
  source_chapter: OTC for iPhone / OTC iPhone+ enhancement
  source_quote: |
    "All notifications from OpenTouch server to OTC iPhone are sent through Apple Push Notification Server (APNS). APNS is an Apple Cloud service: firewall configuration is impacted" (p97)
    "Multi SIP invite required: UDP mandatory" (p99)
    "kamailio-wasp: SIP proxy between SBC and OXE; wspcfg: service to provide configuration for kamailio" (p101)
    "New SBC (used for OTC iPhone devices) • Same FQDN as OT SBC • Port 5265" (p102)
  summary: |
    iPhone 特有架构三层：①APNS 推送——OT→苹果云→终端的通知链（端口 5223/2195/2196/443），OT 随附 APNS 证书一年有效、每年发专用 hotfix 更新，Geotrust 根证书默认随装；②后台来电——应用在后台时第一个 SIP INVITE 被忽略、推送唤醒后再次 INVITE 被接受，故需多次 INVITE：本地 UDP 强制；出网经 SBC 时 TCP 强制，OT 服务器充当 SIP 代理"缓冲"INVITE；③VoIP everywhere 组件——kamailio-wasp（SBC 与 OXE 之间的 SIP 代理）+ wspcfg（给 kamailio 提供配置），并要求新建 iPhone+ 专用 SBC 声明（FQDN 与通用 SBC 相同、端口 5265，OT SBC 增加对应 SIP 接口）。
  conditions: 自 OpenTouch R2.3.1 起；Android 不走 APNS
  tags: [diagram, apns, iphone, kamailio, sbc]

- id: f09
  title: OpenTouch 远程接入拓扑——反向代理 / OTSBC / NAT/DNS 三层结构
  type: diagram
  source_pages: p104-107
  source_chapter: OpenTouch server settings for remote access (How-To) / Topology overview
  source_quote: |
    "Reverse Proxy public URL has to be declared. Declare the reverse proxy with the following URL for all services: https://ot-podx.company.com • https://ot-podx.company.com:8016 for EVS (notifications)" (p104)
    "NAT rules: 10.20.X.105<->192.168.2.105 Ports: 5261<->5261 8061<->8061 RTP/sRTP ports: 7000-7499<->7000-7499" (p105)
    "DNS entries: Pod1: ot-pod1.company.com->10.20.1.105 ... Pod6: ot-pod6.company.com->10.20.11.105" (p104)
  summary: |
    远程接入三件套：①反向代理（DMZ 192.168.2.105，公网 10.20.X.105）——数据面 https 入口，API/EVS/ACS/DMS 四个公共 URL 都声明到 OT（SystemServices/System services/Topology/Reverse proxy），EVS 通知走 8016 端口，NAT 443/8016；②OTSBC——SIP/媒体面：OTC 客户端注册用 FQDN ot-podX.company.com + 端口 5261（Eco system/IT server，Network type WAN），WebRTC 用 otsbc-podx.company.com + 8061，RTP/sRTP 端口段 7000-7499；③DNS/NAT——外部 DNS 按 POD 给 ot-podN/conf-podN → 10.20.1/3/5/7/9/11.105 的解析条目，内部 DNS 192.168.1.254。客户端配置文件使用这些 URL 做 SIP 注册与呼叫。
  conditions: 实验口径的 IP/域名模板；生产按客户 DMZ 规划替换
  tags: [diagram, remote-access, reverse-proxy, otsbc, nat]

- id: f10
  title: ACS 会议服务 FQDN 与证书生命周期（验证 → rehost → CSR → CA → 导入 → 部署）
  type: flow
  source_pages: p109-118
  source_chapter: OpenTouch server settings for remote access / ACS Service configuration
  source_quote: |
    "A specific FQDN and (virtual) IP address are assigned to OpenTouch server for conferencing service, in order to generate the link for conferences accesses into email invitation." (p109)
    "THIS SPECIFIC FQDN ASSIGNED FOR CONFERENCES INVITATION MUST BE PART (SUBJECT ALTERNATIVE NAME) OF THE REVERSE PROXY AND OPENTOUCH SERVER CERTIFICATES." (p109)
    "Launch the rehosting script thanks to the command: 'ot-config.sh --rehost'" (p111)
  summary: |
    证书流程六步：①验证——查 /var/data/bics/bics.conf 末尾 ACS 参数与 OT 证书 SAN（My Profile 页证书图标 → Details）；未配置则：②rehost——ot-config.sh --rehost，在 ACS 页录入 Hostname（conf-podx）/Domain（company.com）/IP（192.168.1.55），内部 DNS 必须有该 FQDN 条目；③CSR——System services/Security/Certificate → Generate CSR（国家/省/市/公司/部门/邮箱/SHA256）；④CA 签发——https://eco.company.com/CertSrv → advanced request → Base 64 提交 CSR → Web Server 模板 → 下载证书链；⑤导入——Change server certificate → 选 pkcs#7（pkcs#12 需 passphrase）→ Import；⑥部署与验证——Deploy（WebAdmin 会话断开属正常，重登即可），再查 SAN。会议邀请 FQDN（conf-podX）双解析：公网指反向代理 IP、内网指 ACS 虚拟 IP。
  conditions: 仅在 ACS 名称/IP 未配置或需变更时执行 rehost；DNS 条目前置
  tags: [flow, certificate, acs, san, rehost]

- id: f11
  title: UM 四种邮件后端架构与能力递减谱系
  type: diagram
  source_pages: p170-178
  source_chapter: Unified Messaging Services / Architecture & Cross compatibility
  source_quote: |
    "The OpenTouch server handles the voice messaging process and the company mail server/Gmail stores voice messages • Single point of storage • Voice messages are stored in Wav format" (p170)
    "Gmail platform can be used to store voice mails ... Limited to 500 OpenTouch users" (p176)
    "IMAP4 mail server • No plug-in: less services • No PPR • No Extensions • No MWI • No class of message" (p177)
  summary: |
    四后端架构：①Exchange（CPE 本地）——EWS + MWI + CAS，TUI/GUI/邮件客户端三通道，Exchange Web Services 与 HTTPS 流量；②Exchange 云（Office365）——Web Services 走反向代理或防火墙 URL 规则（/ExchangeNotificationService）直连 OT 通知；③Gmail——OAuth 2.0 认证（Developer Console 建 Client ID/私钥/服务账号），上限 500 OT 用户；④IMAP4——无插件故无 PPR/扩展/MWI/消息类别。兼容表（p178）：Outlook 加载项/联系人同步自 OT 2.1.1（O365 例外需 2.5 且仅桌面版 Office）；UM 自 OT 2.1.1/2.2.1/2.5 视客户端而异。语音邮件单点存储 Wav、无复制、容量只受邮件服务器限制。
  conditions: 各后端功能差异直接影响用户体验，售前需按后端选型
  tags: [diagram, um, exchange, gmail, imap]

- id: f12
  title: UDAS 同步与合并目录结构——同步库、联系人卡、照片优先级
  type: diagram
  source_pages: p220-230
  source_chapter: Directory search / UDAS & Directories synchronization & Photo homogenization
  source_quote: |
    "UDAS is a module that receives requests from client phone or software searching for contacts information stored on OpenTouch server ... Client search requests are driven to UDAS using a web service implemented in Chameleon." (p220)
    "Directories synchronization is a one way directory synchronization ... all the searches are made in the synchronized database (synchronized directories) and not directly in the declared directories storages" (p222)
    "A contact card = 4 default attributes + [1 .. 5] dynamic attributes" (p224)
    "First: Avatar ... Second: LDAP photo • Third: Local photo" (p230)
  summary: |
    数据流：OXE 电话簿（phonebookdir 表）、OT 内部目录（internaldir）、外部 LDAP（8770/AD，ldapdir 表）单向同步进 PostgreSQL 同步库（UDAS 经 RMI），所有搜索（Chameleon Web Service 接入 OTC 家族/80x8/80x8s/8082/8088 客户端）都查同步库。联系人卡 = 4 默认属性（sn/givenName/mail/telephoneNumber）+ 1..5 个动态属性（X500 预定义或自定义 Search Attribute）。Single Business Card 合并：多目录按权重（Synchronization Order）覆盖成 merged_directory 表，Merge keys（至少姓+名）识别同一人。高级搜索：多关键字（最多 5 个字符串）、% 前缀通配、- 排除。照片优先级：Avatar（internaldir，OTC 设置或 ACS WebAdmin 上传）> LDAP 照片 > 本地照片；仅在启用目录合并时有意义。
  conditions: 同步是单向快照；照片目录 /var/data/slides/d.DEFAULT/
  tags: [diagram, udas, directory, sbc-merge, postgresql]

- id: f13
  title: 会议三类型与角色权限体系（ad-hoc / scheduled / reservationless）
  type: structure
  source_pages: p266-272, p330-331
  source_chapter: Collaboration & Conference services
  source_quote: |
    "The conference access is granted through a 7 digits access code which is unique. A specific code is generated for leaders and another one for participants" (p266)
    "Types of conferences: Ad-hoc conferences (conference on the fly ... No conference identification and no access code needed) / Scheduled conferences / Reservationless conferences" (p267-269)
    "PARTICIPANTS CANNOT: Make presentations or share files • Invite other participant • Control the conference • End the conference call" (p270)
  summary: |
    三类会议：ad-hoc（通话中加人即建，无码无计划）、scheduled（日期/时长/周期/邀请/文档，可配"领导者开始才开、领导者挂断即散、静音全员、互相不可见"等选项）、reservationless（长期占用同一桥+访问码，数月/年）。角色：7 位唯一访问码分领导者码/参与者码；领导者全功能（静音他人、外呼、提升领导者、剔除参与者、邮件邀请、控制演示、控制共享），参与者受限（听演示、下载附件、静音自己、IM）；会后加入者自动为参与者；领导者可中途提权。控制双通道：应用界面 + DTMF 码。文档分 presentation（参与者不可下载）与 attachment（可下载）。音频录制仅领导者发起、只录音频、开场/结束有提示音，WAV 下载且仅发起人（认证用户）或会议创建者（访客 DTMF 录制时）可取。
  conditions: 视频 ad-hoc/点对点仅限非 Connection 用户；需 MCU（AMS）
  tags: [structure, conference, roles, dtmf]

- id: f14
  title: 视频会议架构——AMS 媒体服务器与 Dial by URI
  type: diagram
  source_pages: p273-274, p295-296
  source_chapter: Collaboration & Conference features / Dial by URI
  source_quote: |
    "ad hoc and scheduled video conferences can only be set up using a video media server, also called video Multipoint Control Unit (MCU). This video MCU can be the ALE International Media Server (AMS): an internal video media server, included in the OpenTouch server" (p273)
    "'Any SIP equipments' means any SIP device, on the LAN, supporting H.264 ... For example: English: sip:31250@opentouch.company.com" (p295)
    "SIP proxy listening on default SIP port (5060)" (p296)
  summary: |
    视频架构：多方视频必须经 MCU——OT 内置 AMS（仅支持 Active talker 切换画面，无 continuous presence；Radvision MCU 与 UVC LifeSize 外部 MCU 已不再支持）。终端：OTC PC、OTC MAC（仅 scheduled）、LAN 内任意 H.264 SIP 设备经 SIP URI 入会。Connection 用户不能做点对点视频与 ad-hoc 视频，只能参加 scheduled 视频会议。Dial by URI：ACS 的 SIP 代理监听 5060，ACS/SIP server/AMS 各用 5260 端口，会议 SIP URI 按语言随邀请邮件发出，设备可设一键入会可编程键。
  conditions: URI 拨号仅限 LAN 内设备；设备兼容性查技术文档
  tags: [diagram, video, mcu, ams, sip-uri]

- id: f15
  title: DAS 规则处理流程与法国 10 规则集
  type: flow
  source_pages: p108, p299-305, p317-318
  source_chapter: DAS rules for Conference server / DAS rules configuration
  source_quote: |
    "The call routing rules are called DAS rules. DAS rules are a set of up to 20 Unix regular expressions that are applied to the user's dialed digits. The rules are applied in order, one after the other, the output of each rule is the input to the next one." (p299)
    "First: user's dialed digits are taken into account Second: system options assign a right format to the dialed number Third: DAS rules are applied" (p301)
    "s/^\\+(\\d{3,6})$/+x\\1/ ... s/^\\+x// ... s/^\\+33/00/ ... s/^\\+/000/" (p108, p317-318 法国 Default 域 10 条)
  summary: |
    处理管线三段：用户所拨号码 → 系统选项格式化（国际前缀 00/国家码 33/国内前缀 0/分机过滤器 3-5 位：31500→+x31500、0298…→+33…、0041…→+41…、无 + 无前缀的长号报"请输入有效号码"）→ DAS 规则链（最多 20 条 Unix 正则，s/XXX/YYY/ 替换、() 捕获 \1，前一条输出作后一条输入，结果交 ACS 呼叫处理）。法国 Default 域 10 条：分机补 x、放行内呼、国际/国内格式化、放行国内、nomadic（+N/N）、移动/OTC PC/外号（+M/M）、视频（+V/V）、放行国际（+/000）。管理入口：Configuration → Advanced settings → Edit DAS rules（按 Domain 配置）；R2.0 起 nomadic 需确保规则 7/8 存在。DAS 规则按国家而定、顺序敏感、可多条同时命中。
  conditions: 规则集为国家相关；本书只给法国口径，其他国家需自行推导
  tags: [flow, das, regex, dialplan, conference]

- id: f16
  title: OTC Web 定位、能力边界与 WebRTC 架构
  type: structure
  source_pages: p323-334, p336-337
  source_chapter: OpenTouch Conversation for WEB & Web RTC appendix
  source_quote: |
    "Available for everyone: OpenTouch Conversation users • OpenTouch Connection users • And also for guests (through intranet or internet)" (p323)
    "Purpose is to access to scheduled or reservationless conferences as anonymous" (p324)
    "From outside the company: Https access through internet for data access (RP) • Audio access through PSTN OR through OTSBC (if using Web RTC)" (p332)
    "Some features are not yet available ... No white board • No poll • No recording • No video" (p334)
  summary: |
    OTC Web 是免安装浏览器端：面向 OT 用户与访客（匿名入会，凭访问码定角色，可上传头像、请求回呼、输领导者码）。能力：IM/侧栏 IM、桌面共享（发布/观看，发布端可能需插件）、文档共享+批注、上传下载、静音控制、参与者管理。架构：外部数据面走 RP（https 443/8016），音频走 PSTN 或 WebRTC 经 OTSBC（SIPS/SRTP）；内部无需网关。部署要求：HTML5 浏览器（JS+cookies 必开），WebRTC 仅 Chrome/Firefox、Windows/Mac。边界：无白板/投票/录制/视频/联系人列表/历史/排期界面（排期靠 OTC PC 或 Outlook）；WebRTC 自 OT R2.1.1 起支持免插件入会（G.711 优先）。
  conditions: 匿名访客无 OT 账号也能入会；Leader/Participant 权限矩阵见 p330-331
  tags: [structure, otc-web, webrtc, guest]

- id: f17
  title: DCS 两模式与安装形态（Basic/Advanced × 内部 KVM/外部 VM 或 PC）
  type: structure
  source_pages: p365-373
  source_chapter: Document Conversion Server
  source_quote: |
    "Natively, without any installation of additional component, only 'pdf' and 'images' documents can be shared • Pictures authorized formats: png, gif and jpeg" (p365)
    "OpenTouch has the capacity to include an INTERNAL virtual machine on top of KVM • No tools needed, only Windows OS DVD and MS Office DVD to supply" (p367)
    "An external DCS server can also be deployed in a virtual machine (on top of VMware ESXi) or on an external PC/server." (p368)
  summary: |
    矩阵：Basic 模式（ACS 内嵌，零安装）只支持 pdf + 图片（png/gif/jpeg），Office 文档只能作附件；Advanced 模式（装 DCS）支持 doc/docx/ppt/pptx/xls/xlsx 作演示，文档从用户电脑传到 DCS 服务器打开转换。安装形态：内部 DCS——OT 服务器 KVM 上自动构建 Windows 虚机（填 Windows/Office 密钥 → 插 Windows DVD → VNC 监控 → 换 Office DVD → 激活+关自动更新 → Complete；约 20 分钟 + 15-30 分钟）；外部 DCS——ESXi 虚机或物理机（Hyper-threading 必须关：Hyperthreaded Core Sharing=None；手动装或 S.O.T. 工具做 ovf 模板，3 张 DVD），在 ACS 管理台登记外部 DCS 地址与管理员账号，DCS 软件由 OT 自动推送更新。硬件与 Windows/Office 许可 ALE 均不提供。
  conditions: 兼容矩阵见 p371（内部 Win7 32bit + Office 2010/2019 US English；外部扩至 8.1/2008R2/2012R2/Win10 + Office 2013/2016）
  tags: [structure, dcs, kvm, esxi, documents]

- id: f18
  title: Calendar presence / Calendar synchro 机制与状态优先级
  type: diagram
  source_pages: p386-393
  source_chapter: Calendar presence & calendar synchro
  source_quote: |
    "Calendar information is an additional text message added next to the user presence status ... The color code is not modified by the calendar presence information" (p387)
    "Out of Office > Busy > Tentative > Working Elsewhere > Free" (p389)
    "The main purpose of the OpenTouch/Exchange calendar synchronization is to perform actions to Create/Modify and Delete Exchange Calendar Appointment on the behalf of an OpenTouch user" (p390)
    "Recurrent meetings created from OTC client are not pushed into Exchange." (p392)
  summary: |
    两个机制：①Calendar presence——从 Exchange 本地或 O365 取日历，作为在场旁注文本（如"Busy – In a meeting until 11AM"），不改颜色码；自动随日历变化更新、用户可覆盖主状态、可按用户开关（Outlook 端 Free/Busy Read 权限控制，Read=None 即关闭；默认开启）。多日程重叠按 OOO>Busy>Tentative>Working Elsewhere>Free 取优。②Calendar synchro——OT↔Exchange 双向会议同步（OT 侧 Wireal 组件经 EWS，Exchange 侧同 UM 的委托账号原理），Outlook 建会自动进 OTC、OTC 建会自动进 Outlook 并发邀请；限制：OTC 建的周期会议不推送到 Exchange，Outlook 建的周期会议可推进 OT。配置与 UM 同源（ICEaccess+Impersonation+证书），勾选 Mail Server 的 calendar presence/conference synchronization 两个开关。
  conditions: 依赖 UM 前置；本地存储邮箱场景走 TC2558
  tags: [diagram, calendar, presence, wireal, ews]

- id: f19
  title: 外部认证架构——Downstream/Upstream 双轨与插件级联
  type: diagram
  source_pages: p417-431
  source_chapter: External authentication
  source_quote: |
    "Internal authentication (by default): means that the authentication server is the Authentication provided by the OpenTouch: This server is the DTA (means 'DaTa Access'; internal authentication database)" (p417)
    "'Downstream authentication' means that the user has not been authenticated before the client sends a request to the OpenTouch server ... External downstream authentication protocols can be LDAP/LDAPS, Radius (external Radius server), or other on request" (p418)
    "'Upstream authentication' means that the OpenTouch server is not responsible for performing the authentication ... Kerberos, NTLM V2 are protocols that can be used" (p427)
    "If external authentication fails, there is an automatic cascading to DTA for Web clients (WBM for Administrator…) • No automatic cascading for thick clients (OTC PC…)" (p426)
  summary: |
    双轨架构：Downstream（OT 验证用户）——用户提交账密，OT 经 Tomcat JAAS realm → Alcatel JAAS 模块读 /opt/Alcatel-Lucent/Authentication.xml 决定插件（AlcDtaAuthenticatePlugin 本地 / AlcLdapAuthenticatePlugin / AlcRadiusAuthenticatePlugin），插件用 user.uid.attribute（AD 为 sAMAccountName）唯一 ID 与 OT 侧 External Login 字段匹配出 Alcatel User ID 存会话 cookie；多个插件可级联，文件内顺序即尝试顺序。Upstream（外部先验）——Kerberos/NTLM V2：客户端持票据访问，OT 验票识人；认证应用分 authenticationbasic（厚客户端）与 authenticationform（Web），各有 web.xml 模板（kerberos 等）重命名即启用。作用域：外认对所有应用/设备全局生效（IP Touch 应用与 TUI 除外，其按话机号码认证）；Web 客户端失败自动级联回 DTA，厚客户端不级联。
  conditions: 管理员账号必须预先填 External login 并在外部服务器建同名账密
  tags: [diagram, authentication, ldap, radius, kerberos, dta]

- id: f20
  title: Kerberos SSO 流程与四件套配置（web.xml/krb5.conf/auth.config/keytab）
  type: flow
  source_pages: p429-431, p435-436, p443-455
  source_chapter: Single Sign On via Kerberos & Kerberos How-To
  source_quote: |
    "To provide SSO, the Kerberos authentication uses the current Microsoft Windows session credentials to derive user SSO token to log into OpenTouch ... The Microsoft Windows login name must match the 'External login' data of OpenTouch users" (p429)
    "A 'web.xml' file has to be managed for thick clients ... Some « web.xml » templates are available (for Kerberos, NTLM V2). Only necessary to rename these files." (p428)
    "Creation of a user account ('ice_kerb'), dedicated for OpenTouch, is mandatory" (p436)
  summary: |
    票据流：用户 Windows 登录域 → 向 KDC（AD 域控的 AS/TGS）请求 TGT → 取 Service Ticket 给 OT → OT 用 keytab 验票识人 → 建立 DTA 用户与认证身份的关联 → 后续请求带凭据。启用四件套：①web.xml 模板重命名（thin：/opt/Alcatel-Lucent/infra_webapps/authenticationform/…/WEB-INF；thick：authenticationbasic/…；web.xml→web.xml.default，web.xml.kerberos→web.xml，反向改名即停用）；②krb5.conf（样例在 kerberos_conf 目录，拷到 /opt/Alcatel-Lucent/platform/tomcat/conf，改域名/realm/KDC）；③auth.config（拷到 /var/data/ics-group/tomcat，含 KeyTab 路径与 principal）；④ice_kerb.keytab（ktutil 工具生成：addent -password -p ice_kerb@company.com -k 0 -e rc4-hmac → wkt）。AD 侧：建 ice_kerb 专用账号（密码不可改、永不过期、与 keytab 一致）+ setspn 注册 HTTP/opentouch 与 HTTP/opentouch.company.com；重启 tomcatd。配套管理：WBM 需预建 External login 指向 AD 的管理员（Delegate authentication 选项），否则 8770 客户端无法再进 WBM。
  conditions: Kerberos 仅 Windows 上的 Web 应用 + OTC PC；不支持经反向代理；启用后必须全应用生效
  tags: [flow, kerberos, sso, keytab, spn, web-xml]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-24）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 实验 POD 搭建核对 | 有 | f02 | POD 拓扑/虚机设置表结构（菜单路径在 case.md c01） |
| task-02 | ITSP1 模拟器联调 | 有 | f03 | 模拟器拓扑与号码变换图 |
| task-03 | Nomadic 蜂窝模式 | 有 | f04, f05 | 三模式表 + Ghost Z 池定量结构 |
| task-04 | Nomadic VoIP 模式 | 有 | f04, f05 | 双模式机制 + 池关系（1 Ghost Z + 1 SIP 设备） |
| task-05 | Nomadic 资源维护 | 有 | f05 | 池机制即维护对象（命令在 case.md c04） |
| task-06 | Desksharing 配置 | 有 | f06 | DSU/DSS 机制图 |
| task-07 | Desksharing OTC PC 与维护 | 有 | f06 | UA 替代/远程释放机制 |
| task-08 | 反向代理与 OTSBC 声明 | 有 | f09 | 三层接入拓扑与端口/NAT/DNS 结构 |
| task-09 | DAS 规则与 ACS FQDN/证书 | 有 | f10, f15 | 证书生命周期流 + DAS 处理管线 |
| task-10 | OXE 通用参数 | 有 | f07 | 9 对象清单的 OXE 侧 |
| task-11 | iPhone+ SBC 与系统参数 | 有 | f08 | APNS/kamailio/5265 架构 |
| task-12 | 设备档案与用户 | 有 | f07 | 自动创建边界与关联流程 |
| task-13 | 自动对象核验与手工补充 | 有 | f07 | p95 自动项矩阵结构 |
| task-14 | Extended Mobility 部署 | 有 | （触发语法/前提在 principle p 系列） | 机制页（p150-152）并入 f04 移动性语境；QR/NFC 语法与前提归数值类 |
| task-15 | UM (Exchange) 部署 | 有 | f11 | 四后端架构 |
| task-16 | 邮箱权限/云上下文/UM 维护 | 有 | f11 | O365 通知架构与 OAuth 结构 |
| task-17 | 目录搜索部署 | 有 | f12 | UDAS 同步结构 |
| task-18 | SBC 合并与 UDAS 维护 | 有 | f12 | 合并表/merge keys/照片优先级 |
| task-19 | 会议服务器配置 | 有 | f13, f14, f15 | 会议类型/角色、视频架构、DAS 管线 |
| task-20 | 数据会议运用与协作限制 | 有 | f13, f16 | 角色权限矩阵 + OTC Web 边界 |
| task-21 | DCS 安装与声明 | 有 | f17 | 两模式安装矩阵 |
| task-22 | 日历在场/同步与排障 | 有 | f18 | 双机制与优先级 |
| task-23 | LDAP/RADIUS 认证 | 有 | f19 | Downstream 插件架构 |
| task-24 | Kerberos SSO | 有 | f19, f20 | Upstream 架构 + 四件套流程 |

补充说明：
- f01（课程主线）不对应单一 task，是 24 项任务的组织轴。
- 全部 24 项 task 均有框架类条目覆盖（task-14 的机制性内容较薄，其落地语法/前提由 principle 承接，已注明）。
- 端口/容量/语法逐值（5261/8061/5265/5223 系、Ghost Z 定量、QR 语法、DAS 10 条逐条）在 principle.md 展开；本文件只保留结构锚点与少数标志性引用。
- 生产化边界提示（来自 BOOK_OVERVIEW 批判节）：号码计划（DAS/ARS/DID）仅法国口径；容量与高可用在书外；外部文档 TC2341/TC2391/TC2258/TC2558/TC1623 是各框架条目落地生产环境的必备补充。
