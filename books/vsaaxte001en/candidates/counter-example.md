# 反例/限制/边界/易错点候选 — Visual Automated Attendant (VSAAXTE001EN Ed20, R4.8.006)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: VAA 4.8.006 只能"全新安装 + 数据库恢复"，原地升级不存在
  type: version-trap
  source_pages: p78, p80, p89, p308
  source_chapter: S.O.T summary / MANUAL INSTALLATION / Install the VAA application / UPDATE A VAA VERSION
  source_quote: |
    p78/p80: "For VAA version 4.8.006, only an installation from scratch followed by a database restore is supported."
    p89: "Important information to read carefully before installing VAA 4.8.006: • Only a fresh installation followed by a database restoration is supported. • A new license (Release 11) is required."
  summary: |
    同一句警告在书中出现三次：4.8.006 的唯一支持路径是全新安装后恢复数据库备份，且强制换 Release 11 新许可。
    把"升级 VAA"理解成"跑一遍新版 install.sh 就完事"会直接失败；迁移项目要按重装 + 恢复排期。
  conditions: 4.8.006 版本口径；新版本以官方说明为准
  tags: [version-trap, installation, licensing]

- id: n02
  title: G729 编解码与语音识别互斥——要 ASR 必须 G711
  type: limitation
  source_pages: p42, p101
  source_chapter: High level software architecture / install.sh codec step
  source_quote: |
    p42: "Note: G729 can't be used with Automatic Speech Recognition feature"
    p101: "Do not use G729 if you want to use speech recognition - If you are unsure about this setting, select G711a, G711mu and G729. If you intend to use Speech Recognition, you must use a G711 codec. Accepting other codecs will cause issue with speech recognition."
  summary: |
    两处一致的口径：勾选 G729 就不能开 ASR；要用语音识别，编解码必须用 G711，接受其他编解码会导致识别故障。
    规划 ASR 功能时先把编解码方案定死，否则识别表现为"莫名不准/不识别"。
  conditions: ASR 为 Google ASR
  tags: [limitation, codec, asr]

- id: n03
  title: 规格/端口/兼容表只是示例——原文两处"务必查官方文档"
  type: limitation
  source_pages: p52, p53, p55
  source_chapter: Server prerequisites / Virtualized environment / TCP-UDP port usages
  source_quote: |
    "Given as an example! Always consult the official documentation!" (p52 与 p53 同句重复)
    "The remote SSH access for the ROOT account is forbidden. You must use the admin account with the function 'sudo'." (p55)
  summary: |
    服务器规格表、Hypervisor 兼容表与端口清单都标注"仅示例，务必查官方文档"。教材数值只能做初筛，
    投标/交付文档引用时必须带免责边界并对照 Installation Manual 最新版。p55 端口清单正文只有一句安全规则。
  conditions: 任何选型与防火墙设计场景
  tags: [limitation, sizing, documentation]

- id: n04
  title: HA 从属机只读——故障期间无统计，Master 恢复后不自动回同步
  type: limitation
  source_pages: p44, p47, p240, p245, p255
  source_chapter: High availability / spatial redundancy use cases / vaa ha free / slave web
  source_quote: |
    p44: "The slave VAA database is in ReadOnly mode. Therefore, no statistics will be recorded for a call handled during the failure period on the PCS side."
    p47: "No database synchronisation will be performed when master VAA will be recovered. Web client must reconnect (to Slave VAA)."
  summary: |
    三条易踩点：①Slave 库只读——故障期间它接的呼叫不产生统计（话务报表会出现缺口）；②Master 恢复后不自动回同步，
    必须手工 vaa ha resync，否则两台配置分叉；③Web 客户端要手动重连（到 Slave）。把"双机"理解成"全自动无缝"
    是误解——丢话与统计缺口是设计行为。
  conditions: Master/Slave HA 部署
  tags: [limitation, ha, statistics]

- id: n05
  title: 任何切换都丢进行中呼叫（三用例重复三遍）
  type: limitation
  source_pages: p45, p46, p47
  source_chapter: OXE local & spatial redundancy – 3 use cases
  source_quote: |
    "Existing ongoing calls are lost when switch over occurs" (p45、p46、p47 三处重复出现)
  summary: |
    呼叫服务器切换、主 VAA 丢失、WAN 断三种切换场景，进行中呼叫一律丢失——这句话原书重复三遍，是客户预期管理
    的硬口径。向客户承诺"高可用不掉话"会直接违约；SLA 条款要写清只保证新呼叫接续。
  conditions: 所有冗余场景
  tags: [limitation, ha, sla]

- id: n06
  title: N+1 中 reference VAA 挂了——其余照跑但不能改任何配置
  type: limitation
  source_pages: p51
  source_chapter: Multiple VAA in N+1 redundancy mode
  source_quote: |
    "If 'reference VAA' becomes unavailable, the other VAAs continue to operate but any configuration changes is impossible during the 'reference VAA' unavailability … The overall capacity decreases during the downtime period of failed VAA"
  summary: |
    N+1 的配置基准机不可用期间：业务可续、容量下降、但全系统配置冻结。要改脚本/提示音得等它恢复——
    把 reference 放在维护窗口外、或把"改配置"排进它宕机期间的运维计划都会落空。
  conditions: N+1 扩容型部署（与 Master/Slave 冗余型不同）
  tags: [limitation, n+1, configuration]

- id: n07
  title: multi-company 共享媒体服务器，不能为公司预留端口
  type: limitation
  source_pages: p50
  source_chapter: Integration with OXE multi-company feature
  source_quote: |
    "The Visual Automated Attendant Media Server is shared by all companies • It's not possible to reserve ports for a given company"
  summary: |
    OXE 多公司场景下 VAA 媒体服务器被各公司共享，无法为某公司独占端口配额。客户提"给 A 公司保底 20 路 IVR"
    这类需求时，产品机制不支持，只能靠扩容或拆 VAA 变通（拆分方案的边界书内未展开）。
  conditions: OXE multi-company 集成（细节见 TBE083）
  tags: [limitation, multi-company, capacity]

