# 框架/流程/结构候选 — OpenTouch Fax Center Starter (OTFCXTE200EN R9.2 Ed04)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、界面分区。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——认知地基 → 安装闭环 → 管理面 → 两大外部集成 → 运维纵深
  type: flow
  source_pages: p3-233
  source_chapter: 全书章节排布（OTFC overview / Key concepts / Architecture / Installation & Basic configuration / Clients overview / Manage users & administrators / User Profiles / Phone Books / OmniPCX Enterprise & OTFC / SMTP integration / Services OTFC / Advanced configuration / Maintenance）
  source_quote: |
    "The OpenTouch Fax Center solution is a suite of powerful fax services which interact with the
    OmniPCX Enterprise (OXE)" (p4)
    "Lesson summary • Ecosystem example • Installation step-by-step • Basic configuration •
    OmniPCX Enterprise configuration" (p44)
  summary: |
    课程分十段推进：①OTFC 概览（p3-20，定位/能力/合规/收发图示）；②关键概念（p21-30，System/Site/User/Profile、队列历史、组件流程）；③架构（p31-42，部署形态/生态/多网关多站点/支持矩阵）；④安装与基础配置（p43-70，实验生态 + 准备服务器/安装/FTW 三个 How-To）；⑤客户端概览（p71-96，管理双入口/用户四件套/封页）；⑥用户与管理员（p97-116 + How-To）；⑦Profile 与电话簿（p117-139）；⑧OXE 集成（p140-155 + OXE SIP 网关 How-To）；⑨SMTP 集成（p156-175 + How-To）；⑩服务架构、高级配置与维护（p176-232 + 备份恢复 How-To）。这是"先装起来、再接两端（OXE/邮件）、最后管好运维"的交付主线，也是实际项目的推荐顺序。
  conditions: 无特殊版本前提；OXE 侧细节外置 TC3048
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: OTFC 能力全景——定位/传输/合规三张清单
  type: structure
  source_pages: p4-12
  source_chapter: What Is OTFC? / OTFC solution supporting / Send & Receive / other Features / Serviceability / Security
  source_quote: |
    "The OpenTouch Fax Center solution is a suite of powerful fax services which interact with the
    OmniPCX Enterprise (OXE) • Hardware agnostic • Installed on a dedicated server or virtual
    machine" (p4)
    "Sensitive documents in TIFF or PDF format are routed to only approved recipients and
    designated secure printers/MFPs ... Fax deletion options allow the system to be configured
    for zero retention if desired ... An automated event log ensures advanced traceability" (p6)
  summary: |
    三张清单构成本书的能力叙事：①基础能力（p5）——收发传真服务器、Web+客户端双管理、AD/Exchange 集成、文档管理、出/入局转换、归档审计、安全可靠；②传输与安全（p6-7）——加密保护文档隐私并支持 GDPR/HIPAA/FERPA/SOX 合规、敏感文档只路由给批准的收件人与指定安全打印机/MFP、可配零保留、自动事件日志；③可服务性与安全（p11-12）——归档外置存储、Web 报表、经 OmniVista 8770 计费、用户清单导出、SNMP trap V2、可配密码策略、第三方组件安全更新。售前/选型按这三张清单对答。
  conditions: 合规法规为原文列举；安全配置细节全书未展开
  tags: [structure, overview, compliance, feature-list]

- id: f03
  title: 发送/接收入口矩阵与入局路由四法
  type: structure
  source_pages: p8-10, p15-18
  source_chapter: Send Faxes From / Receive Faxes From / Inbound routing methods / Illustrations
  source_quote: |
    "Anywhere through web access • Any e-mail messaging system • Any desktop application through
    a virtual fax printer • Scheduled fax sending from all above interfaces • Barring linked to
    a user profile. e.g. national only" (p8)
    "To one or several email addresses (HTML or text format, Fax attachments in PDF or fax
    TIFF) • To one or several users via the web interface • To one or several printers • Into a
    folder (Local to the fax server, Shared network folder) ... Inbound routing methods •DNIS,
    CSID, ANI, DTMF" (p9)
  summary: |
    发送入口四类（Web/邮件/虚拟打印机打印/SendFAX 及 MFP，见 f04）+ 全入口支持定时发送 + 按 Profile 闭锁（如仅国内）；接收去向四类（邮箱 HTML/文本 + PDF/TIFF 附件、Web 界面、打印机、本地/共享文件夹）；入局路由依据 DNIS、CSID、ANI、DTMF 四种（书中未展开四个缩写全称）。附加特性（p10）：委托访问、定时、Web 电话簿、邮件 From 字段含传真号、广播完成通知、Office 邮件合并群发、O365 支持。
  conditions: 45 种文件格式以 Feature List 为准（p18）
  tags: [structure, interfaces, routing, inbound]

- id: f04
  title: 收发图示三张——邮件/Web/打印三通道、MFP/文件夹、虚拟打印机三条径
  type: diagram
  source_pages: p15-17
  source_chapter: Illustrations / Sending & receiving Faxes 1-2/2 / Methods available from any applications
  source_quote: |
    "From an e-mail client •From a web browser ... Mail server OTFC Email connector ... From
    SendFax or any printing capable application (Print to fax)" (p15)
    "T.37 capable LAN multifunction printer ▪From multifunction printers ▪Folder (fax reception
    only) ▪ Fax 1.pdf ▪ Fax 2.pdf Local or network folder" (p16)
    "Using Print to mail ... OR Using web fax composer ... Based on 'virtual' printers ▪Using
    SendFAX" (p17)
  summary: |
    三张图给出全部收发路径：①图一（p15）——邮件客户端经邮件服务器→Email connector→OTFC；Web 浏览器直连 OTFC；SendFAX 或任意可打印应用走 Print to fax；②图二（p16）——T.37 能力的局域网多功能一体机（MFP）可发可收；文件夹只收（本地或网络共享，产 Fax 1.pdf/Fax 2.pdf，可直查或经定制应用调阅）；③图三（p17）——Windows 客户端三条虚拟打印机路径：Print to mail（经邮件服务器+Email connector）、Web Fax Composer（进 Web 客户端）、SendFAX（XML 直达 OTFC）。
  conditions: MFP 发送依赖 T.37 能力；文件夹仅收不发
  tags: [diagram, interfaces, mfp, virtual-printer, folder]

- id: f05
  title: 组件流程链——入局路由图 + 外发/内收流水线
  type: flow
  source_pages: p19, p26-27
  source_chapter: Routing / Fax flows (Outbound fax flow, Inbound fax flow)
  source_quote: |
    "OmniPCX Enterprise routes the incoming fax to the Fax Server. Fax server internal routing
    table based on: -- called number -- calling fax machine identifier ... Notification rules
    Printer Folder" (p19)
    "The Gateway receives a fax submission. Note: The 'Gateway' here is either SmtpGateway or
    XmlGateway, depending on the client application that submits the fax. The Gateway transfers
    it to the FaxManager." (p26)
  summary: |
    外发流水线（p26 七步）：Gateway（SMTP 或 XML，取决于提交方客户端）收传真提交 → 转 FaxManager → FaxManager 通知 DocumentRasterizer 把封面与附件转 TIFF → 通知 FaxDriver 发送 → 通知 SMTP Gateway 发回执通知 → 通知 FaxArchive 入库。内收流水线（p27 四步）：FaxDriver 收传真 → 转 FaxManager → 通知 SMTP Gateway 把传真路由给用户等目的地 → 通知 FaxArchive 入库。入局路由图（p19）：OXE 把来传真正到传真服务器，内部路由表按被叫号码/主叫传真机标识匹配，再按通知规则投递打印机/文件夹/邮箱。
  conditions: 广播（p28）共享相同附件与封面；归档用 MySQL（XMFaxArchive 与 XMCoConfig，p29）
  tags: [flow, component-chain, outbound, inbound, routing]

