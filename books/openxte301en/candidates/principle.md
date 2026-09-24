# 原则/清单/规则/公式/数值口径候选 — OpenTouch Advanced (OPENXTE301EN Ed08, R2.6.1)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号、号码）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: Nomadic 资源池定量规则——1 路蜂窝=1 Ghost Z；1 路 VoIP=1 Ghost Z + 1 SIP 设备；占满至关闭
  type: formula
  source_pages: p47, p51
  source_chapter: OTC PC for Connection users in nomadic mode
  source_quote: |
    "The system requires ONE Ghost Z set for each Nomadic connection ... Ghost Z sets are retained as busy
    throughout the connection and are only released when nomadic mode is disabled. Ghost Z sets are managed
    as pools of resources. So, it is very important to know how many Nomadic connections will be established
    simultaneously, because the quantity must equal the number of Ghost Z sets available in the Oxe system." (p47)
    "For each Nomadic SIP connection, the system requires: 1 SIP device ... 1 Ghost Z set ... SIP devices &
    Ghost Z sets are managed as pools of resources." (p51)
  summary: |
    容量公式：池规模 = 最大并发 nomadic 连接数。蜂窝模式每连接消耗 1 个 Ghost Z；VoIP 模式每连接消耗
    1 个 Ghost Z + 1 个 SIP 设备（SIP 设备整个会话期被占用）。资源在用户关闭 nomadic 前一直 busy，
    不随通话结束释放。实验建了 3 个 Ghost Z（31017/31018/31019）与 2 个 SIP 设备（31951/31952，实验口径）。
  conditions: 池资源可在 OXE/OT 两侧按范围登记；规划输入是并发用户数
  tags: [formula, capacity, nomadic, ghost-z]

- id: p02
  title: Connection 用户软话音编解码与 QoS 口径
  type: metric
  source_pages: p36, p44
  source_chapter: Nomadic use cases / Summary table
  source_quote: |
    "The SoftPhone is based on SIP signaling • Supported codecs (G711 / G729 / G723.1 / G722.2) • Packet Loss
    Concealment (PLC), Voice Activity Detection • VLAN tagging is not supported • Quality of Service based on
    IP TOS field • Echo cancellation • Restriction: SIP survivability (OXE CS, OXE PCS, third party sip
    gateway) is not supported" (p36)
    "Voice over IP communications are SIP-based with narrowband (G.711u/a, G.729a, G.723) and wideband
    (G.722.2) audio codecs." (p44)
  summary: |
    软话音口径：SIP 信令；编解码窄带 G.711u/a、G.729a、G.723（.1）+ 宽带 G.722.2；支持 PLC 抖动隐藏与
    VAD；VLAN 打标不支持；QoS 依据 IP TOS 字段；带回声消除；硬限制——SIP 生存性（OXE CS/OXE PCS/第三方
    SIP 网关）不支持。网络规划与故障定界按此口径。
  conditions: 适用于 nomadic VoIP 与 Softphone 模式
  tags: [metric, codec, qos, voip]

- id: p03
  title: OT 许可/权限成对规则——Nomadic GSM+Desktop、Nomadic SIP+Desktop、Desksharing 释放要 Flex Office+Desktop
  type: rule
  source_pages: p46, p49, p54, p72
  source_chapter: Nomadic How-To / DeskSharing How-To
  source_quote: |
    "Note that a 'Desktop' license must be assigned to the user to be able to activate nomadic mode from OTC
    PC desktop client" (p46)
    "Nomadic GSM Must be enabled / Desktop Must be enabled" (p49)
    "Nomadic SIP Must be enabled / Desktop Must be enabled" (p54)
    "Enable the following licenses in order to be able to release (LogOff) the DSS from the OTC PC client:
    Desktop • Flex Office" (p72)
  summary: |
    许可组合三条：蜂窝 nomadic = Nomadic GSM + Desktop（licenses 页签）；VoIP nomadic = Nomadic SIP +
    Desktop；OTC PC 远程释放 DSS = Desktop + Flex Office。会议/桌面协作场景（另章）为 Desktop +
    Conferencing。缺任一许可时功能入口直接不可用，排障先查 Licenses 页签。
  conditions: 权限在 OT 侧 Users and Devices/User → Licenses 配置
  tags: [rule, licensing, nomadic, desksharing]

- id: p04
  title: DSU 虚拟 MAC 规则：aa:bb + 目录号十六进制；DSS 用真实 MAC
  type: formula
  source_pages: p65-66, p68
  source_chapter: DeskSharing How-To
  source_quote: |
    "For a DSU, the MAC address is a virtual one. This MAC address appears immediately after the creation of
    the user, and is based on the following rule: 'aa:bb:xx:xx:xx:xx' where xx:xx:xx:xx is the directory
    number. Example for 31000: 'aa:bb:03:10:00'" (p67)
    "Directory Number 31000 / Terminal Ethernet Address aa:bb:00:03:10:00 / IP Address unused" (p68)
    "For a DSS, the MAC address is the device real one. This MAC address appears after the registration of
    the physical set (with the directory number 31100)." (p66)
  summary: |
    两条 MAC 规则：DSU 的 MAC 是系统生成的虚拟值 = "aa:bb:" + 6 位目录号 hex（31000 → aa:bb:00:03:10:00），
    建号即出现、IP 字段 unused；DSS 的 MAC 是物理话机真实地址，注册后才显示。命令行维护时可用 MAC 反查
    DSU 当前登录在哪台 DSS（ippstat）。
  conditions: ippstat 显示 DSU 未登录时 INTIP 为 255/255、登录后为 DSS 的 INTIP
  tags: [formula, desksharing, mac, metric]

- id: p05
  title: Desksharing 系统参数四件——免密登出/定时登出/忙时重置/默认密码修改
  type: checklist
  source_pages: p70-71
  source_chapter: DeskSharing How-To / System parameters management
  source_quote: |
    "Activate Logoff without pwd — False: (default value) The DSU must dial its secret code in order to log
    off. True: The DSU can activate the log off without entering its secret code." (p70)
    "DSU Auto Log-off Time — -1: (default value) the feature is not activated; 0 to 23: time when the
    automatic log off is activated for all the DSU ('20' means 8 PM)" (p70)
    "Allow Reset of Busy DSU — True: if a DSU is busy (on line), the call is released and it can be log off
    ... An incident '6004' is generated. False: ... In case of log on from another DSS, a message
    'Unauthorized' is displayed." (p71)
    "Default DSU Secret Code Change — True: Desk Sharing Users will be prompted to change their Secret code
    at first login if they have the Default one." (p71)
  summary: |
    四个系统参数（/System/Other System Param./System Parameters 与 Spec. Customer Features Parameters）：
    ①Activate Logoff without pwd（默认 False=需密码）；②DSU Auto Log-off Time（-1 关闭；0-23 为整点自动
    登出，"20"=晚 8 点）；③Allow Reset of Busy DSU（True=释放通话强制登出并产生 6004 事件；False=保持通话，
    他机登录显示 Unauthorized；自动登出时若在通话则 DSU 保持登录）；④Default DSU Secret Code Change
    （True=首登强制改默认密码）。
  conditions: 事件 6004 可用 incvisu 查看（p73）
  tags: [checklist, desksharing, system-parameters]

- id: p06
  title: 实验口径：POD 服务器设置总表（IP/账号/密码全集）
  type: metric
  source_pages: p9, p17
  source_chapter: Training lab environment / Settings
  source_quote: |
    "OXE OPEN_OXE_ADVANCED csa (physique) csm (principal) 192.16.8.1.1 192.16.8.1.3 255.255.255.0
    192.168.1.254 mtcl swinst root / mtcl SoftInst letacla
    OMS OPEN_OMS 192.168.1.13 root letacla1
    OPENTOUCH OPEN_OTMS_ADVANCED opentouch 192.168.1.50 root superuser
    8770 OPEN_8770_ADVANCED nms 192.168.1.70 Administrator adminnmc Superuser Superuser01*
    DCS OPEN_DCS dcs 192.168.1.31 Administrator superuser
    ECOSYSTEM OPEN_ECOSYSTEM eco 192.168.1.100 Administrator superuser
    PC CLIENT 10/11 client10/11 192.168.1.10/.11 Administrator superuser" (p9，实验口径)
  summary: |
    实验口径（RLAB 专用，生产必须替换）：OXE 主/备 CPU 192.16.8.1.1 / 192.16.8.1.3（原文如此，疑为
    192.168.1.1/3 的排版变体），账号 mtcl/mtcl、swinst/SoftInst、root/letacla；OMS 192.168.1.13
    root/letacla1；OpenTouch 192.168.1.50 root/superuser；8770 192.168.1.70 adminnmc/Superuser01*；
    DCS 192.168.1.31 与 ECOSYSTEM 192.168.1.100 均 Administrator/superuser；PC Client 10/11 =
    192.168.1.10/11。子网掩码 255.255.255.0、网关 192.168.1.254。
  conditions: 仅 RLAB；IPDSP 软话机 TFTP 指向 OXE CS Main 192.168.1.3（p27）
  tags: [metric, lab, credentials]

