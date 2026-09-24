# 反例/限制/边界/易错点候选 — Rainbow Hub (RAINXTE101EN Sprint 170 Ed16)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: 纯云不等于"零前提"——网络要求（端口/带宽/防火墙）全书外置，只给文章指针
  type: out-of-scope
  source_pages: p37-41, p90, p136
  source_chapter: Network prerequisites / Cloud PBX prerequisites / Devices network requirements
  source_quote: |
    p37: "Find all the network requirements on the Rainbow support site • Use the following URL to get all
    the information and updates needed to implement Rainbow Hybrid and Rainbow Hub https://help.
    openrainbow.com/hc/en-us/articles/23942019777170-Check-Rainbow-Network-Requirements"
    p41: "This document details: ... Bandwidth requirements • Configuration of corporate network elements
    DNS, Proxy, Firewall..."
  summary: |
    端口/协议全集、带宽要求、Rainbow 域名与 IP 清单、企业网 DNS/代理/防火墙配置全部在支持文章与两份 PDF 里
    （通用版+健康数据托管版），书内只有链接、变更注与三份局部摘录（Cloud PBX 带宽四行表 p90、设备端口表
    p136）。交付前必须按该文章全文核查并用 Rainbow Pilot 做连通性评估；教材不承担网络前提展开。
  conditions: 任何站点上线前
  tags: [out-of-scope, network]

- id: n02
  title: Rainbow Pilot 部分测试分区在教材截图里标注 To come
  type: limitation
  source_pages: p44
  source_chapter: Network prerequisites – Rainbow Pilot
  source_quote: |
    "SEVERAL TEST SECTIONS ARE AVAILABLE ... To come ... To come"
  summary: |
    Pilot 的部分测试分区在 Ed16 截图里显示 "To come"，说明工具分区随平台演进。做站点评估时以工具当时的
    实际分区为准，不能照搬教材截图的分区清单下结论。
  conditions: 使用 pilot.openrainbow.com 评估站点时
  tags: [limitation, tool, network]

- id: n03
  title: 一个用户不能同时属于两家公司；建司前必须查重
  type: limitation
  source_pages: p48
  source_chapter: Rainbow Hub companies
  source_quote: |
    "Before you start a company: • Check that the target company does not exist in Rainbow. To avoid
    possible duplicates, enter the name of the future company in the search bar • A user cannot be part
    of 2 different companies"
  summary: |
    账号以邮箱为身份，一人不能同时在两家公司；建司前先搜索查重。给已有 Rainbow 账号的用户开新公司前，
    先确认其在原公司的归属，否则操作会卡在"人已在别家"。
  conditions: 创建公司、吸收已有 Rainbow 用户时
  tags: [limitation, company, members]

- id: n04
  title: BP 独占四项（PBX 声明/付费订阅/终端声明/电话线），EC 管理员做不了
  type: limitation
  source_pages: p49, p58-59
  source_chapter: Rainbow Hub companies / Administrator roles
  source_quote: |
    "the following actions can only be performed by the BP: • Declaration & activation of a Cloud PBX (or
    traditional PBX) • Opening of paid subscriptions • Declaration of terminals (Deskphones or DECT) •
    Addition or portability of telephone lines."
    p58: "Some elements can only be created by the Reseller's administrator: • The company • Subscriptions
    • Cloud PBX • Public numbers (DID) • Extensions"
  summary: |
    客户管理员不能声明 Cloud PBX、不能开付费订阅、不能声明终端、不能加装/携转电话线（p58 从可创建元素
    角度再加：公司、公网号 DID、分机）。现场客户管理员"点不出"这些入口是权限体系设计而非故障，要找 BP
    账户操作。EC 公司有且只能挂一个 BP，集成伙伴必须是 DR 或 IR。
  conditions: EC 管理员账户操作
  tags: [limitation, bp, licensing, company]

- id: n05
  title: ISOLATED 可见性不推荐（外部 bubble 邀请失效）；Hub 场景官方力荐 CLOSED
  type: warning
  source_pages: p53
  source_chapter: Rainbow Hub companies – Privacy & visibility
  source_quote: |
    "This 'isolated' mode is not recommended as it is very restrictive. ... In particular, your users will
    no longer be able to be invited to conferences (bubbles) external to your organization."
    "This mode is highly recommended, especially in a Rainbow Hub setting. When performing directory
    searches, users will appreciate finding only their colleagues and entries in their Business Directory,
    and not the entire Rainbow community."
  summary: |
    ISOLATED 让公司用户对外完全不可见不可邀，直接后果是无法被外部组织拉进 bubble 会议——不推荐。Hub 语境
    新增 CLOSED 的力荐理由：目录搜索只见同事与企业目录，不会搜出整个 Rainbow 社区。拿不准就建司即设
    CLOSED（可见性可在 company settings 改）。
  conditions: 创建或调整公司可见性时
  tags: [warning, company, visibility]

- id: n06
  title: 服务级别硬门槛——SSO 需 Enterprise、AAD 导入需 Voice Enterprise、频道创建需 Enterprise
  type: limitation
  source_pages: p54, p62, p167
  source_chapter: SSO & authentication / Information channels / Members creation
  source_quote: |
    p54: "The administrator must have an 'Enterprise' service level"
    p62: "Only users with an 'Enterprise' service level can create Information Channels."
    p167: "Import via Azure Active Directory is reserved for administrators with 'Voice Enterprise'
    service level"
  summary: |
    三处硬门槛：配置 SSO 的管理员须 Enterprise 级；信息频道仅 Enterprise 级可创建；AAD 批量导入/同步只对
    Voice Enterprise 级管理员开放。列表外的认证方式（SAML V2: Shibboleth/RSA；OIDC: LemonLDAP/OKTA/
    CAS APEREO/Ping Identity）须经 ALE 确认（p54 NB）。操作前先核操作者订阅级别，别让低级别管理员白折腾。
  conditions: SSO/频道创建/AAD 导入操作前
  tags: [limitation, licensing, sso, azure-ad, channel]

- id: n07
  title: 强制订阅的公司频道成员无法退订
  type: limitation
  source_pages: p62
  source_chapter: Administrator roles – Information channels
  source_quote: |
    "The members you choose in your company will automatically be subscribed to these channels. Members
    will not be able to unsubscribe." / "All Rainbow members in your company will automatically subscribe
    to these channels. Members will not be able to unsubscribe."
  summary: |
    信息频道一旦把成员设为自动订阅（指定成员或公司全员两种范围），成员端不能自行退订。给全员推频道前先
    确认内容会长期维护，否则频道会变成退不出去的骚扰源。
  conditions: 创建公司级信息频道并选择强制订阅范围时
  tags: [limitation, channel]

- id: n08
  title: 培训环境禁用预付订阅（三处警告）
  type: warning
  source_pages: p17, p68, p74
  source_chapter: Training lab / Subscriptions / How-To company
  source_quote: |
    p17: "Use ONLY 4 Voice Entreprise MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID !!!"
    p68: "During LAB Use ONLY Voice MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID!!!"
    p74: "Assign 4 'Voice Enterprise MONTHLY' subscriptions ... DO NOT USE 'YEAR PREPAID' SUBSCRIPTIONS"
  summary: |
    培训/实验环境只允许月付订阅（Voice 与 Attendant 实验同样，p285 "Use monthly for this lab"），禁止
    1/3/5 年预付，否则实验许可无法按预期调整回收。这是培训场景规则，生产环境预付是正常计费方式（p65）；
    把实验习惯带进生产、或把生产做法带进实验，都会踩坑。
  conditions: RLAB/虚拟课堂实验环境
  tags: [warning, training, licensing, subscription]

