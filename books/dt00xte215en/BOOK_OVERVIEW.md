# OmniSwitch LAN Access Switching (DT00XTE215EN Ed23) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OmniSwitch LAN Access Switching (Participant's Guide)
- **作者**: ALE Training Services
- **出版/发布时间**: OmniSwitch LAN - R8 / Access Switching - Edition 23（实验镜像出现 8.10.9.R04，历史截图残留 8.7.98.R03，见 p141/p504）
- **内容类型**: 课程（官方售后培训讲义幻灯片 + 分步实验 How-To；三日课程 Agenda 见 p6-8）
- **版本来源**: `F:\AIwork\ZCode\books\dt00xte215en\source_fulltext.txt`（587 页；素材目录标注为 Postsales on ALE Connect，**素材归类待确认**，PDF 实际内容为 OmniSwitch LAN Access Switching R8）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To，讲义约占 60%、实验约占 40%）

### 一句话主旨
把 OmniSwitch R8 接入/汇聚交换机从"开箱"带到"生产就绪"：登录与 AAA、闪存目录与配置生命周期、Virtual Chassis 堆叠、VLAN/链路聚合/STP/DHL 二层底座、IP 接口与 VRRP 网关冗余、QoS/ACL/Access Guardian 策略安全，收尾于 LLDP/PoE/软件升级/Auto-Fabric/Fleet Supervision 等运维周边。

### 骨架 (主要论点及其关系)

1. **课程行政与远程实验环境**（三日议程、R-Lab 拓扑、RustConn/Proxmox、Linux 与无线客户端操作、多交换机广播命令）
2. **产品组合**（OmniSwitch 全家桶按 Edge/Aggregation/Core 分层 + Stellar AP 产品线，仅选型背景）
3. **接入与管理基础**（AAA 认证框架、console/EMP/SSH/WebView/SNMP 五类接入、本地用户与密码策略、管理面加固、How-To：远程接入）
4. **快速开局**（OmniSwitch Lightning Config：端口 1 DHCP + HTTPS 192.168.0.1，模板下发，示例拓扑与环路避免警告）
5. **配置生命周期**（working/certified/running 三层模型、write memory / copy running certified / flash-synchro、回滚、配置与 USB 备份，How-To）
6. **Virtual Chassis**（堆叠即一台交换机：ISIS-VC、选举与接管、Auto VFL、分裂防护 RCD/VCSP、ISSU，How-To）
7. **二层与三层底座**（VLAN 静态/动态 UNP/802.1Q；链路聚合静态与 LACP；STP flat/1x1 与保护；DHL Active-Active；How-To×4）
8. **三层与网关冗余**（IP 接口/DHCP Client/DHCP Relay/UDP Relay/Loopback0/静态路由；VRRP 主备与负载分担，How-To×2）
9. **策略与安全**（统一 policy 引擎：QoS/ACL/PBR/策略镜像/auto-QoS；UserPorts/DropServices；Access Guardian=UNP+RADIUS，How-To×3）
10. **运维周边**（诊断工具箱 swlog/mirroring/monitoring/RMON/health/sFlow；LLDP-MED；PoE 管理；软件升级；Auto-Fabric 零触开局；Fleet Supervision；OST 2.0 安装，How-To×3）

**论点之间的关系**: 1-2 是地基与背景，3-5 是"接得上、开得了局、存得住配置"的生存技能，6-8 是组网能力（堆叠→二层→三层逐级向上），9 是在底座上叠加策略，10 是日常运维与规模化手段。How-To 实验章逐一对应各讲义模块，形成"讲义→CLI 逐条操作→show 验证"闭环；Day1≈骨架 3-7，Day2≈骨架 8+诊断+二层冗余，Day3≈骨架 9+LLDP/PoE（p6-8 议程），升级/Auto-Fabric/Fleet/OST 安装为议程外附加模块。

