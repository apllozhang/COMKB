# 框架/流程/结构候选 — OmniPCX Enterprise Loading (ENTPXTE402EN Ed12)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径（swinst/netadmin/CCTool/spadmin 菜单树）、组件关系图示、平台/界面分区。实验环境给定值（IP/密码/账号）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——环境 → SOT 工具 → 三条加载路径 → 两种承载形态 → 云连接 → 订阅许可
  type: flow
  source_pages: p1-408
  source_chapter: 全书章序（SOT / CS SOFTWARE LOADING / EASY INSTALLATION / OXE-V / GAS / CLOUD CONNECT / OPEX）
  source_quote: |
    "S.O.T . stands for «Software Orchestration Tool»; it is a solution to deploy ALE products
    (physical or virtualized)" (p22)
    "The OmniPCX Enterprise Call Server software package dedicated to virtualized environment is
    called OXE-V" (p133)
    "OXE registration in Cloud Connect infrastructure is mandatory" (p352)
  summary: |
    课程按八段推进：①RLAB 实验环境（p1-20，五类节点与访问表）；②S.O.T. 部署工具（p21-48，含 Stand-alone 部署 How-To）；③CS 软件加载三场景（p49-110：单版本、补丁、多版本，各配 How-To）；④Easy Installation 分发器模式（p111-130，无 SOT 环境的替代加载）；⑤OXE-V 虚拟化（p131-154）；⑥GAS 通用设备服务器（p219-282，含加载与后安装 How-To）；⑦Cloud Connect（p283-349，含 DNS/代理与 FTR/RTR How-To）；⑧OPEX/Purple on Demand（p350-408，含许可下载与 PoD 配置 How-To）。OXE-V 章与 GAS 章之间穿插虚拟化相关 How-To（p155-218）。这是"先装起来、再连上云、最后换许可模型"的交付主线。
  conditions: 无特殊版本前提；各章 How-To 依赖前章实验成果（如 FTR 依赖 swk 许可与连通性）
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: RLAB 全虚拟化实验平台——POD 结构与五类节点访问表
  type: structure
  source_pages: p1-20
  source_chapter: TRAINING LAB ENVIRONMENT / POD TOPOLOGY / PC CLIENT / SOT / CS3 / KVM / GAS
  source_quote: |
    "Remote Lab allows accessing a pool of virtual and physical machines (depending on the course)
    hosted in a data center." (p5)
    "PC CLIENT PC-CLIENT-PODX 192.168.1.9 ... Administrator superuser" (p10)
    "VM SOT sot 192.168.1.130 ... admin upload Default password: letacla New password: Superuser2580*" (p13)
  summary: |
    实验平台分 POD（相互独立、配置相同、共享公共资源 NAS 与 SIP 模拟器 12.0.0.2），网段 192.168.1.x/24，网关 192.168.1.254，内部 DNS 192.168.1.250。五类节点（实验口径）：PC Client（物理 Windows，192.168.1.9，Guacamole RDP 进入，桌面快捷方式到各服务器，D 盘 USB、Y 盘trainer 共享、Z 盘 ENTP NAS）；SOT VM（192.168.1.130，admin/upload，letacla→Superuser2580*）；CS3（csa 192.168.1.101 / csm 192.168.1.103，mtcl/swinst/root）；KVM 服务器（kvm 192.168.1.55 root/superuser，其上部署 OXE 192.168.1.201/203 与 OMS 192.168.1.213）；GAS 服务器（gas 192.168.1.45 root/letacla1，其上 OXE 192.168.1.1/1.3、OMS 192.168.1.13、WebRTC VM 192.168.1.15 rainbow/Rainbow123）。RLAB 面板对物理 PC Client 的 start/stop/reboot 灰置。
  conditions: 仅 RLAB 培训环境（"RLAB ONLY, NO CLASSROOM EQUIPMENT"，p3）；所有 IP/密码为实验口径
  tags: [structure, lab, rlab, topology]

- id: f03
  title: SOT 形态与模式矩阵——ISO/OVA 交付 × Standalone/Hosted × default/Template Factory
  type: structure
  source_pages: p22-29
  source_chapter: S.O.T. / INTRODUCTION / « STAND-ALONE » MODE / « HOSTED » MODE / configurations
  source_quote: |
    "The S.O.T . is a virtual machine delivered under an “ISO” format • This “.iso” file
    (sot-x.x.xxx.xxx.iso) contains the “.ova” file" (p23)
    "In « Standalone mode » ... Installed on technician laptop thanks to Virtual Box client or
    VMware workstation ... Used to deploy mainly physical servers as OXE CS, GAS « bare metal »" (p24)
    "In « Hosted mode » ... Deployed in a vSphere ecosystem : ESXI server ... Used to deploy other
    virtual machine(s) as OXE, OMS,…" (p25)
  summary: |
    三维矩阵：交付形态（ISO 内含 OVA；更新补丁 sot-update-x.x.xxx.xxx.zip）× 运行模式（Standalone=技术员笔记本 VirtualBox/VMware Workstation，主用于物理机 OXE CS/GAS 裸机加载；Hosted=部署在 vSphere/ESXi，主用于加载同虚拟化系统内的 OXE/OMS 虚机，或经 Template Factory 服务 KVM 环境）× 配置（default=softwareOrchestrationTool.ova，物理加载与目标 OVA 生成；Template Factory=softwareOrchestrationToolWithTemplateFactory.ova，加第二块盘建模板，前置 8CPU/16GB 内存/500GB 第二盘/Vmx 标志/USB 控制器）。版本兼容查 S.O.T. Release Note（TC2456）。一次只允许一个部署任务（p22 Notes）。
  conditions: Template Factory 仅 Hosted 模式用于虚机加载；降级模式见 f04
  tags: [structure, sot, mode-matrix, template-factory]

