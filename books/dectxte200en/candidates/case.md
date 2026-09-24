# 案例/实验/操作序列候选 — OmniPCX Enterprise DECT Solutions (DECTXTE200EN Ed12)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号、PARI 值）标注"实验口径"。
> 条目说明: 全书 14 个 How-To 实验章 → 14 条（p167-173 与 p235-241 为同一实验的 xBS/IBS 两版，均按章保留）。

```yaml
- id: c01
  title: 配置培训 POD（SIP 中继注册、DID 翻译、数据库备份）
  type: lab
  source_pages: p50-54
  source_chapter: Pod Configuration for the labs
  source_quote: |
    "According to your POD number, configure 2 parameters in your external SIP gateway: • Registration
    ID: pbxN ... • Outgoing username= pbxN" (p53)
    "First external number: 33210N41000 (where N is your POD Number) • First internal number: 31000 •
    Range size 500" (p53-54)
    "Perform a backup of the OXE database and save it on the PC. This backup will be restored in a
    later hands-on." (p54)
  steps: |
    1. 启动全部虚拟机；OXE 预配置已就绪（许可还原、SSH 放行、NTP 192.168.1.252、FlexLM 192.168.1.80、DHCP 池 192.168.1.145-155、机架板卡/用户/语音导引/公共 SIP 中继已建，实验口径）。
    2. 核查机架板卡（Hybrid Mode）：硬件机架 Rack 2——GD4 slot0 192.168.1.12/24、MIX484 slot1；软件机架 Rack 4（OMS）——虚拟 GD4 slot0 192.168.1.13/24 MAC 00:50:56:01:01:13（实验口径）。
    3. 开通用户：31000 IPDSP（PC 课堂）、31010 ALE-500、31011 ALE-300、31012 ALE-20H（动态 IP）、31020 ALE-30h TDM/UA；IPDSP 设置里 TFTP 服务器填 OXE Main 192.168.1.3（实验口径）。
    4. 外部 SIP 网关按 POD 号配两参数：Registration ID=pbxN、Outgoing username=pbxN（如 POD 3 → pbx3）。
    5. DID 翻译按 POD 号：Translator/External Numbering Plan/Default DID num. translator → Create；First external number=33210N41000、First internal number=31000、Range Size=500。
    6. 外呼验证公网 SIP 中继（参照 SIP Carrier Simulator 文档操作模拟器）。
    7. 备份 OXE 数据库到本地 PC（后续混合模式实验要用它恢复默认配置）。
  verification: |
    书中验收点：外呼成功（"To make sure that access to public SIP carrier is working properly, set up
    some outgoing calls"，p54）；数据库备份文件落 PC。
  conditions: RLAB POD 可用；SIP 模拟器账号 pbxP/alcatel（实验口径）
  tags: [lab, pod, sip-trunk, did, backup]

- id: c02
  title: 部署 8378 IP-xBS（全局参数 → WBM → PARI/Site → DHCP → 注册 → 状态核验 → 时间服务器）
  type: lab
  source_pages: p143-148
  source_chapter: 8378 DECT IP-xBS — Deploy 8378 IP-xBS
  source_quote: |
    "Deploy an IP-xBS solution with one PARI in a single site. PARI number: 100004101x4 (x = platform
    number) PLI = 31 AC code = 1111" (p144)
    "xBS WBM engineer password (Default: Engineer00!) xBS WBM admin password (Default: Admin00!)" (p145)
    "Registration node 1 Registration enabled YES ... Command dectview xbs" (p147)
  steps: |
    1. 全局参数 PWT/DECT System：Radio base type=xBS（或 Mixed）；Station Base Type=DECT Europe；PLI for CTM=31；AC System=1111、Security level=Authentication（AC 可选）。
    2. xBS 参数 PWT/DECT System / xBS System：Number of PARI=1（最多 8）；Allow xBS Web Based Management=YES，WBM engineer/admin 口令（默认 Engineer00!/Admin00!，实验口径）。
    3. 建 PARI：PWT/DECT System / xBS System / xBS Pari → PARI Number=0、PARI Value=100004100x4（实验口径示例）、Area type=1 area of 256 xBS。
    4. 改 Site：PWT/DECT System / xBS System / xBS Site → Site Number=0、Site Name=BREST、Station Base Type=DECT Europe（Site 0 默认存在）。
    5. 基站参数 PWT/DECT System / xBS System / xBS base station：Terminal Ethernet Address=自动、Location name=GF-01、Site 0、PARI 0、Area 0、RPN 只读；Clusters 0-7 默认全在 Cluster 0。
    6. DHCP：内部 OXE DHCP 已管地址池 192.168.1.145-155（实验口径），vendor class alcatel.ipxbs.0。
    7. 开注册：PWT/DECT System / xBS System → Registration node=1、Registration enabled=YES（注意指定注册节点）；Default PARI / Default location area 可用 auto(255)；随后接通两台 IP-xBS。
    8. 状态核验：mtcl 下 dectview xbs——两行 OK、IP/MAC/FW 落表、RPN 已分配（实验输出：192.168.1.145/146 等）。
    9. 时间服务器：NTP（192.168.1.252，实验口径）已在 OXE 声明；登录 xBS WBM（https://基站 IP，engineer/Engineer00!）核验 Time server=OXE 地址（经 UA 信令下发，可手工改）。
  verification: |
    书中验收点：dectview xbs 显示 "Region 0 (EUROPE) has 1 site(s) with 2 XBS in service"，基站
    State=OK 且系统已分配 RPN（p147）；WBM 内 Time server 为 OXE（p148）。
  conditions: POD 已按 c01 配置；基站 PoE 供电接入 LAN
  tags: [lab, ip-xbs, deployment, pari, registration]

- id: c03
  title: 更换故障 IP-xBS 基站（删旧 MAC@ → 手动注册新 MAC@ 保 RPN）
  type: lab
  source_pages: p149-151
  source_chapter: 8378 DECT IP-xBS — Replace an out of service IP-xBS base station
  source_quote: |
    "Un-register the IP-xBS Base station by removing its MAC @ in the OXE DB ... PWT/DECT System /
    xBS System / xBS base station" (p150)
    "The manual registration is recommended when replacing a broken base station by a new one (with a
    new MAC@)" (p150)
  steps: |
    1. 实验模拟：与邻座交换基站模拟故障；拔掉 id 0 基站。
    2. 注销：PWT/DECT System / xBS System / xBS base station → Base station id 0 → 删除 Terminal Ethernet Address（MAC@），记下位置名（GF-01）。
    3. 注册新站：同一页面 → Base station id 0 → 手工录入新基站 MAC@、重填位置名 GF-01、Site Number=0；接上新基站。
    4. 状态核验：mtcl 下 dectview xbs——id 0 行 State=OK、新 MAC@ 生效。
    5. 数据库核验：PWT/DECT System / xBS System / xBS base station → MAC@ 在库、RPN 已分配（PARI 0 / Area 0）。
  verification: |
    书中验收点：dectview xbs 两站 OK（p151 输出含 GF-01/FL1-01 两行）；数据库页 MAC@ 存在且
    "the system has assigned a RPN value to the xBS"（p151）。
  conditions: c02 已完成（基站已入网）；备件基站 MAC@ 已知
  tags: [lab, ip-xbs, replacement, mac, rpn]

- id: c04
  title: 收集 IP-xBS 日志到 syslog 服务器（装 Visual Syslog → 声明服务器 → debug 级别 → 核验）
  type: lab
  source_pages: p155-161
  source_chapter: 8378 DECT IP-xBS — Collect IP-xBS logs on a syslog server
  source_quote: |
    "Install the free software 'Visual Syslog server' on the client PC. The installation program,
    visualsyslog_setup.exe, is available on the NAS server. To get there, map a network drive ...
    (\\12.0.0.2\RLAB\ENTP; login: RLAB\Trainee; password: Superuser1234)" (p156，实验口径)
    "SYSLOG IP address < Enter the IP address of the syslog server > 192.168.1.9 ... SYSLOG port 514" (p160)
    "Debug: Used for troubleshooting. Must not be enabled during normal operation." (p160)
  steps: |
    1. 客户端 PC 装 Visual Syslog server（安装包在 NAS：映射 \\12.0.0.2\RLAB\ENTP，RLAB\Trainee/Superuser1234，实验口径）→ 完成安装向导 → 启动应用。
    2. 声明服务器：PWT/DECT System / xBS system → Modify → SYSLOG IP address=192.168.1.9、SYSLOG port=514（默认值）。
    3. 设级别：PWT/DECT System / xBS system / xBS base station → 选基站 id 0 → Syslog level=Debug（可选 off / Normal operation / System Analyze / Debug）。
    4. 基站侧核验：xBS WBM（https://基站 IP，engineer/Engineer00!）→ Syslog 菜单 → 核对 Syslog Server IP/port/级别已下发。
    5. 服务器侧核验：Visual Syslog 界面收到该基站日志。
  verification: |
    书中验收点：syslog 服务器应用上可见 xBS 信息（"Check the information's received on the Syslog
    server"，p161）。
  conditions: c02 已完成；客户端 PC 与基站同网可达
  tags: [lab, syslog, logs, troubleshooting]

- id: c05
  title: 注册 IP-xBS 到多 Site 并验证跨站漫游（Site 创建/分配/WBM 看同步树/漫游模拟）
  type: lab
  source_pages: p199-203
  source_chapter: 8378 DECT IP-xBS — Manage the multi sites (Branch Offices)
  source_quote: |
    "Add a new site with the name 'BO' (for Branch Office) and move the xBS base station id 1 to it.
    Modify the name of the site number 0 by the new name HQ" (p200)
    "Browse the IP @ of the base station id 1 to check the synchronization tree ... Select 'multi
    Cell' ... See the DECT chain information" (p202)
    "Switch off the handsets. Unplug the base station of the head quarter. Switch on the handsets and
    try to make calls" (p203)
  steps: |
    1. 建 Site：PWT/DECT System / xBS System / xBS Site → Create → Site Number=1、Site Name=BO、Station Base Type=DECT Europe。
    2. 改 Site 0：同一菜单 Modify → Site Number=0、Site Name=HQ。
    3. 分配基站：PWT/DECT System / xBS System / xBS base station → 选 id 1 → Site Number=1（默认基站属 Site 0）。
    4. 核验 Site 归属：mtcl 下 dectview xbs——id 0 行 HQ、id 1 行 BO，各自带主站标志（每 Site 一棵同步树，各站应为本 Site 的 Master）。
    5. WBM 看树：浏览器开 https://192.168.1.146（id 1）与 https://192.168.1.147（id 0）（实验口径）→ Multi Cell → 查看 DECT chain information。
    6. 跨站漫游模拟：关手机 → 拔 HQ 基站 → 开手机 → 试打电话（手机应锁定 BO 站继续通话）。
  verification: |
    书中验收点：dectview xbs 显示 "Region 0 (EUROPE) has 2 site(s) with 2 XBS in service"，两站各为
    本站 Master（P+ 标志，p201）；拔 HQ 后手机经 BO 仍可呼出（p203）。
  conditions: c02 已完成；两台基站分别代表 HQ/BO
  tags: [lab, multi-site, site, roaming, wbm]

- id: c06
  title: 手机勘测模式开关（*7378423* 激活 Site Survey、按键语义、关闭）
  type: lab
  source_pages: p213-217
  source_chapter: Introduction to radio coverage — Switch On / Off the survey mode
  source_quote: |
    "Enter the code *7378423* (mnemonic: *service*) ... Select 'Site Survey mode' in the menu" (p214)
    "The site survey will be in front of the normal display, using the top third of the display area.
    It will be shown in all modes, idle, conversation" (p215)
    "This mode is intended for debugging purpose and shall not be used for normal end user operation
    ... In this mode, battery autonomy is reduced." (p216)
  steps: |
    1. 手机空闲主页按 Menu 键（或两次 OK）进入菜单。
    2. 输入 *7378423*（助记 *service*）。
    3. 选 "Site Survey mode" → 按 On 激活（勘测层显示在正常界面上方 1/3，任何模式可见）。
    4. 按键语义（p216）：长按 * = 慢/快测量切换；长按 # = No Lock/Lock to base；Vol- = 显示 RFPI 附加屏；Vol+ = 回主屏；侧功能键 = 第一按冻结结果（右上角 P）/第二按隐藏/第三按恢复。
    5. 绕场测量，找覆盖边界（实验任务：-70dBm 等值线，p214）。
    6. 关闭：菜单中按 Off → On hook → 回空闲主页。
  verification: |
    书中验收点：勘测信息层出现并随位置更新 RSSI/基站列表；Off 后回空闲主页（p217）。
  conditions: 仅调试用途、不得给最终用户常开；续航下降
  tags: [lab, survey-mode, rssi, handset]

- id: c07
  title: 创建 DECT 用户并注册手机（webadmin DECT Register / dectinston 双通道）
  type: lab
  source_pages: p167-173
  source_chapter: DECT handsets — Create and register the DECT handsets（IP-xBS 版）
  source_quote: |
    "Create 2 users with the following directory numbers, 31015 and 31016, and whose set type is
    'GAP+'. Create one user with the directory number 31017 and whose set type is 'GAP'." (p168，实验口径)
    "Warning THE POINT 2.2 HAS TO BE DONE MORE OR LESS SIMULTANEOUSLY WITH POINT 2.1.1 OR 2.1.2 TO
    REGISTER A DECT ONLY ONE OF THE 2 METHODS MUST BE USED" (p169)
    "command dectinston <directory number> or dectinston -g ... Wait until the set rings, but you
    don't have to hang up!!! Press 0 to leave. Installation succeed. Effective Security Level: Use
    Authentication" (p170)
  steps: |
    1. 建用户：Users → Create → Directory number=31015/31016（GAP+）、31017（GAP），姓名任意（各 20 字符内），Set type=GAP+ / GAP Handset。
    2. （通道 A）webadmin：Users / <用户> / DECT set → 点 "DECT Register" → 同时执行步骤 4 的手机侧操作 → 注册完成后 IPUI N/IPUI O 字段回填。
    3. （通道 B）dectinston：mtcl 下 dectinston <目录号> 或 dectinston -g →（可选）选择指定基站 → 核对 GAP 特性（DN/用户名/MAO type/PARI/PLI）→ Y 确认 → 等手机响铃（不要挂断）→ 按 0 退出；续装选 1（自动选号）或 2（手工选号）。
    4. 手机侧（与 2/3 近乎同时）：Yes → Select → 输 PIN 码 → Ok → Select → Ok → 输 AC 码（如已配置，实验 1111）→ Ok → 选 Normal → 选 Yes。
    5. 注册完成：手机响一声并显示注册信息（姓名、名、分机号、PARI、PLI）。
  verification: |
    书中验收点：dectinston 输出 "Installation succeed. Effective Security Level : Use Authentication"
    （p170）；webadmin 侧 IPUI N/IPUI O 更新（p169）；手机屏显注册信息（p173）。
  conditions: c02 已完成（基站入网）；双通道只能取一
  tags: [lab, registration, dectinston, gap, handset]

- id: c08
  title: 注销并删除 DECT 手机（DECT Deregister / dectrm 双通道 + 用户保留技巧）
  type: lab
  source_pages: p174-177
  source_chapter: DECT users — Uninstall and remove a DECT handset
  source_quote: |
    "Warning TO DEREGISTER A DECT ONLY ONE OF THE 2 METHODS MUST BE USED: POINT 1.1.1 OR 1.1.2" (p175)
    "command dectrm <directory number> ... Are you really sure to remove this set. (Y/N - Default is
    Y) ? ... Operation succeed." (p176)
    "If the handset has been deregistered to be changed/replaced ... it is not necessary to delete the
    user from the OXE DB. It is possible to re-register directly with the new handset." (p177 Tips)
  steps: |
    1. （通道 A）webadmin：Users / <用户> / DECT set → 点 "DECT Deregister" → 完成后 IPUI N/IPUI O 更新。
    2. （通道 B）dectrm：mtcl 下 dectrm <目录号>（实验例 dectrm 31015，输出含 IPEI 1410309133756）→ Y 确认 → 等待向手机发注销消息 → "Operation succeed"。
    3. 手机侧结果：手机显示已注销状态（p176 屏显）。
    4. 删用户（可选）：Users / <用户> → Delete——仅在不再需要该分机时执行。
    5. 维护技巧：换机维护场景不删用户，直接用新手机重新注册（保留分机配置）。
  verification: |
    书中验收点：dectrm 输出 "Operation succeed"（p176）；手机显示已注销；webadmin IPUI 字段清空/更新。
  conditions: c07 已完成（有在册手机可注销）；双通道只能取一
  tags: [lab, deregistration, dectrm, lifecycle]

- id: c09
  title: 部署 8379 IBS 基础设施（全局参数 → PARI → 网关指派 → 建 IBS 站 → 维护命令）
  type: lab
  source_pages: p226-234
  source_chapter: IBS DECT Infrastructure deployment — Deploy IBS infrastructure
  source_quote: |
    "Radio base type Select IBS (or Mixed if xBS stations are also used) ... PLI for CTM 31 ... AC
    System 1111 ... Security level Authentication" (p227，实验口径)
    "Manage the IBS PARI number as 100004101x0 with: x: POD number ... PARI Value Enter a PARI number
    (e.g. 10000410110 for POD 1)" (p228)
    "Shelf / <concerned media gateway> / Board / <concerned UA board> / IBS ... Equipment address
    Enter the physical address of the base station (an even port if 2 UA links used)" (p230)
  steps: |
    1. 恢复默认数据库（用 c01 的备份）；全局参数 PWT/DECT System：Radio base type=IBS（或 Mixed）、PLI=31、AC System=1111、Security level=Authentication（IBS 不能选 Encryption）、Station base type=DECT Europe。
    2. PARI：PWT/DECT System/ IBS System → PARI Value=100004101x0（x=POD 号，实验口径）、Area type 按漫游优化设置。
    3. PARI 指派到网关：Shelf / <目标 media gateway> → PARI Number=选 IBS PARI。
    4. 建 IBS 站：Shelf / <mg> / Board / <UA 板> / IBS → Create → Equipment address=物理端口（双链路用偶数口）、RPN 默认、Location name、Line delay 按距离（Short 0-400M/Medium 400-800M/Long 800-1200M）、Number of UA links=1（3TS）或 2（6TS，系统预留下一端口）、IBS generation=1G/2G；Location area 字段在建站后才出现。
    5. 状态核验：dectview ibs——IBS 行 INSERV、3 channe DECT、2G/1G、AUTHE。
    6. UA 链路核验：listerm <mg> <cpl>——终端在服务、T 标志含义对照表内注释。
    7. 站详情：listibs p <mg> <cpl> 0 <equip>（输出 line_delay/nb_ua_link/rpn/ibs_generation 等）。
    8. 复位演示：outserv p 2 1 0 34 → Y → inserv p 2 1 0 34 → Y。
  verification: |
    书中验收点：dectview ibs 显示 "INSERV just 3 channe DECT V 2G 8379 53.02 odd AUTHE NORMAL"
    （p231）；listerm 显示终端在服务（p232）。
  conditions: MIX484/UAI 板卡在位（c01 步骤 2）；IBS 布线在长度口径内（SYT 800m / LY278 1200m）
  tags: [lab, ibs, deployment, ua-board, maintenance]

- id: c10
  title: 创建并注册 DECT 手机（IBS 版——与 xBS 版同流程）
  type: lab
  source_pages: p235-241
  source_chapter: DECT handsets — Create and register the DECT handsets（IBS 版）
  source_quote: |
    "Create 2 users with the following directory numbers, 31015 and 31016, and whose set type is
    'GAP+' ..." (p236，实验口径)
    "Warning THE POINT 2.2 HAS TO BE DONE MORE OR LESS SIMULTANEOUSLY WITH POINT 2.1.1 OR 2.1.2 ..." (p237)
  steps: |
    1-5. 与 c07 完全同构（同用户号 31015/31016/31017、同双通道、同手机侧按键序列），差异仅在基础设施：本实验的注册经由 IBS 基站完成。
    补充规则（p165 讲义）：混合 IBS+xBS 时注册可经任一类基站完成（订阅由 Call Server 管理，命令
    dectinston），注册后的手机在两类基站上都可用。
  verification: |
    同 c07（dectinston "Installation succeed"、IPUI 回填、手机屏显注册信息）。
  conditions: c09 已完成（IBS 入网）；AC=1111 时手机侧需输入该码
  tags: [lab, ibs, registration, duplicate]

- id: c11
  title: 部署混合 DECT 基础设施（TDM & xBS 同站、PLI=30 统一两 PARI）
  type: lab
  source_pages: p242-248
  source_chapter: 8378 DECT IP-xBS — Mixed DECT infrastructure (TDM & xBS)
  source_quote: |
    "Setup an IP-xBS solution on a site with an existing IBS infrastructure. The IBS PARI is
    100004101x0. The new xBS PARI will be 100004101x4 (x = POD number). The PLI value will be 30.
    With that all DECT users will be able to connect on all DECT base stations (xBS & TDM)." (p244)
    "Radio base type Mixed ... RPN 0 xBS PARI: 100004101x4 ... RPN 0 RPN 1 IBS PARI: 100004101x0 ...
    PLI = 30" (p244)
  steps: |
    1. 拓扑确认：IBS PARI=100004101x0（RPN 0/1，c09 已建）、新 xBS PARI=100004101x4（RPN 0），两基站间距 15 米内（实验口径）。
    2. 全局参数 PWT/DECT System：Radio base type=Mixed、Station Base Type=DECT Europe、PLI for CTM=30（混合模式适配，原 31 降为 30）、AC System=1111、Security level=Authentication。
    3. xBS 参数：xBS System → Number of PARI=1、WBM YES + 口令。
    4. 建 xBS PARI：xBS System / xBS Pari → PARI Number=1、PARI Value=100004101x4、Area type=1 area of 256 xBS。
    5. Site：xBS Site → Site 0 命名 BREST。
    6. 基站参数：xBS base station → Location name GF-01、Site 0、PARI Number=1、Area 0；Clusters 默认。
    7. DHCP（192.168.1.145-155 池，vendor class alcatel.ipxbs.0）。
    8. 注册：xBS System → Registration node=1、Registration enabled=YES → 接通两台 xBS。
    9. 核验：dectview xbs——两站 OK、PARI-Area-RPN 列为 1-0-0 / 1-0-1。
  verification: |
    书中验收点：dectview xbs 输出 "Region 0 (EUROPE) has 1 site(s) with 2 XBS in service" 且
    PARI-Area-RPN=1-0-x（p248）；PLI=30 使全部 DECT 用户可接入两类基站（p244 任务声明）。
  conditions: c09 已完成（IBS 在网）；PLI 改动后老手机按 PLI 缩位语义兼容，或按 c12 重注册
  tags: [lab, mixed-mode, pli, pari]

- id: c12
  title: DECT 手机自动重注册（dectinston -update 单机 / -f 文件批量 / 结果文件核验）
  type: lab
  source_pages: p259-262
  source_chapter: DECT handset automatic re-registration — Re-register automatically DECT handsets
  source_quote: |
    "To ensure that the roaming between the two PARI will be possible, the PLI has to be managed with
    the following value: 30." (p260)
    "(1)csa> dectinston -update 31015 -pari 10000410114 -pli 30 ... 31015 re-installed successfully!!!" (p260)
    "Create a 'DECT.txt' file containing the directory numbers 31016 et 31017 ... transfer the file via
    FTP/SFTP to the OXE directory: /tmpd" (p261)
  steps: |
    1. 前置：系统 PLI 已调为 30（c11），xBS PARI=10000410114（实验口径值）。
    2. 单机重注册：mtcl 下 dectinston -update 31015 -pari 10000410114 -pli 30 → 核对回显（DN/用户名/MAO type/PARI/PLI）→ "Auto Re-registration in progress" → "31015 re-installed successfully!!!"。
    3. 批量准备：Notepad++ 建 DECT.txt（每行一个目录号：31016、31017；# 开头行为注释）→ FTP/SFTP 传到 OXE /tmpd。
    4. 批量执行：cd /tmpd → dectinston -update -f DECT.txt -pari 10000410114 -pli 30 → 逐台回显成功。
    5. 结果核验：more ReinstallSuccessHandsetsList.txt（成功清单，带命令头注释）与 more ReinstallNOKHandsetsList.txt（失败清单，应为空）；两文件生成在输入文件同目录（/tmpd）。
  verification: |
    书中验收点：单机回显 "re-installed successfully!!!"（p260）；批量回显 "Process Completed!!" 且
    ReinstallSuccessHandsetsList.txt 含 31016/31017、NOK 文件为空（p262）。
  conditions: 手机已注册、在运行且在安装节点覆盖内；机型满足最低版本表（p252）
  tags: [lab, re-registration, update, batch, tmpd]

- id: c13
  title: 配置跨 PARI 外部同步链路与外部 handover（IBS↔xBS 混合切换验证）
  type: lab
  source_pages: p263-270
  source_chapter: 8378 DECT IP-xBS — External synchronization link
  source_quote: |
    "Flag External Handoff yes" (p266)
    "PWT / DECT System / xBS system / xBS Site / External Synchronization ... PARI Number 1 ... Sync
    Master RPN 0 ... Sync Master backup RPN 255 ... External Synchronization PARI 100004101x0 ...
    External Synchronization RPN 0" (p266)
    "Using the DECT handset in 'Survey mode', estimate the 'handover' area between the IBS and xBS
    base stations." (p267)
  steps: |
    1. 前置核验：Radio base type=Mixed（PWT/DECT System）；xBS PARI（PARI 1=100004101x4）、IBS PARI（100004101x0）；Site=BREST；PLI=30；两站间距约 15 米（实验口径），手机 survey mode 核对覆盖重叠（RSSI>70dB 强区与 <70dB 切换区）。
    2. 允许外部切换：PWT/DECT System → Flag External Handoff=yes。
    3. 建外部同步链路：PWT/DECT System / xBS system / xBS Site / External Synchronization → PARI Number=1（被同步的 xBS PARI）、Sync Master RPN=0（xBS 中作 Sync Master 的站）、Sync Master backup RPN=255（实验取 none）、External Synchronization PARI=100004101x0（同步源 TDM PARI）、External Synchronization RPN=0（IBS 同步源站 RPN）。
    4. 同步核验：mtcl 下 dectview xbs——表尾出现 External sync source 表（S 0-IBS → *M 0-GF-01，Backup B 255）。
    5. 估算切换区：手机开 survey mode——IBS（实验中增益 -28dBm）排列表首；移向 xBS RPN 01，当 xBS 升到列表首位即进入 handover 区。
    6. 通话验证（IBS 侧）：在 IBS 上建立呼叫（要点：通话必须先建在 IBS）→ dectview com 显示 Link/State STABLE、Num:31016、"Elastiques (External Handover in ABC)"。
    7. 切换验证（xBS 侧）：保持通话移向 xBS 完成 handover → dectview com 显示 RELAY: 1/0/55、RADIO=1/0/55，通话不断。
  verification: |
    书中验收点：dectview xbs 表尾 External sync source 行（p267）；dectview com 先后显示 IBS 时隙通话
    与 xBS RELAY 通话（p269-270）。
  conditions: c09+c11 已完成（IBS 与 xBS 同站在网）；同步门槛 RSSI≥-80dBm（基站间）
  tags: [lab, external-synchronization, handover, mixed]

- id: c14
  title: 部署 8328 SIP-DECT（DHCP 固定 IP → 基站基础配置 → OXE SIP 用户 → 注册关联 → 双小区）
  type: lab
  source_pages: p279-291
  source_chapter: 8328 base stations and 8214 handsets — Deploy 8328 base stations & 8214 handsets
  source_quote: |
    "DHCP Configuration / DHCP Server / CPU Main Subnetwork/ Static IP Address (local subnet) ... IP
    address Enter a compliant IP address: e.g. 192.168.1.150 ... Alcatel-Lucent terminals only NO" (p280)
    "Server Alias Enter a name for the server. Example: OXE ... Registrar Enter the OXE FQDN. Example
    in our case here: oxe.company.com" (p282)
    "Directory Number 31040 ... Set type Select 'SIP Extension' ... SIP password ... E.g. the
    directory number: 31040" (p283，实验口径)
    "THE PRIMARY STATION WILL BE THE STATION WITH ALREADY AT LEAST ONE EXTENSION DECLARED." (p288)
  steps: |
    1. DHCP 固定 IP：DHCP Configuration / DHCP Server / CPU Main Subnetwork / Static IP Address (local subnet) → Create → IP=192.168.1.150 + 8328 MAC；DHCP 配置里 "Alcatel-Lucent terminals only"=NO（8328 不被识别为 ALE 设备）→ Apply Modifications；接网线，基站绿灯闪烁表示取到地址。
    2. （技巧）不知 IP 时用手机发现：手机空闲按菜单键拨 *47* 进搜索基站功能。
    3. 基站基础配置：浏览器 https://192.168.1.150 → admin/admin（默认，实验口径）→ Country 区选国家（France）、Time server=NTP（R-lab 192.168.1.252）；Network 区核对 DNS（DHCP 下发，FQDN 声明必需）；Servers 区 → Server Alias=OXE、Registrar=oxe.company.com。
    4. OXE 侧建用户：WBM Users → Create → Directory Number=31040、Set type=SIP Extension；SIP 页 Sub type=default、SIP password=31040（实验口径示例）。
    5. 基站侧声明手机：Extensions/Handset → Add Handset → Save → 选中该行 → Register Handset(s)。
    6. 手机侧注册：开机（全新/已注销机自动提议注册）→ 选 SIP → 输设备 PIN（默认 0000）→ 输 AC 码（基站 webadmin 可见可改，默认 0000）→ 注册成功提示；此时主页显示"无 SIP 注册"属正常（下一步才关联）。
    7. 声明扩展并关联：Extensions/Extensions → Add extension → Extension=31040、Authentication User Name=31040、Authentication Password=31040、Server=OXE → 勾选已注册手机 → Save；表格出现 IPEI-31040 关联，手机屏显扩展名。
    8. 通话测试：手机呼系统内其他用户、反向呼入。
    9. 双小区：仅给第二台基站配 DHCP（IP=192.168.1.151 + MAC，实验口径）后入网——无需任何管理动作，副站自动发现主站并拉取配置（主站=已声明至少一个 Extension 的那台）；等约 5 分钟。
    10. 双小区核验：主站（192.168.1.150）Home/Status → Dual Cell 区显示副站已连接；副站（192.168.1.151）→ 显示 secondary；Servers/Extensions 区数据自动来自主站；链路不起时按 Tip 在两站 reset the chain。
  verification: |
    书中验收点：手机注册后 IPEI 不再是通用值 FFFFFFFFFF（p286）；关联后手机屏显扩展名且 IPEI 挂到
    31040（p287）；双小区状态页主/副站互相可见（p289-290）；双向通话成功（p287）。
  conditions: 双小区同 IP 子网 + NTP mandatory；仅 8214 手机、仅欧洲频段
  tags: [lab, sip-dect, 8328, dual-cell, sip-extension]
```

