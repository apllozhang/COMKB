# 框架/流程/结构候选 — OmniTouch CC Standard · Advanced Call Routing (OTCCXTE150EN Issue 01)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、脚本语言结构。实验环境给定值（对象编号 3xXXX、账号、路径）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——概念地基 → 公共实验矩阵 → 脚本工具链 → 规则族/特征源 → 综合 → 统计 → 外部化
  type: flow
  source_pages: p3-470
  source_chapter: 全书章节编排（ACR Introduction → 12 个讲义课程章 + 20 个 How-To 实验章交替）
  source_quote: |
    "The ACR feature is based on script • An ACR script editor is embedded in the CCS and allows you to
    create ACR scripts with ACR rules like (Rule ISM, Rule LCA, …)" (p6)
  summary: |
    全书按十二段推进：①ACR 引论（p3-18：痛点、9 规则、ASM 架构、分发原理、呼叫特征、容量上限）；
    ②基础 CCD 矩阵 How-To（p19-41，后续一切实验的公共地基）；③脚本管理 How-To（p42-50）；④授权/
    非授权名单（讲义 p51-61 + How-To p62-81）；⑤重定向/再分发（p82-91 + p92-102）；⑥直拨与 ACR
    （p103-117 + p118-127）；⑦内部数据库（p128-141 + p142-164）；⑧Call Tag 生成与传递（p165-173 +
    p174-189）；⑨字符串处理（p190-196 + p197-211）；⑩多语言语音引导（p212-221 + p222-229）；⑪综合
    特性（p230-262 + p263-282）+ 过滤器统计（p283-307 + p308-317）；⑫外部化三线：外部 ASM（p318-343
    + p344-360）、双机热备（p361-373）、外部数据库（p374-394 + Access 实验 p395-407 + SQL 准备四 How-To
    p408-426/p453-469 + SQL 实验 p427-452）。这是"先矩阵后脚本、先单机后外部"的教学主线，也是实际
    交付项目的推荐顺序。
  conditions: 无特殊版本前提；每个 How-To 都默认基础矩阵（f06）已建成
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: ASM 架构全景——脚本编辑器/管理器/服务器/数据库四方与呼叫处理链
  type: diagram
  source_pages: p9-11
  source_chapter: ACR Introduction / Agent Selection Modul principle (ASM)
  source_quote: |
    "Call Handling (MAO) — Alcatel Front End Server — Call handling request → ASM Server … Script Editor
    (ASM Client) / ASM manager (ASM Client) … Data base Internal and / or External" (p9)
    "The ASM script editor is in charge of writing and loading of a script … The ASM server is in charge of
    Script interpretation • Data base queries • Update of data base • Calculation of the agent list according
    to Agents configuration • Script rules • Call profile" (p10)
  summary: |
    架构四方：①脚本编辑器与 ASM 管理器（均为 ASM Client，编辑器内嵌在 CCS）负责写脚本、装载与激活；
    ②ASM 服务器负责解释脚本、查询/更新数据库、按坐席配置+脚本规则+呼叫档案计算坐席列表；③数据库
    内部与/或外部；④呼叫侧由呼叫处理（MAO）与 Alcatel Front End Server（AFE）发出 call handling request。
    脚本形态：ASM 语言源文件 *.scr，编译后伪代码 *.alb（Unix/Windows 解释执行，p11）。呼叫进 ACR Pilot
    → ASM 执行 → 返回按规则排序的坐席列表（动态组）。
  conditions: ASM 可驻留 OXE（内部 alb 进程）或 Windows PC（外部服务，见 f23）
  tags: [diagram, architecture, asm, afe, script]

- id: f03
  title: 呼叫分发三步流程与动态组——特征化 → ASM 算列表 → 带列表进 Waiting Room
  type: flow
  source_pages: p12-14
  source_chapter: ACR Introduction / Distribution principles
  source_quote: |
    "1 Characterization of the call and association of a profile to the call, distribution of the call towards
    a pilot 2 Drawing up of a list of agents suitable to process the call according to the rule of the selection
    of the agent 3 Recovering of the list of agents transmitted by the ASM unit and call distribution to the
    agents" (p12)
    "Waiting Rooms are needed in ACR & don't work in FIFO mode" (p12)
  summary: |
    三步主流程：①呼叫被特征化（CLID/标签/档案）并分发到一个 Pilot；②ASM 按坐席选择规则拟出适合处理
    该呼叫的坐席列表；③CCD 取回该列表并把呼叫分发给其中坐席。ISMF 示例（p14）五步：档案赋予呼叫 →
    呼叫路由向 ACR Pilot → ASM 按算法搜技能坐席 → ASM 返回列表（即动态组）→ 呼叫带列表进入 Waiting
    Room。配套结构约束：ACR Pilot 同时可挂普通 Waiting Queue 与 Waiting Room，但 Waiting Room 与
    Waiting Queue 不能同开（p13）；ACR 呼叫没有资源选择优先级——选人完全由 ASM 接管（p13、p233）。
  conditions: ACR Pilot 必须连一个 Waiting Room 才能把 ASM 列表用起来
  tags: [flow, distribution, dynamic-group, waiting-room]

