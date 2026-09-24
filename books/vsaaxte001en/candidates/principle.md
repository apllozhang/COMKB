# 原则/清单/规则/公式/数值口径候选 — Visual Automated Attendant (VSAAXTE001EN Ed20, R4.8.006)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号、token）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: 服务器规格三档与 120 端口上限
  type: metric
  source_pages: p52
  source_chapter: Server prerequisites
  source_quote: |
    "The maximum number of VAA ports supported is 120 • To go above this limit, please contact the central presales team
    Given as an example! Always consult the official documentation!
    up to 8 ports up to 50 ports up to 120 ports
    Processor Dual-core 2.4 GHz Quad-core 2.4 GHz Octo-core 2.4 GHz
    Memory 8 GB 16 GB 32 GB
    Network 100 Mb/s 1 Gb/s 1 Gb/s
    Hard Disk 80 GB 80 GB min 320 GB" (p52)
  summary: |
    逐格转写：≤8 端口——双核 2.4GHz / 8GB 内存 / 100Mb/s 网卡 / 80GB 硬盘；≤50 端口——四核 2.4GHz / 16GB / 1Gb/s / 80GB；≤120 端口——八核 2.4GHz / 32GB / 1Gb/s / 最低 320GB。VAA 最大支持 120 端口，超限联系中央售前。表中值原文两次标注"仅作示例，务必查官方文档"——售前引用时必须带这句边界。
  conditions: Suse-base Linux（p52 操作系统前提）
  tags: [metric, sizing, capacity]

- id: p02
  title: 虚拟化兼容三前提
  type: checklist
  source_pages: p53
  source_chapter: Virtualized environment
  source_quote: |
    "VMware ESXi 8.0 • Network adapter for the VM must be VMXNet3 • VMWare Tools must be installed
    Microsoft Hyper-V 2022 • VM type recommended is Generation 2
    KVM hypervisor Proxmox 8.2 • Network adapter for the VM must be VMXNet3
    (1) KVM hypervisor Proxmox supported from VAA 4.6.1" (p53)
  summary: |
    上线前核查清单：ESXi 8.0——虚机网卡必须 VMXNet3 + 必须装 VMware Tools；Hyper-V 2022——推荐 Generation 2 虚机；Proxmox 8.2（KVM）——VAA 4.6.1 起支持 + 网卡必须 VMXNet3。部署细节以 VAA Installation Manual 为准。
  conditions: 表格为示例口径（原文同页有免责声明）
  tags: [checklist, virtualization, prerequisites]

- id: p03
  title: 密码策略体系（五层：系统 root/admin、GRUB、Web 账户、S.O.T、锁定与有效期）
  type: metric
  source_pages: p78, p92-94, p275-276
  source_chapter: S.O.T summary / Install the VAA application / Password policy
  source_quote: |
    "admin password: « admin » account password. The password must contain 20 characters with 1 uppercase, 1 numerical character and 1 special characters. - Root password : … 20 characters…" (p78)
    "Create this new password (20 characters mini) for root account: InternationalSuperuser1234*" (p92)
    "Create this new password (12 characters mini) for admin account: Superuser1234*" (p94)
    "Set the following password to secure access to GRUB. This secures access to the BIOS with a password (minimum 14 characters)" (p93)
    "The password must contain at least 12 characters •1 lowercase letter •1 uppercase letter •1 number •and 1 special character from the following list: !\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~" (p275)
    "Account locked after 5 attempts … For an administrator account, the block lasts for 2 hours before being automatically unlocked. •The following command unlocks all locked administrator accounts: 'sudo vaa conf unlockAdmin'." (p275)
    "The default password validity is 92 days. •A warning e-mail is sent 30 days, 7 days and 1 day before expiration" (p276)
  summary: |
    五层数值：①S.O.T 部署的 admin/root 密码——20 位、含 1 大写/1 数字/1 特殊字符；②手工安装的 root 密码——最少 20 位（实验值 InternationalSuperuser1234*），admin 密码——最少 12 位（实验值 Superuser1234*）；③GRUB/BIOS 口令——最少 14 位（实验值 Generalconfig1!，原书两处大小写不一致见 counter-example）；④Web 界面密码——≥12 位且含小写、大写、数字、特殊字符各 1（特殊字符列表见引文），首次登录强制改密；⑤锁定与有效期——5 次失败锁定，管理员锁 2 小时自动解锁（sudo vaa conf unlockAdmin 可全解），管理员账号可由其他管理员在对应页签解锁；默认有效期 92 天，到期前 30/7/1 天发提醒邮件，导航栏出现提醒图标；参数在 Admin menu/Settings/Security parameters 可改。
  conditions: 4.6.104 起密码过期默认启用（p295）；实验值全部为实验口径
  tags: [metric, security, password]

- id: p04
  title: 默认账号与首改密码规则（web admin/admin、系统 letacla1、新建管理员默认密码=用户名）
  type: rule
  source_pages: p22, p80, p114, p128, p291
  source_chapter: WEBADMIN / MANUAL INSTALLATION / Testing the connection / WebAdmin application
  source_quote: |
    "Login: admin - Password: admin … The password for the admin account must be changed on 1st connection." (p22)
    "Use Root account • Login : root • Password : letacla1 • Default password must be changed … Login : admin • Password : letacla1" (p80)
    "BY DEFAULT THE PASSWORD OF THE NEW ACCOUNT IS IDENTICAL TO THE IDENTIFIER OF THE LATEST." (p128)
    "vaa db userreset Remove all users from the database (Reset superadmin account to default admin/admin)" (p291)
  summary: |
    四条规则：①Web 管理默认 admin/admin，首次登录强制改密（实验改为 Superuser1234*）；②操作系统层 root 与 admin 出厂口令都是 letacla1，首登必改；③Web 端新建管理员账号的默认密码=其用户名（原书 Warning 大写强调）——建完必须立即改密，否则是全系统最弱入口；④vaa db userreset 会把超管重置回 admin/admin（应急手段也是风险项）。
  conditions: 全版本通用
  tags: [rule, security, default-credentials]

