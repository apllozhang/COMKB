# 反例/限制/边界/易错点候选 — Rainbow OXO Connect (RAINXTE001EN Ed13)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: 电话服务必须有付费订阅——免费 Essential 无电话且无 SLA
  type: limitation
  source_pages: p33, p65
  source_chapter: Rainbow Overview – Subscription plans / Subscriptions
  source_quote: |
    p33: "Rainbow Essential This free option is available to anyone who wants to try Rainbow for an unlimited period (no SLA)."
    p65: "Each member must have a subscription to use telephony services • Business • Enterprise • Attendant"
  summary: |
    免费版 Essential 只能长期试用协作功能，无 SLA，也不含电话服务；要用话音必须给成员分配 Business/Enterprise/Attendant 之一。
    Conference 是按分钟/连接计费的 pay-as-you-go，Enterprise Conference 则强制按年预付（12 个月）。
    开通时别把"免费可用"理解成"能打电话"，也别漏看两种 Conference 的计费模型差异。
  conditions: 所有电话功能开通场景
  tags: [limitation, licensing, subscription]

- id: n02
  title: 网络要求（端口/带宽/防火墙）全书外置，只给 PDF 指针
  type: out-of-scope
  source_pages: p36-40
  source_chapter: Network Requirements
  source_quote: |
    p36: "Find all network requirements on the Rainbow support site ... 2 PDF files • Rainbow network requirements - Health data hosting • Rainbow network requirements"
    p40: "This document details: ... Bandwidth requirements, Configuration of corporate network elements (DNS, Proxy, Firewall...)"
  summary: |
    端口/协议清单、带宽要求、Rainbow 域名与 IP 清单、企业网络设备（DNS/代理/防火墙）配置全部在《Rainbow Network Requirements》PDF 里，书内只有链接和摘要。
    交付前必须按该 PDF 全文核查，并配合 Rainbow Pilot 工具（pilot.openrainbow.com）做连通性与容量评估；教材不承担网络前提的展开。
  conditions: 任何站点上线前
  tags: [out-of-scope, network]

- id: n03
  title: Rainbow Pilot 部分测试分区在教材截图里标注 To come
  type: limitation
  source_pages: p43
  source_chapter: Network Requirements – Rainbow Pilot
  source_quote: |
    "SEVERAL TEST SECTIONS ARE AVAILABLE ... To come ... To come"
  summary: |
    Rainbow Pilot 的部分测试分区在 Ed13 教材截图里显示 "To come"，说明该工具的分区随平台演进。
    做站点评估时以工具当时的实际分区为准，不能照搬教材截图的分区清单下结论。
  conditions: 使用 pilot.openrainbow.com 评估站点时
  tags: [limitation, tool, network]

- id: n04
  title: 一个用户不能同时属于两家公司，建公司前必须查重
  type: limitation
  source_pages: p47
  source_chapter: Introducing the Companies
  source_quote: |
    "Before you start a company • Check that the target company does not exist in Rainbow. To avoid possible duplicates, enter the name of the future company in the search bar • A user cannot be part of 2 different companies"
  summary: |
    Rainbow 账户以邮箱为身份，一个人不能同时在两家公司；建公司前先在搜索栏查重，避免造出重复公司。
    给已有 Rainbow 账号的用户开新公司前，先确认其在原公司的归属——否则操作会卡在"人已在别家"上。
  conditions: 创建公司、吸收已有 Rainbow 用户时
  tags: [limitation, company, members]

- id: n05
  title: 建 PBX 与开付费订阅是 BP 专属权，EC 管理员做不了
  type: limitation
  source_pages: p48
  source_chapter: Introducing the Companies – 2 types of companies
  source_quote: |
    "However, the following actions can only be performed by the BP: • Declaration & PBX • Opening of paid subscriptions. The customer's integration partner must be either a 'DR' or an 'IR'."
    "To be managed by a BP, an 'EC' company must be attached to the company of this BP (one and only one attachment)."
  summary: |
    客户（EC）管理员不能申报/创建 PBX、不能开通付费订阅，这两件事只能 BP 做；EC 公司有且只能挂靠一个 BP，集成伙伴必须是 DR 或 IR。
    现场如果客户管理员"点不出"建 PBX/开订阅入口，这是权限体系设计而非故障，要找 BP 账户操作。
  conditions: EC 管理员账户操作、公司挂靠与伙伴准入
  tags: [limitation, licensing, company, bp]

- id: n06
  title: ISOLATED 可见性不推荐——用户无法被外部 bubble 邀请
  type: warning
  source_pages: p52
  source_chapter: Introducing the Companies – Privacy & Visibility
  source_quote: |
    "This 'isolated' mode is not recommended as it is very restrictive. Please check the impacts before applying it to your company. In particular, your users will no longer be able to be invited to conferences (bubbles) external to your organization."
    "Get into the habit of systematically setting the 'closed' mode as soon as you create a Rainbow company. This is ideal for the vast majority of customers."
  summary: |
    ISOLATED 让公司用户对外完全不可见且不可被邀请，直接后果是无法被外部组织拉进 bubble 会议。教材明确不推荐。
    拿不准就用 CLOSED（对外不可见但可通过邮箱邀请），建司时默认设 CLOSED 即可；已选 ISOLATED 的要先向客户确认外部协作诉求。
  conditions: 创建或调整公司可见性时
  tags: [warning, company, visibility]

- id: n07
  title: 服务级别硬门槛——SSO 需 Enterprise、AAD 导入需 Voice Enterprise、频道创建需 Enterprise
  type: limitation
  source_pages: p53, p92, p61
  source_chapter: SSO & Authentication / Members Creation / Information Channels
  source_quote: |
    p53: "The administrator must have an 'Enterprise' service level"
    p92: "Import via Azure Active Directory is reserved for administrators with 'Voice Enterprise' service level"
    p61: "Only users with an 'Enterprise' service level can create Information Channels."
  summary: |
    三处硬门槛：配置 SSO 的管理员必须是 Enterprise 级；Azure AD 批量导入/同步只对 Voice Enterprise 级管理员开放；信息频道只有 Enterprise 级用户能创建。
    另两处相关边界：列表之外的认证方式（其他 SAML V2/OIDC 产品）须经 ALE 确认（p53 NB）；Azure AD 与公司的关联是"Manual operation at your own initiative"，要自己动手做（p95）。
    操作前先核查操作者的订阅级别，别让低级别管理员白折腾。
  conditions: SSO/批量导入/频道创建操作前
  tags: [limitation, licensing, sso, azure-ad, channel]

