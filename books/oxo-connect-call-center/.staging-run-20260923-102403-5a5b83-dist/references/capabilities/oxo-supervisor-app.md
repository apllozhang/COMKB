# Supervisor 班长台部署与实时监控（OXO Connect）

## R — 原文依据

> "ACD statistic and Supervisor applications use a dedicated ACD admin password instead of installer password • In order to not communicate to the end customer the installer password"（p150）
> "On Duty - Awaiting call: ... - Not answering: ... - Being routed: ... - Ringing: ... - ACD busy: ... - On hold: ... - Busy, outgoing call: ... - Not available: ..."（p164）
> "The Supervisor application can change the group(s) the agent belongs, the agent rank and the agent status."（p165）

出处：OXOCXTE107EN p147-165。

## I — 自述

班长台（Supervisor application）实时呈现呼叫中心活动并直接干预：看坐席（分机/姓名/组/活动率/状态）与组（状态/活动率），并可改坐席的组、rank、状态，改组的 open/closed/按时段。部署三步前置：先用 OMC 设 **ACD Admin 专用密码**（OMC/System Miscellaneous/Passwords——独立于 installer 密码，避免把安装密码泄露给客户）；再设活动率计算周期（过去 1 小时或半小时）与过载告警闪烁时延；然后装应用（MyPortal 下载）首连（服务器 IP + 语言 + ACD Admin 密码）。看板解读核心是 On Duty 八子态：Awaiting call 待接 / Not answering 已响未接 / Being routed 转接预留中 / Ringing 振铃 / ACD busy 通话中 / On hold 刚挂机休整 / Busy outgoing 外呼中 / Not available 处理非 ACD 来话——"坐席显示忙却不接 ACD"对照子状态即可定位。

## A1 — 书中案例

**部署与验证实验**（p160-165，厂商实验）：OMC 把活动率周期设为 "1/2 hour" → 装应用（ACD_X.X\Alcatel\Call Center\Supervisor）→ 首连填 192.168.1.246、English、Acdc1064（实验值）→ Parameters 里按组选受监控坐席 → 切坐席状态验证实时刷新；打入约 5 分钟 ACD 通话观察 activity rate 递增；Group 菜单测试改组状态。

## A2 — 未来触发

使用情境：班长要实时盯队列与坐席；"这个坐席显示忙怎么不接电话"；调整坐席组/rank；临时开关组。
语言信号：班长台 / 监控 / supervisor / 实时状态 / activity rate / 活动率 / 坐席状态不对 / 组开关。

与相邻能力区分：坐席自己签入签出 → 签入签出能力；本能力是班长视角的监控与干预。

## E — 可执行步骤

输入契约：ACD Admin 密码（OMC 侧先建）、受监控坐席与组清单。缺密码先在 OMC 侧创建。

1. 设密码：OMC → System Miscellaneous → Passwords → Management password 建 ACD Admin 级密码。完成标准：密码与 installer 不同且已交付班长。
2. 设参数：OMC / ACD-SCR Services / General Parameters / General tab → 活动率周期（1 hour / 1/2 hour）+ 过载告警闪烁时延。完成标准：参数保存。
3. 安装：MyPortal 下载解压（ACD_X.X\Alcatel\Call Center\Supervisor）→ setup.exe。完成标准：桌面图标出现。
4. 首连：双击图标 → 服务器 IP + 语言 + ACD Admin 密码。完成标准：看板加载。
5. 选监控对象：Parameters → 按组勾选坐席。完成标准：坐席出现在实时列表。
6. 验证：切坐席状态看实时刷新；5 分钟来话看活动率上升；Group 菜单改组状态（open/closed/时段）。完成标准：三项均生效。
7. 日常判读：坐席"忙而不接"对照八子态（On hold/Busy outgoing/Not available 属正常态，非故障）。完成标准：给出判读。

输出契约：可用班长台 + 受监控对象清单 + 状态判读结论。

## B — 边界

- ACD Admin 密码是 Supervisor 与 Statistics 共用的管理级密码，绝不使用 installer 密码（原书红线）。
- 工具栏/监控图标语义两页（p158-159）为纯图，本卡未覆盖全部图标含义。
- Supervisor 不能代行坐席登录（free seating 是坐席侧操作），只能改坐席的组/rank/状态。
- 八子态是 OXO 口径，与其他平台状态名不通用。
