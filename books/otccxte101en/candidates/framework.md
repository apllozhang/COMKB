# 框架/流程/结构候选 — OmniTouch Contact Center Standard · Advanced (OTCCXTE101EN Ed07)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：课程推进逻辑、端到端流程、操作菜单路径、组件关系图示、平台/界面分区。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进主线——环境基线 → ACR 高级路由主线 → 网络互助 → 增值工具域
  type: flow
  source_pages: p1-2, p3-597
  source_chapter: 全书目录结构（TRAINING LAB / CCD PRECONFIGURATION / ACR 系列讲义与 How-To / IN NETWORK / SOFT PANEL MANAGER / SPECIAL FEATURES / CCS SERVER / 评估）
  source_quote: |
    "OmniTouch Contact Center Standard Edition - R10.15 ADVANCED - EDITION 07 PARTICIPANT'S GUIDE" (p1)
    讲义模块均以 "Upon completion this module, you will be able to…" 开篇（p64、p80、p95、p117、p294、p317、p556 等），
    How-To 章均以 "How to ✓ …" + Contents 开篇（p39、p48、p130、p182、p204、p209、p235、p260、p338、p396、p455、p491、p516、p544、p580）
  summary: |
    课程按"成对结构"推进：每个能力域先讲义（对象模型+数值边界）后 How-To（精确菜单路径+行为验证）。主线四段：①环境与
    基线（RLAB POD、SIP 模拟器、CCD 预配置概览、CCS 安装、POD 定稿）；②ACR 主线（引言→运行原理→CCS 集成→对象管理
    讲义+实验→ISM 算法→脚本编辑器→调试器→重选→LCA 规则，五组讲义+实验递进）；③网络化（互助讲义→Remote PG 讲义+
    实验）；④增值域（Soft Panel Manager 三模块、CCTA、特殊功能、Excel 定制、CCS Server，各讲义+实验）。收尾是在线评估。
    这是实际交付项目的推荐实施顺序，实验依赖链为 CCS 安装 → POD 定稿 → ACR 管理 → ISM 脚本 → 重选/调试 → LCA → Remote PG。
  conditions: 无版本前提；Advanced 级课程，假设学员已完成 Standard 基础课程
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: RLAB 实验 POD 拓扑与实例账号表——OXE 双节点 + Windows 族
  type: diagram
  source_pages: p7, p9
  source_chapter: TRAINING LAB ENVIRONMENT / TRAINING PLATFORM & POD INSTANCES MANAGEMENT
  source_quote: |
    "OXE_LOCAL_NODE Phys: 192.168.1.1 Main: 192.168.1.3 … OXE_REMOTE_NODE Phys: 192.168.1.101 Main: 192.168.1.103 …
    External gateway 10.20.30.254 Internal gateway 192.168.1.254 … FlexLM Server Phys: 192.168.1.80 … Internal DNS
    192.168.1.250 … SIP simulator 12.0.0.2 External DNS 10.20.30.250" (p7)
    "OXE CS1 OTCC_OXE_LOCAL_NODE … mtcl / swinst / root … Superuser2580* … FLEXLM SERVER OTCC_FLEXLM Flex 192.168.1.80
    … root letacla1 … PC CLIENT 10 OTCC_PC_CLIENT_10 client10 192.168.1.10 … IPDSP 31000 … WINDOWS SERVER
    OTCC_WINDOWS_SRV 192.168.1.70 … CCS Server application" (p9)
  summary: |
    每个 POD 含：OXE 本地节点（cs1 物理 192.168.1.1 / 主 192.168.1.3）、OXE 远程节点（cs2 192.168.1.101 / 主
    192.168.1.103）、两块 OMS（本地 192.168.1.13 / 远程 192.168.1.113）、FlexLM 许可服务器（192.168.1.80，root/
    letacla1）、两台客户端 PC（client10 192.168.1.10、client11 192.168.1.11，Administrator/superuser）、一台
    Windows Server（192.168.1.70，装 CCS Server 应用）。网关：内 192.168.1.254 / 外 10.20.30.254；DNS：内
    192.168.1.250 / 外 10.20.30.250。管理账号 mtcl/Superuser2580*、root/Superuser2580*（实验口径）。本地/远程节点
    间为 Direct IP Link，是后续 Remote PG 实验的物理底座。
  conditions: 实验口径（RLAB 专用）；POD 间相互独立，公共 Pod 提供 NAS 与 SIP 模拟器
  tags: [diagram, lab, topology, rlab]

- id: f03
  title: 客户端软话机布局与双接入通道——MicroSIP/IPDSP 分工 + Console/RDP
  type: structure
  source_pages: p10-13, p60-62
  source_chapter: CLIENT PC 10/11 & POD INSTANCES ACCESS & Remote Desktop Connection
  source_quote: |
    "3 MicroSIP softphones installed • MicroSIP – 31010 for internal calls • MicroSIP – 31011 for internal calls •
    MicroSIP – Public for public calls • 1 IP Desktop Softphone installed • 31000 terminal dedicated for agents" (p10)
    "Console mode … Audio resources disabled in this access mode / Remote Desktop Connection from Windows … Based on
    Guacamole session • Mandatory to be used on labs to share audio resources required for softphones applications." (p13)
    "The fact to open an RDP session of Client PC 11 instance from the RDP session of Client PC 10 allows you to have
    in one screen, all softphones required for the lab." (p62)
  summary: |
    Client PC 10 装 3 个 MicroSIP（31010、31011 内部分机 + Public 公网用户，SIP 密码 123456 实验口径）+ 1 个 IPDSP
    软话机（31000，坐席终端，个人码 0000）；Client PC 11 装 1 个 IPDSP（31001 或 32000）。接入两通道：Console mode
    （Guacamole，无音频，用于 PCX/Windows 实例管理）与 Windows 远程桌面（共享软话机音频，实验必用）。技巧：从 PC10 的
    RDP 会话内再开一条到 PC11（192.168.1.11）的 RDP，远程音频选"在本机播放/录音"，单屏容纳全部软话机，避免来回切换。
  conditions: 实验口径；音频资源必须经 RDP 通道
  tags: [structure, lab, softphone, rdp]

- id: f04
  title: ITSP1 公共 SIP 运营商模拟器——拓扑、账号与号码变换规则
  type: diagram
  source_pages: p16-17
  source_chapter: PUBLIC SIP CARRIER SIMULATOR / SIP CARRIER OVERVIEW & EXTERNAL CALLS
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 … ITSP1 Public gateway public.itsp1.com 10.20.30.50 … SIP
    domain: sip.itsp1.fr SIP domain: itsp1.fr … Id: pbxP password: alcatel" (p16)
    "PBX installation nb 3321PN … DDI table - First external nb 41000 … DDI table – First internal nb 31000 …
    Example: 31002's external nb 3321PN41002 … Dialed number: 0210341002 or 33210341002 … Number sent by the PBX:
    +33210341002" (p17)
  summary: |
    模拟器驻留 RLAB 公共区：SIP 网关 gateway1.itsp1.com（10.20.30.51，PBX 以 pbxP/alcatel 注册，P=POD 号，SIP 域
    sip.itsp1.fr）+ 公网网关 public.itsp1.com（10.20.30.50，模拟公网用户）。号码体系：安装号 3321PN（如 POD3=
    332103），DDI 首外号 41000、首内号 31000；分机 31002 的外号=3321PN41002；外呼拨 0210341002 或 33210341002，PBX
    送出 +33210341002 形成外呼环回。OXE 侧对应配置见 f08（外部 SIP 网关注册 ID pbxN、DID 翻译首外号 33210N41000）。
  conditions: 实验口径（教学专用）；号码规则不可套用于生产
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f05
  title: CCD 预配置基线总览——矩阵、双 Pilot、坐席体系与本地 ABC-F 链路
  type: structure
  source_pages: p19-38
  source_chapter: CCD PRECONFIGURATION OVERVIEW
  source_quote: |
    "✓ CCD matrix description ✓ Pilot1 characteristics ✓ Pilot2 characteristics ✓ ACD-authorized-sets, agents and
    supervisor ✓ Local hybrid ABC-F link" (p20)
    "OXE instances used for this training are already configured (Database and Linux Data), such as: ­ Software
    licenses are restored. ­ Direct IP Link between OXE local and OXE remote nodes is setup. … ­ Public SIP trunk
    group is created." (p50)
  summary: |
    实验起点基线：CCD 矩阵已含 Pilot1（31600）/Pilot2（31601）两路完整配置（Pilot configuration / Call routing
    settings / Voice guides management / Call distribution 各一页展示）；ACD 授权话机、坐席（31500 自助登录型、
    31501 非自助登录型）与班长已在 Call Server 与 CCS 两侧配好；本地混合 ABC-F 链路完成；两路 Pilot 语音引导已下载。
    POD 定稿 How-To 在此基础上补齐：用户/软话机启用、坐席登录、外部 SIP 网关注册、DID 翻译、外/内呼入测试。理解点：
    Advanced 全部实验都跑在这套基线之上，Matrix 里默认已有 Normal_WQ、Overflow_WQ、Redirection_WQ、Forwarding_PG、
    Voice_guide_PG 等对象（p148 可从隐藏清单反推）。
  conditions: 讲义级概览（截图为主）；对象号段 31xxx 为实验口径
  tags: [structure, ccd, baseline, pilot]

