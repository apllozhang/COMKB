# 案例/实验/操作序列候选 — OpenTouch Advanced (OPENXTE301EN Ed08, R2.6.1)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号）标注"实验口径"。
> 条目说明: 全书 16 个 How-To 实验章 → 22 条（Pod 配置 1、Nomadic 拆 3、Desksharing 拆 2、远程接入拆 2、智能手机拆 3、UM 拆 2、RADIUS 与 FreeRADIUS 合 1）。

```yaml
- id: c01
  title: 实验 Pod 配置（虚机、机架/板卡、用户/IPDSP、外部 SIP 网关、DID 翻译、外呼验证）
  type: lab
  source_pages: p24-30
  source_chapter: OpenTouch Pod Configuration (How-To)
  source_quote: |
    "Start the virtual machines using the start buttons ... Software licenses are restored • FlexLM Server is
    declared • Shelves / boards are created • Some users (Deskphones & softphones) are created • Voice guides
    are downloaded • Public SIP trunk group is created" (p25)
    "Users / <User to modify> / Tsc IP User ... IP-Softphone Emulation Set to 'No'" (p28)
    "Translator/External Numbering Plan/Default DID num. translator ... First external number 33210N41000 ...
    First internal number 31000 ... Range Size 500" (p30)
  steps: |
    1. 在 RLAB 门户启动全部虚机（OXE/OMS/OTMS/8770/DCS/ECOSYSTEM/PC Client 10/11）；确认预置项：许可已恢复、
       FlexLM 已声明、机架/板卡已建、用户已建、语音引导已下载、公网 SIP 中继组已建。
    2. 机架核对（仅需 OMS）：Software Rack 3U（OMS），Rack N°4，Virtual GD4（slot 0）IP 192.168.1.13/24、
       MAC 00:50:56:01:01:13（实验口径）；确认设备 in service。
    3. 用户/IPDSP：31000 Brad Barkley、31001 Billy Backman（IP DSP，Main，分别装在 PC Client 10/11）；
       IPDSP 右键 Settings → Network 页签填 TFTP 服务器 IP = OXE CS Main 192.168.1.3（实验口径）。
    4. （混合模式）把 31000/31001 改为课堂实机：Users/<user>/Tsc IP User → IP-Softphone Emulation = No；
       Users/<user>/Set Type 选实际话机类型。
    5. 外部 SIP 网关：SIP/SIP Ext. Gateway 选中网关，Registration ID = pbxN、Outgoing username = pbxN
       （N=POD 号，例 POD3 → pbx3，实验口径）。
    6. DID 翻译：Translator/External Numbering Plan/Default DID num. translator → Create：First external
       number = 33210N41000、First internal = 31000、Range size = 500（例 POD3：33210341000）。
    7. 外呼验证：按 SIP Carrier Simulator 文档发起出局呼叫，确认公网 SIP 载体可达。
  verification: |
    外呼测试成功（p30 "To make sure that access to public SIP carrier is working properly, set up some
    outgoing calls"）；IPDSP 注册成功（TFTP 指向正确）。
  conditions: RLAB 环境；全部参数为实验口径；Pod 号 N/P 决定 pbxN 与号码段。
  tags: [lab, pod, oxe, sip-gateway, did]

- id: c02
  title: Nomadic 蜂窝模式（cellular）——Ghost Z 池、权限、号码管理
  type: lab
  source_pages: p45-51
  source_chapter: OTC PC for Connection users in nomadic mode — "1 Nomadic in cellular mode"
  source_quote: |
    "Create three virtual ghost Z sets: 31017, 31018 & 31019 • Assign the 'Nomadic GSM' right to the user ...
    Don't forget to allocate the ('Desktop' rights to Mr Barkley to enable the application. Perform a test." (p47)
    "/Users/ Create & select the 'general Ch.' tab ... Directory number Enter a free directory number • Set
    Type Select 'Analog'" (p47)
    "/System services / Topology / OXE CS / OXE Resources ... Z ghosts min value ... Z ghosts max value" (p48)
    "Tips It is possible to specify an internal number for home and personal mobile phone numbers. Colleague
    number cannot be used for nomadic mode." (p50)
  steps: |
    1. 任务：为 Brad Barkley 开通蜂窝 nomadic，目的号码为其家庭电话 0210X12345（实验口径）。
    2. OXE 建 Ghost Z 池：Users/ → Create → general Ch. 页签：Directory number = 31017/31018/31019、
       Set Type = Analog；facilities 页签：勾 Ghost Z、Ghost Z feature = Nomadic。×3 个。
    3. OT 侧登记范围：System services/Topology/OXE CS/OXE Resources：Z ghosts min/max = 31017/31019。
    4. 授权：Users and Devices/User → 选 Barkley → Licenses 页签：Nomadic GSM 与 Desktop 均启用。
    5. OTC PC 号码管理：设置图标 → Home 填家庭号码、Mobile 填手机号（可填任意希望转接的号码；同事号码
       不可用）。
    6. OTC PC routing 窗口把"当前电话"切到 Home phone/Mobile 触发 nomadic。
  verification: |
    测试：nomadic 激活后办公话机冻结（frozen），呼叫 Barkley 内线号码被转往指定号码；关闭 nomadic 后话机
    恢复。Ghost Z 在连接期间保持 busy（p47 机制口径）。
  conditions: Desktop 许可必须先配（Tips p46）；每路连接占 1 个 Ghost Z。
  tags: [lab, nomadic, cellular, ghost-z]

- id: c03
  title: Nomadic VoIP 模式——SIP 设备池、OT 侧声明、SBC
  type: lab
  source_pages: p51-54
  source_chapter: OTC PC for Connection users in nomadic mode — "2 Nomadic in VoIP mode"
  source_quote: |
    "Create 2 SIP devices: 31951 & 31952 ... Declared in the OXE database • Declared in the OpenTouch
    database • Assign the nomadic SIP rights to 'Barkley' • Switch the current phone from 'Deskphone' to
    'Personal Computer' in order to test this VoIP Nomadic mode" (p51)
    "Warning The management done for nomadic in cellular mode shown in the previous step is a pre-requisite." (p51)
    "/System services / Topology / OXE CS / OXE SIP Subscriber ... SIP nomadic device number ... OXE CS ...
    SIP Login ... SIP Password ... In 'Security' tab, specify the SBC to use for access from outside ... SBC
    WAN" (p53)
  steps: |
    1. 前提：c02 蜂窝模式管理已完成（Warning：cellular 配置是 VoIP 的前置）。
    2. OXE 建 SIP 设备池：Users/ → Create → general Ch.：DN = 31951、Set Type = SIP device（再建 31952）；
       SIP 页签核对自动值：URL UserName（默认=DN）、URL Domain（默认=node 名，取自 netadmin -m 选项 17）、
       SIP Authentication（默认=DN）、Password（默认 "0000"，可改为与 DN 相同，实验示例 31951）。
    3. OT 侧声明池：System services/Topology/OXE CS/OXE SIP Subscriber → General：SIP nomadic device
       number=31951、OXE CS=所在 OXE、SIP Login=URL UserName、SIP Password=SIP 密码；Security 页签：SBC
       WAN 选已声明的远程接入 SBC。
    4. 授权：Users and Devices/User → Barkley → Licenses：Nomadic SIP 与 Desktop 启用。
    5. 测试：OTC PC routing 窗口把当前电话从 Deskphone 切到 Personal Computer。
  verification: |
    来话在 PC（OTC 软话音）接听；办公话机保持冻结；关闭 nomadic 后 SIP 设备与 Ghost Z 释放。
  conditions: 每路 VoIP 连接占 1 Ghost Z + 1 SIP 设备；SIP 参数须 OXE/OT 两侧一致。
  tags: [lab, nomadic, voip, sip-device, sbc]

- id: c04
  title: Nomadic 资源验证与手动同步（tsa_maintenance）
  type: lab
  source_pages: p55-57
  source_chapter: OTC PC for Connection users in nomadic mode — "3 Maintenance"
  source_quote: |
    "[root@opentouch /]# cd /opt/Alcatel-Lucent/infra_services/ots [root@opentouch ots]# ./tsa_maintenance
    ... Trying connect: opentouch.company.com 3595 ... Connection with opentouch.company.com , port 3595 is OK" (p55)
    "Press 'return' and choose option 20 to dump all numbers ... 20 [+ qmcdu] ----------- Dump Nomadic" (p55)
    "Run './tsa_maintenance' script with option 100 to activate the synchronization ... (2998 is the secret
    code value). So, choose the 'ACAPI control' by entering '106 2998'" (p56-57)
  steps: |
    1. OT 服务器控制台/SSH：cd /opt/Alcatel-Lucent/infra_services/ots && ./tsa_maintenance（确认与
       opentouch.company.com:3595 连接 OK）。
    2. 回车后选 20 dump Nomadic：核对 31017/31018/31019 三个 Ghost Z 条目（type analog、Z nomadic 1）在
       ots 库中。
    3. 若缺失则手动同步：选 100（密码保护菜单，秘密码 2998）→ 输入 106 2998 进 ACAPI control → 输入 7
       （Load All Acapi Object）。
    4. 同步完成后再次 dump 核验（原文提示用 option 47 dump all QMCDU 或 option 20 dump nomadic；47 未在
       菜单中出现，按 20 核验）。
  verification: |
    选项 20 输出中三个 Ghost Z 全部在列（State: Free(1) 或 Unknown 均算在库，关键是有条目且 Z nomadic=1）。
  conditions: 脚本仅运行于 OT 服务器；秘密码 2998 为实验口径。
  tags: [lab, nomadic, maintenance, tsa_maintenance]

- id: c05
  title: Desksharing 配置——前缀 600/601、DSS、DSU、COS、系统参数
  type: lab
  source_pages: p62-71
  source_chapter: DeskSharing (How-To)
  source_quote: |
    "Desk Sharing Over Logon (600) • Desk Sharing Over Logoff (601) ... Translator/Prefix Plan/ Create" (p64)
    "Set Type IPTouch 8068 • Set Function Desk Sharing Set ... Directory Number 31100 ... Shelf/Board/
    Equipment Address 255" (p65)
    "Set Function Desk Sharing User ... Directory Number 31000" (p67)
    "aa:bb:xx:xx:xx:xx' where xx:xx:xx:xx is the directory number. Example for 31000: 'aa:bb:03:10:00'" (p67)
  steps: |
    1. 建前缀：Translator/Prefix Plan → Create：600 = Desk Sharing Over Logon（Station Features）；601 =
       Desk Sharing Logoff。
    2. 建 DSS：Users/ → Create：DN 31100、Shelf/Board/Equipment 255、Set Type IPTouch 8068、Set Function =
       Desk Sharing Set、Tel facility category ID = 0（实验口径）；话机注册后在 Users/Tsc IP User 查看
       真实 MAC/IP。
    3. DSS 可编程键：Users/Progr.Keys/：键 1 content 600 名称 LogOn（Locked YES）；键 2 content 0112# 名称
       Emergency（Locked YES，登录故障时呼救）。
    4. DSS COS：Classes of Service/Phone Facilities Categories/ → COS 0：Set features Desk Sharing Over
       Logon = 1、Logoff = 1。
    5. 改 DSU：选已有用户 Barkley（31000）→ Set Type IPTouch 8068、Set Function = Desk Sharing User、
       Shelf/Board/Equipment 255、COS 0；其虚拟 MAC 生成为 aa:bb:00:03:10:00（IP unused）。
    6. DSU 可编程键：键 1 = 600 LogOn、键 2 = 601 Log Off（均 Locked）；DSU COS 同第 4 步开启两项。
    7. 系统参数（/System/Other System Param./System Parameters 与 Spec. Customer Features Parameters）：
       Activate Logoff without pwd（默认 False）、DSU Auto Log-off Time（-1 或 0-23 整点）、Allow Reset of
       Busy DSU（True 时释放通话+6004 事件）、Default DSU Secret Code Change（True 时首登强制改密）。
  verification: |
    DSU 在 DSS 上按 LogOn 键+密码登录使用；LogOff 释放；换机登录行为按 Allow Reset 参数生效。
  conditions: DSS/DSU 的 Set Function 决定 MAC 虚实；Emergency 键为书中推荐配置。
  tags: [lab, desksharing, dsu, dss, cos]

- id: c06
  title: Desksharing 的 OTC PC 支持与命令行维护（domstat/ippstat/incvisu）
  type: lab
  source_pages: p72-75
  source_chapter: DeskSharing (How-To) — "4 OTC PC configuration / 5 Desk Sharing maintenance"
  source_quote: |
    "Enable the following licenses in order to be able to release (LogOff) the DSS from the OTC PC client:
    Desktop • Flex Office" (p72)
    "Warning MAKE SURE THAT THE 'DSU' USER ('BARKLEY') IS KNOWN IN THE OPENTOUCH DATABASE; IF UNKNOWN,
    PLEASE ASSIGN THE RIGHT TO USE 'OT APPLICATIONS' TO THIS USER." (p72)
    "Command incvisu ... |=4:6004=Communication End due to 31100" (p73)
    "Command domstat Option 9 Display all Domains Devices ... DS column shows Desk Sharing specific users S:
    means Desk Sharing Set U: means Desk Sharing User" (p73-74)
  steps: |
    1. OT 侧授权：Users and devices/User → Barkley → Licenses：Desktop 与 Flex Office 启用（远程释放
       DSS 的前提）；若 OT 库不认识该用户，先授 "OT Applications" 权限（Warning）。
    2. OTC PC 以 Barkley 登录，确认 "Release business phone" 选项可用（可远程释放 DSS）。
    3. 维护-事件：CS 上以 mtcl 登录执行 incvisu——6004 事件两种文案（"Communication End due to 31100"=
       他机登录导致、"...due to AutoLogoff"=定时登出导致）。
    4. 维护-清单：domstat（选项 9 列域内设备，DS 列 S=Set/U=User/-=普通）；ippstat（选项 8 列全部 MAC、
       选项 3 列本节点 IP 话机、选项 10 按 MAC/IP/号码检索）。
    5. 维护-状态：ippstat d 31000——DSU 未登录时 Out of service cause 显示 T（hs_terdef）、INTIP 255/255
       （虚拟 MAC 所致）；登录后无异常位、INTIP 为所在 DSS 的值（如 19/1），可据此反查登录在哪台 DSS。
    6. 复位：话机上按 "I"+# → IP parameters → Free seating（清除包括虚拟 MAC 的全部 DeskSharing 信息）。
  verification: |
    OTC PC 可见 Release business phone；domstat 中 S/U 标记正确；6004 事件可追溯。
  conditions: 命令均以 mtcl 登录 CS 执行。
  tags: [lab, desksharing, maintenance, domstat, ippstat]

- id: c07
  title: 远程接入声明——反向代理与 OTSBC（含 WebRTC SBC）
  type: lab
  source_pages: p103-107
  source_chapter: OpenTouch server settings for remote access — "1 Reverse Proxy declaration / 2 OTSBC declaration"
  source_quote: |
    "Declare the reverse proxy with the following URL for all services: https://ot-podX.company.com •
    https://ot-podX.company.com:8016 for EVS (notifications) ... SystemServices/System services/Topology/
    Reverse proxy ... Display name / API public URL / EVS public URL / ACS public URL / DMS public URL" (p104-105)
    "Eco system/IT server Right clic and 'Create' ... FQDN Enter the public FQDN of the OTSBC (e.g:
    ot-podX.company.com) Network type WAN Port 5261" (p106)
    "Declare the OTSBC for WebRTC use: otsbc-podx.company.com ... Port 8061" (p106-107)
  steps: |
    1. 规划：公网 IP 10.20.X.105、NAT 10.20.X.105<->192.168.2.105、端口 443/8016（RP）与 5261/8061/7000-7499
       （SBC）；外部 DNS 建 ot-podN.company.com → 10.20.1/3/5/7/9/11.105（按 POD，实验口径）。
    2. 反向代理声明：OmniVista 8770 → SystemServices/System services/Topology/Reverse proxy：Display name、
       API public URL = https://ot-podX.company.com、EVS public URL = https://ot-podX.company.com:8016、
       ACS public URL 与 DMS public URL 同 API。这些 URL 会写入客户端配置文件。
    3. OTSBC（OTC 客户端）：Eco system/IT server → Create：Name、FQDN = ot-podX.company.com、Network type
       = WAN、Port = 5261。
    4. OTSBC（WebRTC）：同路径 Create：FQDN = otsbc-podx.company.com、WAN、Port = 8061。
  verification: |
    远程 OTC 客户端用公共 URL/FQDN 能注册与呼叫（URL/FQDN 写入客户端配置文件，p105/p106 Notes）。
  conditions: NAT/DNS 前置；证书 SAN 要求见 c08。
  tags: [lab, remote-access, reverse-proxy, otsbc]

- id: c08
  title: DAS nomadic 规则、ACS 会议 FQDN（rehost）与 OpenTouch 证书全生命周期
  type: lab
  source_pages: p108-118
  source_chapter: OpenTouch server settings for remote access — "3 Management for conferences accesses"
  source_quote: |
    "Verify the DAS rules and add following rules if not present: s/^\\+N/N/ • s/^\\+M/M/ ... WARNING THE
    DECLARATION ORDER IS IMPORTANT. SEVERAL RULES CAN BE APLLIED AT A TIME" (p108)
    "Launch the rehosting script thanks to the command: 'ot-config.sh --rehost' ... Hostname conf-podx ...
    Domain name company.com ... IP Address 192.168.1.55" (p111)
    "Click on 'Generate CSR' ... Signature algorithm Select the algorithm (SHA256 is the best for security)" (p112)
    "https://eco.company.com/CertSrv ... Certificate Template Web Server ... Select the 'Base 64 encoded'
    format and click on 'Download certificate chain'" (p113-116)
  steps: |
    1. DAS 规则：Conference server Administration Console → Domain 选 Default → Edit DAS rules，核对/补齐
       法国 10 条（重点 R2.0 起 nomadic 的规则 7 s/^\\+N/N/ 与规则 8 s/^\\+M/M/）；注意顺序重要。
    2. ACS 验证：查 /var/data/bics/bics.conf 末尾 ACS 参数；查 OT 证书 SAN（My Profile 页证书图标 →
       Details）；可 ping ACS IP 192.168.1.55（实验口径）。
    3. 未配置则 rehost：ot-config.sh --rehost → ACS 页填 Hostname=conf-podX、Domain=company.com、
       IP=192.168.1.55；确认内部 DNS 有 conf-podX.company.com 条目（Warning：必须）；重启后 ping 域名与 IP
       验证。
    4. 证书更新：System services/Security/Certificate → Generate CSR（FR/省/市/公司/部门/邮箱/SHA256）→
       浏览器开 https://eco.company.com/CertSrv（administrator/superuser，实验口径）→ advanced request →
       base64 提交 CSR → 模板 Web Server → Base 64 下载证书链 → Change server certificate 选 pkcs#7 导入
       （pkcs#12 需 passphrase）→ Deploy（WebAdmin 会话断开属正常，重登）→ 复核 SAN 含会议 FQDN。
  verification: |
    bics.conf/SAN 显示 ACS 名称与 IP；ping conf-podX.company.com 与 192.168.1.55 通；新证书 SAN 齐全。
  conditions: 会议 FQDN 必须同时出现在 RP 与 OT 证书 SAN 中（Warning p109）。
  tags: [lab, das, acs, certificate, rehost]

- id: c09
  title: OTC 智能手机——OXE/OT 通用设置（ARS 前缀、DISA、RE 前缀、Ghost Z、速拨、SIP 定时器、iPhone+ SBC）
  type: lab
  source_pages: p120-129
  source_chapter: OTC smartphone for Connection users (How-To) — "1 General settings"
  source_quote: |
    "Specific ARS prefix for smartphone ... Number Enter a Prefix directory number (e.g.: #0) ... Prefix
    Meaning ARS Prof Trg Grp Seiz with overlap • Discriminator No. Specify a logical discriminator ID" (p121)
    "Remote extension DISA prefix ... Number Enter the prefix directory number (e.g.: 31280) ... Warning
    CHECK THAT THIS PREFIX IS TRANSLATED IN THE DDI TRANSLATION TABLE" (p122)
    "System/Other System Param./DISA Parameters ... Automatic DISA Substitution Without code" (p122)
    "Eco system / IT Server Right click and « Create » ... Select « SBC server » ... Port 5265" (p127)
  steps: |
    1. OXE：Translator/Prefix Plan 建智能手机专用 ARS 前缀（例 #0，Meaning=ARS Prof Trg Grp Seiz with
       overlap，配逻辑识别码 ID）。
    2. OXE：建 RE DISA 前缀 31280；核对该前缀在 DDI 翻译表中可翻译（Warning）。
    3. OXE：DISA 参数（System/Other System Param./DISA Parameters）Automatic DISA Substitution = Without
       code；公网中继组本地参数 Trunk group used in DISA = Yes。
    4. OXE：RE 激活/停用前缀 61/62（Station Features）；（可选）Applications/Remote Extension Parameters
       改 DTMF 序列。
    5. OXE：建专用 Ghost Z 池（Users/ → Create：DN 可用 B<号> 如 B31091、Set Type Analog、Can be Called/
       Dialed By Name = NO、Ghost Z 勾选、feature = Remote Extension）；建议每 RE 一个 Ghost。
    6. OXE：速拨范围 Speed Dialing/Direct Speed Dialing Numbers：起始索引 0、长度例 1000（不能为 0/满）。
    7. OXE：SIP 溢出参数——SIP/SIP to Ch Error Mapping：Decline → CH Cause Temporary failure；SIP/SIP
       Proxy：INVITE 重传 2 或 3；External Services/Trunk COS 选 COS 31：Timer T310 = 60。
    8. OT：Eco system/IT Server → Create → SBC server（iPhone+ 用）：FQDN 同通用 SBC（ot-podX.company.com）、
       WAN、Port 5265。
    9. OT：执行手动同步取回 OXE 的 RE 激活/停用前缀——System services/Topology/OXE CS/…/OXE CS → Actions
       页签勾 OXE CS prefixes synchro；Telephony settings 页签手工填 RE DISA 公网号（例 +33210X41280）、
       ARS prefix（例 #0306）、专用 Discrimination rule、区域号、中继组 ID（ARS Route list MAX ID 默认 3999）。
  verification: |
    OT 侧前缀同步完成后 RE activation/deactivation 前缀自动出现（p128）。
  conditions: 31280/61/62/#0/#0306 均为实验示例值。
  tags: [lab, smartphone, oxe, disa, sbc]

- id: c10
  title: OTC 智能手机——设备档案与用户配置（含 R2.6 单设备特例）
  type: lab
  source_pages: p129-136
  source_chapter: OTC smartphone How-To — "2 User and device configuration in OpenTouch"
  source_quote: |
    "Profiles tab/Device Right click and 'Create' Select 'OTC Smartphone' ... Type of node OXE • Type of
    mobile Select Android or iPhone • Connectivity Select the mode: GSM only, Wifi only or dual mode" (p129-130)
    "Right click 'Associate SIP device' and 'New' and then 'OTC Smartphone' ... Device number D2131001 • GSM
    number +33610X12345 ... Remote extension directory… 2131001 ... Do NOT use a number beginning with letter
    (A,B,C,D) in the directory number of the Remote Extension!" (p131-132)
    "Assign 'Off site mobility' right to this user. ... 'Licenses' tab Off site mobility Checked" (p133)
    "From release 2.6 of OpenTouch, the main device can be directly the remote extension ... Single device
    (main one): remote extension" (p134)
  steps: |
    1. 建设备档案（Profiles/Device → OTC Smartphone）×2（Android 一个、iPhone 一个）：General 页签 Type of
       node=OXE、Type of mobile、Connectivity（GSM only/Wifi only/dual mode）、Fallback mode enabled 按需；
       Network 页签 SBC WAN=已声明 SBC、Protocol=UDP（默认）；OXE ARS 页签按多租户需要覆盖通用值。
    2. 用户关联：Users 应用 → 选用户（Backman）→ 右键 Associate SIP device → New → OTC Smartphone：
       General 页签 Start with profile=档案、Device number=D2131001、GSM number=+33610X12345（规范格式）、
       OT device profile=档案；OXE CS 页签 Remote extension directory number=2131001（禁用 A-D 字母开头）、
       Direct speed dial number=A2131001。
    3. 核验自动关联：Users → OT configuration 页签 → Device 页签：RE 与 OTC Smartphone 已自动关联。
    4. 授权：OT configuration → Licenses：Off site mobility 勾选。
    5. （R2.6 特例：手机即主设备）建 Connection 用户：User type=OXE、OXE directory number=31033、Device
       type=Remote extension、Applications=OT；关联手机时 RE 目录号填 31033（与主号相同）、设备号
       D2131033、速拨 A31033；同样勾 Off site mobility。
  verification: |
    OT configuration/Device 页签同时列出 RE（2131001）与 OTC Smartphone（D2131001）；Off site mobility 已勾。
  conditions: 手机号用 E.164 规范格式；设备号/速拨号可带字母前缀。
  tags: [lab, smartphone, device-profile, rex, r2.6]

- id: c11
  title: OTC 智能手机——自动对象核验、Entity/COS 手工补充、App 安装与维护
  type: lab
  source_pages: p137-147
  source_chapter: OTC smartphone How-To — "3 Verification / 4 Additional manual management / 5 Application installation / 6 Maintenance"
  source_quote: |
    "Users Select and edit the user corresponding to the remote extension created ... Set type Automatically
    set: Remote extension ... Remote extension number External number to reach the mobile phone automatically
    configured e.g.: #0306xxxxxxxx" (p137)
    "Warning Each Entity where dual mode CT users will be declared, it is important to review the Discriminator
    Selector ... Warning To be able to call the mobile the system must pass the baring." (p142)
    "service kamailio-wasp status|start|stop|restart ... Log files: /var/log/localmessages ... loglevel.sh
    {level}: 3=DBG, 2=INFO, 1=NOTICE, 0=WARN, -1=ERR" (p147)
  steps: |
    1. 核验自动对象（OmniVista OXE 配置工具）：①Users → RE 用户（如 D431001）：DN=2131001、Set type=Remote
       extension、Can be Called/Dialed By Name=NO、RE number=#0306xxxxxxxx；②Speed Dialing/Direct Speed
       Dialing Numbers：前缀 A2131001、Call Number=00610112345、External DISA Dir. No.=2131001；③Tandem：
       Users/Prog. Keys 确认 L1/L2 双线；Users → 主话机 31001 → All 页签：Tandem DN=2131001、Main set 勾选；
       ④SIP 设备：D2131001 Set type=SIP device；⑤识别码：Translator/External Numbering Plan/Numbering
       Discriminator 选 Nb 3：Tandem DN=<3>+<0610112345>、Area=1、ARS Route List=首个空闲号、Schedule=-1、
       位数 11；⑥ARS：ARS Route list 选 3999（对应设备 Mobile_83262）：Route 1=D2131001、Route 2=公网 TG
       拨手机、时间表 1&2。
    2. 手工补充：①Entities → 用户 Entity（例 1）→ Discriminator Selector：逻辑识别码 3 ↔ 物理识别码
       （Discriminator 0x=03）；②Classes of Services/Access COS 选用户公网 COS（例 2）：确认识别码所用区域号
       已授权（barring 放行）。
    3. 安装 App：Android——Google Play 搜 "OpenTouch" 装 OpenTouch Conversation，首启填 Public URL
       （https://ot-podX.company.com）/Private URL（https://opentouch.company.com）/账号/GUI 密码；iPhone——
       App Store 搜 "alcatel" 装 OpenTouch Conversation Plus，同法填写。
    4. 维护（iPhone+）：service kamailio-wasp status|start|stop|restart，日志 /var/log/localmessages，级别
       loglevel.sh {level}（3=DBG…-1=ERR）；service wspcfgd 同族，日志 /logs/wspcfg/wspcfg.log，级别
       loglevel.sh component=wspcfg logger=* level=debug；Logzipper 含两类日志。
  verification: |
    六类自动对象与手工两项齐备；手机 App 登录成功；部署细节以 TC2341（OTC smartphone VoIP Deployment Guide）
    为准（p147 Appendix）。
  conditions: 自动值因设备而异（例中 Mobile_83262 为系统分配的设备标识）。
  tags: [lab, smartphone, verification, entity, cos, kamailio]

- id: c12
  title: Extended Mobility——QR 码生成/NFC 写标签与切换、路由修改测试
  type: lab
  source_pages: p163-167
  source_chapter: Extended Mobility (How-To)
  source_quote: |
    "The syntax must be: {\"v\":\"1\",\"DI\":{\"DiD\":{\"User\":\"xxxxx\"}}} 'User' refers to the device
    directory number • Example: {\"v\":\"1\",\"DI\":{\"DiD\":{\"User\":\"31000\"}}}" (p164)
    "Test 1: Betty Boop (31002) calls Billy Backman (31001). Answer the call by using the OTC Smartphone
    device. By using OTC Mobile application, flash the QR code in order to switch the established call to
    Brad Barkley Deskphone (device=31000) Method: 'Call Transfer' / 'Scan QR code'" (p165)
    "Warning THE NFC FACILITY IS NOT AVAILABLE FOR IPHONE" (p166)
  steps: |
    1. 前提：学员自带智能手机；教室 Wi-Fi 热点（6 SSID，实验口径）；OTC Mobile 已安装；复用 c10 建的
       Backman OTC Smartphone 设备。
    2. QR：用在线生成器（例 https://www.the-qrcode-generator.com/）按语法
       {\"v\":\"1\",\"DI\":{\"DiD\":{\"User\":\"31000\"}}} 生成并打印/投屏。
    3. NFC：Google 市场装 "ALE NFC Extended Mobility" 应用 → Set NFC tag Parameters → OpenTouch Deskphone
       页签：Directory Number=31000、Device Number=31000 写入标签（Warning：NFC 不支持 iPhone；OmniPCX
       Deskphone 页签用于纯 OXE 无 OT 场景）。
    4. 测试 1（呼叫切换）：Boop（31002）呼叫 Backman（31001），用 OTC Smartphone 接听 → OTC Mobile 中
       Call Transfer/Scan QR code（或碰 NFC）→ 呼叫切到 Barkley 话机 31000（用户需拿起话机）。
    5. 测试 2（路由修改）：Backman 空闲 → 从 Routing Profile 菜单扫同一 QR/碰 NFC → 当前路由档案被改写，
       "other number" 目的地 = 31000。
  verification: |
    测试 1 话机侧通话延续、手机侧释放；测试 2 档案含 other number=31000；一小时周期提醒弹窗按 Yes/No/Later
    行为（p154）；再扫一次可 toggle 取消。
  conditions: 切换不可回切（自动场景=二通呼叫+转移）。
  tags: [lab, extended-mobility, qr, nfc]

- id: c13
  title: UM (Exchange)——特权账号、邮箱、Impersonation、CA 证书、邮件服务器与 UM 系统声明
  type: lab
  source_pages: p182-198
  source_chapter: Unified Messaging (Exchange server based) — "1 Eco-system configuration / 2 UM declaration"
  source_quote: |
    "Create 'ICEaccess' user in the Active Directory Login: ICEaccess Password: iceaccess ... Password never
    expires Tick this parameter" (p184-185)
    "New-ManagementRoleAssignment –Name 'Service Account Impersonation' –Role ApplicationImpersonation –User
    'ICEaccess@company.com'" (p190)
    "System services/Security/Certificate 'Server CTL' tab Click on 'Add' button" (p195)
    "Eco system/ IT server 'Right-click' then 'Create' and 'Mail Server' ... Protocol Select 'Exchange Web
    services' ... Location Select 'on-premises'" (p196)
    "System services/ Topology/ VMS ... select 'create' and choose 'UM voicemail system'" (p197)
  steps: |
    1. AD 建 ICEaccess 账号（登录 ICEaccess/密码 iceaccess，实验口径；勾密码永不过期）。
    2. Exchange 建（确认）其邮箱：Exchange Administrative Center（company\\administrator/superuser）→
       Recipient/Mailboxes → + → User Mailbox → 别名 ICEaccess → Existing users 选 ICEaccess → Save。
    3. 授权（R2.3+ 用 impersonation）：EMS 执行 New-ManagementRoleAssignment –Name "Service Account
       Impersonation" –Role ApplicationImpersonation –User "ICEaccess@company.com"；验证
       Get-ManagementRoleAssignment …（R2.2 前用 delegation：对每个 UM 邮箱配 Send as/Full Access/Send on
       behalf 三参数，见 n 系列）。参考 TC2391。
    4. CA 证书入信任库：https://eco.company.com/certsrv → Download a CA certificate（Base 64）→ OT
       WebAdmin System services/Security/Certificate → Server CTL 页签 → Add → 选择根 CA 证书 → Import。
    5. 声明邮件服务器：Eco system/IT server → Create → Mail Server：Name=mail、FQDN=eco.company.com、
       Protocol=EWS、Port=443、EWS login=ICEaccess@company.com（或 DOMAIN\\login）、Password、Location=
       on-premises；勾 Activate calendar presence service 与 Activate conference synchronization service。
    6. 建 UM 语音邮件系统：System services/Topology/VMS → 右键 create → UM voicemail system：Display name
       =UM、Type=UM（自动）、Mail server=mail。
    7. 语音邮件目录号（提醒）：OT 侧 TUI application 建/确认 31200（type=voice mail、user population=OXE
       CS）；OXE 侧 Applications/External Voice Mail → Create：Voice Mail Dir.No=31200、Sub type=Private、
       Directory name=VM_OXE、External gateway=2、Subscription on registration 勾选。
  verification: |
    Exchange 侧 Get-ManagementRoleAssignment 显示 RoleAssignee=ICEaccess、Role=ApplicationImpersonation；
    OT 侧 CA 证书出现在 Server CTL 列表；UM 系统与 mail 服务器关联成功。
  conditions: 版本分界：>2.2.x impersonation / <2.2.x delegation（配置位置不同）。
  tags: [lab, um, exchange, impersonation, certificate]

- id: c14
  title: UM——语音邮箱档案、信箱分配、OXE 话机留言键、用户级应用与维护、云上下文
  type: lab
  source_pages: p199-217
  source_chapter: UM How-To — "3 Voice mail profiles / 4 Voice Mailbox assignment / 5 at user level / 6 maintenance / 7 appendix cloud"
  source_quote: |
    "four VM profiles are available by default: 1 for 'UM' voice mail: standard • 3 for 'Local Storage':
    simplified, classic, advanced" (p199)
    "Warning SYNCHRONIZATION IS REQUIRED TO RETRIEVE THE TEMPLATES FROM THE OPENTOUCH SERVER." (p201)
    "Users and devices/Voicemail box Do a 'right click' then 'create' and choose 'UM voicemail box'" (p204)
    "TO BE ABLE TO CHANGE YOUR GREETING (EXTENDED ABSENCE, PERSONAL, ALTERNATIVE…), YOU FIRST MUST RECORD
    THEM THROUGH YOUR PHONE SET." (p211)
    "Daemons involved in 'Unified Messaging' to deal with MS Exchange are the following: MASC ... Wireal ...
    service 'name' restart where 'name' can be: mascd • wireald" (p215)
  steps: |
    1. 核对 UM 档案：System services/Applications/Messaging/Voicemail profile → UM 档案 configuration1/
       configuration2 页签（Answer only、Direct callback、Attendant call enabled、Keep copy in sent items、
       三时长等，见 principle p32）。
    2. 同步：改/建档案后必须同步（从 OT 或 OXE 节点，Complete/Partial × Separate/Global 四种组合）。
    3. 信箱分配（方式一，建用户时）：Users 应用 → Common attributes + OT attributes（Voice mail server=UM、
       VM profile name=模板）。
    4. 信箱分配（方式二，建后）：Users and devices/Voicemail box → create → UM voicemail box（General：
       Display name/Type=UM/Voice mail system=UM；Greetings：标准/个人/替代〔最多 2 个替代且需授权〕；
       Configuration：Addressing by name、Automatic reading、Delete confirm、Fax number、Voice mail profile）；
       再到 User 处确认 voice mail 许可并把信箱关联到用户。
    5. OXE 话机留言键：经 OXE Profile（Users/create，Set function=Profile，VoiceMail 页签填留言号/类型，
       Profile 名大写）或直接在用户参数填 Voice Mail Dir.N°（type external 自动）。
    6. 用户级验证：My Profile（https://OT FQDN；问候语必须先用话机录过才出现在页面）与 My Messaging
       （https://OT FQDN/MyMessaging）听/转留言；Outlook 2013 配置账户（服务器=邮件服务器 IP 192.168.1.100、
       用户 barkley、密码 1234，实验口径）收听语音邮件。
    7. 维护：UM 相关守护进程 MASC（mascd）与 Wireal（wireald），异常时 service … restart；日志
       logs/masc、logs/wireal。
    8. （云上下文）HTTP proxy：Eco system/IT server → Create → HTTP proxy（FQDN/端口/类型 HTTP/认证 Basic
       或 Digest）；Exchange cloud：Mail Server 的 FQDN=outlook.office365.com、Location=cloud、填 Exchange
       通知服务公共 URL（防火墙按 /ExchangeNotificationService 放行）、选 HTTP proxy。
  verification: |
    给 Alban/Barkley 留言后 My Messaging 与 Outlook 均可见；留言键直达邮箱。
  conditions: 问候语录入渠道限制（Warning p211）；本地存储邮箱的日历特性走 TC2558（Warning p395）。
  tags: [lab, um, voicemail, outlook, o365]

- id: c15
  title: 目录搜索——内部/电话簿同步、AD 目录、可选属性、SBC 合并、UDAS 维护、话机应用与 LDAP 溢出
  type: lab
  source_pages: p243-263
  source_chapter: Directory search (How-To)
  source_quote: |
    "System services/ Applications/ Telephony / Search/ Directory/ InternalDir ... Activation Tick the Check
    box ... Tips Synchronization Date, Time and period MUST BE SET. Synchronization period >= 1 (NEVER SET
    period to 0)" (p243-244)
    "Eco system/ IT Server ... select 'create' and choose 'LDAP Server' ... FQDN: eco.company.com Port: 389" (p246)
    "System services/ Applications/ Telephony / Search/ Merge/ Merge ... Merge activation Check the box" (p252)
    "Applications / LDAP Phone Books Create ... LDAP phone book Enter the phone book index (from 1 to 5)" (p260)
  steps: |
    1. 内部目录：…/Telephony/Search/Directory/InternalDir：General 勾 Activation；Synchronization 页签设
       date/time/period（period≥1）；Status 页签查上次同步；phonebookDir 同法（General 另有 Call Server
       字段）。
    2. 外部 LDAP 服务器：Eco system/IT Server → create → LDAP Server：Display name=Active Directory、
       FQDN=eco.company.com、Port=389、Search delay（ms）。
    3. 新建目录（AD）：…/Telephony settings/Search/Directory → create → LDAP directory：General（Name=AD、
       Activation 勾、LDAP server=Active_directory、Root=cn=users,dc=company,dc=com）；Synchronization（今天/
       时间/period 1）；Access（login=directory@company.com、password=directory，实验口径）；Field names
       （givenName/sn/mail/telephoneNumber）；Force synchronization；可用 LDAP 浏览器核实真实属性名。
    4. 可选属性：…/Search/Contact attribute → Photo：Displayable 勾、Attribute compatibility 选 Attribute
       1..5 之一；再到 AD 目录 Attributes 页签 "+" 映射 Contact attribute=Photo ↔ LDAP attribute name；
       （searchable 仅部分属性可用，photo 不可；可选属性搜索非所有客户端支持）。
    5. SBC 合并：…/Search/Merge/Merge：Merge activation 勾、Merge date/time/period（period≠0）、browse 选择
       目录定 Synchronization Order（AD 最高、内部目录最低，实验要求）、Force directories merge 手动合并；
       各目录 Merge keys 页签：Last/First Name 必选 + 可选 Phone number，配可去前缀/后缀/取前 n 字符（实验例：
       3 键各取 12 字符、first name 去 "_DECT" 后缀）；Status 页签查合并结果。
    6. UDAS 维护：重启 UDAS（必要时 chameleond restart）；chameleon 日志 logs/chameleon/chameleon
       （chameleon.log/.logX）、udas 日志 logs/udas 与 udas-traces.log；照片目录 /var/data/slides/d.DEFAULT/
       （缺失则手动同步 LDAP）。
    7. 话机 Home 页：Network/OXE CS/你的 OXE → PRS 选 "Presentation server - opentouch"（必要时重启 prs、
       tomcat）。
    8. Communicate by name：System services/Applications/IP Touch application → Create：Identifier=MY_C、
       （可选 HTTP proxy）；Application 页签 index=7、Registration URL parameter=action=RegisterDirKey、
       URL registration=http://opentouch.company.com/eccnoe/myphone——让 80x8 键盘找人也走 UDAS。
    9. OXE LDAP 溢出：Applications/LDAP Phone Books → Create（索引 1-5：server 151.1.1.100、port 389、
       user cn=directory,cn=users,dc=company,dc=com、password=directory、base=cn=users,…）；Entity → 挂
       Overflow LDAP phone book 索引；System/Other system parameters → Phone book overflow on LDAP server
       勾选（系统级放行）。
    10. （附录）8770 目录：LDAP_8770（nms.company.com:389）+ 目录 LDAP_omnivista（root
        o=Company,o=directoryRoot，登录 uid=AdminNmc…/adminnmc 或 cn=directory manager/superuser，实验口径）。
  verification: |
    OTC PC/话机搜索可见 AD 联系人与照片；同名联系人合并为单名片；OXE 用户按名找不到时自动/手动溢出 LDAP。
  conditions: 同步参数三处"必填、period≥1/≠0"为硬规则；merge keys 需在每个参与目录配置。
  tags: [lab, udas, ldap, sbc, directory]

- id: c16
  title: 会议服务器设置——桥号（OXE External VM + OT TUI）、系统选项、SIP 代理、DAS、格式规则
  type: lab
  source_pages: p308-320
  source_chapter: Conference server Settings Configuration (How-To)
  source_quote: |
    "Application/External Voice Mail Right click ... Voice Mail Dir. Number ... Directory Name (i.e. Conf-EN)
    ... External Gateway number Enter the SIP external gateway ID, used to access to the SIP Server (e.g. '1')" (p309)
    "System services /Applications /Telephony settings /Vocal applications / TUI application Look for
    'Conferencing' item to modify the default one. ... Number 31250" (p311)
    "International Dialing Prefix: 00 • National Dialing Prefix: 0 • Country Code: 33 • Smart mail relay
    host: eco.company.com • Default web client: OTCWeb" (p314)
    "Configuration / SIP Proxies ... Default Outbound SIP Proxy 192.168.1.50 ... Port 5260" (p316)
  steps: |
    1. OXE 桥号：Applications/External Voice Mail → Create ×2：31250（Conf-EN，External Gateway=1）、31260
       （Conf-FR，同网关）——分别服务英/法语引导。
    2. OT TUI：System services/Applications/Telephony settings/Vocal applications/TUI application → 默认
       "Conferencing" 条目改为 31250（Type=Conferencing、organization=DEFAULT、Language=EN、Include in
       e-mail invitations、Label；可选 Dial in number=外部 DDI）；再 Create 新 TUI 条目 31260（FR）。
    3. 进入会议服务器管理台：8770 Configuration → OpenTouch 节点右键 WBM（otAdmin/admin8770，实验口径）→
       Users and devices/Conference server。
    4. 系统选项：Configuration/System Options：国际 00、国内 0、国家码 33、Smart mail relay host=
       eco.company.com、Default web client=OTCWeb。
    5. SIP 代理：Configuration/SIP Proxies：Outbound 默认 = OT IP:5260；Inbound Realm=opentouch.company.com、
       Server=OT IP、Port=5260；Users 自动出现 31250/31260（装后向导已自动填，仅需核对；UDP 代理用于对接
       SIP 网关/PBX/外部代理）。
    6. DAS 规则：Configuration/Advanced settings/Edit DAS rules → Default 域录入法国 10 条（同 p108/c08）。
    7. 电话格式规则：Advanced settings/Phone Formatting Rules：Extension Pattern =
       /^\\s*\\+*[xX]?(\\d{3,5})\\s*$/（按 5 位分机计划；分机位数不同改第二个数字）。
  verification: |
    SIP Proxies 设置完整（向导自动+人工核对）；邀请邮件含桥号/URL/访问码；拨号格式按 DAS 正确变换。
  conditions: 桥号两端（OXE/OT）必须一致；每语言一号。
  tags: [lab, conference, tui, sip-proxy, das]

- id: c17
  title: 数据会议运用——OTC PC 预约、Outlook 免预约、One Touch、远程控制、协作限制
  type: lab
  source_pages: p338-362
  source_chapter: Data conferencing features (How-To)
  source_quote: |
    "Grant 'Desktop' and 'conferencing' rights to all users via the OmniVista 8770 ... Licenses tab Desktop
    Enabled Conferencing Enabled" (p340)
    "Click on the icon to schedule a conference ... Meeting name / Meeting type / Start date / Duration /
    Time zone / Recurrence pattern" (p341-342)
    "Warning IF EVER THE 'INCLUDE CONFERENCE' ICON IS NOT AVAILABLE IN OUTLOOK CLIENT, MAKE SURE THAT THE
    CONFERENCE ADD-IN IS ACTIVE IN OUTLOOK." (p349)
    "Users and devices / user ... Enable collaboration Checked Enable sharing Checked" (p359)
  steps: |
    1. 前提：Users and Devices/User → Licenses：Desktop 与 Conferencing 启用。
    2. OTC PC 预约会议（Barkley 登录）：Schedule a conference → Settings（名称/类型 scheduled 或
       reservationless/开始/时长/时区/周期）；Options（Leader starts meeting 等）；Password（音频/在线/两者，
       ≥5 位/字符）；People（从联系人或邮箱加 Alban、Boop，定领导者/参与者）；Documents（Add：pdf/图片直接
       作演示，Office 需 DCS；presentation 不可下载、attachment 可）；Schedule 后 Details 页签给出入会 URL/
       桥号/SIP URI/访问码，邮件+日历邀请自动发送。
    3. 入会：OTC PC 点 "Join the meeting"（PC 接听）或 "call me at"（回呼指定设备）；OTC Web 点邮件 URL →
       填姓名/头像/回呼号/领导者码 → Join。
    4. Outlook 免预约会议：OTC PC 装好后 Outlook 自动出现 Include Conference 图标（File/Options/Add-ins 确认
       Conference Scheduling Add-in 激活）；Include Conference → Use OpenTouch Conversation settings（GUI
       密码）→ Show details 逐页配：Date Time and Invitations（Leader/Participant site URL）、Audio
       Conference（lecture mode/录制名/自动录制/billing codes）、Web Conference（webinar mode）、Passwords、
       Joining the conference（toll-free 回呼/按键确认/首个加入即呼我/邮件与短信告警）、Invited Participants。
    5. One Touch：System services/Applications/Vocal applications/TUI application → 会议号加 Dial in number
       （+33210141250，规范格式）、Include in e-mail invitations、Label 以 <*> 开头（如 <*External access with
       english prompts>）、Toll-free 勾选；验证邀请邮件出现一键入会信息。
    6. 远程控制：确认双方 Enable collaboration + Enable sharing → OTC PC 桌面共享启动后 Give control → 点
       用户名移交；Take back control 收回。
    7. 协作限制实验：Users and devices/User → 对 Connection 用户 Barkley 分别关 Enable sharing、再关
       Enable collaboration → 每次做 ad-hoc 会议/点对点会话观察可用动作变化（scheduled 会议不受影响）。
  verification: |
    邀请送达（邮件+日历）；三种客户端入会成功；受限用户按 p291-292 矩阵失去对应功能。
  conditions: 密码不出现在邀请邮件；回呼确认提示语为 "Welcome to the My Teamwork conference center…"。
  tags: [lab, conference, outlook, one-touch, collaboration]

- id: c18
  title: DCS-V——Windows 虚机预配置、DCS 组件安装、OT 侧声明、上传测试
  type: lab
  source_pages: p374-383
  source_chapter: DCS installation on a virtual machine – DCS-V (How-To)
  source_quote: |
    "Warning Activate Licenses keys for Windows and Office ... Warning Failure to perform these updates will
    result in documents that remain in the queued state and do not get converted." (p375)
    "Start/ Run/ regedit.exe HKEY_LOCAL_MACHINE/ SOFTWARE/ Microsoft/ Windows NT/ CurrentVersion/ Winlogon ...
    AutoAdminLogon 1 ... Warning REBOOT WINDOWS VIRTUAL MACHINE" (p379)
    "Mount for example the 'DCS' iso file as CD-Rom and copy its content ... dcs_install.bat •
    dcs_vmware-6.zip • unzip.exe" (p380)
    "Configuration / Advanced Settings ... Configure Access to a Remote Document Conversion VM • Remote DC
    Address Windows machine IP address" (p382)
  steps: |
    1. 前提：Windows（物理/虚拟）机已装 Office；激活 Windows 与 Office 双许可；按微软流程打齐强制更新
       （否则文档卡 queued 不转换）；登录账号 Administrator/superuser（实验口径）。
    2. 预配置：①关闭专用/公用防火墙；②UAC=从不通知（搜索 uac）；③账号勾密码永不过期；④注册表 Winlogon 四
       键（AutoAdminLogon=1、DefaultDomainName、DefaultUserName、新建 DefaultPassword）→ 重启虚机。
    3. 装 DCS：挂 DCS ISO，拷 dcs_install.bat、dcs_vmware-6.zip、unzip.exe 到 C:\\temp，执行 dcs_install.bat；
       完成后重启并验证 Administrator 自动登录、DCS 两个窗口自启。
    4. OT 侧声明：8770 → OpenTouch 节点 WBM（otAdmin/admin8770）→ Users and devices/Conference server →
       Configuration → Advanced Settings → Configure Access to a Remote Document Conversion VM：Remote DC
       Address=Windows 机 IP、Remote DC user name、Remote DC User Domain、Remote DC user password（DCS 软件
       由 OT 自动推送更新，无需手工）。
    5. 测试：OTC PC 建会议并上传 Office 文档（PowerPoint/Excel/Word）为 presentation，确认能上传演示。
  verification: |
    Office 文档可作 presentation 上传并展示（p383 "Make sure that it is possible to upload a MS Office
    document as a presentation"）。
  conditions: 外部 DCS VM 需 Hyperthreaded Core Sharing=None（p373）；兼容矩阵见 principle p35。
  tags: [lab, dcs, windows, conference]

- id: c19
  title: Calendar presence 与 Calendar synchronization 实施（UM 上下文）
  type: lab
  source_pages: p394-399
  source_chapter: Calendar synchronization and calendar presence (How-To)
  source_quote: |
    "Warning THE FOLLOWING PROCEDURE HAS TO BE USED ONLY IF YOU WANT TO BRING INTO SERVICE THE CALENDAR
    SYNCHRONIZATION AND THE CALENDAR PRESENCE FEATURES WITH A UNIFIED MESSAGING CONTEXT. IF USERS HAVE LOCAL
    STORAGE MAILBOXES, PLEASE HAVE A LOOK TO THE TECHNICAL DOCUMENTATION 'TC 2558'" (p395)
    "the management prerequisites are the same as for the 'Unified Messaging' configuration" (p395)
    "Schedule an appointment in the Outlook calendar of Alban (i.e. today, beginning at 15:30) ... Check that
    his calendar presence is displayed on the OTC PC client of Barkley" (p397)
  steps: |
    1. 前提（同 UM）：ICEaccess 特权账号 + Exchange 邮箱 + Impersonation + Exchange CA 证书入 OT 信任库 +
       邮件服务器已声明（c13/c14）。本地存储邮箱场景改查 TC2558（Warning）。
    2. 核对邮件服务器两开关：Eco system/IT server → Mail Server：Activate calendar presence service 与
       Activate conference synchronization service 均勾选（TC2258 3.4：改后 service wireald restart）。
    3. 测试在场：在 Alban 的 Outlook 日历建今天 15:30 开始的约会 → Barkley 的 OTC PC 上查看 Alban 的日历
       在场文本（如 Busy – In a meeting until…）。
    4. 测试同步：在 Barkley 的 Outlook 日历（或 OTC 客户端）建今天 16:00-19:00 的会议 → 核对 Outlook 与
       OTC 客户端两侧会议列表自动同步。
  verification: |
    Alban 约会状态出现在 Barkley 的 OTC PC（p397-399 结果截图）；OTC 建的会议出现在 Outlook、反之亦然。
  conditions: 限制：OTC 创建的周期会议不推送到 Exchange（p392）；Outlook 侧可经 Free/Busy Read 权限控制是否
  发布自己的在场（TC2258 3.5/3.6）。
  tags: [lab, calendar, presence, sync]

- id: c20
  title: 外部认证——LDAP 配置（External login、浏览器 cookie、plugin_ldap.properties、Authentication.xml）
  type: lab
  source_pages: p437-442
  source_chapter: External authentication: LDAP authentication (How-To)
  source_quote: |
    "/Users and Devices/ Users ... External login Enter the user external login. It must match with user
    unique ID managed on the LDAP server" (p438)
    "Warning TO HAVE A HOMOGENEOUS AUTHENTICATION MANAGEMENT, IT IS ADVISED TO ALSO DECLARE THE 'EXTERNAL
    LOGIN' PARAMETER FOR ADMINISTRATOR ACCOUNT" (p438)
    "server.primary.name=192.168.1.100 ... server.basedn=cn=users,dc=company,dc=com ...
    user.login.attribute=sAMAccountName ... user.uid.attribute=sAMAccountName" (p440-441)
    "service tomcatd stop. ... service tomcatd start." (p441)
  steps: |
    1. External login：8770 → Users and Devices/Users → 每个用户 General 页签填 External login（例 Barkley
       → barkley，须与 LDAP 唯一 ID 一致）；管理员账号（如 OTADMIN）同样配置（Warning）。
    2. 浏览器会话 cookie：Chrome/Edge——控制面板/Internet 选项/隐私/高级：勾"覆盖自动 cookie 处理"与"始终
       允许会话 cookie"；Firefox——Privacy/History 选自定义。
    3. 备份：/opt/Alcatel-Lucent 下 authentication.xml 与 plugin_ldap.properties 拷到桌面备份文件夹。
    4. 填 plugin_ldap.properties：protocol=ldap（或 ldaps）、primary/secondary=192.168.1.100、port=389、
       basedn=cn=users,dc=company,dc=com、appli.login=cn=directory,cn=users,…、appli.pwd=directory、
       user.login.attribute=sAMAccountName、user.uid.attribute=sAMAccountName（实验口径）。
    5. 启用：编辑 /opt/Alcatel-Lucent/authentication.xml，删除 LDAP 插件段落的注释符；service tomcatd
       stop/start。
    6. 回退：还原两个原始文件并重启 tomcat。
  verification: |
    用户以 LDAP 账密登录 OTC/Web 应用成功；Web 客户端失败时可级联 DTA、厚客户端不可（验证级联行为差异）。
  conditions: 会话 cookie 必须启用（Kerberos/LDAP 认证依赖）；多插件时 Authentication.xml 内顺序即尝试顺序。
  tags: [lab, authentication, ldap]

- id: c21
  title: Kerberos SSO——浏览器、web.xml 模板、krb5/auth.config/keytab、AD 账号与 SPN、WBM 管理员
  type: lab
  source_pages: p443-455
  source_chapter: Single Sign On Authentication through Kerberos (How-To)
  source_quote: |
    "Rename the file 'web.xml' ... into 'web.xml.default' ... Rename the file 'web.xml.kerberos' ... into
    'web.xml'" (p445)
    "'ktutil' ... 'addent –password –p ice_kerb@company.com –k 0 –e rc4-hmac' ... 'wkt /opt/Alcatel-Lucent/
    platform/tomcat/conf/ice_kerb.keytab'" (p448)
    "Warning THE PASSWORD, PREVIOUSLY DEFINED, MUST BE THE ONE STORED IN THE 'ICE_KERB.KEYTAB' FILE." (p450)
    "'setspn –A HTTP/opentouch ice_kerb' then press 'Enter' • 'setspn –A HTTP/opentouch.company.com ice_kerb'" (p451)
  steps: |
    1. 浏览器静默登录：Chrome/Edge——Internet 选项>高级>启用集成 Windows 认证；安全>本地 Intranet>自定义
       级别>"只在 Intranet 区域自动登录"；站点>高级加入 OT FQDN。Firefox——about:config 改
       network.negociate-auth.delegation-uris 与 trusted-uris 加入 OT FQDN、network.auth.use-sspi=true。
    2. web.xml：thin（/opt/Alcatel-Lucent/infra_webapps/authenticationform/authenticationform/WEB-INF）与
       thick（…/authenticationbasic/…）两处——web.xml 改名 web.xml.default、web.xml.kerberos 改名 web.xml
       （root 终端；停用反向改名）。
    3. krb5.conf：从 …/kerberos_conf 拷到 /opt/Alcatel-Lucent/platform/tomcat/conf，改域名/realm/KDC。
    4. auth.config：从 …/kerberos_conf 拷到 /var/data/ics-group/tomcat（覆盖），核对 KeyTab 路径与 principal。
    5. keytab：ktutil → addent –password –p ice_kerb@company.com –k 0 –e rc4-hmac（密码=AD 账号密码，实验
       1234）→ wkt /opt/Alcatel-Lucent/platform/tomcat/conf/ice_kerb.keytab → quit。
    6. AD 账号：域控上建 ice_kerb（密码 1234、用户不能改密、永不过期；Warning：密码必须与 keytab 一致）。
    7. SPN：域控 PowerShell 执行 setspn –A HTTP/opentouch ice_kerb 与 setspn –A HTTP/opentouch.company.com
       ice_kerb。
    8. 重启：service tomcatd restart。
    9. WBM 管理员：AD 建 wbm_admin；OT System Services/Security/Administrator → Create：Login（唯一）、
       External login=wbm_admin（唯一且对应 AD 名，不能同时给标准用户）、Application=WBM、Delegate
       authentication 勾选、Passwords 页签 GUI 密码必填（Kerberos 下不用）。
    10. 验证：加域机器登录 wbm_admin → 开 https://<OT>/WebAdmin 免密直达；OTC PC/My Profile 同样免密。
    11. 停用：web.xml 改名回退（kerberos/default 对调）+ 重启 tomcat。
  verification: |
    WBM 与 OTC PC 均免密进入（p454 "WBM does not query any authentication and opens on default page"）。
  conditions: Kerberos 只覆盖 Windows 上的 Web 应用与 OTC PC；移动端仍提示输账密；不支持经反向代理。
  tags: [lab, kerberos, sso, spn, wbm]

- id: c22
  title: RADIUS 认证 + FreeRADIUS 实验服务器搭建
  type: lab
  source_pages: p456-467
  source_chapter: External authentication: RADIUS authentication (How-To) & FreeRADIUS server installation (How-To)
  source_quote: |
    "server.primary.name=192.168.1.10 (client PC) ... server.primary.port.authentication=1812 ...
    server.shared_secret=training • server.authenticator=pap" (p459-460)
    "External login Enter the user external login. It must match with user 'Radius login' managed in the
    database of the external Radius server" (p457)
    "double-click on the 'freeRADIUS.net-1.0.5-r0.0.5.exe' file ... copy the 'clients.conf', 'radiusd.conf'
    and 'users' files and paste them into the folder: 'C:\\Program Files (x86)\\ FreeRADIUS.net-1.0.5-r0.0.5\\
    etc\\raddb'" (p463, p466)
  steps: |
    1. External login：Users → 每用户填 External login（=RADIUS 库中的 Radius login，例 barkley）；管理员同
       法（同 LDAP 章 Warning 口径）。
    2. 浏览器会话 cookie：同 c20 第 2 步。
    3. 备份 /opt/Alcatel-Lucent 下 authentication.xml 与 plugin_radius.properties。
    4. 填 plugin_radius.properties：primary/secondary=192.168.1.10（客户端 PC，实验口径）、认证端口 1812、
       计费端口 1813（OT 未用）、shared_secret=training、authenticator=pap、connection.timeout=10（默认
       15）、connection.retries=5（默认 2）。
    5. 启用：Authentication.xml 删除 Radius 插件注释符；service tomcatd stop/start。
    6. （实验服务器）客户端 PC：解压 freeradius_opentouch_training_files.zip 到 C:\\Windows\\Temp → 安装
       freeRADIUS.net-1.0.5-r0.0.5.exe（向导默认值装完）→ 把 clients.conf、radiusd.conf（UDP 端口 1812）、
       users（定义认证用户）三文件拷入 C:\\Program Files (x86)\\FreeRADIUS.net-1.0.5-r0.0.5\\etc\\raddb。
    7. 应用改动：任务管理器结束 radius.exe 进程 → Start/Programs/FreeRADIUS.net/Start FreeRADIUS.net。
  verification: |
    OT 用户以 RADIUS 账密登录成功；主服务器无响应时切备服务器（超时 10s、重试 5 次，实验值）。
  conditions: clients.conf 定义 OT 服务器与共享密钥（training，实验口径）；该章 Notes 原文误写为 LDAP 参数
  说明（原书复制粘贴笔误）。
  tags: [lab, radius, freeradius, authentication]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 24 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 实验 POD 搭建核对 | 有 → c01 |
| task-02 ITSP1 模拟器联调 | 有 → c01 步骤 5-7（模拟器侧机制见 framework f03，模拟器本身无独立实验章） |
| task-03 Nomadic 蜂窝模式 | 有 → c02 |
| task-04 Nomadic VoIP 模式 | 有 → c03 |
| task-05 Nomadic 资源维护 | 有 → c04 |
| task-06 Desksharing 配置 | 有 → c05 |
| task-07 Desksharing OTC PC 与维护 | 有 → c06 |
| task-08 反向代理与 OTSBC 声明 | 有 → c07 |
| task-09 DAS/ACS FQDN/证书 | 有 → c08 |
| task-10 OXE 通用参数 | 有 → c09（步骤 1-7） |
| task-11 iPhone+ SBC/OT 系统参数 | 有 → c09（步骤 8-9） |
| task-12 设备档案与用户 | 有 → c10 |
| task-13 核验与手工补充/安装/维护 | 有 → c11 |
| task-14 Extended Mobility | 有 → c12 |
| task-15 UM (Exchange) 部署 | 有 → c13、c14 |
| task-16 邮箱权限/云上下文/UM 维护 | 有 → c13（步骤 3）/c14（步骤 7-8，含 delegation 与 O365） |
| task-17 目录搜索部署 | 有 → c15（步骤 1-4） |
| task-18 SBC 合并与 UDAS 维护 | 有 → c15（步骤 5-10） |
| task-19 会议服务器配置 | 有 → c16 |
| task-20 数据会议运用与协作限制 | 有 → c17 |
| task-21 DCS 安装声明 | 有 → c18 |
| task-22 日历在场/同步 | 有 → c19 |
| task-23 LDAP/RADIUS 认证 | 有 → c20、c22 |
| task-24 Kerberos SSO | 有 → c21 |

**统计**：22 条（全部 lab 型，按 How-To 章拆并）；24 项任务全部有案例类条目覆盖。两点说明：
1. task-02 的模拟器机制页（p19-23）无独立 How-To，其验证动作并入 c01 外呼验证步骤；号码规则已由 principle p07 承载。
2. 原书 Extended Mobility、Conference settings 等章的 verification 以行为测试问题呈现（如 QR 切换测试、上传 Office 演示），已逐条保留在对应条目的 verification 字段。
