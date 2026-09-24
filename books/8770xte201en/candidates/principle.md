# 原则/清单/规则/公式/数值口径候选 — OmniVista 8770 R5.2 计费与性能管理 (8770XTE201EN Ed45)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，实验环境给定值（IP、密码、账号、教学税率/汇率）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: 虚拟化支持清单（Hypervisor 矩阵）与容量规划工具版本
  type: metric
  source_pages: p8
  source_chapter: SOLUTION OVERVIEW / Virtualization
  source_quote: |
    "• Hypervisors • VMware ESXi (6.x, 7.0 and 8.0) • Microsoft Hyper-V® 2016, 2019, 2022
    • Nutanix AHV ( 20220304) • ASW (Amazon Web Services) ... OmniVista 8770 Capacity Planning
    tool V3.0 for a better sizing flexibility of virtual machines parameters" (p8)
    "• No OmniVista 8770 license for virtualization • According to the different hypervisors, some
    complementary services may require additional license costs" (p8)
  summary: |
    支持四种 Hypervisor：VMware ESXi 6.x/7.0/8.0；Hyper-V 2016/2019/2022；Nutanix AHV（版本号
    20220304）；AWS。虚机要求与物理服务器相同；虚拟化不收 8770 许可，但部分 Hypervisor 上的补充
    服务可能引增许可成本；选型用 Capacity Planning tool V3.0。
  conditions: Ed45 口径；部署前核对最新支持矩阵
  tags: [metric, virtualization, hypervisor]

- id: p02
  title: 跨版本兼容矩阵（8770 版本 × PBX/OpenTouch 版本，逐格）
  type: metric
  source_pages: p9
  source_chapter: SOLUTION OVERVIEW / Cross compatibility
  source_quote: |
    "OT R2.4 to R2.6.1 X X X X ... OXE R12.2 to R12.4 X X X X ... OXE Purple R100 (N1) X X X
    ... OXE Purple R100.1 (N2) X X ... OXE Purple R101.0 (N3), R101.1 (N4) & R101.2 (N5)  X
    ... OXO Connect / OCE R4.0 X X X X ... OXO Connect / OCE R5.0 to R5.1 X X X
    ... OXO Connect / OCE R5.2 to R6.2 X X" (p9，四列依次为 8770 R4.2/R5.0/R5.1/R5.2)
  summary: |
    逐格转写（列=R4.2, R5.0, R5.1, R5.2）：OT BE/MS/MC R2.4-R2.6.1 = 全兼容（4×X）；OXE R12.2-R12.4
    = 全兼容；OXE Purple R100(N1) = 前三版（R5.2 不支持）；Purple R100.1(N2) = R4.2/R5.0；Purple
    R101.0(N3)/R101.1(N4)/R101.2(N5) = 仅 R5.2；OXO Connect/OCE R4.0 = 全兼容；R5.0-R5.1 = R5.0+
    （后三列）；R5.2-R6.2 = R5.1+（后两列）。
  conditions: 矩阵随版本演进；实验机为 OXE R101.1-n4（p93 启动横幅 Active version）
  tags: [metric, compatibility, versions]

- id: p03
  title: 计费缓冲与落盘三时机：≤500 条、90 分钟无票、强制压缩
  type: rule
  source_pages: p62, p64, p93
  source_chapter: External Accounting / Accounting files creation & Using maintenance commands
  source_quote: |
    "Accounting records storage (max 500 records)" (p62)
    "No record received within 90 minutes ... An accounting file is created at 11:00" (p64)
    "account compress ... Force the creation of a new .DAT file. Records stored in the memory buffer
    are saved in the .DAT file. ... Note: A synchronization of the node saves the buffer into an
    accounting file." (p93)
  summary: |
    三条硬规则：(1) 内存缓冲最多 500 条记录；(2) 90 分钟未收到新记录即触发落盘建文件；(3) account
    compress 命令强制把缓冲写入新 .DAT；节点同步也会触发落盘。实验时序示例（缓冲=3 条）：08:10/08:40/
    08:50 满后 08:55 新票进 tax.tmp，09:05 再满时合并成 TAXAAAAC.DAT 并登记 ACCOUNT.LIS。
  conditions: 缓冲大小为 Ed45 口径；生产中同步频率影响文件粒度
  tags: [rule, accounting, buffering, metric]

- id: p04
  title: 出票规则：未接通外线呼出/呼入也出票；本机-本机不出票
  type: rule
  source_pages: p67-68
  source_chapter: External Accounting / Outgoing & incoming calls, Local & network calls
  source_quote: |
    "Note: a non-established outgoing or incoming call (duration=0) generates an accounting record" (p67)
    "Note: accounting record is only generated for established local-local and local-network call" (p68)
  summary: |
    两类出票边界：(1) 外线方向的呼出/呼入（经公共或专线中继组），即使未接通（时长=0）也生成票据——
    这就是过滤器里"Public Outgoing 0 Units calls"的存在意义；(2) 本机-本机（local-local）呼叫只在
    "已建立"时出票，local-network（跨节点）已建立呼叫出票。
  conditions: 记录经 FTP 回收入库后时长=0 的票可被加载过滤排除
  tags: [rule, accounting, records]

- id: p05
  title: 外部计费开启参数：存储上限 31 天=744 个压缩文件；出票类型含 0 计费呼出
  type: metric
  source_pages: p86-88
  source_chapter: How-To / External accounting
  source_quote: |
    "This number defines the maximum of accounting files that can be saved on the PCX: default value
    31 days i.e. 31 x 24 files = 744 compressed files" (p86)
    "Don't forget to select the Public Outgoing 0 Units calls." (p86)
    "Set this parameter to Not masked because the PIN code is masked by the OmniVista 8770 server. ...
    Set this parameter to 0 because the called number is masked by the OmniVista 8770 Server." (p88)
  summary: |
    参数口径：Max No. Days of Storage 默认 31 天（31×24=744 个压缩文件）；Files for External Accounting
    过滤器要选齐公共/专线、出/入、本地/网络呼叫，且必选 Public Outgoing 0 Units calls（0 计费呼出），
    可 Add After 追加 PCX PCX Calls 开本地计费；Financial Report 页签两处设"不遮"：PIN=Not masked、
    被叫遮蔽位数=0（因为 8770 侧自己做遮蔽与 PIN 保护）。路径：Configuration > OXE 右键 Configure >
    Applications > 1 > Accounting > 1；改完 All 页签要点 Apply 再进后续页签。
  conditions: 实验口径；All 页签 Internal Accounting=Yes、Files for External Accounting=Yes
  tags: [metric, accounting, checklist]

- id: p06
  title: OXE 计费维护命令集（account compress / ACCOUNT.LIS / accview）
  type: checklist
  source_pages: p93-95
  source_chapter: How-To / External accounting / Using maintenance commands
  source_quote: |
    "(101)csa> account compress" (p93)
    "cd /usr4/account: Move to the accounting folder. more ACCOUNT.LIS: Display the history of
    accounting files. ll *.DAT: Display the list of existing accounting files." (p94)
    "accview –mtf <name of the .DAT file> ... accview –b 10 –mtf ... Display the 10 firsts records
    ... accview –e 10 –mtf ... Display the 10 lasts records" (p95)
  summary: |
    排障四命令：①account compress 强制落盘；②cd /usr4/account + more ACCOUNT.LIS 看文件清单历史、
    ll *.DAT 列现存文件；③accview -mtf <文件> 逐字段显示票据（-mtf 可交互选文件）；④-b 10 / -e 10
    显示头 10 条/尾 10 条。SSH 登录用 mtcl（实验口径密码 Superuser2580*）。
  conditions: 实验口径：mtcl/Superuser2580*；生产密码由客户管理
  tags: [checklist, accounting, maintenance, oxe-cli]

- id: p07
  title: 节点声明规则：子网号=OXE 网络号；节点号=网络号×100+节点号；报警模式=永久 IP 连接
  type: rule
  source_pages: p75-78
  source_chapter: How-To / OXE node registration
  source_quote: |
    "Subnetwork number: Subnetwork number must be equal to the OmniPCX Enterprise network number" (p76)
    "Subnetwork – Node number: Enter a numeric value equal to the OmniPCX Enterprise network*100 +
    OmniPCX Enterprise node number. Example: With a network number = 1 and node number = 2, you must
    enter 101" (p77)
    "Alarm reception mode: Select Permanent IP connectivity. The OmniVista 8770 server establishes a
    permanent IP connection to receive alarms and events." (p77)
  summary: |
    声明公式三条：(1) Network 名称/号码自由（实验 ale/1）；(2) Subnetwork 号=OXE 网络号；(3) OXE 的
    Subnetwork-Node number = OXE 网络号×100 + OXE 节点号（实验 1×100+1=101）。IP 填 OXE 主地址 csm
    （192.168.1.3，空间冗余时右键 Add a Value 加第二地址）；FTP 用户 adfexc + 密码用于数据取回；勾
    Process configuration 与 Directory Process；Alarm reception mode=Permanent IP connectivity；
    Software download 页签填 mtcl 维护账号；Connectivity 页签勾 SSH 并填唯一 Host name（仅字母数字
    与 .,-_ 且字母开头，MindTerm 据此生成 SSH 公钥）。
  conditions: 实验口径：adfexc/Superuser2580*、mtcl/Superuser2580*；8770 登录 AdminNmc/Superuser01*
  tags: [rule, node-registration, numbering]