- id: f04
  title: Template Factory 降级模式五步流程（低资源机器）
  type: flow
  source_pages: p29, p155-165
  source_chapter: «TEMPLATE FACTORY» CONFIGURATION IN DEGRADED MODE / How-To
  source_quote: |
    "It is important to follow those steps in that order: • Start by deploying SOT with the
    “softwareOrchestrationTool.ova” • Add a new virtual disk of 50Gb. • Start the SOT vm • In the
    SOT console type “templateFactory”" (p29)
    "Enter Y to bypass resource control ... Template Factory mode is enabled in degraded mode for PC" (p164)
  summary: |
    五步（顺序强制）：①先用标准 softwareOrchestrationTool.ova 部署 SOT；②关机后在 VirtualBox 加一块 50GB VDI 虚拟盘（Settings→Storage→Controller SCSI→Adds hard disk）；③启用嵌套虚拟化（System→Nested VT-x/AMD-V；被设备安全阻止时改注册表 HypervisorEnforcedCodeIntegrity Enabled=0 后重启 PC；Paravirtualization Interface 选 KVM）；④启动 SOT，控制台输入 templateFactory 命令，按 Y 绕过资源检查；⑤Web 界面出现 Template Factory 功能。原理：绕过硬编码的硬件前置，使任何服务器/笔记本都能构建 OVA；浏览器首页会显示特定警告。
  conditions: 硬件前置不再受控（降级代价）；OVA 构建时长强依赖机器（RAM/核数）
  tags: [flow, template-factory, degraded-mode, nested-virtualization]

- id: f05
  title: SOT Web 界面分区与两种工作模式（Easy/Expert）
  type: menu-path
  source_pages: p30-32
  source_chapter: USE PRINCIPLE / EXPERT MODE USE PRINCIPLE
  source_quote: |
    "Access to the 3 main pages (4 for Template Factory mode) • Projects • Declare the products to
    load or to update • Medias • Upload softs sources ... • External storage ... • Template Factory" (p32)
    "Two working modes • Easy • Kind of wizard ... • Expert • Management of medias and projects
    are independents: • Medias have to be declared before projects creation" (p31)
  summary: |
    首次开机在 VM 控制台配 IP/键盘，之后经 https://SOT-IP 访问 Web 界面（登录口令）。主页面四个：Projects（声明要加载/更新的产品）、Medias（上传软件源）、External storage（声明 NFS/Windows 服务器存储）、Template Factory（已创建镜像列表，仅该模式显示）。Settings 区含：IP 设置、SOT Update、备份/恢复、账户管理（密码/口令短语）、报表（日志）、重启/关机。Easy 模式是向导（产品类型→媒体→目标设置），Expert 模式下媒体与项目独立管理且媒体必须先声明。
  conditions: Web 访问需登录；Settings 中可改网络（见 p46/p196 一致性警告）
  tags: [menu-path, sot, web-ui, easy-expert]

- id: f06
  title: SOT 媒体库三类型与支持格式清单
  type: structure
  source_pages: p33-34, p86, p95
  source_chapter: EXPERT MODE USE PRINCIPLE / Medias management
  source_quote: |
    "Medias management • 3 types of database • Windows server • NFS server • Internal SOT local
    storage • Supported format • « .iso » file • Complete software version • « .zip » file •
    Software patches, hotfixes • License files • « .mao », « .swk »..." (p33)
    "you have to establish a FTP or SFTP (port 2222) session ... Login: upload • Password: sot" (p86)
  summary: |
    媒体存放三选一：Windows 服务器、NFS 服务器、SOT 本地存储。格式：.iso=完整软件版本；.zip=补丁/热修复；许可文件 .mao/.swk 等。向 SOT 本地存储传文件的通道：FTP 或 SFTP（端口 2222），账号 upload/sot（实验口径），客户端常用 Filezilla；上传后点 Refresh medias list → 勾选文件 → Declare media(s)，版本进入可用列表。目标为虚机时项目还可勾 OVF generation 让 SOT 生成 .ova/.ovf；目标为物理机时需提供 MAC 地址。
  conditions: 实验口径 upload/sot；Hosted/ESXi 章节使用 FTP（非 2222 端口表述）
  tags: [structure, sot, media, ftp]

- id: f07
  title: SOT 版本命名与更新规则（ISO A.B.XXX.000 / zip A.B.XXX.YYY）
  type: flow
  source_pages: p35, p47-48, p197-198
  source_chapter: SOT UPDATE
  source_quote: |
    "The naming of the “ISO” files will be A.B.XXX.000 ... The naming of the “zip” file will be
    A.B.XXX.YYY ... “YYY”: indicates the rank of the “zip” file" (p47)
    "This functionality will only be offered for S.O.T solutions in the same major version. The
    update will be forbidden for version not in the same major version." (p47)
  summary: |
    更新流程：Settings/Update S.O.T. → 选 zip+MD5（媒体须在托管 SOT 的 PC、SOT 本地存储或 NFS 三处之一）→ Launch update（更新过程 SOT 重启）→ About 菜单查版本。规则：仅同主版本（A.B）内可更新，跨主版本禁止；更新后版本号末 3 位非 000（如 3.2.002.006）；zip 与 ISO 同时交付时功能同级（仅 OS 可能不同）；zip 可单独交付修缺陷但须标明所装 ISO 版本。
  conditions: 同主版本限制；update 媒体三处可放
  tags: [flow, sot-update, versioning]

- id: f08
  title: 单版本全加载端到端时序——BOOTP/DHCP→TFTP→Linux RAM→FTP 安装
  type: diagram
  source_pages: p52, p56-60
  source_chapter: CS SOFTWARE LOADING / GENERALITIES / BOOT ON ETHERNET / COMPLETE MONO VERSION LOADING
  source_quote: |
    "Depending on the call server type, the initial request can be: • BOOTP (CS and CPU Crystal) •
    DHCP (Appliance Server) ... CS: startup.txt • Appliance Server: pxeloader • CPU Crystal: none" (p60)
    "The S.O.T . core application is rendered through a Virtual Machine containing all necessary
    layers, services and application to deploy ALE International products • DHCP server • FTP server" (p56)
  summary: |
    加载经 IP 进行（CS 与 SOT 间需 IP 连通，V24 链路用于启动与检查安装）。时序：CS 网络引导 → BOOTP/DHCP(PXE) 请求 → SOT 交付 IP 配置与引导文件（CS=startup.txt、AS=pxeloader、CPU Crystal 无文件）→ CS 用 TFTP 下载文件清单与 Linux RAM → Linux 入内存自动启动 → DHCP 请求 → 经 FTP 自动安装 Linux → 传 Linux/工具/swinst → 下载版本与补丁 → 安装结束 CS 重启。SOT 核心即一台含 DHCP+FTP 服务的虚机。空盘自动进 Standard Installation；盘已有内容需 grubboot ETHER 或 BIOS 菜单强制网络引导（p57）。
  conditions: 目标机与 SOT 同网段；V24/控制台用于过程观察
  tags: [diagram, loading, bootp, tftp, ftp]

