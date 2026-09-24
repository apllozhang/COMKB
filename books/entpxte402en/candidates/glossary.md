# 术语/缩写/产品名候选 — OmniPCX Enterprise Loading (ENTPXTE402EN Ed12)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 62 条（concept 29 / role 3 / subscription 7 / product 6 / protocol 9 / resource 8）。PCS/LMS/FTR/RTR 等缩写书中直接给出全称的照录；未给全称的（如 UMC、ELP、ACTIS、PBWS、CCO 等）full_name 字段如实省略，不采信外部知识。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: S.O.T. (Software Orchestration Tool)
  full_name: Software Orchestration Tool（书中展开）
  category: concept
  source_pages: p22-35, p37-48, p189-203
  source_quote: |
    "S.O.T . stands for «Software Orchestration Tool»; it is a solution to deploy ALE products
    (physical or virtualized)" (p22)
    "The S.O.T . core application is rendered through a Virtual Machine containing all necessary
    layers, services and application to deploy ALE International products • DHCP server • FTP server" (p56)
  definition: |
    全书工具主线：部署 ALE 产品（物理或虚拟）的虚机方案，ISO 内含 OVA、自带 DHCP/FTP 服务；
    Standalone（技术员笔记本 VirtualBox/VMware）与 Hosted（ESXi）两种运行模式，default 与
    Template Factory（含降级模式）两种配置，Easy/Expert 两种工作模式。版本兼容查 TC2456。
  alias_or_related: 两模式两配置见 g02/g03；Easy/Expert 见 f05；一次仅一个部署（n01）
  tags: [concept, sot, core]

- id: g02
  term: Standalone / Hosted mode
  category: concept
  source_pages: p23-25
  source_quote: |
    "S.O.T . VM can be used in 2 different modes • « Standalone » mode • « Hosted » mode" (p23)
    "In « Standalone mode » ... Installed on technician laptop thanks to Virtual Box client or VMware
    workstation ... Used to deploy mainly physical servers ... In « Hosted mode » ... Deployed in a
    vSphere ecosystem : ESXI server ... Used to deploy other virtual machine(s)" (p24-25)
  definition: |
    SOT 的两种运行模式：Standalone=装在技术员笔记本（VirtualBox/VMware Workstation），主要用于加载
    物理服务器（OXE CS、GAS 裸机）；Hosted=部署进 vSphere/ESXi，主要用于加载同一虚拟化系统内的
    OXE/OMS 等虚机（或经 Template Factory 服务 KVM 环境）。要求 SOT 与目标机同网段（p24 Note）。
  alias_or_related: 承载 SOT 的两条部署实验 = c01/c09
  tags: [concept, sot, mode]

- id: g03
  term: Template Factory（含 degraded mode 降级模式）
  category: concept
  source_pages: p27-29, p155-165
  source_quote: |
    "The “Template Factory” configuration adds the possibility to create templates (for OTEC solution
    or not) • This configuration uses a second hard disk for the “Template Factory” part." (p27)
    "Enabling Template Factory mode in degraded mode is a workaround of hardware requirements that are
    hardcoded so that you can build OVA on any server or laptop... etc. with fewer constraints." (p156)
  definition: |
    SOT 的第二配置：加第二块盘用于生成 VMware/KVM 虚机镜像模板（.ova/.tgz），标准前置 8CPU/16GB/
    500GB/Vmx 标志/USB 控制器；降级模式只加 50GB 盘、以 templateFactory 命令绕过硬件前置（官方
    支持的 workaround，首页有警告）。生成 KVM 模板流程见 c07。
  alias_or_related: 前置数值见 principle p02；降级流程见 c06
  tags: [concept, sot, template-factory]

- id: g04
  term: Greenfield project
  category: concept
  source_pages: p85, p140, p168, p183, p206, p214, p249
  source_quote: |
    "Greenfield project Checked for a new installation from scratch" (p85)
  definition: |
    SOT 项目类型之一："从零全新安装"；与"对既有产品更新"（Projects listing → update，见 c03/c04）
    相对。Easy 模式第一步先选 Greenfield 再选产品类型（OXE/OMS/GAS）。
  alias_or_related: 项目字段全集见 framework f06（模板内）与 case 各条
  tags: [concept, sot, project]

- id: g05
  term: 多版本加载 (Multi version loading)
  category: concept
  source_pages: p50, p71-77, p93-99
  source_quote: |
    "Multi-version loading allows two versions to be simultaneously installed on the same hard disk •
    Same releases including correction’s patch • Different Releases ... a 2nd version can be set up on
    the Call Server without stopping the telephone application" (p72)
  definition: |
    同一块盘同时驻留两个版本（active/inactive 分区）：可同版本不同补丁，也可跨版本。优势是不停话音
    即可装好第二条版本，切换（重启）才生效，出问题可回退。两分支：复制+补丁（同基础版本）、完整
    加载+数据复制（跨 Linux 版本）。N3 以下机器不适用（n12）。
  alias_or_related: 分区分组构见 g06；两分支流程见 framework f11；实验 c03
  tags: [concept, loading, multi-version]

- id: g06
  term: 双分区 (Active / Inactive partition)
  category: concept
  source_pages: p54-55, p98
  source_quote: |
    "Disk partition with the ACTIVE version • / Active Linux operating system • /usr2 (linked with
    /DHS3bin) Active OXE version ... Disk partition with the INACTIVE version • /root2_d (linked with
    /root2) Inactive Linux operating system • /usr5 (linked with /DHS3bin2) Inactive OXE version" (p55)
    "Press 0 for the active version, 1 for the inactive one or q to quit" (p98)
  definition: |
    OXE 硬盘的目录结构：活动分区（/、/usr2↔/DHS3bin、/usr3↔/DHS3data、/var）+ 公共区（/usr4↔/DHS3dyn、
    /usr7↔/DHS3ext）+ 非活动分区（/root2_d、/usr5↔/DHS3bin2、/usr6↔/DHS3data2、/var2）。swinst 8-2
    查询时 0=active、1=inactive。多版本、分区复制（swinst 3-2）与切换（3-3）的底层模型。
  alias_or_related: /usr4/ftp/Rload 还承载分发器解包物（g08）
  tags: [concept, partition, filesystem]

- id: g07
  term: 静态补丁 / 动态补丁 (Static / Dynamic patch)
  category: concept
  source_pages: p53, p65-66, p100-110
  source_quote: |
    "A static patch (optional) • A dynamic patch (optional)" (p53)
    "Static patch: • They can only be installed with the phone shut down or when installation is on the
    inactive partition ... Dynamic patch: • They can be installed on the active or inactive partition
    with the phone running without disturbing phone operation" (p65)
    "A patch (static or dynamic) includes all of the previous patch corrections" (p66)
  definition: |
    两类补丁：静态补丁必须停话音安装（或装 inactive 分区），装在完整版本之后；动态补丁可在话音运行中
    装 active/inactive，但必须在对应静态补丁之后。补丁累积包含此前全部修正（N420536 含 1-36、
    N420536d 含 a-d）。文件形态 zip（一包一补丁）或 iso（可静+动同装）。
  alias_or_related: 版本命名见 g33；安装实验 c04；downstat 收尾见 n15
  tags: [concept, patch, static, dynamic]

- id: g08
  term: Distributor / Easy Installation（分发器模式）
  category: concept
  source_pages: p111-130
  source_quote: |
    "OXE Call Server can be used as “Distributor”" (p112)
    "2.Expert menu/9.Remote download/10. ‘Local load as distributor of ISO image/ZIP file and
    installation’" (p114)
  definition: |
    客户环境不允许部署 SOT（外部 BP PC/临时虚机被拒）时的替代加载路径：BP 经 FTP 把 ISO/ZIP 传到 CS
    的 /tmpd 目录，OXE 用 swinst 9-10 菜单自己解包安装（Client CPU type DISTRI）。全版本/静态补丁
    强制 inactive 分区；解包物落 /usr4/ftp/Rload 不自动删除需 9-7 清理，/tmpd 源文件自动删除。
  alias_or_related: 操作流见 framework f14 与 case c05；清理误区见 n16
  tags: [concept, distributor, loading]

