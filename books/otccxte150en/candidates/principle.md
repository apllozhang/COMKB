# 原则/清单/规则/公式/数值口径候选 — OmniTouch CC Standard · Advanced Call Routing (OTCCXTE150EN Issue 01)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（对象编号 3xXXX、账号口令、文件路径）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: ACR 容量上限表（12 项逐格）
  type: metric
  source_pages: p18
  source_chapter: ACR Introduction / ACR Limits
  source_quote: |
    "Statistic Pilot : 1000 • Pilot : 600 • Queues & Waiting Rooms : 600 • Groups : 450 • Directions between
    Pilot and Queues : 30 • Directions between Queues and Processing Groups : 50 • Domains : 20 • Skills :
    1000 • Characteristics List : 1000 • Characteristics (per call profile/ per Agent / max) : 7 / 50 / 20000
    • Authorized List (max number of agents) : 30 • Unauthorized List (max number of agents) : 30
    For more Information check the Feature List" (p18)
  summary: |
    逐格转写：统计 Pilot 1000；Pilot 600；队列与等待房间 600；组 450；Pilot→队列方向 30；队列→处理组
    方向 50；域 20；技能 1000；特征列表 1000；特征数（每呼叫档案/每坐席/系统最大）7/50/20000；
    授权名单最大坐席数 30；非授权名单最大坐席数 30。售前与交付的硬边界以此表为准，细则查 Feature List。
  conditions: 原书 Issue 01 口径；更多容量以 Feature List 为准
  tags: [metric, capacity, limits]

- id: p02
  title: ACD 前缀动作码——话机键盘上的坐席状态码
  type: rule
  source_pages: p22
  source_chapter: How-To Basic CCD matrix creation / step 1
  source_quote: |
    "The ACD prefix can be used (by an analog station or a station without display) to perform the following
    actions: prefix ACD then 1 = unavailable • prefix ACD then 2 = Wrap up • prefix ACD then 3 = call
    supervisor • Prefix ACD then 5 = Logoff • Prefix ACD then 6 = Logon" (p22)
  summary: |
    五个动作码：ACD 前缀+1=不可用、+2=整理（Wrap up）、+3=呼主管、+5=注销、+6=登录。适用于模拟话机
    或无显示屏话机。配套硬规则：ACD 前缀是建一切 CCD 矩阵对象的前提（先查 Translator/Prefix Plan）。
  conditions: 前缀存在性在建矩阵前核查
  tags: [rule, acd-prefix, agent-operations]

- id: p03
  title: 实验口径：公共实验矩阵对象编号全表
  type: metric
  source_pages: p22, p99, p119, p177, p186
  source_chapter: 各 How-To Implementation
  source_quote: |
    "Create one "normal" Pilot: 3x600 • Create one normal Waiting Queue: 3x999700 • Create on Agent
    Processing Group: 3x999800 … Create one ACR Pilot: 3x603 • Create 2 Statistic Pilots: 3X650 (Car
    insurance) & 3X651 (Home insurance) … Create on Waiting Room: 3x999703 … Create some ACD authorized
    phone sets: 3x000, 3x001, 3x002 • Create 1 Superuser set: 3x500 • Create 2 Agent sets: 3x501, 3x502" (p22)
  summary: |
    实验口径（3x 的 x 为讲师给定位数）：普通 Pilot 3x600、ACR Pilot 3x603、等待队列 3x999700、等待房间
    3x999703、坐席处理组 3x999800、统计 Pilot 3x650（车险）/3x651（家险）/31652（Call_Tag2 实验）/
    31653（法语实验）、直拨 Pilot 31604、重定向队列 31999702 + Voice Guide 处理组 31999802 + 引导 710、
    ACD 话机 3x000-3x002、Superuser 3x500、坐席话机 3x501/3x502、坐席 31500/31501/31502、私有号 31001、
    转移目标 31010、IAA 接入号 31900/31888、语音引导 710-719（多语言实验用 740，消息 1000/1001）。
    原文备注 "3X500, 3X501 & 3X502 will be attached to the agent PG 3X800" 中 "3X800" 与前文 3X999800
    不一致，判为教材笔误（照录原文）。
  conditions: 实验口径；生产按客户编号方案整体替换
  tags: [metric, lab, numbering]

- id: p04
  title: 优先级取值规则——0-9 且 0 最高（路由规则/资源选择/呼叫选择三处同口径）
  type: rule
  source_pages: p26, p28, p29
  source_chapter: How-To Basic CCD matrix creation / steps 5-8
  source_quote: |
    "Priority The priority value is from 0 to 9. 0 being the highest priority." (p26)
    "Resource selection priority The value is from 0 to 9. 0 being the highest priority" (p28)
    "Call selection priority The value is from 0 to 9. 0 being the highest priority" (p29)
  summary: |
    三处优先级同一取值域 0-9、0 为最高：Pilot Rule Direction 优先级（队列间）、Resource selection 优先级
    （队列→处理组）、Call selection 优先级（呼叫间排队）。ACR 呼叫经 Waiting Room 时无资源选择优先级
    （选人归 ASM），但呼叫选择优先级仍参与 CCD/ACR 混合排序（见 p24 条目）。
  conditions: 优先级与方向开关均可改由 CCS 管理（p28/p29 Tips）
  tags: [rule, priority, routing]

- id: p05
  title: 规则数量口径——每 Pilot 30 条路由规则（0-29）、分发规则 10 条
  type: metric
  source_pages: p26, p27
  source_chapter: How-To Basic CCD matrix creation / steps 5-6
  source_quote: |
    "Rule Number It is possible to declare up to 30 rules per pilot" (p26)
    "Current Pilot Rule Number Put the number of active rule (from 0 to 29) at the moment for the Pilot." (p26)
    "Rule Number It is possible to create up to 10 rules." (p27)
  summary: |
    每 Pilot 最多声明 30 条路由规则（Rule Number 0-29），同一时刻由 Current Pilot Rule Number 指定一条
    生效；分发规则最多 10 条。生效规则另有两种切换途径：CCS Rule Window 的 Apply 按钮、CCS 日历。
  conditions: 无
  tags: [metric, rules, pilot]

- id: p06
  title: 技能/域/呼叫档案取值域——域名 1-16 字符 ID 0-99 权重 1-20；技能缩写 1-4 字符；档案 ID 0-999、级别 1-9、语言偏好 1-7
  type: metric
  source_pages: p37, p38, p39, p229
  source_chapter: How-To Basic CCD matrix creation / steps 15-17
  source_quote: |
    "Name Name of the Domain (1 to 16 characters) • ID The next free ID will be used (ID range 0 – 99) •
    Weight Weight used by the Individual Skill Mapping (ISM) calculation algorithm to classify domains (1 for
    the least important to 20 for the most important)." (p37)
    "Name Name of the skill (1 to 16 characters) • Abbrev. Abbreviation of the skill (1 to 4 characters)" (p38)
    "ID The next free ID will be used (ID range 0 – 999) • Select the right skill • Level 1 to 9 (Expertise
    Level) • Mandatory or Optional Mandatory -> the agent liable to process the call must have the skill to be
    selected • Preference 1 to 7 only for Languages (1 for the highest priority language)" (p39)
  summary: |
    取值域：域名 1-16 字符、域 ID 0-99、域权重 1-20（ISM 算法用，20 最重要）；技能名 1-16 字符、缩写
    1-4 字符、ID 0-99；呼叫档案 ID 0-999、技能级别 1-9、强制/可选（强制=坐席没有该技能即不入选）、
    偏好 1-7（仅语言技能用，1 最高优先）。坐席技能分配同用级别 1-9（CCSupervisor/Configurations/Agent）。
  conditions: 域与技能也可由 mgr 或 OmniVista 8770 管理；坐席技能也可经 Skill Matrix 配（p227）
  tags: [metric, skill, domain, call-profile]

