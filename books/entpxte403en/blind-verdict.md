# 判卷报告 entpxte403en（oxe-sip）

## 汇总

| 类型 | 通过 / 总数 |
|---|---|
| should_trigger | 26 / 26 |
| should_not_trigger | 5 / 8 |
| edge_case | 5 / 5 |
| **总计** | **36 / 39** |

## Fail 明细

### bait-proto-01
- 预期：RFC 3261 逐字段教学属原书外，应声明边界，不应激活 osip-protocol-foundation 展开报文课
- 盲判：osip-protocol-foundation
- 偏差分析：目录含"SIP 协议栈与消息响应码"，盲判按表面关键词把协议教学题归入协议机理能力，未识别"逐字段 RFC 教学"的深度超出教材定位。此类边界题的判别点在于教材是施工口径而非协议课本。

### bait-sbc-01
- 预期：真实运营商参数以 TC2005 与运营商正式文档为准（书外），不应照 osip-otsbc-carrier-interconnect 的实验口径直配
- 盲判：osip-otsbc-carrier-interconnect
- 偏差分析：题面关键词（运营商、参数、SIPS/PAI）与目录高度吻合，盲判顺关键词路由命中被禁能力。判别点是"正式参数表逐条核对"必须回到书外权威文档，能力内只有实验口径，直配有生产风险。

### bait-remote-01
- 预期：应激活 osip-deskphone-provisioning（话机开通），不应停留在 osip-remote-workers
- 盲判：osip-sip-device-provisioning
- 偏差分析：盲判避开了被禁的 remote-workers，但选了相邻的 SIP Device 三件套而非 ALE 话机六段施工。题面"这台话机"指寄给异地员工的物理终端，开通形态应走 deskphone 线；盲判把泛化"话机开通"归入了设备开通。属相邻能力混淆的部分偏差。

## 判卷口径备注
- should_trigger 26 条全中，包括形态选型（forms-01 五不带边界）、容量核算、寻线组混装等复合题。
- "预期 none/声明边界"的诱饵按盲判 none 判 pass：bait-ales-01（VDI）、bait-cert-01（企业 CA 制度）、bait-feat-01（ACD）三条盲判均正确判 none。
- edge_case 5 条全部按"路由合理或声明边界"通过（edge-quarantine-01 路由防隔离 Framework、edge-supervision-01 路由监督特性，均合理）。
