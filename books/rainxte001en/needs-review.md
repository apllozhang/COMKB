# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 自动配置版本门槛两处表述不一致

- **位置**: p121 "available from system version R4.0.020.002"（讲义）vs p150 "applies to versions greater than R4.0.020.002"（实验手册）
- **差异**: "from"（含该版本）与 "greater than"（高于该版本）语义相差一个版本点。
- **影响**: 版本核查的判定边界；版本恰好等于 R4.0.020.002 的站点是否能用自动配置，两页答案不同。
- **处置**: 能力卡 Boundary 注明两处原文口径；实践建议取"≥R4.0.020.002 可用、生产以更高版本执行"；低版本先升级。候选 n20 已完整记录。

## nr-02 c09 测试清单 "Job Call – Computer" 原文如此

- **位置**: p161 路由切换测试清单第二项。
- **判断**: 疑为 "Office phone"（或类似词）的原文排版/OCR 变体；同一清单其余项（Computer Call – Computer / Computer call – extension / Meeting with 3 participants / Screen sharing / Video）正常。
- **处置**: 保留原文不改；能力卡引用时标注"原文如此"。

## nr-03 BOOK_OVERVIEW 两处计数修正

- **术语数**: OVERVIEW 自记"17 个"，术语表实为 16 行（疑把"内部/外部/OCE-FE GW"一行拆三计）。glossary-extractor 逐条核对 16 行全部有效；下游以 glossary.md 62 条为基准。
- **成员设置块数**: OVERVIEW 记"八块"，p96 原文为 7 分区 + p98 的 Tags/Profiles 横向项；f21/p19 已按原文口径修正，下游以 7 分区为准。
- **处置**: OVERVIEW 保持原样作审计痕迹，凡冲突以 verified.md / candidates 为准。

## nr-04 实验账号命名口径混用（原文如此）

- **位置**: p105-108 实验正文账号为 `cCpP.user1@...`（C=班号 P=POD 号），p106 示例却出现 `c2p1.user1@ale-training.com`、`Password1*`。
- **判断**: 同一命名法的两种写法并存（c2p1 = C2P1 即班 2 POD 1 的实例化），原文如此。
- **处置**: 能力卡统一用 `cCpP` 泛型写法并标注"实验口径"；不采信具体实例值为配置依据。

## nr-05 原文笔误两处（引用时注意）

- p34 "Many answers **tou** your questions"（应为 to）。
- p33 "Microsoft **0365**"（应为 O365）。
- **处置**: 原文引用保留并注明；转述时用正确拼写。

## nr-06 三处含推断成分的结论（引用需带标注）

- n16: "RCC 用户呼叫纯 Rainbow 用户不通"——书中以测试问题呈现未给答案，"不通"为机制推断（无网关即无音频通路）。
- n24: Anydevice 与 OXE REX 的对应引申。
- n43: 监督组与 OXO ACD 组的对比引申。
- **处置**: 三条均已标"（推断）"；能力卡引用时保留推断标注，不升格为书中明示事实。
