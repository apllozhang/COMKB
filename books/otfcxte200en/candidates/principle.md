# 原则/清单/规则/公式/数值口径候选 — OpenTouch Fax Center Starter (OTFCXTE200EN R9.2 Ed04)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号、号码）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: 容量与传输口径：单专用服务器上限 15000 用户/30 端口；T.38 最高 14.4kbps、G.711 最高 33.8kbps
  type: metric
  source_pages: p7
  source_chapter: What Is OTFC?（传真传输协议页）
  source_quote: |
    "Dedicated server • Up to 15000 users • 30 ports ; Fully software-based • Fax over IP •
    SIP/TCP and SIP/TLS • T38 / SIP connection to OmniPCX Enterprise ; Fax transmission
    protocol: • T.38 • Group 3 fax • speed of up to 14.4kbps • G.711 • Speed of up to 33.8kbps" (p7)
  summary: |
    四组口径：①单专用服务器（物理或虚机）上限 15000 用户、30 端口；②全软件实现（Fax over IP），
    支持 SIP/TCP 与 SIP/TLS，经 T.38/SIP 连 OXE；③传输协议两种——T.38（含 Group 3 传真）最高
    14.4kbps，G.711 语音通道透传最高 33.8kbps。售前选型与容量边界按此对答。
  conditions: 30 ports 的"端口"指传真通道资源；明细以 Features List 为准
  tags: [metric, capacity, protocol, t38, g711]

- id: p02
  title: 文件格式支持 45 种（清单外置 Feature List）
  type: metric
  source_pages: p18, p163
  source_chapter: Fax File Types / Sending & Receiving Faxes from an e-mail client
  source_quote: |
    "For a complete list of the currently supported 45 file formats refer to the Feature List" (p18)
    "For a complete list of the currently supported 45 file formats refer to the Feature List" (p163)
  summary: |
    支持的文件格式总数为 45 种，全书两处一致；完整清单外置 Feature List。Rasterizer 可转换
    doc/pdf/txt/xls/png/bmp/gif/jpeg/htm 等（p182 列举），转换结果是传真 TIFF。
  conditions: 数量会随版本变化，书内两页均强调查 Feature List
  tags: [metric, rasterizer, formats]

- id: p03
  title: 入局路由方法四种：DNIS、CSID、ANI、DTMF
  type: metric
  source_pages: p9
  source_chapter: Receive Faxes From
  source_quote: |
    "Inbound routing methods •DNIS, CSID, ANI, DTMF" (p9)
  summary: |
    来传真路由依据四种：被叫号码（DNIS）、主叫传真机标识（CSID）、主叫号码（ANI）、双音多频
    补拨（DTMF）。书中未展开四个缩写的全称，此处括注为通用电信含义（推断），使用时以电信常识与
    产品文档核对。配合 p19 路由图：OXE 把来话转传真服务器，内部路由表按被叫号码/主叫传真机标识
    匹配，再按通知规则投递。
  conditions: 缩写全称为通用含义（推断），原书未给
  tags: [metric, routing, inbound]

- id: p04
  title: 队列与历史状态口径：外发队列六状态、外发历史两态、入呼历史两态
  type: metric
  source_pages: p25
  source_chapter: Queue and History
  source_quote: |
    "Outgoing Queue •Statuses: Preprocessing (converting documents and rendering coversheet),
    Delayed, Ready to Send, Sending, Waiting, Sent. •Faxes can be viewed (images and details) and
    cancelled. Outbound History •Statuses: Sent or Failed (cancelled, failed to reach destination,
    etc)... Inbound History •Statuses: Received or Failed to receive (not all pages were
    transmitted)." (p25)
  summary: |
    三视图状态逐格转写：外发队列六状态（Preprocessing=转换文档并渲染封面、Delayed、Ready to
    Send、Sending、Waiting、Sent），可查看可取消；外发历史两态（Sent/Failed，失败含取消与未达
    目的地等），可重提交；入呼历史两态（Received/Failed to receive，失败=页数不全），可重路由、
    转发。用户只见自己的传真，管理员见全部。
  conditions: 排障按状态对号
  tags: [metric, queue, status]

- id: p05
  title: 服务器与虚拟化支持矩阵（OS 2022/2019/2016 含 IIS 10.0；ESXi 6.5-8.0；Hyper-V 三版；TS/Citrix）
  type: metric
  source_pages: p39
  source_chapter: OTFC server
  source_quote: |
    "OTFC operating system •Microsoft Windows 64bits Servers 2022 / 2019/ 2016 (including IIS
    10.0) ; Virtualization •Hyper-V •Windows Server 2016 / Hyper-V Server 2016 •Windows Server
    2019 / Hyper-V Server 2019 •Windows Server 2022 / Hyper-V Server 2022 •VMware ESXi •From 6.5
    to 8.0 •vSphere •V-Motion •High availability •Terminal server •2019 •2022 •Citrix" (p39)
  summary: |
    逐格转写：服务器 OS 为 64 位 Windows Server 2022/2019/2016（含 IIS 10.0）；虚拟化两条线——
    Hyper-V（Windows Server 2016/2019/2022 或对应 Hyper-V Server 版本）、VMware ESXi 6.5 至 8.0
    （配套 vSphere、v-Motion、高可用特性）；终端服务器 2019/2022；Citrix。全部以 Features List
    为准。
  conditions: 版本清单随版本迭代，实施前查最新
  tags: [metric, requirements, os, virtualization]

- id: p06
  title: 邮件服务器与 Office 矩阵：Exchange 2019/2016/2013、O365、SMTP 兼容；Rasterizer 需 Office 2021/2019/2016
  type: metric
  source_pages: p40
  source_chapter: Supported software
  source_quote: |
    "Supported mail servers • Microsoft Exchange 2019 / 2016 / 2013 • Microsoft Office 365 &
    Exchange online • SMTP-compliant mail servers. For Rasterizer module • Microsoft Office
    2021/ 2019 / 2016 (64-bit and 32-bit)" (p40)
  summary: |
    邮件服务器三档：Exchange 2019/2016/2013、O365 与 Exchange online、任意 SMTP 兼容邮件服务器；
    Rasterizer 模块要求传真服务器本机装 Microsoft Office 2021/2019/2016（64 位与 32 位均可）。
  conditions: 以 Features List 为准
  tags: [metric, requirements, mail, office]

- id: p07
  title: 客户端矩阵：工作站 Win11/10、终端服务 TS 2022/2019、Outlook "2022"/2019/2016（原文如此）
  type: metric
  source_pages: p41
  source_chapter: Client Requirements
  source_quote: |
    "Operating System • For Workstations: • Windows 11 • Windows 10 • For Terminal Services: •
    Windows Terminal Server 2022 / 2019 ; Supported Mail Clients • Microsoft Outlook 2022 / 2019 /
    2016 (64-bit and 32-bit) ; Supported Web Browsers • Refer to feature list" (p41)
  summary: |
    客户端三档：工作站 Windows 11/10；终端服务 Windows Terminal Server 2022/2019；邮件客户端
    Outlook 2022/2019/2016（64/32 位）——注意 Outlook 并无 2022 版本，原文如此，疑为原书笔误
    （忠实转写并以 Features List 核实）。浏览器支持整表外置 Feature List。
  conditions: "Outlook 2022"为原文笔误标注
  tags: [metric, requirements, clients, typo]

