# 框架/流程/结构候选 — OpenTouch Mobility & Remote Worker (OPENXTE225EN R2.6 Issue 10)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、平台/界面分区。实验环境给定值（IP/密码/账号/号码/域名）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书章节推进逻辑——讲义/How-To 成对，先边缘后客户端
  type: flow
  source_pages: p1-287
  source_chapter: 全书结构（各章 Lesson Summary 与 How-To 目录页）
  source_quote: |
    "The objective of this presentation is to describe the main components required to provide secured remote
    access to the communication services of the OpenTouch solution" (p33)
    "How to ✓ Configure general settings in OpenTouch server for remote access (remote workers)" (p62)
  summary: |
    全书 14 个知识域成对推进：①RLAB 实验环境（p1-30）；②远程接入基础设施讲义（p31-46，含参考文档族）；
    ③证书讲义（p47-61）；④OpenTouch 服务器侧远程访问设置 How-To（p62-77）；⑤OTSBC 讲义（p78-88）；
    ⑥OTSBC 部署 How-To（p89-117）；⑦反向代理讲义（p118-130）；⑧内嵌 RP 部署 How-To（p131-144）；
    ⑨客户端远程接入讲义（p145-150）；⑩OTC PC 远程工作者 How-To（p151-161）；⑪OTC 智能手机讲义
    （p162-188）；⑫OTC 智能手机 How-To（p189-217）；⑬附录三连：Nginx RP（p218-259）、OpenSSL CA
    （p260-268）、VMware 虚机（p269-277）；⑭收尾营销页（p278-287）。教学主线是"先打通服务器与边缘
    （证书→申报→SBC→反代），再配客户端（PC→手机）"，与实际交付顺序一致。
  conditions: 无版本前提；⑬附录反向支撑⑥⑧的部署动作
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: RLAB 远程实验平台——POD 池 + 三种学员接入拓扑
  type: structure
  source_pages: p4-10
  source_chapter: Remote-Lab classroom configuration / Introduction & Topology
  source_quote: |
    "Access to a pool of virtual machines (called POD) hosted in a remote data center" (p4)
    "Each platform is independant" (p8)
  summary: |
    实验平台三种接入拓扑：拓扑 1 教室机架经 RAP（Remote Access Point）接入、每 POD 至多 2 人；拓扑 2
    异地学员经 RAP 接物理话机（POE 交换机）；拓扑 3 任意 PC 经 HTTPS 直接接入（无 RAP 无话机）。每个
    POD（平台）相互独立、配置相同：含 IP Media Gateway、Client PC、RAP、Devices、VMs pool。每 POD 的
    虚机池装一台 OpenTouch 平台：Media Gateway + 虚机池（SIP 运营商模拟器、OTMS、OXE、FlexLM 服务器、
    OmniVista 8770、DCS、Eco-system、OMS、第 2 台客户端 PC——部分按场景可选）。POD 间经 VLAN X/Y/Z 与
    NAT（151.1.1.254）隔离，公共资源走 10.20.30.x 网段。
  conditions: 仅培训环境（RLAB）；拓扑按课堂形态三选一
  tags: [structure, lab, rlab, pod, topology]

