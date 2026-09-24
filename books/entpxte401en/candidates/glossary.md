# 术语/缩写/产品名候选 — OmniPCX Enterprise Advanced (ENTPXTE401EN Ed13, R101.1 MD4)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 58 条。DDI/TFTP/WBM/MIPT/SIP/RTP/DTLS/IPSec/FQDN/NPD/T2 等缩写书中未给全称，full_name 字段如实省略，不采信外部知识；C.A.C/PCS/ABC-F2/DSS/DSU/REX/SCP/OMS 等书中已展开的照录。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: CS Duplication
  category: concept
  source_pages: p70-83, p92-138
  source_quote: |
    "Principle: duplication of the Call Server software platform • Main call server • Standby call
    server ... The standby Call Server database is updated in real time ... Updates must be done with a
    'secured copy protocol' (scp)" (p70-71)
  definition: |
    呼叫服务器软件平台复制：main + standby 成对运行，备库实时 scp 复制；主故障时切换（已建立通话保持、
    建立中丢失）。承载平台可为 CS 板卡（Common Hardware）、GAS 或虚拟机；两机必须同版本同类平台。
    部署 How-To 分本地（同子网）与空间（跨子网）两套。
  alias_or_related: mastercopy（g02）、spatial redundancy（g05）、参考 MG（g03）
  tags: [concept, redundancy, duplication]

- id: g02
  term: Mastercopy
  category: concept
  source_pages: p79, p106-108, p130-132
  source_quote: |
    "A database cloning operation, also called 'Mastercopy', is then necessary !" (p79)
    "swinst menu 2 Expert menu • 3 cloning & duplicate operations • 1 CPU cloning • 3 cloning database ...
    Do you wish to copy the DATABASE AND ACCOUNTING (y/n): y ... LINUX DATA (y/n, default n): y" (p107)
  definition: |
    数据库克隆操作：在备机上经 swinst 把主库（至少 DATABASE AND ACCOUNTING，可选 LINUX DATA/VOICE GUIDES/
    TRAFFIC/ACD）复制过来；前提=备机话音已停+SSH 密钥已分发。触发场景：冗余初始化、主备失联超 120 分钟
    （440 事件）、不停机升级的库同步步骤。
  alias_or_related: 与 pcscopy（g27）同族但目标不同；swinst 工具承载
  tags: [concept, mastercopy, database]

- id: g03
  term: Reference Media Gateway
  category: concept
  source_pages: p74, p76-77, p104, p127
  source_quote: |
    "A reference Media Gateway • This one is used when the call servers cannot exchange the 'keep-alive'
    messages (IP network problem) ... the main call server connected to the reference Media Gateway
    continues to authorize management (and broadcast)" (p74)
  definition: |
    参考 MG：double main 场景的裁判网关——两 CS 失联时连接参考 MG 的一侧成为 Real Main（保留管理权），
    链路恢复后未连它的一侧自动重启。声明路径 /Shelf/（实验口径选离 CS 最近的 OMS，MG #4 → Reference YES）。
  alias_or_related: Real Main / Pseudo Main（g33）；double main（g04）
  tags: [concept, redundancy, reference-mg]

- id: g04
  term: Double Main Mode
  category: concept
  source_pages: p76-77, p81-82
  source_quote: |
    "There are two main Call Server (Double Main Mode) on the network • a Real Main Call Server • a Pseudo
    Main Call Server" (p76)
    "Services not provided in Double Main mode: • Accounting ... • Traffic observation ... • One part of
    the network has no Voice Mail" (p82)
  definition: |
    IP 链路中断时网内出现两个"主"：Real Main（MAO 开，由参考 MG 裁决）与 Pseudo Main（MAO 关）。此期间话
    单与话务观察不合并、部分网络无语音邮箱；ABC-F 网络两侧不同步，恢复后靠修改文件交换与主库复制收敛。
  alias_or_related: g03 参考 MG、g05 空间冗余
  tags: [concept, double-main, fault]

- id: g05
  term: Spatial Redundancy
  category: concept
  source_pages: p80, p84-90, p115-138
  source_quote: |
    "It is possible to place the call servers in different IP sub-networks. This feature is called
    'Spatial Redundancy'" (p82)
    "Each CS uses its own router and a different subnet mask" (p85)
  definition: |
    两 CS 分处不同 IP 子网的冗余形态（机制与本地冗余相同）：各自物理地址与 main 角色地址（csma/csmb）、各
    自路由器；配套要求=内部 DNS（仅活动主应答节点名）或客户 DNS 委派到两个主地址、DHCP 由活动 CS 应答、
    IP 设备可填两个 TFTP/主地址。实验口径：csa 192.168.1.1/csma 1.3 ↔ csb 192.168.2.1/csmb 2.3。
  alias_or_related: g01 冗余的同形态；不等于异地容灾（网络层形态定义）
  tags: [concept, spatial-redundancy, dns]

- id: g06
  term: IP Domain
  category: concept
  source_pages: p141-152, p154-159
  source_quote: |
    "An IP domain corresponds to one or several IP address ranges / one or several hosts ... If there is
    no entry, the default IP Domain ('0') is allocated to the equipment" (p143)
    "1000 domains are manageable per system" (p152)
  definition: |
    按设备 IP 归属划分的逻辑域：OXE 在设备初始化时按域地址表（单地址/地址段+掩码）归类，未匹配落默认域 0；
    每系统 1000 域。域承载四类配置：CAC（g07）、时区/国家本地化、编解码带宽档（intra/extra）、资源分配
    （语音导引/会议电路跨域策略）。CS 必须域 0 且其他域不得覆盖 CS 地址。
  alias_or_related: Domain 0、IP Domain Address（地址条目对象）
  tags: [concept, ip-domain]

- id: g07
  term: C.A.C (Call Admission Control)
  full_name: Call Admission Control（书中展开）
  category: concept
  source_pages: p144, p147, p156, p159, p162
  source_quote: |
    "Call Admission Control (C.A.C) • Purpose of C.A.C is to control the link saturation between 2
    locations (Extra Domain Calls) ... 'Domain Max Voice Connection' parameter in the IP domain ('-1'
    means unlimited)" (p144)
  definition: |
    跨域呼叫准入：只控制"从/到某域"的通话条数（Domain Max Voice Connection，-1 不限），域内通话不受控；
    超限来电按呼叫类型与域带宽档处理，溢出退路靠 Local Private to Public Overflow。维护命令 cnx dom 的
    allowed/used/cac over 字段即读它。
  alias_or_related: g06 域的属性；g09 溢出为配套退路
  tags: [concept, cac]

- id: g08
  term: PCS (Passive Communication Server)
  full_name: Passive Communication Server（书中展开）
  category: concept
  source_pages: p164-184, p185-216
  source_quote: |
    "The PCS objective is to secure the telephone service in IP domains, different from the main call
    server IP domain ... Loss of the unique Call Server ... IP domain isolation" (p166)
    "The PCS can have 4 possible states ... Inactive ... Active ... Inactive* ... Undef" (p170)
  definition: |
    域级生存性的备用 CS：许可锁 332>0、版本≥CS、RAM≥CS；失联转 Active 接管域内设备（GD/OMS 软复位改连救
    援地址、话机重启用 TFTP Backup IP@），链路恢复按计时器回切（默认 30 秒/定点/0=人工）；库单向同步、修
    改即丢；最长连续激活 30 天。容量：240 台/系统，一域一 PCS、一 PCS 可救多域。
  alias_or_related: 状态查询 pcsview；库刷新 pcscopy（g27）；四状态详见 principle p19
  tags: [concept, pcs, survivability]

