# 框架/流程/结构候选 — OmniPCX Enterprise 原生加密 (ENTPXTE421EN Ed05)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、命令行/WBM 菜单路径、组件关系图示、拓扑矩阵。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——密码学底座 → 实验环境 → 概念层 → 四条实验线
  type: flow
  source_pages: p1-4, p27-57, p58-110, p111-403
  source_chapter: 全书结构（Lesson Summary 与 How-To 章序列）
  source_quote: |
    "LESSON SUMMARY ✓ Cryptography: Terminology... ✓ Certificates: What is a certificate?...
    CTL (Certificates Trust List) • End-to-end certificate-based server authentication" (p4)
    "Native Encryption for DTLS compatible equipment's How to ✓ Bring into service the 'native
    encryption' for DTLS compatible equipment's (phone sets, IP MG…), using PKCS#7 certificates" (p111)
  summary: |
    课程按四段推进：①密码学与证书基础讲义（p3-26，后续一切实验的钥匙）；②实验环境（p27-57，
    RLAB 两套拓扑 + SIP 模拟器 + Pod 初始配置）；③概念层（p58-110，方案定位/机制/拓扑/管理许可
    四个 Lesson）；④实验线（p111-403 共 19 个 How-To 章，按"单机 DTLS → SIP TLS/中继 → EEGW/NSP
    扩容 → ABC-F 网络 + mTLS 强化"递进，穿插 XCA 证书工厂章与课程评估收尾）。这条"先证书后开关、
    先单机后网络"的顺序就是实际交付项目的推荐顺序。
  conditions: 无版本前提；各实验间有先后依赖（证书先行，后章复用前章成果）
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: RLAB stand-alone 实验拓扑——双 CS + OMS + EEGW×2 + SBC + PCS 远端站点
  type: diagram
  source_pages: p29-35
  source_chapter: TRAINING LAB ENVIRONMENT / TRAINING PLATFORM – NATIVE ENCRYPTION & SETTINGS
  source_quote: |
    "OXE FSNE CSA Phys: 192.168.1.1 Main:192.168.1.3 … OXE FSNE CSB Phys: 192.168.1.2 …
    EEGW FSNE CSA 192.168.1.7 … EEGW FSNE CSB 192.168.1.8 … PCS REMOTE 192.168.2.5 … SBC
    192.168.1.105" (p32)
  summary: |
    stand-alone 拓扑（Subnet 1 = 192.168.1.x 主站点，Subnet 2 = 192.168.2.x 远端站点，公共区
    Subnet 0 = 10.20.30.x）：OXE FSNE CSA/CSB（物理 192.168.1.1/.2，角色 192.168.1.3）、OMS
    CSA/CSB（192.168.1.13，虚拟 GD4 载体）、EEGW CSA/CSB（192.168.1.7/.8）、SBC（192.168.1.105/
    192.168.2.205）、PCS REMOTE（192.168.2.5）、PC CLIENT 10/20/21（192.168.1.10 / 2.10 / 2.11，
    挂 IPDSP 31000/31002/31003 与 ALES 31030/31031）、FLEXLM（192.168.1.80，root/letacla1）、
    IT SERVER/NTP（192.168.1.252）、内部 DNS（192.168.1.250）、外部 DNS（10.20.30.250）、NAS 与
    SIP 模拟器与邮件服务器（12.0.0.2/10.20.30.x）。p34 设置表给出全套登录口令（实验口径：
    mtcl/swinst/root 均为 Superuser2580*，SBC Admin/Admin，PC superuser）。
  conditions: 实验口径（RLAB 专用）；EEGW 与 PCS VM 后启动（p49），其余先起
  tags: [diagram, lab, topology, rlab]

- id: f03
  title: ABC-F 网络实验拓扑——Node 1 / Node 2 双节点 + 直连链路
  type: diagram
  source_pages: p36-40, p283-290
  source_chapter: TRAINING PLATFORM – NATIVE ENCRYPTION IN NETWORK & Pod Configuration: Network labs
  source_quote: |
    "OXE FSNE NODE 1 Phys: 192.168.1.1 Main:192.168.1.3 … OXE FSNE NODE 2 Phys: 192.168.1.101
    Main:192.168.1.103 … OMS NODE 2 192.168.1.113" (p37)
  summary: |
    网络实验换用 NODE 1 / NODE 2 两台 OXE（物理 192.168.1.1/.101，主角色 192.168.1.3/.103），
    OMS NODE 1（192.168.1.13）/ NODE 2（192.168.1.113），PC CLIENT 10/20 分别挂 IPDSP 31000
    （Node1）与 31500（Node2）。p285 交代 RLAB 约束：两台 VM 不能同 IP，需在 Rlab 门户删除
    ENTP_OXE_FSNE_CSA 的 192.168.1.1 接口、给 ENTP_OXE_FSNE_NODE1 新建 192.168.1.1 接口并硬重启。
    p288 警告：ENTP_OMS_CSA_CSB_NODE1 VM 此前被 CSA/CSB 用过、信任库已有证书，转 Node1 拓扑前
    必须用 omsconfig→Certificate management→Erase saved certificates 清除。
  conditions: 实验口径；直连链路要求 hybvisu 显示 UP（p290：Direct IP link 2002 to node 2: UP，Encryption: NO 初始态）
  tags: [diagram, lab, abc-f, topology]