- id: n08
  title: 强制订阅的公司频道成员无法退订
  type: limitation
  source_pages: p61
  source_chapter: Administrators Profiles – Information Channels
  source_quote: |
    "The members you choose in your company will automatically be subscribed to these channels. Members will not be able to unsubscribe."
  summary: |
    公司级信息频道一旦把成员设为自动订阅，成员端不能自行退订。
    给全员推频道前先确认内容会长期维护，否则频道会变成无法退出的骚扰源。
  conditions: 创建公司级信息频道并选择强制订阅范围时
  tags: [limitation, channel]

- id: n09
  title: 培训环境禁用预付订阅（Business 与 Attendant 两处警告）
  type: warning
  source_pages: p66, p176
  source_chapter: Subscriptions / How-To – Attendant console
  source_quote: |
    p66: "During LAB Use ONLY Voice MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID!!!"
    p176: "DON'T USE 'PREPAID' IN THE TRAINING"
  summary: |
    培训/实验环境只允许按月（MONTHLY）订阅，Voice 与 Attendant 两处都明令禁止预付（1/3/5 年 PREPAID），否则实验许可无法按预期调整和回收。
    这是培训场景规则，生产环境预付是正常计费方式；把实验习惯带进生产、或把生产做法带进实验，都会踩坑。
  conditions: RLAB/虚拟课堂实验环境
  tags: [warning, training, licensing, subscription]

- id: n10
  title: OMC 首连三坑——pbxk1064 仅首次、证书必装、密码每客户必须不同
  type: warning
  source_pages: p70, p74-77
  source_chapter: How-To – OMC Installation
  source_quote: |
    p74: "Enter the default installer password pbxk1064 only used for the first connection"
    p75: "In order to avoid displaying the security alert at each connection, you must install the certificate the 1st time."
    p77: "The passwords must be different for each customer!"
  summary: |
    三个易踩点：pbxk1064 只在首次登录有效，之后必须换成客户专属密码；首次连接要把证书装入"受信任的根证书颁发机构"，否则每次连接都弹安全告警；各账户密码必须每个客户都不同，不能沿用默认或通用密码。
    连接方式要用 Expert 模式并勾选 Server authentication（p74）。
  conditions: OMC 安装与首次连接
  tags: [warning, omc, security]

- id: n11
  title: 修改 OXO IP 规划后必须重启设备才生效
  type: limitation
  source_pages: p80-81
  source_chapter: How-To – OXO Connect IP settings modification
  source_quote: |
    p80: "Restart OXO connect"
    p81: "Click OK & Re-start the OXO Connect"
  summary: |
    OMC 改完 LAN/IP 配置（Main CPU 地址、默认路由、DNS、DHCP 池）后必须重启 OXO Connect 才生效。
    改完 IP 也意味着此后的 OMC/浏览器都要用新地址连接，旧会话会失效——改完"连不上"先确认是不是还在用旧地址。
  conditions: IP 规划调整
  tags: [limitation, omc, network]

- id: n12
  title: 接入 Rainbow 域名保持默认 openrainbow.com，状态判据是 connected with final password
  type: limitation
  source_pages: p86, p88
  source_chapter: How-To – Connect an OXO to Rainbow
  source_quote: |
    p86: "Domain name Leave the default value: openrainbow.com"
    p88: "Control the connection status: « connected with final password »"
  summary: |
    OXO 接入 Rainbow 时域名保持默认值 openrainbow.com，教材明示不要改。
    验证是否真正接通，要看 Webdiag（Tools/Webdiag/Services/Rainbow Status）显示 "connected with final password"，同时可用 System/Log files 下的 ccrbagent.log 排障；若仍停留在默认密码状态，说明正式接入未完成。
  conditions: PBX 接入与连接排障
  tags: [limitation, connection, troubleshooting]

- id: n13
  title: 删除成员 10 天宽限期的三重副作用——邮箱不可复用、恢复即回落 Essential、需重配许可与电话线
  type: limitation
  source_pages: p93, p99
  source_chapter: Members – Manual creation / Members Deletion
  source_quote: |
    p93: "If you get an error message about the e-mail address you wish to use, please check that it is not already the identifier of a user deleted less than 10 days ago (grace period)."
    p99: "When deleted, the user's subscription was automatically removed. If you restore it, it will default to 'Essential' (free) mode, so you'll need to reallocate the appropriate license to restore the user's service level. It will also be necessary to reassign the user's telephone line."
  summary: |
    删除用户后账户进入 10 天 "Suspended" 宽限期，三件事要预期到：期间该邮箱 ID 不能复用（新建同名账号会报错）；误删恢复后订阅已被自动移除，账户回落为免费 Essential，必须重新分配订阅、重新关联电话线才恢复服务；不做任何操作则 10 天后永久删除。
    批量人员调整时把这三条算进工单时序，别按"删了马上重建"规划。
  conditions: 删除/恢复成员、复用邮箱建新户
  tags: [limitation, members, licensing]

- id: n14
  title: 管理员改密码会立即踢出该用户所有在线会话
  type: warning
  source_pages: p100
  source_chapter: Members – Security password & login
  source_quote: |
    "If the user is logged in at the time you make the password change, he/she will be logged out immediately. This is very useful if you suspect that a Rainbow account is being spoofed."
  summary: |
    管理员在 Security 页改用户密码的瞬间，该用户在线会话立即全部登出。怀疑盗号时这是特性（踢掉冒用者），日常批量改密则要避开工作时间，否则用户会当成掉线故障报上来。
    相关约束：密码复杂度（≥12 位、至少 1 大写/1 数字/1 特殊字符）同样约束手工建户、邀请回填与 CSV 导入（p93/94）；SSO 场景 CSV 的 password 字段可留空（p94）。
  conditions: 成员 Security 页改密
  tags: [warning, members, security]

- id: n15
  title: Rainbow 平台邮件可能进垃圾箱（建户与邀请两处重复警告）
  type: warning
  source_pages: p106, p108
  source_chapter: How-To – Rainbow accounts configuration and use
  source_quote: |
    "Warning CHECK THAT THE EMAILS SENT BY THE RAINBOW PLATFORM DO NOT ARRIVE IN THE SPAM."
    "PLEASE DELETE THE OLD EMAILS IN THE MAILBOX"
  summary: |
    建户通知邮件与邀请邮件都可能被判为垃圾邮件（教材在两页重复警告），用户说"没收到邮件"先查 spam 再重发。
    实验邮箱还要删掉旧邮件，避免误点旧邀请链接；生产环境应提醒客户把 openrainbow.com 发件域加白。
  conditions: 手工建户（勾选发送 enroll 邮件）与邮件邀请流程
  tags: [warning, members, email]

