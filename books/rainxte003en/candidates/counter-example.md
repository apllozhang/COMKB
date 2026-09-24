# 反例/限制/边界/易错点候选 — Rainbow OmniPCX Enterprise (RAINXTE003EN Ed12)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: 电话服务必须有付费订阅——免费 Essential 无电话且无 SLA，也不能改路由
  type: limitation
  source_pages: p24, p56, p109, p129
  source_chapter: Rainbow Overview – Subscription plans / OXE users with Rainbow
  source_quote: |
    p24: "Rainbow Essential This free option is available to anyone who wants to try Rainbow for an unlimited period (no SLA)."
    p56: "Each member must have a subscription to use telephony services • Business • Enterprise • Attendant"
    p129: "With an 'Essential' subscription, the user can only use RCC feature. He cannot modify his routing."
  summary: |
    免费版 Essential 只能长期试用协作功能，无 SLA，也不含电话服务；要用话音必须 Business/Enterprise/
    Attendant 之一。OXE 线再加一层：Essential 只有 RCC、不能改路由，路由到手机/家庭号需要
    Business/Enterprise。WebRTC 网关使用同样要求 Business/Enterprise（p133）。
    开通时别把"免费可用"理解成"能打电话、能改路由"。
  conditions: 所有电话功能与网关开通场景
  tags: [limitation, licensing, subscription]

- id: n02
  title: 网络要求（端口/带宽/防火墙）全书外置，只给 PDF 指针
  type: out-of-scope
  source_pages: p26-31
  source_chapter: Network Requirements
  source_quote: |
    p27: "Find all network requirements on the Rainbow support site … 2 PDF files • Rainbow network
    requirements - Health data hosting • Rainbow network requirements"
    p31: "This document details: … Bandwidth requirements, Configuration of corporate network elements
    (DNS, Proxy, Firewall...)"
  summary: |
    端口/协议清单、带宽要求、Rainbow 域名与 IP 清单、企业网络设备（DNS/代理/防火墙）配置全部在
    《Rainbow Network Requirements》PDF 里，书内只有链接和摘要。交付前必须按该 PDF 全文核查，并配合
    Rainbow Pilot 工具（pilot.openrainbow.com）做连通性与容量评估；教材不承担网络前提的展开。
  conditions: 任何站点上线前
  tags: [out-of-scope, network]

- id: n03
  title: 培训环境只许 Monthly 订阅，禁用预付（Voice 与 Attendant 两处警告）
  type: warning
  source_pages: p57, p239
  source_chapter: Subscriptions / How-To Attendant console
  source_quote: |
    p57: "During LAB Use ONLY Voice MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID!!!"
    p239: "DON'T USE 'PREPAID' IN THE TRAINING"
  summary: |
    培训/实验环境只允许按月（MONTHLY）订阅，Voice 与 Attendant 两处都明令禁止预付（1/3/5 年
    PREPAID），否则实验许可无法按预期调整和回收。这是培训场景规则，生产环境预付是正常计费方式；把
    实验习惯带进生产、或把生产做法带进实验，都会踩坑。
  conditions: RLAB/虚拟课堂实验环境
  tags: [warning, training, licensing, subscription]

- id: n04
  title: 培训邮箱两坑——Rainbow 邮件可能进 SPAM；必须点邮件底部 JOIN 按钮而非开头链接
  type: warning
  source_pages: p63-65
  source_chapter: How-To Rainbow accounts configuration and use
  source_quote: |
    p63: "Warning CHECK THAT E-MAILS SEND BY RAINBOW PLATEFORM ARE NOT TRUSTED AS SPAMS."
    p65: "Warning CLICK ON 'JOIN BUTTON' AT THE BOTTOM OF THE E-MAIL AND NOT ON THE LINK AT THE
    BEGINNING."
  summary: |
    邀请开户两个易错点：①Rainbow 平台发的邮件可能被判为垃圾邮件，核收前先翻 SPAM；②邀请邮件里有两处
    链接，完成入司必须点底部的 "JOIN BUTTON"，点开头的链接走不通。生产场景同样要先确认客户邮件网关
    放行 noreply@openrainbow（p97 提到邀请邮件发件人）。
  conditions: 邀请式开户、enrollment 邮件验证
  tags: [warning, members, invitation, email]