- id: f06
  title: System/Site/User/Profile 概念模型与属性联动
  type: structure
  source_pages: p22-24
  source_chapter: Key concepts
  source_quote: |
    "System •Global management & system settings •Sites management ; Site •Virtual Fax Server
    •Each site has its own set of users and settings. •Sites are isolated from each other. •One
    fax belongs to one and only one site." (p22)
    "In OpenTouch Fax Center, a user is always identified by an SMTP Address." (p23)
  summary: |
    四级模型：System（全局管理与站点管理）→ Site（虚拟传真服务器，共享系统资源，站点间隔离，一份传真只属于一个站点，可对应公司/分支/部门）→ User（属于一个 Site、有一个 faxing Profile，恒以 SMTP 地址标识）→ Profile（封面信息/组织信息/计费码/优先级/重试/安全/通知等属性集，可服务多用户）。横向机制：Directories Integration 是"查目录找属性"的规则集（查询从 SMTP 地址开始）；Input Attributes 定位用户、Output Attributes 返回 Site 名/Profile 名/个人信息；Notification 三事件（新传真/外发成败/广播完成）三类型（Email/Printer/Folder）。
  conditions: 外部用户必须被 Lookup 表归到 Site+Profile 才能用系统（p198）
  tags: [structure, concept-model, site, profile, smtp-address]

- id: f07
  title: Queue & History 三视图结构（用户看自己、管理员看全部）
  type: structure
  source_pages: p25
  source_chapter: Key concepts / Queue and History
  source_quote: |
    "Outgoing Queue •Shows progress of faxes that are being sent. •Statuses: Preprocessing
    (converting documents and rendering coversheet), Delayed, Ready to Send, Sending, Waiting,
    Sent. •Faxes can be viewed (images and details) and cancelled." (p25)
  summary: |
    三个视图对用户与管理员都可用（权限不同）：①Outgoing Queue 外发队列——六状态 Preprocessing/Delayed/Ready to Send/Sending/Waiting/Sent，可查看图像与详情、可取消；②Outbound History 外发历史——Sent 或 Failed（取消/未达目的地等），可查看或重新提交；③Inbound History 入呼历史——Received 或 Failed to receive（页数不全），可查看、重路由、转发。排障与用户沟通按状态对号入座。
  conditions: 用户只见自己收发，管理员见全部
  tags: [structure, queue, history, status]

- id: f08
  title: 全局架构生态图——OTFC 与 OXE/邮件/客户端的协议关系
  type: diagram
  source_pages: p32-34
  source_chapter: Architecture / Ecosystem
  source_quote: |
    "OTFC is an independent application running besides the OXE ... T.30 ... SIP ... T.37 ... T.38
    G711 ... CSGD ... SMTP ... XML ... HTTP (S)" (p34)
  summary: |
    一张图定位所有接口：桌面用户三形态（email client 走 SMTP 经邮件服务器、web client 走 HTTP(S)、heavy client 走 SMTP/XML）；传真话路侧 OTFC 经 SIP/T.38（或 G711）连 OXE，OXE 再连 PSTN 上的模拟传真（T.30）；T.37 走局域网 MFP；CSGD 在 OXE 侧出现（书中未展开该缩写）；OTFC 本体可物理可虚拟（OTFC-V：虚拟化软件+Windows Server 上跑 OTFC 软件，p32）。理解点：OTFC 独立于 OXE 部署，传真流量与邮件流量分走两路。
  conditions: CSGD 缩写书中未定义；T.37 收发走 MFP
  tags: [diagram, architecture, ecosystem, protocols]

- id: f09
  title: 多网关多站点拓扑与双 SIP 网关号码分段路由
  type: structure
  source_pages: p35-37
  source_chapter: Multi Gateway - Multi Site infrastructure / PBX architecture / Architecture (routing scenarios)
  source_quote: |
    "2 SIP gateways are configured on Fax Center • Sip private Trunks on OXE are necessary to
    support fax connection ... Sip GW 1: OXE 1 = IP adress 1, Fax num 1200 to 1500 ; Sip GW 2:
    OXE 1 = IP adress 2, Fax num 3300 to 3800" (p36)
    "All outgoing faxes go through the same gateway, for example gateway GW1 • Outgoing faxes are
    routed to the gateway corresponding to the recipient number" (p37)
  summary: |
    三张拓扑图：①多网关多站点（p35）——多台 OXE 呼叫服务器经 WAN 互联，各 Site 可挂模拟传真，T38/SIP 混合；②PBX 架构（p36）——Fax Center 配 2 个 SIP 网关，OXE 侧必须建 SIP private trunk；出呼按号码路由到对应网关、入呼按被叫号码分给对应用户；示例口径：GW1 对 OXE1 IP 地址 1、传真号 1200-1500，GW2 对 OXE1 IP 地址 2、传真号 3300-3800（实验口径）；③路由场景（p37）——要么所有出呼走同一网关（如 GW1），要么按收件人号码分流到 GW2/GW3/GW4。
  conditions: OXE 侧 SIP private trunk 是硬前提；IP/号码段为实验口径示例
  tags: [structure, topology, multi-site, sip-gateway, routing]

- id: f10
  title: 部署形态与支持软件矩阵结构
  type: structure
  source_pages: p32, p38-41
  source_chapter: Architecture (Virtualized OTFC) / Recommended server resources / OTFC server / Supported software / Client Requirements
  source_quote: |
    "OTFC operating system •Microsoft Windows 64bits Servers 2022 / 2019/ 2016 (including IIS
    10.0) ... VMware ESXi •From 6.5 to 8.0 •vSphere •V-Motion •High availability •Terminal server
    •2019 •2022 •Citrix" (p39)
    "Supported mail servers • Microsoft Exchange 2019 / 2016 / 2013 • Microsoft Office 365 &
    Exchange online • SMTP-compliant mail servers. For Rasterizer module • Microsoft Office
    2021/ 2019 / 2016 (64-bit and 32-bit)" (p40)
  summary: |
    支持矩阵四块：①服务器 OS——Windows 64 位 Server 2022/2019/2016（含 IIS 10.0）；②虚拟化——Hyper-V（Server 2016/2019/2022 与 Hyper-V Server 对应版）、VMware ESXi 6.5-8.0（vSphere、v-Motion、高可用）、终端服务器 2019/2022、Citrix；③软件——邮件服务器 Exchange 2019/2016/2013、O365 与 Exchange online、任意 SMTP 兼容服务器；Rasterizer 模块需本机 Microsoft Office 2021/2019/2016（64/32 位）；④客户端——工作站 Windows 11/10、终端服务 Windows Terminal Server 2022/2019、邮件客户端 Outlook 2022/2019/2016（原文如此，Outlook 无 2022 版本，疑为原书笔误）、浏览器见 Feature List。每页都注明"以 OTFC Features List 为准"。
  conditions: 生产前必须查最新 Features List；p38 服务器资源推荐页正文缺数值（只有指针）
  tags: [structure, requirements, compatibility, matrix]

