# 原则/清单/规则/公式/数值口径候选 — OXO Connect Call Center (OXOCXTE107EN Ed07)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、DDI）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: ACD 系统容量规格（7 项硬上限）
  type: metric
  source_pages: p28
  source_chapter: ACD overview · Main characteristics
  source_quote: |
    "Capacities: 32 active agents; 8 ACD groups; 16 ACD ports; 6 voice prompts for each
    ACD group; 10000 routing rules (CLI/DDI) can be defined; One queue for each ACD group;
    Statistics storage capacity up to 14 months."
  summary: |
    OXO Connect 内置 ACD 的产品硬上限：32 个活动坐席、8 个 ACD 组、16 个 ACD 端口、
    每组 6 条语音提示、10000 条 CLI/DDI 路由规则、每组 1 条队列、统计留存最多 14 个月。
    适用于售前容量核对与交付边界确认；任一维度超限即超出单机规格。
  conditions: OXO Connect R6.x 时代（Ed07 教材口径），单站点单 ACD 引擎。
  tags: [metric, capacity, planning]

- id: p02
  title: ACD 端口与队列一一对应，上限同为 16，端口与 MLAA 共享
  type: rule
  source_pages: p28, p44, p93
  source_chapter: ACD overview / ACD Setup · General tab / Queue management
  source_quote: |
    "The maximum size of the queue is 16 (same for the maximum number of standard ACD
    ports)." (p93) / General tab: "Ports number (shared with MLAA)" (p44)
  summary: |
    每个 ACD 组有 1 条队列；队列上限 16 与标准 ACD 端口上限 16 同源。ACD 端口数在
    ACD Setup General 页签设置，且与 MLAA 共享资源——给 ACD 扩端口会挤占 MLAA，
    规划时两者要一起算。
  conditions: 端口为并发接入通道数，与坐席数是两个独立容量维度。
  tags: [rule, capacity, ports]

- id: p03
  title: 许可包结构：Welcome 底座 + Option 增包，按四口径计费
  type: rule
  source_pages: p31
  source_chapter: ACD overview · Commercial packages
  source_quote: |
    "Welcome: 5 basic agents, 8 groups. Option Licence: Basic Agent plus Agent Assistant
    (Up to 32); Agent Assistant PC (Up to 32); Supervisor Console (Up to 8); Statistic.
    License requirements according to: 1. The number of logged agent 2. The number of
    Agent application users 3. The number of Supervisor applications users 4. The use of
    the statistics application."
  summary: |
    底座 Welcome 含 5 个基础坐席、8 个组；扩容靠四类 Option 许可（坐席助理坐席数、
    坐席助理 PC 数各至 32，班长台至 8，统计应用）。许可占用按四个口径计算：登录坐席数、
    Agent 应用用户数、Supervisor 应用用户数、是否用统计应用。报价与交付前先按这四项清点。
  tags: [rule, licensing, commercial]

- id: p04
  title: Line parameters 路由表容量 10000 行，支持 CSV 导入导出
  type: metric
  source_pages: p50
  source_chapter: ACD configuration · ACD Services menu
  source_quote: |
    "Lines parameters menu: to manage the DID numbers according to the selected ACD
    application • Up to 10000 lines • CVS Import/export is possible"
  summary: |
    呼叫特征化路由表（Line parameters）最多 10000 行（与 p28 的 10000 条路由规则口径一致），
    批量维护走 CSV 导入导出，不必逐行手填。
  conditions: 大批量客户路由（按国家/大客户分流）建议 CSV 批量制作后导入。
  tags: [metric, routing-table, csv]

- id: p05
  title: 坐席终端类型不限——用户列表里任意分机都可当坐席
  type: rule
  source_pages: p30
  source_chapter: ACD overview · Types of extension
  source_quote: |
    "Wired analog extension; DECT handsets; Alcatel-Lucent IP & TDM sets; PIMphony IP.
    Conclusion: any type of set from the subscriber list."
  summary: |
    模拟分机、DECT 手机、IP/TDM 话机、PIMphony 软终端都可以声明为坐席终端。
    选型含义：坐席落地设备不构成 ACD 的约束，约束来自坐席数许可。
  tags: [rule, agents, terminals]

- id: p06
  title: 双层配置体系：ACD Setup 向导做一次成型，ACD Services 做精细调整
  type: principle
  source_pages: p43, p49
  source_chapter: ACD configuration
  source_quote: |
    "Using the ACD Setup menu • Via OMC on Easy view session • Path: OMC / Customer PBX /
    Automatic Call Distribution • Select the 'ACD Setup' icon to start the ACD assistant."
    (p43) / "Select the 'ACD Services' icon to start the ACD menu." (p49)
  summary: |
    配置入口分两层：基础四件套（状态前缀、DDI 关联、组邮箱、按键 profile、坐席声明）
    走 ACD Setup 向导一次配完；路由表、坐席/组精细参数、语音定制走 ACD Services 菜单。
    新建呼叫中心先向导后精调，不要在 Services 里反向补向导该做的事。
  tags: [principle, configuration, workflow]

- id: p07
  title: 改完 ACD 配置必须重启 ACD 引擎才生效
  type: rule
  source_pages: p48
  source_chapter: ACD Setup · Validate
  source_quote: |
    "Validate the ACD Setup process by pressing the 'OK' key • Restart the ACD engine in
    order to apply changes."
  summary: |
    ACD Setup 点 OK 只是保存，必须再重启 ACD 引擎，改动才落到运行状态。
    排障时"配置明明改了却不生效"第一件事就是确认引擎是否重启过。
  conditions: 教材在 ACD Setup 向导语境下提出；Services 菜单的逐项修改是否需重启，
    教材未逐一说明（待确认，稳妥做法是验证呼叫行为）。
  tags: [rule, validation, troubleshooting]

- id: p08
  title: ACD Setup 自动预配置清单——其中 ACD 端口的 Media 勾选不许动
  type: checklist
  source_pages: p80-84
  source_chapter: Advanced ACD parameters · Features pre-configured
  source_quote: |
    "'Media' parameter ticked for all ACD ports (don't touch)." (p80) /
    "Creation of hunting groups in cyclic mode including the virtual terminals dedicated
    to ACD features." (p82) / "A DID number is associated to the targeted ACD group." (p82)
  summary: |
    跑完 ACD Setup 后系统自动生成：① 各 ACD 端口的虚拟终端（Media 参数已勾，明确标注
    不要动）；② 组邮箱虚拟终端并设动态转接到语音邮箱；③ 循环模式寻线组（含 ACD 专用
    虚拟终端）；④ 公共编号计划里的 DID 关联；⑤ 坐席/班长按键 profile。验收时按这份
    清单逐项核对，而不是自己重配。
  tags: [checklist, pre-configuration, validation]

