# 原则/清单/规则/公式/数值口径候选 — OmniTouch Contact Center Standard · Advanced (OTCCXTE101EN Ed07)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验教材，所有实验环境给定值（IP、密码、账号、号码）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: ISM 成本公式——Cman 决定排序，Copt 决定同分胜负
  type: formula
  source_pages: p171, p185-186
  source_chapter: ISM / ALGORITHM ISM（How-To 手算章同式复用）
  source_quote: |
    "Mandatory Cost for an agent: • Cman =  ((|Lag(s) - Lcall(s)|) * W(s)) • s: mandatory skills in the attributes
    list • Lag: skill level of the agent profile • Lcall: skill level of the call profile • W: weight of the domain •
    The lowest Cman determines the selected agent … When the Cman are equal, the algorithm selects the agent with the
    lowest Copt • Optional Cost for an agent: • Copt =  ((|Lagent(s) - Lcall(s)|) * W(s)) • s: optional skills in the
    attributes list" (p171)
    "If an Agent doe does not have the Optional Skill the value \"9\" will be set. That's why the value is set to 9
    for the Agent 1 because he has no client skill." (p186)
  summary: |
    两个求和公式：Cman=Σ(|坐席技能等级-呼叫要求等级|×域权重)，只对强制属性求和，最小者胜；同分再算 Copt（对可选属性
    求和，公式同形）。关键边界：坐席没有某可选技能时该技能按等级 9 代入（最大差值惩罚）。手算验证（p185-186，实验口
    径）：Agent1 Cman=(法语 9-3)×1+(车险 4-4)×4+(巴黎 5-1)×2=14，Agent4 Cman=(5-3)×1+(5-4)×4+(5-1)×2=14，同分；
    Copt：Agent1=(寿险 2-1)×4+(客户 9)×3=31，Agent4=(1-1)×4+(2-1)×3=3 → Agent4 排第一。
  conditions: 域权重 1-20、等级 1-9（p164-166）；公式板书在幻灯片中省略了求和符号，以"((...)*W)"形式给出
  tags: [formula, ism, algorithm]

- id: p02
  title: ISM 子列表降级序列——强制属性全满足起步，逐级减一
  type: rule
  source_pages: p168-169
  source_chapter: ISM ALGORITHM
  source_quote: |
    "Agent must have all the mandatory attributes to process the call • Agents are classified according to the result
    of the ISM algorithm • A Reselection timeout is managed from ASM to find agent from sub-list N to sub-list N-1,
    N-2, ... N-N" (p168)
    "1st sub-list: « N » call attributes: with skill level of agent >= skill level of the call • After the timeout •
    2nd sub-list: « N-1 » call attributes: with skill level of agent >= skill level of the call • « 1 » call
    attributes: with skill level of agent < skill level of the call" (p169)
  summary: |
    匹配三规则：①坐席必须具备呼叫档案全部强制属性才进第一子列表（等级判定为坐席≥呼叫）；②超时不中则生成第 2 子列表
    （N-1 项满足 + 1 项不满足），依次降到第 N 子列表（N 项全不满足）；③子列表间由 ASM 的重选定时节拍驱动（间隔由
    RESELECTION_TIMEOUT 决定，见 p12）。注意：强制属性等级不满足的坐席也不会进第一子列表（p185 Agent5 案例——车险
    等级低于要求，只能进后续子列表）。
  conditions: 与 p01 成本公式配合理解——子列表内部才比成本
  tags: [rule, ism, sublist]

- id: p03
  title: asm_ag_free_duration 参数——同分排序在 PLTR 与 LIT 间切换
  type: rule
  source_pages: p179-180
  source_chapter: ISM OPTIONS OF THE FILE PARAMETERS.CFG
  source_quote: |
    "In case same cost the agents can be classified in 2 different ways • Following the default rule or PLTR (period
    logon time ratio) • Following longest idle time or LIT • The method is defined by a new parameter in the file
    parameters.cfg (version mini l2.300.32.a) asm_ag_free_duration • The line must be added by using a text editor" (p179)
    "asm_ag_free_duration=0  use of the rule \"PLTR (Period Logon Time Ratio):\" amount of calls/time to logon. •
    asm_ag_free_duration=1 in this case LIT (Longest Idle Time) is used (rule Idle-time). • asm_ag_free_duration=2 LIT
    in case ASM in network (LIT on local agent or network). • NB: in the case where you wish to use the LIT a specific
    building block 'IDLE' must be added to the program." (p180)
  summary: |
    parameters.cfg（/usr3/afe）新增行 asm_ag_free_duration（最低版本 l2.300.32.a）：0=PLTR（默认，通话时长/登录时长
    比值升序）、1=LIT（最久空闲，需脚本加 IDLE 积木块）、2=网络 ASM 场景的 LIT（本地或网络坐席）。修改流程见 c06：
    nano 编辑 → 值 0 改 1 → 保存 → dhs3_init -R MAIN_AFE 重启 AFE 进程后生效，"Now the agent will be used one after
    the other based on LIT"。
  conditions: 手工用文本编辑器加行，文件里原本没有该参数
  tags: [rule, parameters-cfg, lit, pltr]

- id: p04
  title: 坐席统计 5 分钟刷新——低话务下 LIT 形同轮询
  type: metric
  source_pages: p175, p215
  source_chapter: ALGORITHM ISM：EXAMPLE 2（PLTR 统计期） & ACR Script & ISM Rule Notes
  source_quote: |
    "Same order during the statistic period (5 min by default)" (p175)
    "LIT is not realy working. By default, the agent statistics are refreshed only every 5 min. Which means that with
    a low traffic, the same agent will be rung every 5 min." (p215)
  summary: |
    口径：坐席统计默认每 5 分钟刷新（.inialb 的 StatPeriod 5 与此对应，p272）。推论（书中原话）：低话务量时 LIT 排序
    实际表现为"同一个坐席每 5 分钟被叫一次"，不是严格的逐呼叫公平。给客户承诺"最久空闲优先"前必须先讲清这条粒度。
  conditions: 教材结论为实验观察口径；调小 StatPeriod 属书外操作
  tags: [metric, lit, statistics-period, limitation]

