# 反例/限制/边界/易错点候选 — OpenTouch Message Center Starter (OTMCXTE200EN R2.6 Issue 08)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: Post-install 密码不足 8 位不报错，事后才出问题
  type: warning
  source_pages: p75
  source_chapter: Post-installation wizard / 1.5 OTMC core settings
  source_quote: |
    "ALL PASSWORDS ON THIS PAGE MUST CONTAIN AT LEAST 8 CHARACTERS. THERE IS NO ERROR POP-UP IN CASE YOU USE
    LESS THAN 8 CHARACTERS BUT YOU WILL FACE PROBLEMS AFTERWARDS."
  summary: |
    向导账户页五个密码（root/maintenance/administrator/profile/SNMP）都要求 ≥8 字符，但向导不弹错误——短密码
    会静默通过，问题延后爆发（登录/声明失败）。录入时数清楚位数，别信界面校验。
  conditions: post-installation wizard 账户页
  tags: [warning, passwords, post-installation]

- id: n02
  title: OTMC 账户用户名禁用 admin/adminnmc/htuser 等保留名
  type: limitation
  source_pages: p75-76
  source_chapter: Post-installation wizard / 1.5 OTMC core settings
  source_quote: |
    "THE ACCOUNTS' USERNAMES MUST ALL BE DIFFERENT AND MUST NOT BE 'ADMIN', 'ADMINNMC', 'HTUSER' OR ANY OTHER
    EXISTING ACCOUNTS."
  summary: |
    五个账户的用户名必须互不相同，且不得使用 admin、adminnmc、htuser 或任何既有系统账户名——重名/撞保留名
    会在 8770 声明与组件认证时出莫名故障。维护/管理员/profile 账户默认名（书中"keep the default one"）即可
    用，改名的自由度在密码不在用户名。
  conditions: post-installation wizard 账户定义
  tags: [limitation, accounts, naming]

- id: n03
  title: DNS 必须前向+反向解析七类 FQDN——漏一条全线卡壳
  type: warning
  source_pages: p73
  source_chapter: Post-installation wizard / 1.3 Network settings
  source_quote: |
    "THE DNS MUST BE CONFIGURED TO RESOLVE (FORWARD AND REVERSE RESOLUTION): • OTMC SERVER FQDN • OMNIVISTA
    8770 SERVER FDQN • MAIL SERVER FDQN • LDAP SERVER FDQN • … CALL SERVER … • … H.323 GATEWAY FQDN"
  summary: |
    OTMC 装机后一切交互（8770 声明、通知、OXE 对接）都踩在 DNS 上：OTMC、8770、邮件服务器、LDAP 服务器、
    OXE 呼叫服务器（按冗余模式：无冗余=CS FQDN / 本地冗余=main 角色 FQDN / 空间冗余=每台 CS FQDN）、OXE
    H.323 网关，全部要正反双向解析。装完才补 DNS 是最常见的返工源头；p92/p94 的 nslookup 正反查是标准体检。
  conditions: post-install 网络设置阶段前后
  tags: [warning, dns, prerequisite]

- id: n04
  title: 课堂配置把网络安全关掉——官方明示话费盗打与未授权使用风险
  type: warning
  source_pages: p78
  source_chapter: Post-installation wizard / 1.7 Certificate
  source_quote: |
    "Network Security Off: Confirm Yes … BEWARE: THIS CHOICE IS NOT RECOMMENDED BY ALCATEL-LUCENT ENTERPRISE,
    AS IT IMPLIES INCREASED RISKS OF TOLL FRAUD, AND UNAUTHORIZED USE OF THE SERVICES OR FUNCTIONALITIES ON
    THE SYSTEM"
  summary: |
    向导证书步在课堂用通用证书 + Network security OFF（选 Yes）简化部署；这是实验口径，官方自己标注不推荐——
    关安全等级会放大 toll fraud（话费盗打）与功能被未授权使用的风险。生产部署严禁照搬该页操作。
  conditions: 课堂/实验环境；生产必须正式证书与安全等级
  tags: [warning, security, toll-fraud, lab]

- id: n05
  title: 备份存储：本地备份不推荐；虚拟环境必须外置 NFS
  type: warning
  source_pages: p79
  source_chapter: Post-installation wizard / 1.8 Backup storage
  source_quote: |
    "Local backup has been selected for hands-on purposes. Local backup is not recommended. USB or NFS backup
    should be preferred. … When OTMC installation is made on virtual environment, the backup directory must
    be configured on an external NFS partition."
  summary: |
    备份存储三选一（LOCAL/USB/NFS）。两条边界：①本地备份只是课堂省事的选择，官方不推荐，正式站点用 USB 或
    NFS；②虚拟化安装时备份目录必须配在外置 NFS 分区（要填 NFS Host 与 NFS Path）——虚拟环境选 LOCAL 属于
    直接违反硬规则。8770 侧 NFS server 怎么搭按 TC2024（p246）。
  conditions: post-install 备份存储页；虚拟化部署
  tags: [warning, backup, nfs, virtualization]

