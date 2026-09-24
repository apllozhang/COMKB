# 框架/流程/结构候选 — OmniVista 8770 R5.2 计费与性能管理 (8770XTE201EN Ed45)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、对象模型与文件体系。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——产品底座 → 实验平台 → 计费管道 → 钱/组织/安全治理 → 报表输出 → 性能监控 → 归档
  type: flow
  source_pages: p3-650
  source_chapter: 全书章节推进（SOLUTION OVERVIEW 起至 END OF TRAINING EVALUATIONS）
  source_quote: |
    "OMNIVISTA 8770 - R5.2 ACCOUNTING AND PERFORMANCE ADMINISTRATION - EDITION 45" (p1)
    "✓ General overview ✓ Network topology ✓ Architecture ✓ Virtualization ✓ Cross compatibility
    ✓ Applications suite ✓ Setup suite ✓ Network suite ✓ Reports suite ✓ Directory suite
    ✓ 8770 WBM client ✓ Conclusion" (p4)
  summary: |
    课程按十段推进：①8770 产品概览（架构/虚拟化/兼容性/五套件）；②RLAB 实验平台 + SIP 运营商模拟器；
    ③计费票据原理（缓冲/文件/出票规则）；④OXE 侧接入两个实验（节点注册、SIP 模拟器对接）；⑤票据全链路
    （外部计费配置→维护命令→五种计费方法→回收与加载→PCS）；⑥运营商资费体系（对象模型→币种税→
    Telecom 1/2/Service 三个运营商实验）；⑦Code Book 导出导入；⑧计费组织与安全（组织树→掩码→成本
    档案→可见域）；⑨报表体系（预定义→定制→五个练习实验）；⑩性能监控四件套（VoIP 性能→流量分析→
    Tracking→Web Performance）；⑪归档收尾。这是"先管道后治理、先算钱后看质量"的交付主线，也是生产
    项目的推荐顺序。
  conditions: 无版本前提；各章实验相互依赖（后续实验复用前序产出，如 Telecom 1 被 report #3/#4 引用）
  tags: [flow, course-structure, delivery-order, master-flow]

- id: f02
  title: RLAB 实验平台结构——POD 池 + 公共资源区 + 六实例 POD
  type: structure
  source_pages: p41-51
  source_chapter: REMOTE LABS PLATFORM / Introduction, Training Platform, Settings
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a
    data center." (p43)
    "OMNIVISTA 8770 SERVER 8770_OV8770_SETUP nms 192.168.1.70 ... 8770 credentials: • AdminNmc
    superuser Superuser01*  OmniVista 8770 server already installed" (p47)
  summary: |
    实验平台分两层：POD 1..n 相互独立、配置相同；公共 Pod 提供 NAS（软件/许可）、SIP 模拟器（12.0.0.2）、
    邮件服务器。每个 POD（网段 192.168.1.x，网关 192.168.1.254，内外 DNS 192.168.1.250/10.20.30.250）
    含六个实例：OXE（csa 物理 192.168.1.1 / csm 主 192.168.1.3，mtcl/swinst/root，密码 Superuser2580*，
    已建用户 31000-31002）、OMS（192.168.1.13）、FlexLM 许可服务器（192.168.1.80，letacla1）、Client PC
    （192.168.1.10，装 IPDSP 31000 + MicroSIP 31001/31002 + 公网 MicroSIP + TrapReceiver）、OmniVista
    8770 服务器（nms 192.168.1.70，预装，AdminNmc/Superuser01*）。实例访问两模式：Console mode（管
    理实例/装 8770，无音频）与 Remote Desktop Connection（基于 Guacamole，实验必用以共享软话机音频）。
  conditions: 仅培训环境（RLAB），所有 IP/账号为实验口径；8770 服务器已预装（部分实验重装为讲义演示）
  tags: [structure, lab, rlab, topology]

- id: f03
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则
  type: diagram
  source_pages: p53-58
  source_chapter: SIP CARRIER SIMULATOR / Overview, Public and Emergency numbers, Call to your PBX
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... ITSP1 Public gateway public.itsp1.com
    10.20.30.50 ... SIP domain: sip.itsp1.fr" (p54)
    "DDI table - First external number 3321PN41000 ... DDI table – First internal number 31000 ...
    Example: 100's external number 3321PN41100" (p57)
  summary: |
    模拟器在 RLAB 公共区扮演出局运营商：两条腿——SIP 网关 gateway1.itsp1.com（PBX 注册账号
    pbxP/alcatel，SIP 域 sip.itsp1.fr）与公网网关 public.itsp1.com（两个 MicroSIP 模拟 Public/Urgence
    用户）。号码规则：PN 为两位 POD 号；公网主号 3321PN12345（别名 3311-3351PN12345 国内、3361/3371
    PN12345 移动、4421PN12345 国际 UK），紧急号 112/15/17/18。呼出变换示例（POD 3）：拨 0110312345
    → 送出 +33110312345。呼入本机：安装号 3321PN41000，分机 100 即 3321PN41100。OXE 侧按 POD 号
    配 Registration ID=pbxN 与 DID 首外线 33210N41000。
  conditions: 实验口径（RLAB 专用基础设施）；所有账号/号码均为教学约定值，不可套用到生产
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f04
  title: OmniVista 8770 系统架构与协议矩阵一张图
  type: diagram
  source_pages: p6-7
  source_chapter: SOLUTION OVERVIEW / Network topology & Architecture
  source_quote: |
    "HTTPS, LDAP(S) | IPSec, Corba, TDS, LDAP(S) | LDAP(S) | HTTPS ... CMISE, (S)FTP, Telnet/SSH,
    LDAP — OXO Connect ... SNMP Hypervisor SNMPv3 ... OMC (FTP, HTTPS)" (p7)
  summary: |
    拓扑三层：8770 Client（GUI，登录密码）+ WBM client（HTML 目录访问，允许匿名）+ Manage My Phone
    （终端用户 HTML 自助）经 LAN 连 8770 server。协议矩阵：Server↔OXE 走 CMISE/(S)FTP/Telnet-SSH/
    LDAP；↔OXO Connect 走同步/用户创建经 OMC (FTP,HTTPS)；↔SIP 话机 SNMPv3；Web Directory 走
    HTTPS/LDAP(S)；内部 MariaDB (SQL) + LDAP；邮件 SMTP；WBM 走 HTTPS；对 SNMP Hypervisor 出
    SNMPv3 告警；目录可从 LDAP Client 导入、可群发配置。理解点：8770 是纯 IP 连通的集中网管，
    OMC 是 OXO 侧的伴生管理件。
  conditions: 无版本前提；协议细节与端口在 8770 安装文档（书外）
  tags: [diagram, architecture, protocols, topology]

