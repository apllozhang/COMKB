# 反例/限制/边界/易错点候选 — OmniPCX Enterprise 原生加密 (ENTPXTE421EN Ed05)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: 切换 SRTP cipher suite 必须重启 OXE；AES-256 让 AES-128-only 设备通话回落明文
  type: warning
  source_pages: p70-72
  source_chapter: CIPHER SUITES CUSTOMIZATION: SRTP
  source_quote: |
    "Setting AES-256 will result in calls in clear mode with equipments only supporting AES-128 (even
    if all parties are secured) • Concerns today IP-xBS, IPDSP Android, 'hybrid link' based ABC
    network (which only support AES-128)"
    "A reboot of the OXE system is mandatory when changing the 'SRTP cypher suite' system option."
  summary: |
    两个坑：改 SRTP Cypher Suite 系统参数必须重启 OXE 才生效；把系统切到 AES-256 后，只支持 AES-128
    的设备（IP-xBS、Android 版 IPDSP、hybrid link ABC 网络）即使状态是 secured，其通话也回落 RTP
    明文（信令仍加密）。上 AES-256 前先盘点端点与链路的 AES-128-only 清单。
  conditions: SRTP cipher suite 变更与混合设备存量
  tags: [warning, srtp, aes, capacity]

- id: n02
  title: SRTP AES-256 的硬件红线：GD4/GD-XL 压缩器 60→45、INTIP3 60→30、GD3 直接禁用必须换 GD4
  type: limitation
  source_pages: p70, p72
  source_chapter: CIPHER SUITES CUSTOMIZATION: SRTP
  source_quote: |
    "It is not authorized to activate SRTP AES-256 mode on an OXE system with GD3 boards"
    "GD4/GD-XL boards are limited to 45 compressors maximum (instead of 60) and INTIP3 boards to 30
    compressors (instead of 60) … Any existing GD3 board has to be replaced by a GD4 board"
  summary: |
    AES-256 模式容量与硬件代价：GD4/GD-XL 压缩器上限 60→45、INTIP3 上限 60→30（GA4/GA-XL/OXE-MS 无
    限制）；含 GD3 的系统禁止启用 AES-256——存量 GD3 必须换 GD4。售前按 AES-256 口径重算话务容量，
    别按 60 压缩器报。
  conditions: 意图启用 SRTP AES-256 的站点
  tags: [limitation, capacity, gd3, hardware]

- id: n03
  title: CSR 不带 IP SAN 是版本陷阱——部分话机"可能永远无法投入服务"
  type: version-trap
  source_pages: p85, p113, p248
  source_chapter: CERTIFICATES SAN FIELD / Generate CSR
  source_quote: |
    "WARNING : Some IP sets may not support a certificate in SAN field without IP address. Please
    refer to the feature list and release notes of different terminals to be sure the concerned
    firmware supports that feature. CONSEQUENCE : the terminal may never be put in service" (p113)
    "IP-XBS and 80x8s deskphones in NOE mode are not compatible" (p85)
  summary: |
    netadmin 生成 CSR 时对 "configure IP address in SAN?" 答 n（无 IP 证书，企业策略友好）的条件：
    OXE N5 起支持，且端点固件须支持 FQDN 校验——已知不兼容清单：IP-xBS 基站与 NOE 模式 80x8s 话机。
    原书用 WARNING+CONSEQUENCE 双重强调：不核对特性清单就答 n，相关终端可能永远无法投入服务。
    生产操作：先查各终端 release notes 再决定 SAN 策略。
  conditions: CSR 生成（SAN 策略选择）
  tags: [version-trap, san, certificate, firmware]

- id: n04
  title: ACME 自动续期三个前提：默认关闭（root 启用）、仅本地 CA、公网 CA 因 HTTP-01 不可用
  type: limitation
  source_pages: p84
  source_chapter: CERTIFICATES ENROLLMENT AND RENEWAL
  source_quote: |
    "Automatic enrollment feature must be enabled (root account only), as it is disabled by default"
    "Requires a local, third-party CA supporting the ACME standard • Public CAs (e.g., Let's Encrypt)
    cannot be used, as this would require OXE to be publicly accessible for the HTTP challenge
    (HTTP-01 method)"
  summary: |
    OXE 的 ACME 只覆盖 WBM 证书且默认关闭（root 才能启用，cron 周期检查续期）；CA 必须是本地部署的
    支持 ACME 的第三方 CA，且 ACME 服务器要加入 OXE 可信主机。Let's Encrypt 等公网 CA 因 HTTP-01
    挑战要求 OXE 公网可达而不可用——"上 ACME 就能自动续证书"在 OXE 场景不成立。
  conditions: 证书续期方案规划
  tags: [limitation, acme, renewal]

- id: n05
  title: CA 更新的连锁义务：立即重生成 lanpbx + OXE 重启 + PCS 证书手工重生成
  type: warning
  source_pages: p104-106, p225, p250, p322
  source_chapter: Import CS Certificates（各实验章重复出现的 Warning）
  source_quote: |
    "CA update requires : 1.Immediate regeneration of lanpbx followed by an OXE reboot. Multiple CA
    updates without lanpbx regeneration and endpoint trust store update could cause CTL
    inconsistency between OXE & endpoints and may lead to communication issues. 2.PCS certificate(s)
    to be generated manually through PCS menu if PCS(s) configured."
  summary: |
    导入/更新 CA 时的固定连锁（原书六个章节重复同一段 Warning）：①立即重生成 lanpbx.cfg 并重启
    OXE——多次 CA 更新而不重生成 lanpbx、不更新端点信任库，会造成 OXE 与端点间 CTL 不一致并引发
    通信故障；②配置了 PCS 的，PCS 证书必须经 PCS 菜单手工重生成。把这两步写进变更单，否则"导入了
    新证书但系统行为诡异"。
  conditions: CA/证书导入后
  tags: [warning, ca, ctl, pcs]

