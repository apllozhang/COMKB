# 计费归档与恢复（archZ 生命周期、参数书写规则、恢复标签、定向清除）

## R — 原文依据

> "File extension = archZ (Zipped archive format) • One file per day and per node (if at least 1 record to archive)"（p521）
> "Archive Delay — Defined in days (default value: 31) – Don't add the symbol D after the value. ... Clean-up delay — Defined in days (default value: 94D) – The symbol D must be added after the value."（p529）
> "Loaded records: Without label (visible in the organization). Archived records: with label (the restored records are not visible in the organization)."（p537）
> "Only restored records ... This option only deletes records restored with the label Archived records."（p548）

出处：8770XTE201EN p518-548。

## I — 自述

归档是计费数据生命周期的延长线，四个目标：缩库提速、投诉期追溯旧票、旧票重算成本、长期备份。

- 机制：归档任务（手动或自动）把"上次归档日"到"当前日期−31 天"的票据拷入 archZ（zip，每天每节点一档，默认路径 C:\8770_ARC\Accounting\tickets）；档案再保留 94 天后删除——31+94=最长 125 天
- 清理时机按记录的业务日期而非归档文件创建日期：补归档的旧票也按原日期到期
- 参数书写规则相反（同一页签）：Archive Delay=31 天数、禁止带 D 后缀；Clean-up delay=94D、必须带 D 后缀——照抄格式会配错
- 恢复按单日（选 archZ 文件）或按周期（日期区间+勾节点）两种入口；恢复标签二选一：

| 标签 | 行为 | 适用 |
|---|---|---|
| Loaded records | 无标签、进组织树、与原始票完全不可区分 | 纯业务补查 |
| Archived records | 带标签、组织树 Records 页签不显示、报告可见（Record origin 列可过滤）、可被 "Only restored records" 单独清除 | 审计/对账场景 |

- 恢复成本二选一：Without recalculation（沿用归档时的运营商成本）或 With recalculation（恢复时重算，运营商有效期必须覆盖被恢复记录的日期）

## A1 — 书中案例

**归档、恢复与清除闭环**（p528-548）：

1. Administration > nmc > OmniVista 8770 > nms > NmcArchive > Accounting 的 Accounting archive 页签配参数（归档路径、Archive Delay、Clean-up delay、勾 Archive activation；实验演示把 Archive delay 设 1 天、Clean-up delay 3 年）
2. 执行归档任务：范围=1 月 1 日到 2 月 1 日的票据入 archZ
3. 对同周期执行 Purging 清掉库内票据
4. 恢复单日（1 月 28 日）选标签 Loaded records——记录回组织树且与原始票无法区分
5. 恢复周期（1 月 29 日到 2 月 1 日）选标签 Archived records——组织树 Records 页签不显示，报告可见
6. 用表头 Record origin 过滤验证两种来源（Loaded record / Restored record）
7. 只清恢复票：Accounting/traffic > Purging 勾 Only restored records——仅删除 Archived 标签的恢复票

## A2 — 未来触发

使用情境：库太大报表变慢想缩库；客户投诉半年前的话费要查旧票；归档文件什么时候删；恢复的票和原始票分不清；恢复的票怎么单独清掉；留存期限合规。

语言信号：归档 / archive / archZ / Archive Delay / Clean-up delay / 125 天 / 31 天 / 94 天 / 恢复 / restore / Loaded records / Archived records / Record origin / Only restored records / purge / 清除 / 留存。

与相邻能力区分：恢复后重算成本依赖运营商有效期（资费建模能力）；组织树更新与灰条目清理属组织成本归属能力；库容量与备份策略在书外。

## E — 可执行步骤

输入契约：归档路径磁盘充足；留存期限有合规或业务口径。口径未定 → 判停先确认期限（125 天是机制上限不是合规结论）。

1. 配归档参数：路径、Archive Delay（纯数字）、Clean-up delay（数字+D）、勾 Archive activation。完成标准：两组参数格式各自正确
2. 执行或排程归档任务。完成标准：C:\8770_ARC\Accounting\tickets 出现 archZ
3. 需缩库时对同周期 Purging。完成标准：库内记录数下降
4. 按场景恢复：业务补查用 Loaded records，审计对账用 Archived records。完成标准：标签选择有依据
5. With recalculation 恢复前核对运营商有效期覆盖被恢复日期。完成标准：恢复票成本非空
6. 用 Record origin 列过滤核验恢复票，必要时 Only restored records 定向清除。完成标准：清除只影响恢复票

判停点：

- 两个天数参数书写格式 → Archive Delay 禁带 D、Clean-up delay 必带 D，写反会配错
- 审计要求"能区分原始与恢复票" → 一律用 Archived 标签；Loaded 标签恢复后无法区分
- 恢复选了 With recalculation 但成本算不出 → 运营商有效期未覆盖记录日期，先补周期再恢复
- 客户要求留存超 125 天 → 机制上限之外属外部备份方案（书外），本卡不承诺

输出契约：归档参数表 + 归档/恢复/清除操作记录 + Record origin 核验结论 + 留存期限口径说明。

## B — 边界

- 31+94=125 天是 Ed45 机制口径；法定留存期限（GDPR 类）需按当地法规另定，书内不论（n45）
- 清理按记录日期计算——补归档不改变到期时点（p529/p530）
- 恢复的 Archived 标签票在组织树不可见但可出报告；组织树可见性规则与机密控制能力独立
- 归档参数双入口（NmcArchive 与计费应用 Preferences）指向同一套配置，改一处即可
- MariaDB 容量规划与备份恢复演练在书外（n45）；本卡只覆盖计费票据的数据生命周期
