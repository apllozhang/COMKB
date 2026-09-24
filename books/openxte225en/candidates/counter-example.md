# 反例/限制/边界/易错点候选 — OpenTouch Mobility & Remote Worker (OPENXTE225EN R2.6 Issue 10)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: 预载"通用证书"（security off）被官方明确反对——话费欺诈与服务盗用风险
  type: warning
  source_pages: p50-51, p61
  source_chapter: Certificates / Certificates possibilities & Warning
  source_quote: |
    "BEWARE, this choice is not recommended by Alcatel-Lucent Enterprise as they imply: increased risks of
    toll fraud and unauthorized use of the services or functionalities on the system. … Conclusion: It is
    advised to use an external PKI to obtain CA root public certificate" (p61)
  summary: |
    安装时选"通用证书 + CTL（由通用设备签名）"虽便于批量部署，但安全是关闭状态（security off），官方
    明确不推荐：话费欺诈风险上升、系统服务与功能可被未授权使用。结论口径：用外部 PKI 取得 CA 根证书。
    交付时凡遇到"装的时候图省事选了 generic"的存量系统，先补证书再谈远程接入。
  conditions: 证书选型场景；远程接入必须 CA 签发（p53）
  tags: [warning, certificates, security]

- id: n02
  title: DAS 规则顺序敏感且多条可同时命中；规则国家相关（书中为法国口径）
  type: warning
  source_pages: p67
  source_chapter: OT server settings for remote access / DAS Rules configuration
  source_quote: |
    "Note: DAS rules are mandatory and are country dependant. The configuration proposed in this procedure
    is for France. … WARNING: THE DECLARATION ORDER IS IMPORTANT. SEVERAL RULES CAN BE APLLIED AT A TIME
    (EXAMPLE : RULE 1 AND 2, 4 AND 6 …)" (p67)
  summary: |
    会议域 DAS 规则三条约束：①强制要有（mandatory）；②国家相关——书中 10 条是法国口径，其他国家必须
    改写；③声明顺序重要，且一次可有多条规则同时命中（原书例：规则 1 与 2、4 与 6）。照抄法国配置到
   其他国家，号码变换会成批出错。
  conditions: 会议服务器 Administration Console / Default 域
  tags: [warning, das, conference, country-specific]

- id: n03
  title: 会议邀请专用 FQDN 必须进 RP 与 OT 证书的 SAN；内部 DNS 必须有该条目
  type: warning
  source_pages: p68, p70
  source_chapter: Management for conferences accesses / ACS Service configuration & Rehosting
  source_quote: |
    "WARNING: THIS SPECIFIC FQDN ASSIGNED FOR CONFERENCES INVITATION MUST BE PART (SUBJECT ALTERNATIVE NAME)
    OF THE REVERSE PROXY AND OPENTOUCH SERVER CERTIFICATES." (p68)
    "WARNING: AN ENTRY FOR THIS DEDICATED FQDN AND IP ADDRESS MUST BE MANAGED IN INTERNAL DNS SERVER.
    VERIFY THAT IT IS THE CASE. PERFORM THE REQUIRED ACTION IF IT IS NOT DONE." (p70)
  summary: |
    双重强制：①会议服务专用 FQDN（实验口径 conf-podx.al-mydemo.com）必须同时写入反代与 OT 服务器证书的
    SAN——漏配则会议邀请链接不可用；②rehost 后内部 DNS 必须有"FQDN→专用 IP（151.1.1.55）"条目。两处
    都要主动核验，系统不会替你补。
  conditions: ACS 会议服务未随初装配置或需变更时
  tags: [warning, san, dns, conference]

- id: n04
  title: 证书 Deploy 后 WebAdmin 会话被切断属正常现象，勿当故障
  type: misconception
  source_pages: p76, p268
  source_chapter: Certificate deployment / OpenSSL How-To
  source_quote: |
    "Just after clicking on 'Deploy', a message is displayed (« Impossible to retrieve data from / … ») and
    the WebAdmin session is cut. You have to restart the web session. It is normal because the server's
    certificate used for the 'https' connection has just changed." (p76)
  summary: |
    导入证书后必须点 Deploy；刚点完会弹 "Impossible to retrieve data from / …" 且 WebAdmin 掉线——这是
    https 所用服务器证书刚变更的必然结果，重开会话即可。现场常见误判：把这一步当成"导入失败"反复重做。
  conditions: OpenTouch 服务器证书导入与部署
  tags: [misconception, certificates, webadmin]