- id: f05
  title: 8770 应用套件分区——thick client 五套件 + WBM 四应用
  type: structure
  source_pages: p10-39
  source_chapter: APPLICATIONS SUITE / SETUP SUITE / NETWORK SUITE / REPORTING SUITE / DIRECTORY SUITE / 8770 WBM CLIENT
  source_quote: |
    "Administration Security Maintenance Scheduler | Server Administration Users Devices
    Configuration Alarms Topology Audit Maintenance — PCX Administration & Supervision |
    OmniVista 8770 thick client" (p10)
    "Available with Unified Management license ... Zero footprint (light client)" (p35)
  summary: |
    thick client 五套件：①Setup（Administration 应用设置、Security 管理员/口令策略/管理域、Maintenance
    服务器库备份、Scheduler 任务调度）；②Network（Configuration 节点注册与同步、OXO Connect 监督、
    Users/Devices 批量开通、Alarms/Topology/Audit/PCX Maintenance）；③Reporting（Account./Traf./VoIP、
    Reports）；④Directory（LDAP v3 目录、Web Directory Client）。WBM 四应用：Users（统一用户管理，
    需 Unified Management 许可）、Configuration（网络/子网/节点树浏览，一次连一台 OXE，无 SSH/Telnet）、
    Performance（仪表盘 widget）、Manage My Phone（终端用户自助）。另支持 MCS（托管 OAMP，外包运维）。
  conditions: Audit 与 Traffic Analysis 仅 OmniPCX Enterprise（p25/p29）；OXE SIP 话机不能用 Click to Call（p33）
  tags: [structure, applications, wbm, thick-client]

- id: f06
  title: 虚拟化支持矩阵与容量规划工具
  type: structure
  source_pages: p8
  source_chapter: SOLUTION OVERVIEW / VIRTUALIZATION
  source_quote: |
    "• Hypervisors • VMware ESXi (6.x, 7.0 and 8.0) • Microsoft Hyper-V® 2016, 2019, 2022
    • Nutanix AHV ( 20220304) • ASW (Amazon Web Services) ... OmniVista 8770 Capacity Planning
    tool V3.0" (p8)
  summary: |
    部署两形态：客户现场的单一 Appliance Server，或数据中心托管（大型/托管市场）。虚拟化支持
    VMware ESXi 6.x/7.0/8.0、Hyper-V 2016/2019/2022、Nutanix AHV（20220304）、AWS；虚机要求与
    物理服务器相同；虚拟化本身不占 8770 许可，但个别 Hypervisor 上的补充服务可能引增许可成本；
    选型用 Capacity Planning tool V3.0 灵活定虚机参数。
  conditions: Ed45 时点口径，落地前重核支持矩阵
  tags: [structure, virtualization, hypervisor, sizing]

- id: f07
  title: 跨版本兼容矩阵（8770 R4.2-R5.2 × PBX/OT 版本）
  type: structure
  source_pages: p9
  source_chapter: SOLUTION OVERVIEW / CROSS COMPATIBILITY
  source_quote: |
    "OpenTouch BE / MS / MC OT R2.4 to R2.6.1 X X X X | OmniPCX Enterprise OXE R12.2 to R12.4 X X X X
    | OXE Purple R100 (N1) X X X | OXE Purple R100.1 (N2) X X | OXE Purple R101.0 (N3), R101.1 (N4)
    & R101.2 (N5) X | OXO Connect / OCE R4.0 X X X X | OXO Connect / OCE R5.0 to R5.1 X X X
    | OXO Connect / OCE R5.2 to R6.2 X X" (p9)
  summary: |
    兼容性按列看 8770 版本（R4.2/R5.0/R5.1/R5.2），按行看对端版本：OT BE/MS/MC R2.4-R2.6.1 全兼容；
    OXE R12.2-R12.4 全兼容，Purple 系列随新版本收紧（R101.x 仅 R5.2 支持）；OXO Connect/OCE R4.0 全
    兼容，R5.0-R5.1 需 R5.0+，R5.2-R6.2 需 R5.1+。升级 8770 或 PBX 前必查此表。
  conditions: 矩阵随版本迭代，落地前取最新版
  tags: [structure, compatibility, versions]

