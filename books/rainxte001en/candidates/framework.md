# 框架/流程/结构候选 — Rainbow OXO Connect (RAINXTE001EN Ed13)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、平台/界面分区。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——云侧开户 → PBX 接入 RCC → 网关解锁音频 → 增值域
  type: flow
  source_pages: p4-7
  source_chapter: COURSE STEP BY STEP（Agenda 部分）
  source_quote: |
    "At this step, Rainbow users can only supervise their extension: RCC mode (Remote Call Control)
    • Supervision of DeskPhones by the Rainbow application (Pick up, hang up, transfer)
    • Audio is exclusively managed by the deskphone" (p6)
    "Configure automatically the OCE internal WebRTC Gateway" (p7)
  summary: |
    课程按七段推进：①Rainbow 概览（应用、管理界面、订阅、支持入口）；②网络前提与公司概念；③实验环境（远程实验室 + SIP 运营商模拟器）；④OXO 侧准备（装 OMC、改密码、改 IP）；⑤PBX 用 PBXID+激活码接入 Rainbow，建用户账号，分机关联后进入 RCC 模式（只有监督能力，音频在话机）；⑥WebRTC 网关概览 + OCE 内部网关自动配置 + 管理存量用户并建 Anydevice 用户（解锁完整路由）；⑦话务台与监督组、维护概览收尾。这是整本书的"先云后端、先 RCC 后音频"教学主线，也是实际交付项目的推荐顺序。
  conditions: 无特殊版本前提；RCC 为无网关阶段的中间态，属于课程设计的 deliberate 中间站
  tags: [flow, course-structure, rcc, delivery-order]

- id: f02
  title: RLAB 远程实验平台结构——POD 池 + 公共资源区
  type: structure
  source_pages: p11-16
  source_chapter: TRAINING LAB ENVIRONMENT / Introduction & Training Platform
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data center." (p11)
    "The POD contains a virtual machine • Windows 11 PC for completing the labs" (p15)
  summary: |
    实验平台分两层：POD 1..n 相互独立、配置相同，每个 POD 含一台 Windows 11 客户端虚机（OXOC_PC_CLIENT，IP 192.168.1.10/24，实验口径）和一台 OXO Connect Evolution（IP 192.168.1.246，实验口径）；公共资源区（Subnet 0，10.20.30.x，实验口径）放 NAS（软件、许可）和 SIP 模拟器（12.0.0.2）及外部 DNS（10.20.30.250）。学员通过 Rlab 门户对虚机执行远程桌面/重启/停止/启动/控制台操作。客户端虚机预装 4 个 MicroSIP（分机 100-103）+ 2 个模拟公号的 MicroSIP，另需自装 IPDSP（用分机 104）。
  conditions: 仅培训环境（RLAB），所有 IP 为实验口径；POD 间互不可见，NAS 与 SIP 模拟器为全班级共享
  tags: [structure, lab, rlab, topology]

- id: f03
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则
  type: diagram
  source_pages: p22-26
  source_chapter: SIP CARRIER SIMULATOR / Overview & Public numbers & SIP OXO CONFIG
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... ITSP1 Public gateway public.itsp1.com 10.20.30.50" (p22)
    "SIP account (P= POD number 1 to 6) • Login: pbxP • Password: alcatel ... 210P41000 Installation number • 41100 to 41199 base 100 DDI subscribers • 41000 base 9 DDI Operator group" (p26)
  summary: |
    模拟器在 RLAB 公共区扮演出局运营商：两条腿——SIP 网关 gateway1.itsp1.com（PBX 注册账号 pbxP/alcatel，SIP 域 sip.itsp1.fr）与公网网关 public.itsp1.com（两个 MicroSIP 模拟 Public/Urgence 两个 SIP 用户）。号码规则：PN 为两位 POD 号；国内 33{1-5}1PN12345、移动 3361PN12345/3371PN12345、国际 4421PN12345、紧急 112/15/17/18；呼出时 PBX 把 0110312345 变换为 +33110312345 送出。呼入本 PBX：安装号 3321PN41000，DDI 段 41100-41199（分机 100 即 3321PN41100），操作员组基 9 的 41000。OXO 侧 SIP 网关名 ITSP1G1，Outbound Proxy 指向 gateway1.itsp1.com，DNS A 记录 192.168.1.250。
  conditions: 实验口径（RLAB 专用基础设施）；所有账号/号码/IP 均为教学约定值，不可套用到生产
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f04
  title: Rainbow 平台双定位全景——UCaaS + CPaaS 一张图
  type: diagram
  source_pages: p29-31
  source_chapter: Rainbow / Overview (What is Rainbow, Global view)
  source_quote: |
    "Rainbow is a Cloud-based collaboration application (UCaaS) offering chat services, audio / video calls, screen and file sharing, contact management, phone presence…etc. ... It is also a CPaaS open communication platform with a set of APIs" (p29)
  summary: |
    全景图分三块：①Rainbow Platform 居中，向上供唯一用户体验（联系人、富在场、通知、告警监控、分析、控制管理）；②左下 UCaaS（Rainbow Workplace）——云话音/会议/多媒体流量（Cloud telephony）+ PBX 话音/呼叫控制/联邦（PBX Telephony），经 AGENT 分别对接 OXE、OXO Connect、第三方 PBX 与机器（Machines）；③右下 CPaaS——开放 API/SDK 供业务应用集成、客服关系集成，开发者入口 developers.openrainbow.com。理解点：PBX 保留呼叫控制，Rainbow 提供协作与云服务，两者经 Agent 桥接。
  conditions: 无版本前提；CPaaS 细节超出本教材范围
  tags: [diagram, architecture, ucaas, cpaas, platform]

- id: f05
  title: UCaaS 混合云架构三要素——客户端/通信/PBX+WebRTC 网关
  type: diagram
  source_pages: p32
  source_chapter: Rainbow / Architecture - UCaaS
  source_quote: |
    "Clients • PC Rainbow App • Web • Mobile ... PBX connected to Rainbow with WebRTC gateway ... Communications • Manage and establish calls between Rainbow clients and any phone number or extension • Manage your routing profile according to your needs" (p32)
  summary: |
    混合云架构三要素：客户端三种形态（PC 应用、Web、移动）；通信层负责 Rainbow 客户端之间、客户端与任意号码/分机之间的呼叫建立及个人路由档案；客户侧 PBX 经 WebRTC 网关接入 Rainbow。呼叫控制始终在 PBX，Rainbow 侧只管协作与路由意图——这是后续 RCC 与网关两章的架构底座。
  conditions: PBX 必须带 WebRTC 网关才有完整音频；无网关时即 RCC 模式
  tags: [diagram, architecture, hybrid, webrtc-gateway]

- id: f06
  title: 8 种订阅计划体系与"电话服务必须付费订阅"的分层
  type: structure
  source_pages: p33
  source_chapter: Rainbow / Subscription plans
  source_quote: |
    "Rainbow Essential This free option is available to anyone who wants to try Rainbow for an unlimited period (no SLA). The Essential subscription can also be blended with any premium subscription" (p33)
    "Rainbow Attendant for Hybrid users requires a new specific subscription offer identified as 'Attendant'." (p33)
  summary: |
    订阅八种：Essential（免费无 SLA，可与付费混用）、Business（个人/团队日常通信）、Enterprise（Business 全量 + 多方视频会议 + 扩展存储 + O365/G Suite 集成）、Attendant（话务台：等待队列 + 监督控制台）、Enterprise Conference（Enterprise + 无限电话会议分钟，年付预付）、Conference（按分钟/连接计费的 PSTN 会议可选包，组织者可以是免费用户）、Connect（CRM 连接器集成）、Room（会议室按房间订阅，需额外硬件）。关键分层：电话服务（话音/话务台）必须 Business/Enterprise/Attendant，Essential 不可用。
  conditions: 详情以 help.openrainbow.com 的 Features List 为准（书中给出链接）
  tags: [structure, subscription, licensing]

