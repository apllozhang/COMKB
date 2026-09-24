# 原则/清单/规则/公式/数值口径候选 — OpenTouch Message Center Starter (OTMCXTE200EN R2.6 Issue 08)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号、分机号）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: 规模口径：安装模式标注 15000 用户；话机 GUI 显示 5000 并发用户；扩容必须用专用容量规划工具
  type: metric
  source_pages: p18, p19, p62
  source_chapter: Architecture / Infrastructure / SUSE 安装模式
  source_quote: |
    "5000 simultaneous users with GUI display on series 8 sets, Premium Deskphones 80x8 and Smart DeskPhone
    8088" (p18)
    "Scalability must be managed using the OpenTouch Capacity Planning Tool dedicated for OTMC" (p19)
    "OpenTouch Messaging Center (15000 users) … OpenTouch Messaging Center for Virtualized Infrastructure
    (15000 users) … OpenTouch Messaging Center first (15000 users, single partition)" (p62)
  summary: |
    三条规模数字：三个安装模式均标 15000 users；话机 GUI（可视化信箱）并发显示上限 5000 用户（限 8 系/80x8/8088 话机）；扩容（压缩、站点占比、话务建模）必须用 OTMC 专用的 OpenTouch Capacity Planning Tool——p19 给出示例场景（压缩 2800/1200 用户、30% 远端站点强制压缩、远端 20% PSTN 中继），工具用法本身在书外。
  conditions: 15000 为安装模式标注口径；硬件与软件规格另见 feature list / product limits 文档
  tags: [metric, capacity, scale]

- id: p02
  title: DNS 硬性解析清单：前向+反向覆盖七类 FQDN
  type: checklist
  source_pages: p73
  source_chapter: Post-installation wizard / 1.3 Network settings（DNS Server Parameters）
  source_quote: |
    "THE DNS MUST BE CONFIGURED TO RESOLVE (FORWARD AND REVERSE RESOLUTION): • OTMC SERVER FQDN • OMNIVISTA
    8770 SERVER FDQN • MAIL SERVER FDQN • LDAP SERVER FDQN • ALCATEL-LUCENT OMNIPCX ENTERPRISE COMMUNICATION
    SERVER CALL SERVER: • NO REDUNDANCY: CALL SERVER FQDN • LOCAL REDUNDANCY: CALL SERVER MAIN ROLE FQDN •
    SPATIAL REDUNDANCY : EACH CALL SERVER FQDN • ALCATEL-LUCENT OMNIPCX ENTERPRISE COMMUNICATION SERVER H.323
    GATEWAY FQDN"
  summary: |
    上线检查清单：DNS 必须做前向+反向解析——OTMC FQDN、OmniVista 8770 FQDN、邮件服务器 FQDN、LDAP 服务器 FQDN、OXE 呼叫服务器 FQDN（按冗余模式三选一：无冗余=呼叫服务器 FQDN；本地冗余=main 角色 FQDN；空间冗余=每台呼叫服务器 FQDN）、OXE H.323 网关 FQDN。核查命令：nslookup 正查+反查（p92/p94 示例）。NTP 另有建议：防火墙放行 NTP 请求；虚机的 NTP 客户端自动同步宿主机 NTP（p73 Note）。
  conditions: 主机名与域名必须小写（p72）
  tags: [checklist, dns, network, prerequisite]

- id: p03
  title: Post-install 账户硬规则：五个账户、用户名禁用保留名、密码至少 8 字符且无报错弹窗
  type: rule
  source_pages: p75-76
  source_chapter: Post-installation wizard / 1.5 OTMC core settings
  source_quote: |
    "THE ACCOUNTS' USERNAMES MUST ALL BE DIFFERENT AND MUST NOT BE 'ADMIN', 'ADMINNMC', 'HTUSER' OR ANY OTHER
    EXISTING ACCOUNTS. ALL PASSWORDS ON THIS PAGE MUST CONTAIN AT LEAST 8 CHARACTERS. THERE IS NO ERROR POP-UP
    IN CASE YOU USE LESS THAN 8 CHARACTERS BUT YOU WILL FACE PROBLEMS AFTERWARDS. IT IS RECOMMENDED TO NOTE
    THE DIFFERENT USERNAMES AND PASSWORDS BECAUSE YOU WILL NEED THEM TO DECLARE OPEN TOUCH NODE IN OMNIVISTA
    8770 SERVER."
  summary: |
    五账户及实验口径示例值：root（letacla1234）、maintenance（用户名留默认，密码 maintenanceuser）、administrator（用户名留默认，密码 Admin-8770，8770 全权管理连接用）、profile（用户名留默认，密码 Admin-T1，模板管理用）、SNMP（认证/加密密码 adminsnmp；SNMP Engine ID 自动生成）。密码均 ≥8 字符——不足 8 位不会弹错但事后出问题。用户名互不相同且不得使用 admin/adminnmc/htuser 等既有账户名。账户口令必须记录，8770 声明 OTMC 节点时要用。
  conditions: 实验口径密码；生产必须替换；账户声明值与 /var/data/bics/bics.conf 对账（p92）
  tags: [rule, accounts, passwords, security]