- id: p05
  title: ACR 对象容量上限表
  type: metric
  source_pages: p77
  source_chapter: ACR LIMITS
  source_quote: |
    "Statistic Pilot : 3000 • Pilot : 600 • Queues & Waiting Rooms : 600 • Groups : 450 • Directions between Pilot and
    Queues : 30 • Directions between Queues and Processing Groups : 50 • Domains : 20 • Skills : 1000 •
    Characteristics List : 1000 • Characteristics (per call profile/ per Agent / max) : 7 / 50 / 20000 • Authorized
    List (max number of agents) : 30 • Unauthorized List (max number of agents) : 30. For more Information check the
    Feature List" (p77)
  summary: |
    十二项硬上限逐格：统计 Pilot 3000 / Pilot 600 / 队列与等待室 600 / 组 450 / Pilot→队列方向 30 / 队列→处理组方向
    50 / 域 20 / 技能 1000 / 特征清单 1000 / 特征数（每档案 7、每坐席 50、系统 20000）/ 授权名单 30 坐席 / 非授权名
    单 30 坐席。超出需查 Feature List。
  conditions: R10.15 口径
  tags: [metric, capacity, acr]

- id: p06
  title: 技能体系默认值与区间——域 0-19、技能 0-999、等级 1-9、权重 1-20
  type: metric
  source_pages: p164-166, p150
  source_chapter: CALL PROFILE & AGENT PROFILE & SKILLS（另见 Skill 创建实验）
  source_quote: |
    "Skill Level … Level 1 (low) to 9 (high)" (p164-165)
    "One DOMAIN is made up of • One NUMBER: between 0 and 19 • One NAME: Language for example • One weight: between 1
    and 20 … One skill in a domain is made up of: • One NUMBER: between 0 and 999 … The domains 0 & 1 are created by
    default (language and media) Maximum of 20 domains • Skills from 0 to 99 are created by default (predefined
    languages and media) Maximum of 1000 skills" (p166)
    "Weight Enter the weight from 1 to 20 (i.e. 1) … Name Enter the name of the skill (i.e. Car & Home) (1-16
    characters) Abbrev. Enter the name shown on Agent's display (i.e. Car & Home) (1-4 characters) ID Automatically
    set to the next possible value. You cannot change." (p150)
  summary: |
    逐格区间：域号 0-19（0、1 默认=语言/媒体），域权重 1-20；技能号 0-999（0-99 预定义语言与媒体），技能名 1-16 字
    符、坐席话机显示缩写 1-4 字符，技能 ID 自动分配不可改；等级 1（低）-9（高）；呼叫档案属性最多 7 项、坐席技能最多
    50 项（p102）、坐席技能等级亦 1-9 且默认激活。ABC 网络中域与技能会向全网广播（p150）。
  conditions: 技能编号资源（0-999）与默认段（0-99）规划时要避开预定义段
  tags: [metric, skill, domain, levels]

- id: p07
  title: 坐席列表缓冲 Number of ACR agent buffers——20 起步、400 封顶、默认回 200
  type: metric
  source_pages: p172
  source_chapter: AGENT LIST
  source_quote: |
    "The size of the agent list is defined by the parameter \"Number of ACR agent buffers\" • Under Application / CCD/
    CCD/RSI system parameters • Number of ACR agent buffers = 20 • The value can be managed between 20 and 400 maxi.
    • In case of ACR in network, you will have a good reason to increase this value (to retrieve local and remote
    agents). • By default, maximum 200 agents are returned by the ASM process." (p172)
  summary: |
    参数路径 Application / CCD / CCD / RSI system parameters；页面示例值 20，可调区间 20-400；ASM 进程默认最多返回
    200 坐席（.inialb 里 NbMaxAgent 200 与此互证，p272）。书中给出唯一调优场景：ACR 组网（要取回本地+远端坐席）时应
    调大。其余场景动它之前先想清楚。
  conditions: 两个数字（缓冲 20-400、返回上限 200）并列出现，均如实记录
  tags: [metric, acr, agent-list, rsi]

- id: p08
  title: ASM 脚本命名与产物规则——8 字符名、.scr+.alb、/usr3/afe
  type: rule
  source_pages: p191, p198
  source_chapter: ON-LINE SCRIPT CREATION & COMPILATION
  source_quote: |
    "Script name is limited to 8 characters" (p191)
    "When the script is completed, it must be saved & compiled • 2 files will be generated • \"Script_name\".scr •
    \"Script_name\".alb • The scripts are saved in \"/usr3/afe\" for an internal ASM server (\"alb\" process)" (p198)
  summary: |
    三条硬规则：脚本名 ≤8 字符（ISM、LCA_1、Reselect 等实验名均合规）；保存编译必须成对产出 .scr（源）与 .alb（编
    译产物）；内置 ASM 时两文件存 OXE 的 /usr3/afe（alb 进程工作目录，parameters.cfg 同目录）。命名超长会在创建时被
    拒，规划脚本名要预留缩写空间。
  conditions: 外置 ASM 的存储路径书中未展开
  tags: [rule, script, naming]

- id: p09
  title: 一 Pilot 一脚本——或全 Pilot 公共脚本
  type: rule
  source_pages: p199, p213, p217
  source_chapter: ACTIVATION（How-To 激活步骤 Notes 同文重复）
  source_quote: |
    "1 script per pilot • The same script can be activated on several pilots (pilot selection) • The same script can
    be activated on all pilots (\"common script\" option)" (p199)
    "Only one script per pilot, or one common script for all pilots!" (p213, p217)
  summary: |
    激活约束：一个 ACR Pilot 同一时刻只挂一个脚本；同一脚本可点名挂到多个 Pilot，或选"common script"作用于全部
    Pilot。换脚本=重新 Activate 覆盖。排障时先确认 Pilot 当前挂的是哪个脚本（调试器激活窗口亦会要求选 Pilot）。
  conditions: LCA 系列实验通过"复制脚本→改名→激活到同一 Pilot"实现版本迭代
  tags: [rule, script, activation]

- id: p10
  title: 重选节拍与 21 次上限——RESELECTION_TIMEOUT 与脚本执行次数
  type: metric
  source_pages: p214, p220, p242, p245
  source_chapter: ACR Script & ISM Rule / ISM rule and reselection（Notes）
  source_quote: |
    "The script is used 21 times and the call goes then to the ACR Pilot blocked address if no address is managed the
    \"Blocked Voice Guide\" will be played!" (p214)
    "the alb process makes 21 requests (script is executed 20 times) and in case of empty agent list, the call follows
    the routing management." (p220)
    "The propose of the RESELECTION_TIMEOUT Building Block is to execute the script again after the timeout (example
    10sec.). If the Agents of the 1st sub-list are busy, the 2nd sub-list will be created, after 10 sec. the 3rd
    sub-list and so on." (p242)
    "The maximum number of script execution is 21 times." (p245)
  summary: |
    重选口径：脚本执行上限 21 次（p220 的等价表述为 alb 发起 21 次请求、脚本执行 20 次）；耗尽后呼叫走 ACR Pilot 的
    闭锁地址，未配地址则播 Blocked Voice Guide；RESELECTION_TIMEOUT 积木块（Set a call context variable 设整型秒
    数，实验=10）决定子列表降级/整体重选的间隔——实验观察为"主叫在等待室等 10 秒后 ASM 重执行脚本生成下一子列表"
    （p245）。另一路验证：坐席 Home 技能关掉后打 31651，空列表时呼叫回归路由管理（Int. Overflow 等），最终才是闭锁
    模式（p220）。
  conditions: "21 次"与"20 次+1 请求"两种表述并存，均按原文记录
  tags: [metric, reselection, timeout]

