# 框架/流程/结构候选 — Rainbow OmniPCX Enterprise (RAINXTE003EN Ed12)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、平台/界面分区。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——RLAB 地基 → 云侧体系 → OXE 接入 RCC/路由 → 网关解锁 VoIP → 话务台/维护/Teams
  type: flow
  source_pages: p3-314（章节推进）
  source_chapter: 全书目录结构（Remote Labs → SIP Simulator → Rainbow Overview → Companies → How-To×14）
  source_quote: |
    "RAINBOW - R101.1 N4 MD4/SP161 / OMNIPCX ENTERPRISE - EDITION 12 / PARTICIPANT'S GUIDE" (p1)
    "The OXE must be connected to the Rainbow infrastructure in order to associate directory numbers with
    company members and use PBX resources." (p67)
  summary: |
    课程按九段推进：①实验环境（RLAB 平台 + SIP 运营商模拟器）；②Rainbow 平台概览与网络前提；③云侧体系（公司/管理员/订阅）；④OXE 侧准备与接入（Pod 配置、DNS/代理、Rainbow Agent）；⑤成员与设备关联（RCC → REX/tandem 路由）；⑥WebRTC 网关三连实验（部署、升级、OXE 配置九件套）+ 池化/容量讲义；⑦话务台域（4059EE 与 Rainbow Attendant Console 两条线）；⑧维护与支持；⑨Microsoft Teams 集成。与 OXO 版教材（RAINXTE001）相比，OXE 版把 REX/Ghost Z/tandem 作为独立基础章，网关不走"自动配置"而走完整手工配置（SIP/ARS/判别器/回调），并新增 4059EE 传统话务台线——教学主线是"先云后端、先路由后音频、OXE 侧全程手工可审计"。
  conditions: RCC 为无网关阶段中间站；OXE 侧网关配置要求系统版 12.1 MD4/12.2+（p135）
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: RLAB 远程实验平台结构——POD 池 + 公共资源区 + 每Pod 6 台虚机
  type: structure
  source_pages: p5-11
  source_chapter: OVERVIEW / Remote Labs Platform & POD configuration
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data
    center. … Pods are independent of each other … have the same configuration … have access to common
    resources" (p5)
    "ENTP_OXE_RAINBOW csa (physique) / csm (principal) 192.168.1.1 / 192.168.1.3 … ENTP_WEBRTC webrtc
    192.168.1.15 … rainbow Rainbow123" (p9)
  summary: |
    实验平台两层：POD 1..n 相互独立、配置相同；公共资源区（Subnet 0，10.20.30.x）放 NAS（软件/许可）、SIP 模拟器（12.0.0.2）与外部 DNS（10.20.30.250）。每 POD 含 6 台实例（实验口径 IP）：OXE（csa 物理 192.168.1.1 / csm 主 192.168.1.3，mtcl/swinst/root，Superuser2580*）、OMS（192.168.1.13，root/Superuser2580*）、FlexLM 服务器（192.168.1.80，root/letacla1）、WebRTC 网关（192.168.1.15，rainbow/Rainbow123）、PC Client 10（192.168.1.10，administrator/superuser，装 IPDSP 31000）、PC Client 11（192.168.1.11，装 IPDSP 31001）。Pod 内网关 192.168.1.254，内部 DNS 192.168.1.250。每台 PC 另有 MicroSIP 软话机模拟公号，软件经 RAIN 网络盘从 NAS 下载。
  conditions: 仅培训环境（RLAB），所有 IP/密码为实验口径；POD 间互不可见，NAS 与 SIP 模拟器为全班共享
  tags: [structure, lab, rlab, topology]

