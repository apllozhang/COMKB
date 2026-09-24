# 原则/清单/规则/公式/数值口径候选 — OmniPCX Enterprise Loading (ENTPXTE402EN Ed12)

> 提取器: principle-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 类型标签: principle=原则 / checklist=清单 / rule=规则 / formula=公式 / metric=数值口径
> 注: 原书为培训实验手册，所有实验环境给定值（IP、密码、账号）均标注"实验口径"，生产化需替换。

```yaml
- id: p01
  title: OXE 账户密码规则全集：≥14 字符、9 条约束 + aging 取值 0-366 天 + CIS 警告
  type: rule
  source_pages: p91, p175, p273
  source_chapter: Call Server loading / OXE VM loading / Post-Installation Wizard（三处一致的密码规则输出）
  source_quote: |
    "Password rules :
      - password string must have a minimum of 14 characters
      - password string must have at least 2 alphabets (1 upper case mandatory)
      - password string must have at least 2 numeric characters
      - password string must have atleast 1 special character ( ~!@#$%^&*()_+=`{}|[]\:";'<>?,./ )
      - password string must not contain the user account name in any form
      - password string must not contain 4 or more consecutive same characters
      - password string must not contain 4 or more sequential characters (eg: abcd or 1234)
      - password string must not contain dictionary words
      - password must be different from the last twenty-four used passwords" (p91)
    "How many days do you want to keep validate passwords <10<X<366, 0 for no aging) ? 0
    WARNING ! Deactivation of password aging is not recommended for root user as per
    CIS_Benchmark_Req.No_5.6.1.1" (p91)
  summary: |
    加载后为 root/mtcl/adfexc/swinst 四账户逐个设密时的硬规则 9 条：≥14 字符；≥2 个字母（其中 1 大写强制）；≥2 个数字；≥1 个特殊字符（字符集见原文）；不得含账户名任何形式；不得含 4 个及以上连续相同字符；不得含 4 个及以上顺序字符（如 abcd/1234）；不得含字典词；不得与前 24 个已用密码相同。aging 提问取值 <10<X<366，0=不限期；实验口径全部设 Superuser2580* 且 aging=0。原书在每次 aging=0 后打印 CIS_Benchmark_Req.No_5.6.1.1 警告（不建议对 root 停用 aging）——生产环境应保留 aging。
  conditions: 适用于加载后首次设置；kbdconfig 可后改键盘（p174）
  tags: [rule, security, password, cis]

- id: p02
  title: SOT VM 资源前置：Template Factory 8CPU/16GB/500GB；降级模式仅加 50GB 盘
  type: metric
  source_pages: p28-29, p158-159
  source_chapter: « TEMPLATE FACTORY» CONFIGURATION / DEGRADED MODE / How-To
  source_quote: |
    "Pre-requisites for the S.O.T . VM • 8 CPUs / 16Go memory size / 500Go for the second disk •
    Vmx flag (or Virtual machine capability) activated on the CPU specification • USB controller
    available (mandatory for virtualization software)" (p28)
    "Set the size to 50 GB ... Enter Y to bypass resource control" (p159, p164)
  summary: |
    标准 Template Factory 前置：8 CPU、16GB 内存、第二盘 500GB、CPU 开 Vmx（嵌套虚拟化）标志、USB 控制器（虚拟化软件必需）；对应 OVA 为 softwareOrchestrationToolWithTemplateFactory.ova。降级模式只需在标准 softwareOrchestrationTool.ova 上加一块 50GB 虚拟盘，硬件前置全部不受控（构建 OVA 时长强依赖机器 RAM/核数）。判据：SOT 启动时自动检查并在控制台打印启用行；未满足时用 templateFactory 命令可显示缺失项。
  conditions: default→Template Factory 转换须先关机
  tags: [metric, sot, template-factory, capacity]

- id: p03
  title: SOT 更新三条规则：仅同主版本；zip+MD5 双文件；zip 与 ISO 同交时功能同级
  type: rule
  source_pages: p35, p47, p197
  source_chapter: SOT UPDATE
  source_quote: |
    "SOT VM can be updated by installing patches (“.zip” file + “.MD5” file) • This functionality
    will only be offered for S.O.T solutions in the same major version." (p35)
    "When the “zip” file and the “ISO” file are delivered together, the “ISO” file version is upper
    than the “zip” file version. In this case, those two deliveries have the same level of
    functionalities. Only the O.S. can be different" (p47)
  summary: |
    规则三条：(1) 只能同主版本（A.B）内更新，跨主版本（如 3.1→3.2）禁止，需重装 ISO；(2) 更新必须 zip+MD5 两个文件成对，且媒体须在"托管 SOT 的 PC / SOT 本地存储 / NFS 服务器"三处之一；(3) zip 与 ISO 同时交付时功能同级（可能只有 OS 差异），zip 单独交付修缺陷时必须注明所基于的 ISO 版本。更新过程 SOT 重启，完成后 About 菜单核版本。
  conditions: 版本命名见 p03 关联（ISO A.B.XXX.000 / zip A.B.XXX.YYY，更新版末 3 位非 000）
  tags: [rule, sot-update, versioning]

- id: p04
  title: SOT 网络设置规则：最多 4 个子网；接口数与声明 IP 数必须一致；加接口需重启
  type: rule
  source_pages: p46, p196
  source_chapter: SOT VM deployment（standalone 与 hosted 两章的相同 Warning）
  source_quote: |
    "Up to 4 different subnetworks can be configured. ... Warning THE NUMBER OF NETWORK INTERFACES
    (NETWORK CARDS) ASSIGNED TO THE SOT VIRTUAL MACHINE AND THE NUMBER OF IP ADDRESSES DECLARED IN
    THE SOT WEB PAGE MUST BE COHERENT ... ADDING A NETWORK INTERFACE REQUIRES A RESTART OF SOT
    VIRTUAL MACHINE." (p46)
  summary: |
    三条规则：(1) SOT 最多配 4 个子网（可用于分网段安装/更新）；(2) 虚机网卡数与 Web 页声明的 IP 数必须一致；(3) 默认只有 1 个接口，新增接口必须在虚机上加卡且加卡后要重启 SOT。字段：IP address/Netmask/Gateway。
  conditions: standalone（p46）与 hosted（p196）两章警告原文相同
  tags: [rule, sot, network]

- id: p05
  title: SOT 首连安全规则：强制改密 + 口令短语；复杂度 ≥8 字符四类各一
  type: rule
  source_pages: p44-45, p195-196
  source_chapter: First access to the SOT VM web interface
  source_quote: |
    "At the first connection to the web interface, the user will be asked to provide a new complex
    password; it must contain at least 8 characters with 1 uppercase, 1 lowercase, 1 special
    character and 1 alphanumeric characters. Moreover, the user must select a passphrase with an
    associated answer, in order to be able to use the “forgot password” functionality." (p44)
  summary: |
    SOT Web 首连（默认 admin/letacla，实验口径）强制：新密码 ≥8 字符且含大写、小写、特殊字符、字母数字各 1；必须设置口令短语（passphrase）问题与答案，用于"忘记密码"自助重置。后续可在 Settings/Account settings 修改密码与口令短语（另有 FTP 账号设置菜单，p196）。注意与 OXE 侧密码规则（p01）不同——SOT 是 8 字符四类各一，OXE 是 14 字符九条。
  conditions: 实验口径新密码 Superuser2580*
  tags: [rule, security, sot]

- id: p06
  title: 补丁规则律：静态停话音/先版本、动态热装/后静态、补丁累积包含全部此前修正
  type: rule
  source_pages: p65-66, p104-105, p102
  source_chapter: PATCH LOADING - PRINCIPLES / How-To Warnings
  source_quote: |
    "Static patch: • They can only be installed with the phone shut down or when installation is on
    the inactive partition ... Dynamic patch: • They can be installed on the active or inactive
    partition with the phone running without disturbing phone operation • Dynamic patches are
    installed after static patch installation" (p65)
    "A patch (static or dynamic) includes all of the previous patch corrections • The patch N420536
    includes the patches 1 to 36 corrections • The patch N420536d includes the patches a to d
    corrections" (p66)
    "FOR A SAME VERSION (E.G : « N4.205 »), THE STATIC PATCH (« N4.205.36») MUST BE INSTALLED BEFORE
    THE DYNAMIC PATCH (E.G. : « N4.205.36.A »)" (p105)
  summary: |
    四条定律：(1) 静态补丁只能停话音装（或装 inactive 分区），且必须在对应完整版本已装之后；(2) 动态补丁可在话音运行中装 active 或 inactive，不打扰运行；(3) 同版本内动态补丁必须装在静态补丁之后（版本不存在或静态缺失时都不能装动态）；(4) 补丁累积：N420536 含 1-36 全部修正，N420536d 含 a-d 全部修正——装最新补丁即得全部修正。文件形态：zip 通常一包一补丁（静/动分开装两次）；iso 可同含静态+动态一次装（p102）。加载最多两步：step 1 全系统公共文件，step 2 国家相关文件（p66）。
  conditions: active 分区装静态补丁会自动重启系统（p104 Warning）
  tags: [rule, patch, static, dynamic, versioning]