- id: p11
  title: PLTR 计算式——统计期内通话时长/登录时长升序
  type: formula
  source_pages: p175
  source_chapter: ALGORITHM ISM：EXAMPLE 2
  source_quote: |
    "In case of equal cost, agents are sorted increasingly according to their PLTR (Period Logon Time Ratio) • Ratio1
    < ratio2 so agent1 will be sorted before agent4 … ratio1=(20+50+30)/(20*60) ratio1=0,083 … ratio2=(2)/(20)
    ratio2=0,1 … Same order during the statistic period (5 min by default)"
  summary: |
    PLTR=统计期内累计 ACD 通话时长 ÷ 登录时长，升序排前（比值小=更闲）。书例：Agent1 登录 20 分钟、通话 20+50+30=
    100 秒 → 0.083；Agent4 同期通话 2 分钟 → 0.1；Agent1 先被叫。统计期默认 5 分钟，期内排序不变。与 p03 的
    asm_ag_free_duration=0 对应，是同分场景的默认裁决。
  conditions: 例中秒/分钟混用为原书口径，计算结果按原书
  tags: [formula, pltr, sorting]

- id: p12
  title: LCA 脚本范式——IF+关键字的优先级与超时双轨
  type: rule
  source_pages: p254-255, p262
  source_chapter: LAST CALLED AGENT RULE / MANAGEMENT（LCA_1 设计说明）
  source_quote: |
    "Apply the \"Last Called Agent\" rule IF ((LAST_CALLED_AGENT<>NULL) AND (LAST_CALL_ELAPSED_TIME < 1DY))
    RULE_ISM CHARACTERISTICS_LIST RULE_LAST_CALLED_AGENT" (p254)
    "IF Last_Called_Agent <> NULL IF SKILL [\"VIP\"] IN CHARACTERISTICS_LIST UPDATE_LAST_CALLED_AGENT NO
    UPDATE_LAST_CALLED_AGENT YES LAST_CALLED_AGENT Rule ISM Rule" (p255)
    "For the first sequence, ­ If an agent has answered to the caller this day, the system applies a Priority (Call
    Selection Priority) of 2, a Reselection Timeout of 10s and the \"Last Called Agent Rule\" process. ­ If no agent
    has answered or the elapsed time is greater than 1 day, the system applies a Priority level of 8, a Reselection
    Timeout of 20s and the ISM Rule process … But if the sequence is greater than 1, the system applies a Priority of
    2 and the ISM Rule" (p262)
  summary: |
    LCA 标准范式四条：①守门条件=(LAST_CALLED_AGENT<>NULL) AND (LAST_CALL_ELAPSED_TIME<1DY)，满足走 LCA 规则，否则
    回落 ISM；②命中 LCA 时 SET PRIORITY=2 + SET RESELECTION_TIMEOUT=10；回落时 PRIORITY=8 + 超时 20；SEQUENCE>1
    （重选第二圈起）统一 PRIORITY=2 + ISM；③记忆只写"值得记"的主叫——IF LAST_CALLED_AGENT<>NULL 再按是否含 VIP
    技能分支 UPDATE_LAST_CALLED_AGENT（可做差异化记忆策略）；④LCA_2 追加 AND LAST_CALLED_PILOT=PILOT_NUMBER 限定
    "同服务才回头"，LCA_3 再追加 (LAST_CALL_STATE=DROP_OUT_WAITING) OR (LAST_CALL_STATE=DROP_OUT_RINGING) 并把
    PRIORITY 提到 0（放弃重呼最高优先）。
  conditions: PRIORITY 数值语义见 p17（0 最高）
  tags: [rule, lca, script-pattern]

- id: p13
  title: LCA 状态码表 LAST_CALLED_STATE 1-7
  type: metric
  source_pages: p253
  source_chapter: MEMORY CALL STATUS RETRIEVING
  source_quote: |
    "LAST_CALLED_STATE • 1: the last call has been sent to a dissuaded queue • 2: the last call has been answered •
    3: the last call has been sent to a mutual aid queue • 4: the last call has followed the GFW mode • 5: the last
    call has followed the Blockage mode • 6: the last call has been abandoned on waiting • 7: the last call has been
    abandoned on ringing"
  summary: |
    七个状态码逐格：1 劝阻队列、2 已应答、3 互助队列、4 GFW（全局转发）、5 闭锁、6 等待中放弃、7 振铃中放弃。配套关键
    字：LAST_CALLED_AGENT（最后应答坐席）、LAST_CALLED_PILOT（路由 Pilot 号）、LAST_CALLED_DATE、
    LAST_CALLED_ELAPSED_TIME（距上次呼叫时长）。LCA_3 用 6/7 两码识别"放弃重呼"客户。（How-To 中同一条件写作
    LAST_CALL_STATE 与 LAST_CALL_ELAPSED_TIME，命名差异见 n 系列。）
  conditions: 调试器轨迹中空记忆显示 NULL_STATE（p291）
  tags: [metric, lca, state-codes]