- id: n09
  title: 公司时区强制——留言信箱与欢迎服务日历都基于它
  type: warning
  source_pages: p73, p255
  source_chapter: How-To company – Company information / Calendars
  source_quote: |
    p73: "Warning It is MANDATORY to define the time zone of the company because the voicemail and the
    calendars of the welcome services are based on it."
    p255: "The calendar refers to the company's time zone"
  summary: |
    公司时区是强制项：留言时间戳、日历开闭时段全按它算。漏配或配错的后果是留言时间错乱、欢迎服务按时区
    误开误闭——客服"半夜也播欢迎词"类工单先查公司时区。公司信息可由该公司管理员事后补全（p73 Tips），
    但时区错配的存量影响要先纠正。
  conditions: 建司与多站点客户
  tags: [warning, company, timezone, calendar]

- id: n10
  title: 无 Voice 订阅则建不了 Cloud PBX（界面只见传统 PBX 类型）
  type: limitation
  source_pages: p75, p80
  source_chapter: How-To company / Cloud PBX steps
  source_quote: |
    p75: "Warning IN ORDER TO BE ABLE TO DECLARE A CLOUD PBX FOR THE COMPANY, AT LEAST ONE VOICE
    SUBSCRIPTION IS REQUIRED (VOICE BUSINESS OR VOICE ENTERPRISE)."
    p80: "you need at least a 'Voice' license. Without this, you'll only see traditional PBXs: OXO
    Connect, OmniPCX Enterprise, Third party PBX, etc."
  summary: |
    声明 Cloud PBX 前公司必须至少有一条 Voice Business 或 Voice Enterprise 订阅；否则建通信服务器时根本
    选不到 Cloud PBX 类型，只出现传统 PBX。开户顺序（订阅→PBX）不能倒；"选不到 Cloud PBX"先查订阅池。
  conditions: BP 开户流程
  tags: [limitation, cloud-pbx, subscription]

- id: n11
  title: Cloud PBX 一二一约束——一公司一个、一 PBX 一条 trunk；多站点也不开第二台
  type: limitation
  source_pages: p78, p92, p100-101
  source_chapter: Cloud PBX / Multi-sites / How-To
  source_quote: |
    p78: "One Rainbow company = one and only one CloudPBX. One CloudPBX = one and only one external SIP
    trunk (SIP provider)."
    p92: "Note: here there is only one Rainbow company, and therefore only one Cloud PBX."
    p101: "Only one trunk group can be associated to the Cloud PBX."
  summary: |
    三条硬约束：一公司一 Cloud PBX；一 Cloud PBX 一条外部 SIP trunk（一个运营商）；多站点仍是一台。客户
    提出"每个站点一台 PBX/每地一条中继"的诉求时要当场纠正预期——用站点逻辑分区（f30）实现，PBX 数量不随
    站点走。
  conditions: 架构设计与需求沟通
  tags: [limitation, cloud-pbx, sip-trunk, multi-site]

- id: n12
  title: "免前缀拨叫"与"优化拨叫"是国家相关特性，需与 ALE 确认
  type: limitation
  source_pages: p81
  source_chapter: Cloud PBX – Creation
  source_quote: |
    "Once your Cloud PBX has been created, you'll be able to eliminate the need for outgoing prefix on
    telephone extensions (deskphones & DECT). ... This feature is country dependent, please check with
    ALE"
  summary: |
    Cloud PBX 建好后可让话机/DECT 免拨出局前缀（Optimized phone dialing），但该特性按国家生效——承诺客户
    "话机上不用拨 0"前先与 ALE 确认所在国支持情况，别把演示环境行为当成生产承诺。
  conditions: 话机拨号体验设计
  tags: [limitation, numbering, dialing]

- id: n13
  title: 公共号码必须由集成伙伴分配注入；首个注入号码默认成为公司主号
  type: limitation
  source_pages: p83, p104
  source_chapter: Cloud PBX – Public numbers
  source_quote: |
    p83: "The public numbers shown here must be assigned by the integrating partner. The 1st number you
    inject is, by default, the main number of the installation. You can change it if necessary."
    p104: "By default, the first number (or first number of the first range) will be affected as the main
    public number for the company."
  summary: |
    两条易错点：号码注入是集成伙伴（BP）的活，客户管理员拿不到入口是正常设计；第一段第一个号默认当公司
    主号——如果先注的不是想要的主号，要么手工改，要么在后续建号段时用"自动改主号"选项。主号错认会直接
    影响外呼主叫 ID（Caller ID policy=Company phone number 的用户全显示它）。
  conditions: 号码分配与外呼主叫规划
  tags: [limitation, did, caller-id]

- id: n14
  title: PSTN 服务不在 ALE 手里——话务由 BP/运营商承载，商务模式分 bundled/separated
  type: limitation
  source_pages: p88, p318
  source_chapter: Cloud PBX – Trunk SIP / Analytics CDR
  source_quote: |
    p88: "Rainbow Hub offer is built jointly with a Business Partner/Traffic provider who is in charge to
    provide the voice traffic and manage the customer. PSTN service is not ordered nor managed by ALE
    Rainbow team."
    p318: "ALE doesn't calculate the cost or invoice the public telephonic consumption. • This is ensured
    by the Business Partner providing the SIP trunk connectivity to the public network"
  summary: |
    客户话费、PSTN 计量、话务故障的一线责任都在 BP/运营商：ALE 不订购不管理 PSTN，也不计费开票（只出
    CDR）。给客户报故障时先分清"云侧问题找 ALE、话务/计费问题找 BP/运营商"；报价时确认 bundled（一单一
    票）还是 separated（两单两票）。
  conditions: 商务谈判与故障分级
  tags: [limitation, pstn, business-model, support]

- id: n15
  title: 多站点约束：一公司一 Cloud PBX；每站内线分段只是建议不是机制
  type: limitation
  source_pages: p92
  source_chapter: Cloud PBX – Multi-sites management 1/2
  source_quote: |
    "Note: here there is only one Rainbow company, and therefore only one Cloud PBX. Having an internal
    number range for each site makes it easier to find your way around the Rainbow administration, but
    it's not mandatory."
  summary: |
    多站点只是单 PBX 下的逻辑分区：站点不隔离内线、不隔离 trunk。每站内线号段分段（如 1xx/2xx/3xx）只是
    便于管理的建议做法，系统不强制——规划时不分段也能跑，但目录与话务可读性会差。别把"站点"理解成"分
    PBX"或"分权限域"。
  conditions: 多站点方案宣讲
  tags: [limitation, multi-site, numbering]

