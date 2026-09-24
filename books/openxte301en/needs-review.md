# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 LDAP 溢出服务器上限两处口径不一致

- **位置**: p235 "Restrictions • LDAP version 3.0 or higher • 20 LDAP servers maximum • No referral"（讲义）vs p260 "Up to five LDAP servers can be declared in the OXE ... LDAP phone book Enter the phone book index (from 1 to 5)"（实验 How-To）
- **差异**: 同一特性两页数字打架——20 台 vs 5 个（OXE 侧 LDAP Phone Book 索引仅 1-5）。
- **影响**: 容量规划与引用口径；引用哪个数字决定方案表述。
- **处置**: 现场按实验页 5 个做 OXE 侧配置上限；讲义 20 的适用语境存疑（推断：可能指 OT/UDAS 侧目录数量），引用时注明出处页并以最新技术通报核实。候选 p24/n42 已完整记录。

## nr-02 tsa_maintenance "option 47" 在所列菜单中不存在

- **位置**: p57 同页两处矛盾——正文提示 "check ... by using option "47" again to dump all QMCDU, or, option "20" dump nomadic"，而同页 ACAPI 子菜单仅列 0-20（47 缺席；菜单 20 为 "Load Z IVR directory numbers"）。
- **判断**: 疑为原文笔误；dump/核验动作实际用 option 20（p55 主菜单 "20 [+ qmcdu] —— Dump Nomadic [or LightLine]"）。
- **处置**: 能力卡按 option 20 核验口径书写并标注 nr-02；保留 47 原文痕迹供对照。候选 p47/c04 已记录。

## nr-03 RADIUS 章 Notes 复制粘贴错误

- **位置**: p459 Notes 原文 "Here are all the parameters required to be able to connect to a LDAP directory"，该页实际内容为 plugin_radius.properties（RADIUS 插件参数）。
- **判断**: 原书复制粘贴笔误，非内容错误。
- **处置**: 以文件名与参数名（server.* / 1812/1813 / pap）为准理解；提示实验手册亦有人为错误，关键操作交叉核对 TC 文档。候选 p26/n47 已记录。

## nr-04 POD 服务器 IP 排版异常（原文如此）

- **位置**: p9/p17 两处印作 OXE 地址 "192.16.8.1.1 / 192.16.8.1.3"（同表其余地址均为 192.168.1.x 网段）。
- **判断**: 疑为 "192.168.1.1 / 192.168.1.3" 的排版变体；原文如此照录。
- **处置**: 实验口径引用时保留原文并标注"疑为 192.168.1.x 变体"；不以推断值冒充原文。候选 p06 已记录。

## nr-05 原书拼写/印误清单（引用时注意）

- p108 "CAN BE APLLIED AT A TIME"（应为 APPLIED）。
- p371 外部 DCS 兼容表 "Windows 2010"（应为 Windows 10）。
- p155 "changes the call routing profile to a completly time"（残句，语义按"切换到含 other and mobile() 的档案"理解）。
- p243/p245 "syhchronization"（应为 synchronization）。
- p167 "Drirectory number"（应为 Directory number）。
- p92 "Discriminitor"（应为 Discriminator，p128 起用正确拼写）。
- p57 菜单文案 "createe n call_log tickets"、"Load System parametere"（菜单原文如此）。
- **处置**: 原文引用保留并注明；转述时用正确拼写。

## nr-06 三处含推断成分的结论（引用需带标注）

- n42/p24: "20 可能指 OT/UDAS 侧目录数，OXE 侧 Phone Book 仅 5"——适用语境为推断，书内未明示。
- c04 核验口径: "State: Free(1) 或 Unknown 均算在库，关键是有条目且 Z nomadic=1"——为提取器归纳的核验判读，非原文逐字。
- f04 摘要中"蜂窝配置是 VoIP 的前提"的表述来自 p51 Warning（明确），但"权限成对出现"的概括（p03）为提取器归纳：三条许可组合各有原文出处，"成对"为概括性表述。
- **处置**: 三条引用时保留推断/归纳标注，不升格为原文逐字事实。

## nr-07 版本碎片化引用纪律

- **现象**: 全书各章版本前提不统一——R2.0（DAS 规则 7/8，p108）、R2.1 MD1（Extended Mobility，p161）、R2.2（iPhone QR，p161）、R2.2.x/R2.3（UM delegation 转 impersonation，p189）、R2.3.1（APNS 与日历在场，p98/p406）、R2.5（O365 Outlook 加载项，p178）、R2.6（RE 单设备化，p96/p134）；APNS Geotrust 根证书标注"有效期至 2022"（p98）。
- **影响**: 跨版本交付不能全书统一口径；过期时间标注（2022 证书）按今天环境必须重核。
- **处置**: 能力卡引用任何版本敏感行为时带章内版本口径；生产化前对照最新 release note 与 TC 通报（TC2341/TC2391/TC2258/TC2558/TC1623）。
