# 反例/限制/边界/易错点候选 — OpenTouch Advanced (OPENXTE301EN Ed08, R2.6.1)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: Nomadic 从 OTC PC 激活必须先配 Desktop 许可
  type: limitation
  source_pages: p46
  source_chapter: OTC PC nomadic How-To
  source_quote: |
    "Tips Note that a 'Desktop' license must be assigned to the user to be able to activate nomadic mode from
    OTC PC desktop client"
  summary: |
    蜂窝与 VoIP 两种 nomadic 模式都要求用户持有 Desktop 许可，缺许可时 OTC PC 上 nomadic 入口不出现。
    排障"用户看不到 nomadic 菜单"先查 Licenses 页签（蜂窝另需 Nomadic GSM、VoIP 另需 Nomadic SIP）。
  conditions: 所有 nomadic 激活场景
  tags: [limitation, licensing, nomadic]

- id: n02
  title: VoIP nomadic 以蜂窝模式管理为前提
  type: warning
  source_pages: p51
  source_chapter: OTC PC nomadic How-To — Nomadic in VoIP mode
  source_quote: |
    "Warning The management done for nomadic in cellular mode shown in the previous step is a pre-requisite."
  summary: |
    配置 VoIP nomadic 前，蜂窝模式的全部管理（Ghost Z 池、权限、OT 侧范围登记）必须已完成。
    跳过蜂窝直接配 VoIP 会导致资源/权限链缺失，排障时按"先蜂窝后 VoIP"顺序核查。
  conditions: VoIP nomadic 配置
  tags: [warning, nomadic, dependency]

- id: n03
  title: 同事号码不能用作 nomadic 目的号码
  type: limitation
  source_pages: p50
  source_chapter: OTC PC nomadic How-To — Phone numbers configuration
  source_quote: |
    "Tips It is possible to specify an internal number for home and personal mobile phone numbers. Colleague
    number cannot be used for nomadic mode. But, it is possible to enter any desired number"
  summary: |
    Home/Mobile 字段可填内部号码或任意号码，唯独不能填同事（公司内部其他用户）的号码。
    用户要求"转到我同事座机"时该需求不被 nomadic 支持（改路由档案/呼叫转移另行实现）。
  conditions: nomadic 号码管理配置
  tags: [limitation, nomadic, routing]

- id: n04
  title: Desksharing 的 UA 软件话机不兼容 WAN 与 OTC Mac
  type: limitation
  source_pages: p61
  source_chapter: Desksharing (lecture)
  source_quote: |
    "Restriction: UA software not compatible on Wan, so not available with remote worker, unless VPN
    connectivity is used • UA software not compatible on OTC Mac"
  summary: |
    Desksharing 场景下 OTC PC 上的 UA 软话机（替代已登出话机做 nomadic）有两个硬边界：WAN 直连不可用
    （必须 VPN）；Mac 版 OTC 不支持。远程员工方案设计时别把"Mac + 共享工位"写进承诺。
  conditions: OTC PC + Desksharing + nomadic 组合
  tags: [limitation, desksharing, mac, vpn]

- id: n05
  title: Ghost Z/SIP 设备在 nomadic 期间全程占线，规划只看并发数
  type: limitation
  source_pages: p47, p51
  source_chapter: OTC PC nomadic How-To
  source_quote: |
    "Ghost Z sets are retained as busy throughout the connection and are only released when nomadic mode is
    disabled. ... it is very important to know how many Nomadic connections will be established simultaneously"
    "SIP devices & Ghost Z sets are retained throughout the nomadic mode connection and are only released when
    nomadic mode is disabled by the user"
  summary: |
    资源不是通话结束就释放，而是用户关闭 nomadic 才释放——挂机状态也占资源。用户"挂着 nomadic 不用时"
    会持续消耗池；池满后新用户无法激活。容量=最大并发连接数，且要向用户宣导用完关闭。
  conditions: nomadic 蜂窝/VoIP 容量规划与"激活失败"排障
  tags: [limitation, nomadic, capacity, ghost-z]

- id: n06
  title: DSU 必须为 OT 数据库所知，否则要补 OT Applications 权限
  type: warning
  source_pages: p72
  source_chapter: DeskSharing How-To — OTC PC configuration
  source_quote: |
    "Warning MAKE SURE THAT THE 'DSU' USER ('BARKLEY') IS KNOWN IN THE OPENTOUCH DATABASE; IF UNKNOWN, PLEASE
    ASSIGN THE RIGHT TO USE 'OT APPLICATIONS' TO THIS USER."
  summary: |
    让 OTC PC 远程释放 DSS 的前提是 DSU 用户已在 OT 数据库中；未知用户需先授 "OT Applications" 权限，
    否则 OTC PC 侧远程登出功能不可用。OXE 侧建好的 DSU 不等于 OT 侧可用。
  conditions: OTC PC + Desksharing 集成
  tags: [warning, desksharing, ot-database]

- id: n07
  title: Allow Reset of Busy DSU 的行为分支——6004 事件、Unauthorized 提示、通话中不自动登出
  type: limitation
  source_pages: p71
  source_chapter: DeskSharing How-To — System parameters
  source_quote: |
    "Allow Reset of Busy DSU True: if a DSU is busy (on line), the call is released and it can be log off (by
    automatic log off or log on from another DSS). An incident '6004' is generated. False: the log off is not
    done and the conversation is maintained. In case of log on from another DSS, a message 'Unauthorized' is
    displayed. In case of automatic log off, if the DSU is in communication, the DSU stays log on"
  summary: |
    忙时重置参数三种行为要向客户讲清：True=强制挂断通话并登出（产生 6004 事件）；False=另一台 DSS 登录时
    显示 Unauthorized、定时登出时若在通话则保持登录。选 True 有"通话被掐断"的用户体验代价，需业务确认。
  conditions: DSU Auto Log-off / 多 DSS 场景
  tags: [limitation, desksharing, ux]

- id: n08
  title: DAS 规则声明顺序重要，且多条规则可同时命中
  type: warning
  source_pages: p108
  source_chapter: OT server settings for remote access — DAS Rules configuration
  source_quote: |
    "WARNING THE DECLARATION ORDER IS IMPORTANT. SEVERAL RULES CAN BE APLLIED AT A TIME (EXAMPLE : RULE 1 AND
    2, 4 AND 6 …)"
  summary: |
    DAS 规则是串行管线（前一条输出=后一条输入），顺序错则结果全错；且设计上允许多条规则对同一号码接连生效
    （如规则 1+2、4+6）。改动 Default 域规则前先理解整链，别按"只命中一条"的直觉排规则。
  conditions: 会议服务器 DAS 规则维护
  tags: [warning, das, dialplan]