- id: f07
  title: Rainbow 网络要求文档体系——支持页 + 两份 PDF 的结构
  type: structure
  source_pages: p36-40
  source_chapter: NETWORK REQUIREMENTS
  source_quote: |
    "This page contains: A note on the process for updating the infrastructure ... A summary of port/protocol requirements for: Rainbow collaboration, Rainbow hybrid telephony, Rainbow Hub • 2 PDF files" (p36)
    "This document details: ... Rainbow domains and associated IP addresses • Bandwidth requirements • Configuration of corporate network elements • DNS, Proxy, Firewall..." (p40)
  summary: |
    网络前提的获取结构：支持页（help.openrainbow.com 的 Check Rainbow Network Requirements 文章）给出基础设施更新流程说明、上版以来的变更说明、协作/混合话音/Hub 三类端口协议摘要，并挂两份 PDF——《Rainbow network requirements》与《Rainbow network requirements - Health data hosting》。PDF 正文结构：端口与协议、运行原理与流量、域名及关联 IP 清单、带宽要求、企业网络设备（DNS/代理/防火墙）配置。做生产交付时以这份 PDF 为准，本教材只给指针。
  conditions: 文档按 Edition 迭代（Edxx），实施前必须取最新版
  tags: [structure, network-requirements, ports, bandwidth]

- id: f08
  title: Rainbow Pilot 连通性与承载容量评估流程
  type: flow
  source_pages: p41-44
  source_chapter: NETWORK REQUIREMENTS / Rainbow Pilot
  source_quote: |
    "RAINBOW PILOT allows you to assess your Rainbow connectivity from your location, and the capacity of a given location to handle a population of Rainbow users characterized by a flexible mix of usages between Collaboration, Conferencing, Hybrid or Hub telephony." (p42)
  summary: |
    Pilot 是官方在线评估工具（https://pilot.openrainbow.com/home），两个用途：①从客户现场位置测 Rainbow 连通性；②按"协作/会议/混合话音/Hub 话音"的用法配比评估站点能承载的 Rainbow 用户规模。页面分多个测试区块（部分标注 To come），有若干菜单入口。用法：售前勘测时先跑连通性测试，再按客户用户画像设定用法配比得出容量结论，与网络要求 PDF 配合形成"网络就绪"证据。
  conditions: 售前/勘测工具，不能替代防火墙放行清单；生产端口要求仍以 Network Requirements PDF 为准
  tags: [flow, pilot, connectivity, capacity, presales]

- id: f09
  title: Company 概念体系——两类公司、经销角色链与公司关键要素
  type: structure
  source_pages: p47-49
  source_chapter: INTRODUCING THE COMPANIES
  source_quote: |
    "A user cannot be part of 2 different companies" (p47)
    "However, the following actions can only be performed by the BP: • Declaration & PBX • Opening of paid subscriptions ... To be managed by a BP, an 'EC' company must be attached to the company of this BP (one and only one attachment)." (p48)
  summary: |
    Company 是 Rainbow 的组织单元：主功能仅对公司成员开放，成员=邮箱身份，一人只能属于一家公司；建司前先搜索防止重名。两类公司：Reseller/BP 公司与 End-customer（EC）公司；经销链为 ALE—VAD/DR/IR—EC，EC 必须挂到且只能挂到一个 BP 名下（名称显示在 My company/Dashboard）。BP 专属动作只有两个：申报与创建 PBX、开通付费订阅；其余管理动作 BP 与客户管理员都可行。公司关键要素（p49）分四组：成员/电话/订阅/权限/标签；企业目录/分析/历史/告警；设置（可见性、认证）/支持/信息/地址/Logo/时区；Telephony 子块含订阅、PBX、PBX 链接、WebRTC、监督。
  conditions: 创建 EC 公司是 BP 权限；客户管理员通常无 PBX 创建权
  tags: [structure, company, bp, ec, reseller]

- id: f10
  title: 公司搭建六步主流程（Company Setup）
  type: flow
  source_pages: p50
  source_chapter: INTRODUCING THE COMPANIES / Main steps in company setup
  source_quote: |
    "MAIN STEPS IN COMPANY SETUP: Creation of the company 1 ... Assigning Subscriptions 2 ... Creation of the PBX and connection 3 ... Setting up the WebRTC gateway 4 ... Creation of company members 5 (Assign • A login • A phone number • A subscription) ... Complementary management 6 (Supervision groups, Attendant console etc)" (p50)
  summary: |
    端到端六步：①创建公司；②开订阅（按用户数订阅 Business/Enterprise/Attendant）；③创建 PBX 并连接（PBXID+激活码接入）；④搭建 WebRTC 网关；⑤创建公司成员并同时分配登录名、电话号码、订阅；⑥补充管理（监督组、话务台等）。这条主线即整本书的骨架：步骤 1-2 在 f09/f16，步骤 3 在 f19，步骤 4 在 f25-f33，步骤 5 在 f20-f23，步骤 6 在 f34-f38。
  conditions: 步骤 2 的付费订阅开通、步骤 3 的 PBX 创建为 BP 专属
  tags: [flow, company-setup, master-flow, six-steps]

- id: f11
  title: 公司可见性四级结构（PUBLIC/PRIVATE/CLOSED/ISOLATED）与选型建议
  type: structure
  source_pages: p52
  source_chapter: INTRODUCING THE COMPANIES / Privacy & Visibility
  source_quote: |
    "CLOSED: a user from another company cannot see the members of your company, but he can invite them via their email address. Your users can't see users outside their company, but they can invite them via their email address."
    "Get into the habit of systematically setting the 'closed' mode as soon as you create a Rainbow company. This is ideal for the vast majority of customers."
  summary: |
    可见性四级控制公司成员与外部 Rainbow 世界的互见互邀能力：PUBLIC（外部可见可邀，己方可见可邀外部）、PRIVATE（外部不可见但可经邮箱邀请；己方可见可邀外部）、CLOSED（外部不可见但可经邮箱邀请；己方不可见外部但可经邮箱邀请）、ISOLATED（双向都不可见不可邀）。教材的明确建议：没有特殊理由一律建司即设 CLOSED；ISOLATED 代价大——用户将无法被外部组织邀请进会议（bubble），启用前必须核查影响。可见性后续可在 company settings 里改。
  conditions: 修改入口在 company settings；ISOLATED 影响外部 bubble 邀请
  tags: [structure, visibility, privacy, company]

- id: f12
  title: 认证方式体系——SSO 三协议 + 本地双模式，可按用户混配
  type: structure
  source_pages: p53
  source_chapter: INTRODUCING THE COMPANIES / SSO & Authentication Method
  source_quote: |
    "Azure AD - SAML / Azure AD - OIDC / ADFS - SAML ... You can set up several authentication methods within your company, and decide which users need to use which method."
    "The administrator must have an 'Enterprise' service level"
  summary: |
    认证两条路线：①SSO——Azure AD 走 SAML 或 OIDC、企业 AD（ADFS）走 SAML（其他标准协议方案如 Shibboleth/RSA/OKTA 需 ALE 确认）；②Rainbow 原生——复杂密码（≥12 位）或 TOTP 动态口令（需 Google/Microsoft Authenticator、Authy 等第三方应用，特别推荐给管理员）。同一家公司可并存多种认证方式并按用户指定谁用哪种；配置 SSO 的管理员本人必须有 Enterprise 服务等级；TOTP 配置以支持站点 MFA 文章为准。
  conditions: SSO 依赖客户已有 Azure AD/ADFS 基础设施；管理员账号需 Enterprise 级
  tags: [structure, sso, totp, authentication]

- id: f13
  title: 创建客户公司的界面入口路径
  type: menu-path
  source_pages: p54
  source_chapter: INTRODUCING THE COMPANIES / Company creation
  source_quote: |
    "Reseller Company / End customer companies / List of End customer companies / Global information related to all companies / Create a client company" (p54)
  summary: |
    管理界面左侧导航结构：Reseller Company（本公司）、End customer companies（客户公司列表）、全局信息区；在客户公司列表页点"Create a client company"进入创建表单（必填：名称、国家、时区、邮政地址、邮箱、网站、可见性、公司联系人等，可自定义 Logo 与横幅）。这是 BP 管理员开户新建 EC 公司的固定入口。
  conditions: 仅 BP/经销商账号可见此入口
  tags: [menu-path, company, creation]

