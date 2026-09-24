# 反例/限制/边界/易错点候选 — OmniPCX Enterprise Loading (ENTPXTE402EN Ed12)

> 提取器: counter-example-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23

```yaml
- id: n01
  title: SOT 一次只允许一个部署任务；虚机规格另查 Delivery note
  type: limitation
  source_pages: p22
  source_chapter: S.O.T. – INTRODUCTION
  source_quote: |
    "Notes: Only one deployment at a time For more details concerning virtual machines sizing,
    consult the S.O.T . «Delivery note » document"
  summary: |
    SOT 同一时刻只能跑一个部署任务，且虚机尺寸规格不在本教材，而在《Delivery note》文档。
    并行交付多个目标机时必须排队，或为每个现场起独立 SOT 实例。
  conditions: 所有 SOT 部署场景
  tags: [limitation, sot]

- id: n02
  title: default 转 Template Factory 必须先关机并满足前置；检查自动但缺失项要靠命令暴露
  type: limitation
  source_pages: p28
  source_chapter: « TEMPLATE FACTORY» CONFIGURATION
  source_quote: |
    "Moving from default configuration to template factory configuration • Shutdown the S.O.T . VM and
    make sure that the pre-requisites of the template factory configuration are met. ... If it’s not
    the case, by launching the “templateFactory” command on the console, the missing pre-requisites
    will be displayed."
  summary: |
    从 default 切到 Template Factory：先关机、确认 8CPU/16GB/500GB 第二盘/Vmx/USB 控制器全部就位；
    SOT 启动时自动检查并在控制台打印启用行，缺项时须手动跑 templateFactory 命令才能看到缺什么。
    "模板功能没出现"先跑命令看缺失清单，别反复重启。
  conditions: SOT 配置切换
  tags: [limitation, sot, template-factory]

- id: n03
  title: 降级模式不再控制硬件前置——浏览器首页有警告横幅，构建时长强依赖机器
  type: warning
  source_pages: p29, p156, p164
  source_chapter: «TEMPLATE FACTORY» CONFIGURATION IN DEGRADED MODE / How-To
  source_quote: |
    "is to bypass hardware requirements so that you can build OVAs on any server or laptop... with
    fewer constraints. • Hardware requirements are no longer controlled. • Regardless, a specific
    warning is visible on the browser's homepage. • The time spent to build the OVA depends strongly
    on the machine (RAM, number of proc/core)."
  summary: |
    降级模式是"官方支持的绕过"：硬件前置全部不再受控，任何笔记本都能构建 OVA，但 SOT 首页会一直
    显示警告横幅；OVA 构建时长强烈依赖 RAM/核数，低配机器可能非常久。向客户/团队说明时别把降级
    模式当故障，也别承诺固定构建时长。
  conditions: 低资源机器启用 Template Factory 时
  tags: [warning, sot, degraded-mode]

- id: n04
  title: SOT 更新仅限同主版本；跨主版本（如 3.1→3.2）必须重装 ISO
  type: limitation
  source_pages: p35, p47, p197
  source_chapter: SOT UPDATE
  source_quote: |
    "This functionality will only be offered for S.O.T solutions in the same major version. The update
    will be forbidden for version not in the same major version. ... A major version is named A.B
    (e.g. 3.2.002.000): update process will not be possible in this case (like changing from 3.1 to 3.2)"
  summary: |
    SOT 的 zip+MD5 更新只能在同一主版本（A.B）内做；跨主版本更新被禁止，只能重新部署新 ISO。
    升级 SOT 前先确认目标版本主版本号是否一致，别拿 zip 硬更。
  conditions: SOT 升级
  tags: [limitation, sot, update]

- id: n05
  title: SOT 首连强制改密并设口令短语——漏设口令短语会失去"忘记密码"自助通道
  type: warning
  source_pages: p44-45, p195
  source_chapter: First access to the SOT VM web interface
  source_quote: |
    "Modification of the password and creation of the passphrase is mandatory during the 1st
    connection ... the user must select a passphrase with an associated answer, in order to be able to
    use the “forgot password” functionality. It allows you the reinitialize the password in ever you
    forget it."
  summary: |
    SOT Web 首连（admin/letacla）强制改复杂密码（≥8 字符四类各一）并设置口令短语问题与答案；口令短语
    是密码遗忘后的唯一自助重置途径。部署完随手把口令短语答案记入团队密码库，否则忘密只能重装。
  conditions: SOT 部署初始化
  tags: [warning, sot, security]

- id: n06
  title: SOT 网卡数与声明 IP 数必须一致；加网卡必须重启虚机
  type: warning
  source_pages: p46, p196
  source_chapter: Network settings（standalone 与 hosted 两处相同 Warning）
  source_quote: |
    "THE NUMBER OF NETWORK INTERFACES (NETWORK CARDS) ASSIGNED TO THE SOT VIRTUAL MACHINE AND THE
    NUMBER OF IP ADDRESSES DECLARED IN THE SOT WEB PAGE MUST BE COHERENT ... BY DEFAULT, ONLY ONE
    NETWORK INTERFACE IS PRESENT. THE OTHERS NETWORK INTERFACE WILL BE PRESENT ONCE CREATED IN THE
    SOT VIRTUAL MACHINE. ADDING A NETWORK INTERFACE REQUIRES A RESTART OF SOT VIRTUAL MACHINE."
  summary: |
    默认只有 1 个网卡；多子网安装/更新场景加卡后必须重启 SOT，且 Web 页声明的 IP 数要与虚机网卡数
    对得上。改完 IP/网卡后"连不上"先核对这两条，再查网络。
  conditions: SOT 多子网配置
  tags: [warning, sot, network]

- id: n07
  title: 空盘才自动 Standard Installation；已装系统的目标机必须 grubboot ETHER 或 BIOS 强制网络引导
  type: limitation
  source_pages: p57, p89
  source_chapter: BOOT ON ETHERNET / Boot the Call Server on Ethernet
  source_quote: |
    "There are two cases: • The CS hard disk is empty • Automatic start up in «Standard Installation »
    mode for CS, CPU8, and Appliance Server • The CPU disk is already loaded • Manual starting up on
    all CPUs to force automatic start up • Access via the Bios menu • Or hard disk invalidation
    (“grubboot ETHER”)" (p57)
    "Command grubboot ETHER System will ask your confirmation. Disk have to be reinstalled after
    reboot." (p89)
  summary: |
    只有空盘才会自动进安装；盘上已有内容的机器必须手动强制网络引导（BIOS 菜单或 root 执行
    grubboot ETHER，后者会提示"重启后磁盘将被重装"并需确认）。"配好项目后 SOT 一直等目标机"的
    高频原因就是目标机没走网络引导。
  conditions: CS/CPU8/AS 加载
  tags: [limitation, loading, grubboot]

- id: n08
  title: 加载后两件事容易漏：角色寻址要按需配置；许可没在项目里声明就得手工恢复
  type: warning
  source_pages: p63, p92, p211
  source_chapter: MAIN INSTALLATION STEPS / 加载后 Notes
  source_quote: |
    "WARNING: Configure the role addressing if needed! License are automatically deployed if declared
    in the S.O.T project If not, restore the license files manually" (p63)
    "Operations to perform after loading: ­ Restore the software licenses manually (if the license
    upload was not configured in the S.O.T. project) ­ If required, configure the role addressing for
    the CS (hostname will be “csm” and address will be “192.168.1.103”)" (p92)
  summary: |
    SOT 项目不负责两件事：角色寻址（csm 主用地址等，需按需在 netadmin 配）与许可（项目里没传 OPS
    文件就得事后手工恢复到 /usr4/BACKUP/OPS 再 swinst 恢复）。加载"completed"只是软件就位，系统
    还不能算交付完成——后置清单（键盘/密码/国家码/日期时间/板卡上线/建用户或恢复备份）要逐项过。
  conditions: 所有加载场景完成后
  tags: [warning, loading, licensing, post-install]

- id: n09
  title: 静态补丁在 active 分区必须停话音且自动重启；动态补丁必须排在静态之后
  type: warning
  source_pages: p65, p104-105
  source_chapter: PATCH LOADING / How-To Warnings
  source_quote: |
    "STATIC PATCH INSTALLATION ON ACTIVE PARTITION REQUIRES TO STOP THE TELEPHONE APPLICATION. SO,
    SYSTEM IS REBOOTED AUTOMATICALLY ... FOR A SAME VERSION, DYNAMIC PATCHES HAVE TO BE INSTALLED
    AFTER STATIC PATCHES" (p104)
    "THE STATIC PATCH (« N4.205.36») MUST BE INSTALLED BEFORE THE DYNAMIC PATCH (E.G. : « N4.205.36.A »)" (p105)
  summary: |
    两条维护窗口规则：active 分区装静态补丁=系统自动重启（话音中断，必须排窗口）；同版本内动态补丁
    只能装在静态之后（版本或静态缺失时动态装不上）。给客户报维护窗口按"静态=停机、动态=热装"口径。
  conditions: active 分区补丁安装
  tags: [warning, patch, maintenance-window]

- id: n10
  title: 补丁文件形态差异：zip 一包一补丁（静动分开两次装），iso 可静+动一次装
  type: limitation
  source_pages: p102, p123
  source_chapter: Declare the Media / Easy installation Notes
  source_quote: |
    "If the format is a zip, usually only one patch per zip, it can be a static or dynamic patch. In
    this case, if both must be installed, a static patch and a dynamic patch, two loading operations
    are necessary. In the case of an iso file, it is possible to have in the same iso a static patch
    and a dynamic patch. It is then possible to load the 2 in a single operation."
  summary: |
    zip 通常一个补丁一个文件，静态+动态要装两次；iso 可以把静态+动态打包一次装。收补丁包时先看
    形态再排操作次数，别按"一个包=一次加载"默认。
  conditions: 补丁媒体准备
  tags: [limitation, patch, media]

- id: n11
  title: 版本切换期间板卡可能已拿新二进制——回退老版本可能要重新下载
  type: warning
  source_pages: p72
  source_chapter: MULTI VERSIONS LOADING - PRINCIPLE
  source_quote: |
    "Remark: • During the switch, boards can receive new binaries from new release • If you decide to
    go back with the initial release, another downloading will be done if necessary"
  summary: |
    切到新分区后板卡可能已经接收了新版本的二进制；决定回退老版本时，板卡可能需要再下载一轮——
    回退不是零成本瞬时操作，排回退预案时要留下载窗口。
  conditions: 多版本切换与回退
  tags: [warning, multi-version, rollback]

- id: n12
  title: N3 以下迁移硬约束：必须重格式化、80GB 盘/1GB RAM 门槛、多版本机制整体不可用
  type: limitation
  source_pages: p78
  source_chapter: WARNING INSTALLATION/MIGRATION FROM N3
  source_quote: |
    "Coming from ANY version < N3, the Call Server MUST be reformatted ... Disk size is at minimum of
    80GB • RAM size is at minimum 1GB ... No possibility to use the multi version loading • N3 or
    higher release cannot co-exist with older releases (< n3) in active/in-active partitions and
    switchover is not possible • Refer to TC3104en-Ed08_Migration_guide_to_OXE_R101.x"
  summary: |
    任何 <N3 版本升级到 R101.x：CS 必须重格式化（数据先备份）、盘 ≥80GB、RAM ≥1GB、/root 与
    /root2_d ≥3.5GB（CIS 新分区）；只能完整加载，且 N3+ 与 <N3 不能共存双分区、不能切换——
    多版本"装了再切"的安全网在这一类机器上不存在。按 TC3104en-Ed08 迁移指南执行。
  conditions: 存量旧版本机器升级
  tags: [limitation, migration, version-trap]

- id: n13
  title: 密码 aging=0 触发 CIS 基准警告（对 root 不建议）；实验习惯勿带进生产
  type: warning
  source_pages: p91, p175, p273
  source_chapter: 加载后密码设置（三处一致输出）
  source_quote: |
    "How many days do you want to keep validate passwords <10<X<366, 0 for no aging) ? 0 WARNING !
    Deactivation of password aging is not recommended for root user as per CIS_Benchmark_Req.No_5.6.1.1"
  summary: |
    aging 提问答 0 即关闭密码有效期，系统每次都打印 CIS_Benchmark_Req.No_5.6.1.1 警告（不建议对
    root 关闭）。培训口径一律 0 仅为课堂省事；生产交付应保留 aging 或至少对 root 保留，并把
    Superuser2580* 之类实验密码全部替换。
  conditions: 加载后账户初始化
  tags: [warning, security, lab]

- id: n14
  title: 分发器模式下全版本与静态补丁强制装 inactive 分区
  type: limitation
  source_pages: p113, p123
  source_chapter: EASY INSTALLATION OF OXE
  source_quote: |
    "In case of full software version or static patch, the installation must be performed on OXE
    inactive partition • For a dynamic patch, the choice is offered: active or inactive partition"
  summary: |
    走 swinst 9-10"本地分发器加载"时，完整版本与静态补丁只能进 inactive 分区（即必须先复制数据再
    切换才生效）；只有动态补丁可选 active/inactive。想"直接把新版本怼在 active 上"在这条路径里
    做不到。
  conditions: Easy Installation 场景
  tags: [limitation, distributor, patch]

- id: n15
  title: 动态补丁装完不算完——必须用 downstat d/i/t 检查板卡与话机下载
  type: warning
  source_pages: p127
  source_chapter: Load a dynamic patch（安装输出 Warning）
  source_quote: |
    "WARNING ------- To complete dynamic patch installation, please use the following commands: "downstat
    d" : to obtain boards which need a download "downstat i" : to obtain IP phones which need a download
    "downstat t" : to obtain 40x9 phones which need a download See "downstat" usage given by "downstat ?""
  summary: |
    动态补丁安装器结束时会打印该警告：补丁落地≠终端生效，要用 downstat d（板卡）/i（IP 话机）/
    t（40x9 话机）找出还需要下载的对象并跟完。跳过这步会出现"系统版本上去了、部分话机行为没变"
    的假完成。
  conditions: 动态补丁安装后
  tags: [warning, patch, downstat]

- id: n16
  title: 分发器清理的两个半误区：Rload 解包物不自动删、要手动 9-7 清理；/tmpd 源文件反而自动删
  type: warning
  source_pages: p129-130
  source_chapter: Easy installation / Maintenance
  source_quote: |
    "At the end of the loading procedure, these files are not deleted from the Call Server hard drive.
    So, if you want to purge these files, to not saturate the CS hard drive, a dedicated option is
    available in “swinst” menu ... BE AWARE THAT THIS “CLEANING OPERATION” ... REMOVES ONLY THE
    EXTRACTED FILES (FROM ISO & ZIP) STORED IN “/USR4/FTP/RLOAD” DIRECTORY. THE SOURCES FILES (ISO/ZIP)
    THEMSELVES THAT HAVE BEEN TRANSFERRED MANUALLY IN “/TMPD” DIRECTORY ... ARE AUTOMATICCALY DELETED
    AT THE END OF INSTALLATION OPERATION."
  summary: |
    方向别搞反：解包物（/usr4/ftp/Rload/{version,patch,dynpatch}）不会自动删除，会累积吃满硬盘，
    要用 swinst 9-7 Cleaning operation 清；而手工传进 /tmpd 的 iso/zip 源文件在安装结束时会自动删。
    清理操作也只清 Rload，不清别处。
  conditions: 每次分发器加载后
  tags: [warning, distributor, disk, cleanup]

- id: n17
  title: Hyper-V/Nutanix/AWS 上无 FlexLM+加密狗路径——Cloud Connect 许可是唯一选择
  type: limitation
  source_pages: p136
  source_chapter: Licences control mechanism according to the used virtualization technology
  source_quote: |
    "Hyper-V , Nutanix and AWS don’t provide a native way to redirect an USB dongle from the host to a
    given Virtual Machine • No FlexLM server delivery neither as an Hyper-V , Nutanix or AWS Virtual
    Machine • Cloud Connect is the mandatory license control process in case an OXE is virtualized
    over Hyper-V , Nutanix or AWS technology"
  summary: |
    许可路径由虚拟化平台锁死：Hyper-V/Nutanix/AWS 既不能把 USB 加密狗重定向给虚机，ALE 也不交付
    这三个平台上的 FlexLM 服务器虚机——只能走 Cloud Connect。售前在客户定了 Hyper-V/AWS 后还报
    "FlexLM+加密狗"方案就是方案错误。
  conditions: 虚拟化选型
  tags: [limitation, licensing, oxe-v, matrix]

- id: n18
  title: Hyper-V 虚机代次有讲究：CS 用 gen1，OXE-MS/OST64/EEGW 用 gen2
  type: version-trap
  source_pages: p134
  source_chapter: Virtualization technologies 脚注 (2)
  source_quote: |
    "(2): A generation 1 Virtual Machine has to be created for the Call Server, whereas a generation 2
    Virtual Machine has to be created for OXE-MS, OST64 and EEGW."
  summary: |
    Hyper-V 上呼叫服务器虚机必须建第 1 代，OXE-MS/OST64/EEGW 必须建第 2 代——代次建反虚机起不来。
    另注：Nutanix AHV 属定制 KVM，需专项认证（脚注 3）；平台兼容细节以 TBE043 为准。
  conditions: Hyper-V 部署
  tags: [version-trap, hyper-v, oxe-v]

- id: n19
  title: 内嵌 WebRTC 网关 50 并发封顶——7000 用户以上必须外部网关；GAS 禁装第二台 OMS
  type: limitation
  source_pages: p225-226
  source_chapter: DESIGN RULES / HARDWARE PRE-REQUISITES
  source_quote: |
    "The gateway is restricted to a maximum of 50 simultaneous calls (Above 7,000 users, an external
    WebRTC gateway is required) ... For performance reason, installing a second OXE-MS on the GAS is
    forbidden ... (**) Above 7,000 users, an external WebRTC gateway is required (the one embedded in
    the GAS is limited to 50 simultaneous conversations)"
  summary: |
    GAS 内嵌 Rainbow WebRTC 网关上限 50 并发通话，用户超 7000 就要外置网关；OMS 每 GAS 限 1 台且
    禁装第二台。容量方案按"50 并发/7000 用户"两条线预判，别等上线拥塞再补外置网关（参照 TBE067）。
  conditions: GAS 容量设计
  tags: [limitation, gas, capacity, webrtc]

- id: n20
  title: GAS 只认硬件 RAID；HP DL20 G11 只能跑 GAS 包；新旧 Appliance Server 混搭冗余被禁
  type: limitation
  source_pages: p226-229
  source_chapter: HARDWARE PRE-REQUISITES / APPLIANCE SERVER SHIPPED BY ALE / HISTORY / REDUNDANCY
  source_quote: |
    "Caution: only hardware RAID may be used with a GAS system ­ software RAID is not supported" (p226)
    "This platform have been qualified only with Generic Appliance Server (GAS) software package • Use
    of the classical OXE software package on this platform is not supported" (p227)
    "Both platforms must have similar hardware characteristics in case of redundancy • Mix of Appliance
    Server and Generic Appliance Server not allowed for a redundant OXE" (p229)
  summary: |
    三条硬件红线：GAS 只支持硬件 RAID（软件 RAID 不支持）；HP DL20 G11 仅限 GAS 软件包（经典 OXE 包
    不支持，许可限 ALU-ID 或 CC-SUITE-ID）；冗余双机硬件要相似且禁止 Appliance Server 与 GAS 混搭。
    采购与冗余设计前先对这三条。
  conditions: GAS 硬件选型与冗余
  tags: [limitation, gas, hardware, raid]

- id: n21
  title: 经典 OXE 软件包全面退场：存量 legacy 必须迁 GAS 或虚拟化；GAS 型项目无升级路径
  type: version-trap
  source_pages: p228, p230
  source_chapter: HISTORY OF APPLIANCE SERVERS / SOFTWARE UPGRADE
  source_quote: |
    "Only the Generic Appliance Server software package is available • Existing OXEs with legacy mode
    have to switch to GAS or virtualization • The use of the classical OXE software package is
    therefore no longer supported whatever the physical server" (p228)
    "Via SOT , with an "OXE" type project (Classic procedure) • No upgrade possible today for a "GAS"
    type project" (p230)
  summary: |
    两个版本演进点：(1) 经典 OXE 软件包在所有物理服务器上都不再支持，存量 legacy 只能迁 GAS 或
    虚拟化；(2) GAS 的 OXE 升级要用 OXE 型项目（经典流程），GAS 型项目目前没有升级路径——别建
    GAS 型项目来做版本升级。GAS host 的 Rocky 升级另有 bootDVD/gas-rocky-update.sh 通道。
  conditions: 存量迁移与升级规划
  tags: [version-trap, gas, migration, upgrade]

- id: n22
  title: GAS 安装期间网关 IP 必须可达；没配 DNS 时可用 GAS 自身 IP 顶替
  type: limitation
  source_pages: p235
  source_chapter: GAS - IP CONNECTIVITY
  source_quote: |
    "The IP address of the default gateway (this IP MUST be accessible during installation) • The IP
    address of the DNS server (the GAS IP address may be used if the customer doesn’t want to configure
    a DNS server)"
  summary: |
    安装期硬前提：默认网关 IP 必须可达（装到一半网关不通会卡死）；DNS 服务器没有时可以拿 GAS 自己的
    IP 顶替。开局前把这两个值跟客户网络负责人确认死。
  conditions: GAS 加载
  tags: [limitation, gas, network]

- id: n23
  title: GAS host 升级会先优雅关停全部 VM 再重启 Rocky——升级窗口=全系统停机
  type: warning
  source_pages: p237
  source_chapter: LINUX PATCH UPGRADE SUPPORT FOR GAS (HOST)
  source_quote: |
    "The virtual machines (OXE, OMS and WebRTCGW) will be gracefully shutdown before the patch update
    and the Rocky Linux is rebooted afterwards"
  summary: |
    对 GAS 宿主做 bootDVD/Rocky 补丁升级时，OXE/OMS/WebRTC 三个 VM 会先被优雅关机，Rocky 升级后
    重启——这是一次全系统停机窗口，必须按停机维护排期并提前通知客户，不能当热补丁做。
  conditions: GAS host OS 升级
  tags: [warning, gas, upgrade, downtime]

- id: n24
  title: GAS 上 root 不能直接 SSH 登录；标准 FTP 被禁用（安全）
  type: limitation
  source_pages: p262, p280
  source_chapter: Post-Installation Wizard
  source_quote: |
    "Log on with admin account ... Direct root login is no more possible" (p262)
    "For security reasons, the standard "FTP" protocol cannot be used on the GAS server. Transfer the
    license files using the "SFTP" (Secure FTP) protocol, or "SCP" ... use the "login/password" of
    admin account. Transfer it to /tmp and then move it to the final directory with the mv command with
    the root account." (p280)
  summary: |
    两条安全基线：SSH 直登 root 已禁用（先 admin 登录再提权）；GAS 禁用标准 FTP——传许可等文件走
    SFTP/SCP，且以 admin 传到 /tmp 后用 root mv 到目标目录。老脚本里 root@直接 SSH/FTP 传文件的
    做法在 GAS 上都会失败。
  conditions: GAS 运维与文件传输
  tags: [limitation, gas, security]

- id: n25
  title: 信任主机 CSV 的旅程：SOT 项目导入后落 /opt/config/trust/import_th.csv，iptables 建好后移到 /tmpd
  type: limitation
  source_pages: p265-266
  source_chapter: Post-installation wizard / OXE parameters
  source_quote: |
    "Import-Trusted Host: File define in SOT project for OXE trusted hosts is copied under
    /opt/config/trust by default and renamed import_th.csv ... After successful building of iptables
    rules in OXE, the CSV file will be moved to /tmpd path with name import_th_bkp.csv"
  summary: |
    SOT 项目里选的信任主机 csv 在 GAS 上有固定旅程：/opt/config/trust/import_th.csv → OXE 的
    iptables 规则成功生成后被改名为 /tmpd/import_th_bkp.csv。排障"信任主机没生效"时按这条路径查
    文件在哪个环节丢了；SOT 项目没填的话要在向导里手工指定路径。
  conditions: GAS 后安装
  tags: [limitation, gas, trusted-hosts]

- id: n26
  title: 后安装向导里的 RAINBOW_PBXID 只是示例值——正式值必须来自 Rainbow 云平台
  type: warning
  source_pages: p267-268
  source_chapter: “Rainbow WebRTC Gateway” virtual machine
  source_quote: |
    "PBXID: Enter the "PBX ID" (here, you can enter the ID given as example) ... Note: The
    RAINBOW_PBXID given here is an example. Normally, it is an unique ID linked to the OXE and
    retrieved from Rainbow Cloud platform."
  summary: |
    向导里 WebRTC GW 的 RAINBOW_PBXID 字段教材只让填"示例 ID"，原书明确注明正常流程要用 Rainbow
    云平台为该 OXE 生成的唯一 PBX ID。照抄示例值上线会导致网关连错租户——正式交付前必须换成真实
    PBXID。PBX_DOMAIN 取值也随冗余形态变（单机=物理 IP；本地冗余=Main IP；空间冗余=节点名且需 DNS 委托）。
  conditions: GAS 后安装 WebRTC GW 段
  tags: [warning, gas, rainbow, pbxid]

- id: n27
  title: FlexLM 配置改动后 OXE 呼叫服务器必须重启
  type: warning
  source_pages: p282
  source_chapter: OXE configuration for the FlexLM
  source_quote: |
    "FlexLM Licensing Enabled Yes Flex Server IP Address ... Flex Server port 27000 Product ID
    discovery Yes ... Warning OXE CALL SERVER MUST BE RESTARTED!"
  summary: |
    在 OXE 侧改完 FlexLM 许可配置（启用/服务器 IP/端口/发现开关）后必须重启呼叫服务器才生效。
    改完"许可还是不认"先确认重启过没有；同时注意 FlexLM 与 CCI/RTR 两种模式不可并存（n37）。
  conditions: FlexLM 许可路径配置
  tags: [warning, flexlm, licensing]

- id: n28
  title: 自动 FTR 每 4 小时才试一次——事件 6214 循环出现时手动 CCTool 立即重试
  type: limitation
  source_pages: p296
  source_chapter: FIRST TIME REGISTRATION (FTR) – NEW INSTALL
  source_quote: |
    "Registration attempt every 4 hours till a successful automatic FTR (or a successful manual FTR
    via CCTool) • An incident (6214) is issued at each unsuccessful attempt • Cleared by incident 6207
    in case of successful connection to CCO"
  summary: |
    新装机自动 FTR 的重试周期是 4 小时，每次失败发 6214、成功由 6207 清除。开局等自动重试会白白拖
    半天——网络一通就手动 CCTool 立即做 FTR。另注：已有 CC 密码的存量 OXE 不做自动 FTR；升级到
    R101.0 MD3+ 时云服务启停状态保持不变。
  conditions: FTR 执行与排障
  tags: [limitation, ftr, incidents]

- id: n29
  title: 备机严禁做 FTR；凭证经克隆自动同步；PCS 上不跑云服务
  type: warning
  source_pages: p297, p329
  source_chapter: OXE REDUNDANCY AND PASSIVE CALL SERVER / How-To Warning
  source_quote: |
    "Never perform a First Time Registration (FTR) on a stand-by Call Server ... The final credentials
    received from CCI are automatically synchronized with the TWIN Stand-by CS ... Cloud Services DO
    NOT run on Passive Communication Server (PCS)" (p297)
    "Warning THERE IS NO NEED TO PERFORM “FTR” ON STANDBY CPU." (p329)
  summary: |
    冗余场景 FTR 只在主机做：取回的永久凭证存在 OXE 数据库并自动克隆到 twin，切换后备机转主即恢复
    链接；PCS（OXE-V 拓扑）上不跑任何云服务。在备机上手动 FTR 是多余且有风险的操作，两处原文都
    单独标了警告。
  conditions: OXE 冗余 / OXE-V PCS 拓扑
  tags: [warning, ftr, redundancy]

- id: n30
  title: FTR with PIN 的四个边界：PIN 不落盘、操作在线重置全部云配置、要求 RTR+ccagent 进程活着、5 天有效
  type: warning
  source_pages: p299-300, p330
  source_chapter: FIRST TIME REGISTRATION WITH PIN CODE
  source_quote: |
    "The PIN code will be transmitted to the “ccprocess” process to restart the FTR procedure, but
    won’t be saved in any file. Performing this operation will completely reset the Cloud Connect
    configuration and settings while the system is still in service. The "FTR with PIN code" can only
    be performed with the "RTR" and "ccagent" processes started."
  summary: |
    PIN 恢复是把双刃剑：PIN 只传给 ccprocess、不落任何文件；操作会在系统在线状态下完全重置 Cloud
    Connect 配置；若 RTR 或 ccagent 进程没在跑则 FTR 根本不执行；helpdesk 给的 PIN 有效期仅 5 天。
    申请 PIN 前先确认两个进程状态，拿到 PIN 5 天内用掉。
  conditions: RTR panic 恢复
  tags: [warning, ftr, pin, recovery]

- id: n31
  title: Duplicated 状态两侧同时扣天数——PIN 生成会移除两侧记录，只有用 PIN 的系统活下来
  type: warning
  source_pages: p307
  source_chapter: Status displayed on Fleet Dashboard (2/2)
  source_quote: |
    "The CC Product ID is already in use by another system, which either means a wrong use of this
    credential or a real hacking ... Both OXE Systems with the same CC Product ID will decrease their
    remaning Qualifying Period simultaneously • FTR with PIN code is required to recover the
    connectivity on the real customer system • Pin code generation will remove both recording on RTR
    server • Only the customer system using the PIN Code will be authenticated ... New RTR registration
    will be authorized only for this system to restore the Qualifying Period to 30 days"
  summary: |
    同一 CC Product ID 出现在两台系统（配置复制错误或真实入侵）时，Fleet Dashboard 显示 Duplicated
    且两台同时扣减资格期——不处理会双双进 panic。恢复走 PIN：helpdesk 生成 PIN 时会移除 RTR 服务器上
    两条记录，只有用 PIN 完成重注册的系统恢复 30 天资格期。克隆虚机/复制磁盘前先想清楚 CC 身份
    会被一起复制。
  conditions: Fleet Dashboard 告警处置 / 克隆部署
  tags: [warning, rtr, duplicated, fraud]

- id: n32
  title: spadmin 里 Suite Id 有三个阅读规则：永不在首位、带 CCSID: 前缀、主备共用一个；RTR=No 时干脆不显示
  type: limitation
  source_pages: p327
  source_chapter: CC-suite ID display Notes
  source_quote: |
    "CC-Suite-ID will never be the first one in the file (to not impact Flex configurations for which
    first one is used) In order for OXE to differentiate CCSID from CPU-Id, CC-Suite-ID is prefixed
    with “CCSID:” There is only one CC_SUITE_ID for both main and standby CPU. ... When the parameter
    “Cloud Connect RTR Enabled” is equal to “No” ... the “Suite Id” parameter is not displayed in the
    “spadmin” command."
  summary: |
    在 spadmin 输出里找 Suite Id 的三条规则：它永远不会是文件第一个 ID（避免影响 Flex 配置的用法）；
    显示时带 "CCSID:" 前缀与普通 CPU-Id 区分；主备 CPU 共用同一个 CC-SUITE-ID。而且 RTR 未启用时
    Suite Id 行根本不显示——"spadmin 里找不到 Suite Id"先查 RTR 开关，再怀疑许可文件。
  conditions: FTR 前置核对
  tags: [limitation, spadmin, cc-suite-id]

- id: n33
  title: FTR 失败的排障入口固定两处：ccprocess.log 与 CCTool 状态页
  type: limitation
  source_pages: p329
  source_chapter: First Time Registration Tips
  source_quote: |
    "Tips If FTR fails, access the” ccprocess.log” file stored in the directory: “/tmpd/Cloud_cnx/logs”
    and verify the connectivity state using “CCTool” command (FTR status & Options)"
  summary: |
    FTR 失败的官方排障起点只有两个：/tmpd/Cloud_cnx/logs 下的 ccprocess.log + CCTool 的 FTR status
    & options。先分清"连不上（6205/6209）"还是"注册被拒（6214）"，再回头查 DNS/代理/443/80（c14）
    或许可文件（swk 无 CCSID，n55）。
  conditions: FTR 排障
  tags: [limitation, ftr, troubleshooting]

- id: n34
  title: 虚机上 FlexLM 与 CCI/RTR 不能同时启用；改 RTR 参数需重启
  type: warning
  source_pages: p331
  source_chapter: Right To Run – Configuration
  source_quote: |
    "Tips A reboot is required Warning FOR COMMUNICATION SERVERS RUNNING ON VIRTUAL MACHINES, VERIFY
    THAT LICENSING VIA FLEXLM SERVER IS NOT ACTIVATED. THE TWO LICENSING MODES (FLEXLM SERVER AND
    CCI/RTR) CANNOT RUN AT THE SAME TIME"
  summary: |
    启用 RTR 前必须核对虚机上 FlexLM Licensing Enabled=No——两种许可模式互斥；改 RTR 参数后需要重启
    呼叫服务器。虚机交付时"许可模式二选一"要在设计阶段定死，后期切换=一次重启窗口。
  conditions: RTR 启用
  tags: [warning, rtr, flexlm, licensing]

- id: n35
  title: RTR 重试口径教材内部不一致：4 小时窗口/10 分钟间隔 vs 当天不再重试次日扣 1 天
  type: version-trap
  source_pages: p304, p308, p332
  source_chapter: RTR QUALIFYING PERIOD / MISCELLANEOUS / RTR status Notes
  source_quote: |
    "OXE will retry the Right To Run check up for four hours with interval of ten minutes ... If the
    connection is not restored at end of the fourth hour • OXE will decrement the qualifying period by
    one." (p308)
    "If a problem occurs when RTR request is sent, no retry is performed until next daily request and
    one day is decreased from remaining qualifying period." (p332)
  summary: |
    同一本书两处对"RTR 请求失败后怎么扣天数"给出了不同口径：讲义页说 4 小时窗口内每 10 分钟重试、
    4 小时后才扣 1 天；How-To Notes 说当天不再重试、（出问题时）扣 1 天等次日。监控告警与客户沟通
    按保守口径（当日即可能扣减）设计，最终行为以 ALE 最新 TC 为准——这是教材内部矛盾记录，不作
    统一裁决。
  conditions: RTR 监控设计
  tags: [version-trap, rtr, discrepancy]

- id: n36
  title: KeepAlive 默认 90 秒——会掐空闲 HTTPS 会话的防火墙环境必须调参
  type: limitation
  source_pages: p311, p333
  source_chapter: CLOUD CONNECT – KEEP ALIVE
  source_quote: |
    "Adapt to networks that close automatically HTTPS sessions without traffic for a given period •
    The value of CC connection keep alive will now be managed through MAO • If its value is changed
    (default= 90 sec), it is taken in account dynamically by the “cc-agent process”"
  summary: |
    CC 连接的 KeepAlive 默认 90 秒；客户防火墙若按空闲时长掐 HTTPS 会话，XMPP 常驻链路会被反复掐断
    （表现为 6204/6207 反复交替）。在 MAO/WBM 调大 KeepAlive，cc-agent 动态生效无需重启；CCTool 3
    可核对当前值。
  conditions: 客户防火墙严格的环境
  tags: [limitation, cloud-connect, keepalive, firewall]

- id: n37
  title: 远程控制台三约束：单会话、1 分钟无操作断开、每次登录入 shell.log 审计
  type: limitation
  source_pages: p343-344
  source_chapter: FLEET DASHBOARD - REMOTE MANAGEMENT
  source_quote: |
    "Only one console can be opened at the same time • Console is disconnected after 1 minute of
    inactivity ... Each connection is logged by the Call Server (shell.log) • Logged data: Fleet
    Dashboard account username and company • Can be viewed from OmniVista 8770 audit application"
  summary: |
    Fleet Dashboard 远程控制台同一时间只允许一个会话、1 分钟无操作自动断开、每次连接都由 CS 记入
    shell.log（账号名+公司名，可经 OmniVista 8770 审计）。用它做长脚本维护时注意空闲断连，且操作
    全程可被审计——别在远程控制台里做不该留痕的事。
  conditions: 远程维护
  tags: [limitation, fleet-dashboard, remote-console, audit]

- id: n38
  title: 软件更新只管传输——切换新版本仍是 BP 责任；信任主机必须放行 cdn-oxe-sw-update 域名
  type: limitation
  source_pages: p347-348
  source_chapter: FLEET DASHBOARD – SOFTWARE UPDATE
  source_quote: |
    "Provide to the OXE a temporary URL for the AWS repository • Request the concerned OXE to download
    the version (HTTPS) • Rely on the official ISO files ... • If OXE trusted hosts are used: “cdn-oxe-
    sw-update.al-enterprise.com” domain must be part of them • Transfer only: switch on the new version
    remains under BP’s responsibility • BP may use the remote console to install the version"
  summary: |
    Fleet Dashboard 软件更新只完成"把官方 ISO 下到 OXE"，分区切换仍要 BP 自己做（可用远程控制台）；
    使用信任主机的站点必须把 cdn-oxe-sw-update.al-enterprise.com 加进白名单，否则下载直接失败。
    状态字段里 F=OXE 侧禁用了软件更新，先查 OXE 侧开关。
  conditions: 云端软件更新
  tags: [limitation, fleet-dashboard, software-update, trusted-hosts]

- id: n39
  title: lmsagent 跑在全部 CS（备机只读）——与"云服务不跑备机/PCS"是两回事
  type: misconception
  source_pages: p353, p297, p308
  source_chapter: LICENSE MANAGER SERVER (LMS) / FTR redundancy / RTR misc
  source_quote: |
    "Run in all Call Servers : main, stand by, PCS • Read only access on Stand-by CS" (p353)
    "Cloud Services DO NOT run on Passive Communication Server (PCS)" (p297)
  summary: |
    两个"跑在哪"别混：CC 云服务（FTR/RTR 等）明确不跑在备机与 PCS 上；但 OPEX 的 lmsagent 恰恰要跑
    在全部 CS（主/备/PCS），备机上只是只读。排 OPEX 许可问题时看备机 lmsagent 状态是合理的，排
    FTR/RTR 问题时去主机。
  conditions: OPEX/Cloud Connect 冗余排障
  tags: [misconception, lmsagent, redundancy]

- id: n40
  title: OPEX 打开即"旧 CAPEX 锁全部失效"——唯 lock 87/165 例外仍随版本
  type: version-trap
  source_pages: p354, p389
  source_chapter: OXE LICENSE FILE / spadmin Display active file
  source_quote: |
    "A new lock, 431: 1 means new OPEX mode (0 for CAPEX mode) • Previous CAPEX locks are no more taken
    in account • Except lock Beta tests 87 and lock Release 165"
  summary: |
    .swk 里 lock 431=1 打开 OPEX 模式后，既有 CAPEX 锁（用户数/话务台等）一律不再计数，只有 87（Beta
    tests）与 165（Release）两个版本类锁例外。从 CAPEX 转 OPEX 时按 24 项订阅重新对容量，别按旧
    CAPEX 锁值理解系统容量。
  conditions: C2P/CAPEX→OPEX 转换
  tags: [version-trap, opex, lock-431]

- id: n41
  title: OPEX 模式下 CAPEX 显示的 OPEX activation 旗标"显示但不生效"
  type: warning
  source_pages: p399
  source_chapter: Items controlled in OXE – Users
  source_quote: |
    "Warning IN CAPEX MODE THIS NEW FLAG IS DISPLAYED BUT NOT TAKEN IN ACCOUNT"
  summary: |
    OPEX activation 旗标在 CAPEX 模式的管理界面里也会显示，但完全不起作用。在 CAPEX 系统上看到
    该旗标别得出"这个系统在按云许可计费"的结论；判断系统模式以 lock 431 / spadmin 的 OPEX Flag 为准。
  conditions: 混合环境巡检
  tags: [warning, opex, capex, misconception-adjacent]

- id: n42
  title: PoD 不含 ISDN/模拟中继；Crystal 硬件仅限 C2P 前已在系统；CPU8 只能走 eBuy
  type: limitation
  source_pages: p358-359
  source_chapter: OXE HARDWARE / ENDPOINTS HIGH-LEVEL PERIMETER / CAPEX HARDWARE ITEMS
  source_quote: |
    "PoD doesn’t include ISDN / analog trunk groups" (p358)
    "Crystal Hardware and other boards can be present in an OmniPCX Enterprise Purple system, in a PoD
    context, only if present on the system before the C2P transformation program Added for older CPU
    replacement in a C2P context" (p358)
    "CPU8 board Removed from MLE catalog, orderable only via eBuy" (p359)
  summary: |
    PoD 硬件边界三条：不含 ISDN/模拟中继组（纯 IP/SIP/软件话音）；Crystal 硬件（MR1/MR3/CS-3/GD4/GA4/
    SLI16/UAI16/UAI8）只有 C2P 转换前就在系统上的才能保留（C2P 场景换老 CPU 可加）；CPU8 板卡已从
    MLE 目录移除、只能经 eBuy 订购。售前配置单先按这三条过滤。
  conditions: PoD 报价与 C2P 评估
  tags: [limitation, pod, hardware, isdn]

- id: n43
  title: OV8770 订阅的四个缩水点：30 客户端、5 万管理用户、不能管 CAPEX OXE、不能管 OXO/OpenTouch
  type: limitation
  source_pages: p363
  source_chapter: OPEX SOFTWARE LICENSES – Management
  source_quote: |
    "Compared to CAPEX OV8770: 30 OV8770 clients, no possibility to go above 50,000 managed users, no
    possibility to manage an OXE in CAPEX mode, an OXO or an OpenTouch"
  summary: |
    OPEX 的 OV8770 订阅与 CAPEX 版不等价：最多 30 个 OV8770 客户端、管理用户上限 5 万、不能管理处于
    CAPEX 模式的 OXE、也不能管 OXO 或 OpenTouch。多 PBX 混合（OXE+OXO）或超大站点客户选 PoD 时
    OV8770 这条要单独立项评估。
  conditions: PoD 管理平台选型
  tags: [limitation, opex, ov8770]

- id: n44
  title: VNA 的 911 用量要按并发呼叫配 SIP 中继；VAA/VNA 尚无原生负载均衡高可用
  type: limitation
  source_pages: p364
  source_chapter: OPEX SOFTWARE LICENSES – Attendant & Notification Alerting
  source_quote: |
    ""911/urgency call" usage: SIP trunks are required to support the number of 911 simultaneous calls
    ... For both subscriptions: ... Native high-availability (load balancing) not yet available (will
    be included in a further step)"
  summary: |
    VNA 的紧急呼叫（911）并发量由 SIP 中继容量承载，订阅不自动扩中继；VAA 与 VNA 目前没有原生
    （负载均衡型）高可用，后续版本才补。涉及告警/广播类生命安全场景的高可用承诺要谨慎写进方案。
  conditions: PoD 通知告警类订阅
  tags: [limitation, vna, vaa, ha]

- id: n45
  title: ALE Connect Agent/Channel 是 Voice Agent 的选项；No PRS in PoD
  type: limitation
  source_pages: p362, p365
  source_chapter: OPEX SOFTWARE LICENSES – Openness / Contact Center
  source_quote: |
    "They are options of the Voice Agent license" (p365)
    "No PRS in PoD offer" (p362)
  summary: |
    PoD 范围两条：ALE Connect 的 Agent（用户型）与 Channel（端口型）两个订阅是 Voice Agent 许可的
    选项，不独立成体系；PoD 不提供 PRS。呼入语音之外的渠道（多媒体交互）按 Channel 计数，报价时
    与 Voice Agent 绑定核算。
  conditions: PoD 呼叫中心/开放能力报价
  tags: [limitation, opex, ale-connect, prs]

- id: n46
  title: Unitary 许可无余量时实例创建直接被拒；On activation 靠"停用别人腾许可"
  type: limitation
  source_pages: p367-368
  source_chapter: THREE TYPES OF SUBSCRIPTION CONSUMPTION
  source_quote: |
    "If there are no more licenses available in the LMS, the instance creation is refused" (p367)
    "If the LMS has no license available anymore, it is possible to de-activate another user in order
    to activate this user • A user de-activated (i.e. with OPEX activation flag disabled) is out of
    service from an OXE standpoint" (p368)
  summary: |
    两种"许可不够"的行为：Unitary 类（Softphone/API Telephony/VNA 等）创建实例时直接被拒；Voice
    Enterprise/Room 走 On activation，可在 LMS 无余量时停用另一个用户腾出许可，但被停用用户立即
    退出服务。波动业务（酒店/共享工位）靠"停用-保留配置"周转，但要预期停用即不可用的用户体验。
  conditions: PoD 日常运营
  tags: [limitation, opex, consumption]

- id: n47
  title: LMS 不可达时的冻结规则：建用户不建设备、激活留 disabled、删除照删同步延后
  type: limitation
  source_pages: p370
  source_chapter: OXE SYNCHRONIZATION WITH LMS – Synchronization rules
  source_quote: |
    "If the LMS is unreachable • When creating a user with the flag enabled, the corresponding device
    is NOT created • When activating an already existing device, the flag remains disabled in the OXE
    • When deleting a user with the flag enabled, the user is deleted and the LMS will be updated at
    the next synchronization • When de-activating an already existing device, the flag is disabled in
    the OXE and the LMS will be updated at the next synchronization"
  summary: |
    LMS 失联期间 OXE 的行为很克制但容易误判：建用户（带 flag）时设备根本不会创建；激活既有设备时
    flag 留在 disabled；删除/停用则本地先执行、LMS 恢复后补同步。"LMS 断了还能不能开户"的答案是
    不能（带许可的开户），但删除不受影响。
  conditions: OPEX 运维 / LMS 故障窗口
  tags: [limitation, lms, synchronization]

- id: n48
  title: OXE 启动不依赖 LMS——按本地旧消耗值起，但一切要许可的管理动作被拒
  type: limitation
  source_pages: p373
  source_chapter: CONSUMPTION AT OXE STARTUP
  source_quote: |
    "The OXE starts, without restriction, with the consumption values that were stored in its database
    before the reboot. However, it is not possible to perform a management action requiring a license
    request to LMS (user creation, enabling OPEX activation flag on an existing user, …)"
  summary: |
    LMS 完全无应答时 OXE 仍会照常重启并以重启前数据库里的消耗值起业务——通话不受影响；但任何需要向
    LMS 要许可的管理动作（建用户、给既有用户开 OPEX activation 等）都被拒。"重启能解决吗"的答案：
    话务能保住，扩容不行。
  conditions: LMS 中断窗口
  tags: [limitation, lms, startup]

- id: n49
  title: OPEX panic 时间线两档：超订 15 天温和处置/45 天全面降级；LMS 失联 30 天直接按 45 天档
  type: limitation
  source_pages: p374
  source_chapter: OXE PANIC MODE
  source_quote: |
    "After 15 days ... If Voice Enterprise excess, random de-activation of OPEX activation parameter
    for users & attendants in idle ... After 45 days ... OPEX activation parameter is de-activated for
    all users and attendants • Attendant licenses are setup to 0 • Nothing is done for Softphone excess
    • Case 2 : Connection failure with LMS for more than 30 days • After 15 days, same behavior as
    case 1’s “after 45 days” step"
  summary: |
    超订不处理：15 天后开始随机停用空闲用户的 OPEX activation、下调话务台上限、拒 CC 新登录与 DR-Link
    新录音（Softphone 超订始终不自动处置）；45 天后全部用户/话务员停用、话务台许可清零。LMS 失联超
    30 天则 15 天后直接执行最狠档。"随机停用"意味着受影响用户不可预测——收到 654 事件要按剩余天数
    倒排修复窗口。
  conditions: OPEX panic 处置
  tags: [limitation, opex, panic, timeline]

- id: n50
  title: 各应用的 LMS 失联代价不同：8770 每夜校验、VAA 午夜、O2G 12h、OPR 24h；30 天宽限后各自失效
  type: limitation
  source_pages: p375
  source_chapter: OTHER APPLICATIONS
  source_quote: |
    "30-days grace period, during which services (OmniVista 8770, VAA, VNA, O2G opened sessions, OPR …)
    stay operational • qualifying mode during grace period for O2G: no new session permitted • On the
    grace period expiry: • OXEs systems are de-activated on the OmniVista 8770 ... • VAA or VNA
    licensing service is stopped ... • O2G goes in panic mode : APIs are no longer accessible • OPR
    goes in inactive state: call recording is no longer possible"
  summary: |
    LMS 失联的宽限是统一的 30 天，但期满后果按产品不同：8770 上的 OXE 被停用（配置/设备管理/告警全
    停）；VAA/VNA 许可服务停止（应用失效）；O2G 进 panic（API 不可访问）；OPR 转 inactive（录音与
    管理界面不可用）。宽限期内 O2G 已不允许新会话——别把 30 天当成"完全无影响期"。校验周期也各不同
    （8770 每夜/VAA 午夜/O2G 12 小时/OPR 启动后 24 小时）。
  conditions: PoD 全家桶运维
  tags: [limitation, lms, applications, grace-period]

- id: n51
  title: C2P 下单即定局；转换期间不允许 add-on；转换外 add-on 走常规 PoD 无折扣
  type: warning
  source_pages: p376-377
  source_chapter: COMMUNICATIONS SUITE FOR MLE TO PURPLE ON DEMAND TRANSFORMATION
  source_quote: |
    "Shopping Cart creation • Standard PoD ordering process • Transformation is definitive once
    ordered" (p376)
    "Any add-on on the perimeter to be transformed has to be managed directly in MyPortal B2B eCommerce
    portal • Such add-on will be based on regular PoD commercial items, without any specific
    transformation discount." (p377)
  summary: |
    C2P 两点商务纪律：转换订单一旦下单不可逆（数量调整必须在下单前完成）；准备阶段不允许 add-on，
    转换范围外的扩容要走 MyPortal 常规 PoD 件号、享受不到转换折扣。报价与下单时序要在项目计划里
    钉死，别边转换边加东西。
  conditions: C2P 项目
  tags: [warning, c2p, ordering]

- id: n52
  title: OT-SBC 的 C2P 例外：只需 C2P 维护订阅，无 C2P setup 订阅
  type: limitation
  source_pages: p377
  source_chapter: C2P commercial items
  source_quote: |
    "OT-SBC exception : only the C2P maintenance subscription is required in this transformation (i.e.
    no C2P setup subscription)"
  summary: |
    C2P 订阅映射的一个例外：OT-SBC 转换只买 C2P 维护订阅（件号 3EYxxxxxMA 家族），不存在 C2P setup
    订阅。给 OT-SBC 客户做转换报价时别按"每个 PoD 订阅都有 C2P 对应件"的通则套出一份 setup 报价。
  conditions: OT-SBC 转换
  tags: [limitation, c2p, sbc]

- id: n53
  title: MyPortal PoD 许可下载的前提是项目状态 Active——Pending 意味着交付侧有问题
  type: limitation
  source_pages: p384-385
  source_chapter: Download POD license files from MyPortal
  source_quote: |
    "To be able to download and implement the POD license files, the Project status must be seen
    Active ... If the project is shown as pending, this means that the project has not yet been
    activated (Delivery problems, etc.)."
  summary: |
    Asset & service manager 里项目必须显示 Active 才能下载 PoD 许可文件；显示 Pending 说明项目尚未
    激活（交付问题等）——技术员拿到的是"还没生效的订单"，先推动商务/交付链路激活项目，别在
    MyPortal 上反复重试下载。
  conditions: PoD 交付起点
  tags: [limitation, myportal, pod]

- id: n54
  title: swk 必须同时含 CCSID 与 LOCK 431=1，且装完必须重启 OXE
  type: warning
  source_pages: p388
  source_chapter: Purple On Demand – Prerequisites
  source_quote: |
    "Warning CORRECT “SWK” FILE IS MANDATORY, WITH: ­ CCSID (CLOUD CONNECT SUITE ID) ­ LOCK 431: OPEX
    MODE SET TO “1” ... After licenses installation, make sure that an OXE reboot has been performed."
  summary: |
    OPEX 开通的三件套检查：swk 含 CCSID、swk 的 lock 431=1、装完许可后确实重启过 OXE。任一不满足，
    spadmin 里就看不到 OPEX Flag=1，后续 FTR/LMS 全链条都不会工作。"装了许可但系统还是 CAPEX 行为"
    按这三条顺序排查。
  conditions: OPEX 开通
  tags: [warning, opex, swk, licensing]

- id: n55
  title: NTP 未配置会威胁整个云许可链——系统时间必须正确（swinst 配置）
  type: warning
  source_pages: p394
  source_chapter: Purple On Demand – NTP management
  source_quote: |
    "Warning SYSTEM DATE/TIME HAS TO BE CORRECT, SO NTP SERVER DECLARATION IS REQUIRED (SWINST)"
  summary: |
    PoD 前置清单里的硬警告：系统日期时间必须正确，因此必须在 swinst 声明 NTP 服务器。时间漂移会
    影响证书校验与云侧认证（FTR/RTR/LMS 都依赖 TLS）。新装机"云全链路失败"时把 NTP/时区列入首批
    排查项。
  conditions: OPEX/FTR 前置
  tags: [warning, ntp, opex]

- id: n56
  title: spadmin 计数器读法与 panic 判据：lms/oxe 两列消耗必须一致，否则 panic
  type: limitation
  source_pages: p397, p400, p402, p404
  source_chapter: Purple On Demand – LMS licenses 计数器解读
  source_quote: |
    "Voice Enterprise “15 | 0/0 | 18” 15 is the number max of new licenses “Users” that can be
    requested to the LMS service (in the whole network) The first “0” is the total number of licenses
    consumed for the node on the LMS service The second “0” is the total number of licenses consumed
    on the node 18 is the maximum number of licenses subscribed for the whole network The values
    displayed in # consumed lms/oxe column must be identical (for example: 20/20). If it is not the
    case, the PBX goes in panic mode"
  summary: |
    spadmin 11 的四列读法：全网还可新申请 | 本节点 LMS 侧消耗 / 本节点 OXE 侧消耗 | 全网订阅上限；
    中间两列必须相等，不相等即触发 panic。注意原文 p404 的 Voice Agent(CCD) 示例排版有误（值
    "13 | 2/2 | 18" 下方的解释文字误用了 5/5/25，应为本节点消耗列示例的复制粘贴错误）——判据本身
    以"lms/oxe 一致"为准，示例数值不必照抄。
  conditions: PoD 对账与排障
  tags: [limitation, spadmin, lms, editorial-error]

- id: n57
  title: OPEX 模式收窄了两个自由度：ACD 不再区分 CCD/RSI、DR-Link 不再区分 IP/TDM
  type: limitation
  source_pages: p405
  source_chapter: ACD operator / DR-Link recording
  source_quote: |
    "Due to this new ACD Operator Log-On procedure in this new OPEX mode, it is no more possible to:
    • Authorize CCD Log-On and forbid RSI Log-on and vice versa • Make a difference between the max
    value of logged CCD Operator and logged RSI Operator ... it is no more possible to: ­ Authorize IP
    DR-Link Recording and forbid TDM DR-Link Recording and vice versa ­ Make a difference between the
    max value of IP DR-Link Recording, local TDM DR-Link Recording and remote TDM DR-Link Recording"
  summary: |
    从 CAPEX 迁到 OPEX 会丢两类精细化控制：ACD 登录不能只放行 CCD 或只放行 RSI、也不能分别设上限
   （合并为 max ACD Operators 一个阈值）；DR-Link 录音不能只放行 IP 或 TDM、也不能分别设上限（合并
    为一个阈值）。有这类策略诉求的客户迁移前要确认可接受。
  conditions: CAPEX→OPEX 迁移评估
  tags: [limitation, opex, acd, dr-link]

- id: n58
  title: OPEX activation=No 的终端会有两种"许可拒绝"表现：NOE 屏显 No license available；SIP 收 402 Payment required
  type: limitation
  source_pages: p407-408
  source_chapter: NOE set registration / SIP device registration
  source_quote: |
    "“No license available” message is displayed on the screen" (p407)
    "OXE response during registration of the SIP set of a user which has its new flag to “no” : ­ SIP
    message “402 Payment required” display ­ Minor SIP alarm 5816 generation ... Logs available in
    “/tmpd/sipalarm.log” file: [CKA_MotorRegistrar::onRegister] OPEX Mode - Register of SIP user xxxx
    rejected - Licence required" (p408)
  summary: |
    无许可（OPEX activation=No 且 LMS 无余量）时的现场表现：NOE 话机注册后屏幕显示 "No license
    available"（eqstat 可见 License availability: NO、Terminal OUT OF SERVICE）；SIP 话机注册收到
    402 Payment required，伴随事件 5816 与 /tmpd/sipalarm.log 的 "Register ... rejected - Licence
    required"。用户报"话机注册不上/显示无许可"先查许可链，再查话机本身。
  conditions: OPEX 日常排障
  tags: [limitation, opex, troubleshooting, sip]

- id: n59
  title: 网络要求、虚拟化细节、GAS 安装、OXE 业务配置全部外置——本书是"加载+云连接"教材
  type: out-of-scope
  source_pages: p134, p149, p228, p242, p92, p176
  source_chapter: 各章 Documentation 指针
  source_quote: |
    "For more details, consult the TBE043 document (Virtualization Design Guide) available on My Portal" (p134)
    "TBE063 - OmniPCX Enterprise & Generic Appliance Server ... TC3138 Installation of a GAS server on
    Rocky Linux" (p228, p242)
    "Perform basic management such as user creation… Or restore a backup" (p92)
  summary: |
    本书的边界即外部文档清单：虚拟化设计（TBE043）、OXE 安装手册（8AL91032ENBD）、AWS 部署
    （TC3142en-Ed01）、GAS 与 OXE 关系（TBE063）、GAS 安装（TC3138）、Rainbow WebRTC 网关（TBE067）、
    SOT 版本兼容（TC2456）、N3 迁移（TC3104en-Ed08）、GAS 迁移（TC0000_GAS_migration）；OXE 业务
    配置（用户/路由/编号计划）整体指向 Starter 课程。生产交付每个阶段都要带上对应文档，教材本身
    不承担展开。
  conditions: 全部生产化场景
  tags: [out-of-scope, documentation]
```