- id: p08
  title: OXE 侧接入核查命令：siteid、netadmin -m（角色地址/SSH/信任主机）、netstat
  type: checklist
  source_pages: p71-74
  source_chapter: How-To / OXE node registration / Checking Call Server SSH information
  source_quote: |
    "Enter the command siteid (101)csa> siteid — Node number : 1 ; Network number : 1" (p71)
    "Select option 5: Role addressing ... | local main | Ethernet | csm | 192.168.1.3 |" (p72)
    "Security with SSH: yes ... netstat -an | grep :22 — tcp 0 0 0.0.0.0:22 ... LISTEN" (p73)
    "All hosts machines involved with OXE Call Server must be declared." (p74)
  summary: |
    核查清单：①siteid 显示节点号/网络号（实验均为 1）；②su - 后 netadmin -m：选项 5 Role addressing
    查主地址（csm=192.168.1.3，空间冗余记两个）；选项 2 Show current configuration 查 SSH=yes；netstat
    -an | grep :22 应 LISTEN（22 开/23 关验证法）；选项 11 Security > 1 Firewall > 3 Restricted Access
    > 1 View trusted hosts——8770 服务器（omnivista 192.168.1.70）、OMS、PC、网关都必须在信任主机表内。
  conditions: 实验口径：root 密码 Superuser2580*；涉及 Call Server 的主机必须全部声明
  tags: [checklist, ssh, trusted-hosts, oxe-cli]

- id: p09
  title: 同步语义：Complete/Partial × Separate/Global 四象限；同步日志与验证页签
  type: rule
  source_pages: p79-80
  source_chapter: How-To / OXE node registration / Synchronizing
  source_quote: |
    "Partial synchronization includes changes performed since the date of last synchronization for
    entries of the following types: - Users, Directory, Data terminals, Speed dial numbers, Remote
    users. Other data are synchronized without taking into consideration the date of the last change.
    Complete synchronization includes changes made to all entries" (p79)
    "Log file C:\8770\log\ NMCSyncLdapPbx_1.log" (p80)
  summary: |
    同步二维选择：Complete（全部条目无视改动日期）/ Partial（仅用户/目录/数据终端/缩位拨号/远端用户
    按上次同步日期增量，其余类型始终全量）；Separate（只同步选中 OXE）/ Global（连同关联 OpenTouch）。
    操作四步：任务向导选"of the task"→ Status 页签 → Apply 启动（点 OK 则后台跑、窗口消失）→ Refresh
    看日志。验证：成功提示 + Configuration 树下 OXE 分支生成 + Data Collection 页签"Date of last
    modification"。日志：NMCSyncLdapPbx_1.log。
  conditions: 组织更新任务也可触发缓冲落盘（p93）
  tags: [rule, synchronization]

- id: p10
  title: SIP 模拟器对接参数：Registration ID=pbxN、DID 首外线 33210N41000、号段 500
  type: metric
  source_pages: p83-84
  source_chapter: How-To / OXE configuration to use the public SIP carrier simulator
  source_quote: |
    "Registration ID: pbxN (where N is your POD Number) Example for POD 4, pbx4 ... Outgoing username
    = pbxN" (p83)
    "First external number: 33210N41000 (where N is your POD Number) For POD 4: First external number
    = 33210441000 — First internal number 31000 — Range Size 500" (p84)
  summary: |
    两处按 POD 号配置：①External SIP gateway（菜单 SIP > SIP Ext Gateway，选 ITSP1_GW1）Registration
    ID 与 Outgoing username 均填 pbxN；②DID 翻译（Translator > 1 > External Numbering Plan > 1 >
    Default DID num. translator，右键 Create）First external number=33210N41000、First internal=31000、
    Range size=500。配完打外呼验证（参照 SIP Carrier Simulator 文档）。
  conditions: 实验口径；SIP 中继组与软话机在环境里已预配
  tags: [metric, sip, did, lab]

- id: p11
  title: 成本中心编号约定与用户分配（1=MKT、2=Training、3=TSS；255=未指定）
  type: metric
  source_pages: p89, p91-92, p256
  source_chapter: How-To / External accounting / Configuring the cost centers
  source_quote: |
    "Cost center number / Cost center name — 1 MKT — 2 Training — 3 TSS ... The cost center is created
    by default. You just have to manage the name associated to a cost center." (p89)
    "Charging COS — Justified (default value): all accounting information are displayed in the
    accounting record. Not ticketed: directory number, name and first name are masked" (p91)
    "Dialed number masked — No (default value) ... Yes: ... In the 8770 application, called number
    will be displayed in the following way: --------------" (p92)
  summary: |
    成本中心默认已建（编号即槽位），只需配名字：实验 1=MKT、2=Training、3=TSS；用户分配在 Rights 页签
    选 Cost Center ID（名字自动带出）；cc=255 表示未指定（组织树落根，见 p256）。两个记账开关：Charging
    COS=Justified（全信息出票，默认）/ Not ticketed（分机号/姓/名遮蔽）；Dialed number masked=Yes 时
    被叫在 8770 显示为一串"--------------"（OXE 侧遮蔽，8770 无法还原）。实验用户：31010 Ava Adore、
    31011 Alice Adams（ANALOG）；31000/31001→MKT、31002/31010→Training、31011→TSS。
  conditions: 实验口径；p89 表格 31011 姓/名书写顺序与 p90-91 创建步骤相反（书内笔误，见 counter-example）
  tags: [metric, cost-center, masking]

- id: p12
  title: 五种计费方法语义与"建树期用 organization update、建完切 detailed"原则
  type: principle
  source_pages: p99-102
  source_chapter: ACCOUNTING RECORDS RETRIEVAL / Accounting methods
  source_quote: |
    "Moving Cost center or subscriber into the tree is time-consuming operation when records are
    already stored in the database • When the organization tree is configured, select the detailed
    accounting method to retrieve the records — Goal: construction of the organization tree" (p101)
    "<network number X 1 000 000 + node number> 0298143300*****_1000101" (p102)
  summary: |
    原则：组织树搭建阶段选 "Organization update without records retrieval"（只建树不取票），树建好
    后切 Detailed accounting 开始取票——因为树建好后搬成本中心/分机在已有记录时非常耗时。按节点聚合
    的实体键=网络号×1,000,000+节点号（如 1000101）。每台 PCX 可独立选方法。
  conditions: 方法切换不迁移历史记录归属
  tags: [principle, accounting-methods, ordering]

- id: p13
  title: FTP 凭证铁律：密码随 OXE 改、FTP 用户名（adfexc）禁改（许可校验）
  type: rule
  source_pages: p109, p448
  source_chapter: How-To / Accounting records retrieval & Traffic Analysis
  source_quote: |
    "FTP login and password used to retrieve the accounting files. They must be the same as on the
    OmniPCX Enterprise. Important: Modify the password to match the OmniPCX Enterprise password if it
    has been modified. Do not modify the FTP user to avoid a problem at verification of the license."
    (p109, p448 同文重现)
  summary: |
    规则：PCX 页签的 FTP 用户/密码必须与 OXE 完全一致；OXE 改密后必须同步改这里；FTP 用户名一律不改
    （adfexc），否则许可校验出问题。关联参数：Accounting Process 下拉选 Detailed accounting；Data
    Collection 页签 Record/ticket collection 选 Accounting（默认 None），收集器文件落
    c:\8770\data\collector；"Last accounting file polled"由服务器自动更新。
  conditions: 书中示例密码 Superuser1234* 与实验环境 Superuser2580* 不同——以"与 OXE 一致"为准
  tags: [rule, ftp, licensing]

- id: p14
  title: PCS 相关数值：PCS ID=IP 的十六进制；随日同步开关默认 Yes
  type: metric
  source_pages: p105-106, p110
  source_chapter: ACCOUNTING RECORDS RETRIEVAL / PCS & How-To / PCS synchronization
  source_quote: |
    "PCS ID corresponds to the PCS IP address in hexadecimal • AC199E64 corresponds to
    10*16+12.1*16+9.9*16+14.6*16+4 = 172.25.158.100" (p106)
    "PCS Ticket Collection — Yes (by default). Yes: PCS are synchronized during the daily
    synchronization. No: PCS are not synchronized ... Manager has to synchronize manually" (p110)
  summary: |
    两条口径：(1) PCS ID 是其 IP 地址十六进制（例 AC199E64 ↔ 172.25.158.100，逐字节换算 A=10,C=12→172；
    1×16+9→25；9×16+14→158；6×16+4→100）；票据/索引文件带该后缀。(2) PCS Ticket Collection 默认 Yes
    （随每日同步取回）；设 No 则须手工同步 PCS。
  conditions: PCS 发现经呼叫服务器同步透明完成（p104）
  tags: [metric, pcs, hex]

