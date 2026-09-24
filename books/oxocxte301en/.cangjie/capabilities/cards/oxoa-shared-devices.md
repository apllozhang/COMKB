# 共享终端：站群监督、Hot Desking 与 Multiset

## R — 原文依据

> "Allows you to monitor multiple directory numbers simultaneously … the supervisor is notified by 3 ways • A pop-up display … • An audio tone … • The Groupware supervision key blinking"（p112）
> "Number of supervision keys on the system, up to 50"（p114）
> "It consists in allowing any Hot Desking User (HDU) to use any Hot Desking Position (HDP) in the company … the previous HDU will be first automatically logged out"（p174-175）
> "Hot Desking User: 2 are free of charge, then by package of 50 • Max capacity: 200 Hot Desking Positions / 200 HD users"（p174）
> "One primary set and a maximum of two secondary sets • One directory number • Same level of service for every associated set"（p185）

出处：OXOCXTE301EN p111-118, p173-192。

## I — 自述

三个"一人多机/一机多人"功能，各自解决不同场景：

| 功能 | 场景 | 规格 | 关键口径 |
|---|---|---|---|
| 站群监督 | 前台/助理盯多台话机 | 每键最多 8 号、系统 50 键 | 通知三路（pop-up 5 秒 TmpMenLTim/音调/键闪烁 3 秒 NotiAppTim）；监督方仅 DeskPhones；priv=yes 呼叫不可监督；3 方会议/应用内/ACD 登录时不能应答 |
| Hot Desking | 工位共享、个人环境跟随 | 200 HDP/200 HDU；HDU 前 2 免费、后按 50 包 | 前缀 683 登录/682 注销；抢占登录自动注销前一 HDU；个人环境含 VM/日志/键配置/路由等；监督走 Webdiag Services（可强制 Log out）+OMC 双通道 |
| Multiset | 一人多话机（主有线+副 DECT 即 Twinset） | 1 主+最多 2 副，共享主站目录号与服务级别 | 副站继承主站 14 项功能；空闲副站新呼叫按 MLTSETRING（01 不铃默认/02 短铃/00 长铃）；组呼全铃；外呼显示主站号；秘书不能当经理副站 |

两键成对：Supervision Groupware（监督）+ Audio Signal Supervision（蜂鸣开关），配完必须在监督话机上激活键（n14，两处 Note）。注意本卡的 Twinset 是 PBX 内话机组，与 Rainbow 侧同名概念（虚拟副站）不同物。

## A1 — 书中案例

**站群监督实验**（p116-118，厂商实验）：

1. 取一台话机作监督台，监督另外两台的内部号与 DDI 号。
2. 监督台 Details/Keys 建 Supervision Groupware 键，Monitored No 填号码并勾 Audio control。
3. 验证并测试——别忘了在监督话机上激活该键（p117）。
4. 再建 Audio Signal Supervision 键用于开关蜂鸣。
5. 测试：不摘机应收到通知（pop-up+音调+键闪烁）并可应答。

**Hot Desking 实验**（p178-183，厂商实验）：

1. 空闲 Premium/ALE Deskphone 勾 "Hot Desking set"（实验结束记得停用）。
2. Add 建 Hot Desking User（N° 122、Name Philippe，实验口径）。
3. 内部编号计划核对前缀：683 登录、682 注销。
4. Webdiag Services tab 看 HDU↔HDP 占用，可用 Log out 强制断开。
5. 测试：683 登录取回个人环境，682 注销。

**Multiset 实验**（p190-192，厂商实验）：

1. 主用户（101）Details 的 multiset 菜单 Add 副站 102。
2. 七项行为逐条验证：呼主站全铃、呼副站仅副站铃、副站外呼显示主站号、副站转移后呼主站按转移走、寻线组组呼全铃、经理秘书 screening 场景全铃（p191-192）。

## A2 — 未来触发

使用情境：助理要帮老板接电话；多号码同时盯；开放工位办公；热桌制；一人既有座机又有 DECT 手机；副站来话不响铃；配了监督键没通知。

语言信号：监督 / supervision / Groupware / 代接 / pop-up / Hot Desking / 热桌 / HDU / HDP / 683 / 682 / 工位共享 / Multiset / Twinset / 副站 / secondary set / MLTSETRING / 振铃。

与相邻能力区分：Rainbow 侧话务台与监督组属 starter bundle；DECT 手柄作 HDU 副成员的无线部署归 DECT 能力；MLTSETRING 这类 noteworthy 地址的修改流程归维护工具能力。

## E — 可执行步骤

输入契约：监督关系清单（谁盯谁）、工位与用户清单（HDU/HDP 配对）、multiset 主副分配、license 余量（HDU 前 2 免费）。监督方非 DeskPhone → 判停换机型或改方案。

1. 站群监督：监督台建 Supervision Groupware 键（每键 ≤8 号）+Audio Signal 键；在话机上激活键。完成标准：通知可达
2. Hot Desking：空闲话机勾 Hot Desking set；建 HDU；核对 683/682 前缀。完成标准：登录注销可用
3. 监督双通道：Webdiag Services 看占用并可强制 Log out；OMC 订阅户详情互查。完成标准：占用可视
4. Multiset：主站 Details 加副站（最多 2 个）；按需调 MLTSETRING。完成标准：主副同号
5. 验证：通知三路与应答、683/682 与抢占注销、七项呼叫行为对照预期。完成标准：行为闭环

判停点：

- "配了但没通知" → 先查监督键是否已在话机上激活（n14），再查 priv=yes 呼叫（不可监督）
- 监督员常在 3 方会议/ACD 应用中 → 通知无法应答（n13），改排班或换人
- 抢占登录会踢当前通话中的 HDU → 交付前向客户说明该行为（p175）
- 照抄 Multiset 实验截图 → 注意 p191 法文残留步骤（nr-03），以英文正文选 101 为主

输出契约：监督关系表 + HDU/HDP 分配表（含 license 计数）+ multiset 清单与铃型口径 + 行为验证记录。

## B — 边界

- Hot Desking 需 license：前 2 个 HDU 免费、之后按 50 一包；容量 200/200
- 适用终端：Hot Desking 支持 ALE DeskPhone、IP Desktop Softphone、模拟话机；DECT 手柄可作 HDU multiset 副成员
- 监督键系统上限 50；pop-up/通知时长由 noteworthy（TmpMenLTim/NotiAppTim）调节，改动走维护工具流程
- 实验人名/分机号（Philippe、122、101/102）为实验口径；生产按客户清单
- 与 Rainbow 侧 Twinset/监督组同名不同物：跨 bundle 咨询先问清是 PBX 侧还是 Rainbow 侧