- id: n09
  title: 会议邀请 FQDN 必须进反向代理与 OT 证书的 SAN
  type: warning
  source_pages: p109
  source_chapter: OT server settings for remote access — ACS Service configuration
  source_quote: |
    "WARNING THIS SPECIFIC FQDN ASSIGNED FOR CONFERENCES INVITATION MUST BE PART (SUBJECT ALTERNATIVE NAME) OF
    THE REVERSE PROXY AND OPENTOUCH SERVER CERTIFICATES."
  summary: |
    会议邀请链接用的专用 FQDN（conf-podX.company.com）必须同时写进反向代理与 OpenTouch 两张证书的
    Subject Alternative Name，漏一处就会出现外网或内网一侧打不开会议链接。
    证书变更（rehost）后必须重新签发含该 SAN 的证书。
  conditions: ACS 会议服务 FQDN 配置与证书签发
  tags: [warning, certificate, san, conference]

- id: n10
  title: ACS FQDN 必须有内部 DNS 条目
  type: warning
  source_pages: p111
  source_chapter: OT server settings for remote access — Rehosting script
  source_quote: |
    "WARNING AN ENTRY FOR THIS DEDICATED FQDN AND IP ADDRESS MUST BE MANAGED IN INTERNAL DNS SERVER. VERIFY
    THAT IT IS THE CASE. PERFORM THE REQUIRED ACTION IF IT IS NOT DONE."
  summary: |
    rehost 脚本给会议服务分配 FQDN+内部 IP 后，内部 DNS 必须存在该条目（conf-podX.company.com →
    192.168.1.55，实验口径），否则内网解析失败、会议邀请链接内部不可用。DNS 由客户侧维护，交付清单要单列。
  conditions: ot-config.sh --rehost 执行前后
  tags: [warning, dns, acs]

- id: n11
  title: 证书 Deploy 后 WebAdmin 会话被切断属正常现象
  type: misconception
  source_pages: p117
  source_chapter: OT server settings for remote access — Certificate deployment
  source_quote: |
    "Just after clicking on 'Deploy', a message is displayed (« Impossible to retrieve data from / … ») and the
    WebAdmin session is cut. You have to restart the web session. It is normal because the server's
    certificate used for the 'https' connection has just changed."
  summary: |
    部署新证书瞬间报 "Impossible to retrieve data" 且 WebAdmin 掉线——这是 https 证书更换的预期行为，
    重新打开会话即可；不要当成故障回滚证书。
  conditions: OT 服务器证书部署
  tags: [misconception, certificate]

- id: n12
  title: RE DISA 前缀必须能在 DDI 翻译表中被翻译
  type: warning
  source_pages: p122
  source_chapter: OTC smartphone How-To — Remote extension DISA prefix
  source_quote: |
    "Warning CHECK THAT THIS PREFIX IS TRANSLATED IN THE DDI TRANSLATION TABLE"
  summary: |
    远程扩展 DISA 前缀（实验 31280）建好后必须核对 DDI 翻译表能把它翻译成公网号——否则公网呼入到达后
    无法路由到 DISA 服务，手机侧收不到来话。这是"呼入链路"最常漏的一环（前缀建了、翻译没建）。
  conditions: OTC 智能手机 OXE 侧通用设置
  tags: [warning, disa, ddi, smartphone]

- id: n13
  title: 直达速拨范围长度不能为 0 也不能占满
  type: limitation
  source_pages: p125
  source_chapter: OTC smartphone How-To — Range of direct speed dialing numbers
  source_quote: |
    "The range size CANNOT be 0 and also should NOT be full."
  summary: |
    自动替换要从直达速拨范围取号：范围长度设 0 或已被占满都会让自动替换失败。智能手机用户扩容前先核对
    范围余量，必要时扩长度。
  conditions: OTC 智能手机自动替换机制
  tags: [limitation, numbering, smartphone]

- id: n14
  title: 远程扩展目录号禁止以字母 A-D 开头
  type: limitation
  source_pages: p132
  source_chapter: OTC smartphone How-To — Mobile device declaration
  source_quote: |
    "Remote extension directory… Enter a number for the remote extension created in OXE (e.g. 2131001). Do NOT
    use a number beginning with letter (A,B,C,D) in the directory number of the Remote Extension!"
  summary: |
    命名空间规则：RE 目录号必须纯数字（A-D 开头保留给设备号/速拨号命名，如 D2131001、A2131001）；
    Ghost Z 可用 B<号> 占假号。填错命名空间会导致 OXE 对象创建失败或行为异常。
  conditions: OTC 智能手机关联配置
  tags: [limitation, numbering, rex]

- id: n15
  title: 双模智能手机的两处 Warning——Entity 识别码选择器与公网 COS 闭锁放行
  type: warning
  source_pages: p142
  source_chapter: OTC smartphone How-To — Additional manual management
  source_quote: |
    "Warning Each Entity where dual mode CT users will be declared, it is important to review the Discriminator
    Selector to associate a logical discriminator to a physical discriminator that is dedicated to smartphones."
    "Warning To be able to call the mobile the system must pass the baring. The area of the public access Class
    Of Service specified in the dedicated discriminator for Ct smartphones, must be authorized to call the
    mobile number of the user"
  summary: |
    自动创建不包办两件事：①Entity 的识别码选择器要把逻辑识别码（3）映射到智能手机专用物理识别码；②用户
    公网接入 COS 必须授权识别码所用区域号（barring 放行）。漏掉任一项，GSM 回退路由就是"配了但不通"。
  conditions: 双模智能手机 GSM 路由联调
  tags: [warning, entity, cos, barring, smartphone]

