# 案例/实验/操作序列候选 — Rainbow OXO Connect (RAINXTE001EN Ed13)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号）标注"实验口径"。
> 条目说明: 全书 11 个 How-To 实验章 → 13 条（账户章、话务台章各拆 2）+ 1 条讲义级网关部署操作序列（c07，非 How-To 章但属操作序列），共 14 条。

```yaml
- id: c01
  title: OMC 安装与首次连接 OXO（证书安装、改密、客户信息）
  type: lab
  source_pages: p69-78
  source_chapter: OMC Installation — "Install OMC, connect to the PCX"
  source_quote: |
    "Make a connection to the system with OMC in Expert mode with server authentication" (p74)；
    "In order to avoid displaying the security alert at each connection, you must install the certificate
    the 1st time." (p75)；
    "OMC is ready to start with the customer configuration. The icon on the bottom right shows that you
    are connected to the OXO" (p78)
  steps: |
    1. RLab 中用 console mode 连接 PC Client 虚拟机 OXOC_PC_CLIENT；在桌面 SOFTS OXO CONNECT 目录解压 OMC 安装包（实验口径）。
    2. 双击 setup.exe，选 "Run as administrator"；选安装语言 → OK → Next。
    3. 选 Destination folder → Next；选目标 Country/Distribution Channels（可多选）→ Next。
    4. 选 Target Product → Next；选 OMC 显示语言 → Next；点 Install → 完成后 Finish。
    5. 打开 OMC 应用，选 "Expert" 菜单，连接方式用 LAN/WAN。
    6. 输入 OXO 出厂 IP 192.168.92.246（实验口径），勾选 "Server authentication"，输入首次登录安装密码 pbxk1064（实验口径，仅第一次连接使用）。
    7. Security Alert 弹窗 → View certificate → Install certificate → 存储区选 "Trusted Root Certification Authorities" → OK → Finish → 导入成功后点 OK（此后每次连接不再弹安全告警）。
    8. 按讲师给定值（实验口径）为各账户设置新密码（每客户密码必须不同）；后续可在 OMC/Security 菜单再改。
    9. 录入客户信息（带 * 为必填，首次连接 OXO 强制），可选录入供应商信息（即实施技师联系方式）。
  verification: |
    书中验收点：OMC 右下角图标显示已连接 OXO，即 "OMC is ready to start with the customer configuration"（p78）。
  conditions: OXO Connect 处于出厂默认状态；OMC 安装包在客户端 PC 桌面 SOFTS OXO CONNECT 目录（或 NAS 网络盘）。
  tags: [lab, omc, installation, oxo, first-connection]

- id: c02
  title: OXO Connect 与客户端 PC 的 IP 规划修改
  type: lab
  source_pages: p79-82
  source_chapter: OXO Connect IP settings modification
  source_quote: |
    "With the OMC, change the OXO Connect IP settings" (p80)；
    "Click OK & Re-start the OXO Connect" (p81)；
    "Change the IP settings of the client PC (OXO_PC_CLIENT)" (p82)
  steps: |
    1. 进入 OMC/ Hardware and limits/ Lan/IP configuration，打开 Lan/IP configuration。
    2. Boards 页签：Main CPU 填 192.168.1.246（实验口径）。
    3. LAN Configuration 页签：Mask 255.255.255.0；Default Router Address 192.168.1.254（实验口径）。
    4. DNS 页签：DNS 1 = 192.168.1.250；DNS 2 = 10.20.30.250（实验口径）。
    5. DHCP 页签：定义话机地址池 Start 192.168.1.30 / End 192.168.1.39（实验口径）。
    6. 点 OK 并重启 OXO Connect。
    7. 改客户端 PC（OXO_PC_CLIENT）IP：IP 192.168.1.10 / 掩码 255.255.255.0 / 网关 192.168.1.254 / DNS1 192.168.1.250 / DNS2 10.20.30.250（实验口径）。
  verification: |
    书中隐含验收：IP 生效后（虚拟课堂口径）改用 "Remote Desktop Connection"（RDP）重新连上 Client PC VM（p80）。
  conditions: c01 已完成（OMC 可连 OXO）。
  tags: [lab, omc, ip-planning, oxo]

- id: c03
  title: OXO 接入 Rainbow（PBXID+激活码）与 Webdiag 排障
  type: lab
  source_pages: p83-89
  source_chapter: Connect an OXO to Rainbow — "Configure Rainbow agent in OXO"
  source_quote: |
    "Log in to the Rainbow interface with the client company's administrator account" (p84)；
    "In Cloud menu, select Rainbow … Click on Rainbow enabled … Apply" (p86)；
    "OMC /Tools /Webdiag /Services /Rainbow Status — Control the connection status: « connected with final
    password »" (p88)；
    "The rainbow agent log file name is: ccrbagent.log" (p88)
  steps: |
    1. 前提：公司与 PBX 已在 Rainbow 管理端由经销商/讲师创建（书中 Implementation 声明，讲师需演示该配置）。
    2. 取凭证（两法）：向经销商索取；或自行登录 https://web.openrainbow.com（客户端管理员账号 cCpP.admin@ale-training.com / Superuser-P*，实验口径）→ 点公司管理图标 → My company → Communication 菜单 → 列表中点该 OXO → 查看 PBXID 与 Activation code 并复制。
    3. OMC/Cloud/Rainbow：Cloud 菜单选 Rainbow → 填 Rainbow PBX-ID → 填 Activation code → 勾选 "Rainbow enabled" → Apply；Domain name 保持默认 openrainbow.com。
    4. 在 OMC/Cloud/Rainbow 页面查看连接状态。
    5. 排障-连接状态：OMC/Tools/Webdiag/Services/Rainbow Status（登录 installer + installer 密码，实验口径），确认状态为 "connected with final password"。
    6. 排障-系统日志：Webdiag 的 System 页签 / System Files / Log files，Rainbow agent 日志文件名为 ccrbagent.log。
    7. 排障-用户侧日志：Rainbow 界面 → User Settings 页签 → About Rainbow 页签 → 菜单 Open logs。
  verification: |
    Webdiag 的 Rainbow Status 显示 "connected with final password"（p88）。
  conditions: Rainbow 侧公司与 PBX 已建好（BP/经销商动作，实验中由讲师完成）；OMC 可用。
  tags: [lab, rainbow, pbx-connection, webdiag, ccrbagent]

- id: c04
  title: Rainbow 成员手动创建（user1）与管理员 Enterprise 订阅核验
  type: lab
  source_pages: p102-106
  source_chapter: Rainbow accounts configuration and use — "Create new Rainbow user accounts. Assign ENTERPRISE subscriptions. Use Rainbow clients"
  source_quote: |
    "Log in : cCpP.admin@ale-training.com (C class number and P pod number) — Password: Superuser-P*" (p103)；
    "On the Services tab, validate the Enterprise subscription" (p104)；
    "Click on Members and then on Create … Fill in the required fields" (p105)
  steps: |
    1. 浏览器打开 https://web.openrainbow.com，用客户端管理员登录：cCpP.admin@ale-training.com / Superuser-P*（实验口径，C=班号、P=POD 号）。
    2. 核验管理员订阅：点 Members → 选管理员账户 → Services 页签确认已分配 Enterprise。
    3. 手动建成员：点 Members → Create → 填写：Login = cCpP.user1@ale-training.com（实验口径）；Password = Superuser-P*（实验口径）；Sign-in method 保持默认 "Login and password will be asked to sign-in"；Visibility 保持 "same as company"（该公司按 private 管理）；Last name = cCpP；First name = User1；Subscription = Enterprise。
    4. 勾选 "Send enrollment email to new users" 后提交，平台向用户发送开户通知邮件。
    5. （实验口径）登录培训邮箱核验收信：https://mail44.lwspanel.com/，用户名 = 该邮箱地址，密码 = PasswordP*（P=POD 号）；清理旧邮件；检查 Rainbow 平台邮件是否落入 SPAM。
  verification: |
    Members 列表出现 user1 且 Services 页签为 Enterprise；enrollment 邮件送达（不在 SPAM）。
  conditions: 管理员账户已由讲师创建；培训邮箱服务器由讲师提供（实验专用口径）。
  tags: [lab, members, manual-creation, subscription, enterprise]

- id: c05
  title: Rainbow 成员邀请创建（user2）、补配 Enterprise 与双账户功能测试
  type: lab
  source_pages: p107-110
  source_chapter: Rainbow accounts configuration and use（续）— "Create a new member by invitation / Tests"
  source_quote: |
    "My company / Members — Select the Invitations tab … Click Invite" (p107)；
    "the user must accept the invitation received by email by clicking on the link to join the company" (p107)；
    "Perform the following tests: Place calls between two Rainbow applications (users); Share the computer's
    screen of one of the members; Send an IM messages between the two users" (p110)
  steps: |
    1. 管理员登录 → My company / Members → Invitations 页签 → 点 Invite → 输入 cCpP.user2@ale-training.com（可一次输入多个地址批量邀请）→ OK。
    2. 用户侧：登录其培训邮箱（https://mail44.lwspanel.com/，用户名 = 邮箱，密码 = PasswordP*，实验口径；先清旧邮件、查 SPAM），在邀请邮件中点 Join。
    3. 完成开户：按邮件链接设置密码与必填信息——Name = cCpP、Firstname = User2、Password = Superuser-P*（实验口径；平台密码策略：至少 12 字符，含大写、数字、特殊字符各 1）。
    4. 管理员补配订阅：My company / Members → 选 User2 → Services 页签勾 Enterprise。
  verification: |
    p110 三项行为测试：① 两个 Rainbow 用户间互打呼叫；② 一方共享电脑屏幕；③ 两用户间互发 IM。
    书中提示：管理员也是公司成员，可直接用管理员账户当对端执行上述测试。
  conditions: c04 已完成（管理员可登录）；培训邮箱可用。
  tags: [lab, members, invitation, subscription, collaboration-test]

- id: c06
  title: 分机关联 Rainbow 账户与 RCC 三项测试
  type: lab
  source_pages: p111-116
  source_chapter: Associate extension numbers with Rainbow user accounts
  source_quote: |
    "Once associated, members will be able to supervise their phone from Rainbow (unhook, hang up, transfer),
    this is the RCC (Remote Call Control) mode. Without a WebRTC gateway, the audio will be exclusively
    managed on the phone." (p112)；
    "Select 'Office phone' — Call extension 101 by dialing from the Rainbow app — Does it works ?" /
    "Is it possible to pick up the call that arrived using the Rainbow client? What action(s) is/are available?" /
    "Search for the user cCpP.user2@ale-training.com … Try to call him — Does it works ?" (p116)
  steps: |
    1. 双侧核对 PBX-Rainbow 连接：OXO 侧 OMC/Cloud/Rainbow 看连接状态；Rainbow 侧 My company / Communication → Comm Servers 页签确认 OXO Connect 为 "in service"。
    2. OMC 核对话机在服：确认 100、101 分机 in service。虚拟课堂口径：在 OMC/ Subscriber-BaseStations list 启用 "auto-provisioning"；在 OXOC_PC_CLIENT 上安装 IPDSP 104；预装的 MicroSIP（100/101/102，非成员话机）需在 OMC 中建号；104 IPDSP 分配给 cCpP admin。
    3. 关联分机：Rainbow（PC 应用或 https://web.openrainbow.com）→ My company → Members → 选成员（示例 admin）→ Telephony 页签 → Equipment 字段选 OXO Connect → 选该成员的分机号（课堂口径：admin → 100；V-Class：admin → 104）→ Apply；同法给 cCpP.user1 关联 101。
    4. 观察关联后新增的 "Rainbow number" 字段（例 BBB10070254106463346，书中示例值）；该号由 Rainbow agent 在用户选 "computer" 路由时自动写入 Remote Extension number，无需手工配置，但排障要知道它。
  verification: |
    p116 RCC 三项测试（行为验证，书中原问）：
    1) 呼出至 OXO 用户：从关联 100/104 的 Rainbow 客户端选 "Office phone"，拨 101 — Does it works?
    2) 呼入：从 101 打 100/104 — 能否在 Rainbow 客户端接起？可用动作（接/挂/转）有哪些？
    3) 呼出至纯 Rainbow 用户：在 Rainbow 客户端搜 cCpP.user2（无 OXO 分机）并呼叫 — Does it works?
    （RCC 口径：音频全在话机，Rainbow 仅监督。）
  conditions: c03（PBX 已接入 Rainbow）、c04/c05（账户已建）完成。
  tags: [lab, rcc, extension-association, telephony]

- id: c07
  title: WebRTC 网关三拓扑部署操作序列（OCE-FE FTR / 外部 VM / NUC，讲义级）
  type: howto
  source_pages: p124-145
  source_chapter: Use case #1-#4 — WebRTC integrated to OCE / OCE Front End / VM on VMware / Mini PC (NUC)
  source_quote: |
    "Connect to the OCE Front-End ETH1 in DHCP mode and start a Web browser to 192.168.94.246 … Define the
    product type 'Frontend WebRTC' … FTR OK" (p130-131)；
    "Deploy the .ovf file with Vmware ESXi … Configure the Network settings … Add the OXO Connect IP@ and
    Rainbow PBXID … TURN server configuration according to site location" (p141)；
    "Download the ISO file from MyPortal … Create a Bootable USB drive … RUFUS" (p144-145)
  steps: |
    [OCE Front-End（专用 IPBox，两侧 ≥R4.0 MD，上限 20 通话）]
    1. 前提：客户 OXO Connect 呼叫服务器已连 Rainbow；FTR 自动提供免费专用许可并按需升级版本。
    2. 网线接 OCE Front-End 的 ETH1（DHCP 模式），浏览器访问 192.168.94.246（出厂口径）。
    3. 首连全新 IPBox 必须设置 installer 密码（书中示例 Alcatel1，实验口径）。
    4. FTR 中产品类型选 "Frontend WebRTC"，录客户参考号与 IP 参数 → FTR OK，该 IPBox 即成为 OXO Connect FrontEnd WebRTC Gateway，待与呼叫服务器关联。
    5. 修改 Front-End 的 Rainbow WebRTC Gateway 配置后需 warm reset 生效；Front-End WebRTC CPU 状态可在 Settings 菜单与 Webdiag 工具检查。
    6. Rainbow BP 管理端：为客户公司激活 WebRTC Gateway，网关类型选 "External on OCE Front-End"（上限 20 通话）。
    7. OMC 核验：呼叫服务器上自动生成私网 SIP 网关，核对 SIP Gateway 参数端口到 5059；Front-End 与呼叫服务器两侧的 Rainbow PBXID 必须一致（OXO 侧做 FTR 时 PBXID/激活码默认占位 "FleetRef-Installref"，正式接入前替换）。
    [外部 VM（VMware/ESXi，上限 50 通话）]
    1. 从 MyPortal 下载 WebRTC Gateway 虚拟机（.ovf）与安装规程（Rainbow Support 网站 ALE equipments (PBX) 栏）。
    2. 用 VMware ESXi 部署 .ovf 并启动虚机。
    3. 配置网络（静态或 DHCP）：IP、NETMASK、GATEWAY、DNS。
    4. 填 OXO Connect IP 地址与 Rainbow PBXID；按站点位置配置 TURN 服务器。
    5. Rainbow 管理端为公司勾选 "Activate the WebRTC gateway"，定义 external 网关与通道数（OXO 侧自动配置）。
    6. 用户前提：每人持 Business 或 Enterprise 订阅，且 Rainbow 账户已关联其 PBX 话机。
    [Mini PC（NUC，上限 50 通话）]
    1. MyPortal 下载 ISO（软件包同时含 VMware 用 OVF）；用 RUFUS（rufus.akeo.ie）等工具制作可引导 U 盘。
    2. ISO 安装到 mini PC 存储设备 → 重启独立 PC → 设置配置参数（其余步骤同外部 VM）。
  verification: |
    书中核验点：OCE-FE CPU 状态在 Settings 菜单与 Webdiag 检查（p132）；OMC 侧 Check OXO Connect Rainbow status（p135）；
    生产级配置细节指向 MyPortal《Rainbow WebRTC cookbook》最新版（p135/p137），OCE-FE 开局含多种场景（全新 PBX+OCE-FE、存量 PBX 加装、有无 Partner fleet reference 下单）。
  conditions: PBX 已连 Rainbow（网关部署前提，p120）；版本前提视拓扑（OCE 集成 R3.2+、OCE-FE ≥R4.0 MD）；TURN 位置与防火墙白名单细节在书外（指向外部文档）。
  tags: [howto, webrtc-gateway, deployment, ftr, oce-fe, vmware, nuc]

- id: c08
  title: 内部 WebRTC 网关自动配置（Reseller 激活 + OMC 核验）
  type: lab
  source_pages: p149-154
  source_chapter: Internal WebRTC Gateway automatic configuration on OXO Connect Evolution
  source_quote: |
    "Automatic configuration applies to versions greater than R4.0.020.002" (p150)；
    "Automatic activation of the WebRTC gateway is performed by the trainer with a reseller administrator
    account … He is the only authorized account to manage this service" (p151)；
    "OMC / Cloud / Rainbow — WebRTC Gateway is Connected and Enabled" (p154)
  steps: |
    1. 版本前提：系统版本 > R4.0.020.002。
    2. Reseller 管理员登录 Rainbow（唯一有权管理此服务的账户；实验中由讲师操作，实验口径）。
    3. Client Company / Communication → Manage connection（编辑客户公司 PBX）。
    4. Information 页签 → 勾选 "Activate WebRTC Gateway"。
    5. Settings 页签 → 选 "Internal" 并设定通道数 → 网关启用；客户端管理员随后可在 Rainbow 端查看连接状态。
    6. 自动配置范围（书中清单）：内部 WebRTC 网关激活（仅 OCE）、WebRTC SIP 网关创建、以 Rainbow PBX ID 配置 SIP 账户、VoIP 接入与中继组（trunk group）创建、ARS 路由表配置。
    7. 仍需安装员手工完成：连接 PBX 到 Rainbow、AnyDevice 用户创建与关联、编号计划与闭锁（barring）配置。
  verification: |
    OMC/Cloud/Rainbow 中 WebRTC Gateway 显示 "Connected and Enabled"（p154）；Rainbow Settings 页签显示 enabled，客户端管理员可查连接状态（p153）。
  conditions: PBX 已接入 Rainbow（c03）；Reseller 权限账户。
  tags: [lab, webrtc-gateway, auto-configuration, reseller, omc]

- id: c09
  title: 虚拟终端配置：Twinset 副站（130/131）与 Anydevice（132）
  type: lab
  source_pages: p155-161
  source_chapter: Configure Anydevice/Rainbow virtual terminals for OXO Connect users
  source_quote: |
    "User 100 — Create a virtual terminal, Free rainbow in twinset: 130 — Associate it with extension 100 as
    a secondary set" (p156)；
    "Create an Anydevice terminal: 132 — This terminal will be associated with the Rainbow user account:
    cCpP.user2@ale-training.com" (p158)；
    "Deskphone + Free Rainbow virtual terminal = 1 UTL — Anydevice only = 1 UTL" (p156)
  steps: |
    [形态 A：物理话机 + Rainbow 应用（Multiset）]
    1. OMC/Subscribers list：为每个"话机+Rainbow"用户建虚拟终端 Free Rainbow in Twinset——admin 的主站 100 配副站 130（实验口径；V-Class：IPDSP 104 配 135）。
    2. OMC/Subscribers list：把该虚拟终端挂为用户主分机的副站（secondary set）。
    3. 同法处理 101：建副站 131 并关联（目录号 101 已在 c06 关联 Rainbow 账户 user1）。
    [形态 B：纯软终端（Anydevice，无物理话机）]
    4. OMC/Subscribers list：为纯 Rainbow 用户建 AnyDevice 终端 132（将关联 cCpP.user2；实验口径；V-Class 另建 133 给 user1）。
    5. Rainbow 端绑定：Members → 选 User2 → Telephony 页签 → Equipment 字段选 OXO Connect → 分机号选 132 → Apply（V-Class 同法绑 133 → user1）。
    6. 许可口径：话机 + Twinset 副站 = 1 UTL（R6.0 起 UTL Bypass，副站不额外吃 UTL）；Anydevice = 1 UTL。R5.2 及以前该副站位置用 Anydevice 终端。
  verification: |
    p161 路由切换测试清单（改变呼叫路由后逐项验证）：Computer Call – Computer；Job Call – Computer（原文如此）；
    Computer call – extension；Meeting with 3 participants；Screen sharing；Video；…
    配置后界面核对（p160）：user2（纯软终端）路由含 computer / mobile / other phone 且可呼转；
    admin（100/104）路由另含 office phone。
  conditions: PBX 已接 Rainbow 且内部网关已自动配置（c08）；成员与分机关联已做（c06）。
  tags: [lab, twinset, anydevice, multiset, utl, omc]

- id: c10
  title: 话务台实验：订阅 ATTENDANT、建监督组、打开控制台
  type: lab
  source_pages: p175-179
  source_chapter: Attendant console and Mutual aid supervision groups（章节页眉原文为 "Rainbow OmniPCX Enterprise"，内容为 OXO 培训通用）
  source_quote: |
    "Companies/Customer companies/ <company to manage> 'Subscriptions' section / Service : ATTENDANT …
    Choose the subscription offer: Attendant Monthly" (p176)；
    "'Members' section / Edit the user/ 'Services' tab — Select subscription 'Attendant Monthly'" (p177)；
    "'Communication' section / 'Supervision' tab — Click on 'Create'" (p178)
  steps: |
    1. 订购 ATTENDANT：Companies/Customer companies/<目标公司> → "Subscriptions" 区 → Service: ATTENDANT → 点 "Subscribe to offer" → 选 Attendant Monthly（实验口径：培训禁用 Prepaid，同 p66 警示）→ 许可数设 1 → Subscribe。
    2. 分配订阅：Members 区 → 编辑成员（例 cCpP.user1@ale-training.com）→ Services 页签 → 选 "Attendant Monthly"。
    3. 建监督组：Companies/Customer companies/<目标公司> → "Communication" 区 → "Supervision" 页签 → 点 "Create" → 填 Name、Description → 选监督员（须持 ATTENDANT 订阅，例 user1）→ 勾选被监督成员（公司其余用户）→ 点 "Create"。
    4. 打开控制台：以 user1 登录 web.openrainbow.com 或应用 → 点入口图标进入 Attendant console。
  verification: |
    控制台视图可打开（p179）；结合讲义验收点：控制台呈现监督组页签、Busy Lamp Field 监督区、呼叫排队区
    （呼叫队列 OXO 上限 8 路），并提供 Normal/Small/Condensed 三种显示格式（p164-166）。
  conditions: 监督员与被监督成员须属同一监督组（管理员建组）；Attendant 功能仅 PC 端可用（thick client 或 web），话机/手机上不可用；Attendant 用户须有电话线与 VoIP 软终端能力。
  tags: [lab, attendant, supervision-group, subscription]

- id: c11
  title: 互助监督组创建（Mutual aid group）
  type: lab
  source_pages: p180-181
  source_chapter: Attendant console and Mutual aid supervision groups — "Manage mutual aid supervision groups"
  source_quote: |
    "Create a mutual aid supervision group — Supervisor: cCpP.admin@ale-training.com — Members to supervise:
    Add members with a physical set or PBX softphone (IPDSP/MicroSIP)" (p180)；
    "Name / Description / Type: Mutual aid group / Lock the last member Yes/no" (p180)
  steps: |
    1. Companies/Customer companies/<目标公司> → "Communication" 区 → "Supervision" 页签 → 点 "Create"。
    2. 填字段：Name、Description、Type 选 "Mutual aid group"、"Lock the last member"（Yes/No，锁定最后一名成员不可退出组）。
    3. 添加监督员：cCpP.admin@ale-training.com（实验口径）。
    4. 勾选被监督成员：必须有物理分机或已关联的 PBX 软终端（IPDSP/MicroSIP）。
    5. 以 admin 登录执行监督。
  verification: |
    书中本章未给独立测试步骤；行为口径见讲义（p171-172）：成员/监督员均可一键 Join/leave；
    监督员可临时纳入/排除被监督用户；来话通知后可代接，代接仅对 PBX 电话呼叫有效（Rainbow 软终端呼叫不可代接）；
    同时最多监督 4 路呼叫；被锁定的成员不能退出组。
  conditions: 被监督成员须有物理话机或 PBX 软终端；互助组建法与普通监督组相同，仅类型不同；组类型与双方 In/Out 权限在创建时定义。
  tags: [lab, mutual-aid, supervision-group]

- id: c12
  title: Rainbow for Teams 安装：应用上架、权限同意、Azure 核验
  type: lab
  source_pages: p222-230
  source_chapter: Rainbow for Teams installation — "Add the Rainbow app to the list of Teams apps / Consent the permissions required by the application / Checking of permissions in Azure"
  source_quote: |
    "Teams admin center web interface — Using following URL: https://admin.teams.microsoft.com" (p223)；
    "To give to users the possibility to install it, the status must be 'Allowed' … click on 'Upload new app'" (p224)；
    "Click on the 'Review permissions and consent' button … Click on 'Accept'" (p226-227)；
    "Click on 'Go to Azure Active Directory' … these permissions have been added and … granted by the administrator" (p229-230)
  steps: |
    1. 浏览器打开 Teams 管理中心 https://admin.teams.microsoft.com，选择/输入管理员账户并登录。
    2. "Teams apps" 菜单 → "Manage apps" 子菜单 → 搜索 Rainbow；"Release Status" 为 "--" 表示属微软第三方应用目录；用户可自行安装的前提是状态为 "Allowed"。
    3. 若搜不到（不在默认目录）：点 "Upload new app" → 点 Upload → 选择应用 zip 包 → Open → 关闭"已添加"提示窗；此后应用状态 "Published"，默认 "Allowed"。
    4. 权限同意（方式 A，书中推荐：最简且最合理，用户登录 Teams 时不再弹权限确认）：管理中心点 Rainbow 应用 → "Permissions" 页签 → 点 "Review permissions and consent" → 按需选管理员账户 → 点 "Accept"。
    5. 权限同意（方式 B）：仅当方式 A 未做时，管理员首次在 Teams 内访问 Rainbow 应用点 "Sign in" 会弹权限确认，勾选"代表整个组织"选项后同意（为自己与全组织验证权限）。
    6. Azure 核验：管理中心 → Rainbow 应用 → "Permissions" 页签 → 点 "Go to Azure Active Directory" → 新开页签进 Azure 管理界面（若 Teams 管理员兼有 Azure 访问权则直连）。
  verification: |
    Azure 页面显示 "Rainbow for Teams" 应用所需权限已添加、且由管理员授予（granted by the administrator）（p230）。
  conditions: Teams 管理员账户；应用不在目录时需 zip 包。
  tags: [lab, teams, installation, permissions, azure-ad]

- id: c13
  title: Teams 集成用户配置：账户-PBX 关联、Telephony 权限收敛、订阅分配
  type: lab
  source_pages: p231-235
  source_chapter: Rainbow user configuration for Teams integration
  source_quote: |
    "Select the PBX from the list ('Device' field) and the Extension number. Then click to 'Apply'" (p233)；
    "it is better to apply a restrictive permission to users with Teams integration in order to forbid
    collaboration services from Rainbow … Select the required permission: Here 'Telephony'" (p234)；
    "For Rainbow integration with Teams, a Business or Enterprise subscription is required." (p235)
  steps: |
    1. 账户-PBX 关联：以公司管理员登录 https://web.openrainbow.com → "Manage your company" → "My company" → "Members" → 选成员 → "Telephony" 页签 → "Device" 字段选 PBX、选分机号 → 点 Apply（关联后同样出现 Rainbow number 字段，后续由 Rainbow agent 自动写入 Remote Extension number）。
    2. 权限收敛：My company / Members → 选成员 → "Permissions" 页签 → 只授 "Telephony" 权限 → 点 Apply（协作服务交给 Teams 原生提供，Rainbow 侧收敛为仅电话集成）。
    3. 订阅分配：Members → 选成员 → "Services" 页签 → 选 Business 或 Enterprise（书中例 Enterprise）→ 点 Apply。
  verification: |
    书中本章为纯配置序列，无独立测试问题；效果验收由 c14 的登录启动与在场同步测试承接。
  conditions: Rainbow for Teams 应用已在租户上架并同意权限（c12）；用户需 Business/Enterprise 订阅。
  tags: [lab, teams, user-configuration, permissions, subscription]

- id: c14
  title: Teams 连接器安装与 Teams/Rainbow 在场同步激活
  type: lab
  source_pages: p236-244
  source_chapter: Rainbow for Teams installation — "Install Rainbow for Teams connector / Activate the presence status synchronisation between Teams and Rainbow"
  source_quote: |
    "Click on 'Apps' icon … you can find it by clicking 'Built for your org'" (p237)；
    "THE RAINBOW APPLICATION INTEGRATED INTO TEAMS REQUIRES THE INSTALLATION AND STARTUP OF THE RAINBOW
    DESKTOP APPLICATION ON THE PC." (p239)；
    "we activate the sharing of information with Office 365 … Synchronization is now active." (p243)；
    "Rainbow presence status is now synchronized with Teams one" (p244)
  steps: |
    1. Teams 内点 "Apps" 图标 → 若应用已为组织添加，从 "Built for your org" 找 Rainbow（也可能被直接推荐）；否则用搜索 → 找到后点 "Add" → 新窗口再点 "Add" 确认安装。
    2. 登录启动：点 "Sign in"；若管理员未预先同意权限，此处会提示用户自行接受（书中技巧：首次从管理员账户往 Teams 里加应用，可为全组织验证权限）。
    3. Desktop 依赖：Teams 内 Rainbow 应用要求 PC 上已安装并运行 Rainbow Desktop；若未启动，应用显示 "!" 图标 → 移入点击 "Start" → 点 "Rainbow desktop" → 点 "Continue"；Desktop 启动后提示窗自动消失（若此前 Desktop 未登录过需输入凭证；示例用 Microsoft 凭证 SSO 登录 Rainbow——书中强调连接器不强制要求 SSO）。
    4. 连接成功标志："!" 图标被 Rainbow 图标取代，表示应用已激活并连接；Rainbow Desktop 可最小化。
    5. 同步前基线测试：改 Teams 在场状态（例 Busy）→ 查看 Rainbow 侧在场信息 → 此时应不同（日历/在场同步尚未开启）。
    6. 激活同步：点设置图标 → 勾选与 Office 365 共享信息 → 选用户账户 → 提示 "Synchronization is now active" → 点 Close。
    7. 复测：再改 Teams 在场状态（例 Busy）→ Rainbow 侧在场随之同步。
  verification: |
    前后对照行为验证：激活前 Teams 与 Rainbow 在场不一致（p242）；激活后 "Rainbow presence status is now
    synchronized with Teams one"（p244）。
  conditions: Rainbow Desktop 应用已装于 PC（必须且须运行）；O365 账户可用；应用权限已同意（c12）。
  tags: [lab, teams, connector, presence-sync, o365]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 18 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 网络前提核查与 Pilot 评估 | 无实验。概念章（p35-45），Pilot 为外部工具介绍页，书中无分步实验。 |
| task-02 公司体系创建（BP 建 EC、可见性、SSO） | 无独立实验章。p46-55 为概念讲义；实验中公司/PBX 一律以"已由经销商/讲师创建"为前提（见 c03 步骤 1、c04 conditions），书内未演公司创建操作。 |
| task-03 管理员权责、企业目录、信息频道 | 无实验。概念章（p56-62），目录/频道的启用-创建序列仅截图级，无 How-To。 |
| task-04 订阅开通与分配 | 无独立实验章，但实验口径贯穿：c04/c05 分配 Enterprise 订阅、c10 订购 Attendant Monthly（p66 "During LAB use ONLY Voice MONTHLY subscriptions, DO NOT USE YEAR PREPAID"）。 |
| task-05 安装 OMC 并首次连接 | 有 → c01 |
| task-06 修改 OXO 与客户端 IP | 有 → c02 |
| task-07 PBXID+激活码接入 Rainbow 并验证 | 有 → c03（含 Webdiag "connected with final password"、ccrbagent.log、用户日志三个排障抓手） |
| task-08 成员创建与管理 | 有 → c04（手动建 user1）、c05（邀请建 user2 + 分配 Enterprise + 功能测试）。删除宽限/密码策略/CSV 批量/Azure AD 为概念页（p94-100），无实验。 |
| task-09 分机关联与 RCC 验证 | 有 → c06（含 p116 三项 RCC 测试问题） |
| task-10 WebRTC 拓扑决策 | 无实验。三拓扑对比与自动配置边界为讲义（p117-123），属决策内容非操作序列（决策依据已浓缩进 c07 的 conditions/verification）。 |
| task-11 按拓扑部署网关 | 有 → c07（讲义级操作序列：OCE-FE FTR p130-131、外部 VM p139-142、NUC p144-145；非 How-To 实验章，生产口径指向 Rainbow WebRTC cookbook）。 |
| task-12 容量规划 | 无实验。p146-147 为容量对照表（查表决策，非操作序列），留给概念/参数类提取器。 |
| task-13 内部网关自动配置 | 有 → c08 |
| task-14 虚拟终端配置（Twinset/Anydevice） | 有 → c09（含 p161 路由切换测试清单） |
| task-15 Attendant 话务台与监督组 | 有 → c10 |
| task-16 互助监督组 | 有 → c11（行为口径引自 p171-172 讲义） |
| task-17 维护体系排障 | 无独立 How-To 实验。p182-194 为概念讲义（状态页/告警/操作历史/SR）；维护排障操作已部分嵌入 c03（Webdiag、ccrbagent.log、用户日志三步）。 |
| task-18 Teams 集成全流程 | 有 → c12（上架+权限同意+Azure 核验）、c13（用户配置）、c14（连接器+在场同步） |

**统计**：14 条（lab 13 条 + howto 1 条）；18 项任务中 11 项有案例类条目直接覆盖，7 项为概念章或查表内容无实验（task-01/02/03/10/12/17 无实验，task-04 以实验口径分散覆盖）。
