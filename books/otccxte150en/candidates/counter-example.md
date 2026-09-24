# 反例/限制/边界/易错点候选 — OmniTouch CC Standard · Advanced Call Routing (OTCCXTE150EN Issue 01)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: CCS 安装必须勾选 ASM script 组件——漏装则全书能力无从谈起
  type: warning
  source_pages: p22
  source_chapter: How-To Basic CCD matrix creation
  source_quote: |
    "During the CCS installation don't forget to validate the ASM script component!!!"
  summary: |
    原书以三个感叹号强调：安装 CCS 时必须验证勾选 ASM script 组件。漏装后脚本编辑器/ASM 相关功能
    不可用，而原书没有给对应的排障路径——只能在 CCS 安装层面补救。
  conditions: CCS 安装阶段
  tags: [warning, ccs, installation]

- id: n02
  title: ACD 前缀是建一切 CCD 矩阵对象的前提
  type: limitation
  source_pages: p22
  source_chapter: How-To Basic CCD matrix creation / step 1
  source_quote: |
    "the ACD prefix is mandatory prior to create the CCD matrix objects"
  summary: |
    处理组、队列、Pilot 等对象创建之前必须先存在 ACD 前缀（Translator/Prefix Plan 核查）。顺序颠倒会
    直接卡在建对象这一步。
  conditions: CCD 矩阵初始搭建
  tags: [limitation, acd-prefix, ordering]

- id: n03
  title: ACD Station 类型（Agent/Supervisor）建户后不可修改
  type: limitation
  source_pages: p31
  source_chapter: How-To Basic CCD matrix creation / step 10
  source_quote: |
    "The ACD Station: Type Agent or Supervisor cannot be modified, must be selected during the creation of
    the user"
  summary: |
    用户的 ACD 站类型在建户时一次定型，之后不能改。把坐席建成主管（或反之）只能删号重建——批量开户
    前先核名单。
  conditions: 坐席/主管开户
  tags: [limitation, users, acd-station]

- id: n04
  title: 混合链路至少需要 2 个访问点成环，且邻接网络号必须异于本地
  type: limitation
  source_pages: p34
  source_chapter: How-To Basic CCD matrix creation / step 13
  source_quote: |
    "Adjacent Network Enter a different network number (different from the local network). Value from 0 to
    31 • Multi access hybrid link Set to YES. We need at least 2 accesses to make a loop … At least 2
    accesses needed. access 1 and access 2, or access 3 and access 4, …"
  summary: |
    三条硬约束：邻接网络号取 0-31 且不得等于本地网络号；Multi access hybrid link 必须置 YES；至少配
    2 个 access（1+2 或 3+4 成对）。漏配任何一条链路起不来——用 hybvisu -f all 核两个 access 均为
    "up"。
  conditions: 本地 CCD 呼叫的混合链路配置
  tags: [limitation, hybrid-link, abc-f]

- id: n05
  title: asm_ag_free_duration=0 时 LIT（最长空闲排序）不工作
  type: warning
  source_pages: p48-49
  source_chapter: How-To Manage a script / steps 5-6
  source_quote: |
    "Content of "parameters.cfg" asm_ag_free_duration 0 so, LIT is not working"
  summary: |
    Idle 规则期望"最长空闲"行为时，若 parameters.cfg 里 asm_ag_free_duration 还是默认 0（PLTR 语义），
    实测呼叫不会按最长空闲路由。要先改参数（0→1 单机 / 2 组网）再验证。
  conditions: Idle 规则 + LIT 期望行为
  tags: [warning, lit, parameters-cfg, idle]

- id: n06
  title: 改 parameters.cfg 后必须重启 MAIN_AFE 才生效
  type: limitation
  source_pages: p49, p264, p345
  source_chapter: Manage a script / Miscellaneous / External ASM How-Tos
  source_quote: |
    "Restart MAIN_AFE dhs3_init -R MAIN_AFE" (p49)
    "Restart the MAIN_AFE (dhs3_init -R MAIN_AFE) to take the change of parameters.cfg into account" (p264)
  summary: |
    parameters.cfg 的任何修改（asm_ag_free_duration、asm_on_dhs）都要 dhs3_init -R MAIN_AFE 重启 AFE
    进程才生效；原书三处重复强调。改完参数"没变化"先查是否重启。
  conditions: 参数文件变更后
  tags: [limitation, parameters-cfg, restart]

- id: n07
  title: 值 1 对应的旧 patchIdle 文件已废弃——版本迁移陷阱
  type: version-trap
  source_pages: p49
  source_chapter: How-To Manage a script / step 6
  source_quote: |
    "The value 1 is corresponding to the old patchIdle file. This file doesn't exist anymore. See next
    paragraph "Migration to parameters.cfg file""
  summary: |
    asm_ag_free_duration 的旧实现靠 patchIdle 文件，该文件已不存在，行为并入 parameters.cfg。沿用旧版
    资料找 patchIdle 文件会白费劲；且启用 LIT 还需系统版本 ≥l2.300.32.a（p241）。
  conditions: 旧版本系统升级 / LIT 排障
  tags: [version-trap, patchidle, parameters-cfg]

