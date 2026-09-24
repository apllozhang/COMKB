# 原则/清单/规则/公式/数值口径候选 — OmniVista 8770 (8770XTE200EN Ed47)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: 服务器 OS 与硬件双档要求（<5000 / >5000 用户）
  type: metric
  source_pages: p55-56
  source_chapter: SERVER INSTALLATION / Operating Systems & Hardware requirements
  source_quote: |
    "Windows 2016 Server Standard or Datacenter Edition (64 bits) X X ... Windows 2025 Server
    Standard or Datacenter Edition (64 bits) X X ... The OmniVista 8770 Server must be installed
    on a dedicated server" (p55)
    "Processor Dual-Core (frequency near 2 GHz ...) / Processor Quad-Core (frequency near 2,2
    GHz ...) Processor architecture equivalent or superior to Haswell required / RAM (minimum)
    6 GB 7 GB (with Manage My Phone license) 8 GB 9 GB (with Manage My Phone license) /
    Minimal characteristics of Hard Disk 120 GB 120 GB (disk: RAID5), 15K RPM / Graphic board
    128 MB" (p56)
  summary: |
    OS：<5000 用户可用 Win10/11 Pro&Ent 64 位或 Win2016/2019/2022/2025 Server；>5000 用户仅
    Server 系列（2016/2019/2022/2025）。硬件：<5000 档双核约 2GHz + 6GB（含 Manage My Phone 许可
    7GB）+ 120GB + 显卡 128MB；>5000 档四核约 2.2GHz + 8GB（含 MMP 9GB）+ 120GB RAID5 15K RPM；
    CPU 架构须 Haswell 及以上。服务器必须独占（dedicated）。浏览器口径：IE11（仅 Directory web
    client 与 MMP）、Firefox 140.0.4+、Chrome 138.0.7204.158+、Edge 138.0.3351.95+（WBM/目录/MMP）。
  conditions: R5.2 时点值；虚拟机同物理机要求（p8）
  tags: [metric, sizing, hardware]

- id: p02
  title: 虚拟化平台清单与"免虚拟化许可"口径
  type: rule
  source_pages: p8
  source_chapter: SOLUTION OVERVIEW / Virtualization
  source_quote: |
    "Hypervisors: VMware ESXi (6.x, 7.0 and 8.0), Microsoft Hyper-V® 2016, 2019, 2022, Nutanix
    AHV (20220304), ASW (Amazon Web Services) ... No OmniVista 8770 license for virtualization
    ... According to the different hypervisors, some complementary services may require
    additional license costs" (p8)
  summary: |
    8770 虚机可跑在 VMware ESXi 6.x/7.0/8.0、Hyper-V 2016/2019/2022、Nutanix AHV（build 20220304）、
    AWS 上；虚拟机与物理机要求相同；虚拟化本身不收 8770 许可，但部分 hypervisor 互补服务可能产生
    额外许可成本。容量规划用 OmniVista 8770 Capacity Planning tool V3.0 灵活定虚机参数。
  conditions: 部署形态二选一：客户本地单 Appliance 或数据中心托管大市场
  tags: [rule, virtualization, licensing]

- id: p03
  title: 跨版本兼容矩阵——OXE Purple 代次决定可用 8770 版本
  type: metric
  source_pages: p9
  source_chapter: SOLUTION OVERVIEW / Cross compatibility
  source_quote: |
    "OmniPCX Enterprise OXE R12.2 to R12.4 X X X X / OXE Purple R100 (N1) X X X / OXE Purple
    R100.1 (N2) X X / OXE Purple R101.0 (N3), R101.1 (N4) & R101.2 (N5) X / OXO Connect / OCE
    R4.0 X X X X / OXO Connect / OCE R5.0 to R5.1 X X X / OXO Connect / OCE R5.2 to R6.2 X X" (p9)
  summary: |
    兼容结论：OpenTouch BE/MS/MC R2.4-R2.6.1 与 OXE R12.2-R12.4 支持 8770 全系（R4.2-R5.2）；
    OXE Purple 按代次收窄——N1（R100）支持到 R5.1、N2（R100.1）从 R5.0 起、N3/N4/N5（R101.0/101.1/
    101.2）仅 R5.2；OXO Connect/OCE R4.0 全支持、R5.0-5.1 从 R5.0 起、R5.2-6.2 仅 R5.1/R5.2。
    选型判断：新代 OXE 必须配新 8770；R5.2 是覆盖面最广的版本。
  conditions: Ed47 时点矩阵；升级前以此表核对双侧版本
  tags: [metric, compatibility, versioning]

- id: p04
  title: 8770 服务器命名与网络参数规则（装后难改项清单）
  type: checklist
  source_pages: p58, p67, p77, p79
  source_chapter: SERVER INSTALLATION / Server settings & Notes
  source_quote: |
    "The computer name is the name of the OmniVista 8770 Server. It must: - Be less than 15
    characters - Start with a letter - Not include characters such as / \ [ ] " : ; | < > + =
    , ? * . _" (p67)
    "The HTTP and HTTPS ports can't be modified for compatibilities reasons. All ports used by
    8770 are automatically configured in the Windows firewall. ... This parameter cannot be
    modified after server installation." (p77)
  summary: |
    安装前定案清单：①计算机名 <15 字符、字母开头、不含 / \ [ ] " : ; | < > + = , ? * . _；
    FQDN=计算机名.DNS 后缀（nms.company.com 实验口径），三者装后可改但走 rehosting 流程；
    ②IP 静态 + TCP/IPv4 + 网关；③默认端口 Apache 80 / HTTPS 8443 / LDAP 389 / LDAPS 636 /
    Wildfly 8080，HTTP/HTTPS 端口不可改；④公司名装后不可改；⑤成本中心方式（PCX cost center
    Yes/No）装后不可改（选 No 才能用 >10 字符成本中心名）；⑥目录管理器登录名不可改否则安装失败；
    ⑦邮件服务器 IP/FQDN 装后可改。以上存档于 C:\8770\RestoreContext.ini（svNMCName/svDomain/
    svPortApache/svPortHttps/svServerPort/svPortLDAPS/svPortWildfly/bCostCenter/nmcVersion 等）。
  conditions: 修改计算机名/DNS 后缀需重启；改 IP/FQDN 走备份+rehosting 恢复（f20）
  tags: [checklist, installation, naming, ports]

- id: p05
  title: 安装期账户与初始密码体系（四账号同密 + dba/sql + 85% 内存门槛）
  type: metric
  source_pages: p74, p77
  source_chapter: SERVER INSTALLATION / Notes
  source_quote: |
    "Do not modify the directory manager login or installation may fail. Enter the password
    (8 characters minimum) for the directory manager account. All the following accounts will
    have the same password: Adminnmc ... Admin (LDAP Directory Administrator) ... MSAD8770Admin
    ... Thirdparty8770Admin" (p77)
    "The 'Database administrator login' is dba (read only). The password is sql. It can be
    modified by the ToolsOmniVista.exe application. ... The memory usage must be less than 85%
    to install the 8770 server." (p77)
  summary: |
    初始账户：directory manager（登录名固定，密码 ≥8 字符，实验口径 superuser）与 AdminNmc、Admin、
    MSAD8770Admin、Thirdparty8770Admin 共用同一初始密码；首次登录 AdminNmc 强制改密（实验口径
    Superuser01*）。数据库管理员 dba 只读、默认密码 sql，用 ToolsOmniVista.exe 改。安装门槛：内存
    占用 <85%。安装日志 C:\Users\Administrator\AppData\Local\Temp\OmniVista8770_report.log；许可文件
    *.sw8770 装后存 8770\etc 改名 nmc.license。
  conditions: 所有明文密码为实验口径；生产必须逐账户改密
  tags: [metric, accounts, installation]

- id: p06
  title: 补丁安装与核验口径（patches 目录 + 双 ini 文件）
  type: checklist
  source_pages: p63, p78-79
  source_chapter: SERVER INSTALLATION / Patches installation
  source_quote: |
    "Paste the patches to be installed in the C:\8770\install\patches directory. ... Right click
    on the PatchInstaller.exe file, select Run as administrator ... It should contain the
    following message at the end of the file: Patch installation terminated: success" (p78)
  summary: |
    补丁三步+两档核验：拷补丁到 C:\8770\install\patches → 管理员运行 PatchInstaller.exe →
    C:\8770\install\Patch_Installer.log 尾部出现 "Patch installation terminated: success" 即成功；
    已装清单查同目录 Patch_history.ini（含版本与补丁字母序列）。RestoreContext.ini 中的 nmcVersion
    随补丁/升级更新，是恢复版本绑定的依据。
  conditions: Windows 10/11 上运行安装程序需"以管理员身份运行"
  tags: [checklist, patch]