- id: n08
  title: 空间冗余在 Purple On Demand（OPEX）下不支持
  type: limitation
  source_pages: p46, p305
  source_chapter: OXE spatial redundancy / Purple On Demand
  source_quote: |
    p46: "Spatial redundancy is not supported in Purple On Demand solution"
    p305: "OPEX oriented license management mechanism based on Purple On Demand offer"
  summary: |
    跨数据中心的空间冗余与 OPEX（Purple On Demand）许可模式互斥。客户既要按用量付费又要异地容灾时，
    两个诉求撞车——售前阶段就要二选一或改用传统 CAPEX。
  conditions: OPEX 模式评估
  tags: [limitation, opex, redundancy]

- id: n09
  title: PCS 应急配置在网络恢复后即丢失
  type: limitation
  source_pages: p49, p301
  source_chapter: PCS support（两处同义重复）
  source_quote: |
    p49: "PCS VAA can be configured for local emergency purposes. Anyway, configuration will be lost once network failure is solved."
    p301: "PCS VAA can be configured for emergency purposes, but configuration will be lost once network failure is solved."
  summary: |
    断网期间在 PCS VAA 上做的本地应急配置是临时的——网络一恢复就丢。应急操作的价值仅限于"撑过断网窗口"，
    恢复后要以中心配置为准重新核对，别把应急态当成新基线。
  conditions: PCS 场景断网期间
  tags: [limitation, pcs]

- id: n10
  title: root 禁止 SSH 远程登录——远程连 root 失败是设计不是故障
  type: limitation
  source_pages: p55, p81
  source_chapter: TCP/UDP port usages / VAA distribution installation
  source_quote: |
    p55: "The remote SSH access for the ROOT account is forbidden. You must use the admin account with the function 'sudo'."
    p81: "SSH remote access is forbidden for the root account, you must be connected as superuser to perform the installation: sudo su"
  summary: |
    root 只能本地控制台登录；远程一律 admin + sudo su。现场习惯性"ssh root@vaa"连不上属于安全基线（CIS-2）的
    预期行为，不要去"修复"它，更不要打开 root 远程。
  conditions: 全版本通用
  tags: [limitation, security, ssh]

- id: n11
  title: 升级时选切 HTTPS 会擦除现有配置；S.O.T 只能自签证书
  type: warning
  source_pages: p57
  source_chapter: Switching VAA to HTTPS
  source_quote: |
    "In case of an update, if the HTTPS configuration is already set on the VAA server, no modification will be performed. • If it's not the case, the installer has the possibility to switch the VAA web access to HTTPS or to keep the HTTP access. If the installer chooses to switch to HTTPS, the actual configuration will be erased."
    "Special case with S.O.T: The VAA server installed with the S.O.T will have a self-signed certificate as we can't provide certificate files."
  summary: |
    两个证书坑：①旧版（<4.6.104）升级到仅 HTTPS 版本时，若原来没有 HTTPS 配置，选择切换会擦除现有配置重来；
    ②S.O.T 安装的 VAA 只能用自签证书（工具无法提交证书文件）——要上真证书必须走手工安装路径或事后 vaa conf https 换。
  conditions: 跨版本升级与 S.O.T 部署
  tags: [warning, https, certificate, sot]

- id: n12
  title: Web 管理默认 admin/admin 且首连强制改密——漏改等于裸奔
  type: warning
  source_pages: p22, p80, p114
  source_chapter: WEBADMIN / MANUAL INSTALLATION / Testing the connection
  source_quote: |
    p22: "Login: admin - Password: admin - The password for the admin account must be changed on 1st connection."
    p80: "At the end of the VAA installation, to connect to the web GUI, use: Login : admin - Password : admin"
    p114: "The password of the admin account used for web connection must be changed on 1st use."
  summary: |
    Web 管理出厂凭证是 admin/admin，三处提醒首连必改。跳过改密直接投入使用的系统等于把 IVR 管理权暴露给
    任何知道默认口令的人。同类系统级默认口令还有 letacla1（root/admin，p80）。
  conditions: 安装与交付验收
  tags: [warning, security, default-credentials]

- id: n13
  title: 新建管理员默认密码=其用户名（原书 Warning 大写强调）
  type: warning
  source_pages: p128
  source_chapter: VAA WebAdmin application
  source_quote: |
    "Warning BY DEFAULT THE PASSWORD OF THE NEW ACCOUNT IS IDENTICAL TO THE IDENTIFIER OF THE LATEST."
  summary: |
    在 Administrators 页新建账号（如 letacla）后，默认密码就是用户名本身——建完不改密，等于给全系统留了一个
    可猜解的入口。开账号流程必须内置"立即改密"一步，并把这条写进交付检查单。
  conditions: 创建任何新管理员/用户账号
  tags: [warning, security, accounts]

- id: n14
  title: SMTP 配置改完必须重启服务
  type: warning
  source_pages: p130
  source_chapter: VAA WebAdmin application / Settings tab
  source_quote: |
    "Warning SERVICES MUST BE RESTARTED AFTER SMTP CONFIGURATION"
  summary: |
    Admin 菜单 Settings 里改 SMTP 通知参数后，服务必须重启才生效——只点保存不重启，告警邮件不会发出，
    排障时会误判为"SMTP 服务器不通"。
  conditions: 修改 SMTP/告警设置
  tags: [warning, smtp, alerts]

- id: n15
  title: Supervision 页的停止/重启按钮不要随意按
  type: warning
  source_pages: p131
  source_chapter: VAA WebAdmin application / Supervision tab
  source_quote: |
    "Don't use these buttons unless instructions from the technical support team"
  summary: |
    WebAdmin 的 Supervision 页提供停止/重启 VAA 服务的按钮，原书明确"除非技术支持指示，否则不要用"。
    现场自行动手重启服务可能中断进行中呼叫；日常重启走 SSH 的 vaa restart 并选对窗口。
  conditions: 日常运维
  tags: [warning, maintenance, services]

