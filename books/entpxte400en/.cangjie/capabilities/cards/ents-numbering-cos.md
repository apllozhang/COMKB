# 编号计划与 COS 管理（前缀/后缀、Phone Features COS、Connection/Transfer 矩阵）

## R — 原文依据

> "A prefix corresponds to a unique phone feature • 8 digits maximum (0 to 9, A, B, C, D, #, *)"（p370）
> "31T -> 'Set features/Password modification' prefix • 31000 -> Mr Brad Barkley directory n° … By default, timer 23= 30 (so 30 * 100 mS = 3 seconds)"（p370）
> "Assigned to users 256 categories are available • User rights • Set features • General services • PCX services • External services • Suffixes • Speed dialing areas • Miscellaneous parameters"（p390）

出处：ENTPXTE400EN p366-424。

## I — 自述

编号计划是全系统路由的地基，COS 是权限的开关面：

1. **前缀规则**：每个前缀唯一对应一个功能，≤8 位（0-9ABCD*#）；用于摘机后（拨号音/指南/多功能键）；后缀用于通话中（3=转会议、5=遇忙回叫）
2. **饱和对策**：后缀 T+Timer 23（默认 30×100ms=3 秒）区分功能前缀与用户号（如 31T 改密前缀 vs 31000 分机）
3. **规划建议**：对用户简单、留扩展余量、按用途分段（话务台/外线前缀/用户/缩位/功能/系统/紧急各留段）；多站点示例=站点<20 且每站<1000 用户时首 2 位站号+末 3 位 DDI 尾号
4. **Phone Features COS（256 类）**：取值 1=允许/0=禁止，七分区（Rights 防直代接/防强插等、Set features 呼转/锁机/DND、General services 代接、PCX services 叫醒、External services 账户码、Suffixes 会议/强插、缩位区）+Miscellaneous（摘机路由五模式、默认溢出、留言转接）
5. **Connection/Transfer COS**：三方矩阵（分机/中继两两连转控制）；用户侧两者同 ID 但两张独立矩阵
6. **缩位拨号**：≤400 区/每实体 ≤32 段，COS 控制可用性
7. **维护**：WBM Translator/Prefix Plan、Suffix Plan；CLI ednump -l GEA、listrad

## A1 — 书中案例

**前缀巡检实验**（p382-388，How-To）：

1. WBM Translator/Prefix Plan 用过滤器定位功能前缀
2. 过滤 Prefix Meaning=Set features 且 Station features=Immediate forward，得 FR 库的 51
3. 同法核对取消呼转 41、DND 42、留言 43、叫醒 506
4. CLI ednump -l GEA 全量核对默认前缀表（88 行）
5. listrad 列出全部翻译器条目复核
6. 结论：改前缀须同步核对语音指南播报（p431 Caution）

**COS 行为验证实验**（p400-424，How-To）：

1. 三个用户同挂 COS#0，验证强插保护默认开启
2. 建 COS#11 放开保护，给测试用户挂接后强插成功
3. COS#0 关闭 Immediate forward 后拨 51 被拒（Feature Forbidden）
4. 摘机路由实验：COS 挂 Routing table，摘机直达指定号码
5. 默认溢出实验：COS2 配无应答转关联话机，Timer 4（15 秒）后溢出
6. Connection/Transfer 矩阵实验：奇偶分组互拨与转接行为随矩阵 0/1 变化

## A2 — 未来触发

使用情境：设计或调整拨号计划；拨功能码被拒（Feature Forbidden）；31 打头拨号等 3 秒；限制用户间互拨或转接；强插/代接权限；缩位拨号规划。

语言信号：编号计划 / numbering / 前缀 / prefix / 后缀 / suffix / Timer 23 / COS / 类别服务 / 呼转前缀 / 摘机路由 / Connection COS / Transfer COS / 矩阵 / 缩位 / speed dialing。

与相邻能力区分：外呼区域限制是另一套 Public COS → 闭锁与紧急能力（路由卡）；功能码播报内容 → 呼叫处理能力（语音指南）。

## E — 可执行步骤

输入契约：客户拨号习惯与部门结构、存量前缀清单、权限矩阵需求。计划改动先出对照表评审，不要直接改生产库。

1. 盘点存量：ednump -l GEA 与 listrad 导出当前前缀/后缀全表。完成标准：存量清单成文
2. 设计分段：按用途预留段（话务/外线/用户/缩位/功能/系统/紧急），标注歧义点配 Timer 23。完成标准：计划表评审通过
3. 实施：WBM Translator 建改前缀/后缀（Set features 类需选具体功能参数）。完成标准：拨测功能码生效
4. COS 分域：功能/保护类需求挂 Phone Features COS；连转控制配 Connection/Transfer 矩阵。完成标准：行为验证与需求一致
5. 指南联动：改计划后核对静态指南播报号码并同步换指南文件（n22）。完成标准：指南与计划一致
6. 记录：前缀-功能对照表与 COS 分配台账归档。完成标准：交接单齐全

判停点：

- 拨 31 停顿 3 秒才响 → Timer 23 歧义消解在起作用（p370），属机制非故障；缩短需权衡功能前缀扩展性
- 功能码拨了报 Feature Forbidden → 查用户 Phone Features COS 对应位（1/0），不是编号计划问题
- 改了前缀后用户按指南操作失败 → 指南播报旧号码（n22），先换指南再答复用户
- 连转矩阵改完不生效 → 确认改的是 Connection 还是 Transfer 矩阵（同 ID 两张表），并核对用户挂接的 COS ID

输出契约：评审通过的编号计划 + COS 分配矩阵 + 指南一致性核对记录。

## B — 边界

- FR 库默认前缀（51/41/42/43/405/506 等 88 行）为实验口径的国家码实例值；空库国家码决定默认集（nr-04）
- 摘机路由表 Routing No 取值 1-255；External Alarm/Delay 等模式的深度场景书内仅给口径
- ACD/呼叫中心级队列不属于 COS 域（话务台/CDT 在呼叫处理能力）
- 客户权限矩阵与合规策略是业务输入，书内只给机制与默认值
