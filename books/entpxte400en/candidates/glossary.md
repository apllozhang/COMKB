# 术语/缩写/产品名候选 — OmniPCX Enterprise Starter (ENTPXTE400EN Ed12)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 60 条（concept 18 / role 9 / subscription 6 / product 17 / protocol 6 / resource 4）。PABX/ABC-F/DDI 等缩写书中未给全称处一律如实省略，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: OXE (OmniPCX Enterprise / PABX)
  category: concept
  source_pages: p30-31, p52
  source_quote: |
    "The OmniPCX Enterprise Communication Server or OXE is a Private Automatic Branch eXchange, known as 'PABX': • Software solution, based on a Linux Operating System • System based on an IP data network infrastructure" (p30)
  definition: |
    本书的宿主系统：基于 Linux 的软件 PABX，跑在 IP 数据网上；管内部通信与外线互通（去话/来话）。承载形态四种（见 g12-g14）；单 CS 上限 15000 用户/240 站点，网络式 100 节点/100000 分机。
  alias_or_related: "PABX"（书中直接给出的全称）；A4400（事件显示中的历史网络标识，p751）
  tags: [concept, core, pbx]

- id: g02
  term: Call Server (CS) / OXE-V
  category: concept
  source_pages: p31, p36, p52, p64, p129-131
  source_quote: |
    "The Call Server (CS), which is the system control center" (p31)
    "OXE virtualized Call Server is called OXE-V" (p64)
    "An IP address is linked to the CS physical interface (Ethernet) … This address can be used to access to the Call Server, whatever the Telephone Application status" (p129)
  definition: |
    系统控制中心：话务应用+数据库+OS 的宿主。物理形态为 CS-3 板；虚拟形态叫 OXE-V（VMware/KVM/Hyper-V/Nutanix/AWS）。寻址双体系：物理接口地址（永远可达）+ Role MAIN 地址（话务运行时生效、全网指向它）。主备复制=CS Duplication。
  alias_or_related: CS Main/Standby、Role MAIN/Stand-by；PCS（Passive Call Server，远端保命，Advanced 课程）
  tags: [concept, core, cs, virtualization]

- id: g03
  term: Media Gateway (MG) / IPMG
  category: concept
  source_pages: p31, p54-62
  source_quote: |
    "One or more Media Gateways (MG) supporting standard telephone equipment: • Voice guides • DTMF receptors • Conferences circuits • VOIP Compressors … • Lines for the public or private telephone networks" (p31)
    "Media Gateway 25 (also called « 1U », « Small » or « 3 positions ») … Media Gateway 80 (also called « 3U », « Large » or 9 positions)" (p54)
  definition: |
    承载媒体与接口的机架：1U Small=3 槽（MG25）、3U Large=9 槽（MG80），可内/外置电池；主机架最多带 2 个扩展架（GD-4 HSL↔EvolMEX）。板卡族：GD-4（0 槽网关驱动+30 压缩器）、GA-4（应用板）、EvolMEX、BRA8（8×T0）、PRA（T1/T2）、UAI16（数字）、SLI8/16（模拟 Z）、MIXED X/Y/Z。
  alias_or_related: 虚拟对应物 OMS（g13）；板名在 Common HW 带前缀 MG-（p247）
  tags: [concept, hardware, mg]

- id: g04
  term: MAO
  category: concept
  source_pages: p186-187
  source_quote: |
    "The database contains the customer's configuration • The OXE database is called MAO (Maintenance Administration Operation)"
  definition: |
    OXE 数据库的专有名（书中直接展开全称）：存客户配置。管理四工具=mgr/WBM/OV8770/UMC；运行态许可文件 software.mao 也位于 /usr3/mao 目录。
  alias_or_related: hardware.mao（OPS 兼容副本，g21）；config.mao（空库上限来源，p192）
  tags: [concept, database]

- id: g05
  term: Swinst menu (Easy / Expert)
  category: concept
  source_pages: p112-113, p122, p190-193, p213, p729
  source_quote: |
    "Via the « swinst » menu … 1 DECT registration 2 Backup database on cpu disk … 10 Stop the system" (p112)
    "FACILITIES Expert menu … 5 OPS configuration … 7 Database tools" (p213)
  definition: |
    swinst 账户下的安装设施菜单，系统级操作的总入口。Easy 10 项（DECT 注册/库备份/库恢复/库重建/OPS 备份/OPS 恢复/停话务/起话务/新互联网地址/停机）；Expert 9 项（Packages/Deliveries/Cloning/Backup & restore/OPS configuration/System management/Database tools/Software identity/Remote download）。root 下进入免密。
  alias_or_related: 与 RUNTEL（mtcl 命令）对照；菜单版本号随软件（示例 4.00.94）
  tags: [concept, swinst, menu]

- id: g06
  term: netadmin
  category: concept
  source_pages: p87, p136, p146-149, p364, p558-560
  source_quote: |
    "The netadmin tool can also be used to display the IP parameters: netadmin -m • Option 2 or Option 3 and sub-option 1" (p87)
    "Firewall ('iptables') is configured by using 'netadmin' tool menu • You must be logged as « root » to manage the OXE firewall" (p136)
  definition: |
    IP 网络管理工具（完整安装交互模式与菜单模式 netadmin -m）：节点/CPU/地址/掩码/域名/路由、Role 寻址、Security（iptables 防火墙、CHAP、ICMP、SSH/SSL、PKI、AIDE 等 13 项）、DHCP 查看/释放、DNS、SMTP、主机表、Apply modifications。防火墙管理与 SMTP/DNS/主机表必须 root（防火墙）或 mtcl（其余）。
  alias_or_related: 23 项主菜单（含 Tunnel/VLan/Encryption GW 等，本书只展开 2/5/9/11/12/21/23）
  tags: [concept, netadmin, network]

- id: g07
  term: WBM (Web Based Management)
  category: concept
  source_pages: p45, p232-237
  source_quote: |
    "Free embedded web-based management solution, no software to install, no additional licenses • Graphical interface for managing users and associated telephone services" (p45)
    "It does NOT search for a value managed. • Result is given in the page itself. • 3 characters minimum" (p236, 搜索功能)
  definition: |
    OXE 内嵌 Web 管理（HTML5，仅 HTTPS，https://<OXE IP>）：对象模型树+上下文菜单+过滤器排序+参数名搜索（不搜值）；Mass Provisioning 支持用户批量导入导出（首列 +/-/# 动作符、导入只填待改属性、不导密码）。本书实验的主力图形工具。
  alias_or_related: UMC 的 Expert Configuration 即云版 WBM（p810）；登录用 mtcl 凭据
  tags: [concept, wbm, management]

- id: g08
  term: Entity / CDT
  category: concept
  source_pages: p496-512
  source_quote: |
    "An entity is a logical subset of the OXE system … 2 entities created by default (Entity 0, Entity 1) … Entity IDs from '0' to '1000'" (p498-499)
    "Call Distribution Table (CDT) • One CDT dedicated to each entity … 4 different 'call distribution' status … A fourth 'overflow number' is common to the 4 status … commonly called 'night forwarding number'" (p500)
  definition: |
    Entity=OXE 逻辑分区（用户默认归 1、中继默认归 0），各带 CDT/状态/安装号/隐号/等待指南/留言箱/缩位区段；Attendant Group Manager 可让实体状态跟随话务组。CDT=四状态（Day/Night/Mode1/Mode2）×3 顺次路由+公共溢出号（须单线分机）。
  alias_or_related: Discriminator Selector（实体鉴别符映射表，g30）；状态代码 0-4（p524）
  tags: [concept, entity, cdt]

