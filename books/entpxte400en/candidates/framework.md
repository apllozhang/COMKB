# 框架/流程/结构候选 — OmniPCX Enterprise Starter (ENTPXTE400EN Ed12)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径/CLI 命令、组件关系图示、系统分区。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——准入链（登录→启停→网络→时间→库/许可）→ 配置域（工具+硬件+用户）→ 业务域（呼叫处理+公网）→ 运维
  type: flow
  source_pages: p1-821
  source_chapter: 全书模块排布（每讲义章后跟 How-To 实验章）
  source_quote: |
    "LESSON SUMMARY ✓ Access to OmniPCX Enterprise Call Server • IP & V24 connection ✓ System Accounts & Passwords ✓ Password security" (p83)
    "For this specific hands-on, we suppose that an empty database has been created previously / Ask for the software licenses files to the trainer" (p211)
  summary: |
    全书按"先能碰机器、再配出系统、最后打通业务"推进：①实验环境（RLAB+ITSP1）；②系统概览与硬件架构（概念）；③准入链五连——连接登录/密码安全→系统启停→IP 寻址与内部防火墙→NTP 时间→空库与 OPS 许可，实验顺序即依赖顺序（如空库实验要求话务应用已停、OPS 恢复实验要求空库已建）；④配置域——mgr/WBM/OV8770/UMC 四工具介绍后，连续三个媒体网关上架实验（GD4/OMS/XL），再进入用户终端与基础业务（DHCP/编号/COS）；⑤业务域——语音指南、话务台、Entity、4645 内部呼叫处理，与 SIP 中继/闭锁/紧急/计时器的外线互通；⑥运维收尾——备份恢复、维护工具、T0/T2、UMC。每个实验章结尾常要求"恢复默认配置"以便下章衔接。
  conditions: 模块先后即依赖先后；跳章需自检前置（如不做空库/许可恢复，后续锁计数全为 0）
  tags: [flow, course-structure, master-flow]

- id: f02
  title: RLAB 实验平台两种 POD 拓扑（全虚拟 / 混合课堂设备）
  type: structure
  source_pages: p3-20
  source_chapter: TRAINING LAB ENVIRONMENT - FULLY VIRTUALIZED / HYBRID MODE
  source_quote: |
    "Remote Lab allows accessing a pool of virtual and physical machines (depending on the course) hosted in a data center. … Pods are independent of each other • Pods have the same configuration • Pods have access to common resources" (p5)
    "OXE ENTP_OXE_EMPTY csa (physical) csm (main) 192.168.1.1 / 192.168.1.3 … mtcl Administrator5689! swinst root Superuser2580*" (p9, 实验口径)
  summary: |
    两种实验形态共用同一逻辑拓扑：每 POD 一台 OXE（ENTP_OXE_EMPTY，物理地址 csa=192.168.1.1、Role 地址 csm=192.168.1.3）+ OMS（192.168.1.13）+ FlexLM（192.168.1.80，root/letacla1）+ IT SERVER（NTP/邮件，192.168.1.252）+ 4 台 PC Client（分跨 192.168.1.x/192.168.2.x 两个子网，分别预装 IPDSP 31000/31001/31002 与 4059EE 31003）；公共资源区 Subnet 0（10.20.30.x）放 NAS、SIP 模拟器（12.0.0.2）、外部 DNS（10.20.30.250），内部 DNS 192.168.1.250，网关 192.168.1.254/192.168.2.254/10.20.30.254。差异仅在"混合模式"把 PC Client 换成课堂物理设备（GD4 机架 192.168.1.12、ALE-300/500/20h/30h 话机、4059EE、POE 交换机、PC Classroom 192.168.1.9）。PC Client 挂 ENTP NAS 网络盘取软件，PC10 预装 2 个 MicroSIP 模拟公网号码。
  conditions: 实验口径（RLAB 专用基础设施）；全部 IP/账号为教学约定值，不可套用到生产
  tags: [structure, lab, rlab, topology]

- id: f03
  title: ITSP1 SIP 运营商模拟器拓扑与 POD 号码规则
  type: diagram
  source_pages: p21-26
  source_chapter: SIP CARRIER SIMULATOR
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 … ITSP1 SIP Gateway 2 gateway2.itsp1.com 10.20.30.52 … ITSP1 Public gateway public.itsp1.com 10.20.30.50" (p22)
    "PBX installation nb 3321PN … DDI table - First external nb 41000 … First internal nb 31000 … Example: 31002's external nb 3321PN41002" (p25)
  summary: |
    模拟器扮演出局运营商：两条 SIP 网关腿 gateway1/gateway2.itsp1.com（PBX 注册账号 pbxP/alcatel，SIP 域 sip.itsp1.fr）+ 公网网关 public.itsp1.com（两个 MicroSIP 模拟 Public/Emergency 用户，publicP/urgenceP@itsp1.fr，密码 public）。号码规则：PN 为两位 POD 号；国内 33{1-5}1PN12345、移动 33{6,7}1PN12345、国际 4421PN12345、紧急 112/15/17/18；呼出 0210312345 被变换为 +33210312345。呼入本 PBX：安装号 3321PN，DDI 外线段首号 41000 对内部首号 31000（即 3321PN41002 ↔ 31002），本 POD 回环拨 0210341002 或 33210341002。Pod1-6 安装号 332101-332106。
  conditions: 实验口径（RLAB 专用）；紧急号码显示等行为依赖模拟器特设规则（p636 Warning 明示）
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f04
  title: OXE 系统组件全景——CS + MG + 终端 + 外部应用
  type: diagram
  source_pages: p30-35
  source_chapter: SOLUTION OVERVIEW / Introduction & Main components
  source_quote: |
    "The OmniPCX Enterprise Communication Server or OXE is a Private Automatic Branch eXchange, known as 'PABX': • Software solution, based on a Linux Operating System • System based on an IP data network infrastructure" (p30)
    "The Call Server (CS), which is the system control center • One or more Media Gateways (MG) supporting standard telephone equipment: Voice guides, DTMF receptors, Conferences circuits, VOIP Compressors…" (p31)
  summary: |
    组件四层：①CS 系统控制中心；②一台或多台 MG 承载媒体资源（语音指南/DTMF 收号器/会议电路/VoIP 压缩器/数字模拟话机口/中继线/DECT 基站）；③终端——ALE IP 话机、SIP 终端、DECT/PWT、WLAN 手持、软话机；④外部应用——语音邮件、OmniVista 8770、Rainbow、Contact Center；CS 之间可用 ABC 直连。资源五种：语音指南、音调、压缩器（DSP）、DTMF、会议。中继类型谱系：SIP、T0/T2/T1、ISDN（France/All countries）、QSIG（Basic/Generic/Supplementary）、ABC-F（OXE 互联）、模拟（NDDI/Loop/Ground start）、ABC-F on IP（后章补 H323，p574）。
  conditions: 无版本前提
  tags: [diagram, architecture, components]

- id: f05
  title: 可靠性与拓扑两件套——CS Duplication / 单机集中式 / 网络式组网
  type: structure
  source_pages: p36-38
  source_chapter: SOLUTION OVERVIEW / Call server duplication, Stand-alone & Network topology
  source_quote: |
    "One Call Server is active; it plays the 'main' role • The other is in 'standby' mode. … The standby Call Server is continuously updated" (p36)
    "Scalability: up to 15000 users and 240 sites per CS … Local backup of remote sites with Passive Call Server (PCS)" (p37)
    "n Communication Servers • Up to 100 nodes • Up to 100,000 extensions • Nodes interconnected through ABC Direct IP links" (p38)
  summary: |
    三种形态：①CS Duplication——主备两台 CS，备用持续同步，故障即接管；②单机集中式——一 CS 带 n 个 IP MG，每 CS 上限 15000 用户/240 站点，远端分支用 PCS（Passive Call Server）本地保命，覆盖主备 CPU 同时失效/IP 网断/主 CS 不可达三种场景；③网络式——最多 100 节点、100000 分机，节点间 ABC Direct IP 互联（ABC=Alcatel Business Communication），特性透明+集中管理。空间冗余（跨子网主备）在"Advanced"课程展开（p131 注）。
  conditions: 空间冗余、PCS 细节在书外（Advanced 培训）
  tags: [structure, redundancy, topology, scaling]

- id: f06
  title: 管理工具四件套矩阵——WBM / OmniVista 8770 / UMC / mgr（+MAO 四工具口径）
  type: structure
  source_pages: p45-47, p186, p224-243
  source_chapter: OXE MANAGEMENT & CONFIGURATION TOOLS
  source_quote: |
    "Web Based Management • Free embedded web-based management solution, no software to install, no additional licenses" (p45)
    "Four tools can be used for management • mgr • With console or IP connection • OXE WBM • Alcatel-Lucent OmniVista 8770 • Unified Management Center" (p186)
  summary: |
    概览章给三家：WBM（内嵌免费、图形树、Chrome/Firefox/Edge）；OmniVista 8770（单界面管用户/终端/UC，管理档案委派、账务报表、实时告警、AD 同步、多系统平台）；UMC（云管理平台，简化用户配置与 SIP 中继创建，经 MyPortal 或 Fleet Dashboard 进入，语言 EN FR SP DE）。配置工具章展开四工具：mgr（CS 内置文本模式，mtcl 下 mgr -l <语言>、client 下菜单 1+2 且仅英文；ESC→keyboard mapping，CTRL V 确认 CTRL C 取消）、WBM（HTML5，仅 HTTPS，对象模型树+过滤器+参数名搜索——只搜参数名不搜值，3 字符起；Mass Provisioning 首列 +/-/# 或空=存在改/不存在建，导入只需待改属性，不导出密码）、OV8770（Java 客户端+HTML 目录应用，配置树 NETWORK/PCX/HARDWARE/DEVICES & USERS/SUB-NETWORKS）、UMC（菜单=Easy users/Easy SIP trunk/Expert Configuration(即云 WBM)）。
  conditions: WBM 浏览器/语言口径以 features list 为准；UMC 见 f28
  tags: [structure, tools, wbm, mgr, omnivista, umc]

