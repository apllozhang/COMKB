# 框架/流程/结构候选 — OmniPCX Enterprise Advanced (ENTPXTE401EN Ed13, R101.1 MD4)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、命令/WBM 菜单路径、拓扑图示、系统机制结构。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——安全地基 → 高可用纵深 → 用户特性 → 组网与数据一致
  type: flow
  source_pages: p41-45, p55, p69, p139, p164, p217, p234, p255, p274, p296, p327, p352, p383, p424, p469, p499, p517
  source_chapter: COURSE INTRODUCTION 起的全部章节序列
  source_quote: |
    "CENTRALIZED IP ARCHITECTURE One Communication Server • n Media Gateways connected via IP ...
    Up to 15000 extensions" (p43)
    "NETWORKED ARCHITECTURE n Communication Servers ... Up to 100,000 extensions • ... A high level of
    feature transparency (ABC protocol)" (p44)
  summary: |
    课程按四段推进：①实验地基（RLAB 两种 Pod 拓扑 + SIP 模拟器 + 架构总览 + Pod 预配置两套 How-To）；
    ②安全地基（SSH 密钥分发：oxe-ssh-auth 对机 / oxe-nw-sshkey-sync 全网）；③高可用纵深（CS 冗余本地/空间
    两套 How-To → IP 域与 CAC → PCS 域级生存性 → 本地私到公溢出），穿插话机级特性集（速拨、多线/监督、
    经理/助理、寻线/代接、办公桌共享、多设备）；④组网主线（组网 Pod 迁移 → Direct IP Link → Audit →
    Broadcast → 组网双向溢出）。这也是实际交付项目的推荐顺序：先打通免密与单机基线，再上冗余与生存性，
    最后组网并保持全网一致。
  conditions: 假设读者已修完 Starter 教材（barring/ARS/装机）
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: RLAB 培训平台双拓扑——集中式 IP Pod 与组网 Pod（含公共资源区）
  type: diagram
  source_pages: p7-16, p12-16, p27-31
  source_chapter: TRAINING LAB ENVIRONMENT（Fully Virtualized / Hybrid Mode 两变体）
  source_quote: |
    "OXE CSA Phys: 192.168.1.1 Main:192.168.1.3 ; OXE CSB Phys: 192.168.1.2 Main:192.168.1.3 ;
    OMS CSA CSB 192.168.1.13 ; FLEXLM SERVER 192.168.1.80 ... REMOTE SITE - Subnet 2 - 192.168.2.x" (p8)
    "OXE NODE 2 Phys: 192.168.1.101 Main:192.168.1.103 ... OMS NODE 2 192.168.1.113" (p13)
  summary: |
    集中式 IP Pod（Subnet 1 主站 192.168.1.x / Subnet 2 远端 192.168.2.x）：OXE CSA(1.1)/CSB(1.2)、
    主角色地址 csm 1.3、OMS 1.13、FLEXLM 1.80、IT Server(NTP) 1.252、PC Client 10/11（1.10/1.11，
    装 IPDSP 31000/31001）、PCS REMOTE 2.5、OMS REMOTE 2.13、PC 20/21（2.10/2.11，IPDSP 31002/31003）；
    组网 Pod 换成 NODE 1（1.1/1.3）与 NODE 2（1.101/1.103，OMS 1.113）。公共资源区 Subnet 0（10.20.30.x）：
    NAS（软件/许可）、SIP 模拟器（12.0.0.2）、外部 DNS 10.20.30.250；网关 1/2 为 1.254/2.254，内部 DNS
    1.250。所有账号密码在 p10/p15 设置表：mtcl/swinst/root=Superuser2580*、PC=admin/superuser、
    FlexLM=root/letacla1（全部实验口径）。Hybrid Mode 变体另加教室硬件 MIX484 GD4（1.12）与实体话机。
  conditions: 实验口径（RLAB 专用）；组网实验前须做 VM 网卡迁移（见 f24）；POD 间互不可见
  tags: [diagram, lab, rlab, topology]

- id: f03
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则（PN=两位 POD 号）
  type: diagram
  source_pages: p34-39
  source_chapter: SIP CARRIER SIMULATOR
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... ITSP1 Public gateway public.itsp1.com
    10.20.30.50 ... SIP domain: sip.itsp1.fr / itsp1.fr" (p34)
    "PBX installation nb 3321PN ... DDI table - First external nb 41000 ... DDI table – First internal nb
    31000 ... Range size 500" (p37)
  summary: |
    模拟器扮演出局运营商：PBX 侧注册账号 pbxP/alcatel（SIP 域 sip.itsp1.fr），公网网关 public.itsp1.com
    挂两个 MicroSIP 模拟 Public（publicP@itsp1.fr，主号 3321PN12345）与 Urgence（112/15/17/18）。
    号码规则：国内 3311PN…3351PN12345、移动 3361PN12345/3371PN12345、国际（44）4421PN12345；呼出变换
    示例（POD3）：0110312345→+33110312345。呼入本机：安装号 3321PN41000，DDI 41000-41499 ↔ 内部
    31000-31499；Node 2（组网）安装号 3311PN、DDI 41500 ↔ 31500。节点间互拨走同一条 ITSP1 链路。
  conditions: 实验口径（RLAB 教学基础设施）；生产 SIP 中继行为（安全/编解码/号码格式）与模拟器有差异
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f04
  title: OXE 两种系统架构——集中式 IP（1 CS+nMG）与组网（nCS，ABC 协议）
  type: diagram
  source_pages: p43-44
  source_chapter: COURSE INTRODUCTION / Architectures
  source_quote: |
    "One Communication Server • n Media Gateways connected via IP ... Up to 15000 extensions • ...
    Ability for calls to overflow transparently to the ISDN/PSTN network when the IP WAN is out of
    service" (p43)
    "n Communication Servers ... Up to 100,000 extensions • A high level of feature transparency (ABC
    protocol) • Centralized management" (p44)
  summary: |
    两种架构共用卖点：跨站点免费通话、IP 话机与分布式媒体网关间 Direct RTP（不经网络转发）、WAN 中断或
    IP 中继饱和时透明回落 ISDN/PSTN。差异：集中式以"一 CS 带多网关"降投资运维、加站点容易（CS 可扩展 +
    Hybrid IP/TDM）；组网以"多 CS 互联"达到 100000 分机并靠 ABC 协议保证特性透明、集中管理。全书后续
    机制（冗余/域/PCS/溢出/组网）都围绕这两张架构图展开。
  conditions: 容量为厂商标称上限；话务模型在书外
  tags: [diagram, architecture, centralized-ip, networked, capacity]