- id: f04
  title: ITSP2 SIP 模拟器拓扑与号码变换规则
  type: diagram
  source_pages: p42-47
  source_chapter: SIP CARRIER SIMULATOR - ITSP2
  source_quote: |
    "ITSP2 SIP Gateway gateway.itsp2.com 10.20.30.60 … ITSP1 Public gateway public.itsp1.com
    10.20.30.50 … Id: podP password: alcatel … Public numbers: Id: publicP@itsp1.fr" (p43)
    "PBX installation nb 3392PN … 31002's external nb 3392PN31002 … Number received by the PBX:
    +33920331002" (p46)
  summary: |
    模拟器两条腿：SIP 网关 gateway.itsp2.com（10.20.30.60，SIP 域 sip.itsp2.fr）与公网网关
    public.itsp1.com（10.20.30.50，SIP 域 itsp1.fr，两个 MicroSIP 模拟 Public/Urgence 用户，账号
    publicP@itsp1.fr、urgenceP@itsp1.fr，密码 public；PBX 注册账号 podP/alcatel）。号码规则（PN=
    两位 POD 号）：紧急 112/15/17/18；国内 33{1-5}1PN12345；移动 3361/3371PN12345；国际 4421PN12345；
    公网主号 3321PN12345。呼出变换：拨 0110312345→送 +33110312345。入局本 PBX：安装号 3392PN
    （POD3=339203），DDI 首外线/首内线均 31000，分机 31002 外线号 3392PN31002。注意章内 ITSP1/
    ITSP2 标签混用为原书现象（见反例条目）。
  conditions: 实验口径；SBC 过滤在路径中（图示 SBC 于两侧）
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f05
  title: Pod 初始配置主流程（NTP→根证书→板卡→用户→公网接入四段）
  type: flow
  source_pages: p48-57
  source_chapter: Pod Configuration: Native Encryption (How-To)
  source_quote: |
    "Manage the following NTP server for all the PC clients (used in this training): 192.168.1.252"
    (p50)
    "From the NAS, select the CA certificate ('ca-certgen') in the directory: 'ENTPXTE421/Certificates'
    … Select 'Trusted root certification authorities'" (p51)
    "First external number 33920N31000 (where N is your POD Number) … Range Size 500" (p54)
  summary: |
    五步闭环：①时间同步——控制面板→时钟和区域→日期和时间→Internet 时间→更改设置→填 NTP
    192.168.1.252→立即更新（证书日期校验的前提）；②根 CA 证书——从 NAS ENTPXTE421/Certificates
    取 ca-certgen，右键安装证书→本地计算机→受信任的根证书颁发机构；③机架板卡核对——主站点 OMS
    Rack 4（虚拟 GD4 192.168.1.13/24，MAC 00:50:56:01:01:13）、远端 Rack 6（192.168.2.13）；
    ④用户——装 IPDSP（设置 TFTP=192.168.1.3）与 ALES（local access=192.168.1.3；登录 eevans/
    eeastwood，密码 alcatel，实验口径）；⑤公网接入——OXE 侧 DID 翻译（首外线 33920N31000、首内线
    31000、范围 500）与 NPD 33 默认号，SBC 侧 NAT 规则（12.班级.POD.105 形如 12.2.42.105）与
    Account 的 Contact/User Name 改为 podN，最后外呼/入局测试。
  conditions: 实验口径；OXE VM 已预配置（许可/防火墙/NTP/FlexLM/DHCP/板卡/用户/语音向导/LDAP/SIP trunk/SSH 密钥，p52）
  tags: [flow, lab-setup, ntp, certificate, did, sbc]

- id: f06
  title: 密码学三服务与两类算法对照结构（讲义骨架）
  type: structure
  source_pages: p5-11
  source_chapter: CRYPTOGRAPHY TERMINOLOGY / SYMMETRIC / ASYMMETRIC / DATA CONFIDENTIALITY / INTEGRITY & AUTHENTICATION
  source_quote: |
    "Symmetric algorithms : DES, AES… • It guarantees only confidentiality • 1 interlocutor = 1 key"
    (p6)
    "Asymmetric algorithms : RSA, ECC, Diffie-Helmman… • It guarantees confidentiality and integrity
    & allows to authenticate" (p7)
    "MAC combining hash and encryption with private key is also called digital signature" (p11)
  summary: |
    概念结构：三个安全服务——保密性（加密）、完整性（单向哈希，SHA-2/MD5，1 位改动影响一半哈希位）、
    认证（数字签名=私钥加密的哈希，即 MAC）。两类算法：对称（DES/AES，快、CPU 低、密钥分发难、
    一对通话者一把钥）与非对称（RSA/ECC/Diffie-Hellman，慢、无私钥不外传、一对密钥服务任意人数）。
    实际通信用混合模式：非对称传会话密钥（会话密钥每会话更换），对称加密数据（p9）。书中点名两条
    OXE 落点：IP Premium Security 用对称 MAC；OXE Native Encryption 的 binary 与 lanpbx.cfg 认证
    用非对称 MAC（p11）。
  conditions: 通识层，无版本前提
  tags: [structure, concept, cryptography]

- id: f07
  title: 证书内容与四种文件格式体系
  type: structure
  source_pages: p13-15
  source_chapter: WHAT IS A CERTIFICATE? / CERTIFICATES & FORMATS
  source_quote: |
    "Main ones: X.509 (RFC5280) and OpenPGP (RFC4880) • ALE is using X.509 v3 certificates" (p13)
    "The P7B file contains the certificate and its chain but does not contain the private key" (p15)
    "PKCS #12 or PFX/P12 format is a binary format for storing a certificate (including its
    intermediate) with a private key." (p15)
  summary: |
    证书内容三块：信息（签发者 issuer、持有者身份 subject/subjectAltName、有效期 notBefore/notAfter、
    序列号）、持有者公钥、CA 数字签名。DN 属性串（CN/OU/O/C），样例 CN=Wired Phones, OU=PKI
    Authority, O=Alcatel-Lucent, C=FR。四种格式：PEM（Base-64 ASCII 文本，.cer/.crt/.pem，Apache/
    Unix/Linux 系）；DER（二进制，Java 系）；P7B/PKCS#7（证书+链、无私钥，Java Tomcat 系）；PFX/
    P12/PKCS#12（证书+私钥、口令保护，Windows 系）。CSR 申请文件为 P10/PKCS#10（二进制、不含申请人
    私钥，p16）。OXE 全部支持（p103 导入组合表，见 f24）。
  conditions: 无版本前提
  tags: [structure, certificate, format, x509]

- id: f08
  title: PKI 三种证书生成模式及优劣对比
  type: structure
  source_pages: p18-22
  source_chapter: PKI & CERTIFICATE GENERATION PRINCIPLE / COMPARISON
  source_quote: |
    "Internal PKI: In case of Internal PKI, private keys, CSR, root CA and server(s) certificates are
    created by the system and managed internally • The Root CA certificate in this case is a
    self-signed certificate" (p18)
    "PKCS7/PEM/DER • Avantages: • Use of an external CA which can be referenced in PC clients • CSR
    done on server itself : automatic set of CN and SANs fields" (p22)
  summary: |
    三模式：①Internal PKI——密钥/CSR/根 CA/服务器证书全部系统内生成，根 CA 自签；优点是部署快、
    无需导入根证书，缺点是自签证书、客户端默认不认识内部 CA。②PKCS12（外部 CA 全包）——申请方
    密钥在 CA 生成，打口令包导入；优点是外部 CA 可被 PC 引用，缺点是私钥搬家、CA 侧手工 CSR 易错
    （错 CN、漏 SAN）。③PKCS7/PEM/DER——密钥与 CSR 在申请服务器本地生成，只回签证书；优点兼得
    （外部 CA+自动 CN/SAN），是全书实验主线。混合模式（p18 中列）为内外组合。
  conditions: 模式选择是交付方案的第一决策点
  tags: [structure, pki, comparison]

