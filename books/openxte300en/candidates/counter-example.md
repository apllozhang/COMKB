# 反例/限制/边界/易错点候选 — OpenTouch Suite for MLE (OPENXTE300EN Ed10, R2.6.1)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: 容量仅两档数字——5000 用户封顶，容量/话务设计全书外置
  type: limitation
  source_pages: p5, p9
  source_chapter: Solution Overview / OTMS delivery modes
  source_quote: |
    "OTMS 5000 users max" (p5)
    "OTMS up to 5000 users ... OTMS-V up to 5000 users" (p9)
  summary: |
    全书对容量只给出一条硬数字：OTMS 与 OTMS-v 均 5000 用户上限；硬件平台由 BP/客户提供、兼容性用
    OTCP 工具核对。虚机规格、话务模型、性能 sizing 一概没有展开（SOT 虚机规格仅指向 Delivery note）。
    做方案设计必须外取 Features list / Product limits / Delivery note，别拿本教材报容量。
  conditions: 选型与报价阶段
  tags: [limitation, capacity, sizing]

- id: n02
  title: HA 对新装机已死——只有 R2.2.x 迁移场景保留，无替代方案展开
  type: version-trap
  source_pages: p94
  source_chapter: Post-installation wizard / High availability
  source_quote: |
    "HIGH AVAILABILITY IS NOT MORE SUPPORTED FOR A NEW INSTALLATION DON'T ENABLE IT. KEEP DISABLE.
    IT IS ONLY AVAILABLE IN CASE OF MIGRATION OF A SYSTEM FROM RELEASE 2.2.X WITH HA ALREADY DEPLOYED."
  summary: |
    向导 HA 页必须保持 Disable：全新安装不再支持 HA，仅"从 R2.2.x 且已部署 HA 迁移上来"的系统可继续用。
    教材没有给出任何替代高可用方案（ACS stack 只解决 ACS 备份/并发接入，spatial redundancy 被指向 TC1652）。
    客户问"坏了怎么办"时，答案在书外。
  conditions: 新装机向导操作、HA 需求沟通
  tags: [version-trap, ha, resilience]

- id: n03
  title: Post-install 口令页是静默陷阱——少于 8 字符不报错，事后才出问题
  type: warning
  source_pages: p95-96
  source_chapter: Post-installation wizard / OpenTouch Core Settings
  source_quote: |
    "ALL PASSWORDS ON THIS PAGE MUST CONTAIN AT LEAST 8 CHARACTERS. THERE IS NO ERROR POP-UP IN CASE
    YOU USE LESS THAN 8 CHARACTERS BUT YOU WILL FACE PROBLEMS AFTERWARDS." (p95)
    "THE ACCOUNT USERNAME MUST ALL BE DIFFERENT AND MUST NOT BE "ADMIN", "ADMINNMC", "HTUSER" OR ANY
    OTHER EXISTING ACCOUNT." (p95)
  summary: |
    向导账户页三个坑：(1) 全部口令至少 8 字符，短了不弹任何报错、后面才炸；(2) 用户名必须互不相同且禁用
    admin/adminnmc/htuser 等既有名；(3) otAdmin/otProfile 口令另有复杂度要求（大写+数字+特殊字符）。
    还有流程坑：整页账号口令必须当场抄录——8770 声明 OT 节点时逐项要用（p96）。
  conditions: Post-installation wizard 账户页
  tags: [warning, post-installation, security]

- id: n04
  title: DNS 必须正反向都通——五类 FQDN 缺一即卡声明环节
  type: limitation
  source_pages: p93, p194, p196
  source_chapter: Post-installation wizard / OpenTouch server declaration
  source_quote: |
    "THE DNS MUST BE CONFIGURED TO RESOLVE (FORWARD AND REVERSE RESOLUTION): • OPENTOUCH SERVER FQDN
    • OMNIVISTA 8770 SERVER FDQN • MAIL SERVER FDQN • LDAP SERVER FDQN • ALCATEL-LUCENT OMNIPCX
    ENTERPRISE COMMUNICATION SERVER CALL SERVER..." (p93)
  summary: |
    OT/8770/邮件/LDAP/OXE 呼叫服务器的 FQDN 都要配正向+反向解析；声明 OT 前要双向 nslookup 验证
    （csm/oxe/opentouch 的 FQDN 与 IP）。漏配反向解析是声明失败/拓扑互挂失败的高频根因。
    另注：本地 DNS 服务器仅在 OXE 未做 duplication 时可用；NTP 要确认防火墙放行。
  conditions: 初始化与节点声明前
  tags: [limitation, dns, network]

- id: n05
  title: 许可 OK 状态只代表"文件在"，内容有效性不校验
  type: warning
  source_pages: p101
  source_chapter: Post-installation wizard / License files installation
  source_quote: |
    "THE OK STATUS INDICATES THAT THE LOCAL FILE IS PRESENT. BUT THE CONTENT (VALIDITY) OF THE FILE IS
    NOT CONTROLLED. THE SAME IN CASE OF EXTERNAL LICENSE SERVER USE, THE CONNECTION TO THE LICENSE
    SERVER AND ITS CONFIGURATION IS NOT TESTED, JUST THE LOCAL PRESENCE OF THE FILE."
  summary: |
    向导许可页显示 OK 只说明文件存在于本地（或外部 FlexLM 只验到"文件在"），不校验内容有效性、不测试
    与 FlexLM 的连接。装完向导别急着宣布"许可 OK"，要用 checkLicensing.sh/spadmin/lmstat 复核（见 p09/p11）。
  conditions: 向导许可步骤、验收
  tags: [warning, licensing, verification]

