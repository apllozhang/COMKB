# 框架/流程/结构候选 — OXO Connect Advanced (OXOCXTE301EN Ed18)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、系统结构。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——实验环境地基 → 公网外联 → 三大能力域 → 云/安全/DECT 进阶 → 维护收尾
  type: flow
  source_pages: p3-601
  source_chapter: 全书目录结构
  source_quote: |
    "TRAINING LAB ENVIRONMENT … SIP CARRIER SIMULATOR … OMC Installation How to …
    Public SIP Gateway How to … Hotel solution overview … Cloud Connect …
    Security of the system … DIGITAL CERTIFICATES … IP DECT Solution … LoLa" (p3-601 章节封面)
  summary: |
    课程十段推进：①实验环境（RLAB POD + ITSP1 模拟器）；②OMC 安装与 IP 规划两连发实验；③公网 SIP 网关九 tab 实验；④酒店与计费垂直方案（含 Office Link Driver、账号码/内部替代两个实验）；⑤终端生态（AudioHub/8088/SIP 话机/PIMphony/Multiset/站群监督，配 Zoiper 等实验）；⑥呼叫处理增强（Hot Desking、ARS、私网 SIP、Internal ARS、多实体、语音邮箱、AA、MLAA、SCR、游牧/远程替代，几乎每章配实验）；⑦Cloud Connect 云管理；⑧安全与证书（DTLS、TLS/SRTP）；⑨DECT 移动（硬件、标准、注册、勘测、SUOTA）；⑩Webdiag/noteworthy/LoLa 维护与培训收尾。隐含主线：OMC/Webdiag 双工具 × 编号计划/中继组/ARS 三件套贯穿所有功能。
  conditions: Ed18/R6.3 口径；部分进阶内容（证书 4K、OCE-FE SIP PROXY）延伸自 R6.2 能力
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: RLAB 远程实验平台结构——POD 池 + 公共资源区双网段
  type: structure
  source_pages: p5-13
  source_chapter: TRAINING LAB ENVIRONMENT / Introduction & Training Platform
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data center." (p5)
    "POD 1 to n … Network 192.168.1.X … PODs common resources Subnet 0 10.20.30.x … NAS: softs, licenses … SIP simulator 12.0.0.2 … External DNS 10.20.30.250" (p6)
  summary: |
    平台两层：POD 1..n 相互独立、配置相同，每 POD 含一台 Windows 11 客户端虚机（OXOC_PC_CLIENT，IP 192.168.1.10/24，网关 192.168.1.254，DNS1 192.168.1.250，实验口径）和一台 OXO Connect Evolution（IP 192.168.1.246，实验口径）；公共资源区（Subnet 0，10.20.30.x）放 NAS（软件/许可）与 SIP 模拟器及外部 DNS（10.20.30.250）。客户端预装 4 个 MicroSIP（分机 100-103）+ 2 个模拟公网号码的 MicroSIP，IPDSP（分机 104）需自装；桌面 SOFTS OXO CONNECT 目录与 NAS 网络盘提供软件。
  conditions: 仅培训环境（RLAB），所有 IP 为实验口径；POD 间互不可见
  tags: [structure, lab, rlab, topology]

- id: f03
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则
  type: diagram
  source_pages: p16-22
  source_chapter: SIP CARRIER SIMULATOR
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 … ITSP1 Public gateway public.itsp1.com 10.20.30.50 … SIP domain: sip.itsp1.fr" (p17)
    "210P41000 Installation number • 41100 to 41199 base 100 DDI subscribers • 41000 base 9 DDI Operator group" (p21)
  summary: |
    模拟器两条腿：SIP 网关 gateway1.itsp1.com（PBX 注册账号 pbxP/alcatel，SIP 域 sip.itsp1.fr）与公网网关 public.itsp1.com（2 个 MicroSIP 模拟 Public/Urgence 用户，publicP@itsp1.fr / urgenceP@itsp1.fr，密码 public）。号码规则：PN=两位 POD 号；国内 33{1-5}1PN12345、移动 3361/3371PN12345、国际 4421PN12345、紧急 112/15/17/18；呼出 0110312345 由 PBX 变换为 +33110312345 送出（p19）。呼入本 PBX：安装号 3321PN41000，DDI 段 41100-41199（分机 100 即 3321PN41100），操作员组 base 9 的 41000；本 POD 环回（loop）呼叫也可行。OXO 侧网关参数：名 ITSP1G1，Target/Local domain/Realm=sip.itsp1.fr，Outbound Proxy=gateway1.itsp1.com，DNS A=192.168.1.250。
  conditions: 实验口径（RLAB 专用）；所有账号/号码/IP 均为教学约定值
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f04
  title: IPDSP 安装前置流程——IP 先行 + NTP 时间同步
  type: flow
  source_pages: p14
  source_chapter: INSTALLING THE IPDSP
  source_quote: |
    "Change the IP settings for the OXO Connect and the PC before installing the IPDSP … Otherwise, if there is a time difference between the PC and the OXO system, the IPDSP will not be able to start. An error message related to loading the lanpbx file will appear." (p14)
  summary: |
    四步：①OXO 改 IP 设置；②PC 改 IP 设置；③PC 日期时间设置里把 Set time automatically 关后再开（强制重新 NTP 同步）；④核对时间后安装 IPDSP。原理：IPDSP 走 HTTPS（数字证书），PC 与 OXO 时间差会直接导致证书校验失败。
  conditions: 实验环境专用流程；生产装机同样适用"时间先行"原则
  tags: [flow, ipdsp, ntp, certificate]

- id: f05
  title: 公网 SIP 网关配置九步顺序（含 tab 依赖关系）
  type: flow
  source_pages: p37-56
  source_chapter: Public SIP Gateway (How to)
  source_quote: |
    "Don't forget to now configure the Outbound Proxy: gateway1.itsp1.com in the Domain Proxy tab … The following setting can only be configured after filling in the DNS tab!" (p46-47)
    "The Gateway index must be filled in later when the SIP Gateway is created" (p44)
  summary: |
    固定顺序：①LAN IP/DNS 检查（改后复位）；②编号计划（Public Numbering Plan：DDI 41100-41199、话务台 41000；Installation Numbers：210P41000，必要时复制到 Restricted 公网编号计划）；③VoIP 接入（8 通道、Public network、主中继组 0，网关索引暂空）+中继组+Link-Cat 调整；④SIP 网关九 tab：General（Index 1/ITSP1G1/canonical/End of dialing used）→DNS（DNS A=192.168.1.250）→Domain Proxy（Target/Local domain/Realm=sip.itsp1.fr、Outbound Proxy=gateway1.itsp1.com，依赖 DNS tab 先填）→Registration（requested，registrar=sip.itsp1.fr）→Media（RTP Direct 验证，带宽最少 5 通话）→Identity（RFC 3325）→Protocol（默认）→Topology（ETH0）→Security（明文，默认）；⑤SIP 账号（pbxP/alcatel，Gateway Parameters Index=ITSP1G1）；⑥回 VoIP 外线回填网关索引；⑦验证：OMC/History and Anomalies/History Table 看 "SIP registration success"。
  conditions: 实验口径参数；顺序约束（DNS→Domain Proxy、网关后回填索引）为通用规律
  tags: [flow, sip-gateway, menu-path, ordering]

