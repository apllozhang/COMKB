# 框架/流程/结构候选 — OpenTouch Suite for MLE (OPENXTE300EN Ed10, R2.6.1)

> 提取器: framework-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
>
> 覆盖范围：章节推进逻辑、端到端流程、操作菜单路径、组件关系图示、平台/界面分区。实验环境给定值（IP/密码/账号/号码）一律标注"实验口径"。

```yaml
- id: f01
  title: 全书课程推进逻辑——方案概览 → 实验环境 → 装机初始化 → 许可 → 集成声明 → 业务供给 → 安全客户端 → 运维
  type: flow
  source_pages: p3-10, p38-51, p128-154, p186-254, p255-396, p397-513, p514-603
  source_chapter: 全书章节顺序（Solution Overview / Training lab / Installation / SOT / Licensing / Declarations & SIP / Users & Voice mail / Certificates & Clients / Maintenance & Rehosting）
  source_quote: |
    "OpenTouch™ Multimedia Services (OTMS) is dedicated to large market" (p5)
    "OTMS deployment main steps (1) ◼Software installation ... ◼Post-installation Wizard" (p50)
    "The following objects will be modified after a re-hosting procedure: IP addresses, Name, F.Q.D.N." (p560)
  summary: |
    课程按十段推进：①OTMS 方案概览（组件/虚拟化/交付模式）；②培训实验环境（RLAB POD、混合教室、SIP 模拟器、Pod Configuration 实验）；③安装概览（手动 DVD/ISO 与 SOT 三路线 + 部署主步骤）；④SOT 工具专章（模式/配置/媒体/项目）；⑤初始化（OVF 导入、Post-installation wizard、系统连接、SUSE 界面）；⑥许可（机制、检查、外部 FlexLM、切换）；⑦集成声明（OXE 声明、OT 声明、告警、OXE SIP、prior management）；⑧用户与语音业务（档案/用户/WPC、本地存储邮箱、IMAP、通知、通用公告）；⑨安全与客户端（证书、OTC PC/One、多终端、监督组）；⑩运维（维护、备份、rehosting + TC2149 附录）。这是实际交付项目的推荐顺序：先地基后闸门（许可），先集成后业务，最后安全与运维。
  conditions: 无特殊版本前提；各章版本前提在对应条目中标注
  tags: [flow, course-structure, delivery-order, master-flow]

- id: f02
  title: OTMS 组件架构图——ICAS/ICM/AMS 三组件与 8770/OXE 的分离部署
  type: diagram
  source_pages: p5-7
  source_chapter: OpenTouch Suite for MLE / Solution Overview / Architecture
  source_quote: |
    "OXE and 8770 components are on separated servers" (p6)
    "Media Server characteristics (AMS) ● An audio video mixer (MCU) for • Video switching or Ad-hoc
    Conferencing (3 to N party conferencing) • Audio mixing ... Voice Codec: G711 / G729 /G722
    Video Codec: H264" (p7)
    "Multi-media SIP Core functions (SIP server) ● SIP based communication server for SIP endpoints
    • Make, take, clear reject calls • Fowarding" (p7)
  summary: |
    架构三块：①OTMS Server（SUSE Linux）承载 OpenTouchServer 三组件——AMS（媒体服务器：MCU、视频切换/临时会议 3-N 方、混音、预约会议、放音控制、语音编解码 G711/G729/G722、视频 H264）；ICM（多媒体 SIP 核心：SIP 端点的接/打/挂/拒/转发等）；ICAS（即时通信与协作服务：按姓名呼叫、电话在场、状态、收藏、IM、共享）。②OXE call server（呼叫处理）与 8770 Server（Windows OS）各自独立部署。理解点：Mule 是 AMS 的 SIP 服务器别名（语音邮件接入端口 5040），ESS（ICM 的 SIP 服务器）接入端口 5260——这是后续 SIP 外部网关两条的来由。
  conditions: 组件名 ICASICM AMS 为原文连排（ICAS、ICM、AMS 三个组件在一页）
  tags: [diagram, architecture, otms, icas, icm, ams]

- id: f03
  title: OTMS-v 虚拟化布局——ESXi 上六类虚机
  type: diagram
  source_pages: p8-9
  source_chapter: Solution Overview / Virtualisation / OTMS delivery modes
  source_quote: |
    "OTMS-v ... Vmware ESXi 8770 VMOXE VM OMS VM ... DCS VM ... OTMS VM ... OTFC VM (Windows OS Fax Server)" (p8)
    "VMware ESXi (6.5 and 7.0.x) Microsoft Hyper-V (2016 & 2019) OTMS-V up to 5000 users" (p9)
    "Operating system Suse Linux Enterprise Server 12 SP 5" (p9)
  summary: |
    OTMS-v 在一台虚拟化宿主（VMware ESXi 或 Microsoft Hyper-V）上承载：8770 VM（Windows OS）、OXE VM（Linux OS，呼叫处理）、OMS VM、DCS VM（Windows OS，Office pack）、OTMS VM（SUSE，ICM/ICAS/AMS）、OTFC VM（Windows OS，传真服务器）。版本口径：ESXi 6.5 与 7.0.x、Hyper-V 2016 与 2019；OS 为 SLES 12 SP5；OTMS 与 OTMS-v 均上限 5000 用户；物理服务器由 BP 或客户提供（非 ALE 提供）。
  conditions: HW platform 标注 "not provided by Alcatel-Lucent Enterprise"；OTCP 工具用于核对硬件平台兼容性
  tags: [diagram, virtualization, otms-v, esxi, hyper-v]

- id: f04
  title: 培训实验环境结构——RLAB POD（纯虚拟化）与混合教室两形态 + 实例参数总表
  type: structure
  source_pages: p10-25, p14-16
  source_chapter: Training lab environment / Fully Virtualized (RLAB only) & Hybrid mode / POD CONFIGURATION / Settings
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a
    data center." (p12)
    "Common ressources 10.20.30.x Training platform 10.20.30.254 External DNS ... NAS: softs,
    licenses, … SIP simulator Subnet 192.168.1.x" (p14)
    "OXE OPEN_OXE_STARTER csa (physique) csm (principal) 192.16.8.1.1 192.16.8.1.3 ...
    OPENTOUCH OPEN_OTMS_STARTER opentouch 192.168.1.50 ... 8770 OPEN_8770_STARTER nms 192.168.1.70 ...
    SOT OPEN_SOT sot 192.168.1.230" (p16, 实验口径)
  summary: |
    两形态：Fully Virtualized（RLAB only，无教室设备）与 Hybrid mode（RLAB + 教室设备 MIX484 GD4、ALE-300/500/20h/30h 话机、POE Switch、PC Classroom）。POD 网段 192.168.1.x，公共资源区 10.20.30.x（NAS 软件/许可、SIP 模拟器、外部 DNS 10.20.30.254/250）。实例参数总表（实验口径）：OXE csa 192.168.1.1 / csm 192.168.1.3（表格印作 192.16.8.1.x 为原文排版）；OMS 192.168.1.13；FLEXLM flex 192.168.1.80；OTMS opentouch 192.168.1.50；8770 nms 192.168.1.70；SOT sot 192.168.1.230；ECOSYSTEM eco 192.168.1.100；PC Client 10/11 = 192.168.1.10/11；混合模式另有 PC Classroom 192.168.1.9、GD4 192.168.1.12。账号口令（实验口径）：OXE mtcl/mtcl、swinst/SoftInst；OMS、FLEXLM root/letacla1；OTMS root/superuser（课堂改 superuser）；8770 adminnmc/Superuser01*；PC/ECO Administrator/superuser。PC Client 10 预装 2 个 MicroSIP 模拟公网号码；每台 PC 有 NAS 网络盘。
  conditions: 全部 IP/口令为实验口径；POD 间独立、共享公共资源
  tags: [structure, lab, rlab, pod, topology, lab-credentials]

- id: f05
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则
  type: diagram
  source_pages: p26-30
  source_chapter: SIP Carrier Simulator / Overview / Public numbers / Examples / Call to your PBX
  source_quote: |
    "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... ITSP1 Public gateway public.itsp1.com
    10.20.30.50 ... SIP domain: sip.itsp1.fr" (p27)
    "PBX (POD P) Id: pbxP password: alcatel ... Public numbers: Id: publicP@itsp1.fr password: public" (p27)
    "Dialed number: 0110312345 Number sent by the PBX: +33110312345" (p29)
    "POD P PBX installation nb 3321PN ... DDI table - First external nb 41000 ... First internal nb
    31000 Range size 500" (p30)
  summary: |
    模拟器在 RLAB 公共区扮演出局运营商：SIP 网关 gateway1.itsp1.com（10.20.30.51，SIP 域 sip.itsp1.fr，PBX 注册账号 pbxP/alcatel）与公网网关 public.itsp1.com（10.20.30.50，SIP 域 itsp1.fr，Public/Emergence 两个 SIP 用户由 PC Client 10 的 2 个 MicroSIP 扮演）。号码规则：PN 为两位 POD 号；全国 33{1-5}1PN12345、移动 3361/3371PN12345、国际(英) 4421PN12345、紧急 112/15/17/18；Public 主号码 3321PN12345；呼出时 PBX 把 0110312345 变换为 +33110312345 送出。呼入本 PBX：安装号 3321PN41000，DDI 首外线 41000 / 首内线 31000 / 号段 500（例：31001 外线号 3321PN41001）。
  conditions: 实验口径（RLAB 专用）；所有账号/号码/IP 为教学约定值；ITSP2 仅在拓扑图出现无细节
  tags: [diagram, sip-trunk, simulator, numbering, lab]

- id: f06
  title: 软件安装三路线决策——手动 DVD / 手动 ISO / SOT 自动化
  type: flow
  source_pages: p40-47
  source_chapter: Installation Overview / Deployment overview / Manual installation / Installation thanks to S.O.T.
  source_quote: |
    "Manual installation ... O.S. installation from DVD ... OpenTouch core installation thanks to iso
    files ... or ... Automatic installation thanks to S.O.T. (Software Orchestration Tool)" (p40)
    "Such kind of installation based on manual processes can provide mistakes and inconvenient ...
    Several DVDs to burn • DVD burning errors • DVD medium – DVD drive incompatibility • Manual
    process requiring a permanent human presence" (p43)
    "Optimized methodology Concept based on a "enhanced PC-installer" tool running on a virtual
    machine ... All ISO files automatically mounted Silent installation process (including hotfixes)
    Additional tools provided ... DNS server DHCP server HTTP server" (p46)
  summary: |
    交付物：Boot DVD（SUSE OS）、OpenTouch core 安装包、hotfix、许可文件，从 BPWS 下载。三路线：①手动全 DVD——烧多张盘，易错（烧录错误、介质/光驱不兼容、全程人守、无静默）；②手动 ISO——只烧 bootdvd 装 OS，其余 ISO 拷 USB 硬盘挂载，仍需人工值守、非静默；③SOT——"增强版 PC 安装器"虚机：自动挂载全部 ISO、含 hotfix 静默安装、附带 DNS/DHCP/HTTP 服务器工具；输入为配置（IP、FQDN）、许可、ISO、hotfix，目标机 PXE 网络启动。生产推荐 SOT。
  conditions: 软件从 BPWS 下载；SOT 一次只部署一台（p53）
  tags: [flow, deployment, sot, manual-installation, decision]

- id: f07
  title: SOT 工具结构——两模式 × 两配置 × 两工作模式
  type: structure
  source_pages: p53-65
  source_chapter: Software Orchestration Tool / Introduction / Stand-alone / Hosted / Default / Template Factory / Use principle / Expert mode
  source_quote: |
    "S.O.T. VM can be used in 2 different modes « Standalone » mode « Hosted » mode ... S.O.T. VM can
    be installed in 2 different configurations « default » configuration « Template Factory »
    configuration" (p54)
    "Installed on technician laptop thanks to Virtual Box client (version 5.2.24 minimum) or VMware
    workstation (version 14 minimum)" (p55)
    "Deployed in a vSphere ecosystem : ESXI server version 6.0 minimum" (p56)
    "8 CPUs / 16Go memory size / 500Go for the second disk ... Vmx flag ... USB controller available" (p59)
    "Two working modes Easy Kind of wizard ... Expert Management of medias and projects ... are
    independents" (p61)
  summary: |
    SOT 以 ISO（sot-x.x.xxx.xxx.iso，内含 .ova）交付，补丁为 sot-update zip。使用维度：①运行模式——standalone（技师笔记本 VirtualBox ≥5.2.24 / VMware Workstation ≥14，主要部署物理机）或 hosted（vSphere/ESXi ≥6.0，可生成 OVF 模板部署其他虚机，Template Factory 除 OpenTouch 外可用）；②配置——default（softwareOrchestrationTool.ova）与 Template Factory（softwareOrchestrationToolWithTemplateFactory.ova，第二硬盘 500GB、8 CPU/16GB、VMX flag、USB 控制器；启动时自检或 templateFactory 命令查缺失项）；③工作模式——easy（向导：产品类型→媒体→目标）与 expert（Projects/Medias/External storage/Settings 四页；媒体先于项目声明；媒体库三类：Windows server、NFS server、SOT 本地存储；支持 .iso 整版、.zip 补丁、.ice/.mao/.swk 许可）。SOT 自 3.0 起可用 zip+MD5 补丁升级（限同主版本）。Web 界面 https://SOT-IP，账号口令登录。
  conditions: 虚机规格细节见 SOT Delivery note；Template Factory 对 OpenTouch 产品不可用（p56）
  tags: [structure, sot, deployment-tool, modes, template-factory]

- id: f08
  title: OTMS 部署主步骤链——装机 → 重启 → 向导 → OXE → 8770 → 8770 配置 → OXE 管理
  type: flow
  source_pages: p50-51
  source_chapter: Installation Overview / OTMS deployment main steps (1)(2)
  source_quote: |
    "◼Software installation ⚫S.O.T. required configuration ... ◼Reboot ◼Post-installation Wizard
    ⚫OpenTouch configuration (local settings) ⚫OpenTouch Core settings Accounts ... License
    installation OpenTouch license file (.ice) ⚫System update (upgrade)" (p50)
    "◼OXE installation or upgrade ... ◼8770 installation or update ... ◼8770 configuration ⚫OXE node
    declaration ⚫OpenTouch node declaration Account(s) declaration ◼OXE management ⚫User profile for
    Conversation users SIP device ⚫SIP configuration SIP trunk group External gateway" (p51)
  summary: |
    端到端主链：①软件安装（SOT 配 IP/FQDN、bootdvd+core ISO、hotfix、许可可选）→②重启→③Post-installation wizard（本机设置、核心账户、.ice 许可、系统升级；账户会自动建于 OT 但还要在 8770 的 OT 节点声明里回填）→④OXE 安装或升级（可用 SOT）+ 许可→⑤8770 安装或更新（SOT 或 DVD）+ 许可→⑥8770 配置（声明 OXE 节点、声明 OT 节点并填账户）→⑦OXE 管理（Conversation 用户画像 SIP device、SIP 配置：trunk group、外部网关等）。这条链就是整本书第二到第七部分的组织轴。
  conditions: 向导在 OT 服务器首次开机自动启动（p48）
  tags: [flow, master-flow, deployment-steps, otms]

- id: f09
  title: Post-installation wizard 结构——两模式入口与十个配置节
  type: structure
  source_pages: p88-108
  source_chapter: OTMS Post-installation wizard (How-To) / Contents
  source_quote: |
    "The post-installation proposes two modes: Installation from scratch or From an existing archive" (p89)
    "1.1 Configure local settings 1.2 Network settings 1.3 High availability 1.4 OpenTouch core
    settings 1.5 Advanced Communication Server 1.6 Licenses settings ... 1.7 Certificate 1.8 Backup
    configuration 1.9 Summary overview 1.10 System update" (p88)
  summary: |
    向导在 OT 首次开机自动启动，两种入口：from scratch（十节顺序：本机设置 键盘/国家/公司/时区+DST → 网络参数 主机名小写强制/IP/掩码/网关/域/DNS/NTP → 高可用保持 Disable → OT 核心账户 root/维护 otuser/管理员 otAdmin/模板 otProfile/SNMP + 四类语言 → ACS 栈名与节点 ID → 许可（FlexLM 本地/外部 + .ice 文件）→ 证书（Network security ON 内部 CA SHA256 或外部 PKCS12 / OFF 通用 CTL）→ 备份（NFS 10.20.30.40 /mnt/db/backup/podX 实验口径）→ 汇总核对 → 系统更新（无补丁选 NO）→ Finish 启动 OT 服务）；restore from archive（选本地 /tmp 归档，键盘/root/维护账号，许可可借机更新，其余同尾段）。恢复路径中归档里的旧许可会一并恢复，升级后可换新。
  conditions: 实验归档放 /tmp（实验口径）；HA 仅限 R2.2.x 迁移场景启用（见 principle）
  tags: [structure, post-installation, wizard, otms]

- id: f10
  title: 系统连接通道结构——VM 控制台 / SSH(Telnet) / 远程桌面 三通道 + 账号总表
  type: menu-path
  source_pages: p109-121
  source_chapter: Connections to the system (How-To)
  source_quote: |
    "Accounts reminder System Login Default password Classroom password Esxi server root ... OpenTouch
    root ... otuser ... OmniPCX Enterprise mtcl mtcl ... swinst SoftInst ... adfexc ... OmniVista 8770
    Windows OS Administrator ... 8770 adminnmc superuser Superuser01*" (p111)
    "Telnet is not authorized on the OpenTouch server. You have to establish a SSH V2 connection using
    Putty" (p113)
    "Telnet is authorized on the OXE server." (p117)
  summary: |
    三通道：①VM 控制台——vSphere 客户端（root/letacla，实验口径）右键 Open Console（R-Lab 用浏览器 web 控制台）；②命令行——OT 走 SSH v2（Putty，端口 22，UTF-8，otuser/maintenanceuser；横幅显示 Product: OpenTouch™ Multimedia Services 2.6.1, Version 18.0.100.003），OXE 走 Telnet（端口 23，mtcl/mtcl；启用安全后须换 SSH），IP 核验用 ifconfig -a 与 netadmin -m；③远程桌面——8770 服务器（mstsc，192.168.1.70，nms\\administrator；先在系统属性开允许远程连接，可映射本地盘与即插即用设备）。SUSE 界面（p122-127）：startx 起图形、桌面右键 Open in Terminal、最多 4 个 workspace（示例三个：终端、/opt/Alcatel-Lucent、/var/data/licenses）、YaST 管时区键盘、Log Off 退出。
  conditions: 账号表为"出厂默认 vs 课堂"双列（实验口径）
  tags: [menu-path, connections, ssh, telnet, rdp, accounts]

- id: f11
  title: 许可体系结构——三族文件、两种锚定物、FlexLM 内嵌/外部两形态
  type: structure
  source_pages: p128-154
  source_chapter: Licensing / License files principle / Non virtualized server / Virtualized server / Licenses files deployment / Files description
  source_quote: |
    "OpenTouch license file: <OT license>.ice • OmniPCX Enterprise license file: software.swk
    <OXE license>.ice if OXE-v (Flexlm control) Note: OXE can use also Cloud Connect to control its
    licenses • OmniVista 8770 license file: xxx.sw8770" (p130)
    "The ALUID is a unique 128 bits identifier based on hardware characteristics of the server ... For
    virtualized deployment, the ice license file is linked to a hardware dongle (Aladdin) plugged on
    the server" (p131)
    "License_release Examples: 10 for OpenTouchR2.4 11 for OpenTouchR2.5" (p154)
  summary: |
    结构四层：①文件族——OT 用 <OT license>.ice；OXE 用 <offer ID>.swk（专有加密；物理机 CPUID 验证，OXE-v 用 FlexLM 或 Cloud Connect 验 Product ID）+ OXE-v 专属 .ice；8770 用 .sw8770（在 OT/Flex 服务器侧改名 nmc.license，8770 handle 与 OXE .swk 内 handle 对应）。②锚定物——物理机 ALUID（128 位硬件标识，getaluid 读取）；虚拟化一律加密狗（Aladdin USB dongle 的 Dongle-ID）。③FlexLM 形态——内嵌 OT 服务器或外部 FlexLM 虚机（端口 27000）；OXE 侧只验 Product ID（ProductID discovery=Yes、Use Flex License=No，容量仍看本地 .swk）。④目录流转——向导/手动把 .ice 放入 $LICENSES_HOME（内嵌 /var/data/licenses，外部 /opt/Alcatel-Lucent/data/licenses），Flexlm 服务启动时复制改名到 final_licenses（命名 ALUID_xxx/FLEXID_x-xxx/SERVERMACADDRESS_<if>/ANY_license.ice），OXE 的 .ice 进 final_licenses/oxes；alchostid.cfg（OTID 节流文件）用于 OT-v 外部 FlexLM 场景；OTEC 双 OT 各有 OT1/OT2 ID。许可文件内 License_release 对应版本（10=R2.4，11=R2.5）。
  conditions: 虚拟化产品 ID 也可写进 OT 许可（Case 2）； dongle 必须挂在承载 FlexLM 的虚机上
  tags: [structure, licensing, flexlm, aluid, dongle, ice, swk]

- id: f12
  title: OXE 声明流程（8770 侧）——前置准备 → 网络子网节点三级建树 → 同步
  type: flow
  source_pages: p186-192
  source_chapter: OmniPCX Enterprise declaration (How-To)
  source_quote: |
    "Name used when the CPU role is main: csm Address used when the CPU role is main: 192.168.1.3 ...
    17.'Node Setup' ... Enter the node name? oxe" (p187)
    "Warning DON'T FORGET TO APPLY THE MODIFICATION BEFORE TO LEAVE: 20. 'APPLY MOFIFICATION'" (p187)
    "Subnetwork – Node number Enter a numeric value equal to the ABC network*100 + OmniPCX Enterprise
    node number. Example: With an ABC network number = 1 and node number = 1, you must enter 101" (p190)
    "Execute a Complete -> Separate synchronization of the OmniPCX Enterprise." (p191)
  summary: |
    三段：①OXE 侧准备——netadmin -m 核对 csa/csm 地址（192.168.1.1/192.168.1.3 实验口径）、Role addressing 建主角色名 csm、Node Setup 设节点名 oxe，离开前必须选 20 'APPLY MODIFICATION'（原文拼作 MOFIFICATION）；mgr/Webadmin 的 System/Review-Modify 设 Node Number 与 Network Number（节点 101 = 网络 1 + 节点 1；siteid 命令或提示符前缀核验）；打开 47xx directory – 4400 Synchro = True 让目录变化实时推 8770。②8770 建树——Configuration 应用：右键 Create Network（Logical-Network，号 1）→ 子网（ABC-Subnetwork，号=OXE 网络号）→ OmniPCX 4400 Enterprise 节点（名称、Subnetwork-Node number=ABC 网络×100+节点号、主 IP、FTP adfexc/adfexc、Process configuration 勾选、Alarm reception mode=Permanent IP connectivity、Process directory 勾选；spatial redundancy 时两个主 IP 右键 Add a Value）。③同步——OXE 节点右键 Synchronization，Complete → Separate；日志 C:\\8770\\log\\NMCSyncLdapPbx_1.log；同步后 OXE 下生成各分支；最后查 Configuration/Data Collection 的 Date of last modification。
  conditions: 实验口径 csm=192.168.1.3；同步类型矩阵见 principle
  tags: [flow, oxe-declaration, nmc, netadmin, synchronization, menu-path]

- id: f13
  title: OpenTouch 声明流程（8770 侧）——bics.conf 取凭证 → 双向声明 → 拓扑互挂
  type: flow
  source_pages: p193-203
  source_chapter: OpenTouch server declaration (How-To)
  source_quote: |
    "OpenTouch information can be found in the file bics.conf on the OpenTouch server: HOST_NAME=
    "opentouch" ... ICE_USERNAME="otAdmin" ... ICE_TEMPLATEUSERNAME="otProfile"
    ICE_MAINTENANCEUSERNAME="otuser"" (p194)
    "Node number is a free number. This node number must be different than OXE node numbers existing
    in the OXE network. (Use 99 for example)." (p196)
    "System services/ Topology/ OXE CS/ OXE CS network/ OXE CS subnetwork/ OXE CS ... Port 2570 (OXE
    PRS port number) ... Codec Select the compression algorithm used for inter domain calls: This
    parameter must be the same as the one declared on the Call Server" (p199-201)
  summary: |
    四段：①准备——读 /var/data/bics/bics.conf 取 HOST_NAME/HOST_DOMAIN（拼 FQDN）、otAdmin（8770 配置用）、otProfile（模板管理用）、otuser（维护/备份/SSH 用）；OT 侧 nslookup 验 OXE 的 csm/oxe FQDN 正反向解析；密码遗忘时 otAdmin/otProfile 可经 WBM（System services/Security/Administrator → Modify → Passwords → GUI Password）互改，otuser 用 passwd otuser。②声明 OT 节点——nmc 中在 OXE 同子网右键 Create → OpenTouch：Name、Subnetwork-Node number=99（自由号，不得与 OXE 节点号冲突）、FQDN、otAdmin/口令、Enable notifications=True、Process configuration/directory；Connectivity 页签填 otProfile；Maintenance 页签填 otuser/maintenanceuser。③OT 侧挂 OXE——OT 配置工具 System services/Topology：建 OXE CS network（Logical-network，1）→ subnetwork（ABC-subnetwork，1）→ OXE CS（Display name、Node FQDN oxe.company.com、Main FQDN csm.company.com、主 IP、端口 2570 OXE PRS、FTP adfexc、Node Identifier 1、PRS=Presentation Service – opentouch；CAC IP link 页签 Codec G729 必须与呼叫服务器压缩参数一致）。④同步验证——OT 节点右键 Synchronization（对 OT 节点 Partial 与 Complete 等价）；同步后 OXE 出现在 OT 的 Topology 分支下；站点名在 Users and devices > Site 配置。
  conditions: OT 必须与 OXE 呼叫服务器同子网声明；DNS 正反向解析是硬前提
  tags: [flow, ot-declaration, bics-conf, nmc, topology, menu-path]

- id: f14
  title: OXE SIP 配置流程——trunk group → 本地网关/代理/注册器 → 外部网关 10/11 → trusted → 全局
  type: flow
  source_pages: p226-234
  source_chapter: OmniPCX Enterprise SIP configuration (How-To)
  source_quote: |
    "Trunk Group ID Enter the trunk group number. It must be unique on OmniPCX Enterprise Trunk Group
    Type Select "T2" type ... T2 Specification Select SIP" (p227)
    "SIP/ External Gateways Creation ... Gateway Number Enter the SIP external gateway number ("10"
    in our example) ... Port number 5260 ... Gateway type ICE type" (p231)
    "2.4.2. SIP gateway to reach the voice mail The SIP server of the Media Server (called "mule")
    has to be declared as an external SIP gateway. ... Port number 5040 ... Outbound calls only True" (p232)
    "SIP/ Trusted IP Addresses Creation ... Trusted address Enter the IP address of the OpenTouch
    server (e.g. 192.168.1.50)" (p233)
  summary: |
    五段（8770 的 OXE 配置应用内操作，亦可用 mgr）：①SIP trunk group——ID 10、名 SIP、类型 T2、Q931 信号 ABC-F、Remote Network 用空闲且不同于 OXE 网络号、T2 Specification=SIP；本地参数 End-to-end dialing/DTMF end-to-end 均 No；Virtual accesses for SIP 默认 2。②SIP 本地网关——子网号 10、trunk 10、端口 5060、Subscribe Min Duration 600、DNS 本地域 company.com、DNS 192.168.1.254（实验口径）；SIP Proxy 认证 Digest + 仅认证来话；Registrar Min expiry 600。③外部网关两条——10 号 To_OT→OT SIP server：Remote domain=OT FQDN、端口 5260、TCP、Supervision timer 380、归属 trunk 10、认证 None、Gateway type=ICE type、Support CSTA User-to-User Yes；11 号 TO_VM→Mule（语音邮件）：端口 5040、Outbound calls only=True；OXE spatial redundancy 时 Belonging domain 与 Contact with IP address 两字段的填法不同（指向 TC1652）。④Trusted addresses——加入 OT 服务器 IP。⑤全局——System/Other System Param./Compression Parameters 设 G729（Multi. Algorithms False）；Translator/Prefix plan 建 DPNSS 前缀；Routing Optimisation=Yes。
  conditions: 实验口径 trunk=10/GW=10,11/DNS=192.168.1.254；spatial redundancy 有专章（TC1652）
  tags: [flow, sip, oxe, trunk-group, external-gateway, menu-path]

- id: f15
  title: Prior management 全景——号码段/前缀/语音邮件/拨号规则/UDAS/会议桥六块
  type: structure
  source_pages: p213-225, p235-254
  source_chapter: System prior management (讲义) / Prior management (How-To)
  source_quote: |
    "Range of numbers from 31000 to 31499 (including users, voice mail, attendants, …) are declared
    belonging to OXE." (p216)
    "Dialing rule(s) are used to add automatically the outbound prefix when an external call (by name
    or number) is performed." (p220)
    "UDAS is a module that receives requests from phone client or software searching for contacts
    information stored on OpenTouch server" (p223)
  summary: |
    六块结构：①号码段——OT 的 OXE 声明级 Ranges 页签建 31000-31499（含用户/留言/话务台/缩位号）；架构图口径 ICM(ESS) 端口 5260、AMS/Mule 端口 5040、语音邮件 TUI 31200、会议 31250/31260，外部语音邮件 31200→GW2、31250→GW1。②前缀服务——System Services/Applications/Telephony/Telephone Prefixes：溢出忙/无应答/无应答或忙/取消、路由管理（立即前转）、Join or leave group（监督组进出）、CLIR、话务台前缀；建议与 OXE 同值（法国默认 51/52/53/54/41/9）。③语音邮件——Topology/VMS 验 Local Storage 类型；OT 侧 TUI application 的 Voice Mail 索引=31200；OXE 侧 Applications/External Voice Mail 建 31200→外部网关 11、Subscription on registration Yes。④拨号规则——dialingRule 1：外呼前缀 0 或 9、最小长度=拨号计划长度+1、例外长度；按名呼打全客户端自动加前缀、按号呼打仅 OTC PC/Mobile（客户端下载规则文件）、话机/视频终端须手拨前缀；会议走 DAS Rules。⑤UDAS——internalDir（OT 目录）+ phonebookDir（OXE 话簿）两张同步表进 PostgreSQL 同步库，检索只查同步库；同步日期/时间/周期必须设置且周期 ≥1。⑥ACS 会议——OT TUI application 建 Conferencing 31250（英）/31260（法，各语言一条）；OXE 侧 External Voice Mail 对应两条走外部网关 10；会议服务器管理台（WBM → Users and devices/Conference server）：System options（国际 00/国内 0/国码 33/邮件中继 eco.company.com）、SIP Proxies（出站代理 OT IP:5260，用户 31700/31710 自动生成）、DAS rules（法国十条、顺序重要）、Phone formatting rules（5 位拨号计划正则）。
  conditions: DAS rules 与前缀默认值为法国制式示例；ACS 管理走专用 Web 界面而非 8770 客户端
  tags: [structure, numbering, prefixes, dialing-rules, udas, conference, das]

- id: f16
  title: 告警对接拓扑——OT SNMP agent → 8770 SNMP server（Inform v3）→ MIB 重载
  type: flow
  source_pages: p204-212
  source_chapter: Alarms - OpenTouch (How-To)
  source_quote: |
    "Browse to Ecosystem Right click on IT server Select Create > SNMP server ... Port 162 The SNMP
    server receives notification (Inform request) on port 162. Trap transmission filter ... NO_FILTER
    sends all alarms" (p206-207)
    "The Alarms management service (ams) must be restarted to take into account SNMP configuration.
    ams is controlled by the omp service" (p207)
    "The first time the MIB is downloaded from the OpenTouch to the OmniVista 8770 Server, it is not
    retrieved completely." (p209)
  summary: |
    流程五段：①OT 侧 SNMP agent（向导已建 AdminSNMP/adminsnmp，引擎 ID 自动，接收口 161）；②OT 侧建 SNMP server 对象（Ecosystem → IT server → Create → SNMP server：FQDN nms.company.com、端口 162、trap 过滤 NO_FILTER/MAJOR/CRITICAL、SNMP v3、通知类型 Inform），改完 service ompd stop/start 重启（含 ams）；③8770 侧 OT 节点配置——OT 页签 Alarm monitoring=True，Connectivity 页签 MIB 路径 alarm-mgnt/mib/ICEAlarmMgnt.mib、catalog alarm-mgnt/catalog/ICEAlarmsCatalog.xml、V3 用户/口令/SHA/AES 128/privacy、引擎 ID 自动拼装（落盘 c:\\8770\\data\\config\\netsnmp\\snmptrapd.conf）；④MIB 重载——首次下载不全：删 C:\\8770\\data\\config 的 ICE 目录 → 重启 NMC Alarm Server 服务 → 重启 OT 的 ompd → Alarms 树出现 OT 图标；⑤验证——SSH 停 lama 服务（service lamad stop）→ Alarms 应用收到 minor 告警 → start 后自动恢复；日志：OT 侧 /opt/Alcatel-Lucent/logs/omp/ams/ams.log（Sending inform … to host nms.company.com on port 162），8770 侧 \\8770\\log\\NMCFaultManager_1.log 与 NMCFaultManager_ICEService_1.log。
  conditions: SNMP 口令 ≥8 字符；实验 AdminSNMP/adminsnmp 为实验口径
  tags: [flow, alarms, snmp, mib, menu-path]

- id: f17
  title: 用户与档案体系结构——Users 应用分区、三类用户、双侧档案与 ACU 生成原理
  type: structure
  source_pages: p255-271, p272-278
  source_chapter: Users application (讲义) / User profiles creation (How-To)
  source_quote: |
    "Create voice and applications users on one single screen with few parameters ... Import/export
    user data (mass provisioning) Associate device to user" (p257)
    "This is a directory user - Without any node properties (no device and no applications) - Located
    in the 8770 Company directory ... User has one or more OXE devices - Can have access to OpenTouch
    applications" (p258)
    "OXE User Profile OpenTouch User Profile OpenTouch Voice Mail Profile ... OpenTouch Connection
    ACU: Advanced Communication User" (p264)
    "Only profile modification is allowed via Users application. Creation and deletion must be done
    via OXE or OpenTouch configuration application" (p278)
  summary: |
    结构：①Users 应用四区——Users 页签（公司目录树 + 用户符号：Connection user 有设备 / Directory user 无设备）、Profiles 页签（按服务器分列的档案，可在 Users 应用内改）、Properties 属性区、Directory 树（只能在 Directory 应用配置）。②三类用户——type=None 纯目录用户；type=OXE 无 OT 权（Applications=None）；type=OXE + Applications=OT 的 Connection user（ACU）。③档案三件套——OXE profile（OXE 配置工具建：Set function=Profile、号码用 A0000 式占号、Profile Name 大写；开启 System > Other System Param > Use profile with auto. recognition 才能从档案建用户；8770 实时收事件不需同步）+ OT profile（OT 配置工具 Users and devices/User/Profile：General 页 Category=ACU-OXE、TUI/GUI 语言、时区、部门、Dialing rules；Licenses 页勾 Desktop/Voice mail/Conferencing 等；建完需完整同步才出现在 8770）+ 语音邮箱档案（Advanced/Classic/Simplified）。实验建 BASIC(A0000)/EXECUTIVE(A0001，VM=31200) 与 Basic-Connection/Executive-Connection。④权限边界——Users 应用只能改档案，建删必须回 OXE/OT 配置工具。
  conditions: OT profile 建后需完整同步；OXE profile 走实时事件
  tags: [structure, users, profiles, acu, connection-user]

- id: f18
  title: 用户创建操作流——Directory 建树 → 三类用户逐个建 → 存量加 OT → 移树
  type: flow
  source_pages: p279-288
  source_chapter: Users creation (How-To)
  source_quote: |
    "In order to simplify the labs with simple passwords for the users, security settings must be
    modified: Password minimal length: 5 Trivial passwords (GUI, TUI, SIP) allowed" (p281)
    "THESE MODIFICATIONS ARE DONE HERE FOR A LAB CONTEXT AND ARE NOT RECOMMANDED AT ALL ON SITE." (p281)
    "TUI password ... Available characters are digits (6 digits minimum). Passwords composed of a
    logical series of digits (for example: 12345, 65432 or 13579) are refused by default." (p286)
  summary: |
    四段：①目录建树——Directory 应用在根（Ale）下建分支，实验用户全部放 Training；同时把 OT 密码策略放宽（System services/Security/Password management：密码最小长度 5、允许 trivial GUI/TUI/SIP 口令——仅限实验）。②建用户——Users 应用右键分支 Create user：Directory user（type=None，Carini Claire）；OXE 用户无 OT 权（Alban Alan、31050、BASIC、IPTouch 8068、Applications=None）；Connection user（Adams Alice、adams@company.com、31051、IP Touch 8068、EXECUTIVE、Applications=OT、OT instance=OpenTouch、login adams、GUI 12345、TUI 54321、Site1、OT user template=Executive-Connection、Voice mail server=defaultVmsLS、VM profile=Classic）。③存量加 OT——选 Barkley/Backman 补 Email、Applications=OT、login/口令/Site/OT template（Backman 另配 defaultVmsLS/Classic）；建完在 OT 侧核 General/Contacts/Mailboxes 与 Voice Mail Box 档案。④移树——把用户移动到 France\\Brest\\Training 层级。
  conditions: TUI 口令 6 位纯数字且拒绝顺序数列；GUI 口令字母数字；实验口令 12345/54321 为实验口径
  tags: [flow, users, creation, directory, menu-path]

- id: f19
  title: Web Provisioning Client 供给流程——前置四查 → 登录 → 三页签建 Connection 用户
  type: flow
  source_pages: p289-301
  source_chapter: Web Provisioning Client (讲义 + How-To)
  source_quote: |
    "Enable end-customers to easily process repetitive users Moves, Adds, Create, Delete (MACDs) from
    a single interface ... Available from OmniVista 8770 3.2.8 with Unified management license" (p290)
    "Only support of Chrome versions from 54 ... Restrictions: Management of profiles from OXE/OT
    Configuration • No creation of new OpenTouch Conversation users • Association of one device" (p292)
    "Launch the Web Provisioning Client via the following URL: https://nms.company.com ... Login:
    adminnmc Password: Superuser01*" (p298, 实验口径)
  summary: |
    流程：①前置四查——OXE 档案在机（Users 过滤 SetFunction=Profile）、OXE 空闲号段（System > Free Numbers Ranges List）、OT 档案 Category=ACU OXE、全部档案已上 Users 应用（OT 档案需完整同步）。②登录——Chrome 打开 https://<8770 FQDN>（或 /nmclient、:8443/nmclient）→ NETWORK MANAGEMENT 应用 → adminnmc/Superuser01*（实验口径）。③建用户——左树选部门 → + → Users 页签（type OXE、称呼对 OT 用户强制、姓名、邮箱）→ OXE Rights 页签（OXE、号段内分机或自动、Station type、OXE profile、Key Profiles、OT applications 启用）→ Application 页签（OT 名、Login、GUI/SIP/TUI 口令、OT site、OT user profile、Voice Mail type/server/profile）→ Devices 页签（核对话机；启用 Smartphone right 时另配移动设备四参）→ Save。
  conditions: WPC 不能建新 Conversation 用户、只能关联一台设备、档案管理仍在配置工具
  tags: [flow, wpc, provisioning, menu-path, chrome]

- id: f20
  title: 语音邮箱管理体系——默认系统 → 建箱挂人 → 许可 → 管理员/最终用户两侧定制
  type: flow
  source_pages: p302-337
  source_chapter: Voice mail: Local Storage (讲义) / Voice mailbox configuration (How-To)
  source_quote: |
    "Voice messages are stored in a directory structure, in wav format, on OpenTouch server Messages
    are stored in an uncompressed format Readable from any IMAP client" (p304)
    "Before validating the mailbox creation, it's mandatory to assign a profile to the voice mailbox,
    in the « configuration » tab." (p330)
    "A user can activate a maximum of 2 alternative greetings, only when the administrator has granted
    you the rights to use them." (p333)
  summary: |
    流程：①核默认系统——Services/Topology/VMS 的 defaultVmsLS 类型 Local Storage（默认已建；UM 须另行声明且两者可共存）。②建邮箱——Users and devices/Voicemail box 右键 Create：General 页（Display name <username>VoiceMailBox、Type Local Storage、系统 defaultVmsLS）+ Configuration 页必须先选档案（advanced 等）才能保存；再到 User 的 Mailboxes 页签搜 "VMB" 关联并 Apply。③许可——User 的 Licenses 页签勾 Voice mail。④管理员侧——Greetings 页签（问候类型、Extended absence-on、授权 2 条备选问候）；Configuration 页签（Addressing by name、Automatic reading、Delete confirm、Fax、档案）；问候语上传走 WBM → Users and devices/Voice mail greetings management（Greeting Manager 无数量上限：上传/激活/下载/删除）。⑤最终用户侧——My Profile（https://OT FQDN，GUI 登录）改问候/answer only/按名寻址/自动读/删除确认；OTC PC 客户端亦可管问候。
  conditions: 邮箱字段 Answer only 等受档案取值约束（Manageable by users / Yes / No）
  tags: [flow, voice-mail, local-storage, mailbox, greetings, menu-path]

- id: f21
  title: 语音邮箱档案结构——默认三档案 + 四页签选项面
  type: structure
  source_pages: p338-344
  source_chapter: Voice mailbox profiles (How-To)
  source_quote: |
    "Profiles called "Advanced", "Classic" and "Simplified", dedicated to Local Storage. "Standard"
    profile is dedicated to Unified Messaging." (p339)
    "Answer only • Yes ... • No ... • Manageable by users (default value)" (p340)
    "Configuration 3 ... Max size per mailbox Quota of the mailbox belonging to this profile in MB. ...
    Aging of new messages Lifetime of unheard messages in days Aging of saved messages Lifetime of
    heard messages in days ... Accessible via IMAP Mailboxes belonging to this profile are accessible
    through IMAP4" (p342)
  summary: |
    入口 /System services/Applications/Messaging/Voice Mail Profile；LS 型默认三档案 Advanced/Classic/Simplified（UM 型另有 Standard）。四页签：General（名称、类型）；Configuration 1（Answer only 三态默认 Manageable by users；Check quota；Announce time received；Skip memo；Direct callback；Callback voice prompt；Limited access 防恶意录音；Extended absence 阻止留言；Record invitation；Keep call in system；Callback sender allowed；留言后选项；录音提示音；Attendant call enabled 即零出）；Configuration 2（最大问候/最大留言/最大现场录音秒数；TUI 口令管理三档：允许改/过期禁改/禁改）；Configuration 3（每箱 MB 配额、新留言/已听留言保留天数、口令到期预警天数、可网络化、可 IMAP）。实验要求新建 my_profile：配额 10MB、问候 5 秒、留言 15 秒、现场录音 15 秒、新留言 15 天/已听 7 天等并实测。
  conditions: 配额仅在 Check quota 启用时生效
  tags: [structure, voice-mail-profile, options]

- id: f22
  title: IMAP 收取语音邮件流程——Outlook 建账号 → 安全对齐 → 验证
  type: flow
  source_pages: p345-352
  source_chapter: Voice Messages retrieval through IMAP (How-To)
  source_quote: |
    "Account type Select "IMAP" Incoming mail server Enter the OpenTouch/OTMC server FQDN (e.g:
    opentouch.company.com ...)" (p348)
    "The "send test e-mail message" test fails, if a SMTP server is not reachable or OpenTouch/OTMC
    FQDN is used as outgoing mail server (OpenTouch server/OTMC (local storage voice mail) does NOT
    act as a SMTP server)" (p350)
    "BY DEFAULT, IMAPS IS ENABLED ON OPENTOUCH SIDE WITH "TLS" SECURITY. ... DON'T FORGET TO RESTART
    THE IMAP FRONT-END SERVICE: service imap4fed restart" (p351)
  summary: |
    流程：①Outlook 建账号——控制面板 Mail → E-mail Accounts → New → 手动设置 → POP or IMAP；收件服务器=OT FQDN、发件服务器填真实邮件服务器（OT 不做 SMTP）、用户名=GUI login、口令=GUI 口令。②安全对齐——More Settings/Advanced 选与服务端一致的加密；OT 侧 System services/Topology/Physical servers/OT component/IMAP4 Front End 核 Connection security 与端口（默认 IMAPS+TLS；改 SSL/无加密须改端口并 service imap4fed restart）。③验证——Test Account Settings：登录 IMAP 应完成；"发送测试邮件"失败属预期（无 SMTP 或误用 OT FQDN）；完成后第二账号收语音留言。
  conditions: IMAP 会话上限见 principle（1000/20000）
  tags: [flow, imap, outlook, voice-mail, menu-path]

- id: f23
  title: 通知体系结构——SMTP/SMS 两条链与配置分层
  type: structure
  source_pages: p353-368, p369-378
  source_chapter: SMTP/SMS notification (讲义) / SMTP/SMS notifications (How-To)
  source_quote: |
    "Notifications are sent through an external SMTP server. There is no SMTP server in the OpenTouch
    solution. This server must be used without authentication and without TLS." (p360)
    "An SMS gateway is required for SMS notifications. ... Only one SMS Gateway can be configured in
    the system" (p363)
    "Notifications are handled by "Scorpio" component. To declare the SMTP server for notification to
    this component, a route has to be declared in VPIM sesssion" (p370-371)
  summary: |
    结构：①SMTP 链——留言→OT（Scorpio 组件）→外部 SMTP（无认证无 TLS、须有真实发件账号）→邮箱；变体：wav 附件+MWI 开关、My Messaging 链接、箱满/近满预警（阈值默认 80%）、回呼发件人；模板在 /var/data/panda/notification4（NotifTemplate_xx.properties，按 GUI 语言）。②SMS 链——OT 发邮件到唯一一个 SMTP-SMS 网关（地址形如 SMS$xxxxx$@company.com）→ GSM；只显示提示，按键回呼留言箱/发件人。③配置分层——全局（System services/Applications/Notification：发件人名/地址、SMS 网关地址、附件上限 2MB、阈值、音频格式 AAC/PCM16/PCM8/G711）；SMTP 路由走 VPIM 会话（Domain company.com、FQDN eco.company.com、端口 25）；用户层（Users 的 Notification 页签九项开关：邮件权/激活/可自助改地址/箱满通知/wav 附件/关 MWI/链接/SMS 权/SMS 激活/目标手机）；最终用户 My Profile Notification。④维护——chameleon/scorpio 服务（chameleond/scorpiod）与日志 /logs/chameleon/chameleon/panda.log、/logs/journal/chameleon.log、/logs/journal/scorpio.log。
  conditions: wav 附件/箱满通知/链接/回呼仅 Local Storage 可用（UM 行为不同，见 p366 表）
  tags: [structure, notification, smtp, sms, scorpio, chameleon]

- id: f24
  title: 通用公告机制——播放时机三选、两种录制、TUI 菜单与 wav 落地
  type: flow
  source_pages: p379-396
  source_chapter: General announcement (讲义 + How-To)
  source_quote: |
    "The general announcement can be played for: External calls in message deposit case • Internal
    calls in message deposit case • Voice mail message consultation" (p382-383)
    "Standard Main Menu 1 2 3 4 5 ... Enhanced Main Menu 1 2 3 4 5 6 General Announcement" (p387)
    "If a wav file is used, it is stored under: /var/data/general_announcement The name must be
    "general_announcement.wav" Format: CCITT A-law 8bits 8kHz mono" (p392)
  summary: |
    机制：①管理员在 TUI global configuration 选播放时机（外部来电留言时/内部来电留言时/留言查询时，可多选；"arrive on AA" 选项已废弃无效果）；②授权——OT 配置 User 勾 "User has right to manage the general announcement"；③录制两路——话机 TUI（授权用户增强菜单 6 → 公告菜单 1 听/2 录/3 停用，录完自动激活）或 wav 文件（管理员传 /var/data/general_announcement，How-To 实操口径为 /var/data/ics-group/general_announcement，同名 general_announcement.wav，删文件或 TUI 停用）；④约束——一次仅一条、新录覆盖、最长 5 分钟、格式 CCITT A-law 8bits 8kHz mono。
  conditions: 仅支持 wav 文件语言；路径两处表述不一致（见 counter-example）
  tags: [flow, general-announcement, tui, wav]

- id: f25
  title: 证书三路线与两条 PKI 流程——security OFF / 自签 / 外部 CA（PKCS7、PKCS12）
  type: flow
  source_pages: p397-429
  source_chapter: Certificats (讲义) / External certificate generation and deployment with Windows CA (How-To) / OpenTouch self-signed certificate (How-To)
  source_quote: |
    "Certificates for the server can be generated from different ways Certificate, generated by a
    certification authority server ... Self-signed certificate ... "Generic" certificate and CTL
    signed by a "generic" device Choice done during installation (security off)" (p400)
    "1- GENERATION OF KEYS PAIR AND CSR ON APPLICANT SERVER 2- CSR IMPORTATION ON CA SERVER
    3- CERTIFICATE AND PKCS7 FILE GENERATION 4- PKCS7 FILE AND CA ROOT CERTIFICATE IMPORTATION" (p406)
    "Once the certificate imported, don't forget to deploy it in order to be used by the system" (p423)
  summary: |
    三路线：①security OFF——安装时选预装通用 CTL/证书（全球同款，不推荐，盗打风险，官方建议外部 PKI）；②自签——WebAdmin Certificate 页 Change server certificate → Internal + SHA256（SHA-1 自 R2.2 弃用），Local PKI 页可补信息（默认有效期 7300 天），换证后必须用 808x 话机重签 CTL（USB 流程），Deploy 后 Web 会话断开属正常；③外部 CA——根 CA 先导入 Server CTL 页（客户端也要信任根），CSR 可在 OT WebAdmin 生成（国家/省/市/公司/部门/邮箱/SHA256）或直接在 CA 做，CA 签发后按 CSR 来源导 PKCS7（无口令）或 PKCS12（带 passphrase），Certificate 页 Change server certificate 导入，最后 Deploy（会话断开正常）。Windows CA 实操：https://eco.company.com/CertSrv → 申请证书 → base64 提交 CSR → Web Server 模板 → 下载 Base 64 证书链。远程接入两案：泛域名证书一张撒三处（OT/OTSBC/反向代理）或每服务器各签。
  conditions: 部署（Deploy）与导入是两步，漏 Deploy 证书不生效
  tags: [flow, certificates, pki, pkcs7, pkcs12, windows-ca, menu-path]

- id: f26
  title: OTC PC 客户端交付结构——安装包/两模式、软电话两路线、多终端五设备规则
  type: structure
  source_pages: p430-459, p460-493
  source_chapter: OpenTouch Conversation for PC (讲义) / OTC PC (How-To) / Multi-devices (How-To)
  source_quote: |
    "2 presentation modes Horizontal or vertical • Two different working modes possible for Connection
    users: OTC PC: full mode for Connection users with « Desktop » right (license) • OTC PC One :
    Freemium mode" (p433)
    "Up to 5 devices with following rules: Main device can be: NOE IP, NOE TDM, IPDSP, SIP(SEPLOS),
    desk sharing (DSU), an OTC PC (PC/Mac) (on SEPLOS) ... Only one remote extension Only one DECT" (p439)
    "MAKE SURE THAT THE DESKTOP LICENSE IS ENABLED FOR THIS USER DON'T GRANT "NOMADIC SIP" RIGHT TO
    THIS TYPE OF USER" (p474)
  summary: |
    结构：①安装——从 https://OT FQDN/opentouch_conversation_update/OpenTouchConversation.msi 下载；前置 .NET Framework 4.5 与 VS C++ 2010 Tools for Office（Outlook 加载项）；Standard 部署自动带 Outlook 扩展、Advanced 自选协作系统；必填内部 FQDN（opentouch.company.com）与远程 FQDN（ot.company.com）。②两模式——Desktop 许可决定 OTC PC（全量：RCC+VoIP+协作）或 OTC PC One（免费：话机伴侣、单线、盲通话只能挂断、无 VoIP/无监督/共享仅 viewer/三个静态路由档）。③使用默认 RCC——不授 Desktop 权即落 One。④软电话两路线——Multi-devices（用户挂 SIP 分机为第二设备 + 关联 OTC PC 设备 <分机>@<OT FQDN>，SIP extension type=Softphone；DM 由 8770 充当，SIP 配置文件落在 /var/data/oamp/cms/DevicesDeployment/MYICPCSIP）或 Nomadic 池（另一培训）。⑤多终端——最多 5 设备；主设备可为 NOE IP/TDM、IPDSP、SIP(SEPLOS)、DSU、OTC PC；副设备另加 DECT、MIPT、REX、OTC smartphone；远端分机仅 1、DECT 仅 1；可同时有 OTC PC+手机；VoIP 不冻结话机；任意设备拨/接/移会话。前置：Phone features COS 开 Ring all Secondary if Main Out of Service；建 Twinset get call / No ringing 两前缀并授权。
  conditions: OTC MAC 无桌面共享/桌面集成/VDI（p443 对比表）；远程安全接入靠 SBC+反向代理（443/8016），VPN 非必需
  tags: [structure, otc-pc, otc-pc-one, multi-devices, softphone, licensing]

- id: f27
  title: 监督组结构——角色/模式/边界与 8770+OXE 前缀配置
  type: structure
  source_pages: p494-513
  source_chapter: Supervision groups (讲义) / Supervision groups (How-To)
  source_quote: |
    "Each group is a set of 2 or more members of the same type ... 40 members maximum per group" (p497)
    "An user can only be declared in one group Group members may be declared on different OXE nodes
    but must be attached to the same OT node (no multi OT)" (p500)
    "Create a supervision group named "Connection_SG" working in regular mode." (p509)
  summary: |
    结构：①定义——管理员建/删/改；组名即标识；同类型成员 2-40 人（Conversation 组或 Connection 组）；每成员角色 Supervisor/Supervised/双职。②能力——监督员看全组话务状态；进出组（logout/login）经 OTC PC/手机/TUI 前缀；工作模式 Regular（被监督者不可见他人）与 Collaboration（OTC PC 专属，被监督者可见全组与富在场；话机上即使组设为 collaboration 也按 regular 跑）；无 OXE 话机侧 OT 监督功能、无视频；与 OXE 监督（话机监督键）无联动，代接走 OXE Direct call pick-up。③交互边界——OXE 呼叫路由优先（立即前转到非监督目标则不被监督）、只监督主号码、Twinset 副站同样被监督、溢出与代接规则见交互表。④上限——500 组、40 人/组；监督链 500-1500 用户系统 4000 条、3000-5000 用户 6000 条。⑤配置——OT 配置 Features/User groups/Supision group 建 Connection_SG（Name+Mode）→ 右键 Add 成员勾 Is Supervisor/Is Supervised；前缀：OT 侧 Telephone prefixes 的 Join or leave group 值 + OXE 侧同名 External Voice Mail（走 ICM 网关）；Direct call pick-up 前缀建在 OXE Translator/Prefix plan 并在 Phone Facilities Categories 启用。
  conditions: Direct call pick-up 前缀仅 Connection 用户组需要；专用许可不存在（监督本身免费）
  tags: [structure, supervision-group, limits, prefixes]

- id: f28
  title: 运维工具三通道 + 备份体系 + rehosting 矩阵
  type: structure
  source_pages: p514-578, p579-602
  source_chapter: Maintenance (讲义) / Maintenance tools (How-To) / Backup and Restore (讲义+How-To) / Re-hosting (讲义+How-To) / TC2149 附录
  source_quote: |
    ""otconsole.sh" Available since R2.2 ... Tool (menu) providing access to the main useful commands:
    2 sub-menus Easy administration menu Advanced Administration menu" (p519)
    "The aim of the Maintenance Portal is to simplify ... the BP has the possibility to use a GUI ...
    https://<OpenTouch server FQDN>:4448" (p520-521)
    "Automatic backup done every day at 00:01 Full backup on Sunday Incremental backup on other days
    Saved in "/var/backup/daily" folder and named "fqdn.yyyy-mm-dd-hh-mm.zip"" (p541)
    "TC 2149 for OTMS, OTMC, OXE & 8770 rehosting" (p561)
  summary: |
    三块结构：①维护三通道——原始命令（getaluid/lmutil/tsa_maintenance/getVersion/checkAll.sh/ot-config.sh；listtool.sh 按用途列全部脚本）+ otconsole.sh 菜单（R2.2 起，Easy/Advanced 两级）+ Maintenance Portal（WebAdmin 或 :4448，含 AppGuard Control Center；normal/expert 两种显示）。示例链：DNS 核查 checkdns → otconsole 1-2-7 → Portal Troubleshooting；日志收集 dla.sh（按 feature 如 Presence 收集，产物 /logs/dla）→ otconsole 1-5-1（需 root）→ Portal Log/Dynamic Logs Activation。②备份体系——OT：ot-config.sh --storage 定位（本地/USB[须 FAT32/NTFS/EXT3，prepareUsbdisk -f]/NFS；OT-V 无本地须挂 NFS，USB 无意义）→ otbr.sh backup|restore host|mah(moh)；自动备份每日 00:01（周日全量其余增量，/var/backup/daily/fqdn.yyyy-mm-dd-hh-mm.zip）；OXE 用 swinst（/DHS3dyn/BACKUP/IMMED 的 mao-dat/mao-acc）；8770 用 8770 Maintenance（C:\\8770_ARC\\8770Backup）；三者都可从 8770 网络维护工具发起；OT-V 另可 vSphere 整虚机备份。③rehosting——ot-config.sh --rehost（同向导，改 IP/主机名/FQDN/DNS/License server；隐藏 --suspend 支持换子网场景；约 25 分钟）；死锁风险与 inactive 分区清除警告；OXE/8770/OMS 与生态（DNS/DHCP/SSO/SNMP/防火墙）按 TC2149 操作矩阵（含 ANNEX 1 外部 SIP 网关迁移七步法：建新网关→8770 导出 SIP 设备→改文件→导入→改档案→删旧网关）。
  conditions: dla.sh 选项 1 须 root；rehosting 前必须有可用备份
  tags: [structure, maintenance, backup, rehosting, tc2149, menu-path]
```

