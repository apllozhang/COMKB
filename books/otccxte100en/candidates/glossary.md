# 术语/缩写/产品名候选 — OmniTouch Contact Center Standard (OTCCXTE100EN Ed09)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 46 条。PLTR/AFE/TSC/NOE/AGAP/ProACD/DID/ABC-F/CSTA/ITSP/OMS/FlexLM 等缩写书中未给全称，full_name 字段如实省略或标注"书中未展开"，不采信外部知识。
> 分类：本书为本地部署（on-premise）呼叫中心教材，无用户订阅体系，subscription 类以"许可/token"对齐。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: CCD
  category: concept
  source_pages: p21-29, p63
  source_quote: |
    "CCD Software integrated into OXE Call Server" (p21)
    "The Call Distribution is based on a matrix" (p23)
  definition: |
    本书中 CCD 与 Call Distribution（呼叫分配）同义使用：OXE 内置的呼叫分配软件与对象体系
    （CCD matrix / CCD objects / CCD users），即 OTCC Standard Edition 的核心引擎。书中未给
    "CCD" 三字母的全称展开。
  alias_or_related: Call Distribution（g02）、CCD matrix（f04）、OTCC Standard Edition（g25）
  tags: [concept, engine, core]

- id: g02
  term: Call Distribution (matrix)
  category: concept
  source_pages: p22-24
  source_quote: |
    "Queues Resources (PG) Called departments (pilots) … Call Distribution: Resource availability,
    Priorities, Longest idle time (load) … Call Routing: Priorities, Expected waiting times" (p24)
  definition: |
    呼叫分配矩阵模型：Pilot（被叫部门）→ Call Routing（路由，看优先级与预期等待）→ Waiting Queue
    （排队）→ Call Distribution（分配，看资源可用性/优先级/最长空闲）→ Processing Group（资源）。
  alias_or_related: f04 总模型；CCD（g01）
  tags: [concept, model, matrix]

- id: g03
  term: Pilot
  category: concept
  source_pages: p26, p43-50
  source_quote: |
    "The pilot can be in open state … The pilot can be in general forwarding state … The pilot can
    be in blocked state" (p26)
    "A routing rule is managed to associate each pilot with waiting queues (30 rules max per pilot)" (p43)
  definition: |
    Pilot（引导号/被叫部门号）：外部来话首先到达的虚拟号码，三态（Open/General Forwarding/Blocked），
    经路由规则（每 pilot 最多 30 条）把来话导向等待队列；每个状态有独立语音指南表（Normal/Blocked/
    General Forward Table）。亦称"Called department"。
  alias_or_related: Routing rule（g05）、三态问候指南（p50）、Statistic Pilot（g10）、Direct call pilot（g11）
  tags: [concept, pilot, states]

- id: g04
  term: Waiting Queue (WQ)
  category: concept
  source_pages: p27-28, p40, p350
  source_quote: |
    "be shared among several Pilots (30 max) • serve several Processing Groups (50 max) • Queued
    calls are served FIFO (First In/First Out)" (p27)
    "WQ=Waiting Queue" (p350)
  definition: |
    等待队列：呼叫的"停车常"，三类型（Normal 常规 / Intelligent Overflow 智能溢出 / Redirection
    重定向），FIFO 服务；最多被 30 个 pilot 共享、服务 50 个 PG；四状态（Open/Saturated/Closed/
    Blocked）；6 个 parking level 放指南/地址/EWT 表。
  alias_or_related: Parking level（g08）、EWT（g07）、queue 类型兼容表（f07）
  tags: [concept, queue, fifo]

- id: g05
  term: Routing rule / Distribution rule
  category: concept
  source_pages: p43, p54, p83
  source_quote: |
    "A routing rule is managed to associate each pilot with waiting queues (30 rules max per pilot)" (p43)
    "A call distribution rule (10 max) defines the distribution of the calls to the processing
    groups • A queue can have up to 50 possible distribution directions" (p54)
  definition: |
    两级规则：路由规则把 pilot 连到等待队列（≤30 条/pilot、全局 1200），管方向开闭、优先级与语音
    指南；分配规则把队列连到处理组（全局 ≤10 条），管资源选择/呼叫选择优先级。分配规则默认停用且
    须经 OXE 激活；所有方向默认关闭。
  alias_or_related: p01 优先级语义、n01/n02 默认关闭、Calendar（g15）
  tags: [concept, rules]

- id: g06
  term: Processing Group (PG)
  category: concept
  source_pages: p29, p40
  source_quote: |
    "Agent processing group • Made up of agent or supervisor sets • Forward processing group
    (on-pcx number) … Voice guide processing group … Rerouting processing group … I.V.R processing
    group • Connection to the CCivr application" (p29)
  definition: |
    处理组（资源）：五类型——Agent（座席组，唯一承接 ACD 分发）、Forward（前转到本机号码）、
    Voice Guide（播指南）、Rerouting（改道 ABC-F/公网）、IVR（接外部 CCivr）。实验基准矩阵：
    Agent_PG(31800)/Forwarding_PG(31801)/Voice_guide_PG(31802)。
  alias_or_related: f07 兼容矩阵、Agent（g18）
  tags: [concept, processing-group]