- id: f06
  title: CCsupervision（CCS）软件安装流程——从 NAS 解包到装后重启
  type: flow
  source_pages: p39-43, p349-352
  source_chapter: CCS software installation and set up / 1 CCS software installation（Remote PG 实验章内重复出现同一流程）
  source_quote: |
    "Install the CCS application software, available from the NAS drive." (p40)
    "On Feature level window, select Full for a full CCS version installation. … On Feature level license window,
    select Monosite. … On Setup type window, select Windows standalone as the product installation type. … On Real
    Time Information when logged-off? Window, click on Yes … On ASM Script Editor window, click on No to disable ASM
    script Editor package installation." (p42-43)
  summary: |
    安装八步：①从 OTCC_NAS 拷贝 CCS 软件到 Documents；②解压（More info → Run anyway）；③右键 CCS.msi 安装；④License
    勾选接受；⑤Destination Folder 默认路径；⑥Feature level=Full、许可=Monosite、Excel=Yes（高级统计报表）、位置默认、
    语言 English+French → 界面语言 English、安装类型=Windows standalone、用户文件默认路径、Station ID 核对计算机名、
    登出实时信息=Yes、ASM Script Editor=No（本章不装，p204 有专用安装章）、复查并 Install；⑦ccs.ini 合并提示点 OK；
    ⑧Finish。同一安装流程在 Client11（Remote PG 实验 p349-352）逐字重复，可作为标准 SOP。
  conditions: 密码策略——首次登录 administrator/alcatel 后强制改密（如 Superuser01*，实验口径）
  tags: [flow, installation, ccs, windows]

- id: f07
  title: CCS 声明 OXE 与 Navigator 连通验证——ccs.ini 写入后必须重启
  type: flow
  source_pages: p44-47, p353-354
  source_chapter: CCS software installation and set up / 2 OXE declaration on CCS & 3 Test the CCS with Navigator
  source_quote: |
    "From the main menu, select Window > Customise… From Network menu, select node1 and click on Modify … Manage the
    IP settings on Direct access menu … Master PABX name Enter the IP address of the Call Server (i.e. 192.168.1.3)" (p44-45)
    "The CCS application needs to write the updated values in the file ccs.ini file (call server IP address). So you
    must restart the CCS to consider this and the connection to the server call is established." (p45)
    "From the CCS main menu, select Real time > Navigator. You now view the OXE CCD array with the CCS application." (p47)
  summary: |
    声明路径：Window > Customise… → Network 菜单 → node1 → Modify → Direct access 页：勾选 Connected at start up
    （启动即连）、Direct connection（CCS 直连 AFE/CCD 程序）、Master PABX name 填 Call Server IP（实验口径
    192.168.1.3，远程节点则为 192.168.1.103）→ OK → 确认修改 Yes → 提示重启 OK → 关闭 CCS 再启动。登录
    administrator/alcatel，强制改密（大写+数字+特殊字符规则），重新登录后 Real time > Navigator 打开即见 CCD 矩阵
    全景，验证连通。ccs.ini 是配置落盘文件，改完不重启不生效——这是 CCS 类排障的第一检查点。
  conditions: 适用任意 CCS 客户端首次接入（含 Remote PG 实验的 Client11）
  tags: [flow, ccs, oxe-declaration, navigator, ccs-ini]

- id: f08
  title: POD 定稿四件套——SIP 扩展用户、外部 SIP 网关注册、DID 翻译、呼入验证
  type: flow
  source_pages: p51-59
  source_chapter: Finalizing the pod configuration / 2 POD set up
  source_quote: |
    "From the main menu, select SIP> SIP Ext. Gateway. … Registration ID pbxN (where N is your POD number) … Outgoing
    username pbxN" (p56)
    "According to your POD number, configure the DID translator as follow: ­ First external number: 33210N41000 ­
    First internal number: 31000 ­ Range size 1000. Translator/External Numbering Plan/Default DID num. translator" (p57)
    "Call Pilot1 from Public user by dialing 0210X41600. … When Agent1 hangs up, automatic wrap-up status is applied
    to the agent." (p58)
  summary: |
    定稿流程：①OXE WBM（https://192.168.1.3，mtcl）核对用户 31010/31011（Local SIP SIP extension），MicroSIP 上线，
    Public 用户选 Public POD X profile；②坐席登录——31000/0000 注册后 IPDSP 菜单 LogOn：31500 自助型点 List 选
    Agent_PG，31501 非自助型直接输坐席号登录到偏好组；③外部 SIP 网关：SIP > SIP Ext. Gateway 按 POD 号改两参数
    （Registration ID=pbxN、Outgoing username=pbxN）；④DID 翻译：Translator > External Numbering Plan > Default DID
    num. translator 新建（首外号 33210N41000、首内号 31000、范围 1000）；⑤验证——Public 软话机拨 0210X41600（Pilot1）、
    0210X41601（Pilot2），31010 内部拨 31600/31601，坐席接听挂机后自动进入 wrap-up 状态即通过；⑥嵌套 RDP 布局（f03）。
  conditions: 实验口径；机架核对（主 OMS Rack4 GD4 192.168.1.13 / 远端 Rack3 GD4 192.168.1.113，p51）
  tags: [flow, pod-setup, sip-gateway, did, lab]

- id: f09
  title: ASM 架构——AFE、ASM 服务器、脚本编辑器三角色
  type: diagram
  source_pages: p68-70
  source_chapter: AGENT SELECTION MODUL PRINCIPLE (ASM) / Architecture
  source_quote: |
    "Call Handling (MAO) — Alcatel Front End Server — ASM Server — Script … Script Editor (ASM Client) … Execution
    writing / activation … The ASM Server can be internal (running on OXE) or external (running on Windows PC)" (p68)
    "The ASM script editor is in charge of writing and loading of a script … The ASM server is in charge of • Script
    interpretation • Data base queries • Update of data base • Calculation of the agent list according to • Agents
    configuration • Script rules • Call profile" (p69)
    "Script Interpreted Pseudo code (Unix/Windows) … (*.scr files) (*.alb files) … ASM compilation" (p70)
  summary: |
    ACR 运行时三角色：①AFE（Alcatel Front End，CCD 程序）接收呼叫处理请求并转发给 ASM；②ASM 服务器（内置 OXE 或外置
    Windows）负责脚本解释、数据库查询/更新、按坐席配置+脚本规则+呼叫档案计算坐席列表；③ASM 脚本编辑器（CCS 内嵌的
    ASM Client）负责编写与装载脚本。脚本为解释执行的伪代码（Unix/Windows），源文件 .scr、编译产物 .alb；内置 ASM 场景
    由 Call Server 上的 alb（Agent List Builder）进程承载，脚本存于 /usr3/afe。一个 Pilot 一个脚本，或全 Pilot 公共脚本。
  conditions: ASM external 模式细节本教材未展开
  tags: [diagram, architecture, asm, afe, alb]

- id: f10
  title: ACR 呼叫分发三步——特征化 → 生成动态组 → 等待室分配
  type: diagram
  source_pages: p71-75
  source_chapter: DISTRIBUTION PRINCIPLES & CALL CHARACTERIZATION
  source_quote: |
    "1. Characterization of the call and association of a profile to the call, distribution of the call towards a
    pilot 2. Drawing up of a list of agents suitable to process the call according to the rule of the selection of the
    agent 3. Recovering of the list of agents transmitted by the ASM unit and call distribution to the agents" (p71)
    "Waiting Rooms are needed in ACR & don't work in FIFO mode … Waiting Room & Waiting Queue CANNOT be open at the
    same time" (p71-72)
    "CLID: Caller Line Number / Calling Number • NDI: Called Line Number (for Direct ACD Call) • Dialed Number • Call
    Tag • CSTA filed for call identification • Call Profile (List of attributes) • Required skills to handle the call
    (up to 7)" (p74)
  summary: |
    三步模型：①呼叫特征化并关联档案，路由到 ACR Pilot（可用信息：CLID、NDI、被叫号码、呼叫标签、CSTA 字段、呼叫档案
    ——档案最多 7 项技能属性，另有呼叫类型 Direct Call/Audio/Fax/e-mail）；②ASM 按规则算法产出坐席列表（动态组）；
    ③呼叫携列表进等待室等待分配。等待室不 FIFO、与等待队列不能在同一规则同时打开、动态组下游无资源选择优先级。ISM
    示例流（p73）：档案→ACR Pilot→ASM 按技能搜索→返回动态组→呼叫带列表进等待室。呼叫特征亦可来自脚本内数据库查询
    （按 CLID/Call Tag/坐席号查名称、档案、授权名单、优先级，p76）。
  conditions: 特征化入口（IVR 打 call tag、转接携带）以图示给出
  tags: [diagram, acr, routing, call-profile, waiting-room]

