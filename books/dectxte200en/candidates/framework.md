# 框架/流程/结构候选 — OmniPCX Enterprise DECT Solutions (DECTXTE200EN Ed12)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、技术架构图示、管理对象层级、操作菜单路径、流程机制。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进主线——DECT 底座 → 实验环境 → IP-xBS 全套 → IBS/混合 → 重注册/外部同步 → SIP-DECT
  type: flow
  source_pages: p3-298
  source_chapter: 全书模块顺序（DECT Overview → Training Lab → Pod Configuration → IP-xBS Overview/Management objects/Synchronization/Commissioning → 各 How-To → FWU OTA → Topologies → Multi-sites → Radio coverage → IBS → Mixed → Auto re-registration → External sync → SIP-DECT）
  source_quote: |
    "The DECT protocol is used between a cordless set and a DECT interface for accessing to the PABX" (p5)
    "Hybrid Mode (RLAB + Classroom equipment) is used during 'DECT' training" (p51)
    "Deploy 8328 base stations & 8214 handsets" (p279 目录)
  summary: |
    课程按十段推进：①DECT 技术底座（标准/频段/复用/帧/标识号码/漫游切换/安全）；②RLAB+课堂混合实验环境与 POD 预配置；③8478 IP-xBS 概览（特性/流量/同步/WBM）；④管理对象（PARI/RPN/位置区/Site/Data Sync Primary）；⑤空中同步（内部/簇/外部/Sync Highway/拓扑）；⑥开通（IP/固件/注册/维护工具/工程规则决策树）；⑦手机与用户（创建/注册/注销 + 固件 OTA + 自动重注册）；⑧拓扑与多站点 + 无线覆盖勘测；⑧9479 IBS 与混合模式、外部同步链路；⑩8328 SIP-DECT（单站/双小区）。这是"先懂空中接口、再配 IP 基站、后补 TDM 与低成本支线"的教学主线，也是实际交付的推荐学习顺序。
  conditions: 无版本前提；SIP-DECT 章节明确与 PARI/PLI 体系解耦（p7 脚注）
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: DECT 产品线三分结构——TDM IBS / 全 IP IP-xBS / SIP-DECT
  type: structure
  source_pages: p7
  source_chapter: DECT offer
  source_quote: |
    "TDM offer common hardware IBS: Intelligent Base station Connected to an UA board"
    "VOIP offer common hardware Connected to the customer LAN 8379 DECT IBS 8378 DECT IP-xBS"
    "Low-cost DECT mobility for users connected to small PCX configurations 8328 SIP-DECT (*)"
    "(*) Since the SIP-DECT configuration in OXE is based on SIP users, the following explanations
    (PARI, PLI, etc.) do not necessarily apply to this type of infrastructure." (p7)
  summary: |
    OXE 的 DECT offer 结构：①TDM 线——8379 IBS 接 UA 板卡（UAI/MIX），走 Common Hardware；②VoIP 线——8378 IP-xBS 接客户 LAN（8379 IBS 也归入此框图）；③低成本线——8328 SIP-DECT（及 IP-xBS SIP-DECT 变体），基于 SIP 用户语义，PARI/PLI 概念不适用。三条线的容量/能力边界见 p27 容量表与 p272 SIP-DECT 特性。选型判断入口：站点规模（小站→8328）、存量硬件（TDM→IBS）、全 IP 与加密（→IP-xBS）。
  conditions: SIP-DECT 线为低成本定位，能力子集（见 n13-n15）
  tags: [structure, product-lines, selection]

