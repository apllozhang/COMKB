# 反例/限制/边界/易错点候选 — OmniVista 8770 R5.2 计费与性能管理 (8770XTE201EN Ed45)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: 审计与流量分析只支持 OmniPCX Enterprise——OXO/OpenTouch 不在内
  type: limitation
  source_pages: p25, p29, p431
  source_chapter: AUDIT APPLICATION / ACCOUNT .TRAF. VOIP (TRAFFIC ANALYSIS)
  source_quote: |
    p25: "Limits — Only for OmniPCX Enterprise"
    p29: "Limits • Only for OmniPCX Enterprise"
    p431: "Restriction — Only for OmniPCX Enterprise"
  summary: |
    Audit（操作审计）与 Traffic Analysis（流量分析）两套能力有硬性平台限制：仅支持 OmniPCX Enterprise。
    OXO Connect 站点只有计费票据与 VoIP 报告可用，无流量观察计数器、无操作审计。
    给混合网（OXE+OXO）客户做方案时，话务报表与合规审计的承诺要按平台拆开说。
  conditions: 方案设计与承诺
  tags: [limitation, platform, audit, traffic-analysis]

- id: n02
  title: WBM Configuration 应用的四条边界——本地管理员无配置权、无 SSH/Telnet、一次连一台
  type: limitation
  source_pages: p36
  source_chapter: 8770 WBM CONFIGURATION APPLICATION
  source_quote: |
    "No access to Configuration for local admin • No OT and no OXE direct access via SSH/Telnet
    • Networks, subnetworks and nodes managed from the think client"
  summary: |
    WBM（轻客户端）的 Configuration 应用限制：本地管理员无配置入口；不能经 SSH/Telnet 直连 OpenTouch
    与 OXE；网络/子网/节点的管理只能在 thick client 做。WBM 适合看与浅操作，深度配置回厚客户端。
  conditions: WBM 部署与权限规划
  tags: [limitation, wbm, admin]

- id: n03
  title: OXE SIP 话机不能用 Click to Call
  type: limitation
  source_pages: p33
  source_chapter: WEB DIRECTORY CLIENT
  source_quote: |
    "Limits • OXE SIP phones can't use the Click to Call feature"
  summary: |
    Web Directory Client 的点击外呼（自动拨号）对 OXE SIP 话机不可用——该功能面向 TDM 话机形态。
    做目录集成方案时，"点击即拨"的终端范围要事先框定。
  conditions: 目录客户端功能规划
  tags: [limitation, directory, click-to-call]

- id: n04
  title: 未接通的外线呼叫也出票（时长=0）——"没打通怎么也有话单"不是故障
  type: misconception
  source_pages: p67, p86
  source_chapter: External Accounting / Outgoing & incoming calls
  source_quote: |
    "Note: a non-established outgoing or incoming call (duration=0) generates an accounting record" (p67)
    "Don't forget to select the Public Outgoing 0 Units calls." (p86)
  summary: |
    外线方向的呼出/呼入即使未接通（时长 0）也会生成计费票据，这是设计行为；OXE 侧过滤器还有专门的
    "Public Outgoing 0 Units calls" 类别。客户问"为什么没打通也有记录"、或发现票量比通话量多时，
    先解释此机制；不想要这类票在 8770 侧用 Duration>0 加载过滤排除（入不了库≠没发生）。
  conditions: 计费对账与客诉解释
  tags: [misconception, accounting, tickets]

- id: n05
  title: 本机-本机呼叫只有"已建立"才出票——与外线规则相反
  type: limitation
  source_pages: p68
  source_chapter: External Accounting / Local & network calls
  source_quote: |
    "Note: accounting record is only generated for established local-local and local-network call"
  summary: |
    出票规则分平台：外线呼叫未接通也出票（n04），本机-本机（local-local）呼叫只有已建立才出票。
    用票量统计内线话务时，未接通的内线尝试天然缺失——需要完整话务画像应看流量分析（pmm 计数器）。
  conditions: 话务统计口径设计
  tags: [limitation, accounting, traffic-analysis]

- id: n06
  title: OXE 侧 Financial Report 的 PIN/被叫遮蔽要设"不遮"——遮蔽归 8770 管，双重遮蔽无法解
  type: warning
  source_pages: p88, p319
  source_chapter: How-To / External accounting & Mask profiles
  source_quote: |
    "Set this parameter to Not masked because the PIN code is masked by the OmniVista 8770 server. ...
    Set this parameter to 0 because the called number is masked by the OmniVista 8770 Server." (p88)
    "Note the called number 029845----. It means that the called number has been masked by the OXE
    and it cannot be unmasked by the 8770 server." (p319)
  summary: |
    遮蔽职责在 8770：OXE 侧 PIN 设 Not masked、被叫遮蔽位数设 0，否则票面先被 OXE 遮掉一层。而 OXE
    侧一旦遮了（如 Dialed number masked=Yes，显示成一串"--------------"），8770 任何手段（含解密
    报表）都无法还原。发现"8770 里被叫号是横杠"先查 OXE 侧这两个参数，别在 8770 里白折腾。
  conditions: 计费遮蔽体系设计
  tags: [warning, masking, ox e-config]

- id: n07
  title: 空间冗余 OXE 要登记两个主 IP；信任主机表必须含全部相关主机
  type: limitation
  source_pages: p72, p74, p77
  source_chapter: How-To / OXE node registration
  source_quote: |
    "In case of spatial redundancy, note the 2 main IP addresses." (p72)
    "All hosts machines involved with OXE Call Server must be declared." (p74)
    "In case of spatial redundancy, enter the 2 main IP addresses. To perform this operation: ...
    click right and select Add a Value." (p77)
  summary: |
    两条接入期硬要求：(1) 空间冗余（spatial redundancy）的 OXE 有两个主地址——netadmin 查看时两个都
    记下，8770 声明时用 Add a Value 全部填入，只填一个会在冗余切换后断连；(2) OXE 的 iptables 信任
    主机表必须包含所有与 Call Server 交互的主机（8770、OMS、客户端 PC），缺一台就取不到数据。
  conditions: OXE 纳管前置核查
  tags: [limitation, redundancy, trusted-hosts]