- id: f09
  title: CS 启动相位链与可中断/可失效点
  type: diagram
  source_pages: p58
  source_chapter: CS START UP PHASES
  source_quote: |
    "• Bios starting up • System auto-test • Bootloader starting up • GRUB loader starting up •
    Linux starting up ... • Telephonic application starting up • Automatic starting up if autostart
    is set in swinst • Manual starting up under mtcl with command RUNTEL" (p58)
  summary: |
    启动链六相位：BIOS→系统自检→Bootloader→GRUB→Linux（从 active 分区启动）→电话应用。可干预点：BIOS 相位可中断（选引导设备），GRUB 相位可失效（grubboot ETHER 即从此处改走网络引导），电话应用可自动（swinst 里 autostart 已设）或手动（mtcl 账号 RUNTEL 命令）。这张图是"加载失败停在哪儿"的定位底图。
  conditions: autostart 行为在 swinst 菜单管理
  tags: [diagram, boot-phases, grubboot, runtel]

- id: f10
  title: 硬盘双分区目录结构图（active/inactive/公共区）
  type: diagram
  source_pages: p54-55
  source_chapter: STRUCTURE OF THE HARD DISK
  source_quote: |
    "Disk partition with the ACTIVE version • / Active Linux operating system • /usr2 (linked with
    /DHS3bin) Active OXE version • /usr3 (linked with /DHS3data) Active Data Base • /var Logs and
    active variable data ... /root2_d (linked with /root2) Inactive Linux operating system • /usr5
    (linked with /DHS3bin2) Inactive OXE version • /usr6 (linked with /DHS3data2)" (p55)
  summary: |
    三区结构：活动分区（/、/usr2↔/DHS3bin 活动版本、/usr3↔/DHS3data 活动数据库、/var 日志与变量数据）；公共区（/usr4↔/DHS3dyn 动态计费数据与备份、/usr7↔/DHS3ext 系统语音引导）；非活动分区（/root2_d↔/root2、/usr5↔/DHS3bin2、/usr6↔/DHS3data2、/var2）。该结构是多版本加载、分区复制（swinst 3-2 子菜单）与切换（swinst 3-3）的底层依据；/usr4/ftp/Rload 还承接分发器模式解包物（见 f15）。
  conditions: 无版本前提；N3 以下迁移会重建分区结构（p78）
  tags: [diagram, partitions, filesystem, multi-version]

- id: f11
  title: 多版本加载两分支流程——复制+补丁 vs 完整加载+数据复制
  type: flow
  source_pages: p71-77
  source_chapter: MULTI VERSIONS LOADING - PRINCIPLE / FIRST POSSIBILITY / SECOND POSSIBILITY
  source_quote: |
    "• Copy of the complete first version and loading of a software patch for update • Possible when
    the basic version stays the same • For example: N4.205.19 to N4.205.36a • Complete loading of a
    new version and copy of the data ... To be used for a different version of Linux • For example:
    N3.521.12 to N4.205.36a" (p73)
    "« Duplicate Linux Data » & « Duplicate OXE Data » parameters • Or, to be done manually ... ”
    Switch partition after update installation” parameter" (p76-77)
  summary: |
    分支一（同基础版本，如 N4.205.19→N4.205.36a）：①active 整体复制到 inactive；②在 inactive 装补丁；③切换（重启到 inactive）。分支二（跨 Linux 版本，如 N3.521.12→N4.205.36a）：①在 inactive 装完整新版本；②复制数据（OXE 数据库与 Linux 数据；可经 SOT 项目参数 Duplicate OXE Data/Duplicate Linux Data 自动，或手工）；③自动重启切到 inactive（参数 Switch partition after update installation，可定时 Switch time）；④按需装新 OPS 文件（SOT 可自动带许可）再重启。注意：切换期间板卡可能收到新版本二进制，回退老版本时可能要再下载（p72）。
  conditions: 两版本可同时驻留一盘；OPS 文件变化时分支二需要第④步
  tags: [flow, multi-version, duplication, switch]

- id: f12
  title: swinst 菜单树全景（Main/Expert/Cloning/Identity/Remote download）
  type: menu-path
  source_pages: p98-99, p114, p117-130
  source_chapter: swinst tool（各 How-To 附录与 Easy Installation 章）
  source_quote: |
    "In “swinst” menu 2 - Expert menu • 3 - Cloning & duplicate operations • 2 - Partitions
    duplication • 2 - Duplicate Linux Data" (p98)
    "2.Expert menu/9.Remote download/10. ‘Local load as distributor of ISO image/ZIP file and
    installation’" (p114)
  summary: |
    swinst（swinst 账号登录）两层：Main menu（1 Easy menu / 2 Expert menu）；Expert menu 九项——1 Packages installation、2 Deliveries installation、3 Cloning & duplicate operations（其下 1 CPU cloning / 2 Partitions duplication（再分 1 Duplicate Linux, packages and Linux data、2 Duplicate Linux data、3 Duplicate delivery、4 Duplicate database、5 Duplicate all、6 About last duplicate operation）/ 3 Switch on inactive version / 4 Postponed switch）、4 Backup & restore operations、5 OPS configuration、6 System management、7 Database tools、8 Software identity display（1 System release identity / 2 Application software identity / 3 Delivery status / 4 Component status / 5/6 validity checking；查分区时 0=active 1=inactive）、9 Remote download（十项，含 7 Cleaning operation on master/distributor CPU、8 Programmed operations、9 Fast Delta programmed operations、10 Local load as distributor）。NTP 管理在 6 System management→1 Date & time update→3（p394）。
  conditions: swinst 账号；切换后首次进入 swinst 必须输国家码（p99/p110 Notes）
  tags: [menu-path, swinst, cloning, remote-download]

