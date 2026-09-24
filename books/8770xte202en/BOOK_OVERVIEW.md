# OmniVista 8770 目录管理 (8770XTE202EN Ed40) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OmniVista 8770 — Directory Administration (Participant's Guide)
- **作者**: ALE Training Services
- **出版/发布时间**: Edition 40（OmniVista 8770 R5.2 时代）
- **内容类型**: 课程（官方售后培训讲义幻灯片 + 分步实验 How-To，讲义约占 45%、实验约占 55%）
- **版本来源**: `F:\AIwork\ZCode\books\8770xte202en\source_fulltext.txt`（565 页，PDF 页码口径）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To；实验章节占大头且每步带界面动作与字段表）

### 一句话主旨
把 OmniVista 8770 的"公司目录"做成企业通信的数据中枢：OXE 注册同步把话机用户喂进 LDAP 目录树，六类链接把人与话机绑定，保密级别控制谁能看什么，Web 目录客户端与 Click to Call 把目录变成可拨号的前台，MSAD/Azure AD 同步与 LDIF 工具打通企业身份数据管道，管理域与委派支撑多站点多租户运营，目录复制提供数据冗余。

### 骨架 (主要论点及其关系)

1. **解决方案总览**（8770 套件全景：网络拓扑、架构协议、虚拟化、跨版本兼容、四大套件应用与 WBM 客户端——本书只讲目录套件，其余是背景）
2. **培训环境**（RLAB POD 结构 + ITSP1 SIP 运营商模拟器：实例表、号码规则、DDI 表）
3. **目录应用核心概念**（LDAP v3 目录树、Organization/Termination 条目、UID/DN、六类人员-用户链接、数据更新方向、LDIF 导入导出）
4. **OXE 接入与自动创建**（节点注册三步：准备/声明/同步；从 PCX 事件自动创建人员、UID 构造防同名、自动继承）
5. **链接管理与改名语义**（副链/传真链/多设备链实操；从目录/配置/Users/WBM 四个入口改名的不同后果与修复流程）
6. **Web 目录客户端**（匿名/认证两级访问、个人地址簿、经理/助理链接、Click to Call 原理）
7. **保密与权限体系**（四级保密条目 × 两个应用共十档访问级别的矩阵；管理员账户在 Security 应用中建）
8. **Click to Call 交付**（ISDN 号构造公式、DDI 翻译器、STAP 权限、三类前缀规则与属性关联）
9. **外观与词典定制**（LdapAttributes.dict 属性改名 + Web 客户端主题/网格/详情页定制，含备份与回退）
10. **企业身份数据管道**（MSAD 同步：属性映射+同步规则；Azure AD 同步；MSAD 插件从 AD 直接开通 OXE 用户；LDIF 命令行工具做批量转换/导入/清理/链接计算）
11. **规模化运营**（管理域与本地管理员委派、定制视图简化开户、目录复制主从冗余）
12. **收尾**（培训评估与证书流程，非技术内容）

**论点之间的关系**: 3 是概念地基（全书所有实验都在这个语义模型上展开），4-5 是"接 OXE 进目录"的闭环，6-8 是"把目录用起来"的三个面向（查询、保密、拨号），9 是定制层，10 是数据管道（三条并列通道：MSAD 双向同步 / Azure AD 单向拉取 / LDIF 批量管道），11 是多组织运营层，1-2 是背景。实验章与讲义章一一配对，讲义给模型、实验给动作。