- id: f06
  title: SIP 中继排障三件套——注册历史表 / Webdiag 抓包 / Wireshark 分析
  type: flow
  source_pages: p54-56, p167-170
  source_chapter: Public SIP Gateway / Test & SIP Phones maintenance
  source_quote: |
    "OMC/History and Anomalies/History Table … Message displayed: SIP registration success" (p54)
    "In the menu at the left select TCP Dump traces … Choose SIP … And start the capture … This trace can be saved and transmitted to technical support for analysis" (p55-56)
  summary: |
    三层排障路径：①注册层：OMC/History and Anomalies/History Table 查 "SIP registration success"；②信令层：OMC/Tools/Webdiag（installer 登录）→TCP Dump traces 选 SIP 抓包，停止后自动生成文件；③分析层：PC/Wireshark 打开（实验机预装），可存档发技术支持，任何其它抓包软件亦可。SIP 话机维度补充：Webdiag→VoIP→VoIP information→IP/SIP/DSP→SIP sets 看列表，Traces→Network Capture 抓包，IP 设备远程 trace 支持 level all err/debug、ethlogs start/stop、getlogs 预定义按钮（p170）。
  conditions: Webdiag 登录 installer + installer 密码（实验口径 Alcatel1）
  tags: [flow, troubleshooting, webdiag, wireshark, sip]

- id: f07
  title: 酒店方案双路线架构——OHL/PMS 联动 vs 前台话机内置 Hotel 功能
  type: diagram
  source_pages: p57-68
  source_chapter: Hotel solution overview
  source_quote: |
    "OHL allows the synchronization with an Hotel application (PMS) … A PMS is an application used in hotels to handle reservations, check-in, check out, billing, and guest database" (p59)
    "Native Front Desk management on ALE DeskPhone, 4 simultaneous sessions … Room to room call barring … 300 sets (rooms + administrative telephone)" (p64)
  summary: |
    架构图（p61）围绕 OXO Connect：前台接待话机经 OHL（Office Link Driver，V24 或 IP）连 PC Windows 上的 PMS（须 AHL 兼容，清单见 DSPP/生态 PDF）；check-in 一步激活账单、DDI 分配、语音邮箱、语言、密码、客人姓名；周边挂 DECT/VoWLAN/模拟话机（Vtech 客房机）、语音邮箱、自动话务员、呼叫中心、PIMPhony、Rainbow、会议模块。无 OHL 路线：前台 ALE DeskPhone 内置 Hotel 功能键（check-in/out、预付、wake-up、DND、闭锁、DDI、账单打印、房态监控、V24/IP 实时计费），最多 4 并发会话、300 话机、房对房闭锁。定位 2-3 星酒店/民宿/度假村/学生公寓，Multiset 支持 hotel 模式。
  conditions: OHL 无软件 license；PMS 兼容性查 hospitality-ecosystem PDF（2025-11 版）
  tags: [diagram, hospitality, ohl, pms]

- id: f08
  title: 计费体系三通道——Hotel Metering / Call Accounting Time based / OLD 的 IP/V24 输出
  type: structure
  source_pages: p72-91
  source_chapter: Hotel Parameters & Metering over V24/IP
  source_quote: |
    "The OXO Connect provides real time metering on IP network • Metering tickets are transmitted in the XML data format … TicketCollector.xml for current tickets • TicketCollector_X.xml for archived tickets" (p78-80)
    "When activated, AOC Pulse based is deactivated (no mix configuration) • No license" (p73/83)
  summary: |
    结构：①Hotel Metering（OMC/Metering/Metering，Hotel Counting for Active Currency）：货币/VAT/预付/耗尽切断/蜂鸣阈值/3 级 2 阈/附加服务/40 字符小票脚注；②Call Accounting Time based（OMC-metering 新 tab）：对无 AOC 中继按时长×呼型（Int/Nat/Loc）出脉冲，基于安装号屏幕，与 OCD 共享取值，激活时 AOC 脉冲停用，免 license，适用于全部公网中继（ISDN/模拟/SIP）；③输出通道：IP（External Metering Activation IP，XML 小票经 Office Link Driver，Web service 供外部计费应用，TicketCollector.xml/归档 _X.xml 在 C:\Users\Public\Public Documents）或 V24（External Metering Activation V24 + 打印字段选择 + 传输参数，OMC/Metering/Metering Transmission Characteristics），全呼叫跟踪在 OMC/Users/Base stations list/Details/Counting 选 All Calls。
  conditions: 脉冲须由语音运营商传输，否则需外部时长计费器（p72）
  tags: [structure, metering, hotel, call-accounting, xml]

- id: f09
  title: SIP 呼叫处理架构——Registrar/B2BUA 与三种语音路径（DSP/RTP proxy/Direct RTP）
  type: diagram
  source_pages: p140-148
  source_chapter: SIP Phone and OXO Connect
  source_quote: |
    "The OXO Connect is a Registrar for its SIP client … The OXO Connect is a B2BUA Back-to-Back User Agent for the SIP calls" (p140-141)
    "A voice communication is processed in one of these 3 ways: • Through DSP channels … • RTP proxy: … packets are only routed by OXO … • Direct RTP: … the most optimal solution" (p148)
  summary: |
    注册面：SIP 终端连上即向 Registrar 注册（可带 Digest 401 认证→200 OK），位置服务器把用户 SIP 地址映射到 IP；OXO 是自己 SIP 客户端的 Registrar。呼叫面：OXO 作 B2BUA 中转 SIP 呼叫。媒体面三选一：①DSP 通道（压缩解压，非最优）；②RTP proxy（两腿同编解码同 framing 时仅路由不压缩，省 DSP、降 CPU，但路径仍经 OXO）；③Direct RTP（端点直连，最优）。编解码透传开关（话机侧 OMC\VoIP parameter\SIP Phone；中继侧 OMC\External lines\SIP\Media）：关=仅 OXO 编解码（G.711/G.723/G.729/G722/G722.2/OPUS），开=按终端能力全量音视频；无 Direct RTP 无透传时 Proxy RTP 固定端口（OMC\VoIP parameter\SIP Trunk）。SIP 话机不支持游牧模式（p147）。
  conditions: ALE IP 系列话机可 Direct RTP；TDM 系列话机耗 1 个 VoIP 资源
  tags: [diagram, architecture, sip, rtp-proxy, codec]

- id: f10
  title: PIMphony 四 profile 体系与安装配置流程
  type: structure
  source_pages: p119-138
  source_chapter: PIMphony
  source_quote: |
    "PIMphony Basic (for free) … PIMphony Pro (Basic +) … PIMphony Team (Pro +) … PIMphony Attendant (Team +) … PIMphony over IP Local or remote" (p121-122)
  summary: |
    profile 阶梯：Basic（免费，全功能电话+直观界面+集中日志+可编程键+点击外呼）→Pro（Basic+：屏幕弹窗互动、语音邮箱管理）→Team（Pro+：助理与监督者监控，工作组管理）→Attendant（Team+：单/多站点 PC 话务台）；PIMphony over IP 支持本地/远程。安装流程：OMC 侧先开在线更新（Central Services Global Info/PIMphony tab）与每用户预配置（Subscribers/Basestations List/Details/Serv.Cent/PIMphony tab 选 profile 与更新策略）→PC 装 PIMphony→配置向导（OXO IP→话机号+密码→profile 确认→拨号属性）→（软话机形态）OMC 建 PC Multimedia 终端（如 222）+Operator profile+音频向导。基于 license 检查；与任何设备关联（SIP 话机除外）。
  conditions: 实验注明 "PIMphony lab not feasible in Virtual Classroom"（p129）
  tags: [structure, pimphony, softphone, licensing]

