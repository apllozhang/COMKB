# 框架/流程/结构候选 — OpenTouch Message Center Starter (OTMCXTE200EN R2.6 Issue 08)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、系统对象模型。实验环境给定值（IP/密码/账号/分机号）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——产品认知 → 装机站点配置 → 双向纳管 → SIP 对接 → 信箱业务 → 增值与运维
  type: flow
  source_pages: p3-20, p21-32, p33-45, p46-58, p69-82, p83-118, p119-152, p153-166, p167-192, p193-209, p210-227, p228-246, p247-258
  source_chapter: 全书 9 讲义章 + 13 How-To 章的编排顺序（OTMC Overview / Topology for labs / Licensing principle / Installation Overview + How-To / Post-installation wizard How-To / OXE declaration + OTMC declaration + SIP configuration + Connection user's creation How-To / Mailbox features + configuration + profiles How-To / Web clients / SMTP-SMS notification / IMAP / General announcement / Backup & Restore / Voicemail statistics）
  source_quote: |
    "The OpenTouch™ Message Center is a stand-alone voice mail system installed on a single server, including
    automated attendant capabilities" (p5)
    "This post installation wizard is automatically started at the first boot of the OTMC server" (p70)
    "OTMC server must be declared in the same sub-network than the OXE call server." (p94)
  summary: |
    课程按六段推进：①OTMC 概览（定义/特性/可服务性/架构/商业包/虚拟化/许可/组网，p3-20）；②实验拓扑（VMware 六虚机 + 客户端 PC，p21-32）；③许可原理与装机（许可文件规则、安装概览与安装 How-To，p33-68）；④站点配置（post-installation wizard How-To + 手工装许可，p69-82）；⑤纳管与对接（OXE 声明/OTMC 声明/SIP 配置/Connection 用户四连发 How-To，p83-118）；⑥业务与增值运维（信箱特性/信箱配置/profile 配置三连发 + Web 客户端 + SMTP-SMS 通知 + IMAP + general announcement + 备份恢复 + 统计，p119-258）。这是"先底座后业务、先纳管后对接、先信箱后增值"的交付主线，也是现场实施推荐顺序。
  conditions: 无特殊版本前提；各 How-To 存在硬依赖（如声明依赖 post-install 产出的 bics.conf 账户）
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: OTMC 产品定位与访问三通道图
  type: diagram
  source_pages: p5-6, p8, p11
  source_chapter: OTMC Overview / OTMC Definition & Features
  source_quote: |
    "specifically addressed to Connection users of an OmniPCX Enterprise • OTMC package replaces former 46xx/
    8440 messaging solutions" (p5)
    "Access to voice messages • From any device via the TUI • From Premium Deskphones, Smart Deskphone 8088
    via the GUI • From any IMAP e-mail client" (p6)
  summary: |
    定位三句话：单服务器独立语音邮件系统（附带自动话务员能力定义）、只服务 OXE 的 Connection 用户、取代 46xx/8440。访问通道三条：①任意话机走 TUI；②Premium Deskphone 8xx8 与 Smart Deskphone 8088 走 GUI——信封键直达可视化信箱（envelope key，新留言时消息键闪烁，p8）；③任意 IMAP 邮件客户端（详见 f21）。另有管理员侧两个 Web 应用 My Messaging/My Profile（p11，详见 f19）。存储侧：消息存 OTMC 服务器或 SAN（p6）。
  conditions: GUI 直达可视化信箱仅限 8xx8 系列与 8088（p8）
  tags: [diagram, positioning, access-channels, vvm]

- id: f03
  title: OTMC 软件架构组件图（SUSE + OpenTouch Framework + 语音消息应用）
  type: diagram
  source_pages: p13, p17
  source_chapter: OTMC Overview / System architecture & Software Architecture
  source_quote: |
    "The OpenTouch™ Message Center server runs on a SUSE Linux Enterprise operating system." (p13)
    "SUSE Linux Enterprise Server + OT Hardware / OpenTouch Framework / Voice Messaging Application
    OpenTouch Message Center — HTTP server IMAP PRS MS UDA Msg- voice application My Profile OAM&P
    Chameleon (EVS + FWK)" (p17)
  summary: |
    三层结构：底座 SUSE Linux Enterprise Server（物理机或 VMware ESXi 虚机）；中间 OpenTouch Framework（含 Chameleon 组件，EVS+FWK）；上层语音消息应用，组件含 HTTP server、IMAP、PRS、MS、UDA、Msg-voice application、My Profile、OAM&P。排障抓手：组件服务 chameleond/scorpiod（p192），日志 /logs/chameleon/chameleon/panda.log、/logs/journal/chameleon.log、/logs/journal/scorpio.log。硬件与软件规格、产品上限均外指 feature list 与 product limits 文档（p13/p48 Note）。
  conditions: 缩写 PRS/MS/UDA/OAM&P/EVS/FWK 书中未展开全称
  tags: [diagram, architecture, components, suse]