- id: p07
  title: asm_ag_free_duration 三值语义与最低版本——Idle 规则排序的同名不同义
  type: rule
  source_pages: p48-49, p241-242
  source_chapter: How-To Manage a script / steps 5-6 & Miscellaneous lesson
  source_quote: |
    "0 : free duration feature not enabled The agent order is done in the alb or ASM external server. Agent
    are order depending on their idle time since the logon time. • 1 : free duration feature enabled, previous
    behavior (standalone only) … Value 2 : free duration feature enabled, new behavior (with
    asm_ag_free_duration sent every 3 sec.) This new behavior offers the possibility to know each agent ACD
    idle time in the alb process, and to order them whatever they are in a network node." (p49)
    "asm_ag_free_duration= 0 use of the rule "PLTR (Period Logon Time Ratio):" number of calls/time to logon.
    • asm_ag_free_duration= 1 in this case LIT (Longest Idle Time) is used (rule Idle-time). •
    asm_ag_free_duration= 2 LIT in case ASM in network (LIT on local agent or network)." (p242)
  summary: |
    三值语义：0（默认）=PLTR——登录时段话务比（处理呼叫时长/登录时长），同值再按服务呼叫数；1=LIT
    （最长空闲）单机行为；2=LIT 组网行为（每 3 秒向 alb 上报空闲时长，跨节点统一排序）。最低软件版本
    l2.300.32.a；参数行须用文本编辑器手工添加；改后必须重启 MAIN_AFE（dhs3_init -R MAIN_AFE）。
    使用 LIT 还必须在脚本里显式加 IDLE 构件（p242 NB）。
  conditions: 值 1 对应旧 patchIdle 文件行为，该文件已不存在（迁移见 p49 "Migration to parameters.cfg file"）
  tags: [rule, lit, pltr, version, parameters-cfg]

- id: p08
  title: PLTR/LIT 排序公式——PLTR=处理时长/登录时长，统计周期默认 5 分钟
  type: formula
  source_pages: p239-240
  source_chapter: Miscellaneous lesson / Rule IDLE
  source_quote: |
    "ratio1=(20+50+30)/(20*60) ratio1=0,083 … ratio2=(2)/(20) ratio2=0,1 … Same order during the statistic
    period (5 min by default)" (p239)
    "In case of equal cost, agents are sorted increasingly according to their LIT (Logon Idle Time)" (p240)
  summary: |
    PLTR（asm_ag_free_duration=0）：比率=统计周期内处理呼叫时长之和 ÷ 登录时长，示例坐席 1 =
    (20+50+30)/(20×60)=0.083；坐席 4 = 2/20=0.1；同成本按比率升序排。LIT（=1）：按登录后最长空闲时长
    升序。统计周期默认 5 分钟，周期内排序结果保持不变。COM 规则不受 asm_ag_free_duration 影响
    （按服务呼叫数比率排，同值回看空闲比，p243/p265）。
  conditions: 参数取值影响 Idle 规则语义，不影响 Com 规则
  tags: [formula, pltr, lit, idle, com]

- id: p09
  title: 空坐席列表兜底链——脚本重试 20 次（观察值含 21 次）→ 路由管理 → ACR Pilot 封锁
  type: rule
  source_pages: p50, p184
  source_chapter: How-To Manage a script & Call Tag How-To
  source_quote: |
    "When you call the Statistic pilot 3X651 (Call Profile 2: English and Home), the alb process makes 20
    requests (script is executed 20 times) and in case of empty agent list, the call follows the routing
    management. If no other direction (mutual aid, …) is available, as last resort, the call uses the ACR
    pilot blockage mode" (p50)
    "This Customer Number is NOT known in the Internal Database, so the script will be executed 21 times." (p184)
  summary: |
    兜底链：坐席列表持续为空时脚本按重选机制反复执行（p50 口径 20 次；p184 实验观察 21 次——两处数字
    不一致，照录原文，差异疑与重选计次口径有关，推断），随后呼叫转入路由管理（互助方向等），全无可用
    方向时最后落到 ACR Pilot 封锁模式。设计脚本时必须给重定向/再分发兜底，避免呼叫悬到封锁。
  conditions: 20/21 两个数字均为原书原文；具体计次规则原书未展开（推断为边界差异）
  tags: [rule, fallback, blockage, reselection]

- id: p10
  title: 名单类规则硬上限——100 列表（ID 0-99）、每列表 30 坐席、脚本内显式列表不限、坐席须有≥1 活动技能
  type: rule
  source_pages: p61, p63-64
  source_chapter: Authorized List lesson & How-To step 1
  source_quote: |
    "100 lists (Authorized / Unauthorized) maximum • 30 Agent per list • No limit of Agents, when the content
    of the list is defined in the script • An Agent belonging to a list must have at least 1 active skill •
    The Rule_Authorized_List and Rule_Unauthorized_List can be combined with other Rules (ISM, …)" (p61)
    "ID 0 – 99 for Authorized and Unaurthorized Lists" (p63, "Unaurthorized" 为原文拼写)
  summary: |
    硬规格：授权/非授权名单合计最多 100 个（ID 0-99，授权默认名 WList_x、非授权 BList_x）；每列表最多
    30 坐席；脚本内显式坐席列表无上限；进入任何名单的坐席须至少有 1 个活动技能（无技能坐席被排除）。
    名单规则可与 ISM 等规则组合。
  conditions: 默认名 WList_0/BList_1 等可改名
  tags: [rule, authorized-list, limits]

- id: p11
  title: 脚本命名与字符串大小写敏感——脚本名 ≤8 字符；名单 String 索引区分大小写
  type: rule
  source_pages: p65, p72, p74
  source_chapter: Authorized/Unauthorized How-To steps 2/5
  source_quote: |
    "Script Name Authoriz (max 8 characters)" (p65)
    "Script Name Unauthor (max 8 characters)" (p72)
    "The String is case sensitive! You can use UNAUTHORISED_LIST ->%integer to define -> Integer = ID Number
    of the List" (p74)
  summary: |
    两条命名规则：脚本名最长 8 字符（Authoriz/Unauthor/Redirect/Redistri 均卡在 8 字内）；名单规则的
    "String to define" 索引区分大小写（教材以感叹号强调）。名单关键字书写原文两种拼法混用
    （AUTHORIZED/AUTHORISED），以编辑器实际接受为准。
  conditions: 全版本适用
  tags: [rule, naming, case-sensitive]

- id: p12
  title: 调试器约束——只能修改既有构件、不能新增构件；可直接发起呼叫；INTEGER 观察用 + %0 技巧
  type: rule
  source_pages: p80, p101, p127, p262
  source_chapter: Authorized/Unauthorized & Redirection How-Tos & Miscellaneous
  source_quote: |
    "You can only modify the existing Building Blocks, it is not possible to add a Building Block." (p80, p101)
    "Tips You can also make calls using the Debugger" (p127)
    "To display an INTEGER Value in the Debugger use the following syntax: INTEGER[%1]= INTEGER[%1] + %0" (p262)
  summary: |
    调试器三条使用规则：①运行中只能改既有构件的条件参数（如把 IF TIME<10:0:0 改成 >），不能加新构件；
    ②可直接从 Debugger 发起呼叫做验证；③观察整型变量值需用 INTEGER[%x]=INTEGER[%x]+%0 的显示技巧。
  conditions: 调试器连接 ASM（内部/外部同一功能，p338）
  tags: [rule, debugger, maintenance]

- id: p13
  title: Redirection 地址三形态——静态（内部/外部经缩位拨号或网络号）与动态（STRING 变量/数据库）
  type: checklist
  source_pages: p85, p95
  source_chapter: Redirection lesson & How-To
  source_quote: |
    "Redirection address can be: A static phone number Internal forward (on-pcx) • External forward Through a
    speed dialing number • Through a network N° • A dynamic phone number Stored in a STRING variable Retrieved
    from a database…" (p85)
    "Address can be internal, external or can be defined in a string variable" (p95)
  summary: |
    转发地址清单：静态——内部分机（on-pcx）或外部号（经缩位拨号 speed dialing 或网络号）；动态——
    STRING 变量承载（可从数据库取）。写脚本时构件参数里三选一。
  conditions: Redirection 为单用规则，须独占 APPLY
  tags: [checklist, redirection, addressing]

