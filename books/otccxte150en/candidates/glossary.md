# 术语/缩写/产品名候选 — OmniTouch CC Standard · Advanced Call Routing (OTCCXTE150EN Issue 01)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 55 条。六类口径说明：本书为呼叫中心技术教材，subscription 类仅 1 条（软件许可 N°167，原书唯一"许可"条目），role 类为 CCD 侧坐席/主管角色。ASM/IAA/MAO/REX 等缩写书中未给全称展开的，full_name 如实省略或不采信外部知识；ASM 书中写作 "Agent Selection Modul"（p6，原书拼写），照录。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: ACR (Advanced Call Routing)
  full_name: Advanced Call Routing（书中 p3 标题展开）
  category: concept
  source_pages: p3-18
  source_quote: |
    "ACR purpose • The ACR feature is based on script • An ACR script editor is embedded in the CCS and
    allows you to create ACR scripts with ACR rules like (Rule ISM, Rule LCA, …) • ACR script is attached to
    an ACR pilot • The ACR script is executed by the ASM Server" (p6)
  definition: |
    本书主题特性：基于脚本的呼叫路由。脚本编辑器内嵌于 CCS，脚本挂到 ACR Pilot，由 ASM 服务器执行，
    按规则 + 主叫号 + 呼叫标签 + 被叫号等返回可用坐席列表，替代"每坐席一组 + 外部应用"的传统做法。
  alias_or_related: 载体见 g02 ASM、g03 ACR Pilot；规则族见 g13
  tags: [concept, core, routing]

- id: g02
  term: ASM (Agent Selection Modul)
  full_name: Agent Selection Modul（书中 p6 展开，"Modul" 为原书拼写）
  category: concept
  source_pages: p6, p9-11, p320-321
  source_quote: |
    "ASM: Agent Selection Modul • The ASM Server can be internal (running on OXE) or external (running on
    Windows PC)" (p6)
    "The ASM server is in charge of Script interpretation • Data base queries • Update of data base •
    Calculation of the agent list" (p10)
  definition: |
    坐席选择模块：解释脚本、查询/更新数据库、按坐席配置 + 脚本规则 + 呼叫档案计算坐席列表的服务器。
    两种部署——内部（OXE 上的 alb 进程）与外部（Windows PC 服务，见 g40）；外部版额外支持外部数据库
    访问。
  alias_or_related: 内部实现 = g39 alb 进程；外部部署见 g40 External ASM
  tags: [concept, core, asm]

- id: g03
  term: ACR Pilot
  category: concept
  source_pages: p6, p12-13, p22, p113
  source_quote: |
    "ACR script is attached to an ACR pilot" (p6)
    "ACR Pilot -> Normal Queue & Waiting Room … No resource selection priority" (p13)
  definition: |
    承载 ACR 脚本的引导号（实验口径 3x603/31604）：接受话务方向，呼叫经它进入等待房间并触发脚本执行。
    与普通 Pilot 的差异：挂等待房间、无资源选择优先级（选人由 ASM 接管）、同一时刻仅激活 1 个脚本。
  alias_or_related: 对照普通 Pilot（挂等待队列，走 CCD 常规分发）；统计 Pilot 见 g04
  tags: [concept, pilot, telephony]

- id: g04
  term: Statistic Pilot
  category: concept
  source_pages: p36, p168
  source_quote: |
    "Pilot Stat. Directory Number Statistic Pilot Number • Directory Name Name of the Statistic Pilot (16
    characters) • Routing Pilot Directory Number of the Pilot (ACR Pilot)" (p36)
    "all tag is a character string associated with a call transiting through this statistical pilot and operated
    by ACR distribution mechanisms" (p168, 首词 "all" 为原文笔误)
  definition: |
    统计引导号：业务入口（如车险/家险），带呼叫档案与可选 Call Tag，汇入 Routing Pilot（ACR Pilot）。
    容量 1000 个；配置可在 OMF 或 CCSupervisor 侧改；其 Call Tag 是 ACR 分发机制的输入之一。
  alias_or_related: 路由终点见 g03；Call Tag 见 g09
  tags: [concept, pilot, statistics]

- id: g05
  term: Waiting Room
  category: concept
  source_pages: p12-14, p233
  source_quote: |
    "Waiting Rooms are needed in ACR & don't work in FIFO mode" (p12)
    "No priority for resource selection. The resource selection is made by the ASM Selection Modul (ASM).
    The ASM create a dynamic Processing Group" (p233)
  definition: |
    ACR 专用停放区：不按 FIFO，ASM 返回的坐席列表（动态组）附着在房间里，呼叫按 ISM 成本/优先级/等待
    时间被选中处理。与等待队列互斥（不能同开）。
  alias_or_related: 对照 Waiting Queue（FIFO、普通 CCD）；容量见 p18（队列与房间合计 600）
  tags: [concept, parking, acr]

- id: g06
  term: Dynamic Group
  category: concept
  source_pages: p12
  source_quote: |
    "The ASM server generates a list of agents who match the ACR script needs — Dynamic Group" (p12)
    "the ASM returns a list of agents and this list it is called dynamic group" (p14)
  definition: |
    动态组：ASM 每次呼叫即时算出的坐席列表——不是 PBX 静态分组。呼叫带着该列表进等待房间，分发时
    从中选人。
  alias_or_related: 产生方式见 g02 ASM；附着点见 g05 Waiting Room
  tags: [concept, dynamic-group]

- id: g07
  term: Call Profile
  category: concept
  source_pages: p15, p39, p172
  source_quote: |
    "Call Profile (List of attributes) • ACR Call Profile • Required skills to handle the call (up to 7)" (p15)
    "Mandatory or Optional Mandatory -> the agent liable to process the call must have the skill to be
    selected • Preference 1 to 7 only for Languages (1 for the highest priority language)" (p39)
  definition: |
    呼叫档案：呼叫的技能需求清单——最多 7 项技能 × 级别 1-9 × 强制/可选，语言类技能另有偏好 1-7
    （1 最优先）。ISM 规则按档案计算匹配成本；转移时最后一个档案覆盖之前的。
  alias_or_related: 需求方对照坐席技能（g10 Skill）；取值域见 principle p06
  tags: [concept, call-profile, ism]

