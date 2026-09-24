# otmcxte200en 判卷报告

## 汇总

| 类型 | 通过 | 总数 | 得分 |
|---|---|---|---|
| should_trigger | 24 | 24 | 100% |
| should_not_trigger | 11 | 12 | 91.7% |
| edge_case | 3 | 3 | 100% |
| **总计** | **38** | **39** | **97.4%** |

## 判卷明细

### should_trigger（24/24）
全部命中：install×2、license×2、decl×2、sip×2、umb×2、profile×2、notif×2、backup×2、pos×2、portal×2、imap×2、ga×2，盲判 slug 与预期逐一一致。

### should_not_trigger（11/12）
- bait-install-01：盲判 otmsg-declaration-sync，命中预期"另一能力"，避开 otmsg-install-site-setup。pass
- bait-decl-01：盲判 otmsg-sip-trunk-provisioning，命中预期，避开 otmsg-declaration-sync。pass
- bait-sip-01：盲判 otmsg-declaration-sync，命中预期，避开 otmsg-sip-trunk-provisioning。pass
- bait-umb-01：盲判 otmsg-mailbox-profiles，命中预期，避开 otmsg-user-mailbox-provisioning。pass
- bait-profile-01：盲判 otmsg-user-mailbox-provisioning，命中预期，避开 otmsg-mailbox-profiles。pass
- bait-notif-01：盲判 otmsg-imap-access，命中预期，避开 otmsg-notification-smtp-sms。pass
- bait-portal-01：盲判 otmsg-mailbox-profiles，命中预期，避开 otmsg-web-portal。pass
- bait-backup-01：盲判 otmsg-install-site-setup，命中预期，避开 otmsg-backup-statistics。pass
- bait-ha-01：盲判 none，符合"HA 超书外、应声明边界"。pass
- bait-um-01：盲判 none，符合"UM 对接超书外"。pass
- bait-aa-01：盲判 none，符合"AA 配置超书外"。pass

### edge_case（3/3）
- edge-node-01：路由 otmsg-declaration-sync（节点号规则所在），与预期双口径回答兼容，合理。
- edge-mwi-01：路由 otmsg-notification-smtp-sms（MWI 机制所在），与预期机制口径一致，合理。
- edge-imap-01：路由 otmsg-imap-access，与预期验收判据口径一致，合理。

## 失败清单

### bait-license-01（should_not_trigger）
- **题面**：新买了几台 IP 话机，怎么确认交换机上对应的话机用户许可还够用？
- **预期**：应激活 otmsg-user-mailbox-provisioning（话机许可三族核查/spadmin），不应激活 otmsg-license-management（那是 FlexLM 的 .ice 许可）。
- **盲判**：none（判为 OXE 话侧话机许可、超出目录范围）。
- **偏差分析**：盲判正确避开了被禁止的 otmsg-license-management，但漏判了应激活的另一能力。目录里 otmsg-user-mailbox-provisioning 的描述明确含"许可三族六类核查（spadmin）"，"确认许可够不够"按判据应落到这个 spadmin 核查上；盲判时把"话机用户许可"单独理解为 OXE 话侧许可而判了书外，是对目录描述里许可核查条目的覆盖面读窄了。属诱饵题里"该指认另一能力却判了 none"的偏差，判 fail。