## 收尾自检 — 对照 BOOK_OVERVIEW.md 20 项任务清单

| task | 任务 | 边界类条目覆盖 |
|---|---|---|
| task-01 | RLAB 环境 | 实验口径警示分散于各条 conditions（仅培训环境，n13/n59 关联） |
| task-02 | 部署 SOT VM | 有 → n05（首连口令短语）、n06（网卡一致性） |
| task-03 | 更新 SOT | 有 → n04（同主版本限制） |
| task-04 | Template Factory | 有 → n02（关机+前置）、n03（降级模式警告） |
| task-05 | 媒体与项目 | 有 → n01（单部署任务） |
| task-06 | 单版本加载 | 有 → n07（网络引导前提）、n08（角色寻址/许可后置）、n13（aging CIS 警告） |
| task-07 | 多版本与切换 | 有 → n11（回退需再下载）、n12（N3 以下禁多版本） |
| task-08 | 补丁安装 | 有 → n09（静/动窗口）、n10（zip/iso 形态）、n15（downstat） |
| task-09 | 分发器模式 | 有 → n14（强制 inactive）、n16（Rload 清理误区） |
| task-10 | 虚拟化平台决策 | 有 → n17（许可路径锁死）、n18（Hyper-V 代次） |
| task-11 | OXE VM 加载 | 有 → n18、n59（文档外置） |
| task-12 | OMS 加载 | 有 → n19 关联（OMS 每 GAS 限 1 台） |
| task-13 | GAS 加载 | 有 → n20（RAID/平台）、n22（网关可达） |
| task-14 | GAS 后安装 | 有 → n24（root/FTP）、n25（CSV 旅程）、n26（示例 PBXID） |
| task-15 | GAS 运维 | 有 → n21（GAS 型项目无升级）、n23（host 升级停机）、n27（FlexLM 重启） |
| task-16 | 云连通性 | 有 → n36（KeepAlive 90s）、n55（NTP） |
| task-17 | FTR 与 PIN | 有 → n28（4h 重试）、n29（备机禁做）、n30（PIN 边界）、n32（Suite Id 阅读）、n33（排障入口） |
| task-18 | RTR 监控 | 有 → n31（Duplicated）、n34（FlexLM 互斥）、n35（重试口径矛盾） |
| task-19 | PoD 许可下载 | 有 → n53（Active 判据） |
| task-20 | PoD 配置与同步 | 有 → n39（lmsagent 范围）、n40（锁失效）、n41（CAPEX 旗标）、n42-n52（目录/项目/消耗边界）、n54（swk 三件套）、n56（计数器判据）、n57（能力收窄）、n58（许可拒绝表现） |