- id: p14
  title: Redistribution 触发与退回语义——列表空或全部注销/不可用即退下一路由方向，无方向则 Blockage
  type: rule
  source_pages: p88-90
  source_chapter: Redistribution lesson
  source_quote: |
    "The ASM script returns the call to the next Routing Direction … Routing Direction available and open?
    If not, the call goes to Blockage mode" (p89)
    "If "AGENT_LIST" is NULL or if the list is not empty, but all agents are logged off or unavailable, then
    the REDISTRIBUTION Rule will be applied" (p90)
  summary: |
    触发条件两种：列表为空，或列表非空但坐席全部注销/不可用。行为：把呼叫交回 CCD 矩阵的下一路由
    方向；方向不可用/未开时进 Blockage 模式（封锁地址或语音引导）。工程含义：Redistribution 的落点
    依赖路由规则里预配的次优先方向（如重定向队列接 Voice Guide）。
  conditions: Redistribution 为单用规则
  tags: [rule, redistribution, blockage]

- id: p15
  title: DICA 自动技能规则——配私有号即挂 DirectCall 技能；停用即完全不可直拨
  type: rule
  source_pages: p111
  source_chapter: Direct Calls & ACR lesson
  source_quote: |
    "When a private number is managed for one Agent, the system automatically assigns a new skill for this
    Agent • Domain: Media • Skill: DirectCall • Abbreviation: DICA • If the "DirectCall" skill is not activated,
    it is no more possible to call the agent directly (whatever the agent status: idle, busy…) • The call is
    forwarded immediately to the "pilot direct call"" (p111)
  summary: |
    规则两段：给坐席配私有号（Private Agent No.）后系统自动在 Media 域挂 DirectCall 技能（缩写 DICA，
    CCS 界面可见可改）；该技能一旦停用，无论坐席空闲与否都无法直拨——呼叫立即转到该坐席所在处理组的
    pilot direct call。这是"临时屏蔽直拨"的开关型技能。
  conditions: 直拨特性还需处理组配 Pilot Direct Call（见 f14）
  tags: [rule, dica, direct-call, skill]

- id: p16
  title: 一个 ACR Pilot 同一时刻只能激活 1 个脚本
  type: rule
  source_pages: p113
  source_chapter: Direct Calls & ACR lesson
  source_quote: |
    "Only 1 ACR script can be used at the same time on an ACR Pilot" (p113)
  summary: |
    硬规则：一个 ACR Pilot 上同一时刻只激活一个脚本。设计含义：直拨专用 Pilot 若不直拨可达（dedicated），
    可挂"只管直拨等待"的脚本；若该 Pilot 还接普通来话，则脚本必须用 CALL_TYPE 分支兼容两种呼叫来源。
  conditions: 换脚本=重新激活，原脚本被替换
  tags: [rule, script, pilot]

- id: p17
  title: CALL_TYPE=DIRECT_CALL 关键字与直拨脚本骨架
  type: rule
  source_pages: p114-115, p121
  source_chapter: Direct Calls & ACR lesson & How-To
  source_quote: |
    "The call type "Direct_Call" can be tested with an ACR script … Keyword: CALL_TYPE" (p114)
    "IF SEQUENCE=%1 RULE_REDIRECTION 31010 SET RESELECTION_TIMEOUT=%180 IF CALL_TYPE=DIRECT_CALL
    RULE_ISM Call_Profile=%1" (p115)
  summary: |
    脚本骨架：SEQUENCE=%1 分支 + SET RESELECTION_TIMEOUT 定等待秒数 + IF CALL_TYPE=DIRECT_CALL
    区分直拨（等原坐席 N 秒→超时转目标号）与非直拨（走 ISM 档案）。直拨路径第 1 次执行在等待房间等
    原坐席，第 2 次执行（重选超时后）触发 RULE_REDIRECTION。
  conditions: 直拨行为依赖处理组 Pilot Direct Call 与坐席私有号配置
  tags: [rule, call-type, script-pattern]

- id: p18
  title: 内部数据库口径——4000 条、单值或区段、通配号可用
  type: metric
  source_pages: p131, p132
  source_chapter: Internal Database lesson
  source_quote: |
    "Note: 4000 entries (single value or range) can be created in the Internal Database" (p131)
    "Complete Number or open Number • Unique number or Range" (p132)
  summary: |
    内部数据库容量 4000 条；主叫号键支持完整号或开放号（open number，即通配）、单值或区段——
    例：Call Tag 键录 1000-1999 区段即可整段命中（p135/p152 实验）。
  conditions: 数据在 CCS Configurations/Advanced Call Routing/ACR Data 维护
  tags: [metric, internal-database, capacity]

- id: p19
  title: Call Tag 取值口径——IAA 编码 ≤16 位、统计 Pilot 0-32 字符、屏显计时器 0 或 10-32767
  type: metric
  source_pages: p153, p156, p169
  source_chapter: Internal Database How-To & Call Tag lesson
  source_quote: |
    "Type the Call Tag 0 – 32 Characters" (p153)
    "You also can manage the "Call Tag Display Timer" (Value 0, or 10 – 32767)" (p156)
    "The code entry guide prompts the caller to dial a code (max code length = 16 digits) and send it to the
    CSTA application as "Correlator data"." (p169)
  summary: |
    三处数值：统计 Pilot 的 Call Tag 字段 0-32 字符；IAA 编码叶客户可拨代码最长 16 位（以 Correlator data
    经 CSTA 传递）；坐席屏 Call Tag 显示计时器取 0 或 10-32767（单位秒，0 常显）。要在坐席屏显示 Call Tag
    还需把处理组参数 "Display on agent screen" 设为 Call tag 或 caller and pilot char.（p156）。
  conditions: 无
  tags: [metric, call-tag, display]

- id: p20
  title: 转移覆盖原则——呼叫上下文中最后一个 Call Profile / Call Tag 覆盖之前所有值
  type: principle
  source_pages: p172-173, p189
  source_chapter: Call Profile or Call Tag / Transfer lesson & How-To step 6
  source_quote: |
    "The last profile met in the call context overwrites the previous one" (p172)
    "The last Call tag met in the call context overwrites the previous one" (p173)
    "The first CALLTAG "2500" will be overwritten be the CALLTAG of the Statistic Pilot 31650 (CALLTAG 1500)." (p189)
  summary: |
    原则：呼叫被转移/转发时，路径上最后施加的 Call Profile 或 Call Tag 覆盖先前值。实验实证：呼叫带
    Call Tag 2500 进 ACR Pilot 31604 → 该 Pilot 处于 General Forwarding（GFW）转发到统计 Pilot 31650
    （Call Tag 1500）→ 到达脚本时生效的 Call Tag 是 1500。设计转发链时以此判断"哪个标签最终生效"。
  conditions: GFW（General Forwarding）转发地址在 CCS Pilot 配置里设置并激活（p188）
  tags: [principle, call-tag, transfer, overwrite]

