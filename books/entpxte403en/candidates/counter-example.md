# 反例/限制/边界/易错点候选 — OmniPCX Enterprise SIP (ENTPXTE403EN R101.1 MD4 Ed12)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: 默认域名 oxedomain.com 会引发证书错误——必须先改正式注册域名
  type: warning
  source_pages: p62-63
  source_chapter: OXE domain (How-To)
  source_quote: |
    "!! IMPORTANT WARNING !! OXE is still having default domain name. Please configure a legitimate
    registered domain name, to prevent certificate errors."
    "Warning TO MODIFY THESE PARAMETERS, NETADMIN MENU MUST BE USED."
  summary: |
    出厂默认域名 oxedomain.com 直接用于 SIP 会造成证书错误（教材以 IMPORTANT WARNING 双处强调）；
    SIP 化第一件事是把域名改成客户合法注册域名。且域名参数只能用 netadmin 菜单改，管理工具
    （mgr/WebAdmin）只可查看——在 WBM 里找修改入口会白费劲。
  conditions: 全新站点 SIP 化之前
  tags: [warning, domain, certificate, netadmin]

- id: n02
  title: SIP 两形态服务等级差异是设计而非缺陷——Device 没有前缀/后缀与 CTI
  type: limitation
  source_pages: p67, p78
  source_chapter: SIP USERS / SIP DEVICE MODE
  source_quote: |
    p67: "SIP device • Cannot use prefixes/suffixes to activate PCX phone services"
    p78: "Cannot be supervised by CSTA (therefore, one cannot use the Computer Telephony Integration
    (CTI) mechanisms of the PCX) • Cannot be a call center agent • SIP set cannot belong to A group
    of sets • A pick-up group • A Manager/Assistant configuration"
  summary: |
    客户拿会议话机/门禁/视频设备（SIP Device 形态）提"要参与代接组/呼叫中心/经理助理"时，要正面告知
    这是形态上限：Device 不能用前缀/后缀激活业务、不能当酒店话机、不被 CSTA 监督、不能当坐席、不能
    入组。需要这些能力必须走 SEPLOS（SIP Extension）形态或换 ALE 终端。
  conditions: 终端选型与需求确认阶段
  tags: [limitation, sip-device, seplos]

- id: n03
  title: SIP Device 开通的结构性前提——私网+中继组+本地网关缺一不可
  type: limitation
  source_pages: p67, p85, p89
  source_chapter: SIP DEVICE MODE / SIP Users (How-To)
  source_quote: |
    p67: "Mandatory to configure: The local SIP Gateway, A SIP trunk group, An adjacent subnetwork"
    p85: "Remember that a call from/to a 'SIP device' user requires the OXE local SIP gateway."
    p89: "The local SIP gateway and the local SIP Trunk Group are mandatory for the SIP device."
  summary: |
    建一个 SIP Device 用户之前，必须先有：专用私网（勿占用 ABC 或 VPN 网络号）、私有 SIP 中继组
    （每系统仅一个 ABC 型）、本地 SIP 网关（关联该中继组）。跳过基础设施直接建户是新手最常见的
    "建了不通"。
  conditions: SIP Device 任何开通场景
  tags: [limitation, sip-device, prerequisites]

- id: n04
  title: 修改 SIP 中继组虚拟接入数必须重启系统——即使 TRKSTAT 显示 TS 空闲
  type: warning
  source_pages: p86
  source_chapter: Private SIP Trunk Group
  source_quote: |
    "Warning IN CASE OF MODIFICATION OF THE NUMBER OF VIRTUAL ACCESSES FOR SIP, A RESTART OF THE
    SYSTEM IT'S NECESSARY EVEN IF THE IF THE NEW TS ARE SEEN FREE USING « TRKSTAT »"
  summary: |
    加减虚拟接入（并发通道）后必须重启 OXE 才生效；TRKSTAT 里新 TS 显示 Free 不代表已生效。扩容
    窗口要按"重启级变更"规划，别当成热操作。
  conditions: SIP 中继组容量调整
  tags: [warning, trunk-group, restart]

- id: n05
  title: SIP 端口与计时器默认值不要乱动——仅支持或研发建议才改
  type: warning
  source_pages: p86-87
  source_chapter: Local SIP gateway / SIP Proxy notes
  source_quote: |
    p86: "You don't have to modify these standard values except if the customer uses specific clients
    with a non standard port Nb"
    p87: "SIP initial time-out, SIP timer T2, Timer TLS: do not modify these default values except in
    case of support or R&D specific recommendations"
    p87: "Recursive search: not used for the moment"
  summary: |
    三条"别动"：代理端口 5060 等标准值只在客户端非标时改；SIP initial time-out/T2/TLS timer 只在
    ALE 支持或研发建议下改；Recursive search 参数"暂未使用"（配了也没效果）。凭感觉调计时器是排障
    反模式。
  conditions: 本地网关与代理参数调整
  tags: [warning, parameters, proxy]

- id: n06
  title: ALES 客户端会被 DoS 检测误隔离 30 分钟——Framework 参数必须配
  type: warning
  source_pages: p88, p227, p251
  source_chapter: SIP Quarantine / ALE SoftPhone SIP proxy
  source_quote: |
    p88: "A SIP equipment that sends more than 50 messages in 3 seconds is automatically added in
    this dynamic list. It stays in the list 30'"
    p227: "'Framework period' and 'Framework Nb Message by period' parameters are used to avoid the
    ALES client being put in quarantine by OXE for 30 min due to DoS attack detection."
  summary: |
    3 秒 50 条即自动隔离 30 分钟（报文直接丢弃）。ALES 部署若不把 SIP Proxy 的 Framework period=3s、
    Nb Message=50 配好，软终端注册/订阅风暴会被当成攻击隔离——症状是"软终端莫名 30 分钟连不上"。
    自动隔离记录看 /usr4/tmp/sipalarm.log（f003 告警），高频网关可加 Trusted IP 白名单豁免。
  conditions: ALES 部署、高频 SIP 设备接入
  tags: [warning, quarantine, ales, dos]

- id: n07
  title: SIP 设备/扩展必须是 CS 内部防火墙信任主机（/etc/hosts）——漏配即无响应
  type: warning
  source_pages: p89-90, p177, p230, p349, p451
  source_chapter: SIP Users / ALE-2-3 / ALES / SBC / Remote Worker 各章 Warning
  source_quote: |
    p89: "THE SIP DEVICE MUST BE DECLARED AS TRUSTED HOST IN THE CS INTERNAL FIREWALL (NETADMIN -M /
    SECURITY). SO, MAKE SURE THAT THE IP ADDRESS OF THIS DEVICE IS PRESENT IN THE HOST FILE
    (MORE /ETC/HOSTS)."
    p451: "FOR REMOTE WORKERS PURPOSE, TO PERMIT MESSAGES EXCHANGE BETWEEN OTSBC AND OXE, OTSBC
    PRIVATE IP ADDRESS (LAN SIDE) MUST BE DECLARED AS CALL SERVER TRUSTED HOST."
  summary: |
    同一条 Warning 在全书五处出现（SIP Device、SIP Extension、ALES、SBC、远程链路）：一切主动向 CS
    发请求的网络设备都要登记为信任主机，登记后自动写 /etc/hosts；双机要 Copy set up 同步。漏配的
    典型表现是终端/网关完全无响应且无报错——先查 /etc/hosts 再深挖。内部 DHCP 启用时其地址段自动
    入防火墙（p177 note）。
  conditions: 一切终端/网关接入
  tags: [warning, firewall, trusted-host]