- id: f05
  title: SSH 密钥分发体系——oxe-ssh-auth（对）与 oxe-nw-sshkey-sync（网）双工具
  type: flow
  source_pages: p55-67
  source_chapter: SSH KEY DISTRIBUTION
  source_quote: |
    "From N3 onwards, for security reasons SSHv2 is enabled by default with public key authentication ...
    Host based authentication is no longer supported, thanks to CIS compliance requirements." (p57)
    "Usage: oxe-nw-sshkey-sync –f <.csv file> ... <Main CS IP Address, Node X>,<mtcl password>,<swinst
    password>,<root password>,<log file>" (p62, p64)
  summary: |
    体系三层：①机制——N3 起每台 OXE 的 mtcl/swinst/root 各持独立密钥对，协同功能（mastercopy、pcscopy、
    audit、broadcast）依赖免密互通；②对机工具 oxe-ssh-auth -c <远端IP>（root 执行，自动检测已同步状态，
    双向同步，可对所有账户复用同一密码）；③全网工具 oxe-nw-sshkey-sync -f ssh_multi.csv（每节点跑一次，
    自动从 MAO 推导 twin/PCS/网络节点/4645 清单，先主 CS 后 twin CS 逐对同步，日志 /tmpd/logs/
    oxenwsync.log，结束时删除 csv 并打包 oxenwsynclogs.zip）。
  conditions: 须 root 权限执行；CS 间防火墙须互信（trusted hosts）
  tags: [flow, ssh, security, oxe-ssh-auth, oxe-nw-sshkey-sync]

- id: f06
  title: CS 冗余机制结构——IP 链路承载内容、角色协商与 double main 裁决
  type: structure
  source_pages: p70-82
  source_chapter: CS DUPLICATION（概念）
  source_quote: |
    "An IP Link performs the signaling between both Call servers. It handles: The 'keep alive' messages
    exchange ... MAO (telephonic database) ... LINUX data managed by 'swinst' ... A reference Media
    Gateway" (p74)
    "If the 'Call server role' is not correctly defined, the CS with the highest IP address starts in
    Main role" (p75)
  summary: |
    机制五件套：①IP 链路承载 keep-alive、MAO、话务观察、话单、CCD、swinst 的 Linux 数据、邻居节点广播
    信息、ACTIS 文件（netadmin 维护的 Linux 数据不复制，需 Copy to Twin）；②参考 MG——链路断时连着它的一
    侧继续管理，恢复后另一侧重启；③角色协商——两 CS 互发 CONNECT，按 MAO 的 Preferred CS IP 定 main，
    未配置则 IP 高者上；④切换语义——已建立通话保持、建立中丢失；⑤double main——Real Main（MAO 开）+
    Pseudo Main（MAO 关），话单与话务观察不合并、部分网络无语音邮箱。
  conditions: 冗余对必须同版本同类平台；SSH 公钥须先分发
  tags: [structure, redundancy, duplication, double-main, reference-mg]

- id: f07
  title: 冗余推荐拓扑与空间冗余的 DNS/DHCP/TFTP 适配结构
  type: structure
  source_pages: p80-90, p84-90
  source_chapter: RECOMMENDED TOPOLOGY / SPATIAL REDUNDANCY
  source_quote: |
    "On Common Hardware, the two Call Servers are hosted on CS boards and must be placed in different
    racks ... the two Call Servers ... must be deployed on different hardware" (p80)
    "The CS has an internal DNS server that answers to a 'node name' request with its own main IP address
    • Only the active main CS answers to the DNS requests" (p88)
  summary: |
    拓扑建议：两 CS 同交换机（对网络可靠）；或分两台交换机 + 交换机间备份链（避免 double main）；Common
    Hardware 分机架、GAS/VM 分硬件（每套含 1 CS + 可选 OXE-MS + 可选 WebRTC 网关）。空间冗余（不同子网）
    额外结构：每 CS 有自己的物理地址与 main 角色地址（csma/csmb）；内部 DNS 只由活动主应答节点名；无网内
    DNS 时把两台主地址填为 SIP 设备主/备 DNS；有客户 DNS 时需 DNS 委派（oxe.company.com → 两个主地址）；
    IP 话机/GD/GA/INTIP/8770 可填两个 TFTP/主地址；DHCP 由活动 CS 应答并填自己的主地址，外部 DHCP 须能发
    两个 tftp 地址。
  conditions: 空间冗余下 SIP 应用用节点名 FQDN（如 sip:31000@oxe.company.com）
  tags: [structure, spatial-redundancy, dns, dhcp, tftp, topology]