- id: g08
  term: Characteristics List (CHARACTERISTICS_LIST)
  category: concept
  source_pages: p15, p43, p259
  source_quote: |
    "Characteristics List : 1000 … Characteristics (per call profile/ per Agent / max) : 7 / 50 / 20000" (p18)
    "LIST[%1]=CHARACTERISTICS_LIST" (p259)
  definition: |
    特征列表：呼叫运行时实际携带的技能特征集合，脚本里 ISM 规则最常用的输入（RULE_ISM
    CHARACTERISTICS_LIST）；可赋给 skill 型 LIST 变量参与运算。
  alias_or_related: 与 Call Profile（g07）区分——档案是定义、特征列表是运行时值
  tags: [concept, characteristics, ism]

- id: g09
  term: Call Tag
  category: concept
  source_pages: p15, p168-171, p173
  source_quote: |
    "Call Tag • CSTA filed for call identification" (p15, "filed" 为原文笔误)
    "The code entry guide prompts the caller to dial a code (max code length = 16 digits) and send it to the
    CSTA application as "Correlator data"." (p169)
    "The last Call tag met in the call context overwrites the previous one" (p173)
  definition: |
    呼叫标签：随呼叫走、受 ACR 分发机制操作的字符串（本质是 CSTA Correlator data）。三来源——统计
    Pilot 静态标、IAA 编码叶（≤16 位）、CCivr TransferCall 构件；可作脚本与内部/外部数据库的索引键；
    转移时最后者覆盖前者。
  alias_or_related: CSTA 见 g45；Correlator data 同义
  tags: [concept, call-tag, csta]

- id: g10
  term: Skill / Domain / Weight
  category: concept
  source_pages: p37-38, p41
  source_quote: |
    "Name Name of the Domain (1 to 16 characters) … Weight Weight used by the Individual Skill Mapping
    (ISM) calculation algorithm to classify domains (1 for the least important to 20 for the most
    important)." (p37)
    "These attributes are used to assign a set of skills and level of expertise to the Operator • Level 1-9" (p41)
  definition: |
    技能体系三件：技能（1-16 字符名 + 1-4 字符缩写 + ID 0-99）挂在他属域（1-16 字符、ID 0-99、权重
    1-20，权重参与 ISM 计算）；坐席按技能配级别 1-9。容量：域 20、技能 1000。
  alias_or_related: ISM 见 g13；级别与档案见 g07
  tags: [concept, skill, domain]

- id: g11
  term: ISM cost
  category: concept
  source_pages: p221, p235, p237
  source_quote: |
    "ISM cost • Call parked in a waiting room • ISM rule The ISM cost is calculated in the script according to
    the profile • Other rule No ISM cost, so the cost is fixed by the system to "0" • Call parked in a waiting
    queue No ISM cost, so the cost is fixed to an unlimited value" (p235)
  definition: |
    ISM 成本：呼叫在等待房间里被选中的代价——ISM 规则按档案与坐席技能算出（语言偏好参与，示例
    Ag1=0/Ag2=3），其他规则为 0，等待队列里的普通 CCD 呼叫为无穷。越小越先被服务。
  alias_or_related: 选呼次序见 principle p23；ACR Actual Waiting 见 g20
  tags: [concept, ism, cost]

- id: g12
  term: PLTR / LIT
  full_name: PLTR=Period Logon Time Ratio（书中展开）；LIT=Logon Idle Time（p240 展开）
  category: concept
  source_pages: p239-242
  source_quote: |
    "In case of equal cost, agents are sorted increasingly according to their PLTR (Period Logon Time Ratio)" (p239)
    "asm_ag_free_duration= 1 in this case LIT (Longest Idle Time) is used (rule Idle-time)." (p242)
  definition: |
    Idle 规则的两种排序语义：PLTR=统计周期（默认 5 分钟）内处理呼叫时长/登录时长的比率升序（参数值
    0，默认）；LIT=登录后最长空闲优先（参数值 1 单机、2 组网）。由 parameters.cfg 的
    asm_ag_free_duration 决定，改动需重启 MAIN_AFE。
  alias_or_related: 参数与版本见 g38 parameters.cfg
  tags: [concept, idle, sorting]

- id: g13
  term: 9 ACR Rules（ISM / LCA / Authorized / Unauthorized / Redirection / Redistribution / Idle / Com / IVR）
  category: concept
  source_pages: p7-8, p244
  source_quote: |
    "Individual Skill Mapping Rule (ISM) … Last Called Agent Rule (LCA) … Authorized list Rule /
    Unauthorized list Rule … Redirection Rule … Redistribution Rule … Idle Rule … Com Rule … IVR
    (Inter Active Voice response) Rule" (p7-8)
    "Single ACR Rules … LAST CALLED AGENT, REDIRECTION, REDISTRIBUTION, IVR • Combinable Rules …
    AUTHORIZED LIST, UNAUTHORIZED LIST, ISM, IDLE, COM" (p244)
  definition: |
    规则族：ISM（技能映射选最优）、LCA（选上次接听者）、授权/非授权名单（静态圈定/排除）、重定向（转
    号）、再分发（退下一路由方向）、Idle（按空闲/PLTR 排序）、Com（按服务呼叫数排序）、IVR（送 CCivr
    资源组）。单用规则 4 种须独占 APPLY，可组合规则 5 种，Idle 与 Com 互斥。
  alias_or_related: APPLY 语义见 principle p25；各规则定义页 p51-257
  tags: [concept, rules, taxonomy]

- id: g14
  term: Direct Call / CALL_TYPE / DICA
  category: concept
  source_pages: p105-115
  source_quote: |
    "The call type "Direct_Call" can be tested with an ACR script … Keyword: CALL_TYPE" (p114)
    "Domain: Media • Skill: DirectCall • Abbreviation: DICA" (p111)
  definition: |
    直拨族三件：CCd Direct Call 特性把打到坐席 DN 的外部呼叫 ACD 化（经处理组的 Pilot Direct Call）；
    脚本用关键字 CALL_TYPE=DIRECT_CALL 识别直拨；DICA=配私有号后系统自动挂的开关型技能（Domain
    Media），停用即完全不可直拨。
  alias_or_related: 私有号与 Pilot Direct Call 见 g15
  tags: [concept, direct-call, dica]