- id: g09
  term: OXE-V
  category: concept
  source_pages: p131-154
  source_quote: |
    "The OmniPCX Enterprise Call Server software package dedicated to virtualized environment is called
    OXE-V" (p133)
  definition: |
    专用于虚拟化环境的 OXE 呼叫服务器软件包：支持 ESXi/Hyper-V/KVM/Nutanix AHV/AWS 五类平台，
    可全虚拟化、冗余、原生加密、与硬件混合、分支机构、多节点组网六种拓扑；许可经 FlexLM+加密狗
    （仅 ESXi/KVM）或 Cloud Connect。安装=下载 .ovf 模板（含 mdk 文件）→ 部署 → SOT 项目加载。
  alias_or_related: 平台矩阵 g29、拓扑 f16、OMS g10、PCS g11；设计文档 TBE043（g45）
  tags: [concept, oxe-v, virtualization]

- id: g10
  term: OMS (OXE Media Services)
  full_name: OXE Media Services（书中 Lock 384 名称）
  category: concept
  source_pages: p138-140, p177-188, p212-218
  source_quote: |
    "This soft media-gateway provides media processing features of a GD4 board ... 120 VOIP channels
    per OMS 240 OMS per OXE ... Offers a full software solution Natively virtualized OMS software + Suse
    operating system" (p138)
    "Lock 384: ‘OXE Media Services’ ... Lock 385: ‘VoIP channels on OMS’" (p140)
  definition: |
    软媒体网关虚机（OMS 软件+Suse OS），软件替身一块 GD4 板卡：VoIP 编解码（G.711/G.729/G.722/OPUS，
    仅宽带窄带）、转码、会议 3/6/14/29 方、静态/动态语音引导（可录制）、音调、DTMF RFC4733、QoS
    802.1p/DiffServ。每台 120 VoIP 通道、每 OXE 最多 240 台；许可 Lock 384（台数）/385（通道总数），
    均可不停机安装。升级由 OXE CS 经 TFTP 自动下发（同 GD4 流程，p230）。
  alias_or_related: GAS 上限每台 1 台 OMS（n19）；加载实验 c08/c11；omsconfig 命令（c08 步骤 6）
  tags: [concept, oms, media-gateway]

- id: g11
  term: PCS (Passive Communication Server)
  full_name: Passive Communication Server（书中展开）
  category: concept
  source_pages: p147, p297, p308
  source_quote: |
    "Passive Communication Server (PCS) ... Switch from CS to PCS: soft reset (voice calls are released
    but the Virtual Machine is not rebooted) • Switch from PCS to CS: hard reset (Virtual Machine is
    rebooted)" (p147)
    "Cloud Services DO NOT run on Passive Communication Server (PCS)" (p297)
  definition: |
    OXE-V 拓扑中的被动通信服务器：CS 信令链路故障时可接管 OMS（CS→PCS 软复位：释放话音但虚机不重启；
    PCS→CS 硬复位：虚机重启）。注意 PCS 上不跑 Cloud Connect 云服务；但 OPEX 的 lmsagent 会在 PCS
    上运行（g22 的范围辨析）。
  alias_or_related: 辨析见 n39
  tags: [concept, pcs, redundancy]

- id: g12
  term: GAS (Generic Appliance Server)
  full_name: Generic Appliance Server（书中展开）
  category: concept
  source_pages: p219-242
  source_quote: |
    "Generic Appliance Server (GAS) packaging provided by ALE • Operating system: Rocky Linux •
    Virtualized OXE on top of Rocky linux’s KVM layer • Optional WebRTC & OMS virtual machines • FlexLM
    license server directly installed on Rocky linux • Dongle-less package with license control based on
    the ALU-ID of the server or the OXE Cloud Connect ID" (p221)
  definition: |
    ALE 打包的通用设备服务器：Rocky Linux + KVM 底座，承载 1 OXE VM + 1 OMS VM（可选）+ 1 Rainbow
    WebRTC VM（可选，Debian），FlexLM 直接装在宿主 OS；dongle-less，许可基于服务器 ALU-ID 或
    Cloud Connect ID。BP 按硬件前置表自备服务器即可交付；HP DL20 G11 为 ALE 交付机型（仅限 GAS 包）。
    运维三件套 gasversion/gasbackup/uhwconf。
  alias_or_related: 硬件前置 p12、组件规则 n19/n20、部署模式对比 f18、实验 c12/c13；文档 TBE063/TC3138
  tags: [concept, gas, core]

- id: g13
  term: BootDVD
  category: concept
  source_pages: p184, p237, p244-250
  source_quote: |
    "The BootDVD “.iso” file • The OMS software “.iso” file." (p184)
    "Select the “BootDVD” version in the scrolling menu “BootDVD” is the GAS Operating System" (p250)
    "Upgrade to the latest security fixes that are brought along the different versions of bootDVD
    delivered on My Portal" (p237)
  definition: |
    宿主操作系统的引导安装介质（bootdvd_rocky-v.v.v-x86_64.iso）：加载 OMS/GAS 时与软件 iso 一起作为
    SOT 媒体声明；对 GAS 而言 BootDVD 就是它的 Rocky 操作系统；新版 BootDVD 也是 GAS host 打安全
    补丁的载体（SOT "Project for existing products" 或 gas-rocky-update.sh）。
  alias_or_related: host 升级细节见 principle p16
  tags: [concept, gas, oms, media]

- id: g14
  term: Cloud Connect / CCI
  full_name: Cloud Connect Infrastructure（CCI 书中展开）
  category: concept
  source_pages: p283-349
  source_quote: |
    "OmniPCX Enterprise can connect to the Cloud Connect Infrastructure (CCI) after a “First Time
    Registration” (FTR) and benefits from services such as: “Right To Run” (RTR) ... “Inventory” ...
    “Get Offer file” ... “Push offer” ... “Software update” ... “Remote console” ... Fleet Dashboard
    application" (p286)
  definition: |
    ALE 运营的云基础设施：OXE 经内嵌 CC Agent 以 XMPP over WSS(443) 常驻 + SOCKS5(80) 按需连接
    （FQDN connect2.opentouch.com），换取 RTR 许可、Inventory 资产、Offer 推取、远程控制台、软件更新、
    Fleet Dashboard 机队管理等云服务。OXE 出站发起、TLS 1.2、ALE 自有 CA。
  alias_or_related: 连接架构 f20、网络清单 principle p17；FTR g15、RTR g17、Dashboard g19
  tags: [concept, cloud-connect, core]

- id: g15
  term: FTR (First Time Registration)
  full_name: First Time Registration（书中展开）
  category: concept
  source_pages: p292-297, p322-331
  source_quote: |
    "The main goal of the FTR (First Time Registration) is to allow the OXE to automatically retrieve
    the password corresponding to the CC-Product-ID • The OXE must perform a FTR to be fully Cloud
    Connected and operational • It is done by using a temporary product activation account • Each OXE
    has its owns activation account based on CC-Suite-ID" (p293)
  definition: |
    OXE 首次注册 CCI：用基于 CC-Suite-ID 的临时激活账户换取永久凭证（CC-Product-ID+密码，隐藏存于
    OXE 数据库并自动克隆到 twin）。新装机默认自动执行（每 4 小时重试），也可 CCTool 手动；备机禁止
    做；panic 后走 PIN 恢复（g16）。前置：DNS/代理（netadmin）、swk 含 CCSID、电话应用已启动。
  alias_or_related: CCTool 见 g20；FTR/PIN 行为规则 principle p19/p20；实验 c15
  tags: [concept, ftr, cloud-connect]