- id: p05
  title: root 禁止 SSH 远程登录，一切特权操作走 admin + sudo
  type: rule
  source_pages: p55, p81, p92, p98
  source_chapter: TCP/UDP port usages / VAA DISTRIBUTION INSTALLATION / install.sh
  source_quote: |
    "The remote SSH access for the ROOT account is forbidden. You must use the admin account with the function 'sudo'." (p55)
    "You must be connected as root to perform the installation: •sudo su * … * SSH remote access is forbidden for the root account, you must be connected as superuser to perform the installation: sudo su" (p81)
  summary: |
    规则：root 只能本地控制台（Console mode）登录；远程一律 SSH admin 账号 + sudo su 提权。适用场景：装 VAA（unzip/install.sh）、vaa 命令族、证书操作、HA 命令。排障时发现"root SSH 连不上"是设计而非故障。
  conditions: CIS-2 安全基线的一部分（p20 产品定位）
  tags: [rule, security, ssh]

- id: p06
  title: VAA 4.8.006 只支持"全新安装 + 数据库恢复"，且强制新许可 Release 11
  type: rule
  source_pages: p78, p80, p89, p308
  source_chapter: S.O.T summary / MANUAL INSTALLATION / Install the VAA application / UPDATE A VAA VERSION
  source_quote: |
    "For VAA version 4.8.006, only an installation from scratch followed by a database restore is supported." (p78, p80)
    "Important information to read carefully before installing VAA 4.8.006: • Only a fresh installation followed by a database restoration is supported. • A new license (Release 11) is required." (p89)
  summary: |
    版本规则：4.8.006 不支持原地升级安装，唯一路径是全新安装后恢复数据库备份（vaa db restore / vaa full restore）；许可必须是 Release 11 新许可——旧许可直接失效。规划迁移/升级项目时按"重装 + 恢复"排工期，而不是按"原地升级"。
  conditions: 新版本可能放宽，以当时官方说明为准
  tags: [rule, installation, licensing, version]

- id: p07
  title: 许可文件绑定 MAC/FQDN；目录路径与核查方法
  type: rule
  source_pages: p249, p273-274, p95
  source_chapter: Install HA / CHECK LICENSES / Transfer of distribution files
  source_quote: |
    "The FQDN will be used in the license file • In case of problem, check the license file in the directory •/var/lib/ale/aa-license-server/" (p249)
    "The license file (.lic or .vaa) is linked to the MAC address of the VAA
    Installation directory •/etc/ale/aa-license-server
    In case of problem, check the license file in the directory •/var/lib/ale/aa-license-server/
    You must find: • The FQDN • MAC address" (p274)
    "The installation file is provided as a ZIP file. This file, along with the license file (.vaa), must be uploaded to the VAA server" (p95)
  summary: |
    许可三规则：①许可文件（.lic 或 .vaa）绑定 VAA 的 MAC 地址，且要含正确 FQDN——换网卡/改主机名都会失效；②安装目录 /etc/ale/aa-license-server，排障目录 /var/lib/ale/aa-license-server/，打开文件应能找到 FQDN 与 MAC；③安装时许可与发行包分开传：许可进 /tmp（install.sh 自动识别 .vaa 扩展名），发行包 zip 进 /home/admin。许可内容用 more 查看：FEATURE 项含 AAIVR（IVR 功能）、AAPORTS（端口数）、ECCSTART、VAA_RELEASE（许可版本，实验 9/11），均带到期日。
  conditions: 实验许可为 5 端口（VAA_PORTS [5]，p253）
  tags: [rule, licensing, troubleshooting]

- id: p08
  title: install.sh 交互参数清单（双侧契约）
  type: checklist
  source_pages: p81, p99-103, p251
  source_chapter: VAA installation / install.sh
  source_quote: |
    "Launch the installation script: ./install.sh … ­ OXE CS main and standby IP address: 192.168.1.3 ­ … Incoming username of your Pbx external gateway: vaa1 (no password) ­ Algorithms: G711a and G729 ­ Proxy http: no ­ Mail server: 10.20.30.11 ­ SIP TLS activation: no ­ No postgresSQL password ­ Daily backup in: /var/backup/vaa.tar ­ Remote syslog server: N ­ License file : license1.vaa" (p99, 实验口径)
    "If you don't have a standby, use the Main Pbx IP again" (p101)
    "The parameter 'incoming username' must be defined in the SIP external gateway, you must define the same username! - Username: vaa1 - No Password, leave blank - The parameter 'Minimal authentication method' must be set at - None" (p101)
  summary: |
    install.sh 参数清单（按交互顺序）：①本地 IP 确认（答 y，除非不是预期地址）；②HTTPS 证书（/tmp 已放选"已复制"，否则"稍后提供"→生成自签；证书在 /etc/nginx/certificate/certif_nginx.crt + nginx.key）；③OXE 主 IP 与备 IP（无备用就再填主 IP）；④incoming username（无密码留空）——必须与 OXE 外部网关完全一致，网关侧最小认证方式 None；⑤编解码（空格键勾选；要用语音识别必须 G711，选 G729 会与 ASR 冲突；不确定就 G711a+G711mu+G729 全勾）；⑥HTTP 代理（实验 N）；⑦管理员邮件通知（SMTP 主机/端口 25/协议 plain/认证空/发件与收件地址，可后补到管理界面）；⑧转移禁拨前缀 forbiddenTransferPrefix（逗号分隔，防呼叫者借 VAA 外呼或转到不该转的服务；不确定就填该 PBX 的外拨前缀；实验留空）；⑨数据库自动备份（文件名 .tar 或推荐的 .sql.gz；Daily 午夜/Weekly 周日/Monthly 每月首日/自定义 cron）；⑩SIP TLS/SRTP（激活需 OXE 与 VAA 双方有效证书；实验 N）；⑪PostgreSQL 密码（实验 Superuser1234*）；⑫远程 syslog（实验 N）；⑬许可文件（/tmp 的 .vaa 自动发现）。装完跑 vaa status 核对服务，浏览器 https://<VAA IP> 验收。事后改安装参数用 vaa conf telephony（改 OXE IP 与 incoming username/password）。
  conditions: 全部数值为实验口径；生产先备证书、许可、SMTP
  tags: [checklist, installation, install-sh]