- id: n16
  title: 实验：不要启动 VAA Slave 虚机（配对实验环境约定）
  type: warning
  source_pages: p64, p248
  source_chapter: Pod Configuration / Install HA
  source_quote: |
    p64: "Check that the following virtual machines have started. Don't start the 'VAA slave' instance."
    p248: "HA configuration is performed from the master server"
  summary: |
    实验口径：基础实验阶段（c01-c15）VAA Slave 虚机保持关机，到 HA 章才启用；HA 配置一律从 master 发起。
    提前开 slave 不会得到"自动同步的备机"——没有 addslave 动作它只是台独立 VAA。
  conditions: RLAB 培训环境
  tags: [warning, lab, ha]

- id: n17
  title: 通配符路由表达式"可用但不推荐"
  type: limitation
  source_pages: p28-29
  source_chapter: ROUTING NUMBERS / SPECIFIC CASE
  source_quote: |
    "Possible use but not recommended (See chapter 4.3 Disambiguation about routing expressions in the Administration guide) • ?: to match any number • *: to match any number of digits • [firstNumber]-[lastNumber]: Assign a range of numbers to a tree structure - Recommended use for better readability • Assign a single number to each tree"
  summary: |
    VAA 路由支持 ? / * / 号段通配符，但原书标注"可用但不推荐"，推荐一号一树。通配符的歧义消解规则在
    Administration Guide 4.3——用通配符出的路由问题（号码被别的树抢走）教材不负责解释。
  conditions: 配置路由号码
  tags: [limitation, routing]

- id: n18
  title: 两个破坏性同步——OXE 电话簿同步清空目录、CSV 导入清空过滤器
  type: warning
  source_pages: p32-33
  source_chapter: FILTERS / DIRECTORY
  source_quote: |
    p32: "A filter can be created by importing a CSV file or entering an expression • A CSV import deletes all created entries"
    p33: "Directory management •Manual creation •OXE phonebook synchronization - An OXE synchronization deletes all created entries"
  summary: |
    过滤器 CSV 导入会删除已建条目、目录做 OXE 电话簿同步会删除全部手工条目——两个"导入即清库"的操作。
    混用手工维护与定期同步的方案必然丢数据；同步/导入前先导出备份。
  conditions: 目录与过滤器维护
  tags: [warning, directory, filters, destructive]

- id: n19
  title: 提示音格式与命名硬约束（8KHz PCM 16-bit 单声道、名称无空格）
  type: limitation
  source_pages: p34, p138
  source_chapter: PROMPTS MANAGEMENT / Manage Prompts
  source_quote: |
    p34: "Import of wav files •Format: 8KHz PCM 16-bits mono"
    p138: "Wav files uploaded to prompts should have the format: 8 KHz, PCM 16 bits mono. … No space in the name"
  summary: |
    WAV 必须 8KHz/PCM/16bit/单声道，提示音名称不能含空格。客户给的录音室级高码率文件直接上传会不可用或音质异常，
    要先转格式；名称带空格在引用时会出问题。
  conditions: 提示音导入
  tags: [limitation, prompts]

- id: n20
  title: PicoTTS 不建议生产；云 TTS/ASR 依赖 Google 账号且收费
  type: limitation
  source_pages: p34, p36-37, p141
  source_chapter: PROMPTS MANAGEMENT / TTS / ASR
  source_quote: |
    p141: "The Pico TTS engine can be used free of charge and without an internet connection. But it is not recommended for production. - Google Cloud is recommended but NOT free (credit card required)"
    p141: "The information presented in this documentation may be inaccurate or out of date, as these prices and features may be updated at any time by the Cloud Text to Speech vendor"
    p37: "Google speech to text service (Google Cloud account required) & API key required"
  summary: |
    引擎选型三边界：①内置 Pico 免费离线但官方明说"不建议生产"；②生产推荐 Google Cloud TTS——收费、要信用卡、
    许可不经 ALE；③ASR 必须 Google Cloud 账号 + API key。离线/内网/国产化环境的替代方案教材完全没有覆盖——
    这是真实交付的常见堵点。
  conditions: TTS/ASR 选型
  tags: [limitation, tts, asr, cloud]

- id: n21
  title: 树节点不命名 = 放弃统计排障能力（原书三处强调）
  type: misconception
  source_pages: p145, p165, p175, p187
  source_chapter: FEATURES LIST / Use case 1-3 Implementation
  source_quote: |
    p145: "It is IMPERATIVE to personalize the NAME of each block when configuring a tree! This name is used by statistics and will facilitate the analysis"
    p165/p175/p187: "The name of the nodes is essential for understanding the statistics"
  summary: |
    节点名直接进统计与呼叫日志（逐节点时长记录）。随手默认名（Announcement1/Menu1）的系统，出问题时
    呼叫日志读不出任何语义——"树能跑就行"的认识是错的，命名是交付质量的一部分。
  conditions: 全部树设计
  tags: [misconception, tree-design, statistics]

- id: n22
  title: 多语言树的欢迎语/语言选择语必须双语同文件
  type: warning
  source_pages: p187-188, p193-194
  source_chapter: Use case 3 / Implementation 与 Tree creation
  source_quote: |
    p187: "The Welcome prompt must be recorded in both languages in the same WAV file, because the choice of languages is only made after its broadcast."
    p194: "The language choice prompt must be recorded in both languages in the same WAV file, because the choice of languages is only made after its broadcast"
  summary: |
    语言选择发生在播报之后，所以语言选择之前的所有提示（欢迎语、语言菜单引导语）必须把两种语言录在同一个
    WAV 文件（或 TTS 串联两条）。按"每语言一个文件"的直觉做法会在语言选择前只放一种语言，双语 callers 听不到
    自己语言的引导。
  conditions: 多语言树设计
  tags: [warning, multilanguage, prompts]

