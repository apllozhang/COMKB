# 术语/缩写/产品名候选 — OmniTouch Contact Center Standard · Advanced (OTCCXTE101EN Ed07)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 55 条。DDI/DID、ABC-F、GT、RSI、CSTA、MAO、OMS、GD4、TSC、COS、IPDSP、EWT/MWT 等缩写书中未正式给全称，full_name 字段如实省略或标注上下文对应，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: ACR
  full_name: Advanced Call Routing（书中展开）
  category: concept
  source_pages: p63-78, p161
  source_quote: |
    "ACR = Advanced call routing. Option of the CCD that allows to route calls according to criteria (skills of the
    agents, agent having already answered etc..). ACR requires the ASM software and a specific management of the CCD
    matrix (a waiting room must be created..)." (p161)
    "9 different ACR Rules • Individual Skill Mapping Rule (ISM) • Last Called Agent Rule (LCA) • Authorized list Rule
    / Unauthorized list Rule • Redirection Rule • Redistribution Rule • Idle Rule • Com Rule" (p67)
  definition: |
    CCD 的高级路由选项：按坐席技能、上次应答坐席等条件路由呼叫；硬前提是装 ASM 软件并改造矩阵（必须建等待室）。规则
    族含 ISM、LCA、授权/非授权名单、重定向、重分发、Idle、Com 等（工具栏另有 Call Number、IVR 规则，讲义标题计为 9
    类）。呼叫经"特征化→ASM 生成坐席列表→等待室分配"三步接续。
  alias_or_related: ASM（g02）、ISM（g03）、LCA（g04）、Waiting Room（g11）
  tags: [concept, acr, routing]

- id: g02
  term: ASM
  full_name: Agent Selection Modul（书中拼写，p66；p161 作 Agent Selection Module）
  category: concept
  source_pages: p66-70, p161
  source_quote: |
    "The ACR script is executed by the ASM Server … The purpose of the ACR feature (and so of the ASM server) is to
    provide a list of agents who can answer to the customer call according to: The ACR rule used in the script • The
    caller id • The call tag • The called number" (p66)
    "ASM= Agent Selection Module. Software for dealing with ACR calls. It can be carried by the call Server or to be
    installed on an external server (external ASM)." (p161)
  definition: |
    处理 ACR 呼叫的软件服务器：负责脚本解释、数据库查询与更新、按坐席配置+脚本规则+呼叫档案计算坐席列表。可内置于
    OXE Call Server（alb 进程，脚本存 /usr3/afe）或装在外部 Windows 服务器（外部 ASM，细节书内未展开）。
  alias_or_related: 内置 ASM 的承载进程=alb（g08）；编辑器=ASM Script Editor（g47 相关）
  tags: [concept, asm, acr]

- id: g03
  term: ISM
  full_name: Individual Skill Mapping（书中展开，p67 作 Individual Skill Mapping Rule）
  category: concept
  source_pages: p67, p160-181
  source_quote: |
    "ISM=Individual skill mapping. It is one of the possible subprograms of ACR. It is inserted as a building block in
    the ACR program. This is the most used." (p161)
    "It allows the ASM server to find a list of agents with the skills corresponding to the statistics pilot called." (p162)
  definition: |
    ACR 最常用的规则子程序：按呼叫档案的技能属性与坐席技能匹配生成坐席列表——强制属性全满足进第一子列表，超时逐级降
    级（N-1、N-2…），同级按成本 Cman/Copt 排序，再同分按 PLTR 或 LIT。
  alias_or_related: 成本公式与降级序列见 principle p01/p02；排序参数 asm_ag_free_duration
  tags: [concept, ism, skills]

- id: g04
  term: LCA
  full_name: Last Called Agent（Rule）（书中展开）
  category: concept
  source_pages: p246-259
  source_quote: |
    "Last Called Agent Rule (LCA) • Select the agent who last answered the call" (p67)
    "If an agent has already answered to the customer, this information is stored in the ASM server memory • Whatever
    the call status (blocked, dissuaded…) the agent number who has answered the last time to the caller is kept and
    can be used by the \"Last Called Agent\" rule." (p250)
  definition: |
    从 ASM 记忆取"上次应答该主叫的坐席"的规则：记忆按主叫号码/呼叫标签组织，已接通呼叫记应答坐席，未接通记 7 种状
    态；alb 进程重启清空记忆，MAIN_AFE 重启不清。典型脚本=IF(有记忆且未超时) 走 LCA，否则回落 ISM。
  alias_or_related: 状态码表 LAST_CALLED_STATE（principle p13）；脚本范式（principle p12）
  tags: [concept, lca, memory]

- id: g05
  term: CCD
  category: concept
  source_pages: p19-38, p161
  source_quote: |
    "CCD matrix description" (p21-22 章题)
    "The Direct connection The CCS is connected directly to the AFE (CCD program)." (p45)
  definition: |
    OXE 上的呼叫分配（Contact Center Distribution）程序与矩阵对象体系：Pilot、队列、等待室、处理组、方向（direction）、
    分配规则等。书中未正式展开 CCD 缩写全称；AFE 即 CCD 程序（p45 括注）。矩阵结构可用 CCS Navigator 全景查看。
  alias_or_related: AFE（g07）、矩阵对象族（g40 处理组、g09 Pilot、g11 等待室）
  tags: [concept, ccd, matrix]

- id: g06
  term: CCsupervision（CCS）
  category: concept
  source_pages: p39-47, p94-115
  source_quote: |
    "Alcatel-Lucent CCsupervision Setup Wizard" (p41)
    "Configurations/ Supervisor rights … Configurations/ Agent … Statistics/ Last received calls … Real time/ Filter" (p98-109)
  definition: |
    OTCC 的监督与管理客户端：配置（Pilot/队列/处理组/坐席/技能/ACR 数据/脚本编辑器）、实时（Navigator/Filter/PG/Agent）、
    统计（Last received calls、Excel 报表）与流程管理（Call Flow mgt：Call Routing/Call Distribution）四大区。多客户
    端接入经 CCS Server（g44）。
  alias_or_related: CCS Server（g44）；登录 administrator/alcatel 强制改密（实验口径）
  tags: [concept, ccs, supervision]