- id: n05
  title: 服务器证书变更后，话机使用的 CTL 必须重新签名——操作在另一培训规程里
  type: out-of-scope
  source_pages: p268
  source_chapter: OpenSSL / Certificate and private key deployment on OpenTouch server
  source_quote: |
    "Warning: HOW IT IS SPECIFIED IN THE SNAPSHOT WARNING, THE CTL (USED BY DESKPHONES) HAS TO BE
    REGENERATED (SIGNED AGAIN) BECAUSE THE SERVER'S CERTIFICATE HAS CHANGED. THAT IS EXPLAINED IN ANOTHER
    PROCEDURE PART OF ANOTHER TRAINING." (p268)
  summary: |
    更换 OT 服务器证书后，话机侧依赖的 CTL 必须重新生成（重新签名），否则话机侧信任链断——但本书不含
    该操作（明示属另一门培训的规程）。照本书换证书后话机出现异常，先想到 CTL 未重签。
  conditions: 服务器证书变更后
  tags: [out-of-scope, certificates, ctl, deskphones]

- id: n06
  title: iPhone 部署强制手工配置——向导不覆盖，书内实验也不含
  type: limitation
  source_pages: p105, p117
  source_chapter: OTSBC deployment / Wizard & Manual configuration
  source_quote: |
    "FOR IPHONE DEPLOYMENT, ADDITIONNAL MANUAL CONFIGURATION OF SEVERAL OBJECTS IS MANDATORY. IT IS NOT
    PART OF THIS LAB. CONSULT THE TC2639 FOR CONFIGURATION INFORMATION." (p105)
  summary: |
    OTSBC 向导（Alcatel-Lucent Remote Users 模板）不覆盖 iPhone 所需的若干对象；iPhone 部署必须手工补配
    （两处 Warning 重复强调），配置依据 TC2639。书内能做的只有：SBC 声明用 5265 端口（p188/p197）与 OT
    SBC 增配 5265 SIP 接口（p188）。按"跑完向导就完事"交付 iPhone 场景必然翻车。
  conditions: iPhone（尤其 iPhone+ VoIP everywhere）部署
  tags: [limitation, iphone, otsbc, out-of-scope]

- id: n07
  title: OTSBC 向导只给 OXE 配 UDP——最好手工补 TCP 5060
  type: limitation
  source_pages: p117
  source_chapter: OTSBC deployment / Manual configuration of parameters
  source_quote: |
    "OXE can use UDP as well TCP for SIP. But wizard configures only UDP. It is why it is better to
    configure also TCP port in OTSBC. … TCP port 5060" (p117)
  summary: |
    向导生成的 OXE SIP 接口（SIP interface 2）只有 UDP；OXE 本身 UDP/TCP 都支持，建议手工补 TCP 5060。
    这与 iPhone 场外"TCP 强制"的要求呼应——不补 TCP，场外经 SBC 的部分场景会缺承载。
  conditions: 向导配置完成后
  tags: [limitation, otsbc, sip-interface, wizard]

- id: n08
  title: 同一 PC 客户端两种身份：Conversation 走 OT 服务器、Connection 走 OXE（2.2 起）
  type: limitation
  source_pages: p114
  source_chapter: OTSBC deployment / Thick wizard notes
  source_quote: |
    "Since OpenTouch 2.2 release, Conversation and Connection users are using the same PC client but
    according to the use, the application has a different behavior. With a Conversation user, SIP
    communication is done with OpenTouch SIP server and for a Connection user it is with OXE SIP server." (p114)
  summary: |
    排障 SIP 注册问题时先分清用户身份：同一客户端，Conversation 用户 SIP 注册到 OpenTouch SIP 服务器，
    Connection 用户注册到 OXE SIP 服务器。OTSBC 向导里 OTCV 与 OTCT 两组参数对应这两种身份，漏勾任一组
    该类用户就无法经 SBC 注册。
  conditions: OpenTouch 2.2 起的客户端行为
  tags: [limitation, conversation-user, connection-user, sip]

- id: n09
  title: 内嵌 RP 的 HTTP proxy 功能需要专门许可（实验环境可无许可先测）
  type: limitation
  source_pages: p133
  source_chapter: Embedded Reverse Proxy deployment / License verification
  source_quote: |
    "A specific license is required to use http proxy function of the OTSBC. … Tips: For the lab, the
    feature can be tested without the license." (p133)
  summary: |
    OTSBC 的 HTTP proxy（内嵌 RP）功能要有专门许可（License Key 页显示 HTTP Proxy Available）。实验环境
    无许可也能测——但别把实验习惯带进生产：报价与交付清单里要含这项许可。
  conditions: OTSBC 7.2+ 内嵌 RP 场景
  tags: [limitation, license, reverse-proxy, otsbc]

