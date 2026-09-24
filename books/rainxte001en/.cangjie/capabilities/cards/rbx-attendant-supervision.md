# Rainbow 话务台与监督组（Attendant console、监督组、互助监督组）

## R — 原文依据

> "Call queue management - Manage up to 10 calls for OXE - And up to 8 calls for OXO Connect ... An Attendant subscription is required for each member using this feature • Available on the Rainbow Web and Desktop applications"（p164）
> "Maximum number of supervision groups for a supervisor | Maximum number of users in a group (supervisors + supervised): 5 | 30"（p167）
> "Interception is only possible if supervisors and supervisees are on the same PBX. Only phone calls can be intercepted."（p169）
> "Works only for PBX calls, not for Rainbow softphone calls"（p171）

出处：RAINXTE001EN p162-181。

## I — 自述

**话务台**（Attendant console，Web/Desktop 专属，无移动端）四功能区：

1. 呼叫队列（OXE 10 路 / OXO 8 路）
2. 当前通话控制
3. Busy Lamp Field 监督区
4. 监督组页签区

三种显示密度（Normal/Small/Condensed）。**容量规格**：

| 项目 | OXE | OXO Connect |
|---|---|---|
| 呼叫队列 | 10 路 | 8 路 |
| 保持通话（多线资源） | REX ≤10 | Anydevice ≤8（最低 R6） |
| 监督组/监督员 | ≤5 组 | ≤5 组 |
| 组人数（含监督员） | ≤30 | ≤30 |

**使用前提**：每个使用者持 Attendant 订阅；话务员须有电话线 + VoIP 软话机能力；话机/手机上无任何话务台功能。

**监督组**：监督员（须 Attendant 许可）与被监督成员同组；每监督员 ≤5 组、每组 ≤30 人（含监督员）；可拦截来话、可强制/取消被监督人呼转。

**互助监督组**（Mutual aid group）：创建方法与普通组相同，Type 选 Mutual aid group + Lock the last member（锁定成员不能退组）+ 双方 In/Out 权限；监督员可一键进出、临时纳入/排除成员、收到来话通知后代接；一次最多监督 4 路呼叫；代接仅限同 PBX 的电话呼叫（Rainbow 软话机呼叫不可）。

## A1 — 书中案例

**话务台实验**（p175-179）：

1. Companies → Subscriptions 订购 Attendant Monthly（实验口径禁预付）
2. Members 给监督员分配订阅
3. Communication/Supervision → Create 建组（选监督员 + 勾被监督成员）
4. 以监督员账号登录，从话务台图标进入控制台

**互助组实验**（p180-181）：

1. 同路径 Create，多填 Type=Mutual aid group 与 Lock the last member
2. 监督员用 admin 账号（实验口径）执行监督
3. 被监督成员须有物理分机或 PBX 软话机（IPDSP/MicroSIP）

## A2 — 未来触发

使用情境：给前台/秘书配话务台；建监督组；40 人部门怎么拆组；互助值班方案；能不能代接软话机用户的呼叫；话务员能不能用手机值班；队列容量多少。

语言信号：话务台 / attendant / attendant console / 监督组 / supervision group / 互助组 / mutual aid / 代接 / pickup / interception / 前台 / 秘书 / BLF / 值班。

与相邻能力区分：Attendant 订阅的购买与分配归公司与订阅能力；被监督成员的话机关联见分机关联（路由卡）；OXO 侧 ACD 呼叫中心属第一本书能力域（另一 bundle）。

## E — 可执行步骤

输入契约：PBX 类型（OXE/OXO，决定容量口径）、话务员与被监督名单、 Attendant 订阅数量、成员话机形态清单。名单超 30 人/组 → 先拆组方案。

1. 订购与分配：Subscriptions 订 Attendant（生产可选预付）→ Members → Services 页签分配给话务员。完成标准：话务员持 Attendant
2. 建监督组：Communication → Supervision → Create → 填名称 → 选监督员 → 勾被监督成员。完成标准：组创建成功
3. 互助组（如需）：同路径，Type=Mutual aid group → 定 Lock the last member → 定义双方 In/Out 权限；核被监督成员均有物理分机或 PBX 软话机。完成标准：组建成功
4. 话务员侧验证：登录 Web/Desktop → 打开话务台 → 确认四功能区呈现、组页签可见、被监督人在场状态正确。完成标准：界面就绪
5. 行为验证：向被监督成员发起呼叫 → 监督员收到通知并代接；测试强制呼转/取消呼转。完成标准：代接链路通

判停点：

- 跨 PBX 代接需求 → 平台不支持（拦截限同 PBX），拆方案或改需求
- 代接对象是纯 Rainbow 软话机用户 → 不在代接范围（仅 PBX 电话呼叫），向客户明示边界
- 手机值班需求 → 话务台无移动端，改排班方案而非承诺功能
- 单组需求 >30 人或监督员 >5 组 → 触硬上限，拆组/合并监督职责
- 话务台里保持不了预期路数 → 核多线资源（OXO Anydevice 需 ≥R6 且 ≤8 路；OXE REX ≤10）

输出契约：话务员就绪（订阅+控制台可用）+ 监督组/互助组结构清单 + 代接行为验证记录。

## B — 边界

- 话务台交付的是 Business/Enterprise 级服务，Attendant 订阅是话务员侧解锁键（p164）
- 监督组是 Rainbow 侧概念，与 PBX 侧呼叫分配组（ACD/寻线组）无涉——建组不改变 PBX 话务分配（机制对比为推断，n43）
- 全部呼叫仍由 PBX 处理；话务台是监督/拦截/调度面，不是话务引擎
- 配置细节权威文档：TC2462（OXE）/TC2479（OXO）（p169 指针）
- 实验章节页眉写 "OmniPCX Enterprise" 但内容为 OXO 培训通用（原书如此，c10 已注明）
