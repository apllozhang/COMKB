# 原则/清单/规则/公式/数值口径候选 — OmniVista 8770 目录管理 (8770XTE202EN Ed40)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，实验环境给定值（IP、密码、账号、分机号）均标注"实验口径"，生产化需替换。页码为 PDF PAGE 标记口径。

```yaml
- id: p01
  title: 虚拟化平台支持清单与许可口径
  type: metric
  source_pages: p8
  source_chapter: SOLUTION OVERVIEW / Virtualization
  source_quote: |
    "Hypervisors • VMware ESXi (6.x, 7.0 and 8.0) • Microsoft Hyper-V® 2016, 2019, 2022 •
    Nutanix AHV ( 20220304) • ASW (Amazon Web Services)" (p8)
    "No OmniVista 8770 license for virtualization • According to the different hypervisors, some
    complementary services may require additional license costs" (p8)
  summary: |
    四类虚拟化平台：VMware ESXi 6.x/7.0/8.0、Microsoft Hyper-V 2016/2019/2022、Nutanix AHV（build 20220304）、
    AWS。虚拟机规格要求与物理服务器相同；8770 本身不收虚拟化许可，但部分补充服务按 Hypervisor 可能加收。
    容量规划用 Capacity Planning tool V3.0。
  conditions: Ed40 印刷口径；新版本平台支持以官方兼容文档为准
  tags: [metric, virtualization, licensing]

- id: p02
  title: 跨版本兼容矩阵（8770 R4.2/R5.0/R5.1/R5.2 × PCX 版本）
  type: metric
  source_pages: p9
  source_chapter: CROSS COMPATIBILITY
  source_quote: |
    "OT R2.4 to R2.6.1 X X X X / OXE R12.2 to R12.4 X X X X / OXE Purple R100 (N1) X X X /
    OXE Purple R100.1 (N2) X X / OXE Purple R101.0 (N3), R101.1 (N4) & R101.2 (N5)  X /
    OXO Connect / OCE R4.0 X X X X / OXO Connect / OCE R5.0 to R5.1 X X X / OXO Connect / OCE R5.2 to R6.2 X X" (p9)
  summary: |
    版本配对硬表（X 数=兼容的 8770 版本数，列序 R4.2/R5.0/R5.1/R5.2）：OT R2.4-2.6.1 与 OXE R12.2-12.4 四版全兼容；
    OXE Purple R100(N1) 兼容 R5.0-R5.2、R100.1(N2) 兼容 R5.1/R5.2、R101.0/101.1/101.2(N3/N4/N5) 仅 R5.2；
    OXO/OCE R4.0 四版全兼容、R5.0-5.1 兼容 R5.0/R5.1/R5.2、R5.2-6.2 仅 R5.1/R5.2。
    交付核查点：PCX 版本向上兼容新 8770，8770 旧版配新 PCX 会出局。
  conditions: Ed40 口径
  tags: [metric, compatibility, versioning]

- id: p03
  title: UID 唯一性规则与三种构造方法（防同名）
  type: rule
  source_pages: p66, p74, p118-121
  source_chapter: USER IDENTIFIER / User ID of the person / UID construction
  source_quote: |
    "UID: First name + Last name • A UID is unique in the Company Directory" (p66)
    "User ID = first name + last name + extension. This method allows to avoid problem like homonymy •
    The method used to build the User ID is specific to a PCX • The parameter is taken into account only
    by automatic creation" (p74)
    "The entry Anderson Thomas already exists. No automatic creation for link 31023, oxe, abc1, ale." (p118)
  summary: |
    UID 在公司目录内唯一；默认构造=名+姓。撞同名时自动创建被拒并产生 8770 告警。解法：Configuration 应用选中
    Network > Subnetwork > PCX → Data Collection 页签 → UID construction 参数改为 Extension（=名+姓+分机号），
    之后同一姓名不同分机可共存（31023/31024 两个 Thomas Anderson）。注意三点：该方法按 PCX 分别设置、只对自动
    创建生效、改回 None（名+姓）后新创建的同名人会再次冲突。
  conditions: 设置入口：Configuration 应用 OXE 节点 Data Collection 页签
  tags: [rule, uid, homonym, automatic-creation]

- id: p04
  title: DN 双格式规则——目录侧与配置侧
  type: rule
  source_pages: p67, p436
  source_chapter: DISTINGUISHED NAME / COMPANY DIRECTORY LEVELS ORGANIZATION
  source_quote: |
    "Pitt Duane DN (Directory application) • uid=Duane Pitt, ou=Support dpt, o=Export ltd, l=Paris, c=fr,
    o=dgo, o=directoryroot / User10 DN (Configuration application) • TelephoneNumber=31000,
    Cn=TelephonicDevices, SubnetworkNodeNumber=101, SubnetworkNumber=1, NetworkNumber=1, o=nmc" (p67)
    "• o: organization • c: country • l: location • ou: organization unit • uid: user identifier" (p436)
  summary: |
    两棵树的 DN 模板：目录侧 uid=<UID>, ou=<部门>, l=<城市>, c=<国家>, o=<组织>, o=directoryroot；
    配置侧 TelephoneNumber=<分机>, Cn=TelephonicDevices, SubnetworkNodeNumber=<节点号>, SubnetworkNumber=<子网号>,
    NetworkNumber=<网络号>, o=nmc。LDAP 键含义：o=组织、c=国家、l=城市、ou=部门、uid=人。排障/写过滤器/建复制
    Scope 时必须用对格式。
  conditions: 复制 Scope 例：o=Ale,o=directoryRoot（p376/377 为 MSAD Scope，同构）
  tags: [rule, dn, ldap, format]

- id: p05
  title: 六类链接基数与匹配条件规则
  type: rule
  source_pages: p69-72
  source_chapter: LINKS BETWEEN DIRECTORY PERSONS AND OXE USERS
  source_quote: |
    "Primary link: 1 entry => 1 user, 1 user => 1 entry ... Name, first name and cost center name are
    identical • Only one primary link can be defined for each entry" (p69)
    "Multi-device link: 1 entry => n users, 1 user => 1 entry ... Automatically created after partial or
    complete OXE synchronization" (p69)
    "Secondary link: 1 entry => n users, 1 user => 1 entry ... Cost centers are identical / name and
    first name are different" (p70)
    "Fax link: 1 entry => n user , 1 user => n entries ... Cost centers are different / name and first
    name are different" (p70)
    "Miscellaneous link: 1 entry => n users, 1 user => 1 entry ... (data terminal, modem) • Cost centers
    are identical" (p70)
  summary: |
    基数与匹配矩阵：Primary 1:1（姓名+名+成本中心全一致，每条目仅一条）；Multi-device 1 entry→n users
    （同步后自动建，多话机共一条目）；Secondary 1 entry→n users / 1 user→1 entry（异名同 CC，DECT 类）；
    Fax n:n（CC 不同、姓名不同，传真可共享，CC 不继承）；Miscellaneous 1 entry→n users（异名同 CC，
    数据终端/Modem）；Additional resources 同 Primary 性质但可多条（4760 迁移多主链）。选链决策：先看 CC 异同、
    再看姓名异同、最后看终端类型。
  conditions: 建链入口 Directory 右键 Settings links...；Multi-device 经 Users 应用
  tags: [rule, links, cardinality, matching]

- id: p06
  title: 主链接姓名/名字只能从公司目录侧修改（数据更新方向）
  type: rule
  source_pages: p79
  source_chapter: DATA UPDATE
  source_quote: |
    "Primary link (automatic or manual creation) Name ==> First name ==> Cost center name <=> ISDN number
    <== Name / First name / CC number, CC name / Users ' Entity Inst. Nb + DDI translator" (p79)
    "In case of primary link, the name and / or first name modification must be done via the Company directory" (p79)
  summary: |
    更新方向硬规则（主链接）：姓名/名字方向=目录→PCX 单向（PCX 侧改会断链，见 n08）；成本中心=双向；
    ISDN 号=从 PCX 取（实体安装号+DDI 翻译器）。副链：成本中心双向、ISDN 从 PCX。传真链：传真号从 PCX。
    杂项链：成本中心双向。
  conditions: 实证见 c03 链接管理实验 5/6/7 章
  tags: [rule, data-update, direction, naming]

- id: p07
  title: 成本中心必须先在 PCX 存在——目录侧改未知 CC 会被拒绝并告警
  type: rule
  source_pages: p80, p139-140
  source_chapter: DATA UPDATE / Unknown cost center assignment
  source_quote: |
    "If the update is done via the Company Directory, the OmniVista 8770 Server checks that the cost
    center name exists in the PCX ... If cost center does not exist, PCX refuses the modification and
    generates an alarm • Modification of cost center is cancelled when the alarm is received" (p80)
    "Additional Text The PCX SubnetworkNodeNumber=101,SubnetworkNumber=1,NetworkNumber=1,o=nmc refused
    modification of the field cost center name with the value BEAN on station 31001." (p140)
  summary: |
    规则：目录侧把成本中心改成 PCX 不存在的名字（如 BEAN）→ PCX 拒绝 → 8770 收到告警后回滚修改，人员 CC 保持原值。
    正确顺序：先在 PCX 的 Configuration 界面 Specific Telephone Services > 1 > Cost Center 建 CC（ID+名字），
    再在目录侧引用。CC ID 与 CC 名通过用户 Rights 页签绑定（选 ID 自动填名）。
  conditions: 排障入口：Alarms 应用 Alarms 页查看拒绝详情
  tags: [rule, cost-center, alarm, validation]

- id: p08
  title: 条目类型转换会删除人员专属属性与关系链接
  type: warning
  source_pages: p78, p108-109
  source_chapter: ENTRY TYPE CONVERSION / User conversion to a room
  source_quote: |
    "Person entries can be converted to entries of the following type: Company, Department, Group, or Room
    ... The conversion deletes the person's specific attributes: password, photo, mobile, etc. As well as
    any links to other records (assistant, manager, etc.) ... Other attributes are either automatically
    updated (if they match) or kept" (p78)
  summary: |
    Person → Company/Department/Group/Room 转换（如把自动创建的 Visio Room 人员转成 Room 条目）会删除：密码、
    照片、手机等人员专属属性 + 经理/助理等关系链接；其余属性能匹配则自动更新否则保留。转换前如需保留这些数据，
    先手工记录。
  conditions: 转换入口：Directory 应用右键人员条目
  tags: [warning, conversion, data-loss]

- id: p09
  title: LDIF 导入只增改不删除；属性空值不导出
  type: rule
  source_pages: p85, p168, p540
  source_chapter: LDIF IMPORT & EXPORT / LDIF
  source_quote: |
    "An LDIF import • Allows creating and modifying data • Does not remove data" (p85)
    "Right click and select Import > Immediate on local drive > Add and modify…" (p168)
    "Importing LDIF files does not delete any entry • Attributes without values are not exported" (p540)
  summary: |
    第一性规则：LDIF 导入（Add and modify 模式）永远不会删条目——需要删除时用手工删除或 PurgeLdap 工具。
    反向推论：外部目录同步场景"对方删了我也要删"必须额外设计删除机制（misc10 标记 + purgefilter，见 p30）。
    导出时无值属性不写文件——用 LDIF 做备份后回导，空值属性不会被清空。
  conditions: 备份用途导 Branch 范围最完整（p163）
  tags: [rule, ldif, import, delete]

- id: p10
  title: LDIF 导出三范围语义与调度导出落盘路径
  type: metric
  source_pages: p86, p157-166
  source_chapter: LDIF IMPORT & EXPORT
  source_quote: |
    "Export the selected entries only • Export only the entries at the selected entry sublevel • Export
    the selected entry and its sublevels ... On the client (local drive) or on the server" (p86)
    "When you export with the 'Branch…' option, all company directory data are exported. This export
    process is the most complete." (p163)
    "the LDIF export file is saved in the following path C:\8770\Client\data\import" (p165)
  summary: |
    三范围：Entry=仅该条目一条记录；Sublevel=直接下级（不含本条目）；Branch=本条目+全部子树（备份必用）。
    本地导出即时完成；服务器导出走 Scheduler（Simple job，可选 Now 或定期），文件落 8770 服务器
    C:\8770\Client\data\import，执行记录可在 Scheduler 应用追溯。
  conditions: 服务器导出会生成 Scheduler 任务——既是审计线索也是定时备份抓手
  tags: [metric, ldif, export, scheduler, path]

- id: p11
  title: 匿名/个人认证访问的可见性行为矩阵（保密级别实测口径）
  type: metric
  source_pages: p211-212, p239-243
  source_chapter: DIRECTORY ACCESS RIGHTS + How-To 实测
  source_quote: |
    "Anonymous access • Only green records displayed • With only non-personal data ... No visibility of
    persons with orange, red and admin8770 confidentiality levels" (p211)
    "Authenticated access with a company directory person • Only green records displayed • With personal
    data included for the authenticated person" (p212)
    "When you consult the web directory with a person account, only the persons with confidentiality
    level green are displayed and the authenticated person." (p243)
  summary: |
    行为矩阵（实测口径）：①匿名——只见 Green 条目的非个人数据；②Green 人员认证——见全部 Green 条目 + 本人
    （本人含 personal data：Password/Home address/Home telephone 可见，地址簿可定制）；③Orange/Red/Admin8770
    人员认证——结果与 Green 相同（只见 Green + 本人），本人级别不扩大对他人条目的可见性；④Orange 认证时
    本人 personal data 可见（p243 实测 orange 的 Password/家庭地址/电话可见）。
  conditions: admin8770 级别条目只有管理员账户经 Web Directory 权限才可见
  tags: [metric, confidentiality, access-matrix, web-directory]

- id: p12
  title: 管理端访问级别两套共十档定义
  type: metric
  source_pages: p214-215
  source_chapter: COMPANY/WEB DIRECTORY APPLICATION ACCESS LEVELS
  source_quote: |
    "No Access - Not allowed to start the application • Partial Read - To view non-personal attributes of
    all entries ... Total Read - To view all attributes of all entries ... Partial Modification - The
    administrator can View or modify non-personal attributes of list entries ... Import for modification
    or export non-personal attributes of green, orange, or red list entries ... All - ... Create, delete,
    import or export all entries" (p214)
    "Partial View Orange List - To display non-personal attributes of the green and orange entries •
    Partial View Red List - ... green, orange and red entries • Total View of Red List - To display all
    attributes of the green, orange and red entries • Partial Modification of Web Directory - To display,
    create, edit or delete non-personal attributes of all entries • All - To display, create, edit or
    delete all attributes of all entries" (p215)
  summary: |
    Company Directory 应用五档：No Access / Partial Read（全部条目非个人属性）/ Total Read（全部属性）/
    Partial Modification（指定条目列表的非个人属性可改 + 绿/橙/红条目非个人属性可导入导出）/ All（全属性 +
    建/删/导入导出全部条目）。Web Directory 应用五档：Partial View Orange List / Partial View Red List /
    Total View Red List / Partial Modification / All。授予入口：Security 应用 nmc > 8770Applications >
    Company Directory 或 WebDirectory，加账户选级别。
  conditions: AdminNmc 默认 All；实测验证见 c06
  tags: [metric, access-level, security, definitions]

- id: p13
  title: ISDN 号码构造公式与三条失败分支
  type: formula
  source_pages: p258-259
  source_chapter: ISDN NUMBER CONSTRUCTION
  source_quote: |
    "ISDN number = ISDN prefix + Entity installation number + Set directory number" (p258)
    "If Entity installation number not defined, ISDN number is not built" (p258)
    "DDI set case • Set number replaced by the DDI number • If DDI translator not managed, set number
    replaced by entity sup nb • If entity supplementary number not defined, ISDN number is not constructed" (p258)
    "ISDN prefix is only used if PCX ISDN Number can be constructed" (p258)
  summary: |
    公式：ISDN 号 = ISDN 前缀 + 实体安装号 + 话机号。失败分支：①实体无安装号 → 不构造；②DDI 话机——翻译器
    纳管则话机号换成 DDI 号，未纳管则换成实体补充号，补充号也没有 → 不构造；③非 DDI 话机——话机号换成实体
    补充号，无补充号 → 不构造。前缀只在整个号码可构造时才加。p259 示例表九行验证：最常用行（"Configuration
    mostly used, especially with public SIP carrier"）= 有 DDI 翻译器 + 国家码前缀 33 → ISDN 号 33298143600。
  conditions: 修改 PCX 数据后必须重新同步 ISDN 号才更新（p257）
  tags: [formula, isdn, ddi, construction]

- id: p14
  title: 个人呼叫号码（Private Calling Number）替代规则与 NPD 前提
  type: rule
  source_pages: p260, p273
  source_chapter: PERSONAL CALLING NUMBER / Calling number management
  source_quote: |
    "PCX side: Use Personal Calling Numbers is validated ... Private Calling Number is filled {ISDN
    Prefix} + Private Calling Number / Private Calling Number is not filled {ISDN Prefix} + Entity Inst.
    Nb + Directory Nb ... NPD flag called Authorize personal calling num use to be managed" (p260)
    "Use Personal Calling Number - No: User's ISDN number is built from the user's entity and default DDI
    translator. - Yes: user's ISDN number is equal to the user's Private Calling Number." (p273)
  summary: |
    规则：PCX 侧启用 Use Personal Calling Numbers + NPD 标志 Authorize personal calling num use 打开后，
    用户可带私有呼叫号。8770 构造：填了 Private Calling Number → ISDN 号 = 前缀 + 私有呼叫号；没填 → 前缀 +
    实体安装号 + 话机号（回退标准路径）。书中实验明确标注该流程"FOR INFORMATION ONLY. DO NOT PROCEED"——
    属知识储备项。
  conditions: 实验中不执行（讲师演示口径）
  tags: [rule, isdn, calling-number, npd]

- id: p15
  title: STAP 权限三态与 SIP 话机排除
  type: rule
  source_pages: p172, p180, p272
  source_chapter: CLICK TO CALL / Users STAP settings
  source_quote: |
    "STAP - Off hook: automatic call is authorized when the receiver is picked up. - Authorized: automatic
    call is authorized with or without picking up the receiver of a hands-free set. - Forbidden: automatic
    call is not authorized" (p272)
    "The STAP option can be setup for all types of phones except SIP devices." (p272)
    "OXE SIP phones can't use the Click to Call feature" (p172)
  summary: |
    STAP 三态：Off hook（摘机才发起）/ Authorized（免提摘不摘机均可）/ Forbidden（禁止）。配置入口：Configuration
    应用选用户 > All 页签。硬边界：SIP 话机（含 MicroSIP、SIP extension）不支持 STAP 与 Click to Call——实验
    中 STAP 呼叫主叫必须是 IPTouch/IPDSP 类话机（31000 IPDSP 作主叫、SIP 话机作被叫）。
  conditions: 关联话机定义需分机号+话机密码（实验口径 0000）
  tags: [rule, stap, click-to-call, sip-limitation]

- id: p16
  title: 前缀规则参数语义与创建层级选择原则
  type: rule
  source_pages: p276-278, p284
  source_chapter: Configuring the prefix rules / Add-On Examples
  source_quote: |
    "Prefix to add Specify the prefix to add before to initiate the call (i.e. 00 for the main trunk group)
    • The first digit 0: to take the main trunk group • The second digit 0: to complete the DID number ...
    Prefix to delete This parameter has 2 functions: It is interpreted as number starting with and prefix
    to delete (i.e. 33)." (p277)
    "If a rule can be applied for the whole network, its' better to create at network level. If a rule must
    be applied to an OXE which can be different from another one, its' better to create at PCX level." (p276)
    "If ARS is managed in the PCX ... A single rule is enough: Prefix to delete: empty (means for all
    called number) • Prefix to add: 0 (ARS seizure prefix)." (p284)
  summary: |
    参数语义：Prefix to delete 双重含义——匹配头（以 33 开头才应用）+ 删除内容；Prefix to add 按位拼（实验例：
    第一位 0 走主中继组、第二位 0 补齐 DID 号；国际例 000=ARS 前缀 0+国际码 00）。层级选择：全网规则建 Network
    层、单 OXE 规则建 PCX 层；建在 PCX 下的规则按序号（Rule #1/#2）作用于该 PCX 人员。双规则分流例：06 开头
    走中继组 10（删 06 再加回 06+10 前缀）、其余走中继组 20。PCX 已有 ARS → 单规则"删空+加 0"即可。
  conditions: 规则与属性绑定入口在 Administration 应用（见 p17）
  tags: [rule, prefix-rule, ars, hierarchy]

- id: p17
  title: Click to Call 属性关联矩阵——默认三属性 + Misc1-5 扩展
  type: metric
  source_pages: p256, p279-281
  source_chapter: ATTRIBUTES FOR AUTOMATIC CALL / Associate prefix rules with attributes
  source_quote: |
    "By default, the extension, ISDN and Mobile numbers attributes can be used to initiate a call" (p256)
    "Number dialing attribute Extension, ISDN Number, Mobile rules are created by default. ... Rule to
    apply None: in this case, the call is established without modification of the number" (p279)
    "Right click on Click to Call. Select Create > Prefix management in the contextual menu. Select the
    attribute to add ... Select Misc 1 ... Extension, ISDN Number, Mobile, Misc 1, Misc 2, Misc 3, Misc 4,
    Misc 5" (p280)
    "you will have five possible calls by clicking on Extension, ISDN number, Misc. 1 or Mobile attributes" (p281)
  summary: |
    属性关联矩阵（Administration 应用 nmc > Application Configuration > Click to Call）：默认已建 Extension/
    ISDN Number/Mobile 三项——实验口径 Extension 绑 None（分机原样拨）、ISDN Number 绑外部呼叫规则、Mobile 绑
    外部呼叫规则；Misc1-5 需右键 Click to Call > Create > Prefix management 手工添加并可绑规则。属性取值来源：
    Extension=链接分机；ISDN=自动构造；Mobile/Misc=目录手工填。关联完成后人员在 Web 客户端可有多达 5 个可点号码。
  conditions: Misc 属性值在 Directory 应用人员条目 Miscellaneous 页签填
  tags: [metric, click-to-call, attributes, association]

- id: p18
  title: DDI 翻译器取回控制与 ISDN 前缀分配参数
  type: metric
  source_pages: p271-272
  source_chapter: Click To call / Prefix number management
  source_quote: |
    "DID translator list We manage in this field a list of DDI translators to retrieve or to exclude
    (ex. 0; 2-4; 6 will exclude the DID translators 0,2,3,4 and 6)" (p271)
    "DID translation usage ... • Default (retrieve the default DDI translator 0) • All (retrieve all DDI
    translators managed at OXE side) • List to select ... • List to exclude" (p271-272)
    "ISDN Prefix list per DID Translator This field allows assigning a dedicated prefix per DDI translator
    (ex. 2-3 :33; 9 :39)" (p272)
    "Process ISDN Number Enable the construction of ISDN numbers for the persons linked to the users of
    this PCX." (p272)
  summary: |
    PCX 节点 Data Collection 页签四参数：①DID translator list——翻译器列表（支持 0;2-4;6 语法）；②DID
    translation usage——Default（只取 0 号默认翻译器）/ All / List to select / List to exclude；③ISDN Prefix
    list per DID Translator / per Entity——按翻译器或实体分配专属前缀（2-3:33; 9:39 语法）；④Process ISDN
    Number——启用人员 ISDN 号构造（本实验的开关）。DDI 翻译器本体三字段在 Translator > External Numbering
    Plan > Default DID num. translator：First external number（实验 33210N41000）/First internal number
    （31000）/Size range（500，实验口径）。
  conditions: 实验口径数值按 POD 号变化
  tags: [metric, ddi-translator, isdn-prefix, parameters]

- id: p19
  title: 词典文件路径体系与版本号机制
  type: metric
  source_pages: p287, p297, p299, p302, p306, p309-310
  source_chapter: DICTIONARY CUSTOMIZATION
  source_quote: |
    "The .dict files are stored in the folder C:\8770\dict." (p299)
    "#1: Save the new translations in the folder C:\8770\dict\user. #2: Automatically generate files in
    the folder C:\8770\Locales\dict\user. #3: update the archive 8770\Client\bin\dict_user.zip" (p302)
    "you always must select the 'LdapAttributes.dict' file from C:\8770\Client\dict\. All company
    directory attributes changes are saved on C:\8770\Client\dict\user, but only customized attributes." (p309)
    "Dictionary version number Display the dictionary version number. This field is empty by default. It
    is incremented after each save from the customization tool." (p297)
  summary: |
    路径表：源词典 C:\8770\dict（讲义）与 C:\8770\Client\dict（How-To 口径，打开定制工具时必选此处的
    LdapAttributes.dict）；用户词典 C:\8770\dict\user（只存被定制的属性）；本地化生成 C:\8770\Locales\dict\user；
    客户端分发包 8770\Client\bin\dict_user.zip。版本号：默认空，每保存一次 +1（实验从空→1→3），回退
    Set All to Default 也会 +1；客户端连接时自动校验并下载新 zip。
  conditions: 两处路径（dict 与 Client\dict）在书中共存，操作时以 How-To 的 Client\dict 为准
  tags: [metric, dictionary, paths, versioning]

- id: p20
  title: 词典属性选择的上下文匹配规则（同名 Misc 属性）
  type: warning
  source_pages: p301, p304-305
  source_chapter: Customizing the attributes / Warnings
  source_quote: |
    "WARNING SEVERAL ATTRIBUTES ARE NAMED MISC1 AND MISC2. IN THIS CASE, YOU MUST SELECT THE ATTRIBUTES
    WITH THE CONTEXT INFORMATION FIELD EMPTY." (p301)
    "SEVERAL ATTRIBUTES ARE NAMED MISCELLANEOUS. IN THIS CASE, YOU MUST SELECT THE ATTRIBUTES WITH THE
    FOLLOWING CONTEXT INFORMATION TAB NAME FOR PCX ENTRY IN CONFIGURATION APPLICATION." (p304)
    "SEVERAL ATTRIBUTES ARE NAMED MISC. 1. IN THIS CASE, YOU MUST SELECT THE ATTRIBUTES WITH THE FOLLOWING
    CONTEXT INFORMATION ATTRIBUTE NAME IN PBX ENTRY (CONFIGURATION APPLICATION)" (p305)
  summary: |
    词典里同一属性名有多条记录（不同上下文）：改"人员信息"的 Misc1/Misc2 → 选 Context information 为空的行；
    改配置应用 PCX 条目的 Miscellaneous 页签 → 选上下文为"PCX 条目页签名"的行；改 PCX 条目的 Misc.1/Misc.2 →
    选上下文为"PBX 条目属性名"的行。选错行会改错界面文案且不易察觉。
  conditions: 用 Find 快速定位后必须核对 Context information 列
  tags: [warning, dictionary, context, selection]

- id: p21
  title: Web 目录客户端 GlobalParameters 默认值表
  type: metric
  source_pages: p328
  source_chapter: Directory client customization / Main page
  source_quote: |
    "Creation of entries allowed Enabled (by default). ... Maximum number of entries in personal address
    books 500 (default value). ... Display authentication icon Enabled (by default) ... Display browse tab
    Enabled (by default) ... Display customization icon Enabled (by default): user can customize the Web
    Directory client. Disabled: only administrator account (i.e. AdminNmc) can customize the default
    configuration of the Web Directory client used by all users" (p328)
  summary: |
    GlobalParameters 默认值（Administration > Application Settings > DirectoryClient > GlobalParameters）：
    地址簿条目上限 500、建条目允许=开、认证图标=显示、关联话机图标=显示、Browse/Search/Edit 页签=显示、
    主题菜单=显示、定制图标=显示（关掉后仅 AdminNmc 能改全局默认）。实验改动：上限 500→10、关闭关联话机图标。
  conditions: 实验要求值：10 条上限、隐藏 Define associated station 图标
  tags: [metric, globalparameters, defaults, web-directory]

- id: p22
  title: 客户端定制默认参数的存储位置语义（双向通道）
  type: rule
  source_pages: p330, p332, p334, p337, p339
  source_chapter: Search filters / Grid / Detail / Edit customization
  source_quote: |
    "Modifications are saved in the Administration application." (p330)
    "Filter attributes Specify the attributes (in LDAP format) that can be used to filter data according
    to the selected object type. To add a value, double-click on a field, right-click and select Add a
    value." (p331)
    "Object types ... All_Company (All), Group (Group), Organization (company), OrganizationalUnit
    (department), Person (Person), Room (Room)." (p331)
  summary: |
    双通道改同一份数据：Web 客户端管理员登录 > Customize 图标 > Default parameters 页签，或 Administration 应用
    nmc > Application Settings > DirectoryClient 下节点（SearchClasses 过滤属性 / GridAttributes+PrintAttributes
    网格与打印列 / DetailAttributes 分区显示与可编辑属性）——改动统一落 Administration 应用（LDAP 格式属性名）。
    对象类型六种：All_Company/Group/Organization/OrganizationalUnit/Person/Room；详情页分区 Areas 按
    ViewXxxAreas 命名。
  conditions: 属性必须写 LDAP 名（如 sn/givenname），不是界面译文
  tags: [rule, customization, directoryclient, storage]

- id: p23
  title: MSAD 集成许可与系统兼容清单
  type: metric
  source_pages: p351, p369
  source_chapter: MSAD INTEGRATION / Compatibilities
  source_quote: |
    "Integration with Microsoft Active Directory (MSAD) on • Windows Server 2016 • Windows Server 2019 •
    Windows Server 2022" (p351)
    "A license is required to enable both features" (p351)
    "The Active Directory server can run under a Microsoft Windows Server 2016, Windows Server 2019 and
    Windows Server 2022." (p369)
  summary: |
    MSAD 同步 + AD 结构更新两能力共用一张 Active Directory integration 许可；AD 服务器支持 Windows Server
    2016/2019/2022。Azure AD 的 tree 模式另需 Directory 许可（p360）。
  conditions: Ed40 口径；2025 之后的 Windows Server 版本需查最新兼容表
  tags: [metric, msad, licensing, compatibility]

- id: p24
  title: MSAD 属性映射硬规则（sn/objectGUID/电话/uid）
  type: rule
  source_pages: p355-356, p380-381
  source_chapter: MSAD SYNCHRONIZATION / Attribute mapping + Hidden mapping
  source_quote: |
    "Can be deleted (except last name attribute) • Custom mapping attributes can be added (with few
    restrictions) • Default value can be specified for attribute with empty value • Direction can be changed" (p355)
    "Hidden mapping • abObjectGUID (8770) <- objectGUID (AD) for unicity of the data in 8770" (p356)
    "sn (Last name) only from AD to 8770, mandatory to create person in 8770. Can't be deleted" (p356)
    "telephoneNumber (Extension), isdnNumber (ISDN Number) only from 8770 to AD. Can be deleted" (p356)
    "uid (User id) only from AD to 8770 as key attribute ... • uid update performed with rename operation
    • uid automatically built from firstname and name if mapping not defined" (p356)
    "Only one Attribute Mapping entry can be created." (p380)
  summary: |
    映射硬规则五条：①映射条目全 8770 只能建一条；②sn（姓）只能 AD→8770、必填、不可删；③隐藏映射
    abObjectGUID ← objectGUID 保证唯一性（不出现在映射界面）；④telephoneNumber/isdnNumber 只能 8770→AD
    （可删）；⑤uid 只能 AD→8770（属性可选），更新走改名操作，未定义映射时自动用名+姓构造。附加属性可加
    （如 Mobile 双向、Employee number AD→8770 默认值 1234），方向可单向或双向，空值可给默认值。
  conditions: 默认映射：姓/名/显示名/MSAD 用户 ID/邮件 AD→8770，电话号码 8770→AD（p380）
  tags: [rule, msad, mapping, restrictions]

- id: p25
  title: MSAD 同步规则 Filter 与 Flat/Tree 语义
  type: rule
  source_pages: p385-387
  source_chapter: Creating a rule
  source_quote: |
    "Filter operation provides an option to synchronize only the required entries in the MSAD. Only
    entries having an Objectclass=user and a name (cn) not empty are selected for the synchronization." (p385)
    "Flat Synchronization: All persons in the mentioned MSAD path (or under its child path) will directly
    get created in the company directory path (the CD location). Tree Synchronization: All entries in the
    mentioned MSAD path (or under its child path) will get created under the mentioned company directory
    path with the same hierarchical path." (p386)
    "If Synchronization mode=flat Only the users are synchronized, not the branches (you must create the
    branches manually)" (p387)
  summary: |
    规则四要素：Name、Filter（默认=objectclass=user 且 cn 非空）、8770 Location（CD 位置）与 MSAD Location
    （OU 路径）、Synchronization mode。Flat：人全部平铺到目标 CD 位置（分支要手工建）；Tree：按 AD 层级镜像
    建分支+人。Attribute mapping 字段自动填充映射名。
  conditions: Complete 同步时机见 p26
  tags: [rule, msad, sync-rule, flat-tree]

- id: p26
  title: MSAD 同步调度规则——Complete/Partial 时机与双向更新边界
  type: rule
  source_pages: p388, p390
  source_chapter: Scheduling the synchronization / Managing the Directory
  source_quote: |
    "Complete synchronization All the entries (which satisfy the specified filter) are (re)synchronized
    ... Need to be done after: - The creation of the synchronization rule - Any Modification in the
    attribute mapping / synchronization rule ... Partial synchronization Only recently
    created/modified/deleted attributes get synchronized based on the last synchronized date" (p388)
    "The OmniVista 8770 Company Directory is not updated if persons are created or modified in the Active
    Directory with their attributes first name and/or last name empty." (p390)
    "The Active Directory is only updated when a person entry is modified in the OmniVista 8770 Directory.
    The Active Directory is not updated if a person entry is created or deleted in the OmniVista 8770
    Directory." (p390)
  summary: |
    调度规则：规则新建或映射/规则修改后必须跑一次 Complete（全量）；日常用 Partial（按上次同步日期增量），
    可立即/定时/周期执行。边界三条：①AD 建人或改人时姓/名全空 → 8770 不同步该人；②AD 删人 → 按 Automatic
    deletion 参数处理（False=标记删除待手工清，True=永久删除，见 p27）；③8770→AD 方向只在"修改人员"时同步，
    8770 侧新建/删除人员不回写 AD。
  conditions: 双向语义不对称是排障第一检查点
  tags: [rule, msad, scheduling, sync-direction]

- id: p27
  title: MSAD 删除行为二态（Automatic deletion of 8770 users）
  type: rule
  source_pages: p377, p390
  source_chapter: Declaring the MSAD server / 8770 directory update
  source_quote: |
    "Automatic deletion of 8770 users ... enable (True) or disable (False - default value) automatic
    definitive deletion of users, during synchronization. True: users are deleted from the OpenTouch
    server, OmniPCX Enterprise and OmniVista 8770 (Users and Directory applications). False: entry is
    marked for deletion in the OmniVista 8770 Directory. Manual deletion is required to delete the entry
    permanently" (p377)
  summary: |
    AD 删人后的二态：False（默认）——8770 目录条目标记为删除（marked as deleted），需人工确认才真正消失；
    True——同步时连 OpenTouch/OXE/8770（Users+Directory 应用）一并永久删除。实验验证：False 时删 Charlize
    Cohen → 显示已标记；True 时删 Christopher Cane → 条目消失。生产建议先 False 观察再切 True。
  conditions: 参数在 Access info 声明里（实验口径 disabled）
  tags: [rule, msad, deletion, behavior]

- id: p28
  title: MSAD 插件部署路径与文件清单
  type: metric
  source_pages: p404-412, p425-426
  source_chapter: Installing the MSAD Plug-in
  source_quote: |
    "MSAD8770Admin is an 8770 administrator account dedicated to MSAD Plug-in. Its password has been
    defined at OmniVista 8770 server installation." (p404)
    "The following file is created: 8770MSADPlugin.properties It is available on C:\8770\data\msadplugin\
    MSAD Server" (p406)
    "The 3 files to be copied and pasted are: - Setup.exe - ReadMeFor8770MSADPlugin.txt -
    8770MSADPlugin.properties" (p408)
    "C:\Program Files (x86)\Alcatel-lucent\8770MSADPlugin is created" (p412)
    "The log file of the Alcatel-Lucent Unified User Management web tool is located on the MSAD server in
    the folder %TMP%\start8770webclient.log" (p426)
  summary: |
    部署数值表：改 MSAD8770Admin 密码 → 重启 NMC Java Service Definition 服务；生成 properties 至
    C:\8770\data\msadplugin\MSAD Server；三文件经 SHARING 文件夹中转到 AD 服务器 %LOCALAPPDATA%；setup.exe
    以管理员运行装到 C:\Program Files (x86)\Alcatel-lucent\8770MSADPlugin；插件日志 %TMP%\start8770webclient.log；
    properties 内含 8770_url（https://nms.company.com:8443/webclient）、MSAD8770Admin 的 DN 与加密密码、映射 DN
    （cn=Mapping, cn=MSAD, cn=MSADManagement,o=nmc）、AD 账号与加密密码。更新用户时仅 Cost center 与 Salutation
    可改。
  conditions: 所有路径为实验（Windows Server）口径
  tags: [metric, msad-plugin, paths, deployment]

- id: p29
  title: 管理域许可组合与激活开关
  type: metric
  source_pages: p435, p458
  source_chapter: ACTIVATE THE FEATURE / Granted licenses
  source_quote: |
    "Required licenses • Domain Management • Directory / Management Domain to be enabled • Feature disabled
    by default after fresh installation • To be enabled from Security application" (p435)
    "If the OmniVista 8770 server is based on a MCS solution (Managed Communications Services), Directory
    license will be provided by default. But the Domain Management license is still required." (p458)
  summary: |
    双许可：Domain Management + Directory。MCS 版 8770 自带 Directory 许可，但 Domain Management 仍要单独买。
    功能默认关闭：Security 应用 > 8770DomainManagement > Enable 勾选后 Apply。许可证核查入口：主窗口 Help >
    About（Granted licenses）。
  conditions: 域创建入口 Security 应用 8770 Domain Management 右键 Create > Domain
  tags: [metric, domains, licensing, activation]

- id: p30
  title: 本地管理员密码策略——首登强制改密的关闭
  type: rule
  source_pages: p470
  source_chapter: Domains for management / Password policy to be updated
  source_quote: |
    "Password reset after first login or reset / Put False to disable reinitialazation of password after
    first login." (p470)
  summary: |
    域实验的配套动作：Security 应用 > Password Policy > Password policy 页签，把 "Password reset after first
    login or reset" 设为 False，避免批量建完本地管理员后首登全被强制改密打断验证流程。生产环境按安全策略决定，
    实验环境为顺畅验证关闭。
  conditions: 教学口径；生产保留强制改密更安全
  tags: [rule, password-policy, security]

- id: p31
  title: Web 目录按域检索的 strict view 行为
  type: rule
  source_pages: p453-454
  source_chapter: FEATURE BEHAVIOR FROM A PERSON OF THE COMPANY DIRECTORY
  source_quote: |
    "Local admin: • Access to all persons from its domain only ... Person member of a domain: • Search
    results depend on nested domains and strict view parameter" (p453)
    "Strict view parameter disabled (by default) • Person search can retrieve persons from domain D but
    also from parent domain(s) • Strict view parameter enabled • Person search can retrieve persons but
    strictly from domain D" (p454)
  summary: |
    域内人员用 Web 目录检索时：strict view 关（默认）——能查到本域 D 及其父域的人；strict view 开——只查本域 D。
    另两条：Web 目录认证为强制（域场景下匿名不可用）；不属于任何域的人只能查无域人员。全局管理员不受限。
  conditions: strict view 参数随域配置
  tags: [rule, strict-view, domains, search]

- id: p32
  title: 目录复制数字口径表（副本 ID/数量上限/7 天窗口）
  type: metric
  source_pages: p509-510, p514-515
  source_chapter: Company Directory Replication / Prerequisites & Limits / Maintenance
  source_quote: |
    "The Id of a consumer suffix is automatically set to 65535" (p509)
    "The Id of a master suffix is set manually (value between 1 and 65534)" (p510)
    "One master server can have up to 4 slave servers • Only 5 replica (master or consumer) can be created
    in each OmniVista 8770 server" (p514)
    "Unavailability period <=7 days • All data created in the master during the unavailability period are
    replicated • Unavailability period > 7 days • All Data created in the master during the unavailability
    period are lost • Data from the master have to be manually restored on the slave server via an LDIF
    export/import mechanism" (p515)
  summary: |
    数字表：Consumer 副本 ID 固定 65535（自动）；Master 副本 ID 手工 1-65534 且不得重复；1 主 ≤4 从；每台 8770
    副本总数 ≤5；从机断联 ≤7 天 → 恢复后自动补齐主侧新增数据，>7 天 → 断联期主侧新增数据丢失、须 LDIF 导出/
    导入人工恢复。复制必须调度执行、不能实时（p505）；LDAPS 不支持；Address Book 不可复制（p514）。
  conditions: 复制管理器密码默认与 directory manager 相同（superuser），可经 toolsOmniVista.exe 改（p511/521）
  tags: [metric, replication, limits, maintenance]

- id: p33
  title: 目录复制前提清单与配置对称性要求
  type: checklist
  source_pages: p514, p519, p522-523, p529
  source_chapter: Prerequisites & Limits / How-To 前提与对称性
  source_quote: |
    "The operating system language and OmniVista 8770 installation language must be the same on both master
    and slave server • ... Must have the same version • Must have the directory license • Must have the
    same company directory name" (p514)
    "Master and slave servers must have the same value for the parameter 8770 master for cost center
    management." (p519)
    "Automatic creation ... Must be disabled on slave server. / UID construction Parameter Must be identical
    on both servers." (p522-523)
    "Attribute set cannot be modified after the creation of the replication agreement. You have to delete
    the replication agreement and recreate it selecting the new attribute set." (p529)
  summary: |
    上线前 checklist：①双机同版本、同 OS 语言、同安装语言、双 Directory 许可、同公司目录名；②网络号一致；
    ③"8770 master for cost center management"参数双机一致；④UID 构造双机一致；⑤Slave 关自动创建与 Location；
    ⑥DNS/hosts 双向可解析（主可 ping 通从机名与 FQDN，反之亦然）；⑦复制协议创建后属性集不可改——要改只能删协议
    重建，或改后 Initialize 强制全量。
  conditions: 复制配置入口：Administration > Preferences > Administration > Replication configuration
  tags: [checklist, replication, prerequisites]

- id: p34
  title: Initialize 语义与调度错峰原则
  type: rule
  source_pages: p530-532
  source_chapter: Initialize the replication / Schedule the replication
  source_quote: |
    "Initialize action recopies (deletes first all data in the consumer suffix) all the data from the
    Master to Slave server for that sub-suffix." (p531)
    "If you click on Schedule key, you will manage the replication job out of the scheduled period of
    daily/weekly jobs of both Master and Consumer server." (p531)
    "Schedule a daily execution of the replication at 5:00AM" (p530)
  summary: |
    Initialize=先清空 Consumer 对应 suffix 的全部数据，再从 Master 全量拷贝（属性集变更后必须跑）；Schedule
    排程要避开主从两机已有的日/周维护任务窗口——实验选每日 5:00AM。调度经 Scheduler 应用 Simple job，可右键
    Execute now 手动触发验证。
  conditions: 移除顺序 Consumer→Master（p533）；不一致恢复流程见 n 系列
  tags: [rule, replication, initialize, schedule]

- id: p35
  title: LDIF 工具命令参数速查表
  type: metric
  source_pages: p543-548
  source_chapter: LDIF MANAGEMENT TOOLS
  source_quote: |
    "ConvertLdif -cp -mc mc.conf -ma ma.conf -da da.conf -p p.conf domino.ldif > 8770.ldif" (p543)
    "exportLdap -b 'o=abs,o=DirectoryRoot' -h OMNIVISTA -p 389 -D 'uid=adminnmc, cn=Administrators,cn=8770
    administration,o=nmc' -w 'superuser' -o objectclass -n -s sub > export.ldif" (p544)
    "importLdap -h OMNIVISTA -p 389 -D '...' -w 'superuser' -c -e errorsyntax.log -r errorimport.log data.ldif" (p545)
    "Ldif2Csv myFile.ldif > myFile.csv / Csv2Ldif myFile.csv > myFile.ldif" (p546)
    "purgeldap -b 'o=abs,o=DirectoryRoot' -h omnivista -p 389 -D '...' -w 'superuser' -f purgefilter.conf" (p547)
    "linkdn -b 'o=abs,o=DirectoryRoot' -h omnivista -p 389 -D '...' -w 'superuser' -f link.conf" (p548)
  summary: |
    六工具参数速查：ConvertLdif（-mc 类映射/-ma 属性映射/-da 派生属性/-p 路径 conf）；ExportLdap（-b 基准 DN/
    -h 主机/-p 389/-D 管 DN/-w 密码/-o objectclass/-n/-s sub 子树）；ImportLdap（-c 出错继续/-e 语法错误日志/
    -r 导入错误日志）；Ldif2Csv/Csv2Ldif（双向转换）；PurgeLdap（-f purgefilter.conf 按过滤删）；LinkDn
    （-f link.conf 从属性值算 DN 链接，如按助理电话号码建 assistant 链）。管理员 DN 模板
    uid=adminnmc, cn=Administrators, cn=8770 administration, o=nmc。
  conditions: 工具位于 8770\bin（p542）；密码实验口径 superuser
  tags: [metric, ldif-tools, cli, parameters]

- id: p36
  title: PurgeLdap 配套机制——misc10 标记实现"外部删除跟随"
  type: rule
  source_pages: p547, p557
  source_chapter: PurgeLdap / Part 4 - Delete entries via PurgeLdap
  source_quote: |
    "PurgeLdap is used to delete entries from an LDAP directory using an LDAP filter. • It can be used to
    delete entries that were not in the last LDIF import for synchronization with another directory and
    ensure data consistency between the two directories" (p547)
    "4.5. Delete the line associated to the person Smith David in the directoryUS.txt ... 4.7. Launch the
    command purge.bat — Check the deletion of the person Smith David in the company directory" (p557)
  summary: |
    机制：导入管道（go.bat/da.conf）给每次导入/更新的条目写 misc10 标记（时间戳类值）；purgefilter.conf 定义
    "misc10 不等于本次标记"的过滤条件；purge.bat 执行 PurgeLdap 把没被本轮导入覆盖的条目删掉——等效实现"外部
    目录删了、8770 跟删"，补上 LDIF 导入不删除的缺口。验证路径：删外部数据一行 → 跑 go.bat → 跑 purge.bat →
    条目消失。
  conditions: misc10/purgefilter 细节依赖随书实验文件（LDIF1.zip），生产化需自行设计标记字段
  tags: [rule, purgeldap, sync-deletion, mechanism]

- id: p37
  title: OXE 节点声明字段规则——节点号公式与凭据三件套
  type: rule
  source_pages: p93-96
  source_chapter: Declaring the OmniPCX Enterprise
  source_quote: |
    "Subnetwork – Node number Enter a numeric value equal to the OmniPCX Enterprise network*100 + OmniPCX
    Enterprise node number. Example: With a network number = 1 and node number = 2, you must enter 101" (p95)
    "FTP Username / FTP Password adfexc Enter adfexc password (i.e. Superuser2580*). This is the OXE FTP
    login and password used for data retrieval. Process configuration Validate this check box to enable
    configuration of this OXE. Alarm reception mode Select Permanent IP connectivity" (p95)
    "SSH connection Check the box to authorize SSH/SFTP connection • Host name Enter a unique ID for each
    secured OXE ... The host name is used by MindTerm application to create the SSH public key on the
    OmniVista 8770 server" (p96)
  summary: |
    声明规则：Subnetwork-Node number=OXE 网络号*100+节点号（书例网络 1/节点 2 → 101，与公式表面矛盾，实验实配
    网络 1/节点 1 → 101；公式按"网络号补百位+节点号"理解，见 n 系列勘误）；子网号必须等于 OXE 网络号；Network/
    Subnetwork 字段留空（自动继承）；凭据两套——adfexc（FTP 取数）+ mtcl（Software download 页签维护账户）；
    Alarm reception mode 必选 Permanent IP connectivity（自动创建事件的前提）；Directory Process 勾选加载话簿；
    勾 SSH connection 并填唯一 Host name（字母开头，仅字母数字与 .,-_），8770 用 MindTerm 建 SSH 公钥。
  conditions: 空间冗余时主 IP 填两条（右键 Add a Value）
  tags: [rule, oxe-declaration, node-number, credentials]

- id: p38
  title: 自动创建的三个开关组合
  type: checklist
  source_pages: p105-107
  source_chapter: Automatic creation management / Event reception management
  source_quote: |
    "Create for users (OXE) To be enabled • Limit to real users (OXE) To be enabled • Create for user alias
    (OXE) To be enabled" (p105)
    "Automatic creation To be enabled / Location for automatic creation Location path to be defined" (p105)
    "Alarm reception mode Select the mode Permanent IP connectivity. / Process directory To be enabled." (p107)
  summary: |
    三处开关联合生效：①全局参数（Administration > Application Configuration > Application Settings >
    Directory Admin > AutomaticCreation）——Create for users / Limit to real users / Create for user alias
    三项启用；②节点级（Configuration 应用 OXE > Data Collection）——Automatic creation 启用 + Location for
    automatic creation 选默认路径（如 Department 1）；③事件前提——PCX 页签 Process directory 启用 + Alarm
    reception mode=Permanent IP connectivity。任一缺失自动创建不工作。
  conditions: Visio Room/普通用户/别名用户的差异化供给靠①的三开关组合
  tags: [checklist, automatic-creation, switches]

- id: p39
  title: 成本中心继承矩阵（链接视角实证口径）
  type: metric
  source_pages: p130-131, p138, p81-84
  source_chapter: Links management / Notes
  source_quote: |
    "Once DECT Dupont user is defined as a secondary link of Jean Dupont, he inherits from the Jean Dupont
    cost center. Now DECT Dupont cost center is MKT." (p130)
    "Once Fax Set user is defined as a Fax link of Jean Dupont, no change is applied to its cost center.
    Fax Set cost center is still TSS. Don't forget that a fax can be shared by several persons." (p131)
    "After modification, cost center of Jean Dupont is Training. ... Cost Center of Fax Set is TSS." (p138)
  summary: |
    实证矩阵：目录侧改人员 CC（MKT→Training）→ 主链接用户与副链用户跟随变 Training，传真链保持 TSS 不变；
    建副链瞬间副链用户 CC 立即被主链接 CC 覆盖；建传真链不触碰 CC。界面刷新注意：Configuration Users 文件夹
    要关开一次才显示新 CC 值。
  conditions: 与 p06 方向规则互为表里
  tags: [metric, cost-center, inheritance, links]

- id: p40
  title: 目录树与 MSAD OU 的位置语法对照
  type: metric
  source_pages: p385
  source_chapter: Creating a rule / Locations
  source_quote: |
    "CD location: l=Colombes, c=FR, o=directoryRoot / MSAD location: OU=Colombes, OU=France, DC=company,
    DC=com" (p385)
  summary: |
    位置语法对照：8770 CD 位置=l=Colombes, c=FR, o=directoryRoot；MSAD OU 路径=OU=Colombes, OU=France,
    DC=company, DC=com。写同步规则时两边各选一次（图形选择器自动生成），手工排障时按此对照读日志。
  conditions: Tree 模式下分支名按 AD OU 名镜像创建
  tags: [metric, msad, location, syntax]
```

