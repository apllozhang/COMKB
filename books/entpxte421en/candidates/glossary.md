# 术语/缩写/产品名候选 — OmniPCX Enterprise 原生加密 (ENTPXTE421EN Ed05)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 52 条（六类全量提取）。NOE/OMC/OMS/IPDSP/ALES/VAA/DC/IP-xBS/GD4/FlexLM/DDI/CC-suite-ID 等缩写书中未给全称，full_name 字段如实省略，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: Native Encryption (FSNE)
  full_name: Full Software Native Encryption（书中 p62 展开）
  category: concept
  source_pages: p61-66, p109
  source_quote: |
    "Native Encryption solution (also called 'FSNE' for 'Full Software Native Encryption'): • Support
    encryption natively inside OXE, for signaling and media … Software-based solution; zero hardware
    footprint: • Activation of this feature is managed via the configuration of the OXE database •
    Presence of software licenses is also essential" (p62)
  definition: |
    全书主题：OXE 内原生支持信令（DTLS/TLS 1.2/IPSec）与媒体（SRTP）加密的纯软件能力，零硬件
    footprint；激活=OXE 数据库配置+软件许可（#424/#359）；兼容 OXE 高可用、仅 IPv4 设备、可选 mTLS。
    定位为从"大客户可选件"转向"全客户原生基线"（p61），与 IP Premium Security 旧方案互不兼容。
  alias_or_related: 加密由 Call Server 强制（p65）；按用户"部分加密"见 g09
  tags: [concept, core, encryption]

- id: g02
  term: EGW (Encryption Gateway)
  category: concept
  source_pages: p76-77, p87
  source_quote: |
    "Encryption gateway (EGW) (CS and PCS) • Component handling DTLS signaling encryption • Acts as
    interface for endpoints instead of IPLink • Can be embedded in the Call Server or external …
    Other flows don't transit via EGW (e.g. TFTP …)" (p76)
  definition: |
    处理 DTLS 信令加密的软件组件，是 DTLS 兼容端点的 DTLS 服务器（端点为客户端，各建永久会话）；
    内嵌于 CS/PCS（冗余时每 CS 一个）。只承载 DTLS 信令——TFTP 等其它流不经它；全部配置在 CS 完成。
    判别口径：WBM 的 IP/Encryption GW 菜单里 EGW IP=CS IP 即内部 EGW（只读展示，p126）。
  alias_or_related: 外部形态见 g03 EEGW；容量分界 1500（p77/p109）
  tags: [concept, core, dtls]

- id: g03
  term: EEGW (External Encryption Gateway)
  full_name: External Encryption Gateway（书中 p77 语境展开）
  category: concept
  source_pages: p77, p199-203, p211-213
  source_quote: |
    "External Encryption Gateway (EEGW) • External Virtual Machine mandatory • OXE redundancy: one
    dedicated EEGW per Call Server • Includes the SIP Translator (NSP) • Virtualization of OXE
    mandatory" (p200)
  definition: |
    外部加密网关：>1500 会话场景的必需形态（1500-15000 会话），强制部署为虚拟机（OST 软件包，
    Rocky Linux），每台 CS 一台，VM 内含 SIP Translator（NSP）；要求 OXE 自身虚拟化、CS 与其 EEGW
    同物理主机同虚拟交换机；CS-EEGW 间专用明文 UA/UDP 链路兼做存活监控，断链则 CS 重启；EEGW IP
    在 lanpbxbuild 里作为 DTLS 服务器管理。PCS 亦可外接 EEGW（PCS EGW IP 参数：等于 PCS IP=内嵌、
    不同=外接，p213）。
  alias_or_related: 承载包名 OST（g05）；内含 NSP（g04）；容量公式见 principle p09
  tags: [concept, core, gateway, capacity]

- id: g04
  term: SIP Translator (NSP)
  full_name: NSP = Nginx SIP Proxy（书中 p76 展开）
  category: concept
  source_pages: p76, p202, p247, p266-267
  source_quote: |
    "SIP Translator (NSP: Nginx SIP Proxy) as alternative • Embedded in the External EGW" (p76)
    "Entry point for any SIP TCP or SIP TLS connection to the Call Server (SIP endpoints, SIP
    trunking, SIP application, …)" (p202)
    "Translator Name :nsp • Translator FQDN :nsp.oxe.company.com" (p247)
  definition: |
    SIP 翻译器：与 EEGW 同 VM 的组件（OST 软件包），一切 SIP TCP/TLS 连接（SIP 端点/中继/SIP 应用）
    的入口点；名字叫"翻译器"实为 Nginx SIP 代理（TLS 卸载）。仅外部 EGW 场景强制声明（<1500 会话
    内嵌 EGW+sipmotor 即可，p247）；FQDN=名字+OXE 域（nsp.oxe.company.com），由 OXE 内部 DNS 按冗余
    角色解析（仅主 CS 应答→返回主 CS 的 EEGW IP）；冗余场景 SBC 侧必须用 NSP FQDN。SIP UDP 端点仍
    直连 CS 不经它（p202）。
  alias_or_related: 声明菜单 netadmin 19.2；改名须重生成 CS 证书+重启（p247）
  tags: [concept, core, nsp, proxy]

- id: g05
  term: OST (OXE Signaling Translator)
  full_name: OXE Signaling Translator（书中 p209 展开）
  category: concept
  source_pages: p201-202, p209, p235, p276
  source_quote: |
    "OST (OXE Signaling Translator) software package" (p201)
    "'EEGW' VM loading by using S.O.T. • Rocky Linux OS • OST software package • Machine type
    selection • EEGW / OST64" (p209)
  definition: |
    EEGW 虚拟机的软件包名（装于 Rocky Linux，机器类型 EEGW/OST64，S.O.T. 生成）；配置命令 ostconfig
    （IP/掩码/网关/CS 物理/角色地址、下载证书、证书核对）；S.O.T. 部署的 VM 首次登录 root/letacla1
    （Rocky 9.7，p278-279）。OST/EEGW/NSP 三个词指同一台 VM 的三个侧面：包名/网关角色/代理进程。
  alias_or_related: 状态查询 config ost、日志 ost_importlog（p242-243）
  tags: [concept, eegw, package]

- id: g06
  term: CTL (Certificates Trust List)
  full_name: Certificates Trust List（书中 p4/p24 展开）
  category: concept
  source_pages: p24-25, p79-80, p124, p363
  source_quote: |
    "Chain of trust known as CTL (Certificates Trust List) • Depending on the CA structure, it
    comprises the root certificate and, if present, one or more intermediate level certificate" (p24)
    "CTL basically is an SSL certificates chain including the Root CA certificate of CA in a single
    file … a file containing the concatenation of all trusted CA certificates in PEM format • OXE
    supports up to 5 levels of CA hierarchy" (p79)
  definition: |
    受信 CA 证书链单文件（PEM 拼接，含 Root CA 及中间级，最多 5 级层级），存于端点/CS 的 trust
    store，用于验证对端（CS、EEGW、SBC）证书。分发两法：lanpbx.cfg 自动推送（DTLS 设备；SIP 设备
    经配置文件给路径，p80）或手工预置；lanpbx.cfg 里的字段名 DTLS_CERT_TRUST（p124）。CS 侧端点 CTL
    管理菜单 netadmin 11.9.3（导入/查看/删除，p363）；OXE 侧还预置 ALE 出厂根 CA（ALE_CTL.pem，p376）。
  alias_or_related: 首次获取走 TOFU（g07）；文件实体 /etc/pki/oxe/truststore/trustchain.pem（p191 Tips）
  tags: [concept, core, trust]

