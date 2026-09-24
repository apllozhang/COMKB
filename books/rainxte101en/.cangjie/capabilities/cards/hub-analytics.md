# 分析体系（CDR 话单、仪表盘、组报表、MOS 质量）

## R — 原文依据

> "Pure VoIP Rainbow audio/video call doesn't generate CDR"（p318）
> "To follow the evolution of your users' uses (adoption rate), either over the last 7 days or over the last 30 days. You can export the data in CSV format."（p319）
> "For reasons of sensitivity specific to each country and/or customer, a company administrator may disable individual statistics for a specific group."（p325）
> "Jitter: under 30ms the level is acceptable • RTT: latency must not exceed 150ms • Packet loss: must not exceed 1%"（p328）

出处：RAINXTE101EN p317-328。

## I — 自述

运营数据三个视角，口径不同别混用：

1. **CDR 话单**（计费用）：覆盖经 Cloud PBX 的入/出/内部呼叫，月度 .csv；纯 Rainbow VoIP 音视频呼叫**不产生** CDR；ALE 每月 1 日出文件；BP 三通道获取——月度邮件附件 / 网页手工下载 / REST API 自动拉取；ALE 不计费不开票（计费归提供 SIP trunk 的 BP）
2. **分析仪表盘**（行为用）：全局页看近 7/30 天采纳率、用户活跃、许可、1对1/群组/电话量、MOS、终端类型，可导 CSV；Voice 页按呼向 × 目的地（用户/组/欢迎服务/AA）过滤，周期最长 1 年；欢迎服务统计一次最多 5 个；IVR 统计含取消呼叫与主叫停留时长（min/avg/max）；Groups 页来话/接听/等待/时长四类各 4 图，一次最多 5 组同屏
3. **MOS 质量票**（排障用）：所有呼叫结束即采集（默认启用），汇入音质量仪表盘，支撑逐用户排障与网络/防火墙问题定位；技术明细页可过滤

关键数字口径（p319-328）：

| 指标 | 口径 |
|---|---|
| 全局仪表盘周期 | 近 7/30 天，可导 CSV |
| Voice 页周期 | 最长 1 年 |
| 欢迎服务统计 | 一次最多 5 个 |
| 组对比 | 一次最多 5 组同屏 |
| 抖动（Jitter） | <30 ms 可接受 |
| 单向时延（RTT） | ≤150 ms |
| 丢包（Packet loss） | ≤1% |

隐私开关（p325）：公司管理员可按组关闭成员级统计（各国劳动合规敏感度差异）；关闭后服务器仍采集，只是组管理员无权查看。

## A1 — 书中案例

**分析口径要点**（p317-328，讲义，无实验）：书中本章为概念页（截图级），无分步 How-To。典型使用链路：

1. 月度取 CDR 对账（BP 计费口径）
2. 仪表盘看采纳率与话务趋势
3. 组报表核对团队接听
4. MOS 明细定位音质差的用户与网络段

## A2 — 未来触发

使用情境：月度话费对账数据从哪来；统计"全员话务量"发现少了纯 VoIP 部分；客户要坐席绩效报表（劳动合规）；用户反映通话质量差怎么定位；验收要出运营报告。

语言信号：CDR / 话单 / call detail record / 计费 / billing / 仪表盘 / dashboard / 采纳率 / adoption / 报表 / reports / MOS / 质量票 / quality ticket / 抖动 / jitter / RTT / 丢包 / packet loss / 成员级统计 / 隐私。

与相邻能力区分：话务机制与队列参数归呼叫组能力；欢迎服务/IVR 统计的配置侧归欢迎服务 IVR 能力；计费责任与商务模式归网络就绪（trunk 商务）与 Cloud PBX 口径。

## E — 可执行步骤

输入契约：统计目的（计费/行为/质量）、时间范围、涉及组与成员、隐私合规口径（是否允许成员级统计）。

1. 定口径：计费对账用 CDR、行为分析用仪表盘、音质排障用 MOS——三者不混用。完成标准：口径与目的一致
2. 取 CDR：BP 经邮件/网页/REST API 三通道之一取月度文件（每月 1 日出）。完成标准：话单在手且覆盖经 PBX 呼叫
3. 出行为报告：仪表盘选周期与过滤（Voice 页 ≤1 年、服务/组 ≤5）→ 导 CSV。完成标准：报告成文
4. 质量排障：MOS 明细页过滤问题用户 → 对照抖动 <30 ms/RTT ≤150 ms/丢包 ≤1% 阈值定位网络段。完成标准：劣化原因指向网络或终端
5. 隐私设置（如需）：公司管理员按组关闭成员级统计并告知客户法务口径。完成标准：开关状态与说明留档

判停点：

- 用 CDR 做"全员话务量"统计 → 停，纯 VoIP 呼叫不产生 CDR（n50），全量行为用仪表盘
- 客户要坐席绩效报表 → 停，先过当地法务/HR：成员级统计涉及劳动监控合规，可按组关闭（n51）
- 话费争议 → 停，ALE 不计费不开票（p318/n14），计费解释权在 BP/运营商，CDR 只是数据
- MOS 差但终端正常 → 按 Network Requirements 口径查网络（转网络就绪能力），不在本卡改配置

输出契约：运营/质量报告（CDR 对账+仪表盘导出+MOS 结论）+ 隐私开关状态记录。

## B — 边界

- CDR 文件格式与字段细节在 TBE099_Rainbow Hub - Voice services（p318 指针），书内不展开
- MOS 阈值为排查口径，承诺 SLA 在合同层（p328 是参考值）
- 组报表在 Hub 集中于 Reports 页签（p327）；仪表盘分区与图形随版本演进，以实际界面为准
- 实验章节无分析实操（概念章）；"欢迎服务统计最多 5 个/组对比最多 5 组"为工具口径，可能随版本调整
- 成员级统计关闭后数据仍采集（p325）——"关了就删数据"是误读
