# 术语/缩写/产品名候选 — OmniPCX Enterprise DECT Solutions (DECTXTE200EN Ed12)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 55 条。分类口径：concept/role/subscription/product/protocol/resource 六类；本书为本地部署教材、无订阅体系，subscription 类无条目（见类首注）。缩写书中未给全称的（VAD、CLIP、LLDP-MED、RTP、SIP、UA、IPEI 等）full_name 如实标注"书中未展开"，不采信外部知识。

```yaml
# ── 一、概念 (concept) ──

- id: g01
  term: DECT
  full_name: Digital Enhanced Cordless Telecommunications（书中直接展开）
  category: concept
  source_pages: p4-6
  source_quote: |
    "DECT for Digital Enhanced Cordless Telecommunications ... The DECT standard is published by the
    ETSI (European Telecommunication Standard Institute) ... developed as a European standard since
    1993 and was later adopted by more than 110 countries ... In United States it has been adopted in
    2005" (p4)
  definition: |
    ETSI 发布的数字增强无绳通信标准，OXE 无绳移动的空中接口底座：蜂窝技术、分国频段、宏密度
    （10000 E/Km² 量级）、带漫游/切换/鉴权加密。日本仍用 PHS（p4）。
  alias_or_related: ETSI（标准组织）；与 DECT Protocol（空中接口协议，g44 语境）同源
  tags: [concept, standard]

- id: g02
  term: Cell（小区）
  category: concept
  source_pages: p6, p13
  source_quote: |
    "The radio coverage over a base station is called a cell" (p6)
    "The range of a transmitter (the cell size) depends on the environment ... Cells may overlap
    partially or totally to increase traffic density" (p13)
  definition: |
    一个基站的无线电覆盖范围。功率恒定 250mW，小区大小由环境决定；小区可部分/完全重叠以提升话务密度，
    非相邻小区可复用"频率+时隙"。
  alias_or_related: 与 coverage（覆盖）连用
  tags: [concept, radio]

- id: g03
  term: Roaming（漫游）
  category: concept
  source_pages: p23-24, p87-88
  source_quote: |
    "Allows the user to make or receive calls from any location in the PCX coverage area ... Roaming
    implements a mechanism whereby the mobile is recognized by the system (and vice versa), called
    the 'location phase'" (p23)
    "Roaming is possible between sites" (p88)
  definition: |
    用户在覆盖区内任意位置收发呼叫的能力；前提是手机常开且已注册。空闲态靠"定位阶段"让系统与手机互相
    识别。跨 Site 仍可 roaming（但无 handover）。
  alias_or_related: location phase（g05）
  tags: [concept, mobility]

- id: g04
  term: Handover（切换）
  category: concept
  source_pages: p25-26, p87
  source_quote: |
    "Process permitting a transparent change of Base Station during a communication ... all the base
    station must start their DECT frame at exactly the same time. This condition implies highly
    accurate synchronization" (p25)
    "Handover is only available on a same site" (p87)
  definition: |
    通话中在基站间透明切换；要求全网帧级同步（整个同步体系存在的理由）。作用域是 Site 内；跨 Site、跨
    簇、（IBS）跨网关均无切换。
  alias_or_related: Connection handover（g17，IP 中继切换）；External Handover（跨 PARI 切换，c13）
  tags: [concept, mobility, handover]

- id: g05
  term: Location phase（定位阶段）
  category: concept
  source_pages: p23-24
  source_quote: |
    "The handset regularly scans all radio channels ... The mobile selects the base station with the
    most powerful signal ... The handset transmits its information (IPUI + PARK) ... The handset
    compares system PARI with its PARK number ... the mobile 'locks onto' the system" (p24)
  definition: |
    手机与系统的互相识别流程：扫描测信号→选最强站→上报 IPUI+PARK→基站回 RFPI→手机比对 PARI/PARK→
    锁定系统。锁定后即可正常收发。
  alias_or_related: Roaming（g03）的实现机制
  tags: [concept, mobility]

- id: g06
  term: Location area（位置区）
  category: concept
  source_pages: p84-85
  source_quote: |
    "Location areas may be defined, to optimize the traffic in case of high density installation ...
    Inside a PARI, up to 64 location areas may be defined" (p84)
  definition: |
    按 RPN 区间划分的寻呼优化分区（每 PARI 最多 64 个），高密度安装时缩小 DECT 终端搜索范围；管理员给
    基站配区号后系统自动分配区内空闲 RPN。
  alias_or_related: Area type 配置项（"1 area of 256 xBS"，p145）
  tags: [concept, paging]

- id: g07
  term: Site（站点/同步域）
  category: concept
  source_pages: p86-92
  source_quote: |
    "A SITE is a group of 8378 DECT IP-xBS linked to a call server and located in the same
    geographical location where it is possible to do handover ... By default, all base stations are
    in the same site" (p86, p89)
  definition: |
    可做 handover 的同地理位置 xBS 组——切换的边界单位。默认全部基站属 Site 0；一个 PARI 可拆多 Site、
    一个 Site 可跨多 PARI（此时需配 PARI 间同步链路）。
  alias_or_related: 与 branch office（分支办公）场景对应
  tags: [concept, site, handover]

- id: g08
  term: Internal synchronization（内部同步）
  category: concept
  source_pages: p100, p113-114
  source_quote: |
    "Internal Synchronization is a set of 8378 DECT IP-xBS inside the same PARI of a same SITE which
    are synchronized (time aligned) together" (p100)
    "The criteria ... Link quality / RSSI ... Optimization of the number of hops to the root ... There
    is no configuration needed by default" (p114)
  definition: |
    同 Site 同 PARI 内 xBS 的空中时间对齐；同步树按 RSSI+跳数自动构建（最深 24 级）、随无线环境自动重构，
    默认零配置。
  alias_or_related: Sync Master（g20）；Sync Cluster（见 g11 相关注）
  tags: [concept, synchronization]

- id: g09
  term: External synchronization（外部同步）
  category: concept
  source_pages: p105-109
  source_quote: |
    "The External Synchronization allows to synchronize two sets of xBS which are synchronized with
    Internal Synchronization; or it allows to synchronize a set of xBS with a set of TDM base
    stations" (p105)
  definition: |
    两个同步树之间的对齐：xBS 树↔xBS 树或 xBS 树↔TDM 基站树。Master Sync 与 External Sync RPN 手工
    指定，Backup Sync Master 强制；是跨 PARI/混合部署获得切换能力的前提。
  alias_or_related: Sync Master（g20）、Backup Sync Master（g21）、Sync Highway（g10）
  tags: [concept, synchronization]

- id: g10
  term: Sync Highway（同步高速通道）
  category: concept
  source_pages: p111-112, p141
  source_quote: |
    "When more than 2 PARIs are synchronized together using external sync, additional configuration is
    needed: a synchronization highway" (p111)
  definition: |
    3 个及以上 PARI 做外部同步时所需的附加同步配置（让多棵同步树串联成链）；工程规则决策树的分支条件
    之一（p141）。
  alias_or_related: External synchronization（g09）
  tags: [concept, synchronization]

- id: g11
  term: Mixed mode（混合模式）
  category: concept
  source_pages: p63, p191, p242-248
  source_quote: |
    "Radio base type xBS or Mixed" (p144)
    "Setup an IP-xBS solution on a site with an existing IBS infrastructure ... The PLI value will be
    30" (p244)
  definition: |
    同一台 OXE 同时跑 TDM（IBS）与 IP（xBS）基站的部署形态：Radio base type=Mixed、多 PARI（每类硬件
    一个）、PLI 必须适配。是存量 TDM 演进到全 IP 的主路径。
  alias_or_related: Multi-PARI（g16）、PLI 适配（principle p23）
  tags: [concept, mixed, migration]

- id: g12
  term: Dual cell（双小区）
  category: concept
  source_pages: p272, p288-291
  source_quote: |
    "Offers single/dual DECT cell indoor coverage • Two cells topology: Roaming & handover available •
    Stations located within the same IP subnet • NTP mandatory" (p272)
    "As well as the second one will be plugged and will have access to the network, it will detect the
    first one and will retrieve its configuration from this one automatically." (p288)
  definition: |
    两台 8328 组成的主/从小区：副站自动发现主站并拉取全部配置（仅副站需先配 DHCP）；区内有 handover 与
    roaming；链路建立约 5 分钟。8328 体系中唯一的切换形态。
  alias_or_related: Primary/Secondary station（g23）
  tags: [concept, sip-dect]

- id: g13
  term: Bi-cellular deployment（双小区部署，IP-xBS 语境）
  category: concept
  source_pages: p275
  source_quote: |
    "Except of course in case of bi-cellular deployment (as in 'Area 1' in the above drawing) ...
    Handover & roaming between the 2 Base Stations" (p275)
  definition: |
    多台 8328 各自成区时区间无切换；唯独"双基站小区"部署在两站间有 handover/roaming。区别于 g12 的
    主/从自动配置语境，此处强调"两站一区"的覆盖形态。
  alias_or_related: Dual cell（g12）
  tags: [concept, sip-dect]

- id: g14
  term: Survey mode（勘测模式）
  category: concept
  source_pages: p211, p214-216
  source_quote: |
    "The 'Site Survey Kit' (SSK) allows you to do a Site Survey" (p211)
    "Enter the code *7378423* (mnemonic: *service*) ... Select 'Site Survey mode'" (p214)
  definition: |
    手机侧调试/勘测模式：菜单密钥 *7378423* 激活，顶层显示 RSSI/基站列表/RFPI，用于画覆盖边界
    （-70/-60dBm 门槛）；调试专用、耗电、不得给最终用户常开。
  alias_or_related: SSK（g28）；RSSI（principle p14）
  tags: [concept, survey]

- id: g15
  term: SUOTA / FWU
  full_name: SUOTA = Software Upgrade Over The Air（书中直接展开）；FWU 书中未展开
  category: concept
  source_pages: p58, p179-181
  source_quote: |
    "SUOTA Software Upgrade Over The Air (DECT Phone set firmware upgrade)" (p58)
    "The handset firmware MUST support FWU protocol in order to allow an on-the-air upgrade" (p181)
  definition: |
    手机固件空中升级能力总称：OXE 经无线信道下发固件，语音优先、回充电座生效；手机固件须支持 FWU 协议
    才可空中升级，否则 USB 手动。管理入口 downstat m。
  alias_or_related: downstat m（g54）；与基站固件升级（downstat x/TFTP）区分
  tags: [concept, firmware]

- id: g16
  term: Multi-PARI（多 PARI）
  category: concept
  source_pages: p18-20, p106, p244
  source_quote: |
    "Used in a Multi PARI configuration" (p18)
    "Several PARI are needed In case of large Sites with more than 254 base stations" (p106)
  definition: |
    一台 OXE 上并存多个 PARI 的形态：驱动因素是混合硬件（每类硬件一个 PARI）或超 254 台扩容；配套要求
    PLI 适配（p227 WARNING）与外部同步。
  alias_or_related: PLI（g50 逻辑 AND 缩位）；Mixed mode（g11）
  tags: [concept, pari]

- id: g17
  term: Connection handover（IP 中继切换）
  category: concept
  source_pages: p74, p95-97
  source_quote: |
    "All signaling and media redirection within the IP-xBS DECT subsystem are managed by the IP-xBS
    subsystem itself (Connection Handover) ... media is rerouted between the base stations" (p74)
    "IP-xBS Base Station supports simultaneoulsly 11 DECT radio communications + 11 IP Relays." (p97)
  definition: |
    IP-xBS 体系内切换的实现方式：Call Server 只连初始基站，切换时新旧基站间建 IP 中继（信令+媒体）转发；
    每站 11 路 IP 中继与 11 路无线通话并存，切换瞬间双链路占用。
  alias_or_related: Data Sync Primary（g22）管中继协调
  tags: [concept, handover, ip-xbs]

- id: g18
  term: Visited node（访问节点）
  category: concept
  source_pages: p181, p253
  source_quote: |
    "Handsets on visited node in case of roaming/campus are not downloaded" (p181)
    "Handsets connected to a visited node in case of OXE DECT networking" (p253)
  definition: |
    多节点 OXE DECT 网络（Campus）中手机漫游到达的非安装节点。三类远程操作（固件下载、自动重注册）对
    处于访问节点的手机不生效——批量作业前要确认手机回到安装节点。
  alias_or_related: OXE DECT networking（Campus 拓扑）
  tags: [concept, multi-node]

- id: g19
  term: 安全三级（Identity / Authentication / Encryption）
  category: concept
  source_pages: p35-37
  source_quote: |
    "Identity mode ... based on verification of the IPUI-N number ... Authentication mode ... used
    when: The handset is installed / A call is setup / The mobile is located / The handset is
    uninstalled ... Encryption mode ... initiated at call setup" (p35)
  definition: |
    DECT 安全的三个级别：身份核对（默认）→ 双向鉴权（AC 派生 UAK 挑战，四个时机触发）→ 通话加密（每
    呼叫派生 DCK）。级别在系统 Security level 配置；IBS 无加密（n01）。
  alias_or_related: AC（g52）、UAK（g53）、DCK（g54）
  tags: [concept, security]

# ── 二、角色 (role) ──

- id: g20
  term: Sync Master（同步主站）
  category: role
  source_pages: p101, p106
  source_quote: |
    "A SYNC MASTER is the 8378 DECT IP-xBS root of the internal synchronization tree ... The Sync
    Master is automatically selected by the xBS subsystem and it may change over the time" (p101)
    "The selection of the base station used for external synchronization ('Master Sync' and 'External
    Synchronization RPN' is done manually ... The Sync master base station does not support any
    communications" (p106)
  definition: |
    同步树的根基站。内部同步时自动选举、可随环境漂移；外部同步时手工指定且禁止承载通信（纯同步站）。
  alias_or_related: dectview xbs 状态字 M（Master configured）
  tags: [role, synchronization]

- id: g21
  term: Backup Sync Master（备份同步主站）
  category: role
  source_pages: p106, p109
  source_quote: |
    "A backup Sync Master must also be setup and configured ... This Backup Sync Master needs to be
    placed near to the Sync Master, it must see the same External Sync BS" (p106, p109)
  definition: |
    外部同步时的强制冗余角色：主站故障时接管同步；必须与主站邻近且看得见同一外部同步源；可补承主站
    不支持的话务（主备切换后该话务即失）。
  alias_or_related: dectview xbs 状态字 B（Backup configured）
  tags: [role, synchronization]

- id: g22
  term: Data Sync Primary（数据同步主站）
  category: role
  source_pages: p93-94, p116
  source_quote: |
    "The Data Sync Primary is a xBS base station in charge of synchronizing the data between all the
    xBS base stations of a PARI inside a Site ... Handover is only possible between base stations with
    the same Data Sync Primary" (p93)
  definition: |
    每个 Site/PARI 对自动选出的数据汇集站：协调同步树优化、切换（谁在中继的查询中枢）、基站状态与对
    OXE 的状态上报。切换可行域的隐形边界。
  alias_or_related: dectview xbs 状态字 P；xbssynchro 从它取同步树（p116）
  tags: [role, synchronization, handover]

- id: g23
  term: Primary / Secondary station（8328 主站/副站）
  category: role
  source_pages: p288-291
  source_quote: |
    "THE PRIMARY STATION WILL BE THE STATION WITH ALREADY AT LEAST ONE EXTENSION DECLARED." (p288)
  definition: |
    8328 双小区中的两角色：主站=先声明 Extension 的那台（数据源），副站自动发现并拉取配置；主站 Home/Status
    的 Dual Cell 区可见副站。
  alias_or_related: Dual cell（g12）
  tags: [role, sip-dect]

# ── 三、订阅 (subscription) ──
# 本书为本地部署教材，OXE DECT 无订阅/许可体系（仅 8328 场景提及"每台 DECT 终端需 1 个 SIP 用户许可"，
# p277-278，归入 product 语境），故本类无条目。

# ── 四、产品 (product) ──

- id: g24
  term: 8378 DECT IP-xBS
  category: product
  source_pages: p55-64
  source_quote: |
    "IP-xBS is a DECT mobility solution with base stations connected via the IP network and clock
    synchronized over the air ... 12 radio channels - 11 simultaneous voice communications ... Full IP
    Solution" (p57-58)
  definition: |
    全 IP DECT 基站产品线（本书主线）：UA/UDP 信令、RTP 直达媒体、空中互同步、PoE Class 2、每站 11 通话
    +11 IP 中继、每节点 8 PARI/2032 台；三个硬件型号（3BN67365AA 集成天线 / 3BN67366AA 外置天线 /
    3BN67367AA 室外，p65）。
  alias_or_related: IP-xBS；兼容 OXE R12.2+（p60）
  tags: [product, ip-xbs]

- id: g25
  term: 8379 DECT IBS
  full_name: IBS = Intelligent Base Station（书中直接展开）
  category: product
  source_pages: p218-225
  source_quote: |
    "IBS for Intelligent Base Station • Connected on an UA board (UAI and MIX) • 1 UA link or 2 UA
    links ... Only one PARI number available • Up to 256 base stations for the entire system" (p219)
  definition: |
    TDM DECT 基站产品线：接 UA 板卡、1/2 条 UA 链路对应 3/6 个 B 信道、全网单 PARI/256 台、无加密
    （Common Hardware）、handover 要求同 media gateway；三型号+ATEX 变体（3BN77020EA，p222）。
  alias_or_related: IBS 1G/2G 代际（p230）；SYT/LY278 布线（p220）
  tags: [product, ibs, tdm]

- id: g26
  term: 8328 SIP-DECT
  category: product
  source_pages: p271-278
  source_quote: |
    "8328 SIP-DECT Single Base Station ... Target: small areas requiring a limited number of cordless
    handset ... Supports up to 20 DECT handsets ... 10 simultaneous communications using G.711 / 4
    simultaneous communications using G.729" (p272)
  definition: |
    低成本单站 DECT 产品线：基站以 SIP 语义接入 OXE（每机 1 个 SIP 许可）、仅 8214 手机、仅欧洲频段、
    HTTPS WBM 管理、双小区可切换；PARI/PLI 体系不适用（p7 脚注）。
  alias_or_related: 8214 手机（g27）；Dual cell（g12）
  tags: [product, sip-dect]

- id: g27
  term: 82xx DECT 手机家族
  category: product
  source_pages: p28-30, p70, p181, p252
  source_quote: |
    "A-GAP Mode • 8234, 8244 and 8254 • 8262 and 8262EX ... GAP mode • 8214 • 8234, 8244 and 8254 •
    8262, 8262EX" (p30)
    "bin8212 ... bin8214 ... bin8232 ... bin8234_8254 ... bin8242 ... bin8244 ... bin8262 ... bin8262EX" (p181)
  definition: |
    支持机型谱系：8214（仅 GAP）、8234/8244/8254（GAP+A-GAP）、8262/8262EX（GAP+A-GAP，防溅型 EX）；
    遗留机型 8212/8232/8242（仅存固件二进制与 SSK 勘测机）。自动重注册支持 82x4 全系（版本表 p252），
    OTA 支持 82xx 全系（p179）。
  alias_or_related: GAP（g34）、GAP+/A-GAP（g35）
  tags: [product, handsets]

- id: g28
  term: Site Survey Kit（SSK）
  category: product
  source_pages: p211
  source_quote: |
    "The content of the DECT Site Survey Kit is: One suitcase ... One 8378 IP-xBS integrated antenna
    dedicated for the survey kit ... 2x 8242 DECT handset ... Ref: 3BN67191AA Telescopic Tripod ...
    3BN67192AA" (p211)
  definition: |
    官方勘测套件（TDM DECT/IP-xBS/IP DECT 通用）：专用 8378 xBS 两台（集成/外置天线）、8dBi 天线、充电宝
    供电、2×8242 勘测手机与充电配件、拉杆三脚架（3BN67191AA）等；配合手机 survey mode 做现场勘测。
  alias_or_related: Survey mode（g14）；勘测机型为 8242（与交付机型 82x4 不同，见批判）
  tags: [product, survey]

- id: g29
  term: 8379 IBS ATEX
  category: product
  source_pages: p222
  source_quote: |
    "Options • 3BN77020EA IBS 8379 ATEX Base Station" (p222)
  definition: |
    IBS 的防爆（ATEX）变体基站，用于危险环境场景的选型项。
  alias_or_related: 8379 IBS（g25）
  tags: [product, ibs, atex]

- id: g30
  term: IP-xBS 天线系列
  category: product
  source_pages: p66-69
  source_quote: |
    "3BN67365AA - 8378 DECT IP-xBS integrated antennas ... 3BD52206AA - Directive antenna with 8.0 dB
    gain, circular left polarization ... 3BN67185AA 8dBi Gain Antenna ... 3BN67395AA DECT 7dBi
    omnidirectional antenna" (p65-68)
  definition: |
    外置天线与附件选型目录：8.0dB 定向（左/右旋圆极化，SMA）、8dBi 双极化（+45°/-45°，含 SMA/TNC 线）、
    7dBi 全向（N 型）；配套跳线/抱杆/壁挂/吊装件（3BD52211AA 等，p69）。天线增益与极化是勘测设计的
    输入项。
  alias_or_related: SSK（g28）
  tags: [product, antenna]

- id: g31
  term: OmniPCX Enterprise（OXE）
  category: product
  source_pages: p1, p42, p60
  source_quote: |
    "OMNIPCX ENTERPRISE - R101.1 MD4" (p1)
    "OXE CSA Phys: 192.168.1.1 Main: 192.168.1.3 ... OMS CSA CSB 192.168.1.13" (p42，实验口径)
  definition: |
    本书宿主 PBX：Call Server（CSA 物理机/Main 虚机）、OMS 管理服务器、GD4 网关板、MIX484/UAI UA 板卡
    等构成；DECT 三产品线都注册在它上面。IP-xBS 要求 OXE R12.2 起（p60）。
  alias_or_related: OMS、GD4、MIX484/UAI16-1（UA 板卡，p219）；CSA/CSB
  tags: [product, oxe]

# ── 五、协议 (protocol) ──

- id: g32
  term: FDMA / TDMA / TDD
  full_name: Frequency-Division Multiple Access / Temporal-Division Multiple Access / Temporal-Division Duplex（书中直接展开）
  category: protocol
  source_pages: p9-12
  source_quote: |
    "FDMA: Consists of dividing the bandwidth of the communication medium into separate frequency
    bands ... TDMA: dividing the time ... into small intervals ... TDD: multiplex in time the
    transmission and the reception" (p9)
  definition: |
    DECT 空中接口的三重复用：10 载波分频 × 每帧 24 时隙分时 × 上下行同频时分；合计 120 个复用无线信道。
    IBS/xBS 容量差异的时隙来源（6/12 TS）。
  alias_or_related: 帧结构（principle p03）
  tags: [protocol, radio]

- id: g33
  term: GAP
  full_name: Generic Access Profile（书中直接展开）
  category: protocol
  source_pages: p28
  source_quote: |
    "GAP protocol • Generic Access Profile ... International and multi-manufacturer protocol ... Provides
    basic services: CLIP, Mono-line extension, Access to the various services by prefixes and suffixes
    ... Registration possible on 5 different GAP systems" (p28)
  definition: |
    国际多厂商无绳接入标准协议：基础服务（CLIP、单线扩展、前后缀取服务）、可注册 5 个 GAP 系统；手机侧
    表现为菜单级功能（选语言/锁键盘/音量三档等）。8214 仅支持 GAP。
  alias_or_related: CLIP（书中未展开）；UA 侧翻译（"The GAP protocol is translated into SIP signaling"——
    原文语境为 UA 板翻译为信令，p28）
  tags: [protocol, handset]

- id: g34
  term: GAP+ (A-GAP)
  full_name: Advanced Alcatel GAP protocol（书中直接展开）
  category: protocol
  source_pages: p29-30
  source_quote: |
    "GAP + (or A-GAP) • Advanced Alcatel GAP protocol ... Provides the advanced services: Multi-line
    extension, Supervision key, Manager/Assistant extension with screening / un-screening keys" (p29)
  definition: |
    ALE 私有增强协议（基于 GAP）：多线扩展、监督键、经理/秘书键等高级功能；需 8234/8244/8254/8262/8262EX
    机型。用户建卡时 Set type 选 GAP+ 还是 GAP 决定功能面。
  alias_or_related: GAP（g33）
  tags: [protocol, handset]

- id: g35
  term: UA protocol
  full_name: 书中未展开（ALE 私有信令协议）
  category: protocol
  source_pages: p5, p71-72
  source_quote: |
    "UA Protocol (for IP-xBS / IBS Base Stations)" (p5)
    "Works as a NOE IP phones ... Connection to OXE Call Server with UA / UDP for configuration and
    signaling ... The IP-xBS acts as a DECT / UA / UDP / IP bridge" (p71-72)
  definition: |
    OXE 与基站间的私有信令协议：IP-xBS 像 NOE 话机一样经 UA/UDP 单播注册与信令，DECT 空口消息封装在
    UA 内（DECT/UA/UDP/IP 桥）；IBS 同样走 UA 板卡链路。
  alias_or_related: NOE（书中作为类比出现）；UDP/IP 承载
  tags: [protocol, signaling]

- id: g36
  term: SIP（SIP-DECT 语境）
  full_name: 书中未展开
  category: protocol
  source_pages: p271-278
  source_quote: |
    "Since the SIP-DECT configuration in OXE is based on SIP users" (p7)
    "'SIP Register' on OXE made by the base station during the DECT handset registration ... 1 SIP
    user license is needed per DECT device" (p277)
  definition: |
    8328 体系的接入语义：OXE 侧手机= SIP Extension 用户；注册链路由基站代手机完成 SIP register
    （contact=号码@基站 IP）；每台 DECT 终端消耗 1 个 SIP 用户许可。
  alias_or_related: Registrar/contact（SIP 注册表概念，书中以用法出现）
  tags: [protocol, sip-dect]

- id: g37
  term: RTP 与编解码（G.711 / G.729）
  full_name: RTP 书中未展开；G711 (A-µ law) / G729A/B 为书中写法
  category: protocol
  source_pages: p58-59, p73
  source_quote: |
    "RTP Media stream direct, network topology must be adapted to Voice over IP - Codecs supported:
    G711 (A-µ law), G729A/B" (p59)
    "The media stream (RTP) is direct between an IP set or trunk and an IP-xBS base station ... codec
    are G711 and G729A ... VAD on G729" (p58, p73)
  definition: |
    IP-xBS 媒体面：RTP 流在话机/中继与基站间直达（不经 Call Server）；编解码 G.711（A/µ 律）与
    G.729A/B（带 VAD）。8328 则按编解码限容量（G.711 10 路/G.729 4 路，p272）。
  alias_or_related: VoIP 网络适配要求（QoS/带宽）
  tags: [protocol, media]

- id: g38
  term: LLDP-MED
  full_name: 书中未展开
  category: protocol
  source_pages: p59
  source_quote: |
    "LLDP-MED compliant for network topology discovery" (p59)
  definition: |
    IP-xBS 支持该邻居发现协议，用于网络拓扑自动发现（与 QoS/VLAN 并列的网络特性项）。
  alias_or_related: —
  tags: [protocol, network]

- id: g39
  term: NTP
  full_name: 书中未展开
  category: protocol
  source_pages: p76, p148, p272
  source_quote: |
    "Time on IP-xBS provided by NTP ... The NTP server gives a UTC time. The DST (Daylight Saving
    Time) is given by the Call Server" (p76)
    "The timer server is the OXE. This information is transmitted to the base station via the UA
    signaling link." (p148)
  definition: |
    基站时间来源：OXE 的 NTP 服务器给 UTC 时间、Call Server 给夏令时规则，初始化时经 UA 信令下发；
    8328 双小区 NTP 为强制项（p272）。
  alias_or_related: DST（Daylight Saving Time，书中直接展开）
  tags: [protocol, time]

- id: g40
  term: TFTP
  full_name: 书中未展开
  category: protocol
  source_pages: p59, p125, p129
  source_quote: |
    "Connection to OXE TFTP server" (p59)
    "IP-xBS firmware update • TFTP server • Manual update" (p125)
  definition: |
    基站固件自动升级的下载通道：DHCP 下发 TFTP 地址，基站从 OXE TFTP 取固件后台加载；IP DSP 软终端等
    也依赖 OXE TFTP（实验口径 192.168.1.3）。
  alias_or_related: DHCP（g41）；downstat x（g54）
  tags: [protocol, firmware]

- id: g41
  term: DHCP
  full_name: 书中未展开
  category: protocol
  source_pages: p59, p126-128, p146
  source_quote: |
    "Connection to DHCP server for IP config in dynamic mode (IP Static mode possible)" (p59)
    "A new Vendor Class for the xBS: Vendor id: alcatel.ipxbs.0" (p146)
  definition: |
    基站 IP 动态配置通道：内部 DHCP 为 xBS 新增 vendor class（alcatel.ipxbs.0），下发 IP/掩码/网关/
    TFTP/DNS；外部 DHCP 亦可；8328 要求放开"非 ALE 设备"（p280）。
  alias_or_related: vendor class alcatel.ipxbs.0（g52 资源类同款见 g53）
  tags: [protocol, network]

- id: g42
  term: Syslog
  full_name: 书中未展开
  category: protocol
  source_pages: p153, p160-161
  source_quote: |
    "Collect base station logs on a Syslog server • CS embedded syslog • An external syslog ...
    Default Syslog server port: 514" (p153)
  definition: |
    基站日志集中协议：服务器地址+端口（默认 514）在 OXE 配置，级别按基站四档设定；建议全站日志落同一
    文件便于分析；xBS 亦支持 PCAP 抓包（WBM）。
  alias_or_related: 日志四级口径（principle p18）
  tags: [protocol, logs]

- id: g43
  term: DECT Protocol（空中接口协议）
  category: protocol
  source_pages: p5
  source_quote: |
    "The DECT protocol is used between a cordless set and a DECT interface for accessing to the PABX
    ... Based on cellular technology" (p5)
  definition: |
    手机与 DECT 接口（基站）之间的空中接口协议，即 g01 标准在 OXE 语境下的协议层；与 UA（基站↔OXE）、
    SIP（8328 语境）分层并列。
  alias_or_related: GAP/A-GAP（其上的服务子集，g33/g34）
  tags: [protocol, air-interface]

# ── 六、资源/标识 (resource) ──

- id: g44
  term: PARI
  full_name: Primary Access Right Identifier（书中直接展开）
  category: resource
  source_pages: p14-15, p82
  source_quote: |
    "PARI: Primary Access Right Identifier, identification of the PABX, made of 31 bits or 8 hexa
    decimal digits ... A different PARI is mandatory per type of DECT hardware deployed on an OXE" (p14-15)
  definition: |
    PBX 侧系统标识：31 位（8 个十六进制位 / 11 个八进制位）；每类 DECT 硬件一个、每节点最多 8 个、
    每 PARI 254 台 xBS（IBS 256 台）。配置字段 PARI Value（如实验 100004101x0/x4）。
  alias_or_related: RPN（g45）、PARK（g47）、Multi-PARI（g16）
  tags: [resource, identification]

- id: g45
  term: RPN
  full_name: Radio Part Number（书中直接展开）
  category: resource
  source_pages: p14, p16, p83
  source_quote: |
    "RPN: Radio Part Number: coded in two hexadecimal digits ... Id allocated to the base station by
    the PBX" (p14, p16)
    "The RPN is used for geo-location of DECT handsets ... also used for the synchronization over the
    air to identify a base station" (p83)
  definition: |
    系统分配给基站的空中接口标识（2 个十六进制位）：手机地理定位与空中同步识别的依据；只读字段（注册后
    自动分配），换站手动注册可保持不变。
  alias_or_related: RFPI=PARI+RPN（g46）
  tags: [resource, identification]

- id: g46
  term: RFPI
  full_name: Radio Fixed Part Identifier（书中直接展开）
  category: resource
  source_pages: p14, p22
  source_quote: |
    "RFPI: Radio Fixed Part Identifier, identification of the Base station composed of the PARI and of
    the RPN ... Number emitted by the Base Station" (p14, p22)
  definition: |
    基站空中广播的标识=PARI+RPN 的组合；定位阶段基站把它回给手机，手机取其中的 PARI 与本地 PARK 比对。
    survey mode 的 Vol- 屏可显示 RFPI（p216）。
  alias_or_related: PARI（g44）、RPN（g45）
  tags: [resource, identification]

- id: g47
  term: PARK
  full_name: Portable Access Right Key（书中直接展开）
  category: resource
  source_pages: p14, p17-18
  source_quote: |
    "PARK: Portable Access Right Key, identification of the DECT system in the set that corresponds to
    the PLI + the PARI number of this system (coded in 13 digits) ... PLI=31 and PARI=10000400100 →
    PARK=3110000400100" (p14, p17)
  definition: |
    注册时写入手机的 13 位系统识别号=PLI（2 位十进制）+PARI（11 位八进制）；手机以它（按 PLI 位数）与
    空中收到的 PARI 做逻辑 AND 决定是否锁定。
  alias_or_related: PLI（g48）
  tags: [resource, identification]

- id: g48
  term: PLI
  full_name: Park Length Indicator（书中直接展开）
  category: resource
  source_pages: p14, p18-20
  source_quote: |
    "PLI: Park Length Indicator (maximum value 31) ... The PLI determines how many bits, of the PARI
    received from the base station, must be compared to the local PARK • If the PLI is decreased, the
    handset is compatible with more PARI" (p14, p18)
  definition: |
    PARI 比对位数旋钮（最大 31）：单 PARI 用 31；multi-PARI/混合模式降位（实验 30/29）使相近 PARI 对同一
    手机等效。配置字段 PLI for CTM；自动重注册可经 -pli 推送新值。
  alias_or_related: Mixed mode（g11）；dectinston -pli
  tags: [resource, identification]

- id: g49
  term: IPUI
  full_name: International Portable User Identity（书中直接展开）
  category: resource
  source_pages: p14, p21, p169
  source_quote: |
    "IPUI: International Portable User Identity, identification of the handset international number
    written in the EPROM of the set composed by 14 octal digits" (p14, p21)
    "Once the device is registered ... you can see an update of the fields IPUI N, IPUI O" (p169)
  definition: |
    固化在手机 EPROM 的 14 位八进制国际标识：系统认机的依据。webadmin 用户页的 IPUI N/IPUI O 字段从空到
    有（注销时清除）是注册/注销的核验点。
  alias_or_related: IPEI（g50，同义呈现于命令输出）
  tags: [resource, identification]

- id: g50
  term: IPEI
  full_name: 书中未展开
  category: resource
  source_pages: p176, p286-287
  source_quote: |
    "IPEI: 1410309133756" (dectrm 输出，p176)
    "IPEI number is no more the generic/default one (FFFFFFFFFF)" (p286)
  definition: |
    手机身份标识（dectrm/8328 WBM 输出中的呈现形式）：8328 未注册时显示通用值 FFFFFFFFFF，注册后变为
    真实值；与 IPUI 的换算关系书内未给出。
  alias_or_related: IPUI（g49）
  tags: [resource, identification]

- id: g51
  term: AC（Authentication Code）
  full_name: AC = Authentication Code（书中直接展开）
  category: resource
  source_pages: p36, p144, p227, p285
  source_quote: |
    "This value is called AC for Authentication Code. A registration phase isn't possible if the AC
    key used in the PBX is different from the AC key used in the handset" (p36)
    "AC System 1111 ... The AC code is optional" (p144，实验口径)
  definition: |
    注册鉴权码：系统侧 AC System 字段与手机注册时输入必须一致，否则无法注册；可选项（不用则跳过输入）；
    8328 的对应物是基站侧 Access Code（默认 0000，可改）。它是 UAK 的派生种子（双侧共享秘密）。
  alias_or_related: UAK（g53）
  tags: [resource, security]

- id: g52
  term: UAK
  full_name: User Authentication Key（书中直接展开）
  category: resource
  source_pages: p36
  source_quote: |
    "This key (128 bits) is called UAK for User Authentication Key. For security reason, it can't be
    broadcasted. ... It is calculated from the AC (Authentication Code) ... registered in each mobile
    and in the database of the system" (p36)
  definition: |
    128 位用户鉴权密钥：由 AC 派生，存于手机与系统库，从不上空口/逻辑链路传输；鉴权挑战的双侧算据。
    自动重注册不重算 UAK（p253）。
  alias_or_related: AC（g51）、DCK（g53 相关）
  tags: [resource, security]

- id: g53
  term: DCK
  full_name: Derived Cipher Key（书中直接展开）
  category: resource
  source_pages: p36
  source_quote: |
    "a special random key (64 bits) is derived from UAK. This key is called DCK for Derived Cipher
    Key. A new DCK is computed at the beginning of each call and is maintained during the whole
    conversation, including conversations with handover(s)." (p36)
  definition: |
    64 位通话加密密钥：每次呼叫由 UAK 派生、全程（含切换）保持、不广播不传输；注销时随注册关系失效
    （存储于手机与 PBX 直至注销）。
  alias_or_related: UAK（g52）
  tags: [resource, security]

- id: g54
  term: 维护命令族（dectview / dectinston / dectrm / downstat / xbssynchro / incvisu 等）
  category: resource
  source_pages: p116, p137, p170, p176, p183, p230-234
  source_quote: |
    "dectview / dectinston / dectinfo / dectarea / dectobs / obstraf / ippstat / downstat / Domstat /
    tftp_check" (p137)
    "Oxe tool: xbssynchro ... Command: incvisu | grep xBS (or 60, 78)" (p116)
  definition: |
    mtcl 下的 DECT 命令族：状态（dectview xbs/ibs/com、dectinfo、dectarea）、注册注销（dectinston/-g/
    -update/-forceUpdate、dectrm）、固件（downstat x/m）、同步树（xbssynchro）、事件（incvisu|grep xBS）、
    UA 链路与 IBS 详情（listerm、listibs）、复位（outserv/inserv）、抓包（tcdump）。
  alias_or_related: 排障指南 8AL91443ENAA（p138）
  tags: [resource, commands]

- id: g55
  term: vendor class alcatel.ipxbs.0
  category: resource
  source_pages: p127, p146
  source_quote: |
    "A new Vendor Class for the xBS: Vendor id: alcatel.ipxbs.0" (p146)
  definition: |
    OXE 内部 DHCP 为 xBS 新增的厂商类标识：DHCP 以它识别 xBS 请求并下发专用选项（IP/掩码/网关/TFTP/
    DNS）；外部 DHCP 复现此机制需要支持 vendor class 匹配。
  alias_or_related: DHCP（g41）
  tags: [resource, dhcp]

- id: g56
  term: /usr2/downbin 与 /tmpd
  category: resource
  source_pages: p181, p257-258, p261
  source_quote: |
    "Binaries location on the Call Server: ... (1)csa> cd /usr2/downbin ... ll bin82*" (p181)
    "transfer the file via FTP/SFTP to the OXE directory: /tmpd ... Two Output files are generated in
    the same path as Input file" (p261, p257)
  definition: |
    两个关键路径：/usr2/downbin 存放手机固件二进制（bin8212…bin8262EX，downstat m b 可指定）；/tmpd 为
    批量重注册的输入清单（DECT.txt）与输出结果（ReinstallSuccessHandsetsList.txt /
    ReinstallNOKHandsetsList.txt）所在目录。
  alias_or_related: downstat m（g54）；dectinston -f
  tags: [resource, filesystem]
```

## 任务覆盖自检

| BOOK_OVERVIEW task | 对应 glossary 条目 |
|---|---|
| task-01 | g01-g05, g19, g32-g35, g44-g53（概念与标识资源全部支撑） |
| task-02 | g24, g25, g26（三条产品线） |
| task-03 | g31（OXE 实验平台组件） |
| task-04 | g24, g35, g37, g39-g41, g55 |
| task-05 | g45（RPN 语义） |
| task-06 | g42 |
| task-07 | g33, g34, g49, g51 |
| task-08 | g49, g50 |
| task-09 | g40, g54 |
| task-10 | g15, g54, g56 |
| task-11 | g07, g18 |
| task-12 | g14, g28 |
| task-13 | g25, g29 |
| task-14 | g11, g16, g48 |
| task-15 | g48, g54 |
| task-16 | g09, g10, g20-g22 |
| task-17 | g26, g36, g43 |
| task-18 | g12, g13, g23 |
| task-19 | g22, g54 |
| task-20 | g19, g51-g53 |

全部 20 项 task 均有对应条目，无缺口。
