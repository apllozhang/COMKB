# 框架/流程/结构候选 — OXO Connect Starter (OXOCXTE300EN Ed16)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、硬件平台结构、平台/界面分区。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——实验环境 → 产品硬件 → 开通主干 → 业务深化 → 运维安全 → Rainbow 增量
  type: flow
  source_pages: p3-427
  source_chapter: 全书章节目录结构（TRAINING LAB / OFFER / SYSTEM STARTUP / … / RAINBOW / 培训收尾）
  source_quote: |
    "OXO CONNECT - R6.3 STARTER - EDITION 16 PARTICIPANT'S GUIDE" (p1)
    "OXO Connect is a phone system for Enterprises and Hotels with up to 300 users" (p24)
  summary: |
    课程按八段推进：①实验环境（RLAB 平台 + ITSP1 SIP 模拟器，p3-22）；②产品与硬件（Offer 介绍、
    IPBox/PowerCPU EE、数据采集，p23-49）；③系统开通（部署方案、启停、FTR、OMC、IP 修改、默认
    配置，p50-95）；④终端（话机全家桶、IP 话机、IP-DECT，p96-122）；⑤业务配置（编号计划、四种组、
    用户功能、语音信箱，p123-196）；⑥公共 SIP 中继与站点业务（SIP 网关、消息彩铃、呼入呼出管理、
    闭锁，p197-291）；⑦维护与安全（备份、软件下载、复位、防盗打，p292-329）；⑧Rainbow 集成（概览、
    接入、账户、网关、话务台，p330-426）+ 培训收尾与附注（p427-472，含 8328/8214 附加实验）。这是
    "先本体后云、先系统后业务、先配置后运维"的交付教学主线，也是现场项目的推荐顺序。
  conditions: 无特殊版本前提；主线之外的 p427-472 为培训收尾与硬件/启动/向导附注
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: RLAB 实验平台结构——POD 池 + 公共资源区 + POD 网络规划
  type: structure
  source_pages: p5-13
  source_chapter: TRAINING LAB ENVIRONMENT / Introduction & Training Platform & POD CONFIGURATION
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a
    data center." (p5)
    "Host name: Client1 • IP Address: 192.168.1.10 • Mask: 255.255.255.0 • Gateway: 192.168.1.254
    • DNS Server 1: 192.168.1.250" (p12)
    "IP address: 192.168.1.246 • Mask: 255.255.255.0 • Gateway : 192.168.1.254 • DNS Server 1:
    192.168.1.250" (p13)
  summary: |
    实验平台两层：POD 1..n 相互独立、配置相同，可访问公共资源；每个 POD 含 Windows 11 客户端虚机
    （OXOC_PC_CLIENT，IP 192.168.1.10/24，实验口径）与 OXO Connect Evolution（IP 192.168.1.246），
    共用网关 192.168.1.254 与 DNS 192.168.1.250；公共资源区（Subnet 0，10.20.30.x）放 NAS（软件、
    许可）、SIP 模拟器（12.0.0.2）与外部 DNS（10.20.30.250）。客户端虚机预装 4 个 MicroSIP（分机
    100-103）+ 2 个模拟公号 MicroSIP，另需自装 IPDSP（用分机 104）；NAS 经网络盘 'OXOC' 与桌面
    SOFTS OXO CONNECT 目录提供软件，'Sharing' 盘与讲师交换文件。
  conditions: 仅培训环境（RLAB）；所有 IP 为实验口径；POD 间互不可见
  tags: [structure, lab, rlab, topology]

- id: f03
  title: IPDSP 安装前置顺序——先改 IP 再装软话机（时间同步）
  type: flow
  source_pages: p14
  source_chapter: INSTALLING THE IPDSP
  source_quote: |
    "1. OXO Connect Change IP settings 2. PC Change IP settings 3. Set date & time … 4. IPDSP
    installation" (p14)
    "Otherwise, if there is a time difference between the PC and the OXO system, the IPDSP will not
    be able to start. • An error message related to loading the lanpbx file will appear. • This is
    due to the use of digital certificates (the IPDSP uses the HTTPS protocol)." (p14)
  summary: |
    四步顺序：①改 OXO Connect IP；②改 PC IP；③PC 日期时间设置里把"自动设置时间"关掉再打开
    （强制与 NTP 重新同步）；④核对日期时间后安装 IPDSP。原因链：IPDSP 走 HTTPS 证书校验 → PC
    与 OXO 时间差会导致证书时间无效 → lanpbx 文件加载报错。这是"时间不同步引发证书失败"的典型
    排障入口。
  conditions: 新装 IPDSP 或 IP 大改后；生产环境同样适用于证书校验类故障排查思路
  tags: [flow, ipdsp, certificate, time-sync, troubleshooting]

- id: f04
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则
  type: diagram
  source_pages: p17-21
  source_chapter: SIP CARRIER SIMULATOR / Overview & Public numbers & CALL TO YOUR PBX & SIP OXO CONFIG
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 … ITSP1 Public gateway public.itsp1.com
    10.20.30.50 … SIP domain: sip.itsp1.fr / itsp1.fr" (p17)
    "210P41000 Installation number • 41100 to 41199 base 100 DDI subscribers • 41000 base 9 DDI
    Operator group" (p21)
  summary: |
    模拟器在 RLAB 公共区扮演出局运营商，两条腿：SIP 网关 gateway1.itsp1.com（PBX 注册账号
    pbxP/alcatel，SIP 域 sip.itsp1.fr）与公网网关 public.itsp1.com（两个 MicroSIP 模拟 Public/
    Urgence 两个 SIP 用户，仅入呼叫）。号码规则（PN=两位 POD 号）：国内 33{1-5}1PN12345、移动
    3361PN12345/3371PN12345、国际 4421PN12345、紧急 112/15/17/18，Public 主号 3321PN12345；呼出
    时 PBX 把 0110312345 变换为 +33110312345 送出。呼入本 PBX：安装号 3321PN41000，DDI 段
    41100-41199（分机 100 即 3321PN41100），话务员组基 9 的 41000；本 POD 回环拨 0210341102 或
    33210341102。OXO 侧 SIP 网关名 ITSP1G1，Outbound Proxy 指向 gateway1.itsp1.com，DNS A 记录
    192.168.1.250。
  conditions: 实验口径（RLAB 专用）；所有账号/号码/IP 均为教学约定值
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f05
  title: OXO Connect 产品家族与硬件平台——四平台两 CPU 线
  type: structure
  source_pages: p23-34
  source_chapter: Offer introduction / Communication servers / OXO hardware
  source_quote: |
    "OXO Connect is a phone system for Enterprises and Hotels with up to 300 users" (p24)
    "OXO Connect Compact • Compact rack with a PowerCPU EE … OXO Connect Small • 1U with a
    PowerCPU EE … OXO Connect Large • 3U with a PowerCPU EE" (p34)
    "IP Pure IP – 300 users … Hybrid TDM/IP - 300 users … Pure TDM VOIP optional" (p26)
  summary: |
    家族结构：OXO Connect Compact（PowerCPU EE 紧凑机架）、Small（1U）、Large（3U）三档 PowerCPU
    EE 机箱，加 OXO Connect Evolution（IPBox，纯 IP）；另有 OXO Connect（PowerCPU-EE）混合 TDM/IP
    与 Compact 纯 TDM（VOIP 可选）形态。定位 ≤300 用户、24/7 虚拟前台、认证证书 RSA 2048/4096 位。
    硬件家族含以太网口、WLAN、IP DECT、Rainbow（WebRTC）、OV8770 网管等生态（p28 商用提案图）。
  conditions: 无版本前提；商用许可以报价单为准（书内只给结构）
  tags: [structure, hardware, product-family, oce]

- id: f06
  title: IPBox（OCE）接口与安装形态——ETH0/ETH1 分工
  type: diagram
  source_pages: p30-32
  source_chapter: OXO hardware: IPBox / IPBox for OXO Connect Evolution / IPBox installation
  source_quote: |
    "2 Ethernet ports ETH0: LAN & POE ETH1: For Instant Management access on site (DHCP , DNS)" (p31)
    "The PoE has to be activated on OmniSwitch side, before "zerotouch" can be performed with IP-Box" (p32)
    "OCE can be installed as well as desktop, wall mounted or rack product (1/2 of 19" form factor, 1U)" (p32)
  summary: |
    IPBox 接口：Micro USB 控制台口、USB（工厂保留）、RJ45 AFU 辅助功能口、双以太网口（ETH0=LAN
    与 PoE 供电、ETH1=现场即时管理口，自带 DHCP/DNS）、电源按键与双色 LED（监视启动/运行/云连接/
    告警）、背面 SD 卡槽（可选备份）。安装形态：桌面/壁挂/机架（半宽 19 英寸 1U）；零接触部署前提
    是 OmniSwitch 侧先开 PoE。
  conditions: IPBox 专属；PoE 前提为零接触安装条件
  tags: [diagram, hardware, ipbox, eth1, poe]