- id: f13
  title: 补丁安装双场景操作流——active 分区（停话音）与 inactive 分区（先复制）
  type: flow
  source_pages: p100-110
  source_chapter: Patches installation on active & inactive partitions (How-To)
  source_quote: |
    "STATIC PATCH INSTALLATION ON ACTIVE PARTITION REQUIRES TO STOP THE TELEPHONE APPLICATION. SO,
    SYSTEM IS REBOOTED AUTOMATICALLY" (p104)
    "3.1.2. Duplicate all data from active to inactive partitions ... 5 - Duplicate all" (p106)
  summary: |
    active 分区：siteid 查当前版本 → SOT Expert 项目 update → Update on inactive partition 不勾 →（静态补丁时 OXE 自动重启停话音）→ completed → siteid 复核（实验演示 0→19→36，实验口径）。inactive 分区：先 swinst 2-3-2-5 Duplicate all（连答 y，复制 Linux+网络配置），ver2cho visible 与 df -v 核对两分区一致 → SOT update 项目勾 Update on inactive partition（静态/动态无差别、不立即重启）→ 可设 Switch partition after update installation/Switch time/Switch back → 切换时重启。zip 与 iso 的差别：zip 通常一补丁一文件（静/动分开装），iso 可同含静态+动态一次装（p102）。
  conditions: 动态补丁必须在对应静态补丁之后（p104/p105 Warning）；Duplicate all 失败可退回完整加载（p106 Warning）
  tags: [flow, patch, static, dynamic, partition]

- id: f14
  title: Easy Installation 分发器流程与文件落点图（/tmpd → Rload）
  type: flow
  source_pages: p111-130
  source_chapter: EASY INSTALLATION OF OXE / How-To / Maintenance
  source_quote: |
    "The BP must transfer, through FTP , the “ISO image” and/or “ZIP files” to the “/tmpd” directory
    of the Call Server" (p113)
    "the software (ISO image/ZIP files) transferred in the CS “/tmpd” directory ... are unpacked in:
    ­ “usr4/ftp/Rload/version” directory for a complete version ­ “usr4/ftp/Rload/patch” ... “usr4/
    ftp/Rload/dynpatch”" (p129)
  summary: |
    背景：客户环境不允许临时外部 BP PC/SOT 虚机（p112）。流程：①PC IP 加入 OXE 信任主机（IP tables，实验口径 192.168.1.9）；②Filezilla 把 iso/zip 传到 CS /tmpd；③swinst→2 Expert→9 Remote download→10 Local load as distributor →输入文件名→确认（REMOTE LOAD OPERATION，Client CPU type DISTRI）；④全版本/静态补丁强制装 inactive 分区，动态补丁可选分区（安装器询问 1 ACTIVE/2 INACTIVE）；⑤复核版本（swinst 8-2）；⑥必要时复制 Linux 数据与数据库、切换分区。落点与清理：解包物在 /usr4/ftp/Rload/{version,patch,dynpatch}，加载结束不自动删除，用菜单 9-7 Cleaning operation 清理（只清 Rload）；/tmpd 源文件安装结束自动删除。动态补丁装完后按提示用 downstat d/i/t 检查需下载的板卡/IP 话机/40x9 话机（p127）。
  conditions: full version 与 static patch 必须装 inactive（p113）；无需重新分区的前提下替代 swinst 常规安装
  tags: [flow, distributor, tmpd, rload, easy-installation]

- id: f15
  title: OXE-V 虚拟化技术矩阵与许可控制路径图
  type: structure
  source_pages: p133-136
  source_chapter: OXE-V / GENERAL OVERVIEW / Virtualization technologies / Licences control
  source_quote: |
    "VMware ESXi (1) 8.0 7.0 / Microsoft Hyper-V 2022 2019 2016 (2) / KVM kernel ≥ 4.12.14 & KVM ≥
    5.2 (3) / Nutanix (AHV) 20230302 20220304 (except OST64) / AWS (except OST64)" (p134)
    "Hyper-V , Nutanix and AWS don’t provide a native way to redirect an USB dongle ... Cloud Connect
    is the mandatory license control process in case an OXE is virtualized over Hyper-V , Nutanix or
    AWS technology" (p136)
  summary: |
    平台矩阵：VMware ESXi 8.0/7.0（兼容含该版本的 minor 更新）；Microsoft Hyper-V 2022/2019/2016（CS 用 gen1 虚机，OXE-MS/OST64/EEGW 用 gen2）；KVM 内核 ≥4.12.14 且 KVM ≥5.2（RHEL/SLES/Proxmox 等标准 KVM 均可；Nutanix AHV 等定制 KVM 需专项认证）；Nutanix AHV 20230302/20220304（OST64 除外）；AWS（OST64 除外）。许可双路径：FlexLM+加密狗仅 ESXi/KVM；Hyper-V/Nutanix/AWS 无 USB 重定向也无 FlexLM 虚机交付，必须走 Cloud Connect（CC-SUITE-ID）。架构组件：主/备 CS、FlexLM server、OMS；OXE-V 详见 TBE043 虚拟化设计指南。
  conditions: 版本号为 Ed12 时点值；平台演进需复核 TBE043
  tags: [structure, oxe-v, virtualization, licensing, matrix]

- id: f16
  title: OXE-V 六种拓扑图组与 PCS 接管行为
  type: diagram
  source_pages: p142-148
  source_chapter: OXE-V TOPOLOGIES
  source_quote: |
    "In case of failure of the signaling link with Call Server, OXE-MS can be rescued by a PCS •
    Switch from CS to PCS: soft reset (voice calls are released but the Virtual Machine is not
    rebooted) • Switch from PCS to CS: hard reset (Virtual Machine is rebooted)" (p147)
  summary: |
    六种拓扑：①全虚拟化（OXE-V CS + OMS-1/2 + SIP 运营商）；②呼叫服务器冗余（local 与 spatial，csa/csb 各带 OMS）；③原生加密（信令加密 + SRTP）；④混合（虚机 CS + 硬件媒体网关/ISDN 中继/数字话机）；⑤分支机构（总部 OXE-V CS + WAN + 分支 OMS）；⑥组网（ABC link 连 Node 1/Node 2）。PCS 行为：CS 信令链路故障时 OMS 可由 PCS 接管——CS→PCS 软复位（话音呼叫释放但虚机不重启），PCS→CS 硬复位（虚机重启）。
  conditions: 拓扑图示为讲义级；详细设计在 TBE043
  tags: [diagram, oxe-v, topology, pcs]