- id: g07
  term: EWT (Expected Waiting Time)
  full_name: Expected Waiting Time（书中直接展开，p350）
  category: concept
  source_pages: p44, p47-49, p350-356
  source_quote: |
    "EWT=Expected Waiting Time" (p350)
    "EWT = Average wait x (Nb of calls in queue + 1)" (p47)
  definition: |
    预期等待时间：系统按"平均等待 ×（队内呼叫数+1）"实时计算；三个用途——路由方向同优先级时的
    选择依据、队列饱和判据（EWT>最大等待时间即 Saturated）、EWT 表（6 阈值，每阈值挂指南与
    IAA/CCIVR 地址）实现分档播报。
  alias_or_related: TSP（g09）、EWT Table（f23）、Saturated（g04）
  tags: [concept, ewt, formula]

- id: g08
  term: Parking level
  category: concept
  source_pages: p45, p50, p351
  source_quote: |
    "6 Parking levels that contain • A Voice Guide • Or an Address: IAA or IVR in Queue • Or an EWT
    table: IAA or IVR in Queue (according to Expected Waiting Time)" (p45)
  definition: |
    停车级：普通等待队列内的 6 个播报层级（问候指南之后 L1-L6），每级可填语音指南号、地址（IAA 号
    或队内 IVR PG 号）或 EWT 表；下游资源释放时指南可被打断（cut auth）；第 6 级常作循环音乐保持。
  alias_or_related: Voice guide（g36）、EWT（g07）、cut auth（p225/232）
  tags: [concept, parking, queue]

- id: g09
  term: TSP / MSP / SOP
  category: concept
  source_pages: p47, p79-80, p168, p415
  source_quote: |
    "The 'Average waiting time' is calculated by the system over the TSP (traffic sampling period)
    which is defined for each waiting queue" (p47)
    "MSP (5 mn …60 mn) for statistics on MSP(*)" (p80)
    "These counters are refreshed according to the SOP (supervisor observation period) of 15 min by
    default." (p168)
  definition: |
    三个采样周期：TSP=话务采样周期（每队列定义，算 EWT，越短反应越快）；MSP=Monitoring Sampling
    Period（监控采样周期，5-60 分钟，MSP 统计的窗口）；SOP=supervisor observation period（班长
    观察周期，默认 15 分钟，smiley 刷新）。实验口径 TSP/MSP/SOP 均为 15 分钟档。
  alias_or_related: p08 刷新参数族、smiley（p07）
  tags: [concept, periods, sampling]

- id: g10
  term: Statistic Pilot
  category: concept
  source_pages: p543-551
  source_quote: |
    "Get more pilots for greeting guides • Extend the possibilities of obtaining statistics on the
    pilots • The statistic pilots are used in ACR (advanced call routing)." (p544)
    "Up to 3000 statistic pilots can be declared" (p546)
  definition: |
    统计型 pilot：对外是一个可拨的"业务号"，先播自己的问候指南再把来话转给唯一关联的本地路由
    pilot；可挂 Call Tag（≤32 字符）、ACR Profile、优先级；用于分业务统计与个性化问候。上限 3000 个；
    关联期间路由 pilot 不可删除，且不能兼任 direct call pilot。
  alias_or_related: Call Tag（g12）、ACR（g27）、Routing pilot（g03）
  tags: [concept, statistics-pilot]

- id: g11
  term: CCD Direct Call / Private agent number
  category: concept
  source_pages: p449-458
  source_quote: |
    "The CCD direct call facility is used to assign CCD facilities (supervisor call, transaction code,
    wrap-up, pause, etc.) to all the external calls reaching the agent directory number • A second
    directory number is assigned to the agent and used by the latter for receiving private external
    calls only" (p450)
  definition: |
    直接呼叫机制：经"pilot direct call"（如实验 31603）把打到座席号的外线来话纳入 CCD 待遇
    （wrap-up/pause/事务码/统计），座席忙时按 COS 延时溢出到该 pilot；座席另有私人号码接收私人
    来话，登录时自动前转到座席号、登出自动取消；PG 参数 Outgoing ACD Call 让座席外呼也计入 CCD。
  alias_or_related: p20 判定表、n24（默认阻塞指南 #75）、n31（无欢迎指南）
  tags: [concept, direct-calls, private-number]

- id: g12
  term: Call Tag
  category: concept
  source_pages: p550, p557-558
  source_quote: |
    "Call Tag Enter a call tag name (i.e. GOLD) Up to 32 characters to display during the ringing
    phase on the agent display." (p557)
  definition: |
    呼叫标签：挂在统计 pilot 上的 ≤32 字符显示串（如 GOLD），振铃期在座席话机显示；PG 参数
    Call Tag Display Timer 控制 0=仅振铃期、>0=振铃+接通后再显示该秒数；无 tag 时显示主叫与
    pilot 特征。
  alias_or_related: g10 统计 pilot、p22 显示选项
  tags: [concept, call-tag, display]