- id: g09
  term: Local Private to Public Overflow
  category: concept
  source_pages: p217-227, p228-233
  source_quote: |
    "'Local Private to Public Overflow' feature offers the possibility to reach a device of a remote site
    by rerouting the call via the public network in case of: - PCS (IP link failure) - No more available
    IP compressors - Maximum number of calls reached (CAC)" (p218)
  definition: |
    本地（域内）私到公溢出：跨域呼叫在 CAC 饱和/压缩机枯竭/断链（PCS 激活）时自动改经公网——CS 取 Node
    Access Prefix 的 ARS 前缀占中继、按 DID 段翻译外部号；双层权利（COS busy/OoS 开关 + 被叫外号闭锁），
    话务台恒放行；对 SIP 扩展/设备不适用；话单字段 26 记设施类型。
  alias_or_related: 组网版见 g29（Private to Public Overflow）；thin sector（g10）兜非 DID
  tags: [concept, overflow]

- id: g10
  term: Thin Sector
  category: concept
  source_pages: p224, p230-231, p511-513
  source_quote: |
    "A cleverness, called 'thin sector' allows to assign a DID number to a range of none DID users. All
    numbers, from the associated range, will be translated into a unique external number." (p224)
  definition: |
    DID 翻译的机制：把一段非 DID 内部号映射到唯一外部号（该段首外号），公网先打这个"第三方"号再转接到原
    始被叫；与"唯一内部号"方向相反。约束：该外号不得与 Node Access Prefix 既有 DID 段重叠；本地溢出场景
    下 Install No Last Part 留空、由 thin sector 提供缺省号。
  alias_or_related: Node Access Prefix（g28）的子对象 Node DID Translation 承载
  tags: [concept, did, thin-sector]

- id: g11
  term: Speed Dialing (Direct / by Range / Open / Timed)
  category: concept
  source_pages: p234-245, p246-254
  source_quote: |
    "Speed dial numbers can be: either direct speed dial numbers common to all entities and all network
    nodes • or speed dial numbers by range ... (up to 400)" (p236)
    "A speed dial number may be incomplete. It may correspond to a region, area or company." (p242)
  definition: |
    缩位拨号体系：统一索引表 0-32499（默认仅 4000 可配）；直接式（全网统一段，一号一前缀）与范围式（至多
    400 范围、实体至多 32 区，一范围一前缀）；每号可带目录名（入局按 Calling ID 显示、支持 call by name）、
    可选闭锁受控、可配溢出缩位号；开放缩位号允许不完整号用户补拨，配定时转发号可在超时后自动补全。
  alias_or_related: edabv 查询命令；cfgUpdate 扩容；实体映射 Entity Spd Dial Numbers Range
  tags: [concept, speed-dialing]

- id: g12
  term: Multiline
  category: concept
  source_pages: p257-261, p267-270
  source_quote: |
    "A set can have one or more directory numbers and each call number can be associated with one or more
    programmable lines keys ... Two kind of configuration • Multi-keys • Multi-directory numbers" (p257)
  definition: |
    多线：话机持一或多个目录号、每号可配多把线键；两种形态——Multi-keys（一号多键，多路并发）与 Multi-
    MCDU（多号一机，附加号可为 DID，键数无上限）。默认全部话机单线（SIP 扩展除外）。是监督键/经理助理/
    寻线 multiline 行为/多设备的公共前置。
  alias_or_related: 属性 Automatic Incoming/Outgoing Seizure、Selective Filtering
  tags: [concept, multiline]

- id: g13
  term: Supervision Key
  category: concept
  source_pages: p262-265, p271
  source_quote: |
    "A supervision key is used: To know the status of an equipment (free, busy, out of service) • To reach
    this equipment • To intercept calls ... RESTRICTION: AN ATTENDANT OR A HUNTING GROUP CAN'T BE
    SUPERVISED" (p262)
  definition: |
    监督键（仅 multiline 话机可用）：显示被监督方状态（部分忙/全忙/空闲/振铃/退服）、按键直呼或代接振铃来
    话；铃型五档、No Call 开关决定能否直呼。可监督话机/传真/他人语音邮箱（新留言通知）。上限：20 监督者/
    话机、100（网络 20）/邮箱、15000 键/系统。
  alias_or_related: multitool 菜单 1/5 查询；与经理助理键（g15）互补
  tags: [concept, supervision]

- id: g14
  term: Screening / Unscreening
  category: concept
  source_pages: p277-280, p291-293
  source_quote: |
    "Screening key: Immediate Forwarding by Origin ... Unscreening key: Immediate Pickup by Origin ... If
    the unscreening table is empty, all the calls will be forwarded to the assistant set." (p277)
  definition: |
    经理/助理过滤键：Screening=激活后仅过滤表内来话转助理（Immediate Forwarding by Origin）；Unscreening=
    激活后仅表内来话留经理、其余转助理（Immediate Pickup by Origin）。两者互斥激活；过滤表 1000 张×16 参
    数（内部号/中继组/缩位号/话务台/T2 号可混装）；Selective Filtering 决定只转经理主线。
  alias_or_related: g15 的配套；Screening Supervision 键供助理远程开关
  tags: [concept, screening, filtering]

- id: g15
  term: Manager/Assistant group
  category: concept
  source_pages: p274-285, p286-295
  source_quote: |
    "A Manager/Assistant group is made up of two multiline sets ... two keys must be managed • The
    'assistant call' key on the manager set • The 'manager call' key on the assistant set" (p276)
  definition: |
    经理/助理组：两台 multiline 话机经 Assistant Call（经理侧）/Manager Call（助理侧自动生成）键构成，兼
    直呼与监督；配套四个辅助键——Screening Supervision（助理远程开关过滤）、Assistant Away（助理报离开暂
    停过滤，每助理仅一键）、Routing Assistant（溢出助理顶班，每经理一名、可服务多经理）、Manager Mail（预
    设短信互发，5 条预设）。
  alias_or_related: multitool 菜单 2（Boss/Secretary）查询
  tags: [concept, manager-assistant]

- id: g16
  term: Hunting Group
  category: concept
  source_pages: p298-312, p316-322
  source_quote: |
    "Search types • Sequential • Cyclical • Parallel" (p299)
    "% authorized camp on calls = Max. Number of camp on calls authorized / number of active stations in
    the hunt group x 100" (p305)
  definition: |
    寻线组：组号聚合多用户，来话按搜索类型分发——Sequential（固定队头顺序）、Cyclical（队头轮转、均摊）、
    Parallel（并发同响）。成员随进出组切换组的 Connection COS/公网 COS（留 255 保留自己）/实体；进出组前缀
    默认 480/481；组空或 camp-on 百分比到限溢出到溢出号；可配 greeting guide 替代回铃；multiline 行为由
    系统参数 No Multi-line call in PCX（0/1/2）定义；一台话机仅属一个组。
  alias_or_related: pbxstat -f d / supgpbx -le 维护；ACD/CCD 分配坐席是另一体系（本书仅列为多设备禁用对象）
  tags: [concept, hunting-group]