- id: n10
  title: RP 层 LDAP 认证的 daemon 需要专用机器（内嵌与独立两路线均受影响）
  type: warning
  source_pages: p140, p257
  source_chapter: Embedded Reverse Proxy deployment / External authentication & Nginx LDAP
  source_quote: |
    "WARNING: A DEDICATED MACHINE IS NECESSARY TO RUN THE LDAP-AUTH DEAMON. For this lab, we will not
    implement and test the external LDAP authentication." (p140)
    "The LDAP authentication module is based on a python script: nginx-ldap-auth-daemon.py. An LDAP-auth
    daemon is running on the NGINX server and listening on the port 8888." (p257)
  summary: |
    内嵌 RP 路线：要在外部 LDAP 做认证，LDAP-auth daemon 必须跑在一台专用机器上（Warning 原文），实验
    明确不实施；Nginx 独立路线：daemon 与 Nginx 同机、监听 8888。两条路线的生产方案都要把认证组件的
    资源与位置先定下来，实验跳过≠生产可跳过。
  conditions: 需要 RP 层认证的部署
  tags: [warning, authentication, ldap, capacity]

- id: n11
  title: 用智能手机拨打时永远用手机本机发话——"dial from"设置不生效
  type: misconception
  source_pages: p147, p150
  source_chapter: Clients in remote access / Principle & Smartphone
  source_quote: |
    "When a smart phone is used to dial (dial by number, directory search, from history, from contacts, …),
    it is always used to make the call whatever the 'dial from' specified in the active profile" (p147)
  summary: |
    用户常见误解："我在档案里设了从 PC 拨，为什么手机上点联系人还是手机拨？"——原书两处明示：手机上
    发起拨打（按键/目录/历史/联系人）永远用手机本机发话，"dial from"只对从 PC 等其他端发起的呼叫生效。
    讲解路由档案时要主动说明这个特例。
  conditions: OTC smartphone 用户
  tags: [misconception, smartphone, routing-profile]

- id: n12
  title: multi-devices 的两个特性前缀必须在用户 COS 里 Validate
  type: warning
  source_pages: p153
  source_chapter: OTC PC for remote worker / Prefixes configuration
  source_quote: |
    "Warning: DON'T FORGET TO VALIDATE BOTH FEATURES IN THE USERS' CLASS OF SERVICE." (p153)
  summary: |
    建好 Twinset get call（例 506）与 No ringing（例 507）两个前缀后，必须在用户的 Class of Service 里
    授权这两个特性——原书专门 Warning 强调。漏授权是 multi-devices 副设备"建了但不工作"的高频根因。
  conditions: multi-devices 前提配置
  tags: [warning, multi-devices, cos, prefixes]

- id: n13
  title: SIP Nomadic 必须有 Ghost Z 设备池——按并发数规划，池空则无法游牧
  type: warning
  source_pages: p157-158
  source_chapter: OTC PC for remote worker / Nomadic in VoIP (SIP) mode
  source_quote: |
    "Warning: AS FOR GSM NOMADIC MODE, SIP NOMADIC REQUIRE A POOL OF Z GHOST DEVICES." (p158)
    "it is very important to know how many Nomadic SIP connections will be established simultaneously,
    because it corresponds to the number of SIP devices & Ghost Z sets needed by the system" (p157)
  summary: |
    与 GSM 游牧一样，SIP 游牧强制要求 Ghost Z 设备池；每条并发连接占 1 SIP 设备 + 1 Ghost Z，退出游牧
    才释放。上线前必须统计并发游牧人数定池大小——池耗尽后后续用户无法进入游牧模式（书中以"very
    important"强调，未描述失败提示形态）。
  conditions: Nomadic SIP 场景
  tags: [warning, nomadic-sip, ghost-z, capacity]

- id: n14
  title: SIP 设备默认口令 0000——必须改成与分机号一致等强值
  type: warning
  source_pages: p160
  source_chapter: OTC PC for remote worker / SIP devices configuration in the OXE call server
  source_quote: |
    "Password: Filled in automatically (by default, '0000'); modify the value if needed. Set for example
    the same number as directory number. E.g. 31951" (p160)
  summary: |
    OXE 侧 SIP 设备的 SIP 口令自动填充为默认值 0000，必须修改（书中建议设为与分机号一致）。SIP 注册
    失败排查时先核对 OT 侧 OXE SIP Subscriber 里填的口令与此处一致——两边不一致是最直接的注册失败原因。
  conditions: Nomadic SIP 设备池配置
  tags: [warning, sip, password, nomadic-sip]

- id: n15
  title: 游牧用户需要同时开两个许可：Nomadic SIP 与 Desktop
  type: limitation
  source_pages: p161
  source_chapter: OTC PC for remote worker / Nomadic SIP right
  source_quote: |
    "To be able to use the Nomadic mode using SIP protocol, additional right must be granted to the OTC
    Connection user. … Nomadic SIP: Must be enabled; Desktop: Must be enabled" (p161)
  summary: |
    游牧 SIP 模式要求用户 licenses 页签里 Nomadic SIP 与 Desktop 两项都启用——只开其中一项游牧不可用。
    排障"用户切不到 Personal Computer/游牧失败"先查这两项。
  conditions: OTC Connection 用户
  tags: [limitation, licensing, nomadic-sip]