- id: p07
  title: 实验口径：ITSP1 账号与号码规则（pbxP/alcatel、PN 两位、3321PN41000）
  type: metric
  source_pages: p20-23, p29-30
  source_chapter: SIP Carrier Simulator / Pod Configuration
  source_quote: |
    "PBX (POD P) Id: pbxP password: alcatel ... Public numbers: Id: publicP@itsp1.fr password: public ...
    Emergency numbers: id: urgenceP@itsp1.fr Password: public" (p20)
    "National numbers 3311PN12345 3321PN12345 3331PN12345 3341PN12345 3351PN12345 ... Mobile numbers
    3361PN12345 3371PN12345 ... International call to UK 4421PN12345 ... 112, 15, 17, 18" (p21)
    "PBX installation nb 3321PN ... DDI table - First external nb 41000 ... DDI table - First internal nb
    31000 ... Range size 500 ... Example: 31001's external nb 3321PN41001" (p23)
    "Registration ID: pbxN ... First external number: 33210N41000 ... First internal number: 31000 ... Range
    size 500" (p29-30)
  summary: |
    实验口径（RLAB 专用）：SIP 账号 pbxP/alcatel（P=POD 号）；公网/紧急两 SIP 用户 publicP、urgenceP 密码
    public；号码段——国内 33[1-5]1PN12345（主号 3321PN12345）、移动 3361/3371PN12345、国际英国 4421PN12345、
    紧急 112/15/17/18；本 PBX 安装号 3321PN、DDI 首外线 41000（全 POD 同）、首内线 31000、范围 500，内线
    31001 对应外线 3321PN41001。OXE 外部 SIP 网关：Registration ID 与 Outgoing username 均填 pbxN；DID
    翻译 First external 33210N41000 / First internal 31000 / Range 500。呼出变换：拨 0110312345 →
    +33110312345。
  conditions: PN 为两位 POD 号；纯教学基础设施
  tags: [metric, lab, sip, numbering]

- id: p08
  title: Wi-Fi→GSM 实时溢出的 SIP 参数三件——Decline 映射、INVITE 重传 2-3 次、T310=60
  type: metric
  source_pages: p126
  source_chapter: OTC smartphone How-To / SIP settings and timers for overflow
  source_quote: |
    "SIP/ SIP to Ch Error Mapping — Verify the cause for 'Decline'. ... CH Cause Temporary failure" (p126)
    "SIP/ SIP Proxy — Verify the number of INVITE retransmissions ... Retransmission number for INVITE 2 or 3" (p126)
    "Verify the timer 310 of COS 31 for SIP trunk group: External Services/Trunk COS ... Timer T310 60" (p126)
  summary: |
    为实现 Wi-Fi 到 GSM 的近实时倒换，三个参数口径：①SIP/SIP to Ch Error Mapping 中 "Decline" 响应映射的
    CH Cause 应为 Temporary failure；②SIP Proxy 的 INVITE 重传次数设 2 或 3；③SIP 中继组所用 Trunk COS
    （COS 31）的定时器 T310 = 60。任一不满足都会让溢出切换变慢或失败。
  conditions: 建议值；菜单路径在 OmniVista OXE 配置窗口
  tags: [metric, sip, timers, smartphone]

- id: p09
  title: 直达速拨号范围规则——长度不能为 0 也不能满；Ghost Z 编号可用 B 前缀
  type: rule
  source_pages: p125, p132
  source_chapter: OTC smartphone How-To
  source_quote: |
    "The system will have to automatically use Direct Speed Dial numbers for automatic substitution to the
    remote extensions. The range size CANNOT be 0 and also should NOT be full." (p125)
    "Index for 1st speed dial number 0 (default value) ... Length for speed dialing numbers Specify the size
    of the range (e.g. 1000 numbers)" (p125)
    "Enter a directory number. This number can start with the format B<Dir. No.> to avoid using a real
    number. Example given.: B31091" (p125)
  summary: |
    三条编号规则：①直达速拨范围长度不能为 0 且不能占满（自动替换要从该范围取号），默认起始索引 0，示例
    长度 1000；②Ghost Z 设备目录号可用 B<号码> 格式占用假号段（例 B31091），避免消耗真实号码；③远程扩展
    目录号绝不能用字母 A/B/C/D 开头，而 OTC Smartphone 设备号与速拨号可用带字母形式（D2131001 / A2131001）
    ——带字母位是"设备/速拨"命名空间，不带字母位是真实分机命名空间。
  conditions: Speed Dialing/Direct Speed Dialing Numbers 菜单
  tags: [rule, numbering, smartphone]

- id: p10
  title: RE DISA 与激活/停用前缀——31280 DISA、61/62 前缀、必须进 DDI 翻译表、DISA 免码替换
  type: checklist
  source_pages: p121-124
  source_chapter: OTC smartphone How-To / OmniPCX Enterprise settings
  source_quote: |
    "Remote extension DISA prefix: 31280 ... RE activation/deactivation prefixes (61 & 62) ... Pool of Ghost Z
    devices dedicated to remote extension function" (p121)
    "Warning CHECK THAT THIS PREFIX IS TRANSLATED IN THE DDI TRANSLATION TABLE" (p122)
    "Automatic DISA Substitution Without code" (p122)
    "Trunk group used in DISA Yes" (p123)
  summary: |
    OXE 侧远程扩展四项基座：①DISA 前缀 31280（Translator/Prefix Plan；警告：必须核对 DDI 翻译表能翻译该
    前缀）；②RE 激活/停用前缀 61/62（Station Features）；③专用 Ghost Z 池；④DISA 替换授权两级——系统级
    Automatic DISA Substitution = Without code（DISA Parameters），中继组级 Trunk group used in DISA = Yes。
    OT 侧还必须知道 DISA 公网号与 61/62 前缀（8770 同步自动取回，DISA 公网号手工填，如 +33210X41280）。
  conditions: 前缀值为实验示例；DISA 公网号=DDI 翻译结果
  tags: [checklist, disa, rex, smartphone]

- id: p11
  title: ARS 自动化口径——识别码 3、MAX ID 3999 每用户一表、Route1=SIP 设备 Route2=GSM、号码位数 11
  type: metric
  source_pages: p128, p140-141
  source_chapter: OTC smartphone How-To / Telephony settings & Verification
  source_quote: |
    "Automatic Route Selection prefix Enter the ARS prefix used to reach the mobile number. Example: #0306 ...
    Discrimination rule number Specify the Real Discriminator to use to be dedicated for OTC smartphone ...
    ARS Route list MAX ID 3999 by default. The system will use one table by user and will use the MAX ID for
    the first mobile." (p128)
    "Route 1 Automatically configured: SIP device number (e.g. D2131001) • Route 2 Automatically configured:
    external mobile number using public TG • Time based Route List 1 Automatically configured: 1 & 2" (p141)
    "Number of digits Automatically configured: 11" (p140)
  summary: |
    ARS 自动化数值口径：每用户一张 ARS 路由表，从 MAX ID（默认 3999）向下分配，第一个手机用 MAX ID；专用
    ARS 前缀（示例 #0306）+ 专用识别码（示例 Nb 3，识别码条目=识别码 ID+外线手机号，区域号 1，计划号 -1，
    位数 11）；路由表固定两条：Route 1 = SIP 设备号（D2131001，VoIP 优先）、Route 2 = 经公网中继组拨外线
    手机号，按时间表 1&2 依次。Entity 处需把逻辑识别码（3）映射到物理识别码；公网 COS 必须授权该区域号
    （barring 放行）。
  conditions: 识别码/COS 映射是自动创建之外的手工两步（p142 Warning）
  tags: [metric, ars, discriminator, smartphone]

- id: p12
  title: APNS 端口与证书口径——TCP 5223/2195/2196/443；APNS 证书一年+年度 hotfix；Geotrust 根证书至 2022
  type: metric
  source_pages: p97-98
  source_chapter: OTC for iPhone
  source_quote: |
    "Ports Description: TCP/5223 To communicate with APNs • TCP/2195 To send notification to APNs • TCP 2196
    For the APNS feedback service • TCP/443 Required during device activation, and afterwards for fallback
    (on Wi-Fi only) if devices can't reach APNs on port 5223" (p98)
    "APNS's certificate is shipped with OpenTouch server • Valid one year • A dedicated hotfix will be
    delivered every year to keep the certificate up to date • Root certificate from authority certification
    (Geotrust) is already available by default after OT installation • Valid till year 2022" (p98)
  summary: |
    iPhone 推送四端口：TCP/5223 与 APNS 通信、TCP/2195 发送通知、TCP/2196 反馈服务、TCP/443 设备激活及
    5223 不可达时（仅 Wi-Fi）的回退。证书管理：OT 随附 APNS 证书一年有效，每年需装专用 hotfix；Geotrust
    根证书默认随装（书中标注有效期至 2022 年）。防火墙按四端口放行。
  conditions: 自 OT R2.3.1 起走 APNS；年度 hotfix 是长期运维项
  tags: [metric, apns, firewall, certificate, iphone]