- id: p21
  title: 字符串函数语义表——"+" 拼接 / STRING_LENGHT / SEARCH_STRING（未找到=0）/ STRING_FORMAT / EXTRACT_STRING 双形态
  type: metric
  source_pages: p192-196
  source_chapter: String handling lesson
  source_quote: |
    "STRING[%3] = STRING[%1] + " " + STRING[%2] … STRING[%1]=“test” INTEGER[%1]=STRING_LENGHT STRING[%1]
    … The returned value in this example will be equal to 4." (p192)
    "INTEGER[%1]=SEARCH_STRING “212” STRING[%1] So, the INTEGER[%1]=5 … Content of INTEGER[%1] is set to
    “0” if the SEARCH_STRING was not found" (p193)
    "STRING[%2]=EXTRACT_STRING "0231" STRING[%1] … STRING[%2]=“2121001”" (p195)
    "STRING[%2]=EXTRACT_STRING INTEGER[%1] INTEGER[%2] STRING[%1] … The result in STRING[%2] will be
    ="0221001"" (p196)
  summary: |
    五个关键字语义：①"+" 拼接（可夹空格串）；②STRING_LENGHT（原文拼写如此）取串长，"test"→4；
    ③SEARCH_STRING 在第二串中找第一串，返回起始下标，找不到返回 0（"02312121001" 找 "212"→5）；
    ④STRING_FORMAT 把整数/实数转字符串；⑤EXTRACT_STRING 两形态——(字面串, 源串)=从源串中剔除该
    字面串（"02312121001" 剔 "0231"→"2121001"）；(起始下标, 长度, 源串)=按位截取，首字符位=1。
    注意 p196 示例结果原文印作 "0221001"，与按位截取的直观结果不符，疑教材笔误（照录原文）。
  conditions: 字符串自动变量每脚本最多 64 个（p253）
  tags: [metric, string, functions]

- id: p22
  title: 多语言引导规则——40 语种/引导；档案语言最高优先、无则 Pilot 语言；偏好 1-7（1 最高）；1 门语言技能即命中
  type: rule
  source_pages: p214-216, p229
  source_chapter: Multi-Language Voice Guide lesson
  source_quote: |
    "40 messages maximum per multi-language guide" (p215)
    "The language defined in the call profile has the highest priority • In case of multiple languages, the
    language preference is taken into account … If no language is defined at call profile level, the ACR pilot
    language is used" (p216)
    "The value of the preference associated to each language will determine which language will be above the
    other when broadcasting guides or when choosing the agent who will handle the call (value included
    between 1 and 7, 1 for the highest priority language)" (p229)
    "Remind that an agent is not obliged to have all language skills defined in the call profile: 1 language
    skill is enough" (p214)
  summary: |
    四条规则：①一个多语言引导最多映射 40 条消息（语言 1→消息 1000…语言 40→1039）；②播报语言判定
    链——脚本所用呼叫档案的语言（多语言时按偏好）> ACR Pilot 语言；③偏好值 1-7、1 最高，同时决定
    播报语言与选坐席时的语言优先；④坐席无需具备档案全部语言，命中 1 门即可入选。
  conditions: 多语言引导在 System/Voice Guides 建（Function=Multi-language message、Start=YES、Backup Tone 56）
  tags: [rule, multi-language, preference, voice-guide]

- id: p23
  title: 呼叫选择三序与 ACR Actual Waiting 开关——优先级→ISM 成本→实际等待（False）；优先级→实际等待→ISM 成本（True）
  type: rule
  source_pages: p234, p282
  source_chapter: Miscellaneous lesson & How-To step 8
  source_quote: |
    "By default the system checks: The highest priority • The lowest ISM cost • The highest real waiting time
    (Real waiting time – handicap on waiting) • ACR Actual Waiting parameter: Allows to change the call
    selection mode • Location: "Applications / CCD / CCD/RSI system parameters"" (p234)
    "At equal Priorities & ACR Actual Waiting set to FALSE (Default value), the lowest ISM cost is used. If
    the Parameter ACR Actual Waiting is set to TRUE, the highest real waiting time is used" (p282)
  summary: |
    呼叫选择次序：先比优先级（0-9，0 最高）；优先级相同时按 ACR Actual Waiting 参数（mgr
    Applications/CCD/CCD/RSI system parameters）分两派——False（默认）：先最低 ISM 成本再最长实际等待
    （实际等待−等待惩罚）；True：先最长实际等待再最低 ISM 成本。混合场景实证：等待房间 8 / 队列 9
    优先级不同→房间呼叫先被处理；同为 9→按上述参数分派。
  conditions: 实际等待=Real waiting time – handicap on waiting（等待惩罚可配）
  tags: [rule, call-selection, acr-actual-waiting]

- id: p24
  title: ISM 成本规则——等待房间：ISM 按档案算/其他规则 0；等待队列：无穷；排序 ACR(非ISM)=0 < ACR(ISM)≥0 < CCd=无穷
  type: metric
  source_pages: p235, p221
  source_chapter: Miscellaneous lesson
  source_quote: |
    "ISM cost • Call parked in a waiting room • ISM rule The ISM cost is calculated in the script according to
    the profile • Other rule No ISM cost, so the cost is fixed by the system to "0" • Call parked in a waiting
    queue No ISM cost, so the cost is fixed to an unlimited value • ISM cost priority ACR call, using a rule
    other than ISM rule (ISM cost=0) • ACR call, using an ISM rule (ISM cost>= 0) • CCd call (ISM
    cost=infinite)" (p235)
  summary: |
    成本三档：等待房间里的呼叫——ISM 规则按呼叫档案计算成本、其他规则固定 0；等待队列里的（普通
    CCD）呼叫——无 ISM 成本，按无穷处理。由此形成选呼优先序：非 ISM 的 ACR 呼叫（0）→ ISM 的 ACR
    呼叫（≥0，语言偏好等参与计算，p221 示例 Ag1 成本 0/Ag2 成本 3）→ 普通 CCd 呼叫（无穷）。这是
    ACR 呼叫能"插队"普通 CCD 呼叫的机制本质。
  conditions: 成本仅在等待房间（ACR 侧）语境下有意义
  tags: [metric, ism-cost, call-selection]

- id: p25
  title: 规则组合法则——单用规则独占 APPLY；可组合规则可串接；IDLE/COM 互斥；1 APPLY 链式过滤、多 APPLY 各自独立（首个失效）
  type: rule
  source_pages: p244-247, p266-270
  source_chapter: Miscellaneous lesson & How-To steps 3-4
  source_quote: |
    "When 2 “APPLY” instructions are encountered, the 1st one has no effect on the result sent back to the call
    handling • When only 1 “APPLY” instruction is used, the agent list of a rule is build according to the
    agent list of the previous rule" (p245)
    "Only agent 31501 is part of the agent list" (p246, 1 APPLY)
    "The 1st rule (“AUTHORIZED_LIST”) agent list is not used as input of the 2nd rule" (p247, 多 APPLY)
  summary: |
    组合三法则：①单用规则（LAST CALLED AGENT/REDIRECTION/REDISTRIBUTION/IVR）必须独占 APPLY；
    可组合规则（AUTHORIZED LIST/UNAUTHORIZED LIST/ISM/IDLE/COM）可串接；IDLE 与 COM 互斥。
    ②APPLY 数量决定语义：仅 1 个 APPLY 时前规则输出=后规则输入（授权名单 31501+31502 过滤后仅剩
    技能匹配的 31501）；≥2 个 APPLY 时各 APPLY 独立、第一个的结果不进入第二个（ISN 按全量坐席算，
    授权名单约束失效——实验里 31500 虽不在名单也被呼）。设计"名单+技能"组合必须用单 APPLY。
  conditions: SET 指令（PRIORITY/RESELECTION_TIMEOUT）不占 APPLY
  tags: [rule, apply, combination, idle, com]

- id: p26
  title: IQUEUE 停放级语义——6 级+NEXT 覆写路由规则停放；每级可配引导/EWT 表/地址
  type: rule
  source_pages: p249-252
  source_chapter: Miscellaneous lesson / IQUEUE
  source_quote: |
    "For each one, it's possible to define: A voice guide (VG N°, cut authorized, duration, replay number) •
    An Expected Waiting Time Table • An address (IAA, CCIvr)" (p249)
    "In that case, "NEXT" level replaces the level 2 of the routing rule • The V .G N° 703 of the routing rule
    is then diffused (cause level 3 of IQueue is not specified)" (p252)
  summary: |
    语义：IQUEUE 在脚本内覆写等待房间的停放级体验——1-6 级每级可配语音引导（引导号/允许掐断/时长/
    重播数）、预期等待时间表或地址（IAA/CCivr）；NEXT 级仅在"重选超时重跑脚本而上一停放选项未播完"
    时接管 NEXT 停放。未指定的级回落到路由规则自身的停放配置。
  conditions: 停放级基础管理仍在路由规则（路由规则级示例：Level1 引导 701 15 秒…）
  tags: [rule, iqueue, parking]