- id: n16
  title: R2.6 版本分界：远程分机单设备是新配法，R2.5 及以前必须永不入服 SIP 主设备+溢出
  type: version-trap
  source_pages: p182, p204
  source_chapter: OTC for smartphones / Remote extension as single device & How-To
  source_quote: |
    "The classic configuration of OTC smartphone for Connection users is based on a twinset … In case of a
    user without physical main desk phone but only a smartphone, the configuration principle was the
    following before the OpenTouch R2.6: Main device (desk phone): a SIP extension (which never be in
    service) … Now, from release 2.6 … the main device can be directly the remote extension" (p204)
  summary: |
    同一需求（用户只有手机没有话机）在 R2.6 前后配法完全不同：R2.5 及以前=永不入服的 SIP 扩展当主设备
    + RE 当副设备 + 主设备离线溢出；R2.6 起=RE 直接当主设备（单设备）。收益还包括修复离线呼转问题、
    凭 RE 回调进 OT 会议。混版本交付时按系统实际版本选配法，别把新配法套到老系统。
  conditions: 版本分界 OpenTouch R2.6；SEPLOS 假主设备为旧法产物
  tags: [version-trap, remote-extension, smartphone]

- id: n17
  title: iPhone 推送链路（R2.3.1 起）：APNS 证书一年一换（hotfix），Geotrust 根证书 2022 年到期
  type: version-trap
  source_pages: p183-184
  source_chapter: OTC for iPhone / APNS
  source_quote: |
    "APNS's certificate is shipped with OpenTouch server: Valid one year; A dedicated hotfix will be
    delivered every year to keep the certificate up to date … Root certificate from authority certification
    (Geotrust) is already available by default after OT installation: Valid till year 2022" (p184)
  summary: |
    iPhone 推送依赖两张证书：APNS 证书（随 OT 出厂、有效期一年、每年由专门 hotfix 更新）与 Geotrust 根
    证书（出厂自带、有效期到 2022 年）。运维含义：每年必须跟 OpenTouch 的 APNS hotfix；跨 2022 的部署
    根证书续期机制在书外。"iPhone 突然收不到来话"先查这两张证书与 hotfix 状态。
  conditions: R2.3.1 起全部 iPhone 通知走 APNS
  tags: [version-trap, iphone, apns, certificates]

- id: n18
  title: iPhone 后台来话需要多次 SIP invite：UDP 强制、场外 TCP 由 OT 代理缓冲
  type: limitation
  source_pages: p185-187
  source_chapter: OTC for iPhone / VoIP incoming call principle & Constraints
  source_quote: |
    "SIP Invite: ignored as application is in background … Push Notification … Application wake up" (p185)
    "UDP is mandatory to allow the several SIP Invites during incoming calls, and this is not possible with
    TCP … Behind the SBC, over Internet, TCP is mandatory: OpenTouch server will act as a SIP proxy
    'buffering' the SIP invite message over TCP" (p186)
  summary: |
    机制限制：OTC 在后台时首个 SIP invite 被忽略，需推送唤醒后再来一次 invite，因此"多次 SIP invite"是
    设计行为不是故障。承载约束：场内 UDP 拓扑无影响；场外经 SBC 走互联网强制 TCP，此时由 OT 侧
    kamailio-wasp（SBC 与 OXE 之间的 SIP 代理）+ wspcfg 做 invite 缓冲。iPhone 场外来话慢/漏接，先查
    这条链路与组件状态。
  conditions: iPhone VoIP everywhere 场景（R2.3.1+）
  tags: [limitation, iphone, apns, kamailio-wasp, sip]

- id: n19
  title: RE DISA 前缀必须在 DDI 翻译表有对应，否则外线进不了远程分机
  type: warning
  source_pages: p192
  source_chapter: OTC smartphone for Connection users / Remote extension DISA prefix
  source_quote: |
    "Warning: CHECK THAT THIS PREFIX IS TRANSLATED IN THE DDI TRANSLATION TABLE" (p192)
  summary: |
    建 RE DISA 前缀（实验口径 31280）后必须核对该前缀已进 DDI 翻译表——外线呼叫经公共号码进 DISA 链路
    依赖这张表。漏配的表象是"内部都通、外线打手机进不来"，且不易联想到前缀配置。
  conditions: 远程分机/智能手机 DISA 场景
  tags: [warning, disa, ddi, remote-extension]

- id: n20
  title: 直连速拨号范围不能为 0、也不能配满
  type: limitation
  source_pages: p195
  source_chapter: OTC smartphone for Connection users / Range of direct speed dialing numbers
  source_quote: |
    "The range size CANNOT be 0 and also should NOT be full." (p195)
  summary: |
    系统用 Direct Speed Dial 号段给远程分机做自动替代，范围长度不能设 0、也不应配满（配满后无号可自动
    分配）。实验口径 1000 个；生产按远程分机规模预留余量。
  conditions: 自动替代（automatic substitution）依赖该号段
  tags: [limitation, smartphone, speed-dial]