- id: f03
  title: ITSP1 SIP 运营商模拟器拓扑、号码变换规则与 DDI 表
  type: diagram
  source_pages: p14-17
  source_chapter: SIP CARRIER SIMULATOR
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 … ITSP1 Public gateway public.itsp1.com 10.20.30.50
    … SIP domain: sip.itsp1.fr / itsp1.fr" (p14)
    "PBX installation nb 3321PN … DDI table - First external nb 41000 … First internal nb 31000 … Range size 500" (p17)
  summary: |
    模拟器在 RLAB 公共区扮演出局运营商：两条腿——SIP 网关 gateway1.itsp1.com（PBX 注册账号 pbxP/alcatel，SIP 域 sip.itsp1.fr）与公网网关 public.itsp1.com（两个 MicroSIP 模拟 Public/Urgence 用户，账号 publicP@itsp1.fr / urgenceP@itsp1.fr，密码 public）。号码规则（PN=两位 POD 号）：国内 3311PN12345…3351PN12345、移动 3361PN12345/3371PN12345、国际 4421PN12345、紧急 112/15/17/18；Public 主号 3321PN12345。呼出变换示例（POD 3）：拨 0110312345 → PBX 送 +33110312345 给 public3@itsp1.fr。呼入本 PBX：安装号 3321PN41000，DDI 表首外部号 41000 ↔ 首内部号 31000、范围 500（分机 31001 的外部号即 3321PN41001）。
  conditions: 实验口径（RLAB 专用基础设施）；账号/号码/IP 均为教学约定值，不可套用到生产
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f04
  title: Rainbow 平台双定位全景——UCaaS + CPaaS + Connected Platforms 一张图
  type: diagram
  source_pages: p20-23
  source_chapter: Rainbow / What is Rainbow, Global view, Architecture UCaaS
  source_quote: |
    "Rainbow is a Cloud-based collaboration application (UCaaS) … It is also a CPaaS open communication
    platform with a set of APIs that allows Rainbow collaboration tools to be integrated into existing
    applications and business processes." (p20)
    "PBX connected to Rainbow with WebRTC gateway … Communications • Manage and establish calls between
    Rainbow clients and any phone number or extension • Manage your routing profile according to your needs" (p23)
  summary: |
    全景图分三块：①Rainbow Platform 居中，向上供唯一用户体验（联系人/富在场/通知/告警监控/分析/控制管理）；②UCaaS（Rainbow Workplace）——云话音/会议/多媒体 + PBX 话音/呼叫控制/联邦，经 AGENT 分别对接 OXE、OXO Connect、第三方 PBX 与机器（Machines/AGENT）；③CPaaS——开放 API/SDK 供业务应用与客服关系集成（developers.openrainbow.com）。UCaaS 架构三要素（p23）：客户端（PC App/Web/Mobile）、通信层（客户端间与对任意号码/分机的呼叫 + 个人路由档案）、客户侧 PBX 经 WebRTC 网关接入。呼叫控制始终在 PBX，Rainbow 管协作与路由意图——这是后续 RCC/REX/网关各章的架构底座。
  conditions: 无版本前提；CPaaS 细节超出本教材范围
  tags: [diagram, architecture, ucaas, cpaas, platform]

- id: f05
  title: 8 种订阅计划体系与"电话服务必须付费订阅"的分层
  type: structure
  source_pages: p24
  source_chapter: Rainbow / Subscription plans
  source_quote: |
    "Rainbow Essential This free option is available to anyone who wants to try Rainbow for an unlimited
    period (no SLA). … Rainbow Enterprise Conference … is pre-paid yearly in advance (twelve months)." (p24)
  summary: |
    订阅八种：Essential（免费无 SLA，可与付费混用）、Business（按用户日常通信）、Enterprise（Business 全量+多方视频会议+扩展存储+O365/G Suite 集成）、Attendant（话务台：等待呼叫列表+监督控制台）、Enterprise Conference（Enterprise+无限电话会议分钟，年付预付 12 个月）、Conference（按分钟/连接 pay-as-you-go，组织者可为免费用户）、Connect（CRM 连接器集成）、Room（按会议室订阅需额外硬件）。关键分层（p56）：电话服务必须 Business/Enterprise/Attendant。本书（OXE 线）新增要点：WebRTC 网关使用要求 Business 或 Enterprise（p133/p129），Attendant 订阅专供 Rainbow 内嵌话务台、与 4059EE 无关（p200）。
  conditions: 详情以 help.openrainbow.com 的 Features List 为准（书中给出链接）
  tags: [structure, subscription, licensing]