- id: p07
  title: Windows 前置两件套——IE ESC 关闭 + Defender 排除 C:\8770（Alarms/Topology 前提）
  type: rule
  source_pages: p80-83
  source_chapter: Server installation / Windows Server 2022 management
  source_quote: |
    "Internet Explorer Enhanced Security management option must be deactivated." (p80)
    "The 'C:\8770' folder must be excluded to Windows Defender scanning process." (p81)
    "Both Windows managements are required to enable Alarms and Topology applications." (p83)
  summary: |
    服务器装完 8770 后、启用前必做两项 Windows 管理：Server Manager > Local Server 关闭 IE ESC
    （Administrators 与 Users 都设 Off）；Defender > 病毒和威胁防护 > 排除项添加文件夹 C:\8770。
    书中明确这两项是 Alarms 与 Topology 应用能启用的前提——漏做时告警/拓扑无告警可收。
  conditions: 2022 与 2019 章口径一致（p634-637）
  tags: [rule, windows, prerequisites]

- id: p08
  title: 客户端安装硬门槛（本地管理员权限 + 750MB 磁盘 + Zulu 模块放行 + WMIC）
  type: checklist
  source_pages: p92-93, p98-102, p104-106
  source_chapter: CLIENT INSTALLATION（讲义 + How-To）
  source_quote: |
    "Free disk space: OV8770 client cannot be launched if the space in the memory size is below
    750 MB. It's the minimum required memory space to run JVM application" (p93)
    "Ensure the Windows account used for the installation has administrator privilege (local
    administrator account)." (p98)
    "In Windows 11 build 22572 (22H2), WMIC utility (command line interface), used to run 8770
    client application, is now deprecated." (p104)
  summary: |
    客户端四门槛：①Windows 10/11 Pro/Ent 64 位，Intel Core 2GHz / 4GB RAM / 40GB 硬盘 / 剩余空间
    ≥750MB（低于则 JVM 无法启动）/ 显卡 4MB 1024×768；②安装与运行需本地管理员权限；③首次连接时
    Windows Defender 防火墙拦截 Zulu Platform x32 Architecture 模块，必须在专用网络放行；④Win11
    build 22572（22H2）起 WMIC 被弃用，需 Settings > System > Optional features 装回 WMIC 可选功能。
    无 DNS 时在 C:\WINDOWS\System32\drivers\etc\hosts 加 "<服务器IP> <服务器名> <FQDN>"。
  conditions: 客户端与服务器 LDAPS 636 连通；连接配置存 C:\Users\<账户>\nmc5_5.2.cfg
  tags: [checklist, client, prerequisites]

- id: p09
  title: 节点号换算公式——声明节点 = OXE 网络号×100 + 节点号
  type: formula
  source_pages: p112, p123, p658
  source_chapter: NODE REGISTRATION（讲义 + How-To）& OXO Connect declaration
  source_quote: |
    "Free number = OXE network nb *100 + OXE node nb = OXE network number" (p112)
    "Subnetwork – Node number: Enter a numeric value equal to the OmniPCX Enterprise network*100
    + OmniPCX Enterprise node number. Example: With a network number = 1 and node number = 2,
    you must enter 101" (p123)
    "the OmniVista 8770 server converts it in a declaration node applying the following rule:
    (Subnetwork number X 100) + OXO Connect node number. ... (1x100) + 80 = 180" (p658)
  summary: |
    两个公式：(1) OXE 声明节点号 = OXE 网络号×100 + OXE 节点号（声明时子网号须等于 OXE 网络号），
    该值必须与 OXE 侧 siteid 输出一致；(2) OXO Connect 声明节点号 = 子网号×100 + OXO 节点号
    （例 1×100+80=180），该值同时决定 OXO 备份目录 C:\8770_ARC\OXO\data\<网络>\<子网>\<声明节点>。
  conditions: 空间冗余 OXE 需登记两个主用 IP（IP 字段右键 Add a Value）
  tags: [formula, node-registration, numbering]

- id: p10
  title: 同步四象限语义——Complete/Partial × Separate/Global
  type: rule
  source_pages: p114, p125
  source_chapter: NODE REGISTRATION / Synchronization
  source_quote: |
    "Complete synchronization: Retrieve all technical data from the PCX / Partial
    synchronization: Retrieve data changed since the last synchronization for the following
    entries: Users, Directory, Data terminals, Speed dial numbers, Remote users. Other entries
    are systematically retrieved" (p114)
    "Separate: the selected OXE is synchronized / Global: the selected OXE and associated
    OpenTouch are synchronized." (p125)
  summary: |
    同步矩阵：Complete=全部条目无视上次同步时间重取；Partial=仅 Users/Directory/Data terminals/
    Speed dial numbers/Remote users 五类按变更时间增量取，其余条目总是全取；Separate=只同步所选
    OXE；Global=所选 OXE 连同关联 OpenTouch 一起同步。标准初始化动作为 Complete > Separate；
    日常变更用 Partial。执行窗内 OK=后台跑，Apply=前台看进度。
  conditions: 同步日志 C:\8770\log\NMCSyncLdapPbx_1.log；最后同步时间在 OXE Data Collection 页
  tags: [rule, synchronization]

- id: p11
  title: OXE 实时同步排障入口——重启 NMC Alarm server 服务
  type: checklist
  source_pages: p127-128
  source_chapter: OXE node registration / Checking the Real Time Synchronization & Troubleshooting
  source_quote: |
    "Create a user 31234 ... Open the Alarms application and select Event tab ... The date and
    origin of the event received by the 8770 server can be found in the file:
    C:\8770\log\NMCFaultManager_1.log" (p127)
    "If the real-time synchronization doesn't work, perform the following actions: Restart NMC
    Alarm server service: Start -> OmniVista 8770 -> Tools -> Service Manager ... Stop NMC Alarm
    server service. It will automatically restarted." (p128)
  summary: |
    实时同步核验三步：OXE 侧建用户（如 31234）→ Alarms 应用 Event 页收到事件（mgr 建的 hostname 显
    MANAGER，8770 建的显 8770 服务器名）→ Configuration 树 TelephonicDevices 出现该用户。排障：Service
    Manager 中停止 NMC Alarm server 服务（自动重启），再建用户复测。日志佐证：NMCFaultManager_1.log
    （事件）与 NMCSyncLdapPbx_1.log（订阅者创建处理）。
  conditions: 事件 OSI 行含 EvType/Sev/ProbCause 与 AddInfo（来源标识）
  tags: [checklist, troubleshooting, real-time-sync]

- id: p12
  title: OXE netadmin 关键菜单路径（角色地址/SSH 核查/可信主机）
  type: checklist
  source_pages: p119-120, p130-131, p135-136
  source_chapter: OXE node registration & OXE SSH (How-To)
  source_quote: |
    "Enter the command siteid ... Node number: 1 ; Network number: 1 ;" (p119)
    "Select option 5: Role addressing ... Select option 1: View ... | local main | Ethernet |
    csm | 192.168.1.3 |" (p120)
    "Select option 11: Security → Select option 1: Firewall (iptables) Configuration → Select
    option 3: Restricted Access Configuration → Select option 1: View trusted hosts" (p131)
  summary: |
    OXE Call Server 命令菜单地图：siteid 显示节点号/网络号/告警继电器状态；netadmin -m 主菜单——
    选 2 Show current configuration（SSH 是否启用、接口地址表）；选 5 Role addressing（1 View 查看
    主用角色 IP）；选 11 Security → 1 Firewall (iptables) → 3 Restricted Access Configuration →
    1 View / 2 Add a trusted host（输名→y 入 hosts 库→输 IP）→ 返回主菜单选 22 Apply modifications →
    0 退出。辅助：netstat -an | grep :22（SSH 监听）/ grep :23（telnet 应无输出）。
  conditions: 均需 su - 提权（实验口径密码 Superuser2580*）；改动必须 Apply 才生效
  tags: [checklist, oxe, netadmin, ssh]

- id: p13
  title: SSH 信任策略代际差异——OXE N2 前默认 telnet，N3 起强制可信主机
  type: rule
  source_pages: p110, p132
  source_chapter: NODE REGISTRATION / PCX connectivity & OXE SSH Notes
  source_quote: |
    "Telnet or SSH (SSH mandatory from OXE R101)" (p110)
    "Until OXE N2, telnet protocol is enabled and SSH is disabled by default. ... Since OXE N3,
    SSH protocol is enabled by default and the management of trusted hosts is mandatory." (p132)
  summary: |
    规则：OXE N2（R100.1）及以前出厂默认 telnet 开、SSH 关，SSH 需经 netadmin 启用（可信主机可选）；
    OXE N3（R101.0）起 SSH 默认启用且可信主机管理强制——8770 服务器与所有管理终端都要进可信清单，
    且路由器/SIP 网关/GD/INTIP 板/IP 话机等所有 IP 设备都要配置（可配网段范围，如话机段）。
  conditions: 8770 与 OXE 间 CMISE 配置 + Telnet/SSH 维护均受此约束
  tags: [rule, ssh, security, oxe]