- id: f14
  title: 管理员权责分工——BP 管理员 vs 客户管理员 vs 角色页
  type: structure
  source_pages: p57-59
  source_chapter: ADMINISTRATORS PROFILES
  source_quote: |
    "Create PBXs & activate WebRTC gateways ... Assign subscriptions to end-customer companies" (p57, Reseller/BP administrator)
    "Associate users phones with their Rainbow accounts" (p58, End-customer administrator)
    "The 'Roles' tab is used to assign administrative rights to the client company. It is possible to have several administrators to manage the company." (p59)
  summary: |
    两级权责：BP 管理员——查看客户公司、管理自家与客户公司、给客户公司分配订阅、创建 PBX 并激活 WebRTC 网关、管管理员与用户账号、把 PBX 分机分给 Rainbow 账号、管用户档案、看板监督活动；客户管理员——管理自家公司、用户账号、公司信息、给用户分订阅、查看关联 PBX、把用户话机关联 Rainbow 账号、管用户档案、看板监督。管理权经"Roles"页签授予，支持多管理员并存；完整角色矩阵查 help.openrainbow.com 的 Features List/Administration 页签。
  conditions: PBX 创建与付费订阅开通仅 BP（与 f09 互相印证）
  tags: [structure, admin, roles, bp, responsibilities]

- id: f15
  title: 企业目录与信息频道两步配置路径
  type: menu-path
  source_pages: p60-61
  source_chapter: ADMINISTRATORS PROFILES / Business Directory & Information Channels
  source_quote: |
    "1 Enable right  2 Manual creation or by bulk import via a CSV file (Sample file available). A report is generated after import." (p60)
    "1 Give rights to members – Roles tab  2 Create the channels ... Only users with an 'Enterprise' service level can create Information Channels." (p61)
  summary: |
    企业目录（Business Directory）：步骤①开权限（默认客户管理员可管，也可委托给非管理员用户）；步骤②手工创建或 CSV 批量导入（提供样例文件，导入后生成报告），存放外部联系人及号码，提升来电弹屏识别率。信息频道（Information Channels）：步骤①在 Roles 页签给成员授权；步骤②创建频道，仅 Enterprise 服务等级可创建；可选"公司全员自动订阅"或"指定成员自动订阅"，被订阅者无法退订。
  conditions: 目录管理可委托非管理员；频道创建者须 Enterprise 等级
  tags: [menu-path, directory, channels, csv]

- id: f16
  title: 订阅两层流转——先到公司、再分成员（含开通表单要素）
  type: flow
  source_pages: p64-67
  source_chapter: SUBSCRIPTIONS
  source_quote: |
    "Subscriptions are first assigned to the client company. Then, these subscriptions are assigned to company members by the BP administrator or local administrator. Each member must have a subscription to use telephony services • Business • Enterprise • Attendant" (p65)
    "During LAB Use ONLY Voice MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID!!!" (p66)
  summary: |
    订阅流转两层：第一层 BP 管理员给客户公司开订阅（选混合订阅类型 → 选月付或预付 → 定许可数量 → Subscribe，可定订阅期；计费为按用户，月付或预付 1/3/5 年）；第二层管理员把订阅分给成员（创建成员时或修改既有成员时分配）。电话服务必须 Business/Enterprise/Attendant。实验口径：培训中只用 Voice MONTHLY，禁止年付预付。
  conditions: 第一层为 BP 专属；实验环境禁止预付（实验口径）
  tags: [flow, subscription, allocation, monthly]

- id: f17
  title: OMC 安装与首次连接四步——安装/连接+证书/改密/客户信息
  type: flow
  source_pages: p69-78
  source_chapter: OMC Installation (How-To)
  source_quote: |
    "Make a connection to the system with OMC in Expert mode with server authentication ... Enter the default IP address 192.168.92.246 ... Enter the default installer password pbxk1064 only used for the first connection" (p74)
    "In order to avoid displaying the security alert at each connection, you must install the certificate the 1st time." (p75)
  summary: |
    四步闭环：①装 OMC——在管理 PC 解压后以管理员身份运行 setup.exe，依次选语言、目标目录、国家/发行渠道、目标产品、界面语言，Install→Finish（实验口径：软件在 SOFTS OXO CONNECT 目录）。②首连——Expert 菜单 → LAN/WAN 连接 → 默认 IP 192.168.92.246 → 勾选 Server authentication → 首次安装口令 pbxk1064（实验口径）；安全告警点 View certificate → Install certificate → 存入 Trusted Root Certification Authorities，避免每次弹告警。③改密——为各账户输入培训师给定的新密码（每客户必须不同），后续可在 OMC/Security 菜单改。④录客户信息——带 * 为必填，可另录安装技师（供应商）信息；右下角图标显示已连接 OXO，即可开始正式配置。
  conditions: 实验口径：默认 IP 192.168.92.246、首登密码 pbxk1064；生产中必须首连即改密
  tags: [flow, omc, installation, certificate, first-connection]

- id: f18
  title: OXO 与客户端 IP 规划修改路径（OMC/Lan/IP configuration）
  type: menu-path
  source_pages: p79-82
  source_chapter: OXO Connect IP settings modification (How-To)
  source_quote: |
    "OMC/ Hardware and limits/ Lan/IP configuration ... Choose the Boards tab, and enter a value for the Main CPU: 192.168.1.246 ... In the DHCP tab, define the IP addresses range for deskphones: Start: 192.168.1.30 End: 192.168.1.39 ... Click OK & Re-start the OXO Connect" (p80-81)
  summary: |
    路径：OMC → Hardware and limits → Lan/IP configuration，四个页签依次改——Boards 页签填 Main CPU 地址 192.168.1.246；LAN Configuration 页签填默认网关 192.168.1.254、掩码 255.255.255.0；DNS 页签填 DNS1 192.168.1.250、DNS2 10.20.30.250；DHCP 页签定话机地址段 192.168.1.30-39；点 OK 并重启 OXO 生效。随后改客户端 PC（OXO_PC_CLIENT）静态地址 192.168.1.10/24、网关 192.168.1.254、DNS 同上，改完即可用远程桌面连接。
  conditions: 所有地址为实验口径；改完必须重启 OXO Connect
  tags: [menu-path, omc, ip-planning, dhcp, dns]

- id: f19
  title: OXO 接入 Rainbow 三段流程——找凭证 → OMC 填入启用 → Webdiag 验证
  type: flow
  source_pages: p83-89
  source_chapter: Connect an OXO to Rainbow (How-To)
  source_quote: |
    "Click on the company management icon then My company • Select the Communication menu • Click on the OXO in the list — You will find here: • PBXID • Activation code" (p85)
    "OMC/Cloud/Rainbow ... Enter the Rainbow PABX-ID ... Enter the Activation code ... Click on Rainbow enabled ... Apply ... Domain name Leave the default value: openrainbow.com" (p86)
    "OMC /Tools /Webdiag /Services /Rainbow Status — Control the connection status: 'connected with final password'" (p88)
  summary: |
    三段流程：①取凭证——找经销商要，或用客户管理员账号登录 web.openrainbow.com（实验口径：cCpP.admin@ale-training.com / Superuser-P*）→ 公司管理图标 → My company → Communication → 选中 OXO → 复制 PBXID 与 Activation code；②接入——OMC → Cloud → Rainbow 菜单：填 PBX-ID、激活码、勾 Rainbow enabled → Apply，域名保持默认 openrainbow.com；③验证/维护——OMC/Tools/Webdiag（installer + 安装口令，实验口径）/Services/Rainbow Status 看到即成；系统日志走 Webdiag 的 System tab/System Files/Log files，Rainbow 代理日志名为 ccrbagent.log；用户侧日志在 Rainbow 界面 User Settings → About Rainbow → Open logs。
  conditions: 域名保持默认 openrainbow.com；Webdiag/日志登录用 installer 账号（实验口径）；前提是云侧已由 BP 建好公司与 PBX
  tags: [flow, pbxid, activation-code, webdiag, ccrbagent, menu-path]