### 作者要解决的核心问题
让售后/交付工程师独立完成 OmniVista 8770 目录功能的部署与运营：接 OXE、建目录树、绑人机链接、配保密与拨号、对接企业 Active Directory、按组织分域委派管理，并保证目录数据可批量维护、可冗余、可回退。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| Company Directory | 8770 里的 LDAP v3 公司目录：按地理位置/部门/员工存组织数据，与通信服务器双向同步 | 不是"通讯录文件"，是带同步引擎的目录服务器（含 MariaDB/LDAP 双存储） |
| Directory entry | 目录条目两类：Organization（Country/City/Company/Department）与 Termination（Person/Group/Room） | "Person"只是终止条目的一种，组织节点本身也是条目 |
| UID (User Identifier) | 人员唯一标识，默认"名+姓"，公司目录内唯一；可改为"名+姓+分机号"防同名 | UID 是目录记录的 key，不是登录账号；改构造方法只影响自动创建 |
| DN (Distinguished Name) | 条目在目录树中的唯一位置路径；目录条目与配置条目 DN 格式不同（uid=... ou=... o=... vs TelephoneNumber=... Cn=... Subnetwork...） | 与标准 LDAP DN 同构，但 8770 有自己固定的后缀（o=directoryroot / o=nmc） |
| Primary link | 人员↔OXE 用户的一对一主链接（姓名+成本中心一致），每条目仅一条；姓名/名字修改必须经公司目录 | 主链接是"人机绑定"的根；其它链接都是挂在其上的扩展 |
| Secondary/Multi-device link | 副链：一人多话机（如 DECT，成本中心继承主链接）；多设备链：经 Users 应用建，多话机共用同一条目 | 多设备链是副链的"正规军"版本（同步后自动建）， cardinality 同为 1 entry => n users |
| Fax / Miscellaneous / Additional resources link | 传真链（n:n，成本中心不变）、杂项链（数据终端/Modem）、附加资源链（主链接同性质，用于 4760 迁移多主链） | 这三类解决"非话音终端"与"历史迁移"的绑定需求 |
| Automatic creation | PCX 侧建用户事件到达后，8770 自动在指定位置建人员并建主链接；UID 重名时拒建并告警 | 是"事件驱动"的目录供给，不是批量导入；受 AutomaticCreation 参数与 Location 路径控制 |
| Confidentiality level | 条目保密四级：Green（默认）/Orange/Red/Administration 8770；决定匿名与认证访问的可见范围 | 保密级别挂在"人员条目"上，与管理员权限体系（访问级别）是两套正交机制 |
| Personal data | 个人属性五种：家庭电话/家庭住址/驾照/工号/密码；其余为非个人数据 | "密码"（人员 UID 密码）也算 personal data，认证本人可见 |
| Click to Call (STAP) | 从 Web 目录客户端发起自动呼叫：先绑关联话机（分机号+密码），再点属性拨号；OXE SIP 话机不支持 | STAP 是权限名（Off hook/Authorized/Forbidden），Click to Call 是功能名 |
| ISDN number | 8770 自动构造的外部号码：ISDN 前缀+实体安装号+话机号；DDI 话机用 DDI 号替换 | 不是"ISDN 线路号"，是由同步数据拼出来的可拨外部号码；改了 PCX 数据必须重新同步 |
| DDI translator | DDI 号码翻译器（首个外部号+首个内部号+范围大小），决定 DDI↔内线映射 | PCX 侧配置，8770 同步时取回；选择哪些翻译器取回由 PCX 页签的 DID translation usage 控制 |
| Prefix rule | 拨号前缀规则三类：None/外部呼叫规则（加删前缀）/网间呼叫规则（选目标网络+加前缀） | 是 8770 侧的"迷你 ARS"，与 PCX 的 ARS 是两回事；PCX 已有 ARS 时单规则加 0 即可 |
| LdapAttributes.dict | 目录属性翻译词典（Unicode，含所有语言）；用 CustomDict 工具生成 LdapAttributes_user.dict | 属性"改名"本质是改翻译；同名属性（Misc1）靠上下文信息字段区分 |
| Theme | Web 目录客户端图形皮肤，仅两套（8770WBM→theme1、Custom→theme2），CSS 文件构成 | 用户自选主题存 cookie；Edit 定制仅目录管理员可做 |
| MSAD | Microsoft Active Directory（本地）；8770 经 LDAP/LDAPS 用专用账号做双向属性同步 | MSAD 同步是"属性映射+同步规则"两层结构，映射只能建一条 |
| Azure AD | Microsoft Entra ID（云）；8770 作为应用经 Microsoft Graph API 拉取，Azure AD 为主节点，不 provision OXE 用户 | 与 MSAD 完全不同的认证通道（Graph API 而非 LDAPS）；tree 模式需 Directory 许可 |
| MSAD plug-in | 装在 AD 服务器上的右键插件（Alcatel-Lucent Unified User Management）：从 AD 直接开通 8770/OXE 用户，基于 Meta profile | 是"管理员手动开户"通道，与"定时同步"通道互补；更新时仅成本中心与称谓可改 |
| Meta profile | 用户应用里的开户模板：OXE 节点+空闲号码段+话机类型+OXE profile(+COS) 的组合 | 空闲号码段必须先在 OXE 建并同步；Directory number 留空则自动取段内首个空闲号 |
| Domain for management | 管理域=一组公司目录级别（DN 范围）+一组本地管理员；可嵌套，可多父域 | 域是"可见性+管理权"的切割单位，依赖 Directory+Domain Management 双许可 |
| Local administrator | 本地管理员：只能看/管自己域内的人员与目录级别；三个预定义组决定权限档 | 由中央管理员在 Security 应用建（默认全局管理员），进预定义组后降为 local |
| Delegation | 委派权：本地管理员可在自己域内再建本地管理员与目录级别（经 WBM） | 委派是"权限的分发权"，由 Users & Customization Configuration 组持有并可单开 |
| Customized view | 定制视图：预设用户开户界面显示哪些字段（预定义+自定义），按管理员账户绑定 | 目的是简化本地管理员开户流程；匿名访问与未定制用户回落默认配置 |
| Replica (Master/Consumer) | 复制副本：Master 可读写（供体），Consumer 只读（消费者，写请求经 referral 转给主） | 冗余只覆盖公司目录，不覆盖 8770 服务器本身；复制必须调度，不能实时 |
| Referral | 写重定向机制：Consumer 上的写操作自动转给 Master | 但管理上强烈建议只在 Master 改数据——Consumer 上的改动会在复制后被覆盖 |
| Replication Agreement | 复制协议：主服务器上的参数集（主副本配置/属性集/从服务器 IP:端口/复制管理器密码/初始化与调度） | 属性集（Attribute set）创建协议后不可改，要删协议重建；Initialize 会清空 Consumer 重建 |
| LDIF | LDAP 数据交换格式：8770 导入导出的通用管道；导入只增改不删除 | 配套 6 个命令行工具（8770\bin）：ConvertLdif/ExportLdap/ImportLdap/Ldif2Csv/Csv2Ldif/PurgeLdap/LinkDn |
| PurgeLdap | 按 LDAP 过滤器删除条目：补齐"LDIF 导入不删除"的另一半，常配合 misc10 标记做外部目录同步删除 | 导入与清除是一对：外部目录删了人，8770 靠 purge 机制跟删 |
| Cost Center | 成本中心：PCX 侧建（Specific Telephone Services > 1 > Cost Center），目录侧可改但必须 PCX 已存在 | 成本中心是链接间继承的主线：副链继承主链接的 CC，传真链不继承 |