- id: n06
  title: 许可向导 OK 状态只代表文件存在，有效性不校验；Skip 后系统不正常
  type: warning
  source_pages: p77
  source_chapter: Post-installation wizard / 1.6.2 License files installation
  source_quote: |
    "THE OK STATUS INDICATES THAT THE LOCAL FILE IS PRESENT. BUT THE CONTENT (VALIDITY) OF THE FILE IS NOT
    CONTROLLED. THE SAME IN CASE OF EXTERNAL LICENSE SERVER USE, THE CONNECTION TO THE LICENSE SERVER AND ITS
    CONFIGURATION IS NOT TESTED, JUST THE LOCAL PRESENCE OF THE FILE."
    "If license file is not available or there are problems with, click SKIP. The wizard skips license
    installation. Skipping license installation does not stop the installation process, but, the OTMC server
    will not operate properly unless a manual installation of the correct license files is performed" (Tips)
  summary: |
    两个易被骗的点：①向导里许可文件显示 OK、外部许可服务器配置完成，都只校验"文件在本地"，不做内容有效性
    与服务器连通性测试——"装完了"不等于"许可有效"，要靠 $FLEXLM_HOME 下 ./lmutil lmstat –a 复核（p82）；
    ②点 Skip 不中断安装，但 OTMC 在手工补装正确许可前不会正常工作。
  conditions: 向导许可步骤与装机验收
  tags: [warning, licensing, flexlm, verification]

- id: n07
  title: 虚拟环境 dongle 必须挂到承载 FlexLM 的虚机上
  type: warning
  source_pages: p76-77
  source_chapter: Post-installation wizard / 1.6.1 License server parameter
  source_quote: |
    "Dongle has to be associated to the virtual machine hosting the Flexlm server: • Flexlm server virtual
    machine in case of external license server • OTMC virtual machine in case of embedded license server • In
    both cases, Aladdin USB device has to be added in the settings of the corresponding virtual machine."
  summary: |
    虚拟化许可的绑定锚点是 Aladdin USB dongle：FlexLM 内嵌→dongle 挂 OTMC 虚机；FlexLM 外部→dongle 挂
    FlexLM 虚机。挂错虚机等于许可无处安放。另外从 U 盘导许可时：先在虚机设置里核验/声明 USB 控制器、U 盘插在
    跑 vSphere 的 PC 上（别插 ESXi 主机）、经 vSphere 把 USB 设备转给目标虚机（p77 Notes）。
  conditions: 虚拟化部署；FlexLM 内嵌或外部两种拓扑
  tags: [warning, licensing, dongle, usb]

- id: n08
  title: 拷入新许可文件后必须重启 flexlmd 才生效
  type: limitation
  source_pages: p42, p82
  source_chapter: Licenses files installation / Manual licenses installation
  source_quote: |
    "When a new license file is copied into $LICENSES_HOME directory, the FlexLM service must be restarted to
    load this new file (service flexlmd restart)" (p42)
    "service flexlmd stop … Wait a couple of minutes and start the license server again: service flexlmd
    start" (p82)
  summary: |
    手工换/补许可的标准三步：SFTP（otuser）把 .ice 拷进 /var/data/licenses（=$LICENSES_HOME）→ service
    flexlmd stop 等几分钟再 start → ./lmutil lmstat –a 确认。只拷文件不重启服务，新许可不会被加载——
    "扩容许可后用户还是开不出来"先查有没有重启。
  conditions: 手工许可安装/更换
  tags: [limitation, licensing, flexlm]

- id: n09
  title: OXE 侧 netadmin 改完必须 APPLY MODIFICATION 才落盘
  type: warning
  source_pages: p84
  source_chapter: OmniPCX Enterprise declaration / 1.1 IP configuration
  source_quote: |
    "Warning DON'T FORGET TO APPLY THE MODIFICATION BEFORE TO LEAVE: 20. 'APPLY MOFIFICATION'"（"MOFIFICATION"
    为原文笔误）
  summary: |
    在 OXE 的 netadmin 菜单里改 IP/角色地址/节点名，退出菜单前必须执行第 20 项 APPLY MODIFICATION，否则改动
    全部丢弃——配完"没生效"先看有没有 Apply，再查别处。
  conditions: OXE 声明前准备（netadmin 工具）
  tags: [warning, oxe, netadmin]