- id: n08
  title: 关闭 8770 DM 会删除其上的配置文件——存量话机必须 reset flash
  type: warning
  source_pages: p174, p198
  source_chapter: OXE DM activation (ALE-2/3 与 ALE-x00 两章同款)
  source_quote: |
    "BE AWARE THAT DISABLING THE DM IN THE OMNIVISTA 8770 WILL CAUSE THE REMOVAL OF THE DEVICE
    CONFIGURATION FILES FROM THE 8770 SERVER. SO, SIP CONNECTED PHONES WILL LOOSE THEIR
    CONFIGURATION. A RESET FLASH WILL BE MANDATORY ON ALL DEVICES"
  summary: |
    把 "Device Management in 8770" 参数关掉（切到 OXE DM）的瞬间，8770 上的话机配置文件被删除，原
    有 SIP 话机全部丢配置，所有设备必须 reset flash 重走入网。从 8770 迁移到 OXE DM 是"全站重开"
    级操作，必须有维护窗口与回退预案；混合过渡期话机可留 8770（仅 ALES 归 OXE）。
  conditions: DM 迁移/新装选型切换
  tags: [warning, dm, migration, 8770]

- id: n09
  title: OpenSSL 安全级 2 拒收老话机证书——降级是权宜且必须重启
  type: version-trap
  source_pages: p161-162, p179, p206-207
  source_chapter: OPENSSL SECURITY LEVEL / 话机开通章 SSL 段
  source_quote: |
    "With OXE R101.0 and the upgrade of OpenSSL component to v3.0, the SSL security level has been
    increased to '2', that implies that any certificate with a RSA key length lower than 2048 bits or
    with a SHA-1 signing algorithm is no longer accepted"
    "Decrease the SSL security level if required: it depends on the age of the SIP Deskphones you
    want to bring into service. OXE REBOOT IS MANDATORY."
  summary: |
    R101.0 起 OpenSSL v3.0 默认安全级 2：RSA<2048 位或 SHA-1 签名证书一律拒收——而部分近年的 ALE
    话机出厂就是 1K RSA/SHA-1 证书。老机入网失败的隐性根因在此；降级到 1 或 0 前先用 SSH
    certificate info 或话机 MMI 查证书，且降级必须重启系统（安全敏感站点应换证书而非降级；级别 3
    仅 ALE 内部测试用）。
  conditions: R101.0+ 系统部署存量话机
  tags: [version-trap, openssl, certificates]

- id: n10
  title: 空间冗余下 DM URL 必须用 FQDN 而非主 IP——DNS 委托是前提
  type: limitation
  source_pages: p181, p204
  source_chapter: DHCP Classes (两话机章)
  source_quote: |
    p181: "In case of no redundancy or in case of local redundancy, this URL can be the following
    one: https://<OXE Main IP address>/dmictouch In case of spatial redundancy, this URL must be the
    following one: https://<OXE FQDN>/dmictouch This OXE FQDN must be resolved by a DNS server"
  summary: |
    DHCP 类的 TFTP URL：无冗余/本地冗余可用主 IP；空间冗余必须用 OXE FQDN，且该 FQDN 要能被 DNS
    解析（OXE 内部域名解析器 + 客户 DNS 委托，p58-59）。空间冗余站点直接抄 IP 型 URL 会导致备机
    接管后终端找不到主用 CS。
  conditions: 空间冗余站点终端部署
  tags: [limitation, redundancy, dns, dm]

- id: n11
  title: DHCP 配置必须 Apply Modifications——进程只重启时读 dhcpd.conf
  type: warning
  source_pages: p183, p206
  source_chapter: "dhcpd" process restart
  source_quote: |
    "THE DHCP PROCESS RESTARTS AND READ THE '/ETC/DHCPD.CONF' FILE THAT CONTAIN THE NEW VALUES. IT IS
    MANDATORY TO DO THIS IN ORDER TO TAKE INTO ACCOUT THE MODIFICATIONS"
  summary: |
    WBM 里改完 DHCP（范围/类/子网）后必须点 Apply Modifications：dhcpd 进程重启并读
    /etc/dhcpd.conf 才生效。只改界面不 Apply，话机拿到的仍是旧参数——"配了不生效"高频根因。
  conditions: 任何 OXE 内部 DHCP 变更
  tags: [warning, dhcp]

- id: n12
  title: auto-discovery 的密码是用户密码码（默认 0000），话机高级菜单默认 123456——两码别混
  type: limitation
  source_pages: p183-184, p212
  source_chapter: MAC address allocation / Auto-discovery mode
  source_quote: |
    "If no MAC address is registered manually in the OXE WBM, no configuration file is generated.
    Thus, the set will start in Auto-discovery mode requiring: The username: Directory number of the
    user The password: Secret code from the user (by default 0000)"
  summary: |
    三个默认口令三件事：auto-discovery 认证=分机号+用户密码码（默认 0000）；ALE-2/3 本地 Advanced
    setting 菜单=123456（改网络模式/Auto Provision 用）；DM profile 下发的终端 admin 密码（实验
    2580）。用户报"话机登录不上"先分清是在哪一层要口令；全部默认值生产必须替换。
  conditions: 话机入网与本地维护
  tags: [limitation, passwords, auto-discovery]

- id: n13
  title: NOE↔SIP 切换的六类禁止场景与前置条件——离服/8770 DM/远程用户都不行
  type: limitation
  source_pages: p154-155
  source_chapter: TRIGGER FROM OXE THE SWITCH FROM NOE TO SIP
  source_quote: |
    "Only for local users on site (not the remote one) • Only if these users have the OXE CS as SIP
    DM (not 8770 SIP DM)"
    "Restrictions: The device with manager/assistant keys can't switch • The switch is forbidden for
    desk sharing, ubiquity, automated attendant, user profile and ACD station"
    "This operation is only working when the set is in service. If this operation is done when the
    set is not in service, switch ... must be done locally on the device using local MMI."
  summary: |
    切换不是万能按钮：仅本地用户（远程不行）、仅 OXE DM（8770 DM 不行）、话机必须 in service（离服
    时 OXE 侧改完仍要话机本地 MMI 补做）；六类禁止——带 manager/assistant 键、desk sharing、
    ubiquity、自动话务员、user profile、ACD 站。批量切换前先按这六类过滤存量用户，否则一半会卡住。
  conditions: NOE↔SIP 切换规划
  tags: [limitation, noe-sip-switch, restrictions]

- id: n14
  title: Force Download NOE/SIP=NO 时切换现场补下二进制——切换窗口以 30 分钟计
  type: version-trap
  source_pages: p192, p200
  source_chapter: DUAL PARTITION / Force Download 语义
  source_quote: |
    p192: "As SIP binary was not pre-loaded on the inactive partition, the switch will take time
    because the device has to download now the SIP binary."
    p200: "'Download' message means that currently, the NOE set is downloading the SIP binaries in
    background mode (it can take up to 30 minutes the first time)"
  summary: |
    Phone COS "Force Download NOE/SIP" 的代价差：YES=对侧二进制后台预载（首次下载可达 30 分钟，但
    切换秒级）；NO=切换那一刻现场下载（用户持机等待同量级时间）。R200 前出厂机与未预载机在"批量切换
    日"会形成长尾——要么提前预载，要么把切换排在夜间。
  conditions: ALE-x00/ALE-30 双栈机切换
  tags: [version-trap, dual-partition, force-download]