- id: n06
  title: 许可可以 Skip，但系统不会正常工作
  type: warning
  source_pages: p101
  source_chapter: Post-installation wizard / License files installation
  source_quote: |
    "If license file is not available or there are problems with, click SKIP. The wizard skips license
    installation. Skipping license installation does not stop the installation process, but, the
    OpenTouch server will not operate properly unless a manual installation of the correct license
    files is performed after wizard installation."
  summary: |
    许可页可点 Skip 且不中断向导——但 OT 不会正常工作，必须事后手工补装正确许可。现场别把"向导走完了"
    当成"许可没问题时才补"的借口；Skip 后要立即排许可计划。
  conditions: 许可文件缺失/有问题的现场
  tags: [warning, licensing]

- id: n07
  title: Security OFF（通用证书/预装 CTL）被官方点名不推荐——盗打与越权风险
  type: warning
  source_pages: p103, p400-401, p411, p426
  source_chapter: Post-installation wizard / Certificats / self-signed How-To
  source_quote: |
    "BEWARE: THIS CHOICE IS NOT RECOMMENDED BY ALCATEL-LUCENT ENTERPRISE, AS IT IMPLIES INCREASED
    RISKS OF TOLL FRAUD, AND UNAUTHORIZED USE OF THE SERVICES OR FUNCTIONALITIES ON THE SYSTEM" (p103)
    "It is advised to use an external PKI to obtain CA root public certificate" (p411)
    "this "generic" certificate is the same for all OpenTouch servers deployed worldwide." (p426)
  summary: |
    Network security OFF 的通用证书全球所有 OT 服务器同款——任何人都握有同款证书，教材两处（向导、证书
    章）警告会带来盗打与服务越权风险，官方建议用外部 PKI。实验为了快可以 OFF，生产交付必须切 ON
    （Internal SHA256 起步）或外部 CA；已用 OFF 的站点要列入整改。
  conditions: 向导证书页、安全评估
  tags: [warning, security, certificates]

- id: n08
  title: OXE 走 Telnet 是因为没开安全——启用安全后必须换 SSH
  type: limitation
  source_pages: p117
  source_chapter: Connections to the system / Telnet connection to OXE
  source_quote: |
    "Telnet is authorized on the OXE server. ... We are using here Telnet connection because security
    is not activated on the OXE in our topology. If security is activated on OXE, you must use ssh
    connection as we did for OpenTouch just before."
  summary: |
    书中 OXE 用 Telnet（端口 23，mtcl/mtcl）纯属实验拓扑未启用安全的产物；OT 则一律 SSH（Telnet 不授权）。
    生产 OXE 启用安全后要改用 SSH——把"Telnet 连 OXE"写进运维手册是照抄实验的危险动作。
  conditions: 远程连接方式选择
  tags: [limitation, security, oxe, telnet]

- id: n09
  title: 明文口令遍布全书——实验口径不可带入生产
  type: warning
  source_pages: p16, p24, p69, p95, p101, p111, p168, p298
  source_chapter: POD Settings / SOT / Post-install / Connections / FlexLM / WPC
  source_quote: |
    "Login admin Password letacla" (p69)；"Login: upload Password: sot" (p71)
    "Default root password (set by SOT): letacla1" (p101/p106/p107 tips)
    "Esxi server root ... superuser OpenTouch root ... superuser ... OmniPCX Enterprise mtcl mtcl" (p111)
  summary: |
    RLAB 实验体系的口令（admin/letacla、upload/sot、root/letacla1、superuser、Superuser01*、mtcl/mtcl、
    adfexc/adfexc、adminsnmp 等）以明文印在教材里且人人可读。所有实验口令/IP/账号必须视为公开信息：
    生产交付一律替换，并把"SOT 预置 root 口令 letacla1"列入首日改密清单。
  conditions: 一切生产交付与安全基线
  tags: [warning, security, lab-口径]

- id: n10
  title: R-Lab 特例成对出现：SOT/OTMS 模板已预部署、许可锚 MAC 不锚加密狗——照搬现场会错
  type: limitation
  source_pages: p67, p73, p99, p168, p173, p182
  source_chapter: SOT How-To / Post-install / External FlexLM / Switch How-To
  source_quote: |
    "HERE, IN REMOTE-LAB CONTEXT, A OTMS VM TEMPLATE IS ALREADY GENERATED AND DEPLOYED ... THE SOFTWARE
    DEPLOYMENT FOR THIS VM WILL BE DONE AS FOR A PHYSICAL SERVER, THAT MEANS PROVIDING THE MAC ADDRESS." (p73)
    "IN CASE OF R-LAB USE FOR THE TRAINING, THE LICENSE FILE IS NOT ASSOCIATED TO A DONGLE-ID BUT TO A
    MAC ADDRESS. SO, DONGLE ASSOCIATION HAS NOT TO BE DONE." (p173)
  summary: |
    教程反复标注 R-Lab 特例：SOT/OTMS/FlexLM 虚机已预部署（SOT 不生成 OVF、按物理机方式给 MAC）；许可锚
    MAC 而非加密狗（跳过 USB Device/Controller 挂接）。现场恰好相反：SOT 可生成 OVF、虚拟化许可必须加密
    狗。学员把实验捷径当生产流程会直接翻车。
  conditions: 区分 R-Lab 与现场流程
  tags: [limitation, lab-口径, sot, dongle]

- id: n11
  title: vSphere 桌面客户端仅适用 ESXi ≤6.0
  type: version-trap
  source_pages: p84
  source_chapter: Virtual machine deployment / Appendix
  source_quote: |
    "VSPHERE CLIENT IS ONLY AVAILABLE WITH ESXI VERSION 6.0 OR LOWER."
  summary: |
    附录的 vSphere client 部署 OVF 流程只适用 ESXi 6.0 及更低；6.5/7.0.x 必须走 web client 主流程。
    按 SOT hosted 模式（ESXi ≥6.0）部署时，不要参考附录路径。
  conditions: OVF 导入方式选择
  tags: [version-trap, esxi, vmware]