- id: f11
  title: Hot Desking 组件关系——HDU/HDP/前缀/Webdiag 监督
  type: diagram
  source_pages: p173-183
  source_chapter: Hot Desking
  source_quote: |
    "It consists in allowing any Hot Desking User (HDU) to use any Hot Desking Position (HDP) in the company … If a HDU logs in to a HDP on which another HDU is already connected, the previous HDU will be first automatically logged out" (p174-175)
  summary: |
    关系图：HDU（人，OMC/Subscribers-Basestations List/Add 建 Hot Desking User）在任意 HDP（位子，空闲 Premium/ALE Deskphone 声明为 Hot Desking set）上以前缀 683 登录/682 注销（OMC/Numbering/Numbering Plans/Internal numbering plan 中 Hot Desking 函数），登录取回 VM/呼叫日志/IM/键配置/呼叫路由/multiset/移动性/语音邮箱等个人环境；监督双通道：Webdiag Services tab（看谁占哪个位子，Log out 按钮强制断开）与 OMC 订阅户详情互查。容量 200 HDP/200 HDU，HDU 前 2 免费后按 50 包；DECT 手柄可作 HDU multiset 副成员；适用 ALE DeskPhone、IP Desktop Softphone、模拟话机。
  conditions: 需 license；实验要求结束时停用功能
  tags: [diagram, hot-desking, mobility]

- id: f12
  title: Multiset 结构与呼叫呈现规则
  type: diagram
  source_pages: p184-192
  source_chapter: Multiset
  source_quote: |
    "The multiset feature is the association of two or three sets (wired or mobile) for the same user • One primary set and a maximum of two secondary sets … Usually composed of 2 sets … Called Twinset" (p185)
    "MLTSETRING=00 (long ringing) • MLTSETRING=01 (no ringing, default value) • MLTSETRING=02 (short ringing)" (p188)
  summary: |
    结构：1 主站+最多 2 副站共享主站目录号与服务级别；一话机只能属一个 multiset；副站可用自己目录号收话；创建在主站（OMC\Subscribers list\Subscriber details\Secondary sets 按钮 Add）。行为面：组来话（寻线组）全铃；经理/秘书组可含 multiset 但秘书不能是经理的副站（反之亦然）；忙时新呼叫等待音，空闲副站新呼叫按 MLTSETRING（OMC\System miscellaneous\Memory Read/Write\Other Labels）呈现——不铃（01 默认）/短铃（02）/长铃（00）。副站共享主站全部功能（VM/密码/闭锁/计费/动态路由等清单 p187）。
  conditions: 与 Rainbow 侧 Twinset（虚拟副站）同名不同物
  tags: [diagram, multiset, twinset]

- id: f13
  title: ARS 三表协作机制与号码变换四原则
  type: diagram
  source_pages: p193-205
  source_chapter: ARS management
  source_quote: |
    "Number Dialed → Numbering Plan → ARS Table → Trunk Groups Lists … Manage the ARS Prefix … Analyze the dialing number • Modify the dialing number • Select the trunk group list" (p195)
    "Principle: Addition / Absorption / Substitution / No modification (Transparency)" (p202)
  summary: |
    机制链：主叫拨号 → 内部编号计划（Main/Secondary Trunk Group 函数 base=ARS 触发，NMT Keep/Drop 决定号码保留）→ ARS 表（Automatic Routing Prefixes：Network Priv/Pub+前缀区间+Substitute 替换+TrGpList 列表索引+子线溢出；号码变换四原则：加前缀/吸收/替换/透明）→ 中继组列表（List ID+索引顺序+Char 显示字符+Access digits+Auth Code+Tone/Pause）→ 物理中继组。溢出两种挂法：列表内子行（同列表下一索引）或流量分担矩阵强制（传真场景）。时间维度另有 Day Groups/Hours/Providers-Destinations（p204，供 Internal ARS 与分时选路）。任何中继类型/呼叫类型/接入类型/拨号方式均适用，对用户透明。
  conditions: 详细字段格式以 OMC 屏幕为准（p196 表格）
  tags: [diagram, ars, routing, numbering]

- id: f14
  title: 多运营商分流示例图——GSM 网关/低价 VoIP/ISDN 备份三路
  type: diagram
  source_pages: p197-201
  source_chapter: ARS management / Multi-carrier configuration
  source_quote: |
    "Routing calls via mobile GSM gateway • Routing other calls via a VoIP provider (Lowcost) • ISDN backup overflow in case of saturation or for fax calls" (p197)
  summary: |
    拓扑：TrG400（GSM 网关走移动 06 前缀）、TrG402（ADSL 低价 VoIP 走其它呼叫）、TrG401（ISDN 备份）。配置：编号计划加 Main Trunk Group base=ARS；ARS 表两行（06→列表 1 het GSM；透明行→列表 2 het ADSL）；列表 1=[2:400 G, 3:401 I]、列表 2=[4:402 V, 3:401 I]——两列表共享子线索引 3 实现 ISDN 溢出；传真强制走 ISDN 用流量分担矩阵（Traffic sharing fax 行：400=-、401=+、402=-）。
  conditions: 示例口径（p198-201 表格数值）；生产按运营商前缀重新规划
  tags: [diagram, ars, multi-carrier, overflow]

- id: f15
  title: 私网 SIP 组网与双向溢出架构（两台 OXO 互联）
  type: diagram
  source_pages: p206-224
  source_chapter: Private SIP network with ARS (How to)
  source_quote: |
    "Calls may overflow on the public network in the event of saturation of the private network … Public calls between the 2 sites will be redirected to the private network as a priority" (p208)
  summary: |
    拓扑：OXO1（192.168.1.246）与 OXO2（192.168.2.246）经私网 SIP 网关互联（Domain Proxy 填对端 IP，Media RTP Direct+带宽最少 5 通话，Protocol 选 SIP Option 监督），各挂 T0 公网主中继组 0。配置八节：LAN IP→私网编号计划（Private Numbering Plan N100-N199 base 100）→私网 VoIP 接入+副中继组+链路类别→私网网关八 tab→关联网关到外线→ARS（内部编号计划 Secondary Trunk Group base ARS NMT=Keep Priv=Yes→ARS 表→列表指向 VoIP TG）→公网溢出接入（T0 入主组 0+公网编号计划+安装号）→双向溢出（私→公：ARS 表加子线+列表 index 2 指向主组 0；公→私优先强制：主组 base ARS+ARS 表加公转私行+公到公子线+透明行）。验证字符：私网通话显示 P、溢出公网显示 T（p223-224）。
  conditions: 实验 N=POD 号取值；注意不要与其它 lab 产生 IP 冲突（p208 Attention）
  tags: [diagram, private-sip, ars, overflow, multi-site]

- id: f16
  title: Internal ARS 决策链——一个 DDI 按日组/时段分流到不同内部目的地
  type: diagram
  source_pages: p225-231, p449
  source_chapter: Internal ARS
  source_quote: |
    "The DDI number 0388408571 is analyzed in the Public Numbering Plan • Function: Secondary Trunk Group • Base: ARS … The prefix 0388408571 is substituted by the prefix 101, 125 or 164 … Create a fictive Provider for each destination" (p228-230)
  summary: |
    决策链五级：①公网编号计划（DDI 段 Function=Secondary Trunk Group，Base=ARS，NMT=Keep，Priv=No）；②ARS 表（前缀匹配后按列表选 Substitute：替换成分机号 101/125/164 或寻线组消息；每替代建子线；替换前缀随后在内部编号计划分析落地）；③虚拟 Provider（每目的地建一个假 Provider，如 "Extension 101"）；④中继组列表（Index 选 Local 虚拟中继组+对应 Provider）；⑤Day Groups+Hours（日组=周一~五/周六日，时段表把组 1/2 映射到 Provider，兜底行给 None/消息）。效果：同一 DDI 工作日 8-12→101、12-13→102、13-18→103、其余→含营业时间话术的欢迎消息（实验把 MSG1 挂到寻线组 501）。
  conditions: 实验时段取值（p233 与 p449 表述有出入，见 counter-example）；Day group 分配可自定义
  tags: [diagram, internal-ars, time-routing, ddi]

