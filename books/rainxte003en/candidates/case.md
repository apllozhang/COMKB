# 案例/实验/操作序列候选 — Rainbow OmniPCX Enterprise (RAINXTE003EN Ed12)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号）标注"实验口径"。
> 条目说明: 全书 14 个 How-To 实验章 → 14 条，一章一条（c01..c14 与章一一对应）。

```yaml
- id: c01
  title: Rainbow 账户配置与使用——管理员登录、手动建 user1、邀请建 user2 与协作测试
  type: lab
  source_pages: p60-65
  source_chapter: Rainbow Hub — Rainbow accounts configuration and use
  source_quote: |
    "Login : cCpP.admin@ale-training.com (C: class number ; P : pod number) — Password : Superuser-P*" (p61)；
    "Visibility Keep 'same as company'. The company is managed as private." (p63)；
    "CLICK ON 'JOIN BUTTON' AT THE BOTTOM OF THE E-MAIL AND NOT ON THE LINK AT THE BEGINNING." (p65)；
    "Perform the following tests: Place calls between two rainbow applications (users) — Share the
    computer's screen of one of the members — Send an IM messages between the two users" (p65)
  steps: |
    1. 浏览器打开 https://web.openrainbow.com，用客户公司管理员登录：cCpP.admin@ale-training.com /
       Superuser-P*（实验口径，C=班号、P=POD 号）；也可用 PC 端 Rainbow 应用做管理配置。
    2. 手动建成员：点 "Manage your company" → "My company" → "Members" → "Create"，填 Login =
       cCpP.user1@ale-training.com（实验口径）、Password = Superuser-P*（实验口径）、Sign-in method 保持
       默认（登录时问账号密码）、Visibility 保持 "same as company"（该公司按 private 管理）、
       Last name = Backman、First name = Billy、Subscription 暂留默认（Essential）、勾选 "Send enrollment
       email to new users"。
    3. 核验收信：登录培训邮箱 https://mail44.lwspanel.com/（用户名 = 该邮箱地址，密码 = PasswordP*，P=
       POD 号，实验口径）；Warning：检查 Rainbow 平台邮件没被当垃圾邮件（SPAM）。
    4. 邀请建成员：My company / Members → "Invitations" 页签 → 点 "Invite" → 输入
       cCpP.user2@ale-training.com（可一次邀多人）→ Continue → OK；账户保持 "invited" 状态直到用户
       接受并完成注册。
    5. 用户侧完成开户：登录其邮箱 → 点邮件内链接 → Warning：点邮件底部的 "JOIN BUTTON"，不要点开头
       的链接 → 设密码与必填信息（Last name = Rains、First name = Robby）。
    6. 行为测试（书中三项）：①两个 Rainbow 用户间互打呼叫；②一方共享电脑屏幕；③两用户间互发 IM。
  verification: |
    书中 Tests 节三项行为测试全通过：呼叫/屏幕共享/IM。书中提示：管理员也是公司成员，可直接用管理员
    账户当对端测试（p65 Tips）。
  conditions: 公司与 PBX 已由经销商/讲师创建（书中 Implementation 声明）；培训邮箱可用；注意 p216 的
    4059 实验对同一 user2 邮箱用了不同姓名（Betty Carol），书内前后不一致。
  tags: [lab, members, manual-creation, invitation, subscription]

- id: c02
  title: Pod 实验环境配置——虚机确认、机架板卡、IPDSP 用户、外部 SIP 网关、DID 翻译、外呼验证
  type: lab
  source_pages: p70-76
  source_chapter: Pod Configuration
  source_quote: |
    "Software Rack 3U (OMS) Rack N° 4 Virtual GD4 (slot 0) IP @: 192.168.1.13/24" (p72)；
    "Registration ID pbxN (where N is your POD number) … Outgoing username pbxN" (p73-74)；
    "First external number 33210N41000 (where N is your POD Number) … First internal number 31000 …
    Range Size 500" (p75)；
    "To make sure that access to public SIP carrier is working properly, set up some outgoing calls." (p75)
  steps: |
    1. 确认 6 台虚机默认已启动（RLab 仪表盘看 OXE/OMS/FlexLM/WebRTC/Client 10/11）。
    2. 核对预配基线：XE 虚机已恢复软件许可、FlexLM（192.168.1.80）已声明、DHCP 已启用（地址池
       192.168.1.145-.149）、机架板卡已建、话机与软电话用户已建、语音指南已下载、公共 SIP trunk group
       已建（实验口径）。
    3. 核对主站设备：Software Rack 3U (OMS)，Rack N°4，Virtual GD4（slot 0）IP 192.168.1.13/24，MAC
       00:50:56:01:01:13（实验口径）。
    4. 核对用户：31000 Alan Barkley（IP DSP，装在 PC Client 10）、31001 Billy Backman（IP DSP，装在
       PC Client 11）；在 IPDSP 上右键 Settings → Network 页签填 TFTP 服务器 IP = OXE CS 主 192.168.1.3
       （实验口径）。
    5. 外部 SIP 网关按 POD 号配 2 个参数（公共 SIP trunk 已预配）：Registration ID = pbxN、Outgoing
       username = pbxN（N=POD 号，如 POD 3 → pbx3）。
    6. DID 翻译对齐 POD 号：Translator/External Numbering Plan/Default DID num. translator → Create：
       First external number = 33210N41000（N=POD 号，如 POD 3 → 33210341000）、First internal number =
       31000、Range Size 500。
    7. 做几通外呼验证公网 SIP 载体正常（用法见 SIP Carrier Simulator 文档）。
    8. 核验培训邮箱：https://mail44.lwspanel.com/，三个信箱 cCpP.admin / cCpP.user1 / cCpP.user2 密码均
       PasswordP*（实验口径）；清空旧邮件保持干净基线。
  verification: |
    书中验收：外部呼叫打通（"set up some outgoing calls" 后公网载体可达）；邮箱三账号均可登录。
  conditions: RLAB 环境；OXE 数据库已预配（许可/DHCP/机架/用户/trunk）；全部 IP/账号为实验口径。
  tags: [lab, pod, oxe, sip-trunk, did, lab-environment]

- id: c03
  title: OXE 呼叫服务器 DNS 与 HTTP 代理配置及连通性测试
  type: lab
  source_pages: p77-82
  source_chapter: DNS and proxy configuration
  source_quote: |
    "The DNS and HTTP proxy configuration will only be used by Rainbow and Cloud Connect agents" (p78)；
    "URL PING DOESN'T VALID THE DNS RESOLUTION. Dig and nslookup commands allow to verify correctly the
    DNS resolution." (p82)；
    "The request is OK but curl returns a message to indicate that the web server certificate cannot be
    verified. … The certificate provided by the agent.openrainbow.com is an ALE proprietary certificate
    only recognized/accepted by an OXE/OXO system." (p82)
  steps: |
    1. DNS 配置：netadmin 菜单用 "netadmin -m" 命令 → 选 14 'DNS configuration' → 选 2 'Create/Update
       DNS setup' → Primary DNS = 192.168.1.250、Secondary DNS = 10.20.30.250（实验口径）。
    2. DNS 核查：DNS 菜单选 1 'View DNS configuration'，显示 Primary/Secondary 地址即为生效。
    3. DNS 删除（了解即可）：选 3 'Delete DNS Details'，输 y 确认。Warning：实验中不要真删刚配的配置。
    4. HTTP 代理配置：netadmin 选 15 'Proxy configuration' → 选 2 'Create/Update Configuration' → 填
       Host address（例 10.20.30.253）、Proxy port（例 3128）、代理账号密码。Warning：RLAB 环境上外网
       不需要代理，此步仅了解。
    5. 代理核查/删除：选 1 'View HTTP Proxy Configuration' / 选 3 'Delete HTTP Configuration'。
    6. DNS 测试：console 或 putty 执行 nslookup agent.openrainbow.com 192.168.1.250——Warning：URL
       ping 不能证明 DNS 解析，要用 nslookup/dig；书中输出解析到 178.32.173.187 等 4 个 IP。
    7. HTTP 测试：curl https://54.38.162.129 —— 返回 (77) 证书校验错误属预期：agent.openrainbow.com
       用 ALE 专有证书，只有 OXE/OXO 认；Warning：OXE 只能用 IP@ 做 HTTPS 测试，现场若防火墙/代理要求
       域名则此测可能做不了。
  verification: |
    nslookup 返回 agent.openrainbow.com 的解析结果；curl 虽报证书错误但请求 OK（p82 注释明说 "The
    request is OK"）；checkCloudConfig.sh -rainbow 的 DNS 测试段可交叉验证（p87）。
  conditions: c02 完成（Pod 可用）；netadmin 菜单编号 14=DNS、15=Proxy、20=Apply modifications。
  tags: [lab, dns, proxy, netadmin, connectivity]

- id: c04
  title: OXE 接入 Rainbow——凭证获取、webadmin 激活、双侧状态核验与四抓手维护
  type: lab
  source_pages: p83-88
  source_chapter: OXE connection with Rainbow
  source_quote: |
    "Warning NETWORK PREREQUISITES MUST BE COMPLETED BEFORE!" (p84)；
    "Enable Rainbow Agent Yes … Rainbow PBXID The Rainbow ID is generated by Rainbow. It will be provided
    by the rainbow administrator." (p85)；
    "Verify that OXE is 'running'" (p86)；
    "(1)csa> dhs3_init -R RAINBOWAGENT … (1)csa> checkCloudConfig.sh -rainbow … (1)csa> more
    /var/log/rainbowagent.log" (p87-88)
  steps: |
    1. 前置：网络前提（c03）必须先完成（Warning）。
    2. 登录 Rainbow 客户端（公司管理员 cCpP.admin@ale-training.com / Superuser-P*，实验口径），核对该
       管理员有 Enterprise 许可。
    3. 取凭证：My company / Communication → "Comm. Servers" 页签 → 点该 OXE → 记下 PBXID 与激活码
       （Tips：用复制功能防输错）。
    4. OXE 侧激活：OXE webadmin（或 mgr）→ Rainbow 菜单 → Enable Rainbow Agent 选 YES → Rainbow domain
       保持默认 → 填 Rainbow PBXID 与 Activation code → Save。
    5. 连接状态核验（双侧）：OXE 侧看 Rainbow 菜单连接状态；Rainbow 侧 My company / Communication →
       "Comm. Servers" 页签确认 OXE 为 "running"。
    6. 维护①启动事件：mtcl 账户 incvisu —— 五链路事件码 4503 WebSocket / 4505 XMPP / 4509 CSTA /
       4507 Config / 4511 API_MGT 应全部 in service。
    7. 维护②重启 agent：dhs3_init -R RAINBOWAGENT。
    8. 维护③配置核查：checkCloudConfig.sh -rainbow（测 openrainbow.com:443 与 netadmin 代理，输出含
       DNS 解析、openssl 证书链、"Success !!"）。
    9. 维护④日志：more /var/log/rainbowagent.log（书中样例版本 rainbowagent Version 6.0.1）。
  verification: |
    Rainbow 管理端 Comm. Servers 显示 OXE "running"（p86）；checkCloudConfig.sh 输出 "Success !!"
    （p88）；incvisu 五链路 in service（p87）。
  conditions: c03 完成；PBX 须已由经销商在 Rainbow 侧创建（实验中预置）。
  tags: [lab, rainbow-agent, pbxid, activation, webadmin, maintenance]

- id: c05
  title: OXE 设备关联 Rainbow 账户与 RCC 五项测试
  type: lab
  source_pages: p89-93
  source_chapter: Assign an OXE device to a Rainbow user account
  source_quote: |
    "cCpP.admin@ale-training.com <-> device 31000 … cCpP.user1@ale-training.com <-> device 31001" (p90)；
    "This number will be retrieved later for WebRTC gateway use. It will be automatically configured in
    Remote Extension number by the Rainbow agent (e.g. BBB10070254106463346) when the user selects
    'computer' as routing" (p91)；
    "Is it possible? … Is it possible to take the call from Rainbow client interface? Which action(s)
    is/are possible?" (p92)
  steps: |
    1. 管理员登录 Rainbow → Manage your company → My company → Members → 选成员。
    2. 关联设备：选 "Telephony" 页签 → "Device" 字段选 OXE → 选分机号 → Apply。书中关联对：admin ↔
       31000、user1 ↔ 31001（实验口径）。
    3. 观察关联后新增的 "Rainbow number" 字段（示例 BBB10070254106463346）：它是 WebRTC 网关阶段用的
       隐藏配置，用户选 "computer" 路由时由 Rainbow agent 自动写入 Remote Extension number，无需手工。
    4. RCC 测试①呼出至 OXE 用户：用关联 31000 的 Rainbow 客户端，路由选 "Office phone"，呼叫 31001
       —— Is it possible?
    5. RCC 测试②外呼公网号：用 Rainbow 客户端打公网号（经 SIP 模拟器），例 0210P41001（P=POD 号）
       —— Is it possible?
    6. RCC 测试③来话：从 31001 打 Barkley 的 31000 —— 能否从 Rainbow 客户端界面接起？可用动作
       （接听/挂断/转移等）有哪些？
    7. RCC 测试④呼出至纯 Rainbow 用户：搜此前建的"纯"Rainbow 用户（user2），尝试呼叫 —— Is it
       possible?
    8. RCC 测试⑤纯 Rainbow 用户呼入：用 user2 的客户端呼叫 Barkley —— Is it possible?
  verification: |
    书中五项测试问题（p92-93）逐项记录结论；本阶段口径：RCC 模式音频全在话机，Rainbow 仅监督。
  conditions: c04 完成（PBX 已接 Rainbow）、c01 完成（账户已建）。
  tags: [lab, rcc, extension-association, telephony]

- id: c06
  title: 远程延伸（REX）配置——Ghost Z 池、REX 声明、multi-line、tandem、溢出、订阅与 Nomadic 测试
  type: lab
  source_pages: p119-130
  source_chapter: Remote extensions configuration for Rainbow integration
  source_quote: |
    "Refer to TC2462" (p121)；
    "A ghost device is required per simultaneous call to a REX." (p122)；
    "Configuration is done on one device: the main one. It will be automatically reported on the secondary
    one." (p125)；
    "Select 'Other phone' as routing and specify an external number … Is it working? What is the calling
    number displayed on 31001 device? Consult the number automatically managed in OXE for the REX." (p130)
  steps: |
    1. Ghost Z 系统参数：System/Other System Param./Local Features Parameters —— "Entity for OG calls to
       REX users" 与 "Rex Entity to be used in ARS" 两参数勾选（true）。
    2. 建 Ghost Z：Users → Create：Directory Number = DB1000（建议用字母 A/B/C/D 开头优化拨号计划）、
       Directory name = Ghost1、Shelf/Board/Equipment Address = 255、Set Type = Analog、不可按名呼叫；
       Facilities 页签勾 Ghost Z + Ghost Z Feature = Remote extension。每路 REX 并发呼叫需一个 Ghost。
    3. 声明 REX：Users → Create：Directory Number = 21<主号>（编号计划 prefix<主 set 的 QMCDU>，如
       2131000）、Directory name = Barkley、First name 用 "rex" 区分主站、Set Type = Remote extension、
       不可按名呼叫（当 REX 非用户主站时）。
    4. 配 multi-line：Users/Prog. Keys —— 给 31000 与 2131000 各配至少 2 条 multi-line（选空闲键，功能
       Multi-line，目录号=本机号，助记 L1）。tandem 成员分机必须有 multi-line。
    5. 声明 tandem：选主站 31000 → "Assoc. Sets" 页签 → Tandem Directory Number = 2131000（副站 REX）+
       Main set in the tandem 勾选（配置只在主站做，自动同步副站）。
    6. 溢出①主站失效：System/Other System Param./System Parameters 勾 "Overflow to sec tandem if main
       OOS"；用户 Phone Features COS 勾 Forward if set is out of service、Ring all its secondary if main
       oos，并按需设 Remote Extension Activation（=1 允许系统激活 REX）/Deactivation（=0 禁用户自行停用）。
    7. 溢出②无应答：用户实体 Overflow timer（步进 100ms，例 150=15 秒）；COS 勾 Overflow on no answer to
       associate 与 Cancel Overflow to associate；主设备 "Associated Sets" 页签 Associated Set No. = 留言
       信箱号（如 31499）。
    8. 订阅：给 Admin（Barkley）与 Backman 都分配 Enterprise 订阅（web.openrainbow.com → My company /
       Members → Services 页签 → Enterprise → Apply）——Essential 只能 RCC 不能改路由。
    9. Nomadic 测试①外呼：Rainbow 客户端（关联 31000）路由选 "Other phone" 填外部号（例 0210P12345，
       P=POD 号）→ 呼叫 31001 —— Is it working? 31001 上显示的主叫号是什么？查 OXE 中 REX 自动管理的
       号码。
    10. Nomadic 测试②来话：再配 "Other phone" 外部号 → 从 31001 呼叫 31000 —— 会发生什么？从"外部"
        设备接听。
    11. Nomadic 测试③档案：用户档案配 Professional mobile = 0610P12345、Home phone = 0210P12345、
        Personal mobile = 0710P12345（实验口径）；逐个改路由验证来话/去话，并查每次选择下 REX 的自动
        号码。
  verification: |
    p130 三步 Nomadic 测试 + 每次路由选择下用 remotesets 查 REX 号（对照 p14 路由四案例矩阵：无手机号
    →REX 空；专业手机→双响；个人手机→双响；两者都配→专业优先）。
  conditions: 参考 TC2462；tandem 两端 multi-line 必需；本实验为后续 WebRTC 网关的路由地基。
  tags: [lab, rex, ghost, tandem, overflow, nomadic, tc2462]

- id: c07
  title: WebRTC 网关部署与配置——文档下载、VM 配置（mp 命令族）、核验、Rainbow 激活与排障
  type: lab
  source_pages: p153-162
  source_chapter: Deploy and configure a WebRTC gateway
  source_quote: |
    "Warning THE PBX MUST BE CONNECTED TO RAINBOW • USERS DECLARED IN THE RAINBOW COMPANY MUST HAVE THEIR
    OXE TELEPHONE NUMBER ASSOCIATED TO THEIR RAINBOW ACCOUNT" (p154)；
    "mpconfig --PBX_DOMAIN=\"192.168.1.3\" --PBXID=\"XXXX-…\" … RAINBOW_DOMAIN=\"openrainbow.com\" …
    TURN_SERVER=\"GEOIP\" … WRTRANGE=\"20000-29999\" SIPRANGE=\"30000-39999\"" (p157-158)；
    "In Rainbow Administration, the WebRTC gateway option in PBX settings must be activated by the BP
    administrator." (p161)
  steps: |
    1. 下载官方文档（现场必用）：WebRTC Gateway Installation Guide、WebRTC Gateway Command List、
       Upgrade Guide（Remote+本地）、TC2462（MyPortal/ partners 链接）。
    2. 下载虚机：MyPortal "Taxonomy"（OmniPCX Enterprise / OXO Connect / OXO CE 任选——Tips：同一软件）。
       RLAB 中镜像已部署。
    3. 键盘：首次启动用 VM console 以 kb/kb 登录改键盘（模板默认 QWERTY）。
    4. 网络配置：以 rainbow/Rainbow123（实验口径）登录 → mpnetwork --IP=192.168.1.15
       --NETMASK=255.255.255.0 --GATEWAY=192.168.1.254 --DNS=10.20.30.250,192.168.1.250
       --HOSTNAME=webrtc --HOSTDOMAIN=company.com --NTP=10.20.30.250 → 确认 y → sudo reboot（实验口径）。
    5. PBX 参数：mpconfig --PBX_DOMAIN="192.168.1.3" --PBXID="<PBXID>"（实验口径 OXE IP 192.168.1.3；
       Tips：mpssh on 开 SSH 后用 putty 粘贴 PBXID，PBXID 从 web.openrainbow.com → My company /
       Communication / Comm. servers / <OXE> 复制，BP 账户亦可）；确认输出中 RAINBOW_DOMAIN=
       openrainbow.com、TURN_SERVER=GEOIP、WRTRANGE=20000-29999、SIPRANGE=30000-39999 → sudo reboot
       （书中示例 PBXID：PBX834e-41da-086b-450a-8a14-4914-bef0-36b8）。
    6. 配置核查：mpshow（版本与全量配置，书中样例 Rainbow WebRTC Gateway 1.78.11-470、
       janus-gateway-mediapillar / otlitemediapillargateway 1.77.6、1995 MiB RAM / 4 GiB Disk）；
       mpcheck（DNS 测试、Rainbow connect 多 IP、TLS、STUN/TURN GEOIP、PBX_DOMAIN ping、SIP OPTIONS
       siptest、registration traceroute——实验输出中 GEOIP 段 [FAILED] 属 GEOIP 文件缺失，先确认
       Rainbow connect 段 OK）。
    7. OXE 侧配置：SIP、ARS、Remote extensions 按专门 How-To（c06/c09）。
    8. Rainbow 侧激活：BP 管理员登录 → Customer companies / <company> / Communication / Comm. servers /
       <OXE> → 勾 "Activate WebRTC gateway"。Warning：实验账号是 customer administrator 无此权限，由
       讲师操作。
    9. 排障：mpcheck 八段输出逐段看；三服务状态/重启——sudo service otlitemediapillargateway /
       janus-gateway-mediapillar / kamailio status|restart；更多见 TC2462。
  verification: |
    mpcheck 各段 [OK]（除实验环境 GEOIP 段）；Rainbow 端该 OXE 网关状态启用；OXE 侧 VoIP 测试由 c09
    第 7 节承接。
  conditions: c04（PBX 已接）+ c05（分机已关联）为 Warning 级前提；c06 的 REX/ARS 为 OXE 侧配套。
  tags: [lab, webrtc-gateway, deployment, mpnetwork, mpconfig, mpcheck, bp-activation]

- id: c08
  title: WebRTC 网关升级——远程升级优先（BP Webadmin）与手动升级（mpupgrade）
  type: lab
  source_pages: p172-176（讲义 p163-171）
  source_chapter: WebRTC gateway upgrade
  source_quote: |
    "Update your WebRTC gateway with the REMOTE UPGRADE METHOD via Rainbow, if available. Otherwise,
    perform the update manually. … This method is performed by a Business Partner administrator account" (p173)；
    "Use WinSCP to transfer the following files into the 'Upgrade' folder … Transfer iso and iso.md5 files" (p175)；
    "If WebRTC gateway upgrade does not work, follow the procedure to solve the problem" (p176)
  steps: |
    1. 远程升级（优先，BP 账户）：以 BP 管理员登录 Rainbow → PBX 列表看新版本可用 → 按官方文章
       （23160518410898）执行：Equipment information / WebRTC GW 页签 → Upload（接受出口管制条款；下载
       中断/被代理拦截时出现 Abort 按钮可取消重下）→ 完成后点 Upgrade 确认 → 结束自动重启 → 查状态与
       版本。注意：无显示器/键盘可能起不来的独立 PC 已被排除在远程升级之外（升级后起不来的责任在操作者）。
    2. 手动升级①查新版：从 Client PC 访问 MyPortal（用自己账号）→ Portfolio explorer / Cloud
       Communications / Rainbow → 下载新版（填表）。
    3. 手动升级②解压并开 SSH：Client PC 上解压（OVF 目录内 iso 与 iso.md5）；WebRTC VM console 执行
       "mpssh on"。
    4. 手动升级③传输：WinSCP（协议 SFTP，主机 192.168.1.15 端口 22，登录 rainbow/Rainbow123，实验口
       径）→ 把 iso 与 iso.md5 传到网关根目录下 Upgrade 文件夹。
    5. 手动升级④执行：按官方文章（23159902243218）完成——mpupgrade 并确认 YES（可 -now 立即或
       -delay=30s 延迟），过程自动；完成后 mpcheck 验证配置恢复且已连 Rainbow 云。
    6. 失败处理：升级不工作（如重启后仍是旧版）按文章 15470672923794 处理。
  verification: |
    升级后 mpcheck 显示网关运行正常且已连 Rainbow；版本号更新（mpshow）。讲义口径：远程法适用 1.73.x+
    （35 国清单见文章）、手动法适用 1.67.6-121 起（p164）。
  conditions: 远程法需 BP 账户；独立 PC（无显示/键盘不自启）禁远程升级；出口管制条款须接受。
  tags: [lab, webrtc-gateway, upgrade, mpupgrade, winscp, remote-upgrade]

- id: c09
  title: OXE 侧 WebRTC 网关配置九件套——SIP TG、可信 IP、Rainbow type 网关、IP 域、CDT/ARS/BBB、判别器、回调、CPaaS 补充与 VoIP 测试
  type: lab
  source_pages: p177-197
  source_chapter: OXE configuration for WebRTC gateway use
  source_quote: |
    "AN IP DOMAIN WITHOUT COMPRESSION BUT WITH COMPRESSION RESOURCES (GD/OMS) IS REQUIRED ON THE SYSTEM
    FOR A CORRECT WORKING MODE OF THE WEBRTC GATEWAY." (p180)；
    "Gateway type Rainbow type … Trusted From header Checked (true) … Support G711 YES" (p181)；
    "Number of Digits 17 (length of numbers managed by the Rainbow agent)" (p185)；
    "Using Rainbow client (with account linked to device 31000): • Select 'Computer (VoIP)' for routing …
    Is it possible? What is the caller identity displayed on 31001 device?" (p196)
  steps: |
    1. 国家码：System / Other System Param / Signaling String / SG Country Code（例 33 法国）。
    2. SIP trunk group：Trunk Groups → Create：TG IP = 5、Type = T2、Name = WebRTC、Q931 Signal variant =
       ISDN all countries、T2 Specification = SIP。
    3. IP 域前提（Warning）：网关正常工作要求系统有一个"无压缩但有压缩资源（GD/OMS）"的 IP 域——IP /
       IP domain / 域 0：Intra/Extra domain bandwidth = High bandwidth（无压缩）。
    4. 可信 IP：SIP / Trusted IP Addresses → Create：192.168.1.15（网关 IP，实验口径）。
    5. SIP 外部网关：SIP / SIP Ext Gateway → Create：ID 5、名 WebRTC Gateway、SIP Remote domain =
       192.168.1.15、端口 5060、UDP、监督定时器 380、trunk group 5、SDP in 18x 不勾、最小认证 SIP None、
       Contact with IP 不勾、DTMF 载荷 101、Gateway type = Rainbow type、Trusted From header 勾、支持无
       SDP Re-invite 勾、CSTA U2U=NO、Domain 0 或 -1、G722 NO / G711 YES / G729 NO（全表实验口径）。
    6. ARS 六步：①CDT——Translator / Automatic Routing Table / Numbering Command Table：表 5、Command I
       挂外部 SIP 网关 5（CDT 是 ARS 用 SIP TG 的前提）；②ARS Route List 5 "WebRTC Gateway"，Route 1
       用 TG 5 + CDT 5 + UDI；③Time-based Route List 1 → Route 1；④ARS 前缀 BBB——Translator / Prefix
       Plan：Number BBB、Meaning ARS、判别器号=含 Ghost Z 与用户实体的逻辑判别器；⑤实判别器——
       Translator / External Numbering Plan / Numbering Discriminator：5 号 "WebRTC Gateway"，规则
       Call Number 1 / Area 1 / ARS route list 5 / schedule -1 / 位数 17；⑥逻辑-实判别器关联——
       Entities / <用户与 Ghost Z 实体> / Discriminator Selector：Discriminator 5 = 5。
    7. 回调：Applications / CSTA：Set Callback On Calling Device = Yes；Translator / External Numbering
       Plan / Ext. Callback Translation Table：表 5（国家码 33 France），规则 Basic Number = DEF、删除
       0 位、追加 BBB；建专用实体 50 "WebRTC Gateway"（External Callback Table = 5）；把网关专用 TG 挂
       到该实体（Local trunk group settings → Entity Number = 50）。Tips：把 REX 里的 BBB 号设缩位拨号
       可从 OXE 话机直拨验证到 Rainbow 客户端。
    8. CPaaS 补充（仅当公司含纯 CPaaS 用户）：①用户 Phone Features COS 勾 Calling name display
       (CNIP/I-CNAM)——让非关联 OXE 设备的 Rainbow 呼叫正确显示主叫名；②Applications / Remote Extension
       Parameters：CLI Format（Standard Plan=外呼送外部号 / Private Plan=送内部号）；③System / Other
       System Param. / External Signalling Parameters：NPD for external forward（例 10）。
    9. 维护：sipextgw -l 看外部 SIP 网关在服/退服；lookars i 交互式验 ARS（输 BBB+分机看路由表解析）；
       抓包 motortrace 3 + traced（可 traced > /tmp/WebRTC_SIPlog），停 traced 用 killall traced；
       multidevice <号> / zdpost d <号>（|grep tyterm）/ remotesets d <号> 验 tandem/multi-device 与 REX
       的 BBB 号；其他命令 remotesets |grep、remoteview、compvisu eqt all、represent、cnx dom。
    10. VoIP 测试①呼出：Rainbow 客户端（关联 31000）选 "Computer (VoIP)" 路由 → 查该用户 REX 管理的
        号码 → 呼 31001 —— Is it possible? 31001 显示的主叫身份是什么？
    11. VoIP 测试②来话：从 31001 打 31000 —— 有哪些动作？能否从计算机接听？
    12. VoIP 测试③呼出至 CPaaS 用户：搜"纯"Rainbow 用户 Robby Rains 并呼叫 —— Is it possible?
    13. VoIP 测试④CPaaS 用户呼入：用 Robby Rains 呼叫 Barkley —— Is it possible?
  verification: |
    p196-197 四项 VoIP 测试逐项记录；lookars i 输出应显示 Prefix BBB → Discri 5 → Route List 5；
    remotesets 显示 Active ExtNbr = BBB 开头 17 位号。
  conditions: c06（REX/Ghost/ARS 基础）+ c07（网关已部署并激活）为前提；参考 TC2462。
  tags: [lab, webrtc-gateway, sip, ars, discriminator, callback, cpaas, maintenance]

- id: c10
  title: 4059EE 话务台交付——话务组、话务台、CDT、安装连接、Rainbow 集成与 BLF 状态差异测试
  type: lab
  source_pages: p206-224（概览 p198-205）
  source_chapter: Call distribution and attendants
  source_quote: |
    "Physical Directory No. A0000 … Name GROP1 … Max. No. of Calls Bef. Overfl. 5" (p208)；
    "WARNING: This extension must not be multi-line, as it will be associated to the 4059 IP attendant" (p209)；
    "Device … e.g. B0000@192.168.1.3" (p213)；
    "Warning Don't confuse the Rainbow (presence) status with the telephone status. They are (can be)
    different." (p221)
  steps: |
    1. 建话务组：OXE WBM → /Attendant/Attendants group → Create：Physical Directory No. = A0000、
       Attendant group Id = 0、Name = GROP1、Max. No. of Calls Bef. Overfl. = 5、No display Threshold on
       4059 list = 6（溢出号按 Day/Night/Mode1/Mode2 状态填）。建组即自动生成对应 Call Distribution
       Table。
    2. 建话务台：/Attendant/Attendant sets → Create：Physical Directory No. = B0000、Attendant Id = 0、
       Group Id = 0、Shelf/Board/Equipment = 255、Set Type = 4059 IP、Associated phone set = 31002
       （Carol Betty 的 IPDSP，实验口径）。Warning：该分机不能是 multi-line（与 4059 IP 话务台不兼容）；
       4059EE 只管话务不管话音，必须关联物理话机或 IPDSP。
    3. 个人话务呼叫前缀：/Translator/Prefix plan → Create：Number = 31401、Meaning = Indiv. Attendant
       Call、Information = Attendant id。
    4. 电话簿：/Phone Book → Create：31401 = Welcome Desk、Phone Book Serv. No.、可按名呼叫 Yes（让来话
       显示话务员名）。
    5. 系统参数：/System / Other System Param. / Attendant Parameters：4059 Close auto sign off = True
       （应用关闭/PC 断电自动签退、话务台转夜服）；4059: PC unregistered at logoff = True（登出即抹除
       PC 身份，任意 PC 可再登录；False 则锁定原 PC 的 MAC）。
    6. 启用 IPDSP：启动 IPDSP 输 31002。Warning：必须先 in service 再从 4059EE "connect"。
    7. 装 4059EE：PC_CLIENT_11 装 4059EE_x.x.x.x.exe——选 Custom、勾装 Rainbow agent、不装 ALCATEL USB
       键盘（RLAB 虚机口径）；防火墙放行 4059 EE 应用与 abcacom.exe（培训语境可整体关防火墙）；以管理员
       运行改设置。
    8. 配 PCX 连接：Settings → Show settings → System Settings – PCX Connection → Connection → 右键列表
       Add → Device = B0000@192.168.1.3（设备=[话务员号]@[主机名]；冗余/备份呼叫服务器最多 3 个主机名，
       逗号或分号分隔）。
    9. 核验注册：/Attendant/Attendants sets/Ip phone Attendant 选 B0000——终端以太网地址（MAC）与 IP
       在设备连上 CS 后自动更新。
    10. 签入：4059 EE 应用 → File → Sign on；此后关联的 IP 用户承载 4059EE 的话音。
    11. 实体 CDT：Entities → Entity 1 → 1rst Day Routing = A0000（日间状态来话进话务组）。
    12. 核对 Attendant Call 前缀：Translator/prefix plan——按国家码默认存在（法国 9 / 美国 0）。
    13. 建话务员 Rainbow 成员：My company / Members → Create：cCpP.user2@ale-training.com / Superuser-P*
        （实验口径；姓名 Betty Carol——注意与 p64 的 Rains Robby 同邮箱不同名，书内不一致）。
    14. 4059 关联 Rainbow：4059 EE → Settings → Show settings → User → Rainbow 子菜单：输账户凭证、勾
        "Search in Rainbow"；需代理时在 System 设置的 Rainbow 菜单里配。
    15. 加联系人：用该账户登录 web.openrainbow.com → Contacts → Invite 邀请全员（被监督成员必须在话务
        员账户联系人列表里；4059EE 端亦可加，需先启用 BLF）。
    16. 服务测试：重启 4059 → 搜 Barkley → 看左侧 Rainbow 信息（公司名/邮箱/在场）→ 用户侧改状态验证
        话务侧实时更新 → 右键信息行发 Rainbow IM 并在用户侧查看。
    17. BLF：Settings/General → Enable Busy Lamp field 勾选；右键 BLF 面板 → Add item → User → 输姓名
        与分机（例 Alan Barkley 31000）→ plus → OK。
    18. 状态差异测试①：把 Barkley 的 Rainbow 状态改成 "Do not disturb"，确保其话机空闲 → 话务台上两条
        信息应不同（Rainbow=DND / 电话=free）。
    19. 状态差异测试②（反向）：Rainbow 状态设 free，让用户摘机/通话 → 话务台上两条信息应不同。
  verification: |
    p223-224 两条状态差异测试的"两边信息不同"结论；p220 在场实时更新与 IM 互通。
  conditions: 参考 TC2462；4059EE 安装包与 Rainbow agent 随装；Attendant 订阅与 4059EE 无关（p200）。
  tags: [lab, 4059ee, attendant, cdt, blf, rainbow-integration]

- id: c11
  title: Rainbow Attendant Console——订阅 ATTENDANT、分配、监督组与互助组创建
  type: lab
  source_pages: p238-244（概览 p225-237）
  source_chapter: Attendant console and Mutual aid supervision groups
  source_quote: |
    "Companies/Customer companies/ <company to manage> 'Subscriptions' section / Service : ATTENDANT …
    Choose the subscription offer: Attendant Monthly … DON'T USE 'PREPAID' IN THE TRAINING" (p239)；
    "'Communication' section / 'Supervision' tab — Click on 'Create' … Type Mutual aid group • Lock the
    last member Yes/no" (p243)
  steps: |
    1. 订购 ATTENDANT：Companies/Customer companies/<目标公司> → "Subscriptions" 区 → Service:
       ATTENDANT → 点 "Subscribe to offer" → 选 Attendant Monthly（培训禁 Prepaid）→ 许可数 1 →
       Subscribe。
    2. 分配订阅："Members" 区 → 编辑成员（例 cCpP.user1@ale-training.com）→ "Services" 页签 → 选
       "Attendant Monthly"。
    3. 建监督组：Companies/Customer companies/<目标公司> → "Communication" 区 → "Supervision" 页签 →
       点 "Create" → 填 Name、Description → 选监督员（须持 ATTENDANT 订阅，例 user1）→ 勾选被监督成员
       （公司其余用户）→ 点 "Create"；以 user1 登录即可监督组员。
    4. 打开话务台：以 user1 登录 web.openrainbow.com 或应用 → 点入口图标进 Attendant console（界面：
       监督组页签 + BLF 区 + 呼叫队列 OXE 10 路 + 呼叫控制；三种显示格式 Normal/Small/Condensed）。
    5. 建互助监督组：同上路径点 "Create" → 填 Name、Description、Type = Mutual aid group、Lock the last
       member（Yes/No，锁定最后一名成员不可退出）→ 加监督员 cCpP.admin@ale-training.com（实验口径）→
       勾选被监督成员——这些成员必须有物理分机或已关联的 PBX 软终端（IPDSP/MicroSIP）；以 admin 登录
       监督。
  verification: |
    user1 能打开控制台并看到监督组页签/BLF/队列（p242）；互助组行为口径见讲义 p234-236：一键 Join/Leave、
    临时纳排成员、同时最多监督 4 路、代接仅对 PBX 电话呼叫有效、锁定成员不能退出。
  conditions: 监督员与被监督成员须同组（管理员建组）；Attendant 功能仅 PC 端可用；话务员须有电话线与
    VoIP 软终端能力。
  tags: [lab, attendant, supervision-group, mutual-aid, subscription]

- id: c12
  title: Rainbow for Teams 安装——应用上架、权限同意两法与 Azure 核验
  type: lab
  source_pages: p285-293（概览 p270）
  source_chapter: Rainbow for Teams installation
  source_quote: |
    "Teams admin center web interface — Using following URL: https://admin.teams.microsoft.com" (p286)；
    "To give to users the possibility to install it, the status must be 'Allowed' … click on 'Upload new
    app'" (p287)；
    "Click on the 'Review permissions and consent' button … Click on 'Accept'" (p290)；
    "We see here that these permissions have been added and that they have been granted by the
    administrator." (p293)
  steps: |
    1. 浏览器打开 Teams 管理中心 https://admin.teams.microsoft.com，选/输管理员账户登录。
    2. "Teams apps" 菜单 → "Manage apps" 子菜单 → 搜索 Rainbow：若 "Release Status" 为 "--" 表示属微软
       第三方应用；用户可自行安装的前提是状态为 "Allowed"。
    3. 若搜不到（不在默认目录）：点 "Upload new app" → Upload → 选应用 zip 包 → Open → 关闭"已添加"提示
       窗；此后状态 "published"，默认 "Allowed"。
    4. 权限同意方式 A（推荐，最简且最合理——用户登录 Teams 时不再弹权限确认）：点 Rainbow 应用 →
       "Permissions" 页签 → 点 "Review permissions and consent" → 按需选管理员账户 → 点 "Accept"。
    5. 权限同意方式 B（方式 A 未做时）：管理员首次在 Teams 内打开 Rainbow 应用点 "Sign in"，弹权限确认时
       勾"代表整个组织"的选项后同意（为自己与全组织验证权限）。
    6. Azure 核验：管理中心 → Rainbow 应用 → "Permissions" 页签 → 点 "Go to Azure Active Directory" →
       新开页签进 Azure 管理界面（Teams 管理员兼有 Azure 权限则直连）。
  verification: |
    Azure 页面显示 "Rainbow for Teams" 应用所需权限已添加、且由管理员授予（p293）。
  conditions: Teams 管理员账户；应用不在目录时需 zip 包；Azure AD 租户可用。
  tags: [lab, teams, installation, permissions, azure-ad]

- id: c13
  title: Teams 集成用户配置——账户-PBX 关联、Telephony 权限收敛、Business/Enterprise 订阅
  type: lab
  source_pages: p294-298
  source_chapter: Rainbow user configuration for Teams integration
  source_quote: |
    "Select the PBX from the list ('Device' field) and the Extension number. Then click to 'Apply'" (p296)；
    "it is better to apply a restrictive permission to users with Teams integration in order to forbid
    collaboration services from Rainbow. … Select the required permission: Here 'Telephony'" (p297)；
    "For Rainbow integration with Teams, a Business or Enterprise subscription is required." (p298)
  steps: |
    1. 账户-PBX 关联：公司管理员登录 https://web.openrainbow.com → "Manage your company" → "My company"
       → "Members" → 选成员 → "Telephony" 页签 → "Device" 字段选 OXE、选分机号 → 点 Apply（关联后出现
       Rainbow number 字段，选 "computer" 路由时由 Rainbow agent 自动写入 REX 的 Remote Extension
       number，供 WebRTC 网关使用）。
    2. 权限收敛：My company / Members → 选成员 → "Permissions" 页签 → 只授 "Telephony" 权限 → Apply
       （用户用 Teams 做全部协作，Rainbow 收敛为仅电话集成）。
    3. 订阅分配：Members → 选成员 → "Services" 页签 → 选 Business 或 Enterprise（书中例 Enterprise）→
       Apply。
  verification: |
    书中本章为纯配置序列，无独立测试问题；效果验收由 c14 的登录启动与在场同步测试承接。
  conditions: Rainbow for Teams 应用已在租户上架并同意权限（c12）；用户需 Business/Enterprise 订阅。
  tags: [lab, teams, user-configuration, permissions, subscription]

- id: c14
  title: Teams 连接器安装与 Teams/Rainbow 在场同步激活
  type: lab
  source_pages: p299-307
  source_chapter: Rainbow for Teams connector installation & presence synchronization
  source_quote: |
    "Add the Rainbow app to Teams by searching for it in the applications store. … If the application
    Rainbow was available (added) for your organization, you can find it by clicking 'Built for your org'" (p300)；
    "THE RAINBOW APPLICATION INTEGRATED INTO TEAMS REQUIRES THE INSTALLATION AND STARTUP OF THE RAINBOW
    DESKTOP APPLICATION ON THE PC." (p302)；
    "we activate the sharing of information with Office 365. … Synchronization is now active." (p306)；
    "Rainbow presence status is now synchronized with Teams one" (p307)
  steps: |
    1. Teams 内点 "Apps" 图标 → 若应用已为组织添加，从 "Built for your org" 找 Rainbow（也可能被直接推
       荐）；否则用搜索 → 找到点 "Add" → 新窗口再点 "Add" 确认安装。
    2. 登录启动：点 "Sign in"；若权限未由管理员预先同意，此处提示用户自行接受（书中 Tips：首次从管理员
       账户往 Teams 里加应用，可为全组织验证权限）。
    3. Desktop 依赖：Teams 内 Rainbow 应用要求 PC 上已安装并运行 Rainbow Desktop（Warning）；若未启动，
       应用显示 "!" 图标 → 移入点 "Start" → 点 "Rainbow desktop" → 点 "Continue"（Warning：应用必须在
       PC 上；Note：Desktop 启动后提示窗自动消失）。
    4. 登录 Desktop：若此前未登录过需输凭证——书中示例配置了用 Microsoft 凭据 SSO 登录 Rainbow
       （Important：SSO 并非使用 Rainbow/Teams 连接器的必要条件）；Desktop 启动后可最小化，"!" 图标被
       Rainbow 图标取代=应用已激活并连接。
    5. 同步前基线测试：点用户图标改 Teams 在场（例 Busy）→ 查 Rainbow 侧在场——此时应不同（日历/在场
       同步尚未开启）。
    6. 激活同步：点设置图标 → 勾选与 Office 365 共享信息 → 选用户账户 → 提示 "Synchronization is now
       active" → 点 Close。
    7. 复测：再改 Teams 在场（例 Busy）→ Rainbow 侧在场随之同步。
  verification: |
    前后对照行为验证：激活前 Teams 与 Rainbow 在场不一致（p305）；激活后 "Rainbow presence status is now
    synchronized with Teams one"（p307）。
  conditions: Rainbow Desktop 已装于 PC（必须且须运行）；O365 账户可用；应用权限已同意（c12）。
  tags: [lab, teams, connector, presence-sync, o365]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 19 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 网络前提与 Pilot | 无实验。概念章（p26-36），Pilot 为外部工具介绍，书中无分步实验。 |
| task-02 公司体系 | 无独立实验章。p37-46 为概念讲义；实验中公司/PBX 以"已由经销商/讲师创建"为前提（见 c01 conditions）。 |
| task-03 管理员权责/目录/频道 | 无实验。概念章（p47-53），目录/频道操作仅截图级。 |
| task-04 订阅开通与分配 | 无独立实验章，但实验口径分散覆盖：c01 建成员留订阅默认、c06/c13 分配 Enterprise、c11 订购 Attendant Monthly（p57/p239 培训禁预付）。 |
| task-05 RLAB/OXE 实验环境 | 有 → c02 |
| task-06 DNS/代理配置 | 有 → c03 |
| task-07 OXE 接入 Rainbow | 有 → c04（含四抓手维护） |
| task-08 成员创建与管理 | 有 → c01（手动+邀请+功能测试）。CSV/Azure AD 批量、删除宽限为概念页（p96-104），无实验。 |
| task-09 分机关联与 RCC | 有 → c05（五项 RCC 测试） |
| task-10 用户形态决策 | 无实验。四形态矩阵为讲义（p106-118），决策依据已浓缩进 c06 的步骤与验证。 |
| task-11 远程延伸配置 | 有 → c06 |
| task-12 网关部署 | 有 → c07 |
| task-13 网关升级 | 有 → c08（讲义 p163-171 并入） |
| task-14 OXE 网关配置 | 有 → c09（九件套 + 四项 VoIP 测试） |
| task-15 共享池与容量 | 无实验。p146-152 为讲义与工具指针（查表/工具决策，非操作序列），留给 framework f15/f16 与 principle p19-p21。 |
| task-16 4059EE 话务台 | 有 → c10 |
| task-17 Attendant/互助组 | 有 → c11 |
| task-18 维护体系 | 无独立 How-To。p245-257 为概念讲义；OXE/网关侧维护操作已嵌入 c04（四抓手）、c07（mpcheck/三服务）、c09（sipextgw/lookars/traced）。 |
| task-19 Teams 集成 | 有 → c12（上架+权限+Azure）、c13（用户配置）、c14（连接器+在场同步） |

**统计**：14 条（全部 lab）；19 项任务中 11 项有实验条目直接覆盖，8 项为概念章/查表内容或已并入其他实验（task-01/02/03/10/15/18 无独立实验，task-04 分散覆盖，task-07/12/14/16/17/19 的维护细节部分嵌入）。