### 核心命题 (用自己的话)

1. 8770 目录是一个"双存储"体系：LDAP 树给人看、MariaDB 给系统用，配置应用（o=nmc 技术目录）与目录应用（o=directoryroot 公司目录）是两棵树，靠链接（link）缝合。
2. 人机绑定的根是主链接：一对一、靠"姓名+成本中心一致"匹配；其余五类链接（多设备/副/传真/杂项/附加资源）解决多话机、非话音终端与迁移场景，各有独立基数规则。
3. 目录供给有三条通道：PCX 事件自动创建（实时、受 UID 构造与位置参数约束）、OXE 同步（Complete/Partial × Separate/Global）、LDIF 批量管道（导入只增改不删除）。
4. UID 唯一性是自动创建的第一道坎：默认"名+姓"撞同名就拒建并告警；把 UID 构造改成"名+姓+分机号"即可解，但该方法只对自动创建生效且按 PCX 分别设置。
5. 改名的入口决定后果：从目录应用改，链接全保留；从配置界面改，主链接会断并生成新人（需删除新人重建主链接修复）；从 Users/WBM 应用改，链接与成本中心全保留且名字同步更新——Users 应用是作者钦定的最佳入口。
6. 保密是"条目级"的：四级（Green/Orange/Red/Admin8770）×personal data 列表决定 Web 目录看到什么；匿名只看 Green 的非个人数据，认证本人多看自己的个人数据，Orange/Red 本人并不能看更多别人的条目。
7. 管理端权限是"账户级"的：Company Directory 五档 + Web Directory 五档访问级别，在 Security 应用中按应用分别授予——条目保密与账户权限是正交的两套机制，出问题时先分清是哪套挡住了。
8. Click to Call 的号码逻辑链：链接带出分机号 → 同步构造 ISDN 号（前缀+安装号+话机号，DDI 号优先）→ 前缀规则按属性加删前缀 → STAP 权限放行话机。SIP 话机全线出局（STAP 与 Click to Call 均不支持）。
9. MSAD 同步是"一条映射 + N 条规则"：映射只能建一条（sn 不可删、objectGUID 隐藏保唯一、电话号码只从 8770 写回 AD、uid 经改名更新）；规则定"同步哪段树、Flat 还是 Tree、何时跑"；Complete 同步必须在规则/映射新建或修改后执行。
10. Azure AD 同步与 MSAD 是平行能力：Graph API 认证、Azure AD 永远是主节点、不 provision OXE 用户；tree 模式要 Directory 许可。
11. MSAD 插件是"第三条开户通道"：AD 服务器上装插件，管理员在 AD 右键用户 → 按 Meta profile 一键开通 8770 目录用户 + OXE 用户；但更新时只有成本中心与称谓可改。
12. 规模化三件套：管理域按 LDAP 级别切可见性与管理权（本地管理员三档预定义组 + strict view 参数控制检索范围）；定制视图简化开户界面；目录复制提供最多 1 主 4 从的目录冗余（Consumer ID 固定 65535、Master ID 1-65534、LDAPS 不支持、地址簿不复复制、从机断联 >7 天数据丢失需 LDIF 人工恢复）。

