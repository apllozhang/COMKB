# 两套话务台（4059EE 与 Rainbow Attendant Console）与监督组/互助组

## R — 原文依据

> "Warning - Rainbow and phone status are two distinct things and can be different"（p204）
> "WARNING: This extension must not be multi-line, as it will be associated to the 4059 IP attendant (multiline set is incompatible with 4059 IP attendant)"（p209）
> "Call queue management - Manage up to 10 calls for OXE - And up to 8 calls for OXO Connect"（p227）
> "Maximum number of supervision groups for a supervisor / Maximum number of users in a group (supervisors + supervised): 5 / 30"（p230）

出处：RAINXTE003EN p198-244。

## I — 自述

两套话务台先分清（p200/p227）：

| 维度 | 4059EE（OXE 传统） | Rainbow Attendant Console（云） |
|---|---|---|
| 订阅 | 不需要 Attendant 订阅（只用普通 Rainbow 账户取在场） | 每人必须 Attendant 订阅 |
| 话音 | 只管话务不管话音，必须关联物理话机或 IPDSP | 呼叫全部由 PBX 处理，话务员须有电话线与软终端 |
| 队列 | 话务组溢出门限（Max. No. of Calls Bef. Overfl.） | OXE 10 路 / OXO 8 路 |
| 终端 | PC 应用 + 关联话机（禁 multi-line） | 仅 Web/Desktop，无移动端 |

4059EE 交付四层结构（p198-215）：

- 话务组（Attendant group）：建组即自动生成 CDT，溢出门限按 Day/Night/Mode1/Mode2 状态
- 话务台（4059 IP 类型）：关联话机绝对禁 multi-line——与 tandem 场景要求正好相反（n20）
- 呼叫分配：实体 CDT 日间路由指向话务组、Attendant Call 前缀按国家默认、个人话务呼叫前缀配电话簿显示话务员名
- Rainbow 集成：专用账户、被监督成员须在其联系人列表、Enable Busy Lamp Field 后有 BLF

Rainbow 话务台与监督（p225-237）：界面五区（监督组页签/BLF 区/呼叫队列/呼叫控制/三种显示格式）；监督组规格——监督员最多 5 组、每组（监督员+被监督）最多 30 人；挂起呼叫数取决于软电话线 multi-line 资源（OXE 用 REX 最多 10、OXO 用 Anydevice 最低 R6 最多 8）。

互助监督组（p233-236）：一键 Join/Leave；监督员可临时纳入/排除被监督用户；同时最多监督 4 路；可锁定最后一名成员；代接仅对同 PBX 的电话呼叫有效——Rainbow 软终端（computer 路由）来的呼叫不可代接（n23）。

两条认知纠偏：Rainbow 在场与电话状态是两个独立信息，BLF 上两边可不同（p204/p221，书中专门设计双测试）；4059EE 的 Attendant group 与 Rainbow 监督组是两回事，别混。

## A1 — 书中案例

**4059EE 交付实验**（p206-224）：

1. 建话务组：物理号 A0000、组名 GROP1、溢出门限 5（实验口径取值）
2. 建话务台：Set Type 选 4059 IP、关联话机 31002，Warning 该分机禁 multi-line
3. 建个人话务呼叫前缀 31401 并配电话簿条目显示话务员名
4. 系统参数两项：Close auto sign off 与 PC unregistered at logoff 按 navCtrl 语义勾选
5. 先启动关联的 IPDSP 使其 in service，再从 4059EE 连接（顺序硬约束）
6. 装应用：Custom 勾 Rainbow agent、不装 ALCATEL USB 键盘（RLAB 口径）、防火墙放行应用与 abcacom.exe
7. 配 PCX 连接：设备地址格式为话务员号加主机名（冗余时最多 3 个主机名）
8. 签入后配实体 CDT 日间路由指向话务组
9. 建话务员 Rainbow 成员并配 4059 Rainbow 集成（输账户、勾 Search in Rainbow）
10. 给该账户邀请全员联系人（被监督成员必须在列表内）
11. 启用 BLF 并添加监督项；做两条状态差异测试（Rainbow 状态与话机状态两边不同）

**Rainbow 话务台实验**（p238-244）：

1. 订购 Attendant Monthly（培训禁预付，实验口径）并分配给话务员
2. 建监督组：选监督员与被监督成员后创建
3. 话务员登录打开 Attendant console 核验页签/BLF/队列
4. 建互助监督组：Type 选 Mutual aid group、按需锁定最后一名成员、定义双方 In/Out 权限

## A2 — 未来触发

使用情境：前台工作台选型；建监督组代接电话；互助值班；话务台显示"忙"但用户没打电话；4059 注册不上。

语言信号：4059EE / 话务台 / attendant / 话务组 / CDT / BLF / Busy Lamp / 监督组 / supervision / 互助组 / mutual aid / 代接 / pickup / 在场 / presence / Attendant 订阅。

与相邻能力区分：

- 话务员订阅怎么买 → 公司体系与订阅能力
- tandem 成员的 multi-line（要求相反）→ 远程延伸路由能力
- Rainbow 在场数据源问题 → 维护支持能力（路由卡）

## E — 可执行步骤

输入契约：话务场景（OXE 传统线或云线）、话务员与被监督名单、话机/软终端资源、订阅预算。两套话务台未定 → 先按对比表选型。

1. 选型：按"两套话务台对比表"定线。完成标准：选型与订阅方案成文
2. 4059 线施工：话务组、话务台（关联话机禁 multi-line）、CDT、安装连接、Rainbow 集成与 BLF。完成标准：注册在册且 BLF 显示
3. Rainbow 线施工：订购并分配 Attendant 订阅、建监督组/互助组、打开控制台核验。完成标准：页签/队列/BLF 正常
4. 在场双测试：分别改 Rainbow 状态与话机状态各验一次。完成标准：两列信息独立呈现（可不同属预期）
5. 代接边界确认：核同 PBX 与电话呼叫两个条件。完成标准：需求边界与客户对齐

判停点：

- 4059 注册失败 → 查关联话机是否 multi-line、IPDSP 是否先 in service、防火墙是否放行 abcacom.exe（n22）
- "帮我接一下"跨 PBX 或软终端呼叫 → 停，代接边界不覆盖，提前向客户泼冷水（n23）
- 一个组要装 40 人 → 停，每组上限 30 人，拆组
- 把 Attendant 订阅安到 4059EE 头上 → 停，订阅与 4059EE 无关（n24），退订阅

输出契约：话务台交付记录（选型依据）+ 监督/互助组清单 + 在场差异测试结论。

## B — 边界

- 4059EE 系统参数语义（自动签退/登出抹除 PC 身份）为讲义口径（p210-211）
- 书内 user2 姓名跨章不一致（p64 Rains Robby vs p216 Betty Carol，nr-01）：实验复现勿把姓名当考核点
- 实验取值（A0000/B0000/31002/31401/门限 5）为实验口径，现场按站点规划
- 深入配置在 TC2462（OXE）/TC2479（OXO）（p232 指针）；4059 与 Rainbow 话务台的功能全集以应用版本为准
- 互助组代接依赖被监督成员有物理分机或已关联的 PBX 软终端（p244）