- id: g13
  term: Emergency Closure
  category: concept
  source_pages: p527-529
  source_quote: |
    "Emergency closure purpose. Allow to close manually a list of pilots • Up to 50 pilot lists can
    be created … 600 pilots maximum in each list" (p528)
  definition: |
    紧急关闭：一键手动关闭一列 pilot（≤50 列表、每列 ≤600 pilot、名单 ≤16 字符）；来话优先转紧急
    关闭地址（配置且可达时）否则播关闭指南；未配地址时向他转移被拒；统计计入"通用转发态来话"。
  alias_or_related: n05（管理员权限与清理）、n34（转移拒绝）
  tags: [concept, emergency-closure]

- id: g14
  term: Agent Welcome Guide (guide 538)
  category: concept
  source_pages: p566-570
  source_quote: |
    "When an agent set receives an external call, an agent welcome guide can be broadcast when the
    agent off hooks • No welcome guide on CCD direct calls" (p567)
    "a range of 1500 voice messages is reserved [4500-5999] … up to 5 files maximum" (p568)
  definition: |
    座席欢迎指南：座席摘机时向主叫（默认并含座席本人，COS Silent Connection on Agent=1 时仅主叫）
    播报的个性化问候；由座席自录自管（Welcome guide 动态键，登出时 ACD 前缀+92），机制指南 538
    与消息池 4500-5999（每座席最多 5 条文件）；direct call 来话不播。
  alias_or_related: n27/n28/n31、Voice guide（g36）
  tags: [concept, welcome-guide, 538]

- id: g15
  term: Pilot Calendar / Distribution Calendar / Special Days
  category: concept
  source_pages: p607-616
  source_quote: |
    "Each transition calls a call routing rule ID and a pilot status … Nor: Normal … Fwd: General
    Forwarding" (p612)
    "Maximum of 10 time slot transitions for each of the 7 days of the week … Maximum of 20 time
    slot transitions" (p616)
    "Special days override the days of the weekly calendar • A maximum of 50 special days can be
    defined." (p611)
  definition: |
    两套日历：pilot 日历（每 pilot 一个，切换路由规则 ID+状态 Nor/Fwd，≤10 切换/日）、分配日历
    （挂分配规则，≤20 切换/日）；特殊日（≤50 个，必填年月日，不可选过去日）覆盖周历；切换只在
    时间点执行，活动时间片上的修改延迟生效。
  alias_or_related: n07、p16、c20
  tags: [concept, calendar]

- id: g16
  term: Withdrawal (Unavailable) / Wrap-up / Pause
  category: concept
  source_pages: p275-280, p307
  source_quote: |
    "'Unavailable' feature allows an agent to withdraw temporarily from the processing group … Up to
    9 different types of withdrawal (Coffee break, WC, Smoke…) can be managed and are used for the
    statistics" (p275-276)
    "The pause between calls, or Union break, is the time between two consecutive CCD calls" (p279)
  definition: |
    座席三态：退出/不可用（可分 9 种类型供统计，退出者仍可被直呼其分机）；wrap-up（话后处理，自动
    挂 pilot/手动挂 PG，任何操作除 Queue info 外即取消）；pause（两通 CCD 呼叫之间的 union break，
    期间仍可接个人来电，手动 wrap-up 会重置 pause 计时）。
  alias_or_related: f10 状态时序、n22、p06 计时器
  tags: [concept, agent-states]

- id: g17
  term: Transaction code / Business code
  category: concept
  source_pages: p293, p343-344, p478
  source_quote: |
    "Transaction code from 1 to 15 digits • These codes are only stored in the CCD call records
    • Business codes from 1 to 3 digits • this codes are used in statistics" (p293)
  definition: |
    通话结束后座席摘的表征码：事务码 1-15 位（只存通话记录）；业务码 1-3 位（进 Excel 统计，全域
    上限 1000 个）；摘码窗口 Timer 单位 100ms（最小 10）。
  alias_or_related: n36、p17
  tags: [concept, codes, statistics]

# ── 二、角色 (role) ──

- id: g18
  term: Agent
  category: role
  source_pages: p31-33, p265-302
  source_quote: |
    "Agents: answering the CCD calls • unavailable, wrap-up, supervisor call, waiting queue info,
    call hold" (p266)
  definition: |
    座席：登录 ACD 话机承接 CCD 分发呼叫的用户；能力集含登入登出、退出/多类型退出、wrap-up、pause、
    呼班长、Queue info（WAIT/MAX/AVE/FREE/BUSY/UNAV）、事务码、保持/停车、CBL 选组、多线（MEA）。
    可为 Rainbow 用户形态（g24）。
  alias_or_related: g19 班长、g16 三态、p05 话机兼容
  tags: [role, agent]

- id: g19
  term: Supervisor
  category: role
  source_pages: p31, p274, p286-292
  source_quote: |
    "Supervisor set which can supervise several processing groups and can itself be part of a
    processing group as an agent • Unavailable, wrap-up, secret listening, barge in, call hold" (p31)
    "A supervisor is always self-assigning" (p274)
  definition: |
    班长：监督多个处理组、可兼作座席；专属能力：永久监控、秘密旁听（discrete listening）、强插
    （barge-in，三方有提示音）、受限强插（restricted intrusion，仅座席闻声）、代接求助（Help 键）、
    pilot 通用转发/PG 关闭键、分配日历管理。话机支持集比座席窄（无模拟/DECT/ALE 20H）。
  alias_or_related: n23、p05、g13（紧急关闭需 CCS ADMINISTRATOR）
  tags: [role, supervisor, monitoring]

