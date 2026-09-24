# 案例/实验/操作序列候选 — OpenTouch Suite for MLE (OPENXTE300EN Ed10, R2.6.1)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号）标注"实验口径"。
> 条目说明: 全书 30 个 How-To 实验章 → 30 条（c01-c30），每章一条，步骤保留精确菜单路径。

```yaml
- id: c01
  title: Pod Configuration——起虚机、装 IPDSP、按 POD 号配 SIP 网关与 DID 翻译、验证外呼
  type: lab
  source_pages: p31-37
  source_chapter: OpenTouch Pod Configuration (How-To)
  source_quote: |
    "Registration ID pbxN (where N is your POD number) ... Outgoing username pbxN" (p36)；
    "First external number 33210N41000 (where N is your POD Number) ... First internal number 31000
    Range Size 500" (p37)；
    "Don't forget to specify the TFTP server IP @ in the IP DSP settings." (p34)
  steps: |
    1. 在 Rlab 门户用 Start 按钮启动各虚拟机（OXE、OMS、OTMS、8770、SOT、ECOSYSTEM、PC Client 10/11）。
    2. OXE 出厂数据库已预配置（许可已恢复、FlexLM 已声明、机架/板卡已建、部分用户已建、语音导引已下载、公网 SIP trunk 已建——书中 Implementation 声明）。
    3. [纯虚拟化] 核 Rack/boards：MAIN 站点 Software Rack 3U (OMS)，Rack N°4，Virtual GD4 (slot 0) IP 192.168.1.13/24、MAC 00:50:56:01:01:13（实验口径）。
    4. 核用户：31000 Brad Barkley、31001 Billy Backman（IP DSP，Main 站点）；在 PC Client 10/11 安装并开通 IPDSP（右键 Settings → Network 页签 → TFTP Server Main 填 192.168.1.3=OXE CS Main IP）。
    5. [混合模式] 教室用户改设备类型：Users / <User to modify> / Tsc IP User，IP-Softphone Emulation Set 选 No；Users / <User to modify> / Set Type 按现场话机选型。
    6. 外部 SIP 网关：SIP/SIP Ext. Gateway 选中公网网关，按 POD 号改两参数——Registration ID=pbxN、Outgoing username=pbxN（例 POD 3 → pbx3）。
    7. DID 翻译：Translator/External Numbering Plan/Default DID num. translator → create：First external number=33210N41000（POD 3 → 33210341000）、First internal number=31000、Range Size=500。
    8. 验证外呼：按《SIP Carrier Simulator》文档从 PBX 拨公共号码（如 0110312345 → +33110312345）确认公网 SIP 运营商接入正常。
  verification: |
    外呼测试通过（书中 2.5 External calls："To make sure that access to public SIP carrier is working
    properly, set up some outgoing calls"）；IPDSP 注册上 OXE（TFTP 指向 192.168.1.3）。
  conditions: R-LAB 实验环境；号码规则见 ITSP1（PN=两位 POD 号）。
  tags: [lab, pod, sip-trunk, did, ipdsp]

- id: c02
  title: 用 S.O.T. 以 hosted 模式在 R-Lab 部署 OTMS 虚机（媒体导入 + 项目创建 + 部署）
  type: lab
  source_pages: p66-78
  source_chapter: Use of S.O.T. to deploy OTMS VM on R-Lab infrastructure (How-To)
  source_quote: |
    "IP address: 192.168.1.230 Subnet mask: 255.255.255.0 Gateway: 192.168.1.254 DNS: 192.168.1.254" (p67)；
    "Login admin Password letacla" (p69)；
    "Login: upload Password: sot" (p71)；
    "When installation is finished,OT reboots to present the post-installation wizard." (p78)
  steps: |
    1. [R-Lab 前提] SOT 虚机已在基础设施上部署（书中 Notes）；vSphere 选 SOT 虚机开机，开控制台。
    2. SOT 控制台：按需按 "1" 改键盘类型；选静态网络模式（按 1 static）录入：IP 192.168.1.230、掩码 255.255.255.0、网关 192.168.1.254、DNS 192.168.1.254（实验口径），按 Y 应用。
    3. 客户端浏览器开 https://192.168.1.230（SOT IP），默认登录 admin/letacla（实验口径）；弹出强制改密+安全问题。
    4. 点右上圆图标进 Expert 模式；顶部菜单 Media → Declare media；库选 "Internal SOT local storage"。
    5. 本地存储库须先用 FTP 传文件：账号 upload/sot（Filezilla 上传 bootdvd ISO、OpenTouch core ISO、Fax server ISO、许可文件；文件先从 NAS 拷到本机）。
    6. 回 SOT 界面点 "Refresh media list"，选中文件后点绿色 "Declare media"，确认媒体列表出现 2 个 ISO + 许可。
    7. [R-Lab Warning] OTMS VM 模板已预生成并部署，SOT 不再生成 OVF——软件装载按物理机方式提供 MAC 地址。Projects → Create project → Greenfield project → Next。
    8. 产品选择：OTMS: OpenTouch；页面下方核对各角色媒体已映射；指定许可文件；Info validity=OK → Next。
    9. 项目设置：Project name、OVF Generation 不勾（模板已存在）、Country=France、Timezone=Europe/Paris（实验口径）；目标机参数：Hostname=opentouch、Domain=company.com、Keyboard=french、MAC address=00:50:56:01:01:50、IP address=192.168.1.50、OpenTouch secondary 不勾（实验口径）。
    10. Deploy（保存并立即部署；或 Save 稍后）；SOT 进入等待目标机启动状态。
    11. vSphere 启动 OpenTouch 虚机，开控制台看软件装载；SOT webadmin 亦可看到部署进行中；完成后出提示信息，可停 SOT 虚机。
  verification: |
    OT 虚机安装完成后自动重启进入 post-installation wizard（p78 Notes：OT reboots to present the
    post-installation wizard）。
  conditions: R-Lab 中 OTMS 模板与 SOT 均已预部署；生产部署可勾 OVF Generation 由 SOT 生成 OVF。
  tags: [lab, sot, deployment, otms, media]

- id: c03
  title: OVF/OVA 虚拟机手动导入 ESXi（web client 为主，vSphere client 附录）
  type: lab
  source_pages: p79-87
  source_chapter: OpenTouch Virtual machine deployment (How-To)
  source_quote: |
    "Select the mode to add the new virtual machine: Here: "Deploy a virtual machine from OVF or OVA
    file"" (p81)；
    "Warning VSPHERE CLIENT IS ONLY AVAILABLE WITH ESXI VERSION 6.0 OR LOWER." (p84)
  steps: |
    1. 浏览器输入 ESXi 服务器 IP，用可用账号登录（web client）。
    2. 点添加虚机按钮 → 模式选 "Deploy a virtual machine from OVF or OVA file"（OVA 即 ovf+vmdk 打包，原理相同）。
    3. 命名新虚机 → Next。
    4. 选择 ovf 文件及关联 vmdk → Next。
    5. 选存储位置（datastore）→ Next。
    6. 网络映射：选对应网络（LAN/DMZ…，实验选 DMZ 口径）；Disk provisioning 选 Thin（实验口径）；勾 Power on automatically（部署后自动开机）→ Next。
    7. 核对信息 → Finish。
    8. [附录，仅 ESXi ≤6.0] vSphere client：File → Deploy OVF Template → 选 OVF → Next → 命名 → Next → 选存储 → Next → Thin Provision → Next → 选 VM Network → Finish。
  verification: |
    虚机出现在清单并可开机（书中间接验收：Power on automatically 勾选后自动启动）。
  conditions: vSphere 桌面客户端仅适用 ESXi 6.0 及更低版本。
  tags: [lab, ovf, esxi, deployment]

- id: c04
  title: OTMS Post-installation wizard——from scratch 十步初始化（网络/账户/ACS/许可/证书/备份）
  type: lab
  source_pages: p88-108
  source_chapter: OTMS Post-installation wizard (How-To)
  source_quote: |
    "Hostname Enter the name of the OpenTouch server (lower case mandatory)" (p92)；
    "Root password: superuser Maintenance password: maintenanceuser Administrator password: Admin-8770
    Profile password: Admin-T1 SNMP authentication password: adminsnmp" (p95, 实验口径)；
    "Select "NO" for the question about the update of the System." (p105)
  steps: |
    1. OT 首次开机向导自动启动 → Next → 选 Installation from scratch（恢复路径见 c05）→ Next。
    2. Local settings：Keyboard 按课堂、Country 按地点、Company=Company、Time Zone+勾 D.S.T.（实验口径）。
    3. Network settings：Hostname=opentouch（小写强制）、IP 192.168.1.50、掩码 255.255.255.0、网关 192.168.1.254、Domain=company.com（小写）、DNS server 192.168.1.254、NTP 192.168.1.254（实验口径）；DNS 须满足正反向解析清单（OT/8770/邮件/LDAP/OXE 呼叫服务器 FQDN）；双以太网时两口同 IP 同 MAC；本地 DNS 仅 OXE 无 duplication 时可用。
    4. High availability：保持 Disable（新装机不再支持）→ Next。
    5. OpenTouch core / Host accounts：Root=superuser、Maintenance=otuser/maintenanceuser（用户名留默认）（实验口径）；口令 ≥8 字符无报错弹窗；用户名不得重复且禁用 admin/adminnmc/htuser。
    6. OpenTouch accounts：Administrator=otAdmin/Admin-8770、Profile=otProfile/Admin-T1（口令 ≥8 字符且含大写/数字/特殊字符）、SNMP 用户与认证/加密口令=adminsnmp（实验口径）；抄录全部账号口令（8770 声明要用）；语言四项（管理员/用户 GUI/用户 TUI/会议 Web）按需。
    7. Advanced Communication Server：Stack name=OpenTouch、Node ID=1；Conferencing Service Address 保持 No（VPN-less 专项培训讲）。
    8. Licenses：License Server 选 Local（内嵌）→ Licensing 页 Browse 选 .ice（SOT 指定的在 /opt/sot/licenses）勾选 → Next；或选 External 填 hostname=flex、IP 192.168.1.80、domain=company.com（实验口径）；加密狗挂载（vSphere 给承载 FlexLM 的虚机加 USB Controller+Aladdin USB Device；R-Lab 锚 MAC 无需）。
    9. Certificate：选 Network security ON → Certificate type=Internal + SHA256（推荐）或 External PKCS12（含 passphrase）；（security OFF 用预装通用 CTL，不推荐）。Backup configuration：NFS Host=10.20.30.40、路径 /mnt/db/backup/podX（实验口径）。
    10. Summary 核对全部设置 → Next；System Update 选 NO（无补丁）→ Finish；向导启动 OpenTouch 服务。
  verification: |
    向导结束后 OT 服务启动（p105："The post-installation wizard starts the Open Touch services"）。
  conditions: 实验全部 IP/口令为实验口径；证书档位与备份目的地需客户决策。
  tags: [lab, post-installation, wizard, otms]

- id: c05
  title: Post-installation wizard——restore from archive（用备份重装/迁移）
  type: lab
  source_pages: p106-108
  source_chapter: OTMS Post-installation wizard / 2 Installation (or re-installation) using a backup
  source_quote: |
    "If in this lab, you make installation using a backup, select the archive located (copied) in
    "/tmp" folder. Ask to the trainer for selection and verification." (p106)；
    "When installation is done thanks to an archive, the previous license file will also be restored
    from this archive. But in case of software upgrade, the license version can be different" (p107)
  steps: |
    1. 向导入口选 Installation Type = Restore from archive。
    2. Archive Directory：浏览选择归档所在本地目录（OT 服务器或 USB 设备；实验口径：归档已拷到 /tmp，选前问讲师核对）。
    3. 填 Keyboard、Root Password、Maintenance Username/Password（实验口径同 c04）。
    4. License files installation：如需换许可，Browse 选新 .ice（归档恢复会带回旧许可；软件升级后可借此页替换）→ 勾选文件 → Next。
    5. Summary overview 核对 → Next。
    6. System Update：无补丁选 NO → Finish 启动 OT 服务。
  verification: |
    同 c04：Finish 后 OT 服务启动。
  conditions: 归档传输可用 root 经 SFTP（SOT 预置默认 root 口令 letacla1，实验口径）。
  tags: [lab, post-installation, restore, backup]

- id: c06
  title: 建立系统连接——VM 控制台、SSH 连 OT、Telnet 连 OXE、远程桌面连 8770
  type: lab
  source_pages: p109-121
  source_chapter: Connections to the system (How-To)
  source_quote: |
    "Product : OpenTouch™ Multimedia Services 2.6.1 Version : 18.0.100.003" (p115)；
    "Telnet is authorized on the OXE server. You have to establish a Telnet connection using Putty
    software for example." (p117)；
    "User name Enter a valid login: nms\administrator" (p120)
  steps: |
    1. VM 控制台：vSphere 客户端登录 ESXi（root，实验口令 letacla/课堂 superuser）→ 右键目标虚机 Open Console；R-Lab 场景改用浏览器 web 控制台；vm tools 未装时按 Ctrl+Alt 退控制台。
    2. 核对 OT IP：OT 控制台（root）跑 ifconfig -a（eth0 192.168.1.50，实验口径）。
    3. SSH 连 OT：Putty → Host 192.168.1.50、Port 22、SSH、协议版本 2、键盘 Function keys Linux、收码 UTF-8 → Save → Open 接受主机密钥 → 登录 otuser/maintenanceuser（实验口径）；横幅应显示 Product: OpenTouch™ Multimedia Services 2.6.1、Version 18.0.100.003；OT 不允许 Telnet。
    4. 核对 OXE IP：OXE 控制台跑 ifconfig -a（csa 192.168.1.1、eth0:0 csm 192.168.1.3，实验口径）或 netadmin -m → 3 Local Ethernet interface → 1 View。
    5. Telnet 连 OXE：Putty → Host 192.168.1.1、Telnet、端口 23 → mtcl/mtcl 登录（OXE 未启安全时用 Telnet；启用安全则须 SSH）。
    6. 远程桌面连 8770：8770 服务器上 This PC → Properties → Remote settings → 勾允许远程连接；客户端 Start → Remote Desktop Connection（或 mstsc）→ Computer=192.168.1.70；Options/Local Resources → More 勾 Drives 与即插即用设备；General 页 User name=nms\\administrator → Save As 存 .rdp → Connect。
  verification: |
    SSH 横幅显示 OTMS 2.6.1/18.0.100.003（p115）；RDP 后进入 8770 桌面（p120）。
  conditions: 全部账号口令为实验口径（账号总表 p111）。
  tags: [lab, connections, ssh, telnet, rdp]

- id: c07
  title: SUSE 图形界面操作——startx、终端、工作区、YaST
  type: lab
  source_pages: p122-127
  source_chapter: SUSE OS interface (How-To)
  source_quote: |
    "[root@opentouch ~]# startx" (p123)；
    "Use 3 workspaces with: In workspace 1: terminal window In workspace 2: file browser opened on
    "/opt/Alcatel-Lucent" folder In workspace 3: file browser opened on /var/data/licenses" folder" (p125)
  steps: |
    1. 本地控制台登录 OT（root）后敲 startx 启动图形界面。
    2. 桌面右键 → Open in Terminal 开终端窗口。
    3. 工作区：任务栏切换（最多 4 个）；按书建议布 3 个——WS1 终端、WS2 文件浏览器开 /opt/Alcatel-Lucent、WS3 开 /var/data/licenses。
    4. YaST：Applications 菜单 → System Tools → YaST，查看/改时区、键盘、日期时间等。
    5. 退出：点 Log Off 图标 → Log Out。
  verification: |
    图形界面出现、YaST 可打开设置页（书内以截图演示，无独立测试问题）。
  conditions: 图形界面仅本地控制台（非 SSH）。
  tags: [lab, suse, yast, gui]

- id: c08
  title: 许可文件核查——OXE ice 转载、FlexLM 字段、spadmin 计数、8770 handle、lmutil 系列
  type: lab
  source_pages: p155-166
  source_chapter: Licenses files checking (How-To)
  source_quote: |
    "[root@opentouch licenses]# service flexlmd restart" (p158)；
    ""PANIC flag" value must be "0" ... "Panic Flex" value must be "0"" (p159)；
    "[root@opentouch otuser]# getaluid New ALUID=4A5D2C8A49BA7D6DEAA73A32565E1E9C" (p162)
  steps: |
    1. OXE 的 ice 转入 FlexLM：向导只收了 OT 的 ice；OXE 也用 FlexLM 时，经 sftp（Filezilla）把 OXE ice 传到 OT，再 cp 到 /var/data/licenses（如 OXE.ice）。
    2. root 重启服务：service flexlmd restart；核 final_licenses 下出现 oxes/OXE.ice。
    3. OXE 配 FlexLM 字段：OXE Webadmin（https://<OXE 主地址>）或 mgr → System/Licenses：FlexLM Licensing Enabled=Yes、Flex Server IP=内嵌 192.168.1.50（或外部 192.168.1.80，实验口径）、Flex Server Port=27000、ProductID discovery=Yes、Use Flex License=No；改完必须重启 OXE。
    4. 核许可状态：OXE 控制台 mtcl → spadmin → 1：PANIC Flag / Panic Flex / Panic SWK Check 应全 0。
    5. 读产品 ID 与 handle：spadmin → 2（Display active file）抄 Product-Id（如 K00001111）、Handle 4760（如 123456AB）；Product ID 对应 .ice 中 FEATURE 行。
    6. 读 8770 handle：8770 服务器 C:/8770/etc/nmc.license 编辑查看（或 8770 客户端 Help → About）。
    7. FlexLM 服务与 ALUID：service flexlmd status/restart；物理机 getaluid 抄 ALUID；虚拟化改用 lmutil lmhostid -flexid 读加密狗 ID。
    8. lmutil 系列（$FLEXLM_HOME）：./lmutil -i 看选项；./lmutil lmstat 核服务 UP；./lmutil lmstat -a 看 FEATURE 用量；./lmutil lmhostid 读 MAC；./lmutil lmstat -a | grep K<产品ID> 核 OXE 占用。
    9. 文件 edition：$LICENSE_HOME（内嵌 /var/data/licenses、外部 /opt/Alcatel-Lucent/data/licenses）ls -l 核 OTMS.ice/OXE.ice/alchostid.cfg；more 看内容抄 OTID/Dongle ID/OXE 产品 ID。
  verification: |
    spadmin 三计数全 0；final_licenses/oxes 出现 OXE.ice；lmstat 显示 license server UP 且 ALCFIRM daemon UP。
  conditions: 实验内嵌 FlexLM=OT 服务器（192.168.1.50）、外部 FlexLM=192.168.1.80（实验口径）。
  tags: [lab, licensing, spadmin, lmutil, verification]

- id: c09
  title: 外部 FlexLM 服务器部署——VM 配置、（加密狗挂接）、许可落位、checkLicensing 核验
  type: lab
  source_pages: p167-180
  source_chapter: External FlexLM server deployment (How-To)
  source_quote: |
    "IP Address: 192.168.1.80 FQDN: flex.company.com ... NTP server: 10.20.30.254" (p168, 实验口径)；
    "Copy this license file in $LICENSES_HOME directory (opt/Alcatel-Lucent/data/licenses)" (p177)；
    "============= Potential issue(s): 0 ============" (p178-179)
  steps: |
    1. [R-Lab] FlexLM 虚机已预部署；现场从 My Portal 下载 Flexlm VM 的 ovf 部署到 ESXi/KVM。
    2. FlexLM VM 控制台：选键盘 → 配网络：IP 192.168.1.80、FQDN flex.company.com、掩码 255.255.255.0、网关 192.168.1.254、DNS 192.168.1.254、NTP 10.20.30.254、时区同 OT（实验口径）。
    3. 首登 root/letacla 强制改密（后续可 passwd root）；网络菜单 Edit → Manual IPv4 填参数并勾 Automatically connect；主机名填 FQDN。
    4. [现场] 加密狗：vSphere 选中 FlexLM 虚机 Edit settings → Hardware → Add → USB Device（Aladdin）；内嵌 FlexLM 还须先加 USB Controller；外部 FlexLM 虚机镜像默认带 USB 控制器。（R-Lab 许可锚 MAC，跳过。）
    5. 许可落位：SFTP/SCP（root/自定义口令）传 OTMS.ice 与 OXE.ice（须含 Dongle ID/OT ID/OXE 产品 ID）→ 从 /root cp 到 /opt/Alcatel-Lucent/data/licenses → service flexlmd restart → 核 final_licenses 生成。
    6. 核验：OT 与 FlexLM 两侧各跑 checkLicensing.sh——Server details / Installed licenses（HostID 匹配、到期天数）/ 活动测试（主机名不同、FQDN ping、Flex 服务与 ALCFIRM 运行）/ Potential issue(s)=0；日志在 /opt/Alcatel-Lucent/logs/flexlm/（flexlm_lmlog.log 记 checkout）。
  verification: |
    checkLicensing.sh 两侧 Potential issue(s): 0 且生成日志 zip（/logs/checkLicensing/）；lmstat 显示
    license server UP。
  conditions: 禁用标准 FTP；系统语言保持 CentOS 默认。
  tags: [lab, flexlm, external, dongle, verification]

- id: c10
  title: 内部→外部 FlexLM 切换——解绑/绑加密狗 + ot-config.sh --external_flex
  type: lab
  source_pages: p181-185
  source_chapter: Switch from internal to external FlexLM server in virtualized environment (How-To)
  source_quote: |
    "Disassociate the USB dongle from the OpenTouch virtual machine." (p182)；
    "Enter the command: ot-config.sh --external_flex" (p184)；
    "The operation takes about 5 minutes. Verify the OpenTouch is running." (p185)
  steps: |
    1. [R-Lab] 许可锚 MAC，无加密狗操作，直接到第 4 步；现场：先装好外部 FlexLM（c09）。
    2. 加密狗解绑：vSphere 编辑 OT 虚机属性，选中 USB Device → Remove。
    3. 加密狗绑定：把 Aladdin USB Device 加到外部 FlexLM 虚机（流程同 c09 第 4 步）。
    4. OT 上以 root 执行 ot-config.sh --external_flex → 向导 Next → 填外部 FlexLM 参数（实验口径 flex.company.com / 192.168.1.80）→ Finish。
    5. 等约 5 分钟 → 验证 OT 运行：checkAll.sh；必要时 service opentouchd restart。
  verification: |
    checkAll.sh 全绿、OT 服务运行中（p185）。
  conditions: 切换后许可锚定物变为外部 FlexLM 的加密狗（生产需核对许可形态）。
  tags: [lab, flexlm, switch, ot-config]

- id: c11
  title: 在 8770 中声明 OmniPCX Enterprise——OXE 前置 → 三级建树 → Complete/Separate 同步
  type: lab
  source_pages: p186-192
  source_chapter: OmniPCX Enterprise declaration (How-To)
  source_quote: |
    "Use netadmin –m command to display and update the IP configuration." (p187)；
    "Alarm reception mode Permanent IP connectivity" (p190)；
    "Execute a Complete -> Separate synchronization of the OmniPCX Enterprise." (p191)
  steps: |
    1. OXE 侧核 IP：netadmin -m → 3 Local Ethernet interface（csa 192.168.1.1，实验口径）。
    2. 角色地址：netadmin -m → 5 Role addressing → 2 Add：Name=csm、Address=192.168.1.3（实验口径）。
    3. 节点名：netadmin -m → 17 Node Setup → 2 Update → 节点名 oxe、内部名称解析器 n；离开前选 20 'APPLY MODIFICATION'（勿漏）。
    4. 节点/网络号：mgr 或 OXE Webadmin → System → Review/Modify：Node Number=1、Network Number=1（ABC 网络，实验口径）；siteid 或提示符 (101) 核验。
    5. 实时同步：System → Review/Modify → 47xx directory – 4400 Synchro = True。
    6. 8770 建 Network：Configuration 应用 → 右键 Create → Network：Name=Logical-Network、Network number=1。
    7. 建 Subnetwork：选中网络右键 Create → Network：Name=ABC-Subnetwork、Subnetwork number=1（=OXE 网络号）。
    8. 声明 OXE：子网右键 Create → OmniPCX 4400 Enterprise：Name、Subnetwork-Node number=101（=1×100+1）、IP address=192.168.1.3（主 IP）、FTP Username/Password=adfexc/adfexc、Process configuration 勾、Alarm reception mode=Permanent IP connectivity、Process directory 勾。
    9. 同步：OXE 节点右键 Synchronization → 类型 Complete、目标 Separate → Apply；任务窗口 Status 页刷新看日志。
    10. 核验：OXE 下分支生成；Configuration/Data Collection 查 Date of last modification。
  verification: |
    同步完成且 OXE 下出现预期分支；日志 C:\8770\log\NMCSyncLdapPbx_1.log 无错（p191）。
  conditions: 实验拓扑单 OXE、无 spatial redundancy。
  tags: [lab, oxe-declaration, nmc, synchronization]

- id: c12
  title: 在 8770 中声明 OpenTouch 并互挂拓扑——bics.conf 取凭证 → OT 节点 → OXE 挂入 OT → 同步
  type: lab
  source_pages: p193-203
  source_chapter: OpenTouch server declaration (How-To)
  source_quote: |
    "ICE_USERNAME="otAdmin" ... ICE_TEMPLATEUSERNAME="otProfile" ... ICE_MAINTENANCEUSERNAME="otuser"" (p194)；
    "Subnetwork-Node number ... (Use 99 for example)." (p196)；
    "PRS Select "Presentation Service – opentouch"" (p201)
  steps: |
    1. 读凭证：OT 上 more /var/data/bics/bics.conf 抄 HOST_NAME=opentouch、HOST_DOMAIN=company.com、otAdmin/otProfile/otuser 与口令来源（实验口径 Admin-8770/maintenanceuser）。
    2. DNS 双检：OT 上 nslookup csm.company.com 与 oxe.company.com（应解析 192.168.1.3，实验口径）；缺则补 DNS 正反向。
    3. （如忘密）重置：otAdmin/otProfile 经 WBM System services/Security/Administrator 互改 GUI 口令；otuser 用 passwd otuser。
    4. 8770 侧核 DNS：nslookup opentouch.company.com 与 192.168.1.50 反解。
    5. 声明 OT：nmc/Logical-Network/ABC-Subnetwork 右键 Create → OpenTouch：Name=opentouch、Subnetwork-Node number=99、FQDN=opentouch.company.com、Username=otAdmin/Password、Enable notifications=True、Process configuration 勾、Process directory 勾；Connectivity 页 Username for profile management=otProfile；Maintenance 页 otuser/maintenanceuser。
    6. OT 侧建网络：OT 配置工具（8770 中右键 OT → Configure）→ System services/Topology/OXE CS/OXE CS network 右键 Create：Name=Logical-network、identifier=1。
    7. 建子网：OXE CS subnetwork 右键 Create：Name=ABC-subnetwork、identifier=1、Parent network=上一步网络。
    8. 建 OXE：OXE CS subnetwork 下 OXE CS 右键 Create：Display name=OXE、Node FQDN=oxe.company.com、Local main role FQDN=csm.company.com、Local main role IP=192.168.1.3、Port=2570、FTP adfexc/adfexc、Enable notification、HTTP Mode Default、Node Identifier=1、Parent subnetwork、PRS=Presentation Service – opentouch；CAC IP link 页 Codec=G729（与呼叫服务器一致）。
    9. 同步：nmc 中 OT 节点右键 Synchronization（Complete 或 Partial 等价）→ Separate。
  verification: |
    同步后 OXE 节点 101 出现在 OT 的 Topology 分支下（p203）；站点名可在 Users and devices > Site 配置。
  conditions: OT 必须与 OXE 同子网声明；实验口径 IP/FQDN。
  tags: [lab, ot-declaration, topology, bics-conf]

- id: c13
  title: OT 告警对接 8770——SNMP agent 核验、SNMP server 对象、8770 侧 V3 参数、MIB 重载、停服验证
  type: lab
  source_pages: p204-212
  source_chapter: Alarms - OpenTouch (How-To)
  source_quote: |
    "Create > SNMP server ... Notification type Inform" (p206-207)；
    "[root@opentouch ~]# service ompd stop ... start" (p207)；
    "Delete the ICE directory. Synchronize the OpenTouch server in order to retrieve the MIB." (p209)
  steps: |
    1. 核 SNMP agent（向导已建）：8770 Configuration 中右键 OT → Configure → System services > Security > SNMP agent：Engine ID（系统自动+节点名）、端口 161、用户 AdminSNMP、认证/加密口令 adminsnmp（实验口径，≥8 字符）。
    2. 建 SNMP server：OT 配置 → Eco system → 右键 IT server → Create → SNMP server：Display name（如 8770 SNMP）、FQDN=nms.company.com；Configuration 页：Port=162、Trap filter=NO_FILTER、SNMP version=v3、用户/口令同 agent、Notification type=Inform。
    3. 应用：SSH 到 OT，service ompd stop → service ompd start（重启 ams）。
    4. 8770 侧：选 OT 节点 → OT 页签 Alarm monitoring=True；Connectivity 页签：MIB path=alarm-mgnt/mib/ICEAlarmMgnt.mib、catalog=alarm-mgnt/catalog/ICEAlarmsCatalog.xml、SNMP V3 user=AdminSNMP、SNMP Port=161、认证 SHA、加密 AES 128、security level=V3 authentication: privacy（引擎 ID 自动）。
    5. MIB 重载：文件管理器到 C:\8770\data\config 删 ICE 目录 → 重新同步 OT → Service Manager 停 NMC Alarm server 服务 → Configuration 中 Connect 到 OT（otuser）→ su root → service ompd restart。
    6. 验证：Alarms 应用树出现 OT 图标；SSH 停 lama 服务（service lamad stop）→ 收到 minor 告警 → service lamad start → 告警自动恢复。
  verification: |
    停 lama 产生告警、启 lama 自动清除（p211）；OT 侧 ams.log 出现 Sending inform … to host
    nms.company.com on port 162（p212）。
  conditions: snmptrapd.conf 位于 c:\8770\data\config\netsnmp\（p209）。
  tags: [lab, alarms, snmp, mib]

- id: c14
  title: OXE SIP 配置——trunk group 10、本地网关/代理/注册器、外部网关 10/11、trusted、codec/DPNSS
  type: lab
  source_pages: p226-234
  source_chapter: OmniPCX Enterprise SIP configuration (How-To)
  source_quote: |
    "Trunk Group ID: 10 Trunk group name: SIP ... T2 Specification Select SIP" (p227)；
    "Gateway Number Enter the SIP external gateway number ("10" in our example) ... Port number 5260" (p231)；
    "Trusted address Enter the IP address of the OpenTouch server (e.g. 192.168.1.50)" (p233)
  steps: |
    1. [8770 中 OXE 配置应用；亦可用 mgr] 建 trunk group：Trunk Groups 右键 Create → ID=10、Type=T2、Name=SIP、Node number、Q931=ABC-F、Remote Network=空闲且≠OXE 网络号、T2 Specification=SIP。
    2. 本地参数：Trunk Groups/SIP → End-to-end dialing=No、DTMF end-to-end=No；Virtual accesses for SIP=2（默认）。
    3. SIP 本地网关：SIP/SIP Gateway：Subnetwork number=10、Trunk group=10、Proxy port=5060、Subscribe Min Duration=600、DNS local domain name=company.com、SIP DNS 1=192.168.1.254（实验口径）。
    4. SIP Proxy：认证=Digest、Only authenticated incoming calls=True；Registrar：Min expiry date=600。
    5. 外部网关 10（To_OT → OT SIP server）：SIP/External Gateways 右键 Create → Number=10、Name=To_OT、Remote domain=opentouch.company.com、Port=5260、Transport=TCP、Belonging domain 留空（本地冗余/无冗余）、Supervision timer=380、Trunk group=10、DNS=192.168.1.254、SDP in 18x=False、认证=None、Ignore inactive/black hole=勾、Contact with IP address=不勾、Outbound 100 REL=Supported / Incoming=Not requested、Gateway type=ICE type、Proxy identification on IP address=勾、Support CSTA User-to-User=Yes。
    6. 外部网关 11（TO_VM → Mule 语音邮件）：同上但 Number=11、Port=5040、Outbound calls only=True。
    7. Trusted addresses：SIP/Trusted IP Addresses 右键 Create → 填 OT IP（192.168.1.50，实验口径）。
    8. Codec：System/Other System Param./Compression Parameters → Compression type=G729、Multi. Algorithms=False。
    9. DPNSS 前缀与路由优化：Translator/Prefix plan 右键 Create（Number 空闲、Prefix Meaning=Local Features、Pabx address in DPNSS）；System 中 Routing Optimisation=Yes。
  verification: |
    书中为逐字段配置序列，行为验收由后续呼叫测试承接（external gateway ICE type 与 CSTA User-to-User
    为 OT 互通关键字段，p231）。
  conditions: 实验口径 trunk=10/GW=10,11；spatial redundancy 另有 TC1652。
  tags: [lab, sip, oxe, trunk, gateway]

- id: c15
  title: Prior management——号码段、前缀、语音邮件号、拨号规则、UDAS 同步、会议桥（TUI/DAS/格式规则）
  type: lab
  source_pages: p235-254
  source_chapter: Prior management (How-To)
  source_quote: |
    "/System services/ Topology/ OXE CS/ OXE CS Network / OXE CS Subnetwork/ OXE CS / <OXE name> ...
    "Ranges" tab ... Right click and "Add"" (p237)；
    "/System services/ Applications/ Telephony settings/ Vocal applications/ TUI application Select
    index whose meaning is "Voice Mail" for "OXE CS" population type ... Number 31200" (p241)；
    "Advanced settings/Edit DAS Rules ... s/^\+(\d{3,6})$/+x\1/" (p253)
  steps: |
    1. 号码段：OT 配置 → /System services/Topology/OXE CS/…/<OXE> → Ranges 页签右键 Add：min=31000、max=31499。
    2. 前缀：/System Services/Applications/Telephony/Telephone Prefixes：路由管理（立即前转）51、忙 52、无应答 53、忙或无应答 54、取消 41、话务台 9（法国默认，须核 OXE 现值）；未配话务台前缀的先配再 service wireald restart。
    3. 语音邮件类型：/System Services/Topology/VMS 核 defaultVmsLS Type=Local Storage。
    4. 语音邮件号：OT 侧 /System services/Applications/Telephony settings/Vocal applications/TUI application 选 "Voice Mail"（OXE CS 群体）=31200；OXE 侧 Applications/External Voice Mail 右键 Create：VM Dir No=31200、External Gateway=11（Mule 5040）、Subscription on registration=Yes。
    5. 拨号规则：/System services/Applications/Telephony settings/Dialing rule/dialingRule 1：General 页外呼前缀=0 或 9、Country；Conditions 页 Minimum length=拨号计划+1（实验 7）、Exception length。
    6. UDAS：/…/Search/Directory/InternalDir 与 phonebookDir：General 页 Activation 勾（phonebookDir 另选 Call Server）；Synchronization 页设日期/时间/周期（≥1，禁 0）或勾 Force synchronization。
    7. 会议号 OT 侧：/…/Vocal applications/TUI application：Conferencing 31250（英）核改；另建一条 31260（法）——新 TUI application（Type=Conferencing、语言、邮件邀请、Dial in number）。
    8. 会议号 OXE 侧：Applications/External Voice Mail 右键 Create：Voice Mail Dir. Number=31250（再建 31260）、External Gateway=10。
    9. 会议服务器管理：8770 中右键 OT → WBM（otAdmin）→ Users and devices/Conference server（允许弹窗）：System options（国际 00、国内 0、国码 33、Smart mail relay host=eco.company.com）；SIP Proxies 核默认出站代理（OT IP:5260）与用户 31700/31710。
    10. DAS rules：Advanced settings/Edit DAS Rules 选 Default 域，逐条录入法国十条（R1 s/^\+(\d{3,6})$/+x\1/ … R10 s/^\+/000/，顺序重要）。
    11. 格式规则：Advanced Settings/Phone Formatting Rules：Extension Pattern=/^\s*\+*[xX]?(\d{3,5})\s*$/（按 5 位计划）。
  verification: |
    书中以配置序列为主；行为验收=会议呼入 31250/31260 进桥、外呼前缀自动添加、目录检索命中（书内无独立
    测试问）。
  conditions: 实验口径号码/前缀/域名；DAS 与前缀按国家改写。
  tags: [lab, prior-management, ranges, prefixes, udas, conference, das]

- id: c16
  title: 用户档案创建——OXE 档案（BASIC/EXECUTIVE）+ OT 档案（Basic/Executive-Connection）
  type: lab
  source_pages: p272-278
  source_chapter: User profiles creation (How-To)
  source_quote: |
    "Select Use profile with auto. recognition ... This parameter allows creating a user from a
    profile." (p273)；
    "Profile Name must be in upper case" (p274)；
    "Category Select: ACU-OXE for Connection user having OT features" (p277)
  steps: |
    1. 开档案继承：8770 中 OXE 节点右键 Configure → System > Other System Param. > System Parameters → 勾 Use profile with auto. recognition。
    2. 建 OXE 档案 BASIC：Configuration 应用 → Users 文件夹右键 Create → General Characteristics：Directory number=A0000、Set Type=IP Touch 8068、Set Function=Profile；Profile 页 Profile Name=BASIC（大写）；（EXECUTIVE 同法：A0001、8068、Entity=1、Public network COS=2、Voice Mail Dir.No=31200；BASIC COS=1 无 VM）。
    3. 显示档案：Users 文件夹右键 Filter → "Where Set Function Equal Profile" 过滤查看。
    4. 8770 数据核验：OXE 档案经实时事件直达，无需同步。
    5. 建 OT 档案：OT 配置 /Users and devices/User/ → Profile 页右键 User → Create：Name=Basic-Connection（Executive-Connection 同法）。
    6. General 页：TUI/GUI 语言、Category=ACU-OXE、Time zone、Department=Default、Dialing rules=DialingRule1；Licenses 页勾 Desktop（Executive 另勾 Conferencing、Voice Mail）。
    7. 8770 数据更新：对 OT 服务器发起一次同步（Synchronization is required）。
    8. 核验：Configuration 与 Users 应用的 Profile 页可见全部档案；存量档案修改只能在 Users 应用，建/删回配置工具。
  verification: |
    Users/Configuration 两应用均可见 BASIC、EXECUTIVE、Basic-Connection、Executive-Connection 及 VM 档案
    （p278）。
  conditions: 实验档案命名与号 A0000/A0001 为实验口径。
  tags: [lab, profiles, oxe, ot]

- id: c17
  title: 用户创建——Directory 树、三类用户（Directory/无 OT/Connection）、存量加 OT、移树
  type: lab
  source_pages: p279-288
  source_chapter: Users creation (How-To)
  source_quote: |
    "Create the following tree in the Directory ... For the next questions, all users will be created
    in the "Training" department." (p280)；
    "Create a Connection user with OpenTouch rights: ... Login: adams GUI Password: 12345 TUI
    Password: 54321 ... OT user template: Executive-Connection" (p284, 实验口径)；
    "Move the modified OXE users to the following level: France\Brest\Training" (p288)
  steps: |
    1. 放宽口令策略（实验专用）：OT 配置 System services/Security/Password management：密码最小长度 5、允许 trivial GUI/TUI/SIP。
    2. 建目录树：Directory 应用在根（Ale）下建分支至 Training。
    3. 建 Directory User：Users 应用右键 Training → Create user → type=None：Carini/Claire；8770 password 可空。
    4. 建 OXE 用户（无 OT 权）：Create user → type=OXE：Alban/Alan、OXE ID=oxe、分机 31050、Device type=IPTouch 8068、OXE Profile=BASIC、Applications=None。
    5. 建 Connection user：Create user → type=OXE：称呼 Mrs、Adams/Alice、Email=adams@company.com、OXE ID=oxe、分机 31051、IP Touch 8068、OXE Profile=EXECUTIVE、Applications=OT、OT instance=OpenTouch、Login=adams、GUI=12345、TUI=54321、Site=Site1、OT user template=Executive-Connection、Voice mail server=defaultVmsLS、VM profile=Classic（实验口径）。
    6. 存量加 OT：Users 应用选 Barkley → 补 Email=barkley@company.com、Applications=OT、login=barkley、GUI=12345、TUI=54321、Site1、Basic-Connection；Backman 同法（backman，Executive-Connection，defaultVmsLS/Classic）。
    7. 核验三侧：Directory 有此人、OXE 有此分机、OT 有此用户（General/Contacts/Mailboxes）与 Voice Mail Box（档案）。
    8. 移树：把改过的用户移动到 France\Brest\Training。
  verification: |
    三侧（Directory/OXE/OT）均能查到 Adams 等用户且档案/邮箱正确挂接（p286 检查清单）。
  conditions: 口令 12345/54321 为实验口径；TUI 口令默认拒顺序数列（实验已放宽）。
  tags: [lab, users, creation, directory]

- id: c18
  title: Web Provisioning Client 批量建 Connection 用户——前置四查 + 三页签
  type: lab
  source_pages: p295-301
  source_chapter: Web Provisioning Client (How-To)
  source_quote: |
    "https://<OmniVista 8770 Server FQDN>/nmclient ... https://<OmniVista_8770_server>:8443/nmclient" (p294, p298)；
    "Login: adminnmc Password: Superuser01*" (p298, 实验口径)；
    "User Bruce Baldwin is created" (p301)
  steps: |
    1. 前置四查：OXE 档案在机（Configure → Users 过滤 SetFunction=Profile → Profile 页核对）；OXE 空闲号段（System > Free Numbers Ranges List）；OT 档案 Category=ACU OXE（OT Configure → Profile 页）；Users 应用 Profile 页档案齐全（OT 档案需完整同步）。
    2. Chrome 打开 https://nms.company.com（或 /nmclient、:8443/nmclient）→ NETWORK MANAGEMENT → adminnmc/Superuser01*（实验口径）。
    3. 左树选部门 Training → 点 +。
    4. Users 页签：User type=OXE、Salutation=Mr.（OT 用户强制）、Baldwin/Bruce、Email=baldwin@company.com（实验口径）。
    5. OXE Rights 页签：OXE name=oxe、Directory number 从空闲号段取、Station type=IPTouch 8068s、OXE profile=CONNECTION_T1、Key Profiles 可选、OT applications 启用。
    6. Application 页签：OT Name=OT、Login=baldwin、GUI password=baldwin、TUI password=12345、OT site=site1、OT user profile=Connection_P1、Voice Mail type=Local Storage、OT Voice Mail server=defaultVmsLS、OT Voice Mail profile=advanced（实验口径）。
    7. Devices 页签：核 Station type；（启用 Smartphone right 时：选移动类型、OT mobile device profile、分机号、GSM 号、Remote extension number、系统缩位号）。
    8. Save 保存。
  verification: |
    Bruce Baldwin 创建成功（p301）；用户出现在所选部门。
  conditions: WPC 限 Chrome ≥54、8770 3.2.8+；实验命名（CONNECTION_T1/Connection_P1）为实验口径。
  tags: [lab, wpc, provisioning]

- id: c19
  title: 语音邮箱配置——建箱挂人、Voice mail 许可、管理员/用户两侧定制
  type: lab
  source_pages: p326-337
  source_chapter: Voice mailbox configuration (How-To)
  source_quote: |
    "Users and devices / Voicemail box Right click and select "Create"" (p329)；
    "it's mandatory to assign a profile to the voice mailbox, in the « configuration » tab" (p330)；
    "Voice mail Enabled" (p332)
  steps: |
    1. 核默认系统：OT 配置 Services/Topology/VMS → defaultVmsLS，Type=Local Storage（默认已建）。
    2. 盘点：Users and devices/Voicemail box 看全部箱；Users 选全部用户看 Mailboxes 页签（实验口径：Barkley 无箱）。
    3. 建箱：Voicemail box 右键 Create → General 页 Display name=<username>VoiceMailBox、Type=Local Storage、系统=defaultVmsLS → Configuration 页 Voice mail profile=advanced（必选才能保存）。
    4. 挂人：Users 选 Barkley → Mailboxes 页签 → Voice mailbox 字段搜 "VMB" → 选中 → OK → Apply the changes。
    5. 许可：User 的 Licenses 页签勾 Voice mail=Enabled。
    6. 管理员定制：Voicemail box 的 Greetings 页签（问候类型、Extended absence-on、备选问候授权 ≤2）；Configuration 页签（Addressing by name、Automatic reading、Delete confirm、Fax、profile）。
    7. 问候上传：8770 中 OT 节点右键 WBM（otAdmin）→ Users and devices/Voice mail greetings management（二次认证）→ 选用户 → Upload/Activate/Download。
    8. 用户侧：My Profile（https://OT FQDN，GUI 登录）→ voicemail box 菜单改问候/answer only/按名寻址/自动读/删除确认；OTC PC 客户端亦可管。
    9. 行为测试：话机转接至语音邮件 → 留言 → TUI 听音并测试 answer only、按名寻址、自动阅读、删除确认、各问候类型。
  verification: |
    Barkley 有箱且许可开启；留言-收听-问候切换行为符合配置（p332 测试清单）。
  conditions: 邮箱字段受档案取值约束（Manageable by users 时用户可改）。
  tags: [lab, voice-mail, mailbox, greetings]

- id: c20
  title: 语音邮箱档案——核默认三档案、逐页签口径、新建 my_profile 并实测
  type: lab
  source_pages: p338-344
  source_chapter: Voice mailbox profiles (How-To)
  source_quote: |
    "/System services /Applications /Messaging / Voice Mail Profile" (p339)；
    "Create a voice mail profile ("local storage" type) called "my_profile"" (p343)；
    "Mailbox size: 10 Mb Max greeting: 5 seconds Max message recording: 15 seconds" (p343, 实验口径)
  steps: |
    1. 入口：OT 配置 /System services/Applications/Messaging/Voice Mail Profile；核默认档案（LS：Advanced/Classic/Simplified；UM：Standard）。
    2. 逐页签研读 Advanced：General（名称/类型）；Configuration 1（Answer only=Manageable by users 默认、Check quota、Announce time received、Skip memo、Direct callback、Callback voice prompt、Limited access、Extended absence 阻留言、Record invitation、Keep call in system、Callback sender allowed、留言后选项、录音提示音、Attendant call enabled）；Configuration 2（三时长 + TUI 口令管理三档）；Configuration 3（配额 MB、新旧留言保留天数、口令预警、网络化、IMAP）。
    3. 新建：右键 create → 类型 Local storage、名称 my_profile（实验口径）；参数：Check quota 启用、Announce received date/time、Direct callback、Limited access、Callback sender allowed、Brief prompts、留言后选项 true、10MB、问候 5 秒、留言 15 秒、现场录音 15 秒、新留言 15 天、已听 7 天。
    4. 分配验证：/Users and Devices/Voice Mail Box 选一邮箱，档案下拉应出现 my_profile；向该箱留几条消息验证参数生效。
  verification: |
    用 my_profile 的邮箱实测：问候 5 秒截断、配额/保留天数生效（p343 验证要求）。
  conditions: 配额仅在 Check quota 启用时生效。
  tags: [lab, voice-mail-profile]

- id: c21
  title: IMAP 收取语音邮件——Outlook 建 IMAP 账号、安全对齐、验证
  type: lab
  source_pages: p345-352
  source_chapter: Voice Messages retrieval through IMAP (How-To)
  source_quote: |
    "Account type Select "IMAP" Incoming mail server Enter the OpenTouch/OTMC server FQDN" (p348)；
    "service imap4fed restart" (p351)
  steps: |
    1. 控制面板 → User Accounts → Mail → E-mail Accounts → New。
    2. 选 Manual setup or additional server types → Next → POP or IMAP → Next。
    3. 账号：Your Name/Email（仅备注）、Account type=IMAP、Incoming mail server=opentouch.company.com（OT FQDN，实验口径）、Outgoing mail server=真实邮件服务器 FQDN（OT 不做 SMTP）、User name=GUI login（barkley）、Password=GUI 口令。
    4. More Settings：General 页起账号显示名；Advanced 页选与服务端一致的加密连接。
    5. Test Account Settings："log onto incoming mail server (IMAP)" 应 Completed；"send test e-mail" 失败属预期（无 SMTP 或误填 OT FQDN）。
    6. 服务端核对：OT 配置 System services/Topology/Physical servers/OT component/IMAP4 Front End：Connection security 与 IMAP port（默认 IMAPS+TLS 自动带端口）；改 SSL/无加密须改端口并 service imap4fed restart。
    7. Finish 完成；Outlook 第二账号收语音留言；账号名可改名。
  verification: |
    IMAP 登录测试 Completed；Outlook 第二账号列出 Local Storage 中的语音消息（p352）。
  conditions: 客户端与服务端安全类型必须匹配。
  tags: [lab, imap, outlook]

- id: c22
  title: SMTP/SMS 通知——全局参数、VPIM 路由、模板、用户设置、端到端测试
  type: lab
  source_pages: p369-378
  source_chapter: SMTP/SMS notifications (How-To)
  source_quote: |
    "System services/ Applications/ Notification/ Notification ... Occupancy ratio threshold (%): 80" (p370, 实验口径)；
    "System services/ Applications/ Messaging/ VPIM "Add" a new route ... FQDN or IP eco.company.com Port 25" (p371, 实验口径)；
    "service chameleond status ... service scorpiod status" (p378)
  steps: |
    1. 全局参数：/System services/Applications/Notification/Notification：发件名=OpenTouch、发件地址=administrator@company.com（须为 SMTP 真实账号）、SMS 网关地址=SMS$xxxxx$@company.com、附件上限 2MB（线性 PCM 8bits）、近满阈值 80%、音频格式选型（实验口径）。
    2. SMTP 路由：/System services/Applications/Messaging/VPIM → Add route：Domain=company.com、FQDN or IP=eco.company.com、Port=25（实验口径）。
    3. 模板（可选）：/var/data/panda/notification4 的 NotifTemplate_en_US.properties 改邮件/SMS 文案；升级不覆盖旧模板，要拿新模板须删旧并重启 chameleon。
    4. 用户前置：选一 LS 邮箱用户核邮箱、Email 地址、Voice mail 许可（Licenses 页）。
    5. 用户通知设置：Users → Notification 页签逐项配：Email right/激活/可自助开关、地址/可自助改、箱满通知、wav 附件、关 MWI、My Messaging 链接、SMS right/激活、通知手机。
    6. 端用户侧：My Profile → Notification：激活邮件/SMS 通知、改地址、选手机（受管理员授权约束）。
    7. 测试：向用户箱留言 → 验证邮件（含 wav/链接按配置）到达；配 SMS 网关则验证短信。
    8. 维护：service chameleond status、service scorpiod status；日志 /logs/chameleon/chameleon/panda.log、/logs/journal/chameleon.log、/logs/journal/scorpio.log。
  verification: |
    留言后通知邮件/短信按配置到达（p377 测试要求）；服务状态正常。
  conditions: 外部 SMTP 须无认证无 TLS；wav/箱满/链接仅 LS。
  tags: [lab, notification, smtp, sms]

- id: c23
  title: 通用公告——公告类型、用户授权、TUI 录制、wav 上传
  type: lab
  source_pages: p393-396
  source_chapter: General announcement (How-To)
  source_quote: |
    "/ System services/ Applications/ Telephony/ Vocal applications/ TUI global configuration Select
    one or several types of announcement" (p394)；
    "The user connects to his voicemail; the general announcement is available (Choice 6)" (p395)；
    "Suse console /var/ data/ ics-group/general_announcement ... Format: CCITT A-law 8bits 8kHz mono" (p396)
  steps: |
    1. 公告类型：OT 配置 /System services/Applications/Telephony/Vocal applications/TUI global configuration：勾选 "Is played for external callers / internal callers / calls in message consultation"（可多选；"arrive on AA" 已废弃勿用）。
    2. 授权：OT 配置 /Users and devices/User 选 Barkley → 勾 "User has right to manage the general announcement"。
    3. TUI 录制：该用户话机登录语音邮箱 → 增强主菜单 6（General Announcement）→ 菜单 2 录 "Welcome to OpenTouch training session"（实验口径）→ 录完自动激活；1 听、3 停用。
    4. wav 方式：向讲师取合格 wav（CCITT A-law 8bits 8kHz mono）→ 传到 OT 系统 /var/data/ics-group/general_announcement 目录 → 改名 general_announcement.wav → 即启用；停用=删文件或 TUI 菜单 3。
  verification: |
    留言/查听时能听到公告（按所选播放时机）；TUI 菜单 6 出现在授权用户的增强菜单（p387/395）。
  conditions: 一次仅一条、覆盖式、5 分钟上限。
  tags: [lab, general-announcement, tui, wav]

- id: c24
  title: Windows CA 外部证书——导入根 CA、生成 CSR、CA 签发、导入并部署
  type: lab
  source_pages: p412-423
  source_chapter: External certificate generation and deployment with Windows CA (How-To)
  source_quote: |
    "System services/Security/Certificate "Server CTL" tab Click on "Add"" (p414)；
    "Click on "Generate CSR" ... Signature algorithm Select the algorithm (SHA256 is the best for
    security)" (p417)；
    "Select the certificate and Click on "Deploy"" (p423)
  steps: |
    1. 取根 CA：浏览器开 https://eco.company.com/CertSrv（或 ca.company.com/CertSrv；R-Lab 亦可从 NAS 取，问讲师）。
    2. 导入根 CA 到 OT：WebAdmin（https://<OT FQDN>/WebAdmin，otAdmin）→ System services/Security/Certificate → "Server CTL" 页 → Add → Select CTL server file → Import。
    3. 客户端信任：核 PC 客户端证书存储已有根 CA，没有则打开证书 → Install Certificate。
    4. 生成 CSR（可选步骤）：Certificate 页 → Generate CSR：Country（2 位）/State/City/Company/Org unit/管理员邮箱/Signature algorithm=SHA256 → Create（存 Downloads）。
    5. CA 签发：CertSrv → Request a certificate → advanced certificate request → base64 提交 → 粘贴 CSR 文本 → Template=Web Server → 提交 → Base 64 encoded → Download certificate chain。
    6. 导入：Certificate 页 → 点当前证书 → Change server certificate → 类型选 pkcs#7 → Select certificate file → Import（若 pkcs#12 且 CSR 在 CA 生成，需输 passphrase）。
    7. 部署：选中证书 → Deploy；WebAdmin 会话断开并提示 "Impossible to retrieve data…" 属正常（服务器证书已换），重开会话即可。
  verification: |
    新证书生效：浏览器重开 WebAdmin/OTC 连接显示 CA 签发证书（p423 Notes 说明会话断开为正常现象）。
  conditions: 实验用 Windows CA；现场亦可用 OpenSSL/公共 CA。
  tags: [lab, certificates, windows-ca, pki]

- id: c25
  title: 自签证书——查通用证书、切 Internal+SHA256、补信息、部署（含重签 CTL 提醒）
  type: lab
  source_pages: p424-429
  source_chapter: OpenTouch self-signed certificate (How-To)
  source_quote: |
    "If during the post-installation wizard, you have selected "OpenTouch certificates security levels
    = off", check in "WebAdmin" interface, that you are currently using a certificate whose type is
    "external" and available for all machines (display name =*)" (p425)；
    "Type Select the certificate type: Internal -> autogenerated Signature algorithm Select the
    algorithm: SHA-2 (SHA256)" (p427)；
    "Don't forget to sign the new CTL, by using a 808x device (procedure with USB key)." (p427)
  steps: |
    1. 查通用证书：WebAdmin（otAdmin）→ System services/Security/Certificate → Certificate 页：若装机构选了 security off，当前证书 Display Name=*、类型 external（ALE CA 签发）、SHA1 或 SHA256。
    2. 换自签：选当前证书 → Change server certificate → Type=Internal（autogenerated）、Signature algorithm=SHA-2 (SHA256) → 弹 CTL 须重签的警告 → Yes。
    3. 补信息（可选）：View → Local PKI 页：Country/State/City/Company/Org unit/管理员邮箱/有效期（默认 7300 天）。
    4. 重签 CTL：按专用流程用 808x 话机 + USB key 重签 CTL。
    5. 部署：选中证书 → Deploy；会话断开属正常，重开。
  verification: |
    新自签证书生效（浏览器 https 连接显示 Internal 证书与新信息，p429）。
  conditions: 通用证书全球同款、不安全；SHA-1 自 R2.2 弃用。
  tags: [lab, certificates, self-signed, ctl]

- id: c26
  title: OTC PC 客户端——安装、Desktop 许可、客户端功能测试、软电话模式、OTC PC One 对照
  type: lab
  source_pages: p460-483
  source_chapter: OTC PC (How-To)
  source_quote: |
    "https:// OT server FQDN/opentouch_conversation_update/OpenTouchConversation.msi" (p462)；
    "Device identity Enter the device identity as follows: <directory number>@<OpenTouch™ server
    FQDN> 31009@opentouch.company.com" (p473)；
    "Verify that the application is working as OTC PC One." (p475)
  steps: |
    1. 安装：浏览器开 https://<OT FQDN>/opentouch_conversation_update/OpenTouchConversation.msi 下载并 Run（前置 .NET 4.5、VS C++ 2010 Tools for Office）→ Next → 接受协议 → 选目录 → 部署类型 Standard（自动带 Outlook 扩展；Advanced 需自选协作系统）→ 填内部 FQDN=opentouch.company.com 与远程 FQDN=ot.company.com → 选快捷方式 → Install → Finish（自动附装 VC++ 2013）。
    2. 授 Desktop 许可：8770 Users and devices/User 选 Barkley（与 Betty Boop）→ OT 页签 → Licenses 页签勾 Desktop；Collaboration 页核实 Enable collaboration/sharing 已勾。
    3. 登录：启动 OTC PC → Server=内部 FQDN、用户名、GUI 口令 → Connect；首次询问 IM 默认应用答 Yes；私网 FQDN 不可达时自动转公网 FQDN 弹远程认证窗。
    4. 功能测试：头像/在场/设置与配色；收藏（目录搜索点星标：Alan Alban、Betty Boop）；可编程键（Home=00201031002，实验口径）；呼出三法（键盘/按名/联系人）、接听、挂断、转接；IM 与共享（文档/桌面，双 Windows 会话对测）；呼叫历史核对六类记录并删条目。
    5. 隐私：OT 配置 System services/Applications/Collaboration/Collaboration configuration → DEFAULT 域 → IM & Presence federation 页勾 Enable privacy；Boop 登录把 Barkley 移入 blocked，Barkley 侧验证看不到状态。
    6. 软电话模式：建 Connection user（Black/Barry、31009、Device type=SIP Extension、SIP 口令 98765、Applications=OT、login=black、GUI/TUI=12345、OT SIP 口令留空自动生成、Site1、任一 OT 档案）；用户右键 associate SIP device → New → OTC PC，Device identity=31009@opentouch.company.com；OT configuration → Device 页 SIP extension type=Softphone；确认 Desktop 许可已勾、Nomadic SIP 不勾；查 SIP 配置文件 /var/data/oamp/cms/DevicesDeployment/MYICPCSIP/<号>@<FQDN>；Black 登录打/接电话验证。
    7. OTC PC One 对照：核 Backman 的 Desktop 不勾（Conference 勾）→ Backman 登录 → 应用应以 One 模式工作；测试：呼出可用、来话不能接只能挂、不能转接、IM 可用、共享只能 viewer。
    8. Outlook 扩展：Barkley Windows 会话开 OTC PC（默认 IM）与 Outlook（barkley@company.com）→ 从邮件右键/工具栏发 IM 与呼叫；建联系人（全名/电话/邮箱/IM 地址）后从联系人卡呼叫/IM（多号码时 Call 按钮出下拉）。
    9. 维护：tsa_maintenance（/opt/Alcatel-Lucent/infra_services/ots/）→ 47 dump 全部号码核 ots 库；不同步则 100 → 106 2998 → 7 Load All Acapi Object；日志 logs/ots；客户端 Settings → Support → Activate logging → Save logs；Outlook Options → Add-In Options → Go 启/停加载项。
  verification: |
    RCC/软电话/One 三形态行为与许可一致（p475 各测试问）；ots 库 47 dump 可见全部用户（p480）。
  conditions: 实验账号/号码为实验口径；软电话用户禁 Nomadic SIP 权。
  tags: [lab, otc-pc, softphone, outlook, licensing]

- id: c27
  title: 多终端 Multi-devices——COS 与前缀前置、副站 NOE、副站 OTC PC（软电话第二设备）
  type: lab
  source_pages: p484-493
  source_chapter: Multi-devices for Connection users (How-To)
  source_quote: |
    "Classes of Service/Phone feature COS/<COS ID> ... Ring all Secondary if Main Out of Service Yes" (p485)；
    "Translator/Prefix Plan ... Local features Twinset Get Call ... Station features No ringing" (p486)；
    "Nomadic SIP Not checked Desktop Checked" (p492)
  steps: |
    1. COS：8770 OXE 配置 → Classes of Service/Phone feature COS/<用户 COS> → Ring all Secondary if Main Out of Service=Yes。
    2. 前缀：Translator/Prefix Plan 建两条——506=Local features/Twinset Get Call、507=Set features/Station features/No ringing（实验口径）；在用户 Phone Features COS 授权两特性。
    3. [用例 1：副站为 NOE 话机] Users 应用选 Barkley（主站 31000）→ 右键 Add a secondary set → Add：OXE directory number=2131000、Device type=8068（实验口径）；确认 Desktop 权已授；可给主/副站配可编程键绑 Twinset Get Call/No ringing。
    4. 核验：OXE 侧用户档案 Tandem Directory Number=2131000、Attached MultiDevice；OT 侧 User 的 Device 页出现副设备。
    5. 测试：Barkley 登录——切换呼出设备、用前缀/OTC PC 静音主站振铃、建 Office1/Office2 两路由档案分别用两台话机外呼。
    6. [用例 2：副站为 OTC PC] 先核 DM：OT 配置 /Eco system/IT server 右键 Create → Device management server：Name、FQDN=nms.company.com、Port=8080（实验口径）。
    7. Users 选 Boop（主站 31002）→ Add a secondary set：2131002、Device type=SIP extension、SIP 口令 ≥5 位（实验口径）。
    8. 关联：选该设备右键 Associate SIP device → New → OTC PC：SIP URI=2131002@opentouch.company.com。
    9. 许可：User 的 Licenses 页 Nomadic SIP 不勾、Desktop 勾。
    10. 核验与测试：Tandem DN=2131002；OT 侧 Device 页 Devices 与 Softphone Directory Numbers 均出 2131002；Boop 登录建 "Homeworking" 路由档案（OTC PC VoIP 外呼+主站静音）。
  verification: |
    两用例的 Tandem/Attached/Softphone Directory Numbers 自动生成正确（p488/p493）；设备切换与静音行为
    符合预期。
  conditions: 软电话第二设备禁 Nomadic SIP；多终端上限 5 设备（REX/DECT 各 1）。
  tags: [lab, multi-devices, twinset, softphone]

- id: c28
  title: 监督组——建组派角色、进出组前缀（OT+OXE 两侧）、Direct call pick-up 前缀、代接测试
  type: lab
  source_pages: p508-513
  source_chapter: Supervision groups (How-To)
  source_quote: |
    "Create a supervision group named "Connection_SG" working in regular mode." (p509)；
    "System services/Applications/Telephony settings/Telephone prefixes/Telephone prefixes ... Join or
    leave group Enter the value for the prefix" (p511)；
    "/Categories/Phone Facilities Categories ... General services / Direct call pick-up 1 (enabled)" (p513)
  steps: |
    1. 建组：8770 Configuration → OT 节点右键 Configure → Features 页 User groups → Supervision group → Create：Name=Connection_SG、Mode=regular（实验口径）。
    2. 派角色：组内右键 Add 逐个加：Barkley=Is Supervisor、Boop=Is Supervised、Backman=双职（实验口径；每组 ≤40 人、一人一组）。
    3. 进出组前缀 OT 侧：/System services/Applications/Telephony settings/Telephone prefixes → Join or leave group 填值（实验例 44）。
    4. 进出组前缀 OXE 侧：Applications/External Voice Mail 右键 Create：Voice Mail Dir. No.=同值 44、Directory Name、External Gateway Number=ICM 网关（例 1）。
    5. 代接前缀：OXE Translator/Prefix plan → Create：Number、Prefix meaning=General Features、General features=Direct call pick-up；Categories/Phone Facilities Categories 选用户类目 → General services/Direct call pick-up=1 启用。
    6. 测试：Boop 话机来话 → 监督员（Barkley/Backman）OTC PC 收通知并可代接；监督窗口可开/缩、进出组经 OTC PC/前缀。
  verification: |
    来话时监督员收到通知并代接成功（p513 测试描述）；OTC PC 监督窗口显示组员状态。
  conditions: Direct call pick-up 前缀仅 Connection 用户组需要；监督功能无专用许可。
  tags: [lab, supervision-group, pickup, prefixes]

- id: c29
  title: 维护工具三通道——checkdns 与 dla.sh 各走三种入口
  type: lab
  source_pages: p522-532
  source_chapter: Maintenance tools (How-To)
  source_quote: |
    "[root@opentouch otuser]# checkdns Using external DNS1: 151.1.1.100" (p524)；
    "Your choice [1..5, Q]:2 ... Your choice [1..10, Q]: 7" (p525)；
    "Select the feature for which one you want to collect logs. E.g. "Presence"" (p532)
  steps: |
    1. 列工具：listtool.sh 按 Maintenance/Troubleshooting/Information/Log/Misc 五类列出全部脚本。
    2. DNS 核查（通道一）：ot-config.sh 看用法 → 直接跑 checkdns（核 HOST/FLEXLM_SERVER/HA_ACS_SERVICE 的正反向与可达）。
    3. DNS 核查（通道二）：otconsole.sh → 1 Easy Administration → 2 Troubleshooting → 7 DNS Verification（等价于 checkdns）。
    4. DNS 核查（通道三）：WebAdmin → Monitoring → Maintenance Portal → Troubleshooting → All Verification → DNS verification → Launch（normal/expert 两种显示模式均可找到）。
    5. 日志收集（通道一）：dla.sh → 选 Collect logs → feature（例 Presence）→ 子特性/场景（例 All）→ 文件名（默认日期时间）→ 描述 → 产物在 /logs/dla。
    6. 日志收集（通道二）：otconsole.sh → 1 → 5 Log Management → 1 Dynamic Logs Activation（须 root）→ 同上流程。
    7. 日志收集（通道三）：Maintenance Portal → Log → Dynamic Logs Activation → 选 feature → Collect Logs → 完成后按橙色箭头直接下载 zip。
  verification: |
    checkdns 输出各解析项 [OK]（p524）；dla 产物 zip 落 /logs/dla 且可从 Portal 下载（p530/p532）。
  conditions: dla 菜单选项 1 须 root；示例 DNS 151.1.1.100 为书内演示环境值（实验口径）。
  tags: [lab, maintenance, otconsole, portal, logs]

- id: c30
  title: OT 备份恢复与 rehosting——--storage 定位、otbr.sh、ot-config.sh --rehost、TC2149 收尾
  type: lab
  source_pages: p551-557, p568-578
  source_chapter: OpenTouch backup & restore (How-To) / OTMS rehosting (How-To)
  source_quote: |
    "Configure the backup on NFS server with following settings: NFS server: 10.20.30.40 /mnt/db/
    backup/podX" (p552, 实验口径)；
    "otbr.sh backup host ... otbr.sh restore host" (p557)；
    "enter the command: "ot-config.sh --rehost"" (p569)；
    "After around 25 minutes (with the lab configuration), rehosting is completed" (p572)
  steps: |
    [备份准备与执行]
    1. 定位备份地：ot-config.sh --storage → backupStatus 看现状 → backupConfigure 交互向导：物理机选 Local/USB/NFS（实验选 NFS 10.20.30.40:/mnt/db/backup/podX；USB 须 FAT32/NTFS/EXT3，prepareUsbdisk -f 格式化）；OT-V：/var/backup 整体挂 NFS（LOCAL 选 bics 留在挂载目录；NFS 选 bics 单独挂 /mnt/db/backup/podX/result）；USB 对虚拟化无意义。
    2. 备份：root 跑 otbr.sh backup host（或 moh；OTMS 中 appliall=host）；帮助 otbr.sh --help [backup|restore]。
    3. 恢复：otbr.sh restore host（恢复需先停服务口径见讲义：restore requires system services to be stopped）。
    [rehosting 实验]
    4. 前置：DNS 已录入新值——nslookup otms.company.com 应得 192.168.1.49（实验口径：主机名 opentouch→otms、IP .50→.49）；确认有可用备份。
    5. 执行：root 跑 ot-config.sh --rehost → 警告确认 → 向导 Next → Host Network Parameters 改 Hostname=otms、IP=192.168.1.49 → Next → Summary → Finish；约 25 分钟完成。
    6. TC2149 收尾（本实验改动=OTMS IP+主机名）：OXE——SIP/Trusted IP Addresses 加新 IP、两条外部网关重建（Remote domain=新 FQDN）、核 /etc/ntp.conf；OTMS——证书/反向代理/SBC/OTES/ACS 会议地址/移动设备/OT 软电话核改；8770——OT 节点 FQDN 改新值；生态——DNS/DHCP 更新、SSO/SNMP/防火墙核查。
  verification: |
    otbr.sh 备份产物生成（/var/backup/bics）；rehost 完成后以新 FQDN/IP 可达、checkAll.sh 通过（p572/
    TC2149 第 4 章：bics-rehosting.log 与系统检查命令族）。
  conditions: rehost 配错即死锁无回退——动手前必须有可用备份；OXE/8770/OMS 不被 --rehost 触达。
  tags: [lab, backup, otbr, rehosting, tc2149]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 18 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 POD 搭建 | 有 → c01 |
| task-02 SOT 部署 OTMS | 有 → c02 |
| task-03 OVF 导入 | 有 → c03 |
| task-04 Post-installation wizard（全新） | 有 → c04 |
| task-04b/恢复路径 | 有 → c05（书内同一章的第 2 节，单列成条便于复用） |
| task-05 系统连接与 SUSE | 有 → c06、c07 |
| task-06 许可安装 | 并入 c04 步骤 8（向导内装）与 c09 步骤 5（外部 FlexLM 手动装）；独立“手动装许可”操作书内无单独 How-To 章 |
| task-07 许可核查 | 有 → c08 |
| task-08 外部 FlexLM 与切换 | 有 → c09、c10 |
| task-09 声明 OXE | 有 → c11 |
| task-10 声明 OT | 有 → c12 |
| task-11 OXE SIP | 有 → c14 |
| task-12 prior management | 有 → c15 |
| task-13 告警对接 | 有 → c13 |
| task-14 档案与用户 | 有 → c16、c17、c18 |
| task-15 语音邮箱体系 | 有 → c19、c20、c21、c22、c23 |
| task-16 证书 | 有 → c24（外部 CA）、c25（自签） |
| task-17 客户端交付 | 有 → c26（OTC PC）、c27（多终端）、c28（监督组） |
| task-18 运维 | 有 → c29（维护）、c30（备份+rehosting） |

**统计**：30 条（全部为书内 How-To 章，一一对应，无合并遗漏）；18 项任务全部有案例类条目覆盖，其中 task-06 许可安装的操作内容分散在 c04/c09（书内无独立 How-To 章，已在对应步骤中保留）。