- id: n08
  title: FTP 用户名（adfexc）禁改——改了许可校验出问题；密码必须随 OXE 改
  type: warning
  source_pages: p109, p448
  source_chapter: How-To / Accounting records retrieval & Traffic Analysis
  source_quote: |
    "Important: Modify the password to match the OmniPCX Enterprise password if it has been modified.
    Do not modify the FTP user to avoid a problem at verification of the license."
  summary: |
    票据回收的凭证铁律（书内以 Important 标注、两章重复）：FTP 用户名一律保持 adfexc 不动（改动触发
    许可校验故障）；OXE 侧改密后必须同步改 8770 PCX 页签密码，否则回收静默失败。排障"8770 没有新票"
    第一查这里。
  conditions: 票据回收配置与改密流程
  tags: [warning, ftp, licensing]

- id: n46
  title: PCS Ticket Collection 设 No 后不再随日同步——必须手工同步 PCS
  type: limitation
  source_pages: p110
  source_chapter: How-To / Accounting records retrieval / PCS synchronization
  source_quote: |
    "PCS Ticket Collection — Yes (by default). ... No: PCS are not synchronized during the daily
    synchronization. Manager has to synchronize manually the PCS to retrieve the files."
  summary: |
    关闭 PCS 随日同步（Specific 页签 PCS Ticket Collection=No）后，PCS 票据不会自动回收，管理员必须
    手工同步 PCS 才能取到文件。生产中改这个开关前先确认有人负责手工同步。
  conditions: PCS 部署站点
  tags: [limitation, pcs, synchronization]

- id: n09
  title: 组织树搭建顺序：树没建好前别选 Detailed accounting——搬条目在已有记录时极耗时
  type: warning
  source_pages: p101
  source_chapter: ACCOUNTING RECORDS RETRIEVAL / Accounting methods
  source_quote: |
    "Moving Cost center or subscriber into the tree is time-consuming operation when records are
    already stored in the database • When the organization tree is configured, select the detailed
    accounting method to retrieve the records — Goal: construction of the organization tree"
  summary: |
    计费方法的选择顺序是隐含契约：建树期用 "Organization update without records retrieval"（只建树
    不取票），树定型后切 Detailed accounting 开始取票。一旦库里有记录再搬成本中心/分机，每次移动都
    要重算归属，非常慢。项目排期把"组织树定型"放在开闸取票之前。
  conditions: 新站点计费上线排期
  tags: [warning, accounting-methods, ordering]

- id: n10
  title: 币种铁律：参考币种安装时定死不可删；"PCX 给定成本"模式不换汇
  type: limitation
  source_pages: p128, p139, p145
  source_chapter: CURRENCIES / TYPE OF TARIFF
  source_quote: |
    "OmniVista 8770 does not convert. Currency declared in the PCX must therefore be the same as the
    reference currency" (p128)
    "The reference currency can't be deleted. However, the name and the symbol of the reference
    currency can be modified." (p145)
  summary: |
    两条货币边界：(1) 参考币种由安装时所选国家决定，唯一、不可删（只能改名/符号）——装错国家只能
    重装或迁库；(2) "Cost given by the PCX" 资费模式直接采信 PCX 算好的成本，8770 不做币种换算，
    PCX 币种必须与参考币种一致。跨国多币种靠"附加币种+有效期汇率"在资费层解决，不动参考币种。
  conditions: 安装决策与跨国部署
  tags: [limitation, currency]

- id: n11
  title: 同一被叫前缀不能跨区域——加新主叫区前必须先删旧归属
  type: warning
  source_pages: p181, p156
  source_chapter: How-To / Telecom 1 / Evolution
  source_quote: |
    "The prefix 01 must be deleted from National region because it will be used to complete the
    parameters of the calling region Paris region. Without this modification, an error would be
    displayed ... a same prefix cannot be used for different regions." (p181)
    "the accounting application looks for the indicator prefix that matches the best the first digits
    of the called number." (p156)
  summary: |
    演进实验中最容易踩的顺序坑：要把 01 变成巴黎主叫区的前缀，必须先从 National region 删掉它，否则
    配置报错。归属规则是最优（最长）匹配，删除动作本身就是"改归属"的一部分。做运营商演进时按
    "删前缀→建区→补前缀→重建方向→重算"的顺序走。
  conditions: 运营商配置演进
  tags: [warning, prefix, carrier-evolution]

- id: n12
  title: 资费改动不改存量——必须跑 Compute cost（Force）重算，否则新旧成本混存
  type: warning
  source_pages: p178, p215, p225
  source_chapter: How-To / 各运营商章 Notes
  source_quote: |
    "The cost calculation is performed during records loading into database. A cost recalculation is
    required when a carrier configuration change concerns records already stored in the database."
  summary: |
    成本在票据加载时按当时的运营商配置算好并入库；之后改资费/区域/方向，历史记录不会自动变。要矫正
    存量必须显式跑 Accounting/traffic > Compute cost 并勾 Force cost calculation。对账差异排查顺序：
    先看改动后有没有重算，再查配置本身。
  conditions: 资费变更与对账
  tags: [warning, cost-calculation]

- id: n13
  title: "No first carrier found" 两类根因：无匹配运营商；号码落在多运营商同名区域
  type: limitation
  source_pages: p180
  source_chapter: How-To / Telecom 1 / Log files
  source_quote: |
    "Error: No first carrier found: ... Called number: 00140595989584 ... -->the 8770 server didn't
    find a carrier corresponding to the called number. ... Called number: 118008 ... The called
    number 118008 is defined in several called regions that belong to different carriers. The server
    cannot choose a carrier so the cost is not calculated."
  summary: |
    成本日志（NMCLD_CostCalculation_1.log / NMCCostRecalculation_CostCalculation_1.log）的典型错误
    "No first carrier found" 有两种根因：①被叫号匹配不到任何运营商的被叫区（漏配前缀，如国际号）；
    ②同一号码（如特服 118008）定义在多个运营商的被叫区里，服务器无法抉择而放弃计价。修法：补前缀
    或消除跨运营商的重复前缀。
  conditions: 成本排障
  tags: [limitation, logs, troubleshooting]

