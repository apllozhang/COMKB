# 原则/清单/规则/公式/数值口径候选 — OmniSwitch LAN Access Switching (DT00XTE215EN Ed23)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、账号、POD 规则）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: 出厂默认账号 admin/switch；本地库上限 64 用户；首登强制改密的版本线
  type: metric
  source_pages: p70, p71
  source_chapter: SWITCH USER ACCOUNT / PASSWORD FOR ADMIN
  source_quote: |
    "** Default login name and password Login : admin Password : switch ... By default : 2 users 'admin and default' ... * Up to 64 users can be configured in the local switch database" (p70)
    "From 8.10R03 a warning message will be displayed urging for the default password to be changed when logging in using the 'admin' account. In 8.10R4 changing the default password is mandatory. • From 8.10R04 it is mandatory to change the password at first login" (p71)
  summary: |
    三组数字/规则：①出厂默认登录 admin/switch（双用户 admin 与 default）；②本地用户库上限 64 个；③版本线——8.10R03 起登录警告、8.10R4 强制改默认密码、8.10R04 强制首登改密。升级存量设备后第一件事核查默认口令是否已换。
  conditions: userTable 文件位于 flash/system（p70）
  tags: [metric, users, security, version]

- id: p02
  title: 密码策略可配项全表（policy/size/expiration/history/min-age/refresh）
  type: checklist
  source_pages: p72, p74
  source_chapter: USER CREATION / SECURITY
  source_quote: |
    "-> user password-policy cannot-contain-username cannot-contain-consecutive-characters min-uppercase min-lowercase min-digit min-nonalpha" (p72)
    "-> user password-size min ... -> user password-expiration ... -> user password-history ... -> user password-min-age" (p72)
    "This enhance allows and administrator to enforce a password refresh for a specific user or all users upon their next login. • user password-refresh • user <string> password-refresh" (p74)
  summary: |
    密码治理清单：①复杂度策略四要素可配——禁含用户名、禁连续字符、大写/小写/数字/非字母最少个数（min-uppercase/min-lowercase/min-digit/min-nonalpha）；②生命周期四项——最小长度、过期时间、历史复用限制、最短使用年龄；③强制刷新——user password-refresh（全体）或 user <名> password-refresh（单个）在下次登录强制改密（IEC62443-3-3 Level 2 Ready in 8.10R3 配套）；④创建用户两种方式——明文密码（sha+des 混合）或 password-prompt 交互输入。
  conditions: 具体默认值原书未给数值，配置时逐项显式设定
  tags: [checklist, security, password]

- id: p03
  title: RADIUS 服务器声明与审计命令；RADIUS 建议启用 TLS；命令日志开关
  type: rule
  source_pages: p73
  source_chapter: EXTERNAL SERVER DECLARATION
  source_quote: |
    "-> aaa radius-server rad1 host 192.168.100.102 key alcatel ... -> aaa radius-server rad1 host 192.168.100.102 vrf-name Mgmt key alcatel tls" (p73)
    "For RADIUS server, it is recommended to activate TLS option when possible (enabling SSL on the server side is needed then)" (p73)
    "-> aaa accounting session rad1 rad2 local ... -> command-log enable" (p73)
  summary: |
    三条规则：①RADIUS 服务器声明 aaa radius-server <名> host <IP> key <密钥>，可加 vrf-name 限定管理 VRF；②官方建议尽可能启用 TLS 选项（服务器侧要先开 SSL）；③ASA 会话记账 aaa accounting session <srv1> <srv2> local，命令审计 command-log enable。
  conditions: RADIUS 服务器默认参数（重试/超时/端口）见 p26（Access Guardian，p472 条目 p14）
  tags: [rule, radius, aaa, security]

- id: p04
  title: 证书工具两件——convert-cert 与 check-revocation（CRL/OCSP）
  type: rule
  source_pages: p74
  source_chapter: SECURITY (IEC 62443)
  source_quote: |
    "This enhancement provides the ability to convert certificates in DER, PEM, PKCS#12, and P7B to PEM format. • aaa certificate convert-cert" (p74)
    "This enhance provides the ability to check a certificate's revocation status using either CRL (Certificate Revocation List) or OCSP (Online Certificate Status Protocol). Currently supported for Radius and Syslog over TLS. • ssl pki check-revocation" (p74)
  summary: |
    两条规则：①aaa certificate convert-cert 把 DER/PEM/PKCS#12/P7B 证书转成 PEM；②ssl pki check-revocation 启用吊销检查（CRL 或 OCSP），当前仅支持 RADIUS 与 Syslog over TLS 两类连接。
  conditions: IEC 62443-3-3 Level 2 Ready in 8.10R3（p74）
  tags: [rule, security, certificates]

- id: p05
  title: Console 端口参数——速率分代（9600/115200）、线序默认 DCE、admin-only 与禁用的 RMA 风险
  type: metric
  source_pages: p75-77, p523-527
  source_chapter: ACCESS VIA THE CONSOLE PORT / SECURING CONSOLE PORT ACCESS / CONSOLE CONNECTIONS
  source_quote: |
    "Default settings Speed (baud) : 115200 Parity: None Stop bits : 1 Flow control : none Note: the configuration for the latest generation 6900, 6870 and 6860N switches is different" (p76)
    "* By default, DCE console connection * Except for 6900 V72/C32 (cross cable)" (p75)
    "-> aaa console admin-only enable -> aaa session console disable ... you won't be able to manage anymore your switch ! (RMA necessary in this case)" (p77)
    "OS6900 T20/T40/X20/X40 @ 9600 Baud Rate ... OS6900 V72/C32/X48C6/T48C6/V48C8 @ 115200 Baud Rate ... OS6860/OS6860E @ 9600 ... OS6860N/OS6870 @ 115200 ... Legacy/New Switches @ 9600 Baud Rate 6350 6360 6450 6465 6560 6570M 6850 6855 6865 9900 10K" (p523-527)
  summary: |
    Console 参数逐格：①最新一代 6900/6870/6860N 为 115200，其余（Legacy 6350/6360/6450/6465/6560/6570M/6850/6855/6865/9900/10K）9600；6900 内部再分——T20/T40/X20/X40 与 X72/Q32 均 9600，V72/C32/X48C6/T48C6/V48C8 为 115200；②校验 None/停止位 1/流控 none；③线序默认 DCE 直连，例外 6900 V72/C32 用交叉线；④console 可限 admin-only（aaa console admin-only enable）或整体禁用（aaa session console disable）——全部管理通道同失时无法再管理，只能 RMA。
  conditions: 物理口形态 RJ45/USB-RS232/Micro-USB 因型号而异（p75）
  tags: [metric, console, rma]

- id: p06
  title: EMP 口规则与 USB-to-Ethernet dongle 等效条件
  type: rule
  source_pages: p78-79
  source_chapter: ACCESS VIA THE EMP PORT / APPLYING AN ACL ON THE EMP PORT
  source_quote: |
    "Bypass the network interface modules (NI) • Remotely manage the switch directly via the CMM (not available in all switches) ... ip interface master emp address 172.25.167.203 mask 255.255.255.224" (p78)
    "USB Ethernet Dongle (8.9.R1) ... • USB 3.0 version dongles are supported on OS6360/6465/6560 models. • USB 2.0 version dongles are supported on all models. • All the chassis of a VC should have a USB-to-Ethernet dongle for proper VC EMP functionality." (p78)
    "Only for IP condition in PBR (Policy Based Routing) policy rule. ... Policy condition with Source IPv4 and Destination IPv4 addresses ... Only a single empacl policy list with multiple policy rules is supported." (p79)
  summary: |
    EMP 规则四条：①EMP 旁路 NI 直连 CMM 管理，非全系标配（6900/6870/6860N 有，6560/6360 无）；②无 EMP 口机型从 8.9.R1 起可用 USB-Ethernet dongle 等效（USB 3.0 仅 6360/6465/6560 支持，USB 2.0 全系），EMP 相关命令全部适用；③VC 场景所有成员机箱都必须插 dongle 才有完整 VC EMP 功能；④EMP 口可施加 empacl 策略：仅支持源/目的 IPv4 的 PBR 条件与动作，全机仅一条 empacl 策略列表（可含多规则）。
  conditions: EMP 地址示例 172.25.167.203/27 为配置示例
  tags: [rule, emp, dongle]

