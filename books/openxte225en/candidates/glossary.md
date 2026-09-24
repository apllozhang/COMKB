# 术语/缩写/产品名候选 — OpenTouch Mobility & Remote Worker (OPENXTE225EN R2.6 Issue 10)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 62 条（概念 16 / 角色 2 / 许可 3 / 产品 21 / 协议 9 / 资源 11；任务要求全量提取，OTC 客户端家族按产品形态单列，手机版发布说明与 OTSBC 文档各并为一词）。DISA/UTL 型未展开缩写（如 CTL/CAC/DISA/DCS）书中未给全称，full_name 字段如实省略，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: OpenTouch Suite for MLE
  category: concept
  source_pages: p1, p3, p31, p33
  source_quote: |
    "OPENTOUCH - R2.6 MOBILITY & REMOTE WORKER - ISSUE 10" (p1)
    "OpenTouch Suite for MLE — Infrastructure for remote users access" (p31)
  definition: |
    ALE 面向中大型企业（MLE）的通信套件，本书主角：OTMS 管理服务器 + OXE 呼叫服务器 + OmniVista 8770
    管理工具的组合。本书主题是为其增加"远程工作者与移动接入"能力（R2.6 / Issue 10 版本坐标）。
  alias_or_related: 全书行文多简称 "OpenTouch"；承载虚机见 g25 OTMS
  tags: [concept, platform, core]

- id: g02
  term: Remote worker / Remote access
  category: concept
  source_pages: p33-34, p147
  source_quote: |
    "The remote users can be: Employees of the company or External guests (invited into a multi-party
    conference with web collaboration)" (p33)
    "Step 1: configuration of remote access … Step 2: routing configuration" (p147)
  definition: |
    本书的服务对象与目标状态：员工从互联网全功能接入（远程工作者），外部来宾仅限会议/Web 协作；客户端
    侧落地为"接入配置 + 路由档案"两步。配套参考文档族以 TC2639（Remote Worker/Mobility Configuration
    Update）为总纲。
  alias_or_related: 三类需求原文（p34）；对照 g18 External guest
  tags: [concept, remote-worker, core]

- id: g03
  term: Conversation user
  category: concept
  source_pages: p114, p177, p213
  source_quote: |
    "With a Conversation user, SIP communication is done with OpenTouch SIP server" (p114)
    "Look for 'OpenTouch'; Select 'OpenTouch Conversation'" (p213, Android 商店名)
  definition: |
    Connection/Conversation 二分之一：SIP 通信走 OpenTouch SIP 服务器的用户（中心化注册）。Android 应用
    名即 OpenTouch Conversation。OTSBC 向导里对应 OTCV 参数组（域=OTSBC 公共 FQDN）。
  alias_or_related: 对照 g04 Connection user；OTCV/OTCV Web 参数组（p104-105）
  tags: [concept, user-type, sip]

- id: g04
  term: Connection user
  category: concept
  source_pages: p114, p189, p201
  source_quote: |
    "for a Connection user it is with OXE SIP server" (p114)
    "OTC smartphone for Connection users: Declare and configure OTC smartphone for a Connection user" (p189)
  definition: |
    二分之二：SIP 通信走 OXE SIP 服务器的用户；智能手机移动化（本书 How-To 主体）全部按 Connection 用户
    展开。OTSBC 向导里对应 OTCT 参数组（域同 OTCV）。
  alias_or_related: 对照 g03；自 OpenTouch 2.2 起同一客户端两种行为（p114）
  tags: [concept, user-type, sip]

- id: g05
  term: Multi-devices
  category: concept
  source_pages: p151-152, p156
  source_quote: |
    "Multi-devices operation brings a second way for users to use their OTC PC application as a client to
    phone. It's the possibility to associate a SIP extension as a secondary device to the user." (p152)
  definition: |
    OTC PC 远程办公新法（与 Nomadic 并存）：把一个 SIP 分机（实验口径 213100x）绑为用户副设备，主话机
    保留；管理同"OTC PC 软话机模式"。前提：COS 的 Ring all Secondary if Main Out of Service + 两个功能
    前缀并在用户 COS 授权。
  alias_or_related: 对照 g06 Nomadic；前提清单见 principle p22
  tags: [concept, multi-devices, otc-pc]

- id: g06
  term: Nomadic / Nomadic SIP
  category: concept
  source_pages: p151-152, p157-158, p67
  source_quote: |
    "The previous way is still always possible, and is, based on the Nomadic feature with Nomadic SIP. In
    this case, if the user selects computer as current device, the main set (NOE device and not a SIP
    extension) is frozen and calls are no more routed to the main" (p152)
  definition: |
    游牧模式（老法仍在用）：用户把当前话机从 Deskphone 切到 Personal Computer 后主设备冻结，SIP 软话机
    顶替；每条并发连接占 1 个 SIP 设备 + 1 个 Ghost Z（池化、退出才释放）。DAS 规则里 s/^\+N/N/ 等即为其
    号码变换（N=Nomadic）。
  alias_or_related: 资源公式见 principle p23；对照 g05 Multi-devices
  tags: [concept, nomadic, pooling]

- id: g07
  term: Ghost Z set
  category: concept
  source_pages: p158-159, p194-195
  source_quote: |
    "Ghost Z: Enable the ghost Z feature; Ghost Z feature: Select 'Nomadic'" (p158)
    "One Ghost Z device is required to use the remote extension. Therefore, a pool of ghost Z devices
    dedicated to 'remote extension' use must be created." (p194)
  definition: |
    虚拟 Z 设备（Set Type=Analog + Ghost Z 特性）：把本打给内部设备的呼叫重定向到游牧软话机（特性选
    Nomadic）或远程分机（特性选 Remote Extension）。编号可用 B<数字> 格式避免占用真实号码（实验口径
    B31091）。OXE 侧建、OT 侧经 OXE Resources 申报号段。
  alias_or_related: 两种特性用途（Nomadic / Remote Extension）；模板文件下载另一处 p181 "Pool of ghost Z
    for remote extension"
  tags: [concept, ghost-z, virtual-device]