- id: g09
  term: COS (Phone Features COS / Connection COS / Transfer COS / Public COS)
  category: concept
  source_pages: p389-390, p413-419, p658-660
  source_quote: |
    "Assigned to users 256 categories are available • User rights • Set features • General services • PCX services • External services • Suffixes • Speed dialing areas • Miscellaneous parameters" (p390)
    "The Connection COS is used to authorize or forbid the connection between devices … Extension  Extension … Extension  Trunk … Trunk  Trunk" (p414)
    "The user's Public Network COS is used to control access possibilities to each area" (p659)
  definition: |
    三套类别体系：Phone Features COS（256 类，1=允许/0=禁止，管功能/保护/缩位区/摘机路由/默认溢出）；Connection COS 与 Transfer COS（矩阵式连转控制，用户侧同 ID、两张独立矩阵）；Public/Access COS（32 个，按 Area×实体状态管外呼）。
  alias_or_related: Access COS=Public Network COS 同义（p716）；缩位区 ≤400/每实体 ≤32 段
  tags: [concept, cos]

- id: g10
  term: Discriminator (Logical / Real / Area)
  category: concept
  source_pages: p579-580, p659-661
  source_quote: |
    "ARS prefix (ARS professional Trunk Group Seizure) • Information -> Logical discriminator (0<->7)" (p579)
    "A 'Real Discriminator' that contains the complete 'External Numbering plan' • This discriminator is divided into several areas • Usually a 'Barring Area' corresponds to a geographical telephone Area code" (p659)
    "8 Logical discriminators are available … 256 different Real Discriminators … 64 areas are available" (p660)
  definition: |
    闭锁/路由的中枢概念：逻辑鉴别符（0-7，挂在 ARS 前缀或 TG 的 Number compatible with 上）→ 实体选择器映射 → 真实鉴别符（0-255，外呼计划全集，条目=号码+Area+ARS 表+位数）→ Area（1-64）交 Public COS 决定放行。真实鉴别符未创建时不能在实体做映射。
  alias_or_related: 与 ARS（g28）、Barring（n25/n26 边界）强绑定
  tags: [concept, discriminator, barring]

- id: g11
  term: Trusted hosts (iptables)
  category: concept
  source_pages: p137-139, p157-163
  source_quote: |
    "Any host added in OXE's trusted hosts list is fully trusted by OXE. That is the hosts allowed to communicate to OXE with all its open ports and services, of course after authenticating" (p137)
    "TRUSTED_HOST,<Hostname>,<IP Address> … TRUSTED_RANGE,<First IP Address>,<Last IP Addres>" (p139)
  definition: |
    OXE 防火墙白名单机制：N3 起默认无主机可入站，互通全靠可信主机（单个/网段/域名/CSV 批量）；入列=全端口全服务放行（服务自身认证仍生效）。DHCP 池地址自动入列且来源 MAO 不可经 netadmin 修改。
  alias_or_related: Allow/Deny SSH for all（临时便门）；Bulk Export 固定 /tmpd/export_th.csv
  tags: [concept, firewall, security]

- id: g12
  term: GAS (Generic Appliance Server)
  category: concept
  source_pages: p67-68, p86
  source_quote: |
    "Generic Appliance Server (GAS) • Virtualized OXE Call Server on top of Rocky Linux KVM layer • Hardware agnostic • Dedicated platform provided by ALE or BP … Dongle-less package with license control based on the ALU-ID of the server or the OXE Cloud Connect ID" (p68)
  definition: |
    Rocky Linux+KVM 之上的 OXE 一体化载体：OXE VM+可选 WebRTC VM(Debian)+OMS VM，FlexLM 直装于 Rocky Linux；免加密狗、按 ALU-ID 或 Cloud Connect ID 控许可。访问=VGA 控制台/VMM 或 SSHv2。
  alias_or_related: 许可 ID 家族见 g22；hypervisor 对照见 p64 表
  tags: [concept, gas, virtualization]

- id: g13
  term: OMS (OXE Media Service)
  category: concept
  source_pages: p65, p259-268
  source_quote: |
    "OXE MS, the OmniPCX Enterprise software Media Gateway is natively virtualized … This soft media-gateway provides media processing features of a GD-4 board • 120 compressors • VoIP codecs (G711, G722, G729 & OPUS (WB &NB)) • OPUS & G722 codecs are not available on hardware IPMG" (p65)
  definition: |
    原生虚拟化的软件媒体网关（Rocky Linux VM 的 ALE SW 包）：等价 GD-4 媒体功能——120 压缩器、G711/G722/G729/OPUS（后两种硬件 IPMG 没有）、会议/指南/音调/转码/RTP DTMF；可与物理 MG 混跑。许可锁 #384（台数）/#385（通道总数）。
  alias_or_related: 配置入口 omsconfig（root）/sudo omsconfig（admin）；Shelf 四强制字段见 n16
  tags: [concept, oms, virtual-mg]

- id: g14
  term: Crystal hardware / XL-Media Gateway
  category: concept
  source_pages: p69-78
  source_quote: |
    "ACT (Alcatel-Lucent Crystal Technology) contains the boards … M2 unit capacity: 1 ACT '28 positions' or 2 ACT '14 positions'" (p70)
    "BACK-XL : 14-slot backplane • Targets the high-density analogue subscriber lines segment which was previously addressed by the OmniPCX Enterprise crystal hardware" (p74)
  definition: |
    Crystal=旧高密度硬件（ACT 板/M2/M3 单元/CPU8），因元器件稀缺退场、书中自注不再深入；XL 机架=19" 6U/14 槽背板补位：2 个半架各由 GD-XL 驱动 6 块 FXS32-XL，整架 ≤384 FXS，奇数机位创建，-48Vdc 外置整流器供电。
  alias_or_related: FXS=Foreign eXchange Subscriber（p75 直接展开）；GA-XL 双角色板
  tags: [concept, crystal, xl, hardware]

- id: g15
  term: Role addressing / 双 IP 地址
  category: concept
  source_pages: p129-131, p147-148
  source_quote: |
    "Second IP address can be managed to the 'role MAIN status' of the system Telephone application • This second address is activated (and usable) only when the Telephone Application is started" (p129)
    "Name used when the CPU role is MAIN (default is xma000000) ? csm … Address used when the CPU role is MAIN ? 192.168.1.3" (p148)
  definition: |
    CS 双地址模型：物理接口地址（任何时刻可达，话务停止后唯一可用）+Role MAIN 地址（话务运行时激活，设备与外部应用统一指向；主备共享）。同子网主备=本地冗余、跨子网=空间冗余（Advanced）。配置在 netadmin -m → 5 Role addressing。
  alias_or_related: 与 n08（恢复时必须用物理地址）强关联
  tags: [concept, ip, role]

- id: g16
  term: chrony / NTP
  category: concept
  source_pages: p167, p170-173
  source_quote: |
    "Since OXE R101, the 'chrony' tool is implemented in the OXE O.S. • « chrony » is a versatile implementation of the Network Time Protocol (NTP)" (p167)
    "The use of NTP protocol, via the 'chronyd' process, allows the synchronization of the date and time of several stations in a network • The IP network carries the time messages according the RFC 1305 standard" (p170)
  definition: |
    OXE 时间同步实现：chrony（R101 起）承担渐进同步（client/server、UDP 123、stratum 分层、可对称密钥认证），OXE 可同时作客户端与服务器；瞬时同步为一次性人工操作（须先停 chronyd）。系统时间=UTC+时区+夏令时。
  alias_or_related: 与 g35 RFC 1305 相邻；swinst NTP 菜单七项
  tags: [concept, ntp, chrony, time]