- id: n08
  title: 名单内坐席必须至少有 1 个活动技能，否则被排除
  type: limitation
  source_pages: p61, p81
  source_chapter: Authorized List lesson & How-To
  source_quote: |
    "An Agent belonging to a list must have at least 1 active skill" (p61)
    "The Agent 31501 cannot be rung, all other Agent can get the call, if they have at least 1 active skill." (p81)
  summary: |
    授权/非授权名单里的坐席若无任何活动技能，不参与分发——名单"写了人"不等于"人可用"。实验证据：
    非授权名单排除 31501 后，其余坐席能接的前提正是"有至少 1 个活动技能"。排障时先核技能再核名单。
  conditions: 名单规则运用
  tags: [limitation, authorized-list, skill]

- id: n09
  title: 名单 String 索引大小写敏感；关键字两种拼法混用
  type: warning
  source_pages: p74
  source_chapter: Authorized/Unauthorized How-To step 5
  source_quote: |
    "The String is case sensitive! You can use UNAUTHORISED_LIST ->%integer to define -> Integer = ID
    Number of the List"
  summary: |
    名单规则的 "String to define" 索引区分大小写（教材以感叹号强调）。另注意原书把
    AUTHORIZED/AUTHORISED、UNAUTHORIZED/UNAUTHORISED 两种拼写混用——以脚本编辑器实际接受为准，
    照抄书面前先在编辑器里核对。
  conditions: 名单规则脚本编写
  tags: [warning, case-sensitive, naming]

- id: n10
  title: Debugger 只能改既有构件、不能新增构件
  type: limitation
  source_pages: p80, p101
  source_chapter: Authorized/Unauthorized & Redirection How-Tos
  source_quote: |
    "You can only modify the existing Building Blocks, it is not possible to add a Building Block." (p80)
    "You can only modify the existing Building Blocks, it is not possible to add a Building Block." (p101)
  summary: |
    调试器支持实时改条件参数（如 IF TIME<10:0:0 改成 >），但不能加新构件——验证新逻辑必须回编辑器
    改脚本、重传重激活。两处 Note 原文一字不差，属刻意强调。
  conditions: Debugger 使用
  tags: [limitation, debugger]

- id: n11
  title: Redistribution 无可用方向时呼叫落 Blockage（封锁地址或语音引导）
  type: limitation
  source_pages: p89
  source_chapter: Redistribution lesson
  source_quote: |
    "Routing Direction available and open? If not, the call goes to Blockage mode"
  summary: |
    Redistribution 把呼叫退回"下一路由方向"，但方向不可用/未开时呼叫直接进封锁模式——若封锁地址也没
    配好，客户听到的是忙音类体验。配再分发兜底时必须同时配好第二优先方向或 Blockage 落点。
  conditions: Redistribution 路径设计
  tags: [limitation, redistribution, blockage]

- id: n12
  title: 直拨打到 ACR Pilot 的行为与普通 Pilot 不同
  type: warning
  source_pages: p120
  source_chapter: Direct Call and ACR Pilot How-To step 1
  source_quote: |
    "Direct Call the an ACR Pilot will not work in the same way as with a "normal" Pilot"（原文拼写如此）
  summary: |
    处理组 Pilot Direct Call 指向 ACR Pilot 后，直拨溢出行为与普通 Pilot 不同（可带 ASM 列表在等待房间
    等原坐席）。按普通 Pilot 经验预测直拨忙时行为会误判——必须按 ACR 语义验证。
  conditions: 直拨特性验证
  tags: [warning, direct-call, acr-pilot]

- id: n13
  title: DICA 技能停用即完全不可直拨（含空闲状态）
  type: limitation
  source_pages: p111
  source_chapter: Direct Calls & ACR lesson
  source_quote: |
    "If the "DirectCall" skill is not activated, it is no more possible to call the agent directly (whatever the
    agent status: idle, busy…) • The call is forwarded immediately to the "pilot direct call""
  summary: |
    坐席配私有号后自动获得的 DICA 技能是直拨的开关：停用后无论坐席空闲与否都无法直拨，呼叫立即转
    pilot direct call。用作"临时屏蔽直拨"的开关很方便，但排障时容易漏查这个自动技能的状态。
  conditions: 直拨排障 / 坐席技能管理
  tags: [limitation, dica, direct-call]

- id: n14
  title: 无 ACR 时直拨忙坐席不会"原地等待"——立即溢出可能换人接听
  type: misconception
  source_pages: p108
  source_chapter: Direct Calls & ACR lesson
  source_quote: |
    "Without ACR • In case of direct call on busy agent, there is an immediate call overflow on the pilot (declared
    as "pilot direct call") • So the call is then rerouted in the CCd matrix, and an agent, other than the one
    called initially, can be rung"
  summary: |
    "直拨某坐席、他忙就等着"并非系统默认行为：无 ACR 时直拨忙坐席立即溢出到 pilot direct call 并在矩
    阵内重路由，可能由别的坐席接听。"等原坐席"是 ACR 部署后靠脚本（等待房间 + CALL_TYPE）实现的增
    值能力。
  conditions: 客户需求沟通 / 方案设计
  tags: [misconception, direct-call, overflow]

- id: n15
  title: 一个 ACR Pilot 同一时刻只能激活 1 个脚本；非专用直拨 Pilot 需脚本兼容双来源
  type: limitation
  source_pages: p113
  source_chapter: Direct Calls & ACR lesson
  source_quote: |
    "Only 1 ACR script can be used at the same time on an ACR Pilot • If the "pilot direct call" is a dedicated
    one, which means that it cannot be called directly, the previous example could be interesting • If not
    dedicated, it would be better to create a script usable whatever the call origin (I/C on the pilot, direct call
    on agent)"
  summary: |
    两条设计约束：一个 ACR Pilot 同时只挂 1 个脚本；若直拨 Pilot 同时接普通来话（非专用），脚本必须用
    CALL_TYPE 分支兼容两种呼叫来源，否则直拨或来话必有一边路由错。
  conditions: ACR Pilot 规划
  tags: [limitation, script, pilot, design]