- id: f09
  title: 证书自动注册三协议对比（SCEP / EST / ACME）
  type: structure
  source_pages: p23, p84
  source_chapter: PKI & CERTIFICATE GENERATION PRINCIPLE: AUTOMATION / CERTIFICATES ENROLLMENT AND RENEWAL
  source_quote: |
    "SCEP & EST are used for device certificate enrollment (the certificate subject identifies the
    device), whereas ACME is used to issue domain validated certificate (the certificate subject
    identifies the domain)" (p23)
    "ACME: Automatic enrollment feature must be enabled (root account only), as it is disabled by
    default … Public CAs (e.g., Let's Encrypt) cannot be used, as this would require OXE to be
    publicly accessible for the HTTP challenge (HTTP-01 method)" (p84)
  summary: |
    三协议分工：SCEP（2000 年代初，网络设备注册，HTTP+共享密钥，续期支持有限）→用于 IP 话机导入
    自定义证书（ALE Basic/Enterprise/Essential 与 80x8s，8088 除外，p84）；EST（RFC7030，2013，
    TLS 强认证+内建续期）→用于 OXE-MS、GD4、GA4、GD-XL、GA-XL、GD3、INTIP3 的自动注册与到期续期
    （低于可配阈值自动续，IPMG 需重启切换新证书，事件 5779 成功/5780 失败）；ACME（RFC8555，2019，
    域名验证挑战）→仅用于 WBM 应用证书，OXE CS 作 ACME 客户端、cron 定期查过期，须本地支持 ACME
    的第三方 CA（Let's Encrypt 等公网 CA 因 HTTP-01 需公网可达而不可用），且 ACME 服务器须加入
    OXE 可信主机。
  conditions: ACME 默认关闭（root 启用）；PCS 不支持 ACME
  tags: [structure, scep, est, acme, automation]

- id: f10
  title: 端到端证书服务器认证三步图（CSR→签发→CTL 预置→连接）
  type: diagram
  source_pages: p24-25
  source_chapter: CTL (CERTIFICATES TRUST LIST) / END-TO-END CERTIFICATE-BASED SERVER AUTHENTICATION
  source_quote: |
    "CTL: the complete chain of certificates that has issued the end-entity certificate" (p24)
    "Step 3: opening a connection with A … Based on his trust store content, B can validate the
    received certificate. A has been authenticated" (p25)
  summary: |
    三步模型：Step1 证书请求——A 向 CA 发 CSR，CA 核身份后按 CSR+A 公钥制证，返回证书与 CTL；
    Step2 前置——A 收到的 CTL 必须预置进任何想连 A 的实体（B）的信任库（不预置 B 无法信任签发 A
    证书的 CA）；Step3 建连——B 发起连接，A 出示证书，B 按信任库验证（CA 公钥解签名+哈希校验），
    通过后建连。CTL 链结构：根 CA（自签）→中间证书（可多级）→终端实体证书，逐级签名。
  conditions: 该图是 OXE 端点-CS、EEGW-CS、SBC-OXE 所有 TLS 关系的抽象母版
  tags: [diagram, ctl, trust, authentication]

- id: f11
  title: FSNE 组件兼容三级矩阵（secured / non-secured / incompatible）
  type: structure
  source_pages: p63-64
  source_chapter: NATIVE ENCRYPTION AT A GLANCE / SCOPE
  source_quote: |
    "Secured components … Call Server (CS-3, CPU8, GAS, OXE-V) … Non secured components … SIP
    applications except VAA & DC … Incompatible components … Old ALE boards for CS & PCS: CS-2,
    CS-1, CPU7s2 & older … IPv6 • IP Premium Security" (p64)
  summary: |
    三级清单：已保护——Call Server（CS-3/CPU8/GAS/OXE-V）、被动 CS（CS-3/GAS/PCS-V）、Rainbow
    WebRTC GW、VAA、Dispatch Console、4645/AVST 留言、Premium Deskphone 80x8s、ALE Basic/Essential/
    Enterprise 话机、ALES、IPDSP、IP-xBS、GD4/GA4/GD3/GA3/GD-XL/GA-XL/INT-IP3A/B、OXE-MS、
    Hybrid/Direct Link ABC 组网、SIP 公网 trunk、IP/TDM DR-Link、远程工作者（SIP）；未保护（可共存
    明文）——VAA/DC 之外的 SIP 应用、老世代话机（80x8/40x8(EE)/808x）、老软电话（OTC）、Wi-Fi 81x8、
    IP-DECT、IOIP3 SIP 存活、T.38 传真；不兼容——CS-2/CS-1/CPU7s2 及更老板卡、GD/GA/INTIP/GD2/GA2/
    INTIP2 老板卡、IPv6、IP Premium Security、Backup Signaling Link、淘汰中组件。
  conditions: 选型与升级评估的对照表；存量盘点按此三级归位
  tags: [structure, scope, compatibility, matrix]

- id: f12
  title: Call Server 加密组件关系图（SIPmotor / NSP / IPSec Mgr / CA / EGW / A4645）
  type: diagram
  source_pages: p76
  source_chapter: CALL SERVER COMPONENTS
  source_quote: |
    "SIPmotor (CS and PCS) • Component in charge of SIP TLS signaling … SIP Translator (NSP: Nginx
    SIP Proxy) as alternative • Embedded in the External EGW … EGW … Acts as interface for endpoints
    instead of IPLink • Other flows don't transit via EGW (e.g. TFTP …)" (p76)
  summary: |
    组件分工：SIPmotor（CS/PCS 内嵌，管 SIP TLS 信令；NSP 为其外部替代，驻 EEGW VM）；IPSec Manager
    （仅 CS，基于 OpenSwan，建节点间 IPSec 链路）；Certificate Authority（仅 CS，证书管理组件，
    含端点 CTL 的信任库）；EGW（CS/PCS，DTLS 信令加密的端点接口，替代 IPLink 承载 NOE/IP-Link
    协议 over DTLS，只有信令过 EGW）；A4645 留言（libsrtp 直接管 SRTP，支持以太网冗余）；其余协议
    （SSH、TFTP 等）不过 EGW。全部配置在 Call Server 上完成。
  conditions: 理解后续所有拓扑的底图
  tags: [diagram, components, egw, sipmotor, architecture]