- id: f17
  title: 多实体（Entity）架构——MoH 隔离、呼叫限制与话务员组公共
  type: diagram
  source_pages: p242-251
  source_chapter: Multiple entities/Pseudo multi-company
  source_quote: |
    "The system supports 4 Entities … Call restriction between user of different company … Attendant Group • Common for all entity • No call restriction" (p243-244)
    "Number of entries for individual greetings: from 15 to 200 • Number of preannouncement messages: from 8 to 20 • Message duration: from 128 to 320 seconds" (p248)
  summary: |
    架构：单系统最多 4 实体；用户默认实体 1（OMC\Subscribers Base stations List\Details 关联）；每实体独立 MoH（保持方实体决定播哪个，每段最长 10 分钟，OMC\System Miscellaneous\Messages & Music\Music on Hold 或 MMC 话务员会话录制）；实体间呼叫可禁（OMC\System Miscellaneous\Feature design\Part 1 标志 "Do not allow internal calls between multi-tenant entities"，连带影响立即/忙转、RSL 键、individual pickup、文本/语音邮箱；话务员组话机不受限）。伪多公司扩展：用流量分担链路类别配对（A 公司话机类别=其中继组类别，B 同理）+矩阵 1/1-16/16 直线+ARS 透明线（列表含两公司中继组，Char 1/2 显示确认占线归属），实现两家公司各走各的外线、账单分离、同一外拨前缀。
  conditions: 多实体 MoH license（最多 4 实体音乐-10 分钟）
  tags: [diagram, entity, multi-tenant, moh]

- id: f18
  title: Cloud Connect 架构——OXO 发起的双连接与两门户
  type: diagram
  source_pages: p262-285
  source_chapter: Cloud Connect
  source_quote: |
    "Both connections are initiated by the OXO Connect … No need to change the firewall rules … A VPN connection can be requested by a technician to establish a VPN tunnel between the OXO Connect and the Remote Service Center thanks to the permanent connection to the CCI" (p264)
  summary: |
    架构：客户 LAN 的 OXO 经 Access Gateway 出互联网到 CCI（Cloud Connect infrastructure）：永久 HTTPS 连接（心跳/信息上报）+按需 VPN 连接（技师请求后建立到远程服务中心的隧道）；全部由 OXO 主动发起，无需改防火墙规则。门户三件套（同一 Business Store 账号）：①Fleet Dashboard（fleet-dashboard.al-enterprise.com：舰队监控/SA 合同/Inventory/SW 更新，OXE 与 OXO 通用）；②OXO Connectivity（oxo-connectivity.al-enterprise.com，可 standalone：VPN 配置/Watchdog/OMC 复位/硬件设备许可清单/DSP 统计/默认密码检出/会话日志；系统定位用 CC-Prd-id（<R3.0）/CPU-id/客户参考 Fleet-Install）；③Business Store（store.al-enterprise.com）。软件更新链：Fleet Dashboard/OXO Connectivity→CC Update Service（XMPP）→OXO CC Update Agent，二进制经 ALE CC Download Server（HTTPS），ALE 技术支持可控。
  conditions: Fleet 数据库一天刷新一次（注册后 24h 才可见）
  tags: [diagram, cloud-connect, fleet, vpn]

- id: f19
  title: Cloud Connect 软件更新流程与状态指示灯
  type: flow
  source_pages: p269-273
  source_chapter: Software Update via Cloud Connect
  source_quote: |
    "[D..] if Download indicator is RED: the Current SW version running in the call server is Older that the 'Recommended Version'. → Update is recommended … [D..] → Download Indicator • [.S.] → Swap Indicator • [..P] → Upgrade in Progress" (p271)
  summary: |
    三步：①Connect：多台用 Fleet Dashboard、单台用 OXO Connectivity；②Check：指示灯 [D..]/[.S.]/[..P]，D 或 S 红色=建议动作（运行版本旧于推荐版本）；③Update：点更新按钮下载"最新 SW 版本"到呼叫服务器，按 swap 时间配置自动切换。Fleet Dashboard 批量路径：筛选产品→Software 菜单→SW Minor Update（太旧版本标红）；OXO Connectivity 单台路径：Switch/Download 状态（Recommended/OK/Has been requested）+动作按钮；两处均需用户权限 "advanced"。服务免费（license free），适用于 OXO Connect 与 OXO Connect Evolution。
  conditions: 单系统更新与批量更新权限要求一致（advanced）
  tags: [flow, sw-update, fleet-dashboard, indicators]

- id: f20
  title: 远程维护四种接入路径图
  type: diagram
  source_pages: p290-306
  source_chapter: Remote maintenance
  source_quote: |
    "Port forwarding must be configured at the Internet Access Device to forward incoming traffic received on the public port 443 to the port 50443 of the OXO Connect" (p301)
    "For remote access from Internet forwarded to the OXO Connect, the destination port on the OXO Connect must always be port 50443" (p303)
  summary: |
    路径一（电话网）：保留公网 DDI 作远程接入（无 DDI 时把系统 modem 接入放进默认话务员组并设 ReroutData=01），OMC Menu\Comm\Connect 选 modem+远端 DDI；传统默认是 modem PPP（ISDN TA 或模拟 modem）。路径二（本地 V24）：TC002_US.pdf 口径。路径三（互联网 HTTPS）：OMC 默认 HTTPS 443、50443 专用于互联网连接并施加访问控制；IAD 端口转发"公网任意端口→OXO 50443"（公共 443 被占时转发 {@IPPUBLIC, XXX}→{@IPOXO, 50443}）；OMC 直连填公网名/IP，经代理则 Options→proxy parameters（默认密码 OMCAdmin）。路径四（管理 VPN）：专用管理 IP 仅 OMC 可配（OMC/Hardware and Limits/LAN-IP Configuration，激活/停用须 warm reset），管理与客户网分离、每站点可用同一 IP；配套访问控制在 OMC/security/Network IP Services（WAN 管理服务/WAN 用户应用/LAN 用户应用三开关）。
  conditions: SIP-only 运营商站点无法走 modem，只能 IP 远程维护；远程访问仅在需要时启用（p299）
  tags: [diagram, remote-maintenance, port-forwarding, vpn]