- id: n16
  title: RCC 模式能力边界——只能监督话机动作，音频全在话机，打不了纯 Rainbow 用户
  type: limitation
  source_pages: p6, p110, p112, p116
  source_chapter: How-To – Associate extension numbers with Rainbow user accounts
  source_quote: |
    p112: "Once associated, members will be able to supervise their phone from Rainbow (unhook, hang up, transfer), this is the RCC (Remote Call Control) mode. Without a WebRTC gateway, the audio will be exclusively managed on the phone."
    p116: "Search for the user cCpP.user2@ale-training.com who is a purely Rainbow user (without associated OXO extension) - Try to call him - Does it works ?"
  summary: |
    分机关联后只是 RCC：Rainbow 端只能对接听/挂断/转移做监督，通话音频完全走话机，Rainbow 耳机里没有声音。
    实验 4.3 以提问形式验证 RCC 用户呼叫"纯 Rainbow 用户"（无 OXO 分机），书中未给答案；按无网关即无音频通路的机制，该呼叫预期打不通——这正是下一步必须部署 WebRTC 网关的原因（呼叫失败的结论为推断）。
  conditions: 仅完成分机关联、未部署 WebRTC 网关阶段
  tags: [limitation, rcc, gateway]

- id: n17
  title: RCC 是无网关时的正常形态，不是故障
  type: misconception
  source_pages: p6, p110, p112
  source_chapter: Course Step by Step / Members labs
  source_quote: |
    p6: "At this step, Rainbow users can only supervise their extension: RCC mode (Remote Call Control) ... Audio is exclusively managed by the deskphone"
    p110: "Without the WebRTC gateway, the audio will be exclusively managed on the deskphone."
  summary: |
    教材把 RCC 明确定位为接入流程的中间步骤（课程主线就是先 RCC 后网关），是没有 WebRTC 网关时的正常交付形态。
    用户报"Rainbow 里点了接听但耳机没声音"，先核对站点是否处于 RCC 阶段，别按故障排查。
  conditions: 无网关站点
  tags: [misconception, rcc]

- id: n18
  title: WebRTC 网关只建音频媒体关系，不管呼叫控制
  type: limitation
  source_pages: p118
  source_chapter: OXO Connect WebRTC Gateway – Overview
  source_quote: |
    "The WebRTC Gateway brings voice interoperability between Rainbow Clients and PBX ecosystem. This enables an audio media relationship between Rainbow applications and devices of a PBX connected to Rainbow"
  summary: |
    网关的职责边界是"建立 Rainbow 应用与 PBX 设备间的音频媒体关系"，呼叫控制始终留在 PBX。
    排障分界：能通但没声音/声音单向找网关与媒体路径（含 TURN、防火墙），打不通/路由错找 PBX 侧编号计划与 ARS。
  conditions: 全部网关拓扑
  tags: [limitation, gateway, webrtc]

- id: n19
  title: 网关部署与用户使用的双重前置——PBX 先连 Rainbow、用户需 Business/Enterprise 且已关联话机
  type: limitation
  source_pages: p120, p142
  source_chapter: WebRTC Gateway – Deployment steps / Deployment steps on RAINBOW
  source_quote: |
    p120: "Prerequisites the PBX must be connected to Rainbow"
    p142: "Each user needs to be granted with either a Business or an Enterprise license. And the Rainbow account must be associated to this user PBX phone"
  summary: |
    部署网关前 PBX 必须先连上 Rainbow；用户侧要有 Business 或 Enterprise 订阅，且 Rainbow 账户已关联其 PBX 话机。
    网关建好了但个别用户用不了 VoIP，按这两条逐项核查，常见根因是许可没分或分机没关联。
  conditions: WebRTC 网关部署与用户开通
  tags: [limitation, gateway, licensing]

- id: n20
  title: 网关自动配置的版本门槛——R4.0.020.002（两处口径略有出入）
  type: version-trap
  source_pages: p121, p150
  source_chapter: WebRTC Gateway – Automatic configuration / How-To – Internal WebRTC Gateway automatic configuration
  source_quote: |
    p121: "The automatic configuration of the internal / external WebRTC gateway is available from system version R4.0.020.002"
    p150: "Automatic configuration applies to versions greater than R4.0.020.002"
  summary: |
    内部/外部网关自动配置自 R4.0.020.002 起提供。注意两处表述有细微出入：概述页写 "from ...R4.0.020.002"（含该版本），实验页写 "greater than"（高于该版本）。
    现场建议按"≥R4.0.020.002、实际以更高版本执行"处理；低版本系统先把升级做完再谈自动配置。
  conditions: 系统版本核查（自动配置可用性）
  tags: [version-trap, gateway, auto-config]

- id: n21
  title: 编号计划与闭锁始终由安装员完成——书中无一处教怎么做
  type: out-of-scope
  source_pages: p121, p150
  source_chapter: WebRTC Gateway – Automatic configuration
  source_quote: |
    "The following settings are still to be done by the installer as they are specific to each customer: • Connect PBX to Rainbow • Creation and association of the AnyDevice/Rainbow virtual terminals • Configuration of numbering plans and of the barring"
  summary: |
    自动配置只包办网关激活（仅 OCE 内部）、WebRTC SIP 网关、SIP 账号、VoIP 接入/中继组、ARS 路由；连 PBX 到 Rainbow、创建并关联 AnyDevice/Rainbow 虚拟终端、编号计划与闭锁（barring）仍由安装员完成（外部拓扑还要另加外置虚拟机安装与网关激活）。
    全书没有任何一处教编号计划与闭锁怎么配——混合交付的最后一步在书外（TC2479 与客户拨号规范）。
  conditions: 自动配置完成后
  tags: [out-of-scope, auto-config, numbering]

- id: n22
  title: WebRTC 网关激活只有 Reseller 管理员账户能操作
  type: limitation
  source_pages: p122, p151
  source_chapter: Automatic configuration / How-To – Internal WebRTC Gateway
  source_quote: |
    p151: "Automatic activation of the WebRTC gateway is performed by the trainer with a reseller administrator account ... He is the only authorized account to manage this service"
    p122: "Automatic deployment is managed from the Rainbow Reseller administrator account"
  summary: |
    WebRTC 网关的激活与通道数设置只能用 Reseller（经销商）管理员账户执行，客户管理员只能查看连接状态。
    现场客户管理员找不到激活入口时，先确认用的是谁的账号，别在权限上空耗。
  conditions: 激活网关（内部/外部/OCE-FE 均适用）
  tags: [limitation, gateway, bp]