- id: g08
  term: Remote Extension (RE / REX)
  category: concept
  source_pages: p178-182, p192, p204
  source_quote: |
    "Remote extension DISA prefix … 31280" (p192)
    "from release 2.6 of OpenTouch, the main device can be directly the remote extension" (p204)
    "Automatic REX creation / Automatic REX association" (p179)
  definition: |
    远程分机：经 DISA 公共号码把呼叫引到手机的设备形态；与主话机构成 tandem，配速拨号做自动替代、配判别
    器+ARS 做双模式第二跳。R2.6 起可直接做用户唯一设备。书中缩写 REX（p179，未展开）与 RE混用。
  alias_or_related: REX = 本词条缩写；单设备版本分界见 n16；DISA 见 g09
  tags: [concept, remote-extension, smartphone]

- id: g09
  term: DISA
  category: concept
  source_pages: p178, p192-193, p198
  source_quote: |
    "Remote extension DISA prefix … Number: Enter the prefix directory number (e.g.: 31280)" (p192)
    "The OpenTouch server MUST know the DISA public directory number used to reach the Remote Extension." (p197)
  definition: |
    远程分机的公共接入口机制：DISA 前缀（实验口径 31280）+ 公共 DISA 号码（实验口径 +3320131444）+ 中继
    组允许 DISA + DDI 翻译表落地。缩写全书未展开全称。
  alias_or_related: Automatic substitution（g10）依赖 DISA；DISA Parameters 在 System/Other System Param.
  tags: [concept, disa, remote-extension]

- id: g10
  term: Automatic substitution
  category: concept
  source_pages: p192, p195, p208
  source_quote: |
    "Automatic DISA Substitution: Without code" (p192)
    "The speed dial number is also automatically configured for DISA automatic substitution, when remote
    extension calls." (p208)
  definition: |
    自动替代：远程分机呼入时用直连速拨号（A<RE 号>）替换主叫呈现，让接听方看到的是用户身份而非陌生手机
    号；系统级授权为 "Without code"（无需替代码），号码来自 Direct Speed Dialing 号段。
  alias_or_related: 号段约束见 n20；速拨号见 g12
  tags: [concept, substitution, caller-id]

- id: g11
  term: Tandem (twinset)
  category: concept
  source_pages: p178, p209
  source_quote: |
    "A tandem (twinset) is configured between both the main desktop phone and the remote extension. … To
    configure a tandem, both the desktop and remote extension must be multi-line devices." (p209)
  definition: |
    主话机与远程分机之间的并联结构（同组多线，双方至少 L1/L2 两条线，系统可自动建线）。自动创建清单里
    四种模式全含 Tandem。与呼转（forward）是两种机制——R2.6 单设备的收益之一正是摆脱"呼转到离线设备"。
  alias_or_related: 多线（multi-line）配置在 Users/Prog. Keys 核验（p209）
  tags: [concept, tandem, multi-line]

- id: g12
  term: Direct Speed Dialing number
  category: concept
  source_pages: p178, p195, p201, p208
  source_quote: |
    "Range of direct speed dialing numbers … The range size CANNOT be 0 and also should NOT be full." (p195)
    "Direct speed dial number: Enter a speed dial number associated to the Remote Extension (e.g. A2131001)" (p201)
  definition: |
    自动替代占用的速拨号资源：A<RE 号> 形式（实验口径 A2131001），呼出侧由系统自动管理（Call Number 例
    00687654321）；号段不能为 0、不能满。缩写含义为"直连速拨号码"，书中未再展开。
  alias_or_related: 与 g08 RE、g10 自动替代三者联动
  tags: [concept, speed-dial, numbering]

- id: g13
  term: DAS rule
  category: concept
  source_pages: p67
  source_quote: |
    "Conference server Administration Console / Domain / DAS Rule 1 … DAS Rule 10" (p67)
    "DAS rules are mandatory and are country dependant." (p67)
  definition: |
    会议服务器管理台里的号码变换规则（s/^ 正则），作用于会议接入号码规范化；R2.0 起为游牧 OT Connection
    PC 新增 4 条。缩写全书未展开全称。
  alias_or_related: 10 条法国口径示例与顺序警告见 principle p06 / n02
  tags: [concept, das, conference, numbering]

- id: g14
  term: Fallback mode (DTMF)
  category: concept
  source_pages: p166, p175-176
  source_quote: |
    "No data connection: Fallback mode using DTMF" (p166)
    "Features provided in fallback mode based on DTMF over voice flow: Communication context: Make call &
    Release call; Voicemail; Routing (limited)" (p175)
  definition: |
    智能手机无数据连接时的带内回落模式：靠话音流上的 DTMF 指令支撑打/挂电话、留言与有限路由。需要中继
    侧 DISA/DTMF 序列配合（RE Parameters 可改 DTMF 序列，p193）。Android 无 SIM 时空闲即无回落。
  alias_or_related: 与 DTMF 缩写相关（未展开全称）；RE Parameters 路径 p193
  tags: [concept, fallback, dtmf]

- id: g15
  term: POD
  category: concept
  source_pages: p4-10, p11
  source_quote: |
    "Access to a pool of virtual machines (called POD) hosted in a remote data center … Several possible use
    cases … People present together in a classroom with RAP: up to 2 people assigned by POD" (p4)
  definition: |
    RLAB 远程实验室的独立实验单元（每 POD 一套同构虚机池 + 可选 RAP/物理设备/客户端 PC），POD 间互相
    独立、共享公共资源（NAS 与 SIP 模拟器在公共区/虚机池内，随拓扑而定）。三种学员接入拓扑：教室+RAP、
    RAP+话机、任意 PC 经 HTTPS。
  alias_or_related: RAP=Remote Access Point（p9 图注展开）；DCS 虚机在图中出现、无细节（passing mention）
  tags: [concept, lab, pod]

- id: g16
  term: Device Management server (DM)
  category: concept
  source_pages: p154
  source_quote: |
    "Verify that OmniVista 8770 server is declared as the DM in the OpenTouch database. Open the SIP server
    configuration interface & declare the DM; OTC PC SIP softphone will retrieve the SIP files from the DM." (p154)
  definition: |
    设备管理服务器：OTC PC 软话机从它取 SIP 配置文件——本书场景即把 OmniVista 8770（nms.company.com，
    端口 8080，实验口径）声明为 DM。multi-devices 副设备配置的前置声明。
  alias_or_related: 声明路径 /Eco system/IT server/ → create → Device management server
  tags: [concept, dm, provisioning]

# ── 二、用户角色 (role) ──

