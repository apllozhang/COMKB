# dectxte200en 判卷报告（blind-results.md vs test-prompts.json）

## 汇总

| 类型 | 通过/总数 | 通过率 |
|---|---|---|
| should_trigger | 24/24 | 100% |
| should_not_trigger | 12/13 | 92.3% |
| edge_case | 3/3 | 100% |
| 总计 | 39/40 | 97.5% |

## 逐条判卷明细

| id | 类型 | 预期 | 盲判 | 结果 |
|---|---|---|---|---|
| should-pari-01 | should_trigger | dect-pari-identifier | dect-pari-identifier | pass |
| should-pari-02 | should_trigger | dect-pari-identifier | dect-pari-identifier | pass |
| should-select-01 | should_trigger | dect-product-selection | dect-product-selection | pass |
| should-select-02 | should_trigger | dect-product-selection | dect-product-selection | pass |
| should-deploy-01 | should_trigger | dect-ipxbs-deployment | dect-ipxbs-deployment | pass |
| should-deploy-02 | should_trigger | dect-ipxbs-deployment | dect-ipxbs-deployment | pass |
| should-sync-01 | should_trigger | dect-xbs-sync-topology | dect-xbs-sync-topology | pass |
| should-sync-02 | should_trigger | dect-xbs-sync-topology | dect-xbs-sync-topology | pass |
| should-hsreg-01 | should_trigger | dect-handset-registration | dect-handset-registration | pass |
| should-hsreg-02 | should_trigger | dect-handset-registration | dect-handset-registration | pass |
| should-mixed-01 | should_trigger | dect-mixed-mode | dect-mixed-mode | pass |
| should-mixed-02 | should_trigger | dect-mixed-mode | dect-mixed-mode | pass |
| should-rereg-01 | should_trigger | dect-auto-reregistration | dect-auto-reregistration | pass |
| should-rereg-02 | should_trigger | dect-auto-reregistration | dect-auto-reregistration | pass |
| should-fw-01 | should_trigger | dect-firmware-management | dect-firmware-management | pass |
| should-fw-02 | should_trigger | dect-firmware-management | dect-firmware-management | pass |
| should-maint-01 | should_trigger | dect-maintenance-troubleshooting | dect-maintenance-troubleshooting | pass |
| should-maint-02 | should_trigger | dect-maintenance-troubleshooting | dect-maintenance-troubleshooting | pass |
| should-survey-01 | should_trigger | dect-radio-survey | dect-radio-survey | pass |
| should-survey-02 | should_trigger | dect-radio-survey | dect-radio-survey | pass |
| should-ibs-01 | should_trigger | dect-ibs-deployment | dect-ibs-deployment | pass |
| should-ibs-02 | should_trigger | dect-ibs-deployment（或经路由） | dect-maintenance-troubleshooting | pass（经"或经路由"通道：OOS/inserv 判读在维护能力内可达） |
| should-sip-01 | should_trigger | dect-sip-dect | dect-sip-dect | pass |
| should-sip-02 | should_trigger | dect-sip-dect | dect-sip-dect | pass |
| bait-pari-01 | should_not_trigger | 应激活 dect-handset-registration，禁 dect-pari-identifier | dect-handset-registration | pass |
| bait-select-01 | should_not_trigger | 应 dect-ipxbs-deployment，禁停留 dect-product-selection | dect-ipxbs-deployment | pass |
| bait-deploy-01 | should_not_trigger | 应 dect-xbs-sync-topology，禁 dect-ipxbs-deployment | dect-xbs-sync-topology | pass |
| bait-mixed-01 | should_not_trigger | 应 dect-auto-reregistration，禁停留 dect-mixed-mode | dect-auto-reregistration | pass |
| bait-hsreg-01 | should_not_trigger | 应 dect-firmware-management，禁 dect-handset-registration | dect-firmware-management | pass |
| bait-rereg-01 | should_not_trigger | 应转 dect-firmware-management，禁在 dect-auto-reregistration 硬跑 | dect-auto-reregistration | fail |
| bait-fw-01 | should_not_trigger | 应 dect-ipxbs-deployment，禁停留 dect-firmware-management | dect-ipxbs-deployment | pass |
| bait-survey-01 | should_not_trigger | 应 dect-xbs-sync-topology，禁停留 dect-radio-survey | dect-xbs-sync-topology | pass |
| bait-ibs-01 | should_not_trigger | 应 dect-mixed-mode，禁 dect-ibs-deployment | dect-mixed-mode | pass |
| bait-sip-01 | should_not_trigger | 应 dect-sip-dect 并纠正语义，禁套 dect-handset-registration | dect-sip-dect | pass |
| bait-oos-01 | should_not_trigger | 超范围声明边界 | none | pass |
| bait-oos-02 | should_not_trigger | 超范围声明边界 | none | pass |
| bait-oos-03 | should_not_trigger | 超范围声明边界 | none | pass |
| edge-pli-01 | edge_case | 按降位规则回答（末 2 位不同需 PLI=29） | dect-pari-identifier | pass |
| edge-rssi-01 | edge_case | 按门槛口径回答（-70 为下限、金属场景另判） | dect-radio-survey | pass |
| edge-cap-01 | edge_case | 按硬上限回答（每 PARI 254 台+Sync Highway） | dect-product-selection | pass（容量边界问题路由到产线容量规格，属合理路由） |

## fail 明细

### bait-rereg-01
- 预期：应转 dect-firmware-management（版本太老的 8262 先升固件再跑重注册），不应在 dect-auto-reregistration 里硬跑或直接放弃
- 盲判：dect-auto-reregistration
- 偏差分析：题面"重注册时提示版本太老"把语境锚定在重注册流程内，盲判据目录中 dect-auto-reregistration 描述含"机型版本表 p252"而留在本能力内。但目录描述只列了版本表，没有"版本不达标→转固件轨道"的出口提示，盲测路由器无从得知该转接关系。这是能力目录描述缺口暴露的合理误判，非乱路由。
- 改进方向：在 dect-auto-reregistration 的目录描述里补一句"机型版本不达标者转 dect-firmware-management 先升级"，或把题面语境从"重注册时"改为报错后的处置阶段。
