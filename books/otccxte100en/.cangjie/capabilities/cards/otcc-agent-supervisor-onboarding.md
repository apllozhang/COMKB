# ACD 话机、座席与班长创建登录（固定/移动/自指派）

## R — 原文依据

> "Directory Number Enter the directory number (i.e. 31000) … ACD station Select the ACD function of the set (i.e. ACD authorised phone set)"（p124-125）
> "Self-assigning means that the agent can log himself in any desired processing group."（p137）
> "prefix ACD then 1 = unavailable • prefix ACD then 2 = Wrap up • prefix ACD then 3 = call supervisor • Prefix ACD then 5 = Logoff • Prefix ACD then 6 = Logon"（p66）
> "It is not possible to declare a preferential group for the supervisor because it is automatically self-assigning."（p142）
> "Fixed agent means that the agent can only log on to the set with which he is associated by management. … Mobile agent means that the agent can log on from any authorized set."（p271）

出处：OTCCXTE100EN p31-37, p121-149, p265-274。

## I — 自述

最小人员闭环 = ACD 话机（物理登录点）+ 座席（接呼叫的人）+ 班长（管呼叫的人），三者在 OXE 侧建、在 CCS 侧配属性与挂组。

三种座席形态（p271-273）：

- 固定座席：绑定指定话机，登录免认证
- 移动座席：任意授权话机登录，必须认证
- 自指派座席：登录时自选处理组；非自指派必须设唯一优选组（Preferred Processing Group）

班长恒为自指派、无优选组——给班长配优选组是无效操作（p142/n23）。

ACD 前缀动作表（前缀 12，实验口径，须 COS 启用）：

- +1 退出（可扩展类型：+1+类型号）/+2 wrap-up/+3 呼班长/+5 登出/+6 登入/+91 查私人分机/+92 登出录欢迎指南（p66/p457/p568）

话机兼容（p33）：座席支持模拟话机、ALE-300/400/500/20/20H/30H、AGAP DECT 8232/8242/8262、IP Desktop Softphone；班长支持范围比座席少三类：模拟话机、DECT、ALE 20H。Rainbow 形态仅座席（无班长），三不限制：不入 multiset、不关联 Rainbow 用户、DECT 不支持（p34-35/p19/n39）。

## A1 — 书中案例

**座席班长创建实验**（p121-149）：

1. OXE Users>Create 建 3 台 ACD 话机：31000/PRO1、31001/PRO2、31002/PRO3（ACD authorised phone set）
2. IP 软话机仿真：话机 TSC IP User 页启用 IP-Softphone Emulation
3. 建座席 31500/Agent1、31501/Agent2（ACD station=Agent）；建班长 31502/Supervisor
4. COS 放行：Phone Features COS 启用 ACD Prefixes=1（否则前缀登录登出走不通）
5. CCS Configurations> Agents：Agent1 固定（挂 31000）+自指派；Agent2 移动（优选组 Agent_PG）；班长自动自指派
6. IPDSP 注册（分机 31000 + 个人码 0000，实验口径）→ LogOn → 自指派选组登入；Agent2 输 31501 凭优选组登入
7. 删 pilot 演示指南号 70，实现来话免听欢迎语直振座席（p147）

**验收判读**：登入前 Agent_PG 红色（blocked）；Agent1 登入后变 open、pilot 全部激活（p144-145）。

## A2 — 未来触发

使用情境：新开呼叫中心配人员；"座席登不上/登出不了"；班长要不要优选组；末座席退不了；一登录就是退出态；Rainbow 用户能不能当班长；前缀按了没反应。

语言信号：ACD station / agent / supervisor / LogOn / LogOff / self-assigning / 自指派 / Preferred Processing Group / 优选组 / ACD prefix / 前缀 12 / IPDSP / personal code / IP-Softphone Emulation / withdrawal。

与相邻能力区分：座席状态与计时器调优 → 对象调优能力；监听强插等班长技能 → 座席班长特性能力；直通号与私人号归直接呼叫与紧急关闭能力（路由卡）。

## E — 可执行步骤

输入契约：矩阵已建（Agent_PG 存在）、OXE 与 CCS 双台可用、话机/软话机就绪、座席花名册与形态（固定/移动/自指派）已定。

1. 建 ACD 话机：Users>Create，ACD station=ACD authorised phone set；软话机另启 IP-Softphone Emulation。完成标准：话机可注册
2. 建座席与班长：Users>Create，ACD station 分别选 Agent/Supervisor。完成标准：CCD Users 里可见
3. COS 放行 ACD Prefixes：Phone Features COS 启用。完成标准：话机可执行前缀动作
4. CCS 配座席属性：按形态定固定/移动/自指派、挂组、非自指派设优选组。完成标准：每个座席有组可进
5. 班长核对：确认无优选组、自动自指派，可挂多组。完成标准：不在班长页找优选组字段
6. 登入验证：IPDSP 注册 → LogOn →（自指派）选组。完成标准：Navigator 中 Agent_PG 变 open、pilot 激活

判停点：

- 前缀按了没反应 → 查 COS 是否放行 ACD Prefixes（p134）
- 座席"按退出没反应/一登录就是退出态" → 先查 PG 三个管理项（末座席禁退、登入即退出、无应答自动退出），不是故障（n22）
- 给班长配优选组落空 → 设计如此，班长恒自指派（n23）
- Rainbow 场景撞三不限制（multiset/Rainbow 关联/DECT）→ 选型阶段排除，班长无 Rainbow 形态（n39）
- 个人码 0000 类实验值 → 生产强制改（实验口径，n19）

输出契约：可接 ACD 呼叫的人员体系（话机/座席/班长 + 登录验证记录）。

## B — 边界

- 话机兼容清单为 R10.16 口径，新增型号以 Feature list OmniTouch CC Standard Edition 为准（p33）
- Rainbow/WebRTC 网关侧部署在书外——本书只给架构图与登录形态，无落地步骤（n41）
- 多线座席（MEA）、事务码配置归座席班长特性卡，本卡不展开
- 私人号码（private agent number）机制归直接呼叫与紧急关闭卡
- 实验分机/个人码均为实验口径；登录免密的固定座席在生产按安全基线评估