- id: p09
  title: 编解码与语音识别互斥规则（G729 vs ASR）
  type: rule
  source_pages: p42, p101, p113
  source_chapter: High level software architecture / install.sh codec step / Compression algorithm
  source_quote: |
    "Note: G729 can't be used with Automatic Speech Recognition feature" (p42)
    "Do not use G729 if you want to use speech recognition
    If you are unsure about this setting, select G711a, G711mu and G729
    If you intend to use Speech Recognition, you must use a G711 codec. Accepting other codecs will cause issue with speech recognition." (p101)
    "Compression algorithm G729 is needed on the OXE side to match the configuration made during the installation on the VAA side. From OXE N2, compression algorithm G729 is enabled by default. It has replaced the G723 one which is phase-out." (p113)
  summary: |
    三条规则：①VAA 侧勾了 G729 就不能用 ASR——要用语音识别，编解码必须用 G711（接受其他编解码会导致识别故障）；②不确定时选 G711a+G711mu+G729 全勾（不用 ASR 的场景）；③OXE 侧编解码要与 VAA 侧安装配置匹配（OXE N2 起 G729 默认启用、G723 已淘汰，通常无需动 OXE）。呼叫建立异常时的快速止血：检查 OXE 设置或禁用压缩（p114 Tips）。
  conditions: ASR 引擎为 Google ASR（需 API key）
  tags: [rule, codec, asr]

- id: p10
  title: incoming username 双侧一致契约与 S.O.T 差异
  type: rule
  source_pages: p101, p109, p110, p260
  source_chapter: install.sh / SIP External Gateways / Tips
  source_quote: |
    "Incoming username Enter the same name as the one used in the VAA installation procedure: vaa1 - Incoming Password Leave blank - Minimal authentication method 'None' - Gateway type VAA type" (p109)
    "If the VAA is installed by the S.O.T tool, the parameter 'incoming username' will be set at 'vaa' in the VAA configuration file. The optional parameter 'incoming password' stays empty." (p110)
  summary: |
    契约规则：OXE 外部 SIP 网关的 incoming username 必须与 VAA 安装时定义的完全一致（实验 vaa1/vaa2），密码留空、最小认证方式 None、网关类型选 VAA。S.O.T 安装的 VAA 固定用 "vaa"。排障口诀：接不通先对这一对字符串。修改工具：vaa conf telephony。
  conditions: SIP TLS 激活时另有证书要求
  tags: [rule, sip, gateway, troubleshooting]

- id: p11
  title: 路由号码绑定规则——推荐一号一树，通配符"可用但不推荐"
  type: rule
  source_pages: p28-29, p111
  source_chapter: ROUTING NUMBERS / SPECIFIC CASE
  source_quote: |
    "The routing of the numbers is to be done on the OXE side (Routing or ARS)" (p28)
    "Possible use but not recommended (See chapter 4.3 Disambiguation about routing expressions in the Administration guide) • ?: to match any number • *: to match any number of digits • [firstNumber]-[lastNumber]: Assign a range of numbers to a tree structure - Recommended use for better readability • Assign a single number to each tree" (p29)
  summary: |
    规则两层：①双层路由缺一不可——VAA 内 Routing 菜单把 DID 绑到树（单号对单树，需点图标激活），OXE 侧还要把呼叫送到 VAA（routing 或 ARS）；②绑定表达式推荐"一号一树"（可读性好）；通配符 ?（任意一位）、*（任意多位）、[首]-[尾]（号段）可用但不推荐，语义细节在 Administration Guide 4.3。OXE 侧前缀计划示例：前缀 314、网络 10、trunk group 10、5 位（p111）。
  conditions: 号码须落在公司 DID 段内
  tags: [rule, routing, numbering]

- id: p12
  title: 破坏性操作规则——OXE 电话簿同步清空目录、CSV 导入清空过滤器
  type: rule
  source_pages: p32-33
  source_chapter: FILTERS / DIRECTORY
  source_quote: |
    "A filter can be created by importing a CSV file or entering an expression • A CSV import deletes all created entries" (p32)
    "Directory management •Manual creation •OXE phonebook synchronization - An OXE synchronization deletes all created entries" (p33)
  summary: |
    两条破坏性规则：①过滤器（Filter）用 CSV 导入会删除已创建的全部条目——只能全量重建；②目录（Directory）做 OXE 电话簿同步同样删除全部手工条目。执行同步/导入前先导出备份；混用"手工 + 同步"的运维模型注定丢数据。
  conditions: 全版本通用
  tags: [rule, directory, filters, destructive]

- id: p13
  title: 提示音资产规范——WAV 格式、命名、语音一致性、双语同文件
  type: checklist
  source_pages: p34, p138, p188
  source_chapter: PROMPTS MANAGEMENT / Manage prompts / Use case 3
  source_quote: |
    "Format: 8KHz PCM 16-bits mono" (p34)
    "Wav files uploaded to prompts should have the format: 8 KHz, PCM 16 bits mono. … No space in the name … It is recommended to use the same voice for all prompts: If TTS prompts are used, transcribe any WAV in TTS prompts for a harmony of the voices on the VAA" (p138)
    "The Welcome prompt must be recorded in both languages in the same WAV file, because the choice of languages is only made after its broadcast." (p188)
  summary: |
    四条规范：①WAV 格式硬约束 8KHz / PCM 16-bit / 单声道；②提示音名称不能含空格；③同一 VAA 的提示音应统一声音——用 TTS 时把存量 WAV 全部转成 TTS 生成，保持音色和谐；④多语言树的"语言选择前的提示"（欢迎语、语言选择菜单语）必须把两种语言录在同一个 WAV 文件里（或 TTS 串联两条），因为语言选择发生在播报之后。
  conditions: 树内 Announcement 另有 Server file 模式（放服务器本地音频文件），原文标注 not recommended
  tags: [checklist, prompts, tts, multilanguage]

- id: p14
  title: TTS/ASR 引擎选型与成本规则
  type: rule
  source_pages: p34, p36-37, p141
  source_chapter: PROMPTS MANAGEMENT / TTS / ASR
  source_quote: |
    "Free TTS engine embedded - PicoTTS (DE, GB, US, FR, ES, IT) •Paid (Licenses not provided by ALE) based on the number of characters •Google Cloud TTS" (p34)
    "Google speech to text service (Google Cloud account required) & API key required" (p37)
    "The Pico TTS engine can be used free of charge and without an internet connection. But it is not recommended for production. - Google Cloud is recommended but NOT free (credit card required)" (p141)
    "The information presented in this documentation may be inaccurate or out of date, as these prices and features may be updated at any time by the Cloud Text to Speech vendor" (p141)
  summary: |
    选型规则：①PicoTTS 免费且离线可用（六语言：DE/GB/US/FR/ES/IT），官方明确"不建议用于生产"（音质口径）；②Google Cloud TTS 是生产推荐但收费（按字符计费、需信用卡、许可不经 ALE）；③ASR 用 Google speech-to-text，需 Google Cloud 账号 + API key；④引擎价格的时效性由云厂商决定，教材自注信息可能过时——报价前查官方文档（Administration Guide 第 10 章 Text to Speech）。
  conditions: 引擎在公司设置（Tenant/Settings）激活
  tags: [rule, tts, asr, cost]