- id: n15
  title: DHCP 批量切 SIP 仅限"无其他 NOE 设备"——外部 DHCP 需 option 67
  type: limitation
  source_pages: p208, p214
  source_chapter: 7.1 notes / Appendix: Trigger by DHCP
  source_quote: |
    "This method is used when you need to switch only some of the NOE/SIP compatible deskphones ...
    If all deskphones must run in SIP mode, it is possible to use another method based on the DHCP
    server"
    "This method is ONLY AVAILABLE on system where there is no other device declared in NOE mode (or
    if a dedicated DHCP User Class can be configured on external DHCP server). ... IF YOU USE AN
    EXTERNAL DHCP SERVER, ADD THE NEW DHCP OPTION 67 WITH THE 'SIPCONFIG.TXT' KEYWORD"
  summary: |
    两种切换法适用边界：WBM 按钮=逐台精准切；DHCP 类挂 sipconfig.txt=整机批切，但前提是系统里没有
    其他 NOE 设备（或外部 DHCP 能为 NOE 类单独配置）。混存的站点用 DHCP 法会把不该切的 NOE 话机
    一起带走。外部 DHCP 记得加 option 67。
  conditions: 批量 NOE→SIP 切换方式选型
  tags: [limitation, dhcp, noe-to-sip]

- id: n16
  title: ALES 无二进制托管、无 auto-discovery——login 必须管理员预建
  type: limitation
  source_pages: p163, p230
  source_chapter: PRINCIPLE FOR ALE SOFTPHONE
  source_quote: |
    "OXE does not host any binaries for ALES SIP Softphone ... Compared to hardphone, it's not
    possible to generate configuration files 'on the fly' • There is no auto-discovery feature • The
    'login' has to be configured by an administrator before the first use of an ALES SIP Softphone"
    "Login Enter the login (Ex. eevans) It must correspond to a 'uid' field of the person who is
    defined in the LDAP directory. Password Must be empty (used only in local authentication
    context)"
  summary: |
    ALES 与话机入网路径不同：OXE 不宿其二进制（软件来自 ALE/应用商店），配置不能现场生成，没有
    auto-discovery——用户第一次用之前管理员必须建好 login；外部认证时该 login 必须对应 LDAP 的 uid，
    OXE 侧密码字段留空（只有本地认证才需要）。批量开通漏建 login 是软终端"登录即失败"的头号原因。
  conditions: ALES 开通（PC/移动同）
  tags: [limitation, ales, ldap]

- id: n17
  title: ALES Mobile 专属雷区——Keep Alive 必须 NO、轮询不得低于 21600s
  type: warning
  source_pages: p252-253
  source_chapter: ALE SoftPhone (Android) / COS 与 DM profile
  source_quote: |
    "Keep Alive NO. For ALES Mobile, this 'Keep Alive' option is mandatory to be set 'NO' to be
    compatible with the Push Notification mechanism"
    "Config update polling timer If the value is configured below 21600s, the notification mechanism
    for ALES Android client will not work properly."
  summary: |
    移动端两条强制：Phone COS 的 Keep Alive=NO（否则推送通知机制不工作——来话不推）；DM profile 的
    Config update polling timer 不得低于 21600 秒（低于则配置更新通知失效）。照抄 PC 版参数（Keep
    Alive=Yes）到移动端 profile 是移动来话丢失的经典根因。
  conditions: ALES Android/iPhone 部署
  tags: [warning, ales-mobile, push]

- id: n18
  title: 外部认证与本地认证互斥——切换必须先关再开
  type: warning
  source_pages: p226, p242, p262
  source_chapter: ALE SoftPhone 认证切换 Warning（三处同款）
  source_quote: |
    "IF 'LOCAL AUTHENTICATION' IS ACTIVATED, YOU HAVE TO DEACTIVATE IT FIRST, BEFORE ENABLING LDAP
    ONE"
    "AS 'EXTERNAL AUTHENTICATION' IS CURRENTLY ACTIVATED, YOU HAVE TO DEACTIVATE IT FIRST, BEFORE
    ENABLING INTERNAL ONE"
  summary: |
    swinst 的两种认证互斥：开 LDAP 前必须先停本地认证，开本地认证前必须先停 LDAP（三处 Warning）。
    直接切开关会失败；切到本地认证后还要给每个 ALES 用户补密码（外部认证时该字段不要求，p230），
    且用户首连强制改密。切换动作牵动全量用户，选在维护窗口做。
  conditions: 认证模式切换
  tags: [warning, authentication, swinst]

- id: n19
  title: 一号多机互斥的边界——同型互踢、通话中禁抢、跨型无感
  type: limitation
  source_pages: p115-117
  source_chapter: ALE SOFTPHONE – USE SAME LOGIN ON DIFFERENT DEVICE
  source_quote: |
    "Any SIP message (different than REGISTER) from this Directory Number with a different ALES-DUID
    is rejected"
    "In this case, the login request on ALES PC2 is rejected (even with the force attribute) Call is
    in progress"
  summary: |
    给用户讲清三条：同一账号两台 PC（或两台手机）是互斥的（403 + Warning 399 Multiple Logins，可
    force 抢占，被顶端立即被踢）；PC 与手机跨型登录互不影响；旧设备通话进行中新设备即使 force 也
    进不来。客服口径：403 399 不是被盗号，是二号机登录顶号。
  conditions: ALES 一号多机使用
  tags: [limitation, ales-duid, multi-login]

- id: n20
  title: ALES 视频与若干特性在虚拟桌面不可用——VDI/RDS 明确不支持
  type: limitation
  source_pages: p121, p241
  source_chapter: ALE SOFTPHONE – FEATURES NOT SUPPORTED / 视频实验 note
  source_quote: |
    p121: "Deployment in a client virtualized environment – VDI or RDS"（不支持清单）
    p241: "Note: it's not possible to test this feature with the PC Virtual Machines available in the
    Rlab (because 'Guacamole' does not support video)"
  summary: |
    ALES 不支持 VDI/RDS 虚拟化桌面部署；视频通话在虚拟桌面（如 Guacamole 网关）也测不了。客户在
    虚拟桌面环境推 ALES 的需求要提前劝退或改方案（物理机/瘦客户机直装），别把 VDI 当部署目标。
  conditions: 虚拟桌面/远程办公方案评估
  tags: [limitation, ales, vdi, video]

- id: n21
  title: 监督的机型与平台边界——只有 SIP 监督 SIP、iPhone 无监督、toast 仅 Win/Android
  type: limitation
  source_pages: p130-131
  source_chapter: SET SUPERVISION AND CALL PICK UP
  source_quote: |
    "Only SIP devices can be supervised by another SIP device. ... Supervision is not available on
    ALE SoftPhone on iPhone."
    "Available on Windows PC and Android Smartphone • When several supervisees ring, only one toast
    is displayed corresponding to the latest ringing supervisee"
  summary: |
    监督四边界：被监督的必须是 SIP 设备（NOE 话机进不了 SIP 监督体系）；监督端 iPhone 不可用；来话
    toast+专属铃声仅 Windows 与 Android；多被监督人同振只弹最新一条 toast（其余"静默"是设计）。
    NOE 存量站点想用 SIP 监督要先把被监督人 SIP 化。
  conditions: 监督/代接需求评估
  tags: [limitation, supervision]

- id: n22
  title: 寻线组并行组的混装禁令与组呼叫限制
  type: limitation
  source_pages: p138, p141
  source_chapter: HUNTING GROUPS / PARALLEL HUNTING GROUPS
  source_quote: |
    p138: "Transfer the call is not possible on a group call. • Forward and Do Not Disturb are not
    considered in call distribution."
    p141: "Mixed SIP/NOE configuration is NOT supported for parallel hunting group • Can contain only
    SIP devices or only NOE devices • Multi-devices CANNOT be part of such hunting group"
  summary: |
    四条易错：组来电不能转移；成员的呼转与 DND 不影响分配（用户以为设了 DND 就不被打扰——错）；并行
    组严禁 SIP/NOE 混装（首个成员类型定生死）；多终端用户不能进并行组。顺序/循环组才允许混装与多
    终端。需求评审时先问清要哪种搜索类型。
  conditions: 寻线组建组
  tags: [limitation, hunting-group]

