# OmniTouch Contact Center Standard · Advanced (OTCCXTE101EN Ed07) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OmniTouch Contact Center Standard Edition - R10.15, Advanced - Edition 07 (Participant's Guide)
- **作者**: ALE Training Services
- **出版/发布时间**: Edition 07（OTCC Standard R10.15 / OXE 11.1 时代；实验截图日期为 2024 年 8-9 月）
- **内容类型**: 课程（官方售后培训讲义幻灯片 + 分步实验 How-To，讲义约占 55%、实验约占 45%）
- **版本来源**: ALE 培训教材 OTCCXTE101EN（597 页）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商高级培训教材：概念讲义幻灯片 + 分步实验 How-To；每个能力域都是"讲义模块 → How-To 实验"成对出现）

### 一句话主旨
在预配置好的 OXE 双节点实验 POD 上，把 OmniTouch Contact Center Standard 的高级能力逐一落地：ACR 高级路由（ASM 脚本、ISM 技能匹配、最后应答坐席）、网络化分布式互助（Remote PG）、Soft Panel Manager 实时墙板、话务票据分析器、特殊功能开关、Excel 报表定制与 CCS Server 集中接入。

### 骨架 (主要论点及其关系)

1. **培训实验环境**（RLAB 全虚拟化 POD：OXE 本地/远程双节点 + Windows 客户端/服务器 + FlexLM；公共 Pod 放 NAS 与 SIP 运营商模拟器；Console mode 承载软话机音频）
2. **CCD 预配置概览**（CCD 矩阵、Pilot1/Pilot2 两路预配置：路由设置、语音引导、呼叫分配；ACD 授权话机/坐席/班长；本地混合 ABC-F 链路）
3. **CCS 软件与 POD 定稿**（两个 How-To：CCsupervision 安装/声明 OXE/Navigator 验证；机架、SIP 用户、MicroSIP/IPDSP 软话机、坐席登录、外部 SIP 网关注册、DID 翻译、呼入测试、RDP 嵌套）
4. **ACR 体系**（全书核心：ACR 引言与 9 类规则、ASM 架构、等待室与动态组、呼叫特征化、ACR 容量上限；CCS 集成（权限/技能/实时视图）；ACR 对象管理讲义 + How-To）
5. **ISM 规则与 ASM 脚本**（ISM 算法与成本公式、坐席子列表与重选、PLTR/LIT 排序参数；ASM Script Editor（在线/离线、积木块、编译激活）；调试器三窗格；ISM 手算、脚本、重选三个 How-To）
6. **Last Called Agent 规则**（ASM 记忆模型、7 种 LAST_CALLED_STATE、关键字变量；LCA_1/2/3 三个渐进脚本 How-To）
7. **网络化 Contact Center**（盲互助 vs 智能互助、拒收回退表；Remote PG 分布式互助三对象（Remote PG/虚拟队列/专用 Pilot）；Remote PG How-To 含链路维护命令与故障注入）
8. **Soft Panel Manager**（概览与架构、安装讲义+How-To（服务器/RTI Connector/FlexLM/基础设置）、面板配置讲义+How-To（背景/视图/挂件/消息/告警））
9. **配套工具与增值功能**（CCTA 票据分析器；特殊功能（优先转接、DID 忙音、两种代接、监督监听、永恒整理、中继预留）；Excel 计数器定制；CCS Server 内/外部部署——各自讲义 + How-To）
10. **培训收尾**（在线评估问卷与证书下载流程）

**论点之间的关系**: 1-3 是地基（环境+工具就绪），4-6 是全书主线（ACR 高级路由从对象到脚本到算法层层深入：先建对象 → 再上 ISM 脚本 → 再上 LCA 记忆路由），7 把单点 CC 扩展到网络（依赖 ABC-F 链路），8-9 是并列的四个增值能力域（可视化墙板、票据分析、特殊功能、报表定制、集中接入），10 收尾。讲义与 How-To 严格成对，实验依赖链：CCS 安装 → POD 定稿 → ACR 管理 → ISM 脚本 → 重选/调试器 → LCA → Remote PG。