- id: f11
  title: ACR 容量上限表（Provisioning Level）
  type: structure
  source_pages: p77
  source_chapter: ACR INTRODUCTION / ACR LIMITS
  source_quote: |
    "Statistic Pilot: 3000 • Pilot: 600 • Queues & Waiting Rooms: 600 • Groups: 450 • Directions between Pilot and
    Queues: 30 • Directions between Queues and Processing Groups: 50 • Domains: 20 • Skills: 1000 • Characteristics
    List: 1000 • Characteristics (per call profile/ per Agent / max): 7 / 50 / 20000 • Authorized List (max number of
    agents): 30 • Unauthorized List (max number of agents): 30. For more Information check the Feature List" (p77)
  summary: |
    ACR 对象硬上限：统计 Pilot 3000、Pilot 600、队列与等待室 600、组 450、Pilot→队列方向 30、队列→处理组方向 50、
    域 20、技能 1000、特征清单 1000、特征数（每呼叫档案/每坐席/系统最大）7/50/20000、授权名单 30 坐席、非授权名单
    30 坐席。规划时先对照此表，超限需求要看 Feature List（书中指针）。与 p394 SPM 限制（订阅统计 500/连接 150/面板
    200）共同构成容量合规两表。
  conditions: R10.15 时代口径；新版以 Feature List 为准
  tags: [structure, capacity, limits, acr]

- id: f12
  title: ACR Pilot 路由规则与等待室行为矩阵——互斥、饱和、同优先级、门限
  type: diagram
  source_pages: p81-92
  source_chapter: ACR FUNCTIONING PRINCIPLE / ROUTING PRINCIPLES & CALL FLOW
  source_quote: |
    "A pilot is declared ACR when: • One of its direction is a waiting room • Active pilot rule is applied …
    Saturation if EWT > Maximum Waiting time of waiting room" (p81)
    "Greeting guide + 6 parking levels … Up to the 40 languages in the Alcatel-Lucent OmniPCX Enterprise … For each
    Waiting Rooms parking levels, it's possible to use: EWT tables / Address (IAA) / Voice guide / Interactive
    Queuing with IAA" (p82)
    "It is not possible to open in a rule a waiting queue and a waiting room at the same time" (p85)
    "EWT > MWT => the waiting room is congested so another direction is selected … Directions with same priority •
    Lowest expected waiting time" (p86-87)
  summary: |
    行为矩阵五条：①Pilot 含等待室方向或挂了激活的 Pilot 规则即为 ACR Pilot；②规则里等待队列与等待室互斥（Rule0 开
    WR 则 Rule1 才能开 WQ）；③饱和判定 EWT>最大等待时间 → 选其他方向；④同优先级方向按最小 EWT 选择；⑤等待室下游
    生成按呼叫档案的动态组，故无资源选择优先级管理；坐席视角——无档案坐席只能服务等待队列，有档案坐席可服务两者
    （p89）；呼叫选择看优先级差、最大真实等待时间与分布门限（p90-92）。语音引导=迎宾+6 泊位，支持 OXE 40 种语言、
    EWT 表、IAA 地址、交互排队。
  conditions: 图例（P0/P1 优先级、EWT 数值）为讲义示意
  tags: [diagram, routing, waiting-room, ewt, priority]

- id: f13
  title: CCS 侧 ACR 集成——权限、技能矩阵、统计与实时视图分区
  type: structure
  source_pages: p96-114
  source_chapter: CCSUPERVISION & ACR
  source_quote: |
    "During the CCs software installation, the ASM script editor component must be selected. This allows to manage ACR
    scripts according to the CCs supervisor's rights" (p97)
    "Administrator: has all rights • Supervisor: rights have to be granted • ACR rights for the supervisor •
    Configurations/ Advanced Call Routing • Configurations/ Advanced Call Routing /ACR Data" (p99-101)
    "Configurations/ Agent • Up to 50 skills per agent • Copy and paste skills … Skills matrix • Easier to manage •
    Quicker to manage … Export / import agent skills (assigned skills, skill levels..)" (p102-107)
    "Real time/ Filter (choose ISM filter) … Real time/ Queue and Waiting Room/ Calls in WR … Real time/ Processing
    Group/ PG Agents/IVR/Team • ACR icon … Real time/ Agent • ACR icon is automatically displayed (for an ACR call)" (p109-114)
  summary: |
    CCS 五个 ACR 相关分区：①安装选项——ASM script editor 组件决定能否管脚本（独立安装章见 c05）；②权限——
    Configurations/Supervisor rights 给班长开通 Advanced Call Routing 与 /ACR Data 两项；③坐席技能——
    Configurations/Agent 每坐席最多 50 技能，支持复制粘贴、技能矩阵批量管理、导出/导入；④统计——Statistics/Last
    received calls 按 Pilots/Filters/Groups/Queues/Agents/Hyper objects/Teams 维度 + Excel 模板（Filter/Filters
    summary/Agent per Filter）；⑤实时——Real time/Filter（ISM 过滤器、表格/图形双态）、Queue and Waiting Room/Calls
    in WR（悬停出明细）、Processing Group/PG Agents/IVR/Team 的 ACR 图标、Agent 视图自动显示 ACR 呼叫图标。
  conditions: 班长需 ACR 权限才能看到对应菜单
  tags: [structure, ccs, acr, permissions, real-time]

- id: f14
  title: ACR 对象菜单路径全集——OXE WBM 与 CCS 双侧
  type: menu
  source_pages: p119-126, p134-158
  source_chapter: ACR Management（讲义 + How-To）
  source_quote: |
    "Applications/CCD/Queue • Directory Number: 31703 • Name: WaitingRoom1 • Type + Waiting room • Distribution
    direction 0: 31320 … • Max Waiting Time: 3000 … Ringing Supervision Directory No." (p119)
    "Applications/CCD/Skill/Skill Domain • Skill domain number: 2 • Name: Insurance • Preference: 1 …
    Applications/CCD/Skill/Skill parameters • Skill nb: 100 • Skill domain number: 2 • Name: Car …
    Applications/CCD/Skill/Call profile • Call profile number: 0 … Expertise level: 1 • Mandatory: True • Position: 1" (p120-122)
    "Applications/CCD/Statistics pilot • Pilot Stat. Directory Number: 31650 … Routing pilot: 31600 • Call tag: •
    Call priority: -1 • Call Profile: 0 … Applications/CCD/Operators data management … Manage skills + True" (p123-125)
  summary: |
    OXE WBM（https://192.168.1.3）侧路径：处理组=Applications > Processing Group；等待室=Applications > CCD > Queue
    （Type=Waiting room，方向 0-29，监控定时器/话务采样 5mn/最大等待 3000/振铃监控）；ACR Pilot=Applications > CCD >
    Pilot；统计 Pilot=Applications > CCD > Statistic pilot（挂路由 Pilot、call tag、call priority -1、呼叫档案）；
    技能域/技能/呼叫档案=Applications > CCD > Skill > Skill Domain | Skill parameters | Call profile；坐席数据=
    Applications > CCD > Operators data management（Skill set、Manage skills=True 时坐席可从话机 ACR 主菜单自开关
    技能）。CCS 侧路径见 f13/f16。两侧配合完成一个 ACR 业务对象链。
  conditions: 讲义示例号（31703/31650 等）与 How-To 实际号（31704/31660）不同，均为实验口径
  tags: [menu, oxewbm, acr, objects]

