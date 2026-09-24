# openxte225en 判卷报告

## 汇总

| 类型 | 通过 | 总数 | 得分 |
|---|---|---|---|
| should_trigger | 24 | 24 | 100% |
| should_not_trigger | 8 | 8 | 100% |
| edge_case | 4 | 4 | 100% |
| **总计** | **36** | **36** | **100%** |

## 判卷明细

### should_trigger（24/24）
全部命中：dmz×2、cert×2、otset×2、sbc×2、rp×2、pc×2、sp×2、iph×2、client×2、mode×2、vm×2、lab×2，盲判 slug 与预期逐一一致。

### should_not_trigger（8/8）
- bait-dmz-01：盲判 none，符合"VPN 细节超书外、应声明边界"。
- bait-cert-01：盲判 none，符合"正式 PKI 流程书外"。
- bait-sbc-01：盲判 none，符合"容量与 CAC 数值书内缺位"。
- bait-pc-01：盲判 otm-otc-pc-modes，命中预期"另一能力"，未触碰被禁止的 otm-client-access-profiles。
- bait-rp-01：盲判 otm-otsbc-deployment，命中预期，避开 otm-reverse-proxy。
- bait-sp-01：盲判 otm-iphone-apns，命中预期，避开 otm-smartphone-provisioning。
- bait-otset-01：盲判 otm-reverse-proxy，命中预期，避开 otm-ot-server-settings。
- bait-mode-01：盲判 otm-smartphone-modes，命中预期，避开 otm-smartphone-provisioning。

### edge_case（4/4）
- edge-version-01：路由 otm-smartphone-provisioning（R2.6 单设备版本分界所在），合理。
- edge-nomadic-01：路由 otm-otc-pc-modes（游牧建池公式所在），合理。
- edge-dialfrom-01：路由 otm-client-access-profiles，与预期特例口径完全对应。
- edge-labcred-01：路由 otm-lab-dialtest，与"实验口径不复用生产"红线对应。

## 失败清单

无。