- id: n23
  title: REX/Virtual UA/MIPT 不能进 SIP 多终端；混合多终端上限 3 台
  type: limitation
  source_pages: p134-135
  source_chapter: MULTI-DEVICES
  source_quote: |
    p134: "Only one ALE SoftPhone for Windows and one ALE SoftPhone for Mobile within the
    multi-devices"
    p135: "Second possibility: mixed multi-device configuration with a NOE deskphone and DECT •
    Limited to 3 devices ... ** Virtual UA, REX and MIPT are not supported"
  summary: |
    多终端配额：纯 SIP 组网=1 主 + 最多 4 副，其中 ALES Windows 与 ALES Mobile 各仅一台；NOE+DECT
    混合组网=最多 3 台，且 Virtual UA、REX、MIPT 三类虚拟/资源型终端不支持。用 REX 顶多终端名额的
    老配置思路在 SIP 多终端下不成立。
  conditions: 多终端组网规划
  tags: [limitation, multi-devices]

- id: n24
  title: 呼叫日志是终端本地行为——话机没开机时错过即无记录
  type: misconception
  source_pages: p129
  source_chapter: CALL LOGS note
  source_quote: |
    "Note: The call history is built and managed locally It is not the call history of OXE server.
    Receiving a call while the ALE SIP equipment is not started is not seen in this equipment call
    log"
  summary: |
    SIP 终端的呼叫日志是终端本地生成与管理的，不是 OXE 服务器侧日志——终端未启动时错过的来话不会
    出现在它的历史里。用户投诉"日志少了这条来电"，先核对终端当时是否在线，别往话单系统方向排查。
  conditions: 呼叫日志类投诉
  tags: [misconception, call-logs]

- id: n25
  title: SIP Key 设备级按键管理员只能删不能改；ALE-2/3 不支持集中存储
  type: limitation
  source_pages: p103, p126
  source_chapter: Centralization storage of SIP programmable keys
  source_quote: |
    p103: "Function of programmed keys ('SIP Key'), managed at device level, cannot be modified by
    the OXE administrator, but only deleted"
    p126: "Exception: only 8 keys on ALE-2 & 12 keys on ALE-3 can be defined in OXE Device Management
    (keys 1 & 2 reserved for multiline function)"
  summary: |
    可编程键管理双轨的坑：用户在终端上自配的 "SIP Key" 归设备级，OXE 管理员不可修改只能删除；OXE
    集中管理覆盖 #3~#122（#1/#2 保留 multiline），但 ALE-2 仅 8 键、ALE-3 仅 12 键可进 OXE DM，
    ALE-2/3 与酒店话机不支持集中存储。批量按键策略落地前先按机型分桶。
  conditions: 按键批量配置
  tags: [limitation, programmable-keys]

- id: n26
  title: 酒店模式/话务员助理/MLA 在 SIP 侧全系列缺席；8088 酒店只在 8770
  type: limitation
  source_pages: p98, p105, p121, p147
  source_chapter: 8008 overview / Not supported features / SIP DM: OXE VS 8770
  source_quote: |
    p98: "8008/8008G ... ALE SIP stack, in Business & hotel mode (no attendant, no CC agent)"
    p105: "Common features • Hotel mode • Manager assistant • Multi-Line appearance (MLA)"
    p147: "Support existing SIP phones : 8088 Hotel or Huddle Room, 8008 ... and also some other
    phone types, phased-out today (8001, 8018, 8028s…)"
  summary: |
    汇总边界：SIP 模式全系列没有酒店（8008 例外走 Business & hotel）与话务员助理、没有 MLA；8088
    酒店/Huddle Room 及停产机型（8001/8018/8028s）只能由 8770 DM 管理——OXE DM 不支持。NOE 站点
    SIP 化评估时，酒店与话务员助理用户是"留在 NOE"的硬理由。
  conditions: NOE→SIP 迁移评估
  tags: [limitation, hotel, mla, 8770]

- id: n27
  title: 按名呼叫（OXE 电话簿）只在 ALES 且不可用于远程——属性与并发都受限
  type: limitation
  source_pages: p125
  source_chapter: DIRECTORY SEARCH – ACCESS TO OXE PHONE BOOK
  source_quote: |
    "Compatibility: ALES softphones (PC, mobile) only • Not available for Remote Worker (via SBC /
    Reverse Proxy) • Feature compatible with OXE redundancy, but not available in PCS mode ... Up to
    48 entries are returned per search • The returned contact attributes are limited to first name,
    last name and directory number • Maximum 16 simultaneous requests"
  summary: |
    边界五条：仅 ALES（话机后续版本才有）；远程工作者不可用；PCS 模式不可用（冗余可用）；每次搜索
    最多 48 条、属性只有名/姓/分机号三项；服务最多 16 个并发请求。客户把它当"完整企业目录"承诺会
    翻车——完整目录检索应配 LDAP。
  conditions: 目录检索方案设计
  tags: [limitation, directory, call-by-name]

- id: n28
  title: 外线参数因运营商而异——教材只覆盖模拟运营商，TC2005 与运营商文档是唯一依据
  type: out-of-scope
  source_pages: p349
  source_chapter: SIP Carrier access via SBC (章首 Warning)
  source_quote: |
    "THIS MANAGEMENT MUST BE DONE ACCORDING TO THE SIP PUBLIC PROVIDER REQUESTS! PLEASE CONSULT THE
    DOCUMENTS (TC 2005, AND ADDITIONAL ONE…) GIVEN BY ALE OR THE PUBLIC OPERATOR TO CONFIGURE THE SIP
    GATEWAY AS EACH OPERATOR HAS ITS OWN SPECIFIC PARAMETERS"
  summary: |
    教材明示：每个运营商有自己的特定参数，外部 SIP 网关配置必须对照 TC2005 与运营商给的文档；教材
    流程只在 ITSP2 模拟器上验证过。真实对接时的 REGISTER 行为、P-Asserted-Identity 策略、号码格式、
    SIPS 强制等差异都在书外，任何"照书直配"都要先过运营商参数核对。
  conditions: 一切真实运营商接入
  tags: [out-of-scope, sip-carrier, tc2005]

- id: n29
  title: 系统级编解码开关压过一切——外部网关开了也白开
  type: warning
  source_pages: p274, p351
  source_chapter: CODECS / SIP Carrier access via SBC
  source_quote: |
    p274: "Not available: codec cannot be used whatever the call type (even if it is validated /
    possible at the objects/end-points level)"
    p351: "IF G722 AND OPUS CODECS ARE DISABLED AT SYSTEM LEVEL, THE USE OF THESE ALGORITHMS WILL BE
    FORBIDDEN BY THE OXE, EVEN IF ENABLED IN EXTERNAL SIP GATEWAY"
  summary: |
    G722/OPUS 支持域（System/Compression Parameters）是系统总闸：设为 Not available 时，无论外部
    网关、IP 域、终端怎么开，OXE 都禁用该编解码。外线章再做同款 Warning。排"对方只收 G711"类问题
    时先看总闸再看分闸；反向，想强压带宽时这也是最省事的单点。
  conditions: 编解码能力核查与配置
  tags: [warning, codecs, system-parameters]

- id: n30
  title: 法线不匹配直接回 488——Accept Mu and A law in SIP 关闭时他律 G711 被拒
  type: limitation
  source_pages: p273
  source_chapter: SYSTEM PARAMETERS
  source_quote: |
    "If the parameter is set to false, the other G711 law codec is rejected by the OXE A SIP 488 'not
    acceptable here' message is returned"
  summary: |
    系统法线随安装国（FR→A、US→μ）；"Accept Mu and A law in SIP"=False 时，对侧 SDP 里另一法线的
    G711 被 OXE 拒绝并回 488 not acceptable here——表现为"打运营商某些号码立即失败"。跨法线对接
    （A/μ 混合环境、部分国际中继）必须把该参数开 True。
  conditions: 跨法线互通场景
  tags: [limitation, codecs, 488]