- id: p07
  title: 管理会话并发上限表（Telnet 6 / FTP 4 / SSH 8 / HTTP 4 / 总 20 / SNMP 50）
  type: metric
  source_pages: p80
  source_chapter: TELNET, SSH, HTTP, SNMP Session specification
  source_quote: |
    "Telnet (V4 or V6) 6 ... FTP (V4 or V6) 4 ... SSH + SFTP (V4 or V6 secure session) 8 ... HTTP 4 ... Total sessions (Secure Shell, Telnet, FTP, HTTP, and console) 20 ... SNMP 50" (p80)
    "Secure Shell public key authentication Password DSA/RSA/ECSDA Public Key ... RFCs Supported for SSHv2 RFC 4253 – SSH Transport Layer Protocol RFC 4418 – UMAC: message Authentication Code Universal Hashing" (p80)
  summary: |
    逐格转写（摘自 OmniSwitch AOS Release 8 Specifications Guide）：Telnet 6、FTP 4、SSH+SFTP 8、HTTP 4、五类总会话 20、SNMP 50。SSH 公钥认证支持密码与 DSA/RSA/ECDSA 公钥（第二行表格仅列 DSA/RSA，以 Specification Guide 为准）；SSHv2 依据 RFC 4253 与 RFC 4418（UMAC）。
  conditions: 摘自 Specifications Guide，随版本更新以原Guide为准
  tags: [metric, sessions, capacity]

- id: p08
  title: WebView 默认态与服务开关口径——默认 enabled 但不允许认证；R8 强制 SSL
  type: rule
  source_pages: p82, p97
  source_chapter: ACCESS VIA WEBVIEW / Setting up the HTTP Session
  source_quote: |
    "webview server enable • Enables the WebView Application (default= enabled) ... webview force-ssl enable • Forces SSL connection between browser and switch (default=enabled) ... aaa authentication http local • Checks the local database for HTTP authentication" (p82)
    "By default, the WebView is enabled on the OmniSwitch, but you are not allowed to authenticate. ... It is possible to disable it with the command: no aaa authentication http" (p97)
    "SSL is forced by default in Release 8. It means that you can't connect with plain HTTP on R8 OmniSwitches, you will be automatically redirected to an HTTPS connection." (p97)
  summary: |
    三条口径：①WebView 服务默认 enabled，且 force-ssl 默认 enabled（HTTP 端口 80/HTTPS 443 可改）；②"服务开着"不等于"能登录"——HTTP 认证默认不允许，需 aaa authentication http local；禁用即 no aaa authentication http；③R8 强制 SSL：明文 HTTP 连接会被自动重定向到 HTTPS。
  conditions: WebView 视图限单台交换机（p81）
  tags: [rule, webview, security]

- id: p09
  title: 管理面收缩四清单——ASA 限源 64 地址、禁不安全服务、会话参数、SSH 强加密
  type: checklist
  source_pages: p85-88
  source_chapter: RESTRICT MANAGEMENT ACCESS / DISABLE INSECURE MANAGEMENT PORTS / LOGIN PARAMETERS / SECURING SSH
  source_quote: |
    "-> aaa switch-access management stations admin-state enable -> aaa switch-access management stations 192.168.1.1 -> aaa switch-access management stations 172.16.1.1 255.255.255.224 ... (up to 64 addresses allowed)" (p85)
    "-> ip service all admin-state disable -> ip service telnet/http/ftp/snmp/radius/ntp admin-state disable" (p86)
    "-> session login-attempt 5 -> session login-timeout 20 -> ssh login-grace-time 200 -> session cli/ftp/http timeout 10 -> session ftp/ssh/telnet/http session-limit 2" (p87)
    "-> ssh strong-ciphers enable ... -> ssh strong-hmacs enable ... hmac-sha2-256, hmac-sha2-512 ... -> ssh enforce-pubkey-auth" (p88)
  summary: |
    加固四清单：①ASA 限源——启用后仅清单内地址可管理（上限 64 个，可带掩码）；②禁服务——ip service 按服务或 all 关闭（telnet/http/ftp/snmp/radius/ntp…）；③会话参数——login-attempt（失败尝试次数）、login-timeout（登录限时秒）、ssh login-grace-time（未完成 SSH 会话超时秒）、session cli/ftp/http timeout（空闲超时分钟）、session-limit（各协议并发上限）；④SSH——strong-ciphers（强制 AES256 级）、strong-hmacs（强制 hmac-sha2-256/512）、enforce-pubkey-auth（强制公钥认证免密）；另配 session banner（CLI/FTP/Web 横幅，默认目录 /flash/switch/）与 MFA（Google Authenticator/Duo 方案见 Application Note，p89）。
  conditions: PKA 需先按 Switch Management Guide 生成公私钥对（p88）
  tags: [checklist, hardening, ssh]

- id: p10
  title: Lightning Config 数值口径——192.168.0.1/端口 1 DHCP/5 分钟开局/密码四要素避开 ! $
  type: metric
  source_pages: p104, p106, p113, p115, p116
  source_chapter: OMNISWITCH LIGHTNING CONFIG
  source_quote: |
    "Port 1 DHCP Client Default IP interface VLAN1 192.168.0.1" (p104)
    "• Fast Setup: Go from unboxing to passing traffic in less than 5 minutes per switch. • Minimal Training: Learn to use Lightning Config in under 15 minutes. • Works with Any ALE 6360 Switch" (p106)
    "The laptop will be assigned an IP of 192.168.0.200/24 via the DHCP server on the ALE switch. ... Enter https://192.168.0.1/ • You must use https" (p113)
    "• At least 8 characters • 1 uppercase letter • 1 lowercase letter • 1 digit • 1 special character (but avoid using ! or $)." (p116)
  summary: |
    数值口径：①交换机端口 1 为 DHCP Client，默认 IP 接口 VLAN1 192.168.0.1；笔记本经交换机 DHCP 得 192.168.0.200/24；②开局效率口径——每台 <5 分钟通流量、学习成本 <15 分钟、适用任意 ALE 6360 交换机；③上电后约等 3 分钟看绿灯再开浏览器；④admin 新密码要求——至少 8 字符、各含 1 大写/1 小写/1 数字/1 特殊字符，且建议避开 ! 与 $ 两个字符；⑤模板文件扩展名 .json（p120）。
  conditions: 5 分钟/15 分钟为厂商宣传口径；必须 https 访问
  tags: [metric, lightning-config, onboarding]

- id: p11
  title: 启动目录判定规则——内容相同回 running、不同回 certified、reload all 强制 certified
  type: rule
  source_pages: p142
  source_chapter: Booting behavior in Release 8
  source_quote: |
    "The switch will reboot from certified directory if contents (images and vcboot.cfg) are different from the running directory (which can be the working directory, or a user-defined directory). ­ If contents are the same, the switch will reboot from the running directory" (p142)
    "IF THE OMNISWITCH IS REBOOTED WITH THE 'RELOAD ALL' COMMAND, IT WILL REBOOT FROM THE CERTIFIED DIRECTORY, NO MATTER WHAT THE CONTENT OF THE RUNNING DIRECTORY IS" (p142)
    "If the running directory is the certified directory, you will not be able to save any changes made to the running directory." (p142)
  summary: |
    三条启动规则：①冷启动默认——running 目录（working 或用户目录）与 certified 内容不同则从 certified 启动；相同则从 running 启动；②reload all 特例——无论内容是否相同一律从 certified 启动（强制回滚语义）；③running=certified 时禁止保存，重启后配置改动全部丢失。
  conditions: 判定对象为镜像文件与 vcboot.cfg 内容（p142）
  tags: [rule, boot, rollback, directories]

- id: p12
  title: show running-directory 三字段判读口径（Running configuration / Certify-Restore / Synchronization）
  type: rule
  source_pages: p142-144, p146-147
  source_chapter: Determining from which directory the switch was loaded
  source_quote: |
    "Running configuration : WORKING, Certify/Restore Status : CERTIFIED ... Running Configuration : SYNCHRONIZED" (p142)
    "Running Configuration : NOT SYNCHRONIZED > the running configuration does not match the configuration of the working directory." (p143)
    "Certify/Restore Status: CERTIFY NEEDED > the WORKING directory does not match the CERTIFIED directory." (p144)
    "Running configuration : lab ... Certify/Restore Status : CERTIFIED > the running directory ('lab') matches the CERTIFIED directory." (p147)
  summary: |
    判读口径三字段：①Running configuration——当前启动目录名（WORKING/CERTIFIED/用户目录名）；②Certify/Restore Status——CERTIFIED=running 目录与 certified 内容一致，CERTIFY NEEDED=不一致（已 write memory 但未认证）；③Synchronization Status——SYNCHRONIZED=RAM 与 running 目录一致，NOT SYNCHRONIZED=RAM 有未保存改动。排障三问（从哪启动/是否已认证/是否已保存）全靠这条命令。
  conditions: 改动未保存时重启将回滚（p143 Warning：VLAN 2/3/99 丢失示例）
  tags: [rule, rollback, troubleshooting]

