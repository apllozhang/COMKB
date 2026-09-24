# 报表定制（Querytool 选数、Designer 排版、嵌套汇总、图表、Hit-list 与五练习模式）

## R — 原文依据

> "Detailed: The detailed report does not summarize data ... if a set has dialed the same number twenty-five times, the detailed report lists the set twenty-five times ... Grouped: ... the grouped report lists it only once"（p385）
> "The view defines the report area used to generate a graph or a formula. ... It is impossible to use headers from different areas to generate a graph or a formula."（p396）
> "Hit-list Report — Limits the number of lines in the report. This parameter is used with grouped report definition."（p393）
> "the use of the total cost per called region is necessary ... So the only possibility it's to mask it on the report — On Foreground field, select the blank color"（p617）

出处：8770XTE201EN p384-404, p549-643。

## I — 自述

报表定义四步向导：Source（Accounting records 或 Total counters——后者生成显著更快）> Item（计数器源才选对象）> Type（Detailed/Grouped）> Template（默认 Template/Compact template，不可删默认两件）。

- Querytool 页签管数据：上层可用库字段（§=报表内换行符）双击加入下层；字段可加多次配不同过滤；属性含 Field label 改名、grouped 专有 Operation（Group by/Count/Min/Max/Total/Average；detailed 留空）、表达式编辑器公式（如 $cost=€cost×汇率）、Sort、Filter（含 Generation Time Filter 生成期再选、Display=Not present/Detail/Group Header）、Hit-list（grouped 专用限量）
- Designer 页签管版面：区域分 Report/Page Header-Footer、Group Header/Footer、Detail；字段属性含前后缀、小数位、字体颜色；工具条可插文本/库字段/公式/图片/图表/日期/页码
- 三条版面硬规则：

| 规则 | 内容 | 应用 |
|---|---|---|
| 同视图区域 | 图表与公式只能取同一视图区域的表头 | "成本中心合计=分机合计之和"须在 Cost Center 区把 View 切到 Extension |
| 中间层遮蔽 | 中间合计不想显示，唯一办法是前景色设空白 | 运营商总计必须经过被叫区小计（载体），再前景空白隐藏 |
| 空表头消除 | grouped 报表末页多余 Detail 表头靠共有字段做组头顶掉 | 加 Country 字段作 Group Header 再前景空白遮蔽 |

- 五个练习模式（task-18 题面）：#1 详细+过滤+汇率公式+生成期过滤器；#2 详细+组头排序+Sum 合计+条形图；#3 详细+成本中心到分机嵌套汇总+PSTN 过滤；#4 grouped 双运营商汇总+中间层遮蔽+饼图；#5 grouped Hit-list 前 3+饼图+空表头消除

## A1 — 书中案例

**report #1 实现**（p549-562）：

1. 建定义：Record > Detailed > Compact Template，名 Customized report #1
2. Querytool 选字段：Extension、Called Number、Duration、Date/Hour、成本（两次）
3. Duration 过滤 greater than 00:00:00（只显时长大于 0 的呼出）
4. 第二列成本开表达式编辑器：$cost=€cost×1.3（实现章口径），改名 Cost w/o Tax Dollar
5. Extension 勾 Generation Time Filter（生成期再选分机）
6. Designer：横版纸、拉宽列、Maximum Reduction 收紧行距
7. 两列成本小数位=4、后缀 € 与 $
8. 生成并查看：呼出、时长过滤、双币种列、生成期过滤全部生效

**report #4 的两个技巧**（p606-626）：

1. Type 选 Grouped；No. of calls/Duration/Cost 三列 Operation=Sum
2. Direct Carrier 过滤用 Filter Editor 选 Telecom 1 与 Telecom 2 两条（题面 "Telecom 7/0" 为原文残留，见 needs-review nr-02）
3. Called Region 组头先做 Sum(Direct Carrier Cost) 作中间层载体
4. 中间层字段 Foreground 选空白色遮蔽（信息参与上层计算但不显示）
5. Direct Carrier 组头把 View 切到 Called Region 后引用 Sum(Sum(Direct Carrier Cost)) 得运营商总计
6. Report Footer 插饼图：View=Direct Carrier、Y=运营商总成本

## A2 — 未来触发

使用情境：客户要"按分机汇总再按成本中心汇总"的账单；报表要双币种列；前 10 名话务排行；图表怎么加；为什么公式引用不了别的区域的字段；汇总报表末页多一块空表头。

语言信号：Querytool / Designer / 报表定义 / Detailed / Grouped / Operation / Sum / Hit-list / Generation Time Filter / 表达式 / 公式 / 前缀 / 小数位 / 条形图 / 饼图 / View / 前景色 / report #1 / 嵌套汇总。

与相邻能力区分：跑现成定义、导出分发 → 报表能力；数据被遮与解密 → 机密控制能力。

## E — 可执行步骤

输入契约：报表能力已跑通（库内有票、预定义可生成）。需求未澄清 Detailed/Grouped 语义 → 判停先与客户对齐（25 次呼叫出 25 行还是 1 行）。

1. 建定义：选 Source（大数据量优先 Total counters）、Type、模板。完成标准：向导完成
2. Querytool 选字段并配 Operation（grouped 才有）、Sort、Filter。完成标准：数据列与聚合口径正确
3. 需要派生列时用表达式编辑器写公式并改名。完成标准：公式结果抽样正确
4. 生成期才定的条件勾 Generation Time Filter。完成标准：一份定义多场景复用
5. Designer 布局：区域、前后缀、小数位。完成标准：版面可读
6. 嵌套汇总：下层 Sum 先做，上层区域切 View 后引用下层 Sum。完成标准：逐级合计=手工核算
7. 图表：Insert Chart 选类型与 View/X/Y（同区域字段）。完成标准：图可读
8. 消除多余表头/隐藏中间层：加共有字段组头 + 前景空白遮蔽。完成标准：末页干净
9. Hit-list（grouped）限量并生成。完成标准：行数=限量值

判停点：

- 公式/图表选不到别的区域的字段 → 硬边界（同视图区域），按"切 View"路径重构而不是硬引用
- 想隐藏中间合计却删了字段 → 上层计算会断，唯一做法是前景空白遮蔽
- Hit-list 配在详细定义上 → 不生效，Hit-list 仅 grouped
- 题面汇率（1.21 与 1.3）书内不一致 → 以交付约定为准（needs-review nr-01）

输出契约：报表定义清单（字段/Operation/过滤/公式）+ 生成实例与核算对照 + 版面技巧备注。

## B — 边界

- 五个练习的数值规格是教学题面（实验口径），交付保留模式、替换业务值；题面笔误两处见 needs-review nr-01/nr-02
- 不可删除默认模板两件（Template/Compact template）；自定义模板可另存
- 不同区域的表头不能混用出图/出公式（p396）；中间层隐藏唯一办法是前景空白（p617）
- 图表类型限 Bar/Curve/Pie/Plot/Stacked Bar/Multi-counter pie（Ed45 界面口径）
- 大数据量定义优先 Total counters 数据源，否则受报表能力卡的六项上限约束