- id: n23
  title: SQL 节点四个易错点——慢查询/单字段/首条结果/空结果非错误
  type: limitation
  source_pages: p207-208, p323
  source_chapter: SQL REQUEST NODE / external database How-To
  source_quote: |
    p207: "Using too many database queries and SQL procedures in a script can delay the overall call duration"
    p323: "An empty result does not generate an SQL error … The VAA can only recover one field at a time. … In case of multiple results, the VAA returns the first occurrence only."
  summary: |
    四条：①脚本里塞太多查询/存储过程会拖长呼叫时长（caller 体验为"IVR 卡"）；②一次只取一个字段，要多字段发多条 SQL；
    ③多条结果只取第一条；④空结果不报 SQL 错——只判"SQL 失败"不判"空结果"的树，查无此人时会静默走错分支。
    正确姿势：Condition 判非空 + 红色连线接失败提示（c18 步骤 6-7）。
  conditions: SQL 节点设计
  tags: [limitation, sql, database]

- id: n24
  title: SQL 节点安全口径——库连接应定义在公司设置，不要手工配
  type: warning
  source_pages: p207
  source_chapter: SQL REQUEST NODE
  source_quote: |
    "For security reasons, it is recommended to use a database defined in the company settings. - Do not use manual configuration"
  summary: |
    外部数据库连接应通过公司设置（Tenant/Settings → External Databases）统一定义并加凭证管理，
    不要在 SQL 节点里手工填连接——凭证散落在脚本里既难审计也难轮换。
  conditions: SQL 节点配置
  tags: [warning, sql, security]

- id: n25
  title: JDBC 驱动目录不能直接 SFTP；HA 两台都要装
  type: limitation
  source_pages: p320
  source_chapter: Preamble: jdbc pilot installation
  source_quote: |
    "sudo mv /home/admin/mssql-jdbc-9.4.1.jre8.jar /opt/ale/aa-webapp/lib • It is not possible to make a sftp directly in the directory /opt/ale/aa-webapp/lib … Note: in HA mode, the driver must also be on the slave VAA."
  summary: |
    驱动安装路径固定两段式：SFTP 只能到 /home/admin，再 sudo mv 到 /opt/ale/aa-webapp/lib，重启 aa-webapp 生效。
    两个坑：试图直接 SFTP 到 lib 目录会失败；HA 只在 master 装驱动——切换后 slave 跑 SQL 节点即故障。
  conditions: 外部数据库集成（MS SQL/Oracle 等非默认驱动）
  tags: [limitation, jdbc, ha]

- id: n26
  title: Oracle 两种连接串不等价，可能只有一个能通
  type: limitation
  source_pages: p325
  source_chapter: APPENDIX: Connect an Oracle database
  source_quote: |
    "jdbc:oracle:thin:@10.20.30.11:1521:VAA … VAA is the TNS service name … jdbc:oracle:thin:@(description=(address=…)(connect_data=(service_name=VAA))) … VAA is the 'SERVICE_NAME' … These 2 connection strings are not equivalent and it is possible that only one will work."
  summary: |
    TNS 服务名式与 service_name 长串式看着像同义，实际不等价——取决于 Oracle 服务端配置，可能只有一个能连。
    连接串必须向客户 Oracle 管理员索取，不能凭格式猜测；两种都试是正常排障动作而非蛮干。
  conditions: Oracle 数据库接入（附录内容）
  tags: [limitation, oracle, jdbc]

- id: n27
  title: MS SQL 三个默认值陷阱——TCP/IP 禁用、1433 不再预分配、首登仅 Windows 认证
  type: limitation
  source_pages: p330-333
  source_chapter: MS SQL Express installation
  source_quote: |
    p330: "By default, TCP/IP connection are not allowed"
    p331: "By default, the historic port 1433 is not assigned anymore (depending on MS SQL server release). ­ Check if port 1433 is assigned. If not assign it!"
    p332: "Note : First authentication is in 'Windows Authentication' mode only"
  summary: |
    新装 MS SQL Express 的三连坑：TCP/IP 协议默认禁用；1433 端口默认不再分配（要手工指定静态端口）；
    首次登录只有 Windows 认证（要给 VAA 用 SQL 账号必须切 mixed mode 并重启服务）。"装完连不上"九成栽在这三处。
  conditions: MS SQL Express/Server 接入
  tags: [limitation, mssql, database]

- id: n28
  title: 生产数据库账号权限要最小化，测试库的 vaa 全权限不可照搬
  type: limitation
  source_pages: p335, p336
  source_chapter: MS SQL Express installation / Database creation
  source_quote: |
    p334: "For testing purposes, 'Enforce password policy' may be unchecked if desired"
    p335: "For testing purpose, 'vaa' login will be the owner of the database (full access rights) - On production system, you will need to request specific rights accesses (select, insert, update …) for user depending on the usage of your application (most of the time only SELECT)"
  summary: |
    实验库让 vaa 当 owner（全权限）且可取消密码策略——这是测试口径。生产必须按用途授最小权限
    （多数场景只 SELECT），把实验库的全权账号直接搬上生产是安全事件预备队。
  conditions: 数据库账号规划
  tags: [limitation, mssql, security]

- id: n29
  title: addslave 会用 master 库快照清空 slave 现有配置
  type: warning
  source_pages: p252
  source_chapter: Install the high availability for VAA
  source_quote: |
    "Warning ANY CONFIGURATION THAT HAD BEEN DONE ON THE SLAVE WILL BE ERASED, AS THE DATABASE WILL BE REPLACED BY A COPY OF THE MASTER'S DATABASE."
  summary: |
    vaa ha addslave 执行时，slave 上已做的任何配置（公司、树、提示音）都会被 master 的库快照覆盖。
    误把 slave 当独立系统先配了一堆东西的，addslave 一跑全部蒸发——正确顺序是 slave 保持最小安装、
    一切配置在 master 做完后复制过去。
  conditions: HA 部署
  tags: [warning, ha, destructive]