- id: f17
  title: OMS 软媒体网关定位与能力结构
  type: structure
  source_pages: p138-140
  source_chapter: OXE MEDIA SERVICES / OMS: OVERVIEW / FEATURES / LICENSES
  source_quote: |
    "120 VOIP channels per OMS 240 OMS per OXE ... This soft media-gateway provides media processing
    features of a GD4 board" (p138)
    "Lock 384: ‘OXE Media Services’ ... Lock 385: ‘VoIP channels on OMS’ ... It can be installed
    without rebooting the Call Server" (p140)
  summary: |
    OMS=OXE 软件 + Suse OS 的虚机，等价一块 GD4 板卡的媒体处理：VoIP 编解码（G.711 20ms、G.729 20/40ms、G.722 20ms、OPUS 20ms，仅宽带与窄带）、编解码转码、会议（3/6/14/29 方）、静态与动态语音引导（动态可录制）、音调生成、DTMF RTP payload（RFC4733，旧称 RFC2833）、QoS 标签（802.1p/DiffServ）。容量：每 OMS 120 VoIP 通道，每 OXE 最多 240 台 OMS。许可两把锁：384=OMS 台数、385=全部 OMS 的 VoIP 通道（压缩器）总数，均可不停机安装（spadmin）。
  conditions: 会议方数与编解码清单为 Ed12 口径
  tags: [structure, oms, media-gateway, capacity]

- id: f18
  title: GAS 架构与部署模式对比图（ALE 平台/虚拟化/AS/GAS 四象限）
  type: diagram
  source_pages: p221-224
  source_chapter: GENERIC APPLIANCE SERVER / GAS - OXE DEPLOYMENT MODES / ARCHITECTURE
  source_quote: |
    "Generic Appliance Server (GAS) packaging provided by ALE • Operating system: Rocky Linux •
    Virtualized OXE on top of Rocky linux’s KVM layer • Optional WebRTC & OMS virtual machines •
    FlexLM license server directly installed on Rocky linux • Dongle-less package with license
    control based on the ALU-ID of the server or the OXE Cloud Connect ID" (p221)
    "OXE VM (Rocky) ... OMS VM (Rocky) ... WebRTC VM (Debian Linux) ... KVM (Virtualization package)
    Rocky Linux ... FlexLM server" (p224)
  summary: |
    OXE 四种部署形态：ALE 专有平台（CS-3/CPU8，长生命周期）；虚拟化（VMware/KVM/Hyper-V/Nutanix/AWS，硬件无关）；Appliance Server 平台（ALE 交付、预集成、短生命周期）；GAS（BP 按前置表自备硬件 + ALE 软件包：Rocky Linux+KVM 底座，承载 1 OXE VM（Rocky）、1 OMS VM（Rocky）、1 Rainbow WebRTC VM（Debian），FlexLM 直接装在宿主 OS；许可基于服务器 ALU-ID 或 Cloud Connect ID，无加密狗）。动机：OXE 对 Appliance Server 硬件变更高度敏感、合格平台寿命短（p221）。
  conditions: WebRTC 与 OMS VM 为可选组件；FlexLM 为必装（见 p225）
  tags: [diagram, gas, architecture, deployment-modes]

- id: f19
  title: GAS 许可控制两拓扑（ALU-ID 本地 vs CC-PRODUCT-ID 云端）
  type: diagram
  source_pages: p231-234
  source_chapter: GAS - LICENSES CONTROL TOPOLOGIES
  source_quote: |
    "The license control of each Call Server is based on • The local ALU-ID (if the OXE is not
    registered in Cloud Connect Infrastructure) ... Redundancy: each Call Server has its own ALU-ID" (p231)
    "The Cloud Connect Product ID (CC-PRODUCT ID) • The control is performed by CC/RTR service and
    the OXE CC agent • Redundancy: the CC-PRODUCT ID is common to both Call Servers" (p233)
  summary: |
    拓扑一（未注册 CC）：每台 GAS 内嵌 FlexLM 服务器，.ice 许可文件含服务器标识（dongle ID/MAC/ALUID）+ OXE 产品 ID；冗余时各 CS 有各自 ALU-ID。拓扑二（注册 CC）：按 CC-PRODUCT-ID（=CC-SUITE-ID+"-"+产品类型）经 CC/RTR 服务与 OXE CC agent 控制；冗余时两 CS 共用同一 CC-PRODUCT-ID。许可物件：.ice（FlexLM 侧）、.swk + hardware.mao（OXE 侧 spadmin 视图）。
  conditions: FlexLM 与 CCI/RTR 两种模式不可同时启用（p331 Warning）
  tags: [diagram, gas, flexlm, alu-id, cloud-connect]

- id: f20
  title: Cloud Connect 连接架构图——XMPP over WSS 443 常驻 + SOCKS5 80 按需
  type: diagram
  source_pages: p286-290, p340
  source_chapter: CLOUD CONNECT INFRASTRUCTURE / CONNECTION WITH THE CCI / SECURITY
  source_quote: |
    "XMPP Connectivity over WebSocket Secure (TCP port 443) ... The OXE establishes a permanent
    connection with the CCI (Cloud Connect Infrastructure) operated by the ALE" (p287-288)
    "Establish a temporary SOCKS5 Connection to CCO infra using to port 80/tcp ... The remote FQDN
    used by OXE agent is connect2.opentouch.com" (p290)
  summary: |
    架构：OXE 内嵌 CC Agent，经企业现有数据网络出站连 ALE 云。两条通道——常驻 XMPP over WebSocket Secure（TCP 443；XMPP 服务器衔接 OXE agent 与托管服务，承载 FTR/RTR 会话与 Inventory/Offer 的远程动作）；按需 SOCKS5（TCP 80，穿防火墙取 PBX 数据供 Inventory/Offer）。目标 FQDN 固定 connect2.opentouch.com；HTTP 代理可选。安全：OXE 主动发起双向连接、不改客户安全策略、TLS v1.2（ALE 自有 CA 签发的证书，OXE 信任库专用于 CC agent）、XMPP 按产品一ID一密。服务总览图（p340）另含 DOD 按需 HTTPS 与 CDN 软件仓库。
  conditions: 前提客户网络可达 Internet；DNS 解析 53/udp 必需
  tags: [diagram, cloud-connect, xmpp, socks5, architecture]

