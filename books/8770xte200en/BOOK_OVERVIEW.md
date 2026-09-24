# OmniVista 8770 安装与网络管理 (8770XTE200EN Ed47) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OmniVista 8770 — Setup & Network Management (Participant's Guide)
- **作者**: ALE Training Services
- **出版/发布时间**: Edition 47（OmniVista 8770 R5.2 时代，正文示例出现版本号 8770.5.2.21.01）
- **内容类型**: 课程（官方售后培训讲义幻灯片 + 分步实验 How-To，讲义约占 40%、实验约占 60%）
- **版本来源**: ALE 培训教材 8770XTE200EN（705 页）；全文提取件 `F:\AIwork\ZCode\books\8770xte200en\source_fulltext.txt`
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To，一条"讲义章 + How-To 章"配对主线贯穿全书）

### 一句话主旨
把 OmniVista 8770 网络管理平台从裸机装到管起来：Windows 服务器上装 8770（数据库/LDAP/应用套件一体落地），注册 OXE/OXO Connect 节点并同步，再用 Users/Alarms/Topology/Security/Audit/Reports/Scheduler/Maintenance/License 九大应用完成用户开通、告警集中、可视化、权限、审计、报表、任务编排、备份恢复与许可控制的全套日常运维。

### 骨架 (主要论点及其关系)

1. **解决方案概览**（8770 定位为集中网络管理：架构协议图、虚拟化、跨版本兼容矩阵、四大套件 + WBM 客户端全景）
2. **实验平台**（RLAB 远程实验室：POD 结构、5 台虚机实例表、Console/RDP 两种接入）
3. **服务器与客户端安装**（OS/硬件要求、安装步骤、补丁、IE ESC 与 Defender 前置、首次连接；Windows 2022 与 2019 两套并列 How-To）
4. **节点注册**（Configuration 应用声明网络/子网/OXE、节点号公式、同步语义、OXE SSH 加固、OXO Connect 节点声明与 OMC 在线/离线）
5. **用户开通体系**（Users 应用 Profile/Meta Profile/Key Profile、空闲号码段、批量开通文件语义、WBM 轻客户端开通、Manage My Phone 终端自助）
6. **告警体系**（Alarms 架构与严重级、OXE incident 接入、签名/字典/邮件/脚本定制、SNMP Proxy 转发外部网管）
7. **可视化与审计**（Topology 标准视图/自定义视图/告警重定向；Audit 启用、OXE mao 日志、8770 log、导出与报告）
8. **报表与任务编排**（Reports 预定义报告、导出/邮件/计划；Scheduler Job/Task、简单与同步 job、自动维护与数据清除）
9. **维护体系**（8770 数据库备份恢复/rehosting、维护工具（诊断/DirManag/HeidiSQL）、NMC 服务与日志、OXE 备份恢复、许可体系（ACTIS/锁/更新））
10. **支撑性工程任务**（映射网络驱动器：远程共享 + ADM8770 账号 + ExecdEx/SaveRestore 服务账号，收尾培训评估附注）

**论点之间的关系**: 层层递进为主——1-2 是地基（是什么 + 在哪练），3 是把平台立起来，4 是把被管设备接进来，5-6 是最高频的两类日常运维（开通与告警），7-8 是增值域（可视化/审计/报表/编排），9 是兜底能力（备份/排障/许可），10 是生产化补丁（备份落网络盘）。每章"讲义 → How-To"配对，How-To 内"步骤 → verification"闭环。

