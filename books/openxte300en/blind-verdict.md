# openxte300en 判卷报告（blind-verdict）

## 汇总

| 类型 | 通过 / 总数 | 通过率 |
|---|---|---|
| should_trigger | 24/24 | 100% |
| should_not_trigger | 11/12 | 91.7% |
| edge_case | 4/4 | 100% |
| **总计** | **39/40** | **97.5%** |

## should_trigger 明细（24/24 全过）

should-wizard-01/02、should-license-01/02、should-node-01/02、should-prior-01/02、should-users-01/02、should-vm-01/02、should-client-01/02、should-maint-01/02、should-sot-01/02、should-cert-01/02、should-sg-01/02、should-lab-01/02 全部命中预期能力，无偏差。

## should_not_trigger 明细（11/12）

通过的 11 条：
- bait-wizard-01：盲判 sot-installation（装机在向导之前）→ pass
- bait-sot-01：盲判 post-installation-wizard（装完进向导）→ pass
- bait-license-01：盲判 license-flexlm → pass
- bait-sip-01：盲判 prior-management（未上当去重建 trunk）→ pass
- bait-node-01：盲判 node-declaration-sip（未跳重装）→ pass
- bait-maint-01：盲判 maintenance-rehosting（TC2149 收尾口径）→ pass
- bait-cert-01：盲判 none（SBC/反向代理部署超出十二能力）→ pass
- bait-users-01：盲判 users-profiles（Users 应用只能改档案的边界）→ pass
- bait-sg-01：盲判 supervision-groups（两套机制关系）→ pass
- bait-lab-01：盲判 lab-connections（实验值为公开教学值，须拒绝）→ pass
- （bait-client-01 见 fail）

### fail：bait-client-01
- 预期：应激活 ots-supervision-groups 并按边界回答 One 无监督功能（升 Desktop），不应由 ots-clients-multi-devices 硬答可调出
- 盲判：ots-clients-multi-devices
- 偏差分析：题面焦点词"OTC PC One"命中 clients-multi-devices 里"Desktop 许可决定全量或 One 免费模式"，但问题的动作宾语是"监督窗口"，功能归属 supervision-groups。盲判跟了名词主语，没跟请求的实际功能；"One 无监督"这条跨能力边界在两个目录描述里都只写了一半（一边写许可分档、一边写监督组建组），拼起来才能判对。

## edge_case 明细（4/4 全过）

- edge-ha-01：盲判 post-installation-wizard（HA 保持 Disable 是其明确边界）→ pass
- edge-license-ok-01：盲判 post-installation-wizard（"许可 OK 只代表文件在"正是该边界）→ pass
- edge-announcement-01：盲判 voice-mail（公告一条 5 分钟覆盖式边界）→ pass
- edge-esxi-01：盲判 sot-installation（支持矩阵归属装机）→ pass

## 结论

本书 40 条仅失 1 条，双向诱饵（装机↔向导、前缀↔trunk、声明失败↔重装）全部识破，超范围题（SBC/反向代理、Exchange UM 之外的对照样本）判断正确。唯一 fail 是"产品功能归属"型诱饵：OTC One 与监督功能分属两个能力，盲判被题面主语带偏。整体看，该书的诱饵设计偏"流程顺序"与"边界口径"，目录描述对这类信号的覆盖较好；跨能力功能归属类是残余风险点。