- id: p15
  title: 树设计纪律——每个节点必须命名、逐节点连线、依赖物先行
  type: principle
  source_pages: p145, p165, p175, p187
  source_chapter: FEATURES LIST / Use case 1/2/3 Implementation
  source_quote: |
    "It is IMPERATIVE to personalize the NAME of each block when configuring a tree! This name is used by statistics and will facilitate the analysis" (p145)
    "For each node created, establish the connector with the previous one - The name of the nodes is essential for understanding the statistics" (p165, p175, p187 三处重复)
    "The calendar, schedules and the filter must be created before the creation of the tree" (p175)
    "All prompts must be created before the tree creation" (p187)
  summary: |
    三条纪律：①每个节点的名称必须个性化——名称直接进统计报表（呼叫日志逐节点记录），随手默认名等于放弃排障能力；②每个节点建完立即与前一个节点连线（画布纪律，三个用例重复三遍）；③依赖物先行——日历/营业时间/过滤器（UC2）与全部提示音（UC3）必须在建树之前建好。
  conditions: 全版本通用
  tags: [principle, tree-design, statistics]

- id: p16
  title: 菜单节点参数与异常路径全景
  type: metric
  source_pages: p152-155
  source_chapter: MENU NODE 1/4 - 4/4
  source_quote: |
    "Number of retries: Number of attempts to enter a valid menu option • Timeout: The number of seconds given for an input • Repeat digit: Select the digit to dial to repeat the message • Max repeat: Maximum number of repeats" (p152)
    "Wait Time (s):Time in seconds the VAA will wait for the called number to answer … Bypass forward: For supervised transfer only." (p153)
    "Quota (s): how many seconds of audio data to be sent to the speech recognition engine (for cost control)" (p154)
  summary: |
    菜单节点参数清单：提示音（菜单指引 + 错误选项提示）、重试次数、输入超时秒数、重复播放键、最大重复次数、直拨分机开关、盲转/监督转选择、监督转保持音、号码过滤（命中走黄色连线）、多过滤模式、反向过滤（未命中过滤器的号码走 Filtered 连线）、监督转应答等待秒数、Bypass forward（仅监督转）。ASR 两档：菜单选择档（词/句映射数字，Full match 全匹配开关，Quota 秒数控成本）与"菜单+直拨"档（先匹配菜单词句、再查 VAA 目录姓名）。异常连线五类：Failed（默认）/No answer/Busy/Network error/Wrong number；Exception（用户无输入）。实验参考值（UC3）：重试 2、超时 4s、重复键 *、最大重复 2（p197）。
  conditions: 菜单最多 12 选项（0-9、#、*）
  tags: [metric, menu-node, parameters]

- id: p17
  title: 转接节点与 Bypass forward 机制（SIP 头证据）
  type: rule
  source_pages: p156-157
  source_chapter: TRANSFER NODE / Bypass forward activation
  source_quote: |
    "Transfer Destination • Phone Number: Enter the phone number of the person to join • Directory Assistance: A menu will help the user enter the name of the user he wants to join • Transfer strategy • Supervised • Blind transfer" (p156)
    "An information is sent in the SIP frame to indicate to the call handling of the OXE that it must ignore the forward and ring the destination phone even if a forward is active." (p157)
    "P-Alcatel-CSBU: bypass=on" (p157 SIP 抓包)
  summary: |
    转接节点规则：目的地两种——电话号码或目录辅助（按姓名拨号，可配 ASR 读名、重试次数）；策略两种——监督转（可感知忙/无应答，保持音 + Wait time）与盲转。Bypass forward 仅对监督转生效：开启后在 SIP INVITE 里带 P-Alcatel-CSBU: bypass=on 头，指示 OXE 忽略目的地已设的呼转、直接振铃目标话机。
  conditions: 需 OXE 侧配合解析该私有头
  tags: [rule, transfer, sip, bypass]

- id: p18
  title: 变量三类与使用约束
  type: rule
  source_pages: p216
  source_chapter: IVR node - Variables / Implementation
  source_quote: |
    "Variables could be: ­ Local: The variable is created when the script (tree) is launched and is only visible by the VAA line that uses it ­ Global: the variable is created at company level and is visible by all scripts (trees) used in the company … ­ Contextual: a context variable is a variable linked to the current call. These variables are predefined and cannot be modified." (p216)
  summary: |
    三类：Local——脚本启动时创建，仅本 VAA 线可见；Global——公司级，该公司所有树可见（适合做"不改脚本、改参数"的通用配置）；Contextual——与当前呼叫绑定的预定义变量（如 callingNumber），只读不可改，清单在管理指南。变量是 SQL/HTTP/收号/TTS 四类节点的必需品；全局与上下文变量可在公司设置页查看。
  conditions: 上下文变量清单以 Administration Guide 为准
  tags: [rule, variables, ivr]

- id: p19
  title: 收号节点行为细则（min=max 判失败、* 合法、# 结束不可改）
  type: rule
  source_pages: p205, p222-223
  source_chapter: COLLECT DIGIT NODE / How-To tests
  source_quote: |
    "Digits number: Maximum length of the input • Min count of digits: Minimum length of the input • # required to end digits record: If enabled, the 'Digits Number' is ignored replacing by ending recording using the # button" (p205)
    "Entering 4 digits - In our example, the minimum number of digits = maximum of digits, so this is an entry failure
    Enter * - * is considered as a correct entry
    Enter 1234# - # is the default character to finish the input - Impossible to modify" (p223)
  summary: |
    行为细则：①最小位数=最大位数时，输入位数不足即判失败；②单独输入 * 被视为一次"正确输入"（不是错误）——设计校验逻辑时要想到；③# 默认是结束输入符且不可修改（启用 # 结束时忽略最大位数）；④相邻数字间超时（Digits timeout）与重复提示超时（Timeout）分别可配；结果必须存入变量。实验参数：收 5 位、数字间隔 4s、总输入上限 20s。
  conditions: 参数名以 p205 清单为准
  tags: [rule, collect-digit, ivr]