- id: f04
  title: 9 种 ACR 规则分类学——单用规则 vs 可组合规则，IDLE/COM 互斥
  type: structure
  source_pages: p7-8, p244-248
  source_chapter: ACR Introduction / 9 different ACR Rules & Miscellaneous / Rule combination
  source_quote: |
    "Individual Skill Mapping Rule (ISM) Select the best agent … Last Called Agent Rule (LCA) Select the agent
    who last answered the call • Authorized list Rule / Unauthorized list Rule … Redirection Rule …
    Redistribution Rule … Idle Rule Sort the agent list by the total Idle time since logon • Com Rule … IVR
    (Inter Active Voice response) Rule" (p7-8)
    "Single ACR Rules Have to be used alone in the APPLY instruction: LAST CALLED AGENT, REDIRECTION,
    REDISTRIBUTION, IVR • Combinable Rules: AUTHORIZED LIST, UNAUTHORIZED LIST, ISM, IDLE, COM •
    Rule „IDLE" & Rule „COM" are exclusive Cannot be combined together" (p244)
  summary: |
    规则全景：ISM（按技能档案选最优坐席）、LCA（选上次接听者）、Authorized/Unauthorized List（静态名单
    圈定/排除）、Redirection（转发到目的地）、Redistribution（退回 CCD 矩阵下一可用队列）、Idle（按登录后
    总空闲排序）、Com（按登录后处理呼叫数排序）、IVR（路由到 IVR 资源处理组）。组合语法：单用规则必须
    独占一个 APPLY；可组合规则可串接且可与单用规则配合；IDLE 与 COM 互斥。多个 APPLY 的语义差异见
    p25（principle 条目）。
  conditions: 规则只能写在 ASM 脚本里，脚本激活于 ACR Pilot
  tags: [structure, rules, taxonomy, script]

- id: f05
  title: 呼叫特征清单——路由的五种原料与内部数据库四属性
  type: structure
  source_pages: p15-17, p130-131
  source_chapter: ACR Introduction / Call characterization & Internal Database
  source_quote: |
    "CLID: Caller Line Number / Calling Number • NDI: Called Line Number (for Direct ACD Call) • Call Tag
    CSTA filed for call identification • Call Profile (List of attributes) ACR Call Profile, Required skills to
    handle the call (up to 7) • Type of Call Direct Call, Audio, Fax, e-mail, …" (p15)
    "Caller Identification: Calling Number • Call Tag • Agent Number (in case of Direct Call) … Associated
    Information: Name • Call Profile • Authorized List • Unauthorized List • Call Priority (Call Selection
    Priority)" (p131)
  summary: |
    脚本执行期可用的呼叫信息：CLID（主叫号）、NDI（直拨 ACD 呼叫的被叫号）、Call Tag（CSTA 标识字段）、
    Call Profile（≤7 项技能需求）、呼叫类型（Direct Call/Audio/Fax/e-mail…）。内部数据库以三键
    （主叫号/Call Tag/直拨坐席号）索引四个关联属性（名字、呼叫档案、授权/非授权名单、呼叫优先级），
    脚本通过 ASM 内部库函数按键取用（p17 伪代码示例：CALL FROM PILOT / IF QUEUE GT 30 AND TIME /
    THEN GOTO LAB1 …）。
  conditions: 呼叫档案最多 7 技能（p18 容量表对应）
  tags: [structure, call-characterization, call-tag, internal-database]

- id: f06
  title: 公共实验矩阵对象模型——双 Pilot + 队列/房间 + 统计 Pilot + 坐席组的拓扑
  type: diagram
  source_pages: p21-22, p24-25
  source_chapter: How-To Basic CCD matrix creation / Implementation & steps 2-5
  source_quote: |
    "For the "standard matrix": Create one "normal" Pilot: 3x600 • Create one normal Waiting Queue: 3x999700
    • Create on Agent Processing Group: 3x999800 - For the ACR part: Create one ACR Pilot: 3x603 - Create
    2 Statistic Pilots: 3X650 (Car insurance) & 3X651 (Home insurance) - The Statistics Pilots will be connected
    to the routing Pilot 3X603 - Create on Waiting Room: 3x999703 - Connect the Waiting Room to the Agent
    Processing Group 3x999800" (p22, 实验口径)
  summary: |
    实验矩阵（全部编号为实验口径，3x 的 x 为讲师给定位数）：普通链路——Pilot 3x600 → Waiting Queue
    3x999700 → Agent PG 3x999800；ACR 链路——ACR Pilot 3x603 → Waiting Room 3x999703 → Agent PG
    3x999800；入口分流——两个统计 Pilot 3x650（车险，Call Profile 1: English+Car）与 3x651（家险，
    Call Profile 2: English+Home）都汇入 ACR Pilot 3x603。坐席侧：Superuser 3x500、坐席话机 3x501/3x502
    （挂 agent PG；原文备注写 "3X800" 疑为 3X999800 笔误）、坐席 31501（English 9 / Car 9）、31502
    （English 9 / Home 9）。后续实验都在此矩阵上增量加对象（如直拨 Pilot 31604、重定向队列 31999702、
    IAA 31900、统计 Pilot 31652/31653）。
  conditions: 实验口径；矩阵图在 p21（Implementation 附图）
  tags: [diagram, lab-matrix, ccd, topology, lab]

