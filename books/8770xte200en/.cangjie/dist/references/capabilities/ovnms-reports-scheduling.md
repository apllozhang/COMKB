# OmniVista 8770 报表与任务编排（Reports / Scheduler / 自动维护）

## R — 原文依据

> "Maximum number of lines in TXT format 4000 ... Maximum number of lines in database 100000"（p444）
> "The number of the SMTP port is optional if the default SMTP port number is used ... Careful: no space between ':' and the TCP port number."（p452）
> "When you add another Job, this one is called jobset. ... if you refresh this one, you will see that jobset becomes Job."（p487）
> "In case of deletion or modification of the predefined maintenance jobs, it is possible to restore the default configuration by a LDIF import."（p502）

出处：8770XTE200EN p443-502（Reports、Scheduler、Automatic maintenance）。

## I — 自述

三件事：把报表生成分发出去、把任务编排成链、让数据库自己瘦身后备恢复兜底。

**Reports 报表**

- 大小限制默认值（Preferences > Reports > Reports Preference）：TXT 4000 行、HTML/PDF/EXCEL 各 50 页、图表 X 轴 100 元素、数据库取数 100000 行——超限报告尾部提示截断
- 流程：预定义报告复制到个人文件夹 > Generate Report（Immediate，附加过滤常用 Notification time=This year）> Open to View
- 导出：File（TXT/HTML/PDF/EXCEL，默认名=定义名+生成日期）或 E-MAIL（多地址逗号分隔；依赖 Administration > Export parameters 配 Mail server，SMTP 非默认端口必须显式写且冒号后无空格）
- 计划：右键报告定义 > Schedule > 过滤向导 > Task Type=Simple job > Scheduling 页定 Start Date=As Scheduled、Repeat、Exclude Days

**Scheduler 任务编排**

- 模型：Task=可执行操作（内部操作或外部应用）；Job=同时执行的任务集合（Idle/Waiting/Running）；Simple job=单任务；Synchronized task=挂入已有 job 形成序列；新建子 job 临时叫 jobset，刷新后变 Job
- 预定义 job：Daily Job / Weekly Job / 8770 Data Backup / RTU Scheduled Reports 承担日常维护
- 组装两法：从报告应用 Schedule 时选 Simple job 或 Synchronized task；或在 Scheduler 建新 job 后从其他 job 复制/剪切任务粘贴（Cut+Paste 改变归属实现先后顺序）
- 参数语义：Maximum start delay=错过后允许的最大补跑延迟（超时放弃，如周六任务延迟 1 天、周五关机周一开机则不跑）；Stop on error 默认启用；Retry（次数/间隔/最大时长）；Exclude Days 排除日期
- 执行核验：Execute now 后 Reports 图标查各任务成功态

**自动维护（五类清除 + Purge job + 恢复）**

- 五类清除入口：计费/话务（Accounting preferences，如小时级话务保留 4 天、计费记录 15 天）、报告（Clean taxa Reports=2 天）、告警（Purge configuration，按天数+条数双闸，实验保留 100 告警/100 事件）、审计（Audit purge，日志天数+导出寿命）、文件夹（NmcArchive，磁盘/目录双阈值告警+清理延迟+Keep one backup）
- Purge job 组装：Scheduler 建 job "Purge"，从 Weekly Job 依次复制 Purge Alarms > 新子 job 粘 Clean PTP/Traff Hist > 再嵌 Clean accounting，Enable 后形成告警清除 > 话务清除 > 计费清除的串行链
- 误删/改坏预定义 job 的恢复：Administration 应用 Import LDIF（\8770\data\scheduler 下 DailyJob.ldif 或 WeeklyJob.ldif）> 重启 NMC Scheduler 服务

## A1 — 书中案例

**报表实验**（p443-459）：

1. 核对偏好默认上限（TXT 4000 行/50 页/100000 行）
2. 建个人文件夹 My Alarms reports，复制 OmniVista 8770 alarm detailed report
3. 生成两实例（全部记录 vs This Week+Severity 过滤）并 Open to View
4. 文件导出 PDF 与邮件导出 HTML，Thunderbird 收件核对
5. 计划生成：每日 5:00、Exclude Days 勾周六周日，Execute Now 核验

**任务编排实验**（p469-487）：

1. 审计报告挂 Simple job（每日 5:00 排除周日）
2. 建同步 job "My audit synchronization"（4:00），复制 Load/Fetch audit records 粘入
3. 报告任务以 Synchronized task 挂入该 job
4. 复制 Partial synchronization LDAP 任务并用 jobset 剪切重排，形成审计同步 > 审计报告 > LDAP 部分同步顺序链

**自动维护实验**（p488-502）：五类参数逐一配置后组装 Purge job 三级链并 Enable；LDIF 导入恢复预定义 job 成功。

## A2 — 未来触发

使用情境：运营报表定期分发给管理层；把审计同步和报告串成自动链；数据库膨胀治理；误删预定义任务抢救。

语言信号：Reports / 报告上限 / 截断 / Export E-MAIL / SMTP 端口 / Schedule / Simple job / Synchronized task / jobset / Maximum start delay / Exclude Days / Purge / Clean PTP / LDIF / WeeklyJob.ldif。

与相邻能力区分：审计报告的数据来源（审计合规卡）；8770 Data Backup 预定义 job 的恢复语义（备份恢复卡）；本能力管报表生成、任务编排与数据清理。

## E — 可执行步骤

输入契约：报表需求清单（内容/频率/收件人）、保留期合规要求、维护窗口口径。

1. 报表定义：复制预定义到个人文件夹并试生成一次。完成标准：实例生成且无截断提示（有则调上限或分批）
2. 分发：配 Mail server 后挂文件/邮件导出。完成标准：PDF 落盘、邮件到达
3. 计划：Simple job + As Scheduled + Exclude Days。完成标准：Execute Now 成功、Scheduler 绿态
4. 编排链：同步任务与报告任务按依赖排序（必要时 jobset 剪切重排）。完成标准：刷新后顺序链按序执行
5. 清理参数：五类入口按合规保留期配置。完成标准：各保留值有据可查
6. Purge job：三级链组装并 Enable，Execute Now 验证。完成标准：数据按条件被清
7. 兜底：演练一次 LDIF 导入恢复预定义 job。完成标准：Daily/Weekly Job 恢复可见

判停点：

- 报告被截断 → 先查数据量与上限差值，调参或分批，不要默认"报告全量"
- 错过补跑争议 → 按 Maximum start delay 语义解释并给足延迟或改人工巡检
- 预定义 job 缺失且无 LDIF → 判停升级，不要手工重建冒充预定义

输出契约：报表分发清单 + 任务链拓扑与参数表 + 保留期配置表 + LDIF 恢复演练记录。

## B — 边界

- 话务分析（Traffic Analysis）仅支持 OXE，OXO 站点不可用（应用 Limits 原文）
- 计费/话务域深度应用（Account./Traf./VoIP 的 20 余项清理参数）本书只给默认值表，未逐项教学
- RTU Scheduled Reports 属运营商计费场景，本书仅列名
- 清理执行由 Daily/Weekly Job 按"删除条件在应用中配置"承担（p468）；保留期务必按客户合规确定
- 实验收件人/邮件服务器为实验口径，见 book/overview