- id: g17
  term: Call Pick-up (Group / Direct)
  category: concept
  source_pages: p306, p313-314, p323-326
  source_quote: |
    "Group call pick-up • To pick-up the call, simply dial the group call pick-up prefix ... Direct call
    pick-up ... the Direct call pickup prefix must be dialed and followed by the directory number" (p314)
  definition: |
    代接：组代接（拨组代接前缀即接同组振铃话机）与直接代接（前缀+被叫组号/振铃话机号）；前提=代接方 COS
    授权且被叫未受代接保护。Pickup 组无独立建组菜单——在用户属性填 PickupGroup Name 即自动成组，Groups/
    Pickup Group 只能查不能建。
  alias_or_related: zdpost d <号> |grep pickup_id 验证；寻线组另有 Pickup private call / External Pickup 开关
  tags: [concept, pickup]

- id: g18
  term: Desk Sharing (DSS / DSU)
  category: concept
  source_pages: p327-337, p338-351
  source_quote: |
    "A shared terminal is called a Desk Sharing Set (DSS) ... A roaming user using a DSS is called a Desk
    Sharing User (DSU) ... A user retrieves his telephony configuration by Log-in / log-off" (p329-330)
  definition: |
    办公桌共享：DSS=共享话机（真 MAC 注册，配 LogOn 键+Help Desk 键），DSU=漫游用户（虚拟 MAC aa:bb:分机
    号，配 OverLogOn/LogOff 键），登录即恢复键位/特性/邮箱。系统选项：登出免密、忙时重置（6004）、首次改
    密、定时自动登出、免重启即时登录（限 NOE3GEE/Essential/Enterprise 同族同节点无 AOM，IPDSP 除外）。
  alias_or_related: dsstat/ippstat/doministat DS 列维护；前缀 62/63
  tags: [concept, desk-sharing]

- id: g19
  term: Multi Device / Twinset
  category: concept
  source_pages: p352-364, p365-371
  source_quote: |
    "The twinset feature (also called tandem) is a logical association between two sets: a main set and a
    secondary set ... The number of sets can be extended up to 4 in a multi device user configuration" (p353)
  definition: |
    多设备用户：主站+至多 4 副站（twinset 为 2 台的旧称）逻辑关联，主站号即多设备号；主副必须 multiline；
    副站类型含 NOE IP/TDM/DECT/MIPT/IPDSP/SIP(SEPLOS)/REX/DSU（DECT 与 REX 各限 1）；禁用模拟/S0/话务台/
    ACD/寻线组成员/夜转/客房。建关联清空话机数据；状态语义：Partial busy、Specific supervision、主站退服
    三参数；快速移机=Twinset Get Call 前缀。
  alias_or_related: zdpost 的 tandem_* 字段；REX 振铃前缀 651
  tags: [concept, multi-device, twinset]

- id: g20
  term: Rapid Call Shift (Twinset Get Call)
  category: concept
  source_pages: p363, p368
  source_quote: |
    "Allows an active communication to move seamlessly from one set to the other • Seamlessly means that
    the remote party do not detect the change, neither on audio nor on display" (p363)
  definition: |
    快速移机：多设备用户的空闲一侧拨 Twinset Get Call 前缀（实验口径 652，Local features），当前通话无感
    迁移到本侧（对端听不出、屏显不变）。需 COS 放行 Twinset Get Call。
  alias_or_related: g19 的配套特性
  tags: [concept, rapid-call-shift]

- id: g21
  term: Direct IP Link
  category: concept
  source_pages: p383-398, p399-423
  source_quote: |
    "'ABC-F2 Direct IP link' is the ABC link NEW GENERATION, which ensures 'Full IP' ... To allow network
    calls between OXE nodes of a subnetwork without any VPN management • To replace ABC Hybrid link in
    the long term • No need anymore of H323 channels" (p384)
  definition: |
    ABC-F2 新一代节点间直连链路：子网内全互联（无中继节点）、RTP 装载在 ABC-F 信令内全 IP 直传、免 VPN/免
    H.323/免许可；信令 IPSec、媒体 DTLS/SIP TLS+SRTP；全网 ≥R100.0。系统选项 Disabled→Migrating（重启）
    →Enabled 不可逆；99 条空链自动生成、命名 Link_xx；接入规则与容量见 principle p39/p41。
  alias_or_related: ABC-F2（g38）；hybvisu/trkvisu/rsthyb 维护
  tags: [concept, direct-ip-link, networking]

- id: g22
  term: Audit
  category: concept
  source_pages: p424-443, p444-469
  source_quote: |
    "Audit is a tool allowing an exceptional coherency update of the OXE databases of the ABC network •
    Audit is done in two phases: 1-Construction of a reference database ... 2-Downloading of the reference
    database over the network" (p426)
  definition: |
    全网数据库一次性对账：阶段 1 在执行节点构建参考库（specific 对象全网收集、shared 对象取参考节点），
    阶段 2 把参考库下发全网；直改表（必须先模拟+强烈建议备份）；链式对象常需跑两遍；不审计对象（ARS/中继
    组前缀/IP 域）须本地配。新增节点的网络数据导入也靠它。
  alias_or_related: specific/shared objects；reference node；与 broadcast（g23）互补
  tags: [concept, audit]

- id: g23
  term: Broadcast
  category: concept
  source_pages: p469-486, p487-498
  source_quote: |
    "Broadcast application is a tool allowing a permanent coherency update of the OXE databases of the ABC
    network ... Broadcast process must be enabled manually" (p471, p473)
  definition: |
    数据库持续增量同步：MAO 修改→buffer 文件（cm_cb.sav）→默认 10 分钟落 LOG.N.S→各节点互比 lupd.dat 序
    号索取补齐→全网确认后删除；远端写失败产 RLOG。激活三法（cleanbroad -all / WBM / mao +br）；广播域
    128 个（-1..127）出/入向各三态；对象行为与 audit 联动。
  alias_or_related: prog_diff / maohist / mao -lupd 监控
  tags: [concept, broadcast]

- id: g24
  term: Network Number / Routing Number
  category: concept
  source_pages: p410-411, p456
  source_quote: |
    "A network number corresponds to a complete directory number of a remote user. So, 1 network number
    allows to call 1 specific remote user." (p410)
    "A routing number corresponds to a range of remote user's directory numbers." (p411)
  definition: |
    直链测试期（audit 前）指向远端用户的两种编号手段：Network No.=单个远端完整号（Prefix Meaning=Network
    No.，填网络号/节点号/类型 Station）；Routing No.=远端号段前缀（填网络号/节点号/位数）。audit 完成后
    远端用户自动以 network number 身份进入本地编号计划。
  alias_or_related: Translator/prefix plan 承载
  tags: [concept, numbering]