- id: f15
  title: agacd 与 adm_acd 命令树——OXE 侧 ACD 数据维护入口
  type: menu
  source_pages: p127-128, p176, p257-258
  source_chapter: ACR Management / AGACD & ADM_ACD（另见 ISM、LCA 各章维护用法）
  source_quote: |
    "\"agacd\" command: agacd + Agent dir. number" (p127)
    "Command adm_acd … option 2 + 1 for pilots list / 4 for waiting queues list / 5 for statistics pilots … option 3 +
    1 for agent, IVR PG list / 2 for other PG list … option 4 + 1 for agents list (agent + supervisor) / 2 for
    supervisors list (CCs account) … option 5 + 6 for skills and domains list / 7 for call profile list / 8 for
    authorized, unauthorized list / 9 for internal database" (p128)
    "> adm_acd IP@ of ASM server -salb • 21 agent number … Statistics Login duration: 1800 Nb ACD call in: 3 …" (p176)
    "To display dynamic data • adm_acd IP@ of ASM server -salb • option 28 • number: calling number (CLID) • *: to
    list all the calling numbers" (p257)
  summary: |
    命令树三层：①agacd+坐席号——查单个坐席 ACD 数据；②adm_acd（直连 AFE）——option 2 看对象清单（1 Pilot/4 队列/
    5 统计 Pilot）、option 3 看处理组（1 Agent/IVR PG、2 其他 PG）、option 4 看人员（1 坐席+班长、2 CCs 班长账户）、
    option 5 看 ACR 数据（6 技能与域/7 呼叫档案/8 授权与非授权名单/9 内部数据库）、option 11 Dump TERMINALS（连接
    终端）、option 15 软件包/许可清单；③带参分支——adm_acd <ASM IP> -salb（option 21 坐席统计、option 28 ASM 记忆
    动态数据）、adm_acd <CCS Server IP> -servccs（option 10 Dump MailToTerminal，看经服务器接入的客户端）。三处
    IP 缺省均为 localhost（=Call Server 地址）。
  conditions: mtcl 会话下执行；option 编号以 R10.15 为准
  tags: [menu, cli, maintenance, adm-acd]

- id: f16
  title: ACR Management 实验对象创建序列——编号方案与操作顺序
  type: flow
  source_pages: p130-159
  source_chapter: ACR Management (How to)
  source_quote: |
    "Create the processing group Agent2_PG (31803) … Select Applications > Processing Group" (p133)
    "Create the queue WaitingRoom (31704) … Type Enter the type of queue (i.e. Waiting room)" (p134)
    "Create the pilot ACR Pilot (31603) … Create the statistic pilots for ACR Pilot … Statistic pilot 31660 for Car
    insurance ­ Statistic pilot 31661 for Home insurance" (p135-136)
    "The ACR Pilot is blocked. If the Agent does not have any skill, the Waiting Room is blocked !" (p148)
    "As no script is attached to the ACR Pilot, the Waiting Room is not used; the System will try to use another
    Waiting Queue, if possible. As last resort, the ACR Pilot blockage data (Address or Voice Guide) will be used." (p159)
  summary: |
    七步序列（含实验编号，实验口径）：①建处理组 Agent2_PG=31803（WBM）；②建等待室 WaitingRoom=31704；③建 ACR
    Pilot=31603；④建统计 Pilot 31660（Car Insurance）/31661（Home Insurance），路由 Pilot 均指 31603；⑤CCS 配路由
    ——Call Flow mgt > Call Routing 建 Rule_0 并 Apply，Configurations > Pilot 把 WaitingRoom 加进 Call Routing，
    Call Flow mgt > Call Routing Normal 页启用；⑥CCS 配分配——Configurations > Queue and Waiting Room 给 31704 加
    Agent_PG+Agent2_PG，Call Flow mgt > Call Distribution 资源选择页勾通两方向；⑦坐席附加 PG（Configurations >
    Agent，31500 自助、31501 设 Preferred GT Agents=Agent2_PG）后重新登录。验收：Navigator Tab1 全景 / Tab8 定制
    ACR 视图；技能赋给坐席前 WR 阻塞、赋给后 WR 打开变绿；未挂脚本时 WR 不启用，呼叫落到其他队列或 Pilot 闭锁数据。
  conditions: 全部编号为实验口径；依赖 f06/f07/f08 完成
  tags: [flow, acr, lab, sequence]

- id: f17
  title: Navigator 定制视图——Tab 页与对象显隐
  type: menu
  source_pages: p147-148, p237
  source_chapter: ACR Management / 5 Matrix overview（另见 ISM reselection 实验）
  source_quote: |
    "From the main menu, select Real time> Navigator … Click on Navigator customization icon … From the Displayed
    Objects menu, select Tab8 … From Pilots Displayed menu, select Pilot1 and Pilot2 to hide them. … From Queues
    Displayed menu, select Normal_WQ, Overflow_WQ and Redirection_WQ to hide them. … From PGs Displayed menu, select
    Forwarding_PG and Voice_guide_PG to hide them. … Click on Record … Select the tab #8" (p148)
    "On Waiting room queue parameter, setup the Real Time Info parameter with the option #Calls queued." (p237)
  summary: |
    Navigator 支持多 Tab 页：Tab1 默认显示整张 CCD 矩阵；定制入口为 Navigator customization 图标 → Displayed Objects
    选 Tab 号 → 分别从 Pilots/Queues/PGs Displayed 里隐藏无关对象 → Record 保存 → Exit。把 Tab8 只留 ACR Pilot +
    WaitingRoom + 两个坐席 PG 即得"ACR 专用视图"。实时参数可按对象改显示口径（如等待室显示 #Calls queued 排队数）。
  conditions: 视图配置保存在 CCS 客户端侧
  tags: [menu, navigator, real-time, ccs]

- id: f18
  title: 呼叫档案/坐席档案数据模型——域、技能、等级、权重的四层结构
  type: structure
  source_pages: p163-166, p102
  source_chapter: INDIVIDUAL SKILL MAPPING RULE (ISM) / CALL PROFILE & AGENT PROFILE & SKILLS
  source_quote: |
    "A call profile is made up of attributes list • 7 attributes maximum per call profile … Each attribute has got: •
    A characteristic: for agent selection • A domain: family of skills • A component: a skill in the domain • A skill
    level: requested level of the agent or the caller profile" (p163-164)
    "Skills are associated to the agent • Each skill has a level between 1 (low) and 9 (high) … Skills from 0 to 99
    are created by default (predefined languages and media) Maximum of 1000 skills … The domains 0 & 1 are created by
    default (language and media) Maximum of 20 domains" (p165-166)
  summary: |
    四层模型：域（0-19 号，0/1 默认为语言与媒体，最多 20 个，各带权重 1-20）→ 技能（域内 0-999 号，0-99 为预定义
    语言/媒体，最多 1000 个，名称 1-16 字符、缩写 1-4 字符）→ 等级（呼叫档案里是"要求等级"，坐席档案里是"具备等级"
    1 低-9 高，另含激活标志）→ 属性（特征+域+技能+等级+强制/可选，呼叫档案最多 7 项；坐席最多 50 项技能）。CCS 里
    Configurations > Advanced Call Routing > Skill 管域与技能（域 ID 自动分配、权重 1-20），ACR Data 页管呼叫档案。
  conditions: 域与技能在 ABC 网络中会广播（p150）
  tags: [structure, data-model, skill, call-profile]

- id: f19
  title: ISM 子列表降级算法——从满配匹配到全不匹配的 N 级漏斗
  type: flow
  source_pages: p168-172, p184-186
  source_chapter: ISM ALGORITHM & ALGORITHM ISM（含 How-To 手算章）
  source_quote: |
    "Agent must have all the mandatory attributes to process the call • Agents are classified according to the result
    of the ISM algorithm • A Reselection timeout is managed from ASM to find agent from sub-list N to sub-list N-1,
    N-2, ... N-N" (p168)
    "1st sub-list: « N » call attributes: with skill level of agent >= skill level of the call • After the timeout •
    2nd sub-list: « N-1 » call attributes: with skill level of agent >= … • « 1 » call attributes: with skill level of
    agent < skill level of the call" (p169)
    "The size of the agent list is defined by the parameter \"Number of ACR agent buffers\" • Under Application / CCD/
    CCD/RSI system parameters • Number of ACR agent buffers = 20 • The value can be managed between 20 and 400 maxi." (p172)
  summary: |
    算法流：呼叫档案 N 项强制属性 → 第 1 子列表=N 项全满足（坐席等级≥呼叫等级）→ 重选定时不中则降级第 2 子列表
    （N-1 项满足+1 项不满足）→ 依次降到第 N 子列表（N 项全不满足）→ 仍未接续则整体重选，上限 21 次（p245）。同级内
    排序按 Cman 最小（公式见 p01），同分比 Copt，再同分按 PLTR/LIT（p09 相关参数见 principle）。坐席列表长度由
    Application / CCD / CCD / RSI system parameters 的 Number of ACR agent buffers 控制（20-400）。手算全例见
    c04（5 坐席 4 域场景，Sub-List1=Agent4、Agent1，Sub-List2=Agent5）。
  conditions: 重选次数上限 21 为实验观察结论（p214、p245）
  tags: [flow, ism, algorithm, reselection]

