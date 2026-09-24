# ACD 营业时段与例外日配置（OXO Connect）

## R — 原文依据

> "Exceptional closing days • Possibility to define a maximum of 40 closing days • Exceptional opening days • Possibility to define a maximum of 10 opening days • A maximum of 2 times ranges per opening day can be managed"（p100）
> "The ACD groups will be open from Monday to Friday, from 08:00 to 12:00 and 13:00 to 18:00. In addition, ACD groups will be closed 1 January, 1 May and 25 December. Only the Group ACD n°1 will be open December 25 from 9:30 to 11:30"（p108）

出处：OXOCXTE107EN p100（上限规格）、p108（配置实验）。

## I — 自述

营业日历分两层：每周常规时段 + 例外日。常规时段按组在 Opening criteria 里填（如周一至五 8-12、13-18）；例外日按组分两类——例外关闭日（法定节假日，上限 40 天）与例外开放日（通常关门的日子例外开门，上限 10 天，且每天最多 2 个时段）。组关闭时的来话行为（关闭语/转接/邮箱）由六场景里的关闭流程接管，本能力只负责把"什么时候开门"定义准。

## A1 — 书中案例

**时段+例外日实验**（p108，厂商实验）：常规周一至五 08:00-12:00 与 13:00-18:00；1 月 1 日、5 月 1 日、12 月 25 日三个例外关闭日；组1 在 12 月 25 日 9:30-11:30 例外开放。操作：General parameters → "Group 1-4" tab → 选组点 Opening criteria 图标填时段 → Exceptional days 页签选显示方式（opened/closed/both）后按组填两类例外日。

## A2 — 未来触发

使用情境：下班/周末不接听；法定节假日批量关闭；节假日轮值例外开放；不同组不同营业时间。
语言信号：营业时间 / opening hours / 节假日 / 例外日 / exceptional / closing days / 下班后。

与相邻能力区分：关闭时段的来话行为出口 → 六场景能力；本能力只管日历定义。

## E — 可执行步骤

输入契约：每周时段表、节假日清单、例外开放需求（哪天/哪个组/几点到几点）。缺节假日清单先向客户索取。

1. OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / "Group 1-4" tab。完成标准：组列表可见。
2. 选组 → Opening criteria 图标 → 填每周开放时段。完成标准：时段表保存。
3. Exceptional days 页签：选列表过滤方式（opened/closed/both）→ 填例外关闭日（≤40）与例外开放日（≤10，每日 ≤2 时段），按组分别维护。完成标准：两类例外日录入且未超限。
4. 验证：在例外日当天实呼确认行为（关闭组播关闭语、例外开放组正常进 ACD）。完成标准：行为与日历一致。

输出契约：各组营业日历表 + 例外日清单 + 验证记录。

## B — 边界

- 例外日容量硬上限：关闭 40 天/开放 10 天/每开放日 2 时段——全年假日超 40 天的需求要提前发现（多组分担或方案层解决）。
- 例外日跨年维护、日期输入格式原书未展开（needs-review），录入后务必实呼验证。
- 组关闭后的来话出口配置属六场景能力；时段改了但行为不对时先查出口再查日历。