- id: p14
  title: OXE profile 生效双前提——自动识别开关 + Profile 名称大写
  type: rule
  source_pages: p183-184, p190
  source_chapter: Users application - OXE user creation (How-To)
  source_quote: |
    "Browse to System > Other System Param. > System Parameters, Select Use profile with auto.
    recognition ... This parameter allows creating a user from a profile." (p183)
    "Profile Name Define the name of the profile that will be displayed in the Users application
    (i.e. BASIC). Profile Name must be in upper case." (p184)
    "Warning: THE 'USE PROFILE WITH AUTOMATIC RECOGNITION' MUST BE SET IN ORDER TO MAKE THE KEY
    PROFILES WORK." (p190)
  summary: |
    两条硬规则：(1) OXE System > Other System Param > System Parameters 的 "Use profile with auto.
    recognition" 必须勾选，用户 profile 与 key profile 才能工作；(2) Profile 名称必须全大写（如
    BASIC、PROFILE_8068S），否则 Users 应用看不到。附加口径：profile 用户的 Rights 三 COS（Public
    Network/Phone Feature/Connection）在 Rights 页设；All 页可设约 20 项继承默认值（成本中心、话务台
    ACD、语言、信箱类型等）；profile 用户默认不显示，需 Filter "Set Function = Profile"。
  conditions: key profile 检索回 8770 需同步一次（p194 Warning）
  tags: [rule, profiles, oxe]

- id: p15
  title: Meta profile 取号规则——空闲号码段首个可用号 + 建段必同步
  type: rule
  source_pages: p204-207
  source_chapter: Meta profiles for OXE users (How-To)
  source_quote: |
    "During the OXE user creation via a meta profile, the first available free number of the
    range can be selected as the directory number associated to this user" (p204)
    "Warning: SYNCHRONIZATION IS REQUIRED TO RETRIEVE THE FREE NUMBER RANGES FROM THE OMNIPCX
    ENTERPRISE!" (p205)
    "OXE free number range Select a free number range ... The user directory number is the first
    available number from the free number range" (p207)
  summary: |
    流程规则：OXE 配置界面 System > 1 > Free Numbers Ranges List 建号段（名称/起 31050/止 31059/
    仅数字）→ 必须同步（Partial > Separate）8770 才可见 → Users 应用 Profiles 页建 Meta profile
    （名称 + OXE 节点 + 号段 + 设备类型 + OXE profile 可选 + Key Profile 可选 + SIP 密码规则（设备为
    SIP 时选"=分机号"或随机）+ 邮箱号（选了 OXE profile 时不可用）+ 成本中心（覆盖 profile 值）+ OT
    应用选 None）→ 建户时选 meta profile 自动填 OXE 属性并取段内第一个空闲号。
  conditions: 手工指定号码需在导入文件 oxeDirectoryNumber 字段填值（p222）
  tags: [rule, meta-profile, numbering]