- id: n16
  title: 内部数据库 4000 条上限；主叫号键支持通配但容量按条计
  type: limitation
  source_pages: p131-132
  source_chapter: Internal Database lesson
  source_quote: |
    "Note: 4000 entries (single value or range) can be created in the Internal Database"
  summary: |
    内部数据库硬上限 4000 条（单值或区段均按条计）。大客户群个性化路由放内部库前先估算条数，超出
    需改用外部数据库方案（外部 ASM + SQL）。
  conditions: 内部库容量规划
  tags: [limitation, internal-database, capacity]

- id: n17
  title: Call Tag 想显示在坐席屏必须改处理组 display 参数；计时器取值有限制
  type: limitation
  source_pages: p156
  source_chapter: Internal Database How-To step 9
  source_quote: |
    "To display the "CALLTAG" on Agent screen, you must change the parameter "Display on agent screen" to
    Call tag or caller and pilot char. in the Agent Processing Group. • You also can manage the "Call Tag
    Display Timer" (Value 0, or 10 – 32767)"
  summary: |
    Call Tag 默认不上坐席屏——要改处理组参数 "Display on agent screen"（选 Call tag 或 caller and pilot
    char.）；显示计时器只能取 0 或 10-32767。注意脚本里 DISPLAY_AGENT 构件的屏显与该参数无关（两套
    机制，见 p253）。
  conditions: 坐席屏显示需求
  tags: [limitation, call-tag, display]

- id: n18
  title: 转移/转发链中最后一个 Call Tag / Call Profile 覆盖之前所有值
  type: limitation
  source_pages: p172-173, p189
  source_chapter: Call Profile or Call Tag / Transfer lesson & How-To
  source_quote: |
    "The last profile met in the call context overwrites the previous one" (p172)
    "The first CALLTAG "2500" will be overwritten be the CALLTAG of the Statistic Pilot 31650 (CALLTAG
    1500)." (p189)
  summary: |
    呼叫经 IAA/统计 Pilot/转发链时，标签与档案会被后到者覆盖（GFW 实验证实 2500 被 1500 覆盖）。设计
    "多级 IVR 打标"或"转发到另一个统计 Pilot"时，最终生效的标签是路径上最后一个——排障时按路径末端
    查，不要按入口标签查。
  conditions: Call Tag/档案传递与转发设计
  tags: [limitation, call-tag, transfer, overwrite]

- id: n19
  title: IAA 只能从外部呼入
  type: limitation
  source_pages: p211
  source_chapter: String handling How-To
  source_quote: |
    "IAA can only be called from external"
  summary: |
    自动话务员接入号不接受内呼。内部用户想走 IVR 式引导（按键选部门、输客户号）需另找入口（如直接
    呼统计 Pilot 或 CCivr），不要把 IAA 设计进内部流程。
  conditions: IVR 流程设计
  tags: [limitation, iaa, internal-calls]

- id: n20
  title: 改 IAA 配置前必须先停用（Valid=FALSE）改完再启用
  type: warning
  source_pages: p199
  source_chapter: String handling How-To step 1
  source_quote: |
    "First deactivate the Automatic Attendant Applications /Automated Attendant/Review-Modify Automated
    Attendant valid: FALSE … Activate the Automatic Attendant … valid: TRUE"
  summary: |
    修改 IAA 叶/树/接入前要先在 Review/Modify 把 Automated Attendant Valid 置 FALSE，改完再置 TRUE，
    中继组 Automated Attendant 属性也须为 YES。跳过停用直接改配置的生效行为原书未给保障。
  conditions: IAA 配置变更
  tags: [warning, iaa, configuration]

- id: n21
  title: CCivr TransferCall 构件前置要求 GetPilotInfo；代码长度上限 16 位
  type: limitation
  source_pages: p169-170
  source_chapter: Call Profile or Call Tag / Transfer lesson
  source_quote: |
    "Transfer to Pilot • Blind Transfer • Previous GetPilotInfo BB is required" (p170)
    "The code entry guide prompts the caller to dial a code (max code length = 16 digits)" (p169)
  summary: |
    两条 IVR 侧约束：CCivr 用 TransferCall 盲转前必须先执行 GetPilotInfo 构件；IAA 编码叶客户可拨代码
    最长 16 位（以 Correlator data 经 CSTA 传递）。构件顺序漏了或代码超长都会断链。
  conditions: CCivr/IAA 集成
  tags: [limitation, ccivr, iaa, correlator]

- id: n22
  title: Waiting Room 与 Waiting Queue 不能同开；同一路由规则不能同时开两个方向
  type: limitation
  source_pages: p13, p232
  source_chapter: ACR Introduction & Miscellaneous lesson
  source_quote: |
    "Waiting Room & Waiting Queue CANNOT be open at the same time" (p13)
    "Not possible to open both direction simultaneously in the same routing rule" (p232)
  summary: |
    结构性互斥：等待房间与等待队列不能同时打开；同一条路由规则里也不能同时开两个方向。设计 Pilot 的
    停放结构时只能二选一（ACR Pilot 用房间、普通 Pilot 用队列是教材的推荐形态）。
  conditions: Pilot/路由规则设计
  tags: [limitation, waiting-room, routing-rule]

