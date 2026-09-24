# Click to Call 交付（DDI 翻译器、ISDN 构造、STAP、前缀规则、属性关联）

## R — 原文依据

> "ISDN number = ISDN prefix + Entity installation number + Set directory number"（p258）
> "STAP - Off hook: automatic call is authorized when the receiver is picked up. - Authorized: ... - Forbidden: ... The STAP option can be setup for all types of phones except SIP devices."（p272）
> "Types of prefix rules • None • Rule for external call • Rule for call between network"（p261）
> "By default, the extension, ISDN and Mobile numbers attributes can be used to initiate a call"（p256）
> "All phone numbers in bold characters are available for STAP call"（p283）

出处：8770XTE202EN p254-263, p265-284。

## I — 自述

Click to Call 的号码逻辑链五环，缺一环号码就点不动：

1. **PCX 数据环**：DDI 翻译器定义 DDI 与内线映射（首个外部号/首个内部号/范围大小）；用户 STAP 权限三态（Off hook 摘机发起 / Authorized 均可 / Forbidden 禁止）；OXE 同步回填
2. **ISDN 构造环**：8770 侧 Process ISDN Number 启用后为人员自动构造 ISDN 号；公式为"前缀+实体安装号+话机号"，DDI 话机的话机号被 DDI 号替换；无安装号/翻译器未纳管且无补充号时都不构造；改了 PCX 数据必须重新同步
3. **前缀规则环**：三类规则——None 原样拨、外部呼叫规则（Prefix to delete 是"匹配头+删除"双重语义）、网间呼叫规则（选目标网络+加前缀）；全网通用建 Network 层、单 OXE 建 PCX 层；PCX 已有 ARS 时单规则"删空+加 0"即可
4. **属性关联环**：Administration 应用 nmc > Application Configuration > Click to Call 下默认已建 Extension/ISDN Number/Mobile 三项；Misc 1-5 需 Create > Prefix management 手工添加并可绑规则
5. **使用环**：Web 目录客户端 Define associated station（分机号+话机密码）绑主叫话机，搜索后在 Detail(s) 点粗体号码发起呼叫

关联完成后人员最多可有 5 个可点号码（Extension/ISDN/Mobile/Misc 1-5）。

## A1 — 书中案例

**Click to Call 交付实验**（p265-284）：

1. 配外部 SIP 网关注册与 DID 翻译器（首外部号/首内部号/范围，实验口径随 POD 号）
2. PCX 页签配 DID translation usage 与按需的专属前缀
3. Data Collection 页签勾 Process ISDN Number
4. 用户 31000 All 页签设 STAP=Authorized
5. Directory 核验 Jean Dupont/Paul Tregueur 的 ISDN 号已自动构造
6. Client PC 启动 IPDSP 关联 31000，MicroSIP 注册其余分机（实验口径）
7. Configuration 树建外部呼叫规则：Prefix to add=00、Prefix to delete=33
8. 再建网间呼叫规则：目标子网+中继组前缀（实验口径）
9. Administration 应用 Click to Call 下：Extension 绑 None、ISDN/Mobile 绑外部规则
10. 右键 Create > Prefix management 添加 Misc 1 并绑规则
11. 给 Paul Tregueur 补 Mobile 与 Misc.1 值
12. Web 客户端 Define associated station（31000+密码）后搜人，点粗体号码拨测四路

## A2 — 未来触发

使用情境：客户要从网页目录一键外呼；点了号码话机不响；人员的 ISDN 号没生成；拨出去的号码少了/多了前缀；SIP 话机能不能点；想多加几个可拨字段。

语言信号：Click to Call / 点击外呼 / STAP / Off hook / DDI translator / DDI 翻译器 / ISDN 号 / Process ISDN Number / 前缀规则 / prefix rule / 外部呼叫规则 / 网间呼叫 / associated station / 关联话机 / 粗体号码 / Misc 属性。

与相邻能力区分：

- 通话质量/媒体问题 → 语音侧（书外）
- 目录条目缺属性值 → 保密与客户端能力域的数据维护
- OXE 没注册同步 → OXE 注册能力

## E — 可执行步骤

输入契约：OXE 已注册且可同步、话机类型清单（SIP 话机先排除）、外部号码方案（DDI 段）、主叫话机分机与密码。话机全为 SIP → 判停本能力不适用。

1. 核 DDI：确认 PCX 侧翻译器三字段与取回参数（DID translation usage）。完成标准：翻译器可用
2. 开构造：Data Collection 勾 Process ISDN Number，触发同步。完成标准：人员 ISDN 号生成
3. 配 STAP：目标用户 All 页签按场景设三态之一。完成标准：主叫用户已授权
4. 建规则：按号段方案建外部/网间规则于正确层级。完成标准：规则序列符合匹配预期
5. 关联属性：Click to Call 下默认三项按需绑规则，Misc 属性按需新增。完成标准：属性规则表成文
6. 交付拨测：Define associated station 绑主叫话机，点粗体号码逐路验证。完成标准：四路（或五路）可点通

判停点：

- ISDN 号没生成 → 按"安装号、DDI 翻译器、补充号"顺序排查，最后查前缀；改过 PCX 数据先重同步（n11/n12）
- 点了号码不响 → 依次查关联话机定义（分机+密码）、STAP 权限、主叫话机是否 SIP 话机
- 号码前缀不对 → 先核对 Prefix to delete 的"匹配头"语义是否被当纯删除理解（n14）
- 想用个人呼叫号码（Private Calling Number） → 原书标注 FOR INFORMATION ONLY 未验证（n13），先测试环境演练
- 需要真实运营商中继参数 → 实验模拟器口径不可用于生产，转客户中继方案（nr-08）

输出契约：可用的点击外呼系统 + 属性规则关联表 + 拨测记录（主叫话机、目标号码、结果）。

## B — 边界

- SIP 话机全线不支持 STAP 与 Click to Call（n10，含 MicroSIP/SIP extension）：交付前先盘点话机类型
- ISDN 号不自动更新（n11）：PCX 数据变更后必须重新同步
- 前缀规则是 8770 侧"迷你 ARS"，与 PCX 自身 ARS 独立；两者并存时单规则方案（p284）
- 通话媒体质量、中继侧路由属语音与运营商域，本书不覆盖
- 实验号码（33210N41000 族等）全部为实验口径（n47），生产以客户 DDI 段替换
