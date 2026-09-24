# 案例/实验/操作序列候选 — OmniVista 8770 目录管理 (8770XTE202EN Ed40)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号）标注"实验口径"。
> 条目说明: 全书 17 个 How-To 实验章 → 17 条（c01-c17），按书中出现顺序编排。页码为 PDF PAGE 标记口径。

```yaml
- id: c01
  title: OXE 节点注册与同步（前置检查、网络/子网/节点声明、Complete-Separate 同步）
  type: lab
  source_pages: p88-98
  source_chapter: OXE node registration（How-To）
  source_quote: |
    "Use the siteid command to display network and node number. ... Node number : 1 ; Network number : 1" (p89)
    "Subnetwork – Node number Enter a numeric value equal to the OmniPCX Enterprise network*100 + OmniPCX
    Enterprise node number. Example: With a network number = 1 and node number = 2, you must enter 101" (p95)
    "Log file C:\8770\log\ NMCSyncLdapPbx_1.log" (p98)
    "Date of last modification This field indicates the date and time of the last synchronization performed." (p98)
  steps: |
    1. 前置-收集 OXE 信息（p89）：主机名 csa、网络号 1、节点号 1、物理 IP 192.168.1.1、掩码 255.255.255.0、网关 192.168.1.254、主名 csm、主 IP 192.168.1.3、节点名 oxe；GD IP 192.168.1.12 在服（实验口径）。
    2. PuTTY SSH 连主 IP 192.168.1.3，执行 siteid 核对 Node number=1 / Network number=1。
    3. su - （密码 Superuser2580*，实验口径）→ netadmin -m → 选 5 Role addressing → 1 View：核对 local main csm 192.168.1.3（空间冗余时记录两条主 IP）。
    4. netadmin -m → 选 2 Show current configuration：确认 "Security with SSH: yes"；亦可用 netstat -an | grep :22（LISTEN 即开）与 grep :23（无输出即 telnet 关闭）。
    5. netadmin -m → 11 Security → 1 Firewall (iptables) Configuration → 3 Restricted Access Configuration → 1 View trusted hosts：核对 8770（omnivista 192.168.1.70）等主机在信任列表——所有与 Call Server 交互的主机都必须声明。
    6. Configuration 应用声明网络：右键 nmc → Create > Network：Name=ale，Network number=1。
    7. 声明子网：右键 ale → Create > Subnetwork：Name=abc1，Subnetwork number=1（必须等于 OXE 网络号）。
    8. 声明 OXE：右键 abc1 → Create > OmniPCX 4400/Enterprise：Name=oxe；Subnetwork-Node number=101（=网络号*100+节点号）；Network/Subnetwork 留空自动继承；IP address=192.168.1.3；FTP Username=adfexc / Password=Superuser2580*（实验口径）；勾 Process configuration；Alarm reception mode=Permanent IP connectivity；勾 Directory Process。
    9. Software download 页签：Username maintenance=mtcl，Password maintenance=Superuser2580*（实验口径）。
    10. Connectivity 页签：勾 SSH connection，Host name 填唯一名（字母开头，仅字母数字与 .,-_，MindTerm 据此建公钥）。
    11. 同步：右键 oxe → Synchronization > Partial > Global（课程用 Complete -> Separate，p97：Complete=不看上次同步日期全量，Partial=只同步上次之后变更；Separate=仅本 OXE，Global=含关联 OpenTouch）→ 对话框选 "of the task" → Status 页签 → Apply 启动 → Refresh 刷日志。
    12. 核验：同步成功消息出现；日志 C:\8770\log\NMCSyncLdapPbx_1.log；OXE 下生成 Users/Directory 等分支；oxe > Data Collection 页签 Date of last modification 显示本次时间。
  verification: |
    同步完成成功提示 + NMCSyncLdapPbx_1.log 无致命错误 + Data Collection 页签 Date of last modification 更新（p98）。
  conditions: OXE 为出厂实验配置（无用户）；8770 服务器已装好（AdminNmc/Superuser01*，实验口径）。
  tags: [lab, oxe, node-registration, ssh, synchronization]

- id: c02
  title: 从 PCX 自动创建目录条目（树搭建、三开关、事件接收、UID 构造、自动继承）
  type: lab
  source_pages: p99-122
  source_chapter: Directory Application - Automatic creation from the PCX（How-To）
  source_quote: |
    "Create for users (OXE) To be enabled • Limit to real users (OXE) To be enabled • Create for user alias
    (OXE) To be enabled" (p105)
    "The user Visio Room has been created on the Company Directory, in the default path, managed previously." (p108)
    "All users, previously created on the PCX, are available as persons on the Company Directory, in the
    default path, also managed previously." (p117)
    "After the cut and paste of the person Michel Vincent, its directory parameters have been automatically updated." (p122)
  steps: |
    1. 建目录树（Directory 应用 Company 页签）：Create > Country 选 France；France 右键 Create > City 建 Brest 与 Colombes；Brest 下 Create > Department 建 Department 1、Department 2；Colombes 下建 Department 3。
    2. 自动创建全局开关（Administration 应用 nmc > Application Configuration > Application Settings > Directory Admin > AutomaticCreation）：Create for users (OXE)、Limit to real users (OXE)、Create for user alias (OXE) 全部启用。
    3. 默认路径（Configuration 应用 oxe > Data Collection 页签）：勾 Automatic creation，点 Location for automatic creation → 搜索字段选 Department → 搜索 → 双击 Department 1 → OK。
    4. 事件前提（Configuration 应用 oxe > PCX 页签）：Alarm reception mode=Permanent IP connectivity；Process directory 启用。
    5. 建 Visio Room 用户（Configuration 界面右键 Users > Create）：General Characteristics：Directory Number=31022，Directory name=Visio Room。
    6. 验证事件：Alarms 应用 Event 页签出现 User 31022 创建事件；Directory 应用 Department 1 下自动出现 Visio Room 人员。
    7. 转型（可选）：Directory 右键 Visio Room 人员 → 转 Room → 确认（属性删除代价见 p08）。
    8. 建成本中心（Configuration 界面主菜单 Specific Telephone Services > 1 > Cost Center）：ID 0=MKT、1=Training、2=TSS（实验口径）。
    9. 建五个用户（右键 Users > Create）：31000 Dupont Jean（Set Type=IPTouch 8068s，Rights 页签 CC ID=0→MKT，另从该用户选 TSC IP User 选项开 IP-Softphone Emulation=YES）；31001 Tregueur Paul（SIP extension，SIP 页签 SIP Passwd=123456，实验口径，CC=0）；31003 Anderson Thomas（SIP extension，CC=1 Training）；31004 Vincent Michel（SIP extension，CC=1）；31005 Williams Pierre（IPTouch 8078s，CC=2 TSS）。
    10. 验证自动落地：Directory 应用 Department 1 下五人全部出现。
    11. UID 防同名（p118-121）：建 31023 Anderson Thomas → Alarms 应用 Alarms 页选 NMC > nms > LDAP server 查看告警 "The entry Anderson Thomas already exists. No automatic creation for link 31023..."；按书提示先删除刚建的 31023；Configuration 应用 ale > abc1 > oxe > Data Collection → UID construction=Extension；重建 31023 → 目录出现 UID "Thomas Anderson 31023"；再建 31024 Anderson Thomas → 出现 "Thomas Anderson 31024"；Data Collection 把 UID construction 改回 None。
    12. 自动继承（p121-122）：Directory 右键 Michel Vincent → Cut → 右键 Department 3 → Paste → 选人员 Organization 页签确认城市/部门已自动更新。
  verification: |
    ①Visio Room 与五用户全部出现在 Department 1；②同名告警出现且改 Extension 后 31023/31024 两个 Thomas Anderson 共存（UID 带分机号后缀）；③Cut/Paste 后 Michel Vincent 组织属性自动更新（p117/p120/p122）。
  conditions: c01 已完成（OXE 已注册同步）；目录树为实验约定结构。
  tags: [lab, automatic-creation, uid, cost-center, inheritance]

- id: c03
  title: 链接管理与四入口改名语义（副链/传真链/多设备链、CC 修改、姓名修改与修复）
  type: lab
  source_pages: p123-155
  source_chapter: Directory Application - Links management（How-To）
  source_quote: |
    "he inherits from the Jean Dupont cost center. Now DECT Dupont cost center is MKT." (p130)
    "After modifications of first name and last name of Paul Tregueur, the primary link between Paul
    Tregueur and the phone 31001 is broken. A new primary link is created between Michel Durand and the
    phone 31001." (p145)
    "Using the Users application, thick or web client, is the best way to update and modify the first name
    and last name of a person. • All links are kept. • Cost center is kept." (p151)
  steps: |
    1. 补建 PCX 用户：31002 Dupont DECT（SIP/DECT 类，CC=1 Training）、31011 Fax Set（CC=2 TSS）；Directory 中删除这两个用户自动生成的人员条目（右键 Delete → Yes）。
    2. 副链（Jean Dupont）：Directory 右键人员 Jean Dupont > Settings links… > Secondary link 页签 > Edit… > OK > Searching new links 窗口 Search → 双击分机 31002 行 → OK → OK。核验：DECT Dupont 的 CC 从 Training 变 MKT（继承主链接）；Configuration Users 文件夹关开刷新查看。
    3. 传真链（Jean Dupont）：Settings links… > Fax link 页签 > Edit… > OK > Search → 双击 31011 → OK → OK。核验：Fax Set CC 仍为 TSS（传真链不改 CC，传真可多人共享）。
    4. 多设备链（Pierre Williams，经 Users 应用）：Users 应用 Users 页签（先刷新树）→ 右键 Pierre Williams > Add a secondary set > Add：OXE directory number=31105，Device type=IPTouch 8068s（IPDSP）；Configuration 界面选用户 31105 → TSC IP user → IP-Softphone Emulation=YES；Directory 中核验 Pierre Williams 出现多设备链接。
    5. 目录侧改 CC（Jean Dupont：MKT→Training）：Directory 选人 > Organization 页签 > Cost center 填 Training → 应用。核验：Jean Dupont 与 DECT Dupont 变 Training，Fax Set 保持 TSS。
    6. 目录侧改未知 CC（Paul Tregueur：MKT→BEAN）：同上填 BEAN → Alarms 应用出现拒绝告警："The PCX SubnetworkNodeNumber=101,... refused modification of the field cost center name with the value BEAN on station 31001."；CC 保持 MKT。
    7. 目录侧改名（Jean Dupont→Albert Simon）：Individual 页签改 Last name=Simon、First name=Albert、Name=Simon Albert、User id=Albert Simon。核验：Configuration 中 31000 的姓名同步更新，全部链接保留。
    8. 配置界面改名（31001 Paul Tregueur→Michel Durand）：Configuration 界面改 Directory name=Durand、Directory First Name=Michel。核验：Paul Tregueur 主链接断裂，新生成人员 Michel Durand 挂 31001——需修复。
    9. 修复（p146-149）：Directory 删除人员 Michel Durand → 右键 Paul Tregueur > Settings links… > Primary link 页签 > Edit… > OK > Search → 双击 31001 → OK → OK；主链接恢复。
    10. Users 应用改名（Michel Vincent→Philippe Martin）：Users 应用 General 页签改 Last name/First name/User ID。核验：全部链接与 CC 保留，Name 选项同步更新（书注：Users 应用是最佳改名入口）。
    11. WBM 改名（Philippe Martin→Michel Vincent；Albert Simon→Jean Dupont）：Web 客户端 https://nms.company.com:8443 → NETWORK MANAGEMENT（adminnmc/Superuser01*，实验口径）→ Department 选人 → 改 Last name/First name/User ID。核验：目录与用户同步更新。
  verification: |
    ①副链 CC 继承、传真链 CC 不变；②未知 CC 被拒并告警；③配置入口改名断链+新人，修复流程成功；④Users/WBM 入口改名链接全保留（p130/p140/p145/p151）。
  conditions: c02 已完成（五用户与目录树就绪）。
  tags: [lab, links, secondary-link, fax-link, multi-device, rename, repair]

- id: c04
  title: LDIF 导入导出（三范围本地导出、服务器调度导出、删除后导入恢复）
  type: lab
  source_pages: p156-169
  source_chapter: Directory application - LDIF import/export（How-To）
  source_quote: |
    "Right click and select Export > Immediate on local drive > Entry / Sublevel… / Branch…" (p157-161)
    "When you export with the 'Branch…' option, all company directory data are exported. This export
    process is the most complete." (p163)
    "the LDIF export file is saved in the following path C:\8770\Client\data\import" (p165)
    "Right click and select Import > Immediate on local drive > Add and modify…" (p168)
  steps: |
    1. Entry 导出：Directory 选 France → 右键 Export > Immediate on local drive > Entry → 选路径、文件名 France_entry_export → Export；记事本打开核验：只含 France 一条。
    2. Sublevel 导出：France → Export > Immediate on local drive > Sublevel… → France_sublevel_export；核验：只含 Brest 与 Colombes。
    3. Branch 导出：France → Export > Immediate on local drive > Branch… → France_branch_export；核验：国家+城市+部门+用户全量（最完整）。
    4. 服务器调度导出：France → Export > Scheduled on server > Entry… → 文件名 France_entry_export_scheduled → Export → 选 Simple job → Continue → Scheduler 窗口选 Now → Apply → Status 页签看执行 → Close。核验：文件出现在服务器 C:\8770\Client\data\import；Scheduler 应用有任务记录（可改排程定期生成）。
    5. 导入恢复：Directory 删除 Department 1（右键 Delete → Yes）→ 选城市 Brest → 右键 Import > Immediate on local drive > Add and modify… → 选 France_branch_export.ldif → Import → 核验 Department 1 恢复。
    6. 恢复默认配置（p169）：删除人员 Michel Durand；Paul Tregueur 主链接重挂 31001；Albert Simon 改回 Jean Dupont。
  verification: |
    三范围导出内容逐一符合定义；调度导出文件落 C:\8770\Client\data\import 且 Scheduler 可查；删除 Department 1 后经 LDIF 导入完整恢复（p163/p165/p168）。
  conditions: c03 已完成（目录含完整人员与链接）。
  tags: [lab, ldif, export, import, backup, scheduler]

- id: c05
  title: Web 目录客户端使用（匿名搜索、UID 认证、属性修改、地址簿、经理/助理链接）
  type: lab
  source_pages: p183-205
  source_chapter: Directory client（How-To）
  source_quote: |
    "Enter the following command, nslookup nms.company.com ... Edit the hosts file from
    C:\Windows\System32\drivers\etc ... 151.1.1.70 nms nms.company.com" (p185-186)
    "Once authenticated, you can modify the information linked to the person and customize its personal
    address book." (p194)
    "The manager of Jean Dupont is Thomas Anderson. ... The assistant of Thomas Anderson is Pierre Williams." (p202/p205)
  steps: |
    1. 前置：cmd 执行 nslookup nms.company.com 核验解析；无 DNS 时编辑 C:\Windows\System32\drivers\etc\hosts 加行 "<8770 IP> nms nms.company.com"。
    2. 启动：浏览器开 https://nms.company.com → 选语言 → 点 Directory consultation 图标进欢迎页。
    3. 匿名搜索（Ale 根）：Browse 页签展开选 Ale → Search 页签类别 Individual(s)（可按 Last name/First name 等属性 + Begin with/Contains 等条件组合，可增删条件）→ Search → Results 页签看全员 → 点 Jean Dupont 在 Detail(s) 页签看属性（可见范围随权限；详情页还有删除/助理列表/经理列表按钮）。
    4. 匿名搜索（Department 1 根）：Browse 选 Ale > France > Brest > Department 1 → Search 选 Individual(s)、Last name、Begin with → 核验只显示 Department 1 人员。
    5. 给 Jean Dupont 设 UID 密码：Directory 应用选人 → Password 填 Superuser01*（实验口径）。
    6. UID 认证：Web 客户端点 Authenticate 图标 → Login=jean dupont / Password=Superuser01* → 认证后可编辑本人属性。
    7. 改属性：搜索 Dupont → 点名字 → Edit 页签 → 加第二邮箱（多值属性加值）、改密码、加照片（Change Photo > Choose File 选 8770 服务器上的图片 > Open > 确认）、Address 填 Prat-Pip → 保存。
    8. 个人地址簿：点 Address Book 图标 > Add entry：Last name=Adore、First name=Ava → 确认；8770 客户端 Directory 应用 Address books 页签核验 jean dupont 地址簿中出现该条目（地址簿名=UID，只显示姓名）。
    9. 经理链接（Jean Dupont 的经理=Thomas Anderson）：先以 adminnmc/Superuser01* 认证 → 搜 dupont → Edit 页签 > Manager Add links 框 → 默认搜索条件搜索 → 选 Thomas Anderson → OK → 确认。
    10. 助理链接（Thomas Anderson 的助理=Pierre Williams）：同法搜 anderson → Assistant Add links → 选 Pierre Williams → 确认。
  verification: |
    匿名只见 Green 条目非个人数据；认证后本人可改属性/照片/地址/地址簿；Jean Dupont 详情页经理=Thomas Anderson、Anderson 详情页助理=Pierre Williams（p194/p202/p205）。
  conditions: c04 已完成（默认目录配置恢复）。
  tags: [lab, web-directory, authentication, address-book, manager, assistant]

- id: c06
  title: 目录保密级别与访问级别矩阵验证（RH 八人 + 五管理员账户）
  type: lab
  source_pages: p217-251
  source_chapter: Directory confidentiality levels（How-To）
  source_quote: |
    "green Superuser01* Green Brest - Guipavas 0298112233 ... admin8770_2 Superuser01* Administration 8770
    Brest - Guipavas 0298112267" (p219)
    "When you consult the web directory in anonymous mode, only the persons with confidentiality level
    green are displayed. The attributes that are displayed are the non-personal data" (p239)
    "With AdminNmc account, you can display, create edit or delete all attributes of all entries." (p251)
  steps: |
    1. 建 RH 部门：Directory 选 Ale 根 → Create > Department，名 RH。
    2. 建八个人员（RH 下右键 Create > Person，Individual 页签填 Last name/Password=Superuser01*（实验口径）/Confidentiality；Personal 页签填 Home telephone 与 Home address=Brest - Guipavas）：green/green2（Green，电话 0298112233/234）、orange/orange2（Orange，2244/245）、red/red2（Red，2255/256）、admin8770/admin8770_2（Administration 8770，2266/267）。
    3. 建五个管理员账户（Security 应用 nmc > 8770 administration > Administrators 右键 Create > Administrator，密码 Superuser01*）：partial_read、total_read、partial_orange_web、partial_red_web、total_red_web。
    4. 授访问级别（Security 应用 nmc > 8770Applications）：Company Directory 下加 partial_read（级别 Partial reading of company directory）与 total_read（Total red of company directory，书中原文如此）；WebDirectory 下加 partial_orange_web（Partial View Orange List）、partial_red_web（Partial View Red List）、total_red_web（Total View Red List）。
    5. 匿名验证（Web 客户端 https://nms.company.com:8443 > DIRECTORY CONSULTATION）：Browse 选 RH → Search Individual(s) + Last name Begins with "*" → 结果仅 green/green2；点 green > All attributes 图标核验只有非个人数据。
    6. Green 人员验证：Authenticate 登录 green → 结果 green/green2 + 本人；本人含 Password/家庭地址/家庭电话（personal data），green2 仅非个人数据。
    7. Orange/Red/Admin8770 人员验证：分别登录 orange（及 orange2/red/red2/admin8770/admin8770_2）→ 结果均为 green、green2 + 本人；本人 personal data 可见。
    8. Web 管理员验证：partial_orange_web → 见 green/green2/orange/orange2（非个人属性）；partial_red_web → 加 red/red2（仍非个人属性）；total_red_web → 同六人但含个人属性；AdminNmc → 八人全见（含 admin8770 级别），全属性，可建删改。
  verification: |
    七类会话的可见人数与属性范围逐一符合 p239-p251 各 Notes 矩阵（匿名=2 绿非个人；人员=2 绿+本人；orange web=4 人；red web=6 人；total red=6 人全属性；AdminNmc=8 人全属性）。
  conditions: 依赖 Security 应用管理员权限；所有口令为实验口径。
  tags: [lab, confidentiality, access-level, security, verification-matrix]

- id: c07
  title: OXE 配置使用公共 SIP 运营商模拟器（外部 SIP 网关 + DID 翻译器）
  type: lab
  source_pages: p265-268
  source_chapter: OXE configuration to use the public SIP carrier simulator（How-To）
  source_quote: |
    "Registration ID pbxN (where N is your POD number) For POD 4: Registration ID= pbx4" (p267)
    "First external number 33210N41000 (where N is your POD Number) For POD 4: First external number=
    33210441000 / First internal number 31000 / Range Size 500" (p268)
    "To make sure that access to public SIP carrier is working, set up some outgoing calls." (p268)
  steps: |
    1. 环境确认：软电话与 OXE↔模拟器 SIP 中继组已预配，只需按 POD 号配外部 SIP 网关。
    2. 配外部 SIP 网关（OXE 配置界面菜单 SIP > SIP Ext Gateway，选 ITSP1_GW1）：Registration ID=pbxN（N=POD 号，实验口径）；Outgoing username=pbxN。
    3. 配 DID 翻译器（Translator > 1 > External Numbering Plan > 1 > Default DID num. translator，右键 Create）：First external number=33210N41000（POD4 即 33210441000）；First internal number=31000；Range Size=500。
    4. 外呼验证：按《SIP Carrier Simulator》文档从 PBX 发起出局呼叫测试。
  verification: |
    外呼到模拟器公共号成功（p268；号码规则见 framework f09）。
  conditions: RLAB 环境；所有号码为实验口径（N=POD 号）。
  tags: [lab, sip-gateway, did-translator, simulator]

- id: c08
  title: Click to Call 交付（DDI 核验、STAP、软电话、前缀规则、属性关联、拨测）
  type: lab
  source_pages: p269-284
  source_chapter: Click To call（How-To）
  source_quote: |
    "STAP - Off hook: automatic call is authorized when the receiver is picked up. - Authorized: ...
    - Forbidden: ... The STAP option can be setup for all types of phones except SIP devices." (p272)
    "Rule to apply Rule for external call: in this case, the call is established with modification of the
    number." (p279)
    "All phone numbers in bold characters are available for STAP call" (p283)
  steps: |
    1. 核验 DDI 翻译器（Configuration 应用 Translator > External Numbering Plan > DDI numbering translator > Default DID num. translator）：First external number=33210441000（POD4，实验口径）/First internal number=31000/Size range=500。
    2. 配前缀取回（选 oxe > PCX 页签）：DID translation usage 按需选 Default/All/List to select/List to exclude（DID translator list 支持 0;2-4;6 语法）；ISDN Prefix list per DID Translator / per Entity 按需分配专属前缀（2-3:33; 9:39 语法）。
    3. 开 ISDN 构造（oxe > Data Collection 页签）：勾 Process ISDN Number。
    4. 用户 STAP（选用户 31000 Jean Dupont > All 页签）：STAP=Authorized（Off hook=摘机发起；Authorized=免提均可；Forbidden=禁止；SIP 话机不支持）。
    5. 核验 DDI 取回（Directory 应用选 Jean Dupont 与 Paul Tregueur）：ISDN 号自动填 33210441000/33210441001（实验口径）。
    6. 软电话：Client PC 启动 IP Desktop Softphone 关联 31000（分机 31000/密码 0000，实验口径）；MicroSIP 分别选 Tregueur-31001、Anderson-31003、Vincent-31004 档位注册上线。
    7. 建外部呼叫规则（Configuration 应用树右键目标层 Network/Subnetwork/PCX > Create > Rule for external call；全网规则建 Network 层、单 OXE 规则建 PCX 层）：Name=Rule for external calls；Prefix to add=00（第一位 0 走主中继组、第二位 0 补齐 DID）；Prefix to delete=33（匹配以 33 开头并删除）。
    8. 建网间规则（右键 > Create > Rule for calls between network）：Name=Rule for network calls；Called number/Destination Subnetwork 二选一（过滤选目标）；Prefix to add=1（ABC 中继组键，实验口径）。
    9. 属性关联（Administration 应用 nmc > Application Configuration > Click to Call）：Extension → Rule to apply=None（分机原样拨）；ISDN number → Rule for external call；Mobile → Rule for external call；Misc 1 → 右键 Click to Call > Create > Prefix management → 选 Misc 1 → 绑 Rule for external call。
    10. 补属性（Directory 选 Paul Tregueur）：Individual 页签 Mobile=33610512345；Miscellaneous 页签 Misc.1=33210412345（他 POD 的号，实验口径）。
    11. 拨测（Web 客户端 https://nms.company.com > DIRECTORY CONSULTATION）：点 Define associated station 图标 → Station No.=31000、Secret code=0000（实验口径）→ 搜 tregueur → Detail(s) 页签中粗体号码（Extension/ISDN/Mobile/Misc 1）点击即发起 STAP 呼叫。
    12. Add-on 演练（p284，读流程）：06 开头走中继组 10、其余走 20 → 两条外部规则；PCX 已有 ARS → 单规则"删空+加 0"。
  verification: |
    Detail(s) 页签出现四个粗体可点号码；点击后 31000 话机按关联发起呼叫到目标号码（p281 五路可点/实测四属性 + p283 粗体可用）。
  conditions: c07 已完成（SIP 运营商可用）；SIP 话机不能作 STAP 主叫。
  tags: [lab, click-to-call, stap, prefix-rule, isdn, dial-test]

- id: c09
  title: 目录词典定制（CustomDict 改名、版本号、三动作保存、回退）
  type: lab
  source_pages: p295-310
  source_chapter: Dictionary customization（How-To）
  source_quote: |
    "Dictionary version number The field has been incremented after the save from the customization tool
    (i.e. 1)." (p303)
    "IF THE OMNIVISTA 8770 CLIENT IS ALREADY RUNNING ON THE SERVER, CHANGES CANNOT BE SAVED SINCE THE
    DICT_USER.ZIP FILE IS CURRENTLY BEING USED. CLOSE THE APPLICATION BEFORE SAVING." (p303)
    "The previous example shows that each time you need to open the Dictionary Customization application
    for directory attributes modification, you always must select the 'LdapAttributes.dict' file from
    C:\8770\Client\dict\." (p309)
  steps: |
    1. 记录当前词典版本号（Administration 应用 nmc > OmniVista 8770 > OmniVista 8770 页签 > Dictionary version number，默认空）。
    2. 关闭服务器上运行中的 8770 客户端（dict_user.zip 占用会导致保存失败）。
    3. 启动工具（8770 服务器 Windows 开始菜单 > OmniVista 8770 > Dictionary customization）→ Open 选 C:\8770\Client\dict 的 LdapAttributes.dict → 语言选 English for US。
    4. 改人员属性名（Dictionary items 列表 + Find 定位）：选 Context information 为空的 Misc.1 → New translation 填 Passport number；同法 Misc.2 → Sport。
    5. Save（三动作：写 C:\8770\dict\user、生成 C:\8770\Locales\dict\user、更新 8770\Client\bin\dict_user.zip）。
    6. 核验版本号 +1；Directory 应用选 Ale > Miscellaneous 页签见新名；Account./traf./VoIP 应用选 Jean Dupont > Properties 见新名；Web 客户端搜 Dupont > Detail(s) 见新名。
    7. 改 PCX 条目属性（p304-305）：选 Miscellaneous 行（上下文=Configuration 应用 PCX 条目页签名）→ Technical data；选 Misc. 1（上下文=PBX 条目属性名）→ Technician name；选 Misc. 2（同上下文）→ Installation date；Save；核验版本号再 +1（实验至 3）；Configuration 应用 PCX 节点出现 Technical data 页签与两个新属性名。
    8. 回退：工具 Open 重新选 LdapAttributes.dict → Edit > Set All to Default → Save → Close；核验全部属性回默认、版本号仍自增。
  verification: |
    每次保存后 Dictionary version number 递增；Directory/Accounting/Web 客户端三处同步显示新译名；Set All to Default 后回默认（p303/p306/p309）。
  conditions: 服务器上 8770 客户端必须先关闭；客户端重连时自动下载新 dict_user.zip（p310）。
  tags: [lab, dictionary, customization, versioning, rollback]

- id: c10
  title: Web 目录客户端定制（备份、参数/过滤器/网格/详情/编辑、主题、用户参数、回退）
  type: lab
  source_pages: p324-348
  source_chapter: Directory client customization（How-To）
  source_quote: |
    "Right click on DirectoryClient option, Select Export > Immediate on local drive > Branch…" (p326)
    "To restore the default setting of the themes, you must replace the folder C:\8770\Client\Themes by
    the saved folder." (p327)
    "Number of lines per page Enter the number of lines per page: 6 / Grid attributes Setup the attributes
    ... Last name – First name – Extension – Department - City" (p333)
  steps: |
    1. 备份默认配置：Administration 应用 nmc > Application Configuration > Application Settings 右键 DirectoryClient > Export > Immediate on local drive > Branch… → Default_web_directory_client.ldif；另拷贝 C:\8770\Client\Themes 整个文件夹到 Documents。
    2. 改全局参数（Application Settings > DirectoryClient > GlobalParameters）：Maximum number of entries in personal address book 500→10；Display define associated station icon 禁用。
    3. 搜索过滤器（Web 客户端管理员 adminnmc 登录 > Search 页签 > Customize 图标 > Default parameters 页签）：为每类搜索对象配过滤属性与 Quick Search 属性条件；等价 Administration 路径 DirectoryClient > SearchClasses（LDAP 属性名，Add a value 加值；对象类型 All_Company/Group/Organization/OrganizationalUnit/Person/Room）。
    4. 网格（Results 页签 Customize > Default parameters）：每页行数=6；Grid attributes=Last name–First name–Extension–Department–City；等价路径 DirectoryClient > Grid > GridAttributes/PrintAttributes；匿名会话核验新网格。
    5. 详情页（Detail(s) 页签 Customize > Default parameters）：Area1=Last name,First name,Title,Mail,Extension,ISDN number；Area2=Building name,Floor,Cost center；Area3=Company,Department,City,State,Country,Employee number；等价路径 DirectoryClient > DetailAttributes（ViewDumpAreas/ViewGroupAreas/ViewOAreas/ViewOuAreas/ViewPersonAreas/ViewRoomAreas 六类对象 × Area）。
    6. 编辑页（Edit 页签 Customize > Default parameters）：按对象/Area 配置可修改属性与照片可改性；等价路径 DetailAttributes > Edit attributes。
    7. 主题（点主题名选 8770WBM > Edit > Browse 上传 c:\8770\Apache2\icons\apache_pb2.gif 替换 Logo，可位左/右/中）→ Save；Custom 主题同法换 Logo + 背景色 pink + 文字色 red。存储：theme1=8770WBM、theme2=Custom（CSS 文件）。
    8. 用户参数（jean dupont 登录 > Results 页签 Customize > User parameters 页签）：行数 5；Grid attributes=Last name–First name–Extension–Title；保存后翻页核验个人视图生效（用户主题选择存 cookie；主题 Edit 仅管理员）。
    9. 回退：Administration 右键 DirectoryClient > Import > Immediate on local drive > Modify only… 导入备份 LDIF；主题恢复=清空 C:\8770\Client\Themes 后粘贴备份内容；核验回默认。
  verification: |
    匿名/认证会话分别显示 6 行新网格与三区详情；用户参数 5 行视图仅对 jean dupont 生效；LDIF 导入 + Themes 替换后全部回默认（p332/p333/p336/p346/p347）。
  conditions: 先做第 1 步备份再动手；管理员账户 adminnmc/Superuser01*（实验口径）。
  tags: [lab, client-customization, theme, grid, backup, restore]

- id: c11
  title: MSAD 服务器声明（AD 侧建管理员、Access info 八字段）
  type: lab
  source_pages: p368-377
  source_chapter: MSAD integration - Server configuration（How-To）
  source_quote: |
    "The user must belong to the domain admins group. ... For French Operating System, enter admins only." (p373-374)
    "Automatic deletion of 8770 users ... (False - default value)" (p377)
    "When applying the changes, the 8770 server makes a LDAP bind request to the MSAD server. The LDAP
    request must be successful to create the entry" (p377)
  steps: |
    1. 实验环境：Ecosystem 实例（eco.company.com / 192.168.1.100，Administrator/superuser，实验口径）作 AD 服务器。
    2. 建管理员（Server Manager > Tools > Active Directory Users and Computers > Users 右键 New > User）：Last name/Full name/User logon name=MSADadmin；密码 Superuser01*（实验口径）；勾 User cannot change password 与 Password never expires。
    3. 授权：右键 MSADadmin > Add to a group… → 填 domain admins（法语系统填 admins du domaine 对应项，书中注 "admins only"）→ Check Names → OK；Properties > Member Of 核验 Domain Admins 在列。
    4. 声明 MSAD（Administration 应用 nmc 右键 MSAD Management > Create > Access info）：Name=MSAD；Host=eco.company.com；Port=389（LDAPS 为 636）；Username=MSADadmin；Password=Superuser01*；Is LDAPS=No（启用需 AD 服务器装 Active Directory Certificate Services 角色发证书）；Automatic deletion of 8770 users=No（False 默认：AD 删人只标记；True：连 OT/OXE/8770 一起永久删）；Scope=o=Ale, o=directoryRoot。
    5. Apply 保存——8770 立即发 LDAP bind 请求，绑定成功才能建条目。
  verification: |
    Access info 条目创建成功（LDAP bind 通过）（p377 Tips）；Member Of 显示 Domain Admins（p375）。
  conditions: AD 服务器为 Windows Server 2016/2019/2022；LDAPS 需先配 AD CS。
  tags: [lab, msad, server-declaration, ldap]

- id: c12
  title: MSAD 属性映射与同步规则（映射一条、附加属性、Flat/Tree、调度与删除行为验证）
  type: lab
  source_pages: p378-393
  source_chapter: MSAD integration - Directory synchronization（How-To）
  source_quote: |
    "Only one Attribute Mapping entry can be created." (p380)
    "Only entries having an Objectclass=user and a name (cn) not empty are selected for the
    synchronization." (p385)
    "If Synchronization mode=flat Only the users are synchronized, not the branches (you must create the
    branches manually)" (p387)
    "Check that user Charlize Cohen is marked as deleted in the 8770 Directory application" (p390)
  steps: |
    1. 建 AD 分支（Ecosystem > Active Directory Users and Computers）：右键 company.com > New > Organizational Unit 建目标 OU 树（勾 Protect container from accidental deletion）。
    2. 建 AD 用户（Marketing 容器下 New > User）：Charlize Cohen 与 Christopher Cane，密码 Superuser01*（实验口径），勾不可改密+永不过期；Charlize 在 Properties > Attribute Editor（看不到先开 View > Advanced features）设 Employee Number=1234。
    3. 建映射（Administration 应用 nmc > MSAD Management 右键 MSAD > Create > Attribute mapping）：Name=Mapping，保持默认值——默认姓/名/显示名/AD 用户 ID/邮件 AD→8770，电话号码 8770→AD。
    4. 加附加属性：Mobile（方向 8770→MSAD，无默认值）；Employee number（方向 MSAD→8770，默认值 1234）。隐藏映射 abObjectGUID←objectGUID 自动存在（唯一性）。
    5. 建规则（右键 MSAD > Create > Synchronization rule）：Name=Synchronization - Colombes；Filter 默认（objectclass=user 且 cn 非空）；8770 Location 选 l=Colombes, c=FR, o=directoryRoot；MSAD Location 选 OU=Colombes, OU=France, DC=company, DC=com；Synchronization mode=Tree；Attribute mapping 自动填 Mapping。
    6. 首次全量（右键规则 > Synchronization > Complete）：核验 8770 目录出现 AD 分支镜像与两人（Tree 模式连分支一起建；Flat 只建人）。
    7. 增量验证：8770 目录给 Charlize Cohen 填 Mobile=0612345678，AD 侧 Attribute Editor 给她 mobile=0687654321 → 右键规则 > Synchronization > Partial → 核验两侧 Mobile=0612345678（8770→AD 方向胜出）。
    8. 删除行为（False 态）：确认 Automatic deletion=False → AD 删 Charlize Cohen → Complete 同步 → 8770 目录中她被标记为删除（marked as deleted）。
    9. 删除行为（True 态）：Access info 把 Automatic deletion 改 True → AD 删 Christopher Cane → Complete 同步 → 8770 目录中他消失。
    10. 重建 Christopher Cane（同第 2 步）供后续实验使用。
    11. Tips（p391-393）：Attribute Editor 不显示时开 View > Advanced features；删除对象报"受保护"时 Properties > Object 页取消 Protect object from accidental deletion。
  verification: |
    Tree 首次全量镜像 AD 结构；Partial 后 Mobile 以 8770 侧值为准双向一致；False 删除=标记、True 删除=消失（p387/p389/p390）。
  conditions: c11 已完成；AD 用户姓/名不可为空（空则不同步）。
  tags: [lab, msad, mapping, sync-rule, tree, deletion]

- id: c13
  title: MSAD 插件部署与从 AD 一键开通 OXE 用户（Meta profile 前置 + properties + 安装 + 开户）
  type: lab
  source_pages: p394-426
  source_chapter: MSAD integration - User Management Web Tool（How-To）
  source_quote: |
    "SYNCHRONIZATION IS REQUIRED TO RETRIEVE THE FREE NUMBER RANGES FROM THE OMNIPCX ENTERPRISE!" (p401)
    "When you customize the MSAD8770Admin account password, you will be asked to restart the NMC Java
    Service Definition service to consider the new password." (p404)
    "If the URL 'nms.company.com' is not a trusted site, the plug-in will display its interface with
    missing fields." (p414)
    "Only the cost center and Salutation field (when available) can be modified." (p425)
  steps: |
    1. 前置-OXE profile（OXE 配置界面右键 Users > Create）：General：Directory number=A0001（占位空闲号）、Set Function=Profile；Profile 页签 Profile Name=BASIC（大写）；Rights：Public Network COS=3、Phone Feature COS=4、Connection COS=5（实验口径）。
    2. 前置-空闲号码段（System > 1 右键 Free Numbers Ranges List > Create）：Name=Range 31050-31059、Range beginning=31050、Range end=31059；同步 OXE（右键 oxe > Synchronization > Partial > Separate）——警告：不同步取不回号码段；Configuration 应用核验段列表。
    3. 前置-Meta profile（Users 应用 Profiles 页签右键 Meta profiles > Create > OXE meta profile）：Meta profile name=OXE meta profile – 8078s；OXE node name=oxe；OXE free number range=Range 31050-31059（开户取段内首个空闲号）；Device type=IP Touch 8078s；OXE profile=BASIC；Key Profiles 按需；OT applications=None（无 OT 服务器）。
    4. 改 MSAD8770Admin 密码（Security 应用 nmc > 8770 administration > Administrators 选 MSAD8770Admin → 密码字段改 Superuser01*，实验口径）→ 按提示重启服务：服务器 Service Manager 选 NMC Java Service Definition → Stop → Refresh 确认重启。
    5. 生成插件配置（Administration 应用 nmc > MSAD Management > MSAD 右键 Mapping > Create > ADPlugin）→ 填 MSAD8770Admin 密码 → OK → 生成 C:\8770\data\msadplugin\MSAD Server\8770MSADPlugin.properties（内含 8770 URL/账户 DN/加密密码/映射 DN/AD 账号）。
    6. 传文件：8770 实例把 Setup.exe、ReadMeFor8770MSADPlugin.txt、8770MSADPlugin.properties 拷到 SHARING 文件夹 → Ecosystem 实例从 SHARING 取出 → %LOCALAPPDATA%（Win+R 输入）粘贴。
    7. 安装：右键 setup.exe > Run as administrator → Next ×2 → Install → Finish；装到 C:\Program Files (x86)\Alcatel-lucent\8770MSADPlugin；注销当前管理员会话。
    8. IE 前提（Ecosystem Internet Explorer）：Tools > Internet Options > Security > Trusted sites > Sites 添加 https://nms.company.com；Advanced 页签勾 Allow active content to run in files on My Computer（IE9 另需开 active scripting）；未加信任站点插件界面会缺字段。
    9. 首次调用装证书：AD 中右键用户（如 Christopher Cane）> Alcatel-Lucent Unified User Management → 证书告警点 Continue → View certificates > Install Certificate… > Current User > 放入 Trusted Root Certification Authorities → 完成。
    10. 开户验证：AD 建 Cesar Ciudad（Marketing 容器，ciudad/Superuser01*，勾不可改密+永不过期）→ 右键 > Alcatel-Lucent Unified User Management → Meta profile 选 OXE meta profile – 8078s → 按需改 Directory number（留空自动取段内首个空闲号）/Device type/Cost center → Create → 确认框显示用户名与号码。
    11. 核验三处：Company Directory 应用出现 Cesar Ciudad 人员+主链接；Users 应用出现用户且 OXE configuration 页签参数齐全。
    12. Add-on（p424-425）：Meta profile 留空 Create=只建目录用户；更新用户仅 Cost center 与 Salutation 可改；Delete 确认后删除；排障看 AD 服务器 %TMP%\start8770webclient.log。
  verification: |
    Create 后确认框显示用户名与分机号；Directory（含主链接）与 Users 应用均可查 Cesar Ciudad（p421-423）。
  conditions: c11/c12 已完成；IE 流程为本书环境强依赖（现代浏览器环境需重估）。
  tags: [lab, msad-plugin, meta-profile, provisioning, certificate]

- id: c14
  title: 管理域搭建（许可、激活、六管理员、三组、六域、密码策略、可见性验证）
  type: lab
  source_pages: p456-476
  source_chapter: Domains for management（How-To）
  source_quote: |
    "Granted licenses Directory and Domain Management are enabled" (p458)
    "Put False to disable reinitialazation of password after first login." (p470)
    "The visibility for local administrator account AdminBrest is restricted to the town Brest. ... The
    option 'Domain configuration' is displayed but inactive for local administrator account AdminBrest." (p472)
  steps: |
    1. 扩目录树（Directory 应用）：加国家 Portugal，城市 Lisbon、Porto，Lisbon 下 Department 4，Porto 下 Department 5、6。
    2. 核许可（主窗口 Help > About）：Directory 与 Domain Management 均已启用（MCS 版自带 Directory，Domain Management 仍需）。
    3. 激活功能（Security 应用 nmc > 8770DomainManagement）：勾 Enable → Apply。
    4. 建六个管理员（Security > 8770 Administration > Administrators 右键 Create > Administrator，密码均 Superuser01*，实验口径）：AdminFrance、AdminBrest、AdminColombes、AdminPortugal、AdminLisbon、AdminPorto。
    5. 归组（nmc > 8770 Administration > Groups）：Users Configuration 加 AdminBrest/Colombes/Lisbon；Users & Directory Configuration 加 AdminPorto；Users & Customization Configuration 加 AdminFrance/Portugal。组语义：①只管用户（Directory 仅 Partial modification）；②+域内目录结构全管；③+定制视图与 Web Admin 的域/账户管理。
    6. 建六域（nmc > 8770 Domain Management 右键 Create > Domain）：FranceDomain（级别=Country France，Member=AdminFrance）；BrestDomain（City Brest）；ColombesDomain（City Colombes）；PortugalDomain（Country Portugal）；LisbonDomain（City Lisbon）；PortoDomain（City Porto）。选级：Search Location 图标 → 字段 Country/City → 搜索选目标；Members 字段 → Search users → Administrator → 选人 → Apply。
    7. 密码策略（Security > Password Policy > Password policy 页签）：Password reset after first login or reset=False。
    8. 可见性验证：分别以 AdminBrest（厚客户端+https://nms.company.com:8443 WBM）登录——目录只见 Brest、仅能管用户、Domain configuration 菜单显示但不可用；AdminPorto 同法（可管域内目录结构）；AdminFrance/AdminPortugal 同法（另可管定制视图）。
  verification: |
    三个组的本地管理员可见范围与可管内容逐组符合 p472/p474/p476 Notes；Domain configuration 对本地管理员显示但 inactive。
  conditions: 双许可就绪；预定义组语义以讲义 p441 + How-To p463-466 为准。
  tags: [lab, domains, local-administrator, groups, license]

- id: c15
  title: 委派与定制视图（Delegation、WBM 建域/视图/本地管理员、开户效率对比）
  type: lab
  source_pages: p477-500
  source_chapter: Delegation and Customized views（How-To）
  source_quote: |
    "Delegation rights provide the possibility for a local administrator to create others local
    administrator accounts." (p479)
    "Custom View Name Enter the name the customzed view (i.e. RennesView)" (p485)
    "The aim of the customized views is to simplify/optimize the user creation process for a local
    administrator." (p495)
  steps: |
    1. 开委派（WBM https://nms.company.com:8443 以 AdminNmc/Superuser01* 登录 > Settings > Administrator configuration）：选 AdminFrance > Application rights 页签 > Delegation 启用。
    2. AdminFrance 登录 WBM 建级别：主界面 Add a level 图标 ×2 → Type=City，Name=Nantes / Rennes。
    3. AdminFrance 建域：Settings > Domain configuration → Domain name=NantesDomain，选级别 Nantes，Add；同法 RennesDomain。
    4. 建定制视图 RennesView（Settings > Customized views > 选预定义 Default View）：User 页签 Show all 关；Main device 页签 OXE name 开、Station type 关（预定义 IPTouch 8078s）、Application 与 Secondary sets 关（0）、其余选项关（Directory number 必填）；ALES-Desktop/ALES-Mobile 页签全关；Details 页签 Dial by name and text msg 关 → Save As → 名称 RennesView。
    5. 建两个本地管理员（AdminFrance 会话 > Settings > Administrator configuration > Admin 页签）：AdminNantes（密码 Superuser01*，Custom view=Default view，Domains=NantesDomain）与 AdminRennes（Custom view=RennesView，Domains=RennesDomain）；Application rights 页签 User 级别选 Directory → Save。
    6. AdminNantes 开户：登录 WBM → Add a level（Type=City，Name=Department 44——实际落在 Nantes 下）→ 选 Department 44 > Add a user：User 页签 Last name=Murphy、First name=Peter；Main device 页签 OXE name=oxe、Directory number=31025、Station type=IPTouch 8078s → Save。
    7. AdminRennes 开户：同法建 Department 35 与用户 Daniel Ash（31026）——RennesView 视图下页签更少、流程更快。
    8. 可见性核验：AdminNantes 在 Directory/Users 应用只见 Peter Murphy；AdminRennes 只见 Daniel Ash；AdminFrance 两人均见；AdminNmc 全见；各人员的 OmniPCX resources 页签主链接已建。
  verification: |
    RennesView 开户步数明显少于 Default view（p495 Notes 明示该对比结论）；四层管理员的可见性边界逐一符合（p490/p493/p496-500）。
  conditions: c14 已完成（域体系就绪）；视图选项开关表见 p484-485。
  tags: [lab, delegation, customized-view, wbm, provisioning]

- id: c16
  title: 目录复制主从部署（Slave 先行、Master 五步、初始化、调度 5:00、移除与恢复）
  type: lab
  source_pages: p517-535
  source_chapter: Company Directory Replication（How-To）
  source_quote: |
    "Don't modify the replication password (default: superuser)." (p520)
    "Initialize action recopies (deletes first all data in the consumer suffix) all the data from the
    Master to Slave server for that sub-suffix." (p531)
    "The consumer replica must be deleted before the Master replica." (p533)
  steps: |
    1. 前置：DNS 有 replication8770.company.com → 151.1.1.71（实验口径）；双机同 OS 语言/同 8770 语言/同版本/双 Directory 许可/同公司名/同 OXE 声明；主从互 ping 计算机名与 FQDN 通；cost center 管理参数一致（Administration > Application Configuration > 8770 master for cost center management，默认 yes）。
    2. Slave 建 Consumer（Slave 服务器 8770 客户端 > Preferences > Administration > Replication configuration）：Sub-suffix 类型选 Country → 选 France → Add → Database name=FR → Add → 选 Consumer suffix → Add。核验：服务器 C:\8770\SunONE\sldap-8770\db\C_FR 数据库目录生成；副本 ID 自动 65535；若根下已有 France 条目须先删（否则报错）。
    3. Slave 配复制管理器密码：运行 toolsOmniVista.exe → 输 directory manager 密码 → y 停服务 → 选 1 Password update → 选 6 LDAP Replication Manager password update → 设置（实验默认不动，=superuser）。
    4. Slave 配 PCX：Configuration 选 oxe——Automatic creation 禁用、Location 不用；Data Collection 的 UID construction 与主机一致。
    5. Master 导出结构：Company Directory 选根 ALE → Export > Immediate on local drive > Branch… 存 LDIF → 删除 France 分支（复制建副本要求分支为空；非空流程=导 LDIF→删→建副本→配协议→导回→初始化）。
    6. Master 建 Master replica（Preferences > Administration > Replication configuration）：Country → France → Add → FR → Add → 选 Master suffix → 副本 ID 填 1（1-65534 且未占用）→ Add。
    7. Master 配协议（Replication agreement 区 Add）：Host: Port=从机 IP/FQDN+LDAP 端口（LDAPS 不支持）；Replication manager password=从机复制管理器密码；点 Click to Edit 定义属性集（实验：Replicate all 启用）；勾启用协议 → OK。
    8. Master 导回结构：Company Directory 选 ALE → Import > Immediate on local drive > Add and modify… 选第 5 步 LDIF → Import → 关开应用核验。
    9. Master 配 PCX：若主副本作自动创建位置，配置 Location 到主副本并同步节点触发；Mobile/Employee number/Title 可补填；UID 构造双机一致。
    10. 初始化（Replication configuration > Replication agreement 选协议行 > Initialize）：核验 Slave 上 Consumer suffix 数据出现；思考题核验 Mobile/Employee number/Title 值。
    11. 调度（选协议 > Schedule > Simple job > Continue > Start Date=As Scheduled，每日 5:00AM）→ OK；Scheduler 应用核验任务（可右键 Execute now 手动触发）。
    12. 复制过程验证（p533）：Master 加 P1 → 未调度前 Consumer 无 P1；Consumer 加 P2 → 经 referral 转 Master；Scheduler 右键 replication job > Execute now → Consumer 更新。
    13. 移除（先从后主）：Slave 删 Consumer suffix；Master 删协议（先禁 Replicate all）→ 删 Master suffix；注意删 suffix 会连带删目录分支与 LDAP 数据库。
    14. 数据不一致恢复（p535，>7 天场景）：Master 导出主副本分支 LDIF → Master 禁用协议 → Slave 删 Consumer → Slave 重建 Consumer → Slave 导入 LDIF → Master 重新启用协议。
  verification: |
    初始化成功提示 + Slave 端目录结构完整复制；Execute now 后 Master 新增人员出现在 Slave；移除后双机分支与数据库同步清除（p530-535）。
  conditions: 从机断联 >7 天将丢主侧断联期数据（LDIF 人工恢复）；属性集建协议后不可改。
  tags: [lab, replication, master-slave, initialize, schedule, recovery]

- id: c17
  title: LDIF 管理工具实战（CSV 管道导入、链接计算、删除跟随、导出、Domino 管道）
  type: lab
  source_pages: p552-558
  source_chapter: LDIF Management Tools（How-To，实验任务书形态）
  source_quote: |
    "The go.bat file contains the commands Csv2Ldif, ConvertLdif and ImportLdap. These commands use the
    different .conf files." (p553)
    "THE COMPANY DIRECTORY ROOT NAME MODIFICATION IS VERY IMPORTANT !!! IF YOU FORGET SUCH MODIFICATION
    AND RUN THE GO.BAT FILE, A BAD STRUCTURE WILL BE CREATED ... YOU WILL HAVE TO CONNECT TO 8770 SERVER
    VIA DIRMANAG.EXE APPLICATION AND DELETE THE ROOT 'ABS'." (p555)
    "This file allows creating the assistant, manager and see also link. It uses the link.conf file." (p553)
  steps: |
    1. 取材：解压 LDIF1.zip 到 c:\ldif1（directoryUS.xls/.txt 数据采集 + go.bat/link.bat/purge.bat/export.bat 与各 .conf）。
    2. 编辑 go.bat：读 Csv2Ldif/ConvertLdif/ImportLdap 三命令说明；ImportLdap 参数按本机改（服务器名、adminnmc DN、密码）。
    3. Csv2Ldif 环节：确认列分隔符与多值分隔符；执行后开 tmp.ldif 看结构与 Paul Martin 的 Address 值。
    4. ConvertLdif 环节：研读 mc.conf（person 所需 objectclass）、ma.conf（Last name 处理、修改日期处理）、da.conf（uid/cn/mail 的构造式、7bit 选项用途）、p.conf（把 o=abs 改成本客户根名——高危步骤，见引文警告）；执行转换后核验 result.ldif 的 uid/cn/mail、国家与部门、修改日期已删。
    5. ImportLdap 执行：导入后核验公司目录树成形。
    6. link.bat 链接计算：数据采集里 Misc4=助理电话号码、Misc5=经理电话号码；读 link.conf 理解 assistant/manager 链构造；改 link.bat（根名、服务器名、DN 密码）；执行；分析 Durand Martin 报错原因；核验 Martin Paul 的 assistant 与 see also 链、Jesequel Albert 与 Bellec Jean 的 manager 链。
    7. purge.bat 删除跟随：da.conf 的 misc10 值与 purgefilter.conf 的过滤逻辑；删 directoryUS.txt 中 Smith David 行（模拟外部删除）→ 跑 go.bat → 查 purgefilter.conf 与 misc10 变化 → 跑 purge.bat → 核验 Smith David 从公司目录消失。
    8. export.bat 导出：改根名/服务器名/DN 密码 → 执行 → 开 export.ldif 与 export.txt。
    9. Domino 管道（Part 6）：向讲师取 LDIF2.zip 解到 C:\LDIF2 → 改 domino.bat（根名/服务器名/DN 密码）→ 按 .conf 头部说明逐个改 → 执行 → 核验目录树更新。
  verification: |
    go.bat 三连后目录树按采集数据成形；link.bat 产出 assistant/manager/see also 链；purge.bat 删掉外部已删条目；export 产出 LDIF/TXT 双格式；domino 管道导入成功（p556-558 各任务验收问题）。
  conditions: p.conf 根名忘改会产生坏结构且重跑无效——须 dirmanag.exe 删 ABS 根后重来（书中大写警告）。
  tags: [lab, ldif-tools, batch, linkdn, purge, domino]
```

---

## 任务覆盖自检（task↔id 映射）

| task | 对应 case 条目 |
|---|---|
| task-01 OXE 注册同步 | c01 |
| task-02/03/04/05 树+自动创建+UID+继承 | c02 |
| task-06/07/08/09 链接与改名 | c03 |
| task-10 LDIF 导入导出 | c04 |
| task-11 Web 客户端使用 | c05 |
| task-12 保密级别 | c06 |
| task-13 SIP 运营商配置 | c07 |
| task-14 Click to Call | c08 |
| task-15 词典定制 | c09 |
| task-16 客户端定制 | c10 |
| task-17 MSAD 声明 | c11 |
| task-18 MSAD 同步 | c12 |
| task-19 MSAD 插件 | c13 |
| task-20 管理域 | c14 |
| task-21 委派与定制视图 | c15 |
| task-22 目录复制 | c16 |
| task-23 LDIF 工具 | c17 |

17 个 How-To 章全部覆盖，无遗漏、无合并遗漏（书中共 17 个 How-To，本文件 17 条一一对应）。