- id: g17
  term: Degraded mode / PANIC flag
  category: concept
  source_pages: p204-206, p154, p220
  source_quote: |
    "When the Call Server software detects an incoherency between the different keys or with the features, it switches to the degraded mode and triggers some actions" (p204)
    "the 'Panic flag' is set up and the system behaviour is impacted. • The phases of this degraded mode are: Action 1 … Action 2 (4 hours later) … Action 3 (8 hours later)" (p206)
  definition: |
    许可不一致的降级运行态：PANIC flag=1（spadmin 可查，另有 Panic Flex/SWK/RTR 三旗标）；三阶段动作（即时话务台告警+命令锁→4 小时全屏提示+禁内呼→8 小时循环）；CPU-ID 不一致给 30 天宽限。恢复合法 OPS 后归零。
  alias_or_related: 与 g21 OPS、g22 RTR 同族
  tags: [concept, licensing, degraded]

- id: g18
  term: Attendant / Attendant group / 4059 EE
  category: concept
  source_pages: p33, p449-463, p464-478
  source_quote: |
    "The attendant is the basic call reception element; he/she receives external and internal calls." (p33)
    "Minimum of one Attendant group per OXE … Number of attendant groups per node: 50" (p451)
    "The operator console 4059 Extended Edition includes • A dedicated ergonomic USB keyboard with attendant functions • A desktop application" (p465)
  definition: |
    话务体系三层：Attendant group（≤50/节点，并行/轮转呈现，互援+溢出门限）；Attendant set（≤250/节点，必须属组，位置 Idle/Busy/Unplugged/Absent）；终端=ALE-300/400/500 或 4059 EE PC 坐席（专用 USB 键盘+软件，语音由关联话机/IPDSP 承载，BLF/Rainbow 集成/Call by name/S-F 键）。
  alias_or_related: CDT 四状态分配；BLF 用户监视 ≤5 设备聚合
  tags: [concept, attendant, 4059ee]

# ── 二、角色/账户 (role) ──

- id: g19
  term: mtcl
  category: role
  source_pages: p88, p90
  source_quote: |
    "mtcl: maintenance account (ex. maintenance commands, database configuration…)" (p88)
    "The 'root' and 'mtcl' accounts use a none configurable 900 seconds inactivity timer" (p90)
  definition: |
    维护账户：日常 CLI（role/config/trkstat/sipextgw/mgr 等）、su - 至 root 的跳板、SFTP 文件传输（OPS/备份/指南/防火墙 CSV）的默认身份。900 秒无操作超时。
  alias_or_related: 实验口令 Administrator5689!（实验口径）
  tags: [role, account]

- id: g20
  term: swinst
  category: role
  source_pages: p88, p100, p112
  source_quote: |
    "swinst: 'Facilities' account (ex. Backup & Restore operations, date & time…)" (p88)
    "When you run the 'swinst' menu from the 'root' account, the 'swinst' password is not required." (p100)
  definition: |
    Facilities 账户+同名菜单入口：系统启停、autostart、备份恢复（库/OPS）、空库创建、日期时区、NTP 管理、账户管理（client 建户/改密/锁定/老化）。root 下进入免密。
  alias_or_related: Easy/Expert 双菜单见 g05
  tags: [role, account]

- id: g21
  term: root
  category: role
  source_pages: p88, p90, p99
  source_quote: |
    "root: Administrator account, expert maintenance (ex. security management…)" (p88)
    "IT IS POSSIBLE TO CONNECT DIRECTLY VIA THE ROOT ACCOUNT ONLY IF YOU USE A LOCAL ACCESS (SERIAL CONNECTION, KVM, …)" (p99)
  definition: |
    管理员/专家账户：防火墙 iptables 管理、passwd 改任意账户、tcpdump/infocollect、OMS/GDXL 板侧 su。仅本地（串口/KVM）直登，IP 侧必须 mtcl→su -。
  alias_or_related: 实验口令 Superuser2580*（实验口径）
  tags: [role, account, security]

- id: g22
  term: client
  category: role
  source_pages: p88, p101-102
  source_quote: |
    "client: Account with basic access (ex. basic maintenance commands) • Disabled by default, can be activated via swinst menu • Note: To use 'client' account, telephone application must be running" (p88)
    "MENU CLIENT - Exit : 0 - Data Base : 1 - Network Maintenance : 2 - Resources Maintenance : 3 - Financial Report : 4" (p102)
  definition: |
    基础访问账户：默认禁用，经 swinst（Expert→System management→User's accounts management→Create）启用；登录前提是话务应用运行中；菜单仅五项（退出/数据库/网络维护/资源维护/财务报表），mgr 仅英文。
  alias_or_related: 与 g19-g21 并列四账户
  tags: [role, account]

- id: g23
  term: Attendant (话务员角色)
  category: role
  source_pages: p460-463, p502, p517
  source_quote: |
    "The attendant may be in one of the following positions: Idle … Busy … Unplugged … Absent" (p461)
    "Attendants belonging to this group can modify the entity status • Manually, from the attendant console • Rights must be granted to the attendant" (p502)
  definition: |
    基础来话接收角色：能力覆盖电话操作（转接/单独保持/链式呼叫/监督）、服务访问（客户管理/计费/系统管理如日期时间/分配状态）、自定义键盘（F1-F12/S1-S8）；在权限内可从控制台手动切换 Entity 状态。
  alias_or_related: 与 g18 组结构互补；Absent 由 Timer 76 触发
  tags: [role, attendant]

- id: g24
  term: kb (OMS 键盘账户)
  category: role
  source_pages: p261
  source_quote: |
    "To modify the keyboard layout, log as 'kb' account • Login: kb • Password: kb … == Use 'kb' as login and password to perform keyboard layout change (default: us)."
  definition: |
    OMS 虚拟机专用低权账户（kb/kb）：仅用于修改 VM 键盘布局（Rocky Linux 9.6 控制台）。
  alias_or_related: 与 GD4/OMS 的 admin/root 无关
  tags: [role, account, oms]

- id: g25
  term: admin / root（媒体网关板侧）
  category: role
  source_pages: p248, p262, p759
  source_quote: |
    "o V24 speed is 115200 bauds … default passwords: admin [letacla1] and root [mg4.ale]]" (p248, GD4)
    "o Only 'admin' account is accessible ▪ ssh admin@<GD4 IP @> … 'root' account is not accessible (use 'su' command from 'admin' account)" (p248)
  definition: |
    GD4/GDXL/OMS 板载双账户：V24 控制台可用 admin+root；SSH 只暴露 admin 且仅可从 CS 发起（需 ippstat/mgconfig/omsconfig 授权），root 经 su。首连强制改密。
  alias_or_related: 默认口令差异见 n15；配置命令 mgconfig/omsconfig
  tags: [role, account, hardware]

- id: g26
  term: trainer / IT Server 账户（training/superuser）
  category: role
  source_pages: p9, p178, p566
  source_quote: |
    "IT SERVER ENTP_ITSERVER itserver 192.168.1.252 … training superuser NTP Server" (p9)
    "Open the 'NTP server' console; log as: training/superuser (login/password)" (p178)
  definition: |
    实验环境角色：IT Server（NTP+邮件服务器 192.168.1.252）的登录账户 training/superuser；NTP 实验从其控制台对时。纯教学基础设施。
  alias_or_related: 实验口径；Thunderbird 实验密码 alcatel 亦为实验口径
  tags: [role, lab]