- id: p13
  title: iPhone 呼叫协议口径——本地 UDP 强制（多次 INVITE）；经 SBC 出网 TCP 强制（OT 做 SIP 代理缓冲）；iPhone+ 用 5265
  type: rule
  source_pages: p99-102, p130
  source_chapter: OTC for iPhone / OTC iPhone+ enhancement
  source_quote: |
    "Multi SIP invite required: UDP mandatory" (p99)
    "Calls when users are off-site: Behind the SBC, over Internet, TCP is mandatory. Impact: OpenTouch server
    will act as a SIP proxy 'buffering' the SIP invite message over TCP" (p100)
    "New SBC (used for OTC iPhone devices) • Same FQDN as OT SBC • Port 5265 ... OT SBC: Additional SIP
    interface as to be declared for iPhone users • Port 5265" (p102)
    "Protocol UDP (default value)" (p130, 设备档案 Network 页签)
  summary: |
    三条协议规则：①iPhone 应用后台时首个 INVITE 被忽略、推送唤醒后再 INVITE 才被接受——需要多次 INVITE，
    故本地/站内拓扑只用 UDP；②出网在 SBC 之后走互联网时 TCP 强制，OT 服务器充当 SIP 代理在 TCP 上缓冲
    INVITE；③"VoIP everywhere for iPhone"需专用 SBC 声明：FQDN 与通用 SBC 相同、端口 5265，OT SBC 上为
    iPhone 用户加一条 5265 SIP 接口；OTC Smartphone 设备档案的 Network 协议默认 UDP。
  conditions: kamailio-wasp + wspcfg 组件承载该代理功能（p101）
  tags: [rule, sip, udp, tcp, iphone, sbc]

- id: p14
  title: 远程接入端口与端口段总表——RP 443/8016、OTSBC 5261/8061、RTP 7000-7499、ACS SIP 5060/5260
  type: metric
  source_pages: p104-107, p296
  source_chapter: OpenTouch server settings for remote access / Dial by URI architecture
  source_quote: |
    "Ports: 443<->443 8016<->8016" (p104)
    "Ports: 5261<->5261 8061<->8061 RTP/sRTP ports: 7000-7499<->7000-7499" (p105)
    "Port 5261 (OTC clients) ... Port 8061 (WebRTC)" (p106-107)
    "SIP proxy listening on default SIP port (5060) ... Port 5060 / Port 5260 / Port 5260" (p296)
  summary: |
    端口总表（实验模板，生产按需调整）：反向代理 NAT——443（API/ACS/DMS 公共 URL）、8016（EVS 通知）；
    OTSBC NAT——5261（OTC 客户端 SIP 注册）、8061（WebRTC）、RTP/sRTP 媒体段 7000-7499；会议 Dial by URI
    SIP 代理监听 5060，ACS/SIP server/AMS 互连端口 5260；iPhone+ 专用 SBC 5265（见 p13）；会议服务器 SIP
    代理 Outbound 默认指向 OpenTouch IP:5260。
  conditions: 防火墙策略需覆盖以上端口/端口段；实验口径 10.20.X.105<->192.168.2.105
  tags: [metric, ports, firewall, remote-access]

- id: p15
  title: 会议密码与访问码规则——7 位唯一访问码双码制；音频密码≥5 位数字、在线密码≥5 字符；密码不进邀请邮件
  type: rule
  source_pages: p266, p276, p342-343, p354
  source_chapter: Conference services / Data conferencing How-To
  source_quote: |
    "The conference access is granted through a 7 digits access code which is unique. A specific code is
    generated for leaders and another one for participants" (p266)
    "Audio meeting password At least 5 digits long • To be entered after the access code • Online meeting
    password At least 5 characters long" (p276)
    "Passwords will not be included in email invitations. Conference leaders must inform people who are
    invited to the conference of the password." (p354)
    "Passwords that you assign to the audio conference will automatically be assigned to any recordings that
    you made during the conference" (p354)
  summary: |
    四条规则：①访问码固定 7 位数字、全局唯一，领导者/参与者各一码；②可选密码——音频会议密码至少 5 位数字
    （在访问码后输入）、在线会议密码至少 5 个字符，可只配音频、只配在线或两者；③密码不写进邀请邮件，领导
    者须自行告知参会人；④音频密码自动套用到该会议的录音。OTC PC 端对应 Passwords 菜单（p343）。
  conditions: 密码为可选项，访问码必有
  tags: [rule, conference, password, metric]

- id: p16
  title: 会议 DTMF 控制码——参与者 ##1/##3/##4；领导者 ##91/##92/##93
  type: metric
  source_pages: p271
  source_chapter: Leaders and participants
  source_quote: |
    "Participant options: ##1: Mute or un-mute your line • ##3: Raise your hand • ##4: Hear the number of
    callers • Leader options: ##91: Mute / Un-mute all participants • ##92: Recording conference • ##93:
    Place a call" (p271)
  summary: |
    会议 DTMF 速查：参与者——##1 静音/取消静音本线、##3 举手、##4 听当前与会人数；领导者——##91 全员静音/
    取消、##92 录制会议、##93 外呼。访客经电话入会时同样可用。
  conditions: "…" 表示书中省略了其余码；完整清单以语音提示为准
  tags: [metric, dtmf, conference]

- id: p17
  title: 协作限制矩阵——sharing/collaboration 两级禁用；对 scheduled 会议无效；S4B/Teams 与 OT networking 不适用
  type: rule
  source_pages: p291-292, p360
  source_chapter: Conference features / Data conferencing How-To
  source_quote: |
    "The administrator can limit the usage of collaboration to scheduled conference • Collaboration features
    can be disabled at two levels: 'sharing capability only' or 'full collaboration' features • The disabling
    operation is done by administrator at a user level • Concerns only Connection users" (p291)
    "Note: this parameter has no impact for scheduled conference, because for this kind of conference, full
    collaboration capabilities are always available." (p360)
  summary: |
    权限治理规则：管理员可在用户级禁用两级——Enable sharing off（禁文档/桌面共享，保留 IM/在场/状态）或
    Enable collaboration off（连 IM、日历在场、状态消息、联系人/电话在场、共享全禁）；仅作用于 ad-hoc 会议
    与点对点会话，scheduled/reservationless 会议始终全量协作。该特性只面向 Connection 用户；Skype for
    Business/Teams 集成（在场与协作不归 OT）与 OT networking 场景下不可用。禁用后功能矩阵见 p292 表。
  conditions: 入口 Users and devices/User 的两个开关
  tags: [rule, collaboration, permissions]

- id: p18
  title: 日历状态优先级与展示规则——OOO>Busy>Tentative>Working Elsewhere>Free；FREE 只在二级界面；自己看不到自己
  type: rule
  source_pages: p389, p402-405 (TC2258)
  source_chapter: Calendar presence
  source_quote: |
    "the following precedence on the five calendar states: Out of Office > Busy > Tentative > Working
    Elsewhere > Free" (p389)
    "As an OTC PC or OTC One user we don't see our own calendar presence in our application." (TC2258 p4)
    "The FREE calendar status information (+endate) is only displayed at 2nd level of application. That means
    ... it will not be displayed in the favorite list nor in the communication log but it will be displayed
    in the contact card." (TC2258 p6)
    "The color code is not modified by the presence information." (TC2258 p3)
  summary: |
    日历在场四条规则：①多日程重叠按 OOO>Busy>Tentative>Working Elsewhere>Free 取结果状态；②用户看不到
    自己的日历在场；③FREE 状态信息（含结束时间）只在二级界面（联系人名片）显示，收藏列表与通话记录不显示；
    ④日历在场只是旁注文本，不改变在场颜色码。按用户开关的入口是 Outlook 端 Free/Busy Read 权限
    （Read=None 即全局停用，默认启用）。
  conditions: 功能自 OT R2.3.1 起（依赖 Exchange impersonation）；仅收藏联系人显示
  tags: [rule, calendar, presence]

- id: p19
  title: 日历 endTime 展示公式——ISO 8601 UTC 存储、按终端 locale 展示；今天→"until HH:mm"，明天及以后→"for the next hours"
  type: formula
  source_pages: p404-405 (TC2258)
  source_chapter: Calendar Presence / How is displayed the endtime information
  source_quote: |
    "endTime information is an UTC datetime whose format (ISO 8601 compatible) is
    yyyy-MM-ddTHH:mm:ss.SSSZ (example: 2013-05-16T18:17:15.489Z)." (TC2258 p5)
    "If the endTime date part (yyyy-MM-dd) is the same than the current date (today), only the time
    information will be displayed ... On a French PC: OTC clients will display 'busy until 11:00'. On an US
    PC: OTC clients will display 'busy until 11:00 AM'." (TC2258 p6)
    "In that case, the text will be 'free for the next hours' or 'busy for the next hours'." (TC2258 p6)
  summary: |
    展示公式：endTime 以 UTC ISO 8601 存储；展示用最终用户 locale。结束日在今天→只显示"busy/free until
    HH:mm"（法语区无 AM/PM，美区带 AM/PM）；结束日在明天或更远→显示"free/busy for the next hours"。
    售前演示与验收脚本要按此口径写预期文案。
  conditions: 时区显示差异常被误报为"时间不对"
  tags: [formula, calendar, i18n]

- id: p20
  title: 目录同步周期规则——date/time/period 必填；period≥1 永不为 0；merge period≠0
  type: rule
  source_pages: p243-245, p253
  source_chapter: Directory search How-To
  source_quote: |
    "Tips Synchronization Date, Time and period MUST BE SET. Synchronization period >= 1 (NEVER SET period to
    0) 1 => synchronization every day at declared time 2 => every 2 days etc …" (p244, p245 两处重复)
    "Merge Period Configure the merge period (must be different from 0)" (p253)
  summary: |
    同步三参数硬规则：目录同步的日期（yyyy-mm-dd）、时间（hh:mm:ss）、周期（天）都必须设置；周期 ≥1，永不允许
    0（1=每天、2=每两天）；SBC 合并的 Merge Period 同样必须非 0。同步在 OT 服务器上生成搜索用数据库
    （目录数据快照），另有"by merge"勾选可让合并前自动同步、此后跟随合并节奏。
  conditions: 手动同步用 Force synchronization 勾选
  tags: [rule, udas, synchronization]