- id: f07
  title: 硬件承载四形态 + Common HW 机架板卡体系
  type: structure
  source_pages: p49-62
  source_chapter: HARDWARE ARCHITECTURE
  source_quote: |
    "The Communication Server, which can run on following hardware: 'CS' (Call Server) in common Hardware, 'Virtual machine' (KVM, Vmware, MS Hyper-v, Nutanix, AWS), 'GAS' …, 'CPU' … in Crystal Hardware (in phase-out)" (p52)
    "The 1U type rack (referred to as Small or S rack) has 3 slots … The 3U type racks (Large rack) have 9 slots" (p54)
  summary: |
    CS 四种承载：Common HW、虚拟机、GAS、Crystal CPU（退场）。Common HW：1U Small 机架 3 槽（MG25）/3U Large 9 槽（MG80），可内/外置电池；主机架最多带 2 个扩展机架（GD-4 的 HSL 子板 ↔ EvolMEX）。核心板卡：CS-3（OXE 大脑，LAN1+LAN2 以太网冗余、4 口交换机、V24）；GD-4（固定 0 槽网关驱动，自带 30 压缩器+音调/指南/会议/DTMF，子板 HSL1/HSL2/ARMADA+30）；GA-4（应用板，30 压缩器/三方会议/静态动态指南，子板 ARMADA、SLANX 不可配置的 4 口 LAN 交换）；EvolMEX（驱动扩展机架）；接口板——BRA8（8×T0，无 S0）、PRA（T1/T2）、UAI16（数字 UA：ALE-20h/30h、IBS DECT）、SLI8/16（模拟 Z）、MIXED X/Y/Z（如 MIX 4/4/8=4T0+4 数字+8 模拟）。
  conditions: Crystal 细节书中自注不再深入（p70）；混装限制查技术文档
  tags: [structure, hardware, boards, racks]

- id: f08
  title: 虚拟化三线——OXE-V / OMS / GAS（含许可证控制差异）
  type: structure
  source_pages: p63-68
  source_chapter: VIRTUALIZATION / GENERIC APPLIANCE SERVER
  source_quote: |
    "OXE virtualized Call Server is called OXE-V • OXE-v license control • Based on Cloud Connect or on FlexLM server (except for Hyper-V, Nutanix & AWS)" (p64)
    "This soft media-gateway provides media processing features of a GD-4 board • 120 compressors • VoIP codecs (G711, G722, G729 & OPUS (WB &NB)) • OPUS & G722 codecs are not available on hardware IPMG" (p65)
    "Generic Appliance Server (GAS) • Virtualized OXE Call Server on top of Rocky Linux KVM layer • Hardware agnostic … Dongle-less package with license control based on the ALU-ID" (p68)
  summary: |
    虚拟化三条线：①OXE-V——虚拟 CS，5 种 hypervisor（VMware/KVM/Hyper-V/Nutanix AHV/AWS），许可走 Cloud Connect 或 FlexLM（Hyper-V/Nutanix/AWS 除外），功能限额与非虚拟化相同；②OMS——软件媒体网关（ALE SW 包跑 Rocky Linux VM），可配物理 OXE 或 OXE-V，同节点可与物理 MG 混跑；提供 GD-4 级媒体功能：120 压缩器、G711/G722/G729/OPUS（OPUS 与 G722 为软件独有）、会议/指南/音调/转码/RTP DTMF；③GAS——Rocky Linux+KVM 一体化（OXE VM + 可选 WebRTC VM(Debian)+OMS VM），FlexLM 直装于 Rocky Linux，免加密狗、按 ALU-ID 或 Cloud Connect ID 控制。全虚拟化示例拓扑：CS Main/Standby + FlexLM + OMS1/OMS2 四台 VM。
  conditions: hypervisor 兼容版本查最新 release notes
  tags: [structure, virtualization, oxe-v, oms, gas]

- id: f09
  title: Crystal 退场与 XL 机架补位结构
  type: structure
  source_pages: p69-80, p73-78
  source_chapter: CRYSTAL HARDWARE / XL-MEDIA GATEWAY
  source_quote: |
    "Reasons • Scarcity of components … • New XL-rack introduction" (p72)
    "XL chassis features 2 * independent Media gateways, each of them driven by a Gateway Driver (GD-XL) board … XL-Media gateway chassis provides up to 384 * FXS ports • Up to 12 * FXS32-XL boards … Each of the two GD-XL drives 6 * FXS32-XL boards" (p75)
    "Limit: 240 Racks maximum per node • Including common racks, crystal ACT and OMS" (p80)
  summary: |
    Crystal（ACT 技术，M2/M3 单元、CPU8 板）因元器件稀缺与市场趋势退场，向 Common HW 或全软件/IP 演进。XL 机架=19 英寸 6U Schroff 外壳 + BACK-XL 14 槽背板，瞄准高密度模拟用户线：内含 2 个独立半机架（各由一块 GD-XL 驱动 6 块 FXS32-XL），FXS32-XL=32 个 Z 口（=2×SLI-16-2），整架最多 384 FXS；GD/GA-XL 为同一块板（0 槽=GD-XL，1/2 槽按 GA-XL 声明，背板自动识别），可加 ARMADA；正面走 32 对线缆到 MDF，-48Vdc 由后部外部整流器供电。一个 XL 架占两个连续机位、只能从奇数位创建（X 与 X+1 空闲，GD-XL 自动创建）。混装上限：每节点 240 racks（含 Common/Crystal ACT/OMS）。
  conditions: XL 参数多处为占位（mgxl_XX.XX），以技术文档为准
  tags: [structure, xl, crystal, phase-out, fxs]

- id: f10
  title: 系统访问三通道与四账户模型
  type: structure
  source_pages: p84-90
  source_chapter: CONNECTION & LOGIN
  source_quote: |
    "4 accounts can be used on the OXE: • mtcl: maintenance account … • swinst: 'Facilities' account … • root: Administrator account, expert maintenance … • client: Account with basic access … Disabled by default, can be activated via swinst menu" (p88)
    "Direct access (by login request) to the root account can only be performed on the console port. • Access via IP (SSHv2) can only be performed indirectly by using the 'su' command from the mtcl account" (p90)
  summary: |
    通道：物理 CS=V24 串口或以太网 SSHv2（Putty/Teraterm）；虚拟 CS=各 hypervisor 控制台（vSphere/VMM/Hyper-V Manager/Prism/AWS EC2）或 SSHv2；GAS=VGA+键鼠经 VMM 或 SSHv2。V24 下可用 ifconfig -a 或 netadmin -m（选 2/3 再选 1）找回 IP。账户：mtcl（维护）、swinst（Facilities：备份恢复/日期）、root（专家维护/安全）、client（基础访问，默认禁用，经 swinst 启用，需话务应用运行中）；root 本地直登、IP 侧必须从 mtcl su；root/mtcl 固定 900 秒无操作超时。登录横幅含版本/ACD 版/SSH/iptables 状态/(E)提示符等信息。
  conditions: root 直登仅限本地（p99 Warning）；(E) 提示符不实时刷新（p117 Note）
  tags: [structure, accounts, access, security]

- id: f11
  title: swinst 双菜单体系（Easy 10 项 / Expert 9 项）与启停命令对照
  type: menu-path
  source_pages: p112-119, p122-125
  source_chapter: START & STOP THE SYSTEM
  source_quote: |
    "FACILITIES Easy menu … 1 DECT registration 2 Backup database on cpu disk 3 Restore database from cpu disk 4 Database re-init 5 Backup OPS files on cpu disk 6 Restore OPS from cpu disk 7 Stop the telephone 8 Start the telephone 9 Set new internet address 10 Stop the system" (p112)
    "There is no command to stop the telephone application. The whole system must be restarted and a telephone start-up cancelation must be performed" (p122 Notes)
  summary: |
    swinst 登录后先选 Easy(1)/Expert(2)。Easy 菜单 10 项如引文；Expert 菜单 9 项：1 Packages installation / 2 Deliveries installation / 3 Cloning & duplicate operations / 4 Backup & restore operations / 5 OPS configuration / 6 System management / 7 Database tools / 8 Software identity display / 9 Remote download。启停对照：起话务=Easy 8（默认即启 autostart）或 mtcl 下 RUNTEL；停话务=Easy 7（同时自动取消 autostart，p124 Warning）；重启=shutdown -r now；停机=shutdown -h now 或 Easy 10（显示 "Software Watchdog stopped / Power down."）；无话务重启=reboot 时在 "automatic start of dhs3 is about to begin waiting 5 seconds…" 提示处按回车取消。autostart 管理=Expert→6 System management→2。话务状态=role 命令（MAIN/STAND-BY=运行；"erreur mapping on remagen -7"=停止；提示符 (E)=大概率停止、(数字)=运行）。
  conditions: 菜单版本号随软件（示例 4.00.94）；改网络配置后必须重启系统（p148 Warning）
  tags: [menu-path, swinst, start-stop, role]

