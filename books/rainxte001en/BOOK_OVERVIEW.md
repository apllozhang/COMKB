# Rainbow OXO Connect 集成 (RAINXTE001EN Ed13) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: Rainbow OXO Connect (Participant's Guide)
- **作者**: ALE Training Services
- **出版/发布时间**: Edition 13（Rainbow / OXO Connect R6.3 / SP149 时代）
- **内容类型**: 课程（官方售后培训讲义 + 分步实验 How-To）
- **版本来源**: `F:\ALE知识库\Training Offer by Job Function\CBD\Cloud\RAINXTE001EN.pdf`（251 页）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To，讲义约占 60%、实验约占 40%）

### 一句话主旨
把 OXO Connect 话机系统接入 Rainbow 云协作平台：从云侧公司/订阅/账户体系搭建，到 PBX 接入与 RCC 远程控制，再到 WebRTC 网关三种拓扑部署打通音频，最后覆盖话务台监督、云维护体系与 Microsoft Teams 集成。

### 骨架 (主要论点及其关系)

1. **培训实验环境**（RLAB 远程实验室 POD 结构 + ITSP1 SIP 运营商模拟器：号码规则、账号、网关参数）
2. **Rainbow 平台概览**（UCaaS+CPaaS 双定位、8 种订阅、网络要求文档与 Rainbow Pilot 连通性工具）
3. **公司与管理体系**（Company 概念、BP/EC 两类公司、可见性四级、SSO/认证、管理员权责、订阅开通与分配）
4. **OXO 侧准备**（OMC 安装首连、IP 规划修改、PBXID+激活码接入 Rainbow、Webdiag 维护）
5. **成员与账户**（成员创建三法、成员八块设置、10 天删除宽限、分机关联 RCC 模式）
6. **WebRTC 网关**（全书核心：三种拓扑（OCE 集成/OCE Front End/外部 VM 或 NUC）、自动配置边界、虚拟终端 Twinset/Anydevice、容量规划表）
7. **话务台与监督组**（Attendant console、监督组规格、互助监督组）
8. **维护与支持**（用户日志、问题上报、status 状态页、告警、操作历史、SR 流程）
9. **Microsoft Teams 集成**（架构、应用上架与权限同意、用户配置、连接器与在场同步）

**论点之间的关系**: 层层递进为主——1 是地基，2-3 是云侧体系，4-5 是接入闭环（无网关只能 RCC），6 解锁完整音频（三种拓扑并列 + 容量 + 终端形态），7-9 是并列的三个增值能力域，培训收尾为附注。