### 论证链
教材以"讲义给语义模型 → How-To 给界面动作 → Notes 给行为结果 → Alarms 应用给异常证据"推进：几乎每个机制（自动创建、成本中心拒绝、链接断裂、保密过滤、同步删除标记）都设计了"制造异常 → 看告警/看结果"的验证环节，用行为闭环替代理论论证；数字口径（4 从机、5 副本、7 天、65535、500 条地址簿）以表格与字段默认值形式给出。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 R5.2 / Ed40 界面；跨版本兼容表只到 OXE Purple R101.2 (N5)、OXO Connect/OCE R6.2、OT R2.6.1——后续版本需另行核对。
- Azure AD 一章已注明"renamed Microsoft Entra ID"，但 MSAD 章的 Windows Server 支持只列到 2022；MSAD 插件实验强依赖 Internet Explorer（trusted sites、active scripting、IE9 专属设置），浏览器演进后该流程需重估。
- 复制一章明确"LDAPS is not supported"，安全基线在当年是已知短板。

### 作者的立场盲点
- 全书默认实验环境：Superuser01*/Superuser2580*/superuser 等明文密码遍布正文与配置文件示例（8770MSADPlugin.properties 里连密码字段都印在书上）；生产的密码策略、LDAPS/证书体系只有只言片语（LDAPS 需 AD CS、MSAD 端口 636）。
- 目录复制只保证"目录"冗余，8770 服务器本身无冗余方案，书中一句话带过，没有给出整套高可用建议。
- 备份/回退动作散落在各 How-To 里（导出 LDIF 备份、Themes 文件夹拷贝、Set All to Default），没有一章把"目录数据备份策略"串起来。
- WBM/Manage My Phone 等应用只在总览章点名，目录相关能力（如 WBM 改名）在后文实验中才补充，总览与实验之间存在信息差。

### 未被证明的假设
- 假设读者有 RLAB 环境与讲师给定 POD 号（所有 DDI 号、号码规则均为实验口径）。
- 假设企业 AD 现成可用且有权建 MSADadmin（domain admins 组）——生产中客户目录团队未必放行。
- 假设 OXE 侧 STAP/COS/成本中心配置可随意改（生产中涉及计费与闭锁策略）。
- 假设"先导出 LDIF 再删分支再复制"这类多步手工流程不会出错（p.conf 根名忘改的警告说明作者也知道脆）。