### 作者要解决的核心问题
让售后/渠道工程师独立完成 OmniVista 8770 的完整交付与运维：从 Windows 服务器安装、OXE/OXO 节点接入，到用户批量开通、告警集中与外送、权限划分、审计报表、计划任务、数据库与 OXE 备份恢复、许可扩容的全流程动手能力。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| OmniVista 8770 | ALE 集中网络管理解决方案：单服务器承载应用套件（ thick client + WBM 轻客户端），管理 OXE/OXO Connect/OpenTouch | 是"套件集合体"而非单一应用；服务器必须独占（dedicated server） |
| Node（节点） | Configuration 应用中被管通信服务器的登记项：Network > Subnetwork > PCX 三级树，节点号 = 子网号×100+OXE 节点号 | 不是"物理设备"，是 8770 侧的逻辑声明；声明值必须与 OXE 侧 siteid 一致 |
| Synchronization | 从 PCX 检索技术数据的过程：Complete/Partial（按变更范围）× Separate/Global（是否连带 OpenTouch） | Partial 只同步 Users/Directory/Data terminals/Speed dial/Remote users 五类，其他条目总是全取 |
| Profile | OXE 用户参数预设集：Set Function=Profile 的特殊用户；"Use profile with auto. recognition" 启用后可在建用户时引用 | Profile 本身是一个"用户对象"，不是独立配置表；名称必须大写 |
| Meta profile | 8770 侧再封装：OXE profile + 空闲号码段 + 设备类型，建用户时自动填充 OXE 属性并自动取号 | 依赖 OXE 侧 Free Numbers Ranges List（建完必须同步）；与 OXE profile 是两层 |
| Key profile | 可编程键预设：set profile + Progr. Keys 定义 + Profile Features 关联键功能；取回 8770 需同步 | 键 profile 生效前提同 profile 继承开关；检索必须同步一次 |
| Correlated/Uncorrelated alarm | PCX 能检测问题结束的告警为相关告警（自动清除）；不能检测的为非相关（手动清除） | Topology 只显示相关告警；只有非相关告警可被手动 clear |
| Job / Task | Scheduler 中 Job=同时执行的一个或多个 Task 的实体；Task=可执行操作（内部操作或外部程序） | 任务创建时临时叫 jobset，刷新后变 Job；Simple job 单任务、Synchronized task 挂入已有 job |
| RestoreContext.ini | 安装设置存档（目录/端口/计算机名/DNS 后缀/版本号），恢复时比对校验 + 升级历史 | 恢复的前提文件：nmcVersion 决定备份只能还原到同版本服务器 |
| Rehosting | 换机/改 IP/FQDN 后带配置恢复：比对 RestoreContext.ini（排除 svNMCName/svDomain）后脚本改写 LDAP 数据 | 改 IP 不用重装，改 FQDN 同机要卸载重装/异机走 rehosting |
| nmc.license | 8770 许可文件：ACTIS 生成 *.sw8770，安装时放入 8770\etc 改名 nmc.license；NMC License Server 校验 | 应用锁在 [Modules] 段：布尔键（Topology/Audit 等）与用户数键（其余）；Security 键 0-5 特殊 |
| 8770Handle | 申报节点锁：许可中登记的 OXE OPS 文件标识（如 123456AB），License Server 周期核验 | 许可控制方法 #1；方法 #2 是绑定服务器特征（MAC/IP/ProductID/UUID） |
| NMC Service Manager | 8770 内部服务总管：按依赖顺序拉起 20 个 NMC 服务、监督崩溃重启 | Windows 服务（Automatic）与 NMC 服务（Manual 被监督）两层；被监督服务不要手动 Start |
| ADM8770 | 网络驱动器场景的专用 Windows 账号：远程服务器与 8770 服务器同名同密，赋 5 项用户权利 | 报表导出（ExecdEx）与备份恢复（SaveRestore）服务以此账号运行才能写网络盘 |
| maо 日志 | OXE 侧管理操作审计日志（/usr3/mao/mao_hist 等），8770 Audit 经 rsh list_fhdet 检索 | Audit 仅支持 OXE；Secure access for system management 决定是否记录管理员名 |

### 核心命题 (用自己的话)