- id: p04
  title: 根密码两段口径：SUSE 安装默认 letacla1 → 强制改为自定值；Post-install 再定义 root 新密码
  type: rule
  source_pages: p60, p63, p75
  source_chapter: OTMC installation How-To & Post-installation wizard
  source_quote: |
    "Login: root • Password: OtmcV01* (default password is: letacla1)" (p60)
    "Log on as 'root' using the default password 'letacla1'. You are prompted to change the 'root' password.
    Enter the new password twice: OtmcV01*" (p63)
    "Root password: letacla1234 … Enter the root password (8 characters minimum)" (p75)
  summary: |
    root 密码时间线：SUSE 阶段默认 letacla1 → 首登强制改（实验口径 OtmcV01*）→ post-install 向导 1.5 再填 root 密码（实验口径 letacla1234）。两处实验密码不同属实验剧本设定；生产口径是"默认密码仅在首登存在，随即替换"。
  conditions: 全部为实验口径；letacla1 为出厂默认
  tags: [rule, passwords, lab, security]

- id: p05
  title: 许可服务器绑定规则：虚拟环境 dongle 必须挂到承载 FlexLM 的虚机；向导 OK 只代表文件存在
  type: rule
  source_pages: p76-77, p42, p82
  source_chapter: Post-installation wizard / 1.6 Licenses Server settings & 手工装许可
  source_quote: |
    "Dongle has to be associated to the virtual machine hosting the Flexlm server: • Flexlm server virtual
    machine in case of external license server • OTMC virtual machine in case of embedded license server" (p76-77)
    "THE OK STATUS INDICATES THAT THE LOCAL FILE IS PRESENT. BUT THE CONTENT (VALIDITY) OF THE FILE IS NOT
    CONTROLLED. THE SAME IN CASE OF EXTERNAL LICENSE SERVER USE, THE CONNECTION TO THE LICENSE SERVER AND ITS
    CONFIGURATION IS NOT TESTED, JUST THE LOCAL PRESENCE OF THE FILE." (p77)
    "When a new license file is copied into $LICENSES_HOME directory, the FlexLM service must be restarted to
    load this new file (service flexlmd restart)" (p42)
  summary: |
    三条许可规则：①虚拟环境 dongle 绑定对象=承载 FlexLM 的虚机（外部 FlexLM→FlexLM 虚机；内嵌→OTMC 虚机），Aladdin USB 设备要在对应虚机设置里添加；②向导许可页 OK/外部许可服务器均只校验"本地文件存在"，不做有效性与连通性测试——有效性要靠 $FLEXLM_HOME 下 ./lmutil lmstat –a 核验；③拷入新 .ice 到 $LICENSES_HOME（/var/data/licenses）后必须 service flexlmd stop/start（或 restart）才加载。Skip 跳过装许可不中断安装，但 OTMC 在手工补装前不会正常工作（p77 Tips）。
  conditions: 手工拷录用 otuser 走 SFTP（p82）
  tags: [rule, licensing, flexlm, dongle]

- id: p06
  title: 备份存储选型规则：虚拟环境必须外置 NFS；本地备份仅课堂口径，官方建议 USB/NFS
  type: rule
  source_pages: p79
  source_chapter: Post-installation wizard / 1.8 Backup storage
  source_quote: |
    "LOCAL: internal and in the same directory as the backup one. USB: on a USB key. NFS: on a NFS drive you
    must specify on Local Storage field. … When OTMC installation is made on virtual environment, the backup
    directory must be configured on an external NFS partition. In this case, you will have to specify the
    NFS Host: IP address of the host machine providing the NFS drive / NFS Path" (p79)
    "Local backup has been selected for hands-on purposes. Local backup is not recommended. USB or NFS backup
    should be preferred."
  summary: |
    备份存储三选一（LOCAL/USB/NFS），落盘文件为 bics.conf（站点配置账本）。硬规则：虚拟化安装时备份目录必须配在外置 NFS 分区（要给 NFS Host 与 NFS Path）；课堂为省事选 LOCAL 属实验口径，官方明确不推荐。8770 侧 NFS server 部署按 TC2024（p246）。
  conditions: bics.conf 同时是 OTMC 声明对账来源（p92）
  tags: [rule, backup, nfs, virtualization]

- id: p07
  title: 网络安全 OFF 仅限课堂：官方明示增加话费盗打（toll fraud）与未授权使用风险
  type: rule
  source_pages: p78
  source_chapter: Post-installation wizard / 1.7 Certificate
  source_quote: |
    "For deployment in this classroom configuration, the server will use the generic certificate. … Network
    Security Off: Confirm Yes … BEWARE: THIS CHOICE IS NOT RECOMMENDED BY ALCATEL-LUCENT ENTERPRISE, AS IT
    IMPLIES INCREASED RISKS OF TOLL FRAUD, AND UNAUTHORIZED USE OF THE SERVICES OR FUNCTIONALITIES ON THE
    SYSTEM"
  summary: |
    证书与安全等级规则：课堂用预载通用证书 Trust List 并把 Network security 关掉（选 Yes）以简化部署；该选择官方明确不推荐——toll fraud（话费盗打）与未授权使用风险上升。生产部署必须按正式证书与安全等级执行（具体生产证书流程不在本书展开）。
  conditions: 实验口径；生产禁止照搬
  tags: [rule, security, certificate, toll-fraud]