- id: n23
  title: Anydevice 语义在 R5.2 前后不同——R6.0 起副站必须用 Twinset 才省 UTL
  type: version-trap
  source_pages: p123, p156
  source_chapter: Deployment steps on OXO Connect / How-To – Configure Anydevice/Rainbow virtual terminals
  source_quote: |
    "The secondary station is • Free Rainbow in Twinset from R6.0 • (Anydevice up to R5.2)"
    "Note: Until Release 5.2 the AnyDevice equipment was also used as a secondary station in multiset. Secondary station from Release 6.0: The Free Rainbow in Twinset virtual terminal must be used in order to save an UTL license (UTL Bypass)"
    p156: "Deskphone + Free Rainbow virtual terminal = 1 UTL • Anydevice only = 1 UTL"
  summary: |
    同一个 "Anydevice" 跨版本含义不同：R5.2 及以前它兼作 Multiset 副站；R6.0 起副站必须用 Free Rainbow in Twinset 虚拟终端（UTL Bypass，不额外吃 UTL），Anydevice 专指无物理话机的纯软话机终端。
    升级过的系统做用户扩容时若按旧语义建 Anydevice 副站，会白占 UTL。两种形态（话机+Twinset 副站、纯 Anydevice）各占 1 UTL。
  conditions: R5.2 与 R6.0 前后版本混存的系统
  tags: [version-trap, utl, terminal]

- id: n24
  title: Anydevice 不等于"移动分机"
  type: misconception
  source_pages: p123, p160, p169
  source_chapter: Deployment steps on OXO Connect / Configure virtual terminals lab / Attendant miscellaneous
  source_quote: |
    p123: "In the case of a user with only Rainbow (without a physical station), create for this user only an Anydevice terminal"
    p160: "The user has added his mobile number himself in his profile."
    p169: "Any Device on OXO Connect (minimum R6 version Maximum 8 calls"
  summary: |
    Anydevice 是 OXO 侧的纯软话机终端：无物理分机，全部通信经 Rainbow 应用（Client/Web/移动）；话务台场景下它是承载保持通话的多线路资源（≤8 路，≥R6）。
    用户的手机号是他在自己 profile 里加的路由选项，不代表 Anydevice 把手机注册成了 PBX 分机（与 OXE REX 的对应关系为推断性引申）。
  conditions: 向客户解释软话机形态与许可时
  tags: [misconception, terminal, anydevice]

- id: n25
  title: Rainbow 侧完整配置以 TC2462（OXE）/TC2479（OXO）为准
  type: out-of-scope
  source_pages: p123, p169
  source_chapter: Deployment steps on OXO Connect / Attendant – Miscellaneous
  source_quote: |
    p169: "Consult the technical communication for the OXE (TC2462) or OXO Connect (TC2479) for Rainbow configuration"
    p123: "TC2479 Rainbow WebRTC Gateway with OXO Connect / OXO Connect Evolution"
  summary: |
    OXO 侧 Rainbow/WebRTC 网关的完整配置细节在 TC2479（OXE 为 TC2462），教材只覆盖培训主线。
    叠加 n23 的版本语义变化，交付与排障必须以 TC2479 最新版为准，不能凭教材记忆操作。
  conditions: 生产配置与排障
  tags: [out-of-scope, tc2479, documentation]

- id: n26
  title: 集成网关 R3.2 起才有；之前的外置方案需要 SIP trunk 许可
  type: version-trap
  source_pages: p125
  source_chapter: Use case #1 – WebRTC integrated to OCE
  source_quote: |
    "Integrated WebRTC GW From R3.2 ... No need for SIP trunk licenses (bypass)"
    "Before R3.2 ... External WebRTC GW ... Private SIP Trunk ... SIP Trunk Licenses needed"
  summary: |
    集成 WebRTC 网关从 R3.2 起提供，且走 bypass 不占 SIP trunk 许可；R3.2 之前只能外置网关，并需要 SIP trunk 许可。
    给低版本站点评估方案与许可成本时，别按"集成免费"口径套算。
  conditions: OCE 系统版本与许可评估
  tags: [version-trap, gateway, licensing]

- id: n27
  title: OCE-FE 方案要求前端与呼叫服务器双端都 ≥R4.0 MD
  type: version-trap
  source_pages: p128
  source_chapter: Use case #2 – WebRTC gateway on OCE Front End
  source_quote: |
    "The release ≥ R4.0 MD must be installed on both the Front-End RGW and the OXO Connect call server"
    "Release ≥ R4.0 MD is mandatory"
  summary: |
    Front-End 网关方案要求前端 RGW 和呼叫服务器两台都升到 ≥R4.0 MD，只升一台不成立。
    好在 FTR 会自动提供 FE 免费许可并在需要时把 OCE 升到 ≥R4.0 MD；但呼叫服务器侧的版本要单独核对。
  conditions: OCE-FE 拓扑部署
  tags: [version-trap, oce-fe, gateway]

- id: n28
  title: OCE Front-End 无 PBX 能力、不吃 UTL，OMC 不参与其开通
  type: limitation
  source_pages: p129
  source_chapter: Use case #2 – Rainbow WebRTC Gateway on OCE Front-End
  source_quote: |
    "An OCE in front-end Mode is limited to WebRTC GW feature (No UTLs, etc…)"
    "OCE Front-End does not provide PBX capabilities • OMC tool is not needed for OCE Front-End provisioning"
  summary: |
    Front-End 模式的 OCE 只干 WebRTC 网关一件事：不提供 PBX 能力、不吃发 UTL，其开通也不需要 OMC（管理走 Rainbow Admin + Cloud Connect/FTR）。
    别把 FE 设备当备用 PBX 用，或试图往上面建用户分机。
  conditions: OCE-FE 拓扑
  tags: [limitation, oce-fe]

- id: n29
  title: 集成网关不支持 OXO Connect Power CPU EE，仅 Evolution（IPBox）可跑
  type: limitation
  source_pages: p118, p129
  source_chapter: WebRTC Gateway – Installation requirement / OCE Front-End 容量表
  source_quote: |
    p129 表格: "Internal GW — OXO Connect (Power CPU EE): Not supported / OXO Connect evolution (IPBox): 20 calls max."
    p118: "Installation requirement OXO Connect ... OXO Connect PowerCPU EE"
  summary: |
    内置（集成）WebRTC 网关只有 OXO Connect Evolution（IPBox）能跑，上限 20 通话；OXO Connect Power CPU EE 硬件不支持集成网关。
    Power CPU EE 站点要上 Rainbow 话音，只有两条路：OCE-FE（20 通话）或外置 NUC/ESXi（50 通话）。
  conditions: Power CPU EE 硬件站点选型
  tags: [limitation, capacity, hardware, gateway]