- id: g07
  term: AFE
  full_name: Alcatel Front End（Server）（书中以 "Alcatel Front End Server" 出现，p68）
  category: concept
  source_pages: p45, p68, p557-558
  source_quote: |
    "Direct connection The CCS is connected directly to the AFE (CCD program)." (p45)
    "The maximum # of connections to the AFE is 15" (p558)
  definition: |
    OXE 侧承载 CCD 的前端程序：CCS 直连的对象（Direct connection），也是 ASM/alb、CCS Server 的连接对端。物理连接
    上限 15 条——这是 CCS 客户端规模与 CCS Server 存在意义的根源。
  alias_or_related: CCS Server 连接模型（g44）；MAO（Call Handling (MAO)，p68，未展开）
  tags: [concept, afe, ccd]

- id: g08
  term: alb / ALB
  full_name: Agent List Builder（书中展开，p161）
  category: concept
  source_pages: p161, p172, p198, p272
  source_quote: |
    "ALB =Agent List Builder (=asm) process of the call server used by ACR." (p161)
    "The scripts are saved in \"/usr3/afe\" for an internal ASM server (\"alb\" process)" (p198)
  definition: |
    Call Server 上承载内置 ASM 的进程：计算并返回坐席列表（默认最多 200 个），运行脚本编译产物 .alb，维护 LCA 记忆；
    其参数文件为 /DHS3data/afe/.inialb（实验观察：StatPeriod 5、DualTimeOut 200、NbMaxAgent 200）。kill alb=清 ASM
    记忆。adm_acd <IP> -salb 为其维护入口。
  alias_or_related: ASM（g02）；记忆清理（counter-example n15）
  tags: [concept, alb, asm]

- id: g09
  term: Pilot（路由 Pilot）
  category: concept
  source_pages: p81, p123, p134-136
  source_quote: |
    "A pilot is declared ACR when: • One of its direction is a waiting room • Active pilot rule is applied" (p81)
    "Create the pilot ACR Pilot (31603)." (p135)
  definition: |
    CCD 矩阵的呼叫入口对象：带路由规则（open/closed/blocked on rule）与到队列/等待室的方向。满足"有等待室方向或挂
    激活规则"即为 ACR Pilot。业务号码规划：客户拨统计 Pilot，路由 Pilot 是矩阵内部入口。
  alias_or_related: Statistics pilot（g10）；Pilot rule / Direction（f12）
  tags: [concept, pilot]

- id: g10
  term: Statistics pilot（统计 Pilot）
  category: concept
  source_pages: p123, p136, p162
  source_quote: |
    "Applications/CCD/Statistics pilot • Pilot Stat. Directory Number: 31650 … Routing pilot: 31600 • Call tag: •
    Call priority: -1 • Call Profile: 0" (p123)
    "It allows the ASM server to find a list of agents with the skills corresponding to the statistics pilot called." (p162)
  definition: |
    承载 ACR 呼叫档案的入口对象：客户实际拨打的号码。参数含统计 DN、名称、路由 Pilot、呼叫标签、呼叫优先级（例 -1）
    与呼叫档案号。换档案=换统计 Pilot 或改其绑定。
  alias_or_related: Call profile（g14）
  tags: [concept, statistics-pilot, call-profile]

- id: g11
  term: Waiting Room（等待室）
  category: concept
  source_pages: p71-72, p82, p119, p134
  source_quote: |
    "Waiting Rooms are needed in ACR & don't work in FIFO mode … Waiting Room & Waiting Queue CANNOT be open at the
    same time" (p71-72)
    "Greeting guide + 6 parking levels … Up to the 40 languages in the Alcatel-Lucent OmniPCX Enterprise" (p82)
    "Type + Waiting room … Max Waiting Time: 3000" (p119)
  definition: |
    ACR 专用等待对象：非 FIFO、按呼叫档案挂动态组、无资源选择优先级；语音引导=迎宾+最多 6 个泊位（parking level），
    每"泊位可用 EWT 表/IAA 地址/语音引导/IAA 交互排队，支持 OXE 40 种语言。与等待队列互斥（同一规则不能同开）；饱和
    判定 EWT>最大等待时间。
  alias_or_related: 阻塞传导链（n19）；Traffic Sampling Period 对等待室不可用（p365）
  tags: [concept, waiting-room]

- id: g12
  term: Dynamic group（动态组）
  category: concept
  source_pages: p71, p83, p88
  source_quote: |
    "The ASM server generates a list of agents who match the ACR script needs — Dynamic Group" (p71)
    "The ASM returns a list of agents and this list it is called dynamic group" (p83)
    "A dynamic PG is created downstream the WR according to the call profile: So, no resource selection priority
    management" (p88)
  definition: |
    ASM 按脚本算出的坐席列表实体：呼叫携其进入等待室；系统在等待室下游按呼叫档案动态生成组，因此没有资源选择优先级
    管理可言——分配完全由列表与档案驱动。
  alias_or_related: ISM 列表（g03）；坐席列表缓冲（principle p07）
  tags: [concept, dynamic-group]

- id: g13
  term: Call tag（呼叫标签）
  category: concept
  source_pages: p74-76, p123
  source_quote: |
    "Call Tag … CSTA filed for call identification" (p74)
    "IVR — Call tag CLID … Call Profile" (p75)
    "adm_acd IP@ of ASM server -salb • option 28 … CALLTAG: enter calltag number or characters" (p257, p228)
  definition: |
    随呼叫携带的业务标记（IVR 打标、转接携带、CSTA 字段），用于 ASM 特征化与 LCA 记忆索引（主叫号码和/或呼叫标签）；
    调试器可按 CALLTAG 过滤轨迹。统计 Pilot 参数之一。
  alias_or_related: CLID（g15）；调试器 CALLTAG 过滤（f22）
  tags: [concept, call-tag, characterization]

