# 案例/实验/操作序列候选 — OmniPCX Enterprise Loading (ENTPXTE402EN Ed12)

> 提取器: case-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 注: 实验环境给定值（IP、密码、账号）标注"实验口径"。
> 条目说明: 全书 17 个 How-To 实验章 → 17 条，编号与原书 How-To 顺序一致。

```yaml
- id: c01
  title: SOT VM 部署（Standalone 模式）与初始化（IP/键盘/账户/网络）
  type: lab
  source_pages: p37-48
  source_chapter: SOT VM deployment in Stand-alone mode — "Deploy the SOT VM in stand-alone mode"
  source_quote: |
    "Unzip the SOT iso file on your PC: Right-click on the SOT_X.X.XXX.XXX.iso Select 7-Zip > Extract"
    (p39)；
    "Enter the new IP settings, and validate your management by pressing the “Y” key ... IP address:
    192.168.1.130 Host Network Fqdn: sot.company.com ... DNS: 192.168.1.250" (p43)；
    "By default: • Login: admin • Password: letacla Modification of the password and creation of the
    passphrase is mandatory during the 1st connection" (p44)
  steps: |
    1. 软件源准备：拷贝 SOT 归档到本地 PC；安装 7-zip（7-zip.org，Run as administrator）；右键 SOT_X.X.XXX.XXX.iso → 7-Zip → Extract 解包（含基础 SOT VM 与 SOT update）；双击 iso 挂载为 DVD（实验口径：iso 在 NAS N:\Softs）。
    2. 导入 VM：VirtualBox → File → Import Appliance → 选 S.O.T. ova → Settings；默认 Guest OS 为 32-bits，宿主为 64 位时改为 64 bits → Finish（版本兼容查 S.O.T. 手册/TC2456）。
    3. 首次配置：启动 VM，控制台按 1 改键盘（默认 en_US）；选 "1) static" 配 IP——IP 192.168.1.130、FQDN sot.company.com、掩码 255.255.255.0、网关 192.168.1.254、DNS 192.168.1.250（无 DNS 可回车跳过；实验口径）→ 按 Y 确认，VM 自动重启；后续改配置用控制台命令 setIp / setKb。
    4. 首连 Web：浏览器开 https://192.168.1.130 → admin/letacla 登录（实验口径）→ 强制设置新复杂密码（≥8 字符，含大写/小写/特殊字符/字母数字各 1；实验口径 Superuser1234*）+ 选择口令短语问题与答案（用于忘记密码自助重置）。
    5. 账户管理（可选）：Settings/Account settings 修改密码与口令短语。
    6. 网络设置（可选）：Settings/Network settings 配置 IP/掩码/网关并 Save；最多 4 个子网；虚机网卡数必须与声明 IP 数一致；加网卡需关机加卡并重启 SOT。
  verification: |
    书中验收点：Web 界面可登录且密码/口令短语设置完成；网络设置保存生效（p46）。
  conditions: 宿主 PC 已装 VirtualBox 或 VMware Workstation Player；SOT 与目标机同网段。
  tags: [lab, sot, deployment, standalone, virtualbox]

- id: c02
  title: 用 SOT 完成 CS3 单版本全加载（Easy 项目 + 网络引导 + 加载后初始化）
  type: lab
  source_pages: p83-92
  source_chapter: Call Server loading with SOT – Mono Version — "Load a full release on a CS3, CPU8"
  source_quote: |
    "Create a project using “Easy mode” ... CS name: CSa • IP address: 192.168.1.101 • MAC address:
    consult the Excel file present on the NAS (Softs)" (p84)；
    "Command grubboot ETHER ... Do you want to continue (y/n, default y): y" (p89)；
    "Define “Superuser2580*” for all account passwords Do not activate the aging password control:
    value “0”" (p91)
  steps: |
    1. 软件源准备：OXE 版本 .iso 拷到本地 PC（实验口径：NAS N:\Softs）。
    2. 登录 SOT Web（https://192.168.1.130；admin / 部署时口令，实验口径 Superuser2580*）；Easy 模式（左侧圆圈图标）→ 新建项目 "from scratch"。
    3. 项目类型选 Greenfield（全新安装）→ Next；Product Selection 选 OXE；媒体存储位置选 Local storage（出现 "OXE media is missing" 说明需传文件）。
    4. 传输媒体：FTP 或 SFTP（端口 2222）登录 upload/sot（实验口径），用 Filezilla 上传 OXE 版本 .iso（可同时传 OPS 许可文件）→ 回 SOT 点 Refresh medias list → 勾选 iso → Declare medias。
    5. 选择软件版本：选不带补丁的版本（本实验后续另装补丁）；可选在 Storage area 上传许可文件；Next。
    6. 项目设置：Project name/Description；OVF generation 不勾（目标是 CS3 板卡）；Country=France、Timezone=Europe/Paris（示例）。
    7. 目标机设置：OXE Hardware Type=CS-3；keyboard=fr；OXE country=France；CPU hostname=CSa；CPU IP=192.168.1.101；CPU MAC（NAS 的 Excel 文件查本 POD 值，或 mtcl 登录终端 ifconfig）；CPU redundancy 按需 → Verify → Deploy（SOT 进入等待目标机状态）。
    8. 目标机网络引导（二选一）：(a) root 登录执行 grubboot ETHER → 确认 y（提示 Disk have to be reinstalled after reboot，系统自动重启）；(b) CS3/CPU8 启动初期按 CTRL+B 进 BIOS → Save & Exit 页选 Ethernet 接口。
    9. 观察加载：SOT Web 进度条；OXE 终端可见加载过程；完成后项目状态 "completed"。
    10. 加载后初始化：OXE 重启后选键盘类型（可先测试）；为 root/mtcl/adfexc/swinst 逐个设密码（实验口径 Superuser2580*；规则见 principle p01）与 aging（实验口径 0，注意 CIS 警告）→ 确认修改。
  verification: |
    SOT Web 项目状态 "completed"（p90）；OXE 控制台出现登录提示 "CSa login:"（p92）；
    可用 siteid 命令核对软件版本（p92 Notes）。
  conditions: 目标机与 SOT 同网段；空盘自动 Standard Installation，已装系统需 grubboot/BIOS 强制网络引导。
  tags: [lab, sot, mono-version, cs3, grubboot]

- id: c03
  title: 多版本加载：装 inactive 分区并（可选）自动切换
  type: lab
  source_pages: p93-99
  source_chapter: Call server loading on inactive partition with SOT – Multi versions — "Load a full version on inactive partition"
  source_quote: |
    "Select “Media/Declare media” ... Check “Internal SOT local storage”" (p94-95)；
    "Update on inactive partition Checked, to install version/patch on inactive partition" (p96)；
    "In “swinst” menu 2 - Expert menu • 8 - Software Identity display • 2 - Application software
    identity ... Press 0 for the active version, 1 for the inactive one" (p98)
  steps: |
    1. 声明媒体：SOT Expert 模式（右侧圆圈图标）→ Media/Declare media → 勾 Internal SOT local storage → 经 FTP/SFTP(2222) upload/sot 上传新版本 .iso → Refresh media list → 勾选 → Declare media → Media/Media listing 确认版本入列。
    2. 更新既有项目：Projects/Projects listing → 选中项目 → update 按钮 → 选要装的版本并补全字段 → Update selected product（"checking" 按钮可先校验项目与目标机版本/密码的一致性）。
    3. 关键字段：Update on inactive partition=勾；Enable Autostart=Yes/No/Unchanged（仅当勾选 Switch partition 后可配；YES=切换后电话应用自启）；Use a clean inactive partition=按需勾（装前清空第二分区）；Duplicate OXE Data=勾（自动复制 OXE 数据库到 inactive）；Duplicate Linux data=勾（自动复制 IP 配置、host 文件等）；Switch partition after update installation=勾（装完自动切换）；Switch time=排定切换时刻（减少业务影响）；Switch back=按天定义回切周期；Update Standalone=勾；OXE license=按需；mtcl/swinst/root 密码逐项填 → OK。
    4. 部署：SOT 显示进度；若启用切换，加载结束 OXE 重启并切到新分区 → 项目 "completed"。
    5. swinst 收尾：swinst 登录输入国家码；核验 autostart；未启用 autostart 时 mtcl 用 RUNTEL 手动起电话应用。
    [附录：手工操作]
    6. 查两分区版本：swinst → 2 Expert menu → 8 Software Identity display → 2 Application software identity → 按 0 查 active / 1 查 inactive。
    7. 手工复制 Linux 数据：swinst → 2 → 3 Cloning & duplicate operations → 2 Partitions duplication → 2 Duplicate Linux Data → 确认 y。
    8. 手工复制数据库：同菜单 → 4 Duplicate database → 确认 y（迁移场景会提示翻译数据库，答 YES）。
    9. 手工切换：swinst → 2 → 3 → 3 Switch on inactive version → 确认 y → 保留 autostart 选 y → "switch back if system resets" 选 n → Do a version switch 确认 y（系统自动重启；首次进 swinst 需输国家码）。
  verification: |
    swinst 8-2 显示 inactive 分区为目标版本（p98）；切换后 siteid/swinst 显示新版本生效；
    项目状态 "completed"（p97）。
  conditions: 前提 OXE 项目已存在（active 已用同一 SOT 装过）；两版本均须 ≥N3（跨 N3 见迁移规则）。
  tags: [lab, multi-version, inactive-partition, swinst, switch]

- id: c04
  title: 补丁安装：active 分区（静态停话音）与 inactive 分区（先 Duplicate all）双场景
  type: lab
  source_pages: p100-110
  source_chapter: Patches installation on active & inactive partitions — "Deploy static and dynamic patches"
  source_quote: |
    "STATIC PATCH INSTALLATION ON ACTIVE PARTITION REQUIRES TO STOP THE TELEPHONE APPLICATION. SO,
    SYSTEM IS REBOOTED AUTOMATICALLY" (p104)；
    "In “swinst” menu 2 - Expert menu • 3 - Cloning & duplicate operations • 2 - Partitions
    duplication • 5 - Duplicate all" (p106)；
    "(E)CSa> siteid ... Linux version : 601.017 ... Patch version : 36" (p109)
  steps: |
    1. 声明补丁媒体：SOT Expert → Media/Declare media → Internal SOT local storage → Filezilla 经 FTP/SFTP(2222) upload/sot 上传补丁（.zip 或 .iso）→ Refresh → Declare media。
    2. 查当前版本：mtcl 登录终端看登录横幅，或 siteid 命令（实验演示：patch 0 / Linux 601.007）。
    3. [场景 A：active 分区] Projects → 项目 → update → 选补丁 → Update on inactive partition 不勾 → Update selected product(s)（静态补丁时 OXE 自动重启停话音；动态补丁不打扰运行）→ completed → siteid 复核（实验演示：静态补丁 19 后 Linux 601.012）。
    4. [场景 B：inactive 分区·先复制] swinst → 2 Expert → 3 Cloning & duplicate operations → 2 Partitions duplication → 5 Duplicate all → 全程确认 y（复制 Linux+包+网络配置）→ mtcl 用 ver2cho visible 与 df -v 核对两分区一致。
    5. [场景 B：装补丁] SOT update 项目 → 选补丁 → Update on inactive partition 勾（静/动无差别、不立即重启）→ Duplicate OXE Data / Duplicate Linux data 均不勾（上一步已复制）→ 按需勾 Switch partition after update installation 并设 Switch time / Switch back → Update Standalone 勾 → 填三账户密码 → OK → completed。
    6. 复核：siteid（实验演示：切到含补丁 36 的分区后 Linux 601.017、Patch version 36）；或 swinst 8-2 按分区查（0 active / 1 inactive）。
    7. [附录：手工切换] swinst → 2 → 3 → 3 Switch on inactive version（同 c03 步骤 9）。
  verification: |
    siteid 显示补丁号按预期推进（0→19→36，实验口径）；项目状态 "completed"（p105/p109）。
  conditions: 动态补丁必须在同版本静态补丁之后；Duplicate all 失败时退回"对 inactive 做完整版本加载"的备用路径（p106 Warning）。
  tags: [lab, patch, static, dynamic, duplicate-all, siteid]

- id: c05
  title: Easy Installation：OXE 作分发器本地加载版本与补丁（/tmpd + swinst 9-10）
  type: lab
  source_pages: p116-130
  source_chapter: Easy installation of OXE — "To load a version or a patch on the OXE Call Server, used as a distributor"
  source_quote: |
    "transfer a version (“.iso” file) to the “tmpd” OXE Call Server directory. Don’t forget to define
    PC host into the OXE IP Tables." (p117)；
    "Your choice [1..10, Q] 10 ... Please enter the name of the ISO/ZIP file in /tmpd directory :
    nYYYY.iso Confirm the local load of nYYYY.iso (y/n, default y): y" (p118)；
    "Select the partition for installation of dyn_nY.YYY.Y.Y 1 for the ACTIVE version (default)
    2 for the INACTIVE version => 2" (p127)
  steps: |
    1. 前置：PC IP（实验口径 192.168.1.9）加入 OXE 信任主机——mtcl 登录 → netadmin -m → 11 Security → 1 Firewall(iptables) Configuration → 3 Restricted Access Configuration → 2 Add a trusted host（名称 pc、IP 192.168.1.9）→ a 应用退出。
    2. 传输：Filezilla 连 OXE，把版本 .iso 传到 /tmpd 目录。
    3. 装版本（inactive）：swinst（swinst 账号）→ 2 Expert menu → 9 Remote download → 10 Local load as distributor of ISO image/ZIP file and installation → 输入文件名 nYYYY.iso → 确认 y（REMOTE LOAD OPERATION 显示 path /usr4/ftp/ISO/dhs3mgr/nYYYY、Client CPU type DISTRI；"THE MODULE fr IS CORRECTLY INSTALLED" 结束）。
    4. 复核：swinst → 8 Software identity display → 2 Application software identity → 按 1 查 inactive 分区为新版本。
    5. 复制数据：swinst → 2 → 3 Cloning & duplicate operations → 2 Partitions duplication → 2 Duplicate Linux data（确认 y，含网络配置复制与时区）→ 返回后 4 Duplicate database（确认 y；询问是否翻译数据库按需 y）。
    6. 切换：swinst → 2 → 3 → 3 Switch on inactive version → y → 保留 autostart y → switch back n → 确认 y（系统重启；提示切换后需以 swinst 重连完成安装）。
    7. 装静态补丁（inactive）：静态补丁 .zip 传 /tmpd → 同菜单 9-10 → 输入 nYYYYY.zip → 确认（path /usr4/ftp/ZIP/nYYYYY；"THE MODULE comm IS CORRECTLY INSTALLED"）→ swinst 8-2 复核 inactive 补丁号。
    8. 装动态补丁（active 或 inactive）：动态补丁 .zip 传 /tmpd → 9-10 → 输入 nYYYYYY.zip → 确认 → 安装器询问目标分区：1 ACTIVE（默认）/2 INACTIVE → 选择后确认安装（"To complete dynamic patch installation" 提示用 downstat d（板卡）/downstat i（IP 话机）/downstat t（40x9 话机）检查需下载对象）。
    9. 维护/清理：解包物落在 /usr4/ftp/Rload/{version,patch,dynpatch}，不会自动删除——swinst → 2 → 9 Remote download → 7 Cleaning operation on master/distributor CPU → 回车选本机 csa → 逐项确认移除 version/patch/dynpatch → Done（该操作只清 Rload 下解包物；/tmpd 源文件在安装结束时已自动删除）。
  verification: |
    swinst 8-2 显示 inactive/active 分区版本与补丁号按步骤推进（p119/p125）；清理后 Rload
    目录为空（p129）；REMOTE LOAD 输出 "OPERATION ENDED CORRECTLY"（p118/p124）。
  conditions: 全版本与静态补丁必须装 inactive 分区；动态补丁可选分区；前提无重新分区需求。
  tags: [lab, distributor, easy-installation, tmpd, downstat]

- id: c06
  title: SOT Template Factory 降级模式启用（低资源机器）
  type: lab
  source_pages: p155-165
  source_chapter: Configuration of the S.O.T. in Template Factory mode on a machine with low resources
  source_quote: |
    "Right-click on the virtual machine and select Shutdown from the Stop menu" (p157)；
    "Navigate to: `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\DeviceGuard\Scenarios\Hypervisor
    EnforcedCodeIntegrity` Double-click on Enabled and set the value to 0" (p161)；
    "In the console, type templateFactory and then the Enter key ... Enter Y to bypass resource
    control" (p163-164)
  steps: |
    1. 前提：已用标准 softwareOrchestrationTool.ova 部署 SOT（同 c01）。
    2. 关机：SOT Web（Settings → Shutdown S.O.T.）或 VirtualBox 右键虚机 → Stop → Shutdown → 确认。
    3. 加第二块盘：Settings → Storage → Controller: SCSI → "Adds hard disk" 图标 → Create → 类型 VDI → 大小 50 GB → Finish → 选中新盘 → Choose → 确认挂到 SCSI 控制器 → OK。
    4. 启用嵌套虚拟化：Settings → System → 勾 "Nested VT-x/AMD-V"；若灰置（被设备安全阻止）：regedit 定位 HKLM\SYSTEM\ControlSet001\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity → Enabled=0 → 确定 → 重启 PC；再在 Settings → System → Acceleration → Paravirtualization Interface 选 KVM → OK。
    5. 启用功能：启动 SOT VM → 控制台输入 templateFactory 回车 → 按 Y 绕过资源检查 → 提示 Template Factory mode is enabled in degraded mode。
    6. 界面核验：浏览器登录 SOT Web（admin / Superuser2580*，实验口径）→ 可见 Template Factory 新功能入口。
  verification: |
    控制台提示 "Template Factory mode is enabled in degraded mode for PC"（p164）；
    Web 界面出现 Template Factory 功能（p165）。
  conditions: 硬件前置不再受控（浏览器首页显示警告）；构建 OVA 时长强依赖机器规格。
  tags: [lab, template-factory, degraded-mode, nested-virtualization]

- id: c07
  title: OXE VM 加载（SUSE KVM 环境）：Template Factory 生成模板 + virsh 定义并启动
  type: lab
  source_pages: p166-176
  source_chapter: OXE VM loading with S.O.T. deployment tool for a SUSE KVM environment
  source_quote: |
    "Select the project type: Template Factory. ... Template Factory Must be validated to create an
    image for Vmware or KVM environment" (p168)；
    "Transfer files to the /var/lib/libvirt/images directory on the host machine ... Type the command:
    virsh define <template_name>.xml" (p171-173)；
    "Enter Superuser2580* as password for all accounts. Do not activate the aging control for
    accounts: enter 0 and confirm Y" (p175)
  steps: |
    1. 软件源准备：OXE iso 拷本地（实验口径 NAS N:\Softs）。
    2. 登录 SOT Web → Easy 模式 → 新建项目；项目类型选 Template Factory（生成 VMware/KVM 镜像必须选它）→ Next。
    3. 产物选 OXE；媒体存储 Local storage（缺媒体则按 c02 步骤 4 传输并 Declare）；选 OXE 软件版本（不带补丁/带静态/带静+动三选一）→ Next。
    4. 项目设置：Project name/Description；OXE sizing 按用户数选模板（500/3000/7000/15000，决定虚机硬盘与内存）；如需 AWS 用 "OXE template for AWS"；→ Deploy 生成模板。
    5. 取模板：Template Factory/Template Listing → 点模板链接下载 .tgz 到本地 → 解压得 "KVM Images" 文件夹。
    6. 传到 KVM 宿主：Filezilla 把模板文件传到 KVM 主机（实验口径 192.168.1.55）/var/lib/libvirt/images。
    7. 创建并启动 VM：经 .jnlp 连 SUSE KVM 宿主（root/superuser，实验口径；GNOME Classic）→ 终端执行 virsh define <template_name>.xml → 打开 Virtual Machine Manager → 选中 OXE 实例启动 → Open 看启动过程。
    8. 加载后初始化：OXE 启动后选键盘语言（US 或按实际）→ 确认键盘（可测试；后续 root 可用 kbdconfig 改）→ 为各账户设密码（实验口径 Superuser2580*）与 aging=0 → 完成加载出现登录提示。
    9. 加载后操作（Notes 清单）：管理 CS IP（实验口径 192.168.1.201）；建数据库；管理 OXE IP tables 信任主机；装许可文件；swinst 输国家码；按需启 autostart；mtcl 启动电话应用；siteid 核版本；配日期时间；板卡上线；建用户或恢复备份。
  verification: |
    Virtual Machine Manager 中 OXE VM 启动并完成加载（出现 CSa login:，p175）；siteid 可查版本。
  conditions: 需要 Template Factory 模式的 SOT（见 c06）；KVM 宿主满足版本前置。
  tags: [lab, kvm, template-factory, virsh, oxe-vm]

- id: c08
  title: OMS VM 加载（SUSE KVM 环境）：VMM 手工建虚机 + SOT OMS 项目 + IPXE 引导加载
  type: lab
  source_pages: p177-188
  source_chapter: OMS loading with S.O.T. deployment tool into Suse KVM environment
  source_quote: |
    "Create a Virtual Machine for an OMS in the Virtual machine Manager with the following settings:
    ­ OMS name: OMS ­ Operating System: Rocky Linux 9.4 ­ Memory size: 1 GB ­ CPUs: 1 ­ Disk size:
    16 GB" (p178)；
    "Select NIC into the Menu Read the MAC address that will be asked for the SOT OMS project
    creation ... Press ESC when the VM boots up Then option 3 for IPXE boot" (p182, p187)；
    "You are now able to configure the OMS settings with “omsconfig” command" (p188)
  steps: |
    1. VMM 建虚机：连 KVM 宿主（.jnlp，root/superuser 实验口径）→ Virtual Machine Manager → File → New Virtual Machine → Manual Install → Forward → OS 搜 "Rocky" 选 Rocky Linux 9 (rocky9) → Forward → 内存 1GB、CPU 1 → Forward → 磁盘 16GB → Forward → 命名 OMS、网络选 Bridge device br0 → Finish。
    2. 读 MAC 与引导设置：Edit → Virtual machine Details → NIC 记下 MAC（SOT 项目要用）；Boot Options 勾 "Enable boot menu"（可顺带勾宿主开机自启）。
    3. SOT 项目：Easy 模式 → Greenfield → Product=OMS → Local storage → 出现 "BootDVD media is missing" → FTP upload/sot 传 BootDVD.iso + OMS 软件 iso → Refresh → 勾两个 iso → Declare medias → 选 BootDVD 版本与 OMS 软件版本 → Next。
    4. 项目设置与目标：Project name/Description；OVF Generation 不勾；Country/Timezone → OMS keyboard、Hostname=oms、MAC=步骤 2 所记、"Add an OMS server"=No、IP=192.168.1.213（实验口径）→ Deploy → SOT 进入等待 VM PXE boot。
    5. IPXE 引导加载：VMM 启动 OMS VM → 启动时按 ESC → 选 3 IPXE boot → 加载进行中（SOT Web 可跟进度）→ 完成显示 deployment result → Close。
    6. 初始化：kb 账号 kb/kb 登录改键盘 → root 登录（默认 letacla1，实验口径）→ 首连强制改密为 Superuser2580* → 用 omsconfig 命令配置 OMS。
    7. 加载后操作（Notes 清单）：管理 OMS IP（192.168.1.213）；装许可（如未装）；在 OXE 数据库声明 OMS；把 OMS 加入 OXE 信任主机；确认 OMS 进入服务。
  verification: |
    SOT Web 显示 deployment result 完成（p187）；omsconfig 可用（p188）；OXE 侧 OMS 进入服务
    （p188 Notes）。
  conditions: 需 BootDVD 与 OMS 两个 iso 媒体；OMS 规格为教材给定（1GB/1CPU/16GB/Rocky 9.4）。
  tags: [lab, oms, kvm, ipxe, vmm]

- id: c09
  title: SOT VM 部署（Hosted 模式，ESXi Web 界面）与 vSphere 厚客户端附录
  type: lab
  source_pages: p189-203
  source_chapter: S.O.T. VM deployment in hosted mode — "Deploy the S.O.T. Virtual Machine in hosted mode"
  source_quote: |
    "User name: root Password: Superuser-X* Where X is your pod number" (p190)；
    "Select the creation type ... “Deploy a virtual machine from OVF or OVA file”" (p191)；
    "IP address: 192.168.1.230 ... Host Network Fqdn: sot.deploy.ale (e.g.) ... DNS: 192.168.1.254" (p193-194)
  steps: |
    1. 准备 SOT ova（同 c01 步骤 1）。
    2. ESXi 导入：浏览器开 ESXi 管理页（IP 或 FQDN）→ root / Superuser-X*（X=POD 号，实验口径）→ Virtual Machines → Create/Register VM → 选 "Deploy a virtual machine from OVF or OVA file" → Next → 命名并选择 ova（或 OVF+vmdk）→ Next → 选存储 → Next → 网络选 Subnet-1（RLAB infra）→ 磁盘类型 Thin Provision → 按需勾 Power on automatically → Next → Finish。
    3. 首次配置：开机（若未自动）→ 打开 VM 控制台 → 按 1 改键盘 → 按 1 静态配 IP：IP 192.168.1.230、FQDN sot.deploy.ale（示例）、掩码 255.255.255.0、网关 192.168.1.254、DNS 192.168.1.254（实验口径）→ Y 确认重启；后续 setIp/setKb。
    4. 首连与账户：https://192.168.1.230 → admin/letacla → 强制改密（≥8 字符四类各一）+ 口令短语（同 c01）；Settings/Account settings 可改密与 FTP 账号。
    5. 网络设置：Settings/Network settings（最多 4 子网；接口数与 IP 数一致警告）。
    6. 更新：Settings/Update S.O.T. 选 zip+MD5 → Launch update → About 查版本。
    [附录：vSphere thick client（仅 ESXi ≤6.0 可用）]
    7. vSphere 客户端 → File → Deploy OVF Template → 选 ova → Next → 改名 → Thin Provision → 网络映射到生产网络 → 按需勾部署后开机 → Finish；VM 控制台同步骤 3 配 IP。
  verification: |
    ESXi 中 SOT VM 运行；https://192.168.1.230 可登录并完成密码/口令短语设置（p195）；
    About 显示更新后版本（p198）。
  conditions: p199 Warning——vSphere thick client 仅支持到 ESXi 6.0；Web 界面流程为主路径。
  tags: [lab, sot, hosted, esxi, vsphere]

- id: c10
  title: OXE VM 生成（.ova）与加载（ESXi）：OVF generation 项目 + ESXi 部署 + 自动加载
  type: lab
  source_pages: p204-211
  source_chapter: OXE VM loading with S.O.T. deployment tool — "Generate an OXE virtual machine (.ova) with S.O.T. / Load an OXE virtual machine with S.O.T."
  source_quote: |
    "OVF generation To be checked only if the target is a virtual machine, whose “.ovf” file will be
    generated by SOT VM. Must be enabled for this lab" (p208)；
    "“Copy to clipboard” button allows the copy of the URL link for later “.ova” file download." (p208)；
    "Start the OXE virtual machine, and check that the loading starts automatically" (p209)
  steps: |
    1. 登录 SOT Web（实验口径 https://192.168.1.230）→ Easy 模式 → Greenfield → Product=OXE → Local storage → FTP upload/sot 传 OXE iso → Refresh → Declare media → 选版本（无补丁/+静态/+静动）→ Next。
    2. 项目设置：OVF generation 勾（目标是 SOT 生成 ovf 的虚机）；Country/Timezone。
    3. 目标设置：OXE sizing 模板（500/3000/7000/15000）；keyboard=fr（示例）；CPU hostname=CSa；CPU MAC 不填（SOT 生成 ovf 时不需要）；CPU redundancy 按需；OXE country=France；CPU IP=192.168.1.201（实验口径）→ Verify → Deploy。
    4. 取 ova：".ova" 生成中 → Download 保存（或 Copy to clipboard 复制 URL 稍后下载）。
    5. ESXi 部署：同 c09 步骤 2 的 OVF/OVA 部署流程部署 OXE VM。
    6. 加载：Power On 启动 OXE VM → 加载自动开始（VM 控制台可见）；SOT Web 显示进度条 → completed 后可关停 SOT VM。
    7. 加载后初始化：OXE 重启后选键盘语言（US 等）→ 确认（后续 kbdconfig 可改）→ 各账户设密码（实验口径 Superuser2580*）与 aging=0 → 完成。
    8. 加载后操作（Notes 清单）：定义 OXE IP tables 信任主机；手工恢复许可（若项目未配）；按需配角色寻址（csm=192.168.1.203，实验口径）；swinst 国家码；autostart；mtcl 启电话应用；siteid 核版本；日期时间；板卡上线；建用户或恢复备份。
  verification: |
    SOT Web 项目 "completed"（p210）；OXE VM 完成加载出现登录提示（p211）。
  conditions: SOT hosted 模式可用（c09）；目标网络与 SOT 连通。
  tags: [lab, esxi, ova, oxe-vm, ovf-generation]

- id: c11
  title: OMS VM 生成（.ova）与加载（ESXi）
  type: lab
  source_pages: p212-218
  source_chapter: OMS generation & loading with S.O.T. deployment tool
  source_quote: |
    "OVF Generation Checked when the target is a virtual machine generated by S.O.T. ... “ovf” file is
    then generated by S.O.T." (p216)；
    "MAC address No MAC address required in case of virtual machine loading ... Add an OMS server
    Checked the box, if more than 1 OMS VM has to be generated and loaded (4 OMS maximum can be
    declared in the project)" (p216)；
    "Check in the Web client that the project is in “OVA generated” status up to now" (p216)
  steps: |
    1. 登录 SOT Web → Easy 模式 → Greenfield → Product=OMS → Local storage → 出现 "BootDVD media is missing" → FTP upload/sot 传 BootDVD.iso + OMS 软件 iso → Refresh → 勾两个 iso → Declare medias → 选 BootDVD 与 OMS 软件版本 → Next。
    2. 项目设置：OVF Generation 勾（SOT 生成 ovf）；Country/Timezone。
    3. 目标设置：OMS keyboard；Hostname=oms；MAC 不填（虚机加载无需 MAC）；"Add an OMS server" 多台时勾选（一个项目最多声明 4 台 OMS）；IP=192.168.1.213（实验口径）→ Deploy → ".ova" 生成中 → Download；Projects/Projects listing 核对项目状态 "OVA generated"。
    4. ESXi 部署：同 c09 的 OVF/OVA 流程部署 OMS VM。
    5. 加载：Power On（或部署时已勾自动开机）→ 加载自动开始 → VM 控制台看进度；SOT Web 进度条 → completed → 之后可停掉 SOT VM。
  verification: |
    项目状态 "OVA generated"（p216）；SOT Web 项目 "completed"（p218）。
  conditions: 需要 BootDVD + OMS 两个媒体；OMS 后续需在 OXE 数据库声明（见 c08 步骤 7）。
  tags: [lab, esxi, oms, ova]

- id: c12
  title: GAS 加载（SOT Easy 项目 + BIOS 取 MAC + PXE 引导）
  type: lab
  source_pages: p244-254
  source_chapter: Generic Appliance Server loading using S.O.T. — "Perform the software loading of a Generic Appliance Server"
  source_quote: |
    "Press the F9 key to access the System Utilities menu ... Select “System information” then
    “Summary”" (p246)；
    "A Firewall_Rules_gas.csv file is available on the NAS for managing trusted hosts." (p250)；
    "Select “Embedded LOM 1 Port 1 : BCM 5720 1GbE 2p BASE-TLOM Adptr (PXE IPv4)” ... The
    installation in the training environment takes around 60 minutes." (p253-254)
  steps: |
    1. 软件源准备：bootdvd_rocky-v.v.v-x86_64.iso + oxe_sws-vv.v.iso 两个 iso 拷本地（实验口径 NAS N:\Softs）。
    2. 取 MAC：经 ILO 接口接管 GAS（"GAS & KVM accesses" 文件夹的 jnlp → 接受风险 → Continue）→ Power Switch → Reset → 按 F9 进 System Utilities → System information → Summary → 下翻记 Port 1 网卡 MAC（不同服务器进菜单的按键可能不同）。
    3. SOT 项目：Easy 模式 → Greenfield → Product=GAS → Local storage → FTP upload/sot 上传 GAS 版本 iso + BootDVD iso + 信任主机 csv（NAS 提供 Firewall_Rules_gas.csv）→ Refresh → 勾选 → Declare media → 下拉选 BootDVD（GAS 的 OS）与 GAS 软件版本 → Next。
    4. 项目设置与目标：OVF generation 不勾（目标是物理机）；Country=France、Timezone=Europe/Paris（示例）→ GAS keyboard=fr、hostname=gas、MAC=步骤 2、Domain=company.com（示例）、IP=192.168.1.45（实验口径）→ Deploy → 等项目 "loaded"。
    5. PXE 引导：重启 GAS（电源键+按 F11 进启动菜单；或 F9 → One-Time Boot Menu）→ 选 "Embedded LOM 1 Port 1 : BCM 5720 1GbE 2p BASE-TLOM Adptr (PXE IPv4)" → 自动开始加载。
    6. 观察与收尾：SOT Web 进度条——先装 OS，装完服务器自动重启，再装 GAS 软件（OXE VM、OMS VM…；培训环境约 60 分钟）→ "completed" → 停 SOT VM → GAS 重启后登录控制台 → 改各账户密码 → 进入后安装向导（见 c13）。
  verification: |
    SOT Web 显示 "completed"（p254）；GAS 出现登录提示可改密并开始后安装（p254）。
  conditions: 需 BootDVD+GAS 两个 iso；MAC 为 Port 1；引导按键随服务器型号而变。
  tags: [lab, gas, pxe, ilo, sot]

- id: c13
  title: GAS 后安装向导（Xming+Putty X11 → oxeswspostinst.bin：国家码/OXE 参数/冗余/可选组件/WebRTC GW/许可）
  type: lab
  source_pages: p255-282
  source_chapter: Post-Installation Wizard
  source_quote: |
    "Execute “./oxeswspostinst.bin”" (p263)；
    "Select "Spatial Redundancy" if the OXE is duplicated, with the 2 OXE Call Servers present in 2
    different IP subnets" (p266)；
    "Turn Server Enter “GEOIP” to use the geolocalization for the TURN server definition ... PBXID:
    Enter the "PBX ID" (here, you can enter the ID given as example)" (p267-268)
  steps: |
    1. 账户改密：SOT 部署完成后 GAS 登录（root/letacla1、admin/letacla1、kb/kb；实验口径）→ 首连强制改 root 密码（实验口径 Superuser2580*）→ passwd admin 同步改 admin。
    2. 装 X Server：PC 装 Xming（默认下一步装完）→ XLaunch（默认显示设置 → Start no client → 默认参数 → Finish，底栏可见运行中）。
    3. SSH X11：Putty → 会话 IP 192.168.1.45（实验口径）→ Connection/SSH/X11 勾 Enable X11 forwarding → 保存 → Open → admin 登录（root 直接登录已不再允许）。
    4. 启动向导：cd /root（SOT 上传的 GAS 软件在此）→ ./oxeswspostinst.bin → 弹出图形向导。
    5. 欢迎页：New installation（全新无备份）→ 选国家码（用于 OXE 建库与时区）→ Next。
    6. OXE 参数（无冗余示例）：CPU Host name=csa、CPU IP=192.168.1.1、掩码 255.255.255.0、网关名 gateway、网关 IP=192.168.1.254、Network number=1、Node number=1、Node name=oxe（实验口径）；Import-Trusted Host 指向 SOT 项目里 csv（默认复制为 /opt/config/trust/import_th.csv；OXE iptables 建好后移至 /tmpd/import_th_bkp.csv）。[冗余变体] Local Redundancy=两 CS 同子网（一个 Main IP）；Spatial Redundancy=两子网（两个 Main IP；另需填 B 机网关名/IP 与 B 机 Main 名/IP；B 机 Main 地址需 DNS 委托解析节点名）。
    7. 可选组件：勾 OMS（IP 192.168.1.13）与 WebRTC。
    8. WebRTC GW 参数：IP 192.168.1.15、掩码、网关 192.168.1.254、hostname=webrtc、domain=company.com、DNS 192.168.1.250、NTP 192.168.1.252、无代理、TURN=GEOIP（或按区域填 TURN FQDN）、RAINBOW_PBXID（示例值；正常应填 Rainbow 云平台为该 OXE 生成的唯一 PBX ID，如 PBXe5b9-…）、PBX_DOMAIN=192.168.1.1（不冗余填物理 IP；本地冗余填 Main IP；空间冗余填节点名并要求 DNS 委托）、RAINBOW_DOMAIN/RAINBOW_HOST=openrainbow.com、Enable SSH 勾。
    9. OXE 许可：Browse 选许可文件 / Skip（事后补：OXE 许可经 FTP/SFTP 传 /usr4/BACKUP/OPS 再 swinst 恢复；.ice 经 SFTP 传 FlexLM /opt/Alcatel-Lucent/data/licenses，凭证 root/letacla1 默认口径）/ Mount USB（U 盘挂到 /media/usb-drive 后 Browse 选 5 个许可文件）。
    10. 汇总执行：Install（进度条；培训环境约 15-20 分钟）→ Done。
    11. 访问 VM 收尾：同一 SSH 会话执行 virt-manager 打开 Virtual Machine Manager → 双击 OXE/OMS/WebRTC 控制台 → OXE 选键盘（us）并设四账户密码（Superuser2580*，aging 0）；OMS 默认 admin 或 root/letacla1；WebRTC 默认 rainbow/Rainbow123——均首连强制改密。
    [附录 5-6：维护命令与 FlexLM]
    12. gasversion / gasversion all 查组件版本；gasbackup 交互备份（或 gasbackup -d <路径>）；uhwconf 确认 "CPU Hosted On: GAS"。
    13. FlexLM：许可 .ice 入 /opt/Alcatel-Lucent/data/licenses（SFTP 传 /tmp 后 root mv）→ systemctl restart flexlmd → status/lmutil lmstat -a 核对；getaluid 查 ALUID；OXE 侧 System/Licenses：FlexLM Licensing Enabled=Yes、Flex Server IP=192.168.1.45、端口 27000、Product ID discovery=Yes → OXE 重启。
  verification: |
    "POST INSTALLATION SUCCESSFULLY INSTALLED TO: /home/OmniPCXEnterpriseSoftwareServer"（p272）；
    三 VM 均可登录并改默认密码（p272）；flexlmd active (running)（p280）；OXE 重启后 spadmin
    可查许可（p282 Warning 要求重启）。
  conditions: 网关 IP 必须安装期可达；直接 root SSH 登录已禁用；本实验为无冗余场景（冗余参数见步骤 6）。
  tags: [lab, gas, post-installation, webrtc-gw, flexlm, x11]

- id: c14
  title: OXE 云连接前提：netadmin 配 DNS/代理 + checkCloudConfig.sh 验证
  type: lab
  source_pages: p316-321
  source_chapter: DNS and proxy configuration — "Configure DNS and proxy on the Call Server / Test the connectivity with the Cloud servers"
  source_quote: |
    "The DNS and HTTP proxy configuration will only be used by Rainbow and Cloud Connect agents" (p317)；
    "Primary DNS address (default is)? 192.168.1.250 Secondary DNS address (default is)? 127.0.0.1" (p317)；
    "####  DNS test on connect2.opentouch.com domain #### ... ####  TCP connection to SOCKS5
    connect2.opentouch.com:80 #### ... Success !!" (p320-321)
  steps: |
    1. 配 DNS：mtcl 登录 → netadmin -m → 14 'DNS configuration' → 2 'Create/Update DNS setup' → Primary DNS=192.168.1.250（实验口径）→ Secondary=127.0.0.1（无备用 DNS 也必须填 127.0.0.1 占位）。
    2. 复核/删除：同菜单 1 'View DNS configuration'（显示 Primary/Secondary）；3 'Delete DNS setup' → y 确认。
    3. 配代理（按需；实验无代理仅展示）：netadmin -m → 15 'Proxy configuration' → 2 'Create/Update Configuration' → Host address、Proxy port（示例 192.168.1.253:3128）、Proxy login/password → 1 'View' 复核 → 3 'Delete' 撤销。
    4. 连通性验证：mtcl 执行 checkCloudConfig.sh——依次测试：①DNS 解析 connect2.opentouch.com（显示所用 DNS 与解析地址）；②代理参数检查（无代理时提示 No found Proxy parameters，属正常路径）；③443 连接（openssl s_client 显示 ALE-CLOUDCONNECT-ROOT 证书链 → "Success !!"）；④SOCKS5 80 端口 TCP 连接（"Success !!"）。
  verification: |
    checkCloudConfig.sh 的 443 测试与 SOCKS5 80 测试均打印 "Success !!"（p321）。
  conditions: 该 DNS/代理配置仅服务于 Rainbow 与 Cloud Connect 代理（不影响系统其他 DNS 用途的表述以原书 Notes 为准）。
  tags: [lab, netadmin, dns, proxy, checkcloudconfig]

- id: c15
  title: FTR 执行与 RTR 启用监控（swk 许可 → 信任主机 → spadmin 查 CCSID → CCTool FTR → RTR）
  type: lab
  source_pages: p322-337
  source_chapter: First Time Registration (FTR) & Right To Run (RTR)
  source_quote: |
    "netadmin -m ... 11.Security ... 1. 'Firewall(iptables) Configuration' ... 2. 'Add a trusted host'
    ... Trusted host's IP address ? 192.168.1.9" (p324-325)；
    "Your choice or return to update status ? 1 ... I do accept ALE Cloud Connect Terms & Conditions
    ... (y/n)? y ... FTR done!!" (p329)；
    "Service state = RTR_RUNNING CCI mode = CCI_NORMAL Remaining Qualifying Period = 30.0" (p332)
  steps: |
    1. 装 .swk 许可：mtcl 登录 → netadmin -m → 11 Security → 1 Firewall(iptables) Configuration → 3 Restricted Access Configuration → 2 Add a trusted host（pc / 192.168.1.9，实验口径）→ a 应用 → Filezilla 连 OXE（mtcl）把 .swk 传到 /usr4/BACKUP/OPS（实验口径 NAS 路径 ENTP[CV]TE402\Licenses\Cloud Connect licences 选本 POD 文件；恢复失败且文件名过长时改名为 license.swk 再试）→ swinst 恢复。
    2. 前提核对：Internet 可达（含代理可选）；本地 DNS 可解析 CCI 域名；OXE 已知激活账户（CC-SUITE-ID）；checkCloudConfig.sh 连通性通过（见 c14）。
    3. 查 CC-Suite-ID：mtcl → spadmin → 2 Display active file → 读 Cpu Id 1 = CCSID:xxxxx 与 Suite Id 行（RTR 未启用时不显示 Suite Id）。
    4. 核对 Cloud Connect enable：OXE WBM → Cloud Connect → Cloud Connect enable=YES（新装机默认启用；该参数是使用 CCTool 的前提）。
    5. 手动 FTR：CCTool → 1 FTR status & options（读状态：FTR status=Not registered、CC agent state=XMPP_DISCONNECTED）→ 1 Perform FTR → 接受 Terms & Conditions（y）→ "FTR done!!" → 状态变 Registered/Success、Jid=<suite-id>-3@reg-product.connect2.opentouch.com、CC agent state=XMPP_CONNECTED。
    6. [panic 恢复] FTR with PIN：CCTool → 1 → 2 Perform FTR with PIN code → 输入 helpdesk 发的 6 位 PIN（5 天有效）→ 完全重置云配置并重注册（前提 RTR 与 ccagent 进程在跑）。
    7. 启用 RTR：OXE WBM → System/Licenses → FlexLM Licensing Enabled=No（虚机必须核对，两模式不可并存）+ Cloud Connect RTR Enabled=Yes → Tips：需要重启 OXE。
    8. RTR 状态：CCTool → 2 RTR status & options → 读 Service state=RTR_RUNNING、CCI mode=CCI_NORMAL、Remaining Qualifying Period=30.0、Response Code=201、Cause Message=RTR OK - New branch created…；需要时选 1 Force RTR 立即请求。
    9. 日常维护：KeepAlive（WBM Cloud Connect → KeepAlive Timer；默认 90s；CCTool 3 可查各 Feature 开关）；事件 incvisu（6200-6214 + 647-651）；日志级别 CCTool 4（ERROR/INFO/DEBUG/TRACE，可按特性设，1=all）；进程管理 ps -edf | grep ccagent、service ccagent status/restart（root）、dhs3_init -R CCPROCESS；日志 /var/log/ccagent.log、/tmpd/cloud_cnx/log/ccprocess.log、/tmpd/CCAlarm.log。
  verification: |
    FTR 后 CCTool 显示 "FTR status = Registered / FTR operation status = Success / CC agent state =
    XMPP_CONNECTED"（p329）；RTR 状态 Service state=RTR_RUNNING 且 Remaining Qualifying Period=30.0
    （p332）；incvisu 出现 6207（连接成功）。
  conditions: 备机禁止做 FTR；FTR 需电话应用已启动；RTR 修改后重启一次。
  tags: [lab, ftr, rtr, cctool, spadmin, wbm]

- id: c16
  title: 从 MyPortal 下载 PoD 许可文件（Asset & service manager）
  type: lab
  source_pages: p381-385
  source_chapter: Download POD license files from MyPortal
  source_quote: |
    "Connect to MyPortal URL: ­ https://myportal.al-enterprise.com/ Enter your credentials" (p382)；
    "/Installed Base/ Asset & service manager/ ... select Explore Purple Assets and click on Search" (p383)；
    "To be able to download and implement the POD license files, the Project status must be seen
    Active" (p384)
  steps: |
    1. 登录 MyPortal（https://myportal.al-enterprise.com；无凭证联系 BP 客户经理或 ALE 代表申请）。
    2. 顶栏 Installed Base → Asset & service manager。
    3. 列表选 Explore Purple Assets → Search。
    4. 左侧列表选中客户项目。
    5. 对每个产品（示例：OXE、OmniVista 8770、VAA）点 CPU ID 图标下载 PoD 许可文件——OXE 保存 .swk 到本机。
    6. 对其余应用重复同样操作；下载的文件由技术员装入各应用完成整套交付。
    7. 状态核对：项目必须显示 Active 才能下载与实施；显示 Pending 表示项目尚未激活（交付问题等），需先解决。
  verification: |
    各产品许可文件（OXE 为 .swk）成功下载且项目状态为 Active（p384）。
  conditions: 项目与许可池已在 LMS/商务侧建好（c17 前提）。
  tags: [lab, myportal, pod, license-download]

- id: c17
  title: Purple on Demand 配置与 OXE-LMS 许可同步核查（swk+FTR+RTR+NTP → spadmin 对账 → 用户/软话机/阈值实测）
  type: lab
  source_pages: p386-408
  source_chapter: Purple On Demand — "Configure the POD (Purple On Demand) feature / Check the licenses synchronization between OXE and LMS server"
  source_quote: |
    "Warning CORRECT “SWK” FILE IS MANDATORY, WITH: ­ CCSID (CLOUD CONNECT SUITE ID) ­ LOCK 431: OPEX
    MODE SET TO “1”" (p388)；
    "Choice “10”: Force LMS synchronization ... Start Synchronization ... Synchonization done…" (p398)；
    "Voice Enterprise “15 | 0/0 | 18” 15 is the number max of new licenses ... The first “0” is the
    total number of licenses consumed for the node on the LMS service ... 18 is the maximum number of
    licenses subscribed" (p397)
  steps: |
    1. [前提 1：swk] 装入正确 .swk（必须含 CCSID 与 LOCK 431=1）→ 重启 OXE → mtcl → spadmin → 1 Display current counters 核对 OPEX Flag=1、PANIC Flag=0（并列出 OPEX Mode 各项计数）；2 Display active file 核对 431 Opex Mode=1（87/165 锁与版本相关）。
    2. [前提 2：FTR/RTR] netadmin -m → 14 配 DNS（192.168.1.250；备用 127.0.0.1）→ a 应用 → checkCloudConfig.sh 全绿 → CCTool → 1 → Perform FTR → 接受条款 → FTR done/Registered → WBM System/Licenses → Cloud Connect RTR Enabled=Yes。
    3. [前提 3：NTP] swinst → 2 Expert → 6 System management → 1 Date & time update → 3 NTP server management → 5 Modify NTP configuration → 2 Add/Modify server → 192.168.1.252（实验口径）→ 返回菜单 1 Start NTP（NTP is running）。
    4. [进程确认] incvisu 显示 6201 CCagent started 与 6250 LmsAgent started；mtcl 登录横幅看 Panic LMS Check=0（0=连接正常，1=不正常）。
    5. [LMS 侧前提] 客户项目已在 LMS/MyPortal 创建并分配许可池（可挂一台或多台 OXE）。
    6. [对账] spadmin → 11 Read LMS licenses：读四列计数（例 Voice Enterprise “15 | 0/0 | 18”：15=全网还可新申请、0/0=本节点在 LMS/OXE 两侧消耗、18=全网订阅上限；lms/oxe 两列必须一致，不一致即 panic）→ 10 Force LMS synchronization（Start/…done）→ 12 Help LMS licenses 读机型映射规则。
    7. [实测：物理话机] WBM Users/Create 建话机、OPEX Activation=Yes → spadmin 11 复核：Voice Enterprise 变 “14 | 1/1 | 18”（消耗+1）。删除该用户则许可释放回 LMS。
    8. [实测：软话机] 建软话机（Set type SIP、Sub type ALES-mobile/ALES-desktop、OPEX Activation=Yes）→ 复核：ALE Softphone 与 Voice Enterprise 各消耗 1（双份）。
    9. [实测：tandem] 主机建多线话机 flag=1，副机建多线话机 flag=0 并配成副站——副机不占许可（若副机原 flag=1 则自动归 0 并在 LMS 释放）。
    10. [实测：DeskSharing] DSS 与 DSU 两个用户均开 flag（各占一份 Voice Enterprise）。
    11. [实测：阈值类] WBM → OPEX Licences → Edit → 设 Number max of DR-Link recordings=5（范围 0-15000；ACD Operators 0-2800；4059 attendants 0-1000）→ spadmin 11 复核 OXE Recording API option 变 “0 | 5/5 | 25”。
    12. [排障] eqstat d <dn>：License availability: NO + 终端 OUT OF SERVICE 表示无许可（NOE 话机屏显 "No license available"）；SIP 设备注册收 402 Payment required、事件 5816、/tmpd/sipalarm.log 有 "Register of SIP user xxxx rejected - Licence required"；日志 /var/log/lmsagent.log.*（mtcl）与 /var/log/nginx access.log/error.log（root），infocollect 可收集。
  verification: |
    spadmin 计数器随建/删用户精确增减且 lms/oxe 两列一致（p397/p400/p402/p404）；Panic LMS Check=0
    （p396）；incvisu 出现 6250 LmsAgent started（p396）；Force LMS synchronization 返回
    "Synchonization done…"（p398）。
  conditions: LMS 侧项目与许可池必须先建好；CAPEX 模式下 OPEX flag 显示但不生效（原书 Warning）。
  tags: [lab, opex, pod, lms, spadmin, synchronization]
```