- id: p13
  title: 配置备份 .tar 口径——三文件/路径/10 个上限；USB 备份目录结构
  type: metric
  source_pages: p136-137, p148-149
  source_chapter: CONFIGURATION BACKUP & RESTORE / USB Backup and Restore
  source_quote: |
    "Backup of the session banner, userTable* and vcboot.cfg files • The tar file name is 'configuration_backup.tar' and will be placed in '/flash/config-backup-recovery' folder • Up to 10 .tar files can be stored" (p136)
    "usb backup admin-state {enable | disable} [key <> | hash-key<>] ... usb auto-copy <enable | disable> copy-config <enable| disable> from <directory-path> [key <> | hash-key<>]" (p137)
    "the images and configuration from certified and running directories are copied into /uflash/6560/certified and /uflash/6560/running directories" (p148)
  summary: |
    备份口径：①配置备份打包三文件（会话横幅、userTable、vcboot.cfg）为 configuration_backup.tar，存 /flash/config-backup-recovery，上限 10 个 tar；restore 自动选取该文件解出三件；②USB 备份启用后 write memory/copy running-certified/flash-synchro 自动同步 /flash/<目录> 到 /uflash/<型号>/<目录>（示例 /uflash/6560/certified 与 running，含 Nos.img/vcboot.cfg/vcsetup.cfg）；③启用时给 key 则备份加密、恢复时解密；usb auto-copy 支持从 U 盘目录复制恢复。
  conditions: 拔 U 盘前必须 usb disable（p148 WARNING）
  tags: [metric, backup, usb]

- id: p14
  title: RADIUS 服务器默认参数表（retries 3 / timeout 2s / auth 1812 / acct 1813 / 无 SSL）与 MAC 会话 12 小时
  type: metric
  source_pages: p472
  source_chapter: AUTHENTICATION SERVER CONFIGURATION
  source_quote: |
    "Parameters Default ... retries 3 ... seconds 2 ... auth_port 1812 ... acct_port 1813 ... ssl | no ssl No ssl" (p472)
    "Enable the MAC authentication session timer to determine the amount of time the user session remains active after a successful login (the default time is set to 12 hours). ... -> aaa mac session-timeout enable" (p472)
  summary: |
    RADIUS 缺省逐格：重试 3 次、超时 2 秒、认证端口 1812、计费端口 1813、SSL 默认关闭。MAC 认证会话计时器默认 12 小时（aaa mac session-timeout enable 启用计时）。
  conditions: 服务器声明语法含 vrf-name/salt/retransmit/timeout 等可选项（p472 完整命令行）
  tags: [metric, radius, aaa]

- id: p15
  title: VC 选举四级优先序与 10 分钟运行时长门槛；优先级范围 0-255
  type: rule
  source_pages: p156, p167
  source_chapter: ROLES AND ELECTIONS / VIRTUAL CHASSIS CONFIGURATION
  source_quote: |
    "Master/Slave election based on virtual chassis protocol (ISIS-VC) Highest chassis priority value Longest chassis uptime (if difference in uptime >10 mn) Smallest Chassis ID value Smallest chassis MAC address" (p156)
    "Assign a Chassis ID Must be different for each switch belonging to the Virtual Chassis ... Define a Priority Between 0 to 255, switch with the highest priority is elected Master" (p167)
  summary: |
    选举规则：①四级依次比较——最高 chassis 优先级 → 最长运行时间（差距须 >10 分钟才参与比较）→ 最小 Chassis ID → 最小 MAC；②Chassis ID 全 VC 唯一、Group ID 全 VC 相同；③优先级取值 0-255，值大者当选 master；④优先级与 chassis-id 修改都必须 reload 才生效（p175-176 Notes）。
  conditions: slave 更新镜像与配置后需重启（p156）
  tags: [rule, virtual-chassis, election]

- id: p16
  title: VC 一致性核查口径——show virtual-chassis consistency 必检项
  type: checklist
  source_pages: p180
  source_chapter: Virtual Chassis-6360 (How-To)
  source_quote: |
    "sw5 (6360-A) -> show virtual-chassis consistency Legend: * - denotes mandatory consistency which will affect chassis status ... licenses-info - A: Advanced; B: Data Center; ... Chas* ID Status Chas Type* Group* Hello Interv Control Vlan* Oper Control Vlan License* ... 1 1 OK OS6360 1 15 4094 4094 A ... 2 2 OK OS6360 1 15 4094 4094 A" (p180)
    "The two chassis in the same Virtual-Chassis group must maintain identical configuration and operational parameters." (p180)
  summary: |
    一致性核查清单（带 * 为影响 chassis 状态的强制项）：Chassis ID、Chassis Type（型号必须同族，实验两台均 OS6360）、Group（同组须一致，实验均 1）、Hello Interval（实验 15）、Control Vlan（4094）、License（A=Advanced/B=Data Center，两台须同级）。任一强制项不一致会影响 chassis 状态。
  conditions: 实验 Hello 15/Control VLAN 4094 为实验口径，实际以配置为准
  tags: [checklist, virtual-chassis, consistency]

- id: p17
  title: VC 分裂防护取址序与行为口径（RCD IP 优先级 / slave 关用户口 / VFL 恢复重启回归）
  type: rule
  source_pages: p160-161
  source_chapter: VIRTUAL CHASSIS - SPLIT CHASSIS
  source_quote: |
    "RCD use the following IP addresses in order of preference 1. CMM IP address stored in NVRAM (if configured) 2. Chassis EMP IP address" (p160)
    "The former Slave chassis will shutdown all its front-panel user ports to prevent duplicate IP and chassis MAC addresses in the network. The Slave's chassis status will be modified from Running to Split-Topology" (p160)
    "If the VFL comes back up, the former Slave chassis will reboot and rejoin the virtual chassis topology assuming its Slave role again" (p160)
    "Every VC member switch recommended to have one port as part of the VCSP LAG to the helper device" (p161)
  summary: |
    分裂防护口径：①RCD 源地址取序——NVRAM 中 CMM 地址优先，其次机箱 EMP 地址；②检出分裂后原 slave 关闭全部前面板用户口、状态转 Split-Topology（伪 master 不可用标记）；③VFL 恢复后原 slave 重启重新加入并回 slave 角色；④带内 VCSP 需上/下游 helper 交换机，VC 每成员建议一个口加入 VCSP LAG（virtual-chassis split-protection linkagg；helper 侧用 split-protection helper 命令），保护模式下 master 保留、除 VFL 与 LAG 外接口 shutdown。
  conditions: RCD 支持平台 OS6870/OS6860E/N/OS6900/OS9900；VCSP 支持平台表见 p161
  tags: [rule, virtual-chassis, split, rcd, vcsp]

- id: p18
  title: STP 收敛与默认值口径——三协议收敛时间/默认 per-VLAN/默认优先级 32768/Max Age 20
  type: metric
  source_pages: p300, p302, p316, p315
  source_chapter: STP REMINDER
  source_quote: |
    "STP (802.1d): Convergence time : 50 secs • RSTP (802.1w): Convergence time : < 1 sec • MSTP (802.1s): < 1 sec" (p300)
    "flat (single STP instance per switch) • per-VLAN (single STP instance per VLAN) (By default on OmniSwitch)" (p300)
    "By default, the bridge priority is 32768 (0x8000). Since all priorities are identical by default, the switch with the lowest MAC address is selected as the root bridge" (p316)
    "Max Age = 20, Forward Delay = 15, Hello Time = 2" (p315, show 输出)
  summary: |
    STP 数值口径：①收敛——802.1d 50 秒、802.1w/802.1s <1 秒；②默认模式 per-VLAN（1x1，每 VLAN 一实例）；③默认桥优先级 32768（0x8000），全默认时最小 MAC 当根桥；④定时器出厂值 Max Age 20s / Forward Delay 15s / Hello 2s；⑤实验示例：改优先级 20000（0x4E20）让指定交换机当 VLAN 20/30 根桥实现 1x1 负载分担。
  conditions: 路径成本与优先级取值范围见 p19（p20 条目）
  tags: [metric, stp, rstp]

