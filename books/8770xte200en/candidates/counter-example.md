# 反例/限制/边界/易错点候选 — OmniVista 8770 (8770XTE200EN Ed47)

> 提取器: counter-example-extractor（全量扫描，逐页核对 Warning/Note/Limits） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: 服务器必须独占——8770 不能与其他应用混装
  type: limitation
  source_pages: p55
  source_chapter: SERVER INSTALLATION / Operating Systems requirements
  source_quote: |
    "The OmniVista 8770 Server must be installed on a dedicated server" (p55)
  summary: |
    8770 服务器（含其内嵌的 MariaDB、LDAP、Apache/Wildfly 全栈）必须独占一台 Windows 服务器/虚机。
    规划资源时不能按"再挤一个应用"估算，容量与补丁窗口都要按专用机对待。
  conditions: 一切安装场景
  tags: [limitation, installation, sizing]

- id: n02
  title: 虚拟化免 8770 许可，但 hypervisor 互补服务可能另收费
  type: limitation
  source_pages: p8
  source_chapter: SOLUTION OVERVIEW / Virtualization
  source_quote: |
    "No OmniVista 8770 license for virtualization ... According to the different hypervisors, some
    complementary services may require additional license costs" (p8)
  summary: |
    "虚拟化不要 8770 许可"成立，但 VMware/Hyper-V/Nutanix/AWS 侧的高可用、备份等互补特性可能产生
    第三方许可成本——报价时要把 hypervisor 侧成本算进去，别只看 ALE 价目。
  conditions: 虚拟化/云端部署选型
  tags: [limitation, virtualization, licensing]

- id: n03
  title: OXE Purple 代次与 8770 版本强绑定——N3/N4/N5 仅 R5.2 支持
  type: version-trap
  source_pages: p9
  source_chapter: SOLUTION OVERVIEW / Cross compatibility
  source_quote: |
    "OXE Purple R100 (N1) X X X / OXE Purple R100.1 (N2) X X / OXE Purple R101.0 (N3), R101.1 (N4)
    & R101.2 (N5) X" (p9)
  summary: |
    升级陷阱：OXE 升到 Purple R101.x（N3-N5）后，8770 只有 R5.2 能管；反之老 8770（R4.2/R5.0/R5.1）
    管不了新 OXE。OXO Connect/OCE R5.2-6.2 同样只有 R5.1/R5.2 支持。升级两侧必须联动规划，先查此表
    再动版本。
  conditions: 任何 OXE/OXO 或 8770 升级项目
  tags: [version-trap, compatibility, upgrade]

- id: n04
  title: 话务分析仅支持 OXE
  type: limitation
  source_pages: p29
  source_chapter: REPORTING SUITE / Account./Traf./VoIP (TRAFFIC ANALYSIS)
  source_quote: |
    "Traffic analysis reports ... Limits: Only for OmniPCX Enterprise" (p29)
  summary: |
    话务分析（Traffic Analysis）功能明确只支持 OmniPCX Enterprise——OXO Connect 站点做话务容量评估
    时此应用不可用，只有 OXO 的 VoIP 报告（经 Reports 应用）可参考。
  conditions: OXO Connect 站点报表规划
  tags: [limitation, reports, oxo]

- id: n05
  title: OXE SIP 话机不能用 Click to Call
  type: limitation
  source_pages: p33
  source_chapter: DIRECTORY SUITE / Web Directory Client
  source_quote: |
    "Click to Call > Automatic dialing from the directory client (for OXE users) ... Limits: OXE SIP
    phones can't use the Click to Call feature" (p33)
  summary: |
    Web Directory 的点击外呼只对传统 OXE 话机生效，OXE SIP 话机被明确排除。给客户演示"目录点击呼叫"
    前先确认终端型号，SIP 话机现场会直接落空。
  conditions: 目录客户端功能演示与部署
  tags: [limitation, directory, sip-phones]

- id: n06
  title: WBM Configuration 三条硬限制——本地管理员无权 / 无 SSH/Telnet 直连 / 单节点连接
  type: limitation
  source_pages: p36, p153
  source_chapter: 8770 WBM CONFIGURATION APPLICATION
  source_quote: |
    "No access to Configuration for local admin. No OT and no OXE direct access via SSH/Telnet.
    Networks, subnetworks and nodes managed from the think client. Connection to one OXE node at
    a time" (p36)
  summary: |
    WBM 的 Configuration 应用是"看图"级：本地管理员无配置权限、不能经 WBM 直连 OT/OXE 的 SSH/Telnet、
    一次只能连一个 OXE 节点；网络/子网/节点本体管理仍在 thick client。别把 WBM 当成可替代厚客户端的
    全能配置端。
  conditions: WBM 部署与权限规划
  tags: [limitation, wbm, configuration]

- id: n07
  title: 计算机名硬规则——<15 字符、字母开头、11 类禁用字符
  type: warning
  source_pages: p67
  source_chapter: Server installation / Notes> Computer name
  source_quote: |
    "It must: - Be less than 15 characters - Start with a letter - Not include characters such as
    / \ [ ] \" : ; | < > + = , ? * . _" (p67)
  summary: |
    8770 服务器计算机名违反任一规则都会给后续 FQDN/LDAP 埋雷；下划线与点也在禁用列表（比 Windows
    本身更严）。改名走 Settings > System > About > Rename this PC (advanced)，改后必须重启。
  conditions: 安装前命名阶段
  tags: [warning, naming, installation]

