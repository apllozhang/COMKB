# 原则/清单/规则/公式/数值口径候选 — OXO Connect Starter (OXOCXTE300EN Ed16)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号、号码、ARI）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: 交付前数据采集清单——IP/密码/编号/组/呼入呼出/Rainbow 六块
  type: checklist
  source_pages: p43-49
  source_chapter: Data collection（七页讲义）
  source_quote: |
    "Data collection gathers customer needs, information on its ecosystem and the functionalities
    to be implemented." (p43)
    "Ecosystem • OXO Connect Evolution: • Eth0: 192.168.1.246 • Eth1: 192.168.94.246 • PC:
    192.168.1.10 • DNS: 192.168.1.250 • DHCP phones/xBS: 192.168.1.10 to 69 • Default router
    address: 192.168.1.254" (p44)
    "OXO Connect will be connected to Rainbow including the WebRTC gateway. A Rainbow company has
    already been created An administrator has been identified" (p49)
  summary: |
    采集七块：①Ecosystem IP 规划（Eth0/Eth1/PC/DNS/DHCP 池/网关，p44 实验口径）；②FTR 三参考值
    （Partner fleet/Sub-fleet/Installation ID）+ 终端清单（4 IP 话机、1 xBS、1 DECT 手柄）；③系统
    账户密码表（七账户）；④编号计划（三位：分机 100-199、主中继组 0、hunt 500-525、话务台 0、DDI
    41100-41199 话务台 41100、日夜模式分发不同）；⑤语音信箱要求（1 个 answer-only、1 个可录音
    实时监听、建删信箱）；⑥组要求（hunt 501 含 3 话机、代接组 3 话机、广播组 1 发 2 收、经理-秘书
    组）+可编程键清单；⑦呼入（2 个话务台组+组 8 默认、时段 8-19 组1/19-8 组2、欢迎预公告）、SIP
    参数、呼出限制（9 出局、1 用户无权、国际与特服禁、部分用户经话务台）、Rainbow 前提（含网关、
    公司与管理员已定）、维护（1 个自动周期备份、版本升级计划）。
  conditions: 全部为实验口径值；生产替换为客户真实数据
  tags: [checklist, data-collection, planning]

- id: p02
  title: 七个系统账户密码表与默认密码历史
  type: metric
  source_pages: p45, p94-95
  source_chapter: Data collection Settings / Passwords
  source_quote: |
    "Accounts Passwords Attendant Letacla1 Administrator Qwerty12 Installer Alcatel1 Download
    Oxopb123 NMC (omnivista) Pbxnmc12 ACD Acdc1064 Users 142535" (p45，实验口径)
    "The administration passwords must be defined at the first start up of the system" (p94)
    "Old default passwords (< Release 10.1) Don't use anymore: Installer : pbxk1064 Administrator :
    kilo1987 Attendant: help1954 Download: pbxk1064 NMC: tuxalize Users: 151515 … Also used for
    first installation: pbxk1064" (p95)
  summary: |
    七账户：Attendant/Administrator/Installer/Download/NMC(omnivista)/ACD/Users，实验口径密码如上
    （p45 表）。历史默认密码（R10.1 前后）：pbxk1064（installer，至今仍用于首次安装连接）、kilo1987、
    help1954、tuxalize、151515——教材明示"Don't use anymore"。管理密码集中在 OMC/Security/
    Passwords/Management Password；用户密码在 OMC/Security/Passwords/Subscribers Passwords。
  conditions: 首启强制定义管理密码；实验值为教学约定
  tags: [metric, passwords, security]

- id: p03
  title: 密码构造规则——管理 8 位三类字符、用户 4/6 位数字
  type: rule
  source_pages: p94, p184
  source_quote: |
    "Total length of 8 characters • At least one lowercase alphabet letter (a-z) • At least one
    uppercase alphabet (A-Z) • At least one digit (0-9) • Special characters are not allowed …
    4 or 6 digits, strongly advising to use 6 digits for enhanced security" (p94)
    "The system do not allow users to configure weak phone passwords (000000,123456…)" (p184)
  summary: |
    管理密码硬规则：总长 8 字符、至少一个小写+一个大写+一个数字、不允许特殊字符。用户（信箱）密码
    4 或 6 位数字、强烈建议 6 位；系统拒绝弱密码（000000、123456 等简单序列）。安全基线参考技术
    通函 TC1143（p94、p184、p327-329 三处引用）。
  conditions: OMC 在线帮助有细节；特殊字符在管理密码中禁用（版本口径）
  tags: [rule, passwords, security]

- id: p04
  title: DSP 通道扩展表——16/48/60/76 四档与编解码配比
  type: metric
  source_pages: p37
  source_chapter: 76 DSP channels when using the Armada 64
  source_quote: |
    "PowerCPU EE w/o daughter board Always Multi-Codec 16x G711/G729 16 … + ARMADA-32 daughter board
    Optional Multi-Codec 48x G711/G729 48 … + ARMADA-64 daughter board Optional Multi-Codec 60x
    G711/G729 60 … Multi-Codec + G711 30x G711/G729 + 46x G711 76" (p37)
    "76 SIP trunks (60 in former release 2.0, 48 in OXO R10.3)" (p37)
  summary: |
    DSP 通道四档：无子板 16（全 G711/G729 多编解码）；+Armada 32=48；+Armada 64=60（全多编解码）或
    76（30 G711/G729+46 G711 混合）。OMC 两种配比二选一。历史：76 的前身为 60（R2.0 时代 76 SIP
    trunks 限制前值为 60）、OXO R10.3 为 48。收益=突破私有 SIP trunk 与 SIP trunk 应用的部署限制。
  conditions: PowerCPU EE 平台；前提装 Armada 64；容量受 VoIP Channels mode 设置约束
  tags: [metric, dsp, capacity, armada]