- id: n10
  title: 恢复测试删用户：只能从 OT Configuration 窗口删——从 Users 应用删会把虚拟 SIP 设备从 OXE 删掉
  type: warning
  source_pages: p243
  source_chapter: OpenTouch Backup & Restore How-To / 4 Performing OpenTouch data restoration
  source_quote: |
    "Warning DON'T DELETE THE USER ALAN ALBAN FROM THE USERS APPLICATION! IF YOU DO SO, THE VIRTUAL SIP DEVICE
    WILL BE DELETED FROM THE OXE!"
  summary: |
    备份恢复的验证动作是"删用户→恢复→确认回来"，但删入口有讲究：必须走 OT Configuration 窗口；若从 Users
    应用删除，OXE 上的虚拟 SIP 设备会被连带删除——恢复完信箱数据也补不回设备侧。全书大写 Warning 级别只有
    几处，这条是其中之一。
  conditions: 备份恢复验证实验；同样的删用户动作在生产也要分清入口
  tags: [warning, backup, restore, users]

- id: n11
  title: LS 专属通知参数对非 LS 用户照常显示、可配置，但完全无效
  type: limitation
  source_pages: p190
  source_chapter: SMTP/SMS notifications How-To / 2.2 Users notification settings
  source_quote: |
    "The availability of Local Storage is not taken into account on Administration side. It means that
    parameters are always displayed and manageable but it will have no impact in case of a non local storage
    voicemail"
  summary: |
    管理界面不会按用户信箱类型隐藏选项：wav 附件、满箱通知、My Messaging 链接、关 MWI 这些 LS 专属开关对 UM
    用户照样显示、照样能配——但毫无作用。给 UM 用户调"为什么没有附件"之前，先确认其信箱类型是不是 Local
    Storage（可用性矩阵见 p180）。
  conditions: UM（Exchange/Domino/Gmail）信箱用户的通知配置
  tags: [limitation, notification, um, local-storage]

- id: n12
  title: 版本升级不覆盖已存在的通知模板——要新模板必须手删旧模板并重启 chameleon
  type: version-trap
  source_pages: p186
  source_chapter: SMTP/SMS notifications How-To / 1.3 Customization of notification messages
  source_quote: |
    "When installing a new version, the templates of text for Email and SMS notification are not updated if a
    version already exists in order to keep the eventual customization done by the administrator. Therefore if
    you want to have the new templates (for new translations, string changes,…) you have to delete the
    existing ones and restart the chameleon component. Once chameleon is restarted, the new templates replace
    the old ones, after that customization can be reported in these new templates."
  summary: |
    模板目录 /var/data/panda/notification4 的文件在升级时被刻意保护（保留管理员定制）——新版翻译/文案不会自动
    到位。想要新版模板：删旧模板 → 重启 chameleon → 新模板落地 → 再把定制回填。升级后"通知文案还是老样子"
    不是 bug，是这套机制的设计行为。
  conditions: OTMC 版本升级；通知模板已定制或已存在的站点
  tags: [version-trap, templates, notification, chameleon]

- id: n13
  title: OTMC 不充当 SMTP 服务器——Outlook 测试发信失败是预期行为
  type: misconception
  source_pages: p174, p207
  source_chapter: SMTP/SMS notification & Voice Messages retrieval through IMAP
  source_quote: |
    "There is no SMTP server in the OpenTouch solution." (p174)
    "The 'send test e-mail message' test fails, if a SMTP server is not reachable or OpenTouch/OTMC FQDN is
    used as outgoing mail server (OpenTouch server/OTMC (local storage voice mail) does NOT act as a SMTP
    server)" (p207)
  summary: |
    OTMC（LS 型）只当 IMAP 服务器（收语音留言），从不提供 SMTP 服务。IMAP 账户配置里发件服务器是"摆设但别
    乱填"：填 OTMC FQDN 会让 Test Account Settings 的发信测试红叉，被误判成配置失败——正确做法是填真实邮件
    服务器 FQDN，且接受该测试失败属预期，只有 IMAP 登录测试 Completed 才算数。
  conditions: IMAP 客户端配置与验收
  tags: [misconception, imap, smtp, testing]