## 收尾自检：对照 BOOK_OVERVIEW.md 20 项任务清单

| task | 覆盖情况 |
|---|---|
| task-01 RLAB 环境 | 无实验章（p1-20 为环境说明页）；节点信息表已入 principle p38 / framework f02 作 Boundary 背景。 |
| task-02 部署 SOT VM | 有 → c01（Standalone）；c09（Hosted ESXi，含 vSphere 附录）。 |
| task-03 更新 SOT | 无独立实验章。更新操作内嵌于 c01（步骤域 4 Update，p47-48）与 c09（步骤 6，p197-198），两章含完整操作序列。 |
| task-04 Template Factory | 有 → c06（降级模式）；标准前置与转换判据在 framework f03/f04。 |
| task-05 媒体传输与项目配置 | 无独立实验章，作为公共动作内嵌于 c02 步骤 3-7、c03 步骤 1-3、c04 步骤 1、c07/c08/c10/c11/c12 各自项目段。 |
| task-06 单版本全加载 | 有 → c02。 |
| task-07 多版本与切换 | 有 → c03（含 swinst 手工附录）。 |
| task-08 补丁安装 | 有 → c04（双场景）。 |
| task-09 分发器模式 | 有 → c05（含清理与 downstat）。 |
| task-10 虚拟化平台决策 | 无实验。讲义矩阵（p133-136），属决策内容，已浓缩进 framework f15/principle p10-p11。 |
| task-11 OXE VM 加载 | 有 → c07（KVM）、c10（ESXi .ova）。 |
| task-12 OMS 加载 | 有 → c08（KVM）、c11（ESXi）。 |
| task-13 GAS 加载 | 有 → c12。 |
| task-14 GAS 后安装 | 有 → c13（含 FlexLM 附录）。 |
| task-15 GAS 运维 | 部分 → c13 步骤 12-13（gasversion/gasbackup/FlexLM）；host 升级与 UPS 为讲义（p236-238），数值在 principle p16。 |
| task-16 云连通性 | 有 → c14。 |
| task-17 FTR 与 PIN | 有 → c15（FTR 主线 + PIN 恢复 + RTR 启用）；PIN 流程细节另见 framework f22。 |
| task-18 RTR 监控 | 有 → c15 步骤 7-9；状态机数值在 principle p21-p24。 |
| task-19 PoD 许可下载 | 有 → c16。 |
| task-20 PoD 配置与同步 | 有 → c17。 |

**统计**：17 条（全部为 How-To 实验章）；20 项任务中 15 项有实验直接覆盖，task-01/03/05/10 无独立实验章（环境说明/内嵌操作/决策矩阵，处理方式已在表中注明）。