### 作者要解决的核心问题
让售后/渠道工程师独立完成 OmniSwitch R8 交换机的日常交付与维护：能登录并加固管理面、能快速开局、能理解并操作配置保存/认证/回滚机制、能组起堆叠与二层/三层冗余网络、能用统一策略引擎做 QoS/过滤/认证，并掌握诊断、升级与自动化开局工具。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| ASA (Authenticated Switch Access) | 交换机登录认证体系：Telnet/FTP/SNMP/SSH/HTTP/console/modem 均可挑战本地库或 RADIUS/LDAP；每类服务可单独 allow/deny | 不是"账号体系"本身，而是按"服务类型"逐个配置认证链的框架（p67-69、p85 还借它限制管理源 IP） |
| EMP | 旁路 NI 模块、直连 CMM 的管理口（p67 标注 "EMP (Outbound IP interface)"，全称未展开）；无 EMP 口机型可用 USB-to-Ethernet dongle 等效（8.9.R1 起） | 不只是"第二个网口"：它是 VC 分裂检测（RCD）与管理网隔离的物理底座 |
| WebView | 内嵌在交换机里的 Web 管理应用，单机视角，R8 默认强制 SSL；默认 enabled 但不允许认证，需 aaa authentication http | 与 OmniVista 不同：它只管一台交换机，且"服务开着≠能登录" |
| Lightning Config (OLC) | 零专家开局向导：交换机端口 1 起 DHCP（192.168.0.200/24），浏览器 https://192.168.0.1，从拆箱到通流量 <5 分钟/台 | 不是批量工具：一次一台、必须接笔记本、禁止预接线（p108）；模板以 .json 导入 |
| Working / Certified / Running | working=新文件的试验场；certified=授权用户认证过的默认文件；running=RAM 中当前运行配置；write memory 只同步到启动目录 | 与 Cisco "startup-config" 的关键差异：certified 是独立回滚基线，reload all 永远回 certified |
| write memory flash-synchro | = write memory + copy running certified（p133），一步完成"保存+认证"，VC 下还同步各成员 | 不是"多写一份"：它是生产收尾动作，forget 它下次重启即回滚 |
| Virtual Chassis (VC) / VFL | 多台交换机经 VFL（Virtual Fabric Link）互联呈现为一台逻辑交换机；拓扑由私有协议 ISIS-VC 维护，免许可证 | VC 成员间无 STP/VRRP；分裂时有 RCD（带外 EMP）与 VCSP（带内 helper）两套防护 |
| ISSU | In Service Software Upgrade：新代码放独立目录，逐台（chassis ID 从低到高）reload，最小化网络中断 | 升级不是覆盖 working：走 issu_dir，全 VC 共享同一套文件 |
| UNP (User Network Profile / Universal Network Profile) | 按用户/设备下发的网络档案：VLAN+ACL/QoS 策略列表+位置+时段；由 RADIUS Filter-Id 属性回传 | 书内两处全称不一致（p393 "User Network Profile"，p456/p477 "Universal Network Profile"）——同一概念 |
| Access Guardian | 基于 UNP 的角色接入控制：802.1x/MAC 认证、pass-alternate 降级、auth-server-down 策略、端口模板 | 它是特性集合名，不是独立进程；底座就是 VLAN 章的 UNP 分类规则 |
| DHL Active-Active | 双上行 VLAN 分流双活：LinkA/LinkB 各服务一组 VLAN，故障时 VLAN 切换到存活链路；DHL 端口自动禁 STP | 与 STP 二选一的方案；收敛快、双链路 100% 带宽，但每交换机仅 1 会话 2 链路 |
| VRRP | 默认网关冗余协议（RFC 2338）：虚拟 IP+虚拟 MAC 00-00-5E-00-01-{VRID}，组播 224.0.0.18 | 默认优先级 100、默认抢占；改优先级前必须先 disable 实例（p390 警告） |
| QSet / QSP / QSI | 每端口 8 个队列（QSI），队列集档案（QSP 1=8SP，QSP 2=1EF+7SP 等）定义调度与带宽 | QoS 不是先配策略：先懂端口队列模型，再进 policy 引擎 |
| policy (condition/action/rule) | 统一策略引擎：条件（L1-L4 关键字）+ 动作（accept/drop/deny、标记、限速、PBR、镜像…）+ 规则；qos apply 才生效 | QoS/ACL/PBR/镜像共用同一引擎；"ACL"=disposition 为 drop/deny 的 policy |
| LLDP-MED | LLDP 的 VoIP 扩展：网络策略（VLAN/L2 优先级/DSCP）+位置+扩展供电+资产清单；配 mobile tag 让话机打标流量动态入 VLAN | 与普通 802.1Q 的差别：话机从交换机 LLDP 帧里"学"语音 VLAN，不是手工配 |
| Auto-Fabric | 零触开局七步：Auto-VC→RCL 远程配置→Auto-LACP→Auto-Routing→Auto-SPB→Auto-Network Profiling→Auto-MVRP，另含 LBD 环路检测 | 首启提示语义相反：输入 Y 才是"禁用自动配置"，不答/答 N 都是启用（p539） |
| OST (OmniVista Smart Tool) | 装机/排障桌面工具：PoE 向导、一键修不启动的 PoE 设备、auto-ticket、流量分析；2.0 改 Client-Server+Postgres | 1.0（GitHub 社区版）已停更，2.0 经 MyPortal 免费下载但需有效 OmniSwitch 支持合同 |
| Fleet Supervision | 资产与合规监管云（myfleet.ovcirrus.com）：序列号/OmniVista ID 汇聚，看生命周期/支持状态/软件版本 KPI | 免费但只"看"不"管"：配置管理仍在 OmniVista/CLI |