- id: p07
  title: N3 以下迁移硬规则：必须重格式化、盘 ≥80GB、RAM ≥1GB、/root 与 /root2_d ≥3.5GB、禁多版本
  type: rule
  source_pages: p78
  source_chapter: WARNING INSTALLATION/MIGRATION FROM N3
  source_quote: |
    "Coming from ANY version < N3, the Call Server MUST be reformatted: • Ensure the CS model is
    compatible (CS3 / CPU8 / VM). • Disk size is at minimum of 80GB • RAM size is at minimum 1GB ...
    /root and /root2_d need to be at least 3,5GB • No possibility to use the multi version loading
    • N3 or higher release cannot co-exist with older releases (< n3) in active/in-active partitions
    and switchover is not possible" (p78)
  summary: |
    任何低于 N3 的版本迁移：CS 必须重新格式化；机型须兼容（CS3/CPU8/VM）；磁盘 ≥80GB；内存 ≥1GB；只能做完整版本加载（从 N3 起）；新增分区满足 CIS Benchmark 要求，/root 与 /root2_d 各 ≥3.5GB；多版本加载不可用——N3+ 不能与 <N3 版本共存于 active/inactive 分区，也无法切换。权威文档 TC3104en-Ed08_Migration_guide_to_OXE_R101.x。
  conditions: 多版本机制仅适用于双方都 ≥N3 的组合
  tags: [rule, migration, n3, capacity]

- id: p08
  title: OXE VM 规格模板四档：500/3000/7000/15000 用户；OXE-V 虚机无须填 MAC
  type: metric
  source_pages: p169, p208, p216
  source_chapter: OXE VM loading（KVM/ESXi 两章的项目字段表）
  source_quote: |
    "OXE sizing Choose the template, according to the number of users that will be declared in the
    OXE (500/3000/7000/15000). Depending on the chosen template, the OXE VM will have specific
    settings (hard drive size, memory…)" (p169)
    "CPU MAC address Enter the CS MAC address (NOT required when OXE virtual machine (.ovf file) is
    created with S.O.T.)" (p208)
  summary: |
    SOT 生成/加载 OXE VM 时按用户数选模板：500/3000/7000/15000 四档，模板决定虚机硬盘与内存规格；另有 "OXE template for AWS" 选项生成 AWS 环境镜像。目标为 SOT 生成的 .ovf/.ova 虚机时不要求 MAC 地址（虚机自动）；目标为物理 CS 时必须提供 MAC（板卡贴纸/终端 ifconfig/NAS Excel，实验口径）。OMS 项目可勾 "Add an OMS server" 一次生成多台（一个项目最多 4 台 OMS，p216）。
  conditions: 模板档位为 Ed12 口径
  tags: [metric, oxe-v, sizing, template]

- id: p09
  title: OMS 容量与许可数值：120 通道/台、240 台/OXE、Lock 384/385、会议 3/6/14/29 方
  type: metric
  source_pages: p138-140
  source_chapter: OMS: OVERVIEW / FEATURES / LICENSES
  source_quote: |
    "120 VOIP channels per OMS 240 OMS per OXE" (p138)
    "•Three-party conference •6-party conference •14-party conference •29-party conference" (p139)
    "Lock 384: ‘OXE Media Services’ ... Lock 385: ‘VoIP channels on OMS’ ... It can be installed
    without rebooting the Call Server" (p140)
  summary: |
    数值口径：每台 OMS 120 个 VoIP 通道；每 OXE 最多 240 台 OMS；编解码 G.711（20ms）、G.729（20/40ms）、G.722（20ms）、OPUS（20ms），仅宽带与窄带；会议 3/6/14/29 方四档；DTMF 走 RTP payload RFC4733（旧称 RFC2833）；QoS 802.1p/DiffServ。许可：Lock 384 核对配置中 OMS 台数、Lock 385 核对全部 OMS 的 VoIP 通道（压缩器）总数，两锁均可不停机安装（spadmin）。
  conditions: OMS 软件 + Suse OS；许可核查命令 spadmin
  tags: [metric, oms, capacity, licensing]

- id: p10
  title: OXE-V 虚拟化版本矩阵（Ed12 时点）：ESXi 8.0/7.0、Hyper-V 2022/2019/2016、KVM ≥4.12.14、AHV/AWS 除外 OST64
  type: metric
  source_pages: p134
  source_chapter: GENERAL OVERVIEW / Virtualization technologies
  source_quote: |
    "VMware ESXi (1) 8.0 7.0 ... Microsoft Hyper-V 2022 2019 2016 (2) ... KVM kernel ≥ 4.12.14 & KVM
    ≥ 5.2 (3) ... Nutanix (AHV) 20230302 20220304 (except OST64) ... AWS (except OST64)" (p134)
    "(2): A generation 1 Virtual Machine has to be created for the Call Server, whereas a generation 2
    Virtual Machine has to be created for OXE-MS, OST64 and EEGW." (p134)
  summary: |
    逐格口径：ESXi 8.0/7.0（兼容该版本的 minor 更新）；Hyper-V 2022/2019/2016（CS 用第 1 代虚机，OXE-MS/OST64/EEGW 用第 2 代）；KVM 内核 ≥4.12.14 且 KVM ≥5.2（RHEL/SLES/Proxmox 等标准 KVM 均可，定制 KVM 如 Nutanix AHV 需专项认证）；Nutanix AHV 20230302/20220304（OST64 除外）；AWS（OST64 除外）。权威文档 TBE043（Virtualization Design Guide）。
  conditions: 平台版本随教材时点演进，生产以 TBE043 最新版为准
  tags: [metric, oxe-v, virtualization, version-matrix]

- id: p11
  title: 许可路径矩阵：FlexLM+加密狗仅 ESXi/KVM；Hyper-V/Nutanix/AWS 强制 Cloud Connect；两种模式不可并存
  type: rule
  source_pages: p135-136, p331
  source_chapter: OXE-V licensing / RTR configuration Warning
  source_quote: |
    "Hyper-V , Nutanix and AWS don’t provide a native way to redirect an USB dongle from the host to
    a given Virtual Machine • No FlexLM server delivery neither as an Hyper-V , Nutanix or AWS
    Virtual Machine • Cloud Connect is the mandatory license control process in case an OXE is
    virtualized over Hyper-V , Nutanix or AWS technology" (p136)
    "Warning FOR COMMUNICATION SERVERS RUNNING ON VIRTUAL MACHINES, VERIFY THAT LICENSING VIA FLEXLM
    SERVER IS NOT ACTIVATED. THE TWO LICENSING MODES (FLEXLM SERVER AND CCI/RTR) CANNOT RUN AT THE
    SAME TIME" (p331)
  summary: |
    矩阵规则：FlexLM 服务器 + 加密狗路径仅 VMware ESXi 与 KVM 可用；Hyper-V/Nutanix/AWS 无 USB 加密狗重定向、也无 FlexLM 虚机交付，必须走 Cloud Connect（CC-SUITE-ID）许可。且对任何虚机 CS：FlexLM 与 CCI/RTR 两种许可模式不能同时启用——启 RTR 前必须核对 FlexLM Licensing Enabled=No（改 RTR 参数需重启 CS，p331 Tips）。
  conditions: FlexLM 许可文件 .ice（含 dongle ID/MAC/ALUID + 产品 ID）；RTR 详见 p17-p19
  tags: [rule, licensing, flexlm, rtr, matrix]