- id: n14
  title: 服务资费必须配"双资费"并在方向上成对绑定
  type: warning
  source_pages: p162-163, p173
  source_chapter: How-To / Telecom 1 / Tariff & Direction Notes
  source_quote: |
    "When you manage a cost based on a service, you must configure two tariffs. One tariff for the
    communication cost. Another tariff based on the same settings than the previous one for the
    service. — Total tariff of a call is: communication cost + service cost" (p162 Notes)
    "If a service tariff must be applied, you will have to select the one, previously managed." (p173)
  summary: |
    特服/增值业务计价的结构要求：通信资费与服务资费是两个独立对象（参数同源），且服务资费必须在
    Direction 上显式选择（下拉里只有先前建好的服务资费）。只建一个资费就上线，特服号会只算通信费、
    服务费漏收。
  conditions: SVA/特服号计费
  tags: [warning, service-tariff, direction]

- id: n15
  title: Code Book 的 .itl 节点名必须与目标机声明一致——oxe9≠oxe 直接导入失败
  type: warning
  source_pages: p233, p247-248
  source_chapter: CODE BOOK & How-To / Export & import
  source_quote: |
    "Field Node must correspond to the name of the PCX declared in Configuration application ... Node
    name must be configured before importing the code book" (p233)
    "The error linked to Telecom2.itl file is due to bad PCX declaration. The PCX name available on
    Telecom2.itl is called oxe9. The one defined on Configuration application is oxe. Modification on
    Telecom2.itl file must be made before importing Telecom 2 carrier." (p247)
  summary: |
    Code Book 迁移的头号坑：.itl 安装文件里的 Node 字段是**目标机**上声明的 PCX 名。跨服务器导入前先
    用文本编辑器改成目标机实际名字（实验中 oxe9→oxe），否则导入报错且方向建不出来。配套规则：
    (1) 错误 PCX 名时导入"部分成功"更具迷惑性——区域/资费建了，方向没建（p234）；(2) 修改只能在
    Documents 副本上做，不能改 NAS 原件（p246 Warning）。
  conditions: 跨服务器运营商迁移
  tags: [warning, codebook, itl, migration]

- id: n16
  title: 一次导出≠完整备份——完整运营商配置需要第二次导出
  type: limitation
  source_pages: p236
  source_chapter: CODE BOOK / Code book export
  source_quote: |
    "A second export is required to save the complete carrier configuration"
  summary: |
    Code Book 导出分两段：第一次导出后部分信息才就位，需要再导一次才拿到完整配置。做运营商配置
    备份 SOP 时必须写"导出两次"，只导一次的备份不完整。
  conditions: 运营商配置备份
  tags: [limitation, codebook, backup]

- id: n17
  title: EFFECT_DATE 改期再导入=新增周期，不是修改原周期
  type: misconception
  source_pages: p243-244
  source_chapter: How-To / Export & import
  source_quote: |
    "Another period for the direct carrier has been created. From a same carrier, different periods
    can be added. Each period corresponding to a tariff definition which can evaluate according to
    price policy."
  summary: |
    改 .inf 的 EFFECT_DATE 后重新导入，结果是在同一运营商下**新增**一个 Period（原周期自动封口），
    不是覆盖。这正是价目随政策演进的设计用法；但如果意图是"修正原配置"，这个操作会留下两个周期，
    客户看到"配置变多了"别当成事故。
  conditions: 运营商配置维护
  tags: [misconception, codebook, period]

- id: n18
  title: 组织图上移动分机会被拒绝——分机成本中心只能经 OXE 配置或目录应用改
  type: limitation
  source_pages: p285-286
  source_chapter: How-To / Accounting organization
  source_quote: |
    "By default, it's not possible to allocate a cost center to a trunk group from the OXE
    configuration. ... Such move is authorized from the organization map because there is no impact
    on cost center management on the call server." (p285)
    "The move of a subscriber from a cost center to another one is only possible from OXE
    configuration or directory applications. That's why such move is not authorized from the
    organization map." (p286)
  summary: |
    搬移权限二分：中继组等无成本中心对象可以在组织图上自由剪贴（不影响话机侧）；**分机/用户**不行
    ——组织图上剪贴会被拒绝，必须回 OXE 配置（Rights 页签 Cost Center ID）或公司目录改。实验特意让
    学员试一次失败（31011 搬移 failed）来固化这条边界。
  conditions: 组织维护分工
  tags: [limitation, organization, permissions]

- id: n19
  title: 剪贴与复制语义不同：复制产生"灰色历史"且原件转 inactive；剪贴才是纯移动
  type: limitation
  source_pages: p261-262, p287-288, p284
  source_chapter: ACCOUNTING ORGANIZATION & How-To
  source_quote: |
    "Cut & paste • This operation consists in moving an entry without history ... Copy & paste •
    This operation consists in moving an entry with history" (p261-262)
    "The copied item keeps its accounting records and performance counters and becomes inactive.
    The pasted item is active." (p287)
    "This previous status is symbolized by a grey entry. The purpose of this grey entry is to provide
    an history trace of all moves" (p284)
  summary: |
    组织图操作语义表：Cut & paste=不带历史移动；Copy & paste=带历史另立（原件保留记录并转 inactive、
    显示为灰色条目，粘贴件为 active）。灰色条目是历史追溯机制不是垃圾数据——ToolsOmniVista 全局更新
    前它们承担记录归属；客户问"树上怎么有重名灰条"先讲语义再动手清理。
  conditions: 组织树日常维护
  tags: [limitation, organization, cut-copy]

