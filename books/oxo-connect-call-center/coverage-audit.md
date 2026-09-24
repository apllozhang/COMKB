# coverage-audit.md — 原书关键任务覆盖审计（阶段 1.5）

> 核查基准: BOOK_OVERVIEW.md 的 task-01~task-15（不从旧 verified 反推）
> 去向编码: verified 单元号（进阶段 1.6）/ reference / needs_review

| task_id | 任务 | 原文位置 | 候选 | decision | 最终去向 |
|---|---|---|---|---|---|
| task-01 | OMC 安装与首连 | p54-64 | f11 | verified | 阶段 1.6 |
| task-02 | IP 规划修改 | p65-68 | f12 | verified | 阶段 1.6 |
| task-03 | 基础 ACD 搭建 | p43-48, p69-77, p80-84 | f08 + f09 + f10 | verified | 阶段 1.6（三候选合并为一项能力） |
| task-04 | 六场景呼入处理 | p36-42 | f01-f07 | verified | 阶段 1.6（总框架+六场景合一） |
| task-05 | 特征化路由表 | p86-88, p115-116 | f13 + f14 | verified | 阶段 1.6（决策+规程合一） |
| task-06 | 搜索模式与无应答 | p95, p97, p109-111 | f15 + f16 | verified | 阶段 1.6 |
| task-07 | 队列管理 | p93-94, p112 | f17 + f18（流程见 f03/f04） | verified | 阶段 1.6 |
| task-08 | 时段与例外日 | p100, p108 | f20 | verified | 阶段 1.6 |
| task-09 | Login/Logout 与状态码 | p117-123 | f21 + f22 | verified | 阶段 1.6 |
| task-10 | Multi-Secretary | p124-146 | f24（显示框架 f23 归并） | verified | 阶段 1.6 |
| task-11 | Supervisor 应用 | p147-165 | f25 + f26 | verified | 阶段 1.6 |
| task-12 | Agent 应用 | p99, p166-184 | f27 | verified | 阶段 1.6 |
| task-13 | Statistics 应用 | p185-209 | f29 | verified | 阶段 1.6 |
| task-14 | DTMF 客户识别弹屏 | p101-102 | f28 | verified | 阶段 1.6 |
| task-15 | 语音提示定制 | p104-105, p135-136 | f30 | verified | 阶段 1.6 |
| （任务外） | 组间溢出机制 | p96 | f19 | needs_review | 缺溢出定时器配置入口，见 needs-review.md |
| （任务外） | 收尾恢复出厂 | p211 | f31 | reference | 作为各规程的边界提示保留 |

## 覆盖结论

- **15/15 任务全部有 verified 候选覆盖**，无遗漏任务。
- task 清单外新增 5 个有价值单元：f09（向导生成物，归入 task-03 能力）、f19（溢出，needs_review）、f23（显示模式，归入 task-10 能力）、f26（子状态，归入 task-11 能力）、f31（收尾，reference）。
- 部分覆盖说明：task-09 的 Login/Logout 只有讲义无独立实验（case-extractor 已标注）；task-14 无端到端 DTMF 弹屏实测步骤——两者机制完整，V2 以 walkthrough 通过，实验缺口记入 Boundary。
- 支撑材料归并去向：principle 62 条 → 对应单元证据（公式 f17/f18、规则 f13/f14/f21、数值 f08/f20/f29）；case 24 条 → 各单元 A1；counter-example 21 条 → 各单元 B（其中"p184 矛盾"断言撤销）；glossary 60 条 → GLOSSARY.md（阶段 3）。