- id: f06
  title: Rainbow 网络要求文档体系——支持页 + 两份 PDF 的结构
  type: structure
  source_pages: p26-31
  source_chapter: NETWORK REQUIREMENTS
  source_quote: |
    "This page contains: A note on the process for updating the infrastructure … A summary of port/protocol
    requirements for: Rainbow collaboration, Rainbow hybrid telephony, Rainbow Hub • 2 PDF files" (p27)
    "This document details: … Rainbow domains and associated IP addresses • Bandwidth requirements •
    Configuration of corporate network elements DNS, Proxy, Firewall..." (p31)
  summary: |
    网络前提的获取结构：支持页（help.openrainbow.com 的 Check Rainbow Network Requirements 文章）给出基础设施更新流程说明、上版以来的变更说明（如新增公网 IP 与服务器）、协作/混合话音/Hub 三类端口协议摘要，并挂两份 PDF——《Rainbow network requirements》与《Rainbow network requirements - Health data hosting》。PDF 正文结构：端口与协议、运行原理与流量、域名及关联 IP 清单、带宽要求、企业网络设备（DNS/代理/防火墙）配置。做生产交付时以这份 PDF 为准，本教材只给指针。
  conditions: 文档按 Edition 迭代，实施前必须取最新版
  tags: [structure, network-requirements, ports, bandwidth]

- id: f07
  title: Rainbow Pilot 连通性与承载容量评估流程
  type: flow
  source_pages: p32-36
  source_chapter: RAINBOW PILOT
  source_quote: |
    "RAINBOW PILOT allows you to assess your Rainbow connectivity from your location, and the capacity of a
    given location to handle a population of Rainbow users characterized by a flexible mix of usages between
    Collaboration, Conferencing, Hybrid or Hub telephony." (p33)
  summary: |
    Pilot 是官方在线评估工具（https://pilot.openrainbow.com/home），两个用途：①从客户现场位置测 Rainbow 连通性；②按"协作/会议/混合话音/Hub 话音"的用法配比评估站点能承载的 Rainbow 用户规模。页面分多个测试区块（p34 截图标注两处 To come），有若干菜单入口。用法：售前勘测先跑连通性测试，再按客户用户画像设定用法配比得出容量结论，与网络要求 PDF 配合形成"网络就绪"证据。
  conditions: 售前/勘测工具，不能替代防火墙放行清单；生产端口要求以 Network Requirements PDF 为准
  tags: [flow, pilot, connectivity, capacity, presales]

- id: f08
  title: Company 概念体系——两类公司、经销角色链、可见性与公司要素
  type: structure
  source_pages: p37-46
  source_chapter: INTRODUCING THE COMPANIES
  source_quote: |
    "However, the following actions can only be performed by the BP: • Declaration & PBX • Opening of paid
    subscriptions … To be managed by a BP, an 'EC' company must be attached to the company of this BP (one
    and only one attachment)." (p39)
    "Get into the habit of systematically setting the 'closed' mode as soon as you create a Rainbow company." (p43)
  summary: |
    Company 是 Rainbow 的组织单元：主功能仅对公司成员开放，成员=邮箱身份，一人只能属一家公司；建司前先搜索查重。两类公司：Reseller/BP 公司与 End-customer（EC）公司；经销链 ALE—VAD/DR/IR—EC，EC 必须挂到且只能挂到一个 BP 名下。可见性四级 PUBLIC/PRIVATE/CLOSED/ISOLATED 在 company settings 可改，建议默认 CLOSED，ISOLATED 不推荐（用户无法被外部 bubble 邀请）。认证：SSO（Azure AD SAML/OIDC、ADFS SAML，管理员需 Enterprise 级）或 Rainbow 原生（12 位复杂密码 / TOTP）。公司关键要素四组：成员/电话/订阅/权限/标签；企业目录/分析/历史/告警；设置（可见性/认证）/支持/信息/地址/Logo/时区；Telephony 子块（订阅/PBX/PBX 链接/WebRTC/监督）。建司六步（p41）：建司 → 订订阅 → 建 PBX 并连接 → 建 WebRTC 网关 → 建成员（登录+号码+订阅）→ 补充管理（监督组/话务台等）。
  conditions: 创建 EC 公司与开订阅是 BP 权限；客户管理员通常无 PBX 创建权
  tags: [structure, company, bp, ec, reseller, visibility]