### 作者要解决的核心问题
让已掌握 OTCC Standard 基础的售后/渠道工程师，能独立实施呼叫中心的高级路由与运营增值能力：用技能匹配（ISM）和记忆路由（LCA）把"对的音乐交给对的坐席"、用网络互助把话务溢出到兄弟站点、用 Soft Panel Manager 把实时统计上墙、用 CCTA/Excel 把话务票据变成可分析的报表，并具备全链路维护命令的排障能力。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| ACR | Advanced Call Routing，CCD 的选项：按技能、上次应答坐席等条件路由呼叫；需要 ASM 软件和特殊矩阵管理（必须建等待室） | 不是"自动呼叫重试"；它是一套脚本化路由子系统，挂在 CCD 之上 |
| ASM | Agent Selection Module，处理 ACR 呼叫的软件；可内置于 Call Server 或装在外部 Windows 服务器 | ASM 服务器输出的是"坐席列表"（动态组），不直接接续呼叫 |
| ISM | Individual Skill Mapping，ACR 最常用的子程序：按呼叫档案与坐席技能匹配出最佳坐席列表 | 匹配不是布尔筛选，而是"强制属性全满足 → 成本函数排序 → 子列表逐级降级" |
| LCA | Last Called Agent Rule，从 ASM 记忆里取"上次应答该主叫的坐席" | 记忆按主叫号码/呼叫标签存，未接通呼叫也记录状态；alb 进程重启清空，MAIN_AFE 重启不清 |
| CCS | CCsupervision，CC 的管理与监督软件：配置（Configurations）、实时（Real time）、统计（Statistics）、脚本编辑器内嵌 | 既是配置工具也是实时监控台；坐席技能可直接在 CCS 里配，不必回 OXE WBM |
| Pilot / 统计 Pilot | 路由 Pilot 是矩阵入口；统计 Pilot 是 ACR 呼叫档案的挂载点（带 call tag、call priority、call profile） | 呼 ACR 业务时拨的是统计 Pilot 号码，呼叫档案由它带入 ASM |
| Waiting Room | ACR 专用等待室：非 FIFO，按呼叫档案挂动态组，最多 6 个泊位语音引导 + 迎宾 | 与普通等待队列互斥（同一规则不能同时打开）；无资源选择优先级 |
| Call profile / Skill | 呼叫档案 = 最多 7 个属性（域+技能+等级+强制/可选）；技能按域组织（0/1 号域默认语言与媒体） | 技能等级 1-9；域权重 1-20；坐席无可选技能时按等级 9 计入成本 |
| Processing Group | 处理组：Agent / IVR / Other（语音引导、转发等）/ Remote / Rerouting 多种类型 | 不只是"坐席组"；Rerouting PG 无呼叫选择优先级，Remote PG 无呼叫选择优先级但有门限 |
| Mutual aid | 互助：盲互助（无 ABC-F，远端当新呼叫处理）与智能互助（按远端状态路由） | 智能互助要求 ABC 网络；拒收时按五类回退表本地处理 |
| Remote PG / 虚拟队列 / 专用 Pilot | 分布式互助三对象：远端处理组（有门限+资源优先级）、队头镜像的虚拟队列、只服务一个虚拟队列的专用 Pilot | 虚拟队列只含队头呼叫的特征，远端班长看到的等待时间是主叫节点+本节点的总时长 |
| Soft Panel Manager | OTCC 实时统计上墙方案：Web 管理端 + LED 墙板/液晶/电视显示 + 邮件告警 + 业务数据接口 | 不是 CCS 的一部分，是独立服务器 + RTI Connector + FlexLM 许可的三件套 |
| RTI Connector | 从 CCS 取实时统计并推送给 SPM 服务器的 Windows 服务 | 同机共存时 CCS 必须专用于 RTI Connector，禁止手工再启动 CCS |
| CCTA | Contact Center Ticket Analyser：解析 CCd 通信/事件票据（.Z 文件），过滤后导出 ASCII | 离线分析工具，分 Importation（自动导入）与 Ticket Tracer（可视化）两个程序 |
| CCS Server | CCsupervision 集中接入服务器：内部（OXE 上 serv_ccs 进程，15 客户端）或外部（Windows 服务，120 客户端） | 一个 AFE 只能接一个 CCS Server；连接数 >9 时必须用 CCS Server |
| ABC-F | OXE 节点间网络链路协议（Direct IP Link），承载智能互助的 ACD 信息交换 | 书中未给全称；透明支持该协议的中转节点可以是 OXE 或 A4300M/L |

### 核心命题 (用自己的话)