- id: n30
  title: FQDN 进许可文件；改主机名/换网卡会让许可失效
  type: limitation
  source_pages: p249, p274
  source_chapter: Install HA / CHECK LICENSES
  source_quote: |
    p249: "The FQDN will be used in the license file • In case of problem, check the license file in the directory •/var/lib/ale/aa-license-server/"
    p274: "The license file (.lic or .vaa) is linked to the MAC address of the VAA … You must find: • The FQDN • MAC address"
  summary: |
    许可文件与 MAC 地址绑定且要含正确 FQDN——装完改主机名、换虚拟网卡（MAC 变化）都会让许可失效。
    HA slave 的 FQDN（vaa2.company.com）在装系统时就要定对；许可排障先看 /var/lib/ale/aa-license-server/
    里的文件能否找到 FQDN 与 MAC。
  conditions: 许可核查与主机改名场景
  tags: [limitation, licensing, fqdn]

- id: n31
  title: HA 切换测试的三个纪律——首呼延迟、测完 vaa start、先通 SIP
  type: limitation
  source_pages: p271
  source_chapter: OXE Additional configuration / Test the High Availability
  source_quote: |
    "It is imperative to manage SIP on the OXE before proceeding to the tests - Simulate master server failure - Run the command sudo vaa stop or shut down the machine. Call a VAA routing number (ex: 3140X) ­ A short delay may occur on the first call, as OXE will need to determine that the SIP trunk on the master server has been interrupted. - After the test, remember to restart the VAA on the master server by running sudo vaa start."
  summary: |
    三个纪律：①测 HA 前必须先把 OXE 侧 SIP 管好（否则切换测试结果无意义）；②切换后第一通呼叫有短延迟
    （OXE 要先判定 master 中继断），这是预期行为不是故障；③测完必须 sudo vaa start 恢复 master——
    忘了恢复会让系统一直跑在 slave 只读态（不能改配置、没统计）。
  conditions: HA 验收测试
  tags: [limitation, ha, testing]

- id: n32
  title: 自动备份一旦启用就关不掉，且系统不监控备份占用的磁盘
  type: limitation
  source_pages: p292, p294
  source_chapter: DATABASE AUTOMATIC BACKUP
  source_quote: |
    p294: "Once enabled, automatic database backup can't be disabled even if the option Backup activation is unchecked"
    p292: "There is no monitoring of the size used by the scheduled database backup • The administrator should monitor the available free disk space • For a 6 months database backup, 20 GB free disk space is recommended"
  summary: |
    两条运维冷知识：①自动备份启用后无法关闭——连取消勾选 Backup activation 都没用，规划时要按"永久保留"
    设计；②系统不监控备份体积——磁盘被备份文件悄悄吃满是真实事故，按 6 个月 20GB 起预估并纳入监控。
  conditions: 备份策略设计
  tags: [limitation, backup, capacity]

- id: n33
  title: 密码过期默认开启——先改密再做备份，否则恢复后登不进
  type: warning
  source_pages: p295, p276
  source_chapter: WARNING (Password duration and system backup)
  source_quote: |
    "Since version A 4.6.104, password expiration is enabled by default. It is therefore strongly recommended to change the password of the administrator account before backing up the database, if the administrator password is older than the password validity period defined in the VAA server. •In this case, if you haven't changed the password before making the backup, you won't be able to access the web administrator. - On the login page, click on 'Password or login lost' and follow the procedure. - Or ask a VAA server administrator to reset your password with the command : vaa db resetAccount [account]"
  summary: |
    陷阱链：密码有效期默认 92 天（4.6.104 起）→ 备份里封存的密码可能已过期 → 恢复备份后拿旧密码登不进 Web。
    正确顺序：先改密、后备份。已中招走两条路：登录页 "Password or login lost" 流程，或另一管理员执行
    vaa db resetAccount [account]。
  conditions: 备份/恢复与密码生命周期交叉场景
  tags: [warning, backup, password]

- id: n34
  title: SNMP 默认不启用——监控平台收不到 trap 别急着查网络
  type: limitation
  source_pages: p282
  source_chapter: EMAIL ALERTS & SNMP TRAPS
  source_quote: |
    "The SNMP service is not enabled by default"
  summary: |
    邮件告警随 SMTP 配置即可用，但 SNMP trap 服务默认关闭——NMS 平台"收不到 VAA 告警"先确认 SNMP 是否启用，
    再查路由/团体字。告警覆盖面：中继断/恢复、端口到许可上限、许可问题三类。
  conditions: 监控集成
  tags: [limitation, snmp, monitoring]

- id: n35
  title: 显示名仅监督转接且仅振铃期有效，摘机即恢复主叫信息
  type: limitation
  source_pages: p204, p225, p228
  source_chapter: CUSTOM DISPLAY NAME NODE / How-To Display name
  source_quote: |
    p204: "This will work only with supervised transfer"（Custom display name 节点说明）
    p225: "This feature is only available for supervised transfers"
    p228: "When you go off hook, this information disappears and that the caller information is displayed"
  summary: |
    三个边界：盲转不显示；只在振铃期显示（摘机后立刻恢复主叫号码/姓名）；实验还需 OXE 侧配话机特性 COS。
    向客户演示前先确认转接类型与 COS——"屏显怎么忽有忽无"是典型的边界误解。
  conditions: Display name / Custom display name 节点
  tags: [limitation, display-name]

- id: n36
  title: 收号节点的隐藏行为——* 是合法输入、# 结束不可改、min=max 判失败
  type: limitation
  source_pages: p222-223, p205
  source_chapter: IVR node – Collect digits / COLLECT DIGIT NODE
  source_quote: |
    p223: "Enter * - * is considered as a correct entry - Enter 1234# - # is the default character to finish the input - Impossible to modify … the minimum number of digits = maximum of digits, so this is an entry failure"
  summary: |
    三个行为细节：单独按 * 被视为一次"正确输入"（不是错误）——依赖 * 做返回键的树要自己写 Condition 判断；
    # 默认是结束符且不可修改；最小位数=最大位数时位数不足直接判失败。设计自助查询类脚本时把这三条当输入
    契约写进测试用例。
  conditions: Collect digit 节点
  tags: [limitation, collect-digit]