- id: f07
  title: CCD/ACR 配置菜单路径双树——OMF 侧 Applications/CCD 与 CCS 侧 Configurations
  type: menu-path
  source_pages: p23-41, p56, p63, p74, p92, p144, p176, p198, p266, p309, p344
  source_chapter: 各 How-To 章菜单路径汇总
  source_quote: |
    "Applications/CCD/Processing group … Applications/CCD/Queue … Applications/CCD/Pilot …
    Application/CCD/Pilot/Pilot Rule Guide … Application/CCD/Distribution Rule … Applications/CCD/Statistic
    Pilot … Applications/CCD/CCD Users/CCD Operations data management" (p23-36)
    "CCSupervisor/Configurations/Advanced Call Routing/Skill … /ACR Data … /ASM Script Editor …
    CCSupervisor /Configurations/Agent … CCSupervisor /Configurations/ Statistics Pilot …
    CCSupervisor /Configurations/ Call Flow mgt/ Call Distribution" (p37-41, p281)
  summary: |
    两棵配置树分工：OMF 树（Applications/CCD/...）建矩阵对象——Processing group、Queue、Pilot、
    Pilot Rule Guide、Pilot Rule Direction、Distribution Rule（含 Resource selection / Call selection
    configuration）、Statistic Pilot、CCD Users/CCD Operations data management（坐席操作数据与附件名单）；
    Users 树建话机/坐席/主管。CCS 树（CCSupervisor/Configurations/...）建 ACR 逻辑——Advanced Call
    Routing 下的 Skill（域与技能）、ACR Data（呼叫档案、授权/非授权名单、Calling Number/Call Tag/坐席号
    数据库条目）、ASM Script Editor（脚本与 Debugger）、Filter（过滤器）、Agent（坐席技能）、Statistics
    Pilot（档案指派）；另有 Configurations/Super Objects（Super/Hyper-Filter）、Call Flow mgt/Call
    Distribution（呼叫选择优先级）、Real time / Statistics 两组观测窗口。
  conditions: 附件名单（List of Attachments）也可经 CCSupervisor 建（p33）；技能域也可由 mgr 或 OmniVista 8770 管（p37）
  tags: [menu-path, omf, ccsupervisor, configuration-tree]

- id: f08
  title: 路由规则/分发规则配置结构——Pilot Rule Guide → Rule Direction → Distribution Rule → 两级 selection
  type: structure
  source_pages: p26-29
  source_chapter: How-To Basic CCD matrix creation / steps 5-8
  source_quote: |
    "Rule Number It is possible to declare up to 30 rules per pilot … Priority The priority value is from 0 to 9.
    0 being the highest priority. Direction open (norm) It is possible to open or close a direction to a queue."
    (p26)
    "Rule Number It is possible to create up to 10 rules. Active Rule Activate the first Distribution Rule" (p27)
  summary: |
    四层结构：①Pilot Rule Guide——每 Pilot 最多 30 条路由规则（Rule Number 0-29），规则名会显示在 CCS；
    ②Pilot Rule Direction——每条规则内定优先级（0-9，0 最高）与方向开关（开/关到某队列）；③当前生效规则
    由 Pilot 的 Current Pilot Rule Number 指定（p26 下部），另有两种激活途径：CCS Rule Window 的 Apply
    按钮或 CCS 日历；④Distribution Rule——最多 10 条，含 Resource selection configuration（资源选择优先级
    0-9 + 队列→处理组方向开关）与 Call selection configuration（呼叫选择优先级 0-9 + 方向开关）。
  conditions: Waiting Room 与 Waiting Queue 不能在同一条路由规则里同时开（p13/p232）
  tags: [structure, pilot-rule, distribution-rule, priority]

- id: f09
  title: 混合链路（Hybrid Link ABC-F）结构与 hybvisu 校验
  type: flow
  source_pages: p33-35
  source_chapter: How-To Basic CCD matrix creation / step 13
  source_quote: |
    "Inter-Node Links/Logical Links (ABC-F) Create … Link Type Hybrid • Adjacent Node Enter the local node
    number • Adjacent Network Enter a different network number (different from the local network). Value from
    0 to 31 • Multi access hybrid link Set to YES. We need at least 2 accesses to make a loop" (p33-34)
    "Check the hybrid Link Telnet Enter the command "hybvisu -f all" … Main State The 2 access must be "up""
    (p35)
  summary: |
    本地 CCD 呼叫要建混合链路：Inter-Node Links/Logical Links (ABC-F) 下建 Link（类型 Hybrid，邻接节点=
    本地节点号，邻接网络号取 0-31 且须异于本地网络号，多访问混合链路=YES——至少 2 个 access 才能成
    环）；再在 Hybrid Link Access 下建 access 1 与 access 2（或 3 与 4，成对）。校验：telnet 上执行
    hybvisu -f all，两个 access 的 Main State 均须为 "up"。
  conditions: ACR 需要该链路支撑本地 CCD 呼叫；多节点组网细节在书外
  tags: [flow, hybrid-link, abc-f, hybvisu, maintenance]