- id: n23
  title: 启用 LIT 必须在脚本里显式加 IDLE 构件
  type: limitation
  source_pages: p242
  source_chapter: Miscellaneous lesson
  source_quote: |
    "NB: in the case where you wish to use the LIT a specific building block 'IDLE' must be added to the
    program."
  summary: |
    parameters.cfg 改成 LIT（1/2）只是开关，脚本里还得有 IDLE 构件才生效——两处配置缺一不可。排障
    "LIT 不生效"按 参数值 → 重启 AFE → IDLE 构件 三步顺序查。
  conditions: LIT 启用
  tags: [limitation, lit, idle]

- id: n24
  title: Idle 与 Com 规则互斥；asm_ag_free_duration 对 Com 无影响
  type: warning
  source_pages: p244, p265
  source_chapter: Miscellaneous lesson & How-To
  source_quote: |
    "Rule „IDLE" & Rule „COM" are exclusive Cannot be combined together" (p244)
    "The parameter asm_ag_free_duration has no impact on RULE_COM. The Agents are sorted according to the
    number of served calls ratio since logon!" (p265)
  summary: |
    两条排序规则语义警告：IDLE 与 COM 不能出现在同一 APPLY 组合里；asm_ag_free_duration 只改 Idle 的
    语义（PLTR/LIT），对 Com 的"服务呼叫数比率"排序完全无影响。想均匀派话用 Com，想照顾久坐空闲
    坐席用 Idle，别试图叠加。
  conditions: 排序规则选型
  tags: [warning, idle, com, exclusive]

- id: n25
  title: 两个 APPLY 时第一个失效——"名单+ISM"约束会被静默解除
  type: warning
  source_pages: p245-247, p268-270
  source_chapter: Miscellaneous lesson & How-To steps 3-4
  source_quote: |
    "When 2 "APPLY" instructions are encountered, the 1st one has no effect on the result sent back to the call
    handling" (p245)
    "The Agent list of "RULE_AUTHORIZED_LIST" is not considered as the input of the RULE_ISM. So, when the
    RULE_ISM is applied, all Agents with the right skills belonging to the final Agent list. Not only the Agents
    of the Authorized List, as in the previous example" (p270)
  summary: |
    全书最反直觉的语义：仅 1 个 APPLY 时前规则输出=后规则输入（名单真正过滤坐席）；≥2 个 APPLY 时各
    APPLY 独立、第一个结果被丢弃——ISM 会按全量坐席计算，授权名单形同虚设。实验对照：1Apply 仅
    31501 接、2Apply 中 31500（不在名单）也被呼。业务要求"名单+技能"必须用单 APPLY 链式写法。
  conditions: 规则组合脚本设计
  tags: [warning, apply, authorized-list, ism]

- id: n26
  title: 普通 CCD 呼叫 ISM 成本为无穷——ACR 呼叫默认插队
  type: limitation
  source_pages: p235, p282
  source_chapter: Miscellaneous lesson
  source_quote: |
    "Call parked in a waiting queue No ISM cost, so the cost is fixed to an unlimited value … CCd call (ISM
    cost=infinite)" (p235)
    "At equal Priorities & ACR Actual Waiting set to FALSE (Default value), the lowest ISM cost is used." (p282)
  summary: |
    等待队列（普通 CCD）呼叫 ISM 成本按无穷计，等优先级下永远排在 ACR 呼叫之后。这是设计特性但要向
    客户讲清：混跑场景普通来电可能被 ACR 呼叫持续插队，需要靠优先级或 ACR Actual Waiting=TRUE 平衡。
  conditions: CCD/ACR 混合站点
  tags: [limitation, ism-cost, call-selection]

- id: n27
  title: 过滤器不影响分发——它只是统计分组
  type: misconception
  source_pages: p285
  source_chapter: Filter & Statistics lesson
  source_quote: |
    "The call distribution is not impacted by the filters"
  summary: |
    过滤器常被误解为"路由条件"，实际只影响实时观测与统计报表的分组口径，完全不改变呼叫分发。想让某
    类呼叫优先，要改的是优先级/ISM 成本/脚本，不是过滤器。
  conditions: 监控与报表设计沟通
  tags: [misconception, filter]

- id: n28
  title: 新过滤器查不到创建前的 Excel 历史；预置 20 个过滤器兜底
  type: limitation
  source_pages: p302
  source_chapter: Filter & Statistics lesson
  source_quote: |
    "When a new filter is created, we cannot retrieve, in Excel files, data prior to the filter creation date
    • But, keep in mind that 20 predefined filters originally exist; so Excel files will be available using these
    filters"
  summary: |
    过滤器统计从创建时刻起算。月中要新口径报表时拿不到历史；临时救急可用系统预置的 20 个过滤器（它
    们有历史数据）。要新口径的长周期报表必须提前建过滤器。
  conditions: 统计报表规划
  tags: [limitation, filter, history, statistics]

- id: n29
  title: Filter（AND）与 Super-Filter（OR）结果差异——Filter 3 实验中零数据
  type: misconception
  source_pages: p312, p314
  source_chapter: Filter & Statistic How-To
  source_quote: |
    "Filter 3 will not have any Data: We do not have a Call_Profile with English, Car AND Home" (p312)
    "Filter use the Function "AND", a Super-Filer / Hyper-Filer use the Function "OR"" (p314, 原文拼写如此)
  summary: |
    把"三类技能都要"建成一个 Filter（AND 语义）通常得到零数据——没有呼叫会同时带三份技能需求；想统
    计"三类任一"要建 Super-Filter（OR）。报表口径沟通时先确认 AND/OR 语义，否则数字对不上。
  conditions: 过滤器口径设计
  tags: [misconception, filter, and-or]

