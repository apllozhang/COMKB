# 案例提取（case extractor）— OXO Connect Call Center (OXOCXTE107EN Ed07)

> 提取器：case-extractor | 依据：BOOK_OVERVIEW.md + source_fulltext.txt 全文（218 页，索引不存在，回退全量扫描）
> **书的性质说明**：本书是 ALE 官方售后培训动手实验手册（讲义 + How-To 1:1 配比）。全书**没有作者亲历的真实事件**，所有"客户需求/场景"（三组 ACD、银行大客户、医疗中心）都是教学用的模拟情境，按规范一律标记 `worked_example`，不称为真实事件。
> **类型口径**：`完整实验`（How-To 章节动手实验）/ `场景小案例`（正文插图说明的模拟情境）/ `验证测试`（How-To 内 Test/"What happens?" 小节，书中均给出答案）。
> **实验环境总口径**（各条不重复展开）：RLAB 远程实验室（全虚拟化，POD 1-6 相互独立、配置相同）+ 公共资源（NAS 软件/许可、ITSP1 SIP 运营商模拟器 10.20.30.x）；Client PC 虚拟机（OXO_PC_CLIENT，192.168.1.100，预装 4 个 MicroSIP 内部分机 100-103 + 2 个公网 MicroSIP + 待装 IPDSP 作 104）；OXO Connect（改 IP 后 192.168.1.246）。仅当条目有特殊环境要求时单独标注。