- id: p21
  title: 联系人卡结构与可选属性上限——4 默认属性 + 最多 5 个参与搜索的可选属性；photo 不可 searchable；部分客户端不支持可选属性搜索
  type: rule
  source_pages: p224-225, p250
  source_chapter: Contact card structure / Make optional attributes available
  source_quote: |
    "A contact card = 4 default attributes + [1 .. 5] dynamic attributes ... Last name: sn • First name:
    givenName • Email: mail • Phone number: telephoneNumber" (p224)
    "By default, more than 20 contact attributes (business web page, company name…) are already created ... a
    maximum of five of them can be involved during the directory search operation." (p250)
    "The 'searchable' option is not available for all attributes, example for the photo. The search on
    optional attributes doesn't work from all clients even if it is configured." (p250)
  summary: |
    联系人卡规则：默认 4 属性（sn/givenName/mail/telephoneNumber）恒可搜；可选属性库里预置 20+（可自定义
    新属性），但同一时刻最多 5 个可参与目录搜索（Attribute 1..5 兼容位）；"可搜索"开关并非所有属性都有
    （如照片只能 Displayable 不能 Searchable）；即使配置了，可选属性搜索也不是所有客户端都支持。通配符：
    % 前缀匹配、- 排除，最多 5 个搜索串。
  conditions: 属性映射需与 LDAP 字段对应（Field names/Attributes 页签）
  tags: [rule, udas, attributes]

- id: p22
  title: Merge keys 规则——至少姓+名两个键；高权重目录覆盖低权重；预处理（去前缀/后缀/取前 n 字符）
  type: rule
  source_pages: p226, p252-254
  source_chapter: Synchronization with merged directory / SBC configuration
  source_quote: |
    "The directory with the highest weight value, will always have its data replacing the other information in
    the merged directory. ... a mapping must be defined. The mapping is defined for each declared directory
    ('Merge Keys')" (p226)
    "'Merge keys' are composed by several contact attributes (two minimum: firstname & lastname)" (p252)
    "If a contact match is found in the merged table, the merged contact is updated with the values in all
    non empty properties from the processing contact card except givenname and sn." (p253)
    "Merge keys preprocessing takes into account the 12 first characters of the 3 'Merge keys' ... a '_DECT'
    suffix is removed" (p254)
  summary: |
    SBC 合并规则：①识别同一人靠 Merge keys（最少两个：firstname+lastname，可加电话等）；②目录按
    Synchronization Order 定权重，高权重覆盖低权重（已合并条目中 givenname/sn 之外的非空属性按处理目录
    更新）；③每个键可配预处理——去前缀、去后缀、取前 n 个有效字符（实验例：3 个键各取前 12 字符，first
    name 去除 "_DECT" 后缀）；④匹配不到才作为新条目加入合并表。每个参与合并的目录都要做同样的 merge keys
    管理。
  conditions: 仅在启用 Merge 激活后生效；照片同化也依赖合并开启
  tags: [rule, sbc, merge, udas]

- id: p23
  title: 照片同化优先级——Avatar(internaldir) > LDAP 照片 > 本地照片；依赖目录合并开启
  type: rule
  source_pages: p230, p257
  source_chapter: Photo homogenization / UDAS maintenance
  source_quote: |
    "First: Avatar (the photo that the user has set as avatar with OTC clients). Note that this photo is
    stored in the SIP server directory (internaldir) ... Second: LDAP photo • Third: Local photo ... The
    avatar overrides the LDAP photo but if the user removes his or her avatar, the LDAP photo is displayed
    again. Note that the mechanisms described here only make sense if the directory merging is enabled." (p230)
  summary: |
    三级照片优先级：用户 Avatar（存 internaldir，可经 ACS WebAdmin 上传）最优先；其次 LDAP 目录照片；最后
    本地自定义照片。用户删除 Avatar 后 LDAP 照片自动回显。排障：照片在 /var/data/slides/d.DEFAULT/ 检查，
    缺失则手动同步 LDAP 目录。
  conditions: 合并未启用时该优先级机制无意义
  tags: [rule, udas, photo]

- id: p24
  title: LDAP 溢出容量口径冲突——讲义"20 LDAP servers maximum" vs 实验"OXE 最多 5 个电话簿"；LDAP v3.0+；无 referral
  type: metric
  source_pages: p235, p260
  source_chapter: LDAP overflow for OXE users
  source_quote: |
    "Restrictions: LDAP version 3.0 or higher • 20 LDAP servers maximum • No referral" (p235)
    "Up to five LDAP servers can be declared in the OXE ... LDAP phone book Enter the phone book index (from 1
    to 5)" (p260)
  summary: |
    两处口径不一致（实验文档未对齐）：讲义页称 LDAP 溢出最多 20 台 LDAP 服务器（另有 LDAP v3.0+、不支持
    referral 两条硬限制）；How-To 页明确 OXE 的 LDAP Phone Books 索引只有 1-5，即最多 5 个。现场按实验页
    的 5 个做配置上限、以最新版技术通报核实 20 的适用语境（推断：20 可能指 OT/UDAS 侧目录数，OXE 侧
    Phone Book 仅 5）。
  conditions: 溢出需三级配置——LDAP Phone Book 声明、Entity 挂索引、系统参数开启
  tags: [metric, ldap, capacity, version-trap]