- id: p08
  title: 实验口径：生态示例全套参数（IP/主机名/账号/传真号）
  type: metric
  source_pages: p45, p49-50, p70
  source_chapter: Ecosystem example / Installation / First Time Setup Wizard
  source_quote: |
    "fax.company.com 192.168.1.60 ; mail.company.com 192.168.1.100 ; Active directory & DNS
    eco.company.com 192.168.1.100 ; oxe.company.com 192.168.1.3 ... Fax administrator
    baker@company.com Login: administrator Password: Alcatel1!@123" (p45)
    "Define OTFC IP address: 192.168.1.60 ... Username: administrator • Password: 123456 • To
    change at the first login: Alcatel1!@123 ... Fax hostname: fax" (p49)
    "Site Name definition • Name: My Organization ... Administrator's email: baker@company.com •
    Mail server: mail.company.com ... Username: barkley@company.com • Password: 123456" (p50)
    "User's email address: baker@company.com • Temporary password: 123456" (p70)
  summary: |
    实验口径全表（非生产值）：传真服务器 fax.company.com=192.168.1.60；邮件服务器
    mail.company.com=192.168.1.100；AD+DNS eco.company.com=192.168.1.100；OXE
    oxe.company.com=192.168.1.3；OTFC 安装 IP 填 192.168.1.60；传真网关主机名 fax；系统管理员
    administrator（临时密码 123456，首登改 Alcatel1!@123，12 字符）；站点名 My Organization；
    管理员邮箱 baker@company.com；首用户——p50 讲义页为 barkley@company.com、p70 实验页为
    baker@company.com（两页不一致，实验口径记录）；测试用户 allen@company.com=传真号 31604、
    barkley@company.com=31600。
  conditions: 实验口径；生产按客户 DNS/AD 规划整体替换
  tags: [metric, lab, ecosystem, passwords]

- id: p09
  title: IIS 角色服务清单四项（Windows Authentication、ISAPI Filters、ISAPI Extensions、IIS 6 Metabase Compatibility）
  type: checklist
  source_pages: p48, p57
  source_chapter: Preparing the server / Preparing the FAX server host (How-To)
  source_quote: |
    "Web Server (IIS) role with role services: Windows Authentication; ISAPI Filters; ISAPI
    Extensions; IIS Metabase Compatibility" (p48)
    "o Web Server ➤ Security ➤ Windows Authentication ; o Web Server ➤ Application Development ➤
    ISAPI Extension ; o Web Server ➤ Application Development ➤ ISAPI Filters ; o Management Tools
    ➤ IIS 6 Management Compatibility ➤ IIS 6 Metabase Compatibility" (p57)
  summary: |
    IIS 角色下必须启用的 4 个角色服务：Windows Authentication（安全节点）、ISAPI Extension 与
    ISAPI Filters（应用开发节点）、IIS 6 Metabase Compatibility（管理工具→IIS 6 管理兼容性节点）。
    How-To 路径：Start ➤ Server Manager → Add roles and features → Server Roles 启用 Web Server
    (IIS) → Role Services 页签逐项勾选 → Install。
  conditions: 4 项缺一会影响管理界面/网关组件
  tags: [checklist, iis, prerequisites]

- id: p10
  title: 服务账号权限清单六项（域服务账号/LDAP 查询/文件夹读写/打印权限/本地管理员/密码永不过期）
  type: checklist
  source_pages: p48
  source_chapter: Preparing the server
  source_quote: |
    "Create a service account • Domain permissions to act as a service account • Domain user
    access with permissions to query LDAP • Read/write access to any network folders used as fax
    destinations • Print permissions on any network printers used as fax destinations • Be a
    Local Administrator on the fax server • Have a password that does not expire" (p48)
  summary: |
    服务账号六项权限：①域内可充当服务账号；②有查询 LDAP 的域用户权限；③对用作传真目的地的
    网络文件夹有读写权；④对用作传真目的地的网络打印机有打印权限；⑤是传真服务器的本地管理员；
    ⑥密码永不过期。缺任一项都会在后续传真投递/目录查询时踩坑。
  conditions: 依赖客户 AD 规划
  tags: [checklist, service-account, prerequisites]

- id: p11
  title: DNS 正反解与连通性检查口径（FQDN 正解到 IP、IP 反解回 FQDN、ping/nslookup 应成功）
  type: rule
  source_pages: p47, p56
  source_chapter: Preparing the server / Preparing the FAX server host (How-To)
  source_quote: |
    "Server is in the same domain as users • Server FQDN resolves to the server IP address in DNS
    • Reverse lookup of the server IP address in DNS returns the server FQDN • Server can reach
    and is reachable by external components" (p47)
    "1.2. View the complete IP configuration • On your host: ipconfig /all ... 1.3. Perform a
    ping • On your host name: (e.g. fax.company.com); The ping should succeed 1.4. Perform a
    nslookup ... This should also succeed and resolve to your full address" (p56)
  summary: |
    服务器网络就绪判据：与用户同域；FQDN 正向解析到服务器 IP；IP 反向解析返回 FQDN；与外部组件
    双向可达。How-To 验证三连：ipconfig /all 核对；ping 主机名（例 fax.company.com）应通；
    nslookup 主机名应解析出完整地址。任一不成立先修 DNS 再装 OTFC。
  conditions: 依赖客户 DNS；实验域 company.com
  tags: [rule, dns, prerequisites]

- id: p12
  title: 安装语言副作用规则：决定默认邮件通知 Profile 与基本 Profile 封面语言
  type: rule
  source_pages: p59, p63
  source_chapter: Installation (How-To)
  source_quote: |
    "The installation language will define the default Mail Notification Profile used with new
    profiles and new Mail Notification Destinations. It will also define the cover sheet language
    used in the basic Profile." (p59, p63 两页同文)
  summary: |
    规则：Setup 向导里选的安装语言有两项持久副作用——①新建 Profile 与新邮件通知目的地使用的
    默认邮件通知 Profile；②基本（Basic）Profile 使用的封面语言。装反了语言后续要手工改默认
    Profile，选语言时按客户语言环境定。
  conditions: 首装一次性决策
  tags: [rule, installation, language]