- id: f10
  title: 脚本生命周期闭环——编写 → 保存传输 → Pilot 激活 → Debugger 验证 → 内存/运行检查
  type: flow
  source_pages: p44-46, p59-60, p70, p78-80
  source_chapter: How-To Manage a script & Authorized/Unauthorized Rule
  source_quote: |
    "Save the script and transfer it to the ASM. Don't forget to activate the script on the ACR Pilot" (p44)
    "Test the script and control the script execution using the debugger tool … CCSupervisor
    /Configurations/Advanced Call Routing/ASM Script Editor — ASM connection" (p46)
  summary: |
    五环闭环：①编辑器（CCS 内嵌 ASM Script Editor，Graphic/Text 双模式，构件 Building Block 拼装）写脚本
    并保存；②传输到 ASM 服务器（脚本存 OXE /usr3/afe 或外部 ASM 安装目录，见 f23）；③在 ACR Pilot 上
    激活脚本（一个 Pilot 同时仅 1 个脚本）；④Debugger 验证——连接 ASM、观察执行轨迹、可选改既有构件的
    条件参数实时复测、甚至可直接从 Debugger 发起呼叫（p127 Tips）；⑤运维检查——adm_acd -salb 看内存
    与运行数据（选项 28 dump 呼叫动态数据），必要时重启 ASM 进程清内存（ps -edf | grep alb 找进程）。
  conditions: 脚本名最长 8 字符；编辑器只能改既有构件不能在 Debugger 里新增构件
  tags: [flow, script-lifecycle, debugger, activation]

- id: f11
  title: parameters.cfg 参数文件机制——asm_ag_free_duration 与 asm_on_dhs 两个开关
  type: structure
  source_pages: p48-49, p241-242, p322
  source_chapter: How-To Manage a script & Miscellaneous lesson & External ASM lesson
  source_quote: |
    "The method is defined by a new parameter in the file parameters.cfg (version mini l2.300.32.a)
    asm_ag_free_duration • The line must be added by using a text editor" (p241)
    "you must disable the parameter "asm_on_dhs" in the "parameters.cfg" file … (oxe_prompt) > cd /usr3/afe
    more parameters.cfg … Restart "AFE" process dhs3_init –R MAIN_AFE" (p322)
  summary: |
    OXE 侧 /usr3/afe/parameters.cfg 是 ACR 行为的隐藏开关板：asm_ag_free_duration 控制 Idle 规则排序
    语义（0=PLTR 默认 / 1=LIT 单机 / 2=LIT 组网，改后须重启 MAIN_AFE：dhs3_init -R MAIN_AFE）；
    asm_on_dhs=0 用于割接到外部 ASM（让 AFE 不再启动内部 alb 进程）。参数行须用文本编辑器（vi）手工
    添加/修改，ESC :wq 保存。
  conditions: 最低软件版本 l2.300.32.a；值 1 对应旧 patchIdle 文件行为（该文件已废弃）
  tags: [structure, parameters-cfg, lit, pltr, asm-on-dhs]

- id: f12
  title: 授权/非授权名单的五种给值方式与维护入口
  type: structure
  source_pages: p53-58, p60
  source_chapter: Authorized List / Unauthorized List lesson
  source_quote: |
    "AUTHORIZED_LIST: Brings up agents out of a static list. It can be indexed by: A call context index
    (CALLING, CALLTAG, AGENT_NUMBER) • An integer (its logical number in OmniTouch, %index to define) • Its
    name (its name in OmniTouch, "String to define") • Agents list: Brings up an explicit agents list …
    LIST variable: Bring ups agents found in the variable LIST" (p57)
  summary: |
    名单规则给值五式：①呼叫上下文索引（CALLING / CALLTAG / AGENT_NUMBER——名单跟着主叫号、标签
    或被拨坐席号走）；②整数索引 %index（名单的 ID 0-99）；③名字索引 "String"（注意大小写敏感）；
    ④脚本内显式坐席列表（如 RULE_AUTHORISED_LIST 31500 31501，无数量上限）；⑤LIST 变量（动态拼装，
    见 f20）。名单本体在 CCS Configurations/Advanced Call Routing/ACR Data 建（默认名 WList_x/BList_x）；
    运维用 adm_acd -salb 选项 24（节点号[名单号]）查看名单内容。
  conditions: 每列表最多 30 坐席、共 100 列表；脚本内显式列表不受此限；名单内坐席须有 ≥1 活动技能
  tags: [structure, authorized-list, unauthorized-list, indexing]

- id: f13
  title: 空列表兜底结构——Redirection 转发地址形态与 Redistribution 退回链
  type: structure
  source_pages: p84-90
  source_chapter: Redirection Rule / Redistribution Rule lessons
  source_quote: |
    "Redirection address can be: A static phone number Internal forward (on-pcx) • External forward Through a
    speed dialing number • Through a network N° • A dynamic phone number Stored in a STRING variable Retrieved
    from a database…" (p85)
    "If "AGENT_LIST" is NULL or if the list is not empty, but all agents are logged off or unavailable, then the
    REDISTRIBUTION Rule will be applied" (p90)
  summary: |
    两条兜底路径：Redirection——ASM 返回一个转发号（静态：内部分机 / 经缩位拨号或网络号出外部；动态：
    STRING 变量承载、可取自数据库），脚本写法 RULE_REDIRECTION 31010；Redistribution——把呼叫退回
    CCD 矩阵的下一路由方向，若方向不可用/未开则呼叫进 Blockage 模式（封锁地址或语音引导），配合
    "重定向队列接 Voice Guide 处理组"的矩阵扩展（p99 实验口径：队列 31999702 → PG 类型 Voice Guide
    31999802 → 引导 710）。触发条件：列表为空，或列表非空但坐席全部注销/不可用。
  conditions: Redirection 属单用规则；Redistribution 亦然——各需独占 APPLY
  tags: [structure, redirection, redistribution, blockage, fallback]