- id: p16
  title: 批量开通文件字段语义（thick client XXXX/NULL 与 WBM +;-# 体系）
  type: rule
  source_pages: p214-216, p221-222, p258-259
  source_chapter: Mass provisioning（讲义 + How-To）& WBM provisioning
  source_quote: |
    "No use to import a file with full header. UID used to identify user(s) to be modified" (p214)
    "Personal and mandatory attributes which can't be provided by the Profile or Metaprofile
    replaced by XXXX ... Attributes that can be automatically computed from Profile or
    Metaprofile set to NULL" (p216)
    "Action[+;-;#] Replace the # by the + character, to add a new user. ... secretCode@details
    Replace the starts string by NULL. After importing the updated file, the new user will be
    created with a default secret code (i.e. 1234)" (p259)
  summary: |
    thick client 文件语义：action[ADD;MODIFY;DELETE]（模板导出默认 ADD，全参导出为空白）；XXXX=
    必填人工填（姓名等），NULL=可由 profile/metaprofile 自动计算（可覆盖）；改现有用户必须带 UID。
    WBM 文件语义：Action[+;-;#]，导出原样为 #（更新用）、+ 新增、- 删除；secretCode 填 NULL 则新用户
    用默认密码 1234。两套文件互不通用（n22）。导入核验：thick client 看 Scheduler 任务绿态与 ADD 成功
    日志；WBM 看 Activity report。
  conditions: 用 meta profile 建的用户导出模板表头最少；仅 profile 建的表头更多、需填更多参数（p217）
  tags: [rule, mass-provisioning, file-format]

- id: p17
  title: WBM 批量边界——四设备页签上限 + 不能移除设备/OT 应用
  type: limitation
  source_pages: p240-241, p250
  source_chapter: WBM Users provisioning（讲义）
  source_quote: |
    "Device tab available once added. 4 Devices tabs maximum ... ALES-Desktop and ALES-Mobile
    tabs available once selected. Included on the 4 Devices tabs maximum limit" (p240-241)
    "Limits comparing to 8770 thick client: Can't remove devices from users. Can't remove OT
    applications from Connection users. Mass provisioning file generated from thick client
    cannot be used in WebAdmin and vice-et-versa" (p250)
  summary: |
    WBM 建户上限与红线：每用户最多 4 个设备页签（ALES-Desktop/ALES-Mobile 软终端计入 4 个上限）；
    批量文件只能增改、不能移除已有用户设备、不能移除 Connection 用户的 OT 应用；thick client 与
    WBM 的批量文件互不通用。导出模板只落 Windows 登录用户下载目录；计划导出只能整支导出（选中用户
    不可排程）。
  conditions: WBM Users 需 Unified Management 许可
  tags: [limitation, wbm, mass-provisioning]

- id: p18
  title: Manage My Phone 能力边界（两语言 + 20 OXE/100 并发 + 机型清单）
  type: metric
  source_pages: p261-268
  source_chapter: Manage My Phone（讲义）
  source_quote: |
    "Application available on Internet Explorer, Google Chrome and Mozilla Firefox. Application
    only available in two languages (French and English) ... Graphical view available for IP
    Touch (80X8/40X8) and TDM (80X9/40X9) with or without Add-on modules. Access to Manage My
    Phone application submitted to license. 20 OXE and 100 simultaneous connections. .Net
    Framework 4.0 is minimum version supported" (p268)
  summary: |
    MMP 终端自助（https://<FQDN>:8443 > MANAGE MY PHONE）：功能=语言选择/密码码重置/锁机解锁/免打扰/
    呼转与目的地/IP·TDM 话机可编程键（耳机键、程控键）；入口经 8770 网页、终端用户邮箱登录。硬边界：
    仅法语英语两语言；图形视图仅 IP Touch 80X8/40X8 与 TDM 80X9/40X9（含 Add-on）；许可口径 20 个
    OXE + 100 并发连接；服务端 .Net Framework ≥4.0；需 Manage My Phone 许可。
  conditions: 所有 Connection 用户兼容 MMP（p268）
  tags: [metric, manage-my-phone, licensing]

- id: p19
  title: 告警六级色标与处置动作矩阵（确认/清除/删除/签名）
  type: rule
  source_pages: p274, p276-280, p293-295
  source_chapter: Alarms application（讲义 + Functionalities How-To）
  source_quote: |
    "Critical Red / Major Orange / Minor Yellow / Warning Blue / Indeterminate Purple / Cleared
    White" (p274)
    "Acknowledging an alarm: Only active alarms can be acknowledged. Once acknowledged, alarm
    still active ... Clearing an alarm: Only uncorrelated alarms may be cleared. Once cleared,
    alarms becomes inactive" (p278-279)
    "Signature and action are headers available in alarm report. Remarks are not displayed in
    alarm report." (p295)
  summary: |
    严重级色标：Critical 红/Major 橙/Minor 黄/Warning 蓝/Indeterminate 紫/Cleared 白；客户端常显计数器
    框色=当前最高级。处置矩阵：确认（acknowledge）仅限活动告警、确认后仍活动并记录人名；清除（clear）
    仅限非相关告警、清除后转不活动入历史；删除从库移除（选中层级及其子层全删）；签名（Signature）+
    动作（Action）进告警报告表头，Remark 不进报告。历史/活动显示经图标切换；过滤器一键开/关。
  conditions: 相关告警由 PCX 自动清除（p277）；告警字典字段可改名（n34）
  tags: [rule, alarms, workflow]

- id: p20
  title: OXE incident 上送控制参数（Network severity / Topological network / Incident filter）
  type: rule
  source_pages: p285-288
  source_chapter: Alarms application - OXE (How-To)
  source_quote: |
    "Network severity Minimum severity above which the incidents are transmitted to the
    OmniVista 8770 server unless an incident filter requests otherwise. Topological network
    Specify if topological incidents are transmitted or not" (p285)
    "Incident Number Specify incidents identified by their number and their geographic situation
    ... Network incident Yes/No. Specify if the incident must be transmitted to the OmniVista
    8770 irrespective of the network severity filter" (p288)
  summary: |
    上送控制三件套：①Network severity（实验设 None=全量上送）——低于该级别的 incident 不送 8770；
    ②Topological network=YES 上送拓扑类事件；③Incident Filter（Applications > 1 > Incident Manager
    > 1 下右键 Create）按事件号定向强制上送：Network incident=Yes 时无视 Network severity。核验手法：
    rstcpl <MG> <板> 重启 coupler 触发 #2042（Major），mtcl 登录触发 #1125（Minor）；incvisu -t 3 查
    OXE 侧最近事件。
  conditions: 部分事件号（如 1125）不在默认事件表，需先 Create 事件才能设 Network incident（p287 Notes）
  tags: [rule, alarms, oxe, incident]

- id: p21
  title: 告警通知出口参数——邮件服务器语法与脚本变量
  type: rule
  source_pages: p301-306
  source_chapter: Alarms application - Functionalities (How-To)
  source_quote: |
    "Mail server Specify the mail server IP@ or FQDN ... enter: 10.20.30.11:46 if mail server
    uses the SMTP port 46; enter: 10.20.30.11 if mail server uses the default SMTP port (25) ...
    By default, the name is: omnivista@<8770 FQDN>" (p301)
    "Create a .bat file in the folder c:\8770\data\alarms\scripts ... msg * /SERVER nms Alarm
    from %1 received at %2 ... The variable %1 ... replaced by the field $managedobject ...
    %2 ... $notificationtime" (p305)
  summary: |
    邮件出口：Administration > OmniVista 8770 > Export parameters 页填 Mail server（格式 <名称或IP>:
    <SMTP 端口>，默认 25 可省端口且冒号后不能有空格）+ 发件人名（默认 omnivista@<8770 FQDN>，填管理员
    邮箱可收回复）；过滤条件在 Alarms 应用 Preferences > Alarms > Alarms Filters 定义（如 Severity
    Equal Major + E-Mail Addresses 页填收件人，多个逗号分隔）。脚本出口：.bat 放
    c:\8770\data\alarms\scripts，Filter 的 Script 页填脚本名与参数——%1=$managedobject（告警对象）、
    %2=$notificationtime（通知时间）；进阶语法查 Alarms Help 7.1.4。
  conditions: 邮件服务器声明同时是 AdminNmc 邮件重置码的前提（p392）
  tags: [rule, alarms, notification, script]

- id: p22
  title: SNMP Proxy 双层口径——Windows SNMP 服务必须装 + hypervisor 参数表
  type: rule
  source_pages: p308, p313-317
  source_chapter: Alarms application – SNMP proxy (How-To)
  source_quote: |
    "The Windows service SNMP must be installed on the server 8770. Netsnmp component is part of
    Windows SNMP service and it's used for the SNMP service of the OmniVista 8770." (p308)
    "IP Address Enter the IP address of the SNMP hypervisor ... Do not use FQDN. Protocol
    Version ... (V2 for example) Port for Trap Reception Port number used for trap reception
    (162 for example)" (p313)
    "Authentication protocol Select the SNMP authentication protocol between SHA (default) or
    MD5 ... Encryption protocol Select the SNMP encryption protocol between DES (default) or
    AES128" (p314)
  summary: |
    双层结构：①Windows SNMP 服务必须先装（Netsnmp 组件归属它），启用 8770 自带代理后 Windows 服务
    会被停用——"必须装，即使要禁用它"；②hypervisor 声明（Administration > 右键 nmc > Create >
    Hypervisor）：IP 不用 FQDN、协议 V2/V3、trap 端口 162；V3 追加认证（SHA 默认/MD5）与加密（DES 默认/
    AES128）双密码。启用/停用走 ToolsOmniVista → 4 SNMP → 1 SNMP Agent；激活 PBX 监督在 OXE Data
    Collection 页勾 Managed by SNMP proxy（自动发 Add PABX trap，标识 1/1/101）；SNMP Filter 按
    Correlation/Diagnostic 过滤（诊断号分号分隔或连字符区间，可 AND/OR 叠加）。
  conditions: 日志 NMCSnmpAgent_1.log；V3 配置与卸载流程书中标注"仅供信息、勿执行"
  tags: [rule, snmp, proxy]

- id: p23
  title: 报告引擎六项上限（TXT 4000 行 / 各格式 50 页 / 数据库 100000 行）
  type: metric
  source_pages: p444
  source_chapter: Reports application (How-To) / Configuring report size limits
  source_quote: |
    "Maximum number of lines in TXT format 4000 ... Maximum number of pages in HTML format 50 ...
    Maximum number of pages in PDF format 50 ... Maximum number of pages in EXCEL format 50 ...
    Maximum number of elements on X axis 100 ... Maximum number of lines in database 100000" (p444)
  summary: |
    Reports 偏好默认上限：TXT 4000 行；HTML/PDF/EXCEL 各 50 页；图表 X 轴 100 元素；数据库取数上限
    100000 行。超限报告末尾出现截断提示——大数据量导出要改分批或放宽上限。生成入口：预定义报告复制到
    个人文件夹（如 My Alarms reports）→ Generate Report（Immediate/Scheduled + Notification time 等
    附加过滤，一般选 This year）→ Open to View/Export（File：TXT/HTML/PDF/EXCEL，或 E-MAIL）。
  conditions: 邮件导出目标多地址逗号分隔；邮件服务器参数同 p21（含认证 SMTP 选项：账号/密码/starttls）
  tags: [metric, reports, limits]

- id: p24
  title: Scheduler 参数语义表（Maximum start delay / Stop on error / Retry / 依赖延迟）
  type: metric
  source_pages: p473
  source_chapter: Scheduler Application (How-To) / Scheduling & Retry options
  source_quote: |
    "Maximum start delay This is the maximum delay allowed to run a task that was not performed
    on the scheduled date. Example: the job scheduled for Saturday with a maximum delay of one
    day is not performed if the PC is shut down on Friday and restarted on Monday." (p473)
    "Delay dependant job start Time for end of execution of current job before processing the
    next job. The specified time does not take seconds into account. Stop on error Enable this
    option if you want a task to be aborted when one of its sub-tasks is executed incorrectly.
    By default, this option is enabled. ... Number of retries ... Time Between Retries ...
    Maximum Execution Time" (p473)
  summary: |
    任务参数精确语义：Maximum start delay=错过后补跑的最大延迟（示例：周六任务、延迟 1 天，周五关机
    周一开机则不补跑）；Delay dependant job start=上一 job 结束到下一 job 启动的间隔（不计秒）；
    Stop on error 默认启用（子任务失败即中止）；Retry=重试次数/间隔（天时分秒）/最大执行时长；
    Ending date 限定重复区间；Exclude Days 排除星期；Job Owner 不可改。jobset 仅为创建期临时名，
    刷新后变 Job（f18）。
  conditions: 恢复预定义维护 job 用 LDIF 导入 + 重启 NMC Scheduler 服务（p502）
  tags: [metric, scheduler, semantics]

- id: p25
  title: 数据清除默认值与实验口径（计费/话务/报告/告警/审计五类）
  type: metric
  source_pages: p489-493
  source_chapter: Scheduler - Automatic maintenance (How-To)
  source_quote: |
    "Clean PTP hour old than Enter a value as a number of days (i.e. 4). Clean ticketandaffiliated
    old than Enter a value as a number of days (i.e. 15)" (p489)
    "Clean carrier config old than 94 ... Clean monitoring hour old than 45 ... Clean monitoring
    day old than 94 ... Clean monitoring month old than 15 ... Clean monitoring year old than 36
    ... Clean Organization 1" (p490)
    "Clean taxa Reports Enter a value as a number of days (i.e. 2)" (p491)
    "Purge limit for incidents Max number of alarms in database. Alarms older than the specified
    number of days are purged. If the remaining number of alarms is > purge limit for incident,
    oldest alarms are purged" (p492)
  summary: |
    五类清除默认值（实验改三处：小时级话务留 4 天、计费记录留 15 天、计费报告留 2 天）：①计费/话务
    （Accounting preferences）：carrier config 94 天、小时/日/月/年跟踪计数 45 天/94 天/15 月/36 月、
    Clean Organization=1（布尔，清无票组织）、PTP 小时/日/月/年 45/94/15/36、VoIP 同 45/94/15/36、
    taxa 日/月 94 天/15 月、计费票 36 天/94 月/15 天（原表顺序如此）、VoIP 票 94 天/15 月；②报告
    （Reports preferences）：Clean Reports=1（布尔）、Taxa/PTP/Monitoring/VoIP 报告各 94 天；③告警
    （Purge configuration）：按天+按条数双闸（超条数再清最旧），实验 100 告警/100 事件；④审计：日志
    保留天数 + 导出 CSV 寿命 + Keep one backup；⑤文件夹（NmcArchive）：Free disk space 或 Directory
    size 双阈值触发 minor/major 告警 + Clean-up Delay 保留期 + Keep one backup。
  conditions: 各保留期生产需按合规要求定；清除由 Daily/Weekly Job 执行
  tags: [metric, purge, maintenance, defaults]

- id: p26
  title: 8770 备份恢复铁律——版本绑定 + 恢复前清场 + 目录名时间戳
  type: rule
  source_pages: p507, p509-510, p519-520
  source_chapter: 8770 Maintenance application（讲义 + How-To）
  source_quote: |
    "OmniVista 8770 Server is unavailable during backup process. A backup of the 8770 is
    scheduled by default" (p507)
    "A backup is dedicated to a software version. It must be restored on a server having the
    same software version. The file RestoreContext.ini located in the backup folder gives the
    8770 server version that must be used to restore the backup." (p519)
    "The directory name of the backup is based on 'YYYYMMDDHHMMSS'" (p520)
  summary: |
    恢复三条铁律：(1) 备份专用版本——nmcVersion 决定只能还原到同版本服务器（跨版本必须先装同版本）；
    (2) 恢复前清场——删除 Configuration 中已声明节点 + 删除全部告警；(3) 备份目录按 YYYYMMDDHHMMSS
    命名、每备份一目录。备份位置与阈值在维护设置中配（默认 C:\8770_ARC\8770Backup；双阈值告警；
    Record Life 保留期由 Scheduler 日检）。备份期间 8770 不可用。
  conditions: 计划备份为默认任务（Weekly Job > 8770 Data Backup）
  tags: [rule, backup, restore]

- id: p27
  title: rehosting 场景矩阵——改 IP / 改 FQDN 同机 / 换机
  type: rule
  source_pages: p509, p511-513
  source_chapter: 8770 Maintenance application / IP address modification & FQDN modification
  source_quote: |
    "IP address modification: Backup the OmniVista 8770 Server database, Change the IP address,
    Restore the saved data using 8770 Maintenance application. Select the Restore databases with
    rehosting operation" (p511)
    "On the same machine: Uninstall the OmniVista 8770 Server, Change the FQDN, Re-install ...
    On a new machine: Install ... Restore the database with rehosting" (p512)
    "Comparison of RestoreContext.ini files (current and the one from the backup) will exclude
    the hostname svNMCName and domain svDomain entries. After the database restoration, scripts
    are invoked to make the changes in the LDAP data." (p512)
  summary: |
    三场景：①改 IP：备份→改 IP→Restore databases with rehosting（脚本自动改配置）；②改 FQDN 同机：
    卸载 8770→改 FQDN→除 FQDN 外同参数重装（密码/目录树/路径不变）；③换机（含改 FQDN）：新机同参数
    安装→rehosting 恢复。rehosting 比对 RestoreContext.ini 时排除 svNMCName 与 svDomain 两项，恢复后
    脚本改写 LDAP 数据使主机标识生效。
  conditions: 计算机名/DNS 后缀日常修改需重启系统（p67）；恢复前提见 p26
  tags: [rule, rehosting, migration]

- id: p28
  title: 维护工具入口与凭据表（Diagnostic / DirManag / DSCC / HeidiSQL）
  type: checklist
  source_pages: p522-531, p533-538
  source_chapter: Maintenance tools（讲义 + How-To）
  source_quote: |
    "8770 Diagnostic collects information and provides: An html file ... A compressed file (.zip)
    that can be transmitted to Alcatel-Lucent Enterprise support for diagnostic" (p523)
    "Host name 8770 server name, Port number 389 (LDAPS is not supported), Login cn=directory
    manager (you can also use 'adminnmc' as login)" (p535)
    "User Enter the user login (i.e. dba), Password Enter the user password (i.e. sql) (default
    password which can be modified via ToolsOmniVista.exe), Port Select the default port
    (i.e. 3306)" (p536)
  summary: |
    四工具口径：①8770 Diagnostic（Start > OmniVista 8770 > Tools）：交互/非交互两模式（后者只需 LDAP
    端口 389 + SQL 密码 sql），产出 C:\TS 下 HTML + zip（文件名 NMS_周几月日），zip 交 ALE 支持开 SR；
    ②DirManag.exe（c:\8770\bin）：LDAP 浏览改，端口 389（不支持 LDAPS），登录 directory manager 或
    adminnmc，改后 Ctrl+S 保存；③Directory Server Control Center：LDAP 另一入口，登录 admin；
    ④HeidiSQL（Start > MariaDB 10.5）：MariaDB TCP 127.0.0.1:3306，dba/sql，查 nmc5 库（如
    select * from nmc5.organization）；数据文件在 8770\data\data（.frm 表定义/.ibd 数据/.TRN/.TRG 触发器）。
  conditions: 诊断收集含日志/RestoreContext.ini/服务状态/许可/计划任务等（p523 清单）
  tags: [checklist, tools, diagnostic]