- id: n14
  title: IMAP 默认 IMAPS+TLS——客户端加密类型必须匹配；改安全级要改端口并重启 imap4fed
  type: warning
  source_pages: p208
  source_chapter: Voice Messages retrieval through IMAP / IMAP4 Front End
  source_quote: |
    "BY DEFAULT, IMAPS IS ENABLED ON OPENTOUCH SIDE WITH 'TLS' SECURITY. THAT'S WHY YOU NEED TO MANAGE ON
    EMAIL CLIENT SIDE, THE SAME SECURED CONNECTION ON INCOMING MAIL PARAMETERS. IF YOU WANT TO ENABLE IMAP
    PROTOCOL WITH 'SSL' SECURITY OR IMAP PROCOTOL WITHOUT ANY SECURITY, YOU WILL HAVE TO MODIFY THE PORT
    NUMBER ON OPENTOUCH SIDE (AND TO MAKE SURE THAT CONFIGURATION MATCHES ON CLIENT SIDE). DON'T FORGET TO
    RESTART THE IMAP FRONT-END SERVICE: service imap4fed restart"
  summary: |
    "客户端连不上 IMAP"高发根因：OTMC 侧默认 IMAPS（TLS），端口按安全类型自动带出——客户端选错加密类型即
    失败。要降级到 SSL 或明文 IMAP，必须两侧同步改端口并 service imap4fed restart。验收判据用 IMAP 登录测试
    （p207），别被发信测试带偏（见 n13）。
  conditions: IMAP 客户端对接、IMAP4 Front End 参数调整
  tags: [warning, imap, tls, imap4fed]

- id: n15
  title: 读邮件不会灭 MWI——话机留言灯与邮箱状态不同步
  type: limitation
  source_pages: p171
  source_chapter: SMTP/SMS notification / SMTP notification principle
  source_quote: |
    "MWI: Message Waiting Indicator … MWI on the phone set is not synchronized when reading the email"
  summary: |
    SMTP 通知链路里话机 MWI（新留言 LED 亮）与邮件阅读相互独立：用户在邮箱里听完/读了邮件，话机灯不会自动灭。
    这是机制设计而非故障；用户报"邮件看过了灯还亮着"时按此解释（信箱内处理留言才会更新状态）。
  conditions: 启用邮件通知（wav 附件）场景
  tags: [limitation, mwi, notification]

- id: n16
  title: 通知 SMTP 服务器必须无认证、无 TLS；送达失败基本静默
  type: limitation
  source_pages: p174
  source_chapter: SMTP/SMS notification / SMTP server
  source_quote: |
    "This server must be used without authentication and without TLS. … E-mail acknowledgements are not
    handled for notifications. • An SMTP notification of non delivery is delivered in the mailbox of the valid
    e-mail account and there is no other notification of sending failure • An OpenTouch alarm is generated
    only when the operation of sending mail failed before reaching the SMTP server."
  summary: |
    两条运维盲区：①OTMC 发通知要求 SMTP 服务器开"匿名+明文"（无认证无 TLS）——现代邮件服务器默认关匿名，
    要专门准备；②送达回执不处理：投递失败只在发件账户邮箱里有一封退信，OTMC 侧只有"邮件没到达 SMTP 服务器"
    才告警（并转 SNMP trap）——"用户说没收到通知"要先查发件账户的退信，再查服务器连通。
  conditions: 通知链路部署与排障
  tags: [limitation, smtp, notification, troubleshooting]

- id: n17
  title: 书内口径漂移：OTMC 节点号 98 vs 99；实验网段 151.1.1.x 与 155.1.1.x 混用；掩码示例不一致
  type: version-trap
  source_pages: p84, p92, p94, p95
  source_chapter: OTMC declaration（多处示例）
  source_quote: |
    "Subnetwork-Node number=98" (p94 实施参数) 与 "Node number is a free number. This node number must be
    different than OXE node numbers existing in the OXE network. (Use 99 for example)." (p95 模板说明)
    "nslookup csm.company.com … Address: 155.1.1.3" (p92，拓扑章同设备为 151.1.1.3，p27)
    "c:\>nslookup 155.1.1.50 … Name: otmc.company.com Address: 155.1.1.60" (p94，反查 .50 得 .60)
    "Netmask : 255.255.0.0" (p84 netadmin 输出示例，同页设置表为 255.255.255.0)
  summary: |
    声明章的示例值有四处互相打架：①OTMC 节点号实施写 98、模板举例 99（规则本身一致——自由号、不得撞 OXE
    节点号，照抄哪个都行但要写进文档）；②p92-94 示例突然从拓扑章的 151.1.1.x 切到 155.1.1.x（DNS 服务器
    155.1.1.100）；③p94 反查示例 155.1.1.50 返回的是 155.1.1.60；④p84 netadmin 输出示例掩码 255.255.0.0 与
    同页配置表 /24 不符。结论：示例仅示意，实际以自家拓扑表为准；培训材料引用时别把 98/99、151/155 当成
    "标准值"。（推断：疑似沿自旧版课程的示例残留）
  conditions: 声明与 DNS 核验实验
  tags: [version-trap, inconsistency, lab, dns]