- id: f08
  title: 主备数据库一致性三态与不停机升级序列
  type: flow
  source_pages: p79, p83
  source_chapter: DATABASE CONSISTENCY / UPGRADING WITHOUT INTERRUPTING SERVICE
  source_quote: |
    "Limited time: 120 minutes by default • /IP/Duplication Parameters/Updates storage time limit
    (0 to 120 minutes) ... After storage time limit: history of MAO commands is deleted and incident
    « 440 » is triggered. A database cloning operation, also called 'Mastercopy', is then necessary !" (p79)
    "1. Stop the telephone application on the standby Com Server ... 6. Switch over the CS (bascule
    command) ... 11. Restart the telephone on this CS" (p83)
  summary: |
    一致性三态：正常（实时复制）→ 备机失联（主库存 MAO 命令历史，窗口默认 120 分钟、可配 0-120）→ 超时
    （删历史、触发 440、必须 mastercopy）。升级序列 11 步：备机停话音→装新版本→无话音重启→swinst 克隆库
    →重启话音→bascul 切换→对原主机重复停机/装版本/克隆/重启——两机轮换完成升级，全程业务在线。
  conditions: mastercopy 前须停备机电话应用并已分发 SSH 密钥；"BE PATIENT!"（克隆耗时数分钟）
  tags: [flow, duplication, mastercopy, upgrade, incident-440]

- id: f09
  title: IP 域机制结构——域分配、CAC、编解码选择链与资源分配
  type: structure
  source_pages: p141-152
  source_chapter: IP DOMAINS（概念）
  source_quote: |
    "High bandwidth: OPUS SWB (Super Wide Band) > OPUS WB (Wide Band)> G722 > G711 > OPUS NB (Narrow
    Band) > G729 ; Low bandwidth: OPUS NB > G729" (p147)
    "THE CALL SERVER(S) MUST BELONG TO DOMAIN 0" (p152)
  summary: |
    结构五块：①域分配——设备初始化时上报 IP，OXE 按域地址表（单地址或地址段）归类，未匹配进默认域 0；
    ②CAC——只控跨域通话数（Domain Max Voice Connection，-1 不限），域内不受控；③本地化——每域可配时区
    （Time zone Name）与国家（Country，改后需系统重启）；④编解码——信令经虚拟 INTIP A 板（虚拟机架 19 位 1），
    按域 intra/extra 带宽档从选择链取双方能力交集（两域取较低档），G722/OPUS 授权由系统参数定、其媒体服务
    需 OMS；⑤资源分配——语音导引优先同 MG（TDM 话机）或同域（IP 话机），Voice Services Broadcast 决定无本
    域导引时是否借他域或改本机音，会议电路可配置跨域借用/提供；4645 VM 仅 G711，跨域转换需两台压缩机且板
    卡与 4645 同域。
  conditions: 域掩码必须与设备一致；设备须复位后才落入新域；1000 域上限
  tags: [structure, ip-domain, cac, codec, resources]

- id: f10
  title: PCS 机制结构——四状态、救援流程与回切计时器
  type: structure
  source_pages: p166-177
  source_chapter: PASSIVE COMMUNICATION SERVER（概念）
  source_quote: |
    "The PCS can have 4 possible states (viewable by using 'pcsview' command) • Inactive ... Active ...
    Inactive*: temporary state before PCS Reset ... Undef (Undefined)" (p170)
    "By default: the reset is launched 30 seconds after the IP link recovery • Hour: ... • Value of a
    timer: ... Specific case: if the value equals to 0 -> No reset" (p173)
  summary: |
    结构：①状态机——Inactive（随 CS）/ Active（接管）/ Inactive*（链路已恢复但设备仍挂着，等待计时器）/
    Undef（冗余系统切换后未重建连接）； pcsview 在 CS 与 PCS 侧都可查。②救援流程——GD4/OMS VM 软复位改连
    救援 IP（mgconfig/omsconfig），话机重启并用 CS 初始化时下发的 TFTP Backup IP@ 连 PCS（开 Keep RTP flow
    则通话中不复位）；③回切——链路恢复后计时器三模式：默认 30 秒、定点 Hour、定时值 Timer（0=不自动重启，
    管理员手动控制）；④SIP 生存性——SIP 终端/外部网关须支持双 proxy（主=CS，备=PCS），主无响应或 503 即切
    备；spatial 场景主必须用 OXE FQDN 且 DNS 强制；⑤外部 SIP 网关——按 PCS IP 参数与注册计时器决定在服状
    态，全局 PCS 地址 255.255.255.255 表示随任一 PCS/CS 在服，且所有网关的 PCS 参数取法必须一致。
  conditions: PCS 许可锁 332>0；PCS 版本不低于 CS；PCS 必须留在域 0
  tags: [structure, pcs, survivability, states, sip]