- id: p14
  title: ASM 记忆生命周期——alb 重启即清空，MAIN_AFE 重启不清
  type: rule
  source_pages: p252, p272
  source_chapter: FUNCTIONING（next） & ASM memory clean up
  source_quote: |
    "The ASM memory is emptied when the ASM process is re-started. • MAIN_AFE re-starting has no effect on the ASM
    memory." (p252)
    "To clean up the ASM Memory, you must stop the alb process … ps -edf|grep alb … su – Password: Superuser2580* …
    kill -9 5596 … adm_acd 192.168.1.3 -salb select the option: 28* … ASM memory is empty" (p272)
  summary: |
    两条生命周期规则：①ASM（alb）进程重启=记忆清零；②MAIN_AFE 重启不影响记忆——注意与 p03 的参数修改流程冲突点：
    改 asm_ag_free_duration 要重启 MAIN_AFE，但那只让新参数生效，LCA 记忆仍在；要做干净的 LCA 测试必须显式 kill alb。
    清理三步：ps -edf|grep alb 找 PID → su - 提权 → kill -9 <PID>，再用 adm_acd <ASM IP> -salb option 28* 确认为空。
  conditions: kill 前记下 PID 实验值 5596（实验口径，实际以 ps 输出为准）
  tags: [rule, lca, memory, maintenance]

- id: p15
  title: 资源选择优先级数字语义——0 最高、9 最低、同数比 LIT
  type: rule
  source_pages: p363
  source_chapter: Remote Processing Group (How to) / 4.1 Notes
  source_quote: |
    "To manage priority, you must set up a number. It starts from 0 (highest) to 9 (lowest). The lowest is the number,
    the highest is the priority. In this case, where several processing groups are available for a queue, it's the
    processing group with the highest priority that will be selected. If all processing groups have the same priority,
    it's the longest idle time (LIT) that will be applied."
  summary: |
    分配方向的资源选择优先级填数字 0-9：0 最高、9 最低；数字越小优先级越高。同优先级的处理组之间按 LIT（最久空闲）
    裁决。实验验证：Agent_PG=0、Remote_PG=1 时 Agent1 先被叫；Agent1 置 wrap-up 后呼叫流向 Remote_PG 的 Agent3。
  conditions: 与等待室方向选择（f12：同优先级比 EWT）是两套语义，勿混
  tags: [rule, priority, lit]

- id: p16
  title: Remote PG 分布门限语义——等满 N 秒才许流向远端
  type: rule
  source_pages: p364
  source_chapter: Remote Processing Group (How to) / threshold Notes
  source_quote: |
    "thresho. Enter a distribution threshold in seconds (i.e. 15) … Any call waiting longer than this duration can be
    distributed by this direction, which means that the remote PG will be able to receive a call only if it has waited
    in the queue 15 seconds minimum."
  summary: |
    Remote PG 方向的分布门限（Call Selection 页 thresho.，实验=15 秒）：呼叫在队列里等满 15 秒后才允许经该方向流
    向远端——门限就是"本地保底等待时长"。与 p15 优先级、p19 最大等待时间共同构成三级水位控制：先按优先级选方向、
    同级比 LIT、门限控制溢出节奏、MWT 控制队列饱和。
  conditions: 实验观察——Agent1 忙时第二通呼叫 15 秒后转给远端坐席
  tags: [rule, threshold, remote-pg]

- id: p17
  title: 队列最大等待时间与话务采样期——0-3276 秒、2-15 分钟的官方定义
  type: metric
  source_pages: p365
  source_chapter: Remote Processing Group (How to) / 4.2.1 Notes
  source_quote: |
    "Maximum waiting time: Available for normal queues and waiting rooms. This is the threshold of the computed
    waiting time of the queue, after which this queue assumes lowest priority. … When a call is presented, the system
    calculates the computed waiting time. If the result is greater than or equal to the maximum waiting time, the
    priority of the queue is lowered … Enter a value between 0 and 3276 seconds. Use \"Maximum waiting time\"=0 to
    configure a queue without waiting time." (p365)
    "Traffic Sampling Period: Not available for waiting rooms. This is the period from which the system calculates
    the average waiting time in the queue. … Enter a value between 2 and 15 minutes. The correct value of the TSP is
    obtained by successive adjustments … The shorter the TSP, the more the system is able to adapt quickly to sudden
    traffic variations, but with poorer resolution." (p365)
  summary: |
    两参数官方定义：①最大等待时间（普通队列与等待室都可用）——计算等待时间达到阈值即把该队列降为最低优先级；队列
    "大小"由它定义而非能容纳的呼叫数；取值 0-3276 秒；=0 表示无等待队列，下游无资源时呼叫直接改道。②话务采样期
    TSP（等待室不可用）——系统滚动计算平均等待时间的窗口，2-15 分钟；越短对突发流量反应越快但分辨率越差；正确值靠
    反复调整并结合告警观察。实验取值 MWT=10 秒、TSP=2 分钟（快速制造饱和）。
  conditions: EWT>MWT 判饱和（p86）与这里是同一机制的两面
  tags: [metric, queue, mwt, tsp]

- id: p18
  title: ACD 前缀功能键表——1 不可用/2 整理/3 呼班长/5 登出/6 登录
  type: checklist
  source_pages: p346
  source_chapter: Remote Processing Group (How to) / 3.1.1 Notes
  source_quote: |
    "The ACD prefix is mandatory prior to create the CCD matrix objects. … The ACD prefix can be used (by an analog
    station or a station without display) to perform the following actions: prefix ACD then 1 = unavailable … prefix
    ACD then 2 = Wrap up … prefix ACD then 3 = call supervisor … Prefix ACD then 5 = Logoff … Prefix ACD then 6 =
    Logon"
  summary: |
    清单四条：①建任何 CCD 矩阵对象前必须先建 ACD 前缀（Translator > Prefix plan，实验=12，Prefix Meaning=Local
    Features → ACD Prefix）；②无显示屏话机/模拟话机靠"ACD 前缀+数字"完成坐席操作——1=unavailable、2=Wrap up、
    3=呼 supervisor、5=Logoff、6=Logon；③坐席登录/登出功能要在 Categories > Phone Features COS 类别 0 打开 ACD
    Prefixes（值 1）；④默认所有用户同属 COS 类别 0。
  conditions: IP 话机走软键，前缀表是兜底通道
  tags: [checklist, acd-prefix, cos]