- id: g17
  term: Corporate user
  category: role
  source_pages: p35-36, p40-41
  source_quote: |
    "Corporate user using software clients managed by the OpenTouch server … Corporate user with remote
    access via Edge Servers: Reverse Proxy and SBC … Corporate user with remote access via VPN" (p35)
  definition: |
    公司内部用户（有 OpenTouch 账号的员工）：远程接入可用边缘双件套（RP+OTSBC）或 VPN（技术替代）；
    各 OTC 客户端形态的能力边界见用例矩阵（OTC PC 全功能、OTC PC One 无 VoIP 等）。
  alias_or_related: 对照 g18 External guest user；VPN 场景 p01
  tags: [role, corporate-user]

- id: g18
  term: External guest user
  category: role
  source_pages: p33, p35, p42
  source_quote: |
    "External partners/customers can access to conference/web collaboration system from the Internet" (p34)
    "External/Guest user remote access via Edge Servers: Reverse Proxy and SBC" (p35)
  definition: |
    外部来宾（伙伴/客户）：从互联网进会议与 Web 协作（OTC Web/WebRTC），流量经反代（协作）与 SBC（音
    视频）；用例矩阵中外部用户行多为 N.A，能力以会议/协作为限。
  alias_or_related: 依赖 conference FQDN 公共解析与证书 SAN（n03）
  tags: [role, guest]

# ── 三、许可/权利 (subscription) ──

- id: g19
  term: Nomadic SIP right
  category: subscription
  source_pages: p161
  source_quote: |
    "To be able to use the Nomadic mode using SIP protocol, additional right must be granted to the OTC
    Connection user. … Nomadic SIP: Must be enabled" (p161)
  definition: |
    用户级许可（OT 侧 licenses 页签）：SIP 游牧模式的开关之一；必须与 Desktop 许可同开。
  alias_or_related: 与 g20 Desktop、g21 Off-site mobility 同属 OT 用户许可项
  tags: [subscription, license, nomadic]

- id: g20
  term: Desktop license
  category: subscription
  source_pages: p161
  source_quote: |
    "Select the user and then 'licenses' tab … Nomadic SIP: Must be enabled; Desktop: Must be enabled" (p161)
  definition: |
    用户级许可项：游牧 SIP 场景下与 Nomadic SIP 同时启用；书中未展开其完整能力范围（与桌面客户端授权
    相关的口径在书外）。
  alias_or_related: 见 g19
  tags: [subscription, license]

- id: g21
  term: Off-site mobility right
  category: subscription
  source_pages: p178, p198, p203, p206
  source_quote: |
    "Off site mobility: Checked … The right to use a mobile phone linked to OpenTouch services has to be
    set for the user." (p203)
  definition: |
    用户级许可（OT configuration → Licenses）：使用与 OpenTouch 服务绑定的手机的权力；智能手机
    （twinset 与单设备两种配法）都必须勾选，How-To 中两处反复强调"Don't forget"。
  alias_or_related: 智能手机许可三件套语境：Off-site mobility + 设备关联 + 自动对象
  tags: [subscription, license, mobility]

# ── 四、产品/组件名 (product) ──

- id: g22
  term: OTSBC
  full_name: OpenTouch Session Border Controller（书中 p37 展开，ALE OEM）
  category: product
  source_pages: p35-39, p78-88, p89-117
  source_quote: |
    "ALE OpenTouch Session Border Controller (OTSBC): In charge of managing and securing the SIP session
    and the media streams (audio and video) based on RTP or SRTP" (p37)
    "Proxy ToIP (Telephony over IP): NAT Traversal … Quality of service and CAC … Routing of emergency
    numbers" (p81)
  definition: |
    DMZ 上的会话边界控制器：SIP 会话与 RTP/SRTP 媒体的管理与加密（DoS 防护、拓扑隐藏、TLS/SRTP）、
    CAC、NAT 穿越、紧急号码路由；场外客户端把它当 SIP 服务器。承载为 AudioCodes Mediant 平台（p86 配置
    结构、p91 CLI、p110 wizard 版本 7.2 可证）。7.2 起可内嵌反向代理（g23）。
  alias_or_related: 申报端口 5261（OTC）/8061（WebRTC）/5265（iPhone+）；部署见 case c02
  tags: [product, sbc, security, core]

- id: g23
  term: Reverse Proxy (RP)
  category: product
  source_pages: p35-38, p118-130, p131-144
  source_quote: |
    "Reverse Proxy (RP) … In charge of managing the HTTPs session to access the Telephony services provided
    by the software clients … Third party product that is not provided by ALE" (p37)
    "Reverse Proxy features: Topology hiding … Authentication (LDAP, …) … URL rewriting/blocking … SSL
    termination" (p38)
  definition: |
    反向代理：管理远程客户端到话音 Web 服务的 HTTPS 会话；拓扑隐藏、认证（可接 LDAP/RADIUS）、URL 改写/
    封禁、SSL 卸载；协作流量（桌面共享/IM/文档）也经它。第三方产品（如 Nginx），也可由 OTSBC 7.2+ 内嵌
    （HTTP proxy 功能，需专门许可）。OT 侧申报 API/EVS(:8016)/ACS/DMS 四个公共 URL。
  alias_or_related: 两条部署路线见 framework f12；case c03（内嵌）/c08（Nginx）
  tags: [product, reverse-proxy, security, core]

- id: g24
  term: Nginx
  category: product
  source_pages: p129, p218-259
  source_quote: |
    "The reverse proxy used here is Nginx (pronounced engine-x) which is a free, open-source,
    high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server." (p221)
  definition: |
    独立反代路线的承载软件：Ubuntu VM 上安装（mainline 源），配置三份 conf（global/remoteworker/
    conference）+ snippets（证书与 FQDN 变量、LDAP）；OT 2.2 起必须 remoteworker.conf 与 conference.conf
    同改。可选外接 LDAP 认证（Python 2 模块）。
  alias_or_related: 与 g23 RP 的关系=承载实现之一；LDAP 模块见 resource g61
  tags: [product, nginx, reverse-proxy]

- id: g25
  term: OTMS
  category: product
  source_pages: p9, p12, p21
  source_quote: |
    "OTMS-V (virtual machine): Hostname: opentouch.company.com; IP address: 151.1.1.50 … SUSE Linux
    Enterprise Server" (p12, 实验口径)
  definition: |
    OpenTouch 管理服务器虚机（实验口径 opentouch.company.com=151.1.1.50，SUSE）：本书正文的 "OpenTouch
    server" 在实验环境的承载；客户端私网 URL、RP 模板里的 ot.private-ip 都指向它。缩写全书未展开全称。
  alias_or_related: 对照 g26 OMS；DNS 名录见 p21
  tags: [product, lab, server]