- id: f09
  title: 管理员角色分工与企业目录/信息频道两个管理面
  type: structure
  source_pages: p47-53
  source_chapter: ADMINISTRATORS ROLES
  source_quote: |
    "RESPELLER/BP ADMINISTRATORS: Has a view on the customers companies … Create PBXs & activate WebRTC
    gateways … END-CUSTOMER ADMINISTRATORS: Manages its own company … Associate users phones with their
    Rainbow accounts" (p48-49)
    "Only users with an 'Enterprise' service level can create Information Channels." (p52)
  summary: |
    两类管理员：BP 管理员（看所有客户公司、管自家公司、管 EC 公司、给 EC 分订阅、建 PBX 并激活 WebRTC 网关）；EC 管理员（管自家用户/公司信息/订阅分配/查关联 PBX/把用户话机关联 Rainbow 账户/看 dashboard）。具体权限矩阵见 Features List/Administration 页签。"Roles"页签给 EC 公司指派管理权，可多管理员并存。两个管理面：①企业目录（Business Directory）——外部联系人+号码，改善来话识别，可手工建或 CSV 批量导入（含样本文件与导入报告），管理权默认客户管理员、可委托给非管理员用户；②信息频道（Information Channels）——新闻推送，创建者需 Enterprise 级，可对选中成员或全员强制订阅且成员不可退订。
  conditions: Azure AD 之上才有"企业目录"概念；频道强制订阅不可逆（成员端）
  tags: [structure, administrator, directory, channel]

- id: f10
  title: 订阅开通与分配两段式流程（BP 开通 → 管理员分配）
  type: flow
  source_pages: p54-59
  source_chapter: SUBSCRIPTIONS
  source_quote: |
    "The BP administrator takes out subscriptions for his own company or those of his customers. … The price
    is per user and different subscription plans are possible: Monthly • Prepaid 1, 3 or 5 years" (p55)
    "During LAB Use ONLY Voice MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID!!!" (p57)
  summary: |
    两段式：①BP 管理员为客户公司订阅（选 Rainbow Hybrid 订阅类型 → 选月付或预付 → 定许可数 → Subscribe，可定义订阅期间）；②订阅先落到客户公司，再由 BP 或本地管理员分配到成员（建成员时或改成员时）。硬约束：每个成员要有 Business/Enterprise/Attendant 之一才能用电话服务；培训环境禁预付（只许 Voice MONTHLY）。
  conditions: 需 BP 账号执行开通；LAB 环境只许 Monthly（实验口径）
  tags: [flow, subscription, licensing]

- id: f11
  title: 集成 Rainbow Agent 接入架构与五条链路
  type: diagram
  source_pages: p67-68, p87
  source_chapter: CONNECTING THE OXE TO RAINBOW / INTEGRATED RAINBOW AGENT / Maintenance incvisu
  source_quote: |
    "The information available in the Rainbow administration interface and must be reported in the OXE.
    Allows connection of the OXE to Rainbow via • A PBX ID • An Activation Code" (p68)
    "000008M|=5:4503=rainbowagent: WebSocket (rainbowagent<->Rainbow) in service … 4505=XMPP link …
    4509=CSTA link (CSTA server<->Rainbow) … 4507=Config link (PBX config<->Rainbow) … 4511=API_MGT link" (p87)
  summary: |
    OXE 内置 Rainbow Agent：Rainbow 管理端生成 PBXID 与激活码，录入 OXE 的 Rainbow 菜单（webadmin/mgr）启用即完成接入；前置条件是网络参数（DNS/代理，netadmin 配置）就绪。incvisu 输出揭示 agent 与云间五条链路：WebSocket（rainbowagent↔Rainbow）、XMPP link、CSTA link（CSTA server↔Rainbow）、Config link（PBX config↔Rainbow）、API_MGT link——排障时五条应全部 in service。接入是"经销商或客户管理员"都可做的动作，但 PBX 必须先由经销商在 Rainbow 侧创建。
  conditions: 网络前提必须先完成（p84 Warning）；激活码用于首次连接
  tags: [diagram, architecture, rainbow-agent, csta, connection]