- id: f03
  title: 每 POD 虚机清单、Eco-system 角色与 DNS 域（实验口径）
  type: structure
  source_pages: p11-22, p30
  source_chapter: Ressources for one POD / Login-Password
  source_quote: |
    "Eco-System server … Operating system Windows Server 2016 Roles: DNS server, Exchange server, Active
    directory, LDAP server, DHCP server (for mobiles), Certification authority" (p19)
    "DNS domain name is 'company.com'" (p21)
  summary: |
    每 POD 虚机与地址（实验口径）：公共 NFS 服务器 nas.company.com=10.20.30.40（FreeBSD，放安装 iso）；
    OTMS-V opentouch.company.com=151.1.1.50；OmniVista 8770-V nms.company.com=151.1.1.70；OXE-V 物理
    csa.company.com=151.1.1.1、主 CS csm.company.com=151.1.1.3（节点名 oxe.company.com）；FlexLM
    flex.company.com=151.1.1.80；OMS oms.company.com=151.1.1.13；SIP 运营商模拟器（基于 OXE）
    sippublic.company.com=151.1.1.105；客户端 PC2 client2.company.com=151.1.1.11；Eco-system
    eco.company.com=151.1.1.100；物理 PC client.company.com=151.1.1.10；另有 sot.company.com=151.1.1.30、
    OTMC-V otmc.company.com=151.1.1.60。Eco-system 兼任 DNS/Exchange/AD/LDAP/手机 DHCP/证书颁发机构，
    AD 用户 alban/adams/adore/barkley/backman/boop（口令 1234，实验口径）。p30 给全平台账号口令总表
    （OpenTouch SUSE root/superuser、WebAdmin otAdmin/Admin-8770、GUI 12345、TUI 54321、NMC 8770
    Adminnmc/Superuser1*、OMS letacla1 等，全部实验口径）。
  conditions: 实验口径（RLAB 专用）；NFS 为全班级共享
  tags: [structure, lab, vm-inventory, dns, credentials]

- id: f04
  title: 设备 DHCP 池、用户编号计划与 SIP 模拟器号码变换规则
  type: diagram
  source_pages: p23-29
  source_chapter: Devices IP ranges / Users and dialing plan / SIP provider simulator
  source_quote: |
    "OXE CS will be DHCP server for Alcatel-lucent desk phone devices: IP addresses range:
    151.1.1.151-151.1.1.159; Eco system will be DCHP server for smartphones: 151.1.1.160-151.1.1.165" (p23)
    "Caller dials a national number 0abcd31xxx (10 digits) … called number -> 0678931001 … Caller identity
    received and displayed: 0298131000" (p27)
  summary: |
    编号体系三层：①DHCP——OXE CS 给 ALE 话机发 151.1.1.151-159，Eco-system 给智能手机发 151.1.1.160-165
    （用 RAP+物理设备时）；②用户编号——存量 OXE 用户 Barkley 31000/Backman 31001/Boop 31002，新建用户
    Alban 31050/Adams 31051/Adore 31052；副设备号 2x31000（第一位是副设备序号），OTC 智能手机号 Dx31000；
    ③SIP 模拟器变换——国内 0abcd31xxx（10 位，例 0678931001 落到分机 31001，主叫显示 0298131000）、
    国内规范格式 33abcd31xxx（11 位，例 33123431001，主叫显示 33298131000）、国际 00ccabcd31xxx（13 位，
    例 0044123431001，主叫显示 33298131000）；末四位 31xx 即系统内分机。这是各实验拨测的"预期结果表"。
  conditions: 实验口径；模拟器行为与真实运营商存在差异
  tags: [diagram, numbering, dhcp, sip-simulator, testing]

- id: f05
  title: 远程接入需求三分类与总拓扑——DMZ 双边缘 + VPN 备选
  type: diagram
  source_pages: p33-36
  source_chapter: Infrastructure for remote users access / Introduction & Topology
  source_quote: |
    "Employees who benefit from an OTC client (PC/Mobile) must be able to connect remotely from the Internet
    to the OpenTouch system with full services" (p34)
    "* Reverse Proxy function can be delivered by OTSBC server; ** VPN access scenario that is a
    technological alternative" (p35)
  summary: |
    三类需求：①公司员工用 OTC 客户端从互联网全功能接入；②全体员工（含无 OpenTouch 账号者）可远程使用
    Web 协作；③外部伙伴/客户从互联网进会议与 Web 协作。总拓扑：公司网 ↔ DMZ（Edge Servers=反向代理+
    OTSBC）↔ 互联网；五类流量——话音 Web 服务、协作 Web 服务（桌面共享）、SIP 信令、RTP 媒体（语音/视频）、
    PSTN 话音流；员工也可走 VPN（标注为技术替代而非主路线）；反向代理功能可由 OTSBC 服务器兼任。
  conditions: RP 是第三方产品（ALE 不提供，p37）；VPN 场景不作展开
  tags: [diagram, architecture, dmz, edge-servers, vpn]