- id: p20
  title: 显示名节点边界——仅监督转接、仅振铃期、需 OXE COS
  type: rule
  source_pages: p204, p225, p228
  source_chapter: CUSTOM DISPLAY NAME NODE / How-To Display name
  source_quote: |
    "To define the name displayed on the device that will receive the transferred call • Only on a supervised transfer and during the call ringing" (p204)
    "This feature is only available for supervised transfers" (p225)
    "When you go off hook, this information disappears and that the caller information is displayed: ­ Caller number if available for external call ­ Name / first name if local call" (p228)
  summary: |
    三条边界：①只对监督转接生效（盲转不行）；②只在振铃期显示——被叫摘机即消失、恢复显示正常主叫信息（外部显示号码、内部显示姓名）；③实验中还需在 OXE 侧管理话机特性 COS（p225 "Manage the Phone feature COS"）。进阶：显示文本可用变量动态生成。
  conditions: SIP 证据：INVITE 的 From 头显示自定义名（p228 抓包）
  tags: [rule, display-name, transfer]

- id: p21
  title: SQL 节点五条硬规则（单字段/首条结果/空结果非错误/性能/安全）
  type: rule
  source_pages: p207-208, p323
  source_chapter: SQL REQUEST NODE / external database How-To
  source_quote: |
    "Using too many database queries and SQL procedures in a script can delay the overall call duration - For security reasons, it is recommended to use a database defined in the company settings. - Do not use manual configuration • Most used value: SELECT (One field per line)" (p207)
    "<rowNumber>: Row index (starting at 1, up to a maximum of 200)." (p208)
    "An empty result does not generate an SQL error … The VAA can only recover one field at a time. To retrieve several fields, you have to make as many requests as there are fields. In case of multiple results, the VAA returns the first occurrence only." (p323)
  summary: |
    五条硬规则：①一次只取一个字段——要多字段就发多条请求（实验进阶题即"查 VIP 与转接号要 2 条 SQL"）；②多条结果只取第一条；③空结果不产生 SQL 错误——必须用 Condition 节点判"非空"再转接，SQL 失败走红色连线；④脚本里塞太多查询/存储过程会拖长整体呼叫时长；⑤安全上库连接应定义在公司设置（External Databases 页签），不要在节点里手工配置。多行多列模式自动存变量 <名>.<行号>.<列名>，行号 1 起最多 200。
  conditions: 实验查询 SELECT transfertNumber FROM customers WHERE callingNumber='VAR(callingNumber)'
  tags: [rule, sql, database, ivr]

- id: p22
  title: JDBC 驱动安装规则（默认两种、目录限制、HA 双机）
  type: checklist
  source_pages: p320, p325
  source_chapter: Preamble: jdbc pilot installation / Oracle appendix
  source_quote: |
    "By default, only the org.postgresql.Driver and org.mariadb.jdbc.Driver drivers are available and integrated with the VAA. Specific jdbc drivers (MS SQL, Oracle ...) must be downloaded or provided by customer's SGBD administrators. Generic jdbc drivers may be compatible, but it is still recommended to rely on the official versions of the manufacturers." (p320)
    "sudo mv /home/admin/mssql-jdbc-9.4.1.jre8.jar /opt/ale/aa-webapp/lib • It is not possible to make a sftp directly in the directory /opt/ale/aa-webapp/lib … sudo systemctl restart aa-webapp … Note: in HA mode, the driver must also be on the slave VAA." (p320)
    "These 2 connection strings are not equivalent and it is possible that only one will work." (p325)
  summary: |
    安装清单：①默认只内置 PostgreSQL 与 MariaDB 驱动；②MS SQL/Oracle 等驱动需下载或由客户 DBA 提供，优先厂商官方版（通用驱动可能兼容但不推荐）；③安装路径固定——SFTP 传到 /home/admin 再 sudo mv 到 /opt/ale/aa-webapp/lib（该目录不能直接 SFTP），然后 systemctl restart aa-webapp；④HA 模式下 slave 也要装同一驱动；⑤Oracle 连接串两种写法（TNS 服务名式 jdbc:oracle:thin:@host:1521:VAA 与 service_name 长串式）不等价，可能只有一个能通，驱动名 oracle.jdbc.driver.OracleDriver，连接串要向 Oracle 管理员索取。
  conditions: 实验 jar 版本 mssql-jdbc-9.4.1.jre8.jar / ojdbc6（jre8 兼容）
  tags: [checklist, jdbc, database]

- id: p23
  title: HA 行为数值与规则集（只读/丢话/不同步/容量）
  type: rule
  source_pages: p44-47, p51, p255, p271
  source_chapter: High availability / N+1 / slave web / test
  source_quote: |
    "The slave VAA database is in ReadOnly mode. Therefore, no statistics will be recorded for a call handled during the failure period on the PCS side." (p44)
    "Existing ongoing calls are lost when switch over occurs" (p45, p46, p47 三处重复)
    "No database synchronisation will be performed when master VAA will be recovered. Web client must reconnect (to Slave VAA)." (p47)
    "The overall capacity decreases during the downtime period of failed VAA" (p51)
    "A short delay may occur on the first call, as OXE will need to determine that the SIP trunk on the master server has been interrupted." (p271)
  summary: |
    规则集：①Slave 库只读——故障期间它处理的呼叫不产生统计；②任何切换（OXE 呼叫服务器切换、主 VAA 丢失、WAN 断）都丢失进行中呼叫；③主 VAA 恢复后不自动回同步——必须 vaa ha resync；Web 客户端要手动重连（到 Slave）；④N+1 场景单 VAA 故障期间总容量下降，reference VAA 故障期间不能改配置；⑤主 VAA 宕机切换后第一通呼叫有短暂延迟（OXE 要先判定其中继已断）；⑥Slave Web 界面登录会出现只读告警，配置应与 Master 一致（公司/路由/脚本）。
  conditions: 前提：OXE 侧已配 ARS 双路由（f26）
  tags: [rule, ha, behavior]