- id: f12
  title: OXE 用户使用 Rainbow 的形态矩阵——RCC / REX 路由 / 纯 REX / DECT 特例
  type: structure
  source_pages: p106-118
  source_chapter: OVERVIEW - OXE USERS WITH RAINBOW
  source_quote: |
    "Rainbow Essential license • Allows only to control your physical device via the Rainbow application
    (RCC mode) • Call routing is not possible … Rainbow Business/Enterprise licenses • The physical device
    is set in tandem with a Remote Extension (REX) • Call Routing is not a Forwarding" (p109)
    "The DECT device cannot be set up in tandem with a REX (OXE management limitation)" (p139)
  summary: |
    四种形态：①无 REX（Essential 或未配路由）——只有 RCC，音频在话机，可用 OXE 公网资源；②话机+REX（Business/Enterprise）——tandem 结构，可改路由到工作手机/家庭/个人手机/其他外部号（经 OXE 公网资源），Rainbow agent 按路由选择自动改写 REX 内容；路由四案例：无手机号→REX 空、只话机响；配专业手机→REX=专业手机、话机+手机同响；配个人手机→REX=个人手机；两个都配→取专业手机；③纯 REX 用户（无物理话机）——Rainbow 当软电话，WebRTC 网关必须；④仅 DECT 话机——DECT 不能与 REX 直接 tandem（OXE 管理限制），需建 Virtual UA 设备与 DECT+REX 做 multi-devices，Virtual UA 成主设备（通常要重建 DECT），且 Virtual UA 不能被 RCC 控制。
  conditions: 路由 ≠ 呼叫转发；REX 指向外部号码时走 OXE 公网 trunk 而非网关
  tags: [structure, rcc, rex, routing, dect]

- id: f13
  title: REX/Ghost Z/Tandem 机制图——Rainbow agent 自动改写路由载体
  type: diagram
  source_pages: p111-113, p122-125
  source_chapter: REMOTE EXTENSION (REX) & Rainbow user with OXE phone and REX
  source_quote: |
    "A Remote Extension (REX) is a special type of device that allows OXE to reroute calls to an external
    resource … To work, each REX needs an internal technical equipment called Ghost Z … The Ghost Z devices
    pool is the maximum number of concurrent calls being made" (p111)
    "Remote extension will be configured automatically by Rainbow agent according to users' routing" (p113)
  summary: |
    机制链：REX 是 OXE 终端类型，被叫时 OXE 把呼叫转往 REX 中定义的外部号码；呼叫建立期间 OXE 从专用池占用一个 Ghost Z 技术资源（通话结束释放），Ghost Z 池大小=REX 并发呼叫上限。Rainbow 侧：tandem 主站=Deskphone、副站=REX（配置只做在主站、自动同步副站）；用户在 Rainbow 客户端选路由时，Rainbow agent 自动改写 REX 内容——mobile/home/other 路由写外部号码（走公共 trunk），computer 路由写 BBB 前缀的 17 位 Rainbow number（走 WebRTC 网关）。OXE 侧配置顺序：Ghost Z（Analog/255/255/255，Ghost Z 勾选+Feature=Remote extension）→ REX 声明（编号 21<主号 QMCDU>）→ 两端 multi-line（≥2 线）→ tandem 声明。
  conditions: 参考 TC2462；tandem 两端必须 multi-line；每路 REX 并发呼叫需一个 Ghost Z
  tags: [diagram, rex, ghost, tandem, routing]

- id: f14
  title: WebRTC 网关角色、部署形态与配置三块全景
  type: diagram
  source_pages: p131-136
  source_chapter: OMNIPCX ENTERPRISE - WEBRTC GATEWAY OVERVIEW
  source_quote: |
    "A software component located in a customer's premises that runs on a virtual machine. Use of the
    WebRTC Gateway requires a BUSINESS or ENTERPRISE subscription for a member" (p133)
    "Require OXE release 12.1 MD4, 12.2 or later … The virtual machine (OVF) is delivered by ALE • The
    Operating System is based on a Debian" (p135)
  summary: |
    角色：打通 Rainbow 客户端 ↔ OXE 分机/资源（trunk group、话务、留言、公号）的内部与外部通信，提供 one-number 多终端体验；媒体流：Rainbow 客户端 —WebRTC SIP/RTP→ 网关 —SIP/RTP→ OXE 话机；Rainbow↔网关间加密媒体。收益清单：客户端间呼叫、RCC、客户端↔话机、用 OXE 公网资源、REX tandem one-number、终端任选（deskphone/任意外部号/VoIP 加密媒体）。部署：客户 premises 的 VMware VM（独立 ESXi 或与 OXE 同服务器，OXE 一 VM+网关一 VM），OVF 由 ALE 交付、OS 为 Debian；前提 PBX 先连 Rainbow、OXE ≥12.1 MD4/12.2。配置三块（p136）：①网关侧（WebRTC Gateway use 参数、成员/订阅）；②OXE 侧——SIP to RGW（SIP trunk group、SIP 外部网关、判别器、ARS、编号命令表、回调翻译器）+ Remote extensions（Ghost Z、每用户 REX）+ 网络配置/OXE 申报/域名（IP 或 FQDN）/PBXID；③Rainbow 侧（OXE 设置、网关使用参数、成员 Enterprise 订阅）。
  conditions: Business/Enterprise 订阅硬门槛；G711-only 的 SIP 网关取值为实验口径（p181）
  tags: [diagram, webrtc-gateway, deployment, architecture]

