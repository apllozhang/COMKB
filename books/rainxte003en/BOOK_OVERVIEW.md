# Rainbow for OmniPCX Enterprise 集成 (RAINXTE003EN Ed12) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: Rainbow / OmniPCX Enterprise (Participant's Guide)
- **作者**: ALE Training Services
- **出版/发布时间**: Edition 12（Rainbow R101.1 N4 MD4 / SP161 与 OmniPCX Enterprise Edition 12 时代）
- **内容类型**: 课程（官方售后培训讲义 + 分步实验 How-To；讲义与实验各约占一半）
- **版本来源**: 全文提取自 `F:\AIwork\ZCode\books\rainxte003en\source_fulltext.txt`（314 页，PAGE 标记 1-314）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To；How-To 实验章共 14 个，含大量 CLI/命令行与 OXE Web 管理（WBM）界面操作）

### 一句话主旨
把 OmniPCX Enterprise 话机系统接入 Rainbow 云协作平台：从云侧公司/订阅/账户体系，到 OXE 侧 DNS/代理、Rainbow Agent 接入、REX/Ghost Z 远程延伸与路由，再到 WebRTC 网关部署配置与共享池化打通 VoIP 音频，最后覆盖 4059EE 与 Rainbow 两种话务台、维护支持体系与 Microsoft Teams 集成。

### 骨架 (主要论点及其关系)

1. **培训实验环境**（RLAB 远程实验室 POD：6 台虚机 + ITSP1 SIP 运营商模拟器：号码规则、DDI 翻译、账号）
2. **Rainbow 平台概览**（UCaaS+CPaaS 双定位、8 种订阅、网络要求文档体系与 Rainbow Pilot 评估工具）
3. **公司与管理体系**（Company 两类、可见性四级、SSO/TOTP 认证、管理员权责、企业目录、信息频道、订阅开通与分配）
4. **OXE 接入**（netadmin 配置 DNS/代理、Rainbow Agent 以 PBXID+激活码启用、incvisu/checkCloudConfig.sh/日志四类维护抓手）
5. **成员与设备关联**（成员创建、分机关联得 Rainbow number、RCC 模式、REX/Ghost Z/tandem 机制、路由四案例、远程延伸 How-To）
6. **WebRTC 网关**（全书核心：角色与前提 OXE ≥12.1 MD4、用户两类型+DECT 特例、部署配置 VM（mp 命令族）、升级两法、OXE 侧九件套配置、共享池化与 406 溢出、TBE067 sizing 400 并发）
7. **话务台域**（4059EE 话务台 + Rainbow 集成/BLF、Rainbow Attendant Console 与监督组/互助监督组）
8. **维护与支持**（帮助台指南、用户日志、问题上报、状态页、告警、操作历史、SR 流程）
9. **Microsoft Teams 集成**（工作站级架构、Teams 管理中心上架与权限同意、用户配置收敛 Telephony、连接器与在场同步）

**论点之间的关系**: 层层递进为主——1 是地基，2-3 是云侧体系，4-5 是接入闭环（无网关时先 RCC，配 REX/tandem 后解锁外部路由），6 解锁完整 VoIP 音频（部署+升级+OXE 配置+共享池化一条龙），7-9 是并列的三个增值能力域，培训收尾为附注。