- id: g26
  term: OMS
  category: product
  source_pages: p9, p16, p30
  source_quote: |
    "OMS: Hostname: oms.company.com; IP address: 151.1.1.13" (p16, 实验口径)
    "OMS admin admin letacla1; root root letacla1" (p30, 实验口径)
  definition: |
    OpenTouch 体系中的另一管理组件虚机（实验口径 151.1.1.13）；SIP 运营商模拟器拓扑图中与 OXE CS VM 并列
    出现（p26）。书中未展开其职能细节与缩写全称。
  alias_or_related: 口令 letacla1 见 n33
  tags: [product, lab, server]

- id: g27
  term: OmniVista 8770
  category: product
  source_pages: p9, p13, p63-77, p151-212
  source_quote: |
    "OmniVista 8770-V (virtual machine): Hostname: nms.company.com; IP address: 151.1.1.70" (p13, 实验口径)
    "In the OmniVista 8770 application, select the 'OpenTouch' configuration window" (p63)
  definition: |
    网管/配置工具（实验口径 nms.company.com=151.1.1.70）：本书全部 OXE 侧与 OT 侧申报操作的载体——含
    "OpenTouch" 配置窗（System services/Topology/Reverse proxy 等）、"OmniPCX Enterprise" 配置窗
    （Translator/Users/Classes of Service 等）、Users 应用（设备关联）、Profiles（设备档案）。也兼任 DM
    （g16）。
  alias_or_related: 8770 同步动作（OXE CS prefixes synchro）p198
  tags: [product, nms, management]

- id: g28
  term: OXE (OmniPCX Enterprise)
  full_name: OmniPCX Enterprise（p29 语境 "OmniPCX Enterprise Communication Server"）
  category: product
  source_pages: p9, p14, p21, p152-161, p191-212
  source_quote: |
    "OXE-V (virtual machine): Adressage IP Physique (CS physique): Hostname: csa.company.com, IP address:
    151.1.1.1; Adressage IP par rôle (CS main): csm.company.com, 151.1.1.3" (p14, 实验口径)
  definition: |
    呼叫服务器：承载话机注册、编号计划（Translator/Prefix Plan/DDI）、Ghost Z/SIP 设备/远程分机/tandem/
    ARS/判别器等对象；智能手机自动配置的对象全部落在 OXE。SIP 通信对 Connection 用户负责（g04）。
  alias_or_related: SIP 设置 URL Domain 取自 "netadmin -m" 选项 17（p160）
  tags: [product, pbx, call-server]

- id: g29
  term: FlexLM server
  category: product
  source_pages: p9, p15, p260-263
  source_quote: |
    "FlexLM server (virtual machine): Hostname: flex.company.com; IP address: 151.1.1.80" (p15, 实验口径)
    "We will use OpenSSL from the CentOS of the Flexlm server to generate the certificate … The Flexlm
    server will be our Certification authority." (p261)
  definition: |
    许可服务器虚机（CentOS，实验口径 flex.company.com=151.1.1.80）；在证书实验里兼任自建 CA（OpenSSL
    生成根证书与通配符服务器证书）。与 Windows CA（Eco-system CertSrv）并列的两条签发路径。
  alias_or_related: 自建 CA 全流程见 case c09
  tags: [product, lab, ca]

- id: g30
  term: Eco-system server
  category: product
  source_pages: p9, p19-21, p72, p134
  source_quote: |
    "Eco-System server … Operating system: Windows Server 2016; Roles: DNS server, Exchange server, Active
    directory, LDAP server, DHCP server (for mobiles), Certification authority" (p19)
  definition: |
    实验环境的企业生态服务器（Windows Server 2016，实验口径 eco.company.com=151.1.1.100）：兼 DNS、
    Exchange、AD、LDAP、手机 DHCP 与证书颁发机构（https://eco.company.com/CertSrv，administrator/
    superuser，实验口径）。RP HTTP proxy 的 Secondary DNS 也指到公共区 10.20.30.254（实验口径）。
  alias_or_related: AD 用户表 p20；CA 申请路径见 case c01/c02
  tags: [product, lab, ad, ca]

- id: g31
  term: SIP carrier simulator
  category: product
  source_pages: p9, p17, p26-29
  source_quote: |
    "SIP carrier simulator (virtual machine): Hostname: sippublic.company.com; IP address: 151.1.1.105 …
    Based on a OXE" (p17, 实验口径)
  definition: |
    SIP 运营商模拟器（基于 OXE，实验口径 151.1.1.105）：提供出局中继与主叫显示变换（国内 0298131000 /
    规范 33298131000），支持国内 0abcd31xxx、规范 33abcd31xxx、国际 00ccabcd31xxx 三种拨测格式。教学
    专用，生产行为与真实运营商有差异。
  alias_or_related: 拨测预期表见 principle p10
  tags: [product, lab, sip-trunk]

- id: g32
  term: OTC PC
  category: product
  source_pages: p40, p49, p148, p151-161
  source_quote: |
    "PC clients: OTC PC, OTC PC One, OTC Web" (p49)
    "Reverse proxy FQDN configuration: At the startup or In Settings/Preferences/Start menu" (p148)
  definition: |
    PC 全功能软话机客户端（含 VoIP/视频）：远程接入需 RP+OTSBC；multi-devices 里可作 SIP 副设备（SIP URI
    =<号>@<OT FQDN>，SBC 参数 5261/TLS/Encrypted only）；Nomadic 里作游牧软话机。反代 FQDN 在启动时或
    Settings/Preferences 填。
  alias_or_related: 家族对照 g33/g34；Conversation/Connection 同体双行为（g03/g04）
  tags: [product, client, pc]

- id: g33
  term: OTC PC One
  category: product
  source_pages: p40, p49, p82, p122
  source_quote: |
    "N.U : Not Used (because no VoIP/video on this client)" (p82)
  definition: |
    无 VoIP/视频的 PC 客户端（协作型）：远程接入只需 RP，矩阵中标 N.U.（SBC 用不上——不是不支持）。
  alias_or_related: N.U./N.A. 语义见 n24
  tags: [product, client, pc]