- id: n16
  title: 副站点用户的主叫改写权限要显式收紧（默认可改）
  type: warning
  source_pages: p93
  source_chapter: Cloud PBX – Multi-sites management 2/2
  source_quote: |
    "Here you determine whether the user will be authorized to modify his outgoing number. Select whether
    the user will be able to present the company number (set to 'Not allowed' for users outside the main
    site)."
  summary: |
    Telephony 页签里"允许用户改自己外呼号码"与"允许呈现公司号"两项，对主站点之外的成员建议显式设
    Not allowed——否则副站点成员可把主叫改成任一公司 DDI，主叫身份管理会失控。默认行为是可改，别漏配。
  conditions: 多站点用户电话设置
  tags: [warning, multi-site, caller-id]

- id: n17
  title: 第三方话机参数站说明不保证适用 Hub 语境
  type: warning
  source_pages: p107
  source_chapter: Devices range – ALE devices range
  source_quote: |
    "General information on Myriad jobs can be found here: http://aledevice.com/site/halo_Myriad/23
    Please note: the descriptions on this site are generic and do not necessarily apply to the Rainbow Hub
    context."
  summary: |
    书内引用的 Myriad 产品说明外链是通用资料，官方明说"不一定适用于 Rainbow Hub 语境"。向客户引用话机
    功能参数时以 Features List 与 Hub 官方目录为准，别拿通用页面的功能清单当承诺。
  conditions: 话机选型与投标
  tags: [warning, devices, documentation]

- id: n18
  title: Generic SIP 六大功能缺失——无集中配置/无固件自动更新/无 RCC/无统一在场/不能从应用控话机/键状态冲突
  type: limitation
  source_pages: p117, p120
  source_chapter: Generic SIP devices – Integration principles & Important note
  source_quote: |
    p117: "No centralized configuration • Must be configured manually • No automatic firmware updates •
    No remote call control (RCC) • Basic SIP telephony services"
    p120: "Common limitations include: • CLI issues ... • No unified presence: telephony status of these
    devices is not reflected on Rainbow clients • No call control from Rainbow applications: calls cannot
    be made from the computer with audio on the phone; only computer mode is available • Conflict (DND,
    Forward, BLF keys status not consistently managed ...)"
  summary: |
    第三方 SIP 终端在 Hub 里是"二等公民"：全手工配置、固件不自动更、无 RCC（软话机只有 Computer 模式）、
    话机话务状态不回传 Rainbow 在场、DND/呼转/BLF 键状态在本地服务与集中多端服务间不一致、SIP 协议生态
    互操作风险。方案宣讲时逐条讲清，别按 ALE 原生话机体验做承诺。
  conditions: 第三方终端接入评估
  tags: [limitation, generic-sip, rcc, presence]

- id: n19
  title: ALE 官方立场：不支持大规模第三方 SIP 话机部署，且不为该类配置提供支持
  type: warning
  source_pages: p120-121
  source_chapter: Generic SIP devices – Important note & Why ALE recommends native devices
  source_quote: |
    "The intention behind this feature is not to support large-scale deployments of third-party SIP
    DeskPhones. However, it can be used to integrate existing devices when appropriate. ALE cannot provide
    support for such configurations, as the user experience cannot match that of ALE DeskPhones."
    p121: "Third-party SIP devices: Limited integration • Restricted support • Interoperability
    dependency ... Generic SIP devices should remain complementary solutions."
  summary: |
    官方定性：Generic SIP 用于存量设备适度集成（门铃/传真/ATA/DECT base/会议话机），不做大规模桌面话机
    部署，ALE 不为该类配置提供支持（p122：也无官方互操作认证计划，只有参考指南）。项目里把第三方话机
    当主力终端的方案，支持责任会落在集成商自己身上——报价与 SLA 要提前算进去。
  conditions: 终端方案选型与合同边界
  tags: [warning, generic-sip, support, licensing]

- id: n20
  title: 互操作无认证计划，只有参考设备指南——换型号要自己测
  type: out-of-scope
  source_pages: p122
  source_chapter: Generic SIP devices – Supported devices
  source_quote: |
    "Currently, there is no specific program to officially certify the interoperability of these devices
    with Rainbow Hub. However, ALE provides reference guides for devices that have been successfully
    implemented in known deployments. • Yealink CP925 ... • Yealink T3 ... • Snom D385 and D335 ... • Poly
    Edge B30 ... • Poly Trio C60 ... • Grandstream GRP2603P ... • Grandstream DP750 DECT base station with
    DP720 ... • Grandstream HT812"
  summary: |
    Generic SIP 与 Hub 的互操作没有官方认证计划；书内只给 8 款已验证部署的参考配置指南（Yealink/Snom/
    Poly/Grandstream）。上清单外型号＝自行试点＋自行兜底（可把结果反馈 ALE）。选型时优先参考清单内型号。
  conditions: 第三方设备选型
  tags: [out-of-scope, generic-sip, interop]

- id: n21
  title: Zero-Touch 三大破坏源——DHCP option 43/66/67、LAN 内 PBX 的 TFTP 抢先、未分配设备 Config Failed
  type: warning
  source_pages: p136-137
  source_chapter: Devices installation – Network requirements & First installation
  source_quote: |
    p136: "If the device receives a specific management URL in option 43, 66 or 67, Rainbow Hub's 'zero
    touch' mechanism will be broken, as the DHCP option will take precedence. It is recommended to disable
    these options in the DHCP server ... the link distributed by the DHCP server should be:
    https://rdd.openrainbow.com"
    p137: "A Myriad device cannot start up in Cloud mode if a PBX is present on the LAN where the device
    is connected: TFTP will be given priority. A device that is not assigned to a user will not retrieve
    its configuration ('Config Failed' message during initialization)"
  summary: |
    zero-touch 部署前先排雷三处：①DHCP option 43/66/67 会以更高优先级覆盖 zero-touch 指向——必须禁用，
    禁不掉则下发的 URL 必须是 https://rdd.openrainbow.com；②LAN 里有（旧）PBX 在做 TFTP 时设备起不了
    Cloud 模式（TFTP 抢先）；③设备没关联到用户时取不到配置与 Hub 固件，初始化报 Config Failed——报障
    "Config Failed/No Service" 先查 MAC 有没有录、有没有关联成员。
  conditions: 话机/DECT 现场部署
  tags: [warning, zero-touch, dhcp, troubleshooting]

- id: n22
  title: 禁止用设备自带 web 管理页做配置——只有 zero-touch 机制保证正确运行
  type: warning
  source_pages: p137
  source_chapter: Devices installation – First installation (DHCP)
  source_quote: |
    "Unless you have a very specific need (e.g. Static IP), you must never program the device via its own
    web admin (keys, etc.). Proper operation is only guaranteed by the 'zero touch' mechanism."
  summary: |
    话机按键、功能等配置一律经 Rainbow 管理端下发；直接登设备 web 页改配置（除静态 IP 等特殊需求）会破坏
    zero-touch 的一致性。现场工程师"顺手在话机网页上改个键"是高频坏习惯，要在交付规范里明令禁止。
  conditions: 话机配置变更
  tags: [warning, zero-touch, devices]