- id: n05
  title: 删除成员有 10 天宽限期——同名重建会报错；恢复后降级 Essential
  type: limitation
  source_pages: p97, p103
  source_chapter: Members creation / Members deletion
  source_quote: |
    p97: "If you get an error message about the e-mail address you wish to use, please check that it is
    not already the identifier of a user deleted less than 10 days ago (grace period)."
    p103: "When you delete a user, his or her status becomes 'Suspended' for a period of 10 days … If you
    restore it, it will default to 'Essential' (free) mode, so you'll need to reallocate the appropriate
    license … reassign the user's telephone line."
  summary: |
    删除成员后账号 "Suspended" 10 天（grace period）：①这 10 天内同一邮箱不能再建新用户（报邮箱不可用
    错误，先查 10 天内是否删过人）；②恢复用户后订阅已清、默认 Essential，要重新分配许可并重挂话机线。
    批量导入/交接场景要特别注意宽限期内的邮箱占用。
  conditions: 成员删除/恢复/同名重建
  tags: [limitation, members, lifecycle]

- id: n06
  title: 服务级别硬门槛——SSO 需 Enterprise、AAD 导入需 Voice Enterprise、频道创建需 Enterprise
  type: limitation
  source_pages: p44, p96, p52
  source_chapter: SSO & Authentication / Members Creation / Information Channels
  source_quote: |
    p44: "The administrator must have an 'Enterprise' service level"
    p96: "Import via Azure Active Directory is reserved for administrators with 'Voice Enterprise' service level"
    p52: "Only users with an 'Enterprise' service level can create Information Channels."
  summary: |
    三处硬门槛：配置 SSO 的管理员必须 Enterprise 级；Azure AD 批量导入/同步只对 Voice Enterprise 级
    管理员开放；信息频道只有 Enterprise 级能创建。非列表认证方式（其他 SAML V2/OIDC 产品）须经 ALE
    确认（p44 NB）。操作前先核查操作者的订阅级别，别让低级别管理员白折腾。
  conditions: SSO/批量导入/频道创建操作前
  tags: [limitation, licensing, sso, azure-ad, channel]

- id: n07
  title: BP 专属动作（建 PBX/开订阅/激活网关）EC 管理员做不了——实验中由讲师代做
  type: limitation
  source_pages: p39, p161
  source_chapter: 2 types of companies / Deploy WebRTC gateway How-To
  source_quote: |
    p39: "However, the following actions can only be performed by the BP: • Declaration & PBX • Opening of
    paid subscriptions."
    p161: "Warning For this lab your account is a customer administrator and not a BP one — you have no
    access to these parameters — It will be managed by the trainer."
  summary: |
    申报与创建 PBX、开通付费订阅、在 PBX 设置里勾 "Activate WebRTC gateway" 都是 BP 专属；EC 管理员
    界面上无此入口，实验里由讲师代做。现场客户管理员"点不出"这些功能是权限体系设计而非故障；完整交付
    路径必须协调 BP 账户参与。
  conditions: EC 管理员视角、网关激活、订阅开通
  tags: [limitation, bp, licensing, webrtc-gateway]

- id: n08
  title: ISOLATED 可见性不推荐——用户无法被外部 bubble 邀请
  type: warning
  source_pages: p43
  source_chapter: Privacy & Visibility
  source_quote: |
    "This 'isolated' mode is not recommended as it is very restrictive. Please check the impacts before
    applying it to your company. In particular, your users will no longer be able to be invited to
    conferences (bubbles) external to your organization. … Get into the habit of systematically setting
    the 'closed' mode as soon as you create a Rainbow company."
  summary: |
    ISOLATED 让公司用户对外完全不可见且不可被邀请，直接后果是无法被外部组织拉进 bubble 会议。教材明确
    不推荐。拿不准就用 CLOSED（对外不可见但可通过邮箱邀请），建司时默认设 CLOSED 即可；已选 ISOLATED
    的要先向客户确认外部协作诉求。
  conditions: 创建或调整公司可见性时
  tags: [warning, company, visibility]

- id: n09
  title: 强制订阅的公司信息频道成员无法退订
  type: limitation
  source_pages: p52
  source_chapter: Information Channels
  source_quote: |
    "The members you choose in your company will automatically be subscribed to these channels. Members
    will not be able to unsubscribe."
  summary: |
    公司级信息频道一旦设为自动订阅（选中成员或全员），成员端不能自行退订。给全员推频道前先确认内容会
    长期维护，否则频道会变成无法退出的骚扰源。
  conditions: 创建公司级信息频道并选择强制订阅范围时
  tags: [limitation, channel]