- id: f07
  title: PowerCPU EE 硬件结构——CPU 规格、子板与 DSP 通道扩展
  type: structure
  source_pages: p33-39
  source_chapter: Hardware with PowerCPU EE / PowerCPU EE details / daughter boards / DSP channels
  source_quote: |
    "Processor MPC8377 @ 800 MHz • DDR2 512 MB RAM running at 400 MHz • LAN Ethernet port
    10/100/1000 MB/s • 16VoIP resources (1 DSP TMS320C6421) … MSDB is by default equipped with a
    8GB eMMC flash memory" (p35)
    "The maximum number of DSP channels is extended from 60 to 76 when using the Armada 64" (p37)
  summary: |
    PowerCPU EE：MPC8377 @800MHz、DDR2 512MB @400MHz、千兆 LAN、16 VoIP 资源（1 片 TMS320C6421）、
    2MB NOR 引导、MSDB 子板默认 8GB eMMC。可装子板：AFU-1（通用铃/门铃/背景音乐/告警/扬声器/请
    稍候）、HSL1/HSL2（连 PowerMex）、Mini-Mix 2xT0+2Z（仅 Compact）、Armada 32/64（VoIP 资源）。
    DSP 通道表：无子板 16 全 G711/G729；+Armada 32=48；+Armada 64=60 多编解码，或 30 G711/G729 +
    46 G711 合计 76。CPU 槽位在任何机架都固定为 CPU slot。
  conditions: PowerCPU EE 平台；76 通道模式受 VoIP Channels mode 设置约束（OMC 可选两种配比）
  tags: [structure, hardware, powercpu, dsp, armada]

- id: f08
  title: 多机柜互连结构——HSL 链路与 5 米限制
  type: diagram
  source_pages: p42
  source_chapter: Additional racks installation
  source_quote: |
    "Up to 3 racks can be interconnected using HSL links • The HSL link connects the PowerCPU EE to
    the PowerMEX board • The maximum length between the master rack and the extension rack is
    5 meters" (p42)
  summary: |
    PowerCPU EE 多机柜：最多 3 个机柜经 HSL 链路互连；HSL 连接 PowerCPU EE 与 PowerMEX 板；主柜
    到扩展柜最大 5 米。接线为 8 针（TX+/TX-/RX+/RX-）。这是 TDM 扩容的物理边界——不是以太网级联。
  conditions: PowerCPU EE 平台（IPBox 无机柜扩展）
  tags: [diagram, hardware, hsl, multi-cabinet]

- id: f09
  title: OCE 启动与服务口（ETH1）设计——FTR 入口与安全边界
  type: structure
  source_pages: p56-58
  source_chapter: Start & Stop the system / OXO Connect Evolution: Serviceability
  source_quote: |
    "Eth1 is configured with a fixed IP address and an active DHCP server • Fixed IP address:
    192.168.94.246 • Netmask: 255.255.255.0 • Gateway: 192.168.94.1 • DHCP range: 192.168.94.247,
    192.168.94.254 • DHCP lease: 2 hours" (p57)
    "Security warnings: • Eth1 MUST not be connect on the LAN • No access to Eth0 LAN is allowed
    from Eth1. • Eth1 can be disabled in OMC. • Eth1 is disabled in case of IP conflict with Eth0" (p57)
    "Short push (< 5 s) = start / restart • Long push (> 5 s) = shut down … Fast Flashing GREEN :
    "LOLA" mode" (p58)
  summary: |
    ETH1 是 FTR 与现场配置的专用口：固定 IP 192.168.94.246/24、网关 192.168.94.1、DHCP 池
    .247-.254（租期 2h）、本口 DNS；URL 或 OMC 里用 myipbox.ale 直连；仅允许配 ETH0 参数与 Webdiag
    诊断，需 installer/operator/manufacturer 身份，不允许用户应用。安全边界四条：不得接入 LAN、
    Eth1 不能访问 Eth0 侧 LAN、可在 OMC 禁用、与 Eth0 IP 冲突时自动禁用。电源按键语义：<5s 短按
    启动/重启、>5s 长按关机（PoE 后级 DC/DC 断电）、按住接 PoE 直至 LED 快闪绿=LOLA 模式；双色
    LED 状态表覆盖 OFF/红常亮/绿常亮/红慢闪（关机中）/红快闪（重启）/绿慢闪（Linux 运行）/绿快闪
    （LOLA）。ISP 的 SIP 网络也可直连 ETH1，两子网间路由提升安全性。
  conditions: OCE（IPBox）专属；PowerCPU EE 启动流程另见 p436-438 八步监控
  tags: [structure, oce, eth1, ftr, led, startup]

- id: f10
  title: 两种部署方案——Cloud Connect 六步 vs Standard 四步
  type: flow
  source_pages: p51-55
  source_chapter: OXO Connect deployment solutions / "Cloud Connect" solution / "Standard" Solution
  source_quote: |
    "OXO Connect Cloud Connect solution: • Auto registration on Cloud Connect Standard Solution:
    • On-site management with OMC" (p51)
    "Standard … Connect with the OCE default IP address: • 192.168.92.246 … 4 • Upload the 2
    Licences in the OCE • .msl & .csl" (p55)
  summary: |
    Cloud Connect 路线六步：①开箱接客户 LAN（即插即用：IP 配置+Installation Id）→②自动连云→③
    软件与许可自动下载→④现场或远程管理（防火墙友好）→⑤全机队 Web 化分析/资产→⑥云端自动更新。
    Standard 路线四步：①装 OMC→②用默认 IP 192.168.92.246 连接→③上传软件→④上传两把许可
    （.msl 主钥匙+.csl CTI 钥匙）。选型：有云条件走 Cloud Connect（后续升级/资产免维护），否则
    Standard 全现场。
  conditions: Cloud Connect 依赖客户侧出网与 Cloud Connect 服务开通
  tags: [flow, deployment, cloud-connect, standard, licensing]

- id: f11
  title: FTR 首次注册流程（Web 页面版）
  type: flow
  source_pages: p59-62
  source_chapter: OCE Start-up & first Time Registration (FTR) — How To
  source_quote: |
    "To register the OCE on Cloud Connect, open the web browser and enter as URL: 192.168.94.246
    (ETH1)" (p61)
    "Login: installer Pwd: pbxk1064 At the very first time, the system asks to put a new password,
    put Alcatel1 during the training" (p61)
    "The system registers in the Cloud … Licenses are downloaded from the Cloud … The system is
    updated … The system becomes accessible remotely via OXO Connectivity and the Fleet Dashboard" (p62)
  summary: |
    流程：①ETH0 接 PoE 交换机、ETH1 接管理 PC（仅课堂可做，虚课不能——见 c01）；②浏览器开
    192.168.94.246 → Register → installer/pbxk1064（实验口径）→ 强制设新密码；③录入 IP 配置
    （ETH0 192.168.1.246/24、网关 .254、代理 .254:3128、DNS .250）与三参考值：Partner fleet
    reference=OXOP、Partner sub-fleet reference=TRAINING、Installation reference=LAB（实验口径）；
    ④PC 切 DHCP；⑤点右下角 V 提交。结果四项：注册入云、许可自动下载、系统更新、Fleet Dashboard
    远程可达。
  conditions: 仅物理课堂；虚课用 OMC 常规连接改 IP 配置替代
  tags: [flow, ftr, cloud-connect, oce]

- id: f12
  title: OMC 模式体系——六类入口与连接方式
  type: structure
  source_pages: p63-67
  source_chapter: OMC management tool / Installation OMC / Welcome screen / Connection modes / Authentication
  source_quote: |
    "Data Collection and Tools: … Installation Typical: Execute an installation wizard …
    Modification Typical: … Multi site: … Expert: Access to the system configuration manually or
    by wizard" (p65)
    "Default IP Address: 192.168.92.246 • Default Password: pbxk1064 (First connection)" (p67)
  summary: |
    OMC 欢迎屏六入口：Data Collection and Tools（不连系统跑采集向导/迁移/软件下载/批量下发）、
    Installation Typical（首装向导/载入采集）、Modification Typical（改库向导）、Multi site（多站
    点）、Expert（手工或向导全功能）。连接方式：V24 串口、modem 远程（首连后挂断回拨）、LAN/WAN
    （PC 与 OXO 同网段，故障先查 PC IP）。认证：Installer 模式+密码；默认 IP 192.168.92.246、首连
    密码 pbxk1064（实验口径，仅首次）。OMC 软件从 MyPortal 下载，首装 PC 需 Dotnet Framework
    （PIMPhony 包内含）。
  conditions: OMC 全版本适用；版本需与 PBX 软件配套（见 p318 下载清单）
  tags: [structure, omc, connection, authentication]

