# ENTPX 盲判判卷报告（blind-results.md 对比 test-prompts.json）

## 汇总

| 类型 | 通过 / 总数 |
|---|---|
| should_trigger | 24/24 |
| should_not_trigger | 9/10 |
| edge_case | 4/4 |
| **总计** | **37/38** |

- should_trigger：24 条全部命中预期能力，无偏差。
- should_not_trigger：10 条诱饵中 9 条命中预期"另一能力"或正确判 none；1 条失败（见明细）。
- edge_case：4 条路由均合理（rtr-licensing / pod-licensing / oxe-v-deployment / gas-delivery），符合"路由合理或声明边界即 pass"。

## Fail 明细

### bait-license-01（should_not_trigger）— FAIL
- 预期：应激活 entload-pod-licensing（OPEX 许可链排障，eqstat/事件 402/5816），不按硬件故障处理。
- 盲判：none（判超范围）。
- 偏差分析："话机注册 No license available"在能力目录里没有直接对应词条——pod-licensing 的目录描述只写了订阅项、三种消耗、spadmin 对账、C2P，未点名话机注册许可链（eqstat/402/5816）；rtr 只写资格期，oxe-v 只写 OMS Lock 384/385。盲判依据目录无法把话机许可报错关联到 OPEX 订阅链，只能判 none。这是目录描述颗粒度缺口导致的漏判：预期答案依赖的能力线索（eqstat/事件号）没有外显到目录，属于出题与目录不同步，判卷按规则记 fail，但根因建议回修 pod-licensing 的目录描述（补一句"OPEX 许可链排障：eqstat、事件 402/5816"即可闭合）。

## 逐条对照（简表）

| id | 盲判 | 预期 | 结果 |
|---|---|---|---|
| should-sot-01 | entload-sot-installation | 同 | pass |
| should-sot-02 | entload-sot-installation | 同 | pass |
| should-cs-01 | entload-cs-loading | 同 | pass |
| should-cs-02 | entload-cs-loading | 同 | pass |
| should-patch-01 | entload-patch-management | 同 | pass |
| should-patch-02 | entload-patch-management | 同 | pass |
| should-oxev-01 | entload-oxe-v-deployment | 同 | pass |
| should-oxev-02 | entload-oxe-v-deployment | 同 | pass |
| should-gas-01 | entload-gas-delivery | 同 | pass |
| should-gas-02 | entload-gas-delivery | 同 | pass |
| should-cloud-01 | entload-cloud-connect | 同 | pass |
| should-cloud-02 | entload-cloud-connect | 同 | pass |
| should-rtr-01 | entload-rtr-licensing | 同 | pass |
| should-rtr-02 | entload-rtr-licensing | 同 | pass |
| should-pod-01 | entload-pod-licensing | 同 | pass |
| should-pod-02 | entload-pod-licensing | 同 | pass |
| should-dist-01 | entload-distributor-loading | 同 | pass |
| should-dist-02 | entload-distributor-loading | 同 | pass |
| should-media-01 | entload-sot-media | 同 | pass |
| should-media-02 | entload-sot-media | 同 | pass |
| should-gasops-01 | entload-gas-ops | 同 | pass |
| should-gasops-02 | entload-gas-ops | 同 | pass |
| should-fleet-01 | entload-fleet-dashboard | 同 | pass |
| should-fleet-02 | entload-fleet-dashboard | 同 | pass |
| bait-sot-01 | entload-sot-media | 应激活 sot-media | pass |
| bait-cs-01 | entload-distributor-loading | 应激活 distributor-loading | pass |
| bait-patch-01 | entload-sot-installation | 应落在 sot-installation 边界（单任务） | pass |
| bait-oxev-01 | entload-oxe-v-deployment | 应激活 oxe-v-deployment 并纠正 FlexLM | pass |
| bait-gas-01 | entload-gas-ops | 应激活 gas-ops | pass |
| bait-cloud-01 | entload-rtr-licensing | 应激活 rtr-licensing | pass |
| bait-rtr-01 | entload-rtr-licensing | 应激活 rtr-licensing（互斥） | pass |
| bait-pod-01 | entload-pod-licensing | 应激活 pod-licensing | pass |
| bait-license-01 | none | 应激活 pod-licensing | **fail** |
| bait-scope-01 | none | 超范围 none | pass |
| edge-rtr-01 | entload-rtr-licensing | 边界回答，路由合理 | pass |
| edge-pod-01 | entload-pod-licensing | 边界回答，路由合理 | pass |
| edge-oxev-01 | entload-oxe-v-deployment | 边界回答，路由合理 | pass |
| edge-gas-01 | entload-gas-delivery | 边界回答（硬件 RAID 红线），路由合理 | pass |