- id: f06
  title: RP 与 OTSBC 职责分工——Web 服务通道 vs SIP/媒体通道
  type: diagram
  source_pages: p37-39, p81, p121-123
  source_chapter: Components roles / Focus on servers
  source_quote: |
    "Reverse Proxy … In charge of managing the HTTPs session to access the Telephony services provided by
    the software clients … OTSBC: In charge of managing and securing the SIP session and the media streams
    (audio and video) based on RTP or SRTP (encrypted media streams)" (p37)
    "Proxy ToIP (Telephony over IP): NAT Traversal … Quality of service and CAC … Routing of emergency
    numbers" (p81)
  summary: |
    RP 特性清单：拓扑隐藏（内部地址与 FQDN）、认证（LDAP 等）、URL 改写/封禁（如禁止从互联网访问管理
    界面）、SSL 卸载；在 OT 场景管理远程客户端到话音 Web 服务的 HTTPS 会话，可接公司认证服务（LDAP/
    RADIUS），是远程客户端与 OpenTouch 服务器之间的 Web 应用网关；协作流量（桌面共享/IM/文档）也经它。
    OTSBC 特性清单：安全（DoS、拓扑隐藏、信令 TLS 加密与媒体 SRTP 加密）、QoS 与 CAC、信令转换、紧急
    号码路由、NAT 穿越场外注册；OTSBC 侧流出 RTP/SRTP，进内网到 OpenTouch/OXE。若 RP 由 OTSBC 兼任，
    认证部分要另配服务器（p37 注）。
  conditions: 反代为第三方产品；OTSBC 为 ALE OEM（AudioCodes Mediant 平台，p86 配置结构可证）
  tags: [diagram, architecture, reverse-proxy, otsbc, responsibilities]

- id: f07
  title: 客户端×边缘组件用例矩阵（含 N.U./N.A. 语义）
  type: structure
  source_pages: p40-42, p82, p122
  source_chapter: Use cases（PC/智能手机/外部用户三张矩阵）
  source_quote: |
    "OTC PC One … N.A : Not Applicable … N.U : Not Used (because no VoIP/video on this client);
    *: Audio only, no video" (p82)
  summary: |
    三张矩阵共同口径：OTC PC 需要 RP+OTSBC（全功能含 VoIP/视频/IM/桌面共享）；OTC PC One 仅需 RP（无
    VoIP，故 SBC 列为 N.U.——不是不支持，是根本没有 VoIP 可代理）；OTC Web 仅需 RP（协作）；OTC WebRTC
    需 RP+OTSBC（音视频）；OTC for iPhone/Android 需 RP+OTSBC（*仅音频无视频）。矩阵中"加密可能"标注在
    组合格上；外部用户（客户）行大量 N.A。这张矩阵是"给某类用户报边缘组件清单"的查表依据。
  conditions: N.U.=Not Used（该客户端无 VoIP/视频，SBC 无用武之地）；N.A.=Not Applicable
  tags: [structure, use-case-matrix, otc-clients, nomenclature]

