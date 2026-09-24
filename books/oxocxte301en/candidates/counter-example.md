# 反例/限制/边界/易错点候选 — OXO Connect Advanced (OXOCXTE301EN Ed18)

> 提取器: counter-example-extractor（全量扫描，逐页扫 Warning/Note/Tips/Attention/注意事项一个不漏） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: warning=危险操作 / limitation=能力边界 / version-trap=版本陷阱 / misconception=易误解 / out-of-scope=书外依赖 / errata=原书勘误与不一致
> 推断性结论均标注"（推断）"。

```yaml
- id: n01
  title: IPDSP 安装前必须先改 IP 并完成 NTP 时间同步，否则 lanpbx 加载报错
  type: warning
  source_pages: p14
  source_chapter: INSTALLING THE IPDSP
  source_quote: |
    "Change the IP settings for the OXO Connect and the PC before installing the IPDSP • This ensures that the PC synchronizes with the NTP server and adjusts the time and date. • Otherwise, if there is a time difference between the PC and the OXO system, the IPDSP will not be able to start. • An error message related to loading the lanpbx file will appear. • This is due to the use of digital certificates (the IPDSP uses the HTTPS protocol)."
  summary: |
    时序陷阱：IPDSP 走 HTTPS 数字证书，PC 与 OXO 时间不一致会直接证书校验失败，表象是"lanpbx 文件加载错误"——不看这段会把时间问题误判成文件损坏。操作顺序固定：改 OXO IP→改 PC IP→PC 里把自动对时关了再开（强制重同步）→再装 IPDSP。
  conditions: 任何 IPDSP 安装场景（实验与生产同源）
  tags: [warning, ipdsp, ntp, certificate]

- id: n02
  title: 每个客户的密码必须不同（安装时强制）
  type: warning
  source_pages: p31
  source_chapter: OMC Installation / Define the passwords
  source_quote: |
    "The passwords must be different for each customer!"
  summary: |
    首装设密时各账户密码不得在客户间复用；后续可在 OMC/Security 菜单再改。这是书内少见的全大写强调。
  conditions: 首次安装设密
  tags: [warning, password]

- id: n03
  title: 客户信息带 * 字段必填且首次连接强制
  type: limitation
  source_pages: p32
  source_chapter: OMC Installation / Enter the customer information
  source_quote: |
    "Information marked with an * are mandatory. … Enter the customer information, mandatory at the first connection to the OXO"
  summary: |
    首连不填客户信息无法完成初始化；供应商信息（实施技师联系方式）可选。
  conditions: OMC 首次连接
  tags: [limitation, omc]

- id: n04
  title: 公网编号计划配置必要时要复制到 Restricted Public Numbering Plan
  type: warning
  source_pages: p42, p221
  source_chapter: Public SIP Gateway / Private SIP network with ARS
  source_quote: |
    "Notes … Copy the config to the Restricted Public Numbering Plan if necessary" (p42)
    "Copy the config to the Restricted Public Numbering Plan if necessary" (p221)
  summary: |
    只配 Normal 公网编号计划、漏配 Restricted（受限/夜间模式）时，系统处于受限时间范围时 DDI/话务台映射会落空。两处实验都重复了这条 Note，属高频漏项。
  conditions: 配置公网编号计划时
  tags: [warning, numbering, restricted]

- id: n05
  title: VoIP 外线的 Gateway index 要等网关建好后回填
  type: warning
  source_pages: p44
  source_chapter: Public SIP Gateway / Program VoIP Trunks as public
  source_quote: |
    "The Gateway index must be filled in later when the SIP Gateway is created"
  summary: |
    顺序陷阱：先建 VoIP 接入时网关还不存在，索引字段留空属正常；建完网关必须回来补填，否则接入与网关脱钩。
  conditions: 公网/私网网关配置流程
  tags: [warning, sip-gateway, ordering]

- id: n06
  title: Domain Proxy tab 必须在 DNS tab 之后配置
  type: warning
  source_pages: p46-47
  source_chapter: Public SIP Gateway / Gateway Parameters Details
  source_quote: |
    "Don't forget to now configure the Outbound Proxy: gateway1.itsp1.com in the Domain Proxy tab" (p46)
    "The following setting can only be configured after filling in the DNS tab!" (p47)
  summary: |
    双重提醒：DNS tab 填完后 IP 类型才变 dynamic、Domain Proxy 才可配；跳序会找不到参数位。Outbound Proxy 也容易漏——书内用 "Don't forget" 强调。
  conditions: SIP 网关九 tab 配置
  tags: [warning, sip-gateway, ordering]

- id: n07
  title: 默认 Security tab 明文——到该运营商的 SIP 流不加密
  type: limitation
  source_pages: p51
  source_chapter: Public SIP Gateway / Security Tab
  source_quote: |
    "SIP flows will not be encrypted to this operator, default value on the OXO Connect Evolution"
  summary: |
    实验网关的默认状态是明文 SIP（无 TLS/SRTP）；生产上要加密需按 TLS/SRTP 章（p365-378）另配，不能默认当作已加密。
  conditions: 公网 SIP 网关默认配置
  tags: [limitation, security, sip]

- id: n08
  title: 酒店模式进入需先冷复位——默认是 Business 模式
  type: warning
  source_pages: p70
  source_chapter: Configuration of the Hotel application / Wizard hotel
  source_quote: |
    "Switch the OXO Connect in hotel mode thanks to the initial installation Wizard Hotel • Make a cold reset (by default the OXO is in Business mode)"
  summary: |
    直接跑 Wizard Hotel 不生效：必须先冷复位把系统从 Business 模式切出再走 Initial Installation Wizard (Hotel)。冷复位有数据清空风险，生产改造前必须完整备份。
  conditions: 酒店模式部署
  tags: [warning, hotel, cold-reset]

- id: n09
  title: Call Accounting Time based 与 AOC 脉冲互斥——不可混配
  type: warning
  source_pages: p73, p83
  source_chapter: Call Accounting Time based
  source_quote: |
    "When activated, AOC Pulse based is deactivated (no mix configuration)"
  summary: |
    激活"按时长计费"会自动停用"按 AOC 脉冲计费"，两者不能同时生效；期望保留运营商 AOC 的站点不要开此功能。附带：脉冲从第一个时间段开始即计（不按分钟切割）。
  conditions: 计费方案选型
  tags: [warning, metering, aoc]

- id: n10
  title: 内部替代也可用可编程键实现（Tips）
  type: limitation
  source_pages: p101
  source_chapter: Account codes/Internal Substitution code
  source_quote: |
    "Tips … This feature can also be realized by a programmable key … Program a Feature key: Account Code New 1000"
  summary: |
    除 66 前缀外，可给话机直接编 "Account Code New 1000" 功能键实现替代拨号；两种入口并存时按用户习惯选，勿重复配。
  conditions: 内部替代场景
  tags: [limitation, substitution]

- id: n11
  title: 8088 话机仅 v2 及以上被 OXO 支持
  type: version-trap
  source_pages: p105
  source_chapter: 8088 Smart DeskPhone
  source_quote: |
    "Note: only 8088 >= v2 is supported on OXO"
  summary: |
    库存里混有 8088 v1 时上 OXO 会踩坑；采购与翻新要核对硬件版本。
  conditions: 8088 话机选型
  tags: [version-trap, 8088]

- id: n12
  title: 8088 Private Store 默认禁止装应用，且有四类应用装不了
  type: limitation
  source_pages: p107
  source_chapter: 8088 Private Store
  source_quote: |
    "By default, the phone doesn't authorize the user to install applications … Some application can't be installed on the phone because of the following requirements: • Applications who need the GPS • Applications who need the Wi-Fi • Applications who donn't work on Android 6.0.1 version • Applications who doesn't work on landscape display"
  summary: |
    要开放应用安装需先在 OMC 激活 WebView（Private Store URL）；即便开放，需要 GPS/Wi-Fi 的、不兼容 Android 6.0.1 的、不适配横屏的 APK 都装不上。
  conditions: 8088 应用分发
  tags: [limitation, 8088, android]

- id: n13
  title: 监督功能四条边界（监督方机型/50 键/会议中不能应答/private 呼叫）
  type: limitation
  source_pages: p114
  source_chapter: Stations groups supervision
  source_quote: |
    "Supervisor feature is only available on DeskPhones … Number of supervision keys on the system, up to 50 … Answer to the notification can't be done when the supervisor are in a 3-party conference or inside an application of the menu screen or in an ACD Login application … The private (in the public numbering plan, priv = yes) calls can't be supervised"
  summary: |
    四条边界：被监督方任何用户类型都行，监督方只能是 DeskPhones；系统监督键上限 50；监督员在 3 方会议/菜单屏应用/ACD 登录应用中时通知无法应答；公网编号计划 priv=yes 的私密呼叫不可监督（设计使然）。
  conditions: 站群监督部署
  tags: [limitation, supervision]

- id: n14
  title: 监督键配完必须在话机上激活（两处 Note）
  type: warning
  source_pages: p117-118
  source_chapter: Stations groups supervision (How to)
  source_quote: |
    "Validate and test, do not forget to activate the key on the supervisor set." (p117)
    "Notes … Validate and test, do not forget to activate this new key on the supervisor set" (p118)
  summary: |
    OMC 编好 Supervision Groupware 与 Audio Signal Supervision 两键后，还要在监督话机上把键激活才生效——书内两节各提醒一次，漏激活的典型症状是"配了但没通知"。
  conditions: 站群监督实验
  tags: [warning, supervision, activation]

- id: n15
  title: PIMphony 在线更新默认停用且需互联网；注册亦需互联网
  type: limitation
  source_pages: p127, p134
  source_chapter: PIMphony installation
  source_quote: |
    "By default, the service is deactivated. Internet connection is required to update PIMphony." (p127)
    "The PIMphony registration is done on site. An internet connection is required to do this. In our case, choose 'Cancel'." (p134)
  summary: |
    两层互联网依赖：更新服务默认关（要开需勾 Activated）；首次注册要联网（内网隔离站点只能选 Cancel，可能影响后续更新路径）。封闭内网客户部署前先确认更新策略。
  conditions: PIMphony 部署
  tags: [limitation, pimphony, network]

- id: n16
  title: SIP 话机不支持游牧模式
  type: limitation
  source_pages: p147
  source_chapter: SIP Phones and nomadic mode
  source_quote: |
    "SIP Phones do not support nomadic mode"
  summary: |
    移动性方案（游牧/远程替代）不覆盖第三方 SIP 话机；这类用户的移动需求要另走（推断：Rainbow/软话机路线）。
  conditions: 移动性方案选型
  tags: [limitation, sip, nomadic]

- id: n17
  title: SIP 会话计时器（RFC 4028）：无刷新会释放呼叫
  type: warning
  source_pages: p154
  source_chapter: SIP phone maintenance
  source_quote: |
    "Support of RFC 4028: session timer management • Without periodic refresh of the SIP session, the call is released … Timer value is configurable with a noteworthy address 'sipphone_sess_tim'"
  summary: |
    启用 session timer 后，SIP 会话若不按期刷新会被系统释放（防僵死呼叫）；通话莫名掉线时先查此定时器与运营商 refresh 兼容性。
  conditions: SIP 话机维护
  tags: [warning, sip, session-timer]

- id: n18
  title: Zoiper 实验禁改既有 MicroSIP；域必须补 5059 端口且记得保存
  type: warning
  source_pages: p156, p164
  source_chapter: SIP Soft phone (How to)
  source_quote: |
    "Add a new user in 'Open SIP' … Don't modify any existing MicroSIP softphone" (p156)
    "Add port 5059 to the Domain … 192.168.1.246:5059 … When leaving the menu do not forget to save by 'Yes'" (p164)
  summary: |
    三条易错：①实验室预置的 4 个 MicroSIP（100-103）不许动，只能新建 Open SIP 用户；②Zoiper 的 Domain 默认不带端口，必须手工补 :5059，否则注册不上；③离开设置菜单要点 Yes 保存，否则白配。
  conditions: Zoiper 实验
  tags: [warning, zoiper, lab]

- id: n19
  title: SIP 话机远程 SSH 要手动解锁、用完手动锁回（NOE 话机自动）
  type: warning
  source_pages: p170
  source_chapter: IP devices remote trace via Webdiag
  source_quote: |
    "SSH is automatically unlocked for NOE IP devices prior to execute each remote command (a new password is generated at each unlock) … Unlock must be manually processed for SIP phones prior to execute a remote SSH command • SIP phones must be manually locked at the end of the operations"
  summary: |
    安全差异：NOE IP 话机（ALE-20/300/400/500 等）每次远程命令前自动解锁并生成新密码；SIP 话机（ALE-2/ALE-3）要手动解锁且操作完必须手动锁回——忘锁回会留下 SSH 暴露面。
  conditions: Webdiag SIP SSH Control
  tags: [warning, ssh, security, sip]

- id: n20
  title: Hot Desking 实验结束要停用；抢占登录自动注销前一用户
  type: warning
  source_pages: p175, p179
  source_chapter: Hot Desking
  source_quote: |
    "If a HDU logs in to a HDP on which another HDU is already connected, the previous HDU will be first automatically logged out" (p175)
    "Define a free Premium or ALE Deskphone as 'Hot Desking' … Deactivate the feature at the end of the lab" (p179)
  summary: |
    两条：①抢占式登录——新 HDU 登录已占 HDP 时前一 HDU 被自动注销（通话中的现场要小心）；②实验话机用完要把 "Hot Desking set" 属性关掉，防止后续实验被 HDU 行为干扰。
  conditions: Hot Desking 配置与实验
  tags: [warning, hot-desking]

- id: n21
  title: Multiset 实验页残留法文步骤（Sélectionner le poste 100）
  type: errata
  source_pages: p191
  source_chapter: Multiset configuration (How to)
  source_quote: |
    "Sélectionner le poste 100 en poste Primaire"
  summary: |
    OMC 截图说明文字混入法文（"选择 100 为主站"），而实验正文写的是选 101 为主、102 为副——照抄截图文字会配错号码；以英文正文为准。
  conditions: Multiset 实验
  tags: [errata, multiset]

- id: n22
  title: 私网组网实验禁止与其它 lab 产生 IP 冲突（Attention）
  type: warning
  source_pages: p208
  source_chapter: Private SIP network with ARS / Topology
  source_quote: |
    "Attention … Do not make an IP conflict with another OXO lab"
  summary: |
    多 POD 并行做私网实验时，各 POD 按自己的 N（POD 号）取 192.168.N.246；抄别人的 IP 会把别人 lab 的 OXO 配挂。
  conditions: 多 POD 并行实验
  tags: [warning, lab, ip-conflict]

- id: n23
  title: Internal ARS 时段两处口径不一致（12-13/13-18 vs 12-14/14-18）
  type: errata
  source_pages: p233, p449
  source_chapter: Internal ARS management
  source_quote: |
    "Extension 102 from Monday to Friday, from 12:00 PM to 1:00 PM. • Extension 103 from Monday to Friday, from 1:00 PM to 6:00 PM." (p233)
    "Create the 4 requested time slots: 8am to 12pm • 12pm to 2pm • 2pm to 6pm • 6pm to 8am" (p449)
  summary: |
    同一实验，架构页（p233）写 12-13 转 102、13-18 转 103，Hours 操作页（p449）却写 12-14、14-18 四时段。功能机制不受影响，但照单复现会与架构页对不上；交付文档需统一口径。
  conditions: Internal ARS 实验
  tags: [errata, internal-ars]

- id: n24
  title: MSG1-20 欢迎消息与实体 MoH 不得混淆（两处 Be careful）
  type: warning
  source_pages: p241, p256
  source_chapter: Internal ARS & Multi entity (How to)
  source_quote: |
    "Be careful not to be confused with Music on hold for the entities" (p241)
    "Be careful not to be confused with Message 1 to 20 welcome messages (MSG1 to MSG20)" (p256)
  summary: |
    两类语音资产共用 MMC 录音入口：MSG1-20 是欢迎消息（挂寻线组/AA），MUSIC 1-4 是实体保持音乐——录错位置的症状是"来电播错语音/保持听错音乐"。两章各提醒一次。
  conditions: 语音录制场景
  tags: [warning, moh, message]

- id: n25
  title: 实体间呼叫禁止的连带影响清单；话务员组不受限
  type: limitation
  source_pages: p247
  source_chapter: Call restriction management
  source_quote: |
    "Direct call allow or not between user belonging different entities • Other features impacted • Immediate and On busy forwarding • RSL key • Individual pickup • Text and voice messaging • Sets belonging to attendant group don't follow this restriction"
  summary: |
    打开 "Do not allow internal calls between multi-tenant entities" 不止禁直呼：立即转移/忙转、RSL 键、个人代接、文本与语音邮箱都被连带限制；话务员组话机豁免——设计跨公司协作流程时按这份清单核对。
  conditions: 多实体呼叫限制
  tags: [limitation, entity]

- id: n26
  title: MLAA "line parameters" 不随配置存档保存（Warning）
  type: warning
  source_pages: p438
  source_chapter: Management of a tree structure / Transfer
  source_quote: |
    "Recommendations • Save the configuration first and then transfer • OMC \ Multiple Automated Attendant \ MLAA Services \ File \ Save as • Warning the 'line parameters' are not saved"
  summary: |
    Save as 存档不含线路参数（DDI/CLI→树映射）；换机迁移或回滚配置后要手工重配线路参数，否则树在但来话进不来。
  conditions: MLAA 配置备份
  tags: [warning, mlaa, backup]

- id: n27
  title: MLAA 端口与消息改动需引擎复位或等 10 分钟
  type: limitation
  source_pages: p431, p441
  source_chapter: MLAA Setup / Settings voice messages
  source_quote: |
    "The MLAA port number is taken into account after an ACD engine reset or after 10mn without reset" (p431)
    "The MLAA messages are taken into account after an MLAA/ACD engine reset or after 10mn without reset" (p441)
  summary: |
    改完端口数或消息不立即生效：要么手动复位 ACD 引擎，要么干等 10 分钟无复位自动生效。"改了没反应"先查这条再排查配置。
  conditions: MLAA 配置
  tags: [limitation, mlaa, propagation]

- id: n28
  title: 8214 话机版本兼容注记（仅 R6.0 MD1；R5.2 计划 2023 底）
  type: version-trap
  source_pages: p486
  source_chapter: 8328 SIP-DECT single cell base station
  source_quote: |
    "(*) 8214: • Only on R6.0 MD1. Compatibility on R5.2 is planned End 2023 • Predefined Messages icon (as 8212) (for IP-xBS/IBS) planned end 2023. (Available with 8328)"
  summary: |
    8214 话机在 R5.2 上不可用（R6.0 MD1 起）；"预定义消息图标"功能计划 2023 底才覆盖 IP-xBS/IBS（8328 已有）。存量 R5.2 站点配 8214/该图标前先核版本与最新 TC。
  conditions: DECT 话机选型与版本规划
  tags: [version-trap, dect, 8214]

- id: n29
  title: 话机可能锁定在时钟同步但信号较差的基站（xBS 与 TDM IBS 间总是如此）
  type: limitation
  source_pages: p507
  source_chapter: DECT IP-xBS Topologies 2/2
  source_quote: |
    "Important point: a DECT handset may remain locked to a base station although there is another base station with a better radio quality connection but not clock synchronized with the first one. • Possible when both base stations are xBS • Always the case between xBS and TDM IBS"
  summary: |
    空口同步优先于信号强度：旁边基站信号更好但不同步时，话机仍可能赖在原基站——xBS 间可能出现，xBS 与 TDM IBS 之间必然如此。混合组网的用户投诉"信号满格通话差"先查同步关系。
  conditions: 混合 IP-xBS/IBS 组网
  tags: [limitation, dect, sync]

- id: n30
  title: 复杂 DECT 拓扑必须找 TSS；Automatic 模式强烈推荐
  type: limitation
  source_pages: p517
  source_chapter: IP Dect Clock Synchronization (advanced)
  source_quote: |
    "In case of complex deployment use cases contact TSS … Automatic mode (strongly recommended) … In manual mode (to be used in expert mode only in case of very specific cases)"
  summary: |
    多站点/多集群时钟同步属 TSS（技术支持服务）领域；Manual 手动选主仅限专家在极特殊场景使用——自作主张手配同步树是常见事故源。边界数字：每站最多 8 集群、最多 20 站点、站间不切换。
  conditions: DECT 同步规划
  tags: [limitation, dect, tss]

- id: n31
  title: SUOTA 下载让路话务；swap 必须放充电座
  type: limitation
  source_pages: p526
  source_chapter: SUOTA
  source_quote: |
    "The download process has a lower priority than DECT user calls • When a phone has any telephonic activity the download process is paused … the DECT handset needs to be put on a charger cradle to proceed."
  summary: |
    空中升级两约束：下载低优先级，话机一有话务就暂停（整批 4-8 小时是常态）；下载完成后必须放回充电座才能 swap——没座的手机会一直停在"就绪"状态。可中途取下（多色 LED 显示进度）。
  conditions: DECT 批量升级
  tags: [limitation, suota, dect]

- id: n32
  title: 站点勘测专用 xBS 固件与生产版不同，不可混用
  type: version-trap
  source_pages: p530-531
  source_chapter: Site Survey Kit
  source_quote: |
    "One 8378 IP-xBS integrated antenna dedicated for the survey kit (it doesn't run the same FW as the standard 8378 IP-xBS)."
  summary: |
    SSK 里两台勘测 xBS 跑专用固件（还预置实验 PARK/DNR 体系，如室内 PARK 31100170142241，实验口径）——不能当生产基站用，生产 xBS 也别刷勘测固件。
  conditions: 站点勘测
  tags: [version-trap, dect, ssk]

- id: n33
  title: DECT 覆盖判定口径：-72 dBm 边界；测试最少两台话机
  type: limitation
  source_pages: p533-534
  source_chapter: Radio coverage rules & Audio quality test
  source_quote: |
    "measurement of the -72 dBm attenuation at the limit of the area … -80 dBm" (p533)
    "Minimum two handsets must be registered in order to establish a call for the radio coverage test. It is also possible to listen to the continuous dial tone by pressing '0' + 'dial key'" (p534)
  summary: |
    验收口径：语音质量区以 -72 dBm 划界（勘测模式显示下限 -80）；音质要"通话中"测且至少两台话机注册，只听拨号音可用 "0"+拨号键。拿信号格数或单机待机测试当验收依据都不成立。
  conditions: DECT 站点勘测验收
  tags: [limitation, dect, site-survey]

- id: n34
  title: IBS 与 IP-DECT xBS 两个 lab 在虚拟课堂均不可做
  type: limitation
  source_pages: p536, p542
  source_chapter: DECT registration on IBS / IP-DECT xBS (How to)
  source_quote: |
    "In Virtual Classroom: This lab is not possible" (p536)
    "Check OXO Connect IP settings … In Virtual Classroom: This lab is not possible" (p542)
  summary: |
    两章 DECT 实验需真实硬件，虚拟课堂只有过程截图——学员"做过题"不等于"插过基站"；首次现场部署要预留加练时间。（推断：PIMphony 实验同样不可做，p129。）
  conditions: 培训交付
  tags: [limitation, lab, dect]

- id: n35
  title: ARI/PARI 唯一性：每客户唯一、eBuy 获取、xBS 与 IBS 共用
  type: warning
  source_pages: p494-496, p543
  source_chapter: IP DECT Solution / IP-DECT xBS (How to)
  source_quote: |
    "Only one PARI … PARI is common for xBS and IBS" (p496)
    "Reminder the unique ARI number for each customer is to recover on the eBuy site" (p543)
  summary: |
    两条陷阱：①全系统仅一个 PARI，xBS 与 IBS 共用——随意编造会让话机锁错系统；②ARI 每客户唯一，正规来源是 eBuy（实验才由讲师给定），抄邻站 ARI 会造成跨站归属混乱。
  conditions: DECT 系统标识配置
  tags: [warning, dect, pari]

- id: n36
  title: 8158s/8168s 仅 NOE 模式；OXO ≤R4.x 下显示为 8118/8128
  type: version-trap
  source_pages: p550-551
  source_chapter: 8158s/8168s VoWLAN Handsets
  source_quote: |
    "8158s/8168s VoWLAN Handsets work only in NOE mode with OXO Connect System" (p550)
    "the devices are displayed as 'MIPT 8158s' and 'MIPT 8168s' (Seen as 8118 and 8128 in case of OXO ≤ R4.x)" (p551)
  summary: |
    两条版本口径：老 OXO（≤R4.x）订阅户列表里新话机显示旧型号名（8118/8128），别当买错货；这批 VoWLAN 话机不走 SIP，只配 NOE 模式。
  conditions: VoWLAN 话机部署
  tags: [version-trap, voWLAN]

- id: n37
  title: PhD-relay 用完必须擦除 traces（Important）
  type: warning
  source_pages: p557
  source_chapter: PhD-relay
  source_quote: |
    "Important: at the end of this operation, do not forget to erase traces"
  summary: |
    PhD-relay 生成的加密 trace 属调试敏感数据，收集转发 ALE 工程部后要删干净——留在系统里既是空间垃圾也是安全暴露面。
  conditions: PhD-relay 操作
  tags: [warning, phd-relay, security]

- id: n38
  title: Noteworthy 地址写错可致系统恶化；cold reset 全部回默认
  type: warning
  source_pages: p575
  source_chapter: Noteworthy addresses modification
  source_quote: |
    "Writing a value to the wrong address can result in a deterioration in the operation of the system … Noteworthy addresses return to their default values following a cold reset"
  summary: |
    双向风险：写错地址会搞坏系统运行（所以清单要以 TC1398 为准、逐项核对）；反过来冷复位会把所有 noteworthy 调优打回默认——依赖自定义参数的站点做冷复位/重装后必须重放参数。
  conditions: Noteworthy 修改与系统复位
  tags: [warning, noteworthy, reset]

- id: n39
  title: Ringing 基址随软件版本变化；铃音周期必须 <4 秒
  type: warning
  source_pages: p581
  source_chapter: Noteworthy addresses modification / Ringing cadence
  source_quote: |
    "Example: '0242D978' This value depends on the software version of the OXO! … The period of the ringing must be under 4 seconds."
  summary: |
    铃音节奏的 Numeric 地址是"基址+偏移"算出来的，基址每版本都变——照抄书上 0242D978 会写坏别人的内存。周期 >4 秒的节奏不合法。
  conditions: 铃音定制
  tags: [warning, noteworthy, version]

- id: n40
  title: 自签证书在冷复位与 LoLa 后不擦除，但改外部地址/LAN IP 会重建
  type: warning
  source_pages: p327
  source_chapter: Certificate management
  source_quote: |
    "The self-signed certificate is generated at the first install and recreated by changing the access router external address or the LAN IP address … The certificate is not erase with a cold reset and LoLa"
  summary: |
    证书生命周期两个方向：改接入路由器外部地址或 LAN IP 会重建证书（所有已信任客户端要重新信任）；而冷复位/LoLa 反而不清证书（净化转售设备时要单独处理，推断：配合 noteworthy/密码三档冷复位一起核查）。
  conditions: 证书管理与设备处置
  tags: [warning, certificate, reset]

- id: n41
  title: 4K 证书升级后回滚必须先切回 2K（OMC 会报错）
  type: version-trap
  source_pages: p357
  source_chapter: Server certificate migration
  source_quote: |
    "Roll back to previous release after a migration to R6.2 … from R6.2, certificates 4K are stored in a different format than previous release, Roll back requires specific actions before rolling back if the upgrade to 4K was performed • OMC will generate an error warning • switch again to 2K certificates (Via WebDIAG) and then roll back."
  summary: |
    R6.2 用新格式存 4K 证书密钥；升级 4K 后直接回滚旧版本会失败（OMC 报错警告）——正确顺序是 WebDIAG 先切回 2K 证书再回滚。做升级演练时要把这一步写进回滚手册。
  conditions: R6.2 升级/回滚
  tags: [version-trap, certificate, rollback]

- id: n42
  title: TLS 双向认证迁移旧版时证书需再生成
  type: version-trap
  source_pages: p373
  source_chapter: OCE SIP trunks TLS/SRTP configuration
  source_quote: |
    "Note: For Mutual authentication, when migrating from previous releases, certificates needs to be regenerated"
  summary: |
    从旧版本迁移并启用双向认证（Mutual authentication）时，旧证书不能沿用，必须再生成——只切开关不换证书表现为 TLS 握手失败。
  conditions: SIP TLS 迁移
  tags: [version-trap, tls, certificate]

- id: n43
  title: OCE-FE SIP 代理的四项配置被全部 SIP TLS 网关共享；SIPS URI 不支持；ETH1 不走 SIP
  type: limitation
  source_pages: p378
  source_chapter: OCE-FE SIP Trunk TLS SRTP PROXY feature details
  source_quote: |
    "The following configurations in OCE FE are shared by all the SIP TLS Gateways configured in OXOC • Single/Mutual Authentication • DNS • Cryptographic suites • Static NAT … - SIPS URI is not supported by OCE FE … - ETH1 interface of OCE FE is currently not used for SIP traffic"
  summary: |
    三条边界：①认证模型/DNS/密码套件/静态 NAT 在 OCE-FE 上是全局的——想给不同网关配不同套件做不到；②SIPS URI 不支持（要求 SIPS 的运营商接不了）；③OCE FE 的 ETH1 当前不用于 SIP 流量（布线按 ETH0 规划）。
  conditions: OCE-FE 代理方案
  tags: [limitation, oce-fe, tls]

- id: n44
  title: 对端仅 TLS client 时私网 TLS 互联要停用双向认证（变通）
  type: limitation
  source_pages: p369
  source_chapter: OCE SIP trunks TLS/SRTP use cases – Private SIP trunks
  source_quote: |
    "Media gateway / other PBX should have the capability to act as both TLS client and TLS server … If the Media gateway / other PBX has only TLS client capability, then a workaround needs to be deployed. In this case mutual authentication must be deactivated"
  summary: |
    两 OCE 私网 TLS 互联默认一端自动做 TLS Server、一端做 Client；对端设备只会做 client 时必须停用双向认证才能接——安全等级下降要有意识接受并记录。
  conditions: 私网 TLS 组网
  tags: [limitation, tls, mutual-auth]

- id: n45
  title: TLS 模式下 Direct RTP 不可用
  type: limitation
  source_pages: p368
  source_chapter: OCE SIP trunks TLS/SRTP use cases
  source_quote: |
    "TLS SRTP packet processing is done separately at the OCE GW side for each SIP trunk in TLS mode • Direct RTP is not possible"
  summary: |
    启用 TLS/SRTP 后媒体必须在 OCE GW 侧终结处理，端点直通（Direct RTP）不可用——容量与延迟规划要按"媒体过 OCE"重算。
  conditions: TLS/SRTP 中继
  tags: [limitation, tls, rtp]

- id: n46
  title: 邮件通知的 SMTP TLS 认证当前不支持
  type: limitation
  source_pages: p331
  source_chapter: Mail notification Central Services
  source_quote: |
    "To enable SMTP client authentication in the OXO Connect • OMC \ Central Services Global Info \ Email Notification tab, • Note: The authentication with TLS is currently not supported"
  summary: |
    邮件告警的 SMTP 客户端认证可用，但带 TLS 的认证（如 587 STARTTLS 强制站点）不支持——强制 TLS 的邮件服务器接不进来，要另想中继（推断：内网中继或开放 25 的服务器）。
  conditions: 告警邮件配置
  tags: [limitation, email, tls]

- id: n47
  title: 系统级 WAN 用户应用禁用时，每用户 WAN API Access 无效
  type: warning
  source_pages: p334
  source_chapter: Network IP Services / WAN API Access
  source_quote: |
    "When 'Allow User application services from WAN' option is disabled • 'WAN API Access' feature for each subscriber has no effect even though it is enabled • When … enabled • 'WAN API Access' feature for each subscriber has to be enabled to allow WAN access for the corresponding subscriber"
  summary: |
    两级开关是"与"关系：系统级关死时，用户级开了也无效；系统级打开后还要逐用户启用——排障"远程应用连不上"先查两级是否都开。
  conditions: WAN 访问控制
  tags: [warning, network-ip-services]

- id: n48
  title: Console 口重置 installer 密码默认开启、可被客户关闭；关闭后只能现场 LoLa
  type: limitation
  source_pages: p325
  source_chapter: Reset 'installer' password via console port
  source_quote: |
    "In the case the parameter is set to 'disable', the only available alternative to reset the password is to use Lola on site • ALE technical support does not provide any remote service that can reset the installer password or change the control"
  summary: |
    客户可禁用"经 Console 口重置 installer 密码"（状态显示在 OXO Connectivity/Webdiag/Fleet Dashboard）；禁用后密码遗失的唯一出路是现场 LoLa 重载，且 ALE 不提供任何远程重置服务——接手老站点先查这个开关再报价。
  conditions: 密码找回
  tags: [limitation, password, lola]

- id: n49
  title: Rainbow 目录同步先清空 OXO 集体目录且短号随机分配
  type: warning
  source_pages: p309-310
  source_chapter: Rainbow Business directory - End Customer Selfcare
  source_quote: |
    "A synchronization first erases all existing entries of the OCO/OCE system directory" (p309)
    "Existing entries of OXO Collective Repertory are ERASED before sync • Short numbers are randomly affected, not chosen by End Customer" (p310)
  summary: |
    三条：①同步前会擦光 OXO 集体目录现有条目（手工维护的集体目录会被冲掉，先导出备份）；②短号随机分配、客户不能挑；③未连 Rainbow 的 OXO 不同步（多站点各刷各的，短号可能不一致——书内明确 "Short numbers can be different among different Pabx"）。另："Max entries ="原书留白未给上限值。
  conditions: Rainbow 目录同步
  tags: [warning, rainbow, directory-sync]

- id: n50
  title: 互联网远程接入目标端口必须永远 50443（含自定义公网端口场景）
  type: warning
  source_pages: p301, p303
  source_chapter: Remote maintenance via Internet
  source_quote: |
    "For remote access from Internet forwarded to the OXO Connect, the destination port on the OXO Connect must always be port 50443" (p301)
    "Any traffic received on this public port is forwarded by the IAD to the local port 50443 of the OXO Connect system in the LAN" (p303)
  summary: |
    IAD 转发的"目标端口"固定 50443（带专用访问控制），公网侧端口可换（443 被占时任意 XXX），但绝不能直接转发到 443 或其它内部端口——否则绕过访问控制策略。
  conditions: 远程维护接入
  tags: [warning, remote-maintenance, port]

- id: n51
  title: SIP-only 运营商站点无法 modem 远程；远程访问按需开启
  type: limitation
  source_pages: p299
  source_chapter: Remote maintenance through Internet - Problematic
  source_quote: |
    "In case of a SIP provider without ISDN or Analog access, the remote maintenance by modem connection is impossible • Only the remote maintenance by IP connection is possible • Remote access must be enabled only if required"
  summary: |
    纯 SIP 中继站点没有 ISDN/模拟线可走，modem/PPP 远程通道不存在，只剩 IP 远程（且按需开）；投标与 SLA 承诺前先确认站点线型。
  conditions: 远程维护方案选型
  tags: [limitation, remote-maintenance]

- id: n52
  title: Fleet 数据库一天刷新；注册后 24 小时才可见
  type: limitation
  source_pages: p289
  source_chapter: Register OXO Connect in Cloud Connect
  source_quote: |
    "A delay of 24h is required to see the systems"（Cloud Connect database update is once per day，p287）
  summary: |
    注册成功 ≠ 立即可管：Fleet Dashboard/OXO Connectivity 的数据每天刷一次，验收"系统上云"要等 24 小时，勿当场判失败。
  conditions: Cloud Connect 验收
  tags: [limitation, cloud-connect]

- id: n53
  title: 软件更新需 advanced 权限（两门户一致）
  type: limitation
  source_pages: p272-273
  source_chapter: SW update in Fleet Dashboard / OXO Connectivity
  source_quote: |
    "User Privilege 'advanced' is needed for SW update action" (p272)
    "User Privilege 'advanced' is needed for SW update & SW switch action" (p273)
  summary: |
    普通账号只能看指示灯，执行更新/切换必须 "advanced" 权限——运营前把权限矩阵配好，避免现场卡壳。
  conditions: Cloud Connect 软件更新
  tags: [limitation, sw-update, privilege]

- id: n54
  title: 游牧与远程定制默认全禁用，按用户授权
  type: limitation
  source_pages: p466-467, p388
  source_chapter: Nomadic mode & Remote customization
  source_quote: |
    "By default the nomadic mode is disable. It's can be enable user by user in the central services" (p466)
    "By default, the remote customization is disable. It's can be enabled user by user in the feature right … Default value is set to 'NO', and it is in the responsibility of the administrator to give the rights" (p388)
  summary: |
    三重默认关：游牧模式（Cent.Serv 按用户开）、远程定制（Features/Part 2 按用户开）、VMU 远程菜单里的转移选项 7（noteworthy DivRemCust 系统级默认 00）。用户报"手机激活不了游牧/远程改不了设置"先查这三级授权链。
  conditions: 移动性与语音邮箱授权
  tags: [limitation, nomadic, authorization]

- id: n55
  title: 讲义页沿用 OXE 素材（NOE SIP for OXE 水印/字样残留）
  type: errata
  source_pages: p73, p82, p501, p550
  source_chapter: Call Accounting / DECT frequencies / VoWLAN
  source_quote: |
    "NOE SIP … for OXE"（页眉字样，p73/p82/p501/p550 多处）
  summary: |
    至少四页带有 OXE 教材的 "NOE SIP for OXE" 标识（Call Accounting、DECT 频率、8158s 页等）——内容本身适用于 OXO，但个别数字与特性口径（推断）需以 OXO 官方文档复核，不能默认与 OXE 完全等同。
  conditions: 全书引用
  tags: [errata, provenance]

- id: n56
  title: DHCP 池两处口径不一致（.30-.39 vs .10-.39）
  type: errata
  source_pages: p34, p40
  source_chapter: IP settings modification / Public SIP Gateway
  source_quote: |
    "DHCP range : 192.168.1.30 to 192.168.1.39" (p34)
    "Check the IP parameters of the OXO Connect: … DHCP range: 192.168.1.10 to 192.168.1.39" (p40)
  summary: |
    IP 修改章设话机 DHCP 池 .30-.39，紧随其后的公网 SIP 网关章检查清单写 .10-.39（与 PC 静态地址 .10 也撞段）。实验能跑通（lab 环境宽松），但照抄到生产会造成地址冲突；以自己规划为准。
  conditions: IP 规划
  tags: [errata, dhcp, ip-planning]

- id: n57
  title: 书内多处法文/排版残留（证书页、DECT 标识页、OCR 噪声）
  type: errata
  source_pages: p191, p345, p502, p581, p113
  source_chapter: 多章
  source_quote: |
    "les certificats pour le serveur d'appel OXO (OXO Connect et OXO Connect Evolution)" (p345)
    "PARI: Primary Access Right Identifier, identification du PABX, composé de 31 bits…" (p502)
    "weak passwords have been detectedµ"（p321 行文带杂字符，LINE 5669）
  summary: |
    Ed18 存在法文残句（p191 multiset 步骤、p345 证书管理、p502 DECT 标识定义）与排版噪声（"donn't"、"featre"、行尾杂符）——提取与复现时按上下文修正，勿将残句当独立要求。
  conditions: 全书
  tags: [errata, typography]

- id: n58
  title: Cloud Connect 门户域名书内两种写法并存
  type: errata
  source_pages: p264-269, p272-273
  source_chapter: Cloud Connect
  source_quote: |
    "Fleet Dashboard https://fleet-dashboard.al-enterprise.com/" (p267) vs "https://fleet-dashboard.enterprise.alcatel-lucent.com" (p272)
  summary: |
    同一门户在架构页写 al-enterprise.com、在 SW 更新页写 enterprise.alcatel-lucent.com——门户域名随 ALE 站点改版演进过，实际以登录跳转为准，文档引用时统一成当前可用域名。
  conditions: Cloud Connect 门户访问
  tags: [errata, cloud-connect, domain]

- id: n59
  title: AA 树与语音指南定制需 license；冷复位后默认 2 端口进话务员组 8 并应答外呼
  type: limitation
  source_pages: p406, p409
  source_chapter: Automated attendant
  source_quote: |
    "The customization of the tree structure and the voices guides is under license" (p406)
    "After a cold reset, 2 ports are systematically set into the default attendant group n°8 • The automated attendant answers to external incoming calls (by default: because of dynamic routing)" (p409)
  summary: |
    两条：①AA 定制是收费功能（默认树只能留言/转话务员）；②冷复位后系统默认就有 AA 在接外呼（2 端口在组 8）——新装机"外呼进来是语音菜单"不是故障，是默认行为。
  conditions: AA 部署与新机验收
  tags: [limitation, auto-attendant, license]

- id: n60
  title: VMU 远程咨询默认值在迁移与新装间不同
  type: version-trap
  source_pages: p382
  source_chapter: Remote access for voicemail consultation
  source_quote: |
    "In case of migration, this field is disabled • After cold reset or in case of new installation, by default • 'Mailbox consultation from any phone' is enabled • 'Mailbox remote consultation' is disabled"
  summary: |
    迁移场景 "Mailbox remote consultation"（Features/Part 3）字段被置禁用，冷复位/新装则是"本机可查开+远程查关"的组合——升级后用户报"远程查不了邮箱"先核对这组默认值再查权限。
  conditions: 语音邮箱迁移
  tags: [version-trap, voicemail, migration]

- id: n61
  title: 第三方 DECT 话机与 DECT 加密互斥；加密默认关闭
  type: limitation
  source_pages: p364
  source_chapter: IP-DECT encryption
  source_quote: |
    "No support will be provided for third-party sets • Third party device not compliant with encryption will not run on OXO with DECT encryption activated … Encryption is disabled by default, and can activated in OMC"
  summary: |
    激活 DECT 空口加密后，不兼容加密的第三方 GAP 话机直接无法运行（且第三方话机本身不在支持范围）；混用第三方话机的站点开加密前先清点终端。xBS↔呼叫服务器的 IP 段无认证无加密——加密只保护空口段。
  conditions: IP-DECT 加密
  tags: [limitation, dect, encryption]

- id: n62
  title: 端到端语音在 DTLS 下仍是明文（非 SRTP）
  type: misconception
  source_pages: p353, p360
  source_chapter: DTLS OXO certificate / DTLS Encryption
  source_quote: |
    "DTLS (TLS 1.2) secures the signaling. Voice packet are in clear mode (Not SRTP)" (p353)
  summary: |
    别把 DTLS 当"话机加密全案"：它只加密 NOE 话机信令，RTP 语音包仍明文；要语音机密性走 SIP trunk TLS/SRTP（中继侧）方案——合规对话里这两层要分开表述。
  conditions: 安全方案沟通
  tags: [misconception, dtls, srtp]

- id: n63
  title: 公网 SIP 网关实验范围不含短号与紧急号码（无 ADL 表管理）
  type: out-of-scope
  source_pages: p39
  source_chapter: Public SIP Gateway / 1.1 Topology
  source_quote: |
    "Short numbers and emergency numbers are not processed in this exercise, so no ADL table management"
  summary: |
    实验 AF 只验普通号码收发；短号翻译与紧急号码（112 等）的 ADL 表管理在书外（推断：Expert 文档与所在国法规），生产割接前必须补测紧急呼叫。
  conditions: 公网 SIP 上线
  tags: [out-of-scope, emergency, adl]

- id: n64
  title: 网络端口/带宽与生产运营商参数在书外（TC 与运营商合同）
  type: out-of-scope
  source_pages: 全书（实验口径章节通病）
  source_chapter: —
  source_quote: |
    "N values are communicated to you by the trainer"（p208）"the unique ARI number for each customer is to recover on the eBuy site … It is here given by the trainer"（p543）
  summary: |
    全书所有"讲师给值"位（N 值、ARI、密码、接入码、PARK）在生产场景对应：运营商互联参数、eBuy license 资料、客户密码策略、国家 DECT 频段许可——教材不提供生产取值方法论，交付时需外部输入。
  conditions: 生产交付
  tags: [out-of-scope, lab]

- id: n65
  title: 培训机交还前的净化清单（含网络与 installer 密码的冷复位）
  type: warning
  source_pages: p593
  source_chapter: ACTIONS TO PERFORM AT THE END OF A TRAINING
  source_quote: |
    "Erase the MLAA voice guides if used • Clear ACD voice guides if used • Return to ACD / SCR factory settings if used • OXO Cold Reset with the following settings: User data • System data • Network, installer passwords and management data"
  summary: |
    官方净化顺序：先清 MLAA/ACD 语音资产并恢复 ACD/SCR 出厂，再三档冷复位（用户数据/系统数据/网络与 installer 密码及管理数据）。对退役设备同样适用；注意自签证书不受冷复位影响（见 n40），要另行处理（推断）。
  conditions: 培训结束/设备退役
  tags: [warning, cleanup, reset]
```

