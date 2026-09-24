# 术语/缩写/产品名候选 — OmniVista 8770 R5.2 计费与性能管理 (8770XTE201EN Ed45)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 69 条（concept 30 / role 5 / subscription 3 / product 17 / protocol 8 / resource 6）。WBM/NMC/OMC/MOS/RTCP-XR/NDDI/ABC-F/PWT/DECT/RBS/IBS/CAC/GD/GA/PTP/OOS/NOE/INTIP 等缩写书中未给全称，full_name 字段如实省略，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: Accounting record / ticket
  category: concept
  source_pages: p61-62, p66
  source_quote: |
    "Accounting records storage (max 500 records) ... Generated at the end of the call" (p62)
    "(00) TicketVersion = ED5.2 (01) CalledNumber = ... (47) TimeDlt = 0" (p66，accview 展示的 47 字段票据)
  definition: |
    OXE 在呼叫结束时生成的话务票据（本书 ticket=record 同义）：最长 47 个字段（ED5.2 版式），含被叫号/
    计费号/成本中心/呼叫类型/时长/中继组/单元数等；先入内存缓冲，落盘成 TAX 文件。是全书计费链的
    原子数据。
  alias_or_related: 承载文件见 g02/g03；出票规则（duration=0 也出票）见 BOOK_OVERVIEW 命题 1
  tags: [concept, accounting, core]

- id: g02
  term: ACCOUNT.LIS / TAX*****.DAT / tax.tmp
  category: concept
  source_pages: p62-65
  source_quote: |
    "Compressed files containing accounting records — TAX*****.DAT ... AAAAA <= ***** <= ZZZZZ ...
    Contains the list of accounting files created on the OXE — ACCOUNT.LIS ... Buffer file used when
    memory buffer is full — tax.tmp" (p62)
  definition: |
    OXE 计费文件三件套：TAX*****.DAT=压缩票据文件（序号 AAAAA→ZZZZZ 递增）；ACCOUNT.LIS=DAT 清单
    索引（8770 据此做增量对比）；tax.tmp=缓冲满时的过渡文件。都在 /usr4/account。IP/SIP 票据同构
    （IP.LIS/SIP.LIS、IP*.DAT/SIP*.DAT）。
  alias_or_related: IP.LIS/SIP.LIS 见 g34；pmm.lis 见 g35
  tags: [concept, accounting, files]

- id: g03
  term: Accounting methods（五种计费方法）
  category: concept
  source_pages: p99-102
  source_quote: |
    "Each PCX may have a specific accounting method" (p99)
  definition: |
    每台 PCX 独立选择的计费处理方式，五选一：No accounting / Detailed accounting（默认推荐：更新
    组织树+取票归到分机）/ Organization update without records retrieval（建树期）/ Global per node
    without records retrieval / Global per node with records retrieval（实体键=网络号×1000000+节点号）。
  alias_or_related: 方法选择顺序原则见 BOOK_OVERVIEW 命题 1 与 counter-example n09
  tags: [concept, accounting, methods]

- id: g04
  term: Cost center（成本中心）
  category: concept
  source_pages: p89, p256
  source_quote: |
    "The cost center is created by default. You just have to manage the name associated to a cost
    center." (p89)
    "If no cost center defined (cc=255) in the PCX — Chargeable entry placed under root of
    organization tree" (p256)
  definition: |
    OXE 侧为用户/话务台/数据终端指定的记账单位，组织树的主要挂载点；编号即槽位（默认已建，只配名字），
    cc=255 表示未指定（落组织根）。修改只能经 OXE 配置（Rights 页签）或公司目录。
  alias_or_related: 无成本中心对象归"默认成本中心"（g05）
  tags: [concept, accounting, organization]

- id: g05
  term: Default cost center
  category: concept
  source_pages: p257, p260, p271
  source_quote: |
    "By completing the Default cost center attribute in Data collection tab of the PCX
    (Configuration application)" (p257)
    "Such cost center is assigned to the charging items without cost center parameter (like trunk
    group, attendant group)" (p271)
  definition: |
    在 OXE 的 Data collection 页签配置的兜底成本中心：中继组、话务台组、语音信箱、工程等无成本中心
    参数的计费对象统一落到这里；也可事后在组织图上剪贴归位（不影响话机侧）。
  alias_or_related: 搬移权限边界见 counter-example n18
  tags: [concept, accounting, organization]

- id: g06
  term: Organization tree / chargeable entry
  category: concept
  source_pages: p253-256
  source_quote: |
    "Graphical view of the financial organization • Based on a tree structure of chargeable entries
    • Gives an overview of current and past organization" (p253)
  definition: |
    财务组织的图形化树：节点类型 level（层级）/cost center（成本中心）/chargeable entry（可计费条目：
    用户、话务台、数据终端、中继组等）；同时呈现过去与现在，随 OXE 同步/事件与公司目录变化自动更新。
  alias_or_related: 历史条目见 g07；更新语义见 g08
  tags: [concept, accounting, organization]

- id: g07
  term: Inactive entry（灰色历史条目）
  category: concept
  source_pages: p258, p284, p287
  source_quote: |
    "Even if the move is successful ... there is an history trace of the previous status. This
    previous status is symbolized by a grey entry." (p284)
    "The copied item keeps its accounting records and performance counters and becomes inactive.
    The pasted item is active." (p287)
  definition: |
    组织树中的历史痕迹条目（显示为灰色）：条目改名/换成本中心/复制后，旧位置留下带其记录的 inactive
    影子；ToolsOmniVista 组织更新会清除它们并把票据重挂到活动条目。
  alias_or_related: ToolsOmniVista 见 g22；破坏性边界见 counter-example n21
  tags: [concept, organization, history]

- id: g08
  term: Cut & paste / Copy & paste / Assign earlier creation date
  category: concept
  source_pages: p261-264
  source_quote: |
    "Cut & paste • This operation consists in moving an entry without history ... Copy & paste •
    This operation consists in moving an entry with history" (p261-262)
    "Allows reallocation of accounting records and performance counters from an inactive user to an
    active user having the same identity • A user is identified by the couple PCX ID/directory
    number" (p263)
  definition: |
    组织更新三种手工语义：剪贴=无历史搬移；复制=带历史另立（原件转 inactive）；回溯创建日期=把非活动
    条目的记录按创建日期重挂到同身份（PCX ID+分机号）的活动设备——只能选"设备"，level/成本中心/人
    不可回溯。
  alias_or_related: 全局版=ToolsOmniVista（g22）
  tags: [concept, organization, operations]