- id: n18
  title: general announcement wav 存放路径两处不一致（p223 与 p227）
  type: limitation
  source_pages: p223, p227
  source_chapter: General announcement / Conclusion & How-To 4
  source_quote: |
    "If a wav file is used, it is stored under: • /var/data/general_announcement" (p223)
    "Transfer the file to the OpenTouch operating system: Suse console /var/ data/ ics-group/general_announcement"
    (p227)
  summary: |
    同一项 wav 文件存放路径，结论页写 /var/data/general_announcement，How-To 操作页写
    /var/data/ics-group/general_announcement。落地时以现场系统实际存在的目录为准（ls 核实），别按单一页码硬
    记。（推断：p227 与统计文件所在 /var/data/ics-group/vms 同族，疑似为 R2.6 实际路径，但教材自身未统一。）
  conditions: wav 方式部署 general announcement
  tags: [limitation, inconsistency, general-announcement]

- id: n19
  title: general announcement 的 "arrive on AA" 播报选项已废弃——外置 VAA 方案下无效
  type: version-trap
  source_pages: p225
  source_chapter: General announcement How-To / 1 Type of announcement
  source_quote: |
    "3 choices are available (one of the 4 existing choices is not more used: on AA). … Warning THE FIELD 'IS
    PLAYED FOR CALLS THAT ARRIVE ON AA' WAS USED WHEN THE AUTOMATED ATTENDANT WAS EMBEEDED IN THE OPENTOUCH
    SERVER. IT WILL HAVE NO IMPACT IN CASE OF (EXTERNAL) VAA SOLUTION USE FOR EXAMPLE."
  summary: |
    播报类型界面留有四个勾选项，但第四项 "Is played for calls that arrive on AA" 是 OT 服务器曾内嵌自动话务员
    （AA）时代的遗留——现在勾了也没用（外置 VAA 方案下无效果）。有效选项只有三个（外呼落箱/内呼落箱/信箱
    查询）。看到四个选项别以为漏配了 AA。
  conditions: TUI global configuration 播报类型设置
  tags: [version-trap, general-announcement, aa]

- id: n20
  title: general announcement 硬限制：单条、新录覆盖旧录、最长 5 分钟、仅 wav 语言可用
  type: limitation
  source_pages: p223
  source_chapter: General announcement / Conclusion
  source_quote: |
    "Only one general announcement can be recorded at a time. • Any new recording will overwrite the previous
    one. • Max duration: 5 minutes … Feature available for languages using Wav files"
  summary: |
    四条硬边界：全系统同时只有一条 general announcement；任何新录制（TUI 或 wav 上传）直接覆盖上一条，没有
    多套轮换；时长上限 5 分钟；功能只在支持 wav 文件的语言下可用。客户提"不同部门不同公告/按季节轮换"的
    需求时，本功能不覆盖——那要走问候语/多站点方案（书中未展开）。
  conditions: general announcement 需求评估
  tags: [limitation, general-announcement]

- id: n21
  title: 通知增值功能一大半是 LS 专属——UM 用户只有基础邮件/短信通知
  type: limitation
  source_pages: p180
  source_chapter: SMTP/SMS notification / Features availability according to voice mail type
  source_quote: |
    "SMS notification V V • Email notification V V • .wav file attached V • Link to My Messaging web V • Call
    back the message sender V • Notification when voice mailbox is full V • Notification when voice mailbox is
    almost full V"（第三列起仅 Local storage 列有 V）
  summary: |
    可用性矩阵：短信通知与邮件通知 LS/UM 都有；但 .wav 附件、My Messaging 链接、回呼留言主、信箱满/近满提醒
    五项全部仅 Local Storage 可用。客户选 UM（Exchange/Domino/Gmail）方案时，售前别按"全套通知"承诺——
    附件听留言、满箱告警这些体验点在 UM 下不存在。
  conditions: 通知方案设计与信箱类型选型
  tags: [limitation, notification, um, local-storage]

- id: n22
  title: SMS 通知必须经 SMTP-SMS 网关，且系统只允许配一个
  type: limitation
  source_pages: p177
  source_chapter: SMTP/SMS notification / SMS notification principle
  source_quote: |
    "An SMS gateway is required for SMS notifications. • SMS notification consists in sending an e-mail to the
    SMS gateway which is in charge of formatting and sending the SMS. • Only one SMS Gateway can be configured
    in the system"
  summary: |
    OTMC 自己不发短信：SMS 通知=给 SMTP-SMS 网关发一封格式化邮件，由网关转 GSM。且全系统只允许配置一个 SMS
    网关（地址格式 SMS$手机号$@域名，p184）——多运营商/多网关分流的需求不支持。网关选型与采购在书外。
  conditions: SMS 通知部署
  tags: [limitation, sms, gateway]