- id: f04
  title: OXE-OTMC 连接架构图——单 SIP trunk + PRS 链路 + VPIM 组网
  type: diagram
  source_pages: p18-20
  source_chapter: OTMC Overview / Architecture & Infrastructure (Networking)
  source_quote: |
    "Direct SIP trunk group between OXE and OTMC • Only one SIP trunk is supported towards the front node
    • The SIP trunk group Bypass is configured for all ports available independently of the number of users
    • PRS Link between each OXE for GUI display • 5000 simultaneous users with GUI display on series 8 sets,
    Premium Deskphones 80x8 and Smart DeskPhone 8088" (p18)
    "OXE ABC Supra network not supported for centralized VM" (p20)
  summary: |
    连接三要素：①OXE 与 OTMC 间直连 SIP trunk group——仅一条、指向 front node，Bypass 按全部可用端口配置（与用户数无关）；②OXE 之间 PRS 链路支撑话机 GUI 显示语音信箱，上限 5000 并发用户（8 系/80x8/8088）；③VPIM 协议用于 OTMC 实体互联与三方语音邮件互通。组网支持集中式与分布式 OXE 子网（集中式仅一条 SIP trunk 指向 front node）；OXE ABC Supra 网络不支持集中式 VM。扩容必须用 OTMC 专用的 OpenTouch Capacity Planning Tool（p19：压缩场景示例 2800/1200 用户）。
  conditions: 话机 GUI 显示需 PRS；容量规划工具用法在书外
  tags: [diagram, sip-trunk, prs, vpim, networking, capacity]

- id: f05
  title: 商业包装与虚拟化决策结构（非虚拟化 vs OTMC-V）
  type: structure
  source_pages: p14-16
  source_chapter: OTMC Overview / Commercial packages, Virtualization, Licenses
  source_quote: |
    "Voice messaging dedicated commercial package is OT based and can evolve towards the full OT suite" (p14)
    "OTMC-V can be virtualized with VMware ESXi • vMotion, VMware Dynamic Resources Scheduling (manual /
    semi-automatic) are supported (Other VMware services are not supported) • OTMC-V VM Multi-instance is
    supported on the same physical host • Other applications (ALU-E or 3rd party) on virtual machine are
    allowed to run on the same physical host" (p15)
  summary: |
    商业包两分支：非虚拟化（SUSE + OTMC，带 dongle，ALE 整机交付）与虚拟化（OTMC OT based + VMware VM，无 dongle 一栏为"非 ALE 交付"口径）；语音消息专用包基于 OT，可演进到全 OpenTouch 套件。虚拟化边界（OTMC-V，可配 OXE 或 OXE-V）：支持 vMotion 与 VMware DRS（手动/半自动），其它 VMware 服务不支持；同物理主机可多实例、可混跑 ALE 或第三方应用虚机；限制与功能与非虚拟化版完全相同（p15）。许可差异（p16）：非虚拟化 ice 许可文件绑 ALUID（flex-lm 控制），虚拟化绑 Aladdin USB dongle（dongle-ID 控制）。
  conditions: 硬件规格外指 feature list / product limits 文档
  tags: [structure, packaging, virtualization, otmc-v, licensing]

- id: f06
  title: flex-lm 许可机制结构图——.ice 文件、ALUID/OTID、FlexLM 内嵌或外部
  type: structure
  source_pages: p16, p35-45, p76-77, p82
  source_chapter: OTMC Licensing principle / Licenses files installation / Post-installation wizard 1.6
  source_quote: |
    "The Flex-lm server can be embedded in the OTMC or installed on another server (which can be a virtual
    machine)." (p35)
    "the encrypted ALUID can be retrieved the Operating Sytem installation using the command:
    /usr/bin/getaluid" (p36，"Sytem" 为原文笔误)
    "When a new license file is copied into $LICENSES_HOME directory, the FlexLM service must be restarted
    to load this new file (service flexlmd restart)" (p42)
  summary: |
    许可四层结构：①许可文件 <license>.ice；②控制者 flex-lm 服务器——可内嵌 OTMC、也可装在另一台服务器（可以是虚机）；③绑定凭证——非虚拟化绑 ALUID（ALE 整机贴纸上有；仅购软件时用 /usr/bin/getaluid 取加密值），虚拟化绑 Aladdin USB dongle 的 dongle-ID（OTID/alchostid.cfg 见 p40 综合图）；④部署——post-install 向导内浏览选择（Skip 不中断安装但之后必须手工装），或手工 SFTP（otuser）拷入 $LICENSES_HOME（/var/data/licenses）后 service flexlmd stop/start，用 $FLEXLM_HOME 下 ./lmutil lmstat –a 核验。8770/OXE 各自的许可文件（.swk/.zip/hardware.mao/nmc.license8770 等）在各自系统部署（p38/p40 综合图、p42）。
  conditions: 向导 OK 状态只代表文件本地存在，有效性不校验（p77 Warning）
  tags: [structure, licensing, flexlm, aluid, dongle]