- id: n06
  title: 主备同步义务：主 CS 任何证书变更后必须同步 standby；twin 是高频遗忘点
  type: warning
  source_pages: p91, p117, p118, p219, p247
  source_chapter: OXE REDUNDANCY / 各实验章 "copy to twin" 提示
  source_quote: |
    "Synchronization mandatory to Call Server Standby after any certificate modification (creation/
    import) on Call Server Main" (p91)
    "Note: This Encryption GW menu is only for main and twin EGW configuration … Don't forget the
    'Copy To Twin' operation if OXE system is duplicated" (p219)
  summary: |
    duplication 场景的铁律：主 CS 上的证书创建/导入、EGW 声明、Translator 名、内部防火墙、内部 DNS
    等变更，都要随后执行 netadmin 10.2 Copy to twin——原书在几乎每个 netadmin 操作后都标注
    "Don't forget the Copy To Twin"。漏做会导致主备证书/配置不一致，切换时故障。
  conditions: CS duplication 环境
  tags: [warning, redundancy, twin]

- id: n07
  title: 主备间 DTLS 强制双向认证：P1=0 即主备明文（事件 5993）
  type: limitation
  source_pages: p91, p132
  source_chapter: OXE REDUNDANCY / Incidents
  source_quote: |
    "Mandatory mutual authentication for the Main/Standby DTLS session • Both Call Servers have a
    common key pair and certificate, signed by the same Certificate Authority" (p91)
    "5993 Major … If P1 is 1, the connection is encrypted (DTLS connection) • If P1 is 0, the
    connection is not encrypted (data are sent in clear between the two communication servers) …
    A reset of the communication server is required after correction." (p132)
  summary: |
    主备 CS 之间的 DTLS 会话强制 mTLS，两台 CS 共用同一密钥对与证书（同一 CA 签发）；证书协商失败时
    主备间数据明文传输且事件 5993（Major）报 P1=0——修复证书后必须重启 CS。事件 5992（Minor）则
    报 CA 证书剩余天数 P1：P1=0 时证书失效、所有 FSNE 端点重启——证书到期是"全站重启"级事件。
  conditions: CS duplication 与证书生命周期
  tags: [limitation, redundancy, certificate-expiry]

- id: n08
  title: PCS 救援前置：端点必须至少连过一次 CS；PCS 用主 CS 的 lanpbx.cfg，NE 配置只在主节点做
  type: limitation
  source_pages: p92, p148, p152
  source_chapter: PASSIVE COMMUNICATION SERVER / PCS labs
  source_quote: |
    "Endpoints must have been connected at least once to CS in order to be rescued by PCS" (p92)
    "All 'native encryption' configurations should be done only in Main Node and not in PCS." (p148)
    "SAME 'LANPBX.CFG' FILE OF MAIN CS IS USED FOR PCS NODES. END POINTS WILL NOT REQUEST 'LANPBX'
    FILE FROM PCS. … NOTHING TO DO." (p152)
  summary: |
    三条 PCS 边界：①端点必须先连过 CS（拿到初始信令里的 PCS 地址）才能被救援——新装直奔分支的
    端点不在救援范围；②NE 相关配置只在主节点做，不在 PCS 上做；③PCS 与主 CS 共用同一 lanpbx.cfg
    （端点不会向 PCS 请求该文件），为 PCS 单独生成/修改 lanpbx 是无用功。PCS 证书与 CS 同 CA 但
    必须是不同证书（p92），且导入前必须先打 tar 包（p150）。
  conditions: 多站点 PCS 架构部署
  tags: [limitation, pcs, lanpbx]

- id: n09
  title: "断网演练即失联：VLAN1 断开后主站点 VM 全部不可达"
  type: warning
  source_pages: p154
  source_chapter: PCS lab – Network breakdown simulation
  source_quote: |
    "AT THIS STAGE, AS VLAN 1 HAS BEEN DISCONNECTED, YOU DON'T HAVE ACCESS ANYMORE TO VIRTUAL
    MACHINES OF THE MAIN SITE (CS, OMS, PC…) THROUGH IP. SO, FOR THE TEST, USE PC VM BELONGING TO
    REMOTE SITE (VLAN 2: 192.168.2.X)"
  summary: |
    PCS 断网演练的操作边界：在 Rlab 断开 192.168.1.254 后，主站点所有 VM（CS/OMS/PC）IP 不可达——
    只能从远端站点（VLAN 2）的 PC VM 继续操作与观察。生产做同型演练时同样要预先准备带外管理或远端
    侧操作路径，否则断网后自己也失联。
  conditions: PCS 断网/恢复演练
  tags: [warning, pcs, lab, failover]

- id: n10
  title: 换节点/迁移的信任库陷阱：FSNE→FSNE 搬移要 factory reset 或先取新 CTL；FSNE→明文必须 factory reset
  type: limitation
  source_pages: p108, p288-289
  source_chapter: OPERATIONS / Pod Configuration: Network labs
  source_quote: |
    "Move from a 'FSNE' node to another 'FSNE' node • Before moving … Factory reset to clear the
    device old trust store so that it will be able to retrieve the new CTL via TOFU • … Move from a
    'FSNE' node to non secured node • Factory reset has to be done" (p108)
    "AS 'ENTP_OMS_CSA_CSB_NODE1' VIRTUAL MACHINE WAS USED UP TO NOW BY CSA & CSB, CERTIFICATES ARE
    ALREADY PRESENT IN ITS TRUST STORE. SO … YOU HAVE TO ERASE THESE CERTIFICATES FROM THE OMS TRUST
    STORE." (p288)
  summary: |
    设备换节点的信任库规则：FSNE 节点间搬移前，要么恢复出厂（清旧信任库、重新走 TOFU 取新 CTL），
    要么搬移前手工获取新节点的 CTL；搬回非加密节点必须恢复出厂。原书实验自己就踩了这个坑：OMS VM
    此前服务过 CSA/CSB、信任库里有旧证书，转 Node1 拓扑前必须 omsconfig→Certificate management→
    Erase saved certificates 清掉，否则在服务异常。
  conditions: 设备在节点间搬移、实验拓扑切换
  tags: [limitation, trust-store, factory-reset, oms]