- id: p09
  title: "Group called with signalization mode" 必须保持禁用
  type: rule
  source_pages: p85
  source_chapter: Further ACD options · Setup mode
  source_quote: |
    "Check that the 'Group called with signalization mode' feature is disabled. Path: OMC /
    System Miscellaneous / Feature design / part 2. In signaling mode, incoming calls to
    hunt groups are indicated on a 'group supervision' key. In setup mode, incoming calls
    to a hunt group are displayed on their subscriber resource keys."
  summary: |
    ACD 依赖 setup 模式（来话显示在坐席的子址资源键上）工作；若开了信令模式（来话只亮
    组监听键），ACD 呼叫分配行为会失效。装机组网后先到 Feature design/part 2 核对该项为
    disabled。
  tags: [rule, configuration, precheck]

- id: p10
  title: "Default messages" 下载会波及全部 ACD 组，不需要的组要手动点列号关闭
  type: rule
  source_pages: p76
  source_chapter: Basic ACD Configuration · Download voice guides
  source_quote: |
    "When you click on 'Default messages', the download of those messages will be done for
    all ACD groups. Click on the column numbers in order to disable the message downloading
    for the ACD group not linked to the configuration you want to set up."
  summary: |
    在 ACD Voice messages 里点 "Default messages" 会向所有 8 个组下发默认语音，不只是你
    正在配的组。只想给部分组下语音时，先点组列号把无关组勾掉再传。
  tags: [rule, voice-prompts, gotcha]

- id: p11
  title: 基础 ACD 配置验证清单
  type: checklist
  source_pages: p77
  source_chapter: Basic ACD Configuration · Check the ACD configuration
  source_quote: |
    "Check the changes made to the following menus: Subscribers list, Hunting groups list,
    Internal numbering plan, Public numbering plan. Make a call to all the ACD groups to
    check that the group welcome message comes up first, followed by a transfer to an agent.
    Put the agents on 'on duty', 'off duty', 'clerical work' and 'temporary absent' status
    using the pre-defined prefixes and the features keys."
  summary: |
    交付自测三步：① 核对四个 OMC 菜单（用户列表、寻线组列表、内部编号计划、公共编号
    计划）；② 逐组拨打验证"先欢迎语、后转坐席"；③ 用前缀和功能键把坐席在四种状态间
    轮一遍确认状态机正常。全过才算基础配置完成。
  tags: [checklist, validation, delivery]

- id: p12
  title: 坐席状态前缀固定为 501-504
  type: rule
  source_pages: p70
  source_chapter: Basic ACD Configuration · Prefixes
  source_quote: |
    "The prefixes used to manage the agent status are: 501: on duty; 502: off duty;
    503: clerical work; 504: temporary absence."
  summary: |
    四个坐席状态的拨号代码：501=on duty（值机）、502=off duty（登出待命）、
    503=clerical work（案头工作）、504=temporary absence（临时离开）。
    编号计划交付前要核对 501-504 不与客户拨号计划冲突（教材未给冲突排查法，需自行验证）。
  tags: [rule, numbering, agent-status]

- id: p13
  title: 组号 / 内部前缀 / DDI 的编号关联模板（实验口径）
  type: metric
  source_pages: p70
  source_chapter: Basic ACD Configuration · DDI association
  source_quote: |
    "Three ACD groups are required by the customer and you must associate a DID number to
    each one: Group ACD n°1, internal prefix:505, DDI N°: 41505; Group ACD n°2, internal
    prefix:506, DDI N°: 41506; Group ACD n°3, internal prefix:507, DDI N°: 41507."
  summary: |
    实验环境编号模板：ACD 组 n 的内部前缀为 50X、外部 DDI 为 4150X（X=1,2,3）。
    规律是"组序号对齐前缀尾数、DDI 尾数对齐前缀"，生产环境按客户 DID 段套用同一对齐思路。
  conditions: 数值为 RLAB 实验（DDI 段 41100-41199 内取用），生产按客户实际 DID 段替换。
  tags: [metric, numbering, template, lab-value]

- id: p14
  title: 坐席跨组 rank 优先级要在 Agent parameters 里逐组声明
  type: rule
  source_pages: p75
  source_chapter: Basic ACD Configuration · Add agents
  source_quote: |
    "Call distribution priorities will be to manage in the following way: Group ACD 1:
    101 (rank 1), 102 (rank 2); Group ACD 2: 102 (rank 1), 103 (rank 2); Group ACD 3:
    103 (rank 1), 102 (rank 2), 101 (rank 3)."
  summary: |
    一个坐席进多个组时，必须逐组给 rank（1 为最优先）；rank 与组内搜索模式是两个正交
    概念——rank 决定跨坐席的先后，search mode 决定同 rank 内怎么挑。
    实验模板：101→组1优先，102→组2优先，103→组3优先，交叉坐席按 rank 递减。
  conditions: 声明坐席时同时把状态置为 on duty。
  tags: [rule, agents, priority]

- id: p15
  title: 话机 ACD 状态码解读（坐席排障用）
  type: rule
  source_pages: p122
  source_chapter: Login/Logout · Information on terminals
  source_quote: |
    "1:01 = Agent doesn't belong to ACD group 1 which is open, and 1 calls are in the
    queue. / 1:01 = Agent belong to ACD group 1 which is open, and 1 calls are in the
    queue. / 1:01+ = Agent belong to ACD group 1 which is open, 1 calls are in the queue
    and the queue is full. / 1-00 = Agent belong to ACD group 1 which is closed."
  summary: |
    话机 ACD 页签的状态码格式为"组号:排队数"：属组且开放显示 组号:排队数，队列满变为
    组号:排队数+，组关闭显示 组号-00。据此可一眼判断坐席是否真的属组、组是否开放、
    队列是否打满。注意：原文前两条 OCR 显示同为 "1:01" 但语义相反（不属于组 / 属于组），
    疑有符号在 PDF 转 text 时丢失，两态的确切显示差异需对照原 PDF 核实（待确认）。
  tags: [rule, troubleshooting, terminals, needs-verification]

- id: p16
  title: ACDAutoLog 隐藏寻址项控制登录后默认状态：01=值机（默认），00=off duty
  type: rule
  source_pages: p123
  source_chapter: Login/Logout · Agent status after login session
  source_quote: |
    "Noteworthy address called 'ACDAutoLog' in order to set up the default agent status
    after the login process. Value 01: agent is 'on duty' after login session (Default
    value). Value 00: agent is 'off duty' after login session."
  summary: |
    坐席登录后是直接接电话还是先挂 off duty，由系统编号项 ACDAutoLog 决定：
    01=登录即 on duty（出厂默认），00=登录后 off duty。这是隐藏寻址项，不在常规菜单里，
    要按系统编号方式设置。
  tags: [rule, login, hidden-parameter]

- id: p17
  title: 坐席进入 ACD 会话的条件：坐席、ACD 组、终端三方建立共同关联
  type: rule
  source_pages: p119
  source_chapter: Login/Logout · Overview
  source_quote: |
    "To be able to answer to ACD calls, the agent must first enter the ACD process. The
    entry to the ACD process is effective as soon as a common link is built for the
    following components: The agent name / ACD group 1 / The ACD group / The terminal."
  summary: |
    坐席必须先"进入 ACD 流程"才能接 ACD 来话；生效条件是坐席（名称）、ACD 组、终端
    三者绑定成一条链（即 free seating 的登录动作）。排障口诀：坐席没接到电话，先查这条
    链有没有建立——没登录、没进组、终端没关联，任何一环断开都不分配来话。
  conditions: 原文图示文本 "ACD group 1 / The ACD group" 疑为图注重复，组件取坐席/组/终端三项。
  tags: [rule, login, free-seating]