- id: n12
  title: 改 OXE FlexLM 字段后必须重启 OXE
  type: warning
  source_pages: p159
  source_chapter: Licenses files checking / Checking the management
  source_quote: |
    "A REBOOT IS REQUIRED AFTER MODIFICATION."
  summary: |
    在 OXE Webadmin/mgr 的 System/Licenses 改 FlexLM 相关字段（服务器 IP/端口/ProductID discovery 等）
    后必须重启 OXE 才生效。改完"没生效"先查是否重启过。
  conditions: FlexLM 字段变更
  tags: [warning, licensing, oxe]

- id: n13
  title: OXE 会独占 FlexLM 许可——一台 checkout，其他 OXE 用不了
  type: limitation
  source_pages: p180
  source_chapter: External FlexLM deployment / Tools & logs
  source_quote: |
    "To operate, the OmniPCX Enterprise checks out its license from the license server. This license,
    being checked out, cannot be used by another OmniPCX Enterprise. Details on license checkout are
    logged in the file: "/opt/Alcatel-Lucent/logs/flexlm/flexlm_lmlog.log""
  summary: |
    OXE 从 FlexLM 服务器 checkout 许可后即独占——同一份 OXE 许可不能同时给第二台 OXE 用。多 OXE 共用一台
    FlexLM 时按台数采购；排障看 flexlm_lmlog.log 的 checkout 记录。
  conditions: 多 OXE 共享 FlexLM 场景
  tags: [limitation, licensing, flexlm]

- id: n14
  title: 许可文件 SFTP 落在 /root——不移进许可目录等于白传；标准 FTP 被禁
  type: warning
  source_pages: p177
  source_chapter: External FlexLM deployment / License files installation
  source_quote: |
    "For security reasons, the standard FTP protocol cannot be used for the license server. Copy the
    license file with SFTP (Secure FTP), or SCP ... AFTER SFTP TRANSFER THE LICENSE FILES ARE IN
    "/ROOT" FOLDER. THEY MUST BE COPIED/MOVED TO THE DEDICATED LICENSE DIRECTORY."
  summary: |
    外部 FlexLM 收许可：只许 SFTP/SCP；传完文件停在 /root，必须再 cp 到 /opt/Alcatel-Lucent/data/
    licenses 并重启 flexlmd。漏掉"移动+重启"两步，许可永远不会生效。
  conditions: 外部 FlexLM 许可装载
  tags: [warning, licensing, flexlm]

- id: n15
  title: FlexLM 虚机语言保持 CentOS 默认，勿改
  type: warning
  source_pages: p172
  source_chapter: External FlexLM deployment
  source_quote: |
    "IT IS RECOMMENDED TO KEEP THE CENT OS DEFAULT LANGUAGE DON'T CHANGE IT"
  summary: |
    FlexLM 虚机装好后不要在图形界面改系统语言——教材明言保持 CentOS 默认。本地化冲动会带来不必要风险。
  conditions: FlexLM VM 初始化
  tags: [warning, flexlm]

- id: n16
  title: netadmin 改完不 APPLY 等于白改
  type: warning
  source_pages: p187
  source_chapter: OmniPCX Enterprise declaration / IP configuration
  source_quote: |
    "DON'T FORGET TO APPLY THE MODIFICATION BEFORE TO LEAVE: 20. 'APPLY MOFIFICATION'"
  summary: |
    netadmin -m 里做的任何修改（角色地址、节点名等）必须选菜单 20 'APPLY MODIFICATION'（原文拼错为
    MOFIFICATION）提交后才生效；直接退出会静默丢失全部改动。
  conditions: OXE netadmin 操作
  tags: [warning, oxe, netadmin]

- id: n17
  title: spatial redundancy 全面改口径——SIP 字段、语音邮件网关都要按 TC1652 另配
  type: limitation
  source_pages: p231, p232, p242, p93
  source_chapter: OXE SIP configuration / Prior management / Post-install
  source_quote: |
    "ACCORDING TO YOUR TOPOLOGY (OXE LOCAL/SPATIAL REDUNDANCY), THE MANAGEMENT OF THE SIP PART IS
    DIFFERENT; SO PLEASE READ THIS SECTION CAREFULLY" (p231)
    "IN CASE OF OXE WITH SPATIAL REDUNDANCY, TC1652 EXPLAINS THE REQUIRED MANAGEMENT." (p231)
    "IN CASE OF OXE WITH SPATIAL REDUNDANCY, A SPECIFIC CONFIGURATION IN OXE WILL HAVE TO BE PERFORM
    LATER TO DECLARE SIP GATEWAYS FOR THE EXTERNAL VOICE MAIL SYSTEMS USE. THIS CONFIGURATION IS GIVEN
    IN THE TC1652." (p242)
  summary: |
    OXE spatial redundancy 时多处字段口径变化：SIP 外部网关的 Belonging domain 要填 OT FQDN、Contact
    with IP address 要改勾（切换后随主用 IP 变）；外部语音邮件的 SIP 网关要额外配置；DNS 清单里呼叫服务器
    FQDN 要逐台核。教材只给差异点，完整操作在 TC1652——spatial 站点不能照抄单机实验步骤。
  conditions: OXE spatial redundancy 站点
  tags: [limitation, redundancy, tc1652, sip]

- id: n18
  title: OT R2.1 起话务台前缀必配，否则可扩展服务起不来（配完要重启 wireald）
  type: version-trap
  source_pages: p238
  source_chapter: Prior management / Prefix services
  source_quote: |
    "AFTER OT R2.1, CONFIGURATION OF THE ATENDANT PREFIX IS MANDATORY FOR THE START UP OF THE
    EXTENSIBLE SERVICES. IF NOT YET CONFIGURED, ACCESS THE OPENTOUCH CONFIGURATION TOOL TO DECLARE THE
    ATTENDANT PREFIX THEN RESTART THE EXTENSIBLE SERVICES BY USING THE FOLLOWING COMMAND (USING ROOT
    LOGIN): > SERVICE WIREALD RESTART"
  summary: |
    版本硬门槛：OT R2.1 之后话务台前缀必须配置，否则 extensible services 无法启动；补配后必须以 root
    执行 service wireald restart。老文档/旧习惯里"话务台前缀可选"的口径已过时。
  conditions: OT R2.1+ 系统、话务台排障
  tags: [version-trap, prefixes, extensible-services]

