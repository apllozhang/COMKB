# 8770xte201en 判卷报告（blind-results vs test-prompts）

## 汇总

| 类型 | 通过 | 总数 | 正确率 |
|---|---|---|---|
| should_trigger | 24 | 25 | 96% |
| should_not_trigger | 8 | 8 | 100% |
| edge_case | 5 | 5 | 100% |
| **总计** | **37** | **38** | **97.4%** |

## fail 明细

### should-report-02
- 预期：ovbill-reporting（Daily Station Traffic 属累计报表，累计计数器未算先补算 / Total calculation）
- 盲判：ovbill-traffic-tracking
- 偏差分析：题面报表名含 "Traffic"，盲判把它当成 pmm 流量分析数据源问题路由到了流量分析域。而能力目录里"累计报表空表先 Total calculation"归在 ovbill-reporting 描述中，"空表排障"字样只出现在 ovbill-voip-monitoring，目录没有把"Daily Station Traffic"与"累计报表"显式关联，形成描述覆盖盲区。属路由偏差，判 fail。

## 说明
- should-codebook-01：盲判 slug 命中 ovbill-codebook-migration 即 pass；盲判理由里写的"二次导出"与答案口径".itl 节点名不匹配"不同，但判卷以 slug 一致为准，不影响结果。
- edge-multi-01：盲判 ovbill-ticket-pipeline，答案口径为边界声明（PCS ID 换算/同步开关可引用、组网结论不虚构），PCS 参数确在票据管道（收集器、PCS）与纳管两处出现，路由合理，按 edge 规则 pass。
- edge-lab-01：盲判 none，属声明边界（目录无对应能力，口令治理属客户侧安全），按 edge 规则 pass。