- id: g14
  term: Call profile（呼叫档案）
  category: concept
  source_pages: p74, p122, p163-164
  source_quote: |
    "Call Profile (List of attributes) • Required skills to handle the call (up to 7)" (p74)
    "A call profile is made up of attributes list • 7 attributes maximum per call profile … Each attribute has got: A
    characteristic … A domain … A component … A skill level … Mandatory or optional" (p163-164)
  definition: |
    呼叫的技能需求清单：最多 7 个属性，每个属性=特征+域+技能+要求等级+强制/可选；挂在统计 Pilot 上进 ASM。强制属性
    决定第一子列表门槛，可选属性只参与 Copt 排序。
  alias_or_related: 坐席侧对应 Agent profile（技能+等级+激活标志）；技能体系（g16）
  tags: [concept, call-profile]

- id: g15
  term: CLID / NDI
  category: concept
  source_pages: p74
  source_quote: |
    "CLID: Caller Line Number / Calling Number • NDI: Called Line Number (for Direct ACD Call)"
  definition: |
    呼叫特征化两枚号码：CLID=主叫号码（书中此释义为 Caller Line Number），NDI=直接 ACD 呼叫的被叫线路号码。两者是
    ASM 内部数据库查询（按号码查名称/档案/名单/优先级）与 LCA 记忆的键。调试器 CALLING 过滤要求与运营商送达号码逐
    位一致。
  alias_or_related: 脚本内 DB 查询（p76）；LCA 记忆键（g04）
  tags: [concept, clid, characterization]

- id: g16
  term: Skill / Domain / Component（技能体系）
  category: concept
  source_pages: p120-121, p150, p163-166
  source_quote: |
    "2 steps for the skills management • Definition of the skill domains • Definition of the skills (components)" (p120)
    "One DOMAIN is made up of One NUMBER: between 0 and 19 … One weight: between 1 and 20 … One skill in a domain is
    made up of: One NUMBER: between 0 and 999 … The domains 0 & 1 are created by default (language and media)" (p166)
  definition: |
    四层技能模型：域（0-19 号，带权重 1-20）→ 技能/组件（域内 0-999 号，名 1-16 字符、缩写 1-4 字符）→ 等级（1 低-9
    高）→ 激活标志。0/1 号域与 0-99 号技能为预定义（语言/媒体）。坐席最多 50 技能、呼叫档案最多 7 属性。
  alias_or_related: ABC 网络广播（n17）；技能矩阵/导出导入（f13）
  tags: [concept, skills, domain]

- id: g17
  term: EWT / MWT / TSP（队列水位参数族）
  category: concept
  source_pages: p81-82, p86, p365
  source_quote: |
    "Saturation if EWT > Maximum Waiting time of waiting room" (p81)
    "EWT > MWT => the waiting room is congested so another direction is selected" (p86)
    "Maximum waiting time … Enter a value between 0 and 3276 seconds. … Traffic Sampling Period … Enter a value
    between 2 and 15 minutes." (p365)
  definition: |
    三个水位概念：EWT（预期等待时间，书中未正式展开缩写，与 Expected waiting time 混用）用于同优先级方向裁决与饱和
    判定；MWT=队列/等待室的最大等待阈值（0-3276 秒，0=零等待队列）；TSP=话务采样期（2-15 分钟，等待室不可用，滚动
    计算平均等待时间的窗口）。
  alias_or_related: 饱和行为（f12）；MWT=0 语义（n36）
  tags: [concept, ewt, mwt, tsp]

- id: g18
  term: Dissuasion（劝阻）
  category: concept
  source_pages: p253, p500, p520
  source_quote: |
    "1: the last call has been sent to a dissuaded queue" (p253)
    "Sending busy tone instead of dissuasion voice guide" (p501 章题语境)
  definition: |
    队列饱和时对呼叫的"劝退"处理：播劝阻语音引导或改播忙音/间隔引导音。LCA 状态码 1 即"上次呼叫被送入劝阻队列"。
    Transfer to pilot in redirection 决定转接呼叫能否进入劝恼流程。
  alias_or_related: 间隔引导音/忙音（g55、n28、n29）
  tags: [concept, dissuasion]

- id: g19
  term: Wrap-up（整理态）/ Eternal wrap-up（永恒整理）
  category: concept
  source_pages: p58, p346, p510, p526-527
  source_quote: |
    "When Agent1 hangs up, automatic wrap-up status is applied to the agent." (p58)
    "prefix ACD then 2 = Wrap up" (p346)
    "Auto return to wrap up: True … Give the opportunity to realize telephonic actions during the wrap up timer
    without cutting it." (p510)
  definition: |
    坐席接续后的事后处理状态（Pilot 定时器驱动，自动或手动）。永恒整理=PG 上开 Auto return to wrap up：整理期内可外
    呼/撤出/代接而不打断整理计时，动作结束回到剩余整理时间。ACD 前缀 2 可手动进入。
  alias_or_related: Wrap Up duration 配置（Pilot，实验 200 秒）；LCA 调试案例二的前提状态
  tags: [concept, wrap-up]

- id: g20
  term: Mutual aid（互助：Blind / Intelligent）
  category: concept
  source_pages: p293-315
  source_quote: |
    "Blind mutual aid • No ABC-F link between ACD nodes • Doesn't transfer ACD information • Pilot's state is unknown
    • On the remote ACD node, calls are handled as new calls" (p295)
    "Intelligent mutual aid is used in homogeneous or heterogeneous networks to rout calls to remote ACDs depending on
    their state." (p299)
  definition: |
    跨节点溢出的两种形态：盲互助不经 ABC-F，远端把呼叫当新呼叫处理；智能互助经 ABC-F 交换 Pilot 状态/已听引导/真实
    等待时间，按远端状态路由，远端可 REJECT（按地址类型五类回退本地）。专用对象=互助队列+重路由处理组。
  alias_or_related: Remote PG（g21）；拒收回退表（f24）
  tags: [concept, mutual-aid]