- id: n31
  title: OPUS/G722 开关连带 G711 的强制关系；公共中继组只许直连 RTP
  type: rule
  source_pages: p280, p353-354
  source_chapter: EXTERNAL CALLS – SIP TRUNK GROUPS / External SIP gateway notes
  source_quote: |
    p280: "Important: G711 is required for OPUS/G722 -> in case of connection to GD/OMS • If OPUS
    or/and G722 is/are selected (yes), then G711 must also be validated"
    p354: "A public trunk groups (signaling type: ISDN all countries) A public trunk group allows
    only the direct RTP by using a Re-INVITE message (no transfer and no overflow)."
  summary: |
    两条联动：①外部网关开 Support OPUS 或 G722 时必须连带 Support G711=YES（对接 GD/OMS 媒体资源
    时 G711 是桥）；②公共型中继组（ISDN all countries）只允许经 Re-INVITE 的直连 RTP——不支持转移
    与溢出。在公共中继组上做复杂话务编排会踩这两条。
  conditions: 外部网关编解码与公共中继组
  tags: [limitation, codecs, trunk-group]

- id: n32
  title: entity 判别器只能关联已存在的实际判别器——顺序错了配不上
  type: warning
  source_pages: p358
  source_chapter: Logical-real discriminators association
  source_quote: |
    "HERE, IT IS NOT AS FOR THE REAL DISCRIMINATOR CONFIGURATION WITH THE ARS TABLE NUMBER, IT IS NOT
    POSSIBLE TO ASSOCIATE TO A LOGICAL DISCRIMINATOR A REAL DISCRIMINATOR NUMBER IF THIS LAST ONE IS
    NOT ALREADY EXISITING."
  summary: |
    配置顺序约束：entity 的 Discriminator Selector 上把逻辑判别器映射到实际判别器时，实际判别器必须
    已经建好（与 ARS 表号直接引用不同）。先建判别器规则再回 entity 挂映射，顺序反了会找不到可选值。
  conditions: ARS 判别器配置
  tags: [warning, ars, discriminator]

- id: n33
  title: OTSBC 未配置完成前 OXE 外部网关不工作——两章实验有依赖顺序
  type: limitation
  source_pages: p363
  source_chapter: SIP Carrier access via SBC / Maintenance note
  source_quote: |
    "For the moment, as OTSBC is not yet configured, the external gateway N° 3 is not operational for
    external calls establishment."
  summary: |
    OXE 侧把中继组/外部网关/ARS 配完只是"半边"：SBC 侧没配置完成前，外部网关 3 对外呼不通。教材把
    "OXE 侧接入"与"OTSBC 部署"拆成两章，现场排障时别忘了看对端进度，别在 OXE 侧空转。
  conditions: 经 SBC 的外线交付
  tags: [limitation, sbc, dependency]

- id: n34
  title: OTSBC 向导后切 HTTPS——通用证书要手工接受；重启动作别忘了
  type: warning
  source_pages: p369, p373, p431
  source_chapter: OTSBC deployment / RP 激活
  source_quote: |
    p373: "AFTER THE REBOOT, AS SPECIFIED IN SYSTEM SETTINGS WITH THE WIZARD, THE SBC WILL USE
    HTTPS. AS IT IS FOR THE MOMENT A GENERIC CERTIFICATE, YOU HAVE TO ACCEPT IT TO ACCESS TO WEB
    INTERFACE"
    p431: "After validation of reverse proxy function, the OTSBC must be restarted."
  summary: |
    两个"重启后"：向导按 SYSTEM 设置启用 HTTPS/SSH，重启后浏览器访问会撞通用证书，要手工接受才能
    进管理界面；激活反向代理功能后也必须重启 SBC 才生效。漏掉重启会把"配置不生效"误判成配置错误。
  conditions: OTSBC 部署与 RP 启用
  tags: [warning, ot-sbc, certificate, restart]

- id: n35
  title: 向导账号缺 Contact User 导致来话全丢——注册格式错误是隐性故障
  type: warning
  source_pages: p381-383
  source_chapter: OTSBC deployment / Registration credentials
  source_quote: |
    "If you verify, you should receive nothing on the Syslog from the SBC for the incoming call. In
    fact, the ITSP gateway doesn't know how to route the call because the SBC is not registered
    inside."
    "Put the login expected (podX) by the ITSP gateway in the field 'Contact User'"
  summary: |
    向导建的账号若不补 Contact User，REGISTER 的 from/to/contact 域格式不对，ITSP 侧"不知道把来话
    路由给谁"——症状极隐蔽：SBC 的 Syslog 上来话方向一片空白（不是报错而是没有）。修法：Accounts 里
    Contact User=运营商期望登录名，Action→Register 立即重注册。来话无声无息先查注册状态。
  conditions: OTSBC 注册型账号对接
  tags: [warning, ot-sbc, registration]

- id: n36
  title: SBC 默认只放行 2 个编解码——OXE 发的 G722/G729 到 SBC 被裁成 G711
  type: limitation
  source_pages: p374-375
  source_chapter: OTSBC deployment / Codec configuration
  source_quote: |
    "In the INVITE message, from SBC to ITSP, in the SDP, possible codec is G711 (PCMA)"
    "By default, only 2 coders were configured by the wizard. G729 is not present."
  summary: |
    向导给 OXE 侧 IP 组默认只配 2 个 coder：OXE→SBC 的 SDP 有 G722/G711/G729，SBC→ITSP 只剩
    G711——音质降级是 SBC 裁剪而非终端问题。要透传更多编解码须在 Allowed Audio Coders Groups 给
    OXE 组补 G729 等（Apply+Save）。音质投诉先对 SBC 两侧 SDP。
  conditions: OTSBC 部署后首测
  tags: [limitation, ot-sbc, codecs]

- id: n37
  title: 零touch 四大网络限制——HTTP 代理/802.1x/VLAN/Wi-Fi 全不行
  type: limitation
  source_pages: p404
  source_chapter: Case 2: Zero touch / out of the box
  source_quote: |
    "Restrictions: • No outbound HTTP proxy • No network requiring 802.1x authentication or VLAN
    identifier • No Wi-Fi (yet)"
  summary: |
    EDS 零touch 只适配"傻瓜网络"：出向 HTTP 代理环境不行、802.1x 认证网络不行、VLAN 标识网络不行、
    Wi-Fi 暂不支持。远程员工家里若是代理型或企业级认证网络，零touch 直接失败——售前勘察清单要把这
    四条问掉。
  conditions: 零touch 部署评估
  tags: [limitation, eds, zero-touch]

- id: n38
  title: ALE-2/3 不能 LAN↔WAN 动态搬迁——必须先切目标位置专用 DM profile
  type: warning
  source_pages: p402
  source_chapter: Case 1: Move LAN to WAN / Caution
  source_quote: |
    "Caution: ALE-2/3 DeskPhone cannot be moved dynamically from LAN to WAN or from WAN to LAN. They
    need separate DM profiles for LAN and WAN use cases. Before moving an ALE-2/3 DeskPhone from LAN
    to WAN or from WAN to LAN, the administrator must assign to the phone the DM profile dedicated to
    the new location (LAN or WAN), so that the phone reloads the new configuration files before being
    moved"
  summary: |
    机型差异雷区：ALE-x00/ALE-30（双栈）可 LAN→WAN 即插即迁；ALE-2/3 不行——必须管理员预先把目标
    位置的专用 DM profile（本地版/远程版两份）配给话机、让其重载配置后才能搬。直接拔走 ALE-2/3 到
    远程会起不来。远程办公终端清单按机型分别写操作说明。
  conditions: 话机远程搬迁
  tags: [warning, ale-2-3, remote-worker, dm-profile]