- id: p05
  title: SIP 中继服务等级——120 通道（IPBox）/76（PowerCPU+Armada）与编解码帧长
  type: metric
  source_pages: p201
  source_chapter: SIP trunks – Level of services
  source_quote: |
    "VoIP resources: •120 with IP Box •120 Simultaneaous SIP trunks supported •Up to 76 with
    POWERCPU EE and a daughter board ARMADA VoIP64 (16 by default)" (p201)
    "Voice CODEC: OPUS, G711, G722, G722.2, G723.1, G729a … G711/G722 Framing 20 - 30 - 60 ms •
    G723 Framing 30 - 60 - 90 - 120 ms • G729 Framing 20 - 30 – 40 – 50 - 60 - 90 - 120 ms •
    Maximum framing for IP Touch: 60ms" (p201)
  summary: |
    并发 SIP trunk：IPBox 120；PowerCPU EE 默认 16、装 Armada VoIP64 至 76。编解码 OPUS/G711/G722/
    G722.2/G723.1/G729a；VAD（静音抑制+舒适噪声）；帧长：G711/G722 20-30-60ms、G723 30-60-90-120ms、
    G729 20-30-40-50-60-90-120ms、IP Touch 最大 60ms。另支持：Direct RTP 与 RTP Proxy（公私 SIP
    trunk）、FoIP T38 ECM 或 G711 承载、DTMF RFC2833、QoS 三层（L3 ToS/DiffServ RFC2474、L2
    802.1p/q、QoS Ticket 8770）、UDP&TCP、SDP RFC4566。
  conditions: 并发数同时受 license 控制与硬件 DSP 通道约束
  tags: [metric, sip-trunk, codec, qos]

- id: p06
  title: ETH1 服务口参数表与安全四边界
  type: metric
  source_pages: p57
  source_chapter: OXO Connect Evolution: Serviceability
  source_quote: |
    "Fixed IP address: 192.168.94.246 • Netmask: 255.255.255.0 • Gateway: 192.168.94.1 • DHCP
    range: 192.168.94.247, 192.168.94.254 • DHCP lease: 2 hours • DNS server: 192.168.94.246" (p57)
    "Eth1 MUST not be connect on the LAN • No access to Eth0 LAN is allowed from Eth1. • Eth1 can
    be disabled in OMC. • Eth1 is disabled in case of IP conflict with Eth0" (p57)
  summary: |
    ETH1 固定参数：IP 192.168.94.246/24、网关 192.168.94.1、DHCP 池 .247-.254、租期 2h、DNS=本口
    .246；myipbox.ale 可直连。安全四条：不得接 LAN；Eth1 不能访问 Eth0 侧 LAN；可在 OMC 禁用；
    与 Eth0 IP 冲突时自动禁用。能力边界：仅允许配 ETH0 参数与 Webdiag 诊断，需 installer/operator/
    manufacturer 身份，不允许用户应用。
  conditions: OCE 专属；ISP SIP 也可接 ETH1 提升两子网间安全（p57 脚注、p200 重复）
  tags: [metric, eth1, security, oce]

- id: p07
  title: 默认 IP 与版本查询口径
  type: metric
  source_pages: p67, p93
  source_chapter: Authentication / Default Configuration
  source_quote: |
    "Default IP Address: 192.168.92.246 • Default Password: pbxk1064 (First connection)" (p67)
    "Default IP Addresses • Main CPU: 192.168.92.246 • Subnet mask: 255.255.255.0 • Default
    gateway: 192.168.92.1" (p93)
    "By MMC Station on phone 8078s/8068s/8038/8039: • Menu/System/Version • ONEFR03x/xxx.yyy" (p93)
  summary: |
    出厂默认：主 CPU 192.168.92.246/24、网关 192.168.92.1；installer 首连密码 pbxk1064。查版本：
    话机（8078s/8068s/8038/8039）Menu/System/Version 显示 ONEFR03x/xxx.yyy 格式。
  conditions: 默认值适用于出厂/冷复位后
  tags: [metric, default-ip, version]

- id: p08
  title: 动态路由数值口径——默认 12s/24s、计时器上限 3276s、级联上限 5
  type: metric
  source_pages: p90, p164-166
  source_chapter: Default Configuration / Dynamic routing
  source_quote: |
    "Users (internal and external calls) directed to the voice mail after 12 seconds • Operator
    calls to the default operator group (N°8) after 24 seconds" (p90)
    "Timer 1 for level1: Up to 3276 seconds Timer 2 for level2: Up to 3276 seconds" (p165)
    "Maximum value allowed: 5" (p166)
  summary: |
    数值：出厂默认 T1=12s 转信箱、话务台呼叫 24s 转默认组 8；用户级 T1/T2 上限各 3276 秒；不选计时
    器但填目的地=立即转；级联最大级数 5（系统参数可设，示例 3）。目的地类型：hunt group/分机/集体
    缩位（默认 VM hunt group）；General level=活动话务台组、General bell 仅外线呼入。
  conditions: 默认值出厂口径；apply diversion 不勾则一切转移禁用（p165）
  tags: [metric, dynamic-routing, timers]