- id: n16
  title: 呼叫切换不可回切；目标话机配立即呼转则跟呼转走
  type: limitation
  source_pages: p152, p162
  source_chapter: Extended Mobility
  source_quote: |
    "OTC application will execute an automated scenario: <make a 2nd call towards the deskphone> + <transfer
    the call> • Since the automated scenario has been executed, there is no retrieve facility to switch back
    the call to smartphone • If deskphone is configured with immediate forward, the call switching will route
    to this destination"
  summary: |
    Extended Mobility 呼叫切换是"二通呼叫+转移"的自动场景，执行后无法把通话切回手机；且目标话机若配了
    立即呼转，呼叫会跟着呼转目的地走（可能出现"扫了 A 话机、铃在 B 处"）。售前演示要预先清呼转。
  conditions: Extended Mobility 呼叫切换场景
  tags: [limitation, extended-mobility, routing]

- id: n17
  title: NFC 不支持 iPhone；触发需 OTC 应用已启动
  type: limitation
  source_pages: p150, p161, p166
  source_chapter: Extended Mobility
  source_quote: |
    "(*) NFC not supported by iPhone" (p150)
    "NFC & QR Code are triggered by OTC for smartphone (Application must already be launched)" (p161)
    "Warning THE NFC FACILITY IS NOT AVAILABLE FOR IPHONE" (p166)
  summary: |
    两点能力边界：①NFC 只在 Android 可用，iPhone 只能扫 QR 码；②无论 NFC 还是 QR 都由 OTC 应用触发，
    应用必须已经启动（杀后台后标签无效）。用户教育要覆盖这两条。
  conditions: Extended Mobility 终端侧使用
  tags: [limitation, extended-mobility, nfc, iphone]

- id: n18
  title: Gmail 存储语音留言上限 500 个 OT 用户
  type: limitation
  source_pages: p176
  source_chapter: Unified Messaging — Architecture
  source_quote: |
    "Gmail platform can be used to store voice mails ... Limited to 500 OpenTouch users"
  summary: |
    Gmail 后端有 500 用户硬上限，超大规模或快速增长客户不适合选 Gmail 做 UM 存储；量表时按上限卡，
    超限改 Exchange/O365 或 IMAP。
  conditions: UM 后端选型
  tags: [limitation, um, gmail, capacity]

- id: n19
  title: IMAP4 后端砍四项能力——无 PPR/扩展/MWI/消息类别
  type: limitation
  source_pages: p177
  source_chapter: Unified Messaging — Architecture
  source_quote: |
    "IMAP4 mail server • No plug-in: less services • No PPR • No Extensions • No MWI • No class of message"
  summary: |
    IMAP4 是功能最弱后端：无 PPR（话机上播放/录制的扩展交互）、无扩展、无 MWI（留言灯）、无消息类别。
    客户用自建 IMAP 时要把这些降级提前写入方案，别按 Exchange 体验承诺。
  conditions: UM 后端选型与验收标准制定
  tags: [limitation, um, imap]

- id: n20
  title: 每个 UM 用户邮箱必须三参数齐全——Send as / Full Access / Send on behalf
  type: warning
  source_pages: p191
  source_chapter: UM How-To — Assign permissions (delegation)
  source_quote: |
    "Warning FOR EACH PERSON USING A 'UNIFIED MESSAGING' MAILBOX (ALBAN, BACKMAN…), IT'S MANDATORY TO MANAGE
    THE TREE PARAMETERS, CALLED 'MANAGE SEND AS PERMISSION', 'MANAGE FULL ACCESS PERMISSION' AND 'SEND ON
    BEHALF'"
  summary: |
    走 delegation 方案（R2.2 前）时，每个用 UM 的邮箱都要逐个配齐三个权限参数，漏一个该用户留言投递/存取
    即异常；这也是大流量场景下 delegation 被 impersonation 取代的原因（p189）。新版用 impersonation 则改在
    EMS 给服务账号授 ApplicationImpersonation。
  conditions: Exchange 侧权限配置（版本分界 >2.2.x / <2.2.x）
  tags: [warning, um, exchange, permissions]

- id: n21
  title: 语音邮箱档案改动后必须同步才生效
  type: warning
  source_pages: p201
  source_chapter: UM How-To — Synchronization
  source_quote: |
    "Warning SYNCHRONIZATION IS REQUIRED TO RETRIEVE THE TEMPLATES FROM THE OPENTOUCH SERVER."
  summary: |
    新建/修改 VM 档案后必须执行 OT（及/或 OXE）同步，模板才会出现在 Users 工具里并被用户邮箱引用。
    "改了档案没效果"先查是否漏了同步（四种组合 Complete/Partial × Separate/Global 按需选）。
  conditions: 语音邮箱档案生命周期
  tags: [warning, um, synchronization]

- id: n22
  title: 问候语必须先用话机录制才会出现在 My Profile
  type: warning
  source_pages: p211
  source_chapter: UM How-To — My Profile application
  source_quote: |
    "Warning TO BE ABLE TO CHANGE YOUR GREETING (EXTENDED ABSENCE, PERSONAL, ALTERNATIVE…), YOU FIRST MUST
    RECORD THEM THROUGH YOUR PHONE SET. THEY WILL APPEAR IN 'MY PROFILE' ONLY AFTER THAT OPERATION"
  summary: |
    My Profile 里改问候语的前提是该问候语已通过话机录过一次——网页端不能从零创建。
    用户问"为什么 My Profile 里没有我的问候语"，先让他用话机录一遍。
  conditions: 用户级 UM 使用
  tags: [warning, um, my-profile]

- id: n23
  title: Office 365 的 Outlook 加载项/集成从 OT 2.5 起，且仅支持桌面版 Office
  type: version-trap
  source_pages: p178
  source_chapter: UM — Cross compatibility
  source_quote: |
    "Office 365 is supported with Office desktop applications only ... Outlook messaging add-ins ... From OT
    2.5 (1) ... Office Integration From OT 2.5 (1)"
  summary: |
    兼容表注脚：O365 场景的 Outlook 加载项、联系人同步、Office 集成都要 OT 2.5 及以上，且只支持 Office
    桌面应用（网页版 Outlook 不在列）。老版本 OT 接 O365 时这些功能直接不可用，属版本门槛而非故障。
  conditions: O365 + Outlook 集成交付
  tags: [version-trap, um, o365, outlook]