- id: n37
  title: Go to tree 只能跳同租户的树
  type: limitation
  source_pages: p160
  source_chapter: GO TO TREE NODE
  source_quote: |
    "Note that only trees belonging to the same tenant as the original tree can be selected here"
  summary: |
    跳子树节点只能选同一租户内的树——跨公司复用"公共菜单"的需求在租户隔离下不成立。多租户共享话术流程
    要在每个租户各建一份（或用 Global 变量收敛差异参数）。
  conditions: 多租户树设计
  tags: [limitation, tree, tenant]

- id: n38
  title: 树内远程录音要租户用户 ID+PIN——匿名录音不存在
  type: limitation
  source_pages: p161, p28
  source_chapter: RECORD PROMPT NODE / Prompt Recording
  source_quote: |
    p161: "When reaching this node, the caller will be asked to enter the credentials to record the selected prompt, so the caller needs to have the ID and PIN number of a user from the tenant that owns the prompt."
    p28: "Prompt Recording: Integrated message recording application • User ID and secret code"
  summary: |
    Record prompt 节点（季节性提示音远程录制）要求录制者输入该租户某个用户的 ID 与 PIN——没有匿名录制通道。
    给客户开通"电话改欢迎语"能力时，要同步开一个专用账号并管理其 PIN 生命周期。
  conditions: Record prompt 节点使用
  tags: [limitation, prompts, security]

- id: n39
  title: 教材自曝笔误两处——URL 多写一位、GRUB 密码大小写不一致
  type: version-trap
  source_pages: p92, p93, p126, p248, p249
  source_chapter: Install the VAA application / Certificate installation / Install HA
  source_quote: |
    p126: "Enter the URL to connect to VAA web interface. https://192.168.1.1.55"（多写一位 ".1"）
    p92: "Grub access (Bios access) must also be secured with a password: Generalconfig1!"（小写 c）
    p93/p249: "Set the following password to secure access to GRUB. … GeneralConfig1!"（大写 C）
  summary: |
    两处书内不一致：①证书章验证步骤的 URL 写成 https://192.168.1.1.55（正确为 https://192.168.1.55）；
    ②GRUB 实验口令两处大小写不同（Generalconfig1! vs GeneralConfig1!）。照抄书面的 URL 打不开、
    照抄口令可能登不进——以环境实际值为准并按最小 14 位规则自定。
  conditions: 实验口径；照抄书面前先核对
  tags: [version-trap, documentation]

- id: n40
  title: 升级不能拿旧 vaa.conf 直接覆盖新版文件
  type: warning
  source_pages: p308
  source_chapter: UPDATE A VAA VERSION
  source_quote: |
    "Newer version of the VAA may add new required parameters in the file, so just replacing it by the backup is not advised. Please check that the values are still the same and perform modifications if needed. If you had to modify the file, then run vaa restart to apply the changes."
  summary: |
    新版可能引入新必需参数——把备份的 /etc/ale/vaa.conf 原样盖回去会让新版缺参数跑不对。正确动作：升级后
    逐值比对旧值、按需补改、改过就 vaa restart。安装期录入的参数（incoming username、编解码、SMTP）都在这个文件里。
  conditions: 版本升级（4.8.006 及后续）
  tags: [warning, upgrade, configuration]

- id: n41
  title: SIP 模拟器外呼 DID 测试失败要先禁用 Direct RTP（实验口径）
  type: limitation
  source_pages: p118
  source_chapter: SIP configuration in OXE / Calling the tree
  source_quote: |
    "Tips - About DID calls through the SIP simulator: If there is a problem calling the tree via an external call through the SIP simulator, disable 'Allow Direct RTP'. - If you use internal calls to perform your tests, it works perfectly."
  summary: |
    实验环境特有坑：经 SIP 模拟器的外线 DID 呼叫测试树失败时，先禁用中继的 "Allow Direct RTP"；
    内部呼叫不受影响。这是模拟器与虚拟网络叠加的口径——生产环境的 RTP/媒体路径问题按网络要求文档排查，
    不能照搬这条。
  conditions: RLAB 实验环境
  tags: [limitation, lab, rtp]

- id: n42
  title: OXE 侧已有 SIP 参数不要改——教材值只适用白纸环境
  type: warning
  source_pages: p109
  source_chapter: SIP configuration in OXE / SIP Gateway
  source_quote: |
    "Adding the SIP Subnetwork and the SIP Trunk Group numbers in the local SIP gateway allows to initialize the SIP services (SIPMOTOR). On customer premises, if some parameters are already set up, don't change them."
  summary: |
    教材为了实验可跑，教你在本地 SIP 网关新建子网/中继关联——但生产 OXE 上这些参数往往已按现场编号计划配置，
    原书明确"客户现场已有参数不要改"。照抄实验值覆盖生产参数会破坏既有路由。
  conditions: 存量 OXE 现场交付
  tags: [warning, oxe, sip]

- id: n43
  title: 转移禁拨前缀（barring）实验留空——生产不配等于开放外转
  type: warning
  source_pages: p102
  source_chapter: install.sh / Forbidden prefixes
  source_quote: |
    "It is possible to define a list of prefixes (numbers) in order to block or prohibit external dialing to these numbers through the automatic operator. - Not used in the lab. - For transfer on the VAA, please enter the list of prefixes that the VAA should not be able to transfer to. For instance, this is necessary to forbid caller dialing external numbers through the VAA and/or getting transferred to services they should not be able to reach through direct dial. (Any transfer destination starting with one of these prefixes will be seen as a wrong number by the VAA.) - If you are unsure about this setting, just enter the prefix(es) that is(are) being used on this pbx to dial external numbers."
  summary: |
    install.sh 的禁拨前缀在实验中留空，但生产意义明确：不配置时，外部 callers 可以借 VAA 的转接能力外呼公网
    或触达不该触达的服务（变相盗打/越权）。至少把该 PBX 的外拨前缀填进去——这是 VAA 侧唯一的转移封闭手段。
  conditions: install.sh 参数规划（生产必配项）
  tags: [warning, barring, security]