- id: g15
  term: Pilot Direct Call / Private Agent Number
  category: concept
  source_pages: p106, p110, p137
  source_quote: |
    "Complete the "Pilot direct call" parameter at the agent processing group level by indicating the pilot
    number used for this facility • Complete the Private agent number parameter in the agent data" (p106)
    "Declare the "ACR Pilot" as the "Pilot for Direct Call" in the Agent Processing Group" (p137)
  definition: |
    直拨特性两个配置点：处理组级参数 Pilot Direct Call 填承接直拨溢出的 Pilot 号（实验口径填 ACR Pilot
    31604）；坐席数据的 Private Agent No. 填私有号（实验口径 31001）——该参数决定呼叫类型判定（CCd
    还是 private）。
  alias_or_related: 行为语义见 g14 与 principle p15
  tags: [concept, direct-call, configuration]

- id: g16
  term: Internal Database (ACR Data)
  category: concept
  source_pages: p130-141
  source_quote: |
    "Caller Identification: Calling Number • Call Tag • Agent Number (in case of Direct Call) … Associated
    Information: Name • Call Profile • Authorized List • Unauthorized List • Call Priority" (p131)
    "Note: 4000 entries (single value or range) can be created in the Internal Database" (p131)
  definition: |
    ACR 内部数据库：以主叫号（完整/通配、单值/区段）、Call Tag、直拨坐席号为键，存名字、呼叫档案、
    授权/非授权名单、呼叫优先级；容量 4000 条。脚本以 CALL_PROFILE[键]、CALL_PRIORITY[键]、
    AUTHORIZED_LIST[键] 取用。
  alias_or_related: 外部数据库见 g42；配置入口 CCS ACR Data
  tags: [concept, internal-database]

- id: g17
  term: Reselection / SEQUENCE / Reselection Timeout
  category: concept
  source_pages: p43, p97-98, p115
  source_quote: |
    "If one agent is available, he will be rung; if all agents are busy, the call will be parked in the waiting
    room for 10 seconds, then the script is re-executed" (p97)
    "SET RESELECTION_TIMEOUT=%180" (p115)
  definition: |
    重选机制：坐席全忙时呼叫在等待房间停指定秒数后脚本重新执行，执行轮次记在 SEQUENCE 变量里
    （SEQUENCE=%1 为首轮）。脚本用 SET RESELECTION_TIMEOUT 定单轮时长，用 SEQUENCE 分支实现
    "等 N 秒→转走"类业务。空列表反复重试后走路由管理直至封锁。
  alias_or_related: 兜底链见 principle p09；IQUEUE NEXT 级与之交互见 f19
  tags: [concept, reselection, sequence]

- id: g18
  term: Blockage / Blockage mode
  category: concept
  source_pages: p50, p89
  source_quote: |
    "If no other direction (mutual aid, …) is available, as last resort, the call uses the ACR pilot blockage
    mode" (p50)
    "Routing Direction available and open? If not, the call goes to Blockage mode" (p89)
  definition: |
    封锁模式：重分发无可用方向、或脚本重试耗尽时的最终落点——封锁地址或语音引导。配 Redirection/
    Redistribution 兜底时应同步规划 Blockage 落点。
  alias_or_related: 与 Redirection Queue（转发到语音引导队列）不同——后者是主动兜底方向
  tags: [concept, blockage]

- id: g19
  term: IQUEUE / Parking Level
  category: concept
  source_pages: p249-252
  source_quote: |
    "Allows to overwrite the parking level management done in the routing rule • Up to 7 levels: Levels "1…6"
    • Level "Next"" (p249)
  definition: |
    IQUEUE 构件：在脚本内覆写等待房间的停放级体验——1-6 级每级可配语音引导（引导号/掐断/时长/重播）、
    预期等待时间表或地址；NEXT 级在重选重跑而上一停放选项未播完时接管。未指定的级回落路由规则配置。
  alias_or_related: 停放级的基础管理在路由规则（f08）；语音引导见 g31
  tags: [concept, iqueue, parking]

- id: g20
  term: ACR Actual Waiting
  category: concept
  source_pages: p234, p282
  source_quote: |
    "ACR Actual Waiting parameter: Allows to change the call selection mode • Location: "Applications / CCD /
    CCD/RSI system parameters"" (p234)
    "If the Parameter ACR Actual Waiting is set to TRUE, the highest real waiting time is used" (p282)
  definition: |
    RSI 系统参数：False（默认）=同优先级先比最低 ISM 成本再看最长实际等待；True=先最长实际等待再看
    成本。修改入口 mgr Applications/CCD/CCD/RSI system parameters。
  alias_or_related: 完整选呼次序见 principle p23
  tags: [concept, call-selection, parameter]

- id: g21
  term: LIST variable（skill 型 / agent 型）
  category: concept
  source_pages: p258-261
  source_quote: |
    "There are 16 automatic lists, indexed from 1 to 16 … The "agent" type list • The "skill" type list" (p258)
    "If both lists own the same agent, the resulting list owns the agent only one time • There is no maximum
    agent number in an agent typed list" (p260)
  definition: |
    脚本内 16 个 LIST[%1..16] 变量，类型由元素决定：skill 型（CHARACTERISTICS_LIST、CALL_PROFILE[x]
    可赋值，"+"同技能取高级别、超 7 技能截断）供 ISM 用；agent 型（Last_Called_Agent、AUTHORIZED_LIST[x]、
    (AGENT{号}) 可赋值，无上限）供授权/非授权名单规则用；"-"移除元素。
  alias_or_related: 截断策略见 principle f20 引文；典型用法 RULE_AUTHORIZED_LIST LIST[%x]
  tags: [concept, list-variable]

- id: g22
  term: Filter / Super-Filter / Hyper-Filter
  category: concept
  source_pages: p285-307
  source_quote: |
    "Filters are dedicated for ACR • To group the ACR calls with common characteristics … Up to 200 filters
    • 7 skills per filter max • The call distribution is not impacted by the filters" (p285)
    "Super-Filter: Group of Filters declared in the same node • Hyper-Filter: Group of Filters declared in
    different nodes • 25 objects per Super-Filter /Hyper-Filter" (p303)
  definition: |
    过滤器：按呼叫档案/授权名单/非授权名单给 ACR 呼叫分组（≤200 个、每个 ≤7 技能、AND 语义），只影
    响实时观测与统计、不影响分发；Super-Filter（同节点组）/Hyper-Filter（跨节点组）每组 25 对象、OR
    语义。
  alias_or_related: 报表模板见 g44
  tags: [concept, filter, monitoring]