- id: p19
  title: STP 路径成本两套表与优先级/成本取值范围；path-cost-mode 语义
  type: metric
  source_pages: p301, p307, p309
  source_chapter: STP REMINDER / STP CONFIGURATION
  source_quote: |
    "Link Speed IEEE Recom. Value – 16 bit 10 Mbps 100 100 Mbps 19 1 Gbps 4 10 Gbps 2 ... 802.1s 32-bit Port Path Cost PPC 10 Mbps 2,000,000 100 Mbps 200,000 1 Gbps 20,000 10 Gbps 2,000" (p301)
    "The valid range for the bridge priority is 0–65535. The valid range for the port priority is 0–15. If MSTP is the active flat mode protocol, enter a value that is a multiple of 4096" (p307)
    "Path cost 0 -> 65535 for 16-bit 0 –> 200000000 for 32-bit - Default:0" (p307)
    "spantree path-cost-mode {auto | 32bit} • 16-bit when STP/RSTP protocol is active • 32-bit when MSTP protocol is active • 32-bit regardless of which protocol is active" (p309)
  summary: |
    逐格转写：①16 位成本（STP/RSTP）——10M=100、100M=19、1G=4、10G=2；②32 位成本（MSTP）——2,000,000 / 200,000 / 20,000 / 2,000；③桥优先级 0-65535、端口优先级 0-15、MSTP 模式下优先级须 4096 倍数；④路径成本范围 16 位 0-65535、32 位 0-200,000,000；⑤path-cost-mode：auto=16 位随 STP/RSTP、32 位随 MSTP；32bit=无论何协议一律 32 位。
  conditions: IEEE 推荐值，各型号支持集查 Specification Guide（p301）
  tags: [metric, stp, path-cost]

- id: p20
  title: DHL 规格——1 会话 2 链路/端口类型限制/pre-emption 0-600 秒默认 30 秒/MAC 刷新三选
  type: metric
  source_pages: p326-328, p337, p341, p344
  source_chapter: DUAL-HOME LINK REMINDER / SPECIFICATIONS / TIMERS & MAC-FLUSHING
  source_quote: |
    "Only one session per switch is allowed. • Each session has only two links (linkA and linkB). ... The same port or link aggregate is not configurable as both linkA or linkB. • DHL is not supported on mobile, 802.1x-enabled, GVRP, or UNI ports" (p327)
    "• Pre-Emption timer • Amount of time to wait before a failed link that has recovered can resume servicing VLANs • 0 to 600 seconds" (p328)
    "Spanning Tree is automatically disabled on DHL ports" (p328/p341)
    "when the failed link comes back up, DHL waits a configurable amount of time (default: 30 secs) before the link resumes forwarding of its assigned VLAN traffic." (p344)
    "DHL linkA and linkB must belong to the same default VLAN." (p337)
  summary: |
    DHL 数值口径：①每交换机 1 会话、每会话 2 链路（LinkA/LinkB，物理口或 linkagg，不可一口两用）；②不支持 mobile/802.1x-enabled/GVRP/UNI 端口；③pre-emption 定时器 0-600 秒，实验 show 输出默认 30 秒（故障链路恢复后等 30 秒才收回 VLAN）；④DHL 端口上 STP 自动禁用；⑤LinkA/LinkB 必须同属一个默认 VLAN；⑥MAC 刷新三选——RAW Flooding（广播源 MAC 帧刷表）/MVRP Enhanced（new 标志 join）/None（默认，保留 stale 表项）。
  conditions: 方案对比——STP 牺牲一半带宽；LACP 与 DHL 全带宽；DHL 无交换机级冗余（p330）
  tags: [metric, dhl, timer, redundancy]

- id: p21
  title: DHCP 中继参数口径——全局/接口互斥、max hops 16、Opt82 Base MAC、PXE 默认关
  type: metric
  source_pages: p353-355
  source_chapter: DHCP RELAY
  source_quote: |
    "Two types of DHCP relay agents: global and per-interface. ... They are mutually exclusive" (p353)
    "DHCP Relay Admin Status = Enable, Forward Delay(seconds) = 0, Max number of hops = 16, Relay Agent Information = Disabled, Relay Agent Information Policy = Drop, DHCP Relay Opt82 Format = Base MAC, ... PXE support = Disabled, Relay Mode = Global, Bootup Option = Disable" (p354)
    "-> ip dhcp relay per-interface-mode ... -> ip dhcp relay interface if_name destination ip_address" (p355)
  summary: |
    中继口径：①全局型（destination 全局地址）与接口型（per-interface-mode + interface 指定目的）互斥；②默认参数——Forward Delay 0 秒、Max hops 16、Relay Agent Information 关（策略 Drop）、Opt82 格式 Base MAC、PXE 支持关、Bootup Option 关；③统计命令 show ip dhcp relay statistics 按服务器分桶计数。
  conditions: 接口型仅转发该接口所绑 VLAN 发起的 DHCP 包（p353）
  tags: [metric, dhcp-relay]

- id: p22
  title: DHCP Client 选项语义（Option 1/3/51/58/59/60）
  type: rule
  source_pages: p350-351
  source_chapter: DHCP CLIENT IP INTERFACE
  source_quote: |
    "The DHCP Client interface supports the release and renew functionality according to RFC -2131. • The Option-60 string can be configured on the OmniSwitch and sent as part of the DHCP discover/request packet." (p350)
    "• The IP address and the subnet mask (DHCP Option-1) are assigned ... • A default static route is created according to DHCP Option-3 (Router IP Address) • The lease is periodically renewed and rebound according to the renew time (DHCP Option-58) and rebind time (DHCP Option-59) ... • If the lease cannot be renewed within the lease time (DHCP Option-51) ... the IP address is released" (p351)
  summary: |
    选项语义：Option-1=IP 与掩码落地；Option-3=路由器地址生成默认静态路由；Option-51=租期（到期无法续租则释放）；Option-58/59=续租/重绑时间点；Option-60=可配字符串随 discover/request 发出（示例输出 OmniSwitch-OS6860）。DHCP Client 地址在 VLAN 多地址时作主地址；接口支持 RFC 2131 的 release/renew。
  conditions: 每 VRF 每 VLAN 单个 DHCP Client 接口（p350 "configurable on any one VLAN in any VRF instance"）
  tags: [rule, dhcp-client]

- id: p23
  title: VRRP 数值口径——组播 224.0.0.18/虚拟 MAC 模板/默认优先级 100/改优先级先 disable/同优先级最低 router ID 胜
  type: metric
  source_pages: p375, p380, p387, p390
  source_chapter: VRRP REMINDER / CONFIGURATION / How-To
  source_quote: |
    "Multicast - 224.0.0.18 Virtual MAC address: 00-00-5E-00-01-{VRID}" (p375)
    "RFCs Supported • RFC 2338 – Virtual Router Redundancy Protocol • RFC 2787 – Definitions of Managed Objects for the Virtual" (p375)
    "ip vrrp 1 interface int_20 priority 100 preempt interval 100" (p380)
    "THE VRRP INSTANCE MUST BE DISABLED BEFORE CHANGING THE PRIORITY" (p390)
    "Version = V2 ... Virtual MAC = 00-00-5E-00-01-01 ... Since all priorities are equal, the lowest router ID is the selection criteria." (p387)
  summary: |
    VRRP 口径：①控制组播 224.0.0.18，虚拟 MAC = 00-00-5E-00-01-{VRID}（VRID 1 即 …-01-01）；②依据 RFC 2338/2787，实验输出 Version=V2；③默认优先级 100、默认允许抢占、通告间隔 100（centiseconds）；④改优先级必须先 disable 实例再改再 enable；⑤全部同优先级时最低 router ID 当 master；⑥跟踪策略五类（ADDRESS/IPV4-INTERFACE/IPV6-INTERFACE/PORT/VLAN），track 定义的 priority 为故障时的降级量。
  conditions: 主备两侧须至少两个虚拟路由器（p379）
  tags: [metric, vrrp]

- id: p24
  title: QoS 全局与端口口径——默认启用/默认 disposition accept/默认 802.1p 0/默认端口不信任/qos apply 生效规则
  type: rule
  source_pages: p396, p404, p423, p424, p434
  source_chapter: QOS CONFIGURATION / CONFIGURING PORT DEFAULT
  source_quote: |
    "qos enable/disable ... By default, QoS is enabled on the switch." (p396)
    "Whether the flow matching the rule should be accepted or Denied ... disposition Accept" (p404)
    "By default, the port default values for 802.1p and ToS/DSCP are 0. ... By default, switched ports are untrusted" (p423)
    "the global setting is active immediately; however, modifying a port configuration requires qos apply to activate the change" (p424)
    "* By default, flows that do not match any policies are accepted on the switch" (p434)
  summary: |
    五条口径：①QoS 默认启用（qos enable）；②未匹配任何策略的流默认接受（disposition 默认 Accept）；③端口默认 802.1p 与 ToS/DSCP 均为 0；④交换端口默认不信任（untrusted）——未打标流量贴端口默认值，tagged 流量在不信任口被改写为默认值、在信任口保留原值；⑤生效规则——全局设置立即生效，端口配置与策略改动必须 qos apply；配套命令 qos reset（回默认）/revert（删 pending）/flush（清配置）。
  conditions: qos flush 后再 apply 是实验前的标准清场动作（p422/p449）
  tags: [rule, qos, trusted]

