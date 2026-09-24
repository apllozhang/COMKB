# 流量分析与 Tracking 告警（pmm 计数器、双阈值、PtpType、Tracking 档案与变化率）

## R — 原文依据

> "Files name: C<week nb><day><half-hour nb><seq nb>. type • Week number: 00..51 ... Half-hour number: 00..47 • XX: used for .inf and daily .pmm files"（p433）
> "Replace -PtpType ATT,ATG,TRG –PTP by -PtpType ALL -PTP"（p446）
> "Variation rate = 100 * ( current value of the data – average of the x last values of the data) / average of the x last values of the data — X is called moving average period • Day (x = 30 days by default)"（p462）
> "If you want to force assignment to all entities, select the corresponding Reset Profile option The Default Tracking box of each entity is then forced to YES"（p478）

出处：8770XTE201EN p429-488。

## I — 自述

流量分析（仅 OXE）与 Tracking 是话务计数器监控的两段：前者把计数器变成报表，后者把阈值变成告警。

- 流量分析观察六类对象：中继组、话务台、话务台组、DECT/PWT、终端、被叫分机；数据两源——OXE 半小时计数器文件（/usr4/pmm，命名 C<周><日><半小时><序号>，日文件与 .inf 用 XX 占位，pmm.lis 作索引）与计费记录（供被叫号与终端观察）；回收与计费同管道
- 两组等待阈值互不相干：话务台阈值 1/2（出厂 30s/60s，实验设 5s/10s）只能在 OXE 配置改；8770 侧 Loading > Traffic analysis 的订户阈值 T1/T2（默认 30s/60s，实验设 10s/20s）只喂报表字段；DECT 基站忙触发 RBS 默认 8、IBS 默认 4；计数器保留 10-1488 个半小时（1488=31 天）
- PtpType 出厂差距：Daily/Weekly Job 里计数器任务默认 -PtpType ATT,ATG,TRP 只算话务台/话务台组/中继组；要看被叫号与终端必须把两个任务都改成 -PtpType ALL（顺带授权加载来话记录）
- Tracking=阈值集合档案：每条含 Tracking value（会计/话务/VoIP/性能四域指标）+Period+Threshold+Call Type+Action（告警/邮件/两者）；按实体类型挂默认档案（Default Tracking 管理器）或单条目指定；运营商条目也可挂
- 变化率公式：100×(当前值−前 x 期均值)÷前 x 期均值；移动平均默认期日 30 天/月 3 月/年 1 年，在 MonitoringParameters 改；Max number of alarms 默认 50
- 超限检测由任务与夜间计数器驱动，非实时流；一封告警邮件可含多个超限、附件按 profile 分类

## A1 — 书中案例

**流量分析配置**（p442-454）：

1. 确认外部计费开启（来话记录是被叫号/终端计数器的前提）
2. OXE 配置 Applications > Traffic Observation 设话务台阈值 5s/10s（出厂 30s/60s）
3. 计数器保留期 Number half-hour Period Kept 取 10-1488（实验按 31 天口径）
4. 8770 Loading > Traffic analysis 设订户阈值 T1/T2 与 Busy Threshold
5. Scheduler 里 Daily Job 与 Weekly Job 两处任务把 -PtpType ATT,ATG,TRG 改为 ALL
6. 需要立即出数时手工 Total calculation，生成中继组/话务台预定义报告

**Tracking 三档案**（p469-488）：

1. Profile 1：月呼出次数 >30 告警、>50 邮件（地址实验口径 alban.podX@company.com）
2. Profile 2：日呼出时长 >45 分钟告警、>1 小时邮件
3. Profile 3：出入呼日时长变化率 >100% 告警+邮件——配合 MonitoringParameters 把 Daily moving average period 改 2（默认 30）
4. Default Tracking 管理器按实体类型挂默认档案；单条目（如 Brest 挂 Profile 1、Colombes 挂 Profile 2）先取消 Default Tracking 再选
5. 要全量强制时点 Reset Profile（该类型全部实体的 Default Tracking 置回 YES）
6. 等任务检测超限后验证告警与邮件（一封邮件可含多个超限）

## A2 — 未来触发

使用情境：中继要不要扩容；话务台接听超时考核；被叫号话务报表是空的；某分机话费异常想自动告警；话务量突增检测；告警邮件怎么配。

语言信号：流量分析 / traffic analysis / pmm / pmm.lis / 半小时计数器 / 中继组 / 话务台 / T1 / T2 / 阈值 / PtpType / ALL / Tracking / 跟踪 / 档案 / 变化率 / 移动平均 / moving average / Reset Profile / Max number of alarms / 告警 / 邮件。

与相邻能力区分：IP 话音质量 → VoIP 性能能力；WBM 实时仪表盘 → Web Performance 能力；告警邮件服务器参数与报表共用（报表能力卡的邮件配置）。

## E — 可执行步骤

输入契约：OXE 为监控对象（流量分析不支持 OXO/OpenTouch）、票据管道已通。要监控 OXO → 判停声明平台边界，转 VoIP 报告方案。

1. OXE 设话务台阈值与计数器保留期。完成标准：观察参数落盘
2. 8770 Loading > Traffic analysis 设 T1/T2 与对象勾选。完成标准：报表口径确认
3. Scheduler 两处任务改 -PtpType ALL。完成标准：被叫号/终端计数器可算
4. 手工 Total calculation 或等夜间任务后出预定义报告。完成标准：中继/话务台报表有数
5. 建 Tracking 档案（阈值+动作），按实体类型挂默认或单条目指定。完成标准：覆盖面清单成文
6. 变化率类跟踪值先在 MonitoringParameters 定移动平均期。完成标准：期数与业务预期一致
7. 触发或模拟超限，验证告警与邮件。完成标准：动作生效

判停点：

- 被叫号/终端报表为空 → 查两个 Job 是否都改了 PtpType ALL（出厂默认不含）
- 以为"配了类型=全员生效" → 默认档案只作用于勾了 Default Tracking 的实体，全量强制用 Reset Profile
- 期待实时告警 → 检测由任务与夜间计数器驱动，时延预期要按任务周期谈
- 邮件不达 → 查邮件服务器参数（server:port 无空格、发件人被认识），与报表共用一套配置

输出契约：观察对象与阈值表 + PtpType 变更记录 + Tracking 档案清单（阈值/动作/覆盖面）+ 告警验证记录。

## B — 边界

- 流量分析仅支持 OmniPCX Enterprise（p25/p29/p431）；OXO 站点无此能力
- 话务台阈值（OXE 侧）与 8770 的 T1/T2 无联动，改前者不影响报表口径（p443/p445）
- 变化率只在选定周期的跟踪值上生效（Cost/Duration/Number of calls variation 类）；移动平均期改动影响全部变化率档案
- "一封邮件多个超限、附件按 profile 分类"依赖邮件服务器参数正确（p484；实验用 Thunderbird 收信为教学设施）
- 生产容量结论（中继扩容判据）需结合业务话务模型，书内只提供计数器与报表机制
