# rainxte101en 盲测评判报告

## 汇总

| 类型 | 通过 | 总数 |
|---|---|---|
| should_trigger | 24 | 24 |
| should_not_trigger（诱饵） | 8 | 8 |
| edge_case | 5 | 5 |
| **总计** | **37** | **37** |

## 判卷说明

- should_trigger：24 条盲判 slug 与预期能力逐一比对，全部一致。
- should_not_trigger：
  - bait-company-01 盲判 hub-member-telephony，未命中被禁的 hub-company-voice-subscription，pass；
  - bait-pbx-01 / bait-zt-01 / bait-hunt-01 / bait-ana-01 / bait-ws-01 盲判均命中预期"另一能力"（zero-touch / device-maintenance / welcome-service-ivr / maintenance-support / attendant-supervision），pass；
  - bait-ms-01 预期为"超出站点机制、应声明边界，不应把 hub-multisite 当作可满足该需求执行"，禁的是执行方式而非激活本身；multisite 卡目录自带"目录跨站不变"口径，盲判路由到该卡并明确以对照边界口径为由，正是声明边界的正确姿势，pass；
  - bait-hub-01 预期 none，盲判 none，pass。
- edge_case：5 条盲判路由（member-telephony / hunt-groups x2 / welcome-service-ivr / attendant-supervision）均落在对应能力卡上，属合理路由，按规则全部 pass。

## 失败明细

无。