## 任务覆盖自检

| BOOK_OVERVIEW task | 对应 case 条目 |
|---|---|
| task-01 | 无（概念理解型任务，无操作实验；承载于 framework f03-f06） |
| task-02 | 无（决策型任务；承载于 framework f02/f17） |
| task-03 | c01 |
| task-04 | c02 |
| task-05 | c03 |
| task-06 | c04 |
| task-07 | c07（及 c10 IBS 版） |
| task-08 | c08 |
| task-09 | 无独立 How-To 章（讲义+downstat x 菜单 p129-133，承载于 principle p17） |
| task-10 | 无独立 How-To 章（讲义+downstat m p179-189，承载于 principle p21/p22） |
| task-11 | c05 |
| task-12 | c06 |
| task-13 | c09（手机注册部分 c10） |
| task-14 | c11 |
| task-15 | c12 |
| task-16 | c13 |
| task-17 | c14 |
| task-18 | c14（dual cell 部分，书中与部署同一章） |
| task-19 | 无独立章（命令族分散在各实验验证步；承载于 principle p30） |
| task-20 | 无独立章（安全级别内嵌于 c02/c09 步骤 1；承载于 principle p09） |

14 个 How-To 章全部成条；task-01/02/09/10/19/20 为决策、讲义或内嵌型任务，按分工落在 framework/principle，无遗漏。