- id: g07
  term: TOFU
  full_name: Trust On First Use（书中 p80 展开）
  category: concept
  source_pages: p80, p74, p108
  source_quote: |
    "First CTL acquisition is done in 'trust on first use' (TOFU) mode. TOFU principle consists in
    accepting that a factory-state endpoint, or more generally an endpoint whose trust store is still
    empty, can establish its very first connection with a protected PBX without verifying the server
    certificate. Subsequent connections are then fully authenticated based on the stored CTL." (p80)
  definition: |
    首次信任机制：出厂/空信任库的端点第一次连接受保护 PBX 时不验证服务器证书，之后按存储的 CTL 全量
    认证。客户拒绝 TOFU 时走手工 CTL 预置（逐台导入或 SCEP/EST，p80）。安全下载场景 TOFU 激活时 OXE
    CTL 亦经 lanpbx.cfg 自动获取（p74）。设备需回到 TOFU 模式的唯一办法是恢复出厂（p108）。
  alias_or_related: 与 g06 CTL 配套；factory reset 操作 i+#（p108）
  tags: [concept, trust, security]

- id: g08
  term: Mutual Authentication (mTLS)
  category: concept
  source_pages: p82-83, p165-166, p364, p377
  source_quote: |
    "If 'mTLS' is enabled (optional; activated by configuration), OXE ('EGW' / 'sipmotor') requests
    for the end point's certificate during DTLS/TLS handshake and verify it with the CA in its trust
    store. The identity of the certificate owner is verified by comparing the certificate asserted
    identity and the MAC address advertised by the endpoint" (p82)
  definition: |
    双向认证：OXE 在 DTLS/TLS 握手时反向索取并验证端点证书，证书身份与端点首个信令消息宣告的 MAC
    地址比对。启用范围：DTLS 端点全局、SIP TLS 扩展全局、SIP trunk 按外部网关；激活后所有话机/
    软话机（含明文用户）都须有证书、首连总是加密；主备 CS 间 DTLS 强制 mTLS（p91）。版本要点：
    默认 SSL level 2 要求 ≥2048 位证书（N3 起 OpenSSL 3.0，p366）。
  alias_or_related: 参数 Enable Mutual TLS Authentication / SIP TLS Mutual Authentication；端口模型 5061/6261
  tags: [concept, core, mtls]

- id: g09
  term: Partial encryption
  category: concept
  source_pages: p66
  source_chapter: SECURITY ENFORCED BY THE CALL SERVER
  source_quote: |
    "Flexibility for IP NOE and SIP extensions with the 'partial encryption' • User option « Native
    Encryption » to enable/disable encryption per DTLS/TLS capable IP user • Use case 1: only a
    limited set of sensitive users has to be secured (licenses) • Use case 2: the customer has a mix
    of DTLS/TLS compatible equipment's and previous ranges"
  definition: |
    按用户灰度加密：每个 DTLS/TLS 能力端点用用户选项"Native Encryption"逐台开关；两个用例=仅保护
    敏感用户（许可受限）、新旧话机混存的过渡。CS 在每次设备连接后核对；切换模式需话机重启；DSS/DSU
    与 ProACD/agent 上下文必须同质配置。
  alias_or_related: 许可口径见 License #424；IPMG/PCS 不参与灰度（恒加密，p65）
  tags: [concept, enforcement]

- id: g10
  term: lanpbx.cfg
  category: concept
  source_pages: p121-125, p230-233, p256
  source_quote: |
    "DTLS_CERT_TRUST Certificate Trust List (CTL) in a PEM format. The CTL is automatically included
    to the file when the 'Enable Automatic CTL Acquisition' parameter is set to True in OXE
    configuration. … DTLS_SIGN_FILE Digital signature of the 'lanpbx.cfg' file, computed with the
    private key associated to the server certificate." (p124)
  definition: |
    OXE IP 配置文件（/usr3/mao/lanpbx.cfg）：NE 开启后注入 DTLS 参数（DTLS 开关、DTLS_SRV/RD、
    DTLS_PORT 默认 32643、OXE_FQDN、DTLS_CERT_TRUST=CTL、DTLS_SIGN_CERT/FILE 及 _ALT 旧证书旧签名）
    并由系统签名后下发——它是端点侧的信任载体而不仅是下载配置。生成工具 lanpbxbuild；PCS 与主 CS
    共用同一份；duplication 必须在 main 生成（自动产出 lanpbxtwin.cfg 同步）。
  alias_or_related: 工具见 lanpbxbuild（product 类）；字段表见 principle p18
  tags: [concept, core, configuration]

- id: g11
  term: Factory certificate
  category: concept
  source_pages: p78, p83, p370-371
  source_quote: |
    "Customer certificate or factory certificate • Factory certificate only for GD4, GA4, GD-XL &
    GA-XL boards, deskphones and IP-xBS • By the end of 2025, any newly produced board will embed a
    default ALE certificate" (p78)
    "Nothing to do: • 'Factory certificates' are embedded by default in the sets. • And the sets CTL
    (Alcatel RootCA certificates) is already present in the OXE trust store." (p371)
  definition: |
    出厂预置证书：仅 GD4/GA4/GD-XL/GA-XL 板卡、话机与 IP-xBS 携带；板卡工厂证书自 OXE R101.1 MD4
    起可用（低版本部署不报错但用不了）；2025 年底起新产板卡默认内嵌 ALE 证书。话机用工厂证书时
    "无操作"——ALE 根 CA 的 CTL 已预置在 OXE 信任库（ALE_CTL.pem：Alcatel Enterprise Solutions/
    Alcatel IP Touch/AIPT 1-4/Wired Phones/Enterprise Wireless Terminals，p376）。mgconfig 菜单另
    有 Resynchronize factory certificates 项（p368）。
  alias_or_related: 定制证书对照（End Entity、CN=MAC，见 g12 与 p344/p348）
  tags: [concept, certificate]

- id: g12
  term: End entity / CN=MAC 约定
  category: concept
  source_pages: p344, p348, p356, p399
  source_quote: |
    "Take Care, 'Common Name' for 'OMS' end entity must match it's MAC address (as for end entities
    such as GD4/GD3/GA4/GA3/INTIP3 board, IP NOE Deskphones…)" (p344)
    "Take Care, 'Common Name' of end entity must match: • OXE FQDN (node name+domain) for call
    server(s) and for a passive call server (PCS) • The end entity MAC address for a GD3/GA3/INTIP3
    board, for NOE3G EE & 80x8s terminals" (p399)
  definition: |
    端点实体证书的命名约定：板卡（GD3/GD4/GA3/GA4/INTIP3）、IP NOE 话机、IPDSP 软话机的实体证书
    Type=End Entity 且 CN=设备 MAC 地址；CS/PCS 证书 CN=OXE FQDN（节点名+域）。XCA 制作时的固定
    检查项；mTLS 握手时 CS 以 MAC 比对证书身份。
  alias_or_related: IPDSP 的 MAC 在其设置 Network 页 phone identifier 查看（p348）
  tags: [concept, certificate, naming]

