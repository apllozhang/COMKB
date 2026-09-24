# 多实体与伪多公司（Entity 隔离、MoH 分离、分账外线）

## R — 原文依据

> "The system supports 4 Entities … Call restriction between user of different company … Attendant Group • Common for all entity • No call restriction"（p243-244）
> "Number of entries for individual greetings: from 15 to 200 • Number of preannouncement messages: from 8 to 20 • Message duration: from 128 to 320 seconds"（p248）
> "Manage a traffic sharing link category level for the A extensions: 3 for example … Modify the traffic sharing matrix by creating a straight line from 1/1 to 16/16"（p250）
> "Each company will be able to dial the same main trunk group prefix … Each company will take their own external lines to avoid problems according to metering bills"（p249）

出处：OXOCXTE301EN p242-261。

## I — 自述

两级"共享系统"方案：多实体是系统内建隔离，伪多公司是在多实体之上用流量分担实现分账。

**多实体（最多 4 个）**：

| 机制 | 口径 |
|---|---|
| 实体归属 | 用户默认实体 1，逐话机在 Details/Entity 关联 |
| MoH 隔离 | 每实体独立 MoH（保持方实体决定播哪个），每段最长 10 分钟（license：4 实体 MoH-10 分钟） |
| 呼叫禁止 | "Do not allow internal calls between multi-tenant entities" 开关连带影响：立即/忙转、RSL 键、个人代接、文本/语音邮箱；话务员组话机不受限（n25） |
| 系统限制增强 | 个人问候增至 200 条、预告消息增至 20 条、消息时长增至 320 秒；计费小票含实体信息 |

**伪多公司四步法**（p250-251, p257-261）：

1. 话机管理：A 公司话机流量分担链路类别=X，B 公司=Y（讲义例 3/4、实验 1/2，自洽即可，nr-06）
2. 副中继组：A 的中继组类别=X、B 的=Y（话机类别=本公司中继组类别，配对成立）
3. 流量分担矩阵：拉 1/1 到 16/16 直线（类别相同才可互走）
4. ARS：主中继行 base 改 ADL 进 ARS 表，加透明线；中继组列表含两公司中继组并设 Char 1/2

效果：两家公司共享一台 OXO、同一外拨前缀，各走各的外线、账单分离；外拨时话机显示 Char 1 或 2 确认占了本公司中继组。

## A1 — 书中案例

**多实体与伪多公司实验**（p252-261，厂商实验）：

1. 拓扑：100/101 属实体 1、102/103 属实体 2；实体间禁呼；每实体独立 MoH。
2. 实体分布：Details/Entity 把 102、103 放实体 2。
3. Feature design/Part 1 勾 "Do not allow calls between entities"；验证跨实体被禁。
4. 按实体录 MoH1/MoH2（MMC Operator session 或 OMC；勿与 MSG1-20 欢迎消息混淆，p256）。
5. 话机链路类别：公司 1 话机=1、公司 2 话机=2（实验口径）。
6. 中继组 400 类别设 1、401 设 2；流量分担矩阵按直线配置。
7. 主中继行 base 改 ADL；ARS 表加透明线（列表 1）；列表内 Char 1 给公司 1、Char 2 给公司 2。
8. 测试：跨实体呼被禁、保持听各自 MoH、两公司拨 0 外呼显示各自字符 1/2（p255-261）。

## A2 — 未来触发

使用情境：两三家小公司合租一套 PBX；楼宇/园区共享系统分账；分公司要独立保持音乐；实体之间要禁止互呼；外呼要分清哪家公司的线路账单。

语言信号：多实体 / entity / 多租户 / multi-tenant / 实体隔离 / 伪多公司 / pseudo multi-company / MoH / 保持音乐 / 分账 / 流量分担 / traffic sharing / 链路类别 / link category / 矩阵 / Char。

与相邻能力区分：ARS 三表机制归 ARS 套件能力；账号码记账（按客户/项目而非按公司）归酒店与计费垂直能力；多实体 MoH 录制的 MMC 入口与欢迎消息的区分见语音邮箱与移动能力（n24）。

## E — 可执行步骤

输入契约：公司数（≤4）、用户与实体分配表、各公司中继资源、是否禁实体间呼叫、MoH 素材。公司数超 4 → 判停：超出系统上限，改多系统方案。

1. 实体分配：逐话机 Details/Entity 归属（默认实体 1）。完成标准：归属落表
2. 隔离开关：按需勾实体间禁呼；向客户说明连带影响清单（转接/RSL/代接/邮箱，n25）。完成标准：隔离生效且预期一致
3. MoH：按实体分别加载（MMC 或 OMC），与 MSG 欢迎消息分清。完成标准：各实体保持音乐独立
4. 伪多公司：话机与本公司中继组设相同链路类别；矩阵拉直线。完成标准：配对成立
5. ARS：主中继行 base 改 ADL、透明线入列表，列表含两公司中继组并设 Char。完成标准：同前缀各走各线
6. 验证：跨实体呼被禁、MoH 各自播放、外拨显示对应 Char、小票分账。完成标准：三隔离闭环

判停点：

- 需要真正的数据隔离（用户/话务员互不可见）→ 多实体是"伪多租户"：用户与话务员组仍共享（BOOK_OVERVIEW 术语口径），超预期则改独立系统
- 话务员组需求 → 话务员组对所有实体公共且不受限，无法按公司隔离（p244）
- 实体间仍需部分互通（如转接）→ 逐项对照 n25 连带清单再定开关
- 链路类别取值 → 讲义 3/4 与实验 1/2 并存（nr-06），取一套自洽值即可，不照抄

输出契约：实体分配表 + 隔离开关与连带影响确认单 + 链路类别配对与矩阵记录 + 外拨 Char 验证结论。

## B — 边界

- 容量与 license：4 实体上限；每实体 MoH 每段 ≤10 分钟需 license（多实体 MoH-10 分钟）
- 禁实体间呼叫的连带影响覆盖转接/RSL/代接/邮箱（n25）：设计跨公司协作流程前逐项核对
- 伪多公司靠"链路类别配对+ARS 透明线"实现记账隔离，非硬隔离：故障或误配时可能互走对方外线，交付前务必验证 Char
- 计费小票新增实体信息：对账模板需同步更新
- MoH 与 MSG1-20 欢迎消息共用 MMC 录制入口（n24）：录错位置表现为"来电播错语音/保持听错音乐"