- id: p27
  title: 屏显构件口径——显式串/显示变量（CALLING、AGENT NUMBER、CALLTAG）/自动串变量 ≤64/CALLTAG 值；与处理组 display 参数无关
  type: rule
  source_pages: p253, p156
  source_chapter: Miscellaneous lesson
  source_quote: |
    "Allows to display an information on the agent set • Explicit character string • A call display variable
    (CALLING, AGENT NUMBER, CALLTAG) • A string automatic variable (up to 64 strings can be defined in a
    script) • The call tag value • Not related with the "display on agent set" parameter of the Processing
    Group" (p253)
  summary: |
    DISPLAY_AGENT 构件四类取值：显式字符串、呼叫显示变量（CALLING/AGENT NUMBER/CALLTAG）、字符串
    自动变量（每脚本最多 64 个）、Call Tag 值。它与处理组的 "display on agent set" 参数相互独立——脚本
    屏显不需要改处理组参数，但 Call Tag 的"字段级"显示（p156）则要改该参数，两套显示机制并存。
  conditions: 无
  tags: [rule, display-agent]

- id: p28
  title: CLEAR AGENT LIST 与 IVR 规则语义——清空前列表重选；IVR 规则把呼叫送 CCivr 资源组并可传档案
  type: rule
  source_pages: p254-257
  source_chapter: Miscellaneous lesson
  source_quote: |
    "This Building Block is use to clear the previous Agent List" (p254)
    "A CCivr resource group can be managed in the distribution of a waiting room • An "IVR rule" is necessary
    to distribute the call to this IVR processing group • The CCivr server can read the call profile received
    through CSTA and test it in its script, using the "receivephonecall.callprofile" building block result" (p255)
  summary: |
    两条构件语义：①CLEAR AGENT LIST 清空此前规则产生的坐席列表（如 LCA 结果），让后续规则全量重算
    （实验：重选 12 秒后清列表再走 LAST_CALLED_AGENT，p275）；②RULE_IVR 把呼叫分发到等待房间分发
    配置里的 CCivr 资源组，可随呼叫传档案——CCivr 侧用 receivephonecall.callprofile 构件读档案（例如按
    语言技能接对应语言引导）；典型写法 IF WAIT<%30 RULE_IVR … SET RESELECTION_TIMEOUT=%10
    RULE_ISM（先 IVR 后 ISM）。
  conditions: IVR 为单用规则
  tags: [rule, clear-agent-list, ivr, ccivr]

- id: p29
  title: 过滤器口径——≤200 个、每过滤器≤7 技能、AND 语义、不影响分发；临时过滤器活到窗口关闭
  type: metric
  source_pages: p285, p296, p314
  source_chapter: Filter & Statistics lesson & How-To
  source_quote: |
    "Up to 200 filters • 7 skills per filter max • The call distribution is not impacted by the filters" (p285)
    "The temporary filter will be retained until the real time window closure" (p296)
    "Filter use the Function "AND", a Super-Filer / Hyper-Filer use the Function "OR"" (p314, 原文拼写如此)
  summary: |
    口径四条：过滤器最多 200 个、每个最多 7 技能（含级别区间与强制/可选）；过滤器是统计分组视角，
    完全不影响呼叫分发；语义为 AND（三技能全中才算），对照 Super/Hyper-Filter 的 OR；实时窗口里建的
    临时过滤器只活到该窗口关闭。过滤器可含服务水准目标（如 75% 呼叫 15 秒内）与效率告警阈值
    （85%，实验口径）。
  conditions: 过滤器可基于呼叫档案、授权名单或非授权名单
  tags: [metric, filter, and-or]

- id: p30
  title: 过滤器数据时效——新过滤器查不到创建前的 Excel 数据；系统预置 20 个过滤器兜底
  type: rule
  source_pages: p302
  source_chapter: Filter & Statistics lesson
  source_quote: |
    "When a new filter is created, we cannot retrieve, in Excel files, data prior to the filter creation date
    • But, keep in mind that 20 predefined filters originally exist; so Excel files will be available using
    these filters" (p302)
  summary: |
    数据时效规则：过滤器统计从其创建时刻起算，Excel 报表取不到创建前的历史；系统出厂预置 20 个过滤
    器，这些预置过滤器的历史数据可用。运维含义：要按新业务口径出报表，需提前建过滤器。
  conditions: 仅 Excel 统计受限，实时不受影响（实时只看当前）
  tags: [rule, filter, statistics, history]

- id: p31
  title: Super/Hyper-Filter 口径——同节点/跨节点组、每组 25 对象、OR 语义、实时与 Excel 通用
  type: metric
  source_pages: p303, p307
  source_chapter: Filter & Statistics lesson
  source_quote: |
    "Super-Filter: Group of Filters declared in the same node • Hyper-Filter: Group of Filters declared in
    different nodes • 25 objects per Super-Filter /Hyper-Filter … The Super- and Hyper-Filter allow to apply
    the logical function OR on the call profiles" (p303)
    "Excel statistics reports are of course available for Super-filter/Hyper-filter" (p307)
  summary: |
    口径：Super-Filter=同一节点内过滤器组；Hyper-Filter=跨节点过滤器组；每组最多 25 个对象；语义为
    OR（任一成员过滤器命中即计入）；实时窗口与 Excel 统计报表均支持。建组入口 Configurations/
    Super Objects。
  conditions: 无
  tags: [metric, super-filter, hyper-filter]