- id: n30
  title: OCE-FE GW 不支持以 OXO Connect Evolution 作呼叫服务器（该场景用集成网关）
  type: limitation
  source_pages: p129, p133
  source_chapter: OCE Front-End 容量表 / BP 管理配置
  source_quote: |
    p129 表格: "OCE-FE GW — OXO Connect (Power CPU EE): 20 calls max. / OXO Connect evolution (IPBox): Not supported"
    p133: "External on OCE Front End 20 max"
  summary: |
    按教材容量表，OCE-FE GW 只配 Power CPU EE 呼叫服务器（上限 20 通话）；呼叫服务器是 OXO Connect Evolution 时标 Not supported——Evolution 本身能跑 20 通话的集成网关，再挂 FE 无意义。
    选型时按呼叫服务器硬件定拓扑，别交叉套用；需要 50 通话时直接上外置 NUC/ESXi。
  conditions: 网关拓扑选型
  tags: [limitation, oce-fe, capacity]

- id: n31
  title: OCE-FE 配置修改必须 warm reset 才生效
  type: warning
  source_pages: p132
  source_chapter: Use case #2 – OCE Front-End status
  source_quote: |
    "A warm reset is necessary to take into account modification to Rainbow WebRTC Gateway on OCE Front-End"
  summary: |
    对 OCE-FE 网关配置做的修改必须热重启才生效。改完"没变化"先确认是否做过 warm reset，再往 Rainbow 侧查。
    FE CPU 状态可在 Settings 菜单和 Webdiag 工具中查看。
  conditions: OCE-FE 配置变更后
  tags: [warning, oce-fe, gateway]

- id: n32
  title: FTR 默认 PBXID 是占位符 FleetRef-Installref，设备会先连到占位租户
  type: version-trap
  source_pages: p134
  source_chapter: Use case #2 – OMC OCE Front-End configuration
  source_quote: |
    "On the OXO, by entering an FTR, the PBXID and the activation code are initialized by default to 'FleetRef-Installref', which allows the installer to prepare the equipment in advance in RB WebAdmin: the OXO will automatically connect to RB at the end of the FTR to FleetRef-Install_ID"
  summary: |
    FTR 时 PBXID/激活码默认写成 "FleetRef-Installref" 占位值，设备 FTR 结束会自动连到占位租户 FleetRef-Install_ID——便于提前备货预配置。
    正式割接必须替换为 Rainbow 平台生成的正式 PBXID/激活码；若 Rainbow 公司已创建，要把正式 PBXID 同时写入两台 OXO，否则连错租户。
  conditions: FTR 预配置转正式接入
  tags: [version-trap, pbxid, ftr]

- id: n33
  title: FE 与呼叫服务器 PBXID 必须一致；自动建 SIP 网关端口核验 5059
  type: limitation
  source_pages: p134
  source_chapter: Use case #2 – OMC OCE Front-End configuration
  source_quote: |
    "Rainbow PBXID must be the same in both OXO Connect, Front-End and call server"
    "Note: if the Rainbow company was already created put also the PbxId in both OXO"
    "Verify port numbers to 5059 in the SIP Gateway parameters"
  summary: |
    OCE-FE 方案中前端与呼叫服务器两台的 PBXID 必须一致（公司已建时把正式 PBXID 同时写进两台 OXO）；
    呼叫服务器上自动创建的私有 SIP 网关要核验端口为 5059。两处任一不一致都会导致配对或音频失败。
  conditions: OCE-FE 配置与排障
  tags: [limitation, oce-fe, pbxid]

- id: n34
  title: PBXID 不是 PBX 序列号，是 Rainbow 平台生成的接入凭证
  type: misconception
  source_pages: p86, p134
  source_chapter: How-To – Connect an OXO to Rainbow / OCE Front-End configuration
  source_quote: |
    p86: "Rainbow PABX-ID The Rainbow ID is generated by Rainbow. Activation code The activation code is generated by Rainbow."
    p134: "e.g: PBX9a86-5916-b74a-436c-aec6-c08a-58b6-5bb0"
  summary: |
    PBXID 是 Rainbow 平台生成的接入凭证（形如 PBX9a86-5916-...-5bb0），与 OXO 设备序列号无关。
    获取途径：经销商提供，或客户管理员登录 Rainbow 在 My company / Communication 里查看（p84-85）；FTR 场景下另有占位值（见 n32）。把 PBXID 当序列号去设备铭牌上找会白费劲。
  conditions: 查找接入凭证、接入排障
  tags: [misconception, pbxid]

- id: n35
  title: OCE-FE 各 commissioning 场景必须按 MyPortal《Rainbow WebRTC cookbook》最新版执行
  type: out-of-scope
  source_pages: p135, p137
  source_chapter: Use case #2 – OCE Front-End configuration / commissioning
  source_quote: |
    "Details about Front-End mode configuration in document Rainbow WebRTC cookbook available on MyPortal"
    "For this it is essential to follow the document 'Rainbow WebRTC cookbook' latest edition available on MyPortal"
  summary: |
    OCE-FE 有多种 commissioning 场景：全新安装（PBX+FE）、给已有 R4 或低于 R4 的 PBX 加 FE、订购带或不带 Partner fleet reference/Installation reference 等。
    教材明说"必须"按 MyPortal 上最新版 cookbook 执行，书内只给骨架；不同场景步骤差异大，别凭记忆操作。
  conditions: OCE-FE commissioning 全场景
  tags: [out-of-scope, oce-fe, cookbook]

- id: n36
  title: 外置网关（VM/NUC）部署步骤与防火墙白名单都在书外安装指南
  type: out-of-scope
  source_pages: p140, p144
  source_chapter: Use case #3/#4 – External WebRTC gateway deployment
  source_quote: |
    p140: "Download procedures from the Rainbow Support website, ALE equipments (PBX) section"
    p144: "Whitelist (Available in the procedure)"
  summary: |
    ESXi 虚拟机与 NUC 迷你机的网关安装配置步骤、以及防火墙白名单清单，都在 Rainbow 支持网站的安装指南里，教材只列大纲（下载 OVF/ISO、RUFUS 做 USB 启动等）。
    漏配白名单是外置网关不通的高频原因。
  conditions: 外置 VM/NUC 部署
  tags: [out-of-scope, gateway, firewall]

- id: n37
  title: TURN 服务器按站点位置配置，取值规则在书外
  type: out-of-scope
  source_pages: p141
  source_chapter: Use case #3 – WebRTC Gateway configuration steps
  source_quote: |
    "TURN server configuration according to site location"
  summary: |
    外置网关配置项中 TURN 服务器要"按站点位置"配置（是否启用、指向哪个 TURN 由站点网络位置决定），教材不展开取值规则，需按官方 cookbook 与网络要求文档执行。
    公网侧媒体是否走 TURN 直接影响 NAT 穿透与单向语音类问题。
  conditions: 外置 VM/NUC 网关网络配置
  tags: [out-of-scope, turn, network]