- id: n30
  title: 安装外部 ASM 前必须 asm_on_dhs=0，否则 AFE 继续拉起内部 alb
  type: warning
  source_pages: p322, p345
  source_chapter: External ASM lesson & How-To step 1
  source_quote: |
    "you must disable the parameter "asm_on_dhs" in the "parameters.cfg" file • This must be done to use the
    external ASM server, so "AFE" will not start the "ALB" process of the OmniPCX Enterprise" (p322)
    "You must restart the PCX or to kill the alb process Check with "ps-edf |grep alb"" (p345)
  summary: |
    割接顺序陷阱：不把 asm_on_dhs 置 0 并重启 MAIN_AFE（必要时 kill alb），内部 ASM 还在运行，外部
    ASM 连不上 AFE（p353 明示）。割接外部 ASM 按 改参数 → 重启 → 核 alb 进程已停 → 再装服务 的顺序。
  conditions: 外部 ASM 部署
  tags: [warning, external-asm, asm-on-dhs, migration]

- id: n31
  title: 内部 ASM 未停则外部 ASM 无法连接 AFE
  type: warning
  source_pages: p353
  source_chapter: External ASM How-To step 4
  source_quote: |
    "If the Internal ASM server is not Stopped, you will not be able to make the connection from the External
    ASM Server to the AFE!"
  summary: |
    ASMServer Tool 建 Site 时连不上 AFE 的第一嫌疑就是内部 alb 还活着。先回 n30 的顺序核查，再查网络
    与凭据。
  conditions: 外部 ASM 链路排障
  tags: [warning, external-asm, connection]

- id: n32
  title: Windows 防火墙必须放行 ASM 与 ASMMgr 入站 UDP+TCP（Private）
  type: warning
  source_pages: p360
  source_chapter: External ASM How-To step 6
  source_quote: |
    "If the connection to the ASM Server is not possible, check you Windows Firewall configuration. Allow in
    the Inbound Rule ASM Protocol UDP and TCP in Private • Allow in the Inbound Rule ASMMgr Protocol
    UDP and TCP in Private"
  summary: |
    外部 ASM 装好后连不通的高频原因是 Windows 防火墙：需放行 ASM、ASMMgr 两条入站规则（UDP+TCP、
    Private 配置文件）。生产环境还要同步核查网络侧防火墙策略（书外）。
  conditions: 外部 ASM 网络排障
  tags: [warning, firewall, external-asm]

- id: n33
  title: localhost 仅在 hosts 文件配置时可用；服务须自动启动模式
  type: limitation
  source_pages: p327, p329
  source_chapter: External ASM lesson
  source_quote: |
    "Note: Service need to be started in Automatic Mode" (p327)
    "Note: localhost only works, if managed in the file "hosts" of the PC!" (p329)
  summary: |
    两条安装细节：ASM Windows 服务要设 Automatic 启动模式（否则重启后 ASM 不自愈）；ASM Manager 里
    用 localhost 连接仅在 PC 的 hosts 文件里配置了映射时有效——直接用 IP 最稳。
  conditions: 外部 ASM 安装
  tags: [limitation, external-asm, service, hosts]

- id: n34
  title: 脚本迁移必须复制 .scr 并重新编译；迁移后重启 ASM 服务
  type: limitation
  source_pages: p335
  source_chapter: External ASM lesson
  source_quote: |
    "To transfer the script from an internal to an external ASM server (and vice-versa), the "scr" file has to
    be copied and recompiled • Restart the ASM server (windows service) after script transfer"
  summary: |
    内部（OXE /usr3/afe）与外部（Program Files/Alcatel/Agent Selection Module/Script）的脚本文件不通用：
    迁移只能复制 .scr 源文件并重新编译（.alb 不跨环境），迁移完重启服务。直接拷 .alb 会得到不可用脚本。
  conditions: 内外 ASM 割接
  tags: [limitation, script-migration, scr, alb]

- id: n35
  title: 双机配置变更前必须停服务；OmniPCX 名必须被备机知晓
  type: warning
  source_pages: p331, p367, p371
  source_chapter: External ASM lesson & Duplicated How-To
  source_quote: |
    "To change the configuration, the external ASM service must be stopped with the ASMServer Service
    management menu" (p331)
    "The OmniPCX Name must also be known by the Stand-By ASM Server!!!" (p371)
  summary: |
    双机两坑：改 Main/Stand-By 角色前必须停 ASM 服务（配置界面会要求确认并重启服务）；备机上也要能
    解析 OmniPCX 名（hosts/DNS），否则主备切换后连不上 AFE。
  conditions: 双机外部 ASM 部署
  tags: [warning, duplicated-asm, service]

- id: n36
  title: ASM 服务器仅支持 32 位 ODBC——64 位驱动连不上（两处强调）
  type: limitation
  source_pages: p399, p433
  source_chapter: External Database How-Tos
  source_quote: |
    "The ASM Server is not able to make a connecting using a 64-Bit ODBC Driver" (p399, 原文拼写如此)
    "Take care, the ASM Server only allows a 32-bit connection" (p433)
  summary: |
    全书对外部库最强的环境约束：ODBC 必须 32 位（Access 与 SQL Server 两章重复强调）。现代 64 位服务
    器上找齐 32 位驱动（Access 的 *.mdb 驱动、SQL Server 32 位驱动）本身就是交付风险项；DSN 一律在
    "ODBC Data Sources (32-bit)" 里建。
  conditions: 外部数据库接入
  tags: [limitation, odbc, 32-bit]

