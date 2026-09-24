# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 成员配号订阅门槛括注缺 Voice Phone

- **位置**: p194 "A MEMBER MUST HAVE A VOICE SUBSCRIPTION (VOICE BUSINESS, VOICE ENTERPRISE OR VOICE ATTENDANT) TO ASSIGN A PHONE NUMBER."
- **差异**: 括注列三档，未含 Voice Phone；而 p66（"Each member must have a Voice subscription...: Voice Phone • Voice Business • Voice Enterprise • Voice Attendant"）与 p67 订阅表均为四档口径，Voice Phone 是"硬话机上的全部话务特性"的正牌电话订阅。
- **影响**: 纯硬话机用户（Voice Phone 档）配号时，按 p194 字面会被拒、按 p66 应该可行；两页答案不同。
- **处置**: 能力卡按 p66 四档总口径表述（"持任一 Voice 档即可配号"），并注明 p194 括注疑为不完整列举（原文如此）；现场若遇 Voice Phone 用户配号受限，以平台实际行为为准并记录。

## nr-02 Hunt group 溢出秒数两处口径并存（易混淆，非矛盾）

- **位置**: p210-211 图示 "If overflow 60 secondes by default" vs p215 "overflow time (adjustable from 10 to 900 sec)"。
- **判断**: 适用对象不同——60 秒是**无队列组**图示的默认溢出定时；10-900 秒是**带队列组**的可调溢出等待上限（FCFS 派号延迟另为 10 秒）。
- **处置**: 能力卡分开表述并各自标注页码；引用"默认 60 秒"必须带"无队列组"限定（另注：原文 "60 secondes" 为法语拼写照录）。

## nr-03 BP 专属"四项"与 Reseller"五项独占"计数差异（互补口径）

- **位置**: p49 四项（Cloud PBX 声明激活/付费订阅/终端声明/电话线加装携转）vs p58-59 五项（再加 The company 与 Public numbers (DID)、Extensions——从"可创建元素"角度列举）。
- **判断**: p49 按"操作"口径、p58 按"可创建元素"口径，互补非矛盾；但两处清单字面不一致，直接引用任一处都会被质疑。
- **处置**: 能力卡以 p49 四项为主口径、p58 五项为补充口径，并说明视角差异；客户管理员"点不出"公司/订阅/PBX/DID/分机入口均属权限设计。

## nr-04 认证科目按产品线区分（与 RAINXTE001EN 口径不同）

- **位置**: p341 "The ESR will only be created if the partner is certified on Rainbow Hub"；混合云教材同位置为 "certified on Rainbow"。
- **判断**: 两本教材各按自己产品线表述认证科目——做 Hub 项目要 **Rainbow Hub 认证**，不能拿混合云认证替代；MyPortal 表单 Product Category 同样区分（本书 "=Rainbow Hub"，混合云教材 "=Rainbow"）。
- **处置**: 维护支持卡 Boundary 显式呈现跨书差异；项目启动核查认证科目，非认证伙伴先补认证或经认证上家转报。

## nr-05 原文笔误与语言残留集合（引用时注意）

- p62 "allow **to to** distribute"（重复）。
- p107/p149 "lo**we** worker protection"（应为 low）；p107 同页 EM20/EM200 并写（仅 EM200 展开）。
- p136 "SSH (**si activé**)"（法语残留，=若启用）；p179 "**Unidirectionnel**"、"**Connecteur**"（法语残留）。
- p144 "require at least **the the** following firmware"（重复）。
- p192 "RAINBOW **PLATEFORM**"（拼写）。
- p240-241 "**BY DEFAUT**"、"USING WITH WAY"（拼写/表述残留）。
- p210-211 "60 **secondes**"（法语拼写）。
- **处置**: 原文引用保留并注明"原文如此"；转述时用正确拼写。

## nr-06 实验环境值仅限实验口径（不入生产）

- **位置**: p17-34（POD/账号/号段/网段）、p17/p68/p74（培训禁预付三处警告）、p191-192（实验密码与邮箱）。
- **判断**: 账号（bpX.rv1@.../aliceX...）、密码（Superuser-P*/PasswordP*，实验口径）、号段（02982967X0-X9）、网段（192.168.1.x）均为教学给定值；"仅月付禁预付"是培训商务规则，生产预付是正常计费方式（p65）。
- **处置**: 环境值仅进 Boundary 与 book/overview；能力卡正文不出现具体实验密码；引用容量与行为规则时与实验规则分开。

## nr-07 Voice Attendant 设备限制的两层表述（引用要分开）

- **位置**: p67 订阅表 "This subscription does not support hardphones — Devices: PC only" vs p246 "the phone set association is deleted after activation of the attendant console"。
- **判断**: 前者是订阅的设备定位（不卖硬话机形态），后者是话务台激活的联动行为（已配话机被解绑）——两层口径并存，非矛盾但语义不同：前者是选型约束，后者是存量用户的破坏性变更。
- **处置**: 话务台卡两层分开写；给既有话机用户加话务台前必须先告知"话机关联会被删"。

## nr-08 含推断/提示性表述一处（引用需带标注）

- n39 的"漏讲会造成延误报警的重大事故风险"为培训提示性表述，非书内事实陈述；counter-example 自检已声明其余条目均有原文直接支撑。
- **处置**: 紧急组语义按 p228 原文呈现；培训提示性表述保留"提示"定性，不升格为书中明示事实。