- id: p13
  title: 默认（评估）许可边界：每组件 1 实例、共 2 通道、10 站点不限时、100 用户、每页水印
  type: metric
  source_pages: p52-53
  source_chapter: Licensing / Import licenses
  source_quote: |
    "Default License • When installing OpenTouch Fax Center for the first time on a server, a
    default license is automatically • Installed for evaluation purposes, that: • Enables one
    instance of each component • Enables a total of two channels (FoIP and fax boards) in
    evaluation mode • Enables up to 10 sites with no time limit • Allows for 100 users • Applies
    a watermark on every fax page" (p52)
    "To purchase and receive a license, you will need to provide your OpenTouch Fax Center
    reseller with your server physical (MAC) address. ... Import license file manually only" (p52-53)
  summary: |
    出厂自动安装的评估许可五条边界：每组件启用 1 个实例；FoIP 与传真板卡合计 2 通道；最多 10 个
    站点且不限时；100 用户；每页传真打水印。正式许可两级控制（组件上限 users/sites/gateways/
    channels + 特性开关）；采购时向经销商提供服务器物理（MAC）地址；许可文件只能手工导入。
  conditions: 水印与 2 通道直接影响验收，交付前换正式许可
  tags: [metric, licensing]

- id: p14
  title: 管理与客户端访问 URL 口径（/faxadmin、/fax、localhost/fax、fax 或 https://fax）
  type: metric
  source_pages: p74, p76, p80, p85, p115-116
  source_chapter: Administration / Web administration page / Web Client / Windows Clients / Create Users (How-To)
  source_quote: |
    "http://<ServerName_or_IP>/faxadmin or https://<ServerName>/faxadmin" (p74)
    "http://<ServerName_or_IP>/fax or https://<ServerName>/fax. User authentication is required" (p80)
    "Acceptable syntax: fax or http://192.168.1.60, or https://fax" (p85)
    "In a browser, navigate to http://fax/faxadmin ... Logon into the Web Client
    (http://localhost/fax)" (p115-116)
  summary: |
    访问口径：Web 管理页 http(s)://<服务器名或IP>/faxadmin（实验主机名 fax 时即 http://fax/faxadmin）；
    Web Client http(s)://<服务器名或IP>/fax（实验中 http://localhost/fax）；SendFAX 等客户端的
    服务器语法接受主机名 fax、http://192.168.1.60（实验口径 IP）或 https://fax。
  conditions: 服务器名/IP/端口为实验口径
  tags: [metric, url, menu-path, lab]

- id: p15
  title: 密码口径：临时密码首登必改；实验密码 Alcatel1!@123（12 字符）贯穿全书
  type: rule
  source_pages: p49, p62, p70, p77, p115
  source_chapter: Installation / First Time Setup Wizard / Create Users & administrators (How-To)
  source_quote: |
    "Administrator account • Username: administrator • Password: 123456 • To change at the first
    login: Alcatel1!@123" (p49)
    "The password is temporary. You will have to change it at first login." (p62)
    "Note: You will be prompted to change the Administrator's password. Use 'Alcatel1!@123' —
    12 characters" (p115)
    "Field Value / User Name backupadmin / Password Alcatel1!@123" (p115)
  summary: |
    密码生命周期规则：安装时设的密码（如 123456）都是临时的，首登强制修改；系统管理员与首用户
    均如此。实验口径新密码统一 Alcatel1!@123（正好 12 字符，也是密码长度示例）；备份管理员
    backupadmin 同密码。生产环境必须全部替换且不得沿用教材值。
  conditions: Alcatel1!@123/123456/mtcl 均为实验或出厂默认口径
  tags: [rule, security, lab, passwords]

- id: p16
  title: FTW 十二项动作与 QOS 0/0/240、CSID=站点名等固定口径
  type: checklist
  source_pages: p67
  source_chapter: First Time Setup Wizard
  source_quote: |
    "Creates a Site • Sets the Site QOS to 0/0/240 • Sets the XML Poll folder to the Site Name •
    Removes SMTP Messages Require Authentication from default profile • Sets the CSID of the
    default profile to the Site name • Creates the User and sets its Password • Sets the Site
    SMTP Postmaster to the Administrator's SMTP address • Sets the Site Routing Table to route to
    the User • Sets the System Routing Table to route to the Site, with CSID set to Site Name •
    Sets the Alert Notification to go to the Administrator's SMTP address through the specified
    Mail Relay Server • Sets the SMTP Gateway (if installed) Mail Relay Server • Produces a
    summary and instructions on how to use the system. This summary is also automatically saved
    to a file." (p67)
  summary: |
    FTW 十二项动作逐条转写：①建 Site；②Site QOS 设 0/0/240；③XML Poll 文件夹=站点名；④从默认
    Profile 移除"SMTP 消息要求认证"；⑤默认 Profile 的 CSID=站点名；⑥建用户并设密码；⑦Site SMTP
    Postmaster=管理员 SMTP 地址；⑧Site 路由表→该用户；⑨System 路由表→该 Site（CSID=站点名）；
    ⑩告警通知经指定 Mail Relay 发管理员 SMTP；⑪设 SMTP 网关的 Mail Relay Server；⑫产出使用摘要
    并自动存盘。理解这 12 项即理解"最小可用系统"由哪些配置构成（手工配置时逐项对照）。
  conditions: QOS 0/0/240 为向导固定值；摘要文件位置书中未给
  tags: [checklist, ftw, qos, csid]

- id: p17
  title: FTW 事后运行路径：FirstTimeSetup.exe 固定路径
  type: metric
  source_pages: p67
  source_chapter: First Time Setup Wizard
  source_quote: |
    "If you do not choose to use the Wizard, all these configurations can be managed from the Fax
    Administration interface. However, the Administrator has the option to run this application at
    a later time from the Fax directory by executing the following file:
    [install_path]\Alcatel-Lucent Enterprise\FaxCenter\Bin\Util\FirstTimeSetup.exe" (p67)
  summary: |
    跳过向导或需重跑时，执行文件固定路径：
    [install_path]\Alcatel-Lucent Enterprise\FaxCenter\Bin\Util\FirstTimeSetup.exe；
    也可以完全经传真管理界面手工完成同样配置。
  conditions: [install_path] 为实际安装目录占位
  tags: [metric, ftw, path]

- id: p18
  title: Web Client 浏览器与无障碍合规口径（任意浏览器、HTTP/HTTPS、508 条款与 e-inclusion）
  type: metric
  source_pages: p79
  source_chapter: Web Client
  source_quote: |
    "Available from any web browser, for instance •Firefox •Safari •Chrome •… •Compliant with
    section 508 of the US Rehabilitation Act & European e-inclusion •HTTP/HTTPS support" (p79)
  summary: |
    Web Client 可用任意浏览器（书中举例 Firefox/Safari/Chrome），支持 HTTP/HTTPS 两种访问，符合
    美国康复法案 508 条款与欧洲 e-inclusion 无障碍要求（政府采购/合规场景可用作投标口径）。
    浏览器支持明细以 Feature List 为准。
  conditions: 举例非穷举
  tags: [metric, web-client, compliance]

- id: p19
  title: 客户端部署口径：静默安装 + GPO 批量；精简包在 ClientRedistribution；认证两式
  type: rule
  source_pages: p83-84
  source_chapter: Windows Clients
  source_quote: |
    "Silent installation & Installation by Massive Deployment through Group Policy are available.
    User authentication •Windows account in the domain •Internal OTFC user account" (p83)
    "A reduced client applications set including only independent applications usable by most of
    the users (no administration tools) is available through the installation files located in the
    ClientRedistribution folder" (p84)
  summary: |
    三条部署规则：①Windows 客户端支持静默安装与组策略（GPO）大规模部署——企业批量装机走这两条；
    ②面向最终用户的精简客户端集（只含独立应用、不含管理工具）在发行介质 ClientRedistribution
    文件夹；③客户端用户认证两式——域 Windows 账号或 OTFC 内部账号。
  conditions: 精简包不含管理工具
  tags: [rule, clients, gpo, silent-install]

- id: p20
  title: 时区影响三处：封页、传真报头、邮件通知时间戳（可在用户/Profile 级管理）
  type: rule
  source_pages: p102
  source_chapter: Create a user（Internal users）
  source_quote: |
    "Time zone info added in the fax header • Time zone could be managed in user profile • Time
    zone affects time stamps on cover sheets, headers and email notifications" (p102)
  summary: |
    用户时区写入传真报头，并影响三处时间戳：封页、报头、邮件通知。时区可在用户 Profile 级管理——
    跨时区组织的用户要按所在地设置，否则通知时间对不上。
  conditions: 建户时设置
  tags: [rule, users, timezone]

- id: p21
  title: CSV 导入/导出仅限 Webadmin 界面；导入需选 Profile
  type: rule
  source_pages: p104-105
  source_chapter: Import users .CSV / Export users
  source_quote: |
    "Users can be imported by the Webadmin interface only • .csv file format • Click on 'Import
    users' ... 3 Profile to apply" (p104)
    "The list of users could be exported by the Webadmin interface only • As .csv file • Click on
    'export users'" (p105)
  summary: |
    规则：用户 CSV 批量导入与用户清单导出都只能在 Webadmin 界面完成（MMC 不提供）；导入流程要
    选择套用的 Profile（第 3 步）。批量开号场景：先导出样表/既有清单→改→再导入。
  conditions: .csv 格式；MMC 无此功能
  tags: [rule, users, csv, menu-path]

- id: p22
  title: 管理员与用户认证方式口径（SMTP 地址、Windows 认证 SSO/SAML；内部服务器/AD/SAML 三基）
  type: checklist
  source_pages: p77, p110
  source_chapter: Authentication / Create new SYSTEM administrator
  source_quote: |
    "Authentication by: •SMTP Address •Windows authentication SSO and SAML" (p77)
    "Authentication based on internal server, AD and SAML" (p110)
  summary: |
    两处认证口径合并：管理员登录认证可用 SMTP 地址或 Windows 认证（SSO 与 SAML，p77）；建 System
    管理员时认证基础为内部服务器、AD、SAML 三种（p110）。客户有 SSO/SAML 基础设施时优先对接。
  conditions: SAML 配置细节书中未展开
  tags: [checklist, authentication, sso, saml]

- id: p23
  title: Mail Notification Profile 口径：每语言一份、经 Profile 关联、Exchange 场景勾"Exchange integration"+Text 正文
  type: rule
  source_pages: p124-127
  source_chapter: User Profiles – Mail Notification profiles
  source_quote: |
    "Mail Notification Profiles are sets of general and event specific notification options, that
    can be associated with user profiles and mail destinations. ... Mail Notification Profile is
    created for each of the user languages available in OTFC. Sites ➤ Site ➤ Configuration ➤ Mail
    Notification Profiles ➤ Properties ➤ Notification Options" (p124)
    "'Exchange integration' has to be checked with 'Message body format: Text'. Format used for
    email notification, not for web access!" (p126)
    "A mail notification profile must be associated to a user thanks to the user Profile" (p127)
  summary: |
    四条口径：①邮件通知 Profile 是"通用+按事件"的通知选项集，可关联到用户 Profile 与邮件目的地；
    ②OTFC 支持的每种用户语言各有一份；③Exchange 集成场景必须勾选 "Exchange integration" 且正文
    格式选 "Text"——该格式只影响邮件通知，与 Web 访问无关；④它必须经用户 Profile 关联到用户才
    生效。管理路径：Sites ➤ Site ➤ Configuration ➤ Mail Notification Profiles ➤ Properties ➤
    Notification Options。
  conditions: 多语言组织按语言分 Profile
  tags: [rule, notification, exchange, menu-path]

- id: p24
  title: LDAP 声明参数口径（enabled、服务器、端口 389、Search base、Test connection、属性映射、断连 SNMP trap）
  type: checklist
  source_pages: p195-197
  source_chapter: LDAP Server (Default: Active Directory)
  source_quote: |
    "Configure the LDAP directory parameters: • Tick: enabled • Server: eco.company.com • Port:
    389 • Search base: cn=users,dc=company,dc=com • The Search Base indicates where in the tree
    the search begins in the LDAP directory • Test the connection" (p196)
    "If the connection is lost between fax server and LDAP directory a SNMP trap is generated ...
    select the Attributes tab to match the OTFC & LDAP server attributes" (p196-197)
  summary: |
    外部目录声明清单：勾 enabled；填服务器地址（实验口径 eco.company.com）；端口 389（LDAP 明文
    口径）；Search base 填搜索树起点（实验口径 cn=users,dc=company,dc=com）；点 Test connection
    验证。另两条：断连时自动产生 SNMP trap（监控可挂告警）；Attributes 页签做 OTFC 与 LDAP 服务
    器的属性匹配。
  conditions: eco.company.com/389/cn=users... 均为实验口径
  tags: [checklist, ldap, parameters]

- id: p25
  title: NT Account Lookup 过滤器与 IIS 自动登录开关口径
  type: rule
  source_pages: p201-204
  source_chapter: NT Account Lookup / Automatic NT Log-in to the Web Access
  source_quote: |
    "Configure a new LDAP directory with this specific 'Search Filter':
    (&(objectClass=user)(objectCategory=person)(samAccountName=$NtAccountName$)) ... The
    samAccountName attribute is an Active Directory attribute containing the name of a user in a
    Windows domain." (p202)
    "This requires some configuration on IIS. • OTFC server must be a member of the domain ...
    5. Right-click Anonymous Authentication and select Disable if it was enabled. 6. Right-click
    Windows Authentication and select Enable if it was disabled." (p204)
  summary: |
    两条免密登录配置口径：①LDAP 集成路线用固定 Search Filter——
    (&(objectClass=user)(objectCategory=person)(samAccountName=$NtAccountName$))，samAccountName
    是 AD 中存 Windows 域用户名的属性，并在 Conditions 页签加条件（p203）；另一条路是 AD NT
    Account Lookup 专用接口（p201）。②Web 自动登录的 IIS 口径——Default Web Site → Authentication
    里禁用匿名认证、启用 Windows Authentication，且 OTFC 服务器必须是域成员。
  conditions: 需要域环境；两开关按序操作
  tags: [rule, nt-account, iis, ldap, filter]

- id: p26
  title: 入局路由表口径：三类规则、Default 恒最后、Directories Lookup 值 $did:?????$
  type: rule
  source_pages: p205-207
  source_chapter: Incoming Routing Table
  source_quote: |
    "The routing can be done by a multiple combination of routing rules: •Direct rules •Directory
    Lookup rules •Default rule that applies a default routing to misrouted faxes (faxes that
    failed all the rules of the table). Routing rules can be ordered in the Incoming Routing
    Table (except the Default rule, that remains the last)" (p205)
    "Configure the « Directories Lookup » to match with DDI fax numbers managed in internal users
    or external directories (LDAP): • Replace the default value by $did:?????$" (p207)
  summary: |
    规则三条：①入局路由规则三类——Direct 规则、Directory Lookup 规则、Default 兜底规则（对没被
    任何规则命中的错投传真做默认路由）；②规则可排序，但 Default 规则永远排最后、不可移动；③
    Directories Lookup 匹配 DDI 传真号时把默认值替换为 $did:?????$（? 个数对应号码位数口径，按
    实际号长调整）。来话通知故障查 ConfigManager.log 与 Smtp.log（p208）。
  conditions: DDI 书中未展开全称（通用含义 Direct Dial-In，推断）
  tags: [rule, routing, ddi, did]

- id: p27
  title: DTMF 路由语法：+33155667000 P 1234，P=暂停；可激活默认语音提示
  type: rule
  source_pages: p209
  source_chapter: DTMF for outgoing and incoming faxes
  source_quote: |
    "Allows users to send or receive faxes with adding DTMF codes for additional numbering
    dialing. • A default voice prompt could be activated • It asks the fax sender to enter an
    extension number (DTMF code) to route the fax to the appropriate recipient ... +33155667000 P
    1234 ; P = Pause PABX with public number ... After pause, DTMF 1234 sent by OT, to reach Fax
    machine" (p209)
  summary: |
    语法口径：目的地号码后加 P 与 DTMF 分机号（例 +33155667000 P 1234，P=暂停），暂停后发 DTMF
    1234 指向传真机；来话方向激活默认语音提示"请输入 4 位分机"后，主叫键入分机即可路由。适用
    于 PABX 公共号码+分机的场景。示例号码为实验口径。
  conditions: 语音提示可开关
  tags: [rule, dtmf, routing]

- id: p28
  title: Modification Table 规则示例：超过 6 位且 33 开头的外部号→前两位 33 换 00
  type: rule
  source_pages: p210-211
  source_chapter: Modification Table
  source_quote: |
    "Used to modify the destination fax number given by the end-users in case of numbers providing
    from directories or contacts ... Example: for external numbers (more than 6 digits) beginning
    by 33 (country code for France), the 2 first digits (33) will be replaced by 00 (ARS prefix +
    national prefix)" (p211)
    "1) Send fax to the contact Mr Dupond 33298765432 ... 4) Called number: 00298765432" (p210)
  summary: |
    规则与示例：Modification Table 用于规整用户从目录/联系人带来的目的地传真号；书例——超过 6 位
    且以 33（法国国家码）开头的外部号，把前两位 33 替换为 00（ARS 前缀+国内前缀），即 33298765432
    实际呼出 00298765432。客户联系人库存国际格式而 PSTN 要拨 ARS 前缀时，用它免改通讯录。
  conditions: 33/00 为法国示例；ARS 书中未展开全称
  tags: [rule, modification-table, ars]

- id: p29
  title: OTFC 侧 SIP 口径：本地 SIP UDP 端口 5360；单 PBX 时 dial plan 全号码（*）路由
  type: metric
  source_pages: p142, p144
  source_chapter: OmniPCX Enterprise & OTFC / SIP configuration / OmniPCX Enterprise declaration
  source_quote: |
    "SIP configuration • Local SIP UDP port: 5360 • Activate SIP message in log files (for
    maintenance) • SIP authentication" (p142)
    "Configure dial plan for outgoing calls: • In case of mono PBX (default configuration), all
    calls (*) are routed to this PBX." (p144)
  summary: |
    两条口径：①OTFC 本地 SIP 监听为 UDP 5360（防火墙放行与排障核对点）；维护时可激活"日志中记录
    SIP 消息"；支持 SIP 认证。②拨号计划：单 PBX（默认配置）时所有号码（*）都路由到该 PBX；多
    PBX 或空间冗余时按号码模式分派（见 framework f23）。
  conditions: 端口为 OTFC 侧；OXE 侧另有端口体系
  tags: [metric, sip, port, dial-plan]

