# 通信门户课程蒸馏 SOP（cangjie-skill v2.5 标准工艺）

> 版本：v1.0（2026-09-23）· 首例验证：OXOCXTE107EN（218 页，全流程通过）
> 适用：ALE Communications 门户剩余 24 门课程（后续其他门户课程可复用）
> 技能：cangjie-skill v2.5.0+（`C:\Users\Administrator\.agents\skills\cangjie-skill`，升级方式 `git -C <技能目录> pull --ff-only origin main`）

## 0. 前置检查（每门课开始前，约 2 分钟）

1. `python <技能目录>\scripts\cangjie.py doctor` → 必须 PASS
2. 核对技能版本为最新：`git -C <技能目录> describe --tags` + `git fetch` 后 `rev-list --count HEAD..origin/main` = 0
3. 确认素材 PDF 在 `F:\ALE知识库\Training Offer by Job Function\CBD\` 下，记录：课程代码 / 标题 / 版次 / 页数

## 1. 工作区初始化

```
F:\AIwork\ZCode\books\<课程slug>\
├── source_fulltext.txt      # pypdf 提取全文（脚本见 .cangjie\extract_oxo107.py 改路径复用）
├── PIPELINE_STATE.md        # 断点状态（每阶段更新）
└── .cangjie\capabilities\   # 阶段 2 起创建
```

- 提取质量门：空文本页 = 0（纯扫描件需先 OCR，勿直接蒸馏）
- 中文路径的素材用 Python 处理，**不要在 PowerShell .ps1 里写中文路径**（GBK 乱码，已踩坑）

## 2. 流水线（阶段 0 → 5）

| 阶段 | 动作 | 产出 | 质量门 |
|---|---|---|---|
| 0 整书理解 | 通读全文（≤100KB 可直读），Adler 四步 + **原书关键任务清单（带页码）** | BOOK_OVERVIEW.md | **用户确认骨架后才进阶段 1** |
| 1 并行提取 | 一次 spawn 5 个 sub-agent（框架全量/原则全量/案例检索/反例检索/术语检索）；失败改串行 | candidates/ 五类 | 每个提取器附 task 覆盖率自检 |
| 1.5 三重验证 | V1 来源充分 / V2 新输入演练 / V3 任务增益；分流 verified/reference/needs_review/rejected | verified.md + coverage-audit.md + needs-review.md + references.md | 对照 task 清单 15/15（按当次书）；提取器的"矛盾断言"必须复核原文再裁决 |
| 1.6 晋级门 | 五判据（前3必须+后2至少1）；合并同契约单元；入口软预算 **8（含1路由入口）** | destinations.json | 未晋级不删除，全部保留为 router 卡 |
| 2 能力卡 | 六段 R/I/A1/A2/E/B；元数据进 verified.yaml（**card 字段用 slug 命名**） | cards/*.md + verified.yaml | A1 不冒充书中案例；E 段有判停点 |
| 3 链接 | also_read **填 slug 不填 capability_id**（编译器按 slug 生成引用——首例踩坑）；GLOSSARY 落位 book/ | verified.yaml + GLOSSARY.md + book/{glossary,overview}.md | 关系数 8-15 条，不硬造 |
| 4 压力测试 | 独立 sub-agent 盲测：每能力 ≥2 should + ≥2 诱饵（**含跨能力混淆**）+ edge；router 测可达；代表任务实测 | test-prompts.json + test-results.md | 诱饵零失误；实测每能力 1 正常 + 1 边界 |
| 5 编译交付 | DIGEST.md → `cangjie.py compile --bundle <capabilities> --out dist --output single --yes` | dist/（原子发布） | 发布门全绿才算完成 |

## 3. 输出模式决策

- 默认 **single**（single-first：1 个 Skill 内含全部能力卡，按意图路由加载）
- 出现以下证据时改 pack 或拆分：用户实际使用中反复要求某能力独立触发（`cangjie.py replan-output --dry-run` 预览）
- 编译 auto 模式会停在决策报告要求确认——**授权 single-first 后直接 `--output single --yes`**

## 4. 已知坑（首例实录，必读）

| 坑 | 症状 | 规避 |
|---|---|---|
| also_read 填 capability_id | 发布门 14 个 broken-ref，staging 不发布 | also_read 一律填 slug（见阶段 3） |
| .ps1 中文路径乱码 | 脚本报路径不存在 / 搜索假 0 命中 | 中文路径一律用 Python |
| 盲测 agent 被取消 | 并行 spawn 全部 cancelled | 重试一次；仍失败按 skill 降级串行 |
| 容器刚起就健康检查 | 全部 000/0 | 部署脚本 curl 轮询等 200 再查（已内置） |
| 纯文本提取丢视觉差异 | 原文符号歧义（如状态码两条 1:01） | 如实标 needs-review + Boundary，不脑补 |

## 5. 收尾（每门课完成后）

1. `dist\` 复制到 `C:\Users\Administrator\.agents\skills\<课程slug>\`（全局技能库）
2. **门户成果页发布**（关键步，缺此步门户只有"已蒸馏"标签没有实际内容）：
   在 `.cangjie\publish_distilled.py` 的 `DISTILLED_BOOKS` 注册 `课程code: 工作区路径`
   → `build_comm_portal.py` → `publish_distilled.py` → `verify_comm_portal.py` → 部署
   产物：课程子站 index（能力卡目录）+ 15 张能力卡页 + digest/glossary/overview
3. 门户状态同步：对应课程 `distill_status="done"`（首页进度自动 +1）
4. PIPELINE_STATE.md 归档；蒸馏中间产物（candidates/verified.md 等）保留审计
5. 下门课优先级建议按"页数薄→厚"练手排序，或按售后报障频率定

## 6. 首例指标（作为后续基线）

- OXOCXTE107EN：218 页 → 138 条候选 → 29 verified → 15 能力（7 promoted + 8 router）
- 压力测试：触发 34/35（1 近邻可接受）、诱饵 0 失败、可达 8/8、实测 3/3
- 全程一个会话内完成；主要耗时在阶段 1 并行提取（5 agent ≈ 8 分钟）与阶段 2 写卡
