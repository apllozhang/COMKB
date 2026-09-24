# OmniPCX Enterprise Starter (ENTPXTE400EN Ed12) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OmniPCX Enterprise - Starter (Participant's Guide)
- **作者**: ALE Training Services
- **出版/发布时间**: Edition 12（OXE R101.1 MD4 时代；书中实验输出含 2024-2025 年时间戳、chronyd 3.5、Rocky Linux 9.6 "Blue Onyx"）
- **内容类型**: 课程（官方售后培训讲义幻灯片 + 分步实验 How-To，讲义约占 55%、实验约占 45%）
- **版本来源**: `F:\AIwork\ZCode\books\entpxte400en\source_fulltext.txt`（821 页，全书最厚一本）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To；每个讲义章后跟随对应实验章，实验给出逐键菜单路径与验收命令）

### 一句话主旨
把一台 OmniPCX Enterprise（OXE）从"能登录"带到"能打电话"：物理/虚拟/云承载形态识别、安全登录与密码治理、IP 与防火墙、系统启停、空库与许可恢复、机架板卡上架、用户终端开通，再到编号计划/COS/语音指南/话务台/Entity/4645 语音邮件，最后打通公共 SIP 中继（ARS/DID/闭锁/紧急呼叫）并掌握备份恢复与维护排障工具。

### 骨架 (主要论点及其关系)

1. **实验环境**（RLAB 全虚拟/混合两种 POD 拓扑 + ITSP1 SIP 运营商模拟器：POD 号 PN 编号规则、账号、双 SIP 网关）
2. **系统概览**（OXE=Linux 软件交换机；CS+MG 组件；话机/话务台/资源；单机与组网拓扑； duplication/PCS；加密；Rainbow/Cloud Connect/WBM/OV8770/UMC 管理工具矩阵）
3. **硬件架构与虚拟化**（Common HW 机架板卡 GD-4/GA-4/MIX；OXE-V/OMS 虚拟化；GAS；Crystal 退场与 XL 机架补位；混装上限 240 racks）
4. **连接登录与密码安全**（V24/SSHv2/console；mtcl/swinst/root/client 四账户；14 位密码策略；失败锁定与老化）
5. **系统启停**（swinst Easy/Expert 菜单、RUNTEL、autostart、role 状态、一键取消自启窗口）
6. **IP 环境与内部防火墙**（物理地址+Role MAIN 地址双体系；netadmin；N3 起默认 iptables 白名单、可信主机与批量导入）
7. **时间同步**（六种对时途径；chrony/NTP 两阶段同步法）
8. **数据库与许可**（MAO 数据库、空库创建即抹许可；OPS 四文件；CAPEX 本地锁 vs OPEX 云锁；RTR/CC-SUITE-ID；软件保护降级模式三阶段）
9. **配置工具与硬件上架**（mgr/WBM/OV8770/UMC 四工具；GD4/OMS/XL 三类媒体网关上架：mgconfig/omsconfig、crystal number、MAC 校验、压缩器声明）
10. **用户与基础业务**（终端系列与开通三法；IPDSP；TDM 功耗约束；内部 DHCP；前缀/后缀计划；Phone Features COS 与 Connection/Transfer COS）
11. **呼叫处理业务域**（静态语音指南与 MOH；话务台组/4059EE/BLF；Entity 与 CDT；OmniMessage 4645 语音邮件与邮件通知）
12. **公网接入与安全**（公共 SIP 中继全链路：TG→ARS→鉴别符→NPD→DID→回拨翻译器；外呼闭锁 Public COS×Area；紧急呼叫通知与 Location ID；呼叫分配计时器）＋**运维收尾**（DB 备份恢复含 Cloud/Rainbow 剥离选项、维护工具八件套、T0/T2 中继组、UMC 云管理；p815-821 培训评估为附注）

**论点之间的关系**: 先环境后系统、先底层后业务——1 是地基；2-3 建立系统观；4-8 是"碰机器"的准入链（登录→启停→网络→时间→库与许可，顺序即实验顺序，前一步是后一步的前提）；9-10 把硬件和用户配出来；11-12 是两大业务域（内部呼叫处理、外部公网互通），彼此独立但都依赖 6/8/10；运维收尾段与业务域并列，是日常运营抓手。全书的"任务-工具"对位关系：库/许可/网络/时间类任务走 swinst+netadmin+CLI，业务类任务走 WBM/mgr，排障走专用命令（role/config/trkstat/sipextgw/oxetrace…）。

