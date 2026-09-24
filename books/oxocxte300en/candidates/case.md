# 案例/实验/操作序列候选 — OXO Connect Starter (OXOCXTE300EN Ed16)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号、ARI）标注"实验口径"。
> 条目说明: 全书 25 个 How-To 实验章 → c01..c25 一一对应；验收信息以各实验"Notes/Result"或原文验收点为准。

```yaml
- id: c01
  title: OCE 启动与首次注册 FTR（Cloud Connect 上云）
  type: lab
  source_pages: p59-62
  source_chapter: OCE Start-up & first Time Registration (FTR) — How To
  source_quote: |
    "To register the OCE on Cloud Connect, open the web browser and enter as URL: 192.168.94.246
    (ETH1)" (p61)；"Login: installer Pwd: pbxk1064 At the very first time, the system asks to put a
    new password, put Alcatel1 during the training" (p61)；"The system registers in the Cloud …
    Licenses are downloaded from the Cloud … The system is updated" (p62)
  steps: |
    1. 前置确认：本实验仅限实体课堂——虚课无法把 PC 接到 ETH1 口完成注册（书中 Implementation 明示，
       虚课时 OCE 保持默认配置、改用 OMC 常规连接改 IP）。
    2. 布线：IPBox 的 ETH0 接 PoE 交换机、ETH1 接管理 PC；交换机加电。
    3. 等待 OCE 完全启动（约 3 分钟，电源指示灯 1 秒亮 1 秒灭）（p60 Notes）。
    4. 管理 PC 网卡配 DHCP（ETH1 自带 DHCP 池 192.168.94.247-254）。
    5. 浏览器打开 https://192.168.94.246（ETH1），点 "Register"。
    6. 登录 installer / pbxk1064（实验口径，仅首次）；系统强制设置新密码，培训用 Alcatel1（实验口径）。
    7. 录入 Basic IP Configuration 与 Web Proxy：ETH0 IP 192.168.1.246、掩码 255.255.255.0、网关
       192.168.1.254、代理服务器 192.168.1.254 端口 3128、DNS 192.168.1.250（实验口径）。
    8. 录入参考值：Partner fleet reference=OXOP（P=POD 号 1-6，讲师提供）、Partner sub-fleet
       reference=TRAINING、Installation reference=LAB（实验口径）。
    9. 点右下角 "V" 提交注册。
  verification: |
    p62 Result/Notes 四项：系统注册入云（注册状态指示）、许可从云端自动下载、系统自动更新、系统经
    OXO Connectivity 与 Fleet Dashboard 变为远程可管理。
  conditions: 物理课堂 + 出网条件 + Cloud Connect 服务可用；IPBox 处于出厂状态。
  tags: [lab, ftr, cloud-connect, oce]

- id: c02
  title: OMC 安装与首次连接 OXO（证书安装、改密、客户信息）
  type: lab
  source_pages: p73-82
  source_chapter: OMC Installation — "Install OMC, connect to the PCX"
  source_quote: |
    "Make a connection to the system with OMC in Expert mode with server authentication" (p78)；
    "In order to avoid displaying the security alert at each connection, you must install the
    certificate the 1st time." (p79)；"OMC is ready to start with the customer configuration. The
    icon on the bottom right shows that you are connected to the OXO" (p82)
  steps: |
    1. 虚课前置：RLab 用 console mode 连接 PC Client 虚机（OXOC_PC_CLIENT）；OMC 安装包在桌面
       SOFTS OXO CONNECT 目录（实验口径）。
    2. 解压 OMC 文件 → 运行 setup.exe → 选 "Run as administrator"。
    3. 选安装语言 → OK → Next；选 Destination folder → Next。
    4. 选目标 Country/Distribution Channels（可多选）→ Next；选 Target Product → Next。
    5. 选 OMC 显示语言 → Next；点 Install → 完成后 Finish。
    6. 打开 OMC 应用 → 选 "Expert" 菜单 → 连接方式 LAN/WAN。
    7. 输入 OXO 出厂 IP 192.168.92.246（实验口径），勾选 "Server authentication"，输入 installer
       首连密码 pbxk1064（实验口径，仅第一次连接使用）。
    8. Security Alert 弹窗 → View certificate → Install certificate → 存储区选 "Trusted Root
       Certification Authorities" → OK → Finish → 导入成功点 OK（此后连接不再弹安全告警）。
    9. 为各账户设置讲师给定的新密码（p81：每客户密码必须不同）；后续可在 OMC/Security 菜单再改。
    10. 录入客户信息（带 * 必填，首次连接 OXO 强制）；可选录入供应商信息（实施技师联系方式）。
  verification: |
    书中验收点：OMC 右下角图标显示已连接 OXO，即 "OMC is ready to start with the customer
    configuration"（p82）。
  conditions: OXO 处于出厂默认状态；OMC 安装包可从 NAS 网络盘或桌面目录获取。
  tags: [lab, omc, installation, certificate]

- id: c03
  title: OXO Connect 与客户端 PC 的 IP 规划修改
  type: lab
  source_pages: p83-86
  source_chapter: OXO Connect IP settings modification — How To
  source_quote: |
    "With the OMC, change the OXO Connect IP settings" (p84)；"Click OK & Re-start the OXO Connect"
    (p85)；"Once the IP addressing is changed, you will be able to connect to the Client PC VM with
    "Remote Desktop Connection" - RDP" (p84)
  steps: |
    1. 进入 OMC/ Hardware and limits/ Lan/IP configuration。
    2. Boards 页签：Main CPU 填 192.168.1.246（实验口径）。
    3. LAN Configuration 页签：Mask 255.255.255.0；Default Router Address 192.168.1.254（实验口径）。
    4. DNS 页签：DNS 1 = 192.168.1.250；DNS 2 = 10.20.30.250（实验口径）。
    5. DHCP 页签：话机地址池 Start 192.168.1.30 / End 192.168.1.39（实验口径）。
    6. 点 OK 并重启 OXO Connect。
    7. 改客户端 PC（OXO_PC_CLIENT）IP：IP 192.168.1.10 / 掩码 255.255.255.0 / 网关 192.168.1.254 /
       DNS1 192.168.1.250 / DNS2 10.20.30.250（实验口径）。
    8. 虚课：改完用 "Remote Desktop Connection"（RDP）重新连接 Client PC VM。
  verification: |
    书中隐含验收：新 IP 生效后可从新地址管理 OXO；虚课环境以 RDP 重连成功为切换完成标志（p84）。
  conditions: c02 已完成（OMC 可连 OXO）。
  tags: [lab, ip-planning, omc]

- id: c04
  title: IP 话机开通（静态与动态两种模式）
  type: lab
  source_pages: p106-116
  source_chapter: Put in service an IP phone — "Put in service an IP phone in static and dynamic mode"
  source_quote: |
    "Enable « auto provision » in the Subscribers/Base stations list to allow IP devices to register
    onto the OXO Connect" (p107)；"At the start up, the OXO Connect will automatically assign a
    directory number to the deskphone. The deskphone is now in service" (p111)；"There are 2 modes
    for Dynamic: Dynamic and Dynamic Alcatel." (p116)
  steps: |
    静态模式：
    1. OMC/Subscribers BaseStations list → 临时启用 "Auto-Provision"。
    2. 话机侧：断电重上电，启动 2/5 或 3/5 阶段同时按 * 和 #（或屏幕设置图标 → Config MMI）。
    3. Main Menu → IP parameters → IP config → IPv4 wired → Network Settings。
    4. IPv4 mode 选 Static，填：Phone IP 192.168.1.50、掩码 255.255.255.0、网关 192.168.1.254
       （实验口径）。
    5. System Settings → 输入 NOE IP Administrator Password（见 OMC/Security/Device administrator
       password）。
    6. TFTP1 填 OXO Connect IP 192.168.1.246（实验口径）；不动 TFTP#2 与 TFTP 端口（无要求时）。
    7. 校验退出菜单，话机重启后自动分配目录号码。
    动态模式：
    8. OMC/ Hardware and limits / LAN/IP Configuration / DHCP 页签：ALE 设备 DHCP 池 192.168.1.10 至
       192.168.1.39（实验口径）。
    9. OMC/Subscribers BaseStations list → 启用 Auto-Provision。
    10. 话机侧同 2-3 步进入 IPv4 wired → Network Settings，选 Dynamic；校验退出。
    11. 注（p116）：Dynamic=从任意 DHCP 服务器取 IP；Dynamic Alcatel=只接受 OXO 系统（仅 OXO）分配
        的 IP。
  verification: |
    书中验收点：话机重启后 OXO Connect 在启动时自动分配目录号码——"The deskphone is now in
    service"（p111、p115）。
  conditions: DHCP 池与话机同网段；Auto-Provision 处于启用状态（可临时）。
  tags: [lab, ip-phone, provisioning, dhcp]

- id: c05
  title: IP-DECT 8378 IP-xBS 课堂安装（ARI 绑定 + GAP 注册）
  type: lab
  source_pages: p117-122
  source_chapter: IP-DECT xBS classroom installation — "Manage IP-DECT feature"
  source_quote: |
    "Enter the ARI number (11 digits in octal) … 11000436010 for POD 1" (p119)；"Warning Validate
    and do not forget to make a warm reset" (p118)；"Click Assign as soon as the IPUI appears" (p122)
  steps: |
    1. OMC/ Hardware and Limits / LAN/IP Configuration / Boards：系统 IP 192.168.1.246（实验口径）。
    2. 同菜单 DNS-DHCP 页签：启用内置 DHCP 服务器，范围 192.168.1.10-192.168.1.30（实验口径）。
    3. Warning：确认配置并做 warm reset（DHCP 配置后一并做）。
    4. IMPORTANT（p118 原文法文注）：别忘了在话机/基站列表菜单激活 Autoprovision。
    5. OMC/ Dect / DECT-PWT ARI-GAP / ARI：输入 ARI 号（11 位八进制）——POD1-6 分别
       11000436010/20/30/40/50/60（实验口径；ARI 对 IBS 与 IP-DECT 通用，唯一值取自 eBuy）。
    6. （仅课堂）8378 IP-xBS 物理接到 PoE 交换机；观察 LED 六步：红（网络初始化/IP 获取/配置文件）
       →橙（软件下载/呼叫服务器链路/基站配置）→绿 1s 亮 1s 灭=存活。
    7. OMC/ Subscribers/Base stations list：基站上线后出现在列表中。
    8. 建话机：OMC / Subscribers/BaseStations List / Add / IBS-xBS sets / 输入数量 / Add an IBS-xBS
       DECT handset；选未来目录号码并命名。
    9. 点 "GAP registration"；IPUI 出现后点 "Assign"。
    10. 话机侧注册（Tips，p122）：8214/8234/8244/8254/8262 恢复出厂后 Auto Install 模式，或
        Menu\Install\Register\ 输 PIN 0000 \ 其余参数跳过。
    11. 注册完成后终端类型自动显示；互相拨打电话测试。
  verification: |
    书中验收：基站出现在 Subscribers/Basestations 列表（p120）、注册后终端类型自动出现（p122）、
    第 5 节打通话测试（p122）。
  conditions: 仅物理课堂（需 PoE 交换机与实体基站）；ARI 由讲师/eBuy 提供。
  tags: [lab, dect, xbs, ari]

- id: c06
  title: 编号计划配置（编程模式/代接/分机段/缩位拨号）
  type: lab
  source_pages: p131-135
  source_chapter: Setting up the numbering plan — "Set up the numbering plan"
  source_quote: |
    "Put value 20 as "start" and "end" value. Base : empty" (p132)；"Put 21 as « start » and « End »
    value. Base : enter 0 which corresponds to the set call pickup function" (p133)；"Base Always a
    number from 0 to 2199" (p135)
  steps: |
    1. 编程模式前缀 20：OMC → Numbering 菜单 → Numbering Plans → 既有 Subscriber 段 200-299 有冲突
       → 选中删除 → 功能列表选 "Programming Mode" → start/end=20、Base 空 → Add → OK。
    2. 话机代接前缀 21：Numbering Plans → 功能选 "Pick Up" → start/end=21、Base=0（对应话机代接）
       → Add → OK。
    3. 分机段 100-149：Numbering Plans → 选既有 Subscriber 行（100-199）→ end 改 149 → Base 留 100
       （段首话机号）→ Modify → OK；150-199 留作其它功能。
    4. 缩位拨号 400-499：既有 Secondary Trunk Group 400-434 冲突 → 删除；前缀 60 "Appointment" 冲突
       → 删除；功能选 "Collective Speed Dial" → 400-499、Base=0 → Add → OK。
    5. 缩位拨号 600-699：删除所有 6 开头前缀后，同样建 600-699、Base=100 → Add → OK。
  verification: |
    书中隐含验收：计划表无冲突段（Add/Modify 成功、旧冲突段已删）；Base 取值域 0-2199 合法。
  conditions: OMC 可连 OXO；改前缀前确认无业务依赖旧段。
  tags: [lab, numbering-plan, prefix, base]

- id: c07
  title: 建立 Hunt group（含三种分发类型测试）
  type: lab
  source_pages: p142-145
  source_chapter: Setting up a hunting group — "Set up a hunting group"
  source_quote: |
    "Select the hunting group 501. Assign the name: Welcome Add extensions 101 and 102 Define a
    "Sequential" search type" (p143)；"Warning: the group 500 is used by the voice mail server!" (p143)
  steps: |
    1. OMC/ Hunting groups → 打开菜单。
    2. 选组 501 → "Details"（Warning：组 500 被语音信箱服务器占用，勿用）。
    3. 点 "Add" 加成员 101、102；组名 Welcome；类型 Sequential → OK 应用 → return。
    4. 测试：拨 501。
    5. 换类型测试：编辑组 501，分别改 Cyclic（Cyclic/轮转）与 Parallel（并行齐振）再拨测（p145）。
  verification: |
    书中验收：拨组号 501 能按所选类型分发到成员话机（p144 Notes："To test your settings, dial the
    hunting group directory number: 501"）。
  conditions: 成员分机已在役；组号在编号计划 hunt group 范围内。
  tags: [lab, hunt-group, groups]

- id: c08
  title: 建立 Pick-up group 与组代接键
  type: lab
  source_pages: p146-150
  source_chapter: Setting up a pick up group — "Set up a pick up group"
  source_quote: |
    "Configure the Pick-up group "1" Add extensions 101, 102 and 103" (p147)；"Keytype: Function key
    • Keyfunction: Pickup … Select: Group" (p150)
  steps: |
    1. OMC/ Pickup groups → 组 1 → "Details"。
    2. "Add" 加分机 101、102、103 → OK → return（虚课：把 IPDSP 104 入组并用它建键）。
    3. 建组代接键（每组员一台）：OMC/ Subscribers – BaseStations list → 选 101 → "Details" →
       "Keys"。
    4. 选空键 → Keytype: Function key → Keyfunction: Pickup → 命名 → 作用域选 "Group"。
    5. 其余组员话机重复 3-4 步。
  verification: |
    书中验收（p150）：呼叫分机 102、让铃响，用 101 上配置的组代接键接起——"Call extension 102, let
    it ring and pick up the call using the key managed on extension 101."
  conditions: 组代接前缀 base=1（组代接）已在编号计划可用。
  tags: [lab, pickup-group, keys]

- id: c09
  title: 建立 Broadcast group（广播组）
  type: lab
  source_pages: p151-153
  source_chapter: Setting up a broadcast group — "Set up a broadcast group"
  source_quote: |
    "Manage Broadcast Group 1 (Call number: *2) … Extension 101 will have "Send" right Extensions
    102 and 103 will have "Reception" right" (p152-153)；"Warning: To receive, a deskphone must have
    a loudspeaker." (p152)
  steps: |
    1. OMC/ Broadcast group → 组 1 → "Details"。
    2. "Add" 加 101、102、103：101 权限 Send、102/103 权限 Reception；组名 workshop → OK。
    3. 虚课替代：无带扬声器话机时，用 IPDSP 作接收方、microSIP 作广播方完成配置（p152）。
  verification: |
    书中验收（p153）：从 101 拨广播组号 *2——"The loudspeakers on extensions 102 and 103 should be
    activated and you must hear your voice on the loudspeakers."
  conditions: 接收话机必须有扬声器（Warning）；组号 *2 为实验口径。
  tags: [lab, broadcast-group, groups]

- id: c10
  title: 建立 Manager/Secretary 组（经理-秘书）
  type: lab
  source_pages: p154-156
  source_chapter: Setting up a manager/secretary group
  source_quote: |
    "Create a manager/secretary group, the two sets must be multiline sets. Manager: 101 Secretary:
    102" (p155)；"In Virtual classroom: No test possible. Requires 2 multiline phones." (p155)
  steps: |
    1. OMC → 打开 "Manager-Secretary Relations" 菜单 → "Add"。
    2. 目录中选经理分机 101、秘书分机 102（实验口径；两台均须 multiline）。
    3. 配置三类键：Screening（过滤）、RSL（对端本地线）、Supervision（监督）→ OK 应用。
    4. （注）Screening 激活键可更换（p156）。
  verification: |
    书中测试清单（p156）：经理侧激活滤键后呼经理；秘书侧激活滤键后呼经理；在经理与秘书话机上测试
    RSL 键；测试经理与秘书监督键。虚课无法测试（需两台 multiline 话机）。
  conditions: 双方均为 multiline 话机；虚课仅做配置。
  tags: [lab, manager-secretary, groups]

- id: c11
  title: 用户设置与功能管理（直呼键/前转/动态路由/选择性转移/热线/插入/外转）
  type: lab
  source_pages: p173-181
  source_chapter: Users' settings and features management — How To
  source_quote: |
    "Select "Resource Key" for the key type. Select "Local Call" for the "key function"." (p174)；
    "Modify the timer 1 value = 10 sec For the Local Calls, at Level 1 Use Timer 1 and enter the
    Destination No" (p176)；"Select "Immediate" for the parameter "Hotline" Enter the operator
    destination number 9" (p178)
  steps: |
    1. 直呼（RSL 键）：OMC → Subscribers/Basestations List → 选用户 → details → Keys → 空键 →
       Keytype: Resource Key → Keyfunction: Local Call → Dialing 填目标内线号（虚课用 IPDSP）。
    2. 遇忙前转键：同一用户 Keys → 空键 → Feature key → Diversion → 类型 On Busy → 填转移目标号 →
       Keylabel 命名（例 to103）→ OK。
    3. 动态路由 10 秒：用户 details → "Dyn. Rout." → Timer1=10s → Local Calls 勾 Level 1 的 Use
       Timer 1 并填 Destination No → OK。
    4. 选择性转移：用户 details → "Sel Divers" → 清单 1 从 unused 改 active → Service 选 Telephone
       → 填内部转移目标号 → 加 2 个分机入主叫过滤清单（Black list 语义）→ Add → OK。
    5. 热线（摘机即呼话务台）：模拟话机 details → "Misc." → Hotline=Immediate → 目的地填话务台号 9
       → OK（虚课无法测试，需物理话机）。
    6. 允许插入：用户 details → Features → Feature Rights 第一部分勾 "Intrusion Allowed"。
    7. 经理防插入：经理话机 details → Features → 勾 "Intrusion Protection"。
    8. 外线前转仅经理：经理话机 details → Features → 勾 "External Diversion" → OK → 再次 OK 确认
       话机修改。
  verification: |
    书中各小节隐含验收：键生效（直呼一键呼出）、振铃 10 秒后第二话机同响、清单内主叫来电被转、模拟
    话机摘机直连话务台、非授权话机无法插入经理通话、仅经理可设外转。虚课限制项在文中逐条标注。
  conditions: 各功能依赖 Feature Rights 的授权/保护配对（授权者与被保护者分属不同话机）。
  tags: [lab, user-features, keys, diversion, intrusion]

- id: c12
  title: 语音信箱管理（定制/模式/录音监听/远程访问/删建信箱）
  type: lab
  source_pages: p190-196
  source_chapter: Voice Mail management basic services — How To
  source_quote: |
    "press the key "Message" or the corresponding prefix "Mailing" … Enter the default users
    password of this OXO (ex.14 25 35) Enter the new password chosen by the user 14 25 36" (p191，
    实验口径)；"Eg. 41500 base 500 … Function Hunting group … Base 500 Choose the hunting group
    containing the voicemail ports" (p194)
  steps: |
    1. 用户信箱定制（话机侧）：按 Message 键或 Mailing 前缀 → 输入默认用户密码（实验 14 25 35）→
       设新密码（实验 14 25 36）→ 录姓名 → 录问候语（可选）。
    2. Answer-only 模式：OMC → Subscribers/Basestations List → 选用户 → details → Mailbox 按钮 →
       Options 页签 → 模式选 answer only（模式注释：Answer only 不留信/Standard 全功能/Guest 受限）。
    3. 录音与监听：另一用户 Mailbox → Options → 勾 "Recording of Conversation allowed"；建两个功能
       键：Keys → 空键 → Feature key → "Voice Mail: Conversation Rec"；再建 "Voice Mail: Screening"
       键（注：Screening 用户侧受密码保护，必须已改非默认密码）。
    4. 远程访问：OMC → Numbering 菜单 → Numbering Plans → Public Numbering Plan 页签 → Add：功能
       Hunting group、Start=41500、End=41500、Base=500（VM 端口所在 hunt group，法国默认 500，实验
       口径）→ Add → OK；再给用户开权：用户 details → Features → Feature Rights 第 3 部分勾
       "Mailbox remote consultation"。
    5. 删信箱：用户列表选用户 → "Del Mailbox"。
    6. 建回信箱：选用户 → "Mailbox" 按钮 → "Yes"。
  verification: |
    书中各节隐含验收：新密码可进信箱、Answer-only 不留信、录音键按下开始录会话、从外线拨 41500+
    信箱号可远程听留言、删除后再建成功。
  conditions: 虚课用 IPDSP；Screening 测试需非默认密码（p193 注）。
  tags: [lab, voicemail, mailbox, recording]

- id: c13
  title: 公共 SIP 网关配置与注册验证（ITSP1 模拟器）
  type: lab
  source_pages: p223-242
  source_chapter: Public SIP Gateway — How To（20 页实验）
  source_quote: |
    "Program a New Gateway Parameters Index 1 … The index label is ITSP1G1 … SIP numbers format
    index: 1 (For canonical format)" (p232)；"Put the bandwidth at 5 minimum calls in order to allow
    external calls" (p234)；"OMC/History and Anomalies/History Table Message displayed: SIP
    registration success" (p240)
  steps: |
    1. 前置：拓扑按 OXOCCTExxxITSP1EN 文档；本实验不处理短号与紧急号码（无 ADL 表管理）（p225）。
    2. LAN IP 核对：OMC/Hardware and Limits/LAN IP Configuration——Boards=.246、DNS1=.250、
       DNS2=10.20.30.250、Router=.254（改后 Reset OXO）、DHCP 池 1.10-1.39（实验口径）。
    3. 编号计划：OMC/Numbering/Numbering Plans/Public Numbering Plan——DDI 分机 41100-41199、话务台
       41000（必要时复制到 Restricted Public Numbering Plan）；OMC/Numbering/Installation Numbers——
       安装号 210P41000（P=POD 号，实验口径）。
    4. VoIP 中继：OMC/External Lines/List of Accesses/VoIP details——建 8 通道 Public 接入（通道总数
       取决于硬件与许可；Gateway index 网关建好后回填）。
    5. 中继组：OMC/External Lines/List of Trunk Groups/Details——Add 把 VoIP 接入加进主中继组；
       Link-Cat. 页签调整链路类别允许外呼（Check barring）。
    6. SIP 网关：OMC/ External Lines / SIP / SIP Gateways——General：Index 1、标签 ITSP1G1、SIP
       numbers format index=1（canonical）、End of dialing table used。
    7. DNS 页签：DNS A=192.168.1.250（实验口径）；提示：随后必须去 Domain Proxy 配 Outbound Proxy。
    8. Domain Proxy 页签：Target/Local domain/Realm=sip.itsp1.fr、Outbound Proxy=gateway1.itsp1.com
       （配完 DNS 后 IP 类型自动 dynamic）。
    9. Registration 页签：勾 Registration requested、Registrar name=sip.itsp1.fr。
    10. Media 页签：勾 RTP Direct；带宽设最低 5 通话以放行外呼。
    11. Identity 页签：启用 RFC 3325；Protocol 页签保持默认；Topology 页签选 ETH0；Security 页签：
        SIP 流不加密（OCE 默认值）。
    12. SIP 账户：OMC/ External Lines / SIP / SIP Accounts → 右键 Add：Login=pbxP、Password=alcatel、
        Registered username=pbxP（P=POD 号，实验口径）、Gateway Parameters Index=ITSP1G1。
    13. 关联：OMC/External Lines/List of Accesses——把新建网关联到 VoIP 外线（回填 Gateway index）。
    14. 注册核验：OMC/History and Anomalies/History Table。
    15. 测试：拨本机 DDI（0210P41150 等）、模拟器公共号 (0)0210P12345、其它 POD 的用户。
    16. 抓包：OMC/Tools/Webdiag（installer 登录，密码例 Alcatel1）→ TCP Dump traces → 选 SIP →
        开始捕获 → 停止后自动生成文件；PC 用 Wireshark 分析（可存档交技术支持）。
  verification: |
    书中验收（p240）：History Table 显示 "SIP registration success"；通话双向可通；SIP trace 可在
    Wireshark 中看到注册与呼叫流程。
  conditions: 实验口径全表；生产参数由真实运营商提供（TC1284 对应 TC）。
  tags: [lab, sip-gateway, itsp, wireshark]

- id: c14
  title: 音乐保持与预公告消息下载（.wav 上传）
  type: lab
  source_pages: p246-251
  source_chapter: Music on hold and Preannouncement messages downloading — How To
  source_quote: |
    "Application OMC/System Miscellaneous/Music on Hold … Select Recorded Music … Select the
    function PC to OXO download" (p247-248)；"OMC application/Subscribers Misc/Preannouncement
    Messages … Select in the list the message to customize (MSG1 to MSG20)" (p250)
  steps: |
    1. 准备 .wav（16-bit PCM 8kHz Mono 或 CCITT A-law/μ-law 8-bit 8kHz Mono）；无文件时可用 MMC 话机
       话务员会话录：Menu Operator/Expert/Voice/Hold music/Music xx 或 Message xx。
    2. MoH：OMC/System Miscellaneous/Music on Hold → 选 Entity（默认 Entity1，1-4 多公司用）→
       Music source 选 Recorded Music → "Load from and transfer" → 3 点选文件 → 箭头传输（反向用
       "Transfer and save as..."）。
    3. 预公告：OMC/Subscribers Misc/Preannouncement Messages → 选 MSG1-MSG20（默认 4 条、许可至
       20）→ "Load from and transfer" → 选 .wav → 传输。
  verification: |
    书中隐含验收：消息列表中该 MSG/Music 已更新；外线保持时播定制音乐（内线保持为哔哔音，p247
    Reminder）。
  conditions: .wav 格式硬约束；MoH 仅外线保持生效。
  tags: [lab, moh, messages, wav]

- id: c15
  title: 话务台组与时段表管理（日夜切换 + 全局预公告）
  type: lab
  source_pages: p262-269
  source_chapter: Attendant Group and Time Ranges Management — How To
  source_quote: |
    "Group 1: Extensions 100 & 101 Group 2: Message "MSG1" indicating working hours" (p263)；
    "8am to 7pm: Group 1 7pm to 8am: group 2" (p265)；"configure the preannouncement "Before call
    distr." for time range 1 only. Select MSG2 in the list." (p268)
  steps: |
    1. 建组：OMC/ Attendant groups → 组 1 → Details → Add 加分机 100、101（虚课 IPDSP 入组 1）→
       OK；组 2 同法只加 MSG1（MSG1 可由 MMC 话机话务员会话录制或 OMC 导入）。
    2. 周内时段：OMC/ Time ranges → Monday 页签：8am-7pm 活动组=Group 1、7pm-8am=Group 2 →
       Copy/paste 到周二至周五。
    3. 手动限制转移：管理 400 缩位号（默认计划 8000）填内部或 DDI 号，供话务台 N/R 键转移测试。
    4. 周末：Saturday 页签配置后 Copy 到 Sunday 与 Public Holidays（仅组 2 活动）。
    5. 建话务台转移键（Notes，p267）：话务台话机建 "Attendant diversion" 功能键、目标为集体缩位号
       （提醒：受话务员密码保护的键）。
    6. 全局预公告：OMC/ Subscribers Misc/ Preannouncement Overview → Global Greetings → Details →
       对时段 1 配 "Before call distr." 模式、消息选 MSG2 → 复制到其它天。
  verification: |
    书中验收：改系统时间测试时段切换（p265 "Test your configuration by changing the system time"）；
    呼入在营业时间振铃组 1、非营业时间听 MSG1；来电先播 MSG2 再转目的地（Before 模式播完再振）。
  conditions: 时段 End 值=下一行 Start（p266）；话务台组恒并行模式。
  tags: [lab, attendant-groups, time-ranges, preannouncement]

- id: c16
  title: 呼出闭锁管理（时段限呼/副中继组/闭锁表）
  type: lab
  source_pages: p281-291
  source_chapter: Call barring management — How To
  source_quote: |
    "create 4 time ranges … restricted from 12h to 1am and from 7pm to 8am" (p282)；"Modify the
    "start" value by 401 and base by 2 … Enter # for start and End. Enter base =1" (p284-285)；
    "For table number 2 enter a prefix 0053.Turn this prefix Type into authorized type" (p289)
  steps: |
    1. 主中继组时段限呼：OMC → Time Ranges → Monday 建 4 时段（1/3 行=营业时间默认 LC 全员可占、
       2/4 行=非营业时间默认禁占；End=下一行 Start）→ 复制到周二至周五；Public Holidays 页签配置后
       Copy 到 Sunday、Saturday。
    2. 让话机跟随时段（Notes，p283）：话机 details/Feature Rights Part 2 → 关闭 "Inhibition
       Time-ranges"，否则话机恒 normal 模式。
    3. 副中继组（# 占用）：OMC → Numbering Plans → 功能 "Secondary trunk group" → start 改 401、
       base 改 2 → Modify；再 Function 选 "Secondary Trunk Group" → start/end=#、base=1 → Add。
    4. 中继组：OMC → External Lines → List of Trunk Groups：索引 2 组号已变 "#" → Details → Add
       加至少 1 个 SIP 网关 VoIP → Link-Cat.（默认 Normal=12/Restricted=12，不改）。
    5. 授权一个用户：Subscribers/Basestations list → 选用户 → Details → Barring → Traffic Sharing
       Link Cat.：Normal=5、Restricted=5；到 Traffic Sharing Matrix 查 5∩12=+（允许）；其余用户
       12∩12=空默认禁止。
    6. 国际闭锁（仅放行 53 国）：Traffic Sharing & barring → Barring Tables → 表 2 加前缀 0053、
       类型 Authorized → Add。
    7. 全员指到表 2：Subscribers/Basestations list → 各用户 Details → Barring → Barring Link
       Categories：Normal=2、Restricted=2（逐个或用列表 Copy 按钮）。
    8. 核对：Traffic Sharing and barring → Barring Matrix → 行 2 列 1 值=2（用表 2）。
  verification: |
    书中验收：非授权用户按时段无法占主中继组/副中继组；授权用户任何时段可占 # 组；全员国际禁呼、
    0053 开头可呼；矩阵交点与预期一致。
  conditions: 前置=已按 c13 配好公共 SIP 网关；实验业务口径见 p49。
  tags: [lab, barring, time-ranges, trunk-group]

- id: c17
  title: 数据库备份与恢复（OMC 全流程）
  type: lab
  source_pages: p307-314
  source_chapter: Saving and restoring the OXO Connect database — How To
  source_quote: |
    "click on "Read all from PCX" … By default the location of saving is in Documents\OMC" (p308-309)；
    "Before exporting you must Disconnect from the OXO" (p309)；"open "Comm" and click on
    Auto-Connect for Restore Enter the Installer password Select the data to restore, Classic data" (p313)
  steps: |
    1. PC 备份：OMC → Comm → "Read all from PCX"（主对象默认勾选；录过语音导览的勾附加项）→ OK
       传输至完成。
    2. File → Save As → 命名 → Save As（默认存 Documents\OMC）。
    3. 导出外部介质：先 Comm → Disconnect；File → Backup/Store → 选库 → Save 到 USB/网络盘（可导
       出多库）。
    4. 从介质导入：断开状态下 File → Backup → Restore → 选外部介质上的库 → OK（库进入 PC 工作目录
       Documents/OMC）。
    5. 离线查看：File → Open → 选库（未连 OXO 也可查阅客户库）。
    6. 在线恢复：离线打开库 → Comm → Auto-Connect for Restore → 输 installer 密码 → 选恢复数据
       （Classic data）→ OK。
    7. 传输完成提示重启 → Yes；OXO 传输结束自动 warm reset；重启完成后重新连接——系统即运行恢复后
       的库。
  verification: |
    书中验收（p314）：恢复后 OMC 处于在线模式且配置与备份一致；部分更新在重启后生效（"Some updates
    will be activated after a restart of the OXO"）。
  conditions: 导入/导出前必须断开连接；恢复需 installer 权限。
  tags: [lab, backup, restore, omc]

- id: c18
  title: OXO 接入 Rainbow（PBXID+激活码）与三层排障
  type: lab
  source_pages: p344-350
  source_chapter: Connect an OXO to Rainbow — "Configure Rainbow agent in OXO"
  source_quote: |
    "Log in to the Rainbow interface with the client company's administrator account : Login :
    cCpP.admin@ale-training.com" (p345)；"OMC/Cloud/Rainbow In Cloud menu, select Rainbow … Click on
    Rainbow enabled … Apply" (p347)；"Control the connection status: « connected with final
    password » … The rainbow agent log file name is: ccrbagent.log" (p349)
  steps: |
    1. 前提：公司与 PBX 已在 Rainbow 管理端创建（实验中讲师演示该配置）。
    2. 取凭证（两法）：向经销商索取；或自行登录 https://web.openrainbow.com（客户端管理员
       cCpP.admin@ale-training.com / Superuser-P*，实验口径）→ 点公司管理图标 → My company →
       Communication 菜单 → 列表中点该 OXO → 查看 PBXID 与 Activation code 并复制。
    3. （Tips，p346）管理员也可用 PC 上安装的 Rainbow 应用执行公司配置管理操作。
    4. OMC/Cloud/Rainbow：Cloud 菜单选 Rainbow → 填 Rainbow PABX-ID → 填 Activation code → 勾选
       "Rainbow enabled" → Apply；Domain name 保持默认 openrainbow.com（两凭证均由 Rainbow 生成）。
    5. 查看连接状态（OMC/Cloud/Rainbow 页面）。
    6. 排障-状态：OMC/Tools/Webdiag/Services/Rainbow Status（installer 登录）——确认 "connected
       with final password"。
    7. 排障-系统日志：Webdiag System 页签/System Files/Log files——Rainbow agent 日志
       ccrbagent.log。
    8. 排障-用户侧日志：Rainbow 界面 → User Settings → About Rainbow → 菜单 Open logs。
  verification: |
    Webdiag 的 Rainbow Status 显示 "connected with final password"（p349）。
  conditions: Rainbow 侧公司/PBX 已建（BP 动作）；OMC 可连 OXO。
  tags: [lab, rainbow, pbx-connection, webdiag]

- id: c19
  title: Rainbow 成员手动创建（user1）与 Enterprise 订阅核验
  type: lab
  source_pages: p351-356
  source_chapter: Rainbow accounts configuration and use — "Create new Rainbow user accounts"
  source_quote: |
    "Log in to the Rainbow interface with the client company's administrator account: Login :
    cCpP.admin@ale-training.com … Password: Superuser-P*" (p352)；"On the Services tab, validate the
    Enterprise subscription" (p353)；"Click on Members and then on Create … Fill in the required
    fields" (p354)
  steps: |
    1. 浏览器打开 https://web.openrainbow.com（或 PC 端 Rainbow 应用），管理员登录：cCpP.admin@
       ale-training.com / Superuser-P*（实验口径）。
    2. 核验管理员订阅：Members → 选管理员账户 → Services 页签确认 Enterprise。
    3. 手动建成员：Members → Create → 填：Login=cCpP.user1@ale-training.com；Password=Superuser-P*；
       Sign-in method 保持默认 "Login and password will be asked to sign-in"；Visibility 保持
       "same as company"（公司按 private 管理）；Last name=cCpP；First name=User1；Subscription=
       Enterprise。
    4. 勾选 "Send enrollment email to new users" 提交——平台向用户发开户通知邮件。
    5. （注，p356）查收信：邮件服务器 https://mail44.lwspanel.com/、用户名=邮箱、密码=PasswordP*
       （实验口径）；先删除旧邮件；Warning：检查 Rainbow 平台发出的邮件没有落入 SPAM。
    6. 备注：成员也可用邀请或批量导入方式创建（参考支持站点）。
  verification: |
    Members 列表出现 user1 且 Services 页签为 Enterprise；enrollment 邮件送达且不在 SPAM（p356）。
  conditions: 管理员账户已由讲师创建；培训邮箱为实验专用。
  tags: [lab, rainbow, members, subscription]

- id: c20
  title: 分机关联 Rainbow 账户与 RCC 验证
  type: lab
  source_pages: p357-361
  source_chapter: Associate extension numbers with Rainbow user accounts — How To
  source_quote: |
    "Once associated, members will be able to supervise their phone from Rainbow (unhook, hang up,
    put on hold), this is the RCC (Remote Call Control) mode." (p358)；"Select the Telephony tab …
    Select the extension number related to the member." (p360)；"This number will be retrieved later
    for WebRTC gateway use. It will be automatically configured in Remote Extension number by the
    Rainbow agent … when the user selects "computer" as routing" (p360)
  steps: |
    1. 规划：分机 100→管理员 cCpP.admin、101→成员 cCpP.user1（课堂口径）；虚课：IPDSP 104→管理员、
       user1 在网关实验后配 Anydevice。
    2. Rainbow PC 应用或 https://web.openrainbow.com 用管理员账户登录。
    3. 公司管理图标 → My company → Members → 选成员（例 c2p1.admin）。
    4. Telephony 页签 → Equipment 字段选 OXO Connect → Extension number 选分机（课堂 100、虚课
       104）→ Apply。字段含义：Public number=该用户在 OXO 中的 DDI 号。
    5. 对 USER 1 重复：关联分机 101。
    6. 观察（Notes，p360）：分机列表与 Rainbow 环境实时同步；关联后出现 Rainbow number 字段（例
       BBB10070254106463346）——后续 WebRTC 网关用、用户选 "computer" 路由时由 Rainbow agent 自动
       写入 Remote Extension number。
  verification: |
    书中 RCC 测试（p361）：①呼出——Rainbow 客户端（关联 100/104 的账户）选 "Office phone" 拨 101，
    能否打通；②呼入——从 101 呼 100/104，能否用 Rainbow 客户端接起、有哪些动作可用（接听/挂断/保持，
    音频在话机）。
  conditions: 无 WebRTC 网关时音频只在话机（p358 明示）；此为网关实验前的中间态验收。
  tags: [lab, rainbow, rcc, extension-association]

- id: c21
  title: 内部 WebRTC 网关自动配置（Reseller 激活 + OMC 核验）
  type: lab
  source_pages: p394-399
  source_chapter: Internal WebRTC Gateway automatic configuration on OXO Connect Evolution — How To
  source_quote: |
    "Automatic configuration applies to versions greater than R4.0.020.002" (p395)；"Enable Internal
    WebRTC Gateway … He is the only authorized account to manage this service" (p396)；"OMC / Cloud /
    Rainbow WebRTC Gateway is Connected and Enabled" (p399)
  steps: |
    1. 版本前提：系统版本 > R4.0.020.002；自动配置边界（自动五项/安装员三项）见 p395 Description。
    2. Reseller 管理员登录 Rainbow（实验中由讲师执行；该账户是唯一授权管理此服务的账户）。
    3. Client Company / Communication → Manage connection → 编辑客户公司 PBX。
    4. Information 页签 → 勾选 "Activate WebRTC Gateway"。
    5. Settings 页签 → 选 "Internal" 并设置通道数 → 网关启用；客户管理员可查连接状态。
    6. OMC 核验：OMC / Cloud / Rainbow——WebRTC Gateway 状态 Connected and Enabled。
  verification: |
    书中验收（p399）：OMC/Cloud/Rainbow 显示 WebRTC Gateway is Connected and Enabled。
  conditions: OCE；PBX 已连 Rainbow；Reseller 账户操作。
  tags: [lab, webrtc-gateway, auto-configuration, rainbow]

- id: c22
  title: 虚拟终端配置与分配（Free Rainbow in Twinset / Anydevice）
  type: lab
  source_pages: p400-406
  source_chapter: Create and assign Anydevice/virtual terminals to rainbow user accounts for VoIP
  source_quote: |
    "• Deskphone + Free Rainbow virtual terminal = 1 UTL • Anydevice only = 1 UTL" (p401)；
    "Create Virtual Free Rainbow in Twinset terminal: 130 Associate it with extension 100 as a
    secondary set" (p401)；"Create an AnyDevice terminal: 133 This terminal will be associated with
    the Rainbow user account: cCpP.user1@ale-training.com" (p403)
  steps: |
    用户形态 A（物理分机+Rainbow 应用）：
    1. OMC/Subscribers list → 为用户建 Virtual Free Rainbow in Twinset 虚拟终端：用户 100→终端 130
       （虚课：用户 104→终端 135）（实验口径）。
    2. OMC/Subscribers list → 把该虚拟终端加入用户主分机的副站（secondary set；分机 100 已关联
       Rainbow 账户）。
    用户形态 B（纯 Rainbow 软话机）：
    3. OMC/Subscribers list → 建 Anydevice 终端 133（实验口径）。
    4. Rainbow 侧：Members → User1 → Telephony 页签 → Equipment 选 OXO Connect → 分机号选 133 →
       Apply。
  verification: |
    书中配置后界面验证（p405-406）：形态 A 用户（admin 100/104）可从办公电话/电脑/手机/其它电话管理
    呼叫并可转移；形态 B 用户（user1 133）可从电脑（Rainbow 软话机）/手机/其它电话管理呼叫并转移，
    手机号由用户自行加进 profile。
  conditions: 网关已启用（c21）；UTL 口径=物理话机+Twinset 副站合计 1 UTL、Anydevice 单独 1 UTL。
  tags: [lab, twinset, anydevice, virtual-terminal, utl]

- id: c23
  title: Attendant 订阅、监督组与互助监督组配置
  type: lab
  source_pages: p420-426
  source_chapter: Attendant console and Mutual aid supervision groups — How To
  source_quote: |
    "Companies/Customer companies/ <company to manage> "Subscriptions" section / Service :
    ATTENDANT … Choose the subscription offer: Attendant Monthly DON'T USE "PREPAID" IN THE
    TRAINING" (p421)；""Communication" section / "Supervision" tab Click on "Create"" (p423)；
    "Type Mutual aid group Lock the last member Yes/no" (p425)
  steps: |
    1. 订购 ATTENDANT：Companies/Customer companies/<公司> Subscriptions 区 → Service: ATTENDANT →
       "Subscribe to offer" → 选 Attendant Monthly（培训明确禁用 PREPAID）→ 许可数 1 → Subscribe。
    2. 分配：Members 区 → 编辑用户（例 cCpP.user1）→ Services 页签 → 选 "Attendant Monthly"。
    3. 建监督组：Companies/Customer companies/<公司> Communication 区 → Supervision 页签 → Create →
       填 Name/Description → Create → 选持 ATTENDANT 订阅的监督员（user1）→ 勾选被监督成员；用
       user1 登录即可监督。
    4. 查看话务台：user1 登录 web.openrainbow.com 或应用 → 点图标进入 Attendant console。
    5. 建互助组：同入口 Supervision → Create → 填 Name/Description → Type 选 "Mutual aid group" →
       Lock the last member 选 Yes/No → Create；监督员=cCpP.admin；被监督成员须有物理分机或关联 PBX
       软话机（IPDSP/MicroSIP）。
  verification: |
    书中验收：user1 登录可打开话务台并监督组员；admin 登录可见互助组、可加入/退出组、可对被监督
    PBX 呼叫代接（功能边界见 p416-417：仅 PBX 呼叫、锁定成员不可退、至多监督 4 通）。
  conditions: Attendant 订阅为付费项（月付口径）；互助组成员须关联 PBX 终端。
  tags: [lab, attendant-console, supervision-groups, mutual-aid]

- id: c24
  title: 话机侧初始安装向导（Business 模式）
  type: lab
  source_pages: p445-452
  source_chapter: Initial installation wizard — "Make the initial configuration wizard of an OXO
    Connect from the phone set"
  source_quote: |
    "Check that the OXO is in default configuration, if this is not the case do a cold reset." (p446)；
    "Installation number: 0210141100 • IP address of the CPU: 192.168.1.246 • Numbering plan type:
    3 digits national numbering plan" (p447)；"the Initial Installation Wizard is the one and only
    way to put an OXO a Hotel mode" (p447)
  steps: |
    1. 前提：OXO 处于默认配置（首装或冷复位后）——不是则先做 cold reset。
    2. 从带大屏与话务员菜单的话务台（8039 类）启动：屏显 "Define the Basic System Configuration"
       → 按 "Go on"（否则按 Operator）。注：也可经 OMC 开始屏 Installation Typical 菜单在 PC 侧跑。
    3. 选运行模式 Business（本例；Hotel 只有此向导可进）→ Next。
    4. 填安装号（Public Netw Nbr）0210141100（实验口径）。
    5. 网络配置：CPU IP（MAIN@）192.168.1.246 → OK（Next 按钮默认被遮，按向下箭头）。
    6. 选 3 位内部编号计划 → Choice。
    7. 公共计划：填第一个 DDI（Public Ext）41100 → Down 继续 41101 等 → 全部录完选 "OK All"。
    8. 填公网中继数（主中继组通道数，例 2 B 通道）。
    9. 用户与话务台管理模式：用户 PBX mode、话务台 Intercom mode。
    10. 信箱生成类型：All Terminals 或 None；选语言（实验 English）。
    11. 计费：激活 metering、Charge rate per Unit 保持默认。
    12. 配置日期时间 → Finish → 系统以新配置重启。
  verification: |
    书中验收（p452）：Installation is now finished——系统以新配置重启后编号/中继/信箱按向导值生效。
  conditions: 仅初始状态可跑；Hotel 模式唯一入口（规划前定模式）。
  tags: [lab, installation-wizard, business, phone-set]

- id: c25
  title: 8328 基站与 8214 话机课堂安装（SIP-DECT 单基站）
  type: lab
  source_pages: p453-465
  source_chapter: 8328 base stations and 8214 handsets classroom installation — How To
  source_quote: |
    "OMC/ hardware and limits / LAN/IP Configuration / DHCP tab Enable the built-in DHCP server …
    192.168.1.10 to 192.168.1.69" (p455)；"Username admin Password admin (by default)" (p456)；
    "no_pack_support_for_siphone set its value to true" (p460)；"Registration success !" (p462)
  steps: |
    1. OMC DHCP：OMC/Hardware and Limits/LAN/IP Configuration/DHCP → 启用内置 DHCP、范围
       192.168.1.10-192.168.1.69（实验口径）；IMPORTANT：别忘了在 Subscribers/Basestations List 激活
       Auto-Provisioning。
    2. 8328 网线接入 IP 网络；稍后绿闪=已获 IP。
    3. Web Admin：浏览器开 https://<8328 IP>（例 192.168.1.17）→ admin/admin（默认，实验口径）。
    4. Country 区：国家 France、Time server=192.168.1.254（RLab NTP，实验口径）。
    5. Network 区：核验 DNS 由 DHCP 下发。
    6. Servers 区：把 OXO 声明为 SIP 服务器——Alias=OXO、Registrar=192.168.1.246、Registration
       time=3600s、Sipping 19=Disabled、Remote Caller ID Source Priority=ALERT_INFO–PAI–FROM → Save。
    7. （Tips）不知基站 IP 时：8214 待机按 menu 拨 *47* 进基站搜索。
    8. OXO 侧建分机：OMC/Subscribers/Base stations List → Add an IP Terminal → 目录号 120（实验
       口径）、终端类型 Open SIP Phone → IP/SIP 按钮 → SIP Parameters 页签记录 SIP 密码。
    9. OMC/Voice over IP/VoIP Parameters/Advanced：旗标 no_pack_support_for_siphone=true。
    10. 话机注册（8328 Web Admin）：Extensions/Handset → "Add Handset" → Save → 勾选新行 →
        "Register Handset(s)"。
    11. 话机侧：出厂/未注册话机开机提示 Auto Install? → 左键选 SIP → 输 PIN（默认 0000）→ 输 AC 码
        （8328 管理界面可见可改，默认 0000）→ 提示 Registration success!（主页暂显无 SIP 注册属正常，
        下一步才做）。
    12. 分机声明（Web Admin）：Extensions/Extensions → "Add extension" → 目录号 120、SIP 认证登录
        120、SIP 密码（第 8 步记录的）、语音信箱号 120、语音服务器拨入号 67（OXO 内部计划）→ 勾选
        已注册话机关联 → Save。
    13. 表中出现分机-话机关联（IPEI 分配给 120）；话机屏显终端名与关联。
  verification: |
    书中验收（p462-465）：话机提示 "Registration success !"；Web Admin 表中 IPEI 不再是默认
    FFFFFFFFFF、关联出现在列表；互打测试：话机呼系统内另一用户、从另一用户呼该 DECT 话机。
  conditions: 仅物理课堂（需 8328+8214 硬件）；参考《8328 SIP-DECT SINGLE BASE STATION – System
    Guide》。
  tags: [lab, dect, 8328, 8214, sip]
```

### 任务覆盖自检（task↔id 映射）
- task-02→c01；task-03→c02；task-04→c03；task-05→c04；task-06→c05/c25；task-07→c06；task-08→c07/c08/c09/c10；task-09→c11；task-10→c12；task-11→c13；task-12→c14；task-13→c15；task-14→c16；task-15→c17；task-16→（书中软件下载为讲义无独立 How-To 章，操作序列由 f33 承载）；task-17→（复位为讲义，操作入口由 f34/p17 承载）；task-18→（安全为讲义警告，规则由 p18 承载）；task-19→c18；task-20→c19/c20；task-21→c21（部署）+c22（终端）+f39（外部拓扑序列）；task-22→c22；task-23→c23；task-24→c24。25 条实验覆盖 24 个 task 中全部可在书内动手验证的项；task-16/17/18 的 How-To 缺位为原书事实（讲义形态），已由 framework/principle 承接。