- id: g16
  term: FTR with PIN code
  category: concept
  source_pages: p298-301, p330
  source_quote: |
    "Following a Panic Flag for RTR, it is mandatory to reinitialize system registration to restore the
    permanent connection to Cloud Connect Infrastructure ... A new temporary activation account will be
    created with a 6 digits (0-9) PIN code and will be provided by helpdesk." (p299)
  definition: |
    RTR panic（无效 FTR 数据/欺诈复制/失联）后的恢复注册：向 helpdesk 申请 6 位 PIN（5 天有效），CCTool
    以"CC-Suite-ID+PIN"重做 FTR；PIN 不落盘、操作在线重置全部云配置、需 RTR+ccagent 进程在跑；
    helpdesk 侧同时删除其他激活账户并断开同 ID 产品。
  alias_or_related: 流程图 f22；行为边界 n30；Duplicated 场景 n31
  tags: [concept, ftr, pin, recovery]

- id: g17
  term: RTR (Right To Run)
  full_name: Right To Run（书中展开）
  category: concept
  source_pages: p302-308, p331-332
  source_quote: |
    "The Right to Run service removes the need for hardware identifiers or dongle USB keys used to
    validate the license. This is also called dongle-less operation ... It acts like an on/off switch
    giving the product the right to run according its license file limits" (p303)
  definition: |
    dongle-less 许可总开关：不用硬件标识/加密狗，每日经 XMPP 向 RTR 服务器应答——OK 加 0.5 天、
    NOK 减 1 天，30 天资格期归零即 Panic Flag（话机显示 "Call your administrator"、拒绝配置变更）。
    不替代产品级 swk 许可；与 FlexLM 模式互斥。Fleet Dashboard 按剩余天数显示四级状态。
  alias_or_related: 资格期数值 principle p21-p23；事件 647-651 principle p24；实验 c15
  tags: [concept, rtr, licensing, core]

- id: g18
  term: Qualifying Period（资格期）
  category: concept
  source_pages: p304, p306, p332
  source_quote: |
    "A grace period of 30 days is initiated by default at the initialization of the RTR service on the
    OXE system • It is referred as the Qualifying Period" (p304)
    "Remaining Qualifying Period = 30.0" (p332)
  definition: |
    RTR 的宽限天数计数器：RTR 服务初始化即给 30 天；每日应答 OK +0.5（上限 30）/NOK -1（下限 0）。
    Save/Restore 跨重启保留、自动同步 twin。Fleet Dashboard 以 29-28/27-10/9-1/0 映射 Connected/
    Qualifying/Soon Blocked/Blocked-Panic 四态（27 与 20 天触发邮件，Soon Blocked 每日邮件）。
  alias_or_related: 重试口径矛盾记录 n35
  tags: [concept, rtr, qualifying-period]

- id: g19
  term: Fleet Dashboard
  category: concept
  source_pages: p310, p338-348
  source_quote: |
    "Fleet Dashboard application • Used for remote monitoring and control • Allows to download OPS
    files, and so on…" (p286)
    "SERVICES GLOSSARY DC Data Collector DOD Data On-Demand FTR First Time Registration POD Push
    On-Demand RTR Right To Run SU Software Update" (p340)
  definition: |
    CCI 上的机队管理应用：RTR 状态列（四级+Not connected/Duplicated）、Inventory 资产盘点、Offer
    推/取（eBuy+offers server）、单会话远程控制台（1 分钟超时、shell.log 审计）、软件更新（AWS 仓库
    临时 URL）、告警展示与推荐版本橙色高亮。服务缩写体系 DC/DOD/FTR/POD/RTR/SU。
  alias_or_related: 操作状态字段 D/I/A/S、P/O/K/F（principle p26）；远程控制台边界 n37；更新边界 n38
  tags: [concept, fleet-dashboard]

- id: g20
  term: CCTool / checkCloudConfig.sh
  category: concept
  source_pages: p293, p314, p328-335
  source_quote: |
    "“CCTool” command used to perform “FTR”" (p293)
    "The connectivity between the CC Agent and Cloud Connect Operation infrastructure can be controlled
    by the script “checkCloudConfig.sh” launched on the OmniPCX Enterprise." (p314)
    "1. FTR status & options 2. RTR status & options 3. Cloud Connect parameters 4. Set Log levels
    0. EXIT" (p328)
  definition: |
    OXE 云连接的两个命令入口：CCTool（mtcl）四菜单——FTR 状态与执行（含 PIN）、RTR 状态与 Force、
    CC 参数（KeepAlive 90s 默认+各 Feature 开关）、日志级别（ERROR/INFO/DEBUG/TRACE）；
    checkCloudConfig.sh 验证 DNS 解析、443 XMPP/WSS、80 SOCKS5 三项连通性。日志体系 ccagent.log
    (/var/log)、ccprocess.log (/tmpd/cloud_cnx/log)、CCAlarm.log (/tmpd)。
  alias_or_related: 菜单结构 f25；事件码 principle p24；实验 c14/c15
  tags: [concept, cctool, diagnostics]

- id: g21
  term: swinst
  category: concept
  source_pages: p53, p98-99, p114, p117-130, p394
  source_quote: |
    "A release of « facilities » (swinst)" (p53)
    "2 - Expert menu • 3 - Cloning & duplicate operations • 2 - Partitions duplication • 2 - Duplicate
    Linux Data" (p98)
  definition: |
    OXE 的软件安装/设施管理 CLI 工具（swinst 账号登录）：Expert 菜单九项含 Cloning & duplicate（分区
    复制/切换）、Backup & restore、OPS configuration、System management（含 NTP）、Software identity
    display、Remote download（分发器加载与清理）。加载后输国家码、启 autostart、恢复许可都在这里。
  alias_or_related: 菜单树 f12；切换后首进需国家码（n12 关联，c03 附录）
  tags: [concept, swinst, cli]

- id: g22
  term: OPEX / Purple on Demand (PoD)
  full_name: Purple on Demand（书中展开，另称 PoD）
  category: concept
  source_pages: p350-380
  source_quote: |
    "In OPEX subscription mode, licenses of elements in OXE system, such as users, attendants, operator,
    rooms, 8770, DR-Link Recording, … are managed through a License Manager Server in the cloud • This
    new feature is also called “Purple on Demand” (PoD)" (p351)
  definition: |
    订阅模式：用户/话务员/话务台/客房/录音等许可由云端 LMS 按项目池管理（硬件仍 CAPEX）；OXE 以
    lock 431=1 开启；订阅目录缩到 24 项（UMC 免费）；计费月付无承诺或预付 1/3/5 年。OXE 每 4 小时与
    LMS 对账，超订/失联有 panic 时间线。迁移入口为 C2P（g24）。
  alias_or_related: LMS g23、消耗类型 f27、目录 principle p29、panic n49；实验 c16/c17
  tags: [concept, opex, pod, core]

- id: g23
  term: LMS / lmsagent
  full_name: License Manager Server（LMS 书中展开）
  category: concept
  source_pages: p351-354, p370-373, p396-398
  source_quote: |
    "Centralized license server to automatize the licenses management • Pool of licenses on a project
    basis ... The “lmsagent” is a new component in OXE • Stateless component, used as technical bridge ...
    Run in all Call Servers : main, stand by, PCS • Read only access on Stand-by CS" (p353)
  definition: |
    云端集中许可服务器：按项目建许可池、自动化消耗/释放、展示消耗水位；OXE 侧 lmsagent 为无状态
    HTTPS 客户端（TLS）做更新与同步，跑在全部 CS（备机只读）；OmniPCX Record 直连 LMS；
    OT-SBC/Selfcare 仍用本地许可文件、ALE Connect 用自有云。事件 6250/6251/6252、652/653/654。
  alias_or_related: 同步决策树 f28；数值 principle p32；计数器读法 n56
  tags: [concept, lms, lmsagent]

