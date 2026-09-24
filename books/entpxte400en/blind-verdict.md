# entpxte400en 判卷报告（blind-results vs test-prompts）

## 汇总

| 类型 | 通过 | 总数 | 正确率 |
|---|---|---|---|
| should_trigger | 28 | 28 | 100% |
| should_not_trigger | 7 | 8 | 87.5% |
| edge_case | 4 | 4 | 100% |
| **总计** | **39** | **40** | **97.5%** |

## fail 明细

### bait-umc-01
- 预期：不应激活 ents-legacy-trunks-umc 当作可解决；UMC 明确排除多实体与话务台，应声明边界转本地图形工具（等价 none + 边界声明）
- 盲判：ents-legacy-trunks-umc
- 偏差分析：UMC 的排除清单确实写在 ents-legacy-trunks-umc 能力描述内，盲判按"问题域归属"路由到了该能力，属于"用含排除项的能力描述回答越界需求"的合理直觉。但出题口径是"命中被禁止的能力即 fail"——预期把这条视作超范围题（激活能力去解决 = 错）。判卷按规则执行：盲判命中被禁 slug，判 fail。这是"能力描述含排除项"与"排除项应触发拒绝路由"两种口径的碰撞点。

## 说明
- edge-disc-01：盲判 ents-barring-emergency（8 逻辑/256 真实鉴别符），答案机制为"真实鉴别符必须先建才能映射"（该约束字样在目录里挂在 ents-sip-trunk）。鉴别符体系横跨闭锁与 ARS 两域，路由到闭锁侧不算明显乱路由，按 edge 规则"不强求特定 slug"判 pass；若按 should_trigger 严格口径则会判 miss，此处按题面类型执行。
- bait-ha-01：盲判 none，与预期"超出 Starter 单机口径、声明边界"一致，pass。
