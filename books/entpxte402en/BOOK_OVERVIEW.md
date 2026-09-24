# OmniPCX Enterprise 系统装载 (ENTPXTE402EN Ed12) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OmniPCX Enterprise — 系统装载 (Participant's Guide)
- **作者**: ALE Training Services
- **出版/发布时间**: Edition 12（OXE R101.1 MD4 时代；实验日期戳见 2024-08 / 2025-09）
- **内容类型**: 课程（官方售后培训讲义幻灯片 + 分步实验 How-To，讲义约占 55%、How-To 实验约占 45%；全书 17 个 How-To 实验）
- **版本来源**: `F:\AIwork\ZCode\books\entpxte402en\source_fulltext.txt`（ENTPXTE402EN · R101.1 MD4 · Edition 12 · 415 页）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To；主题是"把 OXE 的软件装上去、把云连起来、把许可管起来"）

### 一句话主旨
用 S.O.T. 部署工具完成 OXE 呼叫服务器从物理板卡到虚拟机到 GAS 一体机的全形态软件加载与补丁/多版本管理，接入 Cloud Connect 云基础设施完成 FTR 注册与 RTR 云许可，并掌握 Purple on Demand（OPEX）订阅模式下的 LMS 许可同步与运维。

### 骨架 (主要论点及其关系)

1. **RLAB 实验环境**（p1-20：全虚拟化 POD——PC Client、SOT VM、CS3、KVM（OXE+OMS）、GAS（OXE+OMS+WebRTC）五类节点，网段/账号/密码总表）
2. **S.O.T. 部署工具**（p21-48：ISO/OVA 交付、Standalone/Hosted 两模式、default/Template Factory（含降级模式）两配置、Easy/Expert 两工作模式、媒体三库、zip+MD5 更新与版本命名规则）
3. **CS 软件加载三场景**（p49-110：单版本全加载；静态/动态补丁在 active/inactive 分区；多版本双分区机制——复制+补丁 vs 完整加载+数据复制；N3 以下迁移硬规则）
4. **Easy Installation 分发器模式**（p111-130：客户环境不允许部署 SOT 时，OXE 自身当 Distributor，/tmpd 传输 + swinst 9-10 菜单本地加载）
5. **OXE-V 虚拟化**（p131-154：虚拟化技术矩阵 ESXi/Hyper-V/KVM/Nutanix/AWS、FlexLM 与 Cloud Connect 两条许可路径、OMS 软媒体网关（120 通道/台）、六种拓扑、安装三步）
6. **GAS 通用设备服务器**（p219-282：Rocky Linux+KVM 打包、内嵌 FlexLM、硬件前置表、SOT 加载、后安装向导、gasversion/gasbackup/UPS/host 升级等运维）
7. **Cloud Connect**（p283-349：XMPP over WSS 443 常驻 + SOCKS5 80 按需连 connect2.opentouch.com；FTR 首次注册（自动/手动/PIN 恢复）；RTR dongle-less 许可与 30 天资格期；Fleet Dashboard 五服务；CCTool/incvisu/日志体系）
8. **OPEX / Purple on Demand**（p350-408：LMS 云许可服务器与 lmsagent、lock 431、24 项订阅目录、三种消耗类型、OXE-LMS 同步与 panic 模式、C2P 转换、MyPortal 下载许可）

**论点之间的关系**: 递进为主——1 是地基，2 是全书工具主线（一切加载经 SOT），3-4 是加载的三种途径（SOT 常规、SOT 多版本、无 SOT 分发器），5-6 是两种现代承载形态（纯虚机、一体化打包机），7 把装好的系统接入 ALE 云（注册→许可→远程服务），8 在云连接之上再换一套商务与许可模型（OPEX）。17 个 How-To 实验穿插在各讲义章之后，形成"讲义→动手"节奏。