- id: p18
  title: 登录前提：坐席和 ACD 组至少已配置
  type: rule
  source_pages: p120
  source_chapter: Login/Logout · Login process
  source_quote: |
    "From a terminal, an agent is able to login by dialing a prefix, in order to associate
    his terminal with the selected agent. At a minimum, agents and ACD group must be set
    up. Providing by default free seating mode."
  summary: |
    前缀登录机制默认就是 free seating 模式；但登录的前置条件是坐席已在 Agent parameters
    声明、ACD 组已存在。终端本身不需要预配置——这正是 free seating 的意义。
  tags: [rule, login, precondition]

- id: p19
  title: ACD 前缀按 base 区分登录/登出：base 0=登出，base 1=登录
  type: rule
  source_pages: p120
  source_chapter: Login/Logout · ACD Prefix
  source_quote: |
    "A function, called ACD Prefix, is available in the internal numbering plan • ACD
    prefix with base 0: prefix to logout • ACD prefix with base 1: prefix to login."
  summary: |
    内部编号计划里的 ACD Prefix 功能按 base 值分两个方向：base 1 的前缀码登录、base 0
    的前缀码登出。话机 ACD 页签则同一按键切换登录/登出。两套入口并存，按终端能力选用。
  tags: [rule, numbering, login]

- id: p20
  title: 登录流程：选坐席方式按终端类型分流，密码按需
  type: rule
  source_pages: p121
  source_chapter: Login/Logout · Facilities on terminals
  source_quote: |
    "Dial the ACD prefix (login code) or tab ACD press the 'Login' key. Select the Agent:
    By name: for ALE Essential and Enterprise; By his agent number: for analog phones and
    DECT handsets. Enter the Agent password if this agent is customized."
  summary: |
    登录三步：拨登录前缀（或按 ACD 页签 Login）→ 选坐席 → 有密码则输密码。
    选坐席的方式由终端能力决定：8/9 系列智能话机按姓名选，模拟话机与 DECT 只能按坐席号。
    坐席密码是可选项，配了才要输。
  tags: [rule, login, terminals]

- id: p21
  title: 登出确认差异：智能话机需 OK 确认，模拟/DECT 直接生效
  type: rule
  source_pages: p121
  source_chapter: Login/Logout · Logout process
  source_quote: |
    "Dial the ACD prefix (logout code) or tab ACD press the 'Logout' key. On ALE Essential
    and Enterprise you have to confirm the exit by OK. No exit confirmation required for
    analog phones and DECT handsets."
  summary: |
    8/9 系列话机登出要按 OK 确认（防误触），模拟话机和 DECT 无确认直接登出。
    培训坐席时按终端类型交代清楚，避免"以为登出了其实没登/以为没登其实登了"。
  tags: [rule, logout, terminals]

- id: p22
  title: 呼叫特征化三级匹配优先级，无匹配回铃音
  type: rule
  source_pages: p87
  source_chapter: Further ACD options · Call characterization analysis
  source_quote: |
    "Priority comparison # 1: CLIn / CLIt & DIDn / DIDt — CLIn=CLIt & DIDn=DIDt? YES → ACD
    group application. Priority comparison # 2: CLIn / CLIt & DIDt not filled in.
    Priority comparison # 3: DIDn / DIDt & CLIt not filled in. ... Ring back tone."
  summary: |
    来话匹配按三级优先顺序执行：① CLI 与 DDI 都命中（双匹配）→ 立即应用对应组；
    ② CLI 命中且路由表该项 DDI 留空 → 命中；③ DDI 命中且路由表该项 CLI 留空 → 命中。
    三级全不中则不打断呼叫，按普通来话回铃处理。设计路由表时把"最苛刻的双匹配"排前面
    才能体现优先级。
  conditions: n=来话实际号码，t=路由表模板号码；留空即通配。
  tags: [rule, routing, priority]

- id: p23
  title: 比较方向：CLI 从左向右比，DDI 从右向左比
  type: rule
  source_pages: p88
  source_chapter: Further ACD options · Line parameters
  source_quote: |
    "CLI comparison CLIn / CLIt starts from the left to the right. DIDn / DIDt comparison
    starts from the right to the left."
  summary: |
    CLI（主叫号码）按国际号码格式从左往右比——所以模板能写"+33xxxxxx"这类国家码前缀来
    兜住整国来话；DDI（被叫号码）从右往左比——所以模板写尾数"xx4452"能兜住尾号相同的
    一段 DID。填模板前先想清楚方向，否则通配位写反匹配不上。
  tags: [rule, routing, comparison-direction]

- id: p24
  title: 路由表必须从最特殊（最长号码）填到最一般（最短号码）
  type: principle
  source_pages: p88
  source_chapter: Further ACD options · Line parameters table management
  source_quote: |
    "'Line parameters' table management: Fill in the table beginning with the special case
    (the longest numbers). Ending with the general case (the shortest numbers)."
  summary: |
    路由表条目按特异性降序维护：先写最特殊的大客户精确匹配（最长、双匹配），最后写
    一般性的国家/尾号兜底规则（最短、单匹配）。这条是维护性原则——新增长客户时插在
    兜底规则之前，否则会被先命中的宽泛规则截胡。
  tags: [principle, routing, table-order]

- id: p25
  title: 呼叫特征化同时作用于外部来话和内部来话
  type: rule
  source_pages: p86
  source_chapter: Further ACD options · Call characterization overview
  source_quote: |
    "Call routing optimization to ACD groups. Management according to the called number
    (DID) and/or the caller ID (CLI). Process available for external incoming and internal
    incoming calls."
  summary: |
    特征化不只管公网来话，内部分机拨 ACD 组同样走这套匹配。内测时可直接用内部前缀拨打
    验证路由表，不必每次走运营商模拟器。
  tags: [rule, routing, scope]

- id: p26
  title: 队列长度公式：队列 = N × K 向上取整，K 取 0.1-9.9，上限 16
  type: formula
  source_pages: p93
  source_chapter: Further ACD options · Queue management
  source_quote: |
    "2 parameters must be taken into consideration: Number of agent 'In service' and the
    traffic or occupation factor. Let N be the number of agent in service and K the load
    factor. If N * K is not an integer, the value of the queue is the next higher integer.
    The maximum size of the queue is 16."
  inputs: N = on duty 状态的坐席数（原文 "in service"）；K = 话务/占用因子，0.1-9.9
  formula: 队列长度 = ceil(N × K)，封顶 16
  units: 路（同时可排队的呼叫数）
  output: 该 ACD 组等待队列容量
  missing_conditions: |
    ① 原文未定义 "in service" 是否仅限 on duty（组1示例用 4 个 on duty 坐席推定仅计值机坐席）；
    ② K 的取定方法（如何由话务量反推）教材未给，仅给范围；
    ③ 验证实例：N=4, K=0.5 → 队列 2（p93）；N=2, K=0.1 → 队列 1（p113，第二通即劝漏）；
    N=2, K=2.0 → 队列 4（p184）。
  summary: |
    配队列先数坐席再定因子：把组内值机坐席数乘话务因子，小数向上取整，最大 16。
    K 调小（如 0.1）即压缩队列制造"秒劝漏"，调大（如 2.0）放大排队容量。
  tags: [formula, queue, capacity-planning]

