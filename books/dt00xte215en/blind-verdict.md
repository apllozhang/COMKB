# 盲测验卷报告 · dt00xte215en（omniswitch-lan-access）

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
| bait-vlan-01 | swl2-qos-acl-policy | 应激活 qos-acl-policy（shutdown bpdu），禁 vlan-routing | pass，命中正解、未触禁 |
| bait-aaa-01 | swl2-vlan-routing | 应激活 vlan-routing，禁 aaa-hardening | pass |
| bait-cfg-01 | swl2-upgrade-autofabric | 应转 upgrade-autofabric（RMA 边界），禁 config-lifecycle 虚构恢复 | pass |
| bait-link-01 | swl2-link-redundancy | 应激活 link-redundancy（DHL 自动禁 STP） | pass |
| bait-l3-01 | swl2-vlan-routing | 应先查 vlan-routing，禁直接当 VRRP（l3-services） | pass |
| bait-qos-01 | swl2-access-guardian | 应激活 access-guardian（UNP 下发），禁停留 qos-acl-policy 全局策略 | pass |
| bait-upg-01 | swl2-fleet-tools | 应激活 fleet-tools，禁 upgrade-autofabric / lldp-poe | pass |
| bait-fleet-01 | swl2-fleet-tools | 应按 fleet-tools 只读边界回答 | pass |
| bait-olc-01 | swl2-upgrade-autofabric | 应转 Auto-Fabric，禁停留 lightning-config | pass |
| bait-ag-01 | none | 超范围（RADIUS 服务器侧书外），应声明边界 | pass，盲判 none |

## edge 明细（4 条全过）

| id | 盲判 | 预期要点 | 判定 |
|---|---|---|---|
| edge-mirror-01 | swl2-diagnostics | 镜像会话 4/2 双口径如实说明 | pass，路由正确 |
| edge-lldp-01 | swl2-lldp-poe | 两页数值不一致按边界处理，不编统一值 | pass，目录已含此边界 |
| edge-vc-01 | swl2-virtual-chassis | 优先级改动须 reload 才生效 | pass |
| edge-console-01 | swl2-aaa-hardening | 按型号查分代表表（多数 9600，部分 115200） | pass，console 归管理面属合理路由 |

## 失败清单

无。

## 备注

- should_trigger 26 条盲判 slug 与预期全部逐一对应，无"命中替代能力"情形。
- 10 条诱饵全部落在"应激活的另一能力"或 none 上，没有一条触碰被禁能力，说明仅凭目录描述即可完成主从域区分（业务配置 vs 管理面、参数 vs 规则、工具边界 vs 交换机侧）。