- id: f13
  title: OMC 服务器认证机制——证书校验与告警链
  type: structure
  source_pages: p68-69
  source_chapter: Server authentication
  source_quote: |
    "OMC checks system certificate to authenticate the server that it connects to … Controlled by
    flag 'Server authentication', enabled by default … Connection online icon is displayed in OMC
    status bar, bottom right: Green (Authenticated), Red (Unsecure)" (p68)
    "In case of invalid certificate, an alarm is generated • Urgent alarm in the history file, can
    be reported to OmniVista 8770 • Email sent to the 8770 administrator … the certificates
    management is done through Webdiag installer session" (p69)
  summary: |
    机制四要素：①OMC 连接时校验系统证书（自签或 CA 签），旗标默认启用、可按连接勾选，不信任即
    断连，LAN/WAN 皆适用；②状态栏图标绿=已认证/红=不安全；③证书须装入 PC"受信任的根证书颁发
    机构"存储区，OXO 侧检查证书名与有效期；④无效证书产生紧急告警：历史文件告警可上报 OmniVista
    8770 并邮件通知 8770 管理员；OXO 侧证书管理在 Webdiag（installer 会话）。
  conditions: 全连接类型适用；命令行模式亦可启用
  tags: [structure, omc, certificate, security]

- id: f14
  title: OMC 软件钥匙体系——.msl 与 .csl 双钥匙
  type: structure
  source_pages: p71
  source_chapter: Software keys
  source_quote: |
    "The software keys are linked to the Main CPU serial number … The main key f103f217.msl is
    imported thanks to the first import key button • The CTI key f103f217.csl is imported thanks
    to the import key button below • The apply button transfers the software key in the system •
    The Details button shows the services opened by the software keys." (p71)
  summary: |
    软件钥匙与主 CPU 序列号绑定；保存客户库时钥匙随库保存。导入路径 OMC/Modification typical/
    System/Software key：主钥匙（.msl）走第一个导入按钮、CTI 钥匙（.csl）走下方导入按钮，Apply
    把钥匙送入系统，Details 显示钥匙开启的服务。文件名中的 f103f217 即序列号示例。
  conditions: Standard 路线必需；Cloud Connect 路线由云端自动下发（p62）
  tags: [structure, licensing, omc, software-keys]

- id: f15
  title: 默认配置行为集——话务台/动态路由/信箱/传真/Hotel 预置
  type: structure
  source_pages: p87-93
  source_chapter: Default configuration（六页讲义）
  source_quote: |
    "The operator station by default is the 1st equipment of the 1st set board detected …
    automatically put into attendant groups 1 and 2 and in the default attendant group 8" (p89)
    "Users (internal and external calls) directed to the voice mail after 12 seconds • Operator
    calls to the default operator group (N°8) after 24 seconds" (p90)
    "Default IP Addresses • Main CPU: 192.168.92.246 • Subnet mask: 255.255.255.0 • Default
    gateway: 192.168.92.1" (p93)
  summary: |
    启动后板子从 slot 1 起逐个识别（UAI 常在 slot 1），所有话机获默认 profile，新加话站（非 IP）
    即刻可用（IP 话机走自动配置）。默认话务台=第 1 块话机板第 1 台（建议接 8039），自动入话务台组
    1/2 与默认组 8；Manager/Assistant 默认 Assistant=设备 2、Manager=设备 3（须 multiline）。动态
    路由默认：内外呼叫 12 秒转信箱、话务台呼叫 24 秒转组 8（VM 接入编在默认组=自动话务员）。信箱：
    每话机默认有、首次需定制。预定义传真=第 1 块 SLI 板第 1 设备（Fax 2/3 服务、动态路由不激活、
    防插入/防驻留/警示音保护/禁会议）；Hotel 版预置：电话亭=SLI 第 2 设备、管理话机=全部数字话机、
    房间=其余模拟设备。编号与后缀随国家预置（分机 100 起、9 话务台、0 主中继组、60/61 等后缀）；
    主中继组自动收编第 1 块外部接入板第 1 设备（APA/T0/T2/DLT2）。查版本：话机 Menu/System/Version
    → ONEFR03x/xxx.yyy。默认 IP：192.168.92.246/24 网关 192.168.92.1。
  conditions: 出厂/冷复位后的状态；部分项（Manager 组、Hotel 预置）在跑过安装向导后才生效
  tags: [structure, default-configuration, attendant, voicemail]

- id: f16
  title: 四层拨号计划框架——公共/专用/内部/会话中
  type: structure
  source_pages: p123-128
  source_chapter: Dialing Plans / Default Dialing Plans / Dialing Plans modification / bases
  source_quote: |
    "PUBLIC DIALING PLAN … PRIVATE DIALING PLAN … INTERNAL DIALING PLAN … FEATURES IN CONVERSATION
    IN CONVERSATION" (p124)
    "Star type: the prefixes to activate a function are preceded by « * » and cancellation prefixes
    by « # » with 2, 3 or 4 digits • Standard national type … Three-digits default Dialing Plan" (p125)
    "DDI number 41100 – Base 100 … Directory number 100 – Base 100 … Private directory number 8800
    – Base 100" (p128)
  summary: |
    OXO 拨号四层：公共（DDI）→专用（私网）→内部（分机）→会话中功能（后缀）。默认计划两种风格：
    星号型（* 激活、# 取消，2-4 位）与国内标准型；OXO 默认三位。修改入口：默认计划选择在安装向导
    或 OMC\Numbering\Default configuration；前缀增删改 OMC\Numbering\Numbering Plans（下拉选功能、
    填起止前缀、必要时填 Base）；后缀 OMC\Numbering\Feature in Conversation。Base 是内外映射基数：
    DDI 41100 base 100 ↔ 分机 100；私网号 8800 base 100。
  conditions: 默认三位计划；改计划前先排冲突（见 c06）
  tags: [structure, numbering, dialing-plan, base]

- id: f17
  title: 固定 Base 的功能前缀表——代接与前转两族
  type: structure
  source_pages: p129-130
  source_chapter: Dialing Plans bases for prefixes / Installation number
  source_quote: |
    "Pick up: 0: for handset pickup 1: for group pickup 2: to answer a general call 3: for parked
    call retrieval" (p129)
    "Forwarding: 0 cancel all call diversion types 1 immediate diversion 2 diversion on busy 3 do
    Not Disturb 4 diversion on paging 5 forward group call 6 join into a group 7 group withdraw 8
    forward Calls type diversion (follow-me) 9 canceling Forward Calls type diversion 10 selective
    diversion" (p129)
    "Enter the installation number without the first digit • OMC\ Numbering\ Installation Numbers" (p130)
  summary: |
    两族前缀的 Base 固定不可改：Pick-up 族（0 本机代接/1 组代接/2 应答普通呼叫/3 取驻留，另有
    Pickup Parked Call 前缀 base 0）；Forwarding 族（0 取消全部/1 立即/2 遇忙/3 免打扰/4 寻呼/
    5 组前转/6 加入组/7 退组/8 follow-me/9 取消 follow-me/10 选择性）。安装号=主系统 DDI 号，
    去掉第 1 位录入，入口 OMC\Numbering\Installation Numbers 或安装向导。
  conditions: Base 值为系统固定语义，配置时只能选前缀段不能改 Base 含义
  tags: [structure, numbering, prefix, pickup, forwarding]

- id: f18
  title: 编号计划冲突处理范式——先删旧段再建新段
  type: flow
  source_pages: p131-135
  source_chapter: Setting up the numbering plan — How To
  source_quote: |
    "Subscriber range from 200 to 299 already exists. To avoid conflicts, remove these prefixes" (p132)
    "A range prefixes (from 400 to 434) already exists for secondary trunk groups. To avoid
    conflicts, delete this Secondary Trunk Group … All the prefixes beginning by 6 must be deleted
    before!" (p135)
    "Base Always a number from 0 to 2199" (p135)
  summary: |
    建新前缀段的标准范式：①打开 OMC\Numbering\Numbering Plans；②查与新段冲突的既有段（如
    Programming Mode 段 200-299、Secondary Trunk Group 400-434、Appointment 前缀 60）→选中删除；
    ③下拉选目标功能、填起止与 Base → Add → OK。Base 约束 0-2199。该范式适用于一切前缀/后缀调整
    （缩位拨号、代接、编程模式等）。
  conditions: 修改编号计划前；删除既有段前确认无业务依赖
  tags: [flow, numbering, conflict, omc-path]

- id: f19
  title: Hunt group 三种分发模式与保留组
  type: structure
  source_pages: p137, p143-145
  source_chapter: Groups management / Setting up a hunting group
  source_quote: |
    "Sequential: All calls are routed to the 1st group member, 2nd member, …etc Circular: Calls are
    routed to each member of the group in a circular rotation until the call in answered Parallel:
    All Group members ring simultaneously" (p137)
    "Warning: the group 500 is used by the voice mail server!" (p143)
  summary: |
    Hunt group=多话机共用一号，按类型分发：Sequential（逐个）、Circular（轮转直到接听）、Parallel
    （齐振）。配置路径 OMC/Hunting groups → 选组 → Details → 命名/加成员/选类型。保留组：500 被
    语音信箱服务器占用（VM 端口组），实验与实施都从 501 起（编号计划预置 hunt group 500-525）。
  conditions: 组号范围与编号计划相关（默认 500-525）
  tags: [structure, groups, hunt-group]