### 作者要解决的核心问题
让售后/渠道工程师独立完成"OmniPCX Enterprise + Rainbow 混合云"交付：云侧开户开订阅、OXE 配网接入、用 REX/Ghost Z 搭建呼叫路由、选型部署 WebRTC 网关（单机或共享池）、配好 OXE 侧 SIP/ARS/回调九件套，并能交付 4059EE/Rainbow 两种话务台、处理日常维护与 Teams 共存场景。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| Rainbow | ALE 云协作应用：UCaaS（协作/云话音）+ CPaaS（开放 API 平台），混合云模式集成 OXE/OXO/第三方 PBX | 不只是"软电话 App"，是平台 + 订阅体系 + API 的整体 |
| Company | Rainbow 用户组织单元；分 Reseller/BP 公司与 End Customer 公司；一人不能同时属两家公司 | 类似"租户"，但有 BP/EC 两级与经销角色（DR/IR/VAD）分工 |
| Subscription | 按用户分配的服务许可：Essential(免费)/Business/Enterprise/Attendant/Enterprise Conference/Conference/Connect/Room 8 种 | 电话服务必须 Business/Enterprise/Attendant；免费 Essential 只有 RCC 无路由 |
| RCC (Remote Call Control) | 无 WebRTC 网关时 Rainbow 仅监督话机（接听/挂断/转移），音频全在话机；Essential 订阅只有此能力且不能改路由 | RCC 是中间态不是降级缺陷；Business/Enterprise 无网关时还能靠 REX 路由 |
| REX (Remote Extension) | OXE 特殊终端设备，让 OXE 把呼叫转往外部资源；靠内部技术资源 Ghost Z 承载并发，通话结束释放 | 它是"呼叫路由载体"而非"移动分机"；Rainbow agent 按用户路由自动改写 REX 内容 |
| Ghost Z | REX 功能专用的内部技术设备；每个 REX 并发呼叫需一个 Ghost Z；目录号建议用字母（如 DB1000）优化拨号计划 | 不是"许可"，是系统资源；数量决定 REX 并发上限 |
| Tandem | 主站（Deskphone）+ 副站（REX）的成对结构；两端都必须配 multi-line（≥2 线） | tandem ≠ 转发（书："Call Routing is not a Forwarding"）；配置只做在主站，自动同步副站 |
| Rainbow number | 分机关联后出现、以 BBB ARS 前缀开头的 17 位编号（例 BBB10070254106463346）；用户选"computer"路由时由 Rainbow agent 自动写入 REX 的 Remote Extension number | 不是用户可拨的"号码"，是 OXE 侧路由判别的技术编号，排障要用 remotesets 查看 |
| WebRTC Gateway | Rainbow 客户端与 PBX 资源间语音互通的软件组件：客户 premises 的 Debian VM（OVF 由 ALE 交付）；要求 OXE ≥12.1 MD4/12.2、成员持 Business/Enterprise 订阅 | 它解决"音频媒体"，呼叫控制始终在 PBX；不是硬件盒子而是可共享池化的 VM |
| Shared/scalable WRG | 多个 OXE 共享网关池：靠 ARS 溢出机制分流（网关满时回 SIP 406 Not Acceptable 触发下一路由）；每 OXE 每网关一条 SIP trunk | 扩容靠池化而非每 OXE 挂一个网关；OXE ≥5000 用户时才考虑每 OXE 网关复制 |
| ARS 前缀 BBB | WebRTC 网关专用 ARS 前缀；判别器规则按 17 位号码（Call Number 1/Area 1/route list/schedule -1）匹配 Rainbow agent 写入的号码 | 与标准外呼前缀（走公共 trunk）是两条路：mobile/home 路由走公网，computer 路由走网关 |
| 4059 EE | 传统话务台应用（OXE 里声明为 4059 IP set）：只管话务功能不处理话音，必须关联一部非 multi-line 的物理话机或 IPDSP | 与 Rainbow "Attendant 订阅"无关（书中明确）；Rainbow 在场与电话在场在其界面上是两个信息 |
| Attendant console | Rainbow 内嵌话务台（Web/Desktop）：呼叫队列 OXE 10 路/OXO 8 路 + BLF 监督区 + 监督组页签；需每人 Attendant 订阅；仅 PC 端 | 与 4059EE 是两套话务台；监督组是 Rainbow 侧概念，与 OXE 呼叫分配组（attendant group）不同 |
| Mutual aid group | 互助监督组：一键进出、临时纳排成员；代接仅对 PBX 电话呼叫有效；同时最多监督 4 路；可锁定最后一名成员 | "互助"是动态成员关系，不是第二种权限 |
| Rainbow Pilot | 官方连通性与容量评估工具（pilot.openrainbow.com），按协作/会议/混合话音/Hub 用法混评站点承载能力 | 是售前勘测工具，与 Network Requirements PDF 配合使用 |
| Rainbow App in Teams / Rainbow Desktop | Teams 集成双件套：App 管 telephony 设置/呼叫历史/留言/拨号盘；Desktop 管点击外呼（热键）与单呼叫控制，必须安装且运行 | 集成在工作站级而非租户级；Desktop 是硬依赖，缺了 Teams 内应用显示 "!" |
| Sizing 工具 (TBE067) | WebRTC 网关容量估算 Excel 工具（TBE067_Rainbow - WebRTC Gateway Pres&Sizing - ed06l.zip）：输入用户数/Rainbow 用户占比/直呼占比得并发通道数，再定 OXE 压缩器；单网关上限 400 并发流 | 通道数是"并发流"口径，与用户数是两个量纲；工具适用于 OXE 101.0 MD3 / WebRTC 3.x 起 |

