# 计费组织树与成本归属（成本中心、搬移权限、剪贴/复制语义、历史回溯与工具重建）

## R — 原文依据

> "Chargeable entry placed under cost center created in organization tree — If cost center defined in the PCX ... Chargeable entry placed under root of organization tree — If no cost center defined (cc=255) in the PCX"（p256）
> "Cut & paste • This operation consists in moving an entry without history ... Copy & paste • This operation consists in moving an entry with history"（p261-262）
> "The move of a subscriber from a cost center to another one is only possible from OXE configuration or directory applications. That's why such move is not authorized from the organization map."（p286）
> "TO ASSIGN CORRECTLY THE HISTORY FROM AN INACTIVE SUBCRIBER TO THE ACTIVE ONE, YOU MUST SELECT ITS DEVICE AND NOT THE USER."（p290）

出处：8770XTE201EN p251-295。

## I — 自述

组织树决定"钱归谁"：节点类型 level（层级）/cost center（成本中心）/chargeable entry（用户、话务台、数据终端、中继组等），同时呈现过去与现在（灰色历史条目）。

- 数据来源两条：OXE 同步或事件、公司目录的设备-个人链接变化——组织更新自动完成
- 归属规则：PCX 设了成本中心挂对应节点；cc=255 落组织根；中继组/话务台组/语音信箱等无成本中心对象落 Data collection 页签配置的"默认成本中心"
- 搬移权限二分：分机/用户的成本中心只能在 OXE 配置（Rights 页签）或公司目录改，组织图上剪贴会被拒绝；中继组等对象可以在组织图上自由剪贴（不影响话机侧）
- 操作语义四象限：

| 操作 | 语义 | 后果 |
|---|---|---|
| Cut & paste | 无历史搬移 | 原位置不留灰条目 |
| Copy & paste | 带历史另立 | 原件保留记录并转 inactive（灰色），粘贴件 active |
| Assign earlier creation date | 按身份回溯历史 | 只能选"设备"，把非活动条目记录重挂到同身份（PCX ID/分机号）活动条目 |
| ToolsOmniVista 组织更新 | 全局重挂 | 删除全部非活动实体，票据与 Ptp 计数器重挂到活动实体；强制停 8770 服务 |

- 回溯边界：level/成本中心/人（person）不可回溯，残留的非活动成本中心要手工删；新日期须早于条目现创建日期、晚于等于最后一条对应非活动条目日期
- 灰色条目是历史追溯机制不是垃圾数据，全局更新前它们承担记录归属

## A1 — 书中案例

**组织树搭建与搬移实践**（p268-288）：

1. Data collection 页签设 Default cost center=CC_OXE 后做完整同步
2. Organization 页签清空旧条目，灌测试票并 Compute cost（勾 Force）
3. 根改名 Alcatel，建 level Brest/Colombes；成本中心剪贴归位（Training/TSS 到 Brest，CC_OXE/MKT 到 Colombes）
4. 正道改归属：OXE 配置把 31000 的 Cost Center ID 从 1 改 3，组织树自动搬家且原位留灰色条目
5. 允许项：中继组 SIP_Public 从 CC_OXE 剪贴到 MKT 成功（不影响话机侧）
6. 拒绝项：分机 31011 从 TSS 剪贴到 MKT 失败（分机只能经 OXE 配置或目录应用改）
7. 复制语义验证：Copy Training 到 Colombes 后原件转 inactive 转灰、粘贴件 active

**历史回溯与全局重建**（p289-295）：

1. 记下 inactive 31000 与 active 31000 各自的创建日期
2. 右键 active 31000（选设备不是选用户）> Assign earlier creation date，填 inactive 条目的创建日期并确认告警
3. 验证：inactive 条目消失，active 条目取回完整历史
4. 全局重建：双击 C:\8770\bin\ToolsOmniVista.exe，输 directory manager 口令，输 y 停 8770 服务（强制）
5. 菜单 3 Accounting Organization Update，确认后等完成（实验 5.172s），非活动实体删除、票据重挂
6. 手工收尾：非活动的成本中心 Training 工具清不掉，右键手工删除

## A2 — 未来触发

使用情境：部门重组后票据归错成本中心；组织树上出现重名灰条目；员工离职复用分机后历史怎么并；搬分机被拒绝；ToolsOmniVista 是什么、敢不敢跑；默认成本中心放什么。

语言信号：组织树 / organization tree / 成本中心 / cost center / cc=255 / 默认成本中心 / 灰色条目 / inactive / 剪贴 / 复制 / cut & paste / copy & paste / 回溯 / Assign earlier creation date / ToolsOmniVista / 组织更新 / Ptp 计数器。

与相邻能力区分：票据进没进库属票据管道能力；树配好后的遮蔽与可见性属机密控制能力；发票价调价属成本档案能力。

## E — 可执行步骤

输入契约：OXE 同步正常、成本中心已在 PCX 命名。变更窗口未约定 → 判停先约停机窗口再跑全局更新。

1. 配默认成本中心并完整同步。完成标准：无成本中心对象落位正确
2. 改根名并搭 level/成本中心骨架（剪贴成本中心归位）。完成标准：树结构过业务确认
3. 搬移按对象二分走对通道：分机走 OXE 配置/目录应用；中继组可组织图剪贴。完成标准：无拒绝报错
4. 人员变动回溯：右键活动"设备"> Assign earlier creation date（日期取自非活动条目）。完成标准：非活动条目消失、历史并入
5. 全局重建：先归档，再跑 ToolsOmniVista 组织更新（停服务确认 y）。完成标准：组织树仅剩活动条目
6. 手工删除残留的非活动成本中心/level（工具不处理）。完成标准：树中无灰色残留

判停点：

- 分机搬移被拒 → 回 OXE 配置或公司目录改，不在组织图反复重试
- 回溯选了"用户"挂不上历史 → 必须选设备（书内全大写 Warning），重新操作
- ToolsOmniVista 删除不可逆 → 执行前先归档，并预期大量灰色条目消失、服务中断
- 回溯日期不满足"早于现值、晚于等于最后非活动条目"→ 工具会拒绝，先核对日期

输出契约：组织树结构图（含成本中心映射）+ 搬移/回溯操作记录 + 全局更新前后条目数对照。

## B — 边界

- cc=255 落组织根；中继组等对象在 OXE 配置里本就不能设成本中心（p256/p285）
- 组织更新强制停 8770 服务且删除全部带历史的非活动实体——是变更窗口里的重活，不是日常维护（p293）
- level/成本中心/人不可回溯；工具更新后残留的要手工删（p263/p295）
- 多节点（网络号×1000000+节点号聚合）与 OpenTouch 级联同步只有概念图无实验，生产多节点组网须另行验证
- 树重建前清空旧条目的做法属实验口径，生产用全局更新替代"删了重来"
