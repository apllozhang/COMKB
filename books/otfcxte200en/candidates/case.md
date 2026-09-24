# 案例/实验/操作序列候选 — OpenTouch Fax Center Starter (OTFCXTE200EN R9.2 Ed04)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、传真号）标注"实验口径"。
> 条目说明: 全书 8 个 How-To 实验章 → 8 条（Preparing the FAX server host / Installation / First Time Setup Wizard / Create Users & administrators / Clients installation / OXE SIP gateway configuration / SMTP integration / OTFC Backup & restore）。

```yaml
- id: c01
  title: 准备传真服务器宿主主机（IP 配置核验、Office 预初始化、关防火墙、装 IIS 角色）
  type: lab
  source_pages: p55-57
  source_chapter: Preparing the FAX server host — "Prepare the server which hosts the Fax software"
  source_quote: |
    "1.2. View the complete IP configuration • On your host: ipconfig /all Among the whole result,
    you should see information matching your lab server information." (p56)
    "1.6. Disable the local firewall: ... In the pop-up box, in the Domain Profile tab, change the
    Firewall state to Off. • Repeat this step for the Private Profile and Public Profile tabs." (p56)
    "Enable the Web Server (IIS) role. ... o Web Server ➤ Security ➤ Windows Authentication o Web
    Server ➤ Application Development ➤ ISAPI Extension o Web Server ➤ Application Development ➤
    ISAPI Filters o Management Tools ➤ IIS 6 Management Compatibility ➤ IIS 6 Metabase
    Compatibility" (p57)
  steps: |
    1. 打开命令提示符（Start ➤ 命令提示符）。
    2. 查看完整 IP 配置：执行 ipconfig /all，结果中应能看到与实验服务器信息匹配的条目（实验口径：fax.company.com / 192.168.1.60）。
    3. ping 主机名（例 fax.company.com），应 ping 通。
    4. nslookup 主机名（例 nslookup fax.company.com），应解析出完整地址。
    5. 为 Rasterizer 预初始化 Microsoft Office（已装 Office 时）：Start ➤ Excel 启动，确认无任何对话框弹出；对 PowerPoint 与 Word 重复此步（书中注：Office 应用已在培训前于服务账号上下文中启动过一次）。
    6. 关闭本地防火墙（实验口径，生产不适用）：Start ➤ Windows Firewall → Windows Firewall Properties → Domain Profile 页签把 Firewall state 设为 Off；对 Private Profile 与 Public Profile 页签重复；OK。
    7. 添加 Web Server 角色及其服务：Start ➤ Server Manager → Add roles and features → 向导多次 Next 至 Server Roles 页 → 启用 Web Server (IIS) 角色 → Next 至 Role Services 页 → 启用 4 个角色服务：Web Server ➤ Security ➤ Windows Authentication；Web Server ➤ Application Development ➤ ISAPI Extension；Web Server ➤ Application Development ➤ ISAPI Filters；Management Tools ➤ IIS 6 Management Compatibility ➤ IIS 6 Metabase Compatibility → Next → Install（安装需数分钟）。
  verification: |
    书中验收点：ping 与 nslookup 均成功且解析到完整地址（p56）；IIS 角色服务安装完成（p57 "The
    role services begin installing"）。Office 启动无弹窗（p56）。
  conditions: 实验服务器已按生态示例配好 DNS/域（实验口径）；关防火墙仅限实验环境。
  tags: [lab, prerequisites, iis, firewall, office]

- id: c02
  title: 安装 OTFC 服务器软件并禁用 Microsoft SMTP 服务
  type: lab
  source_pages: p58-65
  source_chapter: Installation — "Install Fax Center application on Windows server"
  source_quote: |
    "• From the root directory of the Fax distribution media, double-click Setup.exe ... • Select
    the XM FAX IP address: 192.168.1.60" (p59)
    "• Define the Fax hostname: Fax o Host Name of the gateway that will be used as interface
    between XM Fax and the telephone network • Select SIP protocol" (p61)
    "The password is temporary. You will have to change it at first login." (p62)
    "o Select all third-party software ... Third Party Software are software packages required by
    several components of Fax to function as designed" (p64)
    "Launch First Time Setup Wizard must be checked ... o Right- click on the Simple Mail
    Transport Protocol (SMTP) service and select Stop. o Set the SMTP service to Disable. o Start
    the XMSMTPGateway service. (By default the SMTP service is set to Automatic)." (p65)
  steps: |
    1. 从传真发行介质根目录双击 Setup.exe，按向导每次点 Next。
    2. 选安装语言（注意：该语言将决定新 Profile 的默认邮件通知 Profile 与基本 Profile 的封面语言）。
    3. 接受许可协议（必选）；选目标文件夹（传真文件安装路径）。
    4. 选 XM FAX IP 地址：192.168.1.60（实验口径）。
    5. 系统安装类型保持 "Create a new system"（首次安装）。
    6. 选择要安装的服务器组件（Custom Setup：Fax manager、Driver、SMTP gateway 等，按需勾选）。
    7. 定义传真主机名：Fax（即与电话网络接口的网关主机名）；协议选 SIP。
    8. 设置管理员账号：默认名 Administrator，密码设 123456（实验口径；临时密码，首登必须修改）。
    9. Ready to install 页点 Install。
    10. 第三方软件安装页：全选所有第三方软件（多个组件运行所必需）。
    11. 收尾页保持勾选 "Launch First Time Setup Wizard"，完成安装。
    12. 禁用 Microsoft SMTP 服务（须在装完服务器应用后做）：Start ➤ Settings ➤ Control Panel → Administrative Tools → Services → 右键 Simple Mail Transport Protocol (SMTP) 服务选 Stop → 启动类型设 Disable → 启动 XMSMTPGateway 服务（默认已是 Automatic）→ 关闭窗口。
  verification: |
    书中验收点：安装完成且 FTW 随装启动（p65 "Launch First Time Setup Wizard must be checked"）；
    XMSMTPGateway 服务已启动、Microsoft SMTP 已停用并禁用（p65 步骤 2）。
  conditions: c01 已完成（IIS 角色、防火墙、Office 就绪）；发行介质可用。
  tags: [lab, installation, setup-wizard, smtp-conflict, third-party]

- id: c03
  title: 执行 First Time Setup Wizard 搭最小可用系统
  type: lab
  source_pages: p66-70
  source_chapter: First Time Setup Wizard — "Perform the First Time Setup Wizard"
  source_quote: |
    "• Site creation: My Organisation" (p68)
    "• Users configuration o Select Internal Database" (p69)
    "• SMTP configuration: o Define the administrator's email address: baker@company.com o Enter
    the mail server FQDN: mail.company.com" (p69)
    "• First user creation o User's email address: baker@company.com o Temporary password: 123456
    • Click Proceed o The Configuration Status Window opens, and then closes automatically when
    the installation is done" (p70)
  steps: |
    1. 启动向导（c02 收尾勾选自启；或事后运行 [install_path]\Alcatel-Lucent Enterprise\FaxCenter\Bin\Util\FirstTimeSetup.exe）。
    2. 站点创建：站点名填 My Organisation（实验口径）。
    3. 用户配置：选 Internal Database（内部数据库；向导只呈现内部库与 AD 两种最常用选项）。
    4. SMTP 配置：管理员邮箱填 baker@company.com；邮件服务器 FQDN 填 mail.company.com（均为实验口径）。
    5. 首用户创建：用户邮箱 baker@company.com、临时密码 123456（实验口径；p50 讲义页首用户写 barkley@company.com，与实验页不一致，此处按实验页口径执行）。
    6. 点 Proceed：配置状态窗口打开，安装完成时自动关闭。
    7. 向导自动完成 12 项配置（建站点、QOS 0/0/240、XML Poll 文件夹、默认 Profile 去 SMTP 认证、CSID=站点名、建用户、Postmaster、站点/系统路由表、告警通知、Mail Relay、产出摘要存盘）。
  verification: |
    书中验收点：Configuration Status Window 自动打开并自动关闭即安装完成（p70）。后续 c04 用
    administrator/Alcatel1!@123 登录管理界面为系统级验证。
  conditions: c02 已完成；邮件服务器 mail.company.com 可达（实验口径）。
  tags: [lab, ftw, wizard, minimal-config, site]

- id: c04
  title: 创建用户与管理员（发现管理界面、建备份管理员、建两测试用户并互发传真）
  type: lab
  source_pages: p114-116
  source_chapter: Create Users & administrators — "Create some users and administrator accounts"
  source_quote: |
    "1 Discover admin MMC Snap-in • Start the OpenTouch Fax Center app • Logon using the
    Administrator name and password. Field Value / User Name Administrator / Password Change for
    Alcatel1!@123" (p115)
    "3 Create a system backup administrator • In a browser, navigate to http://fax/faxadmin •
    Under system Configurations ➤ Administrators select 'add' ... User Name backupadmin /
    Password Alcatel1!@123 • Press 'Create'" (p115)
    "4 Create users • Create 2 users ... Alexandra Allen allen@company.com Alcatel1!@123 31604 ;
    Brad Barkley barkley@company.com Alcatel1!@123 31600 • Logon into the Web Client
    (http://localhost/fax) o Compose and send faxes from a user to the other one o Check inbound,
    outbound & queue menus • From admin interface, monitor faxes exchange" (p116)
  steps: |
    1. 发现管理 MMC Snap-in：启动 OpenTouch Fax Center 应用，用 Administrator 登录；提示改密时改用 Alcatel1!@123（12 字符，实验口径）；展开各菜单节点熟悉界面，不做任何配置改动。
    2. 发现 Web 管理界面：浏览器打开 http://fax/faxadmin（实验口径主机名）。
    3. 建系统备份管理员：浏览器开 http://fax/faxadmin → System Configurations ➤ Administrators → add → 认证选传真服务器认证，填 User Name=backupadmin、Password=Alcatel1!@123（实验口径）→ Create → 打开 MMC 用新账号登录，按提示改密并记录新密码。
    4. 建 2 个用户（Web 管理界面，Sites ➤ Site ➤ Configuration ➤ Internal Users 路径下创建）：Alexandra Allen / allen@company.com / 密码 Alcatel1!@123 / 传真号 31604；Brad Barkley / barkley@company.com / 密码 Alcatel1!@123 / 传真号 31600（均为实验口径）。
    5. 行为测试：浏览器登录 Web Client（http://localhost/fax）→ 用一个用户 Compose 向另一个用户发传真 → 检查 inbound、outbound、queue 三个菜单。
    6. 管理员视角：从管理界面监控传真交换。
    7. （附）客户端安装说明（p115 注）：本实验把客户端装在传真服务器上，真实场景客户端装在用户工作站。
  verification: |
    书中验收点：两用户间传真互发成功；inbound/outbound/queue 菜单可见相应记录（p116）；管理界面
    可监控到传真交换（p116）。
  conditions: c03 已完成（站点与首用户就绪）；首登改密 Alcatel1!@123 为实验口径。
  tags: [lab, users, administrators, backup-admin, web-client, test]

- id: c05
  title: 安装并测试 Windows 客户端（SendFAX/Web Fax Composer/Print to Mail/Coversheet Editor）
  type: lab
  source_pages: p130-133
  source_chapter: Clients installation — "Install client applications"
  source_quote: |
    "• From the Client directory of the Fax distribution media, double-click Setup.exe Follow the
    Wizard instructions (each time click Next) • Choose the language" (p131)
    "• In the Custom Setup dialog, select all applications except the MMC Snap-in and Java API for
    the installation. o Remember: The MMC Snap-in is already installed when we installed the fax
    server. • In the Web Server dialog, enter the internal Host Name or URL of the web server/ o
    fax" (p132)
    "After completing the install, you may be asked to reboot the server. In this case, you can
    safely ignore the reboot request. You will not use the client applications on this server." (p132)
    "For each client, Test the different options: inbound, outbound, queue, delivery options…etc
    Use the user accounts created previously" (p133)
  steps: |
    1. 若 MMC Snap-in 开着，先关闭。
    2. 从发行介质 Client 目录双击 Setup.exe，按向导每次 Next，选安装语言。
    3. 按对话框推进，勾选要装的客户端。
    4. Custom Setup 对话框：选装除 MMC Snap-in 与 Java API 之外的全部应用（MMC Snap-in 随服务器已装）。
    5. Web Server 对话框：填 Web 服务器的内部主机名或 URL——fax（实验口径；可接受语法：fax、http://192.168.1.60 或 https://fax）。
    6. 按对话框完成安装。
    7. 若提示重启服务器可安全忽略（本实验客户端装在传真服务器上仅为教学，真实场景装在用户工作站）。
    8. 测试：用 c04 建的用户账号逐一测试 Web Client、SendFax、Web Fax Composer Printer、Print to mail、Coversheet editor 各客户端的 inbound/outbound/queue/投递选项等功能。
  verification: |
    书中验收点：每个客户端能完成 inbound、outbound、queue、delivery options 等操作（p133）；使用
    c04 建的 allen/barkley 账号登录验证。
  conditions: c04 已完成（用户账号可用）；实验口径服务器名 fax。
  tags: [lab, clients, sendfax, web-fax-composer, print-to-mail]

- id: c06
  title: OXE 侧 SIP 网关配置（MGR 七步：中继组→网关→代理→信任 IP→外部网关→路由表→前缀计划）
  type: lab
  source_pages: p151-155
  source_chapter: OXE SIP gateway configuration — "Manage the SIP gateway on OXE side"
  source_quote: |
    "Configure a SIP gateway on OXE side to connect to the Fax server. Use MGR or Omnivista 8770
    to manage. mtcl is the default login & password ... login: mtcl Password: mtcl … (101)csa> mgr" (p152)
    "• Select mgr / Trunk groups/ Create" (p152)
    "• Select mgr / SIP / SIP gateway ... • Select mgr / SIP / Proxy ... • Select mgr / SIP /
    Trusted IP addresses/ Create ... • Select mgr / SIP / SIP Ext gateway/ Create" (p153-154)
    "• Select mgr / Translator / Network Routing Table/ 5 ... • OXE users directory numbers #31600
    to 31699 • Select mgr / Translator / Prefix plan/ Create" (p155)
  steps: |
    1. 用终端窗口登录 OXE 呼叫服务器：login mtcl / 密码 mtcl（默认账号密码，实验/出厂口径），进入 csa 后执行 mgr。
    2. 建 SIP 中继组：mgr / Trunk groups / Create。
    3. 配置 SIP 网关：mgr / SIP / SIP gateway（传真服务器对接参数，详见书内截图与 TC3048）。
    4. 配置 SIP Proxy：mgr / SIP / Proxy。
    5. 配置信任 IP 地址：mgr / SIP / Trusted IP addresses / Create（把传真服务器地址列入信任）。
    6. 配置 SIP 外部网关：mgr / SIP / SIP Ext gateway / Create。
    7. 配置路由表：mgr / Translator / Network Routing Table / 5。
    8. 配置路由号码（前缀计划）：把 OXE 用户目录号 #31600-31699（实验口径号段）经 mgr / Translator / Prefix plan / Create 指向传真网关。
  verification: |
    书中未设独立验收小节；本书口径为配置完成后与 OTFC 侧 SIP 声明（f23）配合验证话路；排障用
    p148-150 抓包三法（CHtrace/motortrace/tcpdump→Wireshark）。参数细节参照 TC3048（p141、p147）。
  conditions: 需要 OXE 的 mtcl/mgr 访问权限；OTFC 侧 SIP 已配置（本地 UDP 5360）；细节参数以
    TC3048 为准，书中为菜单序列骨架。
  tags: [lab, oxe, sip-gateway, mgr, trunk-group, routing]

- id: c07
  title: SMTP 集成（Exchange 建 'FAX' 地址空间 Send Connector 并核验）
  type: lab
  source_pages: p172-175
  source_chapter: SMTP integration — "Login to administration interface and use it"
  source_quote: |
    "1.1. Open the Exchange management shell • From the command prompt, enter o New-SendConnector
    -Name OTFC -AddressSpace \"fax:*;1\" –SmartHosts \"fax.company.com\" -DNSRoutingEnabled $false
    –SourceTransportServers \"eco.company.com\"" (p173)
    "Field Value / SendConnector name OTFC / Fax server fax.company.com / Source transport server
    eco.company.com (AD, mail, DNS…)" (p173)
    "1.2. In Exchange Admin center • Check the configuration: ... The connector is created" (p173)
    "• Edit the connector to check settings" (p174)
  steps: |
    1. 打开 Exchange Management Shell。
    2. 执行建连接器命令（实验口径参数）：New-SendConnector -Name OTFC -AddressSpace "fax:*;1" –SmartHosts "fax.company.com" -DNSRoutingEnabled $false –SourceTransportServers "eco.company.com"
       ——SendConnector 名称=OTFC；传真服务器=fax.company.com；源传输服务器=eco.company.com（兼 AD、邮件、DNS 的实验服务器）。
    3. 查看命令回显结果确认创建成功。
    4. 在 Exchange Admin center 核验：Mail flow → Send Connectors 页签应出现新连接器（"The connector is created"）。
    5. 双击连接器编辑属性，逐项核对设置（AddressSpace fax:*;1、SmartHosts 指向传真服务器 SMTP 网关、DNSRoutingEnabled=$false、源传输服务器）。
    6. （配套原理）若 Exchange 收件安全过高拦截 OTFC 通知邮件，到 Hub Transport 节点的 Receive Connector 属性调整安全参数（p170）。
  verification: |
    书中验收点：Exchange Admin center 的 Mail flow → Send Connectors 列表出现 OTFC 连接器
    （p173 "The connector is created"）；编辑界面参数与命令一致（p174）。
  conditions: 需要 Exchange 管理权限；SMTP connector 为许可特性（p158）；实验参数
    fax.company.com/eco.company.com。
  tags: [lab, exchange, send-connector, smtp, fax-address-space]

- id: c08
  title: OTFC 备份与恢复（停服冷备、拷三文件夹+MySQL+注册表键、回灌恢复）
  type: lab
  source_pages: p230-232
  source_chapter: OTFC Backup & restore — "Backup & restore the OTFC database"
  source_quote: |
    "1.1. Stop all fax server services ... go to: C:\Program Files\ Alcatel-Lucent
    Enterprise\FaxCenter\Bin\Util and run xmsc -oa ; 1.2. Stop the mysql5 service ; 1.3. Make
    copies of the following folders Folders path: C:\Program Files\ Alcatel-Lucent
    Enterprise\FaxCenter\ ­ the Data folder ­ the Bin folder ­ the Config folder ; 1.4. Make a
    copy of the MySQL database C:\Program Files\MySQL\MySQL Server 8.0 \Data ; 1.5. Start regedit
    Export the HKEY_LOCAL_MACHINE\SOFTWARE\Interstar Technologies key from Regedit to a .reg file." (p231)
    "2.5. Start regedit If necessary, import the HKEY_LOCAL_MACHINE\SOFTWARE\Interstar Technologies
    key from the .reg file to Regedit. ... xmsc -aa ; 2.7. Start mysql5 service" (p232)
  steps: |
    备份（Backing up data）：
    1. 经管理界面 System Monitor ➤ Services Status 确认所有组件 Active。
    2. 停全部传真服务：命令行进 C:\Program Files\Alcatel-Lucent Enterprise\FaxCenter\Bin\Util，执行 xmsc -oa。
    3. 停 mysql5 服务。
    4. 拷贝三文件夹（C:\Program Files\Alcatel-Lucent Enterprise\FaxCenter\ 下）：Data、Bin、Config。
    5. 拷贝 MySQL 数据库目录：C:\Program Files\MySQL\MySQL Server 8.0\Data（实验口径路径）。
    6. 启动 regedit，导出 HKEY_LOCAL_MACHINE\SOFTWARE\Interstar Technologies 键为 .reg 文件。
    7. 备份完成后重启全部传真服务与 MySQL：xmsc -aa。
    恢复（Restore data）：
    1. 经管理界面确认所有组件 Active 后停全部传真服务（xmsc -oa）。
    2. 停 mysql5 服务。
    3. 回灌 Data、Bin、Config 三文件夹到原路径。
    4. 回灌 MySQL 数据库目录。
    5. 启动 regedit，按需从 .reg 文件导入 Interstar Technologies 键。
    6. 重启全部传真服务或重启服务器：xmsc -aa。
    7. 启动 mysql5 服务。
  verification: |
    书中验收点：恢复完成后全部传真服务与 mysql5 处于运行状态（xmsc -aa、Start mysql5 service，
    p232）；配合管理界面 System Monitor ➤ Services Status 全组件 Active（p231/232 开头步骤）。
  conditions: 恢复环境须与备份时相似（版本等同、拓扑一致、同路径）；备份停服不可 kill、恢复可
    kill（p216/p220）；实验口径含 mysql5 服务名与 MySQL Server 8.0 路径。
  tags: [lab, backup, restore, xmsc, mysql, registry]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-24）的案例类覆盖率

| task | 任务 | 案例类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 评估方案能力 | — | — | 无 How-To，属讲义/数值类 |
| task-02 | 规划部署架构 | — | — | 无 How-To，属讲义/图示类（framework f08-f10） |
| task-03 | 准备传真服务器宿主 | 有 | c01 | How-To 实验 1 |
| task-04 | 安装 OTFC 软件 | 有 | c02 | How-To 实验 2 |
| task-05 | 跑 First Time Setup Wizard | 有 | c03 | How-To 实验 3 |
| task-06 | 处理许可 | — | — | 书内仅两页讲义（p52-53），无实验 |
| task-07 | 创建与管理用户 | 有 | c04（步骤 4） | 建两用户在实验 4 内 |
| task-08 | 创建 System/Site 管理员 | 有 | c04（步骤 1-3） | MMC/Web 发现 + 备份管理员在实验 4 内（Site 管理员建法在讲义 p111，无实验） |
| task-09 | 安装并测试客户端 | 有 | c05 | How-To 实验 5 |
| task-10 | 定制封页 | — | — | 讲义五步（p93-96，framework f18），无独立 How-To 章 |
| task-11 | 设计 Profile | — | — | 讲义（p117-129，framework f21），无 How-To |
| task-12 | 管理电话簿 | — | — | 讲义（p134-139），无 How-To |
| task-13 | 配置 OTFC 侧 SIP 与 OXE 声明 | 部分 | — | 书内无独立 How-To 章（p142-146 为讲义+路径），OXE 侧实验见 c06 |
| task-14 | 配置 OXE 侧 SIP 网关 | 有 | c06 | How-To 实验 6 |
| task-15 | OXE 侧抓包 | 部分 | c06（verification 引用） | p148-150 为讲义命令页，无实验小节；已并入 c06 验收口径 |
| task-16 | 集成邮件系统 | 有 | c07 | How-To 实验 7 |
| task-17 | 认知与运维服务架构 | — | — | 讲义（p176-191），命令口径在 principle p34 |
| task-18 | 高级目录与路由 | — | — | 讲义（p192-211），无 How-To |
| task-19 | 配置传真计费 | — | — | 讲义两页（p212-213） |
| task-20 | 备份与恢复系统 | 有 | c08 | How-To 实验 8 |
| task-21 | 升级系统 | — | — | 讲义（p221-222），无 How-To |
| task-22 | 配置传真删除策略 | — | — | 讲义（p223-224） |
| task-23 | 报表与监控 | — | — | 讲义（p225-229） |
| task-24 | 按日志定位故障 | — | — | 讲义（p208），判据在 principle p41 |

**覆盖结论**：全书 8 个 How-To 实验章已 1:1 全部提取（c01-c08），对应 task-03/04/05/07/08/09/14/16/20 共 9 项任务的操作主体；其余 task 为讲义型内容（无实验章），分别由 framework/principle/counter-example 文件承接，无遗漏。