- id: n08
  title: 禁止从网络盘 / iso 挂载 / vSphere 直接安装 8770
  type: warning
  source_pages: p69, p623
  source_chapter: Server installation / Prerequisites
  source_quote: |
    "If installation is made from an iso image, copy the iso file on the server hard disk (in
    C:\soft for example). Do not install the 8770 server from the network, from an iso mount, or
    via vSphere!" (p69)
  summary: |
    安装源必须先落到服务器本地硬盘再运行 ServerSetup.exe——网络路径、虚拟挂载光驱、vSphere 客户端
    直接跑安装都在禁止之列（安装中断/文件锁风险）。虚机环境先把 iso 拷进 C 盘。
  conditions: 物理机与虚机安装均适用
  tags: [warning, installation]

- id: n09
  title: 安装期"不可回改"参数清单（公司名/成本中心/端口/目录管理器登录）
  type: warning
  source_pages: p77
  source_chapter: Server installation / Notes
  source_quote: |
    "Company information: This name cannot be changed after installation. ... The HTTP and HTTPS
    ports can't be modified for compatibilities reasons. ... Do not modify the directory manager
    login or installation may fail. ... This parameter cannot be modified after server
    installation." (p77)
  summary: |
    装后不可改项：公司名（目录树根显示）、PCX 成本中心方式（选 No 才能用 >10 字符成本中心名）、
    HTTP(80)/HTTPS(8443) 端口、目录管理器登录名（改名直接安装失败）。装错这些只能重装——安装向导
    每一步都要对照客户参数表再点 Next。
  conditions: 服务器安装向导执行中
  tags: [warning, installation, parameters]

- id: n10
  title: R5.2 起 wildcard 证书被替换为自动生成证书（设备管理）
  type: version-trap
  source_pages: p77
  source_chapter: Server installation / Notes — Server certificate
  source_quote: |
    "Until release R5.1, a wildcard certificate was setup by default ... From release R5.2, the
    wildcard certificate has been replaced by an autogenerated OV8770 server certificate ... to
    correct some vulnerabilities reported by many security audits." (p77)
  summary: |
    R5.1 及以前装完默认给 wildcard 证书，R5.2 改为自动生成的 OV8770 服务器证书（修复安全审计漏洞），
    SIP 设备安全部署的签名/下发流程不变但证书不同。从老版本升级或与客户 PKI 对接时走
    ToolsOmniVista.exe 换客户证书。
  conditions: R5.2 新装/升级、SIP 设备安全部署
  tags: [version-trap, certificate, security]

- id: n11
  title: IE ESC 关闭 + Defender 排除 C:\8770 是 Alarms/Topology 启用前提
  type: warning
  source_pages: p80-83, p634-637
  source_chapter: Server installation / Windows management before using OmniVista 8770
  source_quote: |
    "Both Windows managements are required to enable Alarms and Topology applications." (p83)
  summary: |
    装完 8770 后两项 Windows 管理是硬前提：IE 增强安全配置对 Administrators 和 Users 都设 Off；
    Windows Defender 排除项加 C:\8770 文件夹。漏做时 Alarms/Topology 收不到告警——这类"应用无数据"
    现象先查这两项再查网络。
  conditions: 2022 与 2019 章口径一致
  tags: [warning, windows, alarms, topology]

- id: n12
  title: Windows 11 22H2 起 WMIC 被弃用——8770 客户端前置
  type: version-trap
  source_pages: p86, p104
  source_chapter: Server installation / Client installation — Appendix WMIC
  source_quote: |
    "In Windows 11 build 22572 (22H2), WMIC utility (command line interface), used to run 8770
    client application, is now deprecated. As prerequisite, WMIC utility must be installed as an
    optional feature." (p104)
  summary: |
    Win11 build 22572（22H2）起 WMIC 不预装，而 8770 客户端运行依赖它——客户端装完打不开先查
    Settings > System > Optional features 里 WMIC 是否已装回。2022 服务器安装章有此附录，2019 章
    没有（对应其更早的基线）。
  conditions: Windows 11 客户端
  tags: [version-trap, client, windows11]

- id: n13
  title: 客户端安装需本地管理员 + 下载 URL 大小写敏感
  type: warning
  source_pages: p98-99
  source_chapter: Client installation / Prerequisites & Retrieve the Installation file
  source_quote: |
    "Warning: Ensure the Windows account used for the installation has administrator privilege
    (local administrator account)." (p98)
    "Be careful, the URL is case sensitive!" (p99)
  summary: |
    两条易翻车点：普通域用户跑 ClientSetup/OmniVista8770Client 安装会失败（需本地管理员）；从
    https://<FQDN>/cgi-bin/OmniVista8770Client.exe 下载时路径大小写敏感，手敲改写会 404。
  conditions: 客户端分发与安装
  tags: [warning, client, installation]

- id: n14
  title: 客户端首连被 Defender 防火墙拦 Zulu Platform x32 模块
  type: warning
  source_pages: p102
  source_chapter: Client installation / Accessing to the OmniVista 8770 Server
  source_quote: |
    "By default, Windows Defender firewall blocks the access Zulu Platform x32 Architecture module.
    Such module is involved on the running mode of the OmniVista 8770 client. You must allow the
    access to the module in private networks." (p102)
  summary: |
    客户端首次启动弹出的"Zulu Platform x32 Architecture"防火墙告警必须放行（专用网络），否则客户端
    连不上 636 端口。批量铺客户端时可提前组策略放行该模块。
  conditions: 客户端首次连接
  tags: [warning, client, firewall]

