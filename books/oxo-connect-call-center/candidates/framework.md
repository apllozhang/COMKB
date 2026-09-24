# Framework Candidates — OXO Connect Call Center (OXOCXTE107EN Ed07)

> 提取器: framework-extractor · 日期: 2026-09-23 · 全量扫描 source_fulltext.txt (218 页)
> 单元类型取值: 框架 / 流程 / 决策 / 排障 / 规程（组合型用 "+" 连接）
> 所有菜单路径、参数名、数值保留原文。

```yaml
- id: f01
  title: ACD 呼入处理总框架（引擎架构 + 六场景清单）
  type: 框架
  source_pages: PAGE 36
  source_quote: |
    "Call Center Engine / Call Distribution to hunt groups ... CSTA link / ACD ports ...
    Processes available: Process when agents are available / Process when all agents are busy /
    Process when the queue is full / Process when all standard ACD ports are busy /
    Process when all agents are logged out or ''off duty'' status / Process when the ACD group is closed"
  summary: |
    OXO Connect 上所有 ACD 呼入由内置 Call Center Engine 经 CSTA 链接驱动寻线组
    （hunting groups with Virtual Terminals Media accesses）与 ACD 端口处理。
    排查任何呼入行为问题时，先判定来电落在六个通用场景中的哪一个：
    坐席空闲 / 坐席全忙（进队列）/ 队列满 / 标准 ACD 端口全忙 / 全员登出或 off duty / 组关闭。
    每个场景有独立的处理分支与出口配置，这是全书法定的排障主轴。
  key_details: |
    - 引擎要素: Call Center Engine、CSTA link、ACD ports、Voice mail/ACD application selection、Queue process
    - 前置判定: Opening hours test（OPEN/CLOSED）
    - 六场景均为"General process"枚举，逐场景流程见 f02-f07
  tags: [framework, acd, call-scenarios, troubleshooting-axis]

- id: f02
  title: 场景1 — 坐席可用（agents available）处理流程
  type: 流程
  source_pages: PAGE 37
  source_quote: |
    "Incoming calls / Opening hours test / OPEN / Welcome greeting / Looking for an agent /
    Call to the agent / Transfer and conversation / End of the call"
  summary: |
    组开放且有空闲坐席时：呼入 → 营业时间测试（OPEN）→ 播欢迎语（Welcome greeting）→
    寻找坐席 → 呼叫转至坐席 → 通话 → 结束。
  key_details: |
    - 欢迎语在寻坐席之前播放（验证基准：p77 "welcome message comes up first, followed by a transfer to an agent"）
  tags: [flow, scenario-1, agent-available]

- id: f03
  title: 场景2 — 坐席全忙进队列（queue process）流程与阈值消息决策
  type: 流程+决策
  source_pages: PAGE 38, 112
  source_quote: |
    "Agent not available: Call placed in the queue ... Queue exit by ''*'' key ...
    Average time or Rank number trigger enabled? ... Threshold reached? . Estimated waiting time message.
    OR . Minimum rank in the queue message. ... Queue message 1 ... Queue message 2"
  summary: |
    组开放但坐席全忙：呼入 → 欢迎语 → 进入等待队列 → 先播 Queue message 1；
    若配置了平均等待时间或队列排名触发器，达到阈值时插播"预计等待时间"或"队列最低排名"消息；
    否则循环播放 Queue message 2。坐席一有空闲，队首呼叫立即转出。
    来电者可随时按星号键（"*"）退出队列，出口为组邮箱留言或转预定义号码。
  key_details: |
    - 实验验证（p112）: 坐席全忙时来电入队，"hear the welcome message 1 first then the waiting message 2 that is looped"
    - 队列出口配置: Call distribution 图标 → Call management 图标 → 依次启用 "Place in group voice mailbox" 与 "Transfer to a number" 并逐一验证
  tags: [flow, decision, scenario-2, queue, star-exit]

- id: f04
  title: 场景3 — 队列满劝漏（第一劝漏形态）出口决策
  type: 决策+流程
  source_pages: PAGE 39
  source_quote: |
    "The queue is full ... Forwarding destination option selected? Mail box Option selected? YES YES NO NO ...
    Transfer to destination number / Message placed in the ACD group mail box / Dissuasion message ...
    First case of a redirection/dissuasion status"
  summary: |
    队列满时的三出口决策：先看是否启用"转接目的地"，再看是否启用"组邮箱留言"；
    两者都未启用则播劝漏语音（Dissuasion message）后释放呼叫。
    这是劝漏（redirection/dissuasion）状态的第一形态。
  key_details: |
    - 出口优先按配置判定：Transfer to destination number > 邮箱留言 > 播语音释放
  tags: [decision, flow, scenario-3, dissuasion, queue-full]

- id: f05
  title: 场景4 — 标准 ACD 端口全忙劝漏（第二劝漏形态）判定
  type: 决策+流程
  source_pages: PAGE 40
  source_quote: |
    "All standard ACD ports busy? NO YES / Use of dedicated ports for dissuasion status /
    Usual ACD process: . Call deterred . Call transferred . Call queued . Etc. ...
    Second case of a dissuasion status"
  summary: |
    呼入先判端口资源：标准 ACD 端口未全忙 → 走常规 ACD 进程（劝退/转接/排队等）；
    标准 ACD 端口全忙 → 直接进入劝漏状态（使用专用端口），按 f04 同样的三出口处理。
    排障含义：来电直接被劝退但队列未满时，应检查 ACD 端口占用（上限 16，与 MLAA 共享）。
  key_details: |
    - 端口全忙是独立于"队列满"的第二种劝漏触发条件
  tags: [decision, scenario-4, acd-ports, dissuasion, troubleshooting]

- id: f06
  title: 场景5 — 全员登出/off duty 的 Transfer number 机制（首呼转接决策）
  type: 决策+流程
  source_pages: PAGE 41, 97
  source_quote: |
    "All the agents are logged out ... 1st call since the agent absence? NO NO YES YES ...
    Transfer to transfer number / Call placed in the queue / Dissuasion message ...
    First ACD incoming call will be transferred to a pre-defined number.
    Subsequent calls are either queued or routed to a deterrent message"
  summary: |
    组开放但全员登出或 off duty：第一通来电转往预定义 Transfer number；
    后续来电进入队列或播劝漏语音。排障要点：该场景下"只有第一通被转接"，
    客户报"偶尔来电丢失/行为不一致"时先确认坐席是否集体登出。
  key_details: |
    - 适用条件: "can be used when a call is routed to an opened ACD group where all agents are logged out or on off duty status"
  tags: [decision, flow, scenario-5, transfer-number, troubleshooting]

- id: f07
  title: 场景6 — 组关闭（closed）处理流程
  type: 流程
  source_pages: PAGE 42, 114
  source_quote: |
    "CLOSED ... Closing message ... Forwarding destination option selected? Mail box option selected? ...
    Transfer to destination number / Message placed in the Call Center group mail box / ... End of the call"
  summary: |
    营业时间测试判为 CLOSED：播关闭语（Closing message）后释放；
    可改为转接预定义目的地或转入组邮箱留言。实验（p114）要求逐一启用两个出口并用组 3 实呼验证。
  key_details: |
    - 关闭判定来源: 营业时段表（f20）或 Supervisor 应用强制组状态 open/closed（p165）
  tags: [flow, scenario-6, closed-status]

- id: f08
  title: ACD Setup 向导五步配置流程
  type: 流程
  source_pages: PAGE 43-48
  source_quote: |
    "Path: OMC / Customer PBX / Automatic Call Distribution. Select the ''ACD Setup'' icon to start the ACD assistant ...
    Validate the ACD Setup process by pressing the ''OK'' key. Restart the ACD engine in order to apply changes"
  summary: |
    ACD 初始配置的双层体系中的第一层：向导一次成型。五个页签按序完成：
    General（端口数、状态前缀、ACD 组与 DDI 关联）→ ACD Group（建组邮箱）→
    Profiles（生成坐席/班长预定义按键 profile）→ Agents/Supervisors（把 profile 应用到指定话机）→
    OK 校验并重启 ACD 引擎生效。
  inputs: OMC Easy view 会话；规划好的 DDI 号码表与坐席话机清单
  outputs: 可用的 ACD 组骨架（寻线组、虚拟终端、DDI、邮箱、profile 均由向导后台生成，见 f09）
  steps: |
    1. General 页签: Ports number（与 MLAA 共享）、坐席状态前缀、Call Center hunting groups 及关联 DDI
    2. ACD Group 页签: 勾选需要创建邮箱（mailbox）的组
    3. Profiles 页签: 选择生成 agent 或 supervisor 的预定义 ACD profiles
    4. Agents/Supervisors 页签: 为选中的坐席/班长话机应用预定义按键 profile
    5. 按 OK 校验 → 重启 ACD 引擎使配置生效
  missing_conditions: 向导里端口数的规划依据（如何从话务量定端口数）书中未给，仅给上限 16
  tags: [procedure, acd-setup-wizard, omc]

- id: f09
  title: ACD Setup 向导后台生成物清单与前置开关检查
  type: 框架
  source_pages: PAGE 80-85
  source_quote: |
    "''Virtual terminals'' relating to ports ACD in the subscribers list. ''Media'' parameter ticked for all ACD ports (don't touch) ...
    Creation of hunting groups in cyclic mode ... A DID number is associated to the targeted ACD group ...
    Check that the ''Group called with signalization mode'' feature is disabled. Path: OMC / System Miscellaneous / Feature design /part 2"
  summary: |
    理解向导"动过什么"是排障的知识底座：ACD Setup 会自动生成——
    (1) ACD 端口对应的虚拟终端（Media 参数已勾选，不许改动）；
    (2) 组邮箱虚拟终端并设动态呼转至语音邮箱；
    (3) cyclic 模式寻线组（含 ACD 专用虚拟终端），用于坐席状态管理与 ACD 组接入；
    (4) 公共编号计划中的 DDI 关联；(5) 预定义 ACD profiles（按键 + feature rights + dynamic routing）。
    另有一个必须人工核查的系统开关：signalization mode 必须保持禁用，
    否则呼入显示在"组监管键"而非话机资源键上，坐席无法正常接听。
  key_details: |
    - signalization mode 开启时: "INCOMING CALLS TO HUNT GROUPS ARE INDICATED ON A ''GROUP SUPERVISION'' KEY"
    - setup mode（默认正确态）: 呼入显示在坐席的 subscriber resource keys 上
  tags: [framework, wizard-artifacts, virtual-terminals, precheck]

- id: f10
  title: 基础 ACD 搭建完整规程（3 组实验：前缀/DDI/邮箱/profile/坐席分组/语音/验证）
  type: 规程
  source_pages: PAGE 69-77
  source_quote: |
    "The prefixes used to manage the agent status are • 501: on duty • 502: off duty • 503: clerical work • 504: temporary absence ...
    Group ACD n°1, internal prefix:505, DDI N°: 41505 ..."
  summary: |
    全书核心交付规程：在 ACD Setup 向导 + ACD Services 菜单两层完成三组 ACD 搭建，
    再下载默认语音并用四态前缀实呼验证。
  inputs: 客户需求（3 组）、DDI 号码段、坐席话机（101/102/103）
  outputs: 可接听的 3 个 ACD 组（内部前缀 505/506/507，DDI 41505/41506/41507）
  steps: |
    1. OMC / Automatic Call Distribution / ACD Setup / "General" tab — 核对状态前缀 501-504；
       添加各组 DDI（505→41505, 506→41506, 507→41507）
    2. ACD Setup / "ACD Group" — 为三组各建 voice mailbox
    3. ACD Setup / "ACD Profiles" — 生成 ACD 按键 profiles
    4. ACD Setup / "Agents / Supervisors" tab — 101/102/103 套 Agent profile，话机 100（话务台）套 Supervisor profile
    5. OMC / Call distribution Services / ACD-SCR Services — 按 505-507/41505-07 维护 "Line parameters"
    6. OMC / Automatic Call Distribution / ACD Services / Agent parameters — 坐席入组并定 rank:
       组1: 101(rank1), 102(rank2)；组2: 102(rank1), 103(rank2)；组3: 103(rank1), 102(rank2), 101(rank3)；
       自定义坐席姓名，状态置 on duty
    7. OMC / ACD / ACD Voice messages — 选 Transfer mode（组1,2,3）→ Default messages → 箭头 PC→PCX 传输；
       注意: 点 Default messages 会向所有组下载，不需配置的组要点列号关掉
    8. 验证: 检查 Subscribers list / Hunting groups list / Internal numbering plan / Public numbering plan 四个菜单；
       实呼每组，确认"先欢迎语后转坐席"；用 501-504 前缀与功能键切换四态测试
  missing_conditions: 无（教材给全参数）；生产化需补真实中继与密码策略（教材实验值仅限实验环境）
  tags: [procedure, basic-acd, task-03-core, verification]

- id: f11
  title: OMC 安装与首次连接规程（Expert 模式/证书/改密/客户信息）
  type: 规程
  source_pages: PAGE 54-64
  source_quote: |
    "Make a connection to the system with OMC in Expert mode with server authentication ...
    Enter the default IP address 192.168.92.246 ... Check the field ''Server authentication'' ...
    Enter the default installer password pbxk1064 only used for the first connection ...
    The passwords must be different for each customer!"
  summary: |
    一切配置的前提流程：装 OMC → Expert 模式首连（服务器认证）→ 装证书消除告警 →
    逐账户改密 → 录入客户信息（带 * 为必填）→ 右下角图标确认已连接。
  inputs: 管理员 PC（SOFTS OXO CONNECT 目录）、出厂 IP 与首登密码
  outputs: 可用于全部后续配置的 OMC 管理连接
  steps: |
    1. 解压 OMC → setup.exe 以管理员运行 → 选语言 → 选 Destination folder →
       选 Country/Distribution Channels（可多选）→ Target Product → 显示语言 → Install → Finish
    2. 打开 OMC → 选 "Expert" 菜单 → LAN/WAN 连接 → 填默认 IP 192.168.92.246 →
       勾选 "Server authentication" → 输首连密码 pbxk1064（仅首次）
    3. Security Alert 弹出 → View certificate → Install certificate →
       浏览到 "Trusted Root Certification Authorities" → OK → Finish（避免每次连接重复告警）
    4. 为各账户定义密码（每个客户必须不同；后续可在 OMC/Security 菜单修改）
    5. 录入客户信息（* 必填），可选填供应商/技术员联系信息
  missing_conditions: 教材密码 pbxk1064 / Acdc1064 为实验值，生产环境必须替换（书中仅提示"must be different for each customer"）
  tags: [procedure, omc, first-connection, certificate]

- id: f12
  title: OXO Connect 与客户端 PC 的 IP 规划修改规程
  type: 规程
  source_pages: PAGE 65-68
  source_quote: |
    "OMC/ Hardware and limits/ Lan/IP configuration ... enter a value for the Main CPU: 192.168.1.246 ...
    In the DHCP tab, define the IP addresses range for deskphones: Start: 192.168.1. 10 End: 192.168.1. 39 ...
    Click OK & Re-start the OXO Connect"
  summary: |
    现场交付第一步：先改 OXO 侧 IP（CPU 地址、网关、掩码、DNS、DHCP 池）并重启，
    再改客户端 PC 地址；改完即可用 RDP 远程连接客户端 VM。
  inputs: 客户网段规划（实验值: OXO 192.168.1.246, PC 192.168.1.100, 网关/DNS1 192.168.1.254, DNS2 10.20.30.254）
  outputs: 按客户网段可管理的新地址
  steps: |
    1. OMC/ Hardware and limits/ Lan/IP configuration → Boards tab: Main CPU = 192.168.1.246
    2. LAN Configuration tab: Default Router Address = 192.168.1.254, Mask = 255.255.255.0
    3. DNS tab: DNS 1 = 192.168.1.254, DNS 2 = 10.20.30.254
    4. DHCP tab: 话机地址池 192.168.1.10 - 192.168.1.39
    5. OK → 重启 OXO Connect
    6. 客户端 PC（OXO_PC_CLIENT）: IP 192.168.1.100 / 掩码 255.255.255.0 / 网关 192.168.1.254 / DNS 同上
  missing_conditions: 无（实验参数齐全）；书中未论证该网段选择的依据（批判性提示: 假设与客户拨号计划不冲突）
  tags: [procedure, ip-planning, task-02]

- id: f13
  title: 呼叫特征化（Call characterization）三级优先匹配决策
  type: 决策
  source_pages: PAGE 86-88
  source_quote: |
    "Priority comparison # 1: CLIn / CLIt & DIDn / DIDt ... CLIn=CLIt & DIDn=DIDt? YES → ACD group application ...
    Priority comparison # 2: CLIn / CLIt & DIDt not filled in ...
    Priority comparison # 3: DIDn / DIDt & CLIt not filled in ... [else] Ring back tone"
  summary: |
    呼入按主叫 CLI 与被叫 DDI 匹配到 ACD 组，比较严格按三级优先序：
    ① CLI 与 DDI 双匹配 → 立即应用该组；② CLI 匹配且路由表该项 DDI 留空 → 应用；
    ③ DDI 匹配且该项 CLI 留空 → 应用；全部不命中 → 回振铃音（不进 ACD）。
    排障含义：路由不生效先核对命中了哪一级、比较方向是否用反。
  key_details: |
    - 比较方向: CLI 从左向右比（starts from the left to the right）；DDI 从右向左比（starts from the right to the left）
    - 适用范围: 外部呼入与内部呼入均处理（p86）
  tags: [decision, call-characterization, cli, ddi, priority, routing]

- id: f14
  title: Smart Call Routing 路由表填写顺序规则与按国别/大客户分流规程
  type: 决策+规程
  source_pages: PAGE 88, 115-116
  source_quote: |
    "''Line parameters'' table management • Fill in the table beginning with the special case (the longest numbers)
    • Ending with the general case (the shortest numbers) ...
    If the accounts do not call the correct DDI, all the calls will be routed to ACD group 3"
  summary: |
    路由表（Line parameters，上限 10000 条，支持 CSV 导入导出）填写顺序是硬规则：
    从最特殊（最长号码）填到最一般（最短号码），否则一般条目会先截胡特殊条目。
    实验场景：按国别分流 UK(0044)→组1、Spain(0034)→组2、Germany(0049)→组3；
    三个大客户（Brest/Paris/Illkirch bank）以 CLI+DDI 双条件指向组1，
    且未拨对 DDI 时兜底落组3——即"双匹配条目在前、仅 CLI 国别条目在后、兜底最一般"。
  inputs: 国别前缀表、大客户 CLI/DDI 清单
  outputs: 按国家/大客户分流的 Line parameters 表
  steps: |
    1. OMC / Call distribution Services / ACD-SCR Services / Smart Call Routing
    2. 先填大客户双匹配条目（CLI + DDI → ACD group 1）
    3. 再填国别条目（仅 CLI: 0044→组1, 0034→组2, 0049→组3；DDI 留空）
    4. 最后填兜底最一般条目（→ ACD group 3）
    5. 实呼验证各国前缀与大客户号码的落组
  missing_conditions: 表内具体行序截图文字未提取（图像页），行间优先级以"特殊→一般"原则为准
  tags: [decision, procedure, routing-table, smart-call-routing, task-05]

- id: f15
  title: 坐席搜索模式三选一决策（Fixed / Rotating / Longest idle）与跨组优先级
  type: 决策
  source_pages: PAGE 95, 97, 109
  source_quote: |
    "Search mode • Fixed priority • Rotating priority • Longest idle period ...
    ACD group 1 has a ''fixed'' search mode, ACD group 2 has a ''longest idle period'' search mode,
    ACD group 3 has a ''rotating'' search mode. ... Do not forget to take into account the priority of the agents"
  summary: |
    组内选坐席的算法三选一：Fixed（按 rank 固定优先级）、Rotating（轮转）、
    Longest idle period（最久空闲优先）。与坐席 rank 是两个正交概念——rank 还用于
    坐席同属多组时"在找等待队列呼叫过程中的组间优先序"（Priority order, p97）。
    教材要求三种模式都要实测对比（结合实验 rank 配置做行为验证）。
  key_details: |
    - 配置路径: OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / "Group 1-4" tab, "Search mode" 选项
    - 振铃上限与无应答处理见 f16；溢出见 f19
  tags: [decision, search-mode, rank, group-strategy, task-06]

- id: f16
  title: 排障：无应答呼叫走向分析（最大振铃 10s 与自动 off duty 移除）
  type: 排障
  source_pages: PAGE 110-111
  source_quote: |
    "Validate the parameter Maximum ringing duration to 10 seconds. Make a call to the ACD No. Group 3 without any response ...
    the call is routed to extension 102 and extension 103 automatically swap to ''off duty'' status ...
    Then the call will definitely stay on extension 101."
  summary: |
    两档行为，用于诊断"来电没人接"类投诉：
    (A) 仅设最大振铃时长（实验值 10 秒）: 呼叫按组3 的 rotating 顺序 103 →(10s)→ 102 →(10s)→ 101 →(10s)→ 103 循环振铃；
    (B) 再启用 "Agents that do not answer are automatically removed": 103 振铃 10s 无应答后呼叫转 102、
    同时 103 自动转 off duty；102 再 10s 无应答转 101、102 转 off duty；最终呼叫停在最后一名在值坐席 101 上。
    诊断动作: 现场表现为"坐席陆续变成 off duty"时，先查该选项是否启用与振铃时长取值。
  key_details: |
    - 路径: OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / General tab
    - 两个选项: "maximum ringing duration"（=10 秒）与 "Agents that do not answer are automatically removed"
  tags: [troubleshooting, no-answer, ringing-duration, auto-removal, task-06]

- id: f17
  title: 队列长度决策公式（N × K，上限 16）
  type: 决策
  source_pages: PAGE 93
  source_quote: |
    "Let N be the number of agent in service and K the load factor
    • If N * K is not an integer , the value of the queue is the next higher integer
    • The maximum size of the queue is 16 (same for the maximum number of standard ACD ports)."
  summary: |
    队列长度 = 值机（On duty）坐席数 N × 话务因子 K（0.1 到 9.9），结果非整数时向上取整；
    上限 16，且 16 同时是标准 ACD 端口数上限。教材示例: 4 名 on duty 坐席 × K=0.5 → 队列最多 2 通。
    配置路径: General parameters / "Group 1-4" tab / Queue management menu。
  key_details: |
    - K 的语义: traffic or occupation factor（话务/占用因子）
    - 验证实验（p184）: 把组1 queue length 从 0.1 改 2.0，Agent 应用上观察队列容量从 1 变 4（两名坐席在值）
  tags: [decision, queue-length, formula, capacity, task-07]

- id: f18
  title: 预计等待时间公式与队列消息选项
  type: 决策
  source_pages: PAGE 94
  source_quote: |
    "Estimated waiting time = [(Number of call in the queue / number of agents on duty) + 1 ] X
    Average duration of ACD conversations ... After selecting the ''Queue rank'' or the ''Queue time'' option,
    set up the parameter linked to the selected option."
  summary: |
    队列内播报的"预计等待时间"按线性公式估算，输入为队列呼叫数、on duty 坐席数与
    ACD 平均通话时长（Average duration 参数）。队列消息二选一或组合:
    "Queue rank"（播队列最低排名）或 "Queue time"（播预计等待时间），选定后须设置对应触发参数
    （对应 f03 的阈值判定）。批判提示: 这是线性简化模型，高峰期会低估等待。
  key_details: |
    - 参数: Average duration of ACD conversations（估算基准）
  tags: [decision, queue, waiting-time, formula, task-07]

- id: f19
  title: 组间溢出（Group overflow）机制
  type: 框架
  source_pages: PAGE 96
  source_quote: |
    "After a timer of 10 s spent in a waiting queue: Overflow to an agent available in the ACD group 2"
  summary: |
    组1 队列中的呼叫在队列中停留满 10 秒定时器后，溢出到组2 的空闲坐席接听。
    机制要点: 溢出目标需组间存在坐席重叠/优先序配置（与 f15 的 Priority order 相关）；
    诊断"为什么别组的坐席接了本组电话"时先查此定时器与组间关系。
  key_details: |
    - 教材仅给 10s 定时器与"组1 队列 → 组2 空闲坐席"的行为图
  missing_conditions: 溢出定时器的配置入口与可调范围书中未写明（页面为示意图），标缺口
  tags: [framework, overflow, queue, cross-group]

- id: f20
  title: 营业时段与例外日配置规程（每周时段 + 40 闭/10 开/每日 2 时段）
  type: 规程
  source_pages: PAGE 100, 108
  source_quote: |
    "Exceptional closing days • Possibility to define a maximum of 40 closing days •
    Exceptional opening days • Possibility to define a maximum of 10 opening days •
    A maximum of 2 times ranges per opening day can be managed"
  summary: |
    营业日历 = 每周常规时段 + 例外日两层。常规: 组开放周一至周五 08:00-12:00 与 13:00-18:00；
    例外关闭日上限 40 天（实验: 1 月 1 日、5 月 1 日、12 月 25 日）；
    例外开放日上限 10 天（实验: 组1 于 12 月 25 日 9:30-11:30 例外开放）；
    每个开放日最多 2 个时段。例外日按组分别定义。
  inputs: 客户营业时间表与节假日清单
  outputs: 每组的 Opening time slots + Exceptional days 表
  steps: |
    1. OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / "Group 1-4" tab
    2. 选中 ACD 组 → 点 Opening criteria 图标 → 填每周开放时段
    3. Tab "Exceptional days": 选择列表显示方式（opened / closed / both）→ 按组填例外关闭日与例外开放日
  missing_conditions: 例外日日期格式与跨年处理书中未展开
  tags: [procedure, opening-hours, exceptional-days, calendar, task-08]

- id: f21
  title: Login/Logout 与 free seating 流程（含 ACDAutoLog 登录后默认状态）
  type: 流程+决策
  source_pages: PAGE 119-123
  source_quote: |
    "The entry to the ACD process is effective as soon as a common link is built for the following components:
    The agent name, The ACD group, The terminal ... ACD prefix with base 0: prefix to logout • ACD prefix with base 1: prefix to login ...
    Value 01: agent is ''on duty'' after login session (Default value) Value 00: agent is ''off duty'' after login session"
  summary: |
    坐席进入 ACD 会话的条件是四要素建链: 坐席名 + ACD 组 + 终端（+坐席号）。
    默认 free seating 模式: 任意终端拨登录前缀即可与所选坐席建立关联，同一 ACD 按键页签
    Login/Logout 同键切换。登入后默认状态由隐藏寻址项 ACDAutoLog 控制: 01=on duty（默认），00=off duty。
    排障含义: "登录了却不接电话"先查 ACDAutoLog=00 或登录后状态停在 off duty。
  inputs: 终端（任意类型: 模拟/DECT/IP/TDM/PIMphony）、坐席账号与密码（若配置）
  outputs: 终端-坐席-组的 ACD 会话建立
  steps: |
    登录: 拨 ACD 前缀（login code，base 1）或按 ACD 页签 "Login" 键 → 选坐席
    （ALE Essential/Enterprise 按姓名选；模拟话机与 DECT 按坐席号选）→ 若配置了密码则输入 → 终端登录完成
    登出: 拨 ACD 前缀（logout code，base 0）或按 "Logout" 键 → Essential/Enterprise 需按 OK 确认，
    模拟/DECT 无需确认 → 终端登出
  missing_conditions: ACDAutoLog 的具体写入路径书中未给（仅称 "Noteworthy address called ACDAutoLog"），标缺口
  tags: [flow, decision, login-logout, free-seating, acdautolog, task-09]

- id: f22
  title: 排障：话机 ACD 状态码解读（ACD 页签键位显示）
  type: 排障
  source_pages: PAGE 122
  source_quote: |
    "• 1:01 = Agent doesn't belong to ACD group 1 which is open, and 1 calls are in the queue.
    • 1:01+ = Agent belong to ACD group 1 which is open, 1 calls are in the queue and the queue is full.
    • 1-00 = Agent belong to ACD group 1 which is closed"
  summary: |
    Premium 8/9 系列话机 ACD 页签是坐席现场排障第一入口。状态键格式可解读为:
    "组号:等待呼叫数"，"+" 后缀表示队列已满，"-" 连接表示组处于关闭态；
    同一显示还存在"不属于该开放组"与"属于该开放组"两种变体（用符号差异区分）。
    处理路径: 读状态码 → 判断组态（open/closed）与队列负载（正常/满）→
    对照坐席登录状态（f21）决定干预动作。注意用导航键下翻 ACD 菜单可见更多功能项
    （On duty/Off duty/Clerical work/Temporary absence/Logout/Password/Groups）。
  key_details: |
    - 原文两行均为 "1:01"（一行指不属于组1、一行指属于组1），疑原文符号缺漏，解读时需实机核对
  missing_conditions: 原文符号体系不完整（两条 1:01 重复），"属于/不属于"的确切显示符号待实机确认，不脑补
  tags: [troubleshooting, terminal-status-code, acd-tab, agent-side, task-09]

- id: f23
  title: ACD 组显示模式框架（ACD mode vs Multi-Secretary mode）
  type: 框架
  source_pages: PAGE 89-90, 107
  source_quote: |
    "''Called ACD group identity'' displayed while the call is being transferred to the agent terminal.
    Once the call is transferred, the CLI is displayed. ...
    The information displayed on the set for the transfer of the call to the agent are
    [GROUP_NAME] [CALLING_NUMBER] [WAITING_TIME]"
  summary: |
    组级显示两模式: ACD mode 在呼叫转往坐席话机期间显示被叫 ACD 组标识，接通后改显主叫 CLI；
    Multi-Secretary mode 同一时段改显被叫号码（或姓名）——这是多秘书场景"秘书知道替谁接电话"的实现。
    无论选哪种模式，话机都会显示 ACD 进程耗时（等待队列 + 振铃时间）。
    转接中显示三元组: [GROUP_NAME 或被叫] [CALLING_NUMBER] [WAITING_TIME]。
    组名在 General parameters 的 Group 1-4 / Group 5-8 页签维护（实验: France/Spain/England），
    显示范围覆盖话机与三个客户端应用。
  key_details: |
    - 路径: OMC / Automatic Call Distribution / ACD Services ACD / General parameters（p90 写法）
      / OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / "Group 1-4" tab（p107 写法）
  tags: [framework, display-mode, multi-secretary, group-name]

- id: f24
  title: Multi-Secretary 配置全流程（医生/秘书案例 8 步）
  type: 流程
  source_pages: PAGE 126-146
  source_quote: |
    "Feature based on ACD engine (license needed) ... The secretary (ies) can provide a personalized reception
    according to the managers called thanks to the display of her station CALLED NUMBER (or the name ) +
    CALLING NUMBER + WAITING TIME ... Carry out the programming in the following order"
  summary: |
    Multi-Secretary 复用 ACD 引擎实现"多经理共享秘书团"（需许可）:
    经理 DDI 作为被叫特征（41505→505, 41506→506, 41507→507），秘书（101/102）作为坐席组全部 rank 1，
    关闭时段溢出到组邮箱，秘书 off duty/登出时走劝漏消息。
    教材明确要求按既定顺序编程。
  inputs: 经理分机与 DDI 清单（105/106/107 ↔ 41505/06/07）、秘书话机（101/102）、营业时段
  outputs: 多经理共享秘书方案（关闭时转邮箱）
  steps: |
    1. OMC/Automatic Call Distribution/ACD Setup/General tab — 按顺序录 3 个经理 DDI 并激活 Multi-Secretary 模式
       （41505: 505 / 41506: 506 / 41507: 507）
    2. ACD Setup/ACD Groups tab — 为秘书组建 voice mailbox（关闭时用）
    3. ACD Setup/ACD Profiles tab — 生成秘书（将任 Supervisor）的 profiles 并加 Services keys
    4. ACD Setup/Agents-Supervisors tab — 把 101/102 声明为 Supervisor 站（以便编程语音留言查询键）
    5. OMC/Automatic Call Distribution/ACD-SCR Services/Agents parameters — 在 ACD 引擎中建秘书账号，放入 3 组且均 rank 1
    6. ACD-SCR Services/Smart Call Routing Line parameters — 录入经理 DDI 号码
    7. OMC/Automatic Call Distribution/ACD-SCR Services/General Parameters（Group 1-4 tab）—
       开放时段周一至周五 8:00-19:00 + 溢出到邮箱；秘书 off duty/登出时用劝漏消息
    8. OMC/Collective speed dialing — 每位医生一条号码，让秘书席显示被叫姓名（DOCTOR A/B/C）
    9. OMC/Automatic Call Distribution/ACD Voice Messages — 定制语音（可 OMC 或话机 MMC:
       Menu/Operator/PASSWORD OP/Expert/Voice/ACD/ACD Group 1 to 3/Welcome...）
    10. 测试: 转接中话机显示 [CALLED_NUMBER] [CALLING_NUMBER] [WAITING_TIME]；接通后只显示 [CALLING_NUMBER]
  missing_conditions: Multi-Secretary 模式的激活开关具体控件名书中未单独说明（General tab 截图页），标缺口
  tags: [procedure, multi-secretary, managers-ddi, rank-1, task-10]

- id: f25
  title: Supervisor 应用部署规程（ACD Admin 密码 + 活动率周期 + 实时监控）
  type: 规程
  source_pages: PAGE 150-165
  source_quote: |
    "ACD statistic and Supervisor applications use a dedicated ACD admin password instead of installer password
    • In order to not communicate to the end customer the installer password ...
    For the ''Length of calculation period for agent activity rates'' option, select ''1/2 hour'' ...
    Admin ACD password : Acdc1064"
  summary: |
    班长实时监控台部署三段式: 先在 OMC 侧设 ACD Admin 专用密码（与 installer 密码分离，
    避免向最终客户泄露 installer 密码）与活动率计算周期；再装应用（MyPortal 下载）；
    最后首连配置并验证实时视图。Supervisor 可对坐席改组/rank/状态，对组改状态（open/closed/按时段）。
  inputs: OMC 管理权限、MyPortal 下载包 ACD_X.X\Alcatel\Call Center\Supervisor
  outputs: 可监控/干预坐席与组的班长台
  steps: |
    1. 设密码: OMC-> System Miscellaneous -> Passwords -> Management password（ACD Admin 级）
    2. 设活动率周期: OMC / ACD-SCR Services / General Parameters / "General" tab →
       "Length of calculation period for agent activity rates" = "1/2 hour"（可选过去一小时或半小时口径）
       同页可设 "Time delay before overload messages flash"（呼叫过载超时后监控屏红色告警框）
    3. 安装: 解压 → setup.exe
    4. 首连: 服务器 192.168.1.246、语言 English、Admin ACD 密码 Acdc1064（实验值）
    5. Parameters 菜单: 按组选受监控坐席
    6. 验证: Agent 菜单切换坐席状态看实时刷新; 打入约 5 分钟 ACD 通话，坐席 activity rate 应上升;
       Group 菜单观察来话信息并测试改组状态
  missing_conditions: 工具栏/监控图标语义两页（p158-159）为纯图，未提取
  tags: [procedure, supervisor, acd-admin-password, real-time-monitoring, task-11]

- id: f26
  title: 坐席实时子状态解读框架（On Duty 八子态）
  type: 框架
  source_pages: PAGE 164
  source_quote: |
    "On Duty - Awaiting call: the agent assigned to an ACD group is able to answer the next ACD call.
    - Not answering: a call has been presented to an agent, who is not answering.
    - Being routed: the agent's station is reserved for a call ... - Ringing ... - ACD busy ...
    - On hold: the agent has just hung up after an ACD call. The agent has rest time before another call ..."
  summary: |
    Supervisor 台上 On Duty 并非单一点，而是八个子状态: Awaiting call（待接）/
    Not answering（已呈现未接）/ Being routed（话机已预留、转接中）/ Ringing（振铃）/
    ACD busy（ACD 通话中）/ On hold（刚挂机休整期）/ Busy, outgoing call（外呼中）/ Not available（处理非 ACD 来话）；
    另有三态: Temporary Absence、Clerical work（通话后文书，暂离分配）、Off Duty（下班或未分配话机）。
    排障含义: "坐席显示忙却不接 ACD"对照子状态即可定位（如 Busy outgoing call / On hold）。
  key_details: |
    - 验证法: 打入约 5 分钟通话观察 activity rate 递增（p164）
  tags: [framework, agent-substates, supervisor, troubleshooting-support, task-11]

- id: f27
  title: Agent 应用部署规程（PC-终端关联 + qualification codes + screen popup 客户库）
  type: 规程
  source_pages: PAGE 99, 166-184
  source_quote: |
    "Architecture based on PC / Terminal association ... Once an ACD incoming call is routed to an agent using the
    Agent application, the agent can tag this call according to the kind of call they are involved with ...
    A screen popup should appear as soon as the call is distributed"
  summary: |
    坐席席面部署: 通话分类码（Types 表）先行定义，再装应用、建 PC-终端关联，
    最后验证状态切换、组变更、弹屏与打标四件事。通话中席面默认显示:
    CLI、DID、所属组、来话组名、等待+振铃耗时、通话时长、客户码关联入口。
    权限管理经 Admin 账户（受 OXO Connect Operator 密码保护）。
  inputs: 坐席 PC 与话机（实验: PC 关联终端 102）、Types 分类码定义
  outputs: 坐席席面（含弹屏与打标能力）
  steps: |
    1. OMC / ACD-SCR Services / General Parameters / "Types" tab — 定义通话分类码（坐席事后给来电打标，供统计）
    2. 安装: MyPortal 下载 ACD_X.X\alcatel\call_center\Agent_assistant → setup.exe
    3. 首连: Server name = 192.168.1.246；Extension number = 关联话机号（102）；选语言 → Connection
    4. 连接参数三要素（p170）: OXO IP 地址、关联分机号、可管理该分机的坐席名单
    5. 测试: 切 On duty/Clerical work/Temporary absence 并用 Supervisor 台核对;
       改坐席所属组并核对; 建客户联系人（Customers data base 图标 → Edit → New → 姓/名/电话 → OK），
       用该号码来电验证弹屏; 来电后在右侧下拉选分类码打标
  key_details: |
    - 来电信息含 DTMF Client code 字段（配合 f28）
    - p183 原文 "agent 1002" 疑为 102 笔误，按上下文（终端 102）理解
  tags: [procedure, agent-application, screen-popup, call-qualification, task-12]

- id: f28
  title: DTMF 客户识别弹屏流程
  type: 流程
  source_pages: PAGE 101-102
  source_quote: |
    "he is able to type a customer DTMF code (ex 035) allowing to generate a specific client information pop-up
    (Customer code=035) on the agent application ... ACD groups with code must be selected in the line parameters ...
    give the ''automatic screen pop up'' rights in the agent parameters"
  summary: |
    来电者在 ACD 语音提示下输入客户码（如 035#），坐席席面即弹出对应客户资料。
    三个前置缺一不可: Line parameters 中为该 ACD 组勾选客户码功能；
    OMC 中定制客户码提示音（107.wav，见 f30）；Agent parameters 中授予坐席
    "automatic screen pop up" 权限。排障: 弹屏不出现按此三点逐一核查。
  inputs: 客户码表（DTMF 码 ↔ 客户）、提示语音文件
  outputs: 来电弹屏（Customer code 关联客户资料）
  steps: |
    1. OMC Line parameters: 选中启用客户码的 ACD 组
    2. OMC: 定制 customer code announce（默认标签 107.wav 系）
    3. Agent 应用参数: 授予 "automatic screen pop up" 权限
    4. 实呼验证: 来电输 035# → 坐席席面弹出 Customer code=035
  tags: [flow, dtmf, client-identification, screen-popup, task-14]

- id: f29
  title: Statistics 应用部署与统计查询/导出规程（S1/S2 阈值）
  type: 规程
  source_pages: PAGE 185-209
  source_quote: |
    "S1 hold-on threshold value: 10 seconds (default value) S2 hold-on threshold value: 40 seconds (default value) ...
    Export of statistics files • Binary files • Used only by the Statistics application. ...
    • CSV files • Useful for clients who want to have customized statistics, reports and printouts"
  summary: |
    统计三件套的第三件: 使用前先核对 ACD 统计阈值参数（S1=10 秒、S2=40 秒默认，另有
    "Waiting begins before overflow time delay" 开关），再建连接、按组/按坐席查数、
    设置自动打印并按 binary/CSV 两种格式导出。统计留存最长 14 个月（p28）。
  inputs: OXO 主 CPU 上的统计文件（需连接检索）、ACD Admin 密码
  outputs: 组/坐席统计报表（图表+表格）、自动打印、导出文件
  steps: |
    1. 核参数（p190）: S1 hold-on threshold = 10 秒（默认）、S2 hold-on threshold = 40 秒（默认）、溢出前等待开关
    2. 安装: 下载 ACD_X.X\alcatel\call_center\Statistics_manager → setup.exe
    3. 首连: Configuration 菜单 → 选 "PBX Server" → 填 OXO IP 192.168.1.246 → 选语言 → 确认 IP →
       输 ACD Admin 密码 Acdc1064（实验值）→ 点 "ACD" 图标进统计
    4. 组统计: Group Statistics → Statistic tab 选组（1,2,3）与日期 → Graphic options tab 选 Color + 3D Bar →
       Synthesis 选 Incoming calls / Answered calls; Number 菜单看 Absolute value / Time
    5. 坐席统计: Agent Statistics → Agent tab 选 All、Group 选 1,2,3 → 选起止日期 →
       Options 选 Summary/Number of calls 与 Summary/Average duration
    6. 打印: 手动（Group/Agent statistics 菜单 → Printing）或自动（两个 Automatic printout 图标配 printing profiles）
    7. 导出: Export 图标 → 选格式（binary: 仅本应用可用，可取全量本地再分析; csv: 交外部应用做定制报表）→
       选保存路径与日期范围 → Export
  missing_conditions: Line statistics / Calls statistics 两图标（p192）教材未展开实验
  tags: [procedure, statistics, s1-s2-threshold, export, task-13]

- id: f30
  title: ACD 语音提示定制规程（wav 编号对照 + MMC 录制 + OMC 上传四步）
  type: 规程
  source_pages: PAGE 104-105, 135-136
  source_quote: |
    "Prompts can be recorded via a MMC session via a terminal • Alcatel-Lucent 8 and 9 series: Attendant session ...
    Customer code announce 107.wav 207.wav 307.wav 407.wav 507.wav 607.wav 707.wav 807.wav ...
    Respect the assignments 101.wav = welcome message, 102.wav = waiting message, etc."
  summary: |
    每组最多 6 条语音提示，按固定 wav 编号管理（101=欢迎语、102=等待语，以此类推;
    客户码提示为 x07.wav 系列，组 1-8 对应 107-807）。制作路径二选一:
    话机 MMC 会话录制（8/9 系列: Attendant session/Expert/Voice/ACD），或 PC 制作 .wav 后
    经 OMC 四步上传。Multi-Secretary 的定制语音示例文本见 p135（医生场景逐条话术）。
  inputs: 定制 .wav 文件（须符合编号与格式要求）或可录制的 8/9 系列话机
  outputs: 各 ACD 组的定制语音包
  steps: |
    1. 确认编号对照: 101.wav=welcome message, 102.wav=waiting message, ...; customer code announce=x07.wav
    2. (路径A) 话机制作: MMC session → Attendant session/Expert/Voice/ACD → 逐组录制
    3. (路径B) OMC 上传四步: (1) Mode 切到 Transfer; (2) 勾选要下载的 prompts;
       (3) 指定定制 prompts 所在目录路径; (4) Load 上传
    4. 实呼验证各组提示音
  missing_conditions: .wav 具体格式参数（采样率/编码）书中以图呈现，文字未提取
  tags: [procedure, voice-prompts, wav-numbering, mmc, task-15]

- id: f31
  title: 培训/实验收尾恢复出厂规程
  type: 规程
  source_pages: PAGE 211
  source_quote: |
    "Erase the MLAA voice guides if used / Clear ACD voice guides if used /
    Return to ACD / SCR factory settings if used / OXO Cold Reset with the following settings:
    •User data •System data •Cloud connect data •Network, installer passwords and management data"
  summary: |
    交付/实验结束的设备还原路径: 清 MLAA 语音 → 清 ACD 语音 → ACD/SCR 恢复出厂 →
    OXO 冷复位（含用户数据、系统数据、Cloud Connect 数据、网络与 installer/管理密码）。
    用于把实验配置从客户设备上清除，避免遗留实验值密码。
  inputs: 已做过 ACD 实验的设备
  outputs: 恢复出厂态设备
  steps: 按上述四步顺序执行（教材仅给清单级粒度，未展开子菜单）
  missing_conditions: Cold Reset 各数据类的具体菜单路径书中未给，标缺口
  tags: [procedure, teardown, factory-reset, boundary]
```