- id: n20
  title: 回溯历史必须选"设备"而非"用户"；level/成本中心/人不可回溯；残留成本中心要手工删
  type: warning
  source_pages: p263, p290, p295
  source_chapter: ACCOUNTING ORGANIZATION & How-To
  source_quote: |
    "TO ASSIGN CORRECTLY THE HISTORY FROM AN INACTIVE SUBCRIBER TO THE ACTIVE ONE, YOU MUST SELECT ITS
    DEVICE AND NOT THE USER." (p290 Warning)
    "Levels, cost centers and persons can not be backdated" (p263)
    "Levels, cost centers and persons cannot be backdated. That's why the inactive cost center
    Training must be deleted manually." (p295)
  summary: |
    三条回溯边界：(1) Assign earlier creation date 只对"设备（device）"生效，选"用户（user）"挂不上
    历史——书内全大写 Warning；(2) level、成本中心、person 三类对象不可回溯，工具清不掉它们的历史
    影子，残留的非活动成本中心要手工删除；(3) 回溯会删除非活动数据（有告警确认），动手前先归档。
  conditions: 人员变动后的历史迁移
  tags: [warning, backdating]

- id: n21
  title: ToolsOmniVista 组织更新是"破坏性"操作：强制停服务、删除全部非活动实体
  type: warning
  source_pages: p293
  source_chapter: How-To / Accounting organization / Complete organization tree update
  source_quote: |
    "Enter 'y' to stop the 8770 services (mandatory) ... All entities with historical data into the
    organization Will be deleted from the database. Their tickets and Ptp counters will be reassigned
    to the active entities! Do you want to continue (y/n) ? y"
  summary: |
    Accounting Organization Update（ToolsOmniVista.exe 菜单 3）执行时：强制停止全部 8770 服务（业务
    中断）；删除所有带历史的非活动实体并把票据与 Ptp 计数器重挂到活动实体——不可逆。它不是"日常
    维护"，是变更窗口里的重活：先归档、再停机、后执行，并预期大量灰色条目消失。
  conditions: 组织全局重挂
  tags: [warning, toolsomnivista, destructive]

- id: n22
  title: Default 掩码档案不可改名删除——停用靠把遮蔽位数清 0
  type: limitation
  source_pages: p300, p306
  source_chapter: MASK PROFILES
  source_quote: |
    "Default profile cannot be renamed or deleted • However, you can reset masked digit to 0 to
    render it inactive" (p300)
    "The displayed number has priority over the masked one." (p306)
  summary: |
    掩码档案两条边界：(1) Default 档案挂组织根，不可改名/删除——想"取消默认遮蔽"只能把它的遮蔽位数
    改成 0；(2) 显示位数优先于遮蔽位数，"显示前 4 位"的语义是至少显示 4 位（号码只有 4 位就全显），
    排障时别误判成"遮蔽失效"。
  conditions: 掩码策略设计
  tags: [limitation, mask]

- id: n23
  title: grouped report 无视组织树上的掩码档案——只认 Default 档案的两个 group 类别
  type: limitation
  source_pages: p310, p318
  source_chapter: How-To / Mask profiles
  source_quote: |
    "In case of grouped report, the server ignores the mask profiles applied to the organization: it
    only takes into account the profile named Default (see masked group and unmasked group call
    categories in the profile Default))" (p310)
    "The unmasking is done according to the configuration of the Default mask profile" (p318)
  summary: |
    给 TSS 等成本中心单独配的掩码档案只影响详细报表与记录查看；grouped（汇总）报表一律按 Default
    档案的 Masked group / Unmasked group 类别处理。合规评审时如果只测了详细报表，会漏掉汇总报表的
    遮蔽口径——两型报表都要纳入验证。
  conditions: 合规验收
  tags: [limitation, mask, reports]

- id: n24
  title: 解密三门槛：默认禁止、须"Mask data access"组成员口令、改组要先关 Reports 应用
  type: warning
  source_pages: p314, p316
  source_chapter: How-To / Mask profiles / Unmasking
  source_quote: |
    "BY DEFAULT, THE GENERATION OF A REPORT WITHOUT MASK IS NOT ALLOWED. TO USE UNMASKING OPERATION,
    IT IS NECESSARY TO CREATE AN 8770 LOGIN WHICH IS MEMBER OF THE GROUP 'MASK DATA ACCESS'. THE
    PASSWORD OF THIS LOGIN IS ASKED WHEN A USER GENERATES A REPORT WITHOUT MASK." (p314)
    "TO MAKE THE UNMASKING CONFIGURATION ENABLED, REPORTS APPLICATION HAS TO BE CLOSED." (p316)
  summary: |
    解密功能默认关闭。启用三步：建 8770 账号→加入 Mask data access 组→**关闭并重开 Reports 应用**
    （组变更不关应用不生效）。日常使用时任何用户点"Generate report w/o mask"都要输该组成员口令；
    解密程度仍受各档案 Unmasked 类别限制（如 Default 档案解密后仍遮 2 位）。口令治理（谁持有、定期
    轮换）书内不论，交付要自行约定。
  conditions: 解密权限管理
  tags: [warning, unmasking, security]

- id: n25
  title: 月订阅当月加入次月才计费；订阅计算永不处理当天；重算订阅=删了重建、可能跑好几天
  type: limitation
  source_pages: p327, p339
  source_chapter: COST PROFILES & How-To
  source_quote: |
    "With a monthly subscription, users arriving in the current month will only be charged from the
    first of the following month ... Subscription cost calculation never processes the current day"
    (p327)
    "Subscription recalculation is based on deletion of subscription records followed by a new
    addition of subscription records. Processing time may be long, depending on the number of records
    involved." (p339)
  summary: |
    订阅费三条业务口径：(1) 月订阅当月中途加入，从次月 1 日起计——当月不摊分；(2) 订阅成本计算永不
    处理"今天"（要等出票后）；(3) 改订阅档案后的重算机制是"先删订阅记录再重建"，量大时耗时以天计。
    财务对账与离职/入职计费争议都挂在第一条上，售前要提前讲清。
  conditions: 订阅计费与对账
  tags: [limitation, subscription]

