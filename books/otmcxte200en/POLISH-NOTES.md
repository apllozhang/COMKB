# POLISH-NOTES — otmcxte200en 中文化润色记录

> 润色范围：.cangjie\capabilities\cards\*.md（12 张）+ book\overview.md + book\glossary.md。
> 红线遵守：R 段英文引用、数字/页码/版本号、菜单路径/命令/参数/slug、yaml、# 标题行均未改动。
> 验收：scan_dense / scan_blank 均零输出（基线即干净，改后复扫仍干净）。

## 逐处修改清单

### 1. otmsg-general-announcement.md（I 段 + B 段）

- "第四项 "arrive on AA" 是 OT 服务器曾内嵌自动话务员时代的遗留" → "第四项 "arrive on AA" 是 OT 服务器早期内嵌自动话务员时留下的功能"
  理由："曾内嵌……时代的遗留"定语堆叠拗口，是英文语序直译腔；改为通顺中文，事实不变（该项系 OT 服务器内嵌 AA 时代遗留、已废弃）。
- "最长 5 分钟、仅支持 wav 文件的语言可用" → "最长 5 分钟、仅对支持 wav 文件的语言开放"
  理由："仅支持 X 的 Y 可用"是英文 "only available for…" 直译句式，主谓关系拧巴；改为自然中文。B 段引用同短语的加引号提法同步更正，保持全书一致。

### 2. otmsg-notification-smtp-sms.md（B 段）

- ""仅支持 wav 文件的语言可用"部分功能（p223 口径的关联限制）" → ""仅对支持 wav 文件的语言开放"部分功能（p223 口径的关联限制）"
  理由：与 otmsg-general-announcement.md 同一短语，同步更正避免两卡口径不一致。

### 3. book/glossary.md（一、核心概念域 AA/VAA 行）

- ""arrive on AA"播报选项即此遗产，已废弃" → ""arrive on AA"播报选项即其遗留，已废弃"
  理由："即此遗产"生硬，改"即其遗留"，与卡片用词（遗留）一致。

### 4. otmsg-install-site-setup.md（I 段）

- "介质两法制法——全 ISO 刻盘" → "介质两种制法——全 ISO 刻盘"
  理由："两法制法"叠床架屋（"法"字重复），且"两法"缺量词。

### 5. otmsg-license-management.md（I 段）

- "Skip 跳过装许可不中断安装，但手工补装前 OTMC 不会正常工作" → "Skip 跳过装许可不会中断安装，但手工补装前 OTMC 不会正常工作"
  理由："不中断安装"易误读为祈使（"别中断安装"），补"会"字消除歧义；后半句已有"不会正常工作"，语气对齐。

## 未改动说明

- 各卡 R 段英文原文引用（含页码）逐字未动。
- "与相邻能力区分：…… → otmsg-xxx"的箭头指引各卡均 ≤2 个/行，符合排版铁律，未动。
- "13 步向导"等步骤计数为书内口径（card A1 的 15 步含向导前装机动作），属事实陈述，未动。
- book/overview.md：通读核对无直译腔，经核对无需修改。