- id: f11
  title: 安装四步主线——准备服务器 → 软件安装 → FTW → 客户端安装/初始设置
  type: flow
  source_pages: p46, p50
  source_chapter: Installation step-by-step
  source_quote: |
    "Preparing the server Follow the requirement and prepare the server for OTFC installation →
    Software installation OTFC installation & global settings. First time wizard First site
    creation. → Clients installation SendFax, Print to mail, Coversheet editor … → Initial set-up
    OTFC basic configuration." (p46)
  summary: |
    全书交付主线四步：①准备服务器（按需求核配置、配网络网关 DNS、关防火墙、装 IIS 角色与服务、建服务账号）；②软件安装（装 OTFC 与全局设置、第三方组件、禁 MS SMTP）；③First Time Wizard（最小配置、建首站点）；④客户端安装与初始设置（SendFax/Print to mail/Coversheet editor，登录管理界面改密、预初始化 Office）。实验生态（p45）给全套锚点：fax.company.com 192.168.1.60、mail.company.com 192.168.1.100、eco.company.com 192.168.1.100（AD+DNS）、oxe.company.com 192.168.1.3、用户 allen@company.com 31604 / barkley@company.com 31600、传真管理员 baker@company.com（administrator / Alcatel1!@123，实验口径）。
  conditions: p45 生态图为实验口径；真实交付按客户 DNS/AD 规划
  tags: [flow, master-flow, installation, ecosystem]

- id: f12
  title: 服务器准备检查结构——网络/DNS 正反解、防火墙、IIS 角色服务、服务账号
  type: structure
  source_pages: p47-48
  source_chapter: Preparing the server
  source_quote: |
    "Server FQDN resolves to the server IP address in DNS • Reverse lookup of the server IP
    address in DNS returns the server FQDN • Server can reach and is reachable by external
    components" (p47)
    "Install • Latest Windows service pack and security updates • Web Server (IIS) role with role
    services: Windows Authentication; ISAPI Filters; ISAPI Extensions; IIS Metabase Compatibility
    ... Create a service account • ... Have a password that does not expire" (p48)
  summary: |
    准备清单两组：①网络（p47）——主机名与 IP、服务器与用户同域、FQDN 正向解析到 IP、IP 反向解析回 FQDN、与外部组件双向可达；②安装项（p48）——关本地与网络防火墙（实验口径，生产不适用）、最新 Windows 补丁、IIS 角色带 4 个角色服务（Windows Authentication、ISAPI Filters、ISAPI Extensions、IIS Metabase Compatibility）、装 Microsoft Office、建服务账号（域内可当服务账号、可查 LDAP 的域用户、对传真目的地网络文件夹读写、对网络打印机有打印权限、是传真服务器本地管理员、密码永不过期）。
  conditions: 关防火墙为实验口径；DNS 正反解依赖客户 DNS 服务
  tags: [structure, prerequisites, iis, service-account, dns]

- id: f13
  title: 软件安装流程——Setup.exe 向导到 FTW 启动 + 禁用 MS SMTP
  type: flow
  source_pages: p49, p59-65
  source_chapter: Software installation / Installation (How-To)
  source_quote: |
    "Define OTFC IP address: 192.168.1.60 ... System setup type • Create a new system ...
    Administrator account • Username: administrator • Password: 123456 • To change at the first
    login: Alcatel1!@123 ... Fax driver (T3.38) • SIP gateway • Fax hostname: fax" (p49)
    "Launch First Time Setup Wizard must be checked ... Disable Microsoft's SMTP service before
    starting the OpenTouch Fax Center SMTP gateway service." (p65)
  summary: |
    安装向导九步：发行介质根目录双击 Setup.exe → 选语言（该语言决定新 Profile 的默认邮件通知 Profile 与基本 Profile 封面语言）→ 接受许可 → 选目标文件夹 → 选 XM FAX IP 192.168.1.60（实验口径）→ 系统类型选 Create a new system（首装）→ 勾选要装的服务器组件（Fax manager/Driver/SMTP gateway…）→ 定传真网关主机名 fax 并选 SIP 协议 → 建系统管理员账号（默认名 administrator，密码 123456 仅为临时、首登强制改）→ Install → 选装全部第三方软件 → 勾"Launch First Time Setup Wizard"收尾。随后禁用 Microsoft SMTP 服务（OTFC SMTP 网关同样占用系统 25 端口，先停并禁用 MS SMTP，再启动 XMSMTPGateway 服务，其默认启动类型为 Automatic）。
  conditions: IP 192.168.1.60 与密码值为实验口径；安装语言影响后续默认通知与封页语言
  tags: [flow, installation, setup-wizard, smtp-conflict, menu-path]

- id: f14
  title: First Time Setup Wizard 十二项动作结构
  type: flow
  source_pages: p50, p67-70
  source_chapter: First time wizard / First Time Setup Wizard (How-To)
  source_quote: |
    "The Wizard performs the tasks listed below: • Creates a Site • Sets the Site QOS to 0/0/240
    • Sets the XML Poll folder to the Site Name • Removes SMTP Messages Require Authentication
    from default profile • Sets the CSID of the default profile to the Site name • Creates the
    User and sets its Password ..." (p67)
    "If you do not choose to use the Wizard, all these configurations can be managed from the Fax
    Administration interface. ... by executing the following file:
    [install_path]\Alcatel-Lucent Enterprise\FaxCenter\Bin\Util\FirstTimeSetup.exe" (p67)
  summary: |
    FTW 定位是"完成最小配置让你立刻能传真"，动作十二项：建 Site；Site QOS 设 0/0/240；XML Poll 文件夹设为站点名；从默认 Profile 移除"SMTP 消息要求认证"；默认 Profile 的 CSID 设为站点名；建用户并设密码；Site SMTP Postmaster 设为管理员 SMTP 地址；Site 路由表路由到该用户；System 路由表路由到该 Site（CSID=站点名）；告警通知经指定邮件中继发管理员 SMTP；设 SMTP 网关的 Mail Relay Server；产出摘要与使用说明并存盘。实验步骤（p68-70）：站点 My Organisation → 用户配置选 Internal Database → SMTP 配置（管理员邮箱 baker@company.com、邮件服务器 mail.company.com，实验口径）→ 首用户（p70 实验页写 baker@company.com/123456；p50 讲义页写 barkley@company.com——两页不一致，以实验口径记录）→ Proceed 后配置状态窗自动开关。跳过向导可事后手工配或运行 FirstTimeSetup.exe。
  conditions: 站点名/邮箱/密码为实验口径；QOS 0/0/240 为向导固定动作
  tags: [flow, ftw, wizard, minimal-config, menu-path]