### 核心命题 (用自己的话)

1. 交换机一切管理的入口是 AAA：五类接入（console/Telnet/FTP/HTTP/SSH/SNMP）各自可独立允许或拒绝，默认全部查本地用户库；管理面收缩（限源 IP、关服务、限会话数）与账号治理（密码策略、外部 RADIUS/LDAP、命令日志）构成第一道安全线。
2. 默认账号是 admin/switch，本地库最多 64 个用户；8.10R3 起登录警告、8.10R04 强制首登改密——默认口令残留是版本升级最容易漏的坑。
3. Lightning Config 把单台开局压到 5 分钟：笔记本 DHCP 接端口 1、浏览器进 192.168.0.1、Recommended Defaults 必做、admin 密码必改（≥8 位含四类字符、避开 ! 和 $）；新机未开局禁止与网络互联。
4. OmniSwitch 的配置可靠性模型是"三目录"：running(RAM)→working（write memory）→certified（copy running certified / flash-synchro）；重启默认回滚到 certified（与 running 内容相同则回 running），reload all 强制回 certified，从 certified 运行时禁止保存——理解这个模型才解释得清"改了配置重启就丢"。
5. Virtual Chassis 用私有 ISIS-VC 把多台合成一台：选举按优先级→运行时长（>10 分钟）→最小 chassis ID→最小 MAC；主备镜像文件与配置，故障接管 MAC 不变；分裂靠 EMP 带外 RCD 与带内 VCSP helper 防双主；升级走 ISSU 逐台滚动。
6. VLAN 有三条入口：静态端口成员（VLAN 1 不可删只可禁）、UNP 动态分类（9 条规则有严格优先级，Extended>Binding>Simple）、802.1Q 打标（4096 个 tag）；VLAN 没有活动端口时其 IP 接口保持 DOWN 且不参与路由。
7. 链路聚合两条路：静态（参数两端必须一致、仅 ALE 设备间）与 LACP（802.3ad，可接服务器/存储）；负载分担 hash 默认值因型号而异（brief/extended），组播默认只走主端口。
8. 环路避免三选一：STP（flat 单实例 / 1x1 每 VLAN 一实例，RSTP 收敛 <1 秒）、DHL Active-Active（双上行 VLAN 分流、端口自动禁 STP、恢复抢占默认等 30 秒、需配 MAC flushing 防 stale 表项）；两套方案不要混用同一链路。
9. 三层侧的出厂路径：IP 接口挂 VLAN 即启动路由；DHCP Client/Relay 解决地址与跨网段取址（全局与接口级互斥）；Loopback0 是最稳定的管理/协议源地址；静态路由默认优先于动态路由。
10. VRRP v2 提供网关冗余：虚拟 IP+MAC 让终端无需重新 ARP；主备由优先级（默认 100）与抢占决定，改优先级必须先 disable 实例；同优先级时最低 router ID 胜出。
11. QoS/ACL/PBR/镜像共用一个策略引擎：condition+action+rule，qos apply 才下发硬件；默认 disposition 为 accept（不匹配即放行）；UserPorts/DropServices 两个保留组做反欺骗与危险服务丢弃；auto-QoS 按 ALE 话机 MAC 段自动给优先级 5。
12. Access Guardian=UNP+RADIUS：认证成功后 RADIUS 以 Filter-Id 回传 UNP 名，用户按档案进 VLAN/吃策略；服务器不可达走 auth-server-down 降级档案，RADIUS 没登记的 MAC 认证一律 Block。
13. 运维闭环：诊断有 swlog/可读事件日志/command-log/镜像/抓包/RMON/health/sFlow 八件套；升级以最新 GA/MR 为基线（8.10R4 起全系列签名镜像）；Auto-Fabric 七步零触开局（首启 Y/N 语义相反）；Fleet Supervision 免费看资产合规，OST 2.0 免费装机排障（需支持合同）。