- id: p08
  title: 节点编号公式：8770 中 OXE 的 Subnetwork-Node number = ABC 网络号 × 100 + OXE 节点号
  type: formula
  source_pages: p85, p87
  source_chapter: OXE declaration / 1.2 Node and network numbers & 2.3 Declaring the OmniPCX Enterprise
  source_quote: |
    "Configure/verify the OmniPCX Enterprise in order to be the node 101 (node 1 in the subnet 1)" (p85)
    "Subnetwork – Node number: Enter a numeric value equal to the ABC network*100 + OmniPCX Enterprise node
    number. Example: With an ABC network number = 1 and node number = 1, you must enter 101" (p87)
  summary: |
    编号公式：Subnetwork-Node number = ABC 网络号 × 100 + OXE 节点号（例：网络 1、节点 1 → 101）。OXE 侧核对法：siteid 命令或命令行提示符括号 (101)。子网号必须等于 OXE 的 ABC 网络号；OTMC 节点号自由但不得与任何 OXE 节点号重复（p94 实施示例 98 / p95 模板举例 99，两处口径见 counter-example n17）。
  conditions: OXE 侧节点/网络号在 mgr 或 OXE Webadmin 的 System/Review/Modify 配置（p85）
  tags: [formula, numbering, node, 8770]

- id: p09
  title: SIP 端口与传输口径：OTMC external gateway 5040/TCP；OXE SIP 5060；OXE PRS 2570；Subscribe 最小时长 600
  type: metric
  source_pages: p99, p103, p105, p106
  source_chapter: OTMC declaration & OXE SIP configuration for OTMC
  source_quote: |
    "Port: 2570 (OXE PRS port number) • SIP Port: 5060 (OXE SIP port)" (p99)
    "SIP external gateway: SIP port number: 5040" (p103)
    "Port number: 5040 • Transport type: TCP … Gateway type: ICE type" (p105)
    "SIP Subscribe Min Duration: Enter 600" (p106)
  summary: |
    端口数字表：OTMC 侧 SIP external gateway 端口 5040（传输 TCP，Gateway type=ICE type）；OXE 侧 SIP 端口 5060；OXE PRS 端口 2570；SIP Gateway 的 Subscribe Min Duration=600。trunk group 侧：类型 T2、Q931 变体 ABC-F、T2 Specification=SIP、SIP 虚拟接入数默认 2（可按需改）。
  conditions: 端口为教材给定配置口径；改动需两侧一致
  tags: [metric, sip, ports]

- id: p10
  title: 编解码与转接优化：G.729 压缩、多算法关、DPNSS 前缀（实验 D1234）、Routing Optimisation=Yes
  type: rule
  source_pages: p108
  source_chapter: OXE SIP configuration for OTMC / 3 General settings
  source_quote: |
    "Compression type: G 729 • Multi. Algorithms for Compression: False" (p108)
    "This prefix is used to optimize the transfers through trunk groups. … Routing Optimisation: Yes" (p108)
  summary: |
    全局三条：压缩算法选 G.729、多算法关闭；建 DPNSS 前缀条目（Translator/Prefix plan，实验 D1234）用于优化经中继组的转接；为让前缀生效必须把 Routing Optimisation 设为 Yes。
  conditions: 前缀值为实验口径
  tags: [rule, codec, dpssn-prefix, routing]

- id: p11
  title: 话机许可三族六类对照表（L173/174/176/177/316/317）与核查两法
  type: metric
  source_pages: p117-118
  source_chapter: Connection user's creation for OTMC / 4 License check
  source_quote: |
    "TDM • Analog → Z equipment: 'Analog users' for Z set (License 174) • 80x9 series → UA equipment:
    'Advanced reflexes users' for 8029 and 8039 (License 173) • 'Connection reflexes users' 4019 (License 316)
    IP • 80x8 series → switch equipment: 'Advanced IP users' for 8028, 8038 and 8068 (License 176) •
    'Connection IP users' for 4008 and 4018 (License 317) SIP • SEPLOS or SIP device → switch equipment:
    'SIP users' for SEPLOS/SIP devices (License 177)" (p117)
    "173 M Advanced Reflexes users = 1/ 10 … 317 M Connection IP users = 2/ 30" (p118)
  summary: |
    逐类转写（License 号 | 名称 | 话机）：174 | Analog users | Z 设备模拟话机；173 | Advanced reflexes users | 8029/8039（UA 设备）；316 | Connection reflexes users | 4019；176 | Advanced IP users | 8028/8038/8068（交换式设备）；317 | Connection IP users | 4008/4018；177 | SIP users | SEPLOS/SIP 设备。核查两法：①8770 配置工具 System/Software package 右键 Filter 勾选全部用户包看计数；②OXE 呼叫服务器 mtcl 登录跑 spadmin → Display active file，格式"已用/可用"（实验读数 1/10、1/10、1/15、4/15、1/30、2/30，实验口径）。
  conditions: spadmin 需 mtcl 账号登录呼叫服务器
  tags: [metric, licensing, devices, checklist]