- id: g09
  term: Mask profile
  category: concept
  source_pages: p298-302, p306
  source_quote: |
    "Following record data may be masked • Called number, Caller number, PIN (Personal Identification
    Number), Cost, Destination area (City/Country name), Call duration, Call date" (p298)
    "The displayed number has priority over the masked one." (p306)
  definition: |
    机密性档案：按呼叫类别（Personal/Project/Professional/Guest，加 Default 档案专属的 Masked/Unmasked
    group）控制被叫号、主叫号、PIN、成本、地名、时长、日期的显示/遮蔽位数；随组织树继承，只影响显示
    不删数据。
  alias_or_related: grouped 报表只认 Default（n23）；解密见 g24
  tags: [concept, mask, confidentiality]

- id: g10
  term: Accounting domain / Visibility domain
  category: concept
  source_pages: p343-346
  source_quote: |
    "Definition of Administrator accounts to only access data for levels and cost centers regarding
    their domain viewing rights" (p343)
  definition: |
    挂在组织树节点上的可见性域名：管理员被分配域后只见域内数据与报表；未配域=不可见；功能开关关闭=
    全可见。AdminNmc 凭根域看全部。群组级配置无效，只认用户级。
  alias_or_related: 启用顺序坑见 counter-example n26
  tags: [concept, domains, access-control]

- id: g11
  term: Cost profile / Invoiced cost
  category: concept
  source_pages: p323-325, p333
  source_quote: |
    "Modify the cost of the communication • Increase or decrease the cost • The modified cost
    corresponds to the invoiced cost" (p323)
    "Type Linear Equation (Ax+B) or percentage (x+A%x)" (p333)
  definition: |
    成本档案第一块：对总成本（直连运营商成本+ISDN 成本+间接运营商成本）做线性/百分比调整得到"发票价"
    （内部再计费/加价/折扣），按呼叫类型定义、随组织树继承。
  alias_or_related: 订阅费在同档案另两页签（g12）；换算示例见 principle p31
  tags: [concept, cost-profile, invoicing]

- id: g12
  term: Subscription record（订阅票）
  category: concept
  source_pages: p327
  source_quote: |
    "Accounting records including only subscription costs are generated by Omnivista 8770 after each
    synchronization" (p327)
  definition: |
    8770 在每次同步后生成的"纯订阅费"会计记录：按持有设备/语音信箱/DDI 号（Services subscriptions）
    与分机类型（Station subscription）计价，日/周/月三种周期（周日/每月 1 日出票，时间戳 00:00:00）；
    月订阅当月加入次月起计；订阅计算永不处理当天。
  alias_or_related: 重算机制=删了重建（counter-example n25）
  tags: [concept, subscription, invoicing]

- id: g13
  term: Carrier（direct carrier / pulse type carrier）
  category: concept
  source_pages: p117, p152, p218
  source_quote: |
    "The carrier configuration allows calculating the cost of records retrieved from the PCX" (p117)
    "Right click on Carrier and select Create a pulse type carrier" (p218)
  definition: |
    8770 里的资费容器（不代表真实运营商合同）：Name 全局唯一、Symbol ≤5 字母唯一、Type=Outgoing、
    Country 仅为信息。分两类建法：直连（direct）运营商走 Period>四件套；脉冲型（pulse，如 Service）
    建时直接定 Unit cost/Tax/Currency，Tariff 自动生成。
  alias_or_related: 对象模型见 g14-g17
  tags: [concept, carrier, core]

- id: g14
  term: Calling region / Called region
  category: concept
  source_pages: p118, p154-156
  source_quote: |
    "Calling region • Location of the caller: PCX or PCX-trunk group ... Called region • Contains
    call prefixes having the same cost from a given calling region • A call prefix corresponds to the
    n first digits of the called number ... A region can be both calling and called" (p118)
  definition: |
    资费的空间维度：主叫区域=PCX 或"PCX+中继组"（须填接入号码，仅信息用）；被叫区域=同资费被叫前缀
    集合（最优/最长匹配归属）；一个区域可兼具两角（如演进后的 Brest/Paris）。
  alias_or_related: 同一前缀不可跨区（n11）
  tags: [concept, carrier, region]

- id: g15
  term: Direction
  category: concept
  source_pages: p118, p172
  source_quote: |
    "Allows calls to be grouped according to the regions in which calls originate or arrive • A
    tariff is applied to each Calling Region - Called Region pair" (p118)
  definition: |
    资费的配对维度：主叫区域×被叫区域，唯一绑定通信资费（可选服务资费/调整/时延 Delay=拨完号到对端
    应答的平均等待秒数）；未定义组合由 "unspecified" 兜底方向承接。远端中继组场景票据记在中继组所在
    节点，方向按"中继组节点→被叫前缀"判定。
  alias_or_related: 服务资费绑定规则见 n14
  tags: [concept, carrier, direction]

- id: g16
  term: Tariff（资费：Day type / Time zone / Segment）
  category: concept
  source_pages: p127-135, p163, p171
  source_quote: |
    "Cumulated time zones must form a complete day." (p163)
    "A time zone is composed of one or several segments, depending on how charging varies during the
    time. ... a segment number must be set up to indicate the chronologic order." (p171 Notes)
  definition: |
    算价规则对象：Day type（Daily/Working day/Weekend/特定日）×Time zone（按时段切价，累计须铺满全天）
    ×Segment（时区内按通话时长分段单价，需排序）×计算模式（exact/round up-down/pulse/PCX 给定）与
    叠加参数（initial cost、initial duration、minimum cost、initial unit、unanswered call initial
    cost）。
  alias_or_related: 公式全表见 principle p18/p19；服务资费开关 Service Tariff mode
  tags: [concept, tariff, core]

- id: g17
  term: Adjustment
  category: concept
  source_pages: p138
  source_quote: |
    "Allows to increase or reduce the cost of a communication • Adjustment is configured using a
    linear equation (Ax+b) or a percentage (A%) • Adjustment can be applied to a tariff, a direction,
    a segment or a carrier"
  definition: |
    资费层的成本调整系数（线性 Ax+b 或百分比 x+A%x），可挂在资费、方向、段、运营商四类对象上；与
    Cost profile（发票价调整，作用于入库后成本）是两层不同的调价。
  alias_or_related: 对照 g11
  tags: [concept, carrier, adjustment]