- id: f13
  title: EGW 内部/外部容量分界与会话计数公式
  type: structure
  source_pages: p77, p87-88, p109, p200
  source_chapter: INTERNAL / EXTERNAL ENCRYPTION GATEWAY / SOFTWARE LICENSE
  source_quote: |
    "1,500≤# DTLS/TLS sessions … 15,000≤1,500 < # DTLS/TLS sessions … ∑ Quoted number of NOE / SIP
    endpoints to be secured + 3 x total nber of GD4/GD4-XL/GD3/INTIP3B/OXE-MS + (3 x total nber of
    external SIP gateways) + 3 x total nber of nodes (direct link or hybrid link)" (p77, p109)
    "Topology available if there are less than 1500 concurrent SIP TLS / DTLS sessions" (p87-88)
  summary: |
    容量结构：内嵌 EGW ≤1500 并发 DTLS/TLS 会话；超出必须 EEGW（强制虚拟机、每 CS 一台、含 SIP
    Translator，上限 15000）。会话计数公式（DTLS 与 SIP TLS 合计）：受保护的 NOE/SIP 端点报价数
    （含 IPDSP、S 系话机、Essential/Enterprise 话机、ALES、ALE-x/ALE-30/ALE-x00、IP-xBS）+ 3×(GD4/
    GD-XL/GD3/INTIP3B/OXE-MS 板卡总数) + 3×外部 SIP 网关数 + 3×节点数（直连或 hybrid 链路）。EEGW
    需人工报价（无自动计数，Actis 系统级计数器管 #424 阈值）。
  conditions: PCS 侧同样适用（PCS 可内嵌或外接 EGW，p211）
  tags: [structure, capacity, licensing, formula]

- id: f14
  title: 一组件一证书体系（工厂证书/自定义证书/单一 CA）
  type: structure
  source_pages: p78, p83
  source_chapter: ONE CERTIFICATE FOR EACH COMPONENT
  source_quote: |
    "Factory certificate only for GD4, GA4, GD-XL & GA-XL boards, deskphones and IP-xBS • By the end
    of 2025, any newly produced board will embed a default ALE certificate" (p78)
    "One single Certificate Authority (CA) for all • All certificates management performed on a
    unique CA … Use case 1: OXE embedded CA … Component based on OpenSSL … Use case 2: External CA"
    (p78)
  summary: |
    证书发放结构：全系统一个 CA（CA 用例 1=OXE 内嵌 CA（OpenSSL），用例 2=客户企业 CA 或证书商）；
    端点证书可由另一 CA 签发（仅在双向认证时要求；SIP trunking 视管理而定）。工厂证书仅 GD4/GA4/
    GD-XL/GA-XL 板卡、话机与 IP-xBS 有；2025 年底起新产板卡默认嵌 ALE 证书；带工厂证书的板卡可
    部署在低于 R101.1 MD4 的版本上正常工作，只是用不了工厂证书（版本前提见 p78 图注）。自定义
    证书部署：手工，或话机走 SCEP（p78/p83 导入路径图：USB/CLI/SFTP/HTTPS(8378 WBM)）。
  conditions: 双向认证时端点证书为必备；服务器认证模式端点无需证书
  tags: [structure, certificate, factory, ca]

- id: f15
  title: 端点获取 CTL 的两条路径与 TOFU 原理
  type: flow
  source_pages: p79-80
  source_chapter: CERTIFICATE AUTHORITY & CERTIFICATE TRUST LIST
  source_quote: |
    "OXE supports up to 5 levels of CA hierarchy (Root CA→ Sub CA1 → Sub CA2…)" (p79)
    "First CTL acquisition is done in 'trust on first use' (TOFU) mode. TOFU principle consists in
    accepting that a factory-state endpoint … can establish its very first connection with a
    protected PBX without verifying the server certificate." (p80)
    "'Manual CTL Configuration' solution must be considered if the customer refuses the
    straightforward TOFU mode." (p80)
  summary: |
    路径 A 自动获取：OXE 把 CTL 打进 lanpbx.cfg 推送（仅 DTLS 兼容设备；SIP 扩展不适用——其配置
    文件给出 CTL 文件路径）。首连走 TOFU：出厂/空信任库端点第一次不验服务器证书直连，之后按存储
    CTL 全量认证。路径 B 手工配置：客户拒绝 TOFU 时，端点接 OXE 前逐台预置定制 CA 链——话机手工
    导入或 SCEP 批量；IPMG（软硬件）/IP-xBS 手工导入或 EST 自动注册（导入通道图：USB 口 GD 系板卡/
    CLI OXE-MS SFTP/SSH>HTTPS 8378 WBM/via SCEP）。
  conditions: TOFU 是安全折衷，需客户明示接受
  tags: [flow, ctl, tofu, acquisition]

- id: f16
  title: 服务器认证与双向认证（mTLS）握手对比
  type: structure
  source_pages: p81-83, p165
  source_chapter: CERTIFICATE-BASED AUTHENTICATION / MUTUAL AUTHENTICATION
  source_quote: |
    "Common Name in CS certificate is verified against the peer IP address during DTLS/TLS handshake"
    (p81)
    "If 'mTLS' is brought into service, certificate must be loaded in any IP deskphone, even those
    in clear mode • The first connection to OXE is always in secured mode" (p82)
  summary: |
    服务器认证：握手时 OXE（DTLS/TLS 服务器）出示证书，端点按信任库验证，CN 对照对端 IP。双向
    认证：OXE（EGW/sipmotor）在握手中反索端点证书并用信任库验证，证书身份与端点首个信令消息宣告
    的 MAC 地址比对。启用规则：配置激活，DTLS 端点全局一刀切、SIP TLS 端点全局一刀切、SIP trunking
    按外部网关逐个；激活后所有话机/软话机（含明文模式用户）都必须装证书、首连总是加密模式。支持
    范围：DTLS=Enterprise/Essential 话机、IPDSP(PC)、GD3、GD4、OXE-MS、IP-xBS（80x8s 自 R101.0 看
    OpenSSL level）；SIP TLS=Basic、Enterprise/Essential。证书要求：工厂 SHA-2 或定制 SHA-2，
    默认 SSL level 下密钥 ≥2048 位。
  conditions: 双向认证为可选增强（服务器认证为基线）
  tags: [structure, mtls, handshake]

- id: f17
  title: DTLS 兼容端点拓扑（内嵌 EGW 版）
  type: diagram
  source_pages: p87
  source_chapter: DTLS COMPATIBLE ENDPOINTS
  source_quote: |
    "'EGW' acts as DTLS server for the endpoints, which are DTLS clients • Each endpoint establishes
    a permanent DTLS session (Active – with Application DL link) with EGW" (p87)
  summary: |
    拓扑要点：EGW 对端点是 DTLS 服务器；每个端点与 EGW 建永久 DTLS 会话（Active，带应用 DL 链路）；
    兼容 Enterprise/Essential 话机与 Premium s 系（含内嵌 VPN 客户端方式）、IPDSP（Windows/Android）、
    IP-xBS、媒体网关 GD4/GD3/INTIP3/OXE-MS；支持以太网冗余。适用门槛：并发 SIP TLS/DTLS 会话
    <1500；超过即须外部 EGW（见 f28）。未加密的 NOE 话机仍走明文 NOE 信令+RTP，与加密侧共存。
  conditions: <1500 会话；明文/加密端点可混合（部分加密）
  tags: [diagram, dtls, egw, topology]