- id: f08
  title: 计费票据文件体系——缓冲/tax.tmp/TAX*.DAT/ACCOUNT.LIS 四件套与落盘时机
  type: structure
  source_pages: p61-65
  source_chapter: EXTERNAL ACCOUNTING / Principle, Accounting files creation, Accounting folder
  source_quote: |
    "Accounting records storage (max 500 records) ... Buffer file used when memory buffer is full ...
    Contains the list of accounting files created on the OXE ... AAAAA <= ***** <= ZZZZZ" (p62)
    "No record received within 90 minutes ... An accounting file is created at 11:00" (p64)
  summary: |
    OXE 侧文件体系四件：内存缓冲（≤500 条记录，呼叫结束即入）；tax.tmp（缓冲满时暂存已缓冲记录的
    过渡文件）；TAX*****.DAT（压缩票据文件，***** 在 AAAAA-ZZZZZ 间递增）；ACCOUNT.LIS（DAT 文件
    清单索引）。落盘三时机：缓冲满（新票进缓冲、旧票进 tax.tmp，再下次满时合并出新 DAT 并登记
    ACCOUNT.LIS）；90 分钟无新票定时落盘；维护命令 account compress 强制落盘（节点同步也会触发）。
    文件都在 /usr4/account 目录。
  conditions: 缓冲大小 500 为 Ed45 口径；同规则适用于 IP/SIP 票据（IP.LIS/SIP.LIS）
  tags: [structure, accounting, files, buffering]

- id: f09
  title: 计费记录回收原理——四步增量同步管道（OXE→8770）
  type: flow
  source_pages: p98, p435
  source_chapter: ACCOUNTING RECORDS RETRIEVAL / Principle
  source_quote: |
    "Comparison of the ACCOUNT.LIS files ... Retrieval (via ftp) of the new files: TAXAAAAB.DAT and
    TAXAAAAC.DAT ... Records extraction and loading in the database ... Deletion of the retrieved
    files ... Update of the file" (p98)
  summary: |
    四步闭环：①同步时对比 8770 侧与 PCX 侧的 ACCOUNT.LIS（流量分析则比 pmm.lis）找新文件；②FTP
    取回新 DAT 到 C:\8770\data\loader\networknumber=N\subnetworknodenumber=NNN；③提取记录经加载
    过滤后入库（成本在此步计算）；④删除已取回文件并更新本地索引。IP/SIP 票据走同一机制（比
    IP.LIS/SIP.LIS，取回后为 .DAI）。每日/每周/每小时轮询任务由 Scheduler 驱动。
  conditions: FTP 凭证须与 OXE 一致且 FTP 用户名不可改（许可校验，见 p109）
  tags: [flow, retrieval, synchronization, ftp, loader]

- id: f10
  title: 五种计费方法与选择逻辑
  type: structure
  source_pages: p99-102
  source_chapter: ACCOUNTING RECORDS RETRIEVAL / ACCOUNTING METHODS
  source_quote: |
    "• No update of organization tree, no retrieval of accounting records — No accounting
    • Update of organization tree, records retrieved from the PCX — Detailed accounting
    • Update of organization tree, no retrieval of accounting records — Organization update without
    records retrieval ... • Global accounting per node with records retrieval" (p99)
  summary: |
    每台 PCX 可各选一种：①No accounting（不更新树、不取票）；②Detailed accounting（更新树+取票按
    分机归位，默认推荐）；③Organization update without records retrieval（只建树不取票——建树期用法，
    因树建好后再搬条目很耗时）；④Global accounting per node without records retrieval（不取票；其他
    PCX 来的本机设备票据归入代表该机的全局实体）；⑤Global per node with records retrieval（取票但
    归到 PCX 实体，实体键=<网络号×1000000+节点号>，如 1000101）。两种 global 法配合同步做组织更新。
  conditions: 方法是 per-PCX 属性；切换方法影响存量记录归属
  tags: [structure, accounting-methods, decision]

- id: f11
  title: 记录收集器与 PCS 被动回收结构
  type: structure
  source_pages: p103-106
  source_chapter: ACCOUNTING RECORDS RETRIEVAL / Records collector & Passive Communications Server
  source_quote: |
    "PCX accounting files available to an external accounting application • No accounting license,
    only Ticket collector license is required" (p103)
    "PCS ID corresponds to the PCS IP address in hexadecimal • AC199E64 corresponds to
    10*16+12.1*16+9.9*16+14.6*16+4 = 172.25.158.100" (p106)
  summary: |
    Ticket collector（票据收集器）：把 PCX 票据文件原样供给外部计费应用，只需 Ticket collector 许可
    （无需计费许可），文件落在 c:\8770\data\collector。PCS（Passive Communications Server）：经呼叫
    服务器同步透明发现并纳入；其票据文件与索引带 PCS ID 后缀（ACCOUNT_AC199E64.LIS、
    TAXAAAAA_AC199E64.DAT），PCS ID=该 PCS IP 的十六进制。8770 侧 Data collection 页签记录最后
    取回文件名。
  conditions: PCS 同步开关在 NmcArchive>Accounting>Specific（默认 Yes 随日同步）
  tags: [structure, collector, pcs, external-accounting]