- id: g20
  term: Fixed / Mobile / Self-assigning agent
  category: role
  source_pages: p271-273, p136-137
  source_quote: |
    "Fixed agent means that the agent can only log on to the set with which he is associated by
    management. There is no need to authenticate at the log-on. • Mobile agent means that the agent
    can log on from any authorized set. Authentication is required in this case." (p271)
    "Self-assignable agent … during the log-on, he will be able to decide in which processing group
    he wants to enter" (p272)
  definition: |
    三种座席形态：固定座席（绑定指定话机、登录免认证）、移动座席（任意授权话机登录、需认证）、
    自指派座席（登录时自选 PG；否则须设唯一优选组 Preferred Processing Group）。班长恒为自指派、
    无优选组。
  alias_or_related: g18、n23、c04 步骤 6-7
  tags: [role, agent-types]

- id: g21
  term: CCS Administrator / CCS supervisor (user account)
  category: role
  source_pages: p84, p542
  source_quote: |
    "It's possible to create new user accounts (administrator or supervisor), and to assign specific
    rights for each of them • Can be manage from the menu configuration / supervisor rights directly
    in the CCS" (p84)
    "You MUST be a CCS ADMINISTRATOR to be able to select the pilot in the emergency closure pilot
    list." (p542)
  definition: |
    CCS 应用内两类账号：administrator（全权，含紧急关闭列表选 pilot、Excel 参数等）与 supervisor
    （经 configuration/supervisor rights 授权的配置与可视化权）；与 OXE 侧班长（g19）是两个层面
    的"班长"，勿混。
  alias_or_related: g19、n05
  tags: [role, ccs-account]

- id: g22
  term: Public user / Local SIP user（模拟器角色）
  category: role
  source_pages: p10, p153, p400
  source_quote: |
    "MicroSIP – Public for public calls" (p10)
    "Local caller is on the waiting queue and will hear at a moment 'You are in position 2 in the
    queue.'" (p400)
  definition: |
    实验角色：Public user = Client PC 10 上经 ITSP1 公网网关呼入的模拟外部客户（拨 0210X… 号）；
    Local SIP user = 经本地 SIP 分机（31010/31011 MicroSIP）呼入的模拟内部呼叫者（拨 00210X…）。
    全部为实验口径。
  alias_or_related: f03、g34 MicroSIP、g33 ITSP1
  tags: [role, lab, simulator]

- id: g23
  term: mtcl / swinst / root（OXE 管理账号）
  category: role
  source_pages: p9, p65, p76
  source_quote: |
    "OXE … Login mtcl / swinst / root Password Superuser2580*" (p9 实例表)
    "Login Enter the mtcl login (i.e. mtcl)" (p65)
  definition: |
    OXE 三个系统账号：mtcl（Web Admin 图形管理与 SSH 命令行的主要账号，实验口令 Superuser2580*）、
    swinst（软件安装）、root（系统级）。CCS 侧另有 administrator/alcatel 默认账号（首次登录强制
    改密）。均为实验口径，生产必须替换。
  alias_or_related: n11（p153 口令矛盾）、n19
  tags: [role, accounts, lab]

- id: g24
  term: Rainbow CCD agent
  category: role
  source_pages: p34-37
  source_quote: |
    "Rainbow user can be used as a CCD Agent (CCD Supervisor not supported) … A new action « Log in »
    replace the standard routing menu." (p34)
  definition: |
    Rainbow 用户形态的 CCD 座席（无班长形态）：专用 Rainbow 账号、唯一分机=CCD agent number；三种
    登录——office phone（CSTA 监控物理 ACD 话机）、other phone（REX 池改址其它号码）、computer
    （REX 改址 WebRTC 网关 SIP 中继，远程免 VPN/SBC）。
  alias_or_related: f11、p19、Rainbow（g28）
  tags: [role, rainbow, remote-worker]

# ── 三、订阅/许可 (subscription) ──

- id: g25
  term: OTCC Standard Edition 的可选件与许可体系（本书的"订阅"位）
  category: subscription
  source_pages: p21, p79, p86, p92
  source_quote: |
    "Additional options (CCS, CCA, ACR, Soft Panel)" (p21)
    "CcsLight=0 ; (if =1, requires CCSLight token; if =0, requires Monosite or Multisite token
    according Multisite parameter)" (p86)
    "On Feature level license window, select Monosite." (p92)
  definition: |
    本书无用户订阅概念（on-premise）；对应"授权"层：OTCC Standard 为 OXE 内置，可选件 CCS（班长
    台）、CCA（座席桌面）、ACR（高级路由）、Soft Panel；CCS 按 token 授权——CCSLight token 或
    Monosite/Multisite token，FlexLM 服务器（实验 192.168.1.80）承载 OXE 侧许可。功能级安装选
    Full，许可类型选 Monosite（实验口径）。
  alias_or_related: FlexLM（g30）、CCS（g26）、n41（书外边界）
  tags: [subscription, licensing, token]