- id: f08
  title: DNS 双侧解析结构与 conference FQDN 特例
  type: diagram
  source_pages: p43, p85, p124-125
  source_chapter: DNS / FQDN resolution principle
  source_quote: |
    "2 DNS requiring different configuration … Public-ot.company.com: Public-RP-IP@ … conference.company.com :
    Public-RP-IP@" (p43)
    "Internal DNS: OTSBC (for WAN access) doesn't need to be declared; Public (external) DNS: External OTSBC
    FQDN -> External OTSBC IP address" (p85)
  summary: |
    双 DNS 结构：内部 DNS——OT FQDN→OT 私网 IP、conference FQDN→会议簇私网 IP、SBC FQDN→SBC 私网 IP
    （但 OTSBC 的 WAN 接入不需要在内部 DNS 申报）；公共 DNS——OT 公共 FQDN（如 public-ot.company.com）→
    RP 公网 IP、conference FQDN→RP 公网 IP、Public-SBC FQDN→SBC 公网 IP；NAT 做公私 IP 对（实验口径：
    195.128.146.102↔11.1.1.10 等）。例：内部 opentouch.company.com→私网 IP，公共 ot-podx.al-mydemo.com
    →RP 公网 IP。理解点：同一个逻辑服务"内外两套名字+两套地址"，客户端按所在网络拿到不同解析。
  conditions: conference FQDN 必须进 RP 与 OT 证书 SAN（见 n03）；公共 DNS 记录归属在书外
  tags: [diagram, dns, fqdn, nat, split-horizon]

- id: f09
  title: 证书体系——三来源、两封装、远程访问两案例
  type: structure
  source_pages: p44-61, p84, p126-127
  source_chapter: Certificates（讲义）
  source_quote: |
    "Certificate, generated by a certification authority server … Self-signed certificate … 'Generic'
    certificate and CTL signed by a 'generic' device: Choice done during installation (security off)" (p50)
    "Case 1: Certificate with wild card … Case 2: Dedicated Certificate per server" (p58-59)
  summary: |
    三种证书来源：CA 服务器签发（安装时或事后经 WebAdmin 导入；远程访问必需、安全性最佳）、自签
    （有安全弱点）、"通用"证书+CTL（安装时选，便于部署但安全关闭）。两种封装：PKCS7（CSR 在申请方
    服务器上生成→CA 只发证书链）与 PKCS12（密钥对在 CA 生成→打包带 passphrase）。远程访问两种布局：
    案例 1 通配符证书 *.company.com 一张部署到 OpenTouch/RP/OTSBC 三处；案例 2 每服务器专用证书
    （OT 证书 SAN 含 opentouch+conference，边缘证书 SAN 含 public-ot+conference）。部署主步骤：CSR 生成
    →CA 签发→根证书导入客户端与服务器→服务器证书导入→部署生效。
  conditions: 预载"通用证书"被 p61 警告明确反对（话费欺诈/服务盗用风险）
  tags: [structure, certificates, pki, pkcs7, pkcs12, wildcard, san]

- id: f10
  title: OpenTouch 服务器侧远程访问设置三段流程
  type: flow
  source_pages: p62-77
  source_chapter: OpenTouch server settings for remote access (How-To)
  source_quote: |
    "Declare the reverse proxy with the following URL for all services: https://ot-podx.al-mydemo.com,
    https://ot-podx.al-mydemo.com:8016 for EVS (notifications)" (p63)
    "From R2.0 new rules must be added for OT Connection PC application used in nomadic mode" (p67)
  summary: |
    三段：①RP 申报——OmniVista 8770 → SystemServices/System services/Topology/Reverse proxy：Display
    name、API public URL、EVS public URL（:8016）、ACS public URL、DMS public URL（这些 URL 会写入配置
    文件供 OTC 从互联网回连）；②OTSBC 申报——Eco system/IT server → Create：FQDN（otsbc-podx…）、
    Network type WAN、Port 5261（OTC 客户端）或 8061（WebRTC），FQDN 写入客户端配置用于 SIP 注册；③
    会议访问管理——DAS 规则核对/新增（R2.0 起游牧 PC 需 4 条新规则，10 条示例按序）+ ACS 会议服务专用
    FQDN（conf-podx）与专用 IP（151.1.1.55，实验口径）：未配置则跑 rehost 脚本（ot-config.sh --rehost）
    并重签 OT 证书把会议名加进 SAN。
  conditions: DAS 规则国家相关（书中为法国口径）；rehost 仅在 ACS 名/IP 未配或需变更时执行
  tags: [flow, ot-server, reverse-proxy-declaration, otsbc-declaration, das, acs]