- id: p12
  title: GAS 硬件前置表逐格：组件组合 × 核数/主频/内存/360GB 盘；>12000 用户 +2GB；>7000 用户外部 WebRTC
  type: metric
  source_pages: p226
  source_chapter: HARDWARE PRE-REQUISITES
  source_quote: |
    "Installed components Minimal requirements
    OXE OXE-MS WebRTC Gateway Cores Core speed RAM Hard disk
    ✓ - - 2 any 4 GB(*) 360 GB
    ✓ ✓ - 2 2.8 GHz 6 GB(*) 360 GB
    ✓ - ✓(**) 3 2 GHz 6 GB 360 GB
    ✓ ✓ ✓(**) 4 2.8 GHz 8 GB 360 GB
    (*) In case there are more than 12,000 users, 2 additional gigabits of vRAM are required
    (**) Above 7,000 users, an external WebRTC gateway is required (the one embedded in the GAS is
    limited to 50 simultaneous conversations)" (p226)
  summary: |
    逐格转写（仅 OXE 为必装底座）：OXE——2 核任意主频/4GB/360GB；OXE+OMS——2 核 2.8GHz/6GB/360GB；OXE+WebRTC——3 核 2GHz/6GB/360GB；OXE+OMS+WebRTC——4 核 2.8GHz/8GB/360GB。附注：用户数 >12000 时内存加 2GB vRAM；内嵌 WebRTC 网关上限 50 并发通话，>7000 用户必须外部网关。平台要求：兼容 Rocky Linux（含 KVM）；CPU 最低 Haswell 代（支持 Intel 64 与 Intel VT）；1GB 网卡；必须能 DVD 引导；建议 USB 口；只允许硬件 RAID（软件 RAID 不支持）。注：满配拓扑在 HP DL20 G10+ 与 DL20 G11 之前的 ALE Appliance Server 上装不下。
  conditions: BP/客户自备服务器须逐项满足；盘 360GB 为最小值
  tags: [metric, gas, hardware, capacity]

- id: p13
  title: GAS 组件规则：OXE+FlexLM 必装；OMS 仅 1 台且禁第二台；WebRTC 50 并发上限；冗余禁混搭平台
  type: rule
  source_pages: p225, p227-229
  source_chapter: DESIGN RULES / APPLIANCE SERVER SHIPPED BY ALE / HISTORY / REDUNDANCY
  source_quote: |
    "Mandatory components when installing a GAS • Both OXE Call Server and FlexLM license server are
    mandatory ... For performance reason, installing a second OXE-MS on the GAS is forbidden ... The
    gateway is restricted to a maximum of 50 simultaneous calls (Above 7,000 users, an external
    WebRTC gateway is required)" (p225)
    "Both platforms must have similar hardware characteristics in case of redundancy • Mix of
    Appliance Server and Generic Appliance Server not allowed for a redundant OXE" (p229)
  summary: |
    五条组件规则：(1) OXE CS 与 FlexLM 许可服务器必装（FlexLM 直接装在宿主 Rocky OS）；(2) OMS 可选但每台 GAS 最多 1 台，且必须与 CS、FlexLM 一起做初始安装，禁装第二台（性能原因）；(3) Rainbow WebRTC GW 可随装或后加装，上限 50 并发，>7000 用户用外部网关，冗余拓扑可在两台 GAS 各部署一个；(4) HP DL20 G11 只能用 GAS 软件包（经典 OXE 包不支持），许可限 ALU-ID 或 CC-SUITE-ID，可跑满配拓扑（<7000 用户），ALE 交付平台可按 HP 生命周期透明更换；(5) 冗余双机硬件须相似，Appliance Server 与 GAS 禁止混搭。存量：经典 OXE 软件包在所有物理服务器上均已不再支持，legacy 须迁 GAS 或虚拟化（TBE063）。
  conditions: 另见 p230：GAS 的 OXE 升级用 OXE 型项目（GAS 型项目无升级路径）；OMS 由 CS 经 TFTP 自动升级
  tags: [rule, gas, components, redundancy]

- id: p14
  title: GAS IP 连通性需求：宿主/FlexLM 同 IP、网关 IP 安装期间必须可达、DNS 可用 GAS IP 顶替
  type: checklist
  source_pages: p235
  source_chapter: GAS - IP CONNECTIVITY
  source_quote: |
    "The IP address / FQDN of the host server (same IP address for the FlexLM server And for the host
    machine) • The IP address of the default gateway (this IP MUST be accessible during installation)
    • The IP address of the DNS server (the GAS IP address may be used if the customer doesn’t want
    to configure a DNS server)" (p235)
  summary: |
    GAS 安装需要：宿主服务器 IP/FQDN（FlexLM 与宿主共用同一 IP）；默认网关 IP（安装期间必须可达）；DNS 服务器 IP（客户不想配 DNS 时可用 GAS 自身 IP 顶替）；OXE CS IP/FQDN；OMS IP/FQDN（可选）；WebRTC GW IP/FQDN（可选）。IP 计数：宿主 1 + OXE VM 1 + OMS VM 1 + WebRTC VM 1。
  conditions: 安装期网关可达为硬前提
  tags: [checklist, gas, network]

- id: p15
  title: GAS 运维命令与备份规则：gasversion / gasbackup（.tar.gz+.cfg）/ 备份+全新安装=免后安装
  type: rule
  source_pages: p239-241, p275-279
  source_chapter: GAS SERVICEABILITY / Post-Installation Wizard 5.x
  source_quote: |
    "“gasversion” command to get version of GAS, OXE, OXE-MS, Rainbow WebRTC gateway and Rocky Linux
    operating system ... #gasversion <component_name> • Here <component_name> can be:
    all|package|oxe|oms|webrtc" (p239)
    "Archive file is created by default in “/var/backup/” directory, in “<oxe_name >_YYMMDD .tar.gz”
    format • The archive file contains “mao-acc” and “Postinstall.cfg” files" (p240)
    "GAS package fresh installation + GAS backup = functional GAS system, without the need to perform
    the post-installation" (p241)
  summary: |
    运维三件套：(1) gasversion——查 GAS 包/OXE/OMS/WebRTC/Rocky 版本，交互菜单（1.GAS Package 2.OXE 3.OMS 4.WebRTC）或 gasversion all|package|oxe|oms|webrtc；(2) gasbackup——整 GAS 备份（OXE 数据库、各组件网络配置、许可文件），交互模式问 OXE 账号/密码/路径（默认 /var/backup）后需确认，CLI 模式 gasbackup -u mtcl -p **** -d <路径> 免确认；产物 <oxe_name>_YYMMDD_hhmmss.tar.gz + 同名 _PostInstall.cfg（后者仅静默恢复后安装用）；归档内容含 *.ice mao-acc cho-dat obstraf acd noe PostInstall.cfg hardware.mao 等；(3) 全新安装+恢复备份=免后安装向导即可用（恢复可在 GUI 或静默模式）。备份前提：OXE 许可控制已配置（.swk 入 /usr4/BACKUP/OPS、.ice 入 FlexLM 目录、OXE 指向 Flex 服务器）。
  conditions: gasbackup 经 SSH 连 OXE（swinst 账号）；Eva-msg 缺失仅警告不阻塞
  tags: [rule, gas, backup, commands]

- id: p16
  title: GAS host OS 升级与 UPS 规则：gas-rocky-update.sh / NUT（30% 默认阈值、5 秒轮询）
  type: rule
  source_pages: p236-238
  source_chapter: LINUX PATCH UPGRADE SUPPORT FOR GAS (HOST) / UPS MONITORING
  source_quote: |
    "Via SOT , with an “GAS" type “Project for existing products” and select the new bootdvd iso file
    • Via gas-rocky-update.sh command after having mounted the Bootdvd on the GAS host ... The virtual
    machines (OXE, OMS and WebRTCGW) will be gracefully shutdown before the patch update and the Rocky
    Linux is rebooted afterwards" (p237)
    "Automatic safe shutdown (server & VMs) if UPS battery power percentage reduces to configured value
    (Default: 30 %) • UPS status retrieved at a configurable frequency (5 seconds by default) • UPS
    management in GAS package is performed with NUT Linux package, present in the BootDVD" (p236)
  summary: |
    host 升级两条路：SOT 建 GAS 型 "Project for existing products" 选新 bootdvd iso；或挂载 BootDVD 后跑 gas-rocky-update.sh（脚本位于 /home/OmniPCXEnterpriseSoftwareServer/Installation_Folders/Tools；示例 mount /dev/cdrom /media/cdrom 后 gas-rocky-update.sh /media/cdrom）；日志 /var/log/rocky-update.log 与 /var/log/gas-rocky-update.log；升级前 VM 优雅关机、Rocky 随后重启。UPS：USB 信号线监控，事件记 /var/log/gasups.log；电量降至阈值（默认 30%）自动安全关机（服务器+VM）；状态轮询频率可配（默认 5 秒）；由 BootDVD 内 NUT（Network UPS Tools）实现，可经补丁升级加装到存量 GAS。
  conditions: host 升级会导致全部 VM 停机窗口
  tags: [rule, gas, upgrade, ups, nut]