- id: f07
  title: 实验拓扑总图——ESXi 六虚机 + 客户端 PC + company.com DNS 域
  type: diagram
  source_pages: p21-32
  source_chapter: Topology for labs
  source_quote: |
    "ESXi Server settings • Host name: esxi.company.com • IP address: 151.1.1.250" (p23)
    "DNS domain name is 'company.com' … OXE-V: CS a: csa.company.com = 151.1.1.1, Main CS: csm.company.com
    = 151.1.1.3, Node name: oxe.company.com = 151.1.1.3 … OmniPCX Enterprise GD: gd.company.com =
    151.1.1.12 … OTMC-V: otmc.company.com = 151.1.1.60 … OmniVista 8770-V: nms.company.com = 151.1.1.70
    … FlexLM server VM: flex.company.com = 151.1.1.80 … Eco-System VM: eco.company.com = 151.1.1.100" (p31)
  summary: |
    实验口径（仅教学）：一台 ESXi（151.1.1.250/24，GW 151.1.1.254）上跑六虚机——OTMC（otmc，151.1.1.60）、FlexLM（flex，151.1.1.80）、OmniVista 8770（nms，151.1.1.70）、OXE-V（csa 151.1.1.1 / csm 151.1.1.3）、OMS（oms，151.1.1.13，CS main 151.1.1.3）、Eco-System（eco，151.1.1.100，Windows Server：DNS/Exchange/AD/LDAP/DHCP(移动用户)，DNS 指向自身 127.0.0.1）；外加 Windows 10 客户端 PC（client，151.1.1.10，DNS 151.1.1.100）。Eco-System 预置六用户（alban/adams/adore/barkley/backman/boop，密码均 1234，实验口径）。DNS 域 company.com 统一登记主机名（另含 gd.company.com=151.1.1.12）。OMS 与 GD 仅在拓扑/域名表出现，书中未展开用途与全称。
  conditions: 全部 IP/账号为实验口径；声明章（p92-94）示例网段漂移为 155.1.1.x（书内不一致，见 counter-example）
  tags: [diagram, lab, topology, dns, esxi]

- id: f08
  title: 安装资料与介质两条制法（DVD 全刻 vs SUSE 单刻 + USB 硬盘）
  type: structure
  source_pages: p49-52
  source_chapter: OTMC installation Overview / Installation
  source_quote: |
    "To install the OTMC server you need: • Boot DVD: SUSE Linux Enterprise Server (1 DVD) • OpenTouch core
    release installation package (1 DVD) • FAX server (1 DVD) • License files: OTMC and Fax (if used)" (p49)
    "Download all software ISO files from the BPWS • Only burn the SUSE Linux Enterprise Server ISO file and
    install the Operating System • Copy all ISO images on a USB hard drive" (p51)
  source_chapter_note: p49 另要求 OmniVista 8770 服务器（已装或装 8770 包，含 8770 与 Windows 2008 R2 Server 许可键）与客户信息（网络规划/基础设施/数据采集）
  summary: |
    安装物料清单：三张 DVD（SUSE 引导盘、OT core 包、FAX server）+ 许可文件 + 8770 侧物料 + 客户数据。介质制法两条：①全 ISO 刻盘逐台安装；②只刻 SUSE 引导盘，其余 ISO 拷到 USB 硬盘（软件从 BPWS 下载）。物理机安装流程链（p52）：OS 安装（分区/时区/重启）→ 部署软件包 → 重启 → OTMC post-installation；Note：RAID 必须在安装前配好、公司 DNS 必须先管理起来。虚机安装（p55-56）：装 ESXi → 装 vSphere 客户端 → 建 SUSE 64 位虚机 → 与物理机同一套 DVD、同一流程。
  conditions: ISO 下载源为 BPWS（书中未展开全称）
  tags: [structure, installation, media, dvd, usb]

- id: f09
  title: SUSE 安装三种模式与语义（硬件 / 虚拟化 / 单分区平滑升级）
  type: structure
  source_pages: p60-62
  source_chapter: OTMC installation How-To / 3 SUSE installation
  source_quote: |
    "OpenTouch Messaging Center (15000 users): OTMC deployment in GUI mode –Hardware – • OpenTouch Messaging
    Center for Virtualized Infrastructure (15000 users): OTMC deployment in virtualized infrastructure •
    OpenTouch Messaging Center first (15000 users, single partition): installation with a single partition
    (no second partition for smooth upgrade) even if the hard disk size is big enough for multi-partitioning" (p62)
  summary: |
    引导菜单三个安装项（都标 15000 users）：①OTMC——GUI 模式硬件部署；②OTMC for Virtualized Infrastructure——虚拟化基础设施部署（实验选此项）；③OTMC first——单分区安装（不留第二分区，即放弃平滑升级 smooth upgrade 能力，即便硬盘足够双分区）。安装设置（实验口径）：键盘 F2 选 us/fr-latin1；时区 + System clock uses UTC（示例 Europe/Paris）；安装约 25 分钟；完成后取盘重启。登录 root 默认密码 letacla1，随即强制改为 OtmcV01*（p60/p63）。
  conditions: 15000 users 为安装模式标注口径；硬件/软件规格仍以 feature list / product limits 为准
  tags: [structure, installation-modes, suse, partition]

- id: f10
  title: OTMC 虚机创建参数与 BIOS/ESXi 调优清单
  type: checklist
  source_pages: p58-59
  source_chapter: OTMC installation How-To / 1 OTMC virtual machine creation & 2 Configure BIOS parameters
  source_quote: |
    "Follow the chapter 6.2: 'Installing the OTMC virtual machine (OTMC-V)' • OS: SUSE Linux Enterprise Server
    12 (64bits) • Number of virtual sockets: 1 • Number of cores: 4 • Memory size: 4Gb • Select network
    adaptor: E1000 • Hard disk size: 250Gb • Thin provisioning" (p58)
    "In the 'Processor' options: disable 'hyper-threading' … From ESXi client, set the option Power Management
    Policy to High performance" (p59)
  summary: |
    OTMC-V 虚机规格（按安装手册 otmc2.6.1_im_InstalManual_8AL90120USAH_1_en 第 6.2 章，MyPortal 可取；实验口径——书中 Note 明说"requirements specified only for lab purposes，生产参数看安装手册"）：SUSE 12 64 位、1 虚拟插槽/4 核/4GB 内存/E1000 网卡/250GB 精简置备磁盘。调优两项：BIOS（F9 进 Processor 选项关超线程）与 ESXi 主机电源策略 High performance。
  conditions: 实验口径；生产部署参数以 MyPortal 安装手册为准
  tags: [checklist, vm-specs, bios, esxi, lab]