- id: f03
  title: DECT 无线底座图——频段 × FDMA/TDMA/TDD × 10ms 帧结构
  type: diagram
  source_pages: p5, p8-12
  source_chapter: DECT overview / DECT characteristics
  source_quote: |
    "1880 MHz – 1900 MHz European / 1900 MHz – 1920 MHz China / 1910 MHz – 1930 MHz Latin America /
    1920 MHz – 1930 MHz North America" (p5)
    "Radio power 250 mW ... Channel bandwidth 1,728 MHz ... Transmission carriers 10 ... Carrier
    spacing 2 MHz ... That is, 120 multiplexed radio channels" (p8)
    "Each DECT frame is 480 bits ... 24 time slots per frame ... Field A: command and signaling
    throughput 6.4 Kbit/s / Field B: voice throughput 32 Kbit/s" (p11)
  summary: |
    DECT 空中接口三层结构：①频率维——按国家分 4 段频谱（欧洲 1880-1900、中国 1900-1920、拉美 1910-1930、北美 1920-1930），带宽切成 10 个载波（F0-F9），每载波 1.728MHz、间隔 2MHz；②时间维——TDD 把 10ms 帧分 24 时隙（IBS 收发各 6、xBS 收发各 12），上下行成对；③信道维——FDMA×TDMA×TDD 合计 120 个复用无线信道。帧内 Field A 承载信令 6.4Kbit/s，Field B 承载语音 32Kbit/s。基站发射功率恒定 250mW，小区大小由环境决定，可重叠提升话务密度，非相邻小区可复用"频率+时隙"。
  conditions: 各国频段以当地法规为准；US 于 2005 年采用 DECT，日本用 PHS（p4）
  tags: [diagram, radio, fdma-tdma-tdd, frame]

- id: f04
  title: 标识号码体系图——PARI/RPN/RFPI/PARK/PLI/IPUI 与逻辑 AND 匹配
  type: diagram
  source_pages: p14-22
  source_chapter: Identification numbers
  source_quote: |
    "PARI: Primary Access Right Identifier, identification of the PABX, made of 31 bits or 8 hexa
    decimal digits ... RFPI: Radio Fixed Part Identifier, identification of the Base station composed
    of the PARI and of the RPN ... PARK: Portable Access Right Key ... corresponds to the PLI + the
    PARI number of this system (coded in 13 digits) ... PLI: Park Length Indicator (maximum value 31)"
    (p14)
    "PLI=31 and PARI=10000400100 → PARK=3110000400100" (p17)
  summary: |
    六号码关系图：系统侧 PARI（31 位，11 个八进制位）+ 系统分配给基站的 RPN（2 个十六进制位）合成基站广播的 RFPI；手机侧 PARK（13 位 = PLI 2 位十进制 + PARI 11 位八进制）在注册时写入、固化 IPUI（14 个八进制位）标识手机本身。锁定算法：手机把收到的 PARI 与本地 PARK 做逻辑 AND，参与比较的位数由 PLI 决定——PLI=31 全位比较（单 PARI）；multi-PARI 时把 PLI 降到 29 等，末几位"Don't care"，两个相近 PARI 可同时兼容同一手机（p19-20 两个 AND 算例）。这是全书包内配置字段（PARI Value/PLI for CTM/AC System）的语义来源。
  conditions: A different PARI is mandatory per type of DECT hardware deployed on an OXE，IBS 与 xBS 各需一个（p15）
  tags: [diagram, pari, pli, park, identification]

- id: f05
  title: Roaming 定位流程与 Handover 三阶段
  type: flow
  source_pages: p23-26
  source_chapter: Roaming / Handover
  source_quote: |
    "The handset regularly scans all radio channels in order to measure the signal strength of each
    one ... The handset compares system PARI with its PARK number ... the mobile 'locks onto' the
    system" (p24)
    "For handover to be possible, all the base station must start their DECT frame at exactly the
    same time. This condition implies highly accurate synchronization" (p25)
  summary: |
    Roaming（定位阶段）：手机扫所有信道测 RSSI → 选最强基站 → 上报 IPUI+PARK → 基站回 RFPI → 手机比对 PARI/PARK → 锁定系统，此后可任意位置收发呼叫。Handover（通话中切换）三步：①通话中手机持续扫描评估其他基站；②与目标基站建立第二条无线链路（同时向两站发射）；③新链路就绪后语音切到新信道、释放旧信道，全程对用户透明。前提：所有基站 DECT 帧精确同步——这就是后续整个同步体系（f13）存在的理由。
  conditions: handover 仅同 Site 内可用（p87），跨 Site 只有 roaming（p88）
  tags: [flow, roaming, handover, localization]