- id: n23
  title: 静态 IP 首装坑——出厂密码 123456；已配过 Hub 的设备要先恢复出厂才能进高级设置
  type: version-trap
  source_pages: p138
  source_chapter: Devices installation – First installation without DHCP
  source_quote: |
    "Enter in Menu, and «Advanced settings», «Network», «IP Config», «IPv4 settings». Factory password:
    123456. Same process if web admin : admin/123456 ... In the special case of a device already
    configured for Rainbow Hub: to access advanced settings and enter a Static IP, you need to perform a
    factory reset on the device (long press on the conf key)"
  summary: |
    静态 IP/特定 VLAN 部署两条：进 Advanced settings 的出厂密码是 123456（web 页 admin/123456）——现场
    必须改掉，默认口令是安全暴露面；设备已在 Hub 上配置过时，长按 conf 键恢复出厂才能重新进高级设置设
    静态 IP。固件升级线（出厂版本→Hub 版本）见 p137。
  conditions: 静态 IP/特定 VLAN 场景
  tags: [version-trap, devices, security, static-ip]

- id: n24
  title: 已注册话机禁止直连——日志要开 debug 会话（≤15 分钟、一次性 TOTP 口令）
  type: limitation
  source_pages: p142, p335-336
  source_chapter: Devices maintenance / Maintenance
  source_quote: |
    p142: "Once a Myriad device is registered and active in the Rainbow Hub environment, it is impossible
    to connect to it, even if you know its IP address (for obvious security reasons). • As an
    administrator, you can activate a debug session, for a maximum duration of 15 minutes. ... The login
    is always 'admin', but the password is one-time use only (TOTP)."
    p336: "Note: If the debugging session cannot be opened and the administrator password is not known, a
    SR must be opened on the Rainbow support."
  summary: |
    安全模型：注册激活后的话机即使知道 IP 也连不上；取日志必须由管理员开 debug 会话（最长 15 分钟，登录名
    admin、密码一次性 TOTP），再登 https://<Phone_IP_Address> 用 Maintenance 区（改日志级别免重启、tcpdump、
    恢复出厂）。debug 开不了且不知管理密码时只能开 SR 走官方支持。排障时间窗要按 15 分钟规划。
  conditions: 话机日志采集与远程排障
  tags: [limitation, maintenance, logs, security]

- id: n25
  title: debug 结束必须把日志级别调回 Error——否则设备行为异常带延迟
  type: warning
  source_pages: p143
  source_chapter: Devices maintenance – Get phone logs from the phone itself
  source_quote: |
    "Restore default log level (« Error »), and press the Save button, (if the logging level remains in
    debug mode, the device may behave incorrectly with certain latencies)."
  summary: |
    用话机本地取日志（Debug 级+pcap 抓包）后，必须把 Log Level 恢复成 Error 并 Save。留在 debug 模式会导致
    话机行为异常且带延迟——排障结束时话机"变卡"的工单先查日志级别有没有复原。
  conditions: 话机本地日志采集后
  tags: [warning, maintenance, logs]

- id: n26
  title: webadmin 设备日志两前提：固件 ≥2.14.22；开启后 24 小时自动失效
  type: version-trap
  source_pages: p144
  source_chapter: Devices maintenance – Get phone logs from the webadmin
  source_quote: |
    "Edit the device — Enable device logs (Auto deactivation after 24h) — Click on Get the device report
    to publish the device logs. Report available in the BP report admin section. require at least the the
    following firmware on the device: 2.14.22"
  summary: |
    管理端远程取设备日志的路径（编辑设备→启用设备日志→Get the device report→报告进 BP report admin 区）
    有两个前提：设备固件至少 2.14.22（版本不足先升级）；日志开关 24 小时后自动失效——长周期问题要在失效
    前重新开启。原文 "the the" 为笔误照录。
  conditions: 管理端日志采集
  tags: [version-trap, maintenance, logs, firmware]

- id: n27
  title: 手工模式先装的 DECT 基站不会转 zero-touch；同一站点部署方法要统一
  type: limitation
  source_pages: p151
  source_chapter: DECT mobility – Managing SIP-DECT infrastructure 1/2
  source_quote: |
    "Any base station installed using the manual mode prior to 'zero touch' (base station in web admin,
    terminal declaration as 'Generic SIP') is not converted to 'zero touch' mode. You must use the same
    method for each of your customers' sites. It is possible for the same customer to have one site with
    base stations deployed manually, and another deployed with the 'zero touch' mode."
  summary: |
    先用手工模式（web admin + 按 Generic SIP 声明）装的基站不会自动迁移到 zero-touch 管理。同一客户允许
    A 站手工、B 站零接触，但同一站点内方法要统一——混装会让后续维护（固件、远端重启、状态）出现两套
    口径。此外 8368 必须录主站 IP，副站靠它找主站（p151）。
  conditions: DECT 基站部署模式选择
  tags: [limitation, dect, zero-touch]

- id: n28
  title: DECT 手持机注册必须按精确型号（8214/8262）而非 Generic SIP；且用户不能已有物理终端
  type: misconception
  source_pages: p152
  source_chapter: DECT mobility – Managing SIP-DECT infrastructure 2/2
  source_quote: |
    "Register a new '8214 DECT Handset' or '8262 DECT Handset' with its IPEI number • Associate it with an
    existing user who does not already have a physical terminal ... Unlike the previous manual mode, the
    terminal is declared with its precise type, and not as 'Generic SIP'."
  summary: |
    两个易错点：zero-touch 手持机要按精确型号（8214/8262）+IPEI 注册，不能按 Generic SIP 声明（那是手工
    旧法的做法）；只能关联到"尚无物理终端"的用户——每用户一台物理 SIP 设备的红线（p134）同样约束 DECT
    手持机，用户已有话机时 second handset 挂不上去。
  conditions: DECT 手持机注册与用户绑定
  tags: [misconception, dect, zero-touch, ipei]

- id: n29
  title: 成员邮箱 10 天宽限期内不可复用——建户报错先查最近删除
  type: limitation
  source_pages: p168, p176
  source_chapter: Members – Manual creation / Members deletion
  source_quote: |
    p168: "If you get an error message about the e-mail address you wish to use, please check that it is
    not already the identifier of a user deleted less than 10 days ago (grace period)."
    p176: "When you delete a user, his or her status becomes 'Suspended' for a period of 10 days (called
    the 'grace period'). ... If you restore it, it will default to 'Essential' (free) mode, so you'll need
    to reallocate the appropriate license ... It will also be necessary to reassign the user's telephone
    line."
  summary: |
    删除成员后 10 天宽限期的三重副作用：期间该邮箱 ID 不能复用（新建同名账号报错）；误删恢复后订阅已被
    回收、账号回落 Essential 免费档，要重新分订阅、重挂电话线；不动作 10 天后自动永久删。批量人员调整时
    把这三条算进工单时序，别按"删了马上重建"规划。
  conditions: 删除/恢复成员、复用邮箱建新户
  tags: [limitation, members, lifecycle, licensing]

- id: n30
  title: 管理员改密码立即踢出该用户所有在线会话
  type: warning
  source_pages: p177
  source_chapter: Members – Security: password & login
  source_quote: |
    "If the user is logged in at the time you make the password change, he/she will be logged out
    immediately. This is very useful if you suspect that a Rainbow account is being spoofed."
  summary: |
    Security 页改密的瞬间，该用户在线会话立即全部登出。怀疑盗号时这是特性（踢掉冒用者）；日常批量改密要
    避开工作时间并提前告知，否则用户会当成掉线故障报上来。密码复杂度（≥12 位、1 大写/1 数字/1 特殊字符）
    同样约束所有设密场景（p54/p168/p169）。
  conditions: 成员 Security 页改密
  tags: [warning, members, security]

