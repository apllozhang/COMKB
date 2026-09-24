# 原则/清单/规则/公式/数值口径候选 — OmniPCX Enterprise Starter (ENTPXTE400EN Ed12)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: OXE 系统容量与组网硬限额（集中式/网络式/机架）
  type: metric
  source_pages: p37, p38, p80
  source_chapter: Solution overview – Stand-alone / Network topology; Hardware miscellaneous
  source_quote: |
    "Scalability: up to 15000 users and 240 sites per CS" (p37)
    "n Communication Servers • Up to 100 nodes • Up to 100,000 extensions" (p38)
    "Limit: 240 Racks maximum per node • Including common racks, crystal ACT and OMS" (p80)
  summary: |
    三条硬限额：单 CS 集中式 15000 用户/240 站点；网络式 100 节点/100000 分机；每节点机架（含 Common、Crystal ACT、OMS）合计 ≤240。
  conditions: 网络式组网细节在 Advanced 课程
  tags: [metric, capacity, scaling]

- id: p02
  title: 系统账户四件套与 root 访问限制、会话超时
  type: rule
  source_pages: p88, p90, p99
  source_chapter: Connection & Login
  source_quote: |
    "4 accounts can be used on the OXE: • mtcl: maintenance account (ex. maintenance commands, database configuration…) • swinst: 'Facilities' account (ex. Backup & Restore operations, date & time…) • root: Administrator account, expert maintenance (ex. security management…) • client: Account with basic access (ex. basic maintenance commands) • Disabled by default, can be activated via swinst menu" (p88)
    "Direct access (by login request) to the root account can only be performed on the console port. • Access via IP (SSHv2) can only be performed indirectly by using the 'su' command from the mtcl account." (p90)
    "The 'root' and 'mtcl' accounts use a none configurable 900 seconds inactivity timer" (p90)
  summary: |
    四账户分工：mtcl=维护；swinst=Facilities（备份恢复/日期时间）；root=专家维护（安全管理）；client=基础访问（默认禁用、经 swinst 启用、需话务运行）。root 只能本地（串口/KVM 控制台）直登，IP 侧必须 mtcl→su -；root/mtcl 固定 900 秒无操作自动登出，不可配置。root 下运行 swinst 免输 swinst 密码（p100 Note）。
  conditions: client 账户菜单仅基础四项（Data Base/Network Maintenance/Resources Maintenance/Financial Report）
  tags: [rule, accounts, security]

- id: p03
  title: 密码策略九条（14 位起）与失败锁定、老化期口径
  type: rule
  source_pages: p89, p92, p93
  source_chapter: System Accounts & Passwords / Password security
  source_quote: |
    "Password string must have a minimum of 14 characters • Password string must have at least 2 alphabets (1 upper case mandatory) • Password string must have at least 2 numeric characters • Password string must have at least 1 special character ( ~!@#$%^&*()_+=`{}|[]\:\";'<>?,./ ) • Password string must not contain the user account name in any form • … not contain 4 or more consecutive same characters • … not contain 4 or more sequential characters (eg: abcd or 1234) • … not contain dictionary words • Password must be different from the last twenty-four used passwords" (p89)
    "Possible values of unsuccessful attempt before locking an account • 3 <= Number of unsuccessful attempts <= 5 • Default value is '3'" (p92)
    "Possible values: 10 < validity period for password in DAYS < 366 ('0' means no aging password)" (p93)
  summary: |
    密码九规则：≥14 字符；≥2 字母（必含 1 大写）；≥2 数字；≥1 特殊字符（给定字符集）；不含账户名；无 4 连同字符；无 4 连顺序字符；无字典词；与最近 24 个历史密码不同。失败锁定：连续失败 3-5 次（默认 3）锁账户 15 分钟（swinst 可调）。老化：有效期 10-366 天（0=不老化），到期后下次登录强制改密；启用 RADIUS 认证时必须关闭老化（RADIUS 认过、OXE 仍可能拒会话）。适用账户 root/mtcl/adfexc/swinst。
  conditions: 软件装载后强制设置强密码
  tags: [rule, security, password, metric]

- id: p04
  title: 防火墙默认策略与可信主机语义（INPUT DROP / OUTPUT ACCEPT / SSH 便门）
  type: rule
  source_pages: p135, p140-143, p157
  source_chapter: OXE internal firewall
  source_quote: |
    "From N3 onwards, the highest level of security is enabled in OXE by default … unless an exception is made for that host via 'iptables' menu. • A full-fledged firewall, using 'iptables', is implemented in OXE since OXE R101.0" (p135)
    "Chain INPUT (policy DROP …) … Chain FORWARD (policy DROP …) … Chain OUTPUT (policy ACCEPT …)" (p140)
    "Useful facility … during fresh installation or migration to N3 (restore database). • Not very secured, must be done in accordance with the customer. • When 'iptables' are successfully configured (trusted hosts), you can 'Deny SSH for all'" (p142)
  summary: |
    四条规则：①N3 起默认无任何主机可入站（R101.0 起为完整 iptables）；②INPUT/FORWARD 默认 DROP、OUTPUT 默认 ACCEPT；回环与 ICMP（ping）默认放行；③可信主机=对该主机全端口全服务放行（服务自身认证仍生效）；④"Allow SSH for all"（tcp dpt:22 全放行）是开局/迁移便门，须客户同意，配完可信主机必须 Deny 回去——Deny 不删规则，可信主机仍可 SSH。
  conditions: 版本锚点 N3 与 R101.0 均保留完整位数
  tags: [rule, security, firewall, version]

- id: p05
  title: 可信主机批量导入 CSV 格式与 DNS 前置条件
  type: checklist
  source_pages: p138-139, p162
  source_chapter: Restricted access configuration
  source_quote: |
    "1. File must not have any heading 2. Fields must be separated by comma's 3. Trusted Host must be in the following format TRUSTED_HOST,<Hostname>,<IP Address> 4. Trusted Range must be in the following format TRUSTED_RANGE,<First IP Address>,<Last IP Addres>" (p139)
    "If DNS is configured through SOT (or manually in /etc/resolv.conf), then the DNS IP should be added as a trusted host" (p138)
  summary: |
    CSV 导入清单：无表头、逗号分隔、主机行 TRUSTED_HOST,<主机名>,<IP>、网段行 TRUSTED_RANGE,<首 IP>,<末 IP>；文件经 SFTP 放 /tmpd 后在 netadmin 导入（自动 dos2unix）；导出固定 /tmpd/export_th.csv。配了 DNS 就必须把 DNS 服务器 IP 加为可信主机，否则域名解析类功能受阻。"Add domain name" 选项要求先配好 DNS。
  conditions: DHCP 池地址由 MAO 自动入规则、netadmin 不可改（见 p11）
  tags: [checklist, firewall, csv]

