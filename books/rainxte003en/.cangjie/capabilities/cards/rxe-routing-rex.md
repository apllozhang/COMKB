# OXE 用户形态决策与远程延伸路由（RCC/REX/Tandem/Ghost Z/溢出）

## R — 原文依据

> "Rainbow Essential license • Allows only to control your physical device via the Rainbow application (RCC mode) • Call routing is not possible"（p109）
> "A Remote Extension (REX) is a special type of device that allows OXE to reroute calls to an external resource … each REX needs an internal technical equipment called Ghost Z"（p111）
> "Multi-lines are required on extensions part of a tandem."（p124）
> "The DECT device cannot be set up in tandem with a REX (OXE management limitation)"（p139）

出处：RAINXTE003EN p106-130, p139。

## I — 自述

先定形态再动手，四种用户形态（p106-118）：

| 形态 | 订阅前提 | 行为 |
|---|---|---|
| 无 REX（RCC） | Essential 或未配路由 | Rainbow 仅监督话机（接/挂/转），音频全在话机，用 OXE 公网资源 |
| 话机+REX（tandem） | Business/Enterprise | 可改路由到手机/家庭/其他外部号；agent 按路由自动改写 REX |
| 纯 REX（无话机） | Business/Enterprise + 网关 | Rainbow 当软电话，WebRTC 网关必须 |
| 仅 DECT 话机 | Business/Enterprise | DECT 不能直接 tandem，须建 Virtual UA 做 multi-devices |

路由四案例矩阵（p116，选 Office phone 路由时）：

| 案例 | 用户档案手机号 | REX 内容 | 振铃终端 |
|---|---|---|---|
| Case 1 | 无手机号 | 空 | 仅话机 |
| Case 2 | 配专业手机 | 专业手机 | 话机+专业手机同响 |
| Case 3 | 配个人手机 | 个人手机 | 话机+个人手机同响 |
| Case 4 | 两个都配 | 专业手机（专业优先） | 话机+专业手机同响 |

机制要点：

1. **Ghost Z**：REX 专用的 OXE 内部技术资源，每路并发呼叫占一个、通话结束释放；Ghost Z 池大小=REX 并发上限（p111/p122）
2. **Tandem**：主站=Deskphone、副站=REX；两端必须 multi-line（至少 2 线）；配置只做在主站，自动同步副站（p124-125）
3. **路由不是转发**：Call Routing is not a Forwarding——路由改 REX 指向的外部目的地，与 forwarding 是两个机制（p109/p114）
4. **computer 路由特殊**：REX 被 agent 写入 BBB 前缀 17 位 Rainbow number，走 WebRTC 网关；mobile/home/other 走 OXE 公网 trunk（p113/p142）
5. **两级溢出**：主站失效溢副站（系统参数+COS）；主副都无应答溢 associate（留言信箱），计时器 100ms 步进（150 即 15 秒）（p126-127）

## A1 — 书中案例

**远程延伸配置实验**（p119-130，参考 TC2462）：

1. 系统参数勾选 REX 出局实体与 ARS 实体两个 Local Features 参数
2. 建 Ghost Z：目录号用字母开头（如 DB1000）、Set Type Analog、机架/板卡/设备地址 255
3. Ghost Z 的 Facilities 页签勾 Ghost Z 且 Feature 选 Remote extension
4. 声明 REX：目录号按 21 加主号 QMCDU 编号（如 2131000），Set Type 选 Remote extension
5. 给主站 31000 与副站 2131000 各配至少 2 条 multi-line（Prog. Keys 页签）
6. 主站 31000 的 Assoc. Sets 页签声明 tandem：副站号 2131000、勾 Main set in the tandem
7. 溢出第一级：勾 Overflow to sec tandem if main OOS 与配套 COS 两项
8. 溢出第二级：实体 Overflow timer（100ms 步进）、COS 勾无应答溢 associate、主设备关联留言信箱号
9. 给用户分配 Enterprise 订阅（Essential 不能改路由）
10. Nomadic 测试：路由选 Other phone 填外部号后做来去话，再用 remotesets 查 REX 自动号码
11. 档案逐个配专业/家庭/个人手机并切路由，对照四案例矩阵核对 REX 内容与振铃

## A2 — 未来触发

使用情境：给用户选接入形态；振铃终端不对；REX 并发上不去；DECT 用户上 Rainbow；"我在 Rainbow 上接不了电话"。

语言信号：REX / 远程延伸 / Ghost Z / tandem / multi-line / 溢出 / overflow / nomadic / DECT / Virtual UA / 路由 / routing / 转发 / forwarding / remotesets。

与相邻能力区分：

- computer 路由的网关侧落地 → 网关部署与 OXE 侧网关配置两能力
- 只做分机绑定不做路由 → 分机关联能力（路由卡）
- Ghost Z 数量与话务量核算 → 共享池与容量能力

## E — 可执行步骤

输入契约：OXE 版本与用户话机类型（物理话机/DECT/无话机）、订阅档位、用户档案手机号口径。形态未定 → 先用形态矩阵决策再施工。

1. 形态决策：按四形态矩阵对号（订阅、话机、预期行为）。完成标准：形态与订阅方案成文
2. Ghost Z 容量：按并发呼叫数建池，目录号字母开头优化拨号计划。完成标准：池大小与话务匹配
3. 声明 REX：编号 21 加主号 QMCDU，Set Type 选 Remote extension。完成标准：REX 设备在册
4. 配 multi-line：主副站各至少 2 线。完成标准：tandem 成员分机均有 multi-line
5. 声明 tandem：只在主站 Assoc. Sets 做，确认自动同步副站。完成标准：主副站配对生效
6. 配溢出：两级参数与 COS 按清单勾选。完成标准：主站失效/无应答路径实测可达
7. 行为验证：切路由做 Nomadic 来去话，remotesets 核对 REX 自动号码。完成标准：与四案例矩阵一致

判停点：

- 来话振铃终端与预期不符 → 先查用户档案手机号字段与 REX 实际内容（remotesets），不按转发思路排障
- DECT 用户要上路由 → 停，走 Virtual UA 方案并讲清两个代价（重建 DECT、Virtual UA 不可 RCC）
- 4059EE 场景要求关联话机"非 multi-line" → 场景相反，不要把 tandem 经验照搬（n20）
- 用户只有 Essential 却要改路由 → 停，先升订阅（Business/Enterprise），不硬调参数

输出契约：用户形态与订阅方案 + Ghost Z/REX/tandem 配置记录 + 路由行为验证结论。

## B — 边界

- 远程延伸的完整生产依据在 TC2462（p121/p125 各章指向），本卡为培训实验口径的提炼
- Ghost Z 数量规划联动容量工具（TBE067 推算压缩器，p151），书内无直接换算表
- "RCC 呼纯 Rainbow 用户不通"为机制推断（书中以测试问题呈现未给答案，nr-04），现场实测确认
- 实验分机号（31000/2131000）、Ghost 示例号（DB1000）与留言信箱号为实验口径，现场按自己编号计划重排
- OXE 网络的多节点 REX 用途（OT/Remote Agent）书中仅点名，未展开