- id: g27
  term: IPDSP user（4059EE 关联语音用户）
  category: role
  source_pages: p310, p482-484
  source_quote: |
    "Create an IP DSP User … Directory number: 31003 … Warning: This extension must not be multi-line" (p482)
    "Associated phone set 31003 (this set must be created previously: physical set or softphone)" (p484)
  definition: |
    4059EE 话务台的语音承载方：一台物理话机或一个 IPDSP 用户（IPTouch 8068s+IP-Softphone emulation=Yes），挂在 Attendant set 的 Associated phone set 字段；禁 multiline。
  alias_or_related: 与 g18/g27 绑定；登记回填见 /Attendant/Attendants sets/Ip phone Attendant
  tags: [role, attendant, ipdsp]

# ── 三、许可/订阅 (subscription) ──

- id: g28
  term: OPS（许可文件组）
  category: subscription
  source_pages: p196, p207-208
  source_quote: |
    "Purchase of licenses results in delivery of OPS files … The OPS files are the following: • hardware.mao • Copy of the xx.hw file … • xx.swk • Contains the listing of customer licenses and software locks • xx.hw • Contains the hardware description … • xx.zip • Archive used by Actis" (p196)
  definition: |
    许可交付物四件套（xx=客户 ID）：xx.swk（锁清单）、xx.hw（硬件描述）、hardware.mao（兼容副本）、xx.zip（Actis 归档）。恢复=传 /usr4/BACKUP/OPS+swinst 恢复（.swk 改名 software.mao）；备份=swinst 备份+SFTP 取回。空库会连同 OPS 一起抹除。
  alias_or_related: 锁值语义 0/1 与 0-99999/99999；与 g29/g30/g31 同族
  tags: [subscription, licensing, ops]

- id: g29
  term: Software locks / spadmin
  category: subscription
  source_pages: p199, p220-221
  source_quote: |
    "Each lock has a maximum value that depends on the xx.swk file … 'spadmin' command can be used to display locks" (p199)
    "384 OXE Media Servers = 3 … 385 VoIP channels on OMS = 120 … 424 Native Encryption Users = 75 … 430 SipSoftPhone = 10" (p199)
  definition: |
    功能锁计量：服务授权型 0/1、数量型 0-99999、99999=无限。spadmin 十项菜单管查看/校验/安装/CPUID/PANIC。书内示例锁号：135（压缩器）、178/179/182/183/194（4645 族）、384/385（OMS）、424（原生加密）、430（SIP 软话机）、467（ARS）、469（G723.1）。
  alias_or_related: CAPEX 模式下的本地锁载体
  tags: [subscription, licensing, locks]

- id: g30
  term: CAPEX / OPEX
  category: subscription
  source_pages: p197-198, p154, p813
  source_quote: |
    "• CAPEX • Software locks controlled locally (in the OXE) … • OPEX (except hardware items) • Software locks controlled in an external LMS server (Cloud)" (p198)
    "OPEX Flag : 0" (p220, spadmin 输出)
    "Active OXE SPS Contract (CAPEX) • Active PoD Subscription (OPEX)" (p813)
  definition: |
    许可双轨：CAPEX=锁在本地 OXE（xx.swk 绑 CPU-ID/Product-ID/ALU-ID）；OPEX=锁在云端 LMS（Communication Suite for MLE、Purple on Demand，OXE R100.1 起；硬件仍 CAPEX）。商务前提：CAPEX 需 SPS 合同、OPEX 需 PoD 订阅（UMC 前提）。
  alias_or_related: spadmin 输出中 "New file in CAPEX"、OPEX Flag 字段
  tags: [subscription, licensing, capex, opex]

- id: g31
  term: RTR (Right To Run) / CC-SUITE-ID
  category: subscription
  source_pages: p200, p44, p813
  source_quote: |
    "License control for OXE is based on a Cloud Connect Operation identifier • Use of Cloud Connect Infrastructure (CCI) to offer the Right To Run service • Based on a CC-SUITE-ID • Syntax: ADCBE-FGHIJ-KLMNO-PQRST • This ID Remains the same during the product life time" (p200)
    "Connected platform … - Right to Run (RTR) - Based on a Cloud Connect product identity" (p44)
  definition: |
    运行权校验：经 Cloud Connect 永久连接到 ALE 云平台核查；CC-SUITE-ID 形如 ADCBE-FGHIJ-KLMNO-PQRST、终身不变；OXE 必须处于云连接（FTR&RTR running）才算就绪（UMC 前提）。spadmin 的 Panic RTR Check 旗标对应此项。
  alias_or_related: Cloud Connect（g37）；与 g32 Product ID 家族并列
  tags: [subscription, licensing, rtr, cloud]

- id: g32
  term: CPU-ID / Product ID / ALU-ID（许可标识三态）
  category: subscription
  source_pages: p197, p201-203
  source_quote: |
    "'CPU-ID' for physical CS • 'Product ID' for virtual CS • 'ALU-ID' for Generic Appliance Server (GAS)" (p197)
    "This ID is stored in the PROM* for each CPU board (CPU-Id)" (p201)
    "A '.ice' license file is deployed on FlexLM server • This file contains the 'Product-ID' and It is linked to the 'dongle-ID' … 'ALUID' controlled by the FlexLM server" (p202-203)
  definition: |
    按载体的许可锚点：物理 CS=CPU-ID（PROM 内，Actis 订购）；虚拟 CS=Product ID（FlexLM 的 .ice 绑 USB Dongle-ID，需加密狗）；GAS=ALU-ID（免狗，FlexLM 内嵌）。CC-SUITE-ID 为全载体通用替代（Cloud Connect）。
  alias_or_related: ACTIS=Alcatel-Lucent Configuration Tool for International Sales（p201 展开）；FlexLM 见 g36
  tags: [subscription, licensing, ids]

- id: g33
  term: SPS Contract / PoD（Purple on Demand）
  category: subscription
  source_pages: p44, p198, p813
  source_quote: |
    "▪ OXE Release status ▪ SPS contract status" (p44, Cloud Connect 功能)
    "Purple on Demand … OXE R100.1 min" (p198)
    "• Active OXE SPS Contract (CAPEX) • Active PoD Subscription (OPEX)" (p813)
  definition: |
    商务侧两凭证：SPS 合同（CAPEX 体系的有效服务合同，Cloud Connect 可查状态）；PoD=Purple on Demand（OPEX 订阅，OXE R100.1 起支持）。UMC 访问的商务前提。
  alias_or_related: 与 g31 RTR 同属 Cloud Connect 核验内容
  tags: [subscription, commercial]

# ── 四、产品/组件名 (product) ──

- id: g34
  term: CS-3 / GD-4 / GA-4 / EvolMEX（Common HW 板卡族）
  category: product
  source_pages: p56-59
  source_quote: |
    "CS-3 board (Communication Server) • Is the OXE 'brain' … LAN1 and LAN2 support Ethernet Redundancy (Active/Stand-by)" (p56)
    "Gateway Driver Version 4 called GD-4 Board • Controls the Media Gateway (always in slot '0') … Voice over IP (30 compressors on the motherboard)" (p57)
    "GA-4 board • Applicative board which provides additional processing resources … SLANX: optional daughterboard providing a 4 ports 10/100BT LAN switch • This switch cannot be configured" (p58)
  definition: |
    Common HW 板卡四件：CS-3（大脑，LAN 冗余+4 口交换+V24）；GD-4（0 槽网关驱动：30 压缩器/音调/指南/会议/DTMF；子板 HSL1/HSL2/ARMADA）；GA-4（应用板：30 压缩器/三方会议/指南；子板 ARMADA、SLANX）；EvolMEX（扩展架驱动，支持 HSL1）。
  alias_or_related: 与 OMS（g13）软件等价物对照；BRA/PRA/UAI/SLI/MIXED 接口板并入本条
  tags: [product, boards, hardware]