- id: g18
  term: Period（资费有效期）
  category: concept
  source_pages: p152, p244
  source_quote: |
    "The expiry date of a period is automatically filled in when creating the next period." (p152)
    "From a same carrier, different periods can be added. Each period corresponding to a tariff
    definition which can evaluate according to price policy." (p244)
  definition: |
    运营商配置的有效期单元：新周期建立时旧周期自动封口；同一运营商可并存多个周期（价目随政策演进的
    正规做法，Code Book 改 EFFECT_DATE 再导入即新增周期）。
  alias_or_related: Calendar（特定日类型/日期）挂在周期下
  tags: [concept, carrier, period]

- id: g19
  term: Code book
  category: concept
  source_pages: p228-233
  source_quote: |
    "Codebook made up of text files • File extension is normalized • File name must be identical" (p228)
  definition: |
    运营商配置的文本文件集（.inf 总信息/.rgn 区域/.trf 资费/.dir 方向/.cal 日历/.ccn 城市-国家/.adj
    调整/.fct ISDN 服务/.itl 安装（PCX 清单）/.trg 中继组），用于跨服务器迁移与存档；@表头（.inf 除外）/
    Tab 分隔/%注释；.itl 的 Node 必须与目标机声明名一致。
  alias_or_related: 导入坑见 counter-example n15/n16
  tags: [concept, codebook, migration]

- id: g20
  term: Report definition / Generated report / Unmasked report
  category: concept
  source_pages: p361
  source_quote: |
    "Reports sorted by type of data and by type of reports • Report definition • Generated report
    • Unmasked report"
  definition: |
    报表树三类节点：definition（定义：Querytool 选数+Designer 排版的模板）、generated（按定义生成的
    实例）、unmasked（带解密口令生成的解密版实例）。预定义报表必须 Copy/Paste 到个人目录才能生成。
  alias_or_related: Querytool/Designer 结构见 framework f21
  tags: [concept, reports]

- id: g21
  term: Detailed report / Grouped report / Hit-list
  category: concept
  source_pages: p385, p393
  source_quote: |
    "Detailed: The detailed report does not summarize data ... Grouped: This type of report summarizes
    data retrieved from the database." (p385)
    "Hit-list Report — Limits the number of lines in the report. This parameter is used with grouped
    report definition." (p393)
  definition: |
    定义类型二分：Detailed 逐条不汇总（Operation 空）；Grouped 聚合（Operation=Group by/Count/Min/
    Max/Total/Average）。Hit-list=grouped 专用限量（如"时长最长的前 10 台话机"）。
  alias_or_related: 语义澄清见 counter-example n30
  tags: [concept, reports]

- id: g22
  term: ToolsOmniVista.exe
  category: concept
  source_pages: p266, p293
  source_quote: |
    "2 - Execution of the ToolsOmnivista.exe ... Records from inactive entries are reallocated to the
    active entry having the same identifier (node number and directory number) — Inactive entries are
    deleted" (p266)
  definition: |
    8770 服务器端命令行工具（C:\8770\bin\），菜单含 Security/Certificate Management/Accounting
    Organization Update/SNMP/Management Domain；其中组织更新会强制停 8770 服务、删除全部非活动实体并
    把票据与 Ptp 计数器重挂到活动实体——破坏性、不可逆。
  alias_or_related: 还承担 SNMP 轮询周期调整（p507）
  tags: [concept, tool, destructive]

- id: g23
  term: Tracking profile / Threshold
  category: concept
  source_pages: p457, p461
  source_quote: |
    "Set of thresholds grouped in a profile which can be applied to one or several Organization
    entries" (p457)
  definition: |
    阈值集合档案：每条定义含 Tracking value（会计/话务/VoIP/性能四域的指标）、Period、Threshold、Call
    Type、Action（告警/邮件/两者）；按实体类型设默认档案（Default Tracking）或对单条目指定；运营商
    条目同样可挂。
  alias_or_related: 变化率见 g25；覆盖面边界见 counter-example n35
  tags: [concept, tracking, threshold]

- id: g24
  term: Mask data access（组）/ Unmasking
  category: concept
  source_pages: p302, p314
  source_quote: |
    "Password required to generate the report — Report without mask" (p302)
    "IT IS NECESSARY TO CREATE AN 8770 LOGIN WHICH IS MEMBER OF THE GROUP 'MASK DATA ACCESS'." (p314)
  definition: |
    解密机制：默认禁止无掩码报表；把某 8770 账号加入"Mask data access"组后，任何人生成 w/o mask 报表
    时输入该组成员口令即可；解密程度仍受各档案 Unmasked 类别限制；组成员变更须重启 Reports 应用。
  alias_or_related: OXE 侧遮蔽不可解（n06）
  tags: [concept, security, unmasking]

- id: g25
  term: Variation rate / Moving average period
  category: concept
  source_pages: p462-463
  source_quote: |
    "Variation rate = 100 * ( current value of the data – average of the x last values of the data)
    / average of the x last values of the data — X is called moving average period"
  definition: |
    Tracking 的变化率跟踪值：当前值对前 x 期移动平均的偏离百分比；x 按周期默认日 30 天/月 3 月/年 1 年，
    在 MonitoringParameters 修改（另有 Max number of alarms，默认 50）。
  alias_or_related: 公式示例（+25%）见 principle p42
  tags: [concept, tracking, formula]

- id: g26
  term: IP ticket / segment
  category: concept
  source_pages: p408-409
  source_quote: |
    "A call between 2 IP devices is divided into one or more segments • IP tickets are generated at
    the end of each segment and give information about the direction of communication" (p408)
  definition: |
    VoIP 话单：按通话段出票（跨节点即多段、双向各一票），字段含节点/机框/板卡、设备类型（INTIP、
    IP-Phone、GA、GD、4645）、源/目的 IP 与分机、时长、压缩算法（G711/G723/G729A）、收发丢包数、时延
    表、BFI 密度。
  alias_or_related: 质量口径见 g27
  tags: [concept, voip, core]

- id: g27
  term: MOS / BFI / BFI Burst / KPI
  category: concept
  source_pages: p408, p414, p422
  source_quote: |
    "Qualitative: information about delay, packet loss, BFI, MOS" (p408)
    "BFI: 'Bad Frame Interpolation' is a packet created by VoIP equipment in case of problem ... R&D
    defined that communication is bad when there is more than 3% of BFI ... 'BFI Burst' is the rate
    of segment (10s) during a communication where there is 3% of BFI ... bad when the BFI burst is
    greater than 5%" (p422)
  definition: |
    VoIP 质量指标族：时延（默认阈值 >150ms）、丢包（>3%）、BFI（设备为丢包/长时延补造的帧；>3% 判坏），
    BFI Burst（通信中 BFI≥3% 的 10 秒段占比；>5% 判坏）；MOS 为质量分（书中未展开全称），散点图呈现。
    KPI=Key Performance Indicators（书中展开）。
  alias_or_related: KPI/SLA Overflow 触发告警与邮件（p413）
  tags: [concept, voip, quality]