- id: f20
  title: ASM Script Editor 入口、工具栏与积木块清单
  type: menu
  source_pages: p189-196
  source_chapter: ASM SCRIPT EDITOR
  source_quote: |
    "Included in the CCs • Configurations/ Advanced Call Routing/ ASM Script Editor • 2 possibilities to create ACR
    scripts • With ASM server connection • ASM/ connection • Without ASM server connection • File/ Add new" (p189)
    "Statement … Rules — If, ISM Rule, Authorized list rule, Unauthorized list rule, Idle Rule, Call Number Rule,
    Redistribution Rule, Redirection Rule, Last Called Agent Rule, IVR Rule … Miscellaneous — Clear the last agent
    list / Interactive queuing / Update Last Called Agent / Display on the agent set … SQL — Connect to an ODBC source
    data base / Request an ODBC source data base / Break Fetch loop / Loop for fetch data / Fetch an SQL request
    result / Set request result" (p192-193)
    "To link 2 blocks, click on the red square and move to join the yellow one. … It is not allowed to have an
    \"Entry\" or an \"Exit\" of a building block open." (p195, p212)
  summary: |
    编辑器入口：CCS → Configurations/Advanced Call Routing/ASM Script Editor；在线模式先 ASM > Connection 填 ASM 服
    务器名/IP（实验=Call Server 192.168.1.3），脚本直接存 ASM 服务器；离线模式 File > Add new 存本地目录，之后导入。
    脚本名限 8 字符。工具栏四组：Statement（取呼叫上下文变量、自动变量、IF）、Rules（ISM/授权名单/非授权名单/Idle/
    呼叫号码/重分发/重定向/最后应答坐席/IVR 共 9+ 类）、Miscellaneous（清最后坐席列表、交互排队、更新 LCA、坐席话机
    显示）、SQL（ODBC 连接/请求/取结果/循环）。图形化编辑：红方块拖到黄方块连线，右键加注释；任何积木块的入口/出口
    不允许悬空，Start-Stop 必须闭合。编译生成 .scr+.alb 两个文件。
  conditions: 独立安装章见 p204-208（专用 asm-se_setup.msi）
  tags: [menu, asm-script-editor, building-blocks]