- id: g35
  term: ALE 话机系列（ALE-2/3/20/20h/30/30h/300/400/500、8008/8088v3）
  category: product
  source_pages: p32, p271-284
  source_quote: |
    "SIP ENTRY DESKPHONE - ALE-2 … Communication protocol SIP • Built-in VPN client for work from home Secure SIP" (p281)
    "ALE-3 … Same functional level as ALE-2 • PoE class 2, 802.3az … The remote worker use case is currently not supported" (p282)
  definition: |
    话机族谱：SIP 入门 ALE-2/ALE-3（SIP-only）；Essential ALE-20/20h/30/30h（NOE IP 或 TDM 混合）；Enterprise ALE-300/400/500（SIP 或 NOE IP，触屏 3.5-5.5 寸，AOM/VPN/蓝牙手柄）；8008(G)(CE)/8088v3（触屏/Android/Rainbow）。配套 ALE-120/EM200 扩展、键盘/墙挂/定制套件。协议标注（1)NOE IP (2)NOE 双模 (3)SIP (4)SIP或NOE (5)SIP或模拟。
  alias_or_related: 参数表归产品目录（OVERVIEW 不适合清单）；DECT 8214-8262EX、WLAN 8158s/8168s 同页
  tags: [product, phones]

- id: g36
  term: IPDSP (IP Desktop Softphone)
  category: product
  source_pages: p287-289, p308-314
  source_quote: |
    "The IP Desktop Softphone offers all the 8068s Premium DeskPhone features on PC, Mac or Android" (p288)
    "OPUS, G.711, G722 and G.729 codecs are supported • QoS Level 3 IP TOS / DSCP • Compliant with native encryption • Outlook plug-in • TEL protocol available" (p288)
  definition: |
    ALE 软话机（Windows/Mac/Android）：全量 8068s 特性；商旅/坐席两用、CTI/VDI 兼容；编解码 OPUS/G711/G722/G729；原生加密兼容；网络口径=TFTP/HTTPS 拉 lanpbx.cfg+端口表（principle p20）；AOM 键盘类型须与 OXE 一致。
  alias_or_related: 与 ALES（ALE Softphone，Windows/Android/iOS）区分；Rainbow 为另一软话机品牌（本系列教材仅点名）
  tags: [product, softphone, ipdsp]

- id: g37
  term: Cloud Connect / Fleet Dashboard
  category: product
  source_pages: p44, p200, p813
  source_quote: |
    "Fleet management and automation ▪ OXE Release status ▪ SPS contract status ▪ Retrieve Actis File … ▪ Software download ▪ License download … - Native secure connection to Cloud Connect - OXE Licenses control - Right to Run (RTR)" (p44)
  definition: |
    ALE 云侧设备管理与运行权平台：连接状态/版本/SPS/Actis/VM 许可/告警（最近 100 条）/软件与许可下载；Fleet Dashboard 提供机队视图并是 UMC 的入口之一（OXE 侧经 CPU-id → Access UMC）。深度内容在 ENTPXTE402。
  alias_or_related: MyPortal（OPEX 入口）；RB WebAdmin/Fleet 术语见 RAINXTE 教材
  tags: [product, cloud, cloud-connect]

- id: g38
  term: OmniVista 8770
  category: product
  source_pages: p46, p238-241, p782
  source_quote: |
    "Single interface for managing users, terminals and unified communications services (client or web interface) … Synchronization with enterprise directory • Microsoft Active Directory synchronization • A single platform for managing multiple systems" (p46)
    "CONFIGURATION TREE NETWORK PCX HARDWARE DEVICES & USERS SUB-NETWORKS" (p240)
  definition: |
    集中式管理系统：Java 客户端+HTML 目录应用；管理档案委派/账务/实时告警/AD 同步/VoIP 质量监控/多系统平台；配置树五分区（NETWORK/PCX/HARDWARE/DEVICES & USERS/SUB-NETWORKS）；T0 实验用它核板。
  alias_or_related: Mass Provisioning 规则与 WBM 相同（p237）；UMC 为其云侧继任方向
  tags: [product, management, omnivista]

- id: g39
  term: UMC (Unified Management Center)
  category: product
  source_pages: p47, p242-243, p797-814
  source_quote: |
    "Unified Management Center (UMC) offers a secure, cloud-based management platform … UMC is accessible via MyPortal (OPEX system) or Fleet Dashboard (OPEX or CAPEX)." (p798)
    "Expert configuration • Cloud WBM • Without the need of LAN access to connect to OXE" (p810)
  definition: |
    云管理平台 R1.1：Easy users（Profile 建户/MultiDevice/按键/群组）、Easy SIP trunk（向导+约 120 架构 Profile，含 WebRTC GW/VAA 私有中继）、Expert Configuration（云 WBM）；法国 OVH 机房、TLS1.2、ISO/IEC 27001。前提与排除项见 n39/n40。
  alias_or_related: 语言 EN FR SP DE；浏览器 Chrome/Firefox/Edge
  tags: [product, umc, cloud]

- id: g40
  term: mgr
  category: product
  source_pages: p226-230
  source_quote: |
    "'mgr' is one of the management tools • 'mgr' stands for 'Manager' • It is integrated in the Communication Server (CS) • Used for the management of the database • Shelves, boards, users, etc… • This tool is working in text mode" (p227)
    "Under the 'mtcl' account • Enter the command 'mgr -l XXX' … ESC … keyboard mapping … 'CTRL V' means 'Validate' … 'CTRL C' means 'Cancel'" (p228-230)
  definition: |
    CS 内置文本模式数据库管理器：机架/板卡/用户等全对象管理；mtcl 下 mgr -l <语言> 启动（client 账户走菜单 1+2、仅英文）；ESC→keyboard mapping 查快捷键（CTRL V 确认/CTRL C 取消）。SIP 中继实验建议用 mgr 或 WBM。
  alias_or_related: 与 swinst（设施菜单）、netadmin（网络）并列为三大 CLI 工具
  tags: [product, mgr, cli]

- id: g41
  term: OmniMessage 4645 / Audio-Station / Eva_tool
  category: product
  source_pages: p39, p526-546, p547-556
  source_quote: |
    "Alcatel-Lucent Omni Message 4645 • Pure Software Voice Mail Solution" (p39)
    "The basic voices guides can be recorded by the 'Alcatel Audio-Station' (no recording from sets)" (p528)
    "Command Eva_tool … 5 : Dump nodes, mailboxes and messages … 17 : VM Directory number for Email notification" (p554, p563)
  definition: |
    纯软件语音邮件（多服务语音应用）：四拓扑部署、集中留言+VPIM 组网、DTLS/SRTP 加密、IMAP4+邮件通知；管理面=WBM Applications/Voice Mail + Eva_tool（信箱/口令/问候导入/端口/通知号码）；基础指南录制专用 Audio-Station 工具。
  alias_or_related: A4645-V=虚拟化免狗版本（p537）；安全文档 SA0046/TC1774
  tags: [product, voicemail, 4645]