- id: p15
  title: 加载过滤阈值：时长/成本/通信类型/呼叫类型/计费节点五道闸
  type: checklist
  source_pages: p110-111
  source_chapter: How-To / Accounting records retrieval / Loading filter
  source_quote: |
    "Duration: this threshold filters records characterizing calls shorter than a specific duration
    Example: For a duration > 0, accounting records with a duration of 0 are not loaded" (p110)
    "Cost must be >= 2.5. Accounting records characterizing all calls with a cost less than 2.5x
    (where x is the currency defined in the OmniVista 8770) are not stored" (p110)
    "By selecting Network, you store inter-OmniPCX Enterprise and internal calls. ... To avoid loading
    the records of OmniPCX Enterprises that are not declared in the OmniVista 8770, deselect the
    Undeclared option." (p111)
  summary: |
    五道加载闸（Account./traf./VoIP > Parameters > Loading > Accounting）：①Duration 阈值（如 >0 排除
    未接通票）；②Cost 阈值（如 ≥2.5×当地币种单位）；③Communication Type 勾选 Unspecified/Voice/Data；
    ④Call type 勾选 Incoming/Outgoing/Network（勾 Network 才存 OXE 间与本机呼叫）；⑤Charged party
    node——按已声明 OXE 勾选，取消 Undeclared 防止未声明节点记录入库。
  conditions: 过滤发生在加载时；被过滤票不入库也不可恢复
  tags: [checklist, loading-filter]

- id: p16
  title: 运营商命名与符号唯一性：Symbol ≤5 字母、名称/符号全局唯一
  type: rule
  source_pages: p152, p197, p218
  source_chapter: How-To / Direct carrier configuration Telecom 1 & 2 & Service
  source_quote: |
    "Symbol: Enter a symbolic name with 5 letters maximum (i.e. T1). Two carriers cannot have the
    same symbol. Symbols can be used in reports to replace long carrier names." (p152)
    "Create a pulse type carrier ... Unit cost: Enter the value for the unit cost (i.e. 1,5)" (p218)
  summary: |
    运营商属性规则：Name 全局唯一；Symbol ≤5 字母且全局唯一（报表里代替长名）；Type=Outgoing；State=
    Active；Carrier prefix 可空；Country 仅为信息字段；Inherit tracking 应关闭。pulse 型运营商经"Create
    a pulse type carrier"入口建（State 位置为生效日期，Unit cost=每脉冲单价，直接选 Tax/Currency/
    Country），Tariff 字段自动生成不可填。
  conditions: 实验口径：Telecom 1/T1、Telecom 2/T2、Service/Srv（1.5/脉冲、TVA、Euro、France）
  tags: [rule, carrier, naming]

- id: p17
  title: 前缀匹配规则：最优（最长）匹配归属；同一前缀不可跨区域；carrier prefix 可与其叠加等效
  type: rule
  source_pages: p156, p181, p154
  source_chapter: How-To / Telecom 1 / Region & Prefix
  source_quote: |
    "To link a called number to a called region, the accounting application looks for the indicator
    prefix that matches the best the first digits of the called number. Example: if the carrier prefix
    defined in the carrier properties is 0, the 2 followings configuration are equivalent" (p156)
    "a same prefix cannot be used for different regions." (p181 Notes)
  summary: |
    三条规则：(1) 被叫号按"与号码前 n 位最匹配"的 indicator prefix 归入被叫区域；(2) 同一前缀不能同
    时属于不同区域——演进实验中必须先从 National region 删除 01 才能在 Paris 主叫区重建，否则报错；
    (3) Carrier prefix（运营商属性）与 indicator prefix 组合可等效配置（如运营商前缀=0 时两种写法
    等价）。主叫区（calling region）含 PCX 时必须填 Access phone number（仅信息用途）。
  conditions: 区域可同时为主叫与被叫（Paris 即如此，p183）
  tags: [rule, prefix, region]

- id: p18
  title: 资费公式族（exact 模式）：线性公式与四个叠加参数
  type: formula
  source_pages: p129-132
  source_chapter: TYPE OF TARIFF FOR COMMUNICATION COSTS
  source_quote: |
    "Call with a duration of 2min 24 s: Cost = 2*0,03 + 24*(0,03/60)" (p129)
    "Answered call initial cost: 0,1 ... Cost = 0,1+ 2*0,03 + 24*(0,03/60)" (p130)
    "Initial duration: 180 ... Call with a duration between 1 s and 180 s: Cost = 0,1 ... Call with a
    duration of 3 min 24 s: Cost = 0,1 + 24*(0,03/60)" (p131)
    "Minimum cost: 0,045 ... Call with a duration less than or equal to 90 s: Cost = 0,045 ... Call
    with a duration equals to 3 min 24 s: Cost = 3*0,03 + 24*(0,03/60)" (p132)
  summary: |
    exact 模式四层公式（教学单价 0.03/分钟，Unit duration=60）：①线性：Cost=分钟数×单价+剩余秒×(单价/
    60)；②+接通费：Cost=initial cost+线性部分（仅计费成功呼、时长>0）；③+免费时长：initial duration
    秒内只收 initial cost，超出后线性累计（180s 内=0.1；3m24s=0.1+24×0.0005）；④保底：minimum cost
    与"initial duration 内成本"取高（≤90s 按 0.045；超过则正常线性、保底失效）。Unit duration=60 对应
    分钟价、=1 对应秒价（服务器内部换算成秒）。
  conditions: initial cost/duration/minimum cost 仅作用于成功呼叫（时长非空）
  tags: [formula, tariff, exact]

- id: p19
  title: 资费公式族：分段（segments）、round up/down、脉冲、未接通费
  type: formula
  source_pages: p133-136
  source_chapter: TYPE OF TARIFF FOR COMMUNICATION COSTS
  source_quote: |
    "Call with a duration equals to 7 min 24 s: Cost = 3*0,08 + 4*0,07 + 24*(0,06/60)
    Segment number 1 2 3 / Segment duration (s) 180 240 0 / Unit cost 0,08 0,07 0,06" (p133)
    "Call with a duration equals to 2min 30 s — If round up, cost = 0,3 — If round down, cost = 0,2
    ... Round up: any stage started is chargeable • Round down: a stage is only counted if complete" (p134)
    "cost = 12*0,03 ... Communication cost calculated using the number of units contained in the
    accounting record" (p135)
    "Unanswered Call Initial Cost: 0,01 ... This is an additional cost applied to unsuccessful calls
    • Call duration is null" (p136)
  summary: |
    四类公式：①分段：按段序依次扣减（180s@0.08→240s@0.07→之后@0.06），7m24s=3×0.08+4×0.07+24×(0.06/
    60)，段必须手工排序；②round up（阶段开始即计）/round down（计满才计），60s 阶段×0.1 时 2m30s 分别
    为 0.3/0.2；③脉冲：Cost=Charge units×unit cost（例 12×0.03）；④未接通费：unanswered call initial
    cost（时长=0 的呼出加收，例 0.01）。
  conditions: 教学数值为实验口径；段 0 表示"最后一段无限长"
  tags: [formula, tariff, segments, pulse]

- id: p20
  title: 服务费 C+S 模型与法国 SVA 示例（ARCEP）
  type: principle
  source_pages: p137
  source_chapter: TYPE OF TARIFF FOR SERVICE COSTS
  source_quote: |
    "• 10 digits numbers starting with 08 called special number • Short numbers from 4 to 6 digits
    (10XX, 3YYY or 118 ZZZ) • SVA tariffs provided by the ARCEP organism (French Telecom regulator)"
    "C=0 & S=0: free contact number • C>0 & S=0: standard contact number • C>0 & S>0: surcharged
    contact number ... 0 825 200 014 — Service 0,15€/min + Cost of local call ... 0 809 100 114 —
    Free Service + Cost of local call ... 0 800 134 426 — Free of charge" (p137)
  summary: |
    增值业务（AVS/SVA）号码：08 开头 10 位特服号与 4-6 位短号；总票价=通信费 C（依运营商资费）+服务
    费 S（固定和/或时长费），三组合对应免费/标准/加收费。法国示例：0825 200 014=S 0.15€/min+本地通话
    费；0809 100 114=免费服务+本地通话费；0800 134 426=完全免费。
  conditions: 各国监管不同；配置上须建双资费（通信+服务）并在 Direction 绑定（p162-163）
  tags: [principle, sva, service-cost, france]

