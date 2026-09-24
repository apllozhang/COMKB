# 盲测验卷报告 · otccxte100en（otcc-standard-starter）

- 盲判依据：blind-input.json 的 13 项能力目录，盲判阶段未读答案；判卷阶段与 test-prompts.json 的 40 条 test_case 逐条对比。
- 判卷规则：should_trigger 盲判 slug 与预期一致；should_not_trigger 不得命中被禁能力、命中"应激活的另一能力"即过；edge_case 路由合理或声明边界即过。

## 汇总

| 类别 | 结果 |
|---|---|
| should_trigger | 26/26 |
| should_not_trigger（诱饵） | 10/10 |
| edge_case | 4/4 |
| 总计 | 40/40 |

## 诱饵明细（10 条全过）

| id | 盲判 | 预期 | 判定 |
|---|---|---|---|
| bait-rules-01 | otcc-object-tuning | 应激活 object-tuning（Queuing overflow），禁当作 routing-distribution-rules | pass |
| bait-tune-01 | otcc-agent-supervisor-onboarding | 应激活 onboarding（前缀/COS），禁 object-tuning | pass |
| bait-vg-01 | otcc-queue-experience | 应激活 queue-experience（518 变量段），不应只 voice-guides | pass |
| bait-mon-01 | otcc-object-tuning | 应激活 object-tuning（阈值与三色判定），禁停留 monitoring-statistics | pass |
| bait-dc-01 | otcc-supervisor-features | 应激活 supervisor-features（通用转发），禁 direct-calls-emergency | pass |
| bait-sp-01 | otcc-direct-calls-emergency | 应激活 direct-calls（direct call pilot），禁 statistic-pilot | pass |
| bait-matrix-01 | otcc-queue-experience | 应激活 queue-experience（IAA 5 层 4 选项 8 树上限），禁 matrix-foundation 承诺可做 | pass |
| bait-out-01 | none | 超范围（ACR 技能路由书外），应声明边界 | pass，盲判 none |
| bait-out-02 | none | 超范围（话务建模书外） | pass，盲判 none |
| bait-out-03 | none | 超范围（Multisite CCS 本书不教），禁 ccs-installation 承诺可做 | pass，盲判 none |

## edge 明细（4 条全过）

| id | 盲判 | 预期要点 | 判定 |
|---|---|---|---|
| edge-lang-01 | otcc-multilanguage-calendar | 语言槽按目标库核对，两处口径并存 | pass，路由正确 |
| edge-pwd-01 | otcc-lab-connectivity | 双口径（Superuser2580* / p153 mtcl），实验按能登录为准 | pass，实验口径归链路打通能力，合理 |
| edge-cmd-01 | otcc-ccd-matrix-foundation | acdsup 为准、现场以实际存在为准 | pass，矩阵验证命令归属正确 |
| edge-abc-01 | otcc-lab-connectivity | R100/N1 双口径，行为一致（access 必建），hybvisu 实测 | pass |

## 失败清单

无。

## 备注

- should_trigger 26 条盲判与预期逐一对应，无歧义项。
- 10 条诱饵中 7 条为"应激活另一能力"、3 条为超范围 none，盲判全部落点正确：易混对（routing vs tuning、tuning vs onboarding、monitoring vs tuning、direct-call vs statistic-pilot、matrix vs queue-experience）均按目录描述中的关键语义区分开。