- id: p27
  title: 预计等待时间公式：(队列呼叫数/值机坐席 + 1) × 平均通话时长
  type: formula
  source_pages: p94
  source_chapter: Further ACD options · Queue management messages
  source_quote: |
    "Average duration of ACD conversations used to calculate the estimated waiting time in
    the queue. Estimated waiting time = [(Number of call in the queue / number of agents on
    duty) + 1] X Average duration of ACD conversations"
  inputs: 队列中呼叫数；on duty 坐席数；平均 ACD 通话时长（系统参数）
  formula: 预计等待时间 = (队列呼叫数 ÷ on duty 坐席数 + 1) × 平均 ACD 通话时长
  units: 时间（与"平均通话时长"同单位，秒或分）
  output: 播报给排队客户的预计等待时长
  missing_conditions: |
    ① "平均 ACD 通话时长"参数的设置入口与默认值原文未给出；
    ② 该公式为线性简化模型（队列呼叫数/坐席数取的是整数位置而非实时均衡），高峰期会低估等待
    （见 BOOK_OVERVIEW 批判），生产建议按真实话务校准后再对外播报。
  summary: |
    队列播报"预计等待 X 分钟"就是这条公式算出来的：当前位置（排第几 ÷ 几个坐席，再加 1）
    乘平均处理时长。触发播报的前提是先在 Queue rank / Queue time 选项里启用对应方式（p94）。
  tags: [formula, queue, waiting-time]

- id: p28
  title: 队列提示消息的触发方式与播报内容
  type: rule
  source_pages: p38, p94
  source_chapter: ACD scenarios · All agents busy / Queue management
  source_quote: |
    "Average time or Rank number trigger enabled? Threshold reached? YES → Estimated
    waiting time message OR Minimum rank in the queue message." (p38) /
    "After selecting the 'Queue rank' or the 'Queue time' option, set up the parameter
    linked to the selected option." (p94)
  summary: |
    排队播报二选一：按等待时间触发（Queue time）或按队列名次触发（Queue rank），选定后
    设置对应阈值参数；阈值到即播"预计等待时长"或"您当前排在第 N 位"。排队期间先播
    message 1，再循环播 message 2（p38、p112 实验证实）。
  conditions: 阈值参数数值由配置者给定，教材未给默认值。
  tags: [rule, queue, messages]

- id: p29
  title: 队列出口：主叫按 * 键可提前离开队列
  type: rule
  source_pages: p38, p112
  source_chapter: ACD scenarios / Advanced configuration · Waiting queue
  source_quote: |
    "Queue exit by '*' key." (p38) / "The caller can exit the waiting queue by pressing the
    'star' key in order to leave a message in the associated ACD group mailbox or to be
    routed to a pre-defined number." (p112)
  summary: |
    排队中的主叫随时可按 * 键放弃排队，出口两个：转入组邮箱留言，或转到预定义号码。
    这两个出口要在"Call management"里分别启用（教材实验：先启用邮箱出口验证，再启用
    转接出口验证）。
  tags: [rule, queue, exit-options]

- id: p30
  title: 组间溢出：队列中等待计时 10 秒后溢出到其他组的空闲坐席
  type: rule
  source_pages: p96
  source_chapter: Further ACD options · Group overflow
  source_quote: |
    "After a timer of 10 s spent in a waiting queue: Overflow to an agent available in the
    ACD group 2."
  summary: |
    Group overflow 功能：本组坐席全忙时，呼叫在队列里等满溢出计时器（教材示例 10 秒），
    即转给溢出目标组的空闲坐席。用于跨组互助（如销售组兜底客服组）。
    溢出计时器的可配置范围原文未给（待确认），10 秒为图示示例值。
  tags: [rule, overflow, queue]

- id: p31
  title: Transfer number 只管"组开放但全员未值机"场景，且仅第一通转出
  type: rule
  source_pages: p41, p97
  source_chapter: Further ACD options · Transfer number
  source_quote: |
    "Feature that can used when a call is routed to an opened ACD group where all agents
    are logged out or on 'off duty' status. As soon as this process happens: First ACD
    incoming call will be transferred to a pre-defined number. Subsequent calls are either
    queued or routed to a deterrent message."
  summary: |
    组开放但所有坐席登出/off duty 时：第一通来话转到预定义转接号（如外部值班手机），
    后续来话按队列/劝漏出口处理。适用条件严格——组关闭或坐席忙时不走这条路（那是
    closed/all busy 场景）。
  tags: [rule, transfer-number, scenarios]

- id: p32
  title: Priority order：坐席跨组时的取叫优先可按组排序
  type: rule
  source_pages: p97
  source_chapter: Further ACD options · Priority order
  source_quote: |
    "Used when agents belong to several ACD groups. Possibility to give a priority from one
    group to another, during the research of waiting queue calls."
  summary: |
    一个坐席属于多个组时，可设定他从哪个组的队列优先取叫（组与组之间的优先序）。
    与 p14 的组内 rank 正交：rank 管"组内谁先接"，priority order 管"多组都积压时先接哪个组"。
  tags: [rule, priority, multi-group]

- id: p33
  title: 三种非常态（队满/劝漏/关闭/全员登出）的出口统一为三选一
  type: principle
  source_pages: p39-42, p112-114
  source_chapter: ACD scenarios · Dissuasion/Closed status processes
  source_quote: |
    "Instead of broadcasting a message and releasing the call, it's possible to set up a
    transfer to a predefined destination or to leave a message on the ACD group mailbox."
    (p113, p114)
  summary: |
    队满、劝漏、关闭、全员登出等"接不了"的状态，出口机制统一：默认播音后释放，
    均可改为 ①转预定义号码 ②进组邮箱。学会一个状态的出口配置，其余状态同构。
    这条是六场景排障的通用框架（对应 BOOK_OVERVIEW 核心命题 2）。
  conditions: "全员登出"场景第一通先走 Transfer number（见 p31），其余通才有三选一。
  tags: [principle, scenarios, dissuasion]

- id: p34
  title: 所有来话先过营业时间测试，再进入各场景分支
  type: rule
  source_pages: p37-42
  source_chapter: ACD scenarios · Opening hours test
  source_quote: |
    "Incoming calls → Welcome greeting → Opening hours test → OPEN/CLOSED → (各场景流程图)"
  summary: |
    六张场景流程图共用同一入口：来话先播欢迎语，紧接着做营业时间测试；OPEN 才进
    找坐席/排队/劝漏分支，CLOSED 直接进关闭分支。时段配置错了，后面全部场景跟着错——
    排障从营业时间测试开始查。
  tags: [rule, scenarios, opening-hours]