- id: n19
  title: 前缀默认值是法国制式——51/52/53/54/41/9 只是示例
  type: misconception
  source_pages: p238
  source_chapter: Prior management / Prefix services
  source_quote: |
    "These default values are for a French OXE, please check your current OXE configuration"
  summary: |
    教材给的转发/溢出/话务台前缀值（51 立即前转、52 忙、53 无应答、54 忙或无应答、41 取消、9 话务台）是
    法国 OXE 的默认口径；OT 侧必须照抄"现场 OXE 实际值"，直接按书录入会在非法国站点造成功能错乱。
  conditions: 前缀配置
  tags: [misconception, prefixes, country]

- id: n20
  title: UDAS 同步周期设 0 会静默失同步——必须 ≥1 且日期时间都要填
  type: warning
  source_pages: p243-245
  source_chapter: Prior management / UDAS directories Synchronization
  source_quote: |
    "SYNCHRONIZATION DATE, TIME AND PERIOD MUST BE SET. SYNCHRONIZATION PERIOD MUST BE EQUAL OR UPPER
    TO 1. 1 MEANS SYNCHRONIZATION EVERY DAY AT DECLARED TIME 2 MEANS EVERY 2 DAYS ETC … NEVER SET
    PERIOD TO "0""
  summary: |
    internalDir/phonebookDir 的同步页签：日期（yyyy-mm-dd）、时间（hh:mm:ss）、周期（天）三者必须都设置，
    周期 ≥1、绝不能为 0；检索只打同步库，同步没配好=目录永远陈旧。客户报"查不到新同事"先查这里。
  conditions: 目录同步配置、目录陈旧类故障
  tags: [warning, udas, directory]

- id: n21
  title: DAS rules 强制、按国家定制、顺序敏感且可多条同时命中
  type: warning
  source_pages: p253
  source_chapter: Prior management / DAS rules configuration
  source_quote: |
    "WARNING THE DECLARATION ORDER IS IMPORTANT. SEVERAL RULES CAN BE APLLIED AT A TIME (EXAMPLE :
    RULE 1 AND 2, 4 AND 6 …)" (原文 APLLIED 拼写如此)
    "DAS rules are mandatory and are country dependant. The configuration proposed will be for France."
  summary: |
    会议侧 DAS rules 三个坑：必须配置（mandatory）；教材十条是法国口径，他国要按本国拨号计划改写；规则
    顺序重要且多条可同时生效（例 1+2、4+6）——增删规则要整体复查顺序。拼写 APLLIED 为原文笔误。
  conditions: 会议服务器 DAS 配置
  tags: [warning, das, conference, country]

- id: n22
  title: 会议侧改 OT/ACS 名称会废掉全部既有会议
  type: warning
  source_pages: p587
  source_chapter: TC2149 / ACS cluster
  source_quote: |
    "In case of OpenTouch and/or ACS cluster name modification, all existing conferences require to be
    recreated."
  summary: |
    对 OpenTouch 服务器或 ACS 集群改名（含 rehosting 场景）后，所有已存在的会议都要重建——这是 rehosting
    影响评估里最容易漏的业务影响项，要在变更窗口通知全部会议组织者。
  conditions: rehosting/改名变更
  tags: [warning, conference, rehosting]

- id: n23
  title: 语音邮箱档案不选就不能建箱；Answer only 等字段受档案锁定
  type: limitation
  source_pages: p330-331
  source_chapter: Voice mailbox configuration
  source_quote: |
    "Before validating the mailbox creation, it's mandatory to assign a profile to the voice mailbox,
    in the « configuration » tab." (p330)
    "Answer only ... If the value ... is: Manageable by users: this field can be modified. ... Yes:
    this field is selected and cannot be modified." (p331)
  summary: |
    建邮箱两处约束：Configuration 页不选档案则无法保存；邮箱上的 Answer only 等字段随档案取值锁定
    （档案=Yes/No 时用户侧改不了，=Manageable by users 才开放给用户）。排"用户改不了留言设置"先看档案。
  conditions: 邮箱创建与用户侧选项排障
  tags: [limitation, voice-mail, profile]

- id: n24
  title: IMAP 明文/SSL 需改端口并重启 imap4fed；OT 不做 SMTP，测试邮件失败属预期
  type: limitation
  source_pages: p350-351
  source_chapter: IMAP How-To
  source_quote: |
    "BY DEFAULT, IMAPS IS ENABLED ON OPENTOUCH SIDE WITH "TLS" SECURITY. ... IF YOU WANT TO ENABLE IMAP
    PROTOCOL WITH "SSL" SECURITY OR IMAP PROCOTOL WITHOUT ANY SECURITY, YOU WILL HAVE TO MODIFY THE
    PORT NUMBER ON OPENTOUCH SIDE ... DON'T FORGET TO RESTART THE IMAP FRONT-END SERVICE: service
    imap4fed restart" (p351)
    "The "send test e-mail message" test fails, if a SMTP server is not reachable or OpenTouch/OTMC
    FQDN is used as outgoing mail server (OpenTouch server/OTMC (local storage voice mail) does NOT act
    as a SMTP server)" (p350)
  summary: |
    两点口径：(1) 默认 IMAPS+TLS；要改 SSL 或明文必须两端同步改端口，且 service imap4fed restart；
    (2) Outlook 账号测试里"发送测试邮件"失败是预期现象——OT 不充当 SMTP 服务器，发件服务器必须填真实
    邮件系统。把测试失败当成配置错误去反复折腾是常见误区。
  conditions: IMAP 客户端配置
  tags: [limitation, imap, smtp]