---

## 收尾自检：对照 BOOK_OVERVIEW.md 任务清单（task-01 ~ task-18）的框架类覆盖率

| task | 任务 | 框架类覆盖 | 对应 id | 说明 |
|---|---|---|---|---|
| task-01 | POD 搭建 | 有 | f04, f05 | 两形态结构 + 模拟器拓扑；操作步骤归 case c01 |
| task-02 | SOT 部署 OTMS | 有 | f06, f07, f08 | 三路线决策、SOT 结构、主步骤链 |
| task-03 | OVF 导入 | 有 | f08 | 主步骤链一环；步骤归 case c03 |
| task-04 | Post-installation wizard | 有 | f09 | 两模式十节结构 |
| task-05 | 系统连接 | 有 | f10 | 三通道 + 账号总表 + SUSE 界面 |
| task-06 | 许可安装 | 有 | f11 | 三族文件/锚定物/目录流转 |
| task-07 | 许可核查 | 有 | f11 | 结构含 spadmin/lmutil 锚点；命令细节归 principle |
| task-08 | 外部 FlexLM | 有 | f11 | 内嵌/外部形态与切换（步骤归 case c08） |
| task-09 | 声明 OXE | 有 | f12 | 三段流程 |
| task-10 | 声明 OT | 有 | f13 | 四段流程含 bics.conf |
| task-11 | OXE SIP | 有 | f14 | 五段流程 |
| task-12 | prior management | 有 | f15 | 六块结构 |
| task-13 | 告警对接 | 有 | f16 | 五段流程 |
| task-14 | 档案与用户 | 有 | f17, f18, f19 | 体系结构 + 逐个建 + WPC |
| task-15 | 语音邮箱体系 | 有 | f20, f21, f22, f23, f24 | 管理流、档案、IMAP、通知、公告 |
| task-16 | 证书 | 有 | f25 | 三路线两流程 |
| task-17 | 客户端交付 | 有 | f26, f27 | OTC PC 结构 + 监督组 |
| task-18 | 运维 | 有 | f28 | 三通道 + 备份 + rehosting |

补充说明：
- f01（课程推进逻辑）不对应单一 task，是 18 项任务的组织轴（f08 主步骤链是装机段的主轴）。
- 全部 18 项 task 均有框架类条目覆盖；逐字段数值与实验口径参数留待 principle/case 提取器展开。
- 生产化边界提示（来自 BOOK_OVERVIEW 批判节）：容量规划指向 Delivery note/Features list/Product limits；spatial redundancy 指向 TC1652；SBC/反向代理指向 TC2257/TC2639；rehosting 全量以 TC2149 为准；磁盘镜像 Clonezilla 指向 TC1625。