### 论证链
教材以"Goal→How it works→CLI Step by Step→How-To 实验→Thank You"推进：讲义给机制图与命令清单，How-To 给逐条 CLI 与真实 show 输出（含重启、断链等破坏性验证），并以开放式问题（"Is the ping still working?"、"What determines which side of the link is blocking?"）强迫学员从行为反推机制。规格类断言（型号容量、会话数、PoE 预算）一律回指 Specification Guide/datasheet，本教材不做权威数值承诺。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 R8（实验镜像 8.10.9.R04）与 Ed23 界面；WebView 截图、hash 默认值、PoE 型号支持（如 OS6360-P10A 不支持 FPoE/PPoE）都随版本漂移；书中多处输出截图仍是 8.7.98.R03（p504 LLDP System Description）。
- OST 1.0 已宣布停止开发（p230），2.0 刚转向 Client-Server——按 1.0 习惯办事的存量资料很快失效。

### 作者的立场盲点
- 全书是"单交换机/单 POD 的 CLI 视角"：OmniVista Terra/Cirrus 只在升级与 OST/Fleet 处露脸，没有任何多站点变更管理、配置基线比对、自动化（Ansible/API）内容。
- 安全只讲交换机侧：RADIUS 服务器用什么、用户库怎么建全书不教（实验直接用现成 AAA Training Server 192.168.100.102）；证书体系只在 IEC62443/convert-cert 处点到。
- 生产割接流程缺位：变更窗口、灰度、回退演练、"谁批准 copy running certified"这类治理问题书内无一处涉及。
- 数值参数大量"回指规格指南"（镜像会话数、PoE 预算、每型号 VC 上限的完整矩阵），现场若不带 Specification Guide 会反复卡壳。

### 未被证明的假设
- 假设学员持有讲师发放的 R-Lab 账号（LanpodXa/Xb，每会话密码）；假设 DHCP/RADIUS/FTP/Web 服务器（192.168.100.102）现成可用。
- 假设读者懂 IP 寻址——Lightning Config 明说"不懂就停下来找方案架构师"（p108）；STP/LACP 模块也只做 reminder 不做推导。
- 假设 POD 拓扑（6900-A/6870-A/6860-B/6360 VC）就是学员的生产缩影，未讨论不同硬件代际混布的例外。