- id: f21
  title: FTR 原理时序——订单链 → CC-SUITE-ID 激活账户 → 永久凭证
  type: diagram
  source_pages: p291-295
  source_chapter: CLOUD CONNECT PRODUCT IDENTITY / FTR - OVERVIEW / PRINCIPLE
  source_quote: |
    "The syntax of the CC-SUITE-ID is: ADCBE-FGHIJ-KLMNO-PQRST • A 23-character string where A..T
    represent an hexadecimal digits ... The 20 hexadecimal digits are packed 5 by 5 and separated by
    “-”" (p291)
    "The main goal of the FTR (First Time Registration) is to allow the OXE to automatically retrieve
    the password corresponding to the CC-Product-ID" (p293)
  summary: |
    身份体系：CC-SUITE-ID 订货链生成、写在 .swk 许可文件里、产品终身不变（23 字符=20 个十六进制大写字符 5 个一组以"-"分隔）；CC-PRODUCT-ID=CC-SUITE-ID+"-"+产品类型。FTR 十步时序：下单 → 生成 CC-SUITE-ID 与激活账户/凭证 → 软件交付 BP → 安装 → .swk 含 SUITE-ID → OXE 以激活账户登录 CCI（步骤 8）→ 取回永久凭证（步骤 9，存盘）→ 建立常驻连接（步骤 10）；凭证备份需在 swinst 下保存 OXE 数据库。前置：DNS（+可选代理）在 netadmin 配置，CCTool 执行 FTR。
  conditions: 密码可变、ID 不变；FTR 需电话应用已启动（p328）
  tags: [diagram, ftr, cc-suite-id, ordering]

- id: f22
  title: FTR with PIN 恢复流程（helpdesk → 6 位 PIN → 重注册）
  type: flow
  source_pages: p298-301
  source_chapter: FIRST TIME REGISTRATION WITH PIN CODE
  source_quote: |
    "A new temporary activation account will be created with a 6 digits (0-9) PIN code and will be
    provided by helpdesk ... Validity period 5 days" (p299-300)
    "• FTR with pin code initialization ... • Other activation accounts deletion • Disconnect all
    products" (p300)
  summary: |
    触发：RTR Panic Flag（无效 FTR 数据如恢复过 CC 数据、欺诈检测即 Fleet Dashboard 出现 Duplicated、连接丢失）。流程：①系统管理员向 helpdesk 申请临时激活账户（核验系统归属/欺诈状态）→ helpdesk 建 6 位数字 PIN（有效期 5 天），删除其他激活账户并断开同 ID 全部产品；②安装员在 OXE 上用 CCTool 以"CC-SUITE-ID+PIN"重做 FTR；③系统以新凭证重连。OXE 侧细节：PIN 交 ccprocess 发起重注册但不落任何文件；操作完全重置 Cloud Connect 配置而系统保持在线；要求 RTR 与 ccagent 进程已启动。
  conditions: 仅在 panic 态使用；PIN 一次性且 5 天有效
  tags: [flow, ftr, pin, recovery]

- id: f23
  title: RTR 状态机——Qualifying Period 数轴与 Fleet Dashboard 六状态
  type: structure
  source_pages: p303-308
  source_chapter: RIGHT TO RUN (RTR)
  source_quote: |
    "A grace period of 30 days is initiated by default ... OK: the remaining Qualifying Period is
    increased of 0,5 day to the limit of 30 days • NOK: the remaining Qualifying Period is decreased
    of 1 day to the limit of 0 day" (p304)
    "Connected / Qualifying / Soon Blocked / Blocked-Panic ... Not connected / Duplicated" (p306-307)
  summary: |
    数轴：30 天资格期初始化；每日 RTR agent 经 XMPP 向 RTR 服务器请求，OK +0.5 天（上限 30）、NOK -1 天（下限 0）；归零触发 Panic Flag——话机显示 "Call your administrator"，数据库与电话服务拒绝配置变更。Fleet Dashboard 状态映射（剩余资格期）：Connected（24h 内有连接或 29-28 天）；Qualifying（超 24h 无连接且 27-10 天；到 27 与 20 天各发一次邮件）；Soon Blocked（9-1 天；每天邮件；事件计数增加）；Blocked-Panic（0 天；需 PIN 恢复）。另有 Not connected（未注册）与 Duplicated（CC Product ID 被另一系统占用——两系统同时扣减，覆盖 Soon Blocked 显示；PIN 生成会移除两侧记录，仅用 PIN 的真系统可重注册并恢复 30 天）。
  conditions: Save/Restore 保留资格期值跨重启；值同步到 twin CS（p308）
  tags: [structure, rtr, qualifying-period, fleet-dashboard, state-machine]

- id: f24
  title: Fleet Dashboard 服务全景与六缩写体系（FTR/RTR/DC/POD/DOD/SU）
  type: structure
  source_pages: p310, p338-348
  source_chapter: CLOUD CONNECT - FLEET DASHBOARD FEATURES
  source_quote: |
    "SERVICES GLOSSARY DC Data Collector DOD Data On-Demand FTR First Time Registration POD Push
    On-Demand RTR Right To Run SU Software Update" (p340)
    "Only one console can be opened at the same time • Console is disconnected after 1 minute of
    inactivity ... Each connection is logged by the Call Server (shell.log)" (p343)
  summary: |
    五个可开关服务（OXE 侧，FTR 必需、许可控制必需，新装机默认启用；OV8770 或 OXE WBM 控制）：Inventory（资产盘点：许可/订阅/终端/中继/板卡；终端含硬件参考/软件版本/MAC/IP 域，中继含 TLS 加密状态）；Get offer files（从运行中的 OXE 取实时 OPS 文件用于 Actis 报价）；Push offer（从 eBuy 拉许可 + offers server 拉 Actis offer 推到 OXE，经 POD/XMPP IBB；切换新文件归 BP）；Remote management（远程控制台：单会话、1 分钟无操作断开、需 OXE 凭证再认证、记 shell.log 并可经 OmniVista 8770 审计）；Software update（SPS 合同 + technical advanced 权限；给 AWS 仓库临时 URL 由 OXE HTTPS 下载；信任主机需含 cdn-oxe-sw-update.al-enterprise.com；切换版本仍归 BP，可用远程控制台安装）。另有告警展示（DC 每日取回）与推荐版本高亮（低于推荐版本橙色，每日计算）。动作状态字段：下载 D/-，安装 I(手动)/A(自动)/S(手动切分区)/-，升级请求 P/O/K/F/-（p348）。
  conditions: 远程管理与软件更新均要求有效 SPS 合同与 technical advanced 特权
  tags: [structure, fleet-dashboard, services, remote-management]