- id: p21
  title: 调整（Adjustment）公式：线性 Ax+b 或百分比 x+A%x，可挂四类对象
  type: formula
  source_pages: p138
  source_chapter: ADJUSTMENT
  source_quote: |
    "Adjustment is configured using a linear equation (Ax+b) or a percentage (A%)
    • Adjustment can be applied to a tariff, a direction, a segment or a carrier ... Apply a discount
    of 10% to calls corresponding to the direction Brest -> Paris — Type Percentage (x+A%x)
    Parameter A -10" (p138)
  summary: |
    两种数学形式：线性 Ax+b（A 倍率 + b 固定值，b 须带币种）或百分比 x+A%x（A 为正加价、为负折扣）。
    作用对象四类：资费、方向、段、运营商。示例：Brest→Paris 方向打 9 折=Type Percentage、A=-10。
  conditions: 与 Cost profile 的发票价调整相区分（那是第二层，见 p24/p32）
  tags: [formula, adjustment]

- id: p22
  title: 币种/税/国家参数：参考币种安装时定死不可删；附加币种带有效期汇率；教学税率 10%/20%
  type: metric
  source_pages: p139, p145-148
  source_chapter: CURRENCIES & How-To / Direct carrier settings
  source_quote: |
    "The choice of a country during the server installation defines the currency used as reference
    currency. Only one currency can be defined as the reference currency. The reference currency can't
    be deleted." (p145)
    "If the reference currency is Dollar, create an additional currency named Euro with the following
    conversion rate: 1 euro=1,21 dollars. If the reference currency is Euro, create an additional
    currency name Dollar with the following conversion rate: 1 dollar =0,82 euros." (p145)
    "a VAT rate of 10% for US target, called VAT. — a VAT rate of 20% for Europe target, called TVA."
    (p146)
  summary: |
    参数规则：参考币种由安装时所选国家决定，唯一且不可删（名称/符号可改）；附加币种须填与参考币种的
    汇率及有效期（无结束日=永久，如 1/1/2024；汇率变动靠开新有效期管理）；实验口径：1€=1.21$ 或
    1$=0.82€。税率按国家建（Tax Rate 页签同带有效期）：美 VAT 10%、欧 TVA 20%（教学口径）。国家清单
    仅为信息字段。资费的"Cost given by the PCX"模式要求 PCX 币种=参考币种（8770 不换算，p128）。
  conditions: 教学汇率/税率为实验口径
  tags: [metric, currency, tax]

- id: p23
  title: Telecom 1 资费参数全表（Local/National/Mobile 逐格）
  type: metric
  source_pages: p160-171
  source_chapter: How-To / Telecom 1 / Configure the tariff
  source_quote: |
    "Local tariff: Calculation mode: exact duration ... Day type: Daily — Unit duration: 60 — Unit
    cost: 0,2" (p160)
    "Time zone: Normal From 8:00 AM to 07:00 PM — Answered call initial cost: 0,7 — Initial duration:
    120 — Unit duration: 60 — Unit cost: 0,5 — Time zone: Reduce From 7:00 PM to 08:00 AM — Answered
    call initial cost: 0,2 — Unit duration: 60 — Unit cost: 0,3" (p164)
    "Mobile tariff: Calculation mode: Duration – round up ... Day type: Working day ... Unit duration:
    120 — Unit cost: 2 ... Day type: Weekend ... Unit duration: 180 — Unit cost: 2" (p168)
    "the 3 first minutes will be charged at 2€. From the 3rd to the 6th minute, it will be 1.5€. And
    from the 6th to the 9th minute, it will be 1€." (p171 Notes)
  summary: |
    逐格口径（货币 Euro/TVA，法国口径）：Local——exact、Daily、12:00AM 起、Unit 60×0.2。National——
    exact、Daily：Normal 08:00 起 initial 0.7/initial duration 120s/unit 60×0.5；Reduce 19:00 起
    initial 0.2/unit 60×0.3；Reduce 12:00AM（午夜段）initial 0.2/unit 60×0.3（累计时段须铺满全天）。
    Mobile——round up：Working day 12:00AM 起 unit 120s×2；Weekend（Reduce）12:00AM 起 unit 180s×2。
    区域：Brest 主叫（PCX Ale.Abc1.oxe，接入号 0298112233）；被叫 Local=02、National=01/03/04/05、
    Mobile=06；方向三支（→Local/→National/→Mobile）。
  conditions: 实验口径；时间用 AM/PM 制（美式界面）
  tags: [metric, tariff, telecom1]

- id: p24
  title: Telecom 2 与 Service 脉冲运营商参数（对照 Telecom 1）
  type: metric
  source_pages: p198-209, p217-221
  source_chapter: How-To / Telecom 2 & Pulse type carrier Service
  source_quote: |
    "Brest region ... Access phone number ... (i.e. 7298010233) ... Indicator prefix ... (i.e. 72)
    ... National region prefixes 71, 73, 74, 75, 76" (p198-202)
    "Time zone: Normal From 7:00 AM to 06:00 PM — Answered call initial cost: 0,6 — Initial duration:
    120 — Unit cost: 0,4 — Time zone: Reduce From 6:00 PM to 07:00 AM — Answered call initial cost:
    0,1 — Unit cost: 0,3" (p205)
    "Create a pulse type carrier ... Unit cost ... (i.e. 1,5) ... Special region ... (i.e. 36) ...
    (i.e. 118712)" (p218-220)
  summary: |
    Telecom 2（T2）：主/被叫区 Brest（接入号 7298010233，前缀 72）；National 前缀 71/73/74/75/76；
    Local 资费 60×0.2；National Normal 07:00 起 initial 0.6/120s/unit 60×0.4，Reduce 18:00 起 initial
    0.1/unit 60×0.3，午夜段 Reduce 0.1/0.3；方向 Brest→Brest（Local）、Brest→National。Service（Srv，
    脉冲型）：Unit cost 1.5、TVA、Euro、France；被叫区 Special 前缀 36 与 118712；唯一方向→Special。
  conditions: 实验口径；p210 方向表把被叫写作"Local region"而主叫为 Brest region（书内文字瑕疵）
  tags: [metric, tariff, telecom2, pulse]

- id: p25
  title: 成本计算与重算规则：加载时算价；改配置必须 Compute cost（Force）；两份日志判错
  type: rule
  source_pages: p117, p176-180
  source_chapter: DIRECT CARRIER CONFIGURATION & How-To / Computing cost
  source_quote: |
    "The cost calculation is performed during records loading into database. A cost recalculation is
    required when a carrier configuration change concerns records already stored in the database."
    (p178, p215, p225 Notes 同文重现)
    "Error: No first carrier found ... Called number: 118008 ... The called number 118008 is defined
    in several called regions that belong to different carriers. The server cannot choose a carrier
    so the cost is not calculated." (p180)
  summary: |
    规则三条：(1) 成本在票据加载入库时计算；(2) 运营商配置变更涉及已入库记录时必须重算——菜单
    Accounting/traffic > Compute cost：设 From/To 日期区间（不填=全部）、勾 Carrier Cost(s) + Force
    cost calculation、Simple job，任务可在 Scheduler 复查；(3) 排障看两份日志：NMCLD_CostCalculation_
    1.log（加载期错误）与 NMCCostRecalculation_CostCalculation_1.log（重算期错误），典型错"No first
    carrier found"=找不到匹配运营商，或号码（如 118008）落在多运营商的多个被叫区无法抉择而不计价。
  conditions: Compute cost 窗口另有 Variable cost(s)（调整档案变更用）与 Fixed Cost（订阅档案变更用）选项（p339）
  tags: [rule, cost-calculation, logs]

- id: p26
  title: Code Book 格式与导入规则：@ 表头/Tab 分隔/% 注释；.itl Node 必须匹配；改 EFFECT_DATE=新周期
  type: rule
  source_pages: p230-236, p243-244, p247-248
  source_chapter: CODE BOOK & How-To / Export & import
  source_quote: |
    "@ is the header character. A line beginning with this symbol gives the name of the fields used
    in the file • Only one header line per file and it is mandatory in all except information file ...
    % is the comment character" (p230)
    "Field Node must correspond to the name of the PCX declared in Configuration application ... Node
    name must be configured before importing the code book" (p233)
    "Another period for the direct carrier has been created. From a same carrier, different periods
    can be added." (p244)
  summary: |
    规则五条：(1) 文件格式——@行=表头（.inf 除外，且每文件仅一行必须），Tab 分隔字段（要默认值就留空
    跳 Tab），%行=注释；(2) .itl 的 Node 字段必须等于目标机 Configuration 里声明的 PCX 名（实验中
    oxe9≠oxe 导致导入报错、方向建不出来），导入前先改；(3) 导出运营商要"第二次导出"才拿到完整配置
    （p236）；(4) 改 .inf 的 EFFECT_DATE（如 20220101）后再导入=同运营商下新增 Period（价目随政策
    演进的正规做法）；(5) 对 code book 的一切修改必须在 Documents 目录做，不能直接改 NAS 上的原件
    （p246 Warning）。
  conditions: 实验口径：Telecom2_7x 文件夹来自 NAS Tools for training
  tags: [rule, codebook, import]