- id: f11
  title: Post-installation wizard 13 步站点配置骨架
  type: flow
  source_pages: p69-81
  source_chapter: OTMC Post-installation wizard (How-To)
  source_quote: |
    "1.1 Installation type … 1.2 Configure host system settings … 1.3 Network settings … 1.4 High Availability
    Parameters … 1.5 OTMC core settings … 1.6 Licenses Server settings … 1.7 Certificate … 1.8 Backup storage
    to select … 1.9 Summary overview … 1.10 System updates" (p69 目录)
    "This post installation wizard is automatically started at the first boot of the OTMC server (after
    software installation)." (p70)
  summary: |
    站点安装（site installation）13 步：①安装类型选 Installation from scratch；②主机设置（键盘/国家/公司名/时区+DST）；③网络（主机名小写、IP/掩码/网关/域、DNS 外部或本地转发器、NTP 外部或本地时钟；DNS 必须前向+反向解析七类 FQDN，见 principle p05）；④HA 参数（默认 Disable；启用需副服务器且两台同时跑向导）；⑤OTMC core 账户（root/maintenance/administrator/profile/SNMP，密码 ≥8 字符，用户名不得用保留名）；⑥许可服务器（Local 内嵌 / External 外部 + dongle 绑定规则）；⑦许可文件（Browse 选择或 Skip；OK 只代表文件存在）；⑧证书（课堂用通用证书、Network security OFF——官方明示不推荐）；⑨备份存储（LOCAL/USB/NFS；虚拟环境必须外置 NFS；落盘 bics.conf）；⑩摘要核对；⑪系统更新（无补丁选 NO）；Finish 后向导启动 OpenTouch 服务。另附手工装许可路径（p82，见 c02）。
  conditions: HA 只留指针（"explained in a dedicated chapter"，本书不含）
  tags: [flow, post-installation, wizard, site-installation]

- id: f12
  title: 8770 网络层级与节点编号规则（Network → Subnetwork → Node）
  type: structure
  source_pages: p85-87, p94-98
  source_chapter: OXE declaration / OTMC declaration
  source_quote: |
    "Subnetwork – Node number: Enter a numeric value equal to the ABC network*100 + OmniPCX Enterprise node
    number. Example: With an ABC network number = 1 and node number = 1, you must enter 101" (p87)
    "Node number is a free number. This node number must be different than OXE node numbers existing in the
    OXE network. (Use 99 for example)." (p95)
  summary: |
    8770 配置树三层：Network（自由编号）→ Subnetwork（编号必须等于 OXE 的 ABC 网络号）→ Node。OXE 节点号 = ABC 网络号×100 + OXE 节点号（实验：1×100+1=101，实验口径）；可用 siteid 命令或提示符括号 (101) 核对。OTMC 也声明为节点（Node number 自由、必须不同于网内所有 OXE 节点号——p94 实施写 98、p95 模板举例 99，两处口径见 counter-example），且必须与 OXE 呼叫服务器同子网（p94）。OTMC 侧拓扑对称：System services/Topology/OXE CS 下建 OXE CS network / subnetwork / OXE CS（名称与编号沿用 8770 侧定义）。
  conditions: OXE 节点在 OTMC 拓扑中可由 WBM 首登自动创建（OXE FQDN），未用 WBM 时手工声明（p96）
  tags: [structure, topology, node-number, 8770]

- id: f13
  title: OXE/OTMC 双向同步矩阵（complete/partial × separate/global × 发起侧）
  type: structure
  source_pages: p88-89, p100
  source_chapter: OXE declaration / 3 Synchronizing & OTMC declaration / 4 OTMC synchronization
  source_quote: |
    "Partial synchronization includes changes performed since the date of last synchronization for entries of
    the following types: Users, Directory, Data terminals, Speed dial numbers, Remote users." (p88)
    "Partial and complete synchronization are identical for OTMC node. (Partial and complete synchronization
    are different for OXE node)" (p100)
  summary: |
    同步两维度：类型（Partial=按上次同步日期增量同步用户/目录/数据终端/缩位拨号/远端用户；Complete=全量）与目标（Separate=仅所选节点；Global=所选节点+关联的 OXE/OpenTouch）。结果矩阵要点：从 OXE 节点发起，Partial+Global=OXE 增量+OpenTouch 全量；从 OpenTouch 节点发起，Partial+Separate=OpenTouch 全量（对 OTMC 而言 Partial 与 Complete 等价）；OTMC 与其挂接 OXE 互相 Global 时连带全量同步对方。上次同步时间查：节点 → Configuration 页签 → Data Collection 页签 → Date of last modification；OXE 同步日志 C:\8770\log\NMCSyncLdapPbx_1.log（p88）。
  conditions: OXE 侧 Partial 生效前提是 OXE 侧已打开目录实时同步（47xx directory – 4400 Synchro = True，p85）
  tags: [structure, synchronization, matrix, 8770]