# ── 二、账户与角色 (role) ──

- id: g13
  term: mtcl
  category: role
  source_pages: p34, p113, p121, p129-131
  source_quote: |
    "In the 'Terminal' window of the OXE Log as 'mtcl' Switch to root, by using 'su' command" (p113)
  definition: |
    OXE 维护账户（全书未展开全称）：绝大多数日常操作与验证命令（netadmin 切 root 前的登录、
    lanpbxbuild、ippstat、twin、cryptview、sipregister、csipsets、sipextgw、motortrace、pcscopy、
    hybvisu）都在 mtcl 下执行；实验口令 Superuser2580*（实验口径）。
  alias_or_related: 与 g14 root、g15 swinst 并列的三个 OXE/Linux 账户
  tags: [role, account, oxo]

- id: g14
  term: root
  category: role
  source_pages: p34, p107, p113, p191, p220, p363
  source_quote: |
    "Run 'netadmin -m' command … (Logged in as root)" (p150)
    "Enter 'root' account password" (p113)
  definition: |
    Linux 超级用户账户（全书未展开——即 Unix 惯例 root）：证书导入/导出、端点 CTL 导入、内部防火墙、
    SSL security level、openssl 命令行与格式转换脚本等敏感操作要求 su - root（从 mtcl 切换）；实验
    口令 Superuser2580*（实验口径）。spadmin/证书导出原书标注用 root 账户（p107）。
  alias_or_related: EEGW VM 的 root 初始口令为 letacla1（p279，须首登即改）
  tags: [role, account, linux]

- id: g15
  term: swinst
  category: role
  source_pages: p34, p107, p133, p237
  source_quote: |
    "Back up Linux Data ('swinst')" (p107)
    "!!!Provide the swinst password of associated call server to perform ssh-copy-id" (p237)
  definition: |
    OXE 软件安装账户（全书未展开全称）：Linux Data 备份走 swinst（备份会自动带上证书，p133 Tips）；
    EEGW 从 CS 下载证书时经 ssh-copy-id 提供 swinst 口令（p237）；实验口令 Superuser2580*（实验
    口径）。
  alias_or_related: 备份方案之二（方案一为 netadmin 证书导出）
  tags: [role, account, backup]

- id: g16
  term: CA Administrator (trainer)
  category: role
  source_pages: p115, p149, p179, p381
  source_quote: |
    "You have to wait that the CA administrator (the trainer) validates (issues) your certificate
    request." (p115)
    "IF YOU ARE USED TO A SPECIFIC EXTERNAL 'CA', DON'T HESITATE TO WORK WITH IT IN ORDER TO GENERATE
    CERTIFICATES" (p381)
  definition: |
    实验/生产中的证书签发方角色：实验里由 trainer 充当外部 CA（XCA）管理员，负责签发 CSR、下发
    .p7b/.cer 证书；生产中对应客户企业 PKI 的 CA 运营方。原书立场：客户已有外部 CA 就用客户的，
    XCA 只是教学替身。
  alias_or_related: XCA 见 product 类 g36；签发流程见 c02/c09/c17/c19
  tags: [role, ca, trainer]

# ── 三、许可 (subscription) ──

- id: g17
  term: License #424 (Native Encryption Users)
  category: subscription
  source_pages: p109, p129
  source_quote: |
    "License#424: defines the numbers of DTLS/TLS sessions allowed within the system … 424 – Native
    Encryption Users" (p109)
    "424   Native Encryption Users             =             75" (p129，实验口径)
  definition: |
    原生加密软件许可：定义系统内允许的 DTLS/TLS 会话总数（受保护端点+板卡/网关/节点折算，见容量
    公式）。用 spadmin（option 2）查看；实验环境授权值 75（实验口径）。会话计数由 Actis 系统级
    计数器管理（无按 PCS 计数）；EEGW 场景需人工报价。
  alias_or_related: 与 g18 #359 并列；容量分界 1500/15000
  tags: [subscription, license, capacity]

- id: g18
  term: License #359 (SIP Encryption Trunks)
  category: subscription
  source_pages: p109, p129
  source_quote: |
    "License#359: defines the maximum number of simultaneous SIP TLS communications … 359 - SIP
    Encryption Trunks" (p109)
    "359   Max com simultaneous SIP TLS        =             30" (p129，实验口径)
  definition: |
    SIP 加密中继许可：定义系统并发 SIP TLS 通信数上限。实验环境授权值 30（实验口径）。与 #424 分属
    两个计数维度（中继方向 vs 端点/系统方向）。
  alias_or_related: 查看命令 spadmin（p129）
  tags: [subscription, license, sip-tls]

# ── 四、产品/组件/工具 (product) ──

- id: g19
  term: OmniPCX Enterprise (OXE) — CS / PCS
  category: product
  source_pages: p1, p62-64, p91-92
  source_quote: |
    "Call Servers (CS & PCS), as well as equipment (IPMG, IP Phone, SIP SEPLOS…) come with TLS/DTLS
    encryption software capability" (p62)
    "Secured components Call Server (CS-3, CPU8, GAS, OXE-V) Passive Call Server (CS-3, GAS, PCS-V)"
    (p64)
  definition: |
    本书主角：ALE 企业级通信服务器（书名主角，R101.2 时代）。CS（Call Server）承载呼叫处理与全部
    加密组件（EGW/CA/SIPmotor/IPSec Manager）；PCS（Passive Communication Server）为分支救援服务
    器——CS 失联后端点切换到 PCS，PCS 与 CS 同 CA 异证书、端点须先连过 CS 才能被救援；受保护的
    CS 硬件形态：CS-3/CPU8/GAS/OXE-V（被动侧 CS-3/GAS/PCS-V）。
  alias_or_related: 冗余行为见 p89/p91；实验 VM 名 ENTP_OXE_FSNE_CSA/CSB、ENTP_OXE_FSNE_NODE_1/2
  tags: [product, pbx, core]

- id: g20
  term: OMS
  category: product
  source_pages: p52, p147, p288-289, p356-359
  source_quote: |
    "Software Rack 3U (OMS) Rack N° 4 Virtual GD4 (slot 0) IP @: 192.168.1.13/24" (p52)
    "[root@oms ~]# sudo omsconfig … Board role OMS" (p147)
  definition: |
    承载虚拟 GD4 板卡的软件机架/VM（全书未展开全称）：实验中即 ENTP_OMS_* VM（主站点 192.168.1.13、
    远端 192.168.2.13、Node2 192.168.1.113），配置工具 omsconfig（IP/板卡号/下载协议/SSH/证书管理）。
    mTLS 场景经 omsconfig 导入 GW.pfx 实体证书（CN=OMS MAC）；切换拓扑时要清除旧信任库证书。
  alias_or_related: 证书管理子菜单：打印/导入 CTL/导入网关证书/清除/EST 配置（p358）
  tags: [product, ipmg, vm]