- id: n23
  title: HA 在本书只留指针；启用高可用必须两台服务器同时跑 post-install 向导
  type: limitation
  source_pages: p74
  source_chapter: Post-installation wizard / 1.4 High Availability Parameters
  source_quote: |
    "Disable Checked by default • Enable Checked if high availability has to be deployed. In this case, a
    secondary sever is required and post-installation wizard has to be run at the same time. … The high
    availability configuration and its settings will be explained in a dedicated chapter."
  summary: |
    向导 HA 页默认 Disable。要启用高可用有三个前置：需要副服务器、两台的 post-installation 向导必须同时跑、
    且 HA 的完整配置在"专门章节"（本书不含，属培训课程后续内容）。Starter 教材毕业≠会做 HA——生产 HA 项目
    要补对应课程/文档。
  conditions: 高可用部署
  tags: [limitation, ha, out-of-scope]

- id: n24
  title: 话机复活/注册默认密码 0000——交付后必须改 set secret code
  type: misconception
  source_pages: p113, p116
  source_chapter: Connection user's creation / Resurrection & Static IP configuration
  source_quote: |
    "Resurrection consists in dialing the phone directory number & the password ('0000' by default) directly,
    from the set" (p113)
    "Enter the extension directory number (e.g. 61020) • Enter the 'secret code' ('0000' by default)" (p116)
  summary: |
    数字/模拟话机的 resurrection 密码与 IP 话机注册的 secret code 出厂默认都是 0000——教材当实验便利值用，
    生产里这是"任何人拿到话机就能认领分机"的口子。交付清单里要有"改每台话机 secret code"一项（改法属 OXE
    课程内容，本书未展开）。
  conditions: 话机开通与交付验收
  tags: [misconception, security, phones, default-password]

- id: n25
  title: 原文笔误与时代混用：Red Hat 字样、CheckSytemLinux.sh、MOFIFICATION 等——引用原文要留心
  type: misconception
  source_pages: p52, p53, p84, p66
  source_chapter: Installation Overview / Installation How-To / OXE declaration
  source_quote: |
    "OS installation from boot DVD • Disk partitioning • Red Hat installation • Time zone to define" (p52，
    全书 OS 实为 SUSE，p13/p48/p60)
    "CheckSytemLinux.sh" (p53) 与 "CheckSystemLinux.sh" (p66) 两种拼写并存
    "20. 'APPLY MOFIFICATION'" (p84，MODIFICATION 之误)
  summary: |
    教材残留多处笔误/旧模板痕迹：p52 安装流程里冒出 "Red Hat installation"（本书操作系统是 SUSE Linux
    Enterprise，应视为沿自 OXE 课程模板的笔误）；前置检查脚本 p53 拼作 CheckSytemLinux.sh、p66 拼作
    CheckSystemLinux.sh；p84 APPLY MOFIFICATION 拼错。按脚本/菜单实际能执行的名称操作，文档引用时以 p66
    拼写与 SUSE 口径为准，别把笔误当知识点。（p49 的 Windows 2008 R2 许可键与 p38/p40 的 Windows 2019
    Server 并存属时代混用，8770 与 Fax server 版本要求分属两套，规划时分别核对。）
  conditions: 安装流程执行与文档二次创作
  tags: [misconception, errata, installation]

- id: n26
  title: OTMC-V 虚拟化边界：仅支持 vMotion 与手动/半自动 DRS，其它 VMware 服务不支持
  type: limitation
  source_pages: p15
  source_chapter: OTMC Overview / Virtualization
  source_quote: |
    "OTMC-V can be virtualized with VMware ESXi • vMotion, VMware Dynamic Resources Scheduling (manual
    /semi-automatic) are supported (Other VMware services are not supported) • OTMC-V VM Multi-instance is
    supported on the same physical host • Other applications (ALU-E or 3rd party) on virtual machine are
    allowed to run on the same physical host"
  summary: |
    虚拟化白名单很短：vMotion 与 DRS（手动/半自动）可以开，其它 VMware 服务（HA、FT、备份快照类等未点名
    功能）一概不在支持列表——客户要求"全套 VMware 高可用"时要按支持边界谈。好消息是同主机可多实例 OTMC-V、
    也可混跑 ALE/第三方应用虚机，且虚机版限制与功能等同物理版。
  conditions: OTMC-V 部署与平台规划
  tags: [limitation, virtualization, vmware]

- id: n27
  title: OXE ABC Supra 网络不支持集中式语音邮件（centralized VM）
  type: limitation
  source_pages: p20
  source_chapter: OTMC Overview / Infrastructure (Networking)
  source_quote: |
    "OTMC is supported in centralized and distributed OXE sub-network • Only one SIP trunk towards the front
    node • OXE ABC Supra network not supported for centralized VM"
  summary: |
    组网选型边界：OTMC 支持集中式与分布式 OXE 子网（集中式下也只允许一条 SIP trunk 指向 front node），但 OXE
    的 ABC Supra 网络场景不能上集中式 VM——这类拓扑要做分布式信箱（VPIM 互联）。多站点客户网络盘点时先确认
    是不是 Supra。
  conditions: 多站点/集中信箱方案设计
  tags: [limitation, networking, vpim, topology]