- id: f06
  title: DECT 安全三级与 UAK/AC/DCK 密钥体系
  type: diagram
  source_pages: p35-37
  source_chapter: DECT security
  source_quote: |
    "Identity mode ... based on verification of the IPUI-N number ... Authentication mode ... The
    handset is installed / A call is setup / The mobile is located / The handset is uninstalled ...
    Encryption mode ... initiated at call setup ... Once the authentication procedure has been
    performed" (p35)
    "This key (128 bits) is called UAK for User Authentication Key ... It is calculated from the AC
    (Authentication Code) ... A registration phase isn't possible if the AC key used in the PBX is
    different from the AC key used in the handset" (p36)
    "a special random key (64 bits) is derived from UAK. This key is called DCK for Derived Cipher
    Key ... never broadcasted or transmitted between PBX and the handset" (p36)
  summary: |
    安全模型三层：①Identity——仅核对 IPUI-N（默认级别）；②Authentication——在装机/呼叫建立/位置变化/卸机四个时机用 UAK（128 位，由双侧共享的 AC 派生，从不上空口）做挑战比对；③Encryption——认证通过后每次呼叫派生新 DCK（64 位）加密集通话含切换全程。AC 在注册时手机侧输入、必须与系统 AC System 一致（p144/p227 配置项）。硬件边界：Common Hardware 上 IBS 无加密，仅 IP-xBS 支持（p37 表）。
  conditions: 系统级安全级别在 PWT/DECT System / Security level 配置；"Can't be Encryption (it's for IP-xBS)"（IBS，p227）
  tags: [diagram, security, uak, ac, dck]

- id: f07
  title: RLAB 培训平台 POD 结构——POD 池 + 课堂硬件 + 公共资源区
  type: diagram
  source_pages: p40-45
  source_chapter: TRAINING LAB ENVIRONMENT / POD CONFIGURATION
  source_quote: |
    "Remote Lab allows accessing a pool of virtual and physical machines (depending on the course)
    hosted in a data center. ... Pods are independent of each other / Pods have the same
    configuration / Pods have access to common resources" (p40)
    "OXE CSA Phys: 192.168.1.1 Main: 192.168.1.3 OMS CSA CSB 192.168.1.13 ... NTP Server
    192.168.1.252 ... FLEXLM SERVER 192.168.1.80" (p42，实验口径)
  summary: |
    实验平台结构：每个 POD（Subnet 1，192.168.1.x，实验口径）含 OXE CSA（物理 192.168.1.1 / Main 192.168.1.3）、OMS 虚机（192.168.1.13）、IT SERVER（192.168.1.252，NTP）、FlexLM（192.168.1.80）、内部 DNS（192.168.1.250）、课堂 PC（192.168.1.9）与 GD4（192.168.1.12）+ 课堂 IBS/xBS 基站与手机（31015/8234、31016/8244、31017/8214、31020/ALE-30h 等）；公共资源区（Subnet 0，10.20.30.x）放 NAS、SIP 模拟器、外部 DNS（10.20.30.250）、邮件服务器。预配置清单（p51）：许可已还原、SSH 放行、NTP/FlexLM 已声明、DHCP VLAN1 池 192.168.1.145-155、机架板卡已建、用户已建、公共 SIP 中继已建。
  conditions: 实验口径（RLAB 专用基础设施）；账号密码见 p44 表（mtcl/Superuser2580*、flex/letacla1、training/superuser 等，实验口径）
  tags: [diagram, lab, rlab, topology]