- id: f12
  title: 运营商资费对象模型——Period/Calendar/Region/Tariff/Direction 五件套
  type: structure
  source_pages: p117-127, p151-175
  source_chapter: DIRECT CARRIER CONFIGURATION / Carrier configuration overview
  source_quote: |
    "The carrier configuration is based on the following objects • Region • Direction • Tariff ...
    Costs are calculated during the records loading into the database" (p117)
    "A tariff is applied to each Calling Region - Called Region pair" (p118)
  summary: |
    Carrier（运营商，Name/Symbol≤5 字母/Type=Outgoing/State/Carrier prefix/Country）下挂 Period
    （资费有效期，新周期建立时旧周期自动封口）→ 四个分支：Calendar（特定日类型+日期，如法国银行
    假日）；Region（Calling=PCX 或 PCX-中继组；Called=前缀集合；一区可兼两角）；Tariff（见 f13）；Direction
    （Calling Region × Called Region 配对 → 通信资费 + 可选服务资费/调整/时延）。未匹配方向由
    "unspecified" 兜底。成本在票据加载时按此模型计算。
  conditions: 同一前缀不能出现在不同区域；前缀按最优（最长）匹配归属
  tags: [structure, carrier, region, direction, tariff, object-model]

- id: f13
  title: 费率计算模式分类与参数体系（资费类型学）
  type: structure
  source_pages: p128-137
  source_chapter: TYPE OF TARIFF FOR COMMUNICATION COSTS
  source_quote: |
    "• Cost based on duration indicated in the accounting record • Exact duration • Round up duration
    • Round down duration ... • Cost based on number of units contained in the accounting record ...
    • OmniVista 8770 does not convert. Currency declared in the PCX must therefore be the same as
    the reference currency" (p128)
  summary: |
    四种计算模式：①Exact duration（线性，可叠加 answered call initial cost、initial duration 免费时长、
    minimum cost 保底、segments 分段单价）；②Round up/down（按阶段计价，开始即计/计满才计）；③Based
    on unit（脉冲：单价×票据 Charge units，可加 initial unit 与 unanswered call initial cost）；④Cost given
    by the PCX（直接采信 PCX 计算的成本，8770 不做币种换算）。另有 Day type（Daily/Working day/
    Weekend/特定日）× Time zone（累计须铺满全天）两维调度；Service tariff 模式独立开关用于服务费。
  conditions: exact 模式 Unit duration=60（按分钟价）或 1（按秒价）；round 模式 Unit duration=阶段时长
  tags: [structure, tariff, formula-types, parameters]

- id: f14
  title: 服务费与 SVA（增值业务）模型
  type: structure
  source_pages: p137, p163
  source_chapter: TYPE OF TARIFF FOR SERVICE COSTS
  source_quote: |
    "For AVS numbers, total tariff of the call is the sum of ... • C=0 & S=0: free contact number
    • C>0 & S=0: standard contact number • C>0 & S>0: surcharged contact number" (p137)
    "When you manage a cost based on a service, you must configure two tariffs. One tariff for the
    communication cost. Another tariff based on the same settings than the previous one for the
    service." (p162 Notes)
  summary: |
    服务费覆盖 08 开头特服号与 4-6 位短号（10XX/3YYY/118ZZZ，法国 SVA 资费由 ARCEP 监管）。模型：
    总票价 = 通信费 C（依运营商）+ 服务费 S（固定和/或按时长），三种组合对应免费/标准/加收费号码。
    配置上必须建两个资费（通信 + 服务，参数同源），并在 Direction 上同时挂 Communication tariff 与
    Service tariff；pulse 型运营商（如 Service）以 Unit cost×Charge units 出服务费。
  conditions: 服务资费的 Tax/Currency 与通信资费分开选；本书以法国 ARCEP 为例
  tags: [structure, service-cost, sva, france]

- id: f15
  title: Code Book 文件体系——十种文件与格式规则
  type: structure
  source_pages: p228-233
  source_chapter: CODE BOOK / Files description, File format, Links, Installation file
  source_quote: |
    "• Contains general information on the carrier — Information file .inf ... • Contains trunk groups
    included in a calling region — Trunk group file .trg" (p229)
    "@ is the header character ... Only one header line per file and it is mandatory in all except
    information file" (p230)
  summary: |
    Code Book = 运营商配置的文本文件集：.inf（总信息，引用其余文件、含 VERSION/CARRIER_NAME/
    CARRIER_INITIAL/EFFECT_DATE 等键）；.rgn 区域与前缀；.trf 资费；.dir 方向；.cal 特定日；.ccn 城市/
    国家名；.adj 调整系数；.fct ISDN 服务费；.itl 安装文件（主叫区内的 PCX：@REGION NUMBER NODE）；.trg
    主叫区内的中继组。格式规则：@行=表头（.inf 除外，每文件仅一行且必须有）；Tab 分隔字段；%行=注释。
    导入时按 .inf 索引重建运营商；.itl 的 Node 必须与目标机 Configuration 里声明的 PCX 名一致。
  conditions: 导出运营商需第二次导出才完整（p236）；EFFECT_DATE 改期再导入=新增 Period
  tags: [structure, codebook, file-format, migration]