- id: n21
  title: 远程分机目录号禁用字母前缀（A/B/C/D）——手机设备号用 D、速拨号用 A 是另一套
  type: warning
  source_pages: p202
  source_chapter: OTC smartphone for Connection users / Mobile device declaration
  source_quote: |
    "Remote extension directory…: Enter a number for the remote extension created in OXE (e.g. 2131001).
    Do NOT use a number beginning with letter (A,B,C,D) in the directory number of the Remote Extension!" (p202)
  summary: |
    OTC Smartphone 的设备号允许字母前缀（惯例 D），速拨号用 A，Ghost Z 可用 B——但远程分机的目录号严禁
    以字母开头（原文大写禁令）。填错位置（把 D 号填进 RE 目录号）会破坏自动替代与 tandem 关联。
  conditions: 手机关联（General 与 OXE CS 两个页签的字段分工）
  tags: [warning, numbering, smartphone]

- id: n22
  title: 双模式呼手机的两道关卡：判别器逻辑→物理关联 + 公网接入 COS 区域授权（barring）
  type: warning
  source_pages: p210, p212
  source_chapter: OTC smartphone for Connection users / Discriminator & Additional manual management
  source_quote: |
    "Warning: Each Entity where dual mode CT users will be declared, it is important to review the
    Discriminator Selector to associate a logical discriminator to a physical discriminator that is
    dedicated to smartphones." (p212)
    "Warning: To be able to call the mobile the system must pass the baring. The area of the public access
    Class Of Service specified in the dedicated discriminator for Ct smartphones, must be authorized to
    call the mobile number of the user" (p212)
  summary: |
    自动对象建完还不算完，两个 Warning 必须手工核：①用户 Entity 的 Discriminator Selector 要把专用 ARS
    前缀里指定的逻辑判别器关联到智能手机专用物理判别器（实验口径 03）；②判别器指定的公网接入 COS 的
    区域必须对该用户手机号放行（"system must pass the baring"）。任一漏配，双模式倒换到 GSM 呼手机的
    路径即断。
  conditions: 双模式智能手机用户（Entity 级配置）
  tags: [warning, discriminator, barring, cos, dual-mode]

- id: n23
  title: Android 无 SIM 模式的功能代价：无回落、无私 人呼叫、无短信
  type: limitation
  source_pages: p176
  source_chapter: OTC smartphone / Android without SIM
  source_quote: |
    "Android Smartphones can run without SIM card; Smartphone is then used as a pure VoIP softphone: No
    carrier charge … No cellular network, so following features are discarded: Fallback mode, Private
    calls, SMS" (p176)
  summary: |
    Android 可无 SIM 卡当纯 VoIP 软话机（省运营商费用），设置上要求：业务手机号留空、VoIP 模式常开、
    来话弹屏常开。代价：无蜂窝网故回落（DTMF）模式、私人呼叫、短信三项全部不可用。给客户报"WiFi-only
    话机"方案时要带着这三条限制谈。
  conditions: Android 平台特有玩法
  tags: [limitation, android, fallback, sms]

- id: n24
  title: 用例矩阵的 N.U. 与 N.A. 是两回事：OTC PC One 无 VoIP 所以"用不上"SBC
  type: misconception
  source_pages: p40-42, p82, p122
  source_chapter: Use cases（三张客户端矩阵）
  source_quote: |
    "N.U : Not Used (because no VoIP/video on this client); N.A : Not Applicable; *: Audio only, no video" (p82)
  summary: |
    矩阵符号语义：N.A.=Not Applicable（该组合不适用）；N.U.=Not Used（客户端根本没有 VoIP/视频，SBC 无
    用武之地——特指 OTC PC One）。报方案时把 OTC PC One 说成"不支持 SBC/不支持加密"是错的：它是没有
    VoIP 可保护。另外带 * 的智能手机客户端仅音频无视频。
  conditions: 客户端×边缘组件选型沟通
  tags: [misconception, otc-pc-one, matrix, nomenclature]

- id: n25
  title: Nginx 配置自 OT 2.2 起必须 remoteworker.conf 与 conference.conf 同改——OTES 已退场
  type: version-trap
  source_pages: p253
  source_chapter: Nginx reverse proxy deployment / Nginx configuration file
  source_quote: |
    "The NGINX configuration has changed since release 2.2. As the OTES server is no more part of the
    solution, the reverse proxy must be configured to support application sharing during data conferences
    (web conferences). It is why there are now two configuration files to modify: remoteworker.conf,
    conference.conf" (p253)
  summary: |
    旧口径（OT 2.2 前）只改 remoteworker.conf；OT 2.2 起 OTES 不再是方案一部分，会议中的应用共享改经
    反代，因此 conference.conf 必须一并修改（server_name 第 13/33 行），漏改则会议协作功能经反代不可用。
    另：反代配置模板的下载链接以 TC2639 最新版为准（p220——旧链接可能失效）。
  conditions: OpenTouch 2.2+ 的 Nginx 反代
  tags: [version-trap, nginx, conference, ot-2.2]