- id: n24
  title: 可选搜索属性三重边界——最多 5 个参与搜索、photo 不可 searchable、部分客户端不支持
  type: limitation
  source_pages: p250
  source_chapter: Directory search How-To — Make optional attributes available
  source_quote: |
    "within all these optional attributes, a maximum of five of them can be involved during the directory
    search operation. ... The 'searchable' option is not available for all attributes, example for the photo.
    The search on optional attributes doesn't work from all clients even if it is configured."
  summary: |
    目录可选属性三个坑：①同刻最多 5 个可选属性参与搜索（预置 20+，选哪 5 个要规划）；②"可搜索"开关并非
    所有属性都有（照片只能显示不能搜）；③配置了也不保证所有客户端都支持可选属性搜索——验收用例要按客户端
    实测。
  conditions: UDAS 可选属性配置与验收
  tags: [limitation, udas, search]

- id: n25
  title: 目录同步参数三处硬规则——date/time/period 必填、period≥1 永 0、merge period≠0
  type: limitation
  source_pages: p244, p245, p253
  source_chapter: Directory search How-To
  source_quote: |
    "Tips Synchronization Date, Time and period MUST BE SET. Synchronization period >= 1 (NEVER SET period to
    0)" (p244 与 p245 两处重复)
    "Merge Period Configure the merge period (must be different from 0)" (p253)
  summary: |
    同步/合并参数不设或设 0，同步库就是空库或合并不跑——"搜不到人"的第一排查项。内部目录、电话簿、LDAP
    目录三处都要设；SBC 的 Merge Period 同样禁 0。
  conditions: UDAS 部署与"搜不到联系人"排障
  tags: [limitation, udas, synchronization]

- id: n26
  title: AMS 只支持 Active talker；Radvision 与 LifeSize 外部 MCU 不再支持
  type: version-trap
  source_pages: p273
  source_chapter: Collaboration & Conference features — Video conferences
  source_quote: |
    "AMS supports only the switched presence ('Active talker'): no continuous presence • The Radvision MCU and
    UVC LifeSize Multipoint external MCU are no more supported"
  summary: |
    视频会议两条边界：①内置 AMS 只能"-active talker"切换画面，做不到 continuous presence（多方同屏），
    需求里有"九宫格"就要另找方案；②Radvision MCU 与 UVC LifeSize 外部 MCU 已不再支持——存量对接方案要按
    最新兼容清单重审。
  conditions: 视频会议方案设计与旧设备复用评估
  tags: [version-trap, video, mcu, ams]

- id: n27
  title: Connection 用户不能做点对点视频与 ad-hoc 视频
  type: limitation
  source_pages: p274
  source_chapter: Collaboration & Conference features — Video conferences
  source_quote: |
    "Connection users cannot perform neither peer to peer video communications nor ad hoc video conferences:
    only scheduled video conferences"
  summary: |
    Connection 用户（绑话机型）只能参加"预约"视频会议；点对点视频与临时拉起的视频会议是 Conversation 用户
    能力。给话机用户承诺"随时拉视频"会翻车，选型时先分清用户类型。
  conditions: 视频会议需求沟通
  tags: [limitation, video, user-type]

- id: n28
  title: 协作限制不适用于 S4B/Teams 集成与 OT networking
  type: limitation
  source_pages: p291, p294
  source_chapter: Conference features — Collaboration capabilities restrictions & Privacy
  source_quote: |
    "The collaboration restriction feature is not available in case of: Skype for Business or Teams integration
    (Presence and collaboration are not provided by OpenTouch) • OT networking" (p291)
    "The privacy feature is not available in case of: OT networking • Skype for Business or Teams integration" (p294)
  summary: |
    两项治理特性都有场景豁免：协作限制（sharing/collaboration 禁用）与在场隐私（followers 阻断）在
    S4B/Teams 集成（在场与协作归微软）与 OT networking（多 OT 互联）下不可用。混合部署里别指望 OT 侧管
    住 Teams 用户的协作。
  conditions: 混合/互联部署的权限治理设计
  tags: [limitation, collaboration, teams, ot-networking]

- id: n29
  title: OTC Web 功能边界——无白板/投票/录制/视频/联系人/历史/排期；JS+Cookies 必开；WebRTC 仅 Chrome/Firefox
  type: limitation
  source_pages: p333-334
  source_chapter: OTC for WEB — Deployment & Restrictions
  source_quote: |
    "A plug-in installation can be required before activation of the Desktop sharing publisher feature ...
    Note that 'Javascript' and 'Cookies' must be enabled in the browser settings • Browser support for Web
    RTC: Google Chrome • Mozilla Firefox" (p333)
    "Some features are not yet available ... No white board • No poll • No recording • No video • No contact
    list (buddy list) • No history • No scheduling interface" (p334)
  summary: |
    OTC Web 的验收边界：不支持白板、投票、录制、视频、联系人列表、历史、排期界面（排期靠 OTC PC/Outlook）；
    桌面共享发布端可能要装插件；浏览器必须开 JS 与 Cookies；WebRTC 音频仅 Chrome/Firefox。
    访客入会方案按此清单定预期。
  conditions: 访客/浏览器端会议方案
  tags: [limitation, otc-web, webrtc]

- id: n30
  title: DCS 未激活许可/未打强制更新 → 文档卡 queued 不转换
  type: warning
  source_pages: p375
  source_chapter: DCS-V How-To — Prerequisites
  source_quote: |
    "Warning Activate Licenses keys for Windows and Office ... Use standard Microsoft procedures to apply all
    Mandatory updates for both Windows and Office. ... Warning Failure to perform these updates will result in
    documents that remain in the queued state and do not get converted."
  summary: |
    DCS 虚机上 Windows/Office 许可未激活或强制更新没打齐，症状是会议里 Office 文档一直"queued"不转换——
    根因在 Windows 侧准备，不在 OT/ACS 配置。装机清单里把激活+更新列为阻断项。
  conditions: DCS 部署与"文档不转换"排障
  tags: [warning, dcs, windows]

- id: n31
  title: DCS 自动登录注册表改完必须重启虚机
  type: warning
  source_pages: p379
  source_chapter: DCS-V How-To — Windows automatic login activation
  source_quote: |
    "Warning REBOOT WINDOWS VIRTUAL MACHINE ... AutoAdminLogon 1 • DefaultDomainName ... DefaultPassword ...
    DefaultUserName"
  summary: |
    Winlogon 四键（AutoAdminLogon/DefaultDomainName/DefaultUserName/DefaultPassword）配完不重启不生效；
    DCS 要求管理员会话自动登录运行，重启遗漏会让 DCS 组件不起、文档转换停止。
  conditions: DCS-V 安装
  tags: [warning, dcs, windows]