- id: n44
  title: 邮件周报日期偏移一天——选周一收到的是周一（前一天）的报
  type: limitation
  source_pages: p317
  source_chapter: TENANT REPORT RECEPTION BY EMAIL
  source_quote: |
    "if the administrator selects 'Monday', he will receive the Tuesday at the time defined, the report of the previous day, i.e. Monday."
  summary: |
    租户活动邮件报告的"星期"参数语义是"次日报前一天"：选 Monday = 周二收到周一的报告。跟客户对验收口径时
    别把"选周一"理解成"周一收当周报"；要周一上班就看上周五数据，得另配。
  conditions: 统计报告配置
  tags: [limitation, reports]

- id: n45
  title: 主 VAA 宕机期间 Slave 无统计 + Web 要手动重连——排障别当成丢数据故障
  type: misconception
  source_pages: p44, p47
  source_chapter: High availability / Master VAA loss use case
  source_quote: |
    p44: "no statistics will be recorded for a call handled during the failure period on the PCS side"
    p47: "Web client must reconnect (to Slave VAA)"
  summary: |
    故障切换期间的话务统计缺口与"Web 打不开要重连"是 HA 设计行为：Slave 只读不记统计、Web 客户端连的是旧
    Master 地址。把这两条报成"双机坏了一台/报表少数据"的工单，按 HA 行为口径答复并推动 resync 即可。
  conditions: HA 故障切换后复盘
  tags: [misconception, ha, statistics]

- id: n46
  title: 实验代码残留旧版本号——SIP 抓包里的 User-Agent 是 4.2.x/4.3.x
  type: version-trap
  source_pages: p157, p228
  source_chapter: TRANSFER NODE / Display name SIP trace
  source_quote: |
    p157: "User-Agent: Visual Automated Attendant 4.2.15"
    p228: "User-Agent: Visual Automated Attendant 4.3.005"
  summary: |
    书中两段 SIP 抓包样例的 User-Agent 显示 4.2.15 与 4.3.005——是旧版环境的历史抓包，与本次教材版本 R4.8.006
    不一致。比对现场抓包时别拿书内报文头逐字段对齐版本行为，以现场版本实测为准。
  conditions: 抓包比对
  tags: [version-trap, documentation]

- id: n47
  title: OXE 编解码匹配口径——N2 起默认 G729，无需动手但要核对
  type: limitation
  source_pages: p113, p114
  source_chapter: SIP configuration in OXE / Compression algorithm
  source_quote: |
    p113: "Compression algorithm G729 is needed on the OXE side to match the configuration made during the installation on the VAA side. From OXE N2, compression algorithm G729 is enabled by default. It has replaced the G723 one which is phase-out. So there is nothing to do on OXE side regarding compression algorithm."
    p114: "If there is a call establishment problem, check your OXE settings or disable compression to resolve the issue quickly."
  summary: |
    OXE N2 起 G729 默认启用（替代淘汰的 G723），通常"无需在 OXE 侧动编解码"——但前提是 VAA 侧安装时勾的
    编解码与之匹配（老 OXE 或改过配置的现场要核对）。呼叫建立异常的快速止血：检查 OXE 设置或禁用压缩。
  conditions: OXE-VAA 对接排障
  tags: [limitation, codec, oxe]

- id: n48
  title: 内部呼叫显示 "0B" 前缀——要配外部回叫翻译规则修正
  type: limitation
  source_pages: p113
  source_chapter: SIP configuration in OXE / Manage the display of internal numbers
  source_quote: |
    "Manage the external callback translator to have the right display on internal call (Avoid the display of '0B' in front of the number on internal call to the VAA) - Basic number B (to remove the letter 'B') - N° Digits to be removed 1"
  summary: |
    未配外部回叫翻译规则时，内部呼叫到 VAA 的号码会带 "0B" 前缀显示。修正动作：Ext. callback Translation rules
    建 Basic number=B、删除位数 1。这是"显示怪异"类工单的标准答案，缺省配置就带这个毛病。
  conditions: OXE 侧显示类配置
  tags: [limitation, oxe, display]

- id: n49
  title: 实验明文密码与公开 token 遍布全书——生产严禁照搬
  type: warning
  source_pages: p9, p66, p92-94, p123, p232, p322
  source_chapter: SETTINGS / Pod Configuration / Install / Certificate / HTTP request / external database
  source_quote: |
    p9: "admin Superuser1234* … root letacla1 … administrator superuser"（实验虚机口令表）
    p123: "VAA1.pfx must be installed on the VAA server, the associated password is: alcatel"
    p232: "The following tokens will be used for the exercises: ­ ccc6a9e2900887a12bbaec89f17e506d ­ 689cd17f15fbb639e8ab7e7fa8f38921"（公开教材里的 token）
    p322: "Login: vaa ­ Password: vaa"
  summary: |
    实验口径的口令体系（let acla1 / Superuser1234* / InternationalSuperuser1234* / alcatel / 0000 / vaa-vaa /
    公开 token）随培训教材公开发行，等同公开凭据。任何生产环境沿用这些值都是即时漏洞；SIP TLS、证书、
    barring 等安全项在实验中全部关闭，交付前必须逐项启用。
  conditions: 生产交付安全基线
  tags: [warning, security, lab]

- id: n50
  title: 生产化依据在书外——安装手册/管理指南/TBE083/OTEC-S 四份文档
  type: out-of-scope
  source_pages: p50, p29, p61, p78, p141, p277-278, p281
  source_chapter: MULTI-COMPANY / ROUTING NUMBERS / public certificate / S.O.T / TTS / MAINTENANCE 各引用页
  source_quote: |
    p50: "For details, refer to the document TBE083 - Multi Companies features OXE … For detail about configuration, please refer to: OTEC-S: Visual Automated Attendant configuration Guide"
    p29: "See chapter 4.3 Disambiguation about routing expressions in the Administration guide"
    p61: "To set up a public certificate, please refer to the installation manual - chapter 6.4 HTTPS configuration for web app"
    p277: "Refer to the section 6 - VAA system management in the installation guide"
    p141: "For more details refer to the administration guide document, section 10 Text to Speech"
    p78: "Refer to the Installation guide – Section 4.2 for complete procedure"
  summary: |
    教材多处把细节外置：multi-company → TBE083 与 OTEC-S 配置指南；路由表达式歧义 → Administration Guide 4.3；
    公网证书与完整安装 → Installation Manual 4.2/6.4；系统管理与命令全集 → Installation Manual 第 6 章；
    TTS 细节与价格 → Administration Guide 第 10 章。VAA 文档统一在 MyPortal。生产交付以这些文档最新版为准。
  conditions: 生产配置与排障
  tags: [out-of-scope, documentation, myportal]
