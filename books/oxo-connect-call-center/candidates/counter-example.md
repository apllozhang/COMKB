# 反例候选 (Counter-Examples) — OXO Connect Call Center (OXOCXTE107EN Ed07)

> extractor: counter-example-extractor · 阶段 2 素材（Boundary B 段来源）
> 取材方式: 词法索引不存在，回退全量扫描 source_fulltext.txt（218 页通读）
> 引用均为原文摘录（每段 ≤100 英文词），页码为 PDF 物理页（`===== PAGE N =====`）

```yaml
- id: ce01
  title: 修改 ACD Setup 后不重启 ACD 引擎，配置"看似保存实则未生效"
  type: counter-example
  source_page: p48
  source_chapter: Main configuration available from the Assistant menu
  source_quote: |
    "Validate the ACD Setup process by pressing the ''OK'' key.
     Restart the ACD engine in order to apply changes."
  failure_mode: |
    工程师在 ACD Setup 向导里逐页填完、点了 OK，就认为配置已生效，
    直接进入拨打测试，不改引擎状态。
  mechanism: |
    ACD 是经 CSTA 链接驱动寻线组与虚拟终端的常驻服务，向导保存的是
    数据库层面的参数；引擎运行时读的是已加载的旧参数副本。OK 只落库，
    重启 ACD 引擎才完成"落库 → 重载"闭环，两步缺一不可。
  correct_practice: |
    每次在 ACD Setup 中改动后，点 OK 之外必须再执行一次 ACD 引擎重启，
    然后才做验证测试。
  consequence: |
    测试行为与配置不符（前缀无效、DDI 不进组、邮箱不落话），排障方向
    被引向"配置写错"，反复改参数仍不生效，浪费整个验证环节。
  warning_signs:
    - "配置明明改了，拨打测试还是老行为"
    - OMC 里参数读回来是对的，实际呼叫却不走
  bound_to:
    - "基础 ACD 搭建流程"
    - "任何涉及 ACD Setup 向导的修改类 skill"
  tags: [counter-example, operation-order, acd-engine, restart]

- id: ce02
  title: 点 Default messages 触发全组广播下载，污染无关 ACD 组
  type: counter-example
  source_page: p76
  source_chapter: Basic ACD Configuration · Download the voice guides
  source_quote: |
    "Notes: When you click on ''Default messages'', the download of those
     messages will be done for all ACD groups. Click on the column numbers
     in order to disable the message downloading for the ACD group not
     linked to the configuration you want to set up."
  failure_mode: |
    只给 3 个组做配置，却直接点 Default messages 全量下载，没有先关掉
    与本次配置无关的组。
  mechanism: |
    该按钮的作用域是"所有 ACD 组"而非当前选中组，界面不弹确认也不做
    范围过滤；列号是唯一的范围开关。这是一个"默认作用域最大"的批量
    操作，必须显式收窄。
  correct_practice: |
    下载前先点列号，把不属于本次配置的 ACD 组的下载勾选关掉，再执行
    Transfer from PC to PCX。
  consequence: |
    无关组被写入默认语音，已有定制语音被默认提示音覆盖，客户现场
    出现"别的组欢迎语突然变成英文默认音"的回归事故。
  warning_signs:
    - 操作目标是"部分组"，但按钮没有让选组
    - 现场存在多套已定制语音的组
  bound_to:
    - "语音提示下载/定制流程"
    - "Multi-Secretary 语音定制（p146 同样入口）"
  tags: [counter-example, voice-prompts, batch-operation, side-effect]

- id: ce03
  title: Multi-Secretary 不按既定顺序编程，中途状态不一致
  type: counter-example
  source_page: p141
  source_chapter: Multi secretary ACD feature · 1.1
  source_quote: |
    "1.1. Program 3 DDI numbers and activate the Multi-Secretary mode
     OMC/Automatic Call Distribution/ACD Setup/General tab
     Carry out the programming in the following order"
  failure_mode: |
    跳步或乱序配置 Multi-Secretary：先去 ACD Services 建坐席/路由，
    回头才在 ACD Setup 里激活模式、建邮箱、生成 profiles。
  mechanism: |
    Multi-Secretary 是 ACD 引擎的预设形态，后一步依赖前一步的产物：
    profiles 依赖已激活的组与 DDI，Agent parameters 依赖 profiles，
    Line parameters 依赖坐席已存在。顺序是依赖图的拓扑序，乱序即
    引用未创建对象。
  correct_practice: |
    严格按 1.1→1.5 顺序：DDI 与模式激活 → 组邮箱 → 生成 profiles →
    声明秘书台为 Supervisor → ACD Services 建坐席与 Line parameters。
  consequence: |
    下拉列表里找不到组/坐席、profiles 生成不全、配置到一半返工重做。
  warning_signs:
    - "某个下拉框里应该有的选项是空的"
    - 配置过程中发现要回头补前面步骤
  bound_to:
    - "Multi-Secretary 全流程 skill"
  tags: [counter-example, operation-order, multi-secretary]

- id: ce04
  title: Signalization 模式与 Setup 模式混淆，来话提示位置错乱
  type: counter-example
  source_page: p85
  source_chapter: Further ACD options · setup mode for the group call mechanism
  source_quote: |
    "Check that the ''Group called with signalization mode'' feature is disabled.
     IN SIGNALING MODE, INCOMING CALLS TO HUNT GROUPS ARE INDICATED ON A
     ''GROUP SUPERVISION'' KEY. IN SETUP MODE, INCOMING CALLS TO A HUNT GROUP
     ARE DISPLAYED ON THEIR SUBSCRIBER RESOURCE KEYS."
  failure_mode: |
    误开 signalization mode（或没检查它处于禁用状态），导致 ACD 来话
    不显示在坐席的用户资源键上。
  mechanism: |
    两种模式决定来话呈现在哪类按键上：signalization 走"组监督键"，
    setup 走"用户资源键"。ACD 的按键 profiles 是按 setup 模式生成的，
    模式与 profiles 不配套，键位映射整体错位。
  correct_practice: |
    配置 ACD 前先到 OMC / System Miscellaneous / Feature design / part 2
    确认该特性为 disabled。
  consequence: |
    坐席话机振铃但资源键不亮、按键功能对不上，表现为"profile 生成了
    但不好使"的疑难杂症。
  warning_signs:
    - 新装/改造现场，历史配置来路不明
    - 来话在组监督键上出现而非资源键
  bound_to:
    - "基础 ACD 搭建前置检查"
    - "按键 profile 排障"
  tags: [counter-example, mechanism-misuse, signaling-mode]

- id: ce05
  title: CLI/DDI 比较方向搞反：CLI 从右向左、DDI 从左向右比
  type: counter-example
  source_page: p88
  source_chapter: Call characterization · number comparison method
  source_quote: |
    "CLI comparison CLIn / CLIt starts from the left to the right.
     DIDn / DIDt comparison starts from the right to the left."
  failure_mode: |
    把两个方向记反：以为 CLI 从右向左（按末几位匹配主叫）、DDI 从左
    向右（按前缀匹配被叫），照此设计路由表条目。
  mechanism: |
    CLI 是主叫号码，特征在国别/区号等前缀，所以从左向右比；
    DDI 是被叫号码，特征在末位分机，所以从右向左比。方向搞反后，
    匹配的是号码的错误端，命中的组与设计意图相反。
  correct_practice: |
    CLI 模板按"从左对齐的前缀"填（如 0044…），DDI 模板按"从右对齐的
    尾号"填（如 …5.05）。
  consequence: |
    按国家分流全部落错组，大客户 CLI 匹配不上专属组，且因为"部分
    号码仍可能碰巧命中"，问题呈间歇性，极难排查。
  warning_signs:
    - 测试呼叫落进了"不该进"的组
    - 同一路由规则对某些号码灵、某些号码不灵
  bound_to:
    - "呼叫特征化路由表设计 skill"
  tags: [counter-example, mechanism-misuse, call-characterization, routing]

- id: ce06
  title: 路由表先填一般规则后填特殊规则，特殊条目永远轮不到
  type: counter-example
  source_page: p88
  source_chapter: Line parameters table management
  source_quote: |
    "''Line parameters'' table management: Fill in the table beginning with
     the special case (the longest numbers). Ending with the general case
     (the shortest numbers)."
  failure_mode: |
    先录"所有 0033 开头进组 1"这类一般规则，再追加"Brest bank 专属
    进组 2"这类特殊规则，以为系统会自动挑最匹配的。
  mechanism: |
    路由表按行序做三级优先比较（CLI+DDI 双匹配 → 仅 DDI → 仅 CLI），
    先命中先应用，不做"最长匹配"重排。一般规则排在前面会先吃掉呼叫，
    特殊规则成为死条目。
  correct_practice: |
    从最长/最特殊的号码开始录入，一般（最短）规则放最后作兜底；
    后补特殊规则时要插行到一般规则之前。
  consequence: |
    大客户识别完全失效，客户按"已配置专属路由"验收时当场翻车。
  warning_signs:
    - 特殊规则配置正确却不生效
    - 路由表按时间顺序追加而非按特殊度排序
  bound_to:
    - "Smart Call Routing 路由表设计"
    - "CLI/DDI 分流的增量维护流程"
  tags: [counter-example, operation-order, routing-table, priority]

- id: ce07
  title: Transfer number 误以为对所有呼叫生效
  type: counter-example
  source_page: p97
  source_chapter: Further ACD options · Transfer number
  source_quote: |
    "Feature that can used when a call is routed to an opened ACD group
     where all agents are logged out or on ''off duty'' status. As soon as
     this process happens: First ACD incoming call will be transferred to
     a pre-defined number. Subsequent calls are either queued or routed to
     a deterrent message."
  failure_mode: |
    把 Transfer number 当成"全员离席转接总机"的通用无应答转移，
    以为每一通来电都会转到预设号码。
  mechanism: |
    该特性只在"组开着但全员登出/off duty"场景触发，且只转第一通；
    之后的呼叫按普通规则进队列或劝漏。它是"叫醒一个留守坐席"的
    机制，不是话务兜底出口。
  correct_practice: |
    需要全员离席时持续兜底，用组邮箱或关闭时段转接方案，而不是
    依赖 Transfer number。
  consequence: |
    话务高峰期全员离席，只有第一通找到人，其余全被劝漏挂断，
    客户感知为"打不通、没人管"。
  warning_signs:
    - 需求描述是"下班后所有电话转到手机"
    - 实测第二通起行为与预期不符
  bound_to:
    - "六场景呼入出口配置"
    - "非工作时间话务方案设计"
  tags: [counter-example, mechanism-misuse, transfer-number]

- id: ce08
  title: 手改 ACD 端口虚拟终端的预配置参数（don't touch 区）
  type: counter-example
  source_page: p80
  source_chapter: Features pre-configured by the ACD Setup menu · Virtual terminals
  source_quote: |
    "''Virtual terminals'' relating to ports ACD in the subscribers list.
     ''Media'' parameter ticked for all ACD ports (don't touch)."
  failure_mode: |
    在用户列表里看到 ACD 端口对应的虚拟终端，当成普通分机去清理
    或修改其 Media 等参数。
  mechanism: |
    ACD 端口虚拟终端是 ACD Setup 自动生成的引擎资源（且端口数与
    MLAA 共享，见 p44），Media 勾选是引擎寻址的一部分；手动改动
    破坏的是向导与引擎之间的隐式契约。
  correct_practice: |
    ACD 相关虚拟终端保持原样（don't touch）；要调整端口数量，回
    ACD Setup 的 General tab 改。
  consequence: |
    端口接续异常、劝漏第二形态不可用，且因属"预配置区"，没有文档
    化的恢复路径，只能重建 ACD 配置。
  warning_signs:
    - 用户列表里出现来历不明的"虚拟"分机
    - 清理"闲置"分机时顺手改了它们
  bound_to:
    - "OMC 用户列表维护"
    - "ACD 端口容量调整"
  tags: [counter-example, donot-touch, virtual-terminal]

- id: ce09
  title: 队列长度当成直接填写的数字，忽略 N×K 公式与上限 16
  type: counter-example
  source_page: p93
  source_chapter: Queue management · queue length configuration
  source_quote: |
    "Let N be the number of agent in service and K the load factor.
     If N * K is not an integer, the value of the queue is the next higher
     integer. The maximum size of the queue is 16 (same for the maximum
     number of standard ACD ports)."
  failure_mode: |
    想让队列等 10 个呼叫就直接找个"队列长度"字段填 10；或按坐席数
    估算时忘了 K 是乘数、结果超 16 上限。
  mechanism: |
    队列长度是派生值：N（值机坐席数）× K（话务因子 0.1-9.9）向上
    取整，且硬上限 16。系统不接受直接设队列值，超上限的部分无效。
  correct_practice: |
    用 N×K 反推：想要 10 个等待位且 N=4，则 K 取 2.5；需求超过 16
    时靠拆组/加端口方案解决，而不是改参数。
  consequence: |
    配置反复"不生效"或与预期不符；上限外的话务在高峰期直接进劝漏，
    来电被挂断。
  warning_signs:
    - 需求方直接给出"要排 N 个电话"的数字
    - 高峰期来电被提前劝退
  bound_to:
    - "队列管理 skill"
    - "话务容量需求落地"
  tags: [counter-example, parameter-limit, queue, formula]

- id: ce10
  title: 话务因子 K 越界（0.1-9.9）与把 off-duty 坐席计入 N
  type: counter-example
  source_page: p93, p184
  source_chapter: Queue management · Agent application lab verification
  source_quote: |
    "Traffic factor (from 0.1 to 9.9)."
    "In the ACD group 1 options, change the ''queue length'' parameter: put
     ''2.0'' instead of ''0.1''. Check that the queue length ... changed from
     1 to 4 calls (for this example, all the agents of the group are not in
     ''off duty'' status)."
  failure_mode: |
    两类错误：给 K 填 10 或 0 之类的越界值；或验证队列长度时把处于
    off duty 的坐席也数进 N，得出"队列怎么对不上公式"的困惑。
  mechanism: |
    K 有硬性取值域 0.1-9.9；公式里的 N 专指 in service（非 off duty）
    坐席数。p184 实验里 2 坐席 × 2.0 = 4 的验证前提明确标注"所有坐席
    不在 off duty"——off-duty 人员不参与分子分母。
  correct_practice: |
    计算前先确认当前 on duty 坐席数作为 N，K 在 0.1-9.9 内取值；
    验证时以 Supervisor 应用实时读到的在值机人数为准。
  consequence: |
    队列实际长度与设计差数倍：要么排不上队（K 被按更低 N 计算），
    要么占用了本不该占的接入资源。
  warning_signs:
    - 同一组队列长度时大时小
    - 坐席状态管理混乱（长期挂 off duty/clerical）
  bound_to:
    - "队列管理 skill"
    - "坐席状态运营规范"
  tags: [counter-example, parameter-limit, queue, formula]

- id: ce11
  title: 例外日规划超限：40 关闭日 / 10 开放日 / 每日 2 时段
  type: counter-example
  source_page: p100
  source_chapter: Exceptional days tab
  source_quote: |
    "Exceptional closing days: Possibility to define a maximum of 40 closing
     days. Exceptional opening days: Possibility to define a maximum of 10
     opening days. A maximum of 2 times ranges per opening day can be
     managed."
  failure_mode: |
    把全年法定假日加调休一次性全录（常超 40 天），或临时加开的
    周末促销日超过 10 天，或一个开放日想排早中晚 3 个时段。
  mechanism: |
    三项都是系统硬上限，不是建议值；且例外日按组管理（definition
    of exceptional days according to groups），超限时多出的日期根本
    无法录入，时段只能有两段。
  correct_practice: |
    录入前先做年度日历盘点：关闭日 ≤40、开放日 ≤10、每个开放日
    拆不超过 2 个时段；超需求用"相邻日期合并 + 组级差异"变通。
  consequence: |
    超限日期被静默丢弃，当天呼叫中心按普通营业日开门（或该开时
    关门），节假日话务事故。
  warning_signs:
    - 客户日历里有十几个调休/促销日
    - 需求里出现"上午 9-12、下午 13-17、晚上 18-20"
  bound_to:
    - "营业日历/例外日配置 skill"
  tags: [counter-example, parameter-limit, exceptional-days]

- id: ce12
  title: 按无限容量规划：32 坐席 / 8 组 / 16 端口 / 10000 条路由
  type: counter-example
  source_page: p28, p44, p50
  source_chapter: Capacities · ACD Setup General tab
  source_quote: |
    "32 active agents. 8 ACD groups. 16 ACD ports. 6 voice prompts for each
     ACD group. 10000 routing rules (CLI/DDI) can be defined. One queue for
     each ACD group. Statistics storage capacity up to 14 months."
  failure_mode: |
    方案设计时按部门数随意拆 ACD 组（超过 8 个）、按全公司坐席规模
    报数（超过 32 在值）、或忘了 ACD 端口总数 16 且与 MLAA 共享。
  mechanism: |
    这些是 R6.x 平台的固定规格：端口是并发接入资源（全忙即劝漏），
    与 MLAA 共享意味着 MLAA 用掉的端口会压缩 ACD 可用并发；组数、
    坐席数、路由条数同样是平台天花板，许可包（Welcome 5 坐席）再
    在其上二次封顶。
  correct_practice: |
    售前核对三层限额：平台规格（32/8/16/10000）→ 许可包 → MLAA
    端口占用后的净端口数；超规格即引出扩容/分机方案。
  consequence: |
    交付时组建不出来、坐席登不上、高峰期端口全忙劝漏，方案推倒重来。
  warning_signs:
    - 需求里组数 >8 或同时在线坐席 >32
    - 同机还开着 MLAA/其他共享端口应用
  bound_to:
    - "ACD 方案设计/售前规划"
    - "许可与容量核算"
  tags: [counter-example, capacity, parameter-limit]

- id: ce13
  title: 话机 ACD 状态码误读：1:01 / 1:01+ / 1-00 混为一谈
  type: counter-example
  source_page: p122
  source_chapter: Information on Alcatel-Lucent terminals
  source_quote: |
    "1:01 = Agent doesn't belong to ACD group 1 which is open, and 1 calls
     are in the queue. 1:01 = Agent belong to ACD group 1 which is open,
     and 1 calls are in the queue. 1:01+ = Agent belong to ACD group 1
     which is open, 1 calls are in the queue and the queue is full.
     1-00 = Agent belong to ACD group 1 which is closed."
  failure_mode: |
    排障时把 1:01、1:01+、1-00 都读成"组 1 有 1 个电话在排"，看不出
    坐席是否真在组内、队列是否已满、组是否处于关闭状态。
  mechanism: |
    该显示编码了三个正交信息：连接符（: 还是 -）区分组开/组关；
    加号（+）表示队满；前后数字分别是组号与排队数。而"在组内/
    不在组内"两种相反状态显示为同一个 1:01（原文两条均如此，
    依终端菜单上下文区分），不看菜单其余项就会误判。
  correct_practice: |
    按三要素解码：先看符号（: 开 / - 关），再看 +（队满），
    再用 ACD 菜单（注意用导航键下滚，p122 提示）确认坐席归属与
    登录状态；登出确认行为还分终端类型（Essential/Enterprise 需按
    OK 确认，模拟/DECT 不需要，p121）。
  consequence: |
    把"坐席没登录/不在组"误判为"队列满"，或把"组已关闭"当成
    呼叫积压，一线排障方向全错。
  warning_signs:
    - 用户报"话机上显示 1-00"却按排队问题处理
    - 电话不进来但显示有排队
  bound_to:
    - "话机状态排障 skill"
    - "坐席日常支持"
  tags: [counter-example, state-misread, troubleshooting, terminal-display]

- id: ce14
  title: ACDAutoLog 默认状态误判：登录成功 ≠ 自动开始接话
  type: counter-example
  source_page: p123
  source_chapter: Agent status after login session
  source_quote: |
    "Noteworthy address called ''ACDAutoLog'' in order to set up the default
     agent status after the login process. Value 01: agent is ''on duty''
     after login session (Default value). Value 00: agent is ''off duty''
     after login session."
  failure_mode: |
    坐席登录成功后坐等来电却一直不来，工程师反复查组配置和路由，
    没意识到登录后的初始状态由隐藏寻址项 ACDAutoLog 决定。
  mechanism: |
    登录只建立"终端-坐席-组"关联，是否进入可分配状态取决于
    ACDAutoLog：01（默认）登录即 on duty，00 登录后 off duty。
    这是编号寻址项而非常规菜单项，不查编号计划根本看不到它。
  correct_practice: |
    排查"登录了但不接电话"时，先让坐席拨 501 或在话机/应用里确认
    状态；如客户要求"登录即待命"，核对 ACDAutoLog=01。
  consequence: |
    整组坐席"已登录却 off duty"，组进入全员 off-duty 处理分支
    （劝漏/转接），客户感知为热线瘫痪。
  warning_signs:
    - 坐席坚持"我登录了"但 Supervisor 里显示 off duty
    - 现场曾改过编号计划或做过系统迁移
  bound_to:
    - "Login/Logout 与 free seating skill"
    - "坐席签入排障"
  tags: [counter-example, state-misread, acdautolog, hidden-parameter]

- id: ce15
  title: 把 installer 密码交给最终客户使用 Supervisor/Statistics
  type: counter-example
  source_page: p150, p188
  source_chapter: Password level "ACD Admin"
  source_quote: |
    "ACD statistic and Supervisor applications use a dedicated ACD admin
     password instead of installer password. In order to not communicate
     to the end customer the installer password.
     OMC-> System Miscellaneous -> Passwords -> Management password."
  failure_mode: |
    部署 Supervisor/Statistics 应用时图省事，直接把 installer 密码
    填给客户管理员用，没有建立独立的 ACD Admin 密码。
  mechanism: |
    两个客户端应用支持专用 ACD Admin 密码正是为了权限分层：班长
    和统计用户拿到 installer 密码等于拿到全网管理权限（改编号计划、
    改中继、改一切）。密码分层是设计意图，不是可选项。
  correct_practice: |
    在 OMC / System Miscellaneous / Passwords / Management password
    里设置独立 ACD Admin 密码，客户端只发这个密码；installer 密码
    留在集成商手里。
  consequence: |
    客户端人员掌握 installer 密码后可绕过集成商改动全网配置，
    出问题无版本可追，责任边界彻底失守。
  warning_signs:
    - 客户要求"给我们一个能登录的密码"
    - 现场只有一个密码被所有人共用
  bound_to:
    - "Supervisor/Statistics 应用部署 skill"
    - "交付安全基线"
  tags: [counter-example, security, password, privilege]

- id: ce16
  title: 实验/出厂默认密码（pbxk1064、Acdc1064）直接上生产
  type: counter-example
  source_page: p59, p62, p162, p205
  source_chapter: OMC Installation · Define the passwords
  source_quote: |
    "The Installer password is ''pbxk1064'' when logging for the fisrt time."
    "The passwords must be different for each customer!"
    "Admin ACD password: Acdc1064."
  failure_mode: |
    交付时沿用教材/出厂默认密码：首次连接的 pbxk1064 不改，
    ACD Admin 用 Acdc1064，或所有客户用同一套密码。
  mechanism: |
    教材明示 pbxk1064 只是"only used for the first connection"的
    出厂值，且"每个客户的密码必须不同"——默认值是公开知识，
    等于把管理入口留在门垫下。本书本身就是公开流转的培训材料，
    所有默认密码对攻击者是已知常量。
  correct_practice: |
    首次连接后立即在 OMC/Security 菜单为各账户设置每客户唯一的
    新密码；培训环境收尾时按 p211 做冷复位清除实验密码。
  consequence: |
    任何拿到同型号设备/教材的人都能以 installer 身份接管系统；
    同密码的多客户站点一站泄露、处处可试。
  warning_signs:
    - 密码字段仍是教材截图里的值
    - 多个客户站点密码相同
  bound_to:
    - "OMC 安装与首次连接 skill"
    - "全部三应用部署（Boundary：实验环境口径）"
  tags: [counter-example, security, default-password, production]

- id: ce17
  title: 无应答自动移除的连锁反应：坐席被逐个自动置 off duty
  type: counter-example
  source_page: p110, p111
  source_chapter: Maximum ringing duration · Agents that do not answer are automatically removed
  source_quote: |
    "After 10 seconds ringing, the call is routed to extension 102 and
     extension 103 automatically swap to ''off duty'' status. After 10
     seconds ringing, the call is routed to extension 101 and extension
     102 automatically swaps to ''off duty'' status. Then the call will
     definitely stay on extension 101."
  failure_mode: |
    打开"Agents that do not answer are automatically removed"以为
    只是"没人接就跳下一个"；忽略它会把未接听坐席直接踢出分配池，
    引发全组连锁崩塌。
  mechanism: |
    与仅开启振铃轮转（p110：103→102→101→103 无限循环）不同，自动
    移除在每次跳转时把前一个坐席置 off duty：坐席没听到/没接，
    组员名单就少一人，呼叫压力向队尾集中，最后一个坐席被持续
    轰炸且永远无法卸载。
  correct_practice: |
    开启该选项必须配套：坐席振铃可闻可见的现场纪律、合理的最大
    振铃时长，以及 Supervisor 端监控 off-duty 异常自动回升机制
    （或干脆用 Fixed 模式靠 rank 控制顺序）。
  consequence: |
    一次午餐时间集体未接听 = 全组被自动下线，组转入全员 off-duty
    分支（劝漏/转接），热线静默死亡，且无人意识到要手动恢复状态。
  warning_signs:
    - Supervisor 里 off-duty 人数随时间单调上涨
    - 坐席反映"电话怎么老打给我一个人"
  bound_to:
    - "搜索模式/无应答移除配置 skill"
    - "组级运营监控"
  tags: [counter-example, side-effect, auto-removal, off-duty]

- id: ce18
  title: 只看搜索模式不看坐席 rank，分配行为与预期不符
  type: counter-example
  source_page: p109
  source_chapter: Configure the search mode · Notes
  source_quote: |
    "Notes: Check the different search modes to compare the modes. Do not
     forget to take into account the priority of the agents defined in the
     previous exercise. Do practical tests."
  failure_mode: |
    把组设成 Rotating/Longest idle 后，以为 rank（跨组优先级）不再
    起作用；或反过来以为改了搜索模式就能覆盖 rank 设定。
  mechanism: |
    搜索模式（组内选人算法）与坐席 rank（跨组/组内优先级，p75 定义）
    是正交的两层：Fixed 模式直接按 rank 序取人，Rotating/Longest idle
    也在 rank 约束的候选集内运转。两层叠加后才产生最终顺序。
  correct_practice: |
    调整分配策略时同时核对两处：General parameters 的 Search mode
    与 Agent parameters 的 rank；按 p109 的要求做实际拨打测试验证
    顺序后再交付。
  consequence: |
    "明明设了轮转，怎么还是 101 先响"类工单；rank 低的坐席长期
    无话务，绩效数据失真。
  warning_signs:
    - 实际响铃顺序与所选模式的理论顺序不一致
    - 坐席同时属于多个组（rank 必然介入）
  bound_to:
    - "搜索模式选择 skill"
    - "坐席分组与优先级设计"
  tags: [counter-example, mechanism-misuse, search-mode, rank]

- id: ce19
  title: 客户识别弹屏只配一处，三处条件缺一即失效
  type: counter-example
  source_page: p101, p102
  source_chapter: Client identification feature
  source_quote: |
    "To get that functionality, ACD groups with code must be selected in the
     line parameters. In OMC, customize the customer code announce. In the
     agent application, it is necessary to give the ''automatic screen pop
     up'' rights in the agent parameters."
  failure_mode: |
    只在 Line parameters 里勾了"组带客户码"就验收弹屏功能，漏掉
    客户码提示语定制或坐席应用的 screen popup 权限。
  mechanism: |
    功能链路横跨三个配置域：线参数决定哪些组收集 DTMF 码（107.wav
    提示来话人输码），OMC 语音决定提示是否存在，坐席应用的
    automatic screen pop up 权限决定坐席端是否弹窗。链路上任一环
    缺失，前两环的投入都不可见。
  correct_practice: |
    按三步清单逐项核对：Line parameters 选中带码组 → OMC 定制
    customer code announce → Agent application 勾自动弹屏权限，
    再以来电输码（如 035#）做端到端测试。
  consequence: |
    来电者听到系统提示输码、输了码，坐席端毫无反应，VIP 识别功能
    形同虚设且客户以为已开通。
  warning_signs:
    - "弹屏有时有有时没有"（不同坐席权限不同）
    - 只在个别坐席电脑上测试过
  bound_to:
    - "DTMF 客户识别弹屏 skill"
    - "Agent 应用权限管理"
  tags: [counter-example, incomplete-config, screen-popup, dtmf]

- id: ce20
  title: 自制 wav 提示音不按编号规则命名，语音内容整体错位
  type: counter-example
  source_page: p104, p136
  source_chapter: Customize voice prompts
  source_quote: |
    "Create with a PC the voice prompts in .wav format. Respect the
     assignments 101.wav = welcome message, 102.wav = waiting message, etc."
  failure_mode: |
    请人录制语音后按"内容"命名文件（welcome_doctor1.wav 等），
    上传时没映射回 101-107 固定编号，或上传错了组号前缀。
  mechanism: |
    引擎按固定编号寻址提示音（101=欢迎语、102=等待语…107=客户码
    提示，各组另有组号前缀），文件名只是载体，编号才是索引。命名
    不守约等于把欢迎语文件插进等待语槽位。
  correct_practice: |
    录音交付时即按编号命名（含组前缀），OMC Transfer 模式批量上传
    前逐个核对编号-内容对照表，上传后逐组试听验证。
  consequence: |
    来电者听到"等待语"当欢迎语、或 A 组语音在 B 组播放，客户
    感知极差且返工需重新走全量上传。
  warning_signs:
    - 语音供应商交付的文件名不含编号
    - 播放内容与呼叫阶段对不上
  bound_to:
    - "ACD 语音提示定制 skill"
  tags: [counter-example, voice-prompts, naming-convention]

- id: ce21
  title: 使用 Statistics 前不核对 S1/S2 阈值，报表口径静默失真
  type: counter-example
  source_page: p190
  source_chapter: Parameters to set up (Statistics)
  source_quote: |
    "Before using the Statistics application, ACD options must be checked.
     S1 hold-on threshold value: 10 seconds (default value).
     S2 hold-on threshold value: 40 seconds (default value).
     Waiting begins before overflow time delay (to enable or not)."
  failure_mode: |
    装完 Statistics 直接出报表，没核对 S1/S2 阈值与 overflow 时延
    开关是否与现场约定一致。
  mechanism: |
    S1/S2 是统计对"等待时长"的分段口径（默认 10s/40s），报表里的
    好/差分层完全由这两个阈值切分；阈值若被改动或与客户 SLA 口径
    不一致，同一份数据会讲出两个故事。
  correct_practice: |
    出第一份报表前，在 OMC 核对 S1/S2 与 overflow 时延设置，并
    把口径写进交付文档（默认 10s/40s 仅是出厂值，非承诺值）。
  consequence: |
    报表"80% 呼叫在 S1 内接听"与客户自测体感严重不符，统计
    可信度被质疑，返工重算。
  warning_signs:
    - 报表指标与客户 SLA 定义对不上
    - 现场曾有人"调优"过 ACD 参数但无记录
  bound_to:
    - "Statistics 应用部署 skill"
    - "SLA 报告口径定义"
  tags: [counter-example, statistics, threshold, weak-signal]
```