- id: p25
  title: auto-QoS 话机 MAC 组全表与优先级 5
  type: metric
  source_pages: p410
  source_chapter: AUTOMATIC PRIORITIZATION FOR IP PHONE TRAFFIC
  source_quote: |
    "MAC Address Range Description 00:80:9F:00:00:00 to 00:80:9F:FF:FF:FF Enterprise IP Phones Range 78:81:02:00:00:00 to 78:81:02:FF:FF:FF Communications IP Phones Range 00:13:FA:00:00:00 to 00:13:FA:FF:FF:FF Lifesize IP Phones Range 48-7A-55-00-00-00 to 48-7A-55-FF-FF-FF ALE 8008 IP Phone MAC Range" (p410)
    "Mac adress = ALE Phone > Priority 5 • Non ALE Phone > Default ... On trusted and un-trusted ports ... policy mac group alaPhones 00:80:9f:00:00:00 mask ff:ff:ff:00:00:00 ... -> qos phones [priority priority_value | trusted] -> qos no phones" (p410)
  summary: |
    auto-QoS 逐格：四个 ALE 话机 MAC 段——00:80:9F::/24（Enterprise IP Phones）、78:81:02::/24（Communications IP Phones）、00:13:FA::/24（Lifesize）、48-7A-55::/24（ALE 8008）；命中即给优先级 5，非 ALE 话机走默认；该机制在信任与非信任端口都生效（交换机按 MAC 识别话机而非信任端口）；可 qos phones priority <值|trusted> 改行为，qos no phones 关闭。alaPhones MAC 组可重定义扩展。
  conditions: 功能默认启用（p410 "Enable by default on the switch"）
  tags: [metric, qos, phones]

- id: p26
  title: 用户口安全保留组口径——UserPorts 仅作用于路由流量、shutdown 清单、violation-recovery
  type: rule
  source_pages: p440-442, p453
  source_chapter: ADVANCED ACL SECURITY FEATURES / Configuring User ports Security
  source_quote: |
    "Used by default to prevent spoofed IP addresses on ports • Packets received on the port are dropped if they contain a source IP network address that does not match the IP subnet for the port ... -> policy port group UserPorts 1/1/1-24 1/2/1-24 3/1/1 4/1/1 -> qos user-port filter spoof rip ospf bgp" (p440)
    "-> qos user-port {filter | shutdown} {spoof|bgp|bpdu|rip|ospf|vrrp|dvmrp|pim|isis|dhcpserver|dns-reply}" (p440)
    "This port group does not need to be used in a condition or rule to be effective on flows and only applies to routed traffic." (p453)
    "-> interfaces violation-recovery-time <num> ... -> interfaces violation-recovery-trap {enable | disable}" (p442)
  summary: |
    保留组规则：①UserPorts 端口组反 IP 欺骗——源 IP 与端口子网不符即丢；该组无需被条件/规则引用即生效，但只作用于路由流量；②qos user-port filter|shutdown 可处理协议清单——spoof/bgp/bpdu/rip/ospf/vrrp/dvmrp/pim/isis/dhcpserver/dns-reply（shutdown 收到即关口，实验用 shutdown bpdu 防用户口环路，p453）；③port-disable 规则命中即管理性关口；④violation-recovery-time 设自动恢复定时（未配或 0 则不自动恢复），violation-recovery-trap 控制恢复时发 trap；⑤DropServices 保留组在 UserPorts 口上丢弃组内 TCP/UDP 服务（示例 135/445/137）。
  conditions: 早期 ARP 丢弃默认启用（p443）；ip directed-broadcast disable 防反射放大（p443）
  tags: [rule, security, userports]

- id: p27
  title: UNP 认证降级口径——pass-alternate / auth-server-down 60 秒 / 无 MAC 登记 Block
  type: rule
  source_pages: p466, p474, p478, p485
  source_chapter: ACCESS GUARDIAN CONFIGURATION STEPS
  source_quote: |
    "-> unp port chassis/slot/port 802.1X-authentication [pass-alternate profile_name] ... [mac-authentication pass-alternate profile_name]" (p466)
    "Users are moved to a specific profile when RADIUS server is not available. ... unp auth-server-down profile1 profile_name ... Auth Server Down Profile1 = ag_SrvDownPrf, Auth Server Down Timeout = 60 ... * When authentication server becomes reachable Users are re-authenticated" (p474)
    "@MAC Auth: as there are no MAC addresses configured on the RADIUS server, the user will be blocked from accessing the network via a MAC address authentication." (p478)
    "As there are not any MAC addresses configured on the RADIUS server, then the user is blocked from accessing the network." (p485)
  summary: |
    降级三口径：①认证通过但 RADIUS 未回 UNP 名（Filter-Id 缺失）→ 进 pass-alternate 指定的备用档案（802.1x 与 MAC 各自可配）；②RADIUS 服务器不可达 → 全体用户迁入 auth-server-down 档案，默认 60 秒重试，服务器恢复后自动重认证；③MAC 认证在服务器无该 MAC 登记时一律 Block（实验口径即如此，用户态显示 Block）。
  conditions: RADIUS 以 Filter-Id 属性回传 UNP 名（p480 Notes）
  tags: [rule, access-guardian, unp]

- id: p28
  title: LLDP 运行参数口径——默认收发双开/30 秒间隔/TTL 倍乘 4/不支持 linkagg 级
  type: metric
  source_pages: p488, p502, p504
  source_chapter: LLDP OVERVIEW / How-To
  source_quote: |
    "Enabled by default on the OmniSwitches" (p488)
    "LLDP is enabled by default in reception and transmission ... LLDP is configured at port level (or NI or chassis), but not at linkagg level." (p502)
    "LLDPDU Transmit Interval = 30 seconds, TTL Hold Multiplier = 4, Reintialization Delay = 2 seconds, Maximum Transmit Credit = 5, LLDPDUs in Fast Transmission = 4, LLDPDU Fast Transmit Interval = 1, MIB Notification Interval = 5 seconds" (p504)
  summary: |
    LLDP 口径：①默认收发双开（IEEE 802.1AB）；②配置层级为端口/槽/机箱，不支持 linkagg 级；③出厂运行参数（实验 show lldp local-system 输出）——发送间隔 30 秒、TTL 保持倍乘 4（即邻居信息存活 120 秒）、重初始化延迟 2 秒、最大发送信用 5、快速发送 4 帧×1 秒、MIB 通知间隔 5 秒；④notification enable 可对端口远端变化发 trap。
  conditions: 实验输出取自 OS6860E 8.7.98.R03 截图（p504），参数为该版本口径
  tags: [metric, lldp]

- id: p29
  title: PoE 供电等级逐格表（802.3af/at Type2/bt Type3/bt Type4）
  type: metric
  source_pages: p513
  source_chapter: POWER OVER ETHERNET
  source_quote: |
    "Power available at the PD 12.95 W 25.50 W 51 W 71 W Maximum power delivered by the EPS 15.40 W 30.0 W 60 W 100 W Maximum current Imax 350 mA 600 mA 600 mA per pair 960 mA per pair Energy Management Three power class levels (1-3) Four power class levels (1-4) Six power class levels (1-6) Eight power class levels (1-8) Supported cabling Category 3 and Category 5 Category 5 Category 5 Category 5" (p513)
  summary: |
    逐格转写：802.3af（=802.3at Type1 "PoE"）——PD 可用 12.95W、PSE 最大 15.4W、Imax 350mA、3 个功率级（1-3）、Cat3 与 Cat5；802.3at Type2（"PoE+"）——25.5W/30W/600mA/4 级/Cat5；802.3bt Type3（"4PPoE"/"PoE++"）——51W/60W/每对 600mA/6 级/Cat5；802.3bt Type4（"4PPoE"/"PoE++"）——71W/100W/每对 960mA/8 级/Cat5。
  conditions: 各型号 PoE 预算不同，查 specification guide/datasheet（p514）
  tags: [metric, poe, standards]

