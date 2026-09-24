# 案例/实验/操作序列候选 — OmniPCX Enterprise 原生加密 (ENTPXTE421EN Ed05)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号）标注"实验口径"。
> 条目说明: 全书 19 个 How-To 实验章逐章一条（c01-c19），无合并拆分。

```yaml
- id: c01
  title: Pod 初始配置（NTP、根 CA 证书、板卡/用户、DID/NPD/SBC/NAT 公网接入）
  type: lab
  source_pages: p48-57
  source_chapter: Pod Configuration: Native Encryption
  source_quote: |
    "Manage the following NTP server for all the PC clients (used in this training): 192.168.1.252"
    (p50)；"Install manually the certificate of the Root CA on all the client PCs … trust store"
    (p51)；"First external number 33920N31000 (where N is your POD Number) … First internal number
    31000 … Range Size 500" (p54)
  steps: |
    1. 按需启动 VM：先不起 ENTP_PCS_FSNE、ENTP_EEGW_CSA、ENTP_EEGW_CSB（后续实验再启动）（p49）。
    2. NTP：客户端 PC 控制面板 → Clock and Region → Date and Time → Internet Time → Change settings
       → 填 NTP 192.168.1.252（实验口径）→ Update now（p50）。
    3. 根 CA 证书：从 NAS 的 ENTPXTE421/Certificates 目录取 ca-certgen → 右键 Install Certificate →
       Open → Local Computer → Trusted root certification authorities → Next → Finish（导入成功）（p51）。
    4. 核对 OME 预配置（已做）：许可/内部防火墙/NTP/FlexLM(192.168.1.80)/DHCP（VLAN1 192.168.1.145-
       149，VLAN2 192.168.2.145-149）/机架板卡/用户/语音向导/LDAP(ALES)/公网 SIP trunk/SSH 密钥（p52）。
    5. 核对板卡：主站点 OMS Rack 4（Virtual GD4 slot 0，IP 192.168.1.13/24，MAC 00:50:56:01:01:13）；
       远端 Rack 6（192.168.2.13，MAC 00:50:56:02:01:13）（p52）。
    6. 装软话机：IPDSP 31000/31002/31003 与 ALES 31030/31031 按用户表装机；IPDSP Settings→Network 填
       TFTP=192.168.1.3；ALES 安装时 local access=192.168.1.3，登录 31030=eevans/alcatel、31031=
       eeastwood/alcatel（实验口径）（p52-54）。
    7. DID 翻译：Translator/External Numbering Plan/Default DID num. translator → Create → First
       external number=33920N31000（N=POD 号）、First internal number=31000、Range Size=500（p54）。
    8. NPD：Translator/External Numbering Plan/Numbering Plan Description (NPD) → 编辑 NPD 33 →
       Default number (num. inst. sup.)=33920N31000（p55）。
    9. SBC NAT：浏览器 https://192.168.1.105（Admin/Admin，实验口径）→ SETUP/IP NETWORK/CORE
       ENTITIES/NAT Translation → 两条规则 Target IP Address 改为 SBC NAT 地址（规则 12.班级号.POD号
       .105，如班级 2、POD 4 = 12.2.42.105）→ Apply → Save（p55-56）。
    10. SBC 账号：SETUP/SIGNALING & MEDIA/SIP DEFINITIONS/Accounts → 编辑既有账号 → Contact User 与
        User Name 均改 podN → Apply → Save；Action 菜单 Register 立即注册（p56-57）。
    11. 外呼验证：按 SIP Carrier Simulator 文档做 Barkley ↔ 公网用户互打（p57）。
  verification: |
    公网 SIP carrier 出局/入局呼叫正常（p57 "To make sure that access to public SIP carrier is
    working properly"）。
  conditions: OXE VM 已预配置（p52 清单）；全部 IP/口令为实验口径。
  tags: [lab, pod-setup, ntp, certificate, did, npd, sbc, nat]

- id: c02
  title: DTLS 设备原生加密主线实验（PKCS#7 证书闭环 + 参数 + lanpbx + 验证 + 维护）
  type: lab
  source_pages: p111-133
  source_chapter: Native Encryption for DTLS compatible equipment's
  source_quote: |
    "Run 'netadmin -m' command Option 11.9.1.2 'Generate CSR'" (p113)；
    "Enter the CA file …: /tmpd/ca.p7 Enter the CS file …: /tmpd/cs.p7b" (p116)；
    "System / Other System Param. / Native Encryption parameters" (p119)；
    "(1)csa> lanpbxbuild … 6. Apply changes" (p121-123)；"Reboot the OXE Call server(s)" (p125)
  steps: |
    1. 生成 CSR：OXE 终端 mtcl 登录 → su - root → netadmin -m → 11.9.1.2 Generate CSR → 交互作答：
       通配符 SAN=y；SAN 配 IP 地址=n（无 IP 证书口径）；附加 SAN=n；密钥 4096；填国家 FR/州 BZH/城市
       BREST/组织 ALE/部门 EDUC → 确认 → 导出路径默认 /tmpd → 生成 /tmpd/csa.csr（p113）。
    2. 提交签发：Filezilla SFTP 连主 CS（远程 /usr4/tmp）→ 把 .csr 拷到共享盘 Y:(\\10.20.30.200\Sharing)
       的 PODx 目录 → 等 CA 管理员（trainer）签发 → 取回 cs.p7b（PKCS#7/DER）（p115）。
    3. 导入：ca.p7（CA_Certificates 目录）与 cs.p7b（PODx 目录）经 Filezilla 放到主 CS /tmpd →
       netadmin -m → 11.9.1.4 Import CS Certificates → all-in-one=n → CA 文件 /tmpd/ca.p7 → CS 文件
       /tmpd/cs.p7b → "without IP address in SAN?" 答 y → Certificates Successfully Imported → 删除
       /tmpd 与共享盘中的 csa.csr/cs.p7b/ca.p7（教学清洁）（p116-117）。
    4. 核验：netadmin -m → 11.9.1.8 View → 依次看 CA/Call Server/Network 证书（issuer/subject/
       notBefore/notAfter/SAN=DNS:oxe.company.com, DNS:*.company.com）（p118）。
    5. 复制 twin：netadmin -m → 10.Copy setup → 2.Copy to twin CPU (all) → 完成后 mtcl 执行
       dhs3_init -R NGINX（p118）。
    6. 系统参数：System/Other System Param./Native Encryption parameters → Enable Native encryption
       =True、Enable automatic CTL Acquisition=True、Authentication for SRTP=Authenticated（p119）。
    7. 用户级加密：Users → 选 31000/31002/31003 → 8&9 Series Parameters → Native encryption=Enable；
       核对其 NOE and SIP extension Phone COS；Phone COS/0 页 Display Encrypted Communication=YES（p120）。
    8. lanpbx.cfg：mtcl → lanpbxbuild -auto（新装口径，会重置 IP_CPU/IP_DOWNLOAD 外配置）→ lanpbxbuild
       → 4 Modify → 1 选行 → 选行 1 → j 填 DTLS1=192.168.1.1、k 填 DTLS2=192.168.1.2、（可选 n 填
       OXE FQDN）→ 0 逐级返回 → 6 Apply changes（输出 CTL_sign OK 与 Native Encryption signing）→
       重启 OXE CS（p121-125）。
    9. EGW 核查：WBM IP/Encryption GW（重启后非空）：EGW IP=CS IP → 内部 EGW（p126）。
    10. IPDSP 验证：启动 IPDSP（若 PC 不认识 CA 则弹证书提示，选 Accept permanently）→ 31000 与
        31002 互打 → 通话出现加密图标（p127）。
    11. 维护：spadmin（option 2）查许可 359/424；ippstat 31000（option 2/3）；twin（Communication
        Mode: Crypted）；cryptview（System is DTLS secured、参数快照）；incvisu/incinfo 看事件
        5991/5992/5993/5995；netadmin -m 11.9.1.5.1 导出证书备份（p129-133）。
  verification: |
    31000↔31002 通话加密图标出现（p127）；cryptview 显示 "System is DTLS secured"（p131）；twin 显示
    "Communication Mode: Crypted"（p130）。
  conditions: 实验口径 IP/口令；duplication 环境须在 main CS 跑 lanpbxbuild 并 copy to twin。
  tags: [lab, dtls, csr, pkcs7, netadmin, lanpbx]

- id: c03
  title: Wireshark 抓包验证媒体加密（话机端口镜像 + RTP 解码）
  type: lab
  source_pages: p134-138
  source_chapter: Wireshark traces
  source_quote: |
    "'mirror set lan' (to activate the port mirroring) 'mirror set idle' (to de-activate)" (p135)；
    "Go to 'Analyze/Decode as' … select RTP" (p136)；"press the 'Play' button to check whether the
    communication is encrypted or not" (p138)
  steps: |
    1.（IPDSP 直接跳步骤 4。）话机 COS：NOE and SIP extension/NOE and SIP COS/Phone COS → State 页
       PC Port 置 Cascad. not filt.（PC 口不过滤，且分机须 in service）（p135）。
    2. 开镜像：OXE 终端 mtcl → tnet d <分机号>（如 31010；默认口令 *tx8000#）→ mirror set lan → exit
       （关闭用 mirror set idle）（p135）。
    3. PC 接话机 PC 口，启动 Wireshark，双击网卡开始抓包（p136）。
    4. 解码 RTP：选中第一条 UDP 报文 → Analyze → Decode As → 点 "+" → Current 字段选 RTP → OK（若
       无 RTP 流则此步必做）→ trace 中出现 RTP 报文（p136-137）。
    5. 听流验证：选 RTP 报文 → Telephony → RTP → Stream Analysis → Player Stream → 选两路音频流 →
       Play：加密时听到噪音（明文时听到语音）（p137-138）。
  verification: |
    RTP Stream 播放为不可辨识噪音 = 媒体已加密（p138 "check whether the communication is encrypted
    or not"）。
  conditions: 话机 PC 口需先在 Phone COS 放开；IPDSP 场景直接从 1.3 开始。
  tags: [lab, wireshark, rtp, port-mirroring]

- id: c04
  title: SIP TLS（sipmotor）加密 ALE SIP 扩展
  type: lab
  source_pages: p139-145
  source_chapter: Native Encryption for TLS compatible SIP extensions
  source_quote: |
    "TLS signaling: True • SRTP offer answer mode: True • Loose Route with RegID: False" (p140)；
    "SRTP Working mode Best Effort … 'None' means RTP: audio flow is in clear mode" (p141)；
    "Run a SIP trace (motortrace 3) and look for the 'X-ALE-CALL-ENCRYPTED' information and TLS
    signaling" (p142)
  steps: |
    1. 前提：承接 c02——CA/CS 证书已加载、NE 主参数已配（p140）。
    2. 系统参数：System/Other System Param./SIP Parameters → TLS signaling possible=True、SRTP offer
       answer mode=True、Loose Route with RegID=False → 重启 CS（或双 bascul）使 TLS 端口进入监听 →
       netstat -an | grep 5061 验证（p140-141）。
    3. 用户参数：Users → 选 ALES 用户 31030/31031 → SIP Extension Parameters → Native encryption=
       Enable、SRTP Working mode=Best Effort（None=RTP 明文）；核对其 Phone COS（p141）。
    4. 加密图标显示：NOE and SIP extension/NOE and SIP COS/Phone COS/0 → Display Encrypted
       Communication=YES（p142）。
    5. 验证：ALES 间互打看盾牌图标；mtcl 执行 sipregister（contact 带 :5061, TLS）；csipsets（TLS/SRTP
       列 YES/AES128）；motortrace 3 + traced 抓 SIP trace：INVITE 的 Via 为 SIP/2.0/TLS、SDP 含
       m=audio … RTP/SAVP 与 a=crypto:AES_CM_128_HMAC_SHA1_80、ACK/200 OK 带 X-ALE-CALL-ENCRYPTED: YES
       （p142-145）。
  verification: |
    sipregister 显示 TLS 注册；csipsets 显示 TLS/SRTP=YES；SIP trace 出现 [TLS]、RTP/SAVP、
    X-ALE-CALL-ENCRYPTED: YES（p143-145）。
  conditions: 仅 SEPLOS 模式设备（ALES/ALE-x00/ALE-30/ALE-x）；IPDSP 之外的老 SIP 设备不支持。
  tags: [lab, sip-tls, sipmotor, ales]

- id: c05
  title: PCS 加密接管（声明、PCS 证书、pcscopy、断网演练与恢复）
  type: lab
  source_pages: p146-156
  source_chapter: PCS & Native Encryption
  source_quote: |
    "sudo omsconfig … 6. Passive CS address … 7. Passive CS domain" (p147)；
    "tar cf pcs.tar pcs.p7b" (p150)；"(1)csa> pcscopy … PCS Database Update => End OK" (p152)；
    "PCS state:ACTIVE … 2 IP users are rescued (IP DSP 31002 & 31003)" (p155)
  steps: |
    1. 前置：启动 PCS VM；OMS VM 控制台/SSH 登录 admin（口令 Superuser2580*，实验口径）→ sudo
       omsconfig → 2 View/Modify IP Addresses → 6 Passive CS address=192.168.2.5、7 Passive CS domain=
       pcs.company.com（p147）；WBM 核对 PCS FQDN 已配置（PCS 证书用 FQDN 而非 IP 入 SAN）（p148）。
    2. 生成 PCS CSR：OXE CS 终端 mtcl → su root → netadmin -m → 11.9.2.2 Generate CSR（通配符 y、
       IP SAN=n、4096 位）→ 产出 tar：/tmpd/csa_pcs_csr.tar → 经 Filezilla 传共享盘 PODx → 解 tar 取
       192.168.2.5_pcs.csr 交 CA 签发（p149-150）。
    3. 导入 PCS 证书：签发后的 pcs.p7b 先打包——OXE 上 cd /tmpd && tar cf pcs.tar pcs.p7b（多 PCS:
       tar cf pcs.tar pcs1.p7b pcs2.p7b…）→ netadmin -m → 11.9.2.3 Import PCS certificates → 输入
       /tmpd/pcs.tar → "Certificate of PCS 192.168.2.5 is imported successfully" → copy to twin（p150-151）。
    4. 核验：netadmin -m → 11.9.2.5 View（PCS 证书 CN=pcs.company.com）（p151-152）。
    5. lanpbx.cfg：PCS 节点用与主 CS 相同的 lanpbx.cfg（端点不会向 PCS 请求 lanpbx）——NOTHING TO DO
       （p152 Warning）。
    6. 拷贝到 PCS：OXE mtcl → pcscopy → 1 PCS update → 输 PCS IP 192.168.2.5 → PCS Database Update =>
       End OK（PCS 随之重启）；在 PCS 上 netadmin -m 11.9.1.8 View 确认证书在位（p152-153）。
    7. 备份：netadmin -m → 11.9.2.4 Export PCS certificates → 路径+口令 → /tmpd/csa_pcs_pfx.tar（p153）。
    8. 断网演练：Rlab 门户 → 本 POD → Routers → 选 192.168.1.254 → Disconnect（VLAN1 断开；此后主
       站点 VM 不可达，测试须用 VLAN2 的 PC VM）；PCS 上 mtcl → pcsview → PCS state:ACTIVE、Domain 2
       secured、IPDSP 31002/31003 rescued、OMS(Rack 6) secured in service；互打 31002↔31003 加密正常
       （p154-155）。
    9. 恢复：Routers → Connect 重连 VLAN1 → 重启 PCS → pcsview 显示 INACTIVE、无救援用户/域（实验
       结束后可关停 PCS VM）（p156）。
  verification: |
    断网后 pcsview：PCS state:ACTIVE、GD4 cr6/OXE MS IN SERVICE、2 IP users rescued（p155）；恢复后
    PCS state:INACTIVE、Nb IP-phones connected 0（p156）。
  conditions: PCS 证书必须先打 tar 再导入；NE 配置只在主节点做（p148 Notes）。
  tags: [lab, pcs, rescue, pcscopy, failover]

- id: c06
  title: OTSBC 侧 SIP TLS 与 SRTP 配置（TLS context、证书、Proxy Set、Media Security）
  type: lab
  source_pages: p173-184
  source_chapter: SIP TLS configuration in OTSBC for SIP Trunk
  source_quote: |
    "SETUP / IP NETWORK / SECURITY / TLS contexts … Name OXE TLS, TLS Version TLSv1.2 … DH key Size
    2048" (p175)；"Offered SRTP Cipher Suites AES-CM-128-HMAC-SHA1-80 ( compatible with the OXE)"
    (p184)
  steps: |
    1. 建 TLS context：WebAdmin https://192.168.1.105 → SETUP/IP NETWORK/SECURITY/TLS contexts →
       New → Index 1、Name=OXE TLS、TLS Version=TLSv1.2、DTLS Version=DTLSv1.2、Cipher server=
       AES256:AES128、DH key Size=2048 → Apply → Save（p175）。
    2. 导入 RootCA：选 OXE TLS → Trusted Root Certificates → Import → 选共享盘 ca-certgen.cer →
       Open → Close → Save（p176）。
    3. 生成私钥：OXE TLS → Change certificates → GENERATE NEW PRIVATE KEY → Private key size=4096 →
       Generate Private Key → OK → Save（p177）。
    4. 生成 CSR：Change certificates → 填 Common name=SBC 的 IP、Organization unit/Company/Locality/
       State/Country、Signature algorithm=SHA-256 → Create CSR → 复制 CSR 文本到记事本 → 存为 .csr 于
       共享盘 PODx → 等 CA 签发（p178-179）。
    5. 导入证书：Change certificates → UPLOAD CERTIFICATE FILES → Load Device Certificate File → 选
       sbc.cer（PEM/Base-64 X.509）→ Open → 保存（p180-181）。
    6. SIP 接口：SETUP/SIGNALING&MEDIA/CORE ENTITIES/SIP Interfaces → 选 SIP interface 1（OXE 侧）→
       Edit → TLS context Name=OXE TLS、UDP Port=不使用、TLS port=5061 → Save（p181-182）。
    7. Proxy Set：SETUP/SIGNALING&MEDIA/CORE ENTITIES/Proxy Sets → 选 index 1（OXE）→ Proxy Address 1
       items → Edit → Sip port=5061、Transport type=TLS → Save（p182-183）。
    8. 媒体安全：SETUP/SIGNALING&MEDIA/MEDIA/Media Security → Enable + Offered SRTP Cipher Suites=
       AES-CM-128-HMAC-SHA1-80 → Apply → Save（p184）。
    9. 兼容未加密用户：SETUP/SIGNALING&MEDIA/CODERS&PROFILES/IP Profiles → 选 OXE profile → Edit →
       SBC Media Security=Offer Both–Answer Prefered Secure（SRTP 与 RTP）→ Apply → Save（p184）。
  verification: |
    本章无独立呼叫测试；与 c07（OXE 侧）联合后按 p192 测试（IPDSP ↔ 公网 MicroSIP 互打、看挂锁图标
    或 Wireshark）。
  conditions: 前提 c01（SBC 可达）；证书由 trainer/CA 签发。
  tags: [lab, otsbc, tls-context, srtp, sip-trunk]

- id: c07
  title: OXE 侧 Native SIP TLS + SRTP for SIP trunk（外部网关/本地网关端口/CTL/维护）
  type: lab
  source_pages: p185-193
  source_chapter: Native SIP TLS and SRTP for SIP Trunk
  source_quote: |
    "SIP / SIP Ext. Gateway … Transport type TLS Client" (p188)；
    "Authentication for SRTP 'Authenticated' … Warning RESTART THE SIPMOTOR PROCESS AFTER THE
    CONFIGURATION." (p190)；"Secured SIP gateway(s): - 3 (ITSP_GW): TLS client, RTP or SRTP." (p193)
  steps: |
    1. 前提：NE 已启用（承接 c02）；OTSBC 侧已完成（c06）（p187）。
    2. 开 TLS 信令：System/Other System param/SIP parameters → TLS signaling possible=Yes → 重启 OXE
       （p188）。
    3. 外部网关：SIP/SIP Ext. Gateway → 选网关（实验 ITSP_GW，ID 3）→ Edit → SIP remote domain=
       192.168.1.105（SBC IP）、SIP Port Number=5061、Transport type=TLS Client（p188）。
    4. 本地网关端口：SIP/SIP Gateway → Edit → SIP TLS (Server Auth.) Port Number=5061（默认，按需改）
       （p189）。
    5. SRTP：SIP/SIP Ext. Gateway → SRTP=RTP or SRTP；System SIP parameters → SRTP offer answer
       mode=True；Native Encryption Parameters → Authentication for SRTP=Authenticated（仅对端也为
       Authenticated 时才改）→ 警告：重启 sipmotor——mtcl 执行 dhs3_init -R SIPMOTOR（p189-190）。
    6. OXE 信任库：同 CA 时 NOTHING TO DO；不同 CA 且（OXE 为 TLS client）或（TLS server+mTLS）时：
       证书拷到 /tmpd → root → netadmin -m → 11.9.3.1 Import Endpoint CTL → 输 /tmpd/RootCA.crt →
       自动同步 twin；11.9.3.2 View 核对；openssl crl2pkcs7 -nocrl -certfile /etc/pki/oxe/truststore/
       trustchain.pem | openssl pkcs7 -print_certs -text -noout 查看全部（p191）。
    7. 测试与维护：IPDSP ↔ 公网 MicroSIP 互打，看挂锁图标或 Wireshark；sipextgw -g 3（State IN
       SERVICE、Transport TLS Client、SRTP RTP or SRTP）；cryptview（Secured SIP gateway(s): 3
       (ITSP_GW): TLS client, RTP or SRTP；Secured SIP Extensions: 2）（p192-193）。
  verification: |
    外呼加密成功（挂锁图标/抓包）；cryptview 列出受保护 SIP 网关与扩展计数（p192-193）。
  conditions: trunk 组类型 "ISDN all countries"；仅当对端同为 Authenticated 才改 SRTP 认证值（p190 Notes）。
  tags: [lab, sip-trunk, srtp, sipmotor, ctl]

- id: c08
  title: 原生加密安全停用（参数→用户→lanpbx→重启→验证明文）
  type: lab
  source_pages: p194-198
  source_chapter: Native Encryption deactivation
  source_quote: |
    "Enable Native Encryption Unchecked; to disable native encryption" (p195)；
    "Enter DTLS 1 IP address …: 0.0.0.0 … Enter DTLS 2 IP address …: 0.0.0.0" (p197)；
    "Reboot the OXE Call Servers (double 'bascul' in case of duplication!)" (p198)
  steps: |
    1. 系统参数：System/Others system parameters/Native Encryption Parameters → Enable Native
       Encryption 取消勾选（p195）。
    2. 用户参数：Users → DTLS 用户（8&9 Series Parameters）Native Encryption=Disable；SIP TLS 用户
       （SIP Extension Parameters）Native Encryption=Disable 且 SRTP working mode=None（p196）。
    3. lanpbx.cfg：mtcl → lanpbxbuild → 4 Modify → 选行 1 → j 填 0.0.0.0、k 填 0.0.0.0、n（FQDN）
       直接回车清空 → 0 返回 → 6 Apply changes（DTLS=DISABLED 自动写入并重签）（p197-198）。
    4. 重启：mtcl → shutdown -r now（duplication 双 bascul）（p198）。
    5. 测试：两用户互打，确认通话为 CLEAR 模式（p198）。
  verification: |
    通话以明文建立（p198 "check that this communication is established in CLEAR mode"）。
  conditions: 停用顺序：先参数后用户再 lanpbx，最后重启。
  tags: [lab, deactivation, rollback]

- id: c09
  title: EEGW 部署实验（声明、内部防火墙、PEM 证书、lanpbx 指向 EEGW、VM 配置与证书下载）
  type: lab
  source_pages: p217-243
  source_chapter: Native encryption with External Encryption Gateway, for DTLS compatible equipment's
  source_quote: |
    "netadmin -m … Option 20.2 … External EGW IP for Main CPU ? 192.168.1.7 … twin CPU ? 192.168.1.8"
    (p219)；"11.1.3.Restricted access … 2. 'Add a trusted host'" (p220)；
    "ostconfig … 11. Download Certificates" (p235-237)；"config ost … IN SERVICE" (p242)
  steps: |
    1. 声明 EEGW：OXE 终端 mtcl → netadmin -m → 20.Encryption GW Management → 2 Create/Update →
       Main=192.168.1.7、twin=192.168.1.8 → 警告确认 y（重生成 CS 证书+重启）→ a Apply → copy to
       twin（p219）。
    2. 内部防火墙：root → netadmin -m → 11.1.3 Restricted access → 2 Add a trusted host → eegwcpua/
       192.168.1.7、eegwcpub/192.168.1.8 → a Apply → copy to twin；11.1.3.1 View 核对（或 more
       /etc/hosts）（p220-221）。
    3. PEM 证书闭环：netadmin 11.9.1.2 生成 CSR（本口径 SAN 保留 IP，输出含 EEGW 的 IP/DNS SAN）→
       共享盘交 CA → 取回 cs.cer + ca.p7 → 11.9.1.4 导入（已有时选 replace，all-in-one=n）→ 11.9.1.8
       View 核对 SAN → copy to twin → dhs3_init -R NGINX（p222-227）。
    4. 参数与 lanpbx：照 c02 步骤 6-7 配参数；lanpbxbuild → j=192.168.1.7、k=192.168.1.8（DTLS 服务
       器=EEGW）→ Apply → 重启 CS；more /usr3/mao/lanpbx.cfg 核对 DTLS_SRV=192.168.1.7/
       DTLS_SRV_RD=192.168.1.8（p228-233）。
    5. EGW 核查：IP/Encryption GW：EGW IP ≠ CS IP → EXTERNAL（p234）。
    6. EEGW VM 配置：root/口令（实验口径 Superuser2580*）登录 EEGWCPUA → ostconfig → 1 IP=192.168.1.7、
       2 Netmask、3 Gateway=192.168.1.254、7 CS physical=192.168.1.1、8 CS role=192.168.1.3 → 0 保存
       重启；EEGWCPUB 同法（IP .8、CS physical .2）（p235-236）。
    7. 证书下载：EEGW 上 root → ostconfig → 11 Download Certificates → y（已有 SSH key 答 n）→ 输
       swinst 口令（ssh-copy-id）→ 等下载完成 → 2 回主菜单 → 12 Certificate check → "Certificates in
       OXE & OST are SAME" → 0 退出保存重启；警告：关联 CS 一并重启（p237-241）。
    8. 测试与维护：IP NOE 软话机/话机互打验证加密；cryptview（DTLS server address: 192.168.1.7
       (External EGW)）；config ost（csa/csb ↔ EEGW IN SERVICE）；ost_importlog 拉 EEGW 日志到 OXE
       /tmp（输 EEGW root 口令）（p241-243）。
  verification: |
    cryptview: "DTLS server address: 192.168.1.7 (External EGW)"（p242）；config ost 两行 IN SERVICE
    （p242）；端点加密通话正常（p241）。
  conditions: 改 EEGW 声明即触发证书重生成+重启；下载证书会让关联 CS 重启（变更窗口按 CS 重启规划）。
  tags: [lab, eegw, ostconfig, firewall, certificate]

- id: c10
  title: NSP/SIP Translator 实验（DER 证书、Translator 声明、nsp 服务、SIP 扩展经 NSP 加密）
  type: lab
  source_pages: p244-263
  source_chapter: Native Encryption with SIP translator, for TLS compatible SIP extensions
  source_quote: |
    "netadmin -m … 19.2.2 'Create/update' … Enter the Translator Name ? nsp" (p247)；
    "[root@eegwcpua ~]# nsp restart … nsp status RUNNING" (p260)；
    "INVITE sip:31031@nsp.oxe.company.com:5061" (p262)
  steps: |
    1. 核查 EGW：netadmin -m → 20.1 View（local CPU↔192.168.1.7、twin↔192.168.1.8）（p246）。
    2. 域名：netadmin -m → 19.1.1 View（OXE DOMAIN=company.com、OXE FQDN=oxe.company.com）（p246）。
    3. 声明 Translator：netadmin -m → 19.2.2 Create/Update → 警告确认（CS 证书重生成+重启）→ 名字
       nsp → a Apply → copy to twin → 19.2.1 View 显示 Translator FQDN=nsp.oxe.company.com（p247）。
    4. DER 证书闭环：11.9.1.2 生成 CSR（SAN 含 IP；本次输出还含 DNS:nsp.oxe.company.com）→ 交 CA →
       取回 CA_DER.cer + cs.cer → 11.9.1.4 导入（replace=y）→ 11.9.1.8 View → copy to twin →
       dhs3_init -R NGINX（p248-252）。
    5. 参数：SIP Parameters（TLS signaling=True、SRTP offer answer=True、Loose Route=False）→ 重启
       CS；Native Encryption 参数照配（cipher suite TLS_ECDHE_RSA_AES128_GCM_SHA256 默认 True，两条
       可同开）；SIP 用户 31030/31031 开 Native encryption + SRTP Best Effort（p253-255）。
    6. CTL 更新：lanpbxbuild → 1 View 核对 EEGW 为 DTLS 服务器 → 6 Apply changes（重签 CTL）→ 重启
       CS（p256-257）。
    7. Translator 核查：IP/Encryption GW 显示 SIP translator FQDN（重启后）（p257）。
    8. EEGW 侧：ostconfig → 11 Download Certificates（两台 EEGW 各自向关联 CS 拉取，密码 swinst）→
       12 Certificate check → SAME → 退出保存重启（CS 连带重启）；root 执行 nsp restart → nsp status
       RUNNING → netstat -an | grep 5061 验证监听（p258-260）。
    9. 验证：ALES 互打看盾牌；sipregister（TLS）；csipsets（TLS/SRTP YES）；motortrace 3 抓 trace：
       INVITE 发往 nsp.oxe.company.com:5061、Via SIP/2.0/TLS 192.168.1.7（EEGW）、
       X-ALE-CALL-ENCRYPTED: YES（p261-263）。
  verification: |
    SIP trace 显示信令经 nsp.oxe.company.com:5061（EEGW IP 192.168.1.7）的 TLS 承载且通话加密
    （p262-263）。
  conditions: 承接 c09（EEGW 已部署）；Translator 声明仅外部 EGW 场景强制。
  tags: [lab, nsp, translator, der, sip-tls]

- id: c11
  title: NSP 场景公网 SIP TLS trunk 切换（SBC 指向 NSP FQDN + 内部 DNS 解析）
  type: lab
  source_pages: p264-271
  source_chapter: Native encryption with SIP translator, for public SIP TLS Trunk
  source_quote: |
    "Proxy Address Enter: nsp.oxe.company.com:5061" (p266)；
    "Do you want to activate internal name resolver (y/n default is 'n') ? y" (p267)；
    "Mediant SW> ping nsp.oxe.company.com … PING 192.168.1.7" (p269)
  steps: |
    1. 前提：EEGW+NSP 已配（c09/c10）、证书与 OTSBC/OXE TLS 配置已就绪（c06/c07）（p265）。
    2. SBC 改指向：OTSBC WebAdmin → SETUP/SIGNALING&MEDIA/CORE ENTITIES/Proxy Sets → Proxy Set 1（OXE）
       → Proxy Address 1 items → Edit → Proxy Address=nsp.oxe.company.com:5061（SIP translator FQDN:
       端口）、Transport type=TLS → Save（冗余场景必须 FQDN；单机可用 EEGW IP）（p266）。
    3. 外部 DNS：委托域 oxe.company.com 转发给 OXE（RLAB 已配好， Nothing to do）（p267）。
    4. OXE 内部 DNS：OXE 终端 mtcl → netadmin -m → 17.2 Node setup → Update → 节点名默认回车 →
       "activate internal name resolver?" y → a Apply → copy to twin（两台 CS 都开）（p267-268）。
    5. 外部 DNS 记录：DNS 服务器（如 pfSense）配 oxe.company.com → 192.168.1.3（主 CS main IP；空间
       冗余再加第二 CS）（p267）。
    6. 核对：netadmin -m → 2 Show current configuration → "internal name resolver activated: yes"
       （p268）。
    7. 测试：SBC console（Admin）→ ping nsp.oxe.company.com → 解析到 192.168.1.7（主 CS 的 EEGW）；
       发起公网外呼 → 话机显示 Encryption 图标 → motortrace 3 抓包确认 INVITE@nsp FQDN:5061、
       X-ALE-CALL-ENCRYPTED: YES（p269-271）。
  verification: |
    SBC ping NSP FQDN 解析到主 CS 的 EEGW IP（p269）；外呼 trace 显示经 NSP 的 TLS 信令与加密媒体
    （p270-271）。
  conditions: 委托域解析的主备行为：主备内部 DNS 都被询问、仅主 CS 应答（p267）。
  tags: [lab, nsp, dns, otsbc, sip-trunk]

- id: c12
  title: S.O.T. 生成并加载 EEGW 虚拟机（Greenfield 工程 → OVA → ESXi → 首次配置）
  type: lab
  source_pages: p272-282
  source_chapter: OST/EGW generation & loading with S.O.T. deployment tool
  source_quote: |
    "Select 'Greenfield' project … Product Selection … OST" (p274)；"Machine type EEGW" (p276)；
    "Log on EEGW VM (default login/password: root/letacla1). Change the password" (p279)
  steps: |
    1. 备源：BootDVD .iso 与 OST 软件 .iso（实验取自 NAS N:Softs；可先拷到本地 PC 提速上传）（p273）。
    2. 登 S.O.T.：浏览器（仅 Chrome/Firefox）开 https://192.168.1.194 → admin / 自定义口令（应为
       Superuser2580*，实验口径）（p273）。
    3. 建工程：Greenfield → NEXT → Product=OST → NEXT；媒体缺失（"BootDVD media is missing"）时经
       FTP（upload/sot）用 Filezilla 传两个 iso → Refresh medias list → 选中 → Declare medias → NEXT
       （p274-275）。
    4. 工程设置：选 BootDVD 与 OST 版本 → Project name/描述 → OVF Generation 勾选（S.O.T. 生成 ovf）
       → Country=France、Timezone=Europe/Paris（实验口径）→ NEXT（p275）。
    5. 机器参数：Machine type=EEGW、Keyboard、Hostname=eegwcpua、EEGW Sizing（最大用户数）、IP=
       192.168.1.7 → 项目摘要 → Deploy → .ovf 生成 → Download 保存 .ova → Projects listing 状态
       "OVA generated"（p276）。
    6. 部署：ESXi 管理界面部署 .ova → 启动 VM → 控制台观察自动加载 → Projects listing 状态
       "COMPLETED"→ 出现 eegwcpua login（Rocky Linux 9.7）（p277-278）。
    7. 首次配置：root/letacla1 登录 → 按 Rocky 规则改 root 与 admin 口令（如 Superuser2580*）→
       ostconfig → 配 IP 192.168.1.7/掩码/网关 192.168.1.254（CS physical/role 此时 0.0.0.0 待后续
       步骤填）→ 0 保存重启（p279-280）。
    8. 收尾：OXE 内部防火墙加 eegwcpua/eegwcpub 信任主机（netadmin 11.1.3，同 c09 步骤 2）→ View
       核对（p281-282）。
  verification: |
    Projects listing 显示 COMPLETED、VM 出现登录提示（p278）；ostconfig 菜单显示 Board role EGW 与
    配置项（p280）。
  conditions: S.O.T. 仅支持 Chrome/Firefox；默认口令 letacla1 必须首登即改。
  tags: [lab, sot, eegw, ova, esxi]

- id: c13
  title: 网络实验室改造（Node1 接口切换、OMS 旧证书清除、直连链路验证）
  type: lab
  source_pages: p283-290
  source_chapter: Pod Configuration: Network labs
  source_quote: |
    "Remove the network interface of 'ENTP_OXE_FSNE_CSA' VM … Select the port '192.168.1.1'" (p285)；
    "omsconfig … Choose option 4: Erase saved certificates" (p288-289)；
    "hybvisu -f all … Direct IP link 2002 to node 2 : UP (Enabled/DATA_TRANSFER)" (p290)
  steps: |
    1. 接口切换：Rlab 门户 → 本 POD → Instances → ENTP_OXE_FSNE_CSA → Show → Remove Interface →
       选 192.168.1.1 → Send；ENTP_OXE_FSNE_NODE1 → Show → Remove Interface（192.168.1.201）→ 再次
       Show → Create Interface → Subnet1 → IP=192.168.1.1 → Send → 硬重启该 VM（p285-287）。
    2. 连通性：从 NODE2（cs2）ping 192.168.1.1 通（p287）。
    3. 预配置核对：许可/防火墙/NTP/FlexLM 已配；DHCP 关闭；直连链路已通；默认号 Network=0（Node1/
       Node2）；SSH 密钥已发（p288）。
    4. 板卡核对：NODE1 OMS Rack 4（192.168.1.13，MAC 00:50:56:01:01:13）；NODE2 OMS Rack 3
       （192.168.1.113，MAC 00:50:56:01:02:13）；警告：ENTP_OMS_CSA_CSB_NODE1 VM 此前服务过 CSA/CSB
       → omsconfig → 8 Certificate management → 4 Erase saved certificates → 保存重启 OMS（p288-289）。
    5. 用户：IPDSP 31000（Node1，PC10，TFTP=192.168.1.3）与 31500（Node2，PC20，TFTP=192.168.1.103）
       （p289）。
    6. 链路验证：mtcl → hybvisu -f all → System Option Direct IP link: ENABLED；Direct IP link 2002
       to node 2: UP (Enabled/DATA_TRANSFER) High Bandwidth；Encryption: NO（初始明文）→ 建一个网络
       呼叫（p290）。
  verification: |
    ping 通 + hybvisu 显示 Direct IP link 2002 UP（p287/p290）。
  conditions: RLAB 约束：两 VM 不能同 IP，切换必须先删后建并硬重启。
  tags: [lab, abc-f, pod, oms, hybvisu]

- id: c14
  title: ABC-F 网络内部 PKI——Node 1 作 CA（自签根 CA + 自动生成 CS 证书）
  type: lab
  source_pages: p309-318
  source_chapter: Native Encryption for ABC-F network with internal PKI (Node 1)
  source_quote: |
    "netadmin -m … 11.9.1 … Then press 1 … CC-suite-ID []:11111-11111-11111-11111" (p310)；
    "Generating Root CA... Generating private key for Call Server... Signing Call Server CSR..." (p311)；
    "The validity period of all entries … is 7300 days." (p312)
  steps: |
    1. 生成自签证书：Node1 终端 mtcl → su root → netadmin -m → 11.9.1 → 1 'Create/Update CS
       certificates (Auto generated)' → 输 CC-suite-ID（11111-11111-11111-11111，实验口径，来自许可
       文件）→ 通配符 SAN=y、IP SAN=y、附加 SAN=n、4096 位 → 填 FR/BZH/BREST/ALE/EDUC → 确认 → 系统
       生成 Root CA + CS 私钥 + CSR + 签名（p310-311）。
    2. 应用：mtcl 执行 dhs3_init -R NGINX（p311）。
    3. 核验：netadmin -m → 11.9.1.8 View → CA 与 CS/Network 证书（CN：CA=CC-suite-ID、CS=oxe.company.com；
       有效期 7300 天）（p312）。
    4. 参数：Native Encryption=True、自动 CTL=True、SRTP Authenticated（p313）；用户 31000 开
       Native encryption、Phone COS 开加密图标（p314）。
    5. lanpbx：cs1 上 lanpbxbuild -auto → lanpbxbuild → j=192.168.1.1（k 本实验不填）→ Apply →
       重启；IP/Encryption GW 核查=内部 EGW（p315-317）。
    6. 端点验证：启动 IPDSP 31000 → 证书弹窗 Accept permanently（内嵌 CA 自签，PC 不认识）→ DTLS
       加密图标出现（p318）。
  verification: |
    netadmin View 显示 CA（CN=CC-suite-ID）与 CS 证书就位、7300 天（p312）；IPDSP 出现 DTLS 加密图标
    （p318）。
  conditions: 内部 PKI 场景 SAN 走 IP（本实验口径）；Node1 即"签发节点/CA 服务器"。
  tags: [lab, internal-pki, abc-f, node1]

- id: c15
  title: ABC-F 网络内部 PKI——Node 2 CSR 网络签发（一步式签名+导入）
  type: lab
  source_pages: p319-328
  source_chapter: Native Encryption for ABC-F network with internal PKI (Node 2)
  source_quote: |
    "netadmin -m … Option 11.9.1.3 'Generate CSR, sign and import in OXE network'" (p320)；
    "Enter the Network Call Server signing IP : 192.168.1.1" (p321)；
    "Do you want to import the certificates (y/n)? y … Certificates are imported successfully." (p322)
  steps: |
    1. 一键签发导入：Node2 终端 mtcl → su root → netadmin -m → 11.9.1.3 'Generate CSR, sign and
       import in OXE network' → 输签发 CS 的 IP=192.168.1.1（Node1）→ 通配符 y、IP SAN=y、附加 n、
       4096 → 填 Node2 的 DN（实验口径 FR/IDF/COL/ALE/DIR）→ 确认 → 系统生成 CSR→送 Node1 签名→
       自动回传并导入（CA 证书 + Node2 CS 证书）→ "Certificates are imported successfully"（p320-322）。
    2. 核验：netadmin -m → 11.9.1.8 View → CA 同 Node1 的 CA、CS 证书 CN=oxe2.company.com（节点 FQDN）、
       SAN 含 192.168.1.103/.101，7300 天（p323）；mtcl 执行 dhs3_init -R NGINX（p324）。
    3. 参数与用户：NE 参数三件套（p324）；用户 31500 开 Native encryption + 加密图标（p325）。
    4. lanpbx：cs2 上 lanpbxbuild -auto → lanpbxbuild → j=192.168.1.101 → Apply → 重启（p326-328）。
    5. 端点验证：启动 IPDSP 31500 → 接受证书 → DTLS 图标（p328）。
  verification: |
    Node2 View 显示 CN=oxe2.company.com 的节点证书（SAN IP .103/.101）（p323）；IPDSP 31500 DTLS
    图标（p328）。
  conditions: CN 恒为节点 FQDN；duplication 场景所有条目须用 netadmin/swinst 的 CLONING 选项送 standby
  （p323 Warning）。
  tags: [lab, internal-pki, abc-f, node2, csr]

- id: c16
  title: ABC-F 直连链路加密（链路 Encryption 参数、SRTP 一致性、系统参数、网络通话验证）
  type: lab
  source_pages: p329-332
  source_chapter: Native Encryption for ABC-F network
  source_quote: |
    "Inter-Nodes links / Logical links (ABC-F) / Hybrid or Direct Link Access … To activate
    encryption for the link, this last one must not be up." (p330)；
    "Authentication for SRTP 'Authenticated': SRTP authentication is mandatory to permit the voice
    flow establishment" (p331)；
    "Set up an ABC-F network call between user 31000 … and user 31500 … check that the communication
    is encrypted" (p332)
  steps: |
    1. 链路加密（Node1 与 Node2 两侧同样操作）：WBM → Inter-Nodes links/Logical links (ABC-F)/Hybrid
       or Direct Link Access → 先禁用该接入（信令下链）→ 在该接入的 "other" 页签激活 Encryption →
       重新启用接入；参数两端必须同值（p330）。
    2. SRTP 认证：System/Other System Param./Native encryption parameters → Authentication for SRTP=
       Authenticated（NE 场景必开；可选项 Authenticated tag emis. w/o ctrl）（p331）。
    3. 系统参数：System SIP parameters → Enhanced codec negotiation=Network Type（所有节点）；
       SRTP offer answer mode=True（p332）。
    4. 测试：31000（Node1）↔ 31500（Node2）网络呼叫 → 确认加密（p332）。
  verification: |
    跨节点网络呼叫加密（p332）；hybvisu 的链路 Encryption 状态翻转（p290 对照）。
  conditions: 链路必须 DOWN 才能改参数；与 IP Premium Security 不互通；transit 仅 hybrid 网络。
  tags: [lab, abc-f, link-encryption, direct-ip-link]

- id: c17
  title: XCA 端点证书工厂（OMS/IPDSP 的密钥、证书、导出与命名约定）
  type: lab
  source_pages: p333-353
  source_chapter: External Certification Authority - Endpoints
  source_quote: |
    "'Common Name' for 'OMS' end entity must match it's MAC address" (p344)；
    "It must be named 'GW.pfx'" (p346)；"Rename the certificate file as: 'softphone_cert.pem'" (p351)；
    "Rename the key file as: 'softphone_pkey.pem'" (p352)
  steps: |
    1. 装 XCA：hohnstaedt.de/xca 下载 setup.exe → 安装（Typical）→ File/New DataBase → Cert_DB +
       库口令（实验口径 Alcatel）（p335-337）。
    2. 根 CA：Private Keys 页 New key（4096 位，Remember as default）→ Certificates 页 New
       certificate → Source：自签 + SHA 256 → Subject：DN + 选私钥 → Extensions：Type=Certification
       Authority、Subject Key Identifier、有效期 → OK → 导出 PEM（*.crt）（p338-341）。
    3. OMS 实体：New key → New certificate → Source：签名证书选根 CA + SHA 256 → Subject：CN=OMS 的
       MAC（005056010113，实验口径）→ Extensions：Type=End Entity、Subject/Authority Key Identifier、
       有效期 → OK → 导出 PKCS12（*.pfx）且必须命名 GW.pfx、设导出口令（p342-346）。
    4. IPDSP 实体：New key → New certificate → 同上，CN=IPDSP MAC（在 IPDSP 设置 Network 页 phone
       identifier 查看）→ Type=End Entity → 导出证书为 .pem 并命名 softphone_cert.pem；Private Keys
       页导出私钥为 .pem encrypted 并命名 softphone_pkey.pem（设口令）（p347-352）。
    5. 用法提示：XCA 用法看 Help/Content（F1）或问 trainer（p353）。
  verification: |
    证书生成并按命名约定导出：GW.pfx（OMS）、softphone_cert.pem/softphone_pkey.pem（IPDSP）（p346/p351/p352）；
    后续在 c18 中部署验证。
  conditions: 命名严格匹配（部署端按文件名读取）；CN=MAC 是 mTLS 身份比对基础。
  tags: [lab, xca, endpoint-certificate, oms, ipdsp]

- id: c18
  title: mTLS 双向认证启用（OMS/IPDSP 证书部署、Endpoint CTL 导入、mTLS 参数、验证与版本限制）
  type: lab
  source_pages: p354-379
  source_chapter: Native Encryption & mTLS
  source_quote: |
    "omsconfig … 3: import gateway certificate … 2: Transfer via sftp and extract client certificate"
    (p357-358)；"DTLSPkeyPassphrase.exe /set <passphrase>" (p360)；
    "netadmin -m … 11.9.3.1 'Import Endpoint CTL'" (p363)；"Enable Mutual TLS Authentication True"
    (p364)
  steps: |
    1. 前提：服务器认证已配（NE 参数、CA/CS 证书、端点 CTL 已随 lanpbx.cfg 或 sipconfig 下发）（p356）。
    2. OMS 部署：XCA 签 GW.pfx（CN=OMS MAC 005056010113，End Entity）→ OMS VM 控制台 root →
       omsconfig → 6 ssh server open + 9 Enable/Disable SSH（1-Enable，输入转移用 PC IP 如
       192.168.1.10；完成后撤销该 IP）→ 8 Certificate management → 3 Import gateway certificate →
       2 Transfer via sftp → Filezilla 把 GW.pfx 传 OMS /tmp → 回车 → 输导入口令 → 1 Print
       certificates 核验 → 退出保存重启 OMS（p356-359）。
    3. IPDSP 部署（文件法）：softphone_cert.pem 与 softphone_pkey.pem 放 IPDSP 安装目录（Program
       Files\Alcatel-Lucent Enterprise\IpDesktopSoftPhone）；私钥口令绑定：装机参数 DTLS_PKEY_PASSWORD
       （批量）或管理员 cmd 执行 serviceability\DTLSPkeyPassphrase.exe /set Alcatel（p360-361）。
       （证书库法：.pfx 装入 Windows 本机个人库 + 装机参数 DTLS_CERT_NAME，本书仅演示未测试。）（p362）
    4. 端点 CTL 导入：XCA 根 CA 证书（.pem/.crt）拷到 OXE /tmpd → root → netadmin -m → 11.9.3.1
       Import Endpoint CTL → /tmpd/XCA.crt → 11.9.3.2 View 确认新条目（p363）。
    5. 启用 mTLS：System/Other System Param./Native Encryption parameters → Enable Mutual TLS
       Authentication=True → lanpbxbuild 6 Apply changes 重签 → 重启 OXE（p364-365）。
    6. 验证：重启 IPDSP；Node1 上 OMS（Rack 4）in service（config 4）；31000 secured；31000↔31500
       直连链路加密通话；cryptview 显示 mTLS authentication enabled（DTLS）（p365）。
    7. 版本限制处置（如遇 1024 位出厂设备）：方案 1=外部 PKI 签 ≥2048 位证书并部署（板卡 V24 串口+
       mgconfig 12 Certificate management 导入，话机 SCEP/证书服务器/手工 Get Certificate）；方案 2=
       R101.1(N4) 起 netadmin 11.6.3 SSL Security level 降级（2→1 或 0）+重启+copy to twin（p366-375）。
    8. SIP 侧 mTLS（附录）：SIP 扩展系统参数 SIP TLS Mutual Authentication=True（节点重启）；公网
       trunk：本地网关 SIP TLS (Mutual Auth.) 端口（默认 6261，与 OTSBC Proxy Set 对齐 host:6261）+
       外部网关 Transport type/SIP TLS Mutual Authentication=True（sipmotor 重启）（p377-379）。
  verification: |
    cryptview 显示 DTLS Mutual TLS Authentication 启用、OMS/IPDSP 在加密模式在服、跨节点加密通话
    （p365）。
  conditions: mTLS 激活后所有话机/软话机（含明文用户）都必须有证书；SSH 开启须告知客户并事后关闭
  （p357）。
  tags: [lab, mtls, endpoint-certificate, ssl-level]

- id: c19
  title: XCA 外部 CA（CS/PCS 侧）——根 CA、PKCS#7 CSR 签发、PKCS#12 实体证书与格式转换
  type: lab
  source_pages: p380-403
  source_chapter: External Certification Authority
  source_quote: |
    "PKCS7 is the easiest and may be the best way to generate certificate(s) signed by an external
    PKI (CA) because the private key of the entity doesn't move" (p391)；
    "Warning PKCS 12 IS NOT THE EASIEST WAY … PRIVATE KEY IS GENERATED ON THE CA AND MUST BE
    TRANSFERRED … CSR IS DONE MANUALLY ON THE CA" (p397)；
    "openssl crl2pkcs7 -nocrl -certfile RootCA.crt -out ca.p7" (p390)
  steps: |
    1. 安装与库：XCA 下载安装 + 建 Cert_DB（同 c17 步骤 1-2）（p381-385）。
    2. 根 CA：New key → New certificate（自签/SHA256/DN/CA 型/有效期）→ 导出 .p7b → Filezilla 传 OXE
       tmpd → 转格式：.p7b 用 root 跑 /usr/netadm/sh/conv-proper-p7-format.pl（输 入
       /tmpd/RootCA.p7b → 输出 /tmpd/ca.p7）；.crt 用 openssl crl2pkcs7 -nocrl -certfile RootCA.crt
       -out ca.p7（p386-390）。
    3. PKCS#7 路线（推荐）：OXE 上 netadmin 11.9.1.2 生成 CSR（实体私钥不出机）→ XCA 的 Certificate
       signing requests 页 Import CSR → 选文件 → 右键 Sign → Source：签发证书=根 CA、SHA 256 →
       Extensions：End Entity/Key Identifiers/有效期 → OK → Certificates 页核验（subject/SAN 与 CSR
       一致、CN=OXE FQDN）→ 导出 .p7b（p391-396）。
    4. PKCS#12 路线（端点）：New key（CA 侧生成）→ New certificate（签名=根 CA）→ Subject：CN 按规则
       （CS/PCS=OXE FQDN，板卡/话机=MAC）→ Extensions：End Entity → SAN 编辑（Edit X509v3 Subject
       Alternative Name：内嵌 EGW 场景填角色/物理 IP；外部 EGW+NSP 场景再加 EEGW 与 NSP FQDN）→ OK →
       导出 PKCS12（设口令）（p397-402）。
    5. 用法：Help/Content（F1）（p403）。
  verification: |
    签发证书在 XCA Certificates 页可查且 SAN/CN 与 OXE 请求一致（p394-395）；格式转换输出 ca.p7
    （p390）；后续经 netadmin 11.9.1.4 导入 OXE 验证（c02/c09）。
  conditions: 客户已有外部 CA 时优先用客户的（p381 Warning）；PCS 证书同法（CN=pcs.company.com）。
  tags: [lab, xca, pki, pkcs7, pkcs12]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 18 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 密码学与证书基础 | 无实验章（p3-26 概念讲义），概念内容归 framework/principle。 |
| task-02 Pod 环境搭建 | 有 → c01 |
| task-03 SIP 模拟器验证 | 无独立 How-To 章（p42-47 为讲义式说明，操作并入 c01 步骤 11 与 ITSP 文档引用）。 |
| task-04 CSR 签发导入闭环 | 有 → c02（PKCS#7 主线）、c19（XCA CA 侧）、c14/c15（内部 PKI 变体） |
| task-05 系统/用户参数 | 并入 c02 步骤 6-7、c04 步骤 2-3（无独立实验章） |
| task-06 lanpbx.cfg | 并入 c02 步骤 8、c09 步骤 4、c10 步骤 6（无独立实验章） |
| task-07 DTLS 验证与维护 | 有 → c02 步骤 10-11（IPDSP/ippstat/twin/cryptview/事件/备份） |
| task-08 Wireshark | 有 → c03 |
| task-09 SIP TLS 扩展 | 有 → c04、c10（NSP 变体） |
| task-10 PCS 接管 | 有 → c05 |
| task-11 SIP trunk TLS/SRTP | 有 → c06（OTSBC 侧）、c07（OXE 侧）、c11（NSP 切换） |
| task-12 安全停用 | 有 → c08 |
| task-13 EEGW/NSP 部署 | 有 → c09（EEGW 主线）、c10（NSP/DER） |
| task-14 S.O.T. 生成 | 有 → c12 |
| task-15 网络实验室改造 | 有 → c13 |
| task-16 ABC-F 网络加密 | 有 → c14（Node1 CA）、c15（Node2 签发）、c16（链路加密） |
| task-17 XCA 端点证书 | 有 → c17（端点实体）、c19（CS/PCS 实体） |
| task-18 mTLS 启用与限制 | 有 → c18 |

**统计**：19 条（全部 lab 型）；18 项任务中 16 项有案例类条目直接覆盖，task-01 为概念讲义、task-03 并入 c01，task-05/06 以步骤形式分散在 c02/c04/c09/c10 中（书中无独立实验章）。