- id: f12
  title: Call Server IP 双地址体系与 netadmin 配置流
  type: flow
  source_pages: p126-133, p145-149
  source_chapter: IP ENVIRONMENT / IP Addressing & Firewall (How-To)
  source_quote: |
    "An IP address is linked to the CS physical interface (Ethernet) • This address can be used to access to the Call Server, whatever the Telephone Application status" (p129)
    "The 'MAIN' IP address will have to be used by all the devices that have to access to the system's MAIN CS" (p131)
    "TO TAKE THE MODIFICATION DONE VIA THE NETADMIN MENU INTO ACCOUNT, IT IS MANDATORY TO RESTART THE SYSTEM" (p148)
  summary: |
    双地址：物理接口地址（任何时刻可达，含话务停止——恢复备份传文件必须用它）+ Role MAIN 地址（仅话务运行时生效，所有设备/外部应用统一指向它；主备共享，同子网=本地冗余、跨子网=空间冗余）。netadmin 完整安装（交互问答）：节点名（唯一）→内部名字解析→单/双 CPU→CPU 名与地址→掩码→OXE 域名（默认 oxedomain.com 会致证书错误，应配合法注册域名）→默认路由。Role 地址：netadmin -m → 5 Role addressing → Add（csm/192.168.1.3）→ 23 Apply modifications（NGINX 重启）→ 重启系统。查看：netadmin -m 选 2（含 "Low dynamic ports range configuration: 10000-10499"）；ifconfig（eth0=主地址、eth0:0=物理地址别名、lo）。
  conditions: 所有实验地址为实验口径；netadmin 改动必须 Apply+重启
  tags: [flow, netadmin, ip-addressing, role-address]

- id: f13
  title: OXE 内部防火墙（iptables）策略与可信主机管理结构
  type: structure
  source_pages: p134-144, p156-163
  source_chapter: OXE INTERNAL FIREWALL
  source_quote: |
    "From N3 onwards, the highest level of security is enabled in OXE by default for various compliance requirements. … A full-fledged firewall, using 'iptables', is implemented in OXE since OXE R101.0" (p135)
    "Chain INPUT (policy DROP …) … Chain FORWARD (policy DROP …) … Chain OUTPUT (policy ACCEPT …)" (p140)
    "Warning: The imported CSV file should be in the following format 1. File must not have any heading 2. Fields must be separated by comma's 3. TRUSTED_HOST,<Hostname>,<IP Address> 4. TRUSTED_RANGE,<First IP Address>,<Last IP Addres>" (p139)
  summary: |
    策略：N3 起默认最高安全——任何主机默认不得入站；R101.0 起为完整 iptables 防火墙。INPUT/FORWARD 默认 DROP、OUTPUT 默认 ACCEPT；回环放行、ICMP 放行（大量工具依赖 ping）。配置入口：root → netadmin -m → 11 Security → 1 Firewall(iptables) Configuration：1 View / 2 Allow-Deny SSH for all（开局便门，"Not very secured, must be done in accordance with the customer"；Deny 后不删规则但可信主机仍可 SSH）/ 3 Restricted Access Configuration（1 查看/2 加单主机/3 加网段/4 删除/5 加域名（需先配 DNS）/6 删域名/7 Bulk Import/8 Bulk Export（/tmpd/export_th.csv））/ 4 iptables 日志开关。可信主机=全端口全服务信任；DHCP 池地址由 MAO 自动入规则且 netadmin 不可改（p364）；CSV 经 SFTP 传到 /tmpd 后导入（dos2unix 自动转换）。
  conditions: 任何主机先于防火墙配置前不可达；配置后按 a 应用
  tags: [structure, firewall, iptables, trusted-hosts, security]

- id: f14
  title: NTP/chrony 双同步方法与命令面
  type: flow
  source_pages: p164-183
  source_chapter: DATE AND TIME OF THE SYSTEM / Date, Time and NTP (How-To)
  source_quote: |
    "Since OXE R101, the 'chrony' tool is implemented in the OXE O.S. … 'chrony' is a versatile implementation of the Network Time Protocol (NTP)" (p167)
    "Instant synchronization is possible only when 'NTP' process ('chronyd') is stopped … This is a 'one shot' method: indeed, to maintain the synchronization, progressive synchronization must be activated" (p172)
    "The NTP protocol uses the port 123 (UDP/TCP)" (p170)
  summary: |
    对时六途径（date 命令/swinst/mao/Call Handling 话务台/T0T2 线上取时/NTP）；前几种为"粗调"（直接跳变），话机自动跟随；多站点可按 IP 域配时区（MAO）。系统时间=UTC+时区+夏令时。chrony（R101 起）承担渐进同步：client/server 模式（broadcast 不支持），UDP 123，包 90 字节（IP 层 76），支持对称密钥认证；OXE 可同时当 NTP 客户端与服务器；stratum 分层模型（0=原子钟、1=主服务器、n+1=次级）。操作链：swinst Expert→6 System management→1 Date & Time update→3 NTP server management：5 Modify NTP configuration→2 Add/Modify server（可加 burst/iburst/prefer 选项）；4 Instant synchronisation（需先 2 Stop NTP）；1 Start NTP。维护命令：chronyc sources/clients、systemctl status|start|stop|restart chronyd、lsof -i:123、chronyc ntpdata、more /etc/chrony.conf、ps -edf|grep chronyd。
  conditions: 时区修改必须重启系统（p176 Warning）
  tags: [flow, ntp, chrony, time-sync]

- id: f15
  title: MAO 数据库与空库创建流程（含许可连带效应）
  type: flow
  source_pages: p184-193
  source_chapter: DATABASE MANAGEMENT / Empty Database Creation (How-To)
  source_quote: |
    "The OXE database is called MAO (Maintenance Administration Operation)" (p186)
    "Create an empty Database • This operation • Overwrites the existing database and the software license files" (p187)
    "THIS OPERATION OVERWRITES THE EXISTING DATABASE AND THE SOFTWARE LICENSE FILES. IT CAN ONLY BE PERFORMED IF THE TELEPHONE APPLICATION IS STOPPED." (p190)
  summary: |
    MAO 管理四工具=mgr/WBM/OV8770/UMC。三类动作：建空库（覆盖现有库与许可文件；按国家码初始化音调/单语指南/前后缀；经"Software Orchestration Tool"装载后默认即空库）；存库（OXE→PC）；还库（PC→OXE）。空库流程：swinst Easy 7 停话务（系统重启、autostart 取消）→ swinst Expert→7 Database tools→2 Create an empty database→确认→输国家码（培训约定 FR，现场必须用真实国家码）→Direct Link Network y/n（Y=自动建 99 条 ABC-F 直连）→记录空库上限（Users 10014/1/2 com 3859，随 config.mao 变化）→重启 CPU→恢复许可→Easy 8 起话务→等 "No problem with compatibilities"。
  conditions: 建空库后必须恢复 OPS 再起话务（p192 Note）；培训约定 FR 为实验口径
  tags: [flow, mao, database, empty-db]

- id: f16
  title: OPS 许可体系——文件组/ID 体系/CAPEX-OPEX 双轨/降级模式三阶段
  type: structure
  source_pages: p194-209
  source_chapter: LICENSES & OPS FILES
  source_quote: |
    "The OPS files are the following: • hardware.mao • Copy of the xx.hw file (for compatibility reasons) • xx.swk • Contains the listing of customer licenses and software locks • xx.hw • Contains the hardware description • xx.zip • Archive used by Actis" (p196)
    "In normal working mode, the Call Server checks its OPS files every five days … In case of 'CPU-Id' incoherency, the system suspects a maintenance operation … and postpones the degraded mode procedure for 30 days" (p205)
  summary: |
    OPS 四文件：hardware.mao/xx.hw/xx.swk/xx.zip（xx=客户 ID）。ID 体系：CC-SUITE-ID（Cloud Connect，任何载体）／CPU-ID（物理 CS，PROM 内）／Product ID（虚拟 CS，FlexLM 的 .ice 绑 Dongle-ID，需 USB 狗）／ALU-ID（GAS，免狗）。CAPEX=锁在本地 OXE；OPEX=锁在云端 LMS（Communication Suite for MLE / Purple on Demand，OXE R100.1 起）。锁值语义：0/1=服务授权；0-99999=数量；99999=无限。spadmin 十项菜单管锁（1 当前计数/2 活动文件/3 校验（"File OK"/"Error: Illegal hardware key"）/10 查 FlexLM（OK / NOK <invalid license> / NOK <not reachable>））。PANIC Flag：0 正常 1 降级。降级三阶段：即时（话务台强制确认告警+事件入档+告警话机长振+管理命令报 "Software protection error"）→4 小时后（全部带屏话机显示 "Please call your administrator"，禁内呼）→8 小时后循环 1/2。FlexLM 对接：WBM System/Licenses（Enabled Yes/服务器 IP/端口 27000/Product ID discovery Yes）→重启 CS。
  conditions: OPS 目录：运行态 /usr3/mao（.swk 改名 software.mao），备份区 /usr4/BACKUP/OPS
  tags: [structure, licensing, ops, rtr, degraded-mode]