- id: n39
  title: 原生加密远程工人是 N4 新语义——旧版本传输模式不匹配直接不 provision
  type: version-trap
  source_pages: p414-415
  source_chapter: NATIVE ENCRYPTION & REMOTE WORKERS
  source_quote: |
    "Native encryption user parameter can be enabled on a remote worker (since OXE N4)"
    "even if the user's native encryption configuration (TLS/TCP/UDP) does not correspond to the
    transport mode managed between the SBC and the OXE (TLS/UDP/TCP), the OXE authorizes the
    provisioning of this user • This was not the case before the OXE N4 version"
  summary: |
    版本语义变化：OXE N4 之前，远程工人的用户加密传输模式与 SBC-OXE 段不一致会被拒（provision 失败）；
    N4 起经 REGISTER Via 头识别远程工人后放行。低版本站点按新语义配置会踩坑——先核系统版本再谈
    远程加密。配套：SBC LAN IP 清单最多登记 10 个，且不向其他节点广播。
  conditions: 远程工人原生加密部署
  tags: [version-trap, encryption, remote-worker]

- id: n40
  title: VPN 路线边界——ALE 不提供客户端、仅 ALE-2/3 内嵌且只支持 OpenVPN
  type: limitation
  source_pages: p398, p412
  source_chapter: ALES – TOPOLOGY THROUGH VPN / BASIC DESKPHONES THROUGH VPN
  source_quote: |
    p398: "A third-party VPN client is required to establish the VPN link • ALE doesn't provide any
    VPN client. • The level of security depends on the deployed VPN infrastructure"
    p412: "ALE-2, ALE-3 SIP basic Deskphones embed a VPN client ... ALE-2/ALE-3 only support
    OpenVPN, not IPSec VPN"
  summary: |
    两条边界：ALES 走 VPN 要客户自备第三方 VPN 客户端（ALE 不提供），安全水平随客户 VPN 基础设施
    而定——交付边界要写清；话机侧只有 ALE-2/3 内嵌 VPN 客户端且仅支持 OpenVPN（不支持 IPSec），兼容
    VPN 网关清单在部署指南里。客户环境是 IPSec-only 时话机 VPN 路线直接出局。
  conditions: VPN 远程方案评估
  tags: [limitation, vpn, ale-2-3]

- id: n41
  title: RP/SBC 证书信任链五方各管一段——漏导一张证书断一条链
  type: limitation
  source_pages: p408-410, p426-430
  source_chapter: AUTHENTICATION ON REMOTE WORKER DEPLOYMENT / TLS Contexts
  source_quote: |
    p408: "OT-SBC CA certificate must be imported in the OXE, so that OXE DM can included them in
    the CTL file ... ALE Terminals RootCA and SubCAs must be installed in RP's trust store"
    p410: "Reverse proxy CA certificate must be imported in EDS, so that it can provision an out of
    the box deskphone."
  summary: |
    远程办公证书是五方接力：话机信任库（Cloud Connect CA 默认在 + SBC/RP CA 经 CTL/EDS 下发）、RP
    信任库（ALE Terminals RootCA/SubCAs）、OT SBC 信任库（OXE 加密网关 CA）、EDS 信任库（默认有终端
    CA，还须导入 RP CA）、OXE（导 SBC/RP CA 以进 CTL）。任何一方缺一张证书，对应那一跳就握手失败
    ——远程排障先画五方图逐库核对。
  conditions: 远程办公证书部署与排障
  tags: [limitation, certificates, trust-chain]

- id: n42
  title: 远程桌面专用的 RP 头机制只认"已知 RP"——X-Real-Mac/X-Forward-For
  type: limitation
  source_pages: p159-160
  source_chapter: Deskphone authentication for configuration file download (remote worker case)
  source_quote: |
    "Reverse proxy must add in a specific HTTP header the Deskphone's MAC address, retrieved from the
    device certificate CN attribute • X-Real-Mac header with the Deskphone's MAC address • X-Forward-
    For header with the Reverse proxy's IP address, as only Reverse Proxys known by the Call Server
    are authorized to perform requests to the Call Server with those specific headers"
  summary: |
    远程话机 mTLS 下载依赖 RP 注入两个头：X-Real-Mac（话机 MAC，取自证书 CN）与 X-Forward-For（RP
    IP）；且只有 CS 已知的 RP 才被允许带这些头——客户自选的第三方反代若不注入或不被登记，远程话机
    拉配置必失败。反代选型与登记是隐性前提。
  conditions: 远程话机经反代拉配置
  tags: [limitation, reverse-proxy, mtls]

- id: n43
  title: DM 配置文件没有备份——数据库恢复后必须手工重新生成
  type: limitation
  source_pages: p166
  source_chapter: MISCELLANEOUS
  source_quote: |
    "There is no backup of configuration files. After database restoration, the manager must generate
    all configurations files manually using the action 'generate all configuration files'"
    "So, make sure that the 'Activate the Web Server' system option is 'true'"
  summary: |
    两个运维暗坑：①DM 配置文件不在备份范围内——数据库恢复后要手工执行 "generate all configuration
    files" 重造全部终端配置，否则全站终端拿不到配置；②SIP 设备经 NGINX+WBM 后端通信，"Activate the
    Web Server" 系统选项必须为 true。灾备演练清单里要有这一步。
  conditions: DM 运维与灾备
  tags: [limitation, dm, backup]

- id: n44
  title: 注册即服务、超时即离服——"话机不通"先查注册库
  type: limitation
  source_pages: p80, p91-93
  source_chapter: REGISTRATION OF THE USERS / Maintenance
  source_quote: |
    p80: "When a de-registration request is received or if the system does not detect SIP set presence
    after a timeout, the IP address of the corresponding SIP set is put to 0.0.0.0 and the SIP set is
    put out of service"
    p90: "Note: if the SIP trunks are out of service, a shutdown of the OXE might be necessary."
    p93: "IF REQUIRED, USE THE FOLLOWING COMMANDS TO REINITIALIZE THE PROCESSES - dhs3_init –R
    SIPMOTOR (RECOMMENDED) - killall sipmotor. WARNING: YOU HAVE TO BE LOGGED AS ROOT"
  summary: |
    排障顺序口径：SIP 用户注册状态即服务状态（注销/超时→IP 置 0.0.0.0→out of service），查
    sipregister 是第一步；私有 SIP 中继组不在服时可能要重启 OXE；sipmotor 进程异常时优先 dhs3_init
    -R SIPMOTOR（killall 需 root，属激进手段）。别在业务层空转，先看注册与进程。
  conditions: SIP 终端不通排障
  tags: [limitation, registration, troubleshooting]

- id: n45
  title: 模拟器与真实运营商不等价——ITSP 口径只是教学口径
  type: limitation
  source_pages: p22, p30, p349
  source_chapter: SIP CARRIER SIMULATOR / ITSP2
  source_quote: |
    p22: "SIP simulator is hosted in the RLAB common area"
    p30: "Id: podP password: alcatel"
  summary: |
    ITSP1/ITSP2 的账号（pbxP/podP + alcatel）、号码规则（嵌 POD 号）、公网用户行为全是教学约定；
    安全机制、编解码策略、号码格式、REGISTER 行为与生产运营商差异大。教材实验结论只能作为"流程已
    通"的证据，不能作为生产参数依据（另见 n28）。
  conditions: 实验结论向生产迁移
  tags: [limitation, simulator, lab-口径]