- id: f21
  title: 脚本生命周期——在线/离线创建 → 编译 → 激活绑定 Pilot
  type: flow
  source_pages: p197-202, p210-213
  source_chapter: ASM SCRIPT EDITOR / COMPILATION & ACTIVATION & OFF-LINE SCRIPT CREATION
  source_quote: |
    "When the script is completed, it must be saved & compiled • 2 files will be generated • \"Script_name\".scr •
    \"Script_name\".alb • The scripts are saved in \"/usr3/afe\" for an internal ASM server (\"alb\" process)" (p198)
    "Script activation • Choose the script to activate • Attach it to an ACR pilot • Note: • 1 script per pilot • The
    same script can be activated on several pilots (pilot selection) • The same script can be activated on all pilots
    (\"common script\" option)" (p199)
    "Scripts will be saved under the selected directory. • To attach it to an ACR pilot, you must export it into the
    ASM server." (p201)
  summary: |
    生命周期五步：①创建（在线 ASM>Connection 后右键远程 ASM > Add new；或离线 File > Add new 存本地）；②图形化编排
    （Rules/Statement 积木块 + 连线 + 属性如 CHARACTERISTICS_LIST、RESELECTION_TIMEOUT）；③保存编译——生成 .scr
    （源）+.alb（可执行）两文件，内置 ASM 存 /usr3/afe；④激活——右键 .scr > Activate…，左侧选目标 Pilot（一 Pilot
    一脚本，或选全部 Pilot 成公共脚本）；⑤离线脚本需先导入 ASM 服务器再激活。调试模式（Debugger）激活流程类似，
    额外弹 Debugger 窗口。参数变更场景（asm_ag_free_duration）另需重启 MAIN_AFE 进程（p219）。
  conditions: 每次替换脚本都要重新激活到 Pilot
  tags: [flow, script, compilation, activation]

- id: f22
  title: 脚本调试器三窗格与四种过滤器——跟踪路由全流程
  type: structure
  source_pages: p221-233
  source_chapter: SCRIPT EDITOR DEBUGGER
  source_quote: |
    "Part1: Script graphic mode window • Provide view of the script • Objects can't be deleted or modified … Part2:
    Console window for script trace • Move the mouse under the script trace to see in which building block the call
    goes through … Part3: Command window • Activation of filters to analyze a call routing" (p224)
    "THIS EXTENSION MUST BE A NORMAL USER, NEITHER AGENT NOR SUPERVISOR." (p225)
    "Calls filtered through CALLING … The calling number must be exactly the number received from the public operator"
    (p226) / "Calls filtered through CALLED … \"Reset filter\" button" (p227) / "Calls filtered through CALLTAG" (p228)
  summary: |
    调试器开法两种（均在 Configurations/Advanced Call Routing/ASM Script Editor 语境下）；三窗格：图形窗（只读展示
    脚本）、控制台窗（脚本轨迹，鼠标悬停联动高亮当前积木块，可双击改脚本保存但新增积木块只能回编辑器）、命令窗（过滤
    器+模拟呼叫）。过滤器四模式：CALLING（主叫号，必须与运营商送来的号码完全一致）、CALLED（被叫号，Reset filter 停止
    跟踪）、CALLTAG、无过滤。Make call 三要素：Node number、Phone number（发起分机——警告：必须是普通用户，不能是坐
    席或班长）、Dialing number；Release call 挂断。轨迹可保存（Save the trace）。实操序列见 c07。
  conditions: 调试器激活脚本时同样要选 Pilot
  tags: [structure, debugger, trace, filter]

- id: f23
  title: LCA 记忆模型与维护命令——ASM 为谁记什么、清到哪里
  type: structure
  source_pages: p248-258
  source_chapter: LAST CALLED AGENT RULE / OVERVIEW & FUNCTIONING & MAINTENANCE
  source_quote: |
    "The system saves in the ASM Module • The caller identification (Phone number and/or call tag) • The node number •
    Last called pilot • Last call date • Last call time" (p251)
    "LAST_CALLED_STATE • 1: the last call has been sent to a dissuaded queue • 2: the last call has been answered • 3:
    … mutual aid queue • 4: … GFW mode • 5: … Blockage mode • 6: … abandoned on waiting • 7: … abandoned on ringing •
    LAST_CALLED_AGENT • The agent who has answered the last time to the caller • LAST_CALLED_PILOT • LAST_CALLED_DATE
    • LAST_CALLED_ELAPSED_TIME" (p253)
    "The ASM memory is emptied when the ASM process is re-started. • MAIN_AFE re-starting has no effect on the ASM
    memory." (p252)
  summary: |
    记忆模型：全量呼叫记录主叫标识（号码/呼叫标签）、节点号、最后 Pilot、日期时间；已接通呼叫另记应答坐席号；未接通
    呼叫记录状态（7 种：1 劝阻队列、2 已应答、3 互助队列、4 GFW、5 闭锁、6 等待中放弃、7 振铃中放弃）。脚本关键字五枚：
    LAST_CALLED_AGENT、LAST_CALLED_PILOT、LAST_CALLED_DATE、LAST_CALLED_ELAPSED_TIME、LAST_CALLED_STATE（书内另一处
    写作 LAST_CALL_ELAPSED_TIME/LAST_CALL_STATE，How-To 用后者，见 n 系列命名差异条目）。维护：adm_acd <ASM IP>
    -salb option 28（输 CLID 查单条，* 列全部，字段含主叫/呼叫次数/最后应答坐席/节点/Pilot/状态/时间）；清理=kill alb
    进程（ps -edf|grep alb → su - → kill -9），MAIN_AFE 重启不影响记忆。脚本范式与验证见 c08。
  conditions: alb 显示 Release 2.6.3、.inialb 参数 StatPeriod 5 / DualTimeOut 200 / NbMaxAgent 200（实验观察，p272）
  tags: [structure, lca, asm-memory, maintenance]

- id: f24
  title: 网络互助双模型与拒收回退表——Blind vs Intelligent mutual aid
  type: diagram
  source_pages: p293-315
  source_chapter: CONTACT CENTER STANDARD EDITION IN NETWORK
  source_quote: |
    "Blind mutual aid • No ABC-F link between ACD nodes • Doesn't transfer ACD information • Pilot's state is unknown
    • On the remote ACD node, calls are handled as new calls" (p295)
    "Intelligent mutual aid is available in the ABC network between two CCdistribution systems • The CCdistribution
    systems do not have to be adjacent • Transit nodes can be: OmniPCX Enterprise with or without CCdistribution •
    Any PABX able to support (transparently) the ABC-F protocol" (p302)
    "Call handling refused on remote node — Rerouting processing group → Local redistribution / General Forwarding
    Address of the local node → General Forwarding Voice Guide of local node / Blocking Address of the local node →
    Blocking Voice Guide of the local node / Overflow in queue → Call remains queued / Overflow on ringing → Local
    redistribution" (p312)
  summary: |
    两模型共用两个对象：互助队列（把呼叫分给重路由/转发处理组）与重路由处理组（把呼叫送到外部直连缩位号或另一
    CCdistribution 的 Pilot；无呼叫选择优先级）。盲互助无 ABC-F，远端当新呼叫处理，本地 Pilot 闭锁/GFWD/拥塞时呼叫走
    本地管理（语音引导/地址）。智能互助经 ABC 链路交换 Pilot 状态、已听语音引导、总等待时间；远端可 REJECT（远端
    Pilot GFWD/闭锁、方向拥塞/闭锁、无空闲时隙），拒收后按上表回退本地。排队溢出呼叫留在原队列等拒收判定；振铃溢出
    15 秒后转远端，失败则本地重分发或播闭锁语音引导（闭锁 VG 强制）。多级链式溢出（35s→15s）与 GFWD/闭锁地址指向远端
    Pilot 的玩法见 p308-313。管理路径四步见 p314（前缀/重路由组/互助队列/分配规则）。
  conditions: 中转节点须透明支持 ABC-F（OXE、A4300M/L）
  tags: [diagram, mutual-aid, abc-f, network]

- id: f25
  title: Remote PG 分布式互助三对象与管理路径——本地/远端分工
  type: structure
  source_pages: p316-336
  source_chapter: REMOTE PG / NETWORK：DISTRIBUTED MUTUAL AID
  source_quote: |
    "Remote PG • Processing Group of the local node, • Has a minimum waiting time threshold (distribution threshold)
    and a resource selection priority but no call selection priority. • Virtual Queue • Single queue serving a
    dedicated pilot on the remote site … The virtual queue is the image of the head of the normal queue … • Dedicated
    Pilot • Remote Pilot is dedicated to one Virtual Queue. • Can only be called by one or more Remote PGs." (p319)
    "Information transferred: • Information on the originating pilot (number, name) • Status of the remote pilot •
    Voice Guides heard on the local node • Real Waiting Time" (p325)
    "Management on the local node • Network prefix creation • Translator/Prefix Plan/Create … • Remote processing
    group creation • Application/CCD/Processing Group/Create • … Type: Remote" (p335)
  summary: |
    三对象关系：Remote PG（本地节点的处理组，Type=Remote，指向远端专用 Pilot；有分布门限+资源选择优先级、无呼叫选择
    优先级）→（经 ABC-F）→ 远端虚拟队列（Type=Virtual，只映射门/队头呼叫特征）→ 专用 Pilot（一个虚拟队列专属，可被
    多个 Remote PG 调用）。约束：一个 Remote PG 可服务多队列；专用 Pilot 只被一个虚拟队列服务；虚拟队列可服务多个专用
    Pilot。传输内容：源 Pilot 号/名、远端 Pilot 状态、本地已听引导、真实等待时间；请求类：资源选择请求/确认/拒绝、呼
    叫选择请求、拥塞、闭锁/开放、暂停/恢复对话。远端班长显示器显示源 Pilot 名与源节点等待时间，呼叫服务（事务码/
    自动 wrap-up/暂停定时）遵循远端 Pilot。Remote PG 闭锁三条件：远端 Pilot GFWD/闭锁、下游方向全闭锁、链路无时隙。
    管理路径：远端建虚拟队列+专用 Pilot+Pilot 规则（Applications/CCD/Queue|Pilot|Pilot Rule Guide|Pilot Rule
    Direction），本地建网络前缀（Translator/Prefix Plan，Prefix Meaning=Network No.，Type=pilot）+Remote PG+分配规
    则。维护命令：config（T2/T0 板状态）、suproutage（节点间链路）、acdsup（mtcl 下查 Remote PG 开闭）、pildstctx
    <Pilot 号>、pgctx <Remote PG 号>、CCS Navigator。
  conditions: 操作序列与验证见 c09
  tags: [structure, remote-pg, virtual-queue, dedicated-pilot]

- id: f26
  title: ABC-F 直连链路诊断——compvisu sys 与 hybvisu 输出解读
  type: menu
  source_pages: p341-342
  source_chapter: Remote Processing Group (How to) / 1 Maintenance command to check ABC-F link status
  source_quote: |
    "compvisu sys … | Direct Link mgr state.......... ENABLED | Inter-node protocol H323....... yes | RTP
    Direct..................... yes … | VAD (Voice Activity Detection): - G723/G729...... no | - G711........... no |
    CNG (Comfort Noise Generation): no" (p341)
    "hybvisu -f all … Direct link 2002 to node 2:UP(Enabled/DATA_TRANS) High Bandwidth … States shown in \"hybvisu\"
    have the following meaning: ­ IDLE … ­ SYN_REQ … ­ SYN_ACK … ­ DATA_TRANS: the link is established and ready to
    transport data … High bandwidth: calls established on this link will allow all codecs (G711, G722, OPUS, G729) …
    Low bandwidth: calls established on this link will use G729 codec … Number of accesses From 1 to 24 … Encryption
    No/Yes" (p341-342)
  summary: |
    两条 mtcl 命令：①compvisu sys——Direct Link 管理状态（ENABLED）、节点间协议（H323）、RTP Direct、Fast Start、
    VAD/CNG 选项；②hybvisu -f all（全部链路）/ hybvisu -f <邻节点号>（单链路）——链路号与邻节点、状态四态（IDLE 未激
    活 / SYN_REQ 本端在建 / SYN_ACK 对端在建 / DATA_TRANS 已建立）、带宽档（High=全编解码 G711/G722/OPUS/G729，默认；
    Low=G729）、接入数 1-24、对端主 CPU IP（CPUb 为空间冗余第二地址）、加密开关。Remote PG 实验 (c09) 的第 0 步就
    是跑这两条确认链路 UP(DATA_TRANS)；实验后段还演示从 mgr 菜单 Inter-Nodes Links > Logical Links (ABC-F) >
    Link_2 > Hybrid or Direct Link Access > X25/Direct Link Synchronization 临时 Disable 链路做故障注入。
  conditions: 实验口径；生产判读需结合带宽规划
  tags: [menu, cli, abc-f, hybvisu, diagnostics]

- id: f27
  title: Soft Panel Manager 架构与安装三件套流程
  type: flow
  source_pages: p371-395, p396-411
  source_chapter: SOFT PANEL MANAGER OVERVIEW / INSTALLATION（讲义 + How-To）
  source_quote: |
    "Soft Panel Manager Server … RTI … LED Wallboards Panel PC Individual PC Screen … Business data interface … Data
    retrieval via RTI Connector which communicates with the Contact Center Supervision software … Business Data can be
    pushed to the Soft Panel Manager server using JMS (Java Message Services). The Soft Panel Manager server uses
    ActiveMQ as a JMS implementation … http://<servername>:<serverportnb>/wbm/services/realTimeDataService" (p376-378)
    "Install the Soft Panel Manager server • Launch ccdSoftpanel_setupx.x.x.x.exe … Check that CCS application is
    installed and that the OXE connection is configured • Install the RTI Connector application • Launch
    RTIConnector_x.x.x.x_installer.exe … Install the FlexLM server • Launch the installation file:
    ALE-FLEXlmServer-11.15.exe" (p389-390)
  summary: |
    数据链：OXE CCD ← CCS ←（RTI Connector，Windows 服务）→ SPM 服务器（Tomcat，默认端口 9060，wbm 应用）→ LED 墙板/
    液晶/Panel PC/电视显示 + 邮件告警；业务数据经 Business Data Interface 以 JMS（ActiveMQ）推送，全部数据另经
    realTimeDataService Web 服务外露。安装顺序三步：①SPM 服务器（ccdSoftpanel_setup，默认目录 C:\SoftPanelServer、
    开始菜单 Alcatel-Lucent\Soft Panel Server、HTTP 端口 9060；装后核 SoftPanelServer 服务自动启动，浏览器
    http://localhost:9060/wbm，admin/admin）；②RTI Connector（RTIConnector 安装器，填 SPM 服务器 IP，装为服务自动
    启动；前提 CCS 已装且配好 OXE 连接；警告：同机共存时 CCS 必须专用于 RTI Connector，RTI 运行期间禁止手工再启
    CCS）；③FlexLM 许可服务器（ALE-FLEXlmServer 安装器 + softpanel.lic 至 C:\FLEXlmServer\License，LMTOOLS 验证
    Start Server 与 Status Enquiry）。前置：OXE 侧需 RTI 许可（103 号包，adm_acd option 15 或 spadmin 核对）。
  conditions: 实验装在 Client11（192.168.1.11）；许可文件由讲师提供（实验口径）
  tags: [flow, spm, rti-connector, flexlm, installation]

- id: f28
  title: SPM 基础设置与日统计链路——Settings 四区 + afe.properties
  type: menu
  source_pages: p412-417
  source_chapter: Soft Panel Manager Installation (How to) / 2 Soft Panel Manager basic settings configuration
  source_quote: |
    "Administration> Settings … In the General section, you can configure the IP address of the server. The Tomcat
    port is configured at installation and cannot be modified. … License Server … FlexLM server host (localhost by
    default) and port (27000 by default) … Mail Configuration … You can test your mail configuration." (p413)
    "CCD filters are mandatory to define the statistics to be usable in the system (widgets, alarm, wallboards). …
    AgentWidget is based on 3 statistics: ServiceState, PhoneStat and StateDuration." (p415)
    "afe.sites OXE main CPU address (hostname or IP address) … afe.pilots A list of pilots names to monitor, separated
    by \";\" … These statistics are retrieved every 15 minutes and reset to 0 at 00h00. This time can't be reduced …
    Every retrieval is performed 2 minutes after the quarter hour (ex…15h02,15h17,15h32….)" (p416-417)
  summary: |
    Settings 四区：General（服务器 IP；Tomcat 端口装后不可改）、License Server（FlexLM 主机缺省 localhost、端口缺省
    27000）、Mail Configuration（SMTP+发件凭据，可勾选 Test the configuration 发测试邮件）、CCD Filters（勾选各对象
    类型要用的统计名后 Save——过滤器决定哪些统计可用于挂件/告警/墙板；全部配置完后点 Keep used filters only 清理未用
    过滤器提性能；AgentWidget 依赖 ServiceState/PhoneStat/StateDuration 三统计）。日统计链路：改
    C:\SoftPanelServer\tomcat\webapps\wbm\WEB-INF\classes\afe.properties——afe.sites=OXE 主 CPU 地址（多站点用分号，
    不支持空间冗余）、afe.pilots=要监控的 Pilot 名单（空=全部）；结果出现在 Real Time Data > Statistics > Ccd
    Consolidated，命名 S(站点号)_(Pilot名)_daily_计数器类型；每 15 分钟取一次（OXE 侧 15 分钟编译一次，不可更快），
    取数在每刻后 2 分钟（15h02、15h17…），0 点清零。
  conditions: 许可失效时统计更新被阻塞（ Administration>Monitoring 可 Check license）
  tags: [menu, spm, settings, daily-statistics]

- id: f29
  title: Soft Panel 对象模型——背景 → 视图 → 面板 → 挂件四层与显示 URL
  type: structure
  source_pages: p420-447, p457-474
  source_chapter: CONFIGURATION OF THE SOFT PANEL（讲义 + How-To）
  source_quote: |
    "A soft panel display is made of one or several views • Each view is alternately displayed for a number of seconds
    • The views are: Created and initialized from the Soft Panel Manager management tool • Customized from the view
    itself using Firefox • other web browsers are not allowed for views customization" (p421)
    "To display the result of this configuration on a soft panel: … Enter this URL:
    http://<SoftPanelSrvIP>:<port>/wbm/displayPanel.htm?name=<soft panel name>" (p427)
    "Supported Display Panels: • Alcatel-Lucent Serial display panel: 1 line 12 characters • IP/Serial Alcatel-Lucent
    display panel: 2/4/6 lines 16 characters • Adaptive Micro System (AMS) display panels range" (p379)
  summary: |
    四层模型：背景（4 张预装 + 上传自定义，Soft Panels > Backgrounds）→ 视图（Soft Panels > Views 新建，选背景；保存
    后自动进入视图定制页——工具栏三个钮：回管理台/插挂件/换背景；默认内容=背景+Logo+左侧消息区；定制只能用 Firefox）
    → 软面板（Soft Panels > Soft Panel，名称+认证 No+绑定一个或多个视图，多视图按定时器轮播）→ 挂件。显示端 URL：
    displayPanel.htm?name=<面板名>。LED 硬墙板另支持 ALE 串口（1 行 12 字符）、IP/串口（2/4/6 行 16 字符）与 AMS 面板。
    挂件全集与参数：Gauge 圆表（Min/Max/角度 ≤180 半圆/Th1 绿转黄/Th2 黄转红/随值变背景）、HorizontalGauge、Chart
    （水平条/垂直条/饼/折线，折线为历史视图，服务端最多存 2000 值或 24 小时；饼图 Display Value=No/Value/Percentage）、
    Simple（计数器如 Pilot1_NbOfWaitingCalls）、Table（行列+单元格级文本/计数器/表头）、HTML（仅 http:// 可嵌入，刷新
    定时+裁剪）、Text、Time（日期模板与自定义）、Barometer（Th1/Th2 三图主题：cat/insect/ladybird/led/note/smiley/
    traffic light/tree/weather，默认 weather，Th1/Th2 缺省 50/80；加主题=建同名目录放 1.png/2.png/3.png）、Agent
    （OTCC SE 专属，绑定坐席，状态色随 CCS）、Image、消息区（常驻特殊挂件，字体走 panel2.css 的 .MessageDisplay）。
  conditions: 全局样式（数据历史 historySize/historyTimer、文字色、图表色、Logo、背景色）在 param.js/panel2.css/mainPanel.css（p429-434）
  tags: [structure, spm, soft-panel, widgets]

- id: f30
  title: SPM 告警机制——阈值条件、两种动作与告警视图
  type: flow
  source_pages: p450-453, p478-479
  source_chapter: CONFIGURATION OF THE SOFT PANEL / Alarm views（讲义 + How-To）
  source_quote: |
    "With alarms, two actions can be realized on real time value condition (statistics, calculated data, business
    data). • Send an email when a threshold is reached • Additionally, a specific view can be displayed on Soft Panels
    when the alarm is raised • Configuration steps: • Create a specific alarm view • Customize the view … • Create an
    alarm linked to a statistics counter • Assign the specific view to the alarm" (p450)
    "Object type … ProcessingGroupAgent - WaintingQueue - Agent - ProcessingGroupOther - Pilot … Condition -<: lower
    >: greater >=: greater or equal <=: lower or equal ==: equal … Validity timer The value must match the condition
    for all the validity timer duration … Notification interval If 0, the alarm will be sent only once, if not 0, the
    alarm will be sent every" (p478)
  summary: |
    告警四步配置：①建专用告警视图并定制挂件；②Alarms > New Alarm 填参数——引用名、描述、Enabled、计数器引用（对象
    类型五选：ProcessingGroupAgent/WaintingQueue[原文拼写]/Agent/ProcessingGroupOther/Pilot + 统计名）、条件
    （<、>、>=、<=、==）与阈值、Validity timer（条件须持续满足整个时长才触发）、Notification interval（0=只发一次，
    非 0=按周期重复）；③动作一——发邮件（Recipients 分号分隔、Subject 前插入[统计引用]、Message 尾附统计描述；前置
    是 Settings 里配好 SMTP）；④动作二——在指定 Soft Panel 上把普通视图替换为告警视图 N 秒，可再挂音频文件。典型
    实验：Sales Pilot 低效率阈值触发告警视图（p457）。
  conditions: 告警统计须先在 CCD Filters 勾选（f28）
  tags: [flow, spm, alarm, email]