### 作者要解决的核心问题
让售后/渠道工程师独立完成 OXE 系统的软件交付：选对承载形态（物理 CS/虚拟机/GAS），用 SOT 完成版本与补丁加载（含客户现场无法部署 SOT 的替代路径），把系统接入 Cloud Connect（FTR/RTR）获得云许可与远程运维能力，并能按 OPEX/PoD 模式完成订阅许可的部署、同步与排障。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| S.O.T. (Software Orchestration Tool) | 部署 ALE 产品（物理或虚拟）的解决方案，核心是一台含 DHCP/FTP 服务的虚机；ISO 内含 OVA，Standalone/Hosted 两模式，default/Template Factory 两配置 | 它自身也要先被部署（VirtualBox/ESXi），加载工具与加载对象是两台机器；不是装在 OXE 里的程序 |
| Template Factory（含 degraded mode） | SOT 的第二配置：加第二块盘生成 VMware/KVM 镜像模板；降级模式绕过硬件前置（8CPU/16GB/500GB），只加 50GB 盘跑 templateFactory 命令 | "降级"是官方支持的绕过手段，不是故障态；首页会有警告横幅 |
| 多版本加载 (Multi version) | 同一块盘同时装两个版本（active/inactive 分区）；第二条版本可在不停话音的情况下装好，切换即重启，可回退 | 两条版本可以同版本不同补丁，也可以跨大版本（跨 Linux 版本时需完整加载+数据复制） |
| 静态/动态补丁 | 静态补丁必须停话音安装（或装在 inactive 分区），装在完整版本之后；动态补丁可在话音运行中安装，必须在对应静态补丁之后；补丁累积包含此前全部修正 | "静态/动态"的分界是"要不要停话音"，与一般软件的热补丁语义相反——动态才是热补丁 |
| Easy Installation / Distributor | 客户现场不允许部署 SOT 时的替代流程：BP 把 ISO/ZIP 传到 CS 的 /tmpd，OXE 以 swinst 9-10 菜单"当分发器"自己解包安装 | 加载工具从"另一台服务器"变成"被加载的机器本身"；全版本/静态补丁只能装 inactive 分区 |
| OXE-V | 专用于虚拟化环境的 OXE 呼叫服务器软件包；支持 ESXi/Hyper-V/KVM/Nutanix AHV/AWS | 虚拟化平台选择直接决定许可路径（FlexLM 只有 ESXi/KVM 可用） |
| OMS (OXE Media Services) | 软媒体网关虚机（OMS 软件+Suse OS），提供 GD4 板卡的媒体处理：VoIP 编解码、会议（3/6/14/29 方）、语音引导、音调；每台 120 VoIP 通道，每 OXE 最多 240 台 | 是"板卡的软件替身"，许可走 lock 384/385，可不停机安装 |
| GAS (Generic Appliance Server) | ALE 打包的通用设备服务器：Rocky Linux+KVM 之上承载 OXE、OMS、Rainbow WebRTC 三个 VM，内嵌 FlexLM；许可基于 ALU-ID 或 Cloud Connect ID | 它是"把硬件不确定性包起来"的产品：BP 自备服务器只要满足前置表即可；HP DL20 G11 只能跑 GAS 包 |
| PCS (Passive Communication Server) | OXE-V 拓扑中的被动通信服务器，可在 CS 信令链路故障时接管 OMS（CS→PCS 软复位，PCS→CS 硬复位） | PCS 不是备份 CS——云服务（FTR/RTR）明确不跑在 PCS 上 |
| Cloud Connect (CCI) | ALE 云基础设施：OXE 经 CC Agent 常驻 XMPP over WSS(443) 连 connect2.opentouch.com，按需 SOCKS5(80)；提供 RTR/Inventory/Offer/远程控制台/软件更新/Fleet Dashboard | 连接是 OXE 出站发起、不改客户防火墙策略；FQDN 固定为 connect2.opentouch.com |
| FTR (First Time Registration) | OXE 用基于 CC-Suite-ID 的临时激活账户向 CCI 换取永久凭证（CC-Product-ID+密码）的首次注册；新装机默认自动执行（每 4 小时重试），也可 CCTool 手动 | "注册"换来的是一对隐藏存储在 OXE 数据库里的凭证；备机禁止做 FTR（凭证经克隆同步） |
| FTR with PIN code | Panic Flag for RTR 后的恢复流程：向 helpdesk 申请 6 位数字 PIN（5 天有效），CCTool 重新注册并重置全部云配置 | PIN 不落盘、一次性；同时会删除其他激活账户并断开所有同 ID 产品 |
| RTR (Right To Run) | dongle-less 许可开关：不用硬件标识/加密狗，每日经 XMPP 向 RTR 服务器应答；OK +0.5 天 / NOK -1 天，归零进 Panic | 它不替代产品级许可（swk 照旧），只是总开关；"欺诈/复制"会让两个同 ID 系统同时扣天数 |
| Qualifying Period | RTR 资格期：初始化默认 30 天，逐日随应答增减；Fleet Dashboard 以 29-28/27-10/9-1/0 分四级显示 | 是"宽限期"的正式名字；期间话机显示"Call your administrator"、拒绝配置变更 |
| Fleet Dashboard | CCI 上的机队管理应用：RTR 状态、Inventory 资产、Offer 推/取、远程控制台、软件更新、告警展示 | 远程控制台限单会话、1 分钟无操作断开、每次登录记入 shell.log |
| LMS (License Manager Server) | OPEX 模式的云许可服务器：按项目建许可池；OXE 内 lmsagent 作为无状态 HTTPS 桥每 4 小时对账 | 许可从"装在机器上的文件"变成"云上池子的消耗额度"；OXE 侧只剩 lmsagent + spadmin 视图 |
| OPEX / Purple on Demand (PoD) | 订阅模式：用户/话务员/话务台/录音等许可由 LMS 管理；swk 中 lock 431=1 打开；订阅目录缩到 24 项 | 不是"云话音"——话音仍在客户 OXE 上，只有许可与订购上云（硬件仍 CAPEX） |
| OPEX activation flag | OXE 数据库中每个用户/设备的标志：激活时才向 LMS 请求许可；停用释放许可但保留配置 | CAPEX 模式下该标志"显示但不生效"（原书 Warning）——看到它不等于在计费 |
| C2P | CAPEX 转 PoD 的转换计划：MyPortal 工具基于既有软件锁与系统配置生成 PoD 项目，C2P 订阅件号 3EYxxxxxMA（PoD 为 3EYxxxxxAA） | 转换"下单即定局"；OPR/ALE Connect/Selfcare/VNA/API Management 与 IP Premium Security 不在 C2P 范围 |
| 双分区 (active/inactive) | 硬盘目录结构：/usr2//usr3//var 为活动版本，/root2_d//usr5//usr6//var2 为非活动版本，/usr4//usr7 为公共区 | 不是"备份"——非活动分区是可启动、可切换的第二版本；/usr4 还承担补丁中转（Rload） |
| checkCloudConfig.sh | OXE 内置连通性脚本：验证 DNS 解析 connect2.opentouch.com、443 XMPP/WSS、80 SOCKS5 三件事 | 只测 Cloud Connect & Rainbow 的连通性，DNS/代理配置也仅服务于这两个代理（原书 Notes） |