- id: n28
  title: 生产化三件套全部书外：硬件规格与上限、HA、UM（Exchange）配置
  type: out-of-scope
  source_pages: p13, p19, p48, p74, p169
  source_chapter: System architecture / Infrastructure / HA / Notification
  source_quote: |
    "Note: for hardware and software specifications refer to feature list and product limits document" (p13/p48)
    "Scalability must be managed using the OpenTouch Capacity Planning Tool dedicated for OTMC" (p19)
    "Unified Messaging (UM) with Microsoft Exchange, Lotus Domino, or Gmail" (p169，仅一句支持性表述)
  summary: |
    教材只给指针不给内容的三块：①硬件/软件规格与产品上限→feature list 和 product limits 文档；②容量规划→
    OpenTouch Capacity Planning Tool（OTMC 专用，用法未教）；③UM（Exchange/Domino/Gmail）与三方 VM 互通
    （VPIM）→仅声明支持，无任何配置细节；④HA→见 n23。Starter 证书只覆盖"装起来+基础信箱业务"，生产方案
    设计要叠加这些外部资料。
  conditions: 生产项目规划
  tags: [out-of-scope, capacity, um, documentation]

- id: n29
  title: 两个专项配置外指：空间冗余 SIP 网关→TC1652；8770 上 NFS server→TC2024
  type: out-of-scope
  source_pages: p105, p246
  source_chapter: OXE SIP configuration & Backup & Restore
  source_quote: |
    "IN CASE OF OXE WITH SPATIAL REDUNDANCY, A SPECIFIC CONFIGURATION IN OXE WILL HAVE TO BE PERFORM LATER TO
    DECLARE SIP GATEWAYS FOR THE EXTERNAL VOICE MAIL SYSTEMS USE. THIS CONFIGURATION IS GIVEN IN THE TC1652" (p105)
    "A technical communication (TC2024), linked to OpenTouch environment and which is available on the Business
    Portal, explains all implementation steps to deploy a NFS server on the 8770 server" (p246)
  summary: |
    两个触发条件明确、但书内零步骤的场景：①OXE 空间冗余（spatial redundancy）站点接外置语音邮件，要按 TC1652
    另行声明 SIP 网关；②虚拟环境备份用的 NFS server 部署在 8770 上，按 Business Portal 的 TC2024 执行。现场
    遇到这两个前提时，直接取对应 TC 文档，别在教材里找步骤。
  conditions: 空间冗余站点、虚拟环境备份
  tags: [out-of-scope, tc1652, tc2024, redundancy]

- id: n30
  title: 统计输出目录要手工创建、注意读写权限；改完 statistics.properties 必须重启 mascd
  type: warning
  source_pages: p258
  source_chapter: Voicemail statistics How-To / 2.2 Example of file configuration
  source_quote: |
    "The directory '/var/data/ics-group/vms/statistics', where the statistics files are generated, has to be
    created manually first. Take care about the directory 'read & write' permissions!!!"
    "Once the 'statistics.properties' file has been modified, don't forget to stop and start the masc service.
    service mascd stop • service mascd start"
  summary: |
    统计功能两个哑坑：①fileLocation 指向的目录不会自动建——要先手工 mkdir 并确认读写权限（原书连用三个感叹
    号），否则生成静默失败；②改完配置文件必须 service mascd stop/start，不重启等于白改。验收时先确认目录与
    服务，再看文件产出。
  conditions: voicemail statistics 启用
  tags: [warning, statistics, mascd, permissions]