- id: p19
  title: DID 翻译三参数与 POD 号码规则——首外号 33210N41000 / 首内号 31000 / 范围 1000
  type: rule
  source_pages: p57, p17
  source_chapter: Finalizing the pod configuration / 2.6 DID Translation（规则源见 SIP 模拟器章）
  source_quote: |
    "According to your POD number, configure the DID translator as follow: ­ First external number: 33210N41000 (where
    N is your POD Number) ­ First internal number: 31000 ­ Range size 1000 … For POD 6: First external number=
    33210641000" (p57)
    "Example: 31002's external nb 3321PN41002 … Dialed number: 0210341002 or 33210341002 … Number sent by the PBX:
    +33210341002" (p17)
  summary: |
    DID 翻译器三参数：首外号=33210N41000（N=POD 号，POD6 即 33210641000）、首内号=31000、范围 1000（覆盖 31000-31999
    → 33210N41000-33210N41999）。呼入拨法两种：0210N41600（带 0 的公网口拨法）或完整号；PBX 收发均带 +33 前缀。配套
    外部 SIP 网关两参数：Registration ID=pbxN、Outgoing username=pbxN（SIP > SIP Ext. Gateway）。全部为实验口径，
    生产按运营商中继号规划。
  conditions: p17 的 3321PN 写法与 p57 的 33210N 写法同义（PN=0N 两位 POD 号）
  tags: [rule, did, numbering, lab]

- id: p20
  title: hybvisu 链路状态与带宽档——四态、两档编解码、接入数 1-24
  type: metric
  source_pages: p342
  source_chapter: Remote Processing Group (How to) / hybvisu 输出字段表
  source_quote: |
    "IDLE : the link is not activated (disabled, or no access defined) ­ SYN_REQ : this side of the link is trying to
    establish ­ SYN_ACK : the other side of the link is trying to establish ­ DATA_TRANS : the link is established and
    ready to transport data … High bandwidth: calls established on this link will allow all codecs (G711, G722, OPUS,
    G729) It is the default value • Low bandwidth: calls established on this link will use G729 codec • Number of
    accesses From 1 to 24"
  summary: |
    直连链路判读表：状态四态 IDLE/SYN_REQ/SYN_ACK/DATA_TRANS（健康=UP(Enabled/DATA_TRANS)）；带宽两档——High（默认，
    全编解码 G711/G722/OPUS/G729）与 Low（强制 G729）；接入数区间 1-24；其余字段：链路号与邻节点号、对端 Main CPUa/
    CPUb IP（CPUb 为空间冗余第二地址）、加密 No/Yes。配合 compvisu sys 看 Direct Link 管理状态与 H.323/RTP Direct
    开关（p341）。
  conditions: 实验链路=Direct link 2002 to node 2
  tags: [metric, hybvisu, link, codecs]

- id: p21
  title: 中继预留两级数学——Max % of trunks out CCD 与 Pilot Trunk limitation
  type: formula
  source_pages: p513-514, p529-530
  source_chapter: SPECIAL FEATURES / BUSINESS TRUNKS RESERVATION & CCDISTRIBUTION TRUNKS RESERVATION FOR A PILOT
  source_quote: |
    "Parameter for each trunk group: • Max % of trunks outside CCdistribution … Example of a SIP trunk group, 80% CCD
    calls maximum … Number of SIP accesses : 2 (31 x 2= 62 SIP trunks) … Max. % of trunks out CCD : 20 … If the total
    % of CCD Time Slots is reached, the caller will hear the busy tone … Trunks reserved for business call (20%) (12
    trunks minimum) • Trunks usable for the CCd (80%) (50 trunks maximum)" (p513)
    "Maximum percent of CCdistribution trunks that can be used simultaneously by a pilot … 80% of the trunk group
    available for CCdistribution calls (50 trunks) • Pilot 1 will be able to use, maximum, 15 trunks among the 50 CCd
    trunks maxi • We will define a trunk limitation of 30% ((15 * 100) / 50)) for the pilot 1" (p514)
    "The SIP trunk contains 62 accesses. From those 62 SIP accesses, 80% are dedicated to CCD, which means about 50
    accesses. 30% of those 50 accesses: stays about 15 accesses available for calls to the pilot 31601." (p530)
  summary: |
    两级预留算法：第一级（中继组）——Max % of trunks out CCD=业务预留百分比，例：62 条 SIP 接入 ×20%≈12 条保底给非
    CC 呼叫，剩 80%≈50 条给 CCd；占比打满后新 CC 呼叫听忙音。第二级（Pilot）——Pilot 限额百分比以"CCd 可用池"为基
    数：15÷50=30%，即单 Pilot 最多同时占 15 条。配置路径：Trunk Groups > Trunk Group（实验=组 1 T2 SIP_Pub_N1，讲义
    示例组 ID 12）与 Applications/CCD/Pilot/<号>/Trunk limitation（Trunk Group ID + Max.% of trunk=30）。
  conditions: "约 50/约 15"为原书取整口径；讲义示例 TG ID 12 与实验 TG ID 1 并存
  tags: [formula, trunk, capacity]

- id: p22
  title: CCS/SPM 默认账户与密码策略基线
  type: checklist
  source_pages: p46, p404, p493
  source_chapter: CCS 安装 / SPM 安装 / CCTA 导入（各章登录步骤）
  source_quote: |
    "User name Enter the login user name (i.e. administrator) Password Enter the default password (i.e. alcatel) You
    will be asked to change the password … The password to be customized must be compliant to following security rules" (p46)
    "Log in the Soft Panel Manager administration using the following username/password: admin/admin This is the
    default login created at startup. It is recommended to change the default password at the first login." (p404)
    "User Enter the mtcl login (i.e. mtcl) Password Enter the mtcl password (i.e. mtcl)" (p493)
  summary: |
    默认凭据清单（实验口径）：CCS=administrator/alcatel 首登强制改密（如 Superuser01*，需满足大写/数字/特殊字符规
    则）；SPM=admin/admin（官方建议首次登录即改）；CCTA Importation 示例=mtcl/mtcl（注意与 OXE 实际口令 Superuser2580*
    不同，按现场实际填）；OXE WBM/Console=mtcl/Superuser2580*、root/Superuser2580*；FlexLM 服务器 root/letacla1；
    ITSP 注册 pbxP/alcatel；SIP 扩展用户密码 123456；IPDSP 个人码 0000。交付检查单第一条：以上全部不得带进生产。
  conditions: 全部为教学约定值
  tags: [checklist, credentials, lab]