- id: n37
  title: 外部库读写需要 167 号软件许可；外部 ASM 连接本身免许可
  type: limitation
  source_pages: p320, p376, p394
  source_chapter: External ASM & External Database lessons
  source_quote: |
    "If you need a connection to an External Database (MS SQL), a software license is needed in the PBX
    (Software License N° 167: "ACR data base read")" (p320)
    "option 61 (precise the lock ACR_SQL (167) availability)" (p394)
  summary: |
    许可边界：OXE↔外部 ASM 的连接不需要许可；脚本读/写外部数据库需要 OXE 软件许可 N°167 "ACR data
    base read"。可用 adm_acd 选项 61 核该锁可用性——脚本连不上库时先核许可再查网络。
  conditions: 外部数据库方案报价与排障
  tags: [limitation, license, external-database]

- id: n38
  title: 存储过程调用仅当目标数据库支持嵌入式过程
  type: limitation
  source_pages: p384
  source_chapter: External Database lesson
  source_quote: |
    "The feature is available only if the target database allows embedded procedures."
  summary: |
    CALL 存储过程能力依赖目标库支持嵌入式过程（Access 这类桌面库不支持过程，只能 SELECT；SQL
    Server/Oracle 可）。选库时按"要不要过程"定方案。
  conditions: 外部库选型
  tags: [limitation, stored-procedure, database]

- id: n39
  title: fetch 无 SQL_BREAK_FETCH 时全表扫；不用 LIST 变量只留最后一行
  type: warning
  source_pages: p391
  source_chapter: External Database lesson
  source_quote: |
    "Without the SQL_BREAK_FETCH BB, all the table records will be consulted • If you don't use a "LIST"
    variable, only the last record will be kept (because it will overwrite the previous one)"
  summary: |
    两条性能与正确性陷阱：结果集循环不带 SQL_BREAK_FETCH 会扫全表（大表即性能事故）；循环体内不
    用 LIST 变量收集时逐行覆写、只留最后一行——想取"第一条匹配"要配 BREAK+ROW_COUNT 判断。
  conditions: SELECT 脚本编写
  tags: [warning, fetch, sql]

- id: n40
  title: 外部库连接生命周期=脚本激活到去激活——排障先看脚本激活状态
  type: limitation
  source_pages: p378, p394
  source_chapter: External Database lesson
  source_quote: |
    "The connection to the database is carried out with the script activation and the disconnection is realized
    during the script de-activation" (p378)
    "option 60, when the ASM server is connected at least to 1 external database" (p394)
  summary: |
    数据库连接不是常驻的：脚本激活时连接、去激活时断开。客户报"查库失效"先确认脚本是否仍激活在
    Pilot 上、再用 adm_acd -salb 选项 60 看连接状态，别直接往数据库侧跑。
  conditions: 外部库排障
  tags: [limitation, connection, script]

- id: n41
  title: 教材存储过程不维护 Name/VIP 默认值（'noname'/'0'），需人工维护
  type: limitation
  source_pages: p434-435
  source_chapter: External Database How-To (MS SQL)
  source_quote: |
    "Note: the customer name is by default 'noname', & our stored procedure can't modify it. - You will be
    able to modify it manually if desired, using the SQL management studio tool." (p434)
    "Note: the customer VIP code is by default '0', & our stored procedure can't modify it." (p435)
  summary: |
    updateCalling 示例过程只写 Caller/Last_Agent 两列；Name（默认 'noname'）与 VIP（默认 0）原样留在
    默认值——示例脚本的"VIP+姓名"屏显依赖人工维护这些列。生产化要么扩展过程，要么另建数据维护
    通道，别指望开箱即得。
  conditions: 复用教材脚本时
  tags: [limitation, stored-procedure, data]

- id: n42
  title: DSN 名必须先有库——"先建库后建 DSN"顺序约束
  type: limitation
  source_pages: p380
  source_chapter: External Database lesson
  source_quote: |
    "Note: The database will be created before because you need to manage the name of this database for the
    name of the Data Source Name."
  summary: |
    ODBC DSN 指向真实数据库文件/实例，库名必须先存在。顺序颠倒会在 DSN 配置页找不到库。脚本里
    USE_DATABASE 的源名（DNS= 语法，原文即写作 DNS）必须与 DSN 名完全一致。
  conditions: ODBC 配置
  tags: [limitation, odbc, dsn]

- id: n43
  title: sa/Alcatel@1 与 Brest/alcatel 是实验口令——sa 密码是安装时自定义而非出厂值
  type: warning
  source_pages: p409, p418
  source_chapter: MS SQL How-Tos
  source_quote: |
    "Notes Password was defined during the MS SQL Server installation" (p409)
    "deactivate "Enforce password policy"" (p418)
  summary: |
    教材三处标注 sa 口令为"MS SQL Server 安装时定义"——Alcatel@1 是该实验环境的选择，照抄到生产既
    登不上也不安全。Brest/alcatel 弱口令 + 关闭密码策略同为实验口径。生产必须强口令、最小授权、保留
    密码策略。
  conditions: 生产环境安全基线
  tags: [warning, security, credentials, lab]