- id: g21
  term: IPMG 家族（GD4/GA4/GD-XL/GA-XL/GD3/GA3/INTIP3/OXE-MS）
  category: product
  source_pages: p63-64, p72, p74, p77, p129, p367
  source_quote: |
    "GD4, GD3, GD-XL, INTIP3, OXE-MS • Built-in DTLS & SRTP • Security enforced by Call Server •
    Factory or custom certificates • Initialization: HTTPS instead of TFTP" (p63)
    "Compatible components: GD4, GA4, GD-XL, GA-XL and OXE-MS • Older VoIP boards, as GD3, INTIP3,
    etc … still rely on TFTP protocol" (p74)
  definition: |
    IP 媒体网关家族：GD4/GA4/GD-XL/GA-XL（新代板卡，GA 系经背板继承 GD 系选择）、GD3/GA3 与 INTIP3
    （老代，HTTPS 下载与部分新特性受限）、OXE-MS（软件网关）。能力差异：SRTP AES-256 支持=GD4/
    GD-XL/OXE-MS/INTIP3（INTIP3 自 R101.1 MD4），GD3 禁用；工厂证书=GD4/GA4/GD-XL/GA-XL；会话计数
    每块 ×3；配置工具 mgconfig（板卡，V24 串口登录）。
  alias_or_related: 压缩器上限 AES-256 下 GD4/GD-XL 45、INTIP3 30（p72）
  tags: [product, ipmg, hardware]

- id: g22
  term: IPDSP
  category: product
  source_pages: p34, p52-53, p127-128, p360-362
  source_quote: |
    "31000 Brad Barkley IP DSP Main Installed on PC Client 10" (p52)
    "There are 2 different ways for an IP Desktop Softphone to accept the OXE certificate…" (p127，
    正文以 "IP Desktop Softphone" 称呼该应用)
  definition: |
    PC 软话机应用（实验中占分机 31000/31002/31003/31500；全书以缩写 IPDSP 为主、正文称 IP Desktop
    Softphone 应用）：设置里指定 TFTP（主 CS IP）；接受 OXE 证书两法（PC 信任库装根 CA→无提示，或
    连接时弹窗 Accept permanently）；CTL/配置落盘目录 %appdata% 下 Roaming…\PBX_CTL\<OXE IP> 与
    Local…\config（p128）；mTLS 证书两法（安装目录 softphone_cert.pem/softphone_pkey.pem + 
    DTLSPkeyPassphrase.exe，或 Windows 证书库 + DTLS_CERT_NAME，p360-362）；只工作在 SRTP 认证模式
    （p119）。
  alias_or_related: SRTP AES-256 在 Android 版不支持（p70）
  tags: [product, softphone]

- id: g23
  term: ALES
  category: product
  source_pages: p52-54, p88, p142
  source_quote: |
    "ALES softphone (PC, Android, iOS)" (p63)
    "31030 Elliot Evans ALES Main Installed on PC Client 10" (p52)
  definition: |
    ALE 软话机（PC/Android/iOS，全书未展开全称）：SIP TLS 扩展加密的主力实验终端（SEPLOS 模式，
    盾牌图标显示加密）；安装时指定 local access（CS main IP），登录用用户凭据（eevans/eeastwood，
    实验口径）。SRTP AES-256 兼容（p70）。
  alias_or_related: 与 IPDSP（NOE 侧软话机）并列
  tags: [product, softphone, sip]

- id: g24
  term: OTSBC (OT-SBC)
  category: product
  source_pages: p55, p90, p160, p173-184
  source_quote: |
    "SRTP on the LAN part requires TLS transport mode between OT-SBC and OXE" (p90)
    "Connect to the OTSBC 'WebAdmin' interface (URL= 'https://IP@ of the SBC')" (p175)
  definition: |
    ALE 会话边界控制器（SIP trunk 实验的运营商侧边界 VM，ENTP_SBC_FSNE）：WebAdmin 管理界面配置
    TLS context/证书/Proxy Set/Media Security/IP Profile（见 c06）；与 OXE 两侧端口成对（Proxy Set
    5061/6261 ↔ SIP Interface TLS 端口）；实验登录 Admin/Admin（实验口径）。
  alias_or_related: 远程工作者场景 SBC IP 需录入 OXE 库（≤10 个，p90）
  tags: [product, sbc, sip-trunk]

- id: g25
  term: 4645 Voice Mail (4645 VM)
  category: product
  source_pages: p63-64, p95
  source_quote: |
    "4645 Voice Mail is automatically secured when it is hosted in an OXE where native encryption is
    activated • Only one system parameter to activate • 'System/Other System Param./Voice Mail
    Parameters'" (p95)
  definition: |
    语音信箱（内置 A4645 组件经 libsrtp 直接管 SRTP，支持以太网冗余）：宿主于开了 NE 的 OXE 内时
    自动受保护（仅一个系统参数）；独立服务器部署需改 eva.cfg 加 DTLS 参数+专用证书（IP 入 SAN）。
    注意：明文话机呼叫受保护 VM 时话音 RTP 不加密。
  alias_or_related: SRTP AES-256 兼容应用之一（p70）
  tags: [product, voicemail]

- id: g26
  term: OmniPCX Record (OPR)
  category: product
  source_pages: p63-64, p97, p304
  source_quote: |
    "Encryption of CSTA link between Call Server and OPR • Allows to transmit securely SRTP keys to
    OPR via CSTA • TLS 1.2 mandatory • Certificate-based authentication • No mutual authentication •
    Only the Call Server (acting as TLS server) is authenticated" (p97)
  definition: |
    录音服务器（正文同段以 OmniPCX Record 与 OPR 混称）：经 IP DR-Link 场景与 CS 间 CSTA 链路 TLS
    1.2 加密（仅认证 CS），SRTP 密钥经 CSTA 安全下发；录音能力（明文/AES-128/AES-256）由 Recording
    SRTP Cipher Suite 参数决定；每次保持/会议/转接换新钥，收到的音频流即时解密。
  alias_or_related: 与 TDM DR-Link 同列受保护特性（p64）
  tags: [product, recording]

- id: g27
  term: VAA
  category: product
  source_pages: p63-64, p98
  source_quote: |
    "Encryption of the SIP link between Call Server and VAA • Native SIP TLS for private SIP trunk
    (internal 'ABC-F' type) … The maximum number of VAA ports is decreased from 120 to 60 in case of
    encryption" (p98)
  definition: |
    语音应用服务器（全书未展开全称）：与 CS 间 SIP 链路走 Native SIP TLS（internal ABC-F 型）+
    SRTP（AES-128/256 均可）；OXE CTL 手工导入 VAA 信任库，可选 mTLS（VAA CTL 导入 OXE）；加密后
    端口上限 120→60；兼容 OXE 冗余与 PCS 本地 VAA。
  alias_or_related: 对照 g28 DC（端口不受影响）
  tags: [product, application]

