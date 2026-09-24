# OTFC 盲判结果（仅依据能力目录，锁死后不回改）

should-install-01 | otfax-installation-ftw | 装机前服务器准备（DNS/IIS 角色服务/服务账号）与 FTW 十二项最小配置均在该能力主线内
should-install-02 | otfax-installation-ftw | 每页水印+只能 2 路并发正是评估许可边界（1 实例/2 通道/10 站点/100 用户/水印）的表现
should-sip-01 | otfax-sip-channel-integration | OTFC 接 OXE 属 SIP 通道集成，OXE 侧 MGR 七步菜单是该能力明列内容
should-sip-02 | otfax-sip-channel-integration | OXE 上传真抓包三法 CHtrace/motortrace/tcpdump 在该能力描述内
should-mail-01 | otfax-mail-exchange-integration | Outlook 发传真走 Exchange 'FAX' 地址空间 New-SendConnector，是该能力核心
should-mail-02 | otfax-mail-exchange-integration | 收发正常但通知收不到对应"通知被拦调 Receive Connector"的排查路径
should-user-01 | otfax-user-administration | 有 AD 走内部库与 AD 双源共存，无域账号外包走内部库，属用户管理规划
should-user-02 | otfax-user-administration | 管理员防锁死靠 System/Site 两级+备份管理员，正是该能力描述
should-profile-01 | otfax-profile-policy | 仅国内禁国际正是出方向 Restriction group 的典型用法
should-profile-02 | otfax-profile-policy | 邮件通知 Profile 每语言一份、勾 Exchange integration 只影响邮件不影响 Web 界面
should-dir-01 | otfax-directory-routing | 目录查得到但用不了对应 Site/Profile Lookup 两表没配即拒用
should-dir-02 | otfax-directory-routing | 33 开头与 00 开头的格式转换靠 Modification Table 规整号码
should-svc-01 | otfax-services-operations | 整体重启用 xmsc -ra/-oa/-aa，日志默认 20MB/15 天归档均在此能力
should-svc-02 | otfax-services-operations | Trace 目录每组件一个日志，ConfigManager.log 与 Smtp.log 排障明列于此
should-bk-01 | otfax-backup-upgrade | 升级五步法与"数据库 CompanyConfig/XmediusArchive 不在自动备份内"正是该能力
should-bk-02 | otfax-backup-upgrade | 零保留靠传真记录与传真文档分开/一起删，属备份删除策略能力
should-cli-01 | otfax-client-coversheet | 500 台批量装客户端对应静默安装+GPO 批量与 ClientRedistribution 精简包
should-cli-02 | otfax-client-coversheet | 封页 .cse 五步（Editor/下载底稿/另存/Web 导入/挂 Profile）在此能力
should-plan-01 | otfax-solution-planning | 用户数/端口数/协议速率属 sizing，指向 OTFC Features List，售前方案评估能力
should-plan-02 | otfax-solution-planning | 一台传真服务器接两台 OXE 与号段规划对应多网关号段分流
should-rpt-01 | otfax-reports-monitoring | 报表模板数量与自定义（BIRT 设计器）属报表监控能力
should-rpt-02 | otfax-reports-monitoring | 网管告警对接是 SNMP V2 trap 清单，属监控能力
should-user-03 | otfax-user-administration | 时区影响封页/报头/通知三处时间戳，属用户属性管理
should-dir-03 | otfax-directory-routing | 按被叫号码路由用 $did:?????$ 规则，属来传真路由三类规则
bait-install-01 | otfax-mail-exchange-integration | 症状是"邮件收发不正常"，排查走 SMTP 网关监听 25/不能与其他 SMTP 共存；IIS 只是猜测项，根因域在邮件集成
bait-sip-01 | otfax-sip-channel-integration | OXE 侧 MGR 七步参数（含编码、号码变换，参照 TC3048）正是该能力覆盖的配置域
bait-mail-01 | otfax-profile-policy | 通知模板按语言走 Profile 的邮件通知（每语言一份），换模板属 Profile 通知配置
bait-user-01 | otfax-directory-routing | AD 查得到但用不了的根因是 Site/Profile Lookup 授权没配，不是再建同名账号
bait-profile-01 | otfax-profile-policy | 骚扰传真拒接主叫是入方向站点级 Calling Number Restriction，题面"出方向限制组"是误导，能力域仍是 Profile 策略
bait-svc-01 | otfax-backup-upgrade | 备份停服但不可 kill 的规则写在备份策略能力里，强杀服务属于该域的禁忌操作
bait-cli-01 | otfax-mail-exchange-integration | SendFAX 的 Outlook 模式走邮件寻址通路（[FAX:] 寻址格式/SMTP），重装客户端不解决，排查域在邮件集成
bait-rpt-01 | otfax-reports-monitoring | 31 个模板只有全系统/单用户维度，按部门需 BIRT 自定义，判断依据仍在报表能力内
bait-plan-01 | otfax-solution-planning | 端口全表一律指向 OTFC Features List，属方案评估能力的资料索引
edge-ha-01 | otfax-services-operations | XMFaultTolerance 是该能力点名的有状态复制服务，双机部署问题首先落在服务架构域
edge-tls-01 | otfax-sip-channel-integration | SIP 信令加密证书配置最贴近 SIP 通道集成域；若教材未覆盖证书细节则属边界外推
edge-mail-02 | otfax-mail-exchange-integration | 不部署邮件服务器、直连 SMTP 网关，对照"前置邮件服务器四大好处/SMTP 网关监听 25"
edge-fire-01 | otfax-installation-ftw | 防火墙关闭是安装阶段语境（同域还有禁用 SMTP 释放 25 端口），生产环境取舍属安装准备边界