- id: f14
  title: OXE 侧 SIP 对接参数结构（trunk group → external gateway → proxy/gateway/registrar/trusted → 全局）
  type: structure
  source_pages: p102-108
  source_chapter: OmniPCX Enterprise SIP configuration for OTMC (How-To)
  source_quote: |
    "Trunk Group Type: Select 'T2' type … Q931 Signal variant: Select ABC-F … T2 Specification: Select SIP" (p103)
    "Port number: 5040 … Transport type: TCP … Gateway type: ICE type" (p105)
    "Compression type: G 729 … Routing Optimisation: Yes" (p108)
  summary: |
    四段结构（8770 或 OXE mgr 均可配）：①SIP trunk group——ID 唯一（实验 1）、类型 T2、T2 Specification=SIP、Q931 变体 ABC-F、远端网络号须空闲且异于 OXE 网络号、节点号取 post-install 定义的值；本地参数 Dialing end to end=No、DTMF end to end=No（默认即对）；SIP 虚拟接入数默认 2（可改）。②SIP external gateway（OTMC 必须声明为外部 SIP 网关，Connection 用户由此访问 OTMC 的 SIP 服务）——Remote domain=OTMC FQDN、端口 5040、传输 TCP、Gateway type=ICE type、Ignore inactive/black hole 与 Contact with IP address 勾选、100 REL 出向 Supported 入向 Not requested。③SIP Proxy（认证 None）/SIP Gateway（远端网络号+trunk 组号、Subscribe Min Duration 600、本地 DNS 域）/SIP Registrar（最小/最大有效期）/SIP Trusted IP Addresses（必须含 OTMC IP）。④全局——编解码 G.729（多算法 False）、DPNSS 前缀（实验 D1234，优化中继转接）、Routing Optimisation=Yes。
  conditions: 空间冗余 OXE 需按 TC1652 另配外置信箱 SIP 网关（p105 Warning）
  tags: [structure, sip, trunk-group, gateway-5040, codec, menu-path]

- id: f15
  title: Connection 用户开通与话机寻址体系（两法建户 + resurrection/空闲地址/IP 静态 + 许可三族）
  type: structure
  source_pages: p109-118
  source_chapter: Connection user's creation for OTMC (How-To)
  source_quote: |
    "The resurrection method is used when no physical address is allocated to the set, in the OmniVista 8770
    management tool (shelf address=255, board address=255, equipment address=255). Resurrection consists in
    dialing the phone directory number & the password ('0000' by default) directly, from the set" (p113)
    "There are three main families of devices TDM … IP … SIP" (p117)
  summary: |
    用户侧结构：①建户两法——8770 的 OXE Configuration 接口（Users 右键 Create，General Characteristics 页签）或 Users 应用（Create user，含 OXE 属性与 OXE mailbox directory number 字段、OT applications=None 口径）；声明 OXE 用户时话机设备自动创建并分配（p112）。②寻址——数字/模拟话机用 resurrection（255/255/255 时空态下话机直拨分机号+密码 0000 即自动绑定真实物理地址；移机配合 In/Out of Service 前缀，ednump –l XXX 查前缀）或空闲地址表（System > Free addresses：UA 地址给 9 系、Z 地址给模拟）；IP 话机无物理地址（恒 255/255/255），静态 IP 经话机 i+# 菜单配（TFTP=呼叫服务器 main 地址），注册输分机号+密码 0000（p116，实验 DN 例 61020）。③许可核查三族六类（p117）：TDM——Z/模拟用户 L174、80x9→UA 高级话务 L173、4019 Connection 话务 L316；IP——80x8 高级 IP L176、4008/4018 Connection IP L317；SIP——L177。核查两法：8770 System/Software package 过滤（p117）或 OXE 侧 mtcl 登录跑 spadmin 看计数器（左=已用/右=可用，p118）。
  conditions: DHCP 服务器管理不在本培训内（p116 Note）；resurrection 密码默认 0000
  tags: [structure, users, addressing, resurrection, licensing, menu-path]

- id: f16
  title: 语音信箱对象模型——VMS → mailbox（必须挂 profile）→ user（Mailboxes/Licenses 页签）
  type: structure
  source_pages: p121-127, p134-141
  source_chapter: OTMC mailbox features & Voice mailbox configuration (How-To)
  source_quote: |
    "Before validating the mailbox creation, it's mandatory to assign a profile to the voice mailbox, in the
    « configuration » tab." (p139)
    "Thank's to the directory number, you will be able to make the link between the user set up on OXE and
    its OTMC account." (p136)
  summary: |
    三级对象：①VMS（语音邮件系统）——系统默认自带 defaultVmLS（Local Storage），路径 Services/Topology/VMS 核验（p137）；②mailbox（信箱）——Users and devices/Voicemail box 创建，General 页签定名/类型（Local Storage）/所属 VMS（defaultVmsLS），Configuration 页签必须选 profile 才能保存；③user（OTMC 账户）——Users and devices/User 创建，Contacts 页签分机号必须与 OXE 用户一致（31000/31001/31002，实验口径）+ 公司邮箱，Passwords 页签 TUI/GUI 密码（可选强制首次改 TUI 密码），Licenses 页签 MyIC Business Communications 与 Voice mail 必开（Messaging API 可选）；回 Users 的 Mailboxes 页签把信箱挂到人（搜索 VMB 选定）。另有三个核查视图：OTMC 节点 UsersAndDevices、OXE 节点 TelephonicDevices、用户 Mailboxes 页签（p136/p137-138）。
  conditions: 信箱可在建户时或建户后分配（p122）
  tags: [structure, object-model, mailbox, vms, menu-path]

