# POLISH-NOTES — entpxte402en（OmniPCX Enterprise 系统装载）

润色日期：2026-09-24。范围：12 张能力卡 + book/overview.md + book/glossary.md。

## 结论

**经逐卡通读与全量句式扫描，未发现机器翻译腔、英文直译、生硬表达问题。** 针对"被配置为/被设置为/被用来/被用于/允许…到…/使用…来进行/respective/能够被"等目标句式做了全书正则扫描（R 段英文引用除外），零命中；"被/进行/允许"三类高频机翻构造人工复核亦为零命中。

实际修改为排版铁律修正，共 4 处（其中 2 处位于能力卡内），全部不改动任何事实。

## 修改明细

| # | 文件 | 位置 | 原文片段 → 改后片段 | 理由 |
|---|---|---|---|---|
| 1 | .cangjie\capabilities\book\overview.md | 全书交付主线（原第 7 行） | "RLAB 实验环境 → S.O.T. 部署工具 → … → OPEX/Purple on Demand 订阅许可（p1-408）。递进关系：先装起来、再连上云、最后换许可模型。" → "全书交付主线按章节递进（p1-408）：先装起来、再连上云、最后换许可模型。" + 编号 1-8 步 | 排版铁律：散文一行 7 个 → 箭头，拆成编号步骤；八个阶段名与页码原样保留 |
| 2 | book\overview.md | 实验环境节点条 | "节点（实验口径）：PC Client 192.168.1.9（…）；SOT VM 192.168.1.130（…）；CS3 …；KVM host 192.168.1.55（…）；GAS 192.168.1.45（…）。" → 在 KVM host 前拆为"节点（实验口径）/ 节点（实验口径，续）"两条 | 单行 290 字超 200 字；全部 IP 原样保留 |
| 3 | .cangjie\capabilities\cards\entload-cs-loading.md | I 段"加载后初始化"第 1 条 | "…不得与前 24 个已用密码重复。aging 取值 <10<X<366、0=不限期（答 0 触发 CIS_Benchmark_Req.No_5.6.1.1 警告，生产对 root 保留 aging）" → 拆为"密码规则九条"与"密码 aging"两条列表项，句号改分条 | 单行 211 字；密码规则与 aging 取值、CIS 条目号原样保留 |
| 4 | .cangjie\capabilities\cards\entload-gas-ops.md | I 段"两条运维等式与前提"第 3 条 | "host 升级两条路：…（…全系统停机窗口）；日志 /var/log/rocky-update.log 与 /var/log/gas-rocky-update.log" → 拆为"host 升级两条路"与"host 升级日志"两条列表项 | 单行 218 字；两条日志路径与升级前提原样保留 |

## 验收凭据

- `python F:\AIwork\ZCode\.cangjie\scan_dense.py F:\AIwork\ZCode\books\entpxte402en` → 仅输出 "scan_dense done: entpxte402en"，零问题
- `python F:\AIwork\ZCode\.cangjie\scan_blank.py F:\AIwork\ZCode\books\entpxte402en` → 仅输出 "scan_blank done: entpxte402en"，零问题
- 未触碰 verified.yaml、destinations.json、dist 目录；未改动任何 # 标题行、R 段英文引用、yaml 代码块
