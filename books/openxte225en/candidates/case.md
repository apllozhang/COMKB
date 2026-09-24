# 案例/实验/操作序列候选 — OpenTouch Mobility & Remote Worker (OPENXTE225EN R2.6 Issue 10)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号、域名）标注"实验口径"。
> 条目说明: 全书 8 个 How-To 实验章 → 10 条（OTC PC 章按其自身两节拆 2、智能手机章按双模式/单设备场景拆 2），无讲义级补充条目。

```yaml
- id: c01
  title: OpenTouch 服务器侧远程访问设置（RP/OTSBC 申报、DAS 规则、ACS 会议服务与证书重签）
  type: lab
  source_pages: p62-77
  source_chapter: OpenTouch server settings for remote access — "Configure general settings in OpenTouch server for remote access (remote workers)"
  source_quote: |
    "Declare the reverse proxy with the following URL for all services: https://ot-podx.al-mydemo.com,
    https://ot-podx.al-mydemo.com:8016 for EVS (notifications)" (p63)；
    "WARNING THE DECLARATION ORDER IS IMPORTANT. SEVERAL RULES CAN BE APLLIED AT A TIME" (p67)；
    "Launch the rehosting script thanks to the command: 'ot-config.sh --rehost'" (p70)
  steps: |
    1. RP 申报：OmniVista 8770 → "OpenTouch" 配置窗 → SystemServices/System services/Topology/Reverse
       proxy → 选 Reverse proxy：Display name 任意；API public URL = https://ot-podx.al-mydemo.com；EVS
       public URL = 同地址:8016；ACS public URL = https://ot-podx.al-mydemo.com；DMS public URL = https://
       ot-podx.al-mydemo.com（实验口径）。这些 URL 会写入配置文件供 OTC 应用从互联网回连。
    2. OTSBC 申报（OTC 客户端用）：Eco system/IT server → 右键 Create：Name、FQDN = otsbc-podx.al-mydemo.com
       （实验口径）、Network type = WAN、Port = 5261。OTSBC FQDN 会写进客户端配置用于 SIP 注册与呼叫。
    3. OTSBC 申报（WebRTC 用）：同路径 Create：FQDN 同上、Network type WAN、Port 8061。
    4. DAS 规则：会议服务器 Administration Console → Domain → 选 "Default" 域 → 逐条核对 10 条规则（含
       R2.0 起游牧 PC 新增 4 条 s/^\+[National Prefix]/[Trunk seizure Prefix]0/、s/^\+N/N/、s/^\+M/M/、
       s/^\+/000/，必须按序），缺失则补 → Result 确认。规则国家相关（书中为法国口径）。
    5. ACS 会议服务核验：查 /var/data/bics/bics.conf 文件尾部 ACS Service 参数；ping ACS 专用 IP（实验
       口径 151.1.1.55）；或开 OT My Profile 页点证书图标 → Details 页签查 Subject Alternative Name。
    6. （未配置时）rehost：OT 服务器控制台或 SSH 执行 ot-config.sh --rehost → ACS 专页配 Hostname
       （conf-podx）、Domain name（al-mydemo.com，须与 OT 公共域一致）、IP Address（151.1.1.55，实验口径）；
       确认内部 DNS 已有该 FQDN 条目；重启后 ping ACS IP 与 conf-podx.al-mydemo.com 验证。
    7. 证书重签（ACS 名/IP 变更后必做）：WebAdmin System services/Security/Certificate → Generate CSR
       （国家 2 字母/省/市/公司/部门/管理员邮箱，Signature algorithm 选 SHA256）→ CSR 落在浏览器
       Downloads；浏览器开 https://eco.company.com/CertSrv（administrator/superuser，实验口径）→ Request
       a certificate → advanced → base-64 提交 → 模板选 Web Server → 警告点 Yes → Base 64 encoded 下载
       证书链；回到 WebAdmin → Change server certificate → 类型 pkcs#7 → Select certificate file →
       Import（pkcs#12 则需 passphrase）→ Deploy。
  verification: |
    p67 DAS 规则页有 "Result" 结果核对；p70 Tips：rehost+重启后 ping ACS IP（151.1.1.55）与域名
    conf-podx.al-mydemo.com；p77 重签后打开证书 Details 页签核对 SAN 已含会议 FQDN。
  conditions: 需 OmniVista 8770 管理入口与 OT 服务器 WebAdmin；CA 用 Eco-system 自建 Windows CA（实验口径）。
  tags: [lab, ot-server, reverse-proxy-declaration, otsbc-declaration, das, acs, certificates]

- id: c02
  title: OTSBC 部署（OVF 上电、CLI 初始化、许可、证书、向导配置、SIP 接口证书选择）
  type: lab
  source_pages: p89-117
  source_chapter: OTSBC deployment — "Deploy OTSBC"
  source_quote: |
    "Username: Admin … Mediant SW(config-voip)# interface network-if 0 … set ip-address 11.1.1.20 … write …
    reload now" (p91)；
    "Application: Remote Users (IP-PBX with remote Users); Template: Alcatel-Lucent Remote Users" (p102)；
    "FOR IPHONE DEPLOYMENT, ADDITIONNAL MANUAL CONFIGURATION OF SEVERAL OBJECTS IS MANDATORY." (p105)
  steps: |
    1. 准备：从 Business Portal 下载 OVF（配置向导软件同站可得）；核对 NAT：195.128.146.102↔11.1.1.20，
       端口 5261/8061，RTP/SRTP 7000-7499（实验口径）。
    2. VM 部署：ESXi 部署 OTSBC OVF 并开机（通用 OVF 步骤见 c10）。
    3. CLI 初始化网口：登录 Admin/Admin（实验口径）→ enable → configure voip → interface network-if 0 →
       set ip-address 11.1.1.20、set prefix-length 24、set gateway 11.1.1.254（实验口径）→ exit 退出两级 →
       write → reload now。
    4. 许可：webadmin（OTSBC LAN IP，Admin/Admin）→ Setup/Administration/Maintenance → License key 输入
       key；Maintenance Actions → RESET（Save to FLASH=Yes）保存重启。
    5. 证书：SETUP/IP NETWORK/SECURITY/TLS Contexts → Trusted Root Certificates → Import CA 根证书 →
       验证信息；New 建 TLS 上下文（Name 例 OTSBC）→ Change Certificate → 先 Generate Private key →
       填 CSR（Subject Name=otsbc-podx.al-mydemo.com、SAN、OU=Training、Company=ALE、Brest/Brittany/FR、
       SHA-256）→ Create CSR → 复制文本到 eco.company.com/CertSrv（advanced、base-64、Web Server 模板）
       → 下载证书链 → 回 TLS Contexts → Select File → Load File → Save。
    6. 向导配置：webadmin → Configuration Wizard → Update from remote server 更新模板 → General
       （End Customer/Country/Integrator/Installer）→ Topology：Application=Remote Users (IP-PBX with
       remote Users)、Template=Alcatel-Lucent Remote Users、Network Setup 按端口拓扑 → System（Web 界面
       HTTP/HTTPS、CLI Telnet/SSH、时区、NTP）→ IP（Group 1、11.1.1.20、掩码、网关、NAT Public IP、内部
       DNS、OAM=WAN）→ OpenTouch SIP（内部 IP/FQDN、UDP）→ OXE SIP（主 IP/FQDN、UDP）→ SBC SIP：OTCV 勾
       Enable（域=OTSBC 公共 FQDN）、OTCT 勾 Enable（同 OTCV 域）、OTCV Web 勾 Enable（域=OT 内部 FQDN）
       → 核对 → Apply & Reset（或 Save INI File 事后上传）。
    7. SIP 接口证书选择：SETUP/SIGNALING & MEDIA/CORE ENTITIES/SIP Interfaces → 逐个把 TLS Context Name
       改为第 5 步生成的证书上下文（例 OTSBC）。
    8. 手工补配（书内明示两项）：OXE 的 SIP interface 2 补 TCP 5060（向导只配 UDP）；iPhone 场景的其余
       手工对象不在本实验，查 TC2639。
  verification: |
    p106 SIP 接口更新 TLS context 后有 "Result" 截图核对；向导末尾 Apply & Reset 成功即配置落地。全书未
    给 OTSBC 端到端呼叫测试问题（端到端行为验证由后续客户端实验承接）。
  conditions: 实验口径 IP/口令；iPhone 部署须另按 TC2639 手工补配（书外）。
  tags: [lab, otsbc, deployment, ovf, license, certificates, wizard, mediant]

- id: c03
  title: OTSBC 内嵌反向代理部署（许可核验、HTTP proxy 激活、RP 证书、接口与模板文件）
  type: lab
  source_pages: p131-144
  source_chapter: Embedded Reverse Proxy deployment — "Deploy the Reverse Proxy integrated to OTSBC"
  source_quote: |
    "Verify if the license parameter is present. … HTTP Proxy Available" (p133)；
    "HTTP Proxy application Enable; Primary DNS Server IP … 151.1.1.100" (p134)；
    "Subject Name: Public FQDN of OpenTouch (e.g. ot-podx.al-mydemo.com); Subject Alternative Name: Public
    FQDN of conference service (e.g. conf-podx.al-mydemo.com)" (p135-137)
  steps: |
    1. 许可核验：webadmin → SETUP/Administration/License/License Key → 确认 "HTTP Proxy Available"
       （实验环境无许可也可先测，Tips 明示）。
    2. 启用 HTTP proxy：SETUP/IP NETWORK/HTTP PROXY/General Settings → HTTP Proxy application=Enable →
       Primary DNS=151.1.1.100、Secondary=10.20.30.254（实验口径）。
    3. RP 专用证书：SETUP/IP NETWORK/SECURITY/TLS Contexts → New（Name 例 RP-Conf）→ Change Certificate →
       Generate Private key → 填 CSR：Subject Name=OT 公共 FQDN（ot-podx.al-mydemo.com）、1st SAN=会议
       公共 FQDN（conf-podx.al-mydemo.com）、OU/公司/城市/省/国家码、SHA-256 → Create CSR → eco.company.com/
       CertSrv（Web Server 模板、base-64）签发 → 回 TLS Contexts → Select File → Load File → Save。
       （也可复用 OTSBC 证书但必须加 OT+会议公共名为 SAN，实验选择新建。）
    4. RP 专用 IP 接口：SETUP/IP NETWORK/CORE ENTITIES/IP Interfaces → New：Name=RP、Application Type=
       Media+Control、IPv4 Manual、IP=11.1.1.10、prefix 24、网关 11.1.1.254、DNS 151.1.1.100（实验口径）；
       或改 template_interface_ed02.ini（InterfaceTable 行）经 SETUP/ADMINISTRATION/MAINTENANCE/Auxiliary
       Files 上传。
    5. RP 设置：修改 template_rp_ed02.ini（12 处映射）：RP_Inbound_Interface=RP、RP_Outbound_Interface=RP、
       TLSContexts=RP-Conf、ot.public_fqdn=ot-podx.al-mydemo.com、.public_domain=.al-mydemo.com、
       conference_fqdn=conf-podx.al-mydemo.com、conference_name=conf-podx、.conference_domain=
       .al-mydemo.com、ot.private-fqdn=opentouch.company.com、ot.private-name=opentouch、ot.private-ip=
       151.1.1.50、.private-domain=.company.com（实验口径）→ Auxiliary Files 上传 Load File + Save →
       按需重启。
    6. LDAP 认证模板：template_ldap_ed02.ini 仅当 RP 层做外部认证时用，且 LDAP-auth daemon 需专用机器
       ——本实验不实施，需要时查 TC2639。
  verification: |
    p143 接口应用后 "you can see the new interface in the list"；p144 应用后经 SETUP/IP NETWORK/HTTP
    PROXY/HTTP Proxy Servers 查看配置生效。书中未给端到端反代访问测试问题。
  conditions: 内嵌 RP 自 OTSBC 7.2 起可用；客户端侧回连 URL 已在 c01 步骤 1 申报。
  tags: [lab, reverse-proxy, embedded, otsbc, http-proxy, template-files]

- id: c04
  title: OTC PC 配置为 multi-devices 副设备（COS/前缀前提、DM 声明、副设备创建与关联）
  type: lab
  source_pages: p151-156
  source_chapter: OTC PC for remote worker — "Multi-devices: OTC PC as a secondary device"
  source_quote: |
    "Ring all Secondary if Main Out of Service: Yes" (p152)；
    "Directory number 213100x (e.g. 2131002)" (p154)；
    "SIP URI: Enter the device identity as follows: <directory number>@<OpenTouch server FQDN>
    2131002@opentouch.company.com" (p156)
  steps: |
    1. COS 前提：OmniVista 8770 → OmniPCX Enterprise 窗 → Classes of Service/Phone feature COS/<COS ID>
       （选目标用户 COS）→ "Ring all Secondary if Main Out of Service"=Yes。
    2. 功能前缀：Translator/Prefix Plan → 建前缀 506（Number=506、Prefix meaning=Local features、Local
       features=Twinset Get Call）；再建前缀 507（Prefix meaning=Set features、Station features=No ringing）
       （号码可自选空闲，实验口径）；Warning：两个特性必须在用户 COS 里 Validate。
    3. DM 声明：SIP 服务器配置界面（OT 侧）→ /Eco system/IT server/ → 右键 /create/Device management
       server/：Name 任意、FQDN=nms.company.com（实验口径，即 OmniVista 8770）、Port 保持默认 8080。
       OTC PC 软话机将从 DM 取 SIP 文件。
    4. 副设备创建：Users 应用 → 选有 NOE 主话机的用户（实验用 Boop，主 31002）→ 右键 "Add a secondary
       set" → "Add"：OXE directory number=2131002（无字母的纯数字）、Device type=SIP extension、OXE
       profile 可选、SIP password≥5 位。
    5. OTC PC 关联：Users 应用 → 选刚建的副设备 → 右键 "Associate SIP device" → New → OTC PC：SIP URI=
       2131002@opentouch.company.com（<分机号>@<OT 服务器 FQDN>，实验口径）；Security 页签配 SBC：
       SBC address=OTSBC 公共 FQDN（otsbc-podx.al-mydemo.com）、SBC port=5261、SBC protocol=TLS、
       SBC security level=Encrypted only。
    6. （可选）为 OTC PC 建设备档案（网络/视频/安全参数批量套用）——实验单用户未用档案。
  verification: |
    书中本章无独立测试问题；行为口径：主话机保留、副设备（OTC PC）作为 SIP 分机振铃（COS 的 Ring all
    Secondary 支配主设备离线时的振铃）。远程拨测场景与 c05 共用 p26-29 模拟器预期。
  conditions: 需 OmniVista 8770 与 OT/OXE 管理权；OTSBC 已部署（c02）。
  tags: [lab, otc-pc, multi-devices, cos, prefixes, sbc-settings]

- id: c05
  title: OTC PC 配置 Nomadic SIP 模式（Ghost Z 池、SIP 设备池、游牧许可、切换测试）
  type: lab
  source_pages: p157-161
  source_chapter: OTC PC for remote worker — "Nomadic in VoIP (SIP) mode"
  source_quote: |
    "Create 2 virtual Z devices for nomadic use: 31017 and 31018 … Create 2 SIP devices: 31951 & 31952 …
    Assign the nomadic SIP rights to 'Barkley' … Switch the current phone from 'Deskphone' to 'Personal
    Computer' in order to test this VoIP Nomadic mode. Test the solution." (p157)
    "AS FOR GSM NOMADIC MODE, SIP NOMADIC REQUIRE A POOL OF Z GHOST DEVICES." (p158)
  steps: |
    1. OXE 建 Ghost Z 池：OXE 配置界面 → /Users/ → Create → "general Ch." 页签：Directory number=
       31017（实验口径）、Set Type=Analog → "facilities" 页签：Ghost Z 勾选、Ghost Z feature=Nomadic；
       同法建 31018。
    2. OT 申报 Ghost Z 池：/System services/Topology/OXE CS/OXE Resources → Z ghosts min value / max
       value 填池号段两端。
    3. OXE 建 SIP 设备池：/Users/ → Create → "general Ch."：Directory number=31951、Set Type=SIP device
       （实验口径）；回该用户 → "SIP" 页签：URL UserName/Domain/SIP Authentication 自动回填，Password
       默认 0000 → 改为与分机号一致（31951）；同法建 31952。
    4. OT 申报 SIP 设备池：/System services/Topology/OXE CS/OXE SIP Subscriber → General 页签：SIP
       nomadic device number=31951、OXE CS=所在 OXE、SIP Login=31951、SIP Password=上步口令；Security
       页签：SBC WAN=选已申报的 SBC（远程接入用）；同法申报 31952。
    5. 授游牧权：/Users and Devices/Users/ → 选 Barkley（实验口径）→ "licenses" 页签：Nomadic SIP 勾选、
       Desktop 勾选。
    6. 测试：把 Barkley 当前话机从 "Deskphone" 切到 "Personal Computer" → Test the solution（游牧激活后
       主设备冻结、SIP 软话机顶替；退出游牧释放池资源）。
  verification: |
    p157 明示测试动作："Switch the current phone from 'Deskphone' to 'Personal Computer' in order to test
    this VoIP Nomadic mode. Test the solution."；呼叫行为验证可用 p26-29 模拟器号码规则互拨核对。
  conditions: 池大小=并发游牧连接数（含 SIP 设备与 Ghost Z 两池）；OTSBC 已部署（c02）。
  tags: [lab, nomadic-sip, ghost-z, sip-device, pooling, otc-pc]

- id: c06
  title: OTC 智能手机配置（双模式/twinset）：OXE 通用参数、OT 侧 SBC 与系统参数、设备档案、用户关联与自动对象核验
  type: lab
  source_pages: p189-203, p207-212
  source_chapter: OTC smartphone for Connection users — "Declare and configure OTC smartphone for a Connection user"
  source_quote: |
    "Number: Enter the prefix directory number (e.g.: 31280); Prefix Meaning: Remote Extension DISA" (p192)；
    "OTC Smartphone number: D2131001; Remote extension number: 2131001; Speed dial number: A2131001" (p201)；
    "Route 1: Automatically configured: SIP device number (e.g. D2131001); Route 2: … external mobile number
    using public TG" (p211)
  steps: |
    1. OXE 通用参数（9 项）：①专用 ARS 前缀（Translator/Prefix Plan，例 #0、ARS Prof Trg Grp Seiz with
       overlap、指定判别器号）；②RE DISA 前缀（例 31280；Warning：核对 DDI 翻译表）；③自动替代
       （System/Other System Param./DISA Parameters=Without code）；④中继组本地参数（Trunk group used in
       DISA=Yes）；⑤RE 参数（Applications/Remote Extension Parameters，DTMF 序列可改）；⑥RE 激活/去激活
       前缀 61/62（Station features）；⑦Ghost Z 池（Users 建 B31091 型号、Analog、Can be Called By Name=
       NO、Ghost Z=Remote Extension；Tip：一个 RE 一个 ghost 更稳）；⑧直连速拨号范围（index 0、长度
       1000；不能为 0、不能满）；⑨溢出定时器（SIP to Ch Error Mapping=Temporary failure、INVITE 重传 2-3、
       Trunk COS 31 的 T310=60）。
    2. OT 服务器参数：①iPhone+ 专用 SBC 声明（Eco system/IT Server → Create → SBC server：FQDN 同通用
       SBC、WAN、Port 5265）；②OXE CS 前缀同步（System services/Topology/OXE CS/…/OXE CS → Actions →
       勾 "OXE CS prefixes synchro" 手动同步）；③Telephony settings 页签：RE DISA 公共号码（例
       +3320131444）、ARS 前缀（例 #0306）、判别器号、公网区号、中继组 ID、ARS Route list MAX ID=3999。
    3. 设备档案（可选但建议）：Profiles/Device → Create → OTC Smartphone：General（Type of node=OXE、
       Type of mobile=Android 或 iPhone、Connectivity=GSM only/Wifi only/dual、Fallback enabled）→
       Network（SBC WAN=已申报 SBC、Protocol=UDP 默认）→ OXE ARS 页签（多租户差异化时用）。
    4. 用户关联（实验用 Backman）：Users 应用 → 选用户 → 右键 "Associate SIP device" → New → OTC
       Smartphone：General 页签（Device number=D2131001、GSM number=+33698765432 规范格式、OT device
       profile=步骤 3 档案）；OXE CS 页签（Remote extension directory number=2131001——禁用字母开头、
       Direct speed dial number=A2131001）。
    5. 授移动权：该用户 "OT configuration" → "Licenses" → Off site mobility 勾选。
    6. 自动对象核验（p207-211 逐项）：RE（Users 里 D431001：号码/类型/名称自动配、RE number 自动=#0306x…）；
       速拨号（Direct SpdDI No. Pref.=A2131001、Call Number=00687654321、External DISA=2131001）；Tandem
       （Prog. Keys 自动建 L1/L2、Tandem DN=2131001、Main set 勾选）；SIP 设备（D2131001、Set type=SIP
       device）；判别器（Nb 3：<3>+<068765432>、Area=1、路由表=MAX ID 起首空号、Schedule=-1、位数=11；
       注意核对用户 COS 授权该区域）；ARS（表 3999：Route 1=D2131001、Route 2=公网 TG 呼手机、时间表 1&2）。
    7. 手工补充两项（Warning）：Entity 判别器关联（Entities → 用户 Entity → Discriminator 0x=03 关联逻辑
       判别器 3）；公网接入 COS（Access COS，例 2）核对区域授权——系统呼手机必须能过 barring。
  verification: |
    p202/206 关联核验（"OT configuration"→"Device" 页签出现 RE 与速拨号）；p207-211 自动对象逐项截图
    核对清单；p210/212 的区域授权核对。端到端呼测可用 p26-29 模拟器规则（书内未单独给智能手机呼叫测试问题）。
  conditions: 双模式要求用户有主话机（twinset 结构）；版本前提 OpenTouch R2.6（单设备另见 c07）。
  tags: [lab, smartphone, dual-mode, disa, ars, discriminator, automatic-provisioning]

- id: c07
  title: OTC 智能手机单设备场景（R2.6 新法）与 App 安装、iPhone+ 维护
  type: lab
  source_pages: p204-206, p213-217
  source_chapter: OTC smartphone for Connection users — "Specific case of smartphone as single device / Application installation / Maintenance"
  source_quote: |
    "Now, from release 2.6 of OpenTouch, the main device can be directly the remote extension" (p204)；
    "Public hostname or URL: Enter the public URL of the server (reverse proxy) e.g.: https//otms.company.com" (p214)；
    "service kamailio-wasp status|start|stop|restart … Location: /var/log/localmessages" (p217)
  steps: |
    1. 建单设备用户：Users Application → Create：User type=OXE、姓名/邮箱等必填项、OXE ID=选 OXE、
       OXE directory number=310xx（实验口径 31033）、Device type=Remote extension、Applications=OT、
       OT instance=选实例、登录/GUI/TUI 口令等补齐。
    2. 关联手机：右键 "Associate SIP device" → New → OTC Smartphone：General（Device number=D21310xx、
       GSM number 规范格式、可选档案）；OXE CS 页签（Remote extension directory number=31033——与建户时
       主号一致、Direct speed dial=A31033）。
    3. 核验与授权：OT configuration → Device 页签核对自动关联；Licenses → Off site mobility 勾选。
    4. Android 安装：Google Play 搜 "OpenTouch" → OpenTouch Conversation → Install → 接受条款 → 首启填
       Public hostname/URL（反代公共 URL，例 https//otms.company.com——原书如此缺冒号）、Private
       hostname/URL（opentouch.company.com）、用户名、GUI 口令。
    5. iPhone 安装：App Store 搜 "alcatel" → OpenTouch Conversation Plus → Get/Install（ iTunes 口令按需）
       → 首启填 Public Server Name、Private Server Name、Login、Password。
    6. iPhone+ 维护：service kamailio-wasp status|start|stop|restart；日志 /var/log/localmessages；级别
       /usr/kamailio-wasp/loglevel.sh {level}（3=DBG、2=INFO、1=NOTICE、0=WARN、-1=ERR）；service wspcfgd
       status|start|stop|restart；日志 /logs/wspcfg/wspcfg.log；loglevel.sh component=wspcfg logger=*
       level=debug；Logzipper 打包含 kamailio 与 wspcfg 日志。
  verification: |
    p206 单设备关联核验截图（Device 页签）；p214/216 App 首启填 URL 后可登录即接入成功（书中以首启界面
    为验收画面）；p217 给维护命令与日志路径作为 iPhone+ 故障抓手。书中未给端到端呼叫测试问题。
  conditions: 单设备为 R2.6 起的新配法（R2.5 及以前需永不入服 SIP 主设备，见 p27/n17）；外链 TC2341en
    部署指南（businessportal2.alcatel-lucent.com/TC2341en）。
  tags: [lab, smartphone, single-device, app-install, kamailio-wasp, wspcfg]

- id: c08
  title: Nginx 独立反向代理部署（Ubuntu VM、Nginx 安装、证书、三份 conf、LDAP 认证）
  type: lab
  source_pages: p218-259
  source_chapter: Nginx reverse proxy deployment — "Install and deploy Nginx Reverse Proxy on Ubuntu server"
  source_quote: |
    "deb http://nginx.org/packages/mainline/ubuntu xenial nginx" (p247)；
    "openssl req -new -key rp.key -out rp.csr … Common Name … ot-podx.al-mydemo.com" (p250)；
    "resolver 151.1.1.100;" (p254)
  steps: |
    1. 准备：模板文件从 nas.alcatel-support.com 链接下载（链接来自 TC2639/TC2257，必须用最新版链接）；
       拓扑 NAT：ot-podx.al-mydemo.com↔195.128.146.10x、195.128.146.10x↔11.1.1.10、443/8016（实验口径）。
    2. 建 VM：ESXi 上建 Ubuntu 64 位 VM（1 vCPU、2 GB 内存、20 GB thin、1 网口接 DMZ、Ubuntu iso 光驱；
       详细逐步见 c10 同款操作）。
    3. 装 Ubuntu：语言/国家/键盘按需 → 手动配网：IP=11.1.1.10、掩码 255.255.255.0、网关 11.1.1.254（实验
       口径；书内清单页一处写 10.1.0.254，为笔误）、DNS 填公共 DNS（装系统更新用；私有 DNS 后续写在
       Nginx 配置）、主机名 rp、域 company.com、建账号、不加密 home、整盘分区、HTTP 代理按需、无自动更新、
       勾 OpenSSH server、装 GRUB → 重启。
    4. 系统更新：rpuser 登录（实验口径口令 Sdfghjk1）→ sudo -s → apt-get clean / update / upgrade。
    5. 装 Nginx：sources.list 追加两行（deb http://nginx.org/packages/mainline/ubuntu xenial nginx 及
       deb-src）→ apt-get update（出现 NO_PUBKEY ABF5BD827BD9BF62 未签名告警，实验继续）→ apt-get
       install nginx（"cannot be authenticated" 选 Y）→ shutdown -r now 重启。
    6. 证书：FileZilla 把 CA 根证书拷到 RP → mv rootCA.pem /etc/ssl/certs/ → update-ca-certificates →
       openssl genrsa -out rp.key 2048 → openssl req -new -key rp.key -out rp.csr（FR/Brest/ALU/TS/CN=
       ot-podx.al-mydemo.com，实验口径）→ CA 签发（同 c02 流程）→ 建 /etc/nginx/cert 与
       /etc/nginx/conf.d/snippets → rp.crt/rp.key 移入 /etc/nginx/cert → 改 snippets 下 conference_ssl.conf
       与 remoteworker_ssl.conf 的 ssl_certificate/ssl_certificate_key 路径（V1.5 模板，含 8016 通知端口
       server 段）。
    7. 配置文件：remoteworker.conf、global.conf、conference.conf 移入 /etc/nginx/conf.d/ → global.conf 的
       resolver 改内网 DNS（151.1.1.100）→ remoteworker.conf 第 17/177 行 server_name 改 OT 公共 FQDN →
       conference.conf 第 13/33 行改会议公共 FQDN → snippets/opentouch_fqdn.conf 改 11 个变量（$otpublic_
       name、$host_domain、$otname、$opentouchfqdn、$ip_opentouch、$ot_domain、$otmanagement、$acsname、
       $acsfqdn、$clusterdomain 等，实验口径值见 p254）→ nginx -t 校验 → /etc/init.d/nginx start。
    8. LDAP 认证（推荐生产；实验可跳过）：不开认证时先注释 remoteworker.conf 的整个 AUTH LDAP 段；启用
       时 apt-get install python python-ldap（仅 Python 2）→ 拷 nginx-ldap-auth 与
       nginx-ldap-auth-daemon.py → mkdir /etc/nginx/conf.d/ldap → 移入、chmod +x、chown root:root →
       update-rc.d nginx-ldap-auth defaults →（脚本报错时 dos2unix 转格式）→ 改 snippets/ldap.conf
       （$ldapaddress=ldap://151.1.1.100、$basedn、$binddn、$ldappwd，实验口径）→ service nginx-ldap-auth
       start（daemon 监听 8888）→ nginx restart。
  verification: |
    p254 "Check the nginx configuration: nginx -t"；p259 service nginx-ldap-auth start 后由认证流程闭环
    验证。书中未给浏览器端到端访问测试问题；反代声明（OT 侧四 URL）由 c01 步骤 1 承接。
  conditions: OT 2.2 起必须 remoteworker.conf 与 conference.conf 同改；模板以 TC2639 最新版链接为准。
  tags: [lab, nginx, reverse-proxy, ubuntu, certificates, ldap-auth]

- id: c09
  title: OpenSSL 自建 CA 并签发通配符证书（含 pkcs12 打包与客户端/服务器导入）
  type: lab
  source_pages: p260-268
  source_chapter: OpenSSL — "Generate a certificate using OpenSSL as certification authority"
  source_quote: |
    "openssl genrsa -out rootCA.key 2048 … openssl req -x509 -new -nodes -key rootCA.key -days 3650 -out
    rootCA.pem" (p261-262)；
    "openssl x509 -req -in /CA/certs/servers.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out
    /CA/certs/servers.crt -days 3650" (p263)；
    "THE CTL (USED BY DESKPHONES) HAS TO BE REGENERATED (SIGNED AGAIN)…" (p268)
  steps: |
    1. 建 CA 目录：在 FlexLM 服务器（CentOS，实验口径）建 /CA/authority、/CA/certs、/CA/keys。
    2. 根 CA：openssl genrsa -out rootCA.key 2048 → openssl req -x509 -new -nodes -key rootCA.key -days
       3650 -out rootCA.pem（填 FR/Brittany/Brest/Company/Training/flex.company.com/administrator@
       company.com，实验口径）。
    3. 服务器密钥与 CSR：cd /CA/keys → openssl genrsa -out servers.key 2048 → cd /CA/certs → openssl req
       -new -key /CA/keys/servers.key -out servers.csr（CN=*.company.com 通配符，挑战口令例 sdfghjk1，
       实验口径）。
    4. 签发：cd /CA/authority → openssl x509 -req -in servers.csr -CA rootCA.pem -CAkey rootCA.key
       -CAcreateserial -out servers.crt -days 3650（首次用 -CAcreateserial；后续用 -CAserial 指定 .srl
       文件）。有效期 10 年。
    5. 打包：openssl pkcs12 -export -in servers.crt -inkey servers.key -certfile rootCA.pem -out
       servers.p12（导出口令=生成时挑战口令，实验口径）。
    6. 客户端导入根证书：Chrome → Settings → Show advanced settings → Manage certificates → Trusted Root
       Certification Authorities → 文件类型选 All Files → 选 rootCA.pem → 导入；IE/Edge 也要做（Windows
       级生效）。
    7. OT 服务器部署：WebAdmin → System services/Certificate/Certificates/ → 点当前证书 → Change server
       certificate → 选 "External certificate (import pkcs#12 file)" → 填 PKCS#12 passphrase → 选
       servers.p12 → Import → Yes。
  verification: |
    p263 签发输出 "Signature ok" 与 subject 行；p268 导入后 WebAdmin https 会话被切断（预期行为，重连
    即可）；Warning 提示 CTL（话机用）须因服务器证书变更而重新签名——该操作属另一培训规程，本实验不含。
  conditions: 通配符证书 *.company.com 用于 OpenTouch/RP（可复用于 OTSBC）；CA 复权与生产签发流程在书外。
  tags: [lab, openssl, ca, certificates, pkcs12, wildcard]

- id: c10
  title: VMware 虚机 OVF/OVA 部署（web client 与 vSphere client 两路）
  type: lab
  source_pages: p269-277
  source_chapter: Virtual machine deployment — "Deploy a VMware virtual machine"
  source_quote: |
    "Deploy a virtual machine from OVF or OVA file … Network mappings: Select the network corresponding to
    the DMZ; Disk provisioning: … 'Thin' for lab" (p271-273)；
    "Warning: VSPHERE CLIENT IS ONLY AVAILABLE WITH ESXI VERSION 6.0 OR LOWER." (p274)
  steps: |
    1. web client 路（ESXi 6.5 口径）：浏览器开 ESXi IP 登录 → 点新增虚机 → "Deploy a virtual machine
       from OVF or OVA file" → 命名 → 选 ovf+vmdk 文件（ova=ovf+vmdk 打包，原理相同）→ Next → 选存储
       位置 → Next → Network mappings 选 DMZ 对应网络、Disk provisioning 选 Thin（实验口径）、勾 Power on
       automatically → 核对 → Finish。
    2. vSphere client 路（仅 ESXi ≤6.0）：vSphere client → File → Deploy OVF Template → 选 OVF → Next →
       命名 → Next → 选存储 → Next → 磁盘类型（例 Thin）→ Next → VM Network 选对应网络（LAN/DMZ）→
       Next → Finish。
  verification: |
    部署向导 Finish 后虚机出现在清单并自动上电（勾选时）；书中无更深验证步骤（该章为通用承载技能，
    服务于 c02/c03/c08 的虚机准备）。
  conditions: vSphere client 仅 ESXi 6.0 及以下可用；生产资源规格按实际 sizing（书外）。
  tags: [lab, vmware, ovf, esxi, deployment]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 14 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 认知 RLAB 实验环境 | 无实验章。p4-30 为环境说明页（虚机清单/账号/编号计划），属认知材料，已在 principle/framework 类收录。 |
| task-02 规划远程接入拓扑 | 无实验章。p31-46 为讲义（拓扑/组件/DNS/证书原则），属决策内容；决策依据已散入 c01-c03 的 conditions。 |
| task-03 证书策略与签发 | 有 → c09（OpenSSL 自建 CA 全流程）；Windows CA 申请路径含于 c01 步骤 7。 |
| task-04 服务器侧远程访问设置 | 有 → c01 |
| task-05 部署 OTSBC | 有 → c02（VM 承载技能由 c10 支撑） |
| task-06 内嵌 RP 部署 | 有 → c03 |
| task-07 Nginx RP 部署 | 有 → c08（虚机与系统安装的通用步骤由 c10/Ubuntu 段承接） |
| task-08 VMware 虚机部署 | 有 → c10 |
| task-09 客户端远程接入 | 无独立实验章。p145-150 为讲义级两步法（各客户端入口界面说明），已由 framework f13 收录；接入动作分散在 c04 步骤 5（OTC PC 填 SBC）与 c07 步骤 4-5（手机填 URL）。 |
| task-10 OTC PC multi-devices | 有 → c04 |
| task-11 OTC PC Nomadic SIP | 有 → c05 |
| task-12 智能手机 Connection 用户 | 有 → c06（双模式全流程）、c07（单设备 + App 安装 + 维护） |
| task-13 iPhone+ APNS 专项 | 部分 → c07 步骤 6（kamailio-wasp/wspcfg 维护）与 c06 步骤 2①（SBC 5265 声明）；防火墙端口/APNS 证书机制为讲义数值（p30 条目），书中无独立 iPhone 实验（明示"not part of this lab"）。 |
| task-14 拨测验证 | 无独立实验章。p26-29 为模拟器规则说明（预期结果表），已由 principle p10 / framework f04 收录；各实验的验证字段如实收录在各条 verification。 |

**统计**：10 条（lab 10 条）；14 项任务中 9 项有案例类条目直接覆盖，5 项为讲义/认知/规则内容无独立实验（task-01/02/09/14，task-13 为部分覆盖），原因已逐条注明。
**验证口径说明**：本书实验的"验证"以界面结果核对（Result 截图、列表出现新条目、证书 SAN、nginx -t、ping）与动作指令（"Test the solution"、切换 Deskphone→Personal Computer）为主，除 c05 外无书面的测试问题清单；各条 verification 均按原文如实转写，未编造测试问题。