- id: n38
  title: 容量硬边界——外置 50 通话、集成/FE 20 通话、150 用户仅低话务成立
  type: limitation
  source_pages: p147, p129, p133
  source_chapter: Dimensioning – Rainbow WebRTC gateway dimensioning
  source_quote: |
    "50 VoIP calls maximum if the WebRTC gateway is external on Mini PC or ESXi server • 20 VoIP calls maximum with OCE integrated WebRTC gateway or if the WebRTC gateway is external on OCE Front End"
    "(*) Integrated WebRTC on OCE: the maximum Rainbow Users with VoIP limits depends on the number of configured Rainbow Channel and end user traffic. Value indicated here is for direction only for 20 configured WebRTC GW channels. But Maximum limit is 150 that is ok in case of very low traffic"
    表格: "70 27/NA ... 150 50/NA"（集成列 SIP trunk 推荐值为 NA）
  summary: |
    三条硬线：外置（NUC/ESXi）网关最多 50 通话；OCE 集成或 OCE-FE 最多 20 通话；容量表中 70/100/150 用户行的集成方案 SIP trunk 推荐值为 NA（20 通道撑不住）。
    "150 用户上限"的前提是 20 通道下用户话务很低，教材明说该值仅为方向性参考。话务量上来就换外置 50 通道方案，通道数与用户话务要同时看。
  conditions: 网关选型与扩容规划
  tags: [limitation, capacity, gateway]

- id: n39
  title: OXO Rainbow VoIP 用户上限已从 50 提升到 150——旧口径过时
  type: version-trap
  source_pages: p147
  source_chapter: Dimensioning
  source_quote: |
    "Maximum of OXO users with Rainbow VoIP option increased from 50 to 150 • Applies for both OXO Connect and OXO Connect evolution"
  summary: |
    OXO 侧 Rainbow VoIP 用户上限已从 50 提升到 150，OXO Connect 与 Evolution 都适用。
    网上旧资料/旧版技术通报里"50 用户上限"的说法已过时；但 150 成立的前提见 n38（通道数与话务量），售前引用数字时要带上前提。
  conditions: 售前容量评估引用旧文档时
  tags: [version-trap, capacity]

- id: n40
  title: Attendant 话务台只在 PC 上——话机与手机上没有任何话务台功能
  type: limitation
  source_pages: p164, p169
  source_chapter: Attendant Console / Miscellaneous
  source_quote: |
    p169: "The attendant may have a deskphone, but none of the functionalities are possible on the deskphone itself. Same behaviour for a smartphone ... Attendant features are only available on PC (thick client or web mode)"
    p164: "Attendant console not available on mobile. ... An Attendant user must have a telephone line, as well as VoIP softphone capability"
  summary: |
    话务台功能只能在 PC（客户端或 Web 模式）上用：话务员即使配了物理话机或智能手机，这些设备上没有任何话务台功能，也没有移动端 App。
    Attendant 用户还必须有电话线和 VoIP 软话机能力。给前台选型时别按"手机也能值班"做承诺。
  conditions: 话务台部署与值班方式设计
  tags: [limitation, attendant]

- id: n41
  title: 话务台容量分两层——队列 OXO 8/OXE 10，保持数取决于多线路资源（REX≤10/AnyDevice≤8）
  type: limitation
  source_pages: p164, p169
  source_chapter: Attendant Console / Miscellaneous
  source_quote: |
    p164: "Manage up to 10 calls for OXE - And up to 8 calls for OXO Connect"
    p169: "The number of calls that can be put on hold, depends on the multi-line resources assigned to the Attendant's softphone line: REX on OXE (Up to 10 calls) - Any Device on OXO Connect (minimum R6 version Maximum 8 calls"
  summary: |
    呼叫队列上限：OXE 10 路、OXO Connect 8 路。可保持的通话数取决于软话机线分配的多线路资源：OXE 用 REX（≤10 路），OXO Connect 用 AnyDevice（要求 R6 以上版本，≤8 路）。
    低版本 OXO 或多线路资源没配够时，实际可保持路数会缩水；容量承诺前先核资源。
  conditions: 话务台容量规划
  tags: [limitation, attendant, capacity]

- id: n42
  title: 监督组规格 5 组/30 人；代接仅限同一 PBX 且只能代接电话呼叫
  type: limitation
  source_pages: p167, p169
  source_chapter: Supervision Groups / Miscellaneous
  source_quote: |
    p167: "Maximum number of supervision groups for a supervisor: 5 ... Maximum number of users in a group (supervisors + supervised): 30"
    p169: "Interception is only possible if supervisors and supervisees are on the same PBX. Only phone calls can be intercepted."
  summary: |
    每个监督员最多属于 5 个监督组，每组（监督员+被监督人合计）最多 30 人。
    代接只在监督员与被监督人同属一台 PBX 时可行，且只能代接电话呼叫（Rainbow 侧会议等不能代接）。跨 PBX 组网或超 30 人的需求要拆组建。
  conditions: 创建监督组
  tags: [limitation, supervision, attendant]

- id: n43
  title: 监督组是 Rainbow 侧组织概念，与 OXO 的 ACD/呼叫组不是一回事
  type: misconception
  source_pages: p167
  source_chapter: Supervision Groups
  source_quote: |
    "In order to supervise the members of a company, users with the attendant subscription, and the supervised members must belong to a supervision group. Each supervision group includes • One or several supervisors: they must be granted an Attendant license ... • The company members to supervise"
  summary: |
    教材中的监督组是 Rainbow 侧的组织概念，服务话务台监督与代接，监督员必须有 Attendant 订阅。
    它与 OXO 话机侧的 ACD/呼叫分配组是两套独立机制：建 Rainbow 监督组不会改变 PBX 侧话务分配，反之亦然（书中未点名 ACD，此对比为两套体系机制的推断性引申）。
  conditions: 概念澄清与需求沟通
  tags: [misconception, supervision, acd]

- id: n44
  title: 互助组代接仅限 PBX 呼叫，不含 Rainbow 软话机呼叫；被监督成员必须是 PBX 设备
  type: limitation
  source_pages: p171, p180-181
  source_chapter: Mutual Aid Supervision Groups / How-To
  source_quote: |
    p171: "As supervisor, you will be notified of telephone calls intended for supervised users. • You can pickup calls. Works only for PBX calls, not for Rainbow softphone calls"
    p181: "These members must have a physical extension or an associated PBX softphone (IPDSP or MicroSIP)."
  summary: |
    互助监督组的代接只对 PBX 呼叫生效，纯 Rainbow 软话机呼叫不能被代接；被纳入互助组的成员必须有物理分机或 PBX 软话机。
    客户提"全员互帮互接"需求时要泼冷水：软话机-only 用户不在代接范围。
  conditions: 创建互助组选人、代接需求评估
  tags: [limitation, supervision, mutual-aid]