- id: p32
  title: 外部 ASM 许可与前提清单——连接免许可；外部 DB 读写需 167 号许可；asm_on_dhs=0；alb 停止；服务自动启动
  type: checklist
  source_pages: p320-322, p327, p376, p394
  source_chapter: External ASM Server lesson & External Database lesson
  source_quote: |
    "Connection to the External ASM Server is possible without any software license • If you need a connection
    to an External Database (MS SQL), a software license is needed in the PBX (Software License N° 167: "ACR
    data base read")" (p320)
    "you must disable the parameter "asm_on_dhs" in the "parameters.cfg" file … so "AFE" will not start the
    "ALB" process" (p322)
    "Note: Service need to be started in Automatic Mode" (p327)
  summary: |
    前提清单五项：①外部 ASM 与 OXE 间连接不需要许可；②脚本要访问外部数据库（读/写）需 OXE 软件
    许可 N°167 "ACR data base read"（运维可用 adm_acd 选项 61 核该锁可用性）；③安装外部 ASM 前必须把
    /usr3/afe/parameters.cfg 的 asm_on_dhs 置 0 并重启 MAIN_AFE（否则 AFE 继续拉起内部 alb）；④必要时
    kill alb 进程（ps -edf | grep alb 核查）；⑤ASM Windows 服务设为自动启动模式。
  conditions: 硬件/软件需求查随软件的 installation procedure（p323）
  tags: [checklist, external-asm, license, prerequisites]

- id: p33
  title: ASM 站点角色语义——Router 处理路由并跑脚本；Default 不处理但坐席可入列表；双机 Main/Stand-By 自动复制
  type: rule
  source_pages: p330, p331-333, p371
  source_chapter: External ASM lesson
  source_quote: |
    ""Router" role: call routing requests will be handled by the ASM server • Scripts will be run • Agents of
    this site could be inserted in the agent list • "Default" role: call routing requests won't be handled
    anymore by the ASM server • Scripts won't be run by the ASM server using a "default" role • Agents of
    this site could be inserted in the agent list" (p330)
    "As soon as the connection between the MAIN ASM Server (PC1) & the AFE Server (Oxe csm), the connection
    will be automatically duplicated between the Stand-By ASM Server (PC2) & the AFE Server." (p371)
  summary: |
    角色语义：站点链接的 Connection role=Router 时该 ASM 处理路由请求并执行脚本，本站点坐席可进列表；
    =Default 时不再处理路由、脚本不跑，但坐席仍可进列表。双机：每台 PC 的服务里互设 Main/Stand-By
    （ASMServer Configuration → Duplicated ASM），改配置前必须停服务；主 ASM 与 AFE 的连接建立后自动
    复制到备机；备机也必须知道 OmniPCX 名；脚本自动同步到备机目录。
  conditions: 改双机配置需确认弹窗并会重启 ASM 服务（p333）
  tags: [rule, asm-site, router, default, backup]

- id: p34
  title: 脚本迁移规则——scr/alb 存放位置内外有别；迁移=复制 scr+重编译；迁移后重启服务
  type: rule
  source_pages: p335, p354
  source_chapter: External ASM lesson & How-To
  source_quote: |
    "The "scr" and "alb" files are stored in the ASM server installation directory in case of External ASM
    server (by default: Program Files/Alcatel/Agent Selection Module / Script) • The "scr" and "alb" files are
    stored in the usr3/afe directory in case of Internal ASM server • To transfer the script from an internal
    to an external ASM server (and vice-versa), the "scr" file has to be copied and recompiled • Restart the
    ASM server (windows service) after script transfer" (p335)
  summary: |
    迁移三规则：位置——外部 ASM 脚本在安装目录（默认 Program Files/Alcatel/Agent Selection Module/
    Script），内部在 OXE /usr3/afe；迁移——内部↔外部迁移必须复制 .scr 源文件并重新编译（.alb 不通用）；
    收尾——迁移后重启 ASM 服务。脚本不在本机时可用 FTP 从 OXE 取（/usr3/afe），再经编辑器 Import/
    From File System 导入。
  conditions: 双机部署下脚本自动复制到备机同目录（p373）
  tags: [rule, script-migration, scr, alb]

- id: p35
  title: 外部 ASM 防火墙口径——放行 ASM 与 ASMMgr 的入站 UDP+TCP（专用配置文件 Profile）
  type: checklist
  source_pages: p360
  source_chapter: External ASM How-To step 6
  source_quote: |
    "If the connection to the ASM Server is not possible, check you Windows Firewall configuration. Allow in
    the Inbound Rule ASM Protocol UDP and TCP in Private • Allow in the Inbound Rule ASMMgr Protocol UDP
    and TCP in Private" (p360)
  summary: |
    连不通外部 ASM 的第一个检查点：Windows 防火墙入站规则须放行 ASM（UDP+TCP）与 ASMMgr（UDP+TCP）
    两条规则（专用 Private 配置文件）。教材把防火墙排障放在维护步骤里，说明这是高频坑。
  conditions: 实验环境为 Windows 防火墙 Private 配置文件口径
  tags: [checklist, firewall, external-asm]

- id: p36
  title: 外部数据库硬边界——同脚本 ≤16 库；连接随脚本激活/去激活；32 位 ODBC 专用；Access 免凭据、SQL/Oracle 需凭据；存储过程需库支持
  type: rule
  source_pages: p376, p378, p384, p399, p433
  source_chapter: External Database lesson & How-Tos
  source_quote: |
    "In the same script, up to 16 different databases can be used … It is necessary to install an external ASM
    server" (p376)
    "The connection to the database is carried out with the script activation and the disconnection is realized
    during the script de-activation" (p378)
    "The feature is available only if the target database allows embedded procedures." (p384)
    "The ASM Server is not able to make a connecting using a 64-Bit ODBC Driver" (p399)
    "Take care, the ASM Server only allows a 32-bit connection" (p433)
  summary: |
    五条硬边界：①同一脚本最多连 16 个库；②连接生命周期=脚本激活到去激活（可用 adm_acd -salb 观察
    连接/断开，选项 60 看外部库连接状态）；③ODBC 必须 32 位（两处强调：64 位驱动连不上）；④凭据——
    SQL/Oracle 类库需在脚本里给用户名密码（USE_DATABASE 参数或 DB 连接串 UID/PWD），Access 类免凭据；
    ⑤存储过程调用仅当目标库支持嵌入式过程。读写（CALL 过程/写请求）还需 167 号许可（见 p32）。
  conditions: DSN 名必须与已建数据库对应——先建库后建 DSN（p380）
  tags: [rule, external-database, odbc, limits]

- id: p37
  title: SQL_RESULT 三值语义——SQL_SUCCESS / SQL_ERROR / SQL_NOT_FOUND
  type: rule
  source_pages: p385
  source_chapter: External Database lesson
  source_quote: |
    "The result of an instruction could be tested by the content of the variable SQL_RESULT who could receives
    the following values … SQL_SUCCESS: OK, there are some results • SQL_ERROR: KO, Bad Request •
    SQL_NOT_FOUND: Request OK, but there is no data for the selection" (p385)
  summary: |
    请求结果三值：SQL_SUCCESS=有结果集；SQL_ERROR=请求错误；SQL_NOT_FOUND=请求合法但无匹配行。
    脚本里以 IF SQL_RESULT=SQL_SUCCESS 分支处理"查到/没查到/查错"三种路径（实验中查无此人即走
    "unknown" 显示 + ISM 兜底）。
  conditions: 无
  tags: [rule, sql-result, script]

- id: p38
  title: 脚本本地变量配额表——STRING 1-64 / INTEGER 1-64 / REAL 1-32 / TIME 1-16 / DATE 1-16 / TIMESTAMP 1-16
  type: metric
  source_pages: p387
  source_chapter: External Database lesson / Mapping
  source_quote: |
    "STRING[%X] with X {1 to 64} do a mapping with the text. • INTEGER[%X] with X {1 to 64} do a mapping with
    the digital or Boolean • REAL [%X] with X {1 to 32} do a mapping with the real number • TIME[%X] with X
    {1 to 16} do a mapping with hours (hours/minutes/seconds) • DATE[%X] with X {1 to 16} do a mapping with
    dates (day/month/year) • TIMESTAMP[%X] with X {1 to 16} do a mapping with the dates and hours" (p387)
  summary: |
    数据映射配额：STRING 与 INTEGER 各 64 个（文本/数字与布尔）、REAL 32 个、TIME/DATE/TIMESTAMP 各
    16 个。外部库列值经 SQL_DATA 构件映射进对应类型的本地变量后才能参与脚本逻辑（比较、拼接、屏显）。
  conditions: 映射构件为 "SQL data" Building Block（p386）
  tags: [metric, mapping, variables]

- id: p39
  title: fetch 循环规则——SQL_START_FETCH/END_FETCH 成环；BREAK 提前退出；ROW_COUNT 计数；无 LIST 只留最后一行
  type: rule
  source_pages: p390-392
  source_chapter: External Database lesson / Fetch
  source_quote: |
    "Without the SQL_BREAK_FETCH BB, all the table records will be consulted • If you use a "LIST" variable
    … all records which match the request will be added to the LIST • If you don't use a "LIST" variable, only
    the last record will be kept (because it will overwrite the previous one) • With the SQL_BREAK_FETCH BB,
    it is possible to build a list and so to retrieve a precise number of records" (p391)
  summary: |
    取行规则：结果集在 SQL_START_FETCH DB[x] 与 SQL_END_FETCH 之间循环加载；SQL_BREAK_FETCH 满足
    条件即退出（例：SQL_ROW_COUNT<2 继续取、否则跳出）；行数记录在 SQL_ROW_COUNT。无 BREAK 时全
    表扫——配 LIST 变量收集全部匹配行，不配则只有最后一行存活（逐行覆写）。
  conditions: fetch 只在 SQL_RESULT=SQL_SUCCESS 后启动
  tags: [rule, fetch, sql-row-count]

- id: p40
  title: WHERE 子句/存储过程 INPUT 可用变量清单（26 项呼叫上下文变量）
  type: checklist
  source_pages: p383-384
  source_chapter: External Database lesson
  source_quote: |
    "Here are all call context variables you can used in the WHERE clause: CALLING, CALLTAG, CALLED,
    PRIORITY, SEQUENCE, PILOT_NUMBER, WAITING_ROOM_NUMBER, EXPECTED_WAITING_TIME, WAIT,
    AGENT_NUMBER, LAST_CALLED_AGENT LAST_CALLED_PILOT, LAST_CALL_DATE, LAST_CALL_STATE,
    CALL_PRIORITY[....], CALL_DISPLAY[....], STRING[....], INTEGER[....], DATE, DATE[....], TIME, TIME[....],
    TIMESTAMP[....], CHARACTERISTICS_LIST.SKILL[....].LEVEL, CHARACTERISTICS_LIST.SKILL[....].CHARACTER,
    CALL_PROFILE[....].SKILL[....].LEVEL, CALL_PROFILE[....].SKILL[....].CHARACTER" (p383)
  summary: |
    可用于 SELECT 的 WHERE 子句与存储过程 INPUT 模式的呼叫上下文变量全集（26 项）：核心八项
    CALLING/CALLTAG/CALLED/PRIORITY/SEQUENCE/PILOT_NUMBER/WAITING_ROOM_NUMBER/AGENT_NUMBER、
    等待与历史类（EXPECTED_WAITING_TIME/WAIT/LAST_CALLED_AGENT/LAST_CALLED_PILOT/LAST_CALL_DATE/
    LAST_CALL_STATE）、变量类（CALL_PRIORITY/CALL_DISPLAY/STRING/INTEGER/DATE/TIME/TIMESTAMP 带
    下标）与技能档案类（CHARACTERISTICS_LIST.SKILL[x].LEVEL/.CHARACTER、CALL_PROFILE 同构）。
  conditions: 存储过程 INPUT 模式用同一清单（p384）
  tags: [checklist, sql, context-variables]

- id: p41
  title: updateCalling 持久化原则——把 LAST_CALLED_AGENT 写入外部库，ASM 重启不丢"上次接听坐席"
  type: principle
  source_pages: p434, p447-452
  source_chapter: External Database How-To (MS SQL) step 3-5
  source_quote: |
    "This could be useful in case of ASM server reboot. Indeed, by default, the "last_called_agent" is kept
    only in the ASM server memory; which means that if the server reboots, all the data are lost. Using this
    procedure, the "last_called_agent" information is stored in a real database: so ASM server reboot has no
    impact on the "last_called_agent"." (p434)
    "The ASM Server reboot does not impact the "LAST_CALLED_AGENT"" (p452)
  summary: |
    原则：LCA 数据默认只活在 ASM 内存，重启即失。把存储过程（updateCalling，IN CALLING +
    IN LAST_CALLED_AGENT）嵌进脚本首段，每次呼叫把主叫号与上次接听坐席写入外部表；查询路径改为
    SELECT 该表——第 1 通呼叫表空走 ISM 并由过程写库，第 2 通起读库还原 LCA，重启 ASM 后依然有效
    （实验以 adm_acd 28 * 与表内容前后对照验证）。注意：教材示例过程不维护 Name（默认 'noname'）与
    VIP（默认 0）字段，需人工或另行扩展维护。
  conditions: 该模式需外部 ASM + 167 许可 + 32 位 ODBC；实验库 acr_sql 表 Customer（实验口径）
  tags: [principle, lca, persistence, stored-procedure]

- id: p42
  title: adm_acd 维护选项语义表——24 名单 / 25 内部库 / 28 呼叫动态数据 / 11 链路 / 14 连接类型 / 60 DB 连接 / 61 ACR_SQL 锁
  type: metric
  source_pages: p60, p141, p276, p339, p341-343, p394
  source_chapter: 全书维护页汇总
  source_quote: |
    "To see all the lists created: option 24 node N° … To a specific list: option 24 node N° List N°" (p60)
    "To see the internal DB management: option 25 node N° … To display a specific object: option 25 node N°
    Id N°" (p141)
    "option 60, when the ASM server is connected at least to 1 external database … option 61 (precise the lock
    ACR_SQL (167) availability)" (p394)
  summary: |
    `adm_acd <ASM IP> -salb` 选项语义：24=授权/非授权名单查看（可带节点号、名单号）；25=内部数据库
    查看（可带对象 ID）；28=呼叫动态数据 dump（28 * 全量，核 LAST_CALLED_AGENT 神器）；11=Agent List
    Builder 链路（外部 ASM 时显示 Windows 侧 IP）；14=ASM↔AFE 连接类型明细；60=外部数据库连接跟踪；
    61=ACR_SQL(167) 锁可用性。配套系统命令：ps -edf | grep alb、dhs3_init -R MAIN_AFE、hybvisu -f all。
  conditions: 均为原书出现过的选项口径
  tags: [metric, adm-acd, maintenance, troubleshooting]

