# 反例/限制/边界/易错点候选 — OXO Connect Starter (OXOCXTE300EN Ed16)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: warning=警告 / limitation=限制 / version-trap=版本陷阱 / misconception=易误解点 / out-of-scope=书外边界
> 逐页扫描 Warning/Note/Tips/IMPORTANT 后汇总；推断性结论标注"（推断）"。

```yaml
- id: n01
  title: IPDSP 安装顺序错会导致 lanpbx 加载失败——先改 IP 再同步时间
  type: warning
  source_pages: p14
  source_chapter: INSTALLING THE IPDSP
  source_quote: |
    "Change the IP settings for the OXO Connect and the PC before installing the IPDSP • This
    ensures that the PC synchronizes with the NTP server and adjusts the time and date. •
    Otherwise, if there is a time difference between the PC and the OXO system, the IPDSP will not
    be able to start. • An error message related to loading the lanpbx file will appear. • This is
    due to the use of digital certificates (the IPDSP uses the HTTPS protocol)."
  summary: |
    顺序敏感：装 IPDSP 前必须先改 OXO 与 PC 的 IP、再把 PC 的"自动设置时间"关掉重开强制同步。PC 与
    OXO 时间不一致 → HTTPS 数字证书时间无效 → IPDSP 无法启动、报 lanpbx 文件加载错误。见到 lanpbx
    报错先查时间同步，别急着重装。
  conditions: 新装 IPDSP 或 IP/时间大改后
  tags: [warning, ipdsp, certificate, time-sync]

- id: n02
  title: FTR 实验仅限实体课堂——虚课环境无法注册 Cloud Connect
  type: limitation
  source_pages: p60
  source_chapter: OCE Start-up & FTR / Implementation
  source_quote: |
    "Virtual class: Not possible to perform. It is not possible to connect the PC to the ETH1 port
    to perform the registration procedure on Cloud Connect. The OCE is initialized with its default
    settings. It will be necessary to use the OMC usual connection procedure in order to change the
    OCE IP configuration."
  summary: |
    FTR 依赖 PC 直连 ETH1 口，远程虚机做不了；虚课时 OCE 保持默认配置，改走 OMC 常规连接改 IP。
    云上交付培训要想演示 FTR 必须有实体设备。
  conditions: 虚拟课堂交付 FTR/Cloud Connect 内容时
  tags: [limitation, ftr, virtual-class]

- id: n03
  title: 每客户密码必须不同——不能一套密码包打天下
  type: warning
  source_pages: p81
  source_chapter: OMC Installation / Define the passwords
  source_quote: |
    "The passwords must be different for each customer! … Passwords can be modified if necessary in
    OMC/Security menu"
  summary: |
    OMC 首连改密时，七个账户密码要按客户区分；后续可在 OMC/Security 菜单再改。这是防"一套密码走
    天下"的硬要求，与 p326-329 防打基线呼应。
  conditions: 所有交付项目
  tags: [warning, passwords, security]

- id: n04
  title: 改 IP/DHCP 后必须 warm reset——配置不会自动生效
  type: warning
  source_pages: p85, p118, p284
  source_chapter: IP settings modification / IP-DECT xBS / Call barring
  source_quote: |
    "Click OK & Re-start the OXO Connect" (p85)
    "Warning Validate and do not forget to make a warm reset, that can be done after DHCP
    configuration" (p118)
  summary: |
    LAN/IP 配置（含 DHCP 池）确认后要做 warm reset 才生效；教材在 IP 修改实验与 DECT 实验两处都
    强调。副中继组编号修改后同样依赖中继组列表刷新（p285 "The previous management of the numbering
    plan gives the following change"）。改完不重启、配置"看着改了没生效"是高频误会。
  conditions: 任何 LAN/IP/DHCP 修改后
  tags: [warning, warm-reset, ip-configuration]

- id: n05
  title: Auto-Provision 忘开是终端注册失败第一原因（三处 IMPORTANT）
  type: warning
  source_pages: p88, p118, p455
  source_chapter: Put in service an IP phone / IP-DECT xBS / 8328 installation
  source_quote: |
    "Enable temporarily Auto-Provision" (p88)
    "IMPORTANT: N'oubliez pas d'activer Autoprovision dans le menu liste des postes" (p118，原书
    残留法文)
    "IMPORTANT: Don't forget to activate Auto-Provisioning in the menu of the Subscribers/
    Basestations List." (p455)
  summary: |
    IP 话机（static/dynamic）、IP-DECT xBS、8328 话机注册全依赖 Subscribers/BaseStations list 里
    的 Auto-Provision；教材三处（含一处未翻译法文）反复强调"别忘开"。终端不上线先查这个开关。
  conditions: 一切 IP 终端开通场景
  tags: [warning, auto-provision, terminal]

- id: n06
  title: Dynamic 与 Dynamic Alcatel 语义不同——选错模式拿不到正确 IP
  type: misconception
  source_pages: p116
  source_chapter: Put in service an IP phone / Notes
  source_quote: |
    "There are 2 modes for Dynamic: Dynamic and Dynamic Alcatel. ­ In the first mode the phone takes
    an IP address from any DHCP server. ­ In the second mode the sets accepts an IP address from an
    Alcatel system (OXO exclusively."
  summary: |
    话机 Dynamic 有两种：Dynamic=任意 DHCP 服务器都接受；Dynamic Alcatel=只接受 Alcatel 系统（且
    仅 OXO）分配的 IP。客户网已有 DHCP 时选 Dynamic Alcatel 会导致拿不到地址；反之安全要求高时
    用 Dynamic Alcatel 防止接错网段。
  conditions: 话机动态模式选择时
  tags: [misconception, dhcp, ip-phone]

- id: n07
  title: 组 500 被语音信箱服务器占用——Hunt group 从 501 起用
  type: warning
  source_pages: p143
  source_chapter: Setting up a hunting group
  source_quote: |
    "Warning: the group 500 is used by the voice mail server!"
  summary: |
    hunt group 500 固定留给语音信箱端口组（VM 接入/自动话务员编在这里，见 p90/p185）；实验与实施
    都从 501 开始（编号计划预置 500-525）。占用 500 会直接破坏信箱与 AA 路由。
  conditions: 规划 hunt group 编号时
  tags: [warning, hunt-group, voicemail]

- id: n08
  title: 广播组接收方必须有扬声器——无扬声器话机收不到广播
  type: warning
  source_pages: p152
  source_chapter: Setting up a broadcast group
  source_quote: |
    "Warning: To receive, a deskphone must have a loudspeaker. In Virtual Classroom there is no
    deskphone with speaker to test. For configuration, use IPDSP to receive and microSip to broadcast"
  summary: |
    广播组 receive 权限只在带扬声器的话机上有效；无扬声器环境（如虚课）用 IPDSP 接收+MicroSIP 广播
    替代。客户采购 Essential 系列低端话机时要提前核对扬声器配置，否则广播业务交付即翻车。
  conditions: 广播组规划与测试
  tags: [warning, broadcast-group, hardware]

- id: n09
  title: 部分功能虚课无法测试——经理秘书组、热线、监听需实体话机
  type: limitation
  source_pages: p155, p178, p193
  source_chapter: manager/secretary group / Automatic routing / Voice Mail management
  source_quote: |
    "In Virtual classroom: No test possible. Requires 2 multiline phones." (p155)
    "In Virtual Classroom: impossible to test. Requires a physical set." (p178)
    "The message screening test will not be possible." (p193)
  summary: |
    三处明示虚课限制：manager/secretary 组需两台 multiline 话机；模拟话机热线（Hotline）需物理话机；
    VM Message Screening 虚课不可测。培训环境下这些功能只配不验，生产验收要补实物测试。
  conditions: 虚拟课堂交付与培训
  tags: [limitation, virtual-class, testing]

- id: n10
  title: "apply diversion" 不勾会禁用一切转移——包括用户自设前转
  type: misconception
  source_pages: p165
  source_chapter: Dynamic routing
  source_quote: |
    "Diversion apply: If "apply diversion" is not ticked, all diversion, including users' forwarding
    (immediate, on-busy, selective…) will be disabled."
  summary: |
    Dyn Rout 页里 "apply diversion" 是总开关：不勾则该话机所有转移（用户立即/遇忙/选择性前转在内）
    全部失效。排障"用户设了前转不生效"时先查这里，再看 Sel Divers 清单与 Feature Rights。
  conditions: 用户前转失效排障
  tags: [misconception, diversion, dynamic-routing]

- id: n11
  title: Screening 功能受密码保护——必须已改非默认密码才能用
  type: warning
  source_pages: p193
  source_chapter: Voice Mail management / Notes
  source_quote: |
    "activation of the feature "Voice Mail: Screening" from the user point of view is password
    protected (user password, must be different from the default password !)"
  summary: |
    信箱监听（边录边听）从用户侧激活时要求输入用户密码，且必须是已改过的非默认密码；默认密码直接
    测试会失败。配套 p184 的弱密码拒绝机制（000000、123456 等系统不收）。
  conditions: 启用 Message Screening 的用户
  tags: [warning, voicemail, screening, passwords]

- id: n12
  title: 公共 SIP 实验跳过短号与紧急号码——ARS 补充配置在书内另一处
  type: limitation
  source_pages: p225, p220-222
  source_chapter: Public SIP Gateway / Implementation / Complementary Setup
  source_quote: |
    "Short numbers and emergency numbers are not processed in this exercise, so no ADL table
    management" (p225)
    "Line 2: copes with all public emergency numbers. The network attribute "emerg" permits the
    line to point automatically to the system list of emergency numbers." (p221)
  summary: |
    c13 实验刻意不含短号/紧急号（无 ADL 表管理）；生产的 ARS 四行模板（0 开头/紧急 emerg/3 开头
    短号/1 开头短号）在 Easy Connect 的 Complementary Setup 一节（p220-222），且国家相关。照抄实验
    配置上生产会漏紧急呼叫路由——这是合规级风险。
  conditions: 实验配置迁移到生产前
  tags: [limitation, ars, emergency-numbers, sip]

- id: n13
  title: Outbound Proxy 必须在 DNS 页签之后配置——顺序依赖
  type: warning
  source_pages: p232-233
  source_chapter: Public SIP Gateway / DNS Tab & Domain Proxy Tab
  source_quote: |
    "Don't forget to now configure the Outbound Proxy: gateway1.itsp1.com in the Domain Proxy tab" (p232)
    "The following setting can only be configured after filling in the DNS tab!" (p233)
  summary: |
    SIP 网关页签有顺序依赖：先配 DNS（DNS A）→ IP 类型才变为 dynamic → 才能填 Domain Proxy 的
    Outbound Proxy。跳序配置会被界面卡住或漏配 Outbound Proxy 导致注册失败。
  conditions: 新建 SIP 网关时
  tags: [warning, sip-gateway, configuration-order]

- id: n14
  title: SIP Media 带宽低于并发数会拒呼——实验要求至少 5
  type: warning
  source_pages: p234
  source_chapter: Public SIP Gateway / Media Tab
  source_quote: |
    "Put the bandwidth at 5 minimum calls in order to allow external calls"
  summary: |
    Media 页签的带宽值=预留的并发通话资源；低于并发需求时外呼被拒。实验下限 5；生产按购买的中继
    通道数配（另受 DSP 通道与许可上限约束，见 p05/p201）。
  conditions: SIP 网关 Media 配置与"外呼打不出"排障
  tags: [warning, sip-gateway, bandwidth]

- id: n15
  title: 实验口径 SIP 流不加密——生产加密要求在 Security 页签外
  type: limitation
  source_pages: p237
  source_chapter: Public SIP Gateway / Security Tab
  source_quote: |
    "SIP flows will not be encrypted to this operator, default value on the OXO Connect Evolution"
  summary: |
    默认与实验口径下 SIP 流不加密（对模拟运营商）；生产对接真实运营商时的 TLS/SIPS 要求取决于运营
    商与 TC1284 对应技术公告，书中不展开。（推断）上生产前要按运营商 TC 核对加密与证书要求。
  conditions: 生产 SIP 中继对接
  tags: [limitation, sip, security]

- id: n16
  title: 欢迎消息默认只有 4 条——20 条需许可
  type: limitation
  source_pages: p244, p250
  source_chapter: Messages 1 to 20 / Preannouncement messages
  source_quote: |
    "According to the Software keys, the system can have 4 to 20 audio messages" (p244)
    "personalize MSG1 to MSG20 welcome messages (4 by default, 20 with license)" (p250)
  summary: |
    MSG1-MSG20 中默认可用 4 条，其余要软件钥匙解锁；总时长 320 秒动态分配。客户要"多时段不同问候"
    时先查许可，别按 20 条设计完交付不了。
  conditions: 话务台组/预公告设计
  tags: [limitation, messages, licensing]

- id: n17
  title: 时段表 End 值=下一行 Start——直接改 End 无效
  type: misconception
  source_pages: p266, p282
  source_chapter: Attendant Group and Time Ranges / Call barring
  source_quote: |
    "End End of the range To modify this column, modify the "Start" column of the next line." (p266)
    "End End of the period : to fill in the end of the period you have to enter the beginning of
    the period below." (p282)
  summary: |
    Time Ranges 的 End 列是派生值：要改某段结束时间，必须改下一行的 Start。两处实验都专门注释了
    这一点——直接编辑 End 会发现"改不动/不生效"。
  conditions: 配置时段表时
  tags: [misconception, time-ranges]

- id: n18
  title: Attendant diversion 键受话务员密码保护
  type: warning
  source_pages: p267
  source_chapter: Attendant Group and Time Ranges / Notes
  source_quote: |
    "Create a function key "Attendant diversion" on the attendant set, with the Common Speed Dialing
    pre-programmed number. (Remind: protected key with operator password)"
  summary: |
    话务台转移键绑定集体缩位号，且是受话务员密码保护的键——普通用户权限改不了。部署时要把话务员
    密码交给话务台管理者并纳入密码管理清单（p02/p94）。
  conditions: 配置话务台转移
  tags: [warning, attendant, keys]

- id: n19
  title: "Inhibition Time-ranges" 不关，话机永远 normal 模式——时段限呼失效
  type: warning
  source_pages: p283
  source_chapter: Call barring management / Notes
  source_quote: |
    "In the set "details/Feature Rights Part 2", disable the parameter "Inhibition Time-ranges", so
    that extensions follow Normal/restricted mode defined in time ranges. Otherwise, the phone sets
    always stay in normal mode even if the system switches in restricted mode."
  summary: |
    默认用户不跟随时段状态（p277）；要让"非营业时间禁外呼"生效，必须逐话机关闭 Feature Rights
    Part 2 的 Inhibition Time-ranges。教材在实验里用注释强调——漏配是"时段限呼不生效"的最常见原因
    （推断：结合默认行为与注释语气判断）。
  conditions: 配置时段限呼后逐用户核对
  tags: [warning, time-ranges, barring, pitfall]

- id: n20
  title: 旧默认密码自 R10.1 起弃用——pbxk1064 仅剩首连用途
  type: version-trap
  source_pages: p95, p67
  source_chapter: Default Configuration / Passwords / Authentication
  source_quote: |
    "Old default passwords (< Release 10.1) Don't use anymore: Installer : pbxk1064 Administrator :
    kilo1987 Attendant: help1954 Download: pbxk1064 NMC: tuxalize Users: 151515 … Also used for
    first installation: pbxk1064" (p95)
    "Default Password: pbxk1064 (First connection)" (p67)
  summary: |
    版本陷阱：网传默认密码表（kilo1987/help1954/tuxalize/151515）是 R10.1 之前的老黄历，现版本
    首启强制定义新密码；pbxk1064 仅剩"首次连接"一个用途。按旧表猜密码做渗透或接管都会失败；交付
    清单要按 p45 实验表+客户自定义口径管理。
  conditions: 跨版本升级/接手存量系统
  tags: [version-trap, passwords, security]

- id: n21
  title: SD 卡恢复仅限同主版本——跨大版本恢复不被支持
  type: limitation
  source_pages: p304
  source_chapter: IP Box SD card Backup/Restore / Misc
  source_quote: |
    "Restore of a recovery point is only supported in the same major release … SDXC is not
    supported … Formatting only via OMC • Supported file system is EXT2"
  summary: |
    SD 卡恢复点不能跨主版本恢复；升级失败想"用升级前的 SD 备份回滚"在大版本跨越时走不通（回滚要
    用软件下载的 switchover 机制，p320）。另：卡 2-32GB、SDXC 不支持、EXT2、仅 OMC 格式化。
  conditions: 升级/回滚方案设计
  tags: [limitation, sd-card, backup, rollback]

- id: n22
  title: 换 PowerCPU EE 后 eMMC 可移植但必须重新生成许可
  type: limitation
  source_pages: p296
  source_chapter: Basic Automatic Data Saving
  source_quote: |
    "POWER CPU EE • Replace Power CPU by a spare one • eMMC flash Eprom of the failed PowerCPU EE
    can be used on the new PowerCPU EE • It is necessary to generate a new license"
  summary: |
    备份存于 MSDB 子板的 eMMC；坏 CPU 更换时 eMMC 可拔到新 CPU 继承数据，但软件钥匙与主 CPU 序列
    号绑定（p71）——必须重新生成 license，否则服务起不来。
  conditions: CPU 硬件更换
  tags: [limitation, licensing, hardware-replacement]

- id: n23
  title: Cold 复位并非清空一切——不勾子选项时保留四类数据
  type: misconception
  source_pages: p323
  source_chapter: System reset / Cold reset options
  source_quote: |
    "When Cold reset is triggered without selecting any sub options • The following settings are not
    deleted: • Installer passwords • Network settings • Management services access flags • Cloud
    Connect parameters"
  summary: |
    "Cold 复位=全清"是误解：不勾子选项时 installer 密码、网络设置、管理服务接入旗标、Cloud Connect
    参数都保留；Factory 才是接近 Lola 出厂态（还删系统日志）。做"转手/回收"流程时想清干净要勾全
    子选项或直接 Factory（p427-428 培训收尾即 Cold Reset 带选项的实例）。
  conditions: 复位选择与设备回收
  tags: [misconception, cold-reset, factory-reset]

- id: n24
  title: 弱信箱密码会被系统拒绝——防打第一道防线
  type: warning
  source_pages: p184, p326-329
  source_chapter: Voice mail initialization / Security warning
  source_quote: |
    "The system do not allow users to configure weak phone passwords (000000,123456…) … The first
    protection against phreaking is • Change frequently the voice mail password • Don't use simple
    digit sequence for the password" (p184)
    "The victims can loose more than 20 K€ in one weekend … The freaking is a business run by
    organised crime" (p326)
  summary: |
    系统拒绝 000000/123456 类弱信箱密码；教材把"常改密码+不用简单序列"列为防打第一道防线，并给出
    盗打损失口径（一个周末 2 万欧以上、有组织犯罪）。信箱弱密码是盗打重放的主要入口（推断：结合
    p326 场景与 p184 位置判断）。
  conditions: 信箱初始化与安全基线
  tags: [warning, voicemail, phreaking, passwords]

- id: n25
  title: Rainbow 平台邮件可能落入 SPAM——开户验证前必查
  type: warning
  source_pages: p356
  source_chapter: Rainbow accounts configuration / Notes & Warning
  source_quote: |
    "PLEASE DELETE THE OLD EMAILS IN THE MAILBOX … Warning CHECK THAT THE EMAILS SENT BY THE RAINBOW
    PLATFORM DO NOT ARRIVE IN THE SPAM."
  summary: |
    实验邮箱要先清旧邮件；Rainbow 平台发出的开户/通知邮件必须确认未进 SPAM——进了 SPAM 会让
    "没收到邮件=没建成账户"的误判，也可能让后续验证邮件持续丢失。生产客户邮箱同样适用（白名单
    发件域，推断）。
  conditions: 成员创建/邀请流程
  tags: [warning, rainbow, email]

- id: n26
  title: Rainbow 域名保持默认 openrainbow.com——不要自行改
  type: warning
  source_pages: p347
  source_chapter: Connect an OXO to Rainbow
  source_quote: |
    "Domain name Leave the default value: openrainbow.com"
  summary: |
    OMC/Cloud/Rainbow 页的 Domain name 明确"保持默认 openrainbow.com"。自作主张改成客户自有域名
    会断开与平台的连接（推断：结合"Leave the default value"的祈使语气与连接排障上下文）。
  conditions: PBX 接入 Rainbow 配置时
  tags: [warning, rainbow, domain]

- id: n27
  title: Multiset 副站终端类型随版本变——R6.0 起必须 Twinset，R5.2 前是 Anydevice
  type: version-trap
  source_pages: p368, p401
  source_chapter: Deployment steps on OXO Connect / virtual terminals
  source_quote: |
    "The main station is the physical station • The secondary station is • Free Rainbow in Twinset
    from R6.0 • (Anydevice up to R5.2) … Note: Until Release 5.2 the AnyDevice equipment was also
    used as a secondary station in multiset … Secondary station from Release 6.0: The Free Rainbow
    in Twinset virtual terminal must be used in order to save an UTL license (UTL Bypass)" (p368)
  summary: |
    版本陷阱：给"物理话机+Rainbow"用户建副站时，R5.2 及以前建 Anydevice、R6.0 起必须建 Free
    Rainbow in Twinset 才能省 UTL（UTL Bypass）。照旧文档给 R6.x 系统建 Anydevice 副站=多烧一个
    UTL（推断：结合 UTL 口径 p401）。
  conditions: 跨版本升级与终端配置
  tags: [version-trap, twinset, anydevice, utl]

- id: n28
  title: WebRTC 自动配置有版本下限 R4.0.020.002——低版本必须手工
  type: version-trap
  source_pages: p366, p395
  source_chapter: Automatic configuration / Internal WebRTC Gateway automatic configuration
  source_quote: |
    "The automatic configuration of the internal / external WebRTC gateway is available from system
    version R4.0.020.002" (p366)
    "Automatic configuration applies to versions greater than R4.0.020.002" (p395)
  summary: |
    自动配置五项只在 R4.0.020.002 以上可用；低版本系统要走全套手工 SIP 网关/SIP 账户/VoIP 接入/
    中继组/ARS 配置（参考 c13 的配置地图）。升级与自动化路径要先看版本。
  conditions: WebRTC 网关部署前核对版本
  tags: [version-trap, auto-configuration, webrtc-gateway]

- id: n29
  title: OCE-FE 强制双机 ≥R4.0 MD——FE 与呼叫服务器版本都要到位
  type: version-trap
  source_pages: p373
  source_chapter: Use case # 2 OCE Front End / Introduction
  source_quote: |
    "The release ≥ R4.0 MD must be installed on both the Front-End RGW and the OXO Connect call
    server … Release ≥ R4.0 MD is mandatory"
  summary: |
    OCE-FE 方案里 FE 网关与呼叫服务器两台都必须 ≥R4.0 MD，缺一台不满足即不可用；FTR 会"提供 FE
    许可并按需升级版本"（p375）——但呼叫服务器侧的升级要自己排。给低于 R4 的存量 PBX 加 FE 属于
    cookbook 多场景之一（p382），别想当然直接装。
  conditions: OCE-FE 选型与部署
  tags: [version-trap, oce-fe, r4]

- id: n30
  title: FTR 默认 PBXID 是占位符 "FleetRef-Installref"——正式接入前要替换
  type: warning
  source_pages: p379
  source_chapter: OCE Front End / OMC configuration
  source_quote: |
    "On the OXO, by entering an FTR, the PBXID and the activation code are initialized by default to
    "FleetRef-Installref", which allows the installer to prepare the equipment in advance in RB
    WebAdmin … Note: if the Rainbow company was already created put also the PbxId in both OXO"
  summary: |
    FTR 后 PBXID/激活码是占位值（FleetRef-Installref），允许提前在 RB WebAdmin 备料；正式接入要把
    真实 PBXID 同时填到 FE 与呼叫服务器两台（两台必须一致）。占位符当真值用会连到错误公司或不连。
  conditions: OCE-FE 交付与多站点备料
  tags: [warning, pbxid, ftr, oce-fe]

- id: n31
  title: OCE-FE 修改后要 warm reset；容量组合有"不支持"格
  type: warning
  source_pages: p374, p377
  source_chapter: OCE Front End / status & capacity
  source_quote: |
    "A warm reset is necessary to take into account modification to Rainbow WebRTC Gateway on OCE
    Front-End" (p377)
    "Type of Rainbow GW … Internal GW Not supported 20 calls max. … OCE-FE GW 20 calls max. Not
    supported" (p374)
  summary: |
    FE 相关修改（含 Rainbow WebRTC Gateway 配置）要 warm reset 才生效；容量矩阵两格"不支持"：内部
    网关不支持 PowerCPU EE、OCE-FE 网关不支持 IPBox 呼叫服务器。选错硬件组合在部署后期才暴露。
  conditions: OCE-FE 部署与硬件选型
  tags: [warning, oce-fe, warm-reset, capacity]

- id: n32
  title: 容量表 70 用户以上"集成/FE 通道列"为 NA——20 通道撑不住中高话务
  type: limitation
  source_pages: p392
  source_chapter: Rainbow WebRTC gateway dimensioning
  source_quote: |
    "70 27/NA 70(*) … 150 50/NA 150(*) … (*) Integrated WebRTC on OCE: the maximum Rainbow Users
    with VoIP limits depends on the number of configured Rainbow Channel and end user traffic. Value
    indicated here is for direction only for 20 configured WebRTC GW channels. But Maximum limit is
    150 that is ok in case of very low traffic"
  summary: |
    集成/FE 拓扑 20 通道封顶：70/100/150 用户的推荐通道列标 NA——要上外部网关（至 50 通道）。表中
    集成列 70-150 用户值是"20 通道+极低话务"下的方向性参考，不是承诺值。售前按表拍 20 通道撑 150
    用户是高风险承诺。
  conditions: 容量规划与售前承诺
  tags: [limitation, capacity, dimensioning]

- id: n33
  title: 自动配置只能 Reseller 管理员做——客户管理员点不了
  type: limitation
  source_pages: p396, p338
  source_chapter: Internal WebRTC Gateway automatic configuration / ADMINISTRATORS PROFILES
  source_quote: |
    "Automatic activation of the WebRTC gateway is performed by the trainer with a reseller
    administrator account … He is the only authorized account to manage this service" (p396)
    "RESELLER / BP ADMINISTRATOR … Create PBXs & activate WebRTC gateways" (p338)
  summary: |
    WebRTC 网关激活/通道数设置是 Reseller/BP 账户专属；客户管理员只能"查连接状态"（p398）。现场
    客户管理员"没有这个按钮"是权限设计而非故障——要走 BP 流程。
  conditions: WebRTC 网关激活
  tags: [limitation, rainbow, reseller, permissions]

- id: n34
  title: 互助监督组只认 PBX 呼叫——Rainbow 软话机呼叫不可代接
  type: limitation
  source_pages: p416, p426
  source_chapter: MUTUAL AID SUPERVISION GROUP / How To
  source_quote: |
    "You can pickup calls Works only for PBX calls, not for Rainbow softphone calls" (p416)
    "These members must have a physical extension or an associated PBX softphone (IPDSP or
    MicroSIP)." (p426)
  summary: |
    互助组代接只对 PBX 呼叫生效，Rainbow 软话机呼叫不在监督/代接范围；被监督成员必须有物理分机或
    关联 PBX 软话机（IPDSP/MicroSIP）——纯 Anydevice 用户进互助组没有监督价值。另外锁定成员
    （Lock the last member）不可退出、监督视图至多 4 通（p417）。
  conditions: 互助组设计与成员准入
  tags: [limitation, mutual-aid, supervision]

- id: n35
  title: 话务台功能只在 PC 上——话机与手机无任何话务台功能
  type: limitation
  source_pages: p414
  source_chapter: ATTENDANT CONSOLE - MISCELLANEOUS
  source_quote: |
    "The attendant may have a deskphone, but none of the functionalities are possible on the
    deskphone itself. • Same behaviour for a smartphone Attendant features are only available on PC
    (thick client or web mode)"
  summary: |
    Rainbow 话务台是纯 PC（厚客户端/Web）功能：话务员的物理话机和手机上没有任何话务台能力。客户
    期望"在话机上用话务台"时要提前纠偏；队列/保持数还取决于软话机线的多线资源（OXE REX 10、OXO
    Connect Any Device 最低 R6 至 8）。
  conditions: 话务台选型与用户沟通
  tags: [limitation, attendant-console]

- id: n36
  title: 培训订阅演示禁用 PREPAID——生产按客户计费模式选
  type: warning
  source_pages: p421
  source_chapter: Attendant console / Subscribe to ATTENDANT subscription
  source_quote: |
    "Choose the subscription offer: Attendant Monthly … DON'T USE "PREPAID" IN THE TRAINING"
  summary: |
    订阅有两种计费形态（Monthly 月付/Prepaid 预付）；培训环境必须选 Monthly 以免产生真实预付扣费。
    （推断）生产选型时两种形态的退订/余额规则不同，报价前要与渠道确认。
  conditions: Rainbow 订阅开通（培训与生产）
  tags: [warning, subscription, training]

- id: n37
  title: Hotel 模式只能经初始安装向导进入——配完再切要冷复位
  type: misconception
  source_pages: p72, p447, p91
  source_chapter: OMC installation wizard / Initial installation wizard / Default Configuration
  source_quote: |
    "The OMC installation wizard allows to choose between Business or Hotel at the very first
    installation (and after a cold reset)" (p72)
    "Note: the Initial Installation Wizard is the one and only way to put an OXO a Hotel mode" (p447)
  summary: |
    Business/Hotel 是安装向导第一步且向导只在初始状态可跑——商业系统想切酒店版必须冷复位重来
    （丢全部客户配置）。酒店项目的模式决策必须前置；Hotel 版有独立预置（电话亭位、Guest 信箱等，
    p91/p186）。
  conditions: 酒店/企业项目模式决策
  tags: [misconception, hotel, wizard, cold-reset]

- id: n38
  title: 8328 出厂动态 IP——没有 DHCP 就管理不了
  type: limitation
  source_pages: p455-456
  source_chapter: 8328 base stations classroom installation
  source_quote: |
    "The factory IP configuration of an 8328 base station is a dynamic IP configuration. Therefore,
    a DHCP server must be present and configured in order to respond to the request from this DECT
    8328 base station." (p455)
    "If you don't know the IP address of the base station 8328 … on the handset in the idle state,
    press the "menu" button, then dial *47*, you will access the base station search function" (p455)
  summary: |
    8328 出厂只做 DHCP；现场没有 DHCP 时基站拿不到 IP、Web Admin 无从谈起。找不到基站 IP 用 8214
    话机 menu+*47* 搜基站。Web Admin 默认 admin/admin——部署完必须改（推断：结合 p326-329 安全基调）。
  conditions: 8328 部署与安全加固
  tags: [limitation, 8328, dhcp, default-credentials]

- id: n39
  title: 8214 走 SIP 前要改 OXO 旗标 no_pack_support_for_siphone
  type: warning
  source_pages: p460
  source_chapter: 8328 installation / Change the VoIP Flag
  source_quote: |
    "Change the VoIP Flag in Advanced Settings: OMC/Voice over IP/VoIP Parameters/Advanced …
    no_pack_support_for_siphone set its value to true"
  summary: |
    8214 话机在 8328 体系下以 Open SIP Phone 接入，OXO 侧要先置 noteworthy 旗标
    no_pack_support_for_siphone=true，否则注册/呼叫异常。这是"照普通 IP 话机流程配完不通"的差异点。
  conditions: 8328+8214 部署
  tags: [warning, 8214, noteworthy, sip]

- id: n40
  title: 话机注册成功≠SIP 注册完成——"无 SIP 注册"提示属正常中间态
  type: misconception
  source_pages: p462
  source_chapter: 8328 installation / Starting Registration on the 8214 Handset
  source_quote: |
    "After a while, you will receive a message to inform you of the successful registration:
    Registration success ! After a while, the "home page" will indicate that there is no SIP
    registration, which is normal, as this step is going to be done in the next step."
  summary: |
    两段注册：先 DECT 层注册成功（Registration success!），主页显示"无 SIP 注册"是正常中间态——
    SIP 分机声明在下一步（Extensions/Extensions → Add extension）。看到"无 SIP 注册"就回头重注册
    是走错路。
  conditions: 8328+8214 部署
  tags: [misconception, 8214, registration]

- id: n41
  title: MoH 只对外线保持生效——内线保持是哔哔音
  type: misconception
  source_pages: p247
  source_chapter: Music on hold
  source_quote: |
    "Reminder: this music is only used when putting on hold external calls (beep beep with internal
    calls)"
  summary: |
    定制保持音乐只在外线保持时播放；内线保持是提示音。客户验收"内线保持怎么没音乐"是产品行为，
    不是配置故障。
  conditions: MoH 验收
  tags: [misconception, moh]

- id: n42
  title: SIP 网关建好后必须回填 VoIP 接入的 Gateway index
  type: warning
  source_pages: p206, p230, p239
  source_chapter: SIP Gateway configuration / Public SIP Gateway
  source_quote: |
    "Must be configured as soon as a Public SIP gateway is created" (p206)
    "The Gateway index must be filled in later when the SIP Gateway is created" (p230)
    "Associate the newly created gateway with the VoIP trunks" (p239)
  summary: |
    顺序闭环：先建 VoIP 接入（此时 Gateway index 空着）→ 建网关 → 再回 List of Accesses 把网关联
    到接入。漏回填=接入没有网关=不注册不呼出。属于"每一步都对但整体不通"的典型断点。
  conditions: SIP 网关与 VoIP 接入配置
  tags: [warning, sip-gateway, configuration-order]

- id: n43
  title: 安全与生产化内容全书外置——TC1143/TC1284/TC1994/TC2479/cookbook 五份指针
  type: out-of-scope
  source_pages: p327-329, p199, p216, p368, p380-382
  source_chapter: Security warning / SIP Provider list / SIP Profile / WebRTC Gateway / OCE-FE
  source_quote: |
    "Refer to the SECURITY chapter from The Expert Documentation •See Security Recommendations for
    OXO system document: TC1143_Security_Recommendations_for_OXO_Connect" (p327)
    "For a complete list, refer to the technical communication: TC1284 Public SIP Trunking
    Interoperability and Technical Support procedure" (p199)
    "Refer to TC1994: SIP Easy Connect: SIP Trunk Profile Import/Export" (p216)
    "TC2479 Rainbow WebRTC Gateway with OXO Connect / OXO Connect Evolution" (p368)
    "For this it is essential to follow the document "Rainbow WebRTC cookbook" latest edition
    available on MyPortal" (p382)
  summary: |
    五份书外文档是生产化的真正依据：TC1143（安全加固）、TC1284（SIP 运营商兼容与支持流程）、
    TC1994（SIP Profile 导入导出）、TC2479（OXO 的 Rainbow WebRTC 网关）、Rainbow WebRTC cookbook
    （OCE-FE 多场景开通，且"必须跟最新版"）。本教材只承担课堂闭环；把书内实验口径直接当生产方案
    是越界使用。
  conditions: 一切生产交付
  tags: [out-of-scope, tc-documents, production]

- id: n44
  title: 明文实验密码贯穿全书——生产严禁照搬
  type: warning
  source_pages: p61, p67, p95, p345, p456, p462
  source_chapter: 全书实验步骤（密码汇总见 BOOK_OVERVIEW 批判节）
  source_quote: |
    "Login: installer Pwd: pbxk1064 At the very first time, the system asks to put a new password,
    put Alcatel1 during the training" (p61)
    "Password: Superuser-P* (P : pod number)" (p345)
    "Username admin Password admin (by default)" (p456)
  summary: |
    pbxk1064、Alcatel1、alcatel（SIP 账户）、Superuser-P*、PasswordP*、admin/admin、0000 全部是
    教学约定值且明文印刷。生产环境沿用任何一个是重大安全隐患（与 p326-329 防打基线直接冲突）；
    从本书提取的任何 skill/清单都必须标注"实验口径"并强制替换。（推断：安全结论由教材自身安全章
    节立场推出）
  conditions: 所有从本书派生的操作指南
  tags: [warning, passwords, lab-values, security]

- id: n45
  title: 部分讲义残留法文与未解释术语——跨版本阅读要小心
  type: limitation
  source_pages: p27, p88, p58
  source_chapter: Hardware Portfolio / IP-DECT DHCP / Power button
  source_quote: |
    "IMPORTANT: N'oubliez pas d'activer Autoprovision dans le menu liste des postes" (p88)
    "Bornes DECT … Combinés DECT … Hybride TDM/IP" (p27)
    ""LOLA" mode" (p58)
  summary: |
    Ed16 存在未翻译残留（p27 硬件页 Bornes/Combinés、p88 IMPORTANT 法文句）；"LOLA 模式/Lola 安装
    态"（p58、p322）在书内无定义。读者遇到这两处要按上下文理解（LOLA=出厂引导态），并注意原书质量
    信号——细节以最新版英文文档为准。
  conditions: 全书阅读与文档引用
  tags: [limitation, documentation-quality]

- id: n46
  title: 外线前转等能力靠 Feature Rights 放行——"配了键不生效"先查权限
  type: misconception
  source_pages: p176, p179-181
  source_chapter: Users' settings and features management
  source_quote: |
    "Only the manager will be allowed to forward his calls to the outside … In the Feature Rights
    first part validate the parameter External Diversion" (p181)
    "In the Feature Rights first part validate the parameter "Intrusion Allowed"." (p179)
  summary: |
    插入/外转等能力的完整链路=Feature Rights 放行（Features 页）+键或前缀配置（Keys 页）两段；
    只建键不开权不生效，只开权没键则用不了。业务要求"仅经理可外转"这类约束也在 Feature Rights 层
    实现（其余用户不开即禁）。
  conditions: 用户功能配置与排障
  tags: [misconception, feature-rights, keys]

- id: n47
  title: Webdiag 抓包文件可直接交技术支持——但登录要用 installer 身份
  type: limitation
  source_pages: p241-242
  source_chapter: Public SIP Gateway / Test
  source_quote: |
    "OMC/Tools/Webdiag Login = installer Password = Alcatel1 for example … In the menu at the left
    select TCP Dump traces Choose SIP And start the capture … This trace can be saved and
    transmitted to technical support for analysis"
  summary: |
    Webdiag（含抓包、Rainbow Status、证书管理）统一走 installer 会话；TCP Dump 选 SIP 过滤、停止后
    自动生成文件、可交 TSS 分析（任意嗅探器亦可）。边界：Webdiag 是诊断入口不是配置工具（ETH1 场景
    只许诊断与改 ETH0 参数，p57）。
  conditions: SIP 与 Rainbow 排障
  tags: [limitation, webdiag, troubleshooting]
```

### 任务覆盖自检（task↔id 映射）
- task-01（采集）→n12（短号/紧急号盲区提示）；task-02（FTR）→n02/n30；task-03（OMC）→n03/n20；task-04（IP）→n04；task-05（话机）→n05/n06；task-06（DECT）→n38/n39/n40；task-07（编号）→（无独立反例，冲突处理见 c06/f18）；task-08（组）→n07/n08/n09；task-09（用户功能）→n10/n46；task-10（信箱）→n11/n24；task-11（SIP）→n12/n13/n14/n15/n42/n47；task-12（消息）→n16/n41；task-13（呼入）→n17/n18；task-14（出局）→n19；task-15（备份）→n21/n22；task-16（软件）→n21（同主版本回滚边界）；task-17（复位）→n23；task-18（安全）→n24/n44/n43；task-19（接入 Rainbow）→n25/n26；task-20（成员/分机）→n25；task-21（网关）→n27/n28/n29/n30/n31/n32/n33；task-22（虚拟终端）→n27；task-23（话务台）→n34/n35/n36；task-24（向导）→n37。24 个 task 全覆盖，无遗漏。