- id: n44
  title: SQL Server 2016 与 SSMS 安装后强制重启
  type: warning
  source_pages: p462, p465
  source_chapter: MS SQL Server 2016 Installation How-To
  source_quote: |
    "Click Close and REBOOT the Server … Notes A Reboot is mandatory !!!" (p462)
    "Notes Server Reboot is mandatory" (p465)
  summary: |
    数据库引擎装完与 SSMS 装完都要求重启服务器，教材两处以 mandatory 强调。跳过重启会在后续建库/
    ODBC 环节出现诡异失败。
  conditions: SQL 环境准备
  tags: [warning, installation, reboot]

- id: n45
  title: 未知 Call Tag 与库外主叫的脚本重试次数口径——20 次与 21 次两处不一致
  type: limitation
  source_pages: p50, p184
  source_chapter: Manage a script & Call Tag How-To
  source_quote: |
    "the alb process makes 20 requests (script is executed 20 times)" (p50)
    "This Customer Number is NOT known in the Internal Database, so the script will be executed 21 times." (p184)
  summary: |
    空列表/未命中场景的脚本重试次数，原书两处口径不同（p50 写 20 次，p184 实验截图注 21 次）。差异
    疑与计次边界有关，原书未解释（推断）。设计超时/重试相关 SLA 时不要引用单一数字，以现场实测为准。
  conditions: 重试行为依赖的重选配置
  tags: [limitation, reselection, discrepancy]

- id: n46
  title: Debugger 里观察 INTEGER 要用 + %0 显示技巧
  type: limitation
  source_pages: p262
  source_chapter: Miscellaneous lesson
  source_quote: |
    "To display an INTEGER Value in the Debugger use the following syntax: INTEGER[%1]= INTEGER[%1] + %0"
  summary: |
    调试器不会直接渲染整型值——要看值需在脚本里加 INTEGER[%x]=INTEGER[%x]+%0 的"自加零"技巧。
    排障脚本变量时不知道这一招会以为变量是空的。
  conditions: 脚本调试
  tags: [limitation, debugger, integer]

- id: n47
  title: 统计 Pilot 的呈现引导会抢 ACR Pilot 问候引导——要去掉
  type: warning
  source_pages: p226
  source_chapter: Multi-Language How-To step 4
  source_quote: |
    "Remove the Presentation Guide from all the Statistic Pilots. We only want to have a Greeting Guide on
    the ACR Pilot 31603"
  summary: |
    统计 Pilot 自带的 Presentation Guide 会先于 ACR Pilot 的（多语言）问候引导播出，导致语言判定失真。
    多语言场景必须清掉所有统计 Pilot 的呈现引导，只留 ACR Pilot 一处问候引导。
  conditions: 多语言引导部署
  tags: [warning, presentation-guide, multi-language]

- id: n48
  title: 教材笔误三处——"3X800"、"STRING_LENGHT"、"DNS=" 照录并提示
  type: limitation
  source_pages: p22, p192, p393
  source_chapter: 多章
  source_quote: |
    "3X500, 3X501 & 3X502 will be attached to the agent PG 3X800" (p22, 前文对象为 3X999800)
    "STRING_LENGHT" (p192, 应为 LENGTH 的拼写)
    "DB[%1]=USE_BATABSE="DNS=ACR"" (p393, USE_BATABSE/USE_DATABASE 混拼、DNS= 实为 DSN 语义)
  summary: |
    原书三处笔误照录：①p22 "agent PG 3X800" 与前文 3X999800 不一致（判为漏写 999）；②字符串函数名
    印作 STRING_LENGHT；③外部库连接串语法页印作 DNS=（DSN 语义）。照抄原文前先在工具里核对实际
    语法（推断以工具行为为准）。
  conditions: 照抄脚本/编号时
  tags: [limitation, typo, documentation]

- id: n49
  title: 容量与规模测算方法全书缺席——只有上限没有算法
  type: out-of-scope
  source_pages: p18
  source_chapter: ACR Introduction / ACR Limits
  source_quote: |
    "For more Information check the Feature List"
  summary: |
    p18 给了 12 项对象/名单容量上限，但"该建多少 Pilot/坐席组/呼叫档案"的测算方法（话务量、Erlang、
    坐席数规划）全书未涉及，最后一句把读者推向 Feature List。做规模方案需 OXE 侧配套文档与话务建模
    知识，教材只给边界。
  conditions: 售前/交付规划
  tags: [out-of-scope, capacity, dimensioning]

- id: n50
  title: 安全话题系统性缺席——口令印在教材、无传输加密与注入防护讨论
  type: out-of-scope
  source_pages: p409, p418, p430, p438
  source_chapter: MS SQL How-Tos 与脚本构件
  source_quote: |
    "Login: sa Password: Alcatel@1" (p409)
    "DB[%1] = USE_DATABASE "DNS=acr_sql; UID=brest; PWD=alcatel"" (p438)
  summary: |
    数据库口令明文印在教材与脚本连接串里；全书无 SQL 注入、传输加密、账号最小授权的讨论（唯 p418
    演示了关闭密码策略）。生产化必须叠加安全基线：强口令、专用低权账号、网络隔离、凭据不入明文脚本
    （推断的整改方向）。
  conditions: 生产部署
  tags: [out-of-scope, security]
