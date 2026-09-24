# 原则/清单/规则/公式/数值口径候选 — OmniPCX Enterprise 原生加密 (ENTPXTE421EN Ed05)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号、分机号）均标注"实验口径"，生产化需替换。版本号一律保留完整位数（R101.0 N3 / R101.1 N4 MD4 / R101.2 N5 MD2 等）。

```yaml
- id: p01
  title: 密码学三服务定义：保密性加密承载、完整性单向哈希、认证数字签名
  type: principle
  source_pages: p5, p10-11
  source_chapter: CRYPTOGRAPHY TERMINOLOGY / DATA INTEGRITY & AUTHENTICATION
  source_quote: |
    "Confidentiality • Ensure that information is protected from every disclosure to an unauthorized
    third party … Integrity • … Usually performed via a one-way hash … Authentication • … Usually
    performed via a digital signature" (p5)
    "One bit modified on the message affects half of the bits of the hash • Two different messages
    don't produce the same hash • Examples: SHA-2, MD5" (p10)
    "MAC combining hash and encryption with private key is also called digital signature" (p11)
  summary: |
    三个安全服务的实现口径：保密性=对传输信息加密；完整性=单向哈希（SHA-2/MD5，雪崩效应：1 位改动
    影响一半哈希位，不可逆）；认证=数字签名（哈希+私钥加密的 MAC）。配套警告（p10）：仅哈希不认证
    时，中间人可用同款哈希算法伪造——哈希必须与认证绑定。
  conditions: 通识层
  tags: [principle, cryptography]

- id: p02
  title: 对称/非对称算法分工：对称加密数据、非对称传密钥与签名
  type: rule
  source_pages: p6-9
  source_chapter: SYMMETRIC / ASYMMETRIC CRYPTOGRAPHY / DATA CONFIDENTIALITY
  source_quote: |
    "Symmetric cryptography • One unique secret key, shared for ciphering / deciphering • Fast
    ciphering, deciphering, low CPU consumption … • 1 interlocutor = 1 key" (p6)
    "Session key: the symmetric key is changed at each session" (p9)
  summary: |
    分工规则：对称（DES/AES）快、CPU 低，但 1 对话者 1 把钥、分发难、只保保密；非对称（RSA/ECC/
    Diffie-Hellman）慢，但 1 对钥服务任意人数、可认证+完整性。工程口径：非对称安全传"会话密钥"
    （每会话更换），对称加密业务数据。OXE 侧对应：SRTP 用对称会话密钥，证书/签名用非对称。
  conditions: 全书加密实现的算法学基础
  tags: [rule, cryptography, algorithm]

- id: p03
  title: SRTP 密钥机制：每方向一把、CS（Linux）或 SIP 端点生成、经 DTLS/TLS 信令下发
  type: rule
  source_pages: p69
  source_chapter: VOICE ENCRYPTION PROTOCOL
  source_quote: |
    "Symmetric Keys, necessary for the use of the SRTP , are generated natively: • By the OXE Call
    Server (via 'Linux'), for IP NOE endpoints or IPMGs • By the SIP endpoint (for TLS compatible
    SIP extensions). • For each communication, there is one SRTP key generated for each direction.
    • Keys sent to the concerned endpoints through the DTLS / TLS secured signaling link" (p69)
  summary: |
    SRTP 密钥生成与分发规则：NOE 端点/IPMG 的密钥由 Call Server（经 Linux）生成，TLS SIP 扩展的
    密钥由 SIP 端点自己生成；每通通信每个方向各一把；密钥经已加密的 DTLS/TLS 信令链路下发——
    前提是信令先加密。排障含义：信令不加密则媒体密钥无从安全分发。
  conditions: 录音场景（OPR）另按每次保持/转接换钥（p97）
  tags: [rule, srtp, key]

- id: p04
  title: SRTP cipher suite 参数与"不混用"规则：AES-CM-128-HMAC-SHA1-80 或 AES-256-CM-HMAC-SHA1-80
  type: rule
  source_pages: p70, p71
  source_chapter: CIPHER SUITES CUSTOMIZATION: SRTP
  source_quote: |
    "SRTP: AES-CM-128-HMAC-SHA1-80 or AES-256-CM-HMAC-SHA1-80 (via system parameter SRTP Cypher
    Suite) • No mixity between SRTP AES-128 and SRTP AES-256 for ciphered communications within a
    given OXE system" (p70)
    "Setting AES-256 will result in calls in clear mode with equipments only supporting AES-128
    (even if all parties are secured) • Concerns today IP-xBS, IPDSP Android, 'hybrid link' based
    ABC network (which only support AES-128)" (p70)
  summary: |
    系统参数 SRTP Cypher Suite 二选一，同一 OXE 系统内加密通信不混用。选 AES-256 的代价：只支持
    AES-128 的设备（IP-xBS、IPDSP Android、hybrid link ABC 网络）通话回落明文 RTP（即使各方都是
    "secured"状态）；信令仍加密（设备在管理上仍为 secured）。AES-256 兼容清单：NOE=Enterprise/
    Essential 话机、IPDSP(PC/Android)、80x8s；SIP=Enterprise、Essential（仅 ALE-30）、Basic 话机、
    ALES；基础设施=GD4、GD-XL、OXE-MS、Rainbow WG、OT-SBC、INTIP3（自 R101.1 MD4）、IP-xBS（自
    R101.2 MD2）；应用=4645、VAA、OmniPCX Record、O2G、DC。
  conditions: 版本门槛：INTIP3 AES-256 自 OXE R101.1 MD4；IP-xBS 自 OXE R101.2 MD2
  tags: [rule, srtp, cipher-suite, version]

- id: p05
  title: SRTP AES-256 的硬件代价：GD4/GD-XL 压缩器 60→45、INTIP3 60→30、GD3 禁用必须换 GD4
  type: metric
  source_pages: p70, p72
  source_chapter: CIPHER SUITES CUSTOMIZATION: SRTP
  source_quote: |
    "It is not authorized to activate SRTP AES-256 mode on an OXE system with GD3 boards" (p70)
    "A reboot of the OXE system is mandatory when changing the 'SRTP cypher suite' system option.
    • In SRTP AES-256 mode, GD4/GD-XL boards are limited to 45 compressors maximum (instead of 60)
    and INTIP3 boards to 30 compressors (instead of 60) • No restriction on GA4/GA-XL boards and
    OXE-MS component" (p72)
    "Any existing GD3 board has to be replaced by a GD4 board" (p72)
  summary: |
    逐格数值：切换 SRTP cipher suite 必须重启 OXE；AES-256 模式下 GD4/GD-XL 压缩器上限 60→45、
    INTIP3 上限 60→30，GA4/GA-XL/OXE-MS 无限制；GD3 板卡禁止 AES-256——存量 GD3 必须换 GD4 才能
    启用。AES-256 还要求 OXE 数据库带 'Direct Link' 标签（stand-alone 或 direct link ABC-F 网络）。
  conditions: 仅 AES-256 模式受限；AES-128 无此约束
  tags: [metric, capacity, hardware, version]

- id: p06
  title: 信令 cipher suite 两条，至少保留一条；信令与话音的 AES 位数选择相互独立
  type: rule
  source_pages: p68, p72
  source_chapter: CIPHER SUITES CUSTOMIZATION: DTLS / SIP TLS
  source_quote: |
    "'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384' • At least one
    of TLS cipher suite must remain selected among both, otherwise the encryption devices won't be
    able to connect." (p68)
    "The choice of AES-128 or AES-256 for voice and signaling is totally independent" (p68, p72)
  summary: |
    两条信令套件：TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256（默认 True）与
    TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384；至少勾一条否则加密设备连不上，两条可同时开。信令加密
    的 AES 位数与 SRTP 的位数完全独立——受保护设备的信令一律加密，即使其 SRTP 能力与系统配置
    不匹配（p68/p72 重复强调）。
  conditions: cryptview 输出可见两参数当前值（p131）
  tags: [rule, tls, cipher-suite]

- id: p07
  title: 加密由 Call Server 强制：IPMG/PCS 恒加密、用户级逐台开关、共享上下文须同质配置
  type: principle
  source_pages: p65-66
  source_chapter: SECURITY ENFORCED BY THE CALL SERVER
  source_quote: |
    "In an OXE system with Native Encryption, IPMGs and PCS are always secured • If Native
    Encryption is enabled on an OXE system, IPMGs and PCS cannot work in non-secured mode" (p65)
    "If a given endpoint is secured in nominal mode (ie on Call Server), it will also be secured in
    PCS mode" (p65)
    "DSS & DSU (desk sharing context), as well as ProACD & agent (contact center context) must be
    configured homogeneously" (p66)
  summary: |
    强制规则四条：①NE 开启后 IPMG 与 PCS 一律加密，不允许明文模式；②加密按用户选项逐台启用
    （部分加密），CS 每次设备连接后核对（按硬件型号+软件版本对照已知能力表）；③名义模式受保护的
    端点在 PCS 模式下必然同样受保护；④共享上下文（DSS/DSU 桌面共享、ProACD/agent 呼叫中心）必须
    同质配置（不能一半加密一半明文）。切换加密模式需要话机重启（p66 图示）。
  conditions: IP-xBS 的加密激活对所有基站统一生效（p65）
  tags: [principle, enforcement, partial-encryption]

- id: p08
  title: 链路两端一致原则：trunk/ABC-F 两侧都要配加密，能力不匹配即退出服务
  type: rule
  source_pages: p65, p303
  source_chapter: SECURITY ENFORCED BY THE CALL SERVER / IMPLEMENTATION
  source_quote: |
    "To secure it, encryption must be set on both peers, as well as in the trunk group / ABC-F link
    settings • The trunk group / ABC-F link gets out of service in case of management / capabilities
    mismatch" (p65)
    "The ABC-IP logical link cannot be established in case only one of the two involved nodes has
    the IP logical link parameter 'Encryption' set to 'Yes', even if both nodes have activated
    'Native Encryption' at system level." (p303)
  summary: |
    一致性规则：trunk 组/ABC-F 链路要加密，两端对等体与链路设置都要开；管理/能力不匹配时链路直接
    out of service（不会静默降级）。ABC-IP 逻辑链路更进一步：仅一侧链路参数 Encryption=Yes（即使
    两侧系统级 NE 都开了）链路就建不起来。SRTP authentication 参数还须在所有参与网络呼叫的受保护
    节点上取相同值（p303）。
  conditions: 排障提示：链路 DOWN 先查两端参数是否一致
  tags: [rule, trunk, abc-f, consistency]

- id: p09
  title: 容量与许可公式：内嵌 1500/EEGW 15000 分界；会话数=端点+3×板卡+3×外部网关+3×节点
  type: formula
  source_pages: p109, p77, p63
  source_chapter: SOFTWARE LICENSE / INTERNAL-EXTERNAL EGW
  source_quote: |
    "License#424: defines the numbers of DTLS/TLS sessions allowed within the system • License#359:
    defines the maximum number of simultaneous SIP TLS communications" (p109)
    "∑ Quoted number of NOE/SIP endpoints to be secured (*) + 3 x total nber of GD4/GD4-XL/GD3/
    INTIP3B/OXE-MS + (3 x total nber of external SIP gateways) + 3 x total nber of nodes (hybrid or
    direct link)" (p109)
    "(*): this includes NOE equipment's (IPDSP, S serie Deskphones, Essential & Enterprise
    Deskphones), SIP equipment's (ALES, ALE-x, ALE-30, ALE-x00) and DECT base stations (IP-xBS)"
    (p109)
  summary: |
    公式：会话数 = 受保护 NOE/SIP 端点报价数 + 3×(GD4/GD4-XL/GD3/INTIP3B/OXE-MS 板卡数) + 3×外部
    SIP 网关数 + 3×节点数。许可：#424 Native Encryption Users（系统 DTLS/TLS 会话数）、#359 SIP
    Encryption Trunks（并发 SIP TLS 通信数）；会话计数由 Actis 系统级计数器管理（无按 PCS 计数）；
    EEGW 需人工报价。分界：<1500 用内嵌 EGW（CS/PCS 内嵌），≥1500 必须 EEGW（每 CS 一台，上限
    15000，p63/p77/p200）。
  conditions: 实验口径许可值：424=75、359=30（p129 spadmin 输出）
  tags: [formula, licensing, capacity]

- id: p10
  title: 证书密钥长度与 SSL 安全等级：默认 level 2 要求 SHA2+≥2048 位；N4 起可降级自担风险
  type: rule
  source_pages: p83, p366
  source_chapter: MUTUAL AUTHENTICATION / Restrictions
  source_quote: |
    "Certificate request from CS requires a minimum size of certificate with 2048 bits keys (with
    OXE default SSL security level) • Since OXE N4, possibility to decrease the OXE SSL security
    level to accept certificates with lower size keys • Risk of jeopardizing the security of the
    system: under the responsibility of the administrator!!" (p83)
    "2 (default value): which requires SHA2 signature and minimum key size of 2K • 1: which requires
    SHA2 signature and minimum key size of 1K, This level is required for ALE PKI v1 • 0: restore
    support of deprecated algorithm SHA1 for certificate signature and no minimum key size" (p366)
  summary: |
    规则：CSR 密钥长度 2048-4096 位、默认 4096（p113）；默认 SSL level 2 拒收 <2048 位或 SHA1 签名
    证书。降级通道（netadmin 11.6.3 SSL security level，自 R101.1/N4）：level 1=SHA2+1K（ALE PKI v1
    需要）、level 0=恢复 SHA1+无最小长度（遗留支持）；level 3 仅供 ALE 专家内部测试。改级后必须
    重启系统（或双 bascul）+ copy to twin。书页原文：1 与 0 的口吻都是"管理员自担风险"。
  conditions: R101.0/N3 起 OpenSSL 3.0 提升安全等级是本规则的由来（p366）
  tags: [rule, ssl, security-level, version]

- id: p11
  title: 内嵌 CA 规则：CN=CC-suite-ID、有效期 7300 天、CA 层级最多 5 级
  type: metric
  source_pages: p79, p310-312, p322
  source_chapter: CERTIFICATE AUTHORITY & CTL / internal PKI labs
  source_quote: |
    "OXE supports up to 5 levels of CA hierarchy ( Root CA→ Sub CA1 → Sub CA2… )" (p79)
    "CC-suite-ID The common name for RootCA is the CC-suite-ID of OmniPCX Enterprise, provided that
    CCsuite-ID is present in the OmniPCX Enterprise license file" (p311)
    "The validity period of all entries (CA, server certificates and private keys) is 7300 days."
    (p312, p322)
  summary: |
    数值口径：OXE 支持最多 5 级 CA 层级（Root→Sub CA1→Sub CA2…）；内嵌 CA 自动生成时 Root CA 的
    CN=OXE 的 CC-suite-ID（11111-11111-11111-11111 形式，须在许可文件中存在，p310 输入）；自动
    生成的 CA/服务器证书/私钥有效期一律 7300 天（约 20 年）。
  conditions: 内部 PKI 场景；外部 CA 场景有效期由 CA 策略定（实验样例约 1 年）
  tags: [metric, ca, pki]

- id: p12
  title: 端点证书 CN 规则：板卡/话机/软话机=MAC 地址；CS/PCS=FQDN；节点证书 CN 恒为节点 FQDN
  type: rule
  source_pages: p344, p348, p399, p322
  source_chapter: External CA - Endpoints / XCA / ABC-F internal PKI
  source_quote: |
    "Take Care, 'Common Name' for 'OMS' end entity must match it's MAC address (as for end entities
    such as GD4/GD3/GA4/GA3/INTIP3 board, IP NOE Deskphones…)" (p344)
    "Take Care, 'Common Name' of end entity must match: OXE FQDN (node name+domain) for call
    server(s) and for a passive call server (PCS) • The end entity MAC address for a GD3/GA3/INTIP3
    board, for NOE3G EE & 80x8s terminals" (p399)
    "THE COMMON NAME IN THE NODE CERTIFICATE IS ALWAYS THE NODE FQDN." (p322)
  summary: |
    CN 命名规则：OMS/GD3/GD4/GA3/GA4/INTIP3 板卡、IP NOE 话机、IPDSP 软话机的实体证书 CN=设备 MAC
    地址（IPDSP 的 MAC 在其设置 Network 页 phone identifier 查看，p348）；CS 与 PCS 证书 CN=OXE
    FQDN（节点名+域）；ABC-F 网络中每个节点证书 CN 恒为该节点 FQDN（如 oxe2.company.com）。CS 与
    PCS 用同一 CA 但各自专属证书（p92）。
  conditions: 身份校验：mTLS 时 CS 把证书身份与端点宣告的 MAC 比对（p82）
  tags: [rule, certificate, cn, mac]

- id: p13
  title: SAN 字段构成：EEGW 拓扑五字段顺序；无 IP SAN 场景自 N5 起支持且部分老设备不兼容
  type: rule
  source_pages: p85, p206, p113-114, p248
  source_chapter: CERTIFICATES SAN FIELD / External EGW Deployment
  source_quote: |
    "If an external PKI is used, the SAN fields of the certificate must be managed as follows: • The
    1st field Type: IP Content: @IP of EEG associated to Csa • The 2nd field Type: DNS Content: @IP
    of EEG associated to Csa • The 3rd field Type: DNS Content: OXE FQDN … • The 4th field … wild
    card (* + domain) • The 5th field … SIP Translator FQDN" (p206)
    "As OXE N5, certificate supports SAN fields without requiring IP addresses … IP-XBS and 80x8s
    deskphones in NOE mode are not compatible" (p85)
  summary: |
    SAN 装配规则：内嵌 CA/内部 CSR 时 SAN 自动管理；外部 PKI 手工做证时按顺序五字段——①IP:EEGW
    (Csa)②DNS:EEGW (Csa)③DNS:OXE FQDN④DNS:通配符(*+域)⑤DNS:SIP Translator FQDN（双 CS 时再加
    CSB 侧与各角色 IP，p206 样例）。无 IP SAN 场景：OXE N5 起 CSR 可不带 IP 地址（CN 含 OXE FQDN，
    SAN 含 OXE FQDN 与 Translator FQDN），NOE 设备靠 lanpbx.cfg 里的 server FQDN 做 FQDN 校验；
    兼容性边界：IP-xBS 与 NOE 模式 80x8s 话机不支持无 IP 证书。
  conditions: CSR 交互中"IP addresses in SAN?"答 n 时有 WARNING：部分话机可能永远无法投入服务（p113）
  tags: [rule, san, version]

- id: p14
  title: 工厂证书适用范围与版本门槛：GD4/GA4/GD-XL/GA-XL/话机/IP-xBS；R101.1 MD4 起可用
  type: rule
  source_pages: p78, p83
  source_chapter: ONE CERTIFICATE FOR EACH COMPONENT
  source_quote: |
    "Factory certificate only for GD4, GA4, GD-XL & GA-XL boards, deskphones and IP-xBS" (p78)
    "GD4/GA4/GD-XL and GA-XL boards factory certificate usable only from OXE R101.1 MD4" (p78, p83)
    "A VoIP board with factory certificate can be deployed on a lower release than R101.1 MD4. It
    will work without limitation, except that it won't be able to use the factory certificate" (p78)
  summary: |
    工厂证书规则：仅 GD4/GA4/GD-XL/GA-XL 板卡、话机与 IP-xBS 出厂带证书；板卡工厂证书只有 OXE
    R101.1 MD4 及以上才能用——低版本部署不报错，只是工厂证书闲置；2025 年底起新产板卡默认内嵌
    ALE 证书。定制证书部署：手工或话机走 SCEP（p78）。
  conditions: 双向认证时端点证书必备；服务器认证模式不需要端点证书
  tags: [rule, factory-certificate, version]

- id: p15
  title: 注册协议分工清单：SCEP=话机、EST=IPMG/IP-xBS、ACME=WBM（仅本地 CA）
  type: checklist
  source_pages: p84, p23
  source_chapter: CERTIFICATES ENROLLMENT AND RENEWAL
  source_quote: |
    "SCEP … Supported by ALE Basic/Enterprise/ Essential IP Deskphones and 80x8s Premium Deskphones
    (not the 8088)" (p84)
    "EST … Apply to OXE-MS, GD4, GA4, GD-XL, GA-XL, GD3, INTIP3, which are acting as an EST client"
    (p84)
    "ACME … Used for automatic deployment and renewal of the certificate used by the WBM application
    • OXE CS acts as an ACME client (not handled by PCS)" (p84)
  summary: |
    分工清单：SCEP（经 HTTP(s)）——让客户证书替换话机出厂 ALE 证书，覆盖 ALE Basic/Enterprise/
    Essential 与 80x8s（8088 除外）；EST——OXE-MS、GD4、GA4、GD-XL、GA-XL、GD3、INTIP3 作 EST 客户端
    自动注册与到期续期（剩余有效期低于可配阈值即续；IPMG 须重启才切换新证书）；ACME——WBM 应用
    证书的自动部署续期，OXE CS 作客户端（PCS 不管），默认关闭须 root 启用，cron 周期查过期，须
    本地支持 ACME 的第三方 CA 且服务器加入 OXE 可信主机；公网 CA（Let's Encrypt 等）因 HTTP-01
    需公网可达而不可用。
  conditions: 注册/续期成功或失败在 IPMG 上产生事件 5779/5780（p84）
  tags: [checklist, scep, est, acme]

- id: p16
  title: 原生加密事件码表：5991/5992/5993/5995（incvisu/incinfo 查看）
  type: metric
  source_pages: p132
  source_chapter: Maintenance – Incidents
  source_quote: |
    "5991 Minor 'No reaction of the system' … check if the CTL is configured correctly on OXE and
    Endpoint" (p132)
    "5992 Minor 'FSNE:EGW – Remaining Validity Period of the CA Certificate. : P1' … If P1 is 0, the
    certificate becomes invalid and all end points with FSNE enabled reboot" (p132)
    "5993 Major … If P1 is 1, the connection is encrypted (DTLS connection) • If P1 is 0, the
    connection is not encrypted" (p132)
    "5995 Major 'FSNE: Inconsistency of CS IP Address between EGW menu and Netadmin configuration'"
    (p132)
  summary: |
    四个事件：5991（Minor）系统无反应→查 OXE 与端点 CTL 配置是否正确，详情查 netadmin 历史文件；
    5992（Minor）CA 证书剩余有效期 P1 天——P1=0 时证书失效、所有开启 FSNE 的端点重启，须在到期前
    换证；5993（Major）duplication 场景主备 CS 间连接是否加密——P1=1 加密（DTLS）、P1=0 明文，修复
    证书后需重启 CS；5995（Major）EGW 菜单与 netadmin 配置的 CS IP 不一致→加密异常，核对两处后
    重启 CS。SIP TLS trunk 无新增事件（p171，trunk 起不来查 /usr4/tmp/sipalarm.log）。
  conditions: EST 注册类事件 5779/5780 归 IPMG 续期（p84，与上列不同族）
  tags: [metric, incidents, maintenance]

- id: p17
  title: lanpbxbuild 操作规则：必须在 main CS 上跑；产出双文件自动同步 twin；-auto 会重置配置
  type: rule
  source_pages: p121, p230, p315-317, p122
  source_chapter: lanpbx.cfg 实验章节 Warning/Notes
  source_quote: |
    "IN CASE OF A COMMUNICATION SERVER DUPLICATION, THE LANPBXBUILD TOOL MUST BE LAUNCHED ON THE MAIN
    COMMUNICATION SERVER. THE LANPBXBUILD TOOL GENERATES TWO FILES: LANPBX.CFG AND LANPBXTWIN.CFG.
    IT AUTOMATICALLY COPIES THE LANPBXTWIN.CFG FILE ON THE STANDBY COMMUNICATION SERVER." (p121)
    "-auto option will reset all the existing configurations except IP_CPU and IP_DOWNLOAD options"
    (p121)
    "To be able to manage the DTLS IP addresses with lanpbx tools (option 'j' and 'k'), the native
    encryption must be previously activated at the OXE configuration level." (p122)
  summary: |
    四条规则：①duplication 时 lanpbxbuild 只能在主 CS 上执行（生成 lanpbx.cfg + lanpbxtwin.cfg 并
    自动拷贝到 standby）；②lanpbxbuild -auto 会重置除 IP_CPU/IP_DOWNLOAD 外的所有既有配置；③要先
    在 OXE 配置级激活 Native Encryption，lanpbx 工具的 j/k（DTLS1/2 地址）选项才可用；④每次 Apply
    changes（菜单 6）都会重签 lanpbx（CTL 生成 + Native Encryption signing），改动后重启 CS 生效。
  conditions: 关键路径选项：j/k=DTLS 1/2 IP，l=DTLS 端口（默认 32643），n=OXE FQDN，d/e/f=证书服务器（dot1x 项复用）
  tags: [rule, lanpbx, duplication]

- id: p18
  title: lanpbx.cfg 的 DTLS 参数字段表（10 个字段逐一定义）
  type: checklist
  source_pages: p124
  source_chapter: DTLS parameters included in the "lanpbx.cfg" file
  source_quote: |
    "DTLS … Possible values: ENABLED/DISABLED … DTLS_SRV Main DTLS server IP address (physical IP
    address of the main OXE, when the internal EGW module is used, or IP address of the associated
    EGW virtual machine, when external EGW is used) … DTLS_PORT DTLS port … DTLS_CERT_TRUST
    Certificate Trust List (CTL) in a PEM format … DTLS_SIGN_CERT Server certificate used to sign the
    'lanpbx.cfg' file … DTLS_SIGN_CERT_ALT Previous server certificate used on the OXE." (p124)
  summary: |
    字段清单：DTLS（FSNE 开关，配置了 DTLS_SRV 即自动 ENABLED）；DTLS_SRV（主 DTLS 服务器：内嵌
    EGW=主 OXE 物理 IP，外部 EGW=EEGW VM IP）；DTLS_SRV_RD（duplication 的备用 DTLS 服务器）；DTLS_
    PORT（DTLS 端口，默认 32643）；OXE_FQDN（无 IP SAN 证书时端点比对用）；DTLS_CERT_TRUST（PEM 格
    式 CTL，"Enable Automatic CTL Acquisition"=True 时自动注入，含单 CA 证书或 CA 链）；DTLS_SIGN_
    CERT（签 lanpbx.cfg 的服务器证书，签名时自动加入）；DTLS_SIGN_FILE（lanpbx.cfg 数字签名）；DTLS_
    SIGN_CERT_ALT / DTLS_SIGN_FILE_ALT（换 CA 后保留的旧证书与旧签名，供过渡期验证）。样例行：
    DTLS=ENABLED DTLS_SRV=192.168.1.1 DTLS_SRV_RD=192.168.1.2 DTLS_PORT=32643 OXE_FQDN=oxe.company.com。
  conditions: 文件位于 /usr3/mao/lanpbx.cfg；more 命令可查看
  tags: [checklist, lanpbx, fields]

- id: p19
  title: 系统参数三件套口径：Native Encryption / SIP Parameters / Voice Mail Parameters 的关键取值
  type: checklist
  source_pages: p119, p140, p190, p254, p95
  source_chapter: 各实验章参数页
  source_quote: |
    "Enable Native encryption … True: Native Encryption is enabled … False (default)" (p119)
    "TLS signaling possible True (used to enable the ports listening)" (p140)
    "SRTP offer answer mode True: SRTP according to SDP offer answer mode. SRTP is done by two keys
    exchange. SRTP authentication can be done. SRTCP is in RFC mode … False: SRTP OXE centralized
    mode. SRTP is done by one key exchange. No SRTP authentication can be done. SRTCP is in THALES
    mode" (p190)
    "Authentication for SRTP … Possible values: • Unauthenticated (default value) • Authenticated •
    Authenticated tag emis. w/o ctrl" (p190)
  summary: |
    参数清单：①Native Encryption 块——Enable Native encryption（默认 False）、Enable automatic CTL
    Acquisition（True=CTL 经 lanpbx.cfg 自动下发）、Authentication for SRTP（Unauthenticated 默认/
    Authenticated/Authenticated tag emis. w/o ctrl 三值；IPDSP 只工作在 SRTP authentication 下，
    故实验一律 Authenticated）、Enable Mutual TLS Authentication（DTLS 端点双向认证）、TLS cipher
    两条、SRTP Cipher Suite；②SIP Parameters 块——TLS signaling possible（默认 False，开启端口监听，
    改后重启 CS 或双 bascul，netstat -an|grep 5061 验证）、SRTP offer answer mode（True=SDP 协商/
    双密钥/可认证/SRTCP RFC 模式，加密网络至少 R10.1.1；False=OXE 集中式/单密钥/不可认证/SRTCP
    THALES 模式）、Loose Route with RegID（True 时相应 INVITE 被 488 Not Acceptable Here 拒绝，实验
    置 False）、Enhanced codec negotiation（Network Type=全网多编解码重协商，须所有节点开；Local
    Type=仅本节点端点间）；③Voice Mail Parameters——Enable Voicemail Encryption（4645 单参数激活）。
  conditions: SIP TLS Mutual Authentication（SIP 扩展互认证）在 Native Encryption 块，节点重启生效（p377）
  tags: [checklist, parameters, wbm]

- id: p20
  title: 证书备份规则：netadmin 导出+Linux Data 备份双保险；导出口令四类 8 位
  type: rule
  source_pages: p107, p133
  source_chapter: BACKUP OF CERTIFICATES INTO OXE / Certificates back up
  source_quote: |
    "ALE strongly recommends to systematically backup certificates and keys whenever modifications
    are performed • 2 solutions • Export CS Certificates ('netadmin –m', with 'root' account) • Back
    up Linux Data ('swinst')" (p107)
    "The password string must have a minimum of 1 upper case letter, 1 lower case letter, 1 numeric
    character, 1 special character (except single quotes) and a minimum length of 8 characters." (p133)
    "Warning TRANSFER THE CERTIFICATE FILES TO A STORAGE MEDIA. THESE CERTIFICATES CAN BE IMPORTED
    AND USED ON THE OMNIPCX ENTERPRISE AFTER A DISK CRASH FOR EXAMPLE" (p133)
  summary: |
    备份规则：每次证书变更后系统化备份——方案 1 netadmin -m 11.9.1.5 导出（选 PKCS#12 或 PKCS#7，
    产出 ca_csa.p7 与 csa.pfx 至指定路径）；方案 2 swinst 备份 Linux Data 时证书自动随备份。导出
    口令规则：≥8 位、含大写+小写+数字+特殊字符各 1（单引号除外）。PCS 证书同理走 11.9.2.4 导出
    （PFX 打包成 tar：csa_pcs_pfx.tar）。警告：必须把证书文件转到存储介质——磁盘崩溃后可用于导入恢复。
  conditions: 导出用 root 账户
  tags: [rule, backup, certificate]

- id: p21
  title: 三套口令规则对照：netadmin 导出 8 位四类 / EEGW Rocky Linux 14 位强化 / 话机下载默认 *tx8000#
  type: metric
  source_pages: p133, p279, p135
  source_chapter: Certificates back up / S.O.T. lab / Wireshark lab
  source_quote: |
    "a minimum length of 8 characters" (p133)
    "-password string must have a minimum of 14 characters -password string must have at least 2
    alphabets (1 upper case mandatory) -password string must have at least 2 numeric characters
    -password string must have atleast 1 special character … -password must be different from the
    last twenty-four used passwords" (p279)
    "If defined, use 'Alcatel-Lucent 8&9 Series / IPTouch Set's Generic Parameters / Noe password'.
    Else, default password is *tx8000#" (p135)
  summary: |
    口令规则三套：①证书导入/导出（PKCS#12/PKCS#7）≥8 位、大写+小写+数字+特殊字符各 1（单引号除外）；
    ②EEGW VM（Rocky Linux）首次改密：≥14 位、≥2 字母（含 1 大写）、≥2 数字、≥1 特殊字符、不含用户
    名、无 4 连同符、无 4 顺序符、非字典词、不与前 24 次重复（默认 root/letacla1，实验口径改为
    Superuser2580*）；③话机远程访问（tnet d）默认口令 *tx8000#（或在系统参数 Noe password 定义）。
    实验口径其余口令：mtcl/swinst/root=Superuser2580*、SBC=Admin/Admin、ALES=alcatel、FlexLM=root/
    letacla1、XCA 库=Alcatel。
  conditions: 全部为实验口径或产品默认值，生产必须替换
  tags: [metric, password, lab]

- id: p22
  title: 加密验证命令口径：ippstat / twin / cryptview / sipregister / csipsets / sipextgw / config ost
  type: checklist
  source_pages: p129-131, p143, p192-193, p242
  source_chapter: Maintenance 各节
  source_quote: |
    "'ippstat' command (option 2) displays IP deskphone data such as the 'native encryption' status"
    (p129)
    "The command shows the status of the communication mode between both call server (Crypted or
    clear)." (p130)
    "'cryptview' command indicates if the OmniPCX Enterprise is secured." (p131)
  summary: |
    验证命令清单：①ippstat <分机>（option 2）单话机加密状态：DTLS/DTLS mao=Yes、SRTP Cipher 套件
    能力（AES_CM_128_HMAC_SHA1_80 / AES_256_CM_HMAC_SHA1_80）、Allow SRTP（如 Yes in AES128）；option
    3 列全节点 IP 话机表（DTLS/SRTP 列）。②twin——主备 CS 通信模式 Crypted/clear（输出含角色、CPU
    位置、Telephony redundancy READY）。③cryptview——System is DTLS secured、OpenSSL Security
    Level、DTLS server address（标注 Internal EGW 或 External EGW）、受保护 coupler 表（SRTP 能力
    与当前值）、系统参数快照、双向认证开关状态、Secured SIP gateway/extension 计数；提示用 cryptcheck
    补充。④sipregister——每 SIP 扩展的注册协议（contact 带 TLS 即加密注册）。⑤csipsets——SIP 扩展表
    的 TLS MAO/SRTP MAO/TLS/SRTP 列。⑥sipextgw -g <n>——外部网关状态（State IN SERVICE、Transport
    TLS Client、Mutual Authentication、SRTP=RTP or SRTP）。⑦config ost——EEGW 状态表（CS 角色/
    EGW IP/IN SERVICE）；ost_importlog 拉 EEGW 日志到 OXE /tmp（tar）。
  conditions: 全部为 mtcl 登录（netstat 需 root 看全量）
  tags: [checklist, maintenance, verification, commands]

- id: p23
  title: SIP TLS trunk 信令/媒体决定表：媒体加密=NE 开启 × 网关 SRTP 参数两者叠加
  type: rule
  source_pages: p161, p93
  source_chapter: OVERVIEW (SIP TLS FOR SIP TRUNK)
  source_quote: |
    "The Native SIP TLS trunk feature deals with signaling only • The media encryption (SRTP) depends
    on the activation of the 'native encryption' in the OXE system and on the management of 'SRTP'
    parameter in the external SIP gateway, towards the SBC" (p161)
  summary: |
    决定表：NE 关——网关配 RTP or RTP/SRTP 或 RTP → 媒体均 RTP（明文，"Encrypted Signaling - Voice
    in Clear"）；NE 开——网关配 RTP → RTP 明文；网关配 RTP or SRTP → 明文（对不支持 SRTP 对端，如
    SBC SRTP 不合规）；网关配 RTP/SRTP → SRTP（"Encrypted Signaling – Encrypted Voice"）。本质规则：
    Native SIP TLS 只管信令；媒体加密=系统 NE 激活 + 外部 SIP 网关 SRTP 参数两者叠加。
  conditions: trunk 组类型须 "ISDN all countries"（p93）
  tags: [rule, sip-trunk, srtp, matrix]

- id: p24
  title: OTSBC 侧配置参数集（TLS context / 证书 / Proxy Set / Media Security / IP Profile）
  type: checklist
  source_pages: p175-184
  source_chapter: SIP TLS configuration in OTSBC
  source_quote: |
    "Index 1, Name OXE TLS, TLS Version TLSv1.2, DTLS Version DTLSv1.2, Cipher server AES256:AES128,
    DH key Size 2048" (p175)
    "Media security Enable … Offered SRTP Cipher Suites AES-CM-128-HMAC-SHA1-80 ( compatible with the
    OXE)" (p184)
    "SBC Media Security Offer Both – Answer Prefered Secure ( SRTP and RTP) Compliant with all oxe
    phone ( FSNE enable or not)" (p184)
  summary: |
    OTSBC 配置清单：①TLS contexts（SETUP/IP NETWORK/SECURITY）：TLSv1.2+DTLSv1.2、Cipher server
    AES256:AES128、DH key 2048；②证书四步——导入 RootCA（ca-certgen.cer）→生成 4096 私钥→生成
    CSR（Common name=SBC 的 IP，SHA-256）→导入 CA 签发证书（.cer，Base-64 X.509）；③SIP Interfaces
    （OXE 侧）：TLS context 选 OXE TLS、UDP Port 置不使用、TLS port 5061；④Proxy Sets（OXE）：
    Proxy Address 端口 5061、Transport type TLS；⑤Media Security：Enable + Offered SRTP Cipher
    Suites=AES-CM-128-HMAC-SHA1-80（与 OXE 兼容）；⑥IP Profiles（OXE profile）：SBC Media Security=
    Offer Both–Answer Prefered Secure（SRTP 与 RTP 都接受，兼容未开 FSNE 的 OXE 用户）。
  conditions: EE GW+NSP 场景 Proxy Address 改 nsp.oxe.company.com:5061（p266）
  tags: [checklist, otsbc, configuration]

- id: p25
  title: ABC-F 链路加密参数规则：链路须 DOWN 才能改、两端取同值、transit 仅 hybrid
  type: rule
  source_pages: p330, p301, p303
  source_chapter: Native Encryption for ABC-F network
  source_quote: |
    "To activate encryption for the link, this last one must not be up. • Disable the access with
    signaling. … In 'other' tab of this access, activate the encryption … The parameter must have the
    same value on the accesses on both sides of the link." (p330)
    "IPsec manager uses the TCP port 2579 • Open SWAN uses the port number 500 for the negotiation
    with the other nodes … Not allowed in a 'Direct Link' based network (even if the link is in clear
    mode) • Topology available only in a 'Hybrid link' based network … Calls are established in clear
    mode for IPv6 devices." (p301)
  summary: |
    规则集：①链路加密参数在 Inter-Nodes links/Logical links (ABC-F)/Hybrid or Direct Link Access，
    必须先禁用接入（信令下链）才能改，两端取同值，改完重新启用；②IPSec 端口：OpenSwan 协商 500、
    IPsec manager TCP 2579；③网络加密不需新许可、支持高可用；④限制：与 IP Premium Security 不互通；
    该 transit 拓扑只允许 hybrid link 网络（direct link 网络即使链路明文也不允许）；IPv6 设备呼叫
    明文；⑤AES 128/256 混置 direct link 网络时节点间媒体明文但直连链路信令仍加密；AES-256 要求
    Direct Link 标签；受保护 SIP 设备场景仅 direct link 模式（p303）。
  conditions: hybvisu -f all 查链路状态（Encryption: NO/YES）
  tags: [rule, abc-f, ipsec, ports]

- id: p26
  title: mTLS 范围规则：DTLS 全局 / SIP TLS 全局 / SIP trunk 按网关；激活后所有话机需证书
  type: rule
  source_pages: p82, p377, p359
  source_chapter: MUTUAL AUTHENTICATION / mTLS Appendix
  source_quote: |
    "Global activation for all DTLS endpoints • Global activation for all SIP TLS endpoints • For
    SIP Trunking (SIP TLS), managed per SIP external gateway" (p82)
    "AS SOON AS 'MTLS' IS BROUGHT INTO SERVICE, CERTIFICATE MUST BE LOADED IN ANY IP DESKPHONE OR ANY
    IP SOFTPHONE, EVEN THOSE IN CLEAR MODE. THE FIRST CONNECTION TO OXE IS ALWAYS IN SECURED MODE"
    (p359)
  summary: |
    范围规则：DTLS 端点全局激活（Enable Mutual TLS Authentication，lanpbx 重生成+重启生效）；SIP
    TLS 扩展全局激活（SIP TLS Mutual Authentication，节点重启生效）；SIP trunk 按外部网关逐个（
    Transport type + SIP TLS Mutual Authentication=True，sipmotor 重启生效）。连带义务：激活后所有
    IP 话机/软话机（含明文模式用户）都必须装证书，且首连总是加密模式；客户认证失败则注册失败，
    EGW 触发含端点身份（IP/MAC）的事件。
  conditions: 服务器认证是 mTLS 的前提（先有 CS 证书与端点 CTL）
  tags: [rule, mtls, scope]

- id: p27
  title: 安全下载（HTTPS 替代 TFTP）规则：前提 NE 激活、DHCP option 66、IPMG 侧还要求 mTLS+TOFU
  type: rule
  source_pages: p73-74
  source_chapter: SECURE DOWNLOADS
  source_quote: |
    "Use of HTTPS protocol, instead of TFTP • Prerequisite: Native Encryption activated on the OXE,
    whether the encryption flag is activated or not at user level • Currently not available for OXE
    systems in IPv6 • In dynamic mode, DHCP option 66 is required in the DHCP offer (otherwise, TFTP
    is considered)" (p73)
    "Prerequisite: Native Encryption & Mutual Authentication activated on the OXE (so a certificate,
    factory one or custom one, must be present in the hardware or software gateway) … If TOFU mode is
    activated, OXE CTL is retrieved automatically via the 'lanpbx.cfg' file" (p74)
  summary: |
    两层规则：①CS↔设备初始化下载（话机固件/定制文件/lanpbx.cfg 等）：HTTPS 替代 TFTP，前提是 OXE
    已激活 NE（与用户级加密开关无关）；IPv6 不支持；动态模式要求 DHCP offer 带 option 66（否则按
    TFTP 处理），FQDN 时还需 DNS；静态模式手工选协议。兼容：Enterprise（含 ALE-120）/Essential
    （含 EM-200）话机与 IPDSP（NOE 模式）；老世代话机/WLAN/IP-xBS 仍走 TFTP；无加密方案或 IP
    Premium Security 的 OXE 不支持 HTTPS。②CS↔IPMG 初始化下载：前提 NE+mTLS（网关内须有证书），
    经 mgconfig（GD4/GD-XL）或 omsconfig（OXE-MS）手工选择（默认 tftp）；TOFU 激活时 OXE CTL 经
    lanpbx.cfg 自动获取，TOFU 关闭则须先把 OXE CTL 手工导入板卡/OXE-MS 再开 HTTPS；兼容 GD4/GA4/
    GD-XL/GA-XL/OXE-MS（GA 系经背板继承 GD 系选择）；GD3/INTIP3 等老板卡仍 TFTP。
  conditions: 下载内容含话机与 AOM 固件、定制文件、lanpbx.cfg、话机请求等
  tags: [rule, https, download, tofu]

- id: p28
  title: EEGW 部署硬规则：强制 VM、与 CS 同宿主同虚拟交换机、CS-EEGW 专线明文、CS 随 EEGW 重启
  type: rule
  source_pages: p200-203, p211, p239
  source_chapter: EEGW 相关讲义与实验 Warning
  source_quote: |
    "External Virtual Machine mandatory • OXE redundancy: one dedicated EEGW per Call Server •
    Includes the SIP Translator (NSP) • Virtualization of OXE mandatory" (p200)
    "The Call Server and its EEGW must be located on the same virtual switch of the same physical
    host … Dedicated UA/UDP connection, including monitoring of the external EGW presence" (p201)
    "The call server goes for reboot if the link with the external EGW is lost" (p203)
    "Warning THE CALL SERVER ASSOCIATED TO THE EEGW VIRTUAL MACHINE WILL REBOOT TOO!" (p239)
  summary: |
    硬规则五条：①EEGW 必须是外部虚拟机（OST 包，Rocky Linux），OXE 自身须虚拟化部署；②CS 与其
    EEGW 必须在同物理主机的同一虚拟交换机上；③CS-EEGW 之间建专用明文 Data Link（UA/UDP 连接+
    EEGW 存活监控），该链路丢失则 CS 重启；④OXE 冗余下每台 CS 一台专属 EEGW；⑤在 EEGW VM 上
    下载/更换证书触发重启时，关联的 CS 会跟着重启（变更窗口必须按 CS 重启规划）。PCS 侧同样规则：
    PCS 可内嵌 EGW（<1500）或外接 EEGW（>1500），PCS EGW IP=PCS IP 即内嵌、不同即外接（p213）。
  conditions: EEGW IP 须加入 CS 内部防火墙（netadmin 11.1.3）；Translator FQDN 须可解析
  tags: [rule, eegw, deployment, reboot]

- id: p29
  title: NSP/SIP Translator 声明规则：仅外部 EGW 场景强制；改名/改声明都要重生成证书+重启
  type: rule
  source_pages: p247, p219, p205, p266
  source_chapter: SIP Translator / Encryption GW Management
  source_quote: |
    "SIP TRANSLATOR HOSTNAME CONFIGURATION IS MANDATORY ONLY WHEN EXTERNAL ENCRYTPION GATEWAY(S)
    IS(ARE) DEPLOYED. IF THERE ARE LESS THAN 1500 SIP TLS/DTLS SESSIONS, INTERNAL ENCRYPTION GATEWAY
    AND SIPMOTOR PROCESS … ARE ENOUGH" (p247)
    "Warning: *** Change of translator name, requires regeneration of Call Server Certificates (CA
    Update is not required ) followed by an OXE reboot ***" (p247)
    "NSP FQDN is mandatory as soon as CS redundancy is implemented. Without redundancy, NSP IP
    address (equal to EEGW IP @) can be used" (p266)
  summary: |
    规则集：①Translator 名（nsp）只在部署外部 EGW 时强制——<1500 会话内嵌 EGW+sipmotor 就够；②
    改 Translator 名或 EEGW 声明都触发"CS 证书重生成（CA 不变）+OXE 重启"，随后 copy to twin；③
    Translator FQDN（nsp.oxe.company.com=名字+OXE 域）由 OXE 内部 DNS 解析（外部 DNS 时把委托域转发
    给 OXE，主备内部 DNS 都会被问、仅主 CS 应答→返回主 CS 的 EEGW IP——这是冗余下主备切换的正确
    行为）；④SBC 侧指向：冗余场景必须用 NSP FQDN，单机可直接用 EEGW IP。
  conditions: 内部 DNS 激活：netadmin 17.2 Node setup→Update→"activate internal name resolver? y"
  tags: [rule, nsp, translator, dns]

- id: p30
  title: 实验口径：Pod IP/账号/号码全表（两套拓扑 + SIP 模拟器 + SBC NAT）
  type: metric
  source_pages: p32, p34, p37, p39, p43-46, p52-56, p219, p276
  source_chapter: SETTINGS 表与各实验参数
  source_quote: |
    "OXE CSa … 192.168.1.1 / 192.168.1.3 … Password Superuser2580* … FLEXLM SERVER … root letacla1"
    (p34)
    "First external number 33920N31000 (where N is your POD Number) … First internal number 31000 …
    Range Size 500" (p54)
    "POD Id -> SBC NAT IP address … 12. Class Number. PoD Number 2.105" (p55)
  summary: |
    实验口径汇总（生产禁用）：stand-alone 拓扑——CSA 192.168.1.1（角色 1.3）、CSB 192.168.1.2、
    OMS 192.168.1.13、EEGW 192.168.1.7/.8、SBC 192.168.1.105/2.205、PCS 192.168.2.5、PC10/20/21
    192.168.1.10/2.10/2.11、NTP 192.168.1.252、FlexLM 192.168.1.80、内部 DNS 192.168.1.250、外部
    DNS 10.20.30.250、CA_MAIL 共享 Y:\\10.20.30.200、NAS Z:\\12.0.0.2\rlab；网络拓扑——Node2
    192.168.1.101（角色 1.103）、OMS Node2 192.168.1.113、用户 31000（Node1 IPDSP）/31500（Node2）。
    口令：mtcl/swinst/root=Superuser2580*、SBC=Admin/Admin、ALES（eevans/eeastwood）=alcatel、
    FlexLM/EEGW 初始=letacla1、SIP 模拟器=podP/alcatel。号码：安装号 3392PN、DID 首外线 33920N31000
    /首内线 31000/范围 500、NPD33 默认号 33920N31000、SBC NAT=12.班级.POD.105、SOT VM
    https://192.168.1.194、EEGW 声明 IP 192.168.1.7/.8。
  conditions: 全部为 RLAB 实验口径，生产环境按客户网段整体替换
  tags: [metric, lab, ip, password, numbering]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 18 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 密码学与证书基础 | 有 | p01, p02 | 三服务定义、两算法分工（格式/模式对比见 f07/f08） |
| task-02 | Pod 环境搭建 | 有 | p30 | IP/账号/号码全表（流程见 f05） |
| task-03 | SIP 模拟器 | 有 | p30 | 号码规则并入全表（拓扑见 f04） |
| task-04 | CSR 签发导入闭环 | 有 | p10, p11, p12, p13, p14 | 密钥长度、CA 规则、CN/SAN 规则、工厂证书 |
| task-05 | 系统/用户参数 | 有 | p19 | 参数三件套逐项口径 |
| task-06 | lanpbx.cfg | 有 | p17, p18 | 操作规则 + 10 字段表 |
| task-07 | DTLS 验证维护 | 有 | p16, p20, p22 | 事件码、备份规则、验证命令口径 |
| task-08 | Wireshark | 无独立数值条目 | （c03） | 纯操作，无新增数值（口令默认值已入 p21） |
| task-09 | SIP TLS 扩展 | 有 | p19, p22 | SIP 参数块 + sipregister/csipsets 判读 |
| task-10 | PCS 接管 | 有 | p07, p17 | PCS 恒加密 + lanpbxbuild 双文件规则 |
| task-11 | SIP trunk TLS/SRTP | 有 | p19, p23, p24, p30 | SRTP offer answer 口径、决定表、OTSBC 清单 |
| task-12 | 安全停用 | 无独立数值条目 | （c08） | 四步回退无新增数值（依赖 p17/p19） |
| task-13 | EEGW/NSP | 有 | p09, p28, p29 | 容量公式、部署硬规则、Translator 规则 |
| task-14 | S.O.T. 生成 | 有 | p21, p30 | Rocky 口令规则 + SOT 入口口径 |
| task-15 | 网络实验室改造 | 有 | p30 | Node2 IP 表（流程见 f03/c13） |
| task-16 | ABC-F 网络加密 | 有 | p08, p25, p22 | 一致性规则、链路参数规则、hybvisu 判读 |
| task-17 | XCA 端点证书 | 有 | p12, p13 | CN=MAC 规则、SAN 装配 |
| task-18 | mTLS 与限制 | 有 | p10, p26, p15 | SSL level、mTLS 范围、注册协议分工 |

**覆盖结论**：18/18 全部有对应条目或明确归入 case/framework（task-08/12 为纯操作序列，无独立数值）。口径说明：
1. 所有版本号保留完整位数：R101.1 MD4（INTIP3 AES-256、工厂板卡证书）、R101.2 MD2（IP-xBS AES-256）、R101.0 N3（OpenSSL 3.0）、R101.1 N4（SSL level 可调）、OXE N5（无 IP SAN）、R10.1.1（SRTP offer answer RFC 模式网络下限）。
2. p05 压缩器数值（60→45、60→30）与 p09 许可公式（+3×板卡等）逐格对照原文转写；p109 公式脚注的设备清单已并入条目。
3. 实验值（p30）逐页对照 p32/p34/p37/p39/p54/p55 设置表与各实验章，生产化必须整体替换。