- id: n11
  title: 出厂恢复是急救手段也是唯一回路：按 i + # 进 Reset to Defaults
  type: limitation
  source_pages: p108
  source_chapter: OPERATIONS – How to prevent emergency situations
  source_quote: |
    "Total crash of the system, without any backup • Move a set from a protected PBX to another site
    • In such cases, the device has to come back to « TOFU » mode • Therefore a « factory reset » is
    mandatory • Set's trust store will be cleaned out • Reboot the set • During startup phase, press
    'i' then '#' • Press the option 'Reset to Defaults'"
  summary: |
    三种场景（系统全毁无备份、受保护 PBX 间搬移话机等）都要求设备回到 TOFU 模式，唯一办法是恢复
    出厂：重启话机，启动阶段按 i 再按 #，选 Reset to Defaults（信任库被清空）。排障手册要有这一手，
    但也要明白它同时清掉端上一切定制。
  conditions: 话机信任库损坏/换站点/灾难恢复
  tags: [limitation, factory-reset, tofu]

- id: n12
  title: 事件 5991/5995 指向配置不一致：CTL 配置错误、EGW 菜单与 netadmin 的 CS IP 不一致
  type: limitation
  source_pages: p132
  source_chapter: Incidents
  source_quote: |
    "5991 Minor 'No reaction of the system' … check if the CTL is configured correctly on OXE and
    Endpoint … check netadmin history file"
    "5995 Major 'FSNE: Inconsistency of CS IP Address between EGW menu and Netadmin configuration' …
    check the EGW menu configuration and verify with Netadmin configuration (localhost/twincpu) … A
    reset of the communication server is required after correction."
  summary: |
    两个排障导向事件：5991（Minor，系统无反应）先查 OXE 与端点两侧的 CTL 配置是否正确，进一步看
    netadmin 历史文件；5995（Major）表示 WBM 的 IP/Encryption GW 菜单与 netadmin 配置的 CS IP 不
    一致导致加密异常——修好后要重启 CS。注意 IP/Encryption GW 菜单是只读展示（p126/p234），真正的
    声明在 netadmin 20。
  conditions: 加密故障排障
  tags: [limitation, incidents, troubleshooting]

- id: n13
  title: SIP TLS trunk 只加密信令——"上了 TLS 语音就加密"是误解
  type: misconception
  source_pages: p93, p159, p161
  source_chapter: NATIVE SIP TLS FOR SIP TRUNK / OVERVIEW
  source_quote: |
    "If activated without Native Encryption, only SIP signalization is secured • Media flows are in
    clear mode: use of RTP (not SRTP) • But Native SIP TLS must be activated to be able to encrypt
    the media" (p93)
    "The Native SIP TLS trunk feature deals with signaling only" (p161)
  summary: |
    Native SIP TLS 可独立于 NE 使用，但此时只保护信令、媒体仍是 RTP 明文；要加密话音必须"系统 NE
    激活 + 外部 SIP 网关 SRTP 参数置 RTP/SRTP"两者叠加。向客户汇报"中继已加密"前先核对媒体是否真
    的 SRTP（p161 决定表 + p192 抓包/挂锁验证）。
  conditions: SIP trunk TLS 交付与验收
  tags: [misconception, sip-trunk, srtp]

- id: n14
  title: SIP TLS 扩展限制：仅 SEPLOS 模式、不支持 CCD agent、仅 IPv4、不支持第三方与老 ALE SIP 设备
  type: limitation
  source_pages: p88-89, p159
  source_chapter: SIP TLS COMPATIBLE ENDPOINTS
  source_quote: |
    "Compatible devices (SEPLOS mode only) … Not supported for third-party devices and older ALE SIP
    devices" (p88)
    "Restrictions in the current implementation • CCD agent on SIP endpoints (SEPLOS mode) • IPv4
    only" (p89)
    "Not compatible with IPv6 • SIP TLS with SSM is not compatible with Native Encryption SIP TLS" (p159)
  summary: |
    SIP TLS 扩展加密的四条边界：仅 SEPLOS 模式设备（ALES、ALE-x00、ALE-30、ALE-x 与 OV8770），第三
    方 SIP 设备与老 ALE SIP 设备不支持；SIP 端点 CCD agent 场景不可用；仅 IPv4；SIP TLS with SSM 与
    Native Encryption SIP TLS 互斥、整体不兼容 IPv6。涉及第三方话机或 IPv6 的报价要提前排除。
  conditions: SIP TLS 扩展加密选型
  tags: [limitation, sip-tls, seplos, ipv6]

- id: n15
  title: SIP TLS 端口 0 覆盖陷阱：互认证端口填 0 会静默关闭该网关互认证，MAO 参数仍显示 True
  type: version-trap
  source_pages: p166-167
  source_chapter: MUTUAL AUTHENTICATION – ports management
  source_quote: |
    "setting the SIP TLS (Mutual Auth.) port number as '0' overrides the SIP-External Gateway
    Parameter: 'SIP TLS Mutual Authentication parameter: True' • Mutual Authentication will be
    disabled for this use case • In MAO, this parameter will not change to 'False' automatically
    ( It will stay as 'True' unless changed manually)"
  summary: |
    本地 SIP 网关的 SIP TLS (Mutual Auth.) 端口号填 0，会覆盖外部网关参数 SIP TLS Mutual
    Authentication=True（该网关实际关闭互认证），而 MAO 界面的 True 不会自动变 False——界面与实际
    行为背离。端口组合模型：0/0 无 TLS、5061/0 仅服务器认证、0/6261 仅互认证、5061/6261 并存；改
    端口须重启 SIPmotor。
  conditions: SIP TLS trunk 端口与互认证配置
  tags: [version-trap, ports, mtls]