- id: g34
  term: OTC Web / OTC WebRTC
  category: product
  source_pages: p40, p42, p49, p149
  source_quote: |
    "PC: OTC Web: Conference public URL received by mail" (p149)
  definition: |
    浏览器端两种形态：OTC Web（协作，仅需 RP；给全体员工与外部来宾用）与 OTC WebRTC（音视频，需 RP+
    OTSBC）。接入方式特殊：用邮件收到的会议公共 URL 直接进入。
  alias_or_related: 会议 URL 依赖 conference FQDN 公共解析（n03）
  tags: [product, client, web]

- id: g35
  term: OTC smartphone (Android / iPhone)
  category: product
  source_pages: p164-188, p189-217
  source_quote: |
    "OTC on smartphone is available on: Android devices; iPhone … Same application for Conversation and
    Connection users; Installed from markets: Google Play; App Store" (p164-165)
  definition: |
    移动客户端家族：Android 版（Google Play 的 OpenTouch Conversation）与 iPhone 版；Connection 用户按
    双模式/单设备配置（关联后自动建 OXE 对象）；iPhone 的推送来话走 APNS（iPhone+）。连接模式矩阵见
    framework f15。
  alias_or_related: 单设备版本分界 R2.6（n16）；无 SIM Android 见 n23
  tags: [product, client, smartphone]

- id: g36
  term: OpenTouch Conversation Plus (OTC Plus / iPhone+)
  category: product
  source_pages: p188, p215-217
  source_quote: |
    "Install OTC Plus application on the iPhone. … Look for 'alcatel'; Select 'OpenTouch Conversation Plus'" (p215)
    "Specific SBC declaration for iPhone+ … FQDN: same as 'generic' SBC … Port: 5265" (p197)
  definition: |
    iPhone+ 专用应用（App Store 名 OpenTouch Conversation Plus）：支持 VoIP everywhere（经 SBC、场外
    TCP+代理缓冲）；配套 SBC 声明用 5265 端口、OT SBC 增配 5265 SIP 接口、防火墙四端口、APNS 证书年更；
    维护抓 kamailio-wasp/wspcfg。
  alias_or_related: APNS 链路见 g37/g38/g39；防火墙端口见 principle p30
  tags: [product, client, iphone]

- id: g37
  term: APNS
  full_name: Apple Push Notification Server（书中 p183 直接展开）
  category: product
  source_pages: p183-186
  source_quote: |
    "All notifications from OpenTouch server to OTC iPhone are sent through Apple Push Notification Server
    (APNS). APNS is an Apple Cloud service: firewall configuration is impacted" (p183)
  definition: |
    Apple 云推送服务：R2.3.1 起 iPhone 的 OT 通知全走它；是 VoIP 来话的"第二振铃路径"（推送唤醒应用后
    才接受 SIP invite）。防火墙放行 TCP 5223/2195/2196/443；APNS 证书一年一换（专门 hotfix）、Geotrust
    根证书至 2022。
  alias_or_related: 机制链与约束见 n17/n18；端口表 principle p30
  tags: [product, push, iphone]

- id: g38
  term: kamailio-wasp
  category: product
  source_pages: p187, p217
  source_quote: |
    "kamailio-wasp: SIP proxy between SBC and OXE" (p187)
    "Service Kamailio: service kamailio-wasp status|start|stop|restart; Log files: /var/log/localmessages" (p217)
  definition: |
    iPhone "VoIP everywhere" 专用 SIP 代理（SBC 与 OXE 之间）：场外 TCP 场景下缓冲多 SIP invite；维护经
    service 命令与 loglevel.sh（3=DBG…-1=ERR），日志 /var/log/localmessages；Logzipper 打包含其日志。
  alias_or_related: 配套配置服务=g39 wspcfg
  tags: [product, iphone, sip-proxy]

- id: g39
  term: wspcfg
  category: product
  source_pages: p187, p217
  source_quote: |
    "wspcfg: service to provide configuration for kamailio" (p187)
    "Service wspcfg: service wspcfgd status|start|stop|restart; Log file: /logs/wspcfg/wspcfg.log" (p217)
  definition: |
    给 kamailio 提供配置的服务（守护进程名 wspcfgd）：日志 /logs/wspcfg/wspcfg.log，日志级别经
    loglevel.sh component=wspcfg logger=* level={LEVEL} 调整。
  alias_or_related: 与 g38 同属 iPhone+ 维护面
  tags: [product, iphone, service]

- id: g40
  term: OTES
  category: product
  source_pages: p46, p253, p267
  source_quote: |
    "TC2257 OpenTouch from 0 to remote worker with OTES replacement" (p46)
    "As the OTES server is no more part of the solution, the reverse proxy must be configured to support
    application sharing during data conferences" (p253)
  definition: |
    OpenTouch 旧代远程接入专用服务器（缩写全书未展开）：在 OT 2.2 起"不再是方案的一部分"（no more part
    of the solution），其职能由反代+OTSBC 接管（TC2257 标题即"with OTES replacement"）。OpenSSL 章的证书
    说明文字仍留有 "OpenTouch/OTES/RP" 三服务器旧表述（p261/p267），阅读时按 OT+RP+OTSBC 新结构理解。
  alias_or_related: 版本影响见 n25
  tags: [product, legacy, version]

- id: g41
  term: WebAdmin
  category: product
  source_pages: p49, p54, p71-77, p267-268
  source_quote: |
    "Web administration: WebAdmin, ACS administration, Maintenance portal" (p49)
    "OpenTouch server certificate import using WebAdmin" (p54)
  definition: |
    OpenTouch 服务器的 Web 管理界面：证书 CSR 生成/导入/部署（System services/Security/Certificate）、
    证书 SAN 核验等操作入口；otAdmin/Admin-8770 为实验登录（p30，实验口径）；部署证书后会被切断会话
    （n04）。
  alias_or_related: 与 OmniVista 8770（g27）分工：WebAdmin 管 OT 服务器自身，8770 管拓扑/用户/OXE
  tags: [product, management, web]

- id: g42
  term: SEPLOS
  category: product
  source_pages: p182
  source_quote: |
    "Remote extension as single device: Configuration simplified: no more need of SEPLOS as main set" (p182)
  definition: |
    R2.6 前单手机用户配法中的"主设备"角色载体（书中仅此一处出现，未展开细节）：旧法需要一个永不入服的
    SIP 主设备（书配图以 SEPLOS 示意）+溢出到 RE；R2.6 起 RE 直接做主设备后无需再用。
  alias_or_related: 版本背景见 n16
  tags: [product, legacy, remote-extension]

# ── 五、协议与技术名 (protocol) ──