- id: n15
  title: 全参导出的用户文件不能直接用于导入；改户必须带 UID
  type: limitation
  source_pages: p214
  source_chapter: Mass provisioning / Export-Import user data function principle
  source_quote: |
    "No use to import a file with full header. UID used to identify user(s) to be modified" (p214)
  summary: |
    两种导出用途要分清：全参导出（全表头）用于参数修改且定位靠 UID——但"全表头文件直接再导入"是
    无效操作；批量新建要用"用户模板导出"（部分表头+优化键值）。拿错模板是批量导入失败的常见首因。
  conditions: Users 应用批量开通
  tags: [limitation, mass-provisioning]

- id: n16
  title: WBM 批量三红线——不能移除设备 / 不能移除 OT 应用 / 与厚客户端文件互不通用
  type: limitation
  source_pages: p250
  source_chapter: Users provisioning from 8770 WBM client / Content update
  source_quote: |
    "Can't remove devices from users. Can't remove OT applications from Connection users. Mass
    provisioning file generated from thick client cannot be used in WebAdmin and vice-et-versa" (p250)
  summary: |
    WBM 批量只能"加"和"改"：不能从用户移除设备、不能移除 Connection 用户的 OT 应用；thick client
    与 WBM 的批量文件格式互不通用——两边倒换文件必失败。需要"减"操作回厚客户端做。
  conditions: WBM 用户批量管理
  tags: [limitation, wbm, mass-provisioning]

- id: n17
  title: WBM 每用户最多 4 个设备页签（软终端计入上限）
  type: limitation
  source_pages: p240-241
  source_chapter: Users provisioning from 8770 WBM client / Multi-devices management
  source_quote: |
    "Device tab available once added. 4 Devices tabs maximum ... ALES-Desktop and ALES-Mobile tabs
    available once selected. Included on the 4 Devices tabs maximum limit" (p240-241)
  summary: |
    WBM 建户的设备页签上限 4 个，且 ALES-Desktop/ALES-Mobile 软终端页签一并计入——"4 话机+2 软终端"
    的组合在 WBM 里配不出来，超四设备场景回 thick client。
  conditions: WBM 多终端用户
  tags: [limitation, wbm, devices]

- id: n18
  title: WBM secretCode 填 NULL 会生成默认密码 1234
  type: warning
  source_pages: p259
  source_chapter: User provisioning from 8770 WBM client / Exported file to be updated
  source_quote: |
    "secretCode@details Replace the starts string by NULL. After importing the updated file, the
    new user will be created with a default secret code (i.e. 1234)" (p259)
  summary: |
    WBM 批量建户时把导出文件中的密码串改成 NULL，新用户会带默认密码 1234 上线——批量开通后必须立刻
    走改密流程，否则批量账户都是弱口令。安全审计必查项。
  conditions: WBM 批量建户
  tags: [warning, mass-provisioning, security]

- id: n19
  title: 相关/非相关告警处置规则——只有非相关可手动清除，确认不等于关闭
  type: misconception
  source_pages: p277-279
  source_chapter: Alarms application / Types of alarm & Alarms customization
  source_quote: |
    "Correlated alarm: When the end of the problem can be detected by the PCX ... Uncorrelated
    alarm: Correction must be performed manually by the user. ... Only active alarms can be
    acknowledged. Once acknowledged, alarm still active. ... Only uncorrelated alarms may be
    cleared." (p277-279)
  summary: |
    两个高频误区：①"确认告警=处理完"——确认只是标记"有人在管"，告警仍活动；②"手动清除相关告警"——
    相关告警由 PCX 自动清，手动清除入口只对非相关告警开放。值机流程要按这两条设计，否则会出现
    "清不掉"或"以为清了"的假象。
  conditions: 告警日常运维
  tags: [misconception, alarms]

- id: n20
  title: 事件 #1125 可能不在默认事件表——须先创建再设 Network incident
  type: limitation
  source_pages: p287-288
  source_chapter: Alarms application - OXE / Configuring incident filter
  source_quote: |
    "In some databases, incident #1125 is not listed in the incident filter by default. To manage
    the sending, it needs to be declared first before network incident can be set to 'Yes'." (p287)
  summary: |
    给特定事件号（如 mtcl 登录 #1125）配 Incident Filter 时，部分 OXE 数据库里该事件不在 Incident
    Number 下拉中——要先右键 Create 把事件补进列表，才能设 Network incident=YES。直接找下拉找不到
    不是故障。
  conditions: OXE 定向告警上送
  tags: [limitation, alarms, oxe]

- id: n21
  title: SNMP hypervisor 声明禁用 FQDN；Windows SNMP 服务必须装（即使被停用）
  type: warning
  source_pages: p308, p313, p317
  source_chapter: Alarms application – SNMP proxy
  source_quote: |
    "IP Address Enter the IP address of the SNMP hypervisor ... Do not use FQDN." (p313)
    "Windows SNMP service must be installed, even if you have to disable it to activate the one
    provided by the 8770 server." (p317)
  summary: |
    两条反直觉规则：①hypervisor 地址只能填 IP（填 FQDN 解析不可靠）；②启用 8770 自带 SNMP 代理后
    Windows SNMP 服务会被停用，但该 Windows 功能不能卸载——Netsnmp 组件归属于它。卸载 Windows SNMP
    功能等于拆掉 8770 代理的地基。
  conditions: SNMP Proxy 部署与排障
  tags: [warning, snmp]