- id: p29
  title: NMC 服务日志口径——2×5MB 滚动 + TraceType 切换 + nmclog 别名
  type: metric
  source_pages: p547-553, p562-567
  source_chapter: NMC services（讲义 + How-To）
  source_quote: |
    "TraceType 0 (Default traces) / TraceType –-1 (Detailed traces) Warning: this mode slows
    down the server! ... Go back to default trace, after investigation" (p547)
    "_1.log file: last recorded actions while the file limit of 5 Mo is not reached. _2.log file:
    If _1.log file limit is more than 5 Mo, second file is created" (p549)
    "https://nms.company.com/nmclog/ — /nmclog/ is a web alias pointing to log files" (p553)
  summary: |
    日志三维度的精确口径：位置——NMC 服务在 <安装目录>\log、Apache 在 <安装目录>\Apache2\logs、LDAP 在
    <安装目录>\SunONE\slapd-8770\logs；滚动——每 NMC 服务上限 10MB（_1.log 满 5MB 后写 _2.log）；
    详细度——Administration 应用 nmc/OmniVista8770/<服务> 的 Argument list 由 -TraceType 0 改
    -TraceType --1 开详细跟踪（拖慢服务器，查完必须改回 0）。Web 查看 https://<FQDN>/nmclog/
    （管理员凭据，浏览器加安全例外）。服务启停：Service Manager 中 Select+Execute 取权；被 NMC Service
    Manager 监督的服务崩溃自动重启（勿手动 Start）。
  conditions: Startup type=Automatic 的四个服务需手动 Start（f21）
  tags: [metric, logging, nmc-services]

- id: p30
  title: ToolsOmniVista.exe 菜单地图与两条 Warning（不校验密码策略 / 非正常退出不停服）
  type: checklist
  source_pages: p315, p389-396, p414-415
  source_chapter: Security Application (How-To) & SNMP proxy & POODLE add-on
  source_quote: |
    "1 : Security / 2 : Certificate Management / 3 : Accounting Organization Update / 4 : SNMP /
    5 : Management Domain / 0 : Quit" (p389)
    "IF THE TOOSLOMNIVISTA.EXE APPLICATION IS NOT CLOSED PROPERLY (PRESS '0' TO EXIT PROPERLY),
    THE NMC SERVICES ARE NOT RESTARTED AUTOMATICALLY! THE TOOLSOMNIVISTA.EXE APPLICATION DOES NOT
    CHECK ANY PASSWORD COMPLIANCE REGARDING THE PASSWORD POLICY RULES OF OMNIVISTA (HISTORY,
    LENGTH ETC.)" (p391)
    "Password Policy: (1) Length of the password must be at least 8 characters in length. (2)
    Should be a mixture of Uppercase, lowercase, digit and special characters (3) Space, accented
    characters, non-printable characters and \" ' ` ^, ; + \ < > % | are not accepted" (p390)
  summary: |
    菜单地图：进工具输 directory manager 密码 → y 停 8770 服务（强制）→ 主菜单 1 Security（1 Password
    Update：1 DB 管理员/2 LDAP directory manager/3 LDAP 控制台管理员/4 AdminNmc/5 8770 Administrator/
    6 LDAP Replication Manager；2 Minimal SSL/TLS release：SSLv3~TLS1.3；3 3DES Cipher Suite 开关）、
    2 Certificate Management、3 Accounting Organization Update、4 SNMP、5 Management Domain → 每层
    0 退出。工具自身密码规则：≥8 字符、四类字符混合、不接受空格/重音/不可打印字符与 " ' ` ^ , ; + \ < >
    % |；但不校验 OmniVista 侧密码策略（历史/长度）；必须按 0 正常退出，否则 NMC 服务不自动重启。
  conditions: AdminNmc 锁定只能用本工具选项 4 或 WBM 邮件重置解锁（p390）
  tags: [checklist, toolsomnivista, passwords]