- id: p27
  title: 组织树归属与搬移权限矩阵：谁能在哪改什么
  type: rule
  source_pages: p256-257, p284-286
  source_chapter: ACCOUNTING ORGANIZATION & How-To
  source_quote: |
    "By default, it's not possible to allocate a cost center to a trunk group from the OXE
    configuration. ... Such move is authorized from the organization map because there is no impact
    on cost center management on the call server." (p285)
    "The move of a subscriber from a cost center to another one is only possible from OXE
    configuration or directory applications. That's why such move is not authorized from the
    organization map." (p286)
  summary: |
    权限矩阵：①用户/话务台/数据终端的成本中心——只能在 OXE 配置（Rights 页签 Cost Center ID）或公司
    目录改，组织图上剪贴分机会被拒绝；②中继组等无成本中心对象——OXE 配置里本就不能设成本中心，在
    组织图上剪贴到成本中心是允许的（不影响话机侧），或经 PCX Data collection 的 Default cost center
    统一归置；③level/成本中心在组织图上可自由剪贴/复制。搬移痕迹：成功搬移后原位置留灰色历史条目。
  conditions: cc=255 的条目落组织根
  tags: [rule, organization, permissions]

- id: p28
  title: 回溯与重建规则：只能选"设备"；level/成本中心/人不可回溯；ToolsOmniVista 强制停服务
  type: rule
  source_pages: p263-266, p290, p293, p295
  source_chapter: ACCOUNTING ORGANIZATION & How-To
  source_quote: |
    "A user is identified by the couple PCX ID/directory number • Levels, cost centers and persons
    can not be backdated — Item to be backdated must be active" (p263)
    "TO ASSIGN CORRECTLY THE HISTORY FROM AN INACTIVE SUBSCRIBER TO THE ACTIVE ONE, YOU MUST SELECT
    ITS DEVICE AND NOT THE USER." (p290 Warning)
    "Enter 'y' to stop the 8770 services (mandatory) ... All entities with historical data into the
    organization Will be deleted from the database. Their tickets and Ptp counters will be reassigned
    to the active entities!" (p293)
  summary: |
    四条硬规则：(1) Assign earlier creation date 只能把历史回挂到同身份（PCX ID/分机号）的**活动设备**
    上——选"用户"会错，Warning 全大写强调；新日期须早于该条目现创建日期、晚于等于最后一条对应非活动
    条目日期；(2) level/成本中心/人（person）不可回溯——组织更新后残留的非活动成本中心要手工删
    （p295）；(3) ToolsOmniVista.exe（C:\8770\bin\）执行 Accounting Organization Update 前强制停 8770
    服务（输入 y），并输入 cn=directory manager 口令（实验口径 superuser）；(4) 该操作删除全部带历史
    的非活动实体并把票据与 Ptp 计数器重挂到对应活动实体——不可逆，先归档再执行。
  conditions: 组织更新耗时与库大小相关（实验 0mn5.172s）
  tags: [rule, backdating, toolsomnivista]

- id: p29
  title: 掩码规则：显示位数优先；Default 档案不可删；grouped 报表只认 Default 的两个 group 类别
  type: rule
  source_pages: p300, p306, p310
  source_chapter: MASK PROFILES & How-To
  source_quote: |
    "Default profile cannot be renamed or deleted • However, you can reset masked digit to 0 to
    render it inactive • Two additional call categories: masked and unmasked group used systematically
    for grouped reports" (p300)
    "The displayed number has priority over the masked one." (p306)
    "In case of grouped report, the server ignores the mask profiles applied to the organization: it
    only takes into account the profile named Default" (p310)
  summary: |
    三条规则：(1) Default 掩码档案挂组织根、不可改名/删除——把遮蔽位数清 0 即等效停用；Masked group
    与 Unmasked group 两个呼叫类别只存在于 Default 档案，专供 grouped 报表；(2) 显示位数优先于遮蔽
    位数（"显示 4 位"的语义是至少显示前 4 位，号码不足 4 位全显）；(3) grouped report 忽略组织树上
    配的所有档案，只按 Default 档案的 group 类别遮蔽。教学示例：Professional 显示 4/遮 4，Unmasked
    professional 显示 4/遮 2——即解密报表也保留 2 位遮蔽。
  conditions: 给成本中心/level 配档案，其下全部设备继承
  tags: [rule, mask, confidentiality]

- id: p30
  title: 解密权限：默认禁止无掩码报表；须建"Mask data access"组成员；生成时索要其口令；改组须关 Reports 应用
  type: rule
  source_pages: p314-318
  source_chapter: How-To / Mask profiles / Unmasking
  source_quote: |
    "BY DEFAULT, THE GENERATION OF A REPORT WITHOUT MASK IS NOT ALLOWED. TO USE UNMASKING OPERATION,
    IT IS NECESSARY TO CREATE AN 8770 LOGIN WHICH IS MEMBER OF THE GROUP 'MASK DATA ACCESS'. THE
    PASSWORD OF THIS LOGIN IS ASKED WHEN A USER GENERATES A REPORT WITHOUT MASK." (p314 Warning)
    "TO MAKE THE UNMASKING CONFIGURATION ENABLED, REPORTS APPLICATION HAS TO BE CLOSED." (p316 Warning)
  summary: |
    解密三步规则：①Security 应用建管理员（实验名 Unmasking，口令 superuser）并加入 Groups > Mask data
    access 组；②组成员变更须关闭 Reports 应用后才生效；③任何用户点 Generate report w/o mask 时弹口令
    框，输入该组成员口令即可出解密版（解密程度仍受各档案 Unmasked 类别控制——如 TSS 档案解密后全显、
    Default 档案解密后仍遮 2 位）。OXE 侧已遮蔽的号码（示例 029845----）任何方式都无法还原（p319）。
  conditions: 解密报表会作为独立实例出现在报表树
  tags: [rule, unmasking, security]

- id: p31
  title: 成本档案公式与教学示例：+10% 两种写法；+5%+0.1€ 固定费；Root +50%；TSS +20%+0.5€
  type: formula
  source_pages: p325, p333, p335-336
  source_chapter: COST PROFILES & How-To
  source_quote: |
    "Example 1: to add 10 % ­ If type = linear equation, A =1,1 and B = 0. ­ If type =Percentage,
    A = 10 and B is not used. — Example 2: to add 5 % and a fixed cost of 0,1 € per communication €
    ­ Type = linear equation, A =1,05, B= 0,1 and currency = Euro." (p333)
    "Create a cost profile called Root cost: ­ To apply an increase of 50% for outgoing calls.
    ... TSS cost: ­ To apply an increase of 20% and to add a fixed cost of 0,5 euro for outgoing call."
    (p335-336)
  summary: |
    发票价公式（Invoiced cost w/o tax 页签，按呼叫类型）：x+B（线性，B 带币种）或 x×(1+A%)。换算表：
    +10% → 线性 A=1.1 B=0 或百分比 A=10；+5% 且每通话加 0.1€ → A=1.05、B=0.1 Euro。A<1 或负值为折扣。
    教学档案：Root cost=呼出 +50%（挂组织根全树生效）；TSS cost=呼出 +20% 且 +0.5€/通话（挂 TSS 成本
    中心，取消继承）。总成本基数=直连运营商成本+ISDN 成本+间接运营商成本（p325）。
  conditions: 订阅费在另两个页签（Services subscriptions/Station subscription）配置
  tags: [formula, cost-profile, invoiced]

- id: p32
  title: 订阅出票规则：日/周日/月一出票、时间戳 00:00:00、当月加入次月计、永不处理当天
  type: rule
  source_pages: p327, p339
  source_chapter: COST PROFILES & How-To
  source_quote: |
    "Subscription records are created at the start of the period: • Every day for daily records
    • Every Sunday for weekly records • On the first day of the month for monthly records • With a
    monthly subscription, users arriving in the current month will only be charged from the first of
    the following month • Time fields are set to 00:00:00 in each record" (p327)
    "Subscription recalculation is based on deletion of subscription records followed by a new
    addition of subscription records. Processing time may be long, depending on the number of records
    involved." (p339)
  summary: |
    订阅费机制：8770 在每次同步后生成"纯订阅费"会计记录（日票每日、周票每周日、月票每月 1 日，时间
    字段全 00:00:00）；月订阅当月加入者从次月 1 日起计；订阅成本计算永不处理当天，处理可能持续数天。
    重算路径：Compute cost 勾 Fixed Cost——机制是"先删订阅记录再重建"，量大时很慢。订阅费维度：持有
    设备/语音信箱/DDI 号（Services subscriptions）与分机类型（Station subscription），可按日/周/月、
    带币种与税。
  conditions: 订阅票与普通票同样可被组织树/掩码/域管控
  tags: [rule, subscription, invoicing]