# ── 四、产品 (product) ──

- id: g26
  term: CCS / CCsupervision
  full_name: Alcatel-Lucent CCsupervision（安装向导名称，p91）
  category: product
  source_pages: p78-88, p91
  source_quote: |
    "Welcome to the Alcatel-Lucent CCsupervision Setup Wizard" (p91)
    "CCS main functions are as follows • System configuration • Management of the CCD objects …
    Real time supervision • Statistics and archiving • Reporting functions" (p79)
  definition: |
    呼叫中心班长/管理台（Windows 应用）：系统配置、CCD 对象修改、座席管理、规则开闭、实时监督
    （Navigator）、Excel 统计、紧急关闭；不能创建 CCD 底层对象（只能建班长与分配规则）。配置文件
    ccs.ini，CCS 10.5 起 ShowStatisticWithData。
  alias_or_related: g21、g25、f14 菜单图
  tags: [product, ccs, supervision]

- id: g27
  term: ACR
  full_name: Advanced Call Routing（书中展开，p544）
  category: product
  source_pages: p21, p544
  source_quote: |
    "The statistic pilots are used in ACR (advanced call routing)." (p544)
    "Additional options (CCS, CCA, ACR, Soft Panel)" (p21)
  definition: |
    高级路由可选项：统计 pilot 可挂 ACR Profile（含语言技能）、呼叫表征阶段可带语言技能——位置
    指南 518 的语言选择链里引用（p379）。本书只点名，细则在进阶教材（书外）。
  alias_or_related: g10、n41
  tags: [product, acr, option]

- id: g28
  term: Rainbow
  category: product
  source_pages: p34-37
  source_quote: |
    "CCD agent on Rainbow • Rainbow user can be used as a CCD Agent … With the WebRTC Gateway, we
    can have a CCD agent on a Rainbow softphone • The Rainbow application doesn't require VPN or SBC
    to support remote worker use case" (p34)
  definition: |
    ALE 云协作平台：本书仅作为 CCD 座席的一种接入形态出现（软话机座席 + 专用 GUI + Log in 动作），
    依赖 WebRTC 网关承载 computer 登录的音频。平台本体、订阅与网关部署不在本册范围。
  alias_or_related: g24、n41、WebRTC（g41）
  tags: [product, rainbow]

- id: g29
  term: OmniPCX Enterprise (OXE) / OXE-V
  category: product
  source_pages: p7, p9, p21, p23
  source_quote: |
    "The OTCC Standard Edition is a complete solution built into the OmniPCX Enterprise" (p23)
    "OXE OTCC_OXE cs1 (physical) cs1 (main) 192.168.1.1 192.168.1.3" (p9 实例表)
  definition: |
    ALE 企业 PBX（呼叫服务器），OTCC Standard 的宿主；实验实例 OTCC_OXE（cs1 物理/cs1m 主 CPU，
    192.168.1.1/192.168.1.3，实验口径），管理入口为 Web Admin（https://192.168.1.3）与 mtcl 控制台/
    SSH。OXE-V 为实验用虚拟化形态。版本口径：R10.16 教材、链路默认始于 R100、SFTP 强制始于 N3。
  alias_or_related: g23、f13、n08/n09
  tags: [product, oxe, pbx]

- id: g30
  term: OMS / FlexLM / GD3 / GA3 / GPA2（硬件与许可组件）
  category: product
  source_pages: p9, p152, p197, p568
  source_quote: |
    "OMS OTCC_OMS 192.168.1.13" (p9) / "FlexLM SERVER OTCC_FLEXLM Flex 192.168.1.80" (p9)
    "GD3 or GA3 for common hardware • No board required in case of OMS" (p197)
    "The agent welcome guides are stored on the Ram Memory, on the GPA2, GD3 or GA3 board." (p568)
  definition: |
    实验硬件/许可件：OMS（软件机架 3U，Rack 4 的 Virtual GD4，192.168.1.13，承载语音指南免专用
      板卡；全称书中未给）；FlexLM（许可服务器，192.168.1.80，口令 letacla1 实验口径）；GD3/GA3
      （通用硬件的语音指南板卡，G711=crystal、ADPCM32=common）；GPA2（欢迎指南 RAM 存储板）。
  alias_or_related: g25、p14、n27
  tags: [product, boards, licensing, lab]

- id: g31
  term: IPDSP (IP Desktop Softphone) / MicroSIP
  category: product
  source_pages: p10-11, p143
  source_quote: |
    "1 IP Desktop Softphone installed • 31000 terminal dedicated for agents" (p10)
    "3 MicroSIP softphones installed • MicroSIP – 31010 for internal calls … MicroSIP – Public for
    public calls" (p10)
  definition: |
    实验软话机：IPDSP（IP Desktop Softphone，ALE 座席软终端，承载 ACD 话机 31000/31001，有 CC/
    Perso/Menu 页签与 LogOn/WrapUp/Unavailable/Help 等动态键）；MicroSIP（第三方轻量 SIP 软话机，
    演内呼 31010/31011 与公呼 Public）。作 ACD 话机需启用 IP-Softphone Emulation（p128）。
  alias_or_related: g22、c04、p05
  tags: [product, softphone, lab]