- id: f31
  title: CCTA 票据分析器双工具链——Importation 与 Ticket Tracer
  type: flow
  source_pages: p480-497
  source_chapter: CONTACT CENTER TICKET ANALYSER（讲义 + How-To）
  source_quote: |
    "2 types of tickets exist: • Tickets \"events\" • Displays the changes of the objects state … • Tickets
    \"communications\" • Displays the information of communications: date and time of the call, duration of
    conversation, agent responding to the call, called pilot, cause of end of the call" (p483)
    "The Importation that permit to import daily and automatically the CCd communication and events tickets (in order
    to analyse offline). • The Ticket Tracer which aims is the visualization of the CCd communication and event
    tickets • They are located in \\Program Files(x86)\\Alcatel\\Ticket Analyser" (p484)
    "PABX Enter the IP address of the Call Server (i.e. 192.168.1.3) … The files will be dropped in C:/Program
    Data /Alcatel /Ticket Analyzer/ (name or IP address of the pcx)." (p493-494)
  summary: |
    工具链四步：①装 ccta_setup.msi（默认路径）；②Importation 工具首次连接声明站点——PABX=Call Server IP、User=mtcl、
    Password（实验示例填 mtcl）、Use SSH 按需、Tickets type=both；导入后 .Z 文件落 C:/ProgramData/Alcatel/Ticket
    Analyzer/<PCX 名或 IP>；③Ticket Tracer 分析——File > Open（Tickets on PC，路径拼 PABX IP，选票据类型与起止日期）
    → 过滤器（Headers selection + Object selection + 激活；实验选 Long Ticket、全部对象、ID Mao、Column）→ 出报表；
    ④Functions > File ASCII 导出文本（Notepad/Excel 可读）。数据口径：结束原因 40 种（0=主叫挂机、1=系统挂机、
    26=坐席挂机）；呼叫类型 10 种（0=非 ACR、1=ACR）。
  conditions: 实验 .Z 文件来自 OXE 票据机制；离线分析不占 CCS 连接
  tags: [flow, ccta, tickets, reporting]