- id: f15
  title: 共享可扩展 WebRTC 网关池——三种配置对比与 406 溢出机制
  type: diagram
  source_pages: p146-150
  source_chapter: SHARED AND SCALABLE WEBRTC GATEWAY
  source_quote: |
    "If the traffic limit is reached, the gateway responds to a new request with a SIP message '406 - Not
    Acceptable'. As a result, the OXE will overflow onto the next ARS route (WebRTC gateway). • If this
    parameter is empty, the SIP trunk limit will determine the overflow." (p149)
    "Note: This type of sharing, depending on the number of nodes, can make ARS management more complex.
    It is recommended to proceed by OXE cluster." (p148)
  summary: |
    三种配置：①每 OXE 网关复制（WebRTC duplication）——抗故障+增并发，但基础设施成本高，流量大时（如每 OXE ≥5000 用户）仍合理；②共享 WebRTC 池（推荐）——多 OXE 共享网关池，抗故障+增并发+省成本，按 OXE 集群推进以控制 ARS 复杂度，要求每 OXE 节点对每网关一条 SIP trunk/外部 SIP 网关；③OXE 网络（ABC/FABC/F 节点）——为多个高低流量节点池化网关组。溢出机制：基于 OXE ARS，各节点需相似 ARS 管理；每网关最大流量在 Rainbow 界面（Rainbow/Communications/Equipments/编辑该 PBX）设定=网关支持的并发流数；满载时网关回 SIP 406 Not Acceptable，OXE 溢出到 ARS 表中下一条路由（声明顺序即溢出顺序 1st/2nd/3rd）；该参数为空则由 SIP trunk 限制决定溢出。示例图值 400（实验口径示例）。
  conditions: 两种配置都基于 ARS overflow 机制（Load Sharing via OXE）；详细配置在 TC2462
  tags: [diagram, webrtc-gateway, pool, ars, overflow, ha]

- id: f16
  title: 网关容量估算流程（TBE067 sizing 工具 + 400 并发上限 + 压缩器推算）
  type: flow
  source_pages: p151
  source_chapter: SHARED AND SCALABLE WEBRTC GATEWAY / SIZING
  source_quote: |
    "An Excel tool is available in which key values must be entered • Total number of OXE users • The
    number of OXE users with a Rainbow client • The percentage of Rainbow client usage • The percentage of
    direct calls from a Rainbow client to a Rainbow client." (p151)
    "Available from OXE 101.0 MD3 and WebRTC 3.x • A WebRTC gateway supports up to 400 simultaneous streams." (p151)
  summary: |
    sizing 四步：①取 TBE067_Rainbow - WebRTC Gateway Pres&Sizing - ed06l.zip（Excel 工具）；②输入四个关键值——OXE 用户总数、持 Rainbow 客户端用户数、Rainbow 客户端使用率、客户端间直呼占比（流量模型假设可调）；③得出所需并发通道数；④由通道数推算 OXE 压缩器数量。硬上限：单网关 400 并发流；工具适用 OXE 101.0 MD3 / WebRTC 3.x 起。注意与 OXO 版教材的容量口径不同（OXO 是 20/50 通话的查表），OXE 版是工具化估算。
  conditions: 工具本体在书外（MyPortal/ALE 内部链接）；话务建模假设可按站点调整
  tags: [flow, sizing, capacity, tool]