### 最强反对意见
"这本教材教的是 8770 目录的单机交付闭环，不是目录治理"——数据备份策略、安全加固（LDAPS 不可用下的加密替代）、ADR（Azure AD）全面替代 MSAD on-prem 的迁移路径、以及多台 8770 间的数据一致性治理都只给了机制碎片。因此每个能力的 Boundary 必须标注"实验环境口径"，并显式指向 8770 官方文档（Installation/Administration Guide）作为生产化依据；MSAD 插件章节的 IE 依赖必须在交付前置核查中标记为风险项。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] OXE 节点注册与同步（前置 SSH/信任列表检查 → 网络/子网/节点声明 → Complete-Separate 同步 → 日志与数据采集页核验）
- [x] 公司目录树搭建与 PCX 自动创建（Country/City/Department、AutomaticCreation 参数、Location 默认路径、事件接收两前提）
- [x] UID 构造调整防同名（含告警判读与回退）
- [x] 六类链接管理（副链/传真链/多设备链的建立与成本中心继承规则）
- [x] 成本中心与姓名修改的入口选择（四入口行为对比 + 配置入口改名的修复流程）
- [x] LDIF 导入导出（三范围 × 本地/服务器、调度与路径、导入恢复）
- [x] Web 目录客户端使用与配置（匿名/认证、地址簿、经理/助理链接、UID 密码管理）
- [x] 目录保密级别与访问级别矩阵配置（RH 演练的可复制流程）
- [x] Click to Call 交付（DDI 翻译器核验、STAP、前缀规则、属性关联、关联话机）
- [x] 目录词典定制（属性改名、版本号、保存三动作、回退与客户端更新）
- [x] Web 目录客户端定制（GlobalParameters、SearchClasses、Grid/Detail/Edit 属性、主题、用户参数、备份回退）
- [x] MSAD 服务器声明与同步（Access info、属性映射、同步规则、Flat/Tree、调度与删除行为）
- [x] MSAD 插件部署与 AD 侧开户（MSAD8770Admin、properties 生成、SHARING 传递、IE 前提、Meta profile）
- [x] Azure AD 同步配置（四步框架）
- [x] 管理域搭建（许可核查、功能激活、管理员账户、三预定义组、域创建、密码策略）
- [x] 委派与定制视图（Delegation 开启、WBM 建域/建视图/建本地管理员、开户对比验证）
- [x] 目录复制主从部署（Slave 先行、Master 五步、初始化与调度、移除与不一致恢复）
- [x] LDIF 命令行工具管道（go.bat/link.bat/purge.bat/export.bat 的 conf 定制范式）

### 不适合 skill 化的内容
- RLAB 平台与 SIP 模拟器细节（p41-58，教学专用基础设施，仅作 Boundary 背景）
- 培训评估/证书流程（p559-565）
- 纯截图操作步骤里与界面强耦合的点击序列（skill 化时保留菜单路径与字段语义即可）

