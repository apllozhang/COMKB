# 翻译工作交接手册（HANDOFF）

> **交接状态：已生效（2026-09-25，路线 1）。** 翻译工作已整体移交给接手方；
> 原维护者不再派发翻译子代理。接手方凭交接包（COMKB-translation-handoff.zip，
> 含 25 本源文 + 全部翻译进度 + 5 份 QA 报告 + 包内 README 使用说明）+ 本仓库续跑。
> 交接包为进度权威快照；接手后一切新进度以接手方本地/私有库为准。

> 目标读者：接手本翻译流水线的 AI/工程师。读完本文件 + 现有仓库即可继续工作。
> 更新：2026-09-25。

## 0. 一分钟理解

把 ALE 通信产品线 25 本英文售后教材全文翻译成中文。流水线对齐 deusyu/translate-book 架构：
6000 字符分块 + SHA-256 manifest + 并行子代理 + 术语表硬约束 + 三道质量门（V1 回译忠实度 /
V2 术语 lint / V3 A-B 双译比对）。一切产出都是**幂等的块文件**——断点即状态，重试不返工。

## 1. 当前进度快照（接手后先跑 `python pipeline/translation_status.py` 核对）

| 书 | 块数 | 状态 |
|---|---|---|
| oxo-connect-call-center | 16 | ✅ 全部完成（试点，V1=96） |
| rainxte001en / dectxte200en / openxte225en / otfcxte200en | 21/34/34/15 | ✅ 第一波端到端完成（A/B 译、回译抽查、QA、全译本合并） |
| otmcxte200en / rainxte003en / rainxte101en / vsaaxte001en | 30/35/31/41 | 🔄 第二波 A 译进行中（30/137），B 译未开始 |
| 其余 16 本（entpxte4xx、oxocxte3xx、openxte3xx、otccxte1xx、8770xte2xx、dt00xte215en） | — | ⏳ 未分块 |

## 2. 接手工作流（每本书）

```bash
python pipeline/translate_pipeline.py chunk --book <code>    # 分块 + manifest
python pipeline/translate_pipeline.py terms --book <code>    # 每块术语清单（按书作用域过滤）
# → 派 A 译子代理（直译打底，提示词见 §4）
python pipeline/translate_pipeline.py check --book <code>    # 机制校验：1:1/非空/页锚
# → 派 B 译子代理（意译对照，提示词见 §4）
python pipeline/translate_pipeline.py lint --book <code>     # 术语/残留 lint（A 译）
python pipeline/translate_pipeline.py compare --book <code>  # A/B 分歧清单 → 人工终审
# → 派回译抽查子代理（抽 20-30% 块，提示词见 §4）
python pipeline/translate_pipeline.py qa --book <code>       # TRANSLATION-QA.md + eval.json
# → 合并全译本（参考仓库外的 tmp_wave1_merge.py 逻辑，或手写：按块序拼接 zh/*.md 去块注释）
```

判定完成：A 译 = en 块数；B 译 = en 块数；back_*.json 平均分 ≥90；lint 无禁用形命中。

## 3. 术语表（term_table.yaml，schema v2）

- `global: true` 条目约束所有书；其余只约束 `books` 列出的书（书内词汇表语义按书成立）。
- `prio`: 0=本书词汇表 > 1=共识全局(≥3书) > 2=curated 基线。terms 子命令已按此过滤注入。
- `fixed: true` 是人工修正（劝漏→呼叫劝退、hunt group→寻线组、Agent/Supervisor→座席/班长）。
- 已做 zh 规范化改写：坐席→座席。新增修正改 build_term_table.py 的 OVERRIDES 后重跑，不要手改 yaml。
- 译者反馈回路：子代理汇报的语境冲突（如 client 在 OXO 语境≠8770 的"基础访问账户"）属正常，
  允许译者按规则 8 就语境取舍并汇报；重复出现的冲突才升级为 OVERRIDES。

## 4. 子代理提示词模板（并发 3-4，失败幂等重试；高并发会撞限流/验证码超时整批报废）

**A 译（直译打底）**，变量：{code} {书名+版次} {N1..N2 块号}：
> 你是电信售后培训教材的英译中译者。任务：把 {code}（{书名}）的 chunk{N1}-{N2} 翻译成中文。
> 【第一步】读术语硬约束：pipeline 同级的 term_table.yaml（en => zh 主译名，必须采用）；
> 每块术语清单 books/{code}/zh-fulltext/work/terms/chunk000N.txt；[本书词汇表] 优先级最高，
> [共识全局] 次之，[通用基线] 兜底。
> 【第二步】逐块读 books/{code}/zh-fulltext/work/en/chunk000N.txt，输出同目录 zh/chunk000N.md（UTF-8）。
> 规则：1) 首行 <!-- chunk ... --> 注释原样保留；2) 所有 ===== PAGE N ===== 页锚原样保留、位置对应
> （质检锚点）；3) 术语用主译名；表外产品名/菜单路径/命令/按键名/型号/版本/IP/数字保留英文；
> 4) 术语首现用"中文（英文）"括注；5) 全中文标点，中英/数字间留空格；6) 长句拆短，像人写的中文教材，
> 表格/列表保 Markdown 结构；7) 只输出译文、不为空、不漏段；8) 主译名与本块语境明显冲突时按语境
> 取舍并在汇报中说明。

**B 译（意译对照）**：同上，输出到 zhb/，风格改为"以读者流畅优先：允许重组句序、合并拆句、
被动改主动、压缩啰嗦交代"，底线不变（事实/页锚/术语/首行注释）。

**回译抽查**：抽 2-3 块，读 zh/<块>.md 与 en/<块>.txt，把中文回译成英文与原文逐段比对，写
work/qa/back_<块>.json：{"chunk": "...", "fidelity": 0-100, "issues": ["问题（含页码）"]}。
口径：100=逐段信息等价；90+ 措辞出入；80+ 小遗漏；<90 必须写清。菜单路径/产品名/控制台输出
保留英文属正常，页锚不算内容。

## 5. 红线（违反=返工）

1. ===== PAGE N ===== 页锚的数量、顺序、位置必须与源一致。
2. 事实零改动：数字、IP、密码示例、型号、版本、菜单路径原样保留；源文笔误照抄（可在汇报中备案）。
3. 术语主译名必须采用；zh_alt/旧译禁用。
4. 只译不评；译文不得为空、不得漏段。
5. 不动 .cangjie 下的工具脚本与已发布的 dist/site。

## 6. 版权边界（重要）

本公开仓库**不含** `source_fulltext.txt`（英文源文）与 `zh-fulltext/`（中文译文）——全文翻译属
ALE 版权衍生全文，只在本地与交接包中流转。接手方必须从交接包（zip）取得源文与进度，
不得把全文翻译产物推送到公开仓库。

## 7. 常见故障

- 并行派发报 "user concurrency limit exceeded" / "Captcha timed out"：降并发到 2-3，稍后重试同组；
  组内已写出的块文件不必重译（幂等）。
- agent 中断但文件已写出一部分：跑 translation_status.py 对账，缺哪块补哪块。
- lint 的"未译残留"多为合法保留的英文菜单路径（OMC / ...），人工确认后豁免；真正要修的是
  禁用形命中与缺空格。