- id: f20
  title: Pick-up group 与 Group pickup 可编程键
  type: structure
  source_pages: p138, p146-150
  source_chapter: Groups management / Setting up a pick up group
  source_quote: |
    "When one phone in a pre-defined group is called, any group member can pick up the call by
    dialing the interception prefix or pressing a specific soft key" (p138)
    "Keytype: Function key • Keyfunction: Pickup … Select: Group" (p150)
  summary: |
    代接组：组内任一成员可接听组内他人来电，经代接前缀（base 0 本机/1 组）或按键。配置两段：
    ①OMC/Pickup groups → 组 1 → Details → 加成员；②每组员话机建键：OMC/Subscribers–BaseStations
    list → 话机 Details → Keys → 空键 → Function key → Pickup → 命名 → 作用域选 Group。测试：
    呼组内 A、振铃时组内 B 按键代接。
  conditions: 组代接前缀 base 固定为 1（f17）
  tags: [structure, groups, pickup, keys]

- id: f21
  title: Broadcast group 发送/接收权限与 Grb 配对
  type: structure
  source_pages: p139, p151-153
  source_chapter: Groups management / Setting up a broadcast group
  source_quote: |
    "The noteworthy address PairedGrb allows to pair up to 2 broadcast groups, thus allowing up to
    64 members" (p139)
    "Attribute The members of the group may call the group (send) or be rung (receive) or both
    (send/rec)." (p153)
    "Warning: To receive, a deskphone must have a loudspeaker." (p152)
  summary: |
    广播组：成员按权限分 send/receive/send+rec，发送方拨组号即可在接收方扬声器播音。约束：接收话机
    必须有扬声器； noteworthy 地址 PairedGrb 可配对至多 2 个广播组、合计 64 成员。配置 OMC/
    Broadcast group → 组 1 → Details → 加成员并设权限、命名。虚课无扬声器话机时用 IPDSP 接收 +
    MicroSIP 广播替代。
  conditions: 默认广播组 1 呼叫号 *2（实验口径）
  tags: [structure, groups, broadcast]

- id: f22
  title: Manager/Secretary 组与三个监督键
  type: structure
  source_pages: p140, p154-156
  source_chapter: Groups management / Setting up a manager/secretary group
  source_quote: |
    "Manager • RSL secretary • Screening • Secretary supervision … Assistant • RSL manager •
    Screening • Manager supervision Programmable keys" (p140)
    "Create a manager/secretary group, the two sets must be multiline sets." (p155)
  summary: |
    经理/秘书组：双方必须 multiline 话机（加键模块更有用），互相持有对方 RSL 键、Screening 键、监督
    键。配置 OMC 中 Manager-Secretary Relations → Add → 选经理/秘书分机 → 设置 Screening/RSL/
    Supervision 键；Screening 激活键可改。测试：激活经理侧滤键后呼经理、激活秘书侧滤键后呼经理、
    测 RSL 与监督键。
  conditions: 需两台 multiline 话机，虚课无法测试
  tags: [structure, groups, manager-secretary]

- id: f23
  title: 三类可编程键体系与默认键 profile 对照
  type: structure
  source_pages: p160-163
  source_chapter: User's Features / Keys / Keys management / Key Profiles
  source_quote: |
    "3 types of Keys are available on OXO Connect • Call keys • Feature keys • Resources keys" (p160)
    "General resources (RGM): To manage incoming and outgoing , internal and external calls
    Dedicated resources (RSL, RSP , RSB, RSD): …" (p161)
    "Type of subscriber Normal Mode Single line Key system PCX … 3 « virtual » resource keys …
    2 RGM n RSP … 2 RGM 2 RSB" (p163)
  summary: |
    键三类：呼叫键（直呼预存号码、用户可改）、功能键（激活功能：VM/转移/代接/会议等）、资源键
    （multiline：RGM 通用收发、RSL 本地、RSP 特殊物理接入、RSB 中继组、RSD DID 监视、监督键）。
    配置统一在 OMC\Subscribers-Basestations List → Keys。默认键 profile 由话机型号/模式（key system
    或 PCX）/用户类型决定：Single line=3 虚拟资源键、1 通话+1 保持+1 驻留；key system=2 RGM+n RSP、
    (n+1) 保持+驻留；PCX=2 RGM+2 RSB、3 保持+驻留；n=模拟线数与 B 通道数（受话机键数上限约束）。
  conditions: 资源键仅 multiline 话机有意义；详见 Expert 文档 User services/Resource key
  tags: [structure, keys, multiline, profiles]

- id: f24
  title: 动态路由两级两计时框架与级联
  type: flow
  source_pages: p164-166
  source_chapter: User's Features / Dynamic routing & cascading
  source_quote: |
    "Allows to forward automatically an incoming call (internal or external), according two levels
    and two timers. … TIMER 1 ex: 12s … TIMER 2 ex: 15s … LEVEL 2: ATTENDANT" (p164)
    "Timer 1 for level1: Up to 3276 seconds … Destination No: Hunt group or User/Subscriber or
    Common/Collective speed dialing number (default destination is Voice mail Hunt group)" (p165)
    "Dynamic Routing cascading is supported for subscribers and Hunting groups • Maximum value
    allowed: 5" (p166)
  summary: |
    久叫不应框架：T1（示例 12s）到→转 LEVEL 1 目的地；T2（示例 15s）到→转话务台（General level=
    活动话务台组，可带 General bell、仅外线）。配置 OMC\Subscribers-Basestations List → Dyn Rout：
    AA lev1/lev2 复选（目的地是否经自动话务员）、计时器最大 3276s、不勾计时器但有目的地=立即转、
    目的地可为 hunt group/分机/集体缩位（默认 VM 组）。总开关：不勾 "apply diversion" 则一切转移
    （含用户自设前转）禁用。级联：被转对象自己再走动态路由，支持分机与 hunt group，系统参数最大
    级数 5（示例配 3）。
  conditions: 级联最大值受系统参数 "Maximum Number of Dynamic Routing Cascading Levels" 限制
  tags: [flow, dynamic-routing, timers, cascading]

- id: f25
  title: 语音信箱体系——容量报价、访问模式与三种信箱
  type: structure
  source_pages: p183-189
  source_chapter: Voice Mailbox basic services（七页讲义）
  source_quote: |
    "Voice mail is integrated in CPU … 1 hour of stored messages … Up to 120 seconds … Additional
    ports (up to 8) • Additional message storage time and languages • 4 hours • 30 hours • 200h" (p183)
    "Consultation in APPLICATION Mode … Consultation in CONNECTED Mode … he calls the first hunt
    group" (p185)
    "Standard Mailbox … Guest Mailbox … Answer Only Mailbox" (p186)
    "The password of the general mailbox is the operator password" (p189)
  summary: |
    基线：VM 集成在 CPU、每话机一信箱、2 接入端口、4 语言、1 小时存储、问候语至 120s；可选购：会话
    录音+分发列表、附加端口至 8、存储扩至 4h/30h/200h。访问双模：APPLICATION 模式（Message 键/专用
    前缀/可编程键，定制与查询不占端口）；CONNECTED 模式（拨端口或 hunt group 号、外拨 VM 的 DDI，
    占 1 端口走 DTMF 语音导览）。信箱三态：Standard（全功能）/Guest（Hotel 客房受限界面）/Answer
    Only（只应答不留信）。特色：Message Screening（键+密码、边录边听可抢接）、Conversation Recorder
    （后缀/键激活、暂停仅软键话机、15 秒静音默认结束、录音默认 30 天删除）、AutoRec 自动录外线、
    General Mailbox（经 AA 访问、仅话务员可听、密码=话务员密码、不绑话机）。语音文件 ADPCM 4bit
    8kHz Mono ↔ WAV PCM 16bit 8kHz Mono 可互转。
  conditions: 容量与端口扩展为可选许可；录音删除期默认 30 天
  tags: [structure, voicemail, modes, recording]

- id: f26
  title: 公共 SIP 拓扑与 OCE 双口接入
  type: diagram
  source_pages: p198, p200
  source_chapter: Public SIP gateway management / Topology – Public SIP provider access / Public SIP Trunk Group
  source_quote: |
    "SBC: Control SIP sessions at the SIP provider border • CE: Router/Firewall/NAT + SIP NAT •
    SIP Proxy: Distribution of calls in the SIP network • Registrar: SIP Subscriber Authentication
    • Location: SIP Subscriber localization • Gateway: Gateway between SIP and the ISDN network" (p198)
    "The ISP's SIP network can be connected either to Eth0 or directly to the dedicated Eth1
    connector of the OCE." (p200)
  summary: |
    运营商侧组件链：SBC（边界会话控制）→ SoftSwitch → SIP Proxy（分发）/Registrar+Location（注册
    认证定位）→ Gateway（SIP↔ISDN）；客户侧 CE 路由器/防火墙/NAT。Public SIP Trunk Group 服务要求
    OXO 经 LAN 接入（外部或内部交换机 LANX）且受软件许可控制。OCE 特有：ISP 的 SIP 网络可接 ETH0
    （与 LAN 同口）或直连专用 ETH1——后者两子网间启用路由，安全性更高。
  conditions: SIP trunk 服务受许可控制；运营商兼容清单见 TC1284（p199 分国别摘录）
  tags: [diagram, sip-trunk, topology, sbc]