- id: f20
  title: 成员创建三法——手工逐个/邮件邀请/批量导入（CSV 与 Azure AD）
  type: structure
  source_pages: p92-95
  source_chapter: MEMBERS OF A RAINBOW COMPANY / Members creation
  source_quote: |
    "Members can be created: Manually • Creation one by one • By invitation • Via email address ... By bulk import • From .CSV file(UTF-8) • Microsoft Azure Active Directory ... Import via Azure Active Directory is reserved for administrators with 'Voice Enterprise' service level" (p92)
  summary: |
    三条建户路径：①手工逐个——管理员直接建号并当场定全字段，适合少量用户；②邮件邀请——发 noreply@openrainbow 邀请邮件，用户自行点链接完成建号（密码须≥12 位含大写/数字/特殊字符），建完后管理员回补电话号码、可见性、标签、权限、认证方式等（适合分批自助入驻；报错时先查邮箱是否属于 10 天内删除的账号）；③批量导入——CSV（UTF-8，下载样例模板，导入出同步报告；可建/改/删用户、按 MAC 绑设备、设全局参数；走 SSO 时密码列留空）或 Azure AD 同步（需先把 AAD 关联到公司：My Company/Settings，且仅 Voice Enterprise 管理员可用，还提供通讯录搜索）。
  conditions: AAD 导入限 Voice Enterprise 管理员；密码策略≥12 位含 1 大写/1 数字/1 特殊字符
  tags: [structure, members, csv, azure-ad, invitation]

- id: f21
  title: 成员设置分区——信息/权限/电话/可编程键/服务/角色/安全 七大块 + 标签与限制档案
  type: structure
  source_pages: p96-98
  source_chapter: MEMBERS OF A RAINBOW COMPANY / Member settings
  source_quote: |
    "Information •Identifier, last name, first name, language, country •Timezone: voicemail timestamp •Visibility ... Permissions •To grant the right to Rainbow features ... Telephony •Equipment: PBX of the company •Extension number and public number ... Services (subscription) ... Roles ... Security •Modify password, identifier & authentication method" (p96)
  summary: |
    成员编辑页分区（页面列出 7 块）：Information（标识/姓名/语言/国家/时区——影响留言时间戳/可见性/标签）；Permissions（授予 Rainbow 功能权）；Telephony（设备=公司 PBX、分机号与公号码、关联物理话机可选、电话功能与权利）；Programmable keys（应用侧与话机侧可编程键，可建键组批量关联）；Services（订阅 Business/Enterprise/Attendant）；Roles（是否管理员、企业目录、频道）；Security（改密码/标识/认证方式）。p98 补充两项横向管理：Tags（手工或批量打标，优化目录搜索）与限制性 Profiles（公司级定义、可按用户定制，用于收敛功能）。总览口径称"八块"，即这 7 分区加 Tags/Profiles 横向项。
  conditions: 无；各块的具体取值受公司订阅与权限体系约束
  tags: [structure, member-settings, telephony, permissions]

- id: f22
  title: 成员删除 10 天宽限流程与安全操作（改密/改登录/改认证）
  type: flow
  source_pages: p99-100
  source_chapter: MEMBERS OF A RAINBOW COMPANY / Members deletion & Security
  source_quote: |
    "When you delete a user, his or her status becomes 'Suspended' for a period of 10 days (called the 'grace period') ... If you restore it, it will default to 'Essential' (free) mode, so you'll need to reallocate the appropriate license ... It will also be necessary to reassign the user's telephone line." (p99)
  summary: |
    删除流程：删用户 → 状态变 Suspended 进入 10 天宽限 → 期间可"恢复"（误删救回）或"彻底删除"；不动作 10 天后自动彻底删。恢复的代价：订阅已随删除移除，恢复后落回免费 Essential，需重新分配许可并重新关联电话线。安全操作（Security 页签）：强制改密（改密瞬间会把在线用户踢下线——怀疑账号被冒用时很有用）、改登录邮箱（保留账号历史）、改认证方式；密码策略≥12 位含大写/数字/特殊字符。
  conditions: 恢复用户必须重配订阅 + 重新分配电话线
  tags: [flow, deletion, grace-period, security, restore]

- id: f23
  title: 分机关联与 RCC 验证四步——验连接/验话机/关联分机/三项测试
  type: flow
  source_pages: p111-116
  source_chapter: Associate extension numbers with Rainbow user accounts (How-To)
  source_quote: |
    "Once the association done, a new field is displayed, the Rainbow number. ... It will be automatically configured in Remote Extension number by the Rainbow agent (e.g. BBB10070254106463346) when the user selects 'computer' as routing from his Rainbow client (PC or smartphone)." (p115)
  summary: |
    四步：①验 PBX-Rainbow 连接——OXO 侧看 OMC/Cloud/Rainbow 连接状态；Rainbow 侧 My company/Communication → Comm Servers 页签确认 OXO in service；②OMC 里确认话机在服（虚拟课堂用 IPDSP 104 + MicroSIP，实验口径：需在 OMC/Subscriber-BaseStations list 开 auto-provisioning）；③关联分机——公司管理图标 → My company → Members → 选中成员 → Telephony 页签 → Equipment 选 OXO Connect → 选分机号 → Apply（分机列表与 Rainbow 实时同步；关联后出现 Rainbow number 字段，用户选 computer 路由时由 Rainbow 代理自动写入 Remote Extension number）；④RCC 测试三问——Rainbow 端选 Office phone 呼出给 OXO 用户通不通？来话能否在 Rainbow 端接听、有哪些动作？呼给纯 Rainbow 用户（无网关）不通。结果即 RCC 边界：能接/挂/转话机呼叫，音频全在话机。
  conditions: 无网关时纯 Rainbow 用户与 PBX 用户之间无法通话（此为预期行为，不是故障）
  tags: [flow, rcc, extension-association, rainbow-number, testing]

- id: f24
  title: WebRTC 网关定位与用例图——音频互操作（来话按路由振铃/去话达任意分机）
  type: diagram
  source_pages: p118-119
  source_chapter: OXO Connect WebRTC Gateway / Overview & Use case examples
  source_quote: |
    "The WebRTC Gateway brings voice interoperability between Rainbow Clients and PBX ecosystem. • This enables an audio media relationship between Rainbow applications and devices of a PBX connected to Rainbow" (p118)
    "Incoming Rainbow or PBX calls ring devices according to user's routing profile settings" (p119)
  summary: |
    定位：网关解决"音频媒体"关系，呼叫控制始终在 PBX。承载形态五种（安装要求清单）：OCE 集成虚拟机、OCE Front End 上的网关、NUC 迷你 PC 上的虚拟机、ESXi 服务器上的虚拟机（需 Rainbow Business/Enterprise 订阅）。两张用例图：来话——PBX 呼叫按用户路由档案同时分发到 PBX 设备（话机/DECT）与 Rainbow 客户端（WebRTC）；去话——从 Rainbow 呼任意内部分机或经 PSTN 出公网。
  conditions: 音频经 HTTPS/SRTP 加密（p126）；前提 PBX 已接入 Rainbow
  tags: [diagram, webrtc-gateway, audio, use-cases]

- id: f25
  title: WebRTC 网关三拓扑对比——OCE 集成 / OCE Front End / 外部 VM 或 NUC
  type: structure
  source_pages: p118-129
  source_chapter: OXO Connect WebRTC Gateway / Use case #1 (OCE integrated) & Use case #2 (OCE Front End)
  source_quote: |
    "Same feature level as the external WebRTC GW topology ... No need for SIP trunk licenses (bypass) • Supported for OCE and OXO Connect • Supported topologies: Integrated and External" (p125)
    "OCE Front-End does not provide PBX capabilities • OMC tool is not needed for OCE Front-End provisioning ... Internal GW: Not supported (Power CPU EE) / 20 calls max (Evolution IPBox); External GW (NUC): 50/50; OCE-FE GW: 20 calls max (Power CPU EE) / Not supported (Evolution)" (p129)
  summary: |
    三拓扑功能等价，差异在硬件、容量与许可：①OCE 集成（R3.2 起）——网关虚拟机集成在 OCE 内，免 SIP trunk 许可（bypass），用 OCE 管理工具即可维护，软件升级走 OXO 管理工具 + Cloud Connect Update；之前需外部网关 + 私有 SIP trunk + SIP trunk 许可。②OCE Front End——标准 OCE（IPBox）置于客户 LAN、在 OXO 呼叫服务器前面只跑网关；两端均须 ≥R4.0 MD；专用许可免费且由 FTR 自动下发；无 PBX 能力（无 UTL），OMC 不参与其开通；管理走 Rainbow Admin（耦合与激活）+ Cloud Connect（设备管理）。③外部 VM/NUC——上限 50 通话。容量矩阵（p129）：内部 GW 仅 Evolution 支持（20 上限）；外部 NUC 两类硬件都 50；OCE-FE 仅 Power CPU EE 支持（20 上限）。
  conditions: OCE 集成需 R3.2+；OCE-FE 需 ≥R4.0 MD（两端）；外部拓扑需 SIP trunk 许可与私有 SIP trunk（集成拓扑豁免）
  tags: [structure, topology, oce, front-end, comparison, licensing]