- id: p24
  title: HA 命令族速查（role/ismaster/whoismaster/listslave/addslave/removeslave/resync/free）
  type: checklist
  source_pages: p243-245, p297-299
  source_chapter: LIST OF AVAILABLE COMMANDS（HA/MASTER/SECONDARY 三页，内容重复出现两次）
  source_quote: |
    "sudo vaa ha role •Classic: VAA is in normal mode without HA •Master: The local server is Master •Slave: The local server is Slave … sudo vaa ha whoismaster … Delete the 'master' role •Delete the file /var/lib/ale/.master •Restart the VAA components •sudo vaa restart" (p243)
    "sudo vaa ha listslave … sudo vaa ha addslave @IP … sudo vaa ha removeslave <secondary @IP> •The secondary becomes autonomous (Classic mode) but keeps its database … sudo vaa ha resync" (p244)
    "sudo vaa ha free • In HA mode, the secondary VAA are in read-only mode … The VAA then switches to 'Classic' mode • The VAA goes back to slave mode on forced resynchronization of the master • sudo vaa ha resync" (p245)
  summary: |
    命令速查：任意节点——vaa ha role（Classic/Master/Slave）、vaa ha ismaster（Yes/No）、vaa ha whoismaster（本地/对端 IP/无）；仅 Master——vaa ha listslave（列 slave IP）、vaa ha addslave @IP（输对端 admin 密码、建 SSH key、推库快照）、vaa ha removeslave @IP（对端转 Classic 但保留库）、vaa ha resync（主从重同步）；仅 Slave——vaa ha free（master 完全不可达时的逃生门：临时转 Classic 改配置，之后须 master 强制 resync 拉回 slave）；删 master 角色——root 删 /var/lib/ale/.master 后 vaa restart。
  conditions: 全部需 root 权限（sudo）
  tags: [checklist, ha, vaa-commands]

- id: p25
  title: 备份/恢复三级命令与内容清单
  type: checklist
  source_pages: p285-290, p293
  source_chapter: EXPORT/IMPORT – BACKUP/RESTORE / MANUAL BACKUP WITH SSH COMMANDS
  source_quote: |
    "A zip file is created and contains the complete database, wav files included. Example: db_2025-01-21_12h13m52s.zip … Whole tenant. You will get a zip file with all tables belonging to that tenant." (p286)
    "vaa db backup <file.sql.gz> Create a database backup into a specified file .sql.gz or .tar" (p287)
    "vaa cert backup <file.sql.gz> … HTTPS configuration backup involving the following elements • Folder /etc/nginx/certificate • File /etc/nginx/nginx.conf • File /etc/nginx/conf.d (if not empty)" (p288)
    "vaa full backup <file.sql.gz> … secureCall configuration backup involving the backup of • Configuration file /etc/ale/vaa.conf • Certificate file /opt/ale/aa-media-server/VAACertificate.jks • Certificate file /etc/ale/aa-media-server/OXECertificate.pfs" (p289)
    "vaa db restore / vaa cert restore / vaa full restore <file.sql.gz>" (p290)
  summary: |
    三级备份：①vaa db——仅数据库（.sql.gz 或 .tar；推荐 .sql.gz）；②vaa cert——HTTPS 配置（/etc/nginx/certificate 目录 + nginx.conf + conf.d）；③vaa full——数据库 + 配置（/etc/ale/vaa.conf + secureCall 证书 VAACertificate.jks 与 OXECertificate.pfs）。对应 restore 同名三命令。Web 端 Admin 菜单导出：全局导出（zip，完整库含 wav 文件，如 db_日期.zip）、按租户导出（该租户全部表的 zip，或按选择出 CSV）；树可 CSV 文本导出（Editor 菜单）。
  conditions: 升级/迁移场景先把三级备份都做（p308 流程第一步）
  tags: [checklist, backup, vaa-commands]

- id: p26
  title: 自动备份规则（默认名/频率/NFS/不可关闭/容量自管）
  type: rule
  source_pages: p292-294, p102
  source_chapter: DATABASE AUTOMATIC BACKUP / install.sh backup step
  source_quote: |
    "It is strongly recommended to configure the AUTOMATIC backup of the database • This backup can be used in the event of reinstallation of the entire VAA … It is possible to backup VAA database onto a remote storage using NFS - There is no monitoring of the size used by the scheduled database backup • The administrator should monitor the available free disk space • For a 6 months database backup, 20 GB free disk space is recommended" (p292)
    "Once enabled, automatic database backup can't be disabled even if the option Backup activation is unchecked" (p294)
  summary: |
    四条规则：①强烈建议启用自动备份（整机重装时的恢复来源）；②配置 vaa conf backup 或 Admin/Settings/Backup parameters——文件名默认 vaa.tar，频率 Daily（午夜）/Weekly（周日午夜）/Monthly（每月首日午夜）/自定义 cron，可定义 NFS 远程存储位置（Web 端独有选项）；③一旦启用就无法关闭——即使取消勾选 Backup activation 也照跑；④系统不监控备份占用空间——管理员要自己盯磁盘，按 6 个月备份预留 20GB 空间。PCS 同步会复用该自动备份（Backup4PCS.sql.gz，p303）。
  conditions: install.sh 阶段即可启用（实验：vaa.tar Daily）
  tags: [rule, backup, nfs, capacity]

- id: p27
  title: 密码过期与备份的联动陷阱及两条解锁路径
  type: warning
  source_pages: p295, p276
  source_chapter: WARNING (Password duration and system backup)
  source_quote: |
    "Since version A 4.6.104, password expiration is enabled by default. It is therefore strongly recommended to change the password of the administrator account before backing up the database, if the administrator password is older than the password validity period defined in the VAA server. •In this case, if you haven't changed the password before making the backup, you won't be able to access the web administrator. - On the login page, click on 'Password or login lost' and follow the procedure. - Or ask a VAA server administrator to reset your password with the command : vaa db resetAccount [account]" (p295)
  summary: |
    陷阱：4.6.104 起密码过期默认开启（92 天）。恢复备份时，若备份里封存的密码在恢复时点已过有效期，恢复完反而登不进 Web 管理。因此改密要在做备份之前完成。已中招的两条路：登录页走 "Password or login lost" 流程；或让另一管理员执行 vaa db resetAccount [account] 重置指定账号。
  conditions: 与 p26 不可关闭的自动备份叠加时尤其要留意
  tags: [warning, backup, password]

- id: p28
  title: 告警与监控口径（邮件三类、SNMP 默认关）
  type: rule
  source_pages: p282-283
  source_chapter: EMAIL ALERTS & SNMP TRAPS
  source_quote: |
    "SIP trunk change status •When the SIP trunk goes down or when it comes back up - Reach ports usage limit •When the number of port reach the license limit - License issue •If your license file is not properly installed or the release doesn't match the software release - The SNMP service is not enabled by default" (p282)
  summary: |
    邮件告警三类事件：SIP 中继断开/恢复、端口使用达到许可上限、许可问题（未正确安装或版本不匹配）。SNMP trap 覆盖同类事件但服务默认不启用——需要网络监控平台集成时要手动开。SMTP 参数在 Admin 菜单 Settings 配置（改后必须重启服务，见 counter-example）。
  conditions: 告警依赖 install.sh/Settings 里的邮件通知配置
  tags: [rule, alerts, snmp, monitoring]