### 核心命题 (用自己的话)

1. Rainbow 与 OXE 是"混合云"关系：OXE 保留呼叫控制与话音资源（trunk group、话务、留言），Rainbow 提供协作、移动端与云服务；OXE 内置 Rainbow Agent，用 PBXID+激活码接入，无需外加硬件。
2. 云侧一切挂在 Company 体系下：BP 公司独享"申报与创建 PBX、开通付费订阅"两项权限；EC 公司有且只能挂靠一个 BP；客户管理员管成员、订阅分配与话机关联。
3. 成员=邮箱身份，一人只能属一家公司；要用电话服务必须 Business/Enterprise/Attendant 订阅；密码策略至少 12 位含大写/数字/特殊字符；删除有 10 天宽限期，恢复后降为 Essential 且需重配订阅与话机线。
4. OXE 接入前先配 DNS/代理（netadmin 菜单 14/15，仅 Rainbow 与 Cloud Connect agent 使用）；验证 DNS 要用 nslookup/dig，URL ping 不算数；OXE 的 HTTPS 测试只能用 IP 且 curl 报证书错误属正常（ALE 专有证书）。
5. 无网关时两级用法：Essential=RCC 只监督；Business/Enterprise=话机与 REX 成 tandem，可改路由到手机/家庭号——路由（routing）与呼叫转发（forwarding）是两回事。
6. REX/Ghost Z 是路由机制的地基：每个 REX 并发呼叫占一个 Ghost Z；Rainbow agent 按用户路由选择自动改写 REX 指向（外部号码经公共 trunk，computer 路由经 BBB 前缀走 WebRTC 网关）；tandem 两端必须 multi-line。
7. WebRTC 网关部署是标准 VM 流程：MyPortal 下载 OVF（OXE/OXO 同一软件）、mpnetwork 配网、mpconfig 填 PBX 域名+PBXID、mpshow/mpcheck 核验、BP 在 Rainbow 侧激活；OXE 侧前提 12.1 MD4/12.2+。
8. OXE 侧网关配套有固定清单：SIP trunk group（T2/SIP）、可信 IP、SIP 外部网关（Gateway type=Rainbow type，仅 G711，端口 5060/UDP）、IP 域无压缩+压缩资源（GD/OMS）、CDT+ARS 路由+BBB 前缀+17 位判别器、CSTA 回调+回调翻译表（DEF→BBB）+专用实体；CPaaS 场景另加主叫名显示与 CLI 格式。
9. 共享网关池是规模化解法：多 OXE 共享网关池，靠 ARS 溢出（网关流量上限满时回 SIP 406 触发下一路由；参数为空则由 SIP trunk 限制决定）；每 OXE 每网关一条 SIP trunk；单网关 400 并发流，容量用 TBE067 工具按用户占比估算。
10. 话务台有两套：4059EE 走 OXE 传统话务（attendant group/CDT/个人呼叫前缀，关联话机不能 multi-line，Rainbow 集成提供在场/搜索/IM/BLF）；Rainbow Attendant Console 走订阅（队列 OXE 10/OXO 8，监督组监督员 ≤5 组、每组 ≤30 人）；两者都强调 Rainbow 在场与电话在场是两个不同信息。
11. Teams 集成在工作站级：Rainbow App in Teams（Telephony Power App）+ Rainbow Desktop（点击外呼/呼叫控制，必须运行）；权限收敛为 Telephony（协作交 Teams 原生）；订阅 Business/Enterprise；在场同步经 O365 信息共享激活；SSO 非必需。
12. 维护抓手双侧齐备：OXE 侧 incvisu（五条链路 4503/4505/4509/4507/4511）、dhs3_init -R RAINBOWAGENT、checkCloudConfig.sh -rainbow、rainbowagent.log；网关侧 mpcheck+三服务；云侧状态页订阅告警、操作历史审计、用户"Report a problem"（集成商同视角）、MyPortal 开 SR（需 Rainbow 认证伙伴）。