- id: p31
  title: 8770 密码策略字段语义与时效公式 B+C<A
  type: formula
  source_pages: p384-385
  source_chapter: Security Application (How-To) / Configuring the password policy
  source_quote: |
    "Lock the Password After maximum Login Failure ... When an account is locked, an alarm is
    generated. ... Password Lockout Duration in Minutes ('0' to password unlock by administrator)
    Enter 0 to allow only the Administrator to unlock the password" (p384)
    "Password Expired in Days ('0' to disable password expiration) (A) ... Password Warning
    Before expiration in Days (B) ... Allow Password Change After (in Days) (C) ... When
    configuring password aging, respect the rule (B) + (C) < (A)" (p385)
  summary: |
    策略字段：密码质量检查（不含用户标识信息）、最小长度、历史个数（0 禁用）、首登/重置后强制改密、
    失败锁定（锁定产生告警；Lockout Duration=0 表示仅管理员可解锁，>0 按分钟自动解锁）、时效三参数
    （A 有效期/B 提前警告天数/C 最短改密间隔）须满足 B+C<A。配置权限：仅 Security 应用访问级别为 All
    的用户（默认 AdminNmc）。
  conditions: 实验把策略放宽（长度 4、关历史/首登改密/时效）仅教学口径
  tags: [formula, password-policy, security]

- id: p32
  title: 账户解锁四路径与告警联动（含 AdminNmc 专属与 WBM 邮件重置）
  type: checklist
  source_pages: p388, p390-394
  source_chapter: Security Application (How-To) / Resetting a locked account
  source_quote: |
    "Open the Alarms Application, Search the (major) alarm corresponding in the section Locked
    User Accounts" (p388)
    "If AdminNmc account is locked, it must be unlocked using ToolsOmniVista.exe." (p390)
    "This email address is used to receive a reset password code from the OmniVista 8770 when
    the administrator account session is locked." (p392)
  summary: |
    锁定表现：连续失败达阈值→账户锁 + Locked User Accounts 区 major 告警。解锁四路径：①普通管理员：
    Security 应用选中账户改密即解锁；②任意管理员：ToolsOmniVista 选项 1→1→5 改 Administrator 密码；
    ③AdminNmc 专属：ToolsOmniVista 选项 1→1→4（或 WBM 邮件重置）；④WBM 邮件重置：前置=邮件服务器已
    声明（p21）+ 管理员账户已填邮箱（Security 应用 Individual 页 Mail 字段）→ WBM 登录页 Forgotten
    your password? → 收重置码邮件（如 Kp709sC1V@ 实验口径）→ 输码+新密解锁。
  conditions: ToolsOmniVista 不校验密码策略（p30）；重置码邮件发往账户 Individual 页邮箱
  tags: [checklist, lockout, security]

- id: p33
  title: OXE Access Profile 体系——11 个 profile / 四级权限 / 全 OXE 共用 / 本地 MIB 重载
  type: rule
  source_pages: p399-402
  source_chapter: Security Application (How-To) / Configuring OXE Access Profiles
  source_quote: |
    "11 Access Profiles are available ... 0 YES Gives access to all objects, all attributes, and
    all actions / 1 YES Restricts access to expert management objects / 2 YES Restricts access to
    usual management objects / 3 YES Restricts access to user management objects / 4 to 9 NO /
    10 YES Specially designed for attendant management" (p399)
    "Rights available: Nothing: the object is not displayed ... Read ... Read/Write ... All" (p400)
    "After managing access profiles, you must delete the OmniPCX Enterprise MIB saved locally on
    the client PC to reload the MIB" (p402)
  summary: |
    规则：profile 0-3 与 10 已占用（10 分配给 Simplified Configuration 组做话务台管理），4-9 可定制；
    每对象类四级 Nothing（树中不显示）/Read/Read-Write/All，另可属性级显隐与 Actions 授权；profile 全
    OXE 通用，应在最新版本 OXE 上编辑以覆盖最多属性；改后必须删客户端本地 MIB（Preferences >
    Configuration > Object Model Save > List > Delete）再连重载。Security 应用侧给组/账户配
    Configuration 访问时选 Access Level（No Access/Configure/All）+ OmniPCX 4400 Access Level=profile 号。
  conditions: 实验配置 profile 9：Users=All、Trunk groups=Read、其余 Nothing
  tags: [rule, access-profile, security]

- id: p34
  title: OXE 侧配置访问控制——大写白名单 + Secure access 前提 + 重置命令链
  type: checklist
  source_pages: p406-412
  source_chapter: Security Application (How-To) / OmniPCX Enterprise access control
  source_quote: |
    "User Name Enter an administrator account, available on Security application, in uppercase.
    (ex: ADMINNMC) ... User List Access Enable User List 1." (p408)
    "The Secure access for system management option must be set up to enable OXE control access." (p408)
    "1. Deactivate MAO (mao off) 2. Launch multitool SECURITY_ACCESS 3. Select option 10:
    Security access reinitialization 4. Activate MAO (mao on)" (p412)
  summary: |
    配置路径：OXE 配置界面 Security and Access Control > 1 > User Access Control 右键 Create——User
    Name 填 8770 Security 应用中的账户（必须大写）、Management by user authorized 与 User Validity
    启用、User List Access 启 User List 1。前提：OXE Connectivity 页 Secure access for system
    management 启用。生效行为：改完断开 8770 会话重连，白名单外账户（如 Expert2）打开配置界面被拒。
    重置回默认：OXE telnet 会话 mao off → multitool SECURITY_ACCESS 选 10 → mao on。
  conditions: 实验授权 ADMINNMC+EXPERT1 拒绝 EXPERT2 验证
  tags: [checklist, access-control, oxe]

- id: p35
  title: TLS/SSLv3 加固口径——ToolsOmniVista 选 TLS 1.3 连带禁用旧协议 + 全网元前提
  type: rule
  source_pages: p413-415
  source_chapter: Security Application (How-To) / ADD-ON: POODLE Vulnerability
  source_quote: |
    "This solution addresses the POODLE (Padding Oracle On Downgraded Legacy Encryption)
    vulnerability (CVE-2014-3566) linked to the support of the obsolete SSLv3 protocol." (p414)
    "ALL THE NETWORK ELEMENTS IN THE INFRASTRUCTURE (OMNIPCX ENTERPRISE, OMNIPCX OFFICE, OPENTOUCH,
    SIP SETS, ACTIVE DIRECTORY, MAIL SERVER, …) MUST BE TLS COMPATIBLE. IF NOT, IT WON'T BE
    POSSIBLE TO DISABLE THE SUPPORT OF THE SSL V3 PROTOCOL FROM THE OMNIVISTA 8770 SERVER." (p414)
    "Select the security level you want to apply 5 - TLS 1.3 ... TLS1.3 security protocol is
    activated and by the same time SSL V3 is deactivated." (p415)
  summary: |
    加固路径：ToolsOmniVista → 1 Security → 2 Minimal SSL/TLS release → 选 5（TLS 1.3）——同时禁用
    SSLv3/TLS1.0/TLS1.1（含 Wildfly 配置与 LDAP 更新）。硬前提：基础设施全部网元（OXE/OXO/OpenTouch/
    SIP 话机/AD/邮件服务器等）必须 TLS 兼容，否则不能从 8770 侧禁 SSLv3。该附录标注"仅供信息、勿执行"。
  conditions: 菜单另有 3DES Cipher Suite 开关（p30 菜单地图）
  tags: [rule, tls, security, hardening]

- id: p36
  title: Audit 启用三开关与 OXE mao 日志三文件
  type: checklist
  source_pages: p426-429, p431-433
  source_chapter: Audit Application (How-To)
  source_quote: |
    "Administration Application: Browse to nmc > OmniVista 8770 > nms > Service > AuditServer ...
    Audit process Validate the check box" (p426)
    "Check the box Process audit ... Username maintenance mtcl ... The rsh command converts the
    /DHS3data/mao/mao_hdet file ... into the text file /DHS3data/mao/list_fhdet.txt" (p427)
    "Validate the check box to enable recording the 8770 administrator names (used to configure
    the OXE) into the mao_hist file of the OXE." (p427)
  summary: |
    启用三开关：①8770 侧 Administration > Service > AuditServer 勾 Audit process（配日志/导出文件
    保留天数 + Keep one backup）；②OXE 侧 Data Collection 页勾 Process audit + Software download 页填
    mtcl（rsh 执行 list_fhdet 转换用）+ Connectivity 页勾 Secure Access for System Management（把
    8770 管理员名记入 OXE mao_hist）；③检索：Configuration 或 Audit 应用右键 OXE > Synchronization >
    Audit information（每日同步自动取）。OXE 侧日志：/usr3/mao/mao_log_hist（配置连接登录记录）、
    mao_hist（增删改操作，标注 (nms|用户) 或 (MANAGER|)）、mao_hdet→list_fhdet.txt（操作明细）；
    系统命令日志 /var/log/shell.log。查询口径：System 页默认搜索条件无效，需清空后建 PbxName Not Empty。
  conditions: Audit 仅支持 OXE；导出功能不适用于 8770 自身日志（n41）
  tags: [checklist, audit, logs]