---

## 覆盖率自检（对照 BOOK_OVERVIEW task-01~task-15）

| task_id | 是否覆盖 | 对应候选 |
|---|---|---|
| task-01 OMC 安装首连 | 到过 | f11 |
| task-02 IP 规划修改 | 到过 | f12 |
| task-03 基础 ACD 搭建 | 到过 | f08（向导五步）、f09（后台生成物）、f10（全规程） |
| task-04 六场景呼入处理 | 到过 | f01（总框架）、f02-f07（逐场景） |
| task-05 特征化路由表 | 到过 | f13（三级优先决策）、f14（填写顺序+分流规程） |
| task-06 搜索模式与无应答 | 到过 | f15（三选一）、f16（无应答排障） |
| task-07 队列管理 | 到过 | f17（N×K 公式）、f18（等待时间公式）、f19（溢出）、f03/f04（出口流程） |
| task-08 时段与例外日 | 到过 | f20 |
| task-09 Login/Logout 与状态码 | 到过 | f21（含 ACDAutoLog）、f22（状态码排障） |
| task-10 Multi-Secretary | 到过 | f24（另 f23 显示模式框架） |
| task-11 Supervisor 应用 | 到过 | f25、f26（子状态解读） |
| task-12 Agent 应用 | 到过 | f27 |
| task-13 Statistics 应用 | 到过 | f29 |
| task-14 DTMF 客户识别弹屏 | 到过 | f28 |
| task-15 语音提示定制 | 到过 | f30 |

**小结**: 15/15 全部到过。另收 task 清单外的框架/规程候选: f09（向导后台生成物）、f19（组间溢出）、f23（组显示模式）、f26（坐席子状态）、f31（收尾恢复出厂）。
**缺口标注（不脑补）**: f19 溢出定时器配置入口、f21 ACDAutoLog 写入路径、f22 状态码符号体系（原文两条 1:01 疑似缺漏）、f24 MS 模式激活控件名、f30 wav 格式参数、f31 Cold Reset 子菜单路径。