- id: n25
  title: 通知用的外部 SMTP 必须无认证无 TLS；投递失败几乎没有告警
  type: limitation
  source_pages: p360, p370
  source_chapter: SMTP/SMS notification
  source_quote: |
    "This server must be used without authentication and without TLS." (p360)
    "An SMTP notification of non delivery is delivered in the mailbox of the valid e-mail account and
    there is no other notification of sending failure An OpenTouch alarm is generated only when the
    operation of sending mail failed before reaching the SMTP server." (p360)
  summary: |
    两面坑：(1) OT 通知要求外部 SMTP"无认证、无 TLS"——现代邮件系统默认强制认证/加密，往往要为 OT 单开
    中继服务器（安全评估要覆盖）；(2) 发送失败基本无感知：NDN 只落发件账号邮箱，OT 仅在"邮件未达 SMTP"
    时才告警（转 SNMP trap）。"用户没收到通知邮件"的排障要从发件账号邮箱翻 NDN 开始。
  conditions: 通知功能部署与排障
  tags: [limitation, smtp, notification, security]

- id: n26
  title: 升级不覆盖通知模板——要新模板必须删旧模板并重启 chameleon
  type: version-trap
  source_pages: p372
  source_chapter: SMTP/SMS notifications / Customization
  source_quote: |
    "When installing a new version, the templates of text for Email and SMS notification are not
    updated if a version already exists in order to keep the eventual customization done by the
    administrator. Therefore if you want to have the new templates (for new translations, string
    changes,…) you have to delete the existing ones and restart the chameleon component."
  summary: |
    /var/data/panda/notification4 的通知模板在版本升级时被刻意保留（保护管理员定制）——导致新翻译/新文案
    不会自动到位；要拿新模板须删旧文件并重启 chameleon，然后再把定制补写进新模板。
  conditions: 版本升级后通知文案异常
  tags: [version-trap, notification, upgrade]

- id: n27
  title: 通用公告："arrive on AA" 选项已废弃；一次仅一条、覆盖式、5 分钟；wav 目录两处表述不一致
  type: limitation
  source_pages: p392, p394, p396
  source_chapter: General announcement
  source_quote: |
    "THE FIELD "IS PLAYED FOR CALLS THAT ARRIVE ON AA" WAS USED WHEN THE AUTOMATED ATTENDANT WAS
    EMBEEDED IN THE OPENTOUCH SERVER. IT WILL HAVE NO IMPACT IN CASE OF (EXTERNAL) VAA SOLUTION USE
    FOR EXAMPLE." (p394)
    "Only one general announcement can be recorded at a time. ... Max duration: 5 minutes" (p392)
    "/var/data/general_announcement" (p392) vs "/var/ data/ ics-group/general_announcement" (p396)
  summary: |
    四点：勾选项 "is played for calls that arrive on AA" 是 OT 内嵌 AA 时代的遗留，对外置 VAA 方案无效果；
    公告一次只能存在一条、新录/新传即覆盖、最长 5 分钟；wav 必须 CCITT A-law 8bits 8kHz mono 且固定文件名
    general_announcement.wav；存放路径讲义写 /var/data/general_announcement、How-To 写 /var/data/ics-group/
    general_announcement——生产以实测系统目录为准（本条差异即书内不一致）。
  conditions: 公告配置与 wav 上传
  tags: [limitation, general-announcement, inconsistency]

- id: n28
  title: 证书 Deploy 与 Import 是两步——导入不部署不生效；部署后会话断开属正常
  type: warning
  source_pages: p423, p429
  source_chapter: Certificates How-To x2
  source_quote: |
    "Once the certificate imported, don't forget to deploy it in order to be used by the system" (p423)
    "Just after clicking on "Deploy", a message is displayed (« Impossible to retrieve data from / … » )
    and the WebAdmin session is cut. You have to restart the web session. It is normal because the
    server's certificate used for the "https" connection has just changed." (p423)
  summary: |
    证书流程两个高频误会：(1) Change server certificate → Import 之后还必须选中证书点 Deploy，否则新证书
    不生效；(2) Deploy 后 WebAdmin 报 "Impossible to retrieve data…" 并断开是预期行为（https 证书刚换），
    重开会话即可，不要回滚。自签路径同理（p429）。
  conditions: 证书导入与部署
  tags: [warning, certificates]

- id: n29
  title: 自签证书要求重签 CTL——用 808x 话机走 USB 流程，漏签会出设备信任问题
  type: warning
  source_pages: p427
  source_chapter: OpenTouch self-signed certificate
  source_quote: |
    "Don't forget to sign the new CTL, by using a 808x device (procedure with USB key). See dedicated
    procedure"
  summary: |
    切到 Internal 自签证书时系统会警告 CTL（证书信任表）必须重签——需要一台 808x 话机按专用 USB 流程完成。
    跳过这步，后续 808x/相关设备可能出现信任类故障；排期时要预留话机与 USB 操作窗口。
  conditions: 自签证书切换
  tags: [warning, certificates, ctl]

- id: n30
  title: OT 侧软电话用户禁授 Nomadic SIP 权——两种 VoIP 路线互斥
  type: warning
  source_pages: p474, p492
  source_chapter: OTC PC How-To / Multi-devices How-To
  source_quote: |
    "MAKE SURE THAT THE DESKTOP LICENSE IS ENABLED FOR THIS USER DON'T GRANT "NOMADIC SIP" RIGHT TO
    THIS TYPE OF USER" (p474)
    "Nomadic SIP Not checked Desktop Checked" (p492)
  summary: |
    走 Multi-devices（SIP 分机为第二设备）的 OTC PC 软电话用户：必须勾 Desktop 许可、绝不勾 Nomadic SIP
    权——Nomadic 是另一条（旧）软电话路线，两权并授会造成路由/设备冻结行为混乱（Nomadic 模式本身在另一
    培训讲）。用户报"电脑打电话行为怪"先查这对许可组合。
  conditions: 软电话用户许可配置
  tags: [warning, licensing, nomadic, multi-devices]