1. 8770 是"装在 Windows 上的套件集合"：MariaDB + Oracle DSEE LDAP + Apache/Wildfly + 应用套件一次装齐；安装参数（目录、端口、账户密码）装后大部分不可改，唯一后悔药是 RestoreContext.ini + 恢复/rehosting。
2. 节点接入的钥匙是"号对号"：8770 侧声明的节点号 = OXE 网络号×100 + 节点号，与 OXE siteid 输出一致才能同步；OXO Connect 同理（子网号×100+节点号），且备份目录按此规则落盘。
3. 同步是数据流的起点：Complete/Partial × Separate/Global 四种语义按需选用；OXE 侧改动经实时事件回传 8770（NMCFaultManager 日志可查），但 profile 范围、键 profile、空闲号码段必须主动同步才可见。
4. 用户开通三层递进：手建（Users 应用）→ Profile 复用（前提启用 profile 自动识别）→ Meta profile 自动取号；批量走导出模板文件（XXXX=必填、NULL=自动、action=ADD/MODIFY/DELETE）导入。
5. WBM 是给"非专家"的轻客户端：Unified Management 许可解锁，单界面 MACD 用户；但它与 thick client 的批量文件互不通用，且不能移除设备/OT 应用。
6. 告警集中在 Alarms 应用：6 级严重色标，相关/非相关告警决定自动/手动清除；OXE 侧 incident manager 的 network severity 与 incident filter 控制上送。
7. 告警出口有三条：人工处理（签名/动作/备注）、邮件通知（SMTP 端口语法 server:port）、脚本执行（.bat 放 scripts 目录，%1/$managedobject、%2/$notificationtime）；对外网管走 SNMP Proxy（v2c/v3，trap 162）。
8. 安全模型分三层：8770 账号（密码策略+组权限取最高+单登录）、OXE Access Profile（11 个 profile，Nothing/Read/Read-Write/All 四级）、OXE 侧 User Access Control（大写账号白名单 + Secure access 前提）。
9. 锁定账户有四条解锁路径：Security 应用改密（普通管理员）、ToolsOmniVista 选项 5、AdminNmc 专用 ToolsOmniVista 选项 4、WBM"忘记密码"邮件重置码（前置：邮件服务器+管理员邮箱已配）。
10. 审计只管 OXE：AuditServer 启用 + OXE Process audit + mtcl 凭据（rsh 转换 mao_hdet）；mao_hist 记录"谁在何时改了什么"，8770 log 记录客户端登录与应用访问；导出功能不适用于 8770 自身日志。
11. 备份恢复铁律"版本绑定"：备份专用版本（nmcVersion），跨版本不可恢复；备份期间 8770 不可用；OXE 备份经 Telnet/SSH bck 命令 + FTP/SFTP 取回，恢复必须先 swinst 停电话（会禁用 role address，需用物理 IP）。
12. 许可是"锁 + 数"：主锁（申报节点/应用/客户端数 ≤30/用户数）；Start Pack 与 Full Pack PPU 两种包型；用户数逼近上限产生告警，超限进受限模式（仅 Directory+Configuration 可用，服务器不停机防数据丢失）。

### 论证链
全书以"讲义（是什么/为什么）→ How-To（怎么做）→ verification（怎么确认）"推进：每个实验用可观察结果收口（如同步成功消息、告警上屏、报告文件落盘、邮件到达 Thunderbird、trap 被 TrapReceiver 收到），用行为闭环替代理论论证；容量与兼容性用矩阵表支撑（OS/硬件表、跨版本兼容矩阵、许可锁表）。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 R5.2（8770.5.2.21.01）与 Ed47 界面；浏览器版本（Firefox 140/Chrome 138/Edge 138）、MariaDB 10.5、Windows 2025 Server 支持均为时点值，随版本漂移。
- Windows 2019 安装章内容明显是从旧版教材沿用（cfg 文件名写 nmc5_5.1.cfg、无 WMIC 附录），与 2022 章并存造成口径不一致。
- OXO Connect 章出现未翻译法语操作提示（p659），且使用与主环境不同的 151.1.1.x 网段，章节间环境衔接弱。

### 作者的立场盲点
- 全书默认实验环境：明文密码（Superuser2580* / superuser / letacla1 / sql / pbxk1064 / Alcatel1）遍布正文，生产密码策略与密钥轮换只字未提。
- HTTP 80 明文口与 dba/sql 默认数据库口令只给"可改"提示，没有基线清单；POODLE 附录承认全网元 TLS 依赖，但未给核查方法。
- 性能容量只有安装门槛（<5000/>5000 两档），8770 自身的用户规模上限、数据库增长与清理策略分散在 Purge 章节而没有统一容量规划视角。

### 未被证明的假设
- 假设读者有 RLAB 环境（5 台虚机 + FlexLM 许可服务器 + 邮件服务器 + NAS），生产中这些前置都要自行搭建。
- 假设 OXE/OXO 已按默认密码可登录（mtcl/adfexc/swinst），N3 起强制改密的现场差异只在备份章一笔带过。
- 假设 Windows Server 补丁/防病毒策略可控——Defender 排除 C:\8770 与 IE ESC 关闭在安全审计严格的客户环境可能被拒。