- id: p17
  title: Cloud Connect 网络要求清单：出站 443(XMPP/WSS)+80(SOCKS5)+53(DNS)、FQDN connect2.opentouch.com、TLS1.2、代理可选
  type: checklist
  source_pages: p287-290
  source_chapter: CONNECTION WITH THE CLOUD CONNECT INFRASTRUCTURE
  source_quote: |
    "Resolve FQDN of a public resource, with DNS resolution to port 53/udp. • Establish a permanent
    XMPP channel to CCO infra over Web Socket Secure to port 443/tcp • HTTP proxy can be provided in
    option • The remote FQDN used by OXE agent is connect2.opentouch.com • Establish a temporary
    SOCKS5 Connection to CCO infra using to port 80/tcp" (p290)
  summary: |
    客户环境要求：ALE 设备可出 Internet；边界网关/防火墙放行出站到公共 CC 基础设施；DNS 解析（53/udp）；常驻 XMPP over WSS 到 443/tcp；按需 SOCKS5 到 80/tcp；两者均可经 HTTP 代理（可选）；目标 FQDN connect2.opentouch.com。安全机制：OXE 主动发起双向连接（不改客户安全策略，防火墙/Web 代理/DNS 零或最小改动）；TLS v1.2（CCI 服务器证书由 ALE 责任下的 CA 签发，OXE 专用信任库存该 CA 证书）；XMPP 认证为每产品唯一 ID+密码。
  conditions: DNS/代理配置仅被 Rainbow 与 Cloud Connect 代理使用（p317 Notes）
  tags: [checklist, cloud-connect, network, ports]

- id: p18
  title: CC-SUITE-ID / CC-PRODUCT-ID 语法与不变性规则
  type: rule
  source_pages: p291, p327
  source_chapter: CLOUD CONNECT PRODUCT IDENTITY / CC-suite ID display Notes
  source_quote: |
    "The syntax of the CC-SUITE-ID is: ADCBE-FGHIJ-KLMNO-PQRST • A 23-character string where A..T
    represent an hexadecimal digits (from “0” to “9” and “A” to “F”) written in upper case
    characters. The 20 hexadecimal digits are packed 5 by 5 and separated by “-” • This ID Remains
    the same during the product lifetime" (p291)
    "CC-Suite-ID will never be the first one in the file (to not impact Flex configurations for which
    first one is used) In order for OXE to differentiate CCSID from CPU-Id, CC-Suite-ID is prefixed
    with “CCSID:” There is only one CC_SUITE_ID for both main and standby CPU." (p327)
  summary: |
    语法规则：CC-SUITE-ID 为 23 字符字符串——20 个十六进制大写字符（0-9/A-F）按 5 个一组、以"-"分隔；订单链生成、写在 .swk 里、产品终身不变（加功能或换 CPU 都不变）。CC-PRODUCT-ID = CC-SUITE-ID + "-" + 产品类型（OXE 示例 af76e-05961-da1c1-de028-3）。spadmin 视图规则：Suite Id 永不出现在文件第一位（避免影响 Flex 配置）；显示时带 "CCSID:" 前缀与 CPU-Id 区分；主备 CPU 共用一个 CC-SUITE-ID；当 MAO 中 "Cloud Connect RTR Enabled"=No 时 spadmin 不显示 Suite Id。
  conditions: 每产品一个激活账户（基于 CC-Suite-ID），密码可变、ID 不变
  tags: [rule, cc-suite-id, identity]

- id: p19
  title: FTR 行为规则集：自动 FTR 每 4h 重试（6214/6207）、备机禁做、凭证克隆同步、PCS 无云服务、需电话应用已启动
  type: rule
  source_pages: p296-297, p328-329
  source_chapter: FTR – NEW INSTALL / OXE REDUNDANCY AND PASSIVE CALL SERVER / How-To
  source_quote: |
    "Automatic FTR to register the OXE on Cloud Connect ... Registration attempt every 4 hours till a
    successful automatic FTR (or a successful manual FTR via CCTool) • An incident (6214) is issued at
    each unsuccessful attempt • Cleared by incident 6207 in case of successful connection to CCO" (p296)
    "Never perform a First Time Registration (FTR) on a stand-by Call Server ... The final credentials
    received from CCI are automatically synchronized with the TWIN Stand-by CS ... Cloud Services DO
    NOT run on Passive Communication Server (PCS)" (p297)
    "This operation can only be performed if the telephone application is started." (p328)
    "Warning THERE IS NO NEED TO PERFORM “FTR” ON STANDBY CPU." (p329)
  summary: |
    行为规则六条：(1) 新装机（Cloud Connect enable 默认开）自动 FTR，每 4 小时重试直至成功；每次失败发事件 6214，成功由 6207 清除；等不及可 CCTool 手动立即做；(2) 已有 CC 密码的存量 OXE 不做自动 FTR；升级到 R101.0 MD3+ 保留现状，enable 参数按有无 CCO 密码初始化；(3) 备机严禁做 FTR（Warning 两处）——永久凭证由主 CS 经标准克隆机制自动同步到 twin（存在 OXE 数据库中、隐藏）；(4) 切换后备机转主即恢复 CCI 链接；(5) PCS 上不跑云服务；(6) FTR 只能在线路应用已启动时执行。排障：失败查 /tmpd/Cloud_cnx/logs 的 ccprocess.log 并用 CCTool 复核（p329 Tips）。
  conditions: CCTool 使用前提是 Cloud Connect enable 参数已激活
  tags: [rule, ftr, redundancy, incidents]

- id: p20
  title: FTR with PIN 规则：6 位数字、5 天有效、不落盘、重置全部云配置、需 RTR+ccagent 进程在跑
  type: rule
  source_pages: p299-300, p330
  source_chapter: FIRST TIME REGISTRATION WITH PIN CODE
  source_quote: |
    "A new temporary activation account will be created with a 6 digits (0-9) PIN code and will be
    provided by helpdesk." (p299)
    "The PIN code will be transmitted to the “ccprocess” process to restart the FTR procedure, but
    won’t be saved in any file. Performing this operation will completely reset the Cloud Connect
    configuration and settings while the system is still in service. The "FTR with PIN code" can only
    be performed with the "RTR" and "ccagent" processes started." (p330)
  summary: |
    规则五条：(1) PIN 为 6 位数字（0-9），由 helpdesk 提供，有效期 5 天；(2) PIN 只交给 ccprocess 发起重注册，不保存到任何文件；(3) 操作在系统在线状态下完全重置 Cloud Connect 配置；(4) 前提是 RTR 与 ccagent 进程已启动，否则 FTR 不执行；(5) helpdesk 侧同时删除其他激活账户并断开同 ID 全部产品；PIN 生成会移除 RTR 服务器上两侧记录（Duplicated 场景），仅用 PIN 的系统可重注册并恢复 30 天资格期。
  conditions: 仅 panic 态使用（RTR Panic Flag / Duplicated / 无效 FTR 数据）
  tags: [rule, ftr, pin, recovery]

- id: p21
  title: RTR 资格期数值律：30 天起、OK +0.5 / NOK -1、归零 Panic 行为清单
  type: metric
  source_pages: p304, p308
  source_chapter: RIGHT TO RUN (RTR): QUALIFYING PERIOD / MISCELLANEOUS
  source_quote: |
    "A grace period of 30 days is initiated by default at the initialization of the RTR service ...
    OK: the remaining Qualifying Period is increased of 0,5 day to the limit of 30 days • NOK: the
    remaining Qualifying Period is decreased of 1 day to the limit of 0 day • If the counter reaches
    the limit of 0, the Panic Flag for RTR is raised on the OXE system, that runs in deprecated mode
    • The message « Call your administrator » is displayed on the DeskPhones when a communication is
    established • No more configuration change is accepted by database and telephonic services" (p304)
    "During Save/Restore operation, the previous value of remaining qualifying period is maintained
    across reboots • The remaining qualifying period value is updated on the Twin Call Server (if
    present)" (p308)
  summary: |
    数值律：RTR 服务初始化即给 30 天资格期；每日经 XMPP 向 RTR 服务器请求——OK 加 0.5 天（上限 30），NOK 减 1 天（下限 0）；归零触发 Panic Flag，系统进 deprecated 模式：话机建立通话时显示 "Call your administrator"，数据库与电话服务拒绝一切配置变更。持久性规则：Save/Restore 后资格期值跨重启保留；值自动更新到 twin CS；RTR 参数自动复制到备机。无应答/断连行为见 p21 关联条目（4 小时窗口）。
  conditions: RTR 不替代产品级 swk 许可，只是总开关（p303）
  tags: [metric, rtr, qualifying-period, panic]

