# 框架/流程/结构候选 — OmniVista 8770 目录管理 (8770XTE202EN Ed40)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、应用/界面分区。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。页码为 PDF PAGE 标记口径。

```yaml
- id: f01
  title: 全书课程推进逻辑——方案总览 → 环境准备 → 目录核心概念 → 接入/使用/定制/管道/运营五大层
  type: flow
  source_pages: p4, p59-60, p88, p170, p206, p252, p285, p311, p349, p427, p501, p536
  source_chapter: LESSON SUMMARY（各章）/ 目录顺序
  source_quote: |
    "General overview / Network topology / Architecture / Virtualization / Cross compatibility /
    Applications suite / Setup suite / Network suite / Reports suite / Directory suite / 8770 WBM client" (p4)
    "✓ Overview ✓ Company & address book ✓ Directory tree ✓ PCX items and links ✓ User identifier
    ✓ Distinguished Name ✓ Links between Directory persons and OXE users ✓ Entry type conversion
    ✓ Data update ✓ LDIF import & export" (p60)
  summary: |
    课程按十二段推进：①8270 套件总览（本书只精讲 Directory suite）；②RLAB 实验平台；③SIP 模拟器；④目录应用核心概念（树/UID/DN/六类链接/数据更新/LDIF）；⑤OXE 节点注册 How-To；⑥PCX 自动创建 How-To；⑦链接管理 How-To；⑧LDIF 导入导出 How-To；⑨Web 目录客户端（讲义+How-To）；⑩保密级别（讲义+How-To）；⑪Click to Call（讲义+How-To，中间插入 OXE SIP 运营商配置 How-To）；⑫词典定制、客户端定制、MSAD 三部曲、管理域、委派、复制、LDIF 工具（各为讲义+How-To 配对）。教学主线：先建"人-机绑定"的语义模型，再逐层叠加查询、保密、拨号、集成、分权与冗余。
  conditions: 无版本前提；How-To 章节间有明确依赖（如链接管理依赖自动创建产物）
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: OmniVista 8770 网络拓扑——服务器/厚客户端/WBM/Web 目录客户端四角色
  type: diagram
  source_pages: p6
  source_chapter: SOLUTION OVERVIEW / NETWORK TOPOLOGY
  source_quote: |
    "Graphical User Interface (GUI) to manage 8770 applications • Simultaneous access to OmniVista 8770
    Server • Requires a login and password" (p6)
    "HTML application to access the directory information • Anonymous access allowed" (p6)
    "HTML interface for network administration management (Users, Configuration, Performance)" (p6)
  summary: |
    LAN 上四类角色：①8270 Server（+本地 client）；②8270 厚客户端（GUI 管理全部应用，需登录密码，支持多客户端并发）；③WBM 客户端（HTML 网管界面：Users/Configuration/Performance + Manage My Phone 终端用户自管话机）；④Web Directory 客户端（HTML 目录查询，允许匿名访问）。全 IP 连通即可，无专用协议通道。理解点：目录查询是唯一开放匿名的入口，这决定了后续保密级别机制的必要性。
  conditions: R5.2 拓扑；WBM Users 应用需 Unified Management 许可（p35）
  tags: [diagram, architecture, topology, clients]

- id: f03
  title: 8770 服务器架构协议图——双存储 + 多协议北向
  type: diagram
  source_pages: p7
  source_chapter: ARCHITECTURE
  source_quote: |
    "Server / Config. / binaries / OXE ... MariaDB (SQL) / LDAP / OV8770 Services / Web Directory ...
    CMISE, (S)FTP, Telnet/SSH, LDAP ... HTTPS, LDAP(S) / IPSec, Corba, TDS, LDAP(S)" (p7)
    "OMC (FTP, HTTPS) ... OXO Connect Synchronization / User creation" (p7)
  summary: |
    架构三块：①存储层——MariaDB(SQL) + LDAP 双库；②服务层——OV8770 Services 承载 Web Directory、邮件（SMTP）、批量开通（Mass provisioning）、LDAP Client import、Manage My Phone；③北向对接——OXE（HTTPS/LDAP(S)/CMISE/(S)FTP/Telnet/SSH/LDAP）、OXE SIP 话机、OXO Connect（经 OMC FTP/HTTPS 同步与建用户）、SNMP Hypervisor（SNMPv3）、WBM（HTTPS）。目录数据流向：PCX 用户 → 配置目录 → 链接 → 公司目录。
  conditions: 协议清单为 R5.2 架构图口径
  tags: [diagram, architecture, protocols, storage]

- id: f04
  title: 虚拟化部署形态与平台支持
  type: structure
  source_pages: p8
  source_chapter: VIRTUALIZATION
  source_quote: |
    "Hypervisors • VMware ESXi (6.x, 7.0 and 8.0) • Microsoft Hyper-V® 2016, 2019, 2022 •
    Nutanix AHV (20220304) • ASW (Amazon Web Services)" (p8)
    "No OmniVista 8770 license for virtualization" (p8)
    "OmniVista 8770 Capacity Planning tool V3.0 for a better sizing flexibility of virtual machines parameters" (p8)
  summary: |
    8770 可跑在客户前提的单台 Appliance 或数据中心托管形态；虚拟机要求与物理机相同，虚拟化本身不收许可，但按 Hypervisor 不同某些补充服务可能额外收费。支持 ESXi 6.x/7.0/8.0、Hyper-V 2016/2019/2022、Nutanix AHV(20220304)、AWS；容量定 型用 Capacity Planning tool V3.0。
  conditions: 背景知识章，本书不展开 sizing
  tags: [structure, virtualization, hypervisor, licensing]

- id: f05
  title: 跨版本兼容矩阵（8770 R4.2-R5.2 × OT/OXE/OXO）
  type: structure
  source_pages: p9
  source_chapter: CROSS COMPATIBILITY
  source_quote: |
    "OpenTouch BE / MS / MC — OT R2.4 to R2.6.1 X X X X" (p9)
    "OmniPCX Enterprise — OXE R12.2 to R12.4 X X X X / OXE Purple R100 (N1) X X X / OXE Purple R100.1 (N2)
    X X / OXE Purple R101.0 (N3), R101.1 (N4) & R101.2 (N5) X" (p9)
    "OXO Connect / OCE — R4.0 X X X X / R5.0 to R5.1 X X X / R5.2 to R6.2 X X" (p9)
  summary: |
    四列 = 8770 R4.2/R5.0/R5.1/R5.2。行规律：OT R2.4-2.6.1 四版全兼容；OXE R12.2-12.4 四版全兼容；OXE Purple 新版本只向后兼容新 8770（R101.x 仅 R5.2）；OXO/OCE R5.2-6.2 仅 R5.1/R5.2。交付前必须按此表核对 PCX 与 8770 版本配对。
  conditions: Ed40 印刷口径，新版本 PCX 需查最新矩阵
  tags: [structure, compatibility, versioning, matrix]

- id: f06
  title: 应用套件全景——厚客户端四套件 15 个应用
  type: structure
  source_pages: p10, p12-26, p27-30, p31-33
  source_chapter: APPLICATIONS SUITE / SETUP / NETWORK / REPORTING / DIRECTORY SUITE
  source_quote: |
    "Administration / Security / Maintenance / Scheduler —— Server Administration" (p10)
    "Configuration / OXO Connect Supervision / Users / Devices / Alarms / Topology / Audit / Maintenance
    —— PCX Administration & Supervision" (p10)
    "Account./Traf./VoIP (Accounting) / (Traffic Analysis) / Reports —— Accounting & Performance monitoring" (p10)
    "Directory / Web Directory —— Directory Configuration & Customization" (p10)
  summary: |
    四套件分组：①Setup/Server Administration（Administration 应用设置、Security 管理员权限、Maintenance 服务器维护、Scheduler 任务调度）；②Network/PCX 管（Configuration 节点声明、OXO Connect 监督/配置、Users 用户、Devices 终端、Alarms 告警、Topology 拓扑图、Audit 审计、Maintenance 节点备份）；③Reporting（Accounting 计费、Traffic Analysis 话务、Reports 统一报表 TXT/XLS/HTML/PDF）；④Directory（Directory 目录应用 + Web Directory 客户端）。本书只精讲第④组及与之交错的 Security/Alarms/Configuration/Administration/Scheduler。
  conditions: 厚客户端视角；WBM 四应用另见 f07
  tags: [structure, applications, suite, menu-map]

- id: f07
  title: 8770 WBM 客户端四应用与边界
  type: structure
  source_pages: p34-38
  source_chapter: 8770 WBM CLIENT
  source_quote: |
    "User provisioning and company directory levels management ... Available with Unified Management license
    • Zero footprint (light client)" (p35)
    "Connection to one OXE node at a time ... No OT and no OXE direct access via SSH/Telnet" (p36)
    "Monitor key elements of different OXE systems ... Dedicated dashboards including several widgets" (p37)
  summary: |
    WBM 四应用：①Users——用户供给与公司目录层级管理（MACD 单界面完成、批量导入导出、需 Unified Management 许可、支持管理域）；②Configuration——网络/子网/OXE 节点树导航（一次只连一个 OXE，不支持 SSH/Telnet 直连，网络/子网/节点只能在厚客户端管理）；③Performance——OXE 关键指标仪表盘（VoIP CDR + SNMP MIB 数据）；④Manage My Phone——终端用户自管话机（邮箱登录、呼叫转移、可编程键）。理解点：后文链接管理实验中 WBM 改名行为与厚客户端 Users 应用一致（p150-155）。
  conditions: WBM 登录 https://nms.company.com:8443（实验口径）
  tags: [structure, wbm, web-client, licensing]

- id: f08
  title: RLAB 远程实验平台结构——POD 池 + 公共资源区
  type: structure
  source_pages: p41-51
  source_chapter: REMOTE LABS PLATFORM
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a
    data center." (p43)
    "OMNIVISTA 8770 SERVER 8770_OV8770_SETUP nms 192.168.1.70 ... 8770 credentials: AdminNmc / Superuser01*" (p47)
    "Console mode ... / Remote Desktop Connection from Windows (Based on Guacamole session ... Mandatory
    to be used on labs to share audio resources required for softphones applications" (p51)
  summary: |
    POD 1..n 相互独立同配置：OXE（csa 192.168.1.1 / csm 192.168.1.3，无用户）、OMS（192.168.1.13）、FlexLM（192.168.1.80）、Client PC（192.168.1.10，装 IPDSP 31000 + MicroSIP 31001/31002 + Public MicroSIP + TrapReceiver）、Ecosystem（192.168.1.100，AD 服务器）、OV8770 server（nms 192.168.1.70，已装好，AdminNmc/Superuser01*）。公共区 10.20.30.x：NAS、邮件服务器、SIP 模拟器（12.0.0.2）、外部 DNS 10.20.30.250；内部 DNS 192.168.1.250，网关 192.168.1.254（均实验口径）。访问两法：Console mode（管 PCX 实例/装服务器，无音频）与 RDP（软电话实验必用）。
  conditions: 实验口径；所有 IP/密码为教学约定值
  tags: [structure, lab, rlab, topology]

- id: f09
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则
  type: diagram
  source_pages: p54-57
  source_chapter: SIP CARRIER SIMULATOR
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... ITSP1 Public gateway public.itsp1.com 10.20.30.50" (p54)
    "PBX P / Id: pbxP / password: alcatel" (p54)
    "National numbers 3311PN12345 3321PN12345 3331PN12345 3341PN12345 3351PN12345 ... Mobile numbers
    3361PN12345 3371PN12345 ... International call to UK 4421PN12345" (p55)
    "DDI table - First external number 3321PN41000 ... DDI table – First internal number 31000" (p57)
  summary: |
    模拟器在公共区扮演运营商：SIP 网关 gateway1.itsp1.com（PBX 注册账号 pbxP/alcatel，SIP 域 sip.itsp1.fr）+ 公网网关 public.itsp1.com（两个 MicroSIP 扮演 Public/Urgence 用户，域名 itsp1.fr）。号码规则：PN=两位 POD 号；紧急号 112/15/17/18；SIP Public 主号 3321PN12345。呼出变换例（POD3）：拨 0110312345 → 送 +33110312345。呼入：DDI 首外部号 3321PN41000 ↔ 首内部号 31000，分机 100 外部号 3321PN41100。LOOP 呼叫可用本 PBX DDI 自呼验证。
  conditions: 实验口径（RLAB 专用基础设施）；生产 SIP 中继需替换全部参数
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f10
  title: 目录树结构——Organization/Termination 两类条目与 LDAP 层级模板
  type: structure
  source_pages: p62-63, p436
  source_chapter: DIRECTORY APPLICATION / COMPANY & ADDRESS BOOK, DIRECTORY TREE；DOMAINS / COMPANY DIRECTORY LEVELS ORGANIZATION
  source_quote: |
    "The Company Directory takes into account the organization with its geographical locations,
    departments, offices and employees ... Address books are an independent organization entry" (p62)
    "Tree structure made of Organization and Termination entries • Country • City • Company • Department
    —— Organization entries • Person • Group • Room —— Termination entries" (p63)
    "DN: o=Ale,o=directoryRoot ... DN: c=FR, o=Ale,o=directoryRoot ... DN: l=Brest, c=FR,o=Ale,o=directoryRoot
    ... DN: ou=Marketing, l=Colombes, c=FR,o=Ale,o=directoryRoot ... • o: organization • c: country
    • l: location • ou: organization unit • uid: user identifier" (p436)
  summary: |
    公司目录是 LDAP 树：组织类条目 Country/City/Company/Department 作枝干，Person/Group/Room 作叶子；地址簿（Address book）是独立于公司目录的组织条目分支。LDAP 层级模板（p436）：o(组织) → c(国家) → l(城市) → ou(部门) → uid(人)，人可挂在任意层级。树是管理域（f27）与复制副本（f29）的切割单位。
  conditions: 树结构创建入口：Directory 应用 Company 页签右键 Create
  tags: [structure, ldap-tree, directory, dn]

- id: f11
  title: 目录条目与配置应用条目的链接关系（PCX items）
  type: diagram
  source_pages: p64-65
  source_chapter: PCX ITEMS AND LINKS
  source_quote: |
    "A directory entry can be linked to an item of the Configuration application • User • Station group
    • System speed dial number • User alias • System speed dial number alias • Service number (Voice mail)" (p64)
    "Link between Company Directory and Configuration application" (p65)
  summary: |
    目录条目可链接到配置应用（技术目录 o=nmc）六类条目：User（用户）、Station group（话机组）、System speed dial number（系统缩位拨号）、User alias（用户别名）、System speed dial number alias、Service number（如语音信箱服务号）。这是"公司目录（给人看）↔技术目录（给系统用）"两棵树的缝合点，也是 Click to Call 取号的来源。
  conditions: 链接类型细分见 f13
  tags: [diagram, links, pcx-items, configuration]

- id: f12
  title: UID 与 DN 双标识体系
  type: structure
  source_pages: p66-67
  source_chapter: USER IDENTIFIER / DISTINGUISHED NAME
  source_quote: |
    "UID: First name + Last name • A UID is unique in the Company Directory ... May be manually modified
    if first name or last name is updated • The name is displayed in the Web Directory client" (p66)
    "Pitt Duane DN (Directory application) • uid=Duane Pitt, ou=Support dpt, o=Export ltd, l=Paris,
    c=fr, o=dgo, o=directoryroot / User10 DN (Configuration application) • TelephoneNumber=31000,
    Cn=TelephonicDevices, SubnetworkNodeNumber=101, SubnetworkNumber=1, NetworkNumber=1, o=nmc" (p67)
  summary: |
    双标识：UID 是人员记录的业务 key（默认名+姓，目录内唯一，Web 客户端显示 Name=姓+名）；DN 是树内位置路径。两棵树 DN 格式不同——目录侧以 uid= 起头落到 o=directoryroot，配置侧以 TelephoneNumber/Cn=TelephonicDevices 起头落到 o=nmc。UID 构造方法可按 PCX 配置（None/Extension），详见 p04 原则。
  conditions: UID 修改不影响 DN 中的 uid 值本身（DN 由树位置+UID 组成）
  tags: [structure, uid, dn, identifier]

- id: f13
  title: 六类人员-用户链接体系与基数规则
  type: structure
  source_pages: p68-72
  source_chapter: LINKS BETWEEN DIRECTORY PERSONS AND OXE USERS
  source_quote: |
    "Primary link: 1 entry => 1 user, 1 user => 1 entry ... Name, first name and cost center name are
    identical • Only one primary link can be defined for each entry" (p69)
    "Multi-device link: 1 entry => n users, 1 user => 1 entry ... Automatically created after partial or
    complete OXE synchronization" (p69)
    "Secondary link: 1 entry => n users, 1 user => 1 entry ... Allow an entry to be associated to a
    telephone extension with a different name (like DECT)" (p70)
    "Fax link: 1 entry => n user, 1 user => n entries ... Miscellaneous link: 1 entry => n users,
    1 user => 1 entry" (p70)
    "Additional resources link: Same properties as Primary link ... Useful for migration of OmniVista
    4760 persons with multiple Primary links with OXE users" (p71)
  summary: |
    六类链接：①Primary（1:1，姓名+成本中心一致，每条目唯一，手工或自动建）；②Multi-device（1 entry→n users，同步后自动建，多话机共用一条目）；③Secondary（手工建，异名同成本中心，典型 DECT，CC 继承主链接）；④Fax（n:n，成本中心互不影响，传真机可共享）；⑤Miscellaneous（异名同成本中心，数据终端/Modem 等非话音终端）；⑥Additional resources（主链接同性质但可多条，4760 迁移场景）。主链接是根：改姓名必须经公司目录（见 n 系列反例）。
  conditions: 建立入口：Directory 应用右键 Settings links...（Primary/Secondary/Fax 页签）；Multi-device 经 Users 应用 Add a secondary set
  tags: [structure, links, person, oxe-user, cardinality]

- id: f14
  title: 主链接自动创建机制——事件驱动四步链
  type: flow
  source_pages: p74-76, p107-109
  source_chapter: LINKS / Primary link – Automatic creation; AUTOMATIC CREATION How-To / Event reception
  source_quote: |
    "Directory entry automatically created in a specified location after the creation of PCX items ...
    During the synchronization of the PCX • When an event is received" (p74)
    "An event is sent → The Configuration tree is updated → Creation of a user ... Automatic creation of
    the person in the specified location" (p75)
    "If a person with same User ID already exists in the directory, an alarm is generated by the
    OmniVista 8770 server" (p76)
  summary: |
    自动创建链：PCX 建用户（如 31022 Visio Room）→ 事件送达 8770 → 配置树更新 → 在 Location 指定路径自动建人员并建主链接。两个前提（p107）：OXE 的 Process directory 启用 + Alarm reception mode=Permanent IP connectivity。同名 UID 时拒建并告警（Alarms 应用 NMC>nms>LDAP server 可查，p118）。另可把误建的人员条目转成 Room 类型（p109）。
  conditions: 依赖 task-01 的节点注册与告警接收模式
  tags: [flow, automatic-creation, event, primary-link]

- id: f15
  title: 数据更新方向表——链接类型 × 属性 × 同步方向
  type: diagram
  source_pages: p79-84
  source_chapter: DATA UPDATE（含四个示例）
  source_quote: |
    "Primary link (automatic or manual creation) Name / First name / Cost center name / ISDN number ==>
    ==> <=> <== ... In case of primary link, the name and / or first name modification must be done via
    the Company directory" (p79)
    "If the update is done via the Company Directory, the OmniVista 8770 Server checks that the cost
    center name exists in the PCX ... If cost center does not exist, PCX refuses the modification and
    generates an alarm" (p80)
  summary: |
    更新方向按链接类型分档：主链接——姓名/名字单向（目录→PCX）、成本中心双向、ISDN 号从 PCX（实体安装号+DDI 翻译器）取回；副链——成本中心双向、ISDN 从 PCX；传真链——传真号从 PCX；杂项链——成本中心双向。四个示例（p81-84）：目录侧改 CC → 主/副链全变、传真链不变；PCX 侧改 CC → 主/副链跟随、传真链不变；PCX 侧改主链接用户姓名 → 主链接断（目录侧姓名不动）；杂项链 CC 更新。成本中心必须在 PCX 已存在，否则拒绝并告警回滚。
  conditions: 改名入口差异详见 counter-example n 系列
  tags: [diagram, data-update, direction, cost-center]

- id: f16
  title: LDIF 导入导出体系——三范围 × 两目的地 + 调度
  type: flow
  source_pages: p85-86, p156-169
  source_chapter: LDIF IMPORT & EXPORT
  source_quote: |
    "All or part of the database can be imported or exported in LDAP Data Interchange Format (LDIF) files
    ... An LDIF import • Allows creating and modifying data • Does not remove data" (p85)
    "Export the selected entries only / Export only the entries at the selected entry sublevel / Export
    the selected entry and its sublevels ... On the client (local drive) or on the server" (p86)
    "When the LDIF export process is scheduled on the server, the LDIF export file is saved in the
    following path C:\8770\Client\data\import" (p165)
    "Right click and select Import > Immediate on local drive > Add and modify…" (p168)
  summary: |
    导出三范围：Entry（仅选中条目）/Sublevel（仅下一层）/Branch（选中条目及全部子层，最完整）；目的地：本地驱动器（即时）或服务器（走 Scheduler，可定期，落盘 C:\8770\Client\data\import）。导入入口：Import > Immediate on local drive > Add and modify…，导入只增改不删除——"删除"靠手工删或 PurgeLdap 工具（f30）。导入前选目标父条目（如 Brest），LDIF 内的相对结构挂入该分支。
  conditions: 导入不删除是全套数据管道设计的第一性约束
  tags: [flow, ldif, import, export, backup]

- id: f17
  title: Web 目录客户端页面结构与两级访问模型
  type: structure
  source_pages: p173-181
  source_chapter: WEB DIRECTORY CLIENT（讲义）
  source_quote: |
    "Anonymous access ... Directory consultation in read only / Authenticated access ... User id and 8770
    password required • Modification of the user's record allowed • Management of the personal address book" (p178)
    "Allows making an automatic call from the web directory client • Enter your extension number and
    secret code • Click the extension number you want to call" (p180)
  summary: |
    页面五区：Home（入口图标：Directory consultation/Authenticate/Address Book/主题选择/Define associated station）、Browse（选搜索根）、Search（按 Individuals/Groups/Room/Company/Department 类别 + 属性/条件/关键词，支持多条件组合）、Results（命中列表）、Details（属性详情，按权限显示；含 Delete/助理/经理查看）。Edit 页签需认证。访问两级：匿名=只读；UID 认证=可改本人记录+管个人地址簿。Click to Call 原理六步（p181）：定义关联话机（分机+密码）→ 搜索 → 点号码 → 8770 服务器发起呼叫请求（31000→32000）→ 话机响铃。
  conditions: WBM 目录客户端入口 https://nms.company.com（p186）或 :8443（p238）
  tags: [structure, web-directory, anonymous, authenticated, click-to-call]

- id: f18
  title: 保密级别 × 访问级别双矩阵
  type: structure
  source_pages: p209-215
  source_chapter: DIRECTORY CONFIDENTIALITY LEVELS（讲义）
  source_quote: |
    "4 levels of confidentiality available • Entries with the confidentiality level 'Green' (default
    value) • Entries with the confidentiality level 'Orange' • Entries with the confidentiality level
    'Red' • Administration 8770 is the most confidential level" (p209)
    "Personal data • Home Telephone • Home Address • Car License • Employee Number • Password" (p210)
    "No Access / Partial Read / Total Read / Partial Modification / All —— Company Directory application
    access levels" (p214)
    "Partial View Orange List / Partial View Red List / Total View of Red List / Partial Modification of
    Web Directory / All —— Web Directory application access levels" (p215)
  summary: |
    两套正交机制：①条目保密四级（Green 默认/Orange/Red/Admin8770）+ 属性两类（personal 五种 vs 非个人）；②账户访问级别——Company Directory 应用五档（No Access/Partial Read/Total Read/Partial Modification/All）、Web Directory 应用五档（Partial View Orange/Partial View Red/Total View Red/Partial Modification/All），在 Security 应用按应用分别授予。行为矩阵：匿名只见 Green 非个人数据；person 账户见 Green 条目 + 本人（含本人 personal data）；web 管理员按级别扩大可见范围；AdminNmc 全开。
  conditions: 实测矩阵见 case c06；访问级别入口 Security 应用 nmc > 8770Applications > Company Directory / WebDirectory
  tags: [structure, confidentiality, access-level, matrix, security]

- id: f19
  title: Click to Call 端到端调用链
  type: flow
  source_pages: p181, p254-256, p269-284
  source_chapter: CLICK TO CALL（讲义+How-To）
  source_quote: |
    "OmniVista 8770 solution allows automatic calls from the Web directory client between a telephone
    set associated to the user and a telephone number in the LDAP directory ... To allow this number to
    be dialled from the Web Directory Client, prefix rules must be configured" (p254)
    "By default, the extension, ISDN and Mobile numbers attributes can be used to initiate a call" (p256)
    "All phone numbers in bold characters are available for STAP call" (p283)
  summary: |
    调用链五环：①PCX 侧——DDI 翻译器定义 DDI↔内线映射，用户 STAP 权限三态（Off hook/Authorized/Forbidden），OXE 同步回填；②8770 侧——Process ISDN Number 启用，为人员自动构造 ISDN 号；③规则层——在 Network/Subnetwork/PCX 层建前缀规则；④关联层——nmc > Application Configuration > Click to Call 下把规则绑到 Extension/ISDN number/Mobile/Misc1-5 属性；⑤使用层——Web 客户端 Define associated station（分机+密码）→ 搜索人员 → 粗体号码点击外呼。默认可用属性：Extension/ISDN/Mobile；Misc 1-5 需手工创建关联。
  conditions: SIP 话机全线不支持（STAP 与 Click to Call 均否，p172/p272）
  tags: [flow, click-to-call, stap, prefix-rule, dial-chain]

- id: f20
  title: ISDN 号码构造规则（DDI/非 DDI 分支）
  type: structure
  source_pages: p257-260
  source_chapter: ISDN NUMBER CONSTRUCTION / PERSONAL CALLING NUMBER
  source_quote: |
    "ISDN number = ISDN prefix + Entity installation number + Set directory number" (p258)
    "If Entity installation number not defined, ISDN number is not built ... Set number replaced by the
    DDI number • If DDI translator not managed, set number replaced by entity sup nb" (p258)
    "Use Personal Calling Number is validated ... Private Calling Number is filled {ISDN Prefix} +
    Private Calling Number / Private Calling Number is not filled {ISDN Prefix} + Entity Inst. Nb +
    Directory Nb ... NPD flag called Authorize personal calling num use to be managed" (p260)
  summary: |
    构造公式：ISDN 号 = ISDN 前缀 + 实体安装号（Inst nb/Sup nb）+ 话机号。分支：DDI 话机——话机号被 DDI 号替换（翻译器未纳管则用实体补充号；补充号也没有则不构造）；非 DDI 话机——话机号被实体补充号替换。ISDN 前缀只在 PCX ISDN 号可构造时使用；按 DDI 翻译器/实体可分别配前缀（PCX 页签 ISDN Prefix list，p272）。改了 PCX 数据必须重新同步才能更新 ISDN 号。个人呼叫号码（Private Calling Number）可整体替代安装号路径，前提 NPD 标志 Authorize personal calling num use 打开。
  conditions: p259 九行示例表为验证基准（"Configuration mostly used, especially with public SIP carrier" 行 = 前缀 33 + DDI 路径）
  tags: [structure, isdn, formula, ddi, numbering]

- id: f21
  title: 前缀规则三类型与创建层级选择
  type: structure
  source_pages: p261-263, p276-284
  source_chapter: PREFIX RULES（讲义）+ Click To Call How-To
  source_quote: |
    "Types of prefix rules • None • Rule for external call • Rule for call between network" (p261)
    "The rule is applied to all numbers beginning with 33 - Delete 33 - Add 00 (0 the ARS prefix + 0 the
    carrier Id) ... The rule is applied to all other numbers - Add 000" (p262)
    "If a rule can be applied for the whole network, its' better to create at network level. If a rule
    must be applied to an OXE which can be different from another one, its' better to create at PCX level." (p276)
  summary: |
    三类规则：None（原样拨）、外部呼叫规则（参数=加前缀+删前缀/匹配头，例：删 33 加 00；对以 33 开头号生效）、网间呼叫规则（选目标 Network 或 Subnetwork + 加前缀，例：经 ABC 中继组键 1/2 呼异子网 3100 → 拨 13100/23100）。创建层级：Configuration 应用树右键 Network/Subnetwork/PCX → Create > Rule for external call / Rule for calls between network；全网通用建在 Network 层，OXE 个性规则建在 PCX 层；建在 PCX 下的规则作用于该 PCX 人员（规则 #1/#2 顺序即匹配顺序）。规则绑定到属性在 Administration 应用做（见 f19④）。
  conditions: Add-on（p284）：按号段分流两条外部规则模拟 ARS；PCX 已有 ARS 时单规则"删空+加 0"即可
  tags: [structure, prefix-rule, ars, routing, hierarchy]

- id: f22
  title: 词典定制机制——dict 文件体系与保存三动作
  type: flow
  source_pages: p287-293, p295-310
  source_chapter: DICTIONARY CUSTOMIZATION（讲义+How-To）
  source_quote: |
    "Default translations are stored in the dictionaries LdapAttributes.dict ... CustomDict tool used to
    generate a second dictionary that contains the new translations • Dictionary LdapAttributes_user.dict" (p287)
    "Save button used to #1: Save the new translations in the folder C:\8770\dict\user. #2: Automatically
    generate files in the folder C:\8770\Locales\dict\user. #3: update the archive 8770\Client\bin\dict_user.zip" (p302)
    "During the connection to the OmniVista 8770 server, the 8770 client check that is has the last
    dictionary version. If not, the dictionary (dict_user.zip) is downloaded from the OmniVista 8770 server." (p310)
  summary: |
    属性"改名"=改翻译：默认词典 LdapAttributes.dict（存于 C:\8770\dict，实验中亦提示 C:\8770\Client\dict），用 CustomDict 工具生成用户词典 LdapAttributes_user.dict；保存一次做三件事（user 目录 + Locales 生成 + dict_user.zip 重打包），每次保存 Dictionary version number 自增（Administration 应用 nmc > OmniVista 8770 页签查看）。客户端连接时校验版本并自动下载 zip。可定制范围（p288-289）：Configuration 的 Misc 页签、Directory 全部属性（Associated sets 页签除外）、Accounting organization 共享九属性（Address/Postal Code/Mail/Office-Room No./Department/Company/Employee Number/Misc1-3）、Reports 同 Directory。回退：Edit > Set All to Default（也自增版本号）。
  conditions: 服务器上 8770 客户端运行时无法保存（dict_user.zip 被占用）
  tags: [flow, dictionary, customization, dict, versioning]

- id: f23
  title: Web 目录客户端定制三层模型——默认参数/用户参数/主题
  type: structure
  source_pages: p311-322, p324-348
  source_chapter: CUSTOMIZATION OF THE DIRECTORY CLIENT（讲义+How-To）
  source_quote: |
    "Themes define a set of graphical properties used for the graphical display ('skins') ... 2 different
    themes are available" (p313-314)
    "Paul didn't customize the tab Results: The default configuration is used / Jean customized the tab
    Results: The user configuration is used / Default configuration of the tab used in case of anonymous
    access" (p322)
    "The theme selected by a user is saved in a cookie stored in the folder C:\Documents and Settings\
    <user name>\Cookies. The Edit option, that allows customizing the theme, is reserved to the Directory
    administrator." (p346)
  summary: |
    三层叠加：①默认参数（目录管理员在 Web 客户端 Customize 图标 > Default parameters 页签或 Administration 应用 DirectoryClient 节点设：GlobalParameters/SearchClasses/Grid/DetailAttributes/EditAttributes，改的是全体用户基线）；②用户参数（认证用户在 User parameters 页签覆盖个人视图，未定制者与匿名用户用默认）；③主题（两套：8770WBM→theme1、Custom→theme2，CSS 构成，存 C:\8770\Client\Themes；用户自选存 cookie，Edit 仅管理员）。回退双通道：LDIF 导入 Modify only（参数）+ Themes 文件夹替换（主题）。定制前置：先导出 DirectoryClient 分支 LDIF + 备份 Themes 文件夹（p326-327）。
  conditions: GlobalParameters 默认值表（500 条地址簿上限等）见 principle p25
  tags: [structure, customization, theme, default-parameters, user-parameters]

- id: f24
  title: MSAD 集成三层结构——服务器声明/映射+规则/插件
  type: structure
  source_pages: p351-359, p368-393
  source_chapter: MSAD INTEGRATION（讲义+两 How-To）
  source_quote: |
    "Persons creation from MSAD to 8770 directory • Update of directory attributes in both ways ...
    Requires a dedicated login on MSAD to update the directory attributes • LDAP or LDAPS connection" (p353)
    "Synchronization with multiple Active Directory servers" (p354)
    "Associate attributes of OV8770 company directory to attributes of Active Directory • Whole default
    mapping attributes customizable" (p355)
    "Defines the directory tree to be synchronized • Several synchronization rules can be created •
    Synchronization is scheduled in OV8770" (p358)
  summary: |
    三层：①Access info（Administration > nmc > MSAD Management > Create > Access info：Name/Host/Port 389 或 636/Username/Password/Is LDAPS/Automatic deletion of 8770 users/Scope/插件生成日期）——可声明多台 AD 服务器（MCS 多客户、大客户多部门各挂各 AD）；②Attribute mapping（只能建一条，默认映射+附加属性+方向+默认值）+ Synchronization rule（N 条：8770 CD 位置↔MSAD OU 位置、Flat/Tree 模式、Filter 过滤、挂映射、经 Scheduler 调度 Complete/Partial）；③MSAD 插件（f26，开户通道）。MSAD 侧前提：专用管理员账号入 Domain Admins 组。
  conditions: 映射硬规则见 principle p28；许可：Active Directory integration
  tags: [structure, msad, active-directory, sync-architecture]

- id: f25
  title: Azure AD (Microsoft Entra ID) 同步四步框架
  type: flow
  source_pages: p360-361
  source_chapter: AZURE ACTIVE DIRECTORY SYNCHRONISATION
  source_quote: |
    "Azure AD is considered as the master node • Synchronization in flat or tree mode supported •
    Authentication towards Azure AD from OV8770 as an application which wants to use Microsoft Graph API,
    instead of LDAPS for MSAD (Authentication without administrator rights) • No OXE users provisioning
    from Azure AD" (p360)
    "Configured in OmniVista 8770 in four steps：Preparation in Azure AD（Create the application secret
    value / Manage User.ReadWrite.All permission）/ Access information to Azure AD tenant / Synchronization
    rule(s)（Criteria to filter users / Flat or tree modes / Planning in scheduler）/ Attributes mapping
    (Attributes and direction are editable / Phone number is imposed by OV8770)" (p361)
  summary: |
    四步：①Azure 侧准备——建应用机密、授 User.ReadWrite.All 权限；②录入租户访问信息；③建同步规则（用户过滤条件、Flat/Tree、8770 Scheduler 排程）；④属性映射（方向可编辑，电话号码字段由 8770 强制）。与 MSAD 的五点差异：主节点恒为 Azure AD、认证走 Graph API 而非 LDAPS（无需管理员权限）、不 provision OXE 用户、可与 MSAD 并行、可同步多 Azure 域。许可：Active Directory integration（与 MSAD 共用）；tree 模式另需 Directory 许可。
  conditions: 本书为讲义章，无配套 How-To 实验
  tags: [flow, azure-ad, entra-id, graph-api, licensing]

- id: f26
  title: MSAD 插件（User Management Web Tool）部署与调用链
  type: flow
  source_pages: p363-366, p394-426
  source_chapter: MSAD PLUG-IN（讲义）+ How-To
  source_quote: |
    "A specific plug-in must be created in OV8770, then installed in MSAD server ... The MSAD plug-in
    enables to launch the web tool from the Active Directory ... HTTPS connection from web tool to
    OmniVista 8770 server • Creates user in 8770 server, OXE and/or OT server" (p365)
    "If 'Directory number' field is empty, selected telephone number will be the one automatically
    generated" (p364)
    "8770MSADPlugin.properties ... is available on C:\8770\data\msadplugin\MSAD Server" (p406-407)
  summary: |
    链路：8770 侧生成 8770MSADPlugin.properties（MSAD Management > MSAD > Mapping 右键 Create > ADPlugin，内含 8770 URL/DN/加密密码/映射 DN/AD 账号）→ 三文件（Setup.exe/ReadMe/properties）经 SHARING 文件夹中转拷到 AD 服务器 %LOCALAPPDATA% → 管理员运行 setup.exe（装到 C:\Program Files (x86)\Alcatel-lucent\8770MSADPlugin）→ AD 用户右键出现 "Alcatel-Lucent Unified User Management" → 选 Meta profile → Create 一键在 8770 目录+Users 应用+OXE 建用户。前置三件：MSAD8770Admin 账户改密（并重启 NMC Java Service Definition 服务）、OXE 空闲号码段、Meta profile。IE 前提：trusted sites 加 nms.company.com + 允许活动内容（未加则界面缺字段）。日志：%TMP%\start8770webclient.log。
  conditions: 更新仅成本中心与称谓可改；删除为确认后直删
  tags: [flow, msad-plugin, provisioning, meta-profile]

- id: f27
  title: 管理域模型——域=目录级别集合×管理员组
  type: structure
  source_pages: p429-450, p427-455
  source_chapter: DOMAINS FOR MANAGEMENT（讲义）
  source_quote: |
    "Possibility to split organization in several parts and manage them independently ... Each local
    administrator sees/manages his own domain for Directory and Users applications" (p429)
    "A domain can include one or several company directory levels ... A domain can be part of several
    parent domains" (p437)
    "A domain name • ServicesDomain • Set of company directory levels defining the domain scope ... List
    of (local) admins having rights in the domain • AdminServices" (p438)
  source_chapter_note: 用例三则——多站点委派（p430）、OXE 多租户 CPE/MCS（p431）、云端多公司（p432）
  summary: |
    域模型：域 = 名字 + 一组公司目录 DN 级别（可在 o/c/l/ou 任意层）+ 本地管理员名单；域可嵌套（FranceDomain ⊃ BrestDomain…）、可多父。搭建五步（p434）：查许可（Domain Management+Directory）→ 建目录结构 → Security 建管理员账户（默认全局，蓝色显示）→ 归入预定义组（f28）→ Security > 8770 Domain Management 建 6 域并关联级别与成员。功能默认关闭，须在 Security 应用手工 Enable（p435）。WBM 侧三入口（p444）：Domain configuration、Customized views、Administrator configuration。
  conditions: 本地管理员的"Domain configuration"菜单显示但不可用（p472）
  tags: [structure, domains, delegation, multi-tenant]

- id: f28
  title: 本地管理员三预定义组与权限档
  type: structure
  source_pages: p441, p444-450, p462-466
  source_chapter: SELECTED GROUPS FOR LOCAL ADMINISTRATORS + How-To
  source_quote: |
    "Users Configuration ... Access level/App: All/Users + All/Devices + All/Configuration + Partial
    modification/ Directory + No access/Customized views" (p441)
    "Users & Directory Configuration ... Full management on company directory levels within their domain(s)
    ... All/Directory + No access/Customized views" (p441)
    "Users & Customization Configuration ... Management of domains and administrator accounts from the
    8770 Web Provisioning Client ... All/Customized views" (p441)
    "Delegation: right for local administrators to create and manage other local administrators within
    their domain" (p450)
  summary: |
    三组权限档：①Users Configuration——只管用户，不能改目录结构与定制视图（Directory 仅 Partial modification）；②Users & Directory Configuration——用户+域内目录结构全管，仍无定制视图；③Users & Customization Configuration——再加定制视图与 Web Admin 客户端的域/账户管理。Delegation 是单独开关（Application rights 页签），开启后本地管理员可在自己域内再建本地管理员与目录级别。可见性验证（p471-476）：本地管理员登录厚客户端/WBM 只见本域分支。
  conditions: How-To 中 Users Configuration 的 Users 权限写为 Write/Users（p463），与讲义 All/Users 表述略有出入，以现场实测为准
  tags: [structure, groups, access-rights, delegation]

- id: f29
  title: 目录复制架构——Master/Consumer/Referral/Agreement 四件套
  type: diagram
  source_pages: p501-515, p517-535
  source_chapter: COMPANY DIRECTORY REPLICATION（讲义+How-To）
  source_quote: |
    "Replication allows to copy selected branches of the company directory from an OmniVista 8770 Master
    to another OmniVista 8770 Slave ... Redundancy only available for the company directory, not for the
    OmniVista 8770 server" (p503)
    "Master Replica • It is a read-write database ... Consumer Replica • It is a read-only database ...
    refers write requests to the master replica via a referral" (p505)
    "Replication Agreement • It is set of parameters defined in master server to configure and control
    the updates to the slave server" (p506)
    "FROM A MANAGEMENT POINT OF VIEW, IT'S STRONGLY RECOMMENDED TO MANAGE UPDATES ONLY FROM THE MASTER
    REPLICA" (p507)
  summary: |
    架构：主服务器建 Master replica（读写，供体）+ Replication agreement（协议：主副本配置/属性集/从机 Host:Port/复制管理器密码/初始化与调度）+ Attribute set（可复制属性组）；从服务器建 Consumer replica（只读，ID 固定 65535）。机制：Master 改动立即生效、Consumer 经调度复制后更新；Consumer 改动经 referral 转发 Master，但管理上强烈建议只在 Master 改。五步部署顺序（先从后主）：Slave 建 consumer → Master 建 master replica → 配协议 → 配属性集 → 初始化+调度（Initialize 会先清空 Consumer 再全量拷贝）。前提：同版本/同 OS 语言/同安装语言/双 Directory 许可/同公司名/同网络号/同 UID 构造/cost center 参数一致。
  conditions: 数字口径与 7 天规则见 principle p35-p36；移除顺序 Consumer→Master（p533）
  tags: [diagram, replication, redundancy, ldap]

- id: f30
  title: LDIF 管理工具管道——六个命令行工具与 conf 文件范式
  type: flow
  source_pages: p536-550, p552-558
  source_chapter: LDIF MANAGEMENT TOOLS（讲义+How-To）
  source_quote: |
    "The LDIF management tools allow you to synchronize the OmniVista 8770 Company Directory by importing
    and exporting LDIF files to and from other commercially available directories. • LDIF management tools
    are located in the folder 8770\bin" (p542)
    "ConvertLdif -cp -mc mc.conf -ma ma.conf -da da.conf -p p.conf domino.ldif > 8770.ldif" (p543)
    "exportLdap -b 'o=abs,o=DirectoryRoot' -h OMNIVISTA -p 389 -D 'uid=adminnmc, cn=Administrators,cn=8770
    administration,o=nmc' -w 'superuser' -o objectclass -n -s sub > export.ldif" (p544)
    "purgeldap -b 'o=abs,o=DirectoryRoot' -h omnivista -p 389 -D ... -f purgefilter.conf" (p547)
  summary: |
    工具箱（8770\bin）：ConvertLdif（补父条目/改属性值/替换属性与类名/改树形/加固定或计算值属性，四个 conf：mc=类映射、ma=属性映射、da=派生属性、p=路径）、ExportLdap（目录→LDIF）、ImportLdap（LDIF→目录，-c 继续 -e 语法错误日志 -r 导入错误日志）、Ldif2Csv/Csv2Ldif（与 Excel 数据采集互转）、PurgeLdap（按 filter 删条目，配合 da.conf 写 misc10 标记实现"外部目录删了我也删"）、LinkDn（从任意属性值算 DN 链接，如按助理电话号码建 assistant 链）。标准管道：CSV → Csv2Ldif → ConvertLdif → ImportLdap → (LinkDn) → (PurgeLdap)。
  conditions: p.conf 的 o=abs 根名必须改成本客户根名——忘改会产生坏结构，需 dirmanag.exe 删根（见 n 系列高危项）
  tags: [flow, ldif, cli-tools, batch, pipeline]
```

