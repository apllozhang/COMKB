# VAA 统计与报告（四指标报表、呼叫日志逐节点排障、邮件周报）

## R — 原文依据

> "The number of calls received • The number of treated calls • The calls released by the caller • The calls lost due to insufficient VAA license port … A pie chart: Number of calls transferred, number of 'released by vaa', number of 'released by caller', number of 'insufficient licenses'"（p314）
> "if the administrator selects 'Monday', he will receive the Tuesday at the time defined, the report of the previous day, i.e. Monday."（p317）
> "In the /etc/ale/vaa.conf file, two options must be set at true: • 'autogenerateTenantActivityReport'. default value Is true. … 'autogenerate ExcelTenantReport'. By default, this option is set at true."（p317）
> "It is IMPERATIVE to personalize the NAME of each block when configuring a tree! This name is used by statistics"（p145）

出处：VSAAXTE001EN p279-281, p312-317。

## I — 自述

统计体系四层，既是运营报表也是排障工具：

1. **报表四指标**：收到呼叫数、已处理数、主叫挂断数、许可端口不足丢失数；辅以两图——端口占用（正在处理的呼叫数/已占端口数）与饼图（转出/VAA 挂断/主叫挂断/许可不足）；全局统计在主菜单，按公司统计需先选中公司
2. **呼叫日志（排障利器）**：Call Logs 逐呼叫明细，点开可见该呼叫经过的节点及各节点时长——树节点命名直接决定日志可读性；CSV 导出字段含 id/主叫/租户/树/时长/结束原因/相关数据输入输出/转接目的地等
3. **租户活动邮件报告**：xlsx 发给管理员，覆盖服务器上全部租户（处理呼叫数与逐小时来话图）

   - 开启条件——/etc/ale/vaa.conf 两个开关（autogenerateTenantActivityReport 与 autogenerateExcelTenantReport，默认 true）+ 管理员须有 "received activity reports" 权限 + 有效邮箱；可定发送时间与星期
4. **日期偏移口径**：星期参数语义是"次日报前一天"——选 Monday 即周二收到周一（前一天）的报告；与客户对验收口径时必须说清

统计前提链：节点命名纪律（树设计阶段）→ 呼叫日志可读 → 报表可解释；HA 故障期间 slave 处理的呼叫无统计（缺口属设计行为）。

## A1 — 书中案例

**周报开启与逐节点诊断**（p312-317 讲义 + p280 字段表，无实验章）：

1. 核对 /etc/ale/vaa.conf 两个报告开关为 true（默认即是）
2. 管理员账号勾选 "received activity reports" 权限并确认邮箱有效
3. 设定发送时间与星期（记住次日报前一天的偏移）
4. 周期核对收件箱中的 xlsx 报告（处理呼叫数 + 逐小时来话图）
5. 排障场景：取 Call Logs 中目标呼叫明细
6. 点开单呼叫查看经过节点与各节点时长
7. 结合 CSV 导出做离线分析（字段含时长/结束原因/转接目的地等）
8. 输出结论：哪个节点停留异常、结束原因分布是否异常

## A2 — 未来触发

使用情境：客户要话务周报；报表数字对不上；投诉"IVR 卡"要定位节点；许可不足丢话取证；统计缺了一段数据；验收要逐节点时长证据。

语言信号：统计 / statistics / 报表 / report / 呼叫日志 / call logs / CSV / 周报 / xlsx / autogenerateTenantActivityReport / 逐节点时长 / 许可不足 / insufficient / released by caller / 节点命名。

与相邻能力区分：节点命名纪律的源头归树设计能力；日志五类与文件路径归维护能力；故障期间无统计的 HA 行为归 HA 能力。

## E — 可执行步骤

输入契约：管理员账号（含报表接收权限与邮箱）、vaa.conf 访问权限（SSH）、树节点命名已合规、客户报表口径（要哪天/哪个时段的数据）。

1. 开周报：核对双开关默认 true，配管理员权限与邮箱、定发送日与时点。完成标准：首封 xlsx 按期到达
2. 口径对齐：向客户说明星期偏移（选周一收周一数据）；要周一上班看上周五需另行安排。完成标准：验收口径书面一致
3. 日常读表：四指标 + 饼图 + 端口占用逐月对照；许可不足项持续非零则评估扩容。完成标准：异常项有结论
4. 逐节点排障：按投诉时段取 Call Logs，点开样本呼叫看各节点时长。完成标准：定位到具体节点
5. CSV 取证：导出目标时段呼叫日志做分布分析（结束原因/时长）。完成标准：证据文件归档
6. 缺口解释：报表若缺故障时段数据，对照 HA 行为口径答复（slave 只读无统计）并推动 resync。完成标准：客户认可口径

判停点：

- 客户把"缺故障时段数据"当丢数据故障 → 停，按 HA 设计行为解释（nr-07 推断标注），不要承诺补录
- 节点全是默认名导致日志读不出语义 → 停，源头在树设计命名纪律，本卡只能给出整改建议
- 要实时监控（SNMP trap 集成） → 停，属告警监控域（维护能力），SNMP 默认关需手动启用
- 周报没收到 → 停，按序查双开关/权限/邮箱/SMTP 配置与重启状态

输出契约：周报开启确认 + 报表解读结论 + 逐节点诊断报告与 CSV 证据。

## B — 边界

- 统计依赖节点命名纪律（p145 三处强调）；默认名节点的日志无排障价值（n21）
- slave 故障期间无统计是设计行为，resync 不回补历史统计（n45，答复口径为实践引申）
- 邮件周报的星期偏移易被误读为"周一收当周报"（n44）
- 报告覆盖服务器上全部租户，无法按租户拆分投递（口径源自 p317 描述）
- p295 之外本域无实验章，A1 为讲义级流程（原书结构如此）
- CSV 字段名以 p280 表为准，跨版本可能有增删，引用时以现场版本实测