- id: p09
  title: 默认键 profile 对照表——Single line / Key system / PCX
  type: metric
  source_pages: p163
  source_chapter: Key Profiles
  source_quote: |
    "Type of subscriber Normal Mode Single line Key system PCX Default resource keys 3 « virtual »
    resource keys 2 RGM n RSP 2 RGM 2 RSB Simultaneous management 1 conversation 1 hold 1 camp-on …
    1 conversation (n+1) holds + camp-on … 1 conversation 3 Holds + camp-on … n = number of analogue
    lines and B channels (within the station key limit)" (p163)
  summary: |
    对照：Single line（普通模式）默认 3 个"虚拟"资源键、并发管理 1 通话+1 保持+1 驻留；Key system
    模式 2 RGM+n RSP、(n+1) 保持+驻留；PCX 模式 2 RGM+2 RSB、3 保持+驻留。n=模拟线数与 B 通道数
    （受话机键数上限约束）。默认 profile 还取决于话机型号与用户类型（attendant/manager/secretary/
    normal）。
  conditions: 详见 Expert 文档 User services/Resource key
  tags: [metric, keys, multiline, profiles]

- id: p10
  title: 语音信箱容量与行为数值——1h/120s/2 端口/30 天/15 秒
  type: metric
  source_pages: p183, p188
  source_chapter: Commercial Offer / Conversation recorder
  source_quote: |
    "2 accesses • 4 languages • 1 hour of stored messages … Greeting messages for the subscriber
    and general mailbox Up to 120 seconds … Additional ports (up to 8) • Additional message storage
    time and languages • 4 hours • 30 hours • 200h" (p183)
    "End of recording … If silence during 15 seconds (by default) Conversations recordings deleted
    after 30 days by default" (p188)
  summary: |
    基线：VM 集成 CPU、每话机一信箱、2 个接入端口、4 语言、1 小时消息存储、问候语至 120 秒；可选
    扩展：端口至 8、存储 4h/30h/200h。会话录音：结束条件=# 键/挂机/15 秒静音（默认）；录音默认 30
    天删除；暂停仅软键话机且时长受限。语音文件格式 ADPCM 4bit 8kHz Mono（系统）与 WAV PCM 16bit
    8kHz Mono 可互转（p186）。
  conditions: 扩展为可选服务（Additional Services）
  tags: [metric, voicemail, capacity]

- id: p11
  title: 编号计划数值口径——Base 0-2199、三位默认、安装号去首位
  type: rule
  source_pages: p128-130, p135
  source_chapter: Dialing Plans bases / Installation number / Setting up the numbering plan
  source_quote: |
    "Base Always a number from 0 to 2199" (p135)
    "Installation number can also be entered at installation wizard • It is the main system DDI
    number • Enter the installation number without the first digit" (p130)
    "Configure directory numbers from 100 to 149 for extension calls This makes numbers 150 to 199
    available for possibly other functions." (p134)
  summary: |
    规则：Base 取值范围 0-2199；默认三位计划（分机 100 起、9 话务台、0 主中继组）；安装号=主系统
    DDI 号去第 1 位录入；规划技巧：分机段收到 100-149、把 150-199 留作其它功能；建段前删冲突旧段
    （200-299 编程模式、400-434 副中继组、60 Appointment 等）。Pick-up 与 Forwarding 两族前缀的
    Base 固定（见 f17）。
  conditions: 默认计划随安装国家变化
  tags: [rule, numbering, base]

- id: p12
  title: 消息与彩铃数值——4-20 条/320 秒/MoH 格式/Entity 1-4
  type: metric
  source_pages: p244, p247-250
  source_chapter: Messages 1 to 20 / Music on hold
  source_quote: |
    "the system can have 4 to 20 audio messages … The total length of the messages is 320 seconds
    This length is allocated dynamically to the 20 messages" (p244)
    "Files .wav must be in 16-bit PCM 8 Khz Mono or CCITT A-law or μ-law 8-bit 8Khz Mono format" (p247)
    "Default value: Entity1 (possible values entity 1 to entity 4 used in case of multi company)" (p248)
    "personalize MSG1 to MSG20 welcome messages (4 by default, 20 with license)" (p250)
  summary: |
    音频消息 4 条（默认）至 20 条（许可）、总长 320 秒动态分配；MoH 仅外线保持播放、三源（默认乐/
    Tape 音频输入/录制 .wav）、按 Entity 1-4 分别配置（多公司场景、无定制播默认乐）。.wav 硬格式：
    16-bit PCM 8kHz Mono 或 CCITT A-law/μ-law 8-bit 8kHz Mono。录制备选路径：话务员 MMC 会话 Menu
    Operator/Expert/Voice/Hold music/Message xx 或 Music xx。
  conditions: 消息数与软件钥匙相关
  tags: [metric, messages, moh, wav-format]