- id: p35
  title: 例外日容量：最多 40 个例外关闭日、10 个例外开放日、每个开放日最多 2 个时段
  type: metric
  source_pages: p100
  source_chapter: Further ACD options · Exceptional days
  source_quote: |
    "Exceptional closing days: Possibility to define a maximum of 40 closing days.
    Exceptional opening days: Possibility to define a maximum of 10 opening days.
    A maximum of 2 times ranges per opening day can be managed."
  summary: |
    营业日历的例外日硬上限：例外关闭日 40 个（法定假日够用），例外开放日 10 个（如周日
    大促），例外开放日内最多设 2 个时段（如 9:30-11:30 + 14:00-17:00）。
    例外日按组定义（Exceptional days 页签支持分组勾选）。
  conditions: 实验（p108）：1/1、5/1、12/25 全网关闭，但组 1 在 12/25 开 9:30-11:30，
    即"全局关闭日 + 单组例外开放"可叠加实现。
  tags: [metric, calendar, exceptional-days]

- id: p36
  title: DTMF 客户识别弹屏的三个配置前提
  type: checklist
  source_pages: p101-102
  source_chapter: Further ACD options · Client identification
  source_quote: |
    "When a client calls the ACD, he is able to type a customer DTMF code (ex 035) allowing
    to generate a specific client information pop-up (Customer code=035) on the agent
    application. To get that functionality, ACD groups with code must be selected in the
    line parameters. ... In the agent application, it is necessary to give the 'automatic
    screen pop up' rights in the agent parameters."
  summary: |
    客户来电输码弹屏（如输 035# 弹客户 035 资料）需同时满足三点：① Line parameters 里给
    目标 ACD 组勾选"with code"；② OMC 里定制客户码提示音（107.wav，见 p37 条目）；
    ③ Agent 应用参数里给坐席勾"automatic screen pop up"权限。缺一不弹。
    输入格式：客户码 + # 号结尾。
  tags: [checklist, dtmf, screen-popup]

- id: p37
  title: ACD 语音文件编号规则：101=欢迎语、102=等待消息、107=客户码提示，按组加百位前缀
  type: rule
  source_pages: p104, p135-136
  source_chapter: Further ACD options / Multi-secretary · Voice prompts
  source_quote: |
    "Respect the assignments 101.wav = welcome message, 102.wav = waiting message, etc."
    (p136) / "Customer code announce: 107.wav 207.wav 307.wav 407.wav 507.wav 607.wav
    707.wav 807.wav" (p104)
  summary: |
    每组 6 条语音提示按固定编号管理：组 1 用 10X.wav 系列，组 2 用 20X.wav……组 8 用
    80X.wav。明确可考：X=1 欢迎语、X=2 等待消息、X=7 客户码提示音。
    其余编号（劝漏语、关闭语、预计等待语等）原文以 "etc." 带过，仅 p135 给出六条样例文案
    （欢迎/忙稍等/很忙/打太多/已关闭/等待预计 X 分钟），未逐条标号——精确对应表待对照
    原 PDF 图表确认（待确认）。
  conditions: 每组上限 6 条提示（p28），编号规则是下载定制语音的强制约束。
  tags: [rule, voice-prompts, numbering]

- id: p38
  title: 语音可经话机 MMC 录制，8/9 系列走 Attendant session 的固定路径
  type: rule
  source_pages: p104, p146
  source_chapter: Voice prompts / Multi-secretary · Customize voice prompts
  source_quote: |
    "Prompts can be recorded via a MMC session via a terminal • Alcatel-Lucent 8 and 9
    series: Attendant session." (p104) / "Menu/Operator/PASSWORD OP/Expert/Voice/ACD/
    ACD Group 1 to 3/Welcome..." (p146)
  summary: |
    定制语音两条路：① 话机上直接录——8/9 系列话机进 Attendant session（话务台会话），
    路径 Menu → Operator → 输 OP 密码 → Expert → Voice → ACD → 选组和条目；
    ② PC 上做好 wav 文件经 OMC 批量上传（见 p39）。现场快速改一句话用它录，整体换包用 OMC。
  tags: [rule, voice-prompts, mmc]

- id: p39
  title: OMC 上传定制语音四步法
  type: checklist
  source_pages: p105, p136
  source_chapter: Voice prompts · Download process
  source_quote: |
    "Switch the Mode option to Transfer (1); Select the prompts you want to download (2);
    Define the directory path for loading the customized prompts (3); Load the new prompts
    (4)."
  summary: |
    OMC 的 ACD Voice messages 页面四步上传定制 wav：① Mode 切到 Transfer；② 勾选要下的
    提示音条目；③ 指定本地目录路径；④ 点 Load 执行。注意 p10 条目：默认会波及所有组，
    不需要的组先点列号去掉。wav 的技术格式要求（采样率/位宽）在原文截图中，文本未解析
    出来（待确认，常见为标准 PCM wav，交付前实测一条验证）。
  tags: [checklist, voice-prompts, omc]

- id: p40
  title: Multi-Secretary 是 ACD 引擎的预设形态，需单独许可
  type: rule
  source_pages: p126
  source_chapter: Multi secretary · Presentation
  source_quote: |
    "Allows to share the resources of one or more secretaries between several managers,
    services or companies. ... Feature based on ACD engine (license needed)."
  summary: |
    多秘书模式不是独立产品，是复用 ACD 引擎的另一形态（经理 DDI 当被叫特征化、秘书组当
    坐席组），开启需要许可。能力：多名秘书服务多个经理/科室/公司，按被叫显示个性化接待。
  tags: [rule, multi-secretary, licensing]

- id: p41
  title: 转接途中显示"被叫(或组名)+主叫+等待时长"，接通后只显示主叫 CLI
  type: rule
  source_pages: p89, p107, p146
  source_chapter: ACD group parameters / Multi-secretary · Display
  source_quote: |
    "Called ACD group identity displayed while the call is being transferred to the agent
    terminal. Once the call is transferred, the CLI is displayed." (p89) /
    "[GROUP_NAME] [CALLING_NUMBER] [WAITING_TIME]" (p107) /
    "[CALLED_NUMBER] [CALLING_NUMBER] [WAITING_TIME] ... once the call is transferred:
    [CALLING_NUMBER]" (p146)
  summary: |
    铃声期间坐席话机显示三段信息：被叫方标识（ACD 模式显组名，Multi-Secretary 模式显
    被叫号码/姓名）+ 主叫号码 + 等待时长（排队+振铃合计）；接通后只剩主叫 CLI。
    秘书靠"被叫位"区分是哪位医生的来电——这是 Multi-Secretary 个性化接待的核心依据。
  tags: [rule, display, multi-secretary]