- id: p30
  title: PoE 管理参数口径——端口 mW/槽 W/优先级三档/delayed-start 120-600 秒/FPoE-PPoE 型号线
  type: metric
  source_pages: p510-511, p516-520
  source_chapter: POE POWER MANAGEMENT / POE MANAGEMENT
  source_quote: |
    "Fast PoE : 2X60, 6360, 6860E, 6860N, 6865, 6870 • Note: OS6360 – P10A does not support FPoE ... Perpetual PoE : 2X60, 6360, 6860E, 6860N, 6865, 6870 • Note: OS6360 – P10A does not support PPoE." (p510-511)
    "-> lanpower port 1/1/24 power 18000 ... for one port (in mW) ... -> lanpower slot 1/1 maxpower 400 ... for a slot (in W)" (p516)
    "Setting Port Priority Levels (Low, High, Critical) • Default priority level for a port is low" (p517)
    "<num> - specific delay value in seconds in multiples of 5. Value should be within 120 to 600 seconds ... • It is mandatory to do write memory to reflect this command on bootup. • Fpoe and Ppoe is not supported on enabling this feature." (p520)
  summary: |
    管理口径：①Fast PoE（上电即供）与 Perpetual PoE（重启不断电）支持 2X60/6360/6860E/6860N/6865/6870，OS6360-P10A 两者都不支持，且均需升级 FPGA/CPLD（查 release note）；②功率设置单位——端口 power 单位 mW（示例 18000），槽 maxpower 单位 W（示例 400）；③优先级三档 low（默认）/high/critical 决定断电顺序，priority-disconnect 控制预算不足时新 PD 准入；④delayed-start——延迟 120-600 秒（5 的倍数），必须 write memory 才随启动生效，启用期间与 FPoE/PPoE 互斥，需先启动 lanpower service；⑤EEE（802.3az）仅铜口 100/1000Mbps，U 型光纤口不支持（p512）。
  conditions: 实验 show lanpower 示例预算 450W/余量 393.5W（p519，实验口径）
  tags: [metric, poe, fast-poe]

- id: p31
  title: 软件版本策略口径——签名镜像 8.10R4/U-boot 密码 8.7R3 无恢复/GA-MR/合规版本源
  type: rule
  source_pages: p531-533
  source_chapter: UPGRADING SOFTWARE IMAGE
  source_quote: |
    "Starting with 8.10R4 signed images are available for the whole portfolio (already available for OS6570M since 8.9R4) • U-boot password protection is available since 8.7R3 – be careful when enabling it (no AOS recovery possible in case you lose this password)" (p531)
    "Generally, use the latest 'GA' (General Availability) or 'MR' (Maintenance) release" (p532)
    "For U-boot / ONIE and or FPGA / CPLD upgrade, it is usually done through CLI. Be careful as a failure during U-boot / ONIE or FPGA/CPLD upgrade will lead to RMA." (p533)
  summary: |
    版本策略：①签名镜像——8.10R4 起全系列（OS6570M 自 8.9R4 已有）；②U-boot 密码保护 8.7R3 起可用，启用需谨慎——密码丢失无任何恢复手段；③日常取最新 GA 或 MR 版本；④合规场景按 FIPS 140-2/JITC/Common Criteria 各自认证版本清单选（书中给出三个查询链接）；⑤U-boot/ONIE/FPGA/CPLD 升级走 CLI 且失败即 RMA。
  conditions: 升级步骤不在本教材内，按 AOS Release Notes（p533）
  tags: [rule, upgrade, version, security]

- id: p32
  title: Auto-Fabric 首启语义与 SPB 默认值（Y/N 反直觉/BVLAN 4000-4015/4×9 秒窗口）
  type: metric
  source_pages: p539, p543, p545, p547, p552
  source_chapter: AUTO-FABRIC
  source_quote: |
    "Do you want to disable auto-configurations on this switch [Y/N]? N ... N If no response or input is [N], then it is assumed to be false. Meaning to use auto-VC, RCL and auto-fabric Y If input is [Y] then auto-VC, RCL and auto-fabric are disabled" (p539)
    "RCL tries 6 times, 3 each on VLAN 1 and 127 to get DHCP and download instruction file • To cancel RCL, run command 'auto-config-abort'" (p543)
    "• Propriatery TLV used to detect the peer ... If LACP negotiation succeeds, form a link aggregation on a detected set of ports ... linkagg lacp agg 127 size 16 admin-state enable ... actor admin-key 65535" (p545)
    "BVLANs 4000-4015 mapped to ECT-IDs 1-16 respectively • Control BVLAN: 4000 • Bridge priority: 0x8000 ... If adjacencies not formed during 4 Hello intervals (4x9 sec) – NOT a part of SPB" (p547)
    "MVRP enabled globally after LACP and SPB discovery process • Spanning Tree mode switch to flat" (p552)
  summary: |
    Auto-Fabric 数值口径：①首启提示语义反直觉——输入 Y 才禁用 auto-VC/RCL/auto-fabric，N 或不答=启用；②RCL 尝试 6 次（VLAN 1 与 127 各 3 次）取 DHCP 与指令文件，auto-config-abort 可取消，末段下载到 vcboot.cfg 会重置设备；③Auto-LACP 生成的聚合口径——agg 127、size 16、actor admin-key 65535；④Auto-SPB 默认——BVLAN 4000-4015 映射 ECT-ID 1-16、控制 BVLAN 4000、桥优先级 0x8000、4 个 Hello（4×9 秒）内未成邻接即不参与 SPB；⑤Auto-MVRP 在 LACP 与 SPB 发现之后全局启用，并把 STP 切为 flat 模式。
  conditions: Auto-VC 期间 Demo License 默认启用（p540）
  tags: [metric, auto-fabric, spb, mvrp]

- id: p33
  title: OST 2.0 容量与获取口径——100 交换机/4000 设备/5 客户端/需支持合同/1.0 停更
  type: metric
  source_pages: p225, p229, p230
  source_chapter: OST 2.0 CLIENT SERVER ARCHITECTURE / ALE OMNIVISTASMART TOOL
  source_quote: |
    "Store information • 100 switches • 4000 devices • 5 clients (simultaneous) • Security: Encrypt contents of database to secure data-at-rest" (p225)
    "OST 2.0 is a Windows-based application available for download free of charge via ALE MyPortal. • The tool is available to customers with a valid OmniSwitch support contract. • The OmniSwitch Smart Tool is available for all Business Partners with a valid distributor agreement" (p229)
    "OST 1.0 will remain in Github as a community available version but no further development will be done by ALE." (p230)
  summary: |
    OST 2.0 口径：①容量——100 台交换机、4000 台设备、5 个并发客户端；②数据库静态内容加密（PostgresSQL 持久化）；③获取——MyPortal 免费下载，但客户需持有效 OmniSwitch 支持合同、BP 需有效分销协议；④OST 1.0 遗留 GitHub 社区版（spacewalkers.com/developers-center 或 github.com/ale-nsa-team/OmniVista-Smart-Tool），ALE 不再开发。
  conditions: OST 支持条件与 OmniSwitch 支持协议绑定（p229）
  tags: [metric, ost, licensing]

- id: p34
  title: 交换日志口径——1250KB/8 文件/归档 40/级别 info(6)/syslog 12 台/阈值 90%
  type: metric
  source_pages: p235-238, p245
  source_chapter: SWITCH LOGGING
  source_quote: |
    "Switch events can be logged to ... Local text file • Configurable default file size 1250 Kbytes • Multiple remote devices (syslog) 12 max ... File Size per file : 1250 Kbytes ... Hash Table entries age limit : 60 seconds ... Swlog Threshold : 90 percent" (p235)
    "Up to 8 Swlog logs files can be stored in the /flash directory starting (from swlog_chassis1 to 1.6) • An Swlog archive can store up to 40 files ... -> swlog output flash-file-size 12500" (p236)
    "Default severity level is 'info'. The numeric equivalent for the level 'info' is 6" (p238)
  summary: |
    日志口径：①输出三地——console、flash 本地文件、syslog（最多 12 台远程）；②文件体系——单文件默认 1250KB，/flash 下最多 8 个 swlog 文件（swlog_chassis1 至 1.6），swlog_archive 归档最多 40 个；③默认级别 info（数值 6），可按 appid/subapp 细调（如 ospf_0 的 hello 单独调 debug3）；④杂项默认——facility local0(16)、哈希表老化 60 秒、溢出阈值 90%、重复检测开、RFC5424 格式关；⑤命令日志 command.log 存最近 100 条命令（命令/用户/时间/来源/结果），启用期间不可删除。
  conditions: 修改文件大小用 swlog output flash-file-size（p236 示例值 12500 bytes）
  tags: [metric, logging, swlog]

- id: p35
  title: 镜像与抓包上限口径——镜像会话 2→4、MTP 索引 4、抓包 1 会话 64KB 上限 2MB、前 64 字节
  type: metric
  source_pages: p248-251
  source_chapter: PORT MIRRORING / PORT MONITORING
  source_quote: |
    "the maximum port-mirroring sessions has been increased from 2 to 4. • There is a limit of 4 Mirror-to-port (MTP) indexes. • Bi-directional counts as two MTP indexes for each destination port in the session." (p249)
    "Remote port mirroring over a link aggregate is now supported on the OS6560. (in 8.9R3)" (p249)
    "Captures first 64-bytes of frame • Session supported per switch or stack: 1 • Default file size: R8: 64 KB (max = 2 MB) • Round-Robin or stop capture when max storage reached • Cannot use port monitoring and mirroring on same port ... Data stored in compliance with the ENC file format (Network General Sniffer Format)" (p251)
  summary: |
    口径逐格：①镜像——会话上限已从 2 提高到 4；MTP（Mirror-to-port）索引上限 4 个，双向镜像每目的口计 2 个索引；同目的口同方向的多个会话只计 1 次；OS6560 自 8.9R3 支持经 linkagg 的远程镜像；②抓包（port monitoring）——每交换机/堆叠 1 会话、捕获帧前 64 字节、R8 默认文件 64KB（最大 2MB）、写满可轮转或停止、存 ENC（Network General Sniffer）格式 pmonitor.enc；③同一端口上镜像与抓包互斥。
  conditions: 各型号镜像/抓包能力差异查 Specification Guide（p248/p251）
  tags: [metric, mirroring, monitoring]