- id: g24
  term: C2P（CAPEX to PoD 转换）
  category: concept
  source_pages: p376-378
  source_quote: |
    "OXE CAPEX installed base transformation program to Purple on Demand: C2P • New tool available on
    MyPortal to ease this transformation ... Main objective is to build a new PoD project, based on
    existing software locks and system configuration" (p376)
    "PoD subscriptions: part number in 3EYxxxxxAA C2P subscriptions: part number in 3EYxxxxxMA" (p377)
  definition: |
    CAPEX 存量转 PoD 的转换计划：MyPortal 工具基于既有软件锁与系统配置生成 PoD 项目（五步：准备→
    校验→导出 JSON→调量→购物车，下单即定局）；C2P 订阅件号 3EYxxxxxMA（PoD 为 3EYxxxxxAA）、同服务
    折扣价；排除 OPR/ALE Connect/Selfcare/VNA/API Management；OT-SBC 仅维护订阅。
  alias_or_related: 流程 f29；边界 n51/n52；产品版本基线 p378（OXE Purple R100.1+ 等）
  tags: [concept, c2p, transformation]

- id: g25
  term: OPEX activation（flag）
  category: concept
  source_pages: p368, p370, p399, p407-408
  source_quote: |
    "The license is not consumed when the user is created, but when it is activated (OPEX Activation
    user parameter)" (p368)
    "A new flag related to OPEX mode is displayed for users ... Warning IN CAPEX MODE THIS NEW FLAG IS
    DISPLAYED BUT NOT TAKEN IN ACCOUNT" (p399)
  definition: |
    OXE 数据库中每个用户/设备的 OPEX 激活旗标：激活时才向 LMS 要许可、停用释放且保留配置；tandem 副机
    强制归 0；Desk Sharing 要求 DSU/DSS 双开；酒店按客人管理时房间与客人双开。CAPEX 模式显示但不生效。
  alias_or_related: 映射规则 principle p31；许可拒绝表现 n58
  tags: [concept, opex, flag]

- id: g26
  term: 项目（PoD Project）
  category: concept
  source_pages: p355, p383-384, p396
  source_quote: |
    "Associated to an end-customer and opportunity • Each project is associated to only one end-customer
    and only one Business Partner ... Maximum 1,500,000 users per project • The subscriptions, purchased
    for a given project, are shared by the systems/applications of this project" (p355)
  definition: |
    PoD 的商务组织单元：一项目=一终端客户+一 BP；可含多台 OXE 与应用、上限 1,500,000 用户；订阅池项目内
    共享、跨项目不可移；购物车启动即创建、可追加 add-on；MyPortal 下载许可与 LMS 建池都以项目为前提，
    状态必须 Active。
  alias_or_related: 规则 principle p28；下载路径 c16
  tags: [concept, pod, project]

- id: g27
  term: 信任主机 / IP tables (Trusted hosts)
  category: concept
  source_pages: p34, p92, p117, p250, p265, p324-325, p347
  source_quote: |
    "Log as “root” and manage security (IP tables)" (p92)
    "Choose 2. 'Add a trusted host' ... Trusted host's IP address ? 192.168.1.9" (p325)
    "“cdn-oxe-sw-update.al-enterprise.com” domain must be part of them" (p347)
  definition: |
    OXE 的防火墙白名单机制（netadmin 11-1-3 管理，支持单主机/网段/域名/批量导入导出）：分发器传输、
    swinst 远程恢复、gasbackup 连 OXE 都要求源 PC/服务器在白名单内；GAS 的 OXE 信任主机可由 SOT 项目
    CSV 批量导入（Firewall_Rules_gas.csv）；云端软件更新要求放行 cdn-oxe-sw-update 域名。
  alias_or_related: CSV 旅程 n25
  tags: [concept, security, iptables]

- id: g28
  term: autostart / RUNTEL
  category: concept
  source_pages: p58, p63, p70, p92
  source_quote: |
    "Automatic starting up if autostart is set in swinst • Manual starting up under mtcl with command
    RUNTEL" (p58)
    "Enable the “Autostart”, in the “swinst” menu, for the future reboots" (p70)
  definition: |
    电话应用的启动策略：swinst 菜单里设 autostart 后每次开机自动起电话应用；未设时以 mtcl 登录手动执行
    RUNTEL 启动。加载/补丁/切换流程的收尾步骤都要核对它（SOT 项目里 Enable Autostart 参数可联动）。
  alias_or_related: 启动相位图 f09
  tags: [concept, autostart, telephony]

- id: g29
  term: 虚拟化技术矩阵（ESXi/Hyper-V/KVM/Nutanix AHV/AWS）
  category: concept
  source_pages: p134-136
  source_quote: |
    "VMware ESXi (1) 8.0 7.0 ... Microsoft Hyper-V 2022 2019 2016 (2) ... KVM kernel ≥ 4.12.14 & KVM ≥
    5.2 (3) ... Nutanix (AHV) 20230302 20220304 (except OST64) ... AWS (except OST64)" (p134)
  definition: |
    OXE-V 认证的五类虚拟化平台及其版本口径（Ed12 时点）：ESXi 8.0/7.0；Hyper-V 2022/2019/2016
    （CS=gen1、OXE-MS/OST64/EEGW=gen2）；标准 KVM（RHEL/SLES/Proxmox 等，定制 KVM 如 AHV 需专项
    认证）；Nutanix AHV 20230302/20220304；AWS（均 OST64 除外）。许可路径随平台而定（n17）。
  alias_or_related: 数值 principle p10；文档 TBE043/TC3142en-Ed01
  tags: [concept, virtualization, matrix]

# ── 二、角色 (role) ──

- id: g30
  term: BP (Business Partner)
  full_name: Business Partner（书中展开，如 "Business Partner Contact Manager"）
  category: role
  source_pages: p294, p355, p376, p382, p112-113
  source_quote: |
    "Software delivery to Business Partner" (p294)
    "Each project is associated to only one end-customer and only one Business Partner" (p355)
    "If you do not have credentials, contact your Business Partner Contact Manager or ALE
    representatives to request an access." (p382)
  definition: |
    全书交付动作的执行者：软件交付（FTR 链条）、分发器模式的 ISO/ZIP 传输、GAS 平台自备与安装、
    PoD 项目唯一关联方、版本切换责任人（云端软件更新只管传输）、MyPortal 访问申请入口。
  alias_or_related: ALE representatives = 无凭证时的另一申请对象（p382）
  tags: [role, bp]

- id: g31
  term: Helpdesk / ALE Technical Support
  category: role
  source_pages: p299-300, p346
  source_quote: |
    "System administrator has to request a temporary activation account from the helpdesk ... will be
    provided by helpdesk." (p299)
    "ALE Technical Support specifies for each release the current recommended version" (p346)
  definition: |
    两个支持角色：helpdesk 负责 FTR with PIN 的身份核验、6 位 PIN 签发（5 天有效）与同 ID 产品断开；
    ALE Technical Support 负责 Fleet Dashboard 上每个 release 的"推荐版本"指定（低于推荐值橙色高亮，
    每日计算，升级与否仍由 BP 决定）。
  alias_or_related: PIN 流程 g16
  tags: [role, support]

- id: g32
  term: VAD / IR（Fleet Dashboard 委托关系）
  full_name: 书中未展开（VAD/IR 仅以缩写出现于 p305）
  category: role
  source_pages: p305
  source_quote: |
    "Value Added Distributor can delegate a sub-fleet of systems to their Indirect Resellers" (p305)
  definition: |
    Fleet Dashboard 的机队委托：VAD 可把子机队委托给其 IR（间接经销商）管理——RTR 状态/邮件通知等
    按委托关系分发。书中仅此一处提及，无操作细节。
  alias_or_related: 无
  tags: [role, fleet-dashboard]