- id: f16
  title: 计费组织树对象模型与自动更新来源
  type: structure
  source_pages: p253-257
  source_chapter: ACCOUNTING ORGANIZATION / Overview, Chargeable entries
  source_quote: |
    "• From OmniPCX Enterprise, at PCX synchronization or event reception • From Company directory,
    at creation, modification or deletion of a set-individual link — Automatically updated" (p253)
    "Chargeable entry placed under cost center created in organization tree — If cost center defined
    in the PCX ... Chargeable entry placed under root of organization tree — If no cost center
    defined (cc=255) in the PCX" (p256)
  summary: |
    组织树=财务组织的图形视图（level/cost center/chargeable entries），保留过去与现在（灰色历史条目）。
    数据来源两条：OXE 同步或事件；公司目录的设备-个人链接变化。归属规则：用户/话务台/数据终端在
    PCX 里设了成本中心→挂对应成本中心；cc=255→挂根；中继组/话务台组/语音信箱/工程等无成本中心
    对象→挂 Data collection 页签里配置的"默认成本中心"，或在组织图上剪贴归位（不影响话机侧）。
    成本中心修改只能经 PCX 配置或公司目录完成。
  conditions: 组织更新自动进行；手工搬移分机被组织图拒绝（见 p286）
  tags: [structure, organization, cost-center, hierarchy]

- id: f17
  title: 组织更新操作语义图——剪贴/复制/回溯/工具重建四象限
  type: diagram
  source_pages: p258-266
  source_chapter: ACCOUNTING ORGANIZATION / ORGANIZATION UPDATE
  source_quote: |
    "Cut & paste • This operation consists in moving an entry without history ... Copy & paste • This
    operation consists in moving an entry with history" (p261-262)
    "Accounting organization update • Removes historical data of all inactive entries and reassigns
    accounting records and performance counters to the corresponding active entries" (p266)
  summary: |
    四种更新语义：①Cut & paste=无历史搬移（原位置不留灰条目）；②Copy & paste=带历史另立（原件保留
    记录并转 inactive/灰色，粘贴件为 active）；③Assign earlier creation date=把非活动条目的记录按
    创建日期回挂到同身份（PCX ID/分机号）活动条目（只能选"设备"不能选"用户"；level/成本中心/人
    不可回溯）；④ToolsOmniVista.exe 组织更新=清除全部非活动条目并把票据/计数器重挂到对应活动条目
    （执行前强制停 8770 服务）。
  conditions: 回溯新日期须早于活动条目现值、晚于等于最后一条非活动条目日期
  tags: [diagram, organization-update, cut-copy, backdating]

- id: f18
  title: 掩码档案结构与继承链
  type: structure
  source_pages: p298-302
  source_chapter: MASK PROFILES / Overview, Management, Inheritance, Impact on reports
  source_quote: |
    "Following record data may be masked • Called number, Caller number, PIN..., Cost, Destination
    area..., Call duration, Call date ... Masking can vary according to the type of call
    • Personal • Project • Professional • Guest" (p298)
    "Grouped report generation • Masking/Unmasking is performed according to the 'Unmasked grouped'
    call type defined in the default profile" (p302)
  summary: |
    掩码档案按呼叫类别（Personal/Project/Professional/Guest + 系统性的 Masked group/Unmasked group）
    定义：显示前 n 位、遮蔽后 n 位、PIN/成本/地名/时长/日期开关。Default 档案挂组织根、不可改名删除
    （把遮蔽位数清 0 即等于停用），且 grouped report 只认 Default 的两个 group 类别；其余条目默认
    Inherited Masks 继承父级，取消继承可单独指定。Report w/o mask 需"Mask data access"组成员口令。
    "Display 4 digits"的语义是"至少显示前 4 位"（号码不足 4 位也全显）。
  conditions: 显示位数优先于遮蔽位数；OXE 侧已遮蔽号码 8770 无法还原（p319）
  tags: [structure, mask, confidentiality, inheritance]

- id: f19
  title: 成本档案（Cost profile）双页签结构——发票价调整与订阅费
  type: structure
  source_pages: p323-328
  source_chapter: COST PROFILES / Overview, Management, Inheritance
  source_quote: |
    "• x is the total cost • Total cost = Direct carrier cost + ISDN cost+ Indirect carrier cost
    • A and B are constant" (p325)
    "Subscription records are created at the start of the period: • Every day for daily records
    • Every Sunday for weekly records • On the first day of the month for monthly records" (p327)
  summary: |
    成本档案两块：①Invoiced cost w/o tax 页签——按呼叫类型定义发票价 = x + B 或 x×(1+A%)（线性式
    Ax+B 或百分比 x+A%x，B 须带币种），随组织树继承；②Services subscriptions 与 Station subscription
    页签——按"拥有设备/语音信箱/DDI 号"与"分机类型"定义日/周/月订阅费。订阅票由 8770 在每次同步后
    生成（日票每日、周票每周日、月票每月 1 日，时间字段 00:00:00）；月订阅当月加入者次月 1 日起计。
  conditions: 订阅成本计算永不处理当天；处理可能持续数天
  tags: [structure, cost-profile, invoiced-cost, subscription]

