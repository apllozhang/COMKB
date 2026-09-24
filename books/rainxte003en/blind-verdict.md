# rainxte003en 判卷报告（blind-results.md vs test-prompts.json）

## 汇总

| 类型 | 通过/总数 | 通过率 |
|---|---|---|
| should_trigger | 26/26 | 100% |
| should_not_trigger | 8/9 | 88.9% |
| edge_case | 5/5 | 100% |
| 总计 | 39/40 | 97.5% |

## 逐条判卷明细

| id | 类型 | 预期 | 盲判 | 结果 |
|---|---|---|---|---|
| should-company-01 | should_trigger | rxe-company-subscription | rxe-company-subscription | pass |
| should-company-02 | should_trigger | rxe-company-subscription | rxe-company-subscription | pass |
| should-agent-01 | should_trigger | rxe-agent-onboarding | rxe-agent-onboarding | pass |
| should-agent-02 | should_trigger | rxe-agent-onboarding | rxe-agent-onboarding | pass |
| should-member-01 | should_trigger | rxe-member-lifecycle | rxe-member-lifecycle | pass |
| should-member-02 | should_trigger | rxe-member-lifecycle | rxe-member-lifecycle | pass |
| should-routing-01 | should_trigger | rxe-routing-rex | rxe-routing-rex | pass |
| should-routing-02 | should_trigger | rxe-routing-rex | rxe-routing-rex | pass |
| should-deploy-01 | should_trigger | rxe-webrtc-gateway-deployment | rxe-webrtc-gateway-deployment | pass |
| should-deploy-02 | should_trigger | rxe-webrtc-gateway-deployment | rxe-webrtc-gateway-deployment | pass |
| should-oxecfg-01 | should_trigger | rxe-oxe-gateway-config | rxe-oxe-gateway-config | pass |
| should-oxecfg-02 | should_trigger | rxe-oxe-gateway-config | rxe-oxe-gateway-config | pass |
| should-pool-01 | should_trigger | rxe-gateway-pool-sizing | rxe-gateway-pool-sizing | pass |
| should-pool-02 | should_trigger | rxe-gateway-pool-sizing | rxe-gateway-pool-sizing | pass |
| should-teams-01 | should_trigger | rxe-teams-integration | rxe-teams-integration | pass |
| should-teams-02 | should_trigger | rxe-teams-integration | rxe-teams-integration | pass |
| should-rcc-01 | should_trigger | rxe-rcc-association | rxe-rcc-association | pass |
| should-att-01 | should_trigger | rxe-attendant-consoles | rxe-attendant-consoles | pass |
| should-att-02 | should_trigger | rxe-attendant-consoles | rxe-attendant-consoles | pass |
| should-maint-01 | should_trigger | rxe-maintenance-support | rxe-maintenance-support | pass |
| should-maint-02 | should_trigger | rxe-maintenance-support | rxe-maintenance-support | pass |
| should-net-01 | should_trigger | rxe-network-readiness | rxe-network-readiness | pass |
| should-net-02 | should_trigger | rxe-network-readiness | rxe-network-readiness | pass |
| should-lab-01 | should_trigger | rxe-lab-pod-setup | rxe-lab-pod-setup | pass |
| should-lab-02 | should_trigger | rxe-lab-pod-setup | rxe-lab-pod-setup | pass |
| should-agent-03 | should_trigger | rxe-agent-onboarding | rxe-agent-onboarding | pass |
| bait-company-01 | should_not_trigger | 成员生命周期+分机关联组合，禁 rxe-company-subscription | rxe-member-lifecycle | pass（命中组合中的开户能力，未命中被禁能力） |
| bait-agent-01 | should_not_trigger | 应 rxe-oxe-gateway-config，禁 rxe-agent-onboarding | rxe-oxe-gateway-config | pass |
| bait-deploy-01 | should_not_trigger | 应 rxe-gateway-pool-sizing，禁 rxe-webrtc-gateway-deployment | rxe-gateway-pool-sizing | pass |
| bait-pool-01 | should_not_trigger | 应 rxe-webrtc-gateway-deployment，禁停留 rxe-gateway-pool-sizing | rxe-webrtc-gateway-deployment | pass |
| bait-routing-01 | should_not_trigger | 应 rxe-attendant-consoles（禁 multi-line），禁照搬 rxe-routing-rex | rxe-attendant-consoles | pass |
| bait-teams-01 | should_not_trigger | 超范围（Teams 租户策略），禁 rxe-teams-integration，应声明边界 | none | pass |
| bait-rcc-01 | should_not_trigger | 应转网关规划/部署，禁停留在 rxe-rcc-association | rxe-routing-rex | fail |
| bait-maint-01 | should_not_trigger | 应 rxe-agent-onboarding，禁 rxe-maintenance-support | rxe-agent-onboarding | pass |
| bait-net-01 | should_not_trigger | 应 rxe-agent-onboarding，禁停留 rxe-network-readiness | rxe-agent-onboarding | pass |
| edge-oxecfg-01 | edge_case | 按 G711 实验口径边界回答 | rxe-oxe-gateway-config | pass |
| edge-pool-01 | edge_case | 按并发流/用户数量纲区分回答 | rxe-gateway-pool-sizing | pass |
| edge-att-01 | edge_case | 按"话务台仅 PC+代接边界"回答 | rxe-attendant-consoles | pass |
| edge-routing-01 | edge_case | 按 DECT 特例边界回答（Virtual UA 路线） | rxe-routing-rex | pass |
| edge-lab-01 | edge_case | 按实验口径禁照搬边界回答 | rxe-lab-pod-setup | pass |

## fail 明细

### bait-rcc-01
- 预期：应转网关规划/部署（rxe-gateway-pool-sizing / rxe-webrtc-gateway-deployment），不应停留在 rxe-rcc-association 当作可解决
- 盲判：rxe-routing-rex
- 偏差分析：盲判避开了被禁止的 rxe-rcc-association（约束满足），并正确识别"RCC 音频在话机是形态属性"，走到四形态矩阵做形态决策——方向对但落点比预期少一跳，停在了"选哪个形态"的决策层，没有落到"网关规划/部署"这个实施能力。按判卷规则，诱饵题需命中预期"另一能力"才 pass，判 fail。属接近通过的边界偏差，非乱路由。
- 改进方向：两可处理——要么把 rxe-routing-rex 的目录描述补上"纯 REX/网关形态的落地入口指向网关部署与容量规划"，要么把该题预期放宽为"rxe-routing-rex 或网关规划/部署任一"。