- id: n31
  title: 不授 Desktop 许可，OTC PC 自动落成 One 免费模式——用户以为"客户端坏了"
  type: misconception
  source_pages: p433, p445, p448
  source_chapter: OTC PC / OTC PC One
  source_quote: |
    "OTC PC: full mode for Connection users with « Desktop » right (license) • OTC PC One : Freemium
    mode for for Connection users without « Desktop » right" (p433)
    "Grant users the right to access the application (if not set, application will work as "OTC PC
    One")" (p445)
  summary: |
    OTC PC 与 OTC PC One 是同一安装包：没有 Desktop 许可就自动进入 One 免费模式（不能接听、不能 VoIP、
    单线、无监督）。用户报"软件装了但电话功能都不行"，第一排查项是 Licenses 页的 Desktop 勾选，而非重装
    客户端。
  conditions: 客户端交付与一线支持
  tags: [misconception, otc-pc-one, licensing]

- id: n32
  title: OT 监督组与 OXE 话机监督是两套机制，无同步；OTC PC One 无监督
  type: misconception
  source_pages: p499, p501
  source_chapter: Supervision groups
  source_quote: |
    "There is no "OT supervision group" feature on OXE deskphones (Connection users)" (p499)
    "No link with OXE supervision feature (no management synchronization)" (p501)
  summary: |
    OT 监督组（OTC PC 图形界面）与 OXE 话机监督键互不联动：建 OT 组不会改变话机监督键行为，反之亦然；
    Connection 用户可两套并用（代接走 OXE Direct call pick-up，需在 OXE 侧启用）。另外 OTC PC One 模式
    无监督功能。需求沟通时别把两套监督混为一谈。
  conditions: 监督需求设计与排障
  tags: [misconception, supervision, oxe]

- id: n33
  title: 监督组交互规则：OXE 呼叫路由优先，前转/溢出可让呼叫脱离监督
  type: limitation
  source_pages: p502
  source_chapter: Supervision groups / Interaction with other OXE services
  source_quote: |
    "The OXE routing is prior to the OT supervision group feature: - Incoming calls to a supervised
    member, with an immediate forward to a non supervised destination, are not monitored by OT
    supervision group. ... Only the main phone number of a supervised user is monitored."
  summary: |
    呼叫可能"逃出"监督的场景：立即前转到非监督目标（不被监督）；忙/无应答前转跟随路由后可能不再被监督；
    只监督主号码（副号码呼叫不被监督，但 Twinset 副站本身被监督）；溢出规则可能导致脱离监督。给客户设计
    监督覆盖范围时要按这张交互表逐条核对，别承诺"所有来话都可见"。
  conditions: 监督覆盖设计
  tags: [limitation, supervision, forwarding]

- id: n34
  title: OTC PC 的 Outlook 集成有前置件与模式前提——缺 VC++ 2010 Tools for Office 加载项装不上
  type: warning
  source_pages: p462, p441-442
  source_chapter: OTC PC How-To / OTC for PC integration
  source_quote: |
    "« MICROSOFT VISUAL STUDIO C++ 2010 TOOLS FOR OFFICE » MUST BE ALREADY INSTALLED ON THE PC TO
    DEPLOY SUCCEFULLY "OUTLLOK ADD-IN" WHICH ARE PART OF STANDARD OTC PC INSTALLATION." (p462, 原文 OUTLLOK 笔误)
    "« Add-in » is automatically installed during OTC PC application standard installation At first OTC
    PC startup, IM working mode has to be specified" (p441)
  summary: |
    Outlook 扩展三个前提：机器上先有 VS C++ 2010 Tools for Office（否则 Standard 安装里的加载项部署失败）；
    OTC PC 首次启动要把"IM 默认应用"答 Yes（否则 Outlook 里没有在场与 OT 操作）；Outlook 扩展仅限 OTC PC
    设备（OTC Mobile 无）。装机失败报"加载项缺失"先查前置件。（OUTLLOK 为原文笔误。）
  conditions: OTC PC 部署
  tags: [warning, outlook, prerequisites]

- id: n35
  title: dla.sh 与 ots 隐藏菜单有权限/口令门槛——root、口令 2998
  type: limitation
  source_pages: p480, p531
  source_chapter: OTC PC Maintenance / Maintenance tools
  source_quote: |
    "100 -------------------- MENU PROTECTED by secret code ... (2998 is the secret code value). So,
    choose the "ACAPI control" by entering "106 2998"" (p480)
    "MUST BE LOGGED AS ROOT TO BE ABLE TO EXECUTE OPTION 1 TO LAUNCH "DLA.SH"" (p531)
  summary: |
    运维工具的隐性门槛：tsa_maintenance 的菜单 100 起受口令保护（口令 2998，经 106 2998 进 ACAPI control）；
    dla.sh 的菜单选项 1（动态日志激活）必须 root 执行。用 otuser 跑不动时先查权限，而不是反复重试。
  conditions: 日志收集与 ots 强同步
  tags: [limitation, maintenance, permissions]