- id: g32
  term: ALE Connect / CCA / Soft Panel
  category: product
  source_pages: p21, p38-39, p508, p522
  source_quote: |
    "ALE Connect solution • Emails • Live web chat • Facebook • Messenger • X-Twitter • Unique
    desktop for agents" (p38)
    "This feature is available since the release CCA 10.7.8.0." (p508)
  definition: |
    全渠道与座席桌面可选项：ALE Connect（邮件/网页聊天/社交渠道统一座席桌面，本书只给一页定位图）；
    CCA（ALE 座席桌面应用，弃呼报表的 click-to-call 回拨超链接自 CCA 10.7.8.0 起；全称书中未给）；
    Soft Panel（可选件，仅点名）。均为书外域。
  alias_or_related: n41、g25
  tags: [product, omnichannel, cca]

- id: g33
  term: ITSP1 / SIP Carrier Simulator / RLAB
  category: product
  source_pages: p5, p14-17
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in
    a data center." (p5)
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 … SIP simulator is hosted in the RLAB
    common area" (p15)
  definition: |
    培训基础设施：RLAB（Remote Labs 远程实验室，POD 池 + 公共区 NAS/SIP 模拟器/DNS）；ITSP1
    （模拟公网运营商，SIP 网关 gateway1.itsp1.com:10.20.30.51 + 公网网关 public.itsp1.com:
    10.20.30.50，注册账号 pbxP/alcatel）。全为实验口径，号码规则见 f03。
  alias_or_related: f02、f03、g22
  tags: [product, lab, simulator]

- id: g34
  term: OTCC_NAS / PuTTY / Alcatel Audio Station / VGTransfer
  category: product
  source_pages: p90, p76, p199
  source_quote: |
    "Install the CCS application software, available from the NAS drive." (p90)
    "PuTTY application (Client 10 instance) … Select the saved session called OXE – SSH" (p76)
    "Alcatel Audio Station • Used to create the voice guide files … VGTransfer tool • Used to
    download the voice guide files into the OXE disk" (p199)
  definition: |
    实验工具链：OTCC_NAS（共享网络盘，放 CCS 安装包与 .wav 素材）；PuTTY（SSH 客户端，会话
    OXE-SSH，字符集 ISO-8859-1）；Alcatel Audio Station（制作语音指南文件，本书未展开）；
    VGTransfer（指南文件传 OXE 硬盘的工具，本书未展开，实验用 CCS 的 Audio File Update 替代）。
  alias_or_related: p14、c02、c08
  tags: [product, tools, lab]

# ── 五、协议/接口 (protocol) ──

- id: g35
  term: ABC-F (hybrid link)
  full_name: 书中未给全称
  category: protocol
  source_pages: p159-165, p29
  source_quote: |
    "Select Inter-Nodes Links> Logical Links (ABC-F)> Loop-Hybrid … Multi access hybrid link …
    At least two acesses must be created." (p163)
    "Rerouting to the ABC-F or public network" (p29)
  definition: |
    OXE 节点间逻辑链路（本书语境=本地混合链路）：供内呼 pilot 使用；同 Node 不同 Network 上声明，
    Loop-Hybrid 多路混合链路 + ≥2 条 access（B Channel 信令）；hybvisu -f all 查 UP、rsthyb 重启；
    R100 起链路默认存在。不能用于 direct call 功能。
  alias_or_related: n03/n04/n09、c06
  tags: [protocol, abc-f, link]

- id: g36
  term: CSTA
  full_name: 书中未给全称
  category: protocol
  source_pages: p34-35, p414, p438
  source_quote: |
    "CSTA … Agent is logged in / Agent is logged out" (p35 时序图标注)
    "CSTA-Monitored must be set to « yes » in the OXE to display values for the trunk group" (p414)
  definition: |
    本书两处用法：①Rainbow CCD 座席场景中 Rainbow 与 OXE 间的呼叫控制接口（登录/登出经 CSTA 通知）；
    ②OXE 中继组属性 CSTA-Monitored——开启后 CCS 才能显示该中继组实时值。
  alias_or_related: g24、n29
  tags: [protocol, csta]

- id: g37
  term: SIP / SIP trunk group / SIP Ext. Gateway
  category: protocol
  source_pages: p15-16, p153
  source_quote: |
    "SIP Trunk Group … ITSP1 SIP Gateway 1 gateway1.itsp1.com" (p15)
    "Select SIP> SIP Ext. Gateway. … Registration ID pbxN" (p153)
  definition: |
    会话发起协议：实验中 OXE 经外部 SIP 网关（SIP> SIP Ext. Gateway，Registration ID/Outgoing
    username=pbxN，SIP 域 sip.itsp1.fr）注册到模拟运营商；公共 SIP trunk 组（实验名 1-T2-SIP
    PUBLIC）承载外呼与公网来话；WebRTC 网关 computer 登录时 REX 改址到"WebRTC Gateway SIP Trunk"。
  alias_or_related: f03、g28、g33
  tags: [protocol, sip, trunk]