### 核心命题 (用自己的话)

1. 一切软件交付围绕 S.O.T.：它是一台自带 DHCP/FTP 的虚机，Standalone 模式装在技术员笔记本上加载物理设备，Hosted 模式跑在 ESXi 上加载虚机；同一套 Easy/Expert 项目逻辑覆盖所有目标。
2. 双分区是 OXE 升级的安全模型：装第二版本不打断话音，"切换"才重启；跨 Linux 版本走完整加载+数据复制，同版本走复制+补丁；回退随时可行，但板卡可能已拿过新二进制。
3. 补丁有严格顺序律：静态补丁必须停话音（或只装 inactive），动态补丁可热装但必须在静态之后；每个补丁累积包含此前全部修正，版本命名 N420536a 自带语义。
4. 客户现场不让架 SOT 时，OXE 自己当分发器：ISO/ZIP 传到 /tmpd，swinst 9-10 菜单解包安装，全版本/静态补丁强制 inactive 分区；解包物留在 /usr4/ftp/Rload 需手动清理，/tmpd 源文件自动删除。
5. 虚拟化平台决定许可路径：ESXi/KVM 可用 FlexLM+加密狗，Hyper-V/Nutanix/AWS 无 USB 重定向也无 FlexLM 虚机、必须走 Cloud Connect；FlexLM 与 RTR 两种许可模式不能同时启用（原书 Warning）。
6. GAS 用"打包"消灭硬件依赖：Rocky+KVM 固定底座，一台服务器最多 OXE+OMS+WebRTC 三个 VM；内嵌 WebRTC 网关 50 并发封顶，7000 用户以上必须外部网关；只认硬件 RAID。
7. Cloud Connect 的设计原则是"零改动入云"：OXE 出站发起，443 常驻 XMPP/WSS + 80 按需 SOCKS5，目标 connect2.opentouch.com；TLS 1.2 + ALE 自有 CA；DNS/代理配置仅服务这两个代理。
8. FTR 是一切云服务的门禁：订单链生成 CC-Suite-ID → .swk 落盘 → CCTool 用激活账户换永久凭证；凭证隐藏存库并自动克隆到 twin；PCS 与备机上不跑云服务。
9. RTR 把"能不能开机"变成云端对账：30 天资格期起，OK +0.5/NOK -1，归零 Panic（话机显示"Call your administrator"、拒绝一切配置变更）；复制 ID 会双双扣减，PIN 恢复是唯一出路。
10. Fleet Dashboard 把远程运维产品化：资产盘点、Offer 推/取、单会话远程控制台（1 分钟超时、shell.log 审计）、软件更新（给 AWS 仓库临时 URL，切换仍归 BP）。
11. OPEX/PoD 把许可从文件变成云池消耗：lock 431 开启后，24 个订阅项按 Unitary/On activation/By threshold 三种方式消耗；OXE 每 4 小时与 LMS 对账，lms/oxe 计数不一致或 30 天失联都会进 Panic。
12. 订阅消耗模型直接映射业务场景：酒店客房/客人各占 Room 许可、办公共享 DSU/DSS 各占一份 Voice Enterprise、tandem 副机不占许可——配置前先对消耗规则，再建用户。