- id: f15
  title: 管理双入口与认证体系——MMC Snap-in + Web admin，System/Site 两级管理员
  type: structure
  source_pages: p74-77
  source_chapter: OTFC administration applications / Authentication
  source_quote: |
    "MMC Snap-in application • Software installed with the Fax server. Can be also installed from
    client setup.exe wizard • Available in: C:\Program Files\Alcatel-Lucent Enterprise\FaxCenter\Client
    ... Web administration page • http://<ServerName_or_IP>/faxadmin or
    https://<ServerName>/faxadmin" (p74)
    "Authentication by: •SMTP Address •Windows authentication SSO and SAML ... Several
    administrators can be created •System administrator: global administration of the systems
    and sites. •Site administrator: manage only its own site" (p77)
  summary: |
    管理入口两个：MMC Snap-in（随服务器安装，也可从客户端 setup.exe 装，位于 FaxCenter\Client 目录，可建快捷方式）；Web 管理页（http://<服务器名或IP>/faxadmin 或 https://<服务器名>/faxadmin）。管理员认证方式：SMTP 地址，或 Windows 认证（SSO 与 SAML）。管理员分两级且可多个：System administrator 全局管系统与站点；Site administrator 只管自己的站点。推荐再建一个备份管理员（p110）。
  conditions: Web 管理页 URL 口径为实验名 fax 时即 http://fax/faxadmin
  tags: [structure, admin-interfaces, mmc, web-admin, authentication]

- id: f16
  title: Web Client 界面分区与访问口径
  type: structure
  source_pages: p79-81
  source_chapter: Web Client
  source_quote: |
    "To access: • Launch your Web browser • http://<ServerName_or_IP>/fax or
    https://<ServerName>/fax. User authentication is required" (p80)
    "Compose: to send fax ; Inbound history: faxes received ; Outboung: faxes sent ; Outgoing
    queue: Fax sent in transit ; Manage faxes & your contacts ; Inbox" (p81)
  summary: |
    Web Client 免安装、任意浏览器（Firefox/Safari/Chrome 等），支持 HTTP/HTTPS，符合美国康复法案 508 条款与欧洲 e-inclusion 无障碍要求；入口 http(s)://<服务器名或IP>/fax，需用户认证。界面六区：Compose（发传真）、Inbound history（收到的传真）、Outbound（已发，原文拼写 Outboung）、Outgoing queue（发送中）、Manage faxes & your contacts（传真与联系人管理）、Inbox。通知机制覆盖发送成败确认与来传真正达。
  conditions: 浏览器支持清单以 Feature List 为准
  tags: [structure, web-client, ui-zones]

- id: f17
  title: Windows 客户端四件套与部署方式
  type: structure
  source_pages: p83-90
  source_chapter: Windows Clients / SendFax / Web Fax Composer printer / Print to Mail
  source_quote: |
    "SendFAX • Web Fax Composer printer • Print to mail ; Silent installation & Installation by
    Massive Deployment through Group Policy are available ; User authentication •Windows account
    in the domain •Internal OTFC user account" (p83)
    "A reduced client applications set including only independent applications usable by most of
    the users (no administration tools) is available through the installation files located in
    the ClientRedistribution folder" (p84)
  summary: |
    四件套：①SendFAX——进阶用户的传真界面（实时预览、Outlook 模式、电话簿、封面、附件、传真选项、redact 涂黑工具；Outlook 模式经 Exchange 发送时要求 'FAX' 地址空间）；②Web Fax Composer printer——装后从任意 Windows 应用打印即经 Web Client 界面发传真；③Print to Mail——任意文档打印成 TIFF 交 Outlook，可作普通邮件或传真发出；④（管理端）MMC Snap-in 亦可由客户端安装包安装。部署支持静默安装与组策略（GPO）批量；认证用域 Windows 账号或 OTFC 内部账号；精简客户端集（无管理工具）在发行介质的 ClientRedistribution 文件夹。SendFAX 界面分区（p87）：手工寻址字段/收件人/缩略图/传真预览。
  conditions: SendFAX 寻址语法见 p163-164（ SMTP 集成章）
  tags: [structure, clients, sendfax, gpo, deployment]

- id: f18
  title: 封面页定制五步流程（Editor → 下载 → 另存 → 导入 → Profile 关联）
  type: flow
  source_pages: p91-96
  source_chapter: Coversheets / Coversheet customization
  source_quote: |
    "Create and modify coversheets (.cse) files (proprietary format) ... Available in 8 languages
    and 2 paper sizes" (p92)
    "Download the server coversheet to your desktop: •Log in the Fax MMC Snap-in. •Go to the Site
    Cover Sheets node. •Select an existing coversheet and save it on your PC" (p93)
    "Import the new coversheet using the web administration interface of fax server ... Assign
    the new coversheet in user Profiles. Several coversheets can be associated to a profile" (p95-96)
  summary: |
    五步闭环：①用 Coversheet Editor 起稿——从 FaxCenter\Client 启动，打开 Samples 目录或 DVD 上的既有封页（.cse 专有格式；编辑器含页面尺寸/分辨率/日期时间区域设置与 Tiff Viewer 旋转镜像注释功能，8 语言 2 纸张）；或②从服务器下载底稿——MMC Snap-in → Site Cover Sheets 节点选既有封页存到本机，双击启动编辑器；③修改后另存新名（如 new coversheet.cse）；④经 Web 管理界面导入新封页；⑤在用户 Profile 中关联（一个 Profile 可关联多个封页）。封页与电话簿一样"仅管理员管理、经 Profile 下发"（p128-129）。
  conditions: .cse 为专有格式；封面语言受安装语言影响（p59/p63）
  tags: [flow, coversheet, editor, menu-path]

- id: f19
  title: 用户双源模型与建户路径（Internal/AD 共存 + CSV）
  type: structure
  source_pages: p100-105
  source_chapter: Users / Internal users / Create a user / Import users .CSV / Export users
  source_quote: |
    "Internal Users: • User list is managed using the product administration tools ... Active
    Directory integration: • Requires a Windows Domain with Active Directory ... The NT Account
    property is used by windows account login (in the Web Client and SendFAX) to retrieve the
    user's SMTP address ... Note: The two type of user's directory can co-exist" (p100)
    "Sites ➤ Site ➤ Configuration ➤ Internal Users ... Users can be imported by the Webadmin
    interface only • .csv file format ... 3 Profile to apply" (p102, p104)
  summary: |
    两种用户源且可共存：①内部用户——OTFC 内建，属于 Site、有 Profile，手工建或从外部源静态导入，可导出 CSV；适合少量用户快速开通。②AD 集成——需 Windows 域，用户与管理员经 AD 用户和计算机管理；Windows 账号登录（Web Client 与 SendFAX）用 NT Account 属性反查用户 SMTP 地址；组织信息/电话号码/时区也可在 Profile 级设置。手工建户路径：Sites ➤ Site ➤ Configuration ➤ Internal Users → Create → 邮箱地址、Profile（传真选项/安全/封面…）、密码（首登必改）、个人信息、电话号码、传真号；时区写入传真报头并影响封页/报头/邮件通知时间戳（可在 Profile 管）。CSV 导入与用户清单导出都只能经 Webadmin 完成，导入时选要套用的 Profile。
  conditions: CSV 仅 Webadmin；AD 登录依赖 NT Account 属性
  tags: [structure, users, internal, active-directory, csv, menu-path]

