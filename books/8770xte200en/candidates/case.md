# 案例/实验/操作序列候选 — OmniVista 8770 (8770XTE200EN Ed47)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号）标注"实验口径"。
> 条目说明: 全书 27 个 How-To 实验章 → 27 条（c01-c27），按原书页序排列。

```yaml
- id: c01
  title: Windows 2022 Server 上安装 OmniVista 8770 服务器（配置/组件/补丁/首连）
  type: lab
  source_pages: p65-88
  source_chapter: Server installation on Windows 2022 Server
  source_quote: |
    "Computer name: nms, DNS suffix: company.com ... IP address: 192.168.1.70, Subnet Mask:
    255.255.255.0, Default gateway: 192.168.1.254, DNS server: 192.168.1.250" (p66-67)
    "License file: 8770 license without directory lock! ... Directory manager password: superuser
    ... Do you want to use the PABX's cost center management method? Yes" (p69)
    "Patch installation terminated: success" (p78)
  steps: |
    1. 配置 Windows 数据：NTFS 分区保留默认目录只换物理盘；Settings > System > About > Rename this
       PC (advanced) > Change 设计算机名 nms > More 设 DNS 后缀 company.com（不勾"域成员变更时更改主
       DNS 后缀"），改后重启。
    2. 设 IP：Network Connections > Ethernet > 属性 > IPv4：IP 192.168.1.70 / 掩码 255.255.255.0 /
       网关 192.168.1.254 / DNS 192.168.1.250（实验口径）。
    3. 前提：服务器先接入网络（静态 IP+网关）；iso 拷到本地盘（如 C:\soft），不得从网络/挂载/vSphere 装。
    4. 双击 ServerSetup.exe（Win10/11 需右键"以管理员身份运行"）→ Yes 接受自动生成设备管理证书 → 选
       English US → Install 装 MariaDB 与 Visual C++ 包 → Next。
    5. 接受许可 → Change 选许可文件 → License verification 全部 Valid → Next → 公司名 Ale（装后不可改）
       → 四目录 C:\8770、C:\8770\SunONE、C:\8770\data、C:\8770_ARC 均用 C: 分区 → 邮件服务器留默认跳过
       → LDAP 389 / LDAPS 636 + 勾 Windows 防火墙配置 → 目录管理器密码 superuser（实验口径）→ AdminNmc
       → 国家 United States → 成本中心 Yes → 预配置不选 → Install → Finish → Yes 重启。
    6. 关 IE ESC：Server Manager > Local Server > IE Enhanced Security Configuration，Administrators
       与 Users 都设 Off，重开 Server Manager 确认。
    7. Defender 排除：设置 > 更新和安全 > Windows 安全中心 > 病毒和威胁防护 > 管理设置 > 排除项 >
       添加文件夹 C:\8770。（6-7 为 Alarms/Topology 启用前提）
    8. 装补丁：补丁拷入 C:\8770\install\patches → 管理员运行 PatchInstaller.exe → 查
       C:\8770\install\Patch_Installer.log 尾部 "Patch installation terminated: success"；已装清单查
       Patch_history.ini；安装设置存档查 C:\8770\RestoreContext.ini。
    9. 首连：Start > OmniVista > OmniVista 8770 Client → 服务器 FQDN（nms）或 IP，端口自动 636 →
       AdminNmc / superuser → 强制改密 Superuser01*（实验口径）。
  verification: |
    8770 管理员会话打开（p85）；Patch_Installer.log 尾部成功消息（p78）；服务器信息存入
    C:\Users\<账户>\nmc5_5.2.cfg，下次直达登录页（p85）。
  conditions: 内存占用 <85% 才能安装；许可文件为无目录锁的 8770 license（实验口径）。
  tags: [lab, installation, windows2022, patch]

- id: c02
  title: Windows 2019 Server 上安装 OmniVista 8770 服务器（与 2022 并列流程）
  type: lab
  source_pages: p618-639
  source_chapter: Server installation on Windows 2019 Server
  source_quote: |
    "IP address: 192.168.1.70 ... Preferred DNS server 192.168.1.100 ... The DNS Server is the
    Ecosystem virtual machine (IP@: 192.168.1.100, FQDN: eco.company.com), used in our classroom
    configuration." (p621)
    "In case of installing the OmniVista 8770 server on Windows 8.1, 10 and 11, you must run the
    software program with administrator rights." (p623)
  steps: |
    1. 配置计算机名 nms + DNS 后缀 company.com（经 System info > Change settings，其余同 c01 步骤 1）。
    2. 设 IP 192.168.1.70 / 255.255.255.0 / 192.168.1.254 / DNS 192.168.1.100（实验口径：2019 章用
       ecosystem 虚机做 DNS，与 2022 章的 192.168.1.250 不同）。
    3-7. ServerSetup.exe 安装参数、补丁、IE ESC 与 Defender 排除均与 c01 步骤 3-7 相同。
    8. 首连 AdminNmc / superuser 改密 Superuser01*。
  verification: |
    8770 管理员会话打开（p639）；书中注明连接信息存 C:\Users\<账户>\nmc5_5.1.cfg（p639，注意文件名
    写的是 5.1，见 n45）。
  conditions: 2019 章为旧版沿用内容（无 WMIC 附录）；参数差异仅 DNS 指向。
  tags: [lab, installation, windows2019]

- id: c03
  title: 安装 8770 客户端并首次连接（URL 下载 / WMIC / Zulu 放行）
  type: lab
  source_pages: p96-106
  source_chapter: OmniVista 8770 - Client installation
  source_quote: |
    "Configure the PC client with the following parameters: IP address: 192.168.1.11 ... Send a
    ping to the OmniVista 8770 Server (ex. ping nms.company.com)" (p97)
    "Enter the following URL: https://<8770 FQDN>/cgi-bin/OmniVista8770Client.exe Be careful,
    the URL is case sensitive!" (p99)
    "By default, Windows Defender firewall blocks the access Zulu Platform x32 Architecture
    module. ... Select 'Private networks, such as my home or work network'. Then, click on
    'Allow access'." (p102)
  steps: |
    1. 客户端 PC 配 IP 192.168.1.11 / 255.255.255.0 / 网关 192.168.1.254 / DNS 192.168.1.250（实验
       口径）；命令行 ping nms.company.com 验证连通（无 DNS 时在 hosts 加 "192.168.1.70 nms
       nms.company.com"）。
    2. （Win11 22H2+）装回 WMIC：Settings > System > Optional features > View features > 搜 WMIC >
       安装。
    3. 浏览器打开 https://nms.company.com/cgi-bin/OmniVista8770Client.exe（大小写敏感；DVD 内
       ClientSetup.exe 流程书中标注"仅供信息、勿执行"）→ AdminNmc/Superuser01* 认证下载。
    4. 运行 OmniVista8770Client.exe：装 Windows 前置包 → 接受许可 → 默认目录 C:\Client8770 5.2\ →
       Install → Finish（安装日志 Documents and settings\<用户>\Local Settings\TEMP\
       OmniVista8770Client_install.log）。
    5. Start > Programs > OmniVista 8770 R5.2 启动：服务器名 nms、端口 636；Defender 弹窗对 Zulu
       Platform x32 选"专用网络"Allow access。
    6. 登录 AdminNmc / Superuser01*，勾选保存参数。
  verification: |
    登录成功进入管理会话；Help > Connected client(s) 显示已连客户端列表（p102）；连接信息存
    C:\Users\<账户>\nmc5_5.2.cfg。
  conditions: 安装账户需本地管理员；剩余磁盘 ≥750MB（JVM 底线）。
  tags: [lab, client-installation, wmic]

- id: c04
  title: 注册 OXE 节点（前置核查 → 三级声明 → 同步 → 实时核验 → 排障）
  type: lab
  source_pages: p118-128
  source_chapter: OXE node registration
  source_quote: |
    "Check that the OXE has the following configuration: Host name: csa, Network number: 1, Node
    number: 1, Physical IP address: 192.168.1.1 ... Main name: csm, Main IP address: 192.168.1.3" (p119)
    "Name Define the OXE name (i.e. oxe). ... IP address Enter the OXE main IP address (i.e.
    192.168.1.3). ... Alarm reception mode Select Permanent IP connectivity" (p123)
    "Create a user 31234 ... Check that the user is available in the Configuration application
    tree structure" (p127)
  steps: |
    1. 前置核查：PuTTY SSH 到 OXE 角色 IP 192.168.1.3 → siteid 确认节点号 1/网络号 1；su -（
       Superuser2580* 实验口径）→ netadmin -m → 5 Role addressing → 1 View 确认主用地址 csm
       192.168.1.3；确认 GD 192.168.1.13 在服务。
    2. 声明网络：8770 Configuration 应用右键 nmc > Create > Network：名称 ale、网络号 1。
    3. 声明子网：右键 ale > Create > Subnetwork：名称 abc1、子网号 1（须等于 OXE 网络号）。
    4. 声明 OXE：右键 abc1 > Create > OmniPCX 4400/Enterprise：名称 oxe、节点号 101（=1×100+1）、
       IP 192.168.1.3、FTP 账号 adfexc/Superuser2580*、勾 Process configuration、告警接收模式
       Permanent IP connectivity；Software download 页填 mtcl/Superuser2580*；Connectivity 页勾 SSH
       connection + 主机名 oxe。
    5. 同步：右键 oxe > Synchronization > Partial > Global → 选 of the task → Status 页 → Apply →
       Refresh 看日志至成功。
    6. 核验同步结果：OXE 下生成 Users/Hardware 等分支；Data Collection 页 Date of last modification
       显示最后同步时间。
    7. 实时同步核验：OXE 侧 mgr 建用户 31234 → Alarms 应用 Event 页收到事件（hostname=MANAGER）→
       Configuration 树 TelephonicDevices 出现 31234。
  verification: |
    同步成功消息显示（p126）；用户 31234 在 8770 树中出现且 NMCSyncLdapPbx_1.log 记录 "Processing
    event: creation of Subscriber directoryNumber: 31234"（p127）。
  conditions: 排障：实时同步失效时 Service Manager 停止 NMC Alarm server（自动重启）后重测（p128）。
  tags: [lab, oxe, node-registration, synchronization]

- id: c05
  title: 配置 OXE SSH 安全访问（核查/信任主机/MindTerm/SFTP）
  type: lab
  source_pages: p129-136
  source_chapter: OXE SSH
  source_quote: |
    "Security with SSH: yes ... netstat -an | grep :22 ... tcp 0 0 0.0.0.0:22 0.0.0.0:* LISTEN" (p130)
    "Try to establish a Telnet session from PuTTY application to the PCX. Check that the access
    is refused." (p132)
    "The public key is stored in the folder Users\Administrators\AppData\Roaming\MindTerm\hostkeys." (p134)
  steps: |
    1. 核查 SSH：PuTTY SSH 到 Call Server，su - 后 netadmin -m → 2 Show current configuration 确认
       "Security with SSH: yes"；netstat -an | grep :22 见 LISTEN、grep :23 无输出。
    2. 查可信主机：netadmin -m → 11 Security → 1 Firewall (iptables) Configuration → 3 Restricted
       Access Configuration → 1 View trusted hosts（实验清单：gateway 192.168.1.254 / oms 192.168.1.13 /
       omnivista 192.168.1.70 / pc 192.168.1.11）。
    3. 验证 telnet 被拒：PuTTY telnet 到 OXE 应拒绝。
    4. 8770 侧配置：Configuration 应用选 OXE > Connectivity 页勾 SSH connection，Host name 填唯一名
       （oxe；字母开头，仅字母数字与 . , - _）。
    5. 建立安全连接：树中右键 oxe > Connect → mtcl / Superuser2580* → 接受 MindTerm 许可 → 确认创建
       home 目录 / hosts 目录 / 公钥 → 确认会话 → SSH 连接建立。
    6. SFTP：MindTerm 菜单 Plugins > SFTP File Transfer。
    7. 加可信主机（Add-on）：netadmin -m → 11 → 1 → 3 → 2 Add trusted host → 输 pc2 → y 入 hosts 库 →
       输 192.168.1.9 → 0 逐级回主菜单 → 22 Apply modifications → 0 退出 netadmin。
  verification: |
    SSH 会话在 8770 Configuration 内建立（p134）；netstat 中出现 192.168.1.3:22 与 192.168.1.70 的
    ESTABLISHED（p130）；新可信主机 apply 后生效（p136）。
  conditions: OXE N3 起可信主机管理强制；公钥存 MindTerm\hostkeys。
  tags: [lab, ssh, security, oxe]

- id: c06
  title: OXE 配置界面高效操作（搜索/冻结/网格文件切换/属性选择/图形视图/导入导出）
  type: lab
  source_pages: p158-167
  source_chapter: Configuration interface - OmniPCX management
  source_quote: |
    "Open the 8770 Configuration application ... Right click on the 'OXE' or 'OT', Select the
    'Configure' option" (p159)
    "Right click on the desired column (ex. Local Features), Select 'Freeze' ... The column is
    frozen and is locked on the left" (p160)
    "Select 'Export All Grids' or 'Export Selected Grid(s)' ... 2 types of extension are
    available : .txt or .prg" (p165)
  steps: |
    1. 打开配置界面：Configuration 应用右键 OXE > Configure。
    2. 搜索：Search 区输入条件（示例：Prefix Meaning = Local Features）显示全部匹配前缀。
    3. 冻结列：右键 Local Features 列 > Freeze，该列锁定在左，滚动他列时保持可见。
    4. 网格/文件切换：选中 Wake-up/appointment reminder 行 > Switch grid display 按钮切 File 视图；
       再点切回。
    5. 属性选择：回到 Grid > 右键行 > Attributes Selection… > 取消勾 Prefix Meaning 与 Prefix
       Information > 重跑搜索刷新视图验证列隐藏；再全选恢复。
    6. 图形视图：右键用户 Brigitte Baker > Graphical View > 选可编程键 > 下方字段配置（Function 如
       Programmed/Multiline、Content 如 31500、Mnemo 显示文本、UTF-8 Mnemo、Locked 是否锁键）。
    7. 树导出：树中选前缀条目 > 右键 Export > 路径 + 文件名 export1 + 扩展名 .txt 或 .prg > Save。
    8. 网格导出：Grid 视图右键 > Export All Grids / Export Selected Grid(s) > export_grid.txt。
    9. 树导入：树中选 Prefix Plan 文件夹 > 右键 Import > 选 export1.txt > Open > 勾导入类 > OK。
    10. 网格导入：Grid 视图选行 > 右键 Import Grid… > 选 export_grid.txt > Open。
  verification: |
    冻结列/隐藏属性即时生效；导出文件生成；导入后数据出现且在导入文件来源目录生成日志文件（p167）。
  conditions: 搜索/冻结/网格操作均在 OXE 图形配置界面内。
  tags: [lab, configuration-ui, import-export]

- id: c07
  title: 创建 OXE Profile 与 Key Profile 并引用建户
  type: lab
  source_pages: p182-195
  source_chapter: Users application - OXE user creation
  source_quote: |
    "Create 1 profile named BASIC. Profile name: BASIC, Directory number: A0001, Public network
    COS: 3, Phone feature COS: 4, Connection COS: 5" (p183)
    "Right click on the Users folder, Select Filter…, Select the filter 'Where Set Function Equal
    Profile'" (p186)
    "Warning: TO RETRIEVE THE KEY PROFILE INFORMATION IN THE OMNIVISTA 8770, A SYNCHRONIZATION
    MUST BE LAUNCHED" (p194)
  steps: |
    1. 启用继承：Configuration 应用右键 OXE > Configure > System > Other System Param. > System
       Parameters > 勾 Use profile with auto. recognition。
    2. 建 profile：配置界面右键 Users 文件夹 > Create：General Characteristics 页 Directory number
       A0001（空闲物理号）、Set Function=Profile；Profile 页名称 BASIC（大写）；Rights 页 Public
       Network COS=3 / Phone Feature COS=4 / Connection COS=5；All 页按需设继承默认值。
    3. 查看 profile：Users 文件夹右键 Filter… > Where Set Function Equal Profile > 确认 BASIC 可见。
    4. 数据实时性：OXE 发事件实时更新 8770 数据，无需同步（profile 显示）。
    5. 建户引用：Users 应用右键分支 Training > Create user：User type=OXE、姓名 Bruno Black、OXE=oxe、
       号码 31003、设备 IP Touch 8078s、OXE Profile=BASIC。
    6. 核验：Users 应用出现 Bruno Black；Configuration 界面 Users 文件夹可见该用户且 Rights 页三个
       COS 已按 profile 值填入。
    7. （附录）Key Profile：建 set profile PROFILE_8068S（Set type=IP Touch 8068s、Set Function=
       Profile）→ Filter 显示后选中 → Progr. Keys 文件夹设 5 个键（如键 5=Programmed 31010）→
       Set Profile > 1 > Profile Features 右键 Create：Set Physical Type=IP Touch 8068s、Key
       Function=Company、Profile Directory Number=A5000 → 同步一次取回键信息 → Users 应用建户时
       Key Profiles 选 Company。
  verification: |
    用户 Bruno Black 在 Users 应用与 OXE 配置中一致、COS 继承生效（p189）；带键 profile 的用户建户后
    可编程键自动下发（p195）。
  conditions: Profile 名称大写；继承开关未开则 key profile 不工作（p190 Warning）。
  tags: [lab, profiles, users, key-profile]

- id: c08
  title: 配置空闲号码段与 Meta profile 并自动建户
  type: lab
  source_pages: p203-210
  source_chapter: Meta profiles for OXE users
  source_quote: |
    "Create a free numbers range list on the OXE: Name: Range 31050-31059, Range beginning: 31050,
    Range end: 31059" (p204)
    "Warning: SYNCHRONIZATION IS REQUIRED TO RETRIEVE THE FREE NUMBER RANGES FROM THE OMNIPCX
    ENTERPRISE!" (p205)
    "Create the user 'Bobby Bell' by using the Meta profile OXE meta profile – 8078s" (p208)
  steps: |
    1. 建号段：OXE 配置界面 System > 1 > 右键 Free Numbers Ranges List > Create：名称 Range
       31050-31059、起 31050、止 31059、Digits Authorized 保持默认。
    2. 同步：右键 OXE > Synchronization > Partial > Separate（四步：of the task / Status / Apply /
       Refresh）→ Configuration 应用中可见号段。
    3. 建 Meta profile：Users 应用 Profiles 页右键 Meta profiles > Create > OXE meta profile：名称
       OXE meta profile – 8078s、OXE 节点 oxe、号段 Range 31050-31059、设备 IP Touch 8078s、OXE
       profile BASIC、OT 应用 None。
    4. 建户：Users 页右键根（Ale）> Create user：User type=OXE、Mr. / Bell / Bobby → OXE Meta-Profile
       选 OXE meta profile – 8078s → OXE 属性区自动填充 → 检查可改 → Apply。
  verification: |
    Users 页出现 Bobby Bell（p209）；OXE 配置界面 Users 中参数正确（号码取段内首个空闲号）（p210）。
  conditions: 号段建后必须同步；邮箱号字段在选了 OXE profile 时不可用（p207）。
  tags: [lab, meta-profile, numbering, users]

- id: c09
  title: Users 应用批量开通（导出模板 / 改文件 / 导入核验）
  type: lab
  source_pages: p219-224
  source_chapter: Mass provisioning from Users application
  source_quote: |
    "export the user Bobby Bell in a file named Bell_export.txt ... Right click and select Export
    user for template" (p220)
    "action[ADD;MODIFY;DELETE] ADD ... lastName XXXX ... oxeMetaProfile OXE profile – 8078s ... If
    you want to customize the directory number for an OXE user, you need to fill in the
    oxeDirectoryNumber field" (p221-222)
    "Right click and select 'Import user data' in the contextual menu. Select 'From local drive'.
    ... On Files of Types field, select All Files" (p223)
  steps: |
    1. 导出模板：Users 应用选中 Bobby Bell > 右键 Export user for template > 本地盘存 Bell_export.txt
       （Text document）。
    2. 编辑：Excel 打开，改出 Berta Bernstein：action=ADD、userType=OXE、lastName=Bernstein、
       firstName=Berta、hierarchy=/Ale、Salutation=MRS、oxeMetaProfile=OXE profile – 8078s；其余 NULL
       保留（uid/password/email/号码等自动）；action 字段可选 ADD/MODIFY/DELETE。
    3. 导入：Users 树根右键 Import user data > From local drive > 文件类型 All Files > 选
       Bell_export.txt > OK → "OXE user has been created successfully"。
    4. 任务核验：Scheduler 应用 > Import user data 条目 → 绿态 + Status 页 ADD 成功 + Log 消息。
  verification: |
    Berta Bernstein 出现在 Users 树（p223）；Scheduler 导入任务成功（p224）。
  conditions: 模板导出为部分表头+优化键值（XXXX/NULL 语义见 p16）。
  tags: [lab, mass-provisioning, import-export]

- id: c10
  title: WBM 轻客户端用户开通（单建 + 批量模板导改导）
  type: lab
  source_pages: p253-260
  source_chapter: User provisioning from 8770 WBM client
  source_quote: |
    "8770 WBM client: https://nms.company.com:8443 Select the following menu: NETWORK MANAGEMENT" (p254)
    "Type Select the template from a selected user (i.e. Users data) ... File format Select the
    format to be exported (i.e. TXT) ... Mode Select when the export process will be proceeded
    (i.e. Immediate)" (p258)
    "Action[+;-;#] Replace the # by the + character, to add a new user. ... secretCode@details
    Replace the starts string by NULL." (p259)
  steps: |
    1. 单建用户：WBM 登录 https://nms.company.com:8443（AdminNmc/Superuser01*）> NETWORK MANAGEMENT >
       Users 应用 > Add：User 页填姓 Buckler 名 Beatriz → Main device 页选 OXE=oxe、号码 31014、机型
       IPTouch 8078s、profile BASIC → 创建。
    2. 核验单建：8770 thick client Configuration 界面 Users 文件夹可见 Beatriz Buckler，COS 为 profile
       值。
    3. 批量导出：Users 应用选 Bruno Black > Export：Type=Users data、File format=TXT、Mode=Immediate →
       文件落 Windows 下载目录（userdata-1234567890123.txt）。
    4. 编辑：改 action # → +；sn Black→Buffy；givenname Bruno→Bill；uid→Bill Buffy；telephonenumber
       31013→31015；secretCode 字符串→NULL（新户默认密码 1234）。
    5. 批量导入：Users 应用 > Import：Mode=Immediate > Choose file 选编辑后文件 → Activity report 核验。
  verification: |
    Bill Buffy 出现在用户列表（p260）；Activity report 显示导入成功。
  conditions: WBM 与 thick client 批量文件互不通用；导出模板仅落下载目录（p249）。
  tags: [lab, wbm, users, mass-provisioning]

- id: c11
  title: 声明 OXO Connect 节点（布线核查 / OMC 安装连接 / 声明 / 同步 / 在线离线）
  type: lab
  source_pages: p640-667
  source_chapter: OXO Connect node declaration
  source_quote: |
    "Connect the PowerCPU LAN port to the LANX16-2 (or to a switch). ... From a Premium set ...
    Menu tab, click on Operator ... Password Letacla1 ... Select Netw.config. Select IP@CPU." (p641-643)
    "Name Enter the OXO Connect name (i.e. oxo connect), Node number Enter the node number (i.e.
    80), IP address Enter the Power CPU EE IP address of the OXO Connect (i.e. 151.1.1.246)" (p657)
    "Right click on OXO Connect, Select Configure > Online mode ... Password Enter Installer
    password (i.e. Alcatel1)" (p663)
  steps: |
    1. 布线：OXO 接电源、CPU 经 lan Switch 板接入 LAN、接话机与 T0；PowerCPU LAN 口接 LANX16-2 或
       交换机，IP Touch 与 PC 同交换机。
    2. 查 IP：Premium 话机 Menu > Operator（密码 Letacla1 实验口径）> Expert > Netw.config > IP@CPU →
       MAIN@=151.1.1.246（实验口径）。
    3. 装 OMC：BP 网站下载 zip → 解压传 8770 服务器 → 右键 Setup.exe 以管理员运行（首装需 .NET
       Framework）→ 语言 English → 默认目录 → 国家 France → 目标产品 France Alcatel Lucent → 显示语言
       English+French → Install → Finish。
    4. OMC 连接：双击 OMC → Expert 会话 → Communication > Connect → LAN/WAN → IP 151.1.1.246 →
       服务器认证默认启用 → installer 密码（cold reset 后 pbxk1064，本实验 Alcatel1）→ Security Alert >
       View Certificate > Install Certificate > Current User > 将证书放入"受信任的根证书颁发机构" →
       完成导入 → 按提示改所有会话账户密码（OXO R10 起强制）→ 首连必填客户信息（* 必填）→ 连接图标
       确认在线。
    5. 8770 声明：Configuration 应用右键 nmc > Create > Network（ale/1）与 Subnetwork（abc1/1）→ 右键
       abc1 > Create > OmniPCX Office：名称 oxo connect、节点号 80、IP 151.1.1.246、FTP password
       Pbxnmc12（NMC 账号，取计费票用）、勾 Process configuration、Alarms reception mode=Permanent IP
       Connectivity、Accounting process=Detailed accounting、成本中心 CC_OXOC、启用 VoIP performance
       process；Connectivity 页 Omc config password=Alcatel1。
    6. 共享目录：Preferences > Configuration > OXO Preferences > User parameters > Secure Shared
       Directory 启用，填 8770 服务器 Windows 会话账号 Administrator/superuser（供 \\nms\OXO-databases
       访问；参数错误需重启 8770）。
    7. 同步：右键 OXO Connect > Synchronization（四步操作）→ 成功消息 → Configuration 中可见 OXO 版本
       号；Data Collection 页 Last connection date 即最后同步时间。
    8. 运维会话：右键 OXO Connect > Configure > Online mode（Expert + installer 密码直连 OMC）；
       Offline mode 为 File > Open 打开本地数据库副本离线编辑。
  verification: |
    同步成功消息（p661）；8770 检索到 OXO 软件版本（p661）；声明节点换算 1×100+80=180、备份目录
    C:\8770_ARC\OXO\data\1\1\180（p658）。
  conditions: Network/Sub-network 已有 OXE 声明时直接复用（p656 Notes）。
  tags: [lab, oxo-connect, omc, node-registration]

- id: c12
  title: 配置 OXE 告警上送 8770（incident manager / incident filter / rstcpl 验证）
  type: lab
  source_pages: p283-289
  source_chapter: Alarms application - OXE
  source_quote: |
    "Configure the OmniVista 8770 Server to receive OXE alarms ... Alarm reception mode Permanent
    IP connectivity" (p284)
    "Network severity: None, Topological network: YES ... Check alarms reception: Reset a coupler
    (rstcpl <Media Gateway number> <Board number>)" (p285)
    "Filter id: 1125, Network incident: Yes ... Minor alarm #1125 is displayed" (p287-288)
  steps: |
    1. 8770 侧：Configuration 应用选 OXE，确认 Alarm reception mode=Permanent IP connectivity。
    2. OXE 侧 incident manager：配置界面 Applications > 1 > Incident Manager > 1：Network severity=
       None、Topological network=YES。
    3. 验证告警：telnet/SSH mtcl 会话执行 rstcpl 4 0（重启 4 号 MG 0 号板）→ incvisu -t 3 查最近事件
       （#2042 Loss of a GD/GD3 type cpl）→ Alarms 应用树中 OMS 虚拟板（Rack #2）出现 Major #2042。
    4. 定向过滤：对 mtcl 登录事件 #1125——先确认 incvisu 可见（external alarm: "mtcl login"）→ 配置
       界面 Incident Manager 下右键 Incident Filter > Create：Incident Number=1125、Network
       incident=YES（部分库中 #1125 需先创建事件）。
    5. 验证过滤：新开 mtcl 会话 → Alarms 应用 Terminal 0 下出现 Minor #1125。
  verification: |
    Major #2042 与 Minor #1125 分别按预期上屏（p286、p288）；NMCFaultManager_1.log 记录
    active/cleared 事件（p289）。
  conditions: incvisu -t 3 仅显示最近 3 条；重启 coupler 会短暂影响该板业务（实验环境）。
  tags: [lab, alarms, oxe, incident]

- id: c13
  title: 定制告警应用（显示/过滤/删除/签名/字典/邮件/脚本）
  type: lab
  source_pages: p290-306
  source_chapter: Alarms application - Functionalities
  source_quote: |
    "Configure the signature fields: Signature: Jean Dupont, Paul Martin ... Action: Software
    Maintenance, Hardware Maintenance" (p295)
    "Create an alarm filter to send an email to alban.podX@company.com in case of reception of an
    alarm having a major severity" (p302)
    "Create a .bat file in the folder c:\8770\data\alarms\scripts ... msg * /SERVER nms Alarm from
    %1 received at %2" (p305)
  steps: |
    1. 界面操作：Alarms 应用 > Network 区打开；List/Details 模式切换；历史/活动显示切换；点过滤器图标
       只显示本 OXE 的 Major 告警（再点关闭）。
    2. 删除告警：右键告警 > Delete（选中层级及子层全从库删）。
    3. 签名与动作：Preferences > Alarms > Alarms Configuration：Signature 页加 Jean Dupont/Paul
       Martin，Action 页加 Software/Hardware Maintenance；Details 模式双击字段选人/选动作 + Remark 自由
       文本。
    4. 字典定制（重命名字段）：8770 服务器上 Start > OmniVista 8770 应用组 > Dictionary customization >
       Open > AlarmReporting.dict → 选语言 → 选属性（Action/Remark/Signature）→ 改译名（Action→
       Operation、Signature→Technician's name）→ File > Save（存 c:\8770\dict\user\
       AlarmsReporting_user.dict）→ 关 8770 客户端 → Service Manager 重启 NMC Service Manager → 重开
       客户端核验字段名已换；重置：打开字典 Edit > Set All to Default。
    5. 邮件通知：先声明邮件服务器（Administration > OmniVista 8770 > Export parameters：Mail server=
       mail-server.company.com，自定义 SMTP 端口格式 server:port，发件人默认 omnivista@<FQDN>）→
       Preferences > Alarms > Alarms Filters：建过滤器名 > 条件 Severity Equal to Major > E-Mail
       Addresses 页填 alban.podX@company.com → OK → rstcpl 4 0 触发 → Alarms 应用见 #2042 →
       Thunderbird（按 pod 选 profile）收件箱收到告警邮件。
    6. 脚本执行：c:\8770\data\alarms\scripts 建 message.bat：msg * /SERVER nms Alarm from %1 received
       at %2 → 建过滤器 Severity Equal to Minor > Script 页填 message.bat 与 $managedobject、
       $notificationtime → mtcl 会话触发 → Alarms 应用见 Minor 告警且 8770 服务器屏幕弹窗（%1=告警
       对象，%2=通知时间）。
  verification: |
    字段重命名后 Details 视图显示 Operation/Technician's name（p300）；邮件到达 Thunderbird 收件箱
    （p304）；脚本弹窗出现（p306）。
  conditions: 字典生效需重启 NMC Service Manager + 重开客户端（p297 Warning）；进阶脚本语法查 Alarms
  Help 7.1.4（p306）。
  tags: [lab, alarms, notification, script, dictionary]

- id: c14
  title: 部署 SNMP Proxy（Windows SNMP 服务 / hypervisor / PCX 激活 / 过滤 / 卸载）
  type: lab
  source_pages: p307-324
  source_chapter: Alarms application – SNMP proxy
  source_quote: |
    "Features menu, scroll down the features menu and tick the SNMP Service ... Click on Add
    Features" (p310)
    "Right click on nmc. Select Create > Hypervisor. ... IP Address Enter the IP address of the
    SNMP hypervisor (192.168.1.11 for example). Do not use FQDN." (p313)
    "Data Collection tab, Managed by SNMP proxy Enabled ... [5/24/2018 1:55:31 PM] SnmpAgent:
    Sending TRAP Add PABX specificValue/trapId:3 pbxKeyId:1/1/101" (p318)
  steps: |
    1. 装 Windows SNMP 服务：Server Manager > Manage > Add Roles and Features > Role-based > 本服务器 >
       Features 勾 SNMP Service（提示加依赖则 Add Features）> Install → Tools > Services 确认 SNMP
       服务运行。
    2. 声明 hypervisor：Administration 应用右键 nmc > Create > Hypervisor：名称 SNMP Hypervisor、IP
       192.168.1.11（不用 FQDN）、协议 V2、trap 端口 162、描述；实验用 Client PC 的 TrapReceiver 模拟
       V2c hypervisor。（V3 版填登录名 + SHA/MD5 认证密码 + DES/AES128 加密密码——书中标注"仅供信息、
       勿执行"。）
    3. 启用 8770 SNMP 代理：C:\8770\bin\ToolsOmniVista.exe → directory manager 密码 → y 停服务 → 选 4
       SNMP → 1 SNMP Agent → y 启用 → 0 退出（自动停用 Windows SNMP、启用 NMC SNMP）→ 查
       8770\log\NMCSnmpAgent_1.log 出现 "SNMP agent started / Connection to LDAP is OK / Connection to
       Alarm Server is OK"；Service Manager 中 NMC SNMP Service 运行。
    4. 激活 PBX 监督：Configuration 应用 OXE > Data Collection 页勾 Managed by SNMP proxy → 日志出现
       "Sending TRAP Add PABX ... 1/1/101" → TrapReceiver 收到 trap。
    5. SNMP 过滤：Alarms 应用 Preferences > Alarms > SNMP Filter → 选产品 + 过滤类型 Correlation
       （Equal True 转发相关告警）或 Diagnostic（号码 1024;1032;1128;1440 或区间 1005-1020）→ 可 +/-
       加 AND/OR 第二条件 → rstcpl 触发告警 → TrapReceiver 验证收到。
    6. （卸载流程"仅供信息"）ToolsOmniVista 4 SNMP → 1 SNMP Agent → y 停用 → Server Manager 移除
       Windows SNMP 功能 → 重启服务器完成。
  verification: |
    NMCSnmpAgent_1.log 的 agent started 与 TRAP Add PABX（p316、p318）；TrapReceiver 显示 trap 明细
    （p318）。
  conditions: Windows SNMP 服务必须装（即使被停用）（p317）。
  tags: [lab, snmp, proxy, hypervisor]

- id: c15
  title: 配置 Topology 标准视图（设置 / 虚拟 ACT / 背景图 / 相关告警核验）
  type: lab
  source_pages: p334-338
  source_chapter: Topology application – Standard view
  source_quote: |
    "Select Preferences > Topology > Configure ... Read Saved Configuration: Custom & standard
    configuration / Custom configuration / Standard configuration" (p335)
    "Select a virtual shelf. Virtual Equipment Deselect the Virtual equipment to display it in the
    Topology." (p336)
    "Select 'EUROPE.gif' image file ... Such maps ... with the standard size of 1100x793, have to
    be stored on 8770\data\topology\maps." (p337)
  steps: |
    1. 应用设置：Network 菜单 > Topology > Preferences > Topology > Configure：Read Saved
       Configuration 选 Standard configuration（改此项需重启 Topology 应用）、Display VPN Links、
       Display OXE Links、Display 8770 server 按需 → 点刷新图标。
    2. 显示虚拟 ACT：Configuration 应用选 OXE 展开树 > Hardware 菜单 > 选虚拟机架 > 取消勾 Virtual
       equipment → 重启 Topology → Standard 页 nmc > ale > oxe 下 Virtual equipment 19 显示。
    3. 加背景图：Standard 页选 nmc > 点背景图图标 > 选 EUROPE.gif > Close → 欧洲地图加载（自定义地图
       gif 1100×793 放 8770\data\topology\maps 后重启 NMC Service Manager）。
    4. 相关告警核验：rstcpl 重启板卡 → Topology 中故障机架出现告警 → 双击故障机架看告警 → 等耦合器
       重新投运后告警自动清除。
  verification: |
    虚拟 ACT 上屏（p336）；地图加载（p337）；告警随 rstcpl 出现并随投运自动清除（p338）。
  conditions: Topology 只显示相关告警（p327 Limits）。
  tags: [lab, topology, standard-view]

- id: c16
  title: 构建 Topology 自定义视图与告警重定向
  type: lab
  source_pages: p339-362
  source_chapter: Topology application - Customized view
  source_quote: |
    "Select the custom tab, Activate the Edit mode" (p341)
    "Click in Create custom view icon ... View name Main Node, Background FRANCE.gif" (p344)
    "Right click on the network element or link. Select Redirecting alarms… option. ... paste the
    alarm on the field Source Object hierarchy." (p358)
    "Warning: FROM RELEASE R11.2 OF THE OMNIPCX ENTERPRISE, ALARM LINKED TO IP PHONE STATUS
    (INCIDENT 386) IS NOT CONSIDERED AS CORRELABLE." (p361)
  steps: |
    1. 编辑模式：Custom 页 > Activate Edit mode，展开定制工具组。
    2. 背景图：Add Background Map 选 Europe → Zoom In/Out 调整 → 拖动居中南欧 → Save。
    3. 建自定义视图：Create custom view 图标 → 点放置位置 → 从 Network 列选被监督对象（OXE）→ 视图名
       Main Node + 背景 FRANCE.gif → 应用 → 移动 nms 图标保证主视图可见 → 树结构与视图同步（双击
       Main Node 进入）。
    4. 网络元素：Create network element → 放置 → 属性（Label=Element #1、图标、短/长描述）→ 应用。
    5. 链接：Create link → 点源元素拖到目标（Element #1 与 nms）→ 标签/说明/线型宽度颜色 → 应用；
       Square link 同法（Element #1 与 Main Node）。
    6. 标签：Create label → 放右上角 → 文本 Customized view + 字号颜色 → 应用。
    7. 多边形背景：Create polygonal background → 六边每边一点、末边双击收尾 → 底色边框色 → 应用；
       Modify polygonal shape 拖角变形。
    8. 矩形底色：Create colored rectangular background → 拖拽定尺寸 → 配色 → 应用 → 同法改梯形。
    9. 默认视角：Default view 图标确认默认位置。
    10. 告警重定向（板卡）：Configuration 界面 Shelf > 4 Media Gateway Large OMS > Board 选 GD4 →
        Ctrl+C → Custom 视图右键网络元素/链接 > Redirecting alarms… > Source Object hierarchy 粘贴 →
        mtcl 执行 rstcpl 4 0 → 该元素上显示告警；右键 > Show Alarms 切到 Alarms 页。
    11. 其他对象同法：T0 中继（MG-BRA 4 > ACT Or SU Events > Behind ACT > Terminal 首个 T0）、TDM 用户
        （MG-UAI 8 同路径）、IP 用户（Hybrid Peripheral ACT > Virtual UA Active 同路径）；8770 自身告警
        从 Alarms 应用复制（NMC > nms > Password policy 选告警 Ctrl+C 粘贴）。
  verification: |
    自定义视图/元素/链接/标签成型（p344-354）；rstcpl 后重定向元素显示 #2042 类告警（p358）。
  conditions: OXE R11.2 起 incident 386（IP 话机状态）不可相关、不能用于 Topology（p361）。
  tags: [lab, topology, custom-view, alarm-redirect]

- id: c17
  title: 配置安全管理（密码策略 / 管理员 / 组 / 单登录 / 解锁 / OXE 访问控制 / TLS）
  type: lab
  source_pages: p382-415
  source_chapter: Security Application
  source_quote: |
    "Configure the password policies: Uncheck the password quality ... To lock the password after
    3 login failures" (p384)
    "Create 4 administrators: user1, user2, Expert1 and Expert2 ... Add user1 to the Accountants
    predefined group ... Validate the single login option" (p385-387)
    "Add Expert1 and Expert2 into the Network experts predefined group ... User Name Enter an
    administrator account ... in uppercase. (exemple : EXPERT1)" (p404-410)
  steps: |
    1. 密码策略：Security 应用 > Password Policy > 修改：取消密码质量、最小长度 4、关历史、关首登改密、
       3 次失败锁定（时长 0=管理员解锁）、关时效（实验放宽口径；字段语义见 p31）。
    2. 建管理员：nmc > 8770 administration > 右键 Administrators > Create > Administrator：建
       user1/user2/Expert1/Expert2，密码 Superuser01*（实验口径；User ID 自动=<名><姓>）。
    3. 入预定义组：Groups > Accountants > Members 字段 > 搜索加 user1 → 新开客户端以 user1 登录核验
       可见应用（计费权限）。
    4. 单登录：Administration 应用选 OmniVista 8770 > 勾 Limit user(s) to single login → user1 已登录
       时第二会话被拒（AdminNmc 与 Normal Administrators 组不受限）。
    5. 锁定与解锁：user1 连错 3 次 → Alarms 应用 NMC > nms > Password policy > Locked user accounts 出
       现 major 告警 → 解锁（a）Security 应用选中 user1 改密；（b）ToolsOmniVista 1 Security → 1
       Password Update → 5 Administrator password update → 输 user1 + 新密（按 0 正常退出）；AdminNmc
       锁定用同工具选项 4；（c）WBM 邮件重置：先声明邮件服务器 + Security 应用 Individual 页给
       AdminNmc 填邮箱 → WBM 登录页 Forgotten your password? → 输 AdminNmc → 收重置码邮件（如
       Kp709sC1V@ 实验口径）→ 输码 + 新密 Superuser03* 进入。
    6. 自定义组：右键 Groups > Create > Group 建My Group（成员 user2）> 8770 Applications >
       Accounting 加 My Group 访问级别 Read + Fault Management=All → 多组取最高原则核验。
    7. OXE Access Profile：Configuration 界面 Preferences > Configuration > Access Profiles… > 选
       Profile 9：Users=All、Trunk groups=Read、其余 Nothing；属性页勾除 UTF-8 外全显示 → Security 应用
       8770 Applications > Configuration 加 My Group：Access Level=All、OmniPCX 4400 Access Level=9 →
       删本地 MIB（Preferences > Configuration > Object Model Save > List > 选 MIB 0 EN-US > Delete）
       → user2 登录开配置界面只见授权对象。
    8. OXE 访问控制：Security 应用把 Expert1/Expert2 加入 Network experts 组 → OXE 配置界面 Security
       and Access Control > 1 > User Access Control 右键 Create：ADMINNMC（大写、启用管理授权/Validity/
       User List 1）→ 重连后 Expert1 打开配置界面先被拒 → Connectivity 页勾 Secure access for system
       management → 再加 EXPERT1 → Expert1 可进、Expert2 被拒。
    9. （重置流程）OXE telnet：mao off → multitool SECURITY_ACCESS → 10 Security access
       reinitialization → 0 退出 → mao on。
    10. （TLS 加固"仅供信息"）ToolsOmniVista → 1 Security → 2 Minimal SSL/TLS release → 5 TLS 1.3 →
        完成后 0 逐级退出。
  verification: |
    user1 第二会话被拒（p387）；锁定告警出现且四路径解锁成功（p388-394）；user2 配置界面只见 profile 9
    授权对象（p402）；EXPERT1 可进 / EXPERT2 被拒（p410-411）；TLS 1.3 启用输出（p415）。
  conditions: 密码时效满足 B+C<A；ToolsOmniVista 不校验密码策略、须按 0 退出。
  tags: [lab, security, password-policy, access-control, tls]

- id: c18
  title: 启用并使用 Audit（启用 / OXE 侧开关 / 日志 / 检索 / 导出 / 报告）
  type: lab
  source_pages: p425-434
  source_chapter: Audit Application
  source_quote: |
    "Browse to nmc > OmniVista 8770 > nms > Service > AuditServer ... Audit process Validate the
    check box to enable the Audit application" (p426)
    "/usr3/mao/mao_hist This file contains the list of mao action performed on the OXE ... 2011/09/20
    16:33:22 CREATE Subscriber 101 31004 (nms|adminnmc)" (p428)
    "Open the System tab. The search options set up by default don't work. Erase all search entries
    and create the following entry: PbxName Not Empty" (p431)
  steps: |
    1. 启用 8770 侧：Administration 应用 nmc > OmniVista 8770 > nms > Service > AuditServer > Specific
       页勾 Audit process + 配审计记录/导出 CSV 保留天数 + Keep one backup。
    2. 启用 OXE 侧：Configuration 应用 OXE > Data Collection 页勾 Process audit；Software download 页填
       mtcl/Superuser2580*（rsh 执行 list_fhdet 转换 mao_hdet 用）；Connectivity 页勾 Secure Access for
       System Management（管理员名记入 mao_hist）。
    3. 产生与核对日志：分别用 AdminNmc、Expert1 在配置界面做增删改 → 查 OXE 上 /usr3/mao/mao_log_hist
       （连接记录 nms|adminnmc）、mao_hist（CREATE/UPDATE/ACTION 行）、/var/log/shell.log（命令历史）。
    4. 检索：Configuration 或 Audit 应用右键 OXE > Synchronization > Audit information（日同步自动）。
    5. 查询：Audit 应用 Operations 页双击行看明细（User 字段广播场景显示源节点 1.2）；System 页先清空
       默认条件再建 PbxName Not Empty；8770 log 页选 nms 看客户端登录登出与 Accounting/Reports 访问
       （先开关一遍应用再查）；最后记录在 Configuration Data Collection 页。
    6. 导出：Audit 应用右键 OXE > Export：Immediate on local drive（目录任选）或 Scheduled on Server
       （固定 8770\Client\data\audit）+ History/Detail 两粒度（8770 log 不适用此导出）。
    7. 报告：Reports 应用 Audit > Predefined Reports > Detailed Reports 复制到 AdminNmc 个人文件夹 >
       右键 Generate Report > 选附加过滤（空=禁用）> Open to View。
  verification: |
    mao_hist 出现 (nms|adminnmc) 标注的 CREATE Subscriber 行（p428）；System 页 PbxName Not Empty 出
    数据（p431）；导出 CSV 落盘（p433）。
  conditions: Audit 仅支持 OXE；System 页默认搜索条件无效。
  tags: [lab, audit, logs]

- id: c19
  title: 报告生成、导出与计划分发
  type: lab
  source_pages: p443-459
  source_chapter: Reports application
  source_quote: |
    "Select Menu Preferences > Reports > Reports Preference ... Maximum number of lines in TXT
    format 4000 ... Maximum number of lines in database 100000" (p444)
    "From Alarms directory, select AdminNmc directory, Right click and select Add > Folder ... My
    Alarms reports" (p445)
    "Schedule the generation of the OmniVista 8770 alarm detailed report. This report will be
    generated every day at 5:00 AM except Saturday and Sunday." (p456)
  steps: |
    1. 大小限制：Preferences > Reports > Reports Preference 核对默认（TXT 4000 行/HTML·PDF·EXCEL 50
       页/X 轴 100 元素/数据库 100000 行），超限报告尾部有截断提示。
    2. 建个人文件夹：Alarms 目录 > AdminNmc > 右键 Add > Folder 建My Alarms reports。
    3. 取定义：预定义目录选 OmniVista 8770 alarm detailed report > Copy > 粘到 My Alarms reports。
    4. 生成两实例：右键报告定义 > Generate Report：Immediate；附加过滤一例全部记录（Notification
       time=This Year）、一例 This Week / Severity 过滤；一般口径 Notification time 选 This year。
    5. 查看：右键生成实例 > Open to View…（导出/打印/搜索/翻页工具条）。
    6. 文件导出：右键 > Export > File > 选 TXT/HTML/PDF/EXCEL > 选位置（默认名=定义名+生成日期）。
    7. 邮件导出：先配邮件服务器（Administration > Export parameters：mail-server.company.com；认证
       SMTP 时填账号/密码/starttls）→ Export > E-MAIL > 目标 alban.podX@company.com + 附件文本说明 >
       选 HTML > OK → 服务器显示成功 + Thunderbird 收件箱核对。
    8. 计划生成：右键报告定义 > Schedule… > 过滤（This Year 等）> Generation Options 可同时打印/导出
       > Simple job > Scheduling 页：Description 改 My scheduled report – OmniVista 8770 alarm detailed
       report、Start Date=As Scheduled 5:00AM、Repeat=Daily、Exclude Days 勾周六周日。
    9. 核验：Scheduler 应用找到任务 > 右键 Execute Now > Reports 确认成功。
  verification: |
    两个报告实例生成（p448）；PDF 落盘与邮件到达（p450、p455）；计划任务执行成功（p459）。
  conditions: 邮件多地址逗号分隔；SMTP 端口冒号后无空格（p452）。
  tags: [lab, reports, scheduling, email]

- id: c20
  title: 编排 Scheduler 任务（简单 job / 同步 job / 任务复制剪切）
  type: lab
  source_pages: p469-487
  source_chapter: Scheduler Application
  source_quote: |
    "Schedule the generation of the Audit report named Detailed Reports. The report will be
    generated every day at 5:00 AM except on Sunday." (p470)
    "Create a job named My audit synchronization to generate an Audit report after Audit
    synchronization. The report will be generated every day at 4:00 AM" (p484)
    "When you add another Job, this one is called jobset. ... if you refresh this one, you will
    see that jobset becomes Job." (p487)
  steps: |
    1. 简单 job：Reports 应用 Audit > Predefined Reports > Detailed Reports 复制到 AdminNmc > 右键
       Schedule… > 过滤向导逐页（Date/Hour=This Week、Node Name/User/Action Performed/Object/
       Broadcasted 均 not empty）> Task Type=Simple job > Scheduling 页：Description=My Audit report –
       Detailed report、Start Date=As Scheduled 每日 5:00、Repeat=Daily、Exclude Days 勾周日；
       Depend Job Options（依赖延迟/Stop on error）；Retry Options（次数/间隔/最大时长）> OK。
    2. 修改与强制执行：Scheduler 选中 job 改 Scheduling/Dependant 参数；右键 Execute now → 报告应用
       核对生成成功。
    3. 同步 job 前提：Scheduler 中确认预定义 OXE Audit synchronization 已成功执行。
    4. 建同步 job：右键 Scheduler > New Job：Description=My audit synchronization、As scheduled 4:00AM、
       Repeat Daily。
    5. 纳入审计任务：Load audit records 复制 → 粘到 My audit synchronization；Fetch audit records 同法。
    6. 挂报告任务：Reports 应用 Detailed report > Schedule… > 过滤同上 > Task Type=Synchronized task >
       选 My audit synchronization job。
    7. 启用：选中 job 右键 Enable（图标变化）> Reports 图标核验全部任务成功。
    8. 任务搬移：Daily Job 中找 Partial synchronization LDAP/PCX 复制 → 粘到 My audit synchronization；
       再用 New Job 建 jobset、Cut 剪切该任务粘到 jobset → 刷新后 jobset 变 Job，形成"审计同步→审计
       报告→LDAP 部分同步"顺序链。
  verification: |
    Execute now 后报告生成（p475）；My audit synchronization 报告全绿（p483）；顺序链按
    同步→报告→LDAP 同步执行（p487）。
  conditions: Maximum start delay 语义（错过超延迟不补跑，见 p24）。
  tags: [lab, scheduler, jobs]

- id: c21
  title: 配置自动维护（五类清除参数 / Purge job / 预定义 job 恢复）
  type: lab
  source_pages: p488-502
  source_chapter: Scheduler application - Automatic maintenance
  source_quote: |
    "Configure the maintenance parameters to: Delete accounting records older than 15 days,
    Delete the hourly traffic Analysis older than 4 days" (p489)
    "Configure the maintenance parameters to: Keep only 100 alarms and 100 events in the database." (p491)
    "In case of deletion or modification of the predefined maintenance jobs, it is possible to
    restore the default configuration by a LDIF import." (p502)
  steps: |
    1. 计费/话务清除：Account./traf./VoIP 应用 > Preferences > Accounting > Accounting preferences：
       Clean PTP hour old than=4（小时级话务）、Clean ticketandaffiliated old than=15（计费记录）（其余
       20 项默认值见 p25）。
    2. 报告清除：Reports 应用 > Reports preferences：Clean taxa Reports=2（天）。
    3. 告警清除：Alarms 应用 > Preferences > alarms > Purge configuration：保留 100 告警 + 100 事件
       （按天+按条数双闸；等效入口 Setup > nmc > OmniVista 8770 > 服务器 > Service > AlarmsServer）。
    4. 审计清除：Audit 应用 Purge configuration：日志保留天数 + 导出 CSV 寿命（等效入口 AuditServer
       Specific 页）。
    5. 文件夹清除：Administration 应用 nmc > OmniVista 8770 > nms > NmcArchive：监控类型（Free disk
       space/Directory size）、双阈值（1/2 阈值触发 minor/major 告警）、路径、Clean-up Delay、Keep one
       backup。
    6. 组 Purge job：Scheduler 右键 Scheduler > New Job 建"Purge" → Weekly Job > Job 下复制 Purge
       Alarms 粘到 Purge → 新建子 job 粘 Clean PTP/Traff Hist → 再建子 job 粘 Clean accounting → 右键
       Purge > Enable → 形成"告警清除→话务清除→计费清除"链。
    7. 执行核验：Execute now + 查数据被删。
    8. 恢复预定义 job（误删/改坏时）：Administration 应用右键 nmc > Import > Immediate on local drive >
       Add and modify > 选 \8770\data\scheduler 下 DailyJob.ldif 或 WeeklyJob.ldif → 重启 NMC Scheduler
       服务 → Scheduler 中任务恢复。
  verification: |
    Purge job 三级链按序执行（p495-501）；LDIF 导入后 Daily/Weekly Job 恢复可见（p502）。
  conditions: 清除由 Daily/Weekly Job 按"删除条件在应用中配置"执行（p468）。
  tags: [lab, purge, maintenance, ldif]

- id: c22
  title: 8770 数据库备份与恢复（维护设置 / 立即备份 / 恢复）
  type: lab
  source_pages: p514-521
  source_chapter: 8770 Maintenance application
  source_quote: |
    "From the 'Setup' menu, click in the '8770 Maintenance' icon ... Preferences-> Maintenance->
    Configuration" (p515)
    "Double-click on 'Databases - Immediate backup' icon ... Save in the default directory" (p517)
    "A backup is dedicated to a software version. It must be restored on a server having the same
    software version." (p519)
  steps: |
    1. 维护设置：Setup 菜单 > 8770 Maintenance > Preferences > Maintenance > Configuration：Backup
       location（默认 C:\8770_ARC\8770Backup；网络盘需额外配置）+ Threshold（Available Disk Space 或
       Maximum Record Volume；单位 %/kB/MB/GB；一/二阈值触发 minor/major 告警）+ Record Life（天或月，
       由 Scheduler 日检超期删除）。
    2. 立即备份：双击 Databases - Immediate backup > 确认位置（Save in the default directory 或
       Search 另选）> 确认图标执行 → 查 C:\8770_ARC\8770Backup 下目录（名 YYYYMMDDHHMMSS）。
    3. 恢复前提：删除 Configuration 中节点 + 删除全部告警；确认备份 RestoreContext.ini 的 nmcVersion
       与目标服务器版本一致。
    4. 恢复：双击 Restore - databases > Backup location 用 Search 选备份目录 > OK > 确认图标启动恢复。
  verification: |
    备份目录生成且含 LDAP/MariaDB/其他数据/RestoreContext.ini（p507、p517）；恢复后数据还原（删除的
    节点与告警重建）（p520）。
  conditions: 备份期间 8770 不可用；跨版本不可恢复。
  tags: [lab, backup, restore, maintenance]

- id: c23
  title: 使用维护工具（8770 Diagnostic / DirManag / HeidiSQL）
  type: lab
  source_pages: p532-538
  source_chapter: 8770 Maintenance tools
  source_quote: |
    "Start-> All Programs-> OmniVista 8770-> Tools-> 8770 Diagnostic ... Press 'N' to select
    'No-Interactive mode'. Enter the LDAP port (389) ... Enter the SQL password (password is: sql)" (p533)
    "Double click c:\8770\bin\DirManag.exe to start the tool ... Port number 389 (LDAPS is not
    supported), Login cn=directory manager" (p535)
    "Start > All Programs > MariaDB 10.5 > HeidiSQL ... User Enter the user login (i.e. dba) ...
    Port Select the default port (i.e. 3306)" (p536)
  steps: |
    1. 诊断采集：Start > All Programs > OmniVista 8770 > Tools > 8770 Diagnostic > 每步回车（交互）或
       N 非交互 → 输 LDAP 端口 389 → 输 SQL 密码 sql → 产出 C:\TS\NMS_周几月日.html 与 zip（zip 交
       ALE 支持开诊断）。
    2. DirManag：双击 c:\8770\bin\DirManag.exe > Connect：主机名 nms、端口 389、登录 cn=directory
       manager（或 adminnmc）、密码 superuser、LDAP V3 → 树展示 → 选条目改值 → Ctrl+S 保存。
    3. HeidiSQL：Start > MariaDB 10.5 > HeidiSQL > New 会话：名 NMS – MariaDB、类型 MySQL (TCP/IP)、
       主机 127.0.0.1、用户 dba、密码 sql、端口 3306 > Save > Open > Databases 页选库 > Query 页执行
       SQL（如 select * from nmc5.organization；输入库名. 后自动补全表名）。
  verification: |
    C:\TS 出现 HTML+zip（p534）；LDAP 树展示（p535）；SQL 查询结果返回（p538）。
  conditions: DirManag 不支持 LDAPS；dba 密码可用 ToolsOmniVista 修改。
  tags: [lab, diagnostic, ldap, sql]

- id: c24
  title: 管理 NMC 服务与日志（Service Manager / TraceType / nmclog）
  type: lab
  source_pages: p554-567
  source_chapter: NMC services and log files
  source_quote: |
    "Click the Select button. Click on Execute option. The rights to start and stop a service are
    now enabled." (p556)
    "Modify the -TraceType Syntax to the following one: -TraceType --1 ... Size of the file: 2,429
    KB instead of 1,640 KB" (p563)
    "ONCE INVESTIGATION IS DONE, DON'T FORGET TO MODIFY THE TRACETYPE ARGUMENT TO DEFAULT SETTINGS" (p564)
  steps: |
    1. 查服务：Start > OmniVista 8770 应用组 > Service Manager → 滚动核对全部注册服务运行态；选中服务
       Properties > Startup 字段区分 Automatic（Windows 拉）与 Manual（NMC Service Manager 拉并监督）。
    2. 停单服务：Select > Execute 取权 → 选 NMC License Server > Stop → Refresh；被监督服务会被自动
       拉起。
    3. 停 NMC Service Manager：同法停 → 其他 NMC 服务连锁停（列表消失）→ Start 拉起（确认 Start）→
       Refresh → 全部服务恢复；注意四个 Automatic 服务（NMC Service Manager/DSEE 控制中心/DSEE/
       MySQL8770）需手动 Start，其余勿手动 Start。
    4. 详细跟踪：Administration 应用 nmc > OmniVista8770 > Scheduler → Argument list 由 -TraceType 0
       改 -TraceType --1 → 记录 C:\8770\logs\NMCScheduler_1/2.log 大小变化（详细模式显著变大）→ 核验后
       改回 -TraceType 0。
    5. 日志查看：文本编辑器开 NMCScheduler_1.log；或浏览器 https://nms.company.com/nmclog/（加安全
       例外 + adminnmc/Superuser01* 认证）→ 点 NMCScheduler_1.log 在线查看。
  verification: |
    停 License Server 后自动重启（p557）；停 Service Manager 连锁停/启全部服务（p560-561）；详细模式
    日志变大（p563）；nmclog 页面显示日志内容（p567）。
  conditions: 详细跟踪拖慢服务器，查完必须改回。
  tags: [lab, nmc-services, logging]

- id: c25
  title: OXE 备份与恢复（备份选项 / 立即与计划备份 / swinst 恢复全链）
  type: lab
  source_pages: p579-593
  source_chapter: OmniPCX Enterprise backup & restore
  source_quote: |
    "From the main menu, select Preferences->Maintenance-> OXE Configuration. Backup location
    (c:\8770_ARC\OXEBackup by default) ... Enable PCX automatic backup" (p580)
    "Double-click on 'PCX – Backup'. Select the type(s) of data to backup. ... Select 'Now', to
    apply a backup process immediately." (p582-583)
    "Select the option Restore mao data by pressing 2 ... You are going to restore mao-ctree from
    cpu disk" (p591)
  steps: |
    1. 备份选项：Network 菜单 > Maintenance > Preferences > Maintenance > OXE Configuration：位置
       c:\8770_ARC\OXEBackup + 勾 Enable PCX automatic backup。
    2. OXE 参数：Configuration 应用 OXE：Data Collection 页勾 Automatic database save；Software
       download 页 mtcl/Superuser2580*；Connectivity 页 Swinst password=Superuser2580*。
    3. 立即备份：Maintenance 选 OXE > 双击 PCX – Backup > 勾数据类型（mao/语音导引/OPS）> 选目录 >
       确认 > Simple job > Start Date=Now > Apply > Status 页 Refresh 至完成 → OXE 上 ll
       /usr4/BACKUP/IMMED 与 /usr4/BACKUP/OPS 核对 → 8770 上 c:\8770_ARC\OXEBackup\1\1\101\<时间戳>
       目录核对。
    4. 计划备份：同路径 PCX – Backup > Simple job > As scheduled 4:00AM + Repeat Daily → Scheduler 中
       Execute Now 核验。
    5. 恢复：先在 OXE 删除部分用户 → Maintenance > PCX – Restore > PCX files to restore 点 MAO >
       Search 选备份目录 > 确认等待完成（文件传回 OXE /usr4/BACKUP/IMMED）→ swinst 恢复：mtcl 会话起
       swinst（swinst 账号）→ Easy 菜单 7 Stop the telephone（y 确认）→ mtcl 重新进 swinst → Expert
       菜单 2 → 4 Backup & restore operations → 3 Restore operations → 1 Restore from cpu disk →
       1 Restore from IMMEDIATE backup → 2 Restore mao data → 确认（securing 填 n）→ Q 退回 → Expert →
       6 System management → 2 Autostart management → 1 Set autostart → Q 退 → Easy 菜单 8 Start the
       telephone → y。
  verification: |
    OXE 与 8770 两侧备份目录出现（p584-585）；恢复完成后被删用户还原（p593）；Autostart 设回（p592）。
  conditions: 停电话期间业务中断且 role address 失效（连 OXE 用物理 IP）；N3 起凭据必须已自定义（p41）。
  tags: [lab, oxe-backup, swinst, restore]

- id: c26
  title: 查询与更新 8770 许可（About / nmc.license / spadmin / 换文件）
  type: lab
  source_pages: p610-617
  source_chapter: 8770 License
  source_quote: |
    "1.1.1. From the OmniVista 8770 Client ... Help menu, Select About" (p611)
    "Browse to C:\8770\etc\. Open the nmc.license file with a text editor" (p612)
    "Rename the nmc.license file into nmc.license.old, Paste the new license file and rename it to
    nmc.license" (p615)
  steps: |
    1. 查询 8770 许可（客户端）：Help > About 看锁与容量。
    2. 查询（文件）：记事本开 C:\8770\etc\nmc.license 看版本/签名/[ALIZE]/[OXE AND ICE]（8770Handle）/
       [Modules] 全部锁值（含 OpenAPI、RTUAuditor）。
    3. 查询 OXE 锁：Telnet/SSH mtcl 会话执行 spadmin → 选 1 Display current counters → Handle 4760=
       123456AB 与 39/42/47/49/50/98/99 各锁值（实验口径）。
    4. 更新许可：Service Manager 停 NMC Service Manager → c:\8770\etc 中 nmc.license 改名
       nmc.license.old → 新许可文件放入并改名 nmc.license → Service Manager 启动 NMC Service Manager →
       客户端 Help > About 核对新锁（实验验证 Directory 锁）。
    5. 用量审计：查 c:\8770\log\NMCLicServer_1.log 各模块 "x/上限 = 百分比 (status=ok)" 行。
  verification: |
    About/文件中锁值与预期一致（p611-612）；spadmin 输出锁表（p613）；更新后新锁生效（p616）；
    日志百分比健康（p617）。
  conditions: 更新期间 NMC Service Manager 停止；许可版本须为 N-1 规则内（p38）。
  tags: [lab, license, update]

- id: c27
  title: 映射网络驱动器（远程共享 / ADM8770 / 服务账号 / 验收）
  type: lab
  source_pages: p668-698
  source_chapter: Map network drive
  source_quote: |
    "Creation of the REPORTS_ECO et BACKUP_ECO folders on the ecosystem server ... Mapp on drive Y,
    the folder \\151.1.1.100\REPORTS_ECO, Mapp on drive Z, the folder \\151.1.1.100\BACKUP_ECO" (p669, p693)
    "Right click on ADM8770 account, Select Properties option, Member of tab ... Enter the object
    name Administrators ... Select the Users group, Click on Remove" (p682-683)
    "Select ExecdEx service, Click on Nt account, Username Enter account in uppercase preceded with
    the following characters .\ (i.e. .\ADM8770)" (p696)
  steps: |
    1. 远程服务器（ecosystem 151.1.1.100）：Server Manager > Tools > Active Directory Users and
       Computers > Users > New > User 建 ADM8770（密码 superuser 实验口径；勾不可改密、永不过期）。
    2. 建文件夹：C 盘根建 REPORTS_ECO（报表导出）与 BACKUP_ECO（OXE/8770 备份）。
    3. 共享授权：两文件夹 Properties > Sharing > Share… > Find people 输 ADM8770 > Check Names >
       Read/Write > Share > Done；Advanced Sharing… 限并发用户数（如 3）> Permissions 加 ADM8770 全允许、
       移除 Everyone。
    4. 8770 服务器本地账号：计算机管理 > 本地用户和组 > Users > New User 建 ADM8770（同密；不可改密/
       永不过期）> 属性 Member of 加 Administrators、移除 Users。
    5. 用户权利：Local Security Policy > Local Policies > User Rights Assignment 逐项加 ADM8770：从
       网络访问此计算机 / 作为服务登录 / 作为操作系统一部分 / 调整进程内存配额 / 替换进程级令牌。
    6. 映射：注销 Administrator 以 ADM8770 登录（ESXi 用 Ctrl+Alt+Insert）> This PC 右键 Map network
       drive：Y: = \\151.1.1.100\REPORTS_ECO、Z: = \\151.1.1.100\BACKUP_ECO。
    7. 服务账号：Setup 套件 Administration 应用 > nmc > OmniVista 8770 > nms > Service > 选 ExecdEx >
       Nt account：用户名 .\ADM8770（大写带 .\）+ 密码；SaveRestore 服务同法。
    8. 验收：Setup > Maintenance 8770 > Operations > Databases – Immediate backup > 取消 Save in the
       default directory > Search… > 确认列表出现 BACKUP_ECO 与 REPORTS_ECO 网络位置 > Cancel。
  verification: |
    网络驱动器映射成功（p696）；立即备份对话框可见网络共享位置（p698）。
  conditions: 两服务器账号需同名同密；权利组合可按客户安全策略裁剪（p684 Notes）。
  tags: [lab, network-drive, windows, services]
```

## 任务覆盖自检（task ↔ id 映射）

| task_id | 对应 case 条目 |
|---|---|
| task-01 | c01 |
| task-02 | c02 |
| task-03 | c03 |
| task-04 | c04 |
| task-05 | c05 |
| task-06 | c06 |
| task-07 | c07 |
| task-08 | c08 |
| task-09 | c09 |
| task-10 | c10 |
| task-11 | c11 |
| task-12 | c12 |
| task-13 | c13 |
| task-14 | c14 |
| task-15 | c15 |
| task-16 | c16 |
| task-17 | c17 |
| task-18 | c18 |
| task-19 | c19 |
| task-20 | c20 |
| task-21 | c21 |
| task-22 | c22 |
| task-23 | c23 |
| task-24 | c24 |
| task-25 | c25 |
| task-26 | c26 |
| task-27 | c27 |
| task-28 | （架构理解类任务，无独立 How-To，由讲义覆盖，见 framework f03/f04/f23） |