- id: p22
  title: RTR 重试口径辨析：每日请求；p304/p308 写"4 小时窗口、10 分钟间隔重试后减 1 天"，p332 写"无重试直到次日并减 1 天"——两处表述不一致
  type: rule
  source_pages: p304, p308, p332
  source_chapter: RTR QUALIFYING PERIOD / MISCELLANEOUS / RTR status Notes
  source_quote: |
    "In case of no reply for Right To Run request or no connection to Cloud Connect Infrastructure •
    OXE will retry the Right To Run check up for four hours with interval of ten minutes • If the
    connection is not restored at end of the fourth hour • OXE will decrement the qualifying period
    by one. The same procedure will be repeated on next day at the exact the same time" (p308)
    "RTR process performs a daily request to RTR server. At each request, RTR read “cc_suite_id” from
    “software.mao” file. If a problem occurs when RTR request is sent, no retry is performed until
    next daily request and one day is decreased from remaining qualifying period." (p332)
  summary: |
    三处口径合并阅读：RTR 做每日请求（请求时读 software.mao 中的 cc_suite_id）。失败后的重试行为两处描述不一致——p308（讲义 Miscellaneous）说"4 小时窗口内每 10 分钟重试，4 小时后仍不通才减 1 天，次日同一时间重复"；p332（How-To Notes）说"当天不再重试直到次日每日请求，且（请求出问题时）减 1 天"。现场建议按保守口径（可能当日即减 1 天）做监控告警，不要赌 4 小时宽限；具体行为以最新 TC/发布说明为准（教材内部口径差异本身记录为待确认）。
  conditions: 本条为教材内部口径差异记录，需以 ALE 最新文档裁决
  tags: [rule, rtr, retry, discrepancy]

- id: p23
  title: RTR 四级状态与通知阈值：Connected 29-28 / Qualifying 27-10（27、20 天各一封）/ Soon Blocked 9-1（每日）/ Blocked-Panic 0
  type: metric
  source_pages: p305-307
  source_chapter: RTR STATUS PRINCIPLES / Status displayed on Fleet Dashboard
  source_quote: |
    ": OXE connected within the last 24h or Remaining Qualifying Period between 29 -28 days ... :
    No connection from OXE in last 24h and Remaining Qualifying Period between 27-10 days Email
    notifications will be sent to inform the change of status when reaching 27 days, then 20 days ...
    : No connection from OXE in last 24h and Remaining Qualifying Period between 9-1 days ... Email
    notifications will be sent to inform the change of status every day ... : ... the remaining
    Qualifying period reach value 0 A Panic Flag for RTR has raised" (p306)
  summary: |
    Fleet Dashboard 状态列（数据库每晚更新）：Connected——24h 内有连接，或剩余资格期 29-28 天；Qualifying——超 24h 无连接且 27-10 天（到 27 天、20 天各发一次状态变更邮件）；Soon Blocked——9-1 天（每天发邮件；CC System Incidents 计数增加）；Blocked-Panic——0 天（Panic Flag 已挂起，需 PIN 恢复；事件计数保持）。两个特殊态：Not connected（未注册 RTR）；Duplicated（CC Product ID 已被另一系统占用——误用或真实入侵；该态覆盖 Soon Blocked 显示，两侧系统同时扣减资格期，必须 PIN 恢复真系统）。可配置管理邮箱接收分级通知；VAD 可把子机队委托给 IR。
  conditions: RTR Status 由"最后连接日期 + 剩余资格期"计算
  tags: [metric, rtr, fleet-dashboard, thresholds]

- id: p24
  title: Cloud Connect 事件码全表：6200-6214（CC）+ 647-651（RTR）
  type: metric
  source_pages: p313, p334
  source_chapter: Monitoring incident of the Cloud Connect XMPP link / Incidents
  source_quote: |
    "6200 CLOUDCONNECT_SUITE_ID_ERROR Error with suiteId ... 6207 CLOUDCONNECT_CCAGENT_CONNECTED XMPP
    link (CCagent<->CloudConnect) in service ... 6214 CLOUDCONNECT_FTR_FAIL Automatic FTR occurs but
    not successfully completed" (p313)
    "647 RTR state, with additional information such as cause and remaining qualifying period
    648 Raised when the PBX switches into panic after 30 days
    649 Generated when FTR with PIN code has been performed. It indicates that PBX exits from panic
    650 Raised when fraudulent activity is detected on PBX: it immediately switches to panic.
    651 Clearance of incident 650" (p334)
  summary: |
    CC 事件（incvisu 查看）：6200 suiteId 错误；6201/6202 ccagent 启/停；6203/6204 WebSocket 通/断；6205 WebSocket 无法连接服务器；6206 XMPP 登录失败；6207/6208 XMPP 链路登入/登出；6209 SOCKS5 建立失败；6210/6211/6212/6213 远程控制台请求/打开/关闭/出错；6214 自动 FTR 未成功。RTR 事件：647 RTR 状态（含原因与剩余资格期）；648 30 天后进 panic；649 PIN FTR 已执行、退出 panic；650 检测到欺诈活动立即 panic；651 清除 650。
  conditions: 事件表为 Ed12 口径；LMS 侧事件见 p31
  tags: [metric, incidents, cloud-connect, rtr]

- id: p25
  title: CC 日志与参数口径：keep alive 默认 90 秒；4 级日志；固定日志路径四件套
  type: metric
  source_pages: p311-312, p333, p336-337
  source_chapter: KEEP ALIVE / SERVICEABILITY / Maintenance
  source_quote: |
    "The value of CC connection keep alive will now be managed through MAO • If its value is changed
    (default= 90 sec), it is taken in account dynamically by the “cc-agent process”" (p311)
    "“CCTool” command to configure the log level for each feature: FTR/RTR/DC/Console/… • 4 log levels
    are available: ERROR/INFO/DEBUG(default)/TRACE" (p312)
  summary: |
    数值与路径口径：KeepAlive 默认 90 秒（MAO/WBM 修改，cc-agent 动态生效；适配会掐空闲 HTTPS 会话的网络；CCTool 3 可查）。日志级别四档 ERROR/INFO/DEBUG（默认）/TRACE，按特性（FTR/RTR/Data Collect/Remote Console/CC agent/Software Update）分别设置。固定路径：/var/log/ccagent.log（XMPP 通道，找最后 STATE_CONNECTED/STATE_DISCONNECTED）；/tmpd/cloud_cnx/log/ccprocess.log（服务执行）及同目录 ccprocesschild/ccservices/collect0-2/oxe_inventory_*/oxe_offer_files；/tmpd/CCAlarm.log（FTR/RTR 事件日记，含 Incident 647 逐日条目）；DC 特性日志同在 /tmpd/cloud_cnx/log/。
  conditions: 日志由 infocollect 工具收集
  tags: [metric, logs, keepalive, serviceability]

- id: p26
  title: Fleet Dashboard 远程控制台与软件更新规则：单会话/1 分钟超时/shell.log 审计；SPS+technical advanced 前提；cdn 域名入信任主机
  type: rule
  source_pages: p341-343, p347
  source_chapter: FLEET DASHBOARD - OFFER FILES / REMOTE MANAGEMENT / SOFTWARE UPDATE
  source_quote: |
    "Only one console can be opened at the same time • Console is disconnected after 1 minute of
    inactivity ... Each connection is logged by the Call Server (shell.log) • Logged data: Fleet
    Dashboard account username and company • Can be viewed from OmniVista 8770 audit application" (p343)
    "OXE with a valid SPS contract • No specific role but ‘technical advanced’ privilege ... “cdn-oxe-
    sw-update.al-enterprise.com” domain must be part of them • Transfer only: switch on the new
    version remains under BP’s responsibility" (p347)
  summary: |
    规则集：远程控制台——同一时间仅一个会话；1 分钟无操作自动断开；连接需 OXE 凭证再认证；每次连接由 CS 记入 shell.log（Fleet Dashboard 账号名与公司名），可经 OmniVista 8770 审计查询；控制台不能从 Fleet Dashboard 主页分离，等价 SSH 远程控制台、支持复制粘贴。Offer Push 与 Software Update 前提——有效 SPS 合同 + technical advanced 特权（无专属角色）；软件更新给 OXE 一个 AWS 仓库临时 URL 由其 HTTPS 下载官方 ISO（与 BPWS 下载区相同文件）；使用信任主机的站点必须把 cdn-oxe-sw-update.al-enterprise.com 加入；只管传输，切换新版本仍是 BP 责任（可用远程控制台安装）。动作状态字段：第一字段 D（需下载）/-；第二字段 I（手动安装）/A（自动安装）/S（手动切分区）/-；第三字段 P（下载中/已请求）/O（完成）/K（失败）/F（OXE 侧禁用软件更新）/-。
  conditions: 远程管理需 OXE 电话应用已启动；Get offer 服务默认启用可关
  tags: [rule, fleet-dashboard, remote-console, software-update]

