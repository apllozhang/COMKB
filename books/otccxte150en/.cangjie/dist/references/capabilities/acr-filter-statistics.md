# ACR 过滤器与统计报表（AND/OR 语义、Super/Hyper-Filter、实时窗口、Excel 三模板）

## R — 原文依据

> "Up to 200 filters • 7 skills per filter max • The call distribution is not impacted by the filters"（p285）
> "Super-Filter: Group of Filters declared in the same node • Hyper-Filter: Group of Filters declared in different nodes • 25 objects per Super-Filter /Hyper-Filter … allow to apply the logical function OR on the call profiles"（p303）
> "When a new filter is created, we cannot retrieve, in Excel files, data prior to the filter creation date • But, keep in mind that 20 predefined filters originally exist"（p302）
> "Filter: Detail Statistics (Formfilter.xls) … Filters: Summary of the statistics (FormFilterS.xls) … Agents per Filter (FormAgentPerFilter.xls)"（p299-301）

出处：OTCCXTE150EN p283-317。

## I — 自述

过滤器是统计分组视角，不改路由——想让某类呼叫优先要改的是优先级、ISM 成本或脚本。

规格口径：

| 项目 | 口径 |
|---|---|
| 过滤器总数 | 最多 200 个（系统出厂预置 20 个，有历史数据） |
| 每过滤器技能数 | 最多 7 个（含级别区间与强制/可选） |
| 过滤器语义 | AND（技能全满足才计入） |
| Super-Filter | 同节点过滤器组，每组 25 对象，OR 语义 |
| Hyper-Filter | 跨节点过滤器组，每组 25 对象，OR 语义 |
| 对分发的影响 | 无（仅实时观测与统计口径） |
| 数据时效 | Excel 数据从过滤器创建时刻起算 |

过滤器可基于呼叫档案、授权名单或非授权名单，可配服务水准目标（如 75% 呼叫 15 秒内）与效率告警阈值。

实时观测窗口族：Real time/Filter、Waiting Room（快捷键 CTRL 加左键）、Calls in Waiting Room、Breakdown by Criteria、临时过滤器（窗口关即失效）、Statistics/Last received calls（近一小时）。

Excel 三模板分工：Formfilter.xls 明细（按时间片粒度）、FormFilterS.xls 汇总（每过滤器一行）、FormAgentPerFilter.xls 坐席乘过滤器交叉活动；Super/Hyper-Filter 亦可出 Excel。

## A1 — 书中案例

**过滤器实验（c11）**：

1. 建 Filter 1：Car 技能 4-9 强制加 English 4-9 强制
2. 同法建 Filter 2（Home 加 English 强制）与 Filter 3（Car 加 Home 加 English 均 5-9 any）
3. 全部配服务水准 75% 15 秒、效率 85%（实验口径）
4. Super Objects 建 Super-Filter：选入 Filter 1 与 Filter 2
5. 实时窗口依次看三个过滤器：Filter 3 无数据（没有同时带三种技能需求的档案）
6. Super-Filter 有数据（Filter 1 与 Filter 2 的并集）
7. 坐席全忙时呼各入口，开 Calls in Waiting Room 观察等待呼叫
8. 出 Excel 明细与汇总两张报表核对粒度差异

## A2 — 未来触发

使用情境：交付验收要业务视角报表；监控大客户呼叫量；Filter 口径数字对不上；要跨节点合并统计；月中要新口径报表。

语言信号：过滤器 / Filter / Super-Filter / Hyper-Filter / AND / OR / 服务水准 / Service Level / 实时监控 / Real time / Excel 报表 / Formfilter / 等待房间观测 / 临时过滤器。

与相邻能力区分：呼叫优先级控制，见 综合规则组合能力；业务入口与档案，见 CCD 矩阵地基能力；名单类过滤器的前提，见 名单规则卡（路由）。

## E — 可执行步骤

输入契约：业务分组口径（技能组合与级别）、服务水准目标值、节点拓扑（跨节点时）。报表口径先与客户书面确认。

1. 规划过滤器清单：每组口径是 AND 还是 OR，决定建 Filter 还是 Super-Filter。完成标准：口径表评审通过
2. CCS 的 Filter 页建过滤器：技能加级别区间加强制/可选。完成标准：过滤器保存
3. 配服务水准目标与效率告警阈值。完成标准：阈值可告警
4. （跨口径统计）Super Objects 建 Super/Hyper-Filter 选入成员。完成标准：组内 25 对象以内
5. 实时窗口核对：逐个过滤器看实时数据。完成标准：AND/OR 口径与预期一致
6. 出 Excel 明细与汇总报表。完成标准：粒度与行数符合模板分工
7. 新口径过滤器提前建（数据从创建时刻起算）。完成标准：交付日历含建过滤器节点

判停点：

- Filter 长期零数据 → 停，AND 口径下可能没有呼叫同时带全部技能，改 OR 组或收窄技能
- 想用过滤器让呼叫优先 → 停，过滤器不影响分发，改优先级/成本/脚本
- 月中要历史报表 → 停，新过滤器无历史，先用预置 20 个过滤器口径救急
- 临时过滤器窗口关了数据没了 → 正常，临时过滤器只活到窗口关闭

输出契约：过滤器与超组配置 + 实时观测视图 + Excel 报表样张。

## B — 边界

- "Super-Filer / Hyper-Filer"（p314）为原文拼写（照录）
- 过滤器建在 CCS；预置 20 个过滤器之外的口径均从创建时刻起算
- 服务水准与效率阈值样例值为实验口径，目标值须与客户约定
- 服务水准的历史测算方法（话务建模）原书不涉及，仅给观测口径
- 跨节点 Hyper-Filter 的多节点组网前提在书外（混合链路细节同为书外）