- id: f26
  title: 自动配置分工清单——自动建项 vs 安装员保留项（内部/外部两张单）
  type: structure
  source_pages: p121-122, p150
  source_chapter: OXO Connect WebRTC Gateway / Automatic configuration
  source_quote: |
    "The automatic configuration of the internal / external WebRTC gateway is available from system version R4.0.020.002 ... The following settings are still to be done by the installer as they are specific to each customer: • Connect PBX to Rainbow • Creation and association of the AnyDevice/Rainbow virtual terminals • Configuration of numbering plans and of the barring" (p121)
  summary: |
    内部网关自动建：网关激活（仅 OCE）、WebRTC SIP 网关创建、用 Rainbow PBXID 配 SIP 账号、VoIP 接入与中继组创建、ARS 路由表配置；安装员保留：连 PBX 到 Rainbow、AnyDevice/Rainbow 虚拟终端创建与关联、编号计划与闭锁。外部网关自动建：SIP 网关/SIP 账号/VoIP 接入与中继组/ARS 四项；安装员保留：连 PBX、外部虚拟机/独立 PC 的安装配置、虚拟终端、编号计划与闭锁、网关激活。自动配置由 Rainbow Reseller 管理员账号发起（编辑客户公司的 PBX 以激活，p122），激活动作触发 OXO 侧配置。
  conditions: R4.0.020.002+；发起人必须是 Reseller 管理员；编号计划与闭锁全书不教（在书外）
  tags: [structure, auto-config, boundary, installer, reseller]

- id: f27
  title: OXO 侧终端创建规则——Multiset（物理主站+Twinset 副站）与纯 Anydevice
  type: structure
  source_pages: p123
  source_chapter: OXO Connect WebRTC Gateway / Deployment steps on OXO Connect
  source_quote: |
    "Create the terminals for VoIP on PC (Softphone) • To be done whatever the topology, integrated WebRTC or external WebRTC • Create a Multiset • The main station is the physical station • The secondary station is • Free Rainbow in Twinset from R6.0 • (Anydevice up to R5.2)" (p123)
    "Secondary station from Release 6.0: The Free Rainbow in Twinset virtual terminal must be used in order to save an UTL license (UTL Bypass)" (p123)
  summary: |
    无论选哪种网关拓扑，OXO 侧终端都要按此规则建：有物理话机的用户建 Multiset——主站为物理话机，副站从 R6.0 起必须用"Free Rainbow in Twinset"虚拟终端（省一个 UTL 许可，即 UTL Bypass），R5.2 及以前副站位置用 Anydevice；只有 Rainbow 没有话机的用户只建一个 Anydevice 终端。配置细节以 TC2479（Rainbow WebRTC Gateway with OXO Connect / OXO Connect Evolution）为准。
  conditions: 版本语义分界在 R5.2/R6.0——升级交付时副站类型要按版本改；细节查 TC2479 最新版
  tags: [structure, terminal, multiset, twinset, anydevice, utl]

- id: f28
  title: OCE Front End 部署链——FTR 开通 → Rainbow 侧激活 → OMC 侧核验
  type: flow
  source_pages: p130-135
  source_chapter: Use case #2 / Installation & Rainbow BP administration & OMC configuration
  source_quote: |
    "Installation of the OCE Front-End is automated with the FTR procedure • FTR provides the OCE Front-End license and upgrades the OCE release (≥ R4.0 MD) if necessary ... Connect to the OCE Front-End ETH1 in DHCP mode • and start a Web browser to 192.168.94.246" (p130)
    "Define the product type 'Frontend WebRTC' ... FTR OK — This IPBox is now an OXO Connect FrontEnd WebRTC Gateway and ready to be associated to the OXO Connect customer call server" (p131)
    "Rainbow PBXID must be the same in both OXO Connect, Front-End and call server ... Verify port numbers to 5059 in the SIP Gateway parameters" (p134)
  summary: |
    四段链路：①FTR 开通——ETH1 DHCP 接入 → 浏览器开 192.168.94.246 → 首连设安装口令（例 Alcatel1，实验口径）→ 产品类型选 Frontend WebRTC → 录客户参考号与 IP 参数 → FTR OK（许可免费自动下发，版本不足自动升到 ≥R4.0 MD）；②设备侧收尾——改 Front-End 配置后必须 warm reset 才生效，状态可在 Settings 菜单与 Webdiag 查；③Rainbow 侧——BP 管理员给客户公司激活 WebRTC 网关，类型选 External on OCE Front End（上限 20）；④OMC 侧核验——呼叫服务器上自动生成私有 SIP 网关，核对 SIP 网关参数端口 5059；两台 OXO（Front-End 与 call server）的 Rainbow PBXID 必须一致（FTR 时默认占位 FleetRef-Installref，公司已建过则两台都填正式 PBXID）；OMC 分别检查两台设备的 Rainbow 状态。细节按 MyPortal 的 Rainbow WebRTC cookbook。
  conditions: ≥R4.0 MD 强制（两端）；端口核对 5059；FTR 默认 PBXID 为占位值需替换；192.168.94.246/Alcatel1 为实验口径示例
  tags: [flow, ftr, front-end, omc, activation, cookbook]

- id: f29
  title: OCE-FE 开通场景分支树（新装/加装/有无 Fleet 参考）
  type: structure
  source_pages: p137
  source_chapter: Use case #2 / Commissioning scenarios
  source_quote: |
    "The commissioning of an OCE-FE can be done with different scenarios: New complete installation, PBX + OCE-FE / Adding OCE-FE to an existing PBX (• PBX already existing in R4 • Existing PBX version lower than R4) / Order made WITH or WITHOUT Partner fleet reference and Installation reference" (p137)
  summary: |
    开通场景分三个维度组合：①全新完整安装（PBX + OCE-FE 一起上）；②在既有 PBX 上加装 OCE-FE——又分既有 PBX 已是 R4、低于 R4 两种（后者涉及升级顺序）；③订单是否带伙伴 Fleet 参考号与安装参考号（影响 FTR 与 Cloud Connect 侧自动关联）。每种场景的操作差异以 Rainbow WebRTC cookbook 最新版（MyPortal）为准，教材明确"必须follow该文档"。
  conditions: 场景细节在书外（cookbook）；不同场景 FTR/Cloud Connect 行为不同
  tags: [structure, scenarios, commissioning, cookbook]

- id: f30
  title: 外部 WebRTC 网关部署流程——VMware（.ovf）与 NUC（ISO）两条线
  type: flow
  source_pages: p139-145
  source_chapter: Use case #3 (VMware) & Use case #4 (Mini PC / NUC)
  source_quote: |
    "Deploy the .ovf file with Vmware ESXi and start the virtual machine ... Configure the Network settings (static or DHCP) • IP, NETMASK, GATEWAY and DNS • Add the OXO Connect IP@ and Rainbow PBXID • TURN server configuration according to site location" (p141)
    "Mini PC installation: • Download the ISO file from MyPortal • Create a Bootable USB drive • Install the ISO file on the mini PC Storage device • Reboot the standalone PC and setup the configuration parameters" (p145)
  summary: |
    两条部署线共享后半段：VMware 线——从 MyPortal 下载网关虚拟机包 → ESXi 部署 .ovf 并开机 → 配网络（静态/DHCP：IP、掩码、网关、DNS）→ 填 OXO Connect 地址与 Rainbow PBXID → 按站点位置配 TURN 服务器；NUC 线——MyPortal 下 ISO（同一软件包内含 OVF 与 ISO）→ RUFUS 等工具做启动 U 盘 → 装进 mini PC 存储 → 重启进配置，其余步骤与 VM 相同（防火墙白名单在安装手册中）。Rainbow 侧收尾——给公司勾"Activate the WebRTC gateway"，定义为外部网关并定通道数（OXO 侧自动配置）；用户侧——每人 Business 或 Enterprise 许可 + Rainbow 账号关联其 PBX 话机。
  conditions: 部署程序从 Rainbow Support 网站 ALE equipments (PBX) 区下载；TURN 位置选择与防火墙白名单在书外（安装手册/cookbook）
  tags: [flow, vmware, nuc, esxi, turn, deployment]