- id: p30
  title: OXE 侧七步与号段口径：mtcl 默认账号、#31600-31699、MGR 或 OmniVista 8770
  type: metric
  source_pages: p152, p155
  source_chapter: OXE SIP gateway configuration (How-To)
  source_quote: |
    "Use MGR or Omnivista 8770 to manage. mtcl is the default login & password ... login: mtcl
    Password: mtcl … (101)csa> mgr" (p152)
    "1.7. Routing number configuration • OXE users directory numbers #31600 to 31699 • Select mgr
    / Translator / Prefix plan/ Create" (p155)
  summary: |
    口径三条：①OXE 侧管理入口为 MGR 命令行（csa 下敲 mgr）或 OmniVista 8770；②默认登录账号与
    密码均为 mtcl（出厂/实验口径，生产必须改）；③路由号配置示例：把 OXE 用户目录号 #31600-31699
    （实验口径号段）经 mgr / Translator / Prefix plan / Create 指向传真网关。七步菜单序列见
    framework f24。
  conditions: mtcl/mtcl 为默认口径；号段为实验口径
  tags: [metric, oxe, mgr, mtcl, lab]

- id: p31
  title: OXE 侧抓包命令逐字口径（tuner/actdbg/mtracer/traced/tcpdump 参数与停止方式）
  type: checklist
  source_pages: p148-150
  source_chapter: Maintenance
  source_quote: |
    "tuner km ; tuner clear-traces ; tuner +cpu +cpl +at hybrid=on ; actdbg all=off sip=on
    abcf=on ; mtracer -ag -d -1 /DHS3dyn/tmp/CHtrace -s 1000000 -f 90 ; To stop the capture: •
    Use 'Control C' • Or kill the process 'traced' with the command : 'killall mtracer'" (p148)
    "motortrace 3 ; traced -d -1 /DHS3dyn/tmp/motortrace -s 1000000 -f 90 ... 'killall traced'" (p149)
    "tcpdump –s 2000 –w /tmp/oxetrace.pcap ... Use ftp to get the file on a PC • Use 'bin' as
    transfer mode • Open the file with Wireshark" (p150)
  summary: |
    三组命令逐字转写（均在 OXE 呼叫服务器 mtcl 账号下）：①呼叫处理 trace：tuner km → tuner
    clear-traces → tuner +cpu +cpl +at hybrid=on → actdbg all=off sip=on abcf=on → mtracer -ag
    -d -1 /DHS3dyn/tmp/CHtrace -s 1000000 -f 90（生成 CHtrace-XX 滚动日志；停止 Control C 或
    killall mtracer）；②SIP trace：motortrace 3 → traced -d -1 /DHS3dyn/tmp/motortrace -s
    1000000 -f 90（生成 motortrace-XX；停止 Control C 或 killall traced）；③网络抓包：tcpdump
    -s 2000 -w /tmp/oxetrace.pcap（停止 Control C），FTP 以 bin 模式取回 PC 用 Wireshark 打开
    （可按 SIP 过滤）。-s 1000000 -f 90 为滚动大小与保留个数口径。
  conditions: 命令在 OXE 侧执行，非 OTFC 侧；路径为 OXE 约定路径
  tags: [checklist, traces, commands, oxe]