- id: g21
  term: Remote PG / Virtual Queue / Dedicated Pilot（分布式互助三对象）
  category: concept
  source_pages: p316-336
  source_quote: |
    "Remote PG • Processing Group of the local node, • Has a minimum waiting time threshold (distribution threshold)
    and a resource selection priority but no call selection priority. • Virtual Queue • … the image of the head of the
    normal queue … • Dedicated Pilot • Remote Pilot is dedicated to one Virtual Queue." (p319)
  definition: |
    分布式互助三件套：Remote PG（本地侧远端处理组，Type=Remote，有门限+资源优先级、无呼叫选择优先级）、虚拟队列
    （Type=Virtual，远端侧只映射队头呼叫特征）、专用 Pilot（一虚拟队列专属，可被多个 Remote PG 调用）。闭锁三条件：
    远端 Pilot GFWD/闭锁、下游方向全闭锁、链路无时隙。
  alias_or_related: 门限语义（principle p16）；维护命令 pildstctx/pgctx（g54）
  tags: [concept, remote-pg, virtual-queue]

- id: g22
  term: Transaction code（事务码）
  category: concept
  source_pages: p323, p534
  source_quote: |
    "Call services: • Transaction code • Automatic Wrap-up timer • Pause timer — All these services are those of the
    pilot on the destination node" (p323)
    "FormCod.xls transaction code (3digits) • FormCods.xls detailed transaction code (3digits)" (p534)
  definition: |
    坐席话机上按呼叫业务打的三位标记（随 Pilot 的呼叫服务下发，远端接续时遵循目的地节点 Pilot 的服务集），Excel 报
    表有专用模板（FormCod/FormCods）按码出报表。
  alias_or_related: Excel 模板体系（g50 相关、f33）
  tags: [concept, transaction-code]

- id: g23
  term: MCDU（OmniPCX 语音信箱号码）
  category: concept
  source_pages: p507
  source_quote: |
    "MCDU = OmniPCX voice mail directory number"
  definition: |
    Pilot 各类溢出/转发/闭锁地址指向的语音信箱目录号：把闭锁地址、全局转发地址、排队溢出地址、无应答溢出地址、转发地
    址配成 MCDU，即实现"呼叫最终落入与 Pilot 关联的信箱留言"。
  alias_or_related: Immediate forwarding to voice mail（g23 关联功能，p509）
  tags: [concept, voice-mail]

# ── 二、角色 (role) ──

- id: g24
  term: Agent（ACD 坐席）
  category: role
  source_pages: p33-35, p53-56, p124
  source_quote: |
    "Operator type + Agent … Skill set • Skill Nb.: 2 • Skill Level: 1 • Skill activation + True" (p124)
    "ACD station Select the ACD function of the set (i.e. Agent)" (p359)
  definition: |
    ACD 接续角色：挂处理组、带技能集（可设激活态）、可自助/被助登录。坐席话机需为 ACD 授权话机（ACD authorised phone
    set）或开 IP-Softphone 仿真；登录/登出受 COS 的 ACD Prefixes 放行。
  alias_or_related: Self-assigning agent（g26）；技能自管理（Manage skills=True，p125）
  tags: [role, agent]

- id: g25
  term: Supervisor（班长/监督员）
  category: role
  source_pages: p98-101, p511-512, p528
  source_quote: |
    "Administrator: has all rights • Supervisor: rights have to be granted • ACR rights for the supervisor" (p99)
    "The supervisor may listen to the agent conversation • Agent does not ear the supervisor" (p511)
  definition: |
    CC 侧监督角色：CCS 权限需逐项授予（ACR 相关=Advanced Call Routing 与 /ACR Data 两项）；话机侧可经 Help 键+坐席
    号做秘密监听/插入（Show Supervisor Listening、Help On External Call 控制）。
  alias_or_related: adm_acd option 4-2 可列 CCS 班长账户（p128）
  tags: [role, supervisor]

- id: g26
  term: Self-assigning agent（自助登录坐席）/ Preferred GT Agents
  category: role
  source_pages: p54-55, p144, p361
  source_quote: |
    "31500 is self-assigning agent, so he can choose the processing group to logon • Click on List to select the
    processing group" (p54)
    "Preferred GT Agents Select the processing group to complete logon (i.e. Agent2_PG)" (p144)
  definition: |
    两种登录形态：自助型坐席（31500/32500）登录时自己点 List 选处理组；非自助型（31501）登录即进偏好组（Preferred
    GT Agents，GT 书中未展开全称）。配置入口=CCS Configurations > Agent。
  alias_or_related: Agent logon 流程（c02/c03/c09）
  tags: [role, logon, gt-agent]

- id: g27
  term: mtcl（维护账户）
  category: role
  source_pages: p9, p51, p272
  source_quote: |
    "OXE CS1 … mtcl … Superuser2580*" (p9 实例表)
    "Enter the mtcl credentials: - login: mtcl - password: Superuser2580*" (p51，实验口径)
  definition: |
    OXE 维护级账户：WBM 管理（https://192.168.1.3 / 192.168.1.103）、console 命令（adm_acd、nano、dhs3_init、
    hybvisu 等）与 CCTA 导入示例均用它。root 仅用于 kill 进程等提权动作。口令为实验约定值。
  alias_or_related: acdsup 在 mtcl 下执行（p336）
  tags: [role, account, maintenance]

# ── 三、订阅/许可 (subscription) ──

- id: g28
  term: Feature level license（Monosite / Multisite）
  category: subscription
  source_pages: p42, p562, p574, p582
  source_quote: |
    "On Feature level license window, select Monosite." (p42)
    "1 \"monosite\" token used" (p562, p574)
  definition: |
    CCS 安装时选择的许可形态：Monosite（单站点，实验取值）或多站点。运行期在 Real Time > Licenses 可见占用（1 个
    monosite 令牌）。多站点组网（ABC 网络/远端互助）需对应多站点形态。
  alias_or_related: CCS 连接规模（g44）
  tags: [subscription, licensing, ccs]

