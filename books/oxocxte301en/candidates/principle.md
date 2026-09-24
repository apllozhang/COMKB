# 原则/清单/规则/公式/数值口径候选 — OXO Connect Advanced (OXOCXTE301EN Ed18)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号、号码）均标注"实验口径"，生产化需替换。数字逐格对照原文。

```yaml
- id: p01
  title: OMC 首连三定值：192.168.92.246 / pbxk1064 仅首连 / 证书装受信任根
  type: rule
  source_pages: p24, p28-30
  source_chapter: OMC Installation
  source_quote: |
    "OXO Connect default IP address 192.168.92.246 … Password 1st login: pbxk1064" (p24)
    "Enter the default installer password pbxk1064 only used for the first connection" (p28)
    "In order to avoid displaying the security alert at each connection, you must install the certificate the 1st time." (p29)
  summary: |
    出厂连接口径：Expert 菜单 + LAN/WAN + 勾 Server authentication + IP 192.168.92.246 + 首连密码 pbxk1064（此后不再用）；Security Alert 弹窗里 View certificate→Install certificate→"Trusted Root Certification Authorities"→导入后不再弹。生产含义：改 IP 后自签证书会重建（CN=接入路由器外部地址），客户端要重新信任。
  conditions: 出厂默认状态；改 IP/路由器外部地址会重建证书（p327）
  tags: [rule, omc, first-connection]

- id: p02
  title: 实验网段基线与 DHCP 池（注意书内两处 DHCP 范围不一致）
  type: metric
  source_pages: p34-36, p40
  source_chapter: OXO Connect IP settings modification / Public SIP Gateway
  source_quote: |
    "Address IP: 192.168.1.246 … Subnet mask: 255.255.255.0 … Default router address: 192.168.1.254 … DNS 1: 192.168.1.250 … DNS 2: 10.20.30.250 … DHCP range: 192.168.1.30 to 192.168.1.39" (p34)
    "DHCP range: 192.168.1.10 to 192.168.1.39" (p40)
  summary: |
    基线：OXO=192.168.1.246、PC=192.168.1.10、网关=192.168.1.254、DNS1=192.168.1.250、DNS2=10.20.30.250。DHCP 池在 IP 修改章写 .30-.39（话机池），公网 SIP 网关章的检查清单写 .10-.39——两处不一致，复现实验时以当章截图语境为准，生产按终端数量自定。改完必须重启 OXO 生效。
  conditions: 实验口径；"DHCP range 不一致"已列入 counter-example（n-勘误类）
  tags: [metric, ip-planning, lab]

- id: p03
  title: SIP 网关参数九 tab 清单（公网 ITSP1 口径）
  type: checklist
  source_pages: p46-53
  source_chapter: Public SIP Gateway / 5.1 Gateway Parameters Details
  source_quote: |
    "SIP numbers format index: 1 (For canonical format) … Select: End of dialing table used" (p46)
    "Registration requested … Registrar name: sip.itsp1.fr … Validate RTP Direct … Put the bandwidth at 5 minimum calls in order to allow external calls … Use RFC 3325 … Choose the ETH0 interface … SIP flows will not be encrypted to this operator, default value" (p47-51)
  summary: |
    九 tab 核对清单：①General：Index 1、标签 ITSP1G1、SIP numbers format index 1（canonical）、用 End of dialing 表；②DNS：DNS A=192.168.1.250；③Domain Proxy：Target/Local domain=Realm=sip.itsp1.fr、Outbound Proxy=gateway1.itsp1.com；④Registration：Registration requested、Registrar=sip.itsp1.fr；⑤Media：RTP Direct 打勾、带宽最少 5 通话；⑥Identity：RFC 3325；⑦Protocol：默认；⑧Topology：ETH0（OCE）；⑨Security：明文（默认）。配完在 SIP Accounts 建 pbxP/alcatel 并把 Gateway Parameters Index 指到 ITSP1G1。
  conditions: 实验口径；生产按运营商参数替换
  tags: [checklist, sip-gateway, menu-path]

- id: p04
  title: 两条 tab 依赖顺序：DNS 先于 Domain Proxy；网关索引回填在网关创建后
  type: rule
  source_pages: p44, p46-47
  source_chapter: Public SIP Gateway
  source_quote: |
    "The Gateway index must be filled in later when the SIP Gateway is created" (p44)
    "The type of IP will be dynamic after configuring the DNS tab … The following setting can only be configured after filling in the DNS tab!" (p47)
  summary: |
    两条硬顺序：①Domain Proxy tab 的参数在 DNS tab 填完前不可配（IP 类型在配 DNS 后变为 dynamic）；②VoIP 外线上的 Gateway index 字段要等 SIP 网关建好后回填。跳序操作会找不到字段或留空失效。
  conditions: 公网与私网网关配置均适用
  tags: [rule, sip-gateway, ordering]

- id: p05
  title: 网关 Media 带宽"最少 5 通话"是外呼放行闸门；RTP Direct 需勾选
  type: rule
  source_pages: p48, p56, p215
  source_chapter: Public SIP Gateway & Private SIP network with ARS
  source_quote: |
    "Validate RTP Direct … Put the bandwidth at 5 minimum calls in order to allow external calls" (p48)
    "Set the bandwidth to a minimum of 5 calls in order to make calls to the outside … Validate direct RTP" (p215)
  summary: |
    公网网关（p48）与私网网关（p215）同一规则：Media tab 里带宽必须 ≥5 通话才能外呼，RTP Direct 要打勾。带宽语义是"该网关允许的并发通话资源"，不是纯 QoS 参数；不设或设 0 表现为外呼不通。
  conditions: 实验口径；生产按并发话务与带宽勘测定值
  tags: [rule, media, bandwidth]

- id: p06
  title: SIP 注册成功判定：History Table 显示 "SIP registration success"
  type: metric
  source_pages: p54
  source_chapter: Public SIP Gateway / 5.4 Check the registration
  source_quote: |
    "OMC/History and Anomalies/History Table … Message displayed: SIP registration success" (p54)
  summary: |
    注册验证口径：OMC/History and Anomalies/History Table 出现 "SIP registration success" 即注册成功；失败类消息在 SIP 话机维度另有 REGISTRATION_REJECT（p154）。这是公网 SIP 网关实验的正式验收点。
  conditions: 消息文本以 History Table 实际显示为准
  tags: [metric, registration, verification]

- id: p07
  title: 酒店参数清单（check-in 序列与默认项）
  type: checklist
  source_pages: p71
  source_chapter: Configuration of the Hotel application / Hotel Parameters
  source_quote: |
    "The different choices offered by the Hotel key are the following: Deposit, name, wake-up, DND, language, barring password." (p71)
  summary: |
    核对清单：①进入 hotel 模式先冷复位（默认 Business 模式）再跑 OMC\Installation Typical\Initial Installation Wizard (Hotel)；②Hotel key 选项六项：Deposit/姓名/wake-up/DND/语言/闭锁密码；③Do at check-in：可系统性激活 DND 与分配 DDI；④Room status：定时后全部或仅占用房切"未清扫"；⑤默认语言（客人来电时前台显示语言）；⑥默认闭锁级别（内线/市话/国内/国际）；⑦默认 wake-up 时间（check-in 时激活）；⑧无操作超时退出 hotel 会话；⑨默认组闭锁（房对房，可开关无组名客人间呼叫）。
  conditions: Wizard Hotel 入口 OMC\Installation Typical\Initial Installation Wizard (Hotel)
  tags: [checklist, hotel, parameters]

- id: p08
  title: Hotel Metering 计费参数表
  type: metric
  source_pages: p72
  source_chapter: Hotel Metering
  source_quote: |
    "Currency: name of the currency unit used … VAT: charge included in the unit cost (in percentage). … Rooms metering levels and thresholds: three levels of charges and two thresholds of charging can be defined. … Ticket footnote: … (a maximum of 40 characters)." (p72)
  summary: |
    参数逐项：货币名；VAT 百分比（含在单价内）；预付金额（可要求押金覆盖话费）；"预付耗尽切断"勾选后余额用完即断；切断前蜂鸣阈值（按剩余脉冲数定义）；房间计费 3 个级别 2 个阈值（脉冲到阈值切换下一档费率）；附加服务=话务员转接外线的收费；小票脚注最长 40 字符。脉冲须由语音运营商传输，否则需外部时长计费器。
  conditions: 路径 OMC/Metering/Metering（tab Hotel Counting for Active Currency）
  tags: [metric, hotel, metering]

- id: p09
  title: Call Accounting Time based 规则：按时长×呼型出脉冲，激活即停 AOC 脉冲，免 license
  type: rule
  source_pages: p73, p82-83
  source_chapter: Hotel Metering / Call Accounting Time based
  source_quote: |
    "Metering service will generate pulses based on the couple (call duration X call type) • Up to three call types (local area, national, international)" (p82)
    "When activated, AOC Pulse based is deactivated (no mix configuration) • Pulse is counted as soon as the first time segment is started • No license" (p83)
  summary: |
    规则四条：①对不支持 AOC（Advice of Charge）的中继提供计费，按"时长×呼型（国际/国内/本地）"生成脉冲，每呼型脉冲秒数自定义（OMC-metering 新 tab Call accounting duration，取值基于安装号屏幕、与 OCD 功能共享）；②适用于全部公网中继（ISDN/模拟/SIP），公/私中继组在内部编号计划定义；③激活时 AOC 脉冲计费停用——两种模式不可混配；④脉冲从第一个时间段开始即计；⑤免 license。
  conditions: OCD=Outgoing Call Duration；AOC=Advice Of Charge（p73 缩写注）
  tags: [rule, call-accounting, aoc]

- id: p10
  title: 账号码表规格：250 上限 / 码 16 位 / 掩码 0-9 或 all
  type: metric
  source_pages: p93-94
  source_chapter: Account codes
  source_quote: |
    "The account codes are configured in the account code table (250 max)" (p93)
    "1 = The code (16 digits maximum) … 6 = The number of digits masked on the metering ticket of the external number (0 to 9, all or Default)" (p94)
  summary: |
    规格表：表上限 250 条；码最长 16 位数字；六字段=码/名称（打印在小票替代主叫名）/是否必须输密码/是否必须身份识别（按目录号）/闭锁类别（1-16 或 none，取话机类别或客人类别）/小票上外呼号码掩码位数（0-9、all、Default）。用法两途：功能键 Account Code New（空字段随用随输/预填字段专码专用）或内部编号计划前缀（Function: New Account Code）。
  conditions: 路径 OMC/Traffic Sharing and Barring/Account Code Table
  tags: [metric, account-code]

- id: p11
  title: 内部替代拨号格式与实验示例
  type: rule
  source_pages: p96, p101
  source_chapter: Internal substitution
  source_quote: |
    "Example of dialing: the manager wants to substitute to his phone (101, pwd 142536) from the workshop phone 110, to call Australia • 66_101_142536_0+61 2 8306 0000" (p96)
    "Test: lock a set and from this set call externally by pretending to be the manager ex. 101: dial 66-101-142536-0-0210x41100" (p101)
  summary: |
    格式：<前缀 66>_<分机>_<该分机密码>_外拨号码。前缀 66=New Account Code（内部编号计划，可 base 指向账号码如 1000 SUBSTITUTION）；也可用可编程键（Account Code New 1000）实现（p101 Tips）。场景价值：全部话机禁国际、仅经理放行时，任何话机（含锁定话机）可"变成"经理外呼。密码与远程替代共用 Remote Access Code 体系之外的"分机密码"。
  conditions: 该功能默认预编在内部编号计划与账号码表（p96）
  tags: [rule, substitution, barring]

- id: p12
  title: 站群监督规格：50 键 / 每键 8 号 / pop-up 5 秒 / 通知 3 秒 / 四条限制
  type: metric
  source_pages: p112-115
  source_chapter: Stations groups supervision
  source_quote: |
    "Number of supervision keys on the system, up to 50" (p114)
    "Pop-up is displayed for 5 sec by default • For modification -> noteworthy address/Timer label: 'TmpMenLTim' … Notification application is displayed for 3 sec by default • … 'NotiAppTim'" (p113)
  summary: |
    规格逐项：每键可监督最多 8 个目录号（内部+DDI 都可）；系统监督键上限 50；通知三方式（pop-up 显示主被叫/音调（空闲态两声长鸣否则一声）/Groupware 键闪烁）；pop-up 默认 5 秒（noteworthy TmpMenLTim）、通知应用默认 3 秒（NotiAppTim）；多来话时 01/02 翻页导航。限制四条：被监督方任意用户类型（IP/TDM 话机、模拟、SIP、My IC Mobile、DECT），监督方仅 DeskPhones；监督员在 3 方会议/菜单屏应用内/ACD 登录应用中时不能应答通知；public 编号计划 priv=yes 的私有呼叫不可监督。
  conditions: 两键成对：Supervision Groupware + Audio Signal Supervision（蜂鸣开关）
  tags: [metric, supervision, groupware]

- id: p13
  title: PIMphony 更新策略参数：全局/用户两级，默认停用
  type: rule
  source_pages: p127-128
  source_chapter: PIMphony installation
  source_quote: |
    "By default, the service is deactivated. Internet connection is required to update PIMphony." (p127)
    "Check the field 'Use customized policy', then 'Periodically' with a period of 6 weeks." (p128)
  summary: |
    规则：在线更新服务两级配置——全局（Central Services Global Info/PIMphony tab：Activated 勾选+Update frequency 手动或周期 N 周；实验设 5 周）与每用户（Subscribers/…/Serv.Cent/PIMphony tab：Use global policy 或 Use customized policy——Never/Manually/Periodically N 周+下载后自动安装开关；实验对 100 设 6 周 Team profile）。默认全系统停用；更新需互联网；PIMphony 注册 on-site 需互联网（实验选 Cancel）。
  conditions: 基于 license 检查 profile 与版本
  tags: [rule, pimphony, update-policy]

- id: p14
  title: SIP 话机接入参数基线（端口 5059 / 注册计时器 ≥120s / UDP 优先 / SNTP）
  type: metric
  source_pages: p149-153
  source_chapter: SIP Phones
  source_quote: |
    "Default Transport Mode: UDP … Domain name: OXO Connect IP address if empty … Authentication Realm: OXO Connect IP address if empty" (p149)
    "SIP username: Directory number of the subscriber … Registrar and Proxy SIP: OXO IP@:5059 … Registration timer: >=120 seconds … Transport protocol: Prefer UDP … SNTP IP address: OXO IP@" (p153)
  summary: |
    接入基线：注册/代理地址=OXO IP:5059；域与 Authentication Realm 留空则用 OXO IP；注册计时器 ≥120 秒；传输优先 UDP；SNTP 由 OXO 提供（同步话机时钟，供 GMT）；SIP 用户名=分机号，注册密码在订阅户 IP/SIP 参数里读。Basic 与 Open SIP 话机都在订阅户列表建（IP Subscriber 改类型），均需虚拟 MAC+注册密码；Open 型多一项特殊功能权 Conference Bridge Allowed（启用 SIP Enhanced 话机 5 方会议，系统最多 3 路，p151）。
  conditions: 非白名单第三方话机按 RFC 符合度 best effort（p143）
  tags: [metric, sip-phone, registration]

- id: p15
  title: 编解码透传开关矩阵与 RTP 三处理取舍
  type: rule
  source_pages: p144-148
  source_chapter: SIP Phones / Codec pass-through / RTP Proxy
  source_quote: |
    "Codec pass-through for SIP phones = □ Only OXO Connect audio codec can be use (G.711,G.723,G.729, G722, G722.2, OPUS) • Codec pass-through for SIP phones= ▪ All Audio/Video codec can be used according end-devices capabilities" (p144)
    "Direct RTP: Media flows are established directly between the endpoints of the call. It is the most optimal solution" (p148)
  summary: |
    开关矩阵：话机侧透传（OMC\VoIP parameter\SIP Phone）与中继侧透传（OMC\External lines\SIP\Media）各自独立——关=仅 OXO 六编解码（G.711/G.723/G.729/G722/G722.2/OPUS）；开=按终端能力全量音视频。媒体三处理取舍：DSP 通道（压缩解压，非最优）→RTP proxy（同编解码同 framing 仅路由，升容量/降 CPU/省 DSP）→Direct RTP（端点直连最优，TLS/SRTP 场景不可用 p368）。无 Direct RTP 且无透传时用 Proxy RTP 固定端口（OMC\VoIP parameter\SIP Trunk）。
  conditions: ALE IP 系列可 Direct RTP；TDM 系列耗 1 VoIP 资源（p147）；SIP 话机不支持游牧（p147）
  tags: [rule, codec, rtp, media]

- id: p16
  title: Hot Desking 容量与计费口径：200/200、前 2 免费、50 包
  type: metric
  source_pages: p174-175
  source_chapter: Hot Desking
  source_quote: |
    "Hot Desking User: 2 are free of charge, then by package of 50 • Max capacity: 200 Hot Desking Positions / 200 HD users" (p174)
    "682 for logout • 683 for login" (p175)
  summary: |
    口径：容量 200 HDP+200 HDU；HDU 计费=前 2 个免费、之后按 50 一包；默认前缀 683 登录/682 注销（内部编号计划 Hot Desking 函数，可用软键替代）；DECT 手柄可作 HDU multiset 的副成员；抢占登录时前一 HDU 自动注销。个人环境含：VM/呼叫日志/用户设置/密码/IM/键配置/呼叫路由/multiset/移动性/语音邮箱。监督：Webdiag Services tab 看占用并可强制 Log out。
  conditions: 需 license；适用 ALE DeskPhone、IP Desktop Softphone、模拟话机
  tags: [metric, hot-desking, licensing]

- id: p17
  title: Multiset 规格：1 主 2 副 / 共享主号 / MLTSETRING 三值
  type: metric
  source_pages: p185-189
  source_chapter: Multiset
  source_quote: |
    "One primary set and a maximum of two secondary sets • One directory number • Same level of service for every associated set" (p185)
    "MLTSETRING=00 (long ringing) • MLTSETRING=01 (no ringing, default value) • MLTSETRING=02 (short ringing)" (p188)
  summary: |
    规格：1 主站+最多 2 副站；全部话机类型可混（DECT/ALE DeskPhone/PIMphony/SIP/模拟）；一话机仅属一个 multiset；全部共享主站目录号、忙态联动、副站可留自己目录号收话；副站继承主站 14 项功能（p187 清单：VM/文本邮箱/个人助理/密码/闭锁/流量分担/快速拨号/语言/功能权/重拨/动态路由/转移/选择转移/计费）。空闲副站新呼叫呈现由 noteworthy MLTSETRING 定：01 不铃（默认）/02 短铃/00 长铃。寻线组组呼全铃；秘书不能当经理副站（反之亦然）。
  conditions: 创建位置在主站（Secondary sets 按钮）；常见形态主有线+副 DECT=Twinset
  tags: [metric, multiset]

- id: p18
  title: ARS 溢出两条实现路径：表内子线 vs 流量分担矩阵强制
  type: rule
  source_pages: p200-203
  source_chapter: ARS management / Other mechanisms
  source_quote: |
    "Overflow management: Create sub-line for each trunk group list" (p200)
    "If the overflow is handled by the trunk group list, then the traffic sharing matrix can be used to force the overflow" (p201)
  summary: |
    规则：溢出优先在"中继组列表内加子线"（同一列表下一索引指向备份中继组，如 400/402 满后走 401 ISDN）；若按列表处理，可用流量分担矩阵强制特定业务（如传真行：400=-、401=+、402=-，即传真只走 ISDN）。ARS 表内溢出（p203）另用子线+替换实现私网溢出公网（例：Priv 21 00-99→21 走列表 1；子线替换为 029857 走列表 2 公网）。
  conditions: 子线=同一 Network/前缀行的第二目的行
  tags: [rule, ars, overflow]

- id: p19
  title: Internal ARS 四时段配置口径与虚拟 Provider 技法
  type: rule
  source_pages: p229-231, p235-237
  source_chapter: Internal ARS management
  source_quote: |
    "The prefix placed in field Substitute will be analyzed in afterward in the Internal Numbering Plan" (p229)
    "The internal ARS uses a virtual trunk groups local … Find 'Local' in the list of trunks and select it." (p237)
  summary: |
    技法四条：①ARS 表每个替代目的地建一条子线（Substitute 填分机号/寻线组号，随后在内部编号计划分析落地）；②每目的地建一个虚构 Provider（如 "Extension 101"），中继组列表索引选 Local（虚拟中继组）配该 Provider；③Day Groups 把星期映射到组号（可自定义，实验把周六日设组 1、工作日组 2）；④Hours 表按"组号→Provider"排时段（8-12→101、12-14→102、14-18→103、18-8 与周末→兜底行给消息寻线组）；设段尾时间=下一段开始时间。非营业时间目的地用"欢迎消息挂寻线组"（OMC/Hunting group 录 MSG1）。
  conditions: 实验取值；欢迎消息别与实体 MoH 混淆（p241）
  tags: [rule, internal-ars, time-routing]

- id: p20
  title: 多实体参数表：4 实体 / MoH 10 分钟 / 问候 200 / 预告 20 / 消息 320 秒
  type: metric
  source_pages: p243, p246-248
  source_chapter: Multiple entities
  source_quote: |
    "The system supports 4 Entities … Software license: up to 4 entity music-on-hold - 10 minutes" (p243)
    "Number of entries for individual greetings: from 15 to 200 • Number of preannouncement messages: from 8 to 20 • Message duration: from 128 to 320 seconds" (p248)
  summary: |
    参数表：实体上限 4；每实体 MoH 上限 10 分钟（无该实体录制 MoH 时回退默认 MoH 或磁带）；实体间呼叫禁止开关连带影响立即/忙转、RSL 键、individual pickup、文本/语音邮箱（话务员组话机不受限）；多实体带来系统限制增强：个人问候条目 15→200、预告消息 8→20、消息时长 128→320 秒；计费小票新增用户实体信息；中继组共享靠 ARS+流量分担+闭锁组合。
  conditions: MoH 按"保持外呼的用户实体"选择播放
  tags: [metric, entity, moh]

- id: p21
  title: 伪多公司四步法：链路类别配对 + 矩阵直线 + ARS 透明线 + Char 显示
  type: rule
  source_pages: p250-251, p257-261
  source_chapter: Pseudo multi-company configuration
  source_quote: |
    "Manage a traffic sharing link category level for the A extensions: 3 for example … Modify the traffic sharing matrix by creating a straight line from 1/1 to 16/16" (p250)
    "The users of the two companies make up 0 to go out and see character 1 or 2 appear on the set display confirming the taking of their respective trunk group" (p261)
  summary: |
    四步：①话机管理——A 公司话机流量分担链路类别=X（讲义例 3，实验用 1），B 公司=Y（讲义例 4，实验用 2）；②副中继组——400（A）与 401（B）设相同类别值；③流量分担矩阵——拉 1/1 到 16/16 直线（类别相同才可互走）；④ARS——主中继行 base 改 ADL 进 ARS 表、加透明线（Trunk group list 1）、列表含两公司中继组并设 Char 1/2。验证：拨 0 外呼，话机显示字符 1 或 2 即确认占了各自中继组。
  conditions: 两公司可拨同一外拨前缀但各走各的外线（计费分账）
  tags: [rule, multi-company, traffic-sharing]

- id: p22
  title: Cloud Connect 注册口径：自动/免 license/默认启用/状态串/24h 延迟
  type: metric
  source_pages: p264-265, p287-289
  source_chapter: Cloud Connect / Register OXO Connect in Cloud Connect
  source_quote: |
    "Registration of OXO Connect will take place automatically. By default, the Cloud Connect right is enabled. The service does not require licenses." (p287)
    "The status must be: Connected with final credentials" (p288)
    "A delay of 24h is required to see the systems" (p289)
  summary: |
    口径：接入客户网络并放行互联网即自动注册（默认启用、免 license、无需配置动作）；验证看 OMC/Cloud/Cloud Connect 状态串 "Connected with final credentials"；Fleet 数据库一天刷新一次，注册后 24 小时才能在 Fleet Dashboard 看到。系统定位三法：CC-Prd-id（<R3.0）、CPU-id、客户参考（Fleet/Install）。
  conditions: 前提 DNS 可用（基线 DNS1=192.168.1.250，实验口径）
  tags: [metric, cloud-connect, registration]

- id: p23
  title: 软件更新指示灯与权限口径：[D..]/[.S.]/[..P] + advanced 权限
  type: rule
  source_pages: p271-273
  source_chapter: HOW and WHEN to trigger a SW update
  source_quote: |
    "[D..] if Download indicator is RED: the Current SW version running in the call server is Older that the 'Recommended Version'. → Update is recommended … When [DS.] indicator are red, action is recommended" (p271)
    "User Privilege 'advanced' is needed for SW update action" (p272)
  summary: |
    规则：指示灯三位——[D..] 下载建议、[.S.] 切换建议、[..P] 升级进行中；D 或 S 红=建议动作（运行版本旧于推荐版本）；无 Download 指示=无需更新。操作路径：多台 Fleet Dashboard（筛选→SW Minor Update，太旧标红）、单台 OXO Connectivity（Switch/Download 状态+动作按钮）；两处均需用户权限 "advanced"。服务免 license，支持单台与批量并行更新。
  conditions: 下载后按 swap 时间配置自动切换版本
  tags: [rule, sw-update, fleet]

- id: p24
  title: 远程维护端口铁律：入站目标端口永远 50443
  type: rule
  source_pages: p300-305
  source_chapter: Remote maintenance via Internet
  source_quote: |
    "Port 50443 is dedicated to connections from the Internet, and it applies adapted access control policies" (p300)
    "For remote access from Internet forwarded to the OXO Connect, the destination port on the OXO Connect must always be port 50443" (p303)
  summary: |
    铁律：OMC↔OXO 默认 HTTPS 443；互联网入站一律转发到 50443（该端口带专用访问控制策略）。三种形态：①固定公网 IP/DNS——IAD 转发公网 443→50443；②公网 443 被占——转发 {@IPPUBLIC, 任意 XXX}→{@IPOXO, 50443}；③管理 VPN——专用管理 IP（仅 OMC 可配，OMC/Hardware and Limits/LAN-IP Configuration，激活/停用须 warm reset，随系统保存恢复，每站点可用同一 IP）。OMC 经代理时 Options→proxy parameters（特权用户默认密码 OMCAdmin）。访问控制三开关在 OMC/security/Network IP Services。
  conditions: SIP-only 站点无法 modem 远程，仅 IP 通道；远程访问仅在需要时启用（p299）
  tags: [rule, remote-maintenance, port]

- id: p25
  title: 密码策略与自动检查参数：8 位固定 / AutoPwdChk 4 周默认 / 01-52 周 / 00 禁用
  type: metric
  source_pages: p315-319, p321-323
  source_chapter: Password Security Enhancement / Automatic Password Check
  source_quote: |
    "It is mandatory for Installer to change all the default passwords in order to proceed further" (p315)
    "Enabled by default, with default periodicity of 4 weeks … every xx weeks (allowed values 01 to 52 weeks, 00 function is disabled) • Systematically after warm reset" (p316)
    "Password rules have been implemented and requires now a minimum of one uppercase letter, one lowercase letter, and one numeric character (fixed length of 8 characters)" (p319)
  summary: |
    口径：首登强制 installer 改全部默认密码才能继续；管理密码固定 8 位、至少 1 大写+1 小写+1 数字；自动检查默认启用、周期 4 周（AutoPwdChk 可配 01-52 周，00=禁用；激活立即查一次+warm reset 后必查）；默认密码检查覆盖管理密码与 SIP 话机管理员密码，弱密码检查覆盖用户与管理密码；发现问题生成 urgent alarm 历史事件并可邮件通知管理员（Global Central Services\Admin Email Address）；订阅户密码管理支持批量重置全部/仅弱密码（无 license）；XML 审计工具用法见 TC2249。
  conditions: SIP 话机管理员密码的 Read（仅非默认）/Reset/Set 需 OMC Expert 级+当前会话密码
  tags: [metric, password, security]

- id: p26
  title: VMU/WS API 锁定公式：失败翻倍 10→20→…→1440 分钟
  type: formula
  source_pages: p328-329, p384
  source_chapter: OXO Connect WS API authentication / Remote Access locking
  source_quote: |
    "Lockout time is set as ten minutes after the first denial and twenty minutes after the second denial… • The lockout time is doubled for each denial (24 hours max value, 1440 minutes)" (p384)
    "It is configurable using noteworthy address 'VMUMaxTry'" (p328)
  summary: |
    公式：锁时 T(n)=10×2^(n-1) 分钟（n=第 n 次连续失败认证），封顶 1440 分钟（24 小时）；本地与远程访问共享失败计数，锁定期内正确凭据也被拒。解锁五途：OMC 重置该设备密码（重置后须本地改密）、Webdiag Services/User Accounts、话机 Settings 改密（记得密码时）、话务员会话、PIMphony Operator 监督模式。锁定/解锁均生成历史事件；远程锁定时邮件通知用户与管理员（用户邮箱在订阅户 Cent.Serv）。
  conditions: 阈值 noteworthy VMUMaxTry；LAN 本地访问不受锁（p329）
  tags: [formula, lockout, security]

- id: p27
  title: Remote Access Code（ACC）两级控制规则
  type: rule
  source_pages: p383
  source_chapter: Two levels access control for remote access to voice mail
  source_quote: |
    "Empty → remote access to VM is based on standard user authentication = phone number + user password … Any value → remote access to VM is based on Access Control Code + phone number + user password … Access control code will get by default a system generated random 6 digits value • System administrator can modify, delete the ACC (up to 16 digits) • ACC is kept after warm reset and newly generated after cold reset" (p383)
  summary: |
    规则：ACC 同时用于远程替代与远程语音邮箱接入。空值=标准认证（话机号+用户密码）；设值=三级认证（ACC+话机号+用户密码）。默认系统随机生成 6 位；管理员可改/删，最长 16 位；warm reset 保留、cold reset 后重新生成。防盗打第一防线（书内反复强调）：勤改语音邮箱密码、不用简单数字序列、遵 TC1143。
  conditions: 路径 OMC/Security/Passwords/Remote Access Code（实验值 780911/615243 为实验口径）
  tags: [rule, acc, voicemail, security]

- id: p28
  title: AA 规格表：2 树 / 2 级 100 节点 / 每级 10 选 / 4 语言 / 端口 2-8
  type: metric
  source_pages: p380, p406-407, p409-410
  source_chapter: Automated attendant
  source_quote: |
    "Two different tree structure: day (Normal) /night (Restricted) • Two menu levels by tree (100 nodes in the tree) • One main menu with 10 choices • 10 submenus with 10 choices … 4 voice guides possible languages" (p407)
    "After a cold reset, 2 ports are systematically set into the default attendant group n°8" (p409)
  summary: |
    规格：树 2 棵（Normal=Opening Hours/Restricted=Closing Hours，手动或随系统时间范围自动切）；每树 2 级共 100 节点；主菜单 10 选（9 种功能）；10 个子菜单各 10 选；每菜单 1 可定制语音指南+每树 1 问候+两树共用 1 再见；4 语言；语音端口 2-8（与语音邮箱/Audiotext 共享，默认动态分配）。冷复位后 2 端口进默认话务员组 8 并默认应答外呼。语音格式：系统 ADPCM (G726) 4bits 8Khz Mono；OMC 可转 CCITT A-Law/µ-Law 8bits 8Khz Mono、PCM 16bits 8Khz Mono。
  conditions: 树结构与语音指南定制需 license；转接模式 noteworthy AATypTrf（02 半监督默认/00 盲转）
  tags: [metric, auto-attendant]

- id: p29
  title: AA 免费拨号开关：AAGrDialng 默认禁 / AAGrTransf 默认启
  type: rule
  source_pages: p419-421
  source_chapter: Automated attendant enhancement - Free dialing
  source_quote: |
    "AAGrDialng: enable (01) / disable (00: Default) direct choice (1 to 8) dialing during company greetings. • AAGrTransf: enable (01: Default) / disable (00) transfer to operator when dialing 0 or 9 during company greetings." (p420)
    "Free dialing is not available during 'Press *' and 'Language selection' menus." (p420)
  summary: |
    规则：问候消息期间——0/9 转话务员（AAGrTransf 默认 01 启用）、# 邮箱咨询、1-8 开始直拨分机号（AAGrDialng 默认 00 禁用，开启后无需语音指南）；AA 主/子菜单期间带语音指南免费拨号（0=Free dialing，播 "if you know the extension you require press 0"+"dial an extension number"）。两处例外：Press '*' 与语言选择菜单期间免费拨号不可用。
  conditions: 问候期直拨序列示例 *100（p419）
  tags: [rule, auto-attendant, free-dialing]

- id: p30
  title: MLAA 规格表：5 树 / 3 级 / 16 端口共享 / 100 消息×4 语言 / 12000 秒总限
  type: metric
  source_pages: p428, p431, p439-440
  source_chapter: Multiple Automated Attendant (MLAA)
  source_quote: |
    "A maximum of 5 tree structures are manageable … Tree structure up to 3 levels … Up to 10 choice by level • Up to 4 Language by tree" (p428)
    "Number of dedicated MLAA ports (0 to16) … The MLAA port number is taken into account after an ACD engine reset or after 10mn without reset" (p431)
    "100 messages per language (4 max) … The total maximum size of all voice prompts must not exceed 12000 seconds (200 minutes)" (p439-440)
  summary: |
    规格逐项：树数按 license（1 或 5）；树 3 级、每级 10 选、每级时间范围（共 10 个时段）、每树最多 4 语言（独立于系统语言，语言 1 默认）；专用 MLAA 端口 0-16（与 ACD 共享 16 上限；改动在 ACD 引擎复位后或 10 分钟无复位后生效）；每语言 100 消息（语言 N 消息号 N001-N100.wav），默认每条 15 分钟（noteworthy MLAA_MSG 可改），全库总量硬上限 12000 秒（示例：400×30s=200×60s=100×120s=50×240s=12000s）；wave 格式 CCITT 8kHz 16bits mono A-Law/µ-Law；通用参数：返回码 *（2/3 级回 1 级、1 级回语言选择）、# 结束免费拨号、位间超时 2 秒；Save as 存档不含 line parameters。
  conditions: 消息改动同样要引擎复位或等 10 分钟（p441）
  tags: [metric, mlaa, capacity]

- id: p31
  title: SCR 规格表：10000 规则 / 10 计划 / 64 特殊日 / 8 条 VP
  type: metric
  source_pages: p451, p454-457
  source_chapter: Smart Call Routing
  source_quote: |
    "Rules available: 10 000" (p454)
    "Up to 10 plans (In addition of the plans used for ACD)" (p455)
    "64 Exceptional days are in common with ACD" (p456)
    "8 voice prompt from 107.wav to 807.wav" (p457)
  summary: |
    规格：规则 10000 条（编辑器内嵌 ACD 呼叫路由表，增客户码/Voice Prompt/Planning/Opened/Closed destination 字段，CSV 导入导出兼容）；开闭计划最多 10 个（ACD 计划之外另计）；特殊日 64 个与 ACD 共用；客户码语音提示 8 条（107.wav-807.wav，与 ACD 语音消息共用，MMC 亦可录）；通配符 X——CLI/DID 中隔离号码段、客户码中替换整码；日志从监督台出、Web Diag 导出；license=SCR+1 个 Supervisor Console。
  conditions: 目的地四类：ACD 组/MLAA 寻线组/本地或寻线组号/外部或集体快速拨号
  tags: [metric, scr, capacity]

- id: p32
  title: 游牧 CLI 发送规则与启用链
  type: rule
  source_pages: p466-467, p474
  source_chapter: Nomadic mode
  source_quote: |
    "if the caller is external, his CLI is sent to the nomadic terminal … If the caller is internal and has a DDI, this DDI is sent … Else the OXO Connect installation number is sent … Accounting ticket includes new information for nomadic calls" (p466)
    "Tick: Nomadic right … Check the automatic creation of a virtual terminal, named 'Virtual Nomadic' with the Nomadic option" (p474)
  summary: |
    规则：来话 CLI 按主叫身份三选一发到游牧终端——外部主叫发原 CLI；内部主叫有 DDI 发 DDI；否则发系统安装号；游牧呼叫在计费小票新增信息。启用链：订阅户 Cent.Serv 勾 Nomadic right（自动建 "Virtual Nomadic" 虚拟终端）→VMU 远程定制菜单 9→选项 6（停用/激活/目的地号，格式 0021PN41102 后按 # # 确认）→话机显示 "Nomadic mode"。也可经 PIMphony 可编程键激活。游牧与远程定制默认均禁用、按用户授权（Features/Part 2）。
  conditions: SIP 话机不支持游牧（p147）
  tags: [rule, nomadic, cli]

- id: p33
  title: 远程替代回环格式：#100-#199 + 内部 ARS 三表配置
  type: rule
  source_pages: p471, p479-480
  source_chapter: Voice Mobility solution with remote substitution
  source_quote: |
    "Secondary Trunk Group #100 #199 ARS Keep Yes … Prefix Ranges Substitute TrGpList #1 00-99 1 2 … 2 Local" (p471)
    "#100 to #199 in order to avoid conflict with line 100 to 199 … TMN: Keep to send the dialing to the ARS table … Private= yes" (p479)
  summary: |
    格式：远程替代后拨内部号要加 # 前缀（#101 表分机 101），避免与本地直拨 100-199 冲突。三表配置：①内部编号计划 Secondary Trunk Group 段 #100-#199 base=ARS、NMT=Keep、Priv=Yes（#9→话务员同理）；②ARS 表 Network=Priv、Prefix=#1、Range=00-99（Substitute 去掉 #）；③中继组列表 Index=Local（内部呼叫）。流程：拨替代 DDI→听音→远程接入码→分机号→密码→拨号音后 #"分机"。
  conditions: 远程接入码在 OMC/Security/Passwords/Remote Access Code（实验 615243 实验口径）
  tags: [rule, remote-substitution, ars]

- id: p34
  title: DECT 容量表：80 xBS/200 手柄/11 并发 vs 60 IBS/6 并发
  type: metric
  source_pages: p494-496, p485
  source_chapter: IP DECT Solution / DECT TDM reminder
  source_quote: |
    "IBS connected on UA equipment … Up to 60 IBS • 1 PARI for the system • Up to 6 calls peer IBS • 1 UA equipment → 3 simultaneous calls • 2 UA equipments → 6 simultaneous calls • 200 Dect handset" (p494)
    "Up to 80 DECT IP-xBS • 1 PARI for the system (common with IBS) • 11 simultaneous calls per xBS • 200 DECT handsets" (p495)
  summary: |
    双轨容量：TDM 轨——IBS 接 UA 板，最多 60 IBS、每 IBS 6 并发、1 UA=3 并发/2 UA=6 并发、200 手柄；IP 轨——8378 IP-xBS 接 IP 网，最多 80 xBS、每 xBS 11 并发（12 时隙去 1）、200 手柄、需 IP-DECT 用户 license。混合拓扑：IP 与 IBS 可共存同一系统，共用唯一 PARI；切换仅同集群内。小分支：8328 SIP-DECT 单基站 20×8214 手柄（G711 10/G.729 4/G722 5 并发），双基站 20 并发 G711/8 G729/8 G722 且有空口同步与切换。全局限制查 MyPortal《OXO Connect Global Limits》。
  conditions: 8214 仅 R6.0 MD1（R5.2 兼容计划 2023 底）；预定义消息图标计划 2023 底（p486）
  tags: [metric, dect, capacity]

- id: p35
  title: DECT 覆盖判定口径：-72 dBm 语音质量边界 / 每 30 秒重扫
  type: metric
  source_pages: p503, p533-534
  source_chapter: RSSI list & Radio coverage rules
  source_quote: |
    "A handset must rescan its local radio environment at least every 30 sec … Thanks to the RSSI list a xBS or a handset is able to select best channel (least interfered) for a call" (p503)
    "measurement of the -72 dBm attenuation at the limit of the area … Zone of voice quality -72 dBm -80 dBm" (p533)
  summary: |
    口径：话机至少每 30 秒重扫无线环境，按空闲 TS/F 对存 RSSI 列表选最少干扰信道；勘测时以 -72 dBm 为覆盖区边界（-72 dBm 以内=语音质量区，-80 dBm 为勘测模式下限）；音质验证要在通话中测，最少两台话机注册才能建立呼叫，也可按 "0"+拨号键听连续拨号音。功率基准：欧洲均值 10mW/峰 250mW、美国 4mW/100mW。
  conditions: 勘测用 SSK 专用 xBS（固件与生产不同）；手册 8AL90874USAA
  tags: [metric, dect, site-survey]

- id: p36
  title: SUOTA 参数：50 并发 / 4-8 小时 / 充电座 swap / 话务优先
  type: metric
  source_pages: p526
  source_chapter: Software Update Over The Air for DECT handsets
  source_quote: |
    "Simultaneous download up to 50 (configurable). • Download duration: ~ 4-8 hours (depending on DECT traffic) … The download process has a lower priority than DECT user calls • When a phone has any telephonic activity the download process is paused" (p526)
  summary: |
    参数：适用 8214/8234/8244/8254/8262/8262EX，经 8378 IP-xBS 与 8379 IBS；自动/手动/关三模式经 WebDIAG 配置；平台限 OCE 与 PowerCPU EE；并发下载最多 50（可配），整包下载约 4-8 小时（视话务）；下载优先级低于用户呼叫，话机有话务活动即暂停；下载完成后话机须放充电座执行 swap，多色 LED 显示进度，中途取下不停 swap。
  conditions: swap 就绪时话机有专门图标提示
  tags: [metric, suota, dect]

- id: p37
  title: 证书四类端口与签发矩阵（2048 默认/4096 R6.2 起）
  type: metric
  source_pages: p346, p348, p351, p353, p356
  source_chapter: DIGITAL CERTIFICATES
  source_quote: |
    "Server Certificate … Port 443, 30443 … 2048 (d) 4096 … Public Server certificate … Port 50443 … Issuer External PKI … DTLS OXO certificate … Port 7780" (p346/348/351/353)
    "Generic OXO server certificate … Port 10443 … 2048 … OXO HAN Server certificate … Port 11443 … RSA Keys 4096 2048" (p356)
  summary: |
    端口与签发矩阵：Server Certificate（LAN 身份：HTTPS 443/30443；OXO Root CA 自签默认或外部 PKI；2048 默认/4096 可配）| Public Server certificate（WAN 身份：SIP-TLS+HTTPS 50443；仅外部 PKI、默认未定义；OCE 与 OCE FE）| DTLS OXO certificate（NOE 话机：7780；DTLS OXO Root CA 自签 4096 不可配或外部 PKI）| Generic OXO server certificate（ALE SIP 话机部署：10443；自签 2048 不可配；覆盖 8001/8008 CE/8008G CE/8082/8002/8012 退市机）| OXO HAN Server certificate（ALE Wi-Fi AP：11443；R6.2 起 4096，此前 2048，迁移全透明）。证书支持 1024/2048/4096 位（p326）；ALE 推荐设备与呼叫服务器统一 4096（p342）。
  conditions: OpenSSL V3 仅 R6.2 起；<R6.2 建议迁 R6.2（p342）
  tags: [metric, certificate, ports]

- id: p38
  title: 4K 证书升级路径与回滚铁律
  type: rule
  source_pages: p349-350, p352, p354-355, p357
  source_chapter: DIGITAL CERTIFICATES / Server certificate migration
  source_quote: |
    "2 Steps are required … Certification authority … Generate a new certification authority • Choose 2048 or 4096 (*) … The OXO root CA certificate is regenerated with the required RSA key length … Server Certificate … Generate a new server certificate … Reboot (only OCE)" (p349)
    "Roll back requires specific actions before rolling back if the upgrade to 4K was performed … switch again to 2K certificates (Via WebDIAG) and then roll back." (p357)
  summary: |
    路径：自签 2 步（CA 再生成→服务器证书再生成，CA 与证书密钥长度必须一致；重启仅 OCE）→检查 WebDIAG/Server Certificate/current certificate（看密钥长度与签发者）；外部 PKI 4 步（CA 再生成→CSR（PKCS#10）生成下载→外部 CA 签→WebDIAG 导入安装）；Public Server 3 步（CSR→签→导入，系统重启；OCE 配公共 FQDN 时同页生成）；DTLS 自签 1 步/外部 3 步。铁律：R6.2 以不同格式存 4K（非 2K）证书密钥——升级到 4K 后回滚旧版本前必须先经 WebDIAG 切回 2K，否则 OMC 报错；迁移 R6.2 本身无缝保留证书。
  conditions: LoLa 可用于重载系统软件（p357）
  tags: [rule, certificate, rollback]

- id: p39
  title: TLS/SRTP 参数表：5061 信令端口 / 四套 AES 套件 / OCE-FE 各 20 通话
  type: metric
  source_pages: p367, p373, p375
  source_chapter: SIP trunks: TLS/SRTP
  source_quote: |
    "Cryptographic suites: AES Counter Mode [128 and HMAC SHA1 80] [256 and HMAC SHA1 80] [128 and HMAC SHA1 32] [256 and HMAC SHA1 32]" (p367)
    "SIP TLS signaling port: 5061" (p373)
    "WebRTC GW + SIP PROXY 20 calls max. 20 calls max." (p375)
  summary: |
    参数：SIP TLS 信令端口 5061（OMC/Voice Over IP/VoIP: Parameters→SIP Trunk）；认证模型=服务器证书认证或双向认证（迁移旧版时启用双向需重生成证书，p373 note）；密码套件四种（AES-CTR 128/256 × HMAC SHA1 80/32）；拓扑 Hosted 或 Static NAT；TLS 模式下 Direct RTP 不可用。OCE-FE 代理容量：WebRTC GW 与 SIP PROXY 各 20 通话上限（共存时各自 20）；OCE FE 的认证/DNS/套件/静态 NAT 四项被该 OXO 全部 SIP TLS 网关共享；SIPS URI 不支持；ETH1 当前不用于 SIP 流量。
  conditions: 私网两 OCE 互联需 Static NAT；对端仅 TLS client 时停用双向认证（p369）
  tags: [metric, tls, srtp, capacity]

- id: p40
  title: DTLS 容量与模式口径：300 连接 / 免 license / 仅 OCE / 语音仍明文
  type: metric
  source_pages: p360-362, p353
  source_chapter: DTLS Encryption
  source_quote: |
    "Supported ALE VOIP devices: Essential & Enterprise ALE IP phones, Remote workers • Up to 300 DTLS connections • License free … Available only with platform OXO Connect Evolution" (p360)
    "DTLS (TLS 1.2) secures the signaling. Voice packet are in clear mode (Not SRTP) • DTLS is activated by default (OCE)" (p353)
  summary: |
    口径：DTLS 加密 ALE VoIP 话机信令通道（TLS 1.2），语音包保持明文（非 SRTP）；上限 300 连接；免 license；仅 OCE 平台；OCE 默认激活。两模式：Standard=Generic Certificate（SMB 推荐，全零接触，话机跨 OCE 免清除移动）；Expert=Specific Certificate（锁定端点到指定呼叫服务器，管理员自有证书）。部署开关两级：OMC/Security/DTLS Encryption（系统）与订阅户 IP-SIP parameters（每用户）；话机侧显示钥匙图标。
  conditions: 支持 NOE 话机清单见 p353（ALE-500/400/300/30/30H/20/20h、Premium 8078s/8068s/8058s/8028s、8018、8008）
  tags: [metric, dtls, encryption]

- id: p41
  title: ETH1 管理限制矩阵：disabled 时仅 SIP trunk 保留
  type: rule
  source_pages: p312
  source_chapter: OCE ETH1: restricted access control
  source_quote: |
    "Limit the use of the ETH1 port exclusively to the SIP gateway by explicitly prohibiting any connection to the OCE management services … OMC/Security/Network IP Services/Allow Management Services on ETH1 • Default value = enabled" (p312)
  summary: |
    矩阵：参数 "Allow Management Services on ETH1" 默认 enabled（ETH1 上 SIP trunk/OMC/WebDiag/OSC 全允许）；置 disabled 后仅 SIP trunk connection 保留，OMC/WebDiag/Debug tool OSC 全部 blocked。用途：把 ETH1 专用于 SIP 网关隔离管理面。
  conditions: 仅 OCE 平台
  tags: [rule, eth1, security]

- id: p42
  title: 端口关闭与系统加固清单
  type: checklist
  source_pages: p337-338
  source_chapter: Other system protection hardening / Security warning
  source_quote: |
    "Not used ports (21, 1721, 5061, 8729, 8888, 17069, 23400) are definitively closed" (p337)
    "Refer to the SECURITY chapter from The Expert Documentation • See technical communication reference TC1143" (p338)
  summary: |
    加固清单：OpenSSL v3（TLS 与通用密码学）；SIP DoS 韧性开发期测试；ARP 欺骗检测（历史事件 "ARP Spoofing Detected"）；移除 WS API 描述文件（wsdl）；Linux 内核安全补丁；未用端口 21/1721/5061/8729/8888/17069/23400 永久关闭。总纲：按 Expert Documentation 的 SECURITY 章 + TC1143（访问控制密码策略/用户密码管理策略/系统密码管理策略/网络安全远程接入/系统安全编程选项/noteworthy 汇总）执行。
  conditions: 注意 5061 在"未用端口"之列——启用 SIP TLS 前先核对该清单与版本行为（推断，原书未展开两者关系）
  tags: [checklist, hardening, security]

- id: p43
  title: LDAP 安全连接口径：LDAPS 636 / StartTLS 389 默认推荐 / Mandatory 默认
  type: metric
  source_pages: p332
  source_chapter: Secured LDAP connection
  source_quote: |
    "LDAPS mode: LDAP over SSL/TLS. Default port is 636 • StartTLS mode … Default port is 389 (recommended mode, activated by default) • Unsecured LDAP is also supported (note: in case of migration, previous configuration is retained)" (p332)
  summary: |
    口径：双模式支持——LDAPS（默认 636）与 StartTLS（默认 389，推荐且默认激活）；非安全 LDAP 也支持（迁移时保留原配置）；证书经 WebDiag Certificate→Trust Store 导入；校验两级：Mandatory（默认；无证书或坏证书立即断会话；导入证书时强制）与 Optional（坏证书忽略继续）；OMC Test 按钮在 Mandatory 下可检证书错误。
  conditions: 检查级别与模式配置在 OMC 的 LDAP 配置屏
  tags: [metric, ldap, security]

- id: p44
  title: 紧急号码表规格：预定义国家号码 / 上限 100 条
  type: metric
  source_pages: p335-336
  source_chapter: Emergency Numbers
  source_quote: |
    "New Emergency window with pre-defined country specific Emergency numbers … A maximum of 100 emergency number entries can be configured … Possibility to Add/Modify/Delete numbers in this table" (p336)
  summary: |
    规格：OMC/Emergency/Emergency Numbers 提供按国家预定义的紧急号码窗口；表上限 100 条；可增改删。实验环境的紧急号码（112/15/17/18）由 ITSP1 模拟器 urgence 用户模拟（p17-18），生产须按所在国号码表配置。
  conditions: 无 license 相关说明
  tags: [metric, emergency]

- id: p45
  title: 语音邮箱默认值矩阵（冷复位/新装 vs 迁移）
  type: rule
  source_pages: p381-382
  source_chapter: Local/Remote access for voicemail consultation
  source_quote: |
    "In case of migration, this field is disabled • After cold reset or in case of new installation, by default • 'Mailbox consultation from any phone' is enabled • 'Mailbox remote consultation' is disabled" (p382)
  summary: |
    默认值矩阵：本地开关 "Mailbox consultation from any phone"（OMC/Voice Processing/General parameters）——冷复位/新装默认启用（任意话机可查邮箱），禁用后仅本机可查；远程权 "Mailbox remote consultation"（订阅户 Features/Part 3）——冷复位/新装默认禁用，迁移场景该字段为禁用。组合出三种姿势：本机查（默认）/任意话机查/外部 DDI 查（需再给 VM 的 DDI+远程权）。
  conditions: 远程接入防盗打三提醒（p382）：勤改密码/不用简单数字/遵 TC1143
  tags: [rule, voicemail, defaults]

- id: p46
  title: Rainbow 目录同步技术约束：16 字符截断 / 非 Unicode 忽略 / 先清后写
  type: rule
  source_pages: p309-310
  source_chapter: Rainbow Business directory - End Customer Selfcare
  source_quote: |
    "FirstName, LastName are truncated to 16 Characters • Non Unicode name are ignored • Short numbers are allocated by the first synchronization and maintained by the next one." (p309)
    "Existing entries of OXO Collective Repertory are ERASED before sync" (p310)
  summary: |
    约束四条：①姓名字段截断到 16 字符；②非 Unicode 名字被忽略（不同步）；③短号由首次同步随机分配（非客户选择）、后续同步维持、不同 PBX 可不同；④每次同步先擦除 OXO 集体目录全部现有条目再写入（未连接的 OXO 不同步）。前提：Rainbow 公司已建 Business Directory 且至少一名 EC 管理员有管理权；OXO 编号计划须保留集体快速拨号段（条目数受其限制；"Max entries ="原书留白未给值）。
  conditions: 同步入口在 Rainbow 侧 sync 按钮；多 OXO 全部联动
  tags: [rule, rainbow, directory-sync]

- id: p47
  title: xBS 部署与 LED 时序口径
  type: metric
  source_pages: p515, p544
  source_chapter: xBS Management / IP-DECT xBS (How to)
  source_quote: |
    "LED RED • Step 1: Network initialisation, LED blinked 100ms On and 3000ms Off … LED ORANGE: • Step 4: Software download … LED Green: • Base station is alive, LED blinked 1s On/1s Off" (p544)
  summary: |
    部署四步：①接 PoE+启用 Automatic provisioning（xBS 自动出现在订阅户列表，别忘了勾 Auto Provision）；②DHCP 池（实验 192.168.1.10-39，OMC/Hardware and Limits/LAN-IP Configuration/DHCP）；③PARI（OMC/Dect/DECT-PWT ARI-GAP/ARI；ARI 11 位八进制、每客户唯一、eBuy 获取、xBS 与 IBS 共用；实验值 110004360P0 实验口径）；④话机声明+GAP 注册。LED 时序：红=步骤 1 网络初始化（100ms 亮/3000ms 灭）→步骤 2 取 IP（100/400/100+3000）→步骤 3 配置文件（(100/400/100)×2+100+3000）；橙=步骤 4 软件下载→步骤 5 呼叫服务器链路→步骤 6 基站配置；绿=就绪（1s 亮/1s 灭）。
  conditions: OMC 默认参数适合简单部署；复杂拓扑联系 TSS（p517）
  tags: [metric, ip-dect, deployment, led]

- id: p48
  title: Noteworthy 修改两例的取值口径：Auto_Reset 五字节 / 铃音节奏 <4 秒
  type: metric
  source_pages: p577, p580-581
  source_chapter: Noteworthy addresses modification
  source_quote: |
    "Byte number: 5 • 1st byte: activation/deactivation • 2nd byte: day • 3rd byte: hour • 4th byte: minutes • 5th byte: not used" (p577)
    "In ringing timer, note the hexadecimal address … Example: '0242D978' This value depends on the software version of the OXO! … The period of the ringing must be under 4 seconds." (p581)
  summary: |
    口径：Auto_Reset（Debug Labels）5 字节=启停（00/01）/日（00 周日…06 周六、07 每天）/时/分（十六进制，如周五 3:30="01 05 03 1E"）/保留；铃音节奏修改要先在 Other Labels 的 Ringing 记下基址（随软件版本变化！）+TC 附录 B 偏移（内部 UA 铃=9AH）求和得 Numeric 地址，长度 14 读出后写入新节奏（响 2s=C8、静 1s=64），warm reset 生效；节奏周期必须 <4 秒。清单以 TC1398 为准；cold reset 后 noteworthy 全部回默认。
  conditions: 写错地址可致系统恶化（p575）——改前备份、改后测试
  tags: [metric, noteworthy, tuning]

- id: p49
  title: LoLa 迁移数据边界：话机数据 LoLa 管，话机配置与语音提示 OMC 管
  type: rule
  source_pages: p583, p589
  source_chapter: LoLa
  source_quote: |
    "Backup and Restore the customer's data • Phones data: Voice mail messages, NMC Tickets • The phones configuration and the voice prompts must be saved by OMC" (p583)
    "Do a OMC Backup … Wait for the end of the phone data backup … Do the OMC restoration" (p589)
  summary: |
    分工规则：LoLa 负责呼叫处理软件+VoIP/ACD 应用包+主/CTI license 的完整加载，以及话机数据（语音留言、NMC 工单）的备份恢复；话机配置与语音提示必须由 OMC 单独保存并在迁移后恢复。Mono CPU 迁移顺序：OMC Backup→旧 CPU 进 LoLa 模式备份话机数据→（必要时硬件迁移）→新 CPU 下载恢复→常规重启→OMC 恢复。
  conditions: 版本建议查最新 TC；应用/板兼容查 OXO Connect Cross compatibility（MyPortal）
  tags: [rule, lola, migration]

- id: p50
  title: 培训结束清理清单（防脏数据带入生产）
  type: checklist
  source_pages: p593
  source_chapter: ACTIONS TO PERFORM AT THE END OF A TRAINING
  source_quote: |
    "Erase the MLAA voice guides if used • Clear ACD voice guides if used • Return to ACD / SCR factory settings if used • OXO Cold Reset with the following settings: User data • System data • Network, installer passwords and management data" (p593)
  summary: |
    清单四项：①擦除 MLAA 语音指南（如用过）；②清 ACD 语音指南；③ACD/SCR 恢复出厂；④OXO 冷复位（覆盖用户数据、系统数据、网络/installer 密码与管理数据三档）。对生产的镜像价值：退役/转售设备时按同一清单净化。
  conditions: 冷复位不擦自签证书（p327），证书需另行处理
  tags: [checklist, cleanup, reset]
```