### 论证链
教材以"云侧体系讲义 → OXE/网关双侧操作 → 分步实验 → 行为验证"推进：每个实验都有明确测试问题（如"Is it possible? What is the calling number displayed? Which action(s) is/are possible?"），用行为闭环替代理论论证；架构选型部分（网关池化、sizing）用对比表与工具支撑判断；OXE 侧配置给出完整参数表（如 SIP 外部网关逐字段值），可照抄复现。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 Rainbow R101.1 N4 MD4/SP161 与 OXE Ed12 界面；WBM 菜单、Rainbow 管理界面迭代快，截图与字段可能漂移。
- 网关软件示例版本 1.78.11-470、rainbowagent 6.0.1 为当时样例；远程升级适用范围（1.73.x+、35 国）随版本演进，须以支持网站最新文为准。
- 教材对 Rainbow 命名仍处过渡期（R101.x 新版号），跨版本交付要对照 TC2462 最新版。

### 作者的立场盲点
- 全书默认实验环境：明文密码（Rainbow123 / Superuser-P* / PasswordP* / alcatel）遍布正文；mpssh on 开 SSH 只讲操作不讲安全基线；TURN_SERVER=GEOIP 一笔带过，生产 TURN 位置选择、防火墙白名单只给外部文档指针。
- 实验中 BP 专属动作（PBX 创建、订阅开通、网关激活）一律"由讲师完成"，客户管理员视角的完整交付路径在书内是断的。
- 4059EE 章复用 user2 邮箱但姓名前后不一（p64 Rains Robby vs p216 Betty Carol），书中未解释，照抄实验会困惑。
- Teams 集成只讲工作站体验，Teams 租户侧策略（应用权限策略、紧急呼叫、直接路由共存）缺位。

### 未被证明的假设
- 假设读者持有 BP/经销商账号与 RLAB 环境（生产中 EC 管理员常常没有 PBX 创建与网关激活权限）。
- 假设 OXE 侧话机（IPDSP 31000/31001）、机架板卡、SIP trunk 已由 Pod 预置——存量现场要从零做。
- 假设 ITSP 模拟器行为与生产 SIP 中继一致（安全、编解码、号码格式差异大；书中 SIP 外部网关仅 G711/UDP 的取值也是实验口径）。
- 假设 Azure AD/O365 环境现成可用，Teams 管理员有权限上架应用并同意权限。

