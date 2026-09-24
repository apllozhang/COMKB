# 框架/流程/结构候选 — OmniSwitch LAN Access Switching (DT00XTE215EN Ed23)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：课程推进逻辑、机制结构图、配置步骤、操作路径、平台/界面分区。实验环境给定值（IP/账号/POD 规则）一律标注"实验口径"。

```yaml
- id: f01
  title: 三日课程推进主线——管理接入 → 配置生命周期 → 堆叠 → 二层 → 三层 → 策略 → 运维
  type: flow
  source_pages: p6-8, p12-11(议程), p580
  source_chapter: Topics / Course agenda (Day 1-3)
  source_quote: |
    "Day 1 • Course introduction ... • OmniSwitch Portfolio ... • AOS OmniSwitch Management ... • Managing Files/Directories ... • Virtual Chassis ... • VLANs Management" (p6)
    "Day 2 • Omnivista Smart Tool ... • Link Aggregation Groups ... • Spanning Tree Protocol (STP) ... • Dual Home Link (DHL) ... • IP interfaces ... • VRRP" (p7)
    "Day 3 • Quality of Service ... • Flow Based Filtering (ACL) ... • Security Network Access Guardian ... • LLDP ... • Power over Ethernet (PoE)" (p8)
  summary: |
    课程按三日推进：Day1 课程介绍与 R-Lab 接入、产品组合、交换机管理（登录/闪电配置/文件目录）、Virtual Chassis、VLAN；Day2 OST、诊断工具、链路聚合、STP、DHL、IP 接口（DHCP/静态路由）、VRRP；Day3 QoS、ACL、Access Guardian、LLDP、PoE。讲义议程之外还有附加模块：Console 连接（p522-528）、软件镜像升级（p529-535）、Intelligent Fabric/Auto-Fabric（p536-554）、Fleet Supervision（p555-569）、OST 2.0 安装指南（p572-580）。这是整本书的"先接入后组网、先二层后三层、先底座后策略"教学主线，也是实际交付项目的推荐学习顺序。
  conditions: 无特殊版本前提；附加模块不在三日议程内，属培训材料附送内容
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: R-Lab 远程实验平台结构——POD 拓扑 + RustConn/Proxmox 双入口
  type: structure
  source_pages: p12-24
  source_chapter: REMOTE LAB CONNECTION / Connect to the Remote Lab
  source_quote: |
    "https://rdp.al-mydemo.com/ - Username: LanpodXa or LanpodXb (X = R-Lab Number [1-32]) - Password: unique per session – Provided by the Instructor" (p14)
    "RustConn : access to the Switches & Access Points consoles. Linux clients 1 to 10 and Wireless Client. Proxmox : access to the linux clients 1 to 10 for starting and stopping only" (p19)
    "DHCP Server, Radius Server: 192.168.100.102 • Web Server: 192.168.100.102 • FTP Server: 192.168.100.102 • Firewall/NAT server • Podxx-pfSense : 192.168.100.108" (p23)
  summary: |
    实验平台结构：Web 浏览器登录 rdp.al-mydemo.com（账号 LanpodXa/Xb，X=1-32，密码每会话唯一由讲师发，实验口径）；RustConn 提供交换机/AP 控制台（双击自动登录）与 Linux/无线客户端桌面；Proxmox 仅用于开停 Client 1-10 虚机。每 POD 含 7 台交换机（6900-A/6870-A/6870-B/6860-B/6560-A/6360-A/6360-B，EMP 地址 10.4.Pod#.1/.7/.2/.8/.3/.5/.6）+ 10 个 Linux 客户端 + 无线客户端；公共服务器 192.168.100.102（DHCP/RADIUS/Web/FTP）、pfSense 192.168.100.108、DNS 10.0.0.51。交换机统一凭据 admin/Superuser=1。
  conditions: 全部为实验口径；POD 号替换规则见 p16（如 SSID EmployeesX 中 X=POD 号）
  tags: [structure, lab, rlab, topology]

- id: f03
  title: Linux/无线客户端操作序列与多交换机广播功能
  type: menu-path
  source_pages: p25-51
  source_chapter: HOW TO USE A LINUX CLIENT / HOW TO USE THE WIRELESS CLIENT / RUSTCONN ADVANCED FEATURE
  source_quote: |
    "SET THE IP ADDRESS OF A CLIENT 1. Double click on network configuration icon ... 4. Method, select in the list: Manual" (p26)
    "USE 802.1X AUTHENTICATION ... 5. Authentication, select in the list: Protected EAP (PEAP) ... 7. Enter the username and password" (p28)
    "Warning: NEVER Disconnect the Ethernet Network > you will lose access to the Wireless Client" (p43)
    "Click it to enable broadcast mode. ... The command is automatically replicated and executed on all the OmniSwitches session displayed in the current tab." (p49-50)
  summary: |
    客户端操作四组：①Linux 客户端——设 IP（图形界面 Manual/DHCP）、802.1X 启停（PEAP+免 CA 证书）、断连重连刷新配置（ip a 验证）、连通性检查命令族（ip a/nmcli device status/ip link show ens18/ip route/ping）；②SSH 到交换机：ssh admin-netadv@10.4.X.Y，口令 Superuser01!（实验口径）；③无线客户端——连/断 SSID、802.1X 连接、ifconfig 验证 wlan0；④RustConn 广播——Split 窗口 + Select Tab + Broadcast 按钮，一条 CLI 同时下发多台交换机。
  conditions: 实验口径；客户端接口名为 ens18；无线客户端断 Ethernet 即失联
  tags: [menu-path, lab, client-operations, broadcast]

- id: f04
  title: OmniSwitch 产品线分层结构（Edge/Aggregation/Core + Hardened）与文档体系
  type: structure
  source_pages: p9, p53-56
  source_chapter: AOS –Technical Documentations / NETWORK PORTFOLIO / OMNISWITCH LAN FAMILY
  source_quote: |
    "OmniSwitch 9907/9912 Modular Chassis AOS Advanced L3 10/40/100 GE ... OmniSwitch 6900 / 6920 AOS Advanced L2-L3 Aggregation/Core DC TOR ... OmniSwitch 6360 AOS L2+ Basic L3 GE" (p54)
    "OmniSwitch 6560/E AOS Advanced L3 licensed 1GE/2.5G/5G 10G uplinks ... OmniSwitch 6370 AOS L2+ Basic L3+ MG New!" (p54-55)
  summary: |
    产品分层：Core——OS9900（模块化机箱）与 OS6900/6920（DC TOR，VRF/SPB/VXLAN/ISSU）；Aggregation——OS6870（新，MPLS/SPB/VXLAN，200G VFL）与 OS6860N；Edge——OS6560/E（MultiGig L3 licensed）、OS6360（L2+ Basic L3）、OS6370（新，MG）、OS2260/2360（WebSmart L2）、OS6570M（Metro）、OS6465（L2+）、OS6865/6575（Hardened/工业）。文档体系五件：Hardware Users Guide、Switch Management Guide、Network Configuration Guide、Advanced Routing Configuration Guide、CLI Reference Guide（+ Transceivers Guide，p9）。技能定位：本教材覆盖 Management/Network Configuration 两册的主干实验。
  conditions: 产品矩阵以 datasheet 为准（p56 给出全部链接）；型号能力随 AOS 版本演进
  tags: [structure, portfolio, positioning]

- id: f05
  title: AAA 认证框架——服务类型 × 认证链 × fail-through 语义
  type: diagram
  source_pages: p67-69
  source_chapter: CONNECTING TO THE SWITCH / Overview & Declaring multiple servers with fail-through
  source_quote: |
    "Service type = Default 1st authentication server = local Authentication exit-on-fail: Enabled ... Service type = Http Authentication = denied" (p67)
    "-> aaa authentication {console | telnet | ftp | http | snmp | ssh | default} server1 [server2...] [local] [exit-on-fail {enable | disable}]" (p69)
    "exit-on-fail Configures if the switch must authenticate using all servers in the list or only the first available server." (p69)
  summary: |
    AAA 框架三要素：①服务类型七种（default/console/telnet/ftp/http/snmp/ssh），各自一条认证链，出厂态全部指向 local 数据库且 exit-on-fail Enabled，唯 http 在概览图示例标 denied；②命令 aaa authentication <service> server1 [server2...] [local] 声明认证链，可挂多服务器实现 fail-through；③exit-on-fail 语义：enabled=只用列表中第一个可用服务器，disabled=逐个查完所有服务器。ASA（Authenticated Switch Access）是这套机制的统称，覆盖 Telnet/FTP/SNMP/SSH/HTTP/console/modem（p95）。
  conditions: 允许/拒绝某服务用 no aaa authentication http 类命令（p68）
  tags: [diagram, aaa, authentication, framework]

- id: f06
  title: 用户数据库与外部服务器结构——userTable/64 用户/密码策略/命令日志
  type: structure
  source_pages: p70-74
  source_chapter: SWITCH USER ACCOUNT / USER CREATION / EXTERNAL SERVER DECLARATION / SECURITY
  source_quote: |
    "The Local userDB file is named userTable* Path: flash/system directory By default : 2 users 'admin and default' ... * Up to 64 users can be configured in the local switch database" (p70)
    "-> user newuser password P@ssW0rd123# read-write all sha+des ... -> user password-policy cannot-contain-username cannot-contain-consecutive-characters min-uppercase min-lowercase min-digit min-nonalpha" (p72)
    "IEC62443-3-3 Level 2 Ready in 8.10R3" (p74)
  summary: |
    账号体系结构：本地用户库存于 flash/system 的 userTable 文件，出厂两用户（admin/default），上限 64；权限=read/write 对命令域和命令族的可访问性。密码治理四层：①创建用户明文或 password-prompt 交互式（sha+des 混合加密）；②password-policy 规则（禁含用户名/禁连续字符/大小写数字非字母最少个数）；③password-size min/expiration/history/min-age 生命周期；④password-refresh 强制下次登录改密（IEC62443-3-3 Level 2 Ready in 8.10R3）。外部服务器：aaa radius-server <name> host ... key ...（建议 TLS），aaa accounting session 记账，command-log enable 命令审计。证书增强：convert-cert（DER/PEM/PKCS#12/P7B→PEM）与 check-revocation（CRL/OCSP，限 RADIUS/Syslog over TLS）。
  conditions: 版本线：8.10R3 警告改默认密码、8.10R04 强制首登改密（p70-71）
  tags: [structure, aaa, users, password-policy, security]

- id: f07
  title: 管理面接入方式全景——console/EMP/WebView/SNMP/会话数表
  type: structure
  source_pages: p75-87
  source_chapter: ACCESS VIA THE CONSOLE PORT / EMP PORT / WEBVIEW / SNMP / Restrict management access
  source_quote: |
    "Default settings Speed (baud) : 115200 Parity: None Stop bits : 1 Flow control : none Note: the configuration for the latest generation 6900, 6870 and 6860N switches is different" (p76)
    "In case you disable console access, and you lose all other means of management access (SSH, HTTPS, SNMP …), you won't be able to manage anymore your switch ! (RMA necessary in this case)" (p77)
    "Telnet (V4 or V6) 6 ... FTP (V4 or V6) 4 ... SSH + SFTP (V4 or V6 secure session) 8 ... HTTP 4 ... Total sessions (Secure Shell, Telnet, FTP, HTTP, and console) 20 ... SNMP 50" (p80)
  summary: |
    接入全景五通道：①console——RJ45/USB-RS232/Micro-USB 三种物理口，默认 9600（新一代 6900/6870/6860N 为 115200），可限 admin-only 或整体禁用（禁用有 RMA 风险）；②EMP——旁路 NI 直连 CMM，无 EMP 口机型用 USB-Ethernet dongle 等效（USB 3.0 仅 6360/6465/6560），可施加 empacl 策略（仅 IPv4 源/目的 PBR，单策略列表）；③WebView——内嵌 Web 服务，R8 默认强制 SSL（80/443）；④SSH/Telnet/FTP——会话并发上限 SSH 8、Telnet 6、FTP 4、HTTP 4、总数 20、SNMP 50；⑤SNMP v1/v2/v3 供 OmniVista 等网管。管理面收缩：ASA 限源（≤64 地址）、ip service 禁用不安全端口、session login-attempt/login-timeout/session-limit、SSH strong-ciphers/strong-hmacs/enforce-pubkey-auth、session banner、MFA（外置 Application Note）。
  conditions: USB dongle 需 8.9.R1+；VC 全部成员都要插 dongle 才有完整 VC EMP（p78）
  tags: [structure, management-access, console, emp, webview, sessions]

- id: f08
  title: WebView 七大配置组与操作动线
  type: structure
  source_pages: p97-101
  source_chapter: Remote Switch Access (How-To) / Accessing to the WebView
  source_quote: |
    "The switch configuration is divided into seven main configuration groups ­ Physical, ­ Layer 2, ­ Networking ­ Service management, ­ Security ­ Quality of service ­ Device management." (p98)
    "From the horizontal menu bar at the top of the page, select Security > ASA, then click Session and then Configuration." (p98)
  summary: |
    WebView 分区：Physical / Layer 2 / Networking / Service management / Security / Quality of service / Device management 七组。常用动线：改会话参数走 Security > ASA > Session > Configuration；机框可视化走 Physical > Chassis management > Chassis visualization（悬停端口看信息、点击进端口配置）；VLAN 增删走 Layer 2 > VLAN（+ 新建，VLAN Mgmt 垃圾桶删除）；写内存用顶部图标栏第三个图标（write memory）。登录 https://<交换机 EMP IP>，R8 强制 SSL。
  conditions: WebView 默认 enabled 但不允许认证，需 aaa authentication http；视图限单台交换机（p81）
  tags: [structure, webview, ui-zones]

- id: f09
  title: Lightning Config 开局七步流——DHCP 接入 → Recommended Defaults → 改密 → 保存认证
  type: flow
  source_pages: p104-121
  source_chapter: OMNISWITCH LIGHTNING CONFIG / Using OmniSwitch Lightning Configuration
  source_quote: |
    "Port 1 DHCP Client Default IP interface VLAN1 192.168.0.1" (p104)
    "1.Click on RECOMMENDED DEFAULTS 2.Click on LIGHTNING CONFIG • Do NOT skip the Recommended Defaults!" (p115)
    "The new password must meet the following requirements: • At least 8 characters • 1 uppercase letter • 1 lowercase letter • 1 digit • 1 special character (but avoid using ! or $)." (p116)
  summary: |
    七步流：①笔记本设 DHCP，网线接交换机端口 1（唯一连线，禁止预接线/接 DHCP 服务器/先接外设，p108）；②上电等约 3 分钟看绿灯，笔记本被交换机 DHCP 分到 192.168.0.200/24；③浏览器开 https://192.168.0.1/（必须 https），接受自签名证书；④admin/switch 登录；⑤RECOMMENDED DEFAULTS → LIGHTNING CONFIG 填必填项（IP/掩码/网关，全网唯一）；⑥YES 应用后立即改 admin 密码（≥8 位含大写/小写/数字/特殊字符，避开 ! 与 $）；⑦保存为 working 版（耐心等绿条），主页继续接边缘设备/其他已配置 ALE 交换机。扩展：IMPORT 导入架构师给的 .json 模板再走 Lightning Config；主页有 Quick Links、搜索、PoE 状态（看 Power mW 列）；每次改动必须 Write Memory。
  conditions: 全程禁止连接未开局的出箱交换机到其他交换机（p117）；适用任意 ALE 6360 交换机口径见 p106
  tags: [flow, lightning-config, zero-touch, onboarding]

- id: f10
  title: 示例网络拓扑两型——纯二层中型网与 Mesh/三层中型网
  type: diagram
  source_pages: p122-125
  source_chapter: ONE SIZE DOES NOT FIT ALL / SAMPLE NETWORK TOPOLOGIES
  source_quote: |
    "MEDIUM NETWORKS – LAYER 2 ONLY ... Small core VMS - Storage Link Aggregation 20Gigs Virtual Chassis 8 Max" (p123)
    "MEDIUM NETWORKS, WITH MESH LAYER 2 OR SPB/LAYER 3 ... Full Layer 3: OSPF, BGP, SPB, PIM Dual core 100G stacking" (p124)
    "If you have been given instructions to interconnect switches in a manner similar to those listed in the preceding templates, please STOP and consult with the solution architect to ensure they have implemented loop avoidance network technologies" (p125)
  summary: |
    两张参考拓扑：①纯二层中型网——小核心（VMS 存储）+ 虚拟机箱（≤8）+ 20G 链路聚合，摄像头容量上限 1952（受上行速率制约，P24/48Z .bt 供电，X10 无 PoE）；②Mesh/三层中型网——双核心 100G 堆叠、4X25G/4X10G/20 1G 上行、OSPF/BGP/SPB/PIM 全三层、备份电源强制、Multigig .bt 90W 可至 2K PoE。硬性提醒：两张图都有物理环路，照图接线前必须确认环路避免技术（STP/DHL 等）已实施，否则 STOP 找架构师。
  conditions: 拓扑为教学示例；容量数字受上行速度约束（原文标注 subject to uplink speeds）
  tags: [diagram, topology, l2, l3, loop-avoidance]

- id: f11
  title: 闪存目录三层模型与启动序列——working/certified/running + 引导链
  type: diagram
  source_pages: p129-131
  source_chapter: AOS MANAGING FILES/DIRECTORIES
  source_quote: |
    "The certified directory contains files that have been certified by an authorized user as the default files for the switch. ­ The working directory is a holding place for new files." (p141, How-To 重述)
    "• Bootstrap Basic Operation (U-Boot) • Hardware Initialization • Memory Diagnostics • Image selection • AOS is copied and loaded into RAM" (p130)
    "Command to force reboot from CERTIFIED directory: -> reload all ... -> reload from working no rollback-timeout -> reload from <userdefined> no rollback-timeout" (p131)
  summary: |
    闪存结构：/flash 下 working（试验场）、certified（认证基线）、用户自定义目录（任意名，可存多套镜像+vcboot.cfg/vcsetup.cfg）、network 目录、日志（swlog_chassis1..1.6 + swlog_archive 最多 40 文件）。启动序列四步：U-Boot 引导 → 硬件初始化与内存诊断 → 镜像选择（按各目录 KERNEL.LNK）→ AOS 载入 RAM（镜像自带内核）。关键规则：冷启动时若 running 目录与 certified 内容不同则从 certified 启动，相同则从 running 启动；reload all 无条件从 certified 启动；reload from <dir> 指定目录启动。
  conditions: 镜像文件名随产品代际不同（Nosa/Nos/Wos/Dos/Uos/Uosn/kaos/Yos/Ypos/Mhost/Mos/Meni.img，p129）
  tags: [diagram, flash, boot-sequence, directories]

- id: f12
  title: 配置保存/认证/回滚状态机——write memory → copy running certified → flash-synchro
  type: flow
  source_pages: p132-135
  source_chapter: AOS MANAGING FILES/DIRECTORIES / Configuration Rollback
  source_quote: |
    "sw7 (OS6860-A) -> write memory ... Running configuration: SYNCHRONIZED" (p132)
    "sw7 (OS6860-A) -> copy running certified ... sw7 (OS6860-A) -> write memory flash-synchro = write memory + copy running certified" (p133)
    "Loads and certifies the images in the WORKING directory on the next reload or power cycle : certify-on-reboot" (p134)
    "When the switch boots from the CERTIFIED directory, changes made to the switch cannot be saved and files cannot be moved between directories." (p135)
  summary: |
    状态机五态：①RAM 改动未保存——show running-directory 显示 Running Configuration: NOT SYNCHRONIZED，重启即丢；②write memory——RAM 同步到启动目录（working），Certify/Restore Status 变 CERTIFY NEEDED；③copy running certified——working 覆盖 certified，状态回 CERTIFIED；④write memory flash-synchro——前两步合并（VC 下同步全体成员）；⑤certify-on-reboot——把 working 目录镜像在下次重启时认证加载（仅当次登录有效，需再固化）。硬约束：从 certified 目录运行时禁止 write memory、禁止在目录间移动文件。
  conditions: copy running certified 只应在 running 配置验证无误后执行（p146 Notes）
  tags: [flow, rollback, write-memory, certified, state-machine]

- id: f13
  title: 配置备份恢复与 USB 备份结构
  type: structure
  source_pages: p136-137, p148-149
  source_chapter: CONFIGURATION BACKUP & RESTORE / USB Backup and Restore
  source_quote: |
    "Backup of the session banner, userTable* and vcboot.cfg files • The configuration backup command creates a .tar file ... will be placed in '/flash/config-backup-recovery' folder • Up to 10 .tar files can be stored" (p136)
    "usb backup admin-state {enable | disable} [key <> | hash-key<>] ... usb auto-copy <enable | disable> copy-config <enable| disable> from <directory-path>" (p137)
    "CAUTION: Do usb disable before removing usb" (p148)
  summary: |
    两条备份线：①内置配置备份——备份会话横幅、userTable、vcboot.cfg 打成 configuration_backup.tar 放 /flash/config-backup-recovery（上限 10 个 tar），restore 时自动选取解包；②USB 备份——启用 usb backup admin-state 后，write memory/copy running-certified/flash-synchro 自动把镜像与配置同步到 /uflash/<型号>/certified 与 running 目录；usb auto-copy 支持从 U 盘恢复；启用时设 key 则备份内容加密。操作纪律：拔 U 盘前必须 usb disable。
  conditions: R-Lab 无法演示 USB 备份（USB 口被 USB-to-Eth dongle 占用，p148）
  tags: [structure, backup, usb, tar]

- id: f14
  title: Virtual Chassis 每型号规模与 VFL 端口矩阵
  type: structure
  source_pages: p152-154, p159
  source_chapter: VIRTUAL CHASSIS – OVERVIEW / TOPOLOGIES / AUTO VFL PORT
  source_quote: |
    "OS6465 Up to 2 VFL stacking ports ... 4 x OS6465 ... OS6560 ... 8 x OS6560 ... 8 x OS6865/OS6860/E/N ... 2 x OS9900 ... 8 x OS6570" (p153)
    "Support of 2,3,.. up to 6 in Partial or fully Mesh topology OS6900-Q32 / OS6900-X72" (p154)
    "New command introduced when adding a 6900-X48C4E to a VC : capability vfl-type {standard | mixed}" (p154)
  summary: |
    规模矩阵：OS6465=4、OS6560=8、OS6865/6860/E/N=8、OS6570M=8、OS6360=4（24/48 口）或 8（10 口机型）、OS9900=2、OS6900 全系=6（部分/全网格，X/T 系与 V72/C32/E/X48C6/T48C6/V48C8/X24C2/T24C2/X48C4E 两大混插组）、OS6870=8。VFL 端口：OS6465 ≤2 个 stacking 口、OS6560 专用 20G VFL 口+末两个 10G SFP+、OS6900 ≤16 个 VFL 成员口（10G SFP+/40G QSFP+/100G QSFP28）、OS9900 ≤8 个（40G QSFP 分裂线/100G）。Auto VFL 合格端口表：OS9900 仅静态 VFL；OS6900 X/T 每机箱最后 5 口；OS6860/6860N 专用 VFL 口；OS6465-P28 27/28；OS6560 (P)24X4/(P)48X4 专用口+末两个 10G SFP+；OS6360-24 27/28、-48 51/52。
  conditions: 混插约束：6900-X48C4E 加入 VC 需 AOS 8.9R4 最低并配合 capability vfl-type 命令（p154）
  tags: [structure, virtual-chassis, vfl, capacity]

- id: f15
  title: VC 选举与接管规则——四级优先序 + MAC retention + 原主不抢回
  type: flow
  source_pages: p155-157
  source_chapter: VIRTUAL CHASSIS TOPOLOGY MANAGER / ROLES AND ELECTIONS / TAKEOVER/FAILOVER
  source_quote: |
    "VC topology managed by ISIS-VC • Private TLV report the switch's capability and numbering ... • Break equal-cost ties in a deterministic manner ala SPBM" (p155)
    "Master/Slave election based on virtual chassis protocol (ISIS-VC) Highest chassis priority value Longest chassis uptime (if difference in uptime >10 mn) Smallest Chassis ID value Smallest chassis MAC address" (p156)
    "'MAC retention' is always enabled ... When the 'original' master comes back, no election will be processed, and the 'new' Master will retain its Master role" (p157)
  summary: |
    VC 控制平面：ISIS-VC 私有协议用私有 TLV 交换能力与编号、HELLO 建邻接、维持无环 BUM 拓扑、SPBM 式确定性打破等价路径。主/备选举四级顺序：最高 chassis 优先级 → 最长运行时间（差 >10 分钟才生效）→ 最小 chassis ID → 最小 MAC；master 与 slave 同步镜像文件与配置，slave 更新后需重启。接管：仅 master 重载无 slave 影响；MAC retention 恒开；新主由各成员本地按已知 partner keys 计算，原主恢复后不触发新选举、不得抢回主角色。
  conditions: 优先级改后必须 reload 才生效（p175 Notes）
  tags: [flow, virtual-chassis, election, failover]

- id: f16
  title: VC 分裂防护双机制——带外 EMP RCD 与带内 VCSP helper
  type: diagram
  source_pages: p160-161
  source_chapter: VIRTUAL CHASSIS - SPLIT CHASSIS
  source_quote: |
    "2 mechanisms • Out of Band: EMP Remote Chassis Detection (RCD) • In Band: VC Split Protocol ... RCD use the following IP addresses in order of preference 1. CMM IP address stored in NVRAM (if configured) 2. Chassis EMP IP address" (p160)
    "The former Slave chassis will shutdown all its front-panel user ports to prevent duplicate IP and chassis MAC addresses in the network. The Slave's chassis status will be modified from Running to Split-Topology" (p160)
    "Use the virtual-chassis split-protection admin-state and virtual-chassis split-protection linkagg commands to enable VCSP ... Platforms Supported in R8" (p161)
  summary: |
    分裂场景（VFL 断链导致潜在 MAC/IP 重复）两套防护：①带外 RCD——经管理网 EMP 口宣告 chassis VC 信息变化以侦测分裂；IP 取址优先级 NVRAM 中 CMM 地址 > 机箱 EMP 地址；检出后原 slave 关闭全部前面板用户口、状态转 Split-Topology，VFL 恢复后重启重新加入做回 slave。②带内 VCSP——需上/下游设备作 helper 交换机（R8 支持 OS6870/6860E/N/6900/9900，经 8.9 R03 CLI 指南），VC 每成员建议一个口入 VCSP LAG（virtual-chassis split-protection linkagg），helper 侧用 split-protection helper 命令；分裂时保护模式主角色保留、其余接口（除 VFL 与 LAG）shutdown。
  conditions: 支持 RCD 的平台：OS6870/OS6860E/N/OS6900/OS9900（p160）
  tags: [diagram, virtual-chassis, split, rcd, vcsp]

- id: f17
  title: ISSU 滚动升级流程与 ssh-chassis 远程访问
  type: flow
  source_pages: p162-163, p181
  source_chapter: IN SERVICE SOFTWARE UPGRADE (ISSU) / REMOTE CLI ACCESS THROUGH ANY MEMBER
  source_quote: |
    "• Upload new code, vcsetup.cfg and vcboot.cfg in a new directory (ex. issu_dir) • Launch the dedicated issu command • The image and configuration files are then copied to all of the Slaves • The Slaves are then reloaded from the ISSU directory in order from lowest to highest chassis ID" (p162)
    "ssh-chassis <username>@<chassis-id> ... -> ssh-chassis admin@2 Executing: ssh admin@127.10.2.65" (p163)
  summary: |
    ISSU 四步：上传新代码与 vcsetup.cfg/vcboot.cfg 到新目录（如 issu_dir）→ 发起 issu 命令 → 镜像与配置自动复制到全部 slave → slave 按 chassis ID 从低到高依次从 ISSU 目录重载，业务中断最小化。远程成员访问：ssh-chassis admin@<chassis-id> 内部映射到 127.10.<id>.65，提示符相同需看 show virtual-chassis topology 的 Local Chassis 字段确认连到哪台。
  conditions: 升级期间 VC 拓扑保持；普通成员 CLI 区分靠 Local Chassis 值（p181）
  tags: [flow, issu, upgrade, ssh-chassis]

- id: f18
  title: VC 配置五步与 VC 内同步语义
  type: flow
  source_pages: p164-168, p170-171
  source_chapter: VIRTUAL CHASSIS CONFIGURATION Step by Step / VIRTUAL CHASSIS SYNCHRONIZATION
  source_quote: |
    "Assign a Chassis ID Must be different for each switch belonging to the Virtual Chassis ... Assign a Chassis Group number Must be the same on all the switches ... Define a Priority Between 0 to 255, switch with the highest priority is elected Master" (p167)
    "-> write memory ... Flash Between CMMs : NOT SYNCHRONIZED ... -> copy running certified This command can also be used to synchronize the virtual chassis -> write memory flash-synchro" (p170-171)
  summary: |
    配置五步：①判定走 Auto-VC（无 vcsetup.cfg 时自动建 VC：Auto VFL + Auto Chassis ID）或手动；②每台分配全局唯一 Chassis ID；③分配相同 Chassis Group ID 与优先级（0-255，最高者当选）；④配 VFL（auto：vf-link-mode auto + auto-vf-link-port 指定合格口；static：建 VFL ID 指定成员口）；⑤从含 vcsetup.cfg 的目录 reload。同步语义：write memory 只同步 RAM→各成员 working（Flash Between CMMs 可能 NOT SYNCHRONIZED）；copy running certified 或 write memory flash-synchro 才完成 certified 级同步（Synchronizing chassis N）。
  conditions: write memory 在 chassis ID 变更后会告警"缺失 chassis 配置将被永久清除"需确认（p176）
  tags: [flow, virtual-chassis, configuration, synchronization]

- id: f19
  title: VLAN 三入口结构——静态成员 / UNP 动态分类 / 802.1Q 打标
  type: structure
  source_pages: p185-200
  source_chapter: VLAN MANAGEMENT
  source_quote: |
    "Ports become members of VLANs by • Static Configuration • Mobility/with or without Authentication * • 802.1q" (p185)
    "-> vlan 2 ... -> vlan 2 members port <chassis/slot/port> untagged ... -> vlan 10-15 100-105 200 name 'Training Network'" (p187)
    "4096 unique VLAN Tags (addresses) ... 802.1P • Three-bit field within 802.1Q header • Allows up to 8 different priorities" (p199)
  summary: |
    端口入 VLAN 三通道：①静态——默认 VLAN 1 不可删仅可禁；vlan <id> 建、members port untagged/tagged 挂口、命名、批量（vlan 10-15 100-105 200）；②动态 UNP——按流量特征（MAC/MAC 段/IP/绑定规则/扩展规则）把移动口分入 VLAN，认证方式在 Access Guardian 章；③802.1Q——一条链路承载多 VLAN（4096 tag），tagged 成员跨交换机扩散，物理口始终保留一个默认 VLAN 做二层桥接。监控：show vlan / show vlan members / show vlan members port。
  conditions: UNP 认证相关分支延后到 Access Guardian 章（p185 脚注）
  tags: [structure, vlan, 8021q, static, dynamic]

- id: f20
  title: UNP 分类规则优先级体系（9 条简单规则 + 绑定/扩展规则）
  type: structure
  source_pages: p189-192
  source_chapter: VLAN MANAGEMENT - DYNAMIC VLAN MEMBERSHIP
  source_quote: |
    "UNP Port classification rules 1. Port/Linkagg 2. Domain 3. MAC address 4. MAC-OUI 5. MAC address range 6. LLDP 7. Auth-type 8. IP address 9. VLAN tag" (p189)
    "Precedence: Extended rule > Binding Rule > Simple Rule" (p192)
    "-> unp classification mac-address 00:11:22:33:44:55 ip-address 10.0.0.20 mask 255.255.0.0 port 1/1/1 profile1 employee" (p192)
  summary: |
    分类体系三层：①九条简单规则按编号即优先级（端口/链路聚合 > 域 > MAC > MAC-OUI > MAC 段 > LLDP > 认证类型 > IP > VLAN tag）；②绑定规则（Binding）= 多条简单规则 AND 组合（如 MAC+IP+端口）；③扩展规则（Extended）= 命名规则列表 + precedence 值（如 ext-r1 = 端口 + vlan-tag），设备须匹配列表内全部规则。生效条件：UNP 口启用但认证关闭或失败时应用分类规则；典型用法是 def_unp 默认档案映射黑名单 VLAN + 分类规则命中则入业务 VLAN。
  conditions: 认证开启时的分支流程见 Access Guardian（f27）
  tags: [structure, unp, classification, precedence]

- id: f21
  title: VLAN 间路由与 IP 接口绑定模型
  type: diagram
  source_pages: p194-196, p348
  source_chapter: INTER VLAN ROUTING / IP INTERFACE
  source_quote: |
    "IP interfaces are associated with VLANs • IP routing is active as soon as at least one IP interface is associated with a VLAN" (p195)
    "ip interface Data address 10.1.20.254 mask 255.255.255.0 vlan 20 ... ip interface Voice address 10.1.60.254 mask 255.255.255.0 vlan 60" (p196)
    "The first interface bound to a VLAN becomes the primary interface for that VLAN." (p348)
  summary: |
    模型：IP 接口（虚拟路由器口）绑定 VLAN 充当该网段网关；≥1 个 IP 接口存在即激活 IP 路由；VLAN 无活动成员口则 oper 状态 down、其 IP 接口 DOWN 且不进路由通告（但二层广播域不受影响）。接口特征：掩码可用点分或 /24；第一个绑定该 VLAN 的接口为主接口；命令 ip interface <name> address <ip/mask> vlan <id> 一步完成。监控 show ip interface / show ip routes（LOCAL 路由自动生成）。
  conditions: EMP/Loopback 为系统接口不占 VLAN 绑定语义
  tags: [diagram, routing, ip-interface, vlan]

- id: f22
  title: OST 工具两代架构——1.0 单机社区版与 2.0 Client-Server
  type: structure
  source_pages: p215-230
  source_chapter: ALE OMNIVISTA SMART TOOL (OST) / OST 2.0 CLIENT SERVER ARCHITECTURE
  source_quote: |
    "One button repairs for PoE devices that won't boot • Debug and open tickets with Tech Support with a single button • One button network health analysis" (p217)
    "The second release of OST supports a Client-Server architecture with multiple users connected to a single server. Data from OmniSwitches persisted in a PostgresSQL database." (p224)
    "Store information • 100 switches • 4000 devices • 5 clients (simultaneous) • Security: Encrypt contents of database to secure data-at-rest" (p225)
  summary: |
    OST 功能五块：装机与排障（快速识别接入设备）、PoE 向导（逐设备验证/一键修复不启动 PoE 设备/查剩余预算/提醒旧软件）、快捷工具（Reset Port/Cable Test/ping）、Auto-Ticket（开低层 debug+自动重置端口+收集 TAC 材料+生成工单模板）、流量分析（坏线/SFP、丢包、广播风暴、组播问题，可存档供 AI 复核）、Config 向导与备份恢复（类 Lightning Config 任意 ALE 交换机、RMA 换机还原）。1.0：Spacewalkers/GitHub 社区版，ALE 不再开发；2.0：Client-Server + PostgresSQL，容量 100 交换机/4000 设备/5 并发客户端，静态数据加密，经 MyPortal 免费下载（需有效 OmniSwitch 支持合同；BP 需分销协议）。
  conditions: OST 支持条件与 OmniSwitch 支持协议绑定（p229）
  tags: [structure, ost, tooling, architecture]

- id: f23
  title: 诊断工具箱八件套结构
  type: structure
  source_pages: p232-259
  source_chapter: DIAGNOSTIC TOOLS
  source_quote: |
    "Switch events can be logged to • Switch console • Local text file • Configurable default file size 1250 Kbytes • Multiple remote devices (syslog) 12 max" (p235)
    "Copies all incoming and outgoing traffic from one switch port to another • Destination port could be local (same switch) or remote (different switch)" (p248)
    "Captures data and stores in Sniffer format on switch ... Captures first 64-bytes of frame • Session supported per switch or stack: 1 • Default file size: R8: 64 KB (max = 2 MB)" (p251)
  summary: |
    八件套：①switch logging（swlog）——输出到 console/flash/syslog（≤12 台），默认单文件 1250KB、存 8 个 swlog 文件 + 归档 40、severity 默认 info(6)、按 appid/subapp 细粒度调级、RFC5424 可选；②可读客户事件日志——swlog appid all subapp all level event + show log events；③command logging——command.log 存最近 100 条命令（命令/用户/时间/来源 IP/结果），启用期间不可删；④port mirroring——复制流量到本机或远端口；⑤port monitoring——本机抓包存 .enc（Sniffer 格式，前 64 字节，1 会话，64KB 默认上限 2MB）；⑥RMON——统计/历史/告警/事件四组供 OmniVista 取数；⑦health——CPU/内存当前/1 分钟/1 小时/1 天均值与阈值；⑧sFlow——agent/receiver/sampler/poller 四角色采样计数。
  conditions: 镜像与抓包不能配在同一端口（p251）；规格上限随型号，查 Specification Guide（p248/p251）
  tags: [structure, diagnostics, logging, mirroring, sflow]

- id: f24
  title: 链路聚合结构——静态 vs LACP + hash 控制矩阵
  type: structure
  source_pages: p270-281
  source_chapter: LINK AGGREGATION GROUPS
  source_quote: |
    "Static • Port parameters MUST be exactly the same at both ends and within the group ... • Only works between Alcatel-Lucent OmniSwitches • Dynamic • IEEE 802.3ad LACP • LACP will negotiate the optimal parameters for both ends using LACPDU" (p273)
    "Two hashing algorithms available • Brief Mode • UDP/TCP ports not included ... • Extended • UDP/TCP ports to be included ... Switch Default Hashing Mode 9900 extended 6900 brief 6870 extended 6860 extended 6865 extended 6560 extended 6465 brief 6360 brief" (p280)
    "Multicast traffic is by default forwarded through the primary port of the Link Aggregation Group" (p281)
  summary: |
    聚合两型：静态（两端与组内参数完全一致、仅 ALE 设备间可用）与动态 LACP（LACPDU 协商、可接服务器/存储）。负载分担：hash-control brief（仅源/目的 IP）或 extended（含 UDP/TCP 端口，分担更均匀），出厂默认逐型号不同（9900/6870/6860/6865/6560=extended；6900/6465/6360=brief）。组播默认仅走主端口，可用 non-ucast 选项启用非单播 hash。监控四命令：show linkagg counters/traffic/accounting/port。逻辑链路可静态划入任意 VLAN 并跑 802.1Q。
  conditions: 同组端口必须同速率（p273）
  tags: [structure, linkagg, lacp, hashing]

- id: f25
  title: STP 体系——两种模式 × 三种协议 + 路径成本与保护特性
  type: structure
  source_pages: p300-311
  source_chapter: SPANNING TREE
  source_quote: |
    "Supports two Spanning Tree operating modes: • flat (single STP instance per switch) • per-VLAN (single STP instance per VLAN) (By default on OmniSwitch)" (p300)
    "STP (802.1d): Convergence time : 50 secs • RSTP (802.1w): Convergence time : < 1 sec • MSTP (802.1s): < 1 sec" (p300)
    "-> spantree cist port 1/1/2 restricted-role enable ... -> spantree cist port 1/2/2 restricted-tcn enable" (p311)
  summary: |
    STP 结构：模式两种——flat（每交换机一实例）与 per-VLAN/1x1（每 VLAN 一实例，OmniSwitch 默认，可按 VLAN 调优先级实现负载分担）；协议三种——STP(802.1d, 收敛 50s)/RSTP(802.1w, <1s)/MSTP(802.1s, <1s)。路径成本两套：16 位（10M=100/100M=19/1G=4/10G=2）与 32 位（200 万/20 万/2 万/2000），path-cost-mode auto 时 16 位随 STP/RSTP、32 位随 MSTP。优先级：桥 0-65535（MSTP 须 4096 倍数）、端口 0-15。保护三件：restricted-role（根端口防护）、restricted-tcn（TCN 传播限制）、qos user-port 过滤用户口 BPDU。监控：show spantree / show spantree vlan <id> ports / show spantree ports blocking。
  conditions: 各型号支持集查 Specification Guide（p301）
  tags: [structure, stp, rstp, mstp, protection]

- id: f26
  title: DHL Active-Active 机制结构——会话/双链/VLAN 映射/MAC flushing
  type: diagram
  source_pages: p326-334
  source_chapter: DUAL-HOME LINK REMINDER / DHL CONFIGURATION
  source_quote: |
    "DHL Active-Active splits VLANs between two active links • The forwarding status of each VLAN is modified by DHL to prevent network loops" (p326)
    "• Only one session per switch is allowed. • Each session has only two links (linkA and linkB). ... • DHL is not supported on mobile, 802.1x-enabled, GVRP, or UNI ports" (p327)
    "• RAW Flooding ... • MVRP Enhanced ... • None (default): The staled MAC address entries are kept in the MAC table" (p328)
  summary: |
    DHL 结构：每交换机 1 会话、每会话 2 链路（LinkA/LinkB，物理口或 linkagg 皆可，不可同口兼任）；一组 VLAN 同时 802.1Q tagged 在两条链上，vlan-map linkb 指定 LinkB 服务哪组 VLAN（其余自动归 LinkA），故障时 VLAN 全量切到存活链。约束：DHL 端口自动禁 STP；不支持 mobile/802.1x/GVRP/UNI 口；pre-emption 定时器 0-600 秒控制恢复链路何时收回 VLAN。MAC 刷新三选项：RAW Flooding（用非 DHL 口学到的 MAC 清单发广播帧刷表）、MVRP Enhanced（带 new 标志的 join 消息）、None（默认，保留 stale 表项）。对比定位：STP 省一半带宽、LACP 与 DHL 全带宽，DHL 不做交换机级冗余。
  conditions: LinkA/LinkB 必须同属一个默认 VLAN（p337）
  tags: [diagram, dhl, active-active, redundancy]

- id: f27
  title: Access Guardian/UNP 认证决策流与配置五层
  type: diagram
  source_pages: p456-459, p461-468, p474
  source_chapter: ACCESS GUARDIAN / CONFIGURATION STEPS
  source_quote: |
    "Role Based Access Control with UNP (Universal Network Profile) • Auto-sensing, multi-client authentication on a port" (p456)
    "Authentication Method • MAC-based (non-supplicant) or • 802.1x-based (supplicant) ... RADIUS Access-Accept + UNP name" (p457)
    "unp auth-server-down profile1 profile_name ... Auth Server Down Timeout = 60" (p474)
  summary: |
    决策流：802.1x 开？→ supplicant 走 802.1x（EAP→交换机改写→RADIUS）；否则 MAC 开？→ 非客户端走 MAC 认证（源 MAC 作账号密码）；两者都关走无认证分支。认证结果分支：Pass→按 RADIUS Filter-Id 下发的 UNP 入网；Fail→进 Default UNP（注册/隔离）；服务器不可达→auth-server-down 档案（默认 60 秒重试重认证）；无匹配→Block 或 pass-alternate 档案。配置五层：①unp port port-type bridge + 802.1x/mac-authentication；②validity-location / validity-period 位置时段策略；③policy list type unp 挂 ACL 规则；④unp profile（qos-policy-list/location-policy/period-policy/map vlan）；⑤端口模板与 AAA profile（aaa profile 设备认证+服务器+计费）；RADIUS 服务器缺省 retries 3/timeout 2s/auth 1812/acct 1813，MAC 会话超时默认 12 小时。
  conditions: RADIUS Filter-Id 属性回传 UNP 名（p457/p480 Notes）；服务器侧用户库在书外
  tags: [diagram, access-guardian, unp, 8021x, radius]

- id: f28
  title: LLDP/LLDP-MED 信息模型与 IP 电话自动语音 VLAN 流
  type: diagram
  source_pages: p488-499
  source_chapter: LINK LAYER DISCOVERY PROTOCOLS (LLDP) / LLDP-MED / LLDP NETWORK POLICY TLV
  source_quote: |
    "IEEE 802.1AB – Link Layer Discovery Protocol (LLDP) ... L2 discovery protocol • Exchange information with neighboring devices to build a database of adjacent devices • Enabled by default on the OmniSwitches" (p488)
    "MED: Power and Capability • Inventory Management • Network Policy" (p489)
    "(OS6860-A) -> unp profile 'voip-temp' mobile-tag ... (OS6860-A) -> unp classification lldp med-endpoint ip-phone profile1 'voip-temp' ... (OS6860-A) -> lldp network-policy 1 application voice vlan 151 l2-priority 5 dscp 46" (p496)
  summary: |
    信息模型：LLDPDU=必选 TLV（Chassis ID/Port ID/TTL）+ 可选 TLV（802.1 VLAN 名/802.3 MAC-Phy/MED 供电能力/资产/网络策略）；默认收发双开、30 秒发送间隔（TTL 倍乘 4）。LLDP-MED 为 VoIP 扩展四件：网络策略（VLAN/L2 优先级/DSCP 按应用类型）、位置 ID（紧急呼叫）、扩展供电（PSE/PD/优先级/功率）、资产清单。IP 电话流：交换机配 lldp network-policy（application voice + vlan + l2-priority + dscp）→ chassis med network-policy 挂接 → 端口使能 med network-policy/capability TLV → 话机收到 LLDP 帧后把语音流量打入指定 VLAN 并打标；配合 unp mobile-tag + unp classification lldp med-endpoint ip-phone 实现话机口动态入 VLAN。
  conditions: LLDP 配置层级为端口/槽/机箱，不支持 linkagg 级（p502 Tips）
  tags: [diagram, lldp, lldp-med, voice, voip]

- id: f29
  title: PoE 管理体系——供电等级表/优先级/特殊特性
  type: structure
  source_pages: p508-520
  source_chapter: POWER OVER ETHERNET (POE)
  source_quote: |
    "Property 802.3af (802.3at Type 1) 'PoE' 802.3at Type 2 'PoE+' 802.3bt Type 3 '4PPoE'/'PoE++' 802.3bt Type 4 ... Power available at the PD 12.95 W 25.50 W 51 W 71 W ... Maximum power delivered by the EPS 15.40 W 30.0 W 60 W 100 W" (p513)
    "Fast PoE : 2X60, 6360, 6860E, 6860N, 6865, 6870 • Note: OS6360 – P10A does not support FPoE" (p510)
    "Setting Port Priority Levels (Low, High, Critical) • Default priority level for a port is low" (p517)
  summary: |
    PoE 结构五块：①等级——802.3af（PD 12.95W/PSE 15.4W/350mA/3 级/class）、802.3at Type2（25.5/30/600mA/4 级）、802.3bt Type3（51/60/每对 600mA/6 级）、bt Type4（71/100/每对 960mA/8 级），全部 Cat5（af 可 Cat3）；②端口 LED——琥珀=已供电，绿=已连接未供电；③预算管理——lanpower port power（mW）/slot maxpower（W）/show lanpower（余量、实际功耗）；④优先级——low（默认）/high/critical 三档决定断电顺序，priority-disconnect 决定预算不足时新 PD 准入；⑤特殊特性——Fast PoE（上电即供不等系统起完）与 Perpetual PoE（重启不断电）支持 2X60/6360/6860E/N/6865/6870（OS6360-P10A 除外，且需升级 FPGA/CPLD）；delayed-start 延迟 120-600 秒（5 的倍数）再启动 lanpower 服务；EEE（802.3az）仅铜口 100/1000M。
  conditions: 每型号 PoE 预算不同，查 specification guide/datasheet（p514）
  tags: [structure, poe, power, fast-poe]

- id: f30
  title: 软件升级三通道与安全版本线
  type: structure
  source_pages: p529-535
  source_chapter: UPGRADING SOFTWARE IMAGE
  source_quote: |
    "Starting with 8.10R4 signed images are available for the whole portfolio (already available for OS6570M since 8.9R4) • U-boot password protection is available since 8.7R3 – be careful when enabling it (no AOS recovery possible in case you lose this password)" (p531)
    "Generally, use the latest 'GA' (General Availability) or 'MR' (Maintenance) release ... For FIPS 140-2 ... For JITC ... For Common Criteria" (p532)
    "Directly to the switch, using FTP/SFTP • Using OmniVista on premises (2500 4.X or Terra) • Using OmniVista Cirrus <= easiest way, recommended software package available directly from the application" (p533)
  summary: |
    升级结构：三通道——直连 FTP/SFTP、OmniVista 本地（2500 4.X/Terra）、OmniVista Cirrus（最简单，软件包直接内置推荐）；U-boot/ONIE/FPGA/CPLD 升级走 CLI 且失败即 RMA。版本策略：一般取最新 GA/MR；合规场景按 FIPS 140-2/JITC/Common Criteria 认证版本表选。安全线：8.10R4 起全系列签名镜像（OS6570M 自 8.9R4）；U-boot 密码保护 8.7R3 起可用但丢失即无法恢复；软件包从 MyPortal 按品类（Switches/WLAN/Network Management）下载。本教材不展开升级步骤，指回 AOS Release Notes。
  conditions: 升级属标准操作，细节在 Release Notes（p533）
  tags: [structure, upgrade, release, security]

- id: f31
  title: Auto-Fabric 零触开局七步链与 LBD 环路检测
  type: flow
  source_pages: p536-553
  source_chapter: INTELLIGENT FABRIC / AUTO-FABRIC
  source_quote: |
    "1- Auto-VC 2- Automatic remote configuration 3- Auto-LACP 4- Auto-Routing 5- Auto-SPB Fabric 6- Auto-Network Profiling 7- Auto-MVRP" (p538)
    "RCL tries 6 times, 3 each on VLAN 1 and 127 to get DHCP and download instruction file • To cancel RCL, run command 'auto-config-abort' • At the end of RCL, if a vcboot.cfg is downloaded, the box will be reset" (p543)
    "Default SPB configuration • BVLANs 4000-4015 mapped to ECT-IDs 1-16 respectively • Control BVLAN: 4000 • Bridge priority: 0x8000" (p547)
  summary: |
    七步链（首启或无配置重载触发，启动提示 Y=禁用/N 或不答=启用）：①Auto-VC——同族发现自动成堆叠（Auto VFL+Auto Chassis ID，Demo License 默认启用）；②RCL 自动远程配置——VLAN 1 与 127 各 3 次共 6 次 DHCP 取指令文件，可 auto-config-abort 取消，下载到 vcboot.cfg 则重置生效；③Auto-LACP——LLDP 私有 TLV 探测对端，成功则聚合（示例 agg 127 size 16 actor admin-key 65535）；④Auto-Routing——OSPFv2/v3、IS-IS 以 Hello 学网络配置并自动建 route-map 重发布本地子网；⑤Auto-SPB——4 个 Hello（4×9 秒）内未成邻接则不参与，默认 BVLAN 4000-4015→ECT 1-16、控制 BVLAN 4000、桥优先级 0x8000；⑥Auto-Network Profiling——接入端口单服务/自动 VLAN 服务画像；⑦Auto-MVRP——LACP 与 SPB 发现后全局启用 MVRP 并把 STP 切 flat。伴随 LBD 环路检测：周期组播帧回收即判环路→端口强制 down+日志+SNMP trap，可手动恢复；SPB SAP 口按 ISID 检测。
  conditions: 各协议可单独 auto-fabric protocols <x> admin-state disable（p553）
  tags: [flow, auto-fabric, zero-touch, lbd, spb]

- id: f32
  title: Fleet Supervision 与 Services Kiosk 结构
  type: structure
  source_pages: p555-568
  source_chapter: OVERVIEW AND BASIC SET-UP / FLEET SUPERVISION
  source_quote: |
    "Register your serial numbers or OmniVista Management platform ID to track your fleet effortless ... Identify device with no or expiring support • Request coverage from your partner. ... Free of charge ... Services Kiosk https://myfleet.ovcirrus.com/" (p558)
    "Sign up and sign in • https://myfleet.ovcirrus.com/signup ... Declare • an OmniVista Management system • OV 2500 on premise • Legacy OV Cirrus 4.X • New OV Cirrus (10.5 and upwards) • OR Import your device list using the template file." (p563)
  summary: |
    Fleet Supervision 四块能力：软件版本可视（受管设备）、库存可视化（机箱/电源/光模块/AP 明细钻取）、KPI 仪表盘（硬件生命周期 GA/EoS/EoL、软件版本分布、维保 Active/Expired/None、硬件支持 AVR/RTF）、资产汇聚（OmniVista 自动收集或 CSV/XLSX 手工导入）。开通三路：声明 OV 2500（取 OV2500 ID：Administration > Preferences > System Settings > Fleet Supervision）、声明 OV Cirrus 4.X（实例 URL + API Key，Security > External Apps）、声明 OV Cirrus 10.5+（URL + Organization ID + Application ID/Secret）；无 OmniVista 时用模板文件导入设备清单。Services Kiosk 免费识别无支持/将到期设备并申请续保。
  conditions: 免费但只读监管；配置管理仍在 OmniVista/CLI（p556-558）
  tags: [structure, fleet-supervision, assets, compliance]

- id: f33
  title: OST 2.0 安装组件与依赖链
  type: flow
  source_pages: p572-580
  source_chapter: OmniVista Smart Tool Installation Guide
  source_quote: |
    "Minimum version 10, 11 ... Version 18.1 is tested. ... Run the setup on your server: postgresql-18.1-2-windows-x64.exe" (p573)
    "The application consists of three main components: • Server: Backend API and Windows Service ... • Client: Desktop application ... • Server Configuration Tool: Initial setup wizard" (p573)
    "Run OmniVistaSmartTool.ServerConfig.exe (C:\Program Files\Alcatel-Lucent Enterprise\Tools\Server Configuration Wizard)" (p577)
  summary: |
    安装链四步：①前置——Windows 10/11 + Postgres（测试版本 18.1，先于 OST Server 安装，设库密码保默认端口，不装 Stack Builder）；②装 OST 2.0——Server（与 Postgres 同机）+ Client 默认同机安装；③Server Configuration Tool 初始化——运行 OmniVistaSmartTool.ServerConfig.exe，填 Postgres 密码测试连接，再定义 OST admin 密码；④Client 连接 Server 后添加交换机。三组件分工：Server=后端 API+Windows 服务，Client=图形桌面，Config Tool=初始化向导。
  conditions: Postgres 必须先装；数据库密码即 Server Config 时所填（p574-577）
  tags: [flow, ost, installation, postgres]

- id: f34
  title: QoS 端口队列模型——QSet/QSI/QSP 与策略引擎接入
  type: diagram
  source_pages: p393-409
  source_chapter: QOS REMINDER / QOS CONFIGURATION
  source_quote: |
    "QSet Profile 1 Q1 = SP7, 100% BW ... Q8 = SP0, 100% BW Strict Priority (SP)" (p397)
    "-> qos qsi port 1/2/1 qsp 2 ... qos qsp system-default 2 ... * Eg: QSet Profile 2 (1 EF + 7 SP)" (p398)
    "A policy (or a policy rule) is made up of: 1. a condition 2. an action ... Gets Policies from • CLI • Webview • PolicyView (OV)" (p400)
  summary: |
    两层结构：硬件队列层——每端口 8 个队列（QSI），队列集档案 QSP 1=8×严格优先级（各 100% BW），QSP 2=1×EF+7×SP 等，可按端口/linkagg 改 QSI 的 QSP 或改系统默认（qos qsp system-default）；策略层——policy condition（L1-L4 条件）+ policy action（accept/drop/deny、优先级、带宽/深度、802.1p/TOS/DSCP 标记映射、PBR 网关、镜像、端口禁用、CIR 限速）+ policy rule（precedence、validity-period、log、count），qos apply 下发生效。策略来源 CLI/WebView/OmniVista PolicyView。auto-QoS：qos phones 按 alaPhones MAC 组（00:80:9F 企业话机/78:81:02/00:13:FA Lifesize/48-7A-55 ALE 8008）自动给 ALE 话机流量优先级 5。
  conditions: 规则计数仅 6860(E)/6865/6900-X72 支持 count（p407）
  tags: [diagram, qos, queue, policy, auto-qos]

- id: f35
  title: VRRP 结构——虚拟路由器/优先级/抢占/跟踪策略
  type: diagram
  source_pages: p374-381
  source_chapter: VRRP REMINDER / VRRP CONFIGURATION STEPS
  source_quote: |
    "Multicast - 224.0.0.18 Virtual MAC address: 00-00-5E-00-01-{VRID}" (p375)
    "Base set of tracking policies supported: • ADDRESS • IPV4-INTERFACE • IPV6-INTERFACE • PORT • VLAN" (p377)
    "ip vrrp 1 interface int_20 priority 100 preempt interval 100 ... * At least two virtual routers must be configured on the LAN—a master router and a backup router." (p379-380)
  summary: |
    VRRP 结构：主+备虚拟路由器共享虚拟 IP（终端网关）与虚拟 MAC 00-00-5E-00-01-{VRID}，组播 224.0.0.18 通告；支持 RFC 2338/2787。配置三件套：ip vrrp <vrid> interface <if> → address <vip> → admin-state enable；完整版加 priority（默认 100，值大者主）/preempt（默认允许，no pre-empt 可禁）/interval（V2 同 VRID 可同间隔）。负载分担：两个 VRID 各主一组 VLAN。跟踪策略五类（ADDRESS/IPV4-INTERFACE/IPV6-INTERFACE/PORT/VLAN）：ip vrrp track <id> ... priority <降级值> 绑定被跟踪对象，再 track-association 挂到 VRID——上行故障自动降优先级让备接管。
  conditions: 版本 V2（实验 show 输出 Version = V2，p387）
  tags: [diagram, vrrp, gateway, redundancy, tracking]

- id: f36
  title: ACL 条件关键字分层与保留安全组
  type: structure
  source_pages: p431-443
  source_chapter: ACCESS CONTROL LISTS (ACL) / ADVANCED ACL SECURITY FEATURES
  source_quote: |
    "LAYER 2 ACL CONDITION KEYWORDS source mac ... LAYER 3 ACL CONDITION KEYWORDS source ip ... MULTICAST ACL CONDITION KEYWORDS multicast ip" (p432)
    "Used by default to prevent spoofed IP addresses on ports ... Done by creating a port group called UserPorts and adding the ports to that group ... -> qos user-port filter spoof rip ospf bgp" (p440)
    "Any services belonging to this group will be dropped if seen on ports included in the UserPorts group" (p441)
  summary: |
    ACL=同引擎策略的过滤用法（disposition accept/drop/deny）。条件按层分箱：L2（MAC/MAC 组/源 VLAN/端口/ethertype/802.1p）、L3/L4（IP/IPv6/网络组/协议/ICMP 类型码/TOS/DSCP/TCP/UDP 端口与业务组/established/tcpflags）、组播（组播 IP/组播网络组）。保留组三件：①UserPorts 端口组——反 IP 欺骗（源 IP 与端口子网不符即丢，仅作用于路由流量）+qos user-port filter/shutdown（spoof/bgp/bpdu/rip/ospf/vrrp/dvmrp/pim/isis/dhcpserver/dns-reply）；②DropServices 服务组——在 UserPorts 口上丢弃指定 TCP/UDP 服务（如 135/445/137）；③port-disable 规则——命中即管理性关闭端口，配 interfaces violation-recovery-time 自动恢复与 recovery-trap。另有点缀：ICMP 丢弃规则、早期 ARP 丢弃（默认启用）、ip directed-broadcast disable。
  conditions: 默认不匹配任何策略的流被接受（p434）
  tags: [structure, acl, userports, security]

- id: f37
  title: IP 服务基础件——DHCP Client/Relay/UDP Relay/Loopback0/静态路由
  type: structure
  source_pages: p349-365
  source_chapter: IP INTERFACES
  source_quote: |
    "-> ip interface dhcp-client [vlan vid] [release | renew] [option-60 string]" (p350)
    "Two types of DHCP relay agents: global and per-interface. ... They are mutually exclusive" (p353)
    "• Not bound to any VLAN • Always remain operationally active (as long as at least one VLAN is active) ... • Automatically advertised by RIP and OSPF protocols when the interface is created (not by BGP)" (p360)
  summary: |
    五个基础件：①DHCP Client——任意 VLAN 单接口动态取址（RFC 2131 release/renew、Option-60 串），租约四选项落地（Option-1 掩码/Option-3 网关生成默认路由/Option-58/59 续租/Option-51 租期），并作 VLAN 主地址；②DHCP Relay——全局型（ip dhcp relay destination + admin-state enable）与接口型（per-interface-mode + interface <if> destination）互斥，参数 max hops 16、Opt82 Base MAC、PXE 默认关；③UDP Relay——tftp/tacacs/ntp/nbns/nbdd/dns 或自定义端口按 VLAN/地址转发；④Loopback0——不绑 VLAN、永活（至少一个 VLAN 活动时）、RIP/OSPF 自动通告（BGP 不会），作 RP/sFlow agent/RADIUS 源/NTP/BGP peering/OSPF router-id/NMS 识别；⑤静态路由——默认优先于动态路由，metric 调优先级，可做主备默认路由；ip service source-ip 统一指定各 IP 服务的源接口。
  conditions: 静态路由关联接口须 up（p363）
  tags: [structure, dhcp, udp-relay, loopback0, static-route]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-26）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 连接远程实验室与客户端操作 | 有 | f02, f03 | R-Lab 结构 + 客户端操作序列 |
| task-02 | 多方式登录交换机 | 有 | f05, f07 | AAA 框架 + 五通道接入全景 |
| task-03 | 用户与外部认证服务器管理 | 有 | f06 | userTable/密码策略/服务器声明结构 |
| task-04 | 加固管理面 | 有 | f07 | ASA 限源/禁服务/会话/SSH 收敛清单 |
| task-05 | WebView 远程管理 | 有 | f08 | 七大配置组与操作动线 |
| task-06 | Lightning Config 开局 | 有 | f09, f10 | 七步流 + 两型示例拓扑 |
| task-07 | 闪存目录与配置生命周期 | 有 | f11, f12, f13 | 三层模型/状态机/备份恢复 |
| task-08 | Virtual Chassis | 有 | f14-f18 | 规模矩阵/选举/分裂防护/ISSU/配置五步 |
| task-09 | VLAN 与 802.1Q | 有 | f19, f20 | 三入口结构 + UNP 分类优先级 |
| task-10 | VLAN 间路由与 IP 接口 | 有 | f21, f37 | 绑定模型 + DHCP/Loopback/静态路由 |
| task-11 | OST 使用 | 有 | f22 | 两代架构与功能五块 |
| task-12 | 诊断八件套 | 有 | f23 | 八件套结构 |
| task-13 | 链路聚合 | 有 | f24 | 静态/LACP + hash 矩阵 |
| task-14 | STP | 有 | f25 | 模式/协议/成本/保护 |
| task-15 | DHL | 有 | f26 | 会话/映射/MAC flushing 结构 |
| task-16 | DHCP Client/Relay | 有 | f37 | 五基础件覆盖 |
| task-17 | VRRP | 有 | f35 | 结构与跟踪策略 |
| task-18 | QoS | 有 | f34 | 队列模型 + 策略引擎 |
| task-19 | ACL 与用户口安全 | 有 | f36 | 条件分层 + 保留组 |
| task-20 | Access Guardian | 有 | f27 | 决策流 + 配置五层 |
| task-21 | LLDP/LLDP-MED | 有 | f28 | 信息模型 + 语音 VLAN 流 |
| task-22 | PoE | 有 | f29 | 等级表/优先级/特殊特性 |
| task-23 | 软件升级 | 有 | f30 | 三通道与版本线 |
| task-24 | Auto-Fabric | 有 | f31 | 七步链 + LBD |
| task-25 | Fleet Supervision | 有 | f32 | 四块能力 + 开通三路 |
| task-26 | OST 2.0 安装 | 有 | f33 | 组件依赖链 |

**26/26 全部有框架类条目覆盖。** 数值细节（会话上限逐格、PoE 功率表、路径成本表、hash 默认逐型号等）属 principle.md 口径；实验操作步骤属 case.md；本文件只保留结构锚点、机制图与菜单路径。生产化边界提示：型号相关规格（VC 上限全矩阵、镜像会话数、PoE 预算）以 Specification Guide/datasheet 为准（各条目 conditions 已标注）。