---

## 覆盖率自检

### 检索方式
词法索引 `books/oxo-connect-call-center/.cangjie/index/lexical.sqlite` 不存在，按规范回退**全量扫描**：通读 `source_fulltext.txt` 全部 3785 行（PAGE 1-218），以警告信号词人工复核。

### 信号词命中核对
| 信号词 | 命中情况 |
|---|---|
| don't touch | p80（ce08） |
| Do not forget | p109（ce18）、p122（并入 ce13 引用） |
| must | p62 密码每客户不同（ce16）、p190 S1/S2（ce21） |
| Notes | p76（ce02）、p107（组名显示说明，非反例，已排除）、p109（ce18）、p110-111（ce17） |
| maximum | p93 队列 16（ce09）、p100 例外日 40/10/2（ce11）、p110 振铃时长（ce17） |
| instead of | p113（劝漏出口对比，被 ce07/ce09 吸收）、p184（ce10） |
| only | p59 "only used for the first connection"（ce16）、p50 binary 仅 Statistics 应用自用（信息性，未立条） |
| forbidden | 仅 p2 版权声明，与技术无关，已排除 |
| Careful / wrong / avoid | 无独立命中（avoid 仅出现于 p60 "avoid displaying the security alert"，属操作便利提示，非失败模式） |