- id: p36
  title: 聚合 hash 默认值逐型号表与组播主端口规则
  type: metric
  source_pages: p280-281
  source_chapter: HASHING CONTROL ALGORITHM / LOAD BALANCING MULTICAST
  source_quote: |
    "Switch Default Hashing Mode 9900 extended 6900 brief 6870 extended 6860 extended 6865 extended 6560 extended 6465 brief 6360 brief ... -> hash-control brief -> hash-control extended [udp-tcp-port | no]" (p280)
    "Multicast traffic is by default forwarded through the primary port of the Link Aggregation Group ... If non-ucast option is not specified, link aggregation will only load balance unicast packets" (p281)
  summary: |
    逐格：出厂 hash 默认——OS9900/6870/6860/6865/6560=extended（含 UDP/TCP 端口，分担更均匀），OS6900/6465/6360=brief（仅源/目的 IP）；可用 hash-control brief / extended [udp-tcp-port] 修改。组播默认只走聚合主端口（primary port）；要非单播也参与分担须显式启用 non-ucast 选项，否则聚合只对单播做负载均衡。
  conditions: hash 同时作用于链路聚合、ECMP 与服务器负载均衡（p280）
  tags: [metric, linkagg, hashing, multicast]

- id: p37
  title: 802.1Q 结构数值——4096 个 tag/802.1p 3 位 8 级/物理口恒有一个默认 VLAN
  type: metric
  source_pages: p199, p295
  source_chapter: 802.1Q – VLAN TAGGING / How-To 提醒
  source_quote: |
    "4096 unique VLAN Tags (addresses) • VLAN ID == GID == VLAN Tag ... 802.1P • Three-bit field within 802.1Q header • Allows up to 8 different priorities • Feature must be implemented in hardware" (p199)
    "A PHYSICAL PORT ALWAYS HAS 1 VLAN (THE DEFAULT VLAN FOR THE PORT) THAT BRIDGES TRAFFIC (LEVEL 2)" (p295)
  summary: |
    两条结构数值：①802.1Q 头插 4 字节，含 12 位 VLAN ID（4096 个 tag）与 3 位 802.1p 优先级（8 级），标记必须硬件实现；②物理端口永远保留一个默认 VLAN 做二层桥接（其余 VLAN 打 tag 共链承载）——实验中口 1/1/3 同时桥接 VLAN 58、打标承载 VLAN 20/30。
  conditions: 实验 p295 输出显示同一口 tagged blocking/forwarding 状态取决于 STP 根桥选举
  tags: [metric, 8021q, vlan]

- id: p38
  title: UNP 分类九规则优先级与三层规则优先序；VLAN 1 不可删
  type: rule
  source_pages: p189, p192, p205, p213
  source_chapter: DYNAMIC VLAN MEMBERSHIP / VLANs (How-To)
  source_quote: |
    "UNP Port classification rules 1. Port/Linkagg 2. Domain 3. MAC address 4. MAC-OUI 5. MAC address range 6. LLDP 7. Auth-type 8. IP address 9. VLAN tag" (p189)
    "Precedence: Extended rule > Binding Rule > Simple Rule" (p192)
    "This VLAN CANNOT be deleted, but it can be disabled if desired." (p205)
    "VLAN 1 cannot be deleted. It is only possible to deactivate." (p213)
  summary: |
    两条结构规则：①UNP 动态分类按 9 条简单规则编号即优先级（端口/聚合 > 域 > MAC > MAC-OUI > MAC 段 > LLDP > 认证类型 > IP > VLAN tag），扩展规则 > 绑定规则 > 简单规则；扩展规则列表内设备须匹配全部规则；②默认 VLAN 1 不可删除，只能禁用（两处 How-To 重复强调）。
  conditions: UNP 口启用但认证关闭/失败时应用分类规则（p191）
  tags: [rule, unp, vlan]

- id: p39
  title: IP 路由启用条件与静态路由优先级——一个 IP 接口即开路由/无成员 VLAN 接口 DOWN/静态优于动态
  type: rule
  source_pages: p195, p348, p363
  source_chapter: INTER VLAN ROUTING / IP INTERFACE / STATIC ROUTING
  source_quote: |
    "IP routing is active as soon as at least one IP interface is associated with a VLAN ... The operational status of a VLAN remains inactive as long as no active port is associated with this VLAN" (p195)
    "IP is enabled by default on the OmniSwitch switches • IP forwarding is enabled when at least one IP interface is configured on a VLAN ... The first interface bound to a VLAN becomes the primary interface for that VLAN." (p348)
    "By default, static routes have preference over dynamic routes • Priority can be set by assigning a metric value ... -> ip static-route 0.0.0.0/0 gateway 1.1.1.1 metric 1 -> ip static-route 0.0.0.0/0 gateway 2.2.2.2 metric 2" (p363-364)
  summary: |
    三条规则：①只要 ≥1 个 IP 接口绑定到 VLAN 即激活 IP 路由（IP 默认已启用）；②VLAN 无活动成员口时 oper down，其 IP 接口 DOWN、不回 PING、不进路由通告（二层广播域不受影响）；③静态路由默认优先于动态路由，metric 调相对优先级，可配主备默认路由（metric 1 主 / metric 2 备）。
  conditions: 静态路由关联接口须 up and running（p363）
  tags: [rule, routing, static-route]

- id: p40
  title: Loopback0 特性与用途清单——不绑 VLAN 永活/RIP-OSPF 自动通告 BGP 不会/七类用途
  type: rule
  source_pages: p360
  source_chapter: LOOPBACK0
  source_quote: |
    "• Not bound to any VLAN • Always remain operationally active (as long as at least one VLAN is active) ... • Automatically advertised by RIP and OSPF protocols when the interface is created (not by BGP)" (p360)
    "• Use • RP (Rendez-Vous Point) in PIMSM • sFlow Agent IP address • Source IP of RADIUS authentication • NTP Client • BGP peering • OSPF router-id • Switch and Traps Identification from an NMS station (i.e OmniVista)" (p360)
  summary: |
    Loopback0 规则：不绑任何 VLAN、只要有一个 VLAN 活动就永远 oper active；创建后由 RIP 与 OSPF 自动通告（BGP 不会）。七类用途——PIM-SM RP、sFlow Agent 地址、RADIUS 认证源地址、NTP 客户端、BGP peering、OSPF router-id、NMS（OmniVista）设备与 trap 识别。各 IP 服务可用 ip service source-ip <Loopback0|接口> 统一指定源（支持 tftp/telnet/tacacs/swlog/ssh/snmp/sflow/radius/ntp/ldap/ftp/dns/all）。
  conditions: 实验：ip service source-ip loopback0 snmp 后 snmp 行显示 Loopback0（p361）
  tags: [rule, loopback0, source-ip]

- id: p41
  title: 实验口径：R-Lab 地址与账号全表（EMP IP 规则/服务器/凭据）
  type: metric
  source_pages: p14-18, p23, p38, p93
  source_chapter: REMOTE LABS
  source_quote: |
    "OmniSwitch credentials: login: admin password: Superuser=1" (p15)
    "ssh admin-netadv@10.4.X.Y // where X is your pod number and Y the switch number. ... Enter the passphrase: Superuser01!" (p38)
    "Switch Interface IP address 6900-A EMP 10.4.Pod#.1 6870-B EMP 10.4.Pod#.2 6560-A EMP 10.4.Pod#.3 6360-A EMP 10.4.Pod#.5 6360-B EMP 10.4.Pod#.6 6870-A EMP 10.4.Pod#.7 6860-B EMP 10.4.Pod#.8" (p93)
    "A DHCP server is running with an IP address of 192.168.100.102 ... DNS server on the client : 10.0.0.51" (p17-18)
  summary: |
    实验口径全表（生产必须替换）：①交换机登录 admin/Superuser=1；从 Linux 客户端 SSH 用 admin-netadv@10.4.X.Y，口令 Superuser01!（与交换机口令不同）；②R-Lab 门户 rdp.al-mydemo.com，账号 LanpodXa/Xb（X=1-32），密码每会话唯一；③EMP 地址规则 10.4.Pod#.{1,2,3,5,6,7,8} 对应 6900-A/6870-B/6560-A/6360-A/6360-B/6870-A/6860-B；④公共服务器 192.168.100.102（DHCP/RADIUS/Web/FTP 同机）、pfSense 192.168.100.108、客户端 DNS 10.0.0.51；⑤Stellar AP 凭据 support/aos2016（p16）。
  conditions: 仅 RLAB 培训环境；交换机预置最小化网络配置（非空配置，含到 10.0.0.0 管理网的静态路由，p92）
  tags: [metric, lab, credentials]