- id: n31
  title: 邀请建的成员"接受邀请前"不在成员列表里
  type: limitation
  source_pages: p191
  source_chapter: How-To members – New member by invitation
  source_quote: |
    "Warning THE USER WILL APPEAR IN THE MEMBER LIST ONLY IF HE CREATES HIS ACCOUNT. AND THE
    ADMINISTRATOR WILL BE ABLE TO FINALIZE THE CREATION OF THE USER ACCOUNT."
  summary: |
    邮件邀请只是发出邀请：用户点链接完成建户后才出现在 Members 列表，管理员才能补配订阅/号码/设备。急着
    当场配好的场景用 Create 直建或批量导入（p191 Tips）。"发了邀请却搜不到人"不是故障，是等用户接受。
  conditions: 邀请法建户
  tags: [limitation, members, invitation]

- id: n32
  title: Rainbow 平台邮件可能被判 SPAM（建户与邀请两处场景）
  type: warning
  source_pages: p192
  source_chapter: How-To members – New member by invitation
  source_quote: |
    "Warning THE EMAIL COMING FROM RAINBOW PLATEFORM COULD BE CONSIDERED AS SPAM"
  summary: |
    建户通知与邀请邮件都可能进垃圾箱。用户说"没收到邮件"先查 SPAM 再重发；实验邮箱还要删旧邮件避免误点
    旧链接。生产环境应提醒客户把 openrainbow.com 发件域加白。原文 "PLATEFORM" 为原文拼写照录。
  conditions: 邮件邀请与 enrollment 流程
  tags: [warning, members, email]

- id: n33
  title: 分配电话号码的硬前提：成员必须已有 Voice 订阅；无话机也可配号（纯软话机用户）
  type: limitation
  source_pages: p194
  source_chapter: How-To members – Telephony settings
  source_quote: |
    "Warning A MEMBER MUST HAVE A VOICE SUBSCRIPTION (VOICE BUSINESS, VOICE ENTERPRISE OR VOICE ATTENDANT)
    TO ASSIGN A PHONE NUMBER. ... A member can have a phone number (internal and public) even if he
    doesn't have a physical deskphone. In this case, the person is a pure softphone user"
  summary: |
    电话页签配号码前先核订阅——没有 Voice 订阅时号码字段配不了（电话服务门槛的成员级体现）。反向澄清：
    配号不要求有物理话机，纯软话机用户（PC/手机 Rainbow 客户端）同样要有号码；"给远程员工只买软话机方案"
    是合法形态，但订阅一档都不能省。
  conditions: 成员电话设置
  tags: [limitation, members, subscription]

- id: n34
  title: 新建功能限制档案时系统会询问是否设为公司默认档案
  type: warning
  source_pages: p201
  source_chapter: How-To members – Profiles configuration
  source_quote: |
    "Warning WHEN VALIDATING A NEW PROFILE, THE SYSTEM WILL ASK IF THIS ONE MUST BECOME THE NEW DEFAULT
    PROFILE FOR THE COMPANY"
  summary: |
    验证新建档案（如 Restricted collaboration）时，系统会问"是否把它设为公司新默认档案"。手快选了 Yes
    会把限制档推给全公司新成员——默认档案变更影响面大，操作时看清弹窗再确认。
  conditions: 成员档案配置
  tags: [warning, members, profiles]

- id: n35
  title: Attendant group 全员须 Voice Attendant 订阅；Manager/Assistant 的 Administrator 功能是"后续提供"
  type: limitation
  source_pages: p209, p249
  source_chapter: Groups overview / Welcome services – Attendant group
  source_quote: |
    p209: "Notes All members must have a Voice Attendant license ... * For this type of group, the
    'Administrator' functions will be proposed later"
    p249: "Members in this group Must Have a Voice Attendant subscription. They will answer company calls
    and supervise members belonging to supervision groups."
  summary: |
    两条许可边界：Attendant group（话务组）内每个接听成员都必须持 Voice Attendant 订阅——把它当"便宜版
    hunt group"用会撞订阅墙；Manager/Assistant 组的 Administrator 管理功能官方标注"后续版本提供"（p209
    * 注），当前版本的该组管理面有限，别在方案里承诺组级管理能力。
  conditions: 话务组/经理助理组设计
  tags: [limitation, attendant, licensing, roadmap]

- id: n36
  title: 退组与组空：可禁最后一名成员退组；非坐席管理员对坐席显示为永久 withdraw
  type: limitation
  source_pages: p212, p214
  source_chapter: Hunt groups – Services / Roles in a group
  source_quote: |
    p212: "Forbid the last member from withdrawing"
    p214: "Note that it is possible to give an « administrator » role to someone who does not take calls,
    only the « agent » role involves receiving group calls. For group members who are « agent », the
    non-agent administrator is seen as being permanently withdrawed."
  summary: |
    两条行为边界：坐席可随时退组（应用或话机键），建组时可勾"禁止最后一名成员退组"防止组空；只授
    Administrator 不授 Agent 的人不接组来电，且在坐席侧显示为"永久已退组"——把主管拉进组当管理员时，
    坐席看到的主管状态不是真实在线状态。原文 "withdrawed/withdrawed" 拼写照录。
  conditions: 组成员与管理员配置
  tags: [limitation, hunt-group, roles]

- id: n37
  title: 组的语音留言与通话记录住在自动生成的 bubble 里
  type: misconception
  source_pages: p217
  source_chapter: Hunt groups – Voice mail
  source_quote: |
    "When a group is created, an exchange bubble is automatically created. It includes all the members of
    the group, in order to allow: ... Management of the group's voice messages • Access to call logs. A
    voice message is automatically transferred to the corresponding bubble as an audio file."
  summary: |
    组语音留言不是"话机留言灯"那套：每组建组时自动配一个协作 bubble，组留言以音频文件自动转入该 bubble，
    组通话记录也在里面，全员权限相同。教客户用组留言时要说"去组 bubble 里听"，别让他们在话机上找。
  conditions: 组留言使用培训
  tags: [misconception, hunt-group, voicemail, bubble]

- id: n38
  title: Manager/Assistant 只筛电话呼叫；经理要筛选来话必须把 DID 配在组级
  type: warning
  source_pages: p219, p221
  source_chapter: Managers/assistants groups – Overview / Settings
  source_quote: |
    p219: "Only telephone calls are filtered. If Rainbow audio calls are allowed, they are not filtered."
    p221: "The DID of the Manager who wants to be able to screen his calls must be assigned to the group
    level, and not to the manager."
  summary: |
    两个配置红线：①筛选范围只覆盖电话呼叫——允许 Rainbow 音视频呼叫时不被助理过滤，经理的 Rainbow 直呼
    会绕过助理；②经理个人 DID 若配在经理个人名下，筛选不生效——必须把该 DID 配到组级。"助理筛不到经理
    电话"的工单先查这两处。
  conditions: 经理助理组配置与排障
  tags: [warning, manager-assistant, did, filtering]