- id: f14
  title: 坐席直拨与 ACR 融合结构——Pilot Direct Call / 私有号码 / DICA 技能 / CALL_TYPE
  type: structure
  source_pages: p105-115
  source_chapter: Direct Calls & ACR lesson
  source_quote: |
    "Creation or modification of a pilot (called "Pilot direct call") … Complete the "Pilot direct call"
    parameter at the agent processing group level … Complete the Private agent number parameter in the agent
    data … Management of this parameter conditions the type of call : CCd or private" (p106)
    "When a private number is managed for one Agent, the system automatically assigns a new skill for this
    Agent • Domain: Media • Skill: DirectCall • Abbreviation: DICA" (p111)
  summary: |
    四件套：①处理组级参数 Pilot Direct Call 填 ACR Pilot 号（直拨呼叫即 ACD 化，忙时溢出到该 Pilot）；
    ②坐席数据里配 Private Agent No.（私有号），该参数的存在与否决定呼叫类型判定（未管理=仅矩阵内呼叫
    是 CCd；私有号=CCd 号=全部外部来电皆 CCd；两号不同=各归各类）；③系统自动给坐席挂 DICA 技能
    （Domain Media/Skill DirectCall），DICA 停用则完全无法直拨该坐席（立即转 pilot direct call）；
    ④脚本用关键字 CALL_TYPE=DIRECT_CALL 识别直拨，与 SEQUENCE 配合实现"第 1 次执行等 N 秒原坐席、
    第 2 次执行转走"。
  conditions: 直拨打到 ACR Pilot 的行为与普通 Pilot 不同（p120）；一个 ACR Pilot 同时仅 1 个脚本（p113）
  tags: [structure, direct-call, dica, call-type, private-number]

- id: f15
  title: 内部数据库结构——三键 × 五属性 × 4000 条与脚本取用语法
  type: structure
  source_pages: p130-141
  source_chapter: Internal Database lesson
  source_quote: |
    "Note: 4000 entries (single value or range) can be created in the Internal Database" (p131)
    "RULE_ISM CALL_PROFILE [CALLING] … IF (CALLTAG>="1000") AND (CALLTAG<="1999") RULE_AUTHORIZED_LIST
    AUTHORIZED_LIST [CALLTAG]" (p133, p135)
  summary: |
    结构：键为主叫号（完整号或通配号、单值或区段）、Call Tag、坐席号（仅直拨场景）；值为名字、呼叫档案、
    授权/非授权名单、呼叫优先级（Call Selection Priority）。配置入口 CCS Configurations/Advanced Call
    Routing/ACR Data。脚本取用语法：CALL_PROFILE[CALLING] / CALL_PROFILE[CALLTAG] /
    CALL_PROFILE[AGENT_NUMBER] 取档案；CALL_PRIORITY[...] 取优先级；AUTHORIZED_LIST[CALLTAG] 取
    名单。直拨场景要求已配 Pilot Direct Call + 私有号。运维：adm_acd -salb 选项 25（节点号 [对象 ID]）。
  conditions: 数据在 CCS/CCSupervisor 侧维护；使用坐席号键的前提是直拨特性已配（p137）
  tags: [structure, internal-database, calling, calltag, agent-number]

- id: f16
  title: Call Tag 三生成途径——统计 Pilot / IAA 编码叶 / CCivr 构件
  type: structure
  source_pages: p167-171
  source_chapter: Call Profile or Call Tag / Transfer lesson
  source_quote: |
    "all tag is a character string associated with a call transiting through this statistical pilot and operated
    by ACR distribution mechanisms" (p168, 首词 "all" 为原文笔误)
    "The code entry guide prompts the caller to dial a code (max code length = 16 digits) and send it to the
    CSTA application as "Correlator data"." (p169)
    "Some building blocks can be used to send a call tag, through CSTA, from the Interactive Voice Response
    Server to the PCX. Example: "TransferCall" Building Block (BB)" (p170)
  summary: |
    三途径：①统计 Pilot 静态标 Call Tag（0-32 字符，Applications/CCD/Statistic Pilot 或 CCS 配置）；
    ②IAA（自动话务员）Code Entry Guide 叶——提示caller 拨 ≤16 位代码，经 CSTA 以 Correlator data 送出，
    可屏显在坐席话机并供 CTI 使用；③CCivr 的 TransferCall 构件（盲转前需先执行 GetPilotInfo 构件）携带
    Correlator Data（客户号/数据库索引/上下文 Id）。转移语义：呼叫上下文中最后一个 Call Tag/Call Profile
    覆盖之前值（p172-173）。
  conditions: IAA 只能从外部呼入（p211）
  tags: [structure, call-tag, iaa, ccivr, correlator]