- id: g25
  term: Node Access Prefix
  category: concept
  source_pages: p222, p504-505, p511-513
  source_quote: |
    "Node access prefix is declared toward the remote node number ... Define a local prefix (preferably
    ARS) • Parameter: 'number to add' • Not broadcasted" (p505)
  definition: |
    节点接入前缀：溢出方向的路由钉子——指向远端节点号，内含本地 ARS/中继前缀（Number to add，不广播）、
    非 DID 第三方号（Install No Last Part，广播）、远端 DID 翻译（Node DID Translation 子菜单，广播）；
    DID 段至多 2000 条/前缀，可绑 IP 域或 MG。子网间场景对应 Network Access Prefix / Network DID
    Translation。
  alias_or_related: g09/g29 溢出的承载对象
  tags: [concept, node-access-prefix]

- id: g26
  term: Reference Node (audit)
  category: concept
  source_pages: p426, p432, p449-452, p463-464
  source_quote: |
    "The reference node is server. It asks simultaneously to the distant nodes the specific objects" (p437)
    "If the reference node is one remote node • Substitution of shared objects in the database" (p432)
  definition: |
    审计参考节点：shared 对象（各类 COS/资费/音色/定时器）以其数据库为准全网替换；specific 对象则全网收集。
    默认=运行 audit 的本地节点（节点问句直接回车）；可指定远端。新增空库节点做参考库构建时不得选自己。
  alias_or_related: audit 两阶段（g22）
  tags: [concept, audit, reference-node]

- id: g27
  term: pcscopy
  category: concept
  source_pages: p179, p209, p232
  source_quote: |
    "Manually: using a dedicated maintenance command ('pcscopy') • Automatically, at a preset time (daily
    or weekly)" (p179)
    "(1)csa> pcscopy ... 1 - PCS update ... PCS Database Update => End OK" (p209)
  definition: |
    PCS 库手动刷新命令（菜单 1=update 指定 PCS IP、2=日志）；自动刷新由 WBM 的 Daily/Weekly 计划承载。前
    提：双向 trusted hosts + hosts 文件条目 + SSH 密钥。改完溢出/OoS 参数后也要 pcscopy 同步 PCS。
  alias_or_related: g08 PCS 的数据面；更新单向 CS→PCS
  tags: [concept, pcscopy, pcs]

- id: g28
  term: Broadcast Area
  category: concept
  source_pages: p481, p483, p490
  source_quote: |
    "An area is made of a group of nodes • In area broadcast case, a node in another area is not concerned
    by modifications ... 128 broadcast areas can be used" (p481)
  definition: |
    广播域：把节点分组限定广播范围，大网里避免全网级联；出向三态（不广播/域内/全网）、入向三态（不收/仅本
    域/全网）；域号 -1（不属域）至 127 共 128 个；配置了域后 buffer/LOG 文件名变为 area_cm_cb.sav /
    A.Z.N.S。
  alias_or_related: g23 的范围控制参数
  tags: [concept, broadcast, area]

- id: g29
  term: Private to Public Overflow（组网场景）与 Public to Private Rerouting
  category: concept
  source_pages: p499-508, p509-516, p517-523, p524-536
  source_quote: |
    "The 'Private to public overflow' feature allows to redirect automatically internal ABC-F private
    network calls on the public network, as soon as the ABC link (Direct IP Links) is congested or out of
    service" (p501)
    "Public to private rerouting automatically redirects calls to a public network station, to a private
    ABC-F Direct IP link: so, this call will become an internal one" (p519)
  definition: |
    组网双向溢出对称对：私→公在直链拥塞/断链时经远端 Node Access Prefix + DID 翻译走公网（权利模型同本地
    溢出）；公→私用 Real Discriminator 按呼叫号挂 ARS 表，路由 1（TG=-1，去/加位还原内号重分析走专线）优
    先、路由 2 公网兜底，Time-based Route List 定序；-1 路由每表一条且首位；非 DID 不适用后者。
  alias_or_related: g25 Node Access Prefix、g09 本地版；两特性均免许可（p507）
  tags: [concept, overflow, rerouting]

# ── 二、角色/账户 (role) ──

- id: g30
  term: mtcl
  category: role
  source_pages: p10, p57, p94, p113, p160
  source_quote: |
    "Login Password ... mtcl / swinst / root — Superuser2580*" (p10, 实验口径设置表)
    "Log as 'mtcl' on the Call Server A • Command spadmin" (p94)
  definition: |
    OXE 电话侧维护账户：全书命令行维护（spadmin/netadmin 例外用 root、role/twin/bascul/domstat/cnx dom/
    compvisu/pcsview/pcscopy/multitool/edabv/pbxstat/zdpost/dsstat/ippstat/audit/prog_diff/maohist 等）
    的默认登录账户；也是 SSH 密钥三账户之一。
  alias_or_related: 与 g31 swinst、g32 root 并列；实验密码 Superuser2580*（实验口径）
  tags: [role, account, maintenance]

- id: g31
  term: swinst
  category: role
  source_pages: p10, p74, p107, p133, p209
  source_quote: |
    "Log as 'swinst' on the Call Server B • In 'swinst' menu, Select '1': Easy menu ... 7 Stop the
    telephone" (p107)
    "LINUX data managed by 'swinst'" (p74)
  definition: |
    软件安装维护账户与同名工具：Easy 菜单（DECT 注册/库备份恢复/空库/停起话音/改 IP/停机）与 Expert 菜单
    （克隆与复制、系统管理-autostart、数据库工具-空库创建等）；swinst 管的 Linux 数据随冗余链路复制（对
    照 netadmin 的不复制）。SSH 密钥三账户之一。
  alias_or_related: mastercopy 操作入口；版本信息在 mtcl 欢迎信息
  tags: [role, account, swinst]

- id: g32
  term: root
  category: role
  source_pages: p10, p59, p101, p193, p203, p445
  source_quote: |
    "The tool requires the root privileges" (p60)
    "On the CS: log as 'root' ... Command netadmin -m" (p193)
  definition: |
    系统超级账户：oxe-ssh-auth / oxe-nw-sshkey-sync 必须以 root 执行；防火墙等 netadmin 维护也常以 root 登
    录（-m 菜单模式）。SSH 密钥三账户之一。
  alias_or_related: 密钥路径 /root/.ssh/
  tags: [role, account, root]

- id: g33
  term: Real Main / Pseudo Main
  category: role
  source_pages: p76-77, p81, p105
  source_quote: |
    "Pseudo Main True/False ... True : Running « real main » + « pseudo main » • False : Running « real
    main » + « real main »" (p105)
  definition: |
    double main 期的两个角色：Real Main（连参考 MG、MAO 开、承担管理）与 Pseudo Main（MAO 关）。/IP/
    Duplication parameters 的 Pseudo Main 参数决定运行组合：True=real+pseudo（典型），False=real+real。
  alias_or_related: g03/g04
  tags: [role, redundancy]

- id: g34
  term: DSS / DSU（set function 角色化）
  category: role
  source_pages: p330-332, p341-345
  source_quote: |
    "Set Function = Desk Sharing Set ... Set Function = Desk Sharing User" (p341, p344)
  definition: |
    办公桌共享把"话机角色"做成用户/话机的 Set Function 属性：DSS（Desk Sharing Set，共享话机）与 DSU
    （Desk Sharing User，漫游用户）不是独立硬件，而是同一数据库对象的不同角色配置；DSU 自动获得虚拟 MAC。
  alias_or_related: g18；Users/TSC IP user 看 MAC
  tags: [role, desk-sharing]