### 论证链
教材以"环境 → 工具 → 场景递进 → 行为验证"推进：每个 How-To 都有明确的完成判据（SOT 网页 "completed" 状态、siteid 版本号变化、CCTool "FTR done!!/Registered"、checkCloudConfig.sh "Success"、spadmin 计数器 15|0/0|18 逐列解读），用可复现的行为闭环替代理论论证；选型部分用矩阵表支撑（虚拟化×许可、GAS 硬件×组件、RTR 状态×天数阈值）。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 R101.1 MD4 / Edition 12；虚拟化矩阵写死 ESXi 8.0/7.0、Hyper-V 2022/2019/2016、KVM ≥4.12.14，vSphere thick client 仅到 ESXi 6.0——平台版本迭代后矩阵需整体核对。
- OPEX 订阅目录"24 项"与件号（3EY945xxAA）是教材时点快照，商务目录动态变化。
- 实验截图含 2024-08/2025-09 时间戳，菜单与 Web 界面可能随版本漂移。

### 作者的立场盲点
- 全书默认 RLAB 实验环境：Superuser2580*、letacla/letacla1 等培训密码遍布正文；生产安全基线除密码 aging 处引用一次 CIS_Benchmark_Req.No_5.6.1.1 外没有展开，IP tables/trusted hosts 只教"加一条放行"。
- OXE 数据库管理（用户创建、编号计划、路由）被压成加载后清单里的一行"Perform basic management such as user creation… Or restore a backup"——本书只管"装上去"，不管"配起来"（作者自己指向 Starter 课程）。
- OPEX 章从运营商/厂商视角写计费与对账，客户最关心的"订阅超了会怎样"只用 panic 行为一段带过，无容量规划指引。

### 未被证明的假设
- 假设读者持有 MyPortal 账号与 BP 身份（下载 SOT/OXE 软件、开 PoD 项目、申请 FTR PIN、Fleet Dashboard 操作全部依赖）。
- 假设客户网络允许出站 443/80 至 connect2.opentouch.com 且 DNS 可解析公网（现成基线未核查）。
- 假设学员已会用 Filezilla/Putty/VirtualBox/Xming 等第三方工具（仅给下载链接）。
- 假设 GIP/HIS/板卡等硬件细节已在其他课程覆盖（shelves/boards into service 只有一行）。