- id: g23
  term: Debugger
  category: concept
  source_pages: p46, p59, p70, p78-80, p338
  source_quote: |
    "Test the script and control the script execution using the debugger tool" (p46)
    "Use the Debugger … Same function than the Internal ASM Server" (p338)
  definition: |
    脚本调试器（CCS 内）：连接 ASM 观察脚本逐构件执行、实时修改既有构件条件、发起测试呼叫；内部与
    外部 ASM 功能相同。约束：不能新增构件；整型值观察需 + %0 技巧。
  alias_or_related: 命令行对照 g36 adm_acd
  tags: [concept, debugger, maintenance]

# ── 二、角色 (role) ──

- id: g24
  term: Agent / Supervisor（ACD Station 类型）
  category: role
  source_pages: p31, p32
  source_quote: |
    "Set type Create the agent in 8068, 8068s or 8078s type • ACD station Select Agent … Select Supervisor" (p31)
    "Self-assignable agent Self-assignable agent means that the agent can log himself in any desired
    processing group. • Secret code expected Secret code needed for logon and logoff" (p32)
  definition: |
    CCD 侧两类坐席角色：Agent（接听呼叫）与 Supervisor（主管），在用户创建时以 ACD station 字段定型且
    不可改；坐席操作数据可配自助登录（任意处理组）与登录/注销密码。坐席话机限定 8068/8068s/8078s。
  alias_or_related: ACD 前缀动作码（呼主管/登录注销）见 principle p02
  tags: [role, agent, supervisor]

- id: g25
  term: Self-assignable agent
  category: role
  source_pages: p32
  source_quote: |
    "Self-assignable agent means that the agent can log himself in any desired processing group."
  definition: |
    自助登录坐席：无需管理员介入即可登录任意期望的处理组（配合 Secret code 鉴权）。实验矩阵中 3x500/
    3x501/3x502 均为自助可登录且免密码（实验口径）。
  alias_or_related: 配置入口 CCD Operations data management
  tags: [role, agent, logon]

# ── 三、订阅/许可 (subscription) ──

- id: g26
  term: Software License N°167 "ACR data base read"
  category: subscription
  source_pages: p320, p376, p394
  source_quote: |
    "If you need a connection to an External Database (MS SQL), a software license is needed in the PBX
    (Software License N° 167: "ACR data base read")" (p320)
    "option 61 (precise the lock ACR_SQL (167) availability)" (p394)
  definition: |
    本书中唯一的许可类条目（本书无订阅体系）：OXE 软件许可 N°167，脚本读/写外部数据库的前提；外部
    ASM 与 OXE 间连接本身免许可。运维经 adm_acd 选项 61 核该锁可用性。
  alias_or_related: OPS look "167 ACR data base read"（p376 用语）
  tags: [subscription, license, external-database]

# ── 四、产品/组件 (product) ──

- id: g27
  term: OmniTouch Contact Center Standard Edition (OTCC Standard Edition)
  category: product
  source_pages: p1, p5
  source_quote: |
    "OMNITOUCH CONTACT CENTER STANDARD EDITION ADVANCED CALL ROUTING - ISSUE 01 PARTICIPANT'S
    GUIDE" (p1)
    "With a "Classical" OTCC Standard Edition solution, this requirements implies: Several Agent groups (one
    agent per group) • Complex monitoring and statistics • One external application" (p5)
  definition: |
    本书宿主产品：ALE OmniTouch 呼叫中心标准版（OXE 上的 CCd/CCD 软件栈）。ACR 是其高级路由特性，
    用于替代传统"每坐席一组+外部应用"做法。
  alias_or_related: 底层 PBX 见 g28 OXE；套件名 OpenTouch Suite for MLE（p3，MLE 书中未展开）
  tags: [product, otcc, core]

- id: g28
  term: OXE (OmniPCX Enterprise)
  full_name: OmniPCX Enterprise（书中 p215/p320 完整拼写）
  category: product
  source_pages: p215, p320-322, p345
  source_quote: |
    "Alcatel-Lucent OmniPCX Enterprise • Flash card" (p215)
    "The internal ASM server on the PBX ("alb" process) has to be stopped" (p320)
  definition: |
    本书底层 PBX：承载 CCD/AFE/alb 进程与 parameters.cfg、语音引导闪存卡；多语言引导消息存其闪存卡。
    ACR 的内部 ASM 即其上的 alb 进程。
  alias_or_related: alb 见 g39；AFE 见 g30；MAO（p9 呼叫处理框，未展开）同域
  tags: [product, pbx]

- id: g29
  term: CCS / CCsupervisor (Contact Center Supervisor)
  category: product
  source_pages: p6, p35, p44, p56
  source_quote: |
    "An ACR script editor is embedded in the CCS" (p6)
    "CCSupervisor/Configurations/Advanced Call Routing/Skill" (p37)
    "Maintenance with Contact Center Supervisor (CCS) • Debugger" (p59)
  definition: |
    联系中心管理/监督工作站软件：内嵌 ASM 脚本编辑器与 Debugger，承载 ACR 逻辑配置树
    （Configurations/Advanced Call Routing 下的 Skill、ACR Data、ASM Script Editor、Filter、Super Objects、
    Agent、Statistics Pilot、Call Flow mgt）与 Real time/Statistics 观测窗口；也可建附件名单、改统计 Pilot。
    简写 CCs/CCsupervisor 混用。
  alias_or_related: 配置树全景见 framework f07
  tags: [product, management, ccs]

- id: g30
  term: AFE (Alcatel Front End) / MAIN_AFE
  category: product
  source_pages: p9, p49, p321-322, p345
  source_quote: |
    "Call Handling (MAO) — Alcatel Front End Server … Call handling request" (p9)
    "Restart MAIN_AFE dhs3_init -R MAIN_AFE" (p49)
    "so "AFE" will not start the "ALB" process of the OmniPCX Enterprise" (p322)
  definition: |
    OXE 上的前端服务器进程：接收呼叫处理请求并（内部 ASM 模式下）启动/管理 alb 进程。parameters.cfg
    的 asm_on_dhs=0 让 AFE 不再拉起 alb（外部 ASM 割接）；重启命令 dhs3_init -R MAIN_AFE。
  alias_or_related: alb 见 g39；MAO 为 p9 架构图中的呼叫处理框（书中未展开全称）
  tags: [product, afe, oxe]