- id: p25
  title: LDAP 认证插件参数必填/选填清单（plugin_ldap.properties）
  type: checklist
  source_pages: p440-441
  source_chapter: External authentication: LDAP authentication How-To
  source_quote: |
    "server.protocol=ldap (Can be 'ldap' or 'ldaps' ... Default value: ldap) [OPTIONAL]
    server.primary.name=192.168.1.100 [MANDATORY]
    server.primary.port=389 [OPTIONAL, default 389]
    server.secondary.name=192.168.1.100 [MANDATORY] (used if the primary doesn't respond)
    server.secondary.port=389 [OPTIONAL]
    server.basedn=cn=users,dc=company,dc=com [MANDATORY]
    appli.login=cn=directory,cn=users,dc=company,dc=com [OPTIONAL]
    appli.pwd=directory [OPTIONAL]
    user.login.attribute=sAMAccountName [MANDATORY]
    user.uid.attribute=sAMAccountName [MANDATORY]" (p440-441)
  summary: |
    plugin_ldap.properties 十参数：必填 4——主/备 LDAP 服务器地址（server.primary.name /
    server.secondary.name）、搜索基 DN（server.basedn）、登录属性（user.login.attribute）、唯一 ID 属性
    （user.uid.attribute，AD 用 sAMAccountName）；选填 6——协议 ldap/ldaps（默认 ldap）、主/备端口（默认
    389）、应用账号 appli.login/appli.pwd。文件必须与 ecc.properties 同目录（/opt/Alcatel-Lucent）；启用
    靠删 Authentication.xml 中对应插件的注释符，改后重启 tomcatd；回退默认认证=还原原始文件再重启。
  conditions: 备服务器仅主无响应时使用；修改前先备份原文件
  tags: [checklist, ldap, authentication]

- id: p26
  title: RADIUS 插件参数清单——1812/1813 端口、shared_secret、pap、超时 10（默认 15）、重试 5（默认 2）
  type: metric
  source_pages: p459-460
  source_chapter: External authentication: RADIUS authentication How-To
  source_quote: |
    "server.primary.name=192.168.1.10 [MANDATORY]
    server.primary.port.authentication=1812 [OPTIONAL, default 1812]
    server.primary.port.accounting=1813 [OPTIONAL, default 1813] (feature not used by OmniTouch)
    server.secondary.name=192.168.1.10 [MANDATORY]
    server.shared_secret=training [MANDATORY]
    server.connection.timeout=10 [OPTIONAL, Default value: 15]
    server.connection.retries=5 [OPTIONAL, Default value: 2]
    server.authenticator=pap [OPTIONAL, Default value: pap]" (p459-460)
  summary: |
    plugin_radius.properties 口径：必填 2——主/备 RADIUS 服务器地址；端口认证 1812/计费 1813（计费 OT 未
    用）；共享密钥 server.shared_secret 必填（实验值 training）；认证方式默认 pap（可选 chap 等）；超时实验
    设 10 秒（默认 15）、单服务器重试实验设 5 次（默认 2）；备服务器在主无响应时启用。OT 侧 External
    login 必须与 RADIUS 用户库的 Radius login 一致。注意：该页 Notes 误写为"连接 LDAP 目录所需参数"（原文
    复制粘贴笔误）。
  conditions: 实验用 FreeRADIUS.net 1.0.5（Windows 版，客户端 PC 192.168.1.10）
  tags: [metric, radius, authentication]

- id: p27
  title: Kerberos 配置四件套路径与 keytab 生成命令
  type: checklist
  source_pages: p445-448
  source_chapter: Single Sign On Authentication through Kerberos How-To
  source_quote: |
    "Rename the file 'web.xml' ... into 'web.xml.default'. Rename the file 'web.xml.kerberos' ... into
    'web.xml' (thin: /opt/Alcatel-Lucent/infra_webapps/authenticationform/authenticationform/WEB-INF; thick:
    .../authenticationbasic/...)" (p445)
    "Copy/paste the 'krb5.conf' file from .../kerberos_conf to /opt/Alcatel-Lucent/platform/tomcat/conf" (p446)
    "Copy/paste the 'auth.config' file ... to /var/data/ics-group/tomcat (will be overwritten)" (p447)
    "'ktutil' ... 'addent –password –p ice_kerb@company.com –k 0 –e rc4-hmac' ... 'wkt
    /opt/Alcatel-Lucent/platform/tomcat/conf/ice_kerb.keytab'" (p448)
  summary: |
    四件套：①web.xml 模板重命名启用/停用（thin=authenticationform、thick=authenticationbasic 两个 WEB-INF
    目录）；②krb5.conf 拷到 /opt/Alcatel-Lucent/platform/tomcat/conf 并改域名/realm/KDC；③auth.config 拷到
    /var/data/ics-group/tomcat（覆盖原文件），含 KeyTab 路径与 principal；④keytab 用 ktutil 生成——
    addent -password -p <principal> -k 0 -e rc4-hmac（输入 AD 账号密码）→ wkt 输出到
    /opt/Alcatel-Lucent/platform/tomcat/conf/ice_kerb.keytab。改完 service tomcatd restart。
  conditions: AD 账号 ice_kerb 密码必须与 keytab 一致；SPN 用 setspn 注册（见 p28）
  tags: [checklist, kerberos, keytab, paths]

- id: p28
  title: SPN 注册与 WBM 管理员保护规则——setspn 两条命令；External login 全局唯一；Delegate authentication 选项
  type: rule
  source_pages: p451-454
  source_chapter: Kerberos How-To
  source_quote: |
    "'setspn –A HTTP/opentouch ice_kerb' then press 'Enter' • 'setspn –A HTTP/opentouch.company.com ice_kerb'" (p451)
    "The value for 'External login' is unique in the OpenTouch configuration. The value for 'External login'
    must match the Active Directory login. The selected Active Directory user name for External login (for
    instance wbm_admin) cannot be used for an OpenTouch standard user and an OpenTouch admin user at the same
    time" (p454)
    "'General' tab / Application WBM must be selected • 'General' tab / Delegate authentication Option must be
    validated ... A password (mandatory) has to be entered ... Note: This password is never used with Kerberos" (p454)
  summary: |
    规则四条：①AD 专用账号需注册两条 SPN：HTTP/短名与 HTTP/FQDN（setspn -A，Windows Server 2003+ 自带）；
    ②External login 在 OT 配置中全局唯一——同一 AD 名不能同时给标准用户和管理员用；③Kerberos 启用后要在
    System Services/Security/Administrator 预建 WBM 管理员：External login=AD 管理员名、Application 选
    WBM、勾 Delegate authentication、GUI 密码必填（Kerberos 下不使用）；④登录验证：加域机器上直接开
    https://<OT>/WebAdmin 免密进入。
  conditions: 启用 Kerberos 后 8770 客户端无法再访问 WBM（p430），此管理员是唯一入口
  tags: [rule, kerberos, spn, wbm, admin]

- id: p29
  title: 外部认证作用域与级联规则——全局生效；IP Touch/TUI 除外；Web 级联 DTA、厚客户端不级联
  type: rule
  source_pages: p426-427, p431
  source_chapter: External authentication
  source_quote: |
    "The authentication mechanism applies to all devices/Applications • You cannot activate a specific
    authentication for one Application/device only • Note that IP Touch applications and TUI do not use this
    mechanism as authentication is based on the user's phone number" (p426)
    "If external authentication fails, there is an automatic cascading to DTA for Web clients (WBM for
    Administrator…) • No automatic cascading for thick clients (OTC PC…)" (p426)
    "When Kerberos authentication is activated for an application, it must be used for every single user of
    this application" (p430)
  summary: |
    三条作用域规则：①外部认证是全局开关，不能按应用单独启用；例外——IP Touch 应用与 TUI 不走此机制（按话机
    号码认证）；②外认失败时 Web 客户端（含 WBM）自动级联回 DTA 本地认证，厚客户端（OTC PC）不级联——账号没
    配好时厚客户端直接登录失败；③Kerberos 一旦对某应用启用，该应用所有用户都必须走 Kerberos。
  conditions: 管理员账号必须在外部认证服务器预建账密并填 External login
  tags: [rule, authentication, cascade]

- id: p30
  title: UM Exchange 特权账号三参数——每个 UM 用户邮箱必须配 Send as / Full Access / Send on behalf
  type: rule
  source_pages: p190-193
  source_chapter: Unified Messaging How-To / Assign permissions
  source_quote: |
    "FOR EACH PERSON USING A 'UNIFIED MESSAGING' MAILBOX (ALBAN, BACKMAN…), IT'S MANDATORY TO MANAGE THE TREE
    PARAMETERS, CALLED 'MANAGE SEND AS PERMISSION', 'MANAGE FULL ACCESS PERMISSION' AND 'SEND ON BEHALF'" (p191)
    "Before OpenTouch release 2.2, the second method (delegation) was used but some troubles were possible in
    case of a lot of traffic ... Since the release 2.3 ... the OpenTouch server uses now impersonation method
    instead of delegation" (p189)
    "New-ManagementRoleAssignment –Name 'Service Account Impersonation' –Role ApplicationImpersonation –User
    'ICEaccess@company.com'" (p190)
  summary: |
    Exchange 侧权限两代方案：R2.2.x 及以前用 delegation（对每个 UM 邮箱逐个配 Send as + Full Access +
    Send on behalf 三参数，用户多时易出问题）；R2.3 起 OT 改用 impersonation——EMS 一条命令给 ICEaccess 账号
    ApplicationImpersonation 角色，验证用 Get-ManagementRoleAssignment。无论哪代：ICEaccess 需 AD 账号 +
    Exchange 邮箱 + 密码永不过期。详细实现见 TC2391。
  conditions: 版本分界 >2.2.x 用 impersonation / <2.2.x 用 delegation（两侧配置不同）
  tags: [rule, um, exchange, impersonation]

- id: p31
  title: UM 邮件服务器声明口径——EWS+443、登录两种格式、云位置 outlook.office365.com、通知服务 URL 规则
  type: checklist
  source_pages: p196, p216-217
  source_chapter: UM How-To / Exchange server declaration
  source_quote: |
    "Protocol Select 'Exchange Web services' • Port Enter the https port number (443 by default) ...
    This field must contain the information of domain name; for that, 2 possibilities: - DOMAIN\\login OR -
    login@DOMAIN" (p196)
    "If location=cloud, the FQDN is set to 'outlook.office365.com' ... Location Select 'cloud' when Exchange
    server is in the cloud (MicroSoft Office 365)" (p217)
    "Public URL of the Exchange notification service ... a simple firewall rule can be configured to authorize
    the Exchange server to connect to the OpenTouch server (so, the need of a Reverse Proxy has been removed).
    This rule is using URL information ('/ExchangeNotificationService')" (p217)
  summary: |
    声明清单：本地 Exchange——FQDN、协议 EWS、端口 443、EWS 登录（DOMAIN\\login 或 login@DOMAIN 两种格式）、
    位置 on-premises；云 Exchange（O365）——FQDN 默认 outlook.office365.com、位置 cloud、额外两项：HTTP
    proxy（OT→Exchange 出网代理，可带 Basic/Digest 认证）与 Exchange 通知服务公共 URL（防火墙按
    /ExchangeNotificationService URL 放行 Exchange 回连 OT，可省反向代理）。两处共同勾选：Activate calendar
    presence service 与 Activate conference synchronization service。
  conditions: 云场景证书仍须入 OT 信任库；8770/CMS 提供公共 URL 给 Exchange
  tags: [checklist, um, o365, ews]

- id: p32
  title: 语音邮箱档案关键参数——Answer only、Direct callback、Attendant call '0'、 sent items 副本（仅 UM）
  type: checklist
  source_pages: p199-201
  source_chapter: UM How-To / Voice mail profiles
  source_quote: |
    "Answer only Yes: the mailbox is in 'answer only' mode; so it is not possible to leave messages in it ...
    Manageable by users: the end-user can modify by himself the 'answer-only' mode parameter" (p200)
    "Direct callback Automatic callback to the users who left a message ... press '2' to call back" (p200)
    "Attendant call enabled True (default value): ... the caller can select the choice '0' of the voice mail
    TUI to be routed to the attendant." (p200)
    "Keep a copy of voice message in sent items Applies to Unified Messaging only." (p201)
  summary: |
    档案配置要点（4 个默认档案：1 个 UM standard + 3 个 Local Storage〔simplified/classic/advanced〕，可自
    建）：Answer only（只应答不收留言，可授权用户自管）、Check quota、Direct callback（按 2 回呼发话人，
    可配确认与语音引导）、Limited access（防滥用录 greeting/语音名）、Extended absence greeting 是否阻断留
    言、Propose options after message deposit（# 键附加选项）、Attendant call enabled（默认 True，拨 0 转
    话务台）、Keep copy in sent items（仅 UM 生效：发留言者 sent items 留副本，默认 False）、configuration2
    的三时长（greeting/留言/live record 上限秒数）。改动档案后必须同步（OT+OXE）才生效。
  conditions: Callback sender allowed 仅适用 Local Storage/Exchange/Gmail（IMAP 不可）
  tags: [checklist, um, voicemail-profile]