- id: f11
  title: OTSBC 配置结构总览（IPG/Media Realm/端口矩阵）与部署主步骤
  type: structure
  source_pages: p86-88
  source_chapter: OTSBC / OTSBC configuration summary & deployment main steps
  source_quote: |
    "IPG 1 Server: OpenTouch … IPG 2 Server: OXE … IPG 3 User: OTCv … IPG 4 User: OTC Web RTC … IPG 6
    Server: <SIP carrier> … Media Realm 3 SRTP/7000:7499" (p86)
    "Virtual machine deployment: OVF template upload, IP settings; Web interface: Wizard use, Additional
    configuration" (p87)
  summary: |
    配置总览（AudioCodes Mediant 结构，实验口径端口）：6 个 IP Profile/IP Group——OT（OpenTouch 服务器）、
    OXE、OTCv、OTC WebRTC、OTCt、SIP carrier，各配 SIP Interface 与 Message Manipulation；4 个 Media
    Realm——RTP/6000:6499、RTP/8000:8499、SRTP/7000:7499、RTP/9000:9499；WAN 侧端口——SIP TLS 5263/8061/
    5261、UDP 5361/5260、UDP+TCP 5060、SIP TLS 5161（OXE 侧）、UDP 5040；公网 RTP 段 28000:39999 与
    32000:32299。部署主步骤四件：OVF 上传→IP 设置→Web 界面（向导）→附加配置；OTSBC 申报分"IT 服务器级"
    与"设备级"两层（p88）。
  conditions: 端口与网段为实验口径；向导模板生成上述结构的绝大多数对象
  tags: [structure, otsbc, ipg, media-realm, ports, audioCodes-mediant]

- id: f12
  title: 反向代理两条部署路线——OTSBC 内嵌（7.2+）与独立 Nginx VM
  type: structure
  source_pages: p128-130, p129
  source_chapter: Reverse Proxy / OTSBC embedded Reverse Proxy & Standalone Reverse Proxy
  source_quote: |
    "RP features embedded in OT SBC can be used since OTSBC release 7.2 … Import RP configuration files
    (based on templates): template_interface_ed02.ini (optional…) template_rp_ed02.ini, template_ldap_ed02.ini:
    optional (for external LDAP authentication)" (p128)
    "Standalone Reverse Proxy … Virtual machine creation, Operating system installation (Ubuntu or other),
    Ethernet interfaces configuration, Ngnix package installation…" (p129)
  summary: |
    路线 A（内嵌）：OTSBC 7.2 起 HTTP proxy 功能——核验/更新许可（HTTP Proxy Available）→ 启用 HTTP
    proxy 并配 DNS → 证书管理（给 OTSBC 证书加 OT/会议公共名 SAN，或新建专用证书）→ 导入模板文件
    （interface 可选、rp 必须、ldap 可选）。路线 B（独立）：建 VM → 装 Ubuntu → 配网口 → 装 Nginx → 改
    Nginx properties/conf 文件 → 部署证书与私钥 → 可选外接 LDAP 认证。两条路线都要在 OT 侧申报反代
    （Public API/EVS/ACS/DMS 四个 URL 指向 RP FQDN，p130）。选型逻辑：已有 OTSBC 且许可允许→内嵌省一台
    机器；需要独立扩展或已有 Nginx 运维→独立 VM。
  conditions: 模板文件下载链接来自 TC2639（或 TC2257），必须取最新版（p220）
  tags: [structure, reverse-proxy, embedded-vs-standalone, nginx, otsbc-7.2]