- id: f21
  title: 系统安全体系结构——密码树/自动检查/审计/网络面收敛
  type: structure
  source_pages: p311-338
  source_chapter: Security of the system
  source_quote: |
    "It is mandatory for Installer to change all the default passwords in order to proceed further" (p315)
    "This period can be configured with the noteworthy address AutoPwdChk … Enabled by default, with default periodicity of 4 weeks" (p316)
  summary: |
    结构五块：①集中密码管理树 OMC→Security→Passwords（管理密码：一窗全显、Set 需当前会话密码、固定 8 位含大小写数字；SIP 话机管理密码：Expert 级可读/重置/设置；订阅户密码：默认密码列表+弱密码检出+批量重置；远程接入码 Remote Access Code）；②自动密码检查（AutoPwdChk 默认 4 周，01-52 周，00 禁用，warm reset 后必查；默认/弱密码生成 urgent alarm 可邮件通知）+XML 审计工具（TC2249）；③网络面：OMC\security\Network IP Services 三开关（WAN 管理服务：OMC from WAN/ETH1、Webdiag、OSC、PhDRelay；WAN 用户应用；LAN 用户应用）+每用户 WAN API Access 联动+ETH1 限制（Allow Management Services on ETH1 默认 enabled，disabled 时仅 SIP trunk 可用，OMC/WebDiag/OSC 全封）；④远程接入锁定（VMUMaxTry，锁时翻倍至 24h）与 Console 口重置 installer 密码开关（默认启用，禁用后只能现场 LoLa）；⑤加固清单（OpenSSL v3、SIP DoS 测试、ARP 欺骗检测事件、移除 WSDL、内核补丁、关闭未用端口 21/1721/5061/8729/8888/17069/23400）+紧急号码表（OMC/Emergency，上限 100 条）+LDAPS/StartTLS（636/389，证书校验 Mandatory 默认）。总纲指向 TC1143。
  conditions: 全部无 license；邮件通知的 SMTP TLS 认证暂不支持（p331）
  tags: [structure, security, passwords, hardening]

- id: f22
  title: 数字证书体系总表与 2K→4K 升级路径
  type: structure
  source_pages: p339-358
  source_chapter: DIGITAL CERTIFICATES
  source_quote: |
    "Server Certificate … HTTPS (OMC, WebDIAG APIs) • SIP trunk with SIP-TLS … 2048 (d) 4096 … Public Server certificate … Issuer External PKI … DTLS OXO certificate … Port 7780" (p346, p351-353)
    "Roll back to previous release after a migration to R6.2 … switch again to 2K certificates (Via WebDIAG) and then roll back." (p357)
  summary: |
    证书四类（WebDIAG 为主管理接口）：①Server Certificate（LAN 私有身份：HTTPS 443/30443 + SIP-TLS；OXO Root CA 自签默认或外部 PKI；2048 默认/4096 可配）；②Public Server certificate（WAN 公共身份：SIP-TLS + HTTPS 50443；仅外部 PKI，默认未定义；OCE 与 OCE FE；R6.0 起 OCE 公网 SIP trunk 用它）；③DTLS OXO certificate（NOE 话机 DTLS，端口 7780；DTLS OXO Root CA 不可配 4096 自签）；④其它：Generic OXO server certificate（ALE SIP 话机简易部署，端口 10443，自签 2048 不可配）、OXO HAN Server certificate（ALE Wi-Fi AP，端口 11443，R6.2 起 4096，迁移透明）。升级路径：自签 2 步（CA 再生成→服务器证书再生成，密钥长度两者一致）；外部 PKI 4 步（CA→CSR（PKCS#10）下载→外部 CA 签→导入安装）；Public Server 3 步；DTLS 自签 1 步/外部 3 步。重启仅 OCE 需要。R6.2 起 OpenSSL V3 + 4K 支持；迁移无缝保留证书；但 4K 证书存储格式不同——回滚前必须先经 WebDIAG 切回 2K（OMC 会报错警告）。证书获取三途：OMC\Import-Export\Export Server Certificate、http://OXO@IP/cert.html、首连安全弹窗接受。
  conditions: R6.2 引入 4K，主目标是 HTTPS 与 DTLS；<R6.2 外部签名仅 2K
  tags: [structure, certificate, pki, openssl]

- id: f23
  title: DTLS 原生加密双模式与端点清除三法
  type: flow
  source_pages: p359-364
  source_chapter: DTLS Encryption
  source_quote: |
    "Standard mode: Generic Certificate (recommended deployment in SMBs) … Fully zero touch … Expert Mode: Specific Certificate … Lock Endpoints to a designated Call server" (p361)
    "Method 1: Partial clear all devices … Method 2: Full Clear one Device … Method 3: use recovery token" (p363)
  summary: |
    部署：系统级 OMC/Security/DTLS Encryption、每用户 OMC/User/Details/IP-SIP parameters/DTLS Encryption；OMC 有状态总览，WebDiag/Certificates 管证书，话机显示钥匙图标。两模式：Generic（零接触，话机可在 OCE 间免清除移动）与 Specific（锁定端点到指定呼叫服务器，管理员自有证书）。移动/清除：同证书系统间透明（OXO↔OXO）；OXO↔OXE 必须清除——方法 1 部分清除（OMC 取消 DTLS 勾选后用 Reset Endpoints TrustList 清全部已连端点）或本地 MMI 恢复出厂（顺带解决端点管理密码丢失）；方法 2 完全清除（WebDiag 用 generic recovery token，任何 OCE 通用；specific 证书须经 ALE 技术支持按端点 MMI key 计算专用 token 导入，仅例外使用）；方法 3 即 recovery token 法。上限 300 DTLS 连接，免 license，仅 OCE。附带 IP-DECT 空口加密：默认禁用可 OMC 激活，xBS↔呼叫服务器 IP 接口无认证无加密，第三方话机不兼容时加密激活后无法运行。
  conditions: DTLS 保护信令（TLS 1.2），语音包仍明文（非 SRTP）；OCE 默认激活
  tags: [flow, dtls, encryption, endpoints]

- id: f24
  title: SIP 中继 TLS/SRTP 双实现——OCE 原生 vs OCE-FE SIP PROXY
  type: diagram
  source_pages: p365-378
  source_chapter: SIP trunks: TLS/SRTP
  source_quote: |
    "TLS Authentication model: Server Provided Certificate Authentication or Mutual Authentication • Cryptographic suites: AES Counter Mode [128 and HMAC SHA1 80] [256 and HMAC SHA1 80] [128 and HMAC SHA1 32] [256 and HMAC SHA1 32]" (p367)
    "WebRTC GW alone 20 calls max. NA … SIP PROXY alone NA 20 calls max. … WebRTC GW + SIP PROXY 20 calls max. 20 calls max." (p375)
  summary: |
    用例 1（OCE 原生）：SIP-TLS/SRTP 内建于 OCE，免 license；配置三处：网关 Security tab（启用特性+认证模型+密码套件）、Topology tab（SIP TLS 端口静态 NAT）、OMC/Voice Over IP/VoIP: Parameters→SIP Trunk（信令端口 5061）；包处理在 OCE GW 侧按每个 TLS trunk 分开做，Direct RTP 不可用；私网两 OCE 互联需 Static NAT，一端自动当 TLS Server 另一端当 Client；对端仅有 TLS client 能力时须停用双向认证变通；与 Rainbow 兼容（外部与集成 WebRTC GW 两种拓扑）。用例 2（OCE-FE SIP PROXY）：OCE Front-End 在 WebRTC 网关之外新增 SIP 代理角色，为 OCO 等平台转发 TLS/SRTP；OXO 侧网关 Security tab 激活 TLS PROXY+OMC/Voice Over IP/VoIP: Parameters 声明；OCE FE 经 WebDIAG Settings 配置（接口/DNS 类型 A/SRV/拓扑 OXOC IP+端口/静态 NAT/认证/套件），ALE CC 注册成功后可用；限制：认证/DNS/套件/静态 NAT 四项被全部 SIP TLS 网关共享、SIPS URI 不支持、ETH1 不用于 SIP 流量；容量 GW 与 PROXY 各 20 通话（共存时各自 20）。
  conditions: OCE-FE license 免费（仅需硬件）；OCE FE 不提供 PBX 能力
  tags: [diagram, tls, srtp, oce-fe, sip-trunk]