- id: f08
  title: ITSP1 SIP 运营商模拟器拓扑与 POD 号码变换规则
  type: diagram
  source_pages: p48-49
  source_chapter: SIP Carrier Simulator
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... ITSP1 Public gateway public.itsp1.com
    10.20.30.50 ... SIP domain: sip.itsp1.fr ... Id: pbxP password: alcatel" (p48，实验口径)
    "PBX installation nb 3321PN ... DDI table - First external nb 41000 ... DDI table – First
    internal nb 31000 ... Example: 31002's external nb 3321PN41002" (p49)
  summary: |
    模拟器扮演出局运营商：PBX 以 SIP 账号 pbxP/alcatel（P=POD 号）注册到 gateway1.itsp1.com（10.20.30.51，SIP 域 sip.itsp1.fr），公网网关 public.itsp1.com（10.20.30.50）。号码体系：安装号 3321PN，DDI 段首外号 41000 对首内号 31000；以 POD 3 为例，31002 的外号 = 33210341002，外呼拨 0210341002 或全号，PBX 送出 +33210341002、收到同样号码（环路验证）。DECT 实验用外呼/呼入环路验证中继，与本书主线解耦。
  conditions: 实验口径（RLAB 教学基础设施）；号码格式不可套用于生产
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f09
  title: 8378 IP-xBS 方案全景——系统特性/网络特性/OXE 兼容性
  type: structure
  source_pages: p57-64
  source_chapter: 8378 DECT IP-xBS - Overview
  source_quote: |
    "12 radio channels - 11 simultaneous voice communications ... Handover and Roaming in mixed IP
    and TDM Base Stations ... SUOTA Software Upgrade Over The Air ... VAD on G729" (p58)
    "PoE compatible Class 2: IPxBS is powered by PoE only ... RTP Media stream direct ... Codecs
    supported: G711 (A-µ law), G729A/B ... LLDP-MED compliant" (p59)
    "Compatible with OXE R12.2 minimum ... Up to 2032 Base Stations per OXE node ... 254 bases
    Stations per PARI ... 8 IP-xBS PARI per OXE node" (p60)
  summary: |
    IP-xBS 方案全景三块：①系统特性——每站 12 信道/11 路并发通话、支持 IP+TDM 混合切换漫游、集中管理、82x2/82x4 手机、8244/8262 可预留 2 信道做告警、SUOTA 空中升级、晶振与 Common Hardware 上支持鉴权加密、G.729 VAD；②网络特性——10/100BaseT、仅 PoE Class 2 供电、仅单播、DHCP/静态、连 OXE TFTP、RTP 媒体直达、UA/UDP 信令、QoS/VLAN、LLDP-MED；③兼容性——OXE R12.2 起、支持中心/周边区/单多节点/Campus/Com Server 冗余/Passive CS survivability、native 加密（IP-xBS R200）、2032 台/8 PARI/254 台每 PARI。硬件三个型号（集成天线/外置天线/室外，p65）。
  conditions: IPv4 only（IPv6 硬件就绪但暂不适用，p59）
  tags: [structure, ip-xbs, capacity, compatibility]

- id: f10
  title: IP-xBS 流量模型——UA/UDP 单播信令 + RTP 直达媒体 + 连接切换中继
  type: diagram
  source_pages: p71-74
  source_chapter: 8378 DECT IP-xBS - Description - Flows
  source_quote: |
    "There is no IP Multicast, only Unicast in the exchanges between IP-xBS and OXE Call Server ...
    Works as a NOE IP phones" (p71)
    "The IP-xBS acts as a DECT / UA / UDP / IP bridge" (p72)
    "The media stream (RTP) is direct between an IP set or trunk and an IP-xBS base station ...
    Supported codec are G711 and G729A" (p73)
    "All signaling and media redirection within the IP-xBS DECT subsystem are managed by the IP-xBS
    subsystem itself (Connection Handover) ... Signaling and media commands are always sent by the
    Call Server to the initial base station" (p74)
  summary: |
    流量模型：基站像 NOE 话机一样经 UA/UDP 注册与信令（无组播）；媒体 RTP 在话机/中继与基站间直达（不经 Call Server）。切换时 Call Server 只与初始基站（Relay xBS）保持信令与媒体连接，xBS 子系统自管切换：新基站与旧基站建 IP 中继（信令+媒体），初始媒体连接保持、在基站间重路由。网络含义：IP 网要按 VoIP 拓扑适配（QoS/带宽），Call Server 到初始基站的信令路径是控制面要害。
  conditions: 编解码 G711/G729A（信令封装 UA/UDP）
  tags: [diagram, flows, ua-protocol, rtp, handover]