### 最强反对意见
"这本手册教的是把 OXE 挂上 Rainbow 的最小闭环，不是混合云交付"——网络要求（端口/域名/带宽）、TURN 部署、sizing 工具本体、共享池化的 OXE 侧详细配置都外置到 Network Requirements PDF、TC2462、TBE067 工具包与支持网站文章。因此每个能力的 Boundary 必须标注"实验环境口径"，并显式指向这四份外部材料作为生产化依据。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] Rainbow 网络前提核查与 Pilot 连通性评估
- [x] 公司体系规划（BP/EC 创建、可见性四级选型、SSO/TOTP 认证）
- [x] 管理员权责划分与企业目录/信息频道配置
- [x] 订阅开通与分配（月付/预付、电话服务订阅门槛）
- [x] RLAB/OXE 实验环境搭建（虚机、机架板卡、用户、外部 SIP 网关、DID 翻译）
- [x] OXE 呼叫服务器 DNS/代理配置与连通性验证（netadmin/nslookup/curl）
- [x] OXE 接入 Rainbow（PBXID/激活码）与接入排障（incvisu/checkCloudConfig.sh/rainbowagent.log）
- [x] 成员管理（手动/邀请、密码策略、10 天宽限期、安全改密）
- [x] 分机关联与 RCC 模式验证
- [x] OXE 用户模式决策（RCC vs REX 路由 vs 纯 REX vs DECT 特例）
- [x] 远程延伸配置（Ghost Z 池、REX、multi-line、tandem、溢出）+ Nomadic 测试
- [x] WebRTC 网关部署配置（VM 下载、mp 命令族、mpcheck 核验、BP 激活）
- [x] WebRTC 网关升级（远程/手动两法 + 失败处理）
- [x] OXE 侧网关九件套配置（SIP TG/可信 IP/Rainbow type 网关/IP 域/CDT/ARS/BBB/判别器/回调）+ VoIP 测试
- [x] 共享网关池架构决策与容量规划（406 溢出、TBE067、400 并发）
- [x] 4059EE 话务台交付（话务组/话务台/CDT/Rainbow 集成/BLF/在场差异测试）
- [x] Rainbow Attendant Console 与监督组/互助组（订阅、建组、规格）
- [x] Rainbow 维护与支持体系（日志/状态页/告警/操作历史/SR）
- [x] Microsoft Teams 集成部署（上架/权限同意/Azure 核验）
- [x] Teams 集成用户配置（关联/Telephony 权限/订阅收敛）
- [x] Teams 连接器与在场同步（Desktop 依赖/O365 共享）

### 不适合 skill 化的内容
- RLAB 实验环境与 SIP 模拟器细节（p3-18，教学专用基础设施，仅作 Boundary 背景）
- 培训评估/证书流程（p308-314）
- 邮箱清理等课堂操作细节（p65/p76 的教学专用提示）