- id: f17
  title: GD4 硬件媒体网关上架流程（Shelf→Board→mgconfig→MAC→压缩器）
  type: flow
  source_pages: p245-258
  source_chapter: Hardware Shelves & Boards (How-To)
  source_quote: |
    "ALL SHELVES AND BOARDS ARE AUTOMATICALLY CREATED ACCORDING TO THE OPS CONTENTS (HARDWARE.MAO) … IF A SLOT IS OUT OF SERVICE IT IS POSSIBLE TO MOVE A BOARD TO ANOTHER SLOT." (p246)
    "Shelf address … Must match the 'crystal number' value, defined in 'mgconfig' menu" (p246)
    "IF YOU USE THIS COMMAND ON A GD4 BOARD, ALL BOARDS OF THE SHELF WILL BE RESTARTED!" (p257)
  summary: |
    五步：①Shelf 创建（WBM Shelf→Create：Shelf address 唯一且=板侧 crystal number；1U="Media Gateway Small"、3U="Media Gateway Large"；扩展机架 Role=Expansion 1/2 且填主架地址；主架 0 槽自动生成 GD4）；②板卡创建/改型（Board address+Interface Type，Common HW 板名以 MG- 开头）；③GD4 板侧配置——V24（115200，root 默认 mg4.ale/admin 默认 letacla1，首连强制改密）或 SSH（仅 CS 发起、ippstat/mgconfig 授权、仅 admin）→mgconfig：IP 模式（IPV4only/IPV6only/Mixed）、IP 四件套（本板 IP/掩码/网关/CS Role 地址）、Crystal number（1-255，18/19 保留，手动或自动）→保存→重启板→信令链初始化；④CS 库侧：IP/INT/IP Parameters/"Ethernet Address checked by TFTP"——crystal number 自动分配或 DHCP 时必须勾选并在 Shelf/Board/Ethernet Parameters 登记 MAC（不登记 CS 不下发 binom）；⑤压缩器：GD4 Daughterboard（None/ARMADA，30+30=60，受许可 #135 约束），改后 rstcpl <架> <板> 重启。维护命令：config/config -d/config all（虚架 0=CS、19=INTIP 信令）/cplstat/rstcpl/listout（离服原因码 A/C/I/X/T/U/P/B/Y）。
  conditions: crystal number 手动时不必登记 MAC；值为实验口径
  tags: [flow, gd4, shelf, mgconfig, hardware]

- id: f18
  title: OMS 虚拟媒体网关上架流程与强制字段
  type: flow
  source_pages: p259-268
  source_chapter: Software Media Gateway - OXE Media Service (How-To)
  source_quote: |
    "'OXE MEDIA SERVICE' VIRTUAL SHELVES (AND VIRTUAL GD4 BOARDS) ARE AUTOMATICALLY CREATED ACCORDING TO THE OPS CONTENTS (HARDWARE.MAO)." (p260)
    "Shelf Type 'Media Gateway Large'; this type is MANDATORY for OMS declaration … Shelf Role Main (Master); MANDATORY … OXE Media Server YES; MANDATORY … OF COURSE, DO NOT DECLARE NEITHER SECONDARY RACKS NOR BOARDS IN THIS SHELF!" (p260-261)
  summary: |
    OPS 恢复后 OMS 自动建为 Shelf 4（示例）。Shelf 四个强制字段：类型 Media Gateway Large / Role Main(Master) / OXE Media Server YES / 地址=VM 侧 crystal number；禁止加扩展架与板卡；虚 GD4 自动落 0 槽。VM 侧：控制台 kb/kb 改键盘布局（Rocky Linux 9.6）；root/admin 默认均 letacla1（与 GD4 的 mg4.ale 不同！），sudo omsconfig（admin）或 omsconfig（root）：IP 四件套+Crystal number（4）→保存（/home/mnt/flash/oms/oms.cfg）→重启。MAC 登记规则与 GD4 相同（Ethernet Address checked by TFTP）。资源声明：压缩器（上限 120，许可 #385 总通道约束）+最大并发指南数（例 16）+三方会议数（≤压缩器数的三分之一），改后须 reset OMS。许可校验：spadmin 看 #384 OXE Media Servers / #385 VoIP channels on OMS。维护同 config/cplstat/rstcpl。
  conditions: 实验口径：OMS=192.168.1.13、crystal 4
  tags: [flow, oms, virtual-mg, omsconfig]

- id: f19
  title: XL 机架上架流程与机位规划
  type: flow
  source_pages: p757-772
  source_chapter: XL rack & boards (How-To)
  source_quote: |
    "Shelf address: must be a free odd position followed be another free one. Example here: 9 and 10 are available, then we specify '9' … Shelf Type Media Gateway XL … The second XL media gateway is automatically created at the next (even) position." (p758)
    "IN THE 2 XL RACKS, IF GAXL BOARD(S) IS/ARE USED, IT MUST BE AT THE POSTIONS 1 OR/AND 2." (p766)
    "IN CASE OF DYNAMIC IP CONFIGURATION … THE RACK NUMBER WAS NOT ALSO DIRECTLY CONFIGURED IN THE BOARD. GDXL BOARD MAC ADDRESS MUST THEN BE SPECIFIED IN THE CALL SERVER DATABASE" (p764)
  summary: |
    流程：①Shelf 创建（奇数地址+Media Gateway XL 类型+Main Role；无 PARI——XL 不支持 DECT 板；Law 可留默认或强设 A/MU；偶数半架自动生成）；②GDXL 压缩器（默认 30，+ARMADA=60，许可 #135）；③GDXL 板侧 mgconfig（root 默认 mgxl.ale/admin letacla1）：IP 四件套+Crystal number（9）→保存重启；或 DHCP 动态（建议静态绑定+gdxl DHCP 类，配置文件 MGXL:-/downbin/mgxl/binmgxlstart 用于刷机）——动态时必须勾 Ethernet Address checked by TFTP 并登记 MAC；④FXS32 声明：GA-XL 只能占 1/2 槽，故规划口诀=前 4 块 FXS32 放 3/4/5/6 槽预留 1/2 槽给 GA-XL（>4 块才动用 1/2 槽）；Bell 标准线对映射参数（True=0 号设备落 1 号线对）；⑤模拟用户按 架/板/端口(0-31) 声明。维护：config 9 / listerm 9 3 / cnx neqt / cplstat 9 0（含虚 GPA 27 语音指南信息）/ rstcpl（GDXL 上执行=全架重启）。
  conditions: -48Vdc 电源与整流器安装工艺在书外（p77 拓扑）
  tags: [flow, xl, gdxl, fxs32, slot-planning]

- id: f20
  title: 用户开通三法与终端绑定标识
  type: structure
  source_pages: p290-296
  source_chapter: USERS / USER MANAGEMENT & Commissioning
  source_quote: |
    "Each user has a directory number • This number is unique in the system and has a length of 8 digits maximum" (p291)
    "The association between the Directory number and the device is done via the MAC Address … This operation allows the system to retrieve the MAC address." (p294)
    "The association between the Directory number and the terminal is done via the address of the equipment on the interface board. Don't specify any equipment number" (p296)
  summary: |
    用户=唯一分机号（≤8 位）。IP 话机绑 MAC：自动分配=话机插线后输分机+密码即回收 MAC；手工=建户时填，换机必须清除。IPDSP 绑 Phone Identifier（同两法）。TDM 绑板位物理地址（机架/板/端口；自动分配=插线注册时回收；手工=建户时填三地址，自动分配时端口位留空）。开通后维护：termstat/eqstat（d=分机/n=Neqt/p=架板0端口 三种语法）、termstat 选项 1-5（特性/呼转/关联/通话/重启）、listfwd/listdnd/listloc/listincall/listerm、edsbr -l GEA 订户查询、outserv/inserv 摘挂服。
  conditions: 初始话机密码统一 0000（p325）；IPDSP 需 PC 有音频设备（p310 Warning）
  tags: [structure, users, commissioning, mac, tdm]

- id: f21
  title: IP 话机两态开通操作链（静态 / 动态 DHCP）
  type: flow
  source_pages: p320-329, p355-365
  source_chapter: IP Desk phones (How-To) / IP Desk Phone in dynamic IP mode (How-To)
  source_quote: |
    "The IP parameters can only be modified during the set startup phase … Press the '#' and '*' key simultaneously … Select 'IP Parameters' … 'IP Config' … 'IPv4 Wired' … 'Network Settings'" (p322)
    "Static IP configuration is done … TFTP #1 Enter the call server main IP adress" (p324)
    "THE DHCP PROCESS RESTARTS AND READ THE '/ETC/DHCPD.CONF' FILE … IT IS MANDATORY TO DO THIS IN ORDER TO TAKE INTO ACCOUT THE MODIFICATIONS" (p358)
  summary: |
    静态线：话机启动期进 MMI（#* 同按或触摸屏设置图标→Config. MMI）→IP Parameters→IP Config→IPv4 Wired→Network Settings→IPv4 Mode Dynamic→Static→填 IP/掩码/路由→System Settings→TFTP #1=CS Main 地址（拉 lanpbx.cfg）→注册（拨自己分机+密码 0000）→自动重启在服。维护：WBM Users/TSC IP User 核对 Terminal Ethernet Address；换机=改 MAC；MAC 检索=背面贴纸或 Hardware infos；tnet d <分机> SSH 上话机；getlogs 取日志（先 ippstat 选 15 开 telnet/ssh 超时 0-1440 分钟，FileZilla SFTP admin/*tx8000#，文件在 /var/volatile/tmp）。动态线：WBM DHCP Configuration→Review-Modify→Configuration DHCP Server（默认 DHCP off；Alcatel terminals only Yes=只应答 ALE 设备）→CPU Main Subnetwork 全局参数（路由/TFTP 留空=沿用 netadmin/CS 本身）→IP Address Range 建 192.168.1.145-149（单 IP 两栏同值）→Apply Modifications（dhcpd 重启读 /etc/dhcpd.conf）→话机保持 Dynamic→注册。巡检：ps -edf|grep dhcpd；more /etc/dhcpd.conf（不可手改，MAO 重建）；netadmin -m 12（查/释放地址）；dhcplease/-t/-a；/var/log/dhcplog。
  conditions: 话务停止时 SFTP 必须用物理地址（p733 类似规则）；DHCP 池自动进防火墙规则
  tags: [flow, ip-phone, dhcp, static, dynamic, menu-path]