- id: f20
  title: 管理员两级结构与账号生命周期（建 System/Site 管理员、改密、登录界面区分）
  type: structure
  source_pages: p106-113
  source_chapter: Administrators / System administrators / Site administrators / Create new SYSTEM administrator / Administrator Login
  source_quote: |
    "There are two types of administrators: SYSTEM Administrators ; SITE Administrators" (p107)
    "Create new SYSTEM administrator It is recommended to create a backup administrator •
    Authentication based on internal server, AD and SAML" (p110)
  summary: |
    管理员两类：System administrator 管整个系统、可设多个；Site administrator 只有权配置自己的站点（如 My Organization）。建 System 管理员三步（p110），认证基于内部服务器、AD 与 SAML，官方推荐建一个备份管理员防锁死；建 Site 管理员四步（p111）；改密码三步（p112）；登录界面区分 System/Site 两栏（p113）。与 f15 呼应：管理员可用 SMTP 地址或 Windows 认证（SSO/SAML）登录。
  conditions: 备份管理员为官方建议动作；实验口径 backupadmin/Alcatel1!@123（p115）
  tags: [structure, administrators, system, site, backup-admin]

- id: f21
  title: Profile 属性块与五种关联机制（限制组/呼号限制/邮件通知/电话簿/封页）
  type: structure
  source_pages: p118-129
  source_chapter: User Profiles（含 Restriction group / Calling Number Restriction / Security / Mail Notification profiles / Phone books / Coversheets）
  source_quote: |
    "By default, the Basic and No Faxing Rights profiles are available: • The Basic profile
    allows the user to fax at a normal fax priority. • The No Faxing Rights profile does not
    allow the transmission of faxes. •Profile information ... •Cover Sheets ... •Billing Codes
    ... •Fax Options (priority, retries, resolution and other options) •Security (options,
    override policy and number restrictions) •Notification settings" (p118)
    "Sites ➤ Site ➤ Configuration ➤ Profile ... A barring table could be linked to one/several
    user profile(s) • E.g. National only: International numbers are forbidden" (p120-121)
  summary: |
    Profile 六块属性（p118）：Profile information（名称/组织/电话号码信息）、Cover Sheets（默认与允许封页）、Billing Codes（发送方/接收方/系统计费码）、Fax Options（优先级/重试/分辨率等）、Security（选项/覆盖策略/号码限制）、Notification 设置。默认两档：Basic（正常优先级可发）与 No Faxing Rights（禁发）。五种挂接：①Restriction group（p121）——拦截表挂一/多个 Profile（例 National only 禁国际号），路径 Sites ➤ Site ➤ Configuration ➤ Profile 关联；②站点级 Calling Number Restriction（p122）——Sites ➤ General Settings ➤ Calling Number restrictions 直接拒来话（call setup 阶段拒接）；③Mail Notification Profile（p124-127）——每语言一份，经 Profile 关联到用户，Exchange 场景勾 "Exchange integration"+正文 Text（只影响邮件通知不影响 Web 访问）；④Public 电话簿（p128）经 Profile 下发、仅管理员管理；⑤封页（p129）经 Profile 下发、仅管理员管理。
  conditions: Restriction group 与 OXE 语音侧闭锁是两套体系
  tags: [structure, profile, restriction, notification, phonebook, menu-path]

- id: f22
  title: 电话簿体系与 LDAP 访问链（Public/Personal、CSV、属性映射）
  type: structure
  source_pages: p134-139
  source_chapter: Phone Books / Overview / Corporate phone books / Import contacts / LDAP Access
  source_quote: |
    "There are two types of Phone Books: • Public (corporate): assigned to users through their
    profile • Personal (private): accessible and manageable only by each user ... You can import
    an external contact list to a Phone Book by using a CSV file ... The OpenTouch Fax Center
    Phone Books can be accessed through LDAP connection" (p135)
    "the Enable LDAP Access box must be checked in the System Configuration ➤ Fax Archive
    properties of your host ... You can set the Authentication in Configuration ➤ General
    Settings properties of the site ; LDAP Attribute Mapping • To match attributes between OTFC
    and LDAP server" (p138-139)
  summary: |
    电话簿两类：Public（企业级）经用户 Profile 分配、仅管理员管理，Webadmin 里可建多本并可把联系人分组；Personal（私人）仅用户本人可见可管。联系人可经 CSV 从外部源导入。LDAP 访问三处配置：①主机级开关——System Configuration ➤ Fax Archive 属性勾 Enable LDAP Access；②站点级认证——Configuration ➤ General Settings 里设 Authentication；③LDAP Attribute Mapping 匹配 OTFC 与 LDAP 服务器属性。
  conditions: LDAP 环境由客户提供；属性映射需按客户目录实勘
  tags: [structure, phonebook, ldap, csv, menu-path]

- id: f23
  title: OTFC 侧 SIP 配置与 OXE 声明路径（含空间冗余双呼叫服务器）
  type: menu-path
  source_pages: p141-146
  source_chapter: OmniPCX Enterprise & OTFC / SIP configuration / OmniPCX Enterprise declaration
  source_quote: |
    "SIP configuration • Local SIP UDP port: 5360 • Activate SIP message in log files (for
    maintenance) • SIP authentication" (p142)
    "Configure dial plan for outgoing calls: • In case of mono PBX (default configuration), all
    calls (*) are routed to this PBX." (p144)
    "OmniPCX Enterprise with spatial redundancy • In Driver/Peer List • Declare the 2 call
    servers: IP addresses or FQDN (if managed in DNS server) ... In Driver/Dial Plan • For the
    number pattern concerned, specify the 2 call servers declared previously with a priority
    order" (p145-146)
  source_chapter_note: SIP 互通全流程参照 TC3048（p141）
  summary: |
    OTFC 侧三处配置：①SIP 基础——本地 SIP UDP 端口 5360、为维护激活 SIP 消息日志、SIP 认证；②OXE 声明——安装时声明的 PBX 可修改、可再声明更多 OXE；③Dial plan——单 PBX 默认所有号码（*）路由到该 PBX。空间冗余两步：Driver/Peer List 声明 2 台呼叫服务器（IP 或 FQDN，若由 DNS 管理）→ Driver/Dial Plan 对相关号码模式指定两台服务器并排优先级。维护抓包命令见 f25。
  conditions: OXE 侧配置为另一半（f24）；细节参照 TC3048
  tags: [menu-path, sip, dial-plan, redundancy, otfc-side]