- id: f25
  title: 语音邮箱服务结构——端口分配/远程接入/ACC 两级控制/锁定
  type: structure
  source_pages: p379-393
  source_chapter: Mailbox customization (advanced parameters)
  source_quote: |
    "From 2 to 8 ports (depending on software keys) … By default, dynamic ports assignment according to traffic … By customizing, fixed ports assignment possible" (p380)
    "Access control code will get by default a system generated random 6 digits value … ACC is kept after warm reset and newly generated after cold reset" (p383)
  summary: |
    结构：语音服务器 2-8 端口服务语音邮箱/自动话务员/Audiotext，默认按流量动态分组、可固定分组。本地接入开关：OMC/Voice Processing/General parameters/"Mailbox consultation from any phone"（禁用后只能本机查邮箱）。远程接入三要素：VM 的 DDI 号（编号计划挂寻线组）+每用户 Features/Part 3 "Mailbox remote consultation"+认证（默认话机号+密码；配置 Remote Access Code 后升级为 ACC+话机号+密码的两级控制；ACC 默认随机 6 位、最长 16 位、warm 保留/cold 重生成）。锁定：连续失败次数 VMUMaxTry（本地远程共享计数），锁时 10→20 分钟翻倍至 1440 分钟；解锁五途（OMC 重置该设备密码/Webdiag Services/User Accounts/话机 Settings 改密/话务员会话/PIMphony Operator 监督）。个人助理（迷你 AA）：三目的地（内部/外部/移动）+转话务员，系统开关 noteworthy PerAssAlwd（默认 00 禁用），远程定制总开关按用户 Features/Part 2；远程定制菜单 1-7 中选项 7 转移受 DivRemCust（默认 00 禁用）。虚拟终端邮箱与寻线组邮箱：OMC 建邮箱+VM 键 LED 通知+外部通知呼叫。
  conditions: 迁移时 "Mailbox remote consultation" 字段为禁用；冷复位/新装默认 any phone 启用、remote 禁用
  tags: [structure, voicemail, acc, lockout]

- id: f26
  title: 自动话务员 AA 树结构与免费拨号机制
  type: diagram
  source_pages: p405-421
  source_chapter: Automated attendant
  source_quote: |
    "Two different tree structure: day (Normal) /night (Restricted) • Two menu levels by tree (100 nodes in the tree) • One main menu with 10 choices • 10 submenus with 10 choices … 4 voice guides possible languages" (p407)
    "AATypTrf • 02 = semi-supervised transfer (by default) • 00 = blind transfer" (p416)
  summary: |
    结构：两棵树（Opening Hours=Normal/ Closing Hours=Restricted，手动切或随系统时间范围自动切）、每树两级 100 节点、主菜单 9 种功能（免费拨号/总邮箱/转用户组/转话务员/信息消息/留言/转邮箱/释放/子菜单）、每菜单 1 可定制语音指南、4 语言；冷复位后 2 端口进默认话务员组 8 并默认接外呼。配置入口：OMC/Voice Processing/Automated attendant（Greetings tab 的 press star/语言选择问题；AA menu tab 的 AA Menu 按钮编辑树）；语音指南话机录（MMC Operator session/Expert/voice mail/auto-attendant）或 wave 导入（系统格式 ADPCM G726 4bits 8Khz Mono，OMC 可转 A-Law/µ-Law/PCM）。转接模式 noteworthy AATypTrf（02 半监督默认/00 盲转：忙 1 露营、不应答触发动态路由、忙 2 半监督时拒转重放菜单）。免费拨号：主菜单 0 键+问候期间 1-8 直拨分机（noteworthy AAGrDialng 默认 00 禁用/AAGrTransf 默认 01 启用 0/9 转话务员；Press '*' 与语言选择菜单期间不可用）。
  conditions: 树与语音指南定制需 license
  tags: [diagram, auto-attendant, tree, free-dialing]

- id: f27
  title: MLAA 多树话务员结构——ACD 引擎/树编辑器/语音文件组织
  type: structure
  source_pages: p427-442
  source_chapter: Multiple Automated Attendant (MLAA)
  source_quote: |
    "A maximum of 5 tree structures are manageable … Tree structure up to 3 levels … Up to 4 Language by tree … Number of dedicated MLAA ports (0 to16)" (p428, p431)
    "The total maximum size of all voice prompts must not exceed 12000 seconds (200 minutes)" (p440)
  summary: |
    结构：基于 ACD 引擎的集成应用，按 DID 和/或 CLI 把来话路由到树；树 3 级、每级 10 选、每级可挂时间范围（10 个）、每树最多 4 语言（独立于系统语言）；动作八种（子菜单/语音指南/免费拨号/免费拨号到 VMB/跳转/转分机组/转话务员/转 VMB）。配置全在 OMC 图形编辑器：MLAA Setup（专用端口 0-16，与 ACD 共享；MLAA 寻线组 DID；改动在 ACD 引擎复位后或 10 分钟无复位后生效）→MLAA Services（问候/语言选择/各级菜单/动作/时间范围/线路参数 DDI-CLI→树映射/通用参数：返回码 *、拨号结束码 #、位间 2 秒）→Tools\Transfer to the server（先 File\Save as，警告 line parameters 不随存档保存）。语音：每语言 100 消息（语言 1: 1001-1100.wav … 语言 4: 4001-4100.wav），默认每条 15 分钟上限（MLAA_MSG 可改），总量硬上限 12000 秒；格式 CCITT 8kHz 16bits mono A-Law/µ-Law。维护：warm reset（停/启 ACD 引擎或端口置零）与 cold reset（Tools\Reset to factory settings）。
  conditions: 树数按 license（1 或 5）
  tags: [structure, mlaa, acd, tree]

- id: f28
  title: Smart Call Routing 决策流程——线选择→目的地选择两段式
  type: diagram
  source_pages: p450-458
  source_chapter: Smart Call Routing
  source_quote: |
    "The routing mechanism is based on the following parameters • CLI Number, DDI Number, DTMF Client Code and the Opening and closing time … Rules available: 10 000" (p451, p454)
  summary: |
    流程：来话→线选择（规则表按 CLI 与 DDI 匹配：CLIn=CLIt 且 DIDn=DIDt；或任一模板为空；X 为通配符——CLI/DID 中隔离号码段、客户码中替换整码）→开/闭时间分析（Opened/Closed destination 两套）→目的地选择（客户码匹配则播 Voice Prompt 1-8 等 DTMF，输码# 校验；无码匹配走 Backup destination）。目的地类型：ACD 组（带/不带客户码）、MLAA 寻线组、本地号码/寻线组、外部号码/集体快速拨号。配置：OMC/ACD-SCR Services/Smart Call Routing（规则编辑器内嵌 ACD 呼叫路由表，增客户码/VP/Planning/开闭目的地五字段，CSV 导入导出兼容，10000 规则）；General Parameters（SCR 开闭计划最多 10 个，64 特殊日与 ACD 共用）；VP 与 ACD 语音消息共用（107-807.wav 八条）；日志从监督台导出（Web Diag）。license：SCR+1 个 Supervisor Console。
  conditions: 规划容量 X5000 匹配 × X10 计划（p451 示意图）
  tags: [diagram, scr, acd, call-routing]

