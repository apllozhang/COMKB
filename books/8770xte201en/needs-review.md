# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。
> 提取器已在 candidates/counter-example.md 登记 4 处书内笔误（n41-n44），此处复核确认并补 1 处命名漂移、1 处口径混用。

## nr-01 报表练习汇率两处不一致（原文如此）

- **位置**: p402 题面 "1 €= 1,21 dollar" vs p550 题面复述 "1 €= 1,3 dollar"、p557 实现公式 "$cost = € cost*1.3"（n41）。
- **差异**: 同一个 report #1 练习，题面章与实现章汇率相差 0.09；教材未修订。
- **影响**: 按"对照题面验收"会判不一致；示例输出列（0.5555€→0.7054$）两页相同，说明正文示例本身按某一口径自洽。
- **处置**: 引用时标注"书内双口径"；实践按当次交付约定汇率取值，公式结构（$cost=€cost×汇率）不受影响。

## nr-02 report #4 题面运营商名排版残留（原文如此）

- **位置**: p607 "Only outgoing calls linked to Telecom 1 or Telecom 7"（或 "Telecom 0"）vs p613 实现章与 Filter Editor 均为 Telecom 1 / Telecom 2（n42）。
- **判断**: 题面排版残留（7 与 2、0 与 2 形近），实现章自洽。
- **处置**: 能力卡引用按 Telecom 1/Telecom 2，并注明题面原文如此；照抄题面会找不到运营商。

## nr-03 成本中心用户姓名字段颠倒（原文如此）

- **位置**: p91 建 31011 的字段表 "Directory Name: Alice / Directory First Name: Adams"；p89 分配表同写 "31011 Adams Alice"；对照 31010（Ava Adore）为正确顺序（n43）。
- **判断**: 示例值写反，字段语义本身清楚（Name=姓、First Name=名）。
- **处置**: 教学复现按 Name=Adams、First Name=Alice 纠正并注明；不改变成本中心与记账机制。

## nr-04 Telecom 2 方向表文字残留（原文如此）

- **位置**: p210 "Direction from Brest region to Brest region" 的字段说明残留 Telecom 1 的 "Called region: Local region"，主叫写作截断的 "Brest re"（n44）。
- **判断**: Telecom 2 并未建 Local region，其本地被叫是 Brest region 自身兼被叫。
- **处置**: 按 Telecom 2 实际区域结构（Brest 双栖区）配置；引用时标注原文残留。

## nr-05 成本中心命名 MKT/Marketing 漂移（原文如此）

- **位置**: p89/p91 命名口径为 MKT（1=MKT）；p305、p332、p349、p470 的组织树提醒行写 "Marketing"，其中 p349 同页上一行 Marketing、下一行又用 "Subscribers are distributed into ... MKT"。
- **判断**: 书内命名漂移，非机制矛盾——成本中心名是自由命名的显示字段，编号 1 才是槽位。
- **处置**: 能力卡统一按 p89 的 MKT 口径引用并标注"书中部分章节写作 Marketing"；不影响任何操作路径。

## nr-06 FTP 示例密码与实验环境不一致（书内自洽）

- **位置**: p109（p448 同文）PCX 页签示例密码 "Superuser1234*"，实验环境 OXE 实际口令为 "Superuser2580*"（p47/p77）。
- **判断**: 原文自己已给出裁决规则——"They must be the same as on the OmniPCX Enterprise"；示例值仅示意。
- **处置**: 能力卡按铁律表述（密码与 OXE 一致、用户名 adfexc 禁改），不引用示例密码为配置依据。

## nr-07 含推断/时效成分的结论（引用需带标注）

- BOOK_OVERVIEW 批判节三条时效性口径：虚拟化清单与 Capacity Planning tool V3.0 为 Ed45 时点（p8）；兼容矩阵随版本演进（p9）；界面/预定义报表清单随版本漂移——引用时标"Ed45 口径"。
- 教学税率 10%/20% 与汇率 1.21/0.82 为实验口径（p145-146），非真实监管费率。
- n32 的生产类推（"话务须走被监控的 IP 承载段"）已用"（生产类推）"字样显式标示；n13 "No first carrier found" 两类根因为书内日志样例的直接归纳。
- **处置**: 三条均已带标注；能力卡引用时保留口径标记，不升格为普适结论。