- id: g43
  term: SIP
  category: protocol
  source_pages: p36-37, p81-86, p104-117
  source_quote: |
    "SIP signaling … OTSBC: In charge of managing and securing the SIP session" (p36-37)
    "The OTSBC for accesses from the WAN has to be declared in the IT servers. … Port 5261" (p65)
  definition: |
    场外话音的信令协议：客户端经 OTSBC 公共 FQDN 注册（SIP over TLS 5261/8061/5263/5161 等，实验口径
    端口矩阵 p86）；OXE 侧 UDP/TCP 5060 均可（向导只配 UDP，建议补 TCP，p117）。
  alias_or_related: SIP 域名口径：OTCV/OTCT=OTSBC 公共 FQDN，OTCV Web=OT 内部 FQDN（p104-105）
  tags: [protocol, sip, signaling]

- id: g44
  term: RTP / SRTP / TLS
  category: protocol
  source_pages: p36, p39, p81, p86, p134
  source_quote: |
    "Encryption of signaling (TLS) and media (SRTP)" (p39)
    "Media Realm 3: SRTP/7000:7499 … RTP/28000:39999" (p86, 实验口径端口段)
  definition: |
    媒体与加密口径：信令 TLS、媒体 RTP/SRTP（可加密矩阵 p40-42）；OTSBC 侧 Media Realm 划分 RTP/SRTP
    端口段（6000-6499、7000-7499、8000-8499、9000-9499；公网侧 28000-39999、32000-32299）。缩写均未
    展开全称。
  alias_or_related: 端口/NAT 规划见 principle p07
  tags: [protocol, media, encryption]

- id: g45
  term: DTMF
  category: protocol
  source_pages: p166, p175, p193
  source_quote: |
    "No data connection: Fallback mode using DTMF" (p166)
    "Remote extension parameters: DTMF code sequences can be modified, if required." (p193)
  definition: |
    带内双音多频指令：回落模式的控制通道（打/挂/留言/有限路由）；RE Parameters 里可改 DTMF 序列。缩写
    未展开全称。
  alias_or_related: 见 g14 Fallback mode
  tags: [protocol, dtmf, fallback]

- id: g46
  term: LDAP
  category: protocol
  source_pages: p19, p37-38, p140, p257-259
  source_quote: |
    "Can connect to the company authentication service (based on LDAP or RADIUS) to authenticate the
    corporate users" (p37)
    "LDAP authentication script deployment … set $ldapaddress ldap://151.1.1.100; set $basedn
    cn=Users,dc=company,dc=com" (p259, 实验口径)
  definition: |
    目录认证协议：RP 层认证可接公司 LDAP/RADIUS；Nginx 路线用 nginx-ldap-auth 模块（Python 2、daemon
    8888）；实验 Eco-system 的 AD 即 LDAP 源（实验口径 ldap://151.1.1.100、binddn cn=directory…）。RADIUS
    仅在 RP 职责描述中并列出现、无展开。
  alias_or_related: 认证约束见 n10/n26
  tags: [protocol, ldap, authentication]

- id: g47
  term: PKCS7 / PKCS12
  category: protocol
  source_pages: p54, p56-57, p76, p263
  source_quote: |
    "OpenTouch server certificate import using WebAdmin: PKCS7: certificate (CSR was done on OT server);
    PKCS12 (protected by passphrase): certificate and private key (generated on CA)" (p54)
  definition: |
    两种证书交换封装：CSR 在申请方本机生成→PKCS7（只含证书链）；密钥对在 CA 生成→PKCS12（含私钥、带
    passphrase，导入时输入）。OpenSSL 章的 servers.p12 即后者（导出口令=挑战口令，实验口径）。
  alias_or_related: 封装流程图 p56-57；部署五步见 principle p04
  tags: [protocol, certificates, pkcs]

- id: g48
  term: CSR
  full_name: Certificate Signing Request（书中 p54 直接展开）
  category: protocol
  source_pages: p54-55, p71, p97, p136, p250
  source_quote: |
    "Certificate Signing Request using WebAdmin interface (this action will also generate private-public
    keys pair)" (p55)
  definition: |
    证书签名请求：可在申请方服务器（WebAdmin/OTSBC TLS Context/Nginx OpenSSL）生成——同时产生密钥对；
    也可直接在 CA 服务器生成。生成位置决定用 PKCS7 还是 PKCS12 导入。
  alias_or_related: 见 g47；OpenSSL 生成命令见 case c08/c09
  tags: [protocol, certificates]

- id: g49
  term: SAN
  full_name: Subject Alternative Name（书中 p127 直接展开）
  category: protocol
  source_pages: p68-69, p77, p97, p127, p136-137
  source_quote: |
    "In 'Details' tab, look for Subject Alternative Name parameter." (p69)
    "Certificat generated for *: public-ot.company.com; conference.company.com. * SAN: Subject Alternative
    Name" (p127)
  definition: |
    证书主题备用名：会议 FQDN 必须进 RP 与 OT 证书的 SAN；专用证书布局下 OT 证书 SAN=opentouch+conference、
    边缘证书 SAN=public-ot+conference；OTSBC 证书复用时也要加 OT/会议公共名（p135 Notes）。核验入口：
    证书 Details 页签。
  alias_or_related: 强制警告见 n03；RP-Conf CSR 的 SAN=会议 FQDN（c03 步骤 3）
  tags: [protocol, certificates, san]

- id: g50
  term: CTL
  category: protocol
  source_pages: p50-51, p268
  source_quote: |
    "'Generic' certificate and CTL signed by a 'generic' device: Choice done during installation (security
    off)" (p50)
    "THE CTL (USED BY DESKPHONES) HAS TO BE REGENERATED (SIGNED AGAIN) BECAUSE THE SERVER'S CERTIFICATE HAS
    CHANGED." (p268)
  definition: |
    话机侧信任列表（由设备签名、伴随服务器证书体系）：预装"通用证书"方案里由"通用设备"签名；服务器证书
    变更后必须重新生成（重新签名）。缩写全书未展开全称；重签操作在另一培训规程。
  alias_or_related: 见 n01/n05
  tags: [protocol, certificates, deskphones]