- id: f24
  title: OXE 侧 SIP 网关 MGR 菜单七步序列
  type: menu-path
  source_pages: p151-155
  source_chapter: OXE SIP gateway configuration (How-To)
  source_quote: |
    "Configure a SIP gateway on OXE side to connect to the Fax server. Use MGR or Omnivista 8770
    to manage. mtcl is the default login & password ... login: mtcl Password: mtcl … (101)csa> mgr"
    (p152)
    "• Select mgr / Trunk groups/ Create ... mgr / SIP / SIP gateway ... mgr / SIP / Proxy ...
    mgr / SIP / Trusted IP addresses/ Create ... mgr / SIP / SIP Ext gateway/ Create ...
    mgr / Translator / Network Routing Table/ 5 ... OXE users directory numbers #31600 to 31699 •
    Select mgr / Translator / Prefix plan/ Create" (p152-155)
  summary: |
    七步菜单序列（How-To 实验 6）：①mgr / Trunk groups / Create（建 SIP 中继组）；②mgr / SIP / SIP gateway（网关参数）；③mgr / SIP / Proxy；④mgr / SIP / Trusted IP addresses / Create（信任 OTFC 地址）；⑤mgr / SIP / SIP Ext gateway / Create；⑥mgr / Translator / Network Routing Table / 5（路由表）；⑦mgr / Translator / Prefix plan / Create（前缀计划，实验口径把 OXE 用户目录号 #31600-31699 指向传真网关）。登录：终端窗口 mtcl/mtcl（默认账号密码，实验/默认口径）进入 csa 后敲 mgr；也可用 OmniVista 8770 管理。高级参数一律参照 TC3048。
  conditions: mtcl/mtcl 为 OXE 默认账号（实验/默认口径，生产必改）；菜单截图细节以书为准
  tags: [menu-path, oxe, mgr, sip-gateway, lab]

- id: f25
  title: OXE 侧传真故障抓包三法（CHtrace/motortrace/tcpdump→Wireshark）
  type: flow
  source_pages: p148-150
  source_chapter: Maintenance
  source_quote: |
    "To capture the Call Handling traces on OXE Call Server: • Using a terminal window, under
    mtcl account, tape the following commands to generate log rotate files called 'CHtrace-XX':
    • tuner km • tuner clear-traces • tuner +cpu +cpl +at hybrid=on • actdbg all=off sip=on
    abcf=on • mtracer -ag -d -1 /DHS3dyn/tmp/CHtrace -s 1000000 -f 90" (p148)
    "tcpdump –s 2000 –w /tmp/oxetrace.pcap ... Use 'bin' as transfer mode • Open the file with
    Wireshark" (p150)
  summary: |
    三类抓包均在 OXE 呼叫服务器终端窗口以 mtcl 账号执行：①呼叫处理 trace（CHtrace-XX 滚动日志）——tuner km → tuner clear-traces → tuner +cpu +cpl +at hybrid=on → actdbg all=off sip=on abcf=on → mtracer -ag -d -1 /DHS3dyn/tmp/CHtrace -s 1000000 -f 90；停止用 Control C 或 killall mtracer；②SIP trace（motortrace-XX）——motortrace 3 → traced -d -1 /DHS3dyn/tmp/motortrace -s 1000000 -f 90；停止 Control C 或 killall traced；③网络抓包——tcpdump –s 2000 –w /tmp/oxetrace.pcap，停止 Control C，用 FTP 以 bin 传输模式取回 PC，Wireshark 打开（可按 SIP 过滤）。
  conditions: 路径 /DHS3dyn/tmp、/tmp 为 OXE 侧约定路径；抓包属只读排障动作
  tags: [flow, maintenance, traces, tcpdump, wireshark, oxe]

- id: f26
  title: SMTP 网关收发事务与中继拓扑结构
  type: structure
  source_pages: p157-163
  source_chapter: SMTP integration（Overview / Sending & Receiving / Typical Deployment / Outbound / Inbound）
  source_quote: |
    "The XMSmtpGateway module, called SMTP Gateway, has the two usual basic functions of a mail
    server, allowing the Fax Server to: • Receive emails from OTFC users in order to convert them
    into faxes. • Send emails to OTFC users for notification purpose" (p157)
    "A feedback address must be filled in the SMTP Gateway settings to enable reply from the
    gateway with a mail header (mail header can't be empty!). ... Receive NDR (Non-Delivery
    Report) messages in case the mail server would not be able to deliver some notifications" (p161)
  summary: |
    结构三层：①模块职责（p157-158）——收用户邮件转成传真、发通知邮件（含收到的传真与发送报告）；任意邮件服务器可用，Exchange 有增强特性；SMTP connector 是许可特性；强烈建议把网关接到真实邮件服务器上。②典型部署（p159-160）——用户邮箱服务器与 OTFC 通知中继可以是同一台；外发时邮件可直达 SMTP 网关或经邮件服务器中转，中转带来队列管理（挂起/转向/并发控制）、客户端-服务器集成（Outlook 表单）、垃圾过滤、病毒检查四大好处。③内收（p161-162）——传真可作 PDF/TIFF 附件或 HTML/Text 正文发到邮箱；网关设置里必须填 feedback address（邮件头不能为空）；经客户 LAN 中继可消除外部服务器时延影响并接收 NDR。寻址（p163）：31600@<传真服务器 FQDN>，或 [FAX:0298131600]，有 Outlook 联系人时直接选联系人。
  conditions: 端口 25 与许可特性见 n 类条目
  tags: [structure, smtp, relay, notification, addressing]

- id: f27
  title: Exchange 'FAX' 地址空间集成与连接器流程
  type: flow
  source_pages: p164-170
  source_chapter: Microsoft Exchange Integration / Creating an SMTP Send-Connector of Type "FAX" / Allowing Reception of Mail Notification Messages
  source_quote: |
    "Create a new send connector. • Associate the 'FAX' address space to this Connector and
    forward all mails to a smart host which corresponds to the fax server's SMTP Gateway. •
    Optionally, you can also associate a fax subdomain to this connector in the SMTP address
    space ... [FAX:5141234567] • [FAX:John Smith@5141234567] •
    [FAX:/fn=John/ln=Smith/jobtitle=Manager@5141234567]" (p164)
    "New-SendConnector -Name <ConnectorName> -AddressSpace \"fax:*;1\" –SmartHosts
    \"<SMTPGateway>\" –DNSRoutingEnabled $false -SourceTransportServers
    \"<HubTransportServers>\"" (p167)
  summary: |
    四段流程：①理解（p164）——Exchange 集成带来 Outlook 传真联系人、SendFAX Outlook/Exchange 模式必需、富文本与自定义 Outlook 表单属性传输；'FAX' 地址空间做法是建 Send Connector 关联 fax:* 并把邮件转发到智能主机（=传真服务器 SMTP 网关），可选再挂传真子域；寻址用法 [FAX:号码]、[FAX:姓名@号码]、[FAX:/fn=/ln=/jobtitle=@号码]，或 5141234567@fax.<域名>、5141234567/fn=John/ln=Smith/co=Ac…；②建连接器（p165-167）——Exchange Management Shell 执行 New-SendConnector（参数模板与示例见 p31 数值条目），SEND connector 出现在组织的 Hub transport 列表；③核验（p168-169）——Exchange admin center → Mail flow → Send Connectors 页签出现新连接器，双击可编辑属性；④放行通知（p170）——Exchange 收件安全过高会拦掉 OTFC 网关的全部通知，需调 Hub Transport 节点下 Receive Connector 属性。
  conditions: SMTP connector 为许可特性；示例值 fax.company.com/eco.company.com 为实验口径
  tags: [flow, exchange, send-connector, fax-address-space, menu-path]