### 作者要解决的核心问题
让售后/渠道工程师独立完成"OXO Connect + Rainbow 混合云"交付：云侧开户开订阅、PBX 接入、选型并部署合适拓扑的 WebRTC 网关、配好用户终端形态，并能处理日常维护与 Teams 共存场景。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| Rainbow | ALE 云协作应用：UCaaS（协作/云话音）+ CPaaS（开放 API 平台），混合云模式集成 OXO/OXE/第三方 PBX | 不只是"软电话 App"，是平台 + 订阅体系 + API 的整体 |
| Company | Rainbow 用户组织单元，主功能仅对公司成员开放；分 Reseller/BP 公司与 End Customer 公司 | 类似"租户"，但有 BP/EC 两级与经销角色（DR/IR/VAD）分工 |
| Subscription | 按用户分配的服务许可：Essential(免费)/Business/Enterprise/Attendant/Conference/Connect/Room 等 8 种 | 电话服务（话音/话务台）必须 Business/Enterprise/Attendant，免费 Essential 不可用 |
| RCC (Remote Call Control) | PBX 接入 Rainbow 但无 WebRTC 网关时的模式：Rainbow 仅监督话机（接听/挂断/转移），音频全在话机 | RCC 是中间态不是降级缺陷——是"无网关时的正常形态" |
| WebRTC Gateway | Rainbow 客户端与 PBX 生态间的语音互操作网关，建立音频媒体关系（HTTPS/SRTP 加密） | 它解决的是"音频"而非"呼叫控制"——呼叫控制始终在 PBX |
| 内部/外部/OCE-FE GW | 三种部署拓扑：OCE 集成（R3.2+，免 SIP trunk 许可）、OCE Front End（专用 IPBox，无 PBX 能力）、外部 VM(ESXi)/Mini PC(NUC) | 三拓扑功能级别相同，差异在承载硬件、容量与许可 |
| Free Rainbow in Twinset | R6.0 起的虚拟副站终端类型，作为物理主站的 Multiset 副站（UTL Bypass 省 UTL 许可） | R5.2 及以前该位置用 Anydevice；升级交付要留意版本语义 |
| Anydevice | 纯软话机终端类型：无物理分机，全部通信经 Rainbow 应用（Client/Web/移动） | 不等于"移动分机"；OXE 侧对应 REX（最多 10 路）而 OXO Anydevice 8 路 |
| Rainbow number | 分机关联后生成的编号（例 BBB10070254106463346）；用户选"computer"路由时由 Rainbow agent 自动写入 Remote Extension number | 是 WebRTC 音频落地的隐藏配置项，无需手工设置但排障要知道它 |
| PBXID & Activation code | OXO 接入 Rainbow 的双凭证，Rainbow 平台生成，可由经销商提供或客户端管理员在 My company/Communication 查询 | 不是 PBX 序列号；FTR 时默认 "FleetRef-Installref" 占位，正式接入前要替换 |
| Supervision group | 话务台监督组：监督员（需 Attendant 许可）+ 被监督成员同组；每监督员 ≤5 组，每组 ≤30 人 | 与 OXO 的 ACD 组完全是两回事；组是 Rainbow 侧概念 |
| Mutual aid group | 互助监督组：可临时一键加入/退出，监督员可临时纳入/排除成员；代接仅限同 PBX 电话呼叫 | "互助"是动态成员关系，不是第二种权限 |
| Visibility 四级 | 公司可见性 PUBLIC/PRIVATE/CLOSED/ISOLATED；教材建议默认 CLOSED，不推荐 ISOLATED | ISOLATED 会导致无法被外部会议（bubble）邀请，选型有代价 |
| Rainbow Pilot | 官方连通性与容量评估工具（pilot.openrainbow.com），按协作/会议/混合话音/Hub 用法混评站点承载能力 | 是售前勘测工具，与网络要求文档配合使用 |
| UTL | 通用电话许可（Universal Telephony License）；Deskphone+Free Rainbow 副站=1 UTL，Anydevice=1 UTL | Twinset 副站的意义就是"不额外吃 UTL"（UTL Bypass） |
| FTR | OXO 首次开箱流程（First Time Release）：定义产品类型（如 Frontend WebRTC）、录 IP/客户参数 | OCE-FE 的免费专用许可由 FTR 自动提供；≥R4.0 MD 强制 |

### 核心命题 (用自己的话)

1. Rainbow 与 OXO 是"混合云"关系：PBX 保留呼叫控制与现场话音，Rainbow 提供协作、移动端与云服务；WebRTC 网关补齐两侧音频互通。
2. 云侧的一切都挂在 Company 体系下：BP 公司创建 EC 公司并开通付费订阅（BP 专属权限），EC 管理员管成员、分配订阅、关联话机。
3. 成员=邮箱身份，一人不能同时在两家公司；要用电话服务必须分配 Business/Enterprise/Attendant 订阅。
4. OXO 接入 Rainbow 极简：拿到 PBXID+激活码，在 OMC/Cloud/Rainbow 填入启用即可；域名保持默认 openrainbow.com。
5. 接入后即得 RCC：Rainbow 可监督话机（接/挂/转），但音频留在话机——这是无网关时的正常形态，不是故障。
6. WebRTC 网关三种拓扑功能等价：OCE 集成（R3.2+，免 SIP trunk 许可）、OCE Front End（≥R4.0 MD，20 通话，无 PBX 能力，免专有许可 FTR 自动装）、外部 VM/NUC（50 通话）。
7. 自动配置有明确边界（R4.0.020.002 起）：网关激活/SIP 网关/SIP 账号/VoIP 接入与中继组/ARS 路由自动建；连 PBX、建 AnyDevice/Rainbow 虚拟终端、编号计划与闭锁仍是安装员责任。
8. 用户终端两形态：有话机=Multiset（物理主站+Free Rainbow in Twinset 虚拟副站，R6.0 起 UTL Bypass）；无话机=Anydevice；两者各占 1 UTL。
9. 容量规划有硬表：5 用户→5 通道，50 用户→20 通道，150 用户→50 通道；外部 GW 上限 50 通话，OCE 集成与 FE 上限 20；Rainbow VoIP 用户上限 150。
10. 话务台按订阅解锁：Attendant console 队列 OXO 8 路/OXE 10 路，监督组 ≤5 组/组、每组 ≤30 人；互助组支持动态进出；代接仅限同 PBX 的话机呼叫。
11. Teams 集成是工作台级而非租户级：Rainbow App in Teams 管电话功能，Rainbow Desktop 管点击外呼与呼叫控制；协作功能建议收敛给 Teams（只留 Telephony 权限）；订阅 Business/Enterprise；在场同步经 O365 日历共享激活。
12. 维护有云侧抓手：status.openrainbow.com 状态页+订阅告警、管理端操作历史审计、用户"Report a problem"上报（集成商同视角可见）、MyPortal 开 SR（需 Rainbow 认证伙伴）；OXO 侧用 Webdiag 查 Rainbow Status 与 ccrbagent.log。