- id: p43
  title: 实验口径：外部 ASM 双机地址与主机名——SoftPanel 10.2.T.20 (Main) / SoftPanel2 10.2.T.21 (Stand-By)
  type: metric
  source_pages: p362
  source_chapter: Duplicated External ASM How-To / Implementation
  source_quote: |
    "Consider that up to now, the external ASM Server which is running has the following IP@ (10.2.T.20;
    T=Table Number), host name: SoftPanel & has the "Main" role. The duplicated external ASM server that we
    are going to install has the following IP@ (10.2.T.21; T=Table Number), host name SoftPanel2 & has the
    "Stand-By" role." (p362)
  summary: |
    实验口径：主 ASM=10.2.T.20/SoftPanel（Main），备机=10.2.T.21/SoftPanel2（Stand-By），T 为组内表号；
    安装备机选 "Duplicate system"+"Stand-by ASM" 并填主 机名，主机改造为 Duplicated ASM/ASM Mode=Main
    并填备机名。验证脚本同步目录：C:\Program Files (x86)\Alcatel\Agent Selector Module\Script。
  conditions: 实验口径；生产按站点规划
  tags: [metric, lab, duplicated-asm]

- id: p44
  title: 实验口径：外部库表结构与账号——Access 表 Records / SQL 库 acr_sql 表 Customer / 登录 Brest
  type: metric
  source_pages: p396, p411-414, p418, p430
  source_chapter: External Database & MS SQL How-Tos
  source_quote: |
    "ID Name First_Name Calling Agent VIP … ID: recording number (Primary Key) … Agent: phone number of the
    preferential agent • VIP: calling inspection or not (1 or 0)" (p396)
    "Caller nvarchar (50) • Last_Agent varchar (8) • Name varchar (50) • VIP decimal (1, 0) … Value: NoAgent …
    Value: NoName … Value: 0" (p411-413)
    "Login name: Brest Select SQL Server authentication Password: alcatel … deactivate "Enforce password
    policy" • Default database: acr_sql" (p418)
  summary: |
    实验口径两套库：Access 库 acr.accdb 表 Records——ID (AutoNumber 主键)/Name/First_Name/Calling/Agent
    （优先坐席号）/VIP (Number, 1=VIP)，样例 3 行；SQL Server 库 acr_sql 表 Customer——Caller nvarchar(50)
    主键、Last_Agent varchar(8) 默认 'NoAgent'、Name varchar(50) 默认 'NoName'、VIP decimal(1,0) 默认 0；
    专用登录 Brest/alcatel（SQL Server 认证、关闭密码策略、默认库 acr_sql、映射 db 权限）；管理员 sa 密码
    Alcatel@1 为安装时自定义（教材 Notes 明言 "Password was defined during the MS SQL Server installation"，
    非出厂默认）。存储过程 updateCalling 由 D:\CCD_ACR\SQL Call Procedure.txt 载入。
  conditions: 实验口径；生产必须换强口令并收效权限（BOOK_OVERVIEW 批判节）
  tags: [metric, lab, database, sql]

