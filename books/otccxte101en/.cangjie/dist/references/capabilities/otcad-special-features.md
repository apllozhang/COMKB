# 特殊功能开关（优先转接、忙音、代接、监督监听、永恒整理、中继预留）

## R — 原文依据

> "Management • Applications/ CCd/ Pilot • Transfer with priority: True … Inter-guide tone Number: 2 • Redirection busy tone on DID: False"（p499-501）
> "Trunk Groups> trunk group … Max. % of trunks out CCD : 20 … Applications/ CCd/ Pilot/ Trunk limitation • Pilot Directory Number: 31600 • Max. % of trunk: 30"（p513-514）
> "Applications/ CCd/ Processing Group • Auto return to wrap up: True … Show Supervisor Listening: False/True"（p510-511）

出处：OTCCXTE101EN p498-530。

## I — 自述

特殊功能全部是"对象上的参数开关 + 行为验证"，按菜单归属分四类：

| 层级 | 菜单归属 | 开关 |
|---|---|---|
| Pilot 级 | Applications/CCD/Pilot/<号> | Transfer with priority（优先转接，双队列）、Transfer to pilot in redirection（劝恼转接）、Redirection busy tone on DID（饱和播忙音）、Inter-guide tone Number（默认 2 号音）、Pilot Supervised Transfer、Trunk limitation（Pilot 中继限额） |
| PG 级 | Applications/CCD/Processing Group | Auto return to wrap up（永恒整理）、Show Supervisor Listening（秘密监听）、Help On External Call（私话后可插入） |
| 坐席数据级 | Applications/CCD/CCD Users/CCD operations data management | Forwarding activ. On Logon/Logoff（登出即取消私号转发到信箱） |
| 系统级 | Translator/Prefix Plan + Trunk Groups + Categories > Phone Features COS | 功能前缀（#013 组内代接、#014 直接代接、Conversation Recording）、Max. % of trunks out CCD（业务中继预留）、COS 放行 |

中继预留两级数学（p513-514）：第一级按中继组——62 条 SIP 接入 × 预留 20% 约 12 条保底给非 CC 呼叫，剩 80% 约 50 条给 CCd，占比打满后新 CC 呼叫听忙音；第二级按 Pilot——限额以"CCd 可用池"为基数：15 ÷ 50 = 30%，即单 Pilot 最多同时占 15 条。

代接两前缀：#013 = 同处理组内代接（Agent processing group call pickup）；#014 = 直接代接指定分机（Direct call pickup）。均需 Prefix Plan 建前缀 + COS 类别 0 放行对应 Phone Features。

行为语义要点：转接饱和 Pilot 时参数两态提示语相反（false=转接方收"不允许转接"；true=被转方听劝恼引导、转接方听"可以挂机"）；队列饱和默认播 2 号间隔引导音，不是忙音。

## A1 — 书中案例

**八连配与逐项验证**（p516-530）：

1. 优先转接：Pilot 31601 开 Transfer with priority；转接呼叫在队列中优先于普通呼叫被接续
2. 劝恼转接：开 Transfer to pilot in redirection，true/false 两态各打一通对比提示语
3. DID 忙音：开 Redirection busy tone on DID，禁用劝恼队列后验证饱和从 2 号音变忙音
4. 组内代接：建 #013 前缀 + COS 放行，31501 拨 #013 截走同组 31500 正在振铃的呼叫
5. 直接代接：建 #014 前缀，两坐席不同组时拨 #014+分机号截 call
6. 监督转接：开 Pilot Supervised Transfer，Yes 时呼叫在询问期即分配到空闲坐席
7. 永恒整理：PG 勾 Eternal Wrap up（Pilot Wrap Up duration=200 秒，实验口径），整理期拨外线通话后回到剩余整理时间
8. 监督监听：PG 开 Show Supervisor Listening，班长按 listen ACD+坐席号，坐机屏显 "supervisor listening"
9. 中继预留：中继组 Max. % of trunks out CCD=20，Pilot 31601 Trunk limitation=30%，核对 62>50>15 链条

## A2 — 未来触发

使用情境：VIP 转接要插队；客户抱怨排队音"怪"；坐席要互相代接；班长要监听质检；坐席整理期要处理私事不打断计时；业务话务要给非 CC 呼叫保底中继。

语言信号：优先转接 / Transfer with priority / 忙音 / busy tone / 代接 / pickup / #013 / #014 / 监听 / Supervisor Listening / 永恒整理 / Eternal Wrap up / wrap up / 中继预留 / Trunk limitation / 劝恼 / dissuasion / 间隔引导音。

与相邻能力区分：队列水位参数（MWT/TSP/优先级）与互助溢出转 Remote PG 卡；坐席技能与档案配置转 ACR 对象卡（路由卡）；监听的法律合规在书外。

## E — 可执行步骤

输入契约：CCD 矩阵与坐席已在运行、要开的功能清单、WBM（mtcl）与 CCS 管理权。前置约束：ACD 前缀必须已建（n20）。

1. 逐项开参数：按上表菜单归属定位开关并保存。完成标准：界面回显 feature is enabled
2. 代接类先删同号冲突前缀再建 #013/#014，并在 COS 类别 0 放行。完成标准：话机上拨前缀有效
3. 每开一项立即做行为验证（按 A1 对应步骤设计主叫/坐席/班长角色）。完成标准：观察到的行为与参数语义一致
4. 中继预留先算后配：中继总数 × 预留百分比、CCd 池 × Pilot 百分比两级核算。完成标准：保底条数与限额符合设计
5. 转接类功能在 true/false 两态各测一遍再下结论。完成标准：两种提示语都能解释

判停点：

- 客户要求秘密监听 → 停，技术可配，但法律告知与合规边界书外零覆盖（n40），先过合规评审
- 队列满时的听感与预期不符 → 停，先核对"默认 2 号间隔引导音 vs 开忙音参数"这条行为链（n29），不当作故障
- 中继百分比要超出两级数学 → 停，先重算基数（预留以总数为基、Pilot 限额以 CCd 池为基），口径错配是常见错

输出契约：逐项功能开关记录 + 行为验证记录（含两态对比）+ 中继预留计算书。

## B — 边界

- 监听/录音功能只有操作没有合规（n40）：法律告知、隐私评估、录音留存策略必须在生产部署前补齐
- Wrap Up duration 与前缀编号为实验口径（200 秒/#013/#014）；生产按客户流程定义
- Inter-guide tone 的触发条件=拥塞+无劝恼选项（p500），与 DID 忙音参数的叠加行为要逐态验证
- 原书基于 R10.15 界面，菜单名与参数名随版本可能漂移；关键开关以现场界面为准
- COS 类别 0 默认含全员，放行前缀功能影响面是全系统，收口要另规划类别