- id: f29
  title: 语音移动方案全景与游牧/远程替代拓扑
  type: diagram
  source_pages: p463-480
  source_chapter: Voice Mobility / Mobility features and remote substitution
  source_quote: |
    "Nomadic Mode & Remote substitution … IP Desktop Softphone for Android … Available off-site anywhere the user can connect the customer IP network via a corporate VPN (works on Ethernet, WiFi, 3G/4G/5G cellular)" (p464)
    "Internal number: 104 … => Nomadic mode toward 021PN41102 … Remote Substitution DDI: 021PN41200 Welcome message MSG1 Access code 615243 … #100 to #199 →100 to 199 #9 → 9 Operator" (p473)
  summary: |
    全景：手机侧（游牧+远程替代；Rainbow 另见 RAINWTE012 培训；Android IP Desktop Softphone 经企业 VPN 远程用）；PC 侧（游牧+PIMphony）。游牧模式：游牧话机（多为手机）替代本地话机（本地可物理可虚拟）；启用链：用户 Cent.Serv 勾 Nomadic right（自动创建 Virtual Nomadic 虚拟终端）→VMU 远程定制选项 9→6 激活并设目的地（0021PN41102 # #）；CLI 规则：外部主叫发 CLI、内部有 DDI 发 DDI、否则发安装号；计费小票含游牧新信息。远程替代：公网编号计划给替代 DDI（41200）→Remote Access Code 设码（实验 615243）→用户 Features/Part 2 勾 Remote Substitution→内部呼叫经内部 ARS：内部编号计划 Secondary Trunk Group #100-#199 base ARS（NMT Keep、Priv Yes）+ARS 表 Priv #1 00-99+列表 Index=Local；流程：拨 DDI→接入码→分机→密码→#"分机"回环呼内部。
  conditions: 游牧与远程定制默认均禁用，按用户授权；实验用 IPDSP 当主话机
  tags: [diagram, nomadic, remote-substitution, mobility]

- id: f30
  title: DECT 标准与标识体系——FDMA/TDMA/TDD 帧结构 + 五种标识号
  type: diagram
  source_pages: p498-503
  source_chapter: Basis of the DECT standard
  source_quote: |
    "DECT is based on a multi carrier FDMA and TDMA with TDD • Up to 12 simultaneous calls per xBS • In case of IP DECT 11 calls … 24 Timeslots … 10 Carriers (Frequencies)" (p500)
    "PARI: Primary Access Right Identifier … RFPI: Radio Fixed Part Identifier, identification de la xBS composé du PARI et du RPN … IPUI: International Portable User Identity" (p502)
  summary: |
    标准：DECT（ETSI EN 300 175-1~-8）与 GAP（ETSI EN 300 444）由 ETSI 发布；频段欧洲 1880-1900/中国 1900-1920/拉美 1910-1930/北美 1920-1930 MHz；发射功率欧洲均值 10mW（峰值 250mW）、美国 4mW（100mW）；语音 ADPCM 32kbit/s（G726）；认证加密基于 4 位 AC 码。帧结构：10 载波×24 时隙（12 上+12 下 TDD），一通信=TS/F 对，每 xBS 12 并发（IP-DECT 11）。标识五件套：PARI（系统 DECT 安装 ID，31 位/8 位十六进制，OXO 全系统一个、xBS 与 IBS 共用）；RFPI（=PARI+RPN，xBS 标识）；PARK（话机内系统标识=PLI+PARI，13+1 校验位）；PLI（=31）；IPUI（话机国际身份，EPROM 硬写，14 位八进制）。话机每 ≥30 秒重扫无线环境建 RSSI 列表选最佳信道。
  conditions: 部分定义页为法文注释（原书素材残留）
  tags: [diagram, dect, standard, identifiers]

- id: f31
  title: DECT 拓扑与同步/切换机制——集群、站点、Relay xBS
  type: diagram
  source_pages: p504-517
  source_chapter: Roaming/Handover and topologies & xBS base stations Synchronization
  source_quote: |
    "Cluster = DECT area where all base stations are synchronized together … The cluster membership is imposed by the OXO Connect" (p506)
    "The xBS solution is using RELAY xBS to establish the media and the signaling flows … All signaling and media redirection within the IP-xBS DECT subsystem are managed by the IP-xBS subsystem itself (Connection Handover)" (p508)
  summary: |
    概念：Roaming（覆盖区内移动可被找到）与 Handover（通话中跨 cell 不断线，Extra cellular handover）。层级：站点（Site，地理位置，最多 20，站间不切换）→集群（Cluster，空口同步组，每站最多 8 个，集群成员由 OXO 强加）→xBS（空口同步树，自动模式下系统选主/备主，推荐 Automatic，Manual 仅专家）。部署四步（单站简单场景）：接 PoE+激活 Automatic provisioning（xBS 自动入订阅户列表）→DHCP→PARI（OMC/Dect/ARI，xBS 与 IBS 同 PARI）→声明话机+GAP 注册。切换机制：呼叫服务器只与初始基站（Relay xBS）保持信令媒体连接，切换由 IP-xBS 子系统自管（媒体在基站间重路由，远端无感）。限制：切换仅同集群内；话机可能锁定在时钟同步但信号较差的基站（xBS 与 TDM IBS 间总是如此）；覆盖区须良好分离；复杂拓扑（多楼>1km、分支办公）联系 TSS。xBS 网页管理（默认 admin/00!，可 OMC 改）。
  conditions: 容量：80 xBS/200 手柄/IP-DECT；60 IBS/TDM；每 xBS 11 并发
  tags: [diagram, dect, cluster, handover, sync]

- id: f32
  title: IP-DECT 部署与站点勘测流程（SSK）
  type: flow
  source_pages: p515-534
  source_chapter: xBS Management / Site survey overview
  source_quote: |
    "A site survey is mandatory before of a product offer or before installation in order to determine the number and position of Dect base stations" (p530)
    "measurement of the -72 dBm attenuation at the limit of the area … Zone of voice quality" (p533)
  summary: |
    部署流：硬件谱系选型（8378 IP-xBS 三型/8379 IBS 三型/8328 单蜂窝小分支）→单站自动部署四步（见 f31）→话机注册（向导 3 步或订阅户列表 2 步，GAP Reg 读 IPUI 后 Assign）→SUOTA 空中升级（8214/8234/8244/8254/8262/8262EX 经 8378/8379；自动/手动/关经 WebDIAG；并发 50 可配，下载 4-8 小时且低于话务优先级；swap 须充电座，多色 LED 显示进度可中途取下）。勘测流：报价或安装前必做；用 Site Survey Kit（行李箱+2 台勘测专用 xBS（固件与标准版不同）+8dBi 天线+充电宝+2 话机等；手册 8AL90874USAA）装载固件与国家频率（室内 PARK 31100170142241/室外 31100170232304，DNR1-9 AC1111-9999，实验口径）→电池供电摆位→话机 site survey 模式测衰减→-72 dBm 划语音质量区（-80 以下放弃）→通话测音质（最少两台话机注册，或拨 0+拨号键听连续拨号音）。
  conditions: 勘测专用 xBS 不运行标准固件，勿与生产混用
  tags: [flow, ip-dect, site-survey, suota]

