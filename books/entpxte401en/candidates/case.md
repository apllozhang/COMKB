# 案例/实验/操作序列候选 — OmniPCX Enterprise Advanced (ENTPXTE401EN Ed13, R101.1 MD4)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号）标注"实验口径"。
> 条目说明: 全书 18 个 How-To 实验章 → 18 条（Pod Configuration 两章、冗余两章、IP 域、PCS、本地溢出、速拨、多线/监督、经理助理、寻线/代接、办公桌共享、多设备、Direct IP Link、Audit、Broadcast、组网双向溢出）。

```yaml
- id: c01
  title: 集中式 IP 实验 Pod 配置（机架板卡、IPDSP 用户、外部 SIP 网关、DID 翻译、出局验证）
  type: lab
  source_pages: p46-54
  source_chapter: Pod Configuration: Centralized IP labs
  source_quote: |
    "Only start the required Virtual machines for this lab ... OXE CSB (ENTP_OXE_CSB) and PCS REMOTE
    (ENTP_PCS_REMOTE) will be started later to avoid IP address conflict." (p47)
    "Don't forget to specify the TFTP server IP @ in IPDSP settings. ... TFTP Server Main 192.168.1.3" (p51)
    "Registration ID pbxN (where N is your POD number) ... First external number 33210N41000 (where N is
    your POD Number) ... Range Size 500" (p53-54)
  steps: |
    1. 按 RLAB/混合模式清单仅启动所需 VM（实验口径：OXE CSB 与 PCS REMOTE 稍后启动，避免 IP 冲突）。
    2. OXE 预配置核对（VM 已预置）：许可已恢复、NTP 192.168.1.252 与 FlexLM 192.168.1.80 已声明、DHCP
       已启用（VLAN1 192.168.1.145-149 / VLAN2 192.168.2.145-149）、SSHv2 已启用、防火墙部分配置、机架/
       板卡/用户/语音导引/公网 SIP 中继组已建。
    3. 核对机架板卡（主站：Rack 4 虚拟 GD4 192.168.1.13/24 MAC 00:50:56:01:01:13；远端：Rack 6 虚拟 GD4
       192.168.2.13/24 MAC 00:50:56:02:01:13；混合模式另含硬件 Rack 2 GD4 192.168.1.12 + MIX484）。
    4. 安装并启用 IPDSP 软话机（实验口径：31000 Brad Barkley→PC10、31001 Billy Backman→PC11、31002 Betty
       Boop→PC20、31003 Becky Bernstein→PC21）；IPDSP 右键 Settings→Network 填 TFTP Server Main=192.168.1.3。
    5. 外部 SIP 网关填 POD 参数：SIP/SIP Ext. Gateway → Registration ID=pbxN、Outgoing username=pbxN
       （N=POD 号，如 POD3→pbx3）。
    6. DID 翻译：Translator/External Numbering Plan/Default DID num. translator → Create → First external
       number=33210N41000、First internal number=31000、Range Size=500。
    7. 外呼验证：按 SIP Carrier Simulator 文档拨测（例 POD3：0110312345，PBX 送出 +33110312345）。
  verification: |
    出局呼叫经 ITSP1 成通（模拟器回铃/接听）；IPDSP 注册成功（TFTP 下载正常）。书中验收口径为"set up some
    outgoing calls ... to make sure that access to public SIP carrier is working properly"（p54）。
  conditions: RLAB 环境；所有 IP/账号为实验口径；OXE CSB/PCS REMOTE 启动顺序受 IP 冲突约束。
  tags: [lab, pod, ipdsp, sip-gateway, did]

- id: c02
  title: 呼叫服务器本地冗余部署（netadmin 双机、防火墙 bulk、MAO 三参数、mastercopy、autostart、设备指向）
  type: lab
  source_pages: p92-114
  source_chapter: Call Servers duplication with local redundancy
  source_quote: |
    "CALL SERVERS MUST HAVE THE SAME SOFTWARE VERSION AND BE IMPLEMENTED ON IDENTICAL PLATFORMS" (p94)
    "Choice 186 E-CS redundancy = 1" (p94, spadmin 输出)
    "Do you wish to copy the DATABASE AND ACCOUNTING (y/n): y ... Do you wish to copy the LINUX DATA
    (y/n, default n): y" (p107)
    "(1)csa> twin ... Transmission CPU-CPU : READY • Telephony redundancy : READY ..." (p113)
  steps: |
    1. 许可核验：csa 上 mtcl 执行 spadmin → 2 → 确认锁 186 E-CS redundancy=1（实验输出另见 184
       Gatekeeper=99999、185 SIP Gateway=2）。
    2. csa IP 配置：mtcl 执行 netadmin（建议 console 模式，IP 方式会在应用新参数时断连）→ 擦除重配：node
       name=oxe、本地 CPU 位置=a、CPU name=csa/192.168.1.1/24、main=csrm→csm/192.168.1.3、twin=csb/
       192.168.1.2、domain=company.com、router=192.168.1.254。
    3. 防火墙：Security→3 Restricted access→7 Bulk Import 导入 /tmpd/Firewall_Rules_multi.txt（含 NTP、
       PC VM、教室 PC、OMS、GD4；csa/csb 本身不在文件内，twin 声明后自动互信）→ a 应用；提示 Copy to twin。
    4. csb 同法：位置=b、CPU csb/192.168.1.2、main csm/1.3、twin csa/1.1；查看 trusted hosts 确认 csa 自动
       在列。⚠ 每台改完 netadmin 后必须关机重启（A SHUTDOWN OF THE CS IS MANDATORY AFTER THE NETADMIN
       MANAGEMENT）。
    5. SSH 密钥：root 执行 oxe-ssh-auth -c 192.168.1.2（输入远端 mtcl 密码，同一密码套用全部账户选 y）；
       完成后两侧 authorized_keys 各含 6 条公钥。
    6. MAO 参数：WBM /Shelf/ 选离 CS 最近的 MG（OMS，MG #4）→ Reference YES；/IP/ → Preferred CS @IP
       (redundancy)=192.168.1.1；/IP/Duplication parameters → Pseudo Main True/False（True=real+pseudo，
       False=real+real）。
    7. mastercopy：在 csb（目标备机）swinst→1 Easy menu→7 Stop the telephone（确认后系统重启）→swinst→2
       Expert menu→3 Cloning & duplicate→1 CPU cloning→3 Cloning database→按需勾选（至少 DATABASE AND
       ACCOUNTING=y，LINUX DATA=y 以带走 csa 防火墙；VOICE GUIDES/TRAFFIC/ACD=n）→确认后等待（BE
       PATIENT!，话音应用自动启动）。
    8. autostart：csb swinst→2 Expert→6 System management→2 Autostart management→1 Set autostart（自动
       同设在 twin CPU）。
    9. 设备指向：GD4 admin 登录 sudo mgconfig→2→CPU role address=192.168.1.3；OMS sudo omsconfig→2→同
       样填 main 地址；静态 IP 话机在 *# → IP Parameters/IP Config/IPv4 Wired/System Settings 填 TFTP
       #1=192.168.1.3。
  verification: |
    ①csa> role -b → MAIN stand-by CPU state : ACTIVE；csb> role -b → STAND-BY；②csa> twin → Redundancy
    State 各项（Duplicated configuration/Transmission CPU-CPU/Telephony/monitel/memloader/All
    applications）全 READY 后才允许切换；③主库建对象备库实时可见；④csa> bascul → y 切换，已建立通话保持；
    测试完切回 csa 为 main。
  conditions: 主备同版本同平台；SSH 密钥先行；mastercopy 只能在备机上、备机话音须已停。
  tags: [lab, redundancy, duplication, mastercopy, bascul]

- id: c03
  title: 呼叫服务器空间冗余部署（双子网、csma/csmb、内部 DNS、DHCP 适配、SIP 终端 DNS 委派）
  type: lab
  source_pages: p115-138
  source_chapter: Call Servers duplication with spatial redundancy
  source_quote: |
    "csa: 192.168.1.1/24 • csb: 192.168.2.1/24 • csma: 192.168.1.3 • csmb: 192.168.2.3 • routera:
    192.168.1.254 • routerb: 192.168.2.254 ... Don't forget to active the Internal DNS Server" (p117)
    "5. CPU redundancy role address 192.168.2.3" (p134-135, mgconfig/omsconfig 输出)
    "INTERNAL DNS RESOLVER activation is mandatory in the OXE (done with 'netadmin' tool)" (p136)
  steps: |
    1-5. 与 c02 同构（许可/防火墙/SSH/mastercopy/autostart），差异在 netadmin 参数：csa=192.168.1.1、main
    =csma/192.168.1.3、twin csb=192.168.2.1、twin main csmb=192.168.2.3、本地 router a=192.168.1.254、
    twin router b=192.168.2.254；csb 镜像配置；两台都激活内部 DNS（netadmin 问 Do you want to activate
    internal name resolver → y）。netadmin 显示 internal name resolver activated: yes。
    6. MAO 参数同 c02（Reference MG、Preferred CS、Pseudo Main），另加 3.4 DHCP：用 OXE DHCP 无需特殊处
       理（各 CS 按自己主地址下发 dhcpd.conf 的 tftp 字段）。
    7. 设备指向（双主地址）：GD4 mgconfig/OMS omsconfig 的 CPU redundancy role address 填第二主地址
       （192.168.2.3）；静态话机 TFTP #1=192.168.1.3、TFTP #2=192.168.2.3。
    8. SIP 终端/应用：外部 DNS 委派节点名到两个主地址（oxe → 192.168.1.3 & 192.168.2.3）；OXE 内部 DNS
       解析器必须启用以应答客户 DNS 查询。
  verification: |
    role -b/twin 全 READY；bascul 切换测试同 c02；netadmin -m 显示两子网接口与 twin 配置（csa: local
    192.168.1.1/main csma 192.168.1.3/router routera；CPU redundancy: twin csb 192.168.2.1/twin main
    csmb 192.168.2.3/router routerb）。
  conditions: 双端不同子网需各自路由器；SIP 设备依赖 DNS 委派与内部解析器。
  tags: [lab, spatial-redundancy, dns, netadmin]

- id: c04
  title: IP 域配置与验证（建域、地址段分配、压缩参数、CAC 测试、domstat/cnx dom/compvisu）
  type: lab
  source_pages: p154-163
  source_chapter: IP domains
  source_quote: |
    "Open the OXE WBM interface IP\\IP Domain 'Create' button ... Maximum number of calls from/to this
    domain that can be established is '1'" (p155)
    "Try to perform 2 calls between sets belonging to Domain 1 & sets belonging to domain 2 ...
    As 'Domain Max Voice Connection' is equal to '1' in each domain, only 1 call can be established." (p159)
    "(1)csa> compvisu eqt all ... nbcomp / comp type : - / LIOE_IP-G722 (83)" (p163)
  steps: |
    1. 建域 1（主站 VLAN 192.168.1.x）：WBM IP\IP Domain→Create→Domain Number=1、Intra domain
       bandwidth=Large、Extra domain bandwidth=Low、Voice Service broadcast=YES、Accept/Provide conf
       circuits=YES、Domain Max Voice Connection=1、Domain Type=IP；同法建域 2（远端 192.168.2.x）。
    2. 分配地址：IP\IP Domain\IP Domain Address→Create：域 1 段 192.168.1.12-1.13（GD/OMS）、
       192.168.1.10-1.11（IPDSP）、单主机 192.168.1.145（Low=High，Tips）；域 2 同法（2.13、2.10-2.11、
       2.145-2.146）。⚠ 掩码必须与设备一致；设备须复位后才落域。
    3. 压缩参数：System\Other System param.\Compression Parameters→G722/OPUS support perimeter（Network
       and local / Local only / Not available）；OPUS dynamic payload type 默认 125；G722 Conference With
       OMS 改后需重启 OMS。
    4. CAC 测试：31000（域 1）呼 31002（域 2）→ 通；再从 31001 呼 31003 → 应被拒（allowed=1）；两域改 -1
       后两通全通。
  verification: |
    ①domstat（mtcl）→ 菜单 1 看域参数（Dom Type=IP_REMOTE、Max. Cnx、Ext/Int Algo=Low/High Bandwidth）、
    菜单 5 看 Entries（R. 段与 Host 条目）、菜单 8/10 看域内设备（含 GD/OMS coupler 与话机 MAC/IP）；②cnx
    dom → allowed/used 计数、RIP/IPP Intr/Extra 带宽档、UseOthCC/ProvidCC、压缩机计数；③compvisu eqt all →
    域内呼叫 LIOE_IP-G722 (83)、跨域呼叫 LIOE_IP-G729 (43)，验证编解码与配置一致。
  conditions: 域 0 为 CS 专用，其他域地址段不得覆盖 CS 地址；实验分机号视可用设备而定。
  tags: [lab, ip-domain, cac, domstat, compvisu]

- id: c05
  title: PCS 部署全流程（许可核验、console 改 IP、防火墙互信、WBM 声明、域绑定、OMS PCS 声明、SSH、pcscopy）
  type: lab
  source_pages: p185-210
  source_chapter: Passive Communication Server
  source_quote: |
    "the PCS VM uses a default IP configuration (10.253.253.1/26), which is not compatible ... you must
    use the 'console mode'" (p187)
    "Open the OXE WBM interface \\Passive Com. Server\\PCS Addresses 'Create' button ... Automatic update
    type: Daily ... Reset type: Timeout value = '0'" (p197-198)
    "(1)csa> pcscopy ... PCS Database Update => End OK" (p209)
  steps: |
    1. 前提：启动 PCS VM；mtcl 登录看欢迎信息比对版本（PCS ≥ CS；实验输出 R101.1-n4.523-0-fr-c0s1）；spadmin
       确认锁 332 PCS max. number=0/3。⚠ PCS 出厂 IP 10.253.253.1/26 与实验网不兼容，第一步必须 console 模式。
    2. PCS IP 配置：console 下 mtcl 执行 netadmin → node=oxe、CPU pcs/192.168.2.5/24、domain=company.com、
       router gw/192.168.2.254。
    3. PCS 防火墙：Security→Restricted access→2 逐个加 csa(1.1)/csb(1.2)/csm(1.3)（pcscopy 必需，hosts 自
       动更新）→7 Bulk Import Firewall_Rules_multi.txt→a 应用；more /etc/hosts 核对。
    4. CS 侧放行 PCS：csa 上 root 执行 netadmin -m→11 Security→1 Firewall→3 Restricted access→2 加
       pcs/192.168.2.5→a；重复配置场景执行 Copy to twin 同步 csb；两边 more /etc/hosts 核对。
    5. WBM 声明：\Passive Com. Server\PCS Addresses→Create→IP=192.168.2.5、Mask=255.255.255.0、Name=PCS、
       Update type=General parameters、Reset type=General parameters、PCS FQDN=pcs.company.com（必填）。
    6. 全局参数：\Passive Com. Server\→Automatic update type=Daily（实验：每天 23:00）、Reset type=Timeout
       值 0（人工重启）、Database validity=0（每次更新都现做新库）。
    7. 域绑定：\IP\IP Domain\ 选域 2（远端 192.168.2.x）→Backup IP address=192.168.2.5；验证：IPDSP 域 2
       用户 Settings→Network 出现 Passive CS PCS IP @；硬件话机可用 tnet d <号>（口令 *tx8000#）→ipconfig
       survi 查看。⚠ THE PCS MUST REMAIN IN IP DOMAIN 0!
    8. OMS 声明：远端 OMS（Shelf 6）sudo omsconfig→2→6 Passive CS address=192.168.2.5、7 Passive CS
       domain=pcs.company.com→保存并重启 OMS。
    9. （信息性，本实验不做）SIP 外部网关：SIP\SIP Ext Gateway→PCS IP address=255.255.255.255（全局地址）
       +注册计时器≠0。
    10. SSH 分发：root 执行 oxe-nw-sshkey-sync -f /tmpd/ssh_multi.csv（含 csa/csb/pcs）；完成后 csv 自动删
        除、日志在 /tmpd/logs；或用 oxe-ssh-auth 跑两遍（csa↔pcs、csb↔pcs）。核验 authorized_keys 共 9 条。
    11. PCS 初始化：swinst 建空库、启用 Autostart、设日期时间；手工参数逐项配（防火墙/NTP/SNMP/Radius 等）。
    12. pcscopy：CS 上 mtcl 执行 pcscopy→1 PCS update→输 192.168.2.5→等待 PCS Database Update => End OK
        （结束后 PCS 自动重启）。
  verification: |
    pcsview（CS 侧）：菜单 1 列 PCS（pcs/192.168.2.5/INACTIVE/Timeout (0 s)）；菜单 3 看 域→PCS 关联
    （pcs(192.168.2.5)→DOMAIN 2）；菜单 5 按域查（Domain 2 is secured by PCS ...）。pcsview（PCS 侧）：
    State INACTIVE、secured 域列表、被救 coupler 清单。
  conditions: PCS 版本 ≥CS、锁 332>0；hosts 文件缺条目则 pcscopy 不工作。
  tags: [lab, pcs, pcscopy, netadmin, omsconfig]

- id: c06
  title: PCS 断网救援与回切演练（Rlab 断链、ACTIVE 接管核验、INACTIVE*、手动重启回切）
  type: lab
  source_pages: p210-216
  source_chapter: Passive Communication Server / 10 Maintenance
  source_quote: |
    "Disconnect the 'main site' (Subnet 192.168.1.X) from the network • Check that the PCS switches to
    'ACTIVE' mode" (p211)
    "PCS is ACTIVE ... Nb Ip Phones connected to the CPU is: 2 ... Number of Domain connect on PCS: 1/1" (p212-213)
    "As 'PCS reset type' has been configured in this lab with a Timeout value = '0', it means that the
    PCS must be restarted manually by the Administrator." (p214)
  steps: |
    1. 断链：Rlab 门户选 POD→Subnet 1（192.168.1.254）点 Disconnect。⚠ 断后主站全部 VM 无法 IP 访问，测
       试须用远端 Subnet 2 的 PC。
    2. 接管核验：PCS 上 mtcl→pcsview→State: ACTIVE；清单显示 Domain 2 (actually connect on pcs)、
       Nb Ip Phones=2、Number of Domain connect on PCS=1/1；菜单 1 看 GD4 cr6 IN SERVICE；config 6 看晶
       体拓扑（GD4 MAIN 30/30 — INTIP3A）。
    3. 话务核验：远端站内互打通；跨站呼叫仅当配置 Local Private to Public Overflow 才可能（Notes）。
    4. 恢复链路：Rlab 点 Connect 重连 Subnet 1。
    5. 过渡态核验：pcsview→State: INACTIVE*（设备仍挂 PCS、等计时器）。
    6. 手动回切（Timeout=0 口径）：PCS 上 shutdown -r now 重启。
    7. 复位核验：pcsview→State: INACTIVE、被救设备/域清零（Nb Ip Phones=0、Number of Domain connect 0/1、
       No cpl in service found），域 2 回到 CS 控制。
  verification: |
    状态迁移链 INACTIVE→ACTIVE→INACTIVE*→(手动重启)→INACTIVE 全程 pcsview 可见；GD4 cr6 在 ACTIVE 期间
    IN SERVICE。
  conditions: 实验口径 Timeout=0；生产默认 30 秒自动回切；断链期间主站不可 IP 管理。
  tags: [lab, pcs, failover, pcsview, rlab]

- id: c07
  title: 本地私到公溢出配置（Node Access Prefix、DID 段、thin sector、COS 双开关、OoS 溢出参数）
  type: lab
  source_pages: p228-233
  source_chapter: Local Private to Public Overflow
  source_quote: |
    "PLEASE, NOTE THAT THIS LAB CANNOT BE PERFORMED WITH THE CURRENT RLAB ENVIRONMENT. THIS MANAGEMENT
    PROCEDURE IS PROVIDED ONLY AS INFORMATION" (p229)
    "First external number 33210141000 ... First internal number 31000 ... Range size 2 ... Thin Sector
    No" (p230)
    "Busy private to public overflow 1 (1 to allow the feature, 0 to forbid) • O/S private to public
    overflow 1" (p232)
  steps: |
    1. ⚠ 本实验在当前 RLAB 不可执行，仅作客户现场配置参考；前提：PCS 已按前章部署；ARS 管理为 Starter 内容
       不在本章展开。
    2. Node Access Prefix 全局参数：Translator/External Numbering Plan/Node Access Prefix→Create→
       Destination Node No.=1、Number to Add=0（ARS 前缀）；⚠ Install.No.Last Part 必须留空（由 thin
       sector 提供缺省号）。ARS 表首路由尽量用主叫本地中继组。
    3. DID 段（主站 DID 用户）：Node DID Translation→Create→First external=33210141000（按 POD，POD1-6
       分别为 332101-33210641000）、First internal=31000、Range size=2（31000/31001）、Thin Sector=No。
    4. DID 段（远端 DID 用户）：First external=33210141002、First internal=31002、Range size=2、Thin=No；
       另一段 33210141011/31011/2/No（31011/31012）。
    5. thin sector 段（非 DID 用户 31020-31029）：First external=33210141010（站点任一 DID 号，如 31010
       的外号）、First internal=31020、Range size=10、Thin Sector=YES。⚠ 该外号不得与既有 DID 段重叠。
    6. COS：Classes of Service/Phone Features COS→选类别（如 0）→Busy private to public overflow=1、O/S
       private to public overflow=1。
    7. OoS 溢出：System/Other System Param./System Parameters→Overflow on OoS Extension=True；⚠ Don't
       forget to perform a 'pcscopy'。
  verification: |
    测试口径（书中 Test）：把域 2 的 Domain Max Voice Connection 改回 1→主叫远端第一通走 IP 通、第二通应
    走公网建立→验证完改回初始值。
  conditions: 本实验不可在 RLAB 执行；需 ARS 与闭锁（starter）前置。
  tags: [lab, overflow, thin-sector, cos, pcs]

- id: c08
  title: 速拨编号体系管理（上限扩容、直接缩位号、闭锁受控、开放缩位号、定时溢出、范围与实体映射、edabv）
  type: lab
  source_pages: p246-254
  source_chapter: Speed Dialing Numbers
  source_quote: |
    "Go to the '/usr3/mao' directory • Type the command 'cfgUpdate' • Select the 'Abbreviated Numbers'
    parameter index value • Enter the new limit (ex: 32500) • Restart OXE (reboot)" (p247)
    "Create the direct Speed Dialing number '112' ... Call Number: 0 112 • Directory Name: Emergency" (p248)
    "To display the Direct Speed Dial Numbers 60 1 - pref = 60 ... enter criteria or command: go" (p254)
  steps: |
    1. 扩容上限（默认仅 4000）：mtcl→cd /usr3/mao→cfgUpdate→选 Abbreviated Numbers→输 32500→重启 OXE。
    2. 直接式范围：Speed Dialing/Direct Speed dialing numbers→Index for 1st=0、Length=1000。
    3. 紧急号：Direct SpdDI No. Pref.→Create→Prefix=112、Call Number=0 112、Directory name=Emergency；
       话机 310x0 拨测。
    4. 普通直接号：Prefix=60、Call Number=0 0210N41000（N=POD）、Name=Office Supply；外呼验证屏显目录名、
       dial by name 可搜到；入局呼 0 0210N410x1 验证屏显 Office Supply。
    5. 闭锁受控：把系统闭锁改为禁外呼→编辑 60 勾 Call Restrictions-Barring→分别用允许/禁止外呼的用户测。
    6. 开放缩位号：Prefix=2、Call Number=0 0210N41、Name=ALE Training；310x1 拨 2 再补 000 测；建 Prefix=
       640、Call Number=0 0210N41000（ALE Training Welcome）作定时转发号→拨 2 后不补拨、等溢出计时器自动
       转发。
    7. 范围 0：Spd DI Numbers by Range→Range 0→Index=1000、Length=100、Number of Digits=2；建号 0→
       Call Number=0 0210N41002、Name=Travel Agency Booking。
    8. 实体映射：Entity/1/Entity Spd Dial Numbers Range→确认 Area 0→0（每实体至多 32 区、系统 400 范围）。
    9. 范围前缀：Translator/Prefix Plan→Create→Number=61、Prefix Meaning=Speed Dialing Area、Information=0；
       拨 61 00 测试。
    10. 查询：mtcl 执行 edabv -l GEA→pref=60、idx、num→go（显示 60|1|00210141000）；可用 =/!=/>/>=/</<=
        /[: ] 运算符；-l US0 切英文。
  verification: |
    外呼/入局屏显目录名、dial by name 命中、闭锁受控行为符合勾选、定时溢出在计时器超时后自动转发、61 00
    经范围 0 呼出、edabv 输出与配置一致。
  conditions: 扩容需重启；号码均含实验口径 POD 变量 N。
  tags: [lab, speed-dialing, cfgupdate, edabv]

- id: c09
  title: 多线与监督键配置（multi-keys、multi-MCDU、自动占用参数、监督键、multitool 核验）
  type: lab
  source_pages: p267-273
  source_chapter: Multi-Line & Supervision Keys
  source_quote: |
    "User Key 1 Key 2 • 310x1 Multi-Line > 310x1 MultiLine > 310x1" (p268)
    "Function Set Supervision ... Ringing Mode ... No Call NO: pressing the key calls the 31001" (p271)
    "(1)xa000001> multitool ... [ 1] - Consult Multilines And Supervised Sets" (p272)
  steps: |
    1. Multi-keys：WBM Users/<用户>/Progr. Keys→310x1 键 1=Multi-Line 310x1、键 2=Multi-Line 310x1；
       310x2 同法两键。测试：310x0 与 310x1 同时呼 310x2，用其两键在线间切换。
    2. Multi-MCDU：310x1 键 3=Multi-Line 31101；310x2 键 3=Multi-Line 31102、键 4=Multi-Line 31202。⚠ 附加
       号必须是编号计划中的空闲号。测试：分别呼 31102/31202 并在键间切换。
    3. 可选参数：Users/<用户>/Progr. Keys→Facilities 页→Automatic Incoming Seizure（True=摘机自动接第一
       个振铃线，默认）与 Automatic Outgoing Seizure（True=摘机自动选第一空闲线，默认）；310x1 上实测两档。
    4. 监督键：310x2 上键 5=Set Supervision→Directory Number=310x1、Ringing Mode 五选一（No ring/Short/
       Long/Short ring without Overring/Long ring without Overring）、No Call（NO=按键直呼被监督者，YES=
       仅监督）。测试：直呼、改 No Call 后禁直呼、来话振铃时按键代接。
  verification: |
    mtcl 执行 multitool：菜单 1 Consult Multilines And Supervised Sets（31001 Multiline=Yes Supervised=
    Yes；31002 Multiline=Yes）；菜单 5 Consult Directory Number Supervision→1 列被监督号、2 按号列监督者
    （31001←31002 键 5）、3 列全部监督关系（含键号与域）。
  conditions: 监督者必须 multiline；话务台/寻线组不可被监督（概念章限制）。
  tags: [lab, multiline, supervision, multitool]

- id: c10
  title: 经理/助理组配置（键组、过滤表、screening/unscreening、助理侧监督键、溢出助理、multitool 核验）
  type: lab
  source_pages: p286-295
  source_chapter: Manager/Assistant groups
  source_quote: |
    "Key No. Programmable Key number (ex. 5) • Function Assistant Call • Directory Number ... (ex. 31001)" (p287)
    "Create 2 filtering tables. The table 1 allows to select all the external calls • The table 2 contains
    only the internal number 310x0" (p291)
    "Function Routing Assistant ... Directory Number Directory Number of the Manager (ex. 31002)" (p294)
  steps: |
    1. 建组：31002 为 Manager、31001 为 Assistant（双方须已 multiline）。Manager 31002 键 5=Assistant Call
       →DN=31001、Key Number=5；Assistant 侧自动生成 Manager Call 键。测试互拨。
    2. Assistant Away：31001 键 6=Assistant Away；按下激活（经理侧可见状态）。
    3. Manager Mail：31001 键 6=Manager Mail；话机按 Mail→选预设"Here is %"→补人名→Apply；经理侧选预设
       回复（如 Do your best）→助理侧收到。
    4. Selective Filtering：Users/31002→Facilities 页→勾 Selective Filtering（只转主线来话）。
    5. 过滤表：Specific Telephone Services/Filtering table→Create 表 1（Filter type=All Trunk Groups，代表
       全部外线来话）；再建表 2（Filter type=One Directory No.→310x0）。Filter type 可选 All Directory No./
       All Trunk Groups/One Directory No./One Speed Dialing No./One Attendant number/T2 Key。
    6. Screening 键：31002 键 6=Screening Key→Filtering Table No.=1（激活后仅外线来话转助理）；用公网用户
       呼入测。
    7. Unscreening 键：31002 键 7=Unscreening Key→Table=2（激活后仅 310x0 来话留经理、其余转助理）；310x0
       内呼测。
    8. Screening Supervision：31001 键 7=Screening Supervision→DN=31002、Key Number=6；助理按键远程开/关
       经理的 screening，LED 同步。
    9. Routing Assistant：310x0（须 multiline，无则先加键）键 3=Routing Assistant→DN=31002；测试链：助理按
       away→经理激活 screening→公网来话应转溢出助理。
  verification: |
    multitool 菜单 2 Consult Boss/Secretary：1 列 Boss（31002 键 5）、2 列 Secretary（31001 键 5）、3 列
    Routing Secretary。
  conditions: 建键前双方至少一把 multiline 键；每经理仅一名溢出助理且不得已是其助理。
  tags: [lab, manager-assistant, screening, multitool]

- id: c11
  title: 寻线组与代接组配置（建组、成员两法、进出组前缀与权利、pbxstat/supgpbx、pickup 组、zdpost）
  type: lab
  source_pages: p316-326
  source_chapter: Hunting and pickup groups
  source_quote: |
    "Create the Hunting Group 31300 with the 'Circular' search type ... Assign 2 users in this group" (p317)
    "The two prefixes are created by default with the numbers 480 for the 'Sta. Group Entry' prefix and
    481 for the 'Sta. Group Exit' prefix." (p320)
    "Action pbxstat –f d <Hunt group directory number> ... modcycle CYCLIC ... etat_groupe ABCA_SG_FREE" (p321)
    "zdpost d 31001 |grep -i pickup_id → pickup_id = 0" (p326)
  steps: |
    1. 预整理：清 310x0/x1/x2 的可编程键；310x0/x1 去掉 multiline、310x2 保留两把主号 multiline 键；统一
       Phone features COS。
    2. 建组：Groups/Hunt Groups→Create→DN=31300、Name=Hunting Gr. 1、Type=Local Hunting Group、Search
       type=Cyclical→Create 后从组侧 Add an element 加 310x1、310x2（或从 Users/<用户>/Facilities 的
       Hunting Group Dir No. 字段加入）。310x0 呼 31300 验证轮转；改 Search type=Sequential 复测。
    3. 进出组前缀核验：Translator/Prefix Plan 过滤 Prefix Meaning=Set Features、Station Features=Sta.
       Group entry / Sta. Group exit（默认 480/481，如缺则建）。
    4. 用户权利：Classes of Service/Phone Features COS→Set features→Sta. group entry/exit=1；310x1 实测
       拨进出组前缀。
    5. 维护：mtcl 执行 pbxstat -f d 31300（nu_tete 头成员、max_att、modcycle、etat_groupe=ABCA_SG_FREE/
       PART_FREE/TOT_BUSY/OOS、成员 etat_poste=ABCA_IDLE/BUSY/HW_OOS）；supgpbx -le（组状态/全网组/统计）。
    6. 代接组：先把 310x1/x2 移出寻线组；Users/<用户> 填 PickupGroup Name=Pickup Gr1（无独立建组菜单，
       填名即自动成组）；Groups/Pickup Group 核对（只能查不能建）。
    7. 代接前缀：Prefix Plan 过滤 General Features=Group call pickup（56）/ Direct call pickup（55）；COS
       里 Group/Direct call pickup=1；互打后分别用 56（同组代接）与 55+号码（直接代接）测。
  verification: |
    zdpost d 31001 |grep -i pickup_id → 0（在组）；zdpost d 31000 → -1（不在组）；pbxstat 输出与 supgpbx
    菜单正常显示。
  conditions: 一台话机只能属于一个寻线组；截图中 480/481 与 55/56 的 Note 文本存在互换（见 counter-example）。
  tags: [lab, hunting-group, pickup, pbxstat, zdpost]

- id: c12
  title: 办公桌共享配置（前缀与 COS、DSS/DSU 与键、虚拟 MAC、系统参数五项、dsstat/ippstat/incvisu）
  type: lab
  source_pages: p338-351
  source_chapter: Desk sharing
  source_quote: |
    "Create the logon and logoff prefixes with the numbers 62 and 63" (p339)
    "Set Function Desk Sharing Set ... Set Function Desk Sharing User ... aa:bb:00:03:10:x0" (p341-344)
    "Command dsstat ... Display all DSS's :1 ... Log-off all DSUs :11" (p348)
  steps: |
    1. 前缀：Translator/Prefix Plan→62=Desk Sharing Over Logon、63=Desk Sharing Logoff；COS→Set features
       →Desk Sharing Over Logon=1、Desk Sharing Logoff=1。
    2. 建 DSS：Users→Create→DN=310x5、Shelf/Board/Equipment=255、Set Type 按实机、Set Function=Desk
       Sharing Set；IPDSP 需在 Users/TSC IP user 开 IP-Softphone emulation=Yes；注册后在 TSC IP user 看到
       真 MAC/IP。
    3. DSS 键：Progr. Keys 键 1=Programmed Content=62（Mnemo LogOn、Locked YES）；键 2=Programmed
       Content=310x2（Help Desk）。
    4. 改 DSU：Users/310x0→Set Type=IPTouch 8068s、Set Function=Desk Sharing User；TSC IP user 自动出现
       虚拟 MAC aa:bb:00:03:10:x0、IP=Unused。
    5. DSU 键：键 1=Programmed Content=62（OverLogOn）；键 2=Programmed Content=63（LogOff）。
    6. 系统参数：System Parameters→Activate Logoff without pwd（默认 False）；Spec. Customer Features→
       DSU Auto Log-off Time（默认 -1；0-23 点）、Allow Reset of Busy DSU（默认 True，触发 6004）；System
       Parameters→Default DSU Secret Code Change（默认 False）；Local Features→Instant DS login/off fro
       NOE3GEE（默认 True）。
    7. 测试登录/登出、忙时被顶（Unauthorized/6004）、自动登出。
  verification: |
    dsstat 13 项（列 DSS/DSU、登入者、8/9 单查、10/11 登出、12 定时登出写 crontab、13 远程登录）；incvisu
    可见 6004 两条样例；domstat 菜单 9 的 DS 列（31005=S、31000=U）；ippstat 菜单 8 全 MAC 表、菜单 3 本节
    点话机、ippstat d 31000 判读（登出态虚拟 INTIP 255/255；登入态 19/1 且按 MAC 反查所在 DSS）；话机清除：
    I+# → IP parameters → Free seating。
  conditions: 虚拟 MAC 为应用层标识；即时登录仅限 NOE3GEE/Essential/Enterprise 同族同节点无 AOM。
  tags: [lab, desk-sharing, dss, dsu, dsstat]

- id: c13
  title: 多设备用户配置（主/副站声明、Twinset Get Call 前缀、主站退服三参数、zdpost 核验）
  type: lab
  source_pages: p365-371
  source_chapter: Multi devices user
  source_quote: |
    "ON CREATION OF THE MULTI DEVICE ASSOCIATION, ALL DATA (CALL FORWARDINGS, CALLBACKS, MESSAGE DEPOSITS,
    ETC.) ARE CANCELLED ON THE SETS." (p366)
    "Tandem Directory Number Enter the directory number of the first secondary set (310x1) • Main set in
    the tandem True ... Attached multi device Add up to 3 secondary devices" (p367)
    "Number Enter a free directory number ... (e.g.: 652) • Prefix meaning Local features • Local features
    Twinset Get Call" (p368)
  steps: |
    1. 前置：把 310x0 恢复 Default set function（去掉 Desk Sharing User）、删其 Over Logon/Logoff 键。⚠ 建
       关联会清空两台话机全部数据（呼转/回叫/留言），主站数据复制到副站且不可再改。
    2. multiline 核验：310x0/x1 各确保至少两把主号 multiline 键。
    3. 主站：Users/310x0→Tandem Directory Number=310x1、Main set in the tandem=True、Attached multi
       device 最多再加 3 台；同页配 Partial busy（默认 False）/Ringing in partial busy（Long 默认）/
       Specific supervision（False 默认）。
    4. 副站核对：Users/310x1 自动显示 Tandem DN=310x0、Main set=False、Attached 空。
    5. 快速移机：Translator/Prefix Plan→Create→Number=652、Prefix Meaning=Local features、Local
       features=Twinset Get Call；COS→Twinset Get Call=1；测试：呼入接听后另一空闲侧拨 652，通话无感迁移。
    6. 主站退服行为：COS→Forward if set is out of service=1；System Parameters→Overflw to sec tandem if
       main OOS=True；COS→Ring all its secondar. if main oos=True（生效依赖前两项）；修改在主站退服期间不
       生效（Tips）。
  verification: |
    mtcl 执行 zdpost d 31000：输出含 multi_device_main=0、tandem_mcdu=31001、tandem_principal=1、
    tandem_occ_part、tandem_son_occ、tandem_supv_spec 等字段；通话与移机行为符合预期。
  conditions: 副站类型限制（DECT/REX 各一）；禁用机型清单见概念章。
  tags: [lab, multi-device, twinset, zdpost]

- id: c14
  title: 组网实验 Pod 迁移与双节点基线（VM 网卡迁移、Network/Node 号、双节点 DID/SIP、互拨验证）
  type: lab
  source_pages: p372-382
  source_chapter: Pod Configuration: Network labs
  source_quote: |
    "Due to RLAB infrastructure and technology, 2 VMs (even if not started) can't have the same IP
    address." (p375)
    "Remove the network interface of 'ENTP_OXE_CSA' VM ... Create Interface ... Select 'Subnet1' ... Enter
    the IP @ '192.168.1.1'" (p375-376)
    "Default number: Network=0; Node = 1" (p378)
  steps: |
    1. VM 网卡迁移（RLAB 口径）：Rlab Instances→ENTP_OXE_CSA→Show→Remove Interface（释放 192.168.1.1）；
       ENTP_OXE_NODE_1→Show→Remove Interface（释放 192.168.1.111）→Create Interface→Subnet1→IP
       192.168.1.1→Send；硬重启 NODE 1；从 NODE 2 ping 1.1 验证。
    2. 预配置核对：许可/SSHv2/防火墙（含静态话机 IP）/NTP/FlexLM 已就绪、DHCP 关闭、机架用户导引中继已建、
       默认编号 Network=0/Node=1。
    3. 机架：NODE1 Rack4 虚拟 GD4 192.168.1.13（MAC 00:50:56:01:01:13）；NODE2 Rack3 虚拟 GD4
       192.168.1.113（MAC 00:50:56:01:02:13）；混合模式另含教室硬件。
    4. 用户：NODE1 31000/31001（PC10/11，TFTP=192.168.1.3）、NODE2 31500/31501（PC20/21，TFTP
       =192.168.1.103）；混合模式 31010 ALE-500/31020 ALE-30H/31510 ALE-300/31511 ALE-20H。
    5. SIP 网关：NODE1 Registration ID/username=pbxN；NODE2=remoteN。
    6. DID：NODE1 First external=33210N41000、internal 31000、size 500；NODE2=33110N41500、31500、500。
    7. 外呼与节点互拨验证（参照 SIP Carrier Simulator：0110341501 / 0210341001 等口径）。
  verification: |
    ping 通、双节点各自出局通、节点间经 ITSP1 的 DID 互打通。
  conditions: 实验口径；生产直接在各自网段布NODE，无 VM 迁移步骤。
  tags: [lab, rlab, network-labs, did]

- id: c15
  title: Direct IP Link 组网（系统选项三态、99 条空链、接入创建、网络号/路由号测试、维护命令、加删节点）
  type: lab
  source_pages: p399-423
  source_chapter: Direct IP Links creation
  source_quote: |
    "Create entire database: Y • Direct Link Network: Y" (p402)
    "OXE REBOOT IS REQUIRED ('SHUTDOWN -R NOW') TO TAKE INTO ACCOUNT THIS PARAMETER" (p403)
    "during the 'RUNTEL', the OXE network becomes fully meshed ... on each node, 99 Direct IP Links,
    WITHOUT ANY ACCESS, are created" (p404)
    "Before adding more accesses (or before deleting), the Direct Link synchronization must be DISABLED." (p407)
    "rsthyb 2 all ... Restarting on node:1 of direct IP link:Link_2" (p417)
  steps: |
    1. 系统标识：System 菜单→NODE1 Network=1/Node=1、NODE2 Network=1/Node=2→各重启。
    2. 系统选项：检查 System/Other System Param./Network Parameters 的 Direct IP Link；空库路径（信息性，
       本实验不做）：swinst 空库时 Direct Link Network=Y；存量路径：Disabled→Migrating→shutdown -r now 重
       启→Enabled（不可逆）。⚠ 本实验 DO NOT CREATE AN EMPTY DATABASE。
    3. 全互联核验：重启 RUNTEL 后每节点自动生成 99 条 Link_xx（无接入、High bandwidth、Max IP calls=-1）；
       WBM 逻辑链路列表只显示带接入的链路（hybvisu/trkvisu 用 dl 选项看全）。
    4. 接入创建：Inter-Nodes Links/Logical Links (ABC-F)/Link_2→Hybrid or Direct Link Access→接入 1：
       Access number=1、Signaling type=IP、对端 CS 主 IP（NODE1 侧填 192.168.1.103；spatial 可在 Other 填
       第二主地址）；NODE2 侧 Link_1 对称。加第二接入前先在任一接入上 Disable Direct Link synchro（整链断）
       →建接入 2：Without signaling + Sig Provider=1（可至多 24）→重新 Enable。⚠ 两端接入数必须一致。
    5. 编解码：System/Other System Param./Compression parameters→G722/OPUS support perimeter=Network and
       local（各节点同配）。
    6. 测试呼叫（audit 前）：Translator/Prefix Plan 建 Network No.（Number=31500、Network=1、Node=2、Type
       =Station）或 Routing No.（Number=315、digits=5）；互拨验证。
    7. 维护：compvisu sys（Direct IP Link ENABLED/压缩参数）；hybvisu -f all / -f 2（状态 IDLE/SYN_REQ/
       SYN_ACK/DATA_TRANSFER、带宽、对端编解码、Main CPUa、Encryption）；trkvisu all/trk/link/<2002>（链
       路与链上呼叫）；rsthyb 2 all（复位）；incvisu（2880/2881/2882/2884/2832/2846）+ incinfo GEA。
    8. 加节点（信息性）：新节点启用直链选项→全网 broadcast Operational→在既有节点对 Link_3 建接入 1（自
       动广播到其他节点）→新节点对 Link_1 建接入 1→新节点 audit：菜单 1→1 Immediate→1 Reference
       building→64 General checks→节点选 2 Only one node=1→参考节点=1；若新节点原有个库，必须再做阶段 2
       Reference downloading（全网）。
    9. 删节点（信息性）：先在全网各节点删对 X 的全部 Without signaling 接入（不广播）→再在任一节点删 IP
       信令接入（经广播全网删除）。
  verification: |
    hybvisu -f 2 显示 Direct IP link 2002 to node 2 : UP (Enabled/DATA_TRANSFER) High Bandwidth、accesses=2、
    Distant codecs 全集；trkvisu 2002 显示链上活跃呼叫；两节点互打成功且 compvisu eqt all 显示 RTP 直达。
  conditions: 全网 ≥R100.0；选项 Enabled 不可逆；两端带宽/加密/接入数一致（否则 2879）。
  tags: [lab, direct-ip-link, abc-f, audit, rsthyb]

- id: c16
  title: Audit 全网对账（防火墙/SSH 前提、模拟先行、两阶段执行、对象/节点列表选择）
  type: lab
  source_pages: p444-469
  source_chapter: Audit
  source_quote: |
    "declare in the internal firewall of each Call Server ... all the remote Call Servers IP addresses as
    trusted hosts ... cs2 / 192.168.1.101 ... cs2m / 192.168.1.103" (p445)
    "(101)cs1> audit -l EN0 ... Choice 4 (Simulation : Immediate running) ... Choice 64 - General checks" (p449-450)
    "In this training context, 6 public keys should be present" (p447)
  steps: |
    1. 防火墙：root 执行 netadmin -m→11 Security→1 Firewall→3 Restricted access→2 逐个加对端全部地址
       （cs2=192.168.1.101、cs2m=192.168.1.103；生产还需 twin 与第二主地址）→a；NODE2 对称配置（⚠ DON'T
       FORGET）；more /etc/hosts 核对。
    2. SSH：oxe-ssh-auth -c 192.168.1.103（多节点用 oxe-nw-sshkey-sync）；完成后 authorized_keys 6 条。
    3. 模拟阶段 1：audit -l EN0→1 Activation→4 Simulation: Immediate→1 Reference building→64 General
       checks→节点选 1 Global network→参考节点问句直接回车（=本地）；审查模拟结果（菜单 2 Results）。
    4. 真实阶段 1：1→1 Immediate→1 Reference building→64→1→回车；完成后本节点库含全网 specific 数据。
    5. 模拟+真实阶段 2：同法选 2 Reference downloading；各节点回报处理报告。
    6. 结果核对：WBM Translator/Numbering Plan——NODE2 用户在 NODE1 显示为 network number。
    7. （信息性）部分审计：菜单 4→5 CK_CONF_OBJ_LIST 建对象列表（.obl）→执行时用 66 CK_LOAD_OBJ_LIST 调
       用；或 4→2 临时选对象（如 2 Phone Book/4 Trunk Groups/8 Voice mail titulars，可带子对象）→执行时用
       65 Selected objects；节点列表（.ndl）同构（菜单 4→4→2 建、执行时节点选择 4 CK_NODE_LIST_RESTORE 或
       3 Selected nodes）。
  verification: |
    两节点编号计划/中继组互见；菜单 2 的 Results of the consistency checks 可复查各步结果；错误链式对象按
    "跑两遍"或部分审计解法处理。
  conditions: 直改数据库、旧数据不留；生产必须先模拟并备份全网库。
  tags: [lab, audit, firewall, ssh, consistency]

- id: c17
  title: Broadcast 启用与监控（激活三法、全局/对象行为、immediate broadcast、lupd.dat/LOG/prog_diff/maohist）
  type: lab
  source_pages: p487-498
  source_chapter: Broadcast
  source_quote: |
    "BEFORE ACTIVATING THE BROADCAST PROCESS, MAKE SURE THAT: INTERNAL FIREWALL ... SSHV2 KEYS ..." (p488)
    "(101)cs1> cleanbroad -all ... Successful Restart broadcast on node 1 ... on node 2" (p488)
    "(101)cs1> mao +br → Broadcast was inhibited -> Broadcast is activated" (p489)
    "ll LOG*.* → LOG.1.1 / LOG.2.1" (p494)
  steps: |
    1. 前提：同 audit（防火墙互信 + SSH 密钥）。
    2. 激活三选一（两节点都要）：cleanbroad -all（一条命令全网重置+重启，含清 LOG/RLOG、序号归零）；
       WBM System/Broadcast→Operational YES；mao +br（mao -a 看状态，mao -br 关）。
    3. 全局参数：System/Broadcast→核对 Broadcast Buffer Timer（LOG 落盘周期，默认 10 分钟）、Poll Timer、
       Maximum number of log files（≤127）、Broadcast Area Number（默认 -1）、Update all Behaviors 与全局
       出/入向行为（本实验保持默认）。
    4. 对象行为（信息性）：System/broadcast/broadcast objects 逐对象配出/入向。
    5. 监控演练：先 mao -lupd 双节点核对 log seq=0；两节点各做管理（NODE1 建 31033/中继组 10、NODE2 建
       31544）→ll cm_cb.sav 非 0；按 Immediate Broadcast→buffer 清零、生成 LOG.1.1/LOG.2.1 且互收到。
    6. 结果核对：NODE2 编号计划可见 31033（network number）、中继组 10 已同步；mao -lupd 两边 log seq 同
       步为 1。
    7. 内容审计：prog_diff -l EN0→1→输 LOG.2.1 看对象明细（Prefix Plan/Phone Book 创建记录）；菜单 2 查远
       端节点序号与 ERRLOG；菜单 3 广播历史；maohist -l EN0 看 MAO 修改史。
  verification: |
    跨节点对象互见、lupd.dat 序号一致、LOG 文件确认后删除仅留最新一条。
  conditions: trunk groups 本身不广播但中继组对象在实验中用于验证（广播的是编号计划/电话簿等对象）。
  tags: [lab, broadcast, cleanbroad, lupd, prog-diff]

- id: c18
  title: 组网双向溢出（Node Access Prefix 双向+权利+断链测试；判别器+ARS 双路由+时间路由+trkstat/trkvisu 验证）
  type: lab
  source_pages: p509-516, p524-536
  source_chapter: Private to public overflow / Public to private rerouting
  source_quote: |
    "Destination node number Enter the remote Node number ... Here, node N° 2 • Number to add Specify the
    local ARS prefix" (p511)
    "Busy priv. to public Overf. 1 ... O/S private to public overflow 1" (p513)
    "Call number 0110X415 ... ARS route list number 100 ... Route 1 ... Trunk group The value '-1'" (p526-527)
    "All virtual 'B channels' are FREE, so, no external call has been established through the public TG" (p535)
  steps: |
    [私到公溢出]
    1. 前提：双节点公网 SIP 中继正常；DID 段——NODE1 0210x41000-0210x41499、NODE2 0110x41500-0110x41999
       （x=POD 号）。
    2. NODE1 建远端节点前缀：Translator/External numbering plan/Node access prefix→Create→Destination
       node=2、Number to add=本地 ARS 前缀、Install N° last part=远端第三方 DID（非 DID 被叫用）、DID
       Translator Mode=Default DID mode；Node DID Translation→Create→First External=0110X41500、First
       Internal=31500、Range size=500、Unique internal number=No、Thin sector=No。NODE2 对称（node=1、
       0210X41000/31000/500）。
    3. 权利：两节点 COS→Busy priv. to public Overf.=1、O/S private to public overflow=1；确认外号未被闭锁。
    4. 测试：临时 Disable 一条直链接入（Inter-Nodes Links/.../Access Number）→互拨 31000↔31500→主叫屏显
       翻译后的外号、被叫屏显外部主叫 ID；trkstat 1（TG1 62 通道表）出现一个 B（Busy）即走公网成立→重新
       Enable 直链。
    [公到私重路由]
    5. 前提：闭锁规则已配（starter）；SIP 中继与直链正常；远端用户已是本地网络号（audit/broadcast 完成）。
    6. NODE1 判别器：Translator/External numbering plan/Numbering Discriminator/Discriminator Rule（选现
       用闭锁判别器，如 0）→Create→Call number=0110X415、ARS route list=100、Number of digits=10。
    7. ARS 表：ARS Route List→Create→100；Route 1→TG=-1、去 6 位、加 3、Called number source=route、
       Route type=Private、Quality=Speech；Route 2→TG=1、去 1 位、加 33、Numbering Command Tabl. ID=1、
       Route type=Public；Time-based Route List→1→route 1、2→route 2。
    8. NODE2 对称：Call number=0210X410、ARS=200、Route 2 用 TG=2/Tabl.ID=2。
    9. 测试：NODE1 拨 0 0110X41500——直链可用时外号被还原为内号，被叫显示主叫姓名；trkstat 1 全 F（未走公
       网）、trkvisu 2002 显示 1 通链上呼叫。
  verification: |
    两个方向的行为与通道占用状态（trkstat B/F、trkvisu 呼叫数）均符合预期；测试后恢复直链接入。
  conditions: 公到私重路由非 DID 不适用；-1 路由每表仅一条且须首位。
  tags: [lab, overflow, rerouting, ars, trkstat]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 21 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 集中式 IP Pod 配置 | 有 → c01 |
| task-02 SSH 免密体系 | 无独立 How-To 章（p55-68 为概念章）；操作序列已嵌入 c02 步骤 5、c05 步骤 10、c16 步骤 2（对机/全网两工具的完整命令口径齐备） |
| task-03 本地冗余部署 | 有 → c02 |
| task-04 空间冗余部署 | 有 → c03 |
| task-05 冗余维护与切换演练 | 有 → c02/c03 的 verification（role/twin/bascul）；概念语义在 framework f06 |
| task-06 不停机升级 | 无独立实验章（p83 概念 11 步，已收进 principle p11；本书无对应 How-To） |
| task-07/08 IP 域配置与验证 | 有 → c04 |
| task-09 PCS 部署 | 有 → c05 |
| task-10 PCS 救援与回切演练 | 有 → c06 |
| task-11 本地私到公溢出 | 有 → c07（书中明示 RLAB 不可执行，保留为参考规程） |
| task-12 速拨体系 | 有 → c08 |
| task-13 多线与监督键 | 有 → c09 |
| task-14 经理/助理组 | 有 → c10 |
| task-15 寻线/代接组 | 有 → c11 |
| task-16 办公桌共享 | 有 → c12 |
| task-17 多设备用户 | 有 → c13 |
| task-18 Direct IP Link 组网 | 有 → c14（Pod 迁移前置）+ c15（建链主实验） |
| task-19 Audit | 有 → c16 |
| task-20 Broadcast | 有 → c17 |
| task-21 组网双向溢出 | 有 → c18 |

**统计**：18 条全为 How-To 实验章转写；task-02/06 无独立实验章，其操作内容已并入相邻案例或原则条目（自检中已注明），21/21 任务均可溯源。