- id: f25
  title: CCTool 菜单结构与 CC 进程/日志布局
  type: menu-path
  source_pages: p312, p328-337
  source_chapter: CLOUD CONNECT - SERVICEABILITY / How-To Maintenance
  source_quote: |
    "1. FTR status & options 2. RTR status & options 3. Cloud Connect parameters 4. Set Log levels
    0. EXIT" (p328)
    "“CCAgent” process is in charge of XMPP secured channel. Logs are stored in “/var/log/ccagent.log”
    ... “CCProcess” process ... “ccprocess.log” (“/tmpd/cloud_cnx/log”) ... “CCAlarm.log” (“/tmpd”)" (p312)
  summary: |
    CCTool（mtcl）四项：①FTR status & options（状态 + 1 Perform FTR / 2 Perform FTR with PIN code；状态字段 CC-Suite-ID/FTR status Registered|Not registered/operation status Not performed|Success|Pending|Failure/Jid/Password/CC agent state XMPP_CONNECTED|DISCONNECTED）；②RTR status & options（Service state RTR_RUNNING/CCI mode/Remaining Qualifying Period/Last Success Time/Response Code/Cause Message/Next Request Date + 1 Force RTR）；③CC parameters（KeepAlive timer 默认 90s + Feature inventory/offer/remote console/pushOffer/swUpdate/swInstall 开关）；④Set Log levels（FTR/RTR/Data Collect/Remote Console/CC agent/Software Update 六特性 × ERROR/INFO/DEBUG(默认)/TRACE 四级 + verbose）。进程与日志：ccagent（XMPP 通道，service ccagent status/restart，/var/log/ccagent.log）；ccprocess（服务执行，dhs3_init -R CCPROCESS 重启，/tmpd/cloud_cnx/log/ccprocess.log，另有 ccprocesschild/ccservices/collect*/oxe_inventory_*/oxe_offer_files）；事件日记 /tmpd/CCAlarm.log。
  conditions: 进程 start/stop/restart 需 root；keep alive 改值经 MAO 且动态生效
  tags: [menu-path, cctool, logs, ccagent, ccprocess]

- id: f26
  title: OPEX/PoD 总体架构图——LMS/lmsagent 与周边系统
  type: diagram
  source_pages: p351-353
  source_chapter: OPEX / CAPEX VS OPEX / ARCHITECTURE / LICENSE MANAGER SERVER (LMS)
  source_quote: |
    "In OPEX subscription mode, licenses of elements in OXE system ... are managed through a License
    Manager Server in the cloud • This new feature is also called “Purple on Demand” (PoD)" (p351)
    "The “lmsagent” is a new component in OXE • Stateless component, used as technical bridge ...
    Run in all Call Servers : main, stand by, PCS • Read only access on Stand-by CS" (p353)
  summary: |
    架构：客户侧 OXE（LMS Agent + CCO Agent）+ OV8770/O2G/VAA/VNA 应用 ↔ Internet ↔ ALE 云（Service Manager、B2B eCommerce、LMS、ZUORA、SAP、eBuy、Fleet Dashboard、ALE Connect 基础设施、OPR）。OXE 必须注册 CCI；每次 FTR 会把 OXE 凭证发给 LMS 完成认证。lmsagent 是无状态 HTTPS 客户端（TLS 连 LMS 做许可更新/同步），为 OXE 管理与不连云的 ALE 应用当桥；跑在全部 CS（备机只读）；OmniPCX Record 直连 LMS。例外：OT-SBC 与 Selfcare 仍用本地许可文件；ALE Connect 用自有云。商务两侧：CAPEX 走 ACTIS 报价，OPEX（除硬件）走 MyPortal B2B eCommerce。
  conditions: 许可控件为 .swk（ELP 生成），ACTIS 不再用于 OPEX 报价（p354）
  tags: [diagram, opex, pod, lms, lmsagent]

- id: f27
  title: 三种订阅消耗类型图——Unitary / On activation / By threshold
  type: diagram
  source_pages: p367-369
  source_chapter: THREE TYPES OF SUBSCRIPTION CONSUMPTION
  source_quote: |
    "Unitary licenses • Softphone • API Telephony • VNA, VNA Broadcast ... Licenses on Activation
    (concerns ‘Voice Enterprise’ and ‘Room’ only) ... Licenses by Threshold / Reservation" (p367-369)
    "A threshold is managed at product level • Licenses are consumed when increasing the threshold,
    not when creating new instances" (p369)
  summary: |
    ①Unitary：实例创建即耗一许可（适用 Softphone、API Telephony、VNA、VNA Broadcast）；LMS 无余量则实例创建被拒。②On activation：仅 Voice Enterprise 与 Room——创建不耗、激活（OPEX Activation 参数）才耗；无余量时可停用另一用户腾许可；停用用户对 OXE 而言退出服务但保留配置（适合酒店/ BP 更替等波动业务）。③By threshold：OXE 侧维护阈值，加阈值才向 LMS 要许可——适用 Attendant Console（4059 话务台上限）、Voice Agent（ACD 操作员上限）、API Recording Cnx（DR-Link 录音上限）、VAA（VAA 侧声明端口数）、OPR 三档（OPR 服务器侧声明）；阈值在 WBM 新增 Opex Licences 菜单维护。
  conditions: 消耗类型的适用清单为 Ed12 口径
  tags: [diagram, opex, consumption, licensing]

- id: f28
  title: OXE-LMS 同步决策流程图（4 小时对账 → panic 判定树）
  type: flow
  source_pages: p371-373
  source_chapter: OXE SYNCHRONIZATION WITH LMS / CONSUMPTION AT OXE STARTUP
  source_quote: |
    "OXE checks every 4 hours that licenses are synchronized ... If can't update the LMS licenses
    because the max of licenses is reached, the OXE switches in panic mode ... The incident 652 is
    sent • If we can't do the synchronization because the LMS is unreachable an incident 654 is sent" (p371)
    "The OXE starts, without restriction, with the consumption values that were stored in its database
    before the reboot. However, it is not possible to perform a management action requiring a license
    request to LMS" (p373)
  summary: |
    运行期：每 4 小时对账——消耗视图一致则无事；不一致则更新 LMS；LMS 满员更新失败→panic+事件 652；LMS 不可达→事件 654，连续 30 天不可达→panic+652；panic 后同步恢复→自动解除 panic。启动期：OXE 向 LMS 要消耗视图作为启动阈值——一致则正常启动；OXE 需启动实例数>LMS 消耗值→请求新许可，LMS 有则给并更新消耗值；LMS 无应答→仍以本地数据库旧消耗值启动，但一切需要向 LMS 要许可的管理动作（建用户、开 OPEX activation）被拒。
  conditions: 强制同步入口 spadmin 选项 10（p398）
  tags: [flow, lms, synchronization, panic]