- id: n10
  title: DNS/代理只服务 Rainbow 与 Cloud Connect agent；URL ping 不能证明 DNS 解析
  type: warning
  source_pages: p78, p82
  source_chapter: DNS and proxy configuration
  source_quote: |
    p78: "The DNS and HTTP proxy configuration will only be used by Rainbow and Cloud Connect agents."
    p82: "Warning URL PING DOESN'T VALID THE DNS RESOLUTION. Dig and nslookup commands allow to verify
    correctly the DNS resolution."
  summary: |
    两个认知纠偏：①netadmin 里的 DNS/HTTP 代理配置只被 Rainbow 与 Cloud Connect agent 使用，不影响
    OXE 其他功能——配完没全局生效属预期；②验证 DNS 解析必须用 nslookup/dig，ping 通 URL 不代表解析
    正确。排障时先分清"解析问题"与"连通问题"。
  conditions: OXE 接入 Rainbow 前的网络验证
  tags: [warning, dns, proxy, netadmin]

- id: n11
  title: OXE 的 HTTPS 连通测试只能用 IP@；curl 报证书错误不代表连接失败（ALE 专有证书）
  type: misconception
  source_pages: p82
  source_chapter: DNS and proxy configuration / 3.2 HTTP test
  source_quote: |
    "Warning OXE ALLOWS HTTPS TEST USING IP@ ONLY. THE FOLLOWING TEST MAY BE NOT POSSIBLE ON SITE, IF
    FIREWALL/PROXY REQUIRES A DOMAIN."
    "curl: (77) error setting certificate verify locations … The request is OK but curl returns a message
    to indicate that the web server certificate cannot be verified. … The certificate provided by the
    agent.openrainbow.com is an ALE proprietary certificate only recognized/accepted by an OXE/OXO system.
    Any classic web browser (as curl) will provide an error as it doesn't know the CA."
  summary: |
    两个易误判点：①OXE 侧 HTTPS 测试只能用 IP 地址——现场防火墙/代理若强制按域名放行，这个测试本身
    就做不了，需换手段；②curl/浏览器访问 agent.openrainbow.com 报证书错误是预期行为：证书是 ALE 专有
    CA 签发、只有 OXE/OXO 认，"报错但请求 OK"。别把证书报错当成"连不上 Rainbow"的证据。
  conditions: 接入前连通性验证、现场防火墙核查
  tags: [misconception, certificate, connectivity, troubleshooting]

- id: n12
  title: 接入 Rainbow 前网络前提必须先完成；激活码用于首次连接、PBXID 由 Rainbow 生成
  type: warning
  source_pages: p84, p85
  source_chapter: OXE connection with Rainbow
  source_quote: |
    "Warning NETWORK PREREQUISITES MUST BE COMPLETED BEFORE!"
    "Rainbow PBXID The Rainbow ID is generated by Rainbow. It will be provided by the rainbow
    administrator. … These credentials must be used for PBX agent configuration"
  summary: |
    接入顺序硬约束：网络前提（DNS/代理/防火墙）没就绪就去填 PBXID+激活码，只会得到连不上的假故障。
    PBXID 与激活码都由 Rainbow 平台生成、由 Rainbow 管理员提供（我的公司/Communication/Comm. Servers
    查询），激活码用于首次连接；Tips 建议用复制功能防输错。
  conditions: OXE 接入 Rainbow 操作前
  tags: [warning, rainbow-agent, pbxid, prerequisite]

- id: n13
  title: 路由不是转发（Call Routing is not a Forwarding）——RCC 监督与 REX 路由是两套机制
  type: misconception
  source_pages: p109, p114
  source_chapter: OXE users with Rainbow
  source_quote: |
    "The physical device is set in tandem with a Remote Extension (REX) • Call routing is possible: ability
    to reroute calls to another external destination • Call Routing is not a Forwarding"
    "REX configured with a mobile number if managed in user's profile* • RCC on deskphone not possible"
  summary: |
    三个易混点：①呼叫路由（改 REX 指向的外部目的地）与呼叫转发（forwarding）是 OXE 两个不同机制，别
    用 forwarding 的思路排路由问题；②来话时 REX 若已改写到外部号码，来话不会振 Rainbow 客户端（音频走
    外部目的地）；③REX 指向手机号时话机侧的 RCC 摘机不可用。用户抱怨"我在 Rainbow 上接不了电话"先查
    当前路由选择。
  conditions: 无网关阶段与网关阶段都成立
  tags: [misconception, routing, rex, rcc]