- id: p12
  title: OTMC 账户-信箱规则：分机号对齐 OXE 用户；Licenses 三项（MyIC/Voice mail 必开，Messaging API 可选）；Voice mail 权必查
  type: rule
  source_pages: p134-136, p141, p190
  source_chapter: Voice mailbox configuration (How-To)
  source_quote: |
    "Directory number: Enter the same directory number you managed for the user declared on OXE. 31000 for
    Brad Barkley …" (p135)
    "MyIC Business Communications: To be enabled. Voice mail: To be enabled. Messaging API: Optional." (p135)
    "Check that the users have the 'Voice mail' right enabled. … Voice mail: Enabled" (p141)
  summary: |
    三条规则：①OTMC 账户 Contacts 页签的分机号必须与 OXE 侧用户分机号一致（31000/31001/31002，实验口径）——这是 OXE 用户与 OTMC 账户的唯一挂钩键（p136）；②账户 Licenses 页签 MyIC Business Communications 与 Voice mail 两项必须启用、Messaging API 可选；③既有用户逐个核查 Licenses 页签 Voice mail 已勾（p141），没有该权即信箱不可用——"用户有信箱但不能留言"先查这里。
  conditions: 账户创建含 Salutation/Login/姓/名 + TUI/GUI 密码（可选强制首改 TUI 密码）
  tags: [rule, accounts, mailbox, licensing]

- id: p13
  title: 信箱创建强规则：必须先挂 voice mail profile 才能保存；信箱类型与所属 VMS（defaultVmsLS）
  type: rule
  source_pages: p137-139
  source_chapter: Voice mailbox configuration / 2 Voice mailbox management
  source_quote: |
    "Check that the Local Storage voice mail is created in the system. If not, create it" (p137)
    "Before validating the mailbox creation, it's mandatory to assign a profile to the voice mailbox, in the
    « configuration » tab. So, choose one of the existing profiles" (p139)
  summary: |
    两条规则：①系统默认自带 Local Storage 型语音邮件系统 defaultVmLS（Services/Topology/VMS 核验，缺失则先建）；②信箱创建 General 页签（Display name 自由文本，示例 <username>VoiceMailBox；Type=Local Storage；Voice mail system=defaultVmsLS）之外，Configuration 页签必须选一个 profile 才允许保存——profile 是信箱的强制前置。建完再到 Users and devices/User 的 Mailboxes 页签把信箱挂给用户（搜索框搜 VMB 选定后 Apply）。
  conditions: 默认语音邮件系统基于 Local Storage 配置（p137）
  tags: [rule, mailbox, profile, vms]

- id: p14
  title: Voice mail profile 参数逐项表（Configuration 1/2/3 全参数与默认值）
  type: metric
  source_pages: p147-150
  source_chapter: Voice mailbox profiles / 1.2 Voice mail profile option
  source_quote: |
    "Answer only • Yes: callers cannot leave messages … • Manageable by users (default value)" (p148)
    "If enabled, the caller can decide to be routed to an attendant by dialing digit '0' while the greetings
    are played (also known as zero-out enabled)" (p149)
    "Max size per mailbox: Quota of the mailbox belonging to this profile in MB. Not taken into account if
    'check quota' is not activated … Aging of new messages: Lifetime of unheard messages in days" (p150)
  summary: |
    逐项转写（默认 profile：Advanced/Classic/Simplified 为 LS、Standard 为 UM）：Configuration 1（行为）——Answer only（Yes/No/Manageable by users 默认）、Check quota、Announce time received、Skip memo、Direct callback（开=按 2 直接回；关=按 2 再按 1 确认）、Callback voice prompt、Limited access（禁录问候语选项 4 与姓名等个人选项 5）、Extended absence greeting blocks message deposit、Record invitation（系统提示语"请留言后按#"）、Keep call in system（信箱满/answer only 时转信箱主菜单而非挂断）、Callback sender allowed、Propose options after message deposit（录后按 # → 1 确认/2 复听/3 重录/0 求助）、Play a beep tone when recording（默认）、Attendant call enabled（zero-out，问候播放中按 0 转话务台）。Configuration 2（时长/密码）——Maximum greeting、Max message recording、Max live record（秒）；TUI password management 三档（change allowed / allowed but forbidden when expired / forbidden；TUI 密码用于可视化信箱与 TUI 信箱菜单）。Configuration 3（容量/期限）——Max size per mailbox（MB，Check quota 关时不生效）、Aging of new/saved messages（天）、Warning（密码到期前提醒天数）、Accessible via network、Accessible via IMAP。
  conditions: 无信箱/无 profile 用户的 My Profile 中 TUI 密码管理回落为 "allowed but forbidden when expired"（p149-150）
  tags: [metric, profile, parameters]