1. ACR 的一切建立在"等待室"上：呼叫先被特征化（CLID/NDI/被叫号码/呼叫标签/呼叫档案），路由到 ACR Pilot，ASM 按脚本算出坐席列表（动态组），呼叫带着这份列表进等待室等坐席。
2. ISM 匹配是三级漏斗：坐席必须具备全部强制属性；不满足则子列表逐级降级（N→N-1→…）；同级内按成本 Cman=Σ(|坐席等级-呼叫等级|×域权重) 最小者胜，同分比可选属性成本 Copt，再同分按 PLTR 或 LIT 排序。
3. 坐席列表长度由"Number of ACR agent buffers"控制（20-400），脚本重选最多执行 21 次，RESELECTION_TIMEOUT 决定降级子列表的节奏。
4. 排序行为可用 parameters.cfg 的 asm_ag_free_duration 切换：0=PLTR（默认），1=LIT，2=网络 LIT；用 LIT 必须在脚本里加 IDLE 积木块；注意坐席统计默认 5 分钟才刷新，低话务量时"最久空闲"形同轮询。
5. LCA 把"客户记住坐席"产品化：ASM 为每个主叫记录最后应答坐席与 7 种上次呼叫状态，脚本用 IF+关键字（LAST_CALLED_AGENT/LAST_CALLED_PILOT/LAST_CALL_STATE/elapsed time）实现"同天同服务找原坐席、放弃重呼升优先级"。
6. 等待室与等待队列互斥且行为不同：WR 不做 FIFO、无资源选择优先级；饱和判定是 EWT>最大等待时间；同优先级选 EWT 最小的方向；分布门限可让呼叫在队列里等满 N 秒才允许流向远端。
7. 网络互助的关键是"知道对方状态"：智能互助经 ABC-F 交换 Pilot 状态/语音引导已听/真实等待时间；远端拒收时按远端 Pilot 地址类型（重路由组/GFWD/闭锁/排队溢出/振铃溢出）回退成本地处理。
8. Remote PG 把远端坐席变成"本地队列的一个方向"：有资源选择优先级和最小等待门限，没有呼叫选择优先级；本地优先级数字 0 最高 9 最低，同优先级按 LIT。
9. Soft Panel Manager 是独立数据链路：RTI Connector 连 CCS 拉统计（订阅 ≤500 项、并发 ≤150、面板 ≤200），经 ActiveMQ 推显示端；统计被选用后最多 1 分钟才开始订阅更新；日统计每 15 分钟取一次且不可更快。
10. 特殊功能全部是"对象上的参数开关 + 行为验证"：优先转接（双队列）、DID 忙音、两种代接前缀、监督监听（Show Supervisor Listening）、永恒整理（Auto return to wrap up）、中继预留（Max % of trunks out CCD + Pilot Trunk limitation）。
11. 运维有完整命令箱：adm_acd（含 -salb/-servccs 分支）、agacd、compvisu sys、hybvisu、pildstctx、pgctx、acdsup、spadmin，配合 CCS Navigator 与 Debugger 完成从链路到脚本的全栈排障。
12. CCS 接入架构二选一：直连 AFE（≤15 连接物理上限）、内部 CCS Server（15 客户端）或外部 CCS Server（120 客户端，Windows Server 2019/2022，CCd R3.1/CCs 4.3.46.1 起，>9 连接时强制）。

### 论证链
全书以"讲义给对象模型与数值边界 → How-To 给精确菜单路径 → 行为测试给验收"推进：每个 How-To 都以呼叫测试或状态观察收尾（如"Agent 31500 is ringing"、"Dedicated pilot is in blocked status"、Debugger 里 SEQUENCE=1→TRUE 的分支轨迹）；算法部分（ISM 成本）用 5 个坐席的完整算例逐步代入公式验证；网络部分用"禁用链路/置坐席不可用"的故障注入验证回退行为。这是行为闭环式的论证，不是理论推导式。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 R10.15/Ed07 与 OXE 11.1 时代的界面；CCS 要求 V10.2.92.0+，浏览器基线是 Firefox/Chrome/Edge 120，SPM 仅支持 Windows 10 64 位与 Server 2016/2019/2022——版本更迭后截图与路径会漂移。
- 明文实验口令贯穿全书（mtcl/Superuser2580*、administrator/alcatel、admin/admin、FlexLM root/letacla1、SIP 密码 123456），生产安全基线完全缺位。
- ASM 记忆、alb 参数（.inialb：StatPeriod 5、NbMaxAgent 200）等关键行为只给实验观察值，没有版本间的演进说明。

### 作者的立场盲点
- 全书默认"高级"读者已具备 CCD/矩阵基础（Pilot1/2 预配置直接当起点），基础薄弱的工程师会在第一章就掉队。
- 技能体系设计方法论（怎么划域、怎么定权重与等级）完全不讲——只教"配"，不教"设计"，而后者才是 ISM 效果的决定因素。
- 容量与性能只给 ACR 对象上限和 SPM 订阅上限，没有话务模型（Erlang、坐席数估算）生产化的桥。
- 安全与合规（监听的法律边界、录音告知、密码策略）零覆盖；监督监听只讲操作。