- id: f20
  title: 计费可见域控制机制与决策树
  type: diagram
  source_pages: p343-346
  source_chapter: ACCOUNTING DOMAINS / Overview, Domain definition, Domain access, Control mechanism
  source_quote: |
    "Visibility domain activation? ... Does the administrator have visibility domain? ...
    Accounting data of the user's domain are visible" (p346)
    "AdminNmc account have access to complete accounting organization" (p343)
  summary: |
    决策树两级：①功能开关 Visibility domain 关→所有数据可见；开→进入第②级：管理员未配域→什么都
    看不见；配了域→只见域内组织树与报表。域挂组织树节点（Properties>Domain name），未设域的子节点
    继承父级域；管理员在 Security>Individual>Visibility domain for accounting 配域（可 Add a value
    多域）。AdminNmc 是超管（根域 Alcatel）。
  conditions: 启用后须重启计费应用；群组级域配置不被采纳
  tags: [diagram, domains, access-control, decision-tree]

- id: f21
  title: Reports 应用结构——预定义/定义/实例/解密报表与 Querytool/Designer 双页签
  type: structure
  source_pages: p359-364, p385-399
  source_chapter: REPORTS APPLICATION / REPORT CUSTOMIZATION
  source_quote: |
    "• Tree structure divided into folders • Reports sorted by type of data and by type of reports
    • Report definition • Generated report • Unmasked report" (p361)
    "The Querytool can be divided into two different parts: ­ The upper part contains the list of
    available database fields ... ­ The lower part contains the fields selected" (p387)
  summary: |
    报表树按数据域分目录（Accounting/Traffic analysis/Voice over IP/Threshold/Alarms），预定义报表须
    Copy/Paste 到个人目录才能生成；节点三类：definition（定义）、generated（实例）、unmasked（解密版）。
    定义四步向导：Source（Accounting records 或 Total counters）→ Item（计数器目标对象）→ Type
    （Detailed 不汇总 / Grouped 汇总）→ Template（Template/Compact template，可自定义，不可删默认）。
    Querytool 页签管字段增删排序、Field label、Operation（Group by/Count/Min/Max/Total/Average，仅
    grouped）、公式（表达式编辑器）、Sort、Filter（含 Generation Time Filter 与 Display=Not present/
    Detail/Group Header）、Hit-list；Designer 页签管 Report/Page/Group Header-Footer 与 Detail 区、
    字段前后缀/小数位、图表（Bar/Curve/Pie/Plot/Stacked Bar/Multi-counter pie）。
  conditions: 不同区域的表头不能混用出图；报表超上限会截断并提示
  tags: [structure, reports, querytool, designer]

- id: f22
  title: IP ticket（VoIP 话单）生成与回收结构
  type: structure
  source_pages: p408-411
  source_chapter: VOIP PERFORMANCE / IP tickets generation, IP tickets files retrieval
  source_quote: |
    "A call between 2 IP devices is divided into one or more segments • IP tickets are generated at
    the end of each segment" (p408)
    "1 - COMPARISON OF IP.LIS & SIP.LIS FILES 2 – RETRIEVAL OF THE NEW FILES (FTP)
    3 – RECORDS EXTRACTION AND LOADING 4 – UPDATE OF IP.LIS & SIP.LIS FILES" (p410)
  summary: |
    一段 IP 通话按段出票（跨节点即多段，双向各一票）。票面关键字段：结束时间、节点/机框/板卡、设备
    类型（INTIP/IP-Phone/GA/GD/4645）、源/目的 IP 与分机、时长、压缩算法（G711/G723/G729A）、收/发/
    丢包数、时延表、BFI 密度。文件侧与计费同构：OXE 存 SIP*****.DAT+SIP.LIS 与 IP*****.DAT+IP.LIS，
    同步比对后 FTP 取回为 .DAI 交加载过滤（观察对象/观察日/IP 掩码）入库，夜间汇总为累计计数器，
    供超阈值告警与邮件。
  conditions: 回收任务在 Scheduler（Daily/Weekly/Hourly polling job）
  tags: [structure, voip, ip-ticket, kpi]

- id: f23
  title: 流量分析文件体系——pmm/inf 命名规则与观察对象
  type: structure
  source_pages: p431-434
  source_chapter: TRAFFIC ANALYSIS / Objects and data information, Traffic analysis files format
  source_quote: |
    "Files name: C<week nb><day><half-hour nb><seq nb>. type • Week number: 00..51 • Days:
    • M Monday • T Tuesday • W Wednesday • J Thursday • F Friday • S Saturday • U Sunday
    • Half-hour number: • 00..47 • XX: used for .inf and daily .pmm files" (p433)
  summary: |
    流量分析（仅 OXE）观察六类对象：中继组、话务台、话务台组、DECT/PWT、终端、被叫分机。数据两源：
    PCX 半小时计数器文件（/usr4/pmm，命名 C<周><日><半小时><序号>，日文件与 .inf 用 XX 占位半小时位，
    pmm.lis 作索引）+ 计费记录（供被叫号与终端观察）。回收与计费同管道（比对 ACCOUNT.LIS 与 pmm.lis）。
    计数器粒度：半小时/小时/日/月/年。报告侧有中继组呼叫分布、话务台活动率、hit-list 等预定义报表。
  conditions: 文件每半小时生成；.inf 含观察对象标识
  tags: [structure, traffic-analysis, pmm, counters]