- id: p23
  title: SPM 独立部署门槛与最低硬件——500 统计/5 用户/10 面板
  type: metric
  source_pages: p386-387
  source_chapter: SOFT PANEL MANAGER INSTALLATION / HARDWARE & SOFTWARE REQUIREMENTS
  source_quote: |
    "It is recommended to set up the application on a dedicated PC: • If the expected number of statistics and
    calculated data is over 500 • or if the number of simultaneous users is greater than 5 (administrators of Soft
    Panel Manager) • or if the number of panels (hard or soft) is greater than 10 • Minimum hardware requirements: •
    2,4 GHz Dual Core processor • 4 GB memory • 50 GB hard disk • The Soft Panel manager can also be set up on a
    VMWare machine. The virtual machine must respect the same memory and power requirements than a physical machine" (p386)
    "Operating systems: Windows 10 64 bits, Windows 2016, 2019 & 2022 … Call Center Supervision V 10.2.92.0 or greater
    installed on the computer running the RTI Connector." (p387)
  summary: |
    三个"上独享机"触发条件：预期统计+计算数据 >500、同时管理用户 >5、面板（硬+软）>10——任一命中即建议独享 PC。最低
    配置：2.4 GHz 双核 / 4 GB 内存 / 50 GB 磁盘；支持 VMWare（资源需求同物理机）。软件基线：Windows 10 64 位或
    Server 2016/2019/2022；RTI Connector 所在机的 CCS 必须 V10.2.92.0 及以上（CCS 与 RTI Connector 可同机也可分机）。
  conditions: 版本基线随 Edition 迭代，实施前复核发布说明
  tags: [metric, spm, requirements]

- id: p24
  title: SPM 端口/防火墙/浏览器兼容矩阵
  type: checklist
  source_pages: p387
  source_chapter: SOFTWARE REQUIREMENTS
  source_quote: |
    "If you have a firewall on the network, the following IP ports must be open: • default 9060 port or your custom
    port number for Soft Panel Manager server • 61618 for active MQ to send statistics to displays • Firewall is not
    supported on the Soft Panel Manager server computer • Proxy is not supported on the Soft Panel Manager browser"
    "Administration View edition / View display (user's PC) / View display (on Panel PC): Firefox 120 minimum X X X X
    / Chrome 120 minimum X X X X / Edge 120 minimum X X X"
  summary: |
    上线核查清单：①放行端口 9060（SPM 服务器，可自定义）与 61618（ActiveMQ 向显示端送统计）；②SPM 服务器本体不支
    持装防火墙、管理浏览器不支持代理；③浏览器矩阵——Firefox ≥120 与 Chrome ≥120 全场景可用（管理/视图编辑/用户 PC
    显示/Panel PC 显示），Edge ≥120 少一项（不支持 Panel PC 显示列，按原表三个 X）；④视图定制仅限 Firefox（p421，
    见 n 系列）。
  conditions: 端口 61618（Requirements 页）与配置文件示例 WBMPortNum=61668（p391）数字不同，按角色区分：前者为防火
    墙放行值，后者为 RTIConnector.ini 示例值——两处均按原文记录（推断为示例环境差异）
  tags: [checklist, spm, ports, browsers]

- id: p25
  title: SPM 许可清单——OXE 侧 103 号包 + FlexLM 四证
  type: checklist
  source_pages: p388, p405
  source_chapter: LICENSES REQUIREMENTS & RTI 许可核对
  source_quote: |
    "Real Time Interface (RTI) license (nb 103) is required on OXE for the RTI Connector • Check the license using
    \"spadmin\" under mtcl • FlexLM Server: The Soft Panel Manager server must connect to a FlexLM license server to
    check its license." (p388)
    "License name / Description — OTCC_STD_EDITION_SOFTPANEL License needed with the OTCCSE / SOFT_PANEL_NB_DISPLAYS
    License needed for each display / SOFT_PANEL_BUSINESS_DATA License needed to use BD Interface / ECCSTART Internal
    use" (p388)
    "adm_acd and then choose option 15 … Package id=103 WBI Licence current=0 max=100 … Package id=167 ACR Database
    current=0 max=1 … Package id=311 Networking ACR current=0 max=1" (p405)
  summary: |
    许可核查清单：①OXE 侧 RTI 许可=103 号包（WBI Licence），核对两法——mtcl 下 spadmin 或 adm_acd option 15（顺带可
    见全部 CCD 包：78 CCD Ticket、77 CCS Mono/102 Multi/112 Light 各 max=120、167 ACR Database max=1、311 Networking
    ACR max=1 等）；②SPM 侧连 FlexLM 验证（默认 localhost:27000），License 文件须含 OTCC_STD_EDITION_SOFTPANEL
    （随 OTCCSE）、SOFT_PANEL_NB_DISPLAYS（每显示端一证）、SOFT_PANEL_BUSINESS_DATA（业务数据接口）、ECCSTART（内
    部用）；③许可全程在线校验，无证/坏证=管理与显示端常驻告警横幅+统计更新冻结（p411）。
  conditions: 许可文件 softpanel.lic 由授权渠道提供（实验由讲师给）
  tags: [checklist, licensing, flexlm]

- id: p26
  title: SPM 容量三限与冗余限制——500 统计/150 连接/200 面板
  type: metric
  source_pages: p394
  source_chapter: LIMITATIONS
  source_quote: |
    "The limit of subscribed statistics (statistics used in views, calculated data or alarms) is 500 • The Soft Panel
    Manager supports only 150 simultaneous connections • The number of Soft Panels and wallboards declared is limited
    to 200. • OXE 11.1 is supported but with the same limits of previous OXE releases in terms of CCD objects. The
    Soft Panel Manager doesn't support the increase of CCD objects number. • Spatial redundancy is not supported for
    AFE statistics."
  summary: |
    五条限制逐格：订阅统计（视图/计算数据/告警在用的）≤500；同时连接 ≤150；面板+墙板声明总数 ≤200；OXE 11.1 受支持但
    CCD 对象数不因 SPM 放宽（沿用旧版上限，呼应 p77）；AFE 统计不支持空间冗余（afe.sites 多站点亦注明，p416）。
  conditions: 与 p05（ACR 对象上限）组成容量合规双表
  tags: [metric, spm, limitations]

