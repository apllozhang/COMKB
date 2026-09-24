# 案例/实验/操作序列候选 — OmniVista 8770 R5.2 计费与性能管理 (8770XTE201EN Ed45)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号、教学税率）标注"实验口径"。
> 条目说明: 全书 How-To 实验章 → 23 条（c01-c23，按原书页序）：计费链 4 条、运营商 5 条（Telecom 1 拆"创建+演进"）、Code Book 1 条、组织与安全 4 条、报表 7 条（界面巡检 + 练习题面 + 五个实现）、无独立条目的 5 个配置型实验（VoIP 性能/流量分析/Tracking/Web Performance/归档）说明见文末自检。

```yaml
- id: c01
  title: OXE 节点注册（信息核查、SSH/信任主机、网络/子网/OXE 声明、同步验证）
  type: lab
  source_pages: p70-80
  source_chapter: OXE node registration — "Declare an OmniPCX Enterprise"
  source_quote: |
    "Use the siteid command to display network and node number. ... Node number : 1 ; Network number : 1" (p71)；
    "Subnetwork – Node number: Enter a numeric value equal to the OmniPCX Enterprise network*100 +
    OmniPCX Enterprise node number. ... you must enter 101" (p77)；
    "At the end of the complete / partial synchronization process, a successful message should be
    displayed. ... C:\8770\log\ NMCSyncLdapPbx_1.log" (p80)
  steps: |
    1. 准备核查（OXE 侧约定值，实验口径）：主机名 csa、网络号 1、节点号 1、物理 IP 192.168.1.1/掩码
       255.255.255.0/网关 192.168.1.254、主名 csm 主 IP 192.168.1.3、节点名 oxe；GD 在服（192.168.1.12）。
    2. PuTTY SSH 连 csm 主 IP（192.168.1.3），执行 siteid 核对节点号/网络号。
    3. su - 切 root（实验口径密码 Superuser2580*），netadmin -m：选项 5 Role addressing > 1 View
       确认主地址（local main / Ethernet / csm / 192.168.1.3；空间冗余需记两个主 IP）。
    4. netadmin -m 选项 2 Show current configuration：确认 "Security with SSH: yes"；辅以
       netstat -an | grep :22（LISTEN 即开）/ grep :23（空即 telnet 关）。
    5. netadmin -m 选项 11 Security > 1 Firewall (iptables) > 3 Restricted Access Configuration >
       1 View trusted hosts：核对 8770（omnivista 192.168.1.70）、OMS（192.168.1.12）、PC
       （192.168.1.10）、网关均在表——所有涉及 Call Server 的主机必须声明。
    6. 8770 Configuration 应用：右键 nmc > Create > Network，Name=ale、Network number=1。
    7. 右键网络 ale > Create > Subnetwork，Name=abc1、Subnetwork number=1（必须=OXE 网络号）。
    8. 右键子网 abc1 > Create > OmniPCX 4400 / Enterprise：Name=oxe；Subnetwork-Node number=101
       （网络号×100+节点号）；Network/Subnetwork 自动继承不填；IP address=192.168.1.3（空间冗余右键
       Add a Value 加第二个）；FTP Username=adfexc、FTP Password=Superuser2580*（实验口径，OXE 数据
       取回凭证）；勾 Process configuration；Alarm reception mode=Permanent IP connectivity；勾
       Directory Process（加载话机簿）。
    9. Software download 页签：Username maintenance=mtcl、Password maintenance=Superuser2580*（实验口径）。
    10. Connectivity 页签：勾 SSH connection；Host name 填唯一 ID（仅字母数字与 .,-_、字母开头；
        MindTerm 据此在 8770 服务器生成 SSH 公钥）。
    11. 右键 OXE > Synchronization > Complete > Separate：向导选 "of the task" > Status 页签 >
        Apply 启动（点 OK 则后台执行）> Refresh 刷新日志；等成功提示。
    12. 验证：Configuration 树下 OXE 出现分支；选中 OXE 的 Data Collection 页签看 "Date of last
        modification"；日志 NMCSyncLdapPbx_1.log。
  verification: |
    同步成功消息显示；OXE 分支（用户/目录等）在 Configuration 树生成；Data Collection 页签显示最近
    同步时间（p80）。
  conditions: OXE 与 8770 IP 连通；OXE 侧 SSH/信任主机已核（步骤 3-5）；8770 登录 AdminNmc/Superuser01*（实验口径）。
  tags: [lab, node-registration, ssh, synchronization]

- id: c02
  title: OXE 对接公共 SIP 运营商模拟器（注册参数、DID 翻译、外呼验证）
  type: lab
  source_pages: p81-84
  source_chapter: OXE configuration to use the public SIP carrier simulator
  source_quote: |
    "The Public SIP trunk group is already configured in the OXE database, but you must specify your
    own 'POD' parameters into the external SIP gateway" (p83)；
    "First external number 33210N41000 (where N is your POD Number) ... First internal number 31000
    ... Range Size 500" (p84)
  steps: |
    1. 前提：环境中软话机与 OXE-模拟器 SIP 中继组已预配，只需按 POD 号激活外部 SIP 网关。
    2. OXE 配置界面菜单 SIP > SIP Ext Gateway，选中外部网关 ITSP1_GW1。
    3. Registration ID=pbxN、Outgoing username=pbxN（N=POD 号；如 POD 4 填 pbx4）（实验口径）。
    4. 菜单 Translator > 1 > External Numbering Plan > 1 > Default DID num. translator，右键 Create。
    5. First external number=33210N41000（N=POD 号，POD 4 即 33210441000）；First internal number=
       31000；Range Size=500。
    6. 打若干出局呼叫验证公网 SIP 运营商通路（用法参照 SIP Carrier Simulator 文档）。
  verification: |
    出局呼叫经 SIP 模拟器接通（书中以"make sure that access to public SIP carrier is working"为验收，
    p84）。
  conditions: 实验口径：模拟器为 RLAB 公共资源（gateway1.itsp1.com，账号 pbxP/alcatel）。
  tags: [lab, sip, did-translation, oxe-config]

- id: c03
  title: OXE 外部计费配置（出票类型、成本中心、用户分配、记账开关）
  type: lab
  source_pages: p85-92
  source_chapter: External accounting — "Configure external accounting on the OmniPCX Enterprise"
  source_quote: |
    "Files for External Accounting — Yes ... Don't forget to select the Public Outgoing 0 Units
    calls." (p86)；
    "Cost center number / Cost center name — 1 MKT — 2 Training — 3 TSS" (p89)；
    "Charging COS — Justified (default value) ... Not ticketed: directory number, name and first name
    are masked in the accounting record." (p91)
  steps: |
    1. 目标出票类型：Public Outgoing PCX Calls、Public Incoming PCX Calls、PCX PCX Calls、Public
       outgoing 0 units calls；被叫号不遮（8770 侧负责）。
    2. Configuration 应用 > 选中 OXE 右键 Configure > Applications > 1 > Accounting > 1。
    3. All 页签：Internal Accounting=Yes、Files for External Accounting=Yes —— 必须先 Apply 再进
       后续页签。
    4. Files for External Accounting 页签：Max No. Days of Storage 保持默认 31（=31×24=744 个压缩
       文件）；Hotel CDR (Tickets) 过滤器勾选各呼叫类型（公共/专线、出/入、本地/网络），**必选 Public
       Outgoing 0 Units calls**。
    5. 加过滤项：在过滤条目滚动条上右键 > Add After > 选 PCX PCX Calls（本地呼叫也出票）。
    6. Financial Report 页签：PIN (Personal Ident. No.)=Not masked、No of Last Masked Called
       Digits=0（遮蔽由 8770 做）。
    7. 成本中心命名：OXE 配置 > Specific Telephone Services > Cost Center：1=MKT、2=Training、3=TSS
       （成本中心默认已存在，只配名字）。
    8. 建两个模拟用户：Users 菜单右键 Create —— Ava Adore（31010，ANALOG）、Alice Adams（31011，
       ANALOG）。
    9. 分配成本中心：Users > 选 31000 > Rights 页签 > Cost Center ID=1（MKT，名字自动带出）；同法：
       31001→MKT、31002→Training、31010→Training、31011→TSS。
    10. 记账开关（Rights 页签）：Charging COS=Justified（默认，全信息出票）；Miscellaneous 页签：
        Dialed number masked=No（默认）。
    11. 对 31001/31002/31010/31011 重复步骤 9-10。
  verification: |
    书中隐含验收：配置完成后做呼叫，OXE 开始按所选类型出票（后续 c04 用 accview 与 8770 回收验证）。
  conditions: c01 完成（OXE 可配置）；PIN/遮蔽参数依赖 8770 侧约定。
  tags: [lab, accounting, cost-center, oxe-config]

- id: c04
  title: 计费票据维护命令与 8770 票据回收（方法/凭证/加载过滤/验证）
  type: lab
  source_pages: p93-95, p108-114
  source_chapter: External accounting / Using maintenance commands & Accounting records retrieval
  source_quote: |
    "(101)csa> account compress ... Note: A synchronization of the node saves the buffer into an
    accounting file." (p93)；
    "Record/ticket collection — Select an accounting ticket collection process ... Accounting: to
    enable record collection ... stored in the folder c:\8770\data\collector by default" (p109)；
    "Browse C:\ 8770 \ data \ loader \ network number=1 \ subnetworknodenumber=101 — Open the
    ACCOUNT.LIS file" (p112)
  steps: |
    1. OXE 侧生成票据：打若干出局/入局/本地呼叫。
    2. Configuration 应用 > OXE 右键 Connect，SSH 登录 mtcl/Superuser2580*（实验口径）。
    3. account compress 强制把缓冲落为新 .DAT（节点同步亦可触发）。
    4. cd /usr4/account → more ACCOUNT.LIS 看清单、ll *.DAT 列文件。
    5. accview -mtf <文件名> 查票据字段（-b 10 / -e 10 看头/尾 10 条）。
    6. 8770 侧配方法：Configuration > 选 OXE > PCX 页签：FTP user=adfexc、FTP password 与 OXE 一致
       （**用户名禁改**，许可校验）；Accounting Process=Detailed accounting。
    7. 同节点 Data Collection 页签：Record/ticket collection=Accounting（默认 None）；收集器文件落
       c:\8770\data\collector；"Last accounting file polled" 由服务器自动更新。
    8. PCS 同步开关：Administration > nmc > OmniVista 8770 > 服务器名 (nms) > NmcArchive > Accounting
       > Specific 页签：PCS Ticket Collection=Yes（默认，随日同步）。
    9. 加载过滤：Account./traf./VoIP > Parameters > Loading > Accounting：设 Duration 阈值（如 >0）、
       Cost 阈值、勾 Communication Type（Unspecified/Voice/Data）与 Call type（Incoming/Outgoing/
       Network）；第二部分 Charged party node 按需取消 Undeclared。
    10. 验证回收：确认 C:\8770\data\loader 与 C:\8770\data\collector 为空 → 执行 OXE 同步 → 复查两
        目录出现文件；打开 loader\networknumber=1\subnetworknodenumber=101\ACCOUNT.LIS。
    11. 验证入库：Parameters > Accounting Organization > Tree 看记录数与首末日期；Organization 页签
        展开树选用户看记录；日志 NMCLD_1.log 看 TicketsRead/BadLines/被过滤数。
  verification: |
    loader 目录出现从节点取回的 DAT 与 ACCOUNT.LIS（p112）；计费组织树显示记录数（p113）；NMCLD_1.log
    显示 "Nb of tickets read = 9 ==> Processing speed = 52 tic/sec"（p114，实验口径）。
  conditions: c03 完成；FTP 凭证必须与 OXE 一致；TicketsRead 实验口径。
  tags: [lab, retrieval, loading-filter, accview]

- id: c05
  title: 运营商基础参数与测试票据灌库（币种/税/国家、NMC Loader 手工加载）
  type: lab
  source_pages: p141-148
  source_chapter: Direct carrier settings
  source_quote: |
    "Search for the file ACCOUNTING_2025.txt ... Paste the selected file on the following path:
    C:\8770 \data \loader \networknumber=1" (p142)；
    "If the reference currency is Dollar, create an additional currency named Euro with the following
    conversion rate: 1 euro=1,21 dollars." (p145)；
    "A minimum of 168 accounting tickets should be available." (p144)
  steps: |
    1. 灌测试票：从 8770_NAS\Tools For Training\Accounting records 复制 ACCOUNTING_2025.txt 到
       C:\8770\data\loader\networknumber=1（实验口径）。
    2. Start > All Programs > OmniVista 8770 > Tools > Service Manager > 选 NMC Loader 服务 > 启用
       Write and Execute 权限 > Stop > Refresh——服务重启后 txt 消失、记录入库。
    3. 验证：Account./traf./VoIP > Organization 页签 > Records 页签显示记录；"Modify the number
       required…" 填 200（最大显示值）；至少应见 168 张票。
    4. 核对参考币种：Parameters > Currency（安装所选国家决定，唯一且不可删）。
    5. 附加币种：右键 Currency > Create（如 Euro / €，Reference=No）> 选中 > Conversion rate 页签 >
       Create：起止日期（无结束日=永久）+ 汇率（1€=1.21$，或反向 1$=0.82€）（实验口径）。
    6. 税：Parameters > Tax > Create：US 建 VAT 10%、欧洲建 TVA 20%（Tax Rate 页签带有效期）（实验
       口径）。
    7. 国家：Parameters > Country > 右键 Create：France/Fr（仅供信息）。
  verification: |
    Records 页签能看到 ≥168 张测试票（p144）；币种/税/国家列表建成后供运营商资费引用（p147 Notes）。
  conditions: 实验口径：教学税率/汇率；NMC Loader 停启即触发加载。
  tags: [lab, currency, tax, loader]

- id: c06
  title: 直连运营商 Telecom 1 全流程建模（周期/日历/区域/资费/方向 + 成本计算）
  type: lab
  source_pages: p149-180
  source_chapter: Direct carrier configuration - Telecom 1
  source_quote: |
    "The start date is: 01/01/2020 ­ Specific dates are January the 1st and May the 1st" (p151)；
    "Configure the direct carrier Telecom 1 with the following settings ..." (p151)；
    "the field Direct Carrier should display the direct carrier previously configured Telecom 1." (p179-180)
  steps: |
    1. 建运营商：Account./traf./VoIP > Carriers 页签 > 右键 Carrier > Create：Name=Telecom 1、
       Symbol=T1（≤5 字母唯一）、Type=Outgoing、State=Active、Carrier prefix 空、Country=France、
       Inherit tracking 关闭。
    2. 建周期：选 Telecom 1 > Period > Create：Start date=1/1/2020（结束日期建下一周期时自动回填）。
    3. 建日历：Calendar > 右键 Create：Specific Day Type Name="Bank holidays in France"；再 Specific
       Date 建两条：1/1/2020、5/1/2020，均勾 Valid each year。
    4. 建主叫区：Period > Region > Create：Name=Brest；其下 PCX > Create：Network.SubNetwork.PCX=
       Ale.Abc1.oxe、Access phone number=0298112233（必填，仅信息）。
    5. 建被叫区与前缀：Local region（02）；National region（01、03、04、05 逐条建）；Mobile region
       （06）；均默认 Prefix - Carrier Dependant=enabled。
    6. Local 资费：Period > Tariff > Create：Name=Local tariff、Calculation=Duration: Exact、
       Currency/Tax 按国别选；Time Zone：Day type=Daily、Start=12:00AM、Unit Duration=60、Unit
       Cost=0.2。
    7. National 资费：同法建 National tariff（exact）；Time Zone 三段——Normal 8:00AM 起（initial
       cost 0.7 / initial duration 120 / unit 60 / cost 0.5）；Reduce 7:00PM 起（initial 0.2 / unit
       60 / cost 0.3）；Reduce 12:00AM 起（initial 0.2 / unit 60 / cost 0.3）——累计时段须铺满全天。
    8. Mobile 资费：Mobile tariff（Duration: round up）；Working day 12:00AM 起 unit 120s×2；
       Weekend（Reduce）12:00AM 起 unit 180s×2。
    9. 建方向：Period > Direction > Create 三条——Brest→Local region=Local tariff；Brest→National
       region=National tariff；Brest→Mobile region=Mobile tariff（Delay=拨完号到对端应答的平均等待
       秒数，可空）。
    10. 成本计算：菜单 Accounting/traffic > Compute cost…：From=1/1/2020（To 空）、Carrier Cost(s)+
        Force cost calculation 勾选 > Simple job > Continue > Description="Cost Calculation –
        Telecom 1" > Apply > Status 页签定期 Refresh。
    11. 验证：Organization 页签 > NMC 根 > Records 页签——Direct Carrier 列=Telecom 1，Direct Carrier
        Direction 列显示方向。
    12. 排障认知：NMCLD_CostCalculation_1.log（加载期错）与 NMCCostRecalculation_CostCalculation_1.log
        （重算期错），典型错 "No first carrier found"。
  verification: |
    Records 页签 Direct Carrier=Telecom 1 且方向正确显示（p179-180）；重算任务可在 Scheduler 复查
    （p178）。
  conditions: c04/c05 完成（有记录与币种税）；资费数值为实验口径（见 principle p23）。
  tags: [lab, carrier, tariff, direction, compute-cost]

- id: c07
  title: Telecom 1 演进：新增巴黎主叫区（前缀冲突处理、方向矩阵重建、重算）
  type: lab
  source_pages: p181-194
  source_chapter: Direct carrier configuration - Telecom 1 / Evolution
  source_quote: |
    "A hardware migration has been applied and a remote Media Gateway has been added in Paris. A
    trunk group 99 has been managed for making outgoing calls from Paris area." (p181)；
    "Paris region is a calling and a called region at the same time." (p183)；
    "Calculation cost has been applied also to some accounting records which trunk group number 99 is
    involved." (p194)
  steps: |
    1. 场景：巴黎新增远端媒体网关，出局走中继组 99；需把 01 归入巴黎主叫区。
    2. 先删前缀：Region > National region > Prefix > 选 01 > 右键 Delete（同一前缀不能跨区域，否则
       配置时报错）。
    3. 建巴黎主叫区：Region > Create：Name=Paris region；Trunk Group > Create：Trunk group=99 +
       PCX=Ale.Abc1.oxe + Access phone number=0102030405。
    4. 巴黎兼作被叫区：Paris region > Prefix > Create：Indicator prefix=01。
    5. 改 Brest 为"主/被叫双栖"：先删方向 Brest–Local region（Direction 页签）→ 删 Local region
       （Region 页签）→ 重命名 Brest 为 "Brest region" → 给 Brest region 加前缀 01。
    6. 重建 8 条方向：Brest→Brest（Local）、Brest→Paris（National）、Brest→National（National）、
       Brest→Mobile（Mobile）；Paris→Paris（Local）、Paris→Brest（National）、Paris→National
       （National）、Paris→Mobile（Mobile）。
    7. 重算：Compute cost（From=1/1/2020、Carrier Cost(s)+Force、Simple job，Description 含 "Paris
       MG included"）。
    8. 验证：Records 页签刷新后 Direct Carrier=Telecom 1，中继组 99 相关记录也带上成本与方向。
  verification: |
    中继组 99 的记录被计价（p194）；重算日志无 "No first carrier found" 新增错误。
  conditions: c06 完成；先删方向再删区域（依赖顺序）。
  tags: [lab, carrier-evolution, trunk-group, prefix-conflict]

- id: c08
  title: 第二直连运营商 Telecom 2（双运营商并存）
  type: lab
  source_pages: p195-215
  source_chapter: Direct carrier configuration - Telecom 2
  source_quote: |
    "Configure the direct carrier Telecom 2 with the following settings ­ The name of the carrier is
    Telecom 2 ­ The start date is: 01/01/2020" (p196)；
    "Indicator prefix Enter access prefixes for this region individually (i.e. 72)" (p199)
  steps: |
    1. 建运营商：Name=Telecom 2、Symbol=T2、Type=Outgoing、State=Active、Country=France。
    2. 建周期：Start date=1/1/2020。
    3. 建主/被叫双栖区 Brest：PCX=Ale.Abc1.oxe、Access phone number=7298010233；前缀 72。
    4. 建 National region：前缀 71、73、74、75、76。
    5. Local 资费：exact、Daily、unit 60×0.2。
    6. National 资费：exact、Daily：Normal 7:00AM 起 initial 0.6/120s/unit 60×0.4；Reduce 6:00PM 起
       initial 0.1/unit 60×0.3；午夜 Reduce 段 initial 0.1/unit 60×0.3。
    7. 方向两条：Brest→Brest（Local tariff）、Brest→National（National tariff）。
    8. Compute cost（From=1/1/2020、Carrier+Force、Simple job，Description="Cost Calculation –
       Telecom 2"）。
    9. 验证：Records 页签 Direct Carrier=Telecom 2 及方向显示。
  verification: |
    记录被计到 Telecom 2（p215）；与 Telecom 1 并存互不干扰。
  conditions: c06 完成；数值为实验口径（见 principle p24）。
  tags: [lab, carrier, multi-carrier]

- id: c09
  title: 脉冲型运营商 Service（特服号区域 + 唯一方向）
  type: lab
  source_pages: p216-225
  source_chapter: Pulse type carrier configuration - Service
  source_quote: |
    "Right click on Carrier and select Create a pulse type carrier ... Unit cost — Enter the value
    for the unit cost (i.e. 1,5)" (p218)；
    "Indicator prefix ... (i.e. 36) ... (i.e. 118712)" (p220)
  steps: |
    1. Carriers 页签 > 右键 Carrier > **Create a pulse type carrier**（专用入口）：Name=Service、
       Symbol=Srv、State Date=1/1/2020、Unit cost=1.5、Tax=TVA、Currency=Euro、Country=France（Tarif
       字段自动生成）。
    2. 建被叫区：Period > Region > Create：Name=Special。
    3. Special > Prefix 建两条：36、118712。
    4. 建唯一方向：Period > Direction：Called region=Special（通信资费按脉冲 Unit cost 生效）。
    5. Compute cost（From=1/1/2025、Carrier+Force、Simple job，Description="Cost Calculation –
       Service"）。
    6. 验证：Records 页签 Direct Carrier=Service、唯一方向显示。
  verification: |
    记录计到 Service 运营商（p225）；总票价=Charge units×1.5（脉冲公式，principle p19）。
  conditions: c05 完成（TVA/Euro 已建）；教学单价 1.5 为实验口径。
  tags: [lab, pulse-carrier, service-numbers]

- id: c10
  title: Code Book 导出与导入（存档迁移、EFFECT_DATE 新周期、.itl 节点修复）
  type: lab
  source_pages: p238-250
  source_chapter: Export & import a code book
  source_quote: |
    "Select Carrier > Telecom 1 > Period > [1/1/2020, … — Right click and select Export…" (p239)；
    "Modify the Telecom 1 code book ­ Update the .inf file and set the parameter 'EFFECT_DATE' to
    20220101" (p243)；
    "ALL MODIFICATIONS ON TELECOM 2 CODE BOOK FILES MUST BE APPLIED FROM THE DOCUMENTS DIRECTORY AND
    NOT FROM THE NAS DRIVE." (p246)
  steps: |
    1. 导出 Telecom 1：Carriers 页签 > Carrier > Telecom 1 > Period > [1/1/2020..] > 右键 Export… >
       选 Documents 下新建文件夹 "Telecom 1" > File Name=Telecom1.inf > 导出（列出全部关联文件）。
    2. 删除运营商 Telecom 1（右键 Delete 确认）。
    3. 重新导入：右键 Carrier > Import… > 浏览到 Telecom 1 文件夹 > 选 Telecom1.inf > 成功重建。
    4. 演进练习：Notepad++ 编辑 Telecom1.inf，把 EFFECT_DATE 改为 20220101；再次 Import——结果：
       同一运营商下新增了一个 Period（价目按周期的正规演进法）。
    5. Telecom 2 迁移练习：从 NAS（Softs > Tools For Training > Carrier codebook）复制 Telecom2_7x
       到 Documents——**修改只能改 Documents 里的副本，不能动 NAS 原件**。
    6. 直接 Import Telecom2.inf → 报错：Telecom2.itl 里的 PCX 名是 oxe9，与本机声明名 oxe 不一致
       （导入报错、方向建不出来）。
    7. Notepad++ 打开 Telecom2.itl，把 Node 名改为 oxe → 删除已导入的 Telecom 2 → 重新 Import →
       成功。
  verification: |
    Telecom 1 重建成功（p242）；改 EFFECT_DATE 后出现新周期（p244）；Telecom 2 修复 .itl 后导入成功
    （p250）。
  conditions: .itl 的 Node 必须先于导入改好（p247 Notes）；书内提问式验收（"What the error deals
  with?"）。
  tags: [lab, codebook, export-import, itl]

- id: c11
  title: 计费组织树搭建与修改（默认成本中心、层级、搬移权限实践）
  type: lab
  source_pages: p268-288
  source_chapter: Accounting organization
  source_quote: |
    "Set up the default cost center called CC_OXE ­ Execute a complete synchronization of the call
    server" (p270)；
    "The root name must be customized, and it is Alcatel ­ Two levels must be created: level Brest
    and level Colombes" (p278)；
    "The move of the trunk group from the cost center CC_OXE to cost center MKT is successful. ...
    Such move is authorized from the organization map" (p285)
  steps: |
    1. 清场：Account./traf./VoIP > Organization 页签 > 从根逐项删除全部条目并确认。
    2. 配默认成本中心：Configuration 应用 > 选 OXE > Data Collection 页签 > Default cost center=CC_OXE
       （承接中继组等无成本中心对象）。
    3. OXE 完整同步（右键 OXE > Synchronization > Complete > Separate，四步操作同 c01）。
    4. 灌测试票：ACCOUNTING_2025.txt 复制到 C:\8770\data\loader\networknumber=1 → Service Manager 停
       NMC Loader → Refresh（同 c05）；Organization > Records 确认 ≥168 票（显示上限 200）。
    5. 成本计算：Accounting/traffic > Compute cost：起日 1/1/2023、勾 Force cost calculation >
       Simple job > Apply；Organization > Records 右键 Refresh 核对 Direct Carrier Cost w/o tax 列。
    6. 建树：Organization > Properties 页签改根名=Alcatel；根右键 Create > Level 建 Brest、Colombes；
       剪切成本中心 Training、TSS 粘贴到 Brest，CC_OXE、MKT 粘贴到 Colombes——树建成后票据按树分布。
    7. 改成本中心（正道）：OXE 配置 > Users > 31000 > Rights 页签 > Cost Center ID=3（TSS）> Apply；
       回组织树看 31000 从 MKT 移到 TSS，原位置留灰色历史条目。
    8. 权限实践 A（允许）：组织图中把中继组 1 SIP_Public 从 CC_OXE 剪贴到 MKT——成功（不影响话机侧）。
    9. 权限实践 B（拒绝）：组织图中把分机 31011 从 TSS 剪贴到 MKT——失败（分机成本中心只能经 OXE
       配置或目录应用改）。
    10. 复制语义：组织图中 Copy Training 到 Colombes——复制件保留记录并转为 inactive（灰），粘贴件
        为 active；Cut MKT 到 Brest——原件带记录转移到新位置。
  verification: |
    组织树结构与票据分布符合预期（p283）；灰色历史条目可见（p284）；非法搬移被拒（p286）。
  conditions: 树重建前清空旧条目；默认成本中心先于同步配置。
  tags: [lab, organization, cost-center, levels]

- id: c12
  title: 历史数据迁移与回溯（Assign earlier creation date + ToolsOmniVista 组织更新）
  type: lab
  source_pages: p289-295
  source_chapter: Accounting organization / Updates of creation dates & Complete organization tree update
  source_quote: |
    "TO ASSIGN CORRECTLY THE HISTORY FROM AN INACTIVE SUBCRIBER TO THE ACTIVE ONE, YOU MUST SELECT ITS
    DEVICE AND NOT THE USER." (p290)；
    "Enter the directory manager account password: superuser — Enter 'y' to stop the 8770 services
    (mandatory)" (p293)；
    "Levels, cost centers and persons cannot be backdated. That's why the inactive cost center
    Training must be deleted manually." (p295)
  steps: |
    1. 单设备回溯：组织树选 MKT 下的 inactive 31000，Property 页签记下其创建日期；再选 TSS 下的
       active 31000 记下创建日期。
    2. 右键 active 31000（**选设备不是选用户**）> Assign earlier creation date… > 新日期填 inactive
       条目的创建日期（实验口径 11/17/23 11:45 AM）> 确认告警（inactive 数据将被删除）。
    3. 验证：inactive 31000 消失，active 31000 取回完整历史（Records 页签）。
    4. 全树重建：在 OXE 配置把 31001→TSS（Cost Center ID=3）、31011→MKT（Cost Center ID=1），组织树
       自动更新出新的灰/活条目。
    5. 全局重挂：Windows 资源管理器进 C:\8770\bin\ > 双击 ToolsOmniVista.exe > 输 directory manager
       口令（实验口径 superuser）> 输 y 停 8770 服务（强制）> 菜单 3 Accounting Organization Update >
       1 > 输 y 确认（"All entities with historical data ... will be deleted ... tickets and Ptp
       counters will be reassigned"）> 等完成（实验 5.172s）> 0 退出菜单、0 退出工具。
    6. 手工收尾：组织树中 inactive 的成本中心 Training 无法被工具处理（level/成本中心/人不可回溯），
       右键 Delete 手工删除。
  verification: |
    工具输出 "Accounting organization has been updated — End processing successful"（p293）；组织树仅剩
    活动条目（p294）；Training 已删（p295）。
  conditions: 执行前建议归档（工具删除不可逆）；服务中断窗口需约定。
  tags: [lab, backdating, toolsomnivista, organization-update]

- id: c13
  title: 掩码档案配置与解密账号（Mask data access 组）
  type: lab
  source_pages: p304-320
  source_chapter: Mask profiles
  source_quote: |
    "Generate a copy of the Default mask profile: ­ Mask the 4 last digits, the duration, the cost and
    the date in case of masking. ­ Mask the last digit, the duration and the date in case of
    unmasking." (p306)；
    "BY DEFAULT, THE GENERATION OF A REPORT WITHOUT MASK IS NOT ALLOWED. TO USE UNMASKING OPERATION,
    IT IS NECESSARY TO CREATE AN 8770 LOGIN WHICH IS MEMBER OF THE GROUP 'MASK DATA ACCESS'." (p314)
  steps: |
    1. 确认组织树（Alcatel/Brest/Colombes + Training/TSS/MKT，分机已分布）。
    2. 打开掩码管理：Organization 页签 > Masks 图标。
    3. 建档案 A：选 Default > 复制图标 > 名 "Copy of Default" > 配置：masking=遮后 4 位 + duration +
       cost + date；unmasking=遮后 1 位 + duration + date > OK。
    4. 建档案 B：新建空档案 "TSS Profile"：masking=遮后 5 位；unmasking=完整显示被叫号 > OK。
    5. 挂全树：Organization > 根 Alcatel > Properties > Masks=Copy of Default（默认全树继承）；
       查 Training 成本中心 Properties 确认 Inherited Masks 生效（显示 Copy of Default (inherited)）。
    6. 按条目覆盖：TSS 成本中心 > Properties > 取消 Inherited mask > Masks=TSS Profile >（其下设备
       全部继承该档案）。
    7. 验证遮蔽：TSS/Training > Records 页签（关开应用后生效）。
    8. 生成掩码报告：Reports > Accounting 目录预定义 Duration by station > Copy 粘贴到 My Reports >
       右键 Generate Report > 过滤器日期设 2023 年（按库内票年）> Cost Center、Name 过滤 > 成功；
       分别看 Training（Copy of Default：后 4 位+时长+成本+日期遮蔽）与 TSS（TSS Profile：后 5 位）。
    9. 配解密：Security > nmc > 8770 administration > Administrators > 右键 Create > Administrator：
       Last name=unmasking、Password=superuser（实验口径）；Groups > Mask data access > Members 字段
       > 搜索并加入 unmasking；**先关闭 Reports 应用**（组变更生效条件）。
    10. 生成解密报告：右键报告定义 > Generate report w/o mask > 输入 unmasking 口令 > 过滤器同上 >
        成功；对比掩码/解密两版（解密程度仍受各档案 Unmasked 类别控制）。
    11. 认知点：TSS 记录里 029845---- 形态的号码是 OXE 侧遮蔽的，8770 无法还原（p319）。
    12. 复位：根 Properties > Masks=Default；TSS Properties > 重新勾 Inherited Masks。
  verification: |
    掩码报告按档案差异化遮蔽（p313）；解密报告生成成功且差异可见（p318）；OXE 侧遮蔽号码不可解（p319）。
  conditions: c11 完成后的组织树；解密账号口令在生成时索要。
  tags: [lab, mask, unmasking, confidentiality]

- id: c14
  title: 成本档案（发票价调整与订阅费）
  type: lab
  source_pages: p331-340
  source_chapter: Cost profiles
  source_quote: |
    "Create a cost profile called Root cost: ­ To apply an increase of 50% for outgoing calls.
    ... TSS cost: ­ To apply an increase of 20% and to add a fixed cost of 0,5 euro for outgoing
    call." (p335-336)；
    "Variable cost(s) — Yes. Select the Variable Cost(s) option if an adjustment profile has been
    added or modified. Fixed Cost — Select this option to update subscription records" (p339)
  steps: |
    1. 打开成本档案：Organization 页签 > Cost Profile 图标；Invoiced cost w/o tax 页签认知字段
       （Call Type/Type/Parameter A/B/Currency；换算示例 +10%→A=1.1,B=0 或 A=10；+5%+0.1€→A=1.05,
       B=0.1 Euro）。
    2. 建档案 A：选 Default cost profile > 复制 > 名 "Root cost" > 呼出类型 +50%（百分比或线性）> OK。
    3. 建档案 B：复制 Default > 名 "TSS cost" > 呼出 +20% 且加固定 0.5€/通话 > OK。
    4. 挂全树：组织根（NMC）> Properties > Costs=Root cost。
    5. 按条目覆盖：TSS 成本中心 > Properties > Inherited Costs=No > Costs=TSS cost（作用于该子树）。
    6. 更新存量：Accounting/traffic > Compute cost：日期区间按需（空=全部）、勾 Variable cost(s)=Yes
       （调整档案变更）；若改订阅档案则勾 Fixed Cost（先删后重建订阅记录，量大耗时长）；可加 Force。
    7. 查看发票价：Organization > TSS > Properties 查看应用后的成本；Records 页签核对 invoiced cost。
    8. 订阅认知（讲义口径，p327）：订阅票在每次同步后生成（日/周日/月一），时间戳 00:00:00，月订阅
       当月加入次月计，订阅计算永不处理当天。
  verification: |
    TSS 子树的记录 invoiced cost 按 +20%+0.5€ 呈现（p340 步骤 5 查看口）；其余树按 Root cost +50%。
  conditions: c13 完成后的组织树；教学百分比/固定费为实验口径。
  tags: [lab, cost-profile, invoiced-cost]

- id: c15
  title: 计费可见域（Visibility domain）
  type: lab
  source_pages: p348-357
  source_chapter: Accounting domains
  source_quote: |
    "Create 2 administrators accounts, members of the group Accounting Experts. ­ AdminBrest (account
    password: superuser) ­ AdminCostCenter (account password: superuser)" (p349)；
    "Visibility domain — Yes ... You must restart the Accounting/traffic/VoIP application to take into
    account the visibility domain activation." (p351)
  steps: |
    1. 建管理员：Security > nmc > 8770 administration > Administrators > 右键 Create > Administrator：
       AdminBrest（口令 superuser）、AdminCostCenter（口令 superuser）（实验口径）。
    2. 入组：Groups > Accounting experts > Members 字段 > 搜索并加入两账号。
    3. 启用功能：Administration > nmc > Application Configuration > Application Settings > Accounting >
       AccountingParameters > Visibility domain=Yes；**重启计费应用**；状态区警告"未配域，仅根可见"。
    4. 根域：Organization 页签 > 选根 > Properties > Domain Name=Alcatel。
    5. 超管配域：Security > AdminNmc > Individual 页签 > Visibility domain for accounting=Alcatel >
       关闭并重启计费应用——AdminNmc 全域可见。
    6. 配子域：Brest level 属性 Domain name=Brest；MKT 成本中心=MKT；Training=Training（子节点无域则
       继承父域，不必逐级配）。
    7. 配访问：AdminBrest > Individual > 域=Brest；AdminCostCenter > Individual > 域=Training > 右键
       该字段 Add a value > 再填 MKT。
    8. 验证：分别以两账号登录开计费应用——AdminBrest 只见 Brest 子树；AdminCostCenter 只见 Training
       与 MKT。
  verification: |
    两账号组织树视图按域裁剪（p356-357）；AdminNmc 全树可见（p352）。
  conditions: c11/c13 完成后的组织树；群组域无效——必须配到用户（p355）。
  tags: [lab, domains, access-control]

- id: c16
  title: 报表应用全流程（个人目录、生成、导出、邮件、累计报表、定时）
  type: lab
  source_pages: p366-383
  source_chapter: Reports application
  source_quote: |
    "Maximum number of lines in TXT format — 400 ... Maximum number of pages in PDF format — 50" (p367)；
    "The Daily Station Traffic is a daily report. ... based on daily cumulative counters ... The
    cumulative counters calculation is performed every night by the 8770 server." (p380)；
    "Select As Scheduled, and setup the hour at 5:00AM — Select Daily — Tick the Saturday and Sunday
    days" (p383)
  steps: |
    1. 看尺寸上限：Preferences > Reports > Reports Preference（TXT 400 行/HTML·PDF·EXCEL 50 页/X 轴
       100/库 100000 行；超限截断提示）。
    2. 建个人目录：Accounting 目录 > 右键 AdminNmc > Add > Folder > 名 "My Reports"。
    3. 取定义：预定义报表 Duration by station > Copy > 粘贴到 My Reports。
    4. 生成两实例：右键定义 > Generate Report > 过滤器 Date/Hour（库内票为 2023 年）与 Name/Call
       Type —— 一份全量、一份 This week。
    5. 查看：右键生成实例 > Open to View…（工具条：导出/打印/搜索/翻页）。
    6. 导出文件：右键定义 > Export… > File > Next > 选 TXT/HTML/PDF/EXCEL > OK > 选存储位置（默认
       名=定义名+生成日期）。
    7. 邮件导出前置：Administration > Nmc > OmniVista 8770 > Export parameters 页签：Mail server=
       mail-server.company.com（可带 :端口，冒号后无空格，默认 25 可省）、认证不用；发件人默认
       OmniVista。Client PC 上 Thunderbird 选对应 POD 的 profile 启动（实验口径）。
    8. 邮件导出：右键第二份定义 > Export… > 选 Email 通道 > 目的地 alban.podX@company.com（多址逗号
       分隔）> HTML > OK > Thunderbird 收信确认。
    9. 累计报表：预定义 Daily Station Traffic > 复制粘贴 > Generate；若实例为空=夜间累计计数器未算
       ——到 Account./traf./VoIP > Accounting/traffic > Total calculation… 手工补算后重新生成。
    10. 定时：右键 Duration by station 定义 > Schedule… > 过滤器 > Generation Options 按需（打印/
        导出）> Simple job > Description、Start Date=As Scheduled 5:00AM、Repeat=Daily、Exclude
        Days=周六周日 > Apply。
  verification: |
    两个报表实例内容正确（p372）；文件与邮件导出成功（p373/p376）；定时任务出现在 Scheduler（p383）。
  conditions: 实验口径：邮件服务器为教学设施；票年 2023。
  tags: [lab, reports, export, scheduling]

- id: c17
  title: 报表定制界面巡检（定义向导、Querytool、Designer、图表）
  type: howto
  source_pages: p384-400
  source_chapter: Report customization — "Create and customize a report definition"
  source_quote: |
    "Source Specify the source (1) of data to be used by the definition: ­ Accounting records ...
    ­ Total counters" (p385)；
    "It is impossible to use headers from different areas to generate a graph or a formula." (p396)
  steps: |
    1. 建定义：个人文件夹右键 Add > Definition > 向导：Source=Accounting records（或 Total counters，
       后者生成显著更快）> Item（计数器源才选目标对象）> Type=Detailed/Grouped > Template（默认
       Template/Compact template，均不可删）> 名称/描述/关键词。
    2. Querytool：上层为可用库字段（§=报表内换行符），双击加入下层；同字段可加多次配不同过滤；右键
       列删字段；拖拽调列序。
    3. 字段属性：Field Values（换字段）、Field label（改名）；grouped 专有 Operation=Group by（默认）/
       Count/Minimum/Maximum/Total/Average（detailed 留空）；表达式编辑器加公式（例 $cost=€cost×1.3）。
    4. Sort：升/降序；组表头左侧列优先级最高。
    5. Filter：选择准则编辑器；Generation Time Filter=生成期再选（一份定义多场景）；Display=Not
       present（只过滤不显示）/Detail/Group Header。
    6. Hit-list：grouped 专用限量（例：时长最长的前 10 台话机）。
    7. Designer：区域=Report Header/Footer、Page Header/Footer、Group Header/Footer、Detail；字段
       属性（字体/颜色/格式/前后缀/小数位/预览）；工具条（保存/打印格式/文本/库字段/公式/图片/图表/
       生成日期/页码/过滤说明/保存路径/最小高度）。
    8. 视图规则：图表/公式只能取同一视图区域的表头；Extension 组页脚可引用 Detail 区的 Charge Units/
       Duration 求和；Name 页脚把 View 切到 Extension 后可引用分机级 Sum。
    9. 图表：右键区域 > Insert Chart > 类型（Bar/Curve/Pie/Plot/Stacked Bar/Multi-counter pie）>
       View/X 轴/Y 轴（从 Data Sources 选入 Chart Data）> 版面（标题/Y 轴名/图例锚点）。
  verification: |
    巡检型章节（无独立测试问题）；产出能力由 c18-c22 五个练习承接验证。
  conditions: 依赖已有库内记录；模板不可删默认两件。
  tags: [howto, reports, querytool, designer]

- id: c18
  title: 报表练习规格（report #1-#5 题面）
  type: howto
  source_pages: p401-404
  source_chapter: Report customization (How-To) — "Create the report definition 'report 1..5'"
  source_quote: |
    "The report only displays outgoing call having a duration > 0. ­ The cost must be displayed with
    4 decimals. ­ The column Cost w/o Tax Dollar gives the cost in Dollar" (p402)；
    "5 Create the report definition 'report 5' — This report must display the 3 extensions having the
    highest number of outgoing calls." (p404)
  steps: |
    1. report 1（详细）：列=分机/被叫号/日期时间/时长/成本€/成本$；只显呼出且时长>0；成本 4 位小数；
       $ 列按汇率换算（p402 写 1€=1.21$，实现章 p550 用 1.3——以当次交付约定为准）；€/$ 后缀；分机
       生成期过滤器。
    2. report 2（详细+分组头）：分机升序组头，组内按时长降序；每分机给时长与成本合计；成本与合计
       4 位小数；报表末尾加条形图"每分机总成本"。
    3. report 3（详细+嵌套汇总）：成本中心组头内嵌分机汇总（成本中心合计基于分机合计）；只显 PSTN
       呼出。
    4. report 4（分组）：只显 Telecom 1 与 Telecom 2 的呼出（实现章 p613 用 Filter Editor 选双运营
       商）；列=被叫区/运营商/分机/呼叫数/时长/直连成本；分机、被叫区、运营商三级合计；运营商总成本
       图表。
    5. report 5（分组+hit-list）：呼出次数最多的前 3 台分机；表=分机/呼叫数/总时长/总成本；附饼图
       每分机总成本。
  verification: |
    题面章节；逐条由 c19-c23 的实现章验收。
  conditions: 题面为教学练习；汇率与运营商名的书内不一致见 counter-example。
  tags: [howto, reports, exercises]

- id: c19
  title: 定制报表实现 report #1（过滤、公式换汇、生成期过滤器、版面微调）
  type: lab
  source_pages: p549-562
  source_chapter: Report customization – report #1
  source_quote: |
    "From the column Duration, click on the Filter option — On Duration filter, select greater than
    — On next field, enter 00:00:00" (p556)；
    "$cost = € cost*1.3 — Rename the field label ... by Cost w/o Tax Dollar" (p557)
  steps: |
    1. 建目录：Accounting > AdminNmc > Add > Folder > "Customized reports"。
    2. 建定义：右键 Definition… > Record > Detailed > Compact Template > 名 "Customized report #1"。
    3. Querytool 选字段：Organization>Extension；Records>Called Number、Duration；Date>Date/Hour；
       Costs>Communication cost $w/o tax（两次）。
    4. 过滤时长：Duration 列 Filter > greater than > 00:00:00。
    5. 美元列：第二列成本 Field value 开表达式编辑器 > 公式 $cost=€cost*1.3 > 改名 Cost w/o Tax
       Dollar；第一列改名 Cost w/o Tax Euro。
    6. 生成期过滤：Extension 列勾 Generation Time Filter。
    7. Designer：Paper Format=Landscape；拖动字段标签与数据对齐；拉宽被叫号/日期列；点 Maximum
       Reduction 收紧行距。
    8. 小数与符号：两成本数据 Properties > 小数位=4、Suffix=€/$。
    9. 生成：Generate report > 分机过滤器留空 OK > Open to View。
  verification: |
    报告只含呼出且时长>0；两列成本 4 位小数带币种符；生成期分机过滤生效（p562 截图说明）。
  conditions: c16/c17 完成；汇率 1.3 为实现章口径（与题面 1.21 不一致，见 counter-example）。
  tags: [lab, reports, formula, filter]

- id: c20
  title: 定制报表实现 report #2（组头排序、Sum 公式、前缀文本、条形图）
  type: lab
  source_pages: p563-584
  source_chapter: Report customization – report #2
  source_quote: |
    "Display — Select Group Header. Sort Type — Select Ascending." (p569)；
    "Double-click on Sum function — Double-click on Duration — The formula Sum of duration is
    created" (p573)；
    "View — Select the view you want to display the data (i.e. Extension) — X-axis — Extension" (p580)
  steps: |
    1. 建定义：Customized report #2（Record > Detailed > Compact Template）。
    2. Querytool：Extension、Called Number、Date/Hour、Communication cost $w/o tax（两次）。
    3. Extension 列：Display=Group Header、Sort Type=Ascending；Duration 列 Sort Type=Descending；
       Duration 过滤 greater than 00:00:00；成本列改名 Cost w/o Tax Euro。
    4. Designer 布局：把成本标签与数据拖到 Duration 旁；拉宽被叫/日期列；Maximum Reduction。
    5. 组合计：Extension 组头放大 > Extension 数据字段右键 Insert Formula > Sum(Duration)——对齐
       Duration 数据列、加 Border；同法 Sum(Cost w/o Tax Euro)；Insert Database Field > Extension
       加"Total for the extension: "前缀文本（Properties>Prefix）。
    6. 4 位小数 + € 后缀（成本与合计两字段都设）。
    7. 条形图：Report Footer > Insert Chart > Bar Chart > View=Extension、X=Extension、Y=Sum(Cost
       w/o Tax Euro) > 标题 "Total cost per extension"、Y 轴名、图例 Upper left。
    8. 生成并查看。
  verification: |
    每分机一组、组内时长降序、组尾合计与条形图正确（p582-584 截图说明）。
  conditions: c19 完成；Sum 公式只能在同视图区域内引用。
  tags: [lab, reports, sum, chart]

- id: c21
  title: 定制报表实现 report #3（嵌套汇总：成本中心→分机；PSTN 呼出过滤）
  type: lab
  source_pages: p585-605
  source_chapter: Report customization – report #3
  source_quote: |
    "Call Type field is only used to select the type of call. ... On Call Type filter, select equal
    PSTN Outgoing Call ... Display ... Not Present" (p592)；
    "Change the default view to Extension ... Double click on =Sum(Direct Carrier Cost w/o Tax" (p598-599)
  steps: |
    1. 建定义：Customized report #3（Record > Detailed）。
    2. Querytool：Cost Center（组头）、Extension（组头）、Called Number、Duration、Direct Carrier
       Cost $w/o tax。
    3. PSTN 过滤：加 Call Type 字段 > Display=Not Present > Filter=equal PSTN Outgoing Call。
    4. 直连成本列改名 Direct Carrier Cost w/o Tax。
    5. 分机级合计：Extension 组头 Insert Formula > Sum(Direct Carrier Cost w/o Tax)（边框、对齐）；
       Insert Database Field > Extension 加前缀 "Total for the extension: "。
    6. 成本中心级合计：Cost Center 组头放大 > **把该区 View 改为 Extension** > Insert Formula >
       Sum(=Sum(Direct Carrier Cost w/o Tax))（引用分机级合计）> 边框；Insert Database Field > Cost
       Center 加前缀 "Total for the cost center: "。
    7. € 后缀三处（明细、分机合计、成本中心合计）。
    8. 生成并查看（三级汇总逐层嵌套）。
  verification: |
    报告按成本中心→分机→明细三级呈现，只含 PSTN 呼出（p605 截图说明）。
  conditions: 跨区域引用必须切 View（principle p37）。
  tags: [lab, reports, nested-sum, call-type-filter]

- id: c22
  title: 定制报表实现 report #4（grouped 双运营商汇总 + 遮蔽技巧 + 饼图）
  type: lab
  source_pages: p606-626
  source_chapter: Report customization – report #4
  source_quote: |
    "Click on the Filter menu ... On Direct Carrier filter, select equal — Then, click on Choose Your
    DB Field menu to select the carrier you want to filter — Telecom 1 — Add another filter ...
    Telecom 2" (p613-614)；
    "On Foreground field, select the blank color ... The formula of Called Region field is masked" (p617)
  steps: |
    1. 建定义：Customized report #4（Record > **Grouped** > Compact Template）。
    2. Querytool：Direct Carrier（组头）、Direct carrier §Called Region（组头，改名 Called Region）、
       Extension、No. of calls、Duration、Direct Carrier Cost §w/o tax。
    3. 聚合：No. of calls/Duration/Cost 三列 Operation=Sum；成本列改名 Direct Carrier Cost。
    4. 双运营商过滤：Direct Carrier 列 Filter > equal > Choose Your DB Field 选 Telecom 1 > 加第二条
       件选 Telecom 2（Filter Editor）。
    5. 被叫区合计：Called Region 组头放大 > Insert Formula > Sum(Direct Carrier Cost)（中间层，先做
       载体）。
    6. 遮蔽中间层：该公式字段 Properties > Foreground=空白色（信息保留参与上层计算但不显示）。
    7. 运营商合计：Direct Carrier 组头放大 > View 切到 Called Region > Insert Formula > Sum(Sum(
       Direct Carrier Cost)) > 边框；Insert Database Field > Direct Carrier 加前缀 "Total for the
       carrier: "。
    8. € 后缀（明细与两级合计）。
    9. 饼图：Report Footer > Insert Chart > View=Direct Carrier、X=Direct Carrier、Y=Sum(Sum(Direct
       Cost Carrier)) > 标题 "Total cost by carrier"。
    10. 生成并查看。
  verification: |
    报告只含 Telecom 1/2 呼出，按运营商-被叫区-分机聚合，中间层被遮蔽、饼图汇总正确（p625-626）。
  conditions: grouped 定义的 Operation 才可用；遮蔽是保留中间合计的唯一办法（p617）。
  tags: [lab, reports, grouped, filter-editor, masking]

- id: c23
  title: 定制报表实现 report #5（Hit-list 前 3 + 饼图 + 空表头遮蔽技巧）
  type: lab
  source_pages: p627-643
  source_chapter: Report customization – report #5
  source_quote: |
    "Enable the option Hit-list Report — Enter the number of extensions you want to display in the
    hit-list (i.e. 3)" (p634)；
    "The Detail header has disappeared on last page of the report." (p643)
  steps: |
    1. 建定义：Customized report #5（Record > Grouped）。
    2. Querytool：Extension、No. of Calls、Duration、Communication cost §w/o tax。
    3. 改名：Duration→Total Duration、成本→Total cost。
    4. Operation=Sum（呼叫数/时长/成本三列）；No. of Calls Sort Type=Descending。
    5. Hit-list Report 勾选、数量=3。
    6. Designer：标签与数据拖右侧、放大字段；Total cost 后缀 €。
    7. 饼图：Report Footer > Insert Chart > Pie > View=Detail、X=Extension、Y=No. of Calls > 标题
       "Highest number of calls"。
    8. 生成发现末页多余的空 Detail 表头（Notes：需要加一个全呼叫共有字段做组头把它顶掉）。
    9. 修版：Querytool 加 Organization>Country 字段并移到最左 > Display=Group Header；Designer 里把
       Country 字段及其文本 Properties > Foreground=空白色遮蔽。
    10. 重新生成——末页 Detail 表头消失，前三名表格与饼图干净呈现。
  verification: |
    报告只显呼出最多的 3 台分机（Hit-list 生效）；末页空表头消失（p643）。
  conditions: Hit-list 仅 grouped 定义；空表头遮蔽为通用版面技巧。
  tags: [lab, reports, hit-list, pie-chart]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 23 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 OXE 纳管 | 有 → c01 |
| task-02 SIP 模拟器对接 | 有 → c02 |
| task-03 OXE 外部计费开启 | 有 → c03 |
| task-04 维护命令核查 | 有 → c04（步骤 2-5） |
| task-05 票据回收链路 | 有 → c04（步骤 6-11） |
| task-06 币种/税/国家 | 有 → c05（步骤 4-7） |
| task-07 Telecom 1 建模 | 有 → c06 |
| task-08 运营商演进 | 有 → c07 |
| task-09 Telecom 2 | 有 → c08 |
| task-10 Service 脉冲运营商 | 有 → c09 |
| task-11 Code Book 导出导入 | 有 → c10 |
| task-12 组织树搭建 | 有 → c11 |
| task-13 历史数据迁移 | 有 → c12 |
| task-14 掩码与解密 | 有 → c13 |
| task-15 成本档案 | 有 → c14 |
| task-16 可见域 | 有 → c15 |
| task-17 报表生成/导出/定时 | 有 → c16 |
| task-18 报表定制 | 有 → c17（界面）+ c18（题面）+ c19-c23（实现） |
| task-19 VoIP 性能 | 无独立条目——原书 How-To（p417-428）为参数配置型实验（开关/阈值/清理周期/命令巡检），数值口径已入 principle p38/p39/p48，操作要点（OXE IP tickets YES、Loading>VoIP、Total calculation、ipview）已入 framework f22 与 menu-path f27；若阶段 1.5 需要可补写。 |
| task-20 流量分析 | 同上：p442-454 配置型实验，口径在 principle p40/p41（阈值、PtpType ALL），流程在 f09/f23。 |
| task-21 Tracking | 同上：p469-488 配置型实验，档案规格在 principle p43，原理链在 f24；三档案步骤为字段填写型，未单列 case。 |
| task-22 Web Performance | 同上：p509-517 配置型实验，SNMPv3 参数在 principle p45，采集结构在 f25。 |
| task-23 归档恢复 | 同上：p528-548 参数+任务型实验，规则在 principle p46/p47，流程在 f26。 |

**统计与说明**：23 条（lab 21 + howto 2：c17 界面巡检、c18 练习题面）。23 项任务中 18 项有实验级条目直接覆盖；task-19~23 共 5 项为"配置开关+数值口径"型实验（VoIP 性能 p417-428、流量分析 p442-454、Tracking p469-488、Web Performance p509-517、归档 p528-548），其可操作内容（菜单路径、参数值、验证点）已分散落在 principle（p38-p48）与 framework（f22/f23/f24/f25/f26/f27）对应条目中——刻意取舍：这五章的"步骤"本质是逐页填参数，与 c03/c05 同型，为控制条目粒度未再展开；阶段 1.5 组装 skill 时如需步骤级依据，可从对应条目 source_pages 回溯原文补齐。