- id: g29
  term: CCS 软件包（CCS Mono / CCS Multi / CCS Light）
  category: subscription
  source_pages: p405
  source_quote: |
    "Package id=77   CCS Mono        current=0       max=120 • Package id=102  CCS Multi       current=0       max=120
    • Package id=112  CCS Light       current=0       max=120"
  definition: |
    OXE 侧按连接类型计数的 CCS 软件包：adm_acd option 15 输出中 Mono/Multi/Light 各 max=120；终端接入类型（如
    CLIENT10 Type: CCS Mono）与包对应。配合 103 号包（RTI/WBI）构成接入许可视图。
  alias_or_related: RTI license（g30）
  tags: [subscription, licensing, packages]

- id: g30
  term: RTI license（103 号包 / WBI Licence）
  category: subscription
  source_pages: p388, p405
  source_quote: |
    "Real Time Interface (RTI) license (nb 103) is required on OXE for the RTI Connector • Check the license using
    \"spadmin\" under mtcl" (p388)
    "Package id=103  WBI Licence     current=0       max=100" (p405)
  definition: |
    OXE 侧实时接口许可（103 号包，包名 WBI Licence，上限 100）：RTI Connector 从 CCS 取数的许可前提。核对两法：
    mtcl 下 spadmin 或 adm_acd option 15。
  alias_or_related: SPM 数据链（g37）
  tags: [subscription, licensing, rti]

- id: g31
  term: Soft Panel Manager 许可族（FlexLM）
  category: subscription
  source_pages: p388
  source_quote: |
    "OTCC_STD_EDITION_SOFTPANEL License needed with the OTCCSE • SOFT_PANEL_NB_DISPLAYS License needed for each
    display • SOFT_PANEL_BUSINESS_DATA License needed to use BD Interface • ECCSTART Internal use"
  definition: |
    SPM 侧 FlexLM 许可四项：主许可（随 OTCCSE）、按显示端数量计的 SOFT_PANEL_NB_DISPLAYS、业务数据接口
    SOFT_PANEL_BUSINESS_DATA、内部用 ECCSTART。许可全程在线校验，失效即冻结统计更新。
  alias_or_related: 许可失效行为（n23）；FlexLM 服务器（g40）
  tags: [subscription, licensing, spm]

# ── 四、产品 (product) ──

- id: g32
  term: OmniTouch Contact Center Standard Edition（OTCC Standard）
  category: product
  source_pages: p1, p377
  source_quote: |
    "OMNITOUCH CONTACT CENTER STANDARD EDITION - R10.15 ADVANCED - EDITION 07" (p1)
    "Complete solution to monitor and display real-time statistics generated by OTCC." (p373)
  definition: |
    ALE 基于 OXE 的呼叫中心标准版（本书版本 R10.15）：CCD 矩阵 + CCsupervision + ACR/ASM 选项 + 网络互助 + Soft Panel
    Manager/CCTA 等外围。本教材为其 Advanced 级课程。
  alias_or_related: OXE（g33）；本教材版本 Ed07
  tags: [product, otcc]

- id: g33
  term: OmniPCX Enterprise（OXE）
  category: product
  source_pages: p7-9, p82, p302
  source_quote: |
    "Up to the 40 languages in the Alcatel-Lucent OmniPCX Enterprise" (p82)
    "Transit nodes can be: Alcatel-Lucent OmniPCX Enterprise with or without CCdistribution • Any PABX able to support
    (transparently) the ABC-F protocol (Alcatel-Lucent OmniPCX Enterprise, A4300M/L)" (p302)
  definition: |
    ALE 企业通信服务器（书内亦称 PABX/Call Server/PCX）：承载 CCD/AFE、Direct IP Link（节点间）、SIP 中继与话机；
    实验含本地/远程两节点（cs1/cs2）。A4300M/L 亦可作 ABC-F 透明中转节点。
  alias_or_related: OMS（g34）；WBM（Web 管理界面）
  tags: [product, oxe]

- id: g34
  term: OMS
  category: product
  source_pages: p7, p9, p51
  source_quote: |
    "OMS CS1 OTCC_OMS_LOCAL_NODE 192.168.1.13 … OMS CS2 OTCC_OMS_REMOTE_NODE 192.168.1.113" (p9)
    "Software Rack 3U (OMS) Rack N° 4 Virtual GD4 (slot 0) IP @: 192.168.1.13/24" (p51)
  definition: |
    OXE 机架/板卡形态中的软件机架实体（书中未展开缩写）：实验以 Software Rack 3U + Virtual GD4 板呈现（主站 Rack4
    192.168.1.13、远端 Rack3 192.168.1.113）。POD 定稿时核对其在役状态。
  alias_or_related: GD4（书中未展开，虚板名）；Rack/Boards 配置（c02）
  tags: [product, oms, hardware]

- id: g35
  term: MicroSIP
  category: product
  source_pages: p10, p52-53
  source_quote: |
    "3 MicroSIP softphones installed • MicroSIP – 31010 for internal calls • MicroSIP – 31011 for internal calls •
    MicroSIP – Public for public calls" (p10)
  definition: |
    实验用 Windows 软话机：Client10 上三实例（两个内部分机+一个公网用户，Public 实例按 POD 选 profile），SIP 密码
    123456（实验口径）；用于充当主叫/被叫做呼叫测试。
  alias_or_related: IPDSP（g36）；SIP 模拟器（g43）
  tags: [product, softphone, lab]