- id: f22
  title: 编号计划体系——Prefix Plan / Suffix Plan / Timer 23 饱和对策
  type: structure
  source_pages: p366-388
  source_chapter: PREFIX & SUFFIX PLAN
  source_quote: |
    "A prefix corresponds to a unique phone feature • 8 digits maximum (0 to 9, A, B, C, D, #, *)" (p370)
    "31T -> 'Set features/Password modification' prefix • 31000 -> Mr Brad Barkley directory n° … Timer 23 is managed by step of 100 mS • By default, timer 23= 30 (so 30 * 100 mS = 3 seconds)" (p370)
    "A suffix is a number dialed • During the communication … On a busy tone, use of the key '5' to activate the 'automatic callback' feature" (p378)
  summary: |
    编号计划每个号=一个前缀（用户/缩位/留言/功能……），前缀唯一对应一个功能，≤8 位（0-9ABCD*#）。饱和对策：后缀 T+Timer 23（默认 30×100ms=3 秒）区分"31T 改密前缀"与"31000 分机"。规划建议：对用户简单、预留扩展，按功能分段保留（0/9 话务台、1 紧急、2-3 用户、8 缩位、9/0 外线、*# 功能、ABCD 系统）；多站点编号示例（<20 站点、每站<1000 用户：首 2 位站号+末 3 位 DDI 尾号）。前缀用于摘机后（拨号音/指南/多功能键），后缀用于通话中（3=转会议、5=遇忙回叫）；功能前缀受 Phone Features COS 管。操作：WBM Translator/Prefix Plan、Translator/Suffix Plan 创建（前缀三字段=号码/含义/Station Features 类参数）；维护：ednump -l GEA、listrad。
  conditions: 空库按国家码已建默认前后缀（FR 库含 51=立即呼转、41=取消呼转、42=DND、43=留言等）
  tags: [structure, numbering, prefix, suffix, timer23]

- id: f23
  title: 双 COS 体系——Phone Features COS（256 类）与 Connection/Transfer COS 矩阵
  type: structure
  source_pages: p389-420
  source_chapter: PHONE FEATURES COS / CONNECTION & TRANSFER COS
  source_quote: |
    "Assigned to users 256 categories are available … User rights • Set features • General services • PCX services • External services • Suffixes • Speed dialing areas • Miscellaneous parameters" (p390)
    "The Connection COS management in the OXE is done via a matrix … Calling Number Connection COS : 1 … Called User Connection COS : 2 … Call … Forbidden" (p415)
    "In the user's properties, the Transfer COS Id is the same as the Connection COS COS Id • Two different matrices are managed in the OXE" (p419)
  summary: |
    Phone Features COS（256 类）七分区：Rights（防直代接/防强插/防呼转保护；外线呼转权/禁替代）；Set features（即时呼转/无应答转/锁机/替代/改密/DND…）；General services（组代接/直代接）；PCX services（关联机快呼/叫醒服务/末位未接回叫）；External services（账户码/重拨/停车取回）；Suffixes（Broker call/强插/会议/回叫/恶意呼叫追查/留言存取）；Speed dialing areas（全系统 ≤400 区、每实体 ≤32 区段，COS 控制可用性）；Miscellaneous（摘机路由模式 Direct/Delay/Specialized incoming/NO Routing/External Alarm + 路由表 1-255；默认溢出类型与目标；留言转接行为）。取值 1=允许 0=禁止。Connection COS：三方矩阵（分机↔分机/分机↔中继/中继↔中继）；Transfer COS 同 ID 但独立矩阵。入口：Classes of Service/Phone Features COS、/Connection COS、/Transfer COS；用户 Rights 页签挂接。
  conditions: 无
  tags: [structure, cos, matrix, rights]

- id: f24
  title: 静态语音指南与音乐保持体系（槽位/索引/MOH 激活/选择规则）
  type: structure
  source_pages: p425-448
  source_chapter: VOICE GUIDES / Static Voice Guides (How-To)
  source_quote: |
    "Voice guides are played by: • GD4, GA4 (ADPCM32 codec) • 4 x 8 minutes for static guides • 1 x 8 minutes for dynamic guides • 16 simultaneous accesses • OMS (ADPCM32 codec) … 120 simultaneous accesses" (p428)
    "Generic: compatible with generic numbering plans and offered in 12 different languages … Dynamic: modifiable, recorded by users via a set or via a PC (.wav file)" (p427)
    "For internal music to be played (broadcast), the following management operation must be performed: • Delete tone 2 (the default waiting tone) • Create voice guide 2" (p436)
  summary: |
    指南四类：静态 Generic（12 语言：保加利亚/英/法/德/希腊/匈牙利/意/日/韩/葡/俄/西）、静态 Standard（国家定制：美西/加法/比弗拉芒…）、动态（话机或 PC .wav 录制，存 /DHS3ext/vg/dhs，一文件一消息，同号覆盖静态）、外部 MOH（SLI 板接外部音源，CS 持续播放）。载体：GD4/GA4=4 静态槽+1 动态槽、16 并发；OMS 同槽位、120 并发。指南=索引号，每索引 8 条消息（对应 8 个系统语言，Index1 法语/Index2 英语……8 备用）。文件位置：/DHS3ext/vgadpcm/flash/std（vgadpcm.FR0/EN0、adpcmmoh）；定制 MOH 放 …/flash/custom/adpcmmoh。MOH 激活=删 Tone 2+建 VG2（两种做法：Single-message VG=按语言给不同消息；Music On Hold VG=全语言同曲，Listening Class 0）。选择规则：单板可用→该板；动静并存→动态；同 MG 多板→空闲通道最多者；跨 MG→与请求设备同 MG；播不出→备用音。维护：vgstat（槽位/语言标识/动态余量 3684 秒/消息语法 xxxx、xxxx-d、xxxx-D）/vgemis/vgstart（yes=每个听者占一路）/incvisu 看下载事件；试听=拨 580+4 位指南号（需 COS 放行）。
  conditions: 修改前缀/后缀后必须核对指南播报内容（p431 Caution）
  tags: [structure, voice-guides, moh, vgstat]

- id: f25
  title: 话务台体系——Attendant group / Attendant set / 4059EE / BLF
  type: structure
  source_pages: p449-478
  source_chapter: ATTENDANT GROUP / ATTENDANT SETS / 4059 EXTENDED EDITION
  source_quote: |
    "Minimum of one Attendant group per OXE … Two mode of call presentation •Parallel ( default mode) … •Statistic • The attendant group calls are presented cyclically on the attendant who has been on standby longest" (p451)
    "Note: Even with one attendant a group has to be created because AN ATTENDANT SET MUST BELONG TO A GROUP" (p451)
    "The 4059 EE handles the specific functions of the attendant but not the voice. It is mandatory to associate a physical set (ALE series) or an IP Desktop Softphone." (p484)
  summary: |
    结构三层：①Attendant group（每节点 ≤50 组、ABC 网 ≤80；并行/轮转两种呈现；组互援=组号+溢出门限；组状态 In service/Absent/Unplugged 决定 Day/Night）；②Attendant set（每节点 ≤250、ABC 网 ≤250；ID 全网唯一；必须隶属一个组；位置 Idle/Busy/Unplugged/Absent——Timer 76=80 秒无应答转 Absent）；③终端=ALE-300/400/500 或 4059EE PC 应用（专用 USB 键盘+坐席软件；语音必须由关联话机/IPDSP 承载；20 种语言；BLF 监视用户（最多 5 设备聚合，OXE 号码或 Rainbow 邮箱）/分机/中继组/中继线；Rainbow 集成=搜索、在场、BLF 监视、IM 模板；文本输入支持 Call by name/LDPR 目录；S1-S8/F1-F12 工具条可映射普通键盘；CDT 四状态×3 路由+溢出号（必须单线分机）自动生成）。
  conditions: 4059 EE 关联分机不得为多线（multiline 与 4059 IP 话务台不兼容，p482 Warning）
  tags: [structure, attendant, 4059ee, blf]