- id: f29
  title: C2P 转换五步流程与范围边界
  type: flow
  source_pages: p376-378
  source_chapter: COMMUNICATIONS SUITE FOR MLE TO PURPLE ON DEMAND TRANSFORMATION
  source_quote: |
    "Preparation ... Checks ... Export to eCommerce portal • Generate ACTIS output JSON file • Import
    it in MyPortal (C2P webpage) ... Quantities adjustment ... Shopping Cart creation ... Transformation
    is definitive once ordered" (p376)
    "Each PoD subscription has a C2P counterpart (discounted commercial item) with a dedicated part
    number ... PoD subscriptions: part number in 3EYxxxxxAA C2P subscriptions: part number in 3EYxxxxxMA" (p377)
  summary: |
    五步：①Preparation（升到支持的最新版本；不允许 add-on；移除不兼容应用；硬件兼容性核查）→ ②Checks（C2P 资格校验，报错回 ACTIS 修）→ ③Export（生成 ACTIS 输出 JSON，导入 MyPortal C2P 网页）→ ④Quantities adjustment（按客户实际需求调数量）→ ⑤Shopping cart（标准 PoD 下单流程；下单即定局）。范围：凡 PoD 目录产品均可 C2P，但 OPR、ALE Connect、Selfcare、VNA、API Management 除外；Dispatch Console/SoftPanel/OTFC/IQ Messenger 与停产件（OTMS/OTMC/OTBE/OV4760/ICS）及 IP Premium Security 须先移除。C2P 件号 3EYxxxxxMA（PoD 为 3EYxxxxxAA），同服务不同价；OT-SBC 例外只需 C2P 维护订阅；转换范围外的 add-on 走常规 PoD 无折扣。产品版本基线（p378）：OXE Purple R100.1+、OV8770 R5.1+、OTCC SE R10.4+、OT-SBC R7.4+、OPR R2.5.0.7+、O2G R2.5+、VNA R2.2.1+、VAA R4.4+、Selfcare R1.13+、UMC；Rainbow 暂经 Rainbow 门户订购。
  conditions: C2P 优惠价以"既有系统能力"为上限；转换程序适用于任何 release/硬件/特性的 OXE
  tags: [flow, c2p, transformation, myportal]

- id: f30
  title: MyPortal PoD 许可下载路径与项目状态判据
  type: menu-path
  source_pages: p381-385
  source_chapter: Download POD license files from MyPortal (How-To)
  source_quote: |
    "/Installed Base/ Asset & service manager/ In top bar, select Asset & service manager from
    Installed base menu ... In the list, select Explore Purple Assets and click on Search" (p383)
    "To be able to download and implement the POD license files, the Project status must be seen
    Active" (p384)
  summary: |
    路径：登录 https://myportal.al-enterprise.com（无凭证找 BP 客户经理/ALE 代表申请）→ 顶栏 Installed Base → Asset & service manager → Explore Purple Assets → Search → 左侧列表选客户项目 → 对每个产品（示例 OXE/8770/VAA）点 CPU ID 图标下载 PoD 许可文件（OXE 为 .swk）→ 保存后由技术员装入各应用。判据：项目状态必须 Active 才能下载与实施；显示 Pending 表示项目未激活（交付问题等）。无凭证或项目异常时的升级路径：BP/ALE 代表。
  conditions: 需 MyPortal 账号；项目含一个终端客户
  tags: [menu-path, myportal, pod, license-download]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-20）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | RLAB 环境与节点访问 | 有 | f02 | POD 拓扑 + 五类节点访问表 |
| task-02 | 部署 SOT VM 并初始化 | 有 | f03, f05, f06 | 模式矩阵、Web 分区、媒体库（部署步骤细节在 case c01/c09） |
| task-03 | 更新 SOT | 有 | f07 | zip+MD5 与版本命名规则 |
| task-04 | 启用 Template Factory | 有 | f03, f04 | 两配置定位 + 降级模式五步 |
| task-05 | 传输媒体并配置项目 | 有 | f06, f05 | 媒体三库/格式/账号 + Easy/Expert 分区 |
| task-06 | 单版本全加载 | 有 | f08, f09 | 加载时序图 + 启动相位链 |
| task-07 | 多版本与切换 | 有 | f10, f11, f12 | 分区结构、两分支流程、swinst 菜单树 |
| task-08 | 补丁安装 | 有 | f13, f12 | 双场景操作流 + swinst 附录菜单 |
| task-09 | 分发器模式加载 | 有 | f14, f12 | /tmpd→Rload 流程与清理 + 9-10 菜单 |
| task-10 | 虚拟化平台与许可决策 | 有 | f15 | 平台×版本矩阵与许可双路径 |
| task-11 | OXE VM 生成与加载 | 有 | f15, f16 | OXE-V 拓扑组（步骤在 case c06/c10） |
| task-12 | OMS 加载与声明 | 有 | f17 | OMS 定位/容量/许可锁（步骤在 case c07/c11） |
| task-13 | GAS 加载 | 有 | f18 | GAS 架构与四形态对比（步骤在 case c12） |
| task-14 | GAS 后安装向导 | 有 | f19 | 许可两拓扑（向导字段在 case c13） |
| task-15 | GAS 运维 | 有 | f19, f18 | FlexLM/ALU-ID 布局（命令细节在 principle/case） |
| task-16 | DNS/代理与云连通性 | 有 | f20 | 连接架构图（netadmin 步骤在 case c14） |
| task-17 | FTR 执行与 PIN 恢复 | 有 | f21, f22 | 身份体系时序 + PIN 恢复流程（CCTool 步骤在 case c15） |
| task-18 | RTR 启用与监控 | 有 | f23, f25 | 资格期状态机 + CCTool 菜单 |
| task-19 | PoD 许可下载 | 有 | f30 | MyPortal 路径与 Active 判据 |
| task-20 | PoD 配置与 LMS 同步 | 有 | f26, f27, f28, f29 | OPEX 架构、消耗类型、同步决策树、C2P 流程 |

补充说明：
- f01（全书主线）、f24（Fleet Dashboard 服务全景）、f13（补丁双场景）为跨任务的结构底座，不单独对应某一 task。
- 全部 20 项 task 均有框架类条目覆盖，无空缺；逐键操作序列保留在 case.md，数值口径保留在 principle.md。
- 生产化边界提示（来自 BOOK_OVERVIEW 批判节）：虚拟化设计对照 TBE043；GAS 部署对照 TC3138 与 TBE063/TBE067；OXE 安装手册 8AL91032ENBD；AWS 部署对照 TC3142en-Ed01；N3 以下迁移对照 TC3104en-Ed08。