- id: p32
  title: SMTP 网关口径：监听 25、不能与其他 SMTP 共存、feedback address 不能为空、可收 NDR
  type: rule
  source_pages: p161, p183
  source_chapter: SMTP Gateway (Inbound) / SMTP Gateway
  source_quote: |
    "A feedback address must be filled in the SMTP Gateway settings to enable reply from the
    gateway with a mail header (mail header can't be empty!). ... Receive NDR (Non-Delivery
    Report) messages in case the mail server would not be able to deliver some notifications
    sent by the Fax Server" (p161)
    "The gateway acts as an SMTP mail server (listens on port 25) to accept new fax jobs • It
    cannot run on a server where another SMTP server is in use" (p183)
  summary: |
    四条规则：①SMTP 网关以邮件服务器身份监听系统 25 端口接收传真作业；②同一服务器上不能有另一
    个 SMTP 服务在用（与 Microsoft SMTP 服务冲突，见安装章）；③网关设置里必须填 feedback address
    （邮件头不能为空），否则无法回信；④经客户 LAN 中继可消除外部时延影响并接收 NDR
    （Non-Delivery Report，书中有全称）——邮件服务器投不出通知时能回告。
  conditions: 25 端口冲突处理见安装流程（先停禁 MS SMTP 再启 XMSMTPGateway）
  tags: [rule, smtp, port, ndr]