### 预估 skill 数量
**约 11-13 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 核查 Rainbow 网络前提并用 Pilot 评估站点连通性与承载能力 | p26-36 | 网络/端口就绪结论 | 一切上线的前提，官方文档指针 + 工具 | 生产需对照 Network Requirements PDF 全文 |
| task-02 | 规划并创建公司体系（BP 建 EC、可见性选型、SSO/TOTP 认证） | p37-46 | 可用的 EC 公司 | 云侧体系地基 | SSO 依赖客户 Azure AD/ADFS |
| task-03 | 划分管理员权责，配置企业目录与信息频道 | p47-53 | 权责清晰的管理团队 + 目录 | 多管理员协作与来电识别 | 无 |
| task-04 | 开通订阅并分配给成员（月付/预付、电话服务门槛） | p54-59 | 成员可用的服务许可 | 电话功能的前置条件 | 无 |
| task-05 | 配置实验 Pod（虚机确认、机架板卡、IPDSP 用户、外部 SIP 网关、DID 翻译、外呼验证） | p70-76 | 可内外呼叫的 OXE 基线 | 一切 OXE 侧实验的前提 | 生产现场拓扑不同，仅方法论可迁移 |
| task-06 | 配置 OXE 呼叫服务器 DNS/代理并验证连通 | p77-82 | DNS/代理就绪的 Call Server | Rainbow/Cloud Connect agent 的网络前提 | 生产防火墙/代理细节在书外 |
| task-07 | 用 PBXID+激活码接入 Rainbow 并验证、维护（incvisu/checkCloudConfig.sh/日志） | p83-88 | PBX-Rainbow 连接 established | 混合闭环的关键一步 | 无 |
| task-08 | 创建与管理 Rainbow 成员（手动/邀请；密码策略、宽限期、安全） | p60-65, p94-105 | 带订阅的成员账户 | 云侧日常运营主体 | CSV/Azure AD 批量仅讲义级 |
| task-09 | 将 OXE 分机关联到 Rainbow 账户并验证 RCC（5 项呼叫测试） | p89-93 | RCC 可用的用户 | 无网关阶段的交付形态 | 无 |
| task-10 | 决策 OXE 用户使用 Rainbow 的形态（RCC/REX 路由/纯 REX/DECT 特例） | p106-118 | 用户形态与订阅方案 | 架构决策，影响许可与体验 | 无 |
| task-11 | 配置远程延伸（Ghost Z 池/REX/tandem/溢出）并做 Nomadic 测试 | p119-130（TC2462） | 可路由的 nomadic 用户 | REX 机制落地 + 4 案例路由验证 | TC2462 全文为生产依据 |
| task-12 | 部署并配置 WebRTC 网关 VM（下载/网络/PBX 参数/核验/BP 激活/排障） | p153-162 | 音频互通的网关 | 解锁完整 VoIP | TURN/防火墙细节在书外 |
| task-13 | 升级 WebRTC 网关（远程/手动两法、失败处理） | p163-176 | 新版本网关 | 长期运维必做 | 远程升级范围（35 国）随版本变化 |
| task-14 | 完成 OXE 侧网关配置九件套并做 VoIP 四项测试 | p177-197 | OXE-RGW 路由打通 | 全书最重的一个 How-To（21 页） | 生产编解码/中继参数需调整 |
| task-15 | 规划共享网关池与容量（三配置对比、406 溢出、TBE067 sizing、400 上限） | p146-152 | 网关池化与通道数方案 | 规模化部署的核心决策 | TBE067 工具本体与话务建模在书外 |
| task-16 | 交付 4059EE 话务台并集成 Rainbow（话务组/话务台/CDT/BLF/在场差异测试） | p198-224 | 可用的话务台 + BLF | 前台/秘书场景刚需（OXE 传统线） | 无 |
| task-17 | 部署 Rainbow Attendant Console 与互助监督组（订阅、建组、规格） | p225-244 | 可用的云话务台 | 前台/秘书场景刚需（Rainbow 线） | 无 |
| task-18 | 运用维护体系排障（日志/问题上报/状态页/告警/操作历史/SR） | p245-257 | 可运转的运维闭环 | 售后日常 | 无 |
| task-19 | 完成 Teams 集成全流程（上架/权限/用户配置/连接器/在场同步） | p258-307 | Teams 内可用的电话集成 | 客户最常见的共存诉求 | Teams 租户策略在书外 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-07 OXE 接入 Rainbow（混合闭环的第一关口）
2. task-14 OXE 侧网关九件套配置（全书最重实验，配错即不通）
3. task-12 网关部署（核心交付动作）
4. task-11 远程延伸配置（REX/tandem 是路由与网关的共同地基）
5. task-10 用户形态决策（架构错误的代价最高）
6. task-15 共享池化与容量规划（售前/交付都要用）
7. task-09 RCC 关联（无网关阶段交付 + 排障入口）
8. task-08 成员管理（云侧日常运营最高频）
9. task-16/17 两种话务台
10. task-19 Teams 集成
11. task-05/06/02/03/04/01/13/18（一次性或支撑类任务）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 9 个一级部分（1 地基 + 云侧体系 2 + 接入闭环 2 + 网关核心 1 + 话务台/维护/Teams 3，收尾附注未计入）
- [x] 术语按实际内容列出（17 个）
- [x] 已检查作者局限/假设（实验环境口径、明文密码、BP 动作由讲师代做、user2 姓名不一致、Teams 租户缺位）
- [x] 原书关键任务 19 项，全部有来源页码、交付物与重要性依据
- [x] 用户已授权全流程连续执行（任务指令自带授权，2026-09-23）

**用户确认时间**: 2026-09-23（任务指令全流程授权）