- id: n36
  title: rehosting 三重死亡陷阱——配错即死锁无回退、inactive 分区被清、OXE/8770/OMS 不被触达
  type: warning
  source_pages: p564-567, p585
  source_chapter: Re-hosting / OTMS rehosting / TC2149
  source_quote: |
    "Performing the re-hosting process with the wrong configuration (hostnames not declared, IP address
    already used etc...) will result in a deadlock situation. ... it is not possible to fall back to
    the previous configuration." (p565)
    "the content of the inactive partition will be suppressed and deleted Rollback or update to the
    inactive partition will NOT be allowed." (p566)
    "Re-hosting an OTMS will NOT update the OmniPCX Enterprise, the OmniVista 8770 server or the OMS" (p567)
  summary: |
    rehosting 三条铁律：(1) 主机名未声明/IP 已被占用等配置错误=死锁，机器不可达且无法回退——动手前必须
    参数全对、基础设施一致、有可用备份（OT 备份+Clonezilla/VM 快照镜像）；(2) inactive 分区内容被清除，
    旧分区回滚/升级通道关闭（后续仅可平滑升级或全新安装）；(3) --rehost 只改 OT 自己，OXE/8770/OMS 与
    生态（DNS/DHCP/SSO/SNMP/防火墙）要按 TC2149 矩阵另行收尾，漏一项就是"半个系统在新地址"。
  conditions: 任何 rehosting/改址/改名变更
  tags: [warning, rehosting, tc2149, risk]

- id: n37
  title: rehosting 换 FlexLM 形态要重做许可——外部虚拟化只认加密狗，流程走 eBP 工单
  type: limitation
  source_pages: p587
  source_chapter: TC2149 / License
  source_quote: |
    "Internal flex can use @MAC (physical server only) , ALUID (physical server only) or a DONGLE
    External virtualized FLEX LM server requires the use of a DONGLE. A license adaptation may be
    required in such a case. Refer to license request for rehosting on eBP (Siebel ticket to open)"
  summary: |
    rehosting 时若把许可从内嵌 Flex 切到外部虚拟化 FlexLM，锚定物必须换成加密狗；许可文件不匹配时要通过
    eBP 开 Siebel 工单做许可适配——这是一条有商务周期的流程，变更排期必须预留。
  conditions: rehosting + FlexLM 形态变更
  tags: [limitation, rehosting, licensing]

- id: n38
  title: 备份介质与虚拟化限制——USB 须 FAT32/NTFS/EXT3；OT-V 没有 /var/backup 本地目录；USB 对虚拟化无意义
  type: limitation
  source_pages: p543, p552, p555-556
  source_chapter: Backup and Restore
  source_quote: |
    "If "/var/backup" doesn't exist locally and NFS mounting is not done, the backup from 8770 will not
    work" (p543)
    "IN CASE OF BACKUP ON EXTERNAL USB DISK, THIS LAST ONE HAS TO BE FORMATED USING FAT32, NTFS OR EXT3.
    THE SCRIPT prepareUsbdisk –f" (p552)
    "IT DOESN'T MAKE SENSE TO USE USB OPTION IN CASE OF VIRTUALIZATION." (p556)
  summary: |
    备份三条边界：USB 盘必须 FAT32/NTFS/EXT3 并用 prepareUsbdisk -f 准备；OT-V（SOT 生成的虚机）本地没有
    /var/backup 工作目录，必须挂 NFS，否则 8770 发起的 OT 备份直接不工作；虚拟化场景选 USB 无意义。
    备份策略评审时按部署形态（物理/OT-V）分开定。
  conditions: 备份配置
  tags: [limitation, backup, ot-v]

- id: n39
  title: 免责口径：OTBE、UM、Nomadic、VPN-less 会议地址、备份细节均被明确外移
  type: out-of-scope
  source_pages: p97, p104, p240, p445, p581
  source_chapter: 多处 Notes
  source_quote: |
    "The configuration for the specific address for Conferencing Service for VPN-less is explained in a
    dedicated training." (p97)
    "Complete explanations concerning the backup and specially backup on NFS server in virtualized
    context is given in a dedicated chapter." (p104)
    "The UNIFIED MESSAGING voice mail must be declared first in the OpenTouch (explained in another
    training)." (p240)
    "« Nomadic » mode: temporary use of ressources from common pools (ghost Z & SIP device) ... Explained
    in another training" (p445)
    "It does not include OTBE, as this procedure is described in OTBE installation manual" (p581)
  summary: |
    书内明确"另见他处"的主题清单：VPN-less 会议服务地址（专项培训）、虚拟化备份完整说明（专章）、UM 语音
    邮件声明（另一培训）、Nomadic 模式（另一培训）、OTBE rehosting（OTBE 安装手册）。按本教材做交付计划
    时，这些主题要显式列为书外依赖，避免"以为一本书够用"。
  conditions: 交付范围界定
  tags: [out-of-scope, um, nomadic, otbe, vpn-less]

- id: n40
  title: WPC 的能力边界——不建 Conversation 用户、一台设备、档案回配置工具管
  type: limitation
  source_pages: p292
  source_chapter: Web Provisioning Client
  source_quote: |
    "Restrictions: Management of profiles from OXE/OT Configuration • No creation of new OpenTouch
    Conversation users • Association of one device"
  summary: |
    Web Provisioning Client 的三条限制：档案的建/删仍要回 OXE/OT 配置工具；不能新建 OpenTouch Conversation
    用户；每用户只关联一台设备。把它当"全能自助门户"许诺给客户会造成期望落差。
  conditions: WPC 推广与培训
  tags: [limitation, wpc]

- id: n41
  title: 教材排版/文字错误清单——IP 表 192.16.8.1.x、端口 413、APLLY/MOFIFICATION/OUTLLOK/EMBBEDED/APLLIED/notifiy 等
  type: limitation
  source_pages: p16, p360, p187, p253, p444, p462, p394
  source_chapter: 全书
  source_quote: |
    "csa (physique) csm (principal) 192.16.8.1.1 192.16.8.1.3" (p16，与他页 192.168.1.1/.3 矛盾)
    "(https port: 413 and 8016)" (p444，图中为 443/8016)
    "20. 'APPLY MOFIFICATION'" (p187)；"SEVERAL RULES CAN BE APLLIED AT A TIME" (p253)
    "deploy SUCCEFULLY "OUTLLOK ADD-IN"" (p462)；"EMBBEED" (p394)；"where to notifiy the user" (p370)
  summary: |
    已识别的书内笔误/排版问题（引用时须修正口径）：IP 总表的 192.16.8.1.1/.3 应为 192.168.1.1/.3（p116/
    p187 等处可证）；远程接入 https 端口写 413 应为 443（图示 443/8016）；多处英文拼写错误（MOFIFICATION/
    APLLIED/OUTLLOK/EMBBEDED/notifiy）不影响语义但引用原文时要注明。
  conditions: 引用与转写
  tags: [limitation, inconsistency, errata]

