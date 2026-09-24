# 案例/实验/操作序列候选 — OmniPCX Enterprise Starter (ENTPXTE400EN Ed12)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号、分机号）标注"实验口径"。
> 条目说明: 全书 32 个 How-To 实验章逐章一条（c01-c32）；维护章（p737-756）为讲义含命令示例、无独立实验，其命令面已并入 principle p35/framework f34。

```yaml
- id: c01
  title: 本地登录 OXE 与账户/密码安全（V24/console、四账户、改密/锁定/老化）
  type: lab
  source_pages: p95-107
  source_chapter: Local access to the system – Accounts and passwords (How-To)
  source_quote: |
    "mtcl (for the current training; password= Administrator5689!) • root … Superuser2580* • swinst … Superuser2580*" (p98)；
    "IT IS POSSIBLE TO CONNECT DIRECTLY VIA THE ROOT ACCOUNT ONLY IF YOU USE A LOCAL ACCESS (SERIAL CONNECTION, KVM, …)" (p99)；
    "How many failed authentication attempts allowed for login (3<=X=5, default 3)? 4" (p104)
  steps: |
    1. 物理机接串口线（PC 串口↔CS 板串口）；虚拟机经 vSphere（浏览器输 ESXi 地址→vSphere 凭据→选 OXE 虚机→Console）；GAS 经 VGA+键鼠的 VMM。
    2. mtcl 登录：login mtcl / Administrator5689!（实验口径）——横幅显示 Active version、ACD/CCD 版本、SSH/iptables 状态；(E) 表示话务停止。
    3. root 登录（Warning：仅本地）：login root / Superuser2580*；或从 mtcl 执行 su -（需 root 密码）。
    4. swinst 登录（root 下进入免密）：Easy/Expert 菜单。
    5. 启用 client 账户：swinst → 2 Expert → 6 System management → 5 User's accounts management → 6 Create the 'client' account → 设密码 Superuser2580*（实验口径）→ q 退出；client 登录（Warning：话务应用必须运行中）验证 MENU CLIENT 四项。
    6. 改密：swinst Expert→System management→User's accounts management→1 Change account password（例：mtcl 新密码 Alibaba&the40thieves）；或 root 下 passwd mtcl / mtcl 下 passwd。
    7. 失败锁定：同菜单 3 Set maximum authentication attempts → 设 4 → 连输错密码验证锁定 15 分钟 → 恢复默认 3。
    8. 老化：同菜单 2 Change account aging passwords → mtcl 21 天；再用 swinst Expert→System management→1 Date & time update→1 Set date & time 把月份 +1 → 重新登录 mtcl 验证强制改密 → 恢复正确时间。
  verification: |
    mtcl/root/swinst/client 四账户均可登录；密码改后新密码生效；错误 4 次提示锁定 15 分钟且到时解锁；mtcl 老化到期登录被强制改密。
  conditions: 实验口令为实验口径；root 直登仅限本地；client 登录需话务运行。
  tags: [lab, accounts, password, swinst]

- id: c02
  title: 系统启停与 autostart 管理
  type: lab
  source_pages: p121-125
  source_chapter: Start & Stop the System (How-To)
  source_quote: |
    "Your choice [1..10, Q] ? 8 … Please confirm to start the telephone (y/n, default y): y" (p122)；
    "WHEN THE TELEPHONE APPLICATION IS STOPPED VIA THE SWINST MENU (1-EASY MENU > 7-STOP THE TELEPHONE), THE AUTOSTART IS AUTOMATICALLY DISABLED" (p124)
  steps: |
    1. 手动起话务：swinst → 1 Easy menu → 8 Start the telephone → y；或 mtcl 下执行 RUNTEL。
    2. 查状态：mtcl 下 role（MAIN/STAND-BY=运行；erreur mapping on remagen -7=停止）；提示符 (E)/(数字) 辅助判断（不实时刷新时重登录）。
    3. autostart：swinst → 2 Expert → 6 System management → 2 Autostart management → 1 Set（或 2 Unset）。
    4. 重启：mtcl 下 shutdown -r now → 等 "No problem with compatibilities" → role 确认话务自启。
    5. 一次性取消自启：重启过程中在 "automatic start of dhs3 is about to begin waiting 5 seconds before starting… type CR key to stop" 出现时按回车。
    6. 停话务：swinst Easy → 7（注意：自动取消 autostart）；无独立停话务命令，只能重启+取消。
    7. 停机：shutdown -h now（显示 "Software Watchdog stopped / Power down."）或 swinst Easy → 10 Stop the system；随后可断电或按任意键重启。
    8. 恢复运行以继续后续实验。
  verification: |
    role 显示 MAIN；Easy 8 后 "Autostart is set"；Easy 7 后提示 "Autostart is not set"；停机显示 Power down。
  conditions: 无。
  tags: [lab, start-stop, autostart, role]

- id: c03
  title: Call Server IP 配置（netadmin 完整安装 + Role 地址 + SSHv2 连接 + who/last）
  type: lab
  source_pages: p145-155
  source_chapter: IP Addressing & Firewall (How-To)
  source_quote: |
    "Enter node name (default is node000000) ? oxe … CPU name (default is xa000000) ? csa … CPU address ? 192.168.1.1 … Enter OXE Domain to be configured (default is oxedomain.com) ? company.com" (p146)；
    "TO TAKE THE MODIFICATION DONE VIA THE NETADMIN MENU INTO ACCOUNT, IT IS MANDATORY TO RESTART THE SYSTEM" (p148)
  steps: |
    1. mtcl 登录执行 netadmin（完整安装口径）：erase=y → IP/X25=n → 节点名 oxe → 内部名字解析 n → 单 CPU n → CPU 名 csa → 地址 192.168.1.1 → 掩码 255.255.255.0 → 域名 company.com（实验口径；默认 oxedomain.com 会致证书错误）→ 外部网关 y → 名 gateway → 192.168.1.254。
    2. 临时安全：Security → Firewall → 2 Allow/Deny SSH for all → y → a 应用。
    3. 重启系统使 netadmin 生效（Warning 强制）。
    4. Role 地址：netadmin -m → 5 Role addressing → 2 Add → 名 csm、地址 192.168.1.3 → 0 → 23 Apply modifications（NGINX 重启）→ 0 退出 → 重启。
    5. 核对：netadmin -m → 2（csa/csm/gateway 表 + Low dynamic ports 10000-10499）；ifconfig（eth0=主址、eth0:0=物理址别名、lo）。
    6. SSHv2：Putty → CS Main IP 192.168.1.3 → SSH → 勾 SSH v2 → Open → 接受公钥 → mtcl 登录（横幅含 Role MAIN/PANIC 旗标；root 不可 IP 直登）。
    7. 身份与历史：who（账户/时间/来源 IP）；last（账户/pts 或 tty/IP/时长）。
  verification: |
    netadmin -m 选 2 显示 csa 192.168.1.1 / csm 192.168.1.3 / gateway 192.168.1.254；SSHv2 以 mtcl 登录成功且横幅 Role: MAIN。
  conditions: 实验地址为实验口径；重启前 SSH-for-all 便于后续实验。
  tags: [lab, netadmin, ip, role-address, ssh]

- id: c04
  title: OXE 内部防火墙：可信主机单加/网段/批量导入
  type: lab
  source_pages: p156-163
  source_chapter: OXE internal Firewall (How-To)
  source_quote: |
    "Add the PC Client 10 (IP @= 192.168.1.10) as a trusted host. … Add the IP address range [192.168.2.10/192.168.2.11] … If currently the option 'Allow SSH for All' is enabled, you have to disable it." (p157)
    "Enter the full path of the CSV file /tmpd/Firewall_Rules.txt" (p162)
  steps: |
    1. root 登录 → netadmin -m → 11 Security → 1 Firewall(iptables) Configuration。
    2. （若开启过）2 Allow/Deny SSH for all → n 先关回。
    3. 3 Restricted Access Configuration → 1 View（默认仅 gateway 可信）→ 2 Add a trusted host：PC10 / 192.168.1.10 → 3 Add a range：192.168.2.10 至 192.168.2.11。
    4. 0 返回 → 2 Deny SSH for all → n？选 n（deny）→ a 应用 → 1 View 核对 INPUT 链仅剩可信源。
    5. 用 Putty 验证：PC10/PC20/PC21 可 SSH，PC11 被拒。
    6. 批量导入：FileZilla（SFTP，mtcl@CS，端口 22）把 NAS 上 Firewall_Rules.txt 传到 OXE /tmpd → netadmin -m → 11 → 1 → 3 → 7 Bulk Import → /tmpd/Firewall_Rules.txt（自动 dos2unix）→ 1 View 核对（cartier/oms/gd4/pc11/pc-classroom/ntp1/dns1/pc10 等）→ a 应用 → 1 View 防火墙规则。
  verification: |
    iptables INPUT 链仅放行可信主机与网段；PC11 连接被拒；导入后 trusted hosts 列表与文件一致。
  conditions: CSV 无表头、逗号分隔（TRUSTED_HOST/TRUSTED_RANGE 两种行）；DHCP 池地址不可经 netadmin 修改。
  tags: [lab, firewall, trusted-hosts, bulk-import]

- id: c05
  title: NTP/chrony 部署（时区/加服务器/瞬时同步/渐进同步/巡检）
  type: lab
  source_pages: p175-183
  source_chapter: Date, Time and NTP (How-To)
  source_quote: |
    "Choice 2 Set timezone … Warning YOU MUST REBOOT THE SYSTEM TO APPLY MODIFICATION!" (p176)；
    "Enter the name or IP address of the server: 192.168.1.252" (p177)；
    "2024-03-05T10:02:42Z System clock wrong by 2674857.352482 seconds (step)" (p179)
  steps: |
    1. 时区：swinst → 2 Expert → 6 System management → 1 Date & Time update → 2 Set timezone（Tab/方向键选择）→ 确认 → 重启（Warning）。
    2. 加 NTP 服务器：同路径 → 3 NTP server management → 5 Modify NTP configuration → 2 Add/Modify server → 192.168.1.252（实验口径）→ key 0 / burst n / iburst n / prefer n → 确认 → 1 View configured servers 核对。
    3. 制造时差：mtcl 下 date 看当前；swinst 路径把 OXE 日期改偏 1 个月。
    4. 瞬时同步：NTP 菜单确认 NTP is stopped → 4 Instant synchronisation → 输 192.168.1.252 → 回车 → 日期恢复；注：chronyd 运行中不可做。
    5. 渐进同步：NTP 菜单 → 1 Start NTP（chronyd）→ 状态 NTP is running。
    6. 巡检：ps -edf | grep chronyd；chronyc sources（^* = 已选中源）；chronyc clients（root）；systemctl status chronyd；lsof -i:123（root）；chronyc ntpdata（root）；more /etc/chrony.conf。
  verification: |
    chronyc sources 显示 ^* ntp1；systemctl status 显示 active (running)；时间与 NTP 服务器一致。
  conditions: NTP 服务器为实验环境 IT Server（实验口径）；时区改动必须重启。
  tags: [lab, ntp, chrony, time]

- id: c06
  title: 空数据库创建（停话务→建库 FR→Direct Link→恢复许可→起话务）
  type: lab
  source_pages: p189-193
  source_chapter: Empty Database Creation (How-To)
  source_quote: |
    "THIS OPERATION OVERWRITES THE EXISTING DATABASE AND THE SOFTWARE LICENSE FILES. IT CAN ONLY BE PERFORMED IF THE TELEPHONE APPLICATION IS STOPPED." (p190)；
    "Enter the country name symbol (0 to Quit). Your choice: FR … The country chosen to initialize the empty database will be FRANCE (5)." (p191-192)
  steps: |
    1. 停话务：swinst → 1 Easy → 7 Stop the telephone → y（系统重启、Autostart is not set、等 csa login:）。
    2. 建库：swinst → 2 Expert → 7 Database tools → 2 Create an empty database → y 确认（"Warning, the current database will be erased"）→ RUN_MKBDD 执行 → 输国家码 FR（培训约定；现场用真实国家码）→ Create entire database y → Direct Link Network y（自动建 99 条 ABC-F 直连）→ 记录空库上限（Users 10014 / 1/2 com 3859）→ 参数表 0 退出。
    3. 重启：shutdown -r now（Note：建库后重启 CPU 再起话务）。
    4. 恢复许可（见 c07）。
    5. 起话务：swinst Easy → 8 Start the telephone → y → 等 "No problem with compatibilities" 或登录提示。
  verification: |
    系统以 FR 空库运行；ednump 可见默认编号计划（51/41/42/43 等）；许可计数经 spadmin 恢复非 0。
  conditions: 国家码 FR 为实验口径；空库必然抹许可，顺序不可乱。
  tags: [lab, database, empty-db, swinst]

- id: c07
  title: OPS 许可恢复/备份与 FlexLM 对接、spadmin 巡检
  type: lab
  source_pages: p210-223
  source_chapter: OPS Files Restore & Backup (How-To)
  source_quote: |
    "Transfer type Binary … Remote site Select the folder /usr4/BACKUP/OPS" (p211-212)；
    "Do you agree the new software keys (y/n): y … Enter OPS working mode : 1=running 2=simulate (default is 1): 1 … ops 2.0.2: operation successful" (p214)；
    "YOU NEED TO RESTART THE CALL SERVER!" (p219)
  steps: |
    1. 取许可文件（讲师/NAS，实验口径）到 PC。
    2. 传输：FileZilla → Transfer 菜单设 Binary → SFTP mtcl@192.168.1.3 端口 22 → 远端 /usr4/BACKUP/OPS ← 拖入 TJ00302A.hw/.swk/.zip/hardware.mao。
    3. 安装：swinst → 2 Expert → 5 OPS configuration → 2 Restore OPS from cpu disk → y → 核对文件清单 → Do you agree the new software keys y → 运行模式 1 →（示例输出含 "30 remaining day(s) to fix this issue"=CPU-ID 宽限提示）→ "ops 2.0.2: operation successful"。
    4. 备份：同菜单 → 1 Backup OPS files on cpu disk → y → 文件落 /usr4/BACKUP/OPS → FileZilla 拖回 PC（例 C:\Soft\OPS Backup\）。
    5. FlexLM（虚拟机环境）：浏览器 https://192.168.1.3（WBM）→ mtcl 登录 → System/Licenses → FlexLM Licensing Enabled=Yes、Flex Server IP=192.168.1.80、端口 27000、Product ID discovery=Yes、Use Flex License=No → 重启 CS（Warning）。
    6. 巡检：spadmin → 1（PANIC 旗标/计数）→ 2（活动文件：Soft Key/Cpu Id/Product-Id/锁清单）→ 3（File OK / Error: Illegal hardware key）→ 10（FlexLM check OK/NOK 两种失败文案）。
  verification: |
    spadmin 选 3 显示 File OK；选 10 显示 license check OK；锁计数（SIP users 2/15、OMS 3、120 通道等）与许可一致。
  conditions: 虚拟环境用外部 FlexLM；许可文件为实验口径。
  tags: [lab, ops, licensing, spadmin, flexlm]

- id: c08
  title: GD4 硬件媒体网关上架（Shelf/板卡/mgconfig/MAC/压缩器/维护命令）
  type: lab
  source_pages: p245-258
  source_chapter: Hardware Shelves & Boards (How-To)
  source_quote: |
    "ALL SHELVES AND BOARDS ARE AUTOMATICALLY CREATED ACCORDING TO THE OPS CONTENTS (HARDWARE.MAO)" (p246)；
    "Enter new crystal number [1..255] (values 18 and 19 are not allowed): 2 … Configuration saved at /etc/config/local/ipmg.cfg … Do you want to reboot now ? (y/n) y" (p250)；
    "IF YOU USE THIS COMMAND ON A GD4 BOARD, ALL BOARDS OF THE SHELF WILL BE RESTARTED!" (p257)
  steps: |
    1. WBM → Shelf：Create 或改 OPS 自动建的机架——Shelf address=2（=crystal number）、Type=Media Gateway Small（1U）/Large（3U）、Name、Role=Main(Master)（扩展架=Expansion 1/2 且填 Main Shelf Address；主架 0 槽自动生成 GD4）。
    2. 板卡：Shelf/2/Board → Create/修改——Board address+Interface Type（MG-MIX、BRA 4、UAI 8、SLI 4；Common HW 板名带 MG- 前缀）。
    3. GD4 板侧：V24（115200；root 默认 mg4.ale、admin 默认 letacla1，首连强制改密）或 SSH（ssh admin@<GD4 IP>，仅 CS 发起）→ root 登录 → mgconfig：1 IP N/W Mode（IPV4only）→ 2 View/Modify IP Addresses：IPv4=192.168.1.12、掩码、网关 192.168.1.254、CPU role address=192.168.1.3 → 3 Crystal number → 2 切手动 → 3 改为 2 → 0 退出 → 保存 y → 重启 y → 信令链初始化。
    4. CS 库侧：IP/INT/IP Parameters/"Ethernet Address checked by TFTP"——自动 crystal 或 DHCP 时勾选并到 Shelf/2/Board/GD4/Ethernet Parameters 登记 MAC（00:80:9F:FE:3A:50 示例；换板必须更新）。
    5. 压缩器：Shelf/2/Board/GD4 → Daughterboard=None/ARMADA、No. Of Compressors=30（+ARMADA=60，许可 #135）→ rstcpl 2 0 生效。
    6. 维护：config 2（整架）/config 2 0 -d（含子板）/config 2 -v（虚板 BRA4/UAI8/SLI4/GPA FICTIF）/config all（虚架 0 与 19）/cplstat 2 0（IP+GD 参数）/rstcpl 2 1（INIT1→INIT2→IN SERVICE）/listout 2 1（离服原因码）。
  verification: |
    config 2 显示 GD4 与 MIX484 均 IN SERVICE；cplstat 2 0 显示板 IP/CS role 正确；板重启后经 INIT 1/2 回到 IN SERVICE。
  conditions: crystal 手动+静态 IP 时无需登记 MAC；实验地址实验口径。
  tags: [lab, gd4, shelf, mgconfig, hardware]

- id: c09
  title: OMS 虚拟媒体网关上架（强制字段/omsconfig/资源声明）
  type: lab
  source_pages: p259-268
  source_chapter: Software Media Gateway - OXE Media Service (How-To)
  source_quote: |
    "Shelf Type 'Media Gateway Large'; this type is MANDATORY for OMS declaration … OXE Media Server YES; MANDATORY … OF COURSE, DO NOT DECLARE NEITHER SECONDARY RACKS NOR BOARDS IN THIS SHELF!" (p260-261)；
    "sudo omsconfig … Enter new crystal number [1..255] (values 18 and 19 are not allowed): 4" (p263-264)
  steps: |
    1. 确认 OPS 恢复后 OMS 自动建为 Shelf 4（实验口径）。
    2. WBM Shelf：核对/创建——Type=Media Gateway Large、Role=Main(Master)、OXE Media Server=YES（三者强制）；不加扩展架与板卡；虚 GD4 自动在 0 槽。
    3. VM 侧键盘（可选）：OMS 控制台 → kb/kb 登录 → 选键盘布局（Rocky Linux 9.6）。
    4. IP 配置：OMS 控制台 admin/letacla1（改密）→ sudo omsconfig（或 root 下 omsconfig）：1 IPV4only → 2 IP 地址=192.168.1.13/掩码/网关 192.168.1.254/CPU role=192.168.1.3 → 3 Crystal number → 手动 4 → 保存 y（/home/mnt/flash/oms/oms.cfg）→ 重启 y。
    5. MAC 登记规则同 GD4（Ethernet Address checked by TFTP 两情形）。
    6. 资源：Shelf/4/Board/GD4 → 压缩器 30（上限 120，许可约束）、Max simultaneous voice guides=16、Max 3-part conference=3（≤压缩器/3）→ 改后 reset OMS（rstcpl 4 0）。
    7. 巡检：spadmin 选 2 查 #384 OXE Media Servers=3、#385 VoIP channels on OMS=120；config 4 0（GD4 OXE MS IN SERVICE）；cplstat 4 0。
  verification: |
    config 4 0 显示 GD4 | OXE MS | IN SERVICE；spadmin #384/#385 与许可一致。
  conditions: OMS 默认口令 admin/root 均 letacla1（与 GD4 不同）；实验地址实验口径。
  tags: [lab, oms, omsconfig, virtual-mg]

- id: c10
  title: IPDSP 软话机部署（建户/装软件/TFTP/注册/端口附录）
  type: lab
  source_pages: p308-314
  source_chapter: IP Desktop SoftPhone (How-To)
  source_quote: |
    "Directory Number: 31000 … Set type: IP Touch 8068s … IP-Softphone emulation Yes" (p309-310)；
    "Warning: IPDSP will not come in service if there are no audio devices in the PC" (p310)；
    "Enter the user directory number, created in the OXE database (e.g. 31000) … (default: 0000)" (p312)
  steps: |
    1. WBM → Users → Create：DN=31000、姓名 Barkley Brad、Set type=IPTouch 8068s、Shelf/Board/Equipment 保持 255。
    2. User → TSC IP user → 选 31000 → IP-Softphone emulation=Yes。
    3. PC 安装 IPDesktopSoftphone_xx.x.x.msi（NAS 取，实验口径）。
    4. 首启：Settings → 填 TFTP server（main=192.168.1.3；空间冗余再填 backup）→ TFTP-HTTPS order 选 TFTP（HTTPS 用于原生加密拉 lanpbx.cfg）→ Apply。
    5. 注册：再启动时按提示输分机 31000 + 密码（默认 0000）→ IPDSP 在服。
    6. 设置巡检：右键 → Settings（语言/皮肤/网络/快速键/AOM 键盘类型 AOM10/40/EL 需与 OXE 一致）。
    7. 防火墙：按附录端口表（UDP 10000-10499/32512-32515/32640-32643/32512-33023/28000-39999；TCP 2535）放行。
  verification: |
    IPDSP 显示在服并可通话；ippstat 选 3 能看到 31000（Ipt 8068s）。
  conditions: PC 必须有音频设备；安装包为实验口径。
  tags: [lab, ipdsp, softphone, users]

- id: c11
  title: User Profile 模板化建户
  type: lab
  source_pages: p315-319
  source_chapter: User Profiles (How-To)
  source_quote: |
    "'User profiles' are created in the regular 'Users' menu with a specific setting: 'Set Function = Profile'. … It can be interesting to use a 'physical' directory number, that means, a directory number beginning by a letter (A, B, C, D)" (p316)；
    "Profile Name Enter a name in capital letters (e.g. IPDSPPROFILE)" (p317)
  steps: |
    1. 建 Profile：WBM → Users → Create：DN=A31250（字母开头、永不被拨打）、Set type=IPTouch 8068s、Set Function=Profile → Profile 页签 → Profile Name=IPDSPPROFILE（必须大写）。
    2. 查看：Users 对象下不可见 → 过滤器 Set Function=Profile → 选 A31250 → TSC IP user → IP-Softphone emulation=Yes。
    3. 按模板建户：WBM → Users by profile → Create：DN=31001 Backman Billy、Set type=IPTouch 8068s、Station profile from=A31250；同法 31002 Boop Betty。
    4. 在 Users 菜单确认新建用户已继承模板参数。
  verification: |
    Users 列表出现 Billy Backman/Betty Boop 且携带模板设置（含 IP-Softphone emulation）。
  conditions: Profile 名必须大写；非强制用法（可选提效手段）。
  tags: [lab, users, profile, bulk]

- id: c12
  title: IP 话机静态 IP 开通与换机/日志维护
  type: lab
  source_pages: p320-329
  source_chapter: IP Desk phones (How-To)
  source_quote: |
    "Directory Number: 31011 … Set type: ALE-300" (p321)；
    "The IP parameters can only be modified during the set startup phase … If the set is already started, you will have to reboot it to access to the configuration interface" (p322)；
    "The secret code by default for all the users is: '0000'" (p325)
  steps: |
    1. 建户：Users → Create：31011 Cartier Calixta、Set type=ALE-300。
    2. 话机静态 IP：重启话机 → 无屏按 #+*、触屏点设置图标→Config. MMI → IP Parameters → IP Config → IPv4 Wired → Network Settings → IPv4 Mode=Static → IP Addr=192.168.1.141、Subnet=255.255.255.0、Router=192.168.1.254 → ✓ → System Settings → TFTP #1=192.168.1.3（TFTP #2=空间冗余第二主址）→ ✓ → 退出。
    3. 注册：按任一键 → 拨自己分机 31011 → 密码 0000 → 自动重启入服（必要时自动升级 binom）。
    4. 核对：WBM Users/TSC IP user → Terminal Ethernet Address 已填 MAC。
    5. 换机：Users/TSC IP → 删旧 MAC 填新 MAC。
    6. MAC 检索：背面贴纸 或 话机菜单 Hardware infos → MAC Address。
    7. SSH 上话机：CS 上 tnet d 31011。
    8. 日志：话机上 getlogs；CS 上 ippstat → 15 → 输 31011 与超时 1440 分钟（0-1440）开 SSH → FileZilla SFTP admin/*tx8000#（默认）→ 取 /var/volatile/tmp 下日志包。
  verification: |
    31011 IN_SERV（termstat d 31011）；WBM 中 MAC 已登记；getlogs 文件可取回。
  conditions: IP 参数仅启动期可改；*tx8000# 为话机默认 SFTP 口令（实验口径提示生产必改）。
  tags: [lab, ip-phone, static, maintenance]

- id: c13
  title: 数字/模拟用户创建与状态巡检（termstat/eqstat/edsbr/outserv）
  type: lab
  source_pages: p330-341
  source_chapter: Digital Deskphones & Analog Sets (How-To)
  source_quote: |
    "Directory Number: 31020 … Set type: depends on the set available in the training room (e.g. ALE-30h TDM) … Automatic Allocation … the directory number and the secret code will be asked." (p331)；
    "(1)csa> outserv d 31020 … Do you really want to put out of service this device ? (Y/N) :y" (p340)
  steps: |
    1. 数字用户（自动分配）：Users → Create：31020 Douglas David、Set type=ALE-30h TDM、Shelf/Board/Equipment 留自动（可加 Add On Module EM200）→ 话机插线后输分机+密码入服。
    2. 模拟用户（手工分配）：Users → Create：31021 Duncan Deborah、Set type=ANALOG、按平台填 Shelf/Board/Equipment。
    3. 板状态：WBM Shelf/<n>/Board（Operational State 只读）；CLI config 2 / config 2 -v（MIX484 物理板映射虚板 BRA4@9/UAI8@10/SLI4@11、GPA FICTIF@27）。
    4. 用户状态：WBM /User/<n>/Dynamic State User；CLI termstat d 31020（选项 1 特性/2 呼转/3 关联/4 通话/5 重启；语法 d=分机、n=Neqt、p=架 板 0 端口）；eqstat d 31020。
    5. 呼转查询：listfwd；DND：listdnd；锁定：listloc；通话中：listincall。
    6. 板上用户：listerm 2 1。
    7. 订户检索：edsbr -l GEA → ? * 看属性（dir/m_dir/act/cpl/pos/typ/name）→ 逐个加入 → go 出报表。
    8. 摘/挂服：outserv d 31020 → y；inserv d 31020 → y（移动工位免跳线场景）。
  verification: |
    termstat d 31020 显示 IN_SERV/ALE-30h TDM；edsbr 报表含全部实验用户；outserv 后终端离服、inserv 恢复。
  conditions: 自动/手工分配区别见 p19；TDM 功耗约束见 principle p18。
  tags: [lab, tdm, analog, termstat]

- id: c14
  title: CS 内部 DHCP 服务器与动态模式话机开通
  type: lab
  source_pages: p355-365
  source_chapter: IP Desk Phone, in dynamic IP mode (How-To)
  source_quote: |
    "Configuration DHCP Server … Alcatel terminals only Yes" (p356)；
    "First address in range 192.168.1.145 … End of address range 192.168.1.149" (p358)；
    "WARNING : the following trusted hosts are DHCP addresses declared by MAO, they cannot be modified by netadmin." (p364)
  steps: |
    1. 开 DHCP：WBM → DHCP Configuration → Review/Modify → Configuration DHCP Server：Configuration=DHCP server（默认 off）、Alcatel terminals only=Yes。
    2. 全局参数：CPU Main Subnetwork：subnet 192.168.1.0/掩码/广播 192.168.1.255；Default router 与 TFTP 留空（分别取 netadmin 网关与 CS IP）。
    3. 地址池：IP Address Range (local subnet) → Create：192.168.1.145-192.168.1.149（单 IP 两栏同值）。
    4. Apply Modifications（Warning：dhcpd 重启读 /etc/dhcpd.conf）。
    5. 建户：31010 Cooper Charles ALE-500、31012 Connor Caitleen ALE-20h IP。
    6. 话机保持 Dynamic 模式（切换路径同静态实验）→ 启动后输分机+密码入服。
    7. 巡检：ps -edf | grep dhcpd；more /etc/dhcpd.conf（vendor id alcatel.a4400.0、租期 3600、range 与 next-server）；netadmin -m → 11 → 1 → 3 → 1 查看（DHCP 段标记为 MAO 声明、不可改）；netadmin -m → 12 → 1 查看已分配 → 2 释放（s 单地址）；root 下 dhcplease / -t / -a；root 下 more /var/log/dhcplog（DISCOVER/OFFER/REQUEST/ACK、CLASS_IDENTIFIER=alcatel.noe.0）。
  verification: |
    话机经 DHCP 获得 192.168.1.145-149 段地址并入服；dhcplog 显示完整四步交互；防火墙自动含该段。
  conditions: 客户已有 DHCP 时改走客户侧；实验地址实验口径。
  tags: [lab, dhcp, dynamic, ip-phone]

- id: c15
  title: 前缀/后缀管理与编号计划巡检
  type: lab
  source_pages: p382-388
  source_chapter: Prefix & Suffix Plan (How-To)
  source_quote: |
    "Number Prefix Number. Must be unique in the OXE system numbering plan … Prefix Meaning Purpose of the prefix (ex. Set features)" (p383)；
    "Number 51; in this OXE system database, 'Immediat forward' prefix value is '51'" (p385)
  steps: |
    1. 说明：空库已按国家码生成默认前后缀，本章不新建特定前缀（后续实验再建）。
    2. 前缀创建路径：WBM → Translator/Prefix Plan → Create：Number（唯一）+Prefix Meaning（Set features 时还需 Station Features 选择具体功能；Local/External/General features 同理）。
    3. 后缀创建：Translator/Suffix Plan → Create：Number+Suffix Meaning。
    4. 过滤器练习：Translator/Prefix Plan 过滤 Prefix Meaning=Set features 且 Station features=Immediate forward → 得 51；同法查 Forward cancellation/Do not disturb/Wake-up/Last Caller Callback。
    5. 巡检：CLI ednump -l GEA（属性 dir/mean；CTRL C 退出）——核对 FR 库默认（400 在/离服、401 录音指南、402 停车、405 改密、41/42/43、505 替代、506 叫醒、51 立即呼转等 88 行）；listrad（选 1 显示全部翻译器条目：Tsl_CH_Local_Station/Tsl_Forwarding_Cancellation 等）。
  verification: |
    过滤器定位功能前缀正确；ednump/listrad 输出与库内配置一致。
  conditions: 改前缀须同步核对语音指南播报（p431 Caution）。
  tags: [lab, numbering, prefix, suffix]

- id: c16
  title: Phone Features COS 管理（强插保护/功能禁用/摘机路由/默认溢出）
  type: lab
  source_pages: p400-409
  source_chapter: Phone features Class of Services (COS) (How-To)
  source_quote: |
    "Protected against all barge-in (intrudes): 1 … Now, you should be allowed to do a call intrusion" (p401-402)；
    "Routing mode at off hook … 'Direct Routing': for the set to be routed to a number as soon as it is off hooked." (p406)；
    "Timer units 150 (by default). Timer is managed by step of 100 ms (so 150 * 100 ms = 15 sec)" (p409)
  steps: |
    1. 强插保护基线：三个用户（310x0/1/2）同用 COS#0（三项保护默认 1）→ 310x2 呼 310x0 尝试强插应被拒。
    2. 放开强插：COS#11 三项保护改 0 → COS#0 的 Suffixes/Barge-in=1 → 用户挂接（Users → Phone Features COS 11/0）→ 310x2 强插成功 → 恢复 COS#0。
    3. 禁功能：COS#0 → Set features/Immediate forward=0 → 310x2 拨 51 应被拒（Feature Forbidden）→ 测完恢复 1。
    4. 摘机路由：COS#31 → Routing mode at off hook=Direct Routing；Specific Telephone Services/Routing Table → Create：Routing No=1、Call number=310x0 → 用户 31010 挂 COS31+Routing table 1 → 摘机直达 310x0 → 恢复（Direct/Delay(timer2)/Specialized incoming/NO Routing/External Alarm 五模式口径）。
    5. 默认溢出：COS#2 → Default overflow type=forward on no answer、address=associated set → 用户 310x1 挂 COS2+关联机=310x2 → 310x0 呼 310x1 不接 → Timer 4（默认 150=15 秒）后 310x2 振铃；可到 System/Timers 调 Timer #4 → 测完恢复。
  verification: |
    强插行为随 COS 开关变化；51 前缀在禁用时报 Feature Forbidden；摘机直达与无应答溢出按预期触发。
  conditions: 摘机路由实验需至少一台硬话机；测试后一律恢复 COS#0。
  tags: [lab, cos, routing, timers]

- id: c17
  title: Connection & Transfer COS 矩阵管理
  type: lab
  source_pages: p421-424
  source_chapter: Connection & Transfer COS (How-To)
  source_quote: |
    "Allocate the Connection (and Transfer) COS '1' to the users with 'odd' directory numbers (310x1) … COS '2' to the users with 'even' directory numbers" (p422)；
    "Connection COS 2 (assigned to 'even' number users) COS 1 0; forbids direct calls from 'even' to 'odd' number users" (p423)
  steps: |
    1. 用户分配：WBM Users → Rights 页签 → 奇数号用户（310x1）Connection COS=1；偶数号（310x0/2）=2（Transfer COS 同 ID、矩阵独立）。
    2. 连接矩阵：Classes of Service/Connection COS → 选 1 → COS2 行=1（允许奇打偶）；选 2 → COS1 行=0（禁止偶打奇）。
    3. 测试：奇→偶通；偶→奇被拒。
    4. 转移矩阵：Classes of Service/Transfer COS → 选 2 → COS2 行=0（禁止偶↔偶转接）→ 测试：310x1 呼 310x0 → 310x1 发起 enquiry 呼 310x2 → 尝试把第一路转给 310x2 → 应被拒。
    5. 复位：全部用户 Connection COS 恢复 0。
  verification: |
    奇偶互拨行为与矩阵一致；转接在 COS2×COS2 格为 0 时被拒。
  conditions: 无。
  tags: [lab, connection-cos, transfer-cos]

- id: c18
  title: 静态语音指南与音乐保持部署（传输/语言索引/MOH 激活/试听）
  type: lab
  source_pages: p439-448
  source_chapter: Static Voice Guides (How-To)
  source_quote: |
    "Transfer the 3 files: 'vgadpcm.EN0' 'vgadpcm.FR0' 'adpcmmoh' in the right directory" (p440)；
    "Delete tone N° 2 and create VG N° 2 for MoH" (p442)；
    "From a set, dial the prefix « 580 » followed by the VG number on 4 digits. … 'Music On Hold' can be listened by dialing 580 0002" (p447)
  steps: |
    1. 传输：FileZilla SFTP（mtcl@CS，端口 22）→ 把 vgadpcm.FR0/vgadpcm.EN0/adpcmmoh（CD-ROM \VG_6.0\guides_generic\…、\VG_6.0\musicalcatel\alaw）传到 /DHS3ext/vgadpcm/flash/std。
    2. 语言索引：WBM → System/Flash Voice Guide configuration → 核对 Index 1=法语、Index 2=英语…（1-8，国家相关）。
    3. 槽位关联：Shelf/<架>/Board/<GDx>/Voice Guide Index MG → Create：VG Item=内存槽（1-4 静态）+语言索引（MOH 不占语言索引；例 Slot1=Index1、Slot2=Index2、Slot3=On hold music）。
    4. MOH 激活：System/Tones → 删 Tone 2；System/Voice Guides → Create VG 2 → 法一 Single-message Voice guide（Flash message for language X=2，可按语言给不同等待音）/法二 Music On Hold Voice guide（Flash message on hold music=2、Listening Class 0=Allowed with no control）。
    5. 实体等待指南：Entities → 实体 1 → Waiting guide=2（默认）。
    6. 巡检：config 4 -v（GPA FICTIF@27 IN SERVICE）；vgstat 4 0（Slot1 FR0/Slot2 EN0/Slot3 On hold music/Slot5 动态区 3684 秒/消息清单）；vgemis（正在播放）；vgstart（起始播放口径）；incvisu（0260/0261 下载事件）。
    7. 试听：确认用户 COS 允许 Tones test → 话机拨 580+4 位（580 0002=MOH）→ 以用户语言播放；核对 Users Language ID 与 System/Language Choice 映射。
  verification: |
    vgstat 显示两语言+MOH 已入槽；话机保持时听到音乐；580 试听正常。
  conditions: 语言映射改动需重启 CS；改编号计划后核对指南播报。
  tags: [lab, voice-guides, moh, vgstat]

- id: c19
  title: 话务台组与 4059EE 部署（组/话务台/CDT/BLF/系统参数/巡检）
  type: lab
  source_pages: p479-495
  source_chapter: Call distribution and attendants (How-To)
  source_quote: |
    "Physical Directory No. A0000 … Attendant group Id 0 … Name GROP1 … Max. No. of Calls Bef. Overfl. 5" (p481)；
    "The 4059 EE handles the specific functions of the attendant but not the voice. It is mandatory to associate a physical set (ALE series) or an IP Desktop Softphone." (p484)；
    "grpopestat 0 … etat_phys :PRESENT … etat_log :DAY" (p494, p519)
  steps: |
    1. 建组：WBM /Attendant/Attendants group → Create：Physical DN=A0000、Id=0、Name=GROP1、Max. No. of Calls Bef. Overfl.=5、Traffic Overflow（Day/Night/Mode1/Mode2 可填）；组 CDT 自动生成。
    2. 组前缀：Translator/Prefix Plan → 31400=Attendant Group Call、Prefix Information=组 ID 0。
    3. 话务语音用户：Users → Create 31003 Attendant Phone、IPTouch 8068s、IP-Softphone emulation=Yes（Warning：禁 multiline）。
    4. 建话务台：/Attendant/Attendant sets → Create：Physical DN=B0000、Attendant Id=0、Group Id=0、Shelf/Board/Equipment=255、Set Type=4059 IP、Associated phone set=31003。
    5. 装 4059EE（4059EE_x.x.x.exe；RLAB 不装 ALE USB 键盘）；放行防火墙 4059EE+abcacom.exe（培训环境可关防火墙）；以管理员运行 → Settings → System Settings-PCX Connection → add 设备 B0000@192.168.1.3（空间冗余可 3 主机逗/分号分隔）。
    6. 注册核对：/Attendant/Attendants sets/Ip phone Attendant → B0000 的 Terminal Ethernet Address/IP 自动回填；File → Sign on 上线。
    7. 系统参数：/System/Other System Param./Attendant Parameters：4059 Close auto sign off=True、4059: PC unregistered at logoff=True。
    8. 话务台前缀：31401=Indiv. Attendant Call（info=话务台 ID）；Phone Book 建 31401 Welcome Desk（可 Called/Dial by name=Yes，来电显示话务台名）。
    9. CDT：/Attendant/Attendant Group Call Distribution：Overflow Routing No=31000（单线）、Day Routing1=A0000；/Attendant/Attendant Call Distribution：Day Routing1=B0000。
    10. BLF：4059EE Settings/General 勾 Enable Busy lamp field → BLF 面板右键 Add item → User → Brad Barkley 31000。
    11. 巡检：grpopestat 0（PRESENT/DAY、max_grp_call 5）；opstat（IDLE/B0000/DAY）；cdtstat -g 0 / -a 0（poste_nuit 31000、DAY 路由）；ippstat d B0000。
  verification: |
    4059EE Sign on 后 grpopestat=PRESENT/DAY；拨 31400/31401 白天振铃话务台、夜间落 31000；BLF 显示 31000 状态。
  conditions: RLAB 口径：PC 防火墙放行或关闭；4059EE 关联分机禁 multiline。
  tags: [lab, attendant, 4059ee, cdt, blf]

- id: c20
  title: Entity 管理（经理组/状态小时表/实体前缀/CDT/实体指南）
  type: lab
  source_pages: p514-525
  source_chapter: Entity (How-To)
  source_quote: |
    "Declare the Attendant group A0000 (ID: 0) as Entity '1' attendant group manager." (p515)；
    "Number 31100 … Prefix Meaning Entity/CRG Call … Prefix Information Entity number (1)" (p520)；
    "entitystat 1 … group_manager : 0 … music : 2 … Location ID :" (p523)
  steps: |
    1. 用户归属核对：Users → Entity Number=1（默认）。
    2. 经理组：Entities → 实体 1 → Attendant Group Manager=0（实体状态随后跟随组状态）。
    3. 状态小时表：Entities/Entity Incoming State Hours → 实体 1 → 周一至周日各天默认配 "Attendant Group"（也可自定义 4 切换时点，如 8-12 Day/12-13:30 Mode1/13:30-19 Day/19-次日 Night）。
    4. 话务台切换权：/Attendant/Attendant sets → 实体状态 Night/Day/Mode1/Mode2 各设 Allowed with no control → 4059EE：Service mode 图标 → Service/Status programming/Entity status → 双击选状态。
    5. 实体 CDT：Entities → 实体 1 → Overflow Routing No.=31000、1rst Day Routing=A0000。
    6. 话务台前缀核对：Translator/prefix plan → 9=Attendant Call（按国家码 9 或 0）→ 测试：B0000 Sign on → grpopestat 0=PRESENT/DAY → 拨 9 应落 A0000；Sign off → grpopestat 0=DISCONNECTED/NIGHT → 拨 9 应落溢出号 31000。
    7. 实体前缀：Translator/prefix plan → Create：31100=Entity/CRG Call、info=1 → 拨 31100 验证按实体状态路由。
    8. 实体指南：Entities → 实体 1 → Waiting guide=2（MOH）；Attendant waiting guide=110；System/Other System Parameters/Attendant Parameters → Play VG for internal Caller=True（内呼播 110）。
    9. 巡检：entitystat 1（状态/group_manager/music/language）；entitystat -b 1（出入向时间表，代码 0=Night 1=Day 2=Mode1 3=Mode2 4=Same As Group）；cdtstat -e 1（CDT idx、poste_nuit、DAY 路由）。
  verification: |
    话务台上下线驱动实体 Day/Night 切换；31100 按实体状态路由；内呼话务台听 110 指南。
  conditions: 溢出号必须单线分机；实体状态切换权需预先授予。
  tags: [lab, entity, cdt, state-hours]

- id: c21
  title: OmniMessage 4645 部署（许可/库内声明/邮箱分配/首访/语言上传）
  type: lab
  source_pages: p547-556
  source_chapter: OmniMessage 4645 (How-To)
  source_quote: |
    "178 4645 Voice mail engine = 1 … 179 M 4645 users = 0/ 15 … 182 4645 networking = 1 … 183 4645 additional language = 5 … 194 4645 Portal users = 15" (p548)；
    "Voice Mail Dir. No. … 31499 … Voice MailType … 4645 … Voice Mail CPU Name Physical address of the call server (192.168.1.1 in our case)" (p549)
  steps: |
    1. 许可：spadmin 选 2 核对锁 178（engine）/179（users 0/15）/182（networking/VPIM）/183（语言 5）/194（portal 15）。
    2. 库内声明：WBM → Applications/Voice Mail → 实例 1：Voice Mail Dir. No.=31499、Directory Name=Voice Mail、Type=4645、Number of accesses=4、Voice Mail CPU Name=192.168.1.1（物理地址，勿用 Role 地址）→ 声明后自动生成一个机架。
    3. 分配邮箱：Users → 31000 → Voice mail 页签：Voice Mail Dir. No.=31499、4645 Voice Mail Type=Standard、4645 Class of Service=1。
    4. 首访：31000 话机拨 31499 → 初始码 0000 → 新码（例 2580）→ # → 录姓名 → # 确认。
    5. 留言/收听：31000 设立即呼转至留言箱 → 31001 呼入留言 → 31000 收通知并进信箱听/删。
    6. 语言：Applications/Voice Mail/4645 VM Global Parameters 核对语言；SFTP（FileZilla mtcl@CS 端口 22）把 evavg.FR0 等传到 /DHS3ext/vgeva → 重启 VM 系统（rstcpl 18 1）→ 让用户（例 Barkley language 2）进信箱验证法语提示。
    7. 巡检：config 18（GD+4645 耦合器 IN SERVICE）；more /usr3/mao/eva.cfg（callserver1/eva/eva_access=4）；Eva_tool → 5 → 1（信箱清单：Administration/Default AA/31000；网络信箱 0/48000）。
  verification: |
    4645 耦合器 IN SERVICE；31000 信箱可留言收听；上传语言后提示语切换。
  conditions: 4645 为软件方案（嵌 CS 拓扑）；CPU Name 用物理地址。
  tags: [lab, 4645, voicemail]

- id: c22
  title: 4645 邮件通知（SMTP 声明/防火墙/CoS 三档/Thunderbird 验证）
  type: lab
  source_pages: p556-571
  source_chapter: 4645 e-mail notification (How-To)
  source_quote: |
    "Host name ? mailserver.company.com … Host address ? 10.20.30.200" (p558)；
    "SMTP server URL ? mailserver.company.com … SMTP protocol (1.Plain / 2.startTLS / 3.TLS) ?1 … SMTP port number ?25" (p559)；
    "E-mail notification None: no notification (default value) … Advanced: email notification with audio file attachment" (p564)
  steps: |
    1. 主机表：netadmin -m → 9 Host names and addresses → 1 → 2 Add/Update：mailserver.company.com=10.20.30.200（实验口径）→ a。
    2. SMTP：netadmin -m → 21 SMTP server configuration → 2 Create/Update：URL=mailserver.company.com、用户/密码可空、protocol 1=Plain、port 25、from 地址可空（Note：按发件域过滤的 SMTP 会把异常域判垃圾；缺省用 OXE 域名）→ a 应用；复制/双 CPU 口径：twin 上同步配置、独立 4645 CPU 时必须在该 CPU 配。
    3. 防火墙：root → netadmin -m → 11 → 1 → 3 → 2 加可信主机 mailserver.company.com=10.20.30.200 → a。
    4. 重启 OXE 生效。
    5. 公开号码：Eva_tool → 17 → VM DDI=33210x41499（x=POD 号）→ 加 + 前缀 y。
    6. CoS：Applications/Voice Mail/4645 VM Classes of Service/<CoS>：E-mail notification=None/Basic/Advanced、Quota Size Limit Notification（百分比）、Email Attachment Size Limit（MB）、Treat msg as read。
    7. 用户：Users → Mail Address=barkley.podx@company.com + 挂 4645 CoS + Voice Mail Dir. No.=31499。
    8. 验证：Thunderbird 配 IMAP（mailserver.company.com、IMAP 143/SMTP 25、Normal password、密码 alcatel 实验口径）→ 31001 呼 31000 留言 → 收 Basic 邮件 → CoS 切 Advanced 再测附件。
    9. 巡检：Eva_tool → 5 → 2（信箱详情含 mail_address）；5 → 8（CoS：Email Notification 0/1/2、Max messages 20、password_valid 180 等）；ping FQDN；/var/log/maillog（TLS 日志）与 /var/log/syslog（root）。
  verification: |
    留言后邮箱收到通知（Advanced 含 .wav 附件）；Eva_tool 信箱显示 mail_address；CoS Dump 显示 Email Notification 档位。
  conditions: SMTP 服务器为实验环境；外线留言验证需待 SIP 中继实验完成后回归。
  tags: [lab, 4645, smtp, email-notification]

- id: c23
  title: 公共 SIP 中继开通全链路（系统参数→TG→网关→ARS→鉴别符→NPD/DID→回叫→国际/紧急）
  type: lab
  source_pages: p609-640
  source_chapter: SIP Carrier access (How-To)
  source_quote: |
    "ARS IS REQUIRED TO USE SIP TRUNK GROUP WITH AN EXTERNAL SIP GATEWAY" (p616)；
    "Trunk Group ID 1 … Q931 Signal variant + ISDN all countries … T2 Specification SIP" (p613)；
    "sipextgw -l … IN SERVICE SIP external gateways list : 1" (p637)
  steps: |
    1. 系统参数：System/Other System Param./System Parameters → Law=A Law（欧洲）；Compression parameters → G722/OPUS support perimeter=Network and local（Warning：系统级不放行则网关级开了也无效）。
    2. TG：Trunk Group → Create：ID=1、Type=T2、Node=1、Q931 variant=ISDN all countries、T2 Specification=SIP、DID transcoding 暂 No。
    3. 外部网关：SIP/SIP Ext Gateway → Create：ID=1、Name=ITSP1_GW1、SIP Remote domain=sip.itsp1.fr、Port=5060、UDP、Belonging Domain=sip.itsp1.fr、Registration ID=pbx<N>、Registration timer=600、Outbound Proxy=gateway1.itsp1.com、Trunk group=1、Realm=sip.itsp1.fr、账号 pbx<N>/alcatel（实验口径）、DNS type=A+DNS1=192.168.1.250、Auth=None、Gateway type=Standard、编解码开关（G711/G729/G722 默认、OPUS 默认 NO）。
    4. 基础 ARS：前缀 0=ARS Prof. Trk Grp Seizure+逻辑鉴别符 0；Numbering Command Table 1（Command I+外部网关 1）；ARS Route list 1（National）→ Route 1（ITSP1 G1：TG1、去 1 位、加 33、命令表 1、Quality=Speech）→ Time-based Route List 1（Route 1、成本上限 -1）；真实鉴别符 0-public → 规则 0（Area1、ARS1、位数 10）；实体鉴别符选择器：逻辑 0→真实 0（真实鉴别符必须已存在，Warning）。
    5. 首测：拨 021PN12345 → 通但显示不友好（P-Asserted=31000）；来话 021PN41000 失败（484 Address Incomplete，无 DID 翻译）。
    6. DID/NPD：默认 DID 翻译器（首外号 3321PN41000 ↔ 首内号 31000、范围 500、Unique Internal Number=NO）→ NPD 33（双 ISDN International、默认号源 NPD=3321PN41000、被/主叫 DID=0）→ TG1 的 Public/Private NPD ID=33、Management Mode=Normal → 出入话复测。
    7. 回叫：默认回叫翻译器加规则 A33（去 3 位加 00）→ 未接显示 021…且回叫可用；国际规则 A（去 1 加 000）；紧急规则 A15/A17/A18（去 1 加 0）、A112（模拟器口径，Warning：按实际运营商调整）。
    8. 国际：ARS 表 2（International：Route1 TG1、去 2 位、不加位、命令表 1）+ 鉴别符规则 00（ARS2、位数 255）；紧急：ARS 表 3（Emergency：去 0 位、不加位）+ 规则 15/17/18（位数 2）、112（位数 3）。
    9. 巡检：sipextgw -l（注册列表）/-g 1（网关参数全景）/-s 1（引用的命令表）；trkstat 1（62 通道状态）/ -r 动态；故障时 dhs3_init -R SIPMOTOR 重启；ps -edf | grep sipmotor。
  verification: |
    sipextgw -l 显示网关 1 IN SERVICE；外显 3321PN41000、来话落 31000；国际/紧急号可拨且显示经回叫规则修饰。
  conditions: 全程按运营商参数定制（TC2005）；模拟器行为≠生产（多处 Warning）；pbxP/alcatel 为实验口径。
  tags: [lab, sip-trunk, ars, npd, did, callback]

- id: c24
  title: SIP 网关双机备份（ARS 第二路由）与负载均衡（SIP Pool）
  type: lab
  source_pages: p641-656
  source_chapter: SIP Carrier access backup (How-To)
  source_quote: |
    "SIP External Gateway ID 2 … Gateway Name … ITSP1_GW2 … SIP Outbound Proxy … gateway2.itsp1.com" (p643-644)；
    "Modify the FQDN of your gateway 1 with something wrong: Example: gateway1.itsp1.bad" (p648)；
    "THE SUPERVISION TIMER IS IMPORTANT TO MONITOR THE GATEWAY, TO SWITCH ON THE OTHER ONE, IF THIS ONE IS OUT OF ORDER." (p651)
  steps: |
    1. 建网关 2：SIP/SIP Ext Gateway → Create：ID=2、ITSP1_GW2、同域/账号、Outbound Proxy=gateway2.itsp1.com、Trunk group=1。
    2. 案 1（ARS 备份）：Numbering Command Table 2（Command I+网关 2）→ 三张 ARS 表（1 国内/2 国际/3 紧急）各加 Route 2（TG1、与 Route1 相同去加位、命令表 2）→ 各 Time-based Route List 1 追加 Route 2 为第二顺位 → sipextgw -l 核对 1/2 双 IN SERVICE（可 dhs3_init -R SIPMOTOR 加速注册）。
    3. 备份测试（个人测）：把网关 1 Outbound Proxy 改成 gateway1.itsp1.bad → sipextgw -l 显示 1 OOS/2 IN SERVICE → 拨外线 → traced 验证走网关 2 → 改回正确 FQDN！（Warning）；通用测：讲师断网关 1 后全班复测。
    4. 案 2（Pool 负载均衡）：删三张时间表中的 Route 2 → 两网关 Pool Number=1 + Supervision timer=5 → sippool 显示池（L=上次使用、OOS）→ 连续外呼观察轮流使用 → 故障注入复测互备。
  verification: |
    网关 1 注错后业务经网关 2 不中断；sippool 显示 L 标记在两网关间切换；测试后配置复原。
  conditions: 两案可并存；Pool 仅限同运营商网关对。
  tags: [lab, sip-gateway, backup, load-balancing]

- id: c25
  title: 外呼闭锁配置（核对四要素→分区→Public COS→换 COS/换 Entity 验证）
  type: lab
  source_pages: p669-681
  source_chapter: Barring (How-To)
  source_quote: |
    "Users … Entity Number … 1 … Rights tab … Public Network COS … 2 (it is the default one)" (p671)；
    "Call Number 00 … Area Number 2" (p675)；
    "BY DEFAULT, AN ENTITY IS IN THE STATE NIGHT." (p674)
  steps: |
    1. 核对：用户（Entity=1、Public Network COS=2）；ARS 前缀 0 的逻辑鉴别符=0；实体 1 鉴别符选择器（逻辑 0→真实 0）；真实鉴别符 0-public 中 0 与 00 均在 Area 1。
    2. 基线测试：紧急/国内/移动/国际全拨一遍（Public COS 2 默认仅 Area 1 全状态放行——而 0/00 都在 Area1，故全通）。
    3. 禁国际：鉴别符 0-public 中 00 → Area 2 → 拨 0044… 被拒。
    4. 禁移动：0-public 建 06/07 → Area 3（ARS1、位数 10）→ 拨 06/07 被拒（国内/紧急不受影响）。
    5. 放开：Access COS 2 → Public Access COS Area 2/3 → Night/Day/Mode1/Mode2 全 1（提醒：实体默认 Night 态，只开 Day 无效）→ 复测全通。
    6. 换 COS 验证：用户 Public Network COS 改 3（默认仅 Area1）→ 复测锁定面变化 → 改回 2。
    7. 换 Entity 验证：用户 Entity 改 0 → 实体 0 选择器把逻辑 0→真实 1 → 复测行为变化（Warning：真实鉴别符未创建不能关联）→ 恢复 Entity 1。
  verification: |
    Area 移动/COS 放行/实体切换三种操作均即时改变外呼能力；紧急号码始终可拨。
  conditions: 实体默认 Night 态是高频坑；测试号码为 ITSP1 实验号段。
  tags: [lab, barring, public-cos, area, entity]

- id: c26
  title: 紧急呼叫配置（紧急区域/Location ID/P-ANI/紧急组）
  type: lab
  source_pages: p689-699
  source_chapter: Area for numbers dedicated to emergency calls and associated services (How-To)
  source_quote: |
    "Update the 'public' real discriminator to assign the area '64' to all emergency numbers: 112, 15, 17 and 18" (p690)；
    "THE USE OF DIRECT IP LINKS BY THE SYSTEM IS A MANDATORY PREREQUISITE FOR SENDING LOCATION ID." (p693)；
    "P_ANI Header … Emergency calls only (our case here)" (p695)
  steps: |
    1. 紧急区域：鉴别符 0-public 中 112/15/17/18 → Area 64（位数 3/2/2/2）；Access COS → Public Access COS Area 64 四状态全 1；System/Other System Param./System Parameters → Emergency numbers area=64（0=关闭）。
    2. 基线抓包：motortrace 3 + traced → 呼 112 → INVITE 无 P-Access-Network-Info。
    3. 前提：System/Other System Param./Network Parameters/Direct IP Link=Enabled（Warning 强制）。
    4. NPD：核对紧急呼叫所用 NPD（ARS 未指定时用 TG 的 Public NPD ID=33）→ Translator/External Numbering Plan/NPD → Location ID Source=Entity。
    5. 位置值：Entities → 实体 1 → Location ID="ALE building B floor 0"（也可直接填 NPD 或 IP 域）。
    6. 发送开关：SIP/SIP Ext Gateway → 网关 1 → P_ANI Header=Emergency only（可 All/None）。
    7. 复测：呼 112 → INVITE 出现 P-Access-Network-Info: IEEE-802.3;eth-location="ALE building B floor 0"；呼普通号码该头缺席。
    8. 紧急组：Applications/Emergency group → 成员 DN=31001（或物理机 31011）→ 从 31000 呼 112 → 31001 收 Tone34+弹窗 → 验证 Snooze（20 秒）/Callback/Clear/EMG log。
    9. 巡检：looknpd n 33（Location ID Source: ENTITY SOURCE）；sipextgw -g 1（P_ANI Header: Emergency only）；entitystat 1（Location ID 字段）。
  verification: |
    紧呼 INVITE 携带 P-ANI 位置；紧急组设备收到通知且四种动作可用；普通呼叫不携带 P-ANI。
  conditions: ARS 必须启用；仅 stand-alone 单节点支持通知；组 ≤10 台商务设备。
  tags: [lab, emergency, p-ani, location-id]

- id: c27
  title: 呼叫分配计时器验证与调优（Entity call 内/外线/等待指南/溢出计时器）
  type: lab
  source_pages: p709-719
  source_chapter: Call Distribution (How-To)
  source_quote: |
    "1st routing: A0000 (Attendant group) • 2nd routing: 310x1 … Overflow routing number: 31000 (mono-line set)" (p710)；
    "Timer N° 76 … Timer units 800 (default value); managed by step of 100 mS … Timer N° 144 … 150" (p711)；
    "Overflow Timer 100 (e.g.); configured by step of 100 mS … '0' by default" (p715)
  steps: |
    1. 前提：实体 1 前缀 31100（DDI）、经理组 A0000、状态小时表全 "Attendant Group"、B0000 在服（Day）；实体 1 CDT：Day 1st=A0000、2nd=310x1、溢出=31000。
    2. 内线测试：310x2 拨 31100 → A0000 振 76（80 秒）→ 310x1 振 144（15 秒）→ 落 31000；调 Timer：System/Timers → 76=800 / 144=150（可改）；提醒话务台未接会转 Absent，需在控制台恢复 Available。
    3. 外线测试：拨 DDI 0021PN41100 → A0000 振 76 → 用户段走 trunk COS 溢出计时器（默认 300=30 秒）→ 31000；查 TG 的 Trunk COS（例 31）：External Services/Trunk COS → Overflow on No Answer/Waiting=300。
    4. 话务等待指南：实体 1 → Attendant waiting guide=110；System/Timers → 102=1（≠0 才播）；换非 110 指南需 System 参数 Entity Call Guide No Answer=True → 外呼 31100 听 110 至摘机。
    5. 实体溢出计时器：Entities → 实体 1 → Overflow Timer=100（10 秒）→ 外呼复测：A0000 段缩短为 10 秒（仅触发一次且仅话务台路由）。
    6. 用户溢出：Access COS 2 → DID Overflow on free set/waiting/Total busy=1 → 外拨 0021PN410x0 不接 → 30 秒后溢出到被叫实体 CDT 的 A0000。
    7. OOS 用户：关掉 IPDSP 31000 → 外拨其 DDI → 立即溢出实体 CDT → 重开 IPDSP。
    8. 未知 DDI：实体 0 CDT（1st Day/Night=B0000、溢出=31000）→ TG1 的 VG for non-existent No.=NO → 外拨未配置 DDI 0021PN41123 → 直落 B0000。
  verification: |
    内/外线溢出时序与计时器值一致；等待指南与实体溢出计时器按配置生效；OOS/未知 DDI 溢出即时。
  conditions: 计时器单位 100ms；测试后恢复默认值。
  tags: [lab, timers, call-distribution, entity]

- id: c28
  title: 数据库备份与恢复（含 secure/Cloud 剥离选项）
  type: lab
  source_pages: p728-736
  source_chapter: Database Backup & Restore (How-To)
  source_quote: |
    "4 Backup & restore operations … 1 Immediate backup operations … 1 Immediate backup on CPU disk … 1 Backup mao, voice guides and accounting data" (p729)；
    "AS THE TELEPHONE APPLICATION IS ALREADY STOPPED, IT IS NOT POSSIBLE TO USE CS MAIN IP ADDRESS TO TRANSFER THE BACKUP FILE. CS PHYSICAL IP ADDRESS MUST BE USED FOR SFTP SESSION." (p733)
  steps: |
    1. 备份：swinst → 2 Expert → 4 Backup & restore operations → 1 Immediate backup operations → 1 Immediate backup on CPU disk → 1 Backup mao, voice guides and accounting data → q 退出。
    2. 传 PC：FileZilla（Binary、mtcl@CS:22）→ /usr4/BACKUP/IMMED → 拖到 C:\Backup\（自动备份在 /usr4/BACKUP/DAY）。
    3. 清理：Expert → 4 → 3 Restore operations → 5 Clean IMMEDIATE backups → 1 Clean mao…；再删几个用户制造差异。
    4. 恢复：Easy 7 停话务（系统重启等登录提示）→（备份已不在机内时）FileZilla 用 CS 物理地址 192.168.1.1（Warning：话务停了 Role 地址不可用）回传 IMMED → Expert → 4 → 3 → 1 Restore from CPU disk → 1 Restore from IMMEDIATE backup → 1 Restore mao, voice guides and accounting data → y → secure restoration y（先存当前库为回退档案）→ restore Cloud and Rainbow services（y/n：实验室选 n 剥离云凭据）→ 完成后 clean up the archive y → Easy 8 起话务 → 等 "No problem with compatibilities"。
    5. 核对被删用户已回来。
  verification: |
    IMMED 目录生成备份并成功传回 PC；恢复后删除的用户恢复；档案清理完成。
  conditions: 传输 Binary；话务停止期间只能用物理地址 SFTP。
  tags: [lab, backup, restore, swinst]

- id: c29
  title: XL 机架上架（GDXL/FXS32/机位规划/模拟用户）
  type: lab
  source_pages: p757-772
  source_chapter: XL rack & boards (How-To)
  source_quote: |
    "Shelf address: must be a free odd position followed be another free one. Example here: 9 and 10 are available, then we specify '9' … Shelf Type Media Gateway XL" (p758)；
    "IN THE 2 XL RACKS, IF GAXL BOARD(S) IS/ARE USED, IT MUST BE AT THE POSTIONS 1 OR/AND 2." (p766)；
    "IF YOU USE THIS COMMAND ON A GDXL BOARD, ALL BOARDS OF THE SHELF WILL BE RESTARTED!" (p772)
  steps: |
    1. 建 XL 架：WBM Shelf → Create：Shelf address=9（奇数、9/10 连续空闲）、Type=Media Gateway XL、Name、PARI=No（XL 无 DECT 板）、Role=Main、Main Shelf Address=-1、Law 默认 → 偶半架自动生成。
    2. GDXL 压缩器：Shelf/9/Board/GDXL → Daughterboard=None/ARMADA、压缩器 15（示例声明；上限 30+30，许可 #135）→ 已在服则 rstcpl 9 0。
    3. GDXL 板侧：V24（root 默认 mgxl.ale/admin letacla1，改密）→ mgconfig：IPv4=192.168.1.109/掩码/网关 192.168.1.254/CS role=192.168.1.3 → Crystal number 手动 9 → 保存重启；或 DHCP 动态（Static IP Address 绑 MAC+TFTP、必要时配置文件 MGXL:-/downbin/mgxl/binmgxlstart；动态时必须勾 Ethernet Address checked by TFTP+登记 MAC）。
    4. FXS32：Shelf/9/Board → Create：Board address=3（规划口诀：前 4 块放 3-6 槽预留 1/2 槽给 GA-XL）、Interface Type=FSX32、Country 默认、Apply Bell Standard Cable Mapping 按现场线对 → config 9 核对 IN SERVICE。
    5. 模拟用户：Users → Create：31041/31042/31043、Set type=ANALOG、Shelf=9、Board=3、Equipment=0/1/2。
    6. 巡检：listerm 9 3（AUTPOS 用户+T_RESU 空口）；cnx neqt 9 3（口状态 Tone）；config 9 0 -d；cplstat 9 0（含虚 GPA 语音指南信息）；rstcpl 9 3（INIT1→INIT2→IN SERVICE；Warning：GDXL 上执行=全架重启）。
  verification: |
    FXS32 IN SERVICE 且三个模拟用户在线；GDXL 与 CS 信令链建立（INTIP3A 对端 19/1）。
  conditions: -48Vdc 供电工艺在书外；GDXL 固件版本书中为占位。
  tags: [lab, xl, gdxl, fxs32, analog]

- id: c30
  title: T0 中继组开通（板/TG/Access/同步/前缀/巡检）
  type: lab
  source_pages: p781-788
  source_chapter: T0 trunk group (How-To)
  source_quote: |
    "Trunk Group ID: 10 … Trunk group type Select T0 … Q931 signal variant … ISDN France" (p783)；
    "IN ORDER TO WORK PROPERLY, THE BOARD WHERE THE TRUNK GROUP IS DECLARED HAS TO BE RESETED" (p785)；
    "Number Prefix Number (ex. #010) … Prefix Meaning Professional Trunk Seize" (p786)
  steps: |
    1. 核板：OV8770/WBM Shelf/Board → MG-BRA4 在服（每口 2B+D；T0 亦可用 MIX 板）。
    2. 节点号：System → 核对本系统节点号。
    3. 建 TG：Trunk groups → Create：ID=10、Name=T0、Type=T0、Node=本机号（Warning：必须本系统 ID）、Tone on seizure 勾选、Q931 variant=ISDN France（教室口径；现场按运营商 VN→France/ETSI→all countries）、Number compatible with=-1 起步、Number Of Digits To Send=10、DDI transcoding=True。
    4. 本地参数：TG/10 → Entity Number、Nb. of digits unused 按运营商（VN 4 位/ETSI 9 位；t3 核对）、B Channel Choice=NO。
    5. Access：TG/10/T2/T1/T0 Access → Create：Physical Address=12-4-0（架-板-口）、Type=T0、时隙自动 → Warning：必须 rstcpl 12 4 重置所在板。
    6. 同步：Shelf/Board/Digital access → Synchro priority=205（T0）、Network mode 客户侧 no/运营商侧 yes。
    7. 前缀：确认无 # 开头前缀冲突 → Translator/Prefix Plan → #010=Professional Trunk Seize（或 With overlap）、info=TG 10、Private route type 不勾 → 出入话测试（教室 ISDN 模拟器）。
    8. 巡检：rstcpl 12 4 → config 12（Running→In service）；trkstat 10（F/B/hs）/-r 动态；trkvisu all（TG 清单与前缀）；t3（ISDN 呼叫追踪：CALLING/CALLED NUMBER，CTRL C 停）。
  verification: |
    trkstat 10 显示 2 个 B 通道 F 状态；#010 抓取可出局；t3 可见主被叫号码。
  conditions: ISDN France 与 10 位为教室实验口径；BRA 板每口 2B+D。
  tags: [lab, t0, trunk-group, isdn]

- id: c31
  title: T2 中继组开通（与 T0 同构、30 通道）
  type: lab
  source_pages: p789-796
  source_chapter: T2 trunk group (How-To)
  source_quote: |
    "Trunk Group ID: 12 … Trunk Group Type Trunk Group Type (ex. T2)" (p791)；
    "Synchro priority 200 for T2 … Network mode set to 'no' on customer side and 'yes' on carrier side" (p794)；
    "NOS Alarm: No Signal on the line" (p796)
  steps: |
    1. 核板：Shelf/board → MG-PRA E1（PRA 板）Operational state=Enabled。
    2. 建 TG：ID=12、Name=T2、Type=T2、Node=本机号、Tone on seizure 勾选、Q931 variant=ISDN France（教室口径）、Number compatible with=-1、发送位数 10、DDI transcoding=True。
    3. 本地参数：Entity、Nb. of digits unused、B Channel Choice=NO。
    4. Access：TG/12/T2/T1/T0 Access → Create：Physical Address=12-2-0、Type=T2 → rstcpl 12 2 重置板。
    5. 同步：Synchro priority=200（T2/T1 优先同步源）、Network mode 客户侧 no/运营商 yes。
    6. 前缀：#012=Professional Trunk Seize、info=TG 12 → 出入话测试。
    7. 巡检：trkstat 12（30 通道 F/B）、trkvisu all、t3、NOS LED（T2 线路无信号告警灯）。
  verification: |
    trkstat 12 显示 30 通道；#012 出局可用；同步优先级 200 生效。
  conditions: 教室信令与位数为实验口径；PRA 板提供 T1 或 T2。
  tags: [lab, t2, trunk-group, isdn]

- id: c32
  title: 维护工具箱实操（oxetrace/ippstat/incvisu/incinfo/syslog/securitystatustool/infocollect/tcpdump）
  type: howto
  source_pages: p737-756
  source_chapter: MAINTENANCE（讲义含命令示例，非独立 How-To 章；此条为命令操作序列汇总）
  source_quote: |
    "OXE TRACE TOOL MAIN MENU 1. Start Trace 2. Stop Trace 3. Decode Trace in Binary Mode" (p740)；
    "Enter the Relevant Question Indexes Separated by Space -> 1 4 6 7 … Enter the folder name (will be created in /tmpd/) ?" (p741)；
    "tcpdump host 192.168.1.3 => Address Filtering … tcpdump –w /tmpd/mytrace.cap –s 0 => Trace backup file" (p755)
  steps: |
    1. oxetrace（mtcl）：选 1 Start Trace → 按问卷输场景序号（空格分隔，如 "1 4 6 7"）→ 输 /tmpd 下目录名 → 复现问题 → 选 2 Stop Trace（自动解码并打包 /tmpd/<名>_<时间>.zip；四子目录 Call_Handling_Traces/-Decoded、SipMotor_Traces、Tcpdump_Captures）→ 选 3 可补解码二进制 → FileZilla 取回分析。注意：启动会复位既有 mtracer/traced/tcpdump；磁盘<4GB 自动减轮转。
    2. ippstat（mtcl）：菜单 1-22（常用 3=全部 IP 话机、8=MAC 清单、15=telnet/ssh 超时、20=加密参数、21/22=OMS/OST SSH 开关；-noname 供 GDPR）。
    3. 事件：incvisu（-t n 最近 n 条）；incinfo GEA <事件号>（2042/2491 等权威释义）；syslog 外发：netadmin 11/8 配置服务器（UDP 514）+ MAO Applications/Incident Manager/Incident Filter 按事件号启用；本地 /var/log/messages。
    4. securitystatustool：XML 全景（版本/SSH/证书/NTP/syslog/密码策略/SIP TLS/默认密码占比/4645 策略；需话务运行）。
    5. infocollect（root）：Classic 模式跑完自动打包 /tmpd/infocollect_<cpu>_<版本>_<时间>.tbz → Binary 传 PC 交支持（选项 -netwnodes i/-pcs 扩展采集）。
    6. tcpdump（root）：host/port/组合过滤；-w /tmpd/mytrace.cap -s 0 存 pcap（Wireshark 可读）。
  verification: |
    oxetrace 停止后生成 zip 且含解码文本；incinfo 能输出事件释义；infocollect 生成 .tbz。
  conditions: 账户要求：oxetrace/ippstat=mtcl、tcpdump/infocollect=root；traces 共需 3GB。
  tags: [howto, maintenance, oxetrace, tcpdump, incidents]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 29 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 登录与账户密码治理 | 有 → c01 |
| task-02 系统启停与 autostart | 有 → c02 |
| task-03 CS IP 双地址 | 有 → c03 |
| task-04 内部防火墙与可信主机 | 有 → c04 |
| task-05 NTP/chrony | 有 → c05 |
| task-06 空数据库创建 | 有 → c06 |
| task-07 OPS 恢复/备份与 FlexLM | 有 → c07 |
| task-08 GD4 上架 | 有 → c08 |
| task-09 OMS 上架 | 有 → c09 |
| task-10 XL 上架 | 有 → c29 |
| task-11 IP 话机开通（静态/动态） | 有 → c12（静态）、c14（动态/DHCP） |
| task-12 IPDSP 部署 | 有 → c10 |
| task-13 User Profile 批量建户 | 有 → c11 |
| task-14 数字/模拟用户 | 有 → c13 |
| task-15 内部 DHCP 服务器 | 有 → c14 |
| task-16 编号计划 | 有 → c15 |
| task-17 两级 COS | 有 → c16（Phone Features）、c17（Connection/Transfer） |
| task-18 语音指南与 MOH | 有 → c18 |
| task-19 话务台组与 4059EE | 有 → c19 |
| task-20 Entity 与 CDT | 有 → c20 |
| task-21 4645 与邮件通知 | 有 → c21（4645）、c22（邮件通知） |
| task-22 公共 SIP 中继 | 有 → c23（全链路）、c24（备份/负载均衡） |
| task-23 外呼闭锁 | 有 → c25 |
| task-24 紧急呼叫通知 | 有 → c26 |
| task-25 呼叫分配计时器 | 有 → c27 |
| task-26 备份恢复 | 有 → c28 |
| task-27 维护工具箱 | 有 → c32（讲义命令序列汇总，非独立实验章，已注明） |
| task-28 T0/T2 中继组 | 有 → c30（T0）、c31（T2） |
| task-29 UMC 云管理 | 无实验。p797-814 为纯讲义（UMC R1.1），书内无 UMC 操作章；结构归 framework f28、数值归 principle p37。 |

**统计**：32 条（lab 31 条 + howto 1 条）；29 项任务中 28 项有案例类覆盖，仅 task-29（UMC）无实验内容（原书即为讲义章，已注明去向）。