- id: f17
  title: IAA（自动话务员）三件套配置结构——Leaf / Tree / Access + 中继激活
  type: menu-path
  source_pages: p177-180, p198-199
  source_chapter: How-To Call Profile or Call Tag / Transfer & String handling
  source_quote: |
    "Applications/Automated Attendant/Automated Attendant Leaves Create … Leaf Type Code Entry Guide …
    DTMF Digit: 4 (1-16) • Action Type + Code Entry • Directory No. : 31603" (p177)
    "Applications/Automated Attendant Tree Create … Applications/Automated Attendant Access Create …
    Directory Number 31900 • Access ID 1 … Trunk Groups/Trunk Group Review/Modify — Automated Attendant
    YES" (p179-180)
  summary: |
    四步结构：①Leaf（叶）——类型 Menu For Auto. Attendant（菜单叶：DTMF 1→路由到预配号/DTMF 2→其他叶）
    或 Code Entry Guide（编码叶：提示音、DTMF 位数 1-16、Action Type +Code Entry → 目的地号）；②Tree
    （树）——树名 + 首叶号；③Access（接入）——接入号（实验口径 31900/31888）、Access ID、昼/夜 Caller
    Rights COS（0 树号）；④激活——Automated Attendant Review/Modify 置 Valid=TRUE，且所在中继组的
    Automated Attendant 属性置 YES。改叶前需先把 Valid 置 FALSE、改完再 TRUE（p199）。
  conditions: 语音引导 710-719 等需先在 System/Dynamic Voice Guides/Assignment 分配并录制（p175-176）
  tags: [menu-path, iaa, automated-attendant, leaf, tree, access]

- id: f18
  title: 多语言语音引导结构——40 语种映射 + 语言判定链 + 坐席语言成本
  type: diagram
  source_pages: p214-221
  source_chapter: Multi-Language Voice Guide lesson
  source_quote: |
    "40 messages maximum per multi-language guide … Voice guides 700 language 1: 1000 language 2: 1001 …
    language 40: 1039" (p215)
    "The language defined in the call profile has the highest priority … If no language is defined at call
    profile level, the ACR pilot language is used" (p216)
  summary: |
    结构三段：①承载——一个多语言引导（如 740/850）映射最多 40 条消息（语言 1→消息 1000、语言 2→1001、
    …语言 40→1039），存在 OXE 闪存卡；System/Voice Guides 建引导（Function=Multi-language message、
    Start=YES、Backup Tone）；②判定——脚本所用呼叫档案里的语言（多个语言时按 preference，值 1-7、1 最
    优先）决定播报语言；档案无语言则退 ACR Pilot 语言；可挂问候/等待/重定向/封锁/转发五类引导；
    ③选人——语言技能只需 1 门命中即可入选，ASM 按语言偏好 + 技能级别计算 ISM 成本排序（p221 示例：
    Ag1 成本 0 优先）。
  conditions: 偏好值仅对语言类技能有意义（1 最高优先）；坐席不必具备档案里全部语言
  tags: [diagram, multi-language, voice-guide, preference]

- id: f19
  title: IQUEUE 停放级编程结构——6 级 + NEXT 级对路由规则停放管理的覆写
  type: structure
  source_pages: p249-252
  source_chapter: Miscellaneous lesson / Building Block "IQUEUE"
  source_quote: |
    "Allows to overwrite the parking level management done in the routing rule • Up to 7 levels: Levels "1…6"
    • Level "Next" Used to replace the "NEXT" parking level when, after a reselection timeout, the script is re
    executed, but the previous parking level option (VG, IVR script… ) is not terminated" (p249)
    "IQUEUE LEVEL[%1] GUIDE=%701, CUT=YES, REPLAY=%1 … LEVEL[%4] EWT=%1 • LEVEL[%5] ADDR=31888" (p250)
  summary: |
    IQUEUE 构件在脚本内重写等待房间的停放体验：1-6 级每级可配语音引导（引导号、允许掐断、时长、重播
    数）、预期等待时间表（EWT）或地址（IAA/CCivr）；第 7 个"NEXT"级在重选超时重跑脚本而上一停放选项
    （引导/IVR）未播完时接管 NEXT 停放级。行为示例（p252）：第 1 次执行 ISM→忙→引导 701 播 15 秒→
    10 秒重选；第 2 次执行换规则→忙→引导 701 播完整→NEXT 级（757）替代路由规则第 2 级→继续路由规则
    第 3 级。
  conditions: 停放级本身仍在路由规则里管理，IQUEUE 只做覆写
  tags: [structure, iqueue, parking-level, voice-guide]

- id: f20
  title: LIST 变量体系——16 个自动列表、skill/agent 两型、加减算子与截断策略
  type: structure
  source_pages: p258-261
  source_chapter: Miscellaneous lesson / Variable List
  source_quote: |
    "There are 16 automatic lists, indexed from 1 to 16 • A LIST variable is typed by its elements … The "agent"
    type list • The "skill" type list … If the resulting list own more than 7 skills, the list is truncated; the
    skills are removed with the following strategy: Optional skills with the lower level • The mandatory skill
    with the lower level" (p258-259)
    "LIST[%5]=LIST[%1]+LIST[%2]-LIST[%3]+LIST[%4]" (p261)
  summary: |
    体系要点：①脚本内 16 个 LIST[%1..16]，类型由元素决定——skill 型（供 ISM 用：CHARACTERISTICS_LIST、
    CALL_PROFILE[x] 可赋给它）与 agent 型（供授权/非授权名单规则用：Last_Called_Agent、AUTHORIZED_LIST[x]、
    (AGENT{号码}) 可赋给它）；②"+"合并——同技能取高级别、同坐席只留一次；skill 型结果超 7 技能截断
    （先删低级别可选技能，再删低级别强制技能）；agent 型无数量上限；③"-"从前者移除后者全部元素。
    典型用法：RULE_AUTHORIZED_LIST LIST[%5] 实现动态名单。
  conditions: LIST 只能配合授权/非授权名单与 ISM 规则使用（p258）
  tags: [structure, list-variable, skill-type, agent-type]