- id: n39
  title: 紧急组激活语义易误读——激活后免前缀紧急呼叫进组不出局；转外线要加前缀（0112）
  type: misconception
  source_pages: p227-228
  source_chapter: Supervision groups – Emergency numbers & Emergency group
  source_quote: |
    p228: "Active group -> Direct calls (without outbound prefix) to emergency numbers are routed to the
    group and not to the outside. To transfer an emergency call to the public emergency number, emergency
    group members must dial the emergency number preceded by the external prefix (e.g. 0112)."
  summary: |
    紧急组不是"紧急呼叫转接服务"：激活后，站内用户免前缀拨紧急号会被接到安保组（组内处置），不直接出公
    网；判定需要真正报警时，组员要手动加出局前缀拨（如 0112）。给客户培训时必须把"进组"与"转警"两条
    路径讲透，漏讲会造成延误报警的重大事故风险。
  conditions: 紧急组启用与安保流程培训
  tags: [misconception, emergency, compliance]

- id: n40
  title: 从 Groups 页签建紧急组时 Emergency 标记默认不勾——忘勾等于建了普通组
  type: warning
  source_pages: p240-241
  source_chapter: How-To emergency – Emergency group creation
  source_quote: |
    "Warning BY DEFAULT, USING WITH WAY, 'EMERGENCY GROUP' IS NOT VALIDATED BY DEFAUT. DON'T FORGET TO DO
    IT."
  summary: |
    紧急组两条创建路：从 Traffic control/Emergency numbers 进（标记默认勾选）；从 Groups 页签进（标记
    默认不勾）。走第二条路忘勾 Emergency group，建出来的就是普通 hunt group——激活后紧急呼叫不会路由进
    它，监管合规直接失效。原文 "BY DEFAUT" 为原文笔误照录。
  conditions: 紧急组创建
  tags: [warning, emergency, configuration]

- id: n41
  title: 紧急定位责任链在书外——BP 登记 DID 地址、运营商判 PSAP，Rainbow 不管
  type: out-of-scope
  source_pages: p229
  source_chapter: Supervision groups – Emergency calls localization
  source_quote: |
    "Rainbow doesn't manage DID location in this model where DIDs are managed by the Business Partner.
    Business Partners have to declare DID addresses into the SIP provider database when purchasing DDIs
    for his Rainbow end customers. Identification of the relevant Public-Safety Answering Point (PSAP) is
    under the responsibility of the SIP provider."
  summary: |
    按国监管要求的紧急呼叫地理定位，在 Hub 架构里由 BP（购号时把 DID 地址登记进 SIP 运营商数据库）与
    运营商（据此路由到正确 PSAP）承担，Rainbow 不管理 DID 位置。多址客户购号时漏登记地址＝紧急呼叫可能
    被派往错误辖区——这是 BP 侧流程义务，项目清单要单列。
  conditions: 号码采购与多站点部署
  tags: [out-of-scope, emergency, psap, bp]

- id: n42
  title: 通话录音存 2 个月且仅最终客户管理员可见；超期归档是付费选件
  type: limitation
  source_pages: p231
  source_chapter: Supervision groups – Call recording
  source_quote: |
    "RECORDINGS ARE STORED FOR 2 MONTHS. The 'Recordings' tab is only accessible by the end-customer
    administrator of the solution, for confidentiality reasons. ... it is possible on request to implement
    'Rainbow Exporter', which copies all recordings daily to Google Drive, or to a customer's own SFTP
    storage server, in addition to traditional Rainbow licenses (pricing on request)."
  summary: |
    三条边界：录音只保留 2 个月，到期即走；Recordings 页签仅最终客户管理员可见——BP/集成商自己看不到客户
    录音（保密设计），别承诺"我们帮客户管录音"；超过 2 个月的法定归档要加购 Rainbow Exporter（按日拷贝
    到 Google Drive/客户 SFTP，pricing on request）。合规需求要在报价阶段锁进合同。
  conditions: 录音合规设计
  tags: [limitation, recording, retention, compliance]

- id: n43
  title: Voice Attendant 用户被锁死在 PC——不能用话机、不能用手机端话务台，激活后话机关联被删
  type: warning
  source_pages: p246
  source_chapter: Welcome services – Attendant console
  source_quote: |
    "Warning: Members with voice attendant subscriptions cannot use: • Attendant mode on the Rainbow
    mobile application • Their telephone set. If configured: the phone set association is deleted after
    activation of the attendant console."
  summary: |
    话务台方案的终端代价：Voice Attendant 成员不能在手机上用话务台模式，也不能再用话机——已配置的话机
    关联会在话务台激活后被删除。给前台/秘书岗做方案时必须讲清"话务员=纯 PC 工位"；用户拿着话机找"为什么
    不能接电话"时先查是否激活了话务台。
  conditions: 话务台部署与岗位设计
  tags: [warning, attendant-console, devices]

- id: n44
  title: 日历法定假日不预填；日历必须先于欢迎服务创建；强制开闭后下个时段自动回 Auto
  type: warning
  source_pages: p255-256, p259
  source_chapter: Welcome services – Calendars & Welcome service
  source_quote: |
    p256: "Note: Public holidays are not pre-filled. ... Define special days (the schedules of these days
    will have priority over those of the usual days)."
    p259: "The calendar of opening and closing hours must be created before the management of the welcome
    service ... The service that has been closed appears in 'forced' mode. At the next time slot, the mode
    returns to 'Auto'."
  summary: |
    三条日历坑：法定假日系统不预填，要手工录特殊日（时隙优先于常规日）——漏录=假日照常播开站欢迎词；建
    欢迎服务前必须先建好日历；人工强制开/闭是"一次性覆盖"，显示 forced 态，到下个时段自动回 Auto——
    排查"强制闭店第二天自己开了"时先讲这个机制。
  conditions: 欢迎服务日历运维
  tags: [warning, calendar, welcome-services]

- id: n45
  title: 欢迎服务素材三上限：文件 ≤4MB、问候 ≤120 秒、单用途引导 ≤5 条；定制时段提示 ≤5 条/特殊日 ≤10 天
  type: limitation
  source_pages: p260, p263-264
  source_chapter: Welcome services – Custom prompts & Voice prompts
  source_quote: |
    p260: "MAXIMUM : 5 — MAXIMUM : 10"
    p263: "Audio file must not exceed 4MB. greeting file must not exceed 120 seconds"
    p264: "Multiple voice guides can be loaded for a single use (maximum: 5)."
  summary: |
    素材规格硬上限：自定义音频 ≤4MB、问候文件 ≤120 秒；单一用途最多挂 5 条引导；欢迎服务的定制时段提示
    最多 5 条、特殊日最多 10 天。给客户做长文案/多语种欢迎词方案时先对规格——超限的方案要拆文件或改设计。
  conditions: 语音提示制作与导入
  tags: [limitation, voice-prompts, welcome-services]

- id: n46
  title: AA 两种入口语义不同——直挂 DDI 即 7×24；经欢迎服务进则 IVR 不带 DID 受日历控制
  type: misconception
  source_pages: p266
  source_chapter: Welcome services – Automated attendant
  source_quote: |
    "An automated attendant can be reached via a dedicated public number or via a welcome service. •
    Direct call via DDI (in this case, the IVR is in service 24/7) • Access via a welcome service with a
    calendar ... In this case, the IVR does not include a DID, as this is associated with the welcome
    service."
  summary: |
    客户报"半夜 IVR 还在收单"或"IVR 半夜没人接"时先查入口方式：IVR 直挂公网号＝7×24 全天服务；经欢迎
    服务进＝受日历控制、闭时段走闭店路由，且 DID 配在欢迎服务上、IVR 本身无号。两种形态都合法，方案里要
    写清选哪种。
  conditions: IVR 入口设计
  tags: [misconception, ivr, welcome-services]

