# ACR 基础 CCD 矩阵地基（双 Pilot、等待房间、坐席技能档案、混合链路）

## R — 原文依据

> "For the "standard matrix": Create one "normal" Pilot: 3x600 • Create one normal Waiting Queue: 3x999700 … Create one ACR Pilot: 3x603 … Create on Waiting Room: 3x999703"（p22，实验口径）
> "Rule Number It is possible to declare up to 30 rules per pilot … Priority The priority value is from 0 to 9. 0 being the highest priority."（p26）
> "Weight Weight used by the Individual Skill Mapping (ISM) calculation algorithm to classify domains (1 for the least important to 20 for the most important)."（p37）
> "the ACD prefix is mandatory prior to create the CCD matrix objects"（p22）

出处：OTCCXTE150EN p19-41。

## I — 自述

基础矩阵是全书一切实验的公共地基，普通链路与 ACR 链路并行：

1. **ACD 前缀先行**：前缀是建一切 CCD 对象的前提（先查 Translator/Prefix Plan）；前缀加数字是话机上的坐席动作码
2. **普通链路**：Pilot → Waiting Queue → Agent Processing Group（FIFO 队列，CCD 常规分发）
3. **ACR 链路**：ACR Pilot → Waiting Room → 同一坐席处理组（房间不按 FIFO，ASM 列表附着其上）
4. **入口分流**：统计 Pilot 挂呼叫档案后汇入 ACR Pilot（车险/家险两类入口）
5. **规则结构**：每 Pilot 最多 30 条路由规则（编号 0-29）、分发规则最多 10 条；优先级三处同口径 0-9 且 0 最高
6. **技能体系**：域（1-16 字符、ID 0-99、权重 1-20）挂技能（缩写 1-4 字符）；呼叫档案最多 7 技能、级别 1-9、强制/可选、语言偏好 1-7

话机与坐席侧动作码表（ACD 前缀 + 数字）：

| 数字 | 动作 |
|---|---|
| 1 | 不可用 |
| 2 | 整理（Wrap up） |
| 3 | 呼叫主管 |
| 5 | 注销 |
| 6 | 登录 |

关键约束：等待房间与等待队列不能同开；ACD Station 类型（Agent/Supervisor）建户后不可改；坐席须有至少 1 个活动技能才参与分发。

## A1 — 书中案例

**矩阵十九步（c01，关键段）**：

1. 核查 ACD 前缀存在（Translator/Prefix Plan），确认 CCS 安装时勾选 ASM script 组件
2. 建坐席处理组（实验口径 3x999800），建普通队列 3x999700 挂到该组
3. 建普通 Pilot 3x600（路由方向接队列）与 ACR Pilot 3x603（路由方向接等待房间 3x999703）
4. Pilot Rule Guide 建规则，Pilot Rule Direction 配优先级与方向开关
5. Distribution Rule 建分发规则并激活，配资源选择与呼叫选择两级配置
6. 建 ACD 授权话机、Superuser 与坐席话机；建坐席/主管用户（ACD Station 一次定型）
7. 建混合链路：类型 Hybrid、邻接网络号异于本地（0-31）、至少 2 个 access 成对
8. telnet 执行 hybvisu -f all 校验：两个 access 的 Main State 均须为 up
9. 建统计 Pilot（3x650/3x651）并指 Routing Pilot 为 ACR Pilot
10. CCS 侧建技能域与技能、呼叫档案（English+Car / English+Home），坐席配技能级别

## A2 — 未来触发

使用情境：从零搭 OTCC 标准版呼叫中心矩阵；ACR Pilot 挂不上等待房间；坐席登录不了处理组；混合链路起不来；配呼叫档案和技能。

语言信号：ACD 前缀 / 处理组 / Waiting Queue / Waiting Room / ACR Pilot / 统计 Pilot / Pilot Rule Guide / Distribution Rule / 呼叫档案 / Call Profile / 技能域 / Weight / 混合链路 / hybvisu。

与相邻能力区分：矩阵好了写脚本，见 脚本编辑器能力；统计与过滤器，见 过滤器统计卡（路由）；上外部 ASM，见 外部 ASM 部署能力。

## E — 可执行步骤

输入契约：客户编号方案（ACD 前缀与号段）、坐席名单与技能需求、OMF/CCS 管理权限。前缀不存在先解决前缀，其余全部卡住。

1. 核 ACD 前缀与 CCS 的 ASM script 组件。完成标准：前缀动作码可用、脚本编辑器可见
2. 建坐席处理组 → 普通队列 → 普通 Pilot（链路一）。完成标准：普通呼叫可排队进组
3. 建等待房间 → ACR Pilot（链路二，房间与队列不同开）。完成标准：ACR Pilot 路由方向指向房间
4. 建路由规则（0-29）与分发规则（10 条内），配两级优先级（0 最高）。完成标准：生效规则可切换
5. 建 ACD 话机、坐席/主管用户、附件名单与坐席操作数据。完成标准：坐席可登录处理组
6. 建混合链路并 hybvisu -f all 校验。完成标准：两 access 均 up
7. 建统计 Pilot 汇入 ACR Pilot。完成标准：统计 Pilot 可配置呼叫档案
8. CCS 侧建域/技能/呼叫档案，坐席配技能级别。完成标准：档案与坐席技能可互相匹配

判停点：

- 建 CCD 对象报前缀缺失 → 停，先规划前缀（顺序约束非故障）
- 坐席建成 Supervisor → 停，类型不可改，删号重建；批量开户前先核名单
- 房间与队列想同开 → 停，结构性互斥，二选一
- 链路 access 起不来 → 核对邻接网络号异于本地、Multi access=YES、成对配置

输出契约：可跑普通 CCD 的矩阵 + ACR 对象就位的双链路 + 技能档案体系。

## B — 边界

- 矩阵编号（3xXXX）全部为实验口径，生产按客户编号方案整体替换；p22 "3X800" 为笔误（nr-02）
- 多节点组网下 ACR 的细节在书外；混合链路仅覆盖本地 CCD 呼叫前提（f09 条件）
- ACD 前缀规划依赖客户编号方案，原书不给规划方法
- 技能域也可由 mgr 或 OmniVista 8770 管理、坐席技能可用 Skill Matrix 批量配（多入口并存，原书未讲冲突处理，推断以单一入口为准）
- CCS 安装未勾 ASM 组件时矩阵能建而脚本不可用（n01）
