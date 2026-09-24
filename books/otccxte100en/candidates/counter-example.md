# 反例/限制/边界/易错点候选 — OmniTouch Contact Center Standard (OTCCXTE100EN Ed09)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: warning=原书显式 Warning / limitation=限制 / version-trap=版本陷阱 / misconception=易误解点 / doc-error=原书文档缺陷 / out-of-scope=书外边界
> 扫描口径：全书逐页扫 Warning / Notes / 注意事项，原书显式 Warning 全部收录（p162、p117、p469、p542、p346 等）；推断性结论标注"（推断）"。

```yaml
- id: n01
  title: 分配方向默认全部关闭——连好线不等于能通话
  type: warning
  source_pages: p117, p119
  source_chapter: Creation of the rules / 2.3 Activation of the Call Distribution rules
  source_quote: |
    "Warning … BY DEFAULT, ALL DIRECTION RULES ARE CLOSED" (p117)
    "It is possible to open or to close a direction toward a processing group. By default, the
    direction is closed." (p119)
  summary: |
    建好分配点（queue→PG 连线）后 Navigator 上显示黄色连接点，含义是"已创建未激活"；必须逐条进入
    Resource selection 页签勾选 Direction 并 Save，连接点才变红/绿。新手最常见的事故：矩阵看着齐全、
    来话却全部走不通，原因就是方向没开。
  conditions: 任何新建分配方向、新增 PG 接线之后
  tags: [warning, direction, activation, navigator]

- id: n02
  title: 分配规则默认停用，且只能从 OXE 侧激活
  type: warning
  source_pages: p113, p626-627
  source_chapter: Creation of the rules / 2.1.2 Rule activation; Calendar / 3.2
  source_quote: |
    "By default, the call distribution rule is deactivated. You must activate the rule from OXE
    management console. It is also possible to activate the call distribution rule from CCS using a
    calendar. A maximum of 10 call distribution rules can be created." (p113)
  summary: |
    CCS 里点 Create 建出的分配规则是停用态；激活入口在 OXE Web Admin（Applications> CCD> Distribution
    Rule> 勾 Active Rule），日历激活属于例外路径。只配 CCS 不回 OXE 激活，规则整体不生效。新建的
    Closed_rule 同样要回 OXE 激活（p626-627 显示节点名带 ".false" 后缀即未激活态）。
  conditions: 每条新建/复制的分配规则
  tags: [warning, distribution-rule, oxo-activation]

- id: n03
  title: ABC-F 链路必须"同节点、不同网络"
  type: warning
  source_pages: p162
  source_chapter: Local hybrid ABC-F link / 2.1 Check the system node number and network number
  source_quote: |
    "Warning … ABC-F LINK MUST BE DELARED ON THE SAME NODE, BUT IN A DIFFERENT NETWORK" (p162，原文
    DELARED 为原书拼写错误，即 DECLARED)
  summary: |
    建本地混合链路前先在 System 页核对 Node 号与 Network 号：同 Node 是硬条件，Network 必须不同，
    否则链路建不通。前置还有一条：pilot 的 ABC Local Call Allowed 必须启用（法国目标库默认启用，
    其它目标库未必）。
  conditions: 内呼 pilot 不通、排查本地混合链路时
  tags: [warning, abc-f, node, network]

- id: n04
  title: 本地混合链路不能用于 CCD 直接呼叫功能
  type: warning
  source_pages: p469
  source_chapter: CCD direct calls / 3 Test the pilot for direct calls
  source_quote: |
    "Warning … THE LOCAL HYBRID LINK CANNOT BE USED FOR THE DIRECT CALL FACILITY." (p469)
  summary: |
    c06 刚建好的本地 ABC-F 混合链路（内呼 pilot 用）在 direct call 场景下不可用——打座席号/私人号的
    公网来话走公网中继，不能借本地链路环回。测试 direct call 必须从 MicroSIP-Public 公网入口拨。
  conditions: CCD direct calls 实验与生产部署
  tags: [warning, direct-calls, abc-f, test-path]

- id: n05
  title: 紧急关闭列表操作需要 CCS ADMINISTRATOR，且测完必须停用
  type: warning
  source_pages: p542
  source_chapter: Emergency closure / 5 Test the feature
  source_quote: |
    "You MUST be a CCS ADMINISTRATOR to be able to select the pilot in the emergency closure pilot
    list. Don't forget to deactivate again the emergency closure list Emergency0." (p542)
  summary: |
    两条纪律：①非管理员账号在紧急关闭界面选不了 pilot，会误判为"功能坏了"；②实验/演练结束后必须
    Deactivate，否则全公司来话持续被关闭转移到指南，属于高危遗留操作。
  conditions: 演练紧急关闭、权限分配
  tags: [warning, emergency-closure, permission, cleanup]

- id: n06
  title: 模拟话机前缀附录仅供参考，书中明令不要执行
  type: warning
  source_pages: p346-347
  source_chapter: Agent and supervisor features / 8 Annex
  source_quote: |
    "THIS ANNEX SUM UP A SET OF POSSIBLE PREFIXES YOU CAN MANAGE ON OXE CALL SERVER. SUCH PREFIXES CAN
    BE HANDLED BY AN AGENT USING AN ANALOGUE TERMINAL. THE FOLLOWING PROCESS IS FOR INFORMATION ONLY.
    DO NOT PROCEED." (p346)
  summary: |
    第 8 章 Annex（Manual Hold 前缀 67、Park Call/Retrieve 前缀 66 的创建步骤）标注"仅供参考、不要
    执行"——实验环境不建这两个前缀。提取自动化流程时应把该章标记为知识参考而非可执行步骤。
  conditions: 消化本章内容、生成操作指引时
  tags: [warning, annex, reference-only, prefixes]

- id: n07
  title: 日历"活动时间片"上的修改不立即生效
  type: limitation
  source_pages: p638
  source_chapter: Calendar / 4.2.2 For special days (Notes)
  source_quote: |
    "A modification carried out in the active transition does not apply immediately, but rather one
    week later since the change-over is only carried out at the exact time indicated by the
    transition. In the case of a test, a modification on a transaction must be carried out a few
    minutes before it becomes active." (p638)
  summary: |
    切换只在时间片定义的时间点执行；改"正在活动中的时间片"不会即时切换（原书表述为按日历循环"一周
    后"才轮到），验证日历改动要提前几分钟改下一个即将生效的时间片。现场"改了日历怎么不生效"的工单
    多半是这一条。
  conditions: 调整日历、验证切换行为
  tags: [limitation, calendar, transition, timing]

- id: n08
  title: OXE N3 起 .wav 传输强制 SFTP
  type: version-trap
  source_pages: p245
  source_chapter: Voice guides management by downloading .wav files / 2.2 Files transfer
  source_quote: |
    "SFTP Enable the SFTP connection (mandatory from OXE N3) … The SFTP option must be selected if
    SSH connection has been implemented on OXE side. The SFTP option is mandatory from OXE N3." (p245)
  summary: |
    CCS 的 Audio File Update 传输语音文件时，OXE N3 及以后版本必须勾 SFTP（且 OXE 侧已实现 SSH），
    否则传输失败。老版本升级到 N3 后，沿用旧操作口径会在这里卡住。
  conditions: OXE N3 及以上传输语音文件
  tags: [version-trap, sftp, voice-guides, oxe-n3]

- id: n09
  title: 混合链路自 OXE R100 起默认创建，但 access 仍须手工建
  type: version-trap
  source_pages: p163-165
  source_chapter: Local hybrid ABC-F link / 3.1-3.2
  source_quote: |
    "The hybrid link is created by default since OXE R100. If it's not the case, you will have to
    create such link instead of checking its creation." (p163)
    "Even if the local hybrid link is created by default from OXE N1, the accesses need to be created." (p165)
  summary: |
    版本语义：R100 之后 Loop-Hybrid 的 Multi access hybrid link 默认启用，动作从"创建"变"核对"；
    但两条 access（Hybrid or Direct Link Access，B Channel）任何版本都要手工创建。把"链路默认有"
    理解成"什么都不用配"是典型错误。
  conditions: R100 前后版本迁移、内呼 pilot 排障
  tags: [version-trap, abc-f, r100, accesses]

- id: n10
  title: ShowStatisticWithData（CCS 10.5）无界面入口，必须手改 ccs.ini
  type: version-trap
  source_pages: p511-512
  source_chapter: SHOW STATISTIC WITH DATA
  source_quote: |
    "A new feature concerning the statistics for agents is provided in CCS 10.5: • Show statistics
    only if data: • The file CCS.ini must be modified (new parameter ShowStatisticWithData)." (p511)
    "ShowStatisticWithData=0 -> works as previously • ShowStatisticWithData=1 -> only agents with
    data are displayed." (p512)
  summary: |
    该特性只能手写进 ccs.ini 的 [default_configuration] 节（多数显示设置可走 CUSTOMIZE 窗口，这是
    例外）；作用于 Agent Session Excel 报表。CCS 版本低于 10.5 无此参数。
  conditions: 座席会话报表出现大量无数据座席时
  tags: [version-trap, ccs-105, ccs-ini, excel]

- id: n11
  title: 原书自相矛盾——WebAdmin 登录口令两处不一致
  type: doc-error
  source_pages: p65, p153
  source_chapter: Basic CCD matrix creation vs Finalizing the pod configuration
  source_quote: |
    "Login Enter the mtcl login (i.e. mtcl) Password Enter the mtcl password (i.e. Superuser2580*)" (p65)
    "OXE WebAdmin (https://192.168.1.3) Enter the mtcl credential: - login: mtcl - password: mtcl" (p153)
  summary: |
    全书绝大多数章节 OXE Web Admin 用 mtcl/Superuser2580*（实验口径），唯独收尾章 p153 写
    mtcl/mtcl。执行 c05 时若按 p153 口令登录失败，应回退 Superuser2580*。属原书排版缺陷，不代表
    生产口令口径。
  conditions: 实验 c05、文档复用
  tags: [doc-error, credentials, inconsistency]

- id: n12
  title: 原书表格缺陷——建队列三步的字段值全部复制粘贴成 31701/Overflow_WQ
  type: doc-error
  source_pages: p71-73
  source_chapter: Basic CCD matrix creation / 3 Create the waiting queues
  source_quote: |
    "3.1. Create the normal type waiting queue … Directory Number Enter the directory number of the
    waiting queue (i.e. 31701) Name Enter the name of the waiting queue (i.e. Overflow_WQ)" (p71)
  summary: |
    3.1/3.2/3.3 三步的截图字段表依次应为 31700 Normal_WQ、31701 Overflow_WQ、31702 Redirection_WQ，
    但原书三张字段表全部误写为 31701/Overflow_WQ。照抄建出的矩阵三个队列撞号。自动化提取时以章节
    标题与 Implementation 目标矩阵（p64）为准。
  conditions: 重建基础矩阵、生成自动化脚本
  tags: [doc-error, queue, copy-paste]

- id: n13
  title: 命令名不一致——acdsup 与 acdsetup 混用
  type: doc-error
  source_pages: p76-77, p120
  source_chapter: Basic CCD matrix creation / 5 Control with command acdsup
  source_quote: |
    "5 Control with command acdsup … Enter the command acdsetup" (p76-77 章节标题与正文命令名不一致)
  summary: |
    章节标题与结果核对用 acdsup，正文步骤写 acdsetup。OXE 实际命令以现场为准（推断：应为 acdsup，
    p120 也是 acdsup；acdsetup 疑为笔误）。命令输出的判读字母（A/F/V/CLO/OPN）两种写法下一致。
  conditions: mtcl 会话验证矩阵
  tags: [doc-error, cli, acdsup]

- id: n14
  title: 原书多处编号笔误（座席号/指南号/pilot 号串写）
  type: doc-error
  source_pages: p188, p190, p335, p394, p432, p589, p601
  source_chapter: 多章
  source_quote: |
    "Call Pilot1 (31600) again and check that Agent2 (31502) answers to the call." (p188，应为 31501)
    "Press the Closing 3100 key previously set up." (p335，应为 31800)
    "VG Sub-message No. Enter the sub-message number previously set up (i.e. 3328)" (p394，上文为
    3228/3229)
    "Rename the Name tab field by the pilot number. (i.e. 31600)" (p432，Tab6 对应的是 31601)
    "Affect the language French for the pilot 31602 and English for the pilot 31602" (p589，第二个
    应为 31600)
    "Guide number Enter the guide number for french language (i.e. 702)" (p601，此处是给 EN pilot
    31600 配指南)
  summary: |
    原书存在成串的编号笔误：Agent2 写成 31502（p188/p190）、Closing PG 键写成 3100（p335）、固定段
    消息 3228/3229 写成 3328/3329（p394）、Tab6 页签名复制成 31600（p432）、多语言章两个 pilot 都写成
    31602（p589）、EN pilot 的指南说明写"french language"（p601）。复用书中步骤时须按上下文纠正，
    不能逐字照抄。
  conditions: 生成自动化指引、照书排障
  tags: [doc-error, typos, numbering]

- id: n15
  title: 统计备份目录路径两处写法不一致
  type: doc-error
  source_pages: p495, p500, p526
  source_chapter: EXCEL STATISTICS / Automatic edition & restart
  source_quote: |
    "C:\ ProgramData\ Alcatel\ A4400 call center supervisor \ Excel \ \daily \weekly \monthly" (p495)
    "C:\ProgramData\Alcatel\CCSupervisor\Excel … \daily \weekly \monthly" (p500)
  summary: |
    自动报表输出目录一处写 "A4400 call center supervisor"、两处写 "CCSupervisor"。实际以本机
    CCS 安装为准（推断：CCSupervisor 为现行目录名，A4400 为历史产品名残留）。找报表文件时两个
    路径都查。
  conditions: 定位自动报表产物
  tags: [doc-error, path, statistics]

- id: n16
  title: 语言索引与文件名混乱——英文时而映射语言 1、时而语言 2；"twenty" 文件名复用
  type: doc-error
  source_pages: p214, p361-363, p390
  source_chapter: Voice guides by the set / Expected Waiting Time / Waiting queue position
  source_quote: |
    "Message 1683 for the language #1 (for English). Message 2683 for the language #2 (For French)." (p214)
    "Only language #2 must be set up." (p361，指英文消息 2720/2721/2722)
    "Language Number Enter the language number for message broadcasting (i.e. 2 for English)" (p390)
    "The file name is 'twenty'. The memo is 'vg2721'." (p363，2720 的文件名也是 twenty，p362)
  summary: |
    三处口径并存：c08 章语言 #1=英文/#2=法文；EWT 章与 518 章语言 #2=英文。说明语言索引与语种的
    对应取决于库配置而非固定映射，照抄会录错语言槽。另有 2720 与 2721 的文件名都写 twenty 的排版
    错误（2721 应另有其名）。多语言部署前必须先核对目标库的语言编号表。
  conditions: 多语言指南录制、跨章复用步骤
  tags: [doc-error, language-index, voice-guides]

- id: n17
  title: EWT 章自述"四条语音消息"实际只有三条
  type: doc-error
  source_pages: p359-360
  source_chapter: Expected Waiting Time / Implementation
  source_quote: |
    "Four voice messages are required for the expected waiting time management: • Voice guide 720:…
    • Voice guide 721:… • Voice guide 722:…" (p359)
  summary: |
    Implementation 写"需要四条语音消息"，下文只列 720/721/722 三条，实验也只建三个。属原书笔误
    （推断：初稿多规划了一条阈值）。按三条执行即可。
  conditions: 重建 EWT 实验
  tags: [doc-error, ewt, count]

- id: n18
  title: 统计 pilot 问候指南填的是"消息号"而非"指南号"
  type: doc-error
  source_pages: p562
  source_chapter: Statistics Pilots / 7 Voice Guide assignment to Statistic Pilot
  source_quote: |
    "Setup the Presentation guides settings for Normal status. … Guide n° Enter the guide number
    (i.e. 2701)." (p562)
  summary: |
    前文建的指南号是 701（消息 1701/2701），此步字段名 Guide n° 却填 2701（消息号）。两种可能：
    该界面实际吃消息号，或原书笔误（推断：按实验截图照填 2701 能工作，说明此处口径就是消息号）。
    在别的界面（pilot 的 Pres.Guide）填的确实是 3 位指南号——同书两种口径并存，现场要两边都试。
  conditions: 配统计 pilot 问候指南
  tags: [doc-error, statistics-pilot, numbering]

- id: n19
  title: 实验环境凭据全公开——培训口径不可带入生产
  type: limitation
  source_pages: p9, p65, p96, p144, p321
  source_chapter: 全书实验值
  source_quote: |
    "mtcl / Superuser2580* / root / Superuser2580* … FLEXLM … root letacla1 … Administrator
    Administrateur superuser" (p9 实例表)
    "Password Enter the default password (i.e. alcatel) … New password Enter a new password (i.e.
    Superuser01*)" (p96)
    "Dial the personal code Enter the personal code (i.e. 0000)" (p144)
    "Enter your password Enter the extension password (i.e. 0000)" (p321)
  summary: |
    全书明文口令（Superuser2580*、alcatel、letacla1、Superuser01*、0000、pbxP/alcatel）均为实验
    口径；生产系统必须全部替换，且 Excel 表单保护密码默认 alcatel（p502）也要改。任何由本书生成
    的操作指引都要带"实验口径"标注并强制改密步骤。
  conditions: 一切生产化复用
  tags: [limitation, credentials, lab-only, security]

- id: n20
  title: CCS 无权创建 CCD 对象——权责边界不是故障
  type: limitation
  source_pages: p79, p84
  source_chapter: CCS APPLICATION OVERVIEW / Main functions
  source_quote: |
    "A CCS station cannot create any object relative to call distribution (trunk groups, pilots,
    queues, processing groups, agents, wall-mounted displays), but can create CCS supervisors and
    distribution rules." (p79)
  summary: |
    CCS 班长站管不了底层对象：中继组、pilot、队列、处理组、座席对象、壁挂显示屏都只能在 OXE 管理
    侧建。CCS 里"找不到建 pilot 的入口"是设计而非缺陷。CCS 能做的例外只有两件：CCS 班长账号与
    分配规则。
  conditions: 权限划分、工单分派
  tags: [limitation, ccs, separation-of-duties]

- id: n21
  title: OXE 侧改 IP/网络参数后 CCS 必须重启才生效
  type: limitation
  source_pages: p95, p505, p518
  source_chapter: CCS installation / Excel parameters / Statistic settings
  source_quote: |
    "The CCS application needs to write the updated values in the file ccs.ini file (call server IP
    address). So you must restart the CCS to consider this and the connection to the server call is
    established." (p95)
    "A restart of the CCS is needed every time a modification is done" (p505)
  summary: |
    三类改动都要求重启 CCS：呼叫服务器 IP 声明（写 ccs.ini）、Excel 参数修改、统计对象数修改。
    "改完没反应"先查有没有重启。
  conditions: CCS 配置变更后
  tags: [limitation, ccs, restart]

- id: n22
  title: 座席退出（withdrawal）可被管理端约束——末座席可禁退、登入即退出、无应答自动退出
  type: limitation
  source_pages: p173-174, p276, p307
  source_chapter: PG 选项与 Unavailable 特性
  source_quote: |
    "Last agent withdrawal authorized If enabled, the last agent of the group has the right to
    withdraw. If not, the last available agent loses this right to preserve the service." (p172)
    "By management • It is possible to inhibit the withdrawal of the last agent available in a PG
    • An agent can be automatically withdrawn when entering in a PG or after a call rotation phase" (p276)
    "Unavailable on no answer Yes: When an extension is rung and the agent is not responding, the
    agent is set automatically in unavailable state at the end of the ring rotation time-out." (p307)
  summary: |
    座席的"退出权"受三个管理项约束：末座席禁退（保服务）、登入即自动退出、振铃超时未接自动转退出。
    座席抱怨"按了退出没反应/一登录就是退出态"，先查 PG 这三个参数，而不是当故障处理。
  conditions: 座席状态异常工单
  tags: [limitation, withdrawal, pg-options]

- id: n23
  title: 班长永远自指派、无优选组——与座席规则不同
  type: limitation
  source_pages: p142, p274
  source_chapter: Supervisor's attachment / Log on/off for supervisor
  source_quote: |
    "It is not possible to declare a preferential group for the supervisor because it is automatically
    self-assigning." (p142)
    "A supervisor is always self-assigning • A supervisor is attached to 1 or several PG(s) by
    management, but has no preferred processing group" (p274)
  summary: |
    给班长配"优选处理组"是无效操作：班长自动自指派、可挂多个组但无优选组概念；登录时手选组。
    照搬座席的固定/优选组配置思路会在班长身上落空。
  conditions: 班长账号配置
  tags: [limitation, supervisor, self-assigning]

- id: n24
  title: 直连 pilot 阻塞态默认播指南 #75，来话一响即断
  type: limitation
  source_pages: p473
  source_chapter: CCD direct calls / 3.4 Call from agent in withdrawal status
  source_quote: |
    "the pilot is blocked and the incoming call follows the direct call pilot configuration which is,
    by default, the voice guide #75." (p473)
    "If you call from MicroSIP – Public softphone to DID number of Agent1, you should hear a tone and
    the call is released." (p473)
  summary: |
    座席不可用时打座席号，来话进 direct call pilot 的阻塞分支，默认只播指南 #75（一声提示音）后
    释放——客户体验差且容易被当成"打不通"故障。生产上应像实验那样显式配置阻塞指南（如 685）或
    关闭地址。
  conditions: direct call pilot 上线前
  tags: [limitation, direct-calls, blocked, default-guide]

- id: n25
  title: Show Supervisor Listening 法国/德国默认关闭——旁听无提示不违法但易投诉
  type: version-trap
  source_pages: p315
  source_chapter: Agent and supervisor features / 3.2 Discrete listening
  source_quote: |
    "Listen The supervisor listens to the conversation between the external person and the agent. He
    is not involved. Agent is notified on his set by a message 'supervisor listening' if the parameter
    Show Supervisor Listening is set to 'True' (default=False in France and Germany)" (p315)
  summary: |
    旁听时座席话机是否显示"supervisor listening"取决于 Show Supervisor Listening 参数，法国/德国
    目标库默认 False。跨国部署时同一动作在不同国家的座席感知不同；合规要求提示旁听的市场要把参数
    打开（是否本地法规强制，书外确认）。
  conditions: 多国库部署、监听合规
  tags: [version-trap, monitoring, compliance, country-default]

- id: n26
  title: Recordable Voice Guides 在法语库默认关闭
  type: version-trap
  source_pages: p218
  source_chapter: Voice guides management by the set / 1.6
  source_quote: |
    "Recordable Voice Guides Enable the facility (i.e. 1) In french database, such parameter is
    disabled by default." (p218)
  summary: |
    拨 401 录音前必须先在 COS 的 PCX SERVICES 启用 Recordable Voice Guides；法语目标库默认是关的。
    不启用时话机录音流程走不通，易误判为话机或前缀问题。
  conditions: 话机录音前、法语库部署
  tags: [version-trap, cos, recording, french-database]

- id: n27
  title: 518 与 538 为系统预置指南，不可创建/修改（法国库）
  type: limitation
  source_pages: p389, p574, p379
  source_chapter: Waiting queue position guide / Agent welcome guide
  source_quote: |
    "Here is the voice guide 518 parameters with the CCD waiting queue position function. Do not
    change." (p389)
    "The voice guide #538 puts into service the agent welcome guide feature … It's not necessary
    neither to create nor to modify (in database France)." (p574)
    "The messages numbers are already created in the OXE (from 3226 to 4217)" (p379)
  summary: |
    位置指南 518、欢迎指南机制指南 538 及其消息段（3226-4217）都是预置资源：只做参数核对、语言与
    消息录制，不许删建改号。自己另建同号指南会破坏机制。
  conditions: 位置/欢迎指南部署
  tags: [limitation, preset-guides, 518, 538]

- id: n28
  title: 座席欢迎指南上限：每座席 5 条消息、消息池 4500-5999 共 1500
  type: limitation
  source_pages: p568, p575
  source_chapter: CCD AGENT WELCOME GUIDE
  source_quote: |
    "a range of 1500 voice messages is reserved [4500-5999] … The voice message assigned to the agent
    can contain up to 5 files maximum (5 different « sub-messages » for each agent are available)." (p568)
    "Agent can record a maximum of 5 prompts." (p575)
  summary: |
    两个硬顶：每座席最多 5 个欢迎文件（切换早晚/场景版本用）；全系统欢迎消息池 4500-5999 共 1500
    条——超大座席规模时按座席数预留，超出需要另想办法（书外）。
  conditions: 大型呼叫中心规划
  tags: [limitation, welcome-guide, capacity]

- id: n29
  title: 中继组实时数据依赖 CSTA-Monitored 开关
  type: limitation
  source_pages: p414, p438
  source_chapter: REAL TIME - TRUNK GROUPS / Real time how-to
  source_quote: |
    "CSTA-Monitored must be set to « yes » in the OXE to display values for the trunk group" (p414)
  summary: |
    中继组实时视窗无数据时先查 OXE 侧 Trunk Group 的 CSTA-Monitored 是否 YES（实验中继组
    1-T2-SIP PUBLIC 要手工打开）。不开开关时其余实时视图正常、唯独中继组空白，排障方向容易跑偏。
  conditions: 中继组实时监控排障
  tags: [limitation, csta, trunk-group, real-time]

- id: n30
  title: EWT 测试受 TSP 制约，存在滞后
  type: limitation
  source_pages: p373, p192
  source_chapter: Expected Waiting Time / 5.3 test
  source_quote: |
    "Pay attention, the tests depend on the TSP (Traffic Sampling Period) of the waiting queue. So,
    expect some lag while testing." (p373)
    "The more the period is short more it reacts quickly." (p192)
  summary: |
    EWT 是按队列 TSP 滚动估计的，测试时播报阈值切换有滞后；TSP 越短反应越快但要靠"逐步调参+观察
    告警"校准。验证 EWT 阈值别用单通呼叫下结论。
  conditions: EWT 上线验收
  tags: [limitation, ewt, tsp, testing]

- id: n31
  title: 欢迎指南不在 CCD direct calls 上播放
  type: limitation
  source_pages: p567
  source_chapter: CCD AGENT WELCOME GUIDE
  source_quote: |
    "When an agent set receives an external call, an agent welcome guide can be broadcast when the
    agent off hooks • No welcome guide on CCD direct calls" (p567)
  summary: |
    欢迎指南只对经 pilot/队列进来的 CCD 来话生效；direct call pilot 直达座席的来话一律不播。期望
    "所有来话都有个性化问候"的方案要把 direct call 流量也算进去重新设计。
  conditions: 欢迎指南方案设计
  tags: [limitation, welcome-guide, direct-calls]

- id: n32
  title: 518 位次播报上限 100、超限播提示音、语言缺失回退链
  type: limitation
  source_pages: p376, p382-383
  source_chapter: "CCD WAITING QUEUE POSITION" VOICE GUIDE / RESTRICTION
  source_quote: |
    "Broadcast limit: • It is possible to specify a position beyond which the guide will no longer be
    broadcast to the caller (maximum value:100) … When it is higher, the inter-guide tone of the pilot
    is broadcast to the caller until the call switches to a position below the managed value" (p382)
    "If the call uses a language not managed for the voice guide, the system uses the default language
    • If no default language has been defined, the voice guide is not broadcast." (p383)
  summary: |
    三个体验边界：位次播报最大 100，超限只听 pilot 提示音；呼叫语言不在指南语言集内时回退默认语言，
    连默认语言都没配则整段不播（跳下一级）；语言在集内但子消息缺失播备份音。排队风暴时高位的呼叫
    体验是"无限提示音"，需在话务设计时接受或另配安抚指南。
  conditions: 排队高峰、多语言站点
  tags: [limitation, position-guide, language-fallback]

- id: n33
  title: 统计 pilot 问候指南只在路由 pilot"按规则"关闭/阻塞时播放
  type: limitation
  source_pages: p545, p547
  source_chapter: STATISTICS PILOTS
  source_quote: |
    "The presentation voice guide of the statistics pilots for blocked States and general forwarding,
    will be played if: • the routing pilot is in blocked State or general forwarding on rule • this
    rule is valid (at least 1 direction is open and) available)" (p545)
    "That's why the routing pilot has to be closed or blocked on RULE." (p545)
  summary: |
    路由 pilot 按"指南/地址"方式关闭或阻塞时，统计 pilot 的问候指南不播、直接按路由 pilot 的分发走；
    只有"按规则（rule）"关闭/阻塞且规则仍有效（至少一个方向开且可用）才播对应状态问候。统计 pilot
    的三态问候方案必须与路由 pilot 的关闭方式配套设计。
  conditions: 统计 pilot + 分时段问候方案
  tags: [limitation, statistics-pilot, rule]

- id: n34
  title: 向紧急关闭中的 pilot 转移会被拒绝（未配关闭地址时）
  type: limitation
  source_pages: p528
  source_chapter: EMERGENCY CLOSURE
  source_quote: |
    "Transfer to a pilot in emergency closure is only authorized if an emergency closure address has
    been configured and is reachable. Transfer is denied if the address has not been configured" (p528)
  summary: |
    紧急关闭期间，座席向该 pilot 转移来话只有在"关闭地址已配置且可达"时放行；只配了关闭指南没配
    地址的站点，转移一律被拒。应急演练要把"转接被拒"当作预期行为向座席交底。
  conditions: 紧急关闭方案设计与演练
  tags: [limitation, emergency-closure, transfer]

- id: n35
  title: IAA 菜单树三重上限与可打断性
  type: limitation
  source_pages: p356
  source_chapter: INTERACTIVE QUEUING / IAA
  source_quote: |
    "Tree menus: • 5 levels max • 4 choices max per level • 8 trees maxi • When an agent becomes free,
    the caller leaves the IAA menu • The IAA is interruptible" (p356)
  summary: |
    队内 IAA 上限：5 层、每层 4 选项、共 8 棵树——复杂菜单要出队走 CCIVR 外部服务器（书外）。座席
    一空出来电者立即离开 IAA、IAA 播报可被打断，所以 IAA 不适合承载长内容（如完整业务宣讲）。
  conditions: 排队菜单方案
  tags: [limitation, iaa, interactive-queuing]

- id: n36
  title: 事务码摘码窗口最短 1 秒且只有 Business 码进统计
  type: misconception
  source_pages: p343-344, p293, p478
  source_chapter: TRANSACTION CODE
  source_quote: |
    "Transaction Code Dialing Timer … (the unit is 100ms). The minimum value allowed is 10." (p343)
    "Only calls assigned to type codes Business appear in the EXCEL statistics." (p344)
    "the business codes are the codes assigned to the clients. Only the business codes are used
    (coded on 3 digits and limited to 1000)" (p478)
  summary: |
    两个易错：①Timer 单位是 100ms，填 10 才是 10 秒——按"秒"理解填 10 就成了 1 秒，座席来不及摘码；
    ②15 位的事务码只存通话记录不进统计，Excel 统计只认 3 位 Business 码（上限 1000 个）。业务报表
    规划用错码类型会白配。
  conditions: 事务码配置与报表口径
  tags: [misconception, transaction-code, timer, statistics]

- id: n37
  title: "服务水平的计时起点是'听完指南'而非'进队'"
  type: misconception
  source_pages: p168
  source_chapter: Setting up the CCD objects / Service level target
  source_quote: |
    "Duration is counted at the end of listening to the guide, until dropping out of an agent (sum
    queue + ringtone agent)." (p168)
  summary: |
    answered within 的计时从听完问候/停车指南后起算，到座席摘机止（排队+振铃之和）。把"进 pilot 就
    开始计时"的直觉套到 SLA 核算上，数值会与系统统计对不上；指南越长，对外承诺 SLA 越要留余量。
  conditions: SLA 承诺与报表对账
  tags: [misconception, service-level, timing]

- id: n38
  title: wrap-up 计时器归属分家——自动挂 pilot、手动挂 PG
  type: misconception
  source_pages: p277-278, p168, p172
  source_chapter: WRAP UP
  source_quote: |
    "Wrap-up is activated • Either automatically at the end of the processing of each CCD call
    according to the source pilot (management of the 'Automatic Wrap Up Timer' parameter at pilot
    level) • Or manually by the agent … The agent controls his exit from wrap-up in the limit of the
    wrap-up timer defined in the pilot (automatic wrap-up) or in the processing group (manual wrap-up)" (p277-278)
  summary: |
    自动 wrap-up 时长改在 pilot 上（挂机后自动进入），手动 wrap-up 时长改在 PG 上（空闲/暂停态按
    键进入）；在 PG 页找不到"自动 wrap-up"参数、在 pilot 页找不到"手动时长"都属正常。调错对象会
    出现"怎么改都不生效"。
  conditions: wrap-up 调优
  tags: [misconception, wrap-up, pilot, pg]

- id: n39
  title: Rainbow CCD 座席三不与角色限制
  type: limitation
  source_pages: p34-35
  source_chapter: CCD APPLICATION OVERVIEW / CCD agent on Rainbow
  source_quote: |
    "Rainbow user can be used as a CCD Agent (CCD Supervisor not supported)" (p34)
    "ACD set must not be part of any multiset, • It must not be associated to a Rainbow user • DECT
    sets are not supported as ProACD devices" (p35)
  summary: |
    三条硬限制：ACD 话机不能属于任何 multiset、不能关联 Rainbow 用户、DECT 不能作 ProACD 设备；
    Rainbow 侧只有座席没有班长。已有话机要入 Rainbow multiset 的用户不能同时当传统 ACD 座席，
    选型阶段就要排除冲突。
  conditions: Rainbow 远程座席方案
  tags: [limitation, rainbow, ccd-agent, multiset]

- id: n40
  title: 队列阻塞（Blocked）是自动态——全员退出即触发，不需人工
  type: misconception
  source_pages: p26, p28, p229
  source_chapter: CCD Matrix Description / Possible states
  source_quote: |
    "The pilot can be in blocked state • Case: Accidental closure • Cause: Resources missing in the
    downstream processing group" (p26)
    "Blocked • Downstream resources are not guaranteed (All agents are logged-off or in unavailable
    state)" (p28)
  summary: |
    Blocked 不是管理动作而是"下游无资源"的自动结果（pilot 意外关闭）；末座席登出/全员不可用瞬间
    pilot 即 blocked，来话立刻改走阻塞分支（专用指南或规则方向）。上线第一天最经典的客诉："没动
    任何配置，客户说打不通"——其实是最后一个座席下班了。
  conditions: 排班与值班兜底设计
  tags: [misconception, blocked, pilot, availability]

- id: n41
  title: 进阶域全书外置——CCIVR、ACR、CCA、Soft Panel、多站点、OmniVista
  type: out-of-scope
  source_pages: p21, p29, p160, p204, p524, p38-39
  source_chapter: Overview / Interactive queuing / Annex
  source_quote: |
    "CCD Software integrated into OXE Call Server • Additional options (CCS, CCA, ACR, Soft Panel)" (p21)
    "Recording on a PC and then downloading with CCs • Procedure explained in OTCC901 Advanced
    Training" (p204)
    "Run macro (ACDMacro) Checkbox to run a macro under Excel (Advanced Training)" (p524)
    "The management can be done via mgr or OmniVista 8770" (p160)
    "I.V.R processing group • Connection to the CCivr application" (p29)
  summary: |
    本册边界：CCIVR 外部语音服务器、ACR（高级路由，含语言技能/呼叫档案）、CCA 座席桌面、Soft Panel、
    Excel 宏（ACDMacro）、多站点（Multisite CCS）、OmniVista 8770/mgr 管理路径、ALE Connect 全渠道
    （邮件/聊天/社交）均只点名不展开；话机录音的第四法与宏在 OTCC901 进阶教材。本书生成的能力单元
    不得越界承诺这些域。
  conditions: 能力边界声明、售前承诺
  tags: [out-of-scope, advanced-training, acr, ccivr, cca]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-22）的反例类覆盖率

| task | 任务 | 反例类覆盖 | 对应 id |
|---|---|---|---|
| task-01 实验环境 | 有 | n19（实验凭据口径） |
| task-02 CCD 模型 | 有 | n40（blocked 自动态） |
| task-03 基础矩阵 | 有 | n01、n12、n13（方向默认关、表格缺陷、命令名） |
| task-04 CCS 安装 | 有 | n21（重启）、n10（ccs.ini 手改） |
| task-05 规则创建 | 有 | n01、n02（方向/规则双默认关） |
| task-06 座席班长 | 有 | n22、n23（退出约束、班长自指派） |
| task-07 收尾 POD | 有 | n11（口令矛盾） |
| task-08 ABC-F | 有 | n03、n04、n09（同节点不同网、direct call 禁用、R100 陷阱） |
| task-09 对象调优 | 有 | n38（wrap-up 归属） |
| task-10 话机录指南 | 有 | n26（法语库默认关）、n16（语言索引） |
| task-11 .wav 导入 | 有 | n08（SFTP 强制） |
| task-12 特性讲义 | 有 | n39（Rainbow 三不）、n25（旁听提示默认） |
| task-13 特性配置 | 有 | n06（annex 禁做）、n36（码参数） |
| task-14 EWT | 有 | n30（TSP 滞后）、n17（三条/四条笔误） |
| task-15 位置指南 | 有 | n27（518 预置）、n32（上限与回退） |
| task-16 实时告警 | 有 | n29（CSTA 开关） |
| task-17 直接呼叫 | 有 | n04、n24、n31（链路禁用、默认 #75、无欢迎指南） |
| task-18 Excel | 有 | n10、n15、n36、n37（手改 ini、路径、码口径、计时起点） |
| task-19 紧急关闭 | 有 | n05、n34（权限与清理、转移拒绝） |
| task-20 统计 pilot | 有 | n18、n33（消息号口径、rule 条件） |
| task-21 欢迎指南 | 有 | n27、n28、n31（预置 538、5 条上限、direct call 不播） |
| task-22 多语言/日历 | 有 | n07（切换延迟）、n16（语言索引）、n32（回退链） |
| 全局 | 有 | n14（编号笔误合集）、n20（CCS 权责）、n41（书外边界） |

说明：原书显式 Warning 5 处（p117、p162、p346、p469、p542）全部收录（n01/n03/n06/n04/n05）；doc-error 类 8 条（n11-n18）均为逐页比对发现的排版/口径缺陷，引用处已给出对照页码。