- id: f18
  title: SIP TLS 端点拓扑与冗余/PCS/远程工作者行为
  type: structure
  source_pages: p88-90
  source_chapter: SIP TLS COMPATIBLE ENDPOINTS / REMOTE WORKERS
  source_quote: |
    "OXE acts as TLS server, while the SIP SEPLOS endpoint acts as TLS client." (p88)
    "Each Call Server is addressed by its 'physical' IP address instead of their role IP address …
    The device maintains both TLS sessions with REGISTER refresh mechanism" (p89)
    "Based on the SIP 'Via' header of the 'REGISTER' message, which must contain one of SBC IP
    addresses known by the OXE (up to 10 SBC IP addresses for remote workers can be specified in
    the OXE DB)" (p90)
  summary: |
    结构要点：sipmotor 管 TLS，OXE 为 TLS 服务器、SEPLOS 端点为客户端；兼容 ALES（PC/Android/
    iOS）、Enterprise（ALE-x00）、Essential（仅 ALE-30）、Basic（ALE-x）话机与 OXE/OV8770 设备管理；
    不支持第三方与老 ALE SIP 设备。冗余：TLS anticipation——与两台 CS 各建一条 TLS 链路（按物理 IP
    非 role IP），REGISTER 刷新维持，standby 只接受受支持设备的 REGISTER。PCS：链路断时分支 SIP
    端点与本地 PCS 建 SIP TLS。ABC 网络仅 Direct Link 模式（stand-alone 需开 Direct Link 标签）；
    NE/SRTP 参数改动由 DM 自动更新设备配置文件并 NOTIFY。限制：SIP 端点 CCD agent 不支持、仅 IPv4。
    远程工作者：按 REGISTER Via 头里的 SBC IP（OXE 库最多录 10 个）动态识别，LAN 侧 SRTP 要求
    OT-SBC 与 OXE 间走 TLS 且用户开加密。
  conditions: 仅 SEPLOS 模式；<1500 会话内嵌，超出走 EEGW/NSP
  tags: [structure, sip-tls, redundancy, pcs, remote-worker]

- id: f19
  title: Native SIP TLS trunk 结构图与"信令/媒体分离"决定表
  type: diagram
  source_pages: p93, p160-161
  source_chapter: NATIVE SIP TLS FOR SIP TRUNK / OVERVIEW
  source_quote: |
    "Native SIP TLS feature can be used independently of OXE Native Encryption • If activated without
    Native Encryption, only SIP signalization is secured … But Native SIP TLS must be activated to be
    able to encrypt the media" (p93)
    "Ext. Gateway config: RTP or RTP/SRTP …→ Media: RTP / … Ext. Gateway config: RTP/SRTP …→ Media:
    SRTP" (p161)
  summary: |
    结构：SIP TLS 由 sipmotor 直接管或由 NSP（VM 上的 SIP 翻译器）管，SIP trunk 组类型须为
    "ISDN all countries"，端口 TCP/5061；支持 OXE 冗余与 PCS 本地 SIP 接入。信令/媒体分离决定表
    （p161）：NE 关闭时——网关配 RTP or RTP/SRTP 或 RTP → 媒体均 RTP（明文）；NE 开启时——网关配
    RTP → 明文、RTP or SRTP → 明文（与不支持 SRTP 对端）、RTP/SRTP → SRTP（信令与话音全加密）。
    兼容 OXE 冗余；PCS 有本地 SIP 接入时同样适用。
  conditions: SIP TLS with SSM 与 Native Encryption SIP TLS 不兼容（p159）；不兼容 IPv6
  tags: [diagram, sip-trunk, srtp, signaling]

- id: f20
  title: 应用生态加密要点图（Rainbow WG / 4645 VM / DR-Link-OPR / VAA / DC）
  type: structure
  source_pages: p94-99
  source_chapter: RAINBOW WEBRTC GATEWAY / 4645 VOICE MAIL / IP DR-LINK AND OMNIPCX RECORD / VAA / DISPATCH CONSOLE
  source_quote: |
    "SIP trunk group in 'SIP-ISDN mode' associated to an external SIP gateway with the 'Rainbow'
    variant" (p94)
    "4645 Voice Mail is automatically secured when it is hosted in an OXE where native encryption is
    activated • Only one system parameter to activate" (p95)
    "The maximum number of VAA ports is decreased from 120 to 60 in case of encryption" (p98)
  summary: |
    五个应用出口的加密路径：①Rainbow WebRTC GW——SIP 信令恒加密、音频仅在 OXE 端点受保护时加密；
    仅网关侧认证（Rainbow 网关为 TLS 服务器）；trunk 组用 "SIP-ISDN mode" + Rainbow 变体外部 SIP
    网关；加密非强制，可明文跑。②4645 VM——宿主在开了 NE 的 OXE 内则自动受保护，仅一个系统参数
    （System/Other System Param./Voice Mail Parameters）；独立服务器部署则需改 eva.cfg 加 DTLS 参数+
    4645 证书（IP 须入 SAN）；明文话机打加密 VM，话音 RTP 不加密。③IP DR-Link 与 OmniPCX Record
    ——CSTA 链路 TLS 1.2 强制、仅认证 CS；录音能力（明文/AES-128/AES-256）由 Recording SRTP Cipher
    Suite 决定；每次保持/会议/转接换新钥、OPR 即时解密复制流。④VAA——SIP TLS（internal ABC-F 型）+
    可选 mTLS（OXE CTL 手工导入 VAA，VAA CTL 导入 OXE）；加密后端口上限 120→60。⑤Dispatch Console
    ——同 VAA 路径，端口数不受影响（仍 120）；话务员设备可按普通设备加密。
  conditions: 各应用的前提细节见对应页
  tags: [structure, applications, voicemail, recording, vaa, dc]