- id: f13
  title: 客户端远程接入两步法——接入配置 + 路由档案
  type: flow
  source_pages: p147-150
  source_chapter: Clients in remote access / Principle
  source_quote: |
    "Step 1: configuration of remote access: Public OpenTouch URL, Login and password; Step 2: routing
    configuration: Activation of required profile (Call from PC/Route to PC, …)" (p147)
    "When a smart phone is used to dial …, it is always used to make the call whatever the 'dial from'
    specified in the active profile" (p147)
  summary: |
    两步法：第一步接入配置——公共 OpenTouch URL + 登录凭证；OTC PC 在启动时或 Settings/Preferences 里填
    反代 FQDN；智能手机在首次启动时填、后续在 Settings/Connections 改；OTC Web 用邮件收到的会议公共 URL
    直接进。第二步路由档案——激活"从哪拨/路由到哪"组合（PC/手机/家庭电话/其他号码的呼出与落地路由）。
    特例规则：用智能手机拨打时（按号、目录、历史、联系人）永远用手机本机发话，"dial from"设置不影响。
  conditions: 手机拨打特例是排障高频误解点（见 n12）
  tags: [flow, clients, otc-pc, smartphone, routing-profile]

- id: f14
  title: OTC PC 远程工作者两模式对比——multi-devices 副设备 vs Nomadic SIP 池
  type: structure
  source_pages: p151-157, p204
  source_chapter: OTC PC for remote worker (How-To) / Implementation
  source_quote: |
    "Multi-devices operation brings a second way for users to use their OTC PC application … The previous
    way is still always possible, and is, based on the Nomadic feature with Nomadic SIP. In this case, if
    the user selects computer as current device, the main set … is frozen and calls are no more routed to
    the main" (p152)
  summary: |
    模式 A（multi-devices，新法）：给用户加一个 SIP 分机（如 OTC PC，213100x）做副设备，主话机保留，管理
    方式同"OTC PC 软话机模式"；前提是 COS 开 Ring all Secondary if Main Out of Service、建 Twinset get
    call 与 No ringing 两个前缀并在用户 COS 授权。模式 B（Nomadic SIP，老法仍在）：用户把当前话机从
    Deskphone 切到 Personal Computer，主设备被冻结，SIP 软话机顶替；每连接占 1 个 SIP 设备 + 1 个 Ghost
    Z（池化资源，按并发规划）。两模式都要求 OT 侧申报 DM（设备管理服务器，OmniVista 8770）给 OTC PC 取
    SIP 文件。
  conditions: 模式 B 池资源在退出游牧时才释放；模式 A 与 B 可并存
  tags: [structure, otc-pc, multi-devices, nomadic-sip, ghost-z, comparison]

- id: f15
  title: 智能手机连接模式矩阵——WiFi/3G4G/DTMF 回落 × Android/iPhone
  type: structure
  source_pages: p166-172, p176
  source_chapter: OTC for smartphones / Use cases & Summary
  source_quote: |
    "Data connection possible: Wifi available (Inside the company / Outside)… 3G/4G data network … No data
    connection: Fallback mode using DTMF" (p166)
    "Android Smartphones can run without SIM card; Smartphone is then used as a pure VoIP softphone" (p176)
  summary: |
    场景五分：①公司内 WiFi——Web 服务+VoIP（可加密）；②场外热点 WiFi——经 RP/SBC 全功能；③3G/4G 数据
    ——Web 服务+VoIP 或话音走 PSTN（cellular 模式）；④无数据连接——回落模式，仅 DTMF 带内指令（打/挂
    电话、留言、有限路由）；⑤汇总表——Android 支持 VoIP everywhere with SBC、cellular mode only、场内
    cellular only、场内 WLAN VoIP 四种，iPhone 支持前两种。附加特性：Android 可无 SIM 卡当纯 VoIP 软话机
    （无运营商费；代价是无回落模式/私人呼叫/短信）。数据通道在时的高级服务清单：单号码、来话/通话中控制、
    统一目录/呼叫日志、呈现、可视留言、N 方会议（N>3）、IM、监督代接、经理/助理等（p173-175/177）。
  conditions: iPhone 表格中 VoIP everywhere with VPN、场内 WLAN 等格未打勾（以原表为准）
  tags: [structure, smartphone, dual-mode, fallback-dtmf, wifi-3g4g]