- id: f21
  title: 过滤器体系结构——AND 语义、Super/Hyper-Filter OR 语义与观测入口
  type: structure
  source_pages: p285-307
  source_chapter: Filter & Statistics lesson
  source_quote: |
    "Up to 200 filters • 7 skills per filter max • The call distribution is not impacted by the filters" (p285)
    "Super-Filter: Group of Filters declared in the same node • Hyper-Filter: Group of Filters declared in
    different nodes • 25 objects per Super-Filter /Hyper-Filter … allow to apply the logical function OR on
    the call profiles" (p303)
  summary: |
    体系四层：①过滤器本体——按呼叫档案/授权名单/非授权名单给 ACR 呼叫分组，最多 200 个、每个 ≤7 技能、
    含服务水准目标（X% 呼叫 Y 秒内）与效率告警阈值；AND 语义（技能全满足才计入）；建在 CCS
    Configurations/Advanced Call Routing/Filter；②Super-Filter（同节点过滤器组）/Hyper-Filter（跨节点）——
    每组 25 对象、OR 语义，建在 Configurations/Super Objects；③实时观测——Real time/Filter、Real time/
    Waiting Room（快捷键 CTRL+左键）、Calls in Waiting Room、Breakdown by Criteria、临时过滤器（窗口关
    闭即失效）；④统计——Last received calls 与三个 Excel 模板（见 f22）。
  conditions: 过滤器不影响分发；新过滤器查不到创建前的数据（预置 20 个过滤器兜底）
  tags: [structure, filter, super-filter, hyper-filter, monitoring]

- id: f22
  title: ACR 统计报表三模板与实时窗口地图
  type: structure
  source_pages: p293-301, p307
  source_chapter: Filter & Statistics lesson
  source_quote: |
    "Filter: Detail Statistics (Formfilter.xls) • Detailed data per time slice (granularity) … Filters: Summary
    of the statistics (FormFilterS.xls) … 1 line per filter … Agents per Filter (FormAgentPerFilter.xls) •
    Agent activity with filters breakdown (all used filters)" (p299-301)
  summary: |
    Excel 三模板分工：Formfilter.xls（明细——按时间片粒度的过滤器数据，Statistics/Excel/Filter 出）、
    FormFilterS.xls（汇总——整个观察期、无粒度、每过滤器一行，Statistics/Excel/Filters Summary 出）、
    FormAgentPerFilter.xls（坐席×过滤器交叉的坐席活动，Statistics/Excel/Agent per Filter 出）；Super/Hyper
    -Filter 同样可出 Excel。实时窗口族：Real time/Filter、Real time/Waiting Room、Real time/Calls in
    Waiting Room、Real time/Breakdown by Criteria、Statistics/Last received calls（近一小时，Update 刷新）。
  conditions: 数据起算点为过滤器创建时刻（见 counter-example）
  tags: [structure, statistics, excel-template, realtime]

- id: f23
  title: 外部 ASM 部署结构——组件选项、站点角色、文件位置与双机复制
  type: structure
  source_pages: p320-335, p352-353, p361-373
  source_chapter: External ASM Server lesson & How-Tos
  source_quote: |
    "Alcatel ASM Module: install the ASM server & ASM manager • ASM Manager: install only the ASM manager
    client tool • ASM server component: install only the ASM server" (p324)
    ""Router" role: call routing requests will be handled by the ASM server … "Default" role: call routing
    requests won't be handled anymore by the ASM server … Agents of this site could be inserted in the agent
    list" (p330)
  summary: |
    部署结构五要素：①组件三选（ASM Module=服务器+管理器 / 仅 Manager 客户端 / 仅 Server 组件）；
    ②服务形态——Windows 服务（ASMServer Tool 安装，需 Automatic 启动模式，MMC 或配置工具启停）；
    ③站点链接——ASM Manager/ASMServer Tool 建 New Site（站名、Main CPU=csm 或 IP、Stand-by CPU、
    Connection role=Router 处理路由并跑脚本 / Default 不处理但本站点坐席可入列表）；④文件位置——外部
    ASM 脚本在安装目录（默认 Program Files/Alcatel/Agent Selection Module/Script，双机实验口径 C:\Program
    Files (x86)\...），内部 ASM 在 OXE /usr3/afe；迁移=复制 .scr 并重新编译+重启服务；⑤双机——
    Main/Stand-By 两台 Windows 服务互指（Duplicate system 安装 + ASMServer Configuration 激活 Duplicated
    ASM），主备连接自动复制、脚本自动同步。
  conditions: 安装外部 ASM 前必须 asm_on_dhs=0 且内部 alb 停止；外部 ASM 连接免许可、连外部 DB 需 167 号许可
  tags: [structure, external-asm, router-role, backup, windows-service]