- id: n26
  title: Nginx 反代 LDAP 认证仅支持 Python 2——版本 3 明确不支持
  type: version-trap
  source_pages: p257
  source_chapter: Nginx reverse proxy deployment / Installation of the needed packages
  source_quote: |
    "Using 'apt-get' install the following packages: Python (version 2 only – version 3 not supported);
    Python-ldap" (p257)
  summary: |
    nginx-ldap-auth-daemon.py 认证模块只支持 Python 2，Python 3 不支持（原文明示）。在 Python 3-only 的
    新系统上部署会直接失败；这是该教材时代（Ubuntu 16.04/xenial 源）的硬边界，生产上替代方案在书外。
  conditions: Nginx 反代外接 LDAP 认证
  tags: [version-trap, nginx, ldap, python]

- id: n27
  title: vSphere client 仅支持 ESXi 6.0 及以下——6.5 起用 web 界面
  type: version-trap
  source_pages: p221, p274
  source_chapter: Nginx RP / VM deployment
  source_quote: |
    "Warning: VSPHERE CLIENT IS ONLY AVAILABLE WITH ESXI VERSION 6.0 OR LOWER." (p274)
  summary: |
    书中两套 OVF 部署步骤对应不同 ESXi 版本：vSphere client 步骤只适用于 ESXi 6.0 及以下（Warning 大写
    强调）；ESXi 6.5 用 web 客户端（原理相同、入口不同）。拿错工具会直接找不到 Deploy OVF 入口。
  conditions: OVF/OVA 虚机部署
  tags: [version-trap, vmware, esxi]

- id: n28
  title: 实验安装 Nginx 时忽略包签名告警（NO_PUBKEY / cannot be authenticated）——教学口径，生产不可照搬
  type: warning
  source_pages: p248
  source_chapter: Nginx reverse proxy deployment / Nginx server installation
  source_quote: |
    "W: GPG error: … NO_PUBKEY ABF5BD827BD9BF62 … N: Data from such a repository can't be authenticated and
    is therefore potentially dangerous to use. … WARNING: The following packages cannot be authenticated!
    nginx Install these packages without verification? [y/N] Y" (p248)
  summary: |
    实验步骤里 apt 报 GPG 未签名（缺公钥 ABF5BD827BD9BF62）与"包无法认证"告警后直接选 Y 继续安装——这
    是教学口径的权宜做法。生产部署应先导入 nginx 官方签名公钥再安装，别把"跳过校验"固化为标准操作。
  conditions: Ubuntu/xenial + nginx mainline 源（实验口径）
  tags: [warning, nginx, security, lab]

- id: n29
  title: 教材文本笔误与不一致清单（照抄会踩坑）
  type: limitation
  source_pages: p156, p229, p236, p250, p251, p214
  source_chapter: 多处
  source_quote: |
    p229: "IP address: 11.1.1.10; Netmask: 255.255.255.0; Gateway: 10.1.0.254"（同章 p236 示例为 11.1.1.254）
    p250: "root@rp:~#/etc/inid.d/nginx restart"（应为 init.d，p254 亦复现）
    p156: "SBC address: Enter the public OTSBC FQDN. E.g. otsbx-podx.al-mydemo.com"（他处均作 otsbc-）
    p214: "e.g.: https//otms.company.com"（缺冒号）
  summary: |
    原书四处笔误/不一致：①Nginx 主机网关一处写 10.1.0.254、另一处写 11.1.1.254（同实验拓扑应为后者）；
    ②nginx 重启路径两处写成 /etc/inid.d/（正确为 /etc/init.d/）；③OTSBC FQDN 示例一处拼作 otsbx-podx；
    ④URL 示例缺 "://" 冒号。跟书操作时以拓扑一致性自校，别逐字照抄。
  conditions: 阅读与跟做实验时
  tags: [limitation, errata, documentation]

- id: n30
  title: 容量与体验数值全书缺位：CAC 无阈值、游牧池无算例、带宽无口径
  type: out-of-scope
  source_pages: p81, p157-158
  source_chapter: OTSBC main functions / Nomadic pooling
  source_quote: |
    "Quality of service and CAC: monitor the quality of the communication and can limit the number of
    communication in case of congestion" (p81)
    "it is very important to know how many Nomadic SIP connections will be established simultaneously" (p157)
  summary: |
    全书容量相关只有三处定性表述：SBC 有 CAC 能力（能限流，无阈值）、游牧池按并发规划（无算例）、媒体
    端口段（7000-7499/28000:39999，实验口径）。并发用户规模、每用户带宽、CAC 阈值建议值全部在书外——
    容量设计必须借助 TC2639/8AL90065USAG 或 ALE sizing 工具，本书不承担。
  conditions: 售前 sizing 与扩容规划
  tags: [out-of-scope, capacity, sizing]