### 作者要解决的核心问题
让零基础售后/渠道工程师在培训后能独立完成一台 OXE 的基础开局与日常维护：从拿到一台裸机（物理或虚拟）开始，安全登录、配网络、启停系统、建库授权、上架媒体网关、开通用户与基础业务，直至接入运营商打通用外线，并具备备份恢复与第一线排障能力。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| OXE (PABX) | 基于 Linux OS 的软件专用交换机，跑在 IP 数据网上；管内部通信+外线互通 | 不是一台"交换机盒子"，是软件方案；承载硬件可选四种 |
| Call Server / OXE-V | 系统控制中心；虚拟化形态叫 OXE-V，跑在 VMware/KVM/Hyper-V/Nutanix/AWS 上 | CS 既是软件也是板卡（CS-3）；虚拟机与物理机功能/限额相同 |
| OMS | OXE Media Service：原生虚拟化的软件媒体网关，提供 GD-4 的媒体功能（120 压缩器，支持 OPUS/G722） | 与"虚拟机里的话机网关"直觉不同：它替代的是机架+GD-4 板，不是话机 |
| GAS | Generic Appliance Server：Rocky Linux+KVM 之上的一体化 OXE 载体，FlexLM 内嵌、免加密狗 | 不是 ALE 专用硬件品牌机，而是"硬件无关的参考服务器形态" |
| MAO | OXE 数据库（Maintenance Administration Operation），存客户配置 | 不是"数据库软件"泛称，是 OXE 专有配置库的专有名 |
| OPS | 许可文件组（xx.swk/xx.hw/hardware.mao/xx.zip）；购买许可=交付 OPS 文件，装入后才解锁功能 | 不等于"license key 文本"；空库创建会把 OPS 一起抹掉 |
| RTR | Right To Run：基于 Cloud Connect 的运行权校验，CC-SUITE-ID 终身不变 | 是"开机权"而非功能许可；断连时的容错口径书中未展开 |
| swinst | "Facilities"系统账户+安装菜单（Easy/Expert），管启停/备份/恢复/日期/账户 | 既是账户名也是菜单入口；root 下进入免密 |
| netadmin | IP 网络管理工具（完整安装/菜单模式 netadmin -m），管地址、Role、防火墙、DHCP、SMTP、主机表 | 改完必须 Apply + 重启系统才生效；不是实时生效的配置中心 |
| WBM | Web Based Management：OXE 内嵌免费 Web 管理（HTML5，仅 HTTPS），管用户与业务对象 | 与"OmniVista"不同：内嵌零安装零许可；只搜参数名不搜值 |
| ARS | Automatic Route Selection：按被叫号码选路由（表≤10 路由），是 SIP 中继可用的强制机制 | SIP 中继不能直抓，必须经 ARS 前缀+鉴别符走 |
| NPD | Numbering Plan Description：定义主/被叫号码格式（ISDN International 等）、默认号码与 DID 翻译器选择 | 不是编号计划本身，是"对外号码格式+CLI 组装"的描述符 |
| DID translator | 公外号码段↔内部分机段的翻译器（首外号+首内号+范围） | 同时服务来话落地与去话 CLI 组装，双向都要配 |
| Public COS (Access COS) | 按 Area（区号分组的外呼规则）×四种实体状态控制用户外呼权限的类别，共 32 个 | 与 Phone Features COS 是两套 COS：一个管"能打哪些外面号码"，一个管"能用哪些功能" |
| Entity | OXE 逻辑分区（0-1000），绑定用户/中继/话务台，各有 CDT/状态/安装号/等待音 | 不是"站点"；单机内即可多 Entity，默认用户归 Entity 1 |
| CDT | Call Distribution Table：四状态（Day/Night/Mode1/Mode2）×3 路由+1 溢出号 | 不是 ACD 队列；溢出号必须是单线分机 |
| Attendant group / 4059 EE | 话务台组（每节点≤50 组，组内并行/轮转呈现）与 4059 Extended Edition PC 话务台（不处理语音，必须关联话机/IPDSP） | 话务台≠总机话机；4059 只是操作台，声音走关联话机 |
| OmniMessage 4645 | 纯软件语音邮件，可嵌 CS/GAS/OXE-V 或独立/虚拟机；每 OXE 节点仅一个 VM 系统 | "4645"不是硬件型号而是软件品牌；基础语音指南不可从话机录音 |
| chrony | OXE 自 R101 起内置的 NTP 实现（chronyd），支持渐进/瞬时两种同步 | 对时不再是"改一次日期"，而是常驻服务+客户端/服务器双角色 |