- id: g36
  term: IPDSP（IP Desktop Softphone）
  category: product
  source_pages: p10-11, p53-55
  source_quote: |
    "1 IP Desktop Softphone installed • 31000 terminal dedicated for agents" (p10)
    "Launch IPDSP softphone … Dial the extension number Enter the extension number (i.e. 31000) Dial the personal code
    Enter the personal code (i.e. 0000)" (p53)
  definition: |
    坐席软话机（缩写书中未展开，上下文为 IP Desktop Softphone）：以分机号+个人码注册，菜单含 LogOn/Logoff、CC 页
    （ACR manage/View 技能开关）等坐席功能；Client10=31000、Client11=31001 或 32000。
  alias_or_related: Agent 话机功能（g24）；ACR 主菜单（p126）
  tags: [product, softphone, agent]

- id: g37
  term: Soft Panel Manager（SPM）
  category: product
  source_pages: p371-383, p394
  source_quote: |
    "Complete solution to monitor and display real-time statistics generated by OTCC. • Dynamic synchronization of the
    OmniTouch CC configuration objects • Collection of statistics in real-time" (p373)
    "The limit of subscribed statistics … is 500 • … only 150 simultaneous connections • … Soft Panels and wallboards
    declared is limited to 200." (p394)
  definition: |
    OTCC 实时统计上墙方案：Tomcat Web 应用（wbm，默认端口 9060，admin/admin）+ LED 墙板/液晶/Panel PC/电视显示 + 邮
    件告警 + 业务数据接口（JMS/ActiveMQ）+ Web 服务外露。限制：订阅统计 500、并发连接 150、面板+墙板 200。
  alias_or_related: RTI Connector（g38）；显示 URL displayPanel.htm（f29）
  tags: [product, spm, wallboard]

- id: g38
  term: RTI Connector
  category: product
  source_pages: p377, p396-411
  source_quote: |
    "Data retrieval via RTI Connector which communicates with the Contact Center Supervision software installed on the
    system" (p377)
    "RTI Connector is a simple application that creates a link between a CCS and the Soft Panel Manager server. It gets
    data from the CCS and broadcasts them to the Soft Panel Manager server. It is installed as a service and starts
    automatically." (p405)
  definition: |
    连接 CCS 与 SPM 的 Windows 服务：启动即全量拉取 CCD 对象推送 SPM，断连每 5 秒重试，统计按需订阅（选用后最多 1 分
    钟生效）。配置文件 RTIConnector.ini（WBMHost/WBMPortNum/dataSubscriptionTimer=60）。
  alias_or_related: 同机共存警告（n21）；RTI 许可（g30）
  tags: [product, rti-connector]

- id: g39
  term: FlexLM Server
  category: product
  source_pages: p7, p388, p408-411
  source_quote: |
    "FLEXLM SERVER OTCC_FLEXLM Flex 192.168.1.80" (p9)
    "The Soft Panel Manager server must connect to a FlexLM license server to check its license. … By default, the
    Soft Panel Manager server will try to connect on the FlexLM server with \"localhost\" hostname and the port 27000." (p408)
  definition: |
    ALE 许可服务器（安装包 ALE-FLEXlmServer，LMTOOLS 管理，默认 localhost:27000）：SPM 启动与运行期持续校验许可；
    实验环境独立 FlexLM 虚机（192.168.1.80，root/letacla1）供 OXE 授权。
  alias_or_related: 许可族（g31）；LMTOOLS 验证步骤（c10）
  tags: [product, flexlm, licensing]

- id: g40
  term: Contact Center Ticket Analyser（CCTA）
  category: product
  source_pages: p480-497
  source_quote: |
    "The aim of the Contact Center Ticket Analyser is to display the data contained in the CCd communication and event
    ticket (files .Z)" (p482)
    "After installation, 2 tools are available: • The Importation … • The Ticket Tracer … located in \\Program
    Files(x86)\\Alcatel\\Ticket Analyser" (p484)
  definition: |
    CCd 票据离线分析工具（.Z 文件）：Importation 负责（每日自动）从 PCX 导入通信/事件两类票据；Ticket Tracer 负责可
    视化过滤分析并导出 ASCII。结束原因 40 种、呼叫类型 10 种。
  alias_or_related: 票据类型（f31）；导出（c12）
  tags: [product, ccta, reporting]

- id: g41
  term: CCS Server（serv_ccs / CCs Server 服务）
  category: product
  source_pages: p555-590
  source_quote: |
    "Internal CCs server: The process \"serv_ccs\" is started on the OmniPCX • 15 CCsupervision Clients … External CCs
    server: \"server CCs\" service is started on the PC • 120 CCsupervision Client" (p557)
    "The CCs server is mandatory for these releases when the CCs connections numbers to the PCX is greater than 9" (p567)
  definition: |
    CCsupervision 集中接入服务器：内部形态=OXE 上 serv_ccs 进程（serv_ccs_on_dhs=1，15 客户端）；外部形态=Windows
    Server 2019/2022 服务（serv_ccs.msi，120 客户端，自报 maxCli=150/maxConnected=120）。CCd R3.1+CCs 4.3.46.1 起连
    接数>9 强制使用；一 AFE 仅一 Server。
  alias_or_related: 切换流程（c15）；维护（adm_acd -servccs，g54）
  tags: [product, ccs-server]

- id: g42
  term: RLAB（Remote Lab）
  category: product
  source_pages: p3-14
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data center." (p5)
    "POD Common: NAS (Softs, licenses,..) SIP Simulator" (p5)
  definition: |
    ALE 远程实验平台：V-Class 班级下 POD 1..n（同构、互不可见）+公共 Pod（NAS 软件许可 + SIP 模拟器）；门户支持远程
    桌面/重启/控制台等实例操作。本教材全部实验的承载环境。
  alias_or_related: POD 拓扑（f02）；接入通道（f03）
  tags: [product, lab, rlab]

- id: g43
  term: ITSP1（公共 SIP 运营商模拟器）
  category: product
  source_pages: p15-18
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 … ITSP1 Public gateway public.itsp1.com 10.20.30.50 … SIP
    domain: sip.itsp1.fr" (p16)
    "Id: pbxP password: alcatel" (p16)
  definition: |
    RLAB 公共区的运营商模拟：SIP 网关（PBX 以 pbxP/alcatel 注册）+公网网关（模拟公网用户）+号码变换规则（3321PN 系
    列）。用于外呼环回与呼入测试，全部为教学约定值。
  alias_or_related: 号码规则（f04、p19）；外部 SIP 网关配置（c02）
  tags: [product, sip-simulator, lab]