- id: n26
  title: 可见域启用顺序坑：开启后未配域=整树只剩根；必须重启计费应用；群组域无效
  type: warning
  source_pages: p351, p353, p355
  source_chapter: How-To / Accounting domains
  source_quote: |
    "A warning indicates that no domain has been managed in the organization: only the organization
    root is visible." (p351)
    "Visibility domains can also be defined for a group. Even if there is such possibility, it is not
    taken into account." (p355)
  summary: |
    启用可见域的三个坑：(1) 开关打开的瞬间，任何没配域的管理员（含 AdminNmc 未配根域时）只见一个
    光杆根节点——看似"数据全丢了"，实为设计顺序问题；(2) 开关变更后必须重启计费应用才生效；(3)
    群组上配域是"摆设"，服务器只认用户级域配置。上线动作序列：开开关→配根域→给 AdminNmc 配域→
    重启→再配子域与各管理员。
  conditions: 多管理员环境上线
  tags: [warning, domains]

- id: n27
  title: 报表有尺寸上限：TXT 400 行、PDF/HTML/EXCEL 50 页、库扫描 100000 行——超限静默截断（有尾注）
  type: limitation
  source_pages: p367
  source_chapter: How-To / Reports application
  source_quote: |
    "If the report is longer than (n) lines or (n) pages, a message indicating that the report is
    truncated is displayed at the end of the report"
  summary: |
    六项默认上限（TXT 400 行 / HTML·PDF·EXCEL 各 50 页 / X 轴 100 元素 / 数据库 100000 行）会把大报表
    截断，截断提示只在报表末尾。给管理层交付"全量"报表前先核尺寸，必要时收窄过滤区间或改用 Total
    counters 数据源（生成更快）。
  conditions: 报表交付
  tags: [limitation, reports]

- id: n28
  title: 累计报表为空=夜间计数器没算——先手工 Total calculation 再生成
  type: limitation
  source_pages: p380-381
  source_chapter: How-To / Reports application / Cumulative report
  source_quote: |
    "If the report instance is empty, it means that the cumulative counters have not yet been
    calculated. If it is the case, perform a manual cumulative counters calculation and generate a new
    instance of the report."
  summary: |
    Daily Station Traffic 这类累计报表依赖 8770 夜间算好的累计计数器；新装、刚同步或刚装的站点首次
    生成会是空表——这不是故障，先到 Account./traf./VoIP > Accounting/traffic > Total calculation 手工
    补算再重新生成。验收排期把"首日出报表"改为"次日或手工补算后"。
  conditions: 报表验收
  tags: [limitation, reports, counters]

- id: n29
  title: 邮件服务器格式细节：冒号与端口间不能有空格；发件人必须是服务器认识 的地址
  type: warning
  source_pages: p374
  source_chapter: How-To / Reports application / Mail server
  source_quote: |
    "The number of the SMTP port is optional if the default SMTP port number is used (default SMTP
    port = 25). Careful: no space between ':' and the TCP port number. ... Indicate a mail address
    known by the mail server"
  summary: |
    邮件配置三个易错点：(1) server:port 写法中冒号后紧跟端口，不能有空格；(2) 端口 25 可省略；
    (3) Name of the mail sender 必须填邮件服务器认识的地址（默认 OmniVista），否则投递被拒。报表
    邮件与 Tracking 告警邮件共用这套参数——配错一处两条通知链一起哑。
  conditions: 邮件通知配置
  tags: [warning, mail, smtp]

- id: n30
  title: 详细 vs 汇总报表语义：同数据 25 次呼叫，Detailed 出 25 行、Grouped 出 1 行
  type: misconception
  source_pages: p385, p390
  source_chapter: How-To / Report customization
  source_quote: |
    "if a set has dialed the same number twenty-five times, the detailed report lists the set
    twenty-five times and indicates the same called number. ­ Grouped: ... the grouped report lists
    it only once" (p385)
    "If the customized report is a detailed one, operation field will be in blank." (p390)
  summary: |
    建定义时 Type 选错，报表"行数不对"的工单就来了：Detailed=逐条不汇总（Operation 字段空置）；
    Grouped=按字段聚合（Operation 才生效）。Hit-list 限量只在 grouped 上有效。客户要"按号码去重的
    账单"是 Grouped，要"逐单审计"是 Detailed——用 25 次呼叫的例子跟客户对齐语义最省事。
  conditions: 报表需求澄清
  tags: [misconception, reports]

- id: n31
  title: 图表/公式不能跨区域取数——嵌套汇总必须切 View；中间层合计不想显示只能前景空白遮蔽
  type: limitation
  source_pages: p396-398, p617, p639-641
  source_chapter: How-To / Report customization & report #4 #5
  source_quote: |
    "It is impossible to use headers from different areas to generate a graph or a formula." (p396)
    "the use of the total cost per called region is necessary ... But the total cost per called
    region information is useless. So the only possibility it's to mask it on the report — On
    Foreground field, select the blank color" (p617)
  summary: |
    Designer 的三条硬边界：(1) 图表与公式的数据必须来自同一视图区域——"成本中心合计=分机合计之和"
    要在 Cost Center 区把 View 切到 Extension 才能引用；(2) grouped 报表做运营商总计必须经过被叫区
    小计这个中间层，而中间层不想显示的唯一办法是把该字段前景色设为空白（不是删除）；(3) grouped 报表
    末页多余的空 Detail 表头，靠加共有字段（Country）做组头再前景空白遮蔽来消除。三条都是"看起来
    该有功能，实际靠技巧"的典型。
  conditions: 复杂报表定制
  tags: [limitation, designer, layout]