- id: f33
  title: Webdiag 信息架构与三会话体系
  type: structure
  source_pages: p559-570
  source_chapter: WebDiag tool
  source_quote: |
    "Login: installer … Operator and Manufacturer sessions are also available" (p560)
    "Services • ACD (ACD Debug and log files) • Instant Messaging … Hot desking (supervise and log off phones sets and users) … Users Accounts (Supervise and unlock user accounts) • Cloud Connect status • Rainbow status" (p564)
  summary: |
    访问：OMC\Tools\Webdiag 或 https://OXO@IP/services/webapp/；会话三种：installer（全功能调试）、operator（每实体 MoH 上传、Hot Desking 监督注销、解锁用户账户）、manufacturer（技术支持用）。信息树七块：Start（系统启动/数据保存恢复/串口）；Information（一般信息/机柜拓扑/启动信息/Config Check（IP 网关 DNS NTP DNS SIP/SIP quarantine）/MSDB）；System（文件系统/系统文件与日志/网络信息/Dump System 摘要/内存/系统复位 warm-cold-出厂）；VoIP（Traces/VoIP information（IP/SIP/DSP 状态）/VoIP Debug（TCP Dump、实况 trace、代理日志、Telnet Control 授权 x 分钟访问 IP 话机））；DECT（xBS 集群同步 RPN/已注册手柄/基站统计）；Certificates（CA/服务器证书/Trust store）；Services（ACD/IM/Hot desking/UDA DB Sync/用户账户/Cloud Connect status/Rainbow status）。图标：Certificates 下载证书与 CA、MIBs 下载 OXO-MIB.zip（三个 MIB 供 SNMP 网管）、IDs（Eth Addr/ID/Serial/eLP license 标识/CC PRODUCT ID）。
  conditions: CPU 启动监视走 V24（115200 8 N 1，RJ45 config 口或 micro USB 控制台）
  tags: [structure, webdiag, troubleshooting]

- id: f34
  title: Noteworthy 地址体系与修改流程
  type: structure
  source_pages: p574-581
  source_chapter: Noteworthy addresses modification
  source_quote: |
    "Writing a value to the wrong address can result in a deterioration in the operation of the system … Noteworthy addresses return to their default values following a cold reset" (p575)
    "Find on MyPortal, the technical communication listing all the Noteworthy addresses • TC1398 OXO Connect Noteworthy addresses" (p578)
  summary: |
    体系：Memory Read/Write 配置服务器全局参数（labels/flags），四类内存区——Timer Labels（定时器）、Debug Labels（调试，如 Auto_Reset 自动重启：5 字节=启停/日/时/分/保留）、Other Labels（其它，如 MLTSETRING 铃型、PerAssAlwd、DivRemCust、AATypTrf、TmpMenLTim、NotiAppTim、AutoPwdChk、VMUMaxTry、MLAA_MSG、sipphone_sess_tim）、Numeric Addresses（十六进制数值，如铃音节奏地址+偏移算法）。流程：OMC/System miscellaneous/Memory Read/Write→选类型→字母列表选地址→Details→改字节值→Modify→Write。风险与边界：写错可致系统恶化；清单以 TC1398 为准；cold reset 全部回默认。Numeric 地址算法示例：Ringing 基址（随软件版本变化）+TC 附录 B 偏移（内部 UA 铃 9AH）→科学计算器求和→按长度 Read→写入新节奏字节→warm reset 生效（铃音周期必须 <4 秒）。
  conditions: 属"地下层"配置，修改前必须核对 TC1398 与对应 TC 附录
  tags: [structure, noteworthy, memory, tuning]

- id: f35
  title: LoLa 系统加载与迁移三流程
  type: flow
  source_pages: p582-591
  source_chapter: LoLa
  source_quote: |
    "Lola allows the complete loading of a PowerCPU or OCE • Loading of the call handling software • Loading of the application packages VoIP and ACD • Loading of the main and CTI software licenses" (p583)
    "LOLA mode: PoE ON with start button pushed until the LED is Fast Flashing Green" (p584)
  summary: |
    进入 LoLa 模式：OCE 按住电源键至双色 LED 快闪绿；PowerCPU/EE 用交叉网线连 PC+Dip switch（Jumper 1-2）后启动。向导三步：Step 1 定位交付文件（C:\Releasexxx）、语言、国家、license 文件（.csl CTI/.msl MAIN）、应用包（VoIP/ACD）；Step 2 选安装类型（Installation / Installation with customer's data erased / Migration Mono CPU（先备份客户数据到备份文件夹）/ Install-Restore（恢复先前 Mono/Multi CPU 迁移存档））；Step 3 按类型执行（无迁移：下载完→停机→Dip 回常规→重启；Mono 迁移：先 OMC Backup→旧 CPU 备份话机数据→（必要时硬件迁移）→新 CPU 下载恢复→重启→OMC 恢复）。边界：话机配置与语音提示须 OMC 保存；版本建议查最新 TC；应用与板兼容查 OXO Connect Cross compatibility（MyPortal）。
  conditions: 本教材将 LoLa 用途限于系统加载/迁移；培训结束清理（p593）也依赖 Cold Reset
  tags: [flow, lola, migration, reload]

- id: f36
  title: Rainbow 业务目录自助同步链路（EC Selfcare）
  type: flow
  source_pages: p307-310
  source_chapter: Rainbow Business directory - End Customer Selfcare
  source_quote: |
    "Shared contact phone numbers are pushed in the OXO Connect collective repertory for dial by name and caller identification" (p308)
    "A synchronization first erases all existing entries of the OCO/OCE system directory … Existing entries of OXO Collective Repertory are ERASED before sync" (p309-310)
  summary: |
    链路：EC 管理员在 Rainbow 建 Business Directory（共享外部联系人）→点 sync 按钮请求同步→公司下全部已连接 OXO 被同步（先清空集体目录再写入）→OXO 侧 Dial by Name 与主叫识别立即可用。技术细节：FirstName/LastName 截断 16 字符；非 Unicode 名忽略；短号首次同步随机分配、后续同步维持、不同 PBX 可不同；其余字段默认值。前提：Rainbow 公司已建目录且至少一名 EC 管理员有管理权；OXO 编号计划须保留集体快速拨号段（数量受编号计划限制）。价值：EC 自助、即时免费、减轻 BP 非盈利操作。
  conditions: 未连接 Rainbow 的 OXO 不同步；Max entries 原书留白未给值
  tags: [flow, rainbow, directory, selfcare]
```

## 任务覆盖自检（task ↔ id 映射）

| task_id | 覆盖条目 |
|---|---|
| task-01/02 | f04（含 IPDSP 前提）、f05 步骤①（f05 主覆盖 task-03） |
| task-03 | f05、f06 |
| task-04 | f07、f08（计费部分） |
| task-05 | f08 |
| task-06 | —（操作序列归 case c06；机制无独立 framework 条目） |
| task-07 | —（归 case c07） |
| task-08 | f10 |
| task-09/10 | f09（架构）、f06（排障） |
| task-11 | f11 |
| task-12 | f12 |
| task-13 | f13、f14、f15 |
| task-14 | f16 |
| task-15 | f17 |
| task-16/17 | f18、f19 |
| task-18 | f20 |
| task-19 | f36 |
| task-20 | f21 |
| task-21 | f22 |
| task-22 | f23 |
| task-23 | f24 |
| task-24 | f25 |
| task-25 | f26 |
| task-26 | f27 |
| task-27 | f28 |
| task-28 | f29 |
| task-29 | f30、f31、f32 |
| task-30 | f33、f34 |
| task-31 | f35 |

自检结论：31 个任务中 29 个有 framework 层覆盖；task-06/07 属纯操作序列，由 case.md 承载，无遗漏主线。
