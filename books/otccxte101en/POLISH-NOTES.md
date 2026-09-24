# POLISH-NOTES — otccxte101en 中文化润色记录

> 润色范围：.cangjie\capabilities\cards\*.md（13 张）+ book\overview.md + book\glossary.md。
> 红线遵守：R 段英文引用、数字/页码/版本号、菜单路径/命令/参数/slug、yaml、# 标题行均未改动。
> 验收：scan_dense / scan_blank 均零输出（基线即干净，改后复扫仍干净）。
> 核对结论：overview.md 与 glossary.md 行文通顺，经核对无需修改。

## 逐处修改清单

### 1. otcad-acd-maintenance.md（A2 段）

- "链路断了的互助行为与水位参数转Remote PG 卡；ASM 记忆的路由语义转ASM 脚本卡" → "……转 Remote PG 卡；……转 ASM 脚本卡"
  理由：动宾之间缺空格，英文术语紧贴"转"字是英文直译排版残留，插入空格后符合本门户"中文与英文术语间留空"的行文习惯。

### 2. otcad-acr-objects.md（A2 段）

- "转ISM 技能匹配卡……转ASM 脚本卡……转Remote PG 卡" → "转 ISM 技能匹配卡……转 ASM 脚本卡……转 Remote PG 卡"（同上，3 处）

### 3. otcad-asm-script-advanced.md（A2 段）

- "转ISM 技能匹配卡……转ACR 对象卡" → "转 ISM 技能匹配卡……转 ACR 对象卡"（2 处）

### 4. otcad-ccs-onboarding.md（A2 段）

- "多客户端集中接入与 CCS Server转CCS Server 卡" → "多客户端集中接入与 CCS Server 转 CCS Server 卡"
  理由：原句英文术语两头紧贴，是全文最拗口的一处；补空格后主宾分明。
- "转ACR 对象卡（路由卡）；……转book/overview 环境区" → "转 ACR 对象卡（路由卡）；……转 book/overview 环境区"（2 处）

### 5. otcad-ccs-server.md（A2 段）

- "转CCS 安装与实验环境卡（路由卡）" → "转 CCS 安装与实验环境卡（路由卡）"
- "实时锁与许可语义转本卡维护锚点" → "实时锁与许可语义归本卡维护锚点"
  理由："转本卡"动宾搭配别扭；该语义本就落在本卡内，用"归"更准确自然。
- "转ACD 维护命令箱卡（路由卡）" → "转 ACD 维护命令箱卡（路由卡）"

### 6. otcad-ccta-ticket-analysis.md（A2 段 + E 段）

- "转Excel 报表卡；实时看板转Soft Panel 卡；SPM 部署问题转SPM 部署卡" → "转 Excel 报表卡；实时看板转 Soft Panel 卡；SPM 部署问题转 SPM 部署卡"（3 处）
- "输入契约：OXE 票据机制在产话务" → "输入契约：OXE 票据机制开启且有在产话务"
  理由：原文省略过度，"机制在产话务"不成句；补出"开启且有"后语义完整且未改事实。

### 7. otcad-excel-report-customization.md（A2 段）

- "转CCTA 卡；日统计的产生与口径转SPM 部署卡" → "转 CCTA 卡；日统计的产生与口径转 SPM 部署卡"（2 处）

### 8. otcad-ism-skill-matching.md（A2 段）

- "转ASM 脚本卡（路由入口……）……转ACR 对象卡（路由卡）" → "转 ASM 脚本卡……转 ACR 对象卡"（2 处）

### 9. otcad-remote-pg-mutual-aid.md（A2 段 + I 段表格）

- "维护命令全表转ACD 维护命令箱卡（路由卡）" → "维护命令全表转 ACD 维护命令箱卡（路由卡）"
- "呼叫在本地队列等满 N 秒才许流向远端" → "……才允许流向远端"
  理由："才许"生硬，补全为"才允许"，语义不变。

### 10. otcad-soft-panel-manager.md（A2 段）

- "转SPM 部署卡；日统计对账转SPM 部署卡；CCTA 离线票据转CCTA 卡" → "转 SPM 部署卡；日统计对账转 SPM 部署卡；CCTA 离线票据转 CCTA 卡"（3 处）

### 11. otcad-special-features.md（A2 段）

- "与互助溢出转Remote PG 卡……转ACR 对象卡（路由卡）" → "转 Remote PG 卡……转 ACR 对象卡"（2 处）

### 12. otcad-spm-deployment.md（A2 段）

- "转Soft Panel 可视化配置卡……转CCS 安装与实验环境卡（路由卡）" → "转 Soft Panel 可视化配置卡……转 CCS 安装与实验环境卡"（2 处）

## 未改动说明

- 各卡 R 段英文原文引用（含页码）逐字未动。
- 各卡 I/A1/E/B 段的电报式紧凑行文（如"经典组合：链路>对象>坐席……"）为本书既有风格且可读，未强行散文化。
- book/overview.md、book/glossary.md：通读核对无直译腔，经核对无需修改。