- id: p27
  title: SPM 数据留存参数——history.maxSize 2000/24h 与 RTIConnector.ini 三键
  type: metric
  source_pages: p391, p407, p471
  source_chapter: CONFIGURATION FILES AFTER INSTALLATION
  source_quote: |
    "The Soft Panel Manager server configuration file is located in C:\\SoftPanelServer\\tomcat\\webapps\\wbm\\WEB-
    INF\\classes\\ • wbm.properties • history.maxSize is the maximum number of values the Soft Panel manager server
    keeps in memory for each available counter. The server keeps those values in memory during 24 hours or until
    maxSize is reached. … wbm.history.maxSize=2000" (p391)
    "RTIConnector.ini … WBMHost=151.1.1.10 WBMPortNum=61668 dataSubscriptionTimer=60 #--Time between CCS connection
    and data subscription" (p391)
    "The Soft Panel Manager server will keep in memory a maximum number of 2000 values. If there are less than 2000
    values, the server will keep a maximum of 24 hours of statistics." (p471)
  summary: |
    三个留存/初始化口径：①wbm.properties 的 history.maxSize=2000——每计数器在服务器内存最多留 2000 个值，或最多 24
    小时，先到为准（挂件层同口径，p471）；②RTIConnector.ini 三键——WBMHost（SPM 地址）、WBMPortNum（示例 61668）、
    dataSubscriptionTimer=60（CCS 连上后等 60 秒再订阅数据）；③RTI Connector 日志在安装目录 logs 下
    RTIConnector<日期时间>.log，启动时全量拉取 CCD 对象推给 SPM。
  conditions: 文件示例值（151.1.1.10/61668）为文档示例环境，非实验 POD 值
  tags: [metric, spm, retention, config]

- id: p28
  title: RTI Connector 行为口径——5 秒重连、自动全量同步、统计按需订阅、1 分钟生效
  type: metric
  source_pages: p407-408
  source_chapter: Soft Panel Manager Installation / RTI Connector Notes & Warning
  source_quote: |
    "RTI Connector starts automatically as a windows service. Upon disconnection (or network problem) from WBM or CCS,
    RTI Connector will try to reconnect each 5 seconds. At the start of the RTI Connector, it will retrieve all the
    CCD objects and push them to the Soft Panel Manager. So, all the statistics are available. Statistics are updated
    only when they are used in a view, calculated data, alarms, etc…." (p407)
    "WHEN A STATISTIC IS CHOSEN IN A WIDGET OR IN AN ALARM, IT TAKES AT MOST 1 MINUTE TO BE SUBSCRIBED AND THEN TO BE
    UPDATED" (p408)
  summary: |
    四条行为口径：①Windows 服务自启；②与 WBM 或 CCS 断连后每 5 秒重试；③启动即全量拉取 CCD 对象推送 SPM（统计目
    录全量可见）；④统计只有在被视图/计算数据/告警使用时才更新——新选用的统计最多 1 分钟完成订阅并开始刷新。排障时
    "墙板数值不动"先查该统计是否已被挂件真正引用。
  conditions: 同机警告见 n 系列（CCS 必须专用于 RTI Connector）
  tags: [metric, rti-connector, subscription]

- id: p29
  title: 日统计节拍——15 分钟编译不可更快、每刻后 2 分钟取数、0 点清零
  type: metric
  source_pages: p417
  source_chapter: Soft Panel Manager Installation / 2.6 Daily statistics configuration
  source_quote: |
    "These statistics are retrieved every 15 minutes and reset to 0 at 00h00. This time can't be reduced because the
    statistics are compiled in OXE every 15 minutes. Every retrieval is performed 2 minutes after the quarter hour
    (ex…15h02,15h17,15h32….)"
  summary: |
    三点节拍：取数周期 15 分钟且不可缩短（OXE 侧就是 15 分钟编译一次）；取数时刻=每刻后 2 分钟（15h02、15h17、
    15h32…）；0 点清零。产物命名 S(站点号)_(Pilot 名)_daily_计数器类型，入口 Real Time Data > Statistics > Ccd
    Consolidated。做日报对账时按"每刻+2 分钟"口径取数。
  conditions: afe.sites 多站点分号分隔；空间冗余不支持（p416）
  tags: [metric, daily-statistics, spm]

- id: p30
  title: CCD Filters 使用规则——必配、按需勾选、AgentWidget 三统计、已用不可撤
  type: checklist
  source_pages: p415
  source_chapter: Soft Panel Manager Installation / 2.5 CCD filters settings
  source_quote: |
    "CCD filters are mandatory to define the statistics to be usable in the system (widgets, alarm, wallboards). You
    must check per object type, the statistic to use. Once all the filters are created, you must save the
    configuration by clicking on the Save button. The service will create automatically all the statistics
    corresponding to the filter for all the objects available from RTI Connector." (p415)
    "When your entire configuration (views, alarms, wallboards) is done, you can click on the button Keep used filters
    only … to remove unused filters. … AgentWidget is based on 3 statistics: ServiceState, PhoneStat and StateDuration.
    These 3 statistics should be checked if you want to use AgentWidget." (p415)
    "WHEN A STATISTIC IS USED IN A WIDGET, WALLBOARD OR AN ALARM, THE CORRESPONDING FILTER CANNOT BE UNCHECKED. IF YOU
    WANT TO UNCHECK THE FILTER, YOU HAVE TO REMOVE ALL THE OBJECTS USING THE STATISTIC CORRESPONDING TO IT" (p415)
  summary: |
    五条清单：①过滤器是统计可用性的总开关，不勾不出数；②按对象类型勾选后必须 Save，服务会为 RTI Connector 上所有
    对象自动生成对应统计；③AgentWidget 依赖 ServiceState、PhoneStat、StateDuration 三统计，要用就先勾；④全部配置完
    成后用 Keep used filters only 清理未用过滤器提性能；⑤已在挂件/墙板/告警中使用的统计，其过滤器撤不掉——必须先删
    光引用对象。
  conditions: 实验=两页全勾后 Save
  tags: [checklist, spm, filters]

