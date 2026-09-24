# POLISH-NOTES — openxte300en（全文中文化润色核对记录）

核对日期：2026-09-24
核对范围：`.cangjie/capabilities/cards/*.md`（12 张卡片）+ `book/overview.md` + `book/glossary.md`，共 14 份文件，全部逐字通读。

## 结论：经核对无需修改

原因：

1. 全书行文已是自然的中文工程文档口吻（短句、动宾结构、判停点/完成标准格式统一），未发现"被配置为""允许……到……""使用……来进行……""respective"等机器翻译腔或英文残留。
2. 用模式扫描做了双重复核（脚本扫描 + 人工通读），以下模式全书零命中：`被配置为/被配置成`、`respective`、`被用来/被用于/被使用`、`允许…到…`、`使用…来（进行|实现|完成）`、`需要被/将会被/可以被`、中文行内英文助动词残留、中英混写生造词（如"零touch"类）。
3. 扫描中的疑似命中经逐条人工判定均为合法内容：
   - "touch 混写"命中全部是产品名/技术名（OpenTouch、opentouchd、opentouch.company.com），按红线不动。
   - "口令被拒"等被动句是自然中文表达，非翻译腔。
   - R 段 `>` 引用的英文原文（含页码）一字未动。

## 核对过但决定保留的边界情况（供后续复核参考）

| 文件 | 卡片/位置 | 原文片段 | 保留理由 |
|---|---|---|---|
| cards/ots-voice-mail.md | I 段档案四页签 | "零出（Attendant call enabled）" | "零出"是 zero-out 功能的紧凑译法，随附英文原名，属术语而非直译腔；改动反而有杜撰术语风险 |
| book/overview.md | 交付主线（全书组织轴） | "方案概览与实验环境 → 软件安装…… → 维护、备份与 rehosting"（箭头链） | 这是章节路线图（组织轴），与菜单路径同类的"链式导航"用法；四本书 overview 采用同一体例，重排为编号步骤会破坏跨书一致性，且本行不涉及表达问题 |
| book/glossary.md | 各术语行 | "口径：定义只采信本书正文……" | 术语表为结构化中英对照，表达已达标 |

## 红线遵守声明

- 未改动任何数字、版本号、页码、IP、端口、容量数字。
- 未改动菜单路径、命令、参数、文件名、slug、链接。
- 未改动 R 段英文引文。
- 未改动任何 `#` 标题行能力名；未触碰 verified.yaml、destinations.json、dist 目录与工具脚本。

## 验收

- `python .cangjie/scan_dense.py books/openxte300en` → 零输出问题（仅 done 行）
- `python .cangjie/scan_blank.py books/openxte300en` → 零输出问题（仅 done 行）