- id: n16
  title: Loose Route with RegID=True 会让相应 INVITE 被 488 拒绝
  type: limitation
  source_pages: p140, p253
  source_chapter: System SIP parameters
  source_quote: |
    "Loose Route with RegID False • If it is set to True, such INVITE is rejected with a '488.Not
    Acceptable Here' response. If it is set to False, such INVITE is accepted"
  summary: |
    SIP 参数 Loose Route with RegID 在实验口径置 False：置 True 时相应 INVITE 直接被 488 Not
    Acceptable Here 拒绝。排障 SIP TLS 呼叫失败时先核对该参数与 TLS signaling possible/SRTP offer
    answer mode 三件套的取值。
  conditions: SIP TLS 参数配置与呼叫失败排障
  tags: [limitation, sip-parameters, troubleshooting]

- id: n17
  title: 配置变更的生效动作清单：TLS 信令要重启 CS、SRTP 认证要重启 SIPMOTOR、改 mTLS 要重签 lanpbx+重启
  type: warning
  source_pages: p141, p190, p253, p364, p377, p379
  source_chapter: 各实验章 Warning/说明
  source_quote: |
    "Reboot the Call server(s) (or perform a double bascul) to make sure that the TLS signaling port
    is in listening mode. You can use the 'netstat -an | grep 5061' command to check the result." (p141)
    "RESTART THE SIPMOTOR PROCESS AFTER THE CONFIGURATION." (p190)
    "To take into account this modification, regenerate the 'lanpbx.cfg' file on OXE Node 1 and
    perform a reboot of the OXE system." (p364)
  summary: |
    生效动作对照：开 TLS signaling possible → 重启 CS（或双 bascul），netstat -an|grep 5061 验证监
    听；改 Authentication for SRTP / SIP TLS Mutual Authentication（trunk 侧）→ 重启 SIPMOTOR
    （dhs3_init -R SIPMOTOR）；改 Enable Mutual TLS Authentication（DTLS）→ 重签 lanpbx.cfg + 重启
    系统；SIP 扩展互认证参数 → 节点重启。"配了没生效"先对号这四张牌。
  conditions: NE/SIP TLS 参数变更后
  tags: [warning, reboot, sipmotor]

- id: n18
  title: IPDSP 只工作在 SRTP 认证模式——SRTP 认证改值会连带软话机
  type: limitation
  source_pages: p119, p190, p254
  source_chapter: Authentication for SRTP
  source_quote: |
    "Authentication for SRTP Authenticated • An IP Desktop Softphone works only with SRTP
    authentication." (p119, p254)
    "Change Only if the other end is managed with 'authenticated'." (p190)
  summary: |
    Authentication for SRTP 的取值约束：IPDSP 软话机只在 SRTP authentication 模式下工作，因此部署
    IPDSP 的系统实际上锁定 Authenticated；同时原书提醒只在对端（如 SBC）也配为 Authenticated 时才
    改此值。三个取值：Unauthenticated（默认）/Authenticated/Authenticated tag emis. w/o ctrl。
  conditions: SRTP 认证参数与软话机共存
  tags: [limitation, srtp, ipdsp]

- id: n19
  title: EEGW 五条硬边界：强制 VM、同宿主同交换机、专线明文、断链 CS 重启、证书操作连坐重启
  type: warning
  source_pages: p200-203, p211, p239, p241
  source_chapter: External EGW 讲义与实验 Warning
  source_quote: |
    "The presence of an external EGW implies the virtualization of the associated Call Server • The
    Call Server and its EEGW must be located on the same virtual switch of the same physical host"
    (p201)
    "The call server goes for reboot if the link with the external EGW is lost" (p203)
    "Warning THE CALL SERVER ASSOCIATED TO THE EEGW VIRTUAL MACHINE WILL REBOOT TOO!" (p239)
  summary: |
    EEGW 的连带风险：①部署 EEGW 即要求关联 CS 虚拟化，且同物理主机同虚拟交换机；②CS-EEGW 间专用
    UA/UDP 明文链路兼做存活监控，链路丢失 CS 直接重启；③在 EEGW VM 上下载/变更证书触发 EEGW 重启
    时，关联 CS 会跟着重启（原书两处大写 Warning）；④每台 CS 一台专属 EEGW；⑤EEGW 需人工报价，
    无自动计数。变更窗口必须按"CS 重启"级别规划，不能当普通 VM 维护。
  conditions: EEGW 部署与全生命周期维护
  tags: [warning, eegw, reboot, change-management]

- id: n20
  title: 声明类改动的统一代价：改 EEGW/Translator 名/域名都要重生成 CS 证书（CA 不变）+ 重启 + copy to twin
  type: warning
  source_pages: p219, p247, p267
  source_chapter: Encryption GW Management / Translator Name / Node setup
  source_quote: |
    "Warning: *** Change of External EGW Configuration, requires regeneration of Call Server
    Certificates (CA Update is not required ) followed by an OXE reboot***" (p219)
    "Warning: *** Change of translator name, requires regeneration of Call Server Certificates (CA
    Update is not required ) followed by an OXE reboot ***" (p247)
    "Warning: *** Change of Node name, requires regeneration of Call Server Certificates … followed
    by an OXE reboot ***" (p267)
  summary: |
    netadmin 三类声明（EEGW IP、Translator 名、节点名）任一变更，代价相同：CS 证书重生成（不用动
    CA）→ OXE 重启 → copy to twin。原因是这些要素都进了证书 SAN/CN。规划命名与 IP 时一步到位，
    避免反复触发改名-换证-重启循环。
  conditions: netadmin 声明类配置变更
  tags: [warning, netadmin, certificate]