```

## 收尾自检 — 对照 BOOK_OVERVIEW.md 22 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | Pod/OXE 基础准备 | 有 → n41（Direct RTP 实验坑）、n16（不启动 slave）、n42（现场参数不改） |
| task-02 | 安装 VAA 应用 | 有 → n01（4.8.006 规则）、n10（root SSH）、n12（默认口令）、n49（明文密码）、n43（barring） |
| task-03 | OXE 侧 SIP 对接与验证 | 有 → n42（SIPMOTOR）、n47（编解码匹配）、n48（0B 显示）、n41 |
| task-04 | 安装 Web 证书 | 有 → n11（HTTPS 切换擦除/S.O.T 自签）、n39（URL 笔误） |
| task-05 | WebAdmin 初始管理 | 有 → n13（新账号默认密码）、n14（SMTP 重启）、n15（Supervision 按钮） |
| task-06 | 公司与业务时间/日历 | 有 → n18（破坏性同步） |
| task-07 | 提示音与 TTS/ASR | 有 → n19（WAV 规范）、n20（Pico/Google 边界）、n38（录音凭证） |
| task-08/09/10 | 三级树设计 | 有 → n21（命名）、n22（双语同文件）、n37（同租户跳树） |
| task-11 | 变量与条件 | 有 → n21（变量纪律归入树设计） |
| task-12 | 收号节点 | 有 → n36（*/#/min=max） |
| task-13 | 显示名节点 | 有 → n35（监督转/振铃期/COS） |
| task-14 | HTTP 节点 | 有 → n49（公开 token） |
| task-15 | 邮件节点 | 有 → n14（SMTP 重启） |
| task-16 | VAA HA 部署 | 有 → n29（addslave 清库）、n30（FQDN/许可）、n04（只读/不同步） |
| task-17 | OXE 侧 HA 配置 | 有 → n05（丢话）、n31（切换测试纪律） |
| task-18 | 日常维护 | 有 → n32（备份关不掉/无监控）、n33（密码-备份陷阱）、n34（SNMP 默认关）、n15 |
| task-19 | PCS/OPEX | 有 → n09（PCS 配置丢失）、n08（OPEX 无空间冗余）、n07（端口不预留） |
| task-20 | 升级 | 有 → n01、n40（vaa.conf 不覆盖）、n11 |
| task-21 | 统计报告 | 有 → n44（日期偏移）、n45（统计缺口）、n21 |
| task-22 | 外部数据库集成 | 有 → n23（SQL 四坑）、n24（安全口径）、n25（JDBC 路径/HA）、n26（Oracle）、n27（MSSQL 三坑）、n28（权限最小化） |

**22/22 全部有边界类条目覆盖，无空缺。**

### 扫描完整性说明（Warning/Note/Tips 标记框逐页核对）

- 已全部入册的 Warning 框：p57（HTTPS 擦除/S.O.T 自签，n11）、p64（不启动 slave，n16）、p101（G729/ASR，n02）、p128（新账号默认密码，n13）、p130（SMTP 重启，n14）、p131（Supervision 按钮，n15）、p252（addslave 清库，n29）、p255（slave 只读告警，n04）、p295（密码-备份陷阱，n33）、p308（4.8.006/vaa.conf，n01/n40）。
- 已入册的 Note/Tips/Tricks 框：p29（通配符不推荐，n17）、p32/33（破坏性导入，n18）、p52/53（示例免责，n03）、p55（root SSH，n10）、p57 Note（S.O.T 证书）、p100（IP 确认答 y，操作提示非边界，未单列）、p101 Note（邮件可后配；incoming username 一致性，操作口径已入 principle p08/p10）、p102 Note（SIP TLS 需证书；barring 实验留空，n43）、p110 Tips（S.O.T 用户名 vaa / vaa conf telephony，已入 principle p10）、p114 Tips（压缩排障，n47）、p118 Tips（Direct RTP，n41）、p120 Tricks（motortrace 级别，操作提示已入 framework f20）、p125 Notes（certmgr.msc；证书/配置可备份，操作口径已入 c04 与 principle p25）、p138（无空格/同声音，n19/p13）、p141 Notes（Pico/Google/价格过时，n20）、p160（同租户，n37）、p161（录音凭证，n38）、p187/194（双语同文件，n22）、p207（SQL 慢查询/安全，n23/n24）、p249 Note（FQDN 许可，n30）、p320 Note（HA 驱动，n25）、p323 提示框（空结果/单字段/首条，n23）、p332 Note（首登 Windows 认证，n27）、p334 Note（密码策略可放宽，n28）。
- 复核后排除的纯操作提示框（非边界类，不构成候选）：p70-73 netadmin 菜单操作提示、p92-94 改密步骤演示说明、p96 首连信任主机提示、p165/175/187"逐节点连线"（已入 principle p15）、p188 双语提示的操作实现部分、p218-220 变量实验的进阶题、p223/235/253 "To go further" 进阶题、p274 许可 more 命令演示、p303 cron 细节（已入 principle p33）、p317 报告开关默认值（已入 principle p31）。
- 推断性结论已在对应条目 summary 内显式标注：本文件无未标注的推断；n45 中"统计缺口报障的答复口径"为运维实践引申，其行为依据（只读/无统计）均为原文直引。
- 版本号均按原文保留完整位数：4.6.104、4.8.006、4.2.15、4.3.005、Release 11、VAA 4.x、R4.8.006（书名页）；N2（OXE 版本代际表述）。