- id: n47
  title: AA"唯一提示"模式创建后不可改；来话显示默认名而非技术号（保密）
  type: warning
  source_pages: p269-270
  source_chapter: Welcome services – Automated attendant & AA voice prompts
  source_quote: |
    p270: "Menus with single voice prompts ... This option is highly recommended (cannot be changed later)."
    p269: "For confidentiality reasons, on incoming call, a default name is displayed instead of the
    technical number of a Welcome service."
  summary: |
    建 AA 时若选"每菜单唯一提示"模式（官方强烈推荐），事后不能切换成逐选项录音模式——只能重建 IVR。另
    一条视觉规则：来话呈现用默认名替代欢迎服务技术号（保密），客户说"来话显示的名字不对"先解释这是设计
    行为。
  conditions: IVR 创建与来话显示核对
  tags: [warning, ivr, voice-prompts]

- id: n48
  title: 组管理员日历权限的显示条件——仅当组只关联一个欢迎服务+一份日历且组用于开站时段
  type: limitation
  source_pages: p273
  source_chapter: Welcome services – Hunt groups & welcome service calendar
  source_quote: |
    "Hunting group administrators can manage the welcome service calendar when that calendar is dedicated
    to their own group ... To keep the experience clear and relevant, the calendar tab is displayed only
    when a single welcome service and a single calendar are linked to the group, and only when the group
    is used for open hours."
  summary: |
    "组管理员改本组日历"功能有显示前提：该组只挂一个欢迎服务、该服务只挂一份日历、且组用于开站时段——
    多服务/多日历/闭站用途的组管理员看不到日历页签。给门店店长放权改营业时间的方案要按此条件设计，别承诺
    复杂结构下的自助改历。
  conditions: 组管理员权限设计
  tags: [limitation, calendar, hunt-group]

- id: n49
  title: 欢迎服务提示音必须挂对日历
  type: warning
  source_pages: p281
  source_chapter: How-To welcome service – Import of customized voice prompts
  source_quote: |
    "Warning: Associate the voice prompts with the right Calendar!"
  summary: |
    导入开/闭提示音时若过滤器/日历选错，提示音挂到错误服务上——拨测时"新提示音不生效"多半是挂错了日历。
    导入后按 p282 的拨测步骤验证（可临时改公司开闭时段来测）。
  conditions: 提示音导入
  tags: [warning, voice-prompts, welcome-services]

- id: n50
  title: 纯 Rainbow VoIP 呼叫不产生 CDR——话单只覆盖经 Cloud PBX 的呼叫
  type: limitation
  source_pages: p318
  source_chapter: Analytics – Call detail record
  source_quote: |
    "They are generated (.csv) for all calls going through the Cloud PBX • Incoming, outgoing and internal
    calls are taken into account • Pure VoIP Rainbow audio/video call doesn't generate CDR"
  summary: |
    CDR 覆盖经 Cloud PBX 的入/出/内部呼叫；纯 Rainbow 音视频（软话机对软话机）呼叫不出现在话单。用 CDR
    做"全员话务量"统计时会漏掉纯 VoIP 部分——要全量行为数据用分析仪表盘（p319），要计费用话单，两者口径
    不同。
  conditions: 话务统计与计费核对
  tags: [limitation, cdr, analytics]

- id: n51
  title: 成员级组统计可被公司管理员关闭（隐私敏感度），关闭后组管理员无权查看
  type: limitation
  source_pages: p325
  source_chapter: Analytics – Group members level
  source_quote: |
    "For reasons of sensitivity specific to each country and/or customer, a company administrator may
    disable individual statistics for a specific group. When disabled, data is still collected at server
    level, but group administrators have no access to it."
  summary: |
    组内成员级统计（接听数/平均时长）涉及各国劳动监控合规差异：公司管理员可按组关闭；关闭后服务器仍在
    采集，只是组管理员无权看。给客户上"坐席绩效报表"前先过法务/HR，别默认全员开放。
  conditions: 组报表方案设计
  tags: [limitation, analytics, privacy]

- id: n52
  title: ALE SIP 终端不支持经 HTTP 代理穿越——部署排障先查路由器协议
  type: limitation
  source_pages: p334
  source_chapter: Maintenance – Connectivity to the Rainbow network
  source_quote: |
    "Before opening an ALE SR, please check that your Internet router supports the following protocols:
    ... Please note: ALE SIP terminals do not support crossing HTTP proxy currently"
  summary: |
    SIP 话机"注册不上/呼叫建立差/无音频"时，开 SR 前先核对路由器放行协议；特别地，ALE SIP 终端目前不支持
    走 HTTP 代理出网——全代理上网的客户网络要开直通（或按 Network Requirements 调整），否则话机类故障在
    网络层就死了。
  conditions: 话机部署与连通性排障
  tags: [limitation, network, devices, troubleshooting]

- id: n53
  title: Web 端用户问题上报不采集事发日期
  type: limitation
  source_pages: p337
  source_chapter: Maintenance – Problems reported by your users
  source_quote: |
    "In web mode, the date is not requested because the logs in a browser are short-lived."
  summary: |
    用户从 Web 端 "Help and Support / Report a problem" 上报时不填事发日期（浏览器日志存活短）；桌面客户端
    才有日期字段。走 Web 上报的工单定位时间要靠附件截图与描述补齐——重要故障引导用户装客户端上报。集成
    伙伴与客户看到同一份上报（p337），可据此代维。
  conditions: 用户问题上报流程
  tags: [limitation, maintenance, support]

- id: n54
  title: Rainbow Hub 服务请求只为认证 Rainbow Hub 的伙伴创建
  type: limitation
  source_pages: p341
  source_chapter: Maintenance – Access to Rainbow support
  source_quote: |
    "The ESR will only be created if the partner is certified on Rainbow Hub."
  summary: |
    经 MyPortal/邮件/Emily BOT/电话开 Rainbow Hub 服务请求，前提是伙伴持 Rainbow Hub 认证（注意：混合云
    教材口径为"certified on Rainbow"，本书为"certified on Rainbow Hub"——认证科目按产品线区分）。非认证
    伙伴的现场问题要么先补认证，要么经认证的上家转报——支持路径要在项目开始前理顺。
  conditions: 开 Service Request 前
  tags: [limitation, support, certification]

- id: n55
  title: LDAP 连接器的 Exchange 日历在场同步是"161 版前功能的等价回归"
  type: version-trap
  source_pages: p179
  source_chapter: Company members – AD synchronization (LDAP connector)
  source_quote: |
    "Synchronize calendar presence with Exchange Server. This is equivalent to the functionality already
    present prior to version 161, as part of Exchange online (Office 365)."
  summary: |
    LDAP 连接器第三功能（与 Exchange Server 同步日历在场）是对 Rainbow 161 版之前（经由 Exchange online/
    Office 365）已有能力的等价实现。老客户从旧版本迁移时不要按"新功能"宣传；版本 161 前后的在场同步行为
    差异要按官方文档核对。原文 "Connecteur" 为法语残留照录。
  conditions: 在场同步方案迁移与宣传口径
  tags: [version-trap, ldap, presence, exchange]