```

## 收尾自检 — 对照 BOOK_OVERVIEW.md 18 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | 部署形态与容量口径决策 | 有 → n26（VMware 边界）、n27（Supra 不支持集中 VM）、n28（规格/容量工具书外） |
| task-02 | 实验拓扑搭建 | 有 → n17（实验口径漂移，拓扑示例值仅示意） |
| task-03 | 许可证体系部署 | 有 → n06（OK 仅文件存在/Skip）、n07（dongle 绑定）、n08（flexlmd 重启） |
| task-04 | OTMC 服务器安装 | 有 → n25（Red Hat 笔误/脚本拼写） |
| task-05 | post-installation wizard | 有 → n01（密码静默）、n02（保留名）、n03（DNS 清单）、n04（安全 OFF）、n05（备份存储） |
| task-06 | 手工装许可 | 有 → n08 |
| task-07 | OXE 声明进 8770 | 有 → n09（APPLY MODIFICATION） |
| task-08 | OTMC 声明与拓扑 | 有 → n17（节点号 98/99、网段漂移） |
| task-09 | OXE SIP 对接 | 有 → n29（空间冗余→TC1652） |
| task-10 | Connection 用户与话机 | 有 → n24（默认密码 0000） |
| task-11 | 账户与信箱交付 | 有 → n21（LS/UM 通知差异）、n11（LS 参数对 UM 无效） |
| task-12 | profile 定制 | 无独立条目——profile 参数为讲义性配置，本章 Warning/Note 已被 p14/principle 覆盖（Check quota 关闭时 Max size 不生效已录入 principle p14 conditions）；无 Warning/Note/Tips 框遗漏。 |
| task-13 | 自助门户 | 无独立条目——web clients 章（p153-166）为界面导览，无 Warning/Note/Tips 框；可见性受授权的 Note 已在 principle/f19 标注。 |
| task-14 | SMTP/SMS 通知 | 有 → n12（模板升级）、n15（MWI 不同步）、n16（SMTP 无认证无 TLS/失败静默）、n21（LS 专属）、n22（单 SMS 网关） |
| task-15 | IMAP 访问 | 有 → n13（OTMC 非 SMTP）、n14（IMAPS 匹配） |
| task-16 | general announcement | 有 → n18（路径不一致）、n19（AA 选项废弃）、n20（硬限制） |
| task-17 | 备份恢复 | 有 → n05（NFS）、n10（删用户入口）、n23（HA 外指）、n29（TC2024） |
| task-18 | 语音信箱统计 | 有 → n30（目录/权限/mascd） |

**统计**：30 条（warning 9 / limitation 11 / version-trap 4 / misconception 4 / out-of-scope 2… 实际按 type 字段：warning n01/n03/n04/n05/n06/n07/n09/n10/n14/n30 共 10 条，limitation n02/n08/n11/n15/n16/n18/n20/n21/n22/n23/n26/n27 共 12 条，version-trap n12/n17/n19 共 3 条，misconception n13/n24/n25 共 3 条，out-of-scope n28/n29 共 2 条）。

### 扫描完整性说明（Warning/Note/Tips 标记框逐页核对）

- 已全部入册的 Warning 框：p73（DNS 前向反向）、p75-76（用户名/密码）、p76-77（dongle 绑定；许可 OK 仅存在性）、p78（Network security OFF）、p84（APPLY MODIFICATION）、p105（空间冗余 TC1652）、p207（OTMC 非 SMTP 的失败说明，并入 n13）、p208（IMAPS 警告）、p223+（GA 路径不一致，比对形成 n18）、p225（AA 废弃）、p243（Alan Alban 警告）、p258（目录权限）。
- 已入册的 Note/Notes：p52（RAID/DNS 前置，纳入 c01 conditions）、p58（VM 规格仅 lab，f10 conditions）、p68（post-install 自动启动，f11）、p72（双以太网同 IP 同 MAC——属信息性说明，非边界，未单列；已记入本说明备查）、p73（NTP 防火墙/虚机同步，principle p02）、p77（USB 导入步骤，n07）、p79（本地备份不推荐，n05）、p82（LICENSES_HOME 变量说明，f06）、p85（siteid/提示符，principle p08）、p92-94（bics.conf/musett.sh/WBM 重置，c04）、p101（站点名配置，c04 步骤 10）、p112-113（建户自动建设备/resurrection，c06）、p115（IP 话机无物理地址，c06）、p116（DHCP 不在培训内，c06 conditions）、p118（计数器含义，p11）、p136（分机号挂钩，principle p12）、p139（profile 强制，principle p13）、p142（问候语详见 QRG，f18）、p150（TUI 密码回落值，p14 conditions）、p173/p178（模板目录/语言，p19）、p180-182（可用性/权限矩阵，p17/n21）、p186（模板升级，n12）、p190（LS 参数显示但无效，n11）、p191（参数按授权可见，f19 conditions）、p225（三选可多选，p21）、p226（录后自动激活，p21）、p240（备份目录/阈值/保留期，p22）、p244（Force 选项，p22）、p245（<5 分钟，p25）、p246（TC2024，n29）、p258（mascd，n30）。
- 已入册的 Tips：p77（Skip 不中断但不工作，n06）、p113-114（resurrection 移机技巧，c06 步骤 3）、p117（许可三族，p11）、p151（无）、p188（信箱完整流程在 Starter 课程，c09 conditions）、p244（返回主页，操作细节未单列）、p258（mascd 重启，n30）。
- 推断性结论已标注"（推断）"：n17（旧课程示例残留）、n18（ics-group 路径疑似实际值）。
- 版本号保留完整位数：OTMC R2.6 / Issue 08、otmc2.6.1_im_InstalManual_8AL90120USAH_1_en、SUSE Linux Enterprise Server 12 (64bits)、Windows 2008 R2、Windows 2019 Server、TC1652、TC2024。