- id: n31
  title: 实验拓扑的域名/公网/口令均为演示口径（al-mydemo.com / 195.128.146.x / 明文口令）
  type: limitation
  source_pages: p63-66, p30, p72, p91-92, p245
  source_chapter: 全书 How-To
  source_quote: |
    "https://ot-podx.al-mydemo.com … ot-podx.al-mydemo.com<->195.128.146.10x" (p63)
    "Username: Admin … Password: (Admin by default)" (p91-92)
    "Login: administrator Password: superuser" (p72)
  summary: |
    全书 How-To 绑定演示域 al-mydemo.com、公网段 195.128.146.10x、DMZ 11.1.1.x，且明文给出各系统口令
    （superuser、Admin/Admin、letacla1、Sdfghjk1 等，见 p08 条目）。这些值整体是"实验口径"：生产化时
    域名、公网资源、凭据全量替换，并按客户安全基线管理口令——书内无生产安全基线章节。
  conditions: 一切实验跟做与方案引用
  tags: [limitation, lab, credentials]

- id: n32
  title: 反代声明四 URL 与手机首启 URL 的书写细节：EVS 必须带 :8016 端口
  type: limitation
  source_pages: p63-64, p214, p216
  source_chapter: Reverse Proxy declaration / App first startup
  source_quote: |
    "EVS public URL: Enter the public URL of the OpenTouch server:8016 (e.g: https://ot-pod3.al-mydemo.com:8016)" (p64)
    "Public hostname or URL: Enter the public URL of the server (reverse proxy)" (p214)
  summary: |
    RP 申报的四个公共 URL 中，EVS（事件通知）必须带 :8016 端口，其余三个不带——漏写端口则通知类功能
    （漏接提醒等）经反代失效；手机端首启的 Public URL 必须填反代（公网）地址而非内网 OT 地址。推送/
    通知类"时好时坏"先核这对端口与地址。
  conditions: RP 申报与客户端接入配置
  tags: [limitation, urls, evs, notification]

- id: n33
  title: OTSBC 初装口令 Admin/Admin 与 OMS 口令 letacla1 属出厂/实验默认——首登必须处置
  type: warning
  source_pages: p91-92, p30
  source_chapter: OTSBC deployment / Login-Password summary
  source_quote: |
    "Login and password are 'Admin'." (p91)
    "OMS admin admin letacla1; root root letacla1" (p30)
  summary: |
    OTSBC（AudioCodes Mediant）CLI 与 webadmin 初始凭据 Admin/Admin；OMS 虚机 admin/root 口令 letacla1
    （实验口径，同时是 ALE 出厂常用默认的演示值）。这些默认口令出现在培训教材里等于公开——生产环境
    首登即改并纳入口令台账；审计存量系统时按此清单核对。
  conditions: 全部涉及系统的首次登录与安全基线核查
  tags: [warning, credentials, security]

- id: n34
  title: 智能手机"自动配置"不等于零手工：Entity 判别器与 COS 区域授权仍要人工核
  type: misconception
  source_pages: p180, p212
  source_chapter: Configuration and installation main steps / Additional manual management
  source_quote: |
    "Automatic configuration of these objects when a Smartphone is associated to a Connection user in order
    to simplify administrator tasks" (p180)
    "4 Additional manual management to do in OXE: 4.1. Entity configuration; 4.2. Public access COS
    configuration" (p212)
  summary: |
    "关联一次自动建 9 类对象"容易让人以为智能手机开卡是零手工；How-To 第 4 章标题即 "Additional manual
    management to do in OXE"——判别器逻辑→物理关联与公网接入 COS 区域授权两步必须人工做。宣传/交付话术
    里要把"自动+两处手工核验"说全。
  conditions: OTC smartphone 双模式开通
  tags: [misconception, smartphone, automatic-provisioning]

- id: n35
  title: 证书模板文件与反代模板的下载链接随 TC 版本漂移——必须用 TC2639 最新版链接
  type: version-trap
  source_pages: p220, p253
  source_chapter: Nginx reverse proxy deployment / Template files download
  source_quote: |
    "The required template files for the reverse proxy configuration are available at this address:
    http://nas.alcatel-support.com/index.php/s/0a26TOag6MaXHD9 … Notes: This link is coming from TC2639
    (or TC2257). Consult the last TC2639 edition to be sure to use the correct URL link and so to download
    the latest template files." (p220)
  summary: |
    书中给出的模板下载链接是 TC2639（或 TC2257）某版快照，官方明示"查最新版 TC2639 以确链接与模板文件
    正确"。Nginx 模板（V1.5）、OTSBC 向导模板、RP 模板（ed02）都会随版本迭代——凭本书 URL 或旧模板做
    生产，存在拿到过期配置结构的风险。
  conditions: Nginx/内嵌 RP 部署取模板时
  tags: [version-trap, templates, documentation]