- id: n22
  title: Topology 只显示相关告警；OXE R11.2 起 IP 话机状态告警（#386）不可相关
  type: version-trap
  source_pages: p24, p327, p361
  source_chapter: TOPOLOGY APPLICATION / Limits & Customized view Warning
  source_quote: |
    "Limits: Only correlative alarms are displayed" (p24)
    "FROM RELEASE R11.2 OF THE OMNIPCX ENTERPRISE, ALARM LINKED TO IP PHONE STATUS (INCIDENT 386)
    IS NOT CONSIDERED AS CORRELABLE. SO THEY CANNOT BE USED ANYMORE IN TOPOLOGY APPLICATION." (p361)
  summary: |
    Topology 拓扑图上只画相关告警——客户问"话机故障怎么不在地图上闪"时，先解释机制：OXE R11.2 起
    IP 话机状态事件 #386 不再可相关，天然上不了 Topology；话机级监控走 Alarms 应用。
  conditions: Topology 视图规划与客户期望管理
  tags: [version-trap, topology, alarms]

- id: n23
  title: Topology 两处"改完要重启"——Read saved configuration 与虚拟 ACT 显示
  type: warning
  source_pages: p335-336
  source_chapter: Topology application – Standard view
  source_quote: |
    "Note that a modification of the Read saved configuration option requires restarting the
    topology application." (p335)
    "Virtual Equipment Deselect the Virtual equipment to display it in the Topology. Restart the
    Topology application to apply the modification." (p336)
  summary: |
    Topology 的设置改动不即时生效：改 Read Saved Configuration（启动视图选择）要重启 Topology 应用；
    让虚拟 ACT 上图要回 Configuration 取消 Virtual equipment 勾选后同样重启 Topology。"改了没反应"
    先重启应用再排障。
  conditions: Topology 标准视图配置
  tags: [warning, topology]

- id: n24
  title: 自定义背景地图要放指定目录并重启 NMC Service Manager
  type: warning
  source_pages: p337
  source_chapter: Topology application – Standard view / Adding a background image
  source_quote: |
    "Such maps, in a gif format (for example) with the standard size of 1100x793, have to be stored
    on 8770\data\topology\maps. After copying them into this folder location and restarting NMC
    Service Manager, the dropdown list in the topology application displays them." (p337)
  summary: |
    客户要用自己的园区图/区域图做背景：gif（建议 1100×793）放 8770\data\topology\maps 后必须重启
    NMC Service Manager 才会出现在下拉列表——只拷文件不重启，下拉里永远没有。
  conditions: Topology 自定义地图
  tags: [warning, topology, maps]

- id: n25
  title: 密码时效公式 B+C<A 违反即配置失效
  type: warning
  source_pages: p385
  source_chapter: Security Application / Configuring the password policy
  source_quote: |
    "When configuring password aging, respect the rule (B) + (C) < (A)" (p385)
  summary: |
    密码时效三参数必须满足：提前警告天数(B) + 最短改密间隔(C) < 有效期(A)。客户安全部给的策略数值
    （如 A=90/B=30/C=30）代入验算再录入——B+C≥A 的组合会让告警与改密窗口逻辑失效。
  conditions: 密码策略配置
  tags: [warning, password-policy]

- id: n26
  title: ToolsOmniVista 不校验 8770 密码策略；非正常退出服务不重启
  type: warning
  source_pages: p390-391, p396
  source_chapter: Security Application / Resetting with ToolsOmniVista.exe
  source_quote: |
    "IF THE TOOSLOMNIVISTA.EXE APPLICATION IS NOT QUIT PROPERLY, THE NMC SERVICES ARE NOT RESTARTED
    AUTOMATICALLY! THE TOOLSOMNIVISTA.EXE APPLICATION DOES NOT CHECK ANY PASSWORD COMPLIANCE
    REGARDING THE PASSWORD POLICY RULES OF OMNIVISTA (HISTORY, LENGTH ETC.)" (p391)
  summary: |
    救援工具两把刀：①用选项 1→1 改的密码不经过 8770 密码策略校验——能设出策略禁止的弱密码；②必须
    按 0 逐级退出，直接叉掉窗口则全部 NMC 服务停在停止态（现场表现为"改个密码全站失联"）。改完
    密码记得主动核对新密码符合策略。
  conditions: 账户解锁/密码救援场景
  tags: [warning, toolsomnivista, passwords]

- id: n27
  title: 组权限取最高——多组成员变相提权
  type: warning
  source_pages: p374, p398
  source_chapter: Security application / Predefined access profiles & Notes
  source_quote: |
    "Principle: Sum of rights applied to administrator account" (p374)
    "An administrator account can belong to several groups. For each application, the highest
    access level found is used (can be attributed to a group or to the user itself)." (p398)
  summary: |
    账户在多组时按应用取最高访问级（组或个人都可以是来源）——把人临时拉进高权组"帮个忙"后忘记移出，
    权限就永久留在了最高档。权限审计要按"账户→全部组→最高级"聚合口径查，不能只看个人配置。
  conditions: 权限设计与审计
  tags: [warning, security, groups]

