# PIPELINE_STATE — rainxte001en (RAINXTE001EN, 251 页)

> 断点状态文件。每阶段完成后更新。字眼口径：对外与产物一律用"文档整理/入库"，不出现工艺专名。

## 基本信息
- 书: Rainbow OXO Connect (RAINXTE001EN Edition 13, R6.3/SP149)
- PDF: F:\ALE知识库\Training Offer by Job Function\CBD\Cloud\RAINXTE001EN.pdf
- 全文: source_fulltext.txt（251 页，0 空文本页，118 KB / 4131 行）
- 用户授权: 2026-09-23 "现在开始"（全流程连续执行，骨架要点已展示）

## 进度

| 阶段 | 状态 | 产出 |
|---|---|---|
| 前置检查 | ✅ | doctor PASS；v2.5.0-3-g3adf9e6（0 落后） |
| 工作区 + 提取 | ✅ | source_fulltext.txt |
| 0 整书理解 | ✅ | BOOK_OVERVIEW.md（9 骨架 / 17 术语 / 18 任务） |
| 1 五路并行提取 | ✅ | candidates/ 五类 224 条（f44/p50/c14/n54/g62） |
| 1.5 三重验证 | ✅ | verified.md（40 verified/3 ref）+ coverage-audit（18/18）+ needs-review（6 项）+ references.md |
| 1.6 晋级门 | ✅ | destinations.json（12 单元：8 promoted + 4 router） |
| 2 能力卡 | ✅ | cards/ 12 张六段卡 + verified.yaml（bundle.rainbow-oxo-connect） |
| 3 链接 | ✅ | also_read 15 条（slug）+ book/glossary.md（62 术语六域）+ book/overview.md |
| 4 压力测试 | ✅ | test-prompts.json（40 条）+ test-results.md：触发 40/40、诱饵 0 失误、边界 4/4、实测 3/3 |
| 5 编译交付 | ✅ | dist/（single，12 卡，发布门通过 run-20260923-225420-ba656c）→ 安装 C:\Users\Administrator\.agents\skills\rainbow-oxo-connect\ |
| 收尾发布 | ✅ | publish_rainxte001.py 注册 → 本地校验 PASS（62 页 0 断链）→ 部署 103:8900（13 项健康检查全过）→ 全站字眼扫描 0 命中 |

## 收尾记录（2026-09-23）

- 门户：/courses/rainxte001en/（index + digest + glossary 62 术语 + overview + 12 技能页）；首页 status-done 徽标已点亮
- 技能安装：rainbow-oxo-connect（SKILL.md + references/ 12 卡 + index/cheatsheet/glossary/overview）
- 本次踩坑补充：verified.yaml 里 router 卡的 status 必须写 active（promoted/router 区分在 promotion.destination）——写错会导致编译发布门 broken-ref
- 顺序纪律：build_comm_portal.py（清空重建站点）→ publish_*.py（两本都要跑）→ verify_comm_portal.py → 部署
- 下门课建议：DECTXTE200EN（298 页，OXE DECT 组网，售后高频）或 RAINXTE003EN（314 页，Rainbow for OXE）

## 排版修复轮（2026-09-23，用户提醒老问题后）

- 浏览器实检 5 类页面（首页/术语表/任务表/精华文/能力卡），发现并修复：
  1. gateway-planning 卡容量对照被写成数字链散文 → 改真表格（3 列 8 行）+ 终端形态表格
  2. 约 8 张卡的 A1 实验段一行 200+ 字 → 全部拆为编号步骤列表
  3. attendant-supervision 话务台规格段落 → 改规格对照小表
  4. company-subscription 8 种订阅行内列举 → 改 3 列表
  5. omc-onboarding IP 参数 → 改设备/PC 参数对照表
  6. DIGEST 容量数字链/维护八抓手/终端形态/三个数字 → 全部表格化；重 bullet 拆薄
- 原则沉淀：数字对照（≥3 组）必须表格；A1 实验段一律编号步骤；菜单路径箭头链保留（本征形态）
- 复验：重编译（快照 pre-run-20260923-231413-2fd144）→ 技能库同步 → 门户校验 PASS（62 页 0 断链）→ 部署 13 项检查全过 → 浏览器复验容量表/digest 通过

## 排版修复轮 2（2026-09-23，用户截图"这种你都不换行"）

- 根因：markdown 列表/表格前缺空行，python-markdown 不解析 → "线一四步"、12 张卡的"判停点："列表全部挤成一段
- 修复：fix_blank.py 批量插入 17 处空行（段落行与列表行之间）；表格分隔行后接数据行是合法语法不处理
- 工具沉淀：scan_blank.py（扫描）+ fix_blank.py（修复）在 .cangjie/，每本书发布前必跑
- 完整发布链：改源卡 → compile → robocopy 技能库 → publish_rainxte001 → verify → deploy → 浏览器复验
- 复验：omc-onboarding 卡线一/线二编号列表正常、判停点 bullet 正常、B 段边界正常；门户 PASS + 部署健康检查全过

## 阶段 1 记录
- 提取器: 框架/原则/案例/反例/术语 五路并行
- 产出: candidates/{structure,principles,cases,counterevidence,terms}.md

## 已知坑提醒（本书执行时遵守）
- also_read 填 slug
- 中文路径一律 Python，不写 .ps1
- 表格数字（容量表 20/50 上限）必须逐格对照原文，不脑补