- id: g28
  term: Dispatch Console (DC)
  category: product
  source_pages: p63-64, p99
  source_quote: |
    "Encryption of the SIP link between Call Server and DC • This private SIP trunking is using
    internal ABC-F type … No impact on the maximum number of DC ports, which remains at 120" (p99)
  definition: |
    调度台（全书未展开全称）：与 VAA 同路径的 SIP TLS（internal ABC-F 型）+可选 mTLS（双向导 CTL）；
    SRTP AES-128/256 均可；端口数不受加密影响（保持 120）；其 conferencer（会议组件）管理的会议同受
    保护；话务员设备可按普通设备加密（需机型兼容+开用户加密参数）。
  alias_or_related: 与 VAA 并列为"SIP 应用中仅有的两个受保护应用"（p64）
  tags: [product, application]

- id: g29
  term: IP-xBS
  category: product
  source_pages: p63, p65, p70, p83, p366
  source_quote: |
    "IP-xBS DECT base stations • Built-in DTLS / SIP-TLS & SRTP • Factory or custom certificates" (p63)
    "For IP-xBS infrastructure, the encryption capability activation is common to all base stations"
    (p65)
    "IP-xBS from OXE R101.2 MD2"（AES-256 兼容版本，p70）
  definition: |
    DECT 基站（全书未展开全称）：内置 DTLS/SIP-TLS 与 SRTP；加密激活对所有基站统一生效（系统参数
    Enable IPxBS Native Encryption，cryptview 可见，p131）；证书经 HTTPS（8378 的 WBM）或 SFTP 导入、
    CTL/证书可走 EST 自动注册；SRTP AES-256 自 R101.2 MD2、无 IP SAN 证书不兼容（p85）。
  alias_or_related: 8378 DECT IP-xBS / 8328 SIP-DECT 的 1024 位出厂证书是 N3 后 mTLS 断裂点（p366）
  tags: [product, dect]

- id: g30
  term: Rainbow WebRTC Gateway
  category: product
  source_pages: p63-64, p94
  source_quote: |
    "Encryption between OXE and the gateway • SIP signaling always encrypted • Audio encrypted only
    if the OXE endpoint is secured • Certificate based authentication • No mutual authentication •
    Only gateway authentication (Rainbow gateway acting as TLS server)" (p94)
  definition: |
    Rainbow 云协作的网关组件（OXE 侧对接）：SIP trunk 组用 "SIP-ISDN mode" + Rainbow 变体外部 SIP
    网关；信令恒加密、音频仅端点受保护时加密；仅网关侧认证（Rainbow 网关为 TLS 服务器）；加密非
    强制可明文运行。
  alias_or_related: 应用生态（4645/O2G/VAA/IP DR-Link/DC）并列表（p63）
  tags: [product, rainbow]

- id: g31
  term: FlexLM
  category: product
  source_pages: p34, p52
  source_quote: |
    "FLEXLM SERVER ENTP_FLEXLM Flex 192.168.1.80 … root letacla1" (p34)
    "FlexLM Server (192.168.1.80) is declared." (p52)
  definition: |
    软件许可服务器（实验 VM，192.168.1.80，root/letacla1 实验口径）：OXE 预配置即声明；CC-suite-ID
    （内嵌 CA 的 Root CA CN）须存在于许可文件（p311）——许可体系是原生加密激活的两要素之一。
  alias_or_related: 许可条目见 g17/g18；CC-suite-ID 见 p11 内嵌 CA 口径
  tags: [product, licensing]

- id: g32
  term: XCA
  category: product
  source_pages: p335-353, p380-403
  source_quote: |
    "'XCA' is a tool for certificate and key management. For further details, go to the
    'https://hohnstaedt.de/xca' website" (p335)
  definition: |
    开源证书与密钥管理工具（书中外部 CA 的教学替身）：装 Windows（setup.exe），建口令保护的数据库，
    管私钥/证书/CSR——根 CA 自签、端点实体（End Entity、CN=MAC 或 FQDN）、CSR 导入签发、导出 PEM/
    PKCS7/PKCS12；原书立场：客户已有 CA 就用客户的（p381）。
  alias_or_related: 操作流程见 c17/c19；根 CA 证书格式转换 conv-proper-p7-format.pl/openssl（p389-390）
  tags: [product, ca, tool]

- id: g33
  term: S.O.T.
  full_name: Software Orchestration Tool（书中 p272 章题展开）
  category: product
  source_pages: p272-282
  source_quote: |
    "Software Orchestration Tool OST/EGW generation & loading with S.O.T. deployment tool • Generate
    an OST/EGW virtual machine (.ovf) with S.O.T." (p272)
  definition: |
    ALE 部署工具（Web 界面，仅 Chrome/Firefox）：Greenfield 工程→选产品 OST→上传 BootDVD/OST 媒体
    （FTP upload/sot）→机器类型 EEGW/主机名/Sizing/IP→Deploy 生成 .ovf→下载 .ova→ESXi 部署→VM
    自动加载。实验 VM 地址 https://192.168.1.194（admin/Superuser2580*，实验口径）。
  alias_or_related: 首登 letacla1 改密；后续配置 ostconfig
  tags: [product, deployment, sot]

- id: g34
  term: ITSP2 / MicroSIP（SIP 模拟器）
  category: product
  source_pages: p35, p42-46
  source_quote: |
    "SIP SIMULATOR OVERVIEW – ITSP2 SIP GATEWAY … ITSP2 SIP Gateway gateway.itsp2.com 10.20.30.60"
    (p43)
    "2 MicroSIP softphones are installed to simulate public numbers." (p35)
  definition: |
    培训专用 SIP 运营商模拟器（托管 RLAB 公共区）：SIP 网关 gateway.itsp2.com（10.20.30.60）+公网
    网关 public.itsp1.com（10.20.30.50，两个 MicroSIP 软话机模拟 Public/Urgence 用户，紧急号
    112/15/17/18）；PBX 注册账号 podP/alcatel；章内 ITSP1/ITSP2 命名混用为原书现象。纯教学基础设施。
  alias_or_related: 号码规则与变换见 f04；生产 SIP 对接行为与模拟器有差异
  tags: [product, lab, sip]

- id: g35
  term: netadmin
  category: product
  source_pages: p101, p104, p113-118, p149-153, p219-221, p246-247, p267-268, p363, p366
  source_quote: |
    "Certificate Authority, certificates and CTL management via netadmin OXE CLI tool • Embedded CA
    activation, certificate creation, CSR generation, certificate import/export, CS's CTL export,
    endpoint's CTL import, … • Leverage OpenSSL Certificate Management Tools" (p101)
    "11.9.1.CS Certificate management … 11.9.2.PCS Management … 11.9.3.Endpoint CTL (Trust Store) …
    20.Encryption GW Management … 19.2.Translator Name configuration"（各实验章输出）
  definition: |
    OXE 命令行管理工具（netadmin -m 菜单树）：11.1.3 受限访问（内部防火墙）、11.6.3 SSL security
    level、11.9.1 CS 证书管理（8 个子项）、11.9.2 PCS 管理、11.9.3 端点 CTL、17 Node setup（内部
    DNS）、19 域管理（域名/Translator 名）、20 EGW 管理、10 Copy setup（twin 同步）、2 当前配置查看；
    底层借力 OpenSSL。是证书全生命周期的主操作面。
  alias_or_related: 菜单号即实验导航坐标（BOOK_OVERVIEW f22）
  tags: [product, cli, certificate]