- id: n46
  title: 编解码设备矩阵有代际特例——8058s/68s/78s 与 GD/媒体资源不在"全支持"列
  type: limitation
  source_pages: p276
  source_chapter: DEVICES CAPABILITIES
  source_quote: |
    "8058s/68s/78s (NOE) specific case : support OPUS (SWB only) / G.722 in local calls … but G.722
    only in network ... G.722 and OPUS not supported • GD3/GD4/INTIP3 (G.711/G.729), A4645 (G.711),
    IP DR-Link (G.711), WLAN / DECT , ABC-F network (Hybrid Link mode)"
    "OXE-MS is required to provide media services (e.g., transcoding, conference, voice guides) with
    OPUS or G.722 codecs"
  summary: |
    矩阵特例三组：8058s/68s/78s（NOE）OPUS 仅 SWB 档且 G722 本地/网络口径特殊（按原文）；GD3/GD4/
    INTIP3、A4645、IP DR-Link、WLAN/DECT、Hybrid Link 完全不支持 G722/OPUS；OPUS/G722 的转码/会议/
    语音指南媒体服务必须有 OXE-MS 资源。全 OPUS 网络设计前先对这张矩阵清点存量媒体设备。
  conditions: 编解码方案设计与扩容
  tags: [limitation, codecs, devices]

- id: n47
  title: 域名判定三条件决定"来话是不是我的"——网关参数拼错整域失联
  type: limitation
  source_pages: p82, p330
  source_chapter: COMMUNICATION WITH A SIP END-POINT / CALLS WITH EXTERNAL SIP GATEWAY
  source_quote: |
    "If the recipient SIP domain corresponds to the SIP domain of the SIP gateway. Then the OXE is
    the destination"
    "The domain part of the 'ReqURI' matches with the OXE_Address parameter (Local Gateway) / The
    Machine Name parameter / The concatenation of the Machine Name and the DNS local domain Name
    parameters"
  summary: |
    来话归属判定靠 Request URI 域部分与本地网关三参数（OXE_Address、Machine Name、Machine
    Name+DNS 域名）逐一匹配；对不上时 OXE 不认为自己是终点，来话不进 Call Handling。改域名/主机名
    后忘记同步网关参数是"外线突然全断"的高频根因。
  conditions: 外线来话排障、域名变更后
  tags: [limitation, domain, incoming]

- id: n48
  title: RDP in RDP 双层远程会话——断错层会把自己主会话踢掉
  type: warning
  source_pages: p453
  source_chapter: ALES Remote Worker / Test
  source_quote: |
    "USING THIS RDP FILE, YOU WILL PERFORM AN RDP CONNECTION IN YOUR ALREADY ACTIVE RDP SESSION.
    TAKE CARE WHEN YOU WILL STOP (DISCONNECT) THIS SECOND RDP SESSION (RDP IN RDP) TO STOP THIS ONE
    AND NOT THE MAIN (FIRST) ONE."
  summary: |
    远程办公实验连"场外 PC"是 RDP 套 RDP：断开时必须断第二层（场外 PC），断成第一层会把自己的主
    会话踢掉。纯实验环境细节，但同类"多层远程"操作在生产运维（跳板机）同样致命，值得写进操作纪律。
  conditions: 多层远程访问
  tags: [warning, remote-access, lab]

- id: n49
  title: profile 必须先建后配用户——DM profile ID 引用不做存在性校验提示
  type: warning
  source_pages: p452
  source_chapter: ALES Remote Worker / User configuration
  source_quote: |
    "TO BE ABLE TO APPLY A DM PROFILE ID TO A USER, THIS PROFILE MUST BE EXISTING. SO, IF YOU WANT TO
    USE A NEW DEDICATED DM PROFILE FOR A PART OF THE USERS, YOU MUST CREATE THE PROFILE BEFORE TO
    CONFIGURE THE USERS."
  summary: |
    顺序约束：给用户挂 DM profile ID 前该 profile 必须已存在（新建专用 profile 也要先建再挂）。
    批量导入/脚本化开通时尤其容易先配用户后建 profile，造成配置引用悬空。
  conditions: DM profile 与用户配置
  tags: [warning, dm-profile, ordering]

- id: n50
  title: 实验明文口令贯穿全书——生产安全基线在书外
  type: out-of-scope
  source_pages: p9, p89, p114, p177, p183, p234, p243, p372, p456-457
  source_chapter: 实验环境 Settings 表与各实验
  source_quote: |
    p9: "mtcl swinst root Superuser2580* ... FLEXLM ... root letacla1 ... SBC ... Admin Admin"
    p89: "SIP Passwd 12345" / p234: "password Same password for all users: alcatel"
    p243-244: "Superuser1245* ... Administrator2580!"
  summary: |
    Superuser2580*、alcatel、12345、123456、0000、2580、letacla1、Admin/Admin、Superuser1245*、
    Administrator2580! 等口令全部是实验口径明文书写，且书中多处"全体用户同一口令"。生产交付必须：
    全量替换默认口令、按 p114 密码策略起配、LDAP/证书体系接管认证、防火墙白名单收敛——这些安全
    基线教材只给机制不给制度。
  conditions: 一切生产交付
  tags: [out-of-scope, security, lab-口径]

- id: n51
  title: 版本混布截图——R100.0/R101.0/R101.1 报文与界面并存，跨版本参数要现场核对
  type: version-trap
  source_pages: p54, p81, p159, p288, p314
  source_chapter: SIP 报文示例与 DM 演进说明
  source_quote: |
    p54: "User-Agent: OmniPCX Enterprise R101.0 n3.320.9.a"
    p314: "User-Agent: OmniPCX Enterprise R101.1 n4.521.3"
    p81: "User-Agent: OmniPCX Enterprise R100.0 n1.291.13.a"
    p159: "OXE DM evolution as of OXE R101.1 to enhance Deskphone authentication"
  summary: |
    全书截图/报文混有 R100.0（n1.291）、R101.0（n3.320）、R101.1（n4.521）多版本输出；mTLS 8443
    强下载认证等能力明确标 "as of OXE R101.1"。按教材操作前先确认站点版本是否具备对应特性——低版本
    站点没有 8443 mTLS、没有 N4 远程加密放行等行为。
  conditions: 跨版本交付与排障
  tags: [version-trap, versioning]

- id: n52
  title: SIP 中继组不在服时可能要整机重启；进程重启用 dhs3_init 而非 killall
  type: warning
  source_pages: p90, p93
  source_chapter: Softphone account management / SIP processes
  source_quote: |
    p90: "Note: if the SIP trunks are out of service, a shutdown of the OXE might be necessary."
    p93: "IF REQUIRED, USE THE FOLLOWING COMMANDS TO REINITIALIZE THE PROCESSES - dhs3_init –R
    SIPMOTOR (RECOMMENDED) - killall sipmotor. WARNING: YOU HAVE TO BE LOGGED AS ROOT"
  summary: |
    两级恢复口径：SIP 中继组 out of service 时教材直言"可能需要 OXE 关机重启"；sipmotor 进程异常先
    用 dhs3_init -R SIPMOTOR（推荐），killall sipmotor 是 root 级激进手段。把 killall 当首选会把
    可控故障升级成事故。
  conditions: SIP 服务恢复
  tags: [warning, restart, sipmotor]