- id: p37
  title: Audit 导出与报告口径（History vs Detail 字段集 + 仅限 OXE 数据）
  type: rule
  source_pages: p432-434
  source_chapter: Audit Application (How-To) / Exporting & Using Audit report
  source_quote: |
    "Immediate on local drive: If selected, the manager can select any network destination folder
    ... Scheduled on Server: If selected, the destination folder (8770\Client\data\audit) cannot
    be modified" (p433)
    "History Export only the main parameters (History ID, Server Name, User, Date, Action,
    Object, PbxName, NodeId, Broadcasted, Attribute1...Attribute5) / Detail Export all the
    parameters (... GRID_MAO_AttributeValue)" (p433)
    "Warning: THIS PART DOES NOT APPLY FOR THE AUDIT INFORMATION ON OMNIVISTA 8770 LOGS" (p433)
  summary: |
    导出两模式两粒度：立即（本地/任意网络目录）或计划（固定 8770\Client\data\audit，不可改）；History
    导 13 个主字段、Detail 追加 Attributes 与 GRID_MAO_AttributeValue 全量；CSV 生命周期与保留一份由
    AuditServer 设置控制。报告：Reports 应用 Audit > Predefined Reports > Detailed Reports 复制到个人
    文件夹后 Generate（附加过滤器选空即禁用）。明确边界：导出不适用于 8770 自身 log 审计数据。
  conditions: 8770 log 页记录客户端登录登出与 Accounting/Reports 应用访问（p432）
  tags: [rule, audit, export]

- id: p38
  title: 许可文件结构精确口径（布尔键/用户数键/8770Clients 30/Security 键 0-5）
  type: metric
  source_pages: p601-605
  source_chapter: 8770 LICENSE / License file parameters
  source_quote: |
    "Topology, AccountingMonitoring, Audit, Security or ExternalDirectorySynchro keys are
    Booleans (1 means that the application is enabled). 8770Clients key is the maximum number of
    simultaneous clients (up to 30)" (p603)
    "Security key is a level of security based on 3 parameters: Secure IP connections ... Use of
    external authentication mechanism (e.g. Radius) ... Use of Public Key (not available anymore
    from release R5.0). Numeric values for this key are: 0: No security flows and no PKI ... 5:
    Security flows and full PKI feature" (p603)
    "Only the N-1 license is supported in the N release ... Release 8770 R5.2 Licence version
    15 or 16" (p602)
  summary: |
    [Modules] 键三型：布尔键（Topology/AccountingMonitoring/Audit/Security/ExternalDirectorySynchro，
    1=启用）；用户数键（Configuration/Alarms/Accounting/PastTimePerformance/Directory/TicketCollector/
    Performance/ALUSIPdevices/ThirdPartySIPDevices/UnifiedUserManagement/SNMPProxy/OXOVoIPTickets/
    OpenAPI/RTUAuditor 等，值为可监管用户数且各应用同值）；特殊键——8770Clients 并发客户端上限（最大
    30）、Security 键 0-5（0 无安全流无 PKI / 1 安全流无 PKI / 2-3 基础 PKI（EJBCA 简包装）/ 4-5 完整
    PKI（集成证书部署），奇数含安全流；PKI 特性 R5.0 起不再可用）。版本规则：只支持 N-1（R5.2 接受
    许可版本 15 或 16）。许可控制方法 #1 申报节点 8770Handle（OXE OPS 文件中，spadmin 显示 Handle
    4760=123456AB 实验口径）；方法 #2 绑定服务器特征 MAC/IP/ProductID/UUID（冗余双机各一组字段）。
  conditions: 许可文件由 ACTIS 报价生成；Training Purpose 许可为实验口径
  tags: [metric, license, locks]

- id: p39
  title: 许可包型与选项清单（Start Pack / Full Pack PPU + 独立选项）
  type: metric
  source_pages: p596, p598-600, p608
  source_chapter: 8770 LICENSE / ACTIS quotation & PCX locks
  source_quote: |
    "Start Pack PPU: Included functionalities: Alarms, Metering and tracking, Unified management,
    Configuration application (not visible but included), Audit (not visible but included).
    Optional functionalities: Active Directory Integration, Manage My Phone, API Provisioning,
    Topology, SNMP Proxy" (p598)
    "Full Pack PPU: Included the Start Pack PPU, with Performance, Company Directory. Options
    whatever selected pack: Ticket Collector, Security, Multi Domain (if Company Directory is
    selected)" (p599)
    "OXO Connect: Accounting: Yes / No. If yes: Default: no ticket, Possibility to increase the
    number of tickets by steps of 1000, 30 000 tickets maximum. Alarms: no lock. OMC: no lock" (p608)
  summary: |
    包型：Start Pack PPU 含告警/计量跟踪/统一管理（Configuration 与 Audit 内含不可见），可选 AD 集成/
    MMP/API Provisioning/Topology/SNMP Proxy；Full Pack 加 Performance 与 Company Directory；任意包型
    可加 Ticket Collector、Security、Multi Domain（需 Company Directory）。被管侧锁：OXE 按 spadmin
    锁号（39 Performance/42 Accounting users/47 Alarms/49 Directory/50 Configuration/98 本地计费/
    99 ABC 计费，SSH 连接无锁）；OXO Connect 仅计费有锁（默认无 ticket、1000 步进、上限 30000 tickets），
    告警与 OMC 无锁。超限行为：逼近上限告警、超限进受限模式仅 Directory+Configuration、服务器不停防
    数据丢失（p606）。
  conditions: 8770 须在 offer 指定的 OT/OXE 节点上申报（p600）
  tags: [metric, license, packs]

- id: p40
  title: 许可更新四步与用量日志（停服务 → 换文件 → 启服务 → About 核验）
  type: checklist
  source_pages: p610-617
  source_chapter: 8770 License (How-To)
  source_quote: |
    "Browse to c:\8770\etc, Rename the nmc.license file into nmc.license.old, Paste the new
    license file and rename it to nmc.license" (p615)
    "Consult the file c:\8770\log\NMCLicServer_1.log ... unifiedusermanagement : percent of max
    subscriber: 15/250 = 6% (status=ok)" (p617)
  summary: |
    更新四步：Service Manager 停 NMC Service Manager → c:\8770\etc 下 nmc.license 改名 .old → 新文件
    改名 nmc.license → 启动 NMC Service Manager → 客户端 Help > About 核对新锁。查询两入口：客户端
    Help > About；或文本编辑器打开 nmc.license 看锁值。用量审计：NMCLicServer_1.log 打印各模块
    "x/上限 = 百分比 (status=ok)"。OXE 侧锁查询：Telnet/SSH mtcl 会话执行 spadmin（Display current
    counters=1）。
  conditions: 换许可文件期间服务停止；更新后应用可见性随 [Modules] 变化
  tags: [checklist, license, update]

- id: p41
  title: OXE 备份机制代际差异与恢复前置（N2 默认密码 / N3 自定义 + 停电话副作用）
  type: rule
  source_pages: p572-575, p577, p589
  source_chapter: OMNIPCX ENTERPRISE BACKUP（讲义 + How-To）
  source_quote: |
    "Telnet or SSH to the OXE (login = mtcl, password = mtcl by default) ... swinst password
    (SoftInst by default) ... FTP or SFTP (login = adfexc, password = adfexc by default) —
    Mechanism until OXE N2" (p573)
    "SSH to the OXE (login = mtcl, password = to be customized) ... swinst password (to be
    customized) — Mechanism from OXE N3" (p574)
    "Managers must stop the telephone first, to restore the backup files via Swinst tool." (p577)
    "by stopping such process, you disable the role address facility. Don't forget to use the OXE
    physical IP address to enter in configuration mode" (p589)
  summary: |
    机制代际：N2 及以前——mtcl（telnet，默认密码 mtcl）、bck 命令经 RSH（swinst 默认密码 SoftInst）、
    取回经 FTP/SFTP（adfexc 默认密码 adfexc）；N3 起——强制 SSH 且 mtcl/adfexc/swinst 密码全部已
    自定义。备份落位：OXE 生成 /usr4/BACKUP/IMMED（mao、vg）与 /usr4/BACKUP/OPS（ops_R10_1.hw/.swk、
    hardware.mao 等），8770 取回存 c:\8770_ARC\OXEBackup\<网络>\<子网>\<节点>\<YYYYMMDDhhmmss>。
    恢复三前置：先停电话（swinst Easy 菜单 7）、停电话会禁用 role address 设施（之后连 OXE 用物理
    IP）、恢复完成要重设 Autostart 再启动电话。
  conditions: 备份类型可选 mao/语音导引/OPS（mao 含用户数据库）
  tags: [rule, oxe-backup, swinst]