- id: p42
  title: VLAN/UNP 实验数值口径——实验 VLAN 编号/客户端 IP 段/RADIUS 用户
  type: metric
  source_pages: p204-214, p445-446, p477-483
  source_chapter: VLANs / Prior Configuration / Access Guardian (How-To)
  source_quote: |
    "sw5 (6360-A) -> ip interface int_1 address 192.168.10.5/24 ... -> ip interface int_50 address 192.168.50.5/24 vlan 50" (p206, p209)
    "Client 5: IP address = 192.168.110.51 Subnet mask = 255.255.255.0 Default gateway = 192.168.110.1 Preferred DNS server = 10.0.0.51" (p446)
    "USER TYPE AUTHENTICATION VLAN UNP POLICY LIST Employee 802.1x 20 UNP-employee deny_employee Contractor 802.1x 30 UNP-contractor deny_contractor" (p478)
    "-> aaa test-radius-server my_radius type authentication user employee password password ... Filter-ID = UNP-employee" (p481)
  summary: |
    实验口径：VLAN 体系——VLAN 1（默认）/50/40/57/58/20/30/110/278 等；客户端 IP 规则——VLAN x 内 Client N 用 192.168.x.10N（如 VLAN 20 的 Client 5 = 192.168.20.105）；网关用交换机 IP 接口地址（如 192.168.20.7）；Access Guardian 实验矩阵——employee/contractor 两 RADIUS 用户（密码 password）分别回传 Filter-Id=UNP-employee（VLAN 20）/UNP-contractor（VLAN 30），策略列表 deny_employees（禁 FTP 20-21）/deny_contractors（禁 HTTP 80）；RADIUS 服务器即 192.168.100.102。
  conditions: 全部为实验口径；客户端 MAC 动态学习后填入 unp classification（p212）
  tags: [metric, lab, vlan, unp]

- id: p43
  title: QoS 实验数值口径——端口默认 802.1p 7/策略 priority 5/限速 100k/precedence 65535 兜底
  type: metric
  source_pages: p423-426, p435, p450
  source_chapter: Quality of Service (QoS) / ACLs (How-To)
  source_quote: |
    "sw5 (6360-A) -> qos port 1/1/1 default 802.1p 7 ... 1/1/1 Yes No 7/ 0 DSCP 1G" (p423)
    "sw5 (6360-A) -> policy action priority_5 802.1p 5 ... -> policy action priority_5 maximum bandwidth 100k" (p425)
    "-> policy action action2 priority 7" (p402)
    "policy rule deny_ftp_employee condition ftpfromvlan20 action deny precedence 65535" (p450)
  summary: |
    实验口径：①端口默认标记实验用 802.1p 7（最高优先级）；②员工流量实验打 802.1p 5 并限 maximum bandwidth 100k（=100kbps），大包 ping（-s 65000）触发 Tri-Color 的 Red 计数；③优先级动作 priority 7 示例用于队列调度；④ACL 兜底规则惯例用 precedence 65535 放在最后（如 deny_ftp_employee/deny_http_contractor），网络组放行规则配 precedence 65535 同理。
  conditions: Tri-Color 统计 Green/Yellow/Red 见 p426 Notes；规则计数仅 6860(E)/6865/6900-X72（p407）
  tags: [metric, qos, lab]

- id: p44
  title: 可读事件日志格式与查看命令口径
  type: rule
  source_pages: p243, p263
  source_chapter: READABLE CUSTOMER EVENT LOGS
  source_quote: |
    "Use the following CLI commands to view Readable Customer Events. • swlog appid command with level event to filter switch logging information for events • To display customer event logs ... show log events ... The log output is in the following format: • <SWLOG TIMESTAMP> : <CMM>/<NI> : <MODULE_NAME> : <LOG_DESCRIPTION>" (p243)
    "2019 Jul 15 20:27:50.148 : CMM : vcmCmm : Virtual Chassis: Chassis 1 Role changed to Master" (p263)
  summary: |
    口径：先 swlog appid all subapp all level event 把全部应用过滤为 event 级，再用 show log events 显示；输出四段格式 = 时间戳 : CMM/NI : 模块名 : 描述。与原始 show log swlog（含调试细节）相比只保留重大事件，适合客户侧快读（示例：License 到期、电源状态、VC 角色变化、STP 根变化、链路 up/down）。
  conditions: show log swlog 支持 timestamp/slot/reverse 参数与 grep 过滤（p241-242）
  tags: [rule, logging, events]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 26 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 远程实验室接入 | 有 | p41 | R-Lab 地址与账号全表（实验口径） |
| task-02 | 多方式登录 | 有 | p05, p07 | console 速率分代 + 会话上限表 |
| task-03 | 用户与认证服务器 | 有 | p01, p02, p03, p14 | 默认账号/64 用户/密码策略/RADIUS 默认参数 |
| task-04 | 加固管理面 | 有 | p09, p08, p04 | 加固四清单 + WebView/SSL 口径 + 证书工具 |
| task-05 | WebView 管理 | 有 | p08 | 默认态与认证口径 |
| task-06 | Lightning Config | 有 | p10 | 192.168.0.1 体系 + 5 分钟口径 + 密码四要素 |
| task-07 | 配置生命周期 | 有 | p11, p12, p13 | 启动判定/三字段判读/备份口径 |
| task-08 | Virtual Chassis | 有 | p15, p16, p17 | 选举序/一致性核查/分裂防护 |
| task-09 | VLAN 与 802.1Q | 有 | p37, p38, p42 | tag 数值/UNP 优先级/VLAN1 不可删/实验编号 |
| task-10 | VLAN 间路由与 IP 接口 | 有 | p39, p22, p40, p21 | 路由启用条件/DHCP 选项/Loopback0/DHCP 中继 |
| task-11 | OST 使用 | 有 | p33 | 容量与获取口径 |
| task-12 | 诊断八件套 | 有 | p34, p35, p44 | 日志/镜像抓包上限/事件日志格式 |
| task-13 | 链路聚合 | 有 | p36 | hash 默认逐型号 + 组播主端口 |
| task-14 | STP | 有 | p18, p19 | 收敛与默认值/成本两套表 |
| task-15 | DHL | 有 | p20 | 1 会话 2 链/600 秒/30 秒默认/端口限制 |
| task-16 | DHCP | 有 | p21, p22 | 中继参数/选项语义 |
| task-17 | VRRP | 有 | p23 | 组播/MAC 模板/优先级规则 |
| task-18 | QoS | 有 | p24, p25, p43 | 默认口径/话机 MAC 表/实验数值 |
| task-19 | ACL 与用户口 | 有 | p26 | UserPorts/DropServices/recovery |
| task-20 | Access Guardian | 有 | p27 | pass-alternate/auth-server-down/Block |
| task-21 | LLDP | 有 | p28 | 30 秒/TTL 4×/层级限制 |
| task-22 | PoE | 有 | p29, p30 | 等级表/管理参数/型号线 |
| task-23 | 软件升级 | 有 | p31 | 签名镜像版本线/无恢复警告 |
| task-24 | Auto-Fabric | 有 | p32 | Y/N 语义/SPB 默认值/6 次尝试 |
| task-25 | Fleet Supervision | 有 | ——（结构类，见 framework f32） | 数值均为入口 URL 与声明要素，无独立数值口径条目 |
| task-26 | OST 2.0 安装 | 有 | p33 | 版本 18.1/容量/合同前提 |

**26/26 全部有原则/数值类覆盖**（task-25 的结构在 framework.md f32，数值类仅入口与要素，不构成独立 metric）。口径说明：
1. 所有实验给定值（p41/p42/p43）已标“实验口径”；版本号均保留完整位数（8.10R03/8.10R04、8.7R3、8.9R1、8.9R3、8.9R4、8.10R4、8.10.9.R04、8.7.98.R03、18.1）。
2. p249 镜像会话数原文表述“increased from 2 to 4”，但实验手册 p265 输出注释仍写“limited to two”——按规格口径取 4、实验注释为旧口径残留，已在对应条目注明（p35）。
3. LLDP-MED 两页示例数值不一致（p496 l2-priority 5 dscp 46 vs p499 l2-priority 7 dscp 14），属示例差异非规格，归入 counter-example 处理，未编造统一值。
