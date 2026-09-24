# 案例/实验/操作序列候选 — OXO Connect Advanced (OXOCXTE301EN Ed18)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号、DDI）标注"实验口径"。
> 条目说明: 全书 24 个 How-To 实验章 → 24 条（每章一条，步骤保留精确菜单路径）。

```yaml
- id: c01
  title: OMC 安装与首次连接 OXO（证书安装、改密、客户信息）
  type: lab
  source_pages: p23-32
  source_chapter: OMC Installation — "Install OMC, connect to the PCX"
  source_quote: |
    "Make a connection to the system with OMC in Expert mode with server authentication" (p28)；
    "In order to avoid displaying the security alert at each connection, you must install the certificate the 1st time." (p29)；
    "The icon on the bottom right shows that you are connected to the OXO" (p32)
  steps: |
    1. RLab 中用 console mode 连接 PC Client 虚机 OXOC_PC_CLIENT；桌面 SOFTS OXO CONNECT 目录解压 OMC 安装包（实验口径）。
    2. 双击 setup.exe 选 "Run as administrator" → 选安装语言 → OK → Next。
    3. 选 Destination folder → Next；选目标 Country/Distribution Channels（可多选）→ Next；选 Target Product → Next；选 OMC 显示语言 → Next；Install → Finish。
    4. 打开 OMC 应用 → Expert 菜单 → LAN/WAN 连接方式。
    5. 输入 OXO 出厂 IP 192.168.92.246（实验口径），勾选 "Server authentication"，输入首次登录安装密码 pbxk1064（实验口径，仅第一次连接使用）。
    6. Security Alert 弹窗 → View certificate → Install certificate → 存储区选 "Trusted Root Certification Authorities" → OK → Finish → 导入成功 OK（此后连接不再弹安全告警）。
    7. 按讲师给定值（实验口径）为各账户设置新密码，"每个客户的密码必须不同"；后续可在 OMC/Security 菜单再改。
    8. 录入客户信息（带 * 必填，首次连接 OXO 强制）；可选录入供应商信息（实施技师联系方式）。
  verification: |
    书中验收点：OMC 右下角图标显示已连接 OXO，即 "OMC is ready to start with the customer configuration"（p32）。
  conditions: OXO 处于出厂默认状态；安装包在桌面 SOFTS OXO CONNECT 目录（或 NAS 网络盘）。
  tags: [lab, omc, installation, first-connection]

- id: c02
  title: OXO Connect 与客户端 PC 的 IP 规划修改
  type: lab
  source_pages: p33-36
  source_chapter: OXO Connect IP settings modification
  source_quote: |
    "With the OMC, change the OXO Connect IP settings" (p34)；
    "Click OK & Re-start the OXO Connect" (p35)；
    "Change the IP settings of the client PC (OXO_PC_CLIENT)" (p36)
  steps: |
    1. OMC/Hardware and limits/Lan/IP configuration，打开 Lan/IP configuration。
    2. Boards 页签：Main CPU 填 192.168.1.246（实验口径）。
    3. LAN Configuration 页签：Mask 255.255.255.0；Default Router Address 192.168.1.254（实验口径）。
    4. DNS 页签：DNS 1 = 192.168.1.250；DNS 2 = 10.20.30.250（实验口径）。
    5. DHCP 页签：话机地址池 Start 192.168.1.30 / End 192.168.1.39（实验口径；注意 p40 检查清单写 .10-.39，见 counter-example）。
    6. 点 OK 并重启 OXO Connect。
    7. 改客户端 PC（OXO_PC_CLIENT）IP：IP 192.168.1.10 / 掩码 255.255.255.0 / 网关 192.168.1.254 / DNS1 192.168.1.250 / DNS2 10.20.30.250（实验口径）。
    8. 虚拟课堂口径：IP 生效后改用 "Remote Desktop Connection"（RDP）重连 Client PC VM。
  verification: |
    RDP 能重新连上 Client PC VM（p34 实现说明）；后续实验均以新网段可达为前提。
  conditions: c01 已完成（OMC 可连 OXO）。
  tags: [lab, ip-planning, oxo]

- id: c03
  title: 公网 SIP 网关配置与注册验证（ITSP1G1）
  type: lab
  source_pages: p37-56
  source_chapter: Public SIP Gateway — "Configure a public SIP Gateway"
  source_quote: |
    "OMC/History and Anomalies/History Table … Message displayed: SIP registration success" (p54)；
    "In the menu at the left select TCP Dump traces … Choose SIP … And start the capture" (p55)
  steps: |
    1. 核对 LAN IP（OMC/Hardware and Limits/LAN IP Configuration：Boards 192.168.1.246；DNS1 192.168.1.250、DNS2 10.20.30.250；Default Router 192.168.1.254，改后复位 OXO；DHCP，实验口径）。
    2. 公网编号计划：OMC/Numbering/Numbering Plans/Public Numbering Plan——DDI 订阅户段 41100-41199、话务台 41000；必要时复制配置到 Restricted Public Numbering Plan。
    3. 安装号：OMC/Numbering/Installation Numbers 填 210P41000（实验示例 +33 (0)2 10 1 41000）。
    4. VoIP 接入：OMC/External Lines/List of Accesses/VoIP details——8 通道、Public network、放入主中继组 "0"；网关索引暂空（网关建好后回填）。
    5. 中继组：OMC/External Lines/List of Trunk Groups/Details 点 Add 加入 VoIP 接入；Link-Cat 页签（…/Details/Link-Cat.）调值放行外呼并查 barring。
    6. 建网关：OMC/External Lines/SIP/SIP Gateways——General tab：Index 1、标签 ITSP1G1、SIP numbers format index 1（canonical）、End of dialing table used；DNS tab：DNS A 192.168.1.250；Domain Proxy tab：Target/Local domain 与 Realm = sip.itsp1.fr、Outbound Proxy = gateway1.itsp1.com（必须先填 DNS tab）；Registration tab：Registration requested、Registrar sip.itsp1.fr；Media tab：验证 RTP Direct、带宽最少 5 通话；Identity tab：Use RFC 3325；Protocol tab：默认；Topology tab：ETH0；Security tab：明文（默认）。
    7. SIP 账号：OMC/External Lines/SIP/SIP Accounts 右键 Add——Login pbxP、Password alcatel、Registered username pbxP（P=POD 号，实验口径）、Gateway Parameters Index=ITSP1G1。
    8. 回到 OMC/External Lines/List of Accesses，把新建网关联到 VoIP 外线（回填 Gateway index）。
    9. 验证注册：OMC/History and Anomalies/History Table。
    10. 呼叫测试：打自家 DDI 0210P41150…或模拟器公网号 (0) 0210P12345 或其它 POD。
    11. 抓包：OMC/Tools/Webdiag（installer / Alcatel1，实验口径）→TCP Dump traces 选 SIP→开始抓包→呼叫→停止（自动生成文件）→PC/Wireshark 分析。
  verification: |
    History Table 显示 "SIP registration success"（p54）；Wireshark 能看到 SIP 消息流（p56）。
  conditions: 依赖 c01/c02；ITSP1 模拟器在 RLAB 公共区；短号与紧急号码不在本实验范围（无 ADL 表管理，p39）。
  tags: [lab, sip-gateway, public-trunk, wireshark]

- id: c04
  title: 酒店模式部署（Wizard Hotel、参数、计费、旋转 DDI、房态）
  type: lab
  source_pages: p69-75
  source_chapter: Configuration of the Hotel application
  source_quote: |
    "Switch the OXO Connect in hotel mode thanks to the initial installation Wizard Hotel • Make a cold reset (by default the OXO is in Business mode)" (p70)；
    "OMC/Miscellaneous System/Hotel Parameters" (p71)
  steps: |
    1. 冷复位后进 hotel 模式：OMC\Installation Typical\Initial Installation Wizard (Hotel)。
    2. 酒店通用参数：OMC/Miscellaneous System/Hotel Parameters——配置 check-in 序列（Deposit/姓名/wake-up/DND/语言/闭锁密码）、Do at check-in（系统性 DND+DDI 分配）、Room status 定时、默认语言、默认闭锁级别、默认 wake-up 时间、无操作退出 hotel 会话、默认组闭锁（房对房）。
    3. 酒店计费：OMC/Metering/Metering（tab Hotel Counting for Active Currency）——货币、VAT、预付金额、预付耗尽切断、切断前蜂鸣阈值、房间计费 3 级 2 阈、附加服务、小票脚注（≤40 字符）。
    4. Call Accounting Time based：OMC-metering 节点新 tab——激活功能、按呼型（Int/Nat/Loc，基于安装号屏幕）定义每类脉冲秒数（注意激活后 AOC 脉冲停用）。
    5. 旋转 DDI 核查：OMC/Dialing/Dialing Plans（tab Public Dialing Plan）——客房 DDI 段配 "Guest DDI unassigned" 功能，check-in 时自动分配首号并切 "Guest DDI assigned"（书例：8540 分配给 117 房）。
    6. 房态：OMC/Dialing/Dialing Plans（tab Internal Dialing Plan）确认房态前缀（例 88）；OMC/Users/Base Stations List 选用户 Details → Hotel key 查看 Terminal Class（Normal/Guest/House Phone）、Guest status、Room status、Room problem。
  verification: |
    书中为讲义式配置章（无独立 test 节）；行为验收在 p75：房态前缀拨号与 Base station 详情的 Hotel 页字段显示。
  conditions: 冷复位进 hotel 模式（默认 Business 模式）；OHL/PMS 联动为概览章内容（p57-68），本实验走无 OHL 的前台话机路线。
  tags: [lab, hotel, wizard, metering]

- id: c05
  title: Office Link Driver 安装与 TicketCollector.xml 生成
  type: lab
  source_pages: p88-91
  source_chapter: Office Link Driver — "Install the Office Link Driver and generate a TicketCollector.xml file"
  source_quote: |
    "Enable: External metering Activation IP … OMC \ Metering \ Metering" (p89)；
    "Check the tickets generated in TicketCollector.xml file … C:\Users\Public \Public Documents\TicketCollector.xml" (p91)
  steps: |
    1. 启用 IP 计费：OMC \ Metering \ Metering 勾选 "External metering Activation IP"（外呼时 OXO 生成 IP Metering Ticket）。
    2. PC 上安装 OLD 驱动（桌面安装包）：右键 setup.exe 选 "Run as administrator"。
    3. 安装中选择 Metering mode。
    4. 从桌面图标启动 Configuration Application：①输入 OXO IP 地址；②输入管理员密码（OMC 菜单 Security/Passwords/Management passwords 所建）；③点 TestConnection（应用显示 OXO 软件版本）；④启动应用。
    5. 打外部电话生成计费小票。
    6. 用浏览器（或 IE）打开 C:\Users\Public\Public Documents\TicketCollector.xml 检查小票。
  verification: |
    TicketCollector.xml 中出现外呼计费小票记录（p91；归档文件为 TicketCollector_X.xml，X 为日期时间，p80）。
  conditions: 依赖 c03（外呼通道可用）；OLD 另有 Hotel application 模式（提供 OHL 接口，p80）。
  tags: [lab, metering, office-link-driver, xml]

- id: c06
  title: 账号码与内部替代配置及测试
  type: lab
  source_pages: p97-101
  source_chapter: Account codes/Internal Substitution code
  source_quote: |
    "Create a code 123456 with a name CLIENT A … Masked digits = 4" (p98)；
    "Test: lock a set and from this set call externally by pretending to be the manager ex. 101: dial 66-101-142536-0-0210x41100" (p101)
  steps: |
    1. 建账号码：OMC/Traffic sharing and barring/Account Code Table——码 123456、名 CLIENT A、User ID=No、Ptct=No、掩码 4（小票遮 4 位）。
    2. 建账号码前缀：OMC/Numbering/Numbering plans/Internal numbering plan——前缀 69，Function: Account code new；用 IPDSP 打电话测试并查 ticketcollector.xml 小票。
    3. 建可编程键：OMC/Users-Base stations List/User details/Keys——给 IPDSP 104 建 "account code new" 功能键并选刚才的账号码；测试并查小票。
    4. 内部替代：OMC/Numbering/Numbering plans/Internal Dialing plan——建/核对前缀 66（New Account Code，base 1000 指向既有账号码 1000 SUBSTITUTION）；（亦可走 Keys 建 Feature key: Account Code New 1000，p101 Tips）。
    5. 闭锁配合：barring 表 N°3 删除 00 禁止项，把经理话机的闭锁类别改为 3（放行国际）。
    6. 测试：锁定一台话机，从它拨 66-101-142536-0-0210x41100（142536 为经理 101 密码，实验口径）以外呼 DDI。
  verification: |
    计费小票 ticketcollector.xml 中出现带账号码的记录（p99/p100 步内验收点）；锁定话机经 66 前缀以经理身份外呼成功（p101）。
  conditions: 内部替代默认预编在内部编号计划与账号码表（p96）；虚拟课堂用 IPDSP 测试。
  tags: [lab, account-code, substitution]

- id: c07
  title: 站群监督两键配置（Supervision Groupware + Audio Signal）
  type: lab
  source_pages: p116-118
  source_chapter: Stations groups supervision
  source_quote: |
    "OMC/ Subscribers Basestations List / select one set details / Keys / Select a free Key / Feature Key: Supervision Groupware" (p117)；
    "Validate and test, do not forget to activate the key on the supervisor set." (p117)
  steps: |
    1. 取一台话机作监督台，监督另外两台（含其内部号与 DDI 号）。虚拟课堂用 IPDSP 测试。
    2. 监督键：OMC/Subscribers Basestations List/选监督台 Details/Keys/选空闲键/Feature Key: Supervision Groupware——Monitored No 填要监督的内部与 DDI 号；同时勾 Audio control 使监督台有蜂鸣。
    3. 验证并测试——别忘了在监督话机上激活该键。
    4. 音频开关键：OMC/Subscribers Basestations List/选监督台 Details/Keys/选空闲键/Feature Key: Audio Signal Supervision——该键在监督台上开关蜂鸣。
    5. 测试：监督台不摘机应收到被监督来话通知（pop-up+音调+键闪烁），可用该键接听或关闭通知。
  verification: |
    被监督话机来话时监督台出现通知（pop-up 显示主被叫、Audio 蜂鸣、Groupware 键闪烁），并能应答（p112 描述的行为闭环；p117 "Validate and test"）。
  conditions: 监督方仅 DeskPhones；每键最多 8 号码、系统 50 键；priv=yes 呼叫不可监督（p114）。
  tags: [lab, supervision, groupware]

- id: c08
  title: PIMphony 安装、预配置与可编程键（物理话机 + PC Multimedia 两形态）
  type: lab
  source_pages: p126-138
  source_chapter: PIMphony installation
  source_quote: |
    "Central Services Global Info / PIMphony tab. Check the field 'Activated', then choose the option 'Periodically 5 weeks'" (p127)；
    "PIMphony lab not feasible in Virtual Classroom … Procedure example" (p129)
  steps: |
    1. 开全局在线更新：OMC 应用 → Central Services Global Info/PIMphony tab——勾 Activated、Update frequency 选 "Periodically 5 weeks"（实验口径；默认停用）。
    2. 每用户预配置（100 话机）：OMC → Subscribers/Basestations List/Set 100/Details/Serv.Cent/PIMphony tab——profile 选 "Team"；勾 Use customized policy、Periodically 6 周（实验口径）；（Miscellaneous 区只读：Device type/TAPI mode/Mac address）。
    3. 安装 PIMphony 并关联物理话机 101：Business Portal 下载的解压目录双击 install→语言 English→（必要时装 Microsoft 组件）→接受许可→选安装目录→Install→Finish→进入配置向导：填 OXO IP（192.168.X.246，X=节点号，实验口径）→下拉选话机 101 并填其密码（默认密码会强制改）→确认 profile 选 Team→填拨号属性→安装完成；PIMphony 注册 on-site 需互联网，实验选 "Cancel"；启动应用。
    4. 可编程键：PIMphony 应用右键可编程键逐个建——键 1 直拨 102、键 2 立即转接目的地 100、键 3 Do Not Disturb、键 4 deflect 到 103。
    5. 呼叫监督：File/Open/Supervision 打开监督窗；呼叫 103 看 "Ringing" 图标出现。
    6. PC Multimedia（PIMphony IP）形态：OMC → Subscribers/Basestations List/Add——选 "IP terminal" 建号 222、类型改 "PC Multimedia"；在其 Details → Serv.Cent → PIMphony tab 选 "Operator" profile；再跑配置向导关联 222；音频向导配扬声器与麦克风（向讲师领耳麦测试）。
  verification: |
    书中无独立 test 节；验收点为配置完成提示窗（p134 "This window indicates that PIMphony is installed and configured properly"）与监督窗 Ringing 图标（p135）。
  conditions: 虚拟课堂不可实操（仅过程示例）；profile 与版本依赖 license（p123）。
  tags: [lab, pimphony, softphone]

- id: c09
  title: Open SIP 软话机接入（Zoiper）
  type: lab
  source_pages: p155-165
  source_chapter: SIP Soft phone — "Configure and use a SIP soft phone"
  source_quote: |
    "Don't modify any existing MicroSIP softphone" (p156)；
    "Add port 5059 to the Domain … 192.168.1.246:5059 … When leaving the menu do not forget to save by 'Yes'" (p164)
  steps: |
    1. OXO 侧声明：OMC\Subscribers Basestations List → Add 新用户为 "IP Terminal"（选分机号如 105、命名）→ OK → 点 Modify 把终端类型改为 "Open Sip Phone" → Details → "IP/SIP" 按钮 → 在 SIP Parameters tab 读/复制该终端的 SIP 密码。（勿改既有 MicroSIP。）
    2. PC 装 Zoiper（SOFTS OXO CONNECT 目录，右键 Run as administrator）→ Next 按默认答完 → Finish（自动启动；需接耳麦）→ "Continue as a Free user" → 不更新。
    3. 登录：Login 填 105@192.168.1.246（实验口径）→ 填上一步读到的 SIP 密码。
    4. 域名：输入 OXO @IP 192.168.1.246 → Skip → Skip → Yes。
    5. 设置：Settings 菜单 → SIP Accounts → Domain 加端口 192.168.1.246:5059 → 离开菜单时记得保存 Yes。
    6. 测试：从另一台 OXO 话机呼叫这个新终端。
  verification: |
    Zoiper 注册成功并能接听来自其它话机的呼叫（p165 "Test by making a call from another OXO station to this new terminal"）。
  conditions: 端口 5059 为 OXO SIP 注册/代理端口（p153）；注册计时器 ≥120 秒。
  tags: [lab, sip-softphone, zoiper, open-sip]

- id: c10
  title: Hot Desking 配置与监督（HDP/HDU/前缀/双通道监督）
  type: lab
  source_pages: p178-183
  source_chapter: Hot Desking — "Configure the Hot Desking function"
  source_quote: |
    "Select: 'Hot Desking set' … Deactivate the feature at the end of the lab" (p179)；
    "By the 'Log out' button it is possible to force the disconnection of a user" (p182)
  steps: |
    1. 声明 HDP：OMC/Subscribers-Basestations List——选一台空闲 Premium/ALE Deskphone，勾选 "Hot Desking set"。（实验结束记得停用该功能。虚拟课堂用 IPDSP。）
    2. 建 HDU：OMC/Subscribers-Basestations List → Add → 选 "Hot Desking User"，N° 122、Name Philippe（实验口径）。
    3. 前缀：OMC/Numbering/Numbering Plans → 内部编号计划中识别既有 Hot Desking 函数——682=注销、683=登录（实验口径默认值）。
    4. Webdiag 监督：经 OMC "Tools" 菜单进 Webdiag（User: installer，Password=installer 密码）→ "Services" tab——看哪个用户登录在哪个位子；用 "Log out" 按钮可强制断开用户。
    5. 订阅户菜单监督：OMC/Subscribers-Basestations List——点 HDP 话机 Details 看当前登录者；在 HDU 详情里看它登录在哪个 HDP。
    6. 测试：HDU 在 HDP 上以前缀 683+密码登录取回个人环境；用 682 注销。
  verification: |
    Webdiag Services 与 OMC 双向显示 HDU↔HDP 对应关系（p182-183）；登录后呼叫日志/VM/路由等个人环境随人走（p174 特性描述）。
  conditions: 需 license（前 2 HDU 免费，后按 50 包）；抢占登录自动注销前一 HDU（p175）。
  tags: [lab, hot-desking, webdiag]

- id: c11
  title: Multiset 配置与七项行为验证
  type: lab
  source_pages: p190-192
  source_chapter: Multiset configuration
  source_quote: |
    "OMC/ Users-Base stations list/ Primary user details … Click on 'Add' to add 102 as secondary set." (p191)；
    "The primary set and the secondary set ring simultaneously." (p191)
  steps: |
    1. 配 multiset：OMC/Users-Base stations list/主用户（101）Details → "…" 键开 multiset 配置菜单 → Add 副站 102。（虚拟课堂用 IPDSP 做主站。）
    2. 呼主站：主副同时振铃。
    3. 呼副站：仅副站振铃。
    4. 副站呼出：对端显示的 CLI 为主站号。
    5. 副站转移：把副站转移到另一分机后呼主站——呼叫按转移走。
    6. 寻线组：把主站加入寻线组后组呼——主副两台按组呼同时振铃。
    7. 经理/秘书组：把主站配为秘书、对经理启用 screening，呼经理——主副同时振铃。
  verification: |
    七个行为问题各有明确预期答案（p191-192 逐条给出结果，如 "Only the secondary set rings."、"The displayed number is primary."）。
  conditions: 副站共享主站功能与忙态（p186-187）；空闲副站新呼叫铃型由 MLTSETRING 控制（默认不铃）。
  tags: [lab, multiset, twinset]

- id: c12
  title: 私网 SIP 组网与 ARS 双向溢出（两台 OXO）
  type: lab
  source_pages: p206-224
  source_chapter: Private SIP network with ARS
  source_quote: |
    "Add a line Secondary Trunk Group base ARS … And set the NMT parameter to Keep … And Pivate to Yes" (p219)；
    "Test the forcing by calling an OXO 2 extension by its DID number, the ARS must force the call to take the correct VoIP path (P on the caller's display)" (p224)
  steps: |
    1. 拓扑（N=lab 号，实验口径）：OXO1 主 CPU/VoIP 192.168.N.246、内部 100-199、公网 DID 1100-1199、私网 1100-1199；勿与其它 lab IP 冲突。
    2. LAN IP：OMC/Hardware and Limits/LAN IP Configuration——Boards（192.168.N.246）、DHCP、Default Router Address；改后复位 OXO。
    3. 私网编号计划：OMC/Numbering Plan/Numbering Plans/Private Numbering Plan——加 N100-N199 base 100（lab1 例 1100-1199）。
    4. 私网 VoIP 接入：OMC/External Lines/List of Accesses——按客户带宽加 VoIP 通道，留 Private network；OMC/External Lines/List of Trunk Groups/Details 建副中继组（可命名 VoIP）；…/Link Category 按需调整并查 discrimination。
    5. 私网 SIP 网关：OMC/External Lines/SIP/SIP Gateways/Create——General：Index 1、canonical、用 End of dialing；Domain Proxy：填对端站点参数（OXO1 填 OXO2 的 192.168.2.246，实验口径）；Registration：默认；Media：带宽最少 5 通话+Direct RTP；DNS/Identity/Topology：默认；Protocol：选 SIP Option 作监督协议。
    6. 关联网关：OMC/External Lines/List of Accesses 把私网网关联到外线。无 ARS 测试：经中继组前缀 400 呼对端私网号（OXO1 打 (400) 21xx）。
    7. 配 ARS：OMC/Numbering plan/Numbering plans/Internal numbering plan——加 Secondary Trunk Group 行（如打 OXO2 的 21xx）base ARS、NMT=Keep、Private=Yes；OMC/Numbering Plan/Automatic Route Selection/Automatic Routing Prefixes 加行（填对端前缀区间）；…/Trunk Group Lists 加行指向含 VoIP 接入的中继组。带 ARS 测试：直拨 21xx。
    8. 公网溢出接入：OMC/External Lines/List of Accesses 用 T0 并确认物理服务在；OMC/External Lines/List of Trunk Groups 把 T0 放入主组 0；…/Details/Link category 按需调整；OMC/Numbering/Numbering Plans/Public Numbering Plan 填 DID 1100-1199（必要时复制到 Restricted）；OMC/Numbering/Installation Numbers 填安装号（lab1 例 +33 (0) 2 01 53 1100）。测试公呼 (0)020153N100。
    9. 私→公溢出：OMC/Numbering/Automatic Routing Selection/Automatic Routing Prefixes 给私网行加溢出子线（指向公网）；…/Trunk Group Lists 加 index 2 行指向主中继组 0。测试：先占满 2 个 VoIP 通道再呼 OXO2 用户，主叫显示应出现正确字符（如 T）。
    10. 公→私优先强制：内部编号计划把主中继行 base 改 ARS；Automatic Routing Prefixes 加"公网强转私网"行+私网饱和时"公到公"子线+其它公网目的地透明行。测试：以 DID 呼 OXO2 分机，ARS 应强制走 VoIP（主叫显示 P）。
  verification: |
    四个里程碑：无 ARS (400)21xx 通、带 ARS 直拨 21xx 通、占满私网后溢出显示 T、DID 呼叫被强制走私网显示 P（p218/219/223/224）。
  conditions: 私网通道数按带宽勘测；实验拓扑由讲师给 N 值。
  tags: [lab, private-sip, ars, overflow, multi-site]

- id: c13
  title: Internal ARS 按日组/时段路由同一 DDI
  type: lab
  source_pages: p232-241
  source_chapter: Internal ARS management
  source_quote: |
    "Select the function 'Secondary trunk group' … Enter 41102 as 'start' and 'end' and fill out the 'Base' field with 'ARS'" (p234)；
    "Record a MSG1 welcome message with opening hours and Add it to an unused hunting group" (p241)
  steps: |
    1. 架构（实验口径）：打 DDI 021PN41102——周一至五 8-12 点转 101、12-14 转 102、14-18 转 103、18 点-次日 8 点及周六日播营业时间消息（501 寻线组挂消息）。
    2. 公网编号计划：OMC/Numbering/Numbering plans/Public Numbering plan tab——选 "Secondary trunk group"，start/end 填 41102，Base 填 ARS，Add。
    3. ARS 前缀：OMC/Numbering/Automatic Routing Selection/Automatic Routing: Prefixes——右键 Add，填 021PN41102（pod01 例 0210141102），再 "subline add" 3 次（每行一个目的地：分机、分机、消息寻线组），Apply。
    4. Provider：OMC/Numbering/Automatic Routing Selection/Automatic Routing: Prefixes/Providers Destination——右键加 4 行并命名（如 Extension 101/102/103/Message）。
    5. 中继组列表：OMC/Numbering/Automatic Routing Selection/Trunk Group Lists——右键 Add 列表；每行 Index 选 "Local"（内部 ARS 用的虚拟中继组）；Provider 列选对应 Provider；Apply。
    6. 日组：OMC/Numbering/Automatic Routing Selection/Day Groups——周六日设组 1，其余天设组 2（实验口径）。
    7. 时段：OMC/Numbering/Automatic Routing Selection/Hours——Add 建 4 时段（8am-12pm、12pm-2pm、2pm-6pm、6pm-8am；段尾=下一段起点），每组 1/组 2 各配目的地；Apply。
    8. 欢迎消息：OMC/Hunting group——录 MSG1 营业时间欢迎消息并挂到未用寻线组（也可 MMC 话务员会话 Operator session/Expert menu/Voice/Hold music/Message 1 或 OMC 导入；勿与实体 MoH 混淆）。
    9. 测试：在不同时刻从其它话机打 021PN41102，核对四时段目的地。
  verification: |
    各时段呼叫分别到达 101/102/103/欢迎消息寻线组（p241 "Test your settings by calling the DDI number … at different moments of the day"）。
  conditions: 时段口径 p233（12-13、13-18）与 p449（12-14、14-18）不一致，复现时任选其一并在文档注明（见 counter-example）。
  tags: [lab, internal-ars, time-routing]

- id: c14
  title: 多实体隔离与伪多公司分账
  type: lab
  source_pages: p252-261
  source_chapter: Multi entity and multi company
  source_quote: |
    "OMC/ Subscribers-Base stations List / select a set / Details / Entity … Put extensions 102 and 103 in entity 2" (p254)；
    "OMC/ Numbering / Automatic Routing Selection / Trunk Groups Lists … Put Char 1 for the company 1 … Put Char 2 for the company 2" (p261)
  steps: |
    1. 拓扑：100/101 属实体 1，102/103 属实体 2；实体间禁呼；每实体独立 MoH（MoH1/MoH2）。（MoH 无 .wav 时用 MMC 话务员会话录制。）
    2. 实体分布：OMC/Subscribers-Base stations List/选话机/Details/Entity——把 102、103 放实体 2（默认全在实体 1）。
    3. 禁实体间呼叫：OMC/System miscellaneous/Feature design/Part 1——勾 "Do not allow calls between entities"；验证跨实体呼叫被禁。
    4. 按实体录 MoH：OMC/System miscellaneous/Message & Music/Music on hold——为实体 1、实体 2 各加载 MoH（或 MMC Operator session/Expert menu/Voice/Hold music/MUSIC 1、MUSIC 2；勿与 MSG1-20 欢迎消息混淆）。
    5. 话机链路类别：OMC/Subscribers-Base stations List/选话机/Details/Barring——公司 1 话机流量分担链路类别=1、公司 2 话机=2（实验口径）。
    6. 分公司中继组：OMC/External Lines/List of Trunk Groups——管 400 与 401；…/Details 分别把 400 类别设 1、401 类别设 2。
    7. 流量分担矩阵：OMC/Traffic Sharing and Barring/Traffic Sharing Matrix——按讲义矩阵配置；验证呼叫。
    8. ARS：OMC/Numbering/Numbering Plans/Internal Numbering Plan 把主中继行 base 改 ADL 进 ARS 表；OMC/Numbering/Automatic Routing Selection/Automatic Routing: Prefixes 右键加透明线（Trunk group list 1）；…/Trunk Groups Lists 建含两公司中继组的列表，Char 1 给公司 1、Char 2 给公司 2。
    9. 测试：两公司用户拨 0 外呼，话机显示字符 1 或 2 确认占了各自中继组。
  verification: |
    跨实体呼叫被禁、各实体保持时听各自 MoH、外拨显示对应公司字符 1/2（p255/256/261）。
  conditions: 多实体 MoH license（4 实体-10 分钟）；链路类别取值讲义（3/4）与实验（1/2）不同，取一套自洽即可。
  tags: [lab, entity, multi-company, traffic-sharing]

- id: c15
  title: OXO 注册 Cloud Connect 并核验状态
  type: lab
  source_pages: p286-289
  source_chapter: Register OXO Connect in Cloud Connect
  source_quote: |
    "OMC/Cloud/Cloud Connect … The status must be: Connected with final credentials" (p288)；
    "A delay of 24h is required to see the systems" (p289)
  steps: |
    1. 前提：系统接入客户网络并获得互联网访问（PC 192.168.1.10 / CPU 192.168.1.246 / 掩码 255.255.255.0 / 网关 192.168.1.254 / DNS 192.168.1.250，实验口径）——注册自动发生，默认启用、免 license。
    2. 核对 IP 设置：OMC/Hardware and limits/LAN/IP Configuration/LAN Configuration。
    3. 核验注册：OMC/Cloud/Cloud Connect——状态必须为 "Connected with final credentials"（默认即启用 Cloud Connect）。
    4. Fleet 演示：由讲师在 Fleet Dashboard 展示学员系统（Cloud Connect 数据库一天更新一次，需等 24 小时）。
  verification: |
    OMC/Cloud/Cloud Connect 状态显示 "Connected with final credentials"（p288）；次日 Fleet Dashboard 可见系统（p289）。
  conditions: Business Store 账号访问两门户；Fleet Dashboard 完整演示为讲师环节（p286 Summary 3）。
  tags: [lab, cloud-connect, registration]

- id: c16
  title: 语音邮箱高级管理（个人助理/远程接入/ACC/锁定/寻线组邮箱）
  type: lab
  source_pages: p394-404
  source_chapter: Voice Mail management (advanced features)
  source_quote: |
    "OMC/ Subscribers/Basestations List/ 103/ Mailbox/ Personal assistant" (p395)；
    "Now, your voice mail is locked for 10 minutes. You can see it in history table." (p402)
  steps: |
    1. 个人助理（103）：OMC/Subscribers/Basestations List/103/Details/Mailbox → "Personal assistant" tab——填三目的地：同事 101、外部 0210P41102、移动 0610P41101（实验口径）→ OK。
    2. 系统级激活：OMC/System Miscellaneous/Memory Read-Write/Other labels → 选 "PerAssAlwd" → Details → 值设 01 → Modify → Return（激活后各用户可在话机上自配）。
    3. 话机侧激活：呼叫语音邮箱组号→输邮箱号 103→密码→菜单 9 "Personal options"→菜单 2 "Personal assistant"→按 2 输入各号码（也可 Settings/Assistant 菜单）。
    4. 远程接入：OMC/Numbering/Numbering Plans → Public Numbering Plan——给语音邮箱寻线组分 DDI：Function=Hunting group、Start-End=41500、Base=500（全号 0210P41500，P=POD 号）。
    5. 只许外部查：OMC/Voice Processing/General parameters——取消 "Mailbox consultation from any phone"（禁止经同事话机查）；OMC/Subscribers Base Stations List/101/Details/Features/Part 3——勾 "Mailbox remote consultation"（放行外部查）。
    6. 两级控制：OMC/Security/Passwords/Remote Access Code——输入码 780911（实验口径；与远程替代同一密码菜单）。
    7. 锁定测试：拨 0210P41500 → 远程接入码 → 分机号 → 连续 3 次错密码——语音邮箱锁 10 分钟；查 History Table 对应消息；到期后再试。
    8. 远程定制授权：OMC/Subscribers/Basestations List/103/Features——勾 "Remote customization"；再经远程定制把 103 的个人助理配移动号+转话务员：拨邮箱组 DDI 0210141500 → 远程接入码 → 邮箱 103 → 密码 → 菜单 9 → 菜单 2 → 按 1 激活个人助理。
    9. 寻线组邮箱：按视频把 509 组关联虚拟分机 112 的邮箱（OMC 建邮箱+成员 VM 键）。
  verification: |
    锁定 10 分钟并见于历史表（p402）；远程激活个人助理后来话按助理目的地分发（p403 测试说明）。
  conditions: 锁定时长翻倍规则见 principle p26；PerAssAlwd/DivRemCust 默认均为 00 禁用。
  tags: [lab, voicemail, personal-assistant, acc]

- id: c17
  title: 自动话务员 AA 树与语音指南配置
  type: lab
  source_pages: p422-426
  source_chapter: Automated attendant
  source_quote: |
    "OMC/Voice Processing /Automated attendant – Greetings tab … From the reception of calls, the auto attendant asks question 'Press star'" (p423)；
    "Test all the tree structure choices." (p426)
  steps: |
    1. 树规划：press star 后一级菜单——1 会计部（子菜单）、2 销售部（子菜单）、3 General mailbox、4 转 104 语音邮箱、6 留言；二级——子菜单 1 转 101/102、子菜单 2 转 102/103（直接转分机，非寻线组）。虚拟课堂用 MicroSIP 呼 AA。
    2. 开 press star：OMC/Voice Processing/Automated attendant → Greetings tab 勾 "press star question"。
    3. 编辑主菜单：AA menu tab → Opening hours tab → AA Menu 按钮——按键 1/2 指向子菜单、3 General mailbox、4 转 104 邮箱、6 留言。
    4. 编辑子菜单：子菜单 1（键 1）转 101 与 102；子菜单 2（键 2）转 102 与 103。
    5. 录语音指南：MMC 话机 Operator session/密码/Expert/Voice mail/Auto attend./Day——录问候 "Welcome to my store"、主菜单五句、子菜单各两句；或经 OMC 导入。
    6. 测试：遍历树上全部选项；从话务台听 General mailbox 留言并转给 101，核对 101 邮箱收到。
  verification: |
    全树选项行为正确 + 留言从 General mailbox 成功转发到 101 邮箱（p426 Tests）。
  conditions: 树与语音定制需 license；转接模式默认半监督（AATypTrf=02）。
  tags: [lab, auto-attendant, tree, voice-guides]

- id: c18
  title: MLAA 多语言话务员树（ISP 场景）
  type: lab
  source_pages: p443-449
  source_chapter: MLAA-multiple automated attendant
  source_quote: |
    "OMC Session \ Multiple Automated Attendant \ MLAA Setup … Number of MLAA ports: 8 … Associate the DDI number 41509 with the hunt group 509" (p446)；
    "Call the automated attendant by its DDI number 021PN41509" (p449)
  steps: |
    1. 树规划（ISP 例）：DID 41509；问候 "Welcome to the Internet Provider"；语言选择英/法；菜单 1（订阅按 1/改合同按 2）→菜单 2（改套餐 1→菜单 3；解约 2→菜单 4）；菜单 3（WIFI？是 1→100、否 2→101）；菜单 4（ADSL 单套 1→101；ADSL+TV+电话 2→101/取消说明消息 msg007）。虚拟课堂只录单语（RDP 录音质量问题）。
    2. 话机录音：MMC Station/Menu tab/Operator session/Password/Expert/Voice mail/MLAA——MSG001 问候、MSG002 语言选择、MSG003-006 菜单 1-4、MSG007 解约说明。
    3. OMC 消息核对：OMC\Multiple Automated Attendant\MLAA Voice messages——已录消息应出现；语言 1/2 可经 OMC 导入导出。
    4. MLAA Setup：OMC Session\Multiple Automated Attendant\MLAA Setup——专用端口 8（ACD 与 MLAA 共享、上限 16 按 license）；DDI 41509 关联寻线组 509。
    5. MLAA Services：OMC Session\Multiple Automated Attendant\MLAA Services——验证第二语言、欢迎消息选 Msg 001、语言选择 Msg 002、错误转人工话务员；右键加菜单 Menu 1-4 并命名、分配消息（msg003 给菜单 1）；接线：菜单 1 按 1→菜单 2、按 2→菜单 4；菜单 2 按 1→菜单 3、按 2→101；菜单 3 按 1→100、按 2→101；菜单 4 按 1→跳转菜单 2、按 2→播 msg007。
    6. 线路参数：…\MLAA Services\Options 选 Line parameters——DDI 41509、Service opened: Tree 1。
    7. 传输：…\MLAA Services\Tools——先保存配置再 "Transfer to the server"（注意 line parameters 不随 Save as 存档）。
    8. 测试：拨 021PN41509 走完整树。
  verification: |
    拨 DDI 后按语言选择与各菜单按键到达对应分机/消息（p449 Tests）。
  conditions: 消息与端口改动在 ACD/MLAA 引擎复位后或 10 分钟无复位后生效；树数按 license（1/5）。
  tags: [lab, mlaa, tree, multi-language]

- id: c19
  title: Smart Call Routing 客户码路由
  type: lab
  source_pages: p459-462
  source_chapter: Smart Call Routing
  source_quote: |
    "OMC/ Call Distribution Services / ACD Setup / General tab … Manage the ACD Setup to include some ACD ports in the hunting group 510" (p460)；
    "Message client code of group 1 = 'please enter your client code and validate by #'" (p462)
  steps: |
    1. 目标（实验口径）：DDI 41510 来话——8:00-14:00 客户码 001→101、002→102、其它码→103；14:00 后→100。
    2. ACD Setup：OMC/Call Distribution Services/ACD Setup/General tab——把 ACD 端口放入寻线组 510（端口总数 16 与 MLAA 共享）；DDI 41510 关联组 510；Add。点 OK 后 ACD 端口自动入组 510、41510 自动建入公网编号计划。
    3. 录客户码提示：MMC 话务员站（Operator session/Expert/Voice/ACD/OK group 1/goto guide Code Client）或 PC 录 107.wav——"please enter your client code and validate by #"。
    4. 开闭时间：OMC/Call Distribution Services/ACD-SCR Services/General Parameters/SCR tab——SCR 服务开放 8am-2pm（周一至五）。
    5. 路由规则：OMC/Call Distribution Services/ACD-SCR Services/Smart Call Routing——CLI/DDI 填 021PN41510（pod01 例 0210141510）；三条规则：客户码 001（# 结束）→101、002→102、通配 x→103；开时段目的地=规则结果、闭时段目的地=100。
    6. 测试：打 41510 输不同客户码核对去向；14 点后核对全部到 100。
  verification: |
    客户码 001/002/其它分别到 101/102/103，闭时段到 100（p460 目标描述即验收标准）。
  conditions: 需 SCR license+1 Supervisor Console；64 特殊日与 ACD 共用。
  tags: [lab, scr, acd, client-code]

- id: c20
  title: 游牧模式与远程替代（含 # 前缀内部 ARS）
  type: lab
  source_pages: p472-480
  source_chapter: Mobility features and remote substitution
  source_quote: |
    "Tick: Nomadic right … Check the automatic creation of a virtual terminal, named 'Virtual Nomadic' with the Nomadic option" (p474)；
    "Once you've got the dial tone, dial an internal extension with '#' first." (p480)
  steps: |
    1. 拓扑（实验口径）：104 为用户主话机（IPDSP）；VM 组 DDI 021PN41500；游牧目的地 021PN41102；远程替代 DDI 021PN41200、欢迎消息 MSG1、接入码 615243；内部 ARS #100-#199→100-199、#9→话务员。
    2. 话机 104 定制邮箱：录名+改密码 142536（实验口径）。
    3. 游牧权：OMC/Subscribers BaseStations list/104/Details/Cent.Serv → User tab 勾 "Nomadic right"；核对自动创建 "Virtual Nomadic" 虚拟终端（带 Nomadic 选项）。
    4. VM 的 DDI：OMC/Numbering/Numbering plans/Public numbering plan——组 500 分配 021PN41500（P=POD 号），Add、OK。
    5. 远程权：OMC/Subscribers list/104/Details/Features——Part 2 勾 Remote customization、Part 3 勾 Mailbox remote consultation。
    6. 激活游牧：拨 VM DDI→远程接入码→邮箱 104→密码 142536→按 9 个人选项→按 6 游牧设置→输 0021PN41102 按 #→再按 # 确认；验证：104 显示 "Nomadic mode"、呼 104 转到 021PN41102；随后停用。
    7. VM 转移：拨 VM DDI→码→104→密码→9→7 转移设置→2 激活转移→目的地+#→# 确认；核对转移生效（noteworthy DivRemCust=01 才开放选项 7，默认 00 禁用）。
    8. 远程替代：OMC/Numbering/Numbering plans/Public Numbering Plan 给替代分 DDI 41200（021PN41200）；OMC/Security/Passwords/Remote Access Code 设码 615243（实验口径）；OMC/Subscribers list/104/Details/Features/Part 2 勾 "Remote Substitution"。
    9. 内部 ARS：OMC/Numbering/Numbering plans/Internal Numbering Plan——加 Secondary Trunk Group 段 #100-#199（避冲突）base ARS、TMN Keep、Private=Yes；OMC/Numbering/Automatic Routing Selection/Automatic Routing Prefixes 右键加行（Network=Priv、Prefix=#1、Range=00-99）；…/Trunk Groups Lists 行 Index=Local。
    10. 测试：打 021PN41200→听音→拨接入码→拨分机 104→拨其密码→拿到拨号音后以 "#" 开头拨内部分机。
  verification: |
    游牧：104 显示 Nomadic mode 且来话转到 021PN41102（p477）；远程替代：回环后能拨通内部分机（p480 Tests）。
  conditions: 虚拟课堂用 IPDSP 当主话机；远程接入码同时服务远程替代与远程 VM 接入。
  tags: [lab, nomadic, remote-substitution, ars]

- id: c21
  title: DECT 话机注册到 IBS（向导法）
  type: lab
  source_pages: p535-540
  source_chapter: DECT registration on IBS — "Register DECT handsets"
  source_quote: |
    "OMC\ Installation typical\ Wizard for DECT/PWT On-Air Registration … If the Wizard icon doesn't appear in the menu, go to 'Comm/Read all from PCX' to refresh the screen." (p537)；
    "From the DECT handset, call a wired extension with display. You should see the directory number of the DECT handset." (p540)
  steps: |
    1. 连 IBS：把 IBS 基站接到 OXO 机架 UAI 板空闲口（红 LED 慢闪=正常）。虚拟课堂不可实操。
    2. 话机复位：Menu（OK 键）→ 输 *7378423* → 选 "Master reset" → 重启进 Auto install 模式。
    3. 向导注册：OMC → Installation typical → 双击 "Wizard for DECT/PWT On-Air Registration"（图标不见则 Comm/Read all from PCX 刷新）；"Additional handsets to create" 填 1 → Next → 选空闲 DECT 接入 → 填订阅户名与 DDI → Next。
    4. 话机侧注册（第 4 节流程，假定出厂态）：Auto install? 答 yes → Register 选 select → Enter current PIN 0000 → empty 选 select → PARK 选 ok → Access code 选 ok（若配了 GAP 认证码则输入）→ Power mode 选 Normal。
    5. 回 OMC：话机 IPUI 出现在 "Unassigned IPUIs" 窗口后选中点 "Assign"；结束窗选 "Yes, finish"。
    6. 测试：话机呼一台有显示话机核对自己目录号显示；再呼有线分机并接听验证。
  verification: |
    有显示话机显示 DECT 话机目录号；通话正常（p540 Tests）。
  conditions: 向导共 3 页（建话机 1-236 台/用户列表个性化/注册分配 IPUI）；也可走订阅户列表 2 步法（Add DECT/PWT set + GAP Reg，p489）。
  tags: [lab, dect, registration, ibs]

- id: c22
  title: IP-DECT xBS 部署（自动供应+注册+日志）
  type: lab
  source_pages: p541-548
  source_chapter: IP-DECT xBS — "Manage IP-DECT feature"
  source_quote: |
    "OMC/ Dect / DECT-PWT ARI-GAP / ARI … Enter the PARI number 110004360P0, replace 'P' with the number of your OXO" (p543)；
    "Don't forget to enable Auto Provision" (p544)
  steps: |
    1. LAN/IP：OMC/Hardware and Limits/LAN/IP Configuration——Boards 填系统 IP 192.168.1.246（实验口径）；Validate 后别忘 warm reset；DHCP tab 启用集成 DHCP 服务器、范围 192.168.1.10-39（实验口径）。虚拟课堂不可实操。
    2. PARI：OMC/Dect/DECT-PWT ARI-GAP/ARI——ARI 11 位八进制（每客户唯一，eBuy 获取，实验由讲师给）；填 110004360P0，P 换成自己 OXO 号（如 OXO1=11000436010，实验口径）；ARI 为 IBS 与 IP-DECT 共用。
    3. 接 PoE 交换机并核对 LED：红（网络初始化→取 IP→配置文件）→橙（软件下载→呼叫服务器链路→基站配置）→绿（1s 亮/1s 灭=就绪）。
    4. 核对列表：OMC/Subscribers-Basestations List 应自动出现 xBS（别忘了启用 Auto Provision）。
    5. 日志：OMC/Tools/Webdiag（installer/installer 密码）→ 选 Dect/xBS——识别每台 xBS 的 IP 地址。
    6. 话机注册：OMC/Subscribers/BaseStations List/Add → IBS-xBS sets → 输数量；点 GAP registration；话机侧 Auto install（出厂复位后）或 Menu\Install\Register\PIN 0000\跳过其它参数；IPUI 出现后点 Assign。
    7. 核对：注册成功后终端类型自动显示在订阅户列表。
  verification: |
    xBS 以绿 LED 就绪并入列表；话机注册后类型自动显示（p544/548）。
  conditions: 依赖 c02 的 IP 基线；复杂同步拓扑（多站/多集群）不在本实验（联系 TSS）。
  tags: [lab, ip-dect, xbs, provisioning]

- id: c23
  title: Webdiag 排障五连查（installer 会话）
  type: lab
  source_pages: p571-573
  source_chapter: Webdiag debug tool
  source_quote: |
    "OMC/Tools/Webdiag … Enter the login: installer … Example Alcatel1 in the classroom" (p572)；
    "Go to System\Dump System … Trace showing main information of the system" (p573)
  steps: |
    1. 开会话：OMC/Tools/Webdiag → login: installer + installer 密码（教室例 Alcatel1，实验口径）。
    2. 查机架板型：Start\System Start。
    3. 查软件版本：Information\General Information。
    4. 查 MAC 与序列号：Information\Cabinet Topology。
    5. 出系统摘要：System\Dump System（主信息 trace，可作报障附件）。
  verification: |
    五项信息全部取得（板型/版本/MAC+序列号/Dump 摘要），对应 p572-573 各节。
  conditions: 另有 operator 会话（MoH 上传/Hot Desking 监督/解锁账户）与 manufacturer 会话（技术支持专用，p560/570）。
  tags: [lab, webdiag, troubleshooting]

- id: c24
  title: Noteworthy 地址修改两例（自动重启与铃音节奏）
  type: lab
  source_pages: p579-581
  source_chapter: Noteworthy addresses modification
  source_quote: |
    "System Miscellaneous/ Memory Read/Write/ Debug Labels … fill out in the field Offset (HEX) the following value: '01 05 03 1E'" (p580)；
    "Do a warm reset and test … Warm reset: go to 'System miscellaneous/System Reset/ Warm reset & Immediately.'" (p581)
  steps: |
    1. 自动 warm reset：OMC → System Miscellaneous/Memory Read/Write/Debug Labels → 选 "Auto_Reset" → Details → Offset (HEX) 填 "01 05 03 1E"（01=启用、05=周五、03=3 时、1E=30 分）→ Modify → Write。
    2. 铃音节奏（内部 UA 呼叫响 2 秒静 1 秒）：OMC → System miscellaneous/Memory Read/write/Other labels——在 ringing timer 记下十六进制基址（例 "0242D978"，随软件版本变化！）；从 TC 附录 B 查内部 UA 铃偏移 9AH；科学计算器求和 9A+0242D978=0242DA12。
    3. 写入：System miscellaneous/Memory Read/write/Numeric Addresses——地址填 0242DA12、长度 14、Read；填新值（02 01 01 C8 00 64 00 00 00 00 00 00 00 00；C8=响 2 秒、64=静 1 秒）→ Modify → Write。
    4. 生效：System miscellaneous/System Reset/Warm reset & Immediately；测试内呼铃音。
  verification: |
    周五 3:30 自动 warm reset 触发（Auto_Reset 语义）；内呼铃声呈 2 秒响+1 秒静（p580/581 两例目标）。
  conditions: 铃音节奏周期必须 <4 秒；noteworthy 清单以 TC1398 为准；cold reset 后全部回默认。
  tags: [lab, noteworthy, memory]
```