- id: f11
  title: PCS 数据库与限制结构——单向同步、手工参数清单、30 天上限
  type: structure
  source_pages: p179-183
  source_chapter: PCS DATABASE / PARAMETERS / ACCOUNTING / RESTRICTIONS
  source_quote: |
    "BE AWARE THAT 'DATABASE SYNCHRONIZATION' IS UNIDIRECTIONAL: ONLY FROM CS TOWARD PCS" (p179)
    "The PCS can be active for 30 days max • After 30 days, it switches in 'Software protection
    violation' position" (p182)
  summary: |
    数据面：PCS 库是主库副本，无实时更新，仅手动 pcscopy 或定时（每日/每周）刷新（scp 传输，SSH 密钥前
    提）；除系统库外还同步密码文件、PCS 证书与私钥、Radius 文件、CCD 统计；CS↔PCS 双向都要把对方列为
    trusted hosts 且 /etc/hosts 含对方地址，否则 pcscopy 不工作。不随库同步、须逐台手工配：内部防火墙
    IPTABLES、日期时间时区、NTP、SSH、Syslog、hosts、SNMP、Radius 用户。限制：PCS 不可冗余；激活最长
    30 天（事件 428/427 报断链、431 报剩余时间、432 报违约态）；被救域话机打不了 4645 VM；PCS 库修改下次
    更新即丢；SIP 传真/SIP VM 不能被救；无 TFTP（无二进制下载）、无 DHCP、无 ABC-F。
  conditions: 话单不在更新时复制；PCS 激活期生成的话单需 OmniVista 8770 日同步或手动取回
  tags: [structure, pcs, database, pcscopy, limits]

- id: f12
  title: Local Private to Public Overflow 机制——三类触发、双层权利与 thin sector
  type: structure
  source_pages: p218-226
  source_chapter: LOCAL PRIVATE TO PUBLIC OVERFLOW（概念）
  source_quote: |
    "For an identified called party, the Call Server activates the 'Local Private to Public overflow'
    mechanism in case of: IP domain saturation • Lack of IP resources • ... A PCS becomes Active" (p221)
    "Up to 2000 DID entries per Prefix Access node ... a 'thin sector' allows to assign a DID number to
    a range of none DID users" (p224)
  summary: |
    机制链：呼叫时 CS 定位被叫所在节点→取 Node Access Prefix 里的 ARS 前缀占中继（尽量用主叫本地资源）→
    按 DID 段翻译出外部号（安装号+用户号）→用户透明地打外线。触发三类：域 CAC 饱和、IP 资源（压缩机）
    枯竭、网络断链（PCS 激活）。双层权利：phone feature COS 授权溢出（busy 态/OoS 态/两者），叠加被叫外
    部号的闭锁规则；话务台永远放行。DID 翻译每前缀至多 2000 条，可多段绑域或 MG；thin sector 把非 DID 段
    压到唯一外部号（段首号）实现第三方转接。OoS 溢出需系统参数 Overflow on OoS Extension=True。计费照常
    出话单（字段 26 描述设施类型）；对 SIP 扩展/SIP 设备无效。
  conditions: ARS 管理为 Starter 内容；配置完建议 pcscopy 同步到 PCS
  tags: [structure, overflow, cac, thin-sector, pcs]

- id: f13
  title: Speed Dialing 编号体系结构——索引表、双形态、前缀计划与实体映射
  type: structure
  source_pages: p236-244
  source_chapter: SPEED DIALING（概念）
  source_quote: |
    "This table can contain up to 32500 numbers, indexed from 0 to 32499 ... Ranges may overlap, but
    cannot overlap with the direct speed number range" (p236, p238)
    "Each entity can offer access up to 32 areas" (p244)
  summary: |
    结构：①统一索引表（0-32499，默认仅前 4000 可配，需 cfgUpdate 扩容）；②直接式——全网/全实体统一一段
    （不可与范围段重叠），每号一个前缀；③范围式——至多 400 个范围（可互相重叠），每范围一个前缀，用户拨
    "范围前缀+序号"；④每号可带目录名/名（入局按 Calling ID 显示、支持 call by name）；⑤可勾闭锁受控、可
    配溢出缩位号（原中继不可用时自动改发）；⑥开放缩位号（不完整号，用户补拨）+ 定时溢出（超时未补拨自动
    转完整号）；⑦实体映射——系统范围 0-399 → 实体区 0-31，区配 Phone features COS 决定可用性。
  conditions: 前缀计划中直接式与范围式前缀含义不同（Direct Speed Dial No Prefix / Speed Dial Area Prefix）
  tags: [structure, speed-dialing, numbering, entity]