- id: p13
  title: 预公告数值与播放模式语义
  type: metric
  source_pages: p260-261, p269
  source_chapter: Pre-announcement / Preannouncement messages
  source_quote: |
    "Number of entries for individual greetings: 200 • Number of preannouncement messages: 20 •
    Messages duration: 320 seconds" (p260)
    "Before Call distr.: The message is broadcasted entirely then the destination will ring During
    Call distr.: The message is broadcasted and the destination will ring at the same time. If the
    called party answer before the end of the message, then the message is interrupted." (p269)
    "Only if busy Checked: the message is broadcast to the caller if the destination is busy" (p269)
  summary: |
    预公告体系数值：个人问候条目上限 200、预公告消息 20 条、时长合计 320 秒。每时段配置：模式三选
    （none/分发前播完再振/分发中边播边振、被叫应答即中断）、消息号 1-20、仅忙旗标（勾=仅目的地忙时
    播）。全局问候在 OMC/Subscribers Misc/Preannouncement Overview 的 Global Greetings/Details 配。
  conditions: 配置按时间范围逐日复制
  tags: [metric, preannouncement, incoming]

- id: p14
  title: 出局闭锁数值口径——6 张表、国际默认禁、默认 LC=12
  type: metric
  source_pages: p271-277, p286
  source_chapter: Outgoing calls management / Call barring management
  source_quote: |
    "6 barring tables = 6 levels of barring" (p274)
    "International calls are barred by default The international prefix 00 is added with type
    "Forbidden" in all barring table" (p274)
    "By default, the traffic sharing Link category values are : "Normal mode = 12" and "restricted
    mode = 12"" (p286)
  summary: |
    数值口径：闭锁表 6 张=6 级；前缀 00（国际）在所有表中默认 Forbidden；Traffic sharing 链路类别
    默认 normal=restricted=12；授权示例：用户改 LC=5 后 5∩12=矩阵"+"放行、其余用户 12∩12=空默认
    禁止；闭链示例：表 2 加 0053 Authorized + 全员 Barring LC=2 + 矩阵行 2 列 1=2。digit counter
    1=表内有授权前缀时的最大拨号位数、counter 2=未列前缀的最大授权位数。
  conditions: 默认值为出厂口径；Normal/Restricted 双值随日夜模式切换
  tags: [metric, barring, link-category]

- id: p15
  title: Normal/Restricted 双模语义与用户豁免权
  type: rule
  source_pages: p277-278, p283
  source_chapter: Normal/Restricted modes / Call barring management Notes
  source_quote: |
    "The system uses restricted LC values for traffic sharing, barring and collective speed dial
    access If the restricted mode is activated • Except if the "Inhibition time ranges" flag is
    disable … By default the users don't follow the time range state." (p277)
    "disable the parameter "Inhibition Time-ranges", so that extensions follow Normal/restricted
    mode defined in time ranges. Otherwise, the phone sets always stay in normal mode even if the
    system switches in restricted mode." (p283)
  summary: |
    规则：restricted 模式激活后系统对 traffic sharing/barring/集体缩位接入采用 restricted LC 值。
    两个用户级豁免权："Inhibition time ranges" 功能权=系统按时段自动切 restricted 时该用户保持
    normal；Inhibition flag=话务员手动切 restricted 时保持 normal。关键坑（p283 注）：要让话机跟随
    时段，必须在话机 details/Feature Rights Part 2 里关掉 "Inhibition Time-ranges"——否则话机永远
    normal 模式。
  conditions: 默认"用户不跟随时段状态"——实施时要逐用户核对
  tags: [rule, restricted-mode, time-ranges, pitfall]

- id: p16
  title: 备份介质数值口径——SD 卡 2-32GB/EXT2/AES256/同主版本
  type: metric
  source_pages: p301-304
  source_chapter: SD card for backup / IP Box SD card Backup/Restore / Misc
  source_quote: |
    "Remotely manageable Encrypted (AES 256) … The minimum size is 2 GB and maximum size is 32GB •
    SD and SDHC supported • SDXC is not supported • Formatting only via OMC • Supported file system
    is EXT2" (p301, p304)
    "Restore of a recovery point is only supported in the same major release The oldest recovery
    point is deleted automatically by a new one" (p304)
  summary: |
    OCE SD 卡备份：加密 AES 256、可远程管理、计划+立即、用户+配置数据、多恢复点；恢复点数量取决于
    卡容量与恢复点大小、最旧的自动被新备份删除；恢复仅支持同主版本；卡约束 2-32GB、SD/SDHC 支持
    SDXC 不支持、仅 OMC 格式化、文件系统 EXT2；插拔须关机状态；ALE 不供卡。
  conditions: OCE 专属；PowerCPU EE 备份在 eMMC（换 CPU 需重新生成 license，p296）
  tags: [metric, backup, sd-card]

- id: p17
  title: 复位数据保留矩阵——Cold 不勾子选项时的保留项
  type: rule
  source_pages: p322-324
  source_chapter: System reset / Cold reset options
  source_quote: |
    "When Cold reset is triggered without selecting any sub options • The following settings are
    not deleted: • Installer passwords • Network settings • Management services access flags •
    Cloud Connect parameters" (p323)
    "Cloud Connect Data: • Activation state • FTR completion status • Server URL • One Time
    Activation account and password • Final account and password" (p323)
  summary: |
    规则：三档复位 Warm/Cold/Factory 递进删除；Cold 不勾子选项时保留四类（installer 密码、网络设
    置、管理服务接入旗标、Cloud Connect 参数）；数据六分类：User Data（VMU/IM/Mails）、System Data
    （备份文件/metering/traces/ACD 统计）、Cloud Connect Data（激活态/FTR 状态/服务器 URL/一次性与
    最终账户密码）、Network（主机名/IP/掩码/广播/网关/VLAN/路由器/DNS/Web 代理五元组）、Management
    Passwords（五个管理账户）、Management Data（WAN 管理旗标）。Factory 额外删系统日志、状态接近
    Lola 安装态。
  conditions: Cold 复位前先备份；OMC 可排程自动复位（p324）
  tags: [rule, reset, data-classification]