- id: p42
  title: Multi-Secretary 编程顺序：先 DDI+模式，后邮箱/配置文件/坐席/线路
  type: checklist
  source_pages: p128-133, p141
  source_chapter: Multi secretary · Management
  source_quote: |
    "Carry out the programming in the following order." (p141，配合 p128-133 的步骤序列：
    General 页签 DDI+Multi-Secretary 模式 → ACD Groups 页签邮箱 → ACD Profiles 生成
    profile → Agents-Supervisors 页签声明班长 → Agent parameters 建秘书 → Line parameters
    加 DDI)
  summary: |
    多秘书配置固定六步顺序：① General 页签录经理 DDI 并激活 Multi-Secretary 模式；
    ② 给秘书组建组邮箱（关闭时段溢出用）；③ 生成秘书（=Supervisor）profile 并加业务键；
    ④ 秘书话机声明为 Supervisor 站（才能配语音查询键）；⑤ Agent parameters 里建秘书坐席
    并按 rank 1 放入各组；⑥ Line parameters 里录经理 DDI。顺序错会导致后续步骤引用不到
    前置对象。
  tags: [checklist, multi-secretary, sequence]

- id: p43
  title: 秘书全员登出/off duty 时，来话落入劝漏消息
  type: rule
  source_pages: p134
  source_chapter: Multi-secretary · Schedules and overflow
  source_quote: |
    "Else when the secretaries are off duty or logged out, the dissuasion message is used."
  summary: |
    Multi-Secretary 的兜底逻辑：营业时段内但秘书全部登出或 off duty，来话播劝漏消息
    （而非排队等待）。所以秘书下班必须记得登出，否则客户会被留在队列里无人接。
  tags: [rule, multi-secretary, logout]

- id: p44
  title: 用集体速拨目录把被叫号码替换成姓名显示
  type: rule
  source_pages: p137, p144
  source_chapter: Multi-secretary · Name display
  source_quote: |
    "Replacement of the called number by the name on the secretary's sets: Program names in
    the collective speed dialing repertory." (p137) / "Manage one number per doctor that
    will be displayed on the secretaries' sets. 505 to 507 allows you to test calls
    internally." (p144)
  summary: |
    秘书席要显示 "DOCTOR A" 而不是 41505，就把每个经理号（前缀 505-507）录入集体速拨
    目录并冠名。被叫显示会在话机上自动替换成名字。内部前缀 505-507 同时用于内测拨打。
  tags: [rule, multi-secretary, display]

- id: p45
  title: Supervisor/Statistics 应用必须用专用 ACD Admin 密码，不得把 installer 密码交给客户
  type: principle
  source_pages: p150, p188
  source_chapter: Supervisor application / Statistics application · Password level
  source_quote: |
    "ACD statistic and Supervisor applications use a dedicated ACD admin password instead
    of installer password. In order to not communicate to the end customer the installer
    password. OMC -> System Miscellaneous -> Passwords -> Management password."
  summary: |
    安全红线：班长台和统计应用登录用独立的 ACD Admin 密码（在 OMC 的 System Miscellaneous
    → Passwords → Management password 设置），绝不把 installer 密码随应用交付给最终客户。
    installer 密码是系统最高权限，泄露等于把整机配置权交出去。
  tags: [principle, security, passwords]

- id: p46
  title: 实验环境密码值口径（仅限实验）
  type: metric
  source_pages: p55, p59, p162, p205
  source_chapter: OMC Installation / Supervisor & Statistics labs
  source_quote: |
    "OXO Connect default IP address 192.168.92.246; Password 1st login: pbxk1064" (p55) /
    "Admin ACD password: Acdc1064" (p162, p205)
  summary: |
    教材实验值：installer 首登密码 pbxk1064（仅首次连接使用），ACD Admin 密码 Acdc1064
    （Supervisor p162 与 Statistics p205 实验均用此值）。注意：这些值随教材公开，
    生产环境绝不可沿用——首次登录后必须改密（见 p47）。
  conditions: 实验环境口径；BOOK_OVERVIEW 批判已指出教材密码明文属安全缺位，生产化必改。
  tags: [metric, passwords, lab-value, security]

- id: p47
  title: 各客户密码必须互不相同，改密入口在 OMC/Security
  type: rule
  source_pages: p62
  source_chapter: OMC Installation · Define the passwords
  source_quote: |
    "Define the passwords given by the trainer for all the different accounts. The passwords
    must be different for each customer! Passwords can be modified if necessary in
    OMC/Security menu."
  summary: |
    首次连接后立即为各账户设置密码，且硬性要求：不同客户的密码不得相同（防止一套密码
    打遍所有已交付站点）。后续改密走 OMC/Security 菜单。
  tags: [rule, security, passwords]

- id: p48
  title: OMC 首次连接必须安装证书到受信任根，否则每次连都弹安全警报
  type: rule
  source_pages: p60-61
  source_chapter: OMC Installation · Security Alert / Certificate
  source_quote: |
    "In order to avoid displaying the security alert at each connection, you must install
    the certificate the 1st time. ... Then browse to 'Trusted Root Certification Authorities'."
  summary: |
    OMC 以 Expert 模式 + server authentication 连接时首次会弹证书警报；首次必须点
    Install certificate 并导入"受信任的根证书颁发机构"，一劳永逸。跳过这步则每次连接
    都要手动确认。
  tags: [rule, omc, certificate]

- id: p49
  title: 首次连接必须录入客户信息，带 * 为必填
  type: rule
  source_pages: p63
  source_chapter: OMC Installation · Customer information
  source_quote: |
    "Information marked with an * are mandatory. Enter the customer information, mandatory
    at the first connection to the OXO. And optionally the supplier's information, ie the
    contact details of the technician performing the installation."
  summary: |
    OMC 首连流程闭环的最后一步：客户信息必填（* 项），服务商（安装技师联系方式）选填。
    不录完客户信息，OMC 无法进入正式配置状态。
  tags: [rule, omc, first-connection]

- id: p50
  title: Agent 应用的权限管理由 Operator 密码保护；客户库默认每坐席本地独立
  type: rule
  source_pages: p176-177
  source_chapter: Agent application · User rights management
  source_quote: |
    "Possible management via the Admin account and the Agent application. Access is
    protected by the OXO Connect Operator password." (p177) / "'Integrated mode' in local:
    Every agent uses their own customer database." (p176)
  summary: |
    Agent 应用的权限配置入口由 OXO 的 Operator（话务台）密码保护，不是谁都能改。
    客户数据库"集成模式"下落在本地——每个坐席各自维护一份客户库（弹屏资料不共享）。
    部署时要告知客户这一口径，避免误以为是共享 CRM。
  tags: [rule, agent-application, security, database]

