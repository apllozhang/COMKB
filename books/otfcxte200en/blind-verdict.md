# OTFC 盲判判卷报告（blind-results.md 对比 test-prompts.json）

## 汇总

| 类型 | 通过 / 总数 |
|---|---|
| should_trigger | 24/24 |
| should_not_trigger | 8/9 |
| edge_case | 4/4 |
| **总计** | **36/37** |

- should_trigger：24 条全部命中预期能力，无偏差。
- should_not_trigger：9 条诱饵中 8 条命中预期"另一能力"或未触禁区；1 条失败（见明细）。
- edge_case：4 条路由均合理（services-operations / sip-channel-integration / mail-exchange-integration / installation-ftw），符合"路由合理或声明边界即 pass"。

## 判卷口径说明（两处判断题）

- bait-sip-01（pass）：预期为"按边界回答：参数细节在 TC3048，不虚构"。盲判命中 otfax-sip-channel-integration，该能力目录自带"参数参照 TC3048"边界，禁止项是虚构行为而非该能力本身，判 pass。
- bait-plan-01（pass）：预期为"按边界回答：端口全表在 Features List，不应停留在 solution-planning 出数"。盲判命中 otfax-solution-planning，其目录明写"端口全表/格式/sizing 一律指向 OTFC Features List"，路由本身携带预期边界，禁止项是"出数"行为，判 pass。

## Fail 明细

### bait-rpt-01（should_not_trigger）— FAIL
- 预期：应转 otfax-directory-routing 的 Accounting 段（OXE 话单 + OmniVista 8770 计费），区分计费与业务量统计。
- 盲判：otfax-reports-monitoring。
- 偏差分析：题面"按部门出传真成本报表"中"成本/计费"才是题眼，"31 个报表"是表面诱饵。盲判被表面词带进报表能力，未识别 OTFC 自带 31 模板只覆盖全系统/单用户维度、无部门成本口径，真正的成本数据在 directory-routing 能力的 OXE 话单对接段。典型"同域近邻词劫持"。

## 逐条对照（简表）

| id | 盲判 | 预期 | 结果 |
|---|---|---|---|
| should-install-01 | otfax-installation-ftw | otfax-installation-ftw | pass |
| should-install-02 | otfax-installation-ftw | otfax-installation-ftw | pass |
| should-sip-01 | otfax-sip-channel-integration | 同 | pass |
| should-sip-02 | otfax-sip-channel-integration | 同 | pass |
| should-mail-01 | otfax-mail-exchange-integration | 同 | pass |
| should-mail-02 | otfax-mail-exchange-integration | 同 | pass |
| should-user-01 | otfax-user-administration | 同 | pass |
| should-user-02 | otfax-user-administration | 同 | pass |
| should-profile-01 | otfax-profile-policy | 同 | pass |
| should-profile-02 | otfax-profile-policy | 同 | pass |
| should-dir-01 | otfax-directory-routing | 同 | pass |
| should-dir-02 | otfax-directory-routing | 同 | pass |
| should-svc-01 | otfax-services-operations | 同 | pass |
| should-svc-02 | otfax-services-operations | 同 | pass |
| should-bk-01 | otfax-backup-upgrade | 同 | pass |
| should-bk-02 | otfax-backup-upgrade | 同 | pass |
| should-cli-01 | otfax-client-coversheet | 同 | pass |
| should-cli-02 | otfax-client-coversheet | 同 | pass |
| should-plan-01 | otfax-solution-planning | 同 | pass |
| should-plan-02 | otfax-solution-planning | 同 | pass |
| should-rpt-01 | otfax-reports-monitoring | 同 | pass |
| should-rpt-02 | otfax-reports-monitoring | 同 | pass |
| should-user-03 | otfax-user-administration | 同 | pass |
| should-dir-03 | otfax-directory-routing | 同 | pass |
| bait-install-01 | otfax-mail-exchange-integration | 应激活 mail-exchange-integration | pass |
| bait-sip-01 | otfax-sip-channel-integration | 边界回答（TC3048），能力域正确 | pass |
| bait-mail-01 | otfax-profile-policy | 应激活 profile-policy | pass |
| bait-user-01 | otfax-directory-routing | 应激活 directory-routing | pass |
| bait-profile-01 | otfax-profile-policy | 应激活 profile-policy 并纠正方向 | pass |
| bait-svc-01 | otfax-backup-upgrade | 应激活 backup-upgrade | pass |
| bait-cli-01 | otfax-mail-exchange-integration | 应激活 mail-exchange-integration | pass |
| bait-rpt-01 | otfax-reports-monitoring | 应转 directory-routing（Accounting） | **fail** |
| bait-plan-01 | otfax-solution-planning | 边界回答（Features List），路由域正确 | pass |
| edge-ha-01 | otfax-services-operations | 边界回答，路由合理 | pass |
| edge-tls-01 | otfax-sip-channel-integration | 边界回答，路由合理 | pass |
| edge-mail-02 | otfax-mail-exchange-integration | 边界回答，路由合理 | pass |
| edge-fire-01 | otfax-installation-ftw | 边界回答，路由合理 | pass |