- id: g28
  term: CDR（Call Detail Record）
  category: concept
  source_pages: p492
  source_quote: |
    "CDR stands for Call Detail Record: set of data emitted at the end of a call by the Call Server
    for billing purposes • Proprietary format for IP devices, IPMG, 4645 and IP-xBS… RTCP-XR format
    for SIP devices" (p492)
  definition: |
    话终话单（书中展开全称）：呼叫服务器在通话结束时发出的计费数据集；Web Performance 经同步与小时
    轮询取回，IP 设备用专有格式、SIP 设备用 RTCP-XR 格式。
  alias_or_related: 与计费票据（g01）同源不同消费面
  tags: [concept, cdr, voip]

- id: g29
  term: archZ / Accounting archiving
  category: concept
  source_pages: p520-523
  source_quote: |
    "File extension = archZ (Zipped archive format) • One file per day and per node (if at least 1
    record to archive)" (p521)
  definition: |
    计费票据归档机制：zip 格式档案、每天每节点一档；任务归档范围为上次归档日到"当前日期−31 天"；
    Archive delay（31，不带 D）+Clean-up delay（94D）=最长 125 天，按记录日期清理。
  alias_or_related: 恢复标签见 g30
  tags: [concept, archiving]

- id: g30
  term: Record origin（Loaded records / Archived records）
  category: concept
  source_pages: p537, p548
  source_quote: |
    "Loaded records: Without label (visible in the organization). Archived records: with label (the
    restored records are not visible in the organization)." (p537)
  definition: |
    恢复票据的来源标签：Loaded=无标签、进组织树、与原始票不可区分；Archived=带标签、树中不可见但报告
    可见、可被 "Only restored records" 单独清除。恢复成本可选沿用归档值或重算（运营商有效期须覆盖）。
  alias_or_related: 审计建议见 counter-example n40
  tags: [concept, archiving, restore]

# ── 二、角色/账号 (role) ──

- id: g31
  term: AdminNmc
  category: role
  source_pages: p47, p75, p343
  source_quote: |
    "8770 credentials: • AdminNmc — superuser — Superuser01*" (p47)
    "Here are the credentials to connect to the OmniVista 8770 server Login: AdminNmc Password:
    Superuser01*" (p75)
    "AdminNmc account have access to complete accounting organization" (p343)
  definition: |
    8770 主管理员账号（书中未展开全称）：实验口径口令 Superuser01*；可见域机制下分配根域即全域可见；
    报表个人目录 AdminNmc 亦以此为名。
  alias_or_related: superuser 为 cn=directory manager 口径（见 g34）
  tags: [role, admin, lab]

- id: g32
  term: adfexc
  category: role
  source_pages: p77, p109
  source_quote: |
    "FTP Username / FTP Password — adfexc ... This is the OXE FTP login and password used for data
    retrieval." (p77)
    "Do not modify the FTP user to avoid a problem at verification of the license." (p109)
  definition: |
    OXE 侧供 8770 FTP 取数的专用账号（书中未展开全称）：8770 PCX 页签必须填它且用户名禁改（许可校验），
    密码须与 OXE 保持一致。
  alias_or_related: 铁律详见 counter-example n08
  tags: [role, oxe, ftp]

- id: g33
  term: mtcl
  category: role
  source_pages: p47, p77, p93
  source_quote: |
    "Username maintenance Enter the mtcl account name (i.e. mtcl)" (p77)
  definition: |
    OXE 维护账号（书中未展开全称）：OXE 声明的 Software download 页签与 SSH/串口登录用它（实验口径
    密码 Superuser2580*）；account compress/accview 等维护命令在该会话执行。
  alias_or_related: 实验同批账号 root/swinst（p47 设置表）
  tags: [role, oxe, maintenance, lab]

- id: g34
  term: cn=directory manager
  category: role
  source_pages: p293
  source_quote: |
    "Please enter password of cn=directory manager : *********" (p293)
  definition: |
    8770 目录服务的顶层管理身份：ToolsOmniVista.exe 执行组织更新等敏感操作时索要其口令（实验口径
    superuser）。
  alias_or_related: 与 g31 AdminNmc 是两套身份
  tags: [role, directory, lab]

- id: g35
  term: MCS（Managed Communications Services）
  category: role
  source_pages: p13
  source_quote: |
    "MCS* customers -> outsourced and remote OAMP performed by a service provider. * MCS : Managed
    Communications Services"
  definition: |
    托管通信服务客户形态：8770 的 OAMP（书中未展开全称）外包给服务商远程执行；Administration 应用
    支持按 MCS 客户清单管理。书中仅定位提及，无部署细节。
  alias_or_related: 全书唯一定义处 p13
  tags: [role, managed-services]

# ── 三、许可/订阅 (subscription) ──

- id: g36
  term: Unified Management license
  category: subscription
  source_pages: p35
  source_quote: |
    "Available with Unified Management license • Zero footprint (light client)" (p35)
  definition: |
    解锁 8770 WBM Users 应用（终端用户/目录树统一管理）的许可；WBM 本身零足迹轻客户端。
  alias_or_related: 另有 Management domains 选项（Domains for management）
  tags: [subscription, license, wbm]

- id: g37
  term: Company Directory license
  category: subscription
  source_pages: p35
  source_quote: |
    "Management of the Company Directory tree structure (submitted to Company Directory license)" (p35)
  definition: |
    公司目录树层级管理的许可门槛：无此许可时 WBM Users 的目录树管理受限。
  alias_or_related: thick client Directory 应用的附加选项（AD 同步/复制/LDIF）另列（p32）
  tags: [subscription, license, directory]

- id: g38
  term: Accounting license / Ticket collector license
  category: subscription
  source_pages: p103
  source_quote: |
    "PCX accounting files available to an external accounting application • No accounting license,
    only Ticket collector license is required" (p103)
  definition: |
    计费相关许可两档：完整计费应用需 accounting 许可；只做票据收集器（把 PCX 票据文件供给外部计费
    应用，文件落 C:\8770\data\collector）仅需 Ticket collector 许可。
  alias_or_related: FTP 用户名禁改与许可校验相关（n08）
  tags: [subscription, license, collector]

# ── 四、产品/组件 (product) ──