- id: n28
  title: OXE Access Profile 全局共用——改一个等于改所有 OXE；要用最新版本 OXE 编辑
  type: warning
  source_pages: p399
  source_chapter: Security Application / Configuring OXE Access Profiles
  source_quote: |
    "Because Access Profiles are common for all OmniPCX Enterprise, work with the OmniPCX
    Enterprise running the latest release to include the greatest number of attributes and objects." (p399)
  summary: |
    11 个 Access Profile 不是每台 OXE 一份，而是全体 OXE 共用一套：在老 OXE 上编辑会缺新属性；在测试
    OXE 上改 profile 9 会直接影响生产 OXE 的可见性。编辑入口固定选最新版本的 OXE，变更走流程评审。
  conditions: 多 OXE 站点权限管理
  tags: [warning, access-profile]

- id: n29
  title: 改 Access Profile 后必须删客户端本地 MIB 才生效
  type: warning
  source_pages: p402
  source_chapter: Security Application / Updating local MIB
  source_quote: |
    "After managing access profiles, you must delete the OmniPCX Enterprise MIB saved locally on
    the client PC to reload the MIB (i.e. to take into account the modification of access profiles)." (p402)
  summary: |
    权限改完"没变化"的经典原因：客户端本地缓存了旧 MIB。路径：Configuration 界面 Preferences >
    Configuration > Object Model Save > List > 选中本地 MIB 版本 > Delete，重连后按新 profile 重载。
    远程排障时先问一句"本地 MIB 删过没"。
  conditions: Access Profile 变更后
  tags: [warning, access-profile, mib]

- id: n30
  title: OXE 侧访问白名单前提——Secure access for system management 未开则控制不生效
  type: warning
  source_pages: p408
  source_chapter: Security Application / OmniPCX Enterprise access control management
  source_quote: |
    "The Secure access for system management option must be set up to enable OXE control access." (p408)
  summary: |
    User Access Control 白名单建完却不拦人？先查 OXE Connectivity 页的 Secure access for system
    management 是否勾选——它是该功能总开关。开启后还要断开 8770 会话重连才生效（会话级缓存）。
  conditions: OXE 配置访问收敛
  tags: [warning, access-control, oxe]

- id: n31
  title: POODLE/禁 SSLv3 的全网元前提——任一网元不支持 TLS 就不能关 SSLv3
  type: warning
  source_pages: p414-415
  source_chapter: Security Application / ADD-ON: POODLE Vulnerability
  source_quote: |
    "ALL THE NETWORK ELEMENTS IN THE INFRASTRUCTURE (OMNIPCX ENTERPRISE, OMNIPCX OFFICE, OPENTOUCH,
    SIP SETS, ACTIVE DIRECTORY, MAIL SERVER, …) MUST BE TLS COMPATIBLE. IF NOT, IT WON'T BE POSSIBLE
    TO DISABLE THE SUPPORT OF THE SSL V3 PROTOCOL FROM THE OMNIVISTA 8770 SERVER." (p414)
  summary: |
    在 8770 上把最低协议提到 TLS 1.3 前，必须确认 OXE/OXO/OpenTouch/SIP 话机/AD/邮件服务器全部 TLS
    兼容——任一老网元只支持 SSLv3，关掉后它就失联。先做协议摸底再动开关（该流程书中标注"仅供信息、
    勿执行"，生产执行要单独立项）。
  conditions: TLS 加固项目
  tags: [warning, tls, security]

- id: n32
  title: Audit 的 System 页默认搜索条件无效——要用 PbxName Not Empty
  type: limitation
  source_pages: p431
  source_chapter: Audit Application / System tab
  source_quote: |
    "The search options set up by default don't work. Erase all search entries and create the
    following entry: PbxName Not Empty" (p431)
  summary: |
    Audit 应用 System 页开箱默认的搜索条件查不出数据（教材原文确认"don't work"），要先清空全部默认
    条目再手工建 PbxName Not Empty。这是产品行为不是故障，排障别在这里空转。
  conditions: 审计系统操作查询
  tags: [limitation, audit]

- id: n33
  title: Audit 仅支持 OXE；导出功能不适用于 8770 自身日志
  type: limitation
  source_pages: p25, p418, p433
  source_chapter: AUDIT APPLICATION / Limits & Exporting Audit information
  source_quote: |
    "Limits: Only for OmniPCX Enterprise" (p418)
    "Warning: THIS PART DOES NOT APPLY FOR THE AUDIT INFORMATION ON OMNIVISTA 8770 LOGS" (p433)
  summary: |
    审计对象双边界：①只审计 OXE（OXO/OpenTouch 的管理操作不进 Audit 应用）；②右键导出只对 OXE 审计
    数据有效——8770 自身 log（客户端登录等）不在导出范围。客户要 OXO 操作审计时明确告知此边界。
  conditions: 审计方案设计
  tags: [limitation, audit]

- id: n34
  title: 告警报告含 Signature/Action 但不含 Remark；字典改完要重启服务链
  type: warning
  source_pages: p295-297
  source_chapter: Alarms application - Functionalities
  source_quote: |
    "Signature and action are headers available in alarm report. Remarks are not displayed in alarm
    report." (p295)
    "IN ORDER TO TAKE INTO ACCOUNT, THE FIELDS CUSTOMIZATION, YOU NEED TO CLOSE THE 8770 CLIENT, THE
    NMC SERVICE MANAGER SERVICE MUST BE RESTARTED, AND THEN YOU OPEN THE 8770 CLIENT AGAIN" (p297)
  summary: |
    报表口径：告警报告带处理人（Signature）与动作（Action）两列，自由文本 Remark 不进报告——重要结论
    别只写在 Remark 里。字典改名三步走：关客户端 → Service Manager 重启 NMC Service Manager → 重开
    客户端，少一步字段名就不变。
  conditions: 告警处置与报表交付
  tags: [warning, alarms, dictionary]