- id: n56
  title: 实验模拟器不能按公网号呼本公司成员——公网呼叫测试必须用 MicroSIP，且训后须删除
  type: warning
  source_pages: p13, p20
  source_chapter: Training lab – Lab topology & Public calls
  source_quote: |
    p13: "*The public SIP simulator used for training does not allow us to call members of our own company
    by their public number,hence the use of the MicroSIP softphone."
    p20: "At the end of the training, you will have to close and delete the MicroSIPs from your PC in
    order to guarantee the completion of future trainings"
  summary: |
    实验口径双约束：SIP 模拟器不允许按公网号呼叫本公司成员——公网方向测试一律用讲师发的 2 个预配 MicroSIP
    （"Start public users.bat" 启动、按 POD 选账号）；训练结束必须关闭并删除 MicroSIP，否则占用下期培训
    的公网账号。把实验脚本当生产验证口径会得出错误结论。
  conditions: 仅 RLAB/虚拟课堂培训环境
  tags: [warning, lab, microsip]

- id: n57
  title: IVR 无数量与许可限制——与话务台（Voice Attendant 订阅）形成成本对照
  type: misconception
  source_pages: p266, p224
  source_chapter: Welcome services – Automated attendant / Supervision groups
  source_quote: |
    p266: "You can create as many IVRs as you like - there are no limits or licenses on this service"
    p224: "Voice Attendant : Supervision-Pickup-Transfer & 10 Calls in queue"
  summary: |
    客户常把 IVR 与话务台混为一谈：IVR（自动话务员）无限创建且零许可，适合自助分流；话务台（人工接听/
    监督代接）才要 Voice Attendant 订阅。预算沟通时先分流——"能用 IVR 自助的别买话务台"；反过来，承诺
    "免费无限话务台"就是错误报价。
  conditions: 报价与方案分流
  tags: [misconception, ivr, attendant-console, licensing]
```

---

## 收尾自检 — 对照 BOOK_OVERVIEW.md 24 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | 网络前提与 Pilot 评估 | 有 → n01（网络要求书外）、n02（Pilot 分区 To come）、n52（HTTP 代理） |
| task-02 | 公司体系创建 | 有 → n03（一人一司/查重）、n05（ISOLATED/CLOSED）、n06（SSO 门槛）、n09（时区强制） |
| task-03 | 管理员权责、目录/频道 | 有 → n04（BP 专属）、n06（Enterprise 门槛）、n07（频道强制订阅） |
| task-04 | 订阅开通与分配 | 有 → n08（培训禁预付）、n10（Voice 订阅是建 PBX 前提）、n33（配号前提） |
| task-05 | Cloud PBX 声明与配置 | 有 → n10、n11（一二一约束）、n12（免前缀国家相关） |
| task-06 | 号码分配与主叫策略 | 有 → n13（伙伴注入/首号默认主号） |
| task-07 | 流量控制与闭锁 | 概念规则已入 principle p25；本类无新增边界（配置本身低风险） |
| task-08 | trunk 商务与带宽 | 有 → n14（PSTN 不归 ALE、bundled/separated） |
| task-09 | 多站点规划 | 有 → n15（一 PBX/分段非强制）、n16（副站主叫权限收紧） |
| task-10 | 成员管理 | 有 → n29（宽限三重副作用）、n30（改密踢人）、n31（邀请未接受不可见）、n32（SPAM）、n33（配号前提）、n34（默认档案弹窗）、n55（LDAP 版本语义） |
| task-11 | 设备部署 | 有 → n17（参数站不保证适用）、n21（zero-touch 三破坏源）、n22（禁用设备 web 页）、n23（静态 IP 坑） |
| task-12 | 设备维护日志 | 有 → n24（禁直连/15 分钟/TOTP）、n25（恢复日志级别）、n26（2.14.22/24h） |
| task-13 | Generic SIP 接入 | 有 → n18（六缺失）、n19（不支持大规模/不兜底）、n20（无认证计划） |
| task-14 | DECT 部署 | 有 → n27（手工站不转 zero-touch）、n28（精确型号/单物理终端） |
| task-15 | Hunt Group 与队列 | 有 → n36（退组/非坐席管理员）、n37（组留言在 bubble） |
| task-16 | Manager/Assistant | 有 → n38（只筛电话/DID 挂组级）、n35（Administrator 后续提供） |
| task-17 | 话务台与监督组 | 有 → n43（Attendant 锁 PC）、n35（Attendant 组订阅门槛）、n57（IVR vs 话务台成本） |
| task-18 | 紧急号码与紧急组 | 有 → n39（激活语义）、n40（Groups 路默认不勾）、n41（定位责任链） |
| task-19 | 录音与归档 | 有 → n42（2 个月/仅客户管理员/Exporter 付费） |
| task-20 | 欢迎服务全家桶 | 有 → n44（假日不预填/先历后服/forced 回 Auto）、n45（素材上限）、n49（提示音挂对日历） |
| task-21 | IVR 配置 | 有 → n46（两种入口语义）、n47（唯一提示不可改/默认名显示） |
| task-22 | 多站点配置 | 有 → n15、n16、n41（DID 登记） |
| task-23 | 分析体系 | 有 → n50（纯 VoIP 无 CDR）、n51（成员级统计可关） |
| task-24 | 维护支持体系 | 有 → n53（Web 无日期）、n54（Hub 认证门槛）、n52（代理不支持）、n56（模拟器限制） |

**24/24 全部有边界类条目覆盖（task-07 由 principle p25 承接，已在表中说明）。**

### 扫描完整性说明（Warning/Note/Tips/Important 标记框逐页核对）

- 已全部入册的 Warning/Important：p53（ISOLATED）、p73（时区 MANDATORY）、p75（Voice 订阅前提）、p136（DHCP option IMPORTANT）、p137（TFTP/Config Failed/禁 web 配置）、p191（邀请未接受不可见）、p192（SPAM）、p194（配号前提）、p201（默认档案）、p240-241（Emergency 默认不勾）、p246（Attendant 设备限制）、p281（提示音挂对日历）、p120（第三方大规模 IMPORTANT）。
- 已入册的 Note/NB/Tips：p92（一公司一 PBX/分段非强制）、p104（首号默认主号）、p136（故障五类清单，并入 n21）、p151（方法统一/8368 IP）、p170（AAD 不自动供应，并入 n06/n29 关联说明）、p214（非坐席管理员显示）、p266（两种入口）、p269（默认名保密）、p270（唯一提示不可改）、p273（日历页签显示条件）、p318（纯 VoIP 无 CDR）、p325（统计可关）。
- 复核后未单列的纯操作提示（非边界类）：p73 Tips（公司信息可后补）、p158（删几台设备做练习）、p191 Tips（急用走直建）、p235 Tips（编辑组开溢出）、p282 Tips（改时段测提示音）、p269 Tip（从根级看 IVR 树）、p136（绿点注册判据，归 principle p32）。
- 推断性结论已在条目内标注"（推断）"的位置：无——本文件全部条目均有原文直接支撑；n39 的"漏讲造成延误报警风险"为培训提示性表述，非对书内事实的推断。
- 版本号均按原文保留完整位数：TLS 1.2、固件 2.14.22、Rainbow version 161（p179）、Sprint 170 / Edition 16（书名页）。