- id: p15
  title: 实验口径：my_profile 新建参数（10MB/5s/15s/15s/15 天/7 天等）
  type: metric
  source_pages: p151
  source_chapter: Voice mailbox profiles / 2 New voice mailbox profile
  source_quote: |
    "Check quota enabled • Announce received date and time enabled • Direct callback enabled • Limited access
    enabled • Callback sender allowed enabled • Brief prompts for TUI enabled • Propose options after message
    deposit : true • Mailbox size: 10 Mb • Max greeting: 5 seconds • Max message recording: 15 seconds • Max
    live record: 15 seconds • Aging of new messages: 15 days • Aging of saved messages: 7 days" (p151)
  summary: |
    实验 my_profile（Local storage 型）全参数（实验口径）：行为开——Check quota、Announce received date and time、Direct callback、Limited access、Callback sender allowed、Brief prompts for TUI、Propose options after message deposit=true；容量期限——信箱 10MB、问候最长 5 秒、留言录制最长 15 秒、live record 最长 15 秒、新留言保留 15 天、已存留言保留 7 天。验收动作：用该 profile 信箱收几条留言并核对参数生效（p151）。
  conditions: 实验口径；生产值按客户策略
  tags: [metric, lab, profile]

- id: p16
  title: SMTP 服务器硬要求：外部、无认证、无 TLS；发送失败仅两处可见（退信 + 到达前失败转 SNMP trap）
  type: rule
  source_pages: p174
  source_chapter: SMTP/SMS notification / SMTP server
  source_quote: |
    "Notifications are sent through an external SMTP server. • There is no SMTP server in the OpenTouch
    solution. • This server must be used without authentication and without TLS. … An OpenTouch alarm is
    generated only when the operation of sending mail failed before reaching the SMTP server. • This alarm is
    then transformed in an SNMP trap for supervision."
  summary: |
    四条硬要求：①OTMC 方案内不含 SMTP 服务器，通知必须发外部 SMTP；②该服务器必须无认证、无 TLS（客户端对接时也要按此口径）；③必须在该服务器上准备一个有效邮箱账户（尽量专用）作为发件人；④送达回执不处理——投递失败只有两个可见信号：SMTP 非送达通知落到发件账户邮箱；只有"邮件根本没到达 SMTP 服务器"才触发 OpenTouch 告警并转 SNMP trap 供网管。给客户选 SMTP 时要确认能开"匿名+明文"端口（实验用 eco.company.com:25，实验口径）。
  conditions: 发件地址须在 SMTP 服务器上真实存在（p184）
  tags: [rule, smtp, notification, security]

- id: p17
  title: 通知功能可用性矩阵（LS vs UM）与管理员/用户权限矩阵
  type: metric
  source_pages: p180-182
  source_chapter: SMTP/SMS notification: summary
  source_quote: |
    "SMS notification V V / Email notification V V / .wav file attached V / Link to My Messaging web V /
    Call back the message sender V / Notification when voice mailbox is full V / Notification when voice
    mailbox is almost full V" (p180，行首功能、两列=Local storage/Unified Messaging)
    "Right for e-mail notification V / … E-mail address V V …" (p181，两列=Administrator/User)
  summary: |
    逐格转写可用性（LS/UM）：SMS 通知 = V/V；Email 通知 = V/V；wav 附件 = 仅 LS；My Messaging 链接 = 仅 LS；回呼留言主 = 仅 LS；信箱已满通知 = 仅 LS；近满通知 = 仅 LS。权限矩阵（管理员/用户）：邮件通知权（管/—）；用户能否自开关通知（管定）；开关通知（双）；用户能否改通知地址（管定）；通知邮箱地址（双）；满箱通知（管）；wav 附件（管）；wav 时是否关 MWI（管）；My Messaging 链接（管）；SMS 通知权（管/—）；SMS 开关（双）；通知手机类型（工作/个人/自由选择）（双）。配套规则：LS 专属参数对非 LS 用户照常显示可配但无实际作用（p190 Note，见 counter-example n11）。
  conditions: 阈值默认 80%（p184）
  tags: [metric, notification, matrix, licensing]