- id: n45
  title: 互助组一次最多监督 4 路呼叫；锁定成员不能退出组
  type: limitation
  source_pages: p172, p180
  source_chapter: Mutual Aid Supervision Groups – Application view / How-To
  source_quote: |
    p172: "Up to 4 calls supervised ... Locked: cannot leave"
    p180: "Lock the last member Yes/no"
  summary: |
    监督员端一次最多监督 4 路呼叫；组内"锁定"的成员不能自行退出组（建组时通过 Lock the last member 设置）。
    临时加入/退出、临时纳入/排除成员是互助组特性，但锁定成员不受个人意愿控制，建组前要和成员讲清楚规则。
  conditions: 互助组日常使用
  tags: [limitation, supervision, mutual-aid]

- id: n46
  title: Web 模式用户问题上报不采集事发日期
  type: limitation
  source_pages: p185
  source_chapter: Maintenance – Problems reported by your users
  source_quote: |
    "In web mode, the date is not requested because the logs in a browser are short-lived."
  summary: |
    用户通过 "Report a problem" 上报问题时，Web 端不要求填事发日期（浏览器日志存活时间短），桌面客户端才有日期字段。
    走 Web 上报的工单定位时间要靠附件截图与文字描述补齐；重要问题尽量引导用户用客户端上报。
  conditions: 用户问题上报流程
  tags: [limitation, maintenance]

- id: n47
  title: Rainbow 服务请求（ESR）只为认证伙伴创建
  type: limitation
  source_pages: p191
  source_chapter: Maintenance – Access to Rainbow support
  source_quote: |
    "The ESR will only be created if the partner is certified on Rainbow"
  summary: |
    通过 MyPortal/邮件/Emily BOT 等 入口开 Rainbow 服务请求的前提是伙伴持有 Rainbow 认证，否则工单不会被创建。
    非认证伙伴的现场问题要么先补认证，要么经认证的上家转报——支持路径要在项目开始前理顺。
  conditions: 开 Service Request 前
  tags: [limitation, support, certification]

- id: n48
  title: Teams 集成是工作站级落地，没有租户级一键生效
  type: misconception
  source_pages: p196
  source_chapter: Integration with Microsoft Teams
  source_quote: |
    "The integration is done at the workstation level"
  summary: |
    Rainbow for Teams 集成按"工作站"（每台 PC 安装应用）落地：Teams 管理中心只管应用上架与权限同意，每个用户机器上还要装 Rainbow Desktop 并保持运行。
    给客户讲方案时别按"管理员点一下全租户生效"表述，终端侧装机量要算进交付工作量。
  conditions: Teams 集成方案宣讲与报价
  tags: [misconception, teams]

- id: n49
  title: Teams 集成用户只配 Business/Enterprise 订阅，权限建议收敛为 Telephony-only
  type: limitation
  source_pages: p208, p234-235
  source_chapter: Integration with Microsoft Teams – Subscription / User configuration
  source_quote: |
    p208: "User must have one of these subscriptions: • Business • Enterprise ... Permissions to limit Rainbow collaboration features as collaboration services will be provided natively by Teams itself"
    p234: "As the user will use Teams for all collaboration services, Rainbow will only provide telephony integration services. So, it is better to apply a restrictive permission to users with Teams integration in order to forbid collaboration services from Rainbow."
  summary: |
    Teams 集成用户必须有 Business 或 Enterprise 订阅（Essential/Attendant 不在此列）。
    且建议把 Rainbow 权限收敛为 Telephony-only，协作（聊天/会议）交给 Teams 原生提供，避免两边都能聊、状态与记录分裂。
  conditions: Teams 集成用户配置
  tags: [limitation, teams, licensing, permissions]

- id: n50
  title: Teams 集成强依赖 Rainbow Desktop——必须已安装且正在运行
  type: warning
  source_pages: p209, p239-240
  source_chapter: Integration with Microsoft Teams / How-To – Rainbow for Teams installation
  source_quote: |
    p209: "Rainbow desktop application is required and must be running"
    p239: "Warning THE RAINBOW APPLICATION INTEGRATED INTO TEAMS REQUIRES THE INSTALLATION AND STARTUP OF THE RAINBOW DESKTOP APPLICATION ON THE PC."
    p240: "Warning The application must be present on the PC"
  summary: |
    Teams 内的 Rainbow 应用只是面板，拨号、呼叫控制、点击外拨都依赖本机安装且正在运行的 Rainbow Desktop。
    Desktop 没启动时 Teams 里会出现 "!" 图标，悬停可从那里拉起；Desktop 未安装则直接不可用。这是 Teams 集成最高频的现场支持请求，交付培训要专门讲。
  conditions: Teams 集成终端侧使用
  tags: [warning, teams, desktop]

- id: n51
  title: Teams 应用上架与权限同意的坑——目录搜到才算数、状态须 Allowed、同意要抢先由管理员做
  type: limitation
  source_pages: p224-228, p239
  source_chapter: How-To – Rainbow for Teams installation
  source_quote: |
    p224: "To give to users the possibility to install it, the status must be 'Allowed'. If the app can't be found, that probably means that it's not part of the third-party Microsoft apps ... To add the wanted application, click on 'Upload new app'"
    p239: "Note If the permissions required by the application have not been previously validated by the administrator ..., the user will be prompted to accept them himself. Tips In this case, it makes sense to add the first time the new app to Teams from an administrator account that will be able to validate the permissions for the entire organization."
  summary: |
    三个坑：Teams 应用目录里搜不到 Rainbow 不代表不能用——它可能不在微软默认第三方目录，需用 zip 包 "Upload new app" 上传；上架后 Release Status 必须是 Allowed 用户才能安装；
    权限同意没由管理员预先完成时，会落到第一个登录的用户头上——建议首次由管理员账号登录并勾选"代表整个组织"同意（或在 Teams 管理中心直接 Review permissions and consent，p226-227，教材注此法最简）。最后在 Azure AD 里核验权限已授予（p229-230）。
  conditions: Teams 管理中心上架与权限同意
  tags: [limitation, teams, permissions]

- id: n52
  title: SSO 并非 Teams 连接器的必要条件
  type: misconception
  source_pages: p241
  source_chapter: How-To – Rainbow for Teams installation (start-up)
  source_quote: |
    "Important SSO is not required to use the Rainbow/Teams connector."
  summary: |
    教材实验里用 Microsoft 凭据 SSO 登录 Rainbow Desktop，只是因为该环境恰好配了 SSO；连接器本身对认证方式无要求，普通密码登录同样可用。
    别把"先上 SSO"当成 Teams 集成的前置任务排进交付计划（教材以 Important 标注此点）。
  conditions: Teams 集成方案规划
  tags: [misconception, teams, sso]