### 未被证明的假设
- 假设 RLAB POD、NAS 软件源与 FlexLM 许可随时可用（生产现场这三样常常都没有）。
- 假设 OXE 本地/远程节点、ABC-F 直连链路已按实验拓扑就绪；hybvisu 的"High Bandwidth 全编解码 / Low 带宽 G729"结论直接照搬到生产链路可能不成立。
- 假设 SIP 模拟器行为与真实运营商一致（号码变换、拥塞行为做了大幅简化）。
- 假设学员 PC 能装 CCS/SPM/CCTA 全家桶（对桌面管控严格的企业客户不现实）。

### 最强反对意见
"这本教材教的是高级功能的操作闭环，不是呼叫中心方案设计"——技能域怎么划分、权重怎么定、互助溢出策略怎么按话务建模、报表 KPI 怎么定义，全书一概不涉及；所有数值（21 次重选、5 分钟统计刷新、15 秒门限）都是实验口径而非调优建议。因此每个能力的 Boundary 必须标注"实验口径"，生产化要回到对应产品的 Feature List 与安装指南（书中多处只给了指针）。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] RLAB 类实验 POD 搭建与接入（VM 清单、账号、Console/RDP 双通道）
- [x] CCS 安装、OXE 声明与 Navigator 连通验证
- [x] POD 定稿：SIP 用户/软话机/坐席登录/外部 SIP 网关注册/DID 翻译
- [x] ACR 基础对象部署（处理组、等待室、ACR Pilot、统计 Pilot、路由/分配规则、附加 PG）
- [x] 技能体系管理（域/技能/呼叫档案/坐席技能/技能矩阵/坐席侧开关）
- [x] ISM 坐席清单手算与算法运用（强制/可选成本、子列表降级）
- [x] ASM Script Editor 安装与 ACR 脚本编写激活（在线/离线、积木块）
- [x] LIT 排序切换（parameters.cfg + MAIN_AFE 重启 + IDLE 规则）
- [x] 脚本调试器排障（过滤器、Make call、轨迹保存）
- [x] 重选机制实施（RESELECTION_TIMEOUT、子列表验证）
- [x] LCA 脚本族编写（三段式脚本、ASM 记忆清理与维护）
- [x] ABC-F 链路检查与网络互助部署（盲/智能、Remote PG 三对象、故障注入验证）
- [x] Soft Panel Manager 部署（SPM 服务器/RTI Connector/FlexLM/基础设置/日统计）
- [x] Soft Panel 可视化配置（背景/视图/面板/挂件/消息/告警视图）
- [x] CCTA 票据分析（导入 .Z、过滤、ASCII 报表）
- [x] 特殊功能配置与验证（优先转接/忙音/代接/监听/永恒整理/中继预留）
- [x] Excel 报表模板定制（FormPil 工作表/链接/图表）
- [x] CCS Server 部署与接入切换（内/外部、维护命令、日志）
- [x] ACD 维护命令箱运用（adm_acd/agacd/compvisu/hybvisu/pildstctx/pgctx/acdsup/spadmin）

### 不适合 skill 化的内容
- RLAB 平台细节与培训评估流程（p3-14、p591-597，教学专用基础设施与行政流程）
- SIP 模拟器的教学专用号码表（p15-18，仅作 Boundary 背景与测试口径）
- 逐屏安装向导的每一步截图复述（CCS/CCTA 等安装步骤可压缩为关键选项清单）