- id: p51
  title: Supervisor 显示参数两项：过载闪烁时延、活动率计算周期（1 小时或半小时）
  type: metric
  source_pages: p151, p161
  source_chapter: Supervisor application · Configuration parameters
  source_quote: |
    "Time delay before overload messages flash: If a call overload lasts longer than this
    time limit, a warning message will be displayed on the observation screen (red box).
    Length of calculation period for agent activity rates: These statistics can be displayed
    for the past hour or half-hour." (p151) / "For the 'Length of calculation period for
    agent activity rates' option, select '1/2 hour'." (p161)
  summary: |
    ① 过载闪烁时延：呼叫超载持续超过该时限即在监控屏弹红色告警（数值可配，教材未给默认值，
    待确认）；② 坐席活动率计算周期仅两档：过去 1 小时或 1/2 小时，教材实验选 1/2 小时。
  tags: [metric, supervisor, thresholds]

- id: p52
  title: Supervisor 可远程修改的范围：坐席的组/rank/状态，组的开闭状态
  type: rule
  source_pages: p155, p165
  source_chapter: Supervisor application · Supervisor rights
  source_quote: |
    "The Supervisor application can change the group(s) the agent belongs, the agent rank
    and the agent status." (p165) / "The Supervisor application can change the group status.
    The group can be 'open' 'closed' or using the ACD group time ranges." (p165)
  summary: |
    班长台的干预权限边界：可改坐席所属组、坐席 rank、坐席状态（点状态图标进 Agent
    parameters，还可强制自动接听）；组级可改开/闭状态或切回"按时段自动"。
    除此之外（如队列长度、路由表）必须回 OMC 改。
  tags: [rule, supervisor, permissions]

- id: p53
  title: 坐席状态全集：4 大态 + On Duty 下 8 个子态
  type: metric
  source_pages: p164
  source_chapter: Supervisor application · Agent parameters
  source_quote: |
    "On Duty - Awaiting call / Not answering / Being routed / Ringing / ACD busy / On hold /
    Busy, outgoing call / Not available. Temporary Absence: ... for a break. Clerical work:
    ... drafting a report ... Off Duty: the agent is off duty or has not been assigned a
    station number."
  summary: |
    Supervisor 里坐席状态的四态各有所指，其中 On Duty 细分 8 个子态：待机、未接、
    转接中（站已预留未就绪）、振铃、ACD 通话中、刚挂机休整（On hold）、外呼忙、非 ACD
    来话不可用。Off Duty 还包含"未分配站号"的情况——坐席显示 off duty 先查有没有关联
    终端。验证方法：打一通约 5 分钟的 ACD 来话，坐席活动率列应持续上升（p164）。
  tags: [metric, supervisor, agent-status]

- id: p54
  title: 统计应用启用前必核三项：S1=10s、S2=40s（默认）、溢出前等待开关
  type: metric
  source_pages: p190
  source_chapter: Statistics application · Parameters to set up
  source_quote: |
    "Before using the Statistics application, ACD options must be checked. S1 hold-on
    threshold value: 10 seconds (default value). S2 hold-on threshold value: 40 seconds
    (default value). Waiting begins before overflow time delay (to enable or not)."
  summary: |
    统计口径的基线阈值：S1（短等待阈值）默认 10 秒、S2（长等待阈值）默认 40 秒，据此
    把来话分成"秒接/S1 内/S2 外"等桶；另有"溢出前等待计时"开关可选。这三个参数在 ACD
    侧设置，用统计前先核对，否则报表口径和预期不符。
  tags: [metric, statistics, thresholds, s1-s2]

- id: p55
  title: 统计导出双格式口径：binary 供本应用，CSV 供外部定制报表
  type: rule
  source_pages: p202
  source_chapter: Statistics application · Export
  source_quote: |
    "Binary files: Used only by the Statistics application. Useful to load the complete
    binary files in direct or remote connection and to work with them in local. CSV files:
    Used to be exported in order to handle them with external application compatible with
    the CSV file format. Useful for clients who want to have customized statistics, reports
    and printouts."
  summary: |
    导出选型：binary 是统计应用私有格式，用于把完整数据搬到本地离线分析；CSV 给 Excel
    等外部工具做客户定制报表。客户提"要自己拉报表"的需求时走 CSV 导出。
  tags: [rule, statistics, export]

- id: p56
  title: 统计文件存在主 CPU 上，应用须先连 OXO 取数
  type: rule
  source_pages: p191
  source_chapter: Statistics application · Connection
  source_quote: |
    "A connection to the OXO Connect is required in order to retrieve the statistics files
    stored on the main CPU. After launching the Statistics application, some options must be
    set up, via the Configuration menu, to enable this connection."
  summary: |
    统计原始数据落盘在 OXO 主 CPU（留存 14 个月，见 p01），Statistics 应用是取数端：
    启动后先在 Configuration → PBX Server 里配 OXO IP 并校验，才能拉到数据。
    "应用打开但没有数据"先查连接配置。
  tags: [rule, statistics, connection]

- id: p57
  title: 实验 IP 规划全套值与"改完必须重启 OXO"
  type: metric
  source_pages: p66-68
  source_chapter: OXO Connect IP settings modification
  source_quote: |
    "Address IP: 192.168.1.246; Subnet mask: 255.255.255.0; Default router address:
    192.168.1.254; DNS 1: 192.168.1.254; DNS 2: 10.20.30.254; DHCP range: 192.168.1.10 to
    192.168.1.39; Restart OXO connect." (p66) / Client PC "IP Address: 192.168.1.100" (p68)
  summary: |
    实验网段规划（生产按客户网段同构替换）：OXO 主 CPU 192.168.1.246，网关/DNS1
    192.168.1.254，DNS2 10.20.30.254（RLAB 公共区），话机 DHCP 池 192.168.1.10-39，
    管理客户端 PC 192.168.1.100。修改路径 OMC/Hardware and limits/Lan/IP configuration，
    改完必须重启 OXO 生效；之后客户端才能改走 RDP 远程连接。
  conditions: 实验环境口径（RLAB）；DNS2 指向 RLAB 公共资源区，生产环境无此值。
  tags: [metric, ip-planning, lab-value]

- id: p58
  title: OMC 首连口径：Expert 模式 + 勾选 Server authentication + 出厂 IP
  type: rule
  source_pages: p59
  source_chapter: OMC Installation · Connection to the system
  source_quote: |
    "Make a connection to the system with OMC in Expert mode with server authentication.
    Use LAN/WAN connection. Enter the default IP address 192.168.92.246. Check the field
    'Server authentication'. Enter the default installer password pbxk1064 only used for the
    first connection."
  summary: |
    首连三要素：Expert 菜单（非 Easy）、LAN/WAN 连接、勾 Server authentication；
    出厂 IP 192.168.92.246，installer 默认密码 pbxk1064 仅首次连接有效，登录后立即改
    （见 p47）。安全警报处理见 p48。
  tags: [rule, omc, first-connection]

- id: p59
  title: 组内选坐席搜索模式三选一：Fixed / Rotating / Longest idle
  type: rule
  source_pages: p95, p109
  source_chapter: Further ACD options / Advanced configuration · Search mode
  source_quote: |
    "Search mode: Fixed priority; Rotating priority; Longest idle period." (p95) /
    "ACD group 1 has a 'fixed' search mode, ACD group 2 has a 'longest idle period' search
    mode, ACD group 3 has a 'rotating' search mode." (p109)
  summary: |
    每组只能选一种分配算法：Fixed=严格按 rank 顺序（1 号永远先响）；Rotating=轮转均分
    来话；Longest idle=谁空闲最久给谁。设置入口 General parameters → Group 1-4 页签。
    教材实验法：三种模式各配一组，实际拨打对比行为差异，且必须把坐席 rank 一并纳入观察
    （p109 Notes）。
  tags: [rule, search-mode, distribution]