- id: n32
  title: VoIP 报告空表的高频根因：呼叫没走"跨 POD 出局"路径（同机软话机互打无效）
  type: warning
  source_pages: p423, p428
  source_chapter: How-To / VoIP Performance
  source_quote: |
    "All calls must be external outgoing calls from one pod to another. Use the command 'account
    compress' if needed." (p423)
    "If the source and destination of external calls are in the same computer (Windows 10 instance),
    using IPDSP and MicroSIP softphones, no VoIP traffic calls can be retrieved in the generated
    report." (p428)
  summary: |
    实验口径（生产类推：话务须走被监控的 IP 承载段）：同一台电脑里 IPDSP 与 MicroSIP 互打虽有话务，
    但生成不了带质量数据的 VoIP 报告。排障顺序：先确认呼叫路径（是否跨节点/出局），再查 IP tickets
    开关、加载过滤与文件回收，最后才看报告过滤器（This Week/System/Sender IP/Board not empty）。
  conditions: VoIP 质量报告取数
  tags: [warning, voip, lab]

- id: n33
  title: 两套等待阈值互不相干：话务台阈值只在 OXE 侧改；8770 的 T1/T2 只喂报表字段
  type: limitation
  source_pages: p443, p445
  source_chapter: How-To / Traffic Analysis
  source_quote: |
    "On initialization, the threshold values are: Threshold 1: 30 seconds, Threshold 2: 60 seconds." (p443)
    "T1 and T2 are waiting thresholds for incoming external calls (calling trunks). These thresholds
    are not related to the waiting thresholds for attendants, that can only be modified via OmniPCX
    Enterprise configuration" (p445)
  summary: |
    容易混为一谈的两组阈值：话务台等待阈值（Attendant threshold 1/2，出厂 30s/60s）只能经 OXE 配置
    （Applications > Traffic Observation）修改；8770 侧 Loading > Traffic analysis 里的订户阈值 T1/T2
    （默认也是 30s/60s）与之无联动，只用于生成话务报表的特定字段。调"话务台超时考核"改前者，调
    "报表口径"改后者。
  conditions: 话务考核口径
  tags: [limitation, traffic-analysis, thresholds]

- id: n34
  title: 流量分析默认只算话务台/话务台组/中继组——被叫号与终端计数器要改 Scheduler 任务的 PtpType
  type: version-trap
  source_pages: p446-447
  source_chapter: How-To / Traffic Analysis / Updating the daily and weekly jobs
  source_quote: |
    "The task Traffic performance cumulative counters calculation of the daily and weekly jobs only
    concerns the Attendant, the Attendant group and the Trunk groups (default observed objects) ...
    Replace -PtpType ATT,ATG,TRG –PTP by -PtpType ALL -PTP"
  summary: |
    装完流量分析就等"被叫号/终端话务报表"，结果只有中继与话务台数据——因为 Daily Job 与 Weekly Job
    里计数器计算任务的命令行默认是 -PtpType ATT,ATG,TRG -PTP。要看全量对象必须手工把**两个任务**都
    改成 -PtpType ALL -PTP。这是出厂默认与预期能力的差距，属于部署清单必查项而非故障。
  conditions: 流量分析部署
  tags: [version-trap, scheduler, ptp]

- id: n35
  title: Tracking 默认档案只作用于勾了 Default Tracking 的实体——Reset Profile 才是全量强制
  type: limitation
  source_pages: p478, p464
  source_chapter: How-To / Tracking application
  source_quote: |
    "The profile applies only to entities using the default profile (Default Tracking box selected).
    If you want to force assignment to all entities, select the corresponding Reset Profile option
    The Default Tracking box of each entity is then forced to YES" (p478)
    "Manual assignment — To force assignment to all entities, select the corresponding Reset Profile
    option." (p464)
  summary: |
    在 Default Tracking 管理器里把档案挂到某实体类型后，只有当时已勾选 Default Tracking 的实体生效；
    历史上被单独指定过档案（取消过 Default Tracking）的实体不在覆盖范围。要"一个档案管全部"必须点
    Reset Profile 强制把该类型的 Default Tracking 全部置回 YES。以为"配了类型=全员生效"会导致漏监控。
  conditions: Tracking 覆盖面核查
  tags: [limitation, tracking]

- id: n36
  title: Web Performance 数据源限制：Hybrid link/直连/远端中继组不支持；仅 ISDN、SIP、NDDI、ABC-F
  type: limitation
  source_pages: p493
  source_chapter: WEB PERFORMANCE APPLICATION / Data collection
  source_quote: |
    "Restrictions • Hybrid link, direct link and remote trunk groups not supported • Only ISDN
    (T0,T1, T2), SIP , NDDI and ABC-F"
  summary: |
    Web Performance 的中继类 widget 覆盖面有限：混合链路、直连链路、远端中继组不在支持列表；承载类型
    仅 ISDN（T0/T1/T2）、SIP、NDDI、ABC-F。其他中继形态（如某些专线上）仪表盘无数据——售前演示前按
    客户中继类型核对，避免现场"空白 widget"。
  conditions: Web Performance 部署范围评估
  tags: [limitation, web-performance]

- id: n37
  title: raw data 显示仅限"最后一天"；widget 单参数最多选 6 个元素
  type: limitation
  source_pages: p499, p503
  source_chapter: WEB PERFORMANCE APPLICATION / Dashboard tricks
  source_quote: |
    "Detailed display option available only if selected period is last day" (p499)
    "A maximum of 6 elements can be selected — For trunks, disk, IP domains and entities" (p503)
  summary: |
    两条仪表盘边界：(1) 原始数据（逐轮询粒度）只能在周期=最后一天时打开，更早的历史只有半小时聚合值；
    (2) 同一 widget 的同一参数最多勾 6 个元素（中继/磁盘/IP 域/实体），大站点要拆多个 widget 分屏看。
  conditions: 仪表盘使用
  tags: [limitation, dashboard]

- id: n38
  title: SNMP 配置不一致的后果：8770 出告警并自动停用性能监控
  type: warning
  source_pages: p511
  source_chapter: How-To / Web Performance application
  source_quote: |
    "These identifiers are arbitrary and do not affect the server's function, but they can be useful
    to have. ... The 8770 Performance monitoring process is aimed at checking the consistency of the
    8770 values (protocol and community, V3 user) with those configured in OXE. It checks the agent
    as well is enabled. In case of misconfiguration the 8770 raise an alarm and disable the SNMP
    monitoring."
  summary: |
    8770 会周期性校验双侧 SNMP 配置一致性（协议/community/V3 用户）与代理启用状态；发现不一致时不是
    重试而是**出告警并停用 SNMP 监控**——OXE 侧改了 V3 用户/口令而 8770 没跟改，仪表盘会整体断粮且
    需人工重新启用。双侧变更要当成同一次变更窗口的两步做。
  conditions: SNMP 变更管理
  tags: [warning, snmp, change-management]