- id: f27
  title: SIP 网关配置菜单地图——OMC/External Lines/SIP 七页签
  type: structure
  source_pages: p203-214, p232-237
  source_chapter: SIP Gateway configuration 讲义 + How-To 5.1.1-5.1.9
  source_quote: |
    "OMC/External Lines/SIP/SIP Gateway/ • Create a new one • These infos are given to the client
    by the public provider" (p208)
    "5.1.1 … General tab … 5.1.2 … DNS tab … 5.1.3 … Domain Proxy Tab … 5.1.4 … Registration Tab …
    5.1.5 … Media Tab … 5.1.6 … Identity Tab … 5.1.7 … Protocol Tab … 5.1.8 … Topology Tab …
    5.1.9 … Security Tab" (p223-224 目录)
  summary: |
    SIP 网关配置地图：周边配置——默认网关指向 CE（OMC/Hardware and Limits/LAN/IP Configuration）、
    安装号（OMC/Numbering/Installation Numbers，SIP 默认规范格式 +国际码+城际码+安装号+DID）、DDI
    （OMC/Numbering/Public Dialing Plan）、VoIP 接入（OMC/External lines/List of Accesses：Public
    属性+通道数，建网关后必须回填 Gateway index）、中继组（OMC/External Lines/list of Trunk Groups：
    加 VoIP 接入+链路类别）。网关本体（OMC/External Lines/SIP/SIP Gateway）九页签：General（索引/
    名称/号码格式索引/拨号结束表）、DNS（DNS A、启停 DNS 功能）、Domain Proxy（Target/Local 域、
    Realm、Outbound Proxy——填 DNS 后 IP 类型自动 dynamic）、Registration（是否注册+Registrar 名）、
    Media（RTP Direct、带宽=并发通话数）、Identity（RFC3325 CLIR）、Protocol（默认）、Topology
    （NAT 开关、ETH0/ETH1 选择）、Security（SIP 流加密）。SIP 账户（OMC/External Lines/SIP/SIP
    Accounts 右键 Add）：登录/密码/注册用户名、关联网关索引；可对非 DDI 用户发公司名、DDI 用户发分机名。
  conditions: 各页签取值以运营商参数为准（生产按 TC1284 对应 TC）
  tags: [structure, sip-gateway, omc-path, menu-map]

- id: f28
  title: SIP Trunk Profile 导入导出与 Easy Connect 流程
  type: flow
  source_pages: p216-222
  source_chapter: SIP Trunks profiles Import/Export via OMC / SIP trunk easy setup through Cloud Connect / Complementary Setup
  source_quote: |
    "Once a new SIP provider gets approved by the TSS, the configuration related to this provider
    is collected by ALE and put in a file called Profile, available on MyPortal … Refer to TC1994:
    SIP Easy Connect: SIP Trunk Profile Import/Export" (p216)
    "Prerequisite : systems must be Cloud Connected • Available for OCO and OCE" (p218)
    "OMC/Numbering/Automatic Routing Selection/Automatic Routing Prefixes … Line 2: copes with all
    public emergency numbers. The network attribute "emerg" … Line 3: example for France, for short
    numbers that begin with digit 3 … Line 4: … digit 1 (e.g. 112, 118712, …)" (p220-221)
  summary: |
    Profile 机制：运营商过 TSS 认证后，其配置被打包成 SPF Profile 文件放 MyPortal（TC1284 引用），
    内容=网关参数集+相关 SIP Public Numbering 参数+VoIP 全局参数子集+特定 noteworthy 地址；导入
    路径 OMC/Import/Export/Import/Export Data 选 SPF 文件。Easy Connect：Cloud Connected 系统（OCO
    与 OCE 均可）在 OXO 网页选 Profile（按版本与 software target 过滤），填少量参数即可完成 SIP
    trunk/网关/账户/编号配置，后续修改仍走 OMC。补充配置：ARS 表按国家补短号与紧急号码——内编号
    计划加 ARS 表入口（OMC/Numbering Plans/Internal numbering plan）+ ARS 前缀表（OMC/Numbering/
    Automatic Routing Selection/Automatic Routing Prefixes，右键 Opt.Parameters）；法国典型四行
    （0 开头标准/紧急 emerg 属性/3 开头短号/1 开头短号）；ARS 中继组清单（OMC/Numbering/Automatic
    Routing Selection/Trunk Groups Lists）Index 1 指向 VoIP 中继所在组。始终参考各运营商
    «SIP Trunk Solution Provider xxx: Configuration Guideline» 技术公告。
  conditions: Easy Connect 前提系统已 Cloud Connected；紧急清单按国家编辑（OMC 菜单 Emergency→Emergency Numbers）
  tags: [flow, sip-profile, easy-connect, ars, emergency]

- id: f29
  title: Messages 1-20 与 Music on hold 体系
  type: structure
  source_pages: p243-245, p247-251
  source_chapter: Messages 1 to 20 utilization / Music on hold and Preannouncement messages downloading
  source_quote: |
    "According to the Software keys, the system can have 4 to 20 audio messages … The total length
    of the messages is 320 seconds This length is allocated dynamically to the 20 messages" (p244)
    "Files .wav must be in 16-bit PCM 8 Khz Mono or CCITT A-law or μ-law 8-bit 8Khz Mono format" (p247)
    "Default value: Entity1 (possible values entity 1 to entity 4 used in case of multi company)" (p248)
  summary: |
    消息体系：按许可 4-20 条音频消息、总长 320 秒动态分配；录制走 MMC 话机话务员会话或 OMC 下载。
    五种用途：Welcome（属话务员组）、Pre-announcement（振铃前/中播）、Remote substitution（代音提
    示流程）、External forwarding（告知已转外线）、DISA（代音提示超拨+内线号）。MoH：仅外线保持时
    播放（内线为哔哔音）、三种源（默认乐/音频输入 Tape/录制的 .wav）、按 Entity 1-4 多公司分别配。
    .wav 格式硬约束：16-bit PCM 8kHz Mono 或 CCITT A-law/μ-law 8-bit 8kHz Mono。无 .wav 时话务员
    会话录：Menu Operator/Expert/Voice/Hold music/Music xx 或 Message xx。
  conditions: 消息数与许可相关；Entity 为多公司场景预留
  tags: [structure, messages, moh, wav]

- id: f30
  title: 呼入分发体系——话务台组、时段表与 Normal/Restricted 双计划
  type: structure
  source_pages: p253-261
  source_chapter: Incoming calls management（九页讲义）
  source_quote: |
    "The normal / restricted mode is used for INCOMING calls distribution • 2 DDI numbering plans •
    One for normal mode, another for restricted mode" (p254)
    "Members of a PO group can be: • Extensions • Welcome messages (MSG1 to 20) … General bell (SG)
    • Or voicemail access (to build an auto attendant) An attendant group is always in parallel
    mode." (p264)
    "Number of entries for individual greetings: 200 • Number of preannouncement messages: 20 •
    Messages duration: 320 seconds" (p260)
  summary: |
    呼入经公共/专用拨号计划分发到话务台/用户；Normal/Restricted 两套 DDI 计划支撑日夜切换（手动
    N/R 键或按时段自动）。话务台组（OMC/Attendant groups）成员可为分机/MSG1-20/General bell/VM 端口
    （拼自动话务员），组永远并行模式。时段表（OMC/Time Ranges）逐日配置组切换，示例 8-12 组1、
    12-14 MSG1、14-18 组3、18-8 MSG1。话务台转移：attendant diversion 功能键转集体缩位号，状态看
    OMC/Time ranges 或键闪烁。Attendant help：功能键激活后终端用户成为外线呼叫目的地（模拟话机用
    Programming Mode+6+虚拟键 General Monitoring）。预公告：DDI 呼叫可配个人问候 200 条、预公告
    MSG1-20、总 320s；每时段配模式（无/分发前/分发中）+消息号+仅忙旗标。
  conditions: 组并行模式不可改；个人问候条目 200 上限
  tags: [structure, incoming-calls, attendant-groups, time-ranges]