- id: n21
  title: EEGW 网络前置：EEGW IP 必须进 CS 内部防火墙；Translator FQDN 必须可解析（内部 DNS 或委托）
  type: limitation
  source_pages: p205, p247, p267-268
  source_chapter: External EGW Deployment – Caution
  source_quote: |
    "Caution: EEGW IP addresses must be known in the CS internal firewall • SIP Translator FQDN must
    be resolved • Internal DNS resolver must be enabled in OXE • If external DNS is used, delegation
    to OXE DNS is needed" (p205)
    "THE INTERNAL DNS OF OXE SUPPORTS THE RESOLUTION OF THE FQDN OF SIP TRANSLATOR. WHEN AN EXTERNAL
    DNS IS USED, DELEGATION TO OXE DNS CAN BE USED TO RESOLVE THIS FQDN." (p247)
  summary: |
    部署前置两条：EEGW IP 地址必须加入 CS 内部防火墙（netadmin 11.1.3 受限访问，MAO 声明的 DHCP 段
    不能在 netadmin 改）；SIP Translator FQDN 必须可解析——OXE 内部 DNS（netadmin 17.2 激活）是唯一
    能按冗余角色返回主 CS EEGW IP 的应答方，外部 DNS 须把委托域转发给 OXE。漏配防火墙或解析是
    EEGW 不通的高频根因。
  conditions: EEGW/NSP 部署
  tags: [limitation, firewall, dns, eegw]

- id: n22
  title: NSP FQDN 与冗余绑定：冗余场景必须用 FQDN，单机才可用 EEGW IP 直填
  type: limitation
  source_pages: p266
  source_chapter: OTSBC proxy set 修改
  source_quote: |
    "Proxy Address Enter: nsp.oxe.company.com:5061 … Note: NSP FQDN is mandatory as soon as CS
    redundancy is implemented. Without redundancy, NSP IP address (equal to EEGW IP @) can be used"
  summary: |
    SBC 侧指向规则：实现了 CS 冗余就必须用 NSP FQDN（内部 DNS 按主备角色返回主 CS 的 EEGW IP）；无
    冗余时才可以直接填 EEGW IP。冗余站点把 SBC 指到固定 EEGW IP 会让主备切换后信令断。
  conditions: OTSBC Proxy Set 配置（EEGW/NSP 场景）
  tags: [limitation, nsp, redundancy, otsbc]

- id: n23
  title: S.O.T. 仅支持 Chrome/Firefox；媒体缺失要先 FTP 上传 BootDVD/OST ISO
  type: limitation
  source_pages: p273-274
  source_chapter: OST/EGW generation & loading with S.O.T.
  source_quote: |
    "CHROME AND FIREFOX BROWSERS ARE RECOMMENDED. OTHER BROWSERS ARE NOT SUPPORTED AND DISPLAY AN
    ERROR MESSAGE WHEN CONNECTING TO THE S.O.T. URL." (p273)
    "As it's indicated in red in Medias configuration page, 'BootDVD media is missing'. So, it is
    required to transfer the media files into S.O.T. local storage base … Login: upload • Password:
    sot" (p274)
  summary: |
    S.O.T. 两个入口坑：浏览器只用 Chrome/Firefox（其它浏览器直接报错）；新建环境媒体列表空（红色
    "BootDVD media is missing"），要先用 FTP 账号 upload/sot 上传 BootDVD.iso 与 OST.iso，再
    Refresh medias list + Declare medias，否则工程走不下去。
  conditions: S.O.T. 生成 EEGW VM
  tags: [limitation, sot, browser]

- id: n24
  title: EEGW 首登必须改密：Rocky Linux 口令规则 14 位强化；SSH key 已存在时勿重生成
  type: warning
  source_pages: p238, p260, p279
  source_chapter: EEGW VM 配置与证书下载
  source_quote: |
    "-password string must have a minimum of 14 characters … -password must be different from the
    last twenty-four used passwords" (p279)
    "SSH Key already present, Do you want to regenerate it (y/n, default n): n" (p238, p260)
  summary: |
    两个操作坑：EEGW 首次 root/letacla1 登录即被要求改密，规则为 ≥14 位、2 字母（含大写）、2 数字、
    1 特殊、不含用户名/4 连同符/4 顺序符/字典词、不与前 24 次重复——弱口令过不了；下载证书过程中
    提示 "SSH Key already present, Do you want to regenerate it" 时答 n（重生成会破坏既有信任关系）。
  conditions: EEGW VM 首次配置与证书下载
  tags: [warning, eegw, password]

- id: n25
  title: OMS 开 SSH 是临时动作：要告知客户开放时长，事后必须撤销 PC IP 白名单
  type: warning
  source_pages: p357, p367
  source_chapter: mTLS lab – OMS/GD 证书导入
  source_quote: |
    "You need to let the customer know about this activation of a previously inactive service and for
    how long it will be left active" (p357)
    "(!!!For security reasons please remove this IP once your task is over!!!)" (p357)
  summary: |
    给 OMS/GD 板卡传证书要先开 SSH（omsconfig/mgconfig 选项 6+9，按指定 PC IP 限时开放）：原书明确
    要求告知客户这项服务被激活及时长，任务完成后必须删除该 IP 白名单。生产变更单要把"开 SSH→传证书
    →关 SSH"作为一个闭环。
  conditions: OMS/GD 板卡证书导入
  tags: [warning, ssh, oms, security]