## 任务覆盖自检（task ↔ id 映射）

| task_id | 覆盖 case 条目 |
|---|---|
| task-01 | c01 |
| task-02 | c02 |
| task-03 | c03 |
| task-04 | c04 |
| task-05 | c05 |
| task-06 | c06 |
| task-07 | c07 |
| task-08 | c08 |
| task-09 | c09（SIP 话机声明内嵌于 c09 步骤 1；概念部分在 principle/framework） |
| task-10 | —（维护操作散于 c03 步骤 11 抓包与 framework f06，无独立 How-To 章，原书即如此） |
| task-11 | c10 |
| task-12 | c11 |
| task-13 | c12 |
| task-14 | c13 |
| task-15 | c14 |
| task-16 | c15 |
| task-17 | —（原书为讲义+视频演示，无 How-To 步骤；framework f19 承载） |
| task-18 | —（原书为讲义三例，无 How-To；framework f20 承载） |
| task-19 | —（原书为讲义，无 How-To；principle p46 承载） |
| task-20 | —（原书为讲义，无 How-To；principle p25/p41-43 承载） |
| task-21 | —（原书为讲义流程，无实验；principle p38 承载） |
| task-22 | —（原书为讲义，无实验；framework f23 承载） |
| task-23 | —（原书为讲义，无实验；framework f24 承载） |
| task-24 | c16 |
| task-25 | c17 |
| task-26 | c18 |
| task-27 | c19 |
| task-28 | c20 |
| task-29 | c21、c22 |
| task-30 | c23、c24 |
| task-31 | —（原书为讲义三流程，无实验；framework f35 承载） |

自检结论：原书 24 个 How-To 章全部提取为 c01-c24；task-17/18/19/20/21/22/23/31 在原书中本就无 How-To（讲义/视频），已由 framework/principle 层覆盖，无遗漏。