- id: n35
  title: 报告默认上限会截断——TXT 4000 行/各格式 50 页/库 100000 行
  type: limitation
  source_pages: p444
  source_chapter: Reports application / Configuring report size limits
  source_quote: |
    "If the report is longer than (n) lines or (n) pages, a message indicating that the report is
    truncated is displayed at the end of the report" (p444)
  summary: |
    默认偏好下大数据量报告被静默截断（仅尾部提示）：TXT 4000 行、HTML/PDF/EXCEL 各 50 页、数据库取数
    100000 行。给管理层交付"完整账单/全量审计"前先核对偏好值与数据量，必要时调参或分批生成。
  conditions: 报告交付
  tags: [limitation, reports]

- id: n36
  title: 报告邮件导出的 SMTP 语法陷阱——冒号后无空格；自定义端口必须显式写
  type: warning
  source_pages: p452
  source_chapter: Reports application / Mail server parameters
  source_quote: |
    "The number of the SMTP port is optional if the default SMTP port number is used (default SMTP
    port = 25). Careful: no space between ':' and the TCP port number." (p452)
  summary: |
    邮件服务器字段格式 <名称或IP>:<SMTP端口>：默认 25 端口可只写地址，非 25 端口必须显式带端口且
    冒号后不能有空格（"server: 46"这种带空格写法直接失效）。报告邮件发不出先核对这半个字符。
  conditions: 邮件通知/报告邮件导出
  tags: [warning, email, smtp]

- id: n37
  title: Scheduler 错过补跑语义——Maximum start delay 超时即放弃
  type: limitation
  source_pages: p473
  source_chapter: Scheduler Application / Scheduling tab
  source_quote: |
    "Maximum start delay This is the maximum delay allowed to run a task that was not performed on
    the scheduled date. Example: the job scheduled for Saturday with a maximum delay of one day is
    not performed if the PC is shut down on Friday and restarted on Monday." (p473)
  summary: |
    计划任务不是"开机必补跑"：停机错过时间超过 Maximum start delay 就放弃执行（书中例：周六任务+
    延迟 1 天，周五关机周一开机=不跑）。备份类关键任务要么给足延迟，要么配合人工 Execute now 巡检。
  conditions: 计划任务设计
  tags: [limitation, scheduler]

- id: n38
  title: 误删/改坏预定义维护 job 的恢复路径——LDIF 导入 + 重启 NMC Scheduler
  type: warning
  source_pages: p502
  source_chapter: Scheduler - Automatic maintenance / Restoring the maintenance jobs
  source_quote: |
    "In case of deletion or modification of the predefined maintenance jobs, it is possible to
    restore the default configuration by a LDIF import. ... Restart NMC Scheduler service." (p502)
  summary: |
    Daily Job/Weekly Job/8770 Data Backup 等预定义 job 没有回收站：删坏后从 \8770\data\scheduler 下
    DailyJob.ldif/WeeklyJob.ldif 经 Administration 应用 Import（Add and modify）恢复，再重启 NMC
    Scheduler 服务。清理实验后务必核对预定义 job 完整。
  conditions: Scheduler 运维
  tags: [warning, scheduler, recovery]

- id: n39
  title: 备份期间 8770 不可用；备份与版本强绑定不可跨版本恢复
  type: warning
  source_pages: p507, p510, p519
  source_chapter: 8770 Maintenance application
  source_quote: |
    "OmniVista 8770 Server is unavailable during backup process." (p507)
    "A backup is dedicated to a version. It cannot be restored on a server running another
    version." (p510)
  summary: |
    两条恢复规划铁律：①备份过程全站管理不可用（话务不受影响，但网管停摆）——窗口放在业务低峰；
    ②备份只能还原到 nmcVersion 相同的版本——"先升级再恢复旧备份"行不通，灾难恢复预案要写明版本
    匹配检查步骤。
  conditions: 备份与灾难恢复
  tags: [warning, backup, restore]

- id: n40
  title: TraceType --1 详细跟踪拖慢服务器——查完必须改回 0
  type: warning
  source_pages: p547, p564
  source_chapter: NMC services / Detailed traces
  source_quote: |
    "TraceType –-1 (Detailed traces) Warning: this mode slows down the server! ... Go back to
    default trace, after investigation" (p547)
    "ONCE INVESTIGATION IS DONE, DON'T FORGET TO MODIFY THE TRACETYPE ARGUMENT TO DEFAULT SETTINGS" (p564)
  summary: |
    给服务开 -TraceType --1 详细日志是排障利器也是性能杀手（日志量翻倍、服务器减速），支持工单关闭后
    忘改回是常见的"排障后遗症"——把"改回 TraceType 0"写进工单关闭检查单。
  conditions: NMC 服务排障
  tags: [warning, logging, performance]

- id: n41
  title: 被 NMC Service Manager 监督的服务不要手动 Start
  type: warning
  source_pages: p561
  source_chapter: NMC services / Notes>Restart a service
  source_quote: |
    "For other services don't restart them using the 'Start' button. These services are supervised
    by NMC service manager and are automatically restarted." (p561)
  summary: |
    服务分两类：四个 Automatic（NMC Service Manager、DSEE 控制中心、DSEE、MySQL8770）停了要手动
    Start；其余 Manual 服务由 NMC Service Manager 监督、崩溃自动重启——手动 Start 反而可能造成双实例
    冲突。Service Manager 里看到服务停了，先等自动拉起再动手。
  conditions: 服务运维
  tags: [warning, nmc-services]