- id: g35
  term: Manager / Assistant（键角色）
  category: role
  source_pages: p276, p287-288
  source_quote: |
    "The 31001 set is the Assistant • The 31002 set is the Manager ... Programmable key N°5 will be
    declared as 'Assistant Call' on the Manager set." (p287)
  definition: |
    经理/助理是经键对声明的逻辑角色（非独立对象）：经理侧建 Assistant Call 键、助理侧自动生成 Manager Call
    键；Routing Assistant 为顶班角色（每经理一名）。
  alias_or_related: g15；multitool Boss/Secretary 术语沿用旧称 boss/secretary
  tags: [role, manager-assistant]

# ── 三、许可/计费 (subscription) ──

- id: g36
  term: Lock 332 (PCS max. number)
  category: subscription
  source_pages: p167, p188
  source_quote: |
    "Lock 332 is greater than 0 in the license file in the Communication Server" (p167)
    "332 M PCS max. number = 0/ 3" (p188)
  definition: |
    PCS 许可锁：决定系统可声明的 PCS 台数（实验文件上限 3，当前已用 0）。spadmin → 2 Display active file
    查看核验。
  alias_or_related: g08 的商务前提
  tags: [subscription, licensing, pcs]

- id: g37
  term: E-CS redundancy (Lock 186) 与软件锁表（184/185/187/188/329/330）
  category: subscription
  source_pages: p94, p188
  source_quote: |
    "184 Integrated Gatekeeper = 99999 • 185 SIP Gateway = 2 • 186 E-CS redundancy = 1 • 187 H323 (G711)
    network link = 20 • 188 SIP network links = 20" (p94)
    "329 M IP-Softphone Agents = 0/ 20 • 330 M Advanced Mobile IP-Touch Users = 0/ 10" (p188)
  definition: |
    本书出现过的软件锁：186 E-CS redundancy=冗余（部署前必须 ≥1）；184 Integrated Gatekeeper、185 SIP
    Gateway、187 H323(G711) network link、188 SIP network links 为话务相关锁；329 IP-Softphone Agents、330
    Advanced Mobile IP-Touch Users 为软终端锁（格式 已用/上限）。
  alias_or_related: spadmin 工具；FlexLM 服务器（g45）供许可
  tags: [subscription, licensing]

- id: g38
  term: ABC-F / ABC-F2
  category: subscription
  source_pages: p44, p81, p384, p387
  source_quote: |
    "'ABC-F2' proprietary protocol stands for 'Alcatel-Lucent Business Communication – Features 2'" (p384)
  definition: |
    ALE 私有组网协议族：ABC-F 提供组网特性透明（g44 网络化架构的核心），ABC-F2 为其新一代（直链承载）；
    书中并列出现 ABC-F IP trunk（子网间中继组）与 ABC-F TDM 链路（直链迁移前须清光）。按六类口径归入协议/
    商务命名，此处集中收录。
  alias_or_related: g21 Direct IP Link、g44 Networked architecture
  tags: [subscription, protocol, abc-f]

- id: g39
  term: FlexLM
  category: subscription
  source_pages: p10, p15, p30, p49, p188
  source_quote: |
    "FlexLM SERVER ENTP_FLEXLM Flex 192.168.1.80 ... root letacla1" (p10, 实验口径)
    "FlexLM Server (192.168.1.80) is declared" (p49)
  definition: |
    浮动许可服务：OXE 预配置声明其地址（实验 192.168.1.80，root/letacla1）；spadmin 有专菜单 Check
    connection with FlexLM（选项 10）。软件锁/CAPEX 模式的许可来源。
  alias_or_related: g37 锁表；PANIC flag=0（spadmin CAPEX 输出）
  tags: [subscription, licensing, flexlm]

# ── 四、产品/组件 (product) ──

- id: g40
  term: OmniPCX Enterprise (OXE)
  category: product
  source_pages: p1, p43-44, 全书
  source_quote: |
    "OMNIPCX ENTERPRISE - R101.1 MD4 • ADVANCED - EDITION 13" (p1)
  definition: |
    本书主角：ALE 企业级通信服务器（本书版本 R101.1 MD4）；两种系统形态（集中式 15000 分机/组网 100000 分
    机）；承载平台三类（Common Hardware CS 板卡、GAS、虚拟机）。组网章节另用 "OXE Purple R100.0" 指代版本
    世系。
  alias_or_related: CS（call server）= 其呼叫服务器角色
  tags: [product, pbx]

- id: g41
  term: OMS (OXE Media Service)
  full_name: OXE Media Service（书中展开）
  category: product
  source_pages: p147, p166, p200-201, p213
  source_quote: |
    "An OMS is required in order to provide media services (e.g., transcoding, conferencing) with OPUS or
    G.722 codecs" (p147)
    "OMS virtual machine ... Welcome to Rocky Linux OMS ... sudo omsconfig" (p135)
  definition: |
    OXE 媒体服务（虚拟机形态，Rocky Linux；omsconfig 工具）：提供 OPUS/G722 转码与会议等媒体资源；冗余章
    作为参考 MG 声明对象、PCS 章作为被救对象（配置 Passive CS address/FQDN 后重启）；每台需指向 CS 主角色
    地址（CPU role address）。
  alias_or_related: 虚拟 GD4 承载（Rack 4/6）；实验值 192.168.1.13 / 192.168.2.13 / 192.168.1.113
  tags: [product, media, oms]

- id: g42
  term: GD4 / mgconfig
  category: product
  source_pages: p49-50, p110-111, p134, p171, p200
  source_quote: |
    "Virtual GD4 (slot 0) IP @: 192.168.1.13/24 ... MAC @: 00:50:56:01:01:13" (p49)
    "[admin@mg4 ~]# sudo mgconfig ... Welcome to the GD configuration tool" (p110)
  definition: |
    GD 媒体网关板卡（GD4；硬件版装在 Rack 2 配 MIX484，虚拟版随 OMS）：mgconfig 工具管理 IP/角色地址/下
    载协议/SSH/证书等；冗余章填 CPU role address（及空间冗余的 redundancy role address）；PCS 救援时软复
    位并用救援 IP 改连 PCS。
  alias_or_related: GDx/GAx/INTIPx 板卡族（IP 域/监督/4645 转换语境）；登录 admin（root/letacla1，实验口径）
  tags: [product, gateway, gd4]

- id: g43
  term: INTIP（virtual INTIP A）
  category: product
  source_pages: p87, p147, p213
  source_quote: |
    "All IP equipment's, belonging to an 'IP Domain' type, exchange the signaling with the virtual INTIP A
    board provided by the CS • The virtual board is in the virtual shelf 19 in position 1" (p147)
  definition: |
    IP 信令板（含 CS 提供的虚拟 INTIP A，虚拟机架 19 位 1）：域内设备与其交换信令；DSU 未登录时 ippstat 显
    示其虚拟 INTIP 为 255/255，登录后为 19/1。GD/GA/INTIP 板族在冗余场景要填 CS 主角色地址。
  alias_or_related: 域信令枢纽；compvisu 输出中的 cr-cpl-term 19-0-x
  tags: [product, board, intip]