- id: p33
  title: Exchange 集成寻址格式全集与 New-SendConnector 命令逐字口径
  type: metric
  source_pages: p163-164, p167
  source_chapter: Sending & Receiving Faxes from an e-mail client / Microsoft Exchange Integration / Creation of SMTP connector
  source_quote: |
    "31600@<your fax server FQDN> ; Without Outlook contacts: [FAX:0298131600] ; With Outlook
    contacts: Terence Hill" (p163)
    "[FAX:5141234567] • [FAX:John Smith@5141234567] •
    [FAX:/fn=John/ln=Smith/jobtitle=Manager@5141234567] ; Usage: • 5141234567@fax.<your domain> •
    5141234567/fn=John/ln=Smith/co=Ac" (p164)
    "New-SendConnector -Name <ConnectorName> -AddressSpace \"fax:*;1\" –SmartHosts
    \"<SMTPGateway>\" –DNSRoutingEnabled $false -SourceTransportServers
    \"<HubTransportServers>\" ... Example: New-SendConnector -Name OTFC -AddressSpace \"fax:*;1\"
    –SmartHosts \"fax.company.com\" -DNSRoutingEnabled $false –SourceTransportServers
    \"eco.company.com\"" (p167)
  summary: |
    寻址格式全集：①普通域内——31600@<传真服务器 FQDN>；②无 Outlook 联系人——[FAX:0298131600]；
    ③有 Outlook 联系人——直接选联系人（Terence Hill）；④扩展——[FAX:号码]、[FAX:姓名@号码]、
    [FAX:/fn=名/ln=姓/jobtitle=职务@号码]，或 5141234567@fax.<域名>、5141234567/fn=John/ln=Smith/
    co=Ac…（斜杠属性语法）。命令模板与示例（实验口径 fax.company.com/eco.company.com）逐字如引文；
    建好后 SEND connector 出现在组织 Hub transport 列表，并在 Exchange admin center → Mail flow →
    Send Connectors 核验。
  conditions: SMTP connector 为许可特性（p158）；示例值为实验口径
  tags: [metric, exchange, addressing, command]

- id: p34
  title: 服务管理命令口径：xmsc -ra/-oa/-aa 与 Bin\Util 路径
  type: metric
  source_pages: p188, p218, p231-232
  source_chapter: Managing the services / Backup process / OTFC Backup & restore (How-To)
  source_quote: |
    "All these commands can be executed from the <install_path>\FaxCenter\Bin\Util folder. •
    Restarting Services • To restart all Fax Services, use the command: • xmsc –ra • Stopping
    Services • To stop all Fax Services, use the command: • xmsc –oa • Starting Services • To
    start all Fax Services, use the command: • xmsc -aa" (p188)
    "From the command line tool: « <Install_path>\FaxCenter\Bin\Util folder », launch: xmsc -oa"
    (p218)
  summary: |
    命令三条（在 <install_path>\FaxCenter\Bin\Util 下执行）：xmsc -ra 重启全部传真服务；xmsc -oa
    停止全部；xmsc -aa 启动全部。备份/恢复实验（p231-232）用 xmsc -oa 停、xmsc -aa 启，配合
    mysql5 服务的停启。是 Windows 服务界面之外的脚本化通道。
  conditions: 参数与文件名一致（实验口径含 mysql5 服务名）
  tags: [metric, commands, services, xmsc]

- id: p35
  title: 日志口径：每组件一个文件、Trace 目录、默认单文件 20MB、归档保留 15 天、满后 zip 入 Archive
  type: metric
  source_pages: p189, p225
  source_chapter: Log files / Logs
  source_quote: |
    "Each OTFC component has a dedicated log file. Log files location: • C:\Program
    Files\Alcatel-Lucent Enterprise\FaxCenter\Trace" (p189)
    "Trace folder stores log files for all the OTFC services. Through the admin interface, System
    Administrators can configure: • Log Size (default is 20 MB) • Archive Retention Period
    (default is 15 Days). • Whenever a log file reaches the size limit configured for it, Fax
    compresses (zip) the log file and puts it in the Archive folder." (p225)
  summary: |
    四条口径：①每个 OTFC 组件有专属日志，统一在 C:\Program Files\Alcatel-Lucent
    Enterprise\FaxCenter\Trace（<install_path> 口径）；②日志大小默认 20MB（System Administrators
    经管理界面可配）；③归档保留期默认 15 天；④日志到大小上限后自动 zip 压缩放进 Archive 文件夹。
    排障时先按组件找对应日志（如 ConfigManager.log、Smtp.log，p208）。
  conditions: 默认值为 R9.2 口径
  tags: [metric, logs, retention]