- id: f26
  title: Entity 体系——逻辑分区/CDT 四状态/状态小时表/经理组
  type: structure
  source_pages: p496-513
  source_chapter: ENTITIES
  source_quote: |
    "An entity is a logical subset of the OXE system … An entity is necessarily associated to: • Users, attendant sets, trunk groups, hunting groups… • 2 entities created by default (Entity 0, Entity 1) … Entity IDs from '0' to '1000'" (p498-499)
    "4 different 'call distribution' status are associated to this table • For each status, three specific (successive) 'routing numbers' are possible • A fourth 'overflow number' is common to the 4 status … This overflow number is commonly called 'night forwarding number'" (p500)
    "By default, 'Attendant Group Manager' equals '-1' • Meaning no Attendant Group Manager … If configured, the entity status follows this attendant group status" (p502)
  summary: |
    Entity=OXE 逻辑分区（0-1000，默认建 0/1，用户默认归 1），各带：Entity Call 前缀、CDT、状态、安装号、主叫/隐号、等待指南、留言箱、缩位区段。CDT 结构：Day/Night/Mode1/Mode2 四状态 × 各 3 个顺次路由号 + 公共溢出号（夜转号，须单线分机）；状态可由日历自动（周一至周日、每天最多 4 个切换时点）或由 Attendant Group Manager 决定（Entity Incoming State Hours 里把时段配成 "Attendant Group" 即跟随组状态；组员话务台在权限内可手动切换实体状态）。外呼侧：呼出闭锁随主叫实体出方向状态小时+接入类别；主叫身份随实体安装号/NPD；隐号可按键或前缀逐话启用。来话侧：DDI 无应答/等待/占线/离服溢出到被叫实体 CDT（需 Access COS 放行）；未知 DDI 落中继组所属实体（默认 0）CDT；MOH/话务等待指南按实体独立。
  conditions: 溢出号必须单线分机；实体状态 Night/Day/Mode1/Mode2 与 Public COS 区块四状态一一对应
  tags: [structure, entity, cdt, call-distribution]

- id: f27
  title: OmniMessage 4645 四种部署拓扑与容量口径
  type: structure
  source_pages: p526-546
  source_chapter: OMNIMESSAGE 4645
  source_quote: |
    "Only one voice mail system (4645 or other) per OXE node" (p527)
    "Call server and voice mail hosted on same server … Mandatory with CPU8 Call Server type … Call server main and call server stand-by separated from voice mail server" (p533-535)
    "4645 supports only G711 algorithm … If G711 algorithm can not be used directly • Other VOIP Codec to G711 conversion performed by a local board (OMS, GD4/GA4 or INTIP3)" (p538)
  summary: |
    定位：纯软件语音邮件（SME，典型 7000 用户）。拓扑四种：①嵌 CS/GAS/OXE-V 同主机（30 端口）；②独立专用服务器（CPU8 强制此形态）；③独立 4645 CS 服务主备双机（主 CS 保障 VM 运转）；④嵌主备之一（VM 不冗余——承载它的 CS 垮则 VM 垮）。虚拟化：可嵌 OXE-CS VM（单 VM）或独立 VM（CentOS，OXE 侧只查许可，A4645-V 免狗）。编码：仅 G711，非 G711 终端经本地板转码（耗 2 压缩器）。组网：ABC 网集中留言（直连/ABC 链）+ VPIM 留言网络互联。容量：≤7000 信箱（许可）、≤30 接入端口、单留言 1 分钟-5 小时、每箱 5-100 条、总录音 500 小时（HDD>80GB 时 600）、8 语言、编号 3-8 位、问候语 10 秒-5 分钟、分发列表 50 成员。接入：可视留言/高级显示动态键/TUI 任意话机/IMAP4+邮件通知。安全：SA0046、TC1774 加固指针+用户改密宣导。
  conditions: 基础语音指南只能由 Alcatel Audio-Station 录制（不可从话机录，p528）
  tags: [structure, 4645, voicemail, topology, sizing]

- id: f28
  title: UMC 云管理平台结构与边界（R1.1）
  type: structure
  source_pages: p797-814
  source_chapter: UNIFIED MANAGEMENT CENTER R1.1
  source_quote: |
    "UMC is accessible via MyPortal (OPEX system) or Fleet Dashboard (OPEX or CAPEX). … UMC Languages EN FR SP DE" (p798)
    "Only 15 Parameters, 120 profiles depend on architecture (Internet, SBC, VPN) … NO Mini SIP trunk" (p807)
    "UMC Mid-Market up to 500 user's max day one • OXE Version N3 MD3 or above • Active OXE SPS Contract (CAPEX) • Active PoD Subscription (OPEX) • OXE must be cloud connected (FTR & RTR running)" (p813)
  summary: |
    UMC=云侧管理平台，入口 MyPortal（OPEX）或 Fleet Dashboard（OPEX/CAPEX），登录用 mtcl 凭据，权限需 Technical advanced。三大功能：①Easy users——按预置/自定义 Profile 建户（仅 15 个参数，*为必填），含 DECT 供应、MultiDevice 自动建设备/关联/DECT 注册/参数复制、按键可视化编程、群组成员管理；边界清单：不管话务台/ACD/ALES 坐席/第三方 SIP（除 VTECH 酒店）/第三方 DECT GAP（8214 除外）/多实体/酒店套房/宾客/多国回叫号。②Easy SIP trunk——向导式建公共/私有（WebRTC GW、VAA）SIP 中继：15 参数+约 120 架构 Profile（Internet/SBC/VPN），后台自动处理约 80 参数；前缀已存在且非 ARS 前缀则拒绝；无鉴别符时连带创建；无 Mini SIP；建前建议 MAO 备份；完成后给"剩余手工配置"提示并要求重启。③Expert Configuration=云 WBM（无需 LAN 直达 OXE）。安全：法国 OVH 机房、TLS1.2 强制、ISO/IEC 27001。前提：N3 MD3+、SPS 合同或 PoD 订阅、FTR&RTR 已跑。
  conditions: 功能随版本演进（R1.1，多处标 NEXT DELIVERY）
  tags: [structure, umc, cloud, sip-trunk-wizard]

- id: f29
  title: 去话九步链路图（ARS 前缀→鉴别符→ARS→TG→NPD→DID→外部网关）
  type: diagram
  source_pages: p578-585, p592-602, p659-666
  source_chapter: PUBLIC SIP TRUNK / OUTGOING CALL PRINCIPLE & EXTERNAL CALL BARRING
  source_quote: |
    "Outgoing call prefix + user's entity will define a (real) discriminator … Real discriminator* + called number will define the ARS table to use … ARS route list provides information on the trunk group and the numbering command table" (p579-581)
    "The trunk group will inform about the NPD to use for DID transcoding and number's format • The numbering command table will provide the external SIP gateway to use" (p582)
    "* Real discriminator is not only used to provide ARS table information It can also be used for barring" (p580)
  summary: |
    去话固定流水线九步：①用户拨 0/9（ARS 前缀，携带逻辑鉴别符 0-7）→②取用户 Entity→③Entity 的 Discriminator Selector 把逻辑鉴别符映射为真实鉴别符（0-255）→④真实鉴别符规则表按被叫号匹配条目（号码→Area 区号+ARS 表号+位数）→⑤ARS 路由表（≤10 路由，时间表定序；每路由=中继组+编号命令表+去位/加位）→⑥中继组（信令变体/规格 SIP/DID 转码开关/NPD 选择器/实体/连接类别/Public COS）→⑦NPD（主被叫 NPI/TON 格式、默认号码源、被/主叫 DID 翻译器 ID）→⑧DID 翻译器（首外号+首内号+范围，组装去话 CLI）→⑨外部 SIP 网关（outbound proxy/域/凭证/注册）。闭锁在第④⑦步交点发生：Area×Public COS×实体状态。直抓中继（#0TG 前缀）走 "Number Compatible with" 取逻辑鉴别符，但 SIP 中继不支持直抓。
  conditions: ARS 是 SIP 中继可用前提（p616 Warning）
  tags: [diagram, ars, discriminator, npd, did, call-flow]

- id: f30
  title: 来话链路与回叫翻译器（Incoming call / External Callback Translator）
  type: diagram
  source_pages: p586-591, p599-603, p595-598
  source_chapter: PUBLIC SIP TRUNK / INCOMING CALL PRINCIPLE & DID NUMBERING TRANSLATOR
  source_quote: |
    "OXE receives a SIP incoming call … SIP invite To: +33210141000" (p586)
    "DID numbering translator D (e.g. 0) • First external number: 33210141000 (e.g.) • First internal number :31000 (e.g.) • Range size: 100" (p589)
    "Objective: to take into account the 'Caller Id' of external incoming call • Information is taken from the INVITE message … Up to 255 translators … Up to 20 entries in each External Callback Translator • It is recommended to manage a default rule (DEF)" (p600-601)
  summary: |
    来话三步：SIP INVITE（To=被叫外线号）→按网关所属中继组→NPD→被叫 DID 翻译器把 +33210141000 映射为内线 31000 振铃。外线号与内线号长度可不同（4500↔31000）；非 DDI 用户去话默认发话务台号。回叫翻译器：从 INVITE 取 Caller Id，按规则（A=国际带+、B=私有、DEF=缺省；每翻译器 ≤20 条，全系统 ≤255 个）加/删位，把 +33… 显示为 0… 并让未接回叫免拨外线前缀（例：A33 去三位加 00；A 去 1 位加 000；紧急号 A15 去 1 加 0）。
  conditions: 翻译器规则按国家/中继位置可分设；多数场景一个缺省翻译器够用
  tags: [diagram, incoming-call, did, callback-translator]