- id: p18
  title: 防盗打基线——损失口径 2 万欧/周末与 TC1143 强制
  type: principle
  source_pages: p325-329
  source_chapter: Security warning
  source_quote: |
    "The Phreaking is the name for the telephony system hacking … The victims can loose more than
    20 K€ in one weekend • Your phreaked line is sell to the long distance carrier • Your phreaked
    line can be connect to a premium rate number The freaking is a business run by organised crime" (p326)
    "Not default • Change them regularly • Not simple, not short…" (p327)
    "It is mandatory to have document latest edition, read and apply its recommendations and also
    the SECURITY Chapter from Expert Documentation" (p329)
  summary: |
    原则：盗打目标是客户钱包（一个周末可损失 2 万欧元以上），被盗线路卖给长途运营商或接高费率号，
    属有组织犯罪。防线：按推荐规则配置系统/用户/功能；密码常识三句（非默认、常改、不简单不短）；
    升级最新版享受默认值与安全补丁；安装员有责任告知用户/管理员安全功能并与客户商定安全级别；
    强制使用最新版 TC1143（内容：访问控制密码策略、用户与系统密码管理、远程接入配置、系统配置
    设置、待处理安全项汇总）并应用 Expert 文档 SECURITY 章。
  conditions: 全部署场景强制；TC1143 在 BPWS/MyPortal 获取
  tags: [principle, security, phreaking, tc1143]

- id: p19
  title: Rainbow 接入验收口径——两个状态字符串
  type: metric
  source_pages: p240, p349
  source_chapter: Public SIP Gateway 5.4 / Connect an OXO to Rainbow 3.1
  source_quote: |
    "OMC/History and Anomalies/History Table Message displayed: SIP registration success" (p240)
    "OMC /Tools /Webdiag /Services /Rainbow Status Control the connection status: « connected with
    final password »" (p349)
  summary: |
    两个验收字符串：①公共 SIP 中继注册成功=OMC/History and Anomalies/History Table 显示 "SIP
    registration success"；②Rainbow 连接正常=Webdiag/Services/Rainbow Status 显示 "connected with
    final password"（登录 installer）。配套排障物：系统日志 ccrbagent.log（Webdiag/System/System
    Files/Log files）与用户侧日志（Rainbow 界面 User Settings/About Rainbow/Open logs）。
  conditions: 字符串为 R6.3/Ed16 口径；升级后以最新文档为准
  tags: [metric, verification, sip, rainbow]

- id: p20
  title: WebRTC 网关容量口径——20/50 通话与 150 用户上限
  type: metric
  source_pages: p374, p392
  source_chapter: Rainbow WebRTC Gateway on OCE Front-End / Dimensioning
  source_quote: |
    "Type of Rainbow GW OXO Connect (Power CPU EE) OXO Connect evolution (IPBox) Internal GW Not
    supported 20 calls max. External GW (NUC) 50 calls max. 50 calls max. OCE-FE GW 20 calls max.
    Not supported" (p374)
    "50 VoIP calls maximum if the WebRTC gateway is external on Mini PC or ESXi server • 20 VoIP
    calls maximum with OCE integrated WebRTC gateway or if the WebRTC gateway is external on OCE
    Front End … Maximum of OXO users with Rainbow VoIP option increased from 50 to 150" (p392)
  summary: |
    容量矩阵：内部网关——PowerCPU EE 不支持、IPBox 20 通话上限；外部网关（NUC）——两硬件均 50；
    OCE-FE 网关——PowerCPU EE 呼叫服务器 20、IPBox 呼叫服务器不支持。通则：外部（Mini PC/ESXi）最
    大 50 通话、OCE 集成或 OCE-FE 最大 20；OCE 需要更多通道时改走外部拓扑（至 50）。Rainbow VoIP
    用户上限 50→150（两硬件均适用）。推荐通道表：5 用户 5 通道、10→7、20→11、30→15、50→20、
    70→27、100→36、150→50（70 以上集成列 NA，见 p392 表）。
  conditions: R6.3 口径；集成拓扑用户上限还受实际话务影响（p392 注 (*)）
  tags: [metric, webrtc-gateway, capacity, dimensioning]

- id: p21
  title: OCE-FE 专用口径——≥R4.0 MD、端口 5059、PBXID 双机一致
  type: rule
  source_pages: p373-379
  source_chapter: Use case # 2 OCE Front End
  source_quote: |
    "The release ≥ R4.0 MD must be installed on both the Front-End RGW and the OXO Connect call
    server … Release ≥ R4.0 MD is mandatory" (p373)
    "Verify port numbers to 5059 in the SIP Gateway parameters … Rainbow PBXID must be the same in
    both OXO Connect, Front-End and call server" (p379)
    "On the OXO, by entering an FTR, the PBXID and the activation code are initialized by default to
    "FleetRef-Installref"" (p379)
  summary: |
    规则三条：①FE 与呼叫服务器两台都必须 ≥R4.0 MD（强制）；②自动创建的私有 SIP 网关核对端口
    5059；③FE 与呼叫服务器的 Rainbow PBXID 必须相同——FTR 时默认占位 "FleetRef-Installref"（允许
    提前在 RB WebAdmin 备料、FTR 结束自动连到 FleetRef-Install_ID），Rainbow 公司已存在时两台都要
    填真实 PbxId（示例 PBX9a86-5916-b74a-436c-aec6-c08a-58b6-5bb0）。配套：FE 模式限 WebRTC GW
    功能（无 UTL）、不提供 PBX 能力、供给不需要 OMC、许可免费由 FTR 自动给。
  conditions: OCE-FE 专属；开通场景细则跟 Rainbow WebRTC cookbook 最新版（p382）
  tags: [rule, oce-fe, version, pbxid]

