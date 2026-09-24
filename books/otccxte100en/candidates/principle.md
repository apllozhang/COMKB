# 原则/清单/规则/公式/数值口径候选 — OmniTouch Contact Center Standard (OTCCXTE100EN Ed09)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号、分机号）均标注"实验口径"，生产化需替换。数字逐格对照原文。

```yaml
- id: p01
  title: 优先级统一语义——0 最高、9 最低；三类平局规则各不相同
  type: rule
  source_pages: p44, p46-49, p53-58, p110, p117, p119
  source_chapter: Call Routing Rule / Call Distribution Rule
  source_quote: |
    "The routing directions choice, between waiting queues (30max), is done according to priorities or
    according to Expected Waiting Time (in case of same priorities) • Priorities value is from 0 to 9
    • 0 is the highest priority • 9 is the lowest priority" (p44)
    "At equal priorities, the call is routed according to the lowest expected waiting time calculated
    by the system" (p49)
    "At equal priority, the longest idle time (LIT) of the agents in the processing groups" (p53)
    "At Equal priority: the real waiting time of the call at the top of the normal queues" (p53)
  summary: |
    优先级数字三处通用（路由方向、资源选择、呼叫选择），语义统一：0 最高、9 最低，数字越小优先级
    越高（p110 Note："The lowest is the number, the highest is the priority. It starts from 0 (highest)
    up to 9 (lowest)."）。三类平局规则：①路由方向同优先级→系统选 EWT 最低的队列（p49）；②资源选择
    同优先级→选 LIT 最长的 PG（p56）；③呼叫选择同优先级→选队首真实等待时间最长的呼叫（p58）。
    默认 Normal 队列优先级高于其它队列（p110）。
  conditions: 实验设定：Normal_WQ 优先级 0，Overflow_WQ/Redirection_WQ 优先级 9（p110）
  tags: [rule, priority, routing, distribution]

- id: p02
  title: EWT 计算公式与饱和判定
  type: formula
  source_pages: p47-48, p28
  source_chapter: Call routing rule principle (in case of queue congestion)
  source_quote: |
    "An 'Expected Waiting Time' is calculated by the system, and is equal to: EWT = Average wait x
    (Nb of calls in queue + 1)" (p47)
    "The 'Average waiting time' is calculated by the system over the TSP (traffic sampling period)
    which is defined for each waiting queue" (p47)
    "Queue saturation means • Expected waiting time > Maximum waiting time" (p48)
  summary: |
    EWT = 平均等待时间 ×（队列中呼叫数 + 1）；平均等待时间按每队列定义的 TSP（话务采样周期）由系统
    计算，TSP 持续更新、周期越短反应越快（p442 参数说明）。饱和判定：EWT > 最大等待时间（MWT）；
    饱和后来话走规则中的下一优先级方向（intelligent overflow / redirection / 指南劝退）。触发饱和的
    那通呼叫仍留在队里直到座席空闲，除非配置了溢出（p192 "Maximum waiting time alert threshold"）。
  conditions: TSP 校准靠"不同取值+观察告警"的 successive adjustments（p442）
  tags: [formula, ewt, saturation, tsp]

- id: p03
  title: CCD 对象容量上限族（队列/规则/方向/统计 pilot/紧急关闭）
  type: metric
  source_pages: p27, p43, p54, p103, p113, p528, p544-546, p557
  source_chapter: 各章数值汇总
  source_quote: |
    "be shared among several Pilots (30 max) • serve several Processing Groups (50 max)" (p27)
    "A routing rule is managed to associate each pilot with waiting queues (30 rules max per pilot)" (p43)
    "It is possible to declare a maximum of 30 rules per pilot (1200 rules max)." (p103)
    "A call distribution rule (10 max) defines the distribution of the calls to the processing groups
    • A queue can have up to 50 possible distribution directions" (p54)
    "Up to 50 pilot lists can be created • A pilot can belong to several lists • 600 pilots maximum
    in each list" (p528)
    "Up to 3000 statistic pilots can be declared" (p546)
  summary: |
    硬上限逐格：队列——被 30 个 pilot 共享、服务 50 个 PG；路由规则——每 pilot 30 条、全局 1200 条；
    分配规则——全局 10 条，每队列最多 50 个分配方向；紧急关闭——50 个列表、每列表 600 个 pilot、
    列表名 ≤16 字符（p532）；统计 pilot——3000 个，且只能溢出到一个本地路由 pilot、路由 pilot 关联
    统计 pilot 期间不可删除、不能当 direct calls pilot（p546）。
  conditions: 全部为 R10.16 教材口径；生产扩容前对照当版 Feature list
  tags: [metric, limits, capacity]

- id: p04
  title: ACD 前缀动作表——座席/班长在话机上的功能码
  type: checklist
  source_pages: p66, p269, p275, p281, p457, p568
  source_chapter: Basic CCD matrix creation / Agent and Supervisor Features
  source_quote: |
    "prefix ACD then 1 = unavailable • prefix ACD then 2 = Wrap up • prefix ACD then 3 = call
    supervisor • Prefix ACD then 5 = Logoff • Prefix ACD then 6 = Logon" (p66)
    "You can check the state of the private extension by using (displayed during 5 seconds): • ACD
    prefix + 91" (p457)
    "By using the ACD prefix followed by '92', the agent number and secret code when the agent is
    logged off" (p568)
  summary: |
    ACD 前缀（实验前缀 12）动作全集：+1 退出（不可用）、+2 wrap-up、+3 呼叫班长、+5 登出、+6 登入、
    +91 查私人分机状态（显示 5 秒）、+92 登出状态下录欢迎指南（后接座席号+密码）。退出类型扩展：
    有多种退出类型时 +1 后再跟类型号（p347 例：12+1+1 选"Tea"）。前缀必须在话机特性 COS 中启用
    （p134：ACD Prefixes=1）才能登入登出。无显示话机（模拟话机）全靠前缀；数字话机用动态键。
  conditions: 前缀号 12、401（录音）、580（试听）均为法国目标库实验值
  tags: [checklist, acd-prefix, feature-codes]

- id: p05
  title: ACD_Authorized 话机兼容清单——座席与班长的差异
  type: checklist
  source_pages: p33, p267
  source_chapter: Agent and Supervisor / ACD_Authorized phone sets
  source_quote: |
    "Agent • Analog • ALE-300/400/500/20/20H/30H (NOE) • DECT handsets in AGAP: 8232,8242,8262
    • IP Desktop Softphone • Supervisor • Same as agent, except analogue set, DECT and ALE 20H" (p33)
  summary: |
    可登录座席的话机类型：模拟话机、ALE-300/400/500/20/20H/30H（NOE）、AGAP DECT 手持机
    8232/8242/8262、IP Desktop Softphone。班长支持集 = 座席集减去模拟话机、DECT 和 ALE 20H。
    完整兼容性以《Feature list OmniTouch CC Standard Edition – Common Hardware Architecture》为准
    （书中给 Salesforce 内部链与 MyPortal 外部链）。另：IPDSP 作 ACD 话机需启用 IP-Softphone
    Emulation（p128）；Rainbow 场景下 DECT 不支持作 ProACD 设备（p35）。
  conditions: 型号清单为 R10.16 口径；新增话机型号查 Feature list
  tags: [checklist, phone-sets, compatibility]

- id: p06
  title: 座席计时器数值域与默认值——wrap-up / pause / ring rotation
  type: metric
  source_pages: p168, p172, p180-185, p304-312
  source_chapter: Setting up the CCD objects with the CCS
  source_quote: |
    "Pause between two calls … The value, expressed in seconds, must be between 1 and 3276. To delete
    the pause between calls, enter none value." (p168)
    "Wrap Up duration (sec.) … The value, expressed in seconds, must be between 1 and 3276. To delete
    the wrap-up, enter the value 0." (p168)
    "Ring rotation time-out This is the ringing time of an agent before the call overflows to another
    agent within this same group. Enter a value between 1 and 3276 seconds" (p172)
    "enter the default values for Wrap Up duration in Idle state and Wrap Up duration in pause options
    (600 sec)." (p185)
  summary: |
    数值域逐格：pilot 的 pause 与 wrap-up 均为 1-3276 秒；删 pause 填 none、删 wrap-up 填 0。PG 的
    Ring rotation time-out 为 1-3276 秒（实验用默认 15 秒：振铃 15 秒后溢到组内下一座席，p181-182）。
    PG 的手动 wrap-up 时长（idle 态与 pause 态）各 1-3276 秒，可留空，书中默认口径 600 秒。实验值：
    pilot1 wrap-up 10s / pause 5s（p167）；手动 wrap-up 测试值 idle 12s / pause 8s（p183）；EWT 实验
    把 idle wrap-up 拉到 300 秒（p371）。
  conditions: 自动 wrap-up/pause 计时器挂 pilot，手动 wrap-up 时长挂 PG
  tags: [metric, timers, wrap-up, pause]

- id: p07
  title: 服务水平目标与 smiley 三色判定规则
  type: rule
  source_pages: p168, p415
  source_chapter: Setting up the CCD objects / Pilot service level
  source_quote: |
    "The settings affect counters smileys of the pilot. These counters are refreshed according to the
    SOP (supervisor observation period) of 15 min by default. Smiley colors: green (quality of service
    equal to or greater than the warning threshold for this pilot), yellow (quality of service below
    the alert threshold fixed for this pilot while being superior or equal to 0.8 times the threshold),
    red (quality of service less than 0.8 times the alert threshold fixed for this pilot)." (p168)
    "% of calls answered within … Duration is counted at the end of listening to the guide, until
    dropping out of an agent (sum queue + ringtone agent)." (p168)
  summary: |
    服务水平目标两参数：% of calls + answered within（时限）。计时口径：从听完指南起算，到座席
    摘机为止（排队+振铃之和）。smiley 计数按 SOP（班长观察周期）刷新，默认 15 分钟；三色判定：
    绿=达到警告阈值以上；黄=低于告警阈值但 ≥ 阈值×0.8；红=< 阈值×0.8。实验目标值：85% 的呼叫
    15 秒内应答（p167）。Pilot 的 % answered / Efficiency（呼叫失败率）/ ASA（平均应答速度）在 CCS
    的 pilot 服务级别管理页（p82）与 Real time>Pilots S.L.（p415 Pacman 按 SL 变色）呈现。
  conditions: 阈值按 pilot 业务性质设定（信息咨询/售后/投诉等，p168）
  tags: [rule, service-level, smiley, sla]

- id: p08
  title: CCS 实时刷新参数族——快照 3 秒、MSP 5-60 分、饼图 30 秒
  type: metric
  source_pages: p79-80, p402-403, p442-445
  source_chapter: CCS Application Overview / Real time
  source_quote: |
    "Real time refresh frequency (1..50 sec) for real time information refresh • MSP (5 mn …60 mn)
    for statistics on MSP(*)" (p80)
    "The snapshot, refreshed every 3 seconds by default" (p402)
    "For information calculated on MSP • Manageable in the CCs (Window / customize / Real time)" (p403)
    "The pie chart will be updated every 30 seconds, by default. (Windows/Customise… /Real-time/
    Refresh frequency for data on MSP)." (p445)
  summary: |
    三个刷新周期：①实时快照默认 3 秒，可调 1-50 秒（Configurations/System）；②MSP（Monitoring
    Sampling Period，监控采样周期）统计数据 5-60 分钟，班长可自调（Window/Customise/Real time），
    实验口径 MSP=15 分钟；③Agent PG 视图饼图默认 30 秒刷新（同 MSP 刷新设置）。实时统计在每次
    通话结束时更新（p402）。Navigator 的对象信息、座席状态分布、队列计数都吃 3 秒快照。
  conditions: SOP（服务水平 smiley 周期，默认 15 分）与 MSP 是两个独立概念，数值上实验都取 15 分
  tags: [metric, refresh, msp, real-time]

- id: p09
  title: 告警/警报/指示三级定义与 100 条存储上限
  type: rule
  source_pages: p425, p447
  source_chapter: REAL TIME - ALARMS
  source_quote: |
    "Alarms: this list contains the high-level alarms. The number of events stored (100 maxi) is
    indicated in the red coloured circle." (p425)
    "Indications: the indications are messages sent following a creation, modification or deletion of
    a CCd object. In the case of a calendar transition, an indication is sent one minute before." (p425)
  summary: |
    三级事件：Alarms=高级别告警（如 pilot 被关闭，红圈）；Alerts=对象阈值越限（中继组/pilot/队列/PG/
    座席，黄圈，如占忙率超 busy rate alarm threshold）；Indications=CCD 对象增删改的系统消息（蓝圈，
    日历切换前 1 分钟会发预告）。每级最多存 100 条。告警配置入口四处：Trunk group / Pilot / Queue and
    Waiting Room / PG Agent 的 Configurations 页；呈现渠道四种：Alarms 窗口、Navigator 对象闪烁
    （Advanced Options）、声音（Window/Customise/Sounds）、计数器背景色（p426）。实验：把 SIP PUBLIC
    中继组 busy rate alarm threshold 从默认 80% 临时改 1% 触发告警（p439）。
  conditions: busy rate alarm threshold 默认 80%（p439）；改回默认须记得还原
  tags: [rule, alarms, thresholds, 100-max]

- id: p10
  title: ccs.ini 关键参数清单——站点 ID、许可类型、ShowStatisticWithData
  type: checklist
  source_pages: p85-87, p511-512, p502
  source_chapter: CCS.ini file / Show Statistic with Data / Excel parameters
  source_quote: |
    "id_terminal=36" + ";idenfier number for this PC station (0..127); must be unique in your network" (p86)
    "CcsLight=0 ; (if =1, requires CCSLight token; if =0, requires Monosite or Multisite token
    according Multisite parameter)" (p86)
    "ShowStatisticWithData=0 -> works as previously • ShowStatisticWithData=1 -> only agents with
    data are displayed." (p512)
  summary: |
    ccs.ini 检查单：version（示例 10.4.92.0）；my_name（PC 站名，全网唯一）；id_terminal（0..127，
    全网唯一，冲突即异常）；MultiSite（0=单站）；CcsLight（1=CCSLight token，0=按 MultiSite 参数取
    Monosite/Multisite token）；Site n=主名,主端口 2538,备名,备端口 2538,站点前缀,CCS token 服务器
    顺序,RTI token 服务器顺序。升级可保留旧文件；显示/阈值类设置优先走 CUSTOMIZE 窗口。特例：
    ShowStatisticWithData（CCS 10.5 起）必须手写进 [default_configuration] 节，作用于 Agent Session
    Excel 报表。Excel 表单保护密码默认 alcatel（p502）。
  conditions: 改 ccs.ini 后重启 CCS 生效（p95 的 IP 修改同样要求重启）
  tags: [checklist, ccs-ini, parameters]

- id: p11
  title: 统计文件保留期与生成节奏
  type: metric
  source_pages: p479-483
  source_chapter: EXCEL STATISTICS REPORTS - GENERALITIES
  source_quote: |
    "« hr yymmdd.sta » files, with a granularity of ¼ H, ½ H or 1 H. These detailed files are kept 5
    weeks per default" (p481)
    "« dy yymmdd.sta » and « ev yymmdd.sta » files with a granularity of one day. These files are kept
    12 months per default" (p481)
    "Write process after 15 min" (p483)
  summary: |
    保留期：临时文件（obj/tr/ind/te/tc 五类，午夜生成）保留 24 小时；hr*.sta（¼h/½h/1h 粒度明细）
    默认保留 5 周；dy*.sta（对象日统计）与 ev*.sta（状态变化流水：登入登出、退出/指派、PG 开关）
    默认保留 12 个月。生成节奏：午夜 procedure + 1H00 batch-hour；通信票据 RAM 缓存 15 分钟后写盘。
    生命周期可按磁盘容量与信息吞吐量配置。弃用文件"purged or off-limits"（p479）。
  conditions: 路径：临时 /usr4/afe；合并 /DHS3dyn/afe；生命周期可配置
  tags: [metric, statistics, retention, files]

- id: p12
  title: Excel 报表参数口径——对象数、粒度、行偏移与计数口径开关
  type: metric
  source_pages: p484-486, p501-503, p518, p520, p524-525
  source_chapter: EXCEL STATISTICS / Excel statistic (How-To)
  source_quote: |
    "Maximum number of objects that can appear in an Excel form (up to 50). Use Excel (yes or no =
    modification brought to ccs.ini file). Password used to protect the Excel forms. Default =alcatel.
    Check this box to maintain the anonymity of agents in Excel forms." (p502)
    "The second object begin always after 132 rows. To be able to display one day with the granularity
    of ¼ hour, Excel need 96 rows." (p520)
    "Add redirected calls • Box selected: redirected calls (inbound calls on a blocked pilot) are
    counted as redirected calls in the statistics." (p503)
  summary: |
    参数逐格：每类对象默认 1 个、最多 50 个（Window>Customise>Statistics，实验设 5：5 统计 pilot/5
    pilot/1 filter/5 PG/5 座席，改后必须重启 CCS）；编辑类型 Daily（单日）或 Over several days of the
    month（1-31 个连续日）；时间精度 ¼ 小时；粒度 ¼h/½h/1h（多日编辑粒度=一天）；多对象时第二个
    对象从 132 行开始（¼h 粒度一天占 96 行）；三种输出：Print/Save/Excel Display（TEMP.xls）。计数
    口径开关：被关闭 pilot 的来话计入 redirected 还是 inbound；饱和/阻塞断开/中继受限的拒绝呼叫计入
    redirected 还是 handled。自动报表目录 C:\ProgramData\Alcatel\CCSupervisor\Excel\{daily,weekly,
    monthly}（p495 处另出现 A4400 call center supervisor 旧写法，见 n15）；日报输出时刻 1-23 点，周报选
    星期，月报选 1-28 日或 last。
  conditions: 座席匿名化选项与 Excel 密码默认 alcatel；只有 Business 码进 Excel 统计（p344）
  tags: [metric, excel, parameters, granularity]

- id: p13
  title: 语音指南编号规则——3 位指南号 + 4 位消息号（首位语言索引）
  type: rule
  source_pages: p214, p239, p586
  source_chapter: Voice guides management by the set / Multi-language voice guides
  source_quote: |
    "The ideal way to manage the whole messages is to create a voice guide in 3 digits and their
    associated messages in 4 digits. The first digit is for the language index and the 3 others for
    the voice guide. Example: for the guide 683, you will create 2 message. Message 1683 for the
    language #1 (for English). Message 2683 for the language #2 (For French)." (p214)
    "Messages number: from 0 to 5999 • 40 messages per voice guide maximum" (p586)
  summary: |
    编号体系：指南号放 CCD 矩阵（如 683/684/685/688/690/701/702/703/720-722/640/518/538）；消息号
    供话机/录音站录制与选择，4 位（语言索引+指南号）；每个指南的消息数=使用语言数，最多 40 条/指南，
    消息号全域 0-5999。无录音时播备份音 56（Backup Tone，p214）。518 位置指南与 538 欢迎指南为系统
    预置，不可创建或改名（法国库，p389/p574）。变量段消息（3226-4217）由 OXE 预置。
  conditions: 实验分配板位 4-0（OMS）；vgstat 4 0 验装载；选择文件=装入 GD 板 RAM
  tags: [rule, voice-guides, numbering, languages]

- id: p14
  title: 语音指南格式、板卡与存储介质对照
  type: metric
  source_pages: p196-199, p241, p245
  source_chapter: VOICE GUIDES / INSTALLATION
  source_quote: |
    "G711 (64 kbps) for crystal hardware • ADPCM32 (32 kbps ) for common hardware" (p197)
    "The prompts are stored in Flash Memory for static guides and in Ram memory for dynamic guides." (p197)
    "The .wav files available on OTCC_NAS instance have got the following attributes: A-Law, 8000Hz,
    64 Kbps, mono" (p241)
    "SFTP Enable the SFTP connection (mandatory from OXE N3)" (p245)
  summary: |
    格式对照：通用硬件 ADPCM32（32kbps），crystal 硬件 G711（64kbps）；源 .wav 标准属性 A-Law、
    8000Hz、64kbps、单声道。板卡：GD3/GA3（通用硬件）、OMS（免板卡）、GPA2（欢迎指南也存 RAM，
    p568）。存储：静态指南 Flash，动态指南 RAM。转换与传输工具：CCS 的 Audio File Conversion
    （转码+定消息号+命名）与 Audio File Update（经 SFTP 传 OXE，OXE N3 起 SFTP 强制）；欢迎指南
    录音文件落 /usr7/vg/dhs。动态提示替换标准提示后以 ^ 标记已选（p207、p580）。
  conditions: 录音前缀 401 / 试听前缀 580（法国目标库实验值）；无 memo 时自动打标
    "Recorded on set 31007 ***18-08-21 @ 11:59***"（话机号+日期时间，p219）
  tags: [metric, voice-guides, formats, boards, sftp]

- id: p15
  title: 排队位置指南 518 播报规则——位次 1-50 逐个、51-100 步进 5
  type: rule
  source_pages: p376-383
  source_chapter: "CCD WAITING QUEUE POSITION" VOICE GUIDE
  source_quote: |
    "The Variable Part is made of several voice messages that give the positions from 1 to 50 then by
    step of 5 up to 100. • All possible position are broadcast up to 50 • From the 51st position, the
    positions are only broadcast 5 by 5 up to 100" (p377)
    "It is possible to specify a position beyond which the guide will no longer be broadcast to the
    caller (maximum value:100)" (p382)
  summary: |
    位次播报规则：1-50 位逐个精确播报；51-100 位按 5 步进向上取整播报（63 位播 65）；可配最大播报
    位次（上限 100），超过后播 pilot inter-guide 音直至位次回落。每次播报重算位次；第 6 级循环播报。
    语言回退链：呼叫语言未管理→默认语言；未定义默认语言→不播（跳下一 parking level 或 level 6 时播
    inter-guide）；语言管理但子消息缺失→播备份音。优先级呼叫插队后，向位次回退的来电者重播其原
    位次（掩盖回退）。位次指南可放 parking level 或 EWT 表阈值；如需同时播位次+预计等待，要用两个
    连续 parking level（p376）。
  conditions: 16 种语言；固定段/变量段消息号 3226-4217 预置；Max position 实验设 2
  tags: [rule, position-guide, 518, announcements]

- id: p16
  title: 日历容量与切换语义——pilot 10 次/日、分配 20 次/日、50 个特殊日
  type: metric
  source_pages: p610-616, p638
  source_chapter: CALENDAR / Calendar possibilities
  source_quote: |
    "Maximum of 10 time slot transitions for each of the 7 days of the week." (p616, Pilot Calendar)
    "Maximum of 20 time slot transitions for each of the 7 days of the week." (p616, Distribution Calendar)
    "Special days override the days of the weekly calendar • A maximum of 50 special days can be
    defined." (p611)
    "A modification carried out in the active transition does not apply immediately, but rather one
    week later since the change-over is only carried out at the exact time indicated by the transition." (p638)
  summary: |
    容量逐格：pilot 日历每天最多 10 个时间片切换（每切换=规则 ID+状态 Nor/Fwd）；分配日历每天最多
    20 个切换（每切换=分配规则 ID）；特殊日最多 50 个（须填日/月/年，不能选过去日期，覆盖周历；
    pilot 与分配日历各有一套特殊日）。切换语义：只在切换时间点执行 change-over；修改"当前活动中的
    时间片"不立即生效，要等下一次切换点（书中表述为"一周后"的日历循环语义；测试时要提前几分钟改）。
    时间片可跨日复制（Copy one day）；活动时间片在界面上以绿色显示，可核对激活的 ID。
  conditions: 分配日历由班长站配置（p616）；pilot 日历挂在 Call Flow mgt>Call Routing>Calendar per Pilot
  tags: [metric, calendar, transitions, special-days]

- id: p17
  title: 事务码与业务码参数——位数、计时单位与统计口径
  type: metric
  source_pages: p293, p343-344
  source_chapter: TRANSACTION CODE / Agent and supervisor features (How-To)
  source_quote: |
    "Transaction code from 1 to 15 digits • These codes are only stored in the CCD call records
    • Business codes from 1 to 3 digits • this codes are used in statistics" (p293)
    "Transaction Code Dialing Timer … (the unit is 100ms). The minimum value allowed is 10." (p343)
    "Only calls assigned to type codes Business appear in the EXCEL statistics." (p344)
  summary: |
    两类码：事务码 1-15 位（只存通话记录）；业务码 1-3 位（进统计，上限 1000 个，p478）。配置项：
    摘码计时器（单位 100ms，最小值 10=1 秒；实验设 10 秒）、位数（0=不摘码；1-15=事务码，
    Business Code=No；1-3=业务码，Business Code=Yes）、Business Code 属性。座席在通话结束后、wrap-up
    前摘码，可用动态键修改/擦除/取消。统计口径：只有 Business 码出现在 Excel 统计中。
  conditions: 配置位置：OXE Applications>CCD>Pilot>TRANSACTION CODE DIALING（p343）
  tags: [metric, transaction-code, business-code, statistics]

- id: p18
  title: 命令行工具箱——acdsup / hybvisu / rsthyb / config / vgstat
  type: checklist
  source_pages: p76-77, p120, p165, p215, p220, p247, p393, p579
  source_chapter: 各 How-To 的 OXE console / SSH session
  source_quote: |
    "From an OXE SSH session, check the CCD matrix configuration. … Enter the command acdsetup …
    A=agent group F=Forward group V=Voice guide processing group CLO= pilot closed" (p76-77)
    "OPN OPN=Open = the Pilot is in normal state." (p120)
    "Type hybvisu -f all … The two accesses must be 'UP'. Possibly make a phone call to the pilot
    internally. In the event of congestion, use the rsthyb command to restart the ABC-F link." (p165)
    "launch config 4 command … launch vgstat 4 0 command … Such command allows to check which static
    voice guides are installed." (p215)
  summary: |
    mtcl 会话命令清单：acdsup——看 CCD 矩阵总览（A=座席组、F=前转组、V=语音指南组、CLO=pilot 关闭、
    OPN=pilot 正常态；章节标题用 acdsup，正文一处写 acdsetup，见 n13）；hybvisu -f all——查 ABC-F
    链路两条 access 是否 UP；rsthyb——拥塞时重启 ABC-F 链路；config 4——查 OMS 板在服；vgstat 4 0——
    查装载到 GD 板的静态/动态指南（含 ^ 选中标记）。SSH 客户端为 PuTTY（会话 OXE-SSH，需设 ISO-
    8859-1 字符集与 Unicode 线框码点，p76）。
  conditions: 实验口径：PuTTY 会话已保存于 Client PC 10；命令均在 mtcl 会话执行
  tags: [checklist, cli, commands, oxe]

- id: p19
  title: Rainbow CCD 座席前提与三种登录形态的能力边界
  type: rule
  source_pages: p34-37
  source_chapter: CCD APPLICATION OVERVIEW / CCD agent on Rainbow
  source_quote: |
    "Rainbow user can be used as a CCD Agent (CCD Supervisor not supported)" (p34)
    "ACD set must not be part of any multiset, • It must not be associated to a Rainbow user • DECT
    sets are not supported as ProACD devices" (p35)
    "With the WebRTC Gateway, we can have a CCD agent on a Rainbow softphone • The Rainbow application
    doesn't require VPN or SBC to support remote worker use case" (p34)
  summary: |
    硬规则三条：ACD 话机不得属于任何 multiset、不得关联 Rainbow 用户、DECT 不支持作 ProACD 设备。
    Rainbow 侧只支持座席角色（无班长），账号专用、分机唯一（=CCD agent number）。三种登录：
    office phone（CSTA 监控物理 ACD 话机）、other phone（登录 REX 池、改址到其它号码）、computer
    （REX 改址到 WebRTC 网关 SIP 中继，音频走 WebRTC）。卖点：远程坐席免 VPN/SBC。
  conditions: computer 方式需要 WebRTC 网关；CCD 班长功能无 Rainbow 形态
  tags: [rule, rainbow, ccd-agent, restrictions]

- id: p20
  title: CCD Direct Calls 呼叫性质判定表（含去话与内部呼叫）
  type: rule
  source_pages: p450-456
  source_chapter: CCD DIRECT CALLS
  source_quote: |
    "Incoming direct ACD calls: • On agent number (agent is free) -> CCD call • On agent number
    (agent is in partial unavailable) -> CCD call • On agent number (agent unavailable or busy:
    transaction code, wrap-up, in call, pause) -> overflow to 'the pilot direct call' (CCD call)" (p456)
    "Outgoing calls done by the agent: • Agent is not in unavailable state -> CCD call • Agent is in
    partial unavailable state -> CCD call • Agent is in unavailable state -> Private call • Internal
    call • Towards agent number or private number -> Private call" (p456)
  summary: |
    判定规则：私人号 = 座席 CCD 号时，打到座席话机的所有外线来话都是 CCD 呼叫；两号不同时，打
    CCD 号的是 CCD、打私人号的是私人呼叫。来话：空闲或部分退出→CCD；不可用/忙（事务码、wrap-up、
    通话、pause）→溢出到 pilot direct call。去话：非不可用态与部分退出态→CCD 呼叫（吃 wrap-up/pause、
    进统计）；完全不可用态→私人呼叫。内部呼叫（打座席号或私人号）一律私人呼叫。私人号须在编号
    计划内，在 Users 菜单声明为物理分机（business 或 ACD_Authorized 型）、虚拟分机或座席分机；
    登录时自动前转到座席号，登出自动取消（p454）。
  conditions: 溢出延时取决于 access COS；暂停/不可用态来话播介绍指南（p455）
  tags: [rule, direct-calls, ccd-vs-private, forwarding]

- id: p21
  title: 紧急关闭行为规则——重定向优先级、转移限制与统计归属
  type: rule
  source_pages: p527-529
  source_chapter: EMERGENCY CLOSURE
  source_quote: |
    "When emergency closure is activated, the direct calls to a pilot in emergency closure are
    redirected in priority to the emergency closure address of the pilot (if there is one) or to the
    emergency closure voice guide of the pilot" (p528)
    "Transfer to a pilot in emergency closure: transfer to a pilot in emergency closure is only
    authorized if an emergency closure address has been configured and is reachable. Transfer is
    denied if the address has not been configured" (p528)
    "The calls received in emergency closure state by a pilot are included in the « calls received in
    general forwarding state » counter." (p529)
  summary: |
    三条行为规则：①激活动作优先级——来话优先转到紧急关闭地址（若配置且可达），否则播紧急关闭
    指南；②direct call 联动——座席的 pilot direct call 被紧急关闭时，打座席的直达来话同样优先转
    关闭地址/指南，无论座席状态；③转移限制——向处于紧急关闭的 pilot 转移，仅在关闭地址已配置且
    可达时允许，未配置则拒绝转移。统计归属：紧急关闭期间的来话计入"通用转发态来话"计数器。
  conditions: 激活/查看历史需 CCS ADMINISTRATOR（p542）；实验列表 Emergency0 含 31600/31601/31603
  tags: [rule, emergency-closure, transfer, statistics]

- id: p22
  title: 统计型 pilot 行为规则——问候指南播放条件与显示选项
  type: rule
  source_pages: p543-551
  source_chapter: STATISTICS PILOTS
  source_quote: |
    "The presentation voice guide of the statistics pilots for blocked States and general forwarding,
    will be played if: • the routing pilot is in blocked State or general forwarding on rule • this
    rule is valid (at least 1 direction is open and) available)" (p545)
    "That's why the routing pilot has to be closed or blocked on RULE." (p545)
    "Different display on the agent set (depending on management) • Caller characteristics (caller
    number) • Pilot characteristics (pilot name) • Call Tag • Entity characteristics (entity name)" (p550)
  summary: |
    行为规则：统计 pilot 被叫→先播其问候指南→转关联路由 pilot；统计 pilot 无指南→播路由 pilot 的
    问候指南；路由 pilot 按指南/地址方式关闭或阻塞→统计 pilot 问候指南不播，来话按路由 pilot 的
    分发走；路由 pilot 按规则（rule）关闭/阻塞且规则有效（至少 1 个方向开且可用）→播统计 pilot 对应
    状态的问候指南。座席话机显示可配四种：主叫号码 / pilot 名 / Call Tag（≤32 字符）/ 实体名；
    无 call tag 时显示主叫与 pilot 特征（p558）。PG 侧 Call Tag Display Timer：0=只在振铃期显示，
    >0=振铃期+接通后按该秒数显示。
  conditions: 网络场景：PilStat 号需经前缀（Meaning=Network No.，Type=Statistic Pilot）广播到各节点（p549）
  tags: [rule, statistics-pilot, call-tag, greeting]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-22）的原则/数值类覆盖率

| task | 任务 | 数值类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 实验环境与 SIP 模拟器 | 弱（结构为主） | — | IP/账号全集在 framework f02/f03 标注实验口径 |
| task-02 | CCD 矩阵模型 | 有 | p01, p02, p03 | 优先级语义、EWT 公式、容量上限 |
| task-03 | 基础 CCD 矩阵 | 有 | p04, p18 | ACD 前缀、acdsup 判读 |
| task-04 | 安装配置 CCS | 有 | p10 | ccs.ini 参数 |
| task-05 | 路由与分配规则 | 有 | p01, p03 | 优先级与平局规则、10/30/50 上限 |
| task-06 | 座席/班长创建 | 有 | p04, p05, p06 | 前缀、话机兼容、计时器 |
| task-07 | 收尾 POD | 弱 | — | DID/SIP 参数见 case 实验值 |
| task-08 | ABC-F 链路 | 有 | p18 | hybvisu/rsthyb |
| task-09 | CCS 调优对象 | 有 | p06, p07, p08 | 计时器、SLA/smiley、刷新周期 |
| task-10 | 话机录指南 | 有 | p13, p14 | 编号规则、格式板卡 |
| task-11 | .wav 导入 | 有 | p14 | A-Law 属性、SFTP 强制 |
| task-12 | 座席班长特性讲义 | 有 | p06, p17 | 计时器、事务/业务码 |
| task-13 | 座席班长特性配置 | 有 | p17, p18 | 码参数、命令行验证 |
| task-14 | EWT 与交互排队 | 有 | p02 | EWT 公式、TSP |
| task-15 | 位置指南 518 | 有 | p15 | 位次播报与语言回退 |
| task-16 | 实时监控告警 | 有 | p08, p09 | 刷新族、三级告警、80% 默认阈值 |
| task-17 | CCD 直接呼叫 | 有 | p20 | 呼叫性质判定 |
| task-18 | Excel 统计 | 有 | p11, p12, p17 | 保留期、报表参数、业务码口径 |
| task-19 | 紧急关闭 | 有 | p21 | 行为三规则 |
| task-20 | 统计 pilot | 有 | p22, p03 | 问候条件、call tag、3000 上限 |
| task-21 | 座席欢迎指南 | 有 | p13, p14 | 538/4500 编号、RAM/板卡 |
| task-22 | 多语言与日历 | 有 | p13, p16 | 40 消息/指南、日历容量与切换语义 |

说明：Rainbow CCD 座席（p19）不对应独立 task，属 BOOK_OVERVIEW 骨架"增值能力域"的知识点，已并入 task-02/12 的讲义范围。全部数值均对照原文页码摘录，实验值已标"实验口径"。