- id: f31
  title: 出局三层限制模型——Traffic sharing → Barring → 闭锁表
  type: diagram
  source_pages: p271-280
  source_chapter: Outgoing calls management（十一页讲义）
  source_quote: |
    "Traffic sharing link category The set is either allowed (authorized) or not allowed (forbidden)
    to seize a trunk group • Barring link category If allowed to seize a trunk group, the number
    dialed is either allowed (authorized) or not (forbidden)" (p271)
    "« + »: Access from an extension set to a trunk group is authorized « Blank »: Access from an
    extension set to a trunk group is prohibited" (p273)
    "International calls are barred by default The international prefix 00 is added with type
    "Forbidden" in all barring table … 6 barring tables = 6 levels of barring" (p274)
    "Counter 1 • Indicates the maximum number of digits which can be dialed … Counter 2 • Indicates
    the maximum number of authorized digits for prefixes not explicitly recognized" (p275)
  summary: |
    出局判定三层：①Traffic sharing LC（用户 COS × 中继组 COS 经矩阵求交：+=可占/空=禁占）；②
    Barring LC（决定用哪张闭锁表，矩阵行=用户类别、列=中继组类别）；③闭锁表（6 张=6 级；前缀
    Forbidden/Authorized；国际 00 默认全部表 Forbidden；digit counter 1=表内有授权前缀时的最大拨号
    位数、counter 2=未列前缀的最大授权位数）。配置位置：用户 OMC\Subscribers list\Detail\Barring；
    中继组 OMC\External lines\List of trunk group\detail\Link Category；接入（Break-in/Break-out）
    OMC\External lines\List of accesses\detail\Link Category。Normal/Restricted 模式（手动 N/R 键或
    时段自动）下系统用 restricted LC 值；用户级权限两枚：时段自动限制时保持 normal 的权利、
    Inhibition flag（话务员手动限制时保持 normal）。多 DDI 段：新 noteworthy 地址 DDIonPRI 支持按
    所用中继线选 DDI 段发送（T0/T2/模拟/VoIP 全适用）。
  conditions: 默认 LC 值（实验与默认口径 normal=restricted=12）；国际默认禁
  tags: [diagram, barring, link-category, outgoing, cos]

- id: f32
  title: 数据备份体系——自动/手动/SD 卡/迁移四线
  type: structure
  source_pages: p294-306
  source_chapter: System data saving（十三页讲义）
  source_quote: |
    "OMC \ Data Saving & Swapping \Date & Time Data Saving • Program the date of the first back-up,
    the periodicity of the next ones" (p296)
    "Scheduled & immediate … Encrypted (AES 256) … The minimum size is 2 GB and maximum size is
    32GB • SD and SDHC supported • SDXC is not supported • Formatting only via OMC • Supported file
    system is EXT2" (p301, p304)
    "DBAdapter is a software tool to convert database files saved with a previous version of OMC to
    the latest installed version" (p306)
  summary: |
    四条备份线：①基础自动备份——OMC\Data Saving & Swapping\Date & Time Data Saving 设首次日期与
    周期（PowerCPU EE 存 eMMC/MSDB、OCE 存文件系统；换 CPU 时 eMMC 可移用但须重新生成许可）；②
    OMC 手动备份恢复——Read all from PBX → Save As → Backup/Store 到外部介质 .cdb；恢复 Reverse
    （见 c17）；③OCE SD 卡——背面槽、关机插卡、AES 256 加密、多恢复点（最旧自动滚动删除）、恢复仅
    同主版本、卡 2-32GB SD/SDHC（SDXC 不支持）、仅 OMC 格式化、EXT2；路径 Data saving & swapping/
    data backup & restore、频率按天数；④DBAdapter 迁移——MyPortal 装 DBAdapterSetup.msi 后 OMC 打开
    旧库自动透明转换，未装则提示安装。
  conditions: OCE SD 卡为 ALE 不提供的选件；eMMC 复用需重新生成 license
  tags: [structure, backup, sd-card, dbadapter]

- id: f33
  title: 软件下载与双版本机制——下载/Swap/回退
  type: flow
  source_pages: p315-320
  source_chapter: Software Download（六页讲义）
  source_quote: |
    "2 versions simultaneously available on a system An active version A replacement version" (p316)
    "It's mandatory to download the following files • The PBX software release xxx_xxx.zip • The
    associated OMC xx.xx.zip • The technical communication associated" (p318)
    "After a download it is possible to go back to the previous version by performing a switchover
    Swap must be scheduled • OMC/Data saving and swapping/SW-downloading" (p320)
  summary: |
    机制：系统同时保留两版本（active + replacement）；下载流程=文件传输→Data saving→Swap（可带或
    不带数据保存）→Data restore。操作：MyPortal 下载三件套（PBX 软件 zip、配套 OMC zip、配套技术
    通函）解压到管理 PC → OMC\Tools\Software download → Download 密码（系统启动时定制）→ 连 BPWS
    后会话生效。Swap 须排程：OMC/Data saving and swapping/SW-downloading。回退：switchover 切回
    前版本。
  conditions: HTTPS 标准协议，LAN 与 modem 连接均可；OMC 版本须与目标软件配套
  tags: [flow, software-download, swap, rollback]

- id: f34
  title: 三种复位的选择矩阵与数据分类
  type: structure
  source_pages: p321-324
  source_chapter: System reset（四页讲义）
  source_quote: |
    "Warm reset • Allows to unlock hardware malfunction without losing the customer database …
    Cold reset • … After a cold reset you loose all the customer's configuration … Factory Reset •
    Removes all the sub categories of data in cold reset and additionally it removes system logs" (p322)
    "When Cold reset is triggered without selecting any sub options • The following settings are
    not deleted: Installer passwords • Network settings • Management services access flags • Cloud
    Connect parameters" (p323)
  summary: |
    三档复位：Warm（重启不丢库，解锁硬件故障）；Cold（回默认配置重定制，默认丢 User Data/System
    Data/Cloud Connect Data/Network/installer 密码/Management Data，但不勾子选项时保留 installer
    密码、网络设置、管理服务接入旗标、Cloud Connect 参数）；Factory（Cold 全部之外再删系统日志，
    状态接近 Lola 安装态）。数据分类：User Data=VMU/IM/Mails；Network=主机名/IP/掩码/广播/网关/
    VLAN/路由器/DNS/Web 代理（IP/hostname/端口/账户/密码）；Management Passwords=Attendant/
    Administrator/Installer/Download/NMC；Management Data=允许 WAN 管理服务；Cloud Connect Data=
    激活状态/FTR 完成状态/服务器 URL/一次性激活账户密码/最终账户密码；System Data=数据保存文件/
    metering/traces 与 core/ACD 统计日志。操作入口：话机 MMC 话务员会话 Menu/Operator/OP 密码/
    Expert/System reset（Warm/Cold）或 OMC Expert OMC\System Miscellaneous\System Reset（Cold 带
    选项/Warm/Factory；时间 Manual/Automatic）。手动关机后再开=warm reset。
  conditions: Cold 前务必备份（配合 c17）；Hotel 模式只能经初始安装向导进入（p447）
  tags: [structure, reset, warm, cold, factory, data-classification]

- id: f35
  title: Rainbow 平台全景与 UCaaS 架构三要素
  type: diagram
  source_pages: p330-334
  source_chapter: Rainbow / Overview / Global view / Architecture - UCaaS / Subscription plans
  source_quote: |
    "Rainbow Is the cloud solution for team Collaboration and Unified Communications featuring phone
    and web calls, video conferencing, mobility, security and many APIs open to all developers" (p331)
    "Unified Communications as a Service [UCaaS] … Communication Platform as a Service [CPaaS]" (p332)
    "Clients • PC Rainbow App • Web • Mobile … PBX connected to Rainbow with WebRTC gateway" (p334)
  summary: |
    Rainbow 双定位：UCaaS（Rainbow Workplace：云话音/会议/多媒体 + PBX 话音/呼叫控制/联邦）与
    CPaaS（开放 API/SDK 供业务应用与客服集成）。全景：Rainbow Platform 居中供唯一用户体验（联系人、
    富在场、通知、告警监控、分析、控制管理），经 AGENT 对接 OXE、OXO Connect、第三方 PBX 与机器；
    门户 hub.openrainbow.com。UCaaS 架构三要素：客户端三形态（PC App/Web/Mobile）+ 通信层（客户端间
    及到任意号码/分机的呼叫、路由 profile）+ 客户侧 PBX 经 WebRTC 网关接入。订阅目录七种（Essential
    免费/Business/Enterprise/Enterprise Conference 年付/Conference pay-as-you-go/Connect CRM/Room）。
  conditions: 订阅详情以 openrainbow.com/Subscription plans 为准
  tags: [diagram, rainbow, ucaas, cpaas, architecture]

- id: f36
  title: Rainbow 管理员双档案与公司管理面
  type: structure
  source_pages: p337-343
  source_chapter: ADMINISTRATORS PROFILES / BUSINESS DIRECTORY / INFORMATION CHANNELS
  source_quote: |
    "RESELLER / BP ADMINISTRATOR … Create PBXs & activate WebRTC gateways … Assign subscriptions to
    end-customer companies" (p338)
    "END- CUSTOMER ADMINISTRATOR … Manage user accounts … View related PBXs … Associate users
    phones with their Rainbow accounts" (p339)
    "Only users with an "Enterprise" service level can create Information Channels." (p342)
  summary: |
    两类管理员：Reseller/BP（看客户公司、管自己与 EC 公司、给 EC 分订阅、建 PBX 并激活 WebRTC 网关、
    管理员/用户账户、分机关联、profile、仪表盘）；EC（管自己公司、用户账户、公司信息、给用户分订阅、
    查关联 PBX、话机关联、profile、仪表盘）。角色细目见 help.openrainbow.com Features List/
    Administration。客户管理员 Roles 页签分配管理权、可多管理员。Business Directory：Azure AD 之外
    的外公司联系人目录（改善来电识别），默认客户管理员可管、可委托非管理员、手动或 CSV 批量导入
    （有样例、导入出报告）。Information Channels：新闻订阅，仅 Enterprise 级可建；可建指定成员强制
    订阅、全公司强制订阅（不可退订）及跨公司频道。
  conditions: BP 专属动作=建 PBX/开付费订阅（与 RAINXTE001EN 口径一致）
  tags: [structure, rainbow, administrators, directory, channels]

