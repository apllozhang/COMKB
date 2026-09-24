# POLISH-NOTES — vsaaxte001en（全文中文化润色核对记录）

核对日期：2026-09-24
核对范围：`.cangjie/capabilities/cards/*.md`（12 张卡片）+ `book/overview.md` + `book/glossary.md`，共 14 份文件，全部逐字通读。

## 结论：经核对无需修改

原因：

1. 全书行文已是自然的中文工程文档口吻（短句动宾、判停点/完成标准格式统一、表格化对比成熟），未发现"被配置为""允许……到……""使用……来进行……""respective"等机器翻译腔，也无"零touch"类中英混写生造词。
2. 模式扫描 + 人工通读双重复核，以下模式全书零命中：`被配置为/被配置成`、`respective`、`被用来/被用于/被使用`、`允许…到…`、`使用…来（进行|实现|完成）`、`需要被/将会被/可以被`、中文行内英文助动词残留、中英混写生造词。
3. 扫描疑似命中逐条人工判定均为自然中文，不是翻译腔：
   - "管理员被锁""slave 现有配置被清空""改配置被拒（只读）"——真实被动语义的自然表达；
   - "PCS/OMS/IPDSP 等缩写书中未给全称，如实标注"——术语纪律声明，非残留。

## 核对过但决定保留的边界情况（供后续复核参考）

| 文件 | 卡片/位置 | 原文片段 | 保留理由 |
|---|---|---|---|
| book/overview.md | 交付主线（组织轴） | "准备 OXE 底座 → 安装 VAA（install.sh）→ ……"（箭头链） | 章节路线图组织轴体例，四本书 overview 一致；本行无表达问题 |
| cards/vaa-install-sip-integration.md | I 段第 3 块 | "外部回叫翻译去 '0B' 显示" | 高度压缩但对应原书具体参数行为（回叫翻译表删位显示），扩写反而有杜撰风险 |
| cards/vaa-pcs-opex-licensing.md | I 段 | "PCS 支撑" | "支撑"在此指对外围站点的支撑结构，语境自明；避免过度改写 |

## 红线遵守声明

- 未改动任何数字、版本号、页码、IP、端口、容量数字、菜单路径、命令、参数、文件名、slug、链接。
- 未改动 R 段 `>` 英文引文；未改动任何 `#` 标题行能力名。
- 未触碰 verified.yaml、destinations.json、dist 目录与 .cangjie 下工具脚本。

## 验收

- `python .cangjie/scan_dense.py books/vsaaxte001en` → 零输出问题（仅 done 行）
- `python .cangjie/scan_blank.py books/vsaaxte001en` → 零输出问题（仅 done 行）
