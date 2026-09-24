# 案例/实验/操作序列候选 — OmniPCX Enterprise SIP (ENTPXTE403EN R101.1 MD4 Ed12)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号、POD 号）标注"实验口径"。
> 条目说明: 全书 14 个 How-To 实验章 → 14 条一一对应（POD preparation、OXE domain、SIP Users、证书 PKI、ALE-2/3、ALE-x00、ALES PC、ALES Android、Codecs、SIP traces、SBC 接入、OTSBC 部署、OTSBC 反代、ALES Remote Worker）。

```yaml
- id: c01
  title: POD 准备——预配置核对、IPDSP 开通与公网接入参数
  type: lab
  source_pages: p35-42
  source_chapter: POD preparation — "Configure the OXE for the next labs"
  source_quote: |
    "OXE VMs used for this training are already configured (Database and Linux Data), such as:
    Software licenses are restored, SSH is enabled (mandatory since OXE Release N3)" (p38)；
    "According to your POD number, configure 2 parameters in your external SIP gateway: Registration
    ID: pbxN ... Outgoing username= pbxN" (p41)；
    "First external number 33210N41000 (where N is your POD Number) For POD 3: First external number=
    33210341000" (p41)
  steps: |
    1. 按实验模式启动虚机：全虚拟化启动清单实例；混合模式额外起课堂相关；Note：ENTP_SBC_SIP 虚机
       稍后启动，混合模式不需要 PC CLIENT 11（课堂有实物话机）（实验口径）。
    2. 核对 OXE 预配置：许可已恢复、SSH 已启用（N3 起强制）、内部防火墙部分配置（PC/OMS/GD4/NTP）、
       NTP=192.168.1.252、FlexLM=192.168.1.80 已声明、DHCP 开启（地址段 192.168.1.145-147，供
       31010/31011/31012）、机架板卡已建、用户已建、语音指南已下载、公共 SIP 中继组已建。
    3. 核对机架：全虚拟化——软件机架 3U(OMS) 机架 4、虚拟 GD4 槽 0 IP 192.168.1.13/24 MAC
       00:50:56:01:01:13；混合——硬件机架 1U 机架 2、GD4 槽 0 192.168.1.12/24（MAC 课堂核对）、
       MIX484 槽 1，另加软件机架同上。
    4. 核对用户表并开通 IPDSP：31000 Brad Barkley（PC Client 10）、31001 Billy Backman（PC Client
       11）；混合再加 31010 Charles Cooper ALE-500(IP NOE)、31011 Calixta Cartier ALE-300、31012
       Caitleen Connor ALE-20H（均动态地址）、31020 David Douglas ALE-30H(TDM/UA)。IPDSP 软件在
       NAS；右键 Settings → Network 填 TFTP Server Main = 192.168.1.3（OXE CS Main 地址，Node 1
       用户）。
    5. 公网接入——外部 SIP 网关：SIP/SIP Ext. Gateway 选中外部网关，Registration ID=pbxN（N=POD
       号，POD 3 即 pbx3），Outgoing username=pbxN。
    6. DID 翻译：Translator/External Numbering Plan/Default DID num. translator → create：First
       external number=33210N41000（POD 3=33210341000）、First internal number=31000、Range
       Size=500。
    7. 外呼验证：按《SIP Carrier Simulator》文档拨打公网号码确认公共 SIP 承载接入正常。
  verification: |
    书中验收：外呼打通（p42 "To make sure that access to public SIP carrier is working properly, set
    up some outgoing calls"）；后续实验均依赖此基线。
  conditions: OXE 基线镜像已按实验口径预配置；POD 号决定所有号码（N=单数字，PN=两位）。
  tags: [lab, pod-preparation, ipdsp, did, sip-gateway]

- id: c02
  title: OXE 域名定制——netadmin 19 菜单查改 + 管理工具只读核对
  type: lab
  source_pages: p61-63
  source_chapter: OXE domain — "Configure OXE domain"
  source_quote: |
    "!! IMPORTANT WARNING !! OXE is still having default domain name. Please configure a legitimate
    registered domain name, to prevent certificate errors." (p62)；
    "Option 19/1/2: Create/Update ... Enter OXE Domain to be configured (default is oxedomain.com) ?
    company.com" (p63)；
    "Warning TO MODIFY THESE PARAMETERS, NETADMIN MENU MUST BE USED." (p62)
  steps: |
    1. 查询（netadmin）：CS 上以 mtcl 登录 → 命令 netadmin -m → 若仍是默认域名先弹 IMPORTANT
       WARNING（防证书错误）→ 回车继续 → 选 19/1/1 'View'：显示 OXE DOMAIN=oxedomain.com、OXE
       FQDN=oxe.oxedomain.com（实验初始态）。
    2. 查询（管理工具）：mgr/WebAdmin → SIP/SIP Gateway → Edit/Consult：看 Machine name-Host（例
       OXE）与 DNS local domain name（默认 oxedomain.com）。
    3. 修改：netadmin -m → 19/1/2 'Create/Update' → 输入新域名 company.com（实验口径）→ 应用。
    4. 复核：再用 WebAdmin SIP/SIP Gateway → Edit/Consult，DNS local domain name 应变为
       company.com（也可用 netadmin 19/1/1 直接看）。
  verification: |
    WebAdmin/管理工具中 DNS local domain name 显示新域名 company.com（p63）；OXE FQDN = 节点名 +
    新域名（p170 口径）。
  conditions: mtcl 账号；修改只能经 netadmin（管理工具仅可查询）。
  tags: [lab, netadmin, domain, menu-path]

- id: c03
  title: SIP Device 用户开通全流程（31060 会议话机）与维护六命令
  type: lab
  source_pages: p84-94
  source_chapter: SIP Users — "Configure, deploy and maintain a SIP Device user"
  source_quote: |
    "Create a private SIP Trunk Group (e.g. #10) ... Trunk Group Type T2 ... T2 Specification SIP"
    (p85)；
    "Warning IN CASE OF MODIFICATION OF THE NUMBER OF VIRTUAL ACCESSES FOR SIP, A RESTART OF THE
    SYSTEM IT'S NECESSARY" (p86)；
    "Create the 'SIP device' user (31060) ... Set Type + SIP device SIP Passwd 12345" (p89)；
    "Verify that the SIP user is registered on the SIP Proxy ('sipregister' command). Verify the
    private SIP trunk group status ('trkstat' command)." (p90)
  steps: |
    1. 私网：Translator/Network Routing Table → Review/Modify：Network Number=10（选空闲号，勿用
       ABC/VPN 号），Protocol Type=ABC-F，Associated Ext SIP gateway=-1（本地网关用 -1）。
    2. 私有 SIP 中继组：Trunk Groups → Create：ID=10、Type=T2、Node number=1、Q931 signal
       variant=ABC-F、Number Compatible With=-1、Digits To Send=0、Remote Network=10、T2
       Specification=SIP。
    3. 虚拟接入：Trunk Groups/Trunk Groups/Virtual Accesses for SIP → Review/Modify：Trunk Group
       Id=10、Number of SIP Accesses=2（默认 2；成对分配；改后必须重启系统）。
    4. 本地 SIP 网关：SIP/SIP Gateway → Review/Modify：SIP Subnetwork=10、SIP Trunk Group=10、IP
       Address=192.168.1.3（角色地址）、Machine name-Host=oxe（自动生成不可改）、Proxy Port=5060、
       Subscribe Min/Max=1800/86400、Session Timer=1800/Min 900/Method+UPDATE、DNS local domain
       name=company.com、DNS Type=+DNS A、SIP DNS1=192.168.1.250、SDP in 18x=True、CAC
       SIP-SIP=False。
    5. SIP 代理（本实验用 Digest 认证）：SIP/SIP Proxy → Review/Modify：Minimal authentication
       method=SIP Digest、Authentication realm=OXE、Only authenticated incoming calls=True、
       Framework Period=3、Framework Nb Message By Period=50、Framework Quarantine Period=1800、
       TCP when long messages=True，其余默认（initial 500/T2 4000/TLS 30/递归 False/重传 3/降级
       TTL 1800/UA 标识 %）。
    6. SIP 注册器：SIP/SIP Registrar → Review/Modify：Min Expiration=1800、Max=86400。
    7. （选做，本实验不要求）SIP 字典：重名用户加 alias（DUPONT1/DUPONT2 例）；（选做）Quarantined/
       Trusted IP 地址。
    8. 转移优化前缀：Translator/Prefix Plan → Create：Number=A31999、Prefix Meaning=Local
       Features、Local Features=PCX address in DPNSS（免拨号前缀）。
    9. 建户：Users → Create：DN=31060、名 Conference Room、Shelf/Board/Equipment=255、Set
       Type=+SIP device、SIP Passwd=12345（实验口径）。Warning：SIP device 须在 CS 内部防火墙登记为
       信任主机（netadmin -m/Security；more /etc/hosts 核对）。
    10. 终端配置：MicroSIP 填用户 SIP 密码 12345（实验口径）并注册。
    11. 维护验证：sipregister（31060 应在注册库）、trkstat（中继组状态；SIP 中继不在服时可能要重启
        OXE）、sipgateway、sipdict -l、ps -edf | grep sipmotor。
  verification: |
    书中验收：sipregister 显示 31060 的 contact 行（p93）；31060 进出呼测试成功（p90）；trkstat 10
    显示 62 路 TS；sipdict -l 中 31060 type=2；自动隔离可在 /usr4/tmp/sipalarm.log 看 f003 告警
    （p94）。
  conditions: 每系统仅一个私有 SIP 中继组(ABC)；标准端口 5060 勿改。
  tags: [lab, sip-device, trunk-group, sip-gateway, sipregister]

- id: c04
  title: OXE DM 证书定制（内部 PKI）——自签根 CA + CS 证书 + CTL 核验
  type: lab
  source_pages: p168-171
  source_chapter: Customization of the certificate for OXE DM with the internal PKI
  source_quote: |
    "It is necessary to customize the OXE certificate from internal OXE PKI or external PKI: To
    update the CN and SAN fields with OXE's FQDN ... To generate the associated CTL file for SIP
    DeskPhones." (p169)；
    "netadmin -m ... 11 : Security 9 : PKI Management 1 : CS Certificates And choice 1 : Create/Update
    CS certificates (Auto generated)" (p169)；
    "Reboot the OXE at the end of the management." (p171)
  steps: |
    1. 终端切 root：登录 mtcl → su → 输 root 口令 → netadmin -m。
    2. 生成：11 Security → 9 PKI Management → 1 CS Certificates → 选 1 Create/Update CS
       certificates (Auto generated)。
    3. 逐项应答：CC-suite-ID（实验示例 11111-11111-11111-11111；许可文件含 CCsuite-ID 时留空自动
       取）；加通配 DNS *.company.com（默认 y）；SAN 写入物理与角色 IP（默认 y）；附加 SAN（默认
       n）；密钥长度（2048-4096，默认 4096，实验录 4096）；国家 FR/州 BRITTANY/城市 BREST/组织 ALE/
       部门 TRAINING（实验口径）→ 确认 y。
    4. 系统生成：Root CA → CS 私钥 → CS CSR → CA 签发 CS 证书（"Call Server Certificate
       successfully generated"）。
    5. 核验证书：netadmin（mtcl→su→root）→ 11/9/1 → 8 View：CA 证书 CN=CC-suite-ID、CS 证书
       CN=oxe.company.com、SAN=DNS:oxe.company.com, DNS:*.company.com, IP:192.168.1.3/1.1，有效期
       示例 2025-11-13 → 2045-11-08。
    6. 重启 OXE。
    7. 核验 CTL：cd /usr3/mao/DM/VHE8082/ → ll：应见 ctl_VHE8082 与 ict8000ctl.pem。
  verification: |
    书中验收：CS 证书 CN/SAN 正确（p170-171 输出）；CTL 文件存在（p171 ll 输出）。
  conditions: 安装默认证书只适配 WBM/HTTPS，不适配 SIP 客户端；外部 CA 亦可。
  tags: [lab, pki, certificate, ctl, netadmin]

- id: c05
  title: ALE-2/ALE-3 SIP 话机开通——DM 激活、DM profile、建户 31033、DHCP 与 auto-discovery
  type: lab
  source_pages: p172-186
  source_chapter: ALE-2/ALE-3 SIP Deskphone — "Bring into service ALE-2/ALE-3 SIP Deskphone"
  source_quote: |
    "Warning BE AWARE THAT DISABLING THE DM IN THE OMNIVISTA 8770 WILL CAUSE THE REMOVAL OF THE
    DEVICE CONFIGURATION FILES FROM THE 8770 SERVER ... A RESET FLASH WILL BE MANDATORY ON ALL
    DEVICES" (p174)；
    "ALE-2/ALE-3 devices belong to a DHCP class, named 'ALE-2X' ... TFTP Server address ... In case
    of spatial redundancy, this URL must be the following one: https://<OXE FQDN>/dmictouch" (p181)；
    "Username Enter the user directory number (e.g. 31033) Password Enter the user secret code (by
    default: 0000)" (p184)
  steps: |
    1. 前提核对：OXE FQDN 已建（节点名+域名）、证书已生成、CTL 在 usr3/mao/DM/VHE8082。
    2. 激活 OXE DM：WBM → System/Other System Param./System Parameters → Consult/modify → 取消勾选
       "Device Management In 8770"（勾=DM 在 8770；不勾=DM 在 OXE）。
    3. SIP Phone COS：WBM → NOE and SIP Extension/NOE and SIP COS/Phone COS → Consult/modify：Display
       call server information=Yes、Optimize resource 3PCC call（可选开）、Send NOTIFY instead of
       MESSAGE 按需。
    4. 建 DM profile 3：WBM → SIP device management/DM profile → Create：Profile number=3、Name 自
       定、General 勾 LDAP：URL=ldap://192.168.1.252:389、search base=ou=users,dc=aletraining,
       dc=com、login=cn=admin,dc=aletraining,dc=com、password=superuser（实验口径）；Device 页：DNS1
       =192.168.1.250、SNTP=192.168.1.252；SIP 页：DTMF=SIP Info 或 RFC 4733、SBC=No；Telephony 页：
       Local conference=Yes、Blind/普通 Transfer=Yes；Advanced 页：Admin password=2580、SSH=Yes
       （实验口径）。
    5. 建户：Users → Create：DN=31033、Ellsworth Esteban、Set type=SIP Extension；SIP 页：Sub
       type=ALE-2 或 ALE-3、DM profile=3；Users/SIP Extension Parameters 选 31033 → Phone COS=0。
       Warning：SIP Extension 须为防火墙信任主机（内部 DHCP 启用时地址段自动加入）。
    6. （按需）SSL 安全级：netadmin（root）→ 11 Security → 6 SSL configuration → 3 SSL security
       level → 新级别（示例 2→1，老话机适用）→ 必须重启 OXE；话机证书核查：SSH certificate info 或
       话机 MMI。
    7. DHCP：WBM → DHCP Configuration → Review-Modify → Configuration=DHCP Server（启动 dhcpd；
       默认 off）、Alcatel-Lucent terminals only=No；CPU Main Subnetwork/IP Address Range → Create：
       192.168.1.161-192.168.1.164（实验口径）；Classes → 选 ALE-2X 类：TFTP Server
       address=https://<OXE Main IP>/dmictouch（无/本地冗余）或 https://<OXE FQDN>/dmictouch（空间
       冗余）；All Subnetworks 核对子网（路由可空、DNS primary 按空间冗余需求）；DHCP Configuration
       → Apply Modifications（强制：进程重启读 /etc/dhcpd.conf）。外部 DHCP 替代：配 VCI=aledevice
       + option 66=DM URL。
    8. 话机网络模式：确保 DHCP（Menu → Advanced setting，口令 123456 → Network/WAN port/IP config/
       IPv4 settings → Dynamic）。
    9. 注册：MAC 手工绑定（Users/IP SIP Extension 选 31033 → Terminal Ethernet Address 填 MAC）或
       auto-discovery（话机屏输入 username=31033、password=0000 → OK；注册后 MAC 自动回写、配置即时
       生成）。
    10. 维护：sipregister（31033@192.168.1.161 应出现）；配置文件 ls /usr3/mao/DM/dmictouch/
        （config.3c28a608010d.xml）；nginx access.log 看 404→401 认证序列；downbin 看二进制升级。
  verification: |
    书中验收：sipregister 显示 31033 注册（p186）；access.log 中 GET /dmictouch/config.xml ST=404 与
    config.<mac>.xml ST=401 的认证序列（p186）；downbin 请求 ST=206。
  conditions: 实验 IP/口令均为实验口径；关 8770 DM 会清其配置文件（存量的 reset flash 预案）。
  tags: [lab, ale-2-3, dhcp, dm-profile, auto-discovery]

- id: c06
  title: ALE-x00 话机 SIP 化——SIP 二进制预载、NOE→SIP 切换与从零建户
  type: lab
  source_pages: p196-216
  source_chapter: ALE-x00 Deskphone in SIP mode, using OXE SIP DM
  source_quote: |
    "Configure an 'NOE & SIP extension' phone COS (e.g. #0) allowing the download of both NOE and SIP
    binaries; assign this COS to the user." (p199)；
    "Select the device to switch and click on 'Change NOE to SIP' button Validate clicking on 'OK'"
    (p208)；
    "Configuration file Enter the 'sipconfig.txt' keyword. This info will be used as 'boot file name'
    in the DHCP messages ... allowing the sets to switch in SIP mode automatically" (p214)
  steps: |
    1. 前提与 DM 激活：同 c05 步骤 1-2。
    2. SIP 二进制预载：先把 31011 作为 NOE 用户在服（Starter 课程口径）；WBM → NOE and SIP
       Extension/NOE and SIP COS/Phone COS → 选 COS 0 → Force download NOE/SIP=Yes；Users/8&9
       Series parameters 选 31011 → Phone COS=0。话机侧观察：Menu/Settings/Phone/Local Menu/About/
       Software 显示 Download（后台下载 SIP 二进制，首次可达 30 分钟）→ Upgrade（安装，数分钟）→
       自动重启 → 再查 Software/Options-Version 显示 SIP 版本。
    3. SIP Phone COS：Display call server information、Keep Alive=Yes（话机建议）、3PCC、NOTIFY 代
       MESSAGE。
    4. DM profile 3：同 c05 步骤 4（ALE-X 设备 LAN 拓扑）。
    5. DHCP：范围 192.168.1.161-164；类 SIP80X8s（VCI=ictouch.0）：TFTP URL 同 c05 规则；子网参数
       同 c05；Apply Modifications；外部 DHCP 用 VCI ictouch.0 + option 66。
    6. SSL 安全级：同 c05 步骤 6。
    7. 路径 A（存量切换）：WBM → Users → 选 31011 → "Change NOE to SIP" → OK → 核对 Set type=SIP
       extension、Sub type 自动带出 ALE-300、补 DM profile=3 → Users/SIP Extension Parameters →
       Phone COS=0。
    8. 路径 B（从零建户）：Users → Create：31034 Ellington Edgar、Set type=SIP extension、Sub
       type=ALE-300、DM profile=3 → Phone COS=0；话机强制 SIP 启动：上电按 "I" 或 "*#" → Software
       Infos → Run Mode=SIP → Save → 自动重启进 SIP；网络模式：按 "I" → Network → IP Config → IP →
       IPV4 mode=Dynamic（或 Dynamic Alcatel）→ OK；注册：MAC 手工绑定或 auto-discovery
       （31034/0000）。
    9. 维护：sipregister（31034@192.168.1.162）；dmictouch 目录 config.487a552966d1.xml；access.log
       GET /dmictouch/config.487a552966d1.xml?PHONE_MODEL=ALE-300 ST=200；downbin 的 bin8658P 与
       sip8658P ST=206。
    10. 附录 A（DHCP 批量触发）：仅当系统无其他 NOE 设备或外部 DHCP 可设专用类——DHCP Configuration/
        Classes → 选 NOE 类 → Configuration file=sipconfig.txt（boot file name；外部 DHCP 加 option
        67）。
    11. 附录 B（手动 SIP→NOE）：话机按 "i" → Settings → Advanced Settings → Maintenance → Run Mode
        → Switch → Save → 重启进 NOE（或 WBM 对应按钮）。
  verification: |
    书中验收：话机 MMI 显示 NOE 与 SIP 双版本（p201）；sipregister 注册成功（p213）；access.log 的
    PHONE_MODEL=ALE-300 ST=200 与 downbin 双二进制请求（p213）。
  conditions: 话机先以 NOE 在服是推荐前提；切换仅限本地用户、OXE DM、话机 in service。
  tags: [lab, ale-x00, dual-partition, noe-to-sip, dhcp]

- id: c07
  title: ALES PC 软终端开通——LDAP 认证、防隔离参数、建户 eevans/eeastwood、特性三实验、切本地认证
  type: lab
  source_pages: p217-246
  source_chapter: ALE SoftPhone (PC) — "Bring into service an ALE SoftPhone on a PC"
  source_quote: |
    "Remember, the login information must match with 'uid' of a person managed in the LDAP
    directory." (p230)；
    "Make calls on the group and test the following features such as: Logon/Logoff using ALE-S GUI
    and prefixes (480 and 481 by default..." (p239)；
    "On 1st connection, the user must change his password: it will be 'Administrator2580!'" (p244)
  steps: |
    1. LDAP 探目录：NAS 取 ldapexplorertool.exe → File/Configurations → New：名 LDAP_server →
       Server 页填 LDAP IP（192.168.1.252，实验口径）→ Connection 页 User DN=cn=admin,dc=aletraining,
       dc=com、Base DN=ou=users,dc=aletraining,dc=com → Test Connection（口令 superuser）→ Open 查
       eevans 的 telephoneNumber/userPassword/cn/uid。
    2. 配 OXE LDAP 认证：swinst 登录 → 2 Expert menu → 6 System management → 5 User's accounts
       management → 5 User authentication → 1 Configure LDAP authentication → 2 Create/Modify LDAP
       server：Realm=ITServer、Hostname=192.168.1.252、Port=389、Scheme=ldap://、Search Base DN、
       Login attribute=uid、Filter/Search attributes/Attribute header prefix 留空、Bind DN、Bind
       password → 验证 y；退菜单时 nginx 重配重启提示按 y → 再 1/3 Enable/Disable LDAP
       authentication → 激活。Warning：本地认证若开着必须先关。
    3. SIP 代理：SIP/SIP Proxy → Minimal authentication method=SIP Digest、Framework period=3、
       Framework Nb Message By Period=50、TCP when long messages=勾选（远程工作者尤其）。
    4. SIP Phone COS：Phone COS 0 → Send NOTIFY instead of MESSAGE 按需。
    5. DM profile 1：SIP device management/DM profile → Create：General 勾 LDAP（URL/search
       base/login/password 同上）；SIP 页：DTMF=SIP INFO 或 RFC4733；Telephony 页：Area code=33、
       Country Code=FR、External access prefix=0、Exception=;0、Minimal length=10、Local
       conference=Yes、Blind/普通 Transfer=Yes。
    6. 建户：31030 Evans Elliot login=eevans、31031 Eastwood Elizabeth login=eeastwood；Set
       type=SIP extension、Sub type=ALES-Desktop、DM profile=1；Password 必须留空（外部认证场景）；
       Facilities 勾 Dial by name and text message=Yes；SIP Extension Parameters → Phone COS=0。
    7. 装软件：运行 ALESoftPhone-x.x.xxx.xxx.msi → 许可 → 目录 → 填 CS 地址（本地访问=主 IP
       192.168.1.3 或空间冗余节点名）→ Mini-view 按需 → Outlook 扩展实验不装 → Install/Finish。
    8. 登录：ALES 图标 → login=eevans、password=alcatel（实验口径，全体同密）→ Connect → 首连接受
       DM 服务器证书（需本机管理员权限；可用 Windows GPO 预铺 ROOT CA 免弹窗）。
    9. 维护：sipregister（31030/31031/31060）；sipdict -l（type 3=Extension、type 2=Device）；
       csipsets（含 -d 31030 看配置文件路径、-f 看内容；编解码能力 SWB/WB/NB、G722/G711/G729 列）；
       csipview com（活动呼叫 CH-CC）；check_ales_ldap eevans（root；-b 可带口令绑定测试）；
       ps -edf | grep sipmotor（重启用 dhs3_init -R SIPMOTOR）。
    10. 寻线组实验：WBM → Groups/Hunt Group → Create：DN=31333、Search Type=circular 或
        sequential、成员=31030 与 31000；测试 ALE-S GUI 与前缀 480/481（须在 Phone features COS
        授权）进出组、查组呼叫日志；测完删组。
    11. 监督实验：WBM → Users/Progr. Keys（选 31030）→ Key No.=3、Function=Set Supervision、DN=
        31031、Ringing Mode=No ring mandatory、No Call=NO（按键可呼叫 31031）、Mnemo=Sup. 31031；
        测试他机呼 31031 时 31030 监督状态与按键直呼。
    12. 视频实验：Users 选 ALES → SIP 页 Video Support Profile=On demand；DM profile → Advanced
        Characteristics：Video call encoding profile=High、packetization mode=NALU、profile level
        ID=0x42081f → Save + Generate All Configuration Files → 双方重登 → 音视频设置选摄像头互打
        视频（Rlab 虚拟桌面因 Guacamole 不支持视频而无法测试）。
    13. 切本地认证：swinst → 先 1/3 停用 LDAP（外部开着必须先关）→ 5 User authentication → 3 Use
        local authentication → 激活 → nginx 重配；WBM → Users 选 31030/31031 → Login=eevans 等 +
        Password=Superuser1245*（符合策略，实验口径）→ ALES 重登（eevans/Superuser1245*）→ 首连强制
        改密为 Administrator2580!（实验口径）→ 重登验证。
  verification: |
    书中验收：登录成功且通话正常（p234-235）；check_ales_ldap 输出 eevans's DN（p238）；组/监督/视频
    行为测试（p239-242）；本地认证首连改密成功（p244-245）。
  conditions: 实验口令均为实验口径；外部与本地认证互斥先关后开。
  tags: [lab, ales, ldap, hunting-group, supervision, video, local-auth]

- id: c08
  title: ALES Android 软终端开通——推送兼容参数与移动端差异
  type: lab
  source_pages: p247-270
  source_chapter: ALE SoftPhone (Android)
  source_quote: |
    "Keep Alive NO. For ALES Mobile, this 'Keep Alive' option is mandatory to be set 'NO' to be
    compatible with the Push Notification mechanism" (p252)；
    "Config update polling timer If the value is configured below 21600s, the notification mechanism
    for ALES Android client will not work properly." (p253)；
    "Install ALE SoftPhone on the Android smartphone from the Play Store. For this lab, connect the
    Smartphone to the RAP SSID (Wifi)" (p255)
  steps: |
    1. LDAP 认证配置：同 c07 步骤 2（swinst 路径与参数完全一致）。
    2. SIP 代理：同 c07 步骤 3（SIP Digest + Framework 3s/50 条 + TCP 长消息）。
    3. SIP Phone COS：Phone COS 0 → 激活 SIP 通知、Keep Alive=NO（ALES Mobile 强制，兼容推送）、
       Send NOTIFY instead of MESSAGE。
    4. DM profile 1：General 勾 LDAP 并加目录映射——Directory Firstname=givenname、Name=sn、Office
       number=telephonenumber；Device 页：Config update polling timer ≥21600s（低于该值 Android 通知
       失效）；SIP/Telephony 页同 c07（DTMF、拨号规则 33/FR/0/;0/10、会议与转移 Yes）。
    5. 建户：31035 Edison Eleonore login=eedison；Set type=Extension SIP、Sub type=ALES-mobile、
       DM profile=1、Password 留空；Facilities 勾 Dial by name；SIP Extension Parameters → Phone
       COS=0。（Tips：login/口令可在 LDAP 目录查——见本章附录 LDAPExplorerTool 步骤。）
    6. 装软件：Play Store 装 ALE Softphone；手机连 RAP SSID（Wi-Fi，实验口径）。
    7. 登录：启动应用 → login=eedison、password=alcatel（实验口径）→ Local access=oxe.company.com
       （节点名/FQDN；无冗余时可用主 IP）→ Remote access=公网 FQDN（本实验未用）→ Connect → 接受
       证书 → 拨打/接听/呼叫日志界面示例验证。
    8. 维护：sipregister（31035@192.168.1.164 等 6 用户）；sipdict -l（5 个 type=3 + 31060 type=2）；
       csipsets（ALESmobil 行）；csipsets d 31035（配置文件路径 /DHS3data/mao/DM/dmsoftphone/ALES-
       mobile/__/65/conf_65656469736f6e.xml）；csipview com；check_ales_ldap eedison；sipmotor 进程。
    9. 切本地认证：停用 LDAP → 启用本地（同 c07 步骤 13 菜单）→ WBM 给 31035 配 Password=
       Superuser1245* → ALES 登录 eedison/Superuser1245* → 首连改密 Administrator2580!（实验口径）。
  verification: |
    书中验收：移动端登录并出/入呼成功（p257）；sipregister/csipsets 输出含 31035（p259-260）；本地
    认证改密成功（p263）。
  conditions: Keep Alive=NO 仅 ALES Mobile 强制；推送依赖该参数与轮询阈值。
  tags: [lab, ales-mobile, push, dhcp, ldap]

- id: c09
  title: 编解码验证——compvisu 四场景读数
  type: lab
  source_pages: p283-286
  source_chapter: Codecs — "Check the voice algorithm used during a communication"
  source_quote: |
    "Establish a call between: A SEPLOS user (example ALES '31030') An IP DSP (31000) ... Use the
    compvisu command to verify the selected codec" (p284)；
    "nbcomp / comp type : - / NOCOMP-OPUS_WB (c0) <--> 0 / NOCOMP-OPUS_WB (c0)" (p285)
  steps: |
    1. 场景 1（SEPLOS 内呼）：ALES 31030 呼 IPDSP 31000（或任一 NOE IP 话机）→ CS 上 mtcl 执行
       compvisu eqt all → 读 nbcomp/comp type 行：LIOE_IP-G722(83) <--> NOCOMP-G722(80)，确认实际
       算法 G722、无转码直通。
    2. 场景 2（经私有中继）：SIP Device 31060 呼 31000 → compvisu：JONCT <--> 10,T2-IPNS,Private TG
       侧 LIOE_IP_NOT-G722(84)，确认 G722 且 ABC-F SIP 中继组参与（本地网关 G722 已开）。
    3. 场景 3（SEPLOS 呼公网）：31030 呼公网 0210x12345 → compvisu：SIP,mcdu=31030 <--> 2,T2-ISDN,
       SIP ITSP2 侧 NOCOMP-OPUS_WB(c0) 双向，确认 OPUS_WB 与公共 SIP 中继参与（外部网关 OPUS/G722
       已开）。
    4. 场景 4（SIP Device 呼公网）：31060 呼公网 → compvisu：JONCT <--> JONCT（10,T2-IPNS,Private
       TG <--> 2,T2-ISDN,SIP ITSP2）NOCOMP-G722(80) 双侧，确认公私两条 SIP 中继同链。
  verification: |
    书中验收：每场景 compvisu 输出与预期算法一致（p284-286 四段 Notes）；结论口径——实际算法取决于
    SIP profile、系统参数、IP 域与外部网关编解码开关。
  conditions: compvisu 为 mtcl 命令；场景前置是 c03/c07 等实验的网关与编解码配置。
  tags: [lab, codecs, compvisu, verification]

- id: c10
  title: SIP 跟踪四工具实验——motortrace、oxetrace、mtracer、sipdump
  type: lab
  source_pages: p312-327
  source_chapter: SIP traces and tools — "Use the different commands and tools available for SIP traces"
  source_quote: |
    "(1)csa> motortrace 1 ... (1)csa> traced" (p313)；
    "Enter the Relevant Question Indexes Separated by Space -> 2 ... Enter the folder name (will be
    created in /tmpd/) ? trace-1" (p315)；
    "Warning IT IS NECESSARY TO HAVE TWO CONNECTIONS ON THE CALL SERVER: ONE FOR NAVIGATING IN THE
    'sipdump' MENU AND THE OTHER IN ORDER TO GET THE RESULTS" (p321)
  steps: |
    1. motortrace：mtcl 登录 → motortrace 1 → traced → 打 SEPLOS 31034 呼 NOE 31000 → 读 INVITE/
       100 Trying/180 Ringing/200 OK 报文 → Ctrl-C 停。级别经验：1 最少、2 大流量观察、3 无流量定向
       深挖。
    2. oxetrace：mtcl → oxetrace → 1 Start Trace → 按问题选号（例 2=SIP Endpoint；菜单含 1 Trunks/
       3 Audio/4 Display/5 Remote Extension(Rainbow)/Nomadic/6 Attendant/7 通用场景/8 actdbg 过滤/
       9 tuner/10 关二进制/11 关 tcpdump/12 改 motortrace 级别默认 8/13 mao 跟踪）→ 命名文件夹
       trace-1（建于 /tmpd/）→ 复现呼叫 → 选 2 Stop → 保留文件夹选 1 Keep（生成 zip 于
       /tmpd/TRACE-1_<时间戳>.zip）→ 0 退出。
    3. 取回分析：PC 上 Filezilla 以 sftp 连 OXE → 从 /tmpd（/usr4/tmp）拷回 → 解压后 Tcpdump_Captures
       的 pcap 双击进 Wireshark：SIP 过滤、看 SDP 编解码、Telephony/SIP Flows 或 VoIP Calls 看流程
       图；Sip_Motor_Traces 目录文本可直接读信令。
    4. mtracer：mtcl → tuner km → tuner clear-traces → tuner +cpl +cpu +at → actdbg csip=on →
       mtracer -a → 复现场景（书中例：31033 对 31000 做 51 立即呼转，观察 INVITE 51@… 与 SDP/算法）→
       Ctrl-C → 收尾：tuner clear-traces、actdbg all=off、dhs3_init -R MTRACER。
    5. sipdump：双连接均 mtcl（Warning：一个跑菜单、一个跑 traced）→ 连接 A 执行 sipdump → 选项 1
       （网关管理数据：许可 20/20、TLS 30/30、降级模式状态）→ 3（呼叫数）→ 4（calls-neqt 映射）→
       5（呼叫清单）→ 复现呼叫后 2 Dump a call（输入 Neqt 与 DialogId：看 From/To/External VM/Sip
       Device/Ext Gateway/Session Timer）→ 7 Release a call（强拆；代理发 BYE）→ 11 追踪过滤：
       Add filter 串 31030@oxe.company.com、To field=y（31 字符内；过滤作用于 motortrace，仅匹配
       通信经 traced 显示）。
  verification: |
    书中验收：traced 输出完整 SIP 事务（p314）；zip 归档与解码目录生成（p316）；Wireshark 流程图
    （p318）；sipdump 强拆后 ALARM terminated 事件（p326）；过滤生效仅显示匹配呼叫（p327）。
  conditions: 各命令登录账号：mtcl（traces/sipdump）、root（部分清理）；tip——测 sipdump 前先建立含
    SIP 用户的呼叫。
  tags: [lab, traces, oxetrace, mtracer, sipdump, wireshark]

- id: c11
  title: OXE 侧经 SBC 接入 SIP 运营商——防火墙到回拨翻译九段配置与 sipextgw 验证
  type: lab
  source_pages: p347-363
  source_chapter: SIP Carrier access via SBC — "Configure the access to a SIP carrier via SBC"
  source_quote: |
    "Warning THIS MANAGEMENT MUST BE DONE ACCORDING TO THE SIP PUBLIC PROVIDER REQUESTS! ... TO
    CONFIGURE THE SIP GATEWAY AS EACH OPERATOR HAS ITS OWN SPECIFIC PARAMETERS" (p349)；
    "Warning ARS IS REQUIRED TO USE SIP TRUNK GROUP WITH AN EXTERNAL SIP GATEWAY" (p355)；
    "(1)csa> sipextgw -l ... IN SERVICE SIP external gateways list : 1 3" (p362)
  steps: |
    1. 防火墙信任主机：root → netadmin -m → 11 Security → 1 Firewall(iptables) Configuration →
       3 Restricted Access Configuration → 2 Add a trusted host：IP name=sbc、IP
       address=192.168.1.105（实验口径）→ Apply；双机用 Copy set up 同步；mtcl 执行 more /etc/hosts
       核对 sbc 行。
    2. 系统参数：WebAdmin → System/Other System Param./System Parameters 核对 Law（欧洲 A 律/美国
       μ 律）；System/Other System Param./Compression Parameters 核对 G722 support perimeter 与 OPUS
       support perimeter（Warning：系统级关了，外部网关开了也没用）。
    3. SIP 中继组：Trunk Groups → Create：ID=2、Type=T2、Node=1、Q931 Signal variant=ISDN all
       countries、Number Compatible With=-1、Digits To Send=0、Remote Network=255 或 15（不参与）、
       T2 Specification=SIP、DID transcoding 暂 No。
    4. 外部 SIP 网关：SIP/SIP Ext Gateway → Create：ID=3、Name=ITSP2_GW、SIP Remote
       domain=192.168.1.105（SBC LAN 地址）、Port=5060、Transport=UDP、Registration timer=0（注册由
       SBC 代做）、Outbound proxy 留空、Supervision timer=0 或 5（OPTIONS 探活）、Trunk group
       number=2、Outgoing realm/username/password 留空、DNS type=DNS A、SIP DNS1=10.20.30.250（可
       选）、Minimal authentication method=None、Gateway type=Standard；编解码四开关：Support
       OPUS=Yes（连带 G711=Yes）、Support G722=Yes（默认，连带 G711）、Support G711=Yes、Support
       G729=Yes（建议恒开）。
    5. ARS——前缀：Translator/Prefix Plan → Create/编辑：Number=0、Prefix Meaning=ARS Prof. Trk Grp
       Seizure、Discriminator No=0（逻辑 0-7）。
    6. ARS——中继组关联：Trunk groups → 编辑 TG 2 → Associated Ext SIP gateway=3（或经编号命令表）。
    7. ARS——路由表：Translator/Automatic Route Selection/ARS Route list → Create：列表 9、名
       ITSP2 national；其下 ARS Route → Create：Route=1、名 ITSP2 Gateway、Trunk Group
       Source=Route、Trunk Group=2、No.Digits To Be Removed=1（去"0"）、Digits To Add=33、Called
       number source=Route、NPD Identifier=255（暂）、Quality=Speech；Time-based Route List →
       Create：ID=1、Route Number=1、Waiting/Stopping Cost Limit=-1。
    8. ARS——判别器：Translator/External Numbering Plan/Numbering Discriminator/0 public/
       Discriminator Rule → Create：Call Number=0、Area Number=1（默认，不做闭锁）、ARS Route List
       Number=9、Schedule Number=-1、Number of Digits=10；entity 关联：Entities/<entity>/
       Discriminator Selector：Discriminator 00→0、01→1、…、07→0（Warning：实际判别器必须已存在）。
    9. DID/NPD/回拨：Translator/External Numbering Plan/DID numbering translator → Create：ID=1
       （0 为默认）、名自定义、模式 Default DID mode；DID number translator rules：First External
       Number=33920131000（POD x 为 33920x31000）、First Internal=31000、Range Size=1000、Unique
       Internal Number=NO；NPD → Create：ID=34、名 public_operator_2、Calling/Called NPI/TON=ISDN
       International、Install. Number source=None used、Default number source=NPD source、Default
       number=33920131000、Called DID identifier=1、Calling/Connected DID identifier=1；Trunk Group 2
       → Trunk group NPD selector：Public/Private NPD ID=34、Management Mode=Normal；回拨：
       Ext. Callback Translation Tables/DEFAULT/Ext. Callback Translation Rules → Create：Basic
       Number=A33、No. Digits To Be Removed=3、Digit To Add=00。
    10. 维护验证：sipextgw -l（在服网关清单含 3）→ sipextgw -g 3（逐参数核对：IN SERVICE、remote
        domain、5060/UDP、TG 2 (ISDN)、四编解码 TRUE；OTSBC 未配好前对外不可用）；trkstat -r 2
        （动态刷新，62 路；Q 退出）。
  verification: |
    书中验收：sipextgw -l 显示网关 3 在服（p362）；trkstat 2 显示 62 trunks（p363）；注释——OTSBC
    尚未配置时外部网关不工作（p363），端到端通话验收在 c12 完成后。
  conditions: 一切参数以运营商要求为准（TC2005 等）；实验中 ITSP2 为模拟器。
  tags: [lab, sbc, external-gateway, ars, did, npd, callback]

- id: c12
  title: OTSBC 部署与调通——CLI 初始化、向导八屏、编解码/消息域/注册三修正
  type: lab
  source_pages: p364-383
  source_chapter: OTSBC deployment — "Deploy OTSBC"
  source_quote: |
    "Mediant SW(config-voip)# interface network-if 0 ... set ip-address 192.168.1.105 ... write ...
    reload now" (p366)；
    "SIP ACCOUNT Account Type Registration Username Enter the login expected by the SIP carrier. Here
    podx (x pod number) Password ... alcatel" (p372)；
    "Put the login expected (podX) by the ITSP gateway in the field 'Contact User'" (p382)
  steps: |
    1. 拓扑确认：OTSBC LAN=192.168.1.105、DMZ=192.168.2.105、NAT 公网=12.C.P2.105（C=class、
       P=POD，实验口径）；实验 VM 已部署（生产从 MyPortal 取软件，OVF 或 ISO）。
    2. CLI 初始化：控制台 Admin/Admin（enable 口令同）→ configure voip → interface network-if 0 →
       set ip-address 192.168.1.105 / prefix-length 24 / gateway 192.168.1.254 → exit 两次 → write →
       reload now。
    3. Web 登录与许可：浏览器开 OTSBC LAN IP → Admin/Admin → 许可核对（Setup/Administration/
       License 可录 key；实验默认 3 通道够用）。
    4. 向导：Actions → Configuration Wizard → WELCOME（模板可 Update from Remote Server）→ GENERAL
       SETUP：IP-PBX=Alcatel-Lucent Enterprise OXE、SIP-Trunk=Generic SIP Trunk、Network Setup=Two
       ports (LAN and WAN) → SYSTEM：HTTPS+SSH、Enable Syslog（IP=192.168.1.10）、Time Zone=GMT+1、
       Primary NTP=10.20.30.250 → INTERFACES：LAN(192.168.1.105/24/GW 192.168.1.254/DNS
       192.168.1.250) 与 WAN(192.168.2.105/24/GW 192.168.2.254/DNS 10.20.30.250)、NAT Public
       IP=12.C.P2.105、OAM=LAN → IP-PBX：Address=192.168.1.3、SIP Domain=192.168.1.3 → SIP TRUNK：
       Address=gateway.itsp2.com、SIP Domain=itsp2.fr → SIP ACCOUNT：Type=Registration、
       Username=podx、Password=alcatel（实验口径；ITSP 认证由 SBC 代做）→ NUMBER MANIPULATION：出向
       目的/源号码勾选 Prefix=+ Remove=1 Add=空；入向 Prefix=* Remove=0 Add=+ → SUMMARY：Apply &
       Reset（或 Save INI 存档）。Warning：重启后向导按 SYSTEM 设置启用 HTTPS，通用证书须手工接受。
    5. 排障一（编解码）：OXE 用户呼 0210x12345 → Syslog 看 SDP：OXE→SBC 带 G722/G711(PCMA)/G729，
       SBC→ITSP 只剩 G711(PCMA) → SETUP/SIGNALING & MEDIA/CODERS & PROFILES/Allowed Audio Coders
       Groups → 组 1 → Allowed Audio Coders 2 items >> → New → G729 → Apply → Save。
    6. 排障二（消息域）：呼出仍被 ITSP 拒（From/Proxy Authorization 域为 OXE IP）→ MESSAGE
       MANIPULATIONS → New：Index=4、名 SBC->ITSP From、Set ID=1、Message Type=Any、Subject=
       header.from.url.host、Type=Modify、Value='itsp2.fr'；Index=5 同法改 header.to.url.host →
       Save；CORE ENTITIES/IP Groups → 选 index 2 ITSP → Edit → Outbound Message Manipulation
       Set=1 → Apply/Save → 重呼：SDP 含 G711+G729、域已识别、出现 ACK。
    7. 排障三（注册）：公网呼入不通（SBC 未在 ITSP 注册成功；REGISTER 的 from/to/contact 不合规）→
       SIP DEFINITIONS/Accounts → 编辑向导建的账号 → Contact User=podX → Apply → Action 菜单
       Register 即时注册 → Syslog 复核 REGISTER 变 podX@itsp2.fr → 公网呼入打通（ACK）。
  verification: |
    书中验收：出向呼叫 ACK（p380）；REGISTER 格式正确（podX@itsp2.fr，p383）；来话呼叫 ACK（p383）。
  conditions: 账号/域/公网 IP 均为实验口径；向导所有产物可在 Webadmin 手工重配。
  tags: [lab, ot-sbc, wizard, message-manipulation, registration]

- id: c13
  title: OTSBC 内嵌反向代理配置——证书、RP 三件套、远程对象六件、路由分流
  type: lab
  source_pages: p421-449
  source_chapter: OTSBC with embedded Reverse Proxy for remote workers
  source_quote: |
    "Create a new 'TLS context' dedicated to the 'Remote Workers' ... Import the 'Root CA'
    certificate in this new 'TLS context'" (p425-426)；
    "Activate the reverse proxy feature of the OTSBC ... After validation of reverse proxy function,
    the OTSBC must be restarted." (p431)；
    "Header.to.URL contains '192.168.1.105'" (p447)
  steps: |
    1. TLS Context：SETUP/IP NETWORK/SECURITY/TLS Contexts → New：名 Remote_Workers、TLS
       Version=TLSv1.1 和 TLSv1.2、DTLS=DTLSv1.0/1.2、Cipher Server=AES:RC4、Client=ALL:!ADH、
       Strict Certificate Extension Validation=Disable、DH Key Size=2048 → Apply/Save。
    2. Root CA 导入：该页底部 Trusted Root Certificates → Import → 选网络盘
       Y:\10.20.30.200\Sharing 的 ca-certgen（实验口径）→ Open → Save。
    3. CSR 与证书：Change Certificate → 先生成 Private key（OK+Save）→ 填 CSR：Subject Name=
       rpsbcX.company.com（X=POD 号）、OU=Training、Company、Locality=Brest、State=Brittany、
       Country=FR、SAN1=rp1.company.com、SAN2=sbc1.company.com（可选）、Signature=SHA-256 → Create
       CSR → CSR 文本存 txt 放网络盘 POD 子目录 → 外部 CA 签发后回 TLS Contexts → Change
       Certificate → Load Device Certificate File（.cer，Base-64 X.509）→ Save。
    4. RP 激活：SETUP/IP NETWORK/HTTP PROXY/General Settings：HTTP Proxy application=Enable、HTTP
       Cache=Disable、Primary DNS=10.20.30.250 → Save → 必须 Restart。
    5. Upstream：SETUP/IP NETWORK/HTTP PROXY/Upstream Groups → New：Index=1、名 OXE_443、
       Protocol=HTTP\HTTPS、Load Balancing=IP Hash、Max Connections=0 → Upstream Hosts items →
       New：Host=192.168.1.3、Port=443、Weight=1、Backup=Disable → Apply/Save。
    6. Proxy Server 与 Location：HTTP Proxy Servers → New：Index=1、名 RP_oxe_443、Domaine
       Name=rpsbcX.company.com、Listening Interface=WAN(eth1)、HTTPS Listening Port=443、TLS
       Context=Remote_Workers、Bind To Device=Disable、Verify Client Certificate=No → HTTP
       Locations items → New：Index=1、URL Pattern=/DM/dmsoftphone/、Type=Prefix、Upstream
       Scheme=HTTPS、Upstream Group=OXE_443、Upstream Path=/DM/dmsoftphone/、Outbound
       Interface=LAN(eth0)、Cache=No、SSL/TLS Context=Remote_Workers、Verify Certificate=No →
       Save。
    7. 媒体安全与 NAT：MEDIA/Media Security：Enable、Behavior=Mandatory、SRTP 套件
       AES-CM-128-HMAC-SHA1-80；MEDIA/Media Settings：NAT Traversal=NAT Only if Necessary（通道默认
       10000）。
    8. SIP Interface：CORE ENTITIES/SIP Interfaces → New：Index=3、Topology Up、Network
       Interface=WAN(eth1)、Application Type=SBC、UDP=0、TCP=0、TLS Port=5261、TLS Context=
       Remote_Workers、User Security Mode=Accept Registred Users、Enable Un-Authenticated
       Registrations=Disable。
    9. Media Realm：CORE ENTITIES/Media Realms → New：Index=3、名 RemoteUsers、IPv4
       Interface=WAN(eth1)、UDP Port Range Start=6000、Media Session Legs=100。
    10. NAT 翻译：IP NETWORK/CORE ENTITIES/NAT Translations → New 两条：5261-5261 与 6000-6399
        （Source Interface=eth1），Target IP=12.C.P2.105（实验口径）→ Save。
    11. IP Profile：CODERS & PROFILES/IP Profiles → New：Index=3、名 RemoteWorkers、Broken
        Connection Mode=Ignore、SBC Media Security Mode=Secured、Signalling Diffserv=40；核对 OXE
        既有 profile：Ignore/Not secured/Replaces 不动。
    12. 操纵组：MESSAGE MANIPULATION/Message Manipulations → 组 3 四条规则：header.to.url.host 与
        header.from.url.host（Message Type Any）→ Modify 'rpsbcX.company.com:5261'；refer.request 且
        header.Refer-To 存在 → header.Refer-To.url.host；refer.request 且 header.Referred-By 存在 →
        header.Referred-By.url.host；再给 OXE 组 2 追加两条：条件 host contains 'rpsbcX' → from/to
        url.host 改 'oxe'。
    13. IP Group 与分类：CORE ENTITIES/IP Groups → New：Index=3、名 RemoteUsers、Topology=up、
        Type=User、IP Profile=RemoteWorkers、Media Realm=RemoteUsers、Classify by proxy
        set=Disable、Media TLS context=Remote_Workers、Outbound Message Manipulation set=3；SBC/
        Classification → New：Index=1、名 ALES Users、Source SIP interface=sipinterface3、
        Destination Host=rpsbcX.company.com、IP Group Selection=Source IP Group、Source IP
        Group=RemoteUsers。
    14. 路由分流：MESSAGE MANIPULATION/Message Conditions → New：Index=1、名 To ITSP、Condition=
        Header.to.URL contains '192.168.1.105'（tip：ITSP 呼叫 header.to=SBC IP，远程呼叫
        header.to=设备注册地址）；SBC/Routing/IP-to-IP Routing → 既有 OXE→ITSP 路由 MATCH 挂 Message
        Condition='To ITSP' → New 两条：Index=15 名 OXE to remote workers（Source IP Group=1、
        Destination Type=All Users）；Index=30 名 ALES->OXE（Source IP Group=3、Destination Type=IP
        Group=1）→ Save。
  verification: |
    书中验收：配置序列完成后由 c14 远程登录验证（端到端）。本章内建核对点：RP 激活后强制重启（p431）、
    操纵规则 Apply/Save 序列、路由条件挂接。
  conditions: 域名/公网 IP/共享盘路径均为实验口径；RP 证书可与 OTSBC 共用（非强制专用）。
  tags: [lab, reverse-proxy, ot-sbc, tls, routing]

- id: c14
  title: ALES Remote Worker 配置与验证——远程 DM profile、异地 PC 登录、sipregister 核对
  type: lab
  source_pages: p450-458
  source_chapter: ALES Remote Worker — "Configure ALES for remote workers"
  source_quote: |
    "Create a new DM profile for remote worker mode use: ID: 2, Name: Remote Workers, SBC: SBC and
    LAN, Outbound proxy and RP addresses: rpsbcX.company.com" (p451)；
    "Warning USING THIS RDP FILE, YOU WILL PERFORM AN RDP CONNECTION IN YOUR ALREADY ACTIVE RDP
    SESSION. TAKE CARE WHEN YOU WILL STOP ... THIS ONE AND NOT THE MAIN (FIRST) ONE." (p453)；
    "contact : sip:FEU461-3-2-1@192.168.1.105, udp, 3543 s" (p458)
  steps: |
    1. 前提：OTSBC LAN 地址 192.168.1.105 已是 CS 信任主机（netadmin；同 c11 步骤 1；见 Starter 与
       "SIP carrier access via SBC" 实验）。
    2. 远程 DM profile：SIP device management/DM profile → Create：Profile number=2、Name=Remote
       Workers；SIP Characteristics：DTMF=SIP Info 或 RFC4733、SBC=SBC and LAN（或按用户场景 SBC
       only）、outbound proxy address=rpsbcX.company.com、outbound proxy port=5261、Reverse proxy
       FQDN=rpsbcX.company.com；Telephony Characteristics：拨号规则 Area code=33、Country=FR、
       External access prefix=0、Exception=;0、Minimal length=10、Local conference=Yes、Blind/
       普通 Transfer=Yes。（可并入默认 profile 0；只给部分用户远程时建议专用 profile——Tips。）
    3. 用户挂 profile：Users/<user>/SIP → DM profile=2（Warning：profile 必须先存在再配用户）。
    4. 远程 PC 接入：用对应 RDP 文件连 PODx-outside 实例（Warning：RDP in RDP，断开时关第二层会话，
       别断主会话）。
    5. 异地安装 ALES：跑 ALESoftPhone msi → Local access=oxe.company.com、Remote
       access=rpsbcX.company.com（POD1 为 rpsbc1）→ 不装 Outlook 扩展 → Install/Finish。
    6. 登录测试：ALES → login=eevans（31030；31031=eeastwood、31032=eelkins）、password=alcatel
       （实验口径）→ Accept 证书 → Connect → 互打通话。
    7. 维护核对：CS 上 sipregister → 远程用户 contact 显示经 SBC 注册（sip:FEU461-3-2-1@192.168.1.105，
       即 SBC LAN 地址），本地用户仍为直连 IP:5160。
  verification: |
    书中验收：ALES 在远程 PC 登录并通话（p457）；sipregister 中远程用户 contact 指向 SBC 地址
    （p458）。
  conditions: 全部域名/口令为实验口径；本实验依赖 c13 的 RP/SBC 配置完成。
  tags: [lab, ales, remote-worker, dm-profile, sipregister]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 20 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 准备实验/交付环境 | 有 → c01（虚机清单、预配置核对、IPDSP/TFTP；环境拓扑本身归 framework f02/f03） |
| task-02 掌握运营商模拟器 | 无独立实验章。p21-34 为讲义（号码规则/变换示例），已并入 c01 步骤 7 的引用与 framework f04/f05 |
| task-03 POD 预配置与外线打通 | 有 → c01（步骤 5-7：pbxN 参数 + DID 翻译 + 外呼验证） |
| task-04 SIP 协议机理 | 无实验。p43-54 概念讲义（报文样例非操作序列），机理归 framework f07-f10 |
| task-05 OXE 域名与空间冗余 | 有 → c02（域名查改；空间冗余解析为讲义，归 f12） |
| task-06 SEPLOS vs SIP Device 选型 | 无实验。p64-82 概念章（f14/f16 承接）；c03 是 Device 开通落地 |
| task-07 SIP Device 开通 | 有 → c03（九段配置 + 建户 + 维护六命令） |
| task-08 终端家族选型 | 无实验。p95-106 功能矩阵讲义（查表决策） |
| task-09 ALES 认证设计 | 有 → c07 步骤 1-2/13（LDAP 配置、外部↔本地切换） |
| task-10 ALE SIP 特性配置 | 有 → c07 步骤 10-12（寻线组/监督/视频）；呼叫路由为 GUI 操作未单列实验 |
| task-11 SIP DM 选型与规划 | 无实验。p144-167 概念章（f26-f29 承接）；DM 激活动作内嵌于 c05/c06 |
| task-12 OXE DM 证书定制 | 有 → c04 |
| task-13 ALE-2/3 话机开通 | 有 → c05 |
| task-14 ALE-x00 双分区与切换 | 有 → c06（含 DHCP 触发与手动切换附录） |
| task-15 ALES 软终端开通 | 有 → c07（PC）、c08（Android） |
| task-16 编解码协商与验证 | 有 → c09（讲义 p271-282 归 principle/framework） |
| task-17 SIP 跟踪采集分析 | 有 → c10（讲义 p287-311 归 framework/principle） |
| task-18 外部网关判定 + OXE 侧 SBC 接入 | 有 → c11（判定流程讲义归 f39） |
| task-19 OTSBC 部署调通 | 有 → c12 |
| task-20 远程办公规划与落地 | 有 → c13（OTSBC 反代）、c14（ALES Remote Worker）；方案决策讲义归 f44-f46 |

**统计**：14 条（全部 lab 型，与 14 个 How-To 实验章一一对应）；20 项任务中 11 项有案例类直接覆盖，9 项为概念章/查表内容或讲义级（task-02/04/06/08/11 无独立实验，已在表内注明承接位置）。