# ── 五、协议 (protocol) ──

- id: g44
  term: ABC-F
  category: protocol
  source_pages: p36, p299-313, p341, p343
  source_quote: |
    "Node number/ABC-F Trunk Group Enter the node number of the remode OXE node (i.e. 2)" (p343)
    "Any PABX able to support (transparently) the ABC-F protocol (Alcatel-Lucent OmniPCX Enterprise, A4300M/L)" (p302)
    "Select Inter-Nodes Links> Logical Links (ABC-F)> Link_2 Direct IP Link" (p368)
  definition: |
    OXE 节点间网络链路协议（书中未展开全称；ABC Link=network link，链路对象为 Direct IP Link）：承载智能互助的 ACD
    信息交换（Pilot 状态、已听引导、真实等待时间、资源选择请求等）。中转节点须透明支持。维护入口=mgr 的 Inter-Nodes
    Links > Logical Links (ABC-F)。
  alias_or_related: hybvisu/compvisu（g54）；拒收回退（f24）
  tags: [protocol, abc-f, network]

- id: g45
  term: H.323 / RTP（节点间话音协议族）
  category: protocol
  source_pages: p341-342
  source_quote: |
    "Inter-node protocol H323....... yes • RTP Direct..................... yes • RTP Direct for H323 terminals.. no •
    Fast Start..................... yes • VAD (Voice Activity Detection): - G723/G729...... no - G711........... no •
    CNG (Comfort Noise Generation): no" (p341)
  definition: |
    Direct IP Link 的话音侧参数（compvisu sys 输出）：节点间协议 H.323、RTP Direct（终端级可分离）、Fast Start、
    VAD/CNG 开关；链路带宽档决定编解码集（High=G711/G722/OPUS/G729，Low=G729）。
  alias_or_related: hybvisu 带宽档（principle p20）
  tags: [protocol, h323, rtp]

- id: g46
  term: CSTA
  category: protocol
  source_pages: p74
  source_quote: |
    "CSTA filed for call identification"
  definition: |
    呼叫标识字段来源之一（书中未展开全称）：与 CLID、被叫号码、呼叫标签并列的呼叫特征化信息源，用于 ACR 脚本执行期
    的呼叫识别。
  alias_or_related: 呼叫特征化（f10）
  tags: [protocol, csta]

- id: g47
  term: JMS（Java Message Service）/ ActiveMQ
  category: protocol
  source_pages: p378
  source_quote: |
    "Business Data can be pushed to the Soft Panel Manager server using JMS (Java Message Services). The Soft Panel
    Manager server uses ActiveMQ as a JMS implementation"
  definition: |
    业务数据推送通道：外部系统把 KPI 经 JMS 推给 SPM 服务器（ActiveMQ 实现）；对应防火墙端口 61618。SPM 数据亦可经
    realTimeDataService Web 服务外露。
  alias_or_related: 端口清单（principle p24）
  tags: [protocol, jms, activemq]

- id: g48
  term: SSH
  category: protocol
  source_pages: p50, p493
  source_quote: |
    "SSH is enabled." (p50，OXE 预配置说明)
    "Use SSH Enable SSH if it's activated on OXE (not enabled)" (p493)
  definition: |
    OXE 侧可开启的安全壳通道：CCTA Importation 声明站点时按 OXE 实际开启情况勾选（实验未开启）。OXE console 实验走
    Guacamole/console mode 而非 SSH。
  alias_or_related: Console mode（f03）
  tags: [protocol, ssh]

# ── 六、资源/工具 (resource) ──

- id: g49
  term: Processing Group（处理组）
  category: resource
  source_pages: p133, p318-320, p344, p347-348
  source_quote: |
    "Directory number … Name … Type Enter the type of processing group (i.e. Agent)" (p133)
    "Type Enter the type of processing group (i.e. Remote) … Voice directory number … Data directory number" (p344)
  definition: |
    呼叫分配的落点对象，按类型分：Agent（坐席组）、IVR、Other（语音引导 Voice_guide_PG、转发 Forwarding_PG 等）、
    Remote（远端互助组）、Rerouting（重路由组，互助用）。属性差异：Remote 有门限+资源优先级，Rerouting 无呼叫选择优
    先级。
  alias_or_related: Remote PG（g21）；资源选择优先级（p15）
  tags: [resource, processing-group]

- id: g50
  term: Voice guide（语音引导）
  category: resource
  source_pages: p82, p366, p368
  source_quote: |
    "Waiting room voice guides / parking levels • Greeting guide + 6 parking levels" (p82)
    "Guide Number Enter the voice guide number (i.e. 685). # of diffusions Enter the number of diffusions (i.e. 2)." (p366)
    "The voice guide #685 \"There is no agent to answer you right now\" is broadcast twice and the call is released." (p368)
  definition: |
    队列/等待室/闭锁场景的语音资源：等待室为迎宾+6 泊位制，支持 40 种语言与按呼叫档案语言选择；PG 型引导（如 685）可
    设扩散次数后释放呼叫。预配置阶段已为两路 Pilot 下载。
  alias_or_related: 间隔引导音（g55）；闭锁 Voice Guide（n07）
  tags: [resource, voice-guide]

- id: g51
  term: Trunk Group / Time Slot（中继组与时隙）
  category: resource
  source_pages: p307, p513-514, p529-530
  source_quote: |
    "No Time Slot available" (p307)
    "Number of SIP accesses : 2 (31 x 2= 62 SIP trunks) … Max. % of trunks out CCD : 20" (p513)
  definition: |
    呼叫承载资源：SIP 中继组按接入数计（实验 2×31=62 条），业务预留（Max % of trunks out CCD）与 Pilot 限额
    （Trunk limitation）两级切分；ABC 链路上时隙（TS）耗尽是 Remote PG/智能互助被拒的原因之一。
  alias_or_related: 两级预留数学（principle p21）
  tags: [resource, trunk, time-slot]