- id: p22
  title: WebRTC 自动配置边界——自动五项 vs 安装员三项
  type: rule
  source_pages: p366, p395
  source_chapter: Automatic configuration / Internal WebRTC Gateway automatic configuration Description
  source_quote: |
    "The following settings are managed automatically: • Activation of internal WebRTC gateway (OCE
    only) • Creation of WebRTC SIP gateway • Configuration of the SIP Account with the Rainbow PBX
    ID • Creation of VoIP accesses and trunk group • Configuration of ARS table to route Rainbow
    calls The following settings are still to be done by the installer as they are specific to each
    customer : • Connect PBX to Rainbow • Creation and association of the AnyDevice/Rainbow virtual
    terminals • Configuration of numbering plans and of the barring" (p366)
    "Automatic configuration applies to versions greater than R4.0.020.002" (p395)
  summary: |
    规则：自动配置（≥R4.0.020.002，Reseller 管理员唯一授权账户发起）自动管五项（内部拓扑：激活内
    部网关[仅 OCE]、WebRTC SIP 网关、SIP 账户含 Rainbow PBXID、VoIP 接入与中继组、ARS 路由表）；
    外部拓扑自动四项（无内部激活项）、安装员另加"安装配置外部 VM/独立 PC"与"激活网关"两项。安装员
    永远自管三项：连 PBX 到 Rainbow、建并关联 AnyDevice/Rainbow 虚拟终端、编号计划与闭锁。
  conditions: 版本下限 R4.0.020.002（实验口径 "greater than"）；Reseller 账户专属（p396）
  tags: [rule, auto-configuration, webrtc-gateway, boundary]

- id: p23
  title: UTL 许可口径——四种终端各占多少
  type: rule
  source_pages: p101, p104, p368, p401
  source_chapter: ALE terminals / WebRTC Gateway / virtual terminals
  source_quote: |
    "Requires an IPDSP licence = UTL" (p101)
    "Requires one UTL + one Open SIP license per analog port" (p104)
    "Secondary station from Release 6.0: The Free Rainbow in Twinset virtual terminal must be used
    in order to save an UTL license (UTL Bypass)" (p368)
    "• Deskphone + Free Rainbow virtual terminal = 1 UTL • Anydevice only = 1 UTL" (p401)
  summary: |
    UTL 口径：IPDSP 软话机=1 UTL；模拟-SIP 网关每模拟口=1 UTL+1 Open SIP license；Deskphone+Free
    Rainbow in Twinset 虚拟副站合计=1 UTL（R6.0 起 UTL Bypass，副站不再额外吃许可）；纯 Anydevice
    =1 UTL。版本语义：R5.2 及以前 Multiset 副站用 Anydevice（额外吃 UTL），R6.0 起必须改用 Free
    Rainbow in Twinset 才省许可。
  conditions: UTL=Universal Telephony License（书中未展开全称，见 p28 Extended/Universal Telephony
    License 字样）
  tags: [rule, licensing, utl, twinset]

- id: p24
  title: Rainbow 话务台规格——8/10 通话、5 组、30 人、4 通监督
  type: metric
  source_pages: p409-417
  source_chapter: RAINBOW ATTENDANT CONSOLE / SUPERVISION GROUPS / APPLICATION VIEW
  source_quote: |
    "Manage up to 10 calls for OXE - And up to 8 calls for OXO Connect" (p409)
    "Maximum number of supervision groups for a supervisor 5 Maximum number of users in a group
    (supervisors + supervised) 30" (p412)
    "REX on OXE (Up to 10 calls) - Any Device on OXO Connect (minimum R6 version Maximum 8 calls" (p414)
    "Up to 4 calls supervised" (p417)
  summary: |
    数值：呼叫队列 OXE 10 通/OXO Connect 8 通；保持数由话务员软话机线的多线资源决定——OXE REX 至
    10、OXO Connect Any Device（最低 R6 版本）至 8；每监督员至多 5 个监督组、每组至多 30 人（监督员
    +被监督者合计）；互助监督视图同时监督至多 4 通呼叫。约束：话务台功能仅 PC（厚客户端/Web）；拦截
    仅同 PBX、仅电话呼叫、互助组代接仅 PBX 呼叫。
  conditions: Attendant 订阅按成员计费；移动端不可用
  tags: [metric, attendant-console, capacity]

