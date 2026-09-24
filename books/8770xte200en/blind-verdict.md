# 判卷报告（8770xte200en）

依据：`blind-results.md`（锁定盲判，判卷阶段未回改）对比 `test-prompts.json` 的 type 与 expected_behavior。

## 汇总

| 类型 | 通过/总数 | 通过率 |
|---|---|---|
| should_trigger | 24/25 | 96% |
| should_not_trigger（诱饵） | 8/9 | 89% |
| edge_case | 6/6 | 100% |
| **总计** | **38/40** | **95%** |

edge_case 判定口径：路由合理或声明边界即 pass，不要求与答案同 slug。edge-ha-01 盲判 none，与答案 out_of_scope 口径一致，判 pass。

## 逐条判定明细（仅列非 pass，其余 37 条 pass）

### 1. should-node-02 — FAIL（记录不一致型）
- 预期：激活 ovnms-node-onboarding（实时核验方法 + 重启 NMC Alarm server）
- 盲判文件记录：`should-node-02 | ovnms-user-provisioning | 用户建了但同步慢，目录里"实时同步核验与 NMC Alarm server 排障"在节点接入条目`
- 偏差分析：该行 slug 列与理由列自相矛盾——理由明说"实时同步核验与 NMC Alarm server 排障在节点接入条目"，指向 ovnms-node-onboarding，slug 列却写成 ovnms-user-provisioning。按盲判协议，结果文件锁定后不得回改，slug 字段是正式答案，故严格记 fail。定性为锁定时的转写笔误而非路由判断错误，但按记录判卷不豁免。

### 2. should-user-03 — FAIL（真路由偏差）
- 预期：激活 ovnms-user-provisioning（Key profile 三层与同步前提）
- 盲判：ovnms-oxe-ui-efficiency
- 偏差分析：目录中"配键"字样唯一出现在 oxe-ui-efficiency 的"图形视图配键（Function/Content/Mnemo）"，而 user-provisioning 条目仅笼统写"Profile"，未展开 Key profile 子能力。盲判选择了字面匹配更强的条目，但语义上"给一批用户预设按键并自动下发"归属用户开通的 Key profile（用户属性模板随建号同步下发），oxe-ui-efficiency 讲的是 Configure 界面的操作手法（搜索/冻结列/导入导出），不是按键业务配置本身。属真实失配，根因是目录粒度差异诱导。

### 3. bait-reports-01 — FAIL（命中被禁能力）
- 预期：应激活 ovnms-reports-scheduling（审计报告计划分发），不应停留在 ovnms-audit-compliance 只讲启用
- 盲判：ovnms-audit-compliance
- 偏差分析：判卷规则要求 should_not_trigger 不得命中被禁能力，本条被禁能力即 audit-compliance（只讲启用），盲判恰好命中，记 fail。偏差根源在目录文本与答案口径存在真实冲突：审计条目明写"History/Detail 导出（Immediate/Scheduled）"，字面上完全覆盖"审计记录每天自动生成报告发邮件"，盲判据此归审计能力；答案口径则将"定时生成+邮件分发"的编排动作归报表与任务编排能力（审计只管开启与取证）。此题与其说是路由错误，不如说是能力目录描述越界（审计条目把导出编排也写进了自己的描述），建议在目录措辞上区分"审计导出动作归审计、定时邮件分发归报表"，否则同类盲判仍会复现。

## 结论
38/40 通过。两处 fail 中，1 处为盲判记录内部矛盾（should-node-02，slug 列转写笔误），2 处为真实/口径偏差（should-user-03 目录粒度诱导、bait-reports-01 目录描述与答案口径冲突）。无 should_not_trigger 误踩 platform-installation / node-onboarding / user-provisioning / alarm-management / license-management / backup-restore 等其余诱饵，全部 edge 与超范围题（edge-ha-01=none）判定正确。