- id: p29
  title: vaa 服务与命令族（stop 保留 postgresql+nginx 等）
  type: checklist
  source_pages: p277-278, p253
  source_chapter: MAIN VAA SERVICES / MAIN COMMANDS
  source_quote: |
    "vaa stop Stop all VAA services except postgresql & nginx / vaa fullstop Stop all VAA services, and also postgresql & nginx / vaa start Start all VAA services, and postgresql & nginx are up / vaa restart Restart all VAA services / vaa status Get status for all VAA services / vaa services Get status for all VAA services / vaa version Get VAA version. Use –d to get details on each component." (p278)
    "VAA_PORTS : [5] ✔ … VAA_IVR : [true] ✔ … VAA_RELEASE : [11] ✔" (p253)
  summary: |
    命令族：stop（停业务服务但保留 postgresql 与 nginx）/fullstop（全停含 postgresql+nginx）/start（全起）/restart/status/services/version（-d 看组件明细）/conf https /conf telephony /conf backup /conf unlockAdmin /conf pcs /diag https /db backup|restore|reset|purgestats|userreset|sendBackup /cert backup|restore /full backup|restore /ha 子族。vaa services 输出同时展示许可要点：VAA_PORTS（端口数）、VAA_IVR（IVR 许可有无）、VAA_RELEASE（许可版本）——巡检一眼看许可。帮助：vaa -h；完整清单在安装手册第 6 章 VAA system management。
  conditions: HA 命令见 p24；服务清单 = p54 组件七件
  tags: [checklist, vaa-commands, services]

- id: p30
  title: 升级流程规则（备份先行、vaa.conf 不得直接覆盖、HA 全员升级+resync）
  type: rule
  source_pages: p307-309
  source_chapter: UPDATE A VAA VERSION / IN CASE OF HIGH AVAILABILITY
  source_quote: |
    "Then check the content of the file etc/ale/vaa.conf - Newer version of the VAA may add new required parameters in the file, so just replacing it by the backup is not advised. Please check that the values are still the same and perform modifications if needed. If you had to modify the file, then run vaa restart to apply the changes." (p308)
    "Perform the same procedure on all servers - On the master server , run • vaa ha resync" (p309)
  summary: |
    三条规则：①升级前先备份配置（/etc/ale/vaa.conf + vaa db backup）；②新版可能新增必需参数——旧 vaa.conf 不能直接覆盖新版文件，要逐值比对、有改动则 vaa restart；③HA 场景所有服务器都要走同一升级流程，最后在 master 上 vaa ha resync 重同步。S.O.T 可做自动升级（选 Boot DVD 与 VAA 目标版本 + admin 密码）。注意 4.8.006 的"升级"实为全新安装 + 恢复（p06）。
  conditions: 新发行包须配新许可（Release 11 口径）
  tags: [rule, upgrade, ha]

- id: p31
  title: 统计四指标与邮件周报开关
  type: metric
  source_pages: p313-317
  source_chapter: STATISTICS / REPORTS / TENANT REPORT RECEPTION BY EMAIL
  source_quote: |
    "The number of calls received • The number of treated calls • The calls released by the caller • The calls lost due to insufficient VAA license port … A pie chart: Number of calls transferred, number of 'released by vaa', number of 'released by caller', number of 'insufficient licenses'" (p314)
    "In the /etc/ale/vaa.conf file, two options must be set at true: • 'autogenerateTenantActivityReport'. default value Is true. … 'autogenerate ExcelTenantReport'. By default, this option is set at true." (p317)
    "if the administrator selects 'Monday', he will receive the Tuesday at the time defined, the report of the previous day, i.e. Monday." (p317)
  summary: |
    数值口径：报表四指标——收到呼叫数、已处理数、主叫挂断数、许可端口不足丢失数；饼图四分项——转出/VAA 挂断/主叫挂断/许可不足；租户报告 xlsx 仅管理员可收（需 "received activity reports" 权限 + 有效邮箱），两个 vaa.conf 开关默认 true（autogenerateTenantActivityReport、autogenerateExcelTenantReport）；发送日有偏移——选周一收的是周二收到的前一天（周一）报告。
  conditions: 逐节点时长明细在 Call Logs（p316）
  tags: [metric, statistics, reports]

- id: p32
  title: OPEX（Purple On Demand）运行条件与许可校验时点
  type: rule
  source_pages: p305
  source_chapter: SUPPORT OF OPEX MODE / PURPLE ON DEMAND
  source_quote: |
    "To use the OPEX mode, VAA must be connected to a cloud connected OXE and be associated to only one subscription - OPEX mode uses a pool of licenses for different applications. That means, the VAA ports declared in the OPEX project must be dispatched between all the VAA applications declared in the project. So, the VAA ports to use on a VAA server must be specified - VAA manages its licensing mode, either CAPEX mode or OPEX mode - License items values will be checked every night at midnight, whatever the working mode, CAPEX or OPEX" (p305)
  summary: |
    规则：OPEX 模式前提是 VAA 连接到云化 OXE 且只关联一个订阅；许可按项目池化——项目内声明的 VAA 端口要在全部 VAA 应用间分摊，因此必须在每台 VAA 服务器上指定可用端口数；VAA 自管理 CAPEX/OPEX 两模式；无论哪种模式，许可项数值每晚午夜校验一次。空间冗余在 Purple On Demand 下不支持（p46）。
  conditions: 多租户下端口不能按公司预留（p50）
  tags: [rule, opex, licensing]

- id: p33
  title: PCS 同步时序与默认值
  type: metric
  source_pages: p302-303
  source_chapter: VAA DATABASES SYNCHRONIZATION (COMMANDS)
  source_quote: |
    "Script to perform a synchronization between primary and PCS VAA • Process to be planned everyday at 01:00 AM, by sending automatic backup file and restoring it remotely" (p302)
    "Daily automatic backup defined with standard name Backup4PCS.sql.gz, if automatic backup file not set … A cron task can be set to launch vaa db sendBackup command • First cron task set at 01:00 AM. • Second cron task set at 01:00 + 1 minute • Third cron task set at 01:00 + 2 minutes (etc.)" (p303)
  summary: |
    数值口径：主 VAA→PCS VAA 同步每天 01:00 起跑（发自动备份文件 + 远端恢复）；未单独配置自动备份时使用默认备份名 Backup4PCS.sql.gz；多台 PCS 时 cron 任务依次错开——第 1 台 01:00、第 2 台 01:01、第 3 台 01:02，依此类推。sendBackup 生效三前提：自动备份已配置、备份文件已生成、SSH key 已布到远端。
  conditions: PCS 应急配置在网络恢复后丢失（p301）
  tags: [metric, pcs, synchronization]