- id: g39
  term: OmniVista 8770（server / OV8770）
  category: product
  source_pages: p5-8, p47
  source_quote: |
    "Centralized network management solution" (p5)
    "OMNIVISTA 8770 SERVER 8770_OV8770_SETUP nms 192.168.1.70" (p47)
  definition: |
    ALE 集中式网管服务器（本书主角）：IP 连通纳管 OXE/OXO Connect/OpenTouch，承载计费、性能、目录、
    配置、告警五域；可物理 Appliance 或虚机部署；图示缩写 OV8770。
  alias_or_related: 客户端形态见 g40/g41/g42；架构协议见 framework f04
  tags: [product, nms, core]

- id: g40
  term: 8770 Client（thick client）
  category: product
  source_pages: p6, p10
  source_quote: |
    "Graphical User Interface (GUI) to manage 8770 applications • Simultaneous access to OmniVista
    8770 Server • Requires a login and password" (p6)
  definition: |
    8770 厚客户端（Java 图形界面）：五套件全功能入口（Setup/Network/Reporting/Directory/PCX 管理），
    登录口令进入，多客户端可同时访问服务器。
  alias_or_related: 与 g41 WBM 的功能边界见 n02
  tags: [product, client]

- id: g41
  term: 8770 WBM client
  category: product
  source_pages: p6, p11, p34-38, p514
  source_quote: |
    "HTML application to access the directory information • Anonymous access allowed" (p6)
    "https://nms.company.com:8443 — Select NETWORK MANAGEMENT" (p514)
  definition: |
    8770 的 Web 管理门户（WBM 缩写书中未展开）：:8443 端口经 NETWORK MANAGEMENT 卡登录，含 Users/
    Configuration/Performance 三应用与 Manage My Phone；Performance 即实时仪表盘（g55 数据）。
  alias_or_related: Users 需 Unified Management 许可（g36）
  tags: [product, web, wbm]

- id: g42
  term: Manage My Phone / Web Directory Client
  category: product
  source_pages: p6, p33, p38
  source_quote: |
    "HTML interface for end-users to manage their phone set — Activate your forward, reset your
    password" (p38)
    "Access the company directory through an Internet browser ... Click to Call > Automatic dialing
    from the directory client (for OXE users)" (p33)
  definition: |
    两个终端用户侧 Web 应用：Manage My Phone=话机自助（呼转/改密/可编程键，邮箱+口令登录）；Web
    Directory Client=目录查询/点击外呼（OXE 用户，SIP 话机除外）/个人通讯录。
  alias_or_related: Click to Call 限制见 n03
  tags: [product, end-user]

- id: g43
  term: OmniPCX Enterprise（OXE，csa/csm/GD）
  category: product
  source_pages: p5, p9, p47, p71
  source_quote: |
    "Host name: csa ... Main name: csm ... Check that the GD is on service: ­ GD IP address:
    192.168.1.12" (p71)
    "OXE Purple R101.0 (N3), R101.1 (N4) & R101.2 (N5)  X" (p9)
  definition: |
    ALE 企业级 PBX（本书计费数据源）：CPU 双地址 csa（物理）/csm（主），GD 为话务台类网关设备（缩写
    未展开，实验 192.168.1.12）；实验机版本 R101.1-n4。计费/流量分析/审计仅对 OXE 全量支持。
  alias_or_related: 版本兼容矩阵见 principle p02
  tags: [product, pbx, core]

- id: g44
  term: OXO Connect / OCE（OXO Connect Evolution）
  category: product
  source_pages: p5, p9, p19-20
  source_quote: |
    "OXO Connect supervision • Configuration via OMC application (on-line/off-line) ... Real-time
    alarms ... VoIP reports (via Reports application)" (p19)
  definition: |
    ALE SMB PBX 系（8770 的纳管对象之二）：经 OMC 做配置与监督（OMC 须装在 8770 服务器与每个客户端），
    支持计费/VoIP 报告/实时告警/数据备份与软件升级；兼容矩阵覆盖 OXO/OCE R4.0-R6.2。
  alias_or_related: OXE 为对照系；无流量分析与审计（n01）
  tags: [product, pbx, smb]

- id: g45
  term: OpenTouch（OT BE / MS / MC）
  category: product
  source_pages: p9, p79
  source_quote: |
    "OpenTouch BE / MS / MC — OT R2.4 to R2.6.1" (p9)
    "Global: the selected OXE and associated OpenTouch are synchronized." (p79)
  definition: |
    ALE 协作通信平台族（本书仅作同步对象与兼容矩阵行出现）：8770 同步 OXE 时可级联其关联 OpenTouch
    （Global 同步）。
  alias_or_related: WBM 不能 SSH/Telnet 直连 OT（n02）
  tags: [product, platform]

- id: g46
  term: OMC
  category: product
  source_pages: p7, p20
  source_quote: |
    "OMC (FTP , HTTPS)" (p7)
    "OMC application must be installed on the 8770 server and on each 8770 client — IP connectivity
    only" (p20)
  definition: |
    OXO Connect 的管理软件（书中未展开全称）：OXO 经 8770 监督/配置的伴生组件，须同时装在 8770 服务器
    与每个 8770 客户端上，仅 IP 连通。
  alias_or_related: 与 RAINXTE001 教材中的 OMC 同物
  tags: [product, management, oxo]

- id: g47
  term: PCS（Passive Communications Server）
  category: product
  source_pages: p104-106
  source_quote: |
    "PCS integration into OmniVista 8770 Server • PCS discovery done transparently through
    synchronization of a Call Server" (p104)
  definition: |
    被动通信服务器：不主动上联、经呼叫服务器同步被透明发现的计费数据源；其文件带 PCS ID（IP 的十六
    进制）后缀；同步开关在 NmcArchive>Accounting>Specific。
  alias_or_related: PCS ID 换算见 principle p14
  tags: [product, accounting]

- id: g48
  term: NMC Loader / Service Manager
  category: product
  source_pages: p142-143
  source_quote: |
    "Browse Start > All Programs > OmniVista 8770 > Tools > Service Manager — Select NMC Loader
    service" (p142)
  definition: |
    8770 的加载服务（NMC Loader）与其管理器（Service Manager）：停/启 Loader 即触发 loader 目录内文件
    的入库处理（手工灌测试票的标准手法）；服务需 Write and Execute 权限才能停。
  alias_or_related: NMC 缩写书中未展开
  tags: [product, loader, service]

