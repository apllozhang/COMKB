# 案例/实验/操作序列候选 — Visual Automated Attendant (VSAAXTE001EN Ed20, R4.8.006)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号、token）标注"实验口径"。
> 条目说明: 全书 19 个 How-To 实验章逐一入册（c01-c19），无合并、无遗漏；讲义级操作序列不另设条目。

```yaml
- id: c01
  title: Pod 配置——OXE 底座准备（虚机核对、用户开通、DID 翻译、SIP 运营商、防火墙信任主机）
  type: lab
  source_pages: p63-74
  source_chapter: How-To / Pod Configuration
  source_quote: |
    "Check that the following virtual machines have started. Don't start the 'VAA slave' instance." (p64)；
    "According to your POD number, Create the DID translator as follow: ­ First external number: 33210P41000 … ­ First internal number: 31000 ­ Range size 500" (p69)；
    "Add the VAA master (IP @= 192.168.1.55) and VAA slave servers (IP @= 192.168.1.56) as a trusted host. via netadmin -m" (p70)
  steps: |
    1. 核对五台虚机已启动（OXE/OMS/FlexLM/PC Client/VAA Master）；不要启动 VAA Slave 实例。
    2. 核对 OXE 预配置（数据库与 Linux 数据已就绪）：许可已恢复、FlexLM 服务器（192.168.1.80）已声明、机架/板卡已建、用户已建、DHCP 已启用（话机地址段 192.168.1.145-149）、语音指引已下载、公网 SIP trunk group 已建。
    3. 核对 MAIN 站点设备在服：Software Rack 3U（OMS）、Rack N°4、Virtual GD4 slot 0，IP 192.168.1.13/24，MAC 00:50:56:01:01:13。
    4. 开通 IPDSP 31000（Brad Barkley）：启动 IPDSP → 按键开始 → 输分机号 31000 → 输密码 0000（实验口径）→ 确认 31000 in service。
    5. 逐个启动 MicroSIP 31001（Billy Backman）、31002、31003、31004，确认均为 Online。
    6. 外部 SIP 网关按 POD 填两个参数（SIP/SIP Ext. Gateway）：Registration ID = pbxP（例 POD 3 → pbx3）、Outgoing username = pbxP。
    7. DID 翻译（Translator/External Numbering Plan/Default DID num. translator，未建则点 create）：First external number = 33210P41000（P=POD 号，例 POD 3 → 33210341000）、First internal number = 31000、Range Size = 500。
    8. 外呼测试：向 SIP 模拟器拨打若干外线号码，确认公网 SIP 运营商正常（参照 SIP Carrier Simulator 文档）。
    9. 防火墙信任主机：OXE 上以 root 登录 → netadmin -m → 选 11 'Security' → 1 'Firewall(iptables) Configuration' → 3 'Restricted Access Configuration' → 先 1 查看现有列表 → 2 逐个添加（vaamaster/192.168.1.55、vaaslave/192.168.1.56，名字不在 hosts 库时答 y 并录地址）→ 1 复核列表 → 0 退出 → 回主菜单选 23 'Apply modifications'。
    10. （附）p74：PC Client 启动 Thunderbird，按 POD 号选择用户档案（例 Administrator – Pod1）用于收培训邮件。
  verification: |
    外呼可达公网模拟器（2.6）；信任主机列表出现 vaamaster 192.168.1.55 与 vaaslave 192.168.1.56（p72）；IPDSP/MicroSIP 全部在服。
  conditions: 实验口径（RLAB POD）；OXE 为预配置虚机。
  tags: [lab, pod, oxe, did-translation, firewall]

- id: c02
  title: VAA 应用安装——系统准备、传输、install.sh 交互与验收
  type: lab
  source_pages: p88-104（讲义前提 p75-87）
  source_chapter: How-To / Install the VAA application
  source_quote: |
    "Important information to read carefully before installing VAA 4.8.006: • Only a fresh installation followed by a database restoration is supported. • A new license (Release 11) is required." (p89)；
    "The new 'root' password must be InternationalSuperuser1234* and the 'admin' password must be Superuser1234*" (p92)；
    "[?] enter the incoming username of your Pbx external gateway::vaa1" (p101)
  steps: |
    1. （知识步，实验跳过）SUSE 系统安装：ALE BootDVD（或 ISO）启动 → 选 VAA → 选 4.8 → 自动安装 → 选键盘语言与 时区。实验从已装系统的虚机起步。
    2. root 首登改密：Console mode 登录 root/letacla1 → 重输旧密码 → 设新 root 密码（≥20 位）InternationalSuperuser1234*（实验口径）。
    3. 配网：依次输入 IP 192.168.1.55、FQDN vaa1.company.com、掩码 255.255.255.0、网关 192.168.1.254、DNS 192.168.1.250 → YES 确认 → 网络服务重启。
    4. GRUB/BIOS 口令：设置 ≥14 位口令（实验 Generalconfig1!；原书两处大小写不一致）。
    5. admin 账号改密：登录 admin/let acla1 → 重输旧密码 → 设新 admin 密码（≥12 位）Superuser1234*（实验口径）→ 退出 root 环境。
    6. 传输文件（FileZilla → 文件/站点管理器 → New site 名 VAA1）：协议 SFTP、主机 192.168.1.55、用户 admin、密码 Superuser1234*；首连勾 "Always trust this host"。发行包 Visual_Automated_Attendant_x.x.xx.zip → /home/admin（二进制模式）；license1.vaa → /tmp（二进制模式）。（实验口径：两个文件可先从 NAS 网络盘拷到 PC Client。）
    7. 解压：SSH/控制台登录 → 确认在 /home/admin → sudo su → unzip Visual_Automated_Attendant-4.8.006.zip。
    8. 安装：cd aa-distribution-4.8.006 → sudo ./install.sh → 本地 IP 192.168.1.55 确认 y。
    9. HTTPS：选 "I will provide the certificate files later" → 自动生成自签证书（/etc/nginx/certificate/certif_nginx.crt + nginx.key）。
    10. 媒体服务器：Main Pbx IP = 192.168.1.3；无备用则 standby 再填 192.168.1.3。
    11. incoming username = vaa1、密码留空（该值必须与 OXE 外部网关一致；网关侧最小认证 None）。
    12. 编解码：空格勾选 G711a 与 G729（要用语音识别则禁 G729；不确定选 G711a+G711mu+G729）。
    13. 代理 N；邮件通知 y：SMTP 10.20.30.11、端口 25、协议 plain、认证留空、发件 vaa.podX@company.com、收件 administrator.podX@company.com（X=POD 号）。
    14. 禁拨前缀（实验留空；生产填 PBX 外拨前缀）。
    15. 自动备份 y：文件名 vaa.tar、Daily（At midnight）。
    16. SIP TLS：N（实验）；PostgreSQL 密码 Superuser1234*（实验口径）；远程 syslog N。
    17. 许可：y → "I already copied my license file in /tmp" → 自动发现 license1.vaa → y 使用。
    18. 验收命令：vaa status 核对全部服务 Running。
  verification: |
    vaa status 全部服务 Running（p103）；浏览器打开 https://192.168.1.55 能看到 VAA Web 界面（p104）。
  conditions: 4.8.006 仅支持全新安装 + 数据库恢复；许可须 Release 11；生产环境证书应在安装前生成并放 /tmp。
  tags: [lab, installation, install-sh, suse, sftp]

- id: c03
  title: OXE 侧 SIP 对接与接通验证（trunk group、外部网关、信任 IP、路由、测试树、排障命令）
  type: lab
  source_pages: p105-121
  source_chapter: How-To / SIP configuration in OXE
  source_quote: |
    "Trunk group group ID: 10 ­ Trunk group name: SIPVAA1 ­ Q931 signal variant: ABC-F ­ Remote network: 10 ­ T2 specification: SIP" (p107)；
    "SIP external gateway ID Enter the number of the external SIP gateway. Example: 2 … Incoming username Enter the same name as the one used in the VAA installation procedure: vaa1 … Gateway type VAA type" (p109)；
    "From a computer (or softphone), call the number 31400 corresponding to tree just created. You should hear the 'welcome' message and the system should hang up automatically." (p118)
  steps: |
    1. 建 SIP trunk group（/Trunk groups/ Create）：Trunk group ID=10（OXE 上唯一）、类型 T2、名称 SIPVAA1、Node No.=1、Q931 signaling variant=ABC-F、Remote network=10（未占用且异于 OXE 网络号）、T2 Specificity=SIP、Homogeneous network for direct RTP=No。
    2. 中继局部设置（/Trunk groups/<SIPVAA1>/Trunk group Edition）：End to end dialing=Yes – Automatic voice frequency switching；DTMF end to end signal=Yes；Quality Profile for VoIP=Always VoIP。
    3. SIP 虚拟接入数（Trunk groups/<SIPVAA1>/Virtual Accesses for SIP Edition）：Number of SIP accesses=2（默认，可按需调整）。
    4. 本地 SIP 网关联动（/SIP/SIP Gateway）：SIP Subnetwork=10、SIP trunk group=10（初始化 SIPMOTOR；客户现场已有参数不要改）。
    5. 建 VAA 外部网关（/SIP/SIP Ext Gateways Create）：ID=2、名称 VAA1、SIP Remote domain=192.168.1.55、端口 5060、UDP、Supervision timer=60、Trunk group number=10、Incoming username=vaa1、Incoming Password 留空、Minimal authentication method=None、Gateway type=VAA type。
    6. 信任 IP（/SIP/Trusted IP Addresses Create）：192.168.1.55。
    7. 网络路由表（Translator/Network Routing Table/<network 10>）：Associated Ext SIP Gateway=2。
    8. 路由号码（Translator/Prefix Plan Create）：Number=314（树在 314xx）、Prefix meaning=Routing No.、Network No.=10、Trunk group ABC-F/No Node=10、Number of digits=5。
    9. 全局参数：DPNSS 前缀 599（/Translator/Prefix plan 删除既有 599 再以 'PCX address in DPNSS' 重建）→ /System Edition → Routing optimization=Yes；编解码 G729 两侧匹配（OXE N2 起默认，无需动）；外部回叫翻译去 0B（/Translator/External Numbering Plan/Ext. Callback Translation tables/rules Create：Basic number=B、删除位数=1）。
    10. 建测试树：浏览器 https://192.168.1.55 → admin/admin 首登改 Superuser1234* → 建公司 TEST（名称 + 号）→ 管理时区 → 位数 5 → 选中公司 → Editor → File/New（自动生成 Start 块）→ 加 Announcement 块连线 → 双击选 Welcome 指引 → 加 Hang up 块连线 → 保存树名 TEST → Routing 菜单输 31400 → 选 TEST 树 → 点图标激活。
    11. 接通测试：软话机拨 31400。
    12. 排障抓手：OXE 上 mtcl 登录跑 trkstat -r 10（中继 62 路状态）与 sipextgw –g 2（网关 IN SERVICE/参数核对）；SIP 抓包 motortrace 3 + traced（级别 1 最少信息、2 量大观察、3 需细节）或 mtracer 全套；VAA 侧 WebAdmin 头像 → Administrator Menu → Logs → 选 softcmp (SIP)，行数默认 200 可调 → Refresh。
  verification: |
    拨 31400 听到 Welcome 欢迎语后系统自动挂断（p118）；trkstat/sipextgw 状态正常。
  conditions: SIP 配置必须手工在 OXE 完成；呼叫建立异常先查 OXE 设置或禁用压缩（p114 Tips）。
  tags: [lab, oxe, sip, trunk-group, testing, motortrace]

- id: c04
  title: 证书安装——服务器换证书 + PC 信任根 CA + HTTPS 验证
  type: lab
  source_pages: p122-126
  source_chapter: How-To / Certificate installation
  source_quote: |
    "VAA1.pfx must be installed on the VAA server, the associated password is: alcatel ­ XCA.crt must be installed on the PC in trusted certification authorities" (p123)；
    "Use vaa diag https … Update the certificate by using the command vaa conf https" (p123)；
    "No certificate message should be displayed." (p126)
  steps: |
    1. 查现状：SSH（admin 登录 → su 到 root）→ vaa diag https（当前为安装期自签证书 VAA.crt）。
    2. 传证书：FileZilla 把 NAS 上的 VAA1.pfx 传到 /tmp（实验口径，证书密码 alcatel）。
    3. 服务器侧更新：vaa conf https → "Do you want to update the certificate used?" y → 选 "I already copied my certificate files in /tmp" → 发现 VAA1.pfx → y → 输证书密码 alcatel → 自动做格式转换（pfx 内嵌密钥）→ Nginx 配置并重启。
    4. 复核：vaa diag https 确认已用新证书。
    5. PC 侧装根 CA：右键 XCA.crt → Install Certificate → 安全警告点 Open → 存储位置选 Local Machine → 证书存储选 "Place all certificates in the following store" → 浏览选 Trusted Root Certification Authorities → OK → Next → Finish → 确认导入成功弹窗；可用 certmgr.msc 复核证书已在正确存储区。
    6. 验证：浏览器开 https://192.168.1.55（原文笔误写作 192.168.1.1.55）→ 应无证书告警 → 点"查看站点信息" → "Connection is secured" 查看安全细节。
  verification: |
    vaa diag https 显示已导入证书；浏览器无证书告警且连接显示已加密（p126）。
  conditions: 实验用 NAS 上的私有 CA 证书（实验口径）；暴露公网须购真证书（安装手册 6.4）。
  tags: [lab, certificate, https, xca]

- id: c05
  title: VAA WebAdmin 初始管理——第二管理员、SMTP 告警、监督/日志/许可页
  type: lab
  source_pages: p127-132
  source_chapter: How-To / VAA WebAdmin application
  source_quote: |
    "Create a second administrator account with the username letacla … Warning BY DEFAULT THE PASSWORD OF THE NEW ACCOUNT IS IDENTICAL TO THE IDENTIFIER OF THE LATEST." (p128)；
    "Configure / modify settings for SMTP notification - SMTP notification enabled: yes - SMTP server: 10.20.30.11 … Warning SERVICES MUST BE RESTARTED AFTER SMTP CONFIGURATION" (p130)；
    "Don't use these buttons unless instructions from the technical support team" (p131)
  steps: |
    1. 登录 https://192.168.1.55（admin / Superuser1234*，实验口径）。
    2. 建第二管理员：点头像图标 → Administrators → 输用户名 letacla → 建（可填姓名与邮箱）→ 注意警告：新账号默认密码=用户名 → 立即用 letacla 登录并改密为 Superuser1234*。
    3. Admin menu 浏览：Server info（服务器系统信息）。
    4. Settings 页签：配 SMTP 通知——enabled=yes、server 10.20.30.11、port 25、username vaa.podX@company.com、password vaa、协议 plain、sender vaa.podX@company.com、destination administrator.podX@company.com（X=POD 号，向讲师确认）→ 保存后必须重启服务（警告框）。
    5. Supervision 页签：查看各 VAA 服务状态、停止/重启（无技术支持指示不要用这些按钮）。
    6. Logs 页签：五类日志——aa-media-server（主日志，SIP 连接与 RTP）、aa-management（Web 管理应用）、aa-engine（VXML server，取脚本）、softcmp (SIP)（与 OXE 的 SIP 交互踪迹）、tts-hub（TTS/识别服务）。
    7. License server 页签：查看当前加载许可文件的内容与占用。
  verification: |
    letacla 能以新密码登录；SMTP 配置保存且服务已重启；Logs 页签可见五类日志并可选类型查询。
  conditions: 实验口径 SMTP 值；新管理员默认密码=用户名是必须立即修复的弱口令。
  tags: [lab, webadmin, smtp, logs, license]

- id: c06
  title: 创建公司 Company1 与业务时间/日历配置
  type: lab
  source_pages: p133-136
  source_chapter: How-To / Create a new company
  source_quote: |
    "Create the following company: ­ Name: Company1 ­ Time zone: Europe/Paris (UTC+02:00) ­ DID range dedicated for trees: 31400 – 31415 ­ Voicemail prefix: 31499 ­ Directory number length: 5 digits" (p134)；
    "Define the Business hours name 'Open hours' … ­ Business hours from 9am to 12 and from 2pm to 6pm ­ Closed during the Weekend" (p135)；
    "Create a new calendar ­ Name: Calendar1 ­ Define closing days: 1st of January, 14th of April, 14th of July and 11 of November" (p135)
  steps: |
    1. 登录 https://192.168.1.55（admin/Superuser1234*）；本实验全程用 TTS Pico 引擎（先行确认已激活，见 c07）。
    2. 建公司：输名称 Company1 → 点 "+"。
    3. 公司设置：Time zone=Europe/Paris (UTC+02:00)；DID Range=31400-31415（实验用内线号口径）；Voice Mail=31499（留言前缀/留言箱号）；Extension Length=5。
    4. 选中公司：点公司名左侧对勾进入其配置参数。
    5. 营业时间：VAA / Schedule 页签 → Business Hours 页签 → 名称 Open hours → "+" → 按天更新时段（9:00-12:00、14:00-18:00，周末关闭，时区 Europe/Paris）。
    6. 日历：Schedule 页签 → Calendars 页签 → 名称 Calendar1 → "+" → 勾闭假日（1 月 1 日、4 月 14 日、7 月 14 日、11 月 11 日）→ 再管理来年的假日。
  verification: |
    公司出现在租户列表且可选中配置；Schedule 页签下 Open hours 与 Calendar1 建成并可编辑。
  conditions: 本实验数值全部为实验口径；日历/营业时间后续供 UC2 树引用。
  tags: [lab, company, business-hours, calendar]

- id: c07
  title: 提示音与 TTS 管理——WAV 导入、Pico 引擎激活与 TTS 生成
  type: lab
  source_pages: p137-142
  source_chapter: How-To / Manage Prompts and Text-to-Speech
  source_quote: |
    "Wav files uploaded to prompts should have the format: 8 KHz, PCM 16 bits mono. … No space in the name" (p138)；
    "Define a name: TTS Pico - Choose the TTS engine: PICO - SAVE - Make a test ­ Language Pico English/French…etc ­ Click on Generate to create a WAV file" (p140)；
    "The Pico TTS engine can be used free of charge and without an internet connection. But it is not recommended for production. - Google Cloud is recommended but NOT free" (p141)
  steps: |
    1. 导入 WAV：NAS 上取样例 WAV → Your company / Prompts → 新建提示音（名称无空格）→ 选语言 → 选 WAV 文件上传（格式必须 8KHz PCM 16-bit 单声道）→ 上传后可播放/下载/录音替换。
    2. 激活 TTS：点设置图标 → Tenant / Settings → Text to speech 页签 → 定义引擎：名称 TTS Pico、类型 PICO → SAVE。
    3. 测试生成：语言选 Pico English/French 等 → 输文本 → Generate 生成 WAV 文件试听。
    4. （知识）TTS 引擎对照：Pico 免费离线六语言（不建议生产）；Google Cloud TTS 生产推荐但收费（信用卡）；价格信息可能过时，详见管理指南第 10 章。
    5. 树内 TTS 生成：Prompts 页选 Text-to-Speech 按钮，或在建树时直接于 Announcement 块内写文本生成（见 c08-c10）。
  verification: |
    Generate 能产出可播放的 WAV；导入的 WAV 在 Prompts 列表可播放。
  conditions: WAV 格式与命名规范是硬约束；ASR（Google）需另行在公司设置配 API key。
  tags: [lab, prompts, tts, pico]

- id: c08
  title: 树用例 1——欢迎 + 监督转接 + 忙/无应答分支（Training 树，31401）
  type: lab
  source_pages: p164-172
  source_chapter: How-To / Manage a VAA script (tree) – Use case 1
  source_quote: |
    "Use a Transfer node to transfer calls to the number entered: 31000. The transfer will be supervised, this will make it possible to manage behavior on busy and no response" (p168)；
    "­ Name : Main Menu Training ­ Destination mode : Phone number ­ Destination : 31000 ­ Transfer : Supervised transfer ­ Wait time : 15s … ­ Bypass forward : OK." (p168)；
    "On No answer – IPDSP 31000 ­ The welcome message must be played ­ After 15s, the prompt No answer must be played" (p172)
  steps: |
    1. 建树：Editor 页签 → File / New（自动生成 Start 块）→ Start 命名 Training、选公司默认语言。
    2. 保存：File / Save 命名。
    3. 欢迎节点：Announcement 块命名 Welcome Training → Mode=Text to speech → TTS=Pico → Language=English US → 文本 "Hello, welcome to the training department, we will answer your call." → Interruption prompt 不勾（呼叫者不能跳过）→ 与 Start 连线。
    4. 转接节点：Transfer 块命名 Main Menu Training → Destination mode=Phone number、Destination=31000 → Supervised transfer → Wait time=15s → Bypass forward 勾选（忽略被叫呼转）→ Hold guide=HoldGuide（系统默认音乐）。
    5. 无应答节点：Announcement 块命名 No answer → TTS（Pico/English US）文本 "We are not available, please call back later"。
    6. 忙节点：Announcement 块命名 Busy → TTS 文本 "All our lines are busy, please call back later"。
    7. 挂断节点：建 Release 块收尾；逐节点连线；保存树。
    8. 路由：Editor 页签 / Routing → Number=31401（公司 DID 段内）→ 填描述 → 选树 Training → 点激活图标。
  verification: |
    p172 三项测试：①31000 空闲——拨 31401 播欢迎语后转接到 IPDSP 31000（回铃期也放保持音）；②31000 忙——先用 MicroSIP 占住 31000，再拨 31401：欢迎语 + 保持音；③无应答——欢迎语后等 15s 播 No answer 提示音。
  conditions: 依赖 c01（用户在服）、c02（VAA 可用）、c03（接通）完成；每个节点必须命名（统计）。
  tags: [lab, tree, use-case-1, transfer, tts]

- id: c09
  title: 树用例 2——日历 + 营业时间 + VIP 过滤分流（Customers services 树，31402）
  type: lab
  source_pages: p173-184
  source_chapter: How-To / Manage a VAA script (tree) – Use case 2
  source_quote: |
    "Callers will be filtered : ­ 31000 (IPDSP) is a VIP. It will receive a personalized answer and will be transferred to the number: 31001 ­ All other callers (Non VIP) will be transferred to the extension number 31002." (p175)；
    "­ Name : VIP transfer ­ Destination mode : Phone number ­ Destination : 31001 ­ Transfer : Blind" (p182)；
    "From the extension 31000 (IPDSP), call the tree number 31402 ­ The welcome message must be played ­ If the company is open, the extension 31001 must ring, that's mean, routed through VIP transfer node" (p184)
  steps: |
    1. 前置（先于建树）：日历 Calendar2（Editor 页签 / Schedule / Calendar，定义闭假日）；营业时间 Business Hours company1（9-12、14-18）；过滤器 VIP filter comp1（Editor / Filters：Filter=31000，多号码可逗号分隔）。
    2. 建树：File / New → Start 命名 Customers services（公司默认语言）→ 保存。
    3. 欢迎节点：Announcement 命名 Welcome customers → TTS Pico / English US → 文本 "Welcome dear customers"。
    4. 日历节点：Calendar 块命名 Calendar2 → 选择 Calendar2 → 营业日走 Business hours 分支、闭日走闭馆提示分支。
    5. 营业时间节点：Business hours 块命名 Business Hours company1 → Hours 选前置建好的 Business Hours company1 → 营业时段走下一节点、非时段走闭馆提示。
    6. 闭馆提示：Announcement 命名 Closing hours prompt → TTS 文本 "Please, call during opening hours" → 接 Release 块（命名 Release call company1）。
    7. 过滤节点：Filter 块命名 VIP filter Comp1 → Filter 选 Filter comp1VIP（Unknown ANI 按需）。
    8. VIP 转接：Transfer 块命名 VIP transfer → Destination=31001 → Blind（盲转）→ 接 Filter 节点的 Filtered 连线。
    9. 非 VIP 转接：Transfer 块命名 NonVIP transfer → Destination=31002 → Blind → 接 Unfiltered 连线。
    10. 保存树；路由：Number=31402 → 树 Customers services → 激活。
  verification: |
    p184 测试：MicroSIP 拨 31402——欢迎语后，公司开门则 31002 振铃（NonVIP 路径）、关门则播闭馆提示；IPDSP 31000 拨 31402——开门则 31001 振铃（VIP 路径）、关门则播闭馆提示。
  conditions: 日历/营业时间/过滤器必须先建；VIP 判定基于主叫号码 31000。
  tags: [lab, tree, use-case-2, calendar, filter]

- id: c10
  title: 树用例 3——法英双语多级菜单（Welcome employees 树，31403）
  type: lab
  source_pages: p185-201
  source_chapter: How-To / Manage a VAA script (tree) – Use case 3
  source_quote: |
    "The Welcome prompt must be recorded in both languages in the same WAV file, because the choice of languages is only made after its broadcast." (p187)；
    "­ Name: Main menu - choices ­ Mode: Prompt ­ Prompt: MainMenuChoices … ­ N° of retries: 2 ­ Timeout: 4 ­ Repeat digit: * ­ Max repeat: 2 … Exception: in case of inactivity, the caller will be transferred to the attendant 31000" (p197)；
    "CHOICE 4 – Create a Go to node connect to training tree ­ Name: Connect to Training tree ­ Target tree: Training Tree" (p200)
  steps: |
    1. 前置提示音（全部先建）：MainMenuChoices（TTS 双语：法 "Taper 1 pour écouter le process à suivre. Taper 2 pour être mis en relation avec l'accueil. Taper 3 pour déposer un message vocal concernant votre requête. Taper 4 pour être mis en relation avec le service formation."；英 "Press 1 to listen to the process to follow. Press 2 to be connected to the reception. Press 3 to leave a voice message concerning your request. Press 4 to be connected to the training department."）；PromptInformationEmployees（双语 "Voici le procedure vous concernant bla bla bla." / "Here is the procedure for you. blah blah blah."）；欢迎语在同一提示音内 TTS 串联法语+英语两条。
    2. 建树：File / New → Start 命名 Welcome employees → 保存。
    3. 欢迎节点：Announcement 命名 Welcome customers → TTS Pico / french → Prompt #1 法语文本 → 加 Prompt #2 英语文本（同一提示音内串联）。
    4. 语言选择菜单：Menu 块命名 Languages choice → TTS → Choice 1 "Tapez 1 pour le Français"、Choice 2 "Press 2 for English"（双语同文件口径）→ Wrong option prompt 配错误提示 → Exception（无输入）接 Release 块。
    5. 语言分支：建 French 与 English 两个节点（Select language 类）并与菜单连线（Choice 1→French、Choice 2→English）。
    6. 主菜单：Menu 块命名 Main menu - choices → Mode=Prompt、Prompt=MainMenuChoices → Wrong option prompt=DidNotUnderstand → N° of retries=2 → Timeout=4 → Repeat digit=* → Max repeat=2 → Exception（无输入）建 Transfer 块 Attendant→31000。
    7. 选项 1：Announcement 命名 Information prompt（Mode=Prompt、Prompt=PromptInformationEmployees）→ 低层再接 Release。
    8. 选项 2：Transfer 块命名 helpdesk → Destination=31002 → Blind。
    9. 选项 3：Voicemail 块命名 Voice mail → Mailbox=31000（留言箱号须在公司设置管理）。
    10. 选项 4：Go to tree 块命名 Connect to Training tree → Target tree=Training Tree（仅同租户可选）。
    11. 保存配置；路由：Number=31403 → 树 Welcome employees → 激活。
  verification: |
    p201 测试：MicroSIP 拨 31403，用英法两种语言走完整脚本（语言选择→主菜单四选项各一遍），并测试异常路径（错误选项重试、超时无输入转话务员/挂断）。
  conditions: 双语提示必须"同一 WAV 内串联"是本用例核心约束；菜单顺序 1-4 由连线顺序决定。
  tags: [lab, tree, use-case-3, multilanguage, menu]

- id: c11
  title: IVR 变量实验——Set variable + Condition 判内外线与 VIP（31404）
  type: lab
  source_pages: p215-220
  source_chapter: How-To / IVR node - Variables
  source_quote: |
    "With Set a variable and Condition nodes, it is possible to create more dynamic scripts (trees)." (p216)；
    "The conditions to be tested will be: ­ Internal numbers start with 31 ­ The external calling number +33210P12345 (P: pod number) is a VIP" (p218)；
    "­ Routing number: 31404 ­ Assign the Tree ­ Enable Routing" (p219)
  steps: |
    1. 建树（File/New，Start 自动生成）。
    2. Set variable 节点：复制上下文变量 "callingNumber" 的内容到自定义变量。
    3. Announcement 节点：欢迎提示（现有指引或 TTS Pico）。
    4. Condition 节点：判断内部来话（号码以 31 开头）→ 是则接 Announcement → TTS 提示 "Internal Call"。
    5. Condition 节点：判断 VIP（等于 +33210P12345，P=POD 号）→ 是则 TTS "VIP call"，否则 TTS "Other calls"。
    6. Release 节点收尾；保存树。
    7. 路由：31404 → 绑树 → 启用。
  verification: |
    p219 三项测试：内部呼叫（报 Internal Call）；"公网用户"呼入 0210P12345（报 VIP call）；内部用户打公网回环（按主叫属性报对应结果）。
  conditions: 上下文变量 callingNumber 只读；进阶（p220）：做 3 次迭代循环并在 TTS 中报每一轮。
  tags: [lab, variables, condition, ivr]

- id: c12
  title: IVR 收号实验——采集 5 位工号（31405）
  type: lab
  source_pages: p221-223
  source_chapter: How-To / IVR node – Collect digits
  source_quote: |
    "The information collected must imperatively be stored in a variable for future use" (p222)；
    "Collect digits node - Collect 5 digits - Timeout between digits 4s - Maximum timeout for input 20s - Manage false input" (p222)；
    "Enter * - * is considered as a correct entry - Enter 1234# - # is the default character to finish the input - Impossible to modify" (p223)
  steps: |
    1. 建树：Start → Announcement（欢迎提示，现有指引或 TTS Pico）。
    2. Collect digits 节点：收 5 位、数字间超时 4s、总输入超时 20s、配置错误输入处理；结果存变量。
    3. Announcement 节点：TTS Pico 播报 "Your file number is xxxx"（变量回读）。
    4. Release 收尾；保存树。
    5. 路由：31405 → 绑树 → 启用。
  verification: |
    p223 行为测试：输 5 位——正常播报；输 4 位——失败（本例 min=max）；不输入——走无输入异常；输 * ——视为一次正确输入；输 1234# ——# 立即结束输入（默认行为不可改）。
  conditions: 进阶（p223）：改造为 3-5 位可变长度输入。
  tags: [lab, collect-digit, ivr]

- id: c13
  title: IVR 显示名实验——监督转接屏显自定义信息（31406）+ OXE COS
  type: lab
  source_pages: p224-230
  source_chapter: How-To / IVR node – Display name
  source_quote: |
    "With the Display name node, the VAA can send a display information on the screen of the destination phone set during the ringing phase. This feature is only available for supervised transfers" (p225)；
    "­ Display name node - Enter the text to display on the phone screen ­ Transfer node – supervised type - Transfer to 31000" (p225)；
    "When you go off hook, this information disappears and that the caller information is displayed" (p228)
  steps: |
    1. 建树：Start → Announcement（欢迎提示）。
    2. Display name 节点：输入要在话机屏显示的文本（示例 "Hello my friend"）。
    3. Transfer 节点：监督转接到 31000（本实验不处理转接失败分支）。
    4. Release 收尾；保存脚本。
    5. 路由：31406 → 绑树 → 启用。
    6. OXE 侧：管理话机特性 COS（1.2 节，界面截图步）。
    7. 抓包对照：OXE 控制台跑 motortrace 1 + traced → 拨打测试树。
  verification: |
    p227-228：①振铃期目标话机屏显自定义文本；②SIP INVITE 的 From 头可见该显示信息（From: "Hello my friend" <…>）；③摘机后显示信息消失、恢复主叫信息（外部显号码、内部显姓名）；停止抓包。
  conditions: 仅监督转接、仅振铃期生效；进阶（p229）：用变量生成动态显示文本。
  tags: [lab, display-name, transfer, sip-trace]

- id: c14
  title: IVR HTTP 实验——openweathermap 天气播报树（31407）
  type: lab
  source_pages: p231-235
  source_chapter: How-To / IVR node – HTTP request
  source_quote: |
    "This weather service is free but requires registration on their platform. When requesting, it is necessary to provide a tokenID. The following tokens will be used for the exercises: ­ ccc6a9e2900887a12bbaec89f17e506d ­ 689cd17f15fbb639e8ab7e7fa8f38921" (p232, 实验口径)；
    "http://api.openweathermap.org/data/2.5/weather?q=brest,FR&appid=689cd17f15fbb639e8ab7e7fa8f38921&units=metric&lang=fr" (p234)；
    "The temperature is VAR(resultHTTP.main.temp) degrees celsius at VAR(resultHTTP.name). The humidity rate is VAR(resultHTTP.main.humidity)%." (p234)
  steps: |
    1. 前置认知：openweathermap 免费但需注册取 tokenID（实验提供两个 token，实验口径）；返回 JSON；VAA 可按对象路径取值——VAR(resultHTTP.main) 取对象、VAR(resultHTTP.main.temp) 取标量（示例 3.33）。
    2. 建树：Start → Announcement（欢迎提示，现有指引或 TTS Pico）。
    3. HTTP 节点：请求 https://api.openweathermap.org/data/2.5/weather?q=brest,FR&appid=<token>&units=metric&lang=fr → 结果存变量 resultHTTP。
    4. Announcement 节点：TTS 播报 "The temperature is VAR(resultHTTP.main.temp) degrees celsius at VAR(resultHTTP.name). The humidity rate is VAR(resultHTTP.main.humidity)%."
    5. Release 收尾；保存脚本。
    6. 路由：31407 → 绑树 → 启用。
  verification: |
    拨 31407 播报布雷斯特实时温度与湿度（p235 测试：换城市、取其他数据复测）。
  conditions: JSON 取值点语法 VAR(变量.对象.字段)；进阶（p235）：Collect digits 收邮编存 resultCP，URL 用 zip=VAR(resultCP),FR 发起请求。
  tags: [lab, http, json, ivr]

- id: c15
  title: IVR 邮件实验——来话通知邮件（31408）
  type: lab
  source_pages: p236-238
  source_chapter: How-To / IVR node – Mail
  source_quote: |
    "Sender: vaa.podX@company.com - Destination: administrator.podX@company.com - SMTP Server: 10.20.30.11 (or mail-server.company.com) - Login: vaa.podX@company.com - Password: vaa" (p237, 实验口径)；
    "­ Mail node: send an email with following information - the caller's number - the called party's number" (p237)；
    "­ Routing number: 31408 ­ Assign the Tree ­ Enable Routing" (p237)
  steps: |
    1. 复核 SMTP 前提（c05 已配或按提醒值配置：SMTP 10.20.30.11、发件 vaa.podX@company.com、收件 administrator.podX@company.com、口令 vaa）。
    2. 建树：Start → Announcement（欢迎提示，现有指引或 TTS Pico）。
    3. Mail 节点：发送邮件，正文含主叫号码与被叫号码（可变量引用）。
    4. Release 收尾；保存脚本。
    5. 路由：31408 → 绑树 → 启用。
  verification: |
    拨打测试树后，用邮件客户端（Thunderbird，c01 第 10 步配置的档案）查收邮件，确认内容含主/被叫号码（p238）。
  conditions: Mail 节点基于客户基础设施 SMTP 服务器；SMTP 改动后需重启服务（c05 警告）。
  tags: [lab, mail, smtp, ivr]

- id: c16
  title: VAA 高可用安装——slave 准备 + addslave + 双侧五项验证
  type: lab
  source_pages: p247-255（讲义 p240-246）
  source_chapter: How-To / Install the high availability for VAA
  source_quote: |
    "Manage the following IP settings: ­ F.Q.D.N: vaa2.company.com ­ IP address: 192.168.1.56 … The new 'root' password must be InternationalSuperuser1234* and the 'admin' password must be Superuser1234*" (p248)；
    "vaa ha addslave 192.168.1.56 … Please enter password for admin@192.168.1.56.(This will be used to generate ssh keys to allow sync to this slave server and to copy a snapshot of the current database to the slave server.)" (p252)；
    "[admin@vaa2 ~]# sudo vaa ha role - VAA role is : Slave" (p252)
  steps: |
    1. slave 系统准备（同 c02 流程）：BootDVD 装 SUSE（实验跳过）→ root 改密 InternationalSuperuser1234* → 配网：IP 192.168.1.56、FQDN vaa2.company.com、掩码 255.255.255.0、网关 192.168.1.254、DNS 192.168.1.250（FQDN 用于许可文件；许可问题查 /var/lib/ale/aa-license-server/）→ GRUB 口令 → admin 改密 Superuser1234*。
    2. slave 装 VAA（步骤同 c02，参数差异）：incoming username=vaa2、许可文件 license2.vaa；其余同 master（CS 192.168.1.3、G711a+G729、SMTP 10.20.30.11、SIP TLS N、无 postgres 密码、每日备份 vaa.tar、无远程 syslog）。
    3. 装后核对：slave Web 界面可访问；两机互 ping 通；HA 配置一律从 MASTER 侧发起。
    4. master 侧：SSH 192.168.1.55（admin/Superuser1234*）→ sudo su → vaa ha role（应显示 Classic）。
    5. 加 slave：vaa ha addslave 192.168.1.56 → 输 slave 的 admin 密码 Superuser1234*（生成 SSH key + 复制当前库快照；警告：slave 上已有配置将被清空覆盖）。
    6. slave 侧：SSH 192.168.1.56 → sudo vaa restart（重启全部组件）→ sudo vaa ha role（应显示 Slave）。
    7. master 侧验证：vaa services（全部 Running，含 VAA_PORTS [5]/VAA_IVR [true]/VAA_RELEASE [11] 实验口径）→ vaa ha role（Master）→ vaa ha listslave（192.168.1.56）。
    8. slave 侧验证：vaa services（全 Running）→ vaa ha role（Slave）→ vaa ha whoismaster（Master : 192.168.1.55）。
    9. slave Web 复核：登录 http://192.168.1.56 → 确认只读告警 → 核对公司/路由/脚本配置与 master 一致。
  verification: |
    双侧 vaa services 全 Running；role Master/Slave 各归其位；listslave/whoismaster 互指正确；slave Web 只读且配置同 master（p253-255）。随后 ARS 配好后做故障切换（c17 第 9 步）。
  conditions: addslave 会用 master 库快照覆盖 slave；实验口径密码/许可名。
  tags: [lab, ha, addslave, vaa-commands]

- id: c17
  title: OXE 侧 HA 附加配置——第二中继/网关/识别符/NPD/ARS 双路由/速拨号 + 切换测试
  type: lab
  source_pages: p256-271
  source_chapter: How-To / OXE Additional configuration in case of High availability
  source_quote: |
    "trunk group ID: 11 ­ Trunk group name: SIPVAA2 … Remote network: 11 ­ T2 specificity: SIP" (p258)；
    "SIP external gateway ID 3 - Gateway name VAA2 - SIP Remote domain … 192.168.1.56 … Incoming username … vaa2" (p260)；
    "Simulate master server failure - Run the command sudo vaa stop or shut down the machine. Call a VAA routing number (ex: 3140X) ­ A short delay may occur on the first call … After the test, remember to restart the VAA on the master server by running sudo vaa start." (p271)
  steps: |
    1. 第二 trunk group（/Trunk groups/ Create）：ID=11、类型 T2、名称 SIPVAA2、Node=1、Q931=ABC-F、Remote network=11、T2 Specificity=SIP、直连 RTP=No；局部设置同 c03 步骤 2；SIP virtual access=2（默认）。
    2. slave 外部网关（/SIP/External Gateways Create）：ID=3、名称 VAA2、SIP Remote domain=192.168.1.56、端口 5060、UDP、proxy=192.168.1.56、Supervision timer=60、Trunk group number=11、Incoming username=vaa2、密码空、Minimal authentication=none、Gateway type=VAA type。
    3. 信任 IP（/SIP/Trusted IP Addresses Create）：192.168.1.56。
    4. 识别符（Translator/External numbering plan/Numbering discriminator Create）：No.=11、name=VAA；识别规则（Discriminator 11 / Discrimination rule Create）：Call number=314（放行 314 开头五位号）、Area number=Zone 1、ARS route list No.=11、Number of digits=5。
    5. Entity 挂接：Entity/1/discriminator selector（分机）与 Entity/0（中继）——条目 05 填识别符 11。
    6. NPD（Translator/External Numbering Plan/Numbering Plan Description Create）：Description id=56、name=VAA、主/被叫 NPI/TON=ISDN Unknown、其余 None used。
    7. 编号命令表：/Translator/automatic route selection/Numbering Command Table——表 10（command=I 大写 i=Insert、Associated Ext SIP Gateway=2）与表 11（command=I、外部网关=3）。
    8. ARS：ARS Route list 建 11（name=VAA）；其下 ARS Route 建 Route 1（name=VAA1、trunk group=10、Num command table ID=10、NPD identifier=56、quality 加 speech）与 Route 2（name=VAA2、trunk group=11、NCT=11、NPD=56、speech）；Time Based Route List 建 1（Route 1=VAA1、Cost-waiting Limit=-1、Stopping cost limit=-1；加 Route 2=VAA2、同 -1）。
    9. 测试号：ARS 前缀（/Translator/Prefix plan Create）：number=21、meaning=ARS Prof.Trk Grp Seiz.with overlap、Discriminator No.=5；速拨（/Speed dialing/ 长度 30；direct SpdDI Create）：Direct speed dial nb=31401、Call number=2131401（ARS 前缀+树号）、name=Training。
    10. HA 切换测试：前提 OXE 侧 SIP 已通（c03）→ master 上 sudo vaa stop（或关机）→ 拨 3140X——首呼有短延迟（OXE 判定 master 中继断开），随后脚本应从 slave 读出，与 master 正常时一致 → 测完 master 上 sudo vaa start。
  verification: |
    拨 3140X：master 停机后呼叫由 slave 脚本接续（首呼短延迟属预期）；恢复 master 后服务回归（p271）。
  conditions: 全部数值为实验口径；识别符/ARS/NPD 为 OXE 编号计划概念，前提 c03/c16 已完成。
  tags: [lab, oxe, ha, ars, discriminator, failover-test]

- id: c18
  title: 外部数据库集成——JDBC 驱动安装 + 库连接 + SQL 节点树（31410）+ Oracle 附录
  type: lab
  source_pages: p319-325
  source_chapter: How-To / IVR node - Connect an external SQL database
  source_quote: |
    "By default, only the org.postgresql.Driver and org.mariadb.jdbc.Driver drivers are available and integrated with the VAA." (p320)；
    "The format of the JDBC URL for MS SQL is as follows: jdbc:sqlserver://10.20.30.11:1433;Database=DB_VAA - JDBC Driver Name for MS SQL: com.microsoft.sqlserver.jdbc.SQLServerDriver … Login: vaa ­ Password: vaa" (p322, 实验口径)；
    "SELECT transfertNumber FROM customers WHERE callingNumber='VAR(callingNumber )'" (p323)
  steps: |
    1. 装驱动（MS SQL 示例）：从共享目录取 mssql-jdbc-9.4.1.jre8.jar → SFTP 传到 VAA 的 /home/admin → SSH 执行 sudo mv /home/admin/mssql-jdbc-9.4.1.jre8.jar /opt/ale/aa-webapp/lib（该目录不能直接 SFTP）→ sudo systemctl restart aa-webapp；HA 模式下 slave 也要装。
    2. 建库连接：Web 管理界面 → Settings 菜单 → External Databases 页签 → 输库名点 "+" 加库 → 填 JDBC URL：jdbc:sqlserver://10.20.30.11:1433;Database=DB_VAA → 驱动名 com.microsoft.sqlserver.jdbc.SQLServerDriver → 凭证 vaa/vaa（实验口径）→ 做连接测试。
    3. 测试数据（实验库 customers 表）：+33210212345（pod2 口径 +3321PN12345，VIP=YES，转 31000）；+33210241000（VIP=NO，转 31001）。
    4. 建树：Startup → Announcement（欢迎提示，现有指引或 TTS Pico）。
    5. SQL request 节点：请求 SELECT transfertNumber FROM customers WHERE callingNumber='VAR(callingNumber)' → 结果存变量；管理 SQL 失败（红色输出接失败提示）。
    6. Condition 节点：测试结果非空（空结果不产生 SQL 错误，必须显式判）。
    7. Transfer 节点：监督转接到库中返回的号码；任何失败（SQL/转接）播专用提示后 Release。
    8. 保存；测试路由号 31410。
  verification: |
    p324：用不同分机外呼，对照 customers 表核验转接号——+33210212345 转 31000、+33210241000 转 31001。进阶（p324）：再查 VIP 字段——VIP 则转接前先播优先处理提示（需要 2 条 SQL 分别取 VIP 与 transfertNumber）。
  conditions: VAA 一次只取一个字段、多条结果取第一条；安全上库连接应定义在公司设置。
  tags: [lab, sql, jdbc, mssql, ivr]

- id: c19
  title: MS SQL Express 测试库搭建——安装、SSMS、TCP/IP、mixed 认证、建库建表、ODBC 验证
  type: lab
  source_pages: p326-344
  source_chapter: How-To / MS SQL Express installation
  source_quote: |
    "By default, TCP/IP connection are not allowed: ­ 'Enable' external TCP/IP connection" (p330)；
    "Select the 'Security' menu and enable 'mixed authentication mode' - Restart the SQL service to take modification into account" (p333)；
    "Unselect 'dynamically determine port' & put static port 1433" (p341)
  steps: |
    1. 下载：MS SQL Express 2019 在线包（microsoft.com download id=101064）或离线包（Basic 约 249MB / Advanced 约 790MB / LocalDB 约 53MB）。
    2. 安装：管理员账户运行 SQL2019-SSEI-Expr.exe（run as administrator）→ 选 Basic → 接受许可 → Install（可改目标目录）。
    3. 装 SSMS：上一步完成窗点 "Install SSMS"，或直接下 aka.ms/ssmsfullsetup（语言须与系统一致）；装完按需重启。
    4. 放行 TCP/IP：启动 SQL Server Configuration Manager → TCP/IP 默认禁用 → Enable；进 TCP/IP 属性 → IP Addresses 页签 → 检查 1433（新版默认不再分配）→ 为所有接口指定静态 1433（测试口径）。
    5. 配引擎：启动 SSMS → Connect（首次仅 Windows 认证）→ 服务器属性 → Security → 启用 mixed authentication mode → 稍后重启 SQL 服务生效。
    6. 建登录：Security / Logins → New Login（实验名 vaa）→ 允许 SQL 认证连接（测试可取消 Enforce password policy）。
    7. 建库：新建测试库，owner 设 vaa（测试口径全权限；生产按需授最小权限——多数场景只 SELECT）。
    8. 建表：Databases/<库>/Tables 建表（如 customers：callingNumber/VIP/transfertNumber）→ 编辑行插入测试记录（表动态保存，无需保存键）。
    9. 防火墙与重启：检查 Windows 防火墙——关闭或加放行 1433 入站的规则 → 重启 SQL 服务使全部改动生效。
    10. ODBC 远程验证：另一台 Windows PC → 管理工具 → ODBC Data Sources (64-bit) → Add → SQL Server → Finish → 命名驱动、填服务器 IP\SQLEXPRESS → 选 SQL Server authentication → Client Configuration → 取消"动态决定端口"、写死 1433 → 输 vaa 口令 → 选默认库 → Next → Finish → Test Data Source。
  verification: |
    ODBC 测试成功（p344 输出页）；随后可供 c18 的 JDBC 连接与 SQL 节点树使用。
  conditions: 整章为测试库搭建（实验口径 vaa/vaa）；生产应由 DBA 按最小权限交付。
  tags: [lab, mssql, ssms, odbc, database]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 22 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 Pod/OXE 基础准备 | 有 → c01 |
| task-02 安装 VAA 应用 | 有 → c02（含 c16 复用的参数差异口径） |
| task-03 OXE 侧 SIP 对接与验证 | 有 → c03（含测试树与四层排障抓手） |
| task-04 安装 Web 证书 | 有 → c04 |
| task-05 WebAdmin 初始管理 | 有 → c05 |
| task-06 公司与业务时间/日历 | 有 → c06 |
| task-07 提示音与 TTS/ASR | 有 → c07 |
| task-08 树用例 1（简单转接） | 有 → c08 |
| task-09 树用例 2（日历+过滤） | 有 → c09 |
| task-10 树用例 3（多语言菜单） | 有 → c10 |
| task-11 变量与条件 | 有 → c11 |
| task-12 收号节点 | 有 → c12 |
| task-13 显示名节点 | 有 → c13 |
| task-14 HTTP 节点 | 有 → c14 |
| task-15 邮件节点 | 有 → c15 |
| task-16 VAA HA 部署 | 有 → c16 |
| task-17 OXE 侧 HA 附加配置 | 有 → c17 |
| task-18 日常维护 | 无独立实验章。p272-295 为讲义（命令/备份/许可）；维护操作已分散嵌入 c03（排障命令）、c05（日志/SMTP）、c16（vaa services/ha 命令）。 |
| task-19 PCS/OPEX | 无实验。p300-305 为讲义（命令清单 p303 可作操作参照，但无分步实验与验收）。 |
| task-20 升级 | 无实验。p307-310 为讲义级流程（备份→install.sh→vaa.conf 核对→resync）。 |
| task-21 统计报告 | 无实验。p312-317 为讲义（报表界面浏览，无分步实验）。 |
| task-22 外部数据库集成 | 有 → c18（JDBC+SQL 树）+ c19（MS SQL Express 测试库） |

**统计**：19 条（全部 lab 型）；22 项任务中 18 项有案例类条目直接覆盖，4 项（task-18/19/20/21）为讲义内容无 How-To 实验，其操作要点已由 framework/principle 条目承载。