```yaml
- id: c01
  title: OMC 安装并首次连接 OXO（证书、密码、客户信息）
  type: case
  case_type: 完整实验 (How-To)
  example_kind: worked_example
  source_chapter: OMC Installation (How to)
  source_page: p54-64
  env: RLAB POD；Client PC VM 需用 console 模式进入（RDP 要等改 IP 后才可用）；OMC 安装包在桌面 SOFTS OXO CONNECT 目录（NAS 网络盘）；出厂 IP 192.168.92.246、首登密码 pbxk1064
  goal: 在管理员 PC 上安装 OMC，以 Expert 模式 + 服务器认证连接 OXO，装证书消除安全告警，设置各账户密码并录入客户信息
  preconditions: RLAB POD 可用；能以 console 模式登录 Client PC VM
  steps: |
    1. 解压桌面 SOFTS OXO CONNECT 目录下的 OMC 压缩包，右键 setup.exe 选 Run as administrator；
    2. 选安装语言 → Next → 选目标文件夹 → 选 Country/Distribution Channels → 选 Target Product → 选 OMC 显示语言 → Install → Finish；
    3. 打开 OMC，选 "Expert" 菜单，连接方式 LAN/WAN，填默认 IP 192.168.92.246，勾选 "Server authentication"，输入首连安装密码 pbxk1064；
    4. 弹出 Security Alert → View certificate → Install certificate → 浏览选择 "Trusted Root Certification Authorities" → OK → Finish；
    5. 按培训师给定值设置各账户密码（每个客户密码必须不同；后续可在 OMC/Security 菜单改）；
    6. 录入客户信息（带 * 为必填），可选填供应商（装机技师）信息。
  expected: 连接成功后 OMC 右下角图标显示已连上 OXO，OMC 可开始客户配置（"OMC is ready to start with the customer configuration"）
  source_quote: |
    "Use console mode to connect to the PC Client VM (OXOC_PC_CLIENT) and install the OMC
    (available on the desktop, folder SOFTS OXO CONNECT). OXO Connect default IP address
    192.168.92.246. Password 1st login: pbxk1064." / "Make a connection to the system with
    OMC in Expert mode with server authentication."
  summary: 一切配置的前提实验：装机 → Expert 模式连接 → 证书入受信根 → 改密 → 录客户信息，形成可用的管理通道
  bound_to:
    - "task-01 安装 OMC 并首次连接 OXO"
    - "核心命题：所有配置经 OMC 完成，先有管理通道"
  outcome: 书中给出成功判据（右下角连接图标）；具体截图结果未说明
  tags: [case, worked_example, omc, installation, how-to]

- id: c02
  title: OXO 与客户端 PC 的 IP 规划修改
  type: case
  case_type: 完整实验 (How-To)
  example_kind: worked_example
  source_chapter: OXO Connect IP settings modification (How to)
  source_page: p65-68
  env: RLAB POD；依赖 c01（OMC 已可连接）；改 OXO IP 后 OXO 会重启，PC 改 IP 后才能用 RDP 连 Client PC VM
  goal: 把 OXO Connect 与客户端 PC 从出厂网段改到培训网段 192.168.1.x
  preconditions: c01 完成；console 模式进入 Client PC VM
  steps: |
    OXO 侧（OMC / Hardware and limits / Lan / IP configuration）：
    1. Boards 页：Main CPU 填 192.168.1.246；
    2. LAN Configuration 页：Mask 255.255.255.0，Default Router Address 192.168.1.254；
    3. DNS 页：DNS1 192.168.1.254，DNS2 10.20.30.254；
    4. DHCP 页：话机地址池 Start 192.168.1.10 / End 192.168.1.39；
    5. 点 OK 并重启 OXO Connect。
    PC 侧：IP 192.168.1.100，掩码 255.255.255.0，网关 192.168.1.254，DNS1 192.168.1.254，DNS2 10.20.30.254。
  expected: 改完并重启后，可用 "Remote Desktop Connection"(RDP) 直接连 Client PC VM（替代 console 模式）
  source_quote: |
    "With the OMC, change the OXO Connect IP settings: Address IP: 192.168.1.246, Subnet
    mask: 255.255.255.0, Default router address: 192.168.1.254, DNS 1: 192.168.1.254,
    DNS 2: 10.20.30.254, DHCP range: 192.168.1.10 to 192.168.1.39, Restart OXO connect."
  summary: 现场交付第一步的模板：OMC 菜单逐页填 IP 五件套 + DHCP 池，重启生效；PC 侧同步改
  bound_to:
    - "task-02 修改 OXO 与客户端 PC 的 IP 规划"
  outcome: 书中以"改后可用 RDP 连接"为成功判据；其余观察未说明
  tags: [case, worked_example, ip-planning, omc, how-to]

- id: c03
  title: POD 3 呼出/呼入号码规则示例（ITSP1 号码演算）
  type: case
  case_type: 场景小案例（号码规则演算示例）
  example_kind: worked_example
  source_chapter: SIP Carrier Simulator / Public and Emergency numbers
  source_page: p18-22（核心示例 p20-21）
  env: RLAB POD（PN=POD 号两位数，示例取 POD 3 即 PN=03）；ITSP1 SIP 模拟器（gateway1.itsp1.com / public.itsp1.com）；MicroSIP 公网/紧急 profile
  goal: 演算 ITSP1 模拟器下的拨号规则：PBX 送出号码与收到号码的 E.164 变换
  preconditions: SIP 中继按 p22 配置（SIP Gateway ITSP1G1，账号 pbxP/alcatel，安装号 210P41000，DDI 41100-41199 base 100）
  steps: |
    输入→演算结果（POD 3）：
    - 拨 0110312345 → PBX 送出 +33110312345（国内，area 1）
    - 拨 0044210312345 → +44210312345（国际，英国 44）
    - 拨 0610312345 → +33610312345（手机，area 6）
    - 拨 112 → +112 或 112（紧急，urgence3@itsp1.fr）
    - 呼入：公网用户拨 0210341102 或 33210341102 → PBX 收到 +33210341102，落到分机 102；从 PBX 3 自环（loop）拨同一号码亦同。
    分机外部号码规则：分机 100 的外部号 = 3321PN41100（POD 3 即 33210341100）。
  expected: 模拟器按别名（alias）规则应答：国家码 33/44、区域 1-7、PN 两位 POD 号，其余位固定；主号 3321PN12345
  source_quote: |
    "Call to Public and Emergency numbers from your PBX – Examples for POD 3 (PN = 03).
    Dialed number: 0110312345, Number sent by the PBX: +33110312345. Dialed number:
    0044210312345, Number sent by the PBX: +44210312345."
  summary: 全书所有"模拟公网呼入/呼出"实验的号码翻译基础：后续 ACD 实验的来话都用此规则从 MicroSIP 公网 profile 拨入
  bound_to:
    - "实验环境（RLAB + SIP 模拟器）——后续所有 ACD 呼叫验证的来话通道"
  outcome: 演算规则明确（输入→送出号码一一对应）；实际呼叫截图未说明
  tags: [case, worked_example, sip-simulator, itsp1, numbering]

- id: c04
  title: 基础 ACD 配置实验（客户要求的三 ACD 组）
  type: case
  case_type: 完整实验 (How-To)
  example_kind: worked_example
  source_chapter: Basic ACD Configuration (How to)
  source_page: p69-77
  env: RLAB POD；依赖 c01/c02；话机用 MicroSIP 100-103（101/102/103 为坐席，100 为班长/话务台）；语音包用 NAS 上的默认语音
  goal: 按客户需求搭建基础 ACD：状态前缀 501-504；三组 ACD（组1 前缀 505/DDI 41505，组2 前缀 506/DDI 41506，组3 前缀 507/DDI 41507）；三组邮箱；坐席/班长按键 profile；坐席分组与优先级；下载默认语音；验证
  preconditions: OMC 可用、IP 规划完成（c01/c02）
  steps: |
    1. 状态前缀核对：OMC / Automatic Call Distribution / ACD Setup / "General" tab（501 on duty，502 off duty，503 clerical work，504 temporary absence）；
    2. 关联 DDI：同 "General" tab，为三组加 DDI 41505/41506/41507；
    3. 三组邮箱：OMC / Automatic Call Distribution / ACD Setup / "ACD Group" tab；
    4. 生成 ACD 按键 profile：同菜单 "ACD Profiles" tab；
    5. 分配 profile：同菜单 "Agents / Supervisors" tab——分机 101/102/103 用 Agent profile，话务台 100 用 Supervisor profile；
    6. Line parameters：OMC / Call distribution Services / ACD-SCR Services / Smart Call Routing，按前缀与 DDI 管理线路参数；
    7. 坐席入组：OMC / Automatic Call Distribution / ACD Services / Agent parameters——组1: 101(rank1), 102(rank2)；组2: 102(rank1), 103(rank2)；组3: 103(rank1), 102(rank2), 101(rank3)；自定义坐席名，状态置 on duty；
    8. 语音下载：OMC / ACD / ACD Voice messages——选 "Transfer mode"（组 1,2,3）、"Default messages"、PC→PCX 传输；注意点列号可禁用不需要下载的组；
    9. 验证（见 c05）。
  expected: 三组可接听；欢迎语先播、随后转坐席（详见 c05 测试）
  source_quote: |
    "Three ACD groups are required by the customer and you must associate a DID number to
    each one: Group ACD n°1, internal prefix:505, DDI N°: 41505; Group ACD n°2, internal
    prefix:506, DDI N°: 41506; Group ACD n°3, internal prefix:507, DDI N°: 41507."
  summary: 全书核心交付实验：ACD Setup 向导（General/ACD Group/Profiles/Agents-Supervisors 四页签）一次成型 + ACD Services 精调（Line parameters、Agent parameters）+ 默认语音下载
  bound_to:
    - "task-03 搭建基础 ACD"
    - "核心命题：配置分两层——ACD Setup 向导 + ACD Services 菜单"
  outcome: 转入 c05 验证测试闭环；具体截图未说明
  tags: [case, worked_example, acd-setup, basic-configuration, how-to]

- id: c05
  title: 基础 ACD 验证测试（呼叫三组 + 四状态前缀）
  type: case
  case_type: 验证测试 (Test)
  example_kind: worked_example
  source_chapter: Basic ACD Configuration / 4 Check the ACD configuration
  source_page: p77
  env: 同 c04；需要能从外部（MicroSIP 公网 profile）及内部对 505/506/507 或 DDI 发起呼叫
  goal: 验证 ACD 配置生效
  preconditions: c04 完成
  steps: |
    1. 参数核对：OMC 检查 Subscribers list、Hunting groups list、Internal numbering plan、Public numbering plan 四处变化；
    2. 呼叫测试：对每个 ACD 组发起呼叫；
    3. 状态测试：用预定义前缀（501-504）及话机功能键，把坐席依次置 on duty / off duty / clerical work / temporary absent。
  expected: "Make a call to all the ACD groups to check that the group welcome message comes up first, followed by a transfer to an agent."（先播组欢迎语，随后转接到坐席）
  source_quote: |
    "Make a call to all the ACD groups to check that the group welcome message comes up
    first, followed by a transfer to an agent. Put the agents on 'on duty', 'off duty',
    'clerical work' and 'temporary absent' status using the pre-defined prefixes."
  summary: 以行为验证闭环收束基础实验：听欢迎语 + 收到转接即判通过；四状态前缀逐一拨测
  bound_to:
    - "task-03 搭建基础 ACD（验证环节）"
    - "task-09 状态前缀操作（前置接触）"
  outcome: 书中给出明确判据（欢迎语→转坐席）；具体听感/截图未说明
  tags: [case, worked_example, test, verification, acd]

- id: c06
  title: ACD 组命名实验（France / Spain / England）
  type: case
  case_type: 完整实验 (How-To) 的一节
  example_kind: worked_example
  source_chapter: Advanced ACD configuration (How to) / 1 ACD group names management
  source_page: p107
  env: RLAB POD；依赖 c04（在基础实验的三组之上命名）
  goal: 把三组命名为 Group ACD n°1: France、n°2: Spain、n°3: England，并使名字在话机/应用上显示
  preconditions: c04 完成
  steps: |
    1. OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / "Group 1-4" tab——填组名；
    2. OMC / Automatic Call Distribution / ACD-SCR Configuration / General tab——校验组名显示。
  expected: 组名显示在话机、Agent/Supervisor 应用和 Statistics 上；转接阶段话机显示格式为 [GROUP_NAME] [CALLING_NUMBER] [WAITING_TIME]
  source_quote: |
    "Compared to the 3 ACD groups created in the TP basic ACD Configuration, name the ACD
    as follow: Group ACD n°1: France, Group ACD n°2: Spain, Group ACD n°3: England." /
    "The information displayed on the set for the transfer of the call to the agent are
    [GROUP_NAME] [CALLING_NUMBER] [WAITING_TIME]."
  summary: 组名是后续所有实验（搜索模式、劝漏、关闭）里三组的别名：1=France、2=Spain、3=England
  bound_to:
    - "task-04/05/06 的高级配置前置（组命名与显示）"
  outcome: 显示格式明确给出；实际截图未说明
  tags: [case, worked_example, group-names, display]

- id: c07
  title: 营业时段与例外日配置实验（含 12 月 25 日仅组 1 开放）
  type: case
  case_type: 完整实验 (How-To) 的一节
  example_kind: worked_example
  source_chapter: Advanced ACD configuration (How to) / 2 Time ranges management
  source_page: p108
  env: RLAB POD；依赖 c04/c06
  goal: 组时段：周一至周五 08:00-12:00 与 13:00-18:00；例外关闭日：1 月 1 日、5 月 1 日、12 月 25 日；例外开放：仅组 1 在 12 月 25 日 9:30-11:30 开放
  preconditions: c04 完成
  steps: |
    OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / "Group 1-4" tab：
    1. 填各组的 Opening time slots；
    2. 选中要配置的组，点 Opening criteria 图标；
    3. 切到 "Exceptional days" 页签，填例外关闭/开放日。
  expected: 时段外呼叫进入 closed 状态处理（见 c13 的行为）；例外日优先于每周时段
  source_quote: |
    "The ACD groups will be open from Monday to Friday, from 08:00 to 12:00 and 13:00 to
    18:00. In addition, ACD groups will be closed 1 January, 1 May and 25 December. Only
    the Group ACD n°1 will be open December 25 from 9:30 to 11:30."
  summary: 营业日历实验：每周时段 + 40 个例外关闭日/10 个例外开放日容量（讲义 p100）+ 每开放日最多 2 个时段
  bound_to:
    - "task-08 配置营业时段与例外日"
  outcome: 配置要求明确；呼叫行为验证并入 c13；实际截图未说明
  tags: [case, worked_example, opening-hours, exceptional-days]

- id: c08
  title: 三种搜索模式对比配置实验（Fixed / Longest idle / Rotating）
  type: case
  case_type: 完整实验 (How-To) 的一节
  example_kind: worked_example
  source_chapter: Advanced ACD configuration (How to) / 3 Configure the search mode
  source_page: p109
  env: RLAB POD；依赖 c04（坐席 rank 已按组1: 101>102；组2: 102>103；组3: 103>102>101 配好）
  goal: 组 1 用 fixed、组 2 用 longest idle period、组 3 用 rotating，并动手对比三种模式的分发差异
  preconditions: c04 完成（组内坐席与优先级已配）
  steps: |
    OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / "Group 1-4" tab，
    "Search mode" 选项：组 1 选 Fixed，组 2 选 Longest idle period，组 3 选 Rotating。
  expected: 书中 Notes 要求："Check the different search modes to compare the modes. Do not forget to take into account the priority of the agents defined in the previous exercise. Do practical tests."（结合坐席 rank 做实测对比）
  source_quote: |
    "ACD group 1 has a 'fixed' search mode, ACD group 2 has a 'longest idle period' search
    mode, ACD group 3 has a 'rotating' search mode." / "Do not forget to take into account
    the priority of the agents defined in the previous exercise. Do practical tests."
  summary: 组级分发算法实验：三种模式各占一组，便于横向对比；搜索模式与坐席跨组 rank 是正交概念
  bound_to:
    - "task-06 选择并验证坐席搜索模式"
  outcome: 具体分发结果留作学员实测，书中未给固定答案
  tags: [case, worked_example, search-mode, fixed, rotating, longest-idle]

- id: c09
  title: 最大振铃时长 10 秒实验：组 3 无人接听会怎样
  type: case
  case_type: 验证测试 (Test)
  example_kind: worked_example
  source_chapter: Advanced ACD configuration / 3.2 Maximum ringing duration parameter
  source_page: p110
  env: RLAB POD；依赖 c04/c08（组 3 = rotating，rank 103→102→101）；MicroSIP 公网 profile 来话
  goal: 把 maximum ringing duration 设为 10 秒，对 ACD 组 3 发起无人接听的来话，观察轮转行为
  preconditions: c08 完成（组 3 搜索模式 rotating）
  steps: |
    1. OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / General tab，
       选项 "maximum ringing duration" 设为 10 秒并 Validate；
    2. 向 ACD 组 3 发起来话，所有坐席都不接听；
    3. 观察 "What is going on?"。
  expected: "The incoming call comes first on extension 103 (if it's the first call for ACD group 3). After 10 seconds ringing, the call is routed to extension 102. After 10 seconds ringing, the call is routed to extension 101. After 10 seconds of ringing, the call is routed to extension 103 and so on."——即按 rank 轮转，每 10 秒跳下一个坐席，循环不止。
  source_quote: |
    "Make a call to the ACD No. Group 3 without any response from the agents. What is
    going on?" / "After 10 seconds ringing, the call is routed to extension 102. After 10
    seconds ringing, the call is routed to extension 101. After 10 seconds of ringing,
    the call is routed to extension 103 and so on."
  summary: 无应答轮转实验：rotating + 10 秒振铃上限 → 来话沿 103→102→101 循环巡游
  bound_to:
    - "task-06 搜索模式、最大振铃与无应答行为验证"
  outcome: 书中 Notes 直接给出答案（如上）；实际截图未说明
  tags: [case, worked_example, test, ringing-duration, rotating]

- id: c10
  title: "无应答自动移除实验：坐席被自动置 off duty"
  type: case
  case_type: 验证测试 (Test)
  example_kind: worked_example
  source_chapter: Advanced ACD configuration / 3.3 Agents that do not answer are automatically removed
  source_page: p111
  env: RLAB POD；依赖 c04/c08（组 3）；MicroSIP 公网 profile 来话
  goal: 启用 "Agents that do not answer are automatically removed" 后，观察无人接听时坐席被逐个移出分发
  preconditions: c08 完成；知晓 c09 行为作为对照
  steps: |
    1. OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / General tab，
       启用 "Agents that do not answer are automatically removed"；
    2. 向 ACD 组 3 发起来话，坐席都不接听；
    3. 观察 "What happens?"。
  expected: "The incoming call comes first on extension 103... After 10 seconds ringing, the call is routed to extension 102 and extension 103 automatically swap to 'off duty' status. After 10 seconds ringing, the call is routed to extension 101 and extension 102 automatically swaps to 'off duty' status. Then the call will definitely stay on extension 101."——无应答者被自动置 off duty 退出分发，最终来话钉在最后一个可用坐席（101）上。
  source_quote: |
    "Make an incoming call to ACD group 3 but the agents won't answer the call. What
    happens?" / "After 10 seconds ringing, the call is routed to extension 102 and
    extension 103 automatically swap to 'off duty' status... Then the call will definitely
    stay on extension 101."
  summary: 与 c09 形成对照实验：同样是无人接听，开了自动移除后坐席逐个掉线、呼叫不再循环
  bound_to:
    - "task-06 无应答自动 off-duty 配置与验证"
  outcome: 书中 Notes 直接给出答案；实际截图未说明
  tags: [case, worked_example, test, auto-removal, off-duty]

- id: c11
  title: 等待队列行为与队列出口验证实验
  type: case
  case_type: 验证测试 (Test)
  example_kind: worked_example
  source_chapter: Advanced ACD configuration / 4 Configure the waiting queue
  source_page: p112
  env: RLAB POD；依赖 c04/c06（组 1 = France）；至少两个来话源（坐席全忙时仍能发起呼叫）
  goal: 组 1 坐席全忙时来话进队列的行为；坐席空闲后的转接；按星号键退出队列；配置两种队列出口并逐一验证
  preconditions: c04/c06 完成
  steps: |
    1. 让组 1 坐席终端全忙或摘机，向组 1 发起来话，观察（答案：呼叫进入组 1 等待队列，先听欢迎语 1，再循环听等待语 2）；
    2. 让一个坐席变可用，观察（答案：队列中的呼叫被转给可用坐席）；
    3. OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / "Group 1-4" tab：
       点组 1 的 "Call distribution" 图标；队列出口点 "Call management" 图标；
    4. 先激活 "Place in group voice mailbox" 选项并按星号键验证流程；再改激活 "Transfer to a number" 选项再次验证。
  expected: 队列中主叫按 "*" 键可退出队列——留言到组邮箱，或转往预定义号码；两种出口逐一听测
  source_quote: |
    "What are the possible exits when the caller is on the waiting queue? The caller can
    exit the waiting queue by pressing the 'star' key in order to leave a message in the
    associated ACD group mailbox or to be routed to a pre-defined number."
  summary: 队列主流程实验：进队（欢迎语+循环等待语）→ 出队（坐席可用即转）→ 主动退出（星号键→邮箱/转号码）
  bound_to:
    - "task-07 配置等待队列"
    - "task-04 六种呼入场景之'全忙'场景出口"
  outcome: 书中以问答形式给出全部预期；实际截图未说明
  tags: [case, worked_example, test, queue, star-key-exit]

- id: c12
  title: 队列长度 0.1 的劝漏（dissuasion）实验
  type: case
  case_type: 验证测试 (Test)
  example_kind: worked_example
  source_chapter: Advanced ACD configuration / 5 Dissuasion status management
  source_page: p113
  env: RLAB POD；依赖 c04/c06（组 2 = Spain）；两个并发来话源
  goal: 把组 2 队列长度压到只容 1 个等待呼叫（因子 0.1），第二通来话触发劝漏，并验证劝漏的三种出口
  preconditions: c04/c06 完成
  steps: |
    1. OMC / Automatic Call Distribution / General parameters / "Group 1-4" tab / Queue management 菜单：
       "Queue length" 选项的因子值设为 "0.1"；
    2. 让组 2 坐席全忙（或摘机），向组 2 发起第一通来话，再发起第二通，观察（答案：第一通进组 2 等待队列；第二通进劝漏状态——主叫听到"坐席全忙请稍后再拨"之类的提示后呼叫被释放）；
    3. 劝漏出口改造：OMC / ... / "Group 1-4" tab / Group n°2，点 Call distribution 图标（Deterrence 流程）：
       先激活 "Place in group voice mailbox" 验证；再激活 "Transfer to a number" 验证。
  expected: 劝漏默认 = 播劝漏语音后释放；可改为留言进组邮箱，或转接预定义号码
  source_quote: |
    "The first call is put on ACD group 2 waiting queue. The second call is put on
    dissuasion status: the caller hears a message telling him, for example, that all the
    agents are busy and to try to call later. Then the call is released."
  summary: 劝漏第二形态实验：队列满（N×K 向上取整，0.1 因子即 1 个队位）→ 第二通被劝退；出口三选一
  bound_to:
    - "task-07 队列管理（队满出口）"
    - "task-04 六种呼入场景之'队满'场景"
  outcome: 书中以问答给出全部预期；实际截图未说明
  tags: [case, worked_example, test, dissuasion, queue-length]

- id: c13
  title: 组关闭（closed）状态实验
  type: case
  case_type: 验证测试 (Test)
  example_kind: worked_example
  source_chapter: Advanced ACD configuration / 6 Closed status management
  source_page: p114
  env: RLAB POD；依赖 c04/c06/c07（组 3 = England，已有营业时段）
  goal: 让组 3 处于关闭时段并来话，观察 closed 状态行为；再验证关闭状态的另外两种出口
  preconditions: c07 的时段配置完成
  steps: |
    1. 把 ACD 组 3 切到关闭时段（可用 Supervisor 应用改组状态或等时段外时间），向组 3 来话，观察；
    2. OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / "Group 1-4" tab / group 3，
       点 "Call distribution" 图标（"End" 流程）；
    3. 先激活 "Place in group voice mailbox" 并来话验证；再激活 "Transfer to a number" 再次来话验证。
  expected: 默认 closed 行为 = 播关闭语（示例文案："hot-line is open from Monday to Friday, from 8:00 AM to 12:00 PM and from 1:00 PM to 6:00 PM..."）后释放；可改为留言进组邮箱或转接预定义号码
  source_quote: |
    "The call is put on closed status: the caller hears a message telling him, for example,
    that the hot-line is open from Monday to Friday, from 8:00 AM to 12:00 PM (8h00 to
    12h00) and from 1:00 PM to 6:00 PM (13h00 to 18h00)... The call is then released."
  summary: 关闭状态实验：补全六场景中"组关闭"出口三件套（语音/邮箱/转接），方法与 c11/c12 同构
  bound_to:
    - "task-04 六种呼入场景之'组关闭'场景"
    - "task-08 营业日历的行为落点"
  outcome: 书中以问答给出预期与提示语示例；实际截图未说明
  tags: [case, worked_example, test, closed-status]

- id: c14
  title: 大客户路由案例：按国家分流 + Brest/Paris/Illkirch 三大银行
  type: case
  case_type: 完整实验 (How-To，客户场景)
  example_kind: worked_example
  source_chapter: Routing table configuration (How to) / 1 Manage the table "Line parameters"
  source_page: p115-116（匹配机制讲义 p86-88）
  env: RLAB POD；依赖 c04（三组与 DDI 41505-07 已建）；来话需能伪造不同 CLI（MicroSIP 公网 profile / ITSP1 别名规则）
  goal: 按 CLI/DDI 组合设计 Smart Call Routing 路由表：国家分流（UK→组1、Spain→组2、Germany→组3）+ 三大银行专线（对上正确 DDI 进组 1，拨错 DDI 一律进组 3）
  preconditions: c04 完成；理解呼叫特征化三级比较（p87）
  steps: |
    客户需求（原文）：
    - All calls from UK (0044) → ACD group 1；Spain (0034) → group 2；Germany (0049) → group 3；
    - 专组给三大账户：
      Brest bank   CLI 02.98.11.22.33  DDI XX.XX.XX.X5.05 → ACD group 1
      Paris bank   CLI 01.30.40.50.60  DDI XX.XX.XX.X5.06 → ACD group 1
      Illkirch bank CLI 03.90.80.70.60 DDI XX.XX.XX.X5.07 → ACD group 1
    - If the accounts do not call the correct DDI, all the calls will be routed to ACD group 3。
    配置入口：OMC / Call distribution Services / ACD-SCR Services / Smart Call Routing（Line and SCR parameters）。
    匹配逻辑（讲义 p86-88，实现本表依据）：
    - 三级优先比较：#1 CLIn=CLIt 且 DIDn=DIDt（CLI+DDI 双匹配）；#2 DIDn=DIDt 且 CLIt 空（仅 DDI 匹配）；#3 CLIn=CLIt 且 DIDt 空（仅 CLI 匹配）；全不中→回铃音、不入 ACD；
    - 方向：CLI 比较从左向右，DDI（DID）比较从右向左；
    - 填表顺序：从最特殊（最长号码）填到最一般（最短号码）。
  expected: 银行账号拨对自己的 DDI（尾缀 .05/.06/.07）→ 双匹配优先级 #1 命中 → 组 1；拨错 DDI → #1 不中、#2 不中（CLI 非空）→ 落到 #3 仅 CLI 匹配规则 → 组 3。国家规则为仅 CLI 匹配（DDI 空）。
  source_quote: |
    "All calls from UK (0044) will be routed to the ACD group 1... If the accounts do not
    call the correct DDI, all the calls will be routed to ACD group 3." / "CLI comparison
    CLIn / CLIt starts from the left to the right. DIDn / DIDt comparison starts from the
    right to the left. Fill in the table beginning with the special case (the longest
    numbers), ending with the general case (the shortest numbers)."（后段引自 p88）
  summary: 全书最核心的路由设计案例：用三级优先级 + 填表顺序规则，同时实现"国家分流"与"大客户拨错 DDI 兜底进组 3"。注意：书中仅给出需求与菜单入口，具体路由表逐行填法在截图里、正文未展开，属学员按 p87-88 机制自行完成的部分；"拨错 DDI 全进组 3"按三级机制推断需为三家银行 CLI 各配一条 DDI 空白的仅 CLI 规则指向组 3（此为机制推演，原文未逐行列出）
  bound_to:
    - "task-05 设计呼叫特征化路由表"
    - "核心命题：CLI+DDI 双匹配 > 仅 DDI > 仅 CLI，特殊→一般填表"
  outcome: 需求与匹配机制原文明确；逐行路由表与实测结果未说明（截图内容，正文无）
  tags: [case, worked_example, call-characterization, smart-call-routing, cli-ddi, major-accounts]

- id: c15
  title: 医疗中心多秘书场景设计（三位医生的语音与分流剧本）
  type: case
  case_type: 场景小案例（正文插图说明）
  example_kind: worked_example
  source_chapter: Multi secretary / Presentation of the Multi secretary function
  source_page: p127
  env: 概念场景（无需环境）；落地实验见 c18
  goal: 用多秘书功能给"医疗中心"设计完整来话剧本：欢迎语→按医生分流→排队/劝漏/关闭四类出口
  preconditions: 无
  steps: |
    场景要素：Doctors A, B, C；来话指向 DDI A/B/C；
    - 欢迎语："Welcome to the medical center"；
    - 应答：按被叫医生显示 "Secretary of doctor A/B/C, may I help you…"；
    - 等待队列："The secretaries are already on line, please hold on"；
    - 劝漏："All our secretaries are occupied, please callback later"；
    - 关闭："Our offices are open from 8h to 19h, you will be transferred to our voice mail box"。
  expected: 秘书席面显示 CALLED NUMBER（或名字）+ CALLING NUMBER + WAITING TIME，实现"按被叫医生个性化接待"
  source_quote: |
    "Doctors A, B, C. Multi secretary. 'Welcome to the medical center'... 'Secretary of
    doctor A, may I help you…'... 'The secretaries are already on line, please hold on'...
    'All our secretaries are occupied, please callback later'."
  summary: Multi-Secretary 的完整业务剧本样例：一段欢迎语 + 三套医生专属应答 + 队列/劝漏/关闭三出口文案，是 c18 实验的业务蓝本
  bound_to:
    - "task-10 配置 Multi-Secretary（需求侧蓝本）"
  outcome: 场景文案完整给出；未涉及配置与实测
  tags: [case, worked_example, multi-secretary, scenario, medical-center]

- id: c16
  title: 队列长度与预计等待时间公式演算示例
  type: case
  case_type: 场景小案例（正文演算示例）
  example_kind: worked_example
  source_chapter: Further ACD options / Queue management
  source_page: p93-94
  env: 无需环境（纸面演算）
  goal: 演算队列长度公式 N×K 与预计等待时间公式
  preconditions: 无
  steps: |
    输入：4 个 on duty 坐席（N=4），话务因子 0.5（K 取 0.1-9.9）；
    演算：N×K = 2（若非整数则向上取整），队列上限 16 → 本例队列长度 = 2，即最多 2 个排队呼叫。
    等待时间公式：Estimated waiting time = [(Number of call in the queue / number of agents on duty) + 1] × Average duration of ACD conversations。
  expected: 4 坐席 × 0.5 → "Maximum of 2 queued calls"；等待时间按公式由系统播报（配合 p38 队列消息 2 的"预计等待时间/最小排位"消息）
  source_quote: |
    "Let N be the number of agent in service and K the load factor. If N * K is not an
    integer, the value of the queue is the next higher integer. The maximum size of the
    queue is 16. 4 agents on 'On duty' status = 0.5 Traffic factor = Maximum of 2 queued
    calls."
  summary: 两条经验公式的唯一演算示例（输入 4×0.5→2）；c12 与 c21 是该公式的实测对照（0.1→1 队位、2.0→4 队位）
  bound_to:
    - "task-07 计算并配置等待队列（N×K 公式）"
  outcome: 演算结果原文明确（2 个排队位）；等待时间公式未配数值算例
  tags: [case, worked_example, queue-formula, calculation]

- id: c17
  title: DTMF 客户识别弹屏场景（客户码 035）
  type: case
  case_type: 场景小案例（正文插图说明）
  example_kind: worked_example
  source_chapter: Further ACD options / Client identification feature
  source_page: p101-102
  env: RLAB POD；依赖 c04；坐席侧需 Agent 应用（c20）；提示语 107.wav（客户码提示，见 p104）
  goal: 来电者输入 DTMF 客户码触发坐席席面弹出客户资料
  preconditions: c04 完成；该 ACD 组在 line parameters 中勾选"带客户码"
  steps: |
    1. Line parameters 中勾选启用客户码的 ACD 组；
    2. OMC 中定制客户码提示音（customer code announce，对应 107.wav 系）；
    3. Agent application 坐席参数中授予 "automatic screen pop up" 权限；
    4. 主叫呼入后按提示输码（例 035#）。
  expected: "he is able to type a customer DTMF code (ex 035) allowing to generate a specific client information pop-up (Customer code=035) on the agent application"
  source_quote: |
    "When a client calls the ACD, he is able to type a customer DTMF code (ex 035) allowing
    to generate a specific client information pop-up (Customer code=035) on the agent
    application. When a client calls this line, he is asked to type a code (e.g.: 035#)."
  summary: VIP 客户识别三件套：组勾选 + 107.wav 提示语 + 坐席弹屏权限；书内无独立 How-To，弹屏实测散在 c20 的客户库弹屏实验
  bound_to:
    - "task-14 配置 DTMF 客户识别弹屏"
  outcome: 机制与配置点明确；端到端 DTMF 弹屏实测书中未安排
  tags: [case, worked_example, dtmf, client-identification, screen-popup]

- id: c18
  title: Multi-Secretary 全流程实验（2 秘书共享 3 医生）
  type: case
  case_type: 完整实验 (How-To)
  example_kind: worked_example
  source_chapter: Multi secretary ACD feature (How to)
  source_page: p140-146（管理讲义 p128-139）
  env: RLAB POD；依赖 c04（复用 DDI 41505-07）；需 Multi-Secretary 许可；秘书席 101/102，医生席 105/106/107；语音可用 OMC 上传或话机 MMC 录制
  goal: 搭建"2 秘书（101/102）接听 3 位医生（DDI 41505/41506/41507 → 前缀 505/506/507）"的多秘书组；下班转邮箱；秘书席按名字识别被叫医生
  preconditions: c04 完成；Multi-Secretary 许可已装
  steps: |
    1. OMC/Automatic Call Distribution/ACD Setup/General tab：按顺序配 3 个 DDI——41505:505、41506:506、41507:507，并激活 Multi-Secretary 模式；
    2. 同菜单 ACD Groups tab：为组建邮箱（关闭时段用）；
    3. 同菜单 ACD Profiles tab：生成秘书（Supervisor）profile；
    4. 同菜单 Agents-Supervisors tab：把 101、102 声明为 Supervisor 席；
    5. OMC/Automatic Call Distribution/ACD-SCR Services/Agents parameters：秘书建入 ACD 引擎，三组均置 rank 1；
    6. 同菜单 Smart Call Routing Line parameters：加入 3 个 DDI；
    7. OMC/Collective speed dialing：为每位医生建一个显示名字（DOCTOR A/B/C，对应 505-507，便于内部测试）；
    8. OMC/Automatic Call Distribution/ACD-SCR Services/General Parameters：营业时间周一至周五 8:00-19:00，溢出转邮箱；
    9. OMC/Automatic Call Distribution/ACD Voice Messages：导入欢迎/排队/关闭语音（也可话机 MMC：Menu/Operator/PASSWORD OP/Expert/Voice/ACD/ACD Group 1 to 3/Welcome...），示例文案见 p135（"Welcome to Doctor's 1 Office"等六条）；
    10. Test（见预期）。
  expected: 测试答案（p146）：转接过程中秘书席显示 [CALLED_NUMBER] [CALLING_NUMBER] [WAITING_TIME]；转接完成后仅显示 [CALLING_NUMBER]。换拨另一个前缀，转接中显示格式相同但被叫号码不同。
  source_quote: |
    "This group contains 2 secretaries, stations 101 and 102. These secretaries answer the
    calls of 3 doctors, stations 105 (DDI 41505), 106 (DDI 41506) and 107 (DDI 41507).
    When the company is closed the calls are routed towards a voice mail box." / "Which
    information is displayed on the set during the call transfer toward the secretaries?
    [CALLED_NUMBER] [CALLING_NUMBER] [WAITING_TIME]."
  summary: 把"经理 DDI 当被叫特征化、秘书组当坐席组"的完整落地实验；验证了 Multi-Secretary 的显示协议（转接中三段式、接通后仅主叫）
  bound_to:
    - "task-10 配置 Multi-Secretary"
    - "核心命题：Multi-Secretary 复用 ACD 引擎"
  outcome: 测试问题书中给出标准答案；实际截图未说明
  tags: [case, worked_example, multi-secretary, doctors, how-to]

- id: c19
  title: Supervisor 应用部署与实时监控实验
  type: case
  case_type: 完整实验 (How-To)
  example_kind: worked_example
  source_chapter: Supervisor application ACD (How to)
  source_page: p160-165（讲义 p147-159）
  env: RLAB POD；依赖 c04；Supervisor 软件从 MyPortal 下载（NAS）；登录用 ACD Admin 密码 Acdc1064（教材实验值，仅限实验环境）；服务器 192.168.1.246
  goal: 配置坐席活动率统计周期，安装并登录 Supervisor 应用，实时监控/干预坐席与组
  preconditions: c04 完成；OMC 中已设 ACD Admin 密码（OMC-> System Miscellaneous -> Passwords -> Management password）
  steps: |
    1. OMC / ACD-SCR Services / General Parameters / "General" tab："Length of calculation period for agent activity rates" 选 "1/2 hour"；
    2. 从 MyPortal 下载 Supervisor 应用并解压（ACD_X.X\Alcatel\Call Center\Supervisor），运行 setup.exe；
    3. 启动应用：服务器名 192.168.1.246，文本语言 English，Admin ACD 密码 Acdc1064；
    4. Parameters 菜单：按组选被监控坐席；
    5. Agent 菜单：切换各坐席状态，确认实时视图联动；向某 ACD 组发起约 5 分钟来话，观察坐席活动率列上升；
    6. 验证 Supervisor 可改坐席的组/ rank/状态；Group 菜单中来话观察组信息，并可把组状态改为 open / closed / 按 ACD 组时段。
  expected: 坐席状态实时变化（Awaiting call / Not answering / Being routed / Ringing / ACD busy / On hold / Busy outgoing / Not available / Temporary Absence / Clerical work / Off Duty）；5 分钟来话期间坐席 activity rate 数值持续增大
  source_quote: |
    "Check the Agent activity by making an incoming call to an ACD group that lasts about
    5 minutes: the agent column should be increasing." / "Admin ACD password: Acdc1064."
  summary: 班长台三步走：OMC 设活动率周期 → 装软件用 Acdc1064 登录 → 用真实来话验证活动率与状态联动；顺带验证班长改组状态（open/closed/按时段）
  bound_to:
    - "task-11 部署 Supervisor 应用"
    - "核心命题：Supervisor/Statistics 必须用独立 ACD Admin 密码"
  outcome: 成功判据原文明确（活动率列上升）；具体截图未说明
  tags: [case, worked_example, supervisor-application, acd-admin-password, how-to]

- id: c20
  title: Agent 应用部署实验（状态联动/弹屏/呼叫限定/打标签）
  type: case
  case_type: 完整实验 (How-To)
  example_kind: worked_example
  source_chapter: Agent application ACD (How to)
  source_page: p180-184（讲义 p166-179）
  env: RLAB POD；依赖 c04；Agent 软件从 MyPortal 下载；PC 与分机 102 关联（free seating 的 PC-终端关联）；与 c19 联动互验
  goal: 定义呼叫限定码（Types），安装 Agent 应用并关联分机 102，验证状态联动、来话信息、改组、客户库弹屏、呼叫打标签
  preconditions: c04/c19 完成（需要 Supervisor 应用做对照）
  steps: |
    1. OMC / ACD-SCR Services / General Parameters / "Types" tab：定义 qualification codes（坐席给来话分类用）；
    2. 把运行 Agent 应用的 PC 与终端 102 关联；
    3. 从 MyPortal 下载解压（ACD_X.X\alcatel\call_center\Agent_assistant），运行 setup.exe；
    4. 首次启动填连接属性：服务器 192.168.1.246、分机号 102，选语言，点 "Connection"；
    5. 点 On duty / Clerical work / Temporary absence 图标，用 Supervisor 应用确认 102 状态同步；
    6. 向组 2 发起被 102 接听的来话，观察默认信息（答案见预期）；
    7. 在应用里改坐席所属组，用 Supervisor 应用核对（应用显示 ACD 组名列表框，改后 Supervisor 显示新配置）；
    8. 弹屏：Customers data base 图标 → Edit → New → 填姓/名/电话号码 → OK；用该号码作主叫呼入组 2 → 呼叫分配到坐席（原文写 agent 1002，疑为 102 之笔误）时弹屏出现；
    9. 再来一通组 2 来话，接通后在应用右侧滚动菜单选 qualification code 给来话打标签。
  expected: 来话默认显示：主叫号（CLI）、被叫号（DID）、坐席所属组、本次来话的 ACD 组名、等待队列+振铃耗时、通话时长、可关联客户码存入联系人档案
  source_quote: |
    "A screen popup should appear as soon as the call is distributed to agent 1002." /
    "Information that are displayed in the Agent application are: The caller number (CLI),
    the called number (DID), the group(s) to which the agent belongs, ACD group name
    involved by this call, the time spent on waiting queue + the ringing time."
  summary: 坐席席面全功能实验：状态与班长台双向联动、来话七要素、客户库弹屏（呼入号码匹配联系人档案）、通话后打 qualification 码
  bound_to:
    - "task-12 部署 Agent 应用"
    - "task-14 弹屏能力的实测载体（客户库弹屏）"
  outcome: 各测试书中给出答案；"agent 1002"为原文笔误（按上下文应为 102），实际截图未说明
  tags: [case, worked_example, agent-application, screen-popup, qualification]

- id: c21
  title: 队列因子 0.1 → 2.0 对照实验（用 Agent 应用读队列长度）
  type: case
  case_type: 验证测试 (Test)
  example_kind: worked_example
  source_chapter: Agent application ACD / 4 Check the size of the waiting queue
  source_page: p184
  env: RLAB POD；依赖 c04/c20（Agent 应用在线可读队列）；与 c12 的 0.1 配置形成对照
  goal: 修改组 1 的 queue length 话务因子，验证队列容量按 N×K 公式变化
  preconditions: c20 完成（Agent 应用已连上）
  steps: |
    1. OMC / ACD-SCR Services / General Parameters / "Group 1-4" tab：组 1 选项中把 "queue length" 参数从 "0.1" 改为 "2.0"；
    2. 用 Agent 应用观察组 1 等待队列长度变化（前提：组内坐席不全在 off duty）。
  expected: "Check that the queue length of the waiting queue of ACD group 1 changed from 1 to 4 calls"——0.1 因子时队位 1 个（4×0.1=0.4→向上取整 1），2.0 因子时队位 4 个（4×2.0=8？——按原文结果为 4，与 8 不符，原文以此为准；书中未给 2.0 的算式过程，实测结果 4 为准）
  source_quote: |
    "In the ACD group 1 options, change the 'queue length' parameter: put '2.0' instead of
    '0.1'. Check that the queue length of the waiting queue of ACD group 1 changed from 1
    to 4 calls (for this example, all the agents of the group are not in 'off duty'
    status)."
  summary: 队列公式的第二组实测点：0.1→1 队位（与 c12 一致）、2.0→4 队位；读书笔记：4 坐席 ×2.0=8 与观察值 4 不一致，书中未解释，此处如实记录存疑
  bound_to:
    - "task-07 队列公式实测验证"
  outcome: 观察值原文明确（1→4）；2.0 的理论值与实测不符之处原书未说明
  tags: [case, worked_example, test, queue-length, traffic-factor]

- id: c22
  title: Statistics 应用部署与报表实验
  type: case
  case_type: 完整实验 (How-To)
  example_kind: worked_example
  source_chapter: Statistics Application ACD (How to)
  source_page: p203-209（讲义 p185-202）
  env: RLAB POD；依赖 c04（最好先做 c19/c20 攒数据）；Statistics 软件从 BPWS 下载；登录密码 Acdc1064；S1/S2 阈值默认 10 秒/40 秒（p190）
  goal: 安装 Statistic Manager，取组 1/2/3 与全体坐席的培训期统计，以 3D 彩色柱状图呈现来话/应答/绝对值/时长各维度
  preconditions: c04 完成；OMC 里核对 S1=10s、S2=40s 阈值与溢出前等待时长开关（p190）
  steps: |
    1. 从 BPWS 下载解压（ACD_X.X\alcatel\call_center\Statistics_manager），运行 setup.exe；
    2. 首启配置：服务器 192.168.1.246，语言 English，ACD Admin 密码 Acdc1064；点 "ACD" 图标进统计；
    3. 组统计：Group Statistics → Statistics 页签选组 1、2、3 → 选期间（起止日期）→ OK；
    4. Options 页签选 Colour + 3D Bar；Graphic options → Synthesis → Incoming calls → OK 出图；同样路径出 Answered calls；
    5. Number 菜单 → Absolute value 任一选项 → OK 查看；Number 菜单 → Time 任一选项 → OK 查看；
    6. 坐席统计：Agent Statistics → Agent 页签选 "All"，Group 选 1、2、3 → 选培训起止日期；Options 配色与图型；先 Summary/Number of calls 再 Summary/Average duration 逐项查看。
  expected: 图形化呈现组与坐席的来话量、应答量、绝对值与时长统计；表格视图有 Absolute value/Percentage/Time 页签（p196）
  source_quote: |
    "During the first open the application, you must set the connection properties. Fill in
    the name of the server: 192.168.1.246... Enter the password ACD Admin: Acdc1064." /
    "Select 'Group Statistics'... Validate groups 1, 2 and 3... Select 'Colour' and '3D Bar'
    options."
  summary: 运营三件套收尾实验：装 → 连（专用密码）→ 组统计（含 3D 图）→ 坐席统计（全员全组、按培训期取数）
  bound_to:
    - "task-13 部署 Statistics 应用"
  outcome: 操作路径与取数范围明确；统计数值结果取决于实验期话务，书中未给样例数值
  tags: [case, worked_example, statistics-application, reports, how-to]

- id: c23
  title: 组溢出（overflow）机制示意案例
  type: case
  case_type: 场景小案例（正文插图说明）
  example_kind: worked_example
  source_chapter: Further ACD options / Group overflow
  source_page: p96
  env: 概念示意（无独立实验步骤）
  goal: 说明组间溢出：组 1 等待队列中呼叫在计时器到期后溢给组 2 空闲坐席
  preconditions: 无（理解用）
  steps: 图示场景：组 1 三坐席全忙，来话入等待队列；队列中停留 10 秒计时器到期后，呼叫溢出转给 ACD 组 2 中的可用坐席。
  expected: "After a timer of 10 s spent in a waiting queue: Overflow to an agent available in the ACD group 2"
  source_quote: |
    "After a timer of 10 s spent in a waiting queue: Overflow to an agent available in the
    ACD group 2."
  summary: 溢出仅以示意给出（组 1 队列 10 秒 → 组 2 空闲坐席），书中未安排配套动手实验
  bound_to:
    - "task-07 队列管理（组间溢出扩展）"
  outcome: 机制说明明确；实测未安排
  tags: [case, worked_example, overflow, illustration]

- id: c24
  title: 话机 ACD 页签状态码解读示例（1:01 / 1:01+ / 1-00）
  type: case
  case_type: 场景小案例（终端显示解读示例）
  example_kind: worked_example
  source_chapter: Login/Logout feature / Information on Alcatel-Lucent terminals
  source_page: p122-123
  env: ALE Essential/Enterprise（Premium 8/9 系列）话机显示；无需特殊环境
  goal: 一线排障时从话机 ACD 页签读出组状态与队列状态
  preconditions: 坐席已登录（free seating：前缀 base1 登录 / base0 注销，或 ACD 页签同键切换）
  steps: |
    读法（原书示例）：
    - 1:01 = 坐席属于 ACD 组 1、组开、队列有 1 个呼叫（两种原文写法，第二处明确"belong...open"）；
    - 1:01+ = 组 1 开、队列 1 个呼叫且队列已满；
    - 1-00 = 坐席属于组 1、组已关闭；
    - 登录后默认状态由寻址项 ACDAutoLog 控制：01=on duty（默认），00=off duty。
  expected: 按上述字段的"组号:队列数[+]/-"格式解读
  source_quote: |
    "1:01+ = Agent belong to ACD group 1 which is open, 1 calls are in the queue and the
    queue is full. 1-00 = Agent belong to ACD group 1 which is closed." / "Value 01: agent
    is 'on duty' after login session (Default value). Value 00: agent is 'off duty' after
    login session."
  summary: 排障速查型示例：话机 ACD 页签三段显示 + ACDAutoLog 隐藏寻址项；本书 Login/Logout 章仅讲义无独立 How-To，此为最接近"实操验证"的素材
  bound_to:
    - "task-09 配置坐席 Login/Logout 与 free seating（话机状态码解读）"
  outcome: 释义原文明确；配套实测未安排
  tags: [case, worked_example, acd-tab, status-codes, acdautolog, troubleshooting]
```