- id: n14
  title: DECT 话机不能与 REX 直接 tandem——须建 Virtual UA，且 Virtual UA 不能被 RCC 控制
  type: limitation
  source_pages: p139
  source_chapter: The different user types (DECT case)
  source_quote: |
    "The DECT device cannot be set up in tandem with a REX (OXE management limitation) • It is necessary to
    create a Virtual UA type device which will be set in multi-devices configuration with the DECT and the
    REX … The Virtual UA becomes the main device of the tandem and usually requires the DECT device to be
    recreated … Please note: It is not possible to control the Virtual UA device in RCC."
  summary: |
    仅 DECT 话机的用户要上 Rainbow 路由，路径比普通话机用户多三步且有两个代价：①DECT 不能直接与 REX
    tandem（OXE 管理限制），必须新建 Virtual UA 设备做 multi-devices（DECT+REX）；②Virtual UA 成 tandem
    主设备，通常要重建 DECT；③Virtual UA 不能被 RCC 控制——用户从 Rainbow 客户端控制话机的能力在这个
    形态下没有了。售前评估 DECT 站点时要把这些代价讲清。
  conditions: 参考 TC2462；涉及重建话机属变更操作
  tags: [limitation, dect, rex, virtual-ua]

- id: n15
  title: 网关三重前提缺一不可——PBX 已接入、用户已关联、OXE 版本 ≥12.1 MD4/12.2
  type: version-trap
  source_pages: p133, p135, p154
  source_chapter: WebRTC Gateway overview / Deploy How-To warning
  source_quote: |
    "Use of the WebRTC Gateway requires a BUSINESS or ENTERPRISE subscription for a member" (p133)
    "Require OXE release 12.1 MD4, 12.2 or later" (p135)
    "Warning • THE PBX MUST BE CONNECTED TO RAINBOW • USERS DECLARED IN THE RAINBOW COMPANY MUST HAVE
    THEIR OXE TELEPHONE NUMBER ASSOCIATED TO THEIR RAINBOW ACCOUNT" (p154)
  summary: |
    版本与顺序双重陷阱：OXE 版本低于 12.1 MD4/12.2 不能部署网关；部署顺序上 PBX 必须先连 Rainbow、
    用户必须先做分机关联，顺序颠倒网关装了也没用。存量低版本站点要先把版本升级排进计划。
  conditions: 网关部署前置核查清单
  tags: [version-trap, webrtc-gateway, prerequisite, oxe]

- id: n16
  title: 网关 VM 模板默认 QWERTY 键盘；配置输错 IP 可用 mpnetwork 重来，重启才生效
  type: warning
  source_pages: p155-156
  source_chapter: Deploy WebRTC gateway How-To / 3.1-3.2
  source_quote: |
    "The virtual machine template is generated with a QWERTY keyboard. It can be necessary to update it
    according to your location. … Login: kb Password: kb"
    "To take in account the new parameters, the system must reboot. If it doesn't reboot automatically, do
    it manually using 'reboot' command."
  summary: |
    两个部署细节坑：①VM 模板键盘是 QWERTY，非美式布局现场输命令/密码容易错字符——先用 kb/kb 登录改
    键盘；②mpnetwork/mpconfig 改完参数要确认 y 且重启才生效（不自动重启就手动 sudo reboot）；关机用
    sudo halt 优雅停（p158 Notes）。
  conditions: 网关 VM 首次配置
  tags: [warning, webrtc-gateway, deployment, keyboard]

