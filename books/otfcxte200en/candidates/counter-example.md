# 反例/限制/边界/易错点候选 — OpenTouch Fax Center Starter (OTFCXTE200EN R9.2 Ed04)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 扫描口径：逐页核查 Warning / Note / Important / 括注提示 / 前后不一致处；推断性结论已标"（推断）"。

```yaml
- id: n01
  title: 教材口径"关闭本地与网络防火墙"——生产环境绝不照搬
  type: warning
  source_pages: p48, p56
  source_chapter: Preparing the server / Preparing the FAX server host (How-To)
  source_quote: |
    "Disable firewall ; Local & network." (p48)
    "1.6. Disable the local firewall: ... in the Domain Profile tab, change the Firewall state to
    Off. • Repeat this step for the Private Profile and Public Profile tabs." (p56)
  summary: |
    准备服务器步骤里明写关闭本地防火墙，How-To 更是要求三个 Profile（域/专用/公用）全关。
    这是实验环境的简化口径：生产环境必须保持防火墙开启并按端口白名单放行——但端口使用表
    （p42）在书内只有标题没有数值，真实端口清单要去 OTFC Features List 查。照书关防火墙上生产
    是安全事故级错误。
  conditions: 任何生产部署
  tags: [warning, firewall, security, lab-only]

- id: n02
  title: SMTP 25 端口冲突：MS SMTP 不停禁，XMSMTPGateway 起不来
  type: warning
  source_pages: p49, p65, p183
  source_chapter: Software installation / Installation (How-To) / SMTP Gateway
  source_quote: |
    "Disabling the Microsoft SMTP service • OTFC SMTP gateway service uses system port 25, the
    same port as Microsoft's SMTP service, conflicts may arise" (p49)
    "Disable Microsoft's SMTP service before starting the OpenTouch Fax Center SMTP gateway
    service." (p65)
    "The gateway acts as an SMTP mail server (listens on port 25) ... It cannot run on a server
    where another SMTP server is in use" (p183)
  summary: |
    OTFC SMTP 网关监听系统 25 端口，与 Microsoft SMTP 服务（及任何其他 SMTP 服务）互斥。顺序
    规则：先 Stop 并 Disable Microsoft SMTP 服务，再启动 XMSMTPGateway（默认启动类型 Automatic）。
    现象对号：装完传真后邮件入口收不到传真任务，先查是不是 25 端口被占了。
  conditions: 服务器同机装有其他 SMTP 服务时
  tags: [warning, smtp, port-conflict]

- id: n03
  title: 默认评估许可打水印、只有 2 通道——验收前必须换正式许可
  type: limitation
  source_pages: p52
  source_chapter: Licensing
  source_quote: |
    "a default license is automatically • Installed for evaluation purposes, that: • Enables one
    instance of each component • Enables a total of two channels (FoIP and fax boards) in
    evaluation mode • Enables up to 10 sites with no time limit • Allows for 100 users • Applies
    a watermark on every fax page" (p52)
  summary: |
    首装自动带的评估许可有五条硬边界：每组件 1 实例、FoIP+板卡合计 2 通道、最多 10 站点、100
    用户、每页传真打水印。测试时"怎么每张传真都有水印/并发就 2 路"是许可边界，不是故障；正式
    交付验收前必须完成许可采购与导入。
  conditions: 未导入正式许可的阶段
  tags: [limitation, licensing, watermark]

- id: n04
  title: 许可采购绑定服务器 MAC 地址，且只能手工导入
  type: limitation
  source_pages: p52-53
  source_chapter: Licensing / Import licenses
  source_quote: |
    "To purchase and receive a license, you will need to provide your OpenTouch Fax Center
    reseller with your server physical (MAC) address." (p52)
    "Import license file manually only" (p53)
  summary: |
    两条流程边界：①买许可前要先从传真服务器取物理（MAC）地址给经销商——服务器换网卡/换虚拟机
    MAC 变化会导致许可问题（（推断）MAC 绑定意味着虚拟化迁移时要注意，书中未展开）；②许可文件
    只能手工导入，无自动/在线激活通道。许可流程的商务环节在书外。
  conditions: 许可采购与导入时；虚拟化部署 MAC 变化场景（推断）
  tags: [limitation, licensing, mac]

- id: n05
  title: 安装语言有持久副作用：决定默认邮件通知 Profile 与基本 Profile 封面语言
  type: warning
  source_pages: p59, p63
  source_chapter: Installation (How-To)
  source_quote: |
    "The installation language will define the default Mail Notification Profile used with new
    profiles and new Mail Notification Destinations. It will also define the cover sheet language
    used in the basic Profile." (p59, p63 两页同文)
  summary: |
    Setup 向导选语言时容易当成"界面语言随便选"——它实际决定两处持久默认值：新建 Profile 与新
    邮件通知目的地的默认邮件通知 Profile、基本 Profile 的封面语言。选错语言的善后是手工改默认
    Profile，比装时选对麻烦得多。多语言组织按主流语言定。
  conditions: 首装一次性决策
  tags: [warning, installation, language]

- id: n06
  title: 安装时设的密码全是临时的，首登强制改；教材默认值 Alcatel1!@123 已是公开秘密
  type: warning
  source_pages: p49, p62, p115
  source_chapter: Installation / First Time Setup Wizard (How-To)
  source_quote: |
    "Password: 123456 • To change at the first login: Alcatel1!@123" (p49)
    "The password is temporary. You will have to change it at first login." (p62)
  summary: |
    安装向导里设的密码（书例 123456）只是临时密码，系统管理员与首用户首登都会被强制改密。教材
    把实验新密码统一写成 Alcatel1!@123——该值随教材公开，生产环境若沿用等于没改密。交付检查表
    必须包含"所有默认/教材密码已替换为客户专属值"。
  conditions: 所有部署；含 mtcl/mtcl（OXE 侧默认账号，p152）
  tags: [warning, security, passwords]

- id: n07
  title: Office 未预初始化会让 Rasterizer 首跑弹窗卡死
  type: warning
  source_pages: p51, p56
  source_chapter: Initial set-up / Preparing the FAX server host (How-To)
  source_quote: |
    "Pre-initialize Office environment • Install Microsoft Office • Open MS Word and MS Excel to
    ensure that no Welcome screen or error messages occur for XMDocumentRasterizer" (p51)
    "Launch an Office application: Start ➤ Excel. • Ensure no dialog boxes pop up. • Note: The
    Office applications have already (before the training) been launched in the service account
    context." (p56)
  summary: |
    Rasterizer 依赖服务器本机 Office 转文档。Office 首次在服务账号上下文里启动会弹欢迎屏/激活/
    隐私等对话框，导致传真转换挂起。规则：装好 Office 后先以服务账号上下文把 Word/Excel/
    PowerPoint 各启动一次，确认无弹窗再投产。书里特意注明实验机"已在培训前做过"——现场不能省
    这步。
  conditions: 服务器装有 Microsoft Office 时（Rasterizer 必需）
  tags: [warning, rasterizer, office, first-run]

- id: n08
  title: 两种用户目录可共存——"必须二选一"是误解
  type: misconception
  source_pages: p100
  source_chapter: Users（Concept）
  source_quote: |
    "Internal Users: ... Simple way to give a few users access to the fax system • Active
    Directory integration: • Requires a Windows Domain ... Note: The two type of user's directory
    can co-exist" (p100)
  summary: |
    FTW 只呈现 Internal Database 与 AD 集成两个选项，容易被理解成互斥选型。原文明确：两种用户
    目录可以共存——常见形态是主体用户走 AD、少量外部/临时用户走内部库。规划时不该为"选型"
    纠结，按用户群体混用。
  conditions: 用户目录规划时
  tags: [misconception, users, active-directory]

- id: n09
  title: 用户 CSV 导入/导出在 MMC 里找不到——仅 Webadmin 提供
  type: limitation
  source_pages: p104-105
  source_chapter: Import users .CSV / Export users
  source_quote: |
    "Users can be imported by the Webadmin interface only" (p104)
    "The list of users could be exported by the Webadmin interface only" (p105)
  summary: |
    批量导入用户与导出用户清单两个功能都只在 Webadmin 界面，MMC Snap-in 没有。现场在 MMC 里
    翻不到"Import users"按钮属正常，切到 Web 管理界面操作；导入时第 3 步要选套用的 Profile。
  conditions: 批量用户操作时
  tags: [limitation, users, csv, webadmin]

- id: n10
  title: 不建备份管理员有锁死风险——官方推荐动作
  type: warning
  source_pages: p110, p115
  source_chapter: Create new SYSTEM administrator
  source_quote: |
    "It is recommended to create a backup administrator • Authentication based on internal
    server, AD and SAML" (p110)
    "3 Create a system backup administrator ... User Name backupadmin" (p115)
  summary: |
    只有一个 System 管理员时，该账号密码丢失/认证方式（如 SSO）故障即锁死整个系统。官方推荐
    建一个备份管理员（实验口径 backupadmin），认证基于内部服务器、AD 与 SAML——与主管理员用
    不同认证路径更能对冲风险（（推断）"对冲"为推断，原文只给推荐动作）。
  conditions: 交付收尾必做项
  tags: [warning, administrators, lockout]

- id: n11
  title: 客户端装在传真服务器上只是实验捷径——生产装在用户工作站
  type: misconception
  source_pages: p115, p131-132
  source_chapter: Create Users & administrators (How-To) / Clients installation (How-To)
  source_quote: |
    "Note: You are installing the client applications on the fax server. However, in a real -life
    scenario, it is rare to install the client applications on the fax server itself. Typically,
    they are installed on user workstations." (p115)
    "you may be asked to reboot the server. In this case, you can safely ignore the reboot
    request. You will not use the client applications on this server." (p132)
  summary: |
    两个实验口径要注意：①实验为省机器把客户端装在传真服务器上，原书两次强调真实场景装在用户
    工作站；②装完提示重启服务器"可安全忽略"——因为这台服务器本来不用这些客户端。生产中在用户
    PC 装客户端后该重启就重启，别把实验口径带进生产。
  conditions: 实验环境 vs 生产的口径切换
  tags: [misconception, clients, lab-only]

- id: n12
  title: 邮件通知格式勾"Exchange integration"+Text 只影响邮件——Web 界面显示不变
  type: misconception
  source_pages: p126
  source_chapter: User Profiles – Mail Notification profiles
  source_quote: |
    "'Exchange integration' has to be checked with 'Message body format: Text'. Format used for
    email notification, not for web access!" (p126)
  summary: |
    Exchange 场景要勾 "Exchange integration" 且正文格式选 "Text"，但这个格式只作用于邮件通知，
    与 Web Client 里的传真显示无关。把"通知里看不到传真图像"归咎于 Web 端是方向性误判——先看
    邮件通知 Profile 配置，再看 Web。
  conditions: Exchange 集成 + 通知格式排查时
  tags: [misconception, notification, exchange]

- id: n13
  title: SendFAX 的 Outlook 模式依赖 'FAX' 地址空间——没建连接器就别开
  type: limitation
  source_pages: p86, p164
  source_chapter: SendFax / Microsoft Exchange Integration
  source_quote: |
    "SendFAX configured in Outlook mode (i.e. to send the faxes through Outlook connected to
    Exchange) requires the use of a 'FAX' address space" (p86)
    "It is also necessary if you want to use SendFAX in Outlook/Exchange mode." (p164)
  summary: |
    SendFAX 在 Outlook 模式（经 Outlook 连 Exchange 发传真）要求 Exchange 侧已建 'FAX' 地址
    空间的 Send Connector。没建连接器就切 Outlook 模式会发不出去——先完成 SMTP 集成章（p164-170）
    再启用该模式。
  conditions: SendFAX Outlook/Exchange 模式启用前
  tags: [limitation, sendfax, exchange]

- id: n14
  title: SMTP connector 是许可特性——功能装得上、许可不.match 就用不了
  type: version-trap
  source_pages: p158
  source_chapter: Sending & Receiving Faxes from an e-mail client / Mail server
  source_quote: |
    "SMTP connector is a licensed feature" (p158)
  summary: |
    一句话陷阱：SMTP 连接器（Exchange 集成的 FAX 地址空间做法）是许可特性，受许可的"特性开关"
    层控制。评估许可/低配许可环境下连接器建好了也可能不生效——排障时把许可特性清单一并核查
    （与 p13 条目许可两级控制呼应）。
  conditions: Exchange 集成交付前核查许可
  tags: [version-trap, licensing, smtp]

- id: n15
  title: SMTP 网关 feedback address 不能为空——空着头通知回不了信
  type: warning
  source_pages: p161
  source_chapter: SMTP Gateway (Inbound)
  source_quote: |
    "A feedback address must be filled in the SMTP Gateway settings to enable reply from the
    gateway with a mail header (mail header can't be empty!)." (p161)
  summary: |
    网关设置里必须填 feedback address，否则网关无法带合法邮件头回信——通知邮件发不出。原文用
    了感叹号强调。排障"用户收不到传真通知邮件"时，在查 Exchange 之前先核对这一项。
  conditions: SMTP 网关入局通知配置时
  tags: [warning, smtp, notification]

- id: n16
  title: Exchange 收件安全过高会拦掉 OTFC 全部通知——调 Receive Connector
  type: warning
  source_pages: p170
  source_chapter: Allowing Reception of Mail Notification Messages
  source_quote: |
    "If you configured your Exchange server with high security for incoming SMTP messages, it
    could block all mail notifications coming from the OTFC SMTP Gateway. • In that case, you
    should adjust the Exchange security parameters in the properties of the Receive Connector,
    located in the Hub Transport node." (p170)
  summary: |
    Exchange 把 OTFC 网关当外部发件人时，高安全的入站 SMTP 策略可能"一封不留"拦掉全部传真通知。
    解法在 Exchange 侧：调 Hub Transport 节点下 Receive Connector 的安全参数，放行来自传真服务器
    的通知流量。现象对号：传真收发正常但通知邮件一封都不到。
  conditions: Exchange 作为邮件中继且安全策略收紧时
  tags: [warning, exchange, notification, receive-connector]

- id: n17
  title: OTFC 独占 25 端口的另一面：同机不能有别的 SMTP 服务常驻
  type: limitation
  source_pages: p183
  source_chapter: SMTP Gateway
  source_quote: |
    "It cannot run on a server where another SMTP server is in use" (p183)
  summary: |
    与 n02 同源的总规则：OTFC 服务器上不能再常驻任何其他 SMTP 服务器（包括把 OTFC 服务器顺带当
    邮件中继的想法）。混合部署要么换机器要么换端口方案（书中未给改端口路径），默认按独占 25
    规划。
  conditions: 服务器角色规划时
  tags: [limitation, smtp, deployment]

- id: n18
  title: 没有站点与 Profile 的外部用户直接被拒——Lookup 表没配等于没开通
  type: limitation
  source_pages: p198
  source_chapter: Site & Profile Lookup tables
  source_quote: |
    "A user who is not associated to any existing Site and any existing Profile is not allowed to
    use OTFC. Through these lookup tables it is possible to grant the faxing rights to some
    users" (p198)
  summary: |
    外部目录（AD/LDAP）用户即使查得到，只要没被 Site/Profile Lookup 表规则归到站点与 Profile，
    就完全不能用 OTFC。目录集成做完但"用户还是用不了"时，先查两张 Lookup 表的规则命中，别只盯
    目录连接。
  conditions: 外部目录用户授权场景
  tags: [limitation, lookup, users]

- id: n19
  title: Web 自动登录三前提：域成员 + 禁匿名 + 启 Windows 认证
  type: warning
  source_pages: p204
  source_chapter: Automatic NT Log-in to the Web Access
  source_quote: |
    "This requires some configuration on IIS. • OTFC server must be a member of the domain ...
    5. Right-click Anonymous Authentication and select Disable if it was enabled. 6. Right-click
    Windows Authentication and select Enable if it was disabled." (p204)
  source_chapter_note: 顺序为原文步骤 5、6
  summary: |
    NT 免密登录 Web 不是开关一开就行：①OTFC 服务器必须已是域成员；②IIS 的 Default Web Site →
    Authentication 里禁用匿名认证；③启用 Windows 认证。三缺一表现为"自动登录不生效、仍弹凭据框"。
    顺序按原文先禁匿名再启 Windows 认证。
  conditions: NT Account Lookup + IIS 配置场景
  tags: [warning, iis, nt-account, web]

- id: n20
  title: 入局路由 Default 规则永远排最后——排序再怎么调兜底都在
  type: limitation
  source_pages: p205
  source_chapter: Incoming Routing Table
  source_quote: |
    "Routing rules can be ordered in the Incoming Routing Table (except the Default rule, that
    remains the last)" (p205)
  summary: |
    入局路由表里 Direct/Directory Lookup 规则可调顺序，但 Default 规则固定最后、不可移动——它是
    "错投传真兜底"。想靠把 Default 排前面"先兜底再细匹配"的思路不成立，只能把精确规则排前面。
  conditions: 路由规则设计时
  tags: [limitation, routing]

- id: n21
  title: 备份必须冷备且服务"停止不可 kill"；恢复反过来"可 kill"
  type: warning
  source_pages: p216, p220
  source_chapter: Backup / Restore
  source_quote: |
    "Backups cannot be performed live, so it is suggested to perform them in a maintenance window
    (downtime). All fax server services (including MySQL) must be stopped (not killed) before
    backing up." (p216)
    "All fax server services (including MySQL) must be stopped before restoring (can be killed)." (p220)
  summary: |
    一对容易搞反的语义：备份前服务要正常停止（not killed）——强杀会丢状态、备出坏档；恢复前
    服务停止（can be killed）——数据反正被覆盖，等不及正常退出就 kill。且备份不能热备，要约
    维护窗口停机。自动化脚本里用 taskkill 强杀再备份属高危操作。
  conditions: 备份/恢复作业设计与执行时
  tags: [warning, backup, restore, maintenance-window]

- id: n22
  title: 用户私人电话本不在系统备份覆盖内——用户自备或换成公共电话簿
  type: limitation
  source_pages: p219
  source_chapter: Backing up users phone books
  source_quote: |
    "To preserve their phone books, individual users can backup the following folder:
    • Users\<username>\AppData\Roaming\Fax\PhoneBook." (p219)
  summary: |
    系统备份三域（Data/Bin/Config + MySQL + 注册表）不含用户私人电话本——它在各用户 PC 的
    AppData\Roaming\Fax\PhoneBook。重装用户机即丢。对电话本资产敏感的组织，把常用联系人收进
    Public（corporate）电话簿（随系统备份走）更稳（（推断）"更稳"为整理建议，原文只给路径）。
  conditions: 备份策略与用户端重装场景
  tags: [limitation, backup, phonebook]

- id: n23
  title: 升级三大陷阱：数据库不在自动备份内、xmedius.war 被替换、自定义工具要预验证
  type: warning
  source_pages: p221
  source_chapter: Upgrade
  source_quote: |
    "The upgrade process will backup any state-related file it modifies, with the exception of the
    databases (CompanyConfig and XmediusArchive). ... The web-related package (xmedius.war) will
    be replaced during the upgrade. If you made custom modifications to the web interface, you
    will have to re-apply them after the upgrade. If you have built custom tools (external
    notification software, JavaApi scripts, reports that query the archive database etc.), it is
    highly recommended that you check to make sure those tools will integrate properly with the
    new version of OTFC. Install the software on a test system before upgrading your production
    system." (p221)
  summary: |
    升级前的三个必查项：①升级自动备份被改的状态文件，但 CompanyConfig 与 XmediusArchive 两个
    数据库除外——升级前必须手工备库；②Web 包 xmedius.war 整包替换，对 Web 界面的自定义修改
    升级后要重做；③自定义工具（外部通知、JavaApi 脚本、查归档库的报表）与新版本兼容性要先在
    测试系统验证。官方流程五步（健康→停流量→停服务→备份→升级）里"备份"一步要含手工备库。
  conditions: 一切生产升级前
  tags: [warning, upgrade, database, customization]

- id: n24
  title: 原书编辑残留两处：SMB 页眉与首用户邮箱不一致——照抄实验值会迷路
  type: version-trap
  source_pages: p66, p151, p50, p70
  source_chapter: First Time Setup Wizard (How-To) / OXE SIP gateway configuration (How-To) 页眉；First time wizard 讲义与实验页
  source_quote: |
    "Communication Suite for SMB" (p66、p151 章头页眉；全书其余章节均为 MLE)
    "First user creation • Internal • Username: barkley@company.com" (p50)
    "First user creation o User's email address: baker@company.com" (p70)
  summary: |
    两处编辑残留提醒读者别照抄：①p66 与 p151 页眉写成 "Communication Suite for SMB"（其余均为
    MLE），是排版残留，不影响内容归属；②首用户邮箱讲义页（p50）写 barkley@company.com、实验页
    （p70）写 baker@company.com——两个都是生态示例里的真实账号（barkley=31600 用户、baker=传真
    管理员），做实验用哪个都能走通，但记录实验报告时要说明取的是哪页口径。
  conditions: 照书做实验/写交付文档时
  tags: [version-trap, documentation, lab]

- id: n25
  title: 支持矩阵里写 "Microsoft Outlook 2022"——版本号疑为原文笔误
  type: version-trap
  source_pages: p41
  source_chapter: Client Requirements
  source_quote: |
    "Supported Mail Clients • Microsoft Outlook 2022 / 2019 / 2016 (64-bit and 32-bit)" (p41)
  summary: |
    客户端要求页把 Outlook 版本写成 "2022 / 2019 / 2016"。Microsoft Office 桌面版没有 2022
    （2021 之后直接到 2024/365 路线）（（推断）版本常识推断，原书如此）。照抄该矩阵给客户出方案
    会写出不存在的产品版本；以 OTFC Features List 为准核实。
  conditions: 客户端环境规划与方案文档编写时
  tags: [version-trap, typo, requirements]

- id: n26
  title: 端口使用表在书内缺正文——p42 只有标题与截图引用
  type: out-of-scope
  source_pages: p42
  source_chapter: Ports in use
  source_quote: |
    "Ports in use" (p42，本提取文本中该页无任何端口数值内容)
  summary: |
    全书唯一的端口章节在提取文本中只剩标题，具体端口/协议清单外置 OTFC Features List。做防火墙
    白名单时不能从本书取数——已知数值仅：OTFC 本地 SIP UDP 5360（p142）、SMTP 网关监听 25
    （p183）、LDAP 明文 389（p196）。其余一律查 Features List。
  conditions: 防火墙策略、网络安全评审时
  tags: [out-of-scope, ports, firewall]

- id: n27
  title: 服务器资源推荐表同样只有指针——容量设计依赖 Features List
  type: out-of-scope
  source_pages: p38
  source_chapter: Recommended server resources
  source_quote: |
    "Important: Always refer to the OTFC features list for any update" (p38，正文无数值表格内容)
  summary: |
    "推荐服务器资源"一页在提取文本中只有"以 Features List 为准"的提示，无 CPU/内存/磁盘数值。
    售前 sizing 不能从本书出数，结合容量口径（15000 用户/30 端口，p7）与 Features List 资源页
    共同确定。
  conditions: 售前 sizing、硬件采购时
  tags: [out-of-scope, sizing, capacity]

- id: n28
  title: XMFaultTolerance 只出现在服务清单——故障切换怎么部署全书没教
  type: out-of-scope
  source_pages: p179, p180
  source_chapter: Services and Components / Fax Manager Module
  source_quote: |
    "Stateful (Replicated) Services/Components • ... • XMFaultTolerance" (p179)
    "XMFaultTolerance ; Monitors faults and supervises failover" (p180)
  summary: |
    服务清单里有 XMFaultTolerance（监控故障并监督 failover），架构上也讲了"有状态组件复制"，
    但高可用部署（第二台服务器怎么装、复制怎么配、切换怎么演练）全书零实操。客户合同带 HA 需求
    时，本书覆盖不了，要另找产品文档/专业服务（（推断）边界结论，原文未指路 HA 文档）。
  conditions: 高可用/容灾需求场景
  tags: [out-of-scope, ha, failover]

- id: n29
  title: OXE 侧互通只剩骨架：MGR 菜单序列 + TC3048 指针——照书做完话路未必通
  type: out-of-scope
  source_pages: p141, p147, p151-155
  source_chapter: OmniPCX Enterprise & OTFC / OmniPCX Enterprise configuration / OXE SIP gateway configuration (How-To)
  source_quote: |
    "To manage SIP connexion between the OTFC & OmniPCX Enterprise, you have to refer to the
    Technical Communication: • TC3048" (p141)
    "See the dedicated procedure following this presentation • And use the TC3048" (p147)
  summary: |
    OXE 侧七步只是菜单路径骨架，网关/中继的具体参数（编码、号码变换、中继属性）全书没给，官方
    明确指向 TC3048。交付 SIP 互通时手上必须有 TC3048；只拿本书上站，OXE 侧配完大概率还要回工
    （（推断）"大概率"为工程经验判断，原文只说 refer to TC3048）。
  conditions: OXE-OTFC SIP 互通交付时
  tags: [out-of-scope, oxe, tc3048, sip]

- id: n30
  title: OTP 直连网关可用但功能受限——官方强烈建议前置真实邮件服务器
  type: limitation
  source_pages: p157, p160
  source_chapter: SMTP integration（Overview / SMTP Gateway (Outbound)）
  source_quote: |
    "For security and queue performance when using OTFC: • It is highly recommended to connect the
    SMTP Gateway to a real mail server with which your Fax Server will benefit from many features
    that are dedicated to emails management." (p157)
    "Direct connection is possible between the user and the SMTP Gateway. However , inserting a
    mail server in front of the SMTP Gateway provides: •More flexible management and better
    performance of email queues ... •Better client-server integration (ex: Outlook forms) •Spam
    filtering •Virus checking" (p160)
  summary: |
    用户邮件可以直连 SMTP 网关发传真，但官方口径是"强烈建议"前面挂真实邮件服务器——直连模式下
    队列管理（挂起/转向/并发）、Outlook 表单集成、垃圾过滤、病毒检查四类能力全部缺失。最小闭环
    实验可用直连，生产方案按带邮件服务器拓扑设计。
  conditions: 邮件拓扑设计时
  tags: [limitation, smtp, topology]

- id: n31
  title: LDAP 断连不静默：直接产生 SNMP trap——监控侧要接住
  type: warning
  source_pages: p196
  source_chapter: LDAP Server (Default: Active Directory)
  source_quote: |
    "If the connection is lost between fax server and LDAP directory a SNMP trap is generated" (p196)
  summary: |
    传真服务器与 LDAP 目录的连接一旦丢失会自动产生 SNMP trap。反面含义：客户没部署 SNMP 网管时
    这个告警没人收，目录挂了只在"用户查不到/路由失败"时才被动发现（（推断）后半句为后果推断）。
    交付含目录集成的站点要顺带确认 SNMP 告警有落点。
  conditions: 目录集成 + 监控设计时
  tags: [warning, ldap, snmp, monitoring]

- id: n32
  title: SIP/TLS 在概览是卖点、在配置章只见 UDP 5360——加密话路启用路径缺失
  type: limitation
  source_pages: p7, p142
  source_chapter: What Is OTFC? / SIP configuration
  source_quote: |
    "Fully software-based • Fax over IP • SIP/TCP and SIP/TLS" (p7)
    "SIP configuration • Local SIP UDP port: 5360 ... • SIP authentication" (p142)
  summary: |
    概览页把 SIP/TCP 与 SIP/TLS 并列为传输能力，但配置章只出现"本地 SIP UDP 端口 5360"与 SIP
    认证，TLS 的证书、启用开关全书无一步。客户合规要求加密信令时，本书给不出落地路径，需查
    Features List 与产品安全文档（（推断）指路结论，原文未给）。
  conditions: 加密/合规要求场景
  tags: [limitation, sip, tls, security]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-24）与全书 Warning/Note 扫描

| task | 任务 | 反例类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 评估方案能力 | 有 | n03, n26, n27 | 许可边界、端口表缺正文、资源表缺数值 |
| task-02 | 规划部署架构 | 有 | n17, n30 | SMTP 独占 25、直连模式功能受限 |
| task-03 | 准备传真服务器宿主 | 有 | n01, n07 | 关防火墙仅实验口径、Office 预初始化 |
| task-04 | 安装 OTFC 软件 | 有 | n02, n05, n06 | 25 端口冲突顺序、语言副作用、临时密码 |
| task-05 | 跑 FTW | 有 | n24 | 首用户邮箱两页不一致 |
| task-06 | 处理许可 | 有 | n03, n04 | 水印/2 通道边界、MAC 绑定与手工导入 |
| task-07 | 创建与管理用户 | 有 | n08, n09 | 双目录共存误解、CSV 仅 Webadmin |
| task-08 | 创建管理员 | 有 | n06, n10 | 教材默认密码、备份管理员防锁死 |
| task-09 | 客户端 | 有 | n11 | 客户端装传真服务器仅实验口径 |
| task-10 | 定制封页 | 部分 | n05 | 封面语言受安装语言影响（副作用面） |
| task-11 | 设计 Profile | 有 | n12 | 通知格式只影响邮件 |
| task-12 | 管理电话簿 | 有 | n22 | 私人电话本不在系统备份内 |
| task-13 | OTFC 侧 SIP | 有 | n32 | SIP/TLS 提及但无启用路径 |
| task-14 | OXE 侧 SIP 网关 | 有 | n06, n29 | mtcl 默认账号、TC3048 外置 |
| task-15 | OXE 抓包 | — | — | p148-150 命令页无 Warning/Note 类内容（命令口径在 principle p31） |
| task-16 | 集成邮件系统 | 有 | n13, n14, n15, n16 | Outlook 模式依赖、许可特性、feedback address、Receive Connector |
| task-17 | 服务架构运维 | — | — | p177-191 无独立 Warning（日志默认值在 principle p35） |
| task-18 | 高级目录与路由 | 有 | n18, n19, n20, n31 | 无 Site/Profile 拒用、IIS 三前提、Default 恒最后、LDAP 断连 trap |
| task-19 | 计费 | — | — | p212-213 无 Warning/Note |
| task-20 | 备份与恢复 | 有 | n21, n22 | 冷备 not killed/恢复可 killed、电话本不覆盖 |
| task-21 | 升级 | 有 | n23 | 三大升级陷阱 |
| task-22 | 删除策略 | — | — | p223-224 无 Warning/Note（合规口径在 principle p43） |
| task-23 | 报表与监控 | — | — | p225-229 无独立 Warning（SNMP 清单在 principle p39） |
| task-24 | 日志排障 | 部分 | n16, n15, n18 | 通知类故障三大先查项；日志判据在 principle p41 |

**覆盖结论**：
1. 全书 Warning/Note/Important 逐页扫描完成——原书显式提示集中于准备/安装/SMTP/备份升级四章，已全部入册（n01-n23）；文档编辑残留与笔误 3 处（n24 SMB 页眉与首用户不一致、n25 Outlook 2022、n26/n27 缺正文页）单独成条。
2. n04/n10/n22/n29/n31/n32 含推断性结论，均已标"（推断）"。
3. 无反例内容的讲义型 task（15/17/19/22/23）已注明去向，无遗漏。