- id: f31
  title: 网关容量规划表——用户数/通道数对照与 20/50/150 三条上限
  type: structure
  source_pages: p147
  source_chapter: Dimensioning / Rainbow WebRTC gateway dimensioning
  source_quote: |
    "50 VoIP calls maximum if the WebRTC gateway is external on Mini PC or ESXi server • 20 VoIP calls maximum with OCE integrated WebRTC gateway or if the WebRTC gateway is external on OCE Front End ... Maximum of OXO users with Rainbow VoIP option increased from 50 to 150" (p147)
  summary: |
    推荐对照表（Rainbow VoIP 用户数 → 通道数）：5→5、10→7、20→11、30→15、50→20（外部/集成两列同值）；外部（OXO 与 OCE）70→27、100→36、150→50；集成（OCE）70/100/150 标 (*)——20 通道配置下的方向性值，实际取决于通道数与话务量，低话务可到 150。三条硬上限：外部网关（Mini PC/ESXi）最大 50 通话；OCE 集成或 OCE Front End 最大 20 通话；OXO 用户带 Rainbow VoIP 选项的上限从 50 提到 150（OXO Connect 与 Evolution 均适用）。通道不够时 OCE 也可改用外部网关拓扑扩展到 50。
  conditions: 括号值依赖话务模型；话务建模本身在书外
  tags: [structure, dimensioning, capacity, channels, limits]

- id: f32
  title: 内部网关自动配置操作流——Reseller 激活 → 定通道 → OMC 核验
  type: flow
  source_pages: p149-154
  source_chapter: Internal WebRTC Gateway automatic configuration on OXO Connect Evolution (How-To)
  source_quote: |
    "Automatic activation of the WebRTC gateway is performed by the trainer with a reseller administrator account ... He is the only authorized account to manage this service" (p151)
    "Client Company / Communication — Manage connection ... Information tab — Select Activate WebRTC Gateway ... Settings tab — Select 'Internal' and set the number of channels" (p151-153)
    "OMC / Cloud / Rainbow — WebRTC Gateway is Connected and Enabled" (p154)
  summary: |
    操作流四步：①Reseller 管理员登录 Rainbow（唯一有权管理此服务的账号）；②进入客户公司 Communication → Manage connection 编辑其 PBX；③Information 页签勾 Activate WebRTC Gateway → Settings 页签选 Internal 并设通道数 → 激活完成（客户管理员即可在连接状态里看到）；④OMC 核验——OMC/Cloud/Rainbow 显示 WebRTC Gateway Connected and Enabled，确认自动建的 SIP 网关/账号/中继/ARS 都已落地。适用版本 R4.0.020.002+。
  conditions: R4.0.020.002+；仅 Reseller 管理员可激活；内部网关仅 OCE（Evolution）支持
  tags: [flow, auto-config, internal-gateway, activation, menu-path]

- id: f33
  title: 虚拟终端配置流程——Twinset 副站与 Anydevice 两条线 + UTL 口径
  type: flow
  source_pages: p155-161
  source_chapter: Configure Anydevice/Rainbow virtual terminals for OXO Connect users (How-To)
  source_quote: |
    "Deskphone + Free Rainbow virtual terminal = 1 UTL • Anydevice only = 1 UTL" (p156)
    "OMC/Subscribers list — Create a Virtual terminal Free Rainbow in twinset ... This virtual terminal must be added as a secondary set of the main extension of the user" (p157)
  summary: |
    两种用户形态的配置线：①有话机 + Rainbow 应用——OMC/Subscribers list 为每个用户建 Free Rainbow in Twinset 虚拟终端（实验口径：用户 100 建 130、101 建 131、V-Class 的 IPDSP 104 建 135），再把它挂为该用户主分机的副站（Multiset）；②纯软话机——OMC 建 Anydevice 终端（实验口径：user2 建 132、V-Class user1 建 133），再到 Rainbow 侧绑定——Members → 选中成员 → Telephony 页签 → Equipment 选 OXO Connect → 选该 Anydevice 号 → Apply。许可口径：话机+Twinset 副站=1 UTL，纯 Anydevice=1 UTL。配完验证：用户可在 computer/office phone/other number 间选路由并改呼转；测试矩阵含电脑↔电脑、话机↔电脑、三方会议、屏幕共享、视频。
  conditions: 副站类型按版本（R6.0 起 Twinset，见 f27）；号码 130-135 为实验口径
  tags: [flow, twinset, anydevice, utl, omc, menu-path]

- id: f34
  title: Attendant 话务台四功能区 + 三种显示格式
  type: structure
  source_pages: p164-166
  source_chapter: Rainbow Attendant Console & Mutual aid supervision groups / Attendant console
  source_quote: |
    "Call queue (X calls) / Call Control of current communication / Busy Lamp Field area (Supervision) / Supervision Groups — Attendant console" (p165)
    "Call queue management - Manage up to 10 calls for OXE - And up to 8 calls for OXO Connect ... An Attendant subscription is required for each member using this feature • Available on the Rainbow Web and Desktop applications" (p164)
  summary: |
    话务台界面四功能区：①呼叫队列（X calls）——OXE 10 路/OXO Connect 8 路；②当前通话的呼叫控制；③Busy Lamp Field 监督区（成员在场与呼叫状态）；④监督组页签区。三种显示格式 Normal/Small/Condensed 适配不同屏。能力范围：监督成员状态与呼叫控制、队列管理、代接/转移/留言转发/呼转状态管理；成员与话务员必须在同一监督组（管理员建）。前提：每个使用者要有 Attendant 订阅；仅 Web 与 Desktop 应用可用（移动端无），话务员本身要有电话线 + VoIP 软话机能力。
  conditions: 仅 Web/Desktop；队列上限 OXE 10 / OXO 8；Attendant 订阅强制
  tags: [structure, attendant-console, ui-zones, queue]

- id: f35
  title: 监督组结构规格——5 组/监督员、30 人/组与平台限制
  type: structure
  source_pages: p167-169
  source_chapter: Attendant console / Supervision groups & Miscellaneous
  source_quote: |
    "Maximum number of supervision groups for a supervisor / Maximum number of users in a group (supervisors + supervised): 5 / 30" (p167)
    "Interception is only possible if supervisors and supervisees are on the same PBX. Only phone calls can be intercepted." (p169)
  summary: |
    监督组规则：监督员（须 Attendant 许可）与被监督成员同组；每位监督员最多 5 个组，每组（监督员+被监督者）最多 30 人。界面原理：每个组一个页签，不可见页签来话显示红点提示，可开音频通知，另有页签复现监督员收藏夹。可行动作：拦截被监督用户的来话、强制呼转（转语音信箱）或取消呼转。硬限制：话务台功能只在 PC（厚客户端/Web）；保持通话数取决于软话机线的多线资源（OXE REX 最多 10 路、OXO Connect Anydevice R6 起最多 8 路）；代接/拦截仅限监督员与被监督者在同一 PBX 且仅限电话呼叫；所有呼叫仍由 PBX 处理。配置参考 TC2462（OXE）/TC2479（OXO）。
  conditions: 拦截限同 PBX、限电话呼叫；Hold 上限受多线资源约束；细节查 TC2462/TC2479
  tags: [structure, supervision-group, limits, interception]