- id: f17
  title: Voice mail profile 参数地图（General + Configuration 1/2/3 四页签）
  type: structure
  source_pages: p146-152
  source_chapter: Voice mailbox profiles (How-To)
  source_quote: |
    "Profiles called 'Advanced', 'Classic' and 'Simplified', dedicated to Local Storage. 'Standard' profile
    is dedicated to Unified Messaging." (p147)
    "Attendant call enabled: If enabled, the caller can decide to be routed to an attendant by dialing digit
    '0' while the greetings are played (also known as zero-out enabled)" (p149)
  summary: |
    profile 入口 /System services/Applications/Messaging/Voice Mail Profile；默认四个：Advanced/Classic/Simplified（LS 专用）+ Standard（UM 专用）。四页签：General（名称、类型 local storage/UM）；Configuration 1（行为——Answer only 三态 Yes/No/Manageable by users（默认）、Check quota、Announce time received、Skip memo、Direct callback、Callback voice prompt、Limited access、Extended absence greeting blocks message deposit、Record invitation、Keep call in system、Callback sender allowed、Propose options after message deposit（# 后 1 确认/2 复听/3 重录/0 求助）、Play a beep tone when recording（默认）、Attendant call enabled/zero-out）；Configuration 2（时长与密码——Maximum greeting/Max message recording/Max live record 秒数、TUI password management 三档 allowed/allowed but forbidden when expired/forbidden）；Configuration 3（容量与期限——Max size per mailbox MB（Check quota 关闭时不生效）、Aging of new/saved messages 天数、Warning（密码到期前提醒）、Accessible via network、Accessible via IMAP）。可自建（示例 my_profile 见 p151，实验口径）并在 Voicemail box 的 Configuration 页签分配（p152）。
  conditions: 无 mailbox 或未挂 profile 的用户，My Profile 里 TUI password management 落到 "allowed but forbidden when expired"（p149-150）
  tags: [structure, profile, parameters, zero-out]

- id: f18
  title: 问候语（Greetings）管理体系——四类问候 + 管理员 Greeting Managers 网页
  type: structure
  source_pages: p128-132, p142-145
  source_chapter: OTMC mailbox features / Greetings Management & Voice mailbox configuration 3.1/3.3
  source_quote: |
    "Solution : Greetings Management Web Interface for Administrators / Greeting Managers • Manage all
    existing greeting types per user • Activate a greeting for a user • Delete existing / Download existing /
    Upload new greeting files • Number of greeting managers is not limited" (p128)
    "A user can activate a maximum of 2 alternative greetings, only when the administrator has granted you
    the rights to use them." (p142)
  summary: |
    问候语四类（p131）：standard（姓名或分机号）、personal（内外线呼入可不同）、absence（长期离开，可阻止/禁用留言）、alternative personal（最多 2 条，须管理员授权；应对会议/午餐等周期场景）。管理三入口：①管理员 Greeting Managers 网页——经 8770 选 OT 节点右键 WBM（otAdmin 登录）→ Users and devices/Voice mail greetings management（再认证一次），按用户选人→上传/激活/下载/删除；②管理员 8770 侧 Voicemail box 的 Greetings 页签（问候类型/Extended absence-on/替代问候授权）；③用户侧——TUI 录制、My Profile 或话机 GUI 激活。细节外指 Quick Reference Guide "Managing your welcome greetings message" 章（p142）。
  conditions: OpenTouch MS/BE/MC 录音棚产出的专业 wav 可上传（p128 图示）
  tags: [structure, greetings, greeting-managers, wbm]

- id: f19
  title: 用户自助 Web 双应用——My Profile 与 MyMessaging 入口与功能区
  type: menu-path
  source_pages: p153-166
  source_chapter: OTMC web clients
  source_quote: |
    "Application available via a web browser using the following URL • https://<OpenTouch Messaging Center
    FQDN>" (p156)
    "Application available via a web browser using the following URL • https://<OpenTouch Messaging Center
    FQDN/MyMessaging> • or through the application 'My Profile'" (p165)
  summary: |
    两个自助应用：My Profile（URL = OTMC FQDN 根路径，GUI 登录）功能分区——按主题的用户设置、退出、保存/取消；语言与时区（TUI 语言/Web 语言/留言时区）；personal assistant 联系人与电话号码定制；语音邮件参数（激活问候语、信箱选项开关）；密码管理（TUI 密码与 My Profile 密码）；跳转 MyMessaging；SMTP/SMS 通知启用与定制。MyMessaging（URL = FQDN/MyMessaging 或经 My Profile 进入）——新/存留言列表（优先级、日期时间、主叫号码、时长、呼叫处理），播放可在 PC 或话机上执行，另有挂断/删除/刷新动作。
  conditions: 登录均用用户 GUI 账号；可见项受管理员授权（p191 Note）
  tags: [menu-path, web-clients, my-profile, my-messaging]