- id: f14
  title: Multiline 与监督键体系——两种形态、键属性与硬上限
  type: structure
  source_pages: p257-265
  source_chapter: MULTILINE & SUPERVISION KEYS（概念）
  source_quote: |
    "By default, all sets are mono-line • Except SIP extensions" (p257)
    "A set can be supervised by 20 sets maximum • The maximum number of supervisors for a same voice
    mailbox is 100 (20 in a network configuration) ... The total number of supervision keys in the
    system is 15000" (p265)
  summary: |
    体系：①两种形态——Multi-keys（主号复制到多键：多路并发、一线忙来话落下一键）与 Multi-MCDU（多号一
    机：主号+附加号各占键）；②属性——Selective Filtering（manager/secretary 过滤用）、自动入/出占线（默认
    True）；选择性呼转可用前缀叠加线选前缀（20 主线/21 副线）实现按线转发；③监督键——显示被监督方状态
    （部分忙/全忙/空闲/振铃/退服），振铃时按键代接、平时按键直呼；铃型五档（无/短/长/短无过铃/长无过
    铃）；可监督话机/传真/他人语音邮箱（新留言通知+凭密码代查）；④硬上限——每话机至多 20 个监督者、每邮
    箱至多 100（组网 20）个监督者、监督者必须 multiline、全网 15000 监督键、一号一机一键；话务台与寻线组
    不可被监督。
  conditions: 同号多键工作组成场景：来话同响全组
  tags: [structure, multiline, supervision-keys, limits]

- id: f15
  title: Manager/Assistant 组机制——键组、过滤表与四个辅助键
  type: structure
  source_pages: p276-284
  source_chapter: MANAGER/ASSISTANT GROUPS（概念）
  source_quote: |
    "Screening key: Immediate Forwarding by Origin ... Unscreening key: Immediate Pickup by Origin ...
    If the unscreening table is empty, all the calls will be forwarded to the assistant set." (p277)
    "1000 tables usable with screening or unscreening keys • 16 parameters in each table" (p278)
  summary: |
    机制：①组由两台 multiline 话机构成，经理键 Assistant Call + 助理键 Manager Call（建一键自动生成另
    一键），兼直呼与监督；②过滤——Screening（激活后仅过滤表内来话转助理）与 Unscreening（激活后仅表内
    来话留经理）互斥切换；过滤表 1000 张×16 参数（可混内部号/中继组/缩位号/话务台/T2 号）；同一经理可对
    多个助理配多组键；③Selective Filtering——只把经理主号来话转助理、副号不转；④Screening Supervision
    键——助理侧远程开/关经理的过滤并同步 LED；⑤Assistant Away 键（每助理仅一键）——助理挂"离开"暂停过
    滤；⑥Routing Assistant（溢出助理，每经理一名、可服务多经理，且不得已是该经理的助理）在 away 时顶
    班；⑦Manager Mail 键——预设短信互发（Here is / Call from / Urgent call from / You have a meeting /
    You have an appointment），经理可预置回复。
  conditions: 过滤只对 multiline 主线（配合 Selective Filtering）
  tags: [structure, manager-assistant, screening, filtering]

- id: f16
  title: Hunting / Pickup 组机制——三种搜索、COS 随组、进出组与溢出
  type: structure
  source_pages: p299-314
  source_chapter: GROUPS（概念：Hunting groups + Call pick-up）
  source_quote: |
    "Sequential ... The search is always carried out from the set at the head of the group ... Cyclical
    ... The head of the group ... changes for each call ... Parallel ... The free sets in the group are
    rung at the same time" (p300-302)
    "% authorized camp on calls = Max. Number of camp on calls authorized / number of active stations
    in the hunt group x 100" (p305)
  summary: |
    寻线组：①三种搜索——顺序（固定队头）、循环（队头轮转、话务均摊）、并行（同响先接）；②成员随进出组
    切换 COS：入组即用组的 Connection COS/公网 COS/实体（公网 COS 留 255 则保留自己的）；③进出组前缀
    （默认 480 入/481 出），可禁末位成员退组（退光则转溢出号或忙音）；④溢出号——组空或 camp-on 百分比到
    限时溢出到话机/另一寻线组/话务台；⑤Pickup Private call / External Pickup 控制组内代接与组外代打；
    ⑥Greeting guide 可向内部主叫播语音导引替代回铃；⑦multiline 行为由系统参数 No Multi-line call in
    PCX（0/1/2）三分支定义；仅循环/顺序组可含 multiline。代接：组代接（前缀 56，须同组）与直接代接
    （前缀 55+号码），需 COS 授权且被叫未受代接保护。
  conditions: 一台话机只能属于一个寻线组
  tags: [structure, hunting-group, pickup, cos]

- id: f17
  title: Desk Sharing 机制——DSS/DSU 角色、虚拟 MAC 与系统选项
  type: structure
  source_pages: p329-336
  source_chapter: DESK SHARING（概念）
  source_quote: |
    "A shared terminal is called a Desk Sharing Set (DSS) ... A roaming user using a DSS is called a
    Desk Sharing User (DSU)" (p330)
    "'aa:bb:xx:xx:xx:xx' → xx:xx:xx:xx is replaced by the directory number of the DSU • Example for the
    DSU user 31000 : 'aa:bb:00:03:10:00'" (p333)
  summary: |
    机制：①DSS（共享话机）配 LogOn 键（登录前缀）+ Help Desk 键（求助号码）；DSU（漫游用户）配 OverLogOn
    键（顶掉已登录者）+ LogOff 键（自身登出），登录即恢复可编程键/特性/邮箱；②注册——DSS 用真 MAC 如常规
    话机，DSU 自动生成虚拟 MAC aa:bb:分机号（物理帧仍用真地址，虚拟 MAC 只在应用层标识 DSU）；③系统选项
    ——登出免密（默认 False）、忙时 DSU 重置（默认 True：自动登出可打断通话并发 6004 事件；False 则保通
    话）、首次登录强制改密（默认 False）、定时全员自动登出（-1 关闭；0-23 点）、免重启即时登录（默认 True，
    仅 NOE3GEE/IP Essential/Enterprise 同族同节点且无 AOM 时适用）。
  conditions: 适用机型：8 系列 IP Touch EE、IP Premium、IP Essential/Enterprise、IPDSP
  tags: [structure, desk-sharing, dss, dsu, mac]

