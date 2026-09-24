# 框架/流程/结构候选 — OmniTouch Contact Center Standard (OTCCXTE100EN Ed09)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、CCD 矩阵模型、端到端流程、OXE Web Admin 与 CCS 双控制台菜单路径、组件关系图示。实验环境给定值（IP/密码/账号/分机号/号码段）一律标注"实验口径"。页码一律按 source_fulltext.txt 的 ===== PAGE N ===== PDF 页标记。

```yaml
- id: f01
  title: 全书课程推进逻辑——环境 → CCD 模型 → 基础矩阵 → CCS 工具 → 规则与人员 → 调优与增值域
  type: flow
  source_pages: p3-649
  source_chapter: 全书章节推进（RLAB → CCD Application Overview → 20 个 How-To → 评估）
  source_quote: |
    "The OTCC Standard Edition is a complete solution built into the OmniPCX Enterprise" (p23)
    "OmniTouch Contact Center Standard Edition is a solution that provides all the call
    distribution advanced features and capabilities … CCD Software integrated into OXE
    Call Server • Additional options (CCS, CCA, ACR, Soft Panel)" (p21)
  summary: |
    课程按五段推进：①实验环境（RLAB 平台 + 公网 SIP 运营商模拟器，p3-17）；②CCD 应用概览讲义
    （呼叫流、CCD 矩阵、座席/班长、路由规则、分配规则、座席选择，p18-62）；③基础交付闭环 How-To
    （建矩阵 → 装 CCS → 建规则 → 建座席/班长 → 收尾 POD → ABC-F 链路，p63-165）；④调优与能力域
    How-To（对象参数调优、语音指南三种管理法、座席班长特性、EWT/排队位置、实时监控、直接呼叫、
    Excel 统计、紧急关闭、统计 pilot、欢迎指南、多语言、日历，p166-642）；⑤培训评估收尾（p643-649）。
    讲义与实验交替出现：每个功能域先讲义后 How-To。这是"先把最小呼叫中心跑通，再逐域加能力"的教学主线。
  conditions: 全书基于 R10.16（Starter Edition 09）；大量能力依赖 OXE 侧预置数据库（法国目标库）
  tags: [flow, course-structure, master-plan]

- id: f02
  title: RLAB 远程实验平台结构——POD 池 + 公共资源区
  type: structure
  source_pages: p3-13
  source_chapter: REMOTE LABS PLATFORM / Introduction, POD Configuration, Training Platform, Instances
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted
    in a data center." (p5)
    "External Gateway 10.20.30.254 / Internal Gateway 192.168.1.254 / Subnet 192.168.1.x …
    Internal DNS 192.168.1.250 … SIP simulator / NAS: softs, licenses … External DNS 10.20.30.250" (p7)
  summary: |
    POD 1..n 相互独立、配置相同；公共 Pod 提供 NAS（软件、许可）与 SIP 模拟器（12.0.0.2）及外部 DNS
    （10.20.30.250，实验口径）。每个 POD 含五台实例（p9 实例表，实验口径）：OXE（OTCC_OXE，cs1 物理/
    cs1m 主 CPU，192.168.1.1 / 192.168.1.3，账号 mtcl/swinst/root，密码 Superuser2580*）；OMS
    （OTCC_OMS，192.168.1.13，root）；FlexLM 服务器（OTCC_FLEXLM，192.168.1.80，root/letacla1）；
    Client PC 10（192.168.1.10，IPDSP 31000）；Client PC 11（192.168.1.11，IPDSP 31001）。
    客户端软件：PC10 装 3 个 MicroSIP（31010、31011 内呼 + Public 公呼）和 1 个 IPDSP（31000 座席终端），
    PC11 装 1 个 IPDSP（31001）；NAS 网络盘从资源管理器可达。访问方式两种（p12）：Console mode
    （管理 PCX/Windows 实例，音频被禁用）与基于 Guacamole 的 Remote Desktop Connection
    （实验必用，共享软电话音频资源）。
  conditions: 仅培训环境；所有 IP/密码为实验口径；FlexLM 为 OXE 许可服务器
  tags: [structure, lab, rlab, topology]

- id: f03
  title: ITSP1 公网 SIP 运营商模拟器拓扑与号码变换规则
  type: diagram
  source_pages: p14-17
  source_chapter: PUBLIC SIP CARRIER SIMULATOR / SIP Carrier Overview & External calls
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 … ITSP1 Public gateway public.itsp1.com
    10.20.30.50 … SIP domain: sip.itsp1.fr / itsp1.fr" (p15)
    "PBX installation nb 3321PN … DDI table - First external nb 41000 … DDI table – First internal
    nb 31000 … Example: 31002's external nb 3321PN41002 … Dialed number: 0210341002 or 33210341002
    … Number sent by the PBX: +33210341002" (p16)
  summary: |
    模拟器两条腿：SIP 网关 gateway1.itsp1.com（PBX 注册账号 pbxP/alcatel，P=POD 号，SIP 域
    sip.itsp1.fr）与公网网关 public.itsp1.com（SIP 域 itsp1.fr，模拟公网用户）。号码规则（PN=两位
    POD 号）：安装号 3321PN（POD3=332103）；DDI 首外线 41000、首内线 31000；分机 31002 外线号
    3321PN41002。外呼环路：拨 0210341002 或 33210341002，PBX 送出 +33210341002，经 ITSP1 环回
    振铃 31001/31002。实验中打 Pilot 的标准拨号串为 0210X41600/0210X41601（X=POD 号 1-6）。
  conditions: 实验口径（RLAB 专用基础设施）；号码规则与生产 ITSP 无关
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f04
  title: CCD 矩阵总模型——Pilot → Call Routing → Waiting Queue → Call Distribution → Processing Group
  type: diagram
  source_pages: p22-29, p40
  source_chapter: CCD APPLICATION OVERVIEW / Call Flows, CCD Matrix Description
  source_quote: |
    "The Call Distribution is based on a matrix: Pilots … Call routing … Queue normal … Int. Overflow
    … Redirection … Processing groups (Resources) … Call Distribution" (p23-24)
    "Queues Resources (PG) Called departments (pilots) … Call Distribution: Resource availability,
    Priorities, Longest idle time (load) … Call Routing: Priorities, Expected waiting times" (p24)
  summary: |
    呼叫流五级：来话先落在 Pilot（被叫部门），经 Call Routing（按 pilot 状态选方向：Normal/Intelligent
    Overflow/Redirection）进入 Waiting Queue 排队，再经 Call Distribution（按资源可用性、优先级、最长
    空闲时间）分发到 Processing Group（资源），最后在 PG 内做 Agent Selection 选座席。路由维度看
    "优先级 + 预期等待时间"，分配维度看"资源可用性 + 优先级 + 最长空闲"。这是全书一切配置的骨架图。
  conditions: 无版本前提；CCD 软件集成在 OXE Call Server 内（p21）
  tags: [diagram, ccd-matrix, architecture, master-model]

- id: f05
  title: Pilot 三态机——Open / General Forwarding / Blocked 与触发来源
  type: structure
  source_pages: p26
  source_chapter: CCD APPLICATION OVERVIEW / Possible states of a pilot
  source_quote: |
    "The pilot can be in open state • Calls are connected to a welcome guide and then are routed
    with or without queuing • The pilot can be in general forwarding state • Pilot closed automatically
    by calendar, Pilot closed manually by a supervisor action, switch on General Forwarding by agent
    action on his phone set … The pilot can be in blocked state • Case: Accidental closure • Cause:
    Resources missing in the downstream processing group" (p26)
  summary: |
    Pilot 三态：①Open——来话接欢迎指南后进队列或直达；②General Forwarding（通用转发/人工关闭）——
    触发来源三个：日历自动、班长手动、座席话机按键；来话接专用指南或转指定号码/新规则；③Blocked
    （意外关闭）——下游 PG 无资源（全部座席登出或不可用）时自动进入，来话接不可用指南。三态各有
    独立语音指南集，路由规则可按状态分别配置方向。这是理解 pilot rule 的 Normal/FWD/Blocked 三张
    表的依据（后续 CCS 操作中三张表反复出现）。
  conditions: Blocked 为自动态，General Forwarding 为管理动作态
  tags: [structure, pilot, state-machine, routing]

- id: f06
  title: 等待队列三类型与四状态——Normal / Intelligent Overflow / Redirection
  type: structure
  source_pages: p27-28, p40
  source_chapter: CCD APPLICATION OVERVIEW / Queue characteristics & states
  source_quote: |
    "A Queue can: be shared among several Pilots (30 max) • serve several Processing Groups (50 max)
    • Queued calls are served FIFO (First In/First Out) • Different types of waiting queue are available:
    Normal … Intelligent overflow … Redirection" (p27)
    "Possible states of the queue • Open (Not saturated) • Saturated • Expected Waiting Time (EWT) >
    Maximum Waiting Time • Closed by CCs user • Blocked • Downstream resources are not guaranteed
    (All agents are logged-off or in unavailable state)" (p28)
  summary: |
    队列规格：一个队列最多被 30 个 pilot 共享、服务 50 个 PG，FIFO 服务。三类型：Normal（pilot 来话
    的停车常，再分配给处理组）、Intelligent Overflow（经公网/专网智能溢出到远端 OTCC 或本地改址重定向）、
    Redirection（其它方向不可用时的兜底重定向，可接语音指南/IVR 类 PG，如"线路全忙请稍后再拨"）。
    四状态：Open、Saturated（EWT>最大等待时间）、Closed（CCS 用户手动关）、Blocked（下游资源无保证）。
    队列与 PG 类型的兼容关系有专表（p40）：Voice Guide PG 只能接 Redirection 队列。
  conditions: 兼容表原文为图形矩阵，本条按图转述；数值 30/50 为硬上限
  tags: [structure, queue, types, states, fifo]

- id: f07
  title: Processing Group 五类型与队列-PG 兼容矩阵
  type: structure
  source_pages: p29, p40
  source_chapter: CCD APPLICATION OVERVIEW / Different types of processing groups & Queue/PG compatibility
  source_quote: |
    "Agent processing group • Made up of agent or supervisor sets … Forward processing group
    (on-pcx number) • Attendant set or group, voice mail … Voice guide processing group • Voice guide
    broadcast (duration, V.G #) • Rerouting processing group • Rerouting to the ABC-F or public network
    • I.V.R processing group • Connection to the CCivr application" (p29)
  summary: |
    PG 五类型：Agent（座席/班长话机组成，唯一承载 ACD 分发的类型）、Forward（本机号码前转：话务台、
    留言、另一 pilot、管理分机、缩位号码）、Voice Guide（播指南，可定时长与指南号）、Rerouting（改道到
    ABC-F 或公网）、IVR（接 CCivr 外部应用）。兼容矩阵（p40）：Normal/Int-Overflow/Redirection 三种
    队列均可接 Agent、IVR、Forward、Rerouting PG；Voice Guide PG 仅可接 Redirection 队列。
    实验基础矩阵的对应关系：Normal_WQ→Agent_PG、Overflow_WQ→Forwarding_PG、
    Redirection_WQ→Voice_guide_PG（p64、p114-115）。
  conditions: 兼容矩阵按原书表格转述；IVR PG 依赖外部 CCivr 服务器
  tags: [structure, processing-group, compatibility, types]

- id: f08
  title: 路由规则结构——每 pilot 最多 30 条规则、方向优先级 0-9、6 级 parking level
  type: structure
  source_pages: p43-50, p103, p110
  source_chapter: CCD APPLICATION OVERVIEW / Call routing rule
  source_quote: |
    "A routing rule is managed to associate each pilot with waiting queues (30 rules max per pilot)" (p43)
    "The routing directions choice, between waiting queues (30max), is done according to priorities or
    according to Expected Waiting Time (in case of same priorities) • Priorities value is from 0 to 9
    • 0 is the highest priority • 9 is the lowest priority" (p44)
    "It is possible to declare a maximum of 30 rules per pilot (1200 rules max)." (p103)
  summary: |
    路由规则把 pilot 与等待队列连起来：每 pilot 最多 30 条规则（系统全局 1200 条上限），可手动或按
    日历切换；方向选择在最多 30 个等待队列间按优先级（0 最高、9 最低）或同优先级时按 EWT。每条
    规则含：方向开/关、优先级、问候指南与 6 个 parking level（每级可放语音指南、地址（IAA 或 IVR in
    Queue）或 EWT 表）。语音指南挂在 pilot 规则上（30 条规则/pilot），按 pilot 状态播放；下游资源
    空出时指南可被打断（cut auth）。
  conditions: 规则上限 30/pilot 与"方向数上限 30"同源；全局 1200 为另一维度上限
  tags: [structure, routing-rule, priority, parking-levels]

- id: f09
  title: 分配规则结构——10 条上限、资源选择与呼叫选择双机制
  type: structure
  source_pages: p51-59, p113-119
  source_chapter: CCD APPLICATION OVERVIEW / Call distribution rule
  source_quote: |
    "A call distribution rule (10 max) defines the distribution of the calls to the processing groups
    • A queue can have up to 50 possible distribution directions" (p54)
    "Resource Selection … The resource selection priority (from 0 to 9) • At equal priority, the longest
    idle time (LIT) of the agents in the processing groups • Call Selection … The Call Selection priority
    (from 0 to 9) • At Equal priority: the real waiting time of the call at the top of the normal queues" (p53)
  summary: |
    分配规则（每系统 10 条上限）决定队列到 PG 的分发：①资源选择（队列挑 PG）——按 PG 优先级 0-9，
    同优先级看 PG 的最长空闲时间 LIT；②呼叫选择（PG 空出时挑呼叫）——按呼叫选择优先级 0-9，同优先级
    看队首呼叫的真实等待时间。另有"最小等待时间阈值"（distribution threshold）：等待超过阈值的呼叫才
    可经该方向分发，且该参数对呼叫选择占优（p59）。分配方向默认全关，须逐条勾选激活（p117 Warning）。
    多 PG 同优先级时的并列规则书中提到 "the rule (PLTR) will be applied"（p117，PLTR 未展开）。
  conditions: 规则默认停用（OXE 侧 Active Rule 激活）；方向默认关闭
  tags: [structure, distribution-rule, resource-selection, call-selection]

- id: f10
  title: 座席状态时序图——free → ringing → conversation → wrap-up → pause 循环
  type: diagram
  source_pages: p280, p275-279
  source_chapter: AGENT AND SUPERVISOR FEATURES / Agent status (CCD call chronology)
  source_quote: |
    "CCD call chronology: Wrap-up in pause (manual) (group timer) … free … ringing (pilot/caller/waiting
    time) … conversation … Wrap-up (automatic) (pilot timer (possible cut-off)) … Pause (pilot timer)
    … code … Wrap-up in idle (manual) (group timer)" (p280)
  summary: |
    座席生命周期：空闲 → 振铃（时长取决于 pilot/呼叫者/排队等待）→ 通话 → 自动 wrap-up（pilot 计时器，
    可被打断）→ pause（pilot 计时器）→ 回空闲；另有两个手动旁支：空闲态手动 wrap-up（组计时器）、
    pause 态手动 wrap-up（组计时器）→ pause；通话结束前还有事务码（code）输入节点。配套规则：
    wrap-up 中做任何操作（除 Queue info 键）即取消 wrap-up（p278）；pause 中可处理个人/本地/外线呼叫
    （p279）；pause 计时器在手动 wrap-up 后完全重置。
  conditions: 计时器归属——自动 wrap-up/pause 挂 pilot，手动 wrap-up 挂 PG（p277-278）
  tags: [diagram, agent-status, wrap-up, pause, lifecycle]

- id: f11
  title: Rainbow CCD 座席三种登录方式图——Office phone / Other phone (REX) / Computer (WebRTC)
  type: diagram
  source_pages: p34-37
  source_chapter: CCD APPLICATION OVERVIEW / CCD agent on Rainbow
  source_quote: |
    "Rainbow user can be used as a CCD Agent (CCD Supervisor not supported) … The Rainbow application
    doesn't require VPN or SBC to support remote worker use case" (p34)
    "Login using office phone … ACD set must not be part of any multiset, • It must not be associated
    to a Rainbow user • DECT sets are not supported as ProACD devices" (p35)
    "Login using computer … REX is configured to route calls to the WebRTC Gateway SIP Trunk" (p37)
  summary: |
    Rainbow 用户可作 CCD 座席（不支持 Rainbow 班长），需专用 Rainbow 账号，唯一分机即 CCD agent
    number；Rainbow 界面出现"Log in"专用动作与基础 CCD 座席 GUI。三种登录：①Office phone——ACD
    话机经 CSTA 被 Rainbow 远程控制（话机须不在任何 multiset 中、未关联 Rainbow 用户、DECT 不支持）；
    ②Other phone——登录到 REX（Remote Extension）池，REX 改址到其它电话号码；③Computer——REX
    改址到 WebRTC 网关 SIP 中继，音频走 WebRTC。远程办公卖点：无需 VPN/SBC。
  conditions: 依赖 Rainbow + WebRTC 网关（仅 computer 方式要音频网关）；CCD Supervisor 不支持 Rainbow
  tags: [diagram, rainbow, ccd-agent, webrtc, remote-worker]

- id: f12
  title: 双控制台分工图——OXE Web Admin 管对象与系统项，CCS 管规则/座席/实时/统计
  type: structure
  source_pages: p63-97, p79, p113
  source_chapter: 全书 How-To 的控制台交替（OXE Web Admin session vs CCsupervision application）
  source_quote: |
    "A CCS station cannot create any object relative to call distribution (trunk groups, pilots, queues,
    processing groups, agents, wall-mounted displays), but can create CCS supervisors and distribution
    rules." (p79)
    "By default, the call distribution rule is deactivated. You must activate the rule from OXE
    management console." (p113)
  summary: |
    两个图形控制台分工：OXE Web Admin（https://192.168.1.3，mtcl 登录）——创建/修改 CCD 底层对象
    （ACD 前缀、PG、队列、Pilot、CCD Users、Statistic Pilot、Distribution Rule 激活、语音指南、COS、
    译码、中继组）；CCsupervision（CCS）——创建/激活路由与分配规则、配置座席属性与挂组、调 pilot/
    队列/PG 参数、实时监控（Navigator）、Excel 统计、紧急关闭。实验中两控制台反复交替，检查动作常
    用"一边配、另一边验"。另有第三入口：OXE 控制台/SSH 命令行（acdsup、vgstat、hybvisu 等）。
  conditions: CCS 不能建 CCD 对象（只能建班长与分配规则）——权责边界必须记住
  tags: [structure, oxo-web-admin, ccs, separation-of-duties, menu-map]

- id: f13
  title: OXE Web Admin 菜单地图——实验涉及的全部路径
  type: menu-path
  source_pages: p65-77, p94-158, p213-239, p307-346, p389, p438, p461-475, p533-534, p554-558, p573-576, p591, p626
  source_chapter: OXE Web Admin session（各 How-To 中的 Select 路径汇总）
  source_quote: |
    "Select Translator> Prefix Plan>" (p66) / "Select Applications> CCD> Processing Group>" (p67)
    "Select Applications> CCD> Queue>" (p71) / "Select Applications> CCD> Pilot>" (p74)
    "Select Classe of Service> Phone Features COS>" (p134) / "Select SIP> SIP Ext. Gateway." (p153)
    "Select Translator> External Numbering Plan> Default DID num. translator>" (p154)
    "Select Inter-Nodes Links> Logical Links (ABC-F)> Loop-Hybrid" (p163)
  summary: |
    实验用到的 OXE Web Admin 路径全集：Translator（Prefix Plan 建 ACD 前缀 12；External Numbering
    Plan>Default DID num. translator 建 DID 翻译）；Applications>CCD（Processing Group / Queue / Pilot /
    Distribution Rule / CCD Users>CCD Operations data management / Statistic Pilot）；System（Voice
    Guides、Dynamic Voice Guides>Assignment）；Classe of Service>Phone Features COS（ACD Prefixes、
    Recordable Voice Guides、Silent Connection on Agent、Manual Hold、Park Call/Retrieve）；Users
    （建话机/座席/班长、TSC IP User>IP-Softphone Emulation、Progr.Keys、Rights）；SIP>SIP Ext. Gateway
    （POD 注册参数）；Trunk Groups>CSTA-Monitored；Inter-Nodes Links>Logical Links (ABC-F)（Loop-Hybrid、
    Hybrid or Direct Link Access）。登录口径两种并存：mtcl/Superuser2580*（多数章节）与 mtcl/mtcl
    （p153 收尾章）。
  conditions: 实验口径：IP 192.168.1.3；p153 一章密码写 mtcl（与全书 Superuser2580* 不一致，见 n11）
  tags: [menu-path, oxe-web-admin, navigation]

- id: f14
  title: CCS 主菜单地图——Call Flow mgt / Configurations / System / Real time / Statistics / Window
  type: menu-path
  source_pages: p99-120, p135-149, p167-193, p221-233, p237-260, p306-341, p364-372, p386-399, p431-448, p462-474, p518-526, p532-541, p556-564, p575-581, p590-604, p620-641
  source_chapter: CCsupervision application（各 How-To 中的 From the main menu, select 路径汇总）
  source_quote: |
    "From the main menu, select Call Flow mgt > Call Routing" (p99)
    "From the main menu, select Configurations> Pilot" (p103)
    "From the main menu, select Real time> Navigator" (p143)
    "From the main menu, select Statistics> Excel> Pilot" (p519)
    "From the main menu, select Call Flow mgt> Emergency closure." (p532)
  summary: |
    CCS 六大菜单域：Call Flow mgt（Call Routing：pilot 规则创建/应用/优先级/日历/Blocked 表；Call
    Distribution：分配规则与方向激活；Emergency closure：紧急关闭列表）；Configurations（Pilot：wrap-up/
    pause/服务水平/关闭地址；Pilot 下的 Call Routing 区加队列方向；Queue and Waiting Room；Processing
    Group>PG Agents / PG Other；Agents；Statistics Pilot；EWT Tables；Precompiled statistics；Voice
    Guide Management>Audio File Conversion / Audio File Update / Dynamic Voice Messages Configuration）；
    System（Pilot、Queue and Waiting Room 的系统级视图）；Real time（Navigator、Trunk group、Pilots S.L.、
    Pilots、Queue and Waiting Room、Processing Group>PG Agents/IVR/Team、Incidents、Alarms）；
    Statistics>Excel（Pilot、Agents、Transaction Code、Abandoned Calls、Statistics Pilot、Agent Session、
    Automatic edition restart）；Window（Customise：Network 节点声明、Statistics 对象数、Real time 刷新）。
  conditions: 菜单名以实验截图转写为准；不同 Edition 界面可能漂移
  tags: [menu-path, ccs, navigation]

- id: f15
  title: ccs.ini 文件结构与关键开关
  type: structure
  source_pages: p85-87, p511-512
  source_chapter: CCS APPLICATION OVERVIEW / CCS.ini file; SHOW STATISTIC WITH DATA
  source_quote: |
    "[network] … version=10.4.92.0 … my_name=pcoliv … id_terminal=36 … MultiSite=0 …
    CcsLight=0 … Site 1=151.1.1.3, 2538, NONE, 2538, 1_, 1, 1" (p86)
    "You must write the line ShowStatisticWithData in the file ccs.ini • In the section
    « default_configuration ». • ShowStatisticWithData=0 -> works as previously • ShowStatisticWithData=1
    -> only agents with data are displayed." (p512)
  summary: |
    ccs.ini 每次启动 CCS 时读取，默认位于 programData/Alcatel/CCsupervisor；内容含站点类型
    （MonoSite/MultiSite）、PABX 地址、PC 站名与终端 ID（0..127，全网唯一）、许可类型（CcsLight=1 需
    CCSLight token）。多数显示/阈值设置可经 "CUSTOMIZE" 窗口改而免手工编辑；CCS 升级时旧 ccs.ini
    可保留。例外：ShowStatisticWithData（CCS 10.5 新特性）必须手写进 [default_configuration] 节，
    控制座席会话报表是否只显示有数据的座席。
  conditions: id_terminal 冲突会导致站点异常；改 ShowStatisticWithData 无 GUI 入口
  tags: [structure, ccs-ini, configuration, file]

- id: f16
  title: CCS 安装向导决策链——九步选择
  type: flow
  source_pages: p89-93
  source_chapter: CCS software installation and set up (How-To) / Software installation
  source_quote: |
    "On Feature level window, select Full for a full CCS version installation. … On Feature level
    license window, select Monosite. … On Excel window, click on Yes to use Excel application to
    provide advanced statistics reports." (p92)
    "On Setup type window, select Windows standalone as the product installation type. … On Real Time
    Information when logged-off? Window, click on Yes … On ASM Script Editor window, click on No" (p93)
  summary: |
    安装链：NAS 拷贝到 Documents → 解压（More info → Run anyway）→ 运行 CCS.msi → 接受 EULA →
    默认安装路径 → 自动装 Microsoft Visual C++ 2017 Redistributable (x86) → Feature level 选 Full →
    许可类型选 Monosite → Excel 集成选 Yes → Excel 统计文件默认位置 → 语言（英文+法文，界面英文）→
    Setup type 选 Windows standalone → 用户文件默认路径 → 核对 Station ID → 无班长登录时也要实时
    信息选 Yes → ASM Script Editor 选 No → 复核摘要 → Install → ccs.ini 合并提示 OK → Finish。
  conditions: 实验口径：软件在 NAS 的 OTCC_NAS 共享；生产按许可类型改选 Multisite
  tags: [flow, ccs, installation, wizard]

- id: f17
  title: OXE 统计文件生成流水线——5 个临时文件 → 3 类合并文件
  type: diagram
  source_pages: p478-483
  source_chapter: STATISTICS WITH EXCEL / Statistic files generation principle
  source_quote: |
    "Each day, at midnight, 5 temporary files are created: obj<date>.sta, tr<date>.sta, ind<date>.sta,
    te<date>.sta, tc<date>.sta • They are kept 24 H • After 24 H, they are deleted, concatenated and
    induce in the consolidated files creation: « .sta » (dy,hr,ev)" (p480)
    "« hr yymmdd.sta » files, with a granularity of ¼ H, ½ H or 1 H. These detailed files are kept 5
    weeks per default • « dy yymmdd.sta » and « ev yymmdd.sta » files with a granularity of one day.
    These files are kept 12 months per default" (p481)
  summary: |
    统计数据流：OXE 硬盘 /usr4/afe 下每天午夜生成 5 个临时文件（obj 对象/tr 中继/ind 指示/te 座席/tc
    事务码），保留 24 小时后合并进合并文件并删除；合并文件在 /DHS3dyn/afe：hr*.sta（¼h/½h/1h 粒度，
    默认保留 5 周）、dy*.sta（对象日统计，保留 12 个月）、ev*.sta（对象状态变化：登入登出、退出/指派、
    PG 开关，保留 12 个月）。处理节奏：午夜 procedure（OHOO）+ batch-hour（1H00）。CCS 的 Excel 报表
    即消费这些 .sta 文件；通信票据（comm. tickets）在座席挂机后生成（含等待/振铃/通话/wrap-up/pause
    时长），RAM 缓存 15 分钟后写盘（p483）。
  conditions: 保留期可按磁盘容量配置；路径 /usr4/afe 与 /DHS3dyn/afe 为 OXE 侧
  tags: [diagram, statistics, files, pipeline, retention]

- id: f18
  title: Navigator 实时监控视图体系——对象图 + 定制化 + 桌面管理
  type: structure
  source_pages: p402-414, p430-437
  source_chapter: REAL TIME INFORMATION AND ALERTS / Navigator & customization
  source_quote: |
    "The snapshot, refreshed every 3 seconds by default, provides: Objects state: pilot, queue, agent,
    group (open, closed, ready, saturated, agent in conversation, ...) • Traffic indicator … Alarms
    indication (threshold violation)" (p402)
    "You can move the objects by clicking « shift »and the left key of the mouse … Selection mode :
    select the objects that will be displayed when returning to visualization mode." (p406)
  summary: |
    Navigator 是 CCS 的图形实时总览：顶区按钮（按号/名显示、explorer 模式、选择模式、对象信息、MSP
    统计、告警缩放、统计 pilot、前转组信息、super objects、定制入口）；底区显示对象动态信息。对象可
    shift+鼠标拖动；Explorer 树控制显示/隐藏；Real Time Info 定制每类对象旁的计数器（新版支持呼叫在
    队列中的进度显示）；Advanced Options 可为座席各话机状态配色、闪烁 CCD 对象；Zoom Options 设缩放。
    桌面管理：Save/Load desktop（按班长私有、存登录站点，可跨 CCS 站恢复）、自动保存/自动加载。
    实验中常用：每 pilot 一个页签（Tab #5/#6 命名 31600/31601）。
  conditions: 快照刷新 3 秒（1-50 可调，Configurations/System）；F1 有在线帮助
  tags: [structure, navigator, real-time, customization]

- id: f19
  title: 告警三级体系——Alarms / Alerts / Indications 与阈值配置入口
  type: structure
  source_pages: p424-428, p447
  source_chapter: REAL TIME INFORMATION AND ALERTS / Alarms
  source_quote: |
    "Alarms: this list contains the high-level alarms. The number of events stored (100 maxi) is
    indicated in the red coloured circle. • Alerts: the alerts only concern overflow of the thresholds
    defined for the trunk groups, pilots, queues, PGs and agents … (100 maxi) … yellow-coloured circle.
    • Indications: the indications are messages sent following a creation, modification or deletion of a
    CCd object. In the case of a calendar transition, an indication is sent one minute before." (p425)
  summary: |
    三级事件：Alarms（高级别告警，红色圈，存 100 条）、Alerts（中继组/pilot/队列/PG/座席的阈值越限，
    黄色圈，100 条）、Indications（CCD 对象增删改的系统消息，日历切换前 1 分钟会发一条，蓝色圈，100 条）。
    阈值配置分散在四个对象配置页：Configurations>Trunk group（如 busy rate alarm threshold，默认 80%）、
    Pilot、Queue and Waiting Room、Processing Group>PG Agent。告警呈现渠道：Alarms 窗口、Navigator
    对象闪烁（Advanced Options）、声音（Window/Customise/Sounds）、计数器背景色。
  conditions: 每类存储上限 100 条；告警可保存与删除
  tags: [structure, alarms, alerts, indications, thresholds]

- id: f20
  title: CCD Direct Calls 呼叫性质分布表——按座席状态判定 CCD 呼叫 vs 私人呼叫
  type: structure
  source_pages: p449-458
  source_chapter: CCD DIRECT CALLS / Distribution according to agent state
  source_quote: |
    "Private agent directory number = CCD agent directory number: all the external calls arriving on
    the agent set are CCD type calls • Private agent directory number different from the CCD agent
    directory number: • all the external calls arriving on the CCD agent directory number are CCD type
    calls, • all the external calls arriving on the private agent directory number are private type calls" (p451)
    "On pause: Pilot Direct call with Introduction VG / Private call … On partial unavailable: ACD call /
    Private call … Logged off: Extension out of service / Depending on private Extension type" (p455)
  summary: |
    直接呼叫机制三要素：①"pilot direct call"（专用 pilot，如实验的 31603）承接座席忙/不可用时的溢出并
    提供 wrap-up/pause 计时；②PG 参数 Pilot Direct Call + Outgoing ACD Call 把直达来话与座席外呼纳入
    CCD 统计；③私人号码（private agent number，登录时自动前转到座席号、登出自动取消）。呼叫性质判定
    （p455 表）：座席空闲/部分退出→打座席号是 ACD 呼叫、打私人号是私人呼叫；通话中→溢出到 direct call
    pilot（延时随 access COS）或溢出到实体；wrap-up/不可用→direct call pilot（无延时）/带介绍指南；
    pause/不可用→带介绍指南的 direct call 或私人呼叫；登出→私人号行为取决于其类型。来话总规则与
    去话规则（不可用态外呼为私人呼叫，p456）单列。
  conditions: 本地 ABC-F 混合链路不能用于 direct call 功能（p469 Warning）
  tags: [structure, direct-calls, private-number, ccd-vs-private]

- id: f21
  title: 日历体系——Pilot 日历（10 切换/日）与分配日历（20 切换/日）+ 特殊日
  type: structure
  source_pages: p607-616, p629-641
  source_chapter: CALENDAR / Calendar possibilities
  source_quote: |
    "Pilot Calendar … Maximum of 10 time slot transitions for each of the 7 days of the week. • Pilot
    rules concern general forwarding devices, routing directions and voice guides. • Distribution
    Calendar … Maximum of 20 time slot transitions for each of the 7 days of the week." (p616)
    "Special days override the days of the weekly calendar • A maximum of 50 special days can be defined." (p611)
  summary: |
    无日历时一套 pilot 规则+分配规则永久生效；有日历后按日期时间与特殊日切换多套规则。Pilot 日历：
    每 pilot 一个，每周每天最多 10 个时间片切换，每个切换指定规则 ID + 状态（Nor/Fwd），管通用转发、
    路由方向与语音指南；分配日历：挂在分配规则上，班长站可配置，每天最多 20 个切换，管队列方向、
    分配阈值与资源/呼叫选择参数。特殊日（须填日/月/年，不能选过去日期，覆盖周历，最多 50 个）。
    实验口径：Offer pilot 设工作日 08:00-12:00/13:30-19:00 用规则 0，午休与夜间、周末、特殊日用
    Closed_rule（规则 1）。
  conditions: 活动时间片上的修改不立即生效——要到下一个切换点才切换（见 n07）
  tags: [structure, calendar, time-slices, special-days]

- id: f22
  title: 语音指南体系——静态/动态、板卡与格式、CCD 指南清单、多语言编号
  type: structure
  source_pages: p194-210, p583-587
  source_chapter: VOICE GUIDES / DYNAMIC VOICE GUIDES / MULTI-LANGUAGE VOICE GUIDES
  source_quote: |
    "Static: several voice prompts are contained in 1 file. This file is fixed and cannot be modified.
    Example of file: vgadpcm.EN0 and vgadpcm.FR0 … 8 languages maximum for internal use … 40 languages
    maximum for external broadcast of voice messages" (p196)
    "GD3 or GA3 for common hardware • No board required in case of OMS … G711 (64 kbps) for crystal
    hardware • ADPCM32 (32 kbps) for common hardware" (p197)
    "Messages number: from 0 to 5999 • 40 messages per voice guide maximum" (p586)
  summary: |
    指南两分法：静态（打包文件不可改，如 vgadpcm.EN0/FR0）与动态（管理员可录可选）。广播需要板卡：
    通用硬件用 GD3/GA3，OMS 无需板卡；静态指南存 Flash，动态指南存 RAM；格式 G711（64kbps，crystal
    硬件）/ADPCM32（32kbps，通用硬件）。下载两步：先到 OXE 硬盘，再装进 GD3/GA3/OMS；工具三件：
    Alcatel Audio Station（做文件）、VGTransfer（传硬盘）、OXE mgr/OmniVista（装板卡）。CCD 环境指南
    清单：presentation、parking 1-6、dissuasion（劝退）、general forwarding、blockage、hold music。
    多语言：消息号 0-5999，每个指南最多 40 条消息（一语言一条），pilot 语言决定播哪条；实验编号法：
    3 位指南号 + 4 位消息号（首位=语言索引，如指南 683→消息 1683/2683）。
  conditions: 实验 OMS 板位 4-0（ACT-Board 4-0）；vgstat 4 0 查装载
  tags: [structure, voice-guides, boards, formats, multilanguage]

- id: f23
  title: 交互排队与 EWT 表结构——parking level 四种内容、6 阈值、IAA 树限制
  type: structure
  source_pages: p348-357
  source_chapter: INTERACTIVE QUEUING / EWT table
  source_quote: |
    "Parking Level … As specified for each Parking Level: Guide N° / IVR in queue PG directory N° /
    IAA directory N° / EWT Table Threshold(1 to 6)" (p351)
    "An EWT(Expected Waiting Time) table is managed in the normal waiting queue parking level … It
    contains 6 thresholds in which you can manage: An EWT value … An address • Only 2 kinds of directory
    number can be managed at this level: IAA N° or CCIVR N° • A voice guide N°" (p352)
    "Tree menus: 5 levels max • 4 choices max per level • 8 trees maxi • When an agent becomes free,
    the caller leaves the IAA menu • The IAA is interruptible" (p356)
  summary: |
    parking level 的四种填充物：语音指南号 / 队内 IVR PG 号 / IAA 号 / EWT 表（阈值 1-6）。EWT 表在
    CCS Configurations>EWT Tables 建，每表 6 个阈值，每阈值含 EWT 值（计算 EWT ≥ 该值即进入）+ 地址
    （仅 IAA 号或 CCIVR 号两种）+ 指南号；在 Call Flow mgt/Call Routing/Additional 里把表挂到 parking
    level。IAA（集成自动话务员）菜单树限制：最多 5 层、每层 4 个选项、最多 8 棵树；座席一空出来电者
    即离开 IAA；IAA 可被打断。CCIVR 为外部语音服务器（书中写作 "Contact center Interactive Voice
    Record"，属于原文拼写）。
  conditions: EWT 表只能挂在 normal 队列的 parking level（p352）
  tags: [structure, ewt, interactive-queuing, iaa, ccivr]

- id: f24
  title: "518 排队位置指南结构——固定段+变量段+固定段与播报规则"
  type: structure
  source_pages: p374-384
  source_chapter: "CCD WAITING QUEUE POSITION" VOICE GUIDE
  source_quote: |
    "The 'CCD waiting queue position' voice guide is set with up to 3 voice messages • A fixed Part:
    'You are in position' • A variable Part 'x' ( 1 < x <= 100 ) • A second Fixed Part: 'in the waiting
    queue'" (p377)
    "The Variable Part is made of several voice messages that give the positions from 1 to 50 then by
    step of 5 up to 100. … If an external caller is in position 63 in the waiting queue, the voice guide
    will announce the position 65" (p377)
    "The messages numbers are already created in the OXE (from 3226 to 4217)" (p379)
  summary: |
    指南 518 = 固定段 1（"您当前排在"）+ 变量段（位次）+ 固定段 2（"位于等待队列中"）；固定段每语言
    一条消息（L1=3226/3227，L2=3228/3229，……L16=3256/3257）；变量段 1-50 逐个播报、51-100 按 5 步进
    （63 位播 65），消息号 L1 从 3258 起、L2 从 3318 起、每语言步进 60，至 4217。播报规则（p382-383）：
    可设最大位次（上限 100），超限时播 pilot 的 inter-guide 音直到位次回落；多次播报每次重算位次，
    第 6 级循环播报；语言未管理→用默认语言，无默认语言则不播（跳下一级）；子消息缺失→播备份音；
    优先级呼叫插队时向被压后的来电者重播其原位次以掩盖回退。语言选择可来自 pilot 语言、ACR 呼叫
    档案语言技能或呼叫表征阶段。
  conditions: 每部分 16 种语言；编号 3226-4217 为 OXE 预置，不可自造
  tags: [structure, position-guide, 518, multilanguage, announcements]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-22）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 准备实验环境与 SIP 模拟器参数化 | 有 | f01, f02, f03 | 平台结构 + 号码规则 |
| task-02 | 掌握 CCD 矩阵模型（讲义） | 有 | f04, f05, f06, f07, f08, f09, f10 | 矩阵总模型 + 各对象结构 |
| task-03 | 创建基础 CCD 矩阵 | 有 | f12, f13 | 双控制台分工 + OXE 菜单 |
| task-04 | 安装配置 CCS | 有 | f14, f15, f16 | CCS 菜单、ccs.ini、安装链 |
| task-05 | 创建路由与分配规则 | 有 | f08, f09, f14 | 规则结构 + CCS 菜单 |
| task-06 | 创建 ACD 话机/座席/班长 | 有 | f10, f13 | 状态时序 + Users 菜单 |
| task-07 | 收尾 POD 配置 | 有 | f02, f03, f13 | 实例表、SIP/DID 路径 |
| task-08 | 开通本地 ABC-F 混合链路 | 有 | f13 | Inter-Nodes Links 路径与前置检查 |
| task-09 | 用 CCS 调优 CCD 对象参数 | 有 | f14 | Configurations 各页 |
| task-10 | 话机录制动态语音指南 | 有 | f22, f13 | 指南体系 + System 菜单 |
| task-11 | .wav 导入语音指南 | 有 | f22, f14 | 格式 + Voice Guide Management 菜单 |
| task-12 | 掌握座席/班长特性（讲义） | 有 | f10, f11 | 状态时序 + Rainbow 座席 |
| task-13 | 配置座席/班长特性 | 有 | f14 | Progr.Keys/PG/Agents 配置路径 |
| task-14 | 交互排队与 EWT | 有 | f23 | EWT 表结构 + IAA 限制 |
| task-15 | 排队位置指南 518 | 有 | f24 | 三段结构与播报规则 |
| task-16 | 实时监控与告警 | 有 | f18, f19 | Navigator 体系 + 告警三级 |
| task-17 | CCD 直接呼叫 | 有 | f20 | 呼叫性质分布表 |
| task-18 | Excel 统计 | 有 | f17, f14 | 统计文件流水线 + Statistics 菜单 |
| task-19 | 紧急关闭 | 有 | f14, f05 | Call Flow mgt 入口 + pilot FWD 态 |
| task-20 | 统计型 pilot | 有 | f14, f05 | Statistic Pilot 配置路径 + 三态问候指南 |
| task-21 | 座席欢迎指南 | 有 | f22, f13 | 动态指南 + 538/4500 编号体系 |
| task-22 | 多语言语音指南与日历 | 有 | f22, f21 | 多语言编号法 + 日历体系 |

补充说明：
- f01（课程主线）为 22 项任务的组织轴；f24（518 指南）、f23（EWT 表）同时支撑 task-14/15。
- 全部 22 项 task 均有框架类条目覆盖；数值类细节（优先级语义、容量上限、计时器默认值、统计保留期）留待 principle.md，逐步操作留待 case.md，Warning/限制留待 counter-example.md。
- 生产化边界提示：本书全部菜单路径基于 OXE R10.16 时代 Web Admin 与 CCS 界面，生产使用前须对照当版 OXE/CCS 文档；RLAB 与 SIP 模拟器相关条目（f02/f03）仅为实验口径。