- id: f20
  title: SMTP/SMS 通知链路图——留言落箱 → Scorpio → 外部 SMTP → 邮件/短信
  type: diagram
  source_pages: p169-182
  source_chapter: SMTP/SMS notification（讲义）
  source_quote: |
    "SMTP Message with: E-Mail clients … Attached wav-file … Link to « My Messaging » web interface … MWI:
    Message Waiting Indicator — MWI on the phone set is not synchronized when reading the email" (p171)
    "SMS notification consists in sending an e-mail to the SMS gateway which is in charge of formatting and
    sending the SMS. • Only one SMS Gateway can be configured in the system" (p177)
  summary: |
    SMTP 链路：留言落箱 → OTMC（Scorpio 组件）→ 经 VPIM session 声明的路由发往外部 SMTP 服务器 → 用户邮箱收到邮件（附件 wav / My Messaging 链接 / 回呼发件人；另有满箱与近满箱告警邮件，阈值管理员定）；话机 MWI 亮灯但读邮件不灭灯。SMS 链路：留言落箱 → SMTP 通知（含信箱号/主叫号）→ SMTP-SMS 网关（系统仅一个，地址形如 SMS$号码$@company.com）→ GSM 网络 → 用户手机一键回呼信箱或主叫。功能可用性矩阵（p180）：短信/邮件通知 LS 与 UM 都有；wav 附件、My Messaging 链接、回呼、满箱/近满箱提醒仅 LS。配置权限矩阵（p181-182）：通知权与 LS 专属开关归管理员，启停开关与地址/号码双方可管（按授权）。
  conditions: 通知对象 LS 与 UM（Microsoft Exchange、Lotus Domino、Gmail）用户（p169）；SMTP 服务器必须无认证无 TLS（p174）
  tags: [diagram, notification, smtp, sms, scorpio, mwi]

- id: f21
  title: IMAP 访问链路——OTMC 即 IMAP 服务器（IMAPS/TLS 默认），邮件客户端直读留言
  type: diagram
  source_pages: p193-201, p207-208
  source_chapter: Voice mail box access via IMAP connection（讲义）& Voice Messages retrieval through IMAP（How-To）
  source_quote: |
    "IMAP4 used for direct consultation to mail server … POP3 used to retrieve all received emails" (p197)
    "BY DEFAULT, IMAPS IS ENABLED ON OPENTOUCH SIDE WITH 'TLS' SECURITY. THAT'S WHY YOU NEED TO MANAGE ON
    EMAIL CLIENT SIDE, THE SAME SECURED CONNECTION" (p208)
  summary: |
    原理：SMTP 发信，收信两协议——POP3 全量下载到本地、IMAP4 直连服务器查阅不落地；OTMC 充当 IMAP 服务器（留言落箱 → MWI 亮灯 → 邮件客户端以独立账户直读留言+附件）。场景：公司内网直连，外网经 VPN（p198）。配置三处对齐：①客户端（Outlook：手动账户，账户类型 IMAP，收件服务器=OTMC FQDN，发件服务器填真实邮件服务器 FQDN——OTMC 不是 SMTP 服务器，用户名/密码=GUI 凭证，Advanced 页签加密类型）；②OTMC 侧 System services/Topology/Physical servers/OT component/"IMAP4 Front End"——Connection security 与端口按安全类型自动带出，默认 IMAPS+TLS，改 SSL/无加密须改端口并 service imap4fed restart；③测试判据——"log onto incoming mail server (IMAP)" 为 Completed 才算配对；"send test e-mail" 失败属预期（无 SMTP 或误用 OTMC FQDN 作发件服务器）。
  conditions: 外网访问依赖 VPN（书中给图不给 VPN 配置）
  tags: [diagram, imap, imaps, imap4fed, outlook]

- id: f22
  title: General announcement 机制——三种播报场景 + 增强菜单与权限
  type: structure
  source_pages: p210-223, p225-227
  source_chapter: General announcement（讲义 + How-To）
  source_quote: |
    "The general announcement can be played for: • External calls in message deposit case • Internal calls in
    message deposit case … • Voice mail message consultation" (p213-214)
    "Enhanced Main Menu 1..6 — New messages / Send message / Read messages / Greetings menu / Personal
    options / General Announcement … General Announcement Menu 1 Listen / 2 Record / 3 Deactivate" (p218)
  summary: |
    机制四要素：①播报场景三类（外呼留言落箱、内呼留言落箱、信箱查询进菜单前），由管理员在 TUI global configuration 勾选，可多选（p216/p225；"arrive on AA" 选项为 OT 内嵌自动话务员时代遗留，外置 VAA 下无效）；②录制两法——wav 文件（音质最佳，适合品牌声音；放 /var/data 下专用目录并改名 general_announcement.wav，格式 CCITT A-law 8bits 8kHz mono）或任意话机 TUI 录制（灵活，适合常换）；③用户权限——"User has right to manage the general announcement"（8770 用户设置），授权后经增强菜单选项 6 进子菜单 1 听/2 录/3 停用；留言一经录制/上传即自动激活；④硬限制——同时仅一条、新录覆盖旧录、最长 5 分钟、仅支持 wav 的语言可用。
  conditions: wav 存放路径两处口径不一（p223 /var/data/general_announcement vs p227 /var/data/ics-group/general_announcement，见 counter-example）
  tags: [structure, general-announcement, tui-menu, branding]