- id: n32
  title: 日历特性流程仅适用 UM 上下文；本地存储邮箱走 TC2558
  type: warning
  source_pages: p395
  source_chapter: Calendar synchronization and calendar presence How-To
  source_quote: |
    "Warning THE FOLLOWING PROCEDURE HAS TO BE USED ONLY IF YOU WANT TO BRING INTO SERVICE THE CALENDAR
    SYNCHRONIZATION AND THE CALENDAR PRESENCE FEATURES WITH A UNIFIED MESSAGING CONTEXT. IF USERS HAVE LOCAL
    STORAGE MAILBOXES, PLEASE HAVE A LOOK TO THE TECHNICAL DOCUMENTATION 'TC 2558' TO CONFIGURE THESE 2
    FEATURES"
  summary: |
    本章流程只对"邮箱在邮件服务器（UM）"的用户生效；本地存储邮箱（OT 内部存储）用户要配置这两个日历特性
    必须改用 TC2558 的另一套流程——按错流程配不出来。
  conditions: Calendar presence/synchro 部署前判型
  tags: [warning, calendar, um, tc2558]

- id: n33
  title: OTC 创建的周期会议不推送到 Exchange
  type: limitation
  source_pages: p392
  source_chapter: Calendar presence & calendar synchro
  source_quote: |
    "Restriction • Recurrent meetings created from OTC client are not pushed into Exchange. • Recurrent
    meetings created from Outlook Calendar are pushed into OpenTouch"
  summary: |
    日历同步的不对称限制：Outlook 建的周期会议能推进 OT，反向不行——OTC 客户端建的周期会议不会出现在
    Exchange 日历。用户习惯在 OTC 排周期例会时，Outlook 日历是空的；规范用法是周期会议从 Outlook 建。
  conditions: Calendar synchro 用户培训与验收用例设计
  tags: [limitation, calendar, sync]

- id: n34
  title: Calendar presence 需 OT R2.3.1+（impersonation）；Synchro 仅 Exchange 2010/2013/O365；Outlook 仅 2010/2013
  type: version-trap
  source_pages: p406, p408 (TC2258)
  source_chapter: TC2258 — Prerequisites
  source_quote: |
    "The feature can be use only from OpenTouch R2.3.1 due to Exchange impersonation configuration. Calendar
    Presence Unified Messaging feature is supported with Microsoft Exchange and Office365 servers." (p406)
    "Calendar Synchro feature is supported with Microsoft Exchange 2010,2013 and Office365. Only Microsoft
    Outlook 2010 or 2013 are supported. The conference license for each user is necessary." (p408)
  summary: |
    版本三重门槛：Calendar Presence 自 OT R2.3.1 起（依赖 impersonation）；Calendar Synchro 只支持
    Exchange 2010/2013/O365（2016+ 未列）；客户端只支持 Outlook 2010/2013（书内主口径 2013）。每个用户还
    必须有会议许可。交付前按客户版本矩阵逐项核对。
  conditions: 日历特性版本评估
  tags: [version-trap, calendar, exchange, outlook]

- id: n35
  title: 外部认证是全局开关——不能按应用启用；IP Touch 应用与 TUI 例外
  type: limitation
  source_pages: p426
  source_chapter: External authentication — restrictions
  source_quote: |
    "The authentication mechanism applies to all devices/Applications • You cannot activate a specific
    authentication for one Application/device only • Note that IP Touch applications and TUI do not use this
    mechanism as authentication is based on the user's phone number"
  summary: |
    外部认证一旦启用对所有应用/设备生效，无法只给某个应用开——影响评估必须覆盖全部客户端；
    例外是 IP Touch 应用与 TUI（话机界面），它们按话机号码认证、不走外认。话机侧行为不会因外认改变。
  conditions: 外部认证启用前影响评估
  tags: [limitation, authentication, scope]

- id: n36
  title: 外认失败级联不对称——Web 客户端级联回 DTA，厚客户端不级联
  type: limitation
  source_pages: p426
  source_chapter: External authentication — restrictions
  source_quote: |
    "If external authentication fails, there is an automatic cascading to DTA for Web clients (WBM for
    Administrator…) • No automatic cascading for thick clients (OTC PC…)"
  summary: |
    LDAP/RADIUS 服务器不可达时：Web 客户端（含 WBM）自动回落本地 DTA 账密，OTC PC 等厚客户端直接登录失败。
    LDAP 维护窗口要预告"厚客户端会登不上"，否则会收到一波故障单。
  conditions: 外部认证服务器维护窗口
  tags: [limitation, authentication, cascade]

- id: n37
  title: Kerberos 启用即全量生效；8770 客户端进不了 WBM，须预留 AD 管理员
  type: warning
  source_pages: p430, p452
  source_chapter: External authentication — Upstream restrictions / Kerberos How-To
  source_quote: |
    "When Kerberos authentication is activated for an application, it must be used for every single user of
    this application • Before enabling external authentication, be sure to fill in the External login field
    for the admin account. If you do not, you will be unable to log in to the configuration tool. • e.g.: Once
    Kerberos has been enabled on the OpenTouch, the OmniVista 8770 client cannot access Web Based Management
    (WBM) anymore • Workaround is to provide access to WBM to one Active Directory user (e.g. 'eric_admin')" (p430)
    "Once Kerberos has been enabled on the OpenTouch, the OmniVista 8770 client cannot access Web Based
    Management (WBM) anymore. ... it is required to do the appropriate management for this administrator
    account. If you do not, you will be unable to log in to the configuration tool." (p452)
  summary: |
    启用 Kerberos 前的保命两步：①管理员账号（OTADMIN）必须预先填 External login 并在 AD 建好账密，否则
    启用后配置工具直接进不去；②Kerberos 一开，8770 客户端无法再访问 WBM——必须按 p454 流程预留一个 AD
    出身的管理员（wbm_admin 类，Application=WBM + Delegate authentication）。顺序颠倒=把自己锁在门外。
  conditions: Kerberos 启用变更窗口
  tags: [warning, kerberos, wbm, admin, lockout]