- id: p33
  title: 可见域规则：开启须重启计费应用；未配域只见根；域按父继承；群组域无效
  type: rule
  source_pages: p351, p353, p355
  source_chapter: How-To / Accounting domains
  source_quote: |
    "Visibility domain — Yes. To interrupt accounting access control and restrictions, deselect this
    option. — You must restart the Accounting/traffic/VoIP application ... A warning indicates that
    no domain has been managed in the organization: only the organization root is visible." (p351)
    "It is not necessary to apply a domain to each level, as objects with no domain inherit one from
    their parent." (p353)
    "Visibility domains can also be defined for a group. Even if there is such possibility, it is not
    taken into account. ... The OmniVista 8770 server ignores the visibility domain of the group if
    visibility domains are specified for the user." (p355)
  summary: |
    四条规则：(1) 开关在 Administration > nmc > Application Configuration > Application Settings >
    Accounting > AccountingParameters 的 Visibility domain，开启后必须重启计费应用，且在配域之前整树
    只剩根可见；(2) 节点域按父继承，不必逐级配；(3) 管理员配域在 Security > Individual > Visibility
    domain for accounting（可 Add a value 配多域）；(4) 群组上的域配置不被采纳——必须配到具体管理员。
    AdminNmc 分配根域 Alcatel 即全域可见。
  conditions: 教学账号 AdminBrest→域 Brest；AdminCostCenter→域 Training+MKT（口令均为 superuser，实验口径）
  tags: [rule, domains, visibility]

- id: p34
  title: 报表尺寸上限：TXT 400 行 / HTML·PDF·EXCEL 50 页 / X 轴 100 元素 / 数据库 100000 行
  type: metric
  source_pages: p367
  source_chapter: How-To / Reports application / Report size limits
  source_quote: |
    "Maximum number of lines in TXT format — 400 ... Maximum number of pages in HTML format — 50 ...
    Maximum number of pages in PDF format — 50 ... Maximum number of pages in EXCEL format — 50 ...
    Maximum number of elements on X axis — 100 ... Maximum number of lines in database — 100000" (p367)
  summary: |
    Preferences > Reports > Reports Preference 六项上限：TXT 400 行；HTML/PDF/EXCEL 各 50 页；X 轴最多
    100 元素；数据库扫描上限 100000 行。超限的报表在末尾显示截断提示。入口：Preferences 菜单。
  conditions: Ed45 默认值，可调
  tags: [metric, reports, limits]

- id: p35
  title: 邮件服务器参数格式：<server>:<port> 无空格；端口缺省 25；发件人须被邮件服务器认识
  type: rule
  source_pages: p374, p477
  source_chapter: How-To / Reports application & Tracking / Mail server
  source_quote: |
    "Other possibilities: <mail server name>:<SMTP TCP port> ... The number of the SMTP port is
    optional if the default SMTP port number is used (default SMTP port = 25). Careful: no space
    between ':' and the TCP port number." (p374)
    "Name of the mail sender — By default: this field is empty. The name of the mail sender is
    OmniVista. Indicate a mail address known by the mail server" (p374)
  summary: |
    邮件配置规则（Administration > Nmc > OmniVista 8770 > Export parameters 页签）：Mail server 可填
    FQDN 或 IP，可加 :端口（默认 25 时可省，冒号与端口间不能有空格）；DNS 不在时只能用 IP；Name of the
    mail sender 默认 OmniVista，须填一个邮件服务器认识的地址。报表可按目的地邮箱导出（多址逗号分隔，
    p376）；Tracking 超限邮件同一封可含多个通知、附件按 profile 分类（p484）。
  conditions: 实验用 Thunderbird 按 POD 选 profile 收信（教学设施）
  tags: [rule, mail, smtp]

- id: p36
  title: Detailed vs Grouped 报表语义与 Hit-list：同一组数据 25 次呼叫的两种呈现
  type: principle
  source_pages: p385, p393
  source_chapter: How-To / Report customization
  source_quote: |
    "Detailed: ... if a set has dialed the same number twenty-five times, the detailed report lists
    the set twenty-five times and indicates the same called number. ­ Grouped: ... the grouped report
    lists it only once for the indicated called number." (p385)
    "Hit-list Report — Limits the number of lines in the report. This parameter is used with grouped
    report definition. Example: Display the 10 sets totaling the longest call duration" (p393)
  summary: |
    定义类型二选一：Detailed=逐条呈现不汇总；Grouped=按字段聚合（配合 Operation：Group by/Count/
    Minimum/Maximum/Total/Average）。Hit-list 限量只用于 grouped 定义（例：通话时长最长的前 10 台话机）。
    Total counters 数据源的分组报表可显著缩短生成时间（p385）。Generation Time Filter 让过滤器在生成
    时再选，一份定义多场景复用（p392）。
  conditions: 详细报表的 Operation 字段留空（p390）
  tags: [principle, reports, grouped]

- id: p37
  title: Designer 视图规则：不能跨区域取表头出图/出公式；嵌套汇总靠 View 切换；无用表头用前景空白遮蔽
  type: rule
  source_pages: p396-398, p617, p639-641
  source_chapter: How-To / Report customization & report #4 #5
  source_quote: |
    "The view defines the report area used to generate a graph or a formula. ... It is impossible to
    use headers from different areas to generate a graph or a formula." (p396)
    "To set up the calculation of the total cost per carrier, the use of the total cost per called
    region is necessary ... But the total cost per called region information is useless. So the only
    possibility it's to mask it on the report — On Foreground field, select the blank color" (p617)
  summary: |
    三条版面规则：(1) 图表/公式只能用同一视图区域内的字段——grouped 报表要"按分机汇总→按成本中心汇总"
    必须在 Cost Center 页脚把 View 切到 Extension 才能引用 Sum(分机级)；(2) 中间层汇总（如被叫区小计）
    若不想显示，唯一办法是把该字段 Foreground 设为空白色遮蔽（report #4 载体技巧）；(3) grouped 报表
    末页多余的"Detail"表头，靠加一个全呼叫共有的字段（如 Country）作 Group Header 再前景空白遮蔽来消掉
    （report #5 技巧）。
  conditions: 前缀文本（如 "Total for the extension:"）经 Properties>Prefix 加
  tags: [rule, designer, layout]

- id: p38
  title: VoIP KPI 阈值默认值：时延>150ms、丢包>3%、BFI burst>5%（且 BFI>3% 才参与）
  type: metric
  source_pages: p414, p422
  source_chapter: VOIP PERFORMANCE & How-To / Additional VoIP parameters
  source_quote: |
    "VoIP quality thresholds used for predefined reports • Delay > Average Delay (150ms by default)
    • Packet loss > Loss rate (3% by default) • BFI Burst > Only used for the segment over 3% (5% by
    default)" (p414)
    "R&D defined that communication is bad when there is more than 3% of BFI during communication.
    ­ BFI Burst: ... is the rate of segment (10s) during a communication where there is 3% of BFI.
    R&D defined that communication is bad when the BFI burst is greater than 5%" (p422)
  summary: |
    三个 KPI 默认阈值：平均时延 >150ms；丢包率 >3%；BFI Burst >5%（BFI=Bad Frame Interpolation，设备
    为丢包/长时延补造的帧；通信 BFI>3% 时才统计 burst——burst 指通信中 BFI≥3% 的 10 秒段占比）。参数
    位置：Nmc > Application Configuration > Application Settings > Accounting > VoipParameters（Delay/
    Packet Loss/Bfi Burst 页签，按编解码 G711 等分子目录：SID 帧 packet size 1，语音包 G711>20 帧长
    20ms packet size 180，BFI rate 3）。
  conditions: 预定义报表即按此三阈值统计"超限票率"
  tags: [metric, voip, kpi, bfi]

- id: p39
  title: VoIP/报表清理周期：小时 45 天、日 94 天、月 15 月、年 36 月、票 15 天、报表 94 天
  type: metric
  source_pages: p421
  source_chapter: How-To / VoIP Performance / IP ticket purge
  source_quote: |
    "Clean VoIP hour old than 45 days (purge of VoIP hourly cumulative counters) — Clean VoIP day old
    than 94 days — Clean VoIP month old than 15 months — Clean VoIP year old than 36 months — Clean
    VoIP ticket old than 15 days (purge of VoIP records) ... Clean VoIP Reports 94 days" (p421)
  summary: |
    清理默认值（Preferences > Accounting > Accounting preference）：VoIP 小时计数器 45 天、日计数器 94
    天、月计数器 15 个月、年计数器 36 个月、VoIP 票据 15 天；VoIP 报表 94 天（Preferences > Reports >
    Reports preference）。
  conditions: 计费票据另有独立的归档生命周期（见 p48）
  tags: [metric, purge, voip]