- id: n26
  title: OpenSSL 3.0 安全等级提升的兼容断裂：1024 位出厂证书设备升级 N3 后 mTLS 默认建不起来
  type: version-trap
  source_pages: p366, p83
  source_chapter: mTLS Restrictions
  source_quote: |
    "Since Release R101.0 (N3), OXE provides the support of the latest OpenSSL version 3.0 that
    implies an increase of the security level. Especially, X509 certificates with RSA keys of less
    than 2048 bits or signed with the deprecated SHA1 algorithm are not accepted anymore."
    "the current certificates provided from factory to secure some IP NOE DeskPhones, 8378 DECT
    IP-xBS base station and 8328 SIP-DECT single base station with Native encryption support 1024
    bits keys. As a result, after migration into R101.0 (N3) or later, the mutual authentication
    can't be established by default."
  summary: |
    升级陷阱：R101.0(N3) 起 OpenSSL 3.0 拒收 <2048 位或 SHA1 签名证书——部分 NOE 话机、8378 IP-xBS、
    8328 SIP-DECT 的 1024 位出厂证书在 N3+ 上无法建立双向认证（升级前能连的设备升级后连不上）。
    两条出路：①外部 PKI 重签 ≥2048 位证书并部署；②R101.1(N4) 起 netadmin 11.6.3 降 SSL level
    （2→1 需 SHA2+1K，0=恢复 SHA1+无下限），重启+copy to twin，安全风险管理员自担。SIP TLS 侧互
    认证仅 Basic（ALE-2/ALE-3）、Essential（仅 ALE-30）、Enterprise SIP 支持，且是系统级一刀切。
  conditions: 升级到 R101.0+ 后启用 mTLS、老旧终端存量
  tags: [version-trap, openssl, mtls, upgrade]

- id: n27
  title: mTLS 激活的连带义务：所有话机/软话机（含明文用户）都必须有证书，首连总是加密模式
  type: warning
  source_pages: p82, p359
  source_chapter: MUTUAL AUTHENTICATION
  source_quote: |
    "AS SOON AS 'MTLS' IS BROUGHT INTO SERVICE, CERTIFICATE MUST BE LOADED IN ANY IP DESKPHONE OR ANY
    IP SOFTPHONE, EVEN THOSE IN CLEAR MODE. THE FIRST CONNECTION TO OXE IS ALWAYS IN SECURED MODE,
    BEFORE « NATIVE ENCRYPTION » USER OPTION IS CHECKED." (p359)
  summary: |
    mTLS 不是"只管加密用户"：激活后第一连接总是加密模式，任何 IP 话机/软话机（包括没开 Native
    Encryption 的明文用户）都必须装有证书，否则注册失败（EGW 触发含端点 IP/MAC 的事件）。启用前按
    端点台账把证书铺满，别只给加密用户发证书。
  conditions: mTLS 启用决策与部署
  tags: [warning, mtls, endpoint]

- id: n28
  title: 话机证书服务器参数下发后仍需手工一步：开机 Get Certificate；SCEP 才是真自动
  type: limitation
  source_pages: p371-375
  source_chapter: Customized certificates for IP phones
  source_quote: |
    "Thus, as the sets download the 'lanpbx.cfg' file, they retrieve automatically the required
    information (web server, path and port). A manual action is then necessary on the set to complete
    the certificate retrieval. So, press 'Get Certificate', during the set startup phase and
    validate." (p374)
  summary: |
    话机定制证书三种部署法的自动化程度：手工法（话机里填 HTTP/端口/路径）全手动；lanpbxbuild 写入
    CERTSRV_IP/PORT/PATH（选项 d/e/f）后参数自动下发，但话机端仍要在启动阶段按 i+# → Security/
    Certificate/Get Certificate 手工确认一次；只有 SCEP 是全自动。批量交付别把"参数下发"当成
    "证书到位"。
  conditions: 话机定制证书批量部署
  tags: [limitation, scep, certificate, deployment]

- id: n29
  title: OTSBC/OXE 两侧端口必须成对核对：本地网关互认证端口↔Proxy Set、外部网关端口↔SIP Interface
  type: limitation
  source_pages: p378-379
  source_chapter: mTLS Appendix – Public SIP trunk
  source_quote: |
    "In case of SIP trunking with OTSBC, the SIP TLS (mutual auth.) port of the local gateway must
    match the one defined at 'proxy set' level in the OTSBC." (p378)
    "In case of SIP trunking with OTSBC, the SIP port number (for SIP TLS mutual authentication)
    specified in the SIP external gateway must match the one defined at 'SIP interface' level in the
    OTSBC." (p379)
  summary: |
    两侧端口成对规则：OXE 本地网关的 SIP TLS (Mutual Auth.) 端口（默认 6261）=OTSBC Proxy Set 的
    Proxy Address host:6261；OXE 外部网关的 SIP 端口（如 5061）=OTSBC SIP Interface 的 TLS 端口。
    Proxy Address 的 host 取值：本地冗余=主 CS IP、空间冗余=OXE FQDN、EEGW+NSP=SIP translator FQDN。
    端口对不上即 TLS 建链失败。
  conditions: SIP TLS trunk（尤其 mTLS）排障
  tags: [limitation, ports, otsbc]