- id: n17
  title: mpcheck 的 GEOIP/STUN-TURN 段 [FAILED] 未必是故障——GEOIP 文件缺失先看 Rainbow connect 段
  type: misconception
  source_pages: p160
  source_chapter: Deploy WebRTC gateway How-To / 3.4 Configuration checking
  source_quote: |
    "STUN/TURN test will be done using GEOIP config … GEOIP file not found, make sure RAINBOW connect test
    is OK … [FAILED] 20220317-172300 GEOIP config"
  summary: |
    书中自己的"成功"输出里 mpcheck 的 GEOIP 段就是 [FAILED]——原因是 GEOIP 文件未下载（提示先确认
    Rainbow connect 段 OK）。别一看到 [FAILED] 就判网关部署失败；逐段看：Network/Rainbow settings/DNS/
    Rainbow connect/TLS/PBX_DOMAIN ping/SIP OPTIONS/registration 才是主干。TURN 生产位置选择在书外
    （TURN_SERVER=GEOIP 为默认口径）。
  conditions: 网关部署核验与排障
  tags: [misconception, mpcheck, turn, troubleshooting]

- id: n18
  title: 网关激活与升级是 BP 权限；远程升级有版本与地域门槛、独立 PC 被排除
  type: version-trap
  source_pages: p161, p164, p168-170, p173
  source_chapter: Deploy / Upgrade WebRTC gateway
  source_quote: |
    p164: "Guide applies to WebRTC gateway installations on VM and standalone PCs since version 1.67.6-121
    (MANUALLY) … REMOTE … since version 1.73.x or higher. Available for 35 countries – list in the procedure."
    p170: "The current status is that some standalone PCs do not boot after a reboot without a connected
    display or keyboard. Therefore, these WebRTC gateways are excluded from the remote update."
    p168: "The Software is subject to export control regulations, you must accept the Specific Terms and
    Conditions before the upload can start."
  summary: |
    升级路径四个边界：①远程升级需 BP 管理员账户在 Rainbow Web 端操作；②远程法适用网关版本 1.73.x+
    且仅 35 国（清单在在线文章，会变）；③无显示器/键盘重启可能起不来的独立 PC（NUC 类）被排除在远程
    升级外，只能走手动 mpupgrade；④上传前必须接受出口管制条款，下载被代理拦截时用 Abort 按钮重试。
    手动法自 1.67.6-121 起适用。
  conditions: 网关升级规划
  tags: [version-trap, webrtc-gateway, upgrade, bp]

- id: n19
  title: 网关正常工作要求"无压缩但带压缩资源（GD/OMS）"的 IP 域——压缩配置会导致工作异常
  type: warning
  source_pages: p180
  source_chapter: OXE configuration for WebRTC gateway use / 2.1 IP domain prerequisite
  source_quote: |
    "AN IP DOMAIN WITHOUT COMPRESSION BUT WITH COMPRESSION RESOURCES (GD/OMS) IS REQUIRED ON THE SYSTEM
    FOR A CORRECT WORKING MODE OF THE WEBRTC GATEWAY. … Intra domain bandwidth High bandwidth • Extra
    domain bandwidth High bandwidth"
  summary: |
    OXE 侧 IP 域配置是隐性前提：承载网关流量的 IP 域必须设为"无压缩"（Intra/Extra domain bandwidth =
    High bandwidth），同时系统要有压缩资源（GD/OMS）存在。存量站点若已把域配成压缩模式，网关会工作不
    正常且表象分散（单通/媒体异常），排障容易走偏——先查域配置。
  conditions: OXE 侧网关配置第一步核查项
  tags: [warning, webrtc-gateway, ip-domain, compression]

- id: n20
  title: 4059EE 关联话机必须非 multi-line——与 tandem 场景的 multi-line 要求正好相反
  type: warning
  source_pages: p209, p124
  source_chapter: Call distribution and attendants How-To
  source_quote: |
    p209: "WARNING: This extension must not be multi-line, as it will be associated to the 4059 IP
    attendant (multiline set is incompatible with 4059 IP attendant)."
    p124: "Multi-lines are required on extensions part of a tandem."
  summary: |
    同一部 OXE 话机，两种场景要求相反：做 REX tandem 的成员（主站与副站）必须配 multi-line（≥2 线），
    而 4059EE 话务台的关联话机（Associated phone set）绝对不能是 multi-line。复用实验话机或规划现场景
    时先把话机角色定清楚，否则 4059 注册不上或 tandem 建不成。
  conditions: 话机角色规划（tandem 成员 vs 话务台关联话机）
  tags: [warning, 4059ee, multi-line, tandem]