- id: g38
  term: G711 / ADPCM32 / A-Law .wav（语音编码与文件格式）
  category: protocol
  source_pages: p197, p241
  source_quote: |
    "G711 (64 kbps) for crystal hardware • ADPCM32 (32 kbps ) for common hardware" (p197)
    "The .wav files … have got the following attributes: A-Law, 8000Hz, 64 Kbps, mono" (p241)
  definition: |
    语音指南两类编码：G711 64kbps（crystal 硬件）、ADPCM32 32kbps（common 硬件）；外部 .wav 素材
    标准为 A-Law/8000Hz/64kbps/单声道，经 CCS Audio File Conversion 转换后才可装入板卡。
  alias_or_related: p14、c09
  tags: [protocol, codecs, voice-guides]

- id: g39
  term: SFTP / SSH / RDP
  category: protocol
  source_pages: p76, p157, p245
  source_quote: |
    "SFTP Enable the SFTP connection (mandatory from OXE N3)" (p245)
    "Click on Open to setup a SSH connection." (p76)
    "3 Remote Desktop Connection … RDP connection to Client PC 10 instance" (p156-157)
  definition: |
    传输与访问三件：SFTP（CCS 向 OXE 传语音文件，N3 起强制，前提 OXE 侧 SSH 已实施）；SSH（PuTTY
    进 mtcl 命令行，注意收尾章记载实验 OXE "SSH is disabled" 与 p76 SSH 会话并存的实验语境差异，
    按 RLAB 实际为准）；RDP（Windows 远程桌面，实验串联 Client PC 10/11 并重定向音频）。
  alias_or_related: n08、n19、c05
  tags: [protocol, sftp, ssh, rdp]

- id: g40
  term: WebRTC / VPN / SBC / REX
  category: protocol
  source_pages: p34-37, p36
  source_quote: |
    "With the WebRTC Gateway, we can have a CCD agent on a Rainbow softphone • The Rainbow
    application doesn't require VPN or SBC to support remote worker use case" (p34)
    "Pool of Remote Extensions configured as ACD sets … REX is configured to route calls to the
    WebRTC Gateway SIP Trunk" (p37)
  definition: |
    远程座席技术栈：WebRTC 网关承载 Rainbow 软话机座席的音频（computer 登录时 REX 改址到网关 SIP
    中继）；REX=Remote Extension（远端分机池，可配成 ACD set，改址到其它电话或网关）；卖点免
    VPN/SBC。网关部署不在本册。
  alias_or_related: g24、f11、n41
  tags: [protocol, webrtc, rex, remote]

- id: g41
  term: DID (translation)
  full_name: 书中未给全称
  category: protocol
  source_pages: p16, p154
  source_quote: |
    "Translator/External Numbering Plan/Default DID num. translator … First external number 33210N41000
    … First internal number 31000 … Range Size 1000" (p154)
  definition: |
    外线号码直译表：把公网来话号码段映射到内部分机段（实验：首外线 33210N41000 → 首内线 31000、
    段长 1000，N=POD 号）；路径 Translator> External Numbering Plan> Default DID num. translator。
    分机 31002 的公网号即 3321PN41002。
  alias_or_related: f03、c05
  tags: [protocol, did, numbering]

- id: g42
  term: Tel protocol (click-to-call hyperlink)
  category: protocol
  source_pages: p508, p522
  source_quote: |
    "A hyperlink based on the Tel protocol allows to call a customer. This feature is available since
    the release CCA 10.7.8.0." (p508)
  definition: |
    弃呼报表中主叫号码的超链接协议（tel:）：CCA 10.7.8.0 起点击即回呼客户；依赖 CCA 座席桌面，
    本书只在此处引用。
  alias_or_related: g32、c15
  tags: [protocol, tel, callback]

# ── 六、资源 (resource) ──

- id: g43
  term: Voice guide（静态/动态）与系统预置指南
  category: resource
  source_pages: p196-201, p205-209, p214, p379, p389, p574
  source_quote: |
    "Static: several voice prompts are contained in 1 file. This file is fixed and cannot be
    modified. Example of file: vgadpcm.EN0 and vgadpcm.FR0" (p196)
    "Dynamic: modifiable, specified voice prompts can be recorded by the administrator." (p196)
    "Each prompt (voice message) is associated to a number (e.g. 683)" (p201)
  definition: |
    语音指南资源：静态（打包文件，如 vgadpcm.EN0/FR0，Flash 存储）与动态（管理员录制，RAM 存储，
    板卡 GD3/GA3/OMS/GPA2 承载）；CCD 清单=presentation/parking 1-6/dissuasion/general forwarding/
    blockage/hold music；指南号放矩阵、消息号供录制（3 位+4 位语言前缀法）；预置件：518（排队
    位置）、538（欢迎机制）、消息 3226-4217（位置段）、备份音 56、默认演示指南 70、直连阻塞默认
    75。文件落 /usr7/vg/dhs。
  alias_or_related: p13/p14、n27、g08
  tags: [resource, voice-guides, presets]