- id: p40
  title: 流量分析阈值与计数器存储：话务台阈值 5s/10s（初始化 30s/60s）；T1/T2 独立；计数器保留 10-1488 个半小时
  type: metric
  source_pages: p443-445
  source_chapter: How-To / Traffic Analysis application
  source_quote: |
    "Configure the Attendant thresholds: ­ Threshold 1: 5 s ­ Threshold 2: 10 s ... On initialization,
    the threshold values are: Threshold 1: 30 seconds, Threshold 2: 60 seconds." (p443)
    "Number half-hour Period Kept ... (values between 10 and 1488) Example: 1488 = 1488/48 =31 i.e.
    31 days counting will be stored on disk" (p443)
    "T1 and T2 are waiting thresholds for incoming external calls (calling trunks). These thresholds
    are not related to the waiting thresholds for attendants ... By default, T1 and T2 are
    respectively set at 30 sec. and 60 sec." (p445)
    "Base station busy trigger — 8 by default (RBS) ... 4 by default (IBS)" (p444)
  summary: |
    两组独立阈值：(1) 话务台等待阈值（OXE 配置 Applications > Traffic Observation > 1，仅能在 OXE 侧
    改）：实验设 5s/10s，出厂 30s/60s；(2) 8770 侧订户等待阈值 T1/T2（Loading > Traffic analysis，
    默认 30s/60s，实验设 10s/20s）——两者互不相干。中继组占用阈值（Busy Threshold）；计数器保留期
    Number half-hour Period Kept 取 10-1488 个半小时（1488÷48=31 天）。DECT 基站忙触发：RBS 默认 8、
    IBS 默认 4（Mixed 类型两者都可配）。
  conditions: 订户阈值用于特定报表字段
  tags: [metric, traffic-analysis, thresholds]

- id: p41
  title: PtpType 任务参数：默认只算话务台/话务台组/中继组；改 ALL 才算被叫号与终端
  type: rule
  source_pages: p446-447
  source_chapter: How-To / Traffic Analysis / Updating the daily and weekly jobs
  source_quote: |
    "The task Traffic performance cumulative counters calculation of the daily and weekly jobs only
    concerns the Attendant, the Attendant group and the Trunk groups (default observed objects)
    ... Replace -PtpType ATT,ATG,TRG –PTP by -PtpType ALL -PTP" (p446)
  summary: |
    Scheduler 里 Daily Job 与 Weekly Job 的"Traffic performance cumulative counters calculation"任务
    命令默认为 -PtpType ATT,ATG,TRG -PTP（只算话务台/话务台组/中继组计数器）；要加载被叫号与终端
    （及 DECT）计数器必须改成 -PtpType ALL -PTP（两处任务都要改）。备注注明此修改同时授权加载来话
    记录。
  conditions: DECT/被叫观察还须在 Loading 里勾选对应对象以优化库操作（p445）
  tags: [rule, scheduler, ptp]

- id: p42
  title: 变化率公式与移动平均默认期（日 30/月 3/年 1）与示例 25%
  type: formula
  source_pages: p462-463, p476
  source_chapter: TRACKING APPLICATION & How-To / MonitoringParameters
  source_quote: |
    "Variation rate = 100 * ( current value of the data – average of the x last values of the data)
    / average of the x last values of the data — X is called moving average period • Day (x = 30 days
    by default) • Month (x = 3 months by default) • Year (x = 1 year by default)" (p462)
    "Variation rate for the date n — Rate = 100 * (10 – 8)/8= 25%" (p463)
    "Daily moving average period — 2 (default value is 30 days) ... Max number of alarms — 50 by
    default" (p476)
  summary: |
    公式：变化率=100×(当前值−前 x 期均值)÷前 x 期均值。移动平均默认期：日=30 天、月=3 个月、年=1 年；
    在 Administration > ... > Accounting > MonitoringParameters 修改（实验 Profile 3 改 Daily=2）；
    Max number of alarms 默认 50。教材示例：前 5 日呼叫数 8/9/6/7/10，均值 8，当日 10 → (10−8)/8×100
    =+25%。适用于 Accounting 的 Cost/Duration/Number of calls variation 类跟踪值。
  conditions: 变化率只在选定周期的跟踪值上生效
  tags: [formula, tracking, variation]

- id: p43
  title: Tracking 档案三实例规格与默认档案/Reset 机制
  type: metric
  source_pages: p470, p478
  source_chapter: How-To / Tracking application
  source_quote: |
    "Profile 1 ­ Monthly number of outgoing calls > 30 ➔ Generate an alarm ­ Monthly number of
    outgoing calls > 50 ➔ Send an e-mail to alban.podX@company.com — Profile 2 ­ Daily call duration
    of outgoing calls > 45 minutes ➔ Generate an alarm ­ Daily call duration of outgoing calls >
    1 hour ➔ Send an e-mail — Profile 3 ­ Daily duration variation of incoming and outgoing calls >
    100 % ➔ Generate an alarm and send an e-mail ... Average is calculated on the 2 last days" (p470)
    "The profile applies only to entities using the default profile (Default Tracking box selected).
    If you want to force assignment to all entities, select the corresponding Reset Profile option
    The Default Tracking box of each entity is then forced to YES" (p478)
  summary: |
    实验三档案（动作可单独或组合：告警/邮件/两者）：Profile 1=月呼出次数 >30 告警、>50 邮件；Profile 2=
    日呼出时长 >45 分钟告警、>1 小时邮件；Profile 3=出入呼日时长变化率 >100%（均值取前 2 天）→ 告警+
    邮件。分配机制：Default Tracking 管理器按"实体类型"挂默认档案，只影响 Default Tracking 勾选的实体；
    Reset Profile 把该类型全部实体的 Default Tracking 强制为 YES；单条目指定档案须先取消 Default
    tracking 再选档案（实验：Brest→Profile 1、Colombes→Profile 2）。运营商条目同样可挂 Tracking。
  conditions: 邮件地址实验口径 alban.podX@company.com
  tags: [metric, tracking, profiles]

- id: p44
  title: Web Performance 轮询口径：SNMP 默认 30 分钟、最低 5 分钟（R5.0 GA/MD1 分界）；widget 刷新同步；同屏最多 6 元素
  type: metric
  source_pages: p492, p503, p507
  source_chapter: WEB PERFORMANCE APPLICATION
  source_quote: |
    "Automatic retrieval via a fixed 30 minutes polling timer (R5.0 GA) and a manageable one with 5
    minutes minimum (R5.0 MD1)" (p492)
    "A maximum of 6 elements can be selected — For trunks, disk, IP domains and entities" (p503)
    "SNMP counters polling time interval from 30 min (default) to minimum 5 min • Polling time to
    retrieve SNMP counters managed via ToolsOmniVista.exe — Data widgets refreshed every 30 min
    (default) • Can be reduced to 5 min" (p507)
  summary: |
    三条口径：(1) SNMP MIB 轮询 R5.0 GA 固定 30 分钟，R5.0 MD1 起可管理、最低 5 分钟（经
    ToolsOmniVista.exe 的 SNMP 菜单）；数据 widget 刷新默认 30 分钟、可缩至 5 分钟；(2) widget 内单参数
    最多选 6 个元素（中继/磁盘/IP 域/实体）；(3) 版本分界：R5.0 GA 与 R5.0 MD1。
  conditions: 原始数据（raw data）显示仅当选定周期=最后一天（p499）
  tags: [metric, web-performance, polling]

- id: p45
  title: SNMPv3 双侧参数（实验口径）：agentV3/superuser/SHA/AES/pwdagentV3；OID 示例=在服话机数
  type: metric
  source_pages: p510-513
  source_chapter: How-To / Web Performance application
  source_quote: |
    "SNMPv3 Username: agentV3 ­ SNMPv3 Username password: superuser ­ SNMPv3 Cypher Passphrase:
    pwdagentV3" (p510)
    "snmpget -v 3 -l authPriv -u agentV3 -a SHA -A superuser -x AES -X pwdagentV3 -E
    8000027D046F786531 localhost .1.3.6.1.4.1.637.64.4400.1.7.0 — A4400-CPU-MIB::a4400CPU.7.0 =
    INTEGER: 5 ... gives the number of sets in service in the system (here: '5')" (p512)
    "SNMP port ... (i.e. 161) — SNMP security level ... (i.e. v3) ... Encryption protocol ... (i.e.
    AES128)" (p513)
  summary: |
    实验口径全参数：OXE 侧（SNMP Configuration > 1 > SNMP Global Configuration）版本 V3、先 Disable 配
    置再 Enable、Agent SNMPv3 Users=agentV3/superuser/pwdagentV3、Contact/Location/Community=public；
    验证命令 snmpget（如上，OID .1.3.6.1.4.1.637.64.4400.1.7.0 返回在服话机数=5）。8770 侧（Connectivity
    页签）：SNMP port 161、security level v3、community public、V3 user agentV3、认证 SHA/superuser、
    加密 AES128/pwdagentV3；PCX 页签勾 SNMP performance monitoring。
  conditions: 口令为实验口径；8770 校验双侧一致性，不一致则出告警并停用 SNMP 监控（p511）
  tags: [metric, snmpv3, lab]