- id: g52
  term: ACD prefix（ACD 前缀）
  category: resource
  source_pages: p346, p360
  source_quote: |
    "prefix ACD then 1 = unavailable … prefix ACD then 2 = Wrap up … prefix ACD then 3 = call supervisor … Prefix ACD
    then 5 = Logoff … Prefix ACD then 6 = Logon" (p346)
    "ACD Prefixes Enter a value to turn on the phone facility (i.e. 1)" (p360)
  definition: |
    坐席话机功能码总开关：建 CCD 对象前必须在 Translator > Prefix plan 建 ACD 前缀（实验=12），并在 Phone Features
    COS 放行；无显示屏话机靠"前缀+数字"完成 unavailable/wrap-up/呼班长/登出/登录。
  alias_or_related: COS（本条关联）；代接前缀（g53 同族）
  tags: [resource, acd-prefix]

- id: g53
  term: Prefix plan / DID translator（编号翻译资源）
  category: resource
  source_pages: p57, p314, p335, p343, p346, p503-504, p522-524
  source_quote: |
    "Translator/External Numbering Plan/Default DID num. translator" (p57)
    "Network prefix creation • Translator/Prefix Plan/Create … Prefix Meaning: Network No." (p335)
    "Prefix meaning: General Features • General features: Agent processing group call pick" (p503)
  definition: |
    Translator 下的号码翻译资源族：DID 翻译器（首外号/首内号/范围）、网络前缀（Network No.+节点号+类型，指向远端
    Pilot）、ACD 前缀、功能前缀（General Features：组内代接 #013/直接代接 #014）、Local Features（会话录音等）。
  alias_or_related: DID 规则（principle p19）；特殊功能前缀（c13）
  tags: [resource, translator, did]

- id: g54
  term: adm_acd / agacd / hybvisu / pildstctx / pgctx / acdsup（ACD 维护命令族）
  category: resource
  source_pages: p127-128, p176, p257, p336, p341-342, p583, p590
  source_quote: |
    "\"agacd\" command: agacd + Agent dir. number" (p127)
    "adm_acd <SRV_IP-@> -servccs … CCS Server release 8.0 cnx= 1, afe= 1" (p590)
    "Dedicated Pilot: pildstctx <pilot directory number> • Remote PG: pgctx <remote PG number>" (p336)
  definition: |
    mtcl 会话下的排障命令箱：adm_acd（对象清单/终端/许可/坐席统计 -salb 21、ASM 记忆 -salb 28、经服务器接入
    -servccs 10）、agacd（单坐席）、compvisu sys 与 hybvisu（链路）、pildstctx/pgctx（专用 Pilot/Remote PG 上下
    文）、acdsup（Remote PG 开闭）、spadmin（许可）。
  alias_or_related: 命令树详解（f15）；各实验内的用法（c08/c09/c15）
  tags: [resource, cli, maintenance]

- id: g55
  term: Inter-guide tone（间隔引导音）
  category: resource
  source_pages: p500, p521
  source_quote: |
    "Sending an inter-guide tone • Conditions • Congested waiting queues • No dissuasion option • Call parking …
    Inter-guide tone Number: 2" (p500)
  definition: |
    队列拥塞且无劝恼时向主叫送的音信号（默认 2 号音），替代泊位引导音；与 Redirection busy tone on DID 配合决定饱和
    时的客户听感。
  alias_or_related: 饱和行为（n29）；劝阻（g18）
  tags: [resource, tone]

- id: g56
  term: Navigator（CCS 实时视图）
  category: resource
  source_pages: p47, p147-148, p237, p336, p366
  source_quote: |
    "From the CCS main menu, select Real time > Navigator. You now view the OXE CCD array with the CCS application." (p47)
    "From the Displayed Objects menu, select Tab8 … Click on Record" (p148)
  definition: |
    CCS 实时菜单下的矩阵全景工具：多 Tab 页定制（Pilots/Queues/PGs 显隐 + Real Time Info 参数如 #Calls queued），
    用于连通验证（c01）、ACR 视图（c03）、等待室观察（c07）与远端矩阵（c09），也是 Remote PG 维护路径的 CCS 侧抓手。
  alias_or_related: 定制方法（f17）
  tags: [resource, navigator, real-time]
```

---

## 任务覆盖自检（task ↔ id 映射）

- 六类分布：concept 23 条（g01-g23）/ role 4 条（g24-g27）/ subscription 4 条（g28-g31）/ product 12 条（g32-g43）/ protocol 5 条（g44-g48）/ resource 8 条（g49-g56 计 8 条：g49 处理组、g50 语音引导、g51 中继、g52 ACD 前缀、g53 翻译族、g54 命令族、g55 引导音、g56 Navigator），合计 56 条编号 g01-g56。
- 书中未给全称的缩写（DDI/DID、ABC-F、GT、RSI、CSTA、MAO、OMS、GD4、TSC、COS、IPDSP、EWT/MWT、ITSP）均未编造 full_name，仅在 definition 里标注书内上下文用法。
- 任务映射：task-04/05（ACR/技能概念）→ g01/g03/g05/g09/g10/g11/g14/g16；task-08/09/10/11（脚本/LCA）→ g02/g04/g08/g12/g13/g15；task-12（网络互助）→ g20/g21/g44/g51；task-13/14（SPM）→ g31/g37/g38/g39/g47；task-15（CCTA）→ g40；task-18（CCS Server）→ g41/g28/g29；task-19（维护命令）→ g27/g54；环境类术语 → g42/g43/g35/g36/g34。
- 覆盖自检：id（g01-g56）连续无缺号；YAML 以 ``` 闭合；每条含 source_pages 与原文引用；alias_or_related 完成六类间交叉引用。
