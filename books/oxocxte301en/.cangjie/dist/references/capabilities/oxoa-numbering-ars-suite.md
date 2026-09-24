# ARS 路由套件：三表协作、多运营商分流与 Internal ARS 时段路由

## R — 原文依据

> "Number Dialed / Numbering Plan / ARS Table / Trunk Groups Lists … Manage the ARS Prefix … Analyze the dialing number • Modify the dialing number • Select the trunk group list"（p195）
> "Principle: Addition / Absorption / Substitution / No modification (Transparency)"（p202）
> "Routing calls via mobile GSM gateway • Routing other calls via a VoIP provider (Lowcost) • ISDN backup overflow in case of saturation or for fax calls"（p197）
> "The DDI number 0388408571 is analyzed in the Public Numbering Plan • Function: Secondary Trunk Group • Base: ARS … Create a fictive Provider for each destination"（p228-230）
> "The internal ARS uses a virtual trunk groups local … Find 'Local' in the list of trunks and select it."（p237）

出处：OXOCXTE301EN p193-205, p225-241, p449。

## I — 自述

ARS（Automatic Route Selection）按被叫号码与可选时段自动选中继组，饱和或故障时溢出，对用户透明；适用于任何中继、呼叫、接入与拨号类型。三张表协作：

| 层 | 表 | 职责 | 关键字段 |
|---|---|---|---|
| 1 | 编号计划 | 识别拨号并触发 ARS | Main/Secondary Trunk Group base=ARS、NMT Keep/Drop |
| 2 | ARS 表 | 前缀匹配 + 号码变换 + 选列表 | Network Priv/Pub、Prefix 区间、Substitute、TrGpList、子线 |
| 3 | 中继组列表 | 按索引顺序选路 | List ID、索引、Char 显示字符、Access digits |

号码变换四原则：加前缀（Addition）/吸收（Absorption）/替换（Substitution）/透明（Transparency）。

**多运营商分流标准构图**（p197-201）：移动 06 前缀走 GSM 网关（TrG400）、其它呼叫走低价 VoIP（TrG402）、ISDN（TrG401）做备份。两个中继组列表共享同一子线索引（列表 1=[2:400, 3:401]、列表 2=[4:402, 3:401]）实现 ISDN 溢出；传真强制走 ISDN 用流量分担矩阵（400=-、401=+、402=-）。

**Internal ARS 反转用法**：把一个入站 DDI 按日组+时段路由到不同内部目的地。五级决策链：

1. 公网编号计划：DDI 段 Function=Secondary Trunk Group、Base=ARS、NMT=Keep
2. ARS 表：前缀匹配后按子线 Substitute 替换为分机号（替换前缀随后在内部编号计划分析落地）
3. 虚拟 Provider：每目的地建一个假 Provider（如 "Extension 101"）
4. 中继组列表：Index 选 Local（虚拟中继组）配对应 Provider
5. Day Groups + Hours：星期映射组号，时段表按"组号→Provider"排目的地，兜底行给消息

## A1 — 书中案例

**多运营商三路分流**（p197-201，讲义示例）：

1. 编号计划加 Main Trunk Group base=ARS。
2. ARS 表两行：06 走列表 1（GSM）、透明行走列表 2（ADSL）。
3. 列表 1=[2:400 G, 3:401 I]、列表 2=[4:402 V, 3:401 I]，共享子线 3 做 ISDN 溢出。
4. 传真走流量分担矩阵强制（401=+）。

**Internal ARS 实验**（p232-241，厂商实验）：

1. 目标：打 DDI 021PN41102——工作日分段转 101/102/103，其余时间播营业时间消息（实验口径）。
2. 公网编号计划选 Secondary trunk group，start/end 填 41102，Base 填 ARS。
3. ARS 前缀右键 Add 填全号，subline add 三次（每行一个目的地）。
4. Providers Destination 加 4 个虚拟 Provider（Extension 101/102/103/Message）。
5. Trunk Group Lists 每行 Index 选 Local、Provider 列选对应项。
6. Day Groups 设周六日组 1、其余组 2；Hours 建 4 时段（段尾=下一段起点）。
7. 录 MSG1 欢迎消息挂到未用寻线组 501（勿与实体 MoH 混淆，p241）。
8. 不同时刻打 DDI 核对四时段目的地（p241 验收）。

## A2 — 未来触发

使用情境：多运营商降费方案；移动呼叫走 GSM 网关；ISDN 备份溢出；传真强制走特定线路；一个 DDI 营业时间转人、非营业时间播语音；分时段来电分配；ARS 表怎么规划前缀。

语言信号：ARS / Automatic Route Selection / 选路 / 中继组列表 / trunk group list / 前缀 / prefix / 号码变换 / 替换 / substitute / 溢出 / overflow / 多运营商 / Internal ARS / Day Groups / Hours / 时段 / 虚拟 Provider / Local。

与相邻能力区分：SIP 网关本身的配置（九 tab/注册）归 SIP 组网能力；远程替代的 # 前缀回环是 Internal ARS 的姊妹用法（见语音邮箱与移动能力）；游牧 CLI 规则归移动能力。

## E — 可执行步骤

输入契约：运营商前缀与费率策略、中继组清单、目的地清单（分机/寻线组/消息）、营业时间表。前缀规划未定 → 判停先做拨号规范，ARS 只执行不设计。

1. 编号计划触发：目标号段行 base 填 ARS（外呼 Main / 内部目的地 Secondary）。完成标准：拨号进入 ARS
2. ARS 表建行：Network/前缀区间/Substitute/TrGpList；溢出用子线（同 Network 第二目的行）。完成标准：匹配与变换成文
3. 中继组列表按优先级排索引，需要显示确认的设 Char 字符。完成标准：列表有序
4. （多运营商）两个列表共享备份子线索引；传真等强制业务走流量分担矩阵。完成标准：溢出路径成立
5. （Internal ARS）每目的地建虚拟 Provider，列表 Index 选 Local。完成标准：内部目的地挂接
6. Day Groups 映射星期，Hours 按段排目的地（段尾=下一段起点），兜底行给消息寻线组。完成标准：时间矩阵闭环
7. 验证：外呼看中继组占用与 Char；打 DDI 核对各时段目的地。完成标准：行为与设计一致

判停点：

- 时段口径两处原文不一致（p233 12-13/13-18 vs p449 12-14/14-18，nr-01）→ 按四时段机制描述，交付文档统一自家口径
- 欢迎消息录制位置 → 挂寻线组的 MSG1-20，不要录进实体 MoH（n24，两处 Be careful）
- 生产前缀规划照抄书例 → 禁止：示例口径（p198-201）须按运营商前缀重新规划
- ARS 溢出仍不通 → 先查带宽闸门（Media 最少 5 通话）与 Link-Cat，再查子线方向

输出契约：ARS 三表配置记录（编号计划/ARS 表/列表）+ 分流与溢出验证结论 + Internal ARS 时段矩阵（含交付口径声明）。

## B — 边界

- 详细字段格式以 OMC 屏幕为准（p196 表格）；书例数值为示例口径，生产须重规划
- Internal ARS 时段两处原文不一致（nr-01/n23）；链路类别取值讲义与实验不同（nr-06）——机制为准，取值自洽即可
- ARS 不做话务建模：前缀怎么规划、时段怎么定属方案设计方法论，书内不教（最强反对意见见 BOOK_OVERVIEW）
- 虚拟 Provider/Local 是"内部目的地"技法，不产生真实外线流量；混淆会导致排障方向错
- 时间相关的所有表（Day Groups/Hours/开闭计划）修改后建议重启相关业务验证，书内未给统一生效口径