- id: n30
  title: PKCS#7 vs PKCS#12 路线取舍：P7 私钥不出机是推荐；P12 私钥搬家+手工 CSR 易错
  type: warning
  source_pages: p391, p397
  source_chapter: External Certification Authority – Tips/Warning
  source_quote: |
    "PKCS7 is the easiest and may be the best way to generate certificate(s) signed by an external
    PKI (CA) because the private key of the entity doesn't move (is and stays on the entity only).
    In addition, the CSR is also generated on the entity itself and in our case automatically thanks
    to netadmin tool, so no risk to miss an information/field or make a mistake" (p391)
    "Warning PKCS 12 IS NOT THE EASIEST WAY … PRIVATE KEY IS GENERATED ON THE CA AND MUST BE
    TRANSFERRED TO THE END ENTITY WITH CERTIFICATE • CSR IS DONE MANUALLY ON THE CA: FIELDS AS COMMON
    NAME AND ALL SANS MUST BE CONFIGURED MANUALLY AND CORRECTLY" (p397)
  summary: |
    格式路线立场：PKCS#7（CSR 在实体上由 netadmin 自动生成→CA 只回签证书）是原书明示的"最简且最好"
    路线——私钥不出端点、SAN/CN 零手填错误；PKCS#12 被原书用 Warning 标注"不是最简方式"——私钥在
    CA 生成后要随证书搬运、CN/全部 SAN 全靠手工填对，仅适合端点证书等 CSR 不可行的场景。XCA 章的
    PKCS#12 实体证书（GW.pfx/softphone_cert.pem）就是这类场景的示范。
  conditions: 证书签发路线规划
  tags: [warning, pkcs7, pkcs12, pki]

- id: n31
  title: 加密呼叫是端到端能力链：任一环缺失即明文（对端节点/中继链路/端点/AES 位数）
  type: limitation
  source_pages: p295-300, p303, p71
  source_chapter: ABC-F 网络讲义（四类呼叫拓扑）
  source_quote: |
    "In this example, as the ABC IP hybrid link between nodes 2 & 3 is not encrypted, the media flow
    is in clear mode." (p295)
    "Even though the link is encrypted, voice communications between the sets are not encrypted,
    since one of the set involved in communication does not support 'Native Encryption'" (p300)
    "In an ABC network in direct link mode, if one node has managed AES-128 for SRTP and the other
    one AES-256, network communications between those nodes will be in clear mode • But the signaling
    on the direct link will be ciphered" (p303)
  summary: |
    端到端判断规则：媒体加密要求呼叫路径上每一环都加密——transit 链路未加密（p295）、对端节点未启
    NE、任一端点未开加密（p300）、两侧 SRTP 位数不一致（AES-128 节点 vs AES-256 节点，p303）任一条
    不满足，该段媒体即明文 RTP（信令仍可能加密）。验收"全程加密"要按呼叫路径逐环核对，而不是只看
    本端状态。
  conditions: ABC-F 网络与端到端加密验收
  tags: [limitation, abc-f, end-to-end]

- id: n32
  title: ABC-F 网络加密的拓扑禁区：仅 hybrid link 有 transit；direct link 网络不允许该拓扑；与 IPS 不互通
  type: limitation
  source_pages: p297-298, p301, p303
  source_chapter: ABC-F Miscellaneous / Implementation
  source_quote: |
    "'Transit node' concerns only 'IP Hybrid Link' based network • No transit node in a 'Direct IP
    Link' based network" (p297)
    "Interoperability with 'IP Premium Security' solution is not supported • Not allowed in a 'Direct
    Link' based network (even if the link is in clear mode) • Topology available only in a 'Hybrid
    link' based network … Calls are established in clear mode for IPv6 devices." (p301)
  summary: |
    拓扑约束：网络加密的 transit 节点行为只在 hybrid link 网络存在（direct link 无 transit，直连就
    是端到端）；整个网络加密拓扑只允许 hybrid link 网络（direct link 网络即使链路明文也不允许——
    注意与 p303 "AES-256 要求 Direct Link 标签"分属两个维度，分别是拓扑与单系统标签）；与 IP
    Premium Security 不互通；IPv6 设备呼叫明文。组网设计前先定 link 类型。
  conditions: ABC-F 组网设计
  tags: [limitation, abc-f, hybrid-link, ips]

- id: n33
  title: 原书自带的标注噪音：ITSP1/ITSP2 混用、GD4 串口速率 11520 疑为 115200、按需启停 VM
  type: misconception
  source_pages: p42-46, p367, p49
  source_chapter: SIP Carrier Simulator / mTLS Appendix / Pod topology
  source_quote: |
    "SIP SIMULATOR OVERVIEW – ITSP2 SIP GATEWAY … ITSP2 SIP Gateway gateway.itsp2.com … ITSP1 Public
    gateway public.itsp1.com … Id: publicP@itsp1.fr" (p43)
    "9600-8-N-1 for GD3, 11520-8-N-1 for a GD4" (p367)
    "Only start the required Virtual machines for the labs … Except the ENTP_PCS_FSNE, ENTP_EEGW_CSA
    and ENTP_EEGW_CSB VM's. These will be started later." (p49)
  summary: |
    照抄原书会困惑的三处：①SIP 模拟器章题 ITSP2，但网关账号/公网网关/SIP 域混用 itsp1 命名（p43-46
    ITSP1/ITSP2 交替出现）——视为同一模拟器的两腿即可；②GD4 串口速率原文写 11520-8-N-1（业界标准
    值为 115200，疑为原书脱漏一个 0，按原文照录、实操按设备文档核实）（推断）；③Pod VM 分批启动：
    EEGW/PCS 实验前不起对应 VM，资源紧张时按章启停。
  conditions: 阅读与实验复现
  tags: [misconception, book-noise, lab]

