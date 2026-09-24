# POLISH-NOTES — entpxte401en（OmniPCX Enterprise Advanced）

润色日期：2026-09-24。范围：12 张能力卡 + book/overview.md + book/glossary.md。

## 结论

**经逐卡通读与全量句式扫描，未发现机器翻译腔、英文直译、生硬表达问题。** 针对"被配置为/被设置为/被用来/被用于/允许…到…/使用…来进行/respective/能够被"等目标句式做了全书正则扫描（R 段英文引用除外），零命中；"被/进行/允许"三类高频机翻构造人工复核亦为零命中。原文口吻已是成熟的中文工程文档风格。

实际修改为排版铁律与错字修正，共 4 处，全部不改动任何事实。

## 修改明细

| # | 文件 | 位置 | 原文片段 → 改后片段 | 理由 |
|---|---|---|---|---|
| 1 | .cangjie\capabilities\book\overview.md | 全书主线（原第 7 行） | "SSH 免密地基 → CS 冗余（本地/空间）→ IP 域与 CAC → … → 组网双向溢出（p41 起的章节序列，p43/p44 两张架构图为底座）。" → "全书主线按章节序列展开（p41 起，p43/p44 两张架构图为底座）：" + 编号 1-9 步 | 排版铁律：散文一行 8 个 → 箭头，拆成编号步骤；九个阶段名与页码原样保留 |
| 2 | book\overview.md | 实验环境集中式 Pod 条 | "集中式 Pod：Subnet 1=192.168.1.x（…）；Subnet 2=192.168.2.x（…）；公共区 10.20.30.x（…）；FlexLM 192.168.1.80（p7-10）。" → 在"公共区"前拆为两条列表项（第二条以"集中式 Pod 公共区"起头） | 单行 218 字超 200 字；网段与地址原样保留 |
| 3 | book\glossary.md | 核心概念域 Broadcast 行 | "MAO 修改→buffer→默认 10 分钟落 LOG→互比 lupd.dat 补齐→确认后删除；…" → "MAO 修改先进 buffer，默认 10 分钟后落 LOG，再互比 lupd.dat 补齐，确认后删除；…" | 排版铁律：一行 4 个 → 箭头的流程散文改为自然短句；数值 10 分钟与文件名原样保留 |
| 4 | .cangjie\capabilities\cards\entadv-desk-sharing.md | A1 步骤 5 | "系统参数五项按客户策略核 对（默认值见 I 段）" → "系统参数五项按客户策略核对（默认值见 I 段）" | 修复"核对"中间的错误空格 |

## 验收凭据

- `python F:\AIwork\ZCode\.cangjie\scan_dense.py F:\AIwork\ZCode\books\entpxte401en` → 仅输出 "scan_dense done: entpxte401en"，零问题
- `python F:\AIwork\ZCode\.cangjie\scan_blank.py F:\AIwork\ZCode\books\entpxte401en` → 仅输出 "scan_blank done: entpxte401en"，零问题
- 未触碰 verified.yaml、destinations.json、dist 目录；未改动任何 # 标题行、R 段英文引用、yaml 代码块