- id: n42
  title: DirManag 不支持 LDAPS（仅 389 明文口）
  type: limitation
  source_pages: p535
  source_chapter: 8770 Maintenance tools / Dirmanag.exe
  source_quote: |
    "Port number 389 (LDAPS is not supported), Login cn=directory manager" (p535)
  summary: |
    DirManag LDAP 浏览器只能走 389 明文口（目录管理器凭据明文过网）——生产网段隔离/跳板机上使用，
    别在跨网段明文通道上跑。要加密的 LDAP 操作走 Directory Server Control Center 或应用层。
  conditions: LDAP 直查场景
  tags: [limitation, ldap, security]

- id: n43
  title: OXE 恢复前必须停电话；停电话会禁用 role address（要用物理 IP）
  type: warning
  source_pages: p577, p589
  source_chapter: OmniPCX Enterprise backup & restore
  source_quote: |
    "Managers must stop the telephone first, to restore the backup files via Swinst tool." (p577)
    "by stopping such process, you disable the role address facility. Don't forget to use the OXE
    physical IP address to enter in configuration mode" (p589)
  summary: |
    OXE 数据库恢复的连环坑：①不先 swinst 停电话，恢复无法进行（业务中断窗口必须提前报备）；②停电话
    后角色地址设施同时失效——原来用 csm 角色 IP 连的会话全断，重连必须用物理 CPU IP（192.168.1.1 类）；
    ③恢复完要重设 Autostart 再起电话，漏了起不来自动恢复。
  conditions: OXE 恢复操作
  tags: [warning, oxe-backup, swinst]

- id: n44
  title: 许可版本只支持 N-1；PKI 特性从 R5.0 起移除
  type: version-trap
  source_pages: p602-603
  source_chapter: 8770 LICENSE / License file parameters
  source_quote: |
    "Only the N-1 license is supported in the N release" (p602)
    "Use of Public Key (not available anymore from release R5.0)" (p603)
  summary: |
    许可两大版本陷阱：①R5.2 只吃版本 15/16 的许可文件——旧许可（≤14）导入无效，扩容/换机申请按
    N-1 规则下单；②Security 键里的 PKI 档位（2-5）从 R5.0 起只剩语义不再供货，别按老资料承诺 PKI
    功能。
  conditions: 许可采购与升级
  tags: [version-trap, license]

- id: n45
  title: 2019 安装章疑似沿用旧版内容——cfg 文件名写 nmc5_5.1.cfg（推断）
  type: version-trap
  source_pages: p618-639
  source_chapter: Server installation on Windows 2019 Server
  source_quote: |
    "The 8770 server information are stored on the following path: C:\Users\<windows_user_account>\
    nmc5_5.1.cfg" (p639)
  summary: |
    2019 章多处与 2022 章不一致且更像旧版残留：连接信息文件名写 nmc5_5.1.cfg（2022 章为
    nmc5_5.2.cfg）、无 WMIC 附录、DNS 指向 192.168.1.100（ecosystem 虚机）而 2022 章为 192.168.1.250。
    按 2019 章操作时以实际版本号与现场 DNS 为准，文件名差异不影响功能（推断：文档未随版本同步）。
  conditions: Windows 2019 安装
  tags: [version-trap, installation, documentation]

- id: n46
  title: OXO Connect R10 起强制改全部账户密码；首连必填客户信息
  type: version-trap
  source_pages: p653-654
  source_chapter: OXO Connect node declaration / OXO Connect connection
  source_quote: |
    "Enter the different passwords for sessions accounts. From OmniPCX Office R10, it's mandatory
    to modify all passwords." (p653)
    "At first connection to OXO Connect, you must fill in the customer information parameters.
    Fields with a star (*) are mandatory." (p654)
  summary: |
    OMC 首连 OXO 的两道强制关卡：R10 起所有会话账户默认密码必须当场改掉（pbxk1064 只在 cold reset 后
    有效）；客户信息（* 项）不填完进不了主界面。批量交付脚本要预留这两步交互。
  conditions: OMC 首次连接
  tags: [version-trap, oxo-connect, omc]

- id: n47
  title: OXO 共享目录参数错误需重启 8770 服务器才能再改
  type: warning
  source_pages: p659
  source_chapter: OXO Connect node declaration / OXO Connect preferences management
  source_quote: |
    "If all parameters are correct, modifications are accepted. If not, a reboot of the OmniVista
    8770 server is required." (p659)
  summary: |
    OXO Preferences 的 Secure Shared Directory（\\nms\OXO-databases 访问凭据）只有填对才被接受；填错
    后不能就地重试——要重启 8770 服务器才能再次修改。首次配置前先确认 8770 的 Windows 会话账号密码
    正确再动手。
  conditions: OXO 纳管配置
  tags: [warning, oxo-connect]

- id: n48
  title: OXO Connect 计费锁默认无 ticket——1000 步进、上限 30000
  type: limitation
  source_pages: p608
  source_chapter: 8770 LICENSE / PCX locks — OXO Connect
  source_quote: |
    "Accounting: Yes / No. If yes: Default: no ticket. Possibility to increase the number of
    tickets by steps of 1000. 30 000 tickets maximum. Alarms: no lock. OMC: no lock" (p608)
  summary: |
    OXO Connect 只有计费有许可锁且默认零 ticket——开了 Accounting=Yes 但没加订 ticket 时计费数据
    就是空的；扩容按 1000 一档、封顶 30000。告警与 OMC 连接不受锁限制。OXO 站点"计费没数据"先查锁。
  conditions: OXO 计费上线与扩容
  tags: [limitation, license, oxo]