- id: g36
  term: lanpbxbuild
  category: product
  source_pages: p121-123, p230-232, p256, p372-374
  source_quote: |
    "First, you can use 'lanpbxbuild -auto' to create the file. It will be located in '/usr3/mao'"
    (p121)
    "1. View 2. Add 3. Delete 4. Modify 5. Move 6. Apply changes 7. Copy lanpbx to lanpbx-mipt 0.
    Quit" (p122)
  definition: |
    lanpbx.cfg 生成/维护工具（mtcl 命令行）：-auto 一键建文件（重置 IP_CPU/IP_DOWNLOAD 外的配置）；
    交互菜单 4→Modify 里 j/k=DTLS 1/2 IP、l=DTLS 端口、n=OXE FQDN、d/e/f=dot1x 证书服务器
    （CERTSRV，复用于话机证书下发）、i=https 服务器；6=Apply changes（重签 CTL+lanpbx 签名）；
    duplication 必须在 main CS 运行。
  alias_or_related: 产出双文件 lanpbx.cfg + lanpbxtwin.cfg（p121 Warning）
  tags: [product, cli, configuration]

- id: g37
  term: ostconfig / omsconfig / mgconfig
  category: product
  source_pages: p147, p235-238, p258-260, p279-280, p288-289, p357-358, p367-369
  source_quote: |
    "Hit the command: 'ostconfig' … 11. Download Certificates 12. Certificate check" (p235)
    "[root@oms ~]# omsconfig … 8. Certificate management" (p147/p289)
    "# mgconfig … 12. Certificate management" (p367)
  definition: |
    三类网元配置工具：ostconfig（EEGW/OST VM：IP/CS 地址、下载证书、证书核对、SSH）；omsconfig
    （OMS VM：IP/板卡号/下载协议 TFTP/SSH/证书管理——导入 GW.pfx、清信任库）；mgconfig（GD3/GD4/
    INTIP3 板卡：同构菜单，V24 串口登录，另有 Resynchronize factory certificates）。三者都有
    "Certificate management" 子菜单（打印/导入 CTL/导入网关证书/清除/EST）。
  alias_or_related: 板卡 SSH 临时开放须告知客户并事后撤销（p357）
  tags: [product, cli, tools]

# ── 五、协议与技术 (protocol) ──

- id: g38
  term: DTLS 1.2
  full_name: Datagram Transport Layer Security（书中 p67 展开）
  category: protocol
  source_pages: p63, p67, p87
  source_quote: |
    "'DTLS 1.2' between OXE CS and others equipment's: IP Media gateways, CS (Main/Stand-by, PCS),
    ALE Essential & Enterprise Deskphones, IP-DSP , DECT IP-xBS base stations… • Stands for 'Datagram
    Transport Layer Security' • Handled by 'Encryption Gateway' module (embedded in OXE or hosted in
    a VM) • RFC 6347, RFC 5246" (p67)
  definition: |
    NOE 侧信令加密协议（RFC 6347/5246）：CS 与媒体网关、主备 CS、PCS、Essential/Enterprise 话机、
    IPDSP、IP-xBS 之间；由 EGW 组件承载（内嵌或外部 VM）；默认端口 32643。端点为 DTLS 客户端、
    EGW 为服务器。
  alias_or_related: 会话计数与 TLS 合并计（#424）
  tags: [protocol, dtls]

- id: g39
  term: TLS 1.2 (SIP TLS)
  full_name: Transport Layer Security（书中 p67 展开）
  category: protocol
  source_pages: p67, p88, p160
  source_quote: |
    "'TLS 1.2' for SIP Extensions (SEPLOS) and for SIP trunking encryption • … Handled by 'sipmotor'
    internal OXE process or by SIP translator module (hosted on a VM) • RFC 5246" (p67)
    "Support TLS 1.2 only • Authentication based on SHA-2 certificates (RSA key length from 2048
    till 4096 bits)" (p160)
  definition: |
    SIP 侧信令加密协议（RFC 5246）：SIP SEPLOS 扩展与 SIP trunking；由 sipmotor（CS 内嵌进程）或
    SIP Translator/NSP 承载；端口 5061（服务器认证）/6261（互认证，可配）；仅 TLS 1.2、SHA-2 证书、
    RSA 2048-4096 位；cipher suite 两条 ECDHE-RSA-AES-GCM（p68/p160）。
  alias_or_related: SIP TLS with SSM 与 NE SIP TLS 互斥（p159）
  tags: [protocol, tls, sip]

- id: g40
  term: SRTP
  full_name: Secure Realtime Transport Protocol（书中 p69 展开）
  category: protocol
  source_pages: p63, p69-72, p161
  source_quote: |
    "SRTP : Secure Realtime Transport Protocol • SRTP defines a Real-time Transport Protocol (RTP)
    profile, which aims to provide confidentiality …, authentication and message integrity" (p69)
    "AES-CM-128-HMAC-SHA1-80 or AES-256-CM-HMAC-SHA1-80 (via system parameter SRTP Cypher Suite)" (p70)
  definition: |
    媒体加密协议：AES-CM-128/256-HMAC-SHA1-80 两档（系统参数二选一、不混用）；密钥每方向一把、
    由 CS（NOE/IPMG）或 SIP 端点生成、经加密信令下发；AES-256 有硬件/版本代价（GD3 禁用、压缩器
    降额、IP-xBS 自 R101.2 MD2）。录音/网关/应用全兼容清单见 p70。
  alias_or_related: SRTCP 模式随 SRTP offer answer 参数 RFC/THALES（p190）
  tags: [protocol, srtp, media]

- id: g41
  term: IPSec
  full_name: Internet Protocol Security（书中 p67 展开）
  category: protocol
  source_pages: p67, p96, p293-294, p301
  source_quote: |
    "'IPSec' for ABC-F signaling encryption • Stands for 'Internet Protocol Security' • Handled by
    'IPSec Manager' OXE software component (OpenSwan based)" (p67)
    "IPsec manager uses the TCP port 2579 • Open SWAN uses the port number 500 for the negotiation
    with the other nodes" (p301)
  definition: |
    ABC-F 网络节点间信令加密协议（ABC-F 信令/审计/广播）：由 IPSec Manager（OpenSwan 基）建立隧道，
    证书认证（全网一 CA、每节点专属证书）；端口=协商 500/TCP 2579；无需新许可；仅 hybrid link 网络
    提供 transit 拓扑。
  alias_or_related: SRTP 密钥经加密 ABC-IP 链路下发（p293）
  tags: [protocol, ipsec, abc-f]

- id: g42
  term: NOE
  category: protocol
  source_pages: p63-64, p69, p87, p122
  source_quote: |
    "SRTP based media encryption between two TLS/DTLS capable devices • Symmetric Keys … By the OXE
    Call Server (via 'Linux'), for IP NOE endpoints or IPMGs" (p69)
    "NOE DTLS 1.2 Sig. (encrypted) NOE Sig. (clear)" (p87)
  definition: |
    ALE 私有 IP 话音协议族名（全书未展开全称；与 SIP 并列的端点信令类型）：IP NOE 端点（话机/IPDSP）
    经 EGW 走 NOE over DTLS，密钥由 CS 生成；CS_MODE=NOE 出现在 lanpbxbuild 输出。受保护 NOE 设备
    清单见 p64/p83。
  alias_or_related: 对照 SIP（SEPLOS）侧
  tags: [protocol, noe]