# ── 三、订阅 (subscription) ──

- id: g33
  term: PoD 订阅目录（24 项）
  category: subscription
  source_pages: p360-366
  source_quote: |
    "… just 24 for the whole POD offer ... UMC is provided for free (no associated subscription)" (p360)
    "Voice Enterprise 3EY94500AA ... Room 3EY94501AA ... Softphone 3EY94502AA ..." (p360)
  definition: |
    PoD 全部 24 个商用订阅（件号 3EY945xxAA 为主）：用户档 Voice Enterprise/Room；软话机 Softphone；
    开放能力 API Telephony/API Management/API Recording Cnx；话务台 Attendant Console；呼叫中心
    Voice Agent + ALE Connect Agent/Channel；管理 Centralized Network Management/Selfcare/OV8770；
    录音 OPR Standard/Business/Enterprise；通知 VAA/VNA/VNA Broadcast；SBC 六项（Session/Remote
    User/Transcoding/Direct Routing/SIPREC/Reverse Proxy）。UMC 免费无订阅；No PRS。
  alias_or_related: 消耗类型归属见 f27 与 principle p30；件号全集 principle p29
  tags: [subscription, catalog]

- id: g34
  term: Voice Enterprise
  category: subscription
  source_pages: p361, p368, p397-398
  source_quote: |
    "User-based license whatever the devices type (IP , SIP , DECT , REX), including multi-devices
    capability ... Advanced telephony services, voice mailbox, local accounting included ... System
    services (redundancy, native encryption, ABC networking (*), outgoing DECT roaming users) included" (p361)
  definition: |
    OPEX 用户主档订阅（件号 3EY94500AA）：按用户计、不分终端类型、天然多终端；含高级电话服务/留言/
    本地计费/系统服务（冗余、原生加密、ABC-F 直连组网、DECT 漫游出户）；On activation 消耗（激活才
    计费）。desk sharing 的 DSU/DSS 各需一份；软话机另加 Softphone。
  alias_or_related: 4059 关联设备与 Attendant 也以其为底（p398 帮助口径）
  tags: [subscription, voice-enterprise]

- id: g35
  term: Softphone（ALE Softphone）
  category: subscription
  source_pages: p361, p398, p402
  source_quote: |
    "Softphone-based license (Voice Enterprise license option) • Allows to deploy either IPDSP or ALES
    softphone • One single Softphone license per user (i.e. a user with ALES PC + ALES Android = 1
    license)" (p361)
  definition: |
    软话机订阅（3EY94502AA，Voice Enterprise 的选项）：覆盖 IPDSP 或 ALES 软话机；每用户一份
    （ALES PC+Android 算一份）。消耗为双份制：SIP/IP 软话机 = Voice Enterprise + ALE Softphone 各一；
    tandem 带软话机同样双份。超订时 panic 不自动处置 Softphone（n49）。
  alias_or_related: 实测步骤 c17 步骤 8
  tags: [subscription, softphone]

- id: g36
  term: Room（Room for hospitality）
  category: subscription
  source_pages: p361, p370, p398
  source_quote: |
    "- Endpoint-based (IP , SIP or DECT) license - In case of Suite equipped with several devices, a
    subscription for each equipment is required - Hospitality voice services, voice mailbox & OXE
    Web-Based Management included" (p361)
  definition: |
    酒店客房订阅（3EY94501AA）：按终端（IP/SIP/DECT）计；一套 Suite 多设备时每设备一份；含酒店话音
    服务/留言/WBM。按客人管理时房间与客人都要开 OPEX activation、各占一份 Room。On activation 消耗。
  alias_or_related: 酒店规则 principle p31
  tags: [subscription, room, hospitality]

- id: g37
  term: SBC 订阅族（Session/Remote User/Transcoding/Direct Routing/SIPREC/Reverse Proxy）
  category: subscription
  source_pages: p360, p366
  source_quote: |
    "- Session (port-based) : for SIP trunking access or remote user access - Remote User (user-based) :
    session licenses required, as well as Reverse Proxy for Device Management) ... - Direct Routing
    (instance-based) : Connection to Microsoft Teams Virtual PBX ... Each of these subscriptions include
    high availability capability" (p366)
  definition: |
    OT-SBC 六个订阅（3EY94520/22/24/26/30/28AA）：Session（端口，SIP 中继/远端用户接入）、Remote User
    （用户，需 Session+Reverse Proxy 支持设备管理）、Transcoding（Session 选项）、Direct Routing
    （实例，对接 Microsoft Teams 虚拟 PBX）、SIPREC（Session 选项，OXE SIP 中继录音）、Reverse Proxy
    （实例，SBC 内置轻量 RP）。均含高可用。C2P 例外：仅需维护订阅（n52）。
  alias_or_related: 无
  tags: [subscription, sbc]

- id: g38
  term: OPR 订阅三档（Standard/Business/Enterprise）+ API Recording Cnx
  category: subscription
  source_pages: p360, p362, p369, p375
  source_quote: |
    "- Standard (port-based) : SIP Trunk and SIPREC recording channels, with basic search and basic user
    management - Business (port-based) : Suitable for majority of the organizations that require advance
    call searching..." (p366)
    "OPR Standard / Business / Enterprise Recording" (p369，阈值类清单)
  definition: |
    录音订阅：OPR Standard/Business/Enterprise（3EY94514/15/16AA，端口型，按检索与管理能力分档）+
    API Recording Cnx（3EY94513AA，端口型，DR-Link 录音通道上限）。OPR 许可在 OPR 服务器侧声明作
    阈值、启动后每 24 小时校验；LMS 失联 30 天后转 inactive（不能录音、管理不可用）。
  alias_or_related: 阈值范围 0-15000（c17 步骤 11）
  tags: [subscription, recording]

- id: g39
  term: UMC（免费组件）
  full_name: 书中未展开
  category: subscription
  source_pages: p360, p378
  source_quote: |
    "UMC is provided for free (no associated subscription)" (p360)
  definition: |
    PoD 目录中免费提供、无对应订阅的组件（与 C2P 版本基线图中 UMC 并列出现）。书中未展开其功能范围，
    不作外部补全。
  alias_or_related: 无
  tags: [subscription, umc, free]

# ── 四、产品/组件名 (product) ──

- id: g40
  term: CS3 / CPU8 / Appliance Server（OXE 物理承载）
  category: product
  source_pages: p24, p57, p63, p78, p84, p227
  source_quote: |
    "Used to deploy mainly physical servers as OXE CS, GAS « bare metal »…" (p24)
    "Automatic start up in «Standard Installation » mode for CS, CPU8, and Appliance Server" (p57)
    "Ensure the CS model is compatible (CS3 / CPU8 / VM)." (p78)
  definition: |
    OXE 的物理承载形态：CS3 板卡（实验主用，BOOTP 引导、MAC 贴纸/ifconfig 获取）、CPU8（BIOS CTRL+B
    网络引导；已从 MLE 目录移除仅 eBuy 订购）、Appliance Server（DHCP/PXE 引导；已由 GAS 接棒）。
    加载后角色寻址主机名为 csm（实验口径 192.168.1.103/203）。
  alias_or_related: OXE-V/GAS 为虚机与打包形态（g09/g12）
  tags: [product, hardware, pbx]

