# 话务台与监督组（Attendant Console、Supervision Group、Attendant Group）

## R — 原文依据

> "A supervisor must have one of the following levels of service: • Voice Attendant: Supervision-Pickup-Transfer & 10 Calls in queue • Voice Business & Enterprise: supervision-pickup-transfer."（p224）
> "Warning: Members with voice attendant subscriptions cannot use: • Attendant mode on the Rainbow mobile application • Their telephone set."（p246）
> "Members in this group Must Have a Voice Attendant subscription."（p249）

出处：RAINXTE101EN p223-225, p245-249, p284-289。

## I — 自述

话务台是 PC 端人工接听/监督工作台（Rainbow 应用内），靠 Voice Attendant 订阅解锁；监督组是它的组织单元。

监督员订阅分级（p224）：

| 订阅档 | 监督能力 |
|---|---|
| Voice Attendant | 监督-代接-转移 + 10 路排队（完整话务台） |
| Voice Business / Enterprise | 仅监督-代接-转移（无话务台排队） |

硬规格与能力清单（p224, p246）：

1. 每用户最多 5 个监督页签；每组（监督员+被监督者合计）上限 30 人；一人最多当 5 个组的监督员
2. 话务台能力：监控被监督成员（在场+话务活动）、代接/转移、最多 10 路保持、修改被监督成员的例行程序
3. 三档显示：Normal / small / condensed
4. 相关联的 attendant group = Subtype 为 Attendant 的 hunt group（多址共享前台、Parallel 分发、可加预通告），组内每个接听成员都必须持 Voice Attendant 订阅

Voice Attendant 的设备代价（p67, p246，两层口径见 needs-review nr-07）：

1. 订阅层：不支持硬话机——设备定位 PC only
2. 行为层：不能用手机端话务台模式；已配置的话机关联会在话务台激活后被删除

## A1 — 书中案例

**订阅、建监督组、开话务台、建 attendant group**（p284-289，How-To）：

1. Subscriptions 区 / Add a new subscription → 选 VOICE ATTENDANT → Monthly（实验口径）。
2. 定许可数 → Subscribe。
3. Members 区编辑用户 elliotX → Services 页签 → 选 Voice Attendant Monthly。
4. Communication 区 / Supervision 页签 / Create → 监督员选 Elliot。
5. 勾被监督成员 Carol、Bob → Create。
6. 以 Elliot 登录 web 或客户端 → 点话务台图标进入 Attendant console。
7. Groups 页签建 attendant group：Type=Hunt Group、Subtype=Attendant → 成员选持 Voice Attendant 的用户。

验收口径：控制台可打开并显示监督成员状态；attendant group 建成后成员均为 Voice Attendant。

## A2 — 未来触发

使用情境：前台/秘书要一张能看人、能代接、能转接的工作台；主管要监督团队话务；多址共享前台；话务员能不能用话机/手机；话务台方案报价。

语言信号：话务台 / attendant console / 监督组 / supervision group / 监督员 / supervisor / 代接 / pickup / 转移 / transfer / Voice Attendant / attendant group / 预通告 / 排队 / 10 路 / supervision。

与相邻能力区分：纯自助分流（不要人工坐席）走欢迎服务 IVR 能力（IVR 无许可限制，与话务台形成成本对照，n57）；组参数与队列机制归呼叫组能力；订阅开通归公司订阅能力。

## E — 可执行步骤

输入契约：岗位设计（话务员/主管/前台）、成员名单与现有订阅、终端现状（有没有人在用话机）、话务量（决定要不要 10 路排队）。

1. 核订阅：监督员与 attendant group 成员须 Voice Attendant；只做监督-代接-转移可用 Business/Enterprise。完成标准：订阅差距清单成文
2. 告知设备代价：Voice Attendant 用户锁定 PC——无手机端话务台、话机关联会被删。完成标准：客户书面确认岗位形态
3. 建监督组：Communication / Supervision / Create → 选监督员与被监督成员（组 ≤30 人）。完成标准：组建成功
4. 开话务台：以监督员登录 web 或客户端 → 话务台图标 → 验证监督页签/BLF 区/呼叫队列。完成标准：状态显示与代接转接抽测通过
5. 建 attendant group（如需共享前台）：Type=Hunt Group、Subtype=Attendant → 配内线与 DDI → 成员全持 Voice Attendant。完成标准：来话按 Parallel 分发到组

判停点：

- 话务员要求"手机值班"或"保留话机" → 停，Voice Attendant 硬约束（p246，n43）：二者不可兼得，改排班方案或换订阅档
- 给已配话机的用户激活话务台 → 停，先告知话机关联会被删（存量破坏性变更），再操作
- 40 人要一个监督组 → 停，每组上限 30 人（监督员+被监督者合计），拆组
- 客户预算想用"免费无限话务台" → 停，那是 IVR 的属性；话务台必须 Voice Attendant 订阅（n57）

输出契约：监督组与话务台就位（订阅/组/控制台验证记录）+ attendant group 配置与岗位说明。

## B — 边界

- 话务台仅在 PC Rainbow 应用（p67 设备=PC only）；Web/桌面客户端形态，无移动端
- 监督员改被监督成员例行程序是话务台能力之一（p246）——涉及他人话务行为，操作权限要在客户侧约定
- 规格数字（5 页签/30 人/5 组/10 路排队）为 Sprint 170 口径，版本演进以 Features List 为准（p8 自注示例非全量）
- 实验按 Monthly 开 Voice Attendant（p285 实验口径）；生产按月付/预付商务选择（needs-review nr-06）
- 话务台三档显示与具体按钮布局随客户端版本漂移，以实际界面为准