- id: g42
  term: ITSP1 SIP Simulator / MicroSIP
  category: product
  source_pages: p10, p21-26
  source_quote: |
    "SIP SIMULATOR OVERVIEW - ITSP1 WITH 2 SIP GATEWAYS … ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 … ITSP1 Public gateway public.itsp1.com 10.20.30.50" (p22)
    "2 MicroSIP softphones are installed to simulate public numbers." (p10)
  definition: |
    培训专用运营商模拟器：两条 SIP 网关腿+公网网关（MicroSIP 扮演 Public/Emergency 用户）；PBX 注册账号 pbxP/alcatel、域 sip.itsp1.fr。ITSP2 仅拓扑图出现。生产行为差异（安全/编解码/号码格式/紧急显示）见 n29。
  alias_or_related: RLAB 公共资源区（12.0.0.2）；PN=两位 POD 号
  tags: [product, lab, simulator]

- id: g43
  term: OXE 内部防火墙（iptables）
  category: product
  source_pages: p134-144
  source_quote: |
    "A full-fledged firewall, using 'iptables', is implemented in OXE since OXE R101.0" (p135)
    "1. 'Firewall(iptables) Configuration' … 4. 'Enable/Disable iptables logs'" (p136)
  definition: |
    OXE 内嵌状态防火墙：INPUT/FORWARD 默认 DROP、OUTPUT ACCEPT；配置入口 netadmin→Security→Firewall（View/Allow-Deny SSH/Restricted Access/日志）；有 iptables 日志开关；RADIUS/SSH/SSL/PKI 等同为 Security 子菜单项。
  alias_or_related: 可信主机语义 g11；DHCP/DNS 联动 n21
  tags: [product, firewall, security]

- id: g44
  term: oxetrace / infocollect / securitystatustool（维护工具三件）
  category: product
  source_pages: p740-746, p753-754
  source_quote: |
    "The 'oxetrace' tool is able to take Call Handling, SIP motor and network traces simultaneously and archive into the path given by the user" (p740)
    "The tool is intended to get most of the pbx logs, ip & telephone configuration for an 'off-line' analysis … Must be run under root" (p754)
    "SSH configuration and SSL certificate details • Isolation / trusted hosts information … • Identify the ratio of users with the default secret code" (p753)
  definition: |
    排障三主力：oxetrace（菜单式三路抓包+解码+打包 zip）；infocollect（root 运行，离线分析大包 .tbz，技术支持标配）；securitystatustool（XML 安全全景：SSH/证书/NTP/syslog/密码策略/默认密码占比/4645 策略，需话务运行）。
  alias_or_related: ippstat/incvisu/incinfo/syslog/tcpdump 并入 g45 或 c32
  tags: [product, maintenance, tools]

- id: g45
  term: ippstat / termstat / trkstat / sipextgw / sippool（巡检命令族）
  category: product
  source_pages: p328, p335, p637-639, p652-653, p748
  source_quote: |
    "Command tnet d <directory number>" (p328)
    "'termstat' command … [1] : Device features. … [5] : Reset the device." (p335)
    "Use the command sipextgw: Option '-l' provides the list of external gateway(s) … '-g' provides the parameters … '-s' … dialing command tables" (p637-638)
  definition: |
    CLI 巡检族：ippstat（IP 话机 1-22 项，-noname 供 GDPR）；termstat/eqstat（终端状态，d/n/p 三语法）；trkstat [-r]（中继通道状态）；sipextgw -l/-g/-s（网关注册/参数/引用）；sippool（池内网关状态与 L/OOS 标记）；tnet d（SSH 上话机）；dhcplease（DHCP 租约）；rstcpl/config/cplstat/listerm/listout（硬件族，见 c08）。
  alias_or_related: 全部在 mtcl/root 下运行；语法差异见各实验
  tags: [product, cli, maintenance]

- id: g46
  term: 4059 EE（4059 Extended Edition）
  category: product
  source_pages: p464-478
  source_quote: |
    "An IP Desk phone or an IP Desktop Softphone is necessary to manage audio and headset connection. • 20 languages are available" (p465)
    "Call Queues can show 'Incoming calls' and 'CampOn' queues … 'CampOn' queue is a combination of 'Routing queue' (transferred calls) and 'Holding queue' (individual parked calls)" (p474)
  definition: |
    PC 话务台（专用 USB 键盘+坐席软件）：呼叫处理窗/队列（Incoming+CampOn）/文本输入（Call by name/LDAP）/S-F 工具条（可映射普通键盘）/拖拽拨号（超长自动加前缀）/BLF/Rainbow 集成与消息模板/20 语言；声明为 Set Type=4059 IP。
  alias_or_related: 语音承载=Associated phone set（g27）；abcacom.exe 防火墙放行（n24）
  tags: [product, attendant]

- id: g47
  term: SIP External Gateway（外部 SIP 网关）
  category: product
  source_pages: p577, p614-615, p637
  source_quote: |
    "The SIP provider must supply all the information to configure the external gateway on the system: • Installation number • Calling and called number format • Emergency calls • Fax calls" (p577)
    "SIP Outbound Proxy Specify the address of the carrier server. … Pool Number: it is possible to specify the same index in 2 gateway that belong to the same provider." (p615, p652)
  definition: |
    面向运营商的 SIP 网关对象：远端域/端口/传输、Belonging Domain、Registration ID+Timer、Outbound Proxy、Realm 与凭证、DNS 类型、编解码开关、P-Asserted 语义、SDP in 18x、Session Timer/方法、Pool Number、P-ANI Header、Gateway type（Standard/ICE）。巡检 sipextgw。
  alias_or_related: 与 TG（g48）成对；参数语义表 principle p30
  tags: [product, sip, gateway]

- id: g48
  term: Trunk Group（T0/T2/SIP 中继组）
  category: product
  source_pages: p35, p573-576, p773-779
  source_quote: |
    "The OXE supports a large range of trunk groups: • SIP • T0, T2, T1 • ISDN (France or All countries) • QSIG … • ABC-F … • Analog (NDDI, Loop start, Ground start) • ABC-F on IP" (p35)
    "Maximum number of accesses per SIP Trunk Group: 32 (always by pair)" (p576)
  definition: |
    中继组对象：索引/逻辑鉴别符/信令变体（ISDN all countries、QSIG、ABC-F）/规格（IP/SIP）/DID 翻译器/发送位数/去位数/实体/连接类别/Public COS。SIP 型 32 接入成对、62 通道每对（Mini 4 通道）；T0=2B+D 每口、T2=30 通道；同步优先级 0-199（Crystal）/200-254（IP）/255 不同步。
  alias_or_related: ABC-F=OXE 间链路（书中未展开全称）；QSIG 三档并列
  tags: [product, trunk-group]

# ── 五、协议/技术 (protocol) ──

- id: g49
  term: ABC-F / ABC Direct IP / Direct Link
  category: protocol
  source_pages: p35, p38, p192, p539
  source_quote: |
    "ABC-F (for Links between OXE systems) … ABC-F on IP" (p35)
    "Nodes interconnected through ABC Direct IP links • A high level of feature transparency (ABC* protocol) … * ABC for Alcatel Business Communication" (p38)
    "Enter 'Y', to allow the automatic creation of 'Direct IP Links' in the OXE database. These 99 links are used in ABC-F Network topology" (p192)
  definition: |
    OXE 间组网协议族：ABC=Alcatel Business Communication（书中展开）；ABC-F 支持 Basic/Generic/Supplementary 分级，含 IP 承载（ABC-F on IP）；Direct IP Link 为节点直连（Location ID/P-ANI 的强制前提，也是空库 Direct Link Network 参数的对象——自动建 99 条）。
  alias_or_related: 混合链（hybrid link）不支持 Location ID（n32）；组网细节在 Advanced
  tags: [protocol, networking]