- id: g43
  term: SCEP
  full_name: Simple Certificate Enrollment Protocol（书中 p23/p84 展开）
  category: protocol
  source_pages: p23, p80, p84, p375
  source_quote: |
    "SCEP: Simple Certificate Enrollment Protocol • born in the early 2000s, was designed for network
    device certificate issuance … Addresses legacy environments with minimal security requirements
    (HTTP, shared secret …) and has limited renewal support" (p23)
    "Using the 'SCEP' protocol, sets are able to get automatically their certificate." (p375)
  definition: |
    证书自动注册协议（面向设备）：用于 IP 话机导入定制证书/CA 链（经 HTTP(s)），覆盖 ALE Basic/
    Enterprise/Essential 与 80x8s（8088 除外）；安全要求低（HTTP+共享密钥）、续期支持有限——是三协议
    中最老的一代。
  alias_or_related: 对照 g44 EST、g45 ACME
  tags: [protocol, scep]

- id: g44
  term: EST
  full_name: Enrollment over Secure Transport（书中 p23/p84 展开，RFC 7030）
  category: protocol
  source_pages: p23, p80, p84
  source_quote: |
    "EST: Enrollment over Secure Transport (RFC 7030, 2013) • Modern, flexible and secure evolution
    of SCEP … It uses strong authentication over TLS (mTLS / credentials) and has a built-in
    certificate renewal process" (p23)
    "Renewal automatically performed if the remaining days of the certificate validity period falls
    below a configurable threshold … the IPMG must be rebooted to switch on the renewed certificate •
    An incident is generated when the certificate enrollment or renewal process succeeds (5779) or
    fails (5780)" (p84)
  definition: |
    证书自动注册与续期协议（RFC 7030，TLS 强认证）：适用于 OXE-MS、GD4、GA4、GD-XL、GA-XL、GD3、
    INTIP3（作 EST 客户端）；剩余有效期低于可配阈值自动续期、IPMG 重启后切换新证书；结果产生事件
    5779（成功）/5780（失败）。
  alias_or_related: mgconfig/omsconfig 证书子菜单含 EST Server Configuration 项（p358）
  tags: [protocol, est, renewal]

- id: g45
  term: ACME
  full_name: Automatic Certificate Management Environment（书中 p23/p84 展开，RFC 8555）
  category: protocol
  source_pages: p23, p84
  source_quote: |
    "ACME: Automatic Certificate Management Environment (RFC 8555, 2019) • The most recent of the
    three … authentication is based on proof of control over a domain via 'challenges'" (p23)
    "Used for automatic deployment and renewal of the certificate used by the WBM application • OXE
    CS acts as an ACME client (not handled by PCS)" (p84)
  definition: |
    域名验证型证书自动化协议（RFC 8555，Let's Encrypt 提出）：OXE 场景仅用于 WBM 应用证书——CS 作
    ACME 客户端（PCS 不管）、默认关闭（root 启用）、cron 周期查过期触发续期；须本地支持 ACME 的
    第三方 CA 并加入 OXE 可信主机；公网 CA 因 HTTP-01 需公网可达而不可用。
  alias_or_related: 与 SCEP/EST 的分工对照见 principle p15
  tags: [protocol, acme]

- id: g46
  term: CRL / CDP / OCSP
  category: protocol
  source_pages: p12, p17
  source_quote: |
    "CRL (Certificate Revocation List) • List of invalid/compromised end-entity certificates, regularly
    updated and published by the Certificate Authority … The CRL is identified in certificates via the
    CRL Distribution Point (CDP) extension … thisUpdate → issue date • nextUpdate → next expected
    update" (p17)
    "Then it checks towards the concerned CA whether this certificate has been or not revoked (via
    OCSP protocol)" (p12)
  definition: |
    证书吊销机制（概念层讲义）：CRL=CA 定期发布的失效证书清单（序列号/吊销原因/日期，CA 数字签名），
    经证书的 CDP 扩展指示下载位置，有 thisUpdate/nextUpdate 有效期；OCSP=实体收到证书后向 CA 在线
    核查吊销状态的协议（缩写未展开）。注意：OXE 侧无吊销操作实验，吊销在书外。
  alias_or_related: 与 g06 CTL 同属 PKI 信任机制
  tags: [protocol, crl, pki]

- id: g47
  term: PKCS 容器家族（PKCS#7 / PKCS#10 / PKCS#12 / PEM / DER）
  category: protocol
  source_pages: p14-16, p103-106, p391, p397
  source_quote: |
    "PEM is a 'Base-64' encoded file, using ASCII letters … DER format is a binary certificate format
    … PKCS#7 or P7B extension means one or more Base-64 ASCII certificates … The P7B file contains the
    certificate and its chain but does not contain the private key … PKCS #12 or PFX/P12 format is a
    binary format for storing a certificate (including its intermediate) with a private key." (p14-15)
    "The most common format for this message sent to a CA, asking for a certificate, is P10/PKCS#10
    (Binary format, which does not contain the applicant's private key)" (p16)
  definition: |
    证书/密钥容器格式族：PEM（Base-64 ASCII，.cer/.crt/.pem）、DER（二进制）、PKCS#7/P7B（证书+链、
    无私钥——书中推荐路线的载体）、PKCS#12/PFX（证书+私钥+口令——端点证书场景）、PKCS#10/CSR（申请
    文件、不含申请人私钥）。OXE 导入组合全表见 p103；路线取舍（P7 最简/P12 私钥搬家）见 n30。
  alias_or_related: PKCS = Public-Key Cryptography Standards（p15 注）
  tags: [protocol, formats, pki]

- id: g48
  term: X.509 v3 / DN / CN / SAN
  category: protocol
  source_pages: p13, p85, p206
  source_quote: |
    "Different types of normalized certificates • Main ones: X.509 (RFC5280) and OpenPGP (RFC4880) •
    ALE is using X.509 v3 certificates" (p13)
    "DN is a set of attributes describing the entity (Common Name, Organizational Unit, Organization,
    Country) … Subject Alternative Name (SAN), extension that defines additional identities … primary
    field used for identity validation, include DNS names and/or IP addresses" (p13)
  definition: |
    证书标准与身份字段：ALE 采用 X.509 v3（RFC5280）；DN=实体属性串（CN/OU/O/C）；CN=主身份（CS/PCS
    用 FQDN、板卡/话机用 MAC）；SAN=附加身份扩展、身份验证主字段（DNS 名与/或 IP 地址，EEGW 拓扑按
    五字段顺序装配）。签名算法样例 SHA256withRSA。
  alias_or_related: 无 IP SAN 的兼容边界见 n03
  tags: [protocol, x509, certificate]

# ── 六、平台与资源 (resource) ──