- id: f36
  title: 互助监督组机制——动态进出/临时纳排/代接边界
  type: structure
  source_pages: p170-173
  source_chapter: Mutual aid supervision groups
  source_quote: |
    "You can supervise two types of group. • Groups that are permanently affiliated to you • Groups that you can join on an ad hoc basis in one click at times ... Works only for PBX calls, not for Rainbow softphone calls" (p171)
  summary: |
    机制三要素：①两类组——长期隶属组与可一键加入/退出的互助组（被锁 Locked 的组不能退出）；②临时成员操作——监督员可临时纳入或排除某个被监督用户（典型场景：成员离开忘了入组）；③来话通知与代接——监督员收到被监督用户的来话通知并可代接，但仅限 PBX 电话呼叫，Rainbow 软话机呼叫不可。应用视图分 Supervisor app（监督的呼叫、代接、进出组、最多同时监督 4 通呼叫）与 Member app（所在组、进出组、锁定组）。管理上与普通组建法相同，只是 Type 选 Mutual aid group，并定义监督员角色与两种画像的 In/Out 权限。
  conditions: 代接仅限 PBX 呼叫；Locked 组不可退出；监督上限 4 通并行呼叫（App 视图）
  tags: [structure, mutual-aid, supervision, dynamic-membership]

- id: f37
  title: 话务台订阅与监督组建组操作流（含互助组建组字段）
  type: flow
  source_pages: p175-181
  source_chapter: Attendant console and Mutual aid supervision groups (How-To)
  source_quote: |
    "Companies/Customer companies/ <company to manage> 'Subscriptions' section / Service: ATTENDANT ... Click 'Subscribe to offer' ... Attendant Monthly ... DON'T USE 'PREPAID' IN THE TRAINING" (p176)
    "Companies/Customer companies/ <company to manage> 'Communication' section / 'Supervision' tab — Click on 'Create' ... Name / Description / Type: Mutual aid group / Lock the last member Yes/no" (p178, p180)
  summary: |
    操作流：①开订阅——Companies/Customer companies/<公司> 的 Subscriptions 区 → Service 选 ATTENDANT → Subscribe to offer → 选 Attendant Monthly → 定数量 → Subscribe（实验口径：培训禁用预付）；②分订阅——Members 区 → 编辑用户 → Services 页签 → 选 Attendant Monthly；③建监督组——Communication 区 → Supervision 页签 → Create → 填 Name/Description → 选带 Attendant 订阅的监督员 → 勾被监督成员 → Create（普通组字段只有 Name/Description）；④用监督员账号登录 web.openrainbow.com 或客户端 → 点话务台图标进入 Attendant console。互助组：同一路径 Create，多两个字段——Type 选 Mutual aid group、Lock the last member（是/否）；被监督成员必须有物理分机或 PBX 软话机（IPDSP/MicroSIP）。
  conditions: 实验口径：仅月付；被监督成员须有物理话机或 PBX 软话机（互助组）
  tags: [flow, attendant, subscription, supervision-tab, menu-path]

- id: f38
  title: Rainbow 维护支持体系八件套——日志/用户上报/状态页/维护预告/告警/操作历史/HelpDesk/SR
  type: structure
  source_pages: p183-193
  source_chapter: MAINTENANCE
  source_quote: |
    "Your users can report problems they encounter directly in their Rainbow interface ('Help and Support' menu, 'Report a problem'). ... The integrator partner has the same reports as the customer, so he can help with end user support." (p185)
    "status.openrainbow.com — The button 'Get updates' allows, if you wish, you can subscribe to alerts by different methods." (p186)
  summary: |
    运维闭环八个抓手：①用户日志——Rainbow 界面点头像 → About Rainbow → Open logs（另有 p89 路径 User Settings → About Rainbow → Open logs）；②用户问题上报——Help and Support → Report a problem（录日期时间/描述/附件/同意支持用日志；管理端统一查看全部事件并可取事件日志；集成商与客户看到同样的上报，便于代维）；③云状态页——status.openrainbow.com，Get updates 订阅告警，可按主题与地域过滤（法国建议勾 WW/EMEA/DE，实验口径建议）；④维护预告——管理门户内看计划内维护及影响等级（颜色区分），按地域与架构（Hybrid/Hub）过滤；⑤告警——设阈值通知音频质量劣化与无音频；⑥操作历史——全部管理操作留档，按类别/类型/日期过滤，多管理员并行时查谁做了什么；⑦Help Desk 指南——help.openrainbow.com 的排障/找日志/报障入口；⑧SR——入口支持邮箱 support@openrainbow.com、Emily BOT、Global Welcome Center（ALE.WelcomeCenter@al-enterprise.com）或电话，且只有 Rainbow 认证伙伴才会被建 ESR。
  conditions: ESR 仅对 Rainbow 认证伙伴创建；web 端用户上报不采集日期（浏览器日志短生命周期）
  tags: [structure, maintenance, logs, status-page, alarms, history]

- id: f39
  title: MyPortal 开 SR 的字段路径（两页表单）
  type: menu-path
  source_pages: p190-193
  source_chapter: MAINTENANCE / Open a Service Request
  source_quote: |
    "Connect to MyPortal • Support > Service Request • Click on Create SR: • SR category= Rainbow • SR type = product support • Severity • Subject • Mail + Description" (p192)
    "• End Customer Company Name • Product Category = Rainbow • Rainbow Version • Details • Subcategory • Rainbow SIP trunk • How found (Origin): Customer site, Beta, demo… • Customer Internal Ref" (p193)
  summary: |
    MyPortal 开 SR 路径与两页字段：登录 MyPortal → Support → Service Request → Create SR。第一页：SR category 选 Rainbow、SR type 选 product support、Severity、Subject、邮箱+描述；第二页：终端客户公司名、Product Category=Rainbow、Rainbow 版本、详情、子类、Rainbow SIP trunk、发现来源（客户现场/Beta/演示等）、客户内部参考号。这是售后升级 ALE 官方的标准通道，前置条件见 f38（认证伙伴）。
  conditions: 需 Rainbow 认证伙伴身份才会建 ESR
  tags: [menu-path, sr, myportal, support]

- id: f40
  title: Teams 集成架构与四条呼叫流程（1-2-3-4/5 步骤图）
  type: diagram
  source_pages: p196-206, p212-216
  source_chapter: INTEGRATION WITH MICROSOFT TEAMS / Architecture & User experience
  source_quote: |
    "The integration is done at the workstation level" (p196)
    "Rainbow App — Managed by the Rainbow Telephony Power App: Telephony settings..., Call history..., Call voicemail..., Dial pad / Rainbow desktop — Managed by the Rainbow desktop app: Click-to-call from any desktop app (hotkey dialing), Management of single calls" (p198)
  summary: |
    架构：工作台级集成（非租户级），两个组件分工——Teams 内的 Rainbow App（Telephony Power App 管：电话设置/呼转/热键、通话历史含未接、语音信箱与未读提醒、拨号盘）+ Rainbow Desktop（管：任意桌面应用热键点击外呼如 F6、单路呼叫控制接听/挂断/取消）。四条呼叫流程：①内呼——Teams 拨 31000 → MakeCall API → 经 CSTA MakeCall API 到 OXE/OXO CE → 话机振铃 → Desktop 做呼叫控制（5 步）；②外呼——拨 +33xxxxxx → MakeCall API → 经 WebRTC 网关出 PSTN → Desktop 呼叫控制（4 步）；③外线来话（无网关路径）——PBX 收到 → 话机呈现 → Rainbow 收来话通知 → 电脑上呈现并控制（4 步）；④外线来话（WebRTC 网关路径）——PBX 收到 → 经网关建 WebRTC 呼叫 → 电脑上呈现（3 步）。
  conditions: 需要 WebRTC 网关才有 VoIP 音频路径；桌面组件必须常驻（见 f44）
  tags: [diagram, teams, call-flows, architecture]

- id: f41
  title: Teams 部署四要素——应用上架/权限同意/订阅/权限收敛
  type: structure
  source_pages: p207-210
  source_chapter: INTEGRATION WITH MICROSOFT TEAMS / Rainbow App availability & Subscription & Permissions
  source_quote: |
    "User must have one of these subscriptions: • Business • Enterprise. Permissions ... limit Rainbow collaboration features as collaboration services will be provided natively by Teams itself" (p208)
    "Rainbow desktop application is required and must be running" (p209)
  summary: |
    部署清单四项：①应用上架——Rainbow App 可默认在 Teams 应用商店，也可由管理员上传 zip；②权限同意——可由管理员直接授权（见 f42 两种方式）；③订阅——用户须有 Business 或 Enterprise；④权限收敛——协作功能交给 Teams 原生提供，Rainbow 侧只保留 Telephony 权限，避免双轨。另有一条硬前提：终端必须安装并运行 Rainbow Desktop 应用。
  conditions: 订阅限 Business/Enterprise；Rainbow Desktop 必须安装并运行
  tags: [structure, teams, deployment, permissions, subscription]