- id: g44
  term: MIX484 / ALE-500 / ALE-300 / ALE-20H / ALE-30H
  category: product
  source_pages: p23, p50, p52, p379-380
  source_quote: |
    "MIX484 (slot1)" (p50)
    "31010 Charles Cooper ALE-500 (IP NOE) Main Dynamic IP @ • 31020 David Douglas ALE-30H (TDM/UA) Main" (p52)
  definition: |
    Hybrid Mode 教室硬件与话机族：MIX484 为板卡（Rack 2 slot1）；ALE-500/ALE-300/ALE-20H 为 IP NOE 话机
    （动态地址在 DHCP 段 .14x）、ALE-30H 为 TDM/UA 话机。虚拟化环境以 IPDSP 31000-31003 替代。
  alias_or_related: NOE 话机族（3GEE/ALEx00 出现在 domstat Type 列）
  tags: [product, handset, classroom]

- id: g45
  term: IPDSP (IP Desktop SoftPhone)
  full_name: IP Desktop SoftPhone（书中展开）
  category: product
  source_pages: p10, p51-52, p329, p379
  source_quote: |
    "IP DSP '31000' Brad Barkley ... Installed on PC Client 10 ... Don't forget to specify the TFTP server
    IP @ in IPDSP settings" (p51)
  definition: |
    ALE 软话机（实验主力终端）：31000-31003 装在四台 PC Client；Settings→Network 填 TFTP Server Main（CS
    主地址）；办公桌共享/多设备场景作为 DSS 需开 IP-Softphone emulation；即时登录特性不适用。
  alias_or_related: MicroSIP（模拟公网号的第三方软话机，p11/p16/p26/p31）
  tags: [product, softphone, ipdsp]

- id: g46
  term: RLAB / POD
  category: product
  source_pages: p5-32, p212, p375
  source_quote: |
    "Remote Lab allows accessing a pool of virtual and physical machines (depending on the course) hosted
    in a data center. ... Pods are independent of each other • Pods have the same configuration • Pods
    have access to common resources" (p5)
  definition: |
    ALE 培训远程实验室：按 POD 划分同构实验单元，Pod 间独立、共享公共资源（NAS/SIP 模拟器/邮件服务器/外部
    DNS）；Rlab 门户提供 VM 开关、console、网卡管理（Remove/Create Interface）、子网断链（Disconnect/
    Connect）等操作。全书实验的承载底座。
  alias_or_related: 两种 Pod 拓扑（集中式/组网）+ Hybrid Mode 变体；SIP 模拟器见 g55 ITSP1
  tags: [product, lab, rlab]

- id: g47
  term: REX (Remote Extension)
  full_name: Remote Extension（书中以 * 注展开）
  category: product
  source_pages: p354, p359-361
  source_quote: |
    "Secondary set types ... Remote extension* (REX) ... • Only one Remote Extension per multi devices user" (p354)
    "Remote extension Deactivation Prefix ... Remote extension Activation Prefix" (p360)
  definition: |
    远端扩展（多设备副站类型之一，每多设备限 1 个）：振铃可经激活/停用前缀（书内示例 651）控制；Ring
    Secondary REX in Parallel 参数控制主为 IPDSP 时 REX 是否同响。
  alias_or_related: g19 副站族
  tags: [product, rex, multi-device]

- id: g48
  term: MIPT
  category: product
  source_pages: p354, p363, p369
  source_quote: |
    "Secondary set types NOE IP, NOE TDM, DECT*, MIPT, IPDSP, SIP (SEPLOS), Remote extension* (REX)" (p354)
  definition: |
    多设备副站类型之一（书中仅在类型清单出现，未给全称与部署细节）。
  alias_or_related: g19 副站族
  tags: [product, mipt]

- id: g49
  term: 4645（Voice Mail）
  category: product
  source_pages: p62, p151, p181, p183
  source_quote: |
    "4645 Voice Mail supports only G711 algorithm" (p151)
    "Terminals of an IP domain rescued by a PCS can not reach the 4645 Voice Mail" (p183)
  definition: |
    语音邮箱服务器：仅 G711；跨域访问需同域板卡转码（两个压缩机）；PCS 被救域不可达；oxe-nw-sshkey-sync 的
    CSV 模板含 4645 条目（密钥同步对象）；audit 对象表含 4645 VM VPIM。
  alias_or_related: g07/g08 的边界案例
  tags: [product, voice-mail, 4645]

- id: g50
  term: OmniVista 8770
  category: product
  source_pages: p87, p181, p473, p489
  source_quote: |
    "with the OmniVista 8770 it is possible to retrieve those tickets: Automatically at the daily
    synchronization • Or manually" (p181)
    "From OXE WBM interface • Or 'mgr', or '8770'" (p473)
  definition: |
    网管/管理平台：PCS 激活期话单的取回通道；broadcast 激活的管理界面之一；8770 应用可为节点指定两个主地
    址（spatial 冗余）。本书仅以引用出现，操作细节在书外。
  alias_or_related: WBM/mgr 为 OXE 侧配置界面（本书主用）
  tags: [product, management, omnivista]

- id: g51
  term: WBM / mgr
  category: product
  source_pages: p155, p197, p401, p473, p489
  source_quote: |
    "Open the OXE WBM interface IP\\IP Domain" (p155)
    "Broadcast process must be enabled manually • From OXE WBM interface • Or 'mgr', or '8770'" (p473)
  definition: |
    OXE 的 Web 图形配置界面（书中未展开全称）：本书全部 WBM 配置路径的入口（IP\IP Domain、\Passive Com.
    Server\、Inter-Nodes Links、Translator、System\Broadcast 等）；mgr 为等价的旧版图形工具。
  alias_or_related: 与命令行（g30/g31/g32）互补
  tags: [product, wbm, management]

# ── 五、协议与技术 (protocol) ──

- id: g52
  term: SSHv2 / 公钥认证
  category: protocol
  source_pages: p49, p55-68, p378
  source_quote: |
    "SSHv2 is enabled (mandatory since release N3)" (p49)
    "SSH passwordless login is an SSH authentication method that employs a pair of public and private
    keys for asymmetric encryption." (p59)
  definition: |
    全书协同机制的安全底座：N3 起默认启用 SSHv2+公钥认证；三账户密钥对与 authorized_keys 路径见 p04 路径
    表；mastercopy/pcscopy/audit/broadcast 均依赖。
  alias_or_related: SSH 缩写书中未展开；known_hosts 清理由同步工具代管
  tags: [protocol, ssh, security]

- id: g53
  term: SCP / SFTP
  category: protocol
  source_pages: p71, p179, p437
  source_quote: |
    "Updates must be done with a 'secured copy protocol' (scp)" (p71)
    "During the transfer, data are converted in ASCII files, compressed and transferred in 'sftp'" (p437)
  definition: |
    安全复制通道：冗余库实时复制用 scp（mastercopy/pcscopy 同族）；audit 数据传输把对象表转 ASCII 压缩后走
    sftp（客户端/服务器模型，参考节点为 server）。
  alias_or_related: scp 全称书中已给；sftp 未展开
  tags: [protocol, transfer]

