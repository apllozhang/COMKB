# 案例/实验/操作序列候选 — OmniTouch CC Standard · Advanced Call Routing (OTCCXTE150EN Issue 01)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（对象编号 3xXXX、账号口令、文件路径）标注"实验口径"。
> 条目说明: 全书 20 个 How-To 实验章 → 20 条（含 5 个 MS SQL 准备类 How-To 章；其中 c01 为后续全部实验的公共地基）。

```yaml
- id: c01
  title: 基础 CCD 矩阵创建（19 步：前缀→处理组→队列→双 Pilot→规则→坐席→混合链路→统计 Pilot→技能档案）
  type: lab
  source_pages: p19-41
  source_chapter: Basic CCD matrix creation (CCD09001CB01CGEN)
  source_quote: |
    "the ACD prefix is mandatory prior to create the CCD matrix objects" (p22)；
    "During the CCS installation don't forget to validate the ASM script component!!!" (p22)；
    "Weight Weight used by the Individual Skill Mapping (ISM) calculation algorithm to classify domains
    (1 for the least important to 20 for the most important)." (p37)
  steps: |
    1. 建 ACD 前缀：Translator/Prefix Plan 核查已有 ACD 前缀（前缀是建一切 CCD 对象的前提；前缀动作码
       +1 不可用/+2 Wrap up/+3 呼主管/+5 注销/+6 登录）。
    2. 建处理组：Applications/CCD/Processing group → create（实验口径：坐席处理组 3x999800）。
    3. 建等待队列：Applications/CCD/Queue → create，Distribution direction 0 填处理组 3x999800（队列
       3x999700）。
    4. 建两个 Pilot：Applications/CCD/Pilot → create——普通 Pilot 3x600 的 Routing direction 挂普通等待
       队列 3x999700；ACR Pilot 3x603 的 Routing direction 挂等待房间 3x999703。
    5. 建 Pilot 规则：Application/CCD/Pilot/Pilot Rule Guide → create（每 Pilot 最多 30 条规则，规则名显示
       在 CCS）；Application/CCD/Pilot/Pilot Rule Direction → Review/Modify——优先级 0-9（0 最高）、方向
       开/关；再在 Pilot Review/Modify 里设 Current Pilot Rule Number（0-29）。
    6. 建分发规则：Application/CCD/Distribution Rule → create（最多 10 条）→ Active Rule 激活第一条。
    7. 改资源选择配置：Application/CCD/Distribution Rule/Resource selection configuration → Review/Modify
       （优先级 0-9、队列→处理组方向开关）；等待房间同样处理。
    8. 改呼叫选择配置：Application/CCD/Distribution Rule/Call selection configuration → Review/Modify
       （优先级 0-9、方向开关）。
    9. 建 ACD 授权话机：Users → create——Set type 可选 8038/8068(s)/8078s/8082 Noe/8039（8068 软话机
       也可）；ACD station 选 ACD authorized phone set（实验口径：3x000、3x001、3x002）。
    10. 建坐席与主管：Users → create——坐席用 8068/8068s/8078s，ACD station=Agent；主管同法 ACD
        station=Supervisor（实验口径：Superuser 3x500、坐席话机 3x501/3x502）。注意：ACD Station 类型建
        户后不可改。
    11. 坐席操作规则：Applications/CCD/CCD Users/CCD Operations data management → create——勾选
        Self-assignable agent（可在任意处理组自助登录）、Secret code expected（登录注销需密码）。
    12. 建附件名单：同路径 /List of Attachments → create——Directory Number=坐席/主管号、Processing
        group Number=处理组号（也可经 CCSupervisor 建）。
    13. 建混合链路：Inter-Node Links/Logical Links (ABC-F) → create——Link Type=Hybrid、Adjacent Node=
        本地节点号、Adjacent Network=异于本地网络号（0-31）、Multi access hybrid link=YES；再建 Hybrid
        Link Access 的 access 1 与 access 2（至少成对）。
    14. 建统计 Pilot×2：Applications/CCD/Statistic Pilot → create——Pilot Stat. DN（3x650 车险、3x651 家险）、
        Directory Name（≤16 字符）、Routing Pilot=ACR Pilot 3x603。
    15. 建技能域：CCSupervisor/Configurations/Advanced Call Routing/Skill → Add——Name（1-16 字符）、ID
        （自动取 0-99 空闲）、Weight（1-20，ISM 域权重）。
    16. 建技能：同路径 → Create——Name（1-16 字符）、Abbrev（1-4 字符）、ID（0-99）；同法建另一技能。
    17. 建呼叫档案：CCSupervisor/Configurations/Advanced Call Routing/ACR Data → Add——Name、ID
        （0-999）、选技能、Level 1-9、Mandatory/Optional、Preference 1-7（仅语言）。同法建第 2 个档案
        （实验口径：档案 1=English+Car，档案 2=English+Home）。
    18. 档案指派到统计 Pilot：CCSupervisor/Configurations/Statistics Pilot → Modify → 选呼叫档案。
    19. 坐席配技能：CCSupervisor/Configurations/Agent → Add——坐席 31501 配 English 9 / Car 9，坐席
        31502 配 English 9 / Home 9（Level 1-9）。
  verification: |
    本章验证点：混合链路 telnet 执行 "hybvisu -f all"，两个 access 的 Main State 均须为 "up"（p35）。
    矩阵可用性由 c02 起的呼叫实验承接。
  conditions: CCS 安装时必须已勾选 ASM script 组件（p22 警告）；ACD 前缀先于一切 CCD 对象存在。
  tags: [lab, ccd-matrix, pilot, waiting-room, skill, domain, call-profile, hybrid-link]

- id: c02
  title: 首个 ACR 脚本：LCA+ISM 组合、ASM 内存检查、Debugger 验证、LIT 参数调校
  type: lab
  source_pages: p42-50
  source_chapter: Manage a script (CCD09001CB02CGEN)
  source_quote: |
    "For the 1st sequence, if an agent has already answered to the caller the same day the system gives a
    priority 2, & applies a reselection timeout of 10 sec + the last called agent rule. If no agent has
    answered or the elapsed time is greater than 1 day, the system applies the priority 8, the reselection
    timeout 20 sec and the ISM rule" (p43)；
    "Modify the parameter of the file parameters.cfg ­ asm_ag_free_duration … Restart MAIN_AFE dhs3_init
    -R MAIN_AFE" (p49)
  steps: |
    1. 编写脚本：CCSupervisor /Configurations/Advanced Call Routing/ASM Script Editor → Create——逻辑：
       SET PRIORITY=%2 + SET RESELECTION_TIMEOUT=%10 + RULE_LAST_CALLED_AGENT（条件
       LAST_CALLED_AGENT<>NULL 且 LAST_CALL_ELAPSED_TIME<1 DY）；IF SEQUENCE=%1 分支：当天有人接过
       → 优先级 2/超时 10 秒/LCA；否则 → 优先级 8/超时 20 秒/RULE_ISM CHARACTERISTICS_LIST；
       SEQUENCE>1 → 优先级 2 + ISM。保存并传输到 ASM，别忘了在 ACR Pilot 上激活。
    2. 查 ASM 内存：telnet OXE → 维护命令 adm_acd -salb → 选项 28；需要时重启 ASM 进程清内存
       （ps -edf | grep alb 找进程）。
    3. Debugger 验证：ASM Script Editor → ASM connection → 拨统计 Pilot 3x650——只应有 1 个坐席
       （31501，持 Car 技能）能接。
    4. 给坐席 3x502 追加 Car 技能：CCSupervisor /Configurations/Agent → Modify → 加 Car → 再呼车险
       Pilot，第 2 个坐席应能接。
    5. 验证 LIT 生效条件：脚本加 Rule "Idle Time"；more /usr3/afe/parameters.cfg——
       asm_ag_free_duration=0 时 LIT 不工作（实验观察：呼叫未按最长空闲路由）。
    6. 改参数启用 LIT：vi /usr3/afe/parameters.cfg 把 asm_ag_free_duration 0→1 → 重启 MAIN_AFE
       （dhs3_init -R MAIN_AFE）→ 复测：呼叫应路由给登录后空闲最久的坐席（0=PLTR 排序；1=旧
       patchIdle 行为；2=组网 LIT、空闲值每 3 秒上报）。
    7. 坐席自我停用技能：CCSupervisor /Configuration/Agent → Modify → 3x502 的 "Can set his skills"
       置 True → 坐席用话机停用技能后呼家险 Pilot 3x651，观察后果（列表空→脚本反复执行→走路由管理）。
  verification: |
    Debugger 轨迹符合 p43 行为描述；步骤 3 仅 1 坐席、步骤 4 两坐席可接；步骤 6 改参数后呼叫按 LIT
    路由；步骤 7 空列表时 alb 执行 20 次后转路由管理、最终 ACR Pilot 封锁（p50）。
  conditions: c01 矩阵已建；ASM script 组件已验证。
  tags: [lab, script, lca, ism, debugger, lit, parameters-cfg]

- id: c03
  title: 授权/非授权名单规则：建 List_1/Beginner 名单、写 Authoriz/Unauthor 脚本、Debugger 实时改条件
  type: lab
  source_pages: p62-81
  source_chapter: Authorized and Unauthorized Rule (CCD09002CB01CGEN)
  source_quote: |
    "If the skill "Home" has a level higher than 2, the ASM server applies the Authorized List 1 (Authorized
    List 1 contains the Agent 3x502) and if the skill level is lower than 2, the ASM applies the Authorized
    List containing the extension 3x501" (p62)；
    "The skill level for "Home" is set to level9, so the statement "IF (CHARACTERISTIS_LIST.SKILL["Home"].LEVEL>2)
    is TRUE and the "RULE_AUTHORIZED_LIST AUTHORIZED_LIST[%0] is applied. The content of the Authorized
    List 0 is the Agent 3x502" (p70)；
    "The String is case sensitive!" (p74)
  steps: |
    1. 建授权名单：CCSupervisor /Configurations/Advanced Call Routing /ACR Data → Add——ID 0-99、名单
       名 List_1（默认 WList_0），内容=坐席 3x502。
    2. 写脚本 Authoriz（≤8 字符，Graphic 模式）：插 Statement 构件定义条件（技能参数选 String to define、
       定级别 2）→ 加 RULE_AUTHORIZED_LIST 构件（参数 Authorized_List %index=0，或 Agents list 显式加
       3x501）→ 连线完成。
    3. 测 Authoriz：Debugger 挂 ACR Pilot 3x603——第 1 通呼家险 3x651（Home 级别 9>2）→ 名单 0 生效、
       3x502 接；第 2 通呼车险 3x650（档案无 Home 技能，条件 FALSE）→ 脚本内显式名单生效、3x501 振铃。
    4. 建非授权名单：ACR Data → Add——名 Beginner（默认 BList_1），内容=坐席 3x501；场景：10 点前
       排除 Beginner（3x501），10 点后排除主管 3x500。
    5. 写脚本 Unauthor（Graphic 模式）：Statement 条件（时间比较）→ RULE_UNAUTHORIZED 构件（String
       to define，注意大小写敏感；可用 UNAUTHORISED_LIST->%整数=名单 ID）→ 加第二构件（名单含主管
       3x500）→ 连线。
    6. 测 Unauthor：呼 3x651——Debugger 时间 12:45:12 > 10:0:0，IF TIME<10:0:0 为 FALSE →
       Rule_Unauthorized_List 生效、名单内坐席不可接。
    7. Debugger 实时改条件：选中 IF 条件 → Statement 属性打开 → 把 IF (TIME < 10:0:0) 改为
       IF (Time > 10:0:0) → 保存 → 再呼：31501 不可接、其余有 ≥1 活动技能的坐席均可接。
  verification: |
    p70/p78/p81 Debugger 轨迹：Home 级别 9 → 名单 0（3x502）生效；12:45:12 条件不匹配 → 非授权名单
    生效；改条件后 31501 被排除、其他坐席可用。
  conditions: c01/c02 已完成；名单内坐席须有至少 1 个活动技能。
  tags: [lab, authorized-list, unauthorized-list, debugger, live-edit]

- id: c04
  title: 重定向/再分发规则：Redirect 脚本（10 秒后转 3x010）与 Redistri 脚本（周日转 Voice Guide 队列）
  type: lab
  source_pages: p92-102
  source_chapter: Redirection Rule and Redistribution Rule (CCD09003CB01CGEN)
  source_quote: |
    "If the language of the caller is not English, the system applies the Authorized_List1, otherwise the ISM
    Rule is applied. In this case, after waiting for 10 seconds (Agents are busy) the call is redirected to the
    extension 3x010." (p93)；
    "create a Redirection Queue 31999702 which is connected to a Processing Group Type "Voice Guide"
    31999802 with the Voice Guide 710. The Voice Guide 710 play the following message: "All agents are busy,
    please call back later"." (p99)
  steps: |
    1. 写脚本 Redirect：CCSupervisor /Configurations/Advanced Call Routing /ACR Script Editor → New
       （名 ≤8 字符）——Statement（语言条件）→ RULE_AUTHORIZED 构件 → RULE_ISM 构件 → Set call
       context variable（Reselection Timeout=10 秒）→ Statement → RULE_REDIRECTION 构件（地址
       3x010，可内部/外部/字符串变量）→ 连线（删连线=选红方块右键）。
    2. 测 Redirect：呼统计 Pilot 3x650（English+Car）——Debugger 显示"English 被请求→IF 为 FALSE→ISM
       生效"；坐席全忙时呼叫在等待房间停 10 秒后脚本重执行；SEQUENCE>1 → Rule Redirection 生效、呼叫
       转 3x010。
    3. 矩阵扩展（为 Redistri 做准备）：建重定向队列 31999702 → 接处理组类型 Voice Guide 31999802 →
       语音引导 710（"All agents are busy, please call back later"）；ACR Pilot 以第二优先级接该重定向队列。
    4. 写脚本 Redistri：构件 Redistribution——周日（calling day=Sunday）时呼叫再分发到重定向队列，否则
       沿用前一脚本逻辑 → 连线。
    5. 测 Redistri：Debugger 选中 IF 条件 → 把 Statement 改为 IF (Day = "actuell Day")（原文如此）实时
       验证再分发路径（调试器只能改既有构件，不能加新构件）。
  verification: |
    p97-98：坐席忙 10 秒后转 3x010（Redirection）；p101：改 Day 条件后再分发路径生效。Voice Guide 队列
    播 710 引导。
  conditions: c01 矩阵已建；语音引导 710 已录制并激活（System/Voice Guides）。
  tags: [lab, redirection, redistribution, voice-guide, debugger]

- id: c05
  title: 坐席直拨与 ACR：建直拨 Pilot 31604、配私有号、停 DICA 实测、写 DICA 脚本验证等待-转接
  type: lab
  source_pages: p118-127
  source_chapter: Direct Call and ACR Pilot (CCD09004CB01CGEN)
  source_quote: |
    "Create a new Pilot 31604 and connect this Pilot to the Waiting Room 31999703. The Pilot will be used for
    "CCD Direct Call" Feature on the Processing Group 31999800. Assign the "ACD authorized phone set"
    number 31001 as Private Agent number." (p119)；
    "IF the CALL_TYPE=DIRECT_CALL: For the 1st sequence, wait for 30 seconds in the waiting room (if the
    Agent is busy) For the 2nd sequence, route the call to the Extension 31010" (p121)
  steps: |
    1. 矩阵扩展：建新 Pilot 31604 → 接等待房间 31999703；Applications/CCD/Processing Group → 该坐席
       处理组 31999800 的 Pilot Direct Call 参数填 31604；CCD Operations Data management → 坐席 31501
       （Directory Number 31500）配 Private Agent No.=31001；初始不给 31604 挂脚本。
    2. 验证直拨特性：坐席空闲时直拨其 DN 应正常；坐席忙时观察行为（无脚本时：溢出到直拨 Pilot=ACR
       Pilot → 呼叫在等待房间等到原坐席空闲；教材留白提问：停多久？答案取决于重选配置——直拨打到
       ACR Pilot 的行为与普通 Pilot 不同）。
    3. 停 DICA 实测：CCSupervisor /Configuration/Agent → 选 31501 → 停用自动生成的 DICA 技能（Domain
       Media/Skill DirectCall）→ 坐席空闲/可用/忙各种状态下直拨 DN——应全部立即转 pilot direct call
       （完全无法直拨）。
    4. 写脚本 DICA：Script Editor → New——逻辑 IF CALL_TYPE=DIRECT_CALL：第 1 次执行（SEQUENCE=%1）
       呼叫在等待房间等 30 秒；第 2 次执行转分机 31010；非直拨 → RULE_ISM（Call-Profile ID1）。构件：
       Statement(SEQUENCE=%1)→RULE_REDIRECTION 31010→SET RESELECTION_TIMEOUT=%30→
       IF(CALL_TYPE=DIRECT_CALL)→RULE_ISM Call_Profile=%1 → 连线。
    5. 激活与验证：脚本 DICA 挂 ACR Pilot 31604 → Debugger 观察坐席忙时首呼等 30 秒、重选后转 31010；
       非直拨呼叫走 ISM。可从 Debugger 直接发起呼叫。
  verification: |
    p125-127 Debugger：首呼坐席忙 → 等待房间 30 秒；坐席仍忙 → 重选后转 31010；非 Direct_Call 呼叫 →
    ISM 路径。
  conditions: c01 矩阵已建；ACD 授权话机 31001 可用（实验口径私有号）。
  tags: [lab, direct-call, dica, call-type, pilot-direct-call]

- id: c06
  title: 内部数据库：三键（Calling/Call_Tag/Agent501）建库条目 + 三个脚本 + 正反用例测试
  type: lab
  source_pages: p142-164
  source_chapter: Internal Database with Calling, Call Tag and Agent Number (CCD09005CB01CGEN)
  source_quote: |
    "For the Calling Number "02312122003" Call Profile: 0 Authorized List: 0 Unauthorized List: - Priority: 0" (p144)；
    "RULE_ISM CALL_PROFILE [CALLING] SET PRIORITY = CALL_PRIORITY [CALLING]" (p147)；
    "The Account "Brest" was created before." ——（此句属 SQL 章；本章 Notes 为 "If the Agents are still busy,
    the System applies the RULE_AUTHORIZED_LIST after the reselection of 30 seconds"）(p164)
  steps: |
    [Calling 键]
    1. 建库条目：CCSupervisor /Configurations /Advanced Call Routing /ACR Data → Open → Add——主叫号
       02312122003（实验口径）：Call Profile 0、Authorized List 0、Priority 0。
    2. 写脚本 Calling：RULE_ISM CALL_PROFILE[CALLING] → SET PRIORITY=CALL_PRIORITY[CALLING] →
       IF (AGENTS_LIST=NULL) → APPLY RULE_AUTHORIZED_LIST AUTHORIZED_LIST[%0]。
    3. 测试：脚本挂 ACR Pilot 31603，从分机 31003 呼入——Debugger 里 Callback Prefix In ASM Debugger=
       FALSE 时主叫号未经外部回拨翻译器翻译；mgr /Applications/CCD/CCD/RSI system parameters（或
       telnet）把该参数置 TRUE 后主叫号带翻译前缀，应与库内容一致；再以库外号码呼入验证落空路径。
    [Call_Tag 键]
    4. 建库条目：Call Tag 区段 1000-1999 → Call Profile None、Authorized List 0、Priority 0。
    5. 统计 Pilot 配 Call Tag：CCSupervisor /Configurations /Statistic Pilot → 31650 → Call Tag 填 1500
       （0-32 字符）。
    6. 写脚本 Call_Tag：IF CALLTAG<>NULL → PRIORITY=CALL_PRIORITY[CALLTAG] → APPLY
       RULE_AUTHORIZED_LIST AUTHORIZED_LIST[CALLTAG] → 否则 APPLY RULE_REDIRECTION（转 31010）。
    7. 测试：脚本挂 31603，呼 31650（带标签 1500）→ 名单路径；呼 31651（无标签）→ Redirection 路径。
       Notes：要在坐席屏显示 CALLTAG，需把处理组 "Display on agent screen" 设为 Call tag 或 caller and
       pilot char.；可配 Call Tag Display Timer（0 或 10-32767）。
    [坐席号键（仅直拨）]
    8. 建库条目：坐席号 31501 → Call Profile 1、Priority 0（前提：31501 已配直拨特性——处理组 Pilot
       Direct Call + 私有号）。
    9. 写脚本 Agent_Nb：IF (CALL_TYPE=DIRECT CALL) → IF (SEQUENCE=%1) → APPLY RULE_ISM
       CALL_PROFILE=[AGENT_NUMBER] + PRIORITY=CALL_PRIORITY[AGENT_NUMBER] →
       RESELECTION_TIMEOUT=%30 → APPLY RULE_AUTHORIZED_LIST AUTHORIZED_LIST[%0]。
    10. 测试：脚本挂 31604（直拨 Pilot），坐席忙时直拨 31501——Debugger 显示 ISM(0)、Call_Profile 0 取自
        内部库；30 秒重选后仍忙 → Authorized_List 0 生效。
  verification: |
    p148-151（Callback Prefix 前后对照）、p157（未知 Call Tag → Redirection）、p163-164（坐席号键 →
    ISM(0) + 30 秒后名单兜底）三组 Debugger 轨迹。
  conditions: c01/c05 已完成（矩阵与直拨特性就绪）。
  tags: [lab, internal-database, calling, calltag, agent-number]

- id: c07
  title: Call Tag 生成与传递：IAA 编码叶 + 统计 Pilot 标签 + GFW 转发覆盖验证
  type: lab
  source_pages: p174-189
  source_chapter: Call Profile or Call Tag / Transfer (CCD09006CB01CGEN)
  source_quote: |
    "Leaf Name Call Tag • Leaf Type Code Entry Guide … DTMF Digit: 4 (1-16) • Action Type + Code Entry •
    Directory No. : 31603" (p177)；
    "The first CALLTAG "2500" will be overwritten be the CALLTAG of the Statistic Pilot 31650 (CALLTAG
    1500)." (p189)
  steps: |
    1. 建可录语音引导：System / Dynamic Voice Guides /Assignment → Create——引导号 710-719（同法 711-719；
       Notes：可录引导 *88、音调测试 *66、引导指派 GD (2-0)）。
    2. 建语音引导：System /Voice Guides → Create（710-719）→ 录音并激活。
    3. 建 IAA：Applications/Automated Attendant/Automated Attendant Leaves → Create——叶 2 "Call Tag"
       （类型 Code Entry Guide，提示音 712、监听 10 秒、DTMF 位数 4（1-16）、Action Type +Code Entry →
       31603）；叶 1 "Intro Menu"（菜单叶，音 711，DTMF 1→路由预配号 31650、DTMF 2→叶 2）；树 "For
       CallTag"（首叶 1）；接入（号 31900、Access ID 1、昼/夜 Caller Rights COS 0 1）；Automated Attendant
       Review/Modify 置 Valid=TRUE；Trunk Group 的 Automated Attendant 属性置 YES。
    4. 改脚本 Call_Tag 验证 IAA：修改 IF 条件（纳入 (CALLTAG>=1000) AND (CALLTAG<=3000)）→ 挂
       ACR Pilot 31603 → 四通外呼测试：①选 1（统计 Pilot 31650 给标签 1500）→ 名单路径；②选 2 拨
       1427（库内有）→ 标签 1427 命中名单；③选 2 拨 2545（区间内但库外）→ 脚本执行 21 次后转路由管理；
       ④选 2 拨 7514（区间外）→ 不匹配条件 → Rule_Redirection。
    5. 建统计 Pilot 31652：Applications / CCD/ Statistic Pilot → Create——31652、Routing Pilot=31604、
       Call Tag 2500。
    6. 建库条目 Call_Tag2：ACR Data → Create——From 2000 To 2999、档案 <NONE>、授权名单 <NONE>、
       非授权名单 Beginner、Priority -。
    7. 配 GFW 转发：CCsupervisor / Configurations/ Pilot → 31604 → Standard General Forwarding=31650 →
       激活 General Forwarding。
    8. 验证标签覆盖：呼 31652（标签 2500）→ 到 ACR Pilot 31604 → 处于 GFW 模式转发到 31650（标签
       1500）→ 31650 的 Routing Pilot 是 31603（脚本 CALL_TAG）→ Debugger 显示生效标签为 1500（2500 被
       覆盖）。
  verification: |
    p182-185 四组 Debugger 轨迹（标签 1500/1427/2545/7514 四条路径）；p189 覆盖验证：GFW 后生效标签
    1500。
  conditions: c06 的 Call_Tag 脚本已存在；IAA 只能外部呼入（测试呼叫必须走外线）。
  tags: [lab, iaa, call-tag, gfw, overwrite]

- id: c08
  title: 字符串处理：单叶 IAA 采集客户号 + String 脚本（长度/查找/提取/屏显）
  type: lab
  source_pages: p197-211
  source_chapter: String handling (CCD09007CB01CGEN)
  source_quote: |
    "A STRING[%1] variable will be used to retrieve the entered Customer Number. An INTEGER[%1] will contain
    the length of the Customer Number. A test will check the entered code length. If the code is lower than or
    equal to 4, that will be an English Customer otherwise that will be an International Customer." (p200)；
    "Notes IAA can only be called from external" (p211)
  steps: |
    1. 建 IAA：Applications /Automated Attendant → 建叶 3 "Customer Code"（Code Entry Guide，提示音
       713、DTMF #=结束编码输入 → 31603）；建树 2 "Code"（首叶 3）；建接入 Access ID 2（COS 0 2）；
       先把 Automated Attendant Valid 置 FALSE 再改，改完置 TRUE。
    2. 写脚本 String（逻辑）：STRING[%1]=CALLTAG（取客户号）→ INTEGER[%1]=STRING_LENGTH STRING[%1] →
       IF (INTEGER[%1] <= %4)（≤4 位=英语客户）→ INTEGER[%2]=SEARCH_STRING "11" STRING[%1] →
       IF (INTEGER[%2] = %1)（以 11 开头）→ STRING[%2]=EXTRACT_STRING "11" STRING[%1] →
       DISPLAY_AGENT=STRING[%2]；否则 DISPLAY_AGENT="New Customer" → APPLY RULE_ISM
       CALL_PROFILE[%0]。国际分支：INTEGER[%3]=SEARCH_STRING "99" STRING[%1] → IF(=%1) →
       INTEGER[%4]=%2 → STRING[%3]=EXTRACT_STRING INTEGER[%3] INTEGER[%4] STRING[%1]（按位截取）→
       DISPLAY_AGENT=STRING[%3]；否则 "New Int. Customer"。
    3. 测试：脚本挂 31603，从外部呼 IAA 31888（实验口径）输入不同客户号，Debugger 逐一核对四类用例：
       11 开头 4 位 / 99 开头 >4 位 / 非 11 开头 4 位 / 11 开头但 >4 位。
  verification: |
    p208-211 四组 Debugger 截图对应四类用例的屏显结果（提取串/"New Customer"/"New Int. Customer"）。
  conditions: c06 脚本环境可复用；测试呼叫必须来自外部（IAA 约束）。
  tags: [lab, string, iaa, display-agent]

- id: c09
  title: 多语言语音引导：740 多语言引导（法语 1000/英语 1001）+ 档案 3 + 语言偏好分发验证
  type: lab
  source_pages: p222-229
  source_chapter: Multi-Language Voice Guides (CCD09008CB01CGEN)
  source_quote: |
    "Voice Guide No. 740 • Function Multi-language message • Voice Guide Start YES • Backup Tone 56 • Add 2x
    Language Number French Message Number 1000 / English 1001" (p224)；
    "The value of the preference associated to each language will determine which language will be above the
    other when broadcasting guides or when choosing the agent who will handle the call (value included
    between 1 and 7, 1 for the highest priority language)" (p229)
  steps: |
    1. 建可录引导：System / Dynamic Voice Guides /Assignment → Create——消息 1000（法语欢迎）、1001
       （英语欢迎）；录音（*88）并激活。
    2. 建多语言引导：System /Voice Guides → Create——号 740、Function=Multi-language message、Start=YES、
       Backup Tone 56、Add 2 次：French→1000、English→1001。
    3. 建呼叫档案 Call_Profile_3：CCsupervisor /Configurations /Advanced Call Routing / ACR Data——
       Domain Language/Skill French/Level 5 + Domain Insurance/Skill Car/Level 9。
    4. 建统计 Pilot 31653：Applications / CCD/ Statistic Pilot → Create——31653、名 French_Car、Greeting
       Guide No (normal)=0、Routing Pilot=31603、Call Profile 3；CCsupervisor → Statistic Pilot → 修
       Presentation Guides 为 Normal。Notes：把所有统计 Pilot 的呈现引导去掉——问候引导只留在 ACR Pilot
       31603 上。
    5. 配技能与脚本：坐席 31501 加技能 French Level 9（也可用 Skill Matrix）；新写简单脚本：APPLY
       RULE_ISM CHARACTERISTICS_LIST → 挂 31603。
    6. 测试：分别呼各统计 Pilot，核对播报语言与选中坐席——呼 31650（English;Car）→ 英语引导；呼
       31653（French;Car）→ 法语引导；对照档案内语言偏好（法语 2/英语 1 时播英语）。
  verification: |
    p228-229 Debugger：两个统计 Pilot 各自播对应语言引导；偏好值决定语言优先与坐席选择。
  conditions: c01 矩阵已建；消息 1000/1001 已录制。
  tags: [lab, multi-language, voice-guide, call-profile, preference]

- id: c10
  title: 综合特性：ISM_IDLE/ISM_COM/1Apply/2Apply/Addition/List_Var 六脚本与 CCD/ACR 混合选呼
  type: lab
  source_pages: p263-282
  source_chapter: Miscellaneous Feature (CCD09009CB01CGEN)
  source_quote: |
    "Only 31501 is rung, because he has the right skills 31500 has also the right skills, but is not rung,
    because he is not part of the agent list, provided by the previous RULE_AUTHORIZED_LIST" (p267)；
    "The Agent list of "RULE_AUTHORIZED_LIST" is not considered as the input of the RULE_ISM." (p270)；
    "At equal Priorities & ACR Actual Waiting set to FALSE (Default value), the lowest ISM cost is used." (p282)
  steps: |
    1. 脚本 ISM_IDLE：APPLY RULE_ISM CHARACTERISTICS_LIST, RULE_IDLE_TIME——默认
       asm_ag_free_duration=0 下 RULE_IDLE 走 PLTR；telnet vi /usr3/afe/parameters.cfg 改
       asm_ag_free_duration=1 → dhs3_init -R MAIN_AFE 重启 → 复测 LIT 模式。
    2. 脚本 ISM_COM：APPLY RULE_ISM CHARACTERISTICS_LIST, RULE_COM——参数对该规则无影响，坐席按
       登录后服务呼叫数比率排序。
    3. 脚本 1Apply（单 APPLY 链式）：APPLY RULE_AUTHORIZED_LIST 31501 31502, RULE_ISM
       CHARACTERISTICS_LIST。坐席技能配置：31501=Car 9/English 9/DICA、31502=Home 9/English 9、
       31500=Car 9/English 9。挂 31603 测试：仅 31501 振铃（31500 技能匹配但不在前列表输出中）。
    4. 脚本 2Apply（双 APPLY 独立）：IF (SEQUENCE=%1) APPLY RULE_AUTHORIZED_LIST 31501 31502 /
       IF (CALLING BEGIN_WITH XXX) RESELECTION_TIMEOUT=%10 ELSE APPLY RULE_ISM … ENDIF ELSE
       APPLY RULE_ISM … ENDIF。测试对照：Calling 前缀命中 → 授权名单路径；未命中 → ISM 路径且名单
       内容不作为 ISM 输入（全量坐席参与）。
    5. 脚本 Addition（IQUEUE + CLEAR）：录常规停放引导 701-706 与 IQUEUE 引导 751-756、NEXT=757。
       逻辑：档案含 Home → ISM + IQUEUE（各级专属引导，坐席全忙时客户在等待房间听专属引导直到有坐
       席）；无 Home → 第 1 序列转坐席 31500 并屏显 "NO HOME"、不可达则停 12 秒；第 2 序列
       CLEAR_PREVIOUS_LIST 后走 RULE_LAST_CALLED_AGENT。分别呼 31651（Home）与 31650（Car）用
       Debugger 验证三条路径。
    6. 脚本 List_Var：建授权名单 2（WList_2，含 31501）；确认本机主叫号已配授权名单条目；脚本=VARIABLE
       LIST[%1]=LAST_CALLED_AGENT + AUTHORIZED_LIST[%2] + AUTHORIZED_LIST CALLING − 显式坐席
       31500 → RULE_AUTHORIZED_LIST LIST[%1]。Debugger 查看 LIST[%1] 内容；LAST_CALLED_AGENT 可用
       adm_acd ASM IP# -salb → 28 * 核对。
    7. CCD/ACR 混合选呼（一）：CCSupervisor /Configurations/ Call Flow mgt/ Call Distribution——队列
       31999700 优先级 9、房间 31999703 优先级 8；两侧各停若干呼叫 → 坐席空闲时房间呼叫先被处理
       （优先级不同）。
    8. CCD/ACR 混合选呼（二）：两处优先级均改 9 → 等优先级下按 ACR Actual Waiting 分派（mgr
       Applications/CCD/CCD/RSI → FALSE=最低 ISM 成本先；TRUE=最长实际等待先）。
  verification: |
    p267/269-270（1Apply vs 2Apply 对照）、p273-275（Addition 三路径）、p280（List_Var 内容）、p281-282
    （选呼两场景） Debugger 轨迹与行为结论。
  conditions: c01/c02 已建；语音引导 701-706/751-757 已录制；asm_ag_free_duration 修改需重启 MAIN_AFE。
  tags: [lab, idle, com, apply, iqueue, list-var, call-selection]

- id: c11
  title: 过滤器与统计：Filter 1/2/3 + Super-Filter + 实时窗口 + Excel 明细/汇总
  type: lab
  source_pages: p308-317
  source_chapter: Filter & Statistic (CCD09010CB01CGEN)
  source_quote: |
    "Filter 1: Car Insurance / level 4 to 9 / mandatory English Language / level 4 to 9 / mandatory …
    Service Level 75% within 15sec, Efficiency 85% for all Filter" (p309)；
    "Filter 3 will not have any Data: We do not have a Call_Profile with English, Car AND Home" (p312)；
    "Filter use the Function "AND", a Super-Filer / Hyper-Filer use the Function "OR"" (p314)
  steps: |
    1. 建 Filter 1：CCSupervisor /Configurations/Advanced Call Routing /Filter → Add——名 Filter 1 →
       Modify 加技能：Car Insurance 4-9 强制 + English 4-9 强制。同法建 Filter 2（Home 4-9 强制 +
       English 4-9 强制）、Filter 3（Car 5-9 any + Home 5-9 any + English 5-9 any）。全部配 Service Level
       75%/15 秒、Efficiency 85%。
    2. 建 Super-Filter：CCSupervisor /Configurations/Super Objects → Create——名 + 选入 Filter 1 与
       Filter 2。
    3. 实时观测：CCSupervisor /Real time/Filter 依次选 Filter 1/2/3——Filter 3 无数据（没有同时带三种
       技能的呼叫档案）。
    4. 等待房间观测：坐席全忙时往各统计 Pilot 打电话 → Real time / Calls in Waiting Room → Open
       （也可 CTRL+左键开 Waiting Room 实时窗口；呼叫多时用 Filter 过滤）。
    5. 概念辨析：Filter 3（AND 全技能）与 Super-Filter（Filter 1 OR Filter 2）的差异——前者只统计同时
       需要三种技能的呼叫，后者统计两类档案的并集。
    6. 近一小时话务：Statistics / Last received Calls → Open（Update 刷新）。
    7. Excel 明细：Statistics / Excel/ Filter → 选 Filter 1/2/3 → Excel Display 模板 "General"。
    8. Excel 汇总：Statistics / Excel/ Filters Summary → 同上模板。
  verification: |
    Filter 3 实时无数据（p312）；Super-Filter 有数据（Filter 1∪Filter 2）；Excel 明细带时间片粒度、汇总
    每过滤器一行。
  conditions: c01 矩阵已建；过滤器统计只对创建之后的呼叫有效（预置 20 个过滤器有历史）。
  tags: [lab, filter, super-filter, statistics, excel]

- id: c12
  title: 外部 ASM 安装割接：asm_on_dhs=0 → 装服务 → 建 Site_1 链路 → 迁移激活脚本 → 防火墙与维护
  type: lab
  source_pages: p344-360
  source_chapter: External Agent Selection Module (ASM) (CCD09011CB01CGEN)
  source_quote: |
    "vi /usr3/afe/parameters.cfg … asm_on_dhs=0 … Restart the MAIN_AFE dhs3_init -R MAIN_AFE" (p345)；
    "Site Name: Site_1 • Main CPU: csm or Ip address • Stand-by CPU: ------- • Connection role: ROUTER" (p352)；
    "If the Internal ASM server is not Stopped, you will not be able to make the connection from the External
    ASM Server to the AFE!" (p353)
  steps: |
    1. 停内部 ASM：telnet OXE → vi /usr3/afe/parameters.cfg 把 asm_on_dhs=1 改 0（光标移到 1 → r → 0 →
       ESC :wq）→ dhs3_init -R MAIN_AFE 重启 AFE；必要时 kill alb（ps -edf | grep alb 核查）。
    2. 装外部 ASM：setup.exe → Next → 接受许可 → Yes → 目录（默认）→ 组件（默认）→ 复制 → Standalone
       system → 重启电脑 → Finish。
    3. 装 ASM 服务：Start /All Programs/ Alcatel-Lucent/ Agent Selector Module/ASM Manager → Install →
       启动服务；MMC 里核服务启动模式（应 Automatic）。
    4. 建 OXE 链路：ASMServer Tool → 填 ASM 服务器 IP → Connection → New Site——Site Name=Site_1、
       Main CPU=csm 或 IP、Stand-by CPU 空、Connection role=ROUTER → OK；连接成功出现链路图
       （内部 ASM 未停则连不上 AFE）。
    5. 迁移并激活脚本：CCSupervisor /Configurations/ Advanced Call Routing/ ASM Script Editor → Open →
       选 ASM 连外部 ASM（填 remote ASM 名或 IP；脚本不在本机可 FTP 从 OXE /usr3/afe 取）→ Import /
       From File System 选 ISM_IDLE.scr → Add → 选脚本 → 为 ACR Pilot 31603 激活 → Debugger 验证 →
       往统计 Pilot 打电话实测。
    6. 维护：telnet OXE → adm_acd ASMServer IP@ -salb 看 OXE↔外部 ASM 链路；选项 11（Agent List
       Builder 显示 Windows PC IP）；选项 14（连接类型）。连不通先查 Windows 防火墙：放行入站 ASM 与
       ASMMgr 的 UDP+TCP（Private）。
  verification: |
    Site 链路建立（p352-353）；ISM_IDLE 在外部 ASM 上对 31603 生效、Debugger 与实际呼叫正常（p357-358）；
    adm_acd 选项 11/14 显示外部链路（p359-360）。
  conditions: c02 的 ISM_IDLE 脚本已存在；外部 ASM 连接免许可（连外部 DB 才需 167 号许可）。
  tags: [lab, external-asm, asm-on-dhs, site, firewall]

- id: c13
  title: 外部 ASM 双机热备：备机 Duplicate system 安装、主机改 Duplicated/Main、脚本同步与切换实测
  type: lab
  source_pages: p361-373
  source_chapter: Duplicated External Agent Selection Module (ASM) (CCD09011CB02CGEN)
  source_quote: |
    "Select "Duplicate system" … Select "Stand-by ASM" Dual ASM: Name of the "Main ASM Server": SoftPanel" (p365)；
    "Activate "Duplicated ASM" … Dual ASM: SoftPanel2 ASM Mode: Main" (p367-368)；
    "Verify that all scripts already created on the Main ASM Server are automatically copied to the Stand-By
    ASM Server." (p373)
  steps: |
    1. 备机安装（实验口径：主 10.2.T.20/SoftPanel=Main，备 10.2.T.21/SoftPanel2=Stand-By）：setup.exe →
       许可 → 目录 → 组件 → 复制 → Duplicate system → Stand-by ASM → Dual ASM 填主机名 SoftPanel →
       重启电脑 → Finish。
    2. 主机改造：ASMServerTool.exe → 停 ASMServer 服务 → Next → ASMServer Configuration → 激活
       "Duplicated ASM" → Configure → Dual ASM=SoftPanel2、ASM Mode=Main → OK → 改配置 → Exit →
       重启电脑。
    3. 备机装服务：ASM Server Tool → Install → 启动服务 → MMC 核启动模式。
    4. 备机维护核查：ASMServer Manager → 填主 ASM IP → Connection 看 Site Connection（主 ASM 与 AFE
       连接建立后备机连接自动复制；OmniPCX 名必须被备机知晓）；再连备机 IP 验证其自身不能直连 AFE。
    5. 切换实测：核备份目录 C:\Program Files (x86)\Alcatel\Agent Selector Module\Script 已自动同步脚本
       → 往统计 Pilot 打电话并接听 → 停主 ASM 服务 → 再打电话：脚本改在备机执行 → 恢复主 ASM 服务。
  verification: |
    备机可见主机的 Site Connection（p371）；主服务停止后备机接管脚本执行（p373 问答式验证）；脚本目录
    两机一致。
  conditions: c12 单机外部 ASM 已运行；两机服务配置变更前必须停服务。
  tags: [lab, duplicated-asm, standby, failover]

- id: c14
  title: Access 外部库：建 acr.accdb/Records 表 → 32 位 ODBC DSN "ACR" → Access 脚本（SELECT+屏显）
  type: lab
  source_pages: p395-407
  source_chapter: External Database (CCD09012CB01CGEN)
  source_quote: |
    "1 Smith James 002312121003 31501 1 … VIP: calling inspection or not (1 or 0)" (p396)；
    "The ASM Server is not able to make a connecting using a 64-Bit ODBC Driver" (p399)；
    "USE_DATABASE DB[%1]=USE_DATABASE="DNS=acr" … SQL_REQUEST DB[%1] SELECT "VIP, NAME,FIRST_NAME"
    FROM "records" WHERE "CALLING={STRING[%1]}"" (p402)
  steps: |
    1. 建 Access 库：Access 2016 → Blank desktop database → 文件名 acr.accdb → Design View 建表
       Records：ID (AutoNumber 主键)/Name/First_Name/Calling/Agent（短文本）、VIP (Number) → 数据表视图
       录 3 行样例（Smith/Fox/Wayne）→ 保存为 acr.mdb（Notes：ASM 服务器不能用 64 位 ODBC 驱动连接）。
    2. 建 ODBC：Start /Control Panel/Administrative Tools/ODBC Data Source (32-bit) → System DSN →
       Add → "Driver do Microsoft Access (*.mdb)" → Data Source Name=ACR → Select 浏览选库 → OK
       （Notes：按 Access 版本选对驱动）。
    3. 写脚本 Access：USE_DATABASE DB[%1]="DNS=acr" → START → IF DB[%1]<>NULL →
       STRING[%1]=CALLING（主叫号前置 0 与否取决于 RSI 参数 Callback Prefix In ASM Debugger）→
       INTEGER[%1]=%0 → SQL_REQUEST SELECT "VIP, NAME,FIRST_NAME" FROM "records" WHERE
       "CALLING={STRING[%1]}" → IF SQL_RESULT=SQL_SUCCESS → SQL_START_FETCH DB[%1] → SQL_DATA
       INTEGER[%1]="VIP"/STRING[%2]="NAME"/STRING[%3]="FIRST_NAME" → SQL_END_FETCH →
       IF INTEGER[%1]=%1 → STRING[%4]=STRING[%3]+" "+STRING[%2] → DISPLAY_AGENT STRING[%4] →
       RULE_ISM CHARACTERISTICS_LIST。
    4. 激活测试：脚本挂 31603 → Debugger 核 CALLING（应以 0 开头且与库内容一致）→ VIP 客户屏显
       "姓名"。
  verification: |
    p406-407 Debugger：CALLING 值与库中 Calling 字段一致；VIP=1 的主叫触发屏显名+姓。
  conditions: c12 外部 ASM 已就绪；32 位 Access ODBC 驱动可用（Access 连接免用户名密码）。
  tags: [lab, access, odbc, select, sql-data]

- id: c15
  title: MS SQL 建库建表：acr_sql 库 + Customer 表（Caller 主键/默认值三件）
  type: howto
  source_pages: p408-415
  source_chapter: Microsoft SQL 2016 Database Table Configuration (CCD09013CB01CGEN)
  source_quote: |
    "Connect to the SQL Server Login: sa Password: Alcatel@1 … Notes Password was defined during the MS SQL
    Server installation" (p409)；
    "Caller nvarchar (50) • Last_Agent varchar (8) • Name varchar (50) • VIP decimal (1, 0)" (p411)
  steps: |
    1. Start / Microsoft SQL Server Management Studio → 连接（sa / Alcatel@1，实验口径，安装时自定义）。
    2. Database 右键 → New Database → 库名 acr_sql。
    3. Tables 右键 → New → Table：Caller nvarchar(50)（Allow Nulls 取消勾选）、Last_Agent varchar(8)、
       Name varchar(50)、VIP decimal(1,0)。
    4. 设默认值：Last_Agent=NoAgent、Name=NoName、VIP=0。
    5. Caller 右键 → Set Primary Key → 保存表名为 Customer。
    6. dbo.Customer 右键 → Edit Top 200 Rows → 核对空表结构。
  verification: |
    表结构四列+主键+默认值与 p415 内容一致（表为空、四列 NULL）。
  conditions: SQL Server 2016 已安装（安装 How-To 见 c19）；登录口令为环境自定义值。
  tags: [howto, sql-server, table, acr-sql]

- id: c16
  title: MS SQL 账号防护：建 SQL 认证登录 Brest/alcatel（关密码策略）+ 映射 acr_sql
  type: howto
  source_pages: p416-420
  source_chapter: Microsoft SQL 2016 Table Access Protection (CCD09013CB02CGEN)
  source_quote: |
    "Login name: Brest Select SQL Server authentication Password: alcatel Confirm: alcatel deactivate
    "Enforce password policy" Default database: acr_sql" (p418)；
    "set Map "acr_sql" to the user Brest Define the Database role membership for: acr_sql" (p419)
  steps: |
    1. SSMS 以 sa 连接 → Security/Logins 右键 → New Login。
    2. Login name=Brest、SQL Server authentication、密码 alcatel/确认 alcatel、取消 "Enforce password
       policy"、默认数据库 acr_sql、默认语言 <default>。
    3. Server Roles 页签按教材截图勾选角色。
    4. User Mapping 页签：勾映射 acr_sql 给 Brest，定义该库的 Database role membership → OK。
    5. 断开重连验证：用 Brest/alcatel 登录 → Databases/acr_sql/Tables/dbo.Customer 右键 → Edit Top 200
       Rows 可编辑。
  verification: |
    Brest 账号可登录并编辑 acr_sql.dbo.Customer（p420）。
  conditions: c15 已建库表；实验口径弱口令，生产必须改强口令并最小授权（见 BOOK_OVERVIEW 批判节）。
  tags: [howto, sql-server, login, security]

- id: c17
  title: MS SQL 装载存储过程：updateCalling 载入 acr_sql 并核验
  type: howto
  source_pages: p421-426
  source_chapter: Microsoft SQL 2016 Stored Procedure (CCD09013CB03CGEN)
  source_quote: |
    "Select /File/Open /File … search for the file "SQL Call Procedure.txt" Drive D:\CCD_ACR\" (p423)；
    "Select "Execute" … You should get a "Commands completed successfully"" (p425)；
    "Select Database/acr_sql/Programmability/dbo.updateCalling" (p426)
  steps: |
    1. SSMS 以 sa 连接 → New Query → 左侧选库 acr_sql。
    2. File/Open/File → 定位 D:\CCD_ACR\ 下的 "SQL Call Procedure.txt"（实验口径路径）→ 打开新窗口。
    3. 全选内容 → 复制 → 切到 SQLQuery1 窗口粘贴。
    4. Execute → 返回 "Commands completed successfully"。
    5. 核验：Database/acr_sql/Programmability 下出现 dbo.updateCalling。
  verification: |
    Programmability 节点下可见 dbo.updateCalling（p426）；执行成功提示（p425）。
  conditions: c15 已建库；过程功能（写 Caller+Last_Agent）在 c18 联调验证。
  tags: [howto, sql-server, stored-procedure]

- id: c18
  title: MS SQL 外部库脚本 sql：连接+updateCalling 写库+SELECT 读库+VIP 分支+ASM 重启持久化验证
  type: lab
  source_pages: p427-452
  source_chapter: External Database (CCD09012CB02CGEN)
  source_quote: |
    "DB[%1] = USE_DATABASE "DNS=acr_sql; UID=brest; PWD=alcatel"" (p438)；
    "SQL_REQUEST DB[%1] CALL "updateCalling" (IN CALLING, IN LAST_CALLED_AGENT)" (p438)；
    "The ASM Server reboot does not impact the "LAST_CALLED_AGENT"" (p452)
  steps: |
    1. 核库：SSMS 17 连 SOFTPANEL（SQL Server 认证，sa/Alcatel@1 或 Brest/alcatel）→ acr_sql/dbo.Customer
       → Edit Top 200 Rows 确认空表。
    2. 建 ODBC：ODBC Data Sources (32-bit) → System DSN → Add → SQL Server → Name=acr_sql、Server=
       SQL 服务器名或 IP（实验口径 151.2.1.20）→ 登录 Brest/alcatel → 默认值下一步 → Finish → Test Data
       Source 应显示 "TEST COMPLETED SUCCESSFULLY"（Notes：ASM 只支持 32 位连接）。
    3. 写脚本 sql（20 个构件两段）：[Part 1] ①USE_DATABASE DB[%1]="DNS=acr_sql; UID=brest; PWD=alcatel"
       → ②SQL_REQUEST DB[%1] CALL "updateCalling" (IN CALLING, IN LAST_CALLED_AGENT) → ③IF
       (DB[%1]<>NULL) → ④STRING[%1]=CALLING → ⑤SQL_REQUEST SELECT "VIP,Name,Last_agent" FROM
       "customer" WHERE "caller={STRING[%1]}" → ⑥IF (SQL_RESULT=SQL_SUCCESS) → ⑦SQL_START_FETCH
       DB[%1] → ⑧SQL_DATA INTEGER[%1]="VIP"/STRING[%2]="Name"/STRING[%3]="Last_agent" →
       ⑨SQL_END_FETCH → ⑩STRING[%4]="UnKnown" → ⑪DISPLAY_AGENT=STRING[%4] → ⑫APPLY
       RULE_ISM CHARACTERISTICS_LIST；[Part 2] ⑬IF (STRING[%3]<>"noAgent") → ⑭IF (INTEGER[%1]=%1)
       → ⑮STRING[%4]="VIP"+" "+STRING[%2] / ⑯STRING[%4]="No VIP"+" "+STRING[%2] →
       ⑰LIST[%1]=(AGENT{STRING[%3]}) → ⑱DISPLAY_AGENT=STRING[%4] → ⑲APPLY
       RULE_AUTHORISED_LIST LIST[%1] → ⑳APPLY RULE_ISM CHARACTERISTICS_LIST。
    4. 首呼测试：脚本挂 31603 → 呼统计 Pilot——表空 → STRING[%3]=默认 NoAgent → ISM 路径；核库表已
       被过程写入 Caller/Last_Agent（写库发生在下一次呼叫读取前，p448）；adm_acd IP@ ASM -salb 28 *
       对照内存中的 LCA。
    5. 二呼：同机再呼——库中 Last_Agent 生效 → AUTHORIZED_LIST LIST[%1]（内容=STRING[%3]）路径；
       屏显 VIP/No VIP+姓名。
    6. 重启持久化验证：ASM Manager 停止再启动 ASM 服务（清内存）→ adm_acd 28 * 确认内存已空 →
     第三呼：LCA 信息从 SQL 库还原，AUTHORIZED_LIST（Last_Agent 31501）依旧生效——ASM 重启不影响
       LAST_CALLED_AGENT。
  verification: |
    p447-452 三组证据链：首呼 ISM+写库、二呼名单路径、重启后第三呼仍走名单；Profiler 侧核验见 p49
    条目（c20）。
  conditions: c15/c16/c17 已完成；外部 ASM + 167 号许可 + 32 位 ODBC（p32/p36 前提）。
  tags: [lab, sql-server, stored-procedure, persistence, lca]

- id: c19
  title: MS SQL Server 2016 与 SSMS 安装（Mixed Mode + sa 口令 + 强制重启）
  type: howto
  source_pages: p453-465
  source_chapter: Microsoft SQL Server 2016 Installation (CCD09013CB04CGEN)
  source_quote: |
    "select Mixed Mode enter the Password for the account "sa" twice Add Current User" (p459)；
    "Click Close and REBOOT the Server … Notes A Reboot is mandatory !!!" (p462)
  steps: |
    1. 运行 SQL 2016 DVD 的 setup.exe → Installation → Specify a free edition（或输入产品密钥）。
    2. 接受许可 → 功能勾选 Database Engine Services → Default Instance → 服务账户默认 → Collation
       默认。
    3. Server Configuration：认证选 Mixed Mode → 输入 sa 口令两次（实验环境即 Alcatel@1 的来源）→
       Add Current User → 数据目录/TempDB/FILESTREAM 全默认 → Install。
    4. 完成后 Close 并强制重启服务器（Notes：重启是强制的）。
    5. 安装 SSMS：安装包 → Install → 完成后再重启（Notes：Server Reboot is mandatory）。
  verification: |
    安装完成且重启后 SSMS 可用 sa 登录（后续 c15/c16/c17 的前置）。
  conditions: Windows 2016 Server 环境（实验口径）；产品密钥/免费版选择按授权情况。
  tags: [howto, sql-server, installation, ssms]

- id: c20
  title: SQL Profiler 观测 updateCalling：Trace 过滤 LoginName=Brest 抓存储过程调用
  type: lab
  source_pages: p466-469
  source_chapter: Microsoft SQL 2016 Profiler (CCD09013CB05CGEN)
  source_quote: |
    "Select /Tools/SQL Server Profiler … Login: sa Password: Alcatel@1" (p467)；
    "Select "LoginName" define Like "Brest" … make a call to the Statistic Pilot Check the exec updateCalling
    Check the declare @p1 …" (p469)
  steps: |
    1. 启动 Profiler：Start / SQL Server Profiler 17（或 SSMS 内 Tools/SQL Server Profiler）→ 连接
       （sa/Alcatel@1，实验口径）。
    2. Trace Properties 保持默认 → Events Selection → 勾 "Show all events" 与 "Show all columns" →
       Column Filters。
    3. 过滤器选 LoginName → Like "Brest" → OK。
    4. 往统计 Pilot 打一通电话 → 跟踪窗口应出现 exec updateCalling 及 declare @p1 … 参数声明。
  verification: |
    Profiler 抓到 Brest 账号下的 exec updateCalling（数据库侧证据，与 c18 的脚本侧行为互证）。
  conditions: c16（Brest 账号）与 c18（脚本）已就位。
  tags: [lab, profiler, stored-procedure, verification]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 17 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 基础 CCD 矩阵 | 有 → c01（19 步全量，含混合链路校验） |
| task-02 脚本编写与调试工具链 | 有 → c02（LCA+ISM、内存、Debugger、LIT 参数） |
| task-03 授权/非授权名单规则 | 有 → c03（List_1/Beginner + 两脚本 + Debugger 实时改条件） |
| task-04 重定向/再分发规则 | 有 → c04（Redirect/Redistri + Voice Guide 队列扩展） |
| task-05 直拨与 ACR 融合 | 有 → c05（直拨 Pilot 31604/私有号/DICA/CALL_TYPE 脚本） |
| task-06 内部数据库定制路由 | 有 → c06（三键三脚本 + 正反用例） |
| task-07 Call Tag 生成与传递 | 有 → c07（IAA 编码叶 + GFW 覆盖验证） |
| task-08 字符串处理 | 有 → c08（单叶 IAA + String 脚本四用例） |
| task-09 多语言语音引导 | 有 → c09（740 引导 + 档案 3 + 偏好验证） |
| task-10 综合脚本能力 | 有 → c10（六脚本 + 混合选呼两场景） |
| task-11 过滤器与统计 | 有 → c11（Filter 1/2/3 + Super-Filter + 实时/Excel） |
| task-12 外部 ASM 割接 | 有 → c12（asm_on_dhs=0 → 服务 → Site → 迁移 → 防火墙） |
| task-13 外部 ASM 双机 | 有 → c13（备机安装/主机改造/同步与切换实测） |
| task-14 外部数据库机制 | 部分 → 机制原理在 principle.md（p36-p40），本章仅 c14/c18 两个落地实验承载 |
| task-15 Access 外部库实验 | 有 → c14 |
| task-16 MS SQL 侧准备 | 有 → c15（建库表）+ c16（账号）+ c17（存储过程）+ c19（安装）+ c20（Profiler） |
| task-17 MS SQL 外部库脚本 | 有 → c18（三呼 + 重启持久化验证链） |

**统计**：20 条（lab 15 条 + howto 5 条）；17 项任务全部有案例类条目或明确分流说明（task-14 的机制语义归 principle，落地由 c14/c18 承载）；每个 How-To 实验章恰好一条，无遗漏、无合并（SQL 准备四 How-To 章与 Profiler 章因验证口径不同各自独立成条）。
