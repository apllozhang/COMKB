# 实时监控告警与 Excel 统计（Navigator/CSTA/三级告警/报表）

## R — 原文依据

> "The snapshot, refreshed every 3 seconds by default, provides: Objects state … Traffic indicator … Alarms indication (threshold violation)"（p402）
> "Real time refresh frequency (1..50 sec) … MSP (5 mn …60 mn) for statistics on MSP"（p80）
> "Alarms: this list contains the high-level alarms. The number of events stored (100 maxi) … Alerts: the alerts only concern overflow of the thresholds … Indications: … a calendar transition, an indication is sent one minute before."（p425）
> "CSTA-Monitored must be set to « yes » in the OXE to display values for the trunk group"（p414）
> "The second object begin always after 132 rows. To be able to display one day with the granularity of ¼ hour, Excel need 96 rows."（p520）

出处：OTCCXTE100EN p401-448, p477-526。

## I — 自述

监控三层（f18/f19/p08/p09）：

- Navigator 快照默认 3 秒（可调 1-50 秒）：对象状态、话务指示、告警提示；对象可 shift+拖动，每 pilot 一个页签；Real Time Info 定制每类对象旁的计数器
- MSP 统计 5-60 分钟（实验 15 分钟档），座席 PG 视图饼图默认 30 秒刷新；Pilots S.L. 页看服务水平与 smiley
- 三级事件各存 100 条：Alarms（高级别，红圈）、Alerts（阈值越限，黄圈）、Indications（对象增删改，日历切换前 1 分钟有预告，蓝圈）；阈值入口四处（Trunk group/Pilot/Queue/PG Agent）；呈现渠道四种（窗口/对象闪烁/声音/计数器底色）

中继组实时：OXE 侧 Trunk Group 必须勾 CSTA-Monitored=YES，否则唯独中继组视图空白（n29）。

Excel 统计（f17/p11/p12）：

- 数据流：OXE 午夜生成 5 类临时文件（/usr4/afe，存 24 小时）合并为 hr（明细，默认存 5 周）、dy（日统计）、ev（状态流水）（各存 12 个月，/DHS3dyn/afe）
- 报表参数：每类对象默认 1 个、最多 50 个（改后重启 CCS）；粒度 ¼h/½h/1h；多对象时第二对象从 132 行起（¼h 一天占 96 行）；输出 Print/Save/Excel Display
- 预编译报表：Daily edition 定模板与输出时刻；产物落 C:\ProgramData\Alcatel\CCSupervisor\Excel\{daily,weekly,monthly}（目录旧写法见 nr-06）
- 口径开关：被关闭 pilot 来话计入 redirected 还是 inbound；拒绝呼叫计入 redirected 还是 handled；只有 Business 码进 Excel（n36）

## A1 — 书中案例

**监控实验**（p430-448）：

1. Navigator Tab5/Tab6 分别配 After-Sales(31600) 与 Offer(31601) 全对象视图并按号命名
2. Real Time Info 定制：pilots=通话数、队列=排队数、PG=ACD 通话数/ACD 呼叫计数
3. Advanced Options 给座席各状态配色，观察 logon/wrap-up/振铃/通话四态
4. OXE 中继组 1-T2-SIP PUBLIC 勾 CSTA-Monitored；CCS 里把 busy rate 阈值从 80% 改 1 触发告警
5. 打一通 ACD 呼叫 → Busy/Total % 变色出 Alert → 阈值改回 80
6. Real time> Pilots S.L. 连打数通观察 MSP 15 分钟统计演化；Incidents/Alarms 窗核对三级事件

**Excel 实验**（p517-526）：

1. Window> Customise> Statistics 把对象数放宽（统计 pilot/pilot/PG/座席各 5），重启 CCS
2. Statistics> Excel> Pilot 选两 pilot 加模板，Excel Display 出 Daily ¼h 报表，核对 132 行偏移
3. Abandoned Calls 出弃呼清单（CCA 10.7.8.0+ 支持超链接回呼）；Transaction Code 出码记录
4. Precompiled statistics 配 Daily 日报（粒度 1 小时），Automatic edition restart 手动重跑

## A2 — 未来触发

使用情境：搭值班监控大屏；中继组实时没数据；告警太多想分级；月末出报表；报表里第二对象错位；座席匿名化；"报表没数据"查数据流。

语言信号：Navigator / Real Time Info / CSTA-Monitored / busy rate / Alarms / Alerts / Indications / MSP / Pilots S.L. / smiley / Excel / 132 行 / Precompiled / 弃呼 / ShowStatisticWithData。

与相邻能力区分：smiley 判定与 SLA 口径 → 对象调优能力；Business 码怎么配 → 座席班长特性能力；ccs.ini 手改参数归 CCS 安装卡。

## E — 可执行步骤

输入契约：CCS 可用、监控对象清单与阈值策略已定、报表模板需求已定。

1. 配页签与计数器：每业务 pilot 一个页签，Real Time Info 按对象选计数器。完成标准：3 秒快照内状态变化可见
2. 开中继组实时：OXE Trunk Group 勾 CSTA-Monitored=YES。完成标准：Real time> Trunk group 有值
3. 定阈值与告警口径：四处入口按对象设阈值，必要时临时调低验证告警链路后复原。完成标准：Alarms/Alerts/Indications 三窗各见一例
4. 放宽报表对象数并重启 CCS：Window> Customise> Statistics。完成标准：新对象数生效
5. 出报表并核版式：Pilot/弃呼/事务码报表各出一次，核对 132 行偏移与 96 行/天。完成标准：多对象不错位
6. 配预编译日报：选模板、粒度、输出时刻。完成标准：文件落 ProgramData\Alcatel\CCSupervisor\Excel 目录

判停点：

- 唯独中继组实时空白 → 查 CSTA-Monitored 开关，别往 CCS 排障方向跑偏（n29）
- 报表完全没数据 → 自底向上查数据流：先看 /usr4/afe 临时文件，再看 /DHS3dyn/afe 合并文件，最后 CCS 读取（f17）
- 座席会话报表全是无数据行 → ccs.ini 手写 ShowStatisticWithData=1（CCS 10.5+，n10）
- 改了对象数/Excel 参数没反应 → 必须重启 CCS（n21）
- 找不到自动报表目录 → 两个历史路径都查（nr-06）

输出契约：运行监控大屏（页签+计数器+告警链路验证记录）+ 报表产物（模板/粒度/目录/口径开关清单）。

## B — 边界

- 快照 1-50 秒、MSP 5-60 分钟、告警各存 100 条为 R10.16/CCS 10.5 口径（p80/p425）
- Excel 宏（ACDMacro）与高级模板在 OTCC901，本书只到预编译日报（n41）
- 弃呼回拨超链接依赖 CCA 10.7.8.0+ 座席桌面，CCA 本身在书外（p508/n41）
- 实验阈值（1%/80%）为验证口径，生产按话务设定；话务建模书外（n30）
- 座席匿名化与 Excel 表单保护密码（默认 alcatel）生产必须改（p502/n19）