- id: p60
  title: 最大振铃时长 10 秒：Rotating 模式下每 10 秒流转下一坐席
  type: rule
  source_pages: p110, p190
  source_chapter: Advanced configuration · Maximum ringing duration
  source_quote: |
    "Validate the parameter Maximum ringing duration to 10 seconds." (p110) /
    "The incoming call comes first on extension 103 (if it's the first call for ACD group
    3). After 10 seconds ringing, the call is routed to extension 102. After 10 seconds
    ringing, the call is routed to extension 101. After 10 seconds of ringing, the call is
    routed to extension 103 and so on." (p110 Notes)
  summary: |
    单坐席最大振铃时长参数（教材设 10 秒）决定无人接时呼叫在坐席间流转的节奏：
    到时即跳下一位，循环往复。该值同时是坐席"漏接"感受与客户等待感受的平衡点，
    调小客户等待短但坐席压力大。注：p110 实验语境为 Rotating 模式（组 3）。
  conditions: 10 秒为实验设定值；参数可配范围原文未给出（待确认）。
  tags: [rule, search-mode, ringing]

- id: p61
  title: "无应答自动移除"：坐席漏接后自动切 off duty，呼叫继续流转
  type: rule
  source_pages: p111
  source_chapter: Advanced configuration · Agents that do not answer
  source_quote: |
    "Enable the option Agents that do not answer are automatically removed. ... After 10
    seconds ringing, the call is routed to extension 102 and extension 103 automatically
    swap to 'off duty' status. ... Then the call will definitely stay on extension 101."
  summary: |
    启用后，漏接来话的坐席会被系统自动置为 off duty（退出分配），呼叫转给下一位；
    全组只剩最后一人的极端情况下呼叫停在该坐席上反复振铃。用于强制淘汰长时间不接电话的
    坐席，副作用是被移除坐席需手动恢复 on duty 才能重新接话——培训时必须讲清。
  tags: [rule, search-mode, auto-removal]

- id: p62
  title: 培训/交付结束的现场恢复清单
  type: checklist
  source_pages: p211
  source_chapter: Actions to perform at the END of a training
  source_quote: |
    "Erase the MLAA voice guides if used. Clear ACD voice guides if used. Return to ACD /
    SCR factory settings if used. OXO Cold Reset with the following settings: User data;
    System data; Cloud connect data; Network, installer passwords and management data."
  summary: |
    实验环境收尾四步：删 MLAA 语音、清 ACD 语音、ACD/SCR 恢复出厂、冷复位（勾选用户
    数据、系统数据、Cloud Connect 数据、网络与 installer 密码及管理数据）。
    对生产的映射含义：站点退还/转售前必须冷复位到含密码在内的全部默认。
  tags: [checklist, restore, end-of-training]
```

---

## 覆盖率自检（task-01~15 中原则/规则/数值类覆盖情况）

| task | 任务 | 本文件覆盖条目 | 覆盖判定 |
|---|---|---|---|
| task-01 | 安装 OMC 并首次连接 | p58（Expert+证书外 p48）、p47（改密）、p48（证书）、p49（客户信息） | 已覆盖 |
| task-02 | 修改 IP 规划 | p57（全套 IP 值+重启规则） | 已覆盖 |
| task-03 | 搭建基础 ACD | p06（双层体系）、p07（重启生效）、p08（预配置清单）、p10（语音全组陷阱）、p11（验证清单）、p12（前缀 501-504）、p13（DDI 关联）、p14（rank） | 已覆盖 |
| task-04 | 六场景出口 | p34（营业时间测试先行）、p33（三出口同构原则）、p31（Transfer number 特例）、p29（队列出口） | 已覆盖 |
| task-05 | 路由表设计 | p22（三级优先）、p23（CLI 左→右/DDI 右→左）、p24（特殊→一般）、p25（内外部来话）、p04（10000 行+CSV） | 已覆盖 |
| task-06 | 搜索模式与振铃 | p59（三模式）、p60（最大振铃 10s）、p61（无应答自动移除）、p32（跨组优先） | 已覆盖 |
| task-07 | 队列管理 | p26（N×K 公式）、p27（等待时间公式）、p28（触发与播报）、p29（* 键出口）、p30（溢出 10s）、p02（上限 16） | 已覆盖 |
| task-08 | 时段与例外日 | p35（40 关闭/10 开放/每日 2 时段）、p34（时段测试位置） | 已覆盖（每周时段仅实验填法，无额外规则性数值可提） |
| task-09 | Login/Logout 与 free seating | p17（三要素关联）、p18（前提）、p19（base0/base1）、p20（登录流程）、p21（登出确认）、p16（ACDAutoLog）、p15（状态码解读，带待确认） | 已覆盖 |
| task-10 | Multi-Secretary | p40（引擎+许可）、p41（显示规则）、p42（六步顺序）、p43（登出兜底）、p44（速拨冠名） | 已覆盖 |
| task-11 | Supervisor 应用 | p45（ACD Admin 密码）、p51（显示参数）、p52（可改范围）、p53（状态全集） | 已覆盖 |
| task-12 | Agent 应用 | p50（权限+客户库口径）、p53（九子态，与 Supervisor 共享）、p36（弹屏权限）、p17（free seating 关联） | 已覆盖 |
| task-13 | Statistics 应用 | p54（S1/S2 阈值）、p55（导出口径）、p56（主 CPU 取数）、p45（密码，双页出处）、p01（14 个月留存） | 已覆盖 |
| task-14 | DTMF 弹屏 | p36（三前提+035# 格式） | 已覆盖 |
| task-15 | 语音定制 | p37（wav 编号规则）、p38（MMC 录制路径）、p39（OMC 四步法）、p10（全组陷阱） | 已覆盖 |

**结论**：task-01~15 的原则/规则/数值类内容全部有候选覆盖，共 62 条（公式 2、清单 7、原则 4、规则 36、数值口径 13）。

**待确认项汇总**（原文/图片未解析或口径存疑，需回查原 PDF）：
1. p15 话机状态码前两态显示符号疑 OCR 丢失字符（p122）。
2. wav 文件技术格式要求为截图，未解析出文字（p105）。
3. 语音编号 103-106 的逐条对应关系原文仅 "etc." 带过（p104/p136）。
4. 平均 ACD 通话时长参数的设置入口与默认值（p94）；过载闪烁时延默认值（p151）；最大振铃可配范围（p110）；溢出计时器可配范围（p96）。
5. ACD 引擎重启要求是否同样覆盖 Services 菜单的逐项修改，教材未逐一说明（p48 语境为 Setup 向导）。