### 最强反对意见
"这是实验册，不是配置参考"——大量机制只有一页 how-it-works（VCSP helper、RCL、auto-fabric 各协议细节、LLDP mobile tag），真正可执行的参数边界在 Specification Guide / CLI Reference / Release Notes 里；把本教材当唯一依据，会在型号差异参数（镜像会话数、PoE 预算、VC 混插规则）和版本门槛（8.9.R1 USB dongle、8.9R4 X48C4E 混插、8.10R4 签名镜像）上翻车。因此每个能力的 Boundary 必须标注"实验口径"，并把规格指南列为生产化必备外置文档。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] 远程实验室接入与客户端操作（仅作 Boundary 背景，不独立成 skill）
- [x] 交换机登录与 AAA 接入框架（五类服务认证链、fail-through、exit-on-fail）
- [x] 本地用户与密码策略治理（user/password-policy 系列、外部 RADIUS/LDAP 声明）
- [x] 管理面加固清单（ASA 限源、禁不安全服务、会话参数、SSH 强加密、banner、MFA 指针）
- [x] WebView 远程管理（会话参数、VLAN 增删、机框可视化）
- [x] Lightning Config 单机快速开局（含模板 .json 与禁令清单）
- [x] 闪存目录与配置生命周期操作（write memory/copy running certified/flash-synchro/reload 语义/回滚）
- [x] 配置备份恢复与 USB 备份（.tar 备份、usb backup/auto-copy、加密）
- [x] Virtual Chassis 规划与配置（ID/组/优先级/VFL 静态与 auto）
- [x] VC 运维（分裂防护 RCD/VCSP、ISSU、ssh-chassis、一致性检查）
- [x] VLAN 配置三入口（静态/UNP 动态分类/802.1Q）
- [x] VLAN 间路由与 IP 接口（DHCP Client/Relay、UDP Relay、Loopback0、静态路由）
- [x] 交换机诊断八件套（swlog/事件日志/command-log/镜像/抓包/RMON/health/sFlow）
- [x] 链路聚合（静态/LACP、hash 控制、冗余测试）
- [x] STP 模式/协议/优先级/保护与 1x1 负载分担
- [x] DHL Active-Active 部署（会话/vlan-map/MAC flushing）
- [x] VRRP 网关冗余（基本/完整配置、跟踪策略、主备指定）
- [x] QoS 配置（端口信任/默认标记/策略三件套/auto-QoS/PBR/远程与策略镜像）
- [x] ACL 与用户口安全（L2/L3/ICMP/HTTP/FTP 过滤、UserPorts、DropServices、BPDU shutdown）
- [x] Access Guardian 部署（UNP 档案/RADIUS/802.1x/MAC/pass-alternate/auth-server-down）
- [x] LLDP/LLDP-MED 与 IP 电话语音 VLAN（network-policy/mobile tag）
- [x] PoE 管理与监控（预算/优先级/Fast/Perpetual/delayed-start）
- [x] 软件镜像升级路径（签名镜像、推荐版本、三种升级通道、U-boot 警示）
- [x] Auto-Fabric 零触开局与 LBD
- [x] Fleet Supervision 开通（OV2500/Cirrus/CSV 三种资产来源）
- [x] OST 2.0 安装与接入（Postgres/Server Config/加交换机）

### 不适合 skill 化的内容
- R-Lab 实验环境细节（rdp.al-mydemo.com、LanpodXa 账号、POD 编号规则、Proxmox/RustConn 操作，p12-51）——教学专用基础设施，仅作 Boundary
- 产品组合营销页与 Stellar AP 参数表（p52-64，选型查 datasheet）
- Console 线缆实物连接图（p522-528，按机型随机附件即可）
- 培训评估与证书流程（p581-587）
- Quiz 占位页（p570）