- id: f23
  title: OpenTouch 备份恢复机制——8770 发起，SSH/SFTP 两段式，恢复后手工起服务
  type: flow
  source_pages: p228-238, p240-245
  source_chapter: OpenTouch Backup & Restore（讲义 + How-To）
  source_quote: |
    "The OmniVista 8770 Server establishes an SSH connection to the OpenTouch for running the backup command.
    Backup archive is created on the OpenTouch server. … The 8770 server retrieves the backup archive from
    the OpenTouch server via SFTP." (p231)
    "Enter the command service opentouchd start in order to restart the OpenTouch services … It takes less to
    5 minutes for the OpenTouch services to restart." (p245)
  summary: |
    备份链路五步（p231）：8770 Maintenance 发起 → SSH（维护账号）执行备份命令 → OTMC 上生成备份归档（临时目录 $BACKUP8770_HOME/<8770 FQDN>/save/<OT FQDN>.<时间戳 YYYY-MM-DD-hh-mm>/，内含 filelist.txt、ngvm3、.zip、.zip.md5、otbr.lock、version.txt，先打包 otarchive.tar.gz）→ 8770 经 SFTP 取回 → OTMC 侧临时目录删除。备份内容（p232）：OpenTouch 数据库（ESS/ICS/ACS/FAX/MOH）+ 特定数据（IP 配置、许可、证书、设备部署数据）。恢复链路：8770 经 SFTP 传回备份 → 停 OpenTouch 服务（service iced stop）→ 恢复 → 删临时文件 → 管理员手工 service opentouchd start（<5 分钟）；旧版本备份恢复到高版本要勾 Force。配置面：默认备份目录与阈值/保留期（Maintenance > Preferences > Maintenance >OT Configuration，默认 C:\8770_ARC\OTBackup；Record Life 由 Scheduler 每日清理）+ OT 节点 Maintenance 页签的维护账号（例 otuser/superuser，实验口径）。
  conditions: 虚拟环境备份目录必须外置 NFS（p79）；NFS server 部署按 TC2024（p246）
  tags: [flow, backup, restore, 8770, sftp]

- id: f24
  title: Voicemail statistics 机制——statistics.properties 参数结构 + 三格式输出
  type: structure
  source_pages: p247-258
  source_chapter: Voicemail statistics（讲义 + How-To）
  source_quote: |
    "Generation of output files in different formats in order to meet customer use cases, at configured
    frequency in a dedicated folder • XML … HTML … CSV" (p251)
    "Once the 'statistics.properties' file has been modified, don't forget to stop and start the masc
    service." (p258)
  summary: |
    统计闭环：配置文件 /var/data/ics-group/vms/ngvm3/statistics.properties（注释+加粗参数的 properties 格式）→ 按频率生成输出文件（XML/HTML/CSV）到指定目录 → 供客户侧应用消费。参数结构（p256）：总开关 enableStatistics（默认 disabled）、生成开关 enableStatisticsGeneration（默认 enabled）、输出位置 fileLocation、时间粒度 timeUnit（default 随频率：day→hour，month/week→day）、频率 frequencyGeneration（month/week/day）、dayGeneration（0-31 或 last day 或 monday-sunday）、生成时刻 timeGeneration、保留份数 historicSize（超限滚动覆盖，0 永不删）、xsltDirectory、删除数据保鲜期 freshness（ISO 8601 周期 PnDTnHnMnS）、frequencyGC（month/week/day/after generation/never）+ dayGC/timeGC。统计项按用户（p250）：登录名、电话号码、信箱 ID、信箱状态、留言总数/新留言/已听/已归档/已删。
  conditions: 输出目录须先手工创建并注意读写权限（p258 Note）；改完重启 mascd
  tags: [structure, statistics, properties, mascd]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-18）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 部署形态与容量口径决策 | 有 | f02, f03, f04, f05 | 定位/架构/连接组网/商业包与虚拟化；容量工具用法在书外（已注明） |
| task-02 | 实验拓扑搭建 | 有 | f07 | 六虚机 + DNS 域全景（实验口径） |
| task-03 | 许可证体系部署 | 有 | f06 | flex-lm 四层结构与核验路径 |
| task-04 | OTMC 服务器安装 | 有 | f08, f09, f10 | 物料介质、三种安装模式、虚机规格与调优 |
| task-05 | post-installation wizard | 有 | f11 | 13 步骨架 |
| task-06 | 手工装许可 | 有 | f06 | SFTP/flexlmd/lmstat 路径（操作细节在 case c02） |
| task-07 | OXE 准备并声明进 8770 | 有 | f12, f13 | 层级编号规则 + 同步矩阵（OXE 侧声明操作在 case c03） |
| task-08 | OTMC 声明与拓扑对置 | 有 | f12, f13 | 节点编号/同子网规则 + OTMC 拓扑对称结构 |
| task-09 | OXE SIP 对接 | 有 | f14 | 四段参数结构 |
| task-10 | Connection 用户与话机 | 有 | f15 | 建户/寻址/许可三族体系 |
| task-11 | OTMC 账户与信箱交付 | 有 | f16 | 三级对象模型 |
| task-12 | profile 定制 | 有 | f17 | 四页签参数地图 |
| task-13 | 自助门户 | 有 | f19 | 双应用入口与功能区 |
| task-14 | SMTP/SMS 通知 | 有 | f20 | 双链路图 + 可用性/权限矩阵 |
| task-15 | IMAP 访问 | 有 | f21 | 链路与三处对齐点 |
| task-16 | general announcement | 有 | f22 | 场景/录制/权限/菜单结构 |
| task-17 | 备份恢复 | 有 | f23 | 两段式机制链路 |
| task-18 | 语音信箱统计 | 有 | f24 | 参数结构与输出体系 |

补充说明：
- f01（课程主线）不对应单个 task，是 18 项任务的组织轴。
- 全部 18 项 task 均有框架类条目覆盖；逐分步操作序列（steps 级）归 case.md，数值逐格对照归 principle.md。
- 生产化边界提示（来自 BOOK_OVERVIEW 批判节）：硬件规格与产品上限→feature list/product limits；OTMC 虚机生产参数→MyPortal 安装手册 otmc2.6.1_im_InstalManual_8AL90120USAH_1_en；空间冗余 SIP→TC1652；NFS→TC2024；问候语细节→Quick Reference Guide。