### 核心命题 (用自己的话)

1. OXE 是软件交换机，承载形态四种并存：Common HW 机架、虚拟机 OXE-V（5 种 hypervisor）、GAS（Rocky Linux 一体机）、Crystal CPU（退场中，由 XL 机架补高密度模拟口）；同一系统可混装，上限每节点 240 racks。
2. 系统准入走"账户-密码-防火墙"三道门：mtcl/swinst/root/client 四账户分工明确；root 只能本地直登、IP 侧必须 su；密码 ≥14 位多规则、失败 3-5 次锁 15 分钟、可强制 10-366 天老化（RADIUS 场景必须关闭老化）。
3. 双 IP 地址体系是理解 OXE 网络的钥匙：物理接口地址永远可达（含话务应用停止时），Role MAIN 地址只在话务应用运行时生效——所有设备与外部应用必须指向 Role 地址。
4. 安全基线从 N3 起默认全关：内部 iptables 防火墙默认 DROP 入站/转发、放行出站；一切外部互通靠"可信主机"白名单（单个/网段/域名/CSV 批量导入），"Allow SSH for all"只是开局临便门，配完必须关回。
5. 系统时间影响计费/留言/排障，用 chrony 做渐进同步（client/server 模式，UDP 123），首次装机用瞬时同步（需先停 chronyd）把钟先拨对。
6. 数据库与许可是一对：MAO 存配置，OPS 存许可；空库创建必然连 OPS 一起抹掉，所以"建空库→恢复 OPS→再起话务应用"是固定顺序；软件每 5 天自查 OPS，不一致先给 30 天宽限再进降级模式（话务台告警→4 小时后全机提示并禁内呼→循环）。
7. 许可双轨制：CAPEX 锁在本地 OXE（xx.swk+CPU-ID/Product-ID/ALU-ID），OPEX 锁在云端 LMS（R100.1 起 Purple on Demand）；RTR 运行权挂在 Cloud Connect 的 CC-SUITE-ID 上，终身不变。
8. 硬件上架三条线一个套路：机架/Shelf（地址=crystal number，1-255 且 18/19 保留）→ 板卡（OPS 自动建，位置不锁死）→ GD4/OMS/XL 的 GD 板自身配 IP+CS Role 地址（mgconfig/omsconfig），自动分配 crystal number 或 DHCP 时必须在 CS 库登记 MAC 并勾"Ethernet Address checked by TFTP"。
9. 用户开通三法按终端形态分：IP 话机绑 MAC（自动分配=插线输分机+密码）、IPDSP 绑 Phone Identifier、TDM 绑机架/板/端口物理地址；用户分机号全系统唯一、最长 8 位，初始密码统一 0000。
10. 编号计划是全系统的路由地基：每个前缀唯一对应一个功能，最长 8 位（0-9ABCD*#）；计划饱和用 Timer 23（默认 3 秒）区分"31T 功能前缀"和"31000 分机"；语音指南必须与计划一致，改前缀不改指南会误导用户。
11. 两套 COS 各管一摊：Phone Features COS（256 类）管功能开关与保护（1=允许 0=禁止），Connection/Transfer COS（矩阵）管"谁能连谁/谁转给谁"，Public COS 管"能打外线哪些区域"。
12. 去话链路是固定流水线：ARS 前缀→逻辑鉴别符→Entity 鉴别符选择器→真实鉴别符规则（号码→Area+ARS 表）→ARS 路由（去位/加位+编号命令表）→中继组→NPD（号码格式）→DID 翻译器（CLI）→外部 SIP 网关（运营商地址/凭证）。闭锁=同一流水线上 Area×Public COS×Entity 状态的交点检查。
13. SIP 中继规格与弹性：每 TG 最多 32 接入（成对），标准型每对 62 通道（满配 992 并发）、Mini 型每对 4 通道（64）；第二网关可走 ARS 第二路由做备份，或 Pool Number 做负载均衡+原生互备（配 Supervision timer 才能快速切换）。
14. 语音邮件 4645 一节点一实例、软件化四拓扑（嵌 CS/独立服务器/主备分离/嵌其中一台 CS），上量 7000 信箱/30 端口/500-600 小时；邮件通知分 None/Basic/Advanced 三档，SMTP 经 netadmin 声明并加入防火墙可信主机。