**20/20 全部有边界类条目覆盖，无空缺。**

### 扫描完整性说明（Warning/Note/Tips 标记框逐页核对）

- 已全部入册的 Warning 框：p46/p196（网卡一致性）、p63（角色寻址/许可）、p78（N3 迁移）、p91/175/273（CIS aging）、p104/p105（静/动补丁）、p106（Duplicate all 失败回退）、p127（downstat）、p129-130（清理范围）、p199（vSphere ≤6.0）、p226（软件 RAID）、p237（host 升级关 VM）、p282（FlexLM 重启）、p297/p329（备机禁 FTR）、p331（FlexLM 互斥）、p354/388（lock 431）、p390（Cloud Connect 必须配置，并入 n54 链条）、p394（NTP）、p396（LMS 项目须先建，并入 c17 前提）、p399（CAPEX 旗标不生效）、p267（示例 PBXID）。
- 已入册的 Note/Important/Tips：p22（单部署）、p28（转换关机）、p29（降级警告横幅）、p57（空盘判定）、p72（切换二进制）、p92/176/211（加载后清单）、p102（zip/iso）、p113（inactive 强制）、p134 脚注（gen1/gen2、AHV 认证）、p136（许可矩阵）、p147（PCS 行为，入 framework f16）、p228/230（legacy 迁移、GAS 项目无升级）、p235（网关可达）、p262/280（root/FTP）、p265-266（import_th.csv）、p269（许可三选项）、p296（4h/6214/6207）、p299-300/330（PIN）、p306-308（状态与重试）、p311（KeepAlive）、p313/334（事件表，入 principle p24）、p317（DNS/代理用途、127.0.0.1 占位，入 c14）、p326（swk 改名 Tips，入 c15 步骤 1）、p327（Suite Id 规则）、p332（重试口径）、p341-348（Dashboard 规则，n37/n38）、p353（lmsagent）、p355（项目规则）、p357-366（目录边界）、p367-370（消耗与失联规则）、p371-375（同步/panic/应用）、p376-377（C2P）、p384（Active）、p397-408（计数器与许可拒绝）。
- 复核后排除的纯操作提示框（非边界类，不构成候选）：p38/p84 等 Tips（训练环境 iso 在 NAS）、p246（不同服务器按键可能不同）、p252（F11/F9 因机型而异）、p270-271（15-20 分钟时长，已入 principle p38 关联口径）、p296（升级保留状态，已并入 n28 正文）。
- 推断性结论：无新增推断条目（本教材的 Warning/Note 均为原文明示；n56 中对 p404 示例文字错误的判断已注明为编辑复制错误的识别，判据本身照抄原文）。
- 版本号均按原文保留完整位数：R101.1 MD4、R101.0 MD3、N3、ESXi 8.0/7.0、Hyper-V 2022/2019/2016、KVM ≥4.12.14、Nutanix AHV 20230302/20220304、ESXi 6.0（thick client 上限）、Rocky Linux 9.4。