- id: p25
  title: Rainbow 订阅目录与电话服务门槛
  type: metric
  source_pages: p335, p409, p421
  source_chapter: Subscription plans / Attendant console / ATTENDANT subscription
  source_quote: |
    "Rainbow Essential This free option is available to anyone who wants to try Rainbow for an
    unlimited period (no SLA). … Rainbow Enterprise Conference … pre-paid yearly in advance (twelve
    months). … Rainbow Conference An optional service proposed as a "pay-as-you-go" model" (p335)
    "An Attendant subscription is required for each member using this feature" (p409)
    "Choose the subscription offer: Attendant Monthly … DON'T USE "PREPAID" IN THE TRAINING" (p421)
  summary: |
    本书订阅目录七种：Essential（免费无 SLA 可混用）、Business、Enterprise（+多方视频/扩展存储/
    O365 与 Google Suite 集成）、Enterprise Conference（+无限电话会议分钟、按年预付 12 个月）、
    Conference（pay-as-you-go 按分钟/连接、组织者可为免费用户）、Connect（CRM 连接器）、Room（按
    房间、需额外硬件）；话务台功能另需 Attendant 订阅（每个使用成员一份数，Web/Desktop 可用、移动
    端不可）。计费方式示例：Attendant Monthly（月付）/Prepaid（培训禁用）。
  conditions: 订阅详情以 openrainbow.com/Subscription plans 为准；与 RAINXTE001EN 的 8 种口径互补
    （Attendant 单列）
  tags: [metric, subscription, licensing]

- id: p26
  title: DECT 部署数值口径——ARI 11 位八进制、LED 六步、PIN/AC 默认 0000
  type: metric
  source_pages: p119-122, p455-462
  source_chapter: IP-DECT xBS classroom installation / 8328 base stations
  source_quote: |
    "Enter the ARI number (11 digits in octal) … 11000436010 for POD 1 … 11000436060 for POD 6 …
    the ARI number is common for IBS and IP-DECT" (p119，实验口径)
    "LED RED • Step 1: Network initialization … LED ORANGE: • Step 4: Software download … LED
    Green: Base station is alive, LED blinked 1s On/1s Off" (p120)
    "Enter the handset PIN if prompted (0000 by default). Then enter the AC code … 0000 (default)" (p462)
  summary: |
    数值：ARI 为 11 位八进制（IBS 与 IP-DECT 共用、唯一值取自 eBuy；实验口径 POD1-6 =
    11000436010/…20/…30/…40/…50/…60）；xBS 启动 LED 六步：红闪三步（网络初始化/IP 获取/配置文件）
    →橙闪三步（软件下载/呼叫服务器链路/基站配置）→绿 1s 亮 1s 灭=存活；GAP 注册 PIN 默认 0000；
    8328 侧话机注册 AC 码默认 0000（Web Admin 可见可改）；8214 搜基站快捷键 menu+*47*；8328 Web
    Admin 默认 admin/admin、SIP 注册周期 3600s、Sipping 19=Disabled、主叫 ID 源优先级
    ALERT_INFO–PAI–FROM；8214 分机需 OMC 侧旗标 no_pack_support_for_siphone=true（p460）；OXO 内
    部计划的语音服务器拨入号 67（p464）。
  conditions: 课堂实验口径（需物理硬件）；生产 ARI 从 eBuy 获取
  tags: [metric, dect, ari, led]

- id: p27
  title: 实验环境账号命名规则——cCpP/Superuser-P*/PasswordP*
  type: metric
  source_pages: p345, p352, p356
  source_chapter: Connect an OXO to Rainbow / Rainbow accounts configuration
  source_quote: |
    "Login : cCpP.admin@ale-training.com (C : class number, P : pod number) • Password: Superuser-P*
    (P : pod number)" (p345)
    "Login : cCpP.user1@ale-training.com … Password: Superuser-P*" (p354-355)
    "Mail server: https://mail44.lwspanel.com/ … Username: e-mail address-> cCpP.user1@ale-training.com
    … Password : PasswordP* (P : pod number)" (p356)
  summary: |
    实验口径账号体系：Rainbow 客户管理员=cCpP.admin@ale-training.com（C=班号、P=POD 号）、密码
    Superuser-P*；成员 user1 同构；培训邮箱服务器 https://mail44.lwspanel.com/、用户名=邮箱、密码
    PasswordP*。配套约定：公司按 private 可见性管理、成员 Visibility 保持 same as company、订阅
    Enterprise。分机映射：课堂 admin=100/user1=101、虚课 admin=104（IPDSP）/user1=Anydevice 133。
  conditions: 仅 RLAB 培训环境；生产账户按客户命名与密码策略
  tags: [metric, lab, accounts, rainbow]

- id: p28
  title: 出局判定流程——从话机到中继的三问
  type: principle
  source_pages: p271-273
  source_chapter: Outgoing calls process / Trunk group traffic sharing matrix
  source_quote: |
    "Traffic sharing link category The set is either allowed (authorized) or not allowed (forbidden)
    to seize a trunk group • Barring link category If allowed to seize a trunk group, the number
    dialed is either allowed (authorized) or not (forbidden) Barring level" (p271)
    "« + »: Access from an extension set to a trunk group is authorized « Blank »: Access from an
    extension set to a trunk group is prohibited" (p273)
  summary: |
    出局三问：①该话机能否占用该中继组？（Traffic sharing：用户 LC × 中继组 LC 查矩阵，+/空）②占用
    后拨的号是否放行？（Barring：用户 Barring LC 经矩阵定位闭锁表→查前缀表与 digit counter）③走
    哪条出局路由？（中继组 0 主组/副中继组 #、ARS 表）。PowerCPU EE 默认把 T0 的 2 个 B 通道或 T2
    的 1 个 B 通道自动收进主中继组 0（p272）。集体缩位目录也受闭锁约束（p280）。
  conditions: 每层独立判定；排障时逐层检查
  tags: [principle, outgoing, barring, routing]