- id: p33
  title: Gmail/IMAP 后端边界——Gmail 上限 500 用户走 OAuth 2.0；IMAP4 无 PPR/扩展/MWI/消息类别
  type: limitation
  source_pages: p176-177, p181
  source_chapter: UM Architecture / Configuration Google Mail
  source_quote: |
    "Gmail platform can be used to store voice mails ... Limited to 500 OpenTouch users" (p176)
    "IMAP4 mail server • No plug-in: less services • No PPR • No Extensions • No MWI • No class of message" (p177)
    "Support of OAuth 2.0 protocol for authentication and authorization ... Create once: Unique Client ID •
    Private Key • Google service account mail@" (p181)
  summary: |
    两条后端边界：Gmail 走 OAuth 2.0（Google Developer Console 一次性建 Client ID/私钥/服务账号；OT 侧每系
    统配 Gmail SMTP/IMAP 服务器与服务账号，每用户关联邮箱与令牌），上限 500 个 OT 用户；IMAP4 无插件因此
    砍掉 PPR、扩展、MWI、消息类别四项能力。选型时电话侧体验按后端递减排：Exchange ≥ O365 > Gmail > IMAP。
  conditions: 每用户令牌由 OT 请求并用于存取
  tags: [limitation, um, gmail, imap]

- id: p34
  title: 会议文档上传规则——免安装支持 pdf/bmp/gif/jpg/jpeg/png；Office 需 DCS；presentation 不可下载 attachment 可
  type: rule
  source_pages: p278, p344, p365
  source_chapter: Conference documents
  source_quote: |
    "Presentations: Not downloadable for participants • Attachments: Downloadable for participants • Both ...
    Uploaded documents • Images, Pdf, PowerPoint, Word, Excel" (p278)
    "You can upload pdf, bmp, gif, jpg, jpeg, and png as a presentation, without any specific installation
    requirements. To upload a Microsoft Office file (doc, docx, ppt, pptx, xls,xlsx) as a presentation, a DCS
    (Document Conversion Server) is mandatory." (p344)
    "Participants cannot download presentation files, only attachment ones." (p344)
  summary: |
    文档三规则：①免 DCS 可作演示的格式——pdf、bmp、gif、jpg、jpeg、png；Office 文档（doc/docx/ppt/pptx/
    xls/xlsx）作演示必须装 DCS，否则只能作附件；②可见性——presentation 参与者不可下载，attachment 可下载，
    同一文件可双身份上传；③DCS 模式下文档从用户电脑上传到 DCS 服务器打开转换。
  conditions: DCS 安装形态见 f17/c18
  tags: [rule, conference, documents, dcs]

- id: p35
  title: DCS 兼容矩阵与外部 VM 约束——Hyperthreaded Core Sharing=None；内部 Win7 32bit；Windows/Office 许可自备
  type: metric
  source_pages: p367-368, p370-371, p373
  source_chapter: Document Conversion Server
  source_quote: |
    "Neither material nor licenses are provided by Alcatel-Lucent • Microsoft Windows DVD & product key •
    Microsoft Office DVD & product key" (p367)
    "Internal DCS Supported OS: Windows 7 Professional 32 bits / Windows 7 Enterprise 32 bits ... Supported
    Office: Office 2010, US English, 32-bit, Professional • Office 2019, US English, Professional" (p371)
    "Hyper-threading must be deactivated on the VM: set the option 'Hyperthreaded Core Sharing' to 'None'" (p373)
  summary: |
    DCS 数值口径：内部 DCS（OT 内 KVM 虚机）——Windows 7 Pro/Enterprise 32 位 + Office 2010 或 2019（US
    English Professional）；外部 DCS——另支持 Win 8.1、Server 2008 R2 32 位、Server 2012 R2 32/64 位、
    Windows 10（原文印作 "Windows 2010"，笔误）32/64 位 + Office 2010/2013/2016（32 位口径为主）；外部
    ESXi 虚机必须关超线程（Hyperthreaded Core Sharing=None）；构建耗时约 20 分钟（Windows）+ 15-30 分钟
    （Office）；多数西欧语言 Office 可用，俄语等需手动装。Windows 与 Office 的介质和许可 ALE 一概不提供。
  conditions: 最新兼容性以 OT release note 为准（书中明示）
  tags: [metric, dcs, compatibility]

- id: p36
  title: DCS-V Windows 预配置四件——关防火墙、UAC 从不通知、密码永不过期、注册表自动登录 4 键
  type: checklist
  source_pages: p375-379
  source_chapter: DCS installation on a virtual machine – DCS-V How-To
  source_quote: |
    "Turn off the firewall for private and public network" (p376)
    "User account control settings Select 'never Notify'" (p377)
    "Password never expires Checked" (p378)
    "AutoAdminLogon set to 1 • DefaultDomainName set to your domain ... • DefaultUserName set to your admin
    login name • Create the new String Value key ... DefaultPassword" (p379)
    "Warning REBOOT WINDOWS VIRTUAL MACHINE" (p379)
  summary: |
    Windows 侧预配置四步：①关闭专用/公用网络防火墙；②UAC 设为"从不通知"（搜索面板输 uac 快速定位）；③所用
    管理员账号勾"密码永不过期"（Computer management/Local Users and Groups）；④注册表
    HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon——AutoAdminLogon=1、DefaultDomainName、
    DefaultUserName、新建 DefaultPassword 四个字符串值，改完必须重启虚机。DCS 组件安装：挂 ISO 拷
    dcs_install.bat / dcs_vmware-6.zip / unzip.exe 到 C:\\temp 执行 bat。
  conditions: Windows/Office 必须先激活并打齐强制更新，否则文档卡 queued（见 n 系列）
  tags: [checklist, dcs, windows]

- id: p37
  title: 证书操作口径——SHA256 最佳；pkcs#7 直导/pkcs#12 需 passphrase；Deploy 后会话断开属正常
  type: rule
  source_pages: p112-117
  source_chapter: OT server settings for remote access / Certificate
  source_quote: |
    "Signature algorithm Select the algorithm (SHA256 is the best for security)" (p112)
    "Select the good type (in this example pkcs#7) ... In case of pkcs#12 file selection when CSR is generated
    directly on CA server, a passphrase is required." (p116-117)
    "Just after clicking on 'Deploy', a message is displayed (« Impossible to retrieve data from / … ») and the
    WebAdmin session is cut. You have to restart the web session. It is normal because the server's
    certificate used for the 'https' connection has just changed." (p117)
  summary: |
    三条操作规则：①CSR 信息含国家（2 字母）/省/市/公司/部门/管理员邮箱，签名算法选 SHA256；②导入类型
    pkcs#7 直接导入，pkcs#12 需要签发方提供 passphrase；③点 Deploy 后提示"Impossible to retrieve data"且
    WebAdmin 会话被切断属正常现象（https 证书已换），重开会话即可；部署完成后用 My Profile 的证书详情核验
    SAN。
  conditions: CA 可为内部 OpenSSL/Windows CA 或外部 Certisign/VeriSign 等
  tags: [rule, certificate, pki]

- id: p38
  title: 会议服务器系统选项与 SIP 代理口径——00/0/33、Smart mail relay、默认 Web 客户端 OTCWeb、Outbound 5260
  type: metric
  source_pages: p314-316, p320
  source_chapter: Conference server Settings Configuration
  source_quote: |
    "International Dialing Prefix: 00 • National Dialing Prefix: 0 • Country Code: 33 • Smart mail relay host:
    eco.company.com • Default web client: OTCWeb" (p314)
    "Default Outbound SIP Proxy: 192.168.1.50 • Default Outbound SIP Proxy port: 5260 • Realm:
    opentouch.company.com • Server IP address: 192.168.1.50 • Port: 5260 • SIP User Name: 31250 & 31260" (p316)
    "Extension Pattern /^\\s*\\+*[xX]?(\\d{3,5})\\s*$/ for a 5 digits length dialing plan" (p320)
  summary: |
    会议服务器数值口径（法国实验）：系统选项——国际前缀 00、国内前缀 0、国家码 33、Smart mail relay host=
    邮件服务器 FQDN（发会议邀请邮件用）、默认 Web 客户端 OTCWeb；SIP 代理——Outbound 默认指向 OpenTouch IP
    端口 5260，Inbound Realm=OT FQDN、Server=OT IP、Port 5260，Users 为 TUI 会议号 31250/31260（自动填入），
    UDP 代理用于与 SIP 网关/PBX/外部代理互连，装后向导自动填好只需核对；电话格式规则（Extension Pattern）
    /^\\s*\\+*[xX]?(\\d{3,5})\\s*$/ 适配 5 位分机计划（第二处数字改分机位数）。
  conditions: WebAdmin 登录 otAdmin/admin8770（实验口径）
  tags: [metric, conference, sip-proxy, dialplan]