- id: g49
  term: RLAB / POD
  category: product
  source_pages: p41-47
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a
    data center. ... Pods are independent of each other • Pods have the same configuration" (p43)
  definition: |
    ALE 培训远程实验室：按 POD 划分的同构实验单元（实验网段 192.168.1.x），每 POD 含 OXE/OMS/FlexLM/
    Client PC/OV8770 服务器等实例；公共 Pod 提供 NAS、SIP 模拟器与邮件服务器；访问分 Console mode 与
    RDP（Guacamole，实验必用以共享音频）。
  alias_or_related: 实例表与口令见 framework f02（实验口径）
  tags: [product, lab, training]

- id: g50
  term: ITSP1（SIP Carrier Simulator）
  category: product
  source_pages: p53-58, p84
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... SIP simulator is hosted in the RLAB
    common area" (p54)
    "Refer to the document SIP Carrier Simulator to know how to use the SIP simulator." (p84)
  definition: |
    培训专用 SIP 运营商模拟器（公网网关 public.itsp1.com + SIP 网关 gateway1.itsp1.com，SIP 域
    sip.itsp1.fr）：PBX 注册账号 pbxP/alcatel，模拟公网/移动/国际/紧急号码（号码含两位 POD 号 PN）；
    ITSP2 仅在拓扑图出现。配套同名使用文档。
  alias_or_related: 号码规则见 framework f03（实验口径）
  tags: [product, lab, sip]

- id: g51
  term: FlexLM Server
  category: product
  source_pages: p45, p47
  source_quote: |
    "FLEXLM SERVER 8770_FLEXLM flex 192.168.1.80 ... root letacla1" (p47)
  definition: |
    实验环境许可服务器（FlexLM 缩写未展开）：为 OXE 等提供许可，POD 内 192.168.1.80（实验口径）。
  alias_or_related: 纯实验基础设施
  tags: [product, lab, license]

- id: g52
  term: OMS
  category: product
  source_pages: p45, p47, p74
  source_quote: |
    "OMS 8770_OMS oms 192.168.1.13 ... admin root Superuser2580*" (p47)
  definition: |
    实验 POD 中的管理服务器实例（OMS 缩写未展开，192.168.1.13）：列入 OXE 信任主机表，角色与 8770
    纳管相关（书中未展开其功能细节）。
  alias_or_related: 信任主机表见 p74
  tags: [product, lab]

- id: g53
  term: IPDSP / MicroSIP
  category: product
  source_pages: p47-48
  source_quote: |
    "1 IPDSP softphone • 31000 • 2 MicroSIP softphones for OXE extension users • 31001, 31002 • 1
    MicroSIP softphone for external call tests • MicroSIP – Public" (p48)
  definition: |
    实验软话机：IPDSP=ALE IP 桌面软话机（占分机 31000）；MicroSIP=第三方 SIP 软话机（31001/31002 内线
    +1 个模拟公网）。位于 Client PC（192.168.1.10，实验口径）。另有 TrapReceiver 应用做 SNMP trap 接收。
  alias_or_related: 同机互打取不到 VoIP 报告（n32）
  tags: [product, lab, softphone]

- id: g54
  term: MariaDB（SQL）/ LDAP directory
  category: product
  source_pages: p7, p32, p460
  source_quote: |
    "MariaDB (SQL) — LDAP" (p7)
    "Cumulative counters on MariaDB tables" (p460)
  definition: |
    8770 内部数据库与目录服务：计费/话务票据、累计计数器（Tracking 数据底座）存 MariaDB；目录服务
    LDAP v3（可 LDIF 导入导出、AD 同步、双机复制——均为附加选项）。
  alias_or_related: DB 运维在书外（n45）
  tags: [product, database]

- id: g55
  term: Web Performance dashboard（widget / node dashboard / detailed dashboard）
  category: product
  source_pages: p494-497
  source_quote: |
    "NODE DASHBOARD ▪ Exposes data of the previous 24 hours ▪ Fixed widgets configuration ▪ 1 widget
    for each of the 5 covered topics ... DETAILED DASHBOARD ▪ Past time performance (last day till
    last year)" (p495-497)
  definition: |
    WBM 的 Performance 应用界面：节点仪表盘（过去 24 小时、固定 5 widget）与详细仪表盘（一天到一年、
    可增删 widget、原始数据、阈值线）；五大主题=IP domains/OXE health/VoIP quality/Trunk groups/
    Devices；另有 Threshold detections widget 与 XY 散点图等技巧。
  alias_or_related: 数据源见 framework f25；边界见 n36/n37
  tags: [product, dashboard, wbm]

# ── 五、协议/技术 (protocol) ──

- id: g56
  term: SNMP v3（A4400-RTM-MIB / UC-DAVIS MIB / OID）
  category: protocol
  source_pages: p7, p492, p510-512
  source_quote: |
    "A4400-RTM-MIB proprietary OXE MIB (trunk supervision, compressor availability, CAC, registered
    SIP devices,…) • UC-DAVIS standard MIB related to the platform health (CPU load, disk usage,…)" (p492)
    ".1.3.6.1.4.1.637.64.4400.1.7.0 gives the number of sets in service in the system (here: '5')" (p512)
  definition: |
    Web Performance 的网管协议腿：SNMPv3（authPriv，SHA 认证+AES 加密）轮询 OXE 两棵 MIB——专有
    A4400-RTM-MIB（中继监督/压缩器/CAC/SIP 注册）+ 标准 UC-DAVIS（CPU/磁盘健康）；OID 含义须查技术
    文档。告警亦可外发 SNMP Hypervisor（SNMPv3）。
  alias_or_related: 实验参数见 principle p45；不一致即停用监控（n38）
  tags: [protocol, snmp, monitoring]

- id: g57
  term: CDR / RTCP-XR（格式）
  category: protocol
  source_pages: p492
  source_quote: |
    "Proprietary format for IP devices, IPMG, 4645 and IP-xBS… RTCP-XR format for SIP devices" (p492)
  definition: |
    VoIP 话单的两种承载格式：IP 设备（IPMG/4645/IP-xBS）用 ALE 专有格式，SIP 设备用 RTCP-XR（缩写未
    展开）；经同步与小时轮询取回，可按类型/时间/IP 过滤。
  alias_or_related: CDR 全称见 g28
  tags: [protocol, format, voip]