- id: g51
  term: NAT
  category: protocol
  source_pages: p10, p43, p63-66, p90, p102
  source_quote: |
    "NAT: Public-RP-IP@ <-> Private-RP-IP@; Public-SBC-IP@<->Private-SBC-IP@" (p43)
    "NAT Public IP: Enter the public IP address corresponding to the SBC (before the NAT). E.g.
    195.128.146.10x" (p103, 实验口径)
  definition: |
    公私网地址映射：RP/SBC 各一组公私 IP 对（实验口径 195.128.146.102↔11.1.1.10 / ↔11.1.1.20）+ 端口与
    RTP 段映射；OTSBC 向导里以 "NAT Public IP" 字段录入。SBC 的 NAT 穿越（NAT Traversal）是其功能清单
    第一项（p81）。
  alias_or_related: 端口规划见 principle p07
  tags: [protocol, nat, network]

# ── 六、网站与资源名 (resource) ──

- id: g52
  term: Business Portal
  category: resource
  source_pages: p46, p90, p101, p107
  source_quote: |
    "Available documents on Business Portal: TC2639 …" (p46)
    "The ovf file is available on Business Portal web site. … On Business Portal web site, you can also find
    the wizard software for OTSBC deployment." (p90)
  definition: |
    ALE 商务门户：本书引用文档族的载体（TC 系列、8AL 系列）、OTSBC 的 OVF 与配置向导软件下载入口。
  alias_or_related: 下载入口对照 g57/g58
  tags: [resource, portal]

- id: g53
  term: TC2639
  category: resource
  source_pages: p46, p105, p117, p140, p143, p220
  source_quote: |
    "TC2639 OpenTouch Remote Worker/Mobility Configuration Update" (p46)
    "CONSULT THE TC2639 FOR CONFIGURATION INFORMATION." (p105)
  definition: |
    本书的第一权威外链：OpenTouch 远程工作者/移动化配置更新（技术通报）。iPhone 手工配置、RP 模板文件
    更新、LDAP 认证细节均指向它；Nginx 模板下载链接亦以 TC2639 最新版为准（p220）。
  alias_or_related: 生产化的必读文档；对照 g54/g55
  tags: [resource, document, tc]

- id: g54
  term: TC2257 / TC1990
  category: resource
  source_pages: p46, p117
  source_quote: |
    "TC2257 OpenTouch from 0 to remote worker with OTES replacement; TC1990 OpenTouch Release 2.x from 0 to
    remote worker" (p46)
  definition: |
    两代"从零到远程工作者"部署文档：TC1990（R2.x 时代）与 TC2257（OTES 替代版）；OTSBC 手工配置的补充
    信息另指 TC1990 或 8AL90065USAG（p117）。并为一词条（同族同用途）。
  alias_or_related: OTES 背景见 g40；模板链接可来自 TC2639 或 TC2257（p220）
  tags: [resource, document, tc]

- id: g55
  term: TC2341en
  category: resource
  source_pages: p217
  source_quote: |
    "Deployment Guide for OTC smartphone in Voice over IP for Connection Users, please consult:
    https://businessportal2.alcatel-lucent.com/TC2341en" (p217)
  definition: |
    OTC 智能手机 VoIP（Connection 用户）部署指南：智能手机章节附录给出的直达链接（Business Portal）。
  alias_or_related: 智能手机 How-To 的生产化补充
  tags: [resource, document, tc]

- id: g56
  term: TC1981 / TC1839
  category: resource
  source_pages: p46
  source_quote: |
    "TC1981 Technical Release Note for OTC Android Smartphone Release 2.5 …; TC1839 Technical Release Note
    for OTC iPhone release 2.3 …" (p46)
  definition: |
    OTC 移动客户端的技术发布说明（Android R2.5 / iPhone R2.3）：手机章节的版本依据文档。并为一词条
    （同族）。注意其版本号（2.5/2.3）低于教材主体 R2.6，反映各组件发布节奏不同。
  alias_or_related: 版本坐标见 BOOK_OVERVIEW 批判节
  tags: [resource, document, release-note]

- id: g57
  term: 8AL90062USAG / 8AL90065USAG
  category: resource
  source_pages: p46, p117
  source_quote: |
    "8AL90062USAG: Alcatel-Lucent OpenTouch Session Border Controler - R2.x Release Note; 8AL90065USAG:
    OpenTouch Session Border Controler R2.x Configuration Guide" (p46)
    "consult TC1990 or otsbc2.x_am_ConfigurationGuide_8AL90065USAG document" (p117)
  definition: |
    OTSBC 的发布说明与配置指南（R2.x 文档族）：OTSBC 手工参数（如 OXE SIP 接口补 TCP）的深入参考。
    并为一词条。
  alias_or_related: OTSBC 部署细节的权威外链
  tags: [resource, document, otsbc]

- id: g58
  term: al-mydemo.com
  category: resource
  source_pages: p63-77, p90, p132, p220, p250
  source_quote: |
    "https://ot-podx.al-mydemo.com … conf-podx.al-mydemo.com … otsbc-podx.al-mydemo.com" (p63-66)
  definition: |
    实验演示公网域（实验口径）：全部公共 FQDN 的后缀——ot-podx（OT/RP）、conf-podx（ACS 会议）、
    otsbc-podx（OTSBC）；对应公网段 195.128.146.10x。生产化时整体替换为客户域名。
  alias_or_related: 对照内网实验域 g59 company.com
  tags: [resource, lab, domain]

- id: g59
  term: company.com
  category: resource
  source_pages: p11, p19-21, p156, p254, p261
  source_quote: |
    "DNS domain name is 'company.com'" (p21)
    "openssl req … Common Name (eg, your name or your server's hostname) []:*.company.com" (p262, 实验口径)
  definition: |
    实验内网 DNS 域（实验口径）：全部内网主机名后缀（opentouch/nms/csa/csm/flex/oms/eco/client…）与
    通配符证书 *.company.com 的域。与演示公网域 al-mydemo.com 分工：内网解析 vs 公网解析。
  alias_or_related: DNS 名录 p21；通配符证书见 c09
  tags: [resource, lab, domain, dns]

- id: g60
  term: eco.company.com/CertSrv
  category: resource
  source_pages: p72, p98, p137
  source_quote: |
    "Using a web browser, access to CA hosted on Eco system server: https://eco.company.com/CertSrv …
    Login: administrator; Password: superuser" (p72, 实验口径)
  definition: |
    实验 Windows 证书颁发机构的申请入口（Eco-system 服务器自带 CA 角色）：OT/OTSBC/RP 的 CSR 都提交到
    这里（advanced request → base-64 → Web Server 模板 → 下载证书链）。纯实验口径，生产用客户 PKI。
  alias_or_related: 申请步骤见 c01/c02/c03；另一条 CA 路线=FlexLM OpenSSL（c09/g29）
  tags: [resource, lab, ca]