- id: n53
  title: SEPLOS 的 SIP MESSAGE 显示可能被终端回 405——按机型关 UTF-8/CS 信息
  type: limitation
  source_pages: p74
  source_chapter: SEPLOS MODE / Phone classes of service
  source_quote: |
    "A SIP MESSAGE can be sent to the SEPLOS device providing information to display call server
    information ... If the terminal is not compatible with the 'Message' method (answer message '405:
    method not allowed') ... According to the set compatibility, it may be required to de-activate
    this feature for a better display"
  summary: |
    CS 经 SIP MESSAGE 向 SEPLOS 推显示信息（呼转/DND/寻线组归属/UTF-8 重音字母等）；终端不支持
    MESSAGE 方式时回 405 method not allowed，显示会乱或失败——按机型在 COS 里关掉该特性（Phone COS
    的 "Send NOTIFY instead of MESSAGE" 与 UTF-8 相关项）。三方话机入网后"显示乱码/无提示"先查这条。
  conditions: SEPLOS 终端显示异常排障
  tags: [limitation, seplos, message]

- id: n54
  title: OXE SIP 对接 rainbow/Rainbow 网关等外部系统属 ICE type 场景——Standard 型不带私有头
  type: limitation
  source_pages: p354, p56
  source_chapter: External SIP gateway (Gateway type note) / OXE SIP IMPLEMENTATION
  source_quote: |
    p354: "Gateway type: The default value of this parameter is 'Standard type', meaning that it
    doesn't handle any specific behavior. In an OmniTouch environment, the SIP gateway which handles
    the OT users has to be set to 'ICE type', to take benefit of the P-Alcatel-CSBU and P-CAC-ALU
    proprietary SIP headers."
    p56: 全景图中 "Rainbow WebRTC Gateway" 作为 SIP 侧互联对象出现
  summary: |
    Gateway type 保持 Standard 即无特殊行为；OmniTouch 环境承载 OT 用户的网关必须设 ICE type 才能启用
    P-Alcatel-CSBU、P-CAC-ALU 私有头。与 Rainbow WebRTC 网关等 ALE 生态互联时选错 gateway type 会
    丢私有头导致功能异常——对接 ALE 家族系统前先核对该字段。
  conditions: OXE 与 ALE 生态（OmniTouch/Rainbow）互联
  tags: [limitation, gateway-type, ecosystem]
```

---

## 收尾自检 — 对照 BOOK_OVERVIEW.md 20 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | 准备实验/交付环境 | 有 → n50（实验明文口令边界）、n12（默认口令三件） |
| task-02 | 掌握运营商模拟器 | 有 → n45（模拟器≠真实运营商） |
| task-03 | POD 预配置与外线打通 | 有 → n47（域名判定三条件）、n50 |
| task-04 | SIP 协议机理 | 无独立边界条目（协议机理为讲义；注册行为边界见 n44） |
| task-05 | OXE 域名与空间冗余 | 有 → n01（默认域名证书错误）、n10（空间冗余 FQDN 强制）、n51（版本混布） |
| task-06 | SEPLOS vs SIP Device 选型 | 有 → n02（Device 五不带）、n03（结构性前提）、n53（405 显示） |
| task-07 | SIP Device 开通 | 有 → n03、n04（改接入数须重启）、n05（参数别乱动）、n07（信任主机）、n52 |
| task-08 | 终端家族选型 | 有 → n26（酒店/MA/MLA 缺席）、n23（多终端配额）、n21（监督机型） |
| task-09 | ALES 认证设计 | 有 → n18（认证互斥）、n16（login 预建）、n19（一号多机边界）、n13 密码见 principle p13 |
| task-10 | ALE SIP 特性配置 | 有 → n21（监督边界）、n22（寻线组禁令）、n24（本地日志）、n25（SIP Key） |
| task-11 | SIP DM 选型与规划 | 有 → n08（8770 关闭清配置）、n26（8088/停产机型留 8770）、n43（配置无备份）、n49（profile 先建） |
| task-12 | OXE DM 证书定制 | 有 → n09（OpenSSL 级 2）、n51、n42（RP 头机制） |
| task-13 | ALE-2/3 话机开通 | 有 → n11（DHCP Apply）、n12（口令三件）、n07、n05 |
| task-14 | ALE-x00 双分区与切换 | 有 → n13（六类禁止）、n14（Force Download 代价）、n15（DHCP 法边界） |
| task-15 | ALES 软终端开通 | 有 → n16、n17（移动端双雷）、n18、n20（VDI/视频） |
| task-16 | 编解码协商与验证 | 有 → n29（系统总闸）、n30（488）、n31（G711 连带）、n46（设备矩阵特例） |
| task-17 | SIP 跟踪采集分析 | 有 → n44（注册即服务/恢复口径）、n52 |
| task-18 | 外线判定 + SBC 接入 | 有 → n28（运营商书外）、n31、n32（判别器顺序）、n33（SBC 依赖）、n47 |
| task-19 | OTSBC 部署调通 | 有 → n34（HTTPS/重启）、n35（Contact User）、n36（2 coder）、n33 |
| task-20 | 远程办公规划与落地 | 有 → n37（零touch 四限制）、n38（ALE-2/3 搬迁）、n39（N4 语义）、n40（VPN 边界）、n41（证书五方）、n42、n48（RDP 双层） |

**20/20 有边界类覆盖（task-04 由 n44 部分承接，协议机理本身无边界语义，已注明）。**

### 扫描完整性说明（Warning/Note/Tips/Important 标记框逐段核对）

- 已全部入册的 Warning：p62（域名/netadmin）、p86（虚拟接入重启）、p89-90/p177/p230/p349/p451（信任主机五处同类）、p161-162/p179/p206-207（OpenSSL+重启）、p174/p198（8770 关闭）、p183/p206（DHCP Apply）、p226/p242/p262（认证互斥三处）、p244/p263（先关外部再开本地，与 p226 同义并入 n18）、p321（sipdump 双连接）、p349（运营商参数）、p351（编解码总闸）、p355（ARS 必配）、p358（判别器存在性）、p373（HTTPS 通用证书）、p402（ALE-2/3 搬迁）、p415（含 Note 性质的 N4 语义）、p451（远程链路信任主机）、p452（profile 先建）、p453（RDP in RDP）。
- 已入册的 Note/Important/Tips：p39（TFTP 指向）、p74（405）、p80（注册即服务）、p86-88（网关/代理字段语义）、p90（中继组不在服要重启）、p92（TS 占用差异）、p103/p126（SIP Key/ALE-2/3 键数）、p115-117（DUID 机制）、p121/p125（不支持清单/按名呼叫）、p129（本地日志）、p130-131（监督边界/toast）、p134-135（多终端配额）、p138/p140-141（寻线组规则）、p146-148（DM 分界）、p152-153（profile 体系）、p156/p163/p165-166（配置文件/ALES/二进制/无备份）、p188/p191-194/p200（双分区）、p214（DHCP 触发边界）、p227/p251（防隔离）、p241（Guacamole）、p252-253（移动端双参数）、p273-274/p280（编解码规则）、p322（sipdump 读数）、p354（网关字段/公共中继）、p363（ExtGW 未生效）、p381-383（注册排障）、p387/p400（RP 规模）、p404（零touch 限制）、p408-410（信任链）、p412（OpenVPN only）、p414-415（N4 语义）、p447（路由条件 tip）。
- 复核后排除的纯操作提示（非边界类）：p36-37（SBC 虚机延后/PC11 不需要——实验环境事实，BOOK_OVERVIEW 已列为不入册）、p34/48/54/314 报文样例（教学材料）、p313（motortrace 级别经验——已入 principle p33）、p315（oxetrace 菜单——已入 case c10）、p455（RDP 文件位置——教学后勤）。
- 推断性结论标注：n26 中"8088 酒店只在 8770"由 p98（8008 Business&hotel）与 p147（8770 支持 8088 Hotel）合并推断，原书未以一句话直陈，条目内已按两处原文并列呈现；n47 "改域名后忘同步网关参数"为机制性推断（依据 p330 三条件匹配逻辑），非原书原话。
- 版本号均按原文保留完整位数：N1、N3、N4、R100.0、R101.0、R101.1、R200、v3.0、RFC 3261/3325/3326/4122/4733、TLSv1.1/1.2、DTLSv1.0/1.2、SHA-256。
