# 监督组（话务监督、进出组与代接）

## R — 原文依据

> "Each group is a set of 2 or more members of the same type (group of Conversation users or group of Connection users) 40 members maximum per group"（p497）
> "An user can only be declared in one group Group members may be declared on different OXE nodes but must be attached to the same OT node (no multi OT)"（p500）
> "No link with OXE supervision feature (no management synchronization)"（p501）
> "The OXE routing is prior to the OT supervision group feature: - Incoming calls to a supervised member, with an immediate forward to a non supervised destination, are not monitored by OT supervision group."（p502）

出处：OPENXTE300EN p494-513。

## I — 自述

OT 监督组是管理员建删改的话务监督单元：同类型成员（Conversation 组或 Connection 组）2-40 人，每成员角色为 Supervisor（看全组话务、收通知、可代接）、Supervised（被监督、可进出组）或双职。

规格与边界：

| 维度 | 口径 |
|---|---|
| 组规模 | 每组 2-40 名同类型成员 |
| 系统上限 | 500 组 |
| 监督链 | 500-1500 用户系统 4000 条；3000-5000 用户系统 6000 条 |
| 归属 | 成员可跨 OXE 节点，但必须挂同一 OT 节点（不支持多 OT） |
| 一人多组 | 不允许，每人只能属于一个组 |
| 许可 | 无专用许可（监督本身免费） |

模式、进出组与代接三要点：

- 工作模式两档：Regular（被监督者看不到他人）与 Collaboration（OTC PC 专属，被监督者可见全组与富在场；话机上即使组设为 collaboration 也按 regular 跑）
- 进出组经 OTC PC、手机或 TUI 前缀（OT 侧 Join or leave group 前缀 + OXE 侧同名 External Voice Mail 走 ICM 网关）
- 代接走 OXE Direct call pick-up（需在 OXE 侧建前缀并在类目启用），仅 Connection 用户组需要

三对易混边界：OT 监督组与 OXE 话机监督键是两套机制、无联动；OTC PC One 无监督功能；OXE 呼叫路由优先——立即前转到非监督目标、忙/无应答前转、副号码呼叫都可能脱离监督（Twinset 副站本身被监督，只监督主号码）。

## A1 — 书中案例

**监督组实验**（p508-513）：

1. 8770 中 OT 节点 Features 页建监督组并选 regular 模式。
2. 组内逐个加成员并勾 Is Supervisor 与 Is Supervised。
3. 双职成员同时勾两项；核对每组不超 40 人。
4. OT 侧 Telephone prefixes 配 Join or leave group 前缀。
5. OXE 侧对同值建 External Voice Mail 走 ICM 网关。
6. OXE Translator/Prefix plan 建 Direct call pick-up 前缀。
7. 用户类目的 Phone Facilities Categories 启用代接。
8. 测试：被监督成员来话，监督员客户端收通知并代接。
9. 验证进出组：客户端操作或话机拨进出组前缀。

## A2 — 未来触发

使用情境：主管要看全组来话并代接；组员要临时退出监督；评估监督覆盖有没有漏洞；话机监督键行为为什么不受 OT 组控制。

语言信号：监督组 / supervision / 主管 / 话务监督 / 代接 / pickup / Direct call pick-up / 进出组 / Join or leave group / Regular / Collaboration / 40 人 / 500 组 / 双职。

与相邻能力区分：话机副站与 Twinset 前缀 → 客户端能力；OXE 话机监督键是另一套机制（n32）；OXE ACD 呼叫中心不在本书范围。

## E — 可执行步骤

输入契约：组员名单与角色（跨 OXE 节点时核对同一 OT 归属）；进出组与代接前缀值规划；监督覆盖范围承诺。

1. 建组派角色。完成标准：2-40 人、一人一组、同 OT 节点
2. 配进出组前缀两侧成对（OT 前缀 + OXE External Voice Mail）。完成标准：进出组生效
3. 配代接前缀并在类目启用。完成标准：代接成功
4. 交互边界核对（前转/溢出/副号码）。完成标准：覆盖承诺与 p502 交互表一致

判停点：

- 客户要"所有来话都可见" → 前转与溢出会让呼叫脱离监督，按交互表核对再承诺
- 想一人进多组 → 不支持，一人一组
- 成员分属两台 OT → 不支持多 OT，重新规划归属
- OTC PC One 用户要监督 → 该模式无此功能，升 Desktop 或换客户端
- 话机上要 Collaboration 行为 → 设计按 regular 跑，预期管理

输出契约：监督组配置记录 + 代接与进出组测试证据 + 覆盖边界说明（给客户的承诺口径）。

## B — 边界

- 实验口径（生产按现场计划替换）：组名 Connection_SG、模式 regular、进出组前缀 44、成员 Barkley/Boop/Backman。
- 监督功能无专用许可；更细 provisioning 上限见 Features list 与 Product limits（书外指针，p507）。
- Collaboration 模式仅 OTC PC 生效；话机上按 regular 跑（p500）。
- 只监督主号码；Twinset 副站本身被监督（p502）。
- 与 OXE 话机监督键无同步；Connection 用户可两套并用，代接走 OXE Direct call pick-up（p499-501）。