- id: f31
  title: 紧急呼叫通知机制链（区域→Location ID→紧急组）
  type: flow
  source_pages: p682-699, p604-607
  source_chapter: EMERGENCY CALLS NOTIFICATION / CALLER GEOLOCATION
  source_quote: |
    "Maximum 100 emergency notifications can be queued (FIFO mode) • Feature available only for stand-alone systems: single node, PCS excluded … Only one emergency group in the OXE system: • Maximum 10 devices" (p683)
    "1- OXE identifies the call made by a user in the system as an emergency one • 2- An emergency call notification is sent to the emergency group (audible tone and visual notification) … 3- EMG log soft key" (p684)
    "Service provided by adding the 'P-ANI' header with the caller location information in outgoing external call • P-ANI (P-Access-Network-Info) is defined by RFC 7913" (p605)
  summary: |
    机制四要素：①系统参数定"紧急号码区域"（1-64，0=关闭）；②真实鉴别符把紧急号（112/15/17/18）划入该 Area 且 Public COS 四状态放行；③紧急组（Applications/Emergency group，最多 10 台 NOE 商务话机/IPDSP，仅 business 模式，单系统仅一组，stand-alone only、需 ARS）：来话判定为紧急→组内设备收 Tone 34+可视弹窗（状态/时间/主叫号码名/被叫紧急号），动作仅 Clear/Snooze(20 秒)/Callback 三种，忙时每 20 秒弹 10 秒提示，EMG log 软键查日志（≤100 条 FIFO）；④Location ID：P-ANI 头（RFC 7913，≤80 字符）随外呼 INVITE 外发——取值源在 NPD 配置（None/NPD/Entity/IP domain），依赖系统启用 Direct IP Link，SIP 网关参数 P-ANI Header 选 All/Emergency only/None；维护命令 looknpd/entitystat/sipextgw 已扩展显示。中继 COS 溢出计时器参与外线来话分配。
  conditions: 通知发到设备不发给用户（多设备场景不计）；跨节点仅限 Direct Link 组网
  tags: [flow, emergency, p-ani, location-id]

- id: f32
  title: 呼叫分配计时器图集（76/141/144/140/142/102/trunk COS/Entity 溢出）
  type: diagram
  source_pages: p700-708
  source_chapter: TIMERS USED FOR THE CALL DISTRIBUTION
  source_quote: |
    "Timer 141: 30'' by default … Timer 76 : 80'' by default" (p701)
    "Timer 140: 15s by default … Timer 142: 15s by default" (p702)
    "'Overflow Timer' is used to speed up the overflow to the next routing number in the entity C.D.T. … this timer is triggered: • Only once • And only if the routing number is an attendant" (p707)
  summary: |
    计时器七件套：76=话务台振铃后转 Absent/溢出（80 秒）；141=话务台 Normal→Urgent 状态切换（30 秒）；144=内部呼叫用户话机振铃段（15 秒）；140/142=延迟振铃静默段（各 15 秒）；102=话务等待指南触发门（0=不播，≠0 后播 VG，默认指南 110，换指南需 "Entity Call Guide No Answer" 参数）；trunk COS 的 Overflow Timer on No Answer/Waiting（默认 300×100ms=30 秒）管外线在用户段的溢出；Entity Overflow Timer 加速 CDT 内话务台段溢出（仅触发一次且仅对话务台路由）。内部呼叫用户段用 144，外线用户段用中继 COS 计时器。
  conditions: 计时器单位 100ms（WBM System/Timers 中 800=80 秒）
  tags: [diagram, timers, call-distribution]

- id: f33
  title: 数据库备份/恢复体系（自动 5:45 + IMMED/OPS 分区 + Cloud/Rainbow 剥离）
  type: flow
  source_pages: p720-736
  source_chapter: OXE DATABASE BACKUP & RESTORE / Database Backup & Restore (How-To)
  source_quote: |
    "By default: daily backup at 5:45 AM • Can be re-scheduled • Local backup -> transfer of backup using SFTP is strongly recommended (HDD crash) • Network backup" (p721)
    "DAY … DAY-6 … FACTORY … IMMED … MONTH-1 … MONTH-2 … OPS … WEEK-1 … WEEK-2 … WEEK-3" (p723)
    "During restoration of a 'mao' database through SWINST, an option is provided to the administrator to restore the database with or without Cloud and Rainbow services." (p726)
  summary: |
    目标三场景：系统崩溃/误配置回滚/版本迁移后找回配置。可存对象：MAO、语音指南、计费、话务历史、ACD、4645 数据（含/不含消息）、Linux 网络数据。备份分区 /usr4/BACKUP：DAY+DAY-1..6（自动每日 5:45）、IMMED（手工）、OPS（许可）、WEEK-1..3、MONTH-1/2、FACTORY。手工备份=swinst Expert→4→1→1（mao+动态指南+计费）→SFTP 传 PC（Binary，mtcl，端口 22）。恢复四步：Easy 7 停话务（此时 SFTP 必须用 CS 物理地址！）→（可选）SFTP 回传备份到 IMMED→Expert→4→3→1→1 Restore from IMMEDIATE（可勾 secure restoration=先存当前库为回退档案；可勾 restore Cloud and Rainbow services=是/否——实验/实验室剥离客户云凭据）→清理档案→Easy 8 起话务。
  conditions: 话务停止后 Role 地址失效是恢复实验的隐藏坑（p733 Warning）
  tags: [flow, backup, restore, swinst]

- id: f34
  title: 维护排障工具箱八件套
  type: structure
  source_pages: p737-756
  source_chapter: MAINTENANCE
  source_quote: |
    "The 'oxetrace' tool is able to take Call Handling, SIP motor and network traces simultaneously and archive into the path given by the user" (p740)
    "Totally 3 GB is needed for three types of traces (mtracer, traced and tcpdump) • If the available space is less than 4 GB, the number of rotation files is reduced" (p743)
    "The tool generates a compressed file • Technical support will usually request this 'infocollect' compressed file" (p754)
  summary: |
    八件套：①oxetrace（菜单式一键抓 Call Handling+SIP motor+tcpdump 三路，问卷式选场景 1-13，存 /tmpd/<名> 四个子目录，停止时解码并打包 zip，二进制可回解码；空间不足自动减轮转文件）；②ippstat（IP 话机数据 1-22 项，-noname 供 GDPR）；③事件三件——incvisu（看事件，-t n 取最近 n 条）/incinfo <语言> <事件号>（事件释义，语言 GEA/FR0/US0）/syslog（netadmin 11/8 配置，UDP 514 外发，MAO Incident Filter 按 事件号 开关，/var/log/messages 同步落盘）；④securitystatustool（XML 输出：SSH/SSL 证书、可信主机、RADIUS、NTP、syslog、密码策略、版本、SNMPv3、DISA、默认密码用户占比、4645 密码策略——需话务运行）；⑤infocollect（root 运行，离线分析大包 .tbz，支持 -netwnodes/-pcs 等选项）；⑥tcpdump（root，host/port 过滤，-w 存 pcap 供 Wireshark）。事件分发通道：屏显/磁盘 usr4/incid/SNMP/外部 syslog/Cloud Connect，WBM 可按派发与类型过滤。
  conditions: 命令需对应账户（oxetrace/ippstat=mtcl；tcpdump/infocollect=root）
  tags: [structure, maintenance, oxetrace, incidents, tools]

- id: f35
  title: T0/T2 中继组开通流程（传统 ISDN 线）
  type: flow
  source_pages: p773-796
  source_chapter: TRUNK GROUPS / T0 trunk group (How-To) / T2 trunk group (How-To)
  source_quote: |
    "'NODE NUMBER' MUST BE YOUR SYTEM ID OTHERWISE IT WILL BE IMPOSSIBLE TO ACCESS TO THE LOCAL TRUNK GROUP PARAMETERS OR TO ALLOCATE A TRUNK" (p784)
    "In reality the customer shall choose the mode of signaling according to the carrier. If the carrier is in VN then put ISDN France. If the carrier uses ETSI put ISDN all country." (p784)
    "IN ORDER TO WORK PROPERLY, THE BOARD WHERE THE TRUNK GROUP IS DECLARED HAS TO BE RESETED" (p785)
  summary: |
    中继组参数组：索引（唯一）/逻辑鉴别符（选填，闭锁用）/信令变体/规格/DID 翻译器/发送位数（直抓用）/来话去位/实体（默认 0：未知号码落其 CDT+TG-TG 闭锁取鉴别符）/连接类别（默认 5）/Public COS（默认 0）。T0/T2 五步：①确认 MG-BRA/PRA 板在服；②建 TG（ID/名称/节点号=本系统 ID/Tone on seizure 勾选/信令变体按运营商 VN→ISDN France、ETSI→ISDN all countries/Number compatible with=-1 起步/发送位数/DDI 转码 True）；③本地参数（实体号、Nb. of digits unused 按运营商——VN 发 4 位 ETSI 发 9 位，t3 验证；B Channel Choice 默认 NO）；④建 Access（物理地址 架-板-口，时隙自动）→必须 rstcpl 重置所在板；⑤同步优先级：Crystal 架 0-199（INTOF）、IP 架 200-254、255=不同步（T2 建议 200、T0 建议 205；Network mode 客户侧 no、运营商侧 yes）；抓取前缀 #010/#012（Professional Trunk Seize/With Overlap，填 TG 号）。巡检：trkstat [-r]、trkvisu all、t3（ISDN 呼叫追踪）、NOS LED（T2 无信号告警）。
  conditions: 教室信令与位数为实验口径；同步参考由运营商提供、T2/T1 优先
  tags: [flow, t0, t2, trunk-group, isdn]

