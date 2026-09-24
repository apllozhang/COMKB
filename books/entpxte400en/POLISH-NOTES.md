# POLISH-NOTES — entpxte400en（OmniPCX Enterprise Starter）

润色日期：2026-09-24。范围：14 张能力卡 + book/overview.md + book/glossary.md。

## 结论

**经逐卡通读与全量句式扫描，未发现机器翻译腔、英文直译、生硬表达问题。** 针对"被配置为/被设置为/被用来/被用于/允许…到…/使用…来进行/respective/能够被"等目标句式做了全书正则扫描（R 段英文引用除外），零命中；"被/进行/允许"三类高频机翻构造人工复核亦为零命中。原文已是自然的中文工程文档口吻。

实际修改为排版铁律与错字修正，共 7 处，全部不改动任何事实（数字/版本/页码/地址/命令/标题均原样保留）。

## 修改明细

| # | 文件 | 位置 | 原文片段 → 改后片段 | 理由 |
|---|---|---|---|---|
| 1 | .cangjie\capabilities\book\overview.md | 课程主线（原第 7 行） | "准入链五连（登录加固 → 系统启停 → …）→ 配置域（…）→ 业务域（…）→ 运维收尾（…）（p1-821，任务-工具对位：…）" → 拆为引句 + 编号 1-4 步 + 单独的"任务-工具对位"句 | 排版铁律：散文一行 7 个 → 箭头且 250 字，拆成编号步骤；事实与页码原样保留 |
| 2 | book\overview.md | 实验环境第 1 条 | "…+ 4 台 PC Client；混合模式另有课堂 GD4（192.168.1.12）、话机与 4059EE（p3-20）。" → 在分号处拆为两条列表项 | 单行 219 字超 200 字上限，按语义边界拆分 |
| 3 | book\overview.md | 实验环境 ITSP1 条 | "…注册账号 pbxP/alcatel、域 sip.itsp1.fr；安装号 3321PN（PN=两位 POD 号）、DDI 段 41000 ↔ 内部 31000、紧急 112/15/17/18（p21-26）。" → 在分号处拆为两条列表项 | 单行 203 字，拆分后号码/域名原样保留 |
| 4 | book\overview.md | 实验环境账号条 | "实验账号口径：…、GDXL root=mgxl.ale、IT Server=training/superuser、…" → 在 GDXL 与 IT Server 之间拆为"实验账号口径 / 实验账号口径（续）"两条 | 单行 254 字；全部账号口令原样保留 |
| 5 | book\overview.md | 系统速览容量条 | "容量与限额：…Entity 0-1000；SIP TG 32 接入成对（…）；4645 7000 信箱/…" → 在 Entity 后拆为"容量与限额 / 容量与限额（续）"两条 | 单行 204 字；容量数字与页码原样保留 |
| 6 | book\glossary.md | 收尾自检第 2 节备查词表 | "SEPLOS（p42）、…、NOS LED（并条 T0/T2）、EVA（…）、…、ICE type（p615 提及）。" → 在 NOS LED 后分作两个自然段 | 单行 250 字的纯词表罗列，分两段便于查阅；词条与页码零改动 |
| 7 | .cangjie\capabilities\cards\ents-first-login-hardening.md | A2 使用情境 | "新 OXE 开局首次登录； SSH 连不上 root" → "新 OXE 开局首次登录；SSH 连不上 root" | 删除"；"后多余的半角空格，与其余卡片分号用法对齐 |

## 验收凭据

- `python F:\AIwork\ZCode\.cangjie\scan_dense.py F:\AIwork\ZCode\books\entpxte400en` → 仅输出 "scan_dense done: entpxte400en"，零问题
- `python F:\AIwork\ZCode\.cangjie\scan_blank.py F:\AIwork\ZCode\books\entpxte400en` → 仅输出 "scan_blank done: entpxte400en"，零问题
- 未触碰 verified.yaml、destinations.json、dist 目录；未改动任何 # 标题行、R 段英文引用、yaml 代码块