- id: p45
  title: 多语言与技能矩阵的配置入口补充——域/技能可用 mgr 或 OmniVista 8770；坐席技能可用 Skill Matrix
  type: checklist
  source_pages: p37, p227
  source_chapter: Basic CCD matrix creation & Multi-Language How-To notes
  source_quote: |
    "This can also be managed by mgr or OmniVista 8770" (p37)
    "Add Skill French Level 9 … Can also be done by "Skill Matrix" (p227)
  summary: |
    配置入口补充：技能域除 CCS（CCSupervisor/Configurations/Advanced Call Routing/Skill）外也可由 mgr
    命令或 OmniVista 8770 管理；坐席技能除逐坐席配置外可用 Skill Matrix 批量视图。统计 Pilot 配置也可经
    CCSupervisor 修改（p36）；附件名单也可经 CCSupervisor 建（p33）。
  conditions: 多入口并存时注意配置源一致性（原书未展开冲突处理，推断需以单一入口为准）
  tags: [checklist, configuration-entry]

- id: p46
  title: IAA 改配与呼叫约束——改叶前先停用自动话务员；IAA 只能从外部呼入
  type: rule
  source_pages: p199, p211
  source_chapter: String handling How-To notes
  source_quote: |
    "First deactivate the Automatic Attendant Applications /Automated Attendant/Review-Modify Automated
    Attendant valid: FALSE" (p199)
    "Notes IAA can only be called from external" (p211)
  summary: |
    两条运行约束：修改 IAA 叶/树前须先把 Automated Attendant Valid 置 FALSE，改完再置 TRUE（避免配置
    生效期冲突）；IAA 接入号只能由外部呼叫进入（内呼不进话务员树）——设计内部分机引导流程时不能指望
    IAA，需用别的入口。
  conditions: 中继组 Automated Attendant 属性须为 YES（p180）
  tags: [rule, iaa, constraint]

- id: p47
  title: 脚本编辑器双模式与构件连接操作——Graphic/Text 双模；删连线=选红方块右键移除
  type: rule
  source_pages: p65, p69, p96, p100
  source_chapter: 各脚本 How-To
  source_quote: |
    "Select Graphic mode • Insert a Statement" (p65)
    "Complete the script Connect the building blocks Graphic mode / Text mode" (p69)
    "To Remove a link, select the red square, right click and remove" (p96, p100)
  summary: |
    编辑器操作规则：脚本有 Graphic（构件图）与 Text（文本）双模式，可切换对照；构件间用连线表达控制流，
    删除连线的方法是选中红方块右键移除；保存后须传输到 ASM 并在 ACR Pilot 上激活（f10 闭环）。
  conditions: 脚本名 ≤8 字符（p11 条目）
  tags: [rule, script-editor, gui]

- id: p48
  title: 混合呼叫选择实证口径——优先级不同房间先；相同优先级按 ACR Actual Waiting 分派
  type: metric
  source_pages: p281-282
  source_chapter: Miscellaneous How-To steps 7-8
  source_quote: |
    "Call Selection Priority: 9 for the Waiting Queue 31999700 • Call Selection Priority: 8 for the Waiting
    Room 31999703 … As the Call Selection Priorities are different, the calls parked in the Waiting Room are
    first considered." (p281)
    "At equal Priorities & ACR Actual Waiting set to FALSE (Default value), the lowest ISM cost is used. If the
    Parameter ACR Actual Waiting is set to TRUE, the highest real waiting time is used" (p282)
  summary: |
    实验口径（编号为实验值）：队列 31999700 优先级 9、房间 31999703 优先级 8→房间呼叫先被处理；两者
    同为 9→默认（ACR Actual Waiting=FALSE）按最低 ISM 成本，改 TRUE 按最长实际等待。修改入口
    CCSupervisor/Configurations/Call Flow mgt/Call Distribution 与 mgr RSI 参数。
  conditions: 与 p23/p24 语义互证
  tags: [metric, call-selection, lab]

- id: p49
  title: SQL Profiler 观测口径——过滤 LoginName Like "Brest" 观察 exec updateCalling
  type: rule
  source_pages: p467-469
  source_chapter: MS SQL 2016 Profiler How-To
  source_quote: |
    "Select "Events Selection" … activate "Show all events" activate "Show all columns" then click Column
    Filters … Select "LoginName" define Like "Brest" … make a call to the Statistic Pilot Check the exec
    updateCalling Check the declare @p1 …" (p468-469)
  summary: |
    观测方法：SQL Server Profiler 17 建跟踪（默认 Trace Properties），Events Selection 勾 Show all events/
    Show all columns，Column Filters 里 LoginName Like "Brest"；随后往统计 Pilot 打一通电话，应看到
    exec updateCalling 及 declare @p1 参数声明——这是验证"脚本→存储过程"链路的数据库侧证据。
  conditions: 登录 sa 或 Brest 均可建跟踪（实验口径账号见 p44）
  tags: [rule, profiler, verification]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 17 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 基础 CCD 矩阵搭建 | 有 | p02, p03, p04, p05, p06, p45 | 前缀动作码、矩阵编号全表、优先级取值、规则数量、技能/域/档案取值域、多配置入口 |
| task-02 | 脚本编写与调试工具链 | 有 | p07, p08, p09, p47 | LIT/PLTR 参数语义与公式、兜底链、编辑器操作 |
| task-03 | 授权/非授权名单规则 | 有 | p10, p11 | 名单硬上限、命名与大小写 |
| task-04 | 重定向/再分发规则 | 有 | p13, p14, p09 | 地址三形态、触发与退回语义、空列表兜底链 |
| task-05 | 直拨与 ACR 融合 | 有 | p15, p16, p17 | DICA 规则、单脚本约束、CALL_TYPE 骨架 |
| task-06 | 内部数据库定制路由 | 有 | p18, p19, p42 | 4000 条口径、Call Tag 数值、adm_acd 25 |
| task-07 | Call Tag 生成与传递 | 有 | p19, p20, p46 | 数值口径、转移覆盖原则、IAA 约束 |
| task-08 | 字符串处理 | 有 | p21, p27 | 五关键字语义表、屏显构件口径 |
| task-09 | 多语言语音引导 | 有 | p22 | 四条规则（40 语种/判定链/偏好/1 门技能） |
| task-10 | 综合脚本能力 | 有 | p23, p24, p25, p26, p27, p28, p48 | APPLY 语义、ISM 成本、IQUEUE、IVR/CLEAR、呼叫选择 |
| task-11 | 过滤器与统计 | 有 | p29, p30, p31 | AND/OR 口径、数据时效、Super/Hyper 规格 |
| task-12 | 外部 ASM 割接 | 有 | p32, p33, p34, p35 | 许可前提、角色语义、迁移规则、防火墙 |
| task-13 | 外部 ASM 双机 | 有 | p33, p43 | 双机复制语义、实验地址口径 |
| task-14 | 外部数据库机制 | 有 | p36, p37, p38, p39, p40, p42 | 硬边界、SQL_RESULT、映射配额、fetch、变量清单、adm_acd 60/61 |
| task-15 | Access 外部库实验 | 有 | p36, p44 | 32 位约束 + Access 表结构口径 |
| task-16 | MS SQL 侧准备 | 有 | p44, p49 | 表结构/账号口径 + Profiler 观测 |
| task-17 | MS SQL 外部库脚本 | 有 | p41, p37, p39 | LCA 持久化原则 + 结果测试 + fetch |

**覆盖结论**：17/17 全部有原则/数值类条目对应，无缺口。两点口径说明：
1. 容量/取值域数值已逐格对照原文（p18 容量表、p37-39 取值域、p387 配额表）；20 次 vs 21 次脚本执行、"3X800"、p196 字符串截取示例值等原文不一致处均照录并标注，未做"修正"。
2. 全部实验环境值（3xXXX 编号、Brest/alcatel、Alcatel@1、10.2.T.2x）标注"实验口径"；sa 密码明确注明为安装时自定义而非出厂值。