- id: f18
  title: Multi Device / Twinset 机制——主副站结构、状态语义与快速移机
  type: structure
  source_pages: p353-363
  source_chapter: MULTI DEVICES USER（概念）
  source_quote: |
    "The twinset feature (also called tandem) is a logical association between two sets: a main set and
    a secondary set ... The number of sets can be extended up to 4 in a multi device user configuration" (p353)
    "To perform a rapid call shift, the set which is in idle state dials the Twinset Get Call prefix ...
    the remote party do not detect the change" (p363)
  summary: |
    结构：①主站 + 至多 4 副站（twinset 为 2 台特例），主站号即多设备号；主副站都必须 multiline；主站类型
    NOE IP/TDM/IPDSP/SIP(SEPLOS)/DSU，副站另可 DECT、MIPT、REX（每多设备仅限 1 台 DECT、1 个 REX）；不能
    是模拟/S0/话务台/ACD/寻线组成员/夜转/客房。②呼叫——主副号同响、先接停响；副号只响副站；忙=主站全
    线忙。③状态——Partial busy（False 按主站忙、True 任一忙）与 Ringing in partial busy（长/短铃）；④
    Specific supervision=True 时监督降级为"状态监督"（按监督键显示 MAIN/SECONDARY/TOTAL BUSY 而不振铃）；
    ⑤振铃控制——NOE 话机静音模式（仅 IP/TDM）；REX 用激活/停用前缀（651）；Ring Secondary REX in
    Parallel 控制主为 IPDSP 时副 REX 是否同响；⑥主站退服三参数——Forward if set OOS（COS）、Overflow to
    sec tandem if main OOS（系统参数）、Ring all its secondar. if main oos（COS）；⑦快速移机——空闲侧拨
    Twinset Get Call 前缀，通话无感迁移。
  conditions: 建关联会清空话机上全部数据（呼转/回叫/留言等）；复制到副站的数据不可再改
  tags: [structure, multi-device, twinset, tandem, rapid-call-shift]

- id: f19
  title: Direct IP Link 机制——ABC-F2 全互联、加密结构与容量边界
  type: structure
  source_pages: p383-397
  source_chapter: DIRECT IP LINK（概念）
  source_quote: |
    "'ABC-F2' proprietary protocol stands for 'Alcatel-Lucent Business Communication – Features 2' ...
    No need anymore of H323 channels" (p384)
    "Signaling between network nodes ... encrypted using 'IPSec' ... Media encryption (SRTP) between two
    networked DTLS/ SIP TLS capable devices" (p393)
  summary: |
    结构：①形态——子网内全互联直连（无中继节点、无 VPN），RTP（语音流）封装在 ABC-F 链路信令内全 IP 传
    输；要求全网 ≥ OXE Purple R100.0；本地 hybrid 链路保留不改。②网络交互——完整同构网（子网内 direct +
    子网间 ABC-F IP trunk，Homogeneous network for Direct RTP 开）、部分迁移网（direct + hybrid+VPN，
    需开该开关）、异构网（含 TDM，需压缩机接续）。③加密——节点间信令 IPSec（证书认证，IPSec Manager 建
    链），终端到终端媒体 DTLS/SIP TLS + SRTP（密钥由各 CS 生成经加密链路下发），可混布加密/非加密链路。
    ④容量——100 节点；每链至多 24 接入（接入 1 用 IP 信令、其余无信令）×62 通道=1488 并发；节点级还有包
    含 direct/SIP/ABCF-IP trunk 的全局上限（超限 6005 事件）；性能约 10000 呼/时/链（8 接入）。⑤杂项——
    链路名固定 Link_xx 不可管理、免许可、IP Premium Security 不适用、不能 SNMP 监管。
  conditions: 迁移前提：全网 ≥N1、子网内无 TDM ABC-F 链路、hybrid 仅 IP 信令或无信令、无备份信令
  tags: [structure, direct-ip-link, abc-f2, encryption, capacity]

- id: f20
  title: Audit 两阶段对账结构——specific/shared 对象行为与参考节点语义
  type: structure
  source_pages: p426-442
  source_chapter: AUDIT（概念）
  source_quote: |
    "Audit is done in two phases: 1-Construction of a reference database ... 2-Downloading of the
    reference database over the network" (p426)
    "IT IS HIGHLY RECOMMENDED TO SAVE THE DATABASE OF ALL NODES BEFORE STARTING THE AUDIT" (p442)
  summary: |
    结构：①对象三分类——specific（编号计划/电话簿/中继组/DDI 等全网收集合并）、shared（各类 COS/资费/音
    色/定时器等，以"参考节点"为准全网替换）、not audited（ARS 表/中继组前缀/IP 域等本地对象，须逐节点配
    置）；审计行为跟随 broadcast 对象配置（如 trunk groups 不广播也不审计）。②两阶段——阶段 1 在执行节点
    构建参考库（并发收集各节点 specific 压缩 ASCII 文件，经 sftp 传输；shared 取参考节点）；阶段 2 把参考
    库下发全网（specific 分析插入、shared 系统替换）。③参考节点=启动 audit 的节点（可指定远端）；④已知
    问题——话务台/实体/呼叫分配等链式对象首跑会互相缺引用，需"部分审计（编号计划+实体+话务台+分配）+全
    局审计"或"全局审计跑两遍"；⑤安全阀——必须先用模拟模式（工作在表副本上），强烈建议全网备份后再跑。
  conditions: 前提=全网防火墙互信（物理+角色+第二主地址）+ SSH 密钥分发
  tags: [structure, audit, database, consistency]