- id: f11
  title: 管理对象四级层级——PARI → RPN → Location Area → Site
  type: structure
  source_pages: p81-92
  source_chapter: 8378 DECT IP-xBS - Management objects
  source_quote: |
    "The Call Server can manage several PARI • Up to 8 different PARI • 254 base stations per PARI" (p82)
    "Inside a PARI, up to 64 location areas may be defined ... Area RPN 0:1-63 / 1:64-127 /
    2:128-191 / 3:192-254" (p84-85)
    "A SITE is a group of 8378 DECT IP-xBS linked to a call server and located in the same
    geographical location where it is possible to do handover ... By default, all base stations are
    in the same site" (p86, p89)
  summary: |
    四级对象层级：①PARI——每节点最多 8 个、每 PARI 254 台基站、每类硬件一个 PARI；②RPN——系统分配的基站空中标识，用于地理定位与同步识别；③Location Area——按 RPN 区间划分的位置区（每 PARI 最多 64 个），高密度安装时优化寻呼流量，示例 4 区划分见引文；④Site——可做 handover 的同地理位置基站组，默认全在 Site 0，跨 Site 可 roaming 无 handover（p87-88）。组合关系：一个 PARI 可拆给多个 Site（小分支办公），一个 Site 也可含多 PARI（此时需配 PARI 间同步链路，p91-92）。
  conditions: Site 增删与基站重分配由系统管理员经管理工具完成
  tags: [structure, pari, location-area, site, management-objects]

- id: f12
  title: Data Sync Primary 与 IP 中继切换机制（含容量）
  type: diagram
  source_pages: p93-97
  source_chapter: Site management – Data Sync Primary / Handover mechanism
  source_quote: |
    "The Data Sync Primary is a xBS base station in charge of synchronizing the data between all the
    xBS base stations of a PARI inside a Site ... One Data Sync Primary for every couple Site/PARI ...
    Handover is only possible between base stations with the same Data Sync Primary" (p93)
    "IP-xBS Base Station supports simultaneoulsly 11 DECT radio communications + 11 IP Relays." (p97)
  summary: |
    切换机制图：每个 Site/PARI 对自动选出 Data Sync Primary（dectview xbs 中的 P 标志），负责同步树优化、切换机制、基站状态、与 OXE 的状态消息。切换五步：①手机与 xBS1 建信令+RTP；②手机移近 xBS2 发起 bearer request，xBS2 问 Data Primary"谁在中继"；③xBS2 与 xBS1 建 IP 中继（信令+媒体）并建立与手机的无线链路；④手机再移到 xBS3 时同理（xBS3 即 Data Primary 时自己查表）；⑤新中继建立、xBS1-xBS2 旧流停止。容量口径：每站同时 11 路 DECT 无线通话 + 11 路 IP 中继，切换瞬间双链路并存时要吃两份资源（表中可用数从 11 降到 10）。
  conditions: Data Primary 由系统自动选择，不可手工指定
  tags: [diagram, data-sync-primary, handover, capacity]