- id: g44
  term: ccs.ini
  category: resource
  source_pages: p85-87, p95, p512
  source_quote: |
    "CCS.ini file is read every time the CCs is started • This file is located in programData /
    Alcatel / CCsupervisor by default" (p85)
  definition: |
    CCS 配置文件（programData/Alcatel/CCsupervisor）：站点类型、PABX 地址、站名与 id_terminal
    (0..127)、token 类型、站点行；升级可保留；多数设置经 CUSTOMIZE 窗口写入；特例参数
    ShowStatisticWithData 须手改 [default_configuration] 节。修改后重启 CCS 生效。
  alias_or_related: f15、p10、n10、n21
  tags: [resource, ccs-ini]

- id: g45
  term: 统计文件（obj/tr/ind/te/tc → dy/hr/ev/iac/oac .sta）
  category: resource
  source_pages: p478-481, p506
  source_quote: |
    "dy<date>.sta hr<date>.sta ev<date>.sta … obj<date>.sta tr<date>.sta ind<date>.sta te<date>.sta
    tc<date>.sta Files used by the CCS application" (p479)
    "-rw-rw-rw-. 1 mtcl tel 36 avr 2 16:30 iac190402.sta … oac190402.sta" (p506)
  definition: |
    OXE 侧统计文件资源：临时 5 件（obj 对象/tr 中继/ind 指示/te 座席/tc 事务码，午夜生成、存 24h，
    /usr4/afe）；合并件 dy（对象日统计）/hr（¼h-1h 明细，存 5 周）/ev（状态变化流水，存 12 月），
    位于 /DHS3dyn/afe；弃呼专用 iac/oac <date>.sta。Excel 报表与帮助文档 Stat_lang.pdf（CCS 端
    ProgramData 下）是消费端。
  alias_or_related: p11、f17、c15
  tags: [resource, statistics, files]

- id: g46
  term: ACD prefix / 编号资源（12、401、580、91、92、66、67）
  category: resource
  source_pages: p66, p216-217, p346-347, p457, p568
  source_quote: |
    "Number Enter the ACD prefix number (i.e. 12)." (p66)
    "Select prefix 401. … Local Features Recordable Voice Guides … Select prefix 580. … Tone test" (p216-217)
    "Number Enter the prefix number (i.e. 67) … Manual Hold … (i.e. 66) … Park Call/Retrieve" (p346-347)
  definition: |
    译码器前缀资源（法国目标库实验值）：12=ACD 功能前缀（+1 退出/+2 wrap-up/+3 呼班长/+5 登出/
    +6 登入/+91 私人号状态/+92 登出录欢迎指南，类型扩展 +1+类型号）；401=录音前缀；580=试听前缀；
    66=停车取回、67=手动保持（Annex 参考不实施，n06）。均在 Translator> Prefix plan 定义并在
    COS 启用。
  alias_or_related: p04、n06、c08
  tags: [resource, prefixes, numbering]
```

---

## 收尾自检：任务覆盖（task↔id 映射）

| task | 任务 | 术语类覆盖 | 对应 id |
|---|---|---|---|
| task-01 实验环境 | 有 | g22、g23、g30、g31、g33、g34 |
| task-02 CCD 模型 | 有 | g01-g09、g16、g17 |
| task-03 基础矩阵 | 有 | g01-g06、g43、g46 |
| task-04 CCS 安装 | 有 | g26、g30、g44 |
| task-05 规则 | 有 | g05、g15 |
| task-06 座席班长 | 有 | g18-g20、g23、g31、g46 |
| task-07 收尾 POD | 有 | g22、g33、g37、g41 |
| task-08 ABC-F | 有 | g35 |
| task-09 对象调优 | 有 | g07、g09、g16 |
| task-10 话机录指南 | 有 | g43、g46、g34 |
| task-11 .wav 导入 | 有 | g38、g44 |
| task-12 特性讲义 | 有 | g16-g20、g24、g40 |
| task-13 特性配置 | 有 | g17、g19、g46 |
| task-14 EWT | 有 | g07、g08、g09 |
| task-15 位置指南 | 有 | g43 |
| task-16 实时告警 | 有 | g09、g36、g19 |
| task-17 直接呼叫 | 有 | g11、g24、g40 |
| task-18 Excel | 有 | g17、g32、g42、g45 |
| task-19 紧急关闭 | 有 | g13、g21 |
| task-20 统计 pilot | 有 | g10、g12、g27 |
| task-21 欢迎指南 | 有 | g14、g30、g43 |
| task-22 多语言/日历 | 有 | g15、g38、g43 |

说明：
- subscription 类（g25）按"许可/token"对齐——本书为 on-premise 产品，无用户订阅；glossary 总数 46 条，PLTR（p117 出现但未展开，见 f09）与 AFE/TSC/NOE/AGAP/ProACD 等书中未给全称的缩写已在相应条目或 full_name 字段如实标注，未编造。
- 六类分布：concept 17 / role 7 / subscription 1 / product 9 / protocol 8 / resource 4。