- id: p39
  title: 会议桥双语号规则——TUI 号 31250(EN)/31260(FR)，OXE External Voice Mail 与 OT TUI application 双侧成对
  type: rule
  source_pages: p309-312
  source_chapter: Conference server Settings Configuration
  source_quote: |
    "Manage the 'TUI Conferencing numbers' in the OXE, used to access to conferences: 31250 for English voice
    guides ... 31260 for French voice guides ... It is of course possible to declare more numbers, associated
    to more languages" (p309)
    "Look for 'Conferencing' item to modify the default one. ... Type Conferencing • Collaboration
    organization ... Language ... Include in e-mail invitations ... Label for e-mail invitation ... Dial in
    number Fill in an other number usable to access to the same conference bridge (i.e. external DDI number)" (p311)
  summary: |
    桥号成对规则：每个语言一个会议号——OXE 侧 Applications/External Voice Mail 建（Voice Mail Dir Number+
    Directory Name Conf-EN/Conf-FR+External Gateway number），OT 侧 TUI application 建对应 Conferencing
    条目（Number 两端一致、Type=Conferencing、Collaboration organization、Language、Include in e-mail
    invitations、Label、可选 Dial in number=外部 DDI 公号码）；One Touch 入会要求 Label 以 <*> 开头（p358，
    Dial in number 用规范格式如 +33210141250，Toll-free 勾选标记免费）。系统选项/语言在 OT 侧绑定。
  conditions: 号码值可自定义，两端一致即可
  tags: [rule, conference, tui]

- id: p40
  title: One Touch 入会与回呼规则——Label 以 <*> 开头、免长途回呼链接、按键确认防误入
  type: rule
  source_pages: p283, p355, p358
  source_chapter: Conference access / Data conferencing How-To
  source_quote: |
    "Simple configuration: 'Label for e-mail invitation' starting with <*>" (p283)
    "Toll-free links are included by default in email and Calendar invitations. Clicking on the link opens a
    web page where a person can join a conference call without paying for long distance." (p355)
    "Confirm callbacks with a keypress ... 'Welcome to the My Teamwork conference center. To join press 1. To
    decline, press 2.'" (p355)
  summary: |
    三条入会规则：①邮件邀请含"一键入会"信息的条件是 TUI 会议号的邀请标签以 <*> 开头（并配规范格式 Dial in
    number，如 +33210141250，可勾 Toll-free 标记免费）；②"Allow others to join with callback"默认在邀请中
    给免长途链接——与会者在网页填自己的号码由系统回呼；③"Confirm callbacks with a keypress"要求回呼接通后
    按 1 确认/按 2 拒绝，防止把语音邮箱等误接进会议。
  conditions: 关闭 toll-free 链接后邀请仍有链接但无填号框
  tags: [rule, conference, callback]

