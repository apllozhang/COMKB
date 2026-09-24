# 术语/缩写/产品名候选 — OmniSwitch LAN Access Switching (DT00XTE215EN Ed23)

> 提取器: glossary-extractor（全量扫描） | 全局上下文: BOOK_OVERVIEW.md | 提取日期: 2026-09-23
> 共 60 条（六类：概念/角色/许可与订阅/产品/协议/资源）。EMP/RCL/VFL/QSI/ISIS-VC/BUM/DCE 等缩写书中未给全称，full_name 字段如实省略，不采信外部知识。UNP 两处全称不一致（p393 User Network Profile / p456 Universal Network Profile）如实并列。

```yaml
# ── 一、核心概念 (concept) ──

- id: g01
  term: AOS (OmniSwitch AOS)
  category: concept
  source_pages: p9, p65, p129
  source_quote: |
    "OmniSwitch AOS Switch Management Guide • Describes basic attributes of the switch and basic switch administration tasks ... OmniSwitch AOS Network Configuration Guide ... OmniSwitch CLI Reference Guide" (p9)
    "image files (AOS) Nosa.img Nos.img Wos.img Dos.img Uos.img ..." (p129)
  definition: |
    OmniSwitch 的操作系统/软件体系（书中未展开全称）：本教材即 "AOS OmniSwitch R8" 的管理课；镜像文件按产品代际有 Nos/Wos/Dos/Uos 等多种命名；文档体系五册（Hardware/Management/Network Config/Advanced Routing/CLI Reference）。
  alias_or_related: R8 = Release 8；镜像命名见 g22 working/certified
  tags: [concept, os, core]

- id: g02
  term: AAA / ASA (Authenticated Switch Access)
  full_name: Authenticated Switch Access（书中展开）
  category: concept
  source_pages: p67-69, p85, p95
  source_quote: |
    "Authenticated Switch Access (ASA) provides the ability to restrict which users can configure the switch remotely. Switch login attempts can be challenged via the local database, or a remote database such as RADIUS or LDAP. ASA applies to Telnet, FTP, SNMP, SSH, HTTP, and the console and modem ports." (p95)
    "-> aaa authentication {console | telnet | ftp | http | snmp | ssh | default} server1 [server2...] [local] [exit-on-fail {enable | disable}]" (p69)
  definition: |
    交换机登录认证框架：按服务类型（console/Telnet/FTP/HTTP/SSH/SNMP/default 七条链）逐条配置认证服务器序列（本地库或 RADIUS/LDAP，支持多服务器 fail-through 与 exit-on-fail 语义）；ASA 还借 aaa switch-access management stations 限制管理源 IP（≤64）。
  alias_or_related: AAA 是命令族名，ASA 是特性名（同域使用）
  tags: [concept, aaa, security, core]

- id: g03
  term: WebView
  category: concept
  source_pages: p81-82, p97-101
  source_quote: |
    "The switch can be monitored and configured using WebView • View is limited to one switch • Access can be secured • The WebView application is embedded in the switch and is accessible via a web browser" (p81)
  definition: |
    内嵌于交换机的 Web 管理应用（ALE 的 web-based device management tool）：单机视角、R8 默认强制 SSL（80/443 可改）；配置分 Physical/Layer 2/Networking/Service management/Security/QoS/Device management 七组；默认服务 enabled 但 HTTP 认证未授权时不能登录。
  alias_or_related: 与 OmniVista（网管平台）分工；入口见 g54
  tags: [concept, webview, management]

- id: g04
  term: Lightning Config (OLC)
  full_name: OmniSwitch Lightning Configuration（p103 展开）
  category: concept
  source_pages: p102-126
  source_quote: |
    "Understand what is OLC, OmniSwitch Lightning Configuration." (p103)
    "ALE Lightning Config simplifies small to medium networks • Fast Setup: Go from unboxing to passing traffic in less than 5 minutes per switch." (p106)
  definition: |
    单机快速开局向导：笔记本 DHCP 接端口 1 → https://192.168.0.1（端口 1 为 DHCP Client、默认 IP 接口 VLAN1）→ Recommended Defaults + LIGHTNING CONFIG 必填项 → 改 admin 密码 → 保存；支持 .json 模板导入复用；禁令体系见反例 n03-n06。
  alias_or_related: OST 的 Config wizard 提供任意 ALE 交换机的同型能力（p222）；对照 g46 Auto-Fabric（多台自动）
  tags: [concept, onboarding, core]

- id: g05
  term: Working / Certified / Running directory
  category: concept
  source_pages: p129-131, p141-147
  source_quote: |
    "The certified directory contains files that have been certified by an authorized user as the default files for the switch. ­ The working directory is a holding place for new files. ... ­ The running directory is the directory where the configuration changes will be saved. ­ The running configuration, stored in the RAM..." (p141)
  definition: |
    闪存三层模型：certified=授权用户认证过的回滚基线；working=新文件的试验场；running=当前启动目录（RAM 中运行配置来自它+用户改动）。冷启动按内容异同决定回 certified 或 running；reload all 强制 certified；certified 运行态只读。
  alias_or_related: 用户自定义目录（任意名）同 working 语义（p141）；状态判读 show running-directory
  tags: [concept, directories, rollback, core]

- id: g06
  term: write memory / copy running certified / write memory flash-synchro
  category: concept
  source_pages: p132-133, p144
  source_quote: |
    "sw7 (OS6860-A) -> write memory ... sw7 (OS6860-A) -> copy running certified ... write memory flash-synchro = write memory + copy running certified" (p133)
    "File /flash/working/vcsetup.cfg replaced. File /flash/working/vcboot.cfg replaced." (p144)
  definition: |
    配置固化三命令：write memory=RAM→启动目录；copy running certified=启动目录→certified 基线；write memory flash-synchro=两者合一（VC 下同步全体成员）。vcsetup.cfg 与 vcboot.cfg 是被写入的两个配置文件。
  alias_or_related: certify-on-reboot（p134，下次重启时认证 working 镜像，仅当次有效）
  tags: [concept, write-memory, core]

- id: g07
  term: Virtual Chassis (VC)
  category: concept
  source_pages: p150-163, p173-182
  source_quote: |
    "Virtual Chassis = Group of switches which appears as a single router or bridge • Key Points • Single Point of management • Single Logical Switch • Redundancy and resiliency supported across the switches • No STP/VRRP between Access and Core switches ... • No license needed" (p152)
  definition: |
    堆叠技术：多台交换机经 VFL 互联呈现为一台逻辑交换机——单管理点、单逻辑交换机、跨机箱冗余、成员间无需 STP/VRRP、免许可证、支持 ISSU 滚动升级。拓扑由私有协议 ISIS-VC 维护（BUM 流量无环、SPBM 式等价路径裁决）。
  alias_or_related: VFL 见 g08；选举/分裂防护见 g09/g10；每型号规模矩阵见 BOOK_OVERVIEW f14
  tags: [concept, virtual-chassis, core]

- id: g08
  term: VFL
  category: concept
  source_pages: p152-154, p159, p180
  source_quote: |
    "Switches inter-connected via dedicated or optional SFP+, QSFP ports • Mesh or Ring topology ... VFL" (p152)
    "sw5 (6360-A) -> virtual-chassis vf-link-mode auto ... show virtual-chassis vf-link ... VFLink mode: Auto" (p177, p180)
  definition: |
    VC 成员间的堆叠互联链路（书中未展开全称，界面名 VFLink）：可专用端口或复用上联口（各型号合格端口表 p159）；支持 auto 模式（vf-link-mode auto + auto-vf-link-port）与静态模式（建 VFL ID 指定成员口）；member-port 有 Is Primary 主备口之分。
  alias_or_related: Auto VFL 特性（p159）；OS9900 仅支持静态 VFL
  tags: [concept, virtual-chassis]

- id: g09
  term: VC 选举与接管（ISIS-VC / MAC retention）
  category: concept
  source_pages: p155-157
  source_quote: |
    "VC topology managed by ISIS-VC • Private TLV report the switch's capability and numbering ... 'MAC retention' is always enabled • When the master reloads or fails, the slaves reelect a new master ... When the 'original' master comes back, no election will be processed, and the 'new' Master will retain its Master role" (p155, p157)
  definition: |
    VC 控制平面：私有协议 ISIS-VC（HELLO 建邻接、私有 TLV 交换能力与编号）；选举四级序=最高优先级→最长运行时长（差>10 分钟才比较）→最小 chassis ID→最小 MAC；主备镜像镜像与配置；接管时 MAC retention 恒开（二层身份不变），原主恢复不抢回。
  alias_or_related: 优先级 0-255（p167）；分裂防护见 g10
  tags: [concept, virtual-chassis, election]

- id: g10
  term: VC 分裂防护（RCD / VC Split Protocol）
  category: concept
  source_pages: p160-161
  source_quote: |
    "2 mechanisms • Out of Band: EMP Remote Chassis Detection (RCD) • In Band: VC Split Protocol ... Proprietary protocol called 'VC Split Protocol' • VCSP LAG towards the helper switch" (p160-161)
  definition: |
    防 VFL 断链导致 MAC/IP 双主的双机制：带外 RCD 经 EMP/管理网侦测（IP 取序：NVRAM 中 CMM 地址→机箱 EMP 地址；检出后原 slave 关用户口、状态 Split-Topology，VFL 恢复重启回归）；带内 VCSP 需 helper 交换机与 VCSP LAG（split-protection 命令族），保护模式下仅保留 master 角色、除 VFL 与 LAG 外接口 shutdown。
  alias_or_related: RCD=Remote Chassis Detection（书中展开）；VCSP=VC Split Protocol（书中展开）
  tags: [concept, virtual-chassis, split]

- id: g11
  term: ISSU (In Service Software Upgrade)
  full_name: In Service Software Upgrade（p162 标题展开）
  category: concept
  source_pages: p162
  source_quote: |
    "Used to upgrade the software on a VC with minimal network disruption • Each element is upgraded individually ... Upload new code, vcsetup.cfg and vcboot.cfg in a new directory (ex. issu_dir) • The Slaves are then reloaded from the ISSU directory in order from lowest to highest chassis ID" (p162)
  definition: |
    VC 滚动升级机制：新代码与配置放独立目录（issu_dir），issu 命令触发，slave 按 chassis ID 从低到高逐台重载，主控最后，业务中断最小化。
  alias_or_related: 另见 p54 产品矩阵中 6900 的 I.S.S.U 卖点
  tags: [concept, upgrade, virtual-chassis]

- id: g12
  term: ssh-chassis
  category: concept
  source_pages: p163, p181
  source_quote: |
    "A user can access to remote CLI console of any VC with secure shell protocol (SSH). ssh-chassis <username>@<chassis-id> ... Executing: ssh admin@127.10.2.65" (p163)
  definition: |
    VC 内跨成员远程 CLI 访问：ssh-chassis admin@<chassis-id> 内部映射到 127.10.<id>.65；提示符相同，需以 show virtual-chassis topology 的 Local Chassis 字段确认所在成员。
  alias_or_related: logout 返回原成员（p181）
  tags: [concept, virtual-chassis, access]

- id: g13
  term: UNP (User Network Profile / Universal Network Profile)
  category: concept
  source_pages: p185, p190, p202, p393, p456, p457, p477
  source_quote: |
    "Role Based Access Control with UNP (Universal Network Profile) • Auto-sensing, multi-client authentication on a port" (p456)
    "Access Guardian * User Network Profile" (p393)
    "Once authenticated, a Universal Network Profile (UNP) will be applied to the network users." (p477)
  definition: |
    按用户/设备下发的网络档案：VLAN 映射 + ACL/QoS 策略列表 + 位置策略 + 时段策略；认证成功后由 RADIUS 以 Filter-Id 属性回传 UNP 名。注意书中全称两写——p393 用 "User Network Profile"、p456/p477 用 "Universal Network Profile"，同一概念。
  alias_or_related: 档案五要素（UNP profile=map vlan + qos-policy-list + location-policy + period-policy + CP 档案）；分类规则见 g14
  tags: [concept, unp, access-guardian, core]

- id: g14
  term: UNP 分类规则（Classification rules / Binding / Extended）
  category: concept
  source_pages: p189, p191-192
  source_quote: |
    "UNP Port classification rules 1. Port/Linkagg 2. Domain 3. MAC address 4. MAC-OUI 5. MAC address range 6. LLDP 7. Auth-type 8. IP address 9. VLAN tag" (p189)
    "Precedence: Extended rule > Binding Rule > Simple Rule" (p192)
  definition: |
    动态把移动端口分入 VLAN/档案的规则体系：九条简单规则按编号定优先级；绑定规则=多条件 AND；扩展规则=命名规则列表+precedence 值（优先级最高）。UNP 口启用而认证关闭/失败时应用分类规则。
  alias_or_related: MAC-OUI=MAC 厂商前缀口径（书中未展开该词）
  tags: [concept, unp, classification]

- id: g15
  term: Access Guardian
  category: concept
  source_pages: p454-475, p476-485
  source_quote: |
    "Describe Access Guardian • Setup Access Guardian - Port - User Network Profile - Classification Rule / policy - Port-Templates - Authentication server (Radius Server)" (p455)
  definition: |
    基于认证的接入控制特性集：802.1x/MAC 双认证、UNP 下发（Filter-Id）、pass-alternate 降级档案、auth-server-down 档案（默认 60 秒重试）、AAA profile、端口模板、Captive Portal 挂钩（p467 属性清单）；监控 show unp user/status/details。
  alias_or_related: 底座是 g13/g14 的 UNP 体系；RADIUS 见 g44
  tags: [concept, access-guardian, security, core]

- id: g16
  term: DHL (Dual-Home Link) Active-Active
  full_name: Dual-Home Link（p324 标题展开）
  category: concept
  source_pages: p324-334, p336-344
  source_quote: |
    "Provides fast failover between Core/Aggregation and Access switches without using STP • DHL Active-Active splits VLANs between two active links" (p326)
  definition: |
    双上行双活方案：每交换机 1 会话、每会话 LinkA/LinkB 两链（物理口或聚合）；一组 VLAN 同打标在两链、vlan-map linkb 指定 LinkB 服务集，其余归 LinkA；故障全量切换、恢复等 pre-emption（默认 30 秒，0-600 可调）；DHL 端口自动禁 STP；配 MAC flushing（RAW/MVRP/None）防 stale 表项。
  alias_or_related: 与 STP/LACP 三方案对比（p330：DHL 无交换机级冗余）
  tags: [concept, dhl, redundancy, core]

- id: g17
  term: policy 引擎（condition / action / rule）
  category: concept
  source_pages: p400-407, p431
  source_quote: |
    "A policy (or a policy rule) is made up of: 1. a condition 2. an action ... Gets Policies from • CLI • Webview • PolicyView (OV)" (p400)
    "QoS policies used to control whether or not packet flows are allowed or denied at the switch or router interface • Policies for ACLs are created in the same manner as QoS policies" (p431)
  definition: |
    统一策略引擎：condition（L1-L4 条件与四种组）+ action（accept/drop/deny、优先级、带宽/深度、802.1p/TOS/DSCP 标记与映射、permanent gateway（PBR）、镜像、port-disable、CIR 限速）+ rule（precedence/validity-period/log/count）；qos apply 下发生效；默认 disposition accept。QoS/ACL/PBR/策略镜像全部复用。
  alias_or_related: 条件组合全表在 Network Configuration Guide（p422 指针）
  tags: [concept, policy, qos, acl, core]

- id: g18
  term: QSet / QSP / QSI
  category: concept
  source_pages: p397-398
  source_quote: |
    "QSet Profile 1 Q1 = SP7, 100% BW ... Q8 = SP0, 100% BW Strict Priority (SP)" (p397)
    "-> qos qsi port 1/2/1 qsp 2 ... qos qsp system-default 2 ... * Eg: QSet Profile 2 (1 EF + 7 SP)" (p398)
  definition: |
    QoS 端口队列模型：每端口 8 个队列（QSet Instance，QSI）；队列集档案 QSP（Queue Set Profile，p397 用语）定义调度与带宽——QSP 1=8×严格优先级、QSP 2=1×EF+7×SP 等；可按端口/linkagg 改 QSI 的 QSP 或改系统默认（qos qsp system-default）。
  alias_or_related: EF=Expedited Forwarding 口径（书中未展开）；SP=Strict Priority（书中标注）
  tags: [concept, qos, queue]

- id: g19
  term: OST (OmniVista Smart Tool)
  category: concept
  source_pages: p215-230, p572-580
  source_quote: |
    "Application for installations and problems resolution • Quickly identify any device connected to the ALE switch • One button repairs for PoE devices that won't boot • Debug and open tickets with Tech Support with a single button" (p217)
  definition: |
    装机与排障桌面工具：设备识别、PoE 一键向导/修复、Reset Port/Cable Test/ping、Auto-Ticket（收集 TAC 材料生成工单模板）、流量分析（坏线/SFP、丢包、广播、组播）、Config 向导与备份恢复（RMA 换机还原）。1.0=单机社区版（停更）；2.0=Client-Server+PostgresSQL（100 交换机/4000 设备/5 并发、静态数据加密）。
  alias_or_related: 安装见 g55 Postgres；下载见 g53 MyPortal
  tags: [concept, ost, tooling]

- id: g20
  term: Fleet Supervision / Services Kiosk
  category: concept
  source_pages: p555-568
  source_quote: |
    "Assess and Control Compliance with Network Fleet Supervision • One View. All Assets. Every Status ... • Accelerate Operations with Service Kiosk • Identify device with no or expiring support • Request coverage from your partner. ... Free of charge" (p558)
  definition: |
    免费资产与合规监管云：软件版本可视、库存可视化（机箱/电源/光模块/AP 钻取）、KPI 仪表盘（生命周期 GA/EoS/EoL、维保 Active/Expired/None、硬件支持 AVR/RTF）、资产汇聚（OmniVista 自动或 CSV/XLSX 导入）；Services Kiosk 识别无支持/将到期设备并申请续保。只读监管，配置管理仍在 OmniVista/CLI。
  alias_or_related: 声明来源见 g57 myfleet
  tags: [concept, fleet, assets]

- id: g21
  term: Auto-Fabric / RCL / LBD
  category: concept
  source_pages: p536-553
  source_quote: |
    "AUTO-FABRIC - PLUG-N-PLAY ZERO TOUCH DEPLOYMENT 1- Auto-VC 2- Automatic remote configuration 3- Auto-LACP 4- Auto-Routing 5- Auto-SPB Fabric 6- Auto-Network Profiling 7- Auto-MVRP" (p538)
    "RCL is run after Auto VC, and before the rest of Auto Fabric ... RCL tries 6 times, 3 each on VLAN 1 and 127" (p543)
    "LBD transmits periodic proprietary Multicast MAC frames on the LBD enabled ports ... Port is disabled (forced down) • Error Log is issued • SNMP trap • Can be re-enabled by user" (p549)
  definition: |
    零触开局七步链：Auto-VC（自动堆叠）→ RCL（远程自动配置，DHCP 取指令文件，全称书中未展开）→ Auto-LACP（LLDP 私有 TLV 探测成聚合，agg 127/admin-key 65535）→ Auto-Routing（OSPFv2/v3、IS-IS 自动邻居与重发布）→ Auto-SPB（BVLAN 4000-4015/ECT 1-16）→ Auto-Network Profiling（接入画像）→ Auto-MVRP（VLAN 传播，STP 切 flat）。伴随 LBD（Loop Back Detection，环路检测：周期组播帧回收即关端口+日志+trap）。
  alias_or_related: 首启 Y/N 语义见反例 n36；各协议可单独 disable（p553）
  tags: [concept, auto-fabric, zero-touch]

- id: g22
  term: vcboot.cfg / vcsetup.cfg / userTable
  category: concept
  source_pages: p129, p136, p141, p179
  source_quote: |
    "A configuration files, named vcboot.cfg and vcsetup.cfg, in text format, sets and controls the configurable functions." (p141)
    "The Local userDB file is named userTable* Path: flash/system directory" (p70)
    "sw5 (6360-A) -> cat /flash/working/vcsetup.cfg ... virtual-chassis chassis-id 1 configured-chassis-id 1 ..." (p179)
  definition: |
    三个关键文件：vcboot.cfg/vcsetup.cfg=文本格式配置文件（VC 参数在 vcsetup.cfg，cat 可读），write memory 时被替换、配置备份时被打包；userTable=本地用户库（flash/system），配置备份三件套之一。
  alias_or_related: [SAVED INFO VC IDs] 区域不可手改（p179 注释）
  tags: [concept, files, directories]

- id: g23
  term: Loopback0
  category: concept
  source_pages: p360-361
  source_quote: |
    "Identify a consistent address for network management purposes • Not bound to any VLAN • Always remain operationally active (as long as at least one VLAN is active) ... • Automatically advertised by RIP and OSPF protocols when the interface is created (not by BGP)" (p360)
  definition: |
    不绑 VLAN 的常活环回接口（名字必须写 Loopback0）：作 PIM-SM RP、sFlow Agent 地址、RADIUS 认证源、NTP 客户端、BGP peering、OSPF router-id、NMS 设备与 trap 识别；RIP/OSPF 自动通告、BGP 不会。配合 ip service source-ip 统一各 IP 服务源地址。
  alias_or_related: 实验 192.168.254.x/32（实验口径）
  tags: [concept, loopback, management]

# ── 二、角色 (role) ──

- id: g24
  term: admin（本地管理员用户）
  category: role
  source_pages: p15, p70, p98
  source_quote: |
    "OmniSwitch credentials: login: admin password: Superuser=1" (p15)
    "** Default login name and password Login : admin Password : switch" (p70)
  definition: |
    出厂内置管理员账号（默认密码 switch，8.10R04 起强制首登改密）；实验口径为 admin/Superuser=1（R-Lab 预改）。WebView、SSH、console 全通道可用。
  alias_or_related: 对照 g25 default 用户
  tags: [role, admin]

- id: g25
  term: default（内置用户）
  category: role
  source_pages: p70
  source_quote: |
    "By default : 2 users 'admin and default'" (p70)
  definition: |
    出厂两用户之一（另一为 admin）；书中未展开其用途细节（按 AOS 惯例用于无法识别用户时的兜底登录，此处不采信外部知识、仅记录其存在）。
  alias_or_related: 与 admin 同存于本地 userTable
  tags: [role, users]

- id: g26
  term: 用户权限（read-write / 命令域与命令族）
  category: role
  source_pages: p70, p72
  source_quote: |
    "* User Privileges : read and write access to command domains and families" (p70)
    "-> user newuser password P@ssW0rd123# read-write all sha+des" (p72)
  definition: |
    本地用户的权限模型：对命令域（domains）与命令族（families）的读/写授权；建用户时以 read-write all 示例授予全部命令域读写。
  alias_or_related: 最小权限需按域/族拆分授予（书中仅给 all 示例）
  tags: [role, privileges]

- id: g27
  term: admin-netadv（R-Lab SSH 账号）
  category: role
  source_pages: p38
  source_quote: |
    "ssh admin-netadv@10.4.X.Y // where X is your pod number and Y the switch number. ... Enter the passphrase: Superuser01!" (p38)
  definition: |
    实验专用 SSH 账号（从 Linux 客户端连交换机用），口令 Superuser01!（与交换机本地 admin 的 Superuser=1 不同）。纯教学基础设施产物（实验口径）。
  alias_or_related: 对照 g24 admin；见反例 n49
  tags: [role, lab]

# ── 三、许可与订阅 (subscription) ──

- id: g28
  term: Advanced License / Data Center License
  category: subscription
  source_pages: p180
  source_quote: |
    "licenses-info - A: Advanced; B: Data Center; ... 1 1 OK OS6360 1 15 4094 4094 A" (p180)
  definition: |
    AOS 功能许可分级口径（书中在 VC 一致性核查里以 A/B 呈现）：A=Advanced、B=Data Center；同一 VC 内成员许可等级必须一致（强制一致性项）。
  alias_or_related: 许可完整目录在书中未展开（以 MyPortal/规格指南为准）
  tags: [subscription, license, virtual-chassis]

- id: g29
  term: Demo License
  category: subscription
  source_pages: p263, p540
  source_quote: |
    "2019 Jul 15 20:26:27.515 : CMM : vc_licManager : Demo License will expire on date: 7/14/2019" (p263)
    "• Auto VFL Default ports • Auto Chassis ID ... Demo License enabled by default" (p540)
  definition: |
    演示许可：Auto-VC 场景下默认启用（p540）；事件日志会出现到期提醒（p263 示例）。到期行为书中未展开。
  alias_or_related: "Valid Advanced or Demo license" 为 VC Mode 判定分支之一（p540）
  tags: [subscription, license]

- id: g30
  term: OmniSwitch 支持合同（OST 2.0 前提）
  category: subscription
  source_pages: p229
  source_quote: |
    "The tool is available to customers with a valid OmniSwitch support contract. • The OmniSwitch Smart Tool is available for all Business Partners with a valid distributor agreement ... ALE will support the OmniVista Smart Tool under the same conditions as the Alcatel-Lucent OmniSwitch" (p229)
  definition: |
    OST 2.0 的获取与支持前提：客户须持有效 OmniSwitch 支持合同（BP 须有效分销协议）；工具免费下载但支持与 OmniSwitch 支持协议绑定。
  alias_or_related: Fleet Supervision 免费无合同门槛（对照）
  tags: [subscription, support, ost]

# ── 四、产品/组件名 (product) ──

- id: g31
  term: OmniSwitch 6360 / 6370
  category: product
  source_pages: p54-55, p174, p476
  source_quote: |
    "OmniSwitch 6360 AOS L2+ Basic L3 GE ... OmniSwitch 6370 AOS L2+ Basic L3+ MG New!" (p54)
    "Model Name: OS6360-P10, ... Part Number: 904306-90 ... In case of OS6360-P10 the VFL ports are 1/1/11-12 ­ In case of OS6360-P24 the VFL ports are 1/1/27-28" (p174)
  definition: |
    接入层主力型号（本书多数实验的宿主）：OS6360=AOS L2+ Basic L3 GE（P10/P24 等子型，VFL 端口随子型不同）；OS6370=新款 L2+ Basic L3+ Multi-Gig。hash 默认 brief（p280）、VC 上限 4（24/48 口）或 8（10 口机型）（p153）。
  alias_or_related: 实验 VC 由两台 6360 组成（c03）；型号识别 show chassis
  tags: [product, switch, edge]

- id: g32
  term: OmniSwitch 6560/E
  category: product
  source_pages: p54-55, p95, p249
  source_quote: |
    "OmniSwitch 6560/E AOS Advanced L3 licensed 1GE/2.5G/5G 10G uplinks" (p54)
    "Log into the OS6560-A ... sw3 (6560-A) -> show aaa authentication" (p95)
  definition: |
    MultiGig 接入/汇聚型号（AOS Advanced L3 licensed）：实验中的 SSH/WebView 宿主（sw3）；hash 默认 extended；8.9R3 起支持经 linkagg 的远程镜像；Auto VFL 用专用口+末两个 10G SFP+。
  alias_or_related: 实验 EMP 地址 10.4.Pod#.3（p93）
  tags: [product, switch]

- id: g33
  term: OmniSwitch 6860/E/N 与 6865
  category: product
  source_pages: p54-55, p129, p153
  source_quote: |
    "OmniSwitch 6860N AOS Advanced L3 1GE/2.5G/5G/10G 10/25/40/100G uplinks ... OmniSwitch 6865 Hardened AOS Advanced L3" (p54)
    "sw8 (6860-B) -> show ip interface ... 10.4.21.8" (p293)
  definition: |
    汇聚层 Advanced L3：6860E/N（N 为新一代，console 115200、专用 VFL 口、支持 FPoE/PPoE/RCD/VCSP）；6865=Hardened 版。实验中 6860-B 为核心侧交换机（sw8）。
  alias_or_related: 分裂防护支持平台 OS6860E/N（p160-161）；hash 默认 extended
  tags: [product, switch, aggregation]

- id: g34
  term: OmniSwitch 6870
  category: product
  source_pages: p54-55, p153
  source_quote: |
    "OmniSwitch 6870 Next Gen L3 LAN switch with MPLS datasheet ... OmniSwitch 6870 AOS Advanced L3 1GE/2.5G/5G/10G 10/25/40/50/100G uplinks 200G VFL New!" (p54)
  definition: |
    新一代汇聚/核心机型（Advanced L3 + SPB/VXLAN/MPLS，200G VFL、2×40/100/200G QSFP56）：实验中 6870-A 为核心（sw7）、6870-B 为第二台；支持 FPoE/PPoE/RCD/VCSP；console 115200；hash 默认 extended。
  alias_or_related: VC 上限 8（p153）；实验聚合 17/78 预置其上（p286）
  tags: [product, switch, aggregation]

- id: g35
  term: OmniSwitch 6900 / 6920
  category: product
  source_pages: p54, p153-154
  source_quote: |
    "OmniSwitch 6900 / 6920 AOS Advanced L2-L3 Aggregation/Core DC TOR 10/40/100/200/400 GE ... VRF, SPB, VXLAN ... I.S.S.U" (p54)
    "OS6900-X20/X40/T20/T40/Q32/X72 models can be mixed in a VC of up to 6 elements" (p154)
  definition: |
    核心/DC TOR 机型（VRF/SPB/VXLAN、ISSU、高密度 10-400G）：子型矩阵复杂（X/T/Q32/X72 与 V72/C32/E/X48C6/T48C6/V48C8/X24C2/T24C2/X48C4E 两组混插规则，上限 6 台）；Auto VFL 取每机箱最后 5 口；X48C4E 混插需 8.9R4+ 与 capability vfl-type 命令。实验中 6900-A 为核心（sw1）。
  alias_or_related: console 波特率按子型 9600/115200 分档（p523-524）
  tags: [product, switch, core]

- id: g36
  term: OmniSwitch 9900（9907/9912）
  category: product
  source_pages: p54, p153
  source_quote: |
    "OmniSwitch 9907/9912 Modular Chassis AOS Advanced L3 10/40/100 GE" (p54)
    "OS9900 Up to 8 VFL member ports ... 2 x OS9900" (p153)
  definition: |
    模块化机箱核心（10/40/100 GE）：VC 上限 2、仅支持静态 VFL（Auto VFL 合格口表明确排除）；40G/100G QSFP 于 CMM 上。hash 默认 extended。
  alias_or_related: RMA 级升级风险语句涉及 ONIE（p533）
  tags: [product, switch, chassis]

- id: g37
  term: OmniSwitch 2260/2360、6465、6570M、6575
  category: product
  source_pages: p54-55
  source_quote: |
    "OmniSwitch 2260/2360 AOS L2 WebSmart ... OmniSwitch 6570M AOS L3+ licensed Metro Ethernet 1GE 10G uplinks ... OmniSwitch 6575 Industrial Hardened AOS Advanced L3 New!" (p54-55)
  definition: |
    其余产品线速览：2260/2360=WebSmart 二层（无本教材实验）；6465=L2+ Basic L3 hardened（hash brief；Auto VFL 口 27/28）；6570M=Metro Ethernet L3+（签名镜像自 8.9R4 最早提供）；6575=工业加固 L3。
  alias_or_related: 详细定位见 p55 堆叠产品矩阵
  tags: [product, switch, portfolio]

- id: g38
  term: OmniAccess Stellar AP
  category: product
  source_pages: p57-63
  source_quote: |
    "OMNIACCESS STELLAR LINEUP – WIFI 6 ... WiFi 6E ... WiFi 7 ... AP1301 ... AP1431 ... AP1521" (p58-60)
  definition: |
    ALE 无线 AP 产品线（WiFi 6/6E/7，室内/室外/医用等分层）：本教材仅作组合背景与 R-Lab 无线客户端的关联（AP 凭据 support/aos2016，p16）；详细参数走 datasheet。
  alias_or_related: 与 OmniSwitch 同属 ALE LAN/WLAN 组合（p53 全景）
  tags: [product, wlan, portfolio]

- id: g39
  term: RustConn / Proxmox
  category: product
  source_pages: p19-24
  source_quote: |
    "RustConn : access to the Switches & Access Points consoles. Linux clients 1 to 10 and Wireless Client. Proxmox : access to the linux clients 1 to 10 for starting and stopping only" (p19)
  definition: |
    R-Lab 两入口工具：RustConn=交换机/AP 控制台与 Linux/无线客户端桌面（双击自动登录、支持分屏广播命令）；Proxmox VE=客户端虚机的开停管理（Pool View）。
  alias_or_related: TigerVNC 为客户端桌面载体（p40）；广播功能见反例 c01 关联 p48-50
  tags: [product, lab]

- id: g40
  term: OmniVista（Terra / 2500 / Cirrus）
  category: product
  source_pages: p56, p84, p533, p563-567
  source_quote: |
    "OmniVista Terra (on premises) datasheet • OmniVista Cirrus (cloud) datasheet" (p56)
    "Using OmniVista on premises (2500 4.X or Terra) • Using OmniVista Cirrus <= easiest way, recommended software package available directly from the application" (p533)
  definition: |
    ALE 网管平台家族：OmniVista 2500 4.X/Terra（本地）与 Cirrus（云）。本书角色：软件升级通道之一（Cirrus 最简单）、SNMP 网管与 RMON 展示端、Fleet Supervision 的资产来源（OV2500 ID / Cirrus API Key / Cirrus 10.5 App ID+Secret）。
  alias_or_related: PolicyView 为其策略下发组件名（p400）
  tags: [product, nms, omnivista]

# ── 五、协议/技术名 (protocol) ──

- id: g41
  term: STP / RSTP / MSTP（802.1d/w/s）
  category: protocol
  source_pages: p300-311, p313-323
  source_quote: |
    "Supports two Spanning Tree operating modes: • flat (single STP instance per switch) • per-VLAN (single STP instance per VLAN) (By default on OmniSwitch)" (p300)
    "STP (802.1d): Convergence time : 50 secs • RSTP (802.1w): Convergence time : < 1 sec • MSTP (802.1s): < 1 sec" (p300)
  definition: |
    生成树家族：两种模式（flat 单实例 / per-VLAN 即 1x1，OmniSwitch 默认后者）；三种协议（802.1d 50 秒收敛、802.1w <1 秒、802.1s <1 秒）；路径成本 16/32 位两套；保护特性 restricted-role/restricted-tcn/用户口 BPDU 过滤。
  alias_or_related: Cisco PVST+ mode 与 VLAN Consistency check 字段出现于 show spantree mode（p305，书中未展开）
  tags: [protocol, stp, core]

- id: g42
  term: LACP (IEEE 802.3ad)
  category: protocol
  source_pages: p273, p275, p283-290, p545
  source_quote: |
    "Dynamic • IEEE 802.3ad LACP • LACP will negotiate the optimal parameters for both ends using LACPDU (Link Aggregation Control Protocol Data Unit)" (p273)
    "-> linkagg lacp agg <agg_num> size <size> admin-state enable -> linkagg lacp agg <agg_num> actor admin-key <actor_admin_key>" (p275)
  definition: |
    动态链路聚合协议：LACPDU 协商两端参数，可跨厂商对接服务器/存储；配置三元组=agg 编号+size+actor admin-key（本地意义）；监控 show linkagg agg N 的 Actor/Partner System Id/Key 字段。Auto-Fabric 也以 LACP 自动成聚合。
  alias_or_related: 静态聚合对照（仅 ALE 间，p273）
  tags: [protocol, linkagg, lacp]

- id: g43
  term: VRRP (RFC 2338 / 2787)
  full_name: Virtual Router Redundancy Protocol（p372 标题展开）
  category: protocol
  source_pages: p374-381, p383-390
  source_quote: |
    "RFCs Supported • RFC 2338 – Virtual Router Redundancy Protocol • RFC 2787 – Definitions of Managed Objects for the Virtual" (p375)
    "Multicast - 224.0.0.18 Virtual MAC address: 00-00-5E-00-01-{VRID}" (p375)
  definition: |
    网关冗余协议：虚拟 IP/MAC（00-00-5E-00-01-{VRID}）+组播 224.0.0.18 通告；优先级默认 100、默认抢占、间隔 100；跟踪策略五类（ADDRESS/IPV4-INTERFACE/IPV6-INTERFACE/PORT/VLAN）实现上行故障降级切换。实验输出 Version=V2。
  alias_or_related: 与 DHL/STP 的分工——VRRP 管三层网关冗余
  tags: [protocol, vrrp, gateway]

- id: g44
  term: RADIUS / TACACS+ / LDAP
  category: protocol
  source_pages: p70, p73, p202, p457, p472
  source_quote: |
    "Stored in the local user database and / or on external authentication servers ... Authentication Server RADIUS or LDAP" (p70)
    "Authentication Method • MAC-based (non-supplicant) or • 802.1x-based (supplicant) ... Filter-ID = 'UNP-name' } RADIUS Access-Accept + UNP name" (p457)
    "aaa radius-server server_name host ... [auth-port auth_port] [acct-port acct_port] ... auth_port 1812 acct_port 1813" (p472)
  definition: |
    外部认证三协议：RADIUS（管理面认证与 Access Guardian 设备认证，默认 1812/1813、建议 TLS；Filter-Id 属性回传 UNP 名）、LDAP（管理面认证）、TACACS+（出现于 UDP relay 服务清单 p357 与命令参数，书中未展开配置）。ASA 认证链可混排多服务器。
  alias_or_related: 实验服务器 192.168.100.102（实验口径）
  tags: [protocol, aaa, radius]

- id: g45
  term: 802.1X / PEAP / MSCHAPv2 / MAC 认证
  category: protocol
  source_pages: p28, p202, p457-458, p472, p481-483
  source_quote: |
    "Users must authenticate through 802.1x client • Authentication is based on either RADIUS, LDAP or TACACS+" (p202)
    "Authentication : Protected EAP (PEAP) • Check the box 'No CA certificate is required' ... Inner authentication: MSCHAPv2" (p481)
  definition: |
    端口准入认证族：802.1x（supplicant 侧 EAP，实验用 PEAP+免 CA+MSCHAPv2）、MAC 认证（non-supplicant，源 MAC 作账号密码）；两者可同端口并存（auto-sensing multi-client）；失败/无登记的降级见 Access Guardian。
  alias_or_related: R-Lab 客户端与无线客户端均有 802.1X 配置步骤（p28/p45）
  tags: [protocol, 8021x, access-guardian]

- id: g46
  term: 802.1Q / 802.1p
  category: protocol
  source_pages: p197-200, p291-297
  source_quote: |
    "4096 unique VLAN Tags (addresses) • VLAN ID == GID == VLAN Tag • 802.1P • Three-bit field within 802.1Q header • Allows up to 8 different priorities • Feature must be implemented in hardware" (p199)
  definition: |
    VLAN 标准与优先级位：802.1Q 头（4 字节）插 12 位 VLAN ID（4096 tag）+3 位 802.1p 优先级（8 级），硬件实现；一条链路承载默认 VLAN（未打标桥接）+其余打标 VLAN。
  alias_or_related: DSCP/ToS 为三层对应标记（QoS 章）
  tags: [protocol, vlan, 8021q]

- id: g47
  term: LLDP / LLDP-MED（IEEE 802.1AB）
  full_name: Link Layer Discovery Protocol（p486 标题展开）/ Media Endpoint Devices（p490 标题展开）
  category: protocol
  source_pages: p486-499, p501-505
  source_quote: |
    "IEEE 802.1AB – Link Layer Discovery Protocol (LLDP) ... L2 discovery protocol • Exchange information with neighboring devices to build a database of adjacent devices • Enabled by default" (p488)
    "LLDP-MED • Provides VoIP-specific extensions to base LLDP protocol • TLVs ... • Device location discovery ... • LAN policy discovery (VLAN, Layer 2 priority, Layer 3 QoS) • Extended and automated power management ... • Inventory management" (p494)
  definition: |
    二层发现协议与 VoIP 扩展：LLDPDU=必选 TLV（Chassis/Port ID/TTL）+可选 TLV（802.1/802.3/MED）；默认收发双开、30 秒间隔；LLDP-MED 四扩展=网络策略（应用类型+VLAN+l2-priority+dscp）、位置 ID、扩展供电（PSE/PD）、资产清单；配 mobile tag 支持 802.1Q 打标流量动态入 VLAN（与固定口 tagging 对照，p495）。
  alias_or_related: 配置层级限制见反例 n30；语音 VLAN 流程见 framework f28
  tags: [protocol, lldp, voip]

- id: g48
  term: SNMP（v1/v2/v3）
  category: protocol
  source_pages: p80, p84, p253
  source_quote: |
    "SNMP - IPv4 & IPv6 • Versions • SNMPv1 • SNMPv2 • SNMPv3 • Main applications to manage and supervise • Discovery • Topology • Access Guardian, UNP • Performance • Traps/Events..." (p84)
  definition: |
    网管协议：三版本并存（书未给安全对比），并发会话上限 50；支撑 OmniVista 发现/拓扑/性能/trap/UNP/RMON 取数等；作为 ip service 可被禁用或限源。
  alias_or_related: RMON 四组（Statistics/History/Alarms/Events）挂在其上（p253）
  tags: [protocol, snmp, nms]

- id: g49
  term: sFlow（RFC 3176）/ RMON
  full_name: Remote MONitoring（p233 展开 RMON）
  category: protocol
  source_pages: p253, p256-259
  source_quote: |
    "RMON probes are used to collect, interpret and forward statistical data about network traffic from designated active ports in a LAN segment ... 4 groups supported: • Ethernet Statistics ... • History Group ... • Alarms Group ... • Events Group" (p253)
    "Industry standard with many vendors • Delivering products with sFlow support (RFC 3176) ... One agent to represent whole switch ... One Sampler for each interface ... One Poller for each interface" (p257, p259)
  definition: |
    流量统计两件：RMON=端口探针四组（统计/历史/告警/事件）供 NMS 轮询；sFlow=交换机内嵌采样技术（Agent/Receiver/Sampler/Poller 四角色，采样包头+计数器经 UDP 送采集器），用于拥塞、DoS、应用 mix、容量规划等。
  alias_or_related: sFlow Collector 为第三方软件（p258）；Agent IP 可用 Loopback0（p360）
  tags: [protocol, sflow, rmon, monitoring]

- id: g50
  term: DHCP（Client/Relay/Option）
  category: protocol
  source_pages: p349-355, p367-371
  source_quote: |
    "The DHCP Client interface supports the release and renew functionality according to RFC -2131." (p350)
    "A DHCP relay agent can transfer DHCP messages between them ... Two types of DHCP relay agents: global and per-interface." (p353, p368)
  definition: |
    动态地址族：Client（RFC 2131，Option-1/3/51/58/59 落地、Option-60 串）；Relay（全局/接口两型互斥，max hops 16、Opt82、PXE 开关）；UDP Relay 为其姊妹功能（tftp/tacacs/ntp/nbns/nbdd/dns 端口转发）。
  alias_or_related: 实验服务器 192.168.100.102（实验口径）
  tags: [protocol, dhcp]

- id: g51
  term: ISIS-VC / SPB（Shortest Path Bridging 口径）/ MVRP / GVRP
  category: protocol
  source_pages: p155, p161, p328, p547, p552
  source_quote: |
    "VC topology managed by ISIS-VC" (p155)
    "Default SPB configuration • BVLANs 4000-4015 mapped to ECT-IDs 1-16 respectively • Control BVLAN: 4000 • Bridge priority: 0x8000" (p547)
    "MVRP enabled globally after LACP and SPB discovery process • Spanning Tree mode switch to flat" (p552)
    "DHL is not supported on mobile, 802.1x-enabled, GVRP, or UNI ports" (p327)
  definition: |
    自动化与二层的协议集合：ISIS-VC（VC 拓扑私有协议，全称未展开）；SPB（Auto-Fabric 默认 BVLAN 4000-4015↔ECT 1-16、控制 BVLAN 4000、桥优先 0x8000，4×9 秒邻接窗）；MVRP（VLAN 动态注册传播，Auto-MVRP 在 LACP/SPB 后全局启用并把 STP 切 flat）；GVRP 在 DHL 端口限制清单中出现（未展开）。
  alias_or_related: ECT-ID/ISID 书中未展开全称
  tags: [protocol, spb, mvrp, isis-vc]

- id: g52
  term: SSH（PKA/strong-ciphers/HMAC）/ HTTPS / FTP / Telnet
  category: protocol
  source_pages: p80, p88, p97, p533
  source_quote: |
    "Enable the enforcement of strong SSH ciphers (AES256 typically) ... hmac-sha2-256, hmac-sha2-512 ... -> ssh enforce-pubkey-auth ... follow instructions from 'OmniSwitch Switch Management Guide' on Secure Shell PKA" (p88)
    "RFCs Supported for SSHv2 RFC 4253 – SSH Transport Layer Protocol RFC 4418 – UMAC: message Authentication Code Universal Hashing" (p80)
  definition: |
    管理面传输协议族：SSHv2（RFC 4253/4418，会话上限 8，可强制强加密套件/强 HMAC/公钥认证 PKA）；HTTPS（WebView 强制，自签名证书）；FTP/Telnet（明文，可禁用）。升级通道可用 FTP/SFTP（p533）。
  alias_or_related: MFA（Google Authenticator/Duo）经 Application Note 扩展（p89）
  tags: [protocol, ssh, security]

- id: g53
  term: PoE / FPoE / PPoE / EEE（802.3af/at/bt、802.3az）
  category: protocol
  source_pages: p508-513, p516-520
  source_quote: |
    "Property 802.3af (802.3at Type 1) 'PoE' 802.3at Type 2 'PoE+' 802.3bt Type 3 '4PPoE'/'PoE++' 802.3bt Type 4 ... Power available at the PD 12.95 W 25.50 W 51 W 71 W" (p513)
    "Fast PoE : 2X60, 6360, 6860E, 6860N, 6865, 6870 ... Perpetual PoE : ..." (p510-511)
    "ENERGY EFFICIENT ETHERNET (EEE) – IEEE 802.3AZ STANDARD" (p512)
  definition: |
    以太网供电与节能：802.3af/at Type2/bt Type3/bt Type4 四档（PD 12.95/25.5/51/71W）；Fast PoE=上电即供、Perpetual PoE=重启不断电（型号线与 P10A 例外见反例 n32）；EEE（802.3az）空闲降功耗（仅铜口 100/1000M）；管理侧 lanpower（mW/W/优先级三档/delayed-start 120-600 秒）。
  alias_or_related: PSE/PD 口径（p513 表）；LED 琥珀=供电/绿=未供电（p509）
  tags: [protocol, poe, power]

- id: g54
  term: BUM / primary port / Mirror-to-port (MTP)
  category: protocol
  source_pages: p155, p281, p249
  source_quote: |
    "Maintains a loop-free topology for BUM traffic" (p155)
    "Multicast traffic is by default forwarded through the primary port of the Link Aggregation Group" (p281)
    "There is a limit of 4 Mirror-to-port (MTP) indexes." (p249)
  definition: |
    三个零散术语：BUM=广播/未知单播/组播流量口径（书中未展开全称）；primary port=聚合与 VC 的主端口（组播默认走它、VFL 有 Is Primary 成员口）；MTP=镜像目的口索引单位（上限 4，双向计 2）。
  alias_or_related: VC 主/备成员的角色词 Master/Slave 见 g09
  tags: [protocol, terms]

# ── 六、网站与资源名 (resource) ──

- id: g55
  term: rdp.al-mydemo.com / R-Lab（LanpodXa/Xb）
  category: resource
  source_pages: p12-24
  source_quote: |
    "https://rdp.al-mydemo.com/ - Username: LanpodXa or LanpodXb (X = R-Lab Number [1-32]) - Password: unique per session – Provided by the Instructor" (p14)
  definition: |
    本教材配套远程实验室入口：浏览器登录，账号 LanpodXa/Xb（X=1-32 号 POD），密码每会话唯一由讲师发放；POD 内 7 台交换机 + 10 Linux 客户端 + 无线客户端 + 公共服务器。纯教学基础设施（实验口径）。
  alias_or_related: POD 编号替换规则（如 EmployeesX 中 X=POD 号，p16）
  tags: [resource, lab]

- id: g56
  term: MyPortal（al-enterprise 门户）
  category: resource
  source_pages: p11, p120, p139, p229, p534
  source_quote: |
    "Partners Website • MyPortal" (p11)
    "OST 2.0 is a Windows-based application available for download free of charge via ALE MyPortal." (p229)
    "If you do the upgrade manually through SFTP / OmniVista Terra you will first need to download latest software package from MyPortal: https://myportal.al-enterprise.com/..." (p534)
  definition: |
    ALE 合作伙伴门户：软件包下载（按 Switches/WLAN/Network Management 分类，OS9900 在 Chassis Switches 等）、OST 2.0 下载、（对照 Rainbow 教材中另有 SR 用途，本书仅下载场景）。
  alias_or_related: ALE Web 站 www.al-enterprise.com/en 与培训页（p10）
  tags: [resource, portal, download]

- id: g57
  term: myfleet.ovcirrus.com（Fleet Supervision 入口）
  category: resource
  source_pages: p558, p563-568
  source_quote: |
    "Services Kiosk https://myfleet.ovcirrus.com/ ... Sign up and sign in • https://myfleet.ovcirrus.com/signup ... Declare • an OmniVista Management system ... OR Import your device list using the template file." (p558, p563)
  definition: |
    Fleet Supervision/Services Kiosk 的云入口：注册账号后声明 OV2500（取 OV2500 ID：Administration > Preferences > System Settings > Fleet Supervision）、OV Cirrus 4.X（URL+API Key，Security > External Apps）或 OV Cirrus 10.5+（URL+Organization ID+Application ID/Secret）；无 OmniVista 时以 CSV/XLSX 模板导入设备清单。
  alias_or_related: 免费；只读监管（p558 "Free of charge"）
  tags: [resource, fleet, portal]

- id: g58
  term: spacewalkers.com / github.com/ale-nsa-team（OST 1.0）
  category: resource
  source_pages: p11, p230
  source_quote: |
    "Spacewalkers Community • www.spacewalkers.com" (p11)
    "From Spacewalkers to github: https://www.spacewalkers.com/developers-center/omnivista-smart-tool • Or directly to github: https://github.com/ale-nsa-team/OmniVista-Smart-Tool ... OST 1.0 will remain in Github as a community available version" (p230)
  definition: |
    OST 1.0 的两个下载源（ALE 开发者社区与 GitHub 仓库）；Spacewalkers 同时是 ALE 用户社区站。1.0 社区维护、ALE 停止开发。
  alias_or_related: 2.0 走 MyPortal（g56）
  tags: [resource, ost, community]

- id: g59
  term: AOS 文档族（Specification Guide / CLI Reference / Release Notes / Switch Management Guide）
  category: resource
  source_pages: p9, p80, p158, p248, p251, p301, p422, p514, p533
  source_quote: |
    "OmniSwitch AOS Release 8 Specifications Guide ... Comprehensive resource to all Command Line Interface (CLI) commands ... OmniSwitch AOS Network Configuration Guide" (p9, p158)
    "We won't cover the upgrade process within these slides, as it is standard operation. Refer to latest AOS Release Notes for details on how to upgrade OmniSwitches." (p533)
  definition: |
    本教材反复回指的权威文档五册：Specifications Guide（会话数/VC/镜像/PoE 等型号规格）、CLI Reference（全命令）、Network Configuration Guide（策略条件组合表）、Switch Management Guide（PKA 等深配置）、Release Notes（升级步骤与前置固件）。生产化必须随手备查。
  alias_or_related: Transceivers Guide（光模块兼容，p9）
  tags: [resource, documentation]

- id: g60
  term: 合规认证源（FIPS 140-2 / JITC / Common Criteria）
  category: resource
  source_pages: p532
  source_quote: |
    "If you need to comply with a specific regulation, you need to check what is the current release validated for this regulation : • For FIPS 140-2 : https://csrc.nist.gov/... • For JITC : https://aplits.disa.mil/... • For Common Criteria : https://www.niap-ccevs.org/products/11404 or https://www.commoncriteriaportal.org/..." (p532)
  definition: |
    选版本时的合规查询三源：NIST FIPS 140-2 密码模块验证计划、DISA JITC 适配清单、NIAP/CC 产品目录（11404 为 ALE 条目号口径）。合规站点按这些清单选版本而非盲目最新。
  alias_or_related: 与签名镜像（8.10R4+）共同构成升级安全面（p531）
  tags: [resource, compliance, security]
```