- id: f24
  title: Tracking 原理链——文件→累计计数器→档案→阈值检测→告警/邮件
  type: flow
  source_pages: p457-464
  source_chapter: TRACKING APPLICATION / Overview, Thresholds, Tracking principle, Profile, Variation rate
  source_quote: |
    "Synchronization — TAX*****.dat Accounting files / IP*****.dat VoIP files / C*******.pmm Traffic
    analysis files / OXE SNMP MIB files → Cumulative counters on MariaDB tables → Tracking profiles
    → ALARMS GENERATION / E-MAIL SENDING" (p460)
    "Variation rate = 100 * ( current value of the data – average of the x last values of the data)
    / average of the x last values of the data" (p462)
  summary: |
    Tracking 定义=阈值集合档案（Tracking value+Period+Threshold+Call Type+Action），可按实体类型设
    默认档案（Default Tracking 图标）或对单条目指定。数据链：四源文件同步→MariaDB 累计计数器→档案
    匹配→阈值检测→告警生成与/或自动邮件。变化率公式以移动平均为基准（日期 n 对前 x 期求均），x 按
    周期取默认 30 天/3 月/1 年，可在 MonitoringParameters 改（最大告警数默认 50）。
  conditions: 超限检测由任务驱动（Detecting exceeded thresholds / 每日任务），非实时流
  tags: [flow, tracking, threshold, variation-rate]

- id: f25
  title: Web Performance 数据采集与仪表盘结构（五大主题）
  type: structure
  source_pages: p491-497
  source_chapter: WEB PERFORMANCE APPLICATION / Data collection, Web application interface
  source_quote: |
    "VoIP CDRs • Proprietary format for IP devices, IPMG, 4645 and IP-xBS… RTCP-XR format for SIP
    devices • Retrieved via synchronization process and hourly polling ... OXE SNMP MIB • A4400-RTM-MIB
    proprietary OXE MIB ... • UC-DAVIS standard MIB related to the platform health" (p492)
    "IP domains | OXE health | VoIP quality | Trunk groups | Devices" (p494)
  summary: |
    两条数据腿：VoIP CDR（话终话单，专有格式+SIP 用 RTCP-XR，经同步与小时轮询取回，可按类型/时间/
    IP 过滤）与 OXE SNMP MIB（A4400-RTM-MIB 专有 + UC-DAVIS 平台健康，R5.0 GA 固定 30 分钟轮询、
    R5.0 MD1 起可管理最低 5 分钟）。WBM 仪表盘五大主题：IP domains（压缩器/会议电路/CAC）、OXE
    health（CPU/IO/磁盘）、VoIP quality（MOS/超限票/记录分布）、Trunk groups（状态/累计 OOS 与超限）、
    Devices（NOE 设备出入服/SIP 注册）。节点仪表盘=过去 24 小时固定 5 widget；详细仪表盘=过去一天到
    一年，可增删预定义 widget、显示原始数据、加阈值线。
  conditions: 限制——Hybrid link、直连链路、远端中继组不支持；仅 ISDN（T0/T1/T2）、SIP、NDDI、ABC-F
  tags: [structure, web-performance, dashboard, snmp, cdr]

- id: f26
  title: 计费归档生命周期——31 天归档 + 94 天清理 = 最长 125 天
  type: flow
  source_pages: p520-526
  source_chapter: ACCOUNTING RECORDS ARCHIVING / Goal, Principle, Archive records process
  source_quote: |
    "Archived files • File extension = archZ (Zipped archive format) • One file per day and per node
    (if at least 1 record to archive)" (p521)
    "This task archives records from the date of the previous archiving operation until the current
    date minus 31 days ... Each archive file is conserved for 94 days ... records may be kept for up
    to 125 days maximum" (p523)
  summary: |
    目标四条：缩库提速、投诉期追溯旧票、旧票重算成本、长期备份。机制：归档任务（手动或自动）把上次
    归档日到"当前日期−31 天"的票据拷入 archZ（zip，每天每节点一档，默认路径 C:\8770_ARC\Accounting\
    tickets）；档案再保留 94 天后删除（按记录日期而非文件创建日期），故数据最长 125 天。恢复支持按
    单日或按周期，恢复标签二选一：Loaded records（入组织树、与原票无异）或 Archived records（打标、
    组织树不可见但可出报表，Record origin 列区分）；可只清除恢复票（Only restored records）。
  conditions: 恢复带重算时，运营商有效期必须覆盖被恢复记录的日期
  tags: [flow, archiving, archz, lifecycle]