- id: n39
  title: 归档两个参数单位规则相反：Archive Delay 不带 D、Clean-up delay 必须带 D；按记录日期清理
  type: warning
  source_pages: p529-530
  source_chapter: How-To / Accounting Records Archiving
  source_quote: |
    "Archive Delay — Defined in days (default value: 31) – Don't add the symbol D after the value.
    ... Clean-up delay — Defined in days (default value: 94D) – The symbol D must be added after the
    value. ... This deletion is performed according to the date of the records and not to the creation
    date of archive files."
  summary: |
    同一页签里两个天数参数书写规则相反：Archive Delay=31（禁止带 D），Clean-up delay=94D（必须带 D）
    ——照抄格式会配错。清理时机按**记录的业务日期**而非归档文件创建日期计算，即补归档的旧票也会按
    原日期到期删除。合规留存期限要按"记录日期+31+94 天"推算，不是按归档动作时间。
  conditions: 归档参数配置与合规留存
  tags: [warning, archiving]

- id: n40
  title: 恢复标签 Loaded records 无法与原始数据区分——审计场景必须用 Archived records
  type: limitation
  source_pages: p537, p543, p548
  source_chapter: How-To / Accounting Records Archiving / Restoring
  source_quote: |
    "Loaded records: Without label (visible in the organization). Archived records: with label (the
    restored records are not visible in the organization)." (p537)
    "There is no way to make a difference between the already loaded records and the ones just
    restored from archives." (p543)
    "Record origin = Loaded record if ... comes from a PCX or if ... restored with the label Loaded
    record — Record origin = Restored record if ... restored with the label Archived records ... Only
    restored records ... only deletes records restored with the label Archived records." (p548)
  summary: |
    恢复票据的标签二选一影响后续一切操作：Loaded records 打回组织树后与原始票完全无法区分（对账/审计
    会混淆"库里的票是原始的还是恢复的"）；Archived records 打标、组织树不显示但报告可见、Record origin
    列可过滤、且可被"Only restored records"单独清除。涉及审计追溯的场景一律用 Archived 标签。另注意
    恢复选 With recalculation 时运营商有效期必须覆盖被恢复记录的日期，否则算不出成本。
  conditions: 归档恢复与审计
  tags: [limitation, restore, audit]

- id: n41
  title: 书内笔误一：报表练习汇率两处不一致（1€=1.21$ vs 1.3$）
  type: warning
  source_pages: p402, p550, p557
  source_chapter: Report customization 练习题面 vs 实现章
  source_quote: |
    p402: "The column Cost w/o Tax Dollar gives the cost in Dollar (1 €= 1,21 dollar)."
    p550: "The column Cost w/o Tax Dollar gives the cost in Dollar (1 €= 1,3 dollar)."
    p557: "$cost = € cost*1.3"
  summary: |
    同一个 report #1 练习，题面章（p402）写 1€=1.21$，实现章（p550/p557）用 1.3。教材自身未修订。
    照抄实验值不影响学操作，但做"对照题面验收"时会判不一致——以实现章口径或交付约定为准。
  conditions: 使用本教材做练习/验收
  tags: [warning, book-defect, reports]

- id: n42
  title: 书内笔误二：report #4 题面出现 "Telecom 7 / Telecom 0"，实现与过滤器实为 Telecom 1/2
  type: warning
  source_pages: p607, p613
  source_chapter: Report customization – report #4
  source_quote: |
    p607: "Only outgoing calls linked to Telecom 1 or Telecom 7 must be displayed. ... Total cost by
    carrier — Telecom 0 — Telecom 7"
    p613: "Only outgoing calls linked to Telecom 1 and Telecom 2 must be displayed in the report ...
    Telecom 1 ... Telecom 2"
  summary: |
    report #4 题面把运营商名写成 Telecom 7/Telecom 0（排版残留），实现章步骤与 Filter Editor 截图均为
    Telecom 1 与 Telecom 2。按题面照抄会找不到运营商——以实现章为准。
  conditions: 使用本教材做练习/验收
  tags: [warning, book-defect, reports]

- id: n43
  title: 书内笔误三：成本中心用户姓名字段颠倒（Alice Adams 建号步骤）
  type: warning
  source_pages: p89, p91
  source_chapter: How-To / External accounting
  source_quote: |
    p91: "Creation of user Alice Adams — Directory Number: (i.e. 31011) — Directory Name: Enter the
    directory first name (i.e. Alice) — Directory First Name: Enter the directory first name (i.e.
    Adams)"
  summary: |
    建 31011 用户的两张字段说明表把 Name/First Name 的示例值写反（Name 填了 Alice、First Name 填了
    Adams；p89 分配表也写作 "31011 Adams Alice"），而 31010（Ava Adore）是正确的。字段语义本身清楚
    （Name=姓、First Name=名），照抄会得到姓名颠倒的目录条目。
  conditions: 使用本教材做练习
  tags: [warning, book-defect, ox e-config]

- id: n44
  title: 书内文字残留：Telecom 2 的 Brest→Brest 方向说明写作 "Local region"
  type: warning
  source_pages: p210
  source_chapter: Direct carrier configuration - Telecom 2 / Local direction
  source_quote: |
    "Direction from Brest region to Brest region — Calling region: Select a calling region if
    necessary (i.e. Brest re). — Called region: Select a called region if necessary (i.e. Local
    region)."
  summary: |
    Telecom 2 章该方向的字段说明残留 Telecom 1 的 "Local region"（Telecom 2 并没有建 Local region，
    其本地被叫是 Brest region 自身兼被叫），主叫区还写作 "Brest re"（截断）。按 Telecom 2 实际区域
    结构（Brest 双栖区）配置即可。
  conditions: 使用本教材做练习
  tags: [warning, book-defect, carrier]