- id: f21
  title: Broadcast 增量同步结构——buffer/LOG/RLOG/lupd.dat 闭环与广播域
  type: structure
  source_pages: p471-485
  source_chapter: BROADCAST（概念）
  source_quote: |
    "The buffer file is emptied and stored every 10 min into a LOG file ... LOG.N.S, with 'N' for node
    number and 'S' for sequence number" (p474, p475)
    "128 broadcast areas can be used ... Area numbers are from –1 (no area) to 127" (p481, p483)
  summary: |
    闭环：MAO 修改进 buffer 文件（cm_cb.sav 或 area_cm_cb.sav）→ 定时（默认 10 分钟，可调）落 LOG 文件
    （LOG.节点号.序号；配置广播域时为 A.Z.N.S）→ 各节点定期互比 lupd.dat（mao -lupd 查看）缺号索取 → 全网
    确认后 LOG 删除（仅留最新一条）；远端写入失败则生成 RLOG。命令件：cleanbroad（重置序号+删文件+全网重
    启）、prog_diff（读 LOG/RLOG 内容、节点状态、历史）、maohist（MAO 修改史）。广播域 128 个（-1 不属域
    至 127）：出向三态（不广播/域内/全网）、入向三态（不接收/仅本域/全网），可全局或逐对象配置。激活三法：
    cleanbroad -all、WBM System/Broadcast、mao +br。
  conditions: 不广播对象：trunk group 前缀与 ARS 表、IP 域、嵌入式 DHCP 内容、本地范围缩拨号等
  tags: [structure, broadcast, log, lupd, consistency]

- id: f22
  title: 组网双向溢出对称结构——Private to Public 与 Public to Private Rerouting
  type: structure
  source_pages: p499-507, p517-522
  source_chapter: PRIVATE TO PUBLIC OVERFLOW / PUBLIC TO PRIVATE REROUTING（概念）
  source_quote: |
    "Node access prefix is declared toward the remote node number ... Define a local prefix (preferably
    ARS) • Parameter: 'number to add' • Not broadcasted" (p505)
    "Use of ARS is mandatory to force calls rerouting from public to private network" (p519)
  summary: |
    对称两方向：①私→公——Direct IP Link 拥塞/断链时，经远端节点的 Node Access Prefix（含本地 ARS 前缀
    Number to add + 远端 DID 翻译 + 非 DID 第三方号 Install N° last part）把内部号翻译成外部号走公网；双层
    权利同本地溢出（COS busy/OoS + 闭锁），话务台恒可用；Node DID Translation 与第三方号属性参与广播，而
    Number to add 不广播。②公→私——用户拨外线号（如 0 0110141500），Real Discriminator 按呼叫号匹配挂
    ARS 表，路由 1 用 Trunk Group=-1（去 6 位加 3 位还原内号后重分析、走专线），失败落路由 2 公网；Time-
    based Route List 定优先序；-1 路由每表仅一条且须在首位；非 DID 被叫不适用。
  conditions: 同一原理可推广到子网间（Network Access Prefix / Network DID Translation）；特性免许可
  tags: [structure, overflow, rerouting, ars, node-access-prefix]

- id: f23
  title: OXE 维护命令地图——按功能域归类的命令/工具清单
  type: menu-path
  source_pages: p94, p100, p106, p113-114, p123, p129, p137, p160-163, p187-216, p247, p254, p272-273, p295, p321-322, p326, p348-351, p370-371, p412-417, p449-456, p476-478, p489-498, p515, p535
  source_chapter: 全书 Maintenance 节汇总
  source_quote: |
    "(1)csa> role -b → MAIN stand-by CPU state : ACTIVE ... (1)csb> role -b → STAND-BY" (p113)
    "Use the different commands of maintenance ... 'compvisu sys' • 'hybvisu' • 'trkvisu' •
    'compvisu eqt all' • 'rsthyb' • 'incvisu'" (p412)
  summary: |
    许可与系统：spadmin（许可文件/锁值）、cfgUpdate（缩拨号上限）、incvisu/incinfo（事件，如 440/2879/2880
    /2884/2832/2846/6004/6005）。IP 与冗余：netadmin（IP/防火墙/DNS/Copy to twin）、role -b、twin、bascul、
    swinst（Easy/Expert 菜单：克隆、autostart、停/起话音）、pcscopy、pcsview、config（板卡状态）。域与话务：
    domstat（域/设备/DS 列）、cnx dom（CAC/压缩机计数）、compvisu sys/eqt all（系统压缩参数与呼叫编解码）、
    represent。话机特性：multitool（多线/监督/经理助理查询）、edabv（缩拨号查询）、pbxstat -f d（寻线组状
    态）、supgpbx -le、zdpost d（话机底层数据：pickup_id/tandem 字段）、dsstat（DSS/DSU 13 项）、ippstat
    （MAC/话机/DSU 状态）。组网：hybvisu（链路状态 IDLE/SYN_REQ/SYN_ACK/DATA_TRANSFER）、trkvisu（中继组/
    链路/链上呼叫）、trkstat（中继组通道 B/F 态）、rsthyb（链路复位）。一致性：audit（交互菜单 0-5）、
    cleanbroad、mao -a/-lupd/+br/-br、prog_diff、maohist。
  conditions: 命令均以 mtcl 登录（部分要求 root）；edabv/audit/prog_diff 支持 -l 语言选项（EN0/FR0/GEA）
  tags: [menu-path, cli, maintenance, toolbox]