- id: f36
  title: 公共 SIP 中继开通主流程（TG→外部网关→ARS→鉴别符→NPD/DID→回叫→国际/紧急）
  type: flow
  source_pages: p609-640
  source_chapter: SIP Carrier access (How-To)
  source_quote: |
    "THIS MANAGEMENT MUST BE DONE ACCORDING TO THE SIP PUBLIC PROVIDER REQUESTS! PLEASE CONSULT THE DOCUMENTS (TC 2005, AND ADDITIONAL ONE…)" (p611)
    "ARS IS REQUIRED TO USE SIP TRUNK GROUP WITH AN EXTERNAL SIP GATEWAY" (p616)
    "IF THE G722 AND OPUS ALGORITHMS ARE NOT ALLOWED HERE AT THE GENERAL LEVEL OF THE SYSTEM, EVEN IF IN THE EXTERNAL GATEWAY SETTINGS, G722 IS ALLOWED, IT WILL NOT BE USED" (p612)
  summary: |
    八段主流程：①系统参数——Law（A 律欧洲/μ 律美国）+G722/OPUS 支持范围（System/Other System Param.：Network and local/not available/local only；系统级不开，网关开了也白开）；②SIP 中继组（类型 T2+Q931 变体 ISDN all countries+T2 Specification=SIP+DID 转码暂 No）；③外部 SIP 网关（SIP/SIP Ext Gateway：远端域/端口 5060/UDP/Belonging Domain/Registration ID+Timer 600/Outbound Proxy/所属中继组/Realm/账号密码/DNS 类型与地址/编解码开关 G711-G729-G722-OPUS/Gateway type Standard/P-Asserted 语义/SDP in 18x/Session Timer 及 UPDATE/RE-INVITE 方法）；④基础 ARS——前缀 0（ARS Prof. Trk Grp Seizure+逻辑鉴别符）→编号命令表（Command I=插余号+外部网关号）→ARS 路由表+路由（去 1 位加 33、关联命令表、Quality=Speech）→Time-based Route List（成本上限 -1）→真实鉴别符规则（0→Area1→ARS 表→位数 10）→Entity 鉴别符选择器（逻辑 0→真实 0；真实鉴别符必须已存在才能关联！）；⑤NPD/DID——默认 DID 翻译器（首外号 3321PN41000↔首内号 31000、范围 500）→NPD（双国际格式+默认号源 NPD+DID 0）→中继组 Public/Private NPD ID 指向它、Management Mode=Normal；⑥回叫规则（A33→00；国际 A→000；紧急 A15/A17/A18/A112→0——模拟器特设）；⑦国际表（去 00 不加位、鉴别符位数 255）与紧急表（不去位不加位、15/17/18 位数 2、112 位数 3）；⑧巡检——sipextgw -l/-g/-s、trkstat [-r]、dhs3_init -R SIPMOTOR 重启、ps 查 sipmotor 进程。
  conditions: 全流程按运营商参数定制（TC2005）；模拟器行为≠生产（多处 Warning）
  tags: [flow, sip-trunk, ars, npd, did, menu-path]

- id: f37
  title: SIP 网关双机备份与负载均衡两案（ARS 第二路由 / SIP Pool）
  type: flow
  source_pages: p641-656
  source_chapter: SIP Carrier access backup (How-To)
  source_quote: |
    "This second gateway will be used as backup of the first gateway … It can also be used for load-balancing purpose." (p642)
    "Pool Number: it is possible to specify the same index in 2 gateway that belong to the same provider. In this case in the ARS table it is necessary to create only one route with the first gateway and the CS will split the traffic between the gateways." (p652)
    "THE SUPERVISION TIMER IS IMPORTANT TO MONITOR THE GATEWAY, TO SWITCH ON THE OTHER ONE, IF THIS ONE IS OUT OF ORDER." (p651)
  summary: |
    两案可并存：案 1 ARS 备份——编号命令表 2 指向网关 2，三张 ARS 表（国内/国际/紧急）各加路由 2 并在 Time-based Route List 中排第二顺位；网关 1 失效自动走路由 2。案 2 SIP Pool——两网关 Pool Number 同值（1）+短 Supervision timer（例 5 秒）→CS 在池内分流量并原生互备；sippool 命令显示池内网关状态与上次使用（L/OOS 标记）。测试法：把网关 1 的 outbound proxy 改成错误 FQDN（gateway1.itsp1.bad）→sipextgw -l 显示 1 OOS、2 IN SERVICE→打外线并用 traced 验证走网关 2→测完必须改回！加速注册可 dhs3_init -R SIPMOTOR。
  conditions: 网关池仅适用于同一运营商的两个网关；两案互不冲突
  tags: [flow, sip-gateway, backup, load-balancing, sippool]

- id: f38
  title: 外呼闭锁操作链（真实鉴别符分区 + Public COS 放行 + Entity 影响）
  type: flow
  source_pages: p657-681
  source_chapter: EXTERNAL CALL BARRING RESTRICTION / Barring (How-To)
  source_quote: |
    "8 Logical discriminators are available for the system • 256 different Real Discriminators can be managed • 64 areas are available … 32 Access Classes Of Service" (p660)
    "Warning: modification of the user's entity can also have an impact on his barring • Different entity -> different real discriminator(s) -> different areas definition" (p667)
    "THE STATE (NIGHT, DAY, MODE 1, MODE 2) ARE THE ENTITY'S STATE. BY DEFAULT, AN ENTITY IS IN THE STATE NIGHT." (p674)
  summary: |
    配置链：①核对用户（General Characteristics→Entity；Rights→Public Network COS）；②核对 ARS 前缀逻辑鉴别符；③核对 Entity 鉴别符选择器（逻辑→真实映射）；④真实鉴别符分区——把 00 移到 Area 2、06/07 建 Area 3（各带 ARS 表号+位数）实现"分区域"；⑤Public COS 授权矩阵——Classes of Service/Access COS/<n>/Public Access COS/<Area>：Night/Day/Mode1/Mode2 各 0/1（默认实体处于 Night 态，只开 Day 不生效是高频错）；⑥换 Public COS 验证权限面变化；⑦换 Entity 验证鉴别符面变化（改 Entity 0 的逻辑 0→真实 1 后行为立即不同）。默认 Public COS 2 仅 Area 1 全放行。设计目标矩阵示例：COS2=紧急+本地+国内+国际全开；COS3=去国际；COS4=仅本地+紧急。
  conditions: 实体默认 Night 态是放行检查的第一前提
  tags: [flow, barring, public-cos, area, entity]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-29）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id |
|---|---|---|---|
| task-01 | 登录与账户密码治理 | 有 | f10（通道+四账户）；密码策略数值归 principle |
| task-02 | 系统启停与 autostart | 有 | f11 |
| task-03 | Call Server IP 双地址 | 有 | f12 |
| task-04 | 内部防火墙与可信主机 | 有 | f13 |
| task-05 | NTP/chrony | 有 | f14 |
| task-06 | 空数据库创建 | 有 | f15 |
| task-07 | OPS 许可与 FlexLM | 有 | f16 |
| task-08 | GD4 上架 | 有 | f17 |
| task-09 | OMS 上架 | 有 | f18 |
| task-10 | XL 机架上架 | 有 | f19 |
| task-11 | IP 话机静态/动态开通 | 有 | f21（f20 绑定模型） |
| task-12 | IPDSP 部署 | 有 | f20（绑定标识）+ f21 网络口径；安装步骤归 case |
| task-13 | User Profile 批量建户 | 部分 | f20（三法总框架）；逐步操作归 case c11 |
| task-14 | 数字/模拟用户 | 有 | f20（TDM 绑定） |
| task-15 | CS 内部 DHCP | 有 | f21（动态线） |
| task-16 | 编号计划 | 有 | f22 |
| task-17 | 两级 COS | 有 | f23 |
| task-18 | 语音指南与 MOH | 有 | f24 |
| task-19 | 话务台组与 4059EE | 有 | f25 |
| task-20 | Entity 与 CDT | 有 | f26 |
| task-21 | 4645 与邮件通知 | 有 | f27（部署拓扑）；SMTP 细节归 case |
| task-22 | 公共 SIP 中继 | 有 | f29, f30, f36, f37 |
| task-23 | 外呼闭锁 | 有 | f38（+f29 链路） |
| task-24 | 紧急呼叫通知 | 有 | f31 |
| task-25 | 呼叫分配计时器 | 有 | f32 |
| task-26 | 备份恢复 | 有 | f33 |
| task-27 | 维护工具箱 | 有 | f34 |
| task-28 | T0/T2 中继组 | 有 | f35 |
| task-29 | UMC 云管理 | 有 | f28（+f06 工具矩阵） |

**覆盖结论**：29/29 全部有框架类条目覆盖；f01-f09 为全书主线与环境/架构底座（不单独对应 task，是各任务的组织轴）；数值类细节（密码规则、限额表、计时器默认值、端口表）留待数值提取器（principle.md），逐步操作序列归 case.md。