- id: p06
  title: 实验口径：RLAB 设备地址与账户密码总表
  type: metric
  source_pages: p9, p18, p98, p103
  source_chapter: RLAB SETTINGS / labs
  source_quote: |
    "OXE ENTP_OXE_EMPTY csa (physical) csm (main) 192.168.1.1 192.168.1.3 255.255.255.0 192.168.1.254 mtcl Administrator5689! swinst root Superuser2580* … FLEXLM SERVER ENTP_FLEXLM flex 192.168.1.80 … root letacla1 … IT SERVER … 192.168.1.252 training superuser NTP Server" (p9)
    "mtcl (for the current training; password= Administrator5689!) • root … Superuser2580* • swinst … Superuser2580*" (p98)
  summary: |
    实验口径总表：OXE csa=192.168.1.1 / Role csm=192.168.1.3（mtcl=Administrator5689!，root/swinst=Superuser2580*）；OMS=192.168.1.13（admin/root 均先 letacla1 后改 Superuser2580*）；FlexLM=192.168.1.80（root/letacla1，端口 27000）；IT Server（NTP/邮件）=192.168.1.252（training/superuser）；PC10/11=192.168.1.10/11、PC20/21=192.168.2.10/11；GD4=192.168.1.12（admin=letacla1、root=mg4.ale）；GD4 课堂网关=192.168.1.254；内部 DNS=192.168.1.250；外部 DNS=10.20.30.250；SIP 模拟器=12.0.0.2；话机默认密码 0000、话机 SSH admin/*tx8000#；SIP 运营商账号 pbxP/alcatel。生产环境必须全部替换。
  conditions: 实验口径（仅 RLAB）
  tags: [metric, lab, accounts]

- id: p07
  title: netadmin 操作三条硬规则（菜单模式/节点名唯一/域名告警/重启生效）
  type: rule
  source_pages: p146, p148
  source_chapter: IP Addressing & Firewall (How-To)
  source_quote: |
    "Warning: for a specific setup please use menu mode (netadmin -m)." (p146)
    "Warning: the node name must be unique." (p146)
    "WARNING: Default domain name is configured Please configure a legitimate registered domain name, to prevent certificate errors. Enter OXE Domain to be configured (default is oxedomain.com)" (p146)
    "TO TAKE THE MODIFICATION DONE VIA THE NETADMIN MENU INTO ACCOUNT, IT IS MANDATORY TO RESTART THE SYSTEM" (p148)
  summary: |
    四条：①特殊场景用菜单模式 netadmin -m（不要跑完整交互安装）；②节点名全系统唯一；③默认域名 oxedomain.com 会导致证书错误，应改为客户合法注册域名；④netadmin 一切改动必须 Apply（a）+重启系统才生效（Apply 时 NGINX 重启）。
  conditions: Role 地址在 netadmin -m → 5 Role addressing 中配置
  tags: [rule, netadmin, network]

- id: p08
  title: 动态端口区间与系统横幅关键字段
  type: metric
  source_pages: p149, p154, p117
  source_chapter: IP settings display / SSH banner
  source_quote: |
    "Low dynamic ports range configuration : 10000 - 10499" (p149)
    "CPU type : KVM(c0s1) … Role : MAIN … Security : SSH : YES(SSHv2) TRUSTED HOSTS : YES (iptables) Encryption : NO … PANIC flag : 1 … Panic Flex : 0 … Panic SWK Check : 1 … Panic RTR Check : 0" (p154)
    "(E) information in the prompt means that the telephonic application is stopped" (p98)
  summary: |
    三个巡检锚点：①低动态端口区默认 10000-10499（netadmin 11/4 可调，IPDSP TFTP 目标端口段与此对应）；②登录横幅给出 CPU 类型/Role/SSH/可信主机/加密/CAPEX 模式/PANIC 四旗标（PANIC flag、Panic Flex、Panic SWK Check、Panic RTR Check）——PANIC flag=1 即降级模式运行中；③提示符 (E)=话务停止、(数字)=话务运行，且不实时刷新，登录早于启动完成时要重新登录才更新。
  conditions: 横幅内容随版本略有差异
  tags: [metric, banner, ports, panic]

- id: p09
  title: NTP 数值口径（端口/包长/分层/chrony 选项）
  type: metric
  source_pages: p170-173, p177, p181-183
  source_chapter: NTP
  source_quote: |
    "The NTP protocol uses the port 123 (UDP/TCP) … The NTP packets have a size of 90 bytes on the Ethernet level (76 bytes on the IP level)" (p170)
    "burst Sends a burst of 8 control messages to the server when it is reachable … iburst Sends a burst of 8 control messages to the server when it is not reachable … prefer Gives a more important priority to this server" (p177)
    "chronyd version 3.5 starting" (p179)
  summary: |
    NTP 数值：端口 UDP/TCP 123；包长 90 字节（以太网）/76 字节（IP 层）；标准 RFC 1305；stratum 0=原子钟、1=主服务器（接参考钟）、n+1=次级；每事务 2 包；OXE 可同时作客户端与服务器。chrony（R101 起，版本 3.5）服务器选项：burst/iburst（可达/不可达时发 8 连发）/prefer（优先）；渐进同步仅 client/server 模式（不支持 broadcast），建立需数分钟；瞬时同步必须先停 chronyd 且为一次性。维护命令：chronyc sources/clients/ntpdata、systemctl status/start/stop/restart chronyd、lsof -i:123。
  conditions: NTP 认证用对称密钥（chrony.conf keyfile）
  tags: [metric, ntp, chrony]

- id: p10
  title: MAO 四工具与空库/恢复顺序规则
  type: rule
  source_pages: p186-187, p190, p192
  source_chapter: Database management / Empty Database Creation
  source_quote: |
    "The OXE database is called MAO (Maintenance Administration Operation)" (p186)
    "THIS OPERATION OVERWRITES THE EXISTING DATABASE AND THE SOFTWARE LICENSE FILES. IT CAN ONLY BE PERFORMED IF THE TELEPHONE APPLICATION IS STOPPED." (p190)
    "After creating an empty database, it is mandatory to restore the software licenses (See next chapter)." (p192)
  summary: |
    规则链：MAO 管理四工具=mgr/WBM/OV8770/UMC；空库创建①只能在话务应用停止时执行②必然连许可文件一起覆盖③完成后必须先恢复 OPS 许可再重启、再起话务。培训约定国家码 FR（实验口径），生产必须用现场真实国家码。Direct Link Network 选 Y=自动生成 99 条 Direct IP Links（ABC-F 用）。
  conditions: 经 Software Orchestration Tool 装载后默认即空库
  tags: [rule, mao, database]

- id: p11
  title: OPS 文件组、许可 ID 体系与锁值语义
  type: metric
  source_pages: p196-199, p201-203
  source_chapter: Licenses & OPS files
  source_quote: |
    "xx.swk • Contains the listing of customer licenses and software locks … xx corresponds to the customers ID" (p196)
    "'CC-SUITE-ID' when using Cloud connect … 'CPU-ID' for physical CS • 'Product ID' for virtual CS • 'ALU-ID' for Generic Appliance Server (GAS)" (p197)
    "The maximum value of a lock can be: • 0 or 1 when it corresponds to a 'service authorization' license • 0 to 99999 when it corresponds to 'number of users' licenses • The value 99999 indicates that the feature is authorized for unlimited use" (p199)
  summary: |
    OPS 四文件：hardware.mao（=xx.hw 兼容副本）、xx.swk（许可+锁清单）、xx.hw（硬件描述）、xx.zip（Actis 归档）。许可 ID 按载体：CC-SUITE-ID（Cloud Connect，全载体；形如 ADCBE-FGHIJ-KLMNO-PQRST，终身不变）/CPU-ID（物理 CS，存 PROM）/Product ID（虚拟 CS，FlexLM .ice 绑 USB Dongle-ID）/ALU-ID（GAS 免狗）。锁值：0/1=服务授权开关；0-99999=数量；99999=无限。示例锁：SIP users 2/15、Advanced IP users 0/15、OXE Media Servers 3、VoIP channels on OMS 120、Native Encryption Users 75、SipSoftPhone 10、ARS 85、G723.1 Server 30。
  conditions: CAPEX=本地锁；OPEX=云 LMS（Purple on Demand，OXE R100.1 起）
  tags: [metric, licensing, ops]

- id: p12
  title: 软件保护节奏——5 天自检 / 30 天宽限 / 降级三阶段动作表
  type: rule
  source_pages: p204-206, p220
  source_chapter: Software protection
  source_quote: |
    "In normal working mode, the Call Server checks its OPS files every five days … In case of inconsistency, the system switches to degraded mode • In case of 'CPU-Id' incoherency, the system suspects a maintenance operation (call server replacement…) and postpones the degraded mode procedure for 30 days" (p205)
    "Action 1 (as soon as detected) • Display a warning to the attendant (acknowledge mandatory) … • Continuous ring on the alarm set • Some management commands are locked and only give the error: 'Software protection error' • Action 2 (4 hours later): • Display the message « Please call your administrator » on every set with screen • Internal calls are not possible • Action 3 (8 hours later): • Loop back on actions 1 and 2" (p206)
  summary: |
    节奏表：正常运行每 5 天自查 OPS；不一致即降级；CPU-ID 不一致视为维护操作（换 CS）宽限 30 天（屏显告警但可用），到期降级。PANIC flag=1 时三阶段：①即时——话务台强制确认告警+事件入档+告警话机长振+管理命令报 "Software protection error"；②4 小时后——全部带屏话机显示 "Please call your administrator"、禁内呼；③8 小时后——循环①②。spadmin 选 1 可查 PANIC 四旗标，恢复 OPS 后归零。
  conditions: 非法解锁属违法并有法律风险（p204）
  tags: [rule, licensing, degraded-mode, metric]

- id: p13
  title: spadmin 十项菜单与 FlexLM 对接参数
  type: checklist
  source_pages: p199, p210-223
  source_chapter: OPS Files Restore & Backup (How-To)
  source_quote: |
    "Display current counters 1 … Display active file 2 … Check active file coherency 3 … Install a new file 4 … Read the system CPUID 5 … CPU-Ids management 6 … Display active and new file 7 … Display OPS limits 8 … Display ACK code 9 … Check connection with FlexLM 10" (p199)
    "FlexLM Licensing Enabled Yes … Flex Server IP Address … (192.168.1.80) … Flex Server port 27000 … Product ID discovery Yes … Use Flex License No … YOU NEED TO RESTART THE CALL SERVER!" (p219)
  summary: |
    spadmin 菜单 0-10 项如引文。判定口径：选 3 → "File OK"=校验通过 / "Error : Illegal hardware key"=不一致；选 10 → "OXE's license check with FlexLM server: OK" / "NOK <invalid license>"（许可无效）/ "NOK <FlexLM server not reachable>"（不可达，仅在配了 FlexLM 时有意义）。FlexLM 配置在 WBM System/Licenses：Enabled Yes+服务器 IP+端口 27000+Product ID discovery Yes+Use Flex License No，改后必须重启 CS。OPS 恢复两步：SFTP（Binary，mtcl）传 xx.* 到 /usr4/BACKUP/OPS → swinst Expert→5 OPS configuration→2 Restore（确认 y→同意新 keys y→运行模式 1=running）。恢复后 .swk 改名 software.mao 落 /usr3/mao；输出 "30 remaining day(s) to fix this issue" 即 CPU-ID 宽限提示。
  conditions: 实验环境许可文件由讲师发放（实验口径）
  tags: [checklist, spadmin, flexlm, licensing]

- id: p14
  title: GD4/OMS/XL 三类网关默认口令与访问规则对照
  type: rule
  source_pages: p248, p262, p759
  source_chapter: Hardware labs
  source_quote: |
    "V24 speed is 115200 bauds … default passwords: admin [letacla1] and root [mg4.ale]], it is requested to change the password of both accounts … at first connection" (p248)
    "root and admin accounts are accessible, default password : admin [letacla1] and root [letacla1]" (p262, OMS)
    "default password: admin [letacla1] and root [mgxl.ale]" (p759, GDXL)
  summary: |
    对照表：GD4——admin/letacla1、root/mg4.ale；OMS 虚拟 GD4——admin 与 root 均为 letacla1；GDXL——admin/letacla1、root/mgxl.ale。访问规则三类通用：V24 控制台 115200 波特可用 root+admin；SSH 只能从 CS 发起（需 ippstat 或 mgconfig/omsconfig 授权）、且只暴露 admin（root 需 su）；OMS VM 另有 kb/kb 账户专改键盘布局。首连强制改密（实验口径统一改 Superuser2580*）。
  conditions: mgconfig（GD4/GDXL）与 sudo omsconfig/omsconfig（OMS）为配置入口
  tags: [rule, security, gd4, oms, xl]

- id: p15
  title: Crystal number 规则与 MAC 登记两情形
  type: rule
  source_pages: p246, p250, p251-252, p264
  source_chapter: Hardware Shelves & Boards / OMS labs
  source_quote: |
    "Enter new crystal number [1..255] (values 18 and 19 are not allowed): 2" (p250)
    "Not checked: it is not required to specify manually the MAC address … Checked: it is mandatory to specify manually the MAC address … This attribute must be checked in 2 situations: -When crystal number is not set manually (automatic mode) -When DHCP addressing is used for GD board(s)" (p251)
    "The 'Board Ethernet Address' of the board must be specified in this menu and modified in case of board replacement, otherwise the CS does not send the binaries." (p252)
  summary: |
    两条硬规则：①crystal number 取值 1-255，18/19 保留（虚架 0=CS、19=INTIP 信令板）；②CS 库参数 IP/INT/IP Parameters/"Ethernet Address checked by TFTP"——在 crystal number 自动分配或 DHCP 寻址两种情形下必须勾选，并在 Shelf/<架>/Board/<GDx>/Ethernet Parameters 手工登记板 MAC（换板必须更新），否则 CS 不下发 binom 文件；必要时可在板上 reboot 强制重新下载。
  conditions: 手动 crystal number 且静态 IP 时无需登记 MAC
  tags: [rule, crystal-number, mac, tftp]

- id: p16
  title: 压缩器与语音指南资源口径（GD4/GA-4/OMS/XL）
  type: metric
  source_pages: p57-58, p65, p253, p266, p428, p759
  source_chapter: Hardware chapters
  source_quote: |
    "GD-4 … Voice over IP (30 compressors on the motherboard) … ARMADA: optional daughterboard providing 30 extra compressors" (p57)
    "This soft media-gateway provides media processing features of a GD-4 board • 120 compressors • VoIP codecs (G711, G722, G729 & OPUS (WB &NB)) • OPUS & G722 codecs are not available on hardware IPMG" (p65)
    "the GD4 has 30 embedded compressors and it is possible to add an additional 'Armada' daughter board in order to have a total of 60 compressors. … depends on the software license #135" (p253)
  summary: |
    资源口径：GD-4 板载 30 压缩器，+ARMADA 子板=60（许可 #135 约束，示例配置声明 30）；GA-4 板载 30；GDXL 同 GD-4 口径；OMS 上限 120 压缩器（许可 #385 控全系统 OMS 通道总数、#384 控 OMS 台数），支持 OPUS/G722——硬件 IPMG 无此两种编解码。OMS 三方会议数 ≤ 压缩器数的三分之一；语音指南并发：GD4/GA4=16 路、OMS=120 路；静态指南 4×8 分钟+动态 1×8 分钟（ADPCM32）。
  conditions: 许可锁号 #135/#384/#385 保留原号
  tags: [metric, capacity, compressors]

- id: p17
  title: XL 机架结构数值（384 FXS / 12 板 / 奇数机位 / GA-XL 机位）
  type: metric
  source_pages: p75, p76, p78, p758, p766
  source_chapter: XL-MEDIA GATEWAY / XL rack lab
  source_quote: |
    "XL-Media gateway chassis provides up to 384 * FXS ports • Up to 12 * FXS32-XL boards can be plugged into XL chassis • Each of the two GD-XL drives 6 * FXS32-XL boards" (p75)
    "One RACK XL is seen as 2 'half-rack' • We can only create a XL Rack with odd shelf position (e.g. 'X') • To have a possible creation, positions X and (X+1) should be free" (p78)
    "IN THE 2 XL RACKS, IF GAXL BOARD(S) IS/ARE USED, IT MUST BE AT THE POSTIONS 1 OR/AND 2." (p766)
  summary: |
    XL 数值：整架 ≤384 FXS=12×FXS32-XL（每板 32 Z 口=2×SLI-16-2），两个半架各由 1 块 GD-XL 驱动 6 板；创建必须占奇偶连续机位（从奇数位声明，偶半架自动生成）；GD/GA-XL 同板双角色（0 槽=GD，1/2 槽=GA，背板自动识别）；规划口诀=前 4 块 FXS32 放 3-6 槽，预留 1/2 槽给 GA-XL（>4 板才用 1/2 槽）；供电 -48Vdc 外置整流器；XL 无 PARI（不支持 DECT 板）；下载超时默认 1200 秒、协议 TFTP。
  conditions: 板卡型号 FXS32-XL；_FW 版本号书中为占位
  tags: [metric, xl, capacity]

- id: p18
  title: TDM 话机功耗规则（MR3 150W/110W、预留槽位、事件 3757）
  type: rule
  source_pages: p299-306
  source_chapter: TDM HYBRID DESKPHONE DEPLOYMENT IN A MR3 RACK
  source_quote: |
    "Incident '3757' is added to indicate if the terminal is not allowed to come in service due to power supply • e.g.: '3757= UA: Power Supply Anomaly: 0 Set 31000'" (p300)
    "With the introduction of the OXE Purple R100.0 version, a new Rack L (MR3), with a new 150W power supply, is available … ps = 0 type unknown … ps = 1 150W MR3 … ps = 2 110W MR3 … These values can be provided only by GD3, PowerMEX 2, GD4 or EvolMEX boards" (p301-302)
    "Minimum 4 slots to deploy such deskphones in the main rack of an IPMG … Minimum 3 slots … in an extension rack … 'MG Reserved' virtual boards must be managed in the MR3" (p304)
  summary: |
    规则组：①新 Essential TDM（ALE-20h/30h）功耗高于老 UA 话机，供电不满足时产生事件 3757 "UA: Power Supply Anomaly"；②R100.0 起 MR3 机架配 150W 电源（兼容所有 OXE 版本、免改 MAO、可与新旧混装），ps 参数（0=未知/1=150W/2=110W）存于 hardware.mao 亦可 config 命令查看，仅 GD3/PowerMEX2/GD4/EvolMEX 能上报；③功耗限制只约束 3U 机架——1U 架、Crystal、本地电源适配器不受限；④110W MR3 上要起 TDM 混合话机：主机架预留 ≥4 空槽、扩展架 ≥3 空槽（用 'MG Reserved' 虚板占位，话机初始化时 CS 检查该虚板），对应最多 64/72 台；⑤110W→150W 升级套件只适用 ps=2 的机架；扩展架 150W 还需 PowerMEX2/EvolMEX。
  conditions: 版本锚点 R100.0；ACTIS 的 UAI 板位规则在书外
  tags: [rule, tdm, power, version]

- id: p19
  title: 用户分机号与终端绑定三法数值口径
  type: rule
  source_pages: p291, p294-296, p325
  source_chapter: USER MANAGEMENT / Commissioning
  source_quote: |
    "Each user has a directory number • This number is unique in the system and has a length of 8 digits maximum" (p291)
    "The association between the Directory number and the device is done via the MAC Address … Manual allocation • Can be filled at the user creation • Must be removed when device replacement" (p294)
    "The secret code by default for all the users is: '0000'" (p325)
  summary: |
    三条：①分机号全系统唯一、≤8 位；②绑定标识按终端类型——IP 话机=MAC、IPDSP=Phone Identifier、TDM=机架/板/端口物理地址；自动分配=设备插线后输分机+密码由系统回收标识，手工分配=建户时填写且换机必须先清除；③用户初始密码统一 0000。TDM 手工分配时设备号位留空（自动分配口径）。
  conditions: IPDSP 需 PC 有音频设备否则不入服（p310）
  tags: [rule, users, commissioning]

- id: p20
  title: IPDSP 网络端口基线（UDP/TCP 全表）
  type: metric
  source_pages: p314
  source_chapter: IP Desktop SoftPhone – Appendix: network requirements
  source_quote: |
    "TFTP … Softphone (49152-65535) for Windows (1024-65535) for macOS,iOS and Android … TFTP Server (CS MAIN) 10000 to 10499" (p314)
    "UA signaling with OXE … Softphone 32512 to 32515 … CS 32640 to 32643" (p314)
    "Communication with Gx boards (GD/GA) … GD, GA, INT_IP A+B 32512 to 33023 … Communication with OTMS … OTMS 28 000 to 39 999 … Set Reassignment CMISE 2535" (p314)
  summary: |
    IPDSP 端口表：配置下载 TFTP——软话机侧 49152-65535（Windows）/1024-65535（macOS/iOS/Android）→CS 主 10000-10499；UA 信令——软话机 32512-32515 ↔ CS 32640-32643（双向）；与 GD/GA/INT_IP 的 RTP/RTCP——32512-32515 ↔ 32512-33023；与 OTMS——28000-39999；话机互打 RTP——32512-32515；TCP CMISE（换机重定向）2535。TFTP-HTTPS 顺序可选 TFTP/HTTPS/TFTP+HTTPS/HTTPS+TFTP：HTTPS 用于原生加密场景拉取 lanpbx.cfg。
  conditions: PC 侧防火墙可能需手工放行（p310 Warning）
  tags: [metric, ports, ipdsp]

- id: p21
  title: 内部 DHCP 服务器规则（默认关/Alcatel-only/租期/文件再生/防火墙联动）
  type: rule
  source_pages: p344-347, p356-358, p364
  source_chapter: INTERNAL DHCP SERVER / dynamic IP lab
  source_quote: |
    "It is mandatory to restart the DHCP server process after a modification • The configuration is checked only at the process startup (file dhcpd.conf) • The internal DHCP server uses the standard UDP ports: '67' on the server, '68' on the client" (p347)
    "Configuration: 'DHCP off' by default. … Alcatel terminals only: Yes-means that the CS DHCP server will answer only to the requests coming from Alcatel-Lucent devices." (p356)
    "WARNING : the following trusted hosts are DHCP addresses declared by MAO, they cannot be modified by netadmin." (p364)
  summary: |
    六条：①内部 DHCP 默认关闭（DHCP off），可只服务 ALE 设备或兼服务数据设备（ALE 话机优先接受 ALE DHCP 应答）；②改配置必须 Apply 重启 dhcpd（启动时才读 /etc/dhcpd.conf，且该文件每次重启按 MAO 重新生成、禁止手改）；③端口 UDP 67/68；④全局参数留空语义——默认路由空=用 netadmin 的、TFTP 空=给 CS 自己的 IP；⑤DHCP 池地址自动写入防火墙规则且 netadmin 不可改；⑥静态绑定=MAC↔IP+可指定启动文件（GD/GA 刷机时必填）。租期示例 default/max-lease-time 3600 秒、bootp 600 秒。巡检：netadmin -m 12（查看/释放）、dhcplease/-t/-a、/var/log/dhcplog。
  conditions: DHCP Relay 可跨网段（位于路由器/PC/VLAN 虚网关）
  tags: [rule, dhcp, firewall]

- id: p22
  title: 编号计划规则（8 位字符集/Timer 23/规划分段建议）
  type: rule
  source_pages: p368-372
  source_chapter: Prefix & Suffix plan
  source_quote: |
    "A prefix corresponds to a unique phone feature • 8 digits maximum (0 to 9, A, B, C, D, #, *)" (p370)
    "31T -> 'Set features/Password modification' prefix • 31000 -> Mr Brad Barkley directory n° … Timer 23 is managed by step of 100 mS • By default, timer 23= 30 (so 30 * 100 mS = 3 seconds)" (p370)
    "Reserve numbers a range for: • Attendant call • Outgoing prefix • Users • Speed dialing numbers • Phone features prefix • System prefix … • Emergency" (p371)
  summary: |
    规则：①每个前缀唯一对应一个功能，≤8 位（0-9ABCD*#）；②计划饱和用后缀 T+Timer 23（默认 30×100ms=3 秒）区分功能前缀与用户号（31T 改密 vs 31000 用户）；③规划建议：尽量简、留余量、按用途分段（话务台/外线前缀/用户/缩位/功能/系统/紧急各留段，示例 0/9 话务、1 紧急、2-3 用户、8 缩位、9/0 外线、*# 功能、ABCD 系统）；④多站点编号示例：站点<20 且每站<1000 用户时用 5 位（首 2 位站号+末 3 位 DDI 尾号）；⑤语音指南按计划录制，事后改前缀会导致指南报错误号码。
  conditions: 空库按国家码自动生成默认前后缀（FR 库：51=立即呼转、41=取消呼转、42=DND、43=留言、405=改密、506=叫醒等）
  tags: [rule, numbering, timer23]

- id: p23
  title: COS 三套体系数值（256 Phone COS / 矩阵 / 32 Access COS + 缩位 400 区 32 段）
  type: metric
  source_pages: p390, p397, p413-419, p660
  source_chapter: Phone Features COS / Connection & Transfer COS / Barring
  source_quote: |
    "Assigned to users 256 categories are available" (p390)
    "Numbers by range are distributed over one or more numbered areas (up to 400) • Among these 400 areas, each user entity can offer access to one or more ranges (up to 32)" (p397)
    "8 Logical discriminators are available for the system • 256 different Real Discriminators can be managed • 64 areas are available … 32 Access Classes Of Service" (p660)
  summary: |
    数值组：Phone Features COS 256 类，取值 1=允许/0=禁止，七分区（Rights/Set features/General services/PCX services/External services/Suffixes/Speed dialing areas）+Miscellaneous（摘机路由五模式 Direct/Delay(timer2)/Specialized incoming/NO Routing/External Alarm；默认溢出类型与地址；留言转接行为）；Connection COS 与 Transfer COS 共用用户侧 ID 但两张独立矩阵；缩位拨号 ≤400 区/每实体 ≤32 段；外呼闭锁侧：8 逻辑鉴别符、256 真实鉴别符、64 Area、32 Access COS。默认溢出示例：COS2 默认 forward on no answer→Timer 4（150×100ms=15 秒）转关联话机。
  conditions: 摘机路由表 Routing No 取值 1-255
  tags: [metric, cos, capacity]

- id: p24
  title: 语音指南资源与语言索引口径（4+1 槽/8 语言索引/MOH 激活二步）
  type: rule
  source_pages: p428-431, p434, p436, p441-444
  source_chapter: Voice guides
  source_quote: |
    "GD4, GA4 (ADPCM32 codec) • 4 x 8 minutes for static guides • 1 x 8 minutes for dynamic guides • 16 simultaneous accesses • OMS (ADPCM32 codec) … 120 simultaneous accesses" (p428)
    "8 different messages (i.e. one for each language available to the manager) are associated with each index number" (p429)
    "A dynamic message (if there is one) replaces a static message with the same index number" (p434)
    "Delete tone 2 (the default waiting tone) • Create voice guide 2 by assigning message No. 2 for each language." (p436)
  summary: |
    口径组：每板 4 个静态槽+1 个动态槽（vgstat 中 Slot5 动态，动态区 7200 页=3684 秒）；每个指南索引挂 8 条语言消息（Index1 法语/Index2 英语……Index8 备用）；动态消息同索引覆盖静态；文件语法 xxxx=静态、xxxx-d=动态、xxxx-D=并存。MOH 激活固定二步=删 Tone 2+建 VG2（Single-message VG 按语言配不同消息 / Music On Hold VG 全语言同曲、Listening Class 0）；ALE 提供 /DHS3ext/vgadpcm/flash/std/adpcmmoh，自制同名录放 custom 目录即替换。Generic 指南内置 4x/7x/*x 三套计划播报。指南选择规则：单板→该板；动静并存→动态；同 MG 多板→空闲通道多者；跨 MG→请求方所在 MG；播不出→对应备用音。vgstart=yes 时每个收听者各占一路，否则一路广播。
  conditions: 试听前缀 580+4 位索引（需 COS 允许 "Tones test"）；改系统语言映射需重启 CS
  tags: [rule, voice-guides, moh]

- id: p25
  title: 话务台与话务组限额数值
  type: metric
  source_pages: p451, p459, p461, p481
  source_chapter: Attendant group / Attendant sets
  source_quote: |
    "Number of attendant groups per node: 50" (p451)
    "Number of attendants per node: 250 • Number of attendant groups per node: 50 • Number of attendants in an ABC network: 250 • Number of attendant groups in an ABC network: 80" (p459)
    "Absent: • When an attendant in the idle position does not answer calls for a certain time (system timer '76'; 80 s by default), the attendant switches to absent state" (p461)
  summary: |
    限额：话务组每节点 50、ABC 网 80；话务员每节点 250、ABC 网 250；每 OXE 至少 1 个组（话务台必须隶属组）；组呈现并行（默认）或轮转（Statistic，最长待命优先）；互援=组号+溢出门限（Max. No. of Calls Bef. Overfl. 示例 5）；话务员位置 Idle/Busy/Unplugged/Absent（Timer 76=80 秒无应答转 Absent）；组三态 In service/Absent/Unplugged；4059EE 必须 IPDSP 关联且关联分机禁 multiline；PCX 连接串格式 [话务台号]@[主机名]，可 3 主机逗/分号分隔（空间冗余/PCS）；系统参数 4059 Close auto sign off（应用退出即拔线转 Night）与 4059: PC unregistered at logoff（True=登出擦 MAC 可换机登录）。
  conditions: BLF 用户监视每项最多 5 设备聚合
  tags: [metric, attendant, capacity]

- id: p26
  title: Entity/CDT 数值口径（0-1000/四状态/3+1 路由/切换时点/默认实体）
  type: metric
  source_pages: p498-502, p509-512, p523-524
  source_chapter: Entities
  source_quote: |
    "Entity IDs from '0' to '1000'" (p499)
    "4 different 'call distribution' status … For each status, three specific (successive) 'routing numbers' are possible • A fourth 'overflow number' is common to the 4 status … This overflow number is commonly called 'night forwarding number' • If a set is used as 'Overflow routing number', it has to be a mono-line extension" (p500)
    "4 changeover times maximum per day" (p501)
  summary: |
    数值：Entity 0-1000，默认建 0/1、用户默认归 1、中继组默认归 0；CDT=4 状态（Day/Night/Mode1/Mode2）×3 顺次路由+1 公共溢出号（必须单线分机）；状态小时表周一至周日、每天 ≤4 个切换时点；状态代码（entitystat -b）：0=Night、1=Day、2=Mode1、3=Mode2、4=Same As Group；Attendant Group Manager 默认 -1（不启用），配置后实体状态跟随该组且组员可在权限内手动切换；等待指南默认 VG2、话务等待指南默认 VG110（内呼播指南需 "Play VG for Internal Caller"=True；外呼还需 Timer 102≠0，换非 110 指南需 "Entity Call Guide No Answer"=True）；Overflow Timer 仅对话务台路由触发一次；每实体可挂 1 个 LDAP 服务器做 Call by Name 溢出（全系统 ≤20 个 LDAP）；实体级留言箱供话务录音。
  conditions: 未知 DDI 落中继组实体 CDT，开关=TG 参数 "VG for non-existent No."=NO
  tags: [metric, entity, cdt]

- id: p27
  title: 4645 容量与限制表（7000 箱/30 端口/时长/VPIM）
  type: metric
  source_pages: p527-529, p541-542, p538
  source_chapter: OmniMessage 4645
  source_quote: |
    "Up to 7000 controlled by software license … Up to 30 accesses … From 1 minute to 5 hours … From 5 to 100 … 500 hours or 600 hours (if HDD>80 GB) … 8 maximum … from 3 to 8 digits … From 10 seconds to 5 minutes … Up to 50 members" (p541-542)
    "Multi-levels, up to 5 levels with 10 choices maximum … Multi-languages, up to 8 languages" (p529)
    "Only one voice mail system (4645 or other) per OXE node" (p527)
  summary: |
    容量表：信箱 ≤7000（许可）、接入端口 ≤30、单留言 1 分钟-5 小时、每箱 5-100 条、总录音 500 小时（HDD>80GB 为 600）、语言 ≤8、编号 3-8 位、问候语 10 秒-5 分钟、分发列表 ≤50 成员；自动话务员 ≤5 级×每级 10 选项；仅支持 G711（非 G711 终端经本地板转码耗 2 压缩器）；一节点仅一个留言系统；拓扑 4 种（嵌 CS/独立服务器（CPU8 强制）/独立 VM 服务双 CS/嵌主备之一——VM 不冗余）；组网=ABC 网集中留言+VPIM；加密=DTLS（信令）+SRTP（媒体）；安全文档指针 SA0046/TC1774。邮件通知三档 None/Basic/Advanced（附音频附件，附件超限则发提示不附件），配额告警百分比与附件大小上限（MB）可配，"Treat msg as read" 可选；SMTP 默认端口 Plain 25/StartTLS 587/TLS 465。
  conditions: 基础指南只能用 Audio-Station 录制，不能从话机录
  tags: [metric, 4645, voicemail, capacity]

- id: p28
  title: 公共 SIP 中继规格（32 接入/62 通道/992 并发/Mini 64）
  type: metric
  source_pages: p576, p638
  source_chapter: Public SIP trunk / trkstat
  source_quote: |
    "Maximum number of accesses per SIP Trunk Group: 32 (always by pair) … Standard: • Each couple of accesses provides 62 (2x31) channels • 992 simultaneous communications maximum (if 32 accesses) • Mini SIP: • each couple of accesses provides 4 (2x2) channels • 64 simultaneous communications maximum" (p576)
    "Trunk Group type SIP: 2 accesses provide 62 channels • Trunk Group type MINI SIP: 2 accesses provide 4 channels" (p638)
  summary: |
    SIP 中继规格：每 TG 最多 32 接入且成对配置；标准型每对 62 通道（2×31）、满配 992 并发；Mini SIP 每对 4 通道、上限 64 并发；UMC 不支持建 Mini SIP。trkstat 输出按通道号显示 F/B/Ct/Cl/WB/Cr/WBD/WBM/D/M 状态。
  conditions: ARS 是外部网关型 SIP 中继的使用前提
  tags: [metric, sip-trunk, capacity]

- id: p29
  title: ARS/鉴别符/回叫翻译器数值与规则语义
  type: metric
  source_pages: p594, p600-602, p660
  source_chapter: ARS details / External callback translator / Barring
  source_quote: |
    "An ARS table can contain up to 10 routes … Each route can have a cost privilege (disabled by default) • The user COS must have a greater privilege than the ARS route in order to be authorized to use it • The ARS routes order can depend on a calendar" (p594)
    "Up to 255 translators … Up to 20 entries in each External Callback Translator • It is recommended to manage a default rule (DEF)" (p601)
    "The following syntax can be used for the rules : • A → International (associated to '+') • (B → Private) • DEF (default one)" (p602)
  summary: |
    数值：ARS 表 ≤10 路由，路由可带成本权限（默认禁用，用户 COS 权限高于路由成本权限才可用），路由顺序可挂日历；回叫翻译器全系统 ≤255 个、每个 ≤20 条、建议保底 DEF 规则；规则语法 A=国际（对应 +33 等）/B=私有/DEF=缺省。鉴别符体系：逻辑 0-7、真实 0-255（每实体可将 8 逻辑映射到不同真实）、Area 1-64、Access COS 32 个；真实鉴别符未创建时不能在实体选择器里关联（两处 Warning 反复强调）。
  conditions: 路由由 Time-based Route List 定序，成本上限默认 -1（不限）
  tags: [metric, ars, callback, discriminator]

- id: p30
  title: SIP 外部网关关键参数语义表（Registration/P-Asserted/Pool/Session Timer）
  type: rule
  source_pages: p614-615
  source_chapter: SIP Carrier access (How-To) – External SIP gateway
  source_quote: |
    "Registration ID: Used to fill the user part of the From header when the register is invoked … The external gateway registers with the URL : 'Registration ID @Authentication Domain' with a frequency defined by the 'Registration timer'" (p615)
    "Registration ID P_Asserted: … If set to No, the user part of the P-Asserted-ID provides the caller's DDI number in the INVITE -If set to Yes, it provides the Registration ID" (p615)
    "A public trunk group allows only the direct RTP by using a Re-INVITE message (no transfer and no overflow)." (p615)
  summary: |
    参数语义：网关以 RegistrationID@认证域 向运营商注册（Registration timer=刷新周期，需注册时设非 0 如 600）；Outbound Proxy=强制经代理（追加 Route 头）；Supervision timer=OPTIONS 探活周期（Pool 备份场景设短如 5 秒）；Registration ID P_Asserted=No 发主叫 DDI、Yes 发 Registration ID；RFC3325 支持与否决定隐号发送形态；SDP in 18x 控制 180 振铃是否带 SDP；Session Timer/Min/Method（UPDATE 默认，不支持则 RE-INVITE）；Pool Number 同值=同运营商双网关分摊+互备；编解码开关联动系统级（G722 需 G711 同开；G729 建议恒开，限带场景在 IP 域做）；公共中继只支持 Re-INVITE 直达 RTP（不支持转移/溢出直达媒体）。
  conditions: 运营商参数以 TC2005 与运营商文档为准
  tags: [rule, sip-gateway, parameters]

- id: p31
  title: 紧急通知机制数值与边界（100 队列/10 设备/Tone34/单机 only）
  type: rule
  source_pages: p683-687
  source_chapter: Emergency calls notification
  source_quote: |
    "Maximum 100 emergency notifications can be queued (FIFO mode) • Feature available only for stand-alone systems: single node, PCS excluded … Only one emergency group in the OXE system: • Maximum 10 devices in the system emergency group • Any NOE device with minimum 3 lines display … • Only business mode: • No room set, no contact center agent, no attendant, no DSS device" (p683)
    "Snooze: hide the notification for 20 seconds … Display a 10 seconds pop-up alert every 20 seconds • Till the notification is cleared or the user gets in idle mode" (p685-686)
  summary: |
    边界与数值：仅 stand-alone 单节点（PCS 排除）；全系统仅 1 个紧急组、≤10 台设备；设备须为 ≥3 行显示的 NOE 商务话机/IPDSP 且仅 business 模式（客房/坐席/话务台/DSS 不行）；通知发设备不发给用户（多设备上下文不计）；FIFO ≤100 条；空闲时可视消息+LED+Tone34，动作仅 Clear/Snooze(20 秒)/Callback；忙时每 20 秒弹 10 秒窗直至清除或回空闲；EMG log 软键（Events/EMG Log 或 Mail 键）查日志。配置前提：ARS 必须启用；紧急号划入专用 Area（1-64，系统参数 Emergency numbers area=0 关闭）且 Public COS 放行该 Area。
  conditions: Location ID（P-ANI）依赖系统启用 Direct IP Link
  tags: [rule, emergency, notification]

- id: p32
  title: Location ID / P-ANI 头规则（RFC 7913、80 字符、取值源四级）
  type: rule
  source_pages: p604-607, p692-698
  source_chapter: Caller geolocation / emergency lab
  source_quote: |
    "Service provided by adding the 'P-ANI' header … P-ANI (P-Access-Network-Info) is defined by RFC 7913, within the framework of private header extensions (RFC 7315) • The expected format includes Access Type & Location Identifier (string of 80 characters max)" (p605)
    "'Location ID Source' parameter: no data … or information managed at NPD, entity or IP domain level" (p605)
    "THE USE OF DIRECT IP LINKS BY THE SYSTEM IS A MANDATORY PREREQUISITE FOR SENDING LOCATION ID." (p693)
  summary: |
    规则：P-ANI 头携带主叫位置（≤80 字符）随外呼 INVITE 外发；网关参数 P-ANI Header=All/Emergency only/None；取值源在 NPD 配置（None/NPD/Entity/IP domain 四级）；过路呼叫沿用入 INVITE 的 P-ANI；限制：仅 SIP 中继（ABC-F 或 ISDN 变体）外呼支持；主叫与中继跨节点时必须 Direct Link（不支持混合链与跨 ABC-F 子网）；≤N2 的异构网络自动弃用但不掉话。维护命令 looknpd/entitystat/sipextgw 显示 Location ID 相关字段。
  conditions: SIP trace 示例头：P-Access-Network-Info: IEEE-802.3;eth-location="ALE building B floor 0"
  tags: [rule, p-ani, location, emergency]

- id: p33
  title: 呼叫分配计时器默认值表（76/141/144/140/142/102/trunk COS/Entity 溢出）
  type: metric
  source_pages: p700-708, p711-715
  source_chapter: Timers used for the call distribution / Call distribution lab
  source_quote: |
    "Timer 141: 30'' by default … Timer 76 : 80'' by default" (p701)
    "Timer 140: 15s by default … Timer 142: 15s by default" (p702)
    "Timer N° 76 … Timer units 800 (default value); managed by step of 100 mS … Timer N° 144 … Timer units 150 (default value)" (p711)
    "Trunk COS 31 (e.g. for SIP Trunk group) … Overflow Timer on No Answer 300 (default value) … Overflow Timer on Waiting 300 (default value)" (p713)
  summary: |
    默认值表（WBM System/Timers，单位 100ms）：76=800（80 秒，话务台振铃转 Absent/溢出）；141=话务台 Normal→Urgent（30 秒）；144=150（15 秒，内呼用户段）；140/142=各 15 秒（延迟振铃静默段）；102=0（0=不播话务等待指南，≠0 触发）；trunk COS 的 Overflow on No Answer/Waiting=300（30 秒，外线在用户段的溢出）；Entity Overflow Timer=0（关闭；触发一次且仅对话务台路由）；功能前缀歧义用 Timer 23=30（3 秒）；默认溢出呼转用 Timer 4=150（15 秒）。
  conditions: 实验口径提醒：外线场景用户段用 trunk COS 计时器、内线用 144
  tags: [metric, timers, call-distribution]

- id: p34
  title: 备份体系数值（每日 5:45 / 分区清单 / 恢复可选项）
  type: metric
  source_pages: p721-723, p726, p733, p736
  source_chapter: Database backup & restore
  source_quote: |
    "By default: daily backup at 5:45 AM • Can be re-scheduled" (p721)
    "DAY … DAY-1 … DAY-2 … DAY-3 … DAY-4 … DAY-5 … DAY-6 … FACTORY … IMMED … MONTH-1 … MONTH-2 … OPS … WEEK-1 … WEEK-2 … WEEK-3" (p723)
    "AS THE TELEPHONE APPLICATION IS ALREADY STOPPED, IT IS NOT POSSIBLE TO USE CS MAIN IP ADDRESS TO TRANSFER THE BACKUP FILE. CS PHYSICAL IP ADDRESS MUST BE USED FOR SFTP SESSION." (p733)
  summary: |
    数值与规则：自动备份每日 5:45（可改期）；分区=DAY+DAY-1..6/IMMED/WEEK-1..3/MONTH-1/2/OPS/FACTORY（/usr4/BACKUP 下）；恢复三选项——secure restoration（先存当前库为回退档案）、restore Cloud and Rainbow services（是/否：实验室剥离云凭据）、clean up archive（成功后删回退档案）；可存对象含 MAO/动态指南/计费/话务历史/ACD/4645（含或不含消息）/Linux 网络数据；话务停止后 SFTP 必须用 CS 物理地址（Role 地址随话务停止失效）。
  conditions: 传输类型必须 Binary；SFTP 端口 22
  tags: [metric, backup, restore]

- id: p35
  title: 维护工具数值口径（oxetrace 3GB/轮转、事件通道、syslog 514）
  type: metric
  source_pages: p740-743, p749-752, p754
  source_chapter: Maintenance
  source_quote: |
    "Totally 3 GB is needed for three types of traces (mtracer, traced and tcpdump) • If the available space is less than 4 GB, the number of rotation files is reduced accordingly" (p743)
    "OXE incidents can be dispatched on several ways: • Screen display • Disk storage, stored in 'usr4/incid' • Viewable with 'incvisu' command • SNMP hypervisor • External syslog server • Cloud Connect" (p749)
    "Syslog event are forwarded in UDP on default server port (514)" (p752)
  summary: |
    数值：oxetrace 三路抓包共需 3GB，可用空间<4GB 时自动减少轮转文件数；事件五通道（屏显/磁盘 usr4/incid/SNMP/外部 syslog/Cloud Connect），syslog 外发 UDP 514（netadmin 11/8 配置，按事件号在 MAO Incident Filter 启用），本地亦落 /var/log/messages；incinfo 语言 GEA/FR0/US0；infocollect 输出 /tmpd/infocollect_<cpu>_<版本>_<时间>.tbz（示例 16MB），需 root；securitystatustool 输出 XML（需话务运行），含默认密码用户占比、4645 密码策略等。
  conditions: oxetrace 启动会复位既有 mtracer/traced/tcpdump 与 actdbg
  tags: [metric, maintenance, tools]

- id: p36
  title: 中继组参数与同步优先级规则（节点号/去位数/同步段 0-199/200-254/255）
  type: rule
  source_pages: p775-779, p784-785, p793-794
  source_chapter: Trunk groups / T0 & T2 labs
  source_quote: |
    "The Entity 0 is used to: • Route a call to CDT in case of unallocated number … • The Connection Category '5' is used … • The public COS '0' is used in case of 'Trunk Group to Trunk Group' barring" (p777)
    "The reference is provided by the public carrier • Priority is given to T2 and T1 … Crystal shelf • Connected with INTOF • Available priorities: 0 to 199 • Shelf connected on the IP network • Available priorities: 200 to 254 • Priority 255 means access does not synchronize" (p779)
    "'NODE NUMBER' MUST BE YOUR SYTEM ID OTHERWISE IT WILL BE IMPOSSIBLE TO ACCESS TO THE LOCAL TRUNK GROUP PARAMETERS OR TO ALLOCATE A TRUNK" (p784)
  summary: |
    规则：中继组节点号必须=本系统节点 ID，否则无法访问本地参数/分配中继；默认实体 0（未知号码落其 CDT）、连接类别 5、Public COS 0（TG-TG 闭锁用）；信令变体按运营商选（VN→ISDN France、ETSI→ISDN all countries）；Nb. of digits unused 按运营商（VN 发 4 位/ETSI 发 9 位，t3 验证）；同步优先级：Crystal 架 0-199、IP 架 200-254、255=不同步（T2 建议 200、T0 建议 205），参考钟由运营商提供且 T2/T1 优先；TG Access 建好后必须 rstcpl 重置所在板；数字中继拨号发送分重叠（逐位）与整块两种。
  conditions: 事件/示例中的 t3 命令可核对收到位数
  tags: [rule, trunk-group, sync]

- id: p37
  title: UMC 前提与边界数值（N3-MD3/500 用户/15 参数 120 Profile/仅 OPEX 订阅入口）
  type: metric
  source_pages: p799, p801, p806-807, p813
  source_chapter: Unified Management Center
  source_quote: |
    "Note: Functionality available from OXE N3-MD3" (p799)
    "Limited number of user parameters (15) • Mandatory parameters are marked with '*' in red." (p801)
    "Only few parameters to define. (benefit of profiles) • Only 15 Parameters, 120 profiles depend on architecture (Internet, SBC, VPN) … NO Mini SIP trunk" (p807)
    "UMC Mid-Market up to 500 user's max day one • OXE Version N3 MD3 or above • Active OXE SPS Contract (CAPEX) • Active PoD Subscription (OPEX) • OXE must be cloud connected (FTR & RTR running)" (p813)
  summary: |
    数值与前提：UMC 功能自 OXE N3-MD3 起可用；Mid-Market 上限 500 用户（day one）；Easy users 仅暴露 15 个参数（*为必填），Easy SIP trunk 15 参数+约 120 个架构 Profile（后台自动约 80 参数），不支持 Mini SIP；访问需 Fleet Dashboard 或 MyPortal 权限（Technical advanced 权限、mtcl 凭据登录）；CAPEX 需有效 SPS 合同、OPEX 需 PoD 订阅，且 OXE 必须 FTR&RTR 云连接就绪；中继向导会在前缀冲突时拒绝或在无鉴别符时连带创建；建中继前建议先 MAO 备份，完成后按提示补配置并重启。
  conditions: 部分功能标注 NEXT DELIVERY（Desk Sharing 等）
  tags: [metric, umc, cloud]

- id: p38
  title: 系统语言/显示语言映射规则与 DB 国家码决定论
  type: rule
  source_pages: p190-191, p431, p447-448
  source_chapter: Empty DB / Voice guides – languages
  source_quote: |
    "please use the French country code (FR) for the creation of the empty database, regardless of the country in which this training is delivered. … on 'real customer site', you must specify the right country code matching to the real OXE system location." (p190)
    "According to the OXE country code (defined during the empty database building), user language indexes are automatically linked with display language index and VG language number. e.g. For a French database, 1=French, 2=English and so on…" (p448)
    "Once the numbering plan has been established, modifying phone feature prefixes/suffixes may result in a voice message providing users with incorrect information." (p431)
  summary: |
    三条耦合规则：①空库国家码决定音调/单语指南/前后缀默认集与语言映射（FR 库 1=法语 2=英语），培训统一 FR 为实验口径、现场必须真实国家码；②系统语言=显示语言（0-7）+指南语言（Flash VG 1-8）的组合，映射改动需重启 CS；③编号计划确定后再改功能前缀/后缀，静态指南播报的号码会失真——改计划必须同步核对指南。
  conditions: Display Language No. 0-7；Voice Guide Language Nb 对应 /System/Flash Voice Guide configuration
  tags: [rule, language, country-code]

- id: p39
  title: TDM/虚拟化编解码与语音加密覆盖口径
  type: metric
  source_pages: p42, p65, p528, p538
  source_chapter: IP encryption / OMS / 4645
  source_quote: |
    "Voice (SRTP) & signaling (DTLS) encryption • End-to-end native encryption for: • NOE IP Phones • SIP extensions (SEPLOS) • Public SIP Trunk • SIP trunk to Rainbow WebRTC Gateway • 8378 IP-xBS DECT Base stations • 4645 Voice Mail" (p42)
    "OPUS & G722 codecs are not available on hardware IPMG" (p65)
    "4645 supports only G711 algorithm" (p538)
  summary: |
    口径：原生加密=软件方案零硬件、证书认证，语音 SRTP+信令 DTLS，端到端覆盖 NOE IP 话机/SIP 分机（SEPLOS）/公共 SIP 中继/至 Rainbow WebRTC 网关的 SIP 中继/8378 IP-xBS/4645；编解码矩阵——OMS 独有 OPUS 与 G722（硬件 IPMG 无），G722/OPUS 需系统级放行才生效；4645 仅 G711，非 G711 终端经本地板转码（每路耗 2 压缩器）。
  conditions: Rainbow 章节在其它教材展开
  tags: [metric, encryption, codecs]

- id: p40
  title: ALE-3 / ALE-120 / AOM 配件关键约束（选型口径）
  type: rule
  source_pages: p276-277, p282, p288-289
  source_chapter: Users – phone range & accessories
  source_quote: |
    "The remote worker use case is currently not supported" (p282, ALE-3)
    "Cascading (up to 3 AOMs per Deskphone in NOE mode) • Up to 3 pages per AOM (24 keys per page) • 72 keys maximum (overall)" (p276)
    "AOM keyboards (must match OXE management) • AOM10: keyboard includes 10 keys • AOM40: Keyboard includes 40 keys • AOMEL: keyboard includes 14 keys" (p289)
  summary: |
    选型约束：ALE-3 仅 SIP 商务模式、功能级同 ALE-2，远程办公场景暂不支持；ALE-120 AOM 级联 NOE 模式最多 3 台、每台 3 页×24 键=72 键上限，2 台配置参考 TC3009（第一台可能需电源适配器 3MG27120AB），支持 PoE boost（Phone COS: Power Boost=Enable）与动态热插（需先在 OXE 配置）；EM200 智能扩展 5 寸屏、最多 3 台、20 键×3 页=60 键，TDM 场景经 U 盘升级、IP 场景经话机升级；IPDSP 的 AOM 键盘类型（AOM10/40/EL）必须与 OXE 管理一致。
  conditions: 话机硬件参数表（屏幕/音频/接口）归产品目录，不入册
  tags: [rule, phones, accessories]

- id: p41
  title: OXE 事件号速查（实验中高频出现的可解释事件）
  type: metric
  source_pages: p300, p746, p750-751
  source_chapter: TDM power / Static VG lab / Maintenance
  source_quote: |
    "'3757= UA: Power Supply Anomaly: 0 Set 31000'" (p300)
    "'=4:0260=Beginning of downloading /DHS3ext/vgadpcm/flash/std/vgadpcm.FR0 … =5:0261=End of downloading'" (p446)
    "'=4:0382=Init of IP set: No response from de set 96:6d:ad:e7:25:35,31003' … '=2:5815=Major failure in SIP component'" (p750)
  summary: |
    实验输出中可解释的事件号：3757=TDM 话机供电不足禁止入服；0260/0261=语音指南文件下载开始/结束；0382=IP 话机初始化无响应；5815=SIP 组件重大故障；5857=GD/GA/INTIP/RGD 重启原因；2019=板卡（耦合器）投运；2166=CPU 要求复位 GPA；2491=虚耦合器投运（Warning 级、无需动作）；2042=丢失 P1 类耦合器（Major，查板插接）。用 incinfo GEA <事件号> 取权威释义。
  conditions: 事件号随版本可能增减，以 incinfo 输出为准
  tags: [metric, incidents, troubleshooting]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 29 项任务清单的覆盖情况

| task | 任务 | 数值/规则类条目 | 对应 id |
|---|---|---|---|
| task-01 | 登录与账户密码治理 | 有 | p02（四账户/root 限制/900s）、p03（密码九规则/锁定/老化）、p06（实验口令总表） |
| task-02 | 系统启停 | 有 | p08（role 提示符口径）；流程归 framework f11 |
| task-03 | CS IP 双地址 | 有 | p07（netadmin 规则）；拓扑归 f12 |
| task-04 | 内部防火墙 | 有 | p04（默认策略）、p05（CSV 清单）、p21⑤（DHCP 池联动） |
| task-05 | NTP/chrony | 有 | p09（端口/包长/分层/选项） |
| task-06 | 空数据库 | 有 | p10（顺序规则）、p38（国家码决定论） |
| task-07 | OPS 许可与 FlexLM | 有 | p11（文件/ID/锁值）、p12（5 天/30 天/三阶段）、p13（spadmin/FlexLM 参数） |
| task-08 | GD4 上架 | 有 | p14（口令对照）、p15（crystal/MAC）、p16（压缩器） |
| task-09 | OMS 上架 | 有 | p14、p15、p16 |
| task-10 | XL 上架 | 有 | p14、p17（XL 数值） |
| task-11 | IP 话机开通 | 有 | p19（绑定/0000）、p20 间接（端口基线在 p20）；步骤归 case |
| task-12 | IPDSP | 有 | p20（端口全表） |
| task-13 | User Profile | 无数值类（纯操作）；步骤归 case c11 | - |
| task-14 | 数字/模拟用户 | 有 | p18（TDM 功耗）、p19 |
| task-15 | 内部 DHCP | 有 | p21（六条规则） |
| task-16 | 编号计划 | 有 | p22（8 位/Timer23/分段） |
| task-17 | 两级 COS | 有 | p23（256/矩阵/32） |
| task-18 | 语音指南与 MOH | 有 | p24（槽位/索引/MOH 二步）、p38（语言映射）、p41（下载事件） |
| task-19 | 话务台与 4059EE | 有 | p25（限额/位置/系统参数） |
| task-20 | Entity 与 CDT | 有 | p26（0-1000/4 状态/3+1/LDAP） |
| task-21 | 4645 与邮件通知 | 有 | p27（容量表/SMTP 端口）、p39（G711） |
| task-22 | 公共 SIP 中继 | 有 | p28（TG 规格）、p29（ARS/回叫数值）、p30（网关参数语义）、p39（编解码联动） |
| task-23 | 外呼闭锁 | 有 | p29（鉴别符/Area/COS 数值） |
| task-24 | 紧急通知 | 有 | p31（边界数值）、p32（P-ANI 规则） |
| task-25 | 呼叫分配计时器 | 有 | p33（默认值表） |
| task-26 | 备份恢复 | 有 | p34（5:45/分区/三选项/物理地址规则） |
| task-27 | 维护工具 | 有 | p35（3GB/514 通道）、p41（事件号） |
| task-28 | T0/T2 中继组 | 有 | p36（节点号/同步段/信令变体） |
| task-29 | UMC | 有 | p37（N3-MD3/500/15+120） |

**覆盖结论**：29/29 中 28 项有数值或规则类条目直接覆盖；task-13（User Profile）为纯操作序列无独立数值（其唯一口径"Profile 名必须大写、建议字母开头分机号"已并入 case.md c11 的 conditions）。两处口径说明：①实验口令总表（p06）为 LAB 专用口径，生产必须替换；②计时器/容量表数值均已按原文逐格转写，单位（100ms 步进）随条目标注。