- id: g54
  term: IPSec / DTLS / SIP TLS / SRTP
  category: protocol
  source_pages: p393-394
  source_quote: |
    "Signaling between network nodes (ABC-F signaling, audit, broadcast) encrypted using 'IPSec' ... Media
    encryption (SRTP) between two networked DTLS/ SIP TLS capable devices • SRTP keys generated by each CS
    ... and sent over the encrypted ABC-IP logical link" (p393)
  definition: |
    直链原生加密栈：节点间信令（含 audit/broadcast 流量）走 IPSec（证书认证，CS 内 IPSec Manager 建链）；
    终端到终端媒体走 DTLS/SIP TLS + SRTP（密钥由各 CS 生成并经加密链路下发）；允许加密/非加密直链混布（两
    端能力+链路加密位一致才建加密链）。
  alias_or_related: trkvisu/hybvisu 的 Encryption 字段；IP Premium Security 不适用直链（p397）
  tags: [protocol, encryption]

- id: g55
  term: RTP (Direct RTP)
  category: protocol
  source_pages: p43-44, p385, p387, p416
  source_quote: |
    "Direct RTP between IP phones and distributed media gateways to minimize delay (no transit in the
    network)" (p43)
    "RTP information (voice flow) is relayed inside the ABC-F link signaling ... All these data (Voice+
    Signaling) are sent through IP" (p385)
  definition: |
    语音媒体流：架构卖点之一是 Direct RTP（话机/网关间直达不经转发）；直链把 RTP 装进 ABC-F 信令内传输；
    represent/cnx 命令可看 RTP 路径与端口（实验输出 network direct RTP to @IP ... port 32514）。
  alias_or_related: RTCP/CNG/VAD 等出现在 compvisu sys 输出；缩写未展开
  tags: [protocol, rtp, media]

- id: g56
  term: SIP / H.323
  category: protocol
  source_pages: p94, p175-178, p384, p396, p402
  source_quote: |
    "No need anymore of H323 channels" (p384)
    "H323 no more used" (p396)
  definition: |
    两组话音协议：SIP——外部网关/中继与 SIP 扩展（PCS 双 proxy、SIP FQDN、compvisu 输出 G_OPUS_SWB 等编
    码名）；H.323——老一代网络信令，直链启用后不再使用（compvisu sys 输出 Inter-node protocol H323 字段
    保留兼容显示）。
  alias_or_related: SIP trunk（ITSP1 实验）、SIP external gateway
  tags: [protocol, sip, h323]

- id: g57
  term: DDI
  category: protocol
  source_pages: p54, p224, p230-231, p37
  source_quote: |
    "First external number 33210N41000 ... First internal number 31000 ... Range Size 500" (p54)
    "DDI table - First external nb 41000 ... DDI table – First internal nb 31000" (p37)
  definition: |
    直拨外线翻译：把外线号段映射到内部号段（Default DID num. translator 与 Node DID Translation 两级）；
    实验口径 Node1 外号 41000-41499 ↔ 内号 31000-31499、Node2 41500-41999 ↔ 31500-31999；thin sector 是
    其反向机制。缩写书中未展开。
  alias_or_related: g10 thin sector、g25 Node Access Prefix
  tags: [protocol, numbering, ddi]

- id: g58
  term: ARS
  category: protocol
  source_pages: p222, p229, p505, p520-521, p526-529
  source_quote: |
    "the Call Server picks up the ARS prefix which allows to seize a trunk group" (p222)
    "Use of ARS is mandatory to force calls rerouting from public to private network" (p519)
  definition: |
    自动路由选择（缩写未展开）：溢出与重路由的路由引擎——Node Access Prefix 的 Number to add 通常填 ARS 前
    缀；公到私重路由经 Real Discriminator→ARS Route List→Route（TG/去加位/类型）→Time-based Route List。
    基础管理属 Starter 内容。
  alias_or_related: 审计/广播明确不覆盖 ARS 表（本地对象）
  tags: [protocol, routing, ars]

- id: g59
  term: TFTP / DHCP
  category: protocol
  source_pages: p51, p90, p128, p172, p183
  source_quote: |
    "TFTP #1 Enter the call server main IP adress ... TFTP #2 Enter the second call server main IP adress
    when the spacial redudancy is up" (p112)
    "sets receive the 'TFTP Backup IP@' information from the CS ... it corresponds to the PCS IP@ specified
    in the IP domain of the sets" (p172)
  definition: |
    终端引导与地址协议：TFTP 承载话机 binaries/配置（lanpbx.cfg）下载，冗余/空间冗余场景设备可填两个 TFTP
    地址；DHCP 由 OXE 或外部服务器分配，spatial 下活动 CS 应答并填自己主地址（外部 DHCP 须能发两个 tftp 地
    址）；PCS 不提供 TFTP/DHCP 服务。缩写均未展开。
  alias_or_related: g08 TFTP Backup IP@、g05 spatial 适配
  tags: [protocol, tftp, dhcp]

- id: g60
  term: T2 / T38 / DTMF (RFC 2833)
  category: protocol
  source_pages: p278, p387
  source_quote: |
    "One T2 number (specific ISDN number) or several" (p278)
    "T38 • DTMF (ABC-F sig. or RFC 2833)" (p387)
  definition: |
    直链业务能力清单中的三项：T2=特定 ISDN 号（过滤表可引用的来话类型）；T38=传真中继（直链支持）；DTMF 可
    走 ABC-F 信令或 RFC 2833。书中仅列名，未展开配置。
  alias_or_related: 直链 services 清单（p387）
  tags: [protocol, isdn, fax]

# ── 六、网站/文件/资源 (resource) ──

- id: g61
  term: /usr2/mtcl/.ssh 与密钥路径族
  category: resource
  source_pages: p67, p100, p207
  source_quote: |
    "Check the content of the 'authorized_keys' file, located in '/usr2/mtcl/.ssh' directory, on CSA &
    CSB." (p100)
  definition: |
    SSH 密钥资源路径族：mtcl——/usr2/mtcl/.ssh/{authorized_keys,id_rsa,id_rsa.pub}；swinst——/usr2/soft_install/
    bin/.ssh/；root——/root/.ssh/。核验同步结果的标准动作是 more authorized_keys 数公钥条数（两机 6 条、
    三机 9 条）。
  alias_or_related: p04 路径表
  tags: [resource, ssh, path]

- id: g62
  term: /usr4/mao（cm_cb.sav / LOG / RLOG / lupd.dat）
  category: resource
  source_pages: p474-478, p492-496
  source_quote: |
    "(101)cs1> cd /usr4/mao • (101)cs1> ll cm_cb.sav ... -rw-rw-rw-. 1 mtcl tel 911 Dec 16 14:15 cm_cb.sav" (p474)
    "The 'lupd.dat' file contains the indexes of the modifications of every nodes in the network" (p477)
  definition: |
    广播文件资源目录：buffer 文件（cm_cb.sav / area_cm_cb.sav）、广播日志（LOG.N.S / A.Z.N.S）、错误日志
    （RLOG）、序号索引（lupd.dat，mao -lupd 查看）。观察广播健康的第一现场。
  alias_or_related: g23/g28；prog_diff/maohist 是其读取工具
  tags: [resource, broadcast, path]