- id: f13
  title: 空中同步体系——Internal Sync / Sync Master / Sync Cluster / External Sync / Sync Highway
  type: structure
  source_pages: p98-116
  source_chapter: 8378 DECT IP-xBS – Synchronization over the air
  source_quote: |
    "A SYNC MASTER is the 8378 DECT IP-xBS root of the internal synchronization tree ... The Sync
    Master is automatically selected by the xBS subsystem and it may change over the time" (p101)
    "Up to 8 Sync Clusters per couple Site/PARI ... By default, all base stations belong to Sync
    Cluster 0 ... A base station may belong up to 8 Sync Clusters ... Only for Special cases when
    the radio coverage is tricky" (p102)
    "The maximum of levels in the synchronisation tree is 24" (p75)
    "The xBS system is only able to build one synchronization tree per PARI ... The Sync master base
    station does not support any communications ... A backup Sync Master must also be setup and
    configured" (p106)
  summary: |
    同步体系五件套：①Internal Synchronization——同 Site 同 PARI 内基站互相时间对齐，树按 RSSI+跳数自动构建（≤24 级），无线环境变化自动重构，默认零配置（p113-114）；②Sync Master——树根，自动选举可漂移；③Sync Cluster——无线环境恶劣（如电梯井）时把基站分组不互相同步，每 Site/PARI 最多 8 簇、默认 Cluster 0、单站可属最多 8 簇；④External Synchronization——两个 xBS 集合之间或 xBS 集合与 TDM 基站之间同步，Master Sync 与 External Sync RPN 手工指定、Sync Master 禁止承载通信、Backup Sync Master 强制且须能看见同一 External Sync BS（p106/109）；⑤Sync Highway——>2 个 PARI 串联同步的附加配置（p111-112）。查询工具 xbssynchro 显示树（RPN+RSSI），incvisu | grep xBS 看事件（p116）。
  conditions: master 与 backup 均失效时无孤岛、无自动恢复（p109，见 n07）
  tags: [structure, synchronization, sync-master, sync-cluster, sync-highway]

- id: f14
  title: IP-xBS 开通总流程与工程规则决策树（简单/复杂部署）
  type: flow
  source_pages: p125-141
  source_chapter: 8378 DECT IP-xBS - Commissioning / Engineering Rules
  source_quote: |
    "IP-xBS IP configuration •Dynamic •Static ... IP-xBS firmware update •TFTP server •Manual update
    ... IP-xBS registration •MAC @ in the OXE Database" (p125)
    "Easy deployment • IP-xBS only • 1 PARI, 1 location area • 1 site • 1 cluster ... IP-xBS is
    registered automatically, using default parameters set in OXE configuration" (p140)
    "Are there branch offices? → Create several 'SITE' ... More than 2 PARI? → Use SYNC HIGHWAY ...
    Full coverage not possible using air sync within a site? → Use several 'Sync Clusters' ...
    More than 254 xBS? → Use External synchronization" (p141)
  summary: |
    开通四步主流程：①IP 配置（动态走 DHCP——内部 DHCP 新增 vendor class alcatel.ipxbs.0，或静态）；②固件更新（TFTP 自动后台或 WBM 手动）；③注册（开启注册开关自动收编，或手工录入 MAC@）；④管理维护（dectview 等命令族）。启动时序（p136）：上电 → DHCP 请求（IP+TFTP 地址）→ 固件更新 → 注册入库。工程规则决策树（p141）：分支办公→建多 Site；>2 PARI→Sync Highway；站内空中同步覆盖不全→多 Sync Cluster；>254 台→External synchronization；其余走"1 PARI/1 位置区/1 Site/1 簇"的极简部署。
  conditions: 简单部署依赖 OXE 默认参数与注册开关开启；复杂部署参照《Getting started with the 8378 DECT IP-xBS solution on OXE》(BP 网站)
  tags: [flow, commissioning, engineering-rules, decision-tree]