- id: f27
  title: 关键菜单路径集（8770 各应用速查）
  type: menu-path
  source_pages: 全书 How-To 各章
  source_chapter: 各 How-To 实验
  source_quote: |
    "Select nmc > Application Configuration > Application Settings > Accounting > AccountingParameters"
    (p351) ； "Start > All Programs > OmniVista 8770 > Tools > Service Manager" (p142)
  summary: |
    高频路径速查：①Service Manager（NMC Loader 停/启）——Start > All Programs > OmniVista 8770 >
    Tools > Service Manager；②PCS/归档参数——Administration > nmc > OmniVista 8770 > 服务器名 > NmcArchive
    > Accounting；③可见域开关——nmc > Application Configuration > Application Settings > Accounting >
    AccountingParameters；④VoIP 参数——同路径 > Accounting > VoipParameters；⑤移动平均/最大告警——
    同路径 > Accounting > MonitoringParameters；⑥成本计算/总计算/归档/恢复/清除——Account./traf./VoIP
    菜单 Accounting/traffic > Compute cost… / Total calculation… / Archive records… / Restoring
    records… / Purging…；⑦掩码/成本档案/Tracking——Organization 页签 > Masks / Cost Profile / Tracking
    图标；⑧管理员与组——Security > nmc > 8770 administration > Administrators / Groups（Mask data
    access、Accounting experts）；⑨OXE 侧——SIP > SIP Ext Gateway；Translator > 1 > External Numbering
    Plan > 1 > Default DID num. translator；Applications > 1 > Accounting > 1；IP > 1；SNMP Configuration
    > 1 > SNMP Global Configuration；⑩ToolsOmniVista.exe——C:\8770\bin\。
  conditions: 菜单名为 Ed45 英文界面口径；版本升级可能漂移
  tags: [menu-path, quick-reference]

- id: f28
  title: 日志与数据目录地图（排障入口）
  type: structure
  source_pages: 分散各章
  source_chapter: 各 How-To 的 Notes
  source_quote: |
    "C:\8770\log\ NMCSyncLdapPbx_1.log" (p80) ； "Consult the log file: C:\8770\log\NMCLD_1.log file"
    (p114) ； "NMC_RealtimePerformance.log file" (p517)
  summary: |
    目录/文件地图：①同步日志 C:\8770\log\NMCSyncLdapPbx_1.log；②票据加载日志 C:\8770\log\NMCLD_1.log
    （TicketsRead/BadLines/处理速度/被过滤票数）；③成本计算错误 C:\8770\log\NMCLD_CostCalculation_1.log
    与重算错误 NMCCostRecalculation_CostCalculation_1.log（"No first carrier found"）；④Web Performance
    日志 NMC_RealtimePerformance.log；⑤票据落地 C:\8770\data\loader\networknumber=N\subnetworknodenumber=
    NNN\（内含 ACCOUNT.LIS）与收集器 C:\8770\data\collector\；⑥归档 C:\8770_ARC\Accounting\tickets\；
    ⑦OXE 侧 /usr4/account（TAX/IP/SIP DAT 与 LIS）与 /usr4/pmm（pmm/inf 与 pmm.lis）。
  conditions: 路径为默认安装口径；诊断 OID 含义须查技术文档（p512 Notes）
  tags: [structure, logs, directories, troubleshooting]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-23）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | OXE 纳管 | 有 | f04, f27, f28 | 架构协议图 + 路径 + 日志地图 |
| task-02 | SIP 模拟器对接 | 有 | f03 | 模拟器拓扑与号码规则 |
| task-03 | OXE 外部计费开启 | 有 | f08 | 票据文件体系与落盘时机 |
| task-04 | 维护命令核查 | 有 | f08, f28 | 文件体系 + 目录地图 |
| task-05 | 票据回收链路 | 有 | f09, f10, f11 | 回收四步 + 五方法 + 收集器/PCS |
| task-06 | 币种/税/国家 | 有 | f12 | 运营商对象模型（参数细节归数值提取器） |
| task-07 | Telecom 1 建模 | 有 | f12, f13, f14 | 对象模型 + 费率类型学 + 服务费模型 |
| task-08 | 运营商演进 | 有 | f12 | 前缀冲突与方向重建的模型依据 |
| task-09 | Telecom 2 | 有 | f12 | 同一对象模型复用 |
| task-10 | Service 脉冲运营商 | 有 | f13, f14 | 脉冲模式 + SVA 模型 |
| task-11 | Code Book 导出导入 | 有 | f15 | 十文件体系与格式规则 |
| task-12 | 组织树搭建 | 有 | f16 | 对象模型与归属规则 |
| task-13 | 历史数据迁移回溯 | 有 | f17 | 四种更新语义图 |
| task-14 | 掩码与解密 | 有 | f18 | 档案结构与继承链 |
| task-15 | 成本档案 | 有 | f19 | 双页签结构 |
| task-16 | 可见域 | 有 | f20 | 决策树 |
| task-17 | 报表生成/导出/定时 | 有 | f21 | Reports 应用结构 |
| task-18 | 报表定制 | 有 | f21 | Querytool/Designer 双页签结构 |
| task-19 | VoIP 性能 | 有 | f22 | IP ticket 体系 |
| task-20 | 流量分析 | 有 | f23 | pmm 文件体系 |
| task-21 | Tracking | 有 | f24 | 原理链与变化率 |
| task-22 | Web Performance | 有 | f25 | 采集与仪表盘结构 |
| task-23 | 归档恢复 | 有 | f26 | 生命周期流程 |

补充说明：
- f01（课程主线）、f02（RLAB）、f05-f07（产品概览）不直接对应 task，属于骨架底座（BOOK_OVERVIEW 骨架 1-2）。
- 全部 23 项 task 均有框架类条目覆盖；数值口径（费率公式逐格、阈值、清理周期）归 principle.md，分步操作序列归 case.md。
- 生产化边界提示：真实运营商价目、数据库容量与备份、SNMP 凭证治理均在书外（见 BOOK_OVERVIEW 批判节）。