- id: f17
  title: 4059EE 话务台 + Rainbow 集成结构（话务组/话务台/CDT/BLF）
  type: structure
  source_pages: p198-205, p208-215
  source_chapter: RAINBOW INTEGRATION ON 4059 EE / Call distribution and attendants
  source_quote: |
    "Rainbow integration allows real-time monitoring of Rainbow members, contact search, and optionally
    provides calendar information. Tag search is also available. … Warning - Rainbow and phone status are
    two distinct things and can be different" (p199, p204)
    "WARNING: This extension must not be multi-line, as it will be associated to the 4059 IP attendant" (p209)
  summary: |
    结构四层：①Attendant group（如 GROP1，物理号 A0000，Max calls before overflow=排队溢出门限，依 Day/Night/Mode1/Mode2 状态溢出；建组即自动生成 Call Distribution Table）；②4059 EE attendant（如 OP1，物理号 B0000，Set Type=4059 IP，必须关联一部非 multi-line 的话机或 IPDSP——4059EE 只管话务不管话音）；③呼叫分配（实体 CDT 日间路由指向话务组；Attendant Call 前缀法国码默认 9/美国码 0；个人话务呼叫前缀如 31401 建电话簿条目以显示话务员名）；④Rainbow 集成——为 4059EE 配专用 Rainbow 账户（取在场信息+联系成员），被监督成员须在该账户联系人列表；Enable Busy Lamp Field 后可实时在场/搜索/IM/BLF。关键提醒：Rainbow 在场与电话在场是两个独立信息，可不同。
  conditions: Attendant 订阅仅用于 Rainbow 内嵌话务台、与 4059EE 无关（p200）；4059 应用与 abcacom.exe 需放行防火墙（培训语境可关防火墙）
  tags: [structure, attendant, 4059ee, blf, call-distribution]

- id: f18
  title: Rainbow Attendant Console 界面结构与监督组/互助组体系
  type: structure
  source_pages: p225-237
  source_chapter: RAINBOW ATTENDANT CONSOLE & MUTUAL AID SUPERVISION GROUPS - OVERVIEW
  source_quote: |
    "Call queue management - Manage up to 10 calls for OXE - And up to 8 calls for OXO Connect … An
    Attendant subscription is required for each member using this feature • Available on the Rainbow Web
    and Desktop applications • Attendant console not available on mobile." (p227)
    "Maximum number of supervision groups for a supervisor / Maximum number of users in a group
    (supervisors + supervised): 5 / 30" (p230)
  summary: |
    界面五区：监督组页签（每页签一组，不可见组的来话显示红点，可开音频提示，另有收藏页签）、BLF 监督区、呼叫队列（OXE 10 路/OXO 8 路）、当前通话呼叫控制、三种显示格式（Normal/Small/Condensed）。可做动作：拦截被监督用户的来话、强制/取消其呼转（如转留言信箱）。监督组：监督员（需 Attendant 订阅）+被监督成员同组；监督员上限 5 组、每组上限 30 人；挂起呼叫数取决于话务员软电话线的 multi-line 资源（OXE REX 最多 10、OXO Anydevice 最低 R6 最多 8）；所有电话呼叫由 PBX 处理；拦截仅限同一 PBX 且仅限电话呼叫。互助监督组：永久归属组之外可一键加入/退出，监督员可临时纳入/排除被监督用户，同时最多监督 4 路，代接仅对 PBX 电话呼叫有效（Rainbow 软终端呼叫不可），可锁定最后一名成员；建法与普通组相同仅 Type 不同，创建时定义双方 In/Out 权限。
  conditions: 监督组是 Rainbow 侧概念，与 OXE attendant group 完全两回事；详见 TC2462（OXE）/TC2479（OXO）
  tags: [structure, attendant-console, supervision-group, mutual-aid]

- id: f19
  title: 维护与支持体系五入口（日志/上报/状态/告警/SR）
  type: structure
  source_pages: p245-257
  source_chapter: MAINTENANCE
  source_quote: |
    "You can view all the incidents of all your users in the section … The integrator partner has the same
    reports as the customer, so he can help with end user support." (p248)
    "The ESR will only be created if the partner is certified on Rainbow" (p254)
  summary: |
    五个入口：①Help Desk Guide（帮助台指南：排障指南/找日志/定位网络或应用问题/报障流程）；②用户日志与问题上报——用户在 Rainbow 界面 "Help and Support / Report a problem"（日期时间、问题描述、截图附件、同意支持用日志；Web 模式不要日期因浏览器日志短期），管理员端可看全部用户事件并取事件日志，集成商与客户同视角；③云服务可用性——status.openrainbow.com 状态页（Get updates 订阅告警，按主题/地域过滤，法国勾 WW/EMEA/DE）+管理门户的计划维护通知（按地域与架构 Hybrid/Hub 过滤、色标关键度、多在晚间周末）；④告警——可设阈值通知音频质量劣化与无音频；⑤操作历史——全部管理操作留档，多管理员场景查"谁在何时做了什么"，按类别/类型/日期过滤。SR 流程：入口 support@openrainbow.com、Emily BOT、Global Welcome Center、电话；ESR 仅为 Rainbow 认证伙伴创建；MyPortal 建 SR 字段清单（category Rainbow/type product support/severity/subject/公司名/版本/子类/SIP trunk/how found/客户参考号）。
  conditions: SR 需 Rainbow 认证伙伴资质；OXE 侧维护命令族另见 c04/c09
  tags: [structure, maintenance, support, sr, status]