- id: p41
  title: Extended Mobility 前提/成本清单与 QR 语法
  type: checklist
  source_pages: p148, p157-161, p164
  source_chapter: Extended Mobility
  source_quote: |
    "«Extended OT mobility» allows users with Android or iPhone (*) Smartphones: To switch an established
    communication from OTC application to any internal deskphone (one way) • To modify the end-user's call
    routing profile with any internal deskphone ... (*) NFC not supported by iPhone" (p150)
    "Pre-requisites: Android smartphones with NFC capacity & QR code • iPhone Smartphones with QR code
    capacity (since OT R2.2) • OpenTouch R2.1 MD1 minimum • Wifi or Cellular network" (p161)
    "QR Code label ... accepted by the smartphone app for audio switch on an OXE deskphone:
    {\"v\":\"1\",\"DI\":{\"DiD\":{\"User\":\"phone number\"}}} with phone number = OXE user directory Number
    • Example: {\"v\":\"1\",\"DI\":{\"DiD\":{\"User\":\"31000\"}}}" (p158)
    "ALE strongly recommends to take ALE NFC tags (Ref 3BA27856AA: NFC tag stickers x100) ... labels bought
    'directly' ... have a chance to be compatible if they respect the reference 'NFC Type 2' • Their
    validation must be realized in this case by the Business Partner" (p160)
  summary: |
    部署清单：版本前提 OpenTouch R2.1 MD1 起（iPhone QR 自 R2.2）；Android 支持 NFC+QR，iPhone 仅 QR（无
    NFC）；触发由 OTC 应用完成（应用必须已启动）。QR 语法固定 JSON
    {\"v\":\"1\",\"DI\":{\"DiD\":{\"User\":\"<OXE 目录号>\"}}}，用任意第三方 QR 生成器制作；NFC 写标签用
    Google 市场的 "ALE NFC Extended Mobility Administration" 工具（Android R4.2+），建议采购 ALE 标签
    （Ref 3BA27856AA，100 张装），自购标签须为 NFC Type 2 且由 BP 验证。成本项：话机（硬件+许可）、手机、
    Connection 用户许可+universal connection client 许可+REX 资源（GhostZ/IP/DTMF）、NFC 标签；无软件增项、
    无使用费。
  conditions: 支持话机范围：ALE-x 系、80x8/80x9、8001、WLAN 81x8、DECT、模拟话机、4135 会议话机（p157）
  tags: [checklist, extended-mobility, qr, nfc]

- id: p42
  title: Extended Mobility 行为规则——切换=<二通呼叫+转移>不可回切；路由修改=选含 other and mobile() 的档案；一小时周期提醒
  type: rule
  source_pages: p152-155, p162
  source_chapter: Extended Mobility
  source_quote: |
    "OTC application will execute an automated scenario: <make a 2nd call towards the deskphone> + <transfer
    the call> • Since the automated scenario has been executed, there is no retrieve facility to switch back
    the call to smartphone • If deskphone is configured with immediate forward, the call switching will route
    to this destination" (p152)
    "OTC Smartphone selects a new profile with the entry « other and mobile() »" (p153)
    "Periodic reminder is displayed each hour to remind the user to return back to the previous call routing
    profile ... Yes: the previous call routing profile is enabled again ... Later: ... the periodic timer is
    re-launched (a new pop-up will be displayed in one hour)" (p154)
  summary: |
    行为三则：①呼叫切换的底层是"向目标话机发起二通呼叫+转移"的自动场景，不可回切到手机；目标话机若配了
    立即呼转，呼叫会跟呼转走（用户需拿起话机以保私密）；②路由修改是把档案切到含 "other and mobile()"（值=
    目标话机号）的条目；③每小时弹周期提醒——Yes 恢复原档案、No 保留新档案并停表、Later 一小时后再弹；停止
    提醒还可再扫一次同一 QR/NFC（toggle）或杀 OTC 应用。路由修改仅限空闲态（无进行中呼叫）执行。
  conditions: 切换时用户必须拿起话机（隐私原因，p162）
  tags: [rule, extended-mobility, routing]

- id: p43
  title: RegExp 速查与 DAS 法国 10 规则全集
  type: metric
  source_pages: p303-305, p108, p317-318
  source_chapter: DAS rules
  source_quote: |
    "? 0 or 1 • * 0, 1 or more • + 1 or more • {3} 3 • {2,} 2 or more • {2,4} 2, 3, or 4 • ^ start with • $
    end with • . any character • \\d digit • \\s space" (p303)
    "s/^\\+(\\d{3,6})$/+x\\1/ (to have a good format for internal calls when 'x' is missing
    s/^\\+x// (permit internal calls)
    s/^\\+00/+/ (to have a good format for international calls)
    s/^\\+0/+33/ (to have a good format for national calls)
    s/^\\+330/00/ (to have a good format for national calls)
    s/^\\+33/00/ (permit national calls)
    s/^\\+N/N/ (for nomadic calls)
    s/^\\+M/M/ (for mobile, OTC PC or external number)
    s/^\\+V/V/ (for video calls)
    s/^\\+/000/ (permit international calls)" (p108/p317-318)
  summary: |
    逐条转写法国 Default 域 DAS 10 规则（顺序即处理序，输出接输入）：①s/^\\+(\\d{3,6})$/+x\\1/ 补 x；
    ②s/^\\+x// 放行内呼；③s/^\\+00/+/ 国际格式化；④s/^\\+0/+33/ 国内格式化；⑤s/^\\+330/00/ 国内格式化；
    ⑥s/^\\+33/00/ 放行国内；⑦s/^\\+N/N/ nomadic 呼叫；⑧s/^\\+M/M/ 移动/OTC PC/外号；⑨s/^\\+V/V/ 视频呼；
    ⑩s/^\\+/000/ 放行国际。构建范式 s/XXX/YYY/ 替换 + () 捕获 \\1；正则元字符见 p303 速查表。R2.0 起
    nomadic 场景必须确保规则 7/8 存在。
  conditions: 规则按国家定制（本书仅法国）；声明顺序重要且可多条同时命中（p108 WARNING）
  tags: [metric, das, regex, conference]

- id: p44
  title: 系统选项格式化实例——00/0/33/3-5 位分机下五类输入的变换结果
  type: metric
  source_pages: p302
  source_chapter: DAS rules / Process example
  source_quote: |
    "International dialing prefix: 00 • National dialing prefix: 0 • Country code: 33 • Extension filter:
    number from 3 to 5 digits
    User's dialed digits / Modifications according to system options:
    31500 +x31500
    0298143322 +33298143322
    0041123456789 +41123456789
    +1234567890 +1234567890
    1234567890 'Please enter a valid phone number'" (p302)
  summary: |
    逐行转写：分机 31500 → +x31500；国内 0298143322 → +33298143322；国际 0041123456789 → +41123456789；
    已带 + 的 +1234567890 原样保留；无 + 无前缀的 10 位长号 1234567890 → 报"Please enter a valid phone
    number"。这是 DAS 之前系统选项层的格式化基准，排障时先核该层输出再查 DAS 规则。
  conditions: 系统选项为 ACS Configuration/System options
  tags: [metric, das, examples]

- id: p45
  title: 实验口径：关键账号与凭据全集（WebAdmin/CA/Outlook/AD/FreeRADIUS）
  type: metric
  source_pages: p99, p113, p186, p210-213, p375, p410, p459
  source_chapter: 各 How-To
  source_quote: |
    "User otAdmin • Password admin8770 (WebAdmin, for this training)" (p313, p381)
    "Login: administrator • Password: superuser (https://eco.company.com/CertSrv)" (p113)
    "Login: ICEaccess • Password: iceaccess ... Password never expires" (p184-185)
    "Login: barkley • Password: 1234 (Outlook 2013 lab)" (p210, p213)
    "Login: Administrator • Password: superuser (DCS VM logon)" (p375)
    "Login: directory@company.com • Password: directory (AD access)" (p247)
    "server.shared_secret=training (FreeRADIUS)" (p459)
  summary: |
    实验口径（RLAB 专用，生产必须替换）：WebAdmin otAdmin/admin8770；Windows CA（eco.company.com/CertSrv）
    administrator/superuser；UM 特权账号 ICEaccess/iceaccess（密码永不过期）；Outlook 实验 barkley/1234；
    DCS 虚机 Administrator/superuser；AD 目录访问账号 directory（@company.com）；Kerberos ice_kerb 密码
    1234；FreeRADIUS 共享密钥 training。8770 客户端另备 adminnmc/Superuser01* 与 Superuser/Superuser01*
    （p9）。
  conditions: 明文密码为 2019 年培训文化产物，禁止用于生产
  tags: [metric, lab, credentials]

- id: p46
  title: 日历/同步排障命令与日志路径清单（TC2258）
  type: checklist
  source_pages: p409-413 (TC2258)
  source_chapter: Calendar Presence & Calendar Synchro / Troubleshooting
  source_quote: |
    "restart the Wireal service with following command: 'service wireald restart'" (p409)
    "If Calendar Presence feature doesn't work after all configuration steps restart tomcat, acs and wireal:
    service tomcatd restart • service acsd restart • service wireald restart
    Then the following logs must be checked: logs/acs-exchange-connector/exchange-connector.log
    /logs/wireal/_calendar.log /logs/wireal/_calendar_acs.log /logs/wireal/_calendar_exchange.log ..." (p411)
    "calendar:users • calendar:calendars • presence;provider-list • presence:display * * •
    ews:subscription-list ($WIREAL_HOME/bin/client)" (p411)
    "Conferences correctly synchronized ... stored in /tmp/exchange-connector-que-suceeded ... waiting to be
    pushed ... /tmp/exchange-connector-que ... not correctly pushed ... /tmp/exchange-connector-que-failed" (p413)
  summary: |
    排障清单：①先重启服务 tomcatd/acsd/wireald；②查日志——exchange-connector.log 与 /logs/wireal/ 下
    _calendar.log、_calendar_acs.log、_calendar_exchange.log、calendar-configuration.log、
    calendar-provider-acs.log；③深度诊断工具 $WIREAL_HOME/bin/client 执行 calendar:users、
    calendar:calendars、presence;provider-list、presence:display * *、ews:subscription-list；④dla.sh 开
    Calendar Presence 全量调试；⑤OTC PC 侧 Save logs + OT 侧 Logzipper.bin 0 days 收集后开 eSR；⑥同步队列
    三目录——/tmp/exchange-connector-que-suceeded（成功）、-que（待推）、-que-failed（失败）。用户侧不发在
    场：Outlook File>Options>Calendar>Free/Busy Options→Read=None；要显示主题/地点选 Free/Busy, subject,
    location。
  conditions: 日历同步验证后需 service wireald restart 生效
  tags: [checklist, calendar, troubleshooting, logs]

- id: p47
  title: Nomadic/Ghost 维护工具 tsa_maintenance 用法——选项 20 dump、受保护菜单 100/2998、ACAPI 106→7 加载
  type: checklist
  source_pages: p55-57
  source_chapter: OTC PC nomadic How-To / Maintenance
  source_quote: |
    "'tsa_maintenance' script is located in '/opt/Alcatel-Lucent/infra_services/ots/'" (p55)
    "20 [+ qmcdu] ----------- Dump Nomadic [or LightLine]" (p55)
    "100 -------------------- MENU PROTECTED by secret code ... This a menu protected by secret code (2998
    is the secret code value). So, choose the 'ACAPI control' by entering '106 2998'" (p56)
    "Load All Acapi Object :7 ... At the end of the synchronization, check that all objects have been
    retrieved in the 'ots' database by using option '47' again to dump all QMCDU, or, option '20' dump
    nomadic" (p57)
  summary: |
    Ghost 资源核查三步：①cd /opt/Alcatel-Lucent/infra_services/ots 后运行 ./tsa_maintenance（连接
    opentouch 3595 端口验证）；②选项 20 dump Nomadic——核对 Ghost Z 号（31017/31018/31019，Z nomadic 1，
    type analog）是否在 ots 库；③不在则手动同步：选项 100（受密码保护，秘密码 2998）→ 输入 106 2998 进
    ACAPI control → 选 7 Load All Acapi Object → 完成后再 dump 核验（原文提及 option 47 dump all QMCDU 或
    option 20 dump nomadic——47 在所列菜单中未出现，疑原文笔误，实际用 20 核验）。
  conditions: "ots" 即 OT 数据库口径；端口 3595/3695 为脚本默认
  tags: [checklist, nomadic, maintenance, tool]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 24 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 实验 POD 搭建核对 | 有 | p06 | POD 设置总表（IP/账号/密码全集，实验口径） |
| task-02 | ITSP1 联调 | 有 | p07 | 账号/号码/变换规则逐值 |
| task-03 | Nomadic 蜂窝模式 | 有 | p01, p03 | 池公式 + 许可对 |
| task-04 | Nomadic VoIP | 有 | p01, p02, p03 | 池公式 + 编解码/QoS 口径 + 许可对 |
| task-05 | Nomadic 维护 | 有 | p47 | tsa_maintenance 三步用法 |
| task-06 | Desksharing 配置 | 有 | p04, p05 | 虚拟 MAC 公式 + 系统参数四件 |
| task-07 | Desksharing OTC PC 与维护 | 有 | p03, p04 | Flex Office+Desktop 许可、MAC 反查 |
| task-08 | 反向代理与 OTSBC | 有 | p14 | 端口/端口段总表 |
| task-09 | DAS/ACS FQDN/证书 | 有 | p37, p43, p44 | 证书规则 + DAS 10 条 + 格式化实例 |
| task-10 | OXE 通用参数 | 有 | p09, p10 | 速拨范围/Ghost 编号 + DISA/前缀清单 |
| task-11 | iPhone+ SBC/系统参数 | 有 | p12, p13, p08 | APNS 端口证书 + 协议规则 + 溢出定时器 |
| task-12 | 设备档案与用户 | 有 | p11 | 编号命名空间规则（B/D/A 前缀语义） |
| task-13 | 核验与手工补充 | 有 | p11, p08 | ARS 数值口径 + Entity/COS |
| task-14 | Extended Mobility | 有 | p41, p42 | 前提/成本/QR 语法 + 行为规则 |
| task-15 | UM (Exchange) 部署 | 有 | p30, p31, p32 | Impersonation + 声明清单 + 档案参数 |
| task-16 | 邮箱权限/云上下文/维护 | 有 | p30, p31, p33 | delegation/impersonation 分界 + O365 通知 + Gmail/IMAP 边界 |
| task-17 | 目录搜索部署 | 有 | p20, p21 | 同步周期规则 + 属性上限 |
| task-18 | SBC 合并与 UDAS 维护 | 有 | p22, p23 | merge keys 规则 + 照片优先级 |
| task-19 | 会议服务器配置 | 有 | p38, p39, p43 | 系统选项/SIP 代理 + 桥号成对 + DAS |
| task-20 | 数据会议运用 | 有 | p15, p16, p17, p34, p40 | 密码/DTMF/协作限制/文档/One Touch |
| task-21 | DCS 安装声明 | 有 | p35, p36 | 兼容矩阵 + Windows 四件 |
| task-22 | 日历在场/同步 | 有 | p18, p19, p46 | 优先级/展示公式 + 排障清单 |
| task-23 | LDAP/RADIUS 认证 | 有 | p24, p25, p26, p29 | 容量口径冲突 + 两份插件清单 + 作用域规则 |
| task-24 | Kerberos SSO | 有 | p27, p28, p29 | 四件套路径/keytab 命令 + SPN/WBM 规则 |

**覆盖结论**：24/24 全部有对应条目，无缺口。三点口径说明：
1. 容量类数字（Ghost Z 池、速拨范围、LDAP 上限）均逐值对照原文；p24 的"20 vs 5"是原书讲义/实验两处口径不一致，已如实并列并给推断标注。
2. p45 实验凭据全集与 p06/p07 有部分重叠（p06/p07 按拓扑组织，p45 按用途组织），供不同场景引用。
3. tsa_maintenance 的 "option 47" 在原文菜单中未出现，按原文照录并标注疑为笔误（p47），未编造修正值。
