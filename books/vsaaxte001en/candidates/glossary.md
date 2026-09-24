# 术语/缩写/产品名候选 — Visual Automated Attendant (VSAAXTE001EN Ed20, R4.8.006)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 58 条（concept 20 + role 2 + subscription/licensing 4 + product 14 + protocol 12 + resource 6）。
> CMIP/DPNSS/TUI/VXML/COS/ANI/Q931/ITSP/OMS/JDBC/SMTP/SNMP/FQDN/MAC/OPEX/CAPEX 等缩写书中未给全称，full_name 字段如实省略或仅注原文出处，不做外部补全。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: VAA
  full_name: Visual Automated Attendant（书名页完整拼写）
  category: concept
  source_pages: p1, p20-21, p42
  source_quote: |
    "VISUAL AUTOMATED ATTENDANT - R4.8.006 INSTALLATION, CONFIGURATION AND MAINTENANCE" (p1)
    "AUTOMATED 24/7 CALL ROUTING AND GREETING … Scalable software solution for small to extra-large
    businesses, multi-tenants and uses the SIP protocol … Security - compliance with CIS-2 Security Standards" (p20)
  definition: |
    全书主角：跑在 SUSE Linux 上的软件自动话务台/IVR——多租户、SIP 协议对接 OXE、7×24 呼叫路由与
    欢迎语，可接数据库或呼叫中心方案；带 FlexLM 许可服务、PostgreSQL 库、Web 管理面的整套服务器
    软件，宣称符合 CIS-2 安全标准。缩写 VAA 通篇使用。
  alias_or_related: 组件族见 g29-g34；对接对象见 g27 OXE
  tags: [concept, product-scope, core]

- id: g02
  term: Tree
  category: concept
  source_pages: p27, p144, p145
  source_quote: |
    "Routing scripts by a simple drag & drop of buildings blocks Easy configuration" (p144)
    "It is IMPERATIVE to personalize the NAME of each block when configuring a tree! This name is used
    by statistics and will facilitate the analysis" (p145)
  definition: |
    与路由号码绑定的呼叫处理脚本：在编辑器里拖拽积木块（节点）编排，负责放欢迎语、收号、按时间/
    主叫过滤、转接等完整流程。每个节点必须个性化命名——名称直接进统计与呼叫日志（逐节点记录）。
  alias_or_related: 原书混用 script / tree（p216 "dynamic scripts (trees)"）；节点见 g03；绑定见 g05
  tags: [concept, tree-editor, core]

- id: g03
  term: Node (building block)
  category: concept
  source_pages: p27, p144-162, p203
  source_quote: |
    "Tree design associated commands • Set default language • Play prompt • Business hours • Calendar •
    Menu • Transfer • Transfer to voicemail • Filter call • Jump to sub tree • Record prompt via TUI •
    Release call • Comments" (p27)
    "IVR options (Additional licenses) • Custom display name • Collect digit • Speech recognition • SQL
    Request • Correlator Data • Condition • HTTP request • Mail • Set Variable" (p27)
  definition: |
    树的基本积木：原生 12 种（Start、Select language、Announcement、Business hours、Calendar、Menu、
    Transfer、Voicemail、Filter、Go to tree、Record prompt、Release，另有 Comment 画布注释）+
    IVR 选项 9 种（另购许可，负责对接信息系统）。原书强调节点命名是统计排障的前提。
  alias_or_related: 原生节点讲义 p144-162、IVR 选项讲义 p203-213；IVR 许可见 g26
  tags: [concept, nodes, tree-editor]

- id: g04
  term: Tenant / Company
  category: concept
  source_pages: p24, p25, p38, p50
  source_quote: |
    "Independent time zones … DDI range … Directory assistance type … Extension length" (p24)
    "The super administrator can create companies • There is no limit about the number of companies" (p25)
    "The Visual Automated Attendant Media Server is shared by all companies • It's not possible to
    reserve ports for a given company" (p50)
  definition: |
    VAA 的多租户配置边界：每个公司独立时区、DDI 段（树号范围，可用内线号）、目录辅助类型、留言前缀、
    分机位长；公司资源含用户/路由/提示音/计划/目录/过滤器/树编辑器/统计。可与 OXE multi-company
    功能联动（细节外置 TBE083），但媒体服务器被各公司共享、不能按公司预留端口。
  alias_or_related: 公司四要素创建流见 framework f21；multi-company 集成边界见 counter-example n07
  tags: [concept, tenant, multi-company]