- id: g61
  term: nginx-ldap-auth
  category: resource
  source_pages: p257-259
  source_quote: |
    "All the information about the authentication module and the scripts used to set up this LDAP
    authentication can be found on https://github.com/nginxinc/nginx-ldap-auth" (p257)
  definition: |
    Nginx LDAP 认证模块的官方开源项目（github）：核心为 Python 2 脚本 nginx-ldap-auth-daemon.py（daemon
    监听 8888）+ init 启动脚本；部署与排错（dos2unix）见 case c08 步骤 8。
  alias_or_related: 约束见 n10/n26
  tags: [resource, open-source, ldap]

- id: g62
  term: nas.alcatel-support.com（模板下载）
  category: resource
  source_pages: p220
  source_quote: |
    "The required template files for the reverse proxy configuration are available at this address:
    http://nas.alcatel-support.com/index.php/s/0a26TOag6MaXHD9 … Consult the last TC2639 edition to be sure
    to use the correct URL link" (p220)
  definition: |
    Nginx/RP 配置模板文件的下载地址（书中快照链接）：remoteworker.conf、global.conf、conference.conf、
    snippets、ldap.conf 等。官方明示以 TC2639 最新版给出的链接为准——本书链接可能过期（见 n35）。
  alias_or_related: 与 RLAB 公共 NFS nas.company.com（f03）是两回事，勿混
  tags: [resource, templates]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列候选术语逐条核对

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| OTSBC | 正文有明确定义（p37/p81） | g22 |
| Reverse Proxy (RP) | 有明确定义（p37/p38） | g23 |
| Conversation user / Connection user | 有明确定义（p114） | g03 / g04 |
| Multi-devices | 有明确定义（p152） | g05 |
| Nomadic (SIP) | 有明确定义（p152/p157） | g06 |
| Ghost Z set | 有明确定义（p158/p194） | g07 |
| Remote Extension (RE) | 有明确定义（p192/p204） | g08 |
| DISA | 有定义性用法（p192-193/p197），全书未展开全称 | g09（full_name 如实省略） |
| Tandem (twinset) | 有明确定义（p209） | g11 |
| Direct Speed Dialing number | 有明确定义（p195/p201/p208） | g12 |
| ARS + Discriminator | ARS 经菜单名展开（Translator/Automatic Route Selection，p211），未单列术语条目——按口径并入 principle p29/p32 与 case c06；Discriminator 同理（p210/p212） | （并入 p 类条目） |
| DAS rule | 有明确定义（p67） | g13 |
| APNS | 有明确定义（p183-184） | g37 |
| kamailio-wasp / wspcfg | 有明确定义（p187/p217） | g38 / g39 |
| OTC 家族 | 有明确定义（p49/p82 矩阵） | g32/g33/g34/g35/g36 |
| PKCS7 / PKCS12 | 有明确定义（p54/p56-57） | g47 |
| SAN (Subject Alternative Name) | 有明确定义（p68/p127） | g49 |
| OTMS / OMS | 有定义性用法（p12/p16，实验口径），全书未展开全称 | g25 / g26 |

结论：**OVERVIEW 的 18 行术语全部"本书正文有明确定义或定义性用法"，无"仅 passing 提及需排除"项，无删除建议。** ARS/Discriminator 在 OVERVIEW 合并为一行表述，本文件按口径落在 principle 条目（p29/p32），未单列术语，已在下节备查中说明。

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：OpenTouch Suite for MLE（g01）、Remote worker（g02）、Automatic substitution（g10）、Fallback mode（g14）、POD（g15）、DM（g16）
- 角色：Corporate user（g17）、External guest user（g18）
- 许可：Nomadic SIP right（g19）、Desktop license（g20）、Off-site mobility right（g21）
- 产品：Nginx（g24）、OmniVista 8770（g27）、OXE（g28）、FlexLM server（g29）、Eco-system server（g30）、SIP carrier simulator（g31）、OTES（g40）、WebAdmin（g41）、SEPLOS（g42）
- 协议：SIP（g43）、RTP/SRTP/TLS（g44）、DTMF（g45）、LDAP（g46）、CSR（g48）、CTL（g50）、NAT（g51）
- 资源：Business Portal（g52）、TC2639（g53）、TC2257/TC1990（g54）、TC2341en（g55）、TC1981/TC1839（g56）、8AL90062USAG/8AL90065USAG（g57）、al-mydemo.com（g58）、company.com（g59）、eco.company.com/CertSrv（g60）、nginx-ldap-auth（g61）、nas.alcatel-support.com（g62）

### 3. 仅 passing 提及、未单列条目的词（备查）

- ARS（Automatic Route Selection）/Discriminator：经菜单名与正文定义，落 principle p29/p32 与 case c06，未单列（OVERVIEW 已合并表述）。
- RAP（p9 Remote Access Point，附于 g15）、DCS（p9/p12 虚机名，无细节）、RAP/POD 客户端拓扑细节（f02）、OTMC-V / sot.company.com（p21 DNS 名录，附于 f03）、IPG / Media Realm / SIP Interface / Message Manipulation（p86 AudioCodes 配置对象名，附于 f11）、CAC（p81，未展开全称，附于 g22）、RADIUS（p37，附于 g46）、OTCV / OTCT（p104-105 向导参数组名，附于 g03/g04）、SEPLOS 已单列（g42，仅 p182 一处）、RUFUS 不在本书、N.U./N.A.（附于 g33 与 n24）、EVS/ACS/DMS（RP 四 URL 中的服务名，附于 g23 与 n32；ACS=会议服务语境，全书未展开全称）、eDemo（p278-287 营销内容，不入册）。

### 4. 提取口径说明

- 所有定义只采信本书正文；DISA、CTL、CAC、DCS、DAS、OTES、SEPLOS、OTMS、OMS、EVS、ACS、DMS、IPG 等缩写书中未给全称，full_name 字段一律省略或标注"未展开"，不做外部补全。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准，引用均为原文摘录；原文笔误（p229 网关 10.1.0.254、p250 /etc/inid.d/、p156 otsbx-、p214 https// 缺冒号）已在 n29 集中登记，引用处不再重复标注。
- 实验环境给定值（IP、域名、口令、号码）一律标注"实验口径"（g25/g26/g27/g28/g29/g30/g31/g41/g51/g58/g59/g60）。
