# ACD 等待队列管理（OXO Connect）

## R — 原文依据

> "Let N be the number of agent in service and K the load factor • If N * K is not an integer, the value of the queue is the next higher integer • The maximum size of the queue is 16"（p93）
> "Estimated waiting time = [(Number of call in the queue / number of agents on duty) + 1] X Average duration of ACD conversations"（p94）
> "Queue exit by ''*'' key ... Activate the ''Place in group voice mailbox'' option ... Then activate the ''Transfer to a number'' option"（p38, p112）

出处：OXOCXTE107EN p93-94（公式）、p38（队列流程）、p112-113（出口实验）、p184（容量实测）。

## I — 自述

队列有两个可配面：容量和体验。容量由公式定——队列长度 = 值机（On duty）坐席数 N × 话务因子 K，非整数向上取整，硬上限 16（与标准 ACD 端口上限同源）。关键在 N 的口径：只数 On duty 状态的坐席，off duty/登出的不计入，所以**坐席签出会实时缩小队列容量**。K 是话务/占用因子（0.1-9.9），取小则早劝漏、取大则多容客。体验由两类消息定：达到阈值时插播"预计等待时间"或"队列最低排名"（二选一配置），预计等待时间 = (队列呼叫数/在值坐席 + 1) × 平均通话时长（Average duration 参数），是线性估算——高峰会低估。出口设计：来电者可随时按 `*` 自救退出（转组邮箱或预定义号码）；队满后来电走劝漏三出口（转号码/组邮箱/劝漏语音后释放），在 Call management 里逐一启用验证。

## A1 — 书中案例

**容量实测**（p93, p184，厂商实验）：
- 讲义示例：4 名 on duty 坐席 × K=0.5 → 队列最多 2 通。
- 实验交叉验证：组1（坐席 101/102 两人在值）把 K 从 0.1 改 2.0 → Agent 应用上观察到队列容量从 1 变 4。核算：2×2.0=4，吻合（注意 N 只数 On duty）。
- 出口实验（p112-113）：坐席全忙呼入组1 → 消息 1 后循环消息 2；坐席释放后队首呼叫转出；按 `*` 退出；依次启用邮箱/转接出口验证。组2 K=0.1 时连打两通 → 第二通直接劝漏。

## A2 — 未来触发

使用情境：
1. "队列设多大合适？"——N×K 公式与 K 取值建议。
2. "客户反映排一下就被挂断"——K 过小或出口配置问题。
3. "想让客人听到还要等多久"——Queue time 选项与 Average duration 参数。
4. "坐席下班后队列是不是变小了"——N 只数 On duty 的口径。
5. "排队的人能不能自己留言走人"——`*` 键退出与 Call management 出口。

语言信号：队列 / 排队长度 / queue length / waiting queue / 等待时间播报 / traffic factor / 话务因子 / 星号退出 / 队满 / 劝漏出口。

与相邻能力区分：来话行为整体走向与场景判定 → 六场景能力；端口全忙劝漏属于场景问题；本能力聚焦"队列容量数值 + 消息阈值 + 出口配置"三件事。

## E — 可执行步骤

输入契约：在值坐席数 N（实时口径）、期望容客量或话务判断（定 K）、平均通话时长（历史值）、客户对等待播报的偏好（报时间/报排名/都不报）。缺平均通话时长时先询问或用近期统计（Statistics 应用可取）。

1. 计算队列长度：queue = ceil(N × K)，K∈[0.1, 9.9]，上限 16。示例核算：N=2、K=2.0 → 4；N=4、K=0.5 → 2。完成标准：得到整数队列值且 ≤16。
2. 配置容量：OMC / Automatic Call Distribution / ACD-SCR Services / General parameters / "Group 1-4" tab → 选中组 → Queue management → 填 K（Queue length 选项）。完成标准：保存成功。
3. 验证容量：坐席全忙后连续呼入，数实际入队通数是否等于计算值（可用 Agent 应用观察队列，参照 p184 方法）。完成标准：实测 = 计算值。
4. 配置等待播报：General parameters 中选 "Queue rank"（播排名）或 "Queue time"（播预计等待），设对应触发阈值；Queue time 依赖 Average duration 参数填平均通话时长（秒）。完成标准：实呼时在阈值后听到对应播报。
5. 配置退出与出口：Call distribution 图标旁的 Call management 中，按需启用 "Place in group voice mailbox"（按 `*` 或队满转入邮箱）与 "Transfer to a number"（按 `*` 或队满转号码）；两者都不启用 = 队满播劝漏语音后释放。完成标准：三种出口实测符合需求。
6. 回归：恢复原 K 值前与客户确认新值观察期。

判停点：客户需求是"永不劝漏"→ 说明上限 16 与端口上限的硬约束，超出即需扩坐席或分流（原书无其他手段），不得承诺。

输出契约：K 取值与队列长度计算书（含 N 口径说明）+ 消息/出口配置清单 + 实测记录。

## B — 边界

- 线性等待公式在高峰/非平稳到达时会**低估**等待（阶段 0 批判结论），向客户承诺播报时间要留余量。
- N 随坐席状态实时变化：签出一个坐席，队列容量立即缩 1×K——与签入签出能力联动排障。
- 上限 16 不可突破；话务量需要更大队列时属方案级问题（换平台/扩容），不是配置能解决的。
- 组间溢出（队列 10 秒后溢到别组坐席，p96）机制存在但**配置入口原书未写明**（needs-review nr-01），不要凭本能力承诺溢出配置。
- 队列消息的语音文件本体（102.wav 等）录制上传见语音定制能力。