- id: g41
  term: HP DL20 G11（ALE 交付的 GAS 机型）
  category: product
  source_pages: p226-227
  source_quote: |
    "HP DL20 G11 • This platform have been qualified only with Generic Appliance Server (GAS) software
    package ... This platform can be now used for the GAS full topology (OXE, OMS and WebRTC Gateway
    VMs) if below 7000 users ... The platform delivered by ALE may change transparently, based on HP
    life cycle" (p227)
  definition: |
    ALE 交付的 GAS 一体机机型（此前的 Appliance Server 因装不下满配拓扑被 DL20 G10+/G11 接替）：仅
    限 GAS 软件包、许可限 ALU-ID 或 CC-SUITE-ID、可跑满配拓扑（<7000 用户）；ALE 可按 HP 生命周期
    透明更换机型。
  alias_or_related: 硬件前置 p12；legacy 退出 n21
  tags: [product, hardware, gas]

- id: g42
  term: FlexLM / flexlmd
  category: product
  source_pages: p135-136, p231-232, p280-282
  source_quote: |
    "A hardware dongle and a FlexLM license server for license control are required" (p135)
    "Copy this license file into the directory /opt/Alcatel-Lucent/data/licenses ... # systemctl restart
    flexlmd" (p280)
  definition: |
    本地许可服务器（GAS 上直接装在 Rocky OS，或独立交付；仅 ESXi/KVM 平台可用）：.ice 许可文件入
    /opt/Alcatel-Lucent/data/licenses 后 systemctl restart flexlmd；工具链 getaluid（查 ALUID）、
    lmutil lmhostid -flexid（dongle ID）、lmutil lmstat -a（状态）；日志 /opt/Alcatel-Lucent/logs/flexlm/
    （flexlm_lmlog.log）；OXE 侧对接端口 27000、改动后必须重启 CS。与 CCI/RTR 互斥。
  alias_or_related: 口径 principle p36；许可拓扑 f19
  tags: [product, licensing, flexlm]

- id: g43
  term: Rainbow WebRTC Gateway（GAS 内嵌 VM）
  category: product
  source_pages: p19, p221, p223-225, p267-268, p230
  source_quote: |
    "WebRTC gateway webrtc 192.168.1.15 ... rainbow Rainbow123 WebRTC VM will be deployed on the GAS
    Server" (p19，实验口径)
    "1 “Rainbow WebRTC gateway” virtual machine ... The gateway is restricted to a maximum of 50
    simultaneous calls" (p225)
  definition: |
    GAS 可选的第三台虚机（Debian Linux）：Rainbow WebRTC 网关，可随装或后加装，上限 50 并发、7000 用户
    以上须外部网关；后安装向导中配置（IP/网关/DNS/NTP/TURN=GEOIP 或区域 FQDN/RAINBOW_PBXID/
    PBX_DOMAIN/Rainbow 域名/SSH）；配置项 TURN/MPROXY 有专门的后安装界面（p230）。
  alias_or_related: 参数边界 n26；文档 TBE067/TC0000_GAS_migration
  tags: [product, webrtc, gas]

- id: g44
  term: 运维工具集（gasversion / gasbackup / uhwconf / omsconfig / spadmin / incvisu / netadmin / siteid）
  category: product
  source_pages: p239-241, p275-279, p327, p332-334, p388-398, p405-407
  source_quote: |
    "“gasversion” command to get version of GAS, OXE, OXE-MS, Rainbow WebRTC gateway and Rocky Linux
    operating system" (p239)
    "“gasbackup” command is used to perform a backup of the different components of a GAS server" (p240)
    "Using “spadmin” command, it is possible to display the CCSID" (p327)
  definition: |
    全书命令面：gasversion（查五层版本，all|package|oxe|oms|webrtc）、gasbackup（整 GAS 备份，
    .tar.gz+_PostInstall.cfg）、uhwconf（确认 OXE 宿主为 GAS）、omsconfig（OMS 配置）、spadmin（许可
    12 菜单：查 CCSID/装文件/强制 LMS 同步/读 LMS 计数/帮助）、incvisu（事件 6200-6214、647-651、
    6250-6254、5816 等）、netadmin -m（23 项网络管理：DNS/代理/安全/防火墙）、siteid（查软件版本全串）、
    downstat d/i/t（补丁后终端下载核对）、ver2cho/df -v（分区核对）、kbdconfig/setIp/setKb/grubboot/
    RUNTEL/RUFUS 级系统命令。
  alias_or_related: 数值口径 principle p15/p36；菜单树 f12/f25
  tags: [product, commands, maintenance]

- id: g45
  term: 第三方工具集（VirtualBox / VMware / Filezilla / Putty / Xming / 7-zip / TeraTerm / RUFUS / NUT）
  category: product
  source_pages: p38, p61, p86, p117, p171, p257-261, p236
  source_quote: |
    "The latest SOT release is compressed in iso format which can be uncompressed with a free tool like
    7-zip. Download the tool at this URL ... https://www.7-zip.org/download.html" (p38)
    "we have to install a X server (Xming for instance) and to use a SSH client tool that can provide
    SSH X11 forward (putty for instance)" (p257)
    "UPS management in GAS package is performed with NUT Linux package, present in the BootDVD" (p236)
  definition: |
    流程依赖的第三方工具：7-zip（解 SOT iso）、VirtualBox/VMware Workstation Player（Standalone 虚拟化
    层）、vSphere Web/thick client（ESXi）、Filezilla（FTP/SFTP 传输）、Putty（SSH/X11）、Xming/XLaunch
    （GAS 后安装图形向导）、TeraTerm（V24 终端）、RUFUS 类启动盘工具（书外通用）、NUT（GAS 的 UPS
    监控包，BootDVD 内置）。
  alias_or_related: 安装点击步骤不入册（BOOK_OVERVIEW 不适合清单）
  tags: [product, tools]

# ── 五、协议与技术名 (protocol) ──

- id: g46
  term: XMPP / WebSocket Secure (WSS)
  full_name: eXtensible Messaging and Presence Protocol（XMPP 书中展开）
  category: protocol
  source_pages: p287-289, p340-347
  source_quote: |
    "XMPP: eXtensible Messaging and Presence Protocol • XMPP consists of a TCP / IP protocol based on a
    client-server architecture to allow decentralized exchanges of instantaneous or non-instant messages
    between clients in the Extensible Markup Language (XML) format" (p288)
  definition: |
    Cloud Connect 的常驻通道协议：XMPP over WebSocket Secure（TCP 443），OXE 主动发起永久连接；
    XMPP 服务器衔接 OXE agent 与托管服务（FTR/RTR 会话、Inventory/Offer 远程动作、Push offer 的
    IBB 传输、远程控制台请求）。ccagent 进程负责该加密通道。
  alias_or_related: 安全口径 TLS1.2 见 principle p17；KeepAlive 90s（n36）
  tags: [protocol, xmpp, cloud-connect]

- id: g47
  term: SOCKS5
  category: protocol
  source_pages: p288, p290, p314, p321
  source_quote: |
    "SOCKS 5 Connectivity (TCP port 80) • SOCKS is an Internet protocol that allows client-server
    applications to transparently use the services of a network firewall. • Used to collect PBX data
    for “Inventory” and “Offer” services" (p288)
  definition: |
    按需穿防火墙通道（TCP 80）：用于 Inventory/Offer 服务的 PBX 数据采集；目标同为 connect2.opentouch.com；
    checkCloudConfig.sh 会测其 TCP 可达性；失败事件 6209。
  alias_or_related: 端口清单 principle p17
  tags: [protocol, socks5]

- id: g48
  term: BOOTP / DHCP / PXE / TFTP
  category: protocol
  source_pages: p56, p59-60, p187, p252-253
  source_quote: |
    "Depending on the call server type, the initial request can be: • BOOTP (CS and CPU Crystal) • DHCP
    (Appliance Server)" (p60)
    "Press ESC when the VM boots up Then option 3 for IPXE boot" (p187)
  definition: |
    网络引导协议族：CS/CPU Crystal 走 BOOTP、Appliance Server 走 DHCP(PXE)；引导文件 CS=startup.txt、
    AS=pxeloader、Crystal 无；文件经 TFTP 下载（清单+Linux RAM）；SOT 内置 DHCP/FTP 服务应答。
    KVM 上 OMS 加载用 IPXE（VMM 启动按 ESC 选 3）；GAS 用网卡 PXE（F11 选 LOM Port 1）。
  alias_or_related: 加载时序 f08
  tags: [protocol, boot, network]