### 论证链
教材以"云侧体系讲义 → OMC/Rainbow 双侧操作 → 分步实验 → 行为验证"推进：每个实验都有明确测试问题（如"呼叫能接吗？可用动作有哪些？"），用行为闭环替代理论论证；拓扑选型部分用对比表与容量表支撑判断。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 R6.3/SP149 与 Ed13 界面；Rainbow 管理界面迭代快，截图与菜单可能漂移。
- Anydevice 语义在 R5.2 前后不同（书中自注），Twinset 是 R6.0 新增——跨版本交付需对照 TC2479 最新版。

### 作者的立场盲点
- 全书默认实验环境：明文密码（pbxk1064 / alcatel / Superuser-P* / PasswordP*）遍布正文；生产的安全基线（防火墙白名单、TURN 位置选择、证书轮换）只有链接指针没有展开。
- 编号计划与闭锁（barring）被反复列为"安装员自做"，但全书无一处教怎么做——连接 Rainbow 的最后一步其实在书外。
- Teams 集成只讲单用户工作台体验，Teams 租户侧策略（应用权限策略、紧急呼叫、直接路由共存）缺位。

### 未被证明的假设
- 假设读者持有 BP/经销商账号与 RLAB 环境（生产中 EC 管理员常常没有 PBX 创建权限）。
- 假设 Azure AD/O365 环境现成可用，SSO 与在场同步的前置条件未核查。
- 假设 ITSP 模拟器行为与生产 SIP 中继一致（安全、编解码、号码格式差异大）。

### 最强反对意见
"这本手册教的是把 PBX 挂上 Rainbow 的最小闭环，不是混合云交付"——网络要求（端口/域名/带宽）、TURN 部署、编号计划、Teams 租户策略都只是引用外部文档。因此每个能力的 Boundary 必须标注"实验环境口径"，并显式指向 Network Requirements PDF、TC2479、Rainbow WebRTC cookbook 三份外部文档作为生产化依据。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] Rainbow 网络前提核查与 Pilot 连通性评估
- [x] 公司体系规划（BP/EC 创建、可见性四级选型、SSO/认证方式）
- [x] 管理员权责划分与企业目录/信息频道配置
- [x] 订阅开通与分配（月付/预付、按成员分配）
- [x] OMC 安装与首次连接（证书/密码/客户信息）
- [x] OXO 与客户端 IP 规划修改
- [x] OXO 接入 Rainbow（PBXID/激活码）与接入排障（Webdiag/ccrbagent.log）
- [x] 成员管理（手动/邀请/CSV 批量/Azure AD、八块设置、10 天宽限期恢复）
- [x] 分机关联与 RCC 模式验证
- [x] WebRTC 网关拓扑决策（三拓扑对比 + 版本前提）
- [x] 三拓扑部署流程（集成/FE FTR/外部 VM 或 NUC）
- [x] WebRTC 网关容量规划（对照表 + 20/50 上限）
- [x] 内部 WebRTC 网关自动配置（Reseller 激活 + OMC 核验 + 自动配置边界）
- [x] 虚拟终端配置（Twinset 副站/Anydevice + UTL 影响）
- [x] Attendant 话务台与监督组（订阅/建组/规格）
- [x] 互助监督组（动态进出/纳排成员/代接限制）
- [x] Rainbow 维护与支持体系（日志/状态页/告警/操作历史/SR）
- [x] Microsoft Teams 集成部署（上架/权限同意/Azure 核验）
- [x] Teams 集成用户配置（关联/Telephony 权限/订阅收敛）
- [x] Teams 连接器与在场同步（Desktop 依赖/O365 共享）

### 不适合 skill 化的内容
- RLAB 实验环境与 SIP 模拟器细节（p9-27，教学专用基础设施，仅作 Boundary 背景）
- 培训评估/证书流程（p245-251）
- 邮件服务器收信检查等课堂操作细节（p106-108 的教学专用提示）

