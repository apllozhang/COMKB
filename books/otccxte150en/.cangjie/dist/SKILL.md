---
name: otcc-advanced-call-routing
description: |
  OTCC 标准版高级呼叫路由（ACR）的交付与排障支持：基础 CCD 矩阵地基（双 Pilot、等待房间、坐席技能档案）、ASM 脚本编写调试工具链、九种路由规则及组合语义（APPLY 链式过滤）、 坐席直拨融合（DICA）、内部数据库三键路由、Call Tag 传递、多语言引导、IQUEUE/LIST 等高级构件、过滤器统计、外部 ASM 部署割接与双机热备、外部数据库 SQL 查询与 LCA 持久化。 适用于 OTCC Standard Edition 的 ACR 配置、脚本、排障与方案问答；容量测算方法、多节点组网与安全基线不在原书范围内（见 out_of_scope）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.otcc-advanced-call-routing
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# OmniTouch Contact Center Standard Edition — Advanced Call Routing (Participant's Guide, Issue 01) — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 规模测算方法（话务量、Erlang、坐席数规划）——原书只给 p18 容量上限表，"该建多少"在书外
- MS SQL Server/Access/SSMS 界面操作细节与语音引导录制内容——通用软件与环境操作，书内仅给与 ACR 相关的字段、账号与过程约定
- 安全基线（强口令、最小授权、传输加密、SQL 注入防护）——原书系统性缺席，仅有实验口令口径
- 多节点组网 ACR 细节与混合链路以外的网络规划、OXE 侧冗余与脚本版本管理

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. ACR 的本质是脚本选坐席：CCS 内嵌编辑器写脚本（.scr 源/.alb 编译），ASM 服务器解释执行并按呼叫特征返回动态坐席列表；选人归 ASM，呼叫控制仍在 CCD 矩阵
2. 分发三步固定：呼叫特征化关联档案进 Pilot，ASM 算列表（动态组），呼叫带列表进等待房间；房间与队列互斥且房间不按 FIFO
3. 规则分两族：单用规则（LCA/Redirection/Redistribution/IVR）独占 APPLY；可组合规则（名单/ISM/IDLE/COM）可串接；单 APPLY 链式过滤，多 APPLY 第一个失效；IDLE 与 COM 互斥
4. 空列表必有两式兜底：Redirection 转号或 Redistribution 退下一路由方向，全无方向落 Blockage；脚本空列表重试原书两处口径 20/21 次
5. 呼叫选择统一排座次：优先级 0-9（0 最高），再按 ACR Actual Waiting 决定 ISM 成本与实际等待谁先；等待队列里普通 CCD 呼叫 ISM 成本为无穷（ACR 默认插队）
6. 外部化三线：外部 ASM 角色与内部 alb 一致（割接先 asm_on_dhs=0 停内部）、双机 Main/Stand-By 自动复制；外部库走 32 位 ODBC 加 167 号许可，存储过程可把 LCA 落库抗重启
7. 实验环境口径：教材对象编号（3xXXX）、账号口令、IP 仅限实验；引用容量数字必须标注原书 Issue 01 口径

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 编写并激活 ACR 脚本；用 Debugger 调试脚本；配置 LIT/PLTR 坐席排序；脚本里处理字符串与屏显；write and debug ACR script | references/capabilities/acr-script-editor-fundamentals.md | references/capabilities/acr-rule-combination-advanced.md |
| 搭建 CCD/ACR 基础矩阵；配置 Pilot 路由与分发规则；建技能域与呼叫档案；配置混合链路；build CCD matrix for ACR | references/capabilities/acr-ccd-matrix-foundation.md | references/capabilities/acr-script-editor-fundamentals.md、references/capabilities/acr-filter-statistics.md |
| 配置空坐席列表兜底；呼叫转接外部号码；再分发到语音引导队列；排查呼叫进封锁；redirection and redistribution rule | references/capabilities/acr-redirect-redistribution.md | references/capabilities/acr-script-editor-fundamentals.md |
| 实现直拨等原坐席；配置私有号与直拨 Pilot；停用/启用坐席直拨；编写 CALL_TYPE 分支脚本；direct call with ACR | references/capabilities/acr-direct-call-dica.md | references/capabilities/acr-internal-database-routing.md |
| 按主叫号定制路由；按 Call Tag 区段配名单；直拨场景按坐席号查档案；配置内部数据库条目；internal database routing | references/capabilities/acr-internal-database-routing.md | references/capabilities/acr-call-tag-transfer.md、references/capabilities/acr-direct-call-dica.md |
| 组合多个 ACR 规则；编程等待停放体验（IQUEUE）；动态拼装坐席/技能列表；调优 CCD 与 ACR 混合呼叫选择；combine ACR rules and APPLY | references/capabilities/acr-rule-combination-advanced.md | references/capabilities/acr-script-editor-fundamentals.md、references/capabilities/acr-list-rules.md |
| 部署外部 ASM 服务器；从内部 ASM 割接；迁移脚本到外部 ASM；部署 Main/Stand-By 双机；external ASM deployment | references/capabilities/acr-asm-deployment.md | references/capabilities/acr-database-query-routing.md |
| 脚本查询外部数据库；配置 ODBC 数据源；调用存储过程读写；实现 LCA 持久化；external database SQL routing | references/capabilities/acr-database-query-routing.md | references/capabilities/acr-asm-deployment.md |
| 建授权/非授权名单；名单按主叫号或标签索引；动态名单传入规则；authorized and unauthorized list | references/capabilities/acr-list-rules.md | references/capabilities/acr-rule-combination-advanced.md |
| 用 IAA 采集客户号作标签；统计 Pilot 打标；排查转发链标签覆盖；call tag generation and transfer | references/capabilities/acr-call-tag-transfer.md | references/capabilities/acr-internal-database-routing.md、references/capabilities/acr-multilanguage-voiceguide.md |
| 配置多语言引导；按客户语言选坐席；排查播报语言错误；multi-language voice guide | references/capabilities/acr-multilanguage-voiceguide.md | references/capabilities/acr-ccd-matrix-foundation.md |
| 建过滤器与超组；出实时监控与 Excel 报表；排查报表口径不符；filter and statistics reporting | references/capabilities/acr-filter-statistics.md | — |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 需要容量测算或坐席数规划 → 指向 OXE 侧配套文档与 Feature List，不以 p18 上限表冒充测算方法
- 数据库安装、界面点选、录音制作类请求 → 声明属通用技能/环境操作，只保留 ACR 相关约定
- 生产环境安全设计 → 按实验口径警示并建议叠加安全基线（整改方向为推断，原书未讨论）
- 版本敏感判定（asm_ag_free_duration 最低 l2.300.32.a、patchIdle 已废弃）→ 按 needs-review nr-08 口径如实说明