- id: g31
  term: Voice Guide / Dynamic Voice Guide / Multi-Language Voice Guide
  category: product
  source_pages: p175-176, p215, p218, p224
  source_quote: |
    "Create the Recordable Voice Guides System / Dynamic Voice Guides /Assignment … Recordeable Voice
    Guides *88 • Tone Test *66 • Voice Guides assigned to the GD (2-0)" (p175, "Recordeable" 为原文拼写)
    "40 messages maximum per multi-language guide … Voice Guide Start up + YES • Backup Tone : 56" (p215, p218)
  definition: |
    语音引导三形态：普通引导（System/Voice Guides 建，录制后激活）、可录引导（Dynamic Voice Guides
    分配，*88 录音、*66 音调测试、指派 GD (2-0)——GD 书中未展开）、多语言引导（Function=Multi-language
    message，最多 40 语种映射消息 1000-1039，Backup Tone 56）。用途覆盖问候/等待/重定向/封锁/转发。
  alias_or_related: 语言判定链见 principle p22；IQUEUE 引导见 g19
  tags: [product, voice-guide]

- id: g32
  term: IAA (Automated Attendant)
  category: product
  source_pages: p169, p177-180, p211
  source_quote: |
    "Call tag using the IAA "Code entry guide" leaf" (p169)
    "Applications/Automated Attendant/Automated Attendant Leaves … Applications/Automated Attendant Tree
    … Applications/Automated Attendant Access" (p177-179)
  definition: |
    自动话务员（书中缩写 IAA，全称未展开）：叶（Leaf）-树（Tree）-接入（Access）三层结构；菜单叶做按键
    分流，Code Entry Guide 叶采集 ≤16 位客户代码作 Call Tag；接入号绑中继（Automated Attendant 属性
    YES）。只能外部呼入。
  alias_or_related: 叶类型与改配约束见 principle p46；Call Tag 见 g09
  tags: [product, iaa, ivr]

- id: g33
  term: CCivr
  category: product
  source_pages: p170, p255-256
  source_quote: |
    "Call tag using the CCivr … Example: "TransferCall" Building Block (BB)" (p170)
    "A CCivr resource group can be managed in the distribution of a waiting room • An "IVR rule" is necessary
    to distribute the call to this IVR processing group" (p255)
  definition: |
    交互式语音应答（IVR）服务器组件：经 CSTA 与 PCX 交互；其资源组可挂在等待房间的分发里，脚本用
    IVR 规则把呼叫送入；TransferCall 构件（前置 GetPilotInfo）可携 Correlator Data 转 Pilot；CCivr 侧用
    receivephonecall.callprofile 构件读取随呼叫传来的档案。
  alias_or_related: IVR 规则见 g13；CSTA 见 g45
  tags: [product, ivr, ccivr]

- id: g34
  term: ASM Script Editor / Building Block
  category: product
  source_pages: p44, p65, p69, p96, p376
  source_quote: |
    "CCSupervisor /Configurations/Advanced Call Routing/ASM Script Editor Create" (p44)
    "Select Graphic mode • Insert a Statement" (p65)
    "A specific "SQL" tab is available in the ASM script editor • 6 building blocks" (p376)
  definition: |
    脚本编辑器（CCS 内嵌）：Graphic（构件图）/Text（文本）双模式；构件（Building Block）包括 Statement
    （条件）、Variable、各规则构件、SET、IQUEUE、DISPLAY_AGENT、CLEAR AGENT LIST 等；SQL 页签另有
    外部库六构件。产物 *.scr（源）/ *.alb（编译后，见 g47）。
  alias_or_related: 生命周期见 framework f10；SQL 构件见 g43
  tags: [product, script-editor]

- id: g35
  term: External ASM Server / ASM Manager / ASMServer Tool
  category: product
  source_pages: p320-324, p327-330, p352
  source_quote: |
    "The External ASM is an external Server … The ASM service, seen as a Window service, must be started" (p320-321)
    ""Router" role: call routing requests will be handled by the ASM server … "Default" role: …" (p330)
    "Site Name: Site_1 • Main CPU: csm or Ip address … Connection role: ROUTER" (p352)
  definition: |
    外部 ASM 三件套：ASM Server（Windows 服务，装 Standalone/Duplicate 两种形态、Main/Stand-By 双角
    色）、ASM Manager（客户端工具：建 OXE 站点链接、看连接）、ASMServer Tool（装服务、改双机配置）。
    站点链接角色 Router（跑脚本）/Default（不跑但坐席可入列表）。
  alias_or_related: 部署结构见 framework f23；许可见 g26
  tags: [product, external-asm, windows-service]

- id: g36
  term: adm_acd
  category: product
  source_pages: p45, p60, p141, p276, p339, p343, p394
  source_quote: |
    "Maintenance command adm_acd -salb Option 28" (p45)
    "adm_acd IP@ of the ASM server –salb … option 24 node N°" (p60)
  definition: |
    OXE 维护命令（形态 adm_acd <ASM IP> -salb）：ACR 的命令行仪表盘——24 名单、25 内部库、28 呼叫动
    态数据（28 * 全量 dump，含 LAST_CALLED_AGENT）、11 Agent List Builder 链路、14 连接类型、60 外部库
    连接、61 ACR_SQL(167) 锁。
  alias_or_related: 配套命令 ps -edf | grep alb、dhs3_init、hybvisu（g37）
  tags: [product, maintenance, command]

- id: g37
  term: hybvisu / dhs3_init / ps -edf
  category: product
  source_pages: p35, p49, p264, p345
  source_quote: |
    "Telnet Enter the command "hybvisu -f all" … Main State The 2 access must be "up"" (p35)
    "Restart MAIN_AFE dhs3_init -R MAIN_AFE" (p49)
    "Check with "ps-edf |grep alb"" (p345, 原文两处拼写 ps -edf / ps-edf 混用)
  definition: |
    OXE 维护命令组：hybvisu -f all（混合链路状态，两 access 须 up）；dhs3_init -R MAIN_AFE（重启 AFE
    进程，parameters.cfg 变更后必做）；ps -edf | grep alb（找 alb 进程，用于核查内部 ASM 是否已停）。
  alias_or_related: alb 见 g39
  tags: [product, maintenance, command]