- id: f42
  title: Teams 应用上架与权限同意流程（Teams 管理中心两条路 + Azure 核验）
  type: flow
  source_pages: p222-230
  source_chapter: Rainbow for Teams installation (How-To)
  source_quote: |
    "Teams admin center web interface Using following URL: https://admin.teams.microsoft.com ... select the 'Teams apps' menu ... Then, select the 'Manage apps' submenu ... To give to users the possibility to install it, the status must be 'Allowed'." (p223-224)
    "Consent the permissions required by the Rainbow app for Teams by one of the 2 following methods: ­ Validation by the Teams admin interface ­ Validation when an administrator first logs in to the app" (p226)
  summary: |
    三段：①上架——Teams 管理中心（admin.teams.microsoft.com）→ Teams apps → Manage apps → 搜 Rainbow：Release Status 为 "--" 表示属微软第三方应用目录，状态置 Allowed 用户才能装；搜不到则 Upload new app 传 zip，上传后 Publication status=published、默认 Allowed；②权限同意二选一——(a) 管理中心内点 Rainbow app → Permissions 页签 → Review permissions and consent → Accept（最简，用户端登录不再弹同意）；(b) 管理员首次登录 Teams 内 Rainbow App 时弹同意框，勾选项可为全组织统一授权；③Azure 核验——Permissions 页签 → Go to Azure Active Directory → 在 Azure 侧确认权限已添加且由管理员授予（两条路殊途同归）。
  conditions: 核验动作在 Azure AD 层面；方法 (a) 推荐为"最简单最合理"
  tags: [flow, teams, consent, admin-center, azure-ad, menu-path]

- id: f43
  title: Teams 集成用户配置三步——关联话机/收敛权限/配订阅
  type: flow
  source_pages: p231-235
  source_chapter: Rainbow user configuration for Teams integration (How-To)
  source_quote: |
    "As the user will use Teams for all collaboration services, Rainbow will only provide telephony integration services. So, it is better to apply a restrictive permission to users with Teams integration in order to forbid collaboration services from Rainbow. ... Assign the 'telephony' permission to the user." (p234)
  summary: |
    三步：①关联 PBX 用户与 Rainbow 账号——web.openrainbow.com 管理员登录 → Manage your company → My company → Members → 选中成员 → Telephony 页签 → Device 字段选 PBX + 分机号 → Apply（关联后显示 Rainbow number，用途同 f23）；②权限管理——My company/Members → 成员 → Permissions 页签 → 只给 Telephony 权限 → Apply（协作功能由 Teams 提供，Rainbow 侧收敛）；③订阅——同一成员 Services 页签 → 选 Business 或 Enterprise → Apply。
  conditions: 订阅必须 Business/Enterprise；权限收敛为官方建议做法
  tags: [flow, teams, user-config, permissions, menu-path]

- id: f44
  title: Teams 内连接器安装与在场同步激活流程
  type: flow
  source_pages: p236-244
  source_chapter: Rainbow for Teams installation (connector & presence sync How-To)
  source_quote: |
    "THE RAINBOW APPLICATION INTEGRATED INTO TEAMS REQUIRES THE INSTALLATION AND STARTUP OF THE RAINBOW DESKTOP APPLICATION ON THE PC." (p239)
    "SSO is not required to use the Rainbow/Teams connector." (p241)
    "As here we especially want to activate the presence synchronization between Teams and Rainbow, we activate the sharing of information with Office 365." (p243)
  summary: |
    流程四段：①装应用——Teams 客户端 Apps → "Built for your org"（组织已上架时）或搜索 → Add → 确认 Add；②启动登录——点 Sign in；未预授权时用户会被要求自行同意权限（技巧：首次由管理员账号添加以便全组织授权）；桌面组件依赖——Teams 内 App 要求 PC 上已装并运行 Rainbow Desktop：显示 "!" 图标时悬停点 Start → Rainbow Desktop → Continue（未登录则输凭证；SSO 可选非必须），连上后 "!" 换成 Rainbow 图标；③在场同步先测后开——先改 Teams 在场状态验证 Rainbow 侧不同步（基线），再点共享图标 → 开启与 Office 365 的信息共享 → 选用户账户 → Close；④复测——改 Teams 状态（如 Busy），Rainbow 在场随之同步。
  conditions: Rainbow Desktop 必须在 PC 上安装且运行；在场同步经 O365 信息共享激活；SSO 非必需
  tags: [flow, teams, connector, presence, office365, desktop-dependency]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-18）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 核查网络前提 + Pilot 评估 | 有 | f07, f08 | 文档体系结构 + Pilot 工具流程；端口/带宽数值属数值类，不在本文件展开 |
| task-02 | 规划创建公司体系 | 有 | f09, f10, f11, f12, f13 | 公司概念、六步主流程、可见性四级、认证体系、创建入口 |
| task-03 | 管理员权责 + 目录/频道 | 有 | f14, f15 | 两级权责结构 + 目录/频道两步路径 |
| task-04 | 订阅开通与分配 | 有 | f06, f16 | 8 种订阅体系 + 两层流转流程 |
| task-05 | OMC 安装首连 | 有 | f17 | 安装-连接-证书-改密-客户信息四步 |
| task-06 | 修改 IP 规划 | 有 | f18 | OMC/Lan/IP configuration 路径 + PC 侧 |
| task-07 | PBXID+激活码接入与验证 | 有 | f19 | 找凭证→填入→Webdiag/ccrbagent.log 三段 |
| task-08 | 成员创建与管理 | 有 | f20, f21, f22 | 三法、设置分区、删除宽限与安全操作 |
| task-09 | 分机关联与 RCC 验证 | 有 | f23 | 四步关联流程 + Rainbow number 机制 + RCC 边界 |
| task-10 | 网关拓扑决策 | 有 | f24, f25, f26, f27 | 定位用例图、三拓扑对比、自动配置分工、终端创建规则 |
| task-11 | 按拓扑部署网关 | 有 | f28, f29, f30 | OCE-FE FTR 链、开通场景分支、VMware/NUC 部署线 |
| task-12 | 容量规划 | 有 | f31 | 容量表结构与 20/50/150 上限（话务建模在书外） |
| task-13 | 内部网关自动配置 | 有 | f32, f26 | Reseller 激活→OMC 核验操作流 + 分工清单 |
| task-14 | 虚拟终端配置 | 有 | f33, f27 | Twinset/Anydevice 两条配置线 + UTL 口径 |
| task-15 | 话务台与监督组 | 有 | f34, f35, f37 | 四功能区、组规格 5/30、订阅建组操作流 |
| task-16 | 互助监督组 | 有 | f36, f37 | 动态进出机制 + 建组字段（Type=Mutual aid group、Lock last member） |
| task-17 | 维护体系排障 | 有 | f38, f39 | 八件套结构 + MyPortal SR 路径 |
| task-18 | Teams 集成全流程 | 有 | f40, f41, f42, f43, f44 | 架构与四条呼叫流程、部署四要素、上架同意、用户配置、连接器与在场同步 |

补充说明：
- f01（课程推进逻辑）、f02/f03（RLAB 与 SIP 模拟器结构）、f04/f05（平台架构图）不直接对应某个 task，属于 BOOK_OVERVIEW 骨架 1-2 的框架底座与全书主线（f10 六步主流程是 18 项任务的组织轴）。
- 全部 18 项 task 均有框架类条目覆盖，无"该 task 无框架类内容"的情况；数值类细节（端口清单、带宽、实验账号口令全集、容量表逐格数值）留待数值提取器处理，本文件只保留结构锚点与菜单路径。
- 生产化边界提示（来自 BOOK_OVERVIEW 批判节）：网络端口/TURN/防火墙细节指向 Rainbow Network Requirements PDF；OXO 侧网关细节指向 TC2479（OXE 为 TC2462）；OCE-FE 开通场景指向 MyPortal 的 Rainbow WebRTC cookbook。三份外部文档是各框架条目落地生产环境的必备补充。
