# oxocxte301en 判卷报告（blind-verdict）

## 汇总

| 类型 | 通过 / 总数 | 通过率 |
|---|---|---|
| should_trigger | 28/28 | 100% |
| should_not_trigger | 5/9 | 55.6% |
| edge_case | 3/3 | 100% |
| **总计** | **36/41** | **87.8%** |

## should_trigger 明细（28/28 全过）

should-sipnet-01/02、should-ars-01/02/03、should-hotel-01/02、should-sec-01/02、should-cert-01/02、should-att-01/02、should-vm-01/02、should-cloud-01/02、should-foun-01/02、should-term-01/02、should-shar-01/02、should-enti-01、should-dect-01/02、should-maint-01/02 全部命中预期能力。其中 should-sec-02 预期为 security-hardening 或 voicemail-mobility 任一，盲判 voicemail-mobility，判 pass。

## edge_case 明细（3/3 全过）

- edge-time-01：盲判 numbering-ars-suite，路由合理 → pass
- edge-dhcp-01：盲判 none（目录十四能力均不覆盖 DHCP 池），声明边界 → pass
- edge-cloud-01：盲判 cloud-connect-fleet（24h 延迟知识点），路由合理 → pass

## fail 明细（4 条，全部在 should_not_trigger）

### bait-att-01
- 预期：动态互动超出按键树能力（书内边界），不应激活 oxoa-attendant-suite 硬套，应声明边界
- 盲判：oxoa-attendant-suite
- 偏差分析：题面首词"AA 语音导航"关键词强锚定，第一判断按字面命中导航套件；未识别"查话费余额的动态菜单"是动态交互需求，超出静态按键树。这是知识边界判断题，仅凭目录描述难以区分"加菜单"（能力内）与"加动态查询菜单"（能力外）。

### bait-vm-01
- 预期：SIP 话机不支持游牧（p147），应激活 oxoa-terminal-ecosystem 或声明边界，不应在 oxoa-voicemail-mobility 内硬配
- 盲判：oxoa-voicemail-mobility
- 偏差分析："游牧模式"关键词直接命中 voicemail-mobility 描述，但题面主语是 ZyXEL 第三方 SIP 话机；terminal-ecosystem 里"SIP 话机不支持游牧"这条反向边界才是本题钥匙，盲判按正向关键词路由，漏了设备类型约束。

### bait-cloud-01
- 预期：云侧公司/订阅/成员管理属 bundle.oxo-connect-starter，不应激活 oxoa-cloud-connect-fleet（本卡只管目录同步到 OXO）
- 盲判：oxoa-cloud-connect-fleet
- 偏差分析：目录中唯一含"Rainbow"字样的能力就是 cloud-connect-fleet，但该条只覆盖"业务目录同步先擦空再写入"，不覆盖 Rainbow 租户管理；跨 bundle 边界在目录里不可见，盲判按关键词就近命中。

### bait-dect-01
- 预期：应激活 oxoa-dect-deployment 并指出 8158s/8168s 仅 NOE 模式（p550），不应走 SIP 话机路径硬配
- 盲判：oxoa-terminal-ecosystem
- 偏差分析：题面"WiFi 话机""SIP 模式注册"两个关键词都指向终端生态，盲判据此排除 DECT；但产品型约束（8168s 归属 DECT 能力、仅 NOE 模式）藏在 dect-deployment 内，仅凭题面字面与目录无法推出 WiFi 话机归 DECT 管。

## 结论

正向触发与边界题全过，失分集中在诱饵题：4 条 fail 全部是"字面关键词命中了被禁止的能力"，其中 2 条（bait-att-01、bait-cloud-01）依赖目录外的跨能力/跨 bundle 边界知识，2 条（bait-vm-01、bait-dect-01）依赖产品型号级归属约束。诱饵题的本质是考"何时收手声明边界"，纯目录相似度路由天然吃亏。