- id: g38
  term: parameters.cfg（asm_ag_free_duration / asm_on_dhs）
  category: product
  source_pages: p48-49, p241-242, p322, p345
  source_quote: |
    "The method is defined by a new parameter in the file parameters.cfg (version mini l2.300.32.a)
    asm_ag_free_duration • The line must be added by using a text editor" (p241)
    "you must disable the parameter "asm_on_dhs" in the "parameters.cfg" file" (p322)
  definition: |
    OXE 侧 ACR 参数文件（/usr3/afe/parameters.cfg，vi 手工编辑）：asm_ag_free_duration 定 Idle 排序语义
    （0=PLTR/1=LIT 单机/2=LIT 组网，最低版本 l2.300.32.a）；asm_on_dhs 置 0 用于外部 ASM 割接。改后
    必须重启 MAIN_AFE。
  alias_or_related: 语义详情见 principle p07；PLTR/LIT 见 g12
  tags: [product, parameters, configuration]

- id: g39
  term: alb process
  category: product
  source_pages: p45, p49, p320-321, p345
  source_quote: |
    "If needed, restart the ASM process to clean up the memory ps -edf |grep alb" (p45)
    "The internal ASM server on the PBX ("alb" process) has to be stopped" (p320)
  definition: |
    OXE 上的内部 ASM 服务器进程：解释脚本、维护名单/内部库/LCA 内存数据。外部 ASM 部署时必须停止
    （asm_on_dhs=0 + 重启 AFE，必要时 kill）。LCA 等动态数据默认只在其内存中——重启即失（外部库持久
    化可解，见 c18）。
  alias_or_related: 内存检查 adm_acd 28；持久化方案见 principle p41
  tags: [product, process, asm]

- id: g40
  term: External ASM（Stand-alone / Duplicated）
  category: product
  source_pages: p320-321, p335, p348, p361-362
  source_quote: |
    "The External ASM is an external Server … Its role is strictly identical to the "alb" process running on the
    OmniPCX … with some additional features such as requests toward external databases" (p320)
    "Select "Standalone system"" (p348) / "Select "Duplicate system"" (p365)
  definition: |
    部署于 Windows PC 的 ASM 服务器软件：角色与内部 alb 完全一致，外加外部数据库访问；安装形态
    Stand-alone（单机）或 Duplicate（双机 Stand-by）。脚本存安装目录 Script 子目录，迁移需复制 .scr 重
    编译。
  alias_or_related: 三件套见 g35；文件位置与迁移见 principle p34
  tags: [product, external-asm]

- id: g41
  term: ODBC / System DSN / ODBC Data Sources (32-bit)
  category: product
  source_pages: p379-380, p399-401, p429-433
  source_quote: |
    "Access to the Database trough an ODBC Driver • Start / Control Panel / Administrative Tools / ODBC Data
    Sources (32-bit) • Management of System DSN by adding a new data source" (p379)
    "The ASM Server is not able to make a connecting using a 64-Bit ODBC Driver" (p399)
  definition: |
    外部库接入通道：ASM 只支持 32 位 ODBC——在"ODBC Data Sources (32-bit)"管理工具里建 System DSN
    （Access 用 Microsoft Access *.mdb 驱动免凭据；SQL Server 驱动可带 Brest 类凭据），DSN 名与脚本
    USE_DATABASE 的源名一致（原文语法印作 DNS=）。
  alias_or_related: 硬边界见 principle p36；glossary 术语 "DNS=" 笔误见 counter-example n48
  tags: [product, odbc, dsn]

- id: g42
  term: MS Access（acr.accdb / Records 表）与 MS SQL Server 2016（acr_sql / Customer 表）
  category: product
  source_pages: p396-399, p409-415, p428
  source_quote: |
    "Create the MS Access database with Name: "acr.accdb" … Select "View" / "Design View" … Type the Table
    Name:"Records"" (p396-397)
    "Database Name: acr_sql … Enter a name for table: Customer" (p410, p414)
  definition: |
    两个实验数据库产品：Access 2016（库 acr.accdb，表 Records：ID/Name/First_Name/Calling/Agent/VIP，
    免凭据连接，须存 .mdb 以配 32 位驱动）；SQL Server 2016（库 acr_sql，表 Customer：Caller 主键/
    Last_Agent 默认 NoAgent/Name 默认 NoName/VIP 默认 0，SQL 认证登录 Brest）。编号/结构均为实验
    口径。
  alias_or_related: 账号与安全口径见 counter-example n43；存储过程见 g43
  tags: [product, database, lab]

- id: g43
  term: Stored Procedure（updateCalling / update_calling）
  category: product
  source_pages: p382, p421-426, p434, p438
  source_quote: |
    "CALL "update_calling" (IN CALLING, OUT INTEGER[%1]) … update_calling is the stored procedure name" (p382)
    "search for the file "SQL Call Procedure.txt" Drive D:\CCD_ACR\" (p423)
    "SQL_REQUEST DB[%1] CALL "updateCalling" (IN CALLING, IN LAST_CALLED_AGENT)" (p438)
  definition: |
    数据库存储过程：脚本经 SQL_REQUEST CALL 调用（IN/OUT 参数，目标库须支持嵌入式过程）。实验过程
    updateCalling（由 D:\CCD_ACR\SQL Call Procedure.txt 载入）把主叫号与上次接听坐席写入 Customer 表，
    实现 LCA 持久化；过程不维护 Name/VIP 默认值。
  alias_or_related: 持久化原则见 principle p41；SQL_RESULT 测试见 principle p37
  tags: [product, stored-procedure]

- id: g44
  term: Formfilter.xls / FormFilterS.xls / FormAgentPerFilter.xls
  category: product
  source_pages: p299-301
  source_quote: |
    "Filter: Detail Statistics (Formfilter.xls) … Filters: Summary of the statistics (FormFilterS.xls) … Agents
    per Filter (FormAgentPerFilter.xls)" (p299-301)
  definition: |
    ACR 统计 Excel 三模板：Formfilter.xls（按时间片明细，Statistics/Excel/Filter）、FormFilterS.xls（观察期
    汇总、每过滤器一行，Excel/Filters Summary）、FormAgentPerFilter.xls（坐席×过滤器活动，Excel/Agent
    per Filter）。Super/Hyper-Filter 亦可用 Excel 报表。
  alias_or_related: 过滤器见 g22；数据时效见 counter-example n28
  tags: [product, statistics, excel]

# ── 五、协议/技术 (protocol) ──

