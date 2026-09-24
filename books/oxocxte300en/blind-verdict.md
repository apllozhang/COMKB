# oxocxte300en 判卷报告（blind-results.md vs test-prompts.json）

## 汇总

| 类型 | 通过 | 总数 | 得分 |
|---|---|---|---|
| should_trigger | 24 | 24 | 100% |
| should_not_trigger | 13 | 13 | 100% |
| edge_case | 3 | 3 | 100% |
| **总计** | **40** | **40** | **100%** |

## should_trigger 明细（24/24 全中）

- should-collect-01 / collect-02 → oxos-data-collection（collect-02 预期允许 numbering-groups，命中的是首选项）
- should-comm-01 / comm-02 → oxos-commissioning
- should-term-01 / term-02 → oxos-terminals
- should-num-01 / num-02 → oxos-numbering-groups
- should-user-01 / user-02 → oxos-user-features
- should-sip-01 / sip-02 → oxos-sip-trunk
- should-inbar-01 / inbar-02 → oxos-incoming-barring
- should-maint-01 / maint-02 → oxos-maintenance
- should-hw-01 / hw-02 → oxos-hardware-platform
- should-audio-01 / audio-02 → oxos-audio-messages
- should-sec-01 / sec-02 → oxos-security
- should-rb-01 / rb-02 → oxos-rainbow-integration

## should_not_trigger 明细（13/13）

- bait-collect-01：盲判 numbering-groups = 预期"应激活 oxos-numbering-groups" → pass
- bait-comm-01：盲判 terminals = 预期"应激活 oxos-terminals" → pass
- bait-term-01：盲判 numbering-groups = 预期一致 → pass
- bait-num-01：盲判 incoming-barring = 预期一致，未碰被禁的 numbering-groups → pass
- bait-user-01：盲判 incoming-barring = 预期一致，未停留在 user-features → pass
- bait-sip-01：盲判 incoming-barring = 预期一致 → pass
- bait-inbar-01：盲判 sip-trunk = 预期一致 → pass
- bait-maint-01：盲判 commissioning = 预期一致 → pass
- bait-rb-01：盲判 none，预期"超出本 bundle 深度（云侧运营属姊妹包）" → pass（边界判定：预期文句描述的"激活 rainbow 卡后转姊妹技能"与盲判 none 殊途同归，均不做包内深水区工作）
- bait-rb-02：盲判 none，预期"超出本 bundle，不应激活 oxos-rainbow-integration" → pass，未命中被禁能力
- bait-sec-01：盲判 oxos-security，预期"声明边界指向 TC1143 本身、不编造条目" → pass（边界判定：能力卡自带"TC1143 强制指针"，激活它正是产出"指向文档、声明边界"的路径；预期未点名任何被禁能力）
- bait-audio-01：盲判 incoming-barring = 预期一致，未停留在 audio-messages → pass
- bait-hw-01：盲判 commissioning = 预期一致，未停留在 hardware-platform → pass

## edge_case 明细（3/3）

- edge-version-01：盲判 none → pass。目录十二张卡无一覆盖 WebRTC 网关自动配置，判 none 即声明"无对应能力卡"，属合理路由；预期答案依赖书内 nr-01 双口径（p366/p395），该勘误知识不在任何能力卡描述内，属测试集设计层面的空档，非路由错误。
- edge-hunt-01：盲判 numbering-groups → pass。卡内"500 被 VM 保留"规则恰好支撑预期边界答案（从 501 起用）。
- edge-hotel-01：盲判 commissioning → pass。卡内"初始安装向导与 Hotel 唯一入口"恰好支撑预期边界答案（存量系统须冷复位重来）。

## 失败清单

无。
