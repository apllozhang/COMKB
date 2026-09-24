# CCD 对象参数调优（pilot/PG/队列：wrap-up、pause、服务水平、PG 选项、饱和溢出）

## R — 原文依据

> "Pause between two calls … The value, expressed in seconds, must be between 1 and 3276."（p168）
> "Wrap Up duration (sec.) … The value, expressed in seconds, must be between 1 and 3276. To delete the wrap-up, enter the value 0."（p168）
> "Last agent withdrawal authorized … If disabled, the last available agent loses this right to preserve the service."（p172-173）
> "Maximum waiting time Enter the maximum waiting time in seconds (i.e. 45) … Address Enter a destination extension number (i.e. 31010) Delay Enter a time-out in seconds (i.e. 60)"（p192-193）
> "green (quality of service equal to or greater than the warning threshold …), yellow (… superior or equal to 0.8 times the threshold), red (… less than 0.8 times)"（p168）

出处：OTCCXTE100EN p166-193, p275-280。

## I — 自述

调优分三层：pilot 计时器、PG 行为选项、队列饱和与溢出参数。

pilot 计时器（Configurations> Pilot，自动态挂 pilot）：

- wrap-up 与 pause 数值域均为 1-3276 秒；删 pause 填 none、删 wrap-up 填 0（p168）
- 手动 wrap-up 时长（idle 态与 pause 态）挂在 PG 上，书中默认口径 600 秒（p185）
- 归属口诀：自动 wrap-up/pause 改在 pilot，手动 wrap-up 改在 PG——调错对象就是"怎么改都不生效"（n38）

服务水平目标（pilot，p168）：

- 两参数：% of calls + answered within（时限）；计时从听完指南起、到座席摘机止（排队+振铃之和，n37）
- smiley 三色按 SOP（默认 15 分钟）刷新：绿=达到阈值；黄=低于阈值但 ≥0.8×阈值；红=<0.8×阈值

PG 行为选项（Configurations> Processing Group> PG Agents，实验逐项开/关对比，c07）：

- Last agent withdrawal authorized（末座席禁退保服务）、Withdrawal after logon（登入即退出）、Call release by agent forbidden（挂机保持）、Eternal Wrap-Up（操作后回 wrap-up）、Wrap Up in Idle/Pause 时长、Ring rotation time-out（默认 15 秒轮转）、Type of search（Cyclic/Sequential/MIT）

队列参数（System> Queue and Waiting Room）：

- Maximum waiting time：超过即按规则走下一方向（实验 45 秒）
- Queuing overflow：排队超过 Delay 秒改址到指定分机（实验 60 秒改 31010）

## A1 — 书中案例

**调优实验**（p166-193）：

1. Pilot1 设 wrap-up=10s、pause=5s、服务水平目标 85%/15 秒（实验口径）
2. 公网来话应答挂机后，Real time 核对 10 秒 wrap-up 与 5 秒 pause 计时
3. 末座席退出实验：先开"允许"测可退，再关测"被拒"，测完恢复
4. Eternal Wrap-Up 实验：不开时 wrap-up 中外呼即取消；开启后操作完回 wrap-up 直至计时耗尽
5. 手动 wrap-up 设 idle=12s、pause=8s 分别实测回闲时长，测完恢复 600 秒
6. Ring rotation 用默认 15 秒：两座席登入不接话，15 秒后振铃转到另一座席
7. Type of search 三连测：Cyclic 轮流接、Sequential 按序号、MIT 空闲最久先振铃，测完恢复 Cyclic

## A2 — 未来触发

使用情境：座席挂机后状态时间不对；"wrap-up 改了不生效"；smiley 全红查 SLA 口径；座席要接私人电话（pause）；末座席退不了被投诉；队列饱和后溢出去向验证。

语言信号：wrap-up / pause / service level / smiley / SOP / Ring rotation / Last agent withdrawal / Eternal Wrap-Up / Type of search / Cyclic / MIT / Maximum waiting time / Queuing overflow / 3276。

与相邻能力区分：人员与登录 → 座席班长体系能力；监听强插/退出类型命名 → 座席班长特性能力；EWT 阈值播报归排队体验卡（路由卡）；监控呈现归监控与统计能力。

## E — 可执行步骤

输入契约：座席已登入、业务 SLA 与话后处理时长已定、每个选项测试后恢复默认的纪律。

1. 定 pilot 计时器：Configurations> Pilot 设 wrap-up 与 pause（1-3276 秒域）。完成标准：来话挂机后按设定计时走 wrap-up → pause → 回闲
2. 定服务水平：填 % of calls 与 answered within。完成标准：smiley 按 SOP 刷新且颜色与实际达成率一致
3. 逐项测 PG 选项：每项开启测一次行为、关闭再测一次、测完恢复。完成标准：行为对比记录完整（退出允许/拒绝、挂机保持、wrap-up 保持/取消、轮转时长、选座席方式）
4. 定队列参数：Maximum waiting time 与 Queuing overflow 地址/延时。完成标准：饱和与改址配置落位并复核（p193 Notes 溢出行为后续实验复核）
5. 回归验证：恢复全部默认值后再跑一通标准呼叫。完成标准：不残留测试参数影响后续

判停点：

- "wrap-up 怎么改都不生效" → 查归属：自动挂 pilot、手动挂 PG（n38）
- SLA 统计与对外承诺对不上 → 计时起点是"听完指南"非"进队"（n37），指南越长余量越大
- EWT 类参数调整后立刻验证 → TSP 滚动计算有滞后，逐步调参勿单通定论（n30）
- 手动 wrap-up 时长页找不到 600 秒默认 → 该值挂 PG 不挂 pilot（p185）
- 测试值（10s/5s/45s/60s/12s/8s/300s）为实验口径 → 生产按业务测定，不照抄

输出契约：按业务调好的参数集（pilot 计时器 + SLA + PG 选项 + 队列饱和溢出）+ 逐项行为测试记录。

## B — 边界

- 全部数值域为 R10.16 教材口径（1-3276 秒、Ring rotation 15 秒默认、手动 wrap-up 600 秒口径）；扩容与话务建模方法在书外（n30/n41）
- pause 中可接个人/本地/外线呼叫（p279）；wrap-up 中除 Queue info 外任何操作即取消——这是行为语义不是故障
- 服务水平阈值按 pilot 业务性质设定（咨询/售后/投诉），原书不给行业基准值（p168）
- smiley 呈现与 Alarms 呈现是两套（服务水平 vs 阈值越限），监控呈现归监控与统计卡
- 实验逐项测试值均为实验口径，引用必须标注