- id: p36
  title: 备份数据三域与注册表键口径（Config/Data/Bin + MySQL + Interstar Technologies 键；电话本用户自备）
  type: checklist
  source_pages: p217-219, p231
  source_chapter: Backup - Data encompasses 3 portions / Backup process / Backing up users phone books / OTFC Backup & restore (How-To)
  source_quote: |
    "Configuration and states are stored in the Windows registry, the Config and Data folders and
    in the MySQL database. ; Fax metadata (MySQL database) • Contains the records of sent and
    received faxes. ; Fax images and documents (MediaStore) • ... Stored under the Data\MediaStore." (p217)
    "Make copies of OTFC Data folders where the Fax is installed • the Data folder • The Bin
    folder • The Config folder ; Make a copy of the MySQL Data folder, found in the folder where
    MySQL was installed ; Export the HKEY_LOCAL_MACHINE\SOFTWARE\Interstar Technologies key from
    Regedit to a .reg file" (p218)
    "Users\<username>\AppData\Roaming\Fax\PhoneBook." (p219)
    "C:\Program Files\MySQL\MySQL Server 8.0 \Data" (p231)
  summary: |
    备份清单逐格：①传真服务器侧拷三文件夹——Data、Bin、Config（FaxCenter 安装目录下）；②MySQL
    数据目录整拷（实验口径 C:\Program Files\MySQL\MySQL Server 8.0\Data）；③注册表导出
    HKEY_LOCAL_MACHINE\SOFTWARE\Interstar Technologies 键为 .reg 文件（键名揭示 OTFC 前身
    Interstar Technologies 的 XMedius 产品线）；④用户私人电话本不在系统备份内，各用户自备份
    Users\<username>\AppData\Roaming\Fax\PhoneBook。数据三域对应：配置与状态（注册表+Config/Data
    +MySQL）、传真元数据（MySQL）、传真图像与文档（Data\MediaStore）。
  conditions: 路径为实验/默认安装口径
  tags: [checklist, backup, registry, mysql]

- id: p37
  title: 备份与恢复的停服语义差：备份"停止不可 kill"，恢复"停止可 kill"
  type: rule
  source_pages: p216, p220
  source_chapter: Backup / Restore
  source_quote: |
    "All fax server services (including MySQL) must be stopped (not killed) before backing up." (p216)
    "All fax server services (including MySQL) must be stopped before restoring (can be killed). •
    Current data (the Windows registry hive, the Config and Data folders and the MySQL database)
    must be erased prior to restoring. • The version of the fax server software must be equivalent
    • The topology of the system must be identical. • The backed up data must be restored at the
    same places in the file system as the original installation" (p220)
  summary: |
    一条易混规则：备份前服务必须正常"停止"（不能 kill——要留状态落盘）；恢复前服务停止（此时可
    kill——数据反正要被覆盖）。恢复四前提：环境与备份时相似；版本等同；拓扑一致；数据回灌到与原
    安装相同的文件系统路径。恢复简化流程：停服→回灌 Data/Bin/Config→回灌 MySQL→导 .reg→重启。
  conditions: 备份不能热备（维护窗口停机）
  tags: [rule, backup, restore]

- id: p38
  title: 升级口径：直接跑新装程序、改写状态文件与 xmedius.war、数据库（CompanyConfig/XmediusArchive）不在自动备份内、自定义工具先验证
  type: checklist
  source_pages: p221-222
  source_chapter: Upgrade / Upgrade - Recommended practice
  source_quote: |
    "The upgrade modifies or overwrites the files that hold the state of the system. ... The
    upgrade process will backup any state-related file it modifies, with the exception of the
    databases (CompanyConfig and XmediusArchive). ... The web-related package (xmedius.war) will
    be replaced during the upgrade. If you made custom modifications to the web interface, you
    will have to re-apply them after the upgrade. If you have built custom tools (external
    notification software, JavaApi scripts, reports that query the archive database etc.), it is
    highly recommended that you check to make sure those tools will integrate properly with the
    new version of OTFC. Install the software on a test system before upgrading your production
    system." (p221)
    "1.Make sure the system is sane 2.Stop traffic 3.Stop services 4.Backup the data 5.Upgrade
    the system" (p222)
  summary: |
    升级五步法：①确认系统健康→②停流量→③停服务→④备份数据→⑤执行升级。四个善后口径：升级会
    改写 [install_path]\FaxCenter\Data、Config 与 MySQL；自动备份被改的状态文件但数据库
    （CompanyConfig 与 XmediusArchive）除外——升级前必须手工备份；Web 包 xmedius.war 被替换，对
    Web 界面的自定义修改要重做；自定义工具（外部通知、JavaApi 脚本、查归档库的报表）要先在测试
    系统验证再上生产。新第三方软件装新禁旧但保留在盘上。
  conditions: 数据库名 CompanyConfig/XmediusArchive 揭示 XMedius 血统
  tags: [checklist, upgrade, xmedius]

- id: p39
  title: 报表与监控口径：31 个报告模板、BIRT 设计器装在 3rd\birt、SNMP V2 trap 十三类
  type: metric
  source_pages: p226, p228
  source_chapter: Reports / Monitoring
  source_quote: |
    "Reports can be executed by using the available report templates •It is possible to manage and
    customize the report templates by using the BIRT report designer •To install the BIRT report
    designer , unzip the .zip file found in the 3rd\birt folder of the OTFC installation package ;
    31 reports are available" (p226)
    "SNMP V2 Services • Component status changes •Incoming queue reaches max size •Site outbound
    quota reaches maximum size •Rasterization failure •Routing failure •XML file reading error
    •Driver transmission error •Partition detection •Channel initialization failure •Host monitor
    traps ▪Component status changes •Performance counter •Components status table •Channel state
    •Monitoring hearts beats from remote host" (p228)
  summary: |
    逐格转写：①31 个报告模板，含数值与图形，覆盖全系统/单用户×月/周/日、模块错误摘要；自定义用
    BIRT 报表设计器（解压安装包 3rd\birt 下的 zip 安装）；②SNMP V2 trap 清单——组件状态变化、
    入呼队列达上限、站点出呼配额满、光栅化失败、路由失败、XML 文件读取错误、驱动发送错误、分区
    检测、通道初始化失败；主机监视 trap——组件状态变化、性能计数器、组件状态表、通道状态、远程
    主机心跳。
  conditions: BIRT 细节与 SNMP 网管平台在书外
  tags: [metric, reports, birt, snmp]

- id: p40
  title: 传真计费口径：OXE 生成话单→OmniVista 8770 取票出报表；映射默认传真号
  type: rule
  source_pages: p212-213
  source_chapter: Accounting of fax calls
  source_quote: |
    "Fax outgoing call generates an accounting ticket on the OmniPCX Enterprise • 8770 gets the
    accounting tickets from the OmniPCX Enterprise • Use reports in 8770 billing application to
    analyse telecommunications costs" (p212)
    "Fax accounting tickets can be mapped to the user's phone number or the user's fax number •
    Default mapping is fax number" (p213)
  summary: |
    计费链路：外发传真在 OXE 生成计费票（accounting ticket）→ OmniVista 8770（网络管理与计费）从
    OXE 下载票→用 8770 标准报表或自建报表分析电信成本。票可映射到用户电话号或用户传真号，默认
    映射为传真号——按人核算时注意改映射口径。
  conditions: 8770 侧报表细节在书外
  tags: [rule, accounting, 8770]