- id: p29
  title: FTR/安装参数实验口径表
  type: metric
  source_pages: p61-62, p447
  source_chapter: OCE Start-up & FTR / Initial installation wizard
  source_quote: |
    "IP address of the IP Box (ETH0): 192.168.1.246 • Subnet mask: 255.255.255.0 • Gateway address:
    192.168.1.254 • Proxy server address: 192.168.1.254 port 3128 • DNS server address: 192.168.1.250
    • Partner fleet reference = OXOP … Partner sub-fleet reference = TRAINING • Installation
    reference = LAB" (p61，实验口径)
    "Installation number: 0210141100 • IP address of the CPU: 192.168.1.246 • Numbering plan type:
    3 digits national numbering plan … Internal Numbers 100 DDI number 41100 … Main trunk group with
    2 B channels • Language: English" (p447，实验口径)
  summary: |
    FTR 实验值：ETH0 .246/24、网关 .254、代理 .254:3128、DNS .250、Fleet=OXOP、Sub-fleet=TRAINING、
    Installation=LAB。话机安装向导实验值：安装号 0210141100、CPU IP .246、三位计划、100↔41100、
    101↔41101、主中继组 2 B 通道、英语。两表都是"生产替换"模板——结构保留、值替换。
  conditions: 全部实验口径；向导要求系统处于默认配置（首启或冷复位后）
  tags: [metric, ftr, wizard, lab-values]

- id: p30
  title: 多 DDI 段发送规则——DDIonPRI 按中继线选段
  type: rule
  source_pages: p279
  source_chapter: Multiple DDI number
  source_quote: |
    "If there are multiple DDI ranges available for a subscriber and multiple trunk lines in an OXO:
    • the first DDI of the subscriber is always sent to the external party Modified behavior • It is
    possible to configure the DDI range to be used according to the trunk line used. … This new
    behavior is controlled with a newly introduced noteworthy address DDIonPRI • This behavior is
    applicable for all types of trunks like T0, T2, Analog and VoIP trunk" (p279)
  summary: |
    规则：旧行为=用户配多段 DDI 且系统多条中继线时，外呼总发第一段 DDI；新行为=按所用中继线配置发
    哪段 DDI（Public numbering plan 里显示中继线标识、勾选关联），受控于 noteworthy 地址 DDIonPRI，
    适用于 T0/T2/模拟/VoIP 全部中继类型。例：N002 关联 DDI 段 5800-5890，用户 100 从第二条 T0 呼出
    送 5800。
  conditions: 需启用 noteworthy 地址 DDIonPRI
  tags: [rule, ddi, trunk, noteworthy]

- id: p31
  title: 呼出限制业务口径（数据采集样例）
  type: rule
  source_pages: p49
  source_chapter: Data collection Settings – Outgoing calls
  source_quote: |
    "Outgoing calls • Users can dial 9 to exit • 1 user will not be authorized • International calls
    and special numbers will not be allowed • Some subscribers will have to go through the
    Attendant to access the external line" (p49)
  summary: |
    样例口径：拨 9 出局（话务台号）；1 个用户无外呼权；国际与特服号禁止；部分用户须经话务台转接才能
    出局。这是 c16 闭锁实验的业务输入，也是生产闭锁方案的最小模板（主中继组时段+副中继组#+闭锁表
    三件套）。
  conditions: 实验业务口径；生产按客户需求裁剪
  tags: [rule, outgoing, barring, sample]

- id: p32
  title: Hotel 模式进入约束——初始安装向导是唯一入口
  type: rule
  source_pages: p72, p447
  source_chapter: OMC installation wizard / Initial installation wizard
  source_quote: |
    "The OMC installation wizard allows to choose between Business or Hotel at the very first
    installation (and after a cold reset)" (p72)
    "Note: the Initial Installation Wizard is the one and only way to put an OXO a Hotel mode" (p447)
  summary: |
    规则：Business/Hotel 模式只能在安装向导中选择，且安装向导仅在系统初始状态（首启或冷复位后）可
    跑——因此酒店项目一旦配完再想切 Hotel 必须冷复位重来。Hotel 版预置（p91）：电话亭=第 1 块 SLI
    板第 2 设备、管理话机=全部数字话机、房间=除传真与电话亭外的全部模拟设备；Guest 信箱受限界面
    （p186）。
  conditions: 规划酒店项目时必须先定模式再配业务
  tags: [rule, hotel, wizard, planning]
```

### 任务覆盖自检（task↔id 映射）
- task-01→p01/p02/p31；task-02→p29（FTR 参数）；task-03→p02/p03/p07；task-04→（c03）；task-05→（c04）；task-06→p26；task-07→p11；task-08→（c07-c10）；task-09→p08/p09；task-10→p10；task-11→p05/p28/p19；task-12→p12；task-13→p13；task-14→p14/p15/p30；task-15→p16；task-16→（f33）；task-17→p17；task-18→p18/p03/p02；task-19→p19/p27；task-20→p27；task-21→p20/p21/p22；task-22→p23；task-23→p24/p25；task-24→p32/p29。24 个 task 全覆盖，无遗漏。