### 最强反对意见
"这本教材教的是把 OXE 装起来、连上云、管住许可，它不教把这个系统交付成能打电话的PBX"——数据库与业务配置、话机开通、路由与编号计划都指向其他课程或"restore a backup"；同时 RTR/LMS 的 panic 机制意味着"连不上云 = 系统逐渐锁死"，生产交付必须把网络前提、证书/信任链、SPS 合同与 PoD 项目状态（Active）当作与软件加载同级的验收项。每个能力的 Boundary 必须标注"加载/云连接/许可"三口径之一。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] RLAB 类实验环境搭建与节点访问约定（IP/账号/密码表管理）
- [x] SOT VM 部署（Standalone VirtualBox / Hosted ESXi 两条线 + IP/键盘/账户初始化）
- [x] SOT 更新（zip+MD5、版本命名规则、同主版本限制）
- [x] SOT Template Factory 启用（标准前置 + 低资源降级模式）
- [x] SOT 媒体传输与项目配置（FTP/SFTP 2222 upload 账号、Declare media、Easy/Expert 项目字段）
- [x] OXE 单版本全加载（CS3/CPU8 网络引导 + 加载后操作清单）
- [x] OXE 多版本加载与分区切换（含 swinst 手工复制/切换附录）
- [x] 静态/动态补丁加载（active/inactive 两场景 + 顺序律）
- [x] Easy Installation 分发器模式（/tmpd 传输、9-10 菜单、Rload 清理）
- [x] OXE-V 虚拟化平台选型与许可路径决策（矩阵）
- [x] OXE VM 生成与加载（ESXi .ova / SUSE KVM 模板两条线）
- [x] OMS 加载与声明（KVM/ESXi 两线 + omsconfig）
- [x] GAS 加载（BootDVD+GAS iso、BIOS 取 MAC、PXE 引导）
- [x] GAS 后安装向导（国家码/OXE 参数/冗余/可选组件/WebRTC GW 参数/许可）
- [x] GAS 运维（gasversion/gasbackup/FlexLM 管理/host 升级/UPS）
- [x] OXE 云连接前提配置（netadmin DNS/代理 + checkCloudConfig.sh 验证）
- [x] FTR 执行与排障（CCTool、FTR with PIN 恢复）
- [x] RTR 启用与状态监控（WBM/CCTool/incvisu/Fleet Dashboard 状态解读）
- [x] PoD 许可下载（MyPortal Asset & service manager）
- [x] PoD 配置与 LMS 同步核查（spadmin 10/11/12、OPEX activation、Opex Licences 阈值、panic 排障）

### 不适合 skill 化的内容
- RLAB 实验环境细节与逐节点密码表（p1-20，教学专用基础设施，仅作 Boundary 背景）
- 7-zip/Xming/XLaunch/Putty 等第三方工具的点击级安装步骤（p38-39、p257-261 课堂操作）
- 培训评估/证书流程（p409-415）
- OXE 数据库业务配置（用户/路由/话机）——本书明确指向 Starter 课程，不在本书范围