### 最强反对意见
"这本手册教的是 8770 单机闭环，不是网络管理体系设计"——高可用（除许可证冗余字段一笔带过）、数据库主备、多 8770 分级、与第三方网管（除 SNMP trap 外）都缺席；目录复制、Radius 等只在功能列表出现没有实验。因此每个能力的 Boundary 必须标注"单服务器实验口径"，生产化要叠加客户的高可用与安全基线要求。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] 8770 服务器安装（Windows 2022/2019：前置配置、组件、许可、补丁、首连）
- [x] 8770 客户端安装与首次连接（URL 下载、WMIC 前置、Zulu 放行）
- [x] OXE 节点注册与同步（网络/子网/节点声明、节点号公式、四种同步、实时同步排障）
- [x] OXE SSH 安全访问加固（netadmin 可信主机、MindTerm 密钥、SFTP）
- [x] OXE 配置界面高效操作（搜索/冻结/网格/属性选择/导入导出）
- [x] OXE 用户 Profile/Key Profile 创建与引用
- [x] Meta profile 批量建户（空闲号码段 + 自动取号）
- [x] Users 应用批量开通（模板导出/文件编辑/导入核验）
- [x] WBM 轻客户端用户开通（单建 + 批量 + 与 thick client 的边界）
- [x] OXO Connect 节点声明（OMC 安装/证书/声明/共享目录/在线离线）
- [x] OXE 告警接入（incident manager/incident filter/rstcpl 验证）
- [x] 告警应用定制（签名/动作/字典/邮件通知/脚本执行）
- [x] SNMP Proxy 部署与过滤（Windows SNMP 服务/hypervisor/SNMP filter/卸载）
- [x] Topology 标准视图与虚拟 ACT 显示
- [x] Topology 自定义视图与告警重定向
- [x] 安全管理（密码策略/管理员/组/单登录/锁定解锁/OXE Access Profile/访问控制/TLS 加固）
- [x] Audit 启用、检索与报告（mao 日志/8770 log/导出）
- [x] 报告生成、导出与计划分发（文件/邮件/计划任务/大小限制）
- [x] Scheduler 任务编排（简单/同步 job、复制剪切、参数语义）
- [x] 自动维护与数据清除（五类 purge 参数、Purge job、预定义 job 恢复）
- [x] 8770 数据库备份恢复与 rehosting（IP/FQDN 修改）
- [x] 维护工具（8770 Diagnostic/DirManag/HeidiSQL）
- [x] NMC 服务与日志排障（Service Manager/TraceType/nmclog）
- [x] OXE 备份与恢复（bck/swinst 全流程）
- [x] 许可查询与更新（锁结构/spadmin/替换 nmc.license）
- [x] 网络驱动器映射（ADM8770 账号/共享/服务账号配置）

### 不适合 skill 化的内容
- RLAB 远程实验平台细节（p41-52，教学专用基础设施，仅作 Boundary 背景）
- Solution Overview 的营销性收益表（p39-40，背景知识）
- 培训评估/证书流程（p699-705）
- 8770 WBM Configuration/Performance/QueryTool/Designer 等纯截图讲义（p151-157、p435-442，无步骤参数）