- id: p46
  title: 归档参数：Archive delay 31（不带 D）+ Clean-up delay 94D（必须带 D）= 最长 125 天；按记录日期清理
  type: metric
  source_pages: p529-530, p523
  source_chapter: How-To / Accounting Records Archiving
  source_quote: |
    "Archive Delay — Defined in days (default value: 31) – Don't add the symbol D after the value.
    ... Clean-up delay — Defined in days (default value: 94D) – The symbol D must be added after the
    value. Archive files stored in the default path are deleted after a total number of days equals
    to Archive delay + Clean-up delay (31+94=125 days). This deletion is performed according to the
    date of the records and not to the creation date of archive files." (p529)
  summary: |
    两个参数单位规则不同：Archive Delay=31（天数，**不能**带 D 后缀）；Clean-up delay=94D（**必须**带
    D 后缀）。合计 31+94=125 天后删除，且按记录日期而非档案文件创建日期算。默认归档路径
    C:\8770_ARC\Accounting\tickets；Archive activation 勾选才允许归档；配置双入口（Administration >
    NmcArchive > Accounting 与计费应用 Preferences）。归档任务范围=上次归档日到当前日期−31 天。
  conditions: 实验把 Archive delay 设 1 天、Clean-up delay 3 年做演示（p529 Implementation）
  tags: [metric, archiving]

- id: p47
  title: 恢复标签语义：Loaded records（入树、与原票不可区分）vs Archived records（打标、树中不可见、可单独清除）
  type: rule
  source_pages: p537, p543, p548
  source_chapter: How-To / Accounting Records Archiving / Restoring
  source_quote: |
    "Loaded records: Without label (visible in the organization). Archived records: with label (the
    restored records are not visible in the organization)." (p537)
    "You can check that the records of January are restored as loaded record. There is no way to make
    a difference between the already loaded records and the ones just restored from archives." (p543)
    "Record origin = Loaded record if the record comes from a PCX or if the record has been restored
    with the label Loaded record — Record origin = Restored record if ... restored with the label
    Archived records ... Only restored records ... This option only deletes records restored with the
    label Archived records." (p548)
  summary: |
    恢复两标签：Loaded records=无标签、进组织树、与原始加载票完全不可区分；Archived records=带标签、
    组织树 Records 页签不显示（但报告可见，Record Origin 列可过滤）， purge 时可选 "Only restored
    records" 单独清掉。Cost entry 二选一：Without recalculation（沿用归档时的运营商成本）或 With
    recalculation（恢复时重算——运营商有效期必须覆盖被恢复记录日期）。
  conditions: 恢复按单日（选 archZ 文件）或按周期（日期区间+勾节点）两种入口
  tags: [rule, restore, labels]

- id: p48
  title: VoIP 报告取数前提：呼叫必须是跨 POD 的出局呼叫；同机软话机互打出不了报告
  type: rule
  source_pages: p423, p428
  source_chapter: How-To / VoIP Performance / Maintenance & Report view
  source_quote: |
    "Manage some calls between OXE IP phones in order to generate some IP tickets ... All calls must
    be external outgoing calls from one pod to another. Use the command 'account compress' if needed."
    (p423)
    "To generate a report with data, all calls must external outgoing call from one pod to another.
    If the source and destination of external calls are in the same computer (Windows 10 instance),
    using IPDSP and MicroSIP softphones, no VoIP traffic calls can be retrieved in the generated
    report." (p428)
  summary: |
    实验口径规则：VoIP 报告有数据的前提是通话为"跨 POD 的出局呼叫"（走模拟器公网腿）；同一台虚机里
    IPDSP 与 MicroSIP 互打虽也出票，但取不回可用的 VoIP 质量数据，报告为空。排障时先核对呼叫路径再查
    配置。预定义报告生成过滤器：Date/Hour=This Week、System not empty、Sender IP address not empty、
    Board + Phone number not empty。
  conditions: 报告类型选 Voice over IP > Traffic analysis > Equipment > Detailed Report
  tags: [rule, voip, lab]

- id: p49
  title: WBM 访问口径：https://nms:8443 → NETWORK MANAGEMENT → AdminNmc；WBM Users 需 Unified Management 许可
  type: metric
  source_pages: p35, p514
  source_chapter: 8770 WBM CLIENT & How-To / Web Performance
  source_quote: |
    "https://nms.company.com:8443 — Select NETWORK MANAGEMENT — Login: Enter the login session (i.e.
    AdminNmc) — Password: ... (i.e. Superuser01*)" (p514)
    "Available with Unified Management license • Zero footprint (light client)" (p35)
  summary: |
    WBM 入口：https://<服务器>:8443，选 NETWORK MANAGEMENT 卡，用 AdminNmc/Superuser01*（实验口径）
    登录，Performance 应用即在其中。WBM Users 应用（统一用户管理）需 Unified Management 许可；公司
    目录树管理受 Company Directory 许可约束；零足迹轻客户端。
  conditions: 实验口径；生产用客户 FQDN 与证书
  tags: [metric, wbm, licensing]

- id: p50
  title: 报表导出默认命名与实例查询：导出名=定义名+生成日期
  type: rule
  source_pages: p373
  source_chapter: How-To / Reports application / Exporting
  source_quote: |
    "By default, it takes the name of the definition from which the report originated, followed by
    its generation date." (p373)
  summary: |
    报表导出到文件时的默认文件名=来源定义名+生成日期；格式 TXT/HTML/PDF/EXCEL 四选一；也可按邮箱导出
    （可多目的地）。生成三入口：Generate Report（正常）/ Generate report w/o mask（解密，需口令）/
    Schedule（定时，可同时打印/导出）。
  conditions: 定时实验：每日 5:00 AM、排除周六周日
  tags: [rule, reports, export]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 23 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | OXE 纳管 | 有 | p07, p08, p09 | 声明公式、核查命令、同步语义 |
| task-02 | SIP 模拟器对接 | 有 | p10 | pbxN/DID 参数 |
| task-03 | OXE 外部计费开启 | 有 | p03, p04, p05, p11 | 缓冲/出票规则、开启参数、成本中心 |
| task-04 | 维护命令核查 | 有 | p06 | 四命令清单 |
| task-05 | 票据回收链路 | 有 | p12, p13, p14, p15 | 方法原则、FTP 铁律、PCS、五道闸 |
| task-06 | 币种/税/国家 | 有 | p22 | 参考币种/汇率/税率 |
| task-07 | Telecom 1 建模 | 有 | p16, p17, p18, p23 | 命名、前缀规则、公式族、全表 |
| task-08 | 运营商演进 | 有 | p17, p25 | 前缀唯一性 + 重算规则 |
| task-09 | Telecom 2 | 有 | p24 | 参数表 |
| task-10 | Service 脉冲运营商 | 有 | p19, p20, p24 | 脉冲公式、SVA 模型 |
| task-11 | Code Book | 有 | p26 | 格式与导入五规则 |
| task-12 | 组织树搭建 | 有 | p27 | 归属与搬移权限矩阵 |
| task-13 | 历史数据迁移 | 有 | p28 | 回溯与重建四规则 |
| task-14 | 掩码与解密 | 有 | p29, p30, p11 | 掩码规则、解密规则、OXE 侧遮蔽 |
| task-15 | 成本档案 | 有 | p31, p32 | 公式与订阅出票规则 |
| task-16 | 可见域 | 有 | p33 | 四条规则 |
| task-17 | 报表生成/导出/定时 | 有 | p34, p35, p50 | 尺寸上限、邮件、命名 |
| task-18 | 报表定制 | 有 | p36, p37 | Detailed/Grouped 与版面规则 |
| task-19 | VoIP 性能 | 有 | p38, p39, p48 | KPI 阈值、清理周期、取数前提 |
| task-20 | 流量分析 | 有 | p40, p41 | 双阈值、PtpType |
| task-21 | Tracking | 有 | p42, p43 | 变化率公式、档案规格 |
| task-22 | Web Performance | 有 | p44, p45, p49 | 轮询、SNMPv3、WBM 入口 |
| task-23 | 归档恢复 | 有 | p46, p47 | 参数规则与标签语义 |

**覆盖结论**：23/23 全部有对应条目，无缺口。三点口径说明：
1. p50 表格中 p89 的 31011 姓/名矛盾、p402 vs p550 汇率矛盾、p607 "Telecom 7/0" 笔误，均属书内缺陷，归 counter-example.md（n 条目），本文件只收录作者意图明确且前后一致的口径。
2. 实验数值（税率 10%/20%、汇率 1.21/0.82、密码、邮箱地址）均已标注"实验口径"。
3. 版本号保留完整位数：R5.0 GA、R5.0 MD1、R101.1-n4、AHV 20220304。
