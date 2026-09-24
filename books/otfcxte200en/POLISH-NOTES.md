# POLISH-NOTES — otfcxte200en 中文化润色记录

> 润色范围：.cangjie\capabilities\cards\*.md（11 张）+ book\overview.md + book\glossary.md。
> 红线遵守：R 段英文引用、数字/页码/版本号、菜单路径/命令/参数/slug、yaml、# 标题行均未改动。
> 验收：scan_dense / scan_blank 均零输出（基线即干净，改后复扫仍干净）。

## 逐处修改清单

### 1. otfax-directory-routing.md（I 段）

- "目录与路由是大客户落地的四个机制：" → "目录与路由是大客户落地的五个机制："
  理由：冒号后实际列出 5 项（目录声明/Lookup 两表/免密登录/路由四旋钮/号码规整与计费），计数词与清单不符是行文硬伤；仅改自述计数，未动任何书内事实。

### 2. otfax-services-operations.md（I 段，两处）

- "4. **三通道运维**……5. **日志体系**……" → "5. **三通道运维**……6. **日志体系**……"
  理由：列表编号"4"出现两次（4/4/5），修正为连续编号 4/5/6，仅排版不涉内容。
- "无状态 4 个（负载均衡的工人，含 XMXmlGateway）" → "无状态 4 个（可负载均衡的工作组件，含 XMXmlGateway）"
  理由："工人"是英文 worker 的生硬直译，改为工程文档惯用语。

### 3. otfax-client-coversheet.md（I 段）

- "用户侧入口与品牌化两件事：" → "用户侧入口与品牌化两条线："
  理由：冒号后列 4 项，"两件事"指两大主题而非条目数，改"两条线"消除计数误导。

### 4. otfax-installation-ftw.md（I 段）

- "采购向经销商提供服务器 MAC 地址" → "采购时向经销商提供服务器 MAC 地址"
  理由：缺时间状语读起来像"采购（这个动作）提供地址"，补"时"字后通顺。

### 5. otfax-mail-exchange-integration.md（I 段）

- "官方强烈建议前置真实邮件服务器——换回队列管理、Outlook 表单集成、垃圾过滤、病毒检查四类能力" → "……——换来队列管理、Outlook 表单集成、垃圾过滤、病毒检查四类能力"
  理由："换回"疑为"带回/换来"之误且歧义；已回查原书 p160（"inserting a mail server in front of the SMTP Gateway provides: … Spam filtering / Virus checking"），确认语义是"前置邮件服务器可换来四类能力"，改"换来"消除歧义，四类能力名未动。

## 未改动说明

- 各卡 R 段英文原文引用（含页码）逐字未动；p142 等处 "Creat"（原书菜单拼写）、"Outlook 2022" 笔误标注等照录项未动。
- otfax-solution-planning.md 第 5 项前有空行（列表 1-4 与 5 分段），Markdown 渲染编号连续，不构成缺陷，未动。
- book/overview.md、book/glossary.md：通读核对无直译腔，经核对无需修改。