- id: p18
  title: 通知全局参数数值：wav 上限 2MB、近满阈值 80%、SMTP 端口 25、附件四种格式、SMS 网关地址格式
  type: metric
  source_pages: p184-185
  source_chapter: SMTP/SMS notifications How-To / 1.1 Notification settings & 1.2 SMTP server declaration
  source_quote: |
    "Maximum .wav file size (linear PCM 8bits): 2 MB • Occupancy ratio threshold (%): 80" (p184)
    "SMS gateway address: Enter the SMS gateway address, e.g. SMS$xxxxx$@company.com where 'xxxxx' will be
    the phone number where to notifiy the user" (p184)
    "Domain name: company.com • FQDN or IP: eco.company.com • Port: 25" (p184)
    "Audio file format: Select the audio file format amoung the following possibilities: AAC/.AAC, linear PCM
    16bits/.wav, linear PCM 8bits/.wav, G.711 PCM/.wav" (p184)
  summary: |
    数值口径：附件大小上限示例 2MB（超限发信不带附件；仅 LS 有效）；近满告警阈值默认 80%；SMTP 路由在 VPIM session 声明（域名 company.com、FQDN/IP=eco.company.com、端口默认 25，实验口径）；附件格式四选一（AAC、linear PCM 16bits wav、linear PCM 8bits wav、G.711 PCM wav）；SMS 网关地址格式 SMS$手机号$@域名，系统仅允许一个 SMS 网关（p177）；发件人名/地址示例 OpenTouch / administrator@company.com（地址须真实存在于 SMTP 服务器）。
  conditions: 实验口径；SMTP 服务器声明入口=System services/Applications/Messaging/VPIM（p185）
  tags: [metric, notification, smtp, sms]

- id: p19
  title: 通知模板规则：按语言存 /var/data/panda/notification4；升级不覆盖旧模板（要新模板须手删+重启 chameleon）
  type: rule
  source_pages: p173, p178, p185-186
  source_chapter: SMTP/SMS notifications / 1.3 Customization of notification messages
  source_quote: |
    "Template files for different languages are saved in $DATA_HOME/panda /notification4 directory
    ('/var/data/panda/notification4')." (p185)
    "When installing a new version, the templates of text for Email and SMS notification are not updated if a
    version already exists in order to keep the eventual customization done by the administrator. Therefore if
    you want to have the new templates … you have to delete the existing ones and restart the chameleon
    component." (p186)
  summary: |
    模板机制：邮件正文（新留言/满箱）与短信正文模板按语言存放在 /var/data/panda/notification4（文件名如 NotifTemplate_en_US.properties），可按语言定制；通知语言跟随用户 GUI 语言（p173/p178）。版本行为：升级安装时已存在的模板不被覆盖（保护管理员定制）——想拿新版模板（新翻译/文案变更）必须先删旧模板再重启 chameleon 组件，新版模板落地后再回填定制。排障抓手：service chameleond status、service scorpiod status；日志 /logs/chameleon/chameleon/panda.log、/logs/journal/chameleon.log、/logs/journal/scorpio.log（p192）。
  conditions: p173/p178 记目录为 /var/data/panda（p185 细化为 .../panda/notification4）
  tags: [rule, notification, templates, version]

- id: p20
  title: IMAP 对接口径：默认 IMAPS+TLS；改安全级须改端口并重启 imap4fed；OTMC 不当 SMTP 服务器
  type: rule
  source_pages: p205, p207-208
  source_chapter: Voice Messages retrieval through IMAP (How-To)
  source_quote: |
    "BY DEFAULT, IMAPS IS ENABLED ON OPENTOUCH SIDE WITH 'TLS' SECURITY. … IF YOU WANT TO ENABLE IMAP PROTOCOL
    WITH 'SSL' SECURITY OR IMAP PROCOTOL WITHOUT ANY SECURITY, YOU WILL HAVE TO MODIFY THE PORT NUMBER ON
    OPENTOUCH SIDE (AND TO MAKE SURE THAT CONFIGURATION MATCHES ON CLIENT SIDE). DON'T FORGET TO RESTART THE
    IMAP FRONT-END SERVICE: service imap4fed restart" (p208)
    "The 'send test e-mail message' test fails, if a SMTP server is not reachable or OpenTouch/OTMC FQDN is
    used as outgoing mail server (OpenTouch server/OTMC (local storage voice mail) does NOT act as a SMTP
    server)" (p207)
  summary: |
    四条规则：①OTMC 侧默认启用 IMAPS（TLS），IMAP 参数入口=System services/Topology/Physical servers/OT component/"IMAP4 Front End"，端口按安全类型自动带出；②客户端加密类型必须与服务端一致；③改用 SSL 或无加密必须在 OTMC 侧改端口号并 service imap4fed restart；④客户端账户配置——收件服务器=OTMC FQDN（例 otmc.company.com，实验口径），发件服务器不参与但建议填真实邮件服务器 FQDN 以免误报（p205），用户名/密码=GUI 凭证；验收判据="log onto incoming mail server (IMAP)" 测试 Completed，"send test e-mail" 失败属预期。
  conditions: 外网访问经 VPN（p198）；OTMC（LS 型）不提供 SMTP 服务
  tags: [rule, imap, tls, imap4fed]