- id: n45
  title: 真实运营商价目、数据库容量/备份、SNMP 凭证治理、话务留存合规全部在书外
  type: out-of-scope
  source_pages: 全书（尤其 p115-225、p520、p510-513）
  source_chapter: 全书口径
  source_quote: |
    "The carrier configuration allows calculating the cost of records retrieved from the PCX" (p117，
    只教配置不教价目来源)
    "Backup of OmniVista 8770 databases ... Backup stored on a network drive" (p15，一句带过)
  summary: |
    四块生产化缺口教材只有指针或缺失：①真实运营商价目数据的获取与维护（书内全用教学数值）；②MariaDB
    容量规划、备份与恢复演练（Maintenance 应用一句话）；③SNMPv3/系统口令的生产治理（书内明文密码为
    实验口径）；④话务数据的法定留存期限与合规（书内 125 天是机制上限不是合规结论）。落地交付须以
    8770 安装文档、客户安全基线、当地法规补齐。
  conditions: 生产交付
  tags: [out-of-scope, production]
```

---

## 收尾自检 — 对照 BOOK_OVERVIEW.md 23 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | OXE 纳管 | 有 → n07（冗余双 IP/信任主机） |
| task-02 | SIP 模拟器对接 | 无独立边界（环境预配前提，实验口径已标注） |
| task-03 | OXE 外部计费开启 | 有 → n04（0 计费票）、n05（内线规则）、n06（OXE 遮蔽）、n43（姓名笔误） |
| task-04 | 维护命令核查 | 有 → n04/n05 同源（票据量差异的解释入口） |
| task-05 | 票据回收链路 | 有 → n08（FTP 铁律）、n46（PCS 手工同步）、n09（方法顺序） |
| task-06 | 币种/税/国家 | 有 → n10（参考币种不可删/不换汇） |
| task-07 | Telecom 1 建模 | 有 → n12（重算）、n13（日志根因）、n14（双资费） |
| task-08 | 运营商演进 | 有 → n11（前缀跨区）、n12 |
| task-09 | Telecom 2 | 有 → n44（文字残留） |
| task-10 | Service 脉冲运营商 | 有 → n14（双资费） |
| task-11 | Code Book | 有 → n15（.itl）、n16（二次导出）、n17（EFFECT_DATE 语义） |
| task-12 | 组织树搭建 | 有 → n18（搬移权限）、n19（剪贴/复制语义） |
| task-13 | 历史数据迁移 | 有 → n20（回溯边界）、n21（工具破坏性） |
| task-14 | 掩码与解密 | 有 → n06、n22、n23、n24 |
| task-15 | 成本档案 | 有 → n25（订阅口径） |
| task-16 | 可见域 | 有 → n26（启用顺序坑） |
| task-17 | 报表生成/导出/定时 | 有 → n27（尺寸）、n28（累计报表空表）、n29（邮件格式） |
| task-18 | 报表定制 | 有 → n30（Detailed/Grouped）、n31（版面边界）、n41/n42（笔误） |
| task-19 | VoIP 性能 | 有 → n32（同机互打无效） |
| task-20 | 流量分析 | 有 → n01（仅 OXE）、n33（双阈值）、n34（PtpType） |
| task-21 | Tracking | 有 → n35（覆盖面） |
| task-22 | Web Performance | 有 → n36（数据源限制）、n37（raw/6 元素）、n38（SNMP 停用） |
| task-23 | 归档恢复 | 有 → n39（参数格式）、n40（标签语义） |

**23/23 中 22 项有边界类条目覆盖（task-02 无独立边界，其实验前提已在 c02 conditions 标注）。**

### 扫描完整性说明（Warning/Note/Tips/Limits/Important 标记框逐页核对）

- 全大写 Warning 框 4 处已全部入册：p246（NAS 副本修改，入 n15）、p290（选设备不选用户，入 n20）、p314（解密默认禁止，入 n24）、p316（关 Reports 应用，入 n24）。
- Important 框 2 处已入册：p109/p448（FTP 用户名禁改，入 n08）。
- Limits/Restrictions 区块已入册：p25/p29/p431（仅 OXE，n01）、p33（Click to Call，n03）、p36（WBM 四条，n02）、p24（Topology 仅相关告警——纯功能描述未入册）、p493（Web 数据源，n36）。
- 已吸收为 principle 的 Note 类（不重复入册）：p86 存储天数、p93 同步落盘、p156 前缀匹配、p171 分段示例、p178 重算、p183 巴黎双栖、p244 周期语义（边界视角另入 n17）、p284 灰条目、p327 订阅口径、p353 域继承、p367 截断、p422 BFI、p446 PtpType、p464 Reset、p511 SNMP 校验、p529 归档参数、p543 无差别说明、p548 Record origin。
- 复核后排除的纯操作提示（非边界类）：p55 公网号码格式说明、p56 呼叫变换示例、p116 资费对象总览、p139 币种机制陈述、p226-232 Code Book 格式描述、p253-257 组织模型陈述、p457-461 Tracking 原理图、p492 数据源描述、p512 OID 查文档提示（"refer to the technical documentation"，已并入 n45 生产缺口）、p517 Wireshark/rstcpl 排障演示（实验性，无生产边界含义）、p644-650 培训评估。
- 推断性结论标注"（推断）"的位置：本文件无推断性条目——全部条目均直接引自原文 Warning/Note/Limits 或书内客观矛盾；n32 的生产类推一句已用"（生产类推）"字样显式标示。
- 书内缺陷单独成条：n41（汇率 1.21/1.3）、n42（Telecom 7/0）、n43（姓名颠倒）、n44（Local region 残留）——供下游引用时避开。
- 版本号保留完整位数：R5.0 GA、R5.0 MD1、T0/T1/T2、R101.1（实验机，n45 未复述但见 principle p02）。