- id: p31
  title: 面板数据历史与全局样式参数——param.js/panel2.css 关键键值
  type: metric
  source_pages: p429-434
  source_chapter: CONFIGURATION OF THE SOFT PANEL / Global parameters
  source_quote: |
    "Data history parameters can be changed in the file: C:\\SoftPanelServer\\tomcat\\webapps\\wbm\\panel\\param.js …
    historySize: number of counter updates you want to retrieve from Soft Panel Manager and to keep in memory. •
    historyTimer: the number of milliseconds to update the history line chart. … gen_params.historySize = 2000;
    gen_params.historyTimer = 120000;" (p429)
    "param_wallBoardColors.green = \"#41ef00\"; param_wallBoardColors.red = \"red\"; … Graphical widgets default
    colors and text font can be changed in: … param_widgets.titleColor = \"#afa4ff\"; param_widgets.axisLabelColor =
    \"#7363ed\"; param_widgets.axisLineColor = \"#445566\"; param_widgets.axisLegendColor = \"#b3aaf9\";
    param_widgets.axisLegendFont = \"Arial\";" (p430-432)
    "The SoftPanels background color can be changed in: C:\\SoftPanelServer\\tomcat\\webapps\\wbm\\panel\\panel2.css
    … div.mainPage { background-color: #000322; } … The logo file must be located in: C:\\SoftPanelServer\\tomcat\\
    webapps\\wbm\\panel" (p433-434)
  summary: |
    全局样式五处：①param.js 数据历史——historySize=2000（保留的计数器更新个数）、historyTimer=120000 毫秒（折线图刷
    新周期）；②param.js 文字色表 param_wallBoardColors（green=#41ef00 等，可用 color.js 预定义色名）；③param.js 图
    表默认色/字体 param_widgets（titleColor #afa4ff、axisLabelColor #7363ed、axisLineColor #445566、axisLegendColor
    #b3aaf9、axisLegendFont Arial）；④panel2.css 背景色 div.mainPage（#000322）与 Logo 图（div.divLogo，位置在
    mainPanel.css 调 left/right/center）；⑤消息区字体 .MessageDisplay 亦在 panel2.css（p448）。
  conditions: 改 CSS/JS 属服务器文件操作，改前备份
  tags: [metric, soft-panel, param-js, css]

- id: p32
  title: CCS Server 容量与强制条件——15/120、>9 强制、一 AFE 一 Server
  type: metric
  source_pages: p557-558, p567, p575, p590
  source_chapter: CCS SERVER / OVERVIEW & REQUIREMENTS & EXTERNAL CCS SERVER
  source_quote: |
    "Internal CCs server: • 15 CCsupervision Clients simultaneously connected • External CCs server: • 120
    CCsupervision Client simultaneously connected" (p557)
    "The maximum # of connections to the AFE is 15 • The maximum # of connections to the CCs server is 120" (p558)
    "This feature is available since the release R3.1 of the CCd and the CCs 4.3.46.1 • The CCs server is mandatory
    for these releases when the CCs connections numbers to the PCX is greater than 9 (whatever the CCs type, mono-site
    or multi-site)" (p567)
    "The AFE server can receive only one CCs server. • If the service (external CCs server) is started and the process
    (internal CCs server) isn't stopped, the connection of the external CCs server is rejected by the AFE server." (p575)
    "Only 1 CCS Server can connect to the PABX!" (p590)
  summary: |
    容量四则：内部 Server 15 客户端、外部 Server 120 客户端；AFE 物理连接上限 15（内部 Server 自身占 1 条，客户端实得
    14——p558 图示"14 connections max + 1 connection"）；CCd R3.1 + CCs 4.3.46.1 起，CCS 连接数 >9（不分单/多站点）
    必须上 CCS Server；一个 AFE 只接一个 CCS Server，内部进程未停时外部服务会被 AFE 拒接（排障看 adm_acd 的拒接显
    示）。外部 Server 系统要求 Windows Server 2019/2022（p567）。运行态数字：外部服务自报 maxCli=150、maxConnected=120
    （p590）。
  conditions: p558 正文"29 or 120 CCs max"的 29 与图示不符，按图示口径理解（差异见 n 系列）
  tags: [metric, ccs-server, capacity]

- id: p33
  title: CCTA 数据口径——40 种结束原因与 10 种呼叫类型的样例码
  type: metric
  source_pages: p488
  source_chapter: RESULT
  source_quote: |
    "End cause • There are 40 possible end cause whose • 0: call released by the caller • 1: call released by the
    system • 26: call released by the agent • Call type • There are 10 types of call • 0: non ACR • 1: ACR call"
  summary: |
    票据字段口径：结束原因共 40 种，书中举例 0=主叫挂机、1=系统挂机、26=坐席挂机；呼叫类型共 10 种，0=非 ACR 呼叫、
    1=ACR 呼叫。其余编码书中未逐一列出（全表在工具/产品文档）。过滤维度：Headers selection（列选择）+Object
    selection（对象筛选，实验选 Long Ticket、全部对象、ID Mao、Column）。
  conditions: 只列书中给出的样例码，未给全表不编造
  tags: [metric, ccta, tickets]
```

---

## 任务覆盖自检（task ↔ id 映射）

- task-06（ISM 手算）→ p01、p02、p11
- task-08/09（ISM 脚本与 LIT）→ p03、p04
- task-20（容量核对）→ p05、p06、p07、p23、p26、p32
- task-08（脚本规范）→ p08、p09、p10
- task-11（LCA）→ p12、p13、p14
- task-12（Remote PG）→ p15、p16、p20
- task-03（DID/SIP 网关）→ p19
- task-16（特殊功能）→ p21
- task-13（SPM 部署）→ p23、p24、p25、p27、p28
- task-14（SPM 配置）→ p29、p30、p31
- task-18（CCS Server）→ p32
- task-15（CCTA）→ p33
- task-02/19（CCS/维护）→ p22（凭据清单）、p18（ACD 前缀）、p17（队列参数）
- 覆盖自检：33 条 id（p01-p33）连续无缺号；YAML 以 ``` 闭合；数值全部逐格对照原文页码，实验值已标"实验口径"，讲义示例与实验取值并列处均已注明。