- id: f16
  title: 智能手机自动配置对象流——关联一次，OXE 自动建对象（按模式增减）
  type: flow
  source_pages: p178-181, p196-198, p207-211
  source_chapter: Configuration and installation main steps / Verification of automatic OXE objects
  source_quote: |
    "OXE configuration principle is complex and specially for Wifi/dual mode: up to 9 objects have to be
    managed" (p178)
    "Automatic configuration of these objects when a Smartphone is associated to a Connection user in order
    to simplify administrator tasks" (p180)
  summary: |
    流程：管理员在 OT 侧用 Users 应用一次完成"OTC Smartphone 声明+关联"→ 系统自动在 OXE 建对象并回填
    OT：远程分机（RE）、RE 手机号、Tandem（twinset，双方自动建 L1/L2 多线）、直连速拨号（自动替代用）、
    SIP 设备、判别器规则、ARS 路由表（Route 1=SIP 设备、Route 2=公网 TG 呼手机、按时间的路由表 1&2）。
    对象集随模式而异（p181 矩阵）：Mobile-only 只建 RE+Tandem；WiFi-only 建全 9 项中的 SIP 设备组但无
    ARS/GSM 侧；Dual（含 GSM 号）建全集。管理员事后按 p207-211 清单逐项核验，并补两项手工：Entity 判别
    器逻辑→物理关联、公网接入 COS 的区域授权（p212）。OT 侧还需先做 OXE CS 前缀同步与 RE DISA 公共号码
    /ARS 前缀配置（p196-198）。
  conditions: RE 目录号禁用字母前缀；ARS 路由表从 MAX ID 3999 起每手机一张（见 p25/p31 条目）
  tags: [flow, smartphone, automatic-provisioning, oxe-objects, dual-mode]

- id: f17
  title: iPhone APNS 推送来话流程与 VoIP everywhere 组件
  type: diagram
  source_pages: p183-188
  source_chapter: OTC for iPhone / OTSBC / OT iPhone+ enhancement
  source_quote: |
    "All notifications from OpenTouch server to OTC iPhone are sent through Apple Push Notification Server
    (APNS); APNS is an Apple Cloud service: firewall configuration is impacted" (p183)
    "Several SIP invites may be required … UDP is mandatory to allow the several SIP Invites during incoming
    calls … Behind the SBC, over Internet, TCP is mandatory: OpenTouch server will act as a SIP proxy
    'buffering' the SIP invite message over TCP" (p186)
    "kamailio-wasp: SIP proxy between SBC and OXE; wspcfg: service to provide configuration for kamailio" (p187)
  summary: |
    机制链：来话到达 → OT 经 APNS 推送（https push）→ iPhone 弹通知唤醒 OTC → 应用前台后才接受 SIP
    invite（后台时首个 invite 被忽略）→ 因此需要多次 SIP invite；UDP 才支持多次 invite（TCP 不行）。分
    场景：场内（仅 UDP 拓扑）无影响；场外经 SBC 走互联网强制 TCP → 由 OpenTouch 侧 kamailio-wasp（SBC
    与 OXE 间的 SIP 代理）+ wspcfg（给 kamailio 提供配置）做 invite 缓冲。配套动作：为 iPhone 新建 SBC
    声明（同 FQDN、端口 5265，实验/部署口径）；OT SBC 增加端口 5265 的 SIP 接口；防火墙放行 TCP 5223/
    2195/2196/443；APNS 证书随 OT 出厂、一年有效、每年专门 hotfix 更新。
  conditions: R2.3.1 起 iPhone 推送全走 APNS；iPhone+ 专属配置不在向导范围（见 n06）
  tags: [diagram, iphone, apns, kamailio-wasp, wspcfg, push-notification]