- id: f32
  title: 特殊功能菜单路径汇总表——Pilot/PG/中继/前缀四类开关
  type: menu
  source_pages: p498-515, p516-530
  source_chapter: SPECIAL FEATURES（讲义 + How-To）
  source_quote: |
    "Management • Applications/ CCd/ Pilot • Transfer with priority: True … • Applications/ CCd/ Pilot • Inter-guide
    tone Number: 2 • Redirection busy tone on DID: False … • Translator/ Prefix Plan • Prefix meaning: General
    Features • General features: Agent processing group call pick" (p499-503)
    "Trunk Groups> trunk group> Virtual accesses for SIP • Number of SIP accesses: 2 (31 x 2= 62 SIP trunks) • Trunk
    Groups/ Trunk Group • Trunk Group ID: 12 • Max. % of trunks out CCD : 20 … Applications/ CCd/ Pilot/ Trunk
    limitation • Pilot Directory Number: 31600 • Trunk Group ID: 12 • Max. % of trunk: 30" (p513-514)
    "Applications/ CCd/ Processing Group • Auto return to wrap up: True … Show Supervisor Listening: False/True …
    Help On External Call: False/True … Applications/ CCd/ CCD Users/ CCD operations data management • Forwarding
    activ. On Logon/Logoff: True" (p510-512, p509)
  summary: |
    四类开关的菜单归属：①Pilot 级（Applications/CCD/Pilot/<号> Offer）——Transfer with priority（优先转接，双队列）、
    Inter-guide tone Number（间隔引导音，默认 2）、Redirection busy tone on DID（饱和播忙音）、Transfer to pilot in
    redirection（劝恼状态可转）、Pilot Supervised Transfer（询问期跟随路由分配）、Trunk limitation（Pilot 中继限额）；
    ②PG 级（Applications/CCD/Processing Group）——Auto return to wrap up（永恒整理）、Show Supervisor Listening
    （秘密监听）、Help On External Call（私话后可插入）；③坐席数据级（Applications/CCD/CCD Users/CCD operations
    data management）——Forwarding activ. On Logon/Logoff（登出即取消私号立即转发到坐席信箱）；④系统级——Translator/
    Prefix Plan 建 #013（Agent processing group call pickup）/ #014（Direct call pickup）/ Conversation Recording 前
    缀 + Categories > Phone Features COS 放行；Trunk Groups > Trunk Group 的 Max. % of trunks out CCD（业务中继预
    留）。逐项行为验证法见 c13。
  conditions: 前缀功能需 COS 类别 0（默认全员）开启对应 Phone Features
  tags: [menu, special-features, pilot, trunk]

- id: f33
  title: Excel 报表模板体系与定制原理——General/Custom 双工作表链接
  type: structure
  source_pages: p531-543, p544-554
  source_chapter: CUSTOMIZATION OF EXCEL COUNTERS（讲义 + How-To）
  source_quote: |
    "Open the file corresponding to the Ccdistribution object under: \\Program Data\\Alcatel\\CCSupervisor\\Excel\\
    Formats • FormPil.xls pilot • FormAgt.xls agent • FormTeam.xls processing group • FormpAg.xls agent per pilot •
    FormpGT .xls group per pilot • Formpgo.xls group type other • FormSyst.xls trunks • FormCod.xls transaction code
    (3digits) … FormPS.xls statistic pilot" (p534)
    "Copy from General tab a structure spreadsheet from B7 to D43 and paste it in the Custom worksheet … Copy from
    General tab, the value from B8 to D39 Paste to Custom tab, the links from B8 to D39" (p537-538)
    "NO!, because only 1 table form has been created, so with the granularity of ½ an hour, you will retrieve only the
    transition from 0:00 to 16:00. • You must create, in \"custom\", a second table form linked to the value contained
    in the \"General\" second table form." (p542)
  summary: |
    模板体系：CCS 出报表=取数写入 TEMP .XLS，结构来自 Formats 目录模板（按对象分 11 种：FormPil/FormAgt/FormTeam/
    FormpAg/FormpGT/Formpgo/FormSyst/FormCod/FormCods/FormPS/FormPePS/FormPpPS）。定制原理=在模板里加 Custom 工作
    表：从 General 复制结构区（B7:D43，3 列=时段时间/已接/放弃；>24 行覆盖全天按小时）再选择性粘贴链接（Paste Link）
    引用 General 的值，即可在 Custom 上加图表、改样式。粒度陷阱：一张表最多 24 行，½ 小时粒度只覆盖 0:00-16:00，须
    建第二张链到 General 第二表。How-To 版本流程：先把 FormPil.xlsm 备份为 FormPil_old.xlsm 再改原件（保回滚）、启用
    宏内容、改名系列（Calls received in open/blocked state）、关 CCS 重开生效，Statistics > Excel > Pilot 选 31600
    + Daily + 1/2 小时粒度 + Keep Excel links 生成（见 c14）。
  conditions: 注意 Formats 目录同时存在 .xls（讲义）与 .xlsm（实验宏版）两种扩展名口径
  tags: [structure, excel, reporting, template]

- id: f34
  title: CCS Server 内/外部架构与客户端接入切换
  type: structure
  source_pages: p555-590
  source_chapter: CCS SERVER（讲义 + How-To）
  source_quote: |
    "Internal CCs server: • The process \"serv_ccs\" is started on the OmniPCX • 15 CCsupervision Clients
    simultaneously connected • External CCs server: • The process \"serv_ccs\" is stopped on the OmniPCX • \"server
    CCs\" service is started on the PC • 120 CCsupervision Client simultaneously connected" (p557)
    "The maximum # of connections to the AFE is 15 • The maximum # of connections to the CCs server is 120 … This
    feature is available since the release R3.1 of the CCd and the CCs 4.3.46.1 • The CCs server is mandatory for
    these releases when the CCs connections numbers to the PCX is greater than 9" (p558, p567)
    "Operating system: Windows Server 2019 and Windows Server 2022. … Only 1 CCS Server can connect to the PABX!" (p567, p590)
  summary: |
    三种接入形态：①直连 AFE——物理上限 15 连接；②内部 CCS Server——OXE 上 serv_ccs 进程（parameters.cfg 的
    serv_ccs_on_dhs=1），最多 15 个 CCS 客户端，自身占 AFE 一条连接；③外部 CCS Server——OXE 进程停掉
    （serv_ccs_on_dhs=0 并 dhs3_init -R MAIN_AFE），Windows Server 2019/2022 装 serv_ccs.msi 服务，最多 120 客户端
    （服务自报 maxCli=150、maxConnected=120）；CCd R3.1 + CCs 4.3.46.1 起连接数 >9 必须用 CCS Server；一个 AFE 只能
    接一个 CCS Server（内部进程未停时外部服务会被 AFE 拒接）。客户端切换：Window > Customise > Network 从 Direct
    connexion 改为经 CCS Server（填服务器 IP）；维护锚点：CCS Real Time > Licenses 看锁占用（AFE 1 连接 + Server 1
    连接 + monosite 令牌）、adm_acd option 11 看 *SERV_CCS* 终端、adm_acd <Server IP> -servccs option 10 看经服
    务器接入的客户端、Server Status 工具看双绿灯、日志 servccsYYMMDD.log。切换操作序列见 c15。
  conditions: 实验把外部 CCS Server 装在 WINDOWS_SRV（192.168.1.70）
  tags: [structure, ccs-server, architecture, licensing]
```

---

## 任务覆盖自检（task ↔ id 映射）

- task-01（POD 搭建核验）→ f02、f03
- task-02（CCS 安装声明）→ f06、f07
- task-03（POD 定稿）→ f04、f05、f08
- task-04（ACR 基础对象）→ f14、f16
- task-05（技能体系）→ f13、f14、f18
- task-06（ISM 手算）→ f19（算法结构，算例值在 principle/c04）
- task-07（ASM 编辑器安装）→ f20（流程细节在 c05）
- task-08（ISM 脚本）→ f20、f21
- task-09（LIT 切换）→ f21（参数语义在 principle）
- task-10（调试器/重选）→ f22、f19
- task-11（LCA）→ f23
- task-12（网络互助/Remote PG）→ f24、f25、f26
- task-13（SPM 部署）→ f27、f28
- task-14（SPM 显示配置）→ f29、f30
- task-15（CCTA）→ f31
- task-16（特殊功能）→ f32
- task-17（Excel 报表）→ f33
- task-18（CCS Server）→ f34
- task-19（维护命令箱）→ f15、f26、f23、f25
- task-20（容量上限）→ f11（SPM 限制在 principle p 系列与 counter-example）
- 全书骨架/课程主线 → f01
- 覆盖自检：34 条 id（f01-f34）连续无缺号；YAML 以 ``` 闭合；关键讲义模块（RLAB/SIP 模拟器/CCD 预配置/ACR 五讲义/互助/Remote PG/SPM 三模块/CCTA/特殊功能/Excel/CCS Server）与 15 个 How-To 章的流程框架均已建条。