- id: n38
  title: Kerberos 覆盖面窄——仅 Windows 上的 Web 应用 + OTC PC；移动端不支持；不经反向代理
  type: limitation
  source_pages: p431
  source_chapter: External authentication — Upstream restrictions
  source_quote: |
    "Applications/Device supported for the external Kerberos authentication are: Web applications running upon
    Microsoft Windows Operating System only • OpenTouch Conversation for PC (OTC PC) • Other Applications/
    devices such as OTC clients for Android and iOS smartphones …, do not support this mechanism ... Kerberos
    authentication is not supported through a reverse proxy. In this case, OTC PC applications fall back to the
    login/password method."
  summary: |
    Kerberos SSO 的适用面三条：①Web 应用仅限跑在 Windows 上的；②OTC PC 支持，Android/iOS 客户端不支持
    （仍提示账密，走 DTA/LDAP/Radius）；③不支持经反向代理——远程用户自动回落账密，本地用户享 SSO。
    "全员无感登录"的预期要按此收敛。
  conditions: Kerberos 方案宣讲
  tags: [limitation, kerberos, mobile, reverse-proxy]

- id: n39
  title: keytab 密码必须与 AD ice_kerb 账号密码一致
  type: warning
  source_pages: p450
  source_chapter: Kerberos How-To — AD account creation
  source_quote: |
    "Warning THE PASSWORD, PREVIOUSLY DEFINED, MUST BE THE ONE STORED IN THE 'ICE_KERB.KEYTAB' FILE."
  summary: |
    生成 ice_kerb.keytab 时输入的密码必须与 AD 上 ice_kerb 账号的密码完全一致（实验值 1234）——不一致则
    票据验证全挂。AD 侧该账号还要勾"不能改密码+密码永不过期"，防止两侧漂移。
  conditions: Kerberos keytab 生成与 AD 账号治理
  tags: [warning, kerberos, keytab]

- id: n40
  title: External login 全局唯一——同一 AD 名不能同时给标准用户和管理员
  type: limitation
  source_pages: p454, p438
  source_chapter: Kerberos How-To — WBM access / LDAP How-To
  source_quote: |
    "The value for 'External login' is unique in the OpenTouch configuration. ... The selected Active Directory
    user name for External login (for instance wbm_admin) cannot be used for an OpenTouch standard user and an
    OpenTouch admin user at the same time" (p454)
    "Warning TO HAVE A HOMOGENEOUS AUTHENTICATION MANAGEMENT, IT IS ADVISED TO ALSO DECLARE THE 'EXTERNAL
    LOGIN' PARAMETER FOR ADMINISTRATOR ACCOUNT, & TO CONFIGURE ITS LOGIN/PASSWORD IN THE EXTERNAL LDAP SERVER." (p438)
  summary: |
    External login 在 OT 配置里全局唯一：一个 AD 名不能既当标准用户又当管理员；且建议管理员账号统一配
    External login（否则 WBM 走 DTA 内部认证，行为不一致）。规划 AD 名映射时要给管理员单独留名字空间。
  conditions: 外部认证账号映射规划
  tags: [limitation, authentication, admin]

- id: n41
  title: 用户改路由档案须在空闲态；周期提醒的三种应答与 toggle 停止
  type: limitation
  source_pages: p154-155, p164
  source_chapter: Extended Mobility
  source_quote: |
    "This can only be performed when the OTC Smartphone is idle and without a communication in progress." (p164)
    "Yes: the previous call routing profile is enabled again and the periodic timer is stopped ... Later: OTC
    applications continues to use the current call routing and the periodic timer is re-launched (a new pop-up
    will be displayed in one hour)" (p154)
    "The end-user changes the call routing profile to a completly time. • By scanning this QR code again
    (toogle action) • By reading this NFC tag again (toogle action)" (p155)
  summary: |
    路由修改（区别于呼叫切换）只在手机空闲、无进行中通话时可执行；每小时提醒弹窗三种应答——Yes 恢复原
    档案、No 保留并停表、Later 一小时后再弹；不再提醒可再扫同一标签（toggle）。用户报"提醒一直弹"时
    按此解释。
  conditions: Extended Mobility 路由修改日常使用
  tags: [limitation, extended-mobility, routing, ux]

- id: n42
  title: LDAP 溢出服务器上限两处口径不一（讲义 20 台 vs OXE 电话簿 5 个）
  type: version-trap
  source_pages: p235, p260
  source_chapter: LDAP overflow for OXE users
  source_quote: |
    "Restrictions • LDAP version 3.0 or higher • 20 LDAP servers maximum • No referral" (p235, 讲义)
    "Up to five LDAP servers can be declared in the OXE ... LDAP phone book Enter the phone book index (from 1
    to 5)" (p260, 实验)
  summary: |
    同一特性两页数字打架：讲义称最多 20 台 LDAP 服务器，实验手册明确 OXE 的 LDAP Phone Books 索引仅 1-5。
    现场按 5 个做 OXE 侧配置上限；20 的适用语境（推断：或指 OT/UDAS 侧目录数量）需以最新技术通报核实，
    引用数字时注明出处页。
  conditions: LDAP 溢出容量规划与引用
  tags: [version-trap, ldap, capacity, contradiction]

- id: n43
  title: R2.6 前后"手机当主设备"语义不同——此前需永不入服的 SIP 扩展做主机+溢出
  type: version-trap
  source_pages: p96, p134
  source_chapter: OTC for smartphones / OTC smartphone How-To
  source_quote: |
    "In case of a user without physical main desk phone but only a smartphone, the configuration principle was
    the following before the OpenTouch R2.6: Main device (desk phone): a SIP extension (which never be in
    service) • Second device: the remote extension • Overflow on secondary device, if the main is out of
    service had to be configured. From release 2.6 of OpenTouch, the main device can be directly the remote
    extension" (p134)
    "Configuration simplified: no more need of SEPLOS as main set • Fix issues due to the foward on out of
    service device" (p96)
  summary: |
    R2.6 是分水岭：之前"只有手机的用户"要配一个永不入服的 SIP 扩展（SEPLOS 类）做主设备 + 溢出到 RE，存在
    "主设备不在服导致前转"的已知问题；R2.6 起 RE 直接当主设备（单设备配置）。升级交付与旧配置迁移要按版本
    分开处理，旧结构要改造。
  conditions: 纯手机用户配置（无物理话机）
  tags: [version-trap, rex, r2.6, smartphone]

