# 反例/限制/边界/易错点候选 — OmniPCX Enterprise DECT Solutions (DECTXTE200EN Ed12)

> 提取器: counter-example-extractor（全量扫描，逐页扫 Warning/Note/Tips/Attention） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 推断性结论已标"（推断）"；实验环境给定值标注"实验口径"。

```yaml
- id: n01
  title: 加密在 Common Hardware 的 IBS 基站上不可用——Encryption 是 IP-xBS 专属
  type: warning
  source_pages: p37, p58, p227
  source_chapter: DECT security – Restrictions / IBS deployment
  source_quote: |
    "Encryption is not available for IBS Base Stations on Common Hardware architecture ... Identity
    Yes / Authentication Yes / Encryption Yes (IP-xBS only)" (p37)
    "Security level: - 'Identity' by default (no authentication) - 'Authentication' (Use of AC code
    during set registration) - Can't be Encryption (it's for IP-xBS)" (p227)
  summary: |
    安全级别的硬件边界：IBS（Common Hardware）最高只能到 Authentication；要 Encryption 必须上 IP-xBS
    （且 native 加密自 IP-xBS R200 起，p60）。客户提出"DECT 要加密"时，产品线即被锁定——这是售前选型
    的一票否决项，别等到实施阶段才发现 IBS 达不了标。
  conditions: 所有涉及加密合规（如医疗/政务）的 DECT 项目
  tags: [warning, security, ibs, ip-xbs]

- id: n02
  title: 混合模式（多 PARI）必须适配 PLI——原书全大写 WARNING
  type: warning
  source_pages: p227, p244-245, p265
  source_chapter: IBS deployment / Mixed DECT infrastructure
  source_quote: |
    "Warning IN CASE OF MIXED MODE, SO WITH MULTI PARI NUMBERS, THE PLI MUST BE ADAPTED." (p227)
    "The PLI value will be 30. With that all DECT users will be able to connect on all DECT base
    stations (xBS & TDM)." (p244)
  summary: |
    单 PARI 默认 PLI=31；IBS+xBS 混合即多 PARI，PLI 不降位则手机按全位比对、无法同时兼容两个 PARI，
    跨类基站漫游失败。实验口径取 30（两个 PARI 仅末位不同）；降位幅度取决于新旧 PARI 的差异位数。
    已注册手机的适配路径：PLI 缩位自动兼容（推断：对满足逻辑 AND 的 PARI 对）或 dectinston -update
    重推标识（见 c12）。
  conditions: 任何 IBS+xBS 混合站点；PLI 变更涉及全部已注册手机
  tags: [warning, pli, mixed-mode]

- id: n03
  title: 注册/注销各有两条通道，只能取一，且系统侧与手机侧操作必须近乎同时
  type: warning
  source_pages: p169, p175, p237
  source_chapter: Create and register / Uninstall and remove DECT handsets
  source_quote: |
    "Warning THE POINT 2.2 HAS TO BE DONE MORE OR LESS SIMULTANEOUSLY WITH POINT 2.1.1 OR 2.1.2 TO
    REGISTER A DECT ONLY ONE OF THE 2 METHODS MUST BE USED: POINT 2.1.1 OR 2.1.2" (p169)
    "Warning TO DEREGISTER A DECT ONLY ONE OF THE 2 METHODS MUST BE USED: POINT 1.1.1 OR 1.1.2" (p175)
  summary: |
    两个易错点：①webadmin 的 DECT Register/Deregister 按钮与 mtcl 的 dectinston/dectrm 是互斥双通道，
    混用会造成状态不一致；②注册是"系统开启等待 + 手机侧发起"的配对动作，系统侧点按钮/跑命令后必须
    立刻在手机上操作（注册窗口期内完成）。批量装机时建议单人顺序执行或两人配合，避免窗口超时。
  conditions: 所有手机注册/注销场景
  tags: [warning, registration, procedure]

- id: n04
  title: 8328 双小区主站判定——"先声明 Extension 者为主"，与 IP 地址无关
  type: warning
  source_pages: p288
  source_chapter: 8328 — Dual cells
  source_quote: |
    "Warning THE PRIMARY STATION WILL BE THE STATION WITH ALREADY AT LEAST ONE EXTENSION DECLARED.
    AS IT THE CASE HERE, AN EXTENSION IS ALREADY DECLARED ON THE ALREADY CONNECTED STATION, WITH ONE
    WILL BE THE PRIMARY AND THE STATION THAT WE WILL CONNECT NOW, WILL BE THE SECONDARY AND WILL
    RETRIEVE AUTOMATICALLY THE DATA FROM THE PRIMARY." (p288)
    "Only one extension can be declared on the station, it is enough to specify its role of primary,
    it is not required to register the handset and to perform the association extension-handset." (p288 Note)
  summary: |
    主站身份由"哪台先声明了 Extension"决定，不是 IP 大小、不是先上电。两台全新站同时入网时角色不确定
    （推断：取决于配置顺序）；要确立主站只需声明一个 Extension（无需注册手机、无需关联）。生产部署：
    先把主站配完（至少一个 Extension）再上副站，避免双主或角色反转。
  conditions: 8328 双小区部署与扩容
  tags: [warning, sip-dect, dual-cell]

- id: n05
  title: 外部 handover 验证的两个 Attention——通话必须先建在 IBS；切换后必须核验通话
  type: warning
  source_pages: p269-270
  source_chapter: External synchronization link – Test
  source_quote: |
    "Attention THE CALL MUST BE ESTABLISHED ON THE IBS BASE STATION" (p269)
    "Attention MOVE TO HAVE A HANDOVER WITH THE XBS BASE STATION AND CHECK THAT THE COMMUNICATION IS
    WELL ESTABLISHED" (p270)
  summary: |
    验证顺序硬约束：外部切换实验的方向是 IBS→xBS，起呼必须落在 IBS 时隙上（dectview com 看到编号通话）
    再移动切换；方向反了验证不成立。切换后必须在 xBS 侧核验通话仍在（RELAY/RADIO 字段），"通话没断"
    才是外部同步链路生效的证据。
  conditions: c13 类混合切换验证
  tags: [warning, handover, verification]

- id: n06
  title: 外部同步主备皆失——无孤岛生成、恢复后无自动重建（"future release"欠账）
  type: version-trap
  source_pages: p109
  source_chapter: External synchronization – Backup Sync Master
  source_quote: |
    "in case of failure of the master and the backup or of a key base • The other base will not work
    anymore, there is no island creation • When the failing bases are back there is no automatic
    recovery of the whole synchronization (will be improved in a future release)" (p109)
  summary: |
    版本陷阱：Master Sync 与 Backup Sync Master（或关键基站）同时失效时，其余基站全部停摆（不会分裂
    成孤岛各自为战）；故障恢复后整棵同步树不会自动重建——要人工干预。原书自注"将在未来版本改进"，说明
    R101.1 MD4 时代这是产品欠账。高可用站点要把"主备不同框、关键基站冗余"写入巡检，并把手动重建同步
    的预案写进运维手册。
  conditions: 使用外部同步的多 PARI/混合站点
  tags: [version-trap, synchronization, availability]

- id: n07
  title: Sync Master 禁止承载通信、Backup 必须看得见同一外部同步源
  type: limitation
  source_pages: p106, p109
  source_chapter: Multi PARI synchronization
  source_quote: |
    "The Sync master base station does not support any communications ... A backup Sync Master must
    also be setup and configured" (p106)
    "This Backup Sync Master needs to be placed near to the Sync Master, it must see the same
    External Sync BS" (p109)
  summary: |
    设计约束：外部同步时手工指定的 Sync Master 是纯同步站（不承载任何通话），容量规划时要把它从话务
    口径里扣除；Backup Sync Master 与主站必须物理邻近且能收到同一 External Sync BS 的信号——选址时
    两个站要按同一无线视角摆放。Backup 平时可补承主站不支持的话务，但主站故障后这部分话务即失；不可
    接受时需在主备旁再加专载话务的基站（p109）。
  conditions: 外部同步拓扑设计
  tags: [limitation, synchronization, capacity]

- id: n08
  title: 手机固件手动下载的前置参数——"Exclude from automatic FW update"须为 Yes（p182 原文表述易误读）
  type: misconception
  source_pages: p182, p188-189
  source_chapter: FIRMWARE UPGRADE OVER THE AIR – Management / Manual download
  source_quote: |
    "Note: If the parameter is set to «Yes», the upgrade of the DECT handset must be bone manually
    using the command downstat m <directory number>." (p182，原文"bone"为笔误，应为 done）
    "Note: the parameter «Exclude from automatic FW update for the DECT user must be set to «Yes»"
    (p188, p189)
  summary: |
    p182 的 Note 单看会误解成"自动下载开关=Yes 时反而要手动"。结合 p188/p189 的重复注释，真实语义是：
    用户级参数"Exclude from automatic FW update"设为 Yes（即排除自动、状态 X/M）后，升级必须经
    downstat m（菜单 4 或 downstat m n 命令）手动触发。全书此参数名在 p182 未写全，属表述缺陷；操作时
    以 p188 口径为准。（推断：p182 的 Note 描述的就是该 Exclude 参数。）
  conditions: 手机固件手动下发场景
  tags: [misconception, fwu, downstat-m]

- id: n09
  title: 手机 OTA 三类限制——FWU 协议不支持走 USB、访问节点不下载、主备切换下载停
  type: limitation
  source_pages: p181
  source_chapter: FIRMWARE UPGRADE OVER THE AIR – Restrictions
  source_quote: |
    "The handset firmware MUST support FWU protocol in order to allow an on-the-air upgrade • If not,
    the handsets have to be upgraded manually using USB link as described in the documentation •
    Handsets on visited node in case of roaming/campus are not downloaded" (p181)
    "When switching on a standby CPU all downloads are stopped. The Download Server resumes the
    downloads but not necessary in the same order than on the main CPU" (p181)
  summary: |
    三类坑：①老固件不满足 FWU 协议的手机空中升不动，只能 UST+USB 手动升（p252 也要求重注册前先升版本）；
    多节点/Campus 网络里漫游到访问节点的手机不会被下载——批量升级后排障要先查手机当前锁定节点；
    ②主备 CPU 切换会停止全部下载，恢复继续但顺序不保证——升级窗口避开 CPU 倒换维护动作。
  conditions: 手机固件批量升级项目
  tags: [limitation, fwu, ota]

- id: n10
  title: 自动重注册覆盖不了的手机——关机、出覆盖、漫游到访问节点
  type: limitation
  source_pages: p253, p255
  source_chapter: DECT handset automatic re-registration – Restrictions
  source_quote: |
    "Handset that are not under radio coverage of their installation node cannot be updated • Handsets
    off when the command is launched • Handsets connected to a visited node in case of OXE DECT
    networking" (p253)
  summary: |
    -update/-forceUpdate 只对"当前可达"的手机生效：关机的、不在安装节点覆盖内的、漫游到访问节点的都会
    失败（-update 失败时手机保留原参数不受影响，p251）。批量迁移的正确流程：先拉在线清单→跑批量→查
    ReinstallNOKHandsetsList.txt→对失败清单换时间重跑或现场手工处理。
  conditions: PARI/PLI 变更迁移项目
  tags: [limitation, re-registration]

- id: n11
  title: -forceUpdate 顺序铁律——先推新标识、后改系统 PARI，且改完失败机只能手工
  type: version-trap
  source_pages: p255
  source_chapter: DECT handset automatic re-registration – forceUpdate
  source_quote: |
    "For an installation where PARI needs to be changed, automatic re-registration must be done before
    changing the system PARI. The handsets must be still reachable while launching the procedure. •
    the handsets are no longer able to communicate with the system, as soon as they receive their new
    configuration • The system configuration must be changed only once the maximum of handsets have
    been registered. • Handsets for whom the procedure has failed will need manual reinstallation" (p255)
  summary: |
    顺序错误不可逆：手机一旦收到新 PARI 就与旧系统断联——若先改了系统 PARI 再想推送，推送通道已不存在，
    全部手机沦为手工重装。执行日顺序：确认手机可达 → -forceUpdate 推新 PARI/PLI → 核对成功清单达到
    预期 → 才改系统 PARI 配置。失败机（NOK 清单）在系统改完后只能现场手工注册。
  conditions: PARI 彻底变更（非相近 PARI）场景
  tags: [version-trap, re-registration, forceupdate]

- id: n12
  title: SIP-DECT 多站点断链即全断，且无 SIP 备份机制
  type: limitation
  source_pages: p274
  source_chapter: 8328 Topology – Multi-site architecture
  source_quote: |
    "If the IP link is broken between the 2 sites, communications are no longer possible with DECT
    users (neither with each other, nor with non-DECT OXE users) • No SIP backup mechanism (via PCS or
    local SIP gateway)" (p274)
  summary: |
    "低成本"的代价：SIP-DECT 基站依赖到 OXE 的 IP 链路，WAN 断则该站 DECT 用户对外、对内全断；书内明示
    无 SIP 备份机制（无 PCS/本地网关兜底）。与 IP-xBS（经 OXE 的 survivability 拓扑，p60）对比后更明显。
    分支办公选 8328 前必须向客户挑明这个可用性边界。
  conditions: 8328 分支办公场景
  tags: [limitation, sip-dect, availability]

- id: n13
  title: SIP-DECT 区与区之间无 handover/roaming——仅双小区例外；PARI/PLI 语义不适用
  type: limitation
  source_pages: p7, p275
  source_chapter: SIP-DECT footnote / Topology
  source_quote: |
    "(*) Since the SIP-DECT configuration in OXE is based on SIP users, the following explanations
    (PARI, PLI, etc.) do not necessarily apply to this type of infrastructure." (p7)
    "No roaming, between 2 DECT areas • No handover between 2 DECT areas ... Except of course in case
    of bi-cellular deployment (as in 'Area 1' in the above drawing)" (p275)
  summary: |
    两个边界：①概念边界——SIP-DECT 走 SIP 用户语义，全书主体讲的 PARI/PLI/RPN 体系对它不适用（多台
    8328 的 PARI 由系统自动分配），用 IP-xBS 的经验套 8328 会踩空；②覆盖边界——多台 8328 各自成区，
    区间没有切换与漫游（靠频率/时隙 agility 保证近距离共存），要区内切换只能双小区（bi-cell）部署。
    大面积覆盖不要用 8328 堆叠，应上 IP-xBS。
  conditions: 8328 选型与多站部署
  tags: [limitation, sip-dect, handover]

- id: n14
  title: SIP-DECT 硬边界——仅欧洲频段、仅 8214 手机、电话本与 OXE 不集成
  type: limitation
  source_pages: p272-273
  source_chapter: 8328 SIP-DECT Single Base Station
  source_quote: |
    "Only European DECT frequencies are supported (not US ones) ... 8214 DECT handsets only, declared
    as SIP extension" (p272)
    "Company phone book can be: Embedded in the base station, as a 'csv' or 'xml' file • Accessible
    via an external LDAP server • No integration with OXE phone book" (p273)
  summary: |
    三个硬边界：①频段仅欧洲（北美/拉美项目直接排除）；②终端仅 8214（GAP 机型，无 A-GAP 高级功能，
    多线/监督键等企业功能缺席）；③电话本体系独立——基站内置 csv/xml 或外接 LDAP，与 OXE 企业电话本
    不集成，改名换号要维护两处（推断）。选型时这三个边界要与客户 IT 提前对齐。
  conditions: 8328 选型评估
  tags: [limitation, sip-dect, phonebook]

- id: n15
  title: 版本封顶——IPv6 暂不适用、OXE R12.2 起步、native 加密需 IP-xBS R200
  type: version-trap
  source_pages: p59-60
  source_chapter: IP-xBS – Network characteristics / Compatibility
  source_quote: |
    "IPV4 (IPV6 hardware ready, not yet applicable)" (p59)
    "Compatible with OXE R12.2 minimum ... Support OXE native encryption (IP-xBS R200)" (p60)
  summary: |
    三个版本口径：①IPv6 仅硬件就绪、暂不可用——纯 IPv6 网络的项目 IP-xBS 不可用；②OXE 侧最低 R12.2，
    老版本升级 OXE 是前置项目；③"OXE native encryption"标注 IP-xBS R200——固件版本是加密能力的一部分，
    升级核查清单要包含基站固件。另有基站固件最低 v73b0003（p131）。
  conditions: 新建/扩容 DECT 项目的版本核查
  tags: [version-trap, ipv6, firmware]

- id: n16
  title: Debug 日志级别禁止常开
  type: warning
  source_pages: p160
  source_chapter: Collect IP-xBS logs – Syslog levels
  source_quote: |
    "Debug: Used for troubleshooting. Must not be enabled during normal operation." (p160)
  summary: |
    四级日志里的 Debug 是排障专用，正常运营必须回落 Normal operation（或 System Analyze）。排障结束
    忘改回是常见遗留问题——日志洪水会占用 syslog 存储并可能影响基站性能（影响程度书内未量化，推断）。
    排障工单闭环项要包含"日志级别还原"。
  conditions: xBS 日志排障后
  tags: [warning, syslog, operations]

- id: n17
  title: Survey mode 是调试模式——干扰正常功能、续航下降、不得给最终用户
  type: warning
  source_pages: p216
  source_chapter: Introduction to radio coverage – Survey mode notes
  source_quote: |
    "This feature allows the user to enable the site survey. Once enabled it will stay enabled until
    you disable it or restart the handset. This mode is intended for debugging purpose and shall not
    be used for normal end user operation (while active, this mode can interfere with other features
    of the phone). In this mode, battery autonomy is reduced." (p216)
  summary: |
    三个运营提醒：①开启后常驻（重启前不消失）——勘测完要显式 Off，否则发给用户的手机带着调试层；
    ②激活期间干扰手机其他功能；③续航明显缩短。另外激活后三个侧键被勘测接管（音量键失效，p216）——
    用户会报"手机坏了"。勘测机与交付机要分开管理。
  conditions: 覆盖勘测作业
  tags: [warning, survey-mode, handset]

- id: n18
  title: 换基站走自动注册会让 RPN 漂移——告警与地理定位随之失准
  type: limitation
  source_pages: p150
  source_chapter: Replace an out of service IP-xBS
  source_quote: |
    "When using the automatic registration, the first free RPN will be used and it can be different.
    This could be problematic if alarming and geo localization is used." (p150)
  summary: |
    自动注册按"首个空闲 RPN"分配，换站后 RPN 大概率变化；凡依赖 RPN 的功能（DECT 告警定位、位置区归属）
    全部失准。正确姿势：换站走手动注册（删旧 MAC@、录新 MAC@、保留位置名与 RPN，见 c03）。运维规程要把
    "换站=手动注册"写成硬规则。
  conditions: 基站硬件更换
  tags: [limitation, replacement, rpn]

- id: n19
  title: 混合区域无法外部同步时必须间隔 >1km
  type: limitation
  source_pages: p196
  source_chapter: Supported Topologies – Mixed without overlap
  source_quote: |
    "When it is not possible to have an external synchronization, the distance between the area must
    be > 1km." (p196)
  summary: |
    拓扑判定数字：IBS 区与 xBS 区如果建不了外部同步链路，两者物理间距必须大于 1km（避免空中互相干扰）。
    同院内既有 IBS 又要加 xBS 的项目，先确认外部同步可行性；不可行且间距不足的，要么换拓扑要么做物理
    隔离。反之可同步时按 c13 配置外部同步链路获得切换能力。
  conditions: 混合 xBS/IBS 站点规划
  tags: [limitation, topologies, mixed]

- id: n20
  title: WBM 改动可被 PBX 覆盖——排障配置可能"改了又变回去"
  type: warning
  source_pages: p77
  source_chapter: xBS base station web based management
  source_quote: |
    "Access authorization to web interface, as long as admin password is programmable by OXE
    management. Modifications of the settings of the base station through WBM can be then overwritten
    by the PBX." (p77)
  summary: |
    WBM 是"从属"管理面：OXE 管理可下授权、可改口令，且 PBX 下发会覆盖 WBM 所做修改。排障时在 WBM 里改
    的 IP/服务器参数可能在下次 OXE 下发时被冲掉——临时改动要记录，长期变更回 OXE 数据库做。同时 WBM
    非日常运维必需（p77 首句），生产上应收紧访问（口令非默认，见 p16 实验口径）。
  conditions: xBS WBM 使用与账号治理
  tags: [warning, wbm, configuration]

- id: n21
  title: 原书两处数值笔误/不一致——p44 IP 表、p281/p282 NTP 示例
  type: misconception
  source_pages: p44, p281-282
  source_chapter: SETTINGS 表 / 8328 basic configuration
  source_quote: |
    "OXE DECT_OXE_CSA csa (physical) csm (main) 192.16.8.1.1 192.16.8.1.3" (p44，对照 p42 拓扑图应为
    192.168.1.1 / 192.168.1.3)
    "NTP server: e.g 10.20.30.254" (p281) → "Time server Enter the NTP server address. Here, in R-lab
    context: 192.168.1.252" (p282)
  summary: |
    照抄书本数值前先交叉核对：①p44 实验环境表的 OXE 地址写成 192.16.8.1.x（点号错位），以 p42 拓扑图
    192.168.1.x 为准；②8328 的 NTP 示例 p281 给 10.20.30.254、p282 又按 R-lab 语境给 192.168.1.252，
    两个都是实验口径（Subnet 0 网关地址与 IT Server 地址），生产一律填客户 NTP。此条提醒：书内实验值
    不是规范值。
  conditions: 依据本书复现实验或引用数值时
  tags: [misconception, typo, lab]

- id: n22
  title: 注册开关全网只能开在一个节点——多节点网络忘配/配重的坑
  type: warning
  source_pages: p147, p247
  source_chapter: IP-xBS registration
  source_quote: |
    "Registration node 1 ... Can be set to True only in one node of a network. ... Notes Don't forget
    to specify the registration node." (p147)
  summary: |
    两个坑：①Registration enabled 在多节点网络只能一个节点为 True——两处都开会被系统拒绝（设计如此，
    防误收编）；②注册节点字段必须显式指定（原书 Notes 专门提醒"Don't forget"），漏配时自动注册不生效、
    新站挂网不入库。多节点 Campus 项目要把"注册节点=哪台"写进交付文档。
  conditions: 多节点网络的 xBS 自动注册
  tags: [warning, registration, multi-node]

- id: n23
  title: 8328 取地址必须放开 DHCP 的"非 ALE 设备"——默认配置取不到 IP
  type: warning
  source_pages: p280
  source_chapter: 8328 deployment – DHCP server configuration
  source_quote: |
    "Configuration 'DHCP Server' to be active ... Alcatel-Lucent terminals only NO (as the 8328 will
    not be recognized as an ALE device)" (p280)
  summary: |
    OXE 内部 DHCP 默认只服务 ALE 终端；8328 走标准 DHCP，不被识别为 ALE 设备——"Alcatel-Lucent terminals
    only"保持默认 Yes 时基站永远拿不到地址（表现为灯不闪绿）。开 NO 后还要注意整网安全：该 DHCP 池将对
    任意设备开放（推断，需配合地址池规划）。外部 DHCP 场景无此开关问题。
  conditions: 8328 部署的 DHCP 环节
  tags: [warning, sip-dect, dhcp]

- id: n24
  title: 8328 注册过程中的两个"假故障"——无 SIP 注册提示与通用 IPEI
  type: misconception
  source_pages: p285-286
  source_chapter: 8328 deployment – Register action / handset display
  source_quote: |
    "After a while, the 'home page' will indicate that there is no SIP registration. It is normal this
    step will be performed in the next step." (p285)
    "Consulting the table, the handset is now registered. IPEI number is no more the generic/default
    one (FFFFFFFFFF)" (p286)
  summary: |
    两个易误判的正常态：①手机空中注册到基站成功后，主页显示"无 SIP 注册"——这是正常中间态，SIP register
    由基站在扩展关联（下一步）后代做；不要在此环节反复重注册手机。②手机未注册时基站表里 IPEI 显示通用值
    FFFFFFFFFF——注册成功的判据恰恰是 IPEI 变成真实值。排障时按四步闭环（SIP 用户→手机注册→扩展声明→
    SIP register）逐段核对。
  conditions: 8328 手机注册排障
  tags: [misconception, sip-dect, registration]

- id: n25
  title: 双小区链路建立约 5 分钟，起不来要 reset the chain
  type: limitation
  source_pages: p291
  source_chapter: 8328 deployment – Dual cell consultation
  source_quote: |
    "The link between the 2 cells may take some time (+- 5 minutes) to be established." (p291 Note)
    "If, despite waiting, the link does not go up or does not fit properly, reset the chain on both
    stations" (p291 Tips)
  summary: |
    时间预期管理：副站入网后双小区链路要约 5 分钟才建立——别在 2 分钟时判定失败回滚。超过预期仍不起
    （或状态不正常）的处理是"在两台基站上 reset the chain"（书内 Tips，具体操作入口在 WBM，未展开
    步骤）。扩容窗口要为这条链路留出时间余量。
  conditions: 8328 双小区部署与验证
  tags: [limitation, sip-dect, dual-cell]

- id: n26
  title: Sync Cluster 仅特殊场景使用——拆簇即簇间失同步
  type: limitation
  source_pages: p102-103, p146
  source_chapter: Sync Cluster
  source_quote: |
    "Only for Special cases when the radio coverage is tricky" (p102)
    "It may be useful to group the DECT base stations so that some don't synchronize together, For
    example, when internal synchronization between some bases may not be stable because of a changing
    radio environment" (p103)
  summary: |
    拆簇是"两害相权"：默认全部基站在 Cluster 0（全同步）；当部分基站间同步不稳定（如电梯井分隔、动态
    无线环境）才把它们拆出独立簇。代价是簇与簇之间不同步——跨簇无法实现无线同步下的平滑切换（推断：
    handover 受限）。不要把拆簇当常规优化手段，能靠天线/选址解决的不拆簇。
  conditions: 站内空中同步覆盖不全的场景（p141 决策树分支）
  tags: [limitation, sync-cluster, radio]

- id: n27
  title: IBS 的 handover 要求全部基站挂同一 media gateway——跨网关无切换
  type: limitation
  source_pages: p224
  source_chapter: 8379 DECT IBS – Topologies (Common Hardware)
  source_quote: |
    "With the common hardware all the base stations must be connected on the same media gateway to
    allow the Handover over the site ... Clock sync for the DECT" (p224)
  summary: |
    Common Hardware 架构的切换域=单个 media gateway：IBS 基站分散在多个网关时跨网关没有 handover（时钟
    同步也依赖网关级时钟源）。多层楼、多机柜站点规划 IBS 时要先按"同一网关"约束划切换域，跨域只能
    roaming。这也是 IBS 向 IP-xBS 演进的动机之一（推断）。
  conditions: IBS 多网关站点规划
  tags: [limitation, ibs, handover]

- id: n28
  title: 生产化知识全部外置——工程规则/勘测/排障/初始配置四份文档
  type: out-of-scope
  source_pages: p138, p140-141, p212, p216, p146
  source_chapter: 各章文档指针
  source_quote: |
    "im_DECT_EngineeringRules_8AL90874USAA_8.pdf" (p212)
    "Check im_8378_DECT_IP-xBS_Troubleshooting_Guide_8AL91443ENAA_1_en-1.pdf document" (p138)
    "Technical documentation: oxe_p_101.1_sd_InitialConfig_8AL91047ENAD_2_en-1.pdf" (p146)
    "Refer to the document 'Getting started with the 8378 DECT IP-xBS solution on OXE' available on
    the BP Web Site" (p140)
    "'DECT and IP-DECT Engineering Rules and Site Survey Kit Manual (8AL90874USAA)'" (p216)
  summary: |
    本教材只承担"配置动作"：无线覆盖设计方法（传播、天线、勘测流程）、深度排障（PCAP 分析）、DHCP/初始
    配置细节、部署评估全部在这几份外置文档里。整理产出的一切 DECT 能力条目，Boundary 必须挂上对应文档
    指针；生产交付前按文档全文核查，不能以教材页数代替工程规则。
  conditions: 所有 DECT 交付与运维场景
  tags: [out-of-scope, documentation, boundary]
```

## 任务覆盖自检

| BOOK_OVERVIEW task | 对应 counter-example 条目 |
|---|---|
| task-01 | n01（安全边界） |
| task-02 | n12, n13, n14, n19（选型边界） |
| task-03 | n21（实验数值笔误） |
| task-04 | n15, n20, n22 |
| task-05 | n18 |
| task-06 | n16 |
| task-07 | n03 |
| task-08 | n03 |
| task-09 | 无（downstat x 流程本身限制少；固件版本坑落 n15） |
| task-10 | n08, n09 |
| task-11 | 无专用反例（跨站无 handover 语义见 f11/p87-88，属正向规则） |
| task-12 | n17 |
| task-13 | n01, n27 |
| task-14 | n02, n19 |
| task-15 | n10, n11 |
| task-16 | n05, n06, n07 |
| task-17 | n23, n24, n12, n13, n14 |
| task-18 | n04, n25 |
| task-19 | n20 |
| task-20 | n01 |

20 项中 18 项有对应；task-09、task-11 无独立反例（其风险已并入 n15 与正向结构条目），属预期分工。