## 任务覆盖自检（task ↔ id 映射）

| task_id | 覆盖条目 |
|---|---|
| task-01 | p01 |
| task-02 | p02 |
| task-03 | p03、p04、p05、p06 |
| task-04 | p07、p08 |
| task-05 | p09 |
| task-06 | p10、p11 |
| task-07 | p12 |
| task-08 | p13 |
| task-09 | p14、p15 |
| task-10 | p06（判定复用） |
| task-11 | p16 |
| task-12 | p17 |
| task-13 | p05、p18 |
| task-14 | p19 |
| task-15 | p20、p21 |
| task-16 | p22 |
| task-17 | p23 |
| task-18 | p24 |
| task-19 | p46 |
| task-20 | p25、p26、p41、p42、p43、p44 |
| task-21 | p37、p38 |
| task-22 | p40 |
| task-23 | p39 |
| task-24 | p26、p27、p45 |
| task-25 | p28、p29 |
| task-26 | p30 |
| task-27 | p31 |
| task-28 | p32、p33 |
| task-29 | p34、p35、p36、p47 |
| task-30 | p48 |
| task-31 | p49 |

自检结论：31 个任务全部有 principle 层覆盖（task-10 借用 p06 判定口径）；数值口径 22 条、规则 20 条、清单 4 条、公式 1 条，共 50 条（清单/规则/公式计数有少量交叉归类）。