- id: g58
  term: LDAP / LDAP(S) / LDIF / Radius / MSAD
  category: protocol
  source_pages: p7, p13-14, p32, p39
  source_quote: |
    "HTTPS, LDAP(S) | IPSec, Corba, TDS, LDAP(S)" (p7)
    "Directory data import/export in LDIF • LDIF mapping tools for mass provisioning • Synchronization
    with Active Directory" (p32)
    "Microsoft Active Directory (MSAD) synchronization: The communication servers and MSAD are
    automatically synchronized." (p39)
  definition: |
    目录与认证协议族：8770 内部 LDAP v3 目录（WBM/客户端走 HTTPS+LDAP(S)）；LDIF 导入导出与映射工具
    （批量开通）；MSAD（Microsoft Active Directory）同步；外部认证可经 Radius Server（附加选项）。
    Corba/TDS 为服务器内部协议（书中未展开）。
  alias_or_related: MSAD 全称书中展开（p39）；Security 应用另有 External authentication via Radius（p14）
  tags: [protocol, directory, auth]

- id: g59
  term: CMISE / (S)FTP / Telnet-SSH / SMTP / HTTPS
  category: protocol
  source_pages: p7, p374
  source_quote: |
    "CMISE, (S)FTP , Telnet/SSH, LDAP — OXO Connect ... SMTP ... HTTPS" (p7)
  definition: |
    8770 架构协议矩阵（图中标注）：对 OXE 走 CMISE+FTP/SFTP+Telnet/SSH+LDAP（数据取回/配置/同步）；
    对 OXO 经 OMC 走 FTP/HTTPS；邮件通知走 SMTP；Web 面走 HTTPS。计费/话务文件回收即 FTP（见 f09）。
  alias_or_related: CMISE/TDS/Corba 书中未展开全称
  tags: [protocol, architecture]

- id: g60
  term: ISDN T0/T1/T2 / NDDI / ABC-F / DDI / DID
  category: protocol
  source_pages: p84, p493
  source_quote: |
    "Translator > 1 > External Numbering Plan > 1 > Default DID num. translator ... First external
    number 33210N41000" (p84)
    "Only ISDN (T0,T1, T2), SIP , NDDI and ABC-F" (p493)
  definition: |
    中继与号码术语：T0/T1/T2=ISDN 基群/一次群接口速率档（书中未逐个展开）；NDDI、ABC-F 为 supported
    中继/编号形态（未展开）；DDI/DID=外线直拨号翻译（DID translator 把外线号段映射内线，如
    33210N41000→31000 起 500 号）。
  alias_or_related: SIP 中继见 g50/f03
  tags: [protocol, trunk, numbering]

- id: g61
  term: PWT/DECT（RBS / IBS）
  category: protocol
  source_pages: p432, p444
  source_quote: |
    "Select the type of radio base: Select PWT/DECT System > 1 — Radio base type: Select RBS or IBS
    or Mixed ... Base station busy trigger — 8 by default (RBS) / 4 by default (IBS)" (p444)
  definition: |
    无线话务观察对象：PWT/DECT 无线系统（缩写未展开）分 RBS/IBS 两类基站（未展开，Mixed 两可配），
    忙触发值默认 8/4；是流量分析六类观察对象之一。
  alias_or_related: PtpType ALL 才加载其计数器（n34）
  tags: [protocol, wireless, traffic]

- id: g62
  term: AOC / PIN / SVA（AVS）/ ARCEP
  category: protocol
  source_pages: p137, p161, p88
  source_quote: |
    "Tax included in AOC. Advice Of Charge: uses the cost given by the PCX" (p161)
    "SVA tariffs provided by the ARCEP organism (French Telecom regulator) ... Based on Added Value
    Services for French market" (p137)
    "PIN (Personal Ident. No.)" (p88)
  definition: |
    计费字段与监管缩写：AOC=Advice Of Charge（书中展开，PCX 给定成本模式相关开关）；PIN=Personal
    Identification Number（书中展开）；SVA/AVS=增值业务（法国监管口径，通信费 C+服务费 S 模型）；
    ARCEP=法国电信监管机构（书中注释）。
  alias_or_related: 服务费模型见 framework f14
  tags: [protocol, billing, france]

- id: g63
  term: MACD
  category: concept
  source_pages: p39
  source_quote: |
    "Light web client for unified user management: Manage frequent users Move/Add/Change/Deletion
    (MACD)" (p39)
  definition: |
    用户管理的四类操作缩写（书中展开：Move/Add/Change/Deletion）：WBM Users 的定位卖点之一。仅结论
    页提及。
  alias_or_related: 全书唯一出现处 p39
  tags: [concept, user-management]

# ── 六、资源/位置 (resource) ──

- id: g64
  term: /usr4/account 与 /usr4/pmm
  category: resource
  source_pages: p65, p94, p433
  source_quote: |
    "(101)xa001001> cd /usr4/account ... more ACCOUNT.LIS" (p65)
    "Files are stored in the folder /usr4/pmm" (p433)
  definition: |
    OXE 侧两个数据目录：/usr4/account 存计费与 VoIP 票据文件（TAX/IP/SIP*.DAT 与对应 .LIS）；
    /usr4/pmm 存流量分析半小时计数器文件（C*.pmm/.inf 与 pmm.lis）。排障第一站（cd+more/ll）。
  alias_or_related: 命令集见 principle p06
  tags: [resource, oxe, directories]

- id: g65
  term: C:\8770\data\loader 与 C:\8770\data\collector
  category: resource
  source_pages: p98, p103, p109, p112
  source_quote: |
    "C:\8770\data\loader folder" (p98)
    "Accounting file retrieved by the tickets collector are stored in the folder c:\8770\data\collector
    by default." (p109)
  definition: |
    8770 侧两个落地目录：loader=计费应用回收目录（子目录按 networknumber=N\subnetworknodenumber=NNN
    组织，含 ACCOUNT.LIS；手工灌票也放这里）；collector=票据收集器目录（供外部计费应用）。同步前后
    对比两目录是回收验证的标准动作。
  alias_or_related: NMC Loader 停启触发入库（g48）
  tags: [resource, directories, loader]

- id: g66
  term: C:\8770_ARC\Accounting\tickets
  category: resource
  source_pages: p529-531
  source_quote: |
    "Path — Path to the default archive folder (C:\8770_ARC\Accounting\tickets)." (p529)
  definition: |
    计费归档默认目录（可改）：archZ 文件按"天+节点"存放；恢复对话框默认也从这里取。
  alias_or_related: 生命周期参数见 principle p46
  tags: [resource, archiving]