- id: g49
  term: FTP / SFTP（端口 2222）
  category: protocol
  source_pages: p63, p67, p86, p95, p102, p117, p280
  source_quote: |
    "you have to establish a FTP or SFTP (port 2222) session, using a FTP client, with the following
    account: ­ Login: upload ­ Password: sot" (p86)
    "For security reasons, the standard "FTP" protocol cannot be used on the GAS server. Transfer the
    license files using the "SFTP" (Secure FTP) protocol, or "SCP"" (p280)
  definition: |
    两条文件通道：向 SOT 传媒体用 FTP 或 SFTP（2222 端口，账号 upload/sot，实验口径）；OXE 侧许可/补丁
    传输用 FTP/SFTP（需信任主机）；GAS 上标准 FTP 被禁用，只能 SFTP/SCP（admin 传 /tmp、root mv）。
  alias_or_related: GAS 上传细节 n24
  tags: [protocol, ftp, sftp]

- id: g50
  term: V24 链路
  category: protocol
  source_pages: p52, p67, p61
  source_quote: |
    "A V24 link allows to start and check the installation" (p52)
  definition: |
    加载过程中 CS 与 PC（SOT）之间的串口/控制台链路：用于启动与检查安装过程；实验中以终端模拟器
    （TeraTerm 等）或 Putty 会话承担观察角色。
  alias_or_related: 主机侧准备清单见 p61/p68/p79
  tags: [protocol, serial, console]

- id: g51
  term: TLS v1.2 / SRTP
  category: protocol
  source_pages: p144, p289
  source_quote: |
    "Secured connection with TLS v1.2: • Cloud Connect Infrastructure servers use a certificate issued
    by a Certificate Authority kept under ALE responsibility. • OXE has this authority certificate in a
    trust store dedicated to the Cloud Connect agent" (p289)
    "Encrypted signaling SRTP" (p144)
  definition: |
    两处加密：Cloud Connect 通道强制 TLS v1.2（CCI 证书由 ALE 责任下的 CA 签发，OXE 有专用信任库；
    checkCloudConfig 输出可见 ALE-CLOUDCONNECT-ROOT 链）；OXE-V 原生加密拓扑中媒体走 SRTP、信令加密。
  alias_or_related: 证书链输出见 c14 步骤 4
  tags: [protocol, security, tls, srtp]

- id: g52
  term: ABC link / ABC-F networking
  category: protocol
  source_pages: p148, p361
  source_quote: |
    "Node 1 ... Node 2 ... ABC link" (p148)
    "System services (redundancy, native encryption, ABC networking (*), outgoing DECT roaming users)
    included ... (*) Direct Link based ABC-F network has to be used" (p361)
  definition: |
    OXE 多节点组网链路（OXE-V Networking 拓扑中 Node 1/Node 2 经 ABC link 互联）；OPEX 的 Voice
    Enterprise 含 ABC networking 系统服务，但要求基于直连（Direct Link）的 ABC-F 网络。书中未展开
    配置细节。
  alias_or_related: 无
  tags: [protocol, networking]

- id: g53
  term: RTP payload / RFC 4733（RFC 2833）
  category: protocol
  source_pages: p139
  source_quote: |
    "RTP payload for DTMF digits (RFC 4733 or previously called RFC 2833)" (p139)
  definition: |
    OMS 的 DTMF 传输方式：RTP payload 承载 DTMF 数字，标准为 RFC4733（旧称 RFC2833）——与 OMS 的
    VoIP 编解码、QoS 标签（802.1p/DiffServ）同列于其媒体能力清单。
  alias_or_related: 无
  tags: [protocol, dtmf, rtp]

- id: g54
  term: IBB protocol / CMISE/SSH
  full_name: 书中均未展开
  category: protocol
  source_pages: p342, p352
  source_quote: |
    "Operation relying on the XMPP channel (IBB protocol)" (p342)
    "HTTPS CMISE/SSH" (p352，架构图连线标注)
  definition: |
    两个仅点到即止的协议名：IBB（XMPP 带内字节流，Push offer 文件传输所依赖）；CMISE/SSH（OPEX 架构
    图中 OXE 与云侧管理面的连线标注）。书中均无展开，不作外部补全。
  alias_or_related: 无
  tags: [protocol, passing-mention]

# ── 六、网站与资源名 (resource) ──

- id: g55
  term: MyPortal
  category: resource
  source_pages: p62, p149, p151, p192, p237, p376, p381-385
  source_quote: |
    "Download the S.O.T . and OXE software from My Portal web site" (p62)
    "Connect to MyPortal URL: ­ https://myportal.al-enterprise.com/" (p382)
  definition: |
    ALE 客户/伙伴门户（myportal.al-enterprise.com）：下载 SOT/OXE/虚机模板（.ovf/.ova）与 bootDVD、
    查 TBE/TC 文档与 cookbook、C2P 转换网页、B2B eCommerce（PoD 订购）、Asset & service manager
    （Explore Purple Assets 下载 PoD 许可）。无凭证找 BP 客户经理/ALE 代表申请。
  alias_or_related: PoD 下载路径 c16；项目 Active 判据 n53
  tags: [resource, portal]

- id: g56
  term: connect2.opentouch.com
  category: resource
  source_pages: p290, p314, p320, p329
  source_quote: |
    "The remote FQDN used by OXE agent is connect2.opentouch.com" (p290)
    "CCI domain:port = connect2.opentouch.com:443" (p320)
  definition: |
    Cloud Connect/RTR 的固定目标 FQDN：443（XMPP/WSS）与 80（SOCKS5）都指向它；checkCloudConfig.sh
    的 DNS 解析测试对象；FTR 成功后 Jid 形如 <suite-id>-3@reg-product.connect2.opentouch.com。
    防火墙放行与 DNS 解析都以该域名为准。
  alias_or_related: 无
  tags: [resource, fqdn, cloud-connect]

- id: g57
  term: cdn-oxe-sw-update.al-enterprise.com
  category: resource
  source_pages: p347
  source_quote: |
    "If OXE trusted hosts are used: “cdn-oxe-sw-update.al-enterprise.com” domain must be part of them"
  definition: |
    Fleet Dashboard 软件更新（SU）的 CDN 软件仓库域名：OXE 使用信任主机时必须把它加入白名单，
    否则 AWS 仓库的 HTTPS 下载失败。
  alias_or_related: 更新边界 n38
  tags: [resource, cdn, software-update]

- id: g58
  term: TBE043 / TBE063 / TBE067
  category: resource
  source_pages: p134, p225, p228, p242
  source_quote: |
    "consult the TBE043 document (Virtualization Design Guide) available on My Portal" (p134)
    "TBE063 - OmniPCX Enterprise & Generic Appliance Server" (p228)
    "refer to Rainbow WebRTC gateway presentation (TBE067)" (p225)
  definition: |
    售前/设计类文档三件：TBE043 虚拟化设计指南（OXE-V 平台/许可设计权威）、TBE063 OXE 与 GAS
    （含硬件历史与迁移背景）、TBE067 Rainbow WebRTC 网关介绍（GAS 内嵌网关参照）。
  alias_or_related: 无
  tags: [resource, document, presales]