- id: p21
  title: general announcement 硬限制与 wav 口径：单条/覆盖/≤5 分钟；文件名与格式固定；TUI 三菜单
  type: metric
  source_pages: p223, p225-227
  source_chapter: General announcement / Conclusion & How-To
  source_quote: |
    "Only one general announcement can be recorded at a time. • Any new recording will overwrite the previous
    one. • Max duration: 5 minutes" (p223)
    "The name must be 'general_announcement.wav' • Format: CCITT A-law 8bits 8kHz mono" (p223)
    "3 choices are available (one of the 4 existing choices is not more used: on AA). Several choices can be
    selected at a time." (p225)
  summary: |
    数值与规则：同时仅一条公告、新录覆盖旧录、最长 5 分钟、仅支持 wav 文件的语言可用；wav 方式须存到指定目录、改名 general_announcement.wav、格式 CCITT A-law 8bits 8kHz mono——文件就位即启用，停用=删文件或走 TUI。播报类型三选可多选（外呼落箱/内呼落箱/信箱查询；第 4 项"arrive on AA"已废弃——AA 曾内嵌 OT 服务器，外置 VAA 方案下无效果）；用户权（User has right to manage the general announcement）授权后可经 TUI 录制/试听/停用，留言录制或上传后自动激活。
  conditions: 存放路径两处口径不一（p223 /var/data/general_announcement vs p227 /var/data/ics-group/general_announcement），见 counter-example n18
  tags: [metric, general-announcement, limits]

- id: p22
  title: 备份恢复规则：恢复后必须手工起服务（opentouchd）；跨版本恢复勾 Force；备份保留期由 Scheduler 每日清理
  type: rule
  source_pages: p235-238, p240, p244-245
  source_chapter: OpenTouch Backup & Restore
  source_quote: |
    "Manager has to restart the OpenTouch services" (p235)
    "Use 'Force' option to restore to a higher release … required when the backup has been performed from an
    old release version of OpenTouch and the restoration must occur for this OpenTouch in a higher release
    version." (p244)
    "All backups saved on the server for a period exceeding the length of time specified in this field are
    deleted. This storage life time verification is performed daily by the Scheduler application." (p240)
    "Enter the command service opentouchd start in order to restart the OpenTouch services" (p245)
  summary: |
    五条规则：①恢复由 8770 自动完成"传包→停服务→恢复→清临时文件"，但起服务必须管理员手工做——SSH（维护账号，实验 otuser/maintenanceuser）→ su - 到 root（实验 superuser）→ service opentouchd start（重启 <5 分钟）；②备份期间停服务的命令为 service iced stop（p238）；③旧版本备份恢复到更高版本必须勾 Force；④8770 侧备份目录默认 C:\8770_ARC\OTBackup，阈值（可用空间或归档量，两级=次要/主要告警）与 Record Life（超期备份每日由 Scheduler 清理）在此配置；⑤备份/恢复凭据=OT 节点 Maintenance 页签的维护账号（例 otuser/superuser，实验口径）。
  conditions: 归档命名 <OT FQDN>.<YYYY-MM-DD-hh-mm>.zip；恢复测试删除用户须走 OT Configuration 窗口（见 counter-example n10）
  tags: [rule, backup, restore, services]

- id: p23
  title: 统计参数默认值与示例值对照（enableStatistics/mascd 等）
  type: metric
  source_pages: p256-258
  source_chapter: Voicemail statistics / How-To
  source_quote: |
    "enableStatistics = disabled … enableStatisticsGeneration = enabled … frequencyGeneration = day …
    dayGeneration = last day … timeGeneration = 22:00:00 … historicSize = 10 … freshness = P10DT0H0M0S …
    frequencyGC = after generation … dayGC = 0 … timeGC = 00:00:00" (p256)
    "enableStatistics = enabled … fileLocation = /var/data/ics-group/vms/statistics … dayGeneration = tuesday
    … timeGeneration = 15:35:00" (p257)
  summary: |
    逐参数默认值（p256）：enableStatistics=disabled；enableStatisticsGeneration=enabled；fileLocation=<streamRepository>/statistics；timeUnit=default（频率 day→hour，month/week→day）；frequencyGeneration=day；dayGeneration=last day（月内 0-31 或 last day，或 monday-sunday）；timeGeneration=22:00:00；historicSize=10（超限滚动删旧，0 永不删）；xsltDirectory=xslt；freshness=P10DT0H0M0S（删除数据保鲜期，ISO 8601 周期格式）；frequencyGC=after generation；dayGC=0；timeGC=00:00:00。实验示例（p257，实验口径）：启用统计与生成、输出到 /var/data/ics-group/vms/statistics、频率 day、dayGeneration=tuesday、时刻 15:35:00。操作规则：输出目录先手工建并检查读写权限；改完 statistics.properties 必须 service mascd stop/start。
  conditions: 配置文件位置 /var/data/ics-group/vms/ngvm3/statistics.properties
  tags: [metric, statistics, defaults]

- id: p24
  title: TUI 密码策略五参数（管理员可定义，默认值查 feature list）
  type: rule
  source_pages: p10, p123
  source_chapter: Features / Password protection & Password Policy
  source_quote: |
    "TUI password rules • Minimum TUI password size • TUI Password history length • TUI Password Validity
    Period • Maximum TUI logon failures • Locked period after Maximum logon failures reached • Those values
    are defined by the administrator. Refer to the feature list for the default values." (p10)
    "Force users to use strong password • Force users to change regularly their password • Lock accounts after
    a specified number of unsuccessful attempts" (p123)
  summary: |
    密码策略五个可配参数：最小密码长度、历史密码保留条数（不可重用窗口）、有效期、最大登录失败次数、达到失败上限后的锁定时长——均由管理员定义，默认值在 feature list（书外）。目的三句话：强密码、定期更换、超限锁定。TUI 密码用于 TUI 信箱与可视化信箱（VVM）访问（p149）；话机复活/注册用另一套 set secret code（默认 0000，p113/p116），两套密码不要混淆。
  conditions: 默认值不在本书内
  tags: [rule, passwords, tui, security]