- id: f28
  title: 服务架构三层模型与 Stateful/Stateless 分类
  type: structure
  source_pages: p177-185
  source_chapter: Services OTFC（Service Oriented Architecture / Fax Manager Module / Fax Driver Module / Rasterizer Module / SMTP Gateway / Services Interactions）
  source_quote: |
    "Components are grouped into services for convenience. Facilitates provisioning and
    maintenance. Services are deployed on a dedicated server. Services are Windows services (i.e.
    manageable from the services snap-in)" (p177)
    "Stateful (Replicated) Services/Components • XMFaxManager • XMConfigManager • XMCoConfig •
    XMFaxArchive • XMFaultTolerance ; Stateless (Load Balanced) Services/Components • XMFaxDriver
    • XMDocumentRasterizer • XMSmtpGateway • XMXmlGateway ... Non-replicated components are
    workers" (p179)
  summary: |
    三层模型：模块（安装单元）→ 服务（Windows 服务，可经服务管理单元管理）→ 组件（执行具体任务，经管理界面 Services Status 监控）。四大模块：①Fax Manager Module（系统心脏）含 XMFaxManager（管收发队列、分发任务、管媒体文件库）、XMCoConfig（管全部站点配置）、XMConfigManager（管全部系统配置）、XMFaxArchive（存取传真详情记录）、XMFaultTolerance（监控故障与监督故障切换）；②Fax Driver Module（XMFaxDriver）用 H.323/SIP（T.38/G.711）收发、可并行多路呼叫；③Rasterizer Module（XMDocumentRasterizer）借本机原生应用与专用转换器把文档转 TIFF；④SMTP Gateway（XMSMTPGateway）监听 25 收作业发通知、不能与其他 SMTP 服务器共存。分类：有状态（复制，持有配置/未决事务/历史）5 个，无状态（负载均衡的工人）4 个（含 XMXmlGateway）。p184-185 两张交互图给出组件间与全局视图。
  conditions: XMFaultTolerance 只作组件介绍，故障切换部署全书未教
  tags: [structure, soa, services, stateful, stateless]

- id: f29
  title: 服务管理三通道与日志体系
  type: structure
  source_pages: p186-191
  source_chapter: Services status / Start, stop Services / Managing the services / Log files
  source_quote: |
    "Services status checking • Using the web administrator interface or MMC snap-in • System
    Monitor/Services Status tab" (p186)
    "All these commands can be executed from the <install_path>\FaxCenter\Bin\Util folder. •
    Restarting Services ... xmsc –ra • Stopping Services ... xmsc –oa • Starting Services ...
    xmsc -aa ... Each OTFC component has a dedicated log file. Log files location: • C:\Program
    Files\Alcatel-Lucent Enterprise\FaxCenter\Trace" (p188-189)
  summary: |
    服务管理三通道：①查状态——Web 管理界面或 MMC Snap-in 的 System Monitor/Services Status；②启停——Windows 服务菜单；③命令行（Bin\Util 目录）——xmsc -ra 重启全部、xmsc -oa 停止全部、xmsc -aa 启动全部。日志体系：每个组件一个专属日志，统一在 FaxCenter\Trace 目录；SIP 日志两步用法（p190-191）——先在管理界面激活"日志中记录 SIP 消息"（三步），再按需调日志级别控制信息量。
  conditions: 日志大小/保留默认值见数值条目；SIP 日志激活入口在管理界面
  tags: [structure, services, xmsc, logs, menu-path]

- id: f30
  title: 目录集成机制链——LDAP 声明 → Lookup 表 → NT Account 免密 → IIS 自动登录
  type: flow
  source_pages: p194-204
  source_chapter: Advanced configuration（External directories / LDAP Server / Site & Profile Lookup tables / NT Account Lookup / Automatic NT Log-in）
  source_quote: |
    "Whether the system needs to assign a fax to a user (inbound faxing) or retrieve a user's
    Personal Information to send a fax (outbound faxing) ... the system will always begin its
    queries with the user's SMTP Address." (p194)
    "A user who is not associated to any existing Site and any existing Profile is not allowed to
    use OTFC. Through these lookup tables it is possible to grant the faxing rights to some
    users" (p198)
  summary: |
    四段机制链：①目录声明（p194-197）——OTFC 自带内部目录（新装默认只用它），可加 AD 或任意 LDAP；声明参数（enabled、服务器地址、端口 389、Search base 树起点、测试连接），连接丢失会产生 SNMP trap，Attributes 页签做 OTFC-LDAP 属性映射；②Lookup 表（p198-200）——外部用户必须有 Site+Profile 才能用系统，Site Lookup 与 Profile Lookup 都是"基于目录属性的 if 规则"，Profile 默认规则是"用用户设置里指定的 Profile"，可加按任意字段（邮箱/传真号/职务…）过滤的规则；③NT Account Lookup（p201-203）——两条路：用 AD NT Account Lookup 专用接口，或在 LDAP 目录集成里配特定 Search Filter（samAccountName 匹配 NT 账号名）并在 Conditions 页签加条件，实现客户端应用免认证登录；④Web 自动登录（p204）——需 IIS 配置（Default Web Site → Authentication：禁用匿名、启用 Windows Authentication）且 OTFC 服务器必须是域成员。
  conditions: 查询恒从 SMTP 地址开始；NT Account 场景先由 NT 账号解析 SMTP 地址
  tags: [flow, ldap, lookup, nt-account, iis, menu-path]

- id: f31
  title: 入局路由三层与号码规整机制（Incoming Routing/DTMF/Modification/Accounting）
  type: structure
  source_pages: p205-213
  source_chapter: Advanced configuration（Incoming Routing Table / DTMF / Modification Table / Accounting of fax calls）
  source_quote: |
    "The routing can be done by a multiple combination of routing rules: •Direct rules •Directory
    Lookup rules •Default rule that applies a default routing to misrouted faxes (faxes that
    failed all the rules of the table). Routing rules can be ordered in the Incoming Routing
    Table (except the Default rule, that remains the last)" (p205)
    "Configure the « Directories Lookup » to match with DDI fax numbers ... Replace the default
    value by $did:?????$" (p207)
  summary: |
    四个机制：①Incoming Routing Table（p205-208）——把来传真 DDI 号匹配到内部用户库或外部目录；规则三类（Direct 规则、Directory Lookup 规则、Default 兜底规则恒排最后），可排序；示例流程：PSTN 呼 0123431500 → OXE 收到 123431500 → 传真服务器侧 31500 → 查目录 owner（内部库或 LDAP 里 barkley@company.com，传真号 33123431500）→ 投递；Directories Lookup 的匹配值配 $did:?????$；来话邮件通知故障查 ConfigManager.log 与 Smtp.log；②DTMF 路由（p209）——收发双方可加 DTMF 补拨分机，出呼语法 +33155667000 P 1234（P=暂停），可激活默认语音提示"请输入 4 位分机"；③Modification Table（p210-211）——改用户从目录/联系人带来的号码（例：超过 6 位且 33 开头的外部号把前两位 33 换成 00，即 ARS 前缀+国内前缀）；④Accounting（p212-213）——外发传真在 OXE 生成计费票，OmniVista 8770 取票出报表，票可映射到用户电话号或传真号（默认传真号）。
  conditions: 示例号码为实验口径；DDI/ARS 书中未展开全称
  tags: [structure, routing, ddi, dtmf, modification-table, accounting]

