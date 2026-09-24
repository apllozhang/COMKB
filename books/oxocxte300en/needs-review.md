# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 自动配置版本门槛两处表述不一致

- **位置**: p366 "available from system version R4.0.020.002"（讲义）vs p395 "applies to versions greater than R4.0.020.002"（实验手册）。
- **差异**: "from"（含该版本）与 "greater than"（高于该版本）语义相差一个版本点。
- **影响**: 版本恰好等于 R4.0.020.002 的站点能否用自动配置，两页答案不同。
- **处置**: 能力卡 Boundary 注明两处原文口径；实践建议取"≥R4.0.020.002 可用、生产以更高版本执行"；低版本先升级。与 RAINXTE001EN 同源问题，两 bundle 口径保持一致。

## nr-02 话务员 DDI 与安装号尾段全书两值并存

- **位置**: p21（ITSP1 参数）与 p229（SIP 章）写 "41000 base 9 DDI Operator group / Attendant call: 41000、Installation number: 210P41000"；p46（数据采集）却写 "Attendant: 41100"；p447（安装向导实验）安装号写 "0210141100"（尾段 41100，与 210P41000 按 P=1 展开的 0210141000 不符）。
- **判断**: 原书两口径并存（疑 p46 话务员 DDI 笔误、p447 为课堂实例值）。p229 的规范格式示例 "+33 (0)2 10 1 41000" 与 p21/p229 自洽。
- **处置**: 引用实验值时按所在章节原文并标注"实验口径"，不跨章混用；生产按运营商真实分配的安装号与话务员 DDI 为准，不采信任何一处具体值。

## nr-03 Hunt group 分发类型讲义与实验用词不一

- **位置**: p137 讲义表 "Sequential / Circular / Parallel"，p145 实验步骤 "Test Cyclic and Parallel Types"。
- **判断**: Circular 与 Cyclic 同指轮转分发，原书两种拼写并存（原文如此），OMC 界面以实际下拉为准。
- **处置**: 能力卡转述用"轮转（Circular/Cyclic）"并注两处出处；不做无据的界面拼写断言。

## nr-04 法文残留与未解释术语

- **位置**: p88 "IMPORTANT: N'oubliez pas d'activer Autoprovision dans le menu liste des postes"（未翻译法文）；p27 "Bornes DECT / Combinés DECT / Hybride TDM/IP"（法文图注）；p58 "LOLA mode" 与 p322 "close to that of Lola installation"（LOLA/Lola 全书无定义）。
- **处置**: 法文句在卡中引用时给中文转述（别忘了在话机/基站列表菜单激活 Autoprovision）并注"原文为法文"；LOLA 按上下文理解为出厂引导/安装态，不升格为书中定义；细节以最新版英文文档为准。

## nr-05 task-16/17/18 无独立 How-To 实验（原书结构事实）

- **位置**: 软件下载（p315-320）、系统复位（p321-324）、安全警告（p325-329）均为讲义形态，全书 25 个实验章不含对应 How-To。
- **处置**: 非提取遗漏。操作序列由 f33/f34、p18 与 counter-example 组承载；能力卡的 E 段按讲义口径给动作入口并注明"讲义口径、无书内实验验收"。

## nr-06 容量表 70/100/150 用户行为方向性参考

- **位置**: p392 表 (*) 注：集成拓扑用户上限取决于配置通道数与用户话务，"Value indicated here is for direction only for 20 configured WebRTC GW channels"，150 仅极低话务可达。
- **处置**: 引用 70/27、100/36、150/50 三行必须带"20 通道+方向性参考"前提；售前承诺先做话务评估（工具与建模在书外）。

## nr-07 含推断成分的结论（引用需带标注）

- n19: "漏配 Inhibition Time-ranges 是时段限呼不生效的最常见原因"——结合默认行为与注释语气的推断。
- n15: 生产 SIP 加密/TLS 要求取决于运营商与 TC1284——书内只给实验不加密口径。
- n24: 信箱弱密码是盗打主要入口——结合 p184/p326 位置的推断。
- n26: 自改 Rainbow 域名会断开连接——由 "Leave the default value" 祈使语气推出。
- n38: 8328 admin/admin 部署完必须改——由 p326-329 安全基调推出。
- **处置**: 五条均已标"（推断）"；能力卡引用时保留推断标注，不升格为书中明示事实。

## nr-08 原文笔误若干（引用时注意）

- p326-327: "The **freaking** is a business run by organised crime"（应为 phreaking）；"victims can **loose** more than 20 K€"（应为 lose）。
- p201: "120 **Simultaneaous** SIP trunks"（应为 Simultaneous）。
- p454: "8328 SIP-DECT SINGLE BASE **SATION**"（应为 STATION）。
- **处置**: 原文引用保留并注明；转述时用正确拼写。