- id: n21
  title: Rainbow 在场状态与电话状态是两个独立信息——BLF 监督时两边可不同
  type: misconception
  source_pages: p204, p221, p223-224
  source_chapter: 4059EE Rainbow integration / Busy Lamp Field
  source_quote: |
    p204: "Warning - Rainbow and phone status are two distinct things and can be different"
    p221: "Warning Don't confuse the Rainbow (presence) status with the telephone status. They are (can be)
    different."
  summary: |
    4059EE/BLF 界面上同时呈现 Rainbow 在场（Online/Away/DND/Invisible）与电话状态（话机空闲/占用），
    两者来自不同数据源、可以不一致（书中专门设计了两条测试验证）。用户报"话务台显示我在忙但我没打电话"
    时，先分清看的是哪一列，别当故障处理。
  conditions: 4059EE BLF 与 Rainbow 话务台监督场景
  tags: [misconception, presence, blf, 4059ee]

- id: n22
  title: 4059EE 安装三坑——不装 ALCATEL USB 键盘（RLAB）、防火墙放行 abcacom.exe、IPDSP 先 in service
  type: warning
  source_pages: p211-212
  source_chapter: Call distribution and attendants How-To / Installation
  source_quote: |
    "The IPDSP must be in service before 'connecting' from the 4059EE IP." (p211)
    "Warning In RLAB mode (Virtual machine for the PC) don't install of the ALCATEL USB Keyboard." (p212)
    "Warning Before launching the application, be sure to have allowed the 4059 EE application in your
    firewall rules along with 'abcacom.exe' (or you can turn off completely the firewall in this training
    context)" (p212)
  summary: |
    4059EE 装机顺序与三个坑：①关联的 IPDSP 必须先 in service 再从 4059EE 连接，顺序反了注册失败；
    ②RLAB/虚机环境不要装 ALCATEL USB 键盘组件；③应用启动前防火墙要放行 4059 EE 与 abcacom.exe（培训
    语境可整体关防火墙，生产必须做放行规则）；④改设置要以管理员身份运行。另：多呼叫服务器冗余时设备
    地址可填最多 3 个主机名（逗号/分号分隔，格式 [话务员号]@[主机名]，p213）。
  conditions: 4059EE 交付现场
  tags: [warning, 4059ee, installation, firewall]

- id: n23
  title: 互助组/监督组代接边界——仅限同 PBX 电话呼叫，Rainbow 软终端呼叫不可代接；同时最多监督 4 路
  type: limitation
  source_pages: p232, p234-236
  source_chapter: Miscellaneous / Mutual aid supervision group
  source_quote: |
    p232: "All phone calls are handled by the PBX • Interception is only possible if supervisors and
    supervisees are on the same PBX. Only phone calls can be intercepted."
    p234: "You can pickup calls. Works only for PBX calls, not for Rainbow softphone calls"
    p235: "Up to 4 calls supervised"
  summary: |
    监督/互助组的四条硬边界：①拦截代接只对 PBX 电话呼叫有效，Rainbow 软终端（computer 路由）来的呼叫
    不可代接；②监督员与被监督者必须同一 PBX；③同时最多监督 4 路呼叫；④组类型（Mutual aid group）与
    双方 In/Out 权限创建时定死，锁定成员不能退出组。售前演示"帮我接一下"场景前先核这四条。
  conditions: 监督组/互助组使用场景
  tags: [limitation, mutual-aid, pickup, boundary]

- id: n24
  title: Attendant 订阅只用于 Rainbow 内嵌话务台，与 4059EE 无关；话务台功能仅 PC 端
  type: misconception
  source_pages: p200, p227, p232
  source_chapter: 4059EE Rainbow account / Rainbow Attendant Console
  source_quote: |
    p200: "Please note that the 'Attendant' subscription is only dedicated to the use of the 'Attendant
    console' embedded in the Rainbow application, not related to the 4059EE."
    p232: "Attendant features are only available on PC (thick client or web mode)."
  summary: |
    两套话务台易混点：①4059EE 是 OXE 传统话务台应用，不需要也不使用 Rainbow "Attendant" 订阅（它只用
    一个普通 Rainbow 账户取在场信息）；②Rainbow 内嵌 Attendant console 才需要每人 Attendant 订阅，且
    功能只在 PC（客户端/Web），话机与手机上没有话务台功能；③队列容量两套不同：Rainbow 话务台 OXE 10
    路/OXO 8 路，4059EE 的话务组溢出门限由 Max. No. of Calls Bef. Overfl. 决定。报价与授权时别把订阅
    安到 4059EE 头上。
  conditions: 话务台选型与许可规划
  tags: [misconception, attendant, licensing, 4059ee]