- id: g45
  term: CSTA
  category: protocol
  source_pages: p15, p169-170, p255
  source_quote: |
    "Call Tag • CSTA filed for call identification" (p15, "filed" 为原文笔误)
    "The code entry guide prompts the caller to dial a code (max code length = 16 digits) and send it to the
    CSTA application as "Correlator data"." (p169)
  definition: |
    计算机电话集成接口（书中未展开全称）：Call Tag 以 Correlator data 形态经 CSTA 在 IVR/IAA/CCivr 与
    PCX 间传递；CCivr 经 CSTA 读呼叫档案（receivephonecall.callprofile）。
  alias_or_related: Call Tag 见 g09
  tags: [protocol, csta]

- id: g46
  term: SQL（SELECT / CALL 存储过程 / WHERE 子句变量）
  category: protocol
  source_pages: p376, p382-384, p402
  source_quote: |
    ""Read" / "Write" SQL requests to databases are available using an ASM script" (p376)
    "The list of the expressions (list of the columns for example): SELECT exp1, exp2 • The name of the table
    which is selected: FROM table1, table2 • The parameters to select some lines: WHERE predicats" (p382)
  definition: |
    ASM 脚本里的受限 SQL：SELECT…FROM…WHERE 查询与 CALL 存储过程（IN/OUT）两种；WHERE 子句与
    过程 INPUT 可用 26 项呼叫上下文变量（CALLING/CALLTAG/CALLED/PRIORITY/SEQUENCE/PILOT_NUMBER/
    WAITING_ROOM_NUMBER/EXPECTED_WAITING_TIME/WAIT/AGENT_NUMBER/LAST_CALLED_AGENT/
    LAST_CALLED_PILOT/LAST_CALL_DATE/LAST_CALL_STATE 及带下标的变量与技能档案类）。
  alias_or_related: 变量全集见 principle p40；结果测试 SQL_RESULT 见 principle p37
  tags: [protocol, sql]

- id: g47
  term: *.scr / *.alb（脚本文件格式）
  category: protocol
  source_pages: p11, p335, p354-355
  source_quote: |
    "ASM compilation ASM Language … (*.scr files) (*.alb files)" (p11)
    "the "scr" file has to be copied and recompiled" (p335)
  definition: |
    脚本两种文件形态：.scr 为 ASM 语言源文件（编辑器产出、可在内部/外部 ASM 间复制后重新编译）；
    .alb 为编译后伪代码（ASM 服务器解释执行，跨环境不通用）。内部 ASM 存 OXE /usr3/afe，外部存安装
    目录 Script 子目录。
  alias_or_related: 迁移规则见 principle p34
  tags: [protocol, file-format, script]

- id: g48
  term: Hybrid Link (ABC-F)
  category: protocol
  source_pages: p33-35
  source_quote: |
    "Inter-Node Links/Logical Links (ABC-F) Create … Link Type Hybrid … Multi access hybrid link Set to
    YES. We need at least 2 accesses to make a loop" (p33-34)
  definition: |
    本地 CCD 呼叫所需的节点间逻辑链路（ABC-F 为 OXE 逻辑链路族名，书中未展开）：类型 Hybrid、邻接
    节点=本地节点号、邻接网络号 0-31 且异于本地、多访问 YES、至少 2 个 access 成对；hybvisu -f all 校验。
  alias_or_related: 校验命令见 g37
  tags: [protocol, hybrid-link, network]

- id: g49
  term: DTMF / Correlator data
  category: protocol
  source_pages: p169, p170, p177
  source_quote: |
    "DTMF Digit: 4 (1-16)" (p177)
    "Correlator Data • A value can be attached to the call • Customer number • Database Index • Context Id" (p170)
  definition: |
    双音多频（书中未展开全称）：IAA 菜单叶按键（DTMF 1/2…）与编码叶按键长度（1-16 位）的输入方式；
    编码与 CCivr 附着值统称 Correlator data（客户号/数据库索引/上下文 Id），即 Call Tag 的传输形态。
  alias_or_related: Call Tag 见 g09
  tags: [protocol, dtmf, correlator]

# ── 六、网站/资源/路径 (resource) ──

- id: g50
  term: /usr3/afe（OXE 侧目录）
  category: resource
  source_pages: p48, p241, p322, p335, p354
  source_quote: |
    "more /usr3/afe/parameters.cfg" (p48)
    "The "scr" and "alb" files are stored in the usr3/afe directory in case of Internal ASM server" (p335)
    "The scripts are located on the OXE in /usr3/afe directory" (p354)
  definition: |
    OXE 上 ACR 的家目录：parameters.cfg 参数文件、内部 ASM 的 .scr/.alb 脚本都在这里；外部化时经 FTP
    从此取脚本。telnet 进 OXE 后 cd /usr3/afe 操作。
  alias_or_related: 参数文件见 g38
  tags: [resource, path, oxe]

- id: g51
  term: Program Files/Alcatel/Agent Selection Module/Script（外部 ASM 脚本目录）
  category: resource
  source_pages: p335, p369, p373
  source_quote: |
    "(by default: Program Files/Alcatel/Agent Selection Module / Script)" (p335)
    "Check the Directory "C:\Program Files (x86)\Alcatel\Agent Selector Module\Script"" (p373)
  definition: |
    外部 ASM 服务器上的脚本存放目录（默认 Program Files\Alcatel\Agent Selection Module\Script；双机实验
    口径为 C:\Program Files (x86)\Alcatel\Agent Selector Module\Script）。主备双机的脚本自动同步到此目录，
    可作为同步核验点。
  alias_or_related: 双机同步见 c13
  tags: [resource, path, external-asm]

- id: g52
  term: D:\CCD_ACR\SQL Call Procedure.txt
  category: resource
  source_pages: p423
  source_quote: |
    "Select /File/Open /File … search for the file "SQL Call Procedure.txt" Drive D:\CCD_ACR\"
  definition: |
    实验环境提供的存储过程脚本文件（updateCalling 的 SQL 源码），经 SSMS File/Open 载入执行。仅此一
    处出现，属实验配套资源。
  alias_or_related: 过程功能见 g43
  tags: [resource, file, lab]

- id: g53
  term: ODBC Data Sources 管理入口（Start/Control Panel/Administrative Tools）
  category: resource
  source_pages: p379, p400, p429
  source_quote: |
    "Start / Control Panel / Administrative Tools / ODBC Data Sources (32-bit)" (p379)
    "Start /Administrative Tools/ODBC Data Sources (32-bit)" (p429)
  definition: |
    Windows 管理工具入口：建 System DSN 的固定路径（务必用 32 位版本）。Access 与 SQL Server 两章共
    用此入口。
  alias_or_related: 32 位约束见 counter-example n36
  tags: [resource, windows, odbc]