---

## 收尾自检

### 1. BOOK_OVERVIEW.md 已列候选术语逐条核对

| OVERVIEW 术语 | 核对结论 | 对应条目 |
|---|---|---|
| ASA (Authenticated Switch Access) | 正文有明确定义（p95） | g02 |
| EMP | 有定义性用法（p78 机制描述 + p67 "Outbound IP interface" 标注），全称未展开 | 并入 g02 所属接入框架，EMP 独立口径见 BOOK_OVERVIEW 术语表（此处不单列避免重复）→ 补记于 passing 提及 |
| WebView | 有明确定义（p81） | g03 |
| Lightning Config (OLC) | 有明确定义（p103 展开 OLC） | g04 |
| Working / Certified / Running | 有明确定义（p141） | g05 |
| write memory flash-synchro | 有明确定义（p133） | g06 |
| Virtual Chassis (VC) / VFL | VC 有明确定义（p152）；VFL 仅有用法（全称未展开） | g07 / g08（VFL full_name 省略） |
| ISSU | 有明确定义（p162 标题展开） | g11 |
| UNP | 有明确定义（p456/p477，全称两写如实并列） | g13 |
| Access Guardian | 有明确定义（p455 目标页） | g15 |
| DHL Active-Active | 有明确定义（p326） | g16 |
| VRRP | 有明确定义（p372-375） | g43 |
| QSet / QSP / QSI | QSP 有 "Queue Set Profile" 用法、QSI 仅有命令用法（全称未展开） | g18（full_name 省略 QSI） |
| policy (condition/action/rule) | 有明确定义（p400） | g17 |
| LLDP-MED | 有明确定义（p490/494） | g47 |
| Auto-Fabric | 有明确定义（p538） | g21 |
| OST | 有明确定义（p217/224） | g19 |
| Fleet Supervision | 有明确定义（p558） | g20 |