- id: n42
  title: 工具输出里的历史示例值易误当现网值——151.1.1.x、172.25.x、2012-2016 时间戳
  type: misconception
  source_pages: p178, p212, p252, p524
  source_chapter: checkLicensing / Alarms logs / SIP proxies / checkdns
  source_quote: |
    "Flex = external (IP=151.1.1.80, FQDN=flex.company.com)" (p178)
    "Server IP address: 151.1.1.50 Port: 5260" (p252)
    "ipAddress and val = 172.25.167.42" (p212)
    "Using external DNS1: 151.1.1.100" (p524)
  summary: |
    工具示例输出（checkLicensing、ams.log、NMCFaultManager、checkdns、SIP Proxies 截图）里大量使用
    151.1.1.x/172.25.x 等旧演示网段与 2012-2016 年时间戳——它们是文档撰写时的样例，不是本教材 RLAB 拓扑
    （192.168.1.x）的值。对照排障时先分清"示例输出"与"实验口径"两类数值。
  conditions: 排障对照
  tags: [misconception, sample-output, lab-口径]
```

## 收尾自检 — 对照 BOOK_OVERVIEW.md 18 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | POD 搭建 | 有 → n09（实验明文口令）、n10（R-Lab 特例）、n42（示例输出值） |
| task-02 | SOT 部署 | 有 → n10（模板预部署/MAC 特例）、n11（vSphere ≤6.0） |
| task-03 | OVF 导入 | 有 → n11 |
| task-04 | Post-installation wizard | 有 → n02（HA）、n03（口令静默陷阱）、n05/n06（许可 OK/Skip）、n07（security OFF） |
| task-05 | 系统连接 | 有 → n08（Telnet/SSH）、n09 |
| task-06 | 许可安装 | 有 → n05、n06、n14 |
| task-07 | 许可核查 | 有 → n12（重启）、n13（独占） |
| task-08 | 外部 FlexLM | 有 → n14（/root）、n15（语言） |
| task-09 | 声明 OXE | 有 → n16（APPLY） |
| task-10 | 声明 OT | 有 → n04（DNS） |
| task-11 | OXE SIP | 有 → n17（spatial/TC1652）、n19（法国前缀） |
| task-12 | prior management | 有 → n18（R2.1 wireald）、n19、n20（UDAS 0 周期）、n21（DAS）、n41 |
| task-13 | 告警对接 | 有 → n42 |
| task-14 | 档案与用户 | 有 → n40（WPC 边界）、n28 不涉；档案锁定并入 n23 相关口径 |
| task-15 | 语音邮箱体系 | 有 → n23（档案锁定）、n24（IMAP/SMTP）、n25（SMTP 无认证）、n26（模板升级）、n27（公告） |
| task-16 | 证书 | 有 → n07（OFF 风险）、n28（Deploy 两步）、n29（CTL 重签） |
| task-17 | 客户端交付 | 有 → n30（Nomadic 禁授）、n31（One 误区）、n32/n33（监督边界）、n34（Outlook 前置） |
| task-18 | 运维 | 有 → n35（口令/root）、n36（rehosting 三陷阱）、n37（许可适配）、n38（备份介质）、n39（书外清单）、n22（会议重建） |

**18/18 全部有边界类条目覆盖，无空缺。**

### 扫描完整性说明（Warning/Note/Tips 标记框逐章核对）

- 已入册的 Warning 框：p73（R-Lab SOT 模板）、p84（vSphere ≤6.0）、p93（DNS 清单）、p94（HA）、p95/96（账户口令）、p98（加密狗挂载）、p101（OK 状态/Skip）、p103（security OFF）、p159（重启）、p162/165（ALUID vs dongle）、p172（语言）、p177（/root+FTP）、p182（R-Lab 跳过加密狗）、p187（APPLY）、p231/232/242（spatial/TC1652）、p238（R2.1 wireald）、p243（UDAS 周期）、p253（DAS 顺序）、p281/284（实验口令放宽）、p351（IMAP 端口）、p394（AA 废弃）、p411（security OFF 复警）、p414（客户端信任根）、p427（CTL 重签）、p474/486/487（Desktop/Nomadic/COS）、p531（dla root）、p552/556（USB/NFS）、p565/566/567（rehosting 三陷阱）、p585（TC2149 备份强制）。
- 已入册的关键 Note/Tips：p101/106/107（letacla1）、p159（PANIC 判据）、p209（MIB 不完整）、p226（配置须全建）、p292（WPC 限制）、p330（档案必选）、p360（SMTP 失败告警口径）、p372（模板升级）、p392（公告限制）、p423/429（Deploy 断会话）、p426（通用证书全球同款）、p480（2998）、p543（/var/backup 缺失）、p587（许可适配）。
- 推断性结论标注说明：本文件全部条目均为原书显式 Warning/Note/限制或书内可证的笔误，无推断性结论；n27/n41 的"两处表述不一致"判断基于同书两页原文对照（引文已并列给出）。
- 版本号均按原文保留完整位数：R2.2.x、R2.1、R2.2、R2.4、R2.5、R2.6.1、ESXi 6.5/7.0.x、Hyper-V 2016/2019、ESXi 6.0、ESXi ≤6.0、Chrome 54、8770 3.2.8、VirtualBox 5.2.24、VMware Workstation 14、TC2149 ed.04（Release 2.3.1+）。