- id: f18
  title: Nginx RP 文件/组件结构——三份 conf + snippets + LDAP 认证模块
  type: structure
  source_pages: p251-259
  source_chapter: Nginx reverse proxy deployment (How-To) / Nginx configuration file & External authentication
  source_quote: |
    "The NGINX configuration has changed since release 2.2. As the OTES server is no more part of the
    solution, the reverse proxy must be configured to support application sharing during data conferences…
    two configuration files to modify: remoteworker.conf, conference.conf" (p253)
    "The LDAP authentication module is based on a python script: nginx-ldap-auth-daemon.py. An LDAP-auth
    daemon is running on the NGINX server and listening on the port 8888" (p257)
  summary: |
    组件布局：/etc/nginx/conf.d/ 下 global.conf（resolver 指内网 DNS）、remoteworker.conf（server_name 改
    OT 公共 FQDN，行 17 与 177）、conference.conf（server_name 改会议公共 FQDN，行 13 与 33）；
    /etc/nginx/conf.d/snippets/ 下 opentouch_fqdn.conf（OT 公共名/域、内部名/FQDN/IP、8770 管理名、ACS
    簇名/FQDN/域共 11 个变量）+ conference_ssl.conf / remoteworker_ssl.conf（证书路径 rp.crt/rp.key，
    V1.5；含 8016 通知端口重定向）+ ldap.conf（LDAP URL/BaseDN/BindDN/口令）。认证模块：Python 2 的
    nginx-ldap-auth-daemon.py（仅支持 Python 2）+ init 脚本，daemon 监听 8888；不开认证时注释掉
    remoteworker.conf 的 AUTH LDAP 段。校验链：nginx -t → /etc/init.d/nginx start/restart。
  conditions: OT 2.2 起必须同时改 remoteworker.conf 与 conference.conf（OTES 退场、会议应用共享经反代）
  tags: [structure, nginx, reverse-proxy, configuration-files, ldap-auth]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-14）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 认知 RLAB 实验环境 | 有 | f02, f03, f04 | POD 结构、虚机清单与账号、DHCP/编号/模拟器规则 |
| task-02 | 规划远程接入拓扑 | 有 | f05, f06, f07, f08 | 三类需求与总拓扑、组件分工、用例矩阵、DNS 双侧 |
| task-03 | 证书策略与签发 | 有 | f09 | 三来源/两封装/两案例结构（签发操作序列在 case 类） |
| task-04 | 服务器侧远程访问设置 | 有 | f10 | RP 申报→OTSBC 申报→会议管理三段流程 |
| task-05 | 部署 OTSBC | 有 | f11 | 配置结构总览与部署主步骤（分步操作在 case 类） |
| task-06 | 内嵌 RP 部署 | 有 | f12 | 路线 A 的对象清单（操作序列在 case 类） |
| task-07 | Nginx RP 部署 | 有 | f12, f18 | 路线 B + 文件/组件结构 |
| task-08 | VMware 虚机部署 | 无独立框架条目 | — | 纯操作序列（web client/vSphere 两路），无结构性内容，收在 case 类 c10 |
| task-09 | 客户端远程接入 | 有 | f13 | 两步法流程 |
| task-10 | OTC PC multi-devices | 有 | f14 | 两模式对比结构（操作序列在 case 类） |
| task-11 | OTC PC Nomadic SIP | 有 | f14 | 池化机制结构（操作序列在 case 类） |
| task-12 | 智能手机 Connection 用户 | 有 | f16 | 自动配置对象流与模式矩阵（操作序列在 case 类） |
| task-13 | iPhone+ APNS 专项 | 有 | f17 | 推送来话机制链与组件 |
| task-14 | 拨测验证 | 有 | f04 | 模拟器号码变换规则即"预期结果表" |

补充说明：
- f01（全书推进逻辑）为 BOOK_OVERVIEW 骨架的组织轴，不对应单一 task。
- 14 项任务中 13 项有框架类覆盖；task-08 为纯操作序列、无结构性内容，原因已注明。
- 容量/QoS 数值（CAC 阈值等）原书未给，框架层不做编造（见 BOOK_OVERVIEW 批判节）。