- id: g50
  term: SIP / SIPMOTOR
  category: protocol
  source_pages: p613-616, p639-640
  source_quote: |
    "T2 Specification SIP … Q931 Signal variant + ISDN all countries" (p613)
    "If ever the SIP trunk group or the SIP external gateway is out of service, it could be useful to restart the 'SIPMOTOR' process by using 'dhs3_init -R SIPMOTOR'command" (p639)
  definition: |
    OXE 的 SIP 中继信令由 SIPMOTOR 进程族承载（ps 可见多个实例）；网关故障时可用 dhs3_init -R SIPMOTOR 重启加速重注册（实验技巧）。SIP 网关对象与信令变体（ISDN all countries 壳+SIP 规格）见 g47/g48。
  alias_or_related: traced/motortrace 为其抓包工具（motortrace 3=全 trace）
  tags: [protocol, sip]

- id: g51
  term: T0 / T2 / T1（ISDN 中继）
  category: protocol
  source_pages: p60, p773, p781-796
  source_quote: |
    "BRA 8 ports Board (Basic Rate Access) • Provides 8 T0 interfaces … PRA (T1,T2) Board (Primary Rate Access) • Provides a T1 or T2 link" (p60)
    "In reality the customer shall choose the mode of signaling according to the carrier. If the carrier is in VN then put ISDN France. If the carrier uses ETSI put ISDN all country." (p784)
  definition: |
    ISDN 中继：T0=BRA 板（每口 2B+D）；T2/T1=PRA 板（30/24 通道）；信令变体按运营商选 ISDN France（VN4 位）或 ISDN all countries（ETSI 9 位）；同步参考由运营商提供、T2/T1 优先（优先级段见 principle p36）；T2 有 NOS LED 告警。t3 命令做 ISDN 呼叫追踪。
  alias_or_related: NDDI/Loop start/Ground start=模拟中继变体（p35）；QSIG 分级并列
  tags: [protocol, isdn, t0, t2]

- id: g52
  term: DHCP（Discover/Offer/Request/ACK）
  category: protocol
  source_pages: p348-351, p344-347
  source_quote: |
    "DHCP Discover • Client is asking any DHCP server on the network • MAC address • Parameter Request list • Vendor class identifier" (p348)
    "The 'DHCP Relay' function can be located in a Router, a PC or can correspond to the Virtual router of a VLAN" (p346)
  definition: |
    标准四步交互：Discover（MAC/参数请求表/Vendor class）→Offer（IP/掩码/路由/租期/厂商标识）→Request（接受 IP/服务器标识）→ACK（租约确认+厂商信息）；UDP 67/68；ALE 话机优先接受 ALE DHCP 应答（vendor id alcatel.a4400.0/alcatel.noe.0）；跨网段走 DHCP Relay（路由器/PC/VLAN 虚网关）。
  alias_or_related: 静态绑定+boot file 用于 GD/GA 刷机（p346）
  tags: [protocol, dhcp]

- id: g53
  term: SRTP / DTLS（原生加密）
  category: protocol
  source_pages: p42, p528
  source_quote: |
    "Voice (SRTP) & signaling (DTLS) encryption • End-to-end native encryption for: • NOE IP Phones • SIP extensions (SEPLOS) • Public SIP Trunk • SIP trunk to Rainbow WebRTC Gateway • 8378 IP-xBS DECT Base stations • 4645 Voice Mail" (p42)
    "Encryption of the signaling link, between CS and 4645 VM (DTLS) • Encryption of the Voice between secured terminals and 4645 VM (SRTP)" (p528)
  definition: |
    原生加密双算法：语音 SRTP+信令 DTLS，基于证书认证、零硬件足迹；端到端覆盖六类端（NOE IP 话机/SEPLOS SIP 分机/公共 SIP 中继/Rainbow WebRTC 网关中继/8378 IP-xBS/4645）。许可锁 424（Native Encryption Users）。与 IDSP 的 HTTPS 配置拉取联动（TFTP-HTTPS order）。
  alias_or_related: 两个缩写书中未展开全称；加密配置细节在后续教材
  tags: [protocol, encryption]

- id: g54
  term: VPIM / IMAP4（留言组网与邮件接入）
  category: protocol
  source_pages: p528, p531-532
  source_quote: |
    "Networking capabilities • Centralized voicemail • VPIM (Voice Profile for Internet Mail) protocol" (p528)
    "IMAP access • Consult messages from an e-mail client • No server plug-in required … E-mail notification … With or without VM attachment" (p532)
  definition: |
    4645 组网双协议：VPIM（书中展开 Voice Profile for Internet Mail）做留言系统互联（网络信箱 0/48000、节点 0/500 口径）；IMAP4 做邮件客户端直接听留言（免服务器插件），叠加 E-mail notification（Basic/Advanced 附 wav）。SMTP 端口三态 25/587/465。
  alias_or_related: SMTP 声明在 netadmin 21；防火墙白名单联动（c22）
  tags: [protocol, voicemail, vpim]

- id: g55
  term: P-ANI (P-Access-Network-Info) / RFC 7913
  category: protocol
  source_pages: p605-607, p696
  source_quote: |
    "Service provided by adding the 'P-ANI' header with the caller location information in outgoing external call • P-ANI (P-Access-Network-Info) is defined by RFC 7913, within the framework of private header extensions (RFC 7315)" (p605)
    "P-Access-Network-Info: IEEE-802.3;eth-location='ALE building B floor 0'" (p696, SIP trace)
  definition: |
    主叫位置外发机制：INVITE 携带 P-ANI 私有扩展头（RFC 7913，隶属 RFC 7315 框架；书中给出两条 RFC 号），内容=Access Type+位置串（≤80 字符）；网关参数控制 All/Emergency only/None；取值源 NPD/Entity/IP domain。RFC 7315 书中一并引用。
  alias_or_related: 与 g56 Emergency 机制配套；trace 工具 motortrace/traced
  tags: [protocol, sip-header, location]

- id: g56
  term: Tone 34 / EMG log（紧急通知信令面）
  category: protocol
  source_pages: p685-686
  source_quote: |
    "Tone N°34 (common to all sets of the group)" (p685)
    "'Events/EMG Log' in the 'Menu' tab OR 'Mail Key' • Maximum 100 notifications (un-cleared entries displayed in bold)" (p686)
  definition: |
    紧急通知的信令与界面口径：组内统一 Tone 34+可视弹窗；动作仅 Clear/Snooze(20s)/Callback；忙时 10 秒弹窗每 20 秒重复；EMG log 软键（Events/EMG Log 或 Mail 键）查 ≤100 条 FIFO 日志（未清除条目加粗）。
  alias_or_related: 机制边界见 n31；区域配置见 c26
  tags: [protocol, emergency]

# ── 六、资源/文档名 (resource) ──

- id: g57
  term: RLAB / POD
  category: resource
  source_pages: p3-20
  source_quote: |
    "Remote Lab allows accessing a pool of virtual and physical machines (depending on the course) hosted in a data center. … Pods are independent of each other • Pods have the same configuration • Pods have access to common resources" (p5)
  definition: |
    ALE 培训远程实验室：按 POD 划分同构实验单元（OXE 虚机+OMS+FlexLM+IT Server+4 PC Client；混合模式加课堂硬件 GD4/话机/4059EE），POD 间独立、共享 NAS/SIP 模拟器/外部 DNS。两种教材形态：Fully virtualized（p3-11）与 Hybrid（p12-20）。
  alias_or_related: 实验口径总表 principle p06；ENTP NAS 网络盘
  tags: [resource, lab, training]