- id: f37
  title: WebRTC 网关四拓扑结构与部署分工
  type: structure
  source_pages: p362-368
  source_chapter: Rainbow WebRTC Gateway / Deployment steps / Automatic configuration / Deployment steps on OXO Connect
  source_quote: |
    "The WebRTC Gateway brings voice interoperability between Rainbow Clients and PBX ecosystem." (p363)
    "OXO Connect Evolution … Web RTC Gateway virtual machine is integrated … OXO Connect WebRTC
    Front End (on OCE Front End) … Web RTC Gateway virtual machine installed on Mini PC (NUC) …
    installed on a server ESXi" (p363)
    "The automatic configuration of the internal / external WebRTC gateway is available from system
    version R4.0.020.002" (p366)
  summary: |
    四拓扑：①OCE 集成（网关 VM 集成在 OCE）；②OCE Front End（网关跑在客户 LAN 的前置 IPBox）；③
    外部 NUC Mini PC VM；④外部 ESXi 服务器 VM。前提：PBX 已连 Rainbow、用户持 Business/Enterprise
    订阅。自动配置（≥R4.0.020.002，Reseller 管理员发起）自动管五项（内部拓扑多一项"激活内部网关
    仅 OCE"）：WebRTC SIP 网关、SIP 账户（含 Rainbow PBXID）、VoIP 接入与中继组、ARS 路由表；安装员
    仍管：连 PBX 到 Rainbow、建关联 AnyDevice/Rainbow 虚拟终端、编号计划与闭锁（外部拓扑再加：安装
    配置 VM/独立 PC、激活网关）。OXO 侧终端规则：有物理话机=建 Multiset（主站物理+副站 Free Rainbow
    in Twinset（R6.0 起）/Anydevice（至 R5.2））；纯 Rainbow 用户=只建 Anydevice。参考 TC2479。
  conditions: 四拓扑功能等级相同（集成拓扑 p370 明示"Same feature level as the external WebRTC GW
    topology"）；生产部署跟 Rainbow WebRTC cookbook
  tags: [structure, webrtc-gateway, topology, auto-configuration]

- id: f38
  title: OCE Front End（OCE-FE）专用形态——FTR 自动化与双机约束
  type: structure
  source_pages: p372-382
  source_chapter: Use case # 2 WebRTC gateway on OCE Front End（十一页讲义）
  source_quote: |
    "The WebRTC gateway runs on an IPBox on the customer's LAN, in front of another OXO Connect
    which runs the customer Call Server … The release ≥ R4.0 MD must be installed on both the
    Front-End RGW and the OXO Connect call server" (p373)
    "An OCE in front-end Mode is limited to WebRTC GW feature (No UTLs, etc…)" (p374)
    "The private SIP gateway is automatically created on the OXO Connect call server Verify port
    numbers to 5059 … Rainbow PBXID must be the same in both OXO Connect, Front-End and call server" (p379)
  summary: |
    OCE-FE：标准 OCE 软硬件+免费专用许可，FE 模式仅限 WebRTC GW 功能（无 UTL）；不提供 PBX 能力、
    供给不需要 OMC。约束：FE 与呼叫服务器均须 ≥R4.0 MD；两台的 Rainbow PBXID 必须相同（FTR 时
    PBXID/激活码默认占位 "FleetRef-Installref"，可提前在 RB WebAdmin 备料；公司已建则两台都填真实
    PbxId）。安装走 FTR：连 FE 的 ETH1（DHCP）开 192.168.94.246 → 首连设 installer 密码 → 产品类型
    选 Frontend WebRTC → 填客户参考与 IP → FTR 自动给许可并按需升级版本；修改后 warm reset 生效；
    FE CPU 状态看 Settings 菜单与 Webdiag。Rainbow BP 侧为公司激活网关、类型选 External on OCE
    Front-End（20 max）；呼叫服务器上私有 SIP 网关自动创建、核对端口号 5059。Cloud Connect 演进：
    Fleet Dashboard 识别 PBX/OCE-FE 配对、一键跳对端、每设备一行同 install_id 根。开通场景多种
    （全新/加装/PBX 低于 R4/带或不带参考值）——务必跟 cookbook 最新版。
  conditions: OCE-FE GW 仅支持 PowerCPU EE 呼叫服务器侧 20 通话（IPBox 呼叫服务器不支持 OCE-FE GW）
  tags: [structure, oce-fe, ftr, pbxid, cookbook]

- id: f39
  title: 外部 WebRTC 网关部署流程——VMware 与 NUC 双路
  type: flow
  source_pages: p383-390
  source_chapter: Use case # 3 / # 4 External WebRTC gateway
  source_quote: |
    "Deploy the .ovf file with Vmware ESXi and start the virtual machine … Configure the Network
    settings (static or DHCP) • IP , NETMASK, GATEWAY and DNS • Add the OXO Connect IP@ and Rainbow
    PBXID • TURN server configuration according to site location" (p386)
    "The Software package available on MyPortal contains the OVF files for VMWARE installation, and,
    an ISO file for installation on a mini PC … RUFUS is very easy to use for this purpose" (p389-390)
  summary: |
    VMware 路：MyPortal 下载网关 VM → .ovf 部署到 ESXi 启动 → 配置网络（静态/DHCP：IP/掩码/网关/
    DNS）→ 填 OXO Connect IP 与 Rainbow PBXID → 按站点位置配 TURN 服务器（部署文档从 Rainbow 支持
    网站 ALE equipments (PBX) 区下载）。NUC 路：同上除 mini PC 本体安装——MyPortal 包含 OVF（VMware）
    与 ISO（mini PC）；ISO 经启动 U 盘（RUFUS 制作）装入 mini PC 存储后重启配置；Whitelist 清单在
    过程文档中。Rainbow 侧：公司选 Activate the WebRTC gateway、定义外部网关与通道数、OXO 侧自动
    管理；用户须 Business/Enterprise 订阅且账户关联 PBX 话机。
  conditions: TURN 位置选择是生产关键项（书中仅一句带过）；Whitelist 见部署文档
  tags: [flow, webrtc-gateway, vmware, nuc, turn]

- id: f40
  title: WebRTC 网关容量规划表——用户数、通道数与拓扑上限
  type: structure
  source_pages: p391-392
  source_chapter: Dimensioning / Rainbow WebRTC gateway dimensioning
  source_quote: |
    "5 → 5/5 → 5 … 50 → 20/20 → 50 … 150 → 50/NA → 150(*)" (p392)
    "50 VoIP calls maximum if the WebRTC gateway is external on Mini PC or ESXi server • 20 VoIP
    calls maximum with OCE integrated WebRTC gateway or if the WebRTC gateway is external on OCE
    Front End" (p392)
    "Maximum of OXO users with Rainbow VoIP option increased from 50 to 150" (p392)
  summary: |
    容量表（列：Rainbow VoIP 用户数 → 外部通道数/集成或 FE 通道数 → 集成拓扑用户数）：5→5/5→5；
    10→7/7→10；20→11/11→20；30→15/15→30；50→20/20→50；70→27/NA→70(*)；100→36/NA→100(*)；
    150→50/NA→150(*)。硬上限：外部（Mini PC/ESXi）50 通话；OCE 集成或 OCE-FE 20 通话；需要更多通道
    时 OCE 也可走外部网关拓扑（至 50）。Rainbow VoIP 用户上限 50→150（OXO Connect 与 Evolution 均适
    用）。(*)注：集成拓扑用户上限取决于配置通道数与用户话务，表值为 20 通道下方向性参考、极低话务
    时 150 可达成。
  conditions: 表为 R6.3 口径；通道数按推荐值配置后再核对话务
  tags: [structure, dimensioning, capacity, webrtc-gateway]