- id: p27
  title: OPEX 模式锁定规则：lock 431=1 开 OPEX；CAPEX 旧锁失效但 87/165 例外；swk 必含 CCSID
  type: rule
  source_pages: p354, p388, p389
  source_chapter: OXE LICENSE FILE / How-To Prerequisites
  source_quote: |
    "A new lock, 431: 1 means new OPEX mode (0 for CAPEX mode) • Previous CAPEX locks are no more
    taken in account • Except lock Beta tests 87 and lock Release 165" (p354)
    "Warning CORRECT “SWK” FILE IS MANDATORY, WITH: ­ CCSID (CLOUD CONNECT SUITE ID) ­ LOCK 431: OPEX
    MODE SET TO “1”" (p388)
  summary: |
    许可文件规则：OPEX 模式的 .swk 由 ELP 生成（ACTIS 不再用于 OPEX 报价）；software.mao（.swk 的 mao 副本）中 lock 431=1 表示 OPEX 模式、0 表示 CAPEX；启用 OPEX 后既有 CAPEX 锁不再生效，唯 lock 87（Beta tests）与 lock 165（Release）例外仍与版本挂钩。部署前提（Warning）：swk 必须正确且包含 CCSID 与 LOCK 431=1；装完许可后必须重启 OXE，再用 spadmin 核对（OPEX Flag=1、Panic Flag=0）。
  conditions: spadmin 的 Display active file 显示 431 Opex Mode 与 87/165 锁值（p389）
  tags: [rule, opex, lock-431, swk]

- id: p28
  title: PoD 项目规则：一项目=一终端客户+一 BP；上限 1,500,000 用户；许可池项目内共享、跨项目不可移
  type: rule
  source_pages: p355, p396
  source_chapter: PROJECT / How-To LMS Warning
  source_quote: |
    "Each project is associated to only one end-customer and only one Business Partner • Several
    projects may be associated to a given end-customer • A project may contain one or more OXE Purple
    systems and optionally applications • Maximum 1,500,000 users per project • The subscriptions,
    purchased for a given project, are shared by the systems/applications of this project • In case of
    end-customer with multiple projects, move of licenses between projects is not possible" (p355)
    "Warning AT LMS SERVER SIDE, A PROJECT HAS TO BE CREATED FOR THE CUSTOMER. THIS PROJECT CAN BE
    ASSOCIATED TO A SINGLE OXE OR TO SEVERAL OXES. A POOL OF LICENSES IS AFTERWARDS ASSIGNED TO THIS
    PROJECT" (p396)
  summary: |
    项目规则六条：(1) 一个项目只关联一个终端客户和一个 BP；(2) 同一终端客户可有多个项目；(3) 项目含一台或多台 OXE Purple 系统及可选应用；(4) 每项目上限 1,500,000 用户；(5) 项目所购订阅由项目内系统/应用共享（许可池）；(6) 多项目客户之间许可不可跨项目移动。项目随购物车启动即创建（除非挂到既有项目）；可含 OPEX 软件与/或 CAPEX 硬件项；可追加 add-on。OXE 侧前提（Warning）：LMS 上必须已为该客户建好项目并分配许可池，项目可挂一台或多台 OXE。
  conditions: 目录口径见 p29（24 项）
  tags: [rule, pod, project, licensing]

- id: p29
  title: PoD 订阅目录口径：24 个商用项（8 大类）+ UMC 免费；对照约 500 个 CAPEX 软件项
  type: metric
  source_pages: p357, p360
  source_chapter: CATALOG SIMPLIFICATION / OPEX SOFTWARE LICENSES
  source_quote: |
    "24 commercial items at offer level (OXE, OV8770, OTCC, VAA, O2G, OT-SBC, VNA, OPR), compared to
    around 500 software items • A unique OV8770 subscription compared to around 60 software items •
    User centric model, with multi-devices capability by design • No notion of bulk for license
    subscription: bulk is only proposed for hardware" (p357)
    "… just 24 for the whole POD offer ... UMC is provided for free (no associated subscription)" (p360)
  summary: |
    数值口径：PoD 目录共 24 个商用软件订阅项（对照约 500 个 CAPEX 软件项；OV8770 由约 60 项并为 1 个订阅），分 8 类——User Base Profiles（Voice Enterprise 3EY94500AA、Room 3EY94501AA）、Softphones（Softphone 3EY94502AA）、Openness（API Telephony 3EY94505AA、API Management 3EY94506AA）、Attendant Solutions（Attendant Console 3EY94509AA）、Contact Center（Voice Agent 3EY94508AA；ALE Connect Agent 3EY94001AA/Channel 3EY94002AA）、Management（Centralized Network Management 3EY94519AA、Selfcare 3EY94532AA）、Recording（OPR Standard/Business/Enterprise 3EY94514/15/16AA、API Recording Cnx 3EY94513AA）、Notification Alerting（VAA 3EY94512AA、VNA 3EY94517AA、VNA Broadcast 3EY94518AA）、SBC（Session 3EY94520AA、Remote User 3EY94522AA、Transcoding 3EY94524AA、Direct Routing 3EY94526AA、SIPREC 3EY94530AA、Reverse Proxy 3EY94528AA）。UMC 免费提供无对应订阅。计费两档：月付无承诺（随时升降配）或预付 1/3/5 年（随时升配、续费时降配，p379）。用户中心模型天然多终端；订阅无 bulk 概念（bulk 仅硬件）；No PRS in PoD offer（p362）。
  conditions: 目录与件号为 Ed12 时点快照；仅显示申请人所在国家授权的条目
  tags: [metric, pod, catalog, part-numbers]

- id: p30
  title: 订阅消耗类型归属清单：Unitary=Softphone/API Telephony/VNA/VNA Broadcast；On activation=仅 Voice Enterprise 与 Room；By threshold=Attendant Console/Voice Agent/API Recording Cnx/VAA/OPR
  type: rule
  source_pages: p367-369
  source_chapter: THREE TYPES OF SUBSCRIPTION CONSUMPTION
  source_quote: |
    "Unitary licenses • Softphone • API Telephony • VNA, VNA Broadcast ... Licenses on Activation
    (concerns ‘Voice Enterprise’ and ‘Room’ only) ... Attendant Console   number MAX of 4059
    attendants Voice Agent  number MAX of ACD Operator API Recording Cnx  number MAX of DR link
    recording Visual Automated Attendant (VAA ports number declared at VAA level) OPR Standard /
    Business / Enterprise Recording" (p367-369)
  summary: |
    归属清单：Unitary（创建即耗）——Softphone、API Telephony、VNA、VNA Broadcast；LMS 无余量则实例创建被拒。On activation（激活才耗、可停用腾挪）——仅 Voice Enterprise 与 Room 两项；停用用户对 OXE 退出服务但保留配置。By threshold（阈值预留、加阈值才要许可）——Attendant Console（对应 4059 话务台上限）、Voice Agent（ACD 操作员上限）、API Recording Cnx（DR-Link 录音上限）、VAA（端口数在 VAA 侧声明）、OPR 三档（OPR 服务器侧声明）；阈值在 WBM "Opex Licences" 菜单维护：ACD Operators 0-2800、DR-Link recordings 0-15000、4059 attendants 0-1000（p403）。
  conditions: 阈值下降时 LMS 核对消耗低于新值（p369）
  tags: [rule, opex, consumption, thresholds]