- id: f21
  title: ABC-F 网络加密四类呼叫拓扑（transit 节点行为）
  type: diagram
  source_pages: p293-301
  source_chapter: NATIVE ENCRYPTION FOR ABC-F NETWORK (lecture)
  source_quote: |
    "Signaling between the network nodes is encrypted using IPsec • Certificate based authentication
    for IPsec tunnel establishment between nodes • Media encryption … is done using SRTP keys sent
    over the encrypted ABCF network" (p293)
    "'Transit node' concerns only 'IP Hybrid Link' based network • No transit node in a 'Direct IP
    Link' based network" (p297-298)
  summary: |
    总原则：节点间信令（ABC-F、审计、广播）用 IPSec（IPSec Manager 建，端口协商 500/管理 2579），
    IPSec 隧道用证书认证（全网一个 CA、每节点一张专属证书）；媒体加密的 SRTP 密钥经加密的 ABC-IP
    逻辑链路下发对端。四类拓扑：①transit 节点支持 NE 且全链路加密→Node1-Node3 语音 SRTP 加密；
    ②transit 节点支持 NE 但 Node2-Node3 链路未加密→Node1-Node3 语音 RTP 明文（短木桶效应）；③
    transit 节点 NE + 原生 SIP TLS 对运营商→Node1-外网全加密；④信令链路加密但对端端点未保护→
    RTP 明文。注意 transit 只在 hybrid link 网络存在，direct link 无 transit。
  conditions: 全部所涉节点 NE 开启+全部所涉链路两端勾 Encryption 才能加密（p295）；hybrid 网络含 transit 节点
  tags: [diagram, abc-f, ipsec, topology]

- id: f22
  title: 管理面地图——WBM/8770/mgr 配置 + netadmin 菜单树 + lanpbxbuild 选项
  type: structure
  source_pages: p101, p104, p113, p205, p219-221, p246-247, p267-268
  source_chapter: CONFIGURATION 及各实验章 netadmin 输出
  source_quote: |
    "Feature activation & deployment options via OXE WBM or OmniVista 8770 … Certificate Authority,
    certificates and CTL management via netadmin OXE CLI tool" (p101)
    "11.9.1.CS Certificate management … 11.9.2.PCS Management … 11.9.3.Endpoint CTL (Trust Store) …
    20.Encryption GW Management … 19.2.Translator Name configuration … 17.Node setup" (p104-268 各实验输出)
  summary: |
    管理三分：①数据库参数（System/Other System Param. 下 Native Encryption parameters、SIP
    Parameters、Voice Mail Parameters 等）走 WBM 或 OmniVista 8770 或 mgr；②证书与网络底层走
    netadmin -m 菜单树：11.1.3 受限访问（内部防火墙信任主机）、11.6.3 SSL security level、11.9.1
    CS 证书管理（1 自动生成/2 CSR/3 网络签发导入/4 导入/5 导出/6 本地签/7 删除/8 查看）、11.9.2 PCS
    管理（2 CSR/3 导入/4 导出/5 查看）、11.9.3 端点 CTL（导入/查看/删除）、17 Node setup（内部 DNS）、
    19 域管理（19.1 OXE 域名、19.2 Translator 名）、20 EGW 管理、10 Copy setup（copy to twin）；
    ③lanpbxbuild 工具（-auto 一键生成；4→1 后 j/k=DTLS1/2 地址、l=端口、n=OXE FQDN、d/e/f=证书
    服务器；6=Apply changes 签名）。EEGW/OMS/GD 板卡另有 ostconfig/omsconfig/mgconfig 三件套。
  conditions: 菜单号是全书实验的导航坐标，生产操作按同路径
  tags: [structure, netadmin, wbm, menu-path, tools]

- id: f23
  title: PKI 管理决策树（密钥在哪生成→证书在哪签发）
  type: diagram
  source_pages: p102
  source_chapter: PKI MANAGEMENT - REMINDER
  source_quote: |
    "CS key pair generated locally? NO → CSR is signed by external CA, CS certificate issued
    externally … YES → CS key pair generated externally, Certificates issued externally" (p102)
  summary: |
    决策树两问：①CS 密钥对本地生成吗？否→本地造 CSR 送外部 CA 签发，导入 CA+CS 证书（PKCS#7/PEM/
    DER 格式路线）；是→密钥对在 CA 侧生成、证书外部签发，导入 CA+CS 证书+CS 密钥对（PKCS#12 格式
    路线）。②CA 与 CS 密钥对都本地生成？是（内嵌 CA）→本地自动生成一切（Internal PKI）。该树
    对应 p103 的导入组合全表（见 f24）。
  conditions: 与 f08 三模式一一对应
  tags: [diagram, pki, decision]

- id: f24
  title: OXE 证书导入格式组合全表（full/partial/all-in-one）
  type: structure
  source_pages: p103-106
  source_chapter: IMPORT OF CERTIFICATE INTO OXE
  source_quote: |
    "Full import (CA certificates chain, CS certificate & CS keys pair) • Partial import (CA
    certificates chain & CS certificate w/o keys pair)" (p103)
    "Do you want to import all in one file(PKCS#12/PKCS#7/PEM) (y/n default n)?" (p104-106)
  summary: |
    三用例：Use case 1 全量导入——CA 链 PEM 文件 + CS 证书及密钥对的 PKCS#12 文件（要口令）；Use
    case 2 全量 all-in-one——单个 PKCS#12 文件同时装 CA 链+CS 证书+密钥（也支持 CA 链+CS 证书单个
    PEM 无私钥）；Use case 3 部分导入——CA 与 CS 证书分开（如均 DER），CS 密钥对与 CSR 由 OXE 本地
    生成、CSR 导出外部 PKI。导入菜单：netadmin 11.9.1.4，问答式（all in one? → CA 文件路径 → CS
    文件路径 → PKCS#12 口令），完成后 /tmp/cs_cert.pem: OK + Certificates Successfully Imported。
  conditions: 导入后须 lanpbx 再生成+OXE 重启（见 n 系列警告条目）
  tags: [structure, import, formats]

- id: f25
  title: EEGW/SIP Translator 部署六步主流程（CS 侧）与 PCS 侧五步
  type: flow
  source_pages: p204-210, p212-215
  source_chapter: External EGW Deployment - Call Server / Passive Call Server
  source_quote: |
    "Step 1: Declare the EEGW and the SIP Translator • Dedicated menus in 'netadmin' tool … Step 4:
    Configure the « lanpbx.cfg » … The DTLS server will be the external EGW IP @ … Step 6: Set up
    EEGW IP configuration and download the certificates from the CS to the EEGW" (p204)
    "PCS EGW IP address' possible values: IP @ of the PCS: … the internal Encryption Gateway of the
    PCS gets active • IP @ different from PCS IP @: … an external EEGW … is associated to the PCS"
    (p213)
  summary: |
    CS 侧六步：①netadmin 20 声明 EEGW（每 CS 一台）+19.2 声明 SIP Translator（名字 nsp）；②
    netadmin -m 管 PKI 与证书（SAN 须含 EEGW 地址/FQDN/通配符/Translator FQDN）；③照常配 NE 参数
    （EEGW IP 自动关联进 mao）；④lanpbx.cfg 的 DTLS 服务器填 EEGW IP（默认端口 32643）；⑤装 EEGW
    虚拟机（OST 包，Rocky Linux，机器类型 EEGW/OST64）；⑥ostconfig 配 EEGW IP（含 CS 物理/角色地址）
    并从 CS 下载证书（EEGW 下载完自动重启）。PCS 侧五步：OXE 库配 PCS（PCS EGW IP：等于 PCS IP=
    内嵌 EGW；不同=外接 EEGW）→CS 上管 PCS 证书→pcscopy 拷证书到 PCS→装 EGW VM→从 PCS 下载证书。
    部署警告：EEGW IP 必须加入 CS 内部防火墙；Translator FQDN 必须可解析（内部 DNS 或外部 DNS 委托）。
  conditions: 改 EEGW/Translator 声明都要求重生成 CS 证书+OXE 重启（p219/p247 警告）
  tags: [flow, eegw, deployment, pcs]

