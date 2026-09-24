# ACD 等待队列管理（OXO Connect）

## R — 原文依据

> "Let N be the number of agent in service and K the load factor • If N * K is not an integer, the value of the queue is the next higher integer • The maximum size of the queue is 16"（p93）
> "Estimated waiting time = [(Number of call in the queue / number of agents on duty) + 1] X Average duration of ACD conversations"（p94）
> "Queue exit by ''*'' key ... Activate the ''Place in group voice mailbox'' option ... Then activate the ''Transfer to a number'' option"（p38, p112）

出处：OXOCXTE107EN p93-94（公式）、p38（队列流程）、p112-113（出口实验）、p184（容量实测）。

## I — 自述

队列管两件事：**容量**和**体验**。

1. **容量公式**：
   - 队列长度 = ceil(在值坐席数 N × 话务因子 K)
   - K ∈ 0.1-9.9；上限 16（与标准 ACD 端口上限同源）
   - **N 只数 On duty 坐席**——坐席签出，队列实时缩容
2. **体验（消息与出口）**：
   - 阈值消息二选一：Queue rank（播排名）/ Queue time（播预计等待时间）
   - 预计等待 = (队列呼叫数 / 在值坐席 + 1) × 平均通话时长（线性估算，高峰低估）
   - 来电者可随时按 `*` 退出：转组邮箱或预定义号码
   - 队满出口三选：转号码 / 组邮箱 / 劝漏语音后释放

## A1 — 书中案例

**容量实测**（p93 讲义 + p184 实验）

- 讲义示例：4 名 on duty 坐席 × K=0.5 → 队列 2 通
- 实验交叉验证：组1（坐席 101/102 两人在值，N=2）把 K 从 0.1 改 2.0 → Agent 应用观察到队列容量 1 → 4；核算 2×2.0=4 吻合
- 出口实验（p112-113）：坐席全忙呼入 → 欢迎语 1 + 循环消息 2；坐席释放即转出；`*` 退出逐项验证；组2 K=0.1 连打两通 → 第二通直接劝漏

## A2 — 未来触发

使用情境：

1. "队列设多大合适？"——N×K 公式与 K 取值
2. "客户反映排一下就被挂断"——K 过小或出口问题
3. "想让客人听到预计等待时间"——Queue time 选项与 Average duration 参数
4. "坐席下班后队列是不是变小了"——N 的实时口径
5. "排队的人能不能自己留言走人"——`*` 退出与出口配置

语言信号：队列 / 排队长度 / queue length / waiting queue / 等待时间播报 / traffic factor / 话务因子 / 星号退出 / 队满 / 劝漏出口。

与相邻能力区分：端口全忙劝漏与场景判定 → 六场景能力；坐席搜索顺序 → 搜索模式能力；本能力聚焦"容量数值 + 消息阈值 + 出口配置"。

## E — 可执行步骤

输入契约：在值坐席数 N（实时口径）、期望容客量或话务判断（定 K）、平均通话时长、播报偏好（时间/排名/不播）。缺平均通话时长先询问或从统计应用取。

1. **计算**：queue = ceil(N × K)，核算 ≤16。完成标准：得到整数值
2. **配置容量**：General parameters / "Group 1-4" tab → 选中组 → Queue management → 填 K。完成标准：保存生效
3. **验证容量**：坐席全忙后连续呼入，实测入队通数 = 计算值（可借 Agent 应用观察）。完成标准：实测吻合
4. **配置播报**：选 Queue rank 或 Queue time → 设触发阈值；Queue time 需填 Average duration（秒）。完成标准：实呼在阈值后听到播报
5. **配置出口**：Call management 中按需启用 "Place in group voice mailbox" 与 "Transfer to a number"；都不启用 = 队满播语音后释放。完成标准：三种出口实测一致
6. 回归：K 值变更与客户确认观察期

判停点：客户要"永不劝漏"→ 说明上限 16 的硬约束，超出即扩坐席或分流，不得承诺。

输出契约：K 取值与队列长度计算书（含 N 口径）+ 消息/出口配置清单 + 实测记录。

## B — 边界

- 线性等待公式高峰**低估**（阶段 0 批判），对外播报留余量
- N 随坐席状态实时变化——与签入签出能力联动排障
- 上限 16 不可突破；更大需求属方案级问题
- 组间溢出（10 秒溢到别组坐席）机制存在但**配置入口原书未写明**（nr-01），不凭本能力承诺
- 消息音频本体（102.wav 等）制作上传见语音定制能力