- id: f15
  title: OXE 配置菜单路径总表——PWT/DECT System 配置树
  type: menupath
  source_pages: p143-291（How-To 各章）
  source_chapter: 全部 How-To 实验的菜单路径汇总
  source_quote: |
    "PWT/DECT System / Radio base type xBS or Mixed ... PWT/DECT System / xBS System / xBS Pari ...
    PWT/DECT System / xBS System / xBS Site" (p144-145)
    "PWT/DECT System / xBS system / xBS Site / External Synchronization" (p266)
    "PWT/DECT System / IBS System ... Shelf / <concerned media gateway> / Board / <concerned UA
    board> / IBS" (p228-230)
  summary: |
    配置菜单全景（webadmin/mgr 通用）：全局参数 PWT/DECT System（Radio base type、PLI for CTM、AC System、Security level、Station base type、Flag External Handoff）；xBS 域 PWT/DECT System / xBS System（Number of PARI、WBM 开关与密码、SYSLOG、Registration node/enabled/Default PARI/Default location area）→ xBS Pari（PARI Number/Value/Area type）→ xBS Site（Site Number/Name、External Synchronization 子页）→ xBS base station（MAC@、Location name、Site Number、PARI Number、Location Area、RPN 只读、Clusters 0-7、Syslog level）；IBS 域 PWT/DECT System / IBS System（PARI Value、Area type）+ 硬件路径 Shelf/<mg>/Board/<UA board>/IBS；用户与注册 Users/<User>/DECT set（DECT Register/Deregister 按钮）与 Users（创建/删除）。8328 例外：OXE 侧仅 Users 建 SIP Extension，其余配置在基站自身 WBM。
  conditions: 菜单名以 R101.1 webadmin 为准；R5.x 旧 mgr 界面字段等价
  tags: [menupath, configuration, webadmin]

- id: f16
  title: 固件双轨升级架构——基站 downstat x 后台下载 / 手机 downstat m 空中 FWU
  type: flow
  source_pages: p129-133, p179-183
  source_chapter: Firmware update (xBS) / FIRMWARE UPGRADE OVER THE AIR (handsets)
  source_quote: |
    "When the call server has some free resources, it requests an xBS to start downloading the new
    firmware on its RAM in background. So that it is still running for handsets calls. After
    successful download and when base station is idle, the call server restarts them" (p130)
    "The Audio communication is preferred over downloading. That means that a software download is
    stopped during an audio communication and will resume later ... The handsets switch on the new
    downloaded software version when they are put on a charger cradle" (p179)
  summary: |
    基站轨（p129-133）：TFTP 自动下载到 RAM（后台、不中断业务）→ downstat x 管理菜单（1 启动下载 / 2 下发 Flash and Reset / 3 恢复 legacy 模式 / 4 重试 DOWNLOAD_FAILED）→ 自动复位开关（YES=下载成功自动重启整站/PARI；NO=手工经 downstat x 控制）。手机轨（p179-183）：Download Server + 电话应用架构，单手机同一时刻仅一条数据信道且语音优先（下载暂停续传）；DECT 应用按话务决定并行度与顺序；新版本在回充电座时生效；管理入口 downstat m 交互菜单（1 显示版本 / 2 下载状态 / 3 可下载清单 / 4 下载单机 / 5 取消），或 downstat m n <列表> 直接下发、downstat m b <binary> n <列表> 指定二进制。
  conditions: 基站固件最低 v73b0003（p131）；手机二进制在 /usr2/downbin（bin8212...bin8262EX，p181）
  tags: [flow, firmware, downstat, suota]

