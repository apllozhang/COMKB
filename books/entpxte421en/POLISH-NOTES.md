# POLISH-NOTES — entpxte421en（OmniPCX Enterprise 加密解决方案）

润色日期：2026-09-24。范围：12 张能力卡 + book/overview.md + book/glossary.md。

## 结论

**经逐卡通读与全量句式扫描，未发现机器翻译腔、英文直译、生硬表达问题。** 针对"被配置为/被设置为/被用来/被用于/允许…到…/使用…来进行/respective/能够被"等目标句式做了全书正则扫描（R 段英文引用除外），零命中；"被/进行/允许"三类高频机翻构造人工复核亦为零命中。

实际修改为排版铁律修正，共 1 处（位于 book/overview.md），12 张能力卡与 glossary.md 经核对无需修改。

## 修改明细

| # | 文件 | 位置 | 原文片段 → 改后片段 | 理由 |
|---|---|---|---|---|
| 1 | .cangjie\capabilities\book\overview.md | 交付主线（原第 7 行） | "密码学/证书基础 → 证书就位（PKI 模式→CSR→签发→导入→twin）→ 系统参数与 lanpbx.cfg → … → ABC-F 网络与 mTLS 强化（p4, p111-403）。先证书后开关、先单机后网络，就是实际交付项目的推荐顺序。" → "交付主线分八段（p4, p111-403）：先证书后开关、先单机后网络，就是实际交付项目的推荐顺序。" + 编号 1-8 步（内层"PKI 模式→CSR→签发→导入→twin"改为顿号列举"PKI 模式、CSR、签发、导入、twin"） | 排版铁律：散文一行 11 个 → 箭头，拆成编号步骤；八个阶段名、内层五环节与页码原样保留 |

## 验收凭据

- `python F:\AIwork\ZCode\.cangjie\scan_dense.py F:\AIwork\ZCode\books\entpxte421en` → 仅输出 "scan_dense done: entpxte421en"，零问题
- `python F:\AIwork\ZCode\.cangjie\scan_blank.py F:\AIwork\ZCode\books\entpxte421en` → 仅输出 "scan_blank done: entpxte421en"，零问题
- 未触碰 verified.yaml、destinations.json、dist 目录；未改动任何 # 标题行、R 段英文引用、yaml 代码块