- id: f26
  title: 内部 EGW → 外部 EGW 迁移四阶段流程
  type: flow
  source_pages: p216
  source_chapter: Migration from internal EGW to External EGW
  source_quote: |
    "External EGW IP Configuration in the mao • Declare the External EGW IP address in 'netadmin' •
    Automatic update of MAO … Certificates Regeneration • Regenerate certificates with external EGW
    IP of main and standby as SAN fields … Lanpbx Rebuilding … OST/EGW Virtual Machine • Install and
    configure the Virtual Machine … Reboot the system" (p216)
  summary: |
    迁移四阶段+收尾：①在 mao 声明外部 EGW IP（netadmin 声明自动更新 mao；PCS 场景在 PCS 管理里填
    外部 EGW IP）；②重生成证书（主/备 EEGW IP 入 SAN；有 PCS 时在 CS 重生成带 PCS 外部 EGW IP 的
    PCS 证书并 pcscopy）；③重建 lanpbx 文件（DTLS 1=CS1 的 EEGW IP、DTLS 2=CS2 的 EEGW IP）；④
    安装配置 OST/EGW 虚拟机（ostconfig 下载证书、重启 OST 机）；最后整体重启系统。
  conditions: 迁移期间两端点重新下载 lanpbx.cfg 后才会改连 EEGW
  tags: [flow, migration, eegw]

- id: f27
  title: S.O.T. 生成与加载 EEGW 虚拟机的工厂流程
  type: flow
  source_pages: p272-282
  source_chapter: OST/EGW generation & loading with S.O.T. deployment tool
  source_quote: |
    "Select 'Greenfield' project for an installation from scratch … Machine type EEGW … EEGW Sizing
    Specify the maximum number of users who will be able to use this EEGW" (p274-276)
    "Log on EEGW VM (default login/password: root/letacla1). Change the password (e.g.
    Superuser2580*)." (p279)
  summary: |
    七步：①备好 BootDVD 与 OST 软件 ISO（实验取自 NAS，可先拷到本地 PC 提速）；②浏览器（仅
    Chrome/Firefox 受支持）登 S.O.T.（https://192.168.1.194，admin/Superuser2580*，实验口径），建
    Greenfield 工程，产品类型 OST，本地存储；③媒体缺失时经 FTP（upload/sot）传 BootDVD.iso 与
    OST.iso→Refresh medias list→Declare medias；④工程设置（OVF Generation 勾选=S.O.T. 生成 ovf、
    国家/时区、机器类型 EEGW、主机名 eegwcpua、EEGW Sizing、IP 192.168.1.7）→Deploy→下载 .ova；
    ⑤ESXi 管理界面部署 .ova；⑥开机自动加载，完成后出现 eegwcpua 登录（Rocky Linux 9.7）；⑦首次
    root/letacla1 登录改密（Rocky 密码规则：≥14 位、2 字母含大写、2 数字、1 特殊、不含用户名/连续
    4 同符/4 顺序符/字典词、不与前 24 次重复），再 ostconfig 配 IP 与 CS 地址。收尾：CS 内部防火墙
    加 EEGW 信任主机（见 f25）。
  conditions: S.O.T. 为 ALE 部署工具；实验口径 SOT VM IP 192.168.1.194
  tags: [flow, sot, eegw, vm, deployment]

- id: f28
  title: Native SIP TLS trunk 双侧配置总流程（OTSBC 侧 + OXE 侧 + NSP 切换）
  type: flow
  source_pages: p173-184, p185-193, p264-271
  source_chapter: SIP TLS configuration in OTSBC / Native SIP TLS and SRTP for SIP Trunk / with SIP translator for public SIP TLS Trunk
  source_quote: |
    "SETUP / IP NETWORK / SECURITY / TLS contexts … Index 1, Name OXE TLS, TLS Version TLSv1.2 …
    DH key Size 2048" (p175)
    "SIP / SIP Ext. Gateway … Transport type TLS Client" (p188)
    "Proxy Address Enter: nsp.oxe.company.com:5061 … NSP FQDN is mandatory as soon as CS redundancy
    is implemented" (p266)
  summary: |
    三段总流程：①OTSBC 侧（p173-184）——建 TLS context（TLSv1.2/DTLSv1.2，Cipher AES256:AES128，
    DH 2048）→导入 RootCA→生成 4096 私钥→生成 CSR（CN=SBC IP，SHA-256）→CA 签发后导入 .cer→
    SIP Interfaces（OXE 侧）挂 context 并开 TLS 5061→Proxy Set（OXE）地址改 5061/TLS→Media Security
    Enable（AES-CM-128-HMAC-SHA1-80）→IP Profile OXE 设 Offer Both–Answer Prefered Secure 兼容
    未加密用户。②OXE 侧（p185-193）——TLS signaling possible=Yes（重启 CS）→外部 SIP 网关（远程域
    =SBC IP、端口 5061、TLS Client、SRTP=RTP or SRTP）→本地 SIP 网关 TLS(Server Auth.) 端口 5061→
    SRTP offer answer mode=True→Authentication for SRTP=Authenticated→重启 sipmotor→必要时导入
    SBC CTL（11.9.3）→sipextgw/cryptview 验证。③EEGW/NSP 场景（p264-271）——SBC 侧 Proxy Set 地址
    改为 nsp.oxe.company.com:5061；OXE 激活内部 DNS（netadmin 17.2），外部 DNS 把委托域转发给 OXE
    （仅主 CS 会应答→返回主 CS 的 EEGW IP）；SBC console ping 验证解析后全链路加密。
  conditions: 冗余场景必须用 NSP FQDN（单机可用 EEGW IP 直填）
  tags: [flow, sip-trunk, otsbc, nsp, dns]

