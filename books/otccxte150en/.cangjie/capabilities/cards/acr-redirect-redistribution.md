# ACR 重定向与再分发兜底（Redirection、Redistribution、Blockage 落点）

## R — 原文依据

> "Redirection address can be: A static phone number Internal forward (on-pcx) • External forward Through a speed dialing number • Through a network N° • A dynamic phone number Stored in a STRING variable Retrieved from a database…"（p85）
> "If "AGENT_LIST" is NULL or if the list is not empty, but all agents are logged off or unavailable, then the REDISTRIBUTION Rule will be applied"（p90）
> "Routing Direction available and open? If not, the call goes to Blockage mode"（p89）
> "the alb process makes 20 requests (script is executed 20 times) and in case of empty agent list, the call follows the routing management"（p50）

出处：OTCCXTE150EN p82-102, p50。

## I — 自述

空坐席列表的两条兜底路径，都是单用规则、各须独占一个 APPLY：

1. **Redirection（重定向）**：把呼叫转到一个号码。地址三形态——静态内部分机（on-pcx）；静态外部号（经缩位拨号或网络号出）；动态号（STRING 变量承载，可取自数据库）
2. **Redistribution（再分发）**：把呼叫退回 CCD 矩阵的下一路由方向。触发两种——列表为空；列表非空但坐席全部注销或不可用
3. **Blockage（封锁）**：再分发无可用方向、或脚本重试耗尽后的最终落点——封锁地址或语音引导

兜底链全景：

| 阶段 | 行为 |
|---|---|
| 坐席列表为空 | 脚本按重选机制反复执行（原书两处口径 20/21 次） |
| 重试耗尽 | 呼叫转路由管理（互助方向等） |
| 全无可用方向 | 落 ACR Pilot 封锁模式 |

配套矩阵扩展：建"重定向队列"接 Voice Guide 类型处理组，ACR Pilot 以第二优先级接该队列——再分发落点变成"播忙音提示后请回拨"，比悬死到 Blockage 体验好。

设计要诀：Redirection 适合"转人工/转外线"类明确落点；Redistribution 适合"退回矩阵让次优先方向接管"；两者都要求提前配好落点。

## A1 — 书中案例

**Redirect 脚本（c04）**：

1. 编辑器建脚本：语言条件 Statement 加 RULE_AUTHORIZED 加 RULE_ISM 加重选超时 10 秒
2. 再加 RULE_REDIRECTION 构件（地址实验口径 3x010），连线完成（删连线选红方块右键）
3. 呼统计 Pilot：Debugger 显示 ISM 生效，坐席全忙时呼叫在等待房间停 10 秒
4. 重选后 SEQUENCE 大于 1，Rule Redirection 生效，呼叫转 3x010

**Redistri 脚本（c04）**：

1. 矩阵扩展：建重定向队列 31999702 接 Voice Guide 处理组 31999802（引导 710）
2. ACR Pilot 以第二优先级接该重定向队列
3. 写 Redistribution 构件：周日（calling day=Sunday）呼叫再分发到重定向队列
4. Debugger 里把 IF 条件改为当前日实时验证再分发路径（只能改既有构件）

## A2 — 未来触发

使用情境：坐席全忙呼叫悬死进封锁；要配"忙时转总机/转外线"；周日夜间兜底到语音引导；客户投诉听忙音。

语言信号：Redirection / 重定向 / 转接号码 / Redistribution / 再分发 / 下一路由方向 / Blockage / 封锁 / Voice Guide 队列 / 兜底 / 空列表。

与相邻能力区分：写规则本身的语法，见 脚本编辑器能力；多规则组合语义，见 综合规则组合能力；名单排除坐席，见 名单规则卡（路由）。

## E — 可执行步骤

输入契约：兜底业务口径（转哪里/播什么）、矩阵上已有重定向队列与语音引导（可选）、脚本编辑权限。

1. 定兜底策略：明确落点号码或退回方向；确认该方向在路由规则里已配且可开。完成标准：落点与优先级约定成文
2. （选重定向）写 RULE_REDIRECTION 构件，地址三形态选一。完成标准：脚本保存传输并激活
3. （选再分发）配好第二优先方向（如 Voice Guide 队列），写 RULE_REDISTRIBUTION 构件。完成标准：方向开关状态正确
4. Debugger 验证：制造坐席全忙（签出/置忙），观察重试、转接或退回路径。完成标准：呼叫落到预定落点而非封锁
5. 核对 Blockage 落点：即使兜底齐备也要配封锁地址，作为最后防线。完成标准：封锁模式有内容可播

判停点：

- 坐席只是忙而未签出，Redistribution 不触发 → 停，触发条件是"空或全部注销/不可用"，改用 Redirection 或调超时
- 重定向队列没接 Voice Guide 处理组 → 停，先补矩阵扩展，否则退回方向无意义
- 想在 Debugger 里加新构件 → 停，回编辑器改脚本重传重激活

输出契约：带兜底的脚本 + 矩阵第二优先方向 + Blockage 落点配置 + 验证轨迹。

## B — 边界

- Redirection 与 Redistribution 均为单用规则，必须独占 APPLY（组合语义见综合规则组合能力）
- 空列表重试次数原书两处口径 20/21 次（nr-01），计次规则原书未展开
- 语音引导的录制内容与分配（710-719、*88/*66）是环境操作，书内只给入口
- 无可用方向时落 Blockage——封锁地址也没配好则客户听忙音类体验（n11），兜底设计必须含最后防线
- 转发地址若来自数据库，依赖外部库链路（见外部数据库查询路由能力），纯内部 ASM 做不到