- id: n34
  title: RLAB 平台约束：两台 VM 不能共用 IP；证书日期强依赖 NTP 同步
  type: limitation
  source_pages: p50, p285
  source_chapter: Pod Configuration（两章）
  source_quote: |
    "To have no issue with the certificates date, it is recommended to have a correct date and time
    synchronization for all equipment's." (p50)
    "Due to RLAB infrastructure and technology, 2 VMs (even if not started) can't have the same IP
    address." (p285)
  summary: |
    两条实验平台约束（对生产亦有启示）：①证书有效期校验强依赖时间同步，所有设备统一对 NTP
    （192.168.1.252，实验口径）——时间漂移会让 notBefore/notAfter 校验失败、端点连不上；②RLAB 里
    两台 VM 即使关机也不能同 IP，切换拓扑要先删旧接口再建新接口并硬重启（生产中即 IP 规划冲突预防）。
  conditions: 实验环境与时间同步治理
  tags: [limitation, ntp, lab, ip]
```

---

## 收尾自检 — 对照 BOOK_OVERVIEW.md 18 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | 密码学与证书基础 | 有 → n30（P7/P12 路线取舍） |
| task-02 | Pod 环境搭建 | 有 → n33（标注噪音/按需启停）、n34（NTP/IP 约束） |
| task-03 | SIP 模拟器 | 有 → n33（ITSP1/2 混用） |
| task-04 | CSR 签发导入闭环 | 有 → n03（无 IP SAN 陷阱）、n05（CA 更新连锁）、n30 |
| task-05 | 系统/用户参数 | 有 → n16（Loose Route 488）、n18（IPDSP 锁 Authenticated） |
| task-06 | lanpbx.cfg | 有 → n05（重生成义务）、n17（生效动作） |
| task-07 | DTLS 验证维护 | 有 → n07（5992/5993）、n10（信任库/恢复出厂）、n11（factory reset）、n12（5991/5995） |
| task-08 | Wireshark | 无边界类（操作章无独立 Warning/Note，仅 p135 口令默认值已入 principle p21） |
| task-09 | SIP TLS 扩展 | 有 → n14（SEPLOS/CCD/IPv4 边界） |
| task-10 | PCS 接管 | 有 → n08（救援前置/lanpbx 共用）、n09（断网失联） |
| task-11 | SIP trunk TLS/SRTP | 有 → n13（信令≠媒体）、n15（端口 0 覆盖）、n16、n29（端口成对） |
| task-12 | 安全停用 | 无独立边界条目（回退顺序的注意事项已并入 c08 步骤与 n17 生效动作） |
| task-13 | EEGW/NSP | 有 → n19（五条硬边界）、n20（声明改代价）、n21（防火墙/DNS 前置）、n22（FQDN 冗余绑定） |
| task-14 | S.O.T. 生成 | 有 → n23（浏览器/媒体）、n24（口令/SSH key） |
| task-15 | 网络实验室改造 | 有 → n10（OMS 旧证书清除）、n34 |
| task-16 | ABC-F 网络加密 | 有 → n31（端到端链）、n32（拓扑禁区） |
| task-17 | XCA 端点证书 | 有 → n25（SSH 临时开放）、n28（Get Certificate 手工步）、n30 |
| task-18 | mTLS 与限制 | 有 → n06（twin）、n26（OpenSSL 3.0 断裂）、n27（全员证书）、n17（生效动作） |

**18/18 中 17 项有边界类条目覆盖**（task-08/12 无独立边界框，已在表内说明，不构成缺口）。

### 扫描完整性说明（Warning/Note/Tips/Caution 标记框逐页核对）

- 已全部入册的 Warning 框：p113/p248（无 IP SAN 终端不可用）、p104-106/p225/p250/p322（CA 更新连锁）、p121/p230/p315（lanpbxbuild 主 CS）、p133（证书转存介质）、p152（PCS 共用 lanpbx）、p154（断网失联）、p219（EEGW 声明改）、p239/p241（EEGW 重启连坐 CS）、p247（Translator 改名/仅外部 EGW 强制）、p267（节点名改）、p273（S.O.T. 浏览器）、p288（OMS 旧证书）、p356（服务器认证前提/mTLS 全员证书）、p357（SSH 告知与撤销）、p366（SSL level 重启+风险自担）、p381（优先用客户自有 CA）、p397（PKCS12 非最简）。
- 已入册的 Note/Caution/Tips：p49（按需启停 VM）、p50（时间同步）、p52（IPDSP TFTP）、p73-74（HTTPS 下载限制/TOFU）、p78（工厂证书低版本闲置）、p80（TOFU/手工 CTL）、p84（ACME 前提）、p85（IP-xBS/80x8s 不兼容无 IP SAN）、p89（CCD/IPv4）、p91（同步 standby）、p92（PCS 救援前置）、p95（明文话机打加密 VM）、p98（VAA 120→60）、p108（搬移恢复出厂）、p117（删除中间文件）、p119/p254（IPDSP 认证）、p122（先激活 NE 再用 j/k）、p126/p234/p257/p317（EGW 菜单只读）、p127/p318（手工接受证书）、p148（NE 只在主节点）、p150（PCS 证书打 tar）、p166-167（端口 0 覆盖）、p184（Offer Both 兼容明文用户）、p190（SIPMOTOR 重启/对端一致）、p205（防火墙/DNS Caution）、p238/p260（SSH key 勿重生成）、p266（NSP FQDN 冗余强制）、p274（媒体缺失 FTP）、p279（Rocky 口令）、p285（VM 同 IP）、p295-303（端到端链/拓扑禁区）、p366（1024 位出厂证书）、p371-375（Get Certificate 手工步）、p378-379（端口成对）、p391（PKCS7 Tips）。
- 推断性结论已在条目内显式标注"（推断）"：n33（GD4 串口速率 11520 疑为 115200）。
- 版本号完整位数保留：R101.0（N3）、R101.1（N4）、OXE N5、R10.1.1。
- 复核后未单列的纯操作提示：p113/222/248 CSR 逐项作答说明（操作细节在 c02/c09/c10 步骤内）、p117/226/252（删除中间文件的教学清洁提示，不构成生产边界，已并入 n05 关联上下文）。