- id: p31
  title: OPEX 许可映射规则（spadmin 帮助口径）：tandem 副机不占、软话机占双份、DSU/DSS 各一份、客房与客人各一份 Room
  type: rule
  source_pages: p370, p398-399, p403
  source_chapter: OXE SYNCHRONIZATION WITH LMS / Help LMS licenses / Items controlled
  source_quote: |
    "For a twinset or multi-device, only one Voice Enterprise license is required for the main set ...
    If a device with the flag enabled is added as secondary device, the flag is disabled, and a
    license freed at LMS level ... For Desk Sharing feature to be operational, both DSS and DSU must
    have the OPEX activation flag enabled • For a hotel with management by guest, the OPEX activation
    flag has to be enabled on both rooms and guests" (p370)
    "Tandem/multi-devices - Without softphone: one license "Voice Enterprise" is needed - With
    softphone : two licenses used ... SIP softphone : two licenses used ... DSS/DSU : two licenses
    "Voice Enterprise" are used ... ROOMs : one license "Room for hospitality" is needed
    4059 : device associated to 4059 uses one license "Voice Enterprise"" (p398)
  summary: |
    映射规则（建用户前先对）：tandem/multi-device 无软话机=1 份 Voice Enterprise（主机）；带软话机=Voice Enterprise+ALE Softphone 各 1；SIP 软话机与 IP 软话机同样双份；DSU/DSS 办公共享=两份 Voice Enterprise（双方 flag 都要开）；客房=1 份 Room（且按客人管理时房间与客人都要开 flag、各占一份 Room）；4059 关联设备占 1 份 Voice Enterprise，Attendant 占 1 份（4059 除外）。副机规则：挂为主机副机时其 flag 强制归 0（原本为 1 则许可在 LMS 释放）；从 tandem 移除的副机 flag 保持 0。设备换节点：旧节点减、新节点加（p399 Note）。Agent/Supervisor ACD 站的 OPEX flag 不可启用，登录时消耗 Voice Agent(CCD) 许可（p405）。
  conditions: "OPEX activation"=No 的设备注册被拒：NOE 终端显示 "No license available"（eqstat 可见 License availability: NO，p407）；SIP 终端收 402 Payment required + 事件 5816（p408）
  tags: [rule, opex, license-mapping]

- id: p32
  title: OXE-LMS 同步与启动数值：每 4 小时对账；事件 652/654；失联 30 天 panic；启动按 DB 旧消耗值放行但拒新许可请求
  type: metric
  source_pages: p371-373, p405-406
  source_chapter: OXE SYNCHRONIZATION WITH LMS / CONSUMPTION AT OXE STARTUP / Maintenance
  source_quote: |
    "OXE checks every 4 hours that licenses are synchronized ... If can't update the LMS licenses
    because the max of licenses is reached, the OXE switches in panic mode and the phones display are
    degraded. The incident 652 is sent • If we can't do the synchronization because the LMS is
    unreachable an incident 654 is sent • If for thirty days, we can't do the synchronization, the OXE
    switches in panic mode" (p371)
    "The OXE starts, without restriction, with the consumption values that were stored in its database
    before the reboot. However, it is not possible to perform a management action requiring a license
    request to LMS (user creation, enabling OPEX activation flag on an existing user, …)" (p373)
  summary: |
    数值口径：每 4 小时对账一次；计数不一致且 LMS 满员→panic+652；LMS 不可达→654（含剩余天数），连续 30 天→panic+652；panic 后同步恢复自动解除（653 清除）。启动规则：OXE 无条件以本地数据库旧消耗值启动；但一切需要向 LMS 要许可的管理动作（建用户、对既有用户开 OPEX activation 等）被拒，直到 LMS 可达。LMS 侧需减许可但不可达时对 OXE 无影响，恢复后Regularize。强制同步入口：spadmin 10；读取双方计数：spadmin 11（列含义：可用余量|lms/oxe 各自消耗|全网订阅上限；lms 与 oxe 消耗列必须一致，否则 panic，p397）。
  conditions: LMS/OXE 计数列一致性是 panic 判据（原书两处重复强调）
  tags: [metric, lms, synchronization, incidents]

- id: p33
  title: OXE panic mode 时间线：超订 15 天温和处置 / 45 天全面降级；LMS 失联 30 天按 45 天档执行
  type: rule
  source_pages: p374
  source_chapter: OXE PANIC MODE
  source_quote: |
    "Case 1 : exceeding the subscribed licenses during OXE startup • After 15 days ... If Voice
    Enterprise excess, random de-activation of OPEX activation parameter for users & attendants in
    idle • If Attendant excess, subscription limit is decreased • Any new login is refused for Contact
    Center and any new recording is refused (IP DR-Link) • Nothing is done for Softphone excess •
    After 45 days ... OPEX activation parameter is de-activated for all users and attendants •
    Attendant licenses are setup to 0 • Nothing is done for Softphone excess • Case 2 : Connection
    failure with LMS for more than 30 days • After 15 days, same behavior as case 1’s “after 45 days”
    step" (p374)
  summary: |
    自动行为时间线（管理员未干预时）：超订（启动期发现）——15 天后例行同步中随机停用空闲用户/话务员的 OPEX activation、下调话务台订阅上限、拒 Contact Center 新登录与 IP DR-Link 新录音、Softphone 超订不处置；45 天后全部用户与话务员的 OPEX activation 停用、话务台许可清零、Softphone 超订仍不处置。LMS 失联超 30 天——15 天后即执行上述"45 天档"行为。结论：超订越久处置越狠，Softphone 超订始终靠商务解决；运维要把 654 事件的剩余天数当作硬告警。
  conditions: panic 解除条件=同步恢复 OK（p371）
  tags: [rule, opex, panic, timeline]

- id: p34
  title: 其他应用的 LMS 校验周期与失联后果：8770 每夜/VAA 午夜/O2G 12h/OPR 24h；30 天宽限后各自失效方式
  type: metric
  source_pages: p375
  source_chapter: OTHER APPLICATIONS
  source_quote: |
    "For OV8770: Right to manage the associated OXE(s) is checked every night during the daily
    synchronization with OXE • For VAA: The license items value is checked every night at midnight ...
    For O2G: The license items consumption value is checked every 12 hours • For OPR: The license
    items value is checked every 24 hours after the last start of OPR" (p375)
    "30-days grace period, during which services ... stay operational ... On the grace period expiry:
    • OXEs systems are de-activated on the OmniVista 8770 ... • VAA or VNA licensing service is
    stopped ... • O2G goes in panic mode : APIs are no longer accessible • OPR goes in inactive state" (p375)
  summary: |
    校验周期：OV8770 每夜随与 OXE 的每日同步核查管理权；VAA 每夜 0 点（端口数在 VAA 服务器侧声明作阈值）；VNA 周期性核查；O2G 每 12 小时；OPR 启动后每 24 小时（许可在 OPR 服务器侧声明作阈值）。失联宽限：30 天内各服务保持运行（O2G 处于 qualifying 模式不许新会话）；期满后果分产品——OV8770 上的 OXE 系统被停用（同步关闭、配置与设备管理不可用、无 OXE 告警）；VAA/VNA 许可服务停止（应用失效）；O2G 进 panic（API 不可访问）；OPR 转 inactive（不能录音、管理界面不可用）。
  conditions: VNA "911/urgency call" 用量需 SIP 中继按并发 911 呼叫数配置（p364）
  tags: [metric, lms, applications, grace-period]

- id: p35
  title: C2P 范围与件号规则：排除 OPR/ALE Connect/Selfcare/VNA/API Management；3EYxxxxxAA↔3EYxxxxxMA；OT-SBC 仅维护订阅
  type: rule
  source_pages: p376-377
  source_chapter: COMMUNICATIONS SUITE FOR MLE TO PURPLE ON DEMAND TRANSFORMATION
  source_quote: |
    "Any product included in Purple on Demand offer, except OmniPCX Record, ALE Connect, Selfcare, VNA
    and API management • Any other applications must be removed from ACTIS configuration before
    launching C2P transformation • Either not included in PoD (Dispatch Console, SoftPanel , OTFC,
    IQ Messenger) or in phase-out (OTMS, OTMC, OTBE, OV4760, ICS, …) • Note that IP Premium Security
    solution is not handled by PoD and must therefore be removed before performing C2P" (p377)
    "PoD subscriptions: part number in 3EYxxxxxAA C2P subscriptions: part number in 3EYxxxxxMA" (p377)
  summary: |
    规则五条：(1) C2P 覆盖 PoD 目录内产品，但排除 OmniPCX Record、ALE Connect、Selfcare、VNA、API Management；(2) PoD 未含或停产应用（Dispatch Console/SoftPanel/OTFC/IQ Messenger；OTMS/OTMC/OTBE/OV4760/ICS 等）须在转换前从 ACTIS 配置移除；(3) IP Premium Security 不在 PoD 范围，转换前必须移除；(4) 每个 PoD 订阅有对应 C2P 折扣件号（3EYxxxxxMA 对 3EYxxxxxAA），服务相同仅价格不同，优惠以既有系统能力为上限；OT-SBC 例外只需 C2P 维护订阅（无 C2P setup 订阅）；(5) 转换范围外的 add-on 走 MyPortal 常规 PoD 件号、无转换折扣；转换下单即定局。
  conditions: 版本基线见 framework f29
  tags: [rule, c2p, part-numbers]