结论：**18 行全部"本书正文有明确定义或定义性用法"，无"书中实际未出现"项。** EMP 一词按"不与接入框架重复"原则并入 passing 提及（见下）。

### 2. 本次新增、OVERVIEW 未列的术语
- 概念：AOS（g01）、AAA/ASA（g02）、UNP 分类规则（g14）、ssh-chassis（g12）、闪存三文件（g22）、Loopback0（g23）、VC 分裂防护（g10）、VC 选举（g09）、用户权限（g26）
- 角色：admin（g24）、default（g25）、admin-netadv（g27）
- 许可：Advanced/Data Center License（g28）、Demo License（g29）、支持合同（g30）
- 产品：OmniSwitch 各系列（g31-g37）、Stellar AP（g38）、RustConn/Proxmox（g39）、OmniVista 家族（g40）
- 协议：STP/RSTP/MSTP（g41）、LACP（g42）、RADIUS/TACACS+/LDAP（g44）、802.1X/PEAP/MSCHAPv2（g45）、802.1Q/802.1p（g46）、SNMP（g48）、sFlow/RMON（g49）、DHCP（g50）、ISIS-VC/SPB/MVRP/GVRP（g51）、SSH 族（g52）、PoE 族（g53）、BUM/MTP（g54）
- 资源：R-Lab（g55）、MyPortal（g56）、myfleet（g57）、Spacewalkers/GitHub（g58）、AOS 文档族（g59）、合规认证源（g60）