### 预估 skill 数量
**约 12-14 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；安装类可合并为一条入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 在 Windows 2022 Server 上安装 8770 服务器（Windows 数据配置/组件/许可/补丁/首连） | p65-88 | 可登录的 8770 服务器 | 全书一切操作的前提；参数装后大多不可改 | 生产需客户化密码与安全基线 |
| task-02 | 在 Windows 2019 Server 上安装 8770 服务器 | p618-639 | 可登录的 8770 服务器 | 2019 现场仍大量存在；与 2022 章并列参照 | 书内流程疑似沿用旧版（cfg 文件名 5.1） |
| task-03 | 安装 8770 客户端并首次连接服务器 | p96-106 | 可用的管理客户端 | 管理员日常工作入口 | 无 |
| task-04 | 注册 OXE 节点并同步（网络/子网/节点声明、实时同步核验、排障） | p118-128 | 已同步且实时联动的 OXE | 被管对象接入的第一关口 | 无 |
| task-05 | 配置 OXE SSH 安全访问（可信主机/MindTerm/SFTP） | p129-136 | 8770 到 OXE 的加密通道 | OXE N3 起强制；安全基线 | 生产需按客户网络收敛可信主机范围 |
| task-06 | 高效使用 OXE 配置界面（搜索/冻结/网格/属性选择/导入导出） | p158-167 | 熟练的配置操作手法 | 日常配置效率基础 | 无 |
| task-07 | 创建 OXE Profile/Key Profile 并引用建户 | p182-195 | 可复用的用户模板 | 批量开通的前置 | 无 |
| task-08 | 配置空闲号码段与 Meta profile 并自动建户 | p203-210 | 取号自动化的建户流程 | 高频开通场景提效 | 无 |
| task-09 | Users 应用批量开通（导出模板/改文件/导入核验） | p219-224 | 批量用户落库 | 迁移/开局大批量场景 | 无 |
| task-10 | WBM 轻客户端用户开通（单建+批量） | p253-260 | 非专家可用的开通界面 | 交给客户自助的路径 | 与 thick client 批量文件互不通用 |
| task-11 | 声明 OXO Connect 节点（OMC 安装/证书/声明/同步/在线离线会话） | p640-667 | 已纳管的 OXO Connect | OXO 现场标配 | OMC 许可/账号在客户侧需自备 |
| task-12 | 配置 OXE 告警上送 8770（incident manager/incident filter） | p283-289 | 告警进 Alarms 应用 | 告警集中的第一步 | 无 |
| task-13 | 定制告警处理（签名/字典/邮件通知/脚本） | p290-306 | 告警运维闭环 | 值班与工单联动 | 邮件服务器与脚本目录生产需规划 |
| task-14 | 部署 SNMP Proxy 并配置过滤 | p307-324 | 告警转 trap 送外部网管 | 与客户 NMS 集成的标准路径 | hypervisor 侧由客户维护 |
| task-15 | 配置 Topology 标准视图（设置/虚拟 ACT/背景图） | p334-338 | 网络图形视图 | 现场展示与排障 | 无 |
| task-16 | 构建 Topology 自定义视图与告警重定向 | p339-362 | 定制监控大屏 | 客户定制诉求高频 | 无 |
| task-17 | 配置安全管理（密码策略/管理员/组/单登录/解锁/OXE Access Profile/访问控制/TLS） | p382-415 | 合规的管理权限体系 | 安全审计必查项 | 生产需结合客户 AD/Radius |
| task-18 | 启用并使用 Audit（mao 日志/检索/导出/报告） | p425-434 | 操作审计能力 | 合规与追责场景 | 仅支持 OXE |
| task-19 | 生成/导出/计划报告（文件/邮件） | p443-459 | 报表分发机制 | 运营报表刚需 | 无 |
| task-20 | 编排 Scheduler 任务（简单/同步 job） | p469-487 | 自动化任务链 | 减少手工操作 | 无 |
| task-21 | 配置自动维护（五类 purge 参数/Purge job/预定义 job 恢复） | p488-502 | 数据库不膨胀的清理体系 | 长期运行稳定性的关键 | 保留期需按客户合规确定 |
| task-22 | 8770 数据库备份恢复与 rehosting（含 IP/FQDN 修改） | p514-521, p503-513 | 可用的备份恢复预案 | 灾难恢复底线 | 网络盘备份结合 task-27 |
| task-23 | 使用维护工具（Diagnostic/DirManag/HeidiSQL） | p532-538 | 排障数据采集能力 | 支持工单（SR）必备 | 无 |
| task-24 | 管理 NMC 服务与日志（启停/详细跟踪/nmclog） | p554-567 | 服务级排障手法 | 二线排障基础 | TraceType 记得改回 |
| task-25 | OXE 备份与恢复（配置/立即/计划/swinst 恢复） | p579-593 | OXE 数据安全预案 | 通话系统灾备底线 | 恢复需停机窗口 |
| task-26 | 查询与更新 8770 许可（锁/spadmin/换文件） | p610-617 | 许可合规与扩容 | 扩容与续费场景 | 新许可文件由 ACTIS 出具 |
| task-27 | 映射网络驱动器（远程共享/ADM8770/服务账号） | p668-698 | 报表与备份落网络存储 | 生产部署常见要求 | 需客户存储侧配合 |
| task-28 | 理解解决方案架构与容量要求（套件/协议/虚拟化/兼容矩阵/许可包型） | p3-40, p594-609 | 选型与方案设计依据 | 售前/交付方案输入 | 生产规模设计需 Capacity Planning 工具 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-01 服务器安装（一切的前提，且参数装后难改）
2. task-04/task-11 节点注册（OXE/OXO 接入的关口）
3. task-07/08/09/10 用户开通体系（日常最高频）
4. task-12/13/14 告警接入与出口（运维价值最高）
5. task-17 安全管理（合规必查）
6. task-22/25 备份恢复（8770 + OXE 两层灾备）
7. task-21 自动维护（长期稳定）
8. task-19/20 报表与计划任务
9. task-18/23/24 审计与排障工具
10. task-26 许可、task-27 网络盘、task-05 SSH、task-06 操作效率、task-02/15/16/28（支撑类）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 10 个一级部分（地基 2 + 安装 1 + 接入 1 + 开通/告警 2 + 增值 2 + 维护 1 + 工程支撑 1，收尾附注未计入）
- [x] 术语按实际内容列出（15 个）
- [x] 已检查作者局限/假设（实验环境明文密码、2019 章沿用旧版、OXO 章法语残句、单机闭环无高可用）
- [x] 原书关键任务 28 项，全部有来源页码、交付物与重要性依据
- [x] 全文 705 页 PAGE 标记完整覆盖（p1-705），无缺页

**用户确认时间**: 2026-09-23（流水线任务指派，按模板结构连续执行）