## 任务覆盖自检（task ↔ id 映射）

| task_id | 覆盖 counter-example 条目 |
|---|---|
| task-01/02 | n01、n02、n03 |
| task-03 | n04、n05、n06、n07、n63 |
| task-04 | n08、n09 |
| task-05 | n09 |
| task-06 | n10 |
| task-07 | n13、n14 |
| task-08 | n15 |
| task-09 | n17、n18 |
| task-10 | n19 |
| task-11 | n20 |
| task-12 | n21 |
| task-13 | n22、n44、n45 |
| task-14 | n23、n24 |
| task-15 | n24、n25 |
| task-16/17 | n52、n53、n58 |
| task-18 | n50、n51 |
| task-19 | n49 |
| task-20 | n46、n47、n48 |
| task-21 | n40、n41、n42 |
| task-22 | n61、n62（n61 为 DECT 加密边界，n62 为 DTLS 语义澄清） |
| task-23 | n43、n44、n45 |
| task-24 | n54、n60 |
| task-25 | n59 |
| task-26 | n26、n27 |
| task-27 | —（原书该章无 Warning/Note/Tips；规格边界在 principle p31） |
| task-28 | n16、n54 |
| task-29 | n28、n29、n30、n31、n32、n33、n34、n35、n36、n61 |
| task-30 | n37、n38、n39 |
| task-31 | n48（LoLa 相关边界）、n65 |
| 全书通用 | n55、n56、n57、n64、n65 |

自检结论：原书 Warning/Note/Tips/Attention/Important 标注全部收编（p14/31/32/42/44/46-47/51/70/73/83/101/105/107/113-114/117-118/127/129/134/147/154/156/164/170/175/179/191/208/233-241/247-248/256/261/289/299/301/303/305/325/327/331/334/353/357/364/369/373/375/378/382-389/410/416/420/431/438/439-441/449/466-467/486/507/517/526/530/533-536/542-544/547/549-551/557/569/575/580-581/593 等），勘误与不一致单列 n21/n23/n55/n56/n57/n58；task-27 原书该章无标注条目，已在自检中说明。
