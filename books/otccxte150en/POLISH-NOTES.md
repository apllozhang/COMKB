# POLISH-NOTES — otccxte150en 中文化润色记录

> 润色范围：.cangjie\capabilities\cards\*.md（12 张）+ book\overview.md + book\glossary.md。
> 红线遵守：R 段英文引用、数字/页码/版本号、菜单路径/命令/参数/slug、yaml、# 标题行均未改动。
> 验收：scan_dense / scan_blank 均零输出（基线即干净，改后复扫仍干净）。
> 核对结论：本套卡片行文质量整体最好（"见 XXX 能力"指引格式统一、无缺空格问题），仅 2 处错字级瑕疵。

## 逐处修改清单

### 1. acr-asm-deployment.md（A2 段）

- "OXE 资占用外部服务器分担" → "OXE 资源占用由外部服务器分担"
  理由："资占"为"资源占用"掉字，且原句缺介词，读不成句；补全后语义不变。

### 2. acr-multilanguage-voiceguide.md（I 段）

- "语言 1 对应消息 1000、语言 2 对应 1001、依此到语言 40 对应 1039" → "……依次到语言 40 对应 1039"
  理由："依此"为"依次"错字。

## 未改动说明

- 各卡 R 段英文原文引用（含页码）逐字未动。
- 全书"加"字代替代号"+"（如"Pilot 3x600 加 队列 3x999700"、"入站 UDP 加 TCP"）、"见 外部数据库查询路由能力"中"见"后留空等，为本书统一行文约定，保持稳定不统一改。
- book/overview.md、book/glossary.md：通读核对无直译腔，经核对无需修改。