---

## 覆盖率自检（对照 BOOK_OVERVIEW task-01~15 中带实验性质的任务）

| task_id | 任务 | 覆盖案例 | 覆盖状态 |
|---|---|---|---|
| task-01 | 安装 OMC 并首次连接 | c01 (p54-64) | 完整（How-To 实验） |
| task-02 | 修改 IP 规划 | c02 (p65-68) | 完整（How-To 实验） |
| task-03 | 搭建基础 ACD | c04+c05 (p69-77) | 完整（How-To + Test） |
| task-04 | 六种呼入场景出口 | c11/c12/c13 (p112-114) + 讲义流程图 p36-42 | 完整（三场景实测：全忙/队满/关闭；空闲与端口全忙/全员登出场景仅讲义无独立实测） |
| task-05 | 呼叫特征化路由表 | c14 (p115-116，机制 p86-88) | 完整（需求完整；逐行路由表在截图、正文未展开，已标注） |
| task-06 | 搜索模式/振铃/无应答 | c08/c09/c10 (p109-111) | 完整（三模式各占一组 + 两个对照实验，答案齐全） |
| task-07 | 等待队列 | c11/c12 (p112-113) + c16 (p93-94) + c21 (p184) + c23 (p96 溢出) | 完整（公式 + 0.1/2.0 两组实测 + 出口验证；2.0→4 与 4×2.0=8 不符已如实记录存疑） |
| task-08 | 营业时段与例外日 | c07 (p108) | 完整（含"12 月 25 日仅组 1 开放"的例外开放配置）；行为落点见 c13 |
| task-09 | Login/Logout 与 free seating | c24 (p122-123) | **部分**——该章（p117-123）只有讲义，全书未配独立 How-To 实验；登录操作散见 c18（秘书登录）与 c20 的 PC-终端关联 |
| task-10 | Multi-Secretary | c15 (p127 场景) + c18 (p140-146) | 完整（场景蓝本 + 全流程实验 + 测试答案） |
| task-11 | Supervisor 应用 | c19 (p160-165) | 完整（含活动率上升判据） |
| task-12 | Agent 应用 | c20 (p180-184) | 完整（状态/信息/改组/弹屏/打标签五项实测） |
| task-13 | Statistics 应用 | c22 (p203-209) | 完整（组统计 + 坐席统计两段） |
| task-14 | DTMF 客户识别弹屏 | c17 (p101-102) + c20 步骤 8 | **部分**——配置点齐全但无端到端 DTMF 弹屏实测（c20 的弹屏是基于客户库号码匹配，非 DTMF 客户码触发） |
| task-15 | 定制语音提示 | c04 步骤 8（默认语音下载 p76）+ c18 步骤 9（定制语音 p146，文案样例 p135）+ 讲义 p104-105 | 完整（两条实操路径均有实验载体；无独立 How-To 章节，属于"内嵌步骤"形态） |

**结论**：15 项任务中 13 项有完整实验载体，2 项部分覆盖（task-09 无独立实验、task-14 无端到端 DTMF 实测），均已如实标注，未推测补齐。全书共提取 24 条记录：完整实验 9 条（c01/c02/c04/c06/c07/c08/c14/c18/c19/c20/c22 中按独立实验单元计）、验证测试 7 条（c05/c09/c10/c11/c12/c13/c21）、场景/演算小案例 8 条（c03/c15/c16/c17/c23/c24 及组命名等 How-To 内小节）。所有案例 `example_kind` 均为 `worked_example`（培训教材的模拟实验，无作者亲历事件）。

## 提取器自检清单

- [x] 每条案例都有 `bound_to`，绑定到 BOOK_OVERVIEW 的任务/核心命题
- [x] 每条有原文引用（均 ≤100 英文词）
- [x] `outcome` 尽量填；书中未给实测截图/数值的一律写"未说明"，未推测
- [x] 例题注明输入与演算结果（c03 号码演算、c16 队列公式；c21 的 2.0→4 与公式推算不符处原书未说明，已标注）
- [x] 不做筛选，全书 218 页全量扫描后按实验单元穷举
