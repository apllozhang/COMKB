# openxte301en 判卷报告（blind-results 对比 test-prompts.json）

## 汇总

| 类型 | 通过 | 总数 | 得分 |
|---|---|---|---|
| should_trigger | 26 | 26 | 26/26 |
| should_not_trigger | 6 | 8 | 6/8 |
| edge_case | 3 | 3 | 3/3 |
| **总计** | **35** | **37** | **35/37（94.6%）** |

## 逐类结论

- should_trigger 26 条全部命中预期 slug，无偏差。
- should_not_trigger 8 条诱饵中 6 条命中预期的"另一能力"或 none；2 条 fail（见明细）。
  - bait-cal-version-01 判 pass 但带保留：答案键未点名禁止 slug，预期是行为层"声明边界并指向最新文档"。盲判选 ota-calendar-sync，而版本门槛（仅 Exchange 2010/2013/O365）恰好写在该能力目录里，声明边界所需知识正来自它，slug 层判 pass；是否真的声明边界属回答行为，超出盲判可验证范围。
- edge_case 3 条均路由合理（目录 LDAP 溢出归目录能力、Ghost Z 容量公式归 Nomadic、单设备化归智能手机交付），按"路由合理即 pass"计。

## Fail 明细

### bait-conf-dcs-01（should_not_trigger）
- 预期：应激活 ota-conference-collaboration（presentation 本就不可下载，attachment 才可），不应激活 ota-dcs-documents 当作转换故障。
- 盲判：ota-dcs-documents
- 偏差分析：题面里用户自己抛出"是不是转换服务器坏了"的假设，盲判顺着故障假设定位到 DCS 能力。更关键的是 ota-dcs-documents 的目录描述同样写明"presentation 不可下载、attachment 可"，两个能力都持有这条知识，仅凭目录无法判断职责归属。答案键把"下载"归为会议内权限语义（协作能力），是更细的切分信号，目录盲判拿不到。

### bait-lab-prod-01（should_not_trigger）
- 预期：应声明实验口径边界并拒绝照搬，不应激活 ota-lab-pod 作为生产配置依据。
- 盲判：ota-lab-pod
- 偏差分析：答案键在"不应"子句点名 ota-lab-pod，盲判命中被禁止能力，按字面判 fail。但需指出键设计的张力：拒绝依据（"教学专用、实验值不入生产"）本身就写在 ota-lab-pod 的目录描述里，工程师要声明这个边界恰恰要先激活该能力查证。slug 级路由表达不了"激活查证但拒绝照搬"的用法区分，此题实际考的是使用方式而非路由。建议答案键口径改为"激活 ota-lab-pod 须同时声明实验边界"。