- id: n25
  title: Teams 集成 Desktop 硬依赖——Desktop 未装/未运行则 Teams 内应用显示 "!"；SSO 非必需
  type: warning
  source_pages: p272, p302-304
  source_chapter: Deployment principle / Rainbow for Teams connector How-To
  source_quote: |
    p302: "THE RAINBOW APPLICATION INTEGRATED INTO TEAMS REQUIRES THE INSTALLATION AND STARTUP OF THE
    RAINBOW DESKTOP APPLICATION ON THE PC."
    p303: "Warning The application must be present on the PC"
    p304: "Important SSO is not required to use the Rainbow/Teams connector."
  summary: |
    Teams 集成最容易翻车的依赖：Rainbow Desktop 必须安装且运行，否则 Teams 内应用一直显示 "!" 图标、
    打不了电话——排障第一步查 Desktop 进程。两个衍生澄清：①Desktop 首次登录可用 Microsoft 凭据 SSO，
    但 SSO 并非连接器必需条件；②权限未预先同意时用户首次 Sign in 会被要求自行接受（先做管理员预同意
    可免全员弹窗，见 c12 方式 A）。
  conditions: Teams 集成最终用户侧
  tags: [warning, teams, desktop, dependency]

- id: n26
  title: 书内不一致——user2 邮箱在两个实验章用了不同姓名（Rains Robby vs Betty Carol）
  type: limitation
  source_pages: p64, p216
  source_chapter: How-To Rainbow accounts / How-To Call distribution and attendants
  source_quote: |
    p64: "Login : cCpP.user2@ale-training.com … Last name: Rains / First name: Robby"
    p216: "Add the new following RAINBOW user: — Login: cCpP.user2@ale-training.com … Name : Betty —
    Firstname : Carol"
  summary: |
    同一实验邮箱 cCpP.user2@ale-training.com 在 p64（账户章）登记为 Rains Robby、在 p216（4059 章）又
    要建为 Betty Carol，书中未解释（推断：不同 lab 的示例人物沿用同一邮箱模板）。照书逐字复现实验会在
    第二次建号时撞邮箱/改名困惑——实操时按自己 POD 的实际状态建或复用即可，勿把姓名当考核点。
  conditions: 实验复现（推断性结论，标注推断）
  tags: [limitation, lab, inconsistency]

- id: n27
  title: ARS 溢出的兜底语义——网关流量上限参数留空时由 SIP trunk 限制决定溢出
  type: limitation
  source_pages: p149
  source_chapter: Shared and scalable WebRTC gateway / ARS
  source_quote: |
    "The maximum traffic for each WebRTC is managed in the RAINBOW interface … If this parameter is empty,
    the SIP trunk limit will determine the overflow."
  summary: |
    池化溢出有个隐蔽分支：Rainbow 界面里每网关的最大并发流参数如果留空，溢出触发条件自动降级为"SIP
    trunk 限制"——trunk 配多少路就承载多少，网关池的弹性容量设计会悄悄失效。做共享池交付时把该参数
    填值列为核查项，并在变更单里记录。
  conditions: 共享网关池配置核查
  tags: [limitation, webrtc-gateway, ars, overflow]

- id: n28
  title: OXE 维护命令的语境边界——sipextgw/lookars/traced/multidevice 各管一段，莫混用
  type: limitation
  source_pages: p191-195
  source_chapter: OXE configuration for WebRTC gateway use / 6 Maintenance
  source_quote: |
    "Use 'sipextgw' command to display the status of SIP external gateways … ARS can be checked using
    lookars command and specially using interactive mode … For more information about maintenance, consult:
    VoIP calling Troubleshooting guide (WebRTC Gateway) • TC 2462"
  summary: |
    OXE 侧排障命令各有语境：sipextgw -l 只看外部 SIP 网关在服/退服；lookars i 模拟指定时间的主叫解析
    （输错日期会用系统时间）；traced 抓 SIP 信令要配合 motortrace 并用 killall traced 停、重定向落盘；
    multidevice/zdpost/remotesets 只验 tandem/multi-device 与 REX 内容。更深排障在书外——VoIP calling
    Troubleshooting guide（support.openrainbow.com）与 TC2462。命令输出与示例中的 IP/号码/ExtNbr 均为
    实验口径。
  conditions: OXE 侧网关排障
  tags: [limitation, maintenance, commands, troubleshooting]