- id: p42
  title: swinst 恢复菜单路径全链（Easy 停起电话 / Expert 备份恢复 / Autostart）
  type: checklist
  source_pages: p587-593
  source_chapter: OmniPCX Enterprise backup & restore (How-To)
  source_quote: |
    "Open a swinst session (101) csa> swinst ... FACILITIES Easy menu / Expert menu / Q Quit ...
    Select the Stop the telephone option by pressing 7" (p589)
    "Select the Expert menu by pressing 2 ... Select the option Backup & Restore operations by
    pressing 4 ... Restore operations by pressing 3 ... Restore from cpu disk by pressing 1 ...
    Restore from immediate backup by pressing 1 ... Restore mao data by pressing 2" (p590-591)
    "Select the System management option by pressing 6 ... Autostart management by pressing 2 ...
    Set autostart by pressing 1" (p592)
  summary: |
    swinst 完整菜单链：mtcl 会话起 swinst（swinst 账号+密码）→ 停电话：Easy 菜单（1）→ 7 Stop the
    telephone → y 确认；恢复：Expert 菜单（2）→ 4 Backup & restore operations → 3 Restore operations →
    1 Restore from cpu disk → 1 Restore from IMMEDIATE backup → 2 Restore mao data → 确认（ securing
    填 n）→ 完成后 Q 退回主菜单；自启：Expert → 6 System management → 2 Autostart management →
    1 Set autostart；起电话：Easy 菜单 → 8 Start the telephone → y 确认。验收：被删用户已还原。
  conditions: 恢复期间电话服务停止（业务中断窗口）；FACILITIES 3.41.0 实验口径
  tags: [checklist, swinst, restore]

- id: p43
  title: OXO Connect 纳管参数口径（话机查 IP / OMC 安装 / 双密码字段 / 共享目录）
  type: checklist
  source_pages: p641-659
  source_chapter: OXO Connect node declaration (How-To)
  source_quote: |
    "On the Menu tab, click on Operator ... Password Letacla1 (password used on a classroom
    environment) ... Select Netw.config. Select IP@CPU. Check the IP address in the field called
    MAIN@" (p642-643)
    "FTP password Enter the FTP password of the NMC account (i.e. Pbxnmc12). This account is used
    to retrieve the metering tickets from the OXO Connect. ... Alarms reception mode Permanent IP
    Connectivity ... Accounting process Detailed accounting" (p657)
    "Secure Shared Directory, Authorized User Name / Authorized User Password ... (\\nms\
    \OXO-databases)" (p659)
  summary: |
    纳管参数五组：①OXO 侧 IP 核查：Premium 话机 Menu > Operator（实验密码 Letacla1）> Expert >
    Netw.config > IP@CPU 看 MAIN@；②OMC 安装：BP 网站下载 zip → 解压传 8770 服务器 → 管理员 Setup.exe
    （首装需 .NET Framework；选国家/目标产品/显示语言）；③OMC 连接：Expert + LAN/WAN + CPU IP +
    服务器认证 + 证书入"受信任的根证书颁发机构"→ installer 密码（cold reset 后默认 pbxk1064，否则用
    首装自定义值，实验 Alcatel1）→ OXO R10 起强制改全部账户密码 → 首连必填客户信息；④8770 声明：
    OmniPCX Office 节点 PCX 页（节点号 80→声明节点 180、IP、FTP password=NMC 账号 Pbxnmc12 用于取
    计费票、Process configuration、Permanent IP Connectivity、Detailed accounting、成本中心、VoIP
    performance）+ Connectivity 页 Omc config password=installer 密码；⑤Preferences > Configuration >
    OXO Preferences > Shared Directory Parameters：启用 Secure Shared Directory 并填 8770 服务器
    Windows 会话账号（Administrator/superuser 实验口径），供备份共享 \\nms\OXO-databases 访问；
    参数错误需重启 8770 服务器。
  conditions: OMC 须装在 8770 服务器与每个 8770 客户端（p20）；节点号换算见 p09
  tags: [checklist, oxo-connect, omc]

- id: p44
  title: 网络驱动器场景的 ADM8770 账号与五项用户权利
  type: checklist
  source_pages: p669, p680-693, p696-697
  source_chapter: Map network drive (How-To)
  source_quote: |
    "ADM8770 account must be member of Administrators group. ADM8770 account must be removed from
    Users group" (p680)
    "Assign the following rights to ADM8770 account: Access this computer from the network / Log
    on as a service / Act as part of the operating system / Adjust memory quotas for a process /
    Replace a process level token" (p684)
    "Username Enter account in uppercase preceded with the following characters .\ (i.e.
    .\ADM8770)" (p696)
  summary: |
    账号口径：两台服务器建同名同密 ADM8770（实验密码 superuser；不可改密、永不过期）；8770 侧账号入
    Administrators 组、移出 Users 组；Local Security Policy > User Rights Assignment 赋五项权利——
    从网络访问此计算机、作为服务登录、作为操作系统一部分、调整进程内存配额、替换进程级令牌（书中注明
    可按客户安全等级裁剪，此组合满足多数场景）。服务注入：Administration 应用 Service 下给 ExecdEx
    （报表）与 SaveRestore（备份恢复）配 Nt account=.\ADM8770（大写、带 .\ 前缀）+ 密码。
  conditions: 映射需以 ADM8770 登录 Windows 后执行（Y:/Z: 实验口径）；验收=立即备份时 Search 可见网络位置
  tags: [checklist, network-drive, windows]

- id: p45
  title: 客户端下载 URL 与 WBM 入口口径（大小写敏感 / 8443 / nmclog）
  type: metric
  source_pages: p99, p254, p392, p553
  source_chapter: Client installation & WBM & Security & NMC services
  source_quote: |
    "Enter the following URL: https://<8770 FQDN>/cgi-bin/OmniVista8770Client.exe Be careful,
    the URL is case sensitive!" (p99)
    "8770 WBM client: https://nms.company.com:8443 Select the following menu: NETWORK MANAGEMENT" (p254)
    "Click in the session icon NETWORK ADMINISTRATION ... Forgotten your password?" (p392-393)
  summary: |
    三个入口精确口径：客户端程序下载 https://<FQDN>/cgi-bin/OmniVista8770Client.exe（URL 大小写敏感，
    需管理员凭据，文件落 Downloads）；WBM 主入口 https://<FQDN>:8443（主菜单 NETWORK ADMINISTRATION /
    NETWORK MANAGEMENT，忘记密码入口在会话图标下）；日志 Web 别名 https://<FQDN>/nmclog/。端口总表：
    80（Apache HTTP，不可改）、8443（HTTPS）、389/636（LDAP/LDAPS）、8080（Wildfly）、3306（MariaDB
    对外管理口径）、162（SNMP trap）、25（SMTP 默认）。
  conditions: 浏览器版本要求见 p01；首次访问 8443/nmclog 需接受自签证书例外
  tags: [metric, urls, ports]
```

## 任务覆盖自检（task ↔ id 映射）

| task_id | 对应 principle 条目 |
|---|---|
| task-01/02 | p01、p04、p05、p06、p07、p45 |
| task-03 | p08、p45 |
| task-04 | p09、p10、p11 |
| task-05 | p12、p13 |
| task-06 | （操作类，主体在 case c06） |
| task-07 | p14 |
| task-08 | p15 |
| task-09 | p16 |
| task-10 | p16、p17 |
| task-11 | p09、p43 |
| task-12 | p20 |
| task-13 | p19、p21 |
| task-14 | p22 |
| task-15/16 | （流程在 case；Topology 边界见 n 系） |
| task-17 | p30、p31、p32、p33、p34、p35 |
| task-18 | p36、p37 |
| task-19 | p23 |
| task-20 | p24 |
| task-21 | p25 |
| task-22 | p26、p27 |
| task-23 | p28 |
| task-24 | p29 |
| task-25 | p41、p42 |
| task-26 | p38、p39、p40 |
| task-27 | p44 |
| task-28 | p02、p03、p39 |