- id: g54
  term: SOFTPANEL / SoftPanel2（实验主机名）
  category: resource
  source_pages: p428, p362
  source_quote: |
    "Server Name: SOFTPANEL" (p428)
    "host name: SoftPanel … host name SoftPanel2" (p362)
  definition: |
    实验环境主机名：SOFTPANEL 为 SQL Server 所在主机（SSMS 连接名）；SoftPanel（10.2.T.20，Main）与
    SoftPanel2（10.2.T.21，Stand-By）为外部 ASM 双机主机名（T=组内表号）。均为实验口径。
  alias_or_related: 双机角色配置见 c13
  tags: [resource, lab, hostname]

- id: g55
  term: CCD09001-CCD09013 文档编号体系
  category: resource
  source_pages: p19, p42, p62, p92, p118, p142, p174, p197, p222, p263, p308, p344, p361, p395, p408, p416, p421, p427, p453, p466
  source_quote: |
    "Basic CCD matrix creation CCD09001CB01CGEN.docx" (p22)
    "Manage a script CCD09001CB02CGEN.docx" (p43)
    "External Database CCD09012CB02CGEN.docx" (p428)
  definition: |
    原书 How-To 章的底层文档编号（页眉可见）：CCD09001CB01/02（矩阵/脚本）、CCD09002（名单规则）、
    CCD09003（重定向/再分发）、CCD09004（直拨）、CCD09005（内部库）、CCD09006（Call Tag）、CCD09007
    （字符串）、CCD09008（多语言）、CCD09009（综合）、CCD09010（过滤器）、CCD09011CB01/02（外部 ASM
    单机/双机）、CCD09012CB01/02（Access/SQL 实验）、CCD09013CB01-05（SQL 建库/账号/过程/安装/
    Profiler）。同一课程模块在不同发布物中可按此编号追溯。
  alias_or_related: 页码映射见 case.md 各条 source_chapter
  tags: [resource, document-id]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列候选术语逐条核对

OVERVIEW 术语表实际 **15 行**，逐条核对如下——

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| ACR (Advanced Call Routing) | 正文有明确定义（p6） | g01 |
| ASM (Agent Selection Modul) | 有明确定义（p6/p10） | g02 |
| ACR Pilot | 有明确定义（p6/p13） | g03 |
| Waiting Room | 有明确定义（p12） | g05 |
| Dynamic Group | 有明确定义（p12/p14） | g06 |
| 9 种 ACR 规则 | 有明确定义（p7-8/p244） | g13 |
| Call Profile | 有明确定义（p15/p39） | g07 |
| Call Tag | 有明确定义（p15/p168-169） | g09 |
| CHARACTERISTICS_LIST | 有定义性用法（p18/p259） | g08 |
| DICA | 有明确定义（p111） | g14 |
| asm_ag_free_duration | 有明确定义（p48-49/p241-242） | g38（PLTR/LIT 为 g12） |
| ISM 成本 | 有明确定义（p235） | g11 |
| ACR Actual Waiting | 有明确定义（p234/p282） | g20 |
| adm_acd | 有定义性用法（p45/p60/p141 等） | g36 |
| SQL 六构件 | 有明确定义（p376/p390） | g43/g46/g41（拆分覆盖） |

结论：15 行全部有正文依据，无"仅 passing 提及需排除"项。

### 2. 本次新增、OVERVIEW 未列的术语

概念：Statistic Pilot（g04）、Characteristics List（g08）、Skill/Domain/Weight（g10）、PLTR/LIT（g12）、Direct Call 族（g14/g15）、Internal Database（g16）、Reselection/SEQUENCE（g17）、Blockage（g18）、IQUEUE（g19）、LIST 变量（g21）、Filter 族（g22）、Debugger（g23）；
角色：Agent/Supervisor（g24）、Self-assignable agent（g25）；
产品：OTCC Standard Edition（g27）、OXE（g28）、CCS/CCsupervisor（g29）、AFE/MAIN_AFE（g30）、Voice Guide 族（g31）、IAA（g32）、CCivr（g33）、ASM Script Editor（g34）、External ASM 三件套（g35）、hybvisu/dhs3_init/ps（g37）、parameters.cfg（g38）、alb（g39）、External ASM 形态（g40）、ODBC/System DSN（g41）、Access/SQL 实验库（g42）、存储过程（g43）、Excel 三模板（g44）；
协议/技术：CSTA（g45）、SQL 受限集（g46）、*.scr/*.alb（g47）、Hybrid Link ABC-F（g48）、DTMF/Correlator data（g49）；
资源/路径：/usr3/afe（g50）、外部 ASM 脚本目录（g51）、SQL Call Procedure.txt（g52）、ODBC 管理入口（g53）、SOFTPANEL/SoftPanel2（g54）、CCD 文档编号体系（g55）。

### 3. 仅 passing 提及、未单列条目的词（附于相关条目或如实省略）

- MAO（p9 架构图呼叫处理框，未展开，附于 g30）；GD (2-0)（p175 语音引导指派目标，未展开，附于 g31）；
- MLE（OpenTouch Suite for MLE，p3 起反复出现，全书未展开全称，附于 g27）；
- RSI（CCD/RSI system parameters，p150/p234/p282，参数界面名，未展开，附于 g20）；
- csm（p352 Main CPU 取值"csm or IP"，未展开，附于 g35）；
- "Speed dialing"（缩位拨号，p85 通用电话术语，附于 principle p13）；
- **empty subscription 说明**：本书无订阅/资费体系，subscription 类仅 g26 软件许可一条，为忠实原书不虚构。

### 4. 提取口径说明

- 所有定义只采信本书正文；IAA/MAO/MLE/RSI/CSTA/DTMF/csm/GD 等缩写书中未给全称的，full_name 一律省略或标注"未展开"，不做外部补全；ASM 全称照录原书拼写 "Agent Selection Modul"；LIT 双表述（Logon Idle Time p240 / Longest Idle Time p242）照录。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准；引用均为原文摘录，原文笔误（"all tag"、"CSTA filed"、"Recordeable"、"ps-edf"、"DNS="、"Unaurthorized"、"UnKown" 等）照录并在括号内注明。