- id: f24
  title: 组网实验的 RLAB 前置——VM 网卡迁移操作流（避免 IP 冲突）
  type: flow
  source_pages: p372-377
  source_chapter: Pod Configuration: Network labs / OXE VM network interface
  source_quote: |
    "Due to RLAB infrastructure and technology, 2 VMs (even if not started) can't have the same IP
    address." (p375)
    "1) Select 'Remove Interface' button 2) Select the port '192.168.1.1' 3) Send ... Start or perform a
    hard reboot of the VM" (p375-377)
  summary: |
    集中式 Pod 与组网 Pod 的主 OXE 都用 192.168.1.1，但分属两台 VM（ENTP_OXE_CSA 与 ENTP_OXE_NODE_1），
    RLAB 不允许两 VM（即使未开机）同 IP。三步迁移：①在 Rlab Instances 页对 ENTP_OXE_CSA 执行 Remove
    Interface（释放 192.168.1.1）；②对 ENTP_OXE_NODE_1 先 Remove Interface（释放其原口 192.168.1.111），
    再 Create Interface 选 Subnet1 并填 192.168.1.1；③硬重启 NODE 1 并从 NODE 2 ping 验证。同时组网 Pod
    的 OXE 预配置与集中式略有差异（DHCP 关闭、默认编号 Network=0/Node=1、双节点各自 SIP 网关 pbxN/remoteN
    与 DID 段 41000/41500）。
  conditions: 实验口径（RLAB 专用流程）；生产无此步骤
  tags: [flow, rlab, network-labs, migration]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-21）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 集中式 IP Pod 配置 | 有 | f02, f03 | Pod 拓扑 + 模拟器号码规则（步骤细节在 case c01） |
| task-02 | SSH 免密体系 | 有 | f05 | 双工具机制与 CSV 格式 |
| task-03 | 本地冗余部署 | 有 | f06, f08, f23 | 冗余机制结构、一致性三态、命令地图 |
| task-04 | 空间冗余部署 | 有 | f07 | DNS/DHCP/TFTP 适配结构 |
| task-05 | 冗余维护与切换演练 | 有 | f06, f23 | 角色协商/double main 语义 + role/twin/bascul |
| task-06 | 不停机升级 | 有 | f08 | 11 步序列 |
| task-07 | IP 域规划与配置 | 有 | f09 | 域分配/CAC/编解码/资源五块结构 |
| task-08 | IP 域验证排障 | 有 | f23 | domstat/cnx dom/compvisu 归类 |
| task-09 | PCS 部署 | 有 | f10, f11 | 状态机/救援/回切 + 数据库与限制 |
| task-10 | PCS 救援与回切演练 | 有 | f10 | 四状态与计时器模式 |
| task-11 | 本地私到公溢出 | 有 | f12 | 三类触发/双层权利/thin sector |
| task-12 | 速拨体系 | 有 | f13 | 索引表/双形态/前缀/实体映射 |
| task-13 | 多线与监督键 | 有 | f14 | 两形态/键属性/硬上限 |
| task-14 | 经理/助理组 | 有 | f15 | 键组/过滤表/四辅助键 |
| task-15 | 寻线/代接组 | 有 | f16 | 三搜索/COS 随组/溢出/pickup |
| task-16 | 办公桌共享 | 有 | f17 | DSS/DSU/虚拟 MAC/系统选项 |
| task-17 | 多设备用户 | 有 | f18 | 主副站/状态语义/快速移机 |
| task-18 | Direct IP Link 组网 | 有 | f19, f24, f23 | ABC-F2 结构/容量/加密 + RLAB 迁移前置 + hybvisu/trkvisu |
| task-19 | Audit | 有 | f20, f23 | 两阶段/对象三分类 + audit 菜单 |
| task-20 | Broadcast | 有 | f21, f23 | buffer/LOG/lupd 闭环 + 命令件 |
| task-21 | 组网双向溢出 | 有 | f22 | 私→公/公→私对称结构 |

补充说明：
- f01（课程推进逻辑）、f04（两种架构）不直接对应单个 task，是全书组织轴与架构底座。
- 21/21 全部有框架类覆盖；数值细节（容量表、锁号、事件号、默认前缀值）归数值提取器（principle.md），本文件只留结构锚点与菜单路径。
- 生产化边界提示：GD/OMS 的 SSH 连接方法、ARS 与闭锁基础、装机流程均明确"REFER TO STARTER TRAINING"（p110、p134、p229、p525），属书外前置。