### 论证链
教材以"讲义概念 → How-To 实验 → 行为验证"推进：每个实验给出精确到按键的菜单路径与验证命令（如 role 看话务状态、trkstat 看中继、sipextgw -l 看网关注册、traced 看信令），用可复现的行为闭环替代理论论证；容量与规则类内容用硬表（限制表、计时器表、端口表）支撑；架构类内容用拓扑图（出门链路九步图、4645 四拓扑、实体 CDT 结构）。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 Edition 12 / R101.1 MD4：UMC 章节标 R1.1 且大量功能标注"NEXT DELIVERY"（Desk Sharing 等），功能清单会快速漂移。
- Crystal 硬件章节"书中自注不再深入讲解"却仍占篇幅；XL 机架作为新补位方案，参数细节多处写"XX.XX"占位，明显处于文档追赶硬件的状态。
- 4645 安全只给 SA0046/TC1774 指针；语音加密（SRTP/DTLS）只在概览页点名，全书无一处实操。

### 作者的立场盲点
- 实验环境安全口径和生产口径混排：明文培训密码（Administrator5689! / Superuser2580* / alcatel / letacla1 / mg4.ale / mgxl.ale / *tx8000#）遍布正文；实验甚至建议"可直接关防火墙"。照抄进生产是事故。
- 培训约定覆盖在通用规则上：空库强制用 FR 国家码、号码统一 10 位、ISDN 用"France"信令变体——每处都补了一句"真实现场要用对的"，但实验步骤本身会形成肌肉记忆。
- 实验输出里出现的告警（如 "Warning rack 1-254: unknown rack type"、"BAD PCMS CODE"、"484 Address Incomplete"）原样贴出但大多不解释，初学者无法分辨哪些是预期现象。
- Rainbow/Cloud Connect/UMC 都只有概览或单章，深度全部指向其它课程（Advanced、CPU Loading、ENTPXTE402）与 MyPortal 文档。

### 未被证明的假设
- 假设读者始终有 RLAB/虚拟环境可用（生产中现场可能只有物理机+串口）。
- 假设 ITSP1 SIP 模拟器行为等同于生产运营商（紧急号码显示管理、callback 规则、登记账号全部是模拟器特设口径，书中自己都在 Warning 里提醒）。
- 假设 FlexLM/Cloud Connect/SPS 合同/MyPortal 权限等商务侧前提已就绪，书内不校验。