- id: n29
  title: 状态页与 SR 的使用边界——订阅告警按地域过滤；ESR 只为 Rainbow 认证伙伴创建
  type: limitation
  source_pages: p249-250, p254
  source_chapter: Cloud service availability / Access to Rainbow support
  source_quote: |
    p249: "If you subscribe to alerts, you can filter by relevant topics and/or geographical areas. For
    France, it is useful to tick WW, EMEA & DE."
    p254: "The ESR will only be created if the partner is certified on Rainbow"
  summary: |
    两条运维边界：①status.openrainbow.com 订阅告警要按主题/地域勾选（法国建议勾 WW+EMEA+DE），漏勾会
    收不到相关事件；计划维护通知按地域与架构（Hybrid/Hub）过滤，多在晚间周末执行。②报障入口虽多
    （邮箱/Emily BOT/Welcome Center/电话），但 ESR 只为持 Rainbow 认证的伙伴创建——没认证的客户侧只能
    通过认证伙伴转报。
  conditions: 运维值守与报障流程
  tags: [limitation, support, status, sr]

- id: n30
  title: 网页端问题上报不采集日期——浏览器日志短期留存，取证据要趁早
  type: limitation
  source_pages: p248
  source_chapter: Problems reported by your users
  source_quote: |
    "* In web mode, the date is not requested because the logs in a browser are short-lived. … The
    integrator partner has the same reports as the customer, so he can help with end user support."
  summary: |
    用户通过 "Report a problem" 上报时：桌面/移动端要填日期时间，Web 端不要填——浏览器侧日志留存期短，
    拖几天再取证就没了。集成商账号与客户管理员看到同一份上报列表（含事件日志下载），帮最终用户支持时
    第一时间是进平台取事件日志。
  conditions: 用户报障取证
  tags: [limitation, support, logs, web]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 19 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 网络前提与 Pilot | 有 → n02（网络要求外置） |
| task-02 公司体系 | 有 → n06（服务级别门槛）、n07（BP 专属）、n08（ISOLATED）、n09（频道强制订阅） |
| task-03 管理员权责/目录/频道 | 有 → n06、n09 |
| task-04 订阅开通与分配 | 有 → n01（Essential 边界）、n03（培训禁预付） |
| task-05 RLAB/OXE 实验环境 | 无独立反例条。实验口径纪律已全局标注（文件头注） |
| task-06 DNS/代理配置 | 有 → n10（DNS/代理语义）、n11（HTTPS 测试与证书误判） |
| task-07 OXE 接入 | 有 → n12（接入顺序与凭证） |
| task-08 成员管理 | 有 → n04（邮箱两坑）、n05（宽限期） |
| task-09 分机关联与 RCC | 无独立反例条。RCC 行为边界并入 n13（路由≠转发） |
| task-10 用户形态决策 | 有 → n13、n14（DECT 特例） |
| task-11 远程延伸配置 | 有 → n13、n14、n20（multi-line 反向要求） |
| task-12 网关部署 | 有 → n15（三重前提）、n16（键盘/重启）、n17（GEOIP 误判）、n19（IP 域压缩） |
| task-13 网关升级 | 有 → n18（升级门槛与排除项） |
| task-14 OXE 网关配置 | 有 → n19、n27（溢出参数）、n28（命令语境） |
| task-15 共享池与容量 | 有 → n27 |
| task-16 4059EE 话务台 | 有 → n20、n21、n22、n24、n26（书内不一致） |
| task-17 Attendant/互助组 | 有 → n23（代接边界）、n24 |
| task-18 维护体系 | 有 → n29（状态页/SR 边界）、n30（Web 端取证） |
| task-19 Teams 集成 | 有 → n25（Desktop 硬依赖） |

**统计**：30 条（warning 11 / limitation 11 / misconception 5 / version-trap 2 / out-of-scope 1；另含 1 条书内不一致记录 n26，1 条推断性结论已标注）；19 项任务中 17 项有反例类条目覆盖，task-05 无专用条（实验口径已全局标注）、task-09 并入 n13。
