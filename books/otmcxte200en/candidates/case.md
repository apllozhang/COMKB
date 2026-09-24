# 案例/实验/操作序列候选 — OpenTouch Message Center Starter (OTMCXTE200EN R2.6 Issue 08)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号）标注"实验口径"。
> 条目说明: 全书 13 个 How-To 实验章 → 13 条，与原书章节一一对应。

```yaml
- id: c01
  title: OTMC 安装（虚机创建、BIOS/ESXi 调优、SUSE 安装、core 安装）
  type: lab
  source_pages: p57-68
  source_chapter: OTMC installation (How-To) — "Pre-install the Alcatel-Lucent OpenTouch™ server"
  source_quote: |
    "Login: root • Password: OtmcV01* (default password is: letacla1)" (p60)；
    "Select 'OpenTouch Messaging Center for Virtualized Infrastructure (15000 users)' and press 'Enter' key." (p62)；
    "check the system pre-requisites by launching the 'CheckSystemLinux.sh' script from a terminal console
    (script is available at DVD root)" (p66)
  steps: |
    1. 建虚机：按 MyPortal 安装手册 otmc2.6.1_im_InstalManual_8AL90120USAH_1_en 第 6.2 章创建 OTMC-V（OS SUSE 12 64 位、1 虚拟插槽/4 核/4GB 内存/E1000 网卡/250GB 精简置备磁盘——实验口径，生产参数看手册）；前提 ESXi 已装、vSphere 客户端已连。
    2. BIOS 调优：开机按 <F9> 进 BIOS → Processor 选项禁用 hyper-threading → 保存退出。
    3. ESXi 调优：ESXi 客户端把 Power Management Policy 设为 High performance。
    4. 挂引导 ISO：vSphere 控制台右键虚机 → Power → Power On；从本地 PC 连接 boot DVD .iso；Ctrl+Alt+Ins 重启，虚机从 DVD 引导。
    5. SUSE 安装设置（实验口径）：Boot 项选 OpenTouch Messaging Center for Virtualized Infrastructure (15000 users)（另两项为硬件 GUI 版 / 单分区 OTMC first）；F2 选键盘 us 或 fr-latin1；选时区并勾 System clock uses UTC（示例 Europe/Paris）；安装约 25 分钟，完成后断开 ISO 回车重启。
    6. 改 root 密码：以 root / letacla1（出厂默认）登录，按提示把 root 密码改为 OtmcV01*（实验口径，输两遍）。
    7. 录 IP 参数（实验口径）：OTMC IP 151.1.1.60、FQDN otmc.company.com、掩码 255.255.255.0、网关 151.1.1.254、DNS 151.1.1.100；核对无误输 Yes 生成 IP 配置（参数由网络管理员提供）。
    8. core 安装：root / OtmcV01* 本地登录 → systemctl start display-manager → 登录窗口点 Not listed? 以 root 登录图形界面；挂载 OT Core .iso。
    9. 终端跑 DVD 根目录的 CheckSystemLinux.sh 检查系统前置（p66 拼写 CheckSystemLinux.sh；p53 出现 CheckSytemLinux.sh 变体，以能执行的为准）。
    10. 前置满足后跑 setup.bin：Welcome → Next；接受许可条款 → Next；向导检查服务器配置与硬件要求并给出信息摘要。
    11. Next 开始部署软件包（约 30 分钟）→ 结束出摘要屏 → 关机（重启后自动进入 post-installation wizard）。
  verification: |
    书中验收点：CheckSystemLinux.sh 检查一切正常（p66）；软件部署结束显示摘要屏（p68）；
    Note 明示重启后 POST INSTALLATION 向导自动启动并显示欢迎页（p68）。
  conditions: ESXi 基础设施与 vSphere 客户端就绪；ISO 从 BPWS 下载；RAID 与公司 DNS 需在安装前就绪（p52 Note，物理机口径）。
  tags: [lab, installation, suse, core, vm]

- id: c02
  title: Post-installation wizard（13 步站点配置）与手工装许可
  type: lab
  source_pages: p69-82
  source_chapter: OTMC Post-installation wizard (How-To) — "Complete the post-installation wizard for OTMS configuration"
  source_quote: |
    "Select 'Installation from scratch'." (p70)；
    "Hostname Enter the name of the OTMC server (lower case mandatory)" (p72)；
    "THE OK STATUS INDICATES THAT THE LOCAL FILE IS PRESENT. BUT THE CONTENT (VALIDITY) OF THE FILE IS NOT
    CONTROLLED." (p77)；
    "service flexlmd stop … service flexlmd start … ./lmutil lmstat –a" (p82)
  steps: |
    1. 首次开机自动进入向导，Welcome → Next；安装类型选 Installation from scratch → Next。
    2. 主机设置：键盘按课堂配置（qwerty/azerty）、国家、公司名 Company（实验口径）、时区+勾 D.S.T. → Next。
    3. 网络设置（实验口径）：主机名 otmc（强制小写）、IP 151.1.1.60、掩码 255.255.255.0、网关 151.1.1.254、域 company.com（小写）、DNS 151.1.1.100、NTP 151.1.1.100；DNS 选外部并填服务器；确认 DNS 已按前向+反向解析清单配置（OTMC/8770/邮件/LDAP/OXE 呼叫服务器/H.323 网关 FQDN）→ Next。
    4. HA 参数：保持 Disable（默认；启用需副服务器且两台同时跑向导）→ Next。
    5. OTMC core 设置（实验口径）：root letacla1234；maintenance 账号密码 maintenanceuser；administrator 账号密码 Admin-8770；profile 账号密码 Admin-T1；SNMP 认证/加密密码 adminsnmp；选默认语言（管理员/GUI/TUI/Conference Web）→ Next；用户名不得用 admin/adminnmc/htuser 等保留名，密码 ≥8 字符。
    6. 许可服务器：Server Type 选 Local（内嵌；External 需另填主机名/IP/域）→ Next；虚拟环境把 Aladdin USB dongle 挂到承载 FlexLM 的虚机设置里。
    7. 许可文件：Browse 选许可目录 → 勾选 .ice 文件 → Next（或 Skip 事后手工装）；注意 OK 仅代表文件存在。
    8. 证书：课堂用通用证书，Network Security Off 选 Yes（实验口径；官方警告有 toll fraud 风险）。
    9. 备份存储：选 LOCAL（实验口径；虚拟环境生产必须外置 NFS 并填 NFS Host/Path；bics.conf 落盘）→ Next。
    10. Summary 核对全部设置 → Next；System Updates 选 NO（无补丁时）→ Finish——向导启动 OpenTouch 服务。
    11. [手工装许可，p82] SFTP（otuser 账号）连 OTMC → 进 /var/data/licenses（即 $LICENSES_HOME）→ 拷入 .ice。
    12. [手工装许可，p82] service flexlmd stop → 等片刻 → service flexlmd start；到 $FLEXLM_HOME 执行 ./lmutil lmstat –a 确认许可服务器已带新文件启动。
  verification: |
    书中验收点：向导结束 "Click on 'Finish' to start the software configuration. The post-installation wizard
    starts the Open Touch services."（p81）；lmutil lmstat –a 输出确认许可加载（p82）。
  conditions: c01 已完成；许可文件（OTMC/Fax）在手；虚机 USB 控制器先在虚机设置里核验/声明（p77 Note）。
  tags: [lab, post-installation, wizard, licenses, dns]

- id: c03
  title: OmniPCX Enterprise 声明进 8770（OXE 侧准备 + 8770 声明 + 同步）
  type: lab
  source_pages: p83-89
  source_chapter: OmniPCX Enterprise declaration (How-To) — "Declare the OmniPCX Enterprise node in the OmniVista 8770"
  source_quote: |
    "Use netadmin –m command to display and update the IP configuration." (p84)；
    "DON'T FORGET TO APPLY THE MODIFICATION BEFORE TO LEAVE: 20. 'APPLY MOFIFICATION'" (p84)；
    "47xx directory – 4400 Synchro. True" (p85)；
    "Log file C:\8770\log\ NMCSyncLdapPbx_1.log" (p88)
  steps: |
    1. OXE 侧核 IP（实验口径：物理地址 csa=192.168.1.1、main 角色 csm=192.168.1.3、掩码 255.255.255.0、网关 192.168.1.254；节点名 oxe）：OXE 命令行 netadmin -m → 3.'Local Ethernet interface' → 1.'View' 核对。
    2. OXE 侧配角色地址：netadmin -m → 5.'Role addressing' → 2.'Add'，main 角色名 csm / 地址 192.168.1.3。
    3. OXE 侧配节点名：netadmin -m → 17.'Node Setup' → 2.'Update'，节点名 oxe，内部名字解析器选 n；离开前必须 20.'APPLY MODIFICATION'。
    4. OXE 侧核节点/网络号（目标：节点 101 = 子网 1 的节点 1）：mgr 工具或 OXE Webadmin → System → Review/Modify → Node Number / Network Number；用 siteid 命令或提示符 (101) 核对。
    5. OXE 侧开实时同步：System → Review/Modify → 47xx directory – 4400 Synchro = True（事件上报，8770 目录/用户自动增改的前提）。
    6. 8770 声明网络：Configuration 应用（nmc）→ 右键 Create → Network：名称 Logical-Network、网络号 1（实验口径）。
    7. 8770 声明子网：Nmc/<Network> → 右键 Create → Network：名称 ABC-Subnetwork、子网号 1（必须等于 OXE 网络号）。
    8. 8770 声明 OXE：Nmc/<Network>/<Subnetwork> → 右键 Create → OmniPCX 4400 Enterprise：名称 oxe、Subnetwork-Node number=101（=ABC×100+节点号）、IP=main 地址（空间冗余加第二地址：右键 Add a Value）、FTP 用户名/密码 adfexc（默认）、勾 Process configuration、告警接收=Permanent IP connectivity、勾 Process directory。
    9. 同步：Nmc/<Network>/<Subnetwork>/<oxe node> → 右键 Synchronization → 类型 Complete、目标 Separate → Apply → 任务参数 → Status 页签刷新日志。
    10. 核对 OXE 下生成的分支（p89 截图清单）；同步时间查节点 Configuration 页签 → Data Collection → Date of last modification。
  verification: |
    书中验收点：同步任务 Status 页签日志无错（p88）；OXE 节点下分支创建完整（p89）；日志文件
    C:\8770\log\NMCSyncLdapPbx_1.log 可查（p88）。
  conditions: OXE 基础可管理（netadmin/mgr 属 OXE 课程内容）；8770 已安装且可达。
  tags: [lab, oxe, declaration, 8770, synchronization]

- id: c04
  title: OTMC 声明进 8770 并在 OTMC 拓扑声明 OXE（bics.conf 对账 + 双向同步）
  type: lab
  source_pages: p90-101
  source_chapter: OTMC declaration (How-To) — "Declare the OTMC node"
  source_quote: |
    "OTMC information can be found in the file bics.conf on the OTMC server: [otuser@otmc ~]$ more
    /var/data/bics/bics.conf … ICE_USERNAME='otAdmin' … ICE_TEMPLATEUSERNAME='otProfile' …
    ICE_MAINTENANCEUSERNAME='otuser'" (p92)；
    "OTMC server must be declared in the same sub-network than the OXE call server." (p94)；
    "Port: 2570 (OXE PRS port number) • SIP Port: 5060 (OXE SIP port) • FTP User name: adfexc" (p99)
  steps: |
    1. 对账 bics.conf：OTMC 上 more /var/data/bics/bics.conf，记下 HOST_NAME/HOST_DOMAIN（FQDN=OTMC.company.com 口径）与 ICE 三账户（otAdmin/otProfile/otuser 及加密口令）。
    2. DNS 双向核验（OTMC 侧）：nslookup csm.company.com 与 nslookup <OXE main IP>（示例输出用 155.1.1.x 网段，实验口径；反向解析须能回名）；必要时在 DNS 服务器补 OXE FQDN 与反向记录。
    3. 密码重置（如丢失）：otAdmin/otProfile 走 WBM https://otmc.company.com/WebAdmin（otAdmin/Admin-8770 登录，实验口径）→ System services/Security/Administrator → 选账户 → Modify → Passwords 页签 → GUI Password → 填新密码 → Modify → Apply；otuser 走 root 执行 /usr/bin/musett.sh password <新密码>。
    4. DNS 双向核验（8770 侧）：Windows 客户端 nslookup otmc.company.com 与反查，确认 8770 也能解析 OTMC。
    5. 8770 声明 OTMC：nmc/<Network>/<Subnetwork> → 右键 Create → OTMC：OT 页签填 Name=OTMC、Subnetwork-Node number=98（实验口径；模板举例 99——自由号但不得与 OXE 节点号重复）、FQDN、Username/Password=otAdmin/Admin-8770、Enable notifications=True、勾 Process configuration 与 Directory Process；Connectivity 页签填 profile 账号 otProfile；Maintenance 页签填 otuser/maintenanceuser。
    6. OTMC 拓扑配网络（若 WBM 首登未自动建 OXE 节点）：8770 Configuration 选 OT 节点右键 configure → System services/Topology/OXE CS/OXE CS network → 右键 Create：Name=Logical-Network、Network identifier=1（沿用 8770 侧定义）。
    7. OTMC 拓ol配子网：System services/Topology/OXE CS/OXE CS subnetwork → Create：Name=ABC-subnetwork、identifier=1、Parent network 选上一步网络。
    8. OTMC 拓扑配 OXE：System services/Topology/OXE CS/.../OXE CS → 右键 Create：Display Name=OXE、Node FQDN=oxe.company.com、Local main role FQDN=csm.company.com、Main IP=151.1.1.3、Node Identifier=1、Port=2570、SIP Port=5060、FTP adfexc/adfexc、Enable notification 勾选、HTTP Mode=Default（实验口径）。
    9. OTMC 同步：Nmc/<Network>/<Subnetwork>/<OTMC node> → 右键 Synchronization（OTMC 节点 Partial 与 Complete 等价）→ 目标 Global（连带全量同步关联 OXE）→ Apply。
    10. 核对 OXE 节点 101 已挂到 OTMC 的 Topology 分支下（p100-101）；站点名可在 OTMC（Users and devices > Site）配置（p101 Note）。
  verification: |
    书中验收点：同步后 "the OXE attached to the OTMC is displayed under the Topology branch of the OTMC"（p100，
    示例 OXE node 101 挂载，p101）。
  conditions: c03 已完成（8770 已有 OXE 节点）；DNS 正反向解析可用；WBM 登录口令即 post-install 的 administrator 账户。
  tags: [lab, otmc, declaration, bics-conf, topology, synchronization]

- id: c05
  title: OmniPCX Enterprise SIP 配置对接 OTMC（trunk group / external gateway / trusted / codec）
  type: lab
  source_pages: p102-108
  source_chapter: OmniPCX Enterprise SIP configuration for OTMC (How-To) — "Configure the SIP settings in OXE"
  source_quote: |
    "Trunk Group ID: 1 • Trunk group name : SIP • SIP external gateway: SIP port number: 5040" (p103)；
    "Gateway Number … Remote domain: Enter the FQDN of the OTMC server • Port number: 5040 • Transport type:
    TCP … Gateway type: ICE type" (p105)；
    "The OTMC server IP address must be declared as trusted IP address." (p107)
  steps: |
    1. 建 SIP trunk group（8770 或 OXE mgr）：Trunk Groups → 右键 Create：Trunk Group ID=1（OXE 内唯一）、Type=T2、Name=SIP、Remote Network=空闲且异于 OXE 网络号、Node number=post-install 定义的节点号、Q931 Signal variant=ABC-F、T2 Specification=SIP（实验口径）。
    2. trunk 本地参数：Trunk Groups/<SIP trunk>/Trunk Group 核对 Dialing end to end=No、DTMF end to end signal=No（默认即对）。
    3. SIP 虚拟接入：Trunk Groups/<SIP trunk>/Trunk Group/Virtual accesses for SIP → Number of SIP Accesses 默认 2（可按 OXE↔OTMC 需要改）。
    4. 声明 OTMC 为 SIP external gateway：SIP/External Gateways → 右键 Create：Gateway Number、Name（如 TO OTMC）、Remote domain=OTMC FQDN、Port=5040、Transport=TCP、Belonging domain 留空、Trunk group number=步骤 1 的组号、First DNS IP=DNS 地址、SDP in 18x=False、Minimal authentication method=None、Ignore inactive/black hole=勾、Contact with IP address=勾、100 REL 出向=Supported、入向=Not requested、Gateway type=ICE type。
    5. 核对 SIP Proxy：SIP/Proxy → Minimal authentication method=None。
    6. 核对 SIP Gateway：SIP/SIP Gateway → Subnetwork number=远端网络号（同步骤 1）、Trunk Group=组号、IP/Machine name 自动带出、SIP Subscribe Min Duration=600、DNS local domain name=company.com、SIP DNS1 IP=DNS 主。
    7. 核对 SIP Registrar：SIP/Registrar → Min/Max expiry date 按需（记录最小/最大生存秒数）。
    8. 信任地址：SIP/Trusted IP Addresses → 右键 Create → 填 OTMC 服务器 IP。
    9. 编解码：System/Other System Param./Compression Parameters → Compression type=G 729、Multi. Algorithms=False。
    10. DPNSS 前缀：Translator → Prefix plan → 右键 Create（实验 D1234；用于优化经中继组的转接）。
    11. 路由优化：System → 查找 Routing Optimisation → Yes。
  verification: |
    书中本章以"参数就位"为验收（无独立呼叫测试问题）；对接效果由 c06 建户后的信箱业务测试间接承接；
    空间冗余 OXE 需按 TC1652 另配外置信箱 SIP 网关（p105 Warning）。
  conditions: c04 已完成（OTMC 已声明、拓扑已建）；OTMC FQDN 可解析。
  tags: [lab, sip, trunk-group, gateway, codec, menu-path]

- id: c06
  title: Connection 用户创建与话机开通（含 resurrection 与许可核查）
  type: lab
  source_pages: p109-118
  source_chapter: Connection user's creation for OTMC (How-To) — "Configure Connection users using the OmniVista 8770 tool"
  source_quote: |
    "Create 3 Connection users • Brad Barkley: 31000 • Billy Backman: 31001 • Betty Boop: 31002" (p110)；
    "Resurrection consists in dialing the phone directory number & the password ('0000' by default) directly,
    from the set" (p113)；
    "173 M Advanced Reflexes users = 1/ 10 … 317 M Connection IP users = 2/ 30" (p118)
  steps: |
    1. 建户（法一，OXE Configuration 接口）：OXE Configuration 界面 → 右键 Users → Create → General Characteristics 页签：Directory Number=31000/31001/31002、Directory name/First name=Brad Barkley / Billy Backman / Betty Boop（实验口径）、Set type 按实际话机选。
    2. 建户（法二，Users 应用）：Users 应用 → Users 页签 → 目录分支右键 Create user → General 页签（User type=OXE、姓名、User ID 自动、Email 可选）+ OXE 属性（OXE ID、分机号、Device type、OXE Profile 可选、SIP password 仅 SIP 终端、OXE mailbox directory number=信箱分机、OT applications=None）；注意声明 OXE 用户时设备自动创建并分配。
    3. 数字/模拟话机寻址——resurrection 法：用户参数保持 255/255/255 时空态，在话机上直拨分机号+密码（默认 0000）→ 系统自动绑定真实物理地址（示例 1-1-34）；移机场景用 In/Out of Service 前缀（先拨前缀+密码释放地址，再到新位置拨分机号+密码重新绑定；前缀用 ednump –l XXX 查）。
    4. 数字/模拟话机寻址——空闲地址法：OXE 配置界面 System > Free addresses → Configuration 页签查空闲表（示例 1 个 UA 地址 1-1-35 给 9 系、3 个 Z 地址 1-1-65/66/67 给模拟，实验口径）→ 在用户 General Characteristics 页签指派。
    5. IP 话机开通：话机断电重启，Initializing 阶段按 i 键再 # 键进主菜单 → IP Parameters：IP mode=Static、IP Addr/Subnet/Router 逐项填 → 翻页把 TFTP 设为呼叫服务器 main 地址 → 应用退出重启，等 5 个初始化阶段 → 注册：输分机号（示例 61020）+ 密码（默认 0000）→ in service。
    6. 许可核查（法一，8770）：OXE 配置工具 → System/Software package → 右键 Filter → 勾选全部用户包看占用。
    7. 许可核查（法二，OXE）：呼叫服务器 mtcl 登录 → 命令 spadmin → 选 Display active file → 读六行计数（左=已用/右=可用；实验读数 173:1/10、174:1/10、176:1/15、177:4/15、316:1/30、317:2/30，实验口径）。
  verification: |
    书中验收点：resurrection 前后 General Characteristics 页签地址从 255/255/255 变为真实地址（p114 示例 1-1-34）；
    IP 话机过 5 个初始化阶段并注册 in service（p116）；spadmin 计数器与许可族对照（p117-118）。
  conditions: c03 已完成（OXE 已被 8770 纳管）；DHCP 由网络管理员负责（书中不覆盖）。
  tags: [lab, users, resurrection, ip-phone, licensing]

- id: c07
  title: 语音邮箱配置（OTMC 账户、VMS 核验、信箱创建与分配、许可权、定制与问候语上传）
  type: lab
  source_pages: p133-145
  source_chapter: Voice mailbox configuration (How-To) — "Create and configure voice mailboxes in Local Storage voice mail system"
  source_quote: |
    "From the menu 'Services / Topology / VMS' … Select 'defaultVmLS'" (p137)；
    "Before validating the mailbox creation, it's mandatory to assign a profile to the voice mailbox" (p139)；
    "User: otAdmin / Password: Enter the password configured thanks to the post installation wizard (e.g.
    Admin-8770)" (p144)
  steps: |
    1. 建 OTMC 账户：OTMC 配置界面 → Users and devices 右键 Create → General 页签（Salutation/Login/First name/Last name，为 Brad Barkley、Billy Backman、Betty Boop 各建一个）。
    2. Contacts 页签：Directory number=31000/31001/31002（与 OXE 用户一致，实验口径）、Company e-mail=用户邮箱；Passwords 页签：TUI 密码输两遍（可选勾 Force TUI password change 首登强改）、GUI 密码输两遍；Licenses 页签：MyIC Business Communications 与 Voice mail 启用（Messaging API 可选）→ Apply。
    3. 核验：OTMC 节点 UsersAndDevices 菜单看 OTMC 用户；OXE 节点 TelephonicDevices 菜看 OXE 用户（分机号对齐即挂钩成功）。
    4. 核验默认 VMS：菜单 Services/Topology/VMS → 选 defaultVmLS → Type 应为 Local Storage（缺失则先建）。
    5. 查已建信箱与分配情况：Users and devices/Voicemail box 看信箱清单（名称/类型/VMS）；Users and devices/User → 选全部用户 → Mailboxes 页签（示例：barkley 无信箱）。
    6. 创建信箱：Users and devices/Voicemail box → 右键 Create → General 页签（Display name 如 barkleyVoiceMailBox、Type=Local Storage、Voice mail system=defaultVmsLS）→ Configuration 页签必选 profile（示例 advanced）→ 保存。
    7. 分配信箱：Users and devices/User → 选 barkley → Mailboxes 页签 → Voice mailbox 字段搜索框搜 VMB → 选中 → OK → Apply；顺带核对 Answer only 相关字段行为（由 profile 的取值决定可改性）。
    8. 许可权核查：Users and devices/User → 选 barkley → Licenses 页签 → Voice mail=Enabled。
    9. 管理员侧定制：Users and devices/Voicemail box → 选用户 → Greetings 页签（问候类型/Extended absence-on/替代问候授权）；Configuration 页签（Addressing by name/Automatic reading/Delete confirm flag/Fax number/Voice mail profile）。
    10. TUI 侧定制与测试：话机进信箱改姓名密码；把话机转信箱→留一条留言→试听；依次测试 standard/extended absence/alternative/personal 四种问候与 answer only、addressing by name（按拼写收件人名发信）、automatic reading、删除确认。
    11. 用户侧 My Profile：浏览器开 https://<OTMC FQDN> → GUI 登录 → voicemail box 菜单核对问候激活/传真号/answer only/addressing by name/automatic reading/删除确认。
    12. 问候语上传（Greeting Managers）：nmc/<Network>/<Subnetwork>/<OpenTouch 节点> → 右键 WBM → otAdmin/Admin-8770 登录 → Users and devices → Voice mail greetings management（再认证一次）→ 选用户（示例 alban）→ Upload/Activate/Download。
  verification: |
    书中验收点：信箱创建必须带 profile 才能保存（p139）；Mailboxes 页签分配后 barkley 有信箱（p140）；
    Licenses 页签 Voice mail=Enabled（p141）；TUI 测试清单逐项通过（p143）。
  conditions: c06 已完成（OXE 用户 31000-31002 已建）；otAdmin 密码=post-install 向导所设（实验 Admin-8770）。
  tags: [lab, mailbox, vms, greetings, my-profile, menu-path]

- id: c08
  title: 语音邮箱 profile 查看与新建（默认四 profile + my_profile 创建分配）
  type: lab
  source_pages: p146-152
  source_chapter: Voice mailbox profiles (How-To) — "Create a voice mailbox profile"
  source_quote: |
    "Profiles called 'Advanced', 'Classic' and 'Simplified', dedicated to Local Storage. 'Standard' profile
    is dedicated to Unified Messaging." (p147)；
    "Create a voice mail profile ('local storage' type) called 'my_profile', with the following parameters:
    … Mailbox size: 10 Mb … Aging of new messages: 15 days • Aging of saved messages: 7 days" (p151)
  steps: |
    1. 查默认 profile：/System services/Applications/Messaging/Voice Mail Profile → 应见 Advanced/Classic/Simplified（LS 用）与 Standard（UM 用）。
    2. 逐页签研读 Advanced（参数地图见 principle p14）：General（名称/类型）、Configuration 1（Answer only/Check quota/Announce time received/Skip memo/Direct callback/Callback voice prompt/Limited access/Extended absence blocks deposit/Record invitation/Keep call in system/Callback sender allowed/Propose options after deposit/beep tone/Attendant call zero-out）、Configuration 2（三时长 + TUI 密码管理三档）、Configuration 3（Max size per mailbox/Aging new/saved/Warning/Accessible via network/Accessible via IMAP）。
    3. 新建 my_profile：同路径右键 Create → 类型选 Local storage（实验口径参数：Check quota、Announce received date and time、Direct callback、Limited access、Callback sender allowed、Brief prompts for TUI、Propose options after message deposit=true；信箱 10MB；Max greeting 5 秒；Max message recording 15 秒；Max live record 15 秒；新留言保留 15 天、已存 7 天）。
    4. 分配：/Users and Devices/Voice Mail Box → 选一个信箱 → Configuration 页签确认 my_profile 出现在可选列表并选之。
    5. 行为验证：用挂 my_profile 的信箱收几条留言，核对参数符合预期（p151 验收要求）。
  verification: |
    书中验收点：Leave some messages in a voice mailbox using this profile. Check that the parameters managed
    above work as you expect（p151）。
  conditions: c07 已完成（信箱已建）；Check quota 关闭时 Max size 不生效（p150）。
  tags: [lab, profile, parameters, menu-path]

- id: c09
  title: SMTP/SMS 通知配置（全局设置、VPIM 路由、模板、用户设置、端到端验证与维护）
  type: lab
  source_pages: p183-192
  source_chapter: SMTP/SMS notifications (How-To) — "Configure SMTP/SMS notifications with OpenTouch"
  source_quote: |
    "Notification sender name: OpenTouch • Notification sender mail address: administrator@company.com •
    Maximum .wav file size (linear PCM 8bits): 2 MB • Occupancy ratio threshold (%): 80" (p184)；
    "Notifications are handled by 'Scorpio' component. To declare the SMTP server for notification to this
    component, a route has to be declared in VPIM sesssion" (p185)；
    "service chameleond status … service scorpiod status … /logs/journal/scorpio.log" (p192)
  steps: |
    1. 全局通知参数：System services/Applications/Notification/Notification → Edit：发件人名 OpenTouch、发件地址 administrator@company.com（实验口径；须为 SMTP 服务器上真实账户，与 SMS 通知共用）、SMS 网关地址（格式 SMS$手机号$@company.com，仅配 SMS 时）、Maximum audio file size=2MB（实验口径；超限发信不带附件）、Occupancy ratio threshold=80%、Audio file format 四选一（AAC/PCM16/PCM8/G.711 wav）。
    2. 声明 SMTP 服务器（VPIM 路由）：System services/Applications/Messaging/VPIM → Add：Domain name=company.com、FQDN or IP=eco.company.com、Port=25（实验口径；SMTP 须无认证无 TLS）。
    3. 定制模板（可选）：/var/data/panda/notification4 → 编辑 NotifTemplate_en_US.properties（新留言邮件正文/满箱邮件正文/新留言短信正文）；升级不覆盖旧模板，要新版模板须删旧+重启 chameleon。
    4. 用户前置：选一个持 LS 信箱的用户（Brad Barkley 等）——核验有信箱、邮箱地址已配、Voice mail 权已勾（缺信箱按 c07 步骤 6-7 补，注意最后把信箱挂到用户）。
    5. 用户通知设置：/Users and devices/Users → Notification 页签：给 Email notification right、启用 Email notification、填通知邮箱（可授权用户自改）、按需开满箱通知/wav 附件/关 MWI/My Messaging 链接（均 LS 专属）、给 SMS right 并启用 SMS、选通知手机号。
    6. 端到端验证（用户级）：向所选用户信箱留一条言，核对邮件通知（附件/链接按设置）、近满/满箱告警（可选）；端用户在 My Profile（Notification 区）自开关邮件/短信通知、改通知地址与短信目的地（可见项按管理员授权）。
    7. 维护排障：service chameleond status / service scorpiod status；日志 /logs/chameleon/chameleon/panda.log、/logs/journal/chameleon.log、/logs/journal/scorpio.log。
  verification: |
    书中验收任务：Enable SMTP notification and test the feature — Leave a message in the voicemail box of an
    user of your choice … and check the notification possibilities（p191）。
  conditions: 外部 SMTP 服务器（无认证无 TLS）与 SMS 网关（如需短信）由环境提供；模板定制后升级行为见 p186。
  tags: [lab, smtp, sms, notification, vpim, menu-path]

- id: c10
  title: IMAP 客户端收取语音邮件（Outlook 账户配置 + IMAP4 Front End 安全匹配）
  type: lab
  source_pages: p202-209
  source_chapter: Voice Messages retrieval through IMAP (How-To) — "Configure an e-mail account based on IMAP with Outlook"
  source_quote: |
    "Account type: Select 'IMAP' • Incoming mail server: Enter the OpenTouch/OTMC server FQDN (e.g:
    opentouch.company.com, otmc.company.com) • Outgoing mail server: Not used in this case, to avoid error
    notifications, enter the real mail server FQDN" (p205)；
    "The 'log onto incoming mail server (IMAP)' test should be in completed status" (p207)；
    "DON'T FORGET TO RESTART THE IMAP FRONT-END SERVICE: service imap4fed restart" (p208)
  steps: |
    1. 为 Brad Barkley（31000，实验口径）建 IMAP 账户：Windows 开始菜单/控制面板/用户账户和家庭安全/邮件 → E-mail Accounts → E-mail 页签 New。
    2. 选 Manual setup or additional server types → Next → 选 POP or IMAP → Next。
    3. 账户设置：Your Name 与 Email address 仅为标识；Account type=IMAP；Incoming mail server=OTMC FQDN（示例 otmc.company.com，实验口径）；Outgoing mail server 填真实邮件服务器 FQDN（OTMC 不做 SMTP，填 OTMC FQDN 会导致测试误报）；Username=GUI 登录名、Password=GUI 密码 → 同窗口点 More Settings。
    4. More Settings：General 页签起账户显示名；Advanced 页签选加密连接类型（必须与 OTMC 服务端一致；OTMC 默认 IMAPS+TLS）。
    5. 点 Test Account Settings：Tasks 页签中 "log onto incoming mail server (IMAP)" 必须 Completed（否则修配置）；"send test e-mail message" 失败属预期（无 SMTP 可达或误用 OTMC FQDN 作发件服务器）。
    6. Finish 完成建户。
    7. 服务端核对：OTMC 配置 System services/Topology/Physical servers/OT component/"IMAP4 Front End"：Connection security 与客户端一致；IMAP port 按安全类型自动带出；若要改用 SSL 或无加密，先在 OTMC 侧改端口号并 service imap4fed restart。
    8. Outlook 内核对：第二账户下经 IMAP 收到 LS 信箱中的全部语音消息（邮件+语音附件），账户名可改名。
  verification: |
    书中验收点：IMAP 登录测试 Completed（p207）；"you retrieve through IMAP protocol all your voice messages,
    stored in the local storage voice mail system, in the second account"（p209）。
  conditions: c07 已完成（用户有 LS 信箱且 GUI 凭证已知）；外网访问需 VPN（p198）。
  tags: [lab, imap, outlook, imaps, imap4fed]

- id: c11
  title: General announcement 配置（播报类型、用户授权、TUI 录制、wav 文件）
  type: lab
  source_pages: p224-227
  source_chapter: General announcement (How-To) — "Choose the type of announcement / Manage user's rights / Configure the general announcement / Use a wav file"
  source_quote: |
    "Only the administrator is allowed to select the type of announcement by using the 8770. 3 choices are
    available (one of the 4 existing choices is not more used: on AA)." (p225)；
    "Record the following message as general announcement: 'Welcome to OpenTouch training session' … the
    general announcement is available (Choice 6)" (p226)；
    "Rename it with the following name: « general_announcement.wav » … Once the wav file is stored in the
    dedicated directory, the announcement is enabled." (p227)
  steps: |
    1. 定播报类型（仅管理员，8770）：/System services/Applications/Telephony/Vocal applications/TUI global configuration → 勾播报场景：Is played for external callers / Is played for internal callers / Is played for calls in message consultation（可多选；"arrive on AA" 已废弃勿选）。实验任务：配置为"用户查询信箱时播放"。
    2. 授权用户：OT configuration/Users and devices/User → 选 Barkley → 勾 "User has right to manage the general announcement"（允许其经信箱录制/试听/停用）。
    3. TUI 录制验证：Barkley 话机登录信箱 → 增强主菜单选 6（General Announcement）→ 子菜单 2 录制 "Welcome to OpenTouch training session"（实验口径文案）→ 录完自动激活；子菜单 1 试听、3 停用。
    4. wav 文件方式：向讲师取一个格式正确的 .wav；经 SFTP/文件浏览器传到 OTMC 系统目录（p227 演示路径 /var/data/ics-group/general_announcement；p223 记述为 /var/data/general_announcement——两处口径见 counter-example）→ 改名 general_announcement.wav（格式 CCITT A-law 8bits 8kHz mono）→ 文件就位即启用；停用=删除 wav 或经 TUI。
    5. 复测：按所配播报场景呼叫/查询，确认公告先于问候语/信箱菜单播放。
  verification: |
    书中验收点：用户信箱菜单出现 General Announcement（Choice 6）且可录/听/停（p226）；wav 就位后 announcement
    is enabled，测试特性生效（p227）。
  conditions: c07 已完成（用户有信箱与 TUI 密码）；wav 语言支持口径见 p223。
  tags: [lab, general-announcement, tui, wav]

- id: c12
  title: OpenTouch 备份与恢复（目录配置、备份参数、执行备份、删用户-恢复验证、手工起服务）
  type: lab
  source_pages: p239-246
  source_chapter: OpenTouch Backup & Restore (How-To) — "Save & Restore OpenTouch Data"
  source_quote: |
    "Backup location: Enter the directory path (C:\8770_ARC\OTBackup by default)" (p240)；
    "Warning DON'T DELETE THE USER ALAN ALBAN FROM THE USERS APPLICATION! IF YOU DO SO, THE VIRTUAL SIP DEVICE
    WILL BE DELETED FROM THE OXE!" (p243)；
    "Enter the command service opentouchd start in order to restart the OpenTouch services" (p245)
  steps: |
    1. 配默认备份目录：Maintenance 应用 → Preferences → Maintenance >OT Configuration：Backup location（默认 C:\8770_ARC\OTBackup；指向其它计算机需在 8770 侧专项配置）；阈值（控制类型=可用空间或归档量、单位 %/kB/MB/GB、两级阈值对应次要/主要告警）；Record Life（天/月；超期备份由 Scheduler 每日清理）。
    2. 配备份参数：Configuration 应用 → 选 OpenTouch → Maintenance 页签：勾 Automatic database save、Username maintenance=otuser、Password maintenance（实验示例 superuser）。
    3. 执行备份：Maintenance 应用 → Operations → 双击 OT 节点 – Backup → 选 All OT data → Simple job → 选 Now（或 As Scheduled：起止时间/频率）→ 确认 → 出结果。
    4. 恢复验证准备：从 OT Configuration 窗口删用户 Alan Alban（警告：绝不能从 Users 应用删——会把虚拟 SIP 设备从 OXE 删掉）。
    5. 执行恢复：Maintenance → Operations → 双击 OT 节点 – Restore → 选 All OT data → Search 选备份目录（示例 20141205153703）→ OK → 执行；跨版本恢复（旧版备份→高版本系统）勾 Force；三步进度（传包→停服务并恢复→Action completed）。
    6. 核对 Alan Alban 已恢复。
    7. 手工起服务：Configuration 应用 → 右键 OpenTouch → Connect（SSH，otuser/maintenanceuser 登录，实验口径）→ su - 输 root 密码（实验 superuser）→ service opentouchd start（<5 分钟）。
  verification: |
    书中验收点：恢复后 "Check that the user Alan Alban has been restored"（p243）；服务重启后 OpenTouch 可用
    （重启耗时 <5 分钟，p245 Tips）。
  conditions: c04/c05 后系统有数据可备份；虚拟环境备份目录须外置 NFS（p79）；8770 上 NFS server 部署按 TC2024（p246）。
  tags: [lab, backup, restore, maintenance, 8770]

- id: c13
  title: 语音信箱统计启用（statistics.properties 配置与验证）
  type: lab
  source_pages: p255-258
  source_chapter: Voicemail statistics (How-To) — "Enable and generate the voicemail statistics"
  source_quote: |
    "Such File is available in the following path: '/var/data/ics-group/vms/ngvm3/'" (p256)；
    "enableStatistics = enabled … fileLocation = /var/data/ics-group/vms/statistics … dayGeneration = tuesday
    … timeGeneration = 15:35:00" (p257)；
    "Once the 'statistics.properties' file has been modified, don't forget to stop and start the masc
    service." (p258)
  steps: |
    1. 定位配置文件：/var/data/ics-group/vms/ngvm3/statistics.properties（参数以 # 注释+加粗参数呈现）。
    2. 通读默认配置（默认值全集见 principle p23）：enableStatistics=disabled 等。
    3. 按实验任务改配置（实验口径）：enableStatistics=enabled；enableStatisticsGeneration=enabled；fileLocation=/var/data/ics-group/vms/statistics；timeUnit=default；frequencyGeneration=day；dayGeneration=tuesday；timeGeneration=15:35:00。
    4. 手工创建输出目录 /var/data/ics-group/vms/statistics 并确认读写权限（Note 明示必须先建、注意权限）。
    5. 重启 masc 服务：service mascd stop → service mascd start。
    6. 到生成时刻后检查输出目录中的统计文件（XML/HTML/CSV 按配置），核对统计项（登录名/电话号码/信箱 ID/信箱状态/留言总数/新留言/已听/已归档/已删）。
  verification: |
    书中验收任务：Generate some voicemail statistics according to the following settings（p257）；输出文件按
    配置频率落在指定目录（p251 讲义 + p258 操作链）。
  conditions: c07/c08 后系统内有信箱数据可统计；freshness/frequencyGC 决定删除数据保留与清理节奏（p256）。
  tags: [lab, statistics, properties, mascd]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 18 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 部署形态与容量口径决策 | 无实验。概念章（p3-20），容量规划工具仅演示场景图（p19），无分步操作。 |
| task-02 搭建实验拓扑 | 无 How-To 章。p21-32 为拓扑描述页（六虚机 IP/账号表），书中未给搭建步骤（ESXi/虚机安装属课前准备）。 |
| task-03 许可证体系部署 | 有 → c02 步骤 6-7、11-12（向导装许可+手工装许可）；许可原理与文件说明为讲义（p33-45）。 |
| task-04 OTMC 服务器安装 | 有 → c01 |
| task-05 post-installation wizard | 有 → c02（步骤 1-10） |
| task-06 手工装/换许可 | 有 → c02（步骤 11-12，p82 专节） |
| task-07 OXE 声明进 8770 | 有 → c03 |
| task-08 OTMC 声明与拓扑对置 | 有 → c04 |
| task-09 OXE SIP 对接 | 有 → c05 |
| task-10 Connection 用户与话机 | 有 → c06（含 resurrection、IP 话机、双法许可核查） |
| task-11 账户与信箱交付 | 有 → c07 |
| task-12 profile 定制 | 有 → c08 |
| task-13 自助门户 | 部分覆盖 → c07 步骤 11（My Profile 定制入口）；p153-166 为讲义导览章，无独立 How-To，用户自助动作散嵌在 c07/c09/c10。 |
| task-14 SMTP/SMS 通知 | 有 → c09 |
| task-15 IMAP 访问 | 有 → c10 |
| task-16 general announcement | 有 → c11 |
| task-17 备份恢复 | 有 → c12 |
| task-18 语音信箱统计 | 有 → c13 |

**统计**：13 条（全部 lab）；18 项任务中 12 项有对应 How-To 章，task-01/02 为概念/拓扑章无实验，task-13 的门户操作散嵌于 c07/c09/c10（原书 web clients 章为界面导览，无独立实验）。