- id: p36
  title: FlexLM 管理口径：.ice 入 /opt/Alcatel-Lucent/data/licenses；FTP 禁用走 SFTP/SCP；端口 27000；getaluid/lmutil 工具链
  type: checklist
  source_pages: p280-282
  source_chapter: Post-Installation Wizard / Appendix: Flexlm management
  source_quote: |
    "The file hosted on the FlexLM server must contain the following information: ­ The identifier
    specific to the "server/client": dongle ID or MAC address or ALUID ­ OXE product ID ... Copy this
    license file into the directory /opt/Alcatel-Lucent/data/licenses ... Restart the FlexLM server
    # systemctl restart flexlmd" (p280)
    "For security reasons, the standard "FTP" protocol cannot be used on the GAS server. Transfer the
    license files using the "SFTP" (Secure FTP) protocol, or "SCP" ... The login/default_password to
    connect to the FlexLM server are "root/letacla1"" (p269)
  summary: |
    操作口径：FlexLM 许可文件（.ice）须含服务器/客户端标识（dongle ID 或 MAC 或 ALUID）+ OXE 产品 ID，复制到 /opt/Alcatel-Lucent/data/licenses 后 systemctl restart flexlmd（或 stop/start），status 核对 active (running)。GAS 上禁用标准 FTP——用 SFTP/SCP（admin 账号传 /tmp 再 root mv）。工具链：getaluid 查服务器 ALUID；lmutil lmhostid -flexid 读加密狗 ID；lmutil lmstat -a 核服务器状态与许可占用；日志 /opt/Alcatel-Lucent/logs/flexlm/（核验详情 flexlm_lmlog.log）。OXE 侧配置（System/Licenses Review/Modify）：FlexLM Licensing Enabled=Yes、Flex Server IP=GAS IP、端口 27000、Product ID discovery=Yes——改完 OXE 必须重启（p282 Warning）。
  conditions: FlexLM 凭证 root/letacla1 为默认口径须改；vSphere thick client 仅到 ESXi 6.0（p199）
  tags: [checklist, flexlm, gas, licensing]

- id: p37
  title: SW 版本命名公式：N420536a 分解 + ISO A.B.XXX.000 / zip A.B.XXX.YYY + R101.1-n4.205-36-a-fr-c83 全串读法
  type: formula
  source_pages: p53, p47, p103, p119
  source_chapter: GENERALITIES / SOT UPDATE / siteid 输出
  source_quote: |
    "N: Product line (eg: N=R100) 4: Option in the line (e.g: R101.1) 205: Software version
    36: Static patch # a: Dynamic patch identification N420536a" (p53)
    "R101.1-nY.YYY-Y-fr-c83 Business identification: R101.1 Release: DELIVERY nY.YYY Patch
    identification: Y Dynamic patch identification: none Country: fr Cpu: c83" (p125)
  summary: |
    三套命名互相咬合：(1) 软件发布名 N420536a——N=产品线（R100 系）、4=线内选项（R101.1）、205=软件版本、36=静态补丁号、a=动态补丁标识；(2) SOT 媒体名——ISO=A.B.XXX.000（末 000 即 ISO），zip=A.B.XXX.YYY（YYY 为 zip 序号，XXX 为所基于 ISO 序号）；SOT 更新版末 3 位非 000；(3) siteid/swinst 全串 R101.1-n4.205-36-a-fr-c83——业务标识-交付-静态补丁-动态补丁-国家-CPU 类型；ACD VERSION 另行显示 release/bug_fixing/protocol_id。实验演示链：patch 0（Linux 601.007）→19（601.012）→36（601.017），实验口径。
  conditions: 补丁累积规则见 p06
  tags: [formula, versioning, naming]

- id: p38
  title: 实验口径：RLAB 节点地址/账号/密码总表与默认口令清单
  type: metric
  source_pages: p10-19, p13-19, p190, p257, p272
  source_chapter: TRAINING LAB ENVIRONMENT（各节点表）/ 各 How-To 默认凭证
  source_quote: |
    "PC CLIENT PC-CLIENT-PODX 192.168.1.9 255.255.255.0 192.168.1.254 Administrator superuser" (p10)
    "GAS server gas 192.168.1.45 ... root letacla1 ... WebRTC gateway webrtc 192.168.1.15 ...
    rainbow Rainbow123" (p19)
    "You can connect with the following login/password (by default) to the "OMS" VM: ­ admin /
    letacla1 or root / letacla1" (p272)
  summary: |
    实验口径总表（RLAB 专用，生产必须替换）：网段 192.168.1.0/24、网关 192.168.1.254、DNS 192.168.1.250、NTP 192.168.1.252、代理示例 192.168.1.253:3128、SIP 模拟器/NAS 12.0.0.2。节点：PC Client 192.168.1.9（Administrator/superuser）；SOT VM 192.168.1.130（admin/upload；letacla→Superuser2580*）；SOT VM hosted 192.168.1.230；ESXi root/Superuser-X*（X=POD 号）；CS3 csa/csm 192.168.1.101/103（mtcl/swinst/root→Superuser2580*）；KVM host 192.168.1.55（root/superuser）；KVM 上 OXE 192.168.1.201/203、OMS 192.168.1.213（letacla1→Superuser2580*）；GAS 192.168.1.45（root|admin letacla1；kb/kb 键盘）；GAS 上 OXE 192.168.1.1/1.3、OMS 192.168.1.13、WebRTC VM 192.168.1.15（rainbow/Rainbow123）。工具默认：SOT FTP upload/sot（SFTP 端口 2222）；OXE swk 恢复路径 /usr4/BACKUP/OPS。GAS 加载约 60 分钟、后安装约 15-20 分钟（培训环境，p254/p270-271）。
  conditions: 全部为实验口径；X=POD 号
  tags: [metric, lab, credentials, network]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 20 项任务清单的覆盖情况

| task | 任务 | 是否有原则/数值类条目 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | RLAB 环境 | 有 | p38 | 节点地址/账号/密码总表 |
| task-02 | 部署 SOT VM | 有 | p05, p04, p38 | 首连安全规则、网络一致性规则 |
| task-03 | 更新 SOT | 有 | p03 | 同主版本/双文件/功能同级 |
| task-04 | Template Factory | 有 | p02 | 8CPU/16GB/500GB 与 50GB 降级 |
| task-05 | 媒体与项目 | 有 | p37, p38 | 版本命名公式、upload/sot 通道 |
| task-06 | 单版本加载 | 有 | p01, p37 | 密码 9 条规则、版本全串读法 |
| task-07 | 多版本与切换 | 有 | p07 | N3 迁移硬规则约束多版本适用域 |
| task-08 | 补丁安装 | 有 | p06, p37 | 静/动顺序律、累积包含 |
| task-09 | 分发器模式 | 有 | p06 | full/static 强制 inactive 属补丁规则域（流程见 f14/c05） |
| task-10 | 虚拟化平台决策 | 有 | p10, p11 | 平台矩阵、许可路径矩阵 |
| task-11 | OXE VM 加载 | 有 | p08, p10 | 规格模板四档、虚机免 MAC |
| task-12 | OMS 加载 | 有 | p09 | 120 通道/240 台/Lock 384-385 |
| task-13 | GAS 加载 | 有 | p12, p14, p38 | 硬件前置表、IP 需求 |
| task-14 | GAS 后安装 | 有 | p14, p16 | IP 清单、host 升级/UPS 规则 |
| task-15 | GAS 运维 | 有 | p15, p16, p36 | gasversion/gasbackup、FlexLM 工具链 |
| task-16 | DNS/代理与连通性 | 有 | p17 | 443/80/53 清单与 FQDN |
| task-17 | FTR 与 PIN | 有 | p18, p19, p20 | ID 语法、FTR 行为、PIN 规则 |
| task-18 | RTR 启用与监控 | 有 | p11, p21, p22, p23, p24 | 资格期数值、状态阈值、事件码、重试口径辨析 |
| task-19 | PoD 许可下载 | 有 | p28 | 项目/许可池规则（Active 判据与路径见 f30/c17） |
| task-20 | PoD 配置与 LMS 同步 | 有 | p27, p29, p30, p31, p32, p33, p34 | lock 431、目录 24 项、消耗归属、同步/panic 时间线、应用周期 |

**覆盖结论**：20/20 全部有对应条目，无缺口。三点口径说明：
1. task-19 的许可池/项目规则由 p28 覆盖，下载路径（菜单级）在 framework f30 与 case c17。
2. p22 显式记录了教材内部关于 RTR 重试行为的口径差异（p304/p308 vs p332），未强行统一，留待 ALE 最新文档裁决。
3. 所有数值（30 天/+0.5/-1、27/20 天邮件、4 小时、90 秒、120/240、50 并发、7000/12000 用户、1,500,000 用户、0-2800/0-15000/0-1000 阈值等）均逐格对照原文；密码规则忠实于原文（OXE 14 字符 vs SOT 8 字符是两套体系，未混写）。