### 预估 skill 数量
**约 10-12 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；入口软预算 8 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 搭建/接入 RLAB 类实验环境并掌握节点访问信息 | p1-20 | 可用的实验 POD（IP/账号/密码表） | 一切实验的地基 | 仅培训环境（实验口径） |
| task-02 | 部署 SOT VM（Standalone 或 Hosted）并完成首连初始化 | p37-48, p189-203 | 可访问的 SOT Web 界面 | 全书工具主线第一步 | 需 VirtualBox/ESXi 与 SOT ova |
| task-03 | 更新 SOT VM 并核对版本 | p47-48, p197-198 | 更新后的 SOT（About 可查） | 版本命名规则是补丁管理基础 | zip+MD5 媒体 |
| task-04 | 启用 Template Factory（标准/低资源降级模式） | p27-29, p155-165 | 可生成 VM 模板的 SOT | 虚拟化交付的前置 | 降级模式需 50GB 附加盘 |
| task-05 | 向 SOT 传输媒体并配置加载项目 | p84-87, p94-95, p101-102 | 项目就绪的 SOT | 所有加载场景的公共动作 | 媒体 iso/zip 从 MyPortal/NAS 获取 |
| task-06 | 用 SOT 完成 CS3/CPU8 单版本全加载 | p83-92 | 加载完成、密码/键盘/国家码设置好的 CS | 核心交付动作 | 需目标机 MAC 与网络引导 |
| task-07 | 多版本加载到 inactive 分区并执行切换 | p93-99 | 双版本在盘、按计划切换 | 升级不停机的关键能力 | Duplicate/Switch 参数决策 |
| task-08 | 在 active/inactive 分区安装静态与动态补丁 | p100-110 | 补丁版本就位（siteid 可验） | 日常维护高频动作 | 静态补丁停话音窗口 |
| task-09 | 用分发器模式（Easy Installation）加载版本与补丁 | p111-130 | 无 SOT 环境下的成功加载 | 客户现场约束下的替代路径 | /tmpd 传输 + trusted hosts |
| task-10 | 决策虚拟化平台并确定许可路径 | p133-136 | 平台×许可矩阵选型结论 | 架构错误的代价最高 | 生产需对照 TBE043 |
| task-11 | 生成并加载 OXE VM（ESXi .ova / SUSE KVM 模板） | p204-211, p166-176 | 运行中的 OXE-V CS | 虚拟化交付主路径 | Template Factory 或 hosted SOT |
| task-12 | 加载 OMS 虚机并在 OXE 数据库声明 | p177-188, p212-218 | 媒体资源就绪的 OMS | VoIP/会议能力来源 | 需 BootDVD 媒体 |
| task-13 | 用 SOT 加载 GAS 服务器 | p244-254 | GAS host + 三 VM 就位 | 一体机形态交付 | BootDVD+oxe_sws iso |
| task-14 | 执行 GAS 后安装向导（含 WebRTC GW 参数） | p255-271 | 完成基础配置的 GAS 系统 | 开局必经步骤 | 客户参数（IP/PBXID 等） |
| task-15 | GAS 日常运维（版本/备份/FlexLM/host 升级/UPS） | p236-241, p275-282 | 可运转的运维闭环 | 售后日常 | FlexLM 许可文件 |
| task-16 | 配置 DNS/代理并验证云连通性 | p316-321 | checkCloudConfig.sh 全绿 | FTR 的前提 | 客户网络出站策略 |
| task-17 | 执行 FTR（自动/手动）并掌握 PIN 恢复 | p322-331 | FTR Registered + XMPP_CONNECTED | 云服务门禁 | .swk 含 CCSID；MyPortal/BP 支持 |
| task-18 | 启用 RTR 并监控状态与事件 | p303-308, p331-337 | RTR_RUNNING + 资格期满值 | dongle-less 许可核心 | 先完成 FTR；重启一次 |
| task-19 | 从 MyPortal 下载 PoD 许可文件 | p381-385 | 各产品 .swk 许可包 | OPEX 交付起点 | 项目状态须 Active |
| task-20 | 配置 PoD 并核查 OXE-LMS 许可同步 | p386-408 | OPEX Flag=1、计数器一致、无 panic | OPEX 模式交付与排障 | LMS 侧项目与许可池已建 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-06 单版本全加载（核心交付动作，其余加载场景由此派生）
2. task-17 FTR 执行（云服务门禁，失败即全部云能力不可用）
3. task-08 补丁加载（日常维护最高频）
4. task-16 云连通性前提（FTR 排障第一入口）
5. task-02 SOT 部署（一切加载的工具前提）
6. task-20 PoD 配置与 LMS 同步（OPEX 模式主力场景）
7. task-07 多版本与切换（升级不停机的关键）
8. task-14/13 GAS 后安装与加载（一体机形态交付）
9. task-11/12 OXE-V/OMS 虚机交付
10. task-09 分发器模式、task-18 RTR 监控、task-10 平台选型、task-19 许可下载、task-15 GAS 运维、task-03/04/05/01（支撑类）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 8 个一级部分（环境 1 + 工具 1 + 加载三途径 2 + 承载两形态 2 + 云连接 1 + 订阅许可 1；收尾培训评估未计入）
- [x] 术语按实际内容列出（20 个）
- [x] 已检查作者局限/假设（培训密码、安全基线薄弱、数据库配置书外、MyPortal/BP 依赖、出站网络假设）
- [x] 原书关键任务 20 项，全部有来源页码、交付物与重要性依据
- [x] 用户已授权全流程连续执行（流水线任务指令，2026-09-23）

**用户确认时间**: 2026-09-23（流水线授权）