- id: n44
  title: UM 权限方案版本分界——R2.2 前 delegation、R2.3 起 impersonation
  type: version-trap
  source_pages: p189-190
  source_chapter: UM How-To — Assign permissions
  source_quote: |
    "Before OpenTouch release 2.2, the second method (delegation) was used but some troubles were possible in
    case of a lot of traffic with the Exchange server (a lot of users or lot of accesses to the mailboxes).
    Since the release 2.3 ... the OpenTouch server uses now impersonation method instead of delegation to work
    with the Exchange server. Only the configuration on Exchange server side is different (point 1.2.1 or point
    1.2.2)."
  summary: |
    同一 UM 功能两种 Exchange 侧配法：OT ≤2.2.x 用 delegation（逐邮箱三参数，大流量有隐患）；OT >2.2.x
    （2.3 起）用 impersonation（EMS 授 ApplicationImpersonation）。OT 侧配置原则不变，只换 Exchange 侧——
    升级 OT 后要同步换 Exchange 权限方案，两代混用会出疑难。
  conditions: UM 权限配置与 OT 版本升级
  tags: [version-trap, um, exchange, impersonation]

- id: n45
  title: R2.0 起 nomadic 必须补 DAS 规则 7/8（+N/+M）
  type: version-trap
  source_pages: p108
  source_chapter: OT server settings for remote access — DAS Rules configuration
  source_quote: |
    "From R2.0 new rules must be added for OT Connection PC application used in nomadic mode and must respect
    the following order: s/^\\+[National Prefix]/[Trunk seizure Prefix]0/ • s/^\\+N/N/ • s/^\\+M/M/ •
    s/^\\+/000/ ... Verify the DAS rules and add following rules if not present: s/^\\+N/N/ • s/^\\+M/M/"
  summary: |
    老系统升级到 R2.0 后，nomadic 用户经会议服务器/ACS 的呼叫需要 DAS 规则 7（+N/N）与规则 8（+M/M）——
    升级后"nomadic 打不出去"先查这两条是否存在且顺序正确。
  conditions: R2.0+ 升级后 nomadic 呼叫验证
  tags: [version-trap, das, nomadic]

- id: n46
  title: 日历在场四条易误解——自己看不到自己、FREE 只在名片显示、不改颜色码、OOO 优先
  type: misconception
  source_pages: p387-389, p402-405 (TC2258)
  source_chapter: Calendar presence
  source_quote: |
    "The color code is not modified by the calendar presence information." (p387)
    "As an OTC PC or OTC One user we don't see our own calendar presence in our application." (TC2258 p4)
    "The FREE calendar status information (+endate) is only displayed at 2nd level of application." (TC2258 p6)
    "Out of Office > Busy >Tentative > Working Elsewhere > Free" (p389)
  summary: |
    验收与用户教育的高频误解：①自己永远看不到自己的日历在场（看别人的）；②FREE 状态只在联系人名片（二级
    界面）显示，收藏列表/通话记录不显示；③日历在场只是旁注文本，不改变在场颜色码；④日程重叠按
    OOO>Busy>Tentative>Working Elsewhere>Free 取值——显示"Busy"不代表没有 OOO 日程。按"没生效"报障的
    多数是这四条预期差。
  conditions: Calendar presence 验收与支持
  tags: [misconception, calendar, presence]

- id: n47
  title: RADIUS 实验章 Notes 复制粘贴错误——写成"连接 LDAP 目录的参数"
  type: limitation
  source_pages: p459
  source_chapter: RADIUS authentication How-To
  source_quote: |
    "Notes Here are all the parameters required to be able to connect to a LDAP directory. All parameters
    required for such management are on bold character." (p459，该页实际内容为 plugin_radius.properties)
  summary: |
    RADIUS 章 Notes 原文写"以下是连接 LDAP 目录所需的参数"，实际页面内容是 RADIUS 插件参数——原书复制
    粘贴笔误。以文件名与参数名（plugin_radius.properties/server.*）为准理解；同时提示实验手册亦有人为
    错误，关键操作交叉核对 TC 文档。
  conditions: 阅读 RADIUS 章配置说明
  tags: [limitation, documentation, radius]

- id: n48
  title: 会议密码不出现在邀请邮件，须领导者自行告知；音频密码自动套用到录音
  type: limitation
  source_pages: p354
  source_chapter: Data conferencing How-To — Passwords
  source_quote: |
    "Passwords will not be included in email invitations. Conference leaders must inform people who are invited
    to the conference of the password. • Passwords that you assign to the audio conference will automatically
    be assigned to any recordings that you made during the conference"
  summary: |
    两条易翻车行为：①会议密码不写进邀请邮件（安全设计），与会人"没有密码进不去"是预期，需领导者另行
    通知；②音频密码会自动应用到该会议的录音，回放也要密码。交付培训要把这两条写进用户指南。
  conditions: 会议密码使用与录音分发
  tags: [limitation, conference, password, recording]

- id: n49
  title: 实验明文密码遍布全书——生产化必须全部替换并纳入安全基线
  type: limitation
  source_pages: p9, p113, p184-185, p210, p313, p375, p448-450, p459
  source_chapter: 全书 Settings 表与各 How-To
  source_quote: |
    "root letacla1 / root superuser / Administrator Superuser01* / Administrator superuser" (p9)
    "Login: ICEaccess Password: iceaccess" (p184-185)
    "User otAdmin Password admin8770 (for this training)" (p313)
    "'addent –password –p ice_kerb@company.com –k 0 –e rc4-hmac'. Type '1234'" (p448)
  summary: |
    letacla/superuser/iceaccess/admin8770/1234/training 等明文口令贯穿全部实验，是教材可复现性的产物。
    生产交付必须：全部默认口令首登即改、特权账号（ICEaccess/otAdmin/ice_kerb）纳入 vault 管理、
    shared_secret 按站点生成——引用本书命令模板时逐个替换凭据。
  conditions: 生产环境交付与安全审计
  tags: [limitation, security, credentials, lab]