- id: f24
  title: 外部数据库编程模型——SQL 六构件 + SELECT/存储过程 + fetch 循环 + 数据映射
  type: diagram
  source_pages: p376-392
  source_chapter: External Database lesson
  source_quote: |
    "A specific "SQL" tab is available in the ASM script editor • 6 building blocks … In the same script, up to
    16 different databases can be used … "Read" / "Write" SQL requests to databases are available using an ASM
    script" (p376)
    "The data are retrieved in the loop created between: SQL_START_FETCH DB[% x] & SQL_END_FETCH •
    SQL_BREAK_FETCH allows to exit the loop • The result number is given in a variable SQL_ROW_COUNT" (p390)
  summary: |
    编程模型六件：①USE_DATABASE 建连接（ODBC 源名必填；SQL/Oracle 类库加用户名密码，Access 不用），
    连接随脚本激活建立、去激活断开；②SQL_REQUEST 发 SELECT（SELECT 列 FROM 表 WHERE 谓词）或
    CALL 存储过程（IN/OUT 参数）；③IF DB[%x]<>NULL 测连接、IF SQL_RESULT=... 测结果（SUCCESS/ERROR/
    NOT_FOUND）；④SQL_DATA 把列值映射到本地变量（STRING/INTEGER/REAL/TIME/DATE/TIMESTAMP 各有
    配额）；⑤SQL_START_FETCH…SQL_END_FETCH 循环取行，SQL_BREAK_FETCH 提前退出，SQL_ROW_COUNT
    计行数；⑥无 BREAK 则全表扫——用 LIST 变量收集全部匹配行，不用则只留最后一行。前提：必须外部
    ASM + 32 位 ODBC +（读写时）167 号许可。
  conditions: 存储过程仅当目标库支持嵌入式过程时可用（p384）
  tags: [diagram, sql, odbc, fetch, mapping, external-database]

- id: f25
  title: adm_acd 维护命令选项地图——ACR 的命令行仪表盘
  type: structure
  source_pages: p45, p60, p141, p276, p339-343, p394, p447-451
  source_chapter: 全书维护页汇总
  source_quote: |
    "adm_acd IP@ of the ASM server –salb … To see all the lists created: option 24 node N° (e.g: 24 1; for
    node 1)" (p60)
    "option 60, when the ASM server is connected at least to 1 external database … option 61 (precise the lock
    ACR_SQL (167) availability)" (p394)
  summary: |
    命令形态 `adm_acd <ASM 服务器 IP> -salb`，选项地图：24=查看授权/非授权名单（24 节点号 [名单号]）；
    25=内部数据库管理（25 节点号 [对象 ID]）；28=呼叫动态数据 dump（28 * 看全部，可核对 LAST_CALLED_
    AGENT）；11=Agent List Builder 链路（显示 ASM 服务器↔AFE 连接，外部 ASM 时显示 Windows PC IP）；
    14=ASM Server 与 AFE 间连接类型明细；60=外部数据库连接跟踪（连接/未连接两态）；61=ACR_SQL(167)
    锁可用性。配套命令：ps -edf | grep alb（找进程）、dhs3_init -R MAIN_AFE（重启 AFE）、hybvisu -f all
    （混合链路状态）。
  conditions: 选项号与 OMNX 维护环境相关，均出自原书页码
  tags: [structure, maintenance, adm-acd, troubleshooting, commands]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-17）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 基础 CCD 矩阵搭建 | 有 | f06, f07, f08, f09 | 矩阵对象模型、双配置树、规则/分发结构、混合链路 |
| task-02 | 脚本编写与调试工具链 | 有 | f02, f10, f11 | ASM 架构、脚本生命周期、parameters.cfg |
| task-03 | 授权/非授权名单规则 | 有 | f12 | 五种给值方式与维护入口 |
| task-04 | 重定向/再分发规则 | 有 | f13 | 地址形态与退回链结构 |
| task-05 | 直拨与 ACR 融合 | 有 | f14 | Pilot Direct Call/私有号/DICA/CALL_TYPE 四件套 |
| task-06 | 内部数据库定制路由 | 有 | f05, f15 | 特征清单 + 三键五属性结构 |
| task-07 | Call Tag 生成与传递 | 有 | f16, f17 | 三生成途径 + IAA 三件套配置 |
| task-08 | 字符串处理 | 部分 | —— | 属语法细节，归 principle.md（字符串函数语义表）与 case.md（c08），本文件不重复 |
| task-09 | 多语言语音引导 | 有 | f18 | 40 语种映射 + 判定链 + 成本 |
| task-10 | 综合脚本能力 | 有 | f04, f19, f20 | 规则分类学、IQUEUE、LIST 体系 |
| task-11 | 过滤器与统计 | 有 | f21, f22 | 过滤器体系 + 三模板地图 |
| task-12 | 外部 ASM 割接 | 有 | f23 | 组件/角色/文件位置结构 |
| task-13 | 外部 ASM 双机 | 有 | f23 | Main/Stand-By 复制机制（同条目） |
| task-14 | 外部数据库机制 | 有 | f24 | 六构件编程模型 |
| task-15 | Access 外部库实验 | 有 | f24 | 同一编程模型（Access 侧免凭据差异入 principle） |
| task-16 | MS SQL 侧准备 | 部分 | —— | 属通用软件操作，仅字段/账号约定归 principle/case，本文件不设结构条目 |
| task-17 | MS SQL 外部库脚本 | 有 | f24, f25 | 编程模型 + adm_acd 60/61 观测 |

补充说明：
- f01（课程推进逻辑）是 17 项任务的组织轴；f02/f03（架构与分发流程）为 task-02/05 等提供原理底座。
- task-08/16 的结构性内容较少（语法与软件操作），已在对应文件覆盖，此处如实标注"部分"。
- 生产化边界提示（来自 BOOK_OVERVIEW 批判节）：容量测算方法、多节点组网、脚本版本管理与安全基线在书外；OXE 侧 CCD 配套文档与 CCS 安装规程是各结构条目落地生产环境的必备补充。