### 预估 skill 数量
**约 10-12 个能力单元**（阶段 1.5 决定保留；入口软预算 8 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 搭建并核验培训 POD（VM 清单/账号/IP/Console 与 RDP 接入） | p3-14, p48-62, p60-62 | 可用的实验环境 | 一切实验的前提 | RLAB 专属，生产仅参考结构 |
| task-02 | 安装 CCS 并声明 OXE、验证 Navigator 连接 | p39-47 | 可用的 CCsupervision | 全书管理动作的载体 | 无 |
| task-03 | 完成 POD 定稿（用户/软话机/坐席登录/SIP 网关注册/DID 翻译/呼入测试） | p48-62 | 外呼/呼入全通的基线矩阵 | 后续所有实验的基线 | 依赖 SIP 模拟器 |
| task-04 | 部署 ACR 基础对象（附加 PG/等待室/ACR Pilot/统计 Pilot/路由与分配规则） | p130-147 | 结构完整的 ACR 矩阵 | ACR 的骨架 | 无 |
| task-05 | 管理技能体系（域/技能/呼叫档案/坐席技能/技能矩阵） | p148-158, p94-115 | 技能匹配可用的数据基础 | ISM 的原料 | 技能域设计方法论在书外 |
| task-06 | 手算 ISM 坐席清单（强制/可选成本公式） | p182-186 | 可核算的排序结论 | 理解 ISM 行为的关键练习 | 无 |
| task-07 | 安装 ASM Script Editor 与 JRE | p204-208 | 可用的脚本工具链 | 脚本能力的前提 | 注意专用 msi 限制 |
| task-08 | 编写并激活 ISM 脚本，完成三路呼叫测试 | p209-214 | 生效的 ISM 路由 | ACR 核心交付 | 无 |
| task-09 | 切换 LIT 排序（parameters.cfg/重启 MAIN_AFE/IDLE 规则脚本） | p215-220, p179-180 | 按最久空闲分配的坐席列表 | 客户最常见的公平性诉求 | 注意 5 分钟统计刷新边界 |
| task-10 | 用调试器跟踪脚本执行并验证重选机制 | p221-245 | 可复现的路由轨迹与多子列表 | 排障核心技能 | 无 |
| task-11 | 编写 LCA_1/2/3 脚本族并做记忆清理验证 | p246-292 | 回头客路由能力 | 客户体验类刚需 | 无 |
| task-12 | 检查 ABC-F 链路并部署 Remote PG 分布式互助 | p293-370 | 跨站点溢出接续 | 多站点客户的核心架构 | 网络话务建模在书外 |
| task-13 | 部署 Soft Panel Manager（服务器/RTI Connector/FlexLM）并完成基础设置 | p371-417 | 实时统计数据链路 | 可视化的前提 | 许可文件需另备 |
| task-14 | 配置 Soft Panel 显示（视图/挂件/消息/告警） | p418-479 | 上墙的实时看板 | 运营可视刚需 | 仅 Firefox 定制视图 |
| task-15 | 部署并使用 CCTA 分析话务票据 | p480-497 | 可导出的明细报表 | 故障复盘/质量分析 | 无 |
| task-16 | 配置特殊功能（优先转接/忙音/代接/监听/永恒整理/中继预留） | p498-530 | 逐项可验证的功能开关 | 交付验收高频项 | 监听合规在书外 |
| task-17 | 定制 Excel 报表模板并生成报表 | p531-554 | 客户化日报 | 报表交付高频项 | KPI 定义在书外 |
| task-18 | 部署 CCS Server 并切换客户端接入 | p555-590 | 集中接入的监督体系 | 多监督员客户必需 | 无 |
| task-19 | 运用 ACD 维护命令箱排障（adm_acd/agacd/hybvisu 等） | p127-128, p257-258, p336, p341-342, p405, p563-564, p576, p583, p590 | 全栈排障能力 | 售后日常 | 无 |
| task-20 | 理解 ACR 容量上限与 SPM 限制并做规划核对 | p77, p394 | 容量合规结论 | 避免上线即触顶 | 话务建模在书外 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-02/03 CCS 安装与 POD 定稿（一切实验与现场工作的地基）
2. task-04/05 ACR 对象与技能体系（高级路由的骨架与原料）
3. task-08 ISM 脚本（全书最核心交付）
4. task-10 调试器与重选（排障差异化能力）
5. task-11 LCA 脚本族（客户体验类刚需）
6. task-12 Remote PG 网络互助（多站点架构决策）
7. task-13/14 SPM 部署与上墙（运营可视化）
8. task-16 特殊功能 + task-09 LIT（高频参数开关）
9. task-15/17 CCTA 与 Excel 报表（数据交付）
10. task-18/19/06/07/20/01（支撑类与理解类任务）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 10 个一级部分（环境 1 + 基线 2 + ACR 主线 3 + 网络 1 + 增值域 3 + 收尾 1，成对"讲义+How-To"结构已在骨架中标注）
- [x] 术语按实际内容列出（16 个）
- [x] 已检查作者局限/假设（实验口径、明文口令、技能设计方法论缺位、容量/安全缺位）
- [x] 原书关键任务 20 项，全部有来源页码、交付物与重要性依据
- [x] 用户已授权全流程连续执行（流水线任务指令，2026-09-23）

**用户确认时间**: 2026-09-23（流水线授权执行）