- id: n50
  title: iPhone 通知依赖苹果云——防火墙四端口 + 每年 APNS 证书 hotfix 是长期运维项
  type: limitation
  source_pages: p97-98
  source_chapter: OTC for iPhone
  source_quote: |
    "APNS is an Apple Cloud service: firewall configuration is impacted" (p97)
    "APNS's certificate is shipped with OpenTouch server • Valid one year • A dedicated hotfix will be delivered
    every year to keep the certificate up to date" (p98)
  summary: |
    iPhone 推送走苹果云而非 OT 直连：防火墙要放行 TCP 5223/2195/2196/443；且 OT 随附的 APNS 证书一年有效，
    ALE 每年发专用 hotfix 更新——漏更的次年推送全停。这是一个"每年必做"的运维日历项，要写进维保合同。
  conditions: OTC iPhone 部署与年度维保
  tags: [limitation, apns, iphone, maintenance]
```

---

## 收尾自检 — 对照 BOOK_OVERVIEW.md 24 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | 实验 POD 搭建 | 间接 → n49（实验凭据口径，生产必须替换） |
| task-02 | ITSP1 联调 | 间接 → n49（同上，教学基础设施不入册） |
| task-03 | Nomadic 蜂窝 | 有 → n01（Desktop 许可）、n05（资源占线）、n03（同事号码） |
| task-04 | Nomadic VoIP | 有 → n02（cellular 前提）、n05、n01 |
| task-05 | Nomadic 维护 | 有 → n05（占线机制即核查对象） |
| task-06 | Desksharing 配置 | 有 → n07（Busy DSU 行为分支） |
| task-07 | Desksharing OTC PC/维护 | 有 → n06（OT 库所知）、n04（UA 不兼容 WAN/Mac） |
| task-08 | 反向代理/OTSBC | 有 → n49（凭据）、n38（Kerberos 与 RP 不兼容，间接） |
| task-09 | DAS/ACS/证书 | 有 → n08（DAS 顺序）、n09（SAN 警告）、n10（内部 DNS）、n11（Deploy 断会话）、n45（R2.0 规则 7/8） |
| task-10 | OXE 通用参数 | 有 → n12（DISA→DDI）、n13（速拨范围）、n14（RE 禁字母开头） |
| task-11 | iPhone+ SBC/参数 | 有 → n50（APNS 年度 hotfix） |
| task-12 | 设备档案与用户 | 有 → n43（R2.6 单设备语义）、n14 |
| task-13 | 核验/手工补充/维护 | 有 → n15（Entity 识别码 + COS barring） |
| task-14 | Extended Mobility | 有 → n16（不可回切/呼转）、n17（NFC 限 Android/应用须启动）、n41（空闲态/周期提醒） |
| task-15 | UM (Exchange) | 有 → n20（三参数）、n21（同步）、n22（话机先录）、n44（delegation/impersonation 分界） |
| task-16 | 邮箱权限/云/维护 | 有 → n20、n23（O365 版本门槛）、n19（IMAP 砍功能）、n18（Gmail 500） |
| task-17 | 目录搜索 | 有 → n24（可选属性三重边界）、n25（同步参数硬规则） |
| task-18 | SBC/UDAS 维护 | 有 → n25、n24 |
| task-19 | 会议服务器 | 有 → n08、n09、n10 |
| task-20 | 数据会议 | 有 → n48（密码不入邮件）、n29（OTC Web 边界）、n28（协作限制豁免）、n26/n27（视频边界） |
| task-21 | DCS | 有 → n30（queued 根因）、n31（注册表重启） |
| task-22 | 日历在场/同步 | 有 → n32（UM 上下文限定）、n33（周期会议不对称）、n34（版本门槛）、n46（四条预期差） |
| task-23 | LDAP/RADIUS | 有 → n35（全局开关）、n36（级联不对称）、n40（External login 唯一）、n42（20 vs 5 口径）、n47（Notes 笔误） |
| task-24 | Kerberos | 有 → n37（锁死风险）、n38（覆盖面）、n39（keytab 密码一致）、n40 |

**24/24 全部有边界类条目覆盖，无空缺。**

### 扫描完整性说明（Warning/Note/Tips 标记框逐页核对）

- 已入册的 Warning 框：p51（cellular 前提）、p72（DSU 须在 OT 库）、p108（DAS 顺序）、p109（证书 SAN）、p111（内部 DNS）、p122（DISA→DDI 翻译）、p142（Entity 识别码 + COS barring 两处）、p166（NFC 无 iPhone）、p191（UM 三参数）、p201（档案同步）、p211（问候语先录）、p349（Outlook 加载项激活）、p375（许可+更新两处）、p379（注册表重启）、p395（TC2558）、p438（管理员 External login）、p450（keytab 密码）。
- 已入册的 Tips/Note/Restriction/Important 框：p46（Desktop 许可）、p50（同事号码）、p61（UA 限制）、p47/p51（资源占线）、p70-71（系统参数行为+6004）、p125（速拨范围）、p132（RE 禁字母）、p152/161/162（切换语义）、p154-155（提醒与 toggle）、p176/177（Gmail 500/IMAP 砍功能）、p178（O365 注脚）、p189-190（delegation/impersonation）、p235/260（LDAP 上限冲突）、p250（可选属性三边界）、p244/245/253（period 硬规则）、p273（AMS/MCU 淘汰）、p274（Connection 无 p2p 视频）、p291/294（豁免场景）、p333/334（OTC Web 边界）、p392（周期会议不对称）、p406/408（TC2258 版本门槛）、p426/430/431（外认作用域/级联/Kerberos 覆盖面）、p454（External login 唯一）、p459（RADIUS Notes 笔误）。
- 复核后排除的纯操作提示框（非边界类）：p27（TFTP 地址提示，并入 c01）、p105/p106（URL 用途 Notes，并入 f09/c07）、p117 Notes（pkcs#12 passphrase，已并入 principle p37）、p124（每 RE 一个 Ghost 建议，并入 c09）、p199（档案可自建，并入 p32）、p316 Notes（代理向导自动填，并入 p38）、p344（DCS 需要，并入 p34）、p355（SMS 地址格式，教学性）、p47（"Don't forget Desktop"与 p46 同义去重）。
- 推断性结论已显式标注"（推断）"：n42（20 vs 5 的适用语境）。
- 版本号均按原文保留完整位数：R2.0、R2.1 MD1、R2.2、R2.2.x、R2.3、R2.3.1、R2.5、R2.6、R4.2（Android NFC 工具要求）、1.0.5-r0.0.5（FreeRADIUS.net）。