```

## 收尾自检 — 对照 BOOK_OVERVIEW.md 17 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | 基础 CCD 矩阵搭建 | 有 → n01（ASM 组件）、n02（前缀前提）、n03（Station 不可改）、n04（混合链路约束）、n48（3X800 笔误） |
| task-02 | 脚本编写与调试工具链 | 有 → n05（LIT 不工作）、n06（重启 AFE）、n07（patchIdle 废弃）、n10（Debugger 不能加构件）、n45（20/21 次）、n46（INTEGER 显示） |
| task-03 | 授权/非授权名单规则 | 有 → n08（技能前提）、n09（大小写）、n25（APPLY 语义） |
| task-04 | 重定向/再分发规则 | 有 → n11（Blockage）、n22（房间/队列互斥） |
| task-05 | 直拨与 ACR 融合 | 有 → n12（ACR Pilot 行为差异）、n13（DICA 停用）、n14（无 ACR 溢出换人）、n15（单脚本/双来源） |
| task-06 | 内部数据库定制路由 | 有 → n16（4000 条）、n17（屏显参数） |
| task-07 | Call Tag 生成与传递 | 有 → n17（屏显参数）、n18（覆盖语义）、n19（IAA 外呼限制）、n20（改前停用）、n21（GetPilotInfo/16 位） |
| task-08 | 字符串处理 | 有 → n48（STRING_LENGHT 笔误） |
| task-09 | 多语言语音引导 | 有 → n47（呈现引导干扰） |
| task-10 | 综合脚本能力 | 有 → n22（方向互斥）、n23（IDLE 构件）、n24（IDLE/COM 互斥）、n25（APPLY 语义）、n26（ISM 成本插队）、n46（INTEGER） |
| task-11 | 过滤器与统计 | 有 → n27（不改分发）、n28（历史时效）、n29（AND/OR） |
| task-12 | 外部 ASM 割接 | 有 → n30（asm_on_dhs）、n31（内部未停）、n32（防火墙）、n33（localhost/服务模式）、n34（脚本迁移） |
| task-13 | 外部 ASM 双机 | 有 → n35（停服务/OmniPCX 名） |
| task-14 | 外部数据库机制 | 有 → n36（32 位）、n37（167 许可）、n38（过程支持）、n39（fetch 陷阱）、n40（连接生命周期）、n42（DSN 顺序） |
| task-15 | Access 外部库实验 | 有 → n36（64 位驱动）、n42（DSN） |
| task-16 | MS SQL 侧准备 | 有 → n43（口令口径）、n44（强制重启）、n48（DNS= 笔误） |
| task-17 | MS SQL 外部库脚本 | 有 → n41（过程不维护 Name/VIP）、n39（fetch）、n50（安全缺席） |

**17/17 全部有边界类条目覆盖，无空缺。**

### 扫描完整性说明（Note/Tips 标记框逐页核对）

- 全书正文无独立 "Warning" 关键字行（原书警告框多为截图元素，文本层未见）；边界语义经 Note/Tips 正文与 Inline Note 全量扫描（约 90 页 Notes/Tips + 6 处内联 Note）提取。
- 已入册的重复强调项（原书多处原文一字不差，判为刻意强调）：p49/p264/p345（重启 MAIN_AFE）、p80/p101（Debugger 不能加构件）、p399/p433（32 位 ODBC）、p462/p465（强制重启）。
- 复核后排除的纯操作提示框（非边界类，不构成候选）：p26/p27 Tips（CCS Apply 按钮与日历激活规则）、p28/p29 Tips（CCS 侧管优先级与方向）、p33/p36/p37/p45（CCSupervisor/mgr/OmniVista/Skill Matrix 等多入口提示，已并入 principle p45）、p44（保存传输激活，归流程）、p59（Debugger 界面页）、p87/p91（Redirection/Redistribution Debugger 界面页）、p95/p96/p100（地址形态/删连线，归 principle p13/p47）、p124（Notes 空白页）、p127 Tips（Debugger 可发起呼叫，已入 p12）、p131（4000 条，已入 p18/n16）、p148/p149（Callback Prefix 设置，已入 c06）、p158（直拨前提，已入 f14/p17）、p164（30 秒重选，已入 c06）、p168（统计 Pilot Call Tag 定义，归 glossary）、p175/p176（*88/*66 录音码，归 glossary/c07）、p182-185（实验过程注记，已入 c07）、p223/p224（录音激活，归 c09）、p227（Skill Matrix，归 p45）、p267/p275/p276/p280（实验过程注记，已入 c10）、p310（建 Filter 2/3 提示，归 c11）、p313（CTRL+左键/Filter，归 c11/f21）、p315/p316/p317（Update 刷新/模板选择，归 c11）、p351（MMC 启动，归 c12）、p354/p358（FTP 取脚本/实测，归 c12）、p366/p368/p370（重启 PC/配置收尾，归 c13）、p373（切换问答，归 c13）、p401（按版本选驱动，归 c14）、p407（CALLING 前缀核对，归 c14）、p415/p420/p426（表内容/重连验证/核验，归 c15/c16/c17）、p428（Brest 账号说明，归 c18）、p447/p449/p452（三呼证据链，已入 c18/p41）、p467（Profiler 登录，归 c20）、p469（实测步骤，归 c20）。
- 推断性结论已在对应条目 summary 内显式标注“（推断）”：n45（20/21 次差异成因）、n48（笔误的实际语法以工具为准）、n50（安全整改方向）。
- 版本号均按原文保留完整位数：l2.300.32.a（parameters.cfg 最低版本）、SQL Server 2016、Access 2016、SSMS 17、SQL Server Profiler 17、许可号 167。