### 最强反对意见
"这本 Starter 教的是'一台 OXE 能跑起来'的最小闭环，不是交付"——SBC/网络 QoS/中继深调、ACD/CCD、Rainbow 与 Cloud Connect 的实操、UMC 批量运维全部外置；每个能力的 Boundary 必须标注"Starter/实验环境口径"，并显式指向 TC2005（SIP 运营商）、SA0046/TC1774（语音邮件安全）、TC3009（ALE-120）、ENTPXTE402（Cloud Connect）等外部文档作为生产化依据。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] OXE 登录与账户密码治理（四账户、14 位策略、失败锁定、老化）
- [x] 系统启停与 autostart 管理（含一键取消自启窗口）
- [x] Call Server IP 寻址（netadmin 完整安装/菜单模式、Role 地址）
- [x] OXE 内部防火墙与可信主机（单加/网段/域名/CSV 批量）
- [x] NTP/chrony 时间同步部署与巡检
- [x] 空数据库创建与恢复（国家码、Direct Link、重启顺序）
- [x] OPS 许可恢复/备份与 FlexLM 对接（spadmin 巡检、PANIC 判读）
- [x] GD4 硬件媒体网关上架（Shelf/板卡/mgconfig/MAC/压缩器）
- [x] OMS 虚拟媒体网关上架（omsconfig/资源声明）
- [x] XL 机架上架（GDXL/FXS32/机位规划/DHCP 类）
- [x] IP 话机静态/动态开通与维护（MAC 检索/换机/日志收集）
- [x] IPDSP 部署与网络端口基线
- [x] 用户 Profile 批量建户法
- [x] CS 内部 DHCP 服务器配置与巡检
- [x] 编号计划（前缀/后缀）规划与维护
- [x] Phone Features COS 管理（权利/功能/离机路由/默认溢出）
- [x] Connection & Transfer COS 矩阵管理
- [x] 静态语音指南与音乐保持部署（含 580 试听）
- [x] 话务台组与 4059EE 部署（CDT/BLF/系统参数）
- [x] Entity 与 CDT 管理（状态小时表/经理组/等待指南）
- [x] OmniMessage 4645 部署与邮箱管理
- [x] 4645 邮件通知（SMTP 声明/CoS 三档/Thunderbird 验证）
- [x] 公共 SIP 中继开通全链路（TG/网关/ARS/NPD/DID/回拨/国际/紧急）
- [x] SIP 网关备份与负载均衡（第二路由/SIP Pool）
- [x] 外呼闭锁配置（Area/Public COS/Entity 三要素）
- [x] 紧急呼叫通知（区域/Location ID/紧急组）
- [x] 呼叫分配计时器调优（76/141/144/102/trunk COS/Entity 溢出）
- [x] 数据库备份与恢复（含 Cloud/Rainbow 剥离选项）
- [x] 维护排障工具箱（oxetrace/ippstat/incvisu/incinfo/syslog/securitystatustool/infocollect/tcpdump）
- [x] T0/T2 中继组开通与巡检

### 不适合 skill 化的内容
- RLAB/ITSP1 教学基础设施细节（p1-26：POD 账号、模拟器账号密码——仅作实验口径 Boundary）
- 培训评估/证书流程（p815-821）
- 话机硬件规格目录页（p273-287：ALE-300/400/500、DECT/WLAN 参数表——归产品目录，仅保留选型要点）
- Crystal 硬件细节（书中自注不深入，p69-72 仅留退场背景）
- 培训教室专用值（ISDN France 信令、10 位号码、#010/#012 教学前缀——标注实验口径后并入相应 skill 的 conditions）