- id: f29
  title: 端点证书部署矩阵（OMS/GD 板卡 / IPDSP / IP 话机 三线）
  type: structure
  source_pages: p356-360, p367-375
  source_chapter: Native Encryption & mTLS / Appendix: Certificates download in the Endpoint
  source_quote: |
    "The IPMG CERTIFICATES ARE 'END ENTITY' TYPE CERTIFICATES. THE CERTIFICATE MUST BE IMPORTED WITH
    PKCS12 … INTO THE OMS VIRTUAL MACHINE IN THE '.PFX' FORMAT" (p356)
    "Certificate files … named exactly as the following: 'softphone_cert.pem' for certificate •
    'softphone_pkey.pem' for private key" (p360)
    "Using the 'SCEP' protocol, sets are able to get automatically their certificate." (p375)
  summary: |
    三条部署线：①IPMG 线（OMS/GD4/GD3）：End Entity 类型 .pfx（GW.pfx，CN=板卡 MAC），omsconfig/
    mgconfig 先开 SSH（option 6/9，按 PC IP 限时开放并事后撤销）→Certificate management→3 导入
    网关证书→2 经 SFTP 接收并解包→输口令→Print certificates 核验→保存并重启；GD 板卡经 V24 串口
    登录（GD3 9600-8-N-1、GD4 11520-8-N-1，原文数值照录）。②IPDSP 线两法：文件法——softphone_
    cert.pem + softphone_pkey.pem（加密导出）放安装目录，DTLS_PKEY_PASSWORD 装机参数或
    DTLSPkeyPassphrase.exe /set <口令> 绑定；Windows 证书库法——.pfx 装入本机个人库，装机参数
    DTLS_CERT_NAME 指定 CN 检索。③话机线三法：手工（开机 I+# 进 Security/Certificate/Get
    Certificate 填 HTTP/端口/路径）；lanpbxbuild 写 CERTSRV 参数（d/e/f）自动下发参数后话机手工点
    Get Certificate；SCEP 全自动。工厂证书话机免部署（ALE 根 CA CTL 预置在 OXE 信任库）。
  conditions: 文件命名严格匹配；mTLS 激活后所有话机都要有证书（含明文用户）
  tags: [structure, endpoint, certificate, deployment]

- id: f30
  title: SIP TLS 端口模型——Server Auth 5061 / Mutual Auth 6261 四组合
  type: structure
  source_pages: p166-168, p377-379
  source_chapter: MUTUAL AUTHENTICATION / mTLS Appendix: Public SIP trunk
  source_quote: |
    "No SIP-TLS: (Server Auth.) Port -> 0 / (Mutual Auth.) Port -> 0 … SIP-TLS with simple and mutual
    authentication: (Server Auth.) Port Number -> 5061 (Mutual Auth.) Port Number -> 6261" (p167)
    "setting the SIP TLS (Mutual Auth.) port number as '0' overrides the SIP-External Gateway
    Parameter: 'SIP TLS Mutual Authentication parameter: True' … In MAO, this parameter will not
    change to 'False' automatically" (p167)
  summary: |
    端口模型：本地 SIP 网关两个端口参数——SIP TLS (Server Auth.) 默认 5061、SIP TLS (Mutual Auth.)
    默认 6261（均可改，改后需重启 SIPmotor 生效）。四组合：0/0=无 SIP TLS；5061/0=仅服务器认证；
    0/6261=仅双向认证；5061/6261=两者并存。陷阱：互认证端口填 0 会覆盖外部网关参数 SIP TLS Mutual
    Authentication=True（该网关实际关闭互认证），且 MAO 界面不会自动变 False。配套：外部网关侧配
    Transport type（TLS Client/TLS Server）+ SIP TLS Mutual Authentication=True（sipmotor 重启生效）；
    OTSBC 侧 Proxy Set/SIP Interface 的端口要与 OXE 侧两两对齐（host 可为主 CS IP/FQDN/NSP FQDN）。
    SIP 扩展（SEPLOS）互认证另走系统参数 SIP TLS Mutual Authentication（节点重启生效）。
  conditions: 端口号可自定义但两侧必须一致
  tags: [structure, ports, mtls, sip-tls]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-18）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | 密码学与证书基础 | 有 | f06, f07, f08, f09, f10 | 三服务/两算法、格式体系、PKI 三模式、注册协议、信任建立图 |
| task-02 | Pod 实验环境搭建 | 有 | f02, f05 | stand-alone 拓扑表 + 初始配置流程 |
| task-03 | SIP 模拟器使用 | 有 | f04 | ITSP2 拓扑与号码变换 |
| task-04 | CSR 签发导入闭环 | 有 | f23, f24, f22 | 决策树、导入组合表、netadmin 菜单树 |
| task-05 | 系统/用户级加密参数 | 有 | f22 | WBM 参数块路径（数值细节归 principle） |
| task-06 | lanpbx.cfg 生成维护 | 有 | f22, f23 | lanpbxbuild 选项结构（字段细节归 principle） |
| task-07 | DTLS 验证与维护 | 有 | f12 | 组件图为排障底图（命令口径归 principle/case） |
| task-08 | Wireshark 抓包验证 | 无独立框架条目 | （c03） | 纯操作序列，归 case.md；流程无结构性新知 |
| task-09 | SIP TLS 扩展 | 有 | f18 | SEPLOS 拓扑与冗余/PCS/远程行为 |
| task-10 | PCS 接管 | 有 | f18, f25 | PCS 行为 + 部署五步 |
| task-11 | SIP trunk TLS/SRTP | 有 | f19, f28, f30 | 信令/媒体分离表 + 双侧总流程 + 端口模型 |
| task-12 | 安全停用 | 无独立框架条目 | （c08） | 四步回退为操作序列，归 case.md |
| task-13 | EEGW/NSP 部署 | 有 | f12, f13, f25, f26 | 组件关系、容量分界、六步部署、迁移四阶段 |
| task-14 | S.O.T. 生成 EEGW | 有 | f27 | 工厂七步流程 |
| task-15 | 网络实验室改造 | 有 | f03 | Node1/Node2 拓扑与 IP 接口改造 |
| task-16 | ABC-F 网络加密 | 有 | f21 | 四类呼叫拓扑与 IPSec 结构 |
| task-17 | XCA 端点证书 | 有 | f14, f29 | 证书体系 + 端点部署矩阵（XCA 软件操作归 case） |
| task-18 | mTLS 启用与限制 | 有 | f16, f29, f30 | 双向认证结构、部署矩阵、端口模型 |

补充说明：
- f01（课程主线）、f11（兼容矩阵）、f17（DTLS 拓扑）、f20（应用生态）不直接对应单个 task，属于 BOOK_OVERVIEW 骨架 3-6 的框架底座。
- task-08/12 无框架类内容（纯操作序列），已在 case.md 覆盖，不构成缺口。
- 生产化边界提示（来自 BOOK_OVERVIEW 批判节）：CA 运营治理、EEGW VM 规格、trunk/EEGW 侧抓包位置在书外，各框架条目落地时需显式指向 OXE 安装/维护文档与客户安全策略。