- id: f41
  title: Rainbow 话务台界面结构与监督组规格
  type: structure
  source_pages: p407-414
  source_chapter: RAINBOW ATTENDANT CONSOLE / SUPERVISION GROUPS / MISCELLANEOUS
  source_quote: |
    "Call queue management - Manage up to 10 calls for OXE - And up to 8 calls for OXO Connect" (p409)
    "Maximum number of supervision groups for a supervisor 5 Maximum number of users in a group
    (supervisors + supervised) 30" (p412)
    "Attendant features are only available on PC (thick client or web mode)" (p414)
  summary: |
    话务台：OXE/OXO Connect 可用；三区（呼叫队列、当前通信呼叫控制、Busy Lamp Field 监督区）+监督组
    页签；队列 OXE 10 通/OXO Connect 8 通；空闲态三种显示（Normal/Small/Condensed）。监督组：监督员
    （须 Attendant 订阅）+被监督成员同组；每监督员 ≤5 组、每组 ≤30 人（含监督员）；不可见组页签红点
    提示、可选音频通知；动作=拦截被监督用户来电、强制（转信箱）或取消其前转。约束：话务台功能仅 PC
    （厚客户端/Web），话机与手机上无任何话务台功能；保持数取决于软话机线多线资源（OXE REX 至 10、
    OXO Connect Any Device 最低 R6 至 8）；所有呼叫由 PBX 处理；拦截仅同 PBX、仅电话呼叫。配置参考
    TC2479（OXO）/TC2462（OXE）。
  conditions: Attendant 订阅按成员计；移动端不可用
  tags: [structure, attendant-console, supervision-groups, capacity]

- id: f42
  title: 互助监督组机制——动态进出与边界
  type: structure
  source_pages: p415-418
  source_chapter: MUTUAL AID SUPERVISION GROUPS / APPLICATION VIEW / MANAGEMENT
  source_quote: |
    "Groups that are permanently affiliated to you • Groups that you can join on an ad hoc basis in
    one click at times … temporarily integrate or exclude a supervised user" (p416)
    "Works only for PBX calls, not for Rainbow softphone calls" (p416)
    "Up to 4 calls supervised … Join/leave the group Locked: cannot leave" (p417)
    "The type must be: Mutual aid group Define the supervisor role & In/Out permission for both
    profiles" (p418)
  summary: |
    互助监督组：两类组并存——永久隶属组+可一键临时加入的组；监督员可临时纳入/排除被监督用户（被监
    督人离开前忘进组时有用）；监督员收到被监督用户来电通知并可代接。边界：仅 PBX 呼叫有效（Rainbow
    软话机呼叫无效）；锁定成员（Lock the last member）不可退出；监督视图至多同时监督 4 通呼叫；监督
    员属于其监督的组。管理：与经典组同法创建（Communication/Supervision/Create），类型选 Mutual aid
    group，定义监督员角色与两种 profile 的进出权限。
  conditions: 创建入口与经典监督组相同；成员须有物理分机或关联 PBX 软话机
  tags: [structure, mutual-aid, supervision, groups]

- id: f43
  title: PowerCPU EE 启动八步与停机指示
  type: flow
  source_pages: p436-438
  source_chapter: PowerCPU EE Start and Stop
  source_quote: |
    "Step 0 Starting of the VoIP services … Step 7 Init of the main cabinet … Basic configuration
    (Initial Installation Wizard)" (p437)
    "When the CPU is shutting down the Power LED blinks in red • When the CPU is stopped the Power
    LED is steady red" (p438)
  summary: |
    启动监控八步（按前面板开关后）：Step0 VoIP 服务启动 → Step1 扩展柜 2 卡检测 → Step2 扩展柜 2
    初始化（HSL2）→ Step3 扩展柜 1 卡检测 → Step4 扩展柜 1 初始化（HSL1）→ Step5 主柜卡检测 →
    Step6 主柜初始化 → Step7 话机启动结束（VMU）→ 基础配置（初始安装向导）。停机：关机中电源 LED
    红闪、停止后红常亮；手动关机（On/Off 键）用于关系统或换 CPU 板；自动关机触发于电源/电池问题或
    软硬件异常。
  conditions: PowerCPU EE 平台专属；IPBox 启停见 p58 LED 表
  tags: [flow, powercpu, startup, led]

- id: f44
  title: 安装向导体系——话机版与 OMC 版阶段清单
  type: structure
  source_pages: p439-444
  source_chapter: Installation Wizards
  source_quote: |
    "The installation wizard Objective: Manage a basic configuration of the system •The system must
    be in initial state •After the first system starting up •After a cold reset" (p440)
    "1. LAN configuration\Boards\DHCP 2. Default Dialing Plans 3. Installation number 4. Operation
    mode 5. Channels in main trunk group 6. DECT ARI* 7. Handset creation 8. Charge rate 9. Date and
    time 10. List of Users 11. User misc. 12. Common speed dial 13. Attendant groups 14. Hunt groups
    15. Broadcast groups 16. Pickup groups 17. Screening" (p443)
  summary: |
    两类向导：安装向导（管基础配置，系统须初始态——首启或冷复位后；可从 OMC 或 8068s/8078s/8039
    话机跑）；修改向导（既有配置的快速修改：系统设置/外部接入/用户/组/集体缩位/DECT；仅 OMC、随时
    可用）。话机安装向导阶段：Business/Hotel 模式→公共分机号→用户模式→话务台模式→公网中继数→安装
    号→内编号计划→DECT ARI→用户语言→日期时间→基本计费单价→终端/信箱→重启。OMC 安装向导 17 阶段
    （LAN/DHCP→默认拨号计划→安装号→运行模式→主中继组通道→DECT ARI→话机创建→费率→日期时间→用户
    清单→用户杂项→集体缩位→话务台组→hunt groups→广播组→代接组→Screening）。
  conditions: 初始安装向导是进入 Hotel 模式的唯一途径（p447 注）
  tags: [structure, wizards, installation, omc]

- id: f45
  title: 8328 基站 Web Admin 配置地图
  type: structure
  source_pages: p453-459
  source_chapter: 8328 base stations and 8214 handsets classroom installation
  source_quote: |
    "The factory IP configuration of an 8328 base station is a dynamic IP configuration. Therefore,
    a DHCP server must be present" (p455)
    "Browser : https//<8328 station IP @> … Username admin Password admin (by default)" (p456)
    "Alias = OXO for example Registrar = 192.168.1.246 Registration time = 3600 sec. … Sipping 19 =
    Disabled Remote Caller ID Source Priority = ALERT_INFO – PAI – FROM" (p458)
  summary: |
    8328 单基站部署地图：①OXO 侧 DHCP 池就绪（OMC/Hardware and Limits/LAN/IP Configuration/DHCP，
    实验 1.10-1.69）+ Auto-Provisioning 激活；②网线接 8328（绿闪=拿到 IP）；③Web Admin（https://IP，
    默认 admin/admin）三区：Country（国家+NTP 192.168.1.254）、Network（核验 DHCP 下发的 DNS）、
    Servers（把 OXO 声明为 SIP 服务器：Alias/Registrar=192.168.1.246/注册周期 3600s/Sipping 19
    Disabled/主叫 ID 源优先级 ALERT_INFO–PAI–FROM）→ Save。不知基站 IP 时用 8214 话机 menu 拨 *47*
    搜基站。参考《8328 SIP-DECT SINGLE BASE STATION – System Guide》。
  conditions: 课堂实验（需物理基站）；8328 出厂为动态 IP
  tags: [structure, dect, 8328, webadmin]

- id: f46
  title: 模拟-SIP 网关（FXS）接入模型
  type: structure
  source_pages: p104
  source_chapter: ALE terminals / Analog-SIP Gateway for OCE
  source_quote: |
    "Passerelle FXS MEDIA5 4102 MEDIA5 C710 MEDIA5 C711 • Ports FXS (RJ-11) 2 4 8 • Ports RJ-45 2 2 2" (p104)
    "Requires one UTL + one Open SIP license per analog port … Appears in OMC as Open SIP Terminal" (p104)
  summary: |
    目标：把模拟话机/传真等接入 OCE。目录三款：MEDIA5 4102（2 FXS）/C710（4 FXS）/C711（8 FXS），
    均双 RJ45；每模拟口耗 1 UTL+1 Open SIP 许可；在 OMC 中显示为 Open SIP 终端。拓扑：模拟设备→
    网关（PoE 交换机供电）→LAN→OCE。部署指南在 MyPortal。
  conditions: OCE 场景；许可按端口数计
  tags: [structure, fxs, analog-gateway, licensing]
```

### 任务覆盖自检（task↔id 映射）
- task-01 数据采集→f10/f15（IP/密码/默认行为背景）；task-02 FTR/部署方案→f09-f11；task-03 OMC→f12-f14；task-04 IP 修改→（c03）；task-05 话机→（c04，结构见 f06/f08）；task-06 DECT→f45/（c05/c25）；task-07 编号→f16-f18；task-08 组→f19-f22；task-09 用户功能→f23-f24；task-10 信箱→f25；task-11 SIP→f26-f28；task-12 消息彩铃→f29；task-13 呼入→f30；task-14 出局→f31；task-15 备份→f32；task-16 软件下载→f33；task-17 复位→f34；task-18 安全→（principle/counter-example）；task-19 接入 Rainbow→（c18，结构见 f35-f36）；task-20 成员/分机→（c19/c20）；task-21 网关→f37-f40；task-22 虚拟终端→（c22，结构见 f37）；task-23 话务台→f41-f42；task-24 向导→f43-f44。24 个 task 全覆盖，无遗漏。