- id: g67
  term: C:\8770\log（NMCSyncLdapPbx_1.log / NMCLD_1.log / NMCLD_CostCalculation_1.log /
    NMCCostRecalculation_*.log / NMC_RealtimePerformance.log）
  category: resource
  source_pages: p80, p114, p179-180, p517
  source_quote: |
    "Log file C:\8770\log\ NMCSyncLdapPbx_1.log" (p80)
    "NMCLD_CostCalculation_1.log This file gives cost calculation errors during records loading into
    database." (p179)
  definition: |
    8770 日志目录五件套：NMCSyncLdapPbx_1（同步）、NMCLD_1（票据加载：TicketsRead/BadLines/速度/被过滤
    数）、NMCLD_CostCalculation_1（加载期成本错误）、NMCCostRecalculation_CostCalculation_1（重算期
    错误）、NMC_RealtimePerformance（Web Performance 数据库加载）。
  alias_or_related: 错误样例见 counter-example n13
  tags: [resource, logs, troubleshooting]

- id: g68
  term: 8770_NAS / SHARING
  category: resource
  source_pages: p49-50, p142, p245
  source_quote: |
    "Network drive connected to 8770_NAS • Installation files, patches, licenses files • Tools for
    training" (p49)
    "Shared folder called SHARING, created on 8770_MAIL_SERVER" (p50)
  definition: |
    实验公共资源：8770_NAS 网络盘（安装包/补丁/许可/训练工具，含 ACCOUNTING_2025.txt 与 Telecom2_7x
    code book）与邮件服务器上的 SHARING 共享夹（文件交换）。**Code Book 修改必须在 Documents 副本上
    做**（p246 Warning）。
  alias_or_related: 纯实验基础设施（实验口径）
  tags: [resource, lab, nas]

- id: g69
  term: ALE Knowledge Hub（enterprise-education.csod.com）
  category: resource
  source_pages: p646-648
  source_quote: |
    "Connect to ALE Knowledge Hub (https://enterprise-education.csod.com ) with your usual credentials" (p646)
  definition: |
    ALE 培训与评估门户：完成在线培训评估后才能下载出席证书；My Training 按讲师给的课程参考号检索。
  alias_or_related: 反馈地址 training-services@al-enterprise.com（p650，Brest）
  tags: [resource, training, portal]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 术语表逐条核对

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| Accounting record / ticket | 有明确定义（p61-62/p66） | g01 |
| ACCOUNT.LIS | 有明确定义（p62） | g02 |
| Detailed accounting | 有明确定义（p99） | g03 |
| Carrier | 有明确定义（p117/p152） | g13 |
| Calling/Called region | 有明确定义（p118） | g14 |
| Direction | 有明确定义（p118） | g15 |
| Tariff | 有明确定义（p127-135） | g16 |
| Cost center | 有明确定义（p89/p256） | g04 |
| Organization tree | 有明确定义（p253） | g06 |
| Mask profile | 有明确定义（p298-302） | g09 |
| Accounting domain | 有明确定义（p343-346） | g10 |
| Cost profile | 有明确定义（p323-325） | g11 |
| Code book | 有明确定义（p228-233） | g19 |
| Report definition / Generated report | 有明确定义（p361） | g20 |
| Tracking profile | 有明确定义（p457） | g23 |
| IP ticket / VoIP KPI | 有明确定义（p408/p414） | g26/g27 |
| pmm 文件 | 有明确定义（p433） | g64（含于 /usr4/pmm）+g26 相邻 |
| archZ | 有明确定义（p521） | g29 |

结论：18 行全部落位，无"仅 passing 提及需排除"的主干术语。

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：tax.tmp（g02）、计费方法族（g03）、默认成本中心（g05）、灰条目（g07）、三种组织更新语义（g08）、订阅票（g12）、被叫/主叫区域外延（g14）、Period/Calendar（g18）、报表三节点（g20）、Detailed/Grouped/Hit-list（g21）、Mask data access（g24）、变化率（g25）、CDR（g28）、Record origin（g30）、MACD（g63）
- 角色：AdminNmc（g31）、adfexc（g32）、mtcl（g33）、cn=directory manager（g34）、MCS（g35）
- 许可：Unified Management（g36）、Company Directory（g37）、Accounting/Ticket collector（g38）
- 产品：OV8770（g39）、thick client（g40）、WBM（g41）、Manage My Phone/Web Directory Client（g42）、OXE+csa/csm/GD（g43）、OXO/OCE（g44）、OpenTouch（g45）、OMC（g46）、PCS（g47）、NMC Loader/Service Manager（g48）、RLAB/POD（g49）、ITSP1（g50）、FlexLM（g51）、OMS（g52）、IPDSP/MicroSIP（g53）、MariaDB（g54）、Web Performance 仪表盘（g55）
- 协议：SNMPv3+MIB（g56）、CDR/RTCP-XR 格式（g57）、LDAP 族/Radius/MSAD（g58）、CMISE/FTP/SSH/SMTP/HTTPS（g59）、ISDN/NDDI/ABC-F/DDI/DID（g60）、PWT/DECT（g61）、AOC/PIN/SVA/ARCEP（g62）
- 资源：/usr4 两目录（g64）、loader/collector（g65）、归档目录（g66）、日志五件套（g67）、NAS/SHARING（g68）、Knowledge Hub（g69）

### 3. 仅 passing 提及、未单列条目的词（备查）

ITSP2（p54 拓扑图，无细节，附 g50）、TrapReceiver（p48，实验 SNMP 工具，附 g53）、Guacamole（p51，RDP 底座，附 g49）、Thunderbird/Wireshark/PuTTY/Notepad++（p374/p517/p71/p243，通用第三方工具，实验用）、MindTerm（p78，SSH 公钥生成组件）、SLA（p407 "KPI/SLA Overflow"，未展开）、OOS（p494，未展开）、INTIP/IPMG/4645/IP-xBS（p409/p492 设备类型名，附 g26/g57）、CAC（p492/p494，未展开）、NOE（p494 "NOE devices"，未展开）、Compact Template/Template（p385，报表模板，附 g20）、Bank holidays in France（p153，实验日历名）、ACCOUNTING_2025.txt（p142，实验数据文件，附 g68）、SIP Carrier Simulator（文档，p84，附 g50）。

### 4. 提取口径说明

- 所有定义只采信本书正文；WBM、NMC、OMC、MOS、RTCP-XR、NDDI、ABC-F、PWT、DECT、RBS、IBS、CAC、GD、GA、PTP、OOS、NOE、INTIP、IPDSP、OMS、FlexLM 等缩写书中未给全称，full_name 一律省略，不做外部补全。
- 书中已展开的缩写按原文收录：MCS（p13）、MACD（p39）、MSAD（p39）、CDR（p492）、BFI（p422）、KPI（p407）、PIN（p298/p88）、AOC（p161）、AVS/SVA（p137）、ARCEP（p137 注）、RLAB（p43 Remote Lab）、NUC 不属本书。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准；实验值（IP/口令/号码）标注"实验口径"。