- id: g49
  term: RLAB / POD
  category: resource
  source_pages: p27-35, p283-290
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines hosted in a data center. … Pods are
    independent of each other • Pods have the same configuration • Pods have access to common
    resources." (p29)
  definition: |
    ALE 培训远程实验室（全虚拟化，无课堂设备）：按 POD 划分同构实验单元，POD 间相互独立、共享公共
    资源（NAS、SIP 模拟器、外部 DNS、邮件服务器）；每 POD 两套拓扑（stand-alone 双 CS + ABC-F 双
    节点）。Rlab 门户可管理 VM 实例/网络接口/路由器（断开/连接 VLAN，p154/p285）。
  alias_or_related: 两套拓扑 IP/账号全表见 principle p30
  tags: [resource, lab, training]

- id: g50
  term: NAS 共享盘（Z:）与 CA_MAIL 共享盘（Y:）
  category: resource
  source_pages: p35, p40, p51, p115, p149
  source_quote: |
    "A network drive ('Z:\\12.0.0.2\rlab') connected to the NAS: software, licenses… retrieval • A
    network drive ('Y:\\10.20.30.200') connected to the Certification Authority (CA_MAIL): exchange of
    CSR, certificate… with the trainer" (p35)
  definition: |
    实验客户端 PC 的两个网络盘：Z:=NAS（软件/许可，ca-certgen 根证书在 ENTPXTE421/Certificates 目录、
    ISO 在 N:Softs）；Y:=CA_MAIL（10.20.30.200\Sharing，与 trainer 交换 CSR/证书的共享区，按 PODx
    子目录分放）。
  alias_or_related: 证书交接流程见 c02/c09/c10
  tags: [resource, lab, share]

- id: g51
  term: ALE Knowledge Hub（培训评估入口）
  category: resource
  source_pages: p404-410
  source_quote: |
    "Connect to ALE Knowledge Hub (https://enterprise-education.csod.com ) with your usual
    credentials … Click on My Training … select Evaluate in the dropdown menu" (p406-408)
  definition: |
    ALE 培训平台（enterprise-education.csod.com）：课后必须完成在线评估才能下载培训证书；课程检索与
    反馈通道（training-services@al-enterprise.com）。属课程运营内容，非技术知识。
  alias_or_related: 课程参考号由讲师提供（p407）
  tags: [resource, training]

- id: g52
  term: hohnstaedt.de/xca（XCA 官网）
  category: resource
  source_pages: p335, p337, p380
  source_quote: |
    "'XCA' program can be downloaded on the following website https://hohnstaedt.de/xca/index.php/
    download" (p335)
  definition: |
    XCA 工具的官方下载与文档站点（hohnstaedt.de/xca）：下载 setup.exe 安装；工具用法查其 Help/Content
    （F1）或问 trainer（p353/p403）。教学用途的外部资源。
  alias_or_related: XCA 工具条目见 g32
  tags: [resource, website, xca]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列候选术语逐条核对

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| Native Encryption (FSNE) | 正文有明确定义（p62 展开） | g01 |
| EGW (Encryption Gateway) | 有（p76 定义） | g02 |
| EEGW (External EGW) | 有（p77/p200） | g03 |
| SIP Translator (NSP) | 有（p76 NSP 展开、p202 职责） | g04 |
| CTL (Certificates Trust List) | 有（p24/p79） | g06 |
| TOFU | 有（p80 展开 trust on first use） | g07 |
| mTLS (Mutual Authentication) | 有（p82/p165） | g08 |
| SRTP | 有（p69 展开） | g40 |
| lanpbx.cfg | 有（p121-125 字段表） | g10 |
| Partial encryption | 有（p66） | g09 |
| netadmin | 有（p101 管理面定义） | g35 |
| X.509 v3 (RFC5280) | 有（p13） | g48 |
| PKCS#7 / PKCS#12 | 有（p15/p16） | g47 |
| SCEP/EST/ACME | 有（p23/p84 三协议全展开） | g43/g44/g45 |
| OMS | 有定义性用法（p52 软件机架/omsconfig），全书未展开全称 | g20 |
| OTSBC (OT-SBC) | 有定义性用法（SBC 角色），全书未展开全称 | g24 |
| OST (OXE Signaling Translator) | 有（p209 展开） | g05 |
| PCS | 有（p92 Passive Communication Server 语境） | g19（并入 OXE 条） |

结论：**OVERVIEW 18 行术语全部在册、全部有正文依据**；本次新增 34 条补全六类（账户角色、许可、工具、协议细节、资源）。

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：OST（g05）、Factory certificate（g11）、End entity/CN=MAC 约定（g12）
- 角色：mtcl/root/swinst/CA Administrator（g13-g16）
- 许可：License #424/#359（g17/g18）
- 产品：OXE/PCS（g19）、IPMG 家族（g21）、IPDSP（g22）、ALES（g23）、4645 VM（g25）、OmniPCX Record/OPR（g26）、VAA（g27）、Dispatch Console（g28）、IP-xBS（g29）、Rainbow WebRTC Gateway（g30）、FlexLM（g31）、XCA（g32）、S.O.T.（g33）、ITSP2/MicroSIP（g34）、lanpbxbuild（g36）、ostconfig/omsconfig/mgconfig（g37）
- 协议：DTLS 1.2（g38）、TLS 1.2（g39）、IPSec（g41）、NOE（g42）、CRL/CDP/OCSP（g46）
- 资源：RLAB/POD（g49）、NAS/Y: 共享盘（g50）、ALE Knowledge Hub（g51）、hohnstaedt.de/xca（g52）

### 3. 仅 passing 提及、未单列条目的词（备查）

CC-suite-ID（p310/p311，内嵌 CA 的 Root CA CN，未展开全称，附于 g31/g17 语境）、DDI/DID（p52/p54，翻译表字段，未展开，附于 c01）、NPD（p55 Numbering Plan Description 展开，属实验编号口径，附 principle p30）、MD5（p10 哈希例）、ECC/Diffie-Hellman（p7 算法例）、AES-GCM（p160 MAC/保密口径）、OpenSwan（p67/p301 IPSec 实现）、OpenSSL（p78/p83/p101/p366）、libsrtp（p76 A4645 组件）、Nginx（p76 NSP 展开）、Rocky Linux（p209/p278 EEGW OS）、pfSense（p267 外部 DNS 例）、*tx8000#（p135 话机默认口令，附 principle p21）、VLAN/DHCP option 66（p73/p52）、MTU（p202 RFC3261 TCP 切换语境）、8135s/8378/8328（p202/p366 设备型号）、ALE-120/EM-200（p73 话机型号）、ALE-2/ALE-3/ALE-30（p366 SIP 互认证支持型号）、8088（p84 SCEP 不支持型号）。

### 4. 提取口径说明

- 所有定义只采信本书正文；NOE/OMS/IPDSP/ALES/VAA/DC/IP-xBS/GD4/FlexLM/DDI/CC-suite-ID/OCSP 等缩写书中未给全称，full_name 字段一律省略，不做外部补全（IPDSP 在正文 p127 以 "IP Desktop Softphone" 指称应用本身，已在条目内注明这一书内对应关系）。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准，引用均为原文摘录；原书笔误保留原样并注明（如 "Diffie-Helmman"（p7）、"your computeur"（p180）、"11520-8-N-1"（p367））。
- 六类分布：concept 12 / role 4 / subscription 2 / product 18 / protocol 11 / resource 5，共 52 条。