### 3. 仅 passing 提及、未单列条目的词（备查）
EMP（p67/p78-79，机制已并入 g02 语境与 principle p06）、PVST+（p305，Cisco 互操作字段，未展开）、BUM（g54 已并入）、MTP（g54 已并入）、DCE（p75 console 线序，未展开）、KERNEL.LNK（p130 启动镜像选择文件）、U-Boot/ONIE（p130/p533，引导层名词）、FPGA/CPLD（p510-511）、DER/PEM/PKCS#12/P7B/CRL/OCSP（p74 证书族）、GA/MR（p532 已展开）、PKA（p88 已展开）、AVLAN（p443，未展开）、DER 未见于本书、FileZilla（p450 实验工具）、TigerVNC（p40 实验桌面）、pfSense（p23 实验 NAT）、EF（p398，未展开）、SP（p397 已标注 Strict Priority）、DEI（p399/p422，未展开）、GVRP（p327，未展开）、UMAC（p80 RFC 4418 名称内）、PolicyView（p400，OmniVista 组件名）、AVR/RTF（p560 支持等级缩写，未展开）、GA/EoS/EoL（p560 生命周期缩写）、IPDSP 未见于本书（Rainbow 教材词，勿混）。

### 4. 提取口径说明
- 所有定义只采信本书正文；EMP/RCL/VFL/QSI/ISIS-VC/BUM/DCE/GVRP/AVLAN/DEI/ECT-ID/ISID/AVR/RTF 等书中未给全称的缩写，full_name 一律省略，不做外部补全。
- UNP 全称两写（User/Universal Network Profile）已在 g13 如实并列。
- 页码以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准，引用均为原文摘录；"Passing 提及"词仅记出现位置不造定义。