### 任务提示锚点逐项核对（全部命中）
- 队列上限 16 / 话务因子 0.1-9.9 → p93（ce09、ce10）
- 例外日 40/10/2 时段 → p100（ce11）
- 坐席 32 / 组 8 / 端口 16 / 路由 10000 → p28、p50（ce12）
- Multi-Secretary 编程顺序 → p141（ce03）
- ACD Setup 后重启引擎 → p48（ce01）
- Default messages 广播 → p76（ce02）
- Signalization vs Setup → p85（ce04）
- CLI/DDI 方向 + 路由表填写顺序 → p88（ce05、ce06）
- 状态码 1:01 / 1:01+ / 1-00 → p122（ce13）
- installer 密码暴露 → p150、p188（ce15）
- 实验密码不可上生产 → p59、p62、p162、p205（ce16）
- 无应答自动移除连锁 → p111（ce17）

### 覆盖的章节范围
p24-52（ACD 概念与配置体系）、p54-77（OMC 安装与基础配置实验）、p78-116（高级参数与高级配置实验）、p117-123（Login/Logout）、p124-146（Multi-Secretary）、p147-165（Supervisor）、p166-184（Agent）、p185-209（Statistics）、p210-211（收尾复位）。

### 主动排除项（不属于反例）
- p2 版权/保密声明、p212-218 评估流程（非技术失败模式）
- p107、p146 组名/显示信息说明（机制事实，归 framework extractor）
- p126 "license needed"（前置条件，归 framework；其"无许可强行配置会失败"未在原文展开，不再演绎）
- p110 与 p111 的对照已合并进 ce17（机制对比最完整）
- p121 登出确认的终端差异、p108 例外日按组生效，分别并入 ce13、ce11 的正确做法/warning_signs，未单独立条

### 不确定/待确认
- p122 两条 `1:01` 在文本提取中无法区分视觉差异（推测原书通过字体/符号区分"组内/组外"），已如实引用原文并在 mechanism 中注明"依终端菜单上下文区分"——建议下游引用时核对 PDF 原图。
- 全书为实验手册口径，无生产环境安全加固章节；相关边界（默认密码、可信内网假设）已在 ce15/ce16 的 bound_to 与 BOOK_OVERVIEW 批判段对齐。