- id: g05
  term: Routing number
  category: concept
  source_pages: p28, p29, p111
  source_quote: |
    "Associate a DID number with a tree structure … Single number associates to a single tree • The
    routing of the numbers is to be done on the OXE side (Routing or ARS)" (p28)
    "Possible use but not recommended … • ?: to match any number • *: to match any number of digits •
    [firstNumber]-[lastNumber]: Assign a range of numbers to a tree structure - Recommended use for
    better readability • Assign a single number to each tree" (p29)
  definition: |
    把 DID 号码与树绑定的路由条目（Routing 菜单创建，点 Forbidden 图标切换激活态）。双层路由缺一不可：
    VAA 内绑号码到树，OXE 侧还要把呼叫经中继送进 VAA（routing 或 ARS）。推荐一号一树；通配符
    ?/*/号段"可用但不推荐"，歧义消解规则在 Administration Guide 4.3。
  alias_or_related: OXE 侧前缀计划（314→网络 10）见 framework f19；通配符边界见 counter-example n17
  tags: [concept, routing, numbering]

- id: g06
  term: Prompt
  category: concept
  source_pages: p28, p34, p138, p149
  source_quote: |
    "Prompts can be imported as wav-files, recorded via any telephone set or generated using TTS" (p21)
    "Format: 8KHz PCM 16-bits mono … Recording from a phone • From a number assigned to a specific
    system tree called '-Prompt Recording-'" (p34)
    "Prompt Recording: Integrated message recording application • User ID and secret code • Prompt ID
    available in « Prompts » menu" (p28)
  definition: |
    提示音资产，四个来源：WAV 导入（8KHz/PCM/16-bit/单声道，名称不能含空格）、电话录制（拨
    "-Prompt Recording-" 专属树号，需租户用户 ID+PIN）、TTS 生成、树编辑器/Prompts 页发起录制。
    Annoucement 节点另有 Server file 模式（放服务器本地音频），原书标注 not recommended。
  alias_or_related: 录音凭证边界见 counter-example n38；格式与命名硬约束见 n19；TUI 缩写未展开（p27）
  tags: [concept, prompts, audio]

- id: g07
  term: TTS
  category: concept
  source_pages: p34, p36, p140, p141
  source_quote: |
    "Free TTS engine embedded - PicoTTS (DE, GB, US, FR, ES, IT) •Paid (Licenses not provided by ALE)
    based on the number of characters •Google Cloud TTS" (p34)
    "The Pico TTS engine can be used free of charge and without an internet connection. But it is not
    recommended for production. - Google Cloud is recommended but NOT free (credit card required)" (p141)
  definition: |
    文本转语音：内置免费 PicoTTS（六语言 DE/GB/US/FR/ES/IT，官方明说"不建议生产"）与付费 Google
    Cloud TTS（按字符计费、需信用卡、许可不经 ALE，生产推荐）。在 Tenant/Settings → Text to speech
    页签激活引擎（如 TTS Pico），可在 Prompts 页或树节点内直接生成。
  alias_or_related: 引擎价格时效性原书自注可能过时（p141）；细节指向 Administration Guide 第 10 章；
  选型边界见 counter-example n20；ASR 见 g08
  tags: [concept, tts, cloud]

- id: g08
  term: ASR
  category: concept
  source_pages: p37, p42, p101, p154
  source_quote: |
    "Google speech to text service (Google Cloud account required) & API key required" (p37)
    "Note: G729 can't be used with Automatic Speech Recognition feature" (p42)
    "Quota (s): how many seconds of audio data to be sent to the speech recognition engine (for cost control)" (p154)
  definition: |
    语音识别：外部云引擎（Google speech-to-text，需 Google Cloud 账号 + API key），在公司设置配置。
    两种用法：菜单节点内的 ASR 菜单选择（词句映射按键，Full match 全匹配开关，Quota 秒数控成本）
    与"菜单+直拨"档（先匹配菜单词句、再查目录姓名）；也可经 Speech recognition 节点把识别结果存变量。
    硬约束：G729 编解码与 ASR 互斥，要用 ASR 必须 G711。
  alias_or_related: 互斥规则见 principle p09 / counter-example n02；识别节点见 p206
  tags: [concept, asr, cloud]

- id: g09
  term: Directory / Dial by name
  category: concept
  source_pages: p33, p156
  source_quote: |
    "To use the VAA dial-by-name feature, users must be created in the Directory tab • Directory
    management •Manual creation •OXE phonebook synchronization - An OXE synchronization deletes all
    created entries" (p33)
    "it is recommended to use a Text to Speech engine to manage them instead. Text to Speech for
    directory assistance can be configured in the tenant settings" (p33)
  definition: |
    按姓名拨号目录：手工创建或 OXE 电话簿同步（经 CMIP 链路，p42）——同步是破坏性的，会删除全部
    手工条目。目录辅助作为 Transfer 节点目的地时，VAA 让 caller 用 DTMF 输名字并播报候选，各姓名的
    语音指引建议用 TTS 生成（在租户设置配置）。
  alias_or_related: 破坏性同步见 counter-example n18；CMIP 见 g45
  tags: [concept, directory, destructive]

- id: g10
  term: Filter
  category: concept
  source_pages: p32, p159
  source_quote: |
    "A filter can be created by importing a CSV file or entering an expression • A CSV import deletes
    all created entries" (p32)
    "Unknown ANI: Check to add unknown call ID (blocked numbers) to the list of filtered numbers" (p159)
  definition: |
    按主叫号码的过滤器：CSV 导入或表达式创建（CSV 导入会清空已有条目）；Filter 节点命中走 Filtered
    连线、未命中走 Unfiltered；菜单/转接节点也可挂过滤（多过滤模式、反向过滤）。Unknown ANI
    （未知主叫）可勾选纳入过滤名单。
  alias_or_related: ANI 缩写未展开；反向过滤语义见 p153；UC2 实验见 case c09
  tags: [concept, filter, caller-id]

- id: g11
  term: Schedule (Calendar & Business hours)
  category: concept
  source_pages: p30, p31, p135
  source_quote: |
    "Bank holidays • Holiday periods / Closures / and exceptional openings • Several calendars can be
    used for the same tree • 'Schedule' tab" (p30)
    "Manage business hours •Time zone configuration •Weekdays •Open/Close operational hours •Manage
    from the 'tree editor' or in 'Schedule' tab" (p31)
  definition: |
    时间类路由依据：日历（闭假日，可多日历用于同一树）与营业时间（时区/星期/时段），既可在 Schedule
    页签集中维护，也可在树内 Business hours/Calendar 节点自定义。UC2 的设计铁律：日历/营业时间/
    过滤器必须先于树创建。
  alias_or_related: 依赖物先行纪律见 principle p15；实验参数见 case c06
  tags: [concept, calendar, business-hours]

- id: g12
  term: Master / Slave
  category: concept
  source_pages: p44, p47, p82, p240
  source_quote: |
    "High availability is made of one Master VAA and one slave VAA … The VAA database is replicated
    from master to slave … The slave VAA database is in ReadOnly mode. Therefore, no statistics will be
    recorded for a call handled during the failure period on the PCS side." (p44)
    "No database synchronisation will be performed when master VAA will be recovered. Web client must
    reconnect (to Slave VAA)." (p47)
  definition: |
    VAA 双机高可用：数据库 Master→Slave 定期复制，Slave 只读（无统计）；OXE 用 ARS 双路由表完成
    呼叫切换（VAA 自身不做漂移）。行为口径：任何切换丢进行中呼叫；Master 恢复后不自动回同步（要
    vaa ha resync）；Web 客户端需手动重连。HA 配置一律从 master 发起（vaa ha addslave）。
  alias_or_related: 行为规则集见 principle p23；命令族见 p24；OXE 侧切换见 g17 ARS
  tags: [concept, ha, redundancy, core]

- id: g13
  term: Reference VAA (N+1 redundancy)
  category: concept
  source_pages: p51
  source_quote: |
    "N+1 redundancy is made of a 'reference VAA' and several other VAAs. The 'reference VAA' serves as
    configuration basis for all VAAs … When one VAA becomes unavailable, ARS mechanism routes the calls
    to other VAAs (N+1 principle) … If 'reference VAA' becomes unavailable, the other VAAs continue to
    operate but any configuration changes is impossible" (p51)
  definition: |
    N+1 扩容型冗余：一台 reference VAA 作配置基准（脚本/提示音/日历等周期复制到其他 VAA，各自统计
    除外），ARS 按 N+1 原则把呼叫分给可用 VAA。单台故障期间总容量下降；reference 挂了其余照跑但
    全系统配置冻结。与 Master/Slave（冗余型）是两种不同结构。
  alias_or_related: 对照 g12；配置冻结边界见 counter-example n06
  tags: [concept, n+1, redundancy]

- id: g14
  term: PCS
  category: concept
  source_pages: p49, p301, p302, p303
  source_quote: |
    "Main VAA manages the peripheral areas … Configuration of the central VAA connected to CS is copied
    toward all the VAA-PCS databases in a regular basis. On network failure, PCS becomes active. PCS VAA
    establishes the SIP Trunk with the PCS and manages local calls." (p49)
    "PCS VAA can be configured for local emergency purposes. Anyway, configuration will be lost once
    network failure is solved." (p49)
  definition: |
    远端外围站点的 VAA（全书未展开全称）：平时从中心 VAA 周期复制库（DB Import/Export），断网时
    激活并与本地 PCS 建中继接管本地呼叫；断网期间做的本地应急配置在网络恢复后即丢失。同步实现：
    vaa conf pcs [IP@] + vaa db sendBackup，每天 01:00 起 cron 依次错开执行。
  alias_or_related: 同步时序与默认值见 principle p33；配置丢失边界见 counter-example n09
  tags: [concept, pcs, synchronization]

- id: g15
  term: S.O.T
  full_name: software Orchestration tool（p76 括注展开）
  category: concept
  source_pages: p76, p77, p78, p110, p310
  source_quote: |
    "AUTOMATICALLYWith S.O.T (software Orchestration tool) • the S.O.T will perform the following steps:
    boot DVD installation, network configuration, default password modification, license configuration
    if the license has been provided and VAA installation." (p76)
    "If the VAA is installed by the S.O.T tool, the parameter 'incoming username' will be set at 'vaa'
    in the VAA configuration file." (p110)
  definition: |
    自动化安装/升级工具：装系统、配网、改默认密码、装许可、装 VAA（物理机或虚机均可）；填写项见
    p78（admin/root 密码须 20 位含大写/数字/特殊字符、键盘、国家、主机名、MAC、IP）。特殊口径：
    S.O.T 安装只能用自签证书、incoming username 固定为 "vaa"；也可经它做自动升级（p310）。
  alias_or_related: 证书限制见 counter-example n11；安装参数对照 principle p03/p08
  tags: [concept, installation, automation]

- id: g16
  term: incoming username
  category: concept
  source_pages: p81, p101, p109, p110
  source_quote: |
    "Define an incoming username which will also be entered in the external SIP gateway" (p81)
    "The parameter 'incoming username' must be defined in the SIP external gateway, you must define the
    same username! - Username: vaa1 - No Password, leave blank - The parameter 'Minimal authentication
    method' must be set at - None" (p101)
  definition: |
    VAA 安装时定义、必须与 OXE 外部 SIP 网关完全一致的对接用户名（无密码留空、最小认证方式 None、
    网关类型选 VAA）——双侧一致是接通的关键开关。实验值 vaa1/vaa2；S.O.T 安装固定为 "vaa"。
    事后修改用 vaa conf telephony。
  alias_or_related: 契约规则见 principle p10；实验值见 case c02/c03/c16
  tags: [concept, sip, credential, troubleshooting]

- id: g17
  term: ARS
  full_name: Automatic Route Selection（书中仅以菜单路径 automatic route selection 出现，p265/p496；正文未作缩写展开）
  category: concept
  source_pages: p28, p44, p86, p242, p265-271
  source_quote: |
    "The routing is performed by OmniPCX Enterprise based on an ARS routing table • When Master VAA goes
    down, ARS mechanism routes calls through SIP Trunk 2 on the Slave VAA" (p44)
    "When you have a configuration with 2 servers in HA mode • You need to use ARS to route the calls
    from OXE" (p86)
  definition: |
    OXE 侧的自动路由选择表：VAA 的"高可用切换"实际由它实现——Master/Slave 各建一条 SIP 中继，ARS
    路由表选路、主 VAA 宕机时把呼叫切到 Slave 中继（首呼有判延）。OXE 侧 HA 实验含 Route list/
    Route 1/Route 2/Time Based Route List 与 ARS 前缀（21）。
  alias_or_related: VAA 的"高可用"其实在 OXE（BOOK_OVERVIEW 命题 8）；配置链见 framework f26/c17
  tags: [concept, oxe, routing, ha]

- id: g18
  term: Discriminator
  category: concept
  source_pages: p262, p263
  source_quote: |
    "Create a discriminator for routing allowed numbers to VAA1 or VAA2 … Discriminator No. Enter
    number: 11 name VAA" (p262)
    "The discriminators are used to define the authorized numbers for the calling stations when taking
    the trunk group (professional trunk group socket prefix or ARS professional trunk group socket prefix)" (p262)
  definition: |
    OXE 编号识别符（实验 11/VAA）：定义主叫在占用中继组时被放行的号码；HA 实验里配识别规则放行
    314 开头五位号、挂 ARS route list 11，并在 entity 1（分机）与 entity 0（中继）的 discriminator
    selector 条目 05 挂接。纯 OXE 侧编号计划概念。
  alias_or_related: 配套 NPD 见 g19；实验步骤见 case c17
  tags: [concept, oxe, numbering, ha]

- id: g19
  term: NPD
  full_name: Numbering Plan Description（p264 标题展开）
  category: concept
  source_pages: p264, p267
  source_quote: |
    "The NDP describes how to translate the numbers received from the external network and how to
    construct the numbers called to this external network … Description id Enter a new number: 56
    name VAA • Calling num plan id NPI/TON: ISDN Unknown • Called num plan id NPI/TON: ISDN Unknown" (p264)
  definition: |
    OXE 编号计划描述（实验 id 56/VAA）：定义外部网络来话号码翻译与去话号码构造；HA 实验中被 ARS
    Route 1/Route 2 引用（NPD identifier 56）。NPI/TON 缩写书内未展开。
  alias_or_related: 与 g18 Discriminator 同属 OXE 编号计划链路
  tags: [concept, oxe, numbering, ha]

- id: g20
  term: Purple On Demand / OPEX / CAPEX
  category: concept
  source_pages: p46, p76, p305
  source_quote: |
    "Spatial redundancy is not supported in Purple On Demand solution" (p46)
    "OPEX oriented license management mechanism based on Purple On Demand offer … VAA must be connected
    to a cloud connected OXE and be associated to only one subscription … License items values will be
    checked every night at midnight, whatever the working mode, CAPEX or OPEX" (p305)
  definition: |
    按用量许可池模式：VAA 须连云化 OXE 且只关联一个订阅；项目内声明的 VAA 端口在全部 VAA 应用间
    分摊，须在每台服务器上指定可用端口数；无论 CAPEX 还是 OPEX，许可项每晚午夜校验一次。
    OPEX 与空间冗余（跨数据中心 Slave）互斥。
  alias_or_related: 互斥边界见 counter-example n08；另见 principle p32
  tags: [concept, licensing, opex]

# ── 二、VAA 内角色 (role) ──

- id: g21
  term: Super administrator / Administrators
  category: role
  source_pages: p22, p25, p26, p128
  source_quote: |
    "The super administrator can create companies • There is no limit about the number of companies" (p25)
    "Some Administration roles • Companies' management • Routing (Full) • Users' management - Can create
    some user accounts, but no administrator accounts" (p26)
    "BY DEFAULT THE PASSWORD OF THE NEW ACCOUNT IS IDENTICAL TO THE IDENTIFIER OF THE LATEST." (p128)
  definition: |
    VAA 管理角色体系：超管可建公司（数量不限）；管理类角色含公司管理、全量路由、用户管理（能建
    普通用户但建不了管理员）；另可在 Users 页给每人派功能角色。新建管理员默认密码=其用户名（原书
    Warning 大写强调），建完必须立即改密；管理员锁 2 小时自动解锁或 vaa conf unlockAdmin 全解。
  alias_or_related: 默认 admin/admin 见 g01 关联的 principle p04；弱口令边界见 counter-example n13
  tags: [role, administrator, security]

- id: g22
  term: Advanced user profile（受限用户档案）
  category: role
  source_pages: p21, p145
  source_quote: |
    "Advanced user profile gives access to a limited part of the management such as the greeting prompt
    control" (p21, p145 同文重现)
  definition: |
    受限用户档案：只开放管理面的局部功能（书中举例"问候语控制"），用于把季节性改欢迎语这类操作
    下放给非管理员。全书仅此一句定义，无配置实验。
  alias_or_related: 功能类角色（Routing/Prompts/Directory/Filters/Calendar management）见 p26，已并入 g21
  tags: [role, profile, delegation]

# ── 三、许可体系 (subscription/licensing) ──

- id: g23
  term: FlexLM license（.lic / .vaa）
  category: subscription
  source_pages: p95, p249, p274
  source_quote: |
    "The license file (.lic or .vaa) is linked to the MAC address of the VAA • Installation directory
    •/etc/ale/aa-license-server • In case of problem, check the license file in the directory
    •/var/lib/ale/aa-license-server/ • You must find: • The FQDN • MAC address" (p274)
    "The FQDN will be used in the license file" (p249)
  definition: |
    VAA 许可文件（.lic 或 .vaa 扩展名）：绑定服务器 MAC 地址且须含正确 FQDN——改主机名/换网卡即失效。
    安装目录 /etc/ale/aa-license-server，排障目录 /var/lib/ale/aa-license-server/；安装时许可传 /tmp
    由 install.sh 自动识别。用 more 查看 FEATURE 项核对内容与到期日。
  alias_or_related: FEATURE 四项见 g25；许可失效边界见 counter-example n30；FlexLM = aa-license-server
  使用的许可服务（p277）
  tags: [subscription, licensing, troubleshooting]

- id: g24
  term: VAA_RELEASE / Release 11
  category: subscription
  source_pages: p89, p253, p274
  source_quote: |
    "Important information to read carefully before installing VAA 4.8.006: … A new license (Release 11)
    is required." (p89)
    "VAA_RELEASE : [11] ✔" (p253)
    "FEATURE VAA_RELEASE ALCFIRM 1.0 04-jul-2025 9 HOSTID=ANY …" (p274)
  definition: |
    许可版本项：4.8.006 强制新许可 Release 11（旧许可失效）。注意书内两处数值不一致——p253 的
    vaa services 显示 VAA_RELEASE [11]，p274 的 .lic 样例 VAA_RELEASE 为 9（样例文件早于换版）；
    排障以 vaa services 实际输出为准。
  alias_or_related: 版本陷阱详见 counter-example n01；FRAMEWORK f18/c02 均按 p89 口径
  tags: [subscription, licensing, version]

- id: g25
  term: AAIVR / AAPORTS / ECCSTART（FEATURE 项）
  category: subscription
  source_pages: p274, p253
  source_quote: |
    "FEATURE AAIVR ALCFIRM 1.0 18-may-2027 1 HOSTID=ANY … • FEATURE AAPORTS ALCFIRM 1.0 04-jul-2025 5
    HOSTID=ANY … • FEATURE ECCSTART ALCFIRM 1.0 04-jul-2025 5 HOSTID=ANY …" (p274)
    "VAA_PORTS : [5] ✔ … VAA_IVR : [true] ✔" (p253)
  definition: |
    .lic 文件内的 FEATURE 清单：AAIVR（IVR 功能）、AAPORTS（端口数，实验 5）、ECCSTART、VAA_RELEASE
    （许可版本，见 g24），各带到期日。运行态对应物是 vaa services 输出的 VAA_PORTS / VAA_IVR /
    VAA_RELEASE 三项——巡检一眼看许可。
  alias_or_related: 端口达到许可上限触发邮件告警（p282）；VAA_PORTS 实验值 5 为实验口径
  tags: [subscription, licensing, feature]

- id: g26
  term: IVR Options（Additional licenses）
  category: subscription
  source_pages: p21, p27, p203
  source_quote: |
    "Option • High availability • IVR • Call qualification • Database read and write • HTTP(s) request •
    SQL request (r/w) • Digit collection • Speech recognition • Test on condition • Custom display name •
    Email" (p21)
    "Options subject to licenses allowing the VAA server to be connected to an information system" (p203)
  definition: |
    另购许可解锁的节点族（9 种，见 g03）：自定义显示名、收号、语音识别、SQL 读写、相关数据、条件、
    HTTP 请求、邮件、变量——定位是"让 VAA 连接信息系统"。许可有无可在 vaa services 的 VAA_IVR
    字段核查。HA（High availability）也列在 Option 栏（p21）。
  alias_or_related: 运行态核查见 g25；节点讲义 p203-213
  tags: [subscription, licensing, ivr]

# ── 四、产品/组件/工具 (product) ──

- id: g27
  term: OXE
  full_name: OmniPCX Enterprise（p42 完整拼写）
  category: product
  source_pages: p42, p43, p85, p107
  source_quote: |
    "VAA is connected to the OmniPCX Enterprise using a SIP trunk of ABC/F Type" (p42)
    "The SIP configuration must be done manually in the OXE, which means that you must create the SIP
    trunk group, the external gateways, manage the local SIP gateway, the proxy..." (p107)
  definition: |
    ALE 企业级 PBX（本书对接对象）：保留呼叫控制与路由，经 ABC/F 型 SIP 中继把被叫号码对应的呼叫
    交给 VAA 执行脚本，并把 VAA 的转接落地。OXE 侧配置全书手工（trunk group/外部网关/信任 IP/路由/
    编号计划），默认读者已会 OXE 运维（netadmin -m、mtcl、trkstat 等）。
  alias_or_related: 对接五段链见 framework f19；OXE 冗余三用例见 p45-48
  tags: [product, pbx, oxe]

- id: g28
  term: OMS
  category: product
  source_pages: p7, p9, p65
  source_quote: |
    "OMS VSAA_OMS 192.168.1.13 … admin Superuser2580*" (p9)
    "Racks are created in the OXE database. Here we need only the OMS. … Software Rack 3U (OMS) Rack N° 4
    Virtual GD4 (slot 0) IP @: 192.168.1.13/24" (p65)
  definition: |
    实验拓扑中的 OXE 管理服务器虚机（全书未展开全称）：VSAA_OMS，192.168.1.13，机架表现为 Software
    Rack 3U + Virtual GD4 slot 0。纯实验基础设施。
  alias_or_related: POD 全景见 g54 RLAB
  tags: [product, lab, oxe]

- id: g29
  term: aa-media-server
  category: product
  source_pages: p54, p132, p277, p281
  source_quote: |
    "aa-media-server Manage the SIP connection with the OXE, and the RTP stack" (p54)
    "aa-media-server Application that connect to the OXE using the SIP and run the VAA scripts" (p277)
  definition: |
    核心服务之一：经 SIP 连 OXE 并承载 RTP 媒体栈、跑 VAA 脚本。日志为 /logs/aa-media-server/
    aa-media-server.log（主日志）与同目录 aa-softcmp.log（SIP 库踪迹，Web 界面 Logs 页对应
    "softcmp (SIP)"）。
  alias_or_related: secureCall 证书在其目录下（VAACertificate.jks / OXECertificate.pfs，p289）
  tags: [product, service, sip]

- id: g30
  term: aa-webapp (aa-management / aa-engine)
  category: product
  source_pages: p54, p132, p277, p320
  source_quote: |
    "aa-webapp A tomcat java web application server, that host two web app. • aa-management is the web
    application to manage the VAA, the main end-user interface with the system. • aa-engine is an
    application that run in close collaboration with the media-server to retrieve the VAA scripts from
    the database." (p54)
    "sudo systemctl restart aa-webapp" (p320)
  definition: |
    Tomcat Java Web 应用服务，承载两个 Web 应用：aa-management（管理界面）与 aa-engine（VXML server，
    与 media-server 协作从库取脚本）。JDBC 驱动装在其 lib 目录（/opt/ale/aa-webapp/lib，装后 restart
    aa-webapp 生效）；日志 /logs/aa-engine/aa-engine.log 等。VXML 缩写书内未展开。
  alias_or_related: JDBC 驱动清单见 principle p22
  tags: [product, service, webapp]

- id: g31
  term: aa-license-server
  category: product
  source_pages: p54, p277
  source_quote: |
    "aa-license-server Manage licenses" (p54)
    "aa-license-server FlexLM license server" (p277)
  definition: |
    FlexLM 许可服务：加载并校验 .lic/.vaa 许可文件，vaa services 输出中的许可要点（VAA_PORTS/
    VAA_IVR/VAA_RELEASE）即由它报告。问题排查目录 /var/lib/ale/aa-license-server/。
  alias_or_related: 许可文件细节见 g23；FlexLM 全称即 FlexLM（产品名，p277）
  tags: [product, service, licensing]

- id: g32
  term: tts-hub
  category: product
  source_pages: p54, p100, p132, p281
  source_quote: |
    "tts-hub Service to access TTS and Speech Recognition service" (p54)
    "tts-hub (Text to speech & Speech Rec): logs about the service which accesses TTS and Speech
    Recognition service" (p132)
  definition: |
    TTS 与语音识别服务的统一接入服务：install.sh 阶段即启用（systemctl 启用 tts-hub，p100）；日志在
    /var/log/ale/tts-hub/tts-hub.log，Web 界面 Logs 页对应 "tts-hub" 类型。
  alias_or_related: 引擎选型见 g07/g08
  tags: [product, service, tts]

- id: g33
  term: Nginx
  category: product
  source_pages: p54, p100, p277, p288
  source_quote: |
    "Nginx Configured as an HTTP reverse proxy to the web app" (p54)
    "nginx Local http proxy. Make the management webapp available on port 80" (p277)
    "vaa cert backup <file.sql.gz> … HTTPS configuration backup involving the following elements • Folder
    /etc/nginx/certificate • File /etc/nginx/nginx.conf • File /etc/nginx/conf.d" (p288)
  definition: |
    HTTP 反向代理：让管理 Web 应用可用（安装期证书也放 /etc/nginx/certificate/，自签时生成
    certif_nginx.crt + nginx.key）。证书级备份（vaa cert）覆盖其证书目录与配置。
  alias_or_related: vaa stop/fullstop 的差别就在是否保留 postgresql 与 nginx（p278）
  tags: [product, service, proxy]

- id: g34
  term: PostgreSQL
  category: product
  source_pages: p54, p277, p102
  source_quote: |
    "Postgresql A postgresql 16 database, storing the prompts, the routing strategies defined in the VAA,
    as well as the statistics generated by caller activities" (p54)
    "Enter a new password for your postgresSQL user 'postgres'" (p102)
  definition: |
    PostgreSQL 16 数据库：存提示音、路由策略与 caller 活动统计——三级备份/恢复与 HA 复制的主体。
    install.sh 阶段设 postgres 用户口令（实验 Superuser1234*）；日志在 /var/lib/pgsql/data/log。
  alias_or_related: 备份命令族见 principle p25；密码实验值为实验口径
  tags: [product, database]

- id: g35
  term: SUSE（Suse-base Linux）
  category: product
  source_pages: p52, p88, p89
  source_quote: |
    "Suse-base Linux" (p52)
    "The installation of the operating system (Suse) is carried out using the ALE Boot DVD. Installation
    can be performed on a physical machine or on a virtual machine." (p88)
  definition: |
    VAA 的操作系统底座：经 ALE BootDVD（或 ISO）安装 SUSE，物理机/虚机均可；实验从预装系统的虚机
    起步。兼容的 Hypervisor 三档见 principle p02。
  alias_or_related: 安装介质见 g55 ALE BootDVD
  tags: [product, os, suse]

- id: g36
  term: XCA
  category: product
  source_pages: p59, p60, p123
  source_quote: |
    "To create certificates for the lab, the certification authority XCA has been used •
    https://hohnstaedt.de/xca/index.php • The web site provides the software, tutorials and documentation." (p59)
    "In the lab, the RootCA has been exported as 'XCA.crt', This file must be copied in the PC trust store" (p59)
  definition: |
    实验用私有 CA 工具（开源软件）：建 RootCA（SHA-256、RSA 4096、填签发者信息）与 VAA 证书
    （SAN 必须含 VAA IP 与 DNS 名、CN 必填如 vaa1.company.com，导出 vaa1.pfx）；RootCA 导出 XCA.crt
    装入 PC 信任库。参数须按客户环境调整。
  alias_or_related: 证书体系全流程见 framework f13 / case c04
  tags: [product, certificate, pki]

- id: g37
  term: IPDSP
  category: product
  source_pages: p10, p66, p67, p172
  source_quote: |
    "1 IPDSP to be put into service" (p10)
    "31000 Brad Barkley IP DSP Main Installed on PC Client 10 … Password: 0000" (p66)
  definition: |
    ALE 的 IP 桌面软话机（书内写作 IPDSP / IP DSP，全称未展开）：实验主用软话机，占分机 31000
    （Brad Barkley，密码 0000 实验口径），在 UC1/UC2 里充当被转接目的地与 VIP 主叫。纯教学基础设施。
  alias_or_related: 对照 g38 MicroSIP
  tags: [product, lab, softphone]

- id: g38
  term: MicroSIP
  category: product
  source_pages: p10, p67
  source_quote: |
    "6 MicroSIP softphones are installed • 2 MicroSIP softphones to simulate public incoming calls and
    emergency calls • 4 MicroSIP softphones for internal deskphones" (p10)
    "31001 Billy Backman SIP extension Main Installed on PC Client 10 …" (p67)
  definition: |
    第三方 SIP 软话机客户端（实验 PC 预装 6 个）：4 个内部用（31001-31004，UC 实验里当主叫/占忙），
    2 个模拟公网来话与紧急呼叫。纯教学基础设施。
  alias_or_related: ITSP1 外呼回环见 g39；树实验测试全部靠它（c08-c15）
  tags: [product, lab, softphone]

- id: g39
  term: ITSP1
  category: product
  source_pages: p15, p16, p17
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 … Id: pbxP - password: alcatel … SIP domain:
    sip.itsp1.fr" (p16)
    "Dialed number: 0210341002 or 33210341002 External call (loop) … Number sent by the PBX:
    +33210341002" (p17)
  definition: |
    SIP 运营商模拟器（Public Carrier，托管在 RLAB 公共区）：SIP 网关 gateway1.itsp1.com（10.20.30.51，
    PBX 注册账号 pbxP/alcatel）+ 公网网关 public.itsp1.com（10.20.30.50）+ SIP 域 sip.itsp1.fr；
    号码规则带 POD 号 PN（安装号 3321PN、外线首号 41000、内线首号 31000），外呼走回环。OXE 侧只需
    填 Registration ID 与 Outgoing username = pbxP。实验口径，生产行为与真实运营商有差异。
  alias_or_related: ITSP2 仅在拓扑图出现（p16），无细节；实验坑（Direct RTP）见 counter-example n41
  tags: [product, lab, sip-trunk]

- id: g40
  term: MS SQL Express / SSMS
  category: product
  source_pages: p326, p327, p329
  source_quote: |
    "MS SQL Express 2019 ONLINE: https://www.microsoft.com/en-US/download/details.aspx?id=101064" (p327)
    "Install Management Studio: 'Install SSMS' by clicking in the previous window Or Download directly:
    https://aka.ms/ssmsfullsetup • MS SQL Server Management Studio language must match your system language" (p329)
  definition: |
    外部数据库实验用的免费微软数据库（2019 版）及其管理工具 SSMS（SQL Server Management Studio，
    p329 全称同页出现）：Basic/Advanced/LocalDB 三种离线包（约 249/790/53MB）。三个默认值陷阱
    （TCP/IP 禁用、1433 不再预分配、首登仅 Windows 认证）见 counter-example n27；整章定位是测试库
    搭建，生产由客户 DBA 承担。
  alias_or_related: 搭建步骤见 case c19；关键数值见 principle p35
  tags: [product, database, microsoft]

# ── 五、协议与技术名 (protocol) ──

- id: g41
  term: SIP trunk (ABC/F)
  category: protocol
  source_pages: p42, p107, p108
  source_quote: |
    "VAA is connected to the OmniPCX Enterprise using a SIP trunk of ABC/F Type" (p42)
    "Trunk group type Select type T2 ('type 'T2') … Q931 signaling variant Select ABC-F … Specificity T2
    Select SIP • Homogeneous network for direct RTP No" (p107)
  definition: |
    OXE 与 VAA 间的 SIP 中继：T2 型中继组、Q931 变体选 ABC-F（缩写书内未展开）、远端网络号独立、
    直连 RTP 否；局部设置端到端拨号/DTMF 端到端/Always VoIP，SIP virtual access 默认 2。SIP 本身的
    TLS 加密为可选项（g43）。
  alias_or_related: Q931、RTP 缩写未展开；中继状态排障 trkstat（f20）
  tags: [protocol, sip, trunk]

- id: g42
  term: G711 / G729 / G723
  category: protocol
  source_pages: p42, p101, p113
  source_quote: |
    "Visual Automated Attendant supports G711 (aLaw/µLaw), and G729. Note: G729 can't be used with
    Automatic Speech Recognition feature" (p42)
    "If you are unsure about this setting, select G711a, G711mu and G729" (p101)
    "Compression algorithm G729 is needed on the OXE side to match the configuration made during the
    installation on the VAA side. From OXE N2, compression algorithm G729 is enabled by default. It has
    replaced the G723 one which is phase-out." (p113)
  definition: |
    语音编解码：VAA 支持 G711（aLaw/µLaw）与 G729；G729 与 ASR 互斥（要用语音识别必须 G711），
    不确定就三个全勾。OXE N2 起 G729 默认启用（替代已淘汰的 G723），通常 OXE 侧无需动手。
  alias_or_related: 互斥规则见 principle p09 / counter-example n02；匹配核对见 n47
  tags: [protocol, codec, asr]

- id: g43
  term: SIP TLS / SRTP / secureCall
  category: protocol
  source_pages: p42, p102, p289
  source_quote: |
    "The SIP Trunk between Visual Automated Attendant and OmniPCX Enterprise can be encrypted." (p42)
    "SIP-TLS and SRTP secure Call option is disable. Valid certificates for OXE and VAA are required to
    activate this feature" (p102)
    "secureCall configuration backup involving the backup of • Configuration file /etc/ale/vaa.conf •
    Certificate file /opt/ale/aa-media-server/VAACertificate.jks • Certificate file
    /etc/ale/aa-media-server/OXECertificate.pfs" (p289)
  definition: |
    中继加密可选项（书中称 secure Call / secureCall）：激活需 OXE 与 VAA 双方有效证书；实验一律选 N。
    vaa full 备份覆盖其两本证书（VAACertificate.jks / OXECertificate.pfs）。管理面加密见 g44。
  alias_or_related: 实验关闭安全项的批判见 BOOK_OVERVIEW 批判节；SRTP/TLS 缩写未展开全称
  tags: [protocol, security, tls]

- id: g44
  term: HTTPS / TLS 1.2
  category: protocol
  source_pages: p22, p42, p57
  source_quote: |
    "Management application access is secured using https over TLS 1.2" (p42)
    "From version 4.6.104, the VAA web interface is only accessible via HTTPS" (p57)
  definition: |
    Web 管理面加密口径：4.6.104 起 VAA 界面仅可经 HTTPS 访问（TLS 1.2）；证书支持 PKCS12（.pfx/.p12）
    与 PEM（.pem/.crt/.cer + .key），约定放 /tmp 让安装进程自动识别，无证书则自签。
  alias_or_related: 证书族见 g52；版本边界（切换擦除/S.O.T 自签）见 counter-example n11
  tags: [protocol, security, https]

- id: g45
  term: CMIP
  category: protocol
  source_pages: p42
  source_quote: |
    "The CMIP link allow to synchronize the Visual Automated Attendant with the OXE Phone book." (p42)
  definition: |
    VAA 与 OXE 电话簿之间的同步链路（缩写书内未展开）：目录（g09）的"OXE phonebook synchronization"
    即经它实现——同步为破坏性操作（清空手工条目）。
  alias_or_related: 破坏性同步见 counter-example n18
  tags: [protocol, synchronization, directory]

- id: g46
  term: DPNSS
  category: protocol
  source_pages: p112
  source_quote: |
    "Use the number 599 for DPNSS prefix, used to optimize call routing. By default, the prefix is
    already in use: • Delete it • And recreate it with the feature 'PCX address in DPNSS'" (p112)
  definition: |
    OXE 侧与路由优化相关的前缀机制（缩写书内未展开）：实验要求把 599 前缀删掉后以 "PCX address in
    DPNSS" 特性重建，并在 /System 里把 Routing optimization 设为 Yes。属 OXE 全局参数，与 VAA 无直接
    配置交互。
  alias_or_related: 配置链见 framework f19 第 9 步
  tags: [protocol, oxe, routing]

- id: g47
  term: DDI / DID
  category: protocol
  source_pages: p17, p24, p28
  source_quote: |
    "DDI table - First external nb 41000 … DDI table – First internal nb 31000" (p17)
    "DDI range • Range of numbers used to call trees belonging to this company • Internal numbers can be
    used (not necessary DDI)" (p24)
    "Associate a DID number with a tree structure" (p28)
  definition: |
    直拨外线号码（两拼写同义混用：公司设置页写 DDI range，路由页写 DID number）：公司 DID 段界定树的
    取号范围，可用内线号（实验即用 31400-31415 内线口径）；OXE 侧 DID 翻译表把外线号映射到内线。
  alias_or_related: 实验翻译规则见 case c01 第 7 步
  tags: [protocol, numbering]

- id: g48
  term: WAV (8KHz PCM 16-bits mono)
  category: protocol
  source_pages: p34, p138
  source_quote: |
    "Import of wav files •Format: 8KHz PCM 16-bits mono" (p34)
    "Wav files uploaded to prompts should have the format: 8 KHz, PCM 16 bits mono. … No space in the name" (p138)
  definition: |
    提示音导入的硬格式约束：8KHz 采样、PCM、16-bit、单声道，名称不能含空格；录音室级高码率文件须先
    转格式。多语言树的语言选择前提示必须双语同文件（或 TTS 串联）。
  alias_or_related: 双语同文件规则见 counter-example n22；语音一致性建议见 principle p13
  tags: [protocol, audio, format]

- id: g49
  term: JSON
  full_name: JavaScript Object Notation（p232 展开）
  category: protocol
  source_pages: p232, p233
  source_quote: |
    "JavaScript Object Notation (JSON) is an open standard file format and data interchange format that
    uses human-readable text to store and transmit data objects." (p232)
    "VAR(resultHTTP.main.temp) returns the content: 3.33" (p233)
  definition: |
    HTTP 节点返回数据的载体格式：VAA 按对象路径点语法取值——VAR(变量.对象) 取对象、VAR(变量.对象.字段)
    取标量（实验取 openweathermap 的 resultHTTP.main.temp 等）。
  alias_or_related: HTTP 节点见 case c14 / framework f16
  tags: [protocol, http, data]

- id: g50
  term: JDBC / SQL
  category: protocol
  source_pages: p207, p208, p320, p322
  source_quote: |
    "The VAA uses jdbc drivers to connect to the various existing databases. By default, only the
    org.postgresql.Driver and org.mariadb.jdbc.Driver drivers are available and integrated with the VAA." (p320)
    "The format of the JDBC URL for MS SQL is as follows: jdbc:sqlserver://10.20.30.11:1433;Database=DB_VAA" (p322)
  definition: |
    外部数据库接入技术：VAA 经 JDBC 驱动连库，默认只内置 PostgreSQL 与 MariaDB 驱动，MS SQL/Oracle
    须手装到 /opt/ale/aa-webapp/lib（HA 两台都要装）；SQL 节点执行 SELECT/INSERT，单字段返回、多结果
    取首条、空结果不算错。JDBC 缩写书内未展开。
  alias_or_related: SQL 五条硬规则见 principle p21 / counter-example n23；驱动清单见 p22
  tags: [protocol, database, jdbc]

- id: g51
  term: SMTP / SNMP
  category: protocol
  source_pages: p101, p130, p282, p283
  source_quote: |
    "Email alert (trunk down, port usage)" (p21)
    "SIP trunk change status … Reach ports usage limit … License issue … The SNMP service is not enabled
    by default" (p282)
    "Warning SERVICES MUST BE RESTARTED AFTER SMTP CONFIGURATION" (p130)
  definition: |
    两类告警通道：邮件（SMTP，覆盖中继断/恢复、端口到许可上限、许可问题三类）与 SNMP trap（同类
    事件，服务默认不启用）。SMTP 参数在 install.sh 或 Admin/Settings 配置，改后必须重启服务。
    两缩写书内均未展开全称。
  alias_or_related: 告警口径见 principle p28；SNMP 边界见 counter-example n34；SMTP 重启陷阱见 n14
  tags: [protocol, alerts, monitoring]

- id: g52
  term: PKCS12 / PEM / SAN / X.509 / PKI
  category: protocol
  source_pages: p57, p59, p60
  source_quote: |
    "PKCS12 certificates (.pfx and .p12 extensions) • PEM certificates (.pem, .crt and .cer extensions
    for the certificate and .key for the certificate key)" (p57)
    "The most common type of certificate is based on the X.509 standard … a public key infrastructure
    (PKI)" (p59)
    "The Subject Alternative Name (SAN) … must be completed by added the VAA IP address and DNS name …
    Mandatory, the commonName: vaa1.company.com" (p60)
  definition: |
    证书族术语：格式两系（PKCS12：.pfx/.p12；PEM：.pem/.crt/.cer + .key）；X.509 为证书标准、PKI 为
    公钥基础设施（两词书中括注展开）；SAN（Subject Alternative Name，书中展开）必须含 VAA 的 IP 与
    DNS 名，commonName 必填。生成参数（SHA-256、RSA 4096）按客户环境调整。
  alias_or_related: 生成流见 g36 XCA / framework f13
  tags: [protocol, certificate, security]

# ── 六、文档与资源 (resource) ──

- id: g53
  term: MyPortal
  category: resource
  source_pages: p76, p95, p162, p277, p278
  source_quote: |
    "Refer to the Installation guide The VAA documentation is available on MyPortal" (p76)
    "The installation zip file (as well as the boot DVD) can be downloaded from MyPortal website" (p95)
    "Find all available commands in Section 6 - VAA system management in the installation guide" (p278)
  definition: |
    ALE 客户服务门户：VAA 文档（安装指南/管理指南）、发行包 zip 与 BootDVD 的下载入口；本书多处把
    细节外置给它承载的官方文档（安装手册 4.2/6.4、第 6 章 VAA system management，管理指南 4.3/第 10 章）。
  alias_or_related: 外置文档清单见 g54；counter-example n50 汇总了全部外置指针
  tags: [resource, portal, documentation]

- id: g54
  term: RLAB / POD
  category: resource
  source_pages: p5, p7, p9, p11
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a
    data center. … Pods are independent of each other • Pods have the same configuration • Pods have
    access to common resources" (p5)
    "Common resources Subnet 0 10.20.30.x External DNS 10.20.30.250 NAS: softs, licenses, … SIP
    Simulator SQL/Mail server 12.0.0.2" (p7)
  definition: |
    ALE 培训远程实验室：纯虚拟化，按 POD 划分的同构实验单元（OXE/OMS/FlexLM/PC Client/VAA Master
    192.168.1.55/VAA Slave 192.168.1.56，网段 192.168.1.x），POD 间相互独立、共享公共资源区
    （10.20.30.x：NAS 软件许可库、SIP 模拟器、SQL/Mail 服务器、外部 DNS）。课堂模式同拓扑，可经
    RAP 接物理话机（p13）。全部教学专用。
  alias_or_related: 虚机清单见 framework f02；NAS 'VSAA' 共享盘与 'Sharing' 网络盘（p11）并入本条；
  SIP 模拟器见 g39 ITSP1
  tags: [resource, lab, training]

- id: g55
  term: ALE BootDVD
  category: resource
  source_pages: p76, p80, p88, p95, p310
  source_quote: |
    "Operating system installation - Boot on .ISO BootDVD ALE … Choose installation language if
    necessary" (p80)
    "The installation zip file (as well as the boot DVD) can be downloaded from MyPortal website" (p95)
  definition: |
    ALE 系统安装介质（物理 DVD 或 ISO）：启动后选 VAA → 选版本（4.8）自动安装 SUSE，并承担 GRUB 口令、
    键盘/时区等安装期交互。S.O.T 与手工安装都以它为系统层起点；新版获取走 MyPortal。
  alias_or_related: 安装流程见 case c02；S.O.T 见 g15
  tags: [resource, installation, media]

- id: g56
  term: TBE083 / OTEC-S VAA configuration Guide
  category: resource
  source_pages: p50
  source_quote: |
    "VAA supports OmniPCX Enterprise multi-company features • For details, refer to the document TBE083
    - Multi Companies features OXE ALE link, click HERE" (p50)
    "For detail about configuration, please refer to: OTEC-S: Visual Automated Attendant configuration
    Guide" (p50)
  definition: |
    multi-company 场景的两份外置权威文档：TBE083（OXE 多公司特性文档）与 OTEC-S 的 VAA 配置指南——
    本书只给一页概念（共享媒体服务器、号码示例 861→8613999），配置细节全在书外。
  alias_or_related: 其余外置文档见 g53/g58 与 counter-example n50
  tags: [resource, document, multi-company]

- id: g57
  term: VAA Installation Guide / Administration Guide
  category: resource
  source_pages: p29, p53, p61, p78, p141, p277, p278
  source_quote: |
    "Possible use but not recommended (See chapter 4.3 Disambiguation about routing expressions in the
    Administration guide)" (p29)
    "Refer to the Installation guide – Section 4.2 for complete procedure" (p78)
    "To set up a public certificate, please refer to the installation manual - chapter 6.4 HTTPS
    configuration for web app" (p61)
    "Refer to the section 6 - VAA system management in the installation guide" (p277)
  definition: |
    VAA 两份官方文档（经 MyPortal 获取）：安装指南——完整安装（4.2）、公网证书（6.4）、系统管理与
    命令全集（第 6 章）；管理指南——路由表达式歧义消解（4.3）、TTS 细节与价格（第 10 章）、上下文
    变量清单。教材明确让位于它们（"Given as an example! Always consult the official documentation!"）。
  alias_or_related: 外置指针全景见 counter-example n50
  tags: [resource, document, production]

- id: g58
  term: ALE Knowledge Hub
  category: resource
  source_pages: p347, p351
  source_quote: |
    "Connect to ALE Knowledge Hub (https://enterprise-education.csod.com) with your usual credentials" (p347)
    "Browse our catalog available on https://enterprise-education.csod.com/ to find your training path
    and course detail." (p351)
  definition: |
    ALE 培训平台：完成在线培训评估后在此下载培训证书；也是查培训路径与课程目录的入口。培训收尾
    流程专用（p345-351），与产品交付无关。
  alias_or_related: 反馈邮箱 training-services@al-enterprise.com（p351，并入本条）
  tags: [resource, training, portal]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 术语表（17 行）逐条核对

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| VAA (Visual Automated Attendant) | 正文有明确定义（p1/p20/p42） | g01 |
| Tree (树/脚本) | 有明确定义（p144/p145/p216） | g02 |
| Node (节点/积木) | 有明确定义（p27 命令清单 + p144-162/p203-213 讲义） | g03 |
| Tenant / Company | 有明确定义（p24/p25/p50） | g04 |
| Routing number | 有明确定义（p28/p29） | g05 |
| Prompt | 有明确定义（p34/p138/p149） | g06 |
| TTS / ASR | 有明确定义（p34/p36-37/p140-141） | g07 / g08 |
| Directory / Dial by name | 有明确定义（p33） | g09 |
| Master / Slave | 有明确定义（p44/p47/p240） | g12 |
| Reference VAA | 有明确定义（p51） | g13 |
| PCS | 有定义性用法（p49/p301），全书未展开全称 | g14（full_name 已如实省略） |
| S.O.T | 有明确定义（p76 括注展开 software Orchestration tool） | g15 |
| incoming username | 有明确定义（p81/p101/p109） | g16 |
| ARS | 有定义性用法（p44/p86），全称仅以菜单路径 automatic route selection 出现（p265） | g17（full_name 已如实注明出处） |
| Discriminator / NPD | 有明确定义（p262/p264，NPD 全称 p264 标题展开） | g18 / g19 |
| OPEX / Purple On Demand | 有明确定义（p305/p46） | g20 |
| FlexLM / Release 11 | 有明确定义（p274/p277/p89） | g23 / g24 |

结论：**17 行全部在册，无"仅 passing 提及需排除"项，无"书中实际未出现"项。** 原书四个合写行（TTS/ASR、Discriminator/NPD 等）按语义拆分为独立条目，故总数 54 条大于 17。

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：Schedule/Calendar/Business hours（g11）、Filter（g10）、受限用户档案（g22）
- 角色：Super administrator/Administrators（g21）
- 许可：FlexLM .lic/.vaa 文件（g23）、VAA_RELEASE/Release 11（g24）、AAIVR/AAPORTS/ECCSTART（g25）、IVR Options（g26）
- 产品/组件/工具：OXE（g27）、OMS（g28）、aa-media-server（g29）、aa-webapp（g30）、aa-license-server（g31）、tts-hub（g32）、Nginx（g33）、PostgreSQL（g34）、SUSE（g35）、XCA（g36）、IPDSP（g37）、MicroSIP（g38）、ITSP1（g39）、MS SQL Express/SSMS（g40）
- 协议/技术：SIP trunk ABC/F（g41）、G711/G729/G723（g42）、SIP TLS/SRTP/secureCall（g43）、HTTPS/TLS 1.2（g44）、CMIP（g45）、DPNSS（g46）、DDI/DID（g47）、WAV 格式（g48）、JSON（g49）、JDBC/SQL（g50）、SMTP/SNMP（g51）、证书族（g52）
- 资源：MyPortal（g53）、RLAB/POD（g54）、ALE BootDVD（g55）、TBE083/OTEC-S（g56）、安装/管理指南（g57）、ALE Knowledge Hub（g58）

### 3. 仅 passing 提及、未单列条目的词（备查）

- ITSP2（p16 拓扑图出现，无细节，附于 g39）
- Thunderbird（p74/p238，课堂收邮件客户端，纯教学操作）
- FileZilla（p81/p96/p123，SFTP 传输工具，操作已入 c02/c04）
- openweathermap（p232-235，HTTP 实验的外部服务，实验口径）
- ODBC（p339-344，MS SQL 连通性测试手段，已入 c19）
- RAP（p13，课堂接物理话机的接入设备，无展开）
- TUI（p27 "Record prompt via TUI"，未展开，附于 g06）
- VXML（p132 "aa-engine (VXML server)"，未展开，附于 g30）
- COS（p225 "Manage the Phone feature COS"，OXE 话机特性，未展开，边界已入 n35/p20）
- ANI（p159 "Unknown ANI"，未展开，附于 g10）
- Q931 / NPI / TON（p107/p264，OXE 信令参数缩写，未展开，附于 g41/g19）
- FQDN / MAC（p92/p274，未展开，已入 g23 许可绑定语义）
- cron（p293-294/p303，Linux 定时任务，已入 principle p26/p33）
- GRUB / CIS-2（p93，书内有概念段解释，已入 BOOK_OVERVIEW 批判与 principle p03）
- RUFUS 无、NUC 无（本书不涉及 Rainbow 网关硬件——与 RAINXTE001EN 无关，仅防混）

### 4. 提取口径说明

- 所有定义只采信本书正文；PCS/OMS/IPDSP/ITSP/CMIP/DPNSS/TUI/VXML/COS/ANI/Q931/NPI/TON/JDBC/SMTP/SNMP/FQDN/MAC/OPEX/CAPEX/ABC-F/G729 系列无全称展开者，full_name 一律省略或仅注原文出处，不做外部补全。
- 已展开全称并标注出处的：Visual Automated Attendant（p1）、software Orchestration tool（p76）、Numbering Plan Description（p264）、Subject Alternative Name（p60）、public key infrastructure（p59）、X.509（p59）、JavaScript Object Notation（p232）、OmniPCX Enterprise（p42）、SQL Server Management Studio（p329）、Automatic Route Selection（仅菜单路径小写出现，p265）。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准，引用均为原文摘录；实验值（IP/密码/账号/号码/token）均为实验口径，生产必须替换。
- 版本号保留原文完整位数：R4.8.006、4.6.104、4.2.15、4.3.005、Release 11、PostgreSQL 16、ESXi 8.0、Hyper-V 2022、Proxmox 8.2、MS SQL Express 2019、OXE N2。