- id: g63
  term: /tmpd（Firewall_Rules_multi.txt / ssh_multi.csv / oxenwsynclogs.zip）
  category: resource
  source_pages: p94, p191, p203, p206
  source_quote: |
    "importing the 'Firewall_Rules_multi.txt' file, already available in 'tmpd' directory" (p94)
    "A '.csv' file, named 'ssh_multi.csv' has been prepared for this training and is available in '/tmpd'
    directory" (p203)
    "Log files Archival Done Successfully in the file /tmpd/oxenwsynclogs.zip" (p206)
  definition: |
    实验文件资源目录：防火墙 bulk 导入文件（TRUSTED_HOST/TRUSTED_RANGE 逗号格式，无表头）、SSH 全网同步
    csv（运行结束自动删除）、同步日志归档 zip（root 解压到 tmpd/logs 查 oxenwsync.log）。
  alias_or_related: 教学专用文件名，生产按现场替换
  tags: [resource, lab, files]

- id: g64
  term: TG0028
  category: resource
  source_pages: p200
  source_quote: |
    "To know all the commands available once connected to an IP set, please refer to the troubleshooting
    guide, named 'TG0028', present on 'My Portal' web site" (p200)
  definition: |
    话机排障指南文档（MyPortal 下载）：IP 话机命令（tnet/ipconfig/ipconfig survi 等）的权威清单来源。书中
    唯一一次引用。
  alias_or_related: MyPortal（g65）
  tags: [resource, document, troubleshooting]

- id: g65
  term: My Portal / ALE Knowledge Hub
  category: resource
  source_pages: p200, p539, p543
  source_quote: |
    "LOGIN TO ALE KNOWLEDGE HUB • Connect to ALE Knowledge Hub (https://enterprise-education.csod.com)
    with your usual credentials" (p539)
    "Find a Course • Browse our catalog available on https://enterprise-education.csod.com/" (p543)
  definition: |
    两个门户：My Portal——技术文档/TG 排障指南下载站（书中引用 TG0028）；ALE Knowledge Hub
    （enterprise-education.csod.com）——培训目录与课后评估/证书入口。培训收尾章（p537-543）的评估流程挂
    在后者。
  alias_or_related: 培训反馈邮箱 training-services@al-enterprise.com（p543）
  tags: [resource, portal, training]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列候选术语逐条核对

OVERVIEW 术语表实为 **22 行**，逐条核对如下：

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| CS Duplication / Mastercopy | 有明确定义（p70-71/p79） | g01 / g02 |
| Reference Media Gateway | 有明确定义（p74） | g03 |
| Double Main Mode | 有明确定义（p76-77/p82） | g04 |
| Spatial Redundancy | 有明确定义（p82/p85） | g05 |
| IP Domain / Domain 0 | 有明确定义（p143/p152） | g06 |
| CAC (Domain Max Voice Connection) | 有明确定义（p144） | g07 |
| PCS | 有明确定义（p166） | g08 |
| Survivability / TFTP Backup IP@ | 有明确定义（p172） | g08 + g59 |
| Global PCS address 255.255.255.255 | 有明确定义（p178/p202） | 并入 g08/g18 相关联的 n18（counter-example）；glossary 收于 g08 定义内 |
| Local Private to Public Overflow | 有明确定义（p218） | g09 |
| Thin Sector | 有明确定义（p224） | g10 |
| Speed Dialing | 有明确定义（p236-244） | g11 |
| Multiline | 有明确定义（p257） | g12 |
| Supervision key | 有明确定义（p262） | g13 |
| Screening/Unscreening | 有明确定义（p277） | g14 |
| Hunting group | 有明确定义（p299-305） | g16 |
| Desk Sharing DSS/DSU | 有明确定义（p329-330） | g18 |
| Multi Device / Twinset | 有明确定义（p353） | g19 |
| Direct IP Link | 有明确定义（p384） | g21 |
| Audit | 有明确定义（p426） | g22 |
| Broadcast | 有明确定义（p471） | g23 |
| SSH key tools | 有明确定义（p57-64） | g52 + g61（oxe-ssh-auth/oxe-nw-sshkey-sync 为工具名，收录于 framework f05 与 principle p02/p03） |

结论：**22 行全部"本书正文有明确定义"，无"仅 passing 提及需排除"项，无"书中实际未出现"项。**

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：Network/Routing Number（g24）、Node Access Prefix（g25）、Reference Node（g26）、pcscopy（g27）、Broadcast Area（g28）、组网双向溢出（g29）、Rapid Call Shift（g20）、Call Pick-up（g17）
- 角色：mtcl/swinst/root（g30-g32）、Real/Pseudo Main（g33）、DSS/DSU 角色化（g34）、Manager/Assistant 键角色（g35）
- 许可：Lock 332/186 及锁表（g36/g37）、ABC-F/ABC-F2（g38）、FlexLM（g39）
- 产品：OXE（g40）、OMS（g41）、GD4/mgconfig（g42）、INTIP（g43）、MIX484/ALE 话机族（g44）、IPDSP（g45）、RLAB/POD（g46）、REX（g47）、MIPT（g48）、4645（g49）、OmniVista 8770（g50）、WBM/mgr（g51）
- 协议：SSHv2（g52）、SCP/SFTP（g53）、IPSec/DTLS/SIP TLS/SRTP（g54）、RTP（g55）、SIP/H.323（g56）、DDI（g57）、ARS（g58）、TFTP/DHCP（g59）、T2/T38/DTMF（g60）
- 资源：/usr2/mtcl/.ssh 路径族（g61）、/usr4/mao 文件族（g62）、/tmpd 文件族（g63）、TG0028（g64）、My Portal/Knowledge Hub（g65）

### 3. 仅 passing 提及、未单列条目的词（备查）

CSTA（本书未出现）、VLAN 802.1q（p129 命令输出 "No frame will be 802.1q-tagged"，netadmin VLAN 菜单 p6689 行）、QSIG/ISDN（p519 "private links (SIP, ISDN, QSIG, etc.)"）、A-GAP DECT / WLAN handsets（p166 PCS 可救清单）、SEPLOS（p354 SIP 话机类型注记，未展开）、AOM（p336 即时登录排除条件，未展开）、VPIM（audit 对象表 "4645 VM VPIM"）、NPD（Numbering_Plan_Descriptor，audit 对象表）、Robinet/RSI/X25/PSPDN（audit 对象表遗留项，未展开）、Keep RTP flow（p171/p174 话机救援选项）、lanpbx.cfg（p112 话机下载文件）、ITSP1/ITSP2 与 MicroSIP（实验基础设施，已在 g46 附注；号码规则收录于 framework f03）、NTP/FlexLM Server/IT Server（实验拓扑组件，IP 与账号见 f02；FlexLM 已单列 g39）、Superuser2580*/letacla1 等实验口令（实验口径，BOOK_OVERVIEW 批判节已声明不入册为可执行知识）。

### 4. 提取口径说明

- 所有定义只采信本书正文；DDI/TFTP/WBM/MIPT/SIP/RTP/DTLS/IPSec/SFTP/FQDN/ARS/VLAN/T2/T38 等书中未给全称的缩写，full_name 一律省略；C.A.C/PCS/ABC-F2/DSS/DSU/REX/SCP/OMS/IPDSP/FlexLM 等书中已展开的照录原文拼写。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准；引用均为原文摘录，原文笔误（如 p54 "spacial redudancy"、p112 "adress"）照录并保留原样。
- 概念 g29 将两个对称特性并为一条（同一机制的正反面）；g38 ABC-F 族按任务书六类口径归入 subscription 类（协议/商务命名），正文交叉引用已注明。