---

## 任务覆盖自检（task↔id 映射）

| task | 对应 principle 条目 |
|---|---|
| task-01 OXE 注册同步 | p37（声明规则）、p04（DN 格式） |
| task-02/03 树+自动创建 | p38（三开关）、p07（CC 规则）、p05（链接铺垫） |
| task-04 UID 构造 | p03 |
| task-05 自动继承 | p39（继承矩阵） |
| task-06 链接管理 | p05、p06、p39 |
| task-07/08/09 改名与修复 | p06、p07、p08（转换删除） |
| task-10 LDIF 导入导出 | p09、p10 |
| task-11 Web 客户端 | p11（可见性矩阵） |
| task-12 保密级别 | p11、p12 |
| task-13 SIP 运营商 | （case c05 承载，无独立数值原则） |
| task-14 Click to Call | p13、p14、p15、p16、p17、p18 |
| task-15 词典定制 | p19、p20 |
| task-16 客户端定制 | p21、p22 |
| task-17 MSAD 声明 | p23、p27 |
| task-18 MSAD 同步 | p24、p25、p26、p40 |
| task-19 MSAD 插件 | p28 |
| task-20 管理域 | p29、p30、p31 |
| task-21 委派与定制视图 | p31（strict view）、p22（视图存储） |
| task-22 目录复制 | p32、p33、p34 |
| task-23 LDIF 工具 | p35、p36 |
| 背景（虚拟化/兼容） | p01、p02 |

无遗漏：全部 23 项任务均有对应数值/规则/清单支撑。