- id: g59
  term: TC2456 / TC3104en-Ed08 / TC3138 / TC3142en-Ed01 / TC0000_GAS_migration
  category: resource
  source_pages: p24, p78, p230, p242, p149
  source_quote: |
    "For version compatibility, consult S.O.T . Release Note (TC2456)" (p24)
    "Refer to TC3104en-Ed08_Migration_guide_to_OXE_R101.x" (p78)
    "TC3138 Installation of a GAS server on Rocky Linux" (p242)
    "TC3142en-Ed01_OXE_deployment_on_AWS" (p149)
    "« TC0000_GAS_migration_FR_ed04.docx »" (p230)
  definition: |
    技术通报/指南五件：TC2456（SOT 版本兼容发布说明）、TC3104en-Ed08（<N3 迁移到 R101.x 指南）、
    TC3138（Rocky Linux 上装 GAS）、TC3142en-Ed01（OXE 部署 AWS）、TC0000_GAS_migration（GAS 迁移，
    WebRTC GW 配置参照）。另有 OXE 101.1 安装手册 8AL91032ENBD（p149/p242）。
  alias_or_related: 无
  tags: [resource, document, tc]

- id: g60
  term: RLAB / POD（培训实验环境）
  category: resource
  source_pages: p1-20
  source_quote: |
    "Remote Lab allows accessing a pool of virtual and physical machines (depending on the course)
    hosted in a data center ... Pods are independent of each other • Pods have the same configuration •
    Pods have access to common resources." (p5)
  definition: |
    ALE 培训远程实验室：按 POD 划分的同构实验单元（本课程 RLAB ONLY、无教室设备），共享 NAS（12.0.0.2，
    软件/许可）与 SIP 模拟器；网段 192.168.1.x/24。PC Client 经 Guacamole RDP 进入，物理机 start/stop
    按钮灰置。全部 IP/账号/密码为实验口径（principle p38）。
  alias_or_related: 节点表 f02
  tags: [resource, lab, training]

- id: g61
  term: Cloud Connect Terms & Conditions（businessportal 链接）
  category: resource
  source_pages: p329, p392
  source_quote: |
    "I do accept ALE Cloud Connect Terms & Conditions (https://businessportal.al-enterprise.com/
    cloud-connect-operations terms-and-conditions) and commit to inform my customer (y/n)? y" (p329)
  definition: |
    手动 FTR 时 CCTool 展示的条款链接（businessportal.al-enterprise.com 下）：接受条款并承诺告知客户
    是 FTR 执行的前置应答（y）。条款内容本身在书外。
  alias_or_related: 无
  tags: [resource, legal, ftr]

- id: g62
  term: ALE Knowledge Hub（培训评估）
  category: resource
  source_pages: p409-415
  source_quote: |
    "Connect to ALE Knowledge Hub (https://enterprise-education.csod.com ) with your usual credentials" (p411)
  definition: |
    培训收尾入口：enterprise-education.csod.com 上按讲师提供的课程参考号找到 session → Evaluate 完成
    在线评估，完成后才能下载培训证书。属培训运营内容，不入知识条目。
  alias_or_related: 反馈邮箱 training-services@al-enterprise.com（p415）
  tags: [resource, training]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列候选术语逐条核对

OVERVIEW 术语表共 20 行，逐条核对如下——

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| S.O.T. (Software Orchestration Tool) | 正文有明确定义（p22） | g01 |
| Template Factory（含 degraded mode） | 有明确定义（p27-29/p156） | g03 |
| 多版本加载 (Multi version) | 有明确定义（p72） | g05 |
| 静态/动态补丁 | 有明确定义（p65-66） | g07 |
| Easy Installation / Distributor | 有明确定义（p112-114） | g08 |
| OXE-V | 有明确定义（p133） | g09 |
| OMS (OXE Media Services) | 有明确定义（p138-140） | g10 |
| GAS (Generic Appliance Server) | 有明确定义（p221） | g12 |
| PCS (Passive Communication Server) | 有明确定义（p147） | g11 |
| Cloud Connect (CCI) | 有明确定义（p286） | g14 |
| FTR (First Time Registration) | 有明确定义（p293） | g15 |
| FTR with PIN code | 有明确定义（p299） | g16 |
| RTR (Right To Run) | 有明确定义（p303） | g17 |
| Qualifying Period | 有明确定义（p304） | g18 |
| Fleet Dashboard | 有明确定义（p286/p338-348） | g19 |
| LMS (License Manager Server) | 有明确定义（p353） | g23 |
| OPEX / Purple on Demand (PoD) | 有明确定义（p351） | g22 |
| OPEX activation flag | 有明确定义（p368/p399） | g25 |
| C2P | 有明确定义（p376） | g24 |
| 双分区 (active/inactive) | 有明确定义（p55） | g06 |

结论：**20/20 全部为"本书正文有明确定义"，无"仅 passing 提及需排除"项，无"书中实际未出现"项。** 下游以本文件 48 条为术语基准。

### 2. 本次新增、OVERVIEW 未列的术语

- 概念：Standalone/Hosted（g02）、Greenfield（g04）、BootDVD（g13）、CCTool/checkCloudConfig.sh（g20）、swinst（g21）、信任主机（g27）、autostart/RUNTEL（g28）、虚拟化矩阵（g29）
- 角色：BP（g30）、Helpdesk/ALE Technical Support（g31）、VAD/IR 委托（g32）
- 订阅：24 项目录（g33）、Voice Enterprise（g34）、Softphone（g35）、Room（g36）、SBC 族（g37）、OPR 三档+API Recording Cnx（g38）、UMC（g39）
- 产品：CS3/CPU8/Appliance Server（g40）、HP DL20 G11（g41）、FlexLM（g42）、Rainbow WebRTC GW VM（g43）、运维命令集（g44）、第三方工具集（g45）
- 协议：XMPP/WSS（g46）、SOCKS5（g47）、BOOTP/DHCP/PXE/TFTP（g48）、FTP/SFTP 2222（g49）、V24（g50）、TLS/SRTP（g51）、ABC link/ABC-F（g52）、RFC4733（g53）、IBB/CMISE（g54）
- 资源：MyPortal（g55）、connect2.opentouch.com（g56）、cdn-oxe-sw-update 域名（g57）、TBE 三件（g58）、TC 五件（g59）、RLAB/POD（g60）、T&C 链接（g61）、Knowledge Hub（g62）

### 3. 仅 passing 提及、未单列条目的词（附于相关条目或备查）

OTEC（p27，模板用途脚注）、OST64/EEGW（p134，虚机组件名随平台矩阵）、GD4/GA4/MR1/SLI16/UAI16（p138/p358-359，板卡型号）、OTCC/O2G/VNA/VAA/Selfcare/OPR/OV8770（订阅目录内已覆盖 g33/g38）、ALES/IPDSP（g35）、ZUORA/SAP/eBuy/Service Manager（p352 架构图组件，附于 g22/g23 背景）、eBuy 另见 n42（CPU8 渠道）、ELP（p354，swk 生成方，未展开）、PBWS（p347，下载区名，未展开）、DCO/CCO（p290 CCO infra 口径，未展开）、"Delivery note"（p22，SOT 规格文档，附于 n01）、SIP Simulator/ITSP（p5 实验资源，纯培训设施）、businessportal.al-enterprise.com（g61）、enterprise-education.csod.com（g62）、training-services@al-enterprise.com（p415）。

### 4. 提取口径说明

- 所有定义只采信本书正文；UMC/ELP/ACTIS/IBB/CMISE/PBWS/CCO/OTEC/OST64/EEGW 等书中未给全称或未展开的缩写，full_name/definition 字段一律省略或标注"未展开"，不做外部补全。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准，引用均为原文摘录（p269 的 letacla1、p254 的 60 分钟等实验值已标"实验口径"）。
- 培训专用设施（RLAB 密码表、SIP 模拟器、第三方工具点击步骤）按要求仅作 Boundary 背景保留（principle p38 / g60 / g45），不展开为操作条目。
