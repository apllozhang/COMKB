# otccxte150en 判卷报告（blind-results 对比 test-prompts.json）

## 汇总

| 类型 | 通过 | 总数 | 得分 |
|---|---|---|---|
| should_trigger | 26 | 26 | 26/26 |
| should_not_trigger | 8 | 10 | 8/10 |
| edge_case | 5 | 5 | 5/5 |
| **总计** | **39** | **41** | **39/41（95.1%）** |

## 逐类结论

- should_trigger 26 条全部命中预期 slug，无偏差。
- should_not_trigger 10 条诱饵中 8 条通过：2 条命中预期"另一能力"前置确认（bait-script-01/bait-script-02 等路由型全中）、2 条超范围题（bait-sql-01、bait-lang-01）盲判 none 命中；2 条 fail（见明细）。
- edge_case 5 条均路由合理：IDLE/COM 互斥、IAA 仅外部呼入、空列表再分发次数、连接串安全、DSN 拼写笔误，分别落在组合规则、Call Tag、重定向、外部数据库查询四个能力上，按"路由合理即 pass"计。

## Fail 明细

### bait-direct-01（should_not_trigger）
- 预期：属普通 CCD 队列与兜底语义，应激活 acr-redirect-redistribution，不应激活 acr-direct-call-dica。
- 盲判：acr-ccd-matrix-foundation
- 偏差分析：盲判把"普通 Pilot 全忙"归到普通链路（地基能力），既未命中被禁项 direct-call-dica（这点规避对了），也未命中预期项 redirect-redistribution。按判卷规则，"应激活另一能力"的诱饵必须命中那个另一能力才算 pass，选了第三个能力即不满足。从知识归属看答案键更有理："全忙之后去哪（转总机/Blockage/Redirection）"是兜底语义，归重定向能力，"普通链路"只是场景背景，属近失。

### bait-intdb-01（should_not_trigger）
- 预期：应转 acr-database-query-routing（外部库方案，内部库 4000 条上限），不应停留在 acr-internal-database-routing 当作可行。
- 盲判：acr-internal-database-routing
- 偏差分析：盲判命中被禁止能力，fail。盲判思路是"先查内部库容量约束再议外部库"，而 4000 条上限恰好写在内部库能力的目录里，这个先查证的直觉本身符合工程师习惯；答案键则要求落点直接跳到外部库方案。偏差实质：盲判停在"确认不可行"，预期是"给出可行替代"。判 fail 成立，但此题暴露口径问题——"5 万条放内部库行不行"是确认类提问，"先在内部库能力里确认上限，再转外部库"是两段动作，键只认第二段落点，建议键里把"确认+转介"两段都算过。