- id: n53
  title: Teams/Rainbow 在场同步默认不生效，须手动激活 O365 信息共享
  type: limitation
  source_pages: p242-243
  source_chapter: How-To – Rainbow for Teams installation (presence synchronization)
  source_quote: |
    p242: "For the moment, the calendar/presence synchronization is not set"
    p243: "we activate the sharing of information with Office 365 ... Synchronization is now active."
  summary: |
    装完连接器后两边在场状态并不自动同步：首次测试会看到 Teams 里改了状态、Rainbow 纹丝不动。
    必须在 Rainbow App 里激活与 Office 365 的信息共享（选择用户账户）后同步才生效。验收清单要单列这一步，别把"装完即同步"写进验收标准。
  conditions: Teams 集成在场同步验收
  tags: [limitation, teams, presence]

- id: n54
  title: Rainbow number 是自动写入的隐藏配置，触发条件是用户路由切到 computer
  type: misconception
  source_pages: p115, p233
  source_chapter: How-To – Associate extension numbers / Rainbow user configuration for Teams
  source_quote: |
    "The list of OXO Connect extension numbers is synchronized live with the Rainbow environment."
    "This number will be retrieved later for WebRTC gateway use. It will be automatically configured in Remote Extension number by the Rainbow agent (e.g. BBB10070254106463346) when the user selects 'computer' as routing from his Rainbow client (PC or smartphone)."
  summary: |
    分机关联后出现的 Rainbow number（BBB 开头长串）无需手工配置：当用户把呼叫路由切到 "computer" 时，由 Rainbow agent 自动写入 PBX 侧的 Remote Extension number。
    排障时别找"手工填 Rainbow number 的入口"，应确认用户路由选择与该值是否已就位；另外 PBX 分机列表与 Rainbow 是实时同步的，PBX 侧建好号 Rainbow 端即可见。
  conditions: 分机关联后、网关音频联调与排障
  tags: [misconception, rcc, gateway, routing]
```

## 收尾自检 — 对照 BOOK_OVERVIEW.md 18 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | 网络前提核查与 Pilot 评估 | 有 → n02（网络要求 PDF 书外）、n03（Pilot 分区 To come） |
| task-02 | 公司体系（BP 建 EC、可见性、SSO/TOTP） | 有 → n04（一人一公司/查重）、n05（BP 专属权）、n06（ISOLATED 警告）、n07（SSO 门槛） |
| task-03 | 管理员权责、目录与信息频道 | 有 → n07（级别门槛）、n08（频道强制订阅） |
| task-04 | 订阅开通与分配 | 有 → n01（Essential 无电话）、n09（培训禁用预付） |
| task-05 | OMC 安装与首连 | 有 → n10（证书/首密/改密三坑） |
| task-06 | OXO 与客户端 IP 规划修改 | 有 → n11（改 IP 须重启） |
| task-07 | PBXID+激活码接入与验证 | 有 → n12（域名默认/状态判据）、n34（PBXID≠序列号） |
| task-08 | 成员创建与管理 | 有 → n13（10 天宽限期副作用）、n14（改密踢人）、n15（邮件 spam）、n07（AAD 导入门槛） |
| task-09 | 分机关联与 RCC 验证 | 有 → n16（RCC 能力边界）、n17（RCC 正常形态）、n54（Rainbow number 隐藏配置） |
| task-10 | 网关拓扑决策 | 有 → n18（GW 只管音频）、n26（R3.2）、n27（R4.0 MD）、n28（FE 无 PBX 能力）、n29（Power CPU EE 不支持集成 GW）、n30（FE 不支持 Evolution 呼叫服务器）、n38（容量硬边界）、n39（50→150 演进） |
| task-11 | 按拓扑部署网关 | 有 → n31（warm reset）、n32（FTR 占位 PBXID）、n33（PBXID 一致/5059）、n35（cookbook）、n36（VM/NUC 指南）、n37（TURN） |
| task-12 | 容量规划 | 有 → n38（20/50/NA/150 前提）、n39（50→150）、n30（FE 20 通话） |
| task-13 | 网关自动配置 | 有 → n20（R4.0.020.002 门槛）、n21（编号计划书外）、n22（仅 Reseller 可激活） |
| task-14 | 虚拟终端配置与 UTL | 有 → n23（Anydevice/Twinset 版本陷阱）、n24（Anydevice≠移动分机） |
| task-15 | 话务台与监督组 | 有 → n40（仅 PC）、n41（容量两层）、n42（5 组/30 人/同 PBX 代接）、n43（监督组≠ACD） |
| task-16 | 互助监督组 | 有 → n44（代接仅 PBX 呼叫）、n45（4 路/锁定成员） |
| task-17 | 维护与支持体系 | 有 → n46（Web 模式无日期）、n47（SR 认证门槛） |
| task-18 | Teams 集成全流程 | 有 → n48（工作台级）、n49（订阅/权限收敛）、n50（Desktop 依赖）、n51（上架与同意）、n52（SSO 非必要）、n53（在场同步默认关） |

**18/18 全部有边界类条目覆盖，无空缺。**

### 扫描完整性说明（Warning/Note/Tips 标记框逐页核对）

- 已全部入册的警告/注意框：p52（ISOLATED）、p66（YEAR PREPAID）、p77（密码每客户不同）、p100（改密踢人）、p106/p108（spam+删旧邮件）、p176（PREPAID）、p239/p240（Rainbow Desktop 警告两处）。
- 已入册的 Note/Important：p53 NB（其他认证方式须 ALE 确认）、p121/150（installer 剩余职责）、p123（R5.2/R6.0 语义）、p134（PBXID 一致/端口 5059）、p147（容量 * 注）、p226/228/239（权限同意）、p241（SSO 非必要）、p185（Web 模式无日期）。
- 复核后排除的纯操作提示框（非边界类，不构成候选）：p85 Tips（管理员可用 PC 客户端做公司管理）、p110 Tips（可用管理员账号做功能测试）、p186 Tips（法国订阅告警勾选 WW/EMEA/DE）、p240 Note（"!"窗口在 Desktop 启动后自动消失）、p113 V-Class 无物理话机（教学环境事实，BOOK_OVERVIEW 已将实验环境列为不入册内容）。
- 推断性结论已在对应条目 summary 内显式标注"（推断）"：n16（RCC 呼叫纯 Rainbow 用户失败的结论）、n24（与 OXE REX 的对应引申）、n43（与 ACD 的对比）。
- 版本号均按原文保留完整位数：R3.2、R4.0.020.002、R4.0 MD、R5.2、R6.0、R6（p169 AnyDevice 最低版本表述）。