### 预估 skill 数量
**约 10-12 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；入口软预算 8 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 核查 Rainbow 网络前提并用 Pilot 评估站点连通性与承载能力 | p35-45 | 网络/带宽/端口就绪结论 | 一切上线的前提，官方文档指针 + 工具 | 生产需对照 Network Requirements PDF 全文 |
| task-02 | 规划并创建公司体系（BP 建 EC、可见性选型、SSO/TOTP 认证） | p46-55 | 可用的 EC 公司 | 云侧体系地基 | SSO 依赖客户 Azure AD/ADFS |
| task-03 | 划分管理员权责，配置企业目录与信息频道 | p56-62 | 权责清晰的管理团队 + 目录 | 多管理员协作与来电识别 | 无 |
| task-04 | 开通订阅并分配给成员（月付/预付、Voice 订阅类型） | p63-68 | 成员可用的服务许可 | 电话功能的前置条件 | 无 |
| task-05 | 安装 OMC 并首次连接 OXO（Expert 模式、证书、改密、客户信息） | p69-78 | 可用的管理控制台连接 | PBX 侧一切配置的前提 | 无 |
| task-06 | 修改 OXO 与客户端 PC 的 IP 规划 | p79-82 | 按客户网段可管理的新地址 | 现场交付第一步 | 无 |
| task-07 | 用 PBXID+激活码接入 Rainbow 并验证（Webdiag/ccrbagent.log） | p83-89 | PBX-Rainbow 连接 established | 混合闭环的关键一步 | 无 |
| task-08 | 创建与管理 Rainbow 成员（手动/邀请/CSV/Azure AD；设置、删除宽限、密码策略） | p90-110 | 带订阅的成员账户 | 云侧日常运营主体 | 无 |
| task-09 | 将 OXO 分机关联到 Rainbow 账户并验证 RCC（呼出/呼入/动作范围） | p111-116 | RCC 可用的用户 | 无网关阶段的交付形态 | 无 |
| task-10 | 决策 WebRTC 网关拓扑（三拓扑对比、版本前提、自动配置边界） | p117-123 | 拓扑选型结论 | 全书最核心的架构决策 | 生产需结合 TC2479/cookbook |
| task-11 | 按所选拓扑部署 WebRTC 网关（OCE 集成/OCE-FE FTR/外部 VM 或 NUC） | p124-145 | 音频互通的网关 | 解锁完整功能 | TURN/防火墙细节在书外 |
| task-12 | 按容量表规划网关通道数与用户上限 | p146-147 | 通道数与拓扑容量方案 | 避免上线即瓶颈 | 话务建模在书外 |
| task-13 | 执行内部 WebRTC 网关自动配置（Reseller 激活 + OMC 核验） | p149-154 | 自动配置完成的网关 | R4.0.020.002+ 标准路径 | 无 |
| task-14 | 配置用户虚拟终端（Twinset 副站/Anydevice）并理解 UTL 影响 | p155-161 | 两种形态可用的用户 | 决定用户实际体验与许可成本 | 无 |
| task-15 | 部署 Attendant 话务台与监督组（订阅、建组、规格） | p162-179 | 可用的话务台 | 前台/秘书场景刚需 | 无 |
| task-16 | 建互助监督组并执行临时进出/纳排/代接 | p170-173, 180-181 | 灵活的互助监督 | 团队互助场景 | 代接仅限同 PBX 电话呼叫 |
| task-17 | 运用维护体系排障（用户日志/问题上报/状态页/告警/操作历史/SR） | p182-194 | 可运转的运维闭环 | 售后日常 | 无 |
| task-18 | 完成 Teams 集成全流程（上架/权限/用户配置/连接器/在场同步） | p195-244 | Teams 内可用的电话集成 | 客户最常见的共存诉求 | Teams 租户策略在书外 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-07 OXO 接入 Rainbow（混合闭环的第一关口）
2. task-10 WebRTC 拓扑决策（架构错误的代价最高）
3. task-11/13 网关部署与自动配置（核心交付动作）
4. task-14 虚拟终端形态（直接影响用户与许可）
5. task-08 成员管理（云侧日常运营最高频）
6. task-09 RCC 关联（无网关阶段交付 + 排障入口）
7. task-12 容量规划（售前/交付都要用）
8. task-15/16 话务台与监督组
9. task-18 Teams 集成
10. task-05/06/02/03/04/01/17（一次性或支撑类任务）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 9 个一级部分（1 地基 + 云侧体系 2 + 接入闭环 2 + 网关核心 1 + 增值域 3，收尾附注未计入）
- [x] 术语按实际内容列出（17 个）
- [x] 已检查作者局限/假设（实验环境口径、明文密码、编号计划缺位、Teams 租户缺位）
- [x] 原书关键任务 18 项，全部有来源页码、交付物与重要性依据
- [x] 用户已授权全流程连续执行（"现在开始"，2026-09-23）——骨架要点已在对话中展示，可随时纠偏

**用户确认时间**: 2026-09-23（全流程授权）