- id: f20
  title: Microsoft Teams 集成架构与三步部署（工作站级）
  type: diagram
  source_pages: p258-273, p280-284
  source_chapter: INTEGRATION WITH MICROSOFT TEAMS
  source_quote: |
    "The integration is done at the workstation level" (p259)
    "Subscription assignment - User must have one of these subscriptions: Business • Enterprise.
    Permissions … to limit Rainbow collaboration features as collaboration services will be provided
    natively by Teams itself" (p271)
  summary: |
    双件套：Rainbow App in Teams（Telephony Power App：电话设置/呼叫历史/留言与通知/拨号盘/呼转控制/当前话机选择）+ Rainbow Desktop（任意桌面应用热键点击外呼如 F6、单呼叫管理：拨打/接听/挂断/取消）。四条呼叫流：①Teams 拨分机 → MakeCall API → CSTA → PBX 话机响；②Teams 拨外部号 → MakeCall API → 计算机VoIP → WebRTC 网关 → 公网；③外部来话 → 话机响 + Desktop 通知（接听/转留言）；④外部来话 → WebRTC 经网关 → 计算机接听。部署三步：①Teams 管理（应用商店可用/管理员上传 zip + 权限同意）；②Rainbow 管理（订阅 Business/Enterprise + 权限收敛为 Telephony）；③最终用户（装 App + Rainbow Desktop 必须安装并运行）。p274-284 与 p259-269 内容重复（架构/体验各讲两遍，讲解义与复习用）。
  conditions: 工作站级集成，非租户级；配置细则在 Rainbow help center 文章
  tags: [diagram, architecture, teams, deployment]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 19 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 网络前提与 Pilot | 有 → f06（文档体系）、f07（Pilot 流程） |
| task-02 公司体系 | 有 → f08（两类公司/角色链/可见性/六步） |
| task-03 管理员权责/目录/频道 | 有 → f09 |
| task-04 订阅开通与分配 | 有 → f05（体系）、f10（两段式流程） |
| task-05 RLAB/OXE 实验环境 | 有 → f02（平台结构）、f03（SIP 模拟器与号码规则） |
| task-06 DNS/代理配置 | 无独立框架条。属操作序列（见 case c03），f11 仅涉及其作为前提 |
| task-07 OXE 接入 | 有 → f11（Agent 架构与五链路） |
| task-08 成员管理 | 无框架条。操作序列见 case c01；规则类见 principle p07/p08 |
| task-09 分机关联与 RCC | 部分覆盖 → f12（形态矩阵的 RCC 行）；操作见 case c05 |
| task-10 用户形态决策 | 有 → f12（四形态矩阵） |
| task-11 远程延伸配置 | 有 → f13（REX/Ghost Z/Tandem 机制图） |
| task-12 网关部署 | 有 → f14（角色/部署/配置三块） |
| task-13 网关升级 | 无框架条。操作序列见 case c08 |
| task-14 OXE 网关配置 | 有 → f14 的配置三块清单；逐字段操作见 case c09 |
| task-15 共享池与容量 | 有 → f15（池化与 406）、f16（sizing 流程） |
| task-16 4059EE 话务台 | 有 → f17 |
| task-17 Attendant/互助组 | 有 → f18 |
| task-18 维护体系 | 有 → f19 |
| task-19 Teams 集成 | 有 → f20 |

**统计**：20 条（flow 5 / structure 10 / diagram 5）；19 项任务中 16 项有框架类条目覆盖，task-06/08/13 属纯操作序列（case 覆盖）。