- id: g58
  term: MyPortal 文档组（Sales Companion / Feature list / product limits / TC2005 / SA0046 / TC1774 / TC3009）
  category: resource
  source_pages: p297, p545, p611, p277
  source_quote: |
    "'Sales Companion' • 'OXE Feature list' • 'OXE product limits' • 'User manual' (OXE documentation package) • 'Desk phone datasheet'" (p297)
    "SA0046: Voicemail phreaking prevention and security measures • TC1774: Reinforce security on 46x5 voicemail systems" (p545)
    "PLEASE CONSULT THE DOCUMENTS (TC 2005, AND ADDITIONAL ONE…) GIVEN BY ALE OR THE PUBLIC OPERATOR" (p611)
  definition: |
    MyPortal 权威文档指针：Sales Companion/Feature list/product limits/User manual/话机 datasheet（产品面）；TC2005（SIP 运营商参数）；SA0046+TC1774（4645 防盗打与加固）；TC3009（ALE-120/AOM 供电与认证）。skill 的 Boundary 应引用。
  alias_or_related: 外置课程：Advanced（组网）、CPU Loading（FlexLM）、ENTPXTE402（Cloud Connect）
  tags: [resource, documentation]

- id: g59
  term: VG CD-ROM（语音指南与 MOH 光盘）
  category: resource
  source_pages: p430, p440
  source_quote: |
    "The OXE is delivered with a CD-ROM containing all available system (static) voice messages, music-on-hold & documentation … Generic voice guides used in countries where standard voice guides are not used (e.g. France)" (p430)
    "Note that on the VG CD-ROM, the files are in the following directories: • '\VG_6.0\guides_generic\French' for 'vgadpcm.FR0' … • '\VG_6.0\musicalcatel\alaw' for 'adpcmmoh'" (p440)
  definition: |
    随机交付的语音资源盘（目录示例 VG_6.0）：Generic 指南（含法国等用 Generic 的国家）、Standard 指南（按国家）、酒店专用指南、缺省 MOH、说明文档；消息索引↔指南号对照表为随盘 EXCEL。文件命名 vgadpcm.<语言>0 / adpcmmoh。
  alias_or_related: 服务器侧目录 /DHS3ext/vgadpcm/flash/std（custom 放自制 MOH）
  tags: [resource, voice-guides]

- id: g60
  term: ALE Knowledge Hub（培训评估入口）
  category: resource
  source_pages: p815-821
  source_quote: |
    "Connect to ALE Knowledge Hub (https://enterprise-education.csod.com) with your usual credentials" (p817)
    "You must complete the end of training evaluation to be able to download your training certificate of attendance." (p816)
  definition: |
    ALE 培训平台（enterprise-education.csod.com）：课后评估问卷（必须完成才能下载出勤证书）与课程目录检索；文档反馈邮箱 training-services@al-enterprise.com。培训流程性内容，不入 skill。
  alias_or_related: 课程检索 "Find a Course"（p821）
  tags: [resource, training]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列候选术语逐条核对

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| OXE (PABX) | 正文有明确定义（p30） | g01 |
| Call Server / OXE-V | 有定义（p31/p64） | g02 |
| OMS | 有定义（p65） | g13 |
| GAS | 有定义（p68） | g12 |
| MAO | 有定义（p186，全称展开） | g04 |
| OPS/RTR | 有定义（p196/p200） | g28 / g31 |
| swinst | 有定义性用法（p88/p112） | g20（菜单体系 g05） |
| netadmin | 有定义性用法（p87/p136） | g06 |
| WBM | 有定义（p45） | g07 |
| ARS | 有定义（p593，Automatic Route Selection 展开） | 并入 g10/g48 边界与 principle p29（ARS 为机制而非对象条目，防重复） |
| NPD/DID translator | 有定义（p596-598，NPD=Numbering Plan Descriptor 展开） | 并入 g47/g48 链路与 principle p29（同上原因）；NPD 全称已按原文记录 |
| Public COS (Access COS) | 有定义（p659-660） | g09 |
| Entity/CDT | 有定义（p498-500） | g08 |
| Attendant group/4059 EE | 有定义（p451/p465） | g18 |
| OmniMessage 4645 | 有定义（p39/p527） | g41 |
| chrony | 有定义（p167） | g16 |

结论：16 行全部"正文有明确定义或定义性用法"；ARS/NPD 以机制并入相邻对象条目以避免重复，NPD 与 VPIM 的全称均取自原文（Numbering Plan Descriptor 见 p596 标题 "NPD - NUMBERING PLAN DESCRIPTOR"；VPIM 见 p528）。

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：Media Gateway（g03）、Trusted hosts（g11）、Role addressing（g15）、Degraded mode/PANIC（g17）、Crystal/XL（g14）、COS 三套（g09）、Discriminator（g10）
- 角色：mtcl/swinst/root/client（g19-g22）、Attendant（g23）、kb（g24）、板侧 admin/root（g25）、实验账户（g26）、IPDSP 关联用户（g27）
- 订阅：Software locks/spadmin（g29）、CAPEX/OPEX（g30）、CPU-ID/Product-ID/ALU-ID（g32）、SPS/PoD（g33）
- 产品：Common HW 板卡族（g34）、话机系列（g35）、IPDSP（g36）、Cloud Connect（g37）、OmniVista 8770（g38）、UMC（g39）、mgr（g40）、ITSP1/MicroSIP（g42）、内部防火墙（g43）、维护工具三件（g44）、巡检命令族（g45）、4059EE（g46）、外部 SIP 网关（g47）、中继组（g48）
- 协议：ABC-F（g49）、SIP/SIPMOTOR（g50）、T0/T2/T1（g51）、DHCP（g52）、SRTP/DTLS（g53）、VPIM/IMAP4（g54）、P-ANI（g55）、Tone34/EMG log（g56）
- 资源：RLAB/POD（g57）、MyPortal 文档组（g58）、VG CD-ROM（g59）、Knowledge Hub（g60）

### 3. 仅 passing 提及、未单列条目的词（备查）

SEPLOS（p42，SIP 分机加密口径）、PCS（p37，Passive Call Server，Advanced 课程）、PWT（p31，与 DECT 并列的无线制式）、DECT 族 8378/8379/8328 与 VoWLAN OmniAccess（p40-41，本教材不深入）、RDVM（未出现）、INTOF（p779，Crystal 架同步接口名）、NDDI（p35，模拟中继变体）、CampOn（g46 内并条）、NOS LED（g51 内并条）、EVA（4645 内部名，eva.cfg/eva_access 已入 c21）、TJ00302A（示例客户 ID）、n4.205.36.a（示例交付号）、dhs3（自启动提示中的进程族名）、abcacom.exe（4059EE 防火墙放行项，n24）、ICE type（OT 环境网关类型，p615 提及）。

### 4. 提取口径说明

- 所有定义只采信本书正文；PABX、NPD、VPIM、ABC、NUC 类全称以书中展开为准（ABC=Alcatel Business Communication p38、VPIM=Voice Profile for Internet Mail p528、NPD=Numbering Plan Descriptor p596、ACT=Alcatel-Lucent Crystal Technology p70、FXS=Foreign eXchange Subscriber p75、ACTIS=Alcatel-Lucent Configuration Tool for International Sales p201）；SRTP/DTLS/DDI/SIP/QSIG/ARS 等书中未展开全称的缩写一律不做外部补全。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准，引用均为原文摘录；p419 "the Connection COS Id is the same as the Connection COS Id" 与 p248 "root [mg4.ale]]" 的多余词/括号为原文笔误，照录。