- id: n49
  title: 许可超限进受限模式——仅 Directory 与 Configuration 可用（服务器不停机）
  type: limitation
  source_pages: p606
  source_chapter: 8770 LICENSE / Control of the number of users
  source_quote: |
    "When some license thresholds are exceeded, client runs in restricted mode: Only Directory and
    Configuration are accessible through 8770 client. Those applications are useful to fix an
    'exceeding' condition. However 8770 servers continue to work to avoid any risk of data loss" (p606)
  summary: |
    用户数/应用数超限的表现是"应用大面积消失"而非宕机：只剩 Directory 与 Configuration（用于删户
    降到限内）。值机看到应用集体不可用先查许可用量（NMCLicServer_1.log），别按故障重启——重启没用
    还丢排障时间。
  conditions: 许可超限场景
  tags: [limitation, license]

- id: n50
  title: 8770 自身无高可用方案在书内展开——redundancy 仅许可字段一笔带过
  type: out-of-scope
  source_pages: p605
  source_chapter: 8770 LICENSE / License file parameters（Redundancy 字段）
  source_quote: |
    "Redundancy: enabled ... MacAddressRedundant / IPAddressRedundant / ProductIDRedundant /
    UUIDRedundant" (p605)
  summary: |
    全书没有 8770 双机/集群部署章节，高可用痕迹只有许可文件里的冗余服务器特征字段。生产高可用设计
    （双机、备份策略、故障切换）需要引用产品 High Availability 文档，本书能力边界止于单机管理。
  conditions: 高可用方案设计
  tags: [out-of-scope, ha]

- id: n51
  title: 容量规划工具与第三方网管集成细节在书外
  type: out-of-scope
  source_pages: p8, p282
  source_chapter: Virtualization & SNMP Proxy
  source_quote: |
    "OmniVista 8770 Capacity Planning tool V3.0 for a better sizing flexibility of virtual machine
    parameters" (p8)
    "Supervise alarms coming from PBX nodes and OmniVista 8770 components by an external hypervisor" (p282)
  summary: |
    两处只给指针：规模设计依赖 Capacity Planning tool V3.0（书内无用法）；与客户 NMS 的集成只教到
    "trap 发出去、TrapReceiver 收到"，hypervisor 侧规则/拓扑/告警收敛都在客户系统内完成。
  conditions: 售前规模设计与 NMS 集成项目
  tags: [out-of-scope, sizing, integration]

- id: n52
  title: RLAB 实验凭据/环境全书明文——生产禁止沿用（实验口径提醒）
  type: limitation
  source_pages: p47, p77, p119, p642, p649
  source_chapter: Remote Labs & 各 How-To
  source_quote: |
    "mtcl / swinst / root — Superuser2580*" (p47)
    "Directory manager password: superuser ... The default Installer password is pbxk1064" (p69, p649)
    "Password Letacla1 (password used on a classroom environment)" (p642)
  summary: |
    教材为教学连贯使用固定明文密码（Superuser2580* / superuser / letacla1 / sql / pbxk1064 / Alcatel1 /
    Pbxnmc12），全部标注实验口径。生产交付必须逐项替换并纳入客户密码策略；据此教材直接复刻的环境
    等于零口令防护。
  conditions: 一切生产环境
  tags: [limitation, security, lab]

- id: n53
  title: OXO 章存在未翻译法语残句——文档质量瑕疵
  type: limitation
  source_pages: p643, p659, p643
  source_chapter: OXO Connect node declaration
  source_quote: |
    "MAIN@: Vérifier que l'adresse IP de la Power CPU EE est : 151.1.1.246" (p643)
    "Renseigner le login de session Windows du serveur OmniVista 8770 (i.e. Administrator)" (p659)
  summary: |
    OXO Connect 章多处操作说明残留在法语（"Vérifier que…"、"Renseigner le login…"），英文版 Ed47 未
    完成翻译。阅读时按上下文理解（=核对 MAIN@ IP、=填 8770 服务器 Windows 会话账号），以此类推
    同章节其他法语片段。
  conditions: 阅读与知识提取（推断：翻译遗漏而非内容差异）
  tags: [limitation, documentation]
```

## 任务覆盖自检（task ↔ id 映射）

| task_id | 相关 n 条目（Boundary 来源） |
|---|---|
| task-01/02 | n01、n07、n08、n09、n10、n11、n45、n52 |
| task-03 | n12、n13、n14 |
| task-04 | n20 |
| task-05 | （p12/p13 覆盖规则侧） |
| task-06 | — |
| task-07/08 | （p14/p15 覆盖） |
| task-09 | n15 |
| task-10 | n16、n17、n18 |
| task-11 | n46、n47、n48 |
| task-12 | n20 |
| task-13 | n34 |
| task-14 | n21 |
| task-15/16 | n22、n23、n24 |
| task-17 | n25、n26、n27、n28、n29、n30、n31 |
| task-18 | n32、n33 |
| task-19 | n35、n36 |
| task-20 | n37、n38 |
| task-21 | n38 |
| task-22 | n39 |
| task-23 | n42 |
| task-24 | n40、n41 |
| task-25 | n43 |
| task-26 | n44、n48、n49 |
| task-27 | — |
| task-28 | n02、n03、n50、n51 |
| 全局 | n52（实验口径总提醒）、n53（文档质量） |
