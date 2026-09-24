# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 密码老化期为开区间（原文与总览简写不一致）

- **位置**: p93 "Possible values: 10 < validity period for password in DAYS < 366（"0" means no aging password）"；BOOK_OVERVIEW 简写为"10-366 天老化"。
- **差异**: 原文为严格不等号（10 与 366 两个端点值本身不合法），总览简写读起来像闭区间。
- **影响**: 配置取值边界；取 10 或 366 会被系统拒绝还是接受，书中未演示端点行为。
- **处置**: 能力卡按"10-366 天范围内取值（原文为开区间，端点值未验证）"表述；引用以 p93 原文为准。

## nr-02 原文笔误/排版瑕疵清单（引用时注意）

- p248 "root [mg4.ale]]"——多一个右括号（原文如此）。
- p139 "TRUSTED_RANGE,<First IP Address>,<Last IP Addres>"——Addres 缺 s（原文如此）。
- p358 "TO TAKE INTO ACCOUT THE MODIFICATIONS"——ACCOUT 拼写（原文如此）。
- p619 "IF THIS LAST ONE IS NOT ALREADY EXISITING"——EXISITING 拼写（原文如此）。
- p419 "the Transfer COS Id is the same as the Connection COS COS Id"——COS 重复（原文如此）。
- p451 "Two mode of call presentation"——单复数（原文如此）。
- **处置**: 原文引用保留并注明"原文如此"；转述时用正确拼写。

## nr-03 BOOK_OVERVIEW 术语计数与实际不符

- **位置**: OVERVIEW 自记"术语按实际内容列出（17 个）"；术语表实为 19 行；glossary-extractor 核对表按合并口径映射为 16 组（OPS/RTR、NPD/DID translator、Entity/CDT 各并一行）。
- **判断**: 三种计数各有口径（17 为笔误；19 为表行数；16 为合并映射组数），非内容矛盾。
- **处置**: OVERVIEW 保持原样作审计痕迹；下游一律以 candidates/glossary.md 60 条为唯一基准。

## nr-04 培训实验约定覆盖在通用规则上（实验口径清单）

- **位置与内容**:

- 空库国家码统一 FR（p190 原文明示"real customer site 需用真实国家码"）；空库上限（Users 10014/1/2 com 3859）随 config.mao 变化，为实验库实例值。
- ISDN 信令变体统一 ISDN France、发送位数 10 位、去位数 4/9 位、抓取前缀 #010/#012（p784 明示现场按运营商定）。
- ITSP1 号段/账号（pbxP/alcatel、3321PN41000 ↔ 31000、紧急回叫规则 A15/A17/A18/A112）为模拟器特设（p636 Warning 自证）。
- 实验租期示例 default/max-lease-time 3600 秒、bootp 600 秒（c14 实验输出值）。
- 实验口令族（Administrator5689! / Superuser2580* / letacla1 / mg4.ale / mgxl.ale / alcatel / 0000 / *tx8000#）遍布正文（n01）。
- **处置**: 全部标"实验口径"；环境值只进能力卡 Boundary 与 book/overview，正文不把实验值当生产依据。

## nr-05 话务台呈现模式标签 "Statistic" 用词存疑

- **位置**: p451 "Two mode of call presentation • Parallel (default mode) • Statistic"，Statistic 模式的行为描述为"按最长待命优先轮转呈现"。
- **判断**: 标签与行为语义不对应，疑为原文用词/排版变体（如 Cyclical 类词）；书中无第二处解释。
- **处置**: 保留原文标签照录，转述按行为描述（并行/轮转两种呈现），不做外部补全。

## nr-06 三处含推断成分的结论（引用需带标注）

- n43: BAD PCMS CODE=实验环境占位、unknown rack type=机架模型差异——书中原样贴出未解释，"非故障"判断基于实验上下文，属谨慎解读。
- n43: 484 Address Incomplete=无 DID 翻译时的预期来话失败——由实验下一步（配 DID 后恢复）反推，机制自洽但书中未明说"预期"。
- n11: RADIUS 与本地密码老化互斥的表述——书中给出机制原因（RADIUS 认过但 OXE 拒会话），"必须关闭"为原文原话，非推断；此条仅提示引用时保留原文语境。
- **处置**: 前两条已标"（推断）"；能力卡引用时保留推断标注，不升格为书中明示事实。