```

---

## 收尾自检 — 对照 BOOK_OVERVIEW.md 14 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | 认知 RLAB 实验环境 | 有 → n31（实验口径总警示）、n33（默认口令） |
| task-02 | 规划远程接入拓扑 | 有 → n24（N.U./N.A. 语义）、n30（容量缺位）、n32（EVS 端口） |
| task-03 | 证书策略与签发 | 有 → n01（通用证书红线）、n04（Deploy 断线）、n05（CTL 重签） |
| task-04 | 服务器侧远程访问设置 | 有 → n02（DAS 顺序/国家）、n03（SAN+DNS 双强制）、n32（EVS 端口） |
| task-05 | 部署 OTSBC | 有 → n06（iPhone 手工强制）、n07（TCP 缺失）、n08（两种用户身份）、n33（默认口令） |
| task-06 | 内嵌 RP 部署 | 有 → n09（许可）、n10（LDAP 专用机器） |
| task-07 | Nginx RP 部署 | 有 → n10、n25（2.2 双 conf）、n26（Python 2）、n28（签名告警）、n29（笔误）、n35（模板链接漂移） |
| task-08 | VMware 虚机部署 | 有 → n27（vSphere 版本限制） |
| task-09 | 客户端远程接入 | 有 → n11（dial from 特例）、n32（URL 细节） |
| task-10 | OTC PC multi-devices | 有 → n12（COS 授权强制） |
| task-11 | OTC PC Nomadic SIP | 有 → n13（池强制/容量）、n14（默认口令 0000）、n15（双许可） |
| task-12 | 智能手机 Connection 用户 | 有 → n16（R2.6 分界）、n19（DDI）、n20（速拨范围）、n21（RE 号禁字母）、n22（判别器+barring）、n23（Android 无 SIM 代价）、n34（自动≠零手工） |
| task-13 | iPhone+ APNS 专项 | 有 → n06、n17（APNS 证书年更/根证书到期）、n18（多 invite/UDP/TCP 缓冲） |
| task-14 | 拨测验证 | 有 → n29（笔误清单影响对照）、n31（实验口径） |

**14/14 全部有边界类条目覆盖，无空缺。**

### 扫描完整性说明（Warning/Note/Tips 标记框逐页核对）

- 已全部入册的 Warning 框：p61（通用证书）、p67（DAS 顺序）、p68（SAN）、p70（内部 DNS）、p105/p117（iPhone 手工）、p140（LDAP 专用机器）、p153（COS 授权）、p158（Ghost Z 池）、p192（DDI 翻译表）、p212（判别器+barring 两处）、p268（CTL）、p274（vSphere 版本）、p248（包签名，作为教学口径警示入册）。
- 已入册的 Note/Tips 类边界：p76（Deploy 断线）、p114（Conversation/Connection）、p133（许可/实验可先测）、p147/150（dial from 特例）、p157（池规划）、p160（口令 0000）、p176（无 SIM 代价）、p182/204（R2.6 分界）、p183-184（APNS 证书年更/Geotrust 2022）、p185-187（多 invite/UDP/TCP）、p195（速拨范围）、p202（RE 禁字母）、p220（模板链接漂移）、p253（OTES 退场）、p257（Python 2）、p63-64（EVS:8016）。
- 复核后排除的纯操作提示框（非边界类，不构成候选）：p91/p110 Tips（OVF 附录、向导软件位置）、p133 Tips（实验无许可可测，已并入 n09 正文）、p141/p143 Tips（interface 可手工建/用查找替换改模板）、p144 Notes（按需重启）、p194 Tips（一个 RE 一个 ghost 更稳，已并入 c06 步骤 1⑦）、p254 Notes（nano 用法）、p258 Notes（dos2unix，已并入 p20 正文）、p263 Notes（-CAcreateserial/-CAserial 用法，已并入 c09 步骤 4）、p265-266（浏览器导入步骤，非边界）。
- 推断性结论标注：本文件各条 summary 均为原书事实或对原文的直接复述；n13（池空后果"无法游牧"）、n18（漏接排查指向）含轻度工程引申，其机制与依据均出自原文，无需额外"（推断）"标记；n30 的"容量在书外"为对全书缺目的归纳性结论（已由 BOOK_OVERVIEW 批判节独立声明）。
- 版本号均按原文保留完整位数：OpenTouch R2.2、R2.3.1、R2.5、R2.6；OTSBC 7.2；ESXi 6.0/6.5；Python 2/3；Ubuntu 16.04.3 LTS（xenial）。