- id: f17
  title: 六种支持拓扑清单（xBS 单线/分支/混合 × 组合）
  type: structure
  source_pages: p191-198
  source_chapter: 8378 DECT IP-xBS - Supported Topologies
  source_quote: |
    "IP-xBS only • 1 node • 8 PARI max • 2032 IP-xBS" (p193)
    "Mixed xBS/IBS on same site ... • 2032 IP-xBS • 256 IBS" (p195)
    "When it is not possible to have an external synchronization, the distance between the area must
    be > 1km." (p196)
    "Two nodes are not synchronized ... • Several nodes ... • roaming" (p198)
  summary: |
    六种拓扑及能力（Handover/External Handover/External inter-node handover/Roaming 四格判定）：①IP-xBS 单线（1 节点 8 PARI 2032 台，全部能力）；②IP-xBS+分支办公（多 Site WAN，全部能力）；③混合 xBS/IBS 同站（+256 IBS，经外部同步链路，全部能力）；④混合无分支无重叠（无法外部同步时区域间距须 >1km）；⑤混合+分支办公；⑥OXE 网络混合 xBS/TDM（多节点、节点间不同步、仅 roaming+跨节点外部切换）。选型读法：先看是否多节点（决定 inter-node 能力），再看 IBS 混入方式（决定是否需外部同步与间距约束）。
  conditions: 每图右上四格图例（Handover/External Handover/External inter node handover/Roaming）为能力判定基准
  tags: [structure, topologies, mixed, multi-node]

- id: f18
  title: 8328 SIP-DECT 注册四步流程与双小区（Dual Cell）机制
  type: flow
  source_pages: p277-278, p288
  source_chapter: Registration / Dual cells
  source_quote: |
    "1) Create SIP extension user on OXE for each corresponding DECT handset ... 2) Declare the DECT
    user on the Base Station ... 3) Register the DECT handset on the Base station ... 4) Then,
    SIP-DECT Base Station makes 'SIP register' on OXE for the Handset ... 'Contact' = 'DECT handset
    phone Number' @ 'Base Station IP address'" (p278)
    "THE PRIMARY STATION WILL BE THE STATION WITH ALREADY AT LEAST ONE EXTENSION DECLARED." (p288)
  summary: |
    SIP-DECT 注册闭环四步：OXE 建 SIP Extension 用户（每机 1 个 SIP 许可）→ 基站 WBM 建扩展+手机并关联 → 手机空中注册到基站 → 基站代手机向 OXE 发 SIP register（Registrar 记录 contact=号码@基站 IP）。双小区：第二台 8328 上电入网后自动发现主站并拉取全部配置（只需先给它配 DHCP）；主站判定=已声明至少一个 Extension 的那台（仅声明 Extension 即可确立主站身份，无需注册手机）；链路建立约 5 分钟，双小区区内有 handover/roaming，两小区间没有。
  conditions: 双小区要求同 IP 子网 + NTP mandatory（p272）；仅 8214 手机
  tags: [flow, sip-dect, registration, dual-cell]
```

## 任务覆盖自检

| BOOK_OVERVIEW task | 对应 framework 条目 |
|---|---|
| task-01 | f03, f04, f05, f06 |
| task-02 | f02, f17 |
| task-03 | f07, f08 |
| task-04 | f09, f10, f14, f15 |
| task-05 | f14（注册机制）；操作步骤见 case c05 |
| task-06 | f15（SYSLOG 路径）；操作步骤见 case c06 |
| task-07 | f15（注册路径）；操作步骤见 case c07 |
| task-08 | f15；操作步骤见 case c08 |
| task-09 | f16 |
| task-10 | f16 |
| task-11 | f11, f17 |
| task-12 | f03（RSSI 语义）；勘测操作见 case c09，数值见 principle p14 |
| task-13 | f15（IBS 域路径）；操作步骤见 case c10 |
| task-14 | f17, f15；操作步骤见 case c11 |
| task-15 | f04（PLI 机制）；操作步骤见 case c12 |
| task-16 | f13；操作步骤见 case c13 |
| task-17 | f18；操作步骤见 case c14 |
| task-18 | f18 |
| task-19 | f12（dectview 标志）, f13（xbssynchro/incvisu）, f16（downstat） |
| task-20 | f06 |

全部 20 项 task 均有对应条目，无缺口。