### 预估 skill 数量
**约 11-13 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；入口软预算 8 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 连接远程实验室并操作 Linux/无线客户端 | p12-51 | 可用的实验接入 | 全部实验的前置 | R-Lab 账号由讲师发放（实验口径） |
| task-02 | 经 console/EMP/SSH/WebView/SNMP 登录交换机 | p65-90 | 多通道可用的管理接入 | 一切配置的前提 | 无 |
| task-03 | 管理本地用户、密码策略与外部认证服务器 | p70-74, p472-474 | 合规的账号体系 | 安全底线；8.10R04 强制改密 | 生产需自建 RADIUS/LDAP |
| task-04 | 加固交换机管理面 | p77-89 | 收敛的管理面 | ASA 限源/禁服务/SSH 强加密/MFA | MFA 细节在 Application Note（书外） |
| task-05 | 用 WebView 远程管理与验证 | p91-101 | WebView 可用并建删 VLAN | 远程排障常用入口 | 无 |
| task-06 | Lightning Config 快速开局与模板下发 | p102-126 | 开局完成的交换机 | 小网络交付主路径 | 需自备 IP 规划 |
| task-07 | 管理闪存目录、保存/认证/回滚配置 | p127-149 | 受控的配置生命周期 | 防配置丢失的核心机制 | 无 |
| task-08 | 组建与维护 Virtual Chassis | p150-182 | 稳定运行的堆叠 | 汇聚/核心高可用基础 | 分裂防护需 EMP/helper 规划 |
| task-09 | 配置静态/动态 VLAN 与 802.1Q | p183-214, p291-297 | 按部门隔离的二层 | 交换基本功 | 无 |
| task-10 | 配置 VLAN 间路由与 IP 接口 | p194-196, p345-366 | 三层可达的网络 | 路由启用条件与网关设计 | 无 |
| task-11 | 用 OST 安装交换机与收集排障信息 | p215-231, p572-580 | 装机/排障工具可用 | 一线装机效率工具 | OST 2.0 需支持合同 |
| task-12 | 运用诊断八件套排障 | p232-269 | 可定位问题的证据链 | 售后日常 | 规格上限查 Specification Guide |
| task-13 | 配置链路聚合并验证冗余 | p270-290 | 冗余上行链路 | 带宽+可靠性基础 | 静态仅限 ALE 互联 |
| task-14 | 配置 STP 并做 1x1 负载分担 | p298-323 | 无环且双活的二层 | 环路避免标配 | 无 |
| task-15 | 配置 DHL Active-Active | p324-344 | 双上行分流方案 | STP 替代方案、收敛更快 | 与 STP 互斥于同一链路 |
| task-16 | 配置 DHCP Client/Relay 与 UDP Relay | p349-371 | 跨网段自动取址 | 用户网段标配 | 需 DHCP 服务器 |
| task-17 | 配置 VRRP 网关冗余 | p372-390 | 不间断的默认网关 | 网关高可用 | 无 |
| task-18 | 配置 QoS（含 auto-QoS/PBR/镜像） | p391-428 | 受控的流量优先级 | 语音/关键业务保障 | 队列模型随型号差异查规格 |
| task-19 | 配置 ACL 与用户口安全 | p429-453 | 按策略过滤的边界 | 安全边界标配 | 无 |
| task-20 | 部署 Access Guardian（UNP+RADIUS） | p454-485 | 角色化接入控制 | 准入+动态策略一体 | RADIUS 服务器侧配置在书外 |
| task-21 | 配置 LLDP/LLDP-MED 语音接入 | p486-505 | 话机自动入语音 VLAN | IP 电话场景刚需 | 无 |
| task-22 | 管理与监控 PoE | p506-521 | 供电可控的端口 | AP/话机/摄像头供电 | 每型号预算查 datasheet |
| task-23 | 升级软件镜像 | p529-535 | 修复与安全合规的版本 | 安全流程强制项 | U-boot/FPGA 升级失败即 RMA |
| task-24 | 部署 Auto-Fabric 零触开局 | p536-554 | 自动成网的新站点 | 规模化部署利器 | 细节依赖 vcboot.cfg 模板设计 |
| task-25 | 开通 Fleet Supervision 资产合规监管 | p555-569 | 资产/生命周期看板 | 服务续约与合规证据 | 需 myfleet 账号与资产来源 |
| task-26 | 安装 OST 2.0 并纳管交换机 | p572-580 | 可用的 OST 2.0 | 2.0 新架构落地 | Postgres 18.1 先装 |

### 优先级排序 (按"最能保障售后工程师交付质量"的角度)
1. task-07 配置生命周期（不懂 working/certified 一切排障都是猜）
2. task-02/04 登录接入与管理面加固（进门+不被人进门）
3. task-09/10 VLAN 与三层接口（网络基本盘）
4. task-13/14/15/17 冗余四件套（LAG/STP/DHL/VRRP）
5. task-08 Virtual Chassis（汇聚层主流形态）
6. task-19/20 ACL 与 Access Guardian（安全边界）
7. task-12 诊断八件套（售后日常）
8. task-18 QoS（语音场景刚需）
9. task-21/22 LLDP-MED 与 PoE（终端供电接入）
10. task-16/06/23/24/25/26/11/01/03/05（一次性或支撑类任务）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 10 个一级部分（1 地基 + 选型背景 1 + 接入/开局/生命周期 3 + 组网 3 + 策略 1 + 运维周边 1）
- [x] 术语按实际内容列出（16 个）
- [x] 已检查作者局限/假设（实验口径、规格数值外置、RADIUS 服务器侧缺位、割接治理缺位）
- [x] 原书关键任务 26 项，全部有来源页码、交付物与重要性依据
- [x] 用户已授权全流程连续执行（流水线任务书，2026-09-23）

**用户确认时间**: 2026-09-23（全流程授权）