---

## 任务覆盖自检（task↔id 映射）

| task | 对应 framework 条目 |
|---|---|
| task-01 OXE 注册同步 | f03（架构）、f12（DN 格式）；流程细节在 case c01 |
| task-02/03/04/05 树+自动创建+UID+继承 | f10、f12、f14、f13（链接铺垫） |
| task-06/07/08/09 链接与改名 | f13、f15 |
| task-10 LDIF 导入导出 | f16 |
| task-11 Web 客户端使用 | f17 |
| task-12 保密级别 | f18 |
| task-13 SIP 运营商配置 | f09 |
| task-14 Click to Call | f19、f20、f21 |
| task-15 词典定制 | f22 |
| task-16 客户端定制 | f23 |
| task-17 MSAD 声明 | f24（第①层） |
| task-18 MSAD 同步 | f24（第②层） |
| task-19 MSAD 插件 | f26 |
| task-20 管理域 | f27、f28 |
| task-21 委派与定制视图 | f28（Delegation）、f23（视图模型在客户端定制框架） |
| task-22 目录复制 | f29 |
| task-23 LDIF 工具 | f30 |
| 背景（总览/虚拟化/兼容/WBM/RLAB/模拟器） | f01-f09 |

无遗漏：全部 23 项任务均可在本文件或 case.md 中找到对应结构/流程支撑。