### 预估 skill 数量
**约 12-14 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；建议入口软预算 10 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 通过 V24/SSH/console 登录 OXE 并管理四账户与密码策略 | p82-107 | 可控的系统访问+密码基线 | 一切操作的准入；密码策略是安全底线 | 生产密码需客户自定 |
| task-02 | 启动/停止/重启系统并管理 autostart | p108-125 | 正确的系统运行态 | 维护与恢复的前置动作 | 无 |
| task-03 | 配置 Call Server IP（物理地址+Role 地址） | p126-133, p145-149 | 双地址可用的 CS | 全部 IP 互通的地基 | 网络规划在书外 |
| task-04 | 配置 OXE 内部防火墙与可信主机 | p134-144, p156-163 | 白名单生效的 iptables | N3 起默认全关，不做则无法互通 | 客户网络清单在书外 |
| task-05 | 部署 NTP/chrony 时间同步 | p164-183 | 时钟受控的系统 | 计费/留言/排障依赖时间 | 上级 NTP 源在书外 |
| task-06 | 创建空数据库 | p184-193 | 按国家码初始化的 MAO | 全部配置的起点 | 无（注意抹许可副作用） |
| task-07 | 恢复/备份 OPS 许可并对接 FlexLM | p194-223 | 许可生效的系统 | 没许可一切功能为 0 | Actis 订购流程在书外 |
| task-08 | 上架 GD4 硬件媒体网关 | p245-258 | IN SERVICE 的机架板卡 | 话机/中继的物理承载 | 硬件安装工艺在书外 |
| task-09 | 上架 OMS 虚拟媒体网关 | p259-268 | IN SERVICE 的 OMS | 虚拟化交付的媒体面 | hypervisor 侧在书外 |
| task-10 | 上架 XL 机架（GDXL/FXS32） | p73-78, p757-772 | 384 FXS 可用 | 高密度模拟口场景 | -48V 电源工艺在书外 |
| task-11 | 开通 IP 话机（静态/动态）并做换机/日志维护 | p320-329, p355-365 | 在服的 IP 话机 | 最高频交付动作 | 无 |
| task-12 | 部署 IPDSP 软话机 | p287-289, p308-314 | 在服的 IPDSP | 远程/软终端场景 | PC 音频设备前提 |
| task-13 | 用 User Profile 批量建户 | p315-319 | 模板化用户 | 规模开通提效 | 无 |
| task-14 | 创建数字/模拟用户并巡检 | p330-341 | TDM 用户可用 | 传统终端场景 | TDM 功耗约束（p299-306） |
| task-15 | 配置 CS 内部 DHCP 服务器 | p342-365 | 话机动态获址 | 无客户 DHCP 时的标准方案 | 客户现有 DHCP 时改走客户侧 |
| task-16 | 规划并维护编号计划（前缀/后缀） | p366-388 | 合理的拨号计划 | 全系统路由地基 | 客户需求分析在书外 |
| task-17 | 管理 Phone Features COS 与 Connection/Transfer COS | p389-424 | 权限受控的用户群 | 功能合规与防滥用 | 客户权限矩阵在书外 |
| task-18 | 部署静态语音指南与音乐保持 | p425-448 | 多语言指南+MOH 生效 | 用户感知最直接 | 录音内容制作在书外 |
| task-19 | 部署话务台组与 4059EE（CDT/BLF） | p449-495 | 可用的话务台 | 前台场景刚需 | 无 |
| task-20 | 管理 Entity 与 CDT（状态/经理组） | p496-525 | 按部门分流生效 | 多部门个性化路由 | 无 |
| task-21 | 部署 4645 语音邮件与邮件通知 | p526-571 | 可留言可通知 | 语音邮件基础业务 | SMTP 服务器由客户提供 |
| task-22 | 开通公共 SIP 中继（全链路） | p572-656 | 可打外线的 SIP 中继 | 外线互通核心任务 | 运营商参数按 TC2005/运营商文档 |
| task-23 | 配置外呼闭锁（Area×Public COS×Entity） | p657-681 | 受控的外呼权限 | 防盗打与合规 | 客户策略在书外 |
| task-24 | 配置紧急呼叫通知（区域/Location ID/紧急组） | p682-699 | 紧急事件可感知 | 合规与安全刚需 | 运营商 Location ID 格式在书外 |
| task-25 | 调优呼叫分配计时器 | p700-719 | 溢出时序符合预期 | 话务体验调参 | 无 |
| task-26 | 数据库备份与恢复 | p720-736 | 可恢复的配置资产 | 灾备底线 | 异地存储策略在书外 |
| task-27 | 运用维护排障工具箱 | p737-756 | 抓包/日志/事件闭环 | 一线排障能力 | 深度分析在 Advanced 课程 |
| task-28 | 开通 T0/T2 中继组 | p773-796 | ISDN 中继可用 | 传统运营商场景 | 运营商信令变体需确认 |
| task-29 | 用 UMC 做云侧简化管理 | p797-814 | 云端可管理 | 新交付模式 | Fleet Dashboard/MyPortal 权限在书外 |

### 优先级排序 (按"最能独立交付一台 OXE"的角度)
1. task-01/02 登录与启停（一切前提）
2. task-03/04 IP 与防火墙（网络不通全停）
3. task-06/07 空库与许可（功能解锁）
4. task-08/09/10 三类媒体网关上架（承载面）
5. task-11/12/14 用户终端开通（业务面）
6. task-22 公共 SIP 中继（外线闭环，全书中权重最高的实验链）
7. task-16/17/23 编号计划与两级闭锁（路由与合规）
8. task-19/20/25 话务台/Entity/计时器（呼叫处理）
9. task-18/21 语音指南与 4645（体验与留言）
10. task-05/15/24/26/27/28/29/13（支撑与专项）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 12 个一级部分（环境 1 + 系统观 2 + 准入链 5 + 配置域 2 + 业务域 2，运维收尾并入第 12 条说明；培训收尾为附注未计入）
- [x] 术语按实际内容列出（17 个）
- [x] 已检查作者局限/假设（实验密码、FR 口径、未解释告警、深度外置课程）
- [x] 原书关键任务 29 项，全部有来源页码、交付物与重要性依据
- [x] 本任务为流水线自动化阶段任务，按任务书全量提取授权连续执行（2026-09-23）

**用户确认时间**: 2026-09-23（流水线授权）