- id: p25
  title: OTMC 安装登录与时刻口径：SUSE 安装约 25 分钟、软件部署约 30 分钟、服务重启 <5 分钟、Clock 用 UTC
  type: metric
  source_pages: p62, p68, p71, p245
  source_chapter: Installation & Post-installation wizard & Backup & Restore
  source_quote: |
    "Installation starts, it takes around 25 minutes" (p62)
    "Click on 'Next' to start the software packages deployment. This operation takes around 30mn." (p68)
    "Select the local time zone and select the option System clock uses UTC" (p62)
    "It takes less to 5 minutes for the OpenTouch services to restart." (p245)
  summary: |
    时长与时刻口径：SUSE 系统安装约 25 分钟；OT core 软件包部署约 30 分钟；恢复后 OpenTouch 服务重启 <5 分钟（验收别太早判失败）；SUSE 安装必须勾 System clock uses UTC（时区另选，示例 Europe/Paris）；post-install 主机设置勾 D.S.T.（夏令时）按当地情况。备份归档时间戳格式 YYYY-MM-DD-hh-mm（p233）、恢复目录示例 20141205153703（p244，YYYYMMDDhhmmss）。
  conditions: 时长为教材经验值
  tags: [metric, installation, timing]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 18 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 部署形态与容量口径决策 | 有 | p01 | 15000/5000 上限与容量工具口径；硬件规格书外（已注明） |
| task-02 | 实验拓扑搭建 | 部分 | p02 | DNS 解析清单（拓扑的隐形地基）；六虚机 IP 表为结构类（f07），账号密码散见 c00x 实验口径 |
| task-03 | 许可证体系部署 | 有 | p05 | dongle 绑定、OK 仅文件存在、flexlmd 重启、lmstat 核验 |
| task-04 | OTMC 服务器安装 | 有 | p04, p25 | root 密码两段口径、安装时长/UTC 口径；VM 规格见 f10 |
| task-05 | post-installation wizard | 有 | p02, p03, p04, p06, p07, p25 | DNS 清单、账户硬规则、备份存储、安全 OFF 警告 |
| task-06 | 手工装许可 | 有 | p05 | SFTP/flexlmd/lmstat 规则（f06 互补） |
| task-07 | OXE 声明进 8770 | 有 | p08, p09 | 节点编号公式、端口表 |
| task-08 | OTMC 声明与拓扑 | 有 | p08, p09 | 节点号自由但唯一、端口表（98/99 口径分歧见 n17） |
| task-09 | OXE SIP 对接 | 有 | p09, p10 | 端口/传输/Subscribe 数值、编解码与 DPNSS/路由优化 |
| task-10 | Connection 用户与话机 | 有 | p11 | 许可三族六类逐类表与核查两法；resurrection 密码 0000 见 c06/counter-example |
| task-11 | 账户与信箱交付 | 有 | p12, p13 | 分机号对齐、Licenses 三项、profile 强制前置 |
| task-12 | profile 定制 | 有 | p14, p15 | 参数逐项表 + my_profile 实验数值 |
| task-13 | 自助门户 | 有 | p12, p24 | TUI/GUI 密码两套口径支撑门户密码管理讲解 |
| task-14 | SMTP/SMS 通知 | 有 | p16, p17, p18, p19 | 服务器硬要求、双矩阵、数值口径、模板与版本规则 |
| task-15 | IMAP 访问 | 有 | p20 | IMAPS/TLS 默认、imap4fed、非 SMTP 声明 |
| task-16 | general announcement | 有 | p21, p25 | 硬限制/wav 格式/TUI 菜单、时长类口径 |
| task-17 | 备份恢复 | 有 | p22, p25 | 恢复后手工起服务、Force、保留期清理、时长口径 |
| task-18 | 语音信箱统计 | 有 | p23 | 默认值/示例值逐参数对照 + mascd 规则 |

**覆盖结论**：18/18 全部有原则/数值类条目覆盖（task-02 以 DNS 清单+结构条目 f07 组合覆盖，IP 全表属实验口径已在 f07/c0x 标注）。两点口径说明：
1. TUI 密码策略五参数（p24）的默认值原书明指 feature list（书外），本文件只收参数名与规则，不编造数值。
2. 所有实验给定值（letacla1/OtmcV01*/letacla1234/maintenanceuser/Admin-8770/Admin-T1/adminsnmp/1234/0000/31000-31002/D1234/eco.company.com:25/2MB/80% 等）已逐条标注"实验口径"，生产化必须替换。