### 预估 skill 数量
**约 10-12 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；入口软预算 8 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 注册 OmniPCX Enterprise 节点并完成同步（SSH/netadmin 前置检查、网络/子网/节点声明、同步与日志核验） | p88-98 | 可同步的 OXE 节点 | 目录一切数据的入口；节点号=网络号*100+节点号规则在此 | 生产需真实 adfexc/mtcl 凭据 |
| task-02 | 搭建公司目录树并配置 PCX 自动创建（树元素、AutomaticCreation、默认路径、事件接收前提） | p99-109 | 自动供给人员的目录树 | 目录运营的日常供给机制 | 无 |
| task-03 | 在 PCX 建用户与成本中心并验证目录自动落地 | p110-117 | 带链接的人员条目 | 与 task-02 配套 | 成本中心须先建 |
| task-04 | 配置 UID 构造解决同名拒建（含告警判读与构造回退） | p118-121 | 无同名冲突的自动创建 | 同名是真实企业常态 | 无 |
| task-05 | 验证自动继承（Cut/Paste 人员后组织属性自动更新） | p121-122 | 继承行为确认 | 组织调整高频场景 | 无 |
| task-06 | 管理六类链接（副链 CC 继承、传真链共享、多设备链经 Users 应用） | p123-137 | 正确的人机绑定关系 | 目录核心语义的落地 | 无 |
| task-07 | 从目录侧改成本中心与姓名并核验（含 PCX 拒绝未知 CC 的告警） | p137-144 | 合规的属性修改路径 | 日常 MACD 高频操作 | 无 |
| task-08 | 处理配置界面改名导致的主链接断裂（删除新人+重建主链接修复） | p144-149 | 链接修复能力 | 最易踩的坑，书专设修复流程 | 无 |
| task-09 | 从 Users/WBM 入口改名并理解其优越性 | p150-155 | 安全改名操作路径 | 作者钦定最佳入口 | 无 |
| task-10 | LDIF 导出/导入（Entry/Sublevel/Branch × 本地/服务器、调度导出、删除后导入恢复） | p156-169 | 目录数据备份与恢复能力 | 一切批量操作的基础 | 无 |
| task-11 | 使用 Web 目录客户端（匿名搜索、UID 认证、改属性/照片/地址、个人地址簿、经理/助理链接） | p183-205 | 目录自助维护能力 | 终端用户与前台场景 | 无 |
| task-12 | 配置保密级别体系（RH 部门八人、五个管理员账户、匿名/个人/管理员三级访问验证） | p217-251 | 可控可见性的目录 | HR/领导层号码保护刚需 | 无 |
| task-13 | 配置 OXE 使用 SIP 运营商（外部 SIP 网关 POD 参数、DID 翻译器、外呼验证） | p265-268 | 可外呼的实验 OXE | Click to Call 的前置 | 实验口径（模拟器） |
| task-14 | 交付 Click to Call（DDI 翻译器、Process ISDN number、STAP、前缀规则、属性关联、关联话机拨测） | p269-284 | 可从网页目录拨号的系统 | 目录变前台的核心卖点 | SIP 话机不支持（边界） |
| task-15 | 定制目录词典（CustomDict 改属性名、版本号、保存三动作、回退默认） | p295-310 | 本地化的目录字段 | 客户字段名适配 | 无 |
| task-16 | 定制 Web 目录客户端（参数/搜索过滤器/网格/详情/编辑属性、主题、用户参数、备份与回退） | p324-348 | 融入客户内网的目录门户 | 交付观感与易用性 | 无 |
| task-17 | 配置 MSAD 服务器声明（AD 侧建 MSADadmin+域管理员组、Access info 八字段、LDAPS 前提） | p368-377 | 已声明的 MSAD | AD 集成第一步 | LDAPS 需 AD CS |
| task-18 | 配置 MSAD 属性映射与同步规则（映射一条、附加属性、规则/Flat/Tree、调度、删除行为验证） | p378-393 | 双向同步的目录 | 企业身份管道主通道 | 无 |
| task-19 | 部署 MSAD 插件并从 AD 开通 OXE 用户（OXE profile/号码段/Meta profile 前置、properties 生成、安装、IE 前提、开户与更新删除） | p394-426 | AD 右键开户能力 | 帮助台友好的开户通道 | IE 依赖为风险项 |
| task-20 | 搭建管理域（许可、激活、管理员账户、三预定义组、六域创建、密码策略、可见性验证） | p456-476 | 分域管理的多组织体系 | 多站点/多租户刚需 | 需 Domain Management+Directory 许可 |
| task-21 | 配置委派与定制视图（Delegation、WBM 建级别/域/视图/本地管理员、开户效率对比） | p477-500 | 可下放的开户体系 | 大组织运营减负 | 无 |
| task-22 | 部署目录复制主从（前提核查、Slave 建副本、Master 五步、初始化调度 5:00AM、移除与不一致恢复） | p517-535 | 目录冗余 | 数据可用性保障 | LDAPS 不支持、地址簿不复复制 |
| task-23 | 使用 LDIF 管理工具管道（go.bat 三命令、link.bat 建助理/经理链、purge.bat 同步删除、export.bat、domino 管道） | p552-558 | 批量数据工程能力 | 外部目录对接的万能管道 | p.conf 根名为高危点 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-01 OXE 注册与同步（目录数据的地基，节点号规则是全书公用前提）
2. task-02/03/04 树+自动创建+UID 构造（目录供给主通道）
3. task-06/07/08/09 链接与改名语义（最核心的领域模型 + 最易踩坑点）
4. task-18 MSAD 同步（企业客户最普遍诉求）
5. task-14 Click to Call（目录的业务价值出口）
6. task-12 保密级别（安全合规刚需）
7. task-22 目录复制（可用性方案，数字口径密集）
8. task-20/21 管理域与委派（多组织运营）
9. task-19 MSAD 插件（开户便利但有 IE 风险）
10. task-10/15/16/11/13/17/23（支撑类与定制类任务）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 12 个一级部分（3 概念地基 + 接入闭环 2 + 使用层 3 + 定制 1 + 数据管道 1 + 运营 1 + 背景 2，收尾附注未计入）
- [x] 术语按实际内容列出（31 个）
- [x] 已检查作者局限/假设（实验环境口径、明文密码、IE 依赖、LDAPS 缺位、备份策略缺位、复制不覆盖服务器）
- [x] 原书关键任务 23 项，全部有来源页码、交付物与重要性依据
- [x] 工作区此前无产出，本文件与 candidates/ 五文件均为本次全量新建

**用户确认时间**: 2026-09-23（流水线任务授权，全流程连续执行）