- id: f32
  title: 备份/恢复/升级流程骨架（三数据域、五步升级法）
  type: flow
  source_pages: p216-222
  source_chapter: Maintenance（Backup / Backup - Data / Backup process / Restore / Upgrade）
  source_quote: |
    "Backup the System and all faxes: • On a periodic basis • Before any upgrade of XM Fax ...
    Backups cannot be performed live, so it is suggested to perform them in a maintenance window
    (downtime). All fax server services (including MySQL) must be stopped (not killed) before
    backing up." (p216)
    "1.Make sure the system is sane 2.Stop traffic 3.Stop services 4.Backup the data 5.Upgrade
    the system" (p222)
  summary: |
    备份三前提与三数据域：备份要周期性做、升级前必做、不能热备（维护窗口停机，全部服务含 MySQL 必须"停止"而非 kill）。数据三域（p217）——配置与状态（站点/用户/Profile/管理员/服务设置/修改表等+组件状态与收发中传真；存于注册表、Config 与 Data 文件夹、MySQL）；传真元数据（MySQL 库）；传真图像与文档（MediaStore，Data\MediaStore）。备份动作（p218）：xmsc -oa 停服 → 拷 Data/Bin/Config → 拷 MySQL 数据目录 → regedit 导出注册表键 → 重启；用户私人电话本单独备份（p219）。恢复（p220）：环境须与备份时相似（版本等同/拓扑一致/路径一致），服务停止（此时可 kill），先擦除现有数据再回灌。升级（p221-222）：直接跑新版安装程序；推荐五步（确认健康→停流量→停服务→备份→升级）；升级会改写状态文件与 Web 包，自定义内容要善后。
  conditions: 备份/恢复/升级的具体陷阱见 counter-example 条目
  tags: [flow, backup, restore, upgrade, maintenance-window]

- id: f33
  title: 报表与监控体系（31 报表 + BIRT + SNMP V2 + 删除策略）
  type: structure
  source_pages: p223-229
  source_chapter: Maintenance（Fax deletion policy / Logs / Reports / Monitoring）
  source_quote: |
    "There are two types of fax elements that can be deleted, either separately or together: •
    The fax records ... including all fax information (metadata) and excluding the fax documents
    (image files) • The fax documents, corresponding to the fax image files stored in the
    Mediastore folder" (p223)
    "31 reports are available •These reports can include numeric values and graphic
    representations ... SNMP V2 Services • Component status changes •Incoming queue reaches max
    size •Site outbound quota reaches maximum size •Rasterization failure •Routing failure ..." (p226, p228)
  summary: |
    四块运维面：①传真删除策略（p223-224）——传真记录（归档库条目，元数据）与传真文档（Mediastore 图像文件）可分开或一起删，支持配置零保留（合规）；②报表（p226-227）——31 个模板（全系统/单用户、月/周/日、模块错误摘要），数值+图形，可用 BIRT 报表设计器自定义（安装包 3rd\birt 下的 zip 解压安装）；③监控（p228-229）——站点级与系统级看路由/来话/去话/排队/错误/传真属性（错误信息/传输信息/时间与大小）；SNMP V2 trap 覆盖组件状态变化、入队满、站点出呼配额满、光栅化失败、路由失败、XML 读取错误、驱动发送错误、分区检测、通道初始化失败、主机监视 trap（性能计数器/组件状态表/通道状态/远程心跳）。
  conditions: BIRT 定制细节在书外；SNMP 网管平台由客户环境提供
  tags: [structure, reports, birt, snmp, deletion-policy, monitoring]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-24）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 评估 OTFC 方案能力与规模上限 | 有 | f02, f03 | 能力三清单 + 收发入口矩阵（容量/速率数值在数值类文件） |
| task-02 | 规划部署架构 | 有 | f08, f09, f10 | 生态协议图、多网关多站点与双网关分段、部署形态与支持矩阵 |
| task-03 | 准备传真服务器宿主 | 有 | f11, f12 | 四步主线的第一步 + 准备清单结构（DNS/防火墙/IIS/服务账号） |
| task-04 | 安装 OTFC 软件 | 有 | f13 | Setup 向导九步 + 禁 MS SMTP |
| task-05 | 跑 First Time Setup Wizard | 有 | f14 | FTW 十二项动作结构与实验步骤 |
| task-06 | 处理许可 | 部分 | — | 许可为数值/规则类（默认许可边界、MAC 口径），在 principle.md，无独立框架结构 |
| task-07 | 创建与管理用户 | 有 | f19 | 双源模型、建户路径、CSV 导入导出 |
| task-08 | 创建 System/Site 管理员 | 有 | f15, f20 | 管理双入口认证 + 两级管理员与账号生命周期 |
| task-09 | 安装并测试客户端 | 有 | f16, f17 | Web Client 分区 + Windows 四件套与 GPO 部署 |
| task-10 | 定制封页 | 有 | f18 | 五步流程 |
| task-11 | 设计与管理用户 Profile | 有 | f21 | Profile 六块与五种挂接机制 |
| task-12 | 管理电话簿 | 有 | f22 | 两类电话簿 + LDAP 访问链 |
| task-13 | 配置 OTFC 侧 SIP 与 OXE 声明 | 有 | f23 | SIP 5360/dial plan/空间冗余路径 |
| task-14 | 配置 OXE 侧 SIP 网关 | 有 | f24 | MGR 七步菜单序列 |
| task-15 | OXE 侧传真故障抓包 | 有 | f25 | 三类抓包流程 |
| task-16 | 集成邮件系统 | 有 | f26, f27 | SMTP 网关事务拓扑 + Exchange FAX 地址空间连接器流程 |
| task-17 | 认知与运维服务架构 | 有 | f28, f29 | 三层模型与分类 + 三通道管理与日志 |
| task-18 | 集成外部目录与高级路由 | 有 | f30, f31 | 目录机制链 + 路由三层与号码规整 |
| task-19 | 配置传真计费 | 有 | f31 | Accounting 机制（第④块） |
| task-20 | 备份与恢复系统 | 有 | f32 | 备份三数据域与恢复骨架 |
| task-21 | 升级系统 | 有 | f32 | 五步升级法 |
| task-22 | 配置传真删除策略 | 有 | f33 | 记录/图像分开删 |
| task-23 | 报表与监控 | 有 | f33 | 31 报表/BIRT/SNMP |
| task-24 | 按日志定位通知/路由故障 | 有 | f29, f31 | 日志体系 + ConfigManager.log/Smtp.log 指针 |

补充说明：
- f01（课程推进）与 f04（收发图示）、f05（组件流程）为 BOOK_OVERVIEW 骨架 1-3 的框架底座，不单对某 task。
- task-06 许可无结构性内容（两页：边界清单+导入按钮），归数值/规则类提取。
- 全部 24 项 task 均有框架类条目覆盖（task-06 除外，已注明归属），无缺口。
- 生产化边界提示：OXE 侧互通细节指向 TC3048；端口全表/浏览器支持/45 格式清单指向 OTFC Features List；f12 关防火墙与 f24 mtcl 默认账号均为实验/默认口径。