- id: p34
  title: 网络服务前提口径（DNS/SMTP/邮件服务器/NFS 为企业现成设施）
  type: checklist
  source_pages: p7, p92, p99, p102, p237, p292
  source_chapter: TRAINING PLATFORM / Network configuration / install.sh / Mail node / NFS
  source_quote: |
    "IP address: 192.168.1.55 - FQDN: vaa1.company.com - Subnet mask: 255.255.255.0 - Gateway: 192.168.1.254 - DNS: 192.168.1.250" (p92, 实验口径)
    "[?] Enter the smtp server hostname or ip (without port): 10.20.30.11 - [?] Enter the smtp server port to use: 25" (p101, 实验口径)
    "This node is based on the client's infrastructure SMTP server." (p237)
  summary: |
    部署前核查清单：①服务器网络五参数（IP/FQDN/掩码/网关/DNS——FQDN 进许可文件，格式形如 vaa1.company.com）；②SMTP 服务器（告警与 Mail 节点都用客户自有 SMTP；实验 10.20.30.11:25 plain，发件 vaa.podX@company.com、收件 administrator.podX@company.com、口令 vaa）；③NFS 远程存储（自动备份异地化，可选）；④远程 syslog（可选）；⑤外部数据库（SQL 节点用，JDBC 可达 + 账号权限）。全部为"客户基础设施现成"假设项，现场先清点。
  conditions: 实验值全部为实验口径
  tags: [checklist, network, prerequisites]

- id: p35
  title: MS SQL Express 测试库搭建关键值（端口/认证/防火墙）
  type: metric
  source_pages: p330-338, p341-342
  source_chapter: MS SQL Express installation / Authorize TCP/IP connections / Configure the database engine
  source_quote: |
    "By default, TCP/IP connection are not allowed: ­ 'Enable' external TCP/IP connection" (p330)
    "By default, the historic port 1433 is not assigned anymore (depending on MS SQL server release). ­ Check if port 1433 is assigned. If not assign it!" (p331)
    "Note : First authentication is in 'Windows Authentication' mode only … Select the 'Security' menu and enable 'mixed authentication mode' - Restart the SQL service" (p332-333)
    "Check if windows firewall is activated. Disable it or add specific rule to accept incoming traffic on port 1433." (p338)
    "Unselect 'dynamically determine port' & put static port 1433" (p341)
  summary: |
    关键数值链：①SQL Server Configuration Manager 里 TCP/IP 默认禁用，要手工 Enable；②1433 端口在新版 MS SQL 默认不再分配，要在 IP Addresses 页签给所有接口手工指定静态 1433；③首次登录仅 Windows 认证——要给 VAA 用 SQL 账号必须切 mixed authentication mode 并重启 SQL 服务；④Windows 防火墙要么关要么放行 1433 入站；⑤VAA 侧/ODBC 测试侧都要取消"动态决定端口"、写死静态 1433；⑥测试登录 vaa/vaa（实验口径），测试库可放宽密码策略（Enforce password policy 可取消勾选），生产则按需授最小权限（多数场景只 SELECT）。
  conditions: 整章为测试库搭建（客户 DBA 正常承担）
  tags: [metric, mssql, database, firewall]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 22 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | Pod/OXE 基础准备 | 有（部分） | p34 | 网络/服务前提口径；DID 翻译参数值已入 framework f17/f03 |
| task-02 | 安装 VAA 应用 | 有 | p03, p04, p05, p06, p08 | 密码五层、默认账号、sudo 规则、4.8.006 规则、install.sh 参数清单 |
| task-03 | OXE 侧 SIP 对接与验证 | 有 | p09, p10, p11 | 编解码互斥、incoming username 契约、路由绑定规则 |
| task-04 | 安装 Web 证书 | 有（间接） | p05 | 证书生成参数（SHA-256/RSA4096/SAN）已入 framework f13 |
| task-05 | WebAdmin 初始管理 | 有 | p04, p28 | 默认账号规则、告警口径 |
| task-06 | 公司与业务时间/日历 | 有（间接） | p15 | 依赖物先行纪律；参数值已入 framework f21 |
| task-07 | 提示音与 TTS/ASR | 有 | p13, p14 | WAV 规范、引擎选型与成本 |
| task-08/09/10 | 三级树设计 | 有 | p15, p16, p17, p19 | 命名纪律、菜单参数全景、转接/Bypass、收号行为 |
| task-11 | 变量与条件 | 有 | p18 | 三类变量规则 |
| task-12 | 收号节点 | 有 | p19 | min=max/*/ # 行为细则 |
| task-13 | 显示名节点 | 有 | p20 | 三条边界 |
| task-14 | HTTP 节点 | 有（间接） | p18 | 变量依赖；GET/POST 等已入 framework f16 |
| task-15 | 邮件节点 | 有 | p34 | SMTP 前提口径 |
| task-16 | VAA HA 部署 | 有 | p23, p24 | HA 行为规则集 + 命令速查 |
| task-17 | OXE 侧 HA 配置 | 有（间接） | p23 | 行为规则；识别符/NPD 参数已入 framework f26 |
| task-18 | 日常维护 | 有 | p07, p25, p26, p27, p28, p29 | 许可、三级备份、自动备份规则、密码备份陷阱、告警、命令族 |
| task-19 | PCS/OPEX | 有 | p32, p33 | OPEX 条件与校验时点、PCS 时序默认值 |
| task-20 | 升级 | 有 | p06, p30 | 4.8.006 规则 + 升级三规则 |
| task-21 | 统计报告 | 有 | p31 | 四指标、开关、日期偏移 |
| task-22 | 外部数据库集成 | 有 | p21, p22, p35 | SQL 五条硬规则、JDBC 清单、MS SQL 关键值 |

**覆盖结论**：22/22 全部有对应条目（其中 6 项以"间接"方式由 framework 承载参数、principle 承载规则）。两点口径说明：
1. 实验口径数值（192.168.1.x 地址、Superuser1234* 口令、vaa/vaa 库凭证、10.20.30.11 SMTP、openweathermap token）均按原书如实转写并标注"实验口径"，生产化必须替换。
2. 服务器规格表（p01）与菜单参数表（p16）已逐格对照原文；原书 GRUB 密码两处大小写不一致（Generalconfig1!/GeneralConfig1!）作为书内缺陷记录在 counter-example，未擅自统一。