- id: p41
  title: 入呼通知故障排障口径：查 ConfigManager.log 与 Smtp.log
  type: rule
  source_pages: p208
  source_chapter: Incoming Routing Table
  source_quote: |
    "In case of email notification problem for incoming fax, you can check: • Using Admin interface
    • In 'ConfigManager.log' and 'Smtp.log' file • Example of ConfigManager.log:" (p208)
  summary: |
    排障规则：来传真邮件通知有问题时，经管理界面查两个日志文件——ConfigManager.log 与 Smtp.log
    （位于 Trace 目录，见 p35 条目）。ConfigManager.log 里有路由/查找过程记录可对照。
  conditions: 日志默认 20MB/15 天滚动（p35）
  tags: [rule, troubleshooting, logs]

- id: p42
  title: 电话簿 LDAP 访问三处开关口径（Enable LDAP Access 在 Fax Archive 属性、认证在 General Settings、属性映射）
  type: checklist
  source_pages: p138-139
  source_chapter: LDAP Access to the Phone Books
  source_quote: |
    "the Enable LDAP Access box must be checked in the System Configuration ➤ Fax Archive
    properties of your host" (p138)
    "LDAP authentication • You can set the Authentication in Configuration ➤ General Settings
    properties of the site ; LDAP Attribute Mapping • To match attributes between OTFC and LDAP
    server" (p139)
  summary: |
    三处配置：①主机级——System Configuration ➤ Fax Archive 属性里勾 Enable LDAP Access（企业电
    话簿才可经 LDAP 访问）；②站点级——Configuration ➤ General Settings 属性里设 LDAP 认证；
    ③LDAP Attribute Mapping 匹配 OTFC 与 LDAP 服务器属性。corporate 电话簿在 Webadmin 管理、可
    建多本、联系人可分组（p136）。
  conditions: 菜单名 Fax Archive 与归档服务同名，注意是在主机属性里
  tags: [checklist, phonebook, ldap, menu-path]

- id: p43
  title: 删除策略口径：传真记录与传真文档两类可分开/一起删（零保留合规）
  type: rule
  source_pages: p223-224
  source_chapter: Fax deletion policy
  source_quote: |
    "There are two types of fax elements that can be deleted, either separately or together: • The
    fax records, corresponding to the entries of the archive database, including all fax
    information (metadata) and excluding the fax documents (image files) • The fax documents,
    corresponding to the fax image files stored in the Mediastore folder. Right click" (p223)
  summary: |
    规则：清理系统时删除对象分两类——传真记录（归档库条目，含全部元数据、不含图像文件）与传真
    文档（Mediastore 文件夹的图像文件）；两类可分开删或一起删，配置界面为右键操作。与概览页
    （p6）"可配置零保留以降低泄露风险"呼应——GDPR/HIPAA 类客户按此设计保留策略。
  conditions: 删除不可逆，合规口径需客户确认
  tags: [rule, deletion, compliance]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 24 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 评估 OTFC 方案能力与规模上限 | 有 | p01, p02, p03 | 容量 15000/30、协议速率、45 格式、路由四法 |
| task-02 | 规划部署架构 | 有 | p05, p06, p07 | OS/虚拟化/邮件/客户端支持矩阵 |
| task-03 | 准备传真服务器宿主 | 有 | p09, p10, p11 | IIS 四角色服务、服务账号六权限、DNS 正反解判据 |
| task-04 | 安装 OTFC 软件 | 有 | p08, p12, p15 | 实验参数全表、语言副作用、密码口径 |
| task-05 | 跑 First Time Setup Wizard | 有 | p16, p17 | FTW 十二项动作与 QOS/CSID 固定值、事后运行路径 |
| task-06 | 处理许可 | 有 | p13 | 评估许可五边界、MAC 采购、手工导入 |
| task-07 | 创建与管理用户 | 有 | p14, p20, p21 | URL 口径、时区三影响、CSV 仅 Webadmin |
| task-08 | 创建 System/Site 管理员 | 有 | p22 | 认证方式三基与 SSO/SAML |
| task-09 | 安装并测试客户端 | 有 | p18, p19 | 浏览器与合规口径、静默/GPO/ClientRedistribution |
| task-10 | 定制封页 | 部分 | p12 | 封面语言受安装语言影响；五步流程在 framework f18，无独立数值 |
| task-11 | 设计与管理用户 Profile | 有 | p23, p26 | 邮件通知 Profile 口径、呼号限制相关（Restriction 结构在 f21） |
| task-12 | 管理电话簿 | 有 | p42 | LDAP 访问三处开关 |
| task-13 | 配置 OTFC 侧 SIP 与 OXE 声明 | 有 | p29 | UDP 5360、dial plan * |
| task-14 | 配置 OXE 侧 SIP 网关 | 有 | p30 | mtcl 默认账号、号段 #31600-31699、七步序列锚点 |
| task-15 | OXE 侧传真故障抓包 | 有 | p31 | 三组命令逐字口径 |
| task-16 | 集成邮件系统 | 有 | p32, p33 | 端口 25/feedback/NDR、寻址全集与 New-SendConnector 逐字 |
| task-17 | 认知与运维服务架构 | 有 | p34, p35 | xmsc 三命令、日志 20MB/15 天 |
| task-18 | 集成外部目录与高级路由 | 有 | p24, p25, p26, p27, p28 | LDAP 参数、NT 过滤器与 IIS 开关、$did、DTMF、Modification |
| task-19 | 配置传真计费 | 有 | p40 | 话单链路与映射默认值 |
| task-20 | 备份与恢复系统 | 有 | p36, p37 | 三域清单与停服语义差 |
| task-21 | 升级系统 | 有 | p38 | 五步法与四个善后口径 |
| task-22 | 配置传真删除策略 | 有 | p43 | 两类删除对象与零保留 |
| task-23 | 报表与监控 | 有 | p39 | 31 报表、BIRT 路径、SNMP trap 清单 |
| task-24 | 按日志定位通知/路由故障 | 有 | p41, p35 | ConfigManager.log/Smtp.log 判据与日志默认值 |

**覆盖结论**：24/24 全部有对应条目（task-10 封页的结构在 framework f18、数值口径 p12，两文件合计覆盖）。两点口径说明：
1. task-02/15 中的生产化数值（端口全表、Feature List 明细）原书外置，本文件按"书内事实"如实标注指针，未编造。
2. p07 客户端矩阵中 "Outlook 2022" 为原文笔误，已忠实转写并标注；p03/p26 中 DNIS/CSID/ANI/DDI/ARS 书中未给全称，括注均标"推断"。
