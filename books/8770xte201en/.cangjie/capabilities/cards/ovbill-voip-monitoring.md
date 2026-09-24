# VoIP 性能监控（IP ticket、KPI 阈值、清理周期、质量报告与空表排障）

## R — 原文依据

> "A call between 2 IP devices is divided into one or more segments • IP tickets are generated at the end of each segment"（p408）
> "VoIP quality thresholds used for predefined reports • Delay > Average Delay (150ms by default) • Packet loss > Loss rate (3% by default) • BFI Burst > Only used for the segment over 3% (5% by default)"（p414）
> "R&D defined that communication is bad when there is more than 3% of BFI during communication. ­ BFI Burst: ... is the rate of segment (10s) during a communication where there is 3% of BFI."（p422）
> "To generate a report with data, all calls must external outgoing call from one pod to another."（p428）

出处：8770XTE201EN p405-428。

## I — 自述

VoIP 性能的量化口径：每段 IP 通话出 IP ticket（按段出票，跨节点即多段、双向各一票），票面含设备类型、源/目的 IP 与分机、压缩算法（G711/G723/G729A）、收/发/丢包数、时延表、BFI 密度。

- 三个 KPI 默认阈值：平均时延 >150ms；丢包率 >3%；BFI Burst >5%——BFI（Bad Frame Interpolation）是设备为丢包/长时延补造的帧，通信 BFI>3% 才统计 burst（BFI≥3% 的 10 秒段占比）；预定义报告按这三阈值统计"超限票率"，MOS 以散点图呈现
- 文件侧与计费同构：OXE 存 IP*****.DAT+IP.LIS 与 SIP*****.DAT+SIP.LIS，同步比对后 FTP 取回为 .DAI 交加载过滤（观察对象/观察日/IP 掩码）入库；夜间汇总为累计计数器，供超阈值告警与邮件
- 清理默认值（Preferences > Accounting > Accounting preference）：VoIP 小时计数器 45 天、日计数器 94 天、月计数器 15 个月、年计数器 36 个月、VoIP 票据 15 天；VoIP 报表 94 天（Reports preference）
- 参数位置：KPI 阈值与编解码子目录参数在 Nmc > Application Configuration > Application Settings > Accounting > VoipParameters（按 G711 等分子目录：SID 帧 packet size 1，语音包 20ms 帧长 packet size 180，BFI rate 3）
- 维护工具：ipview 逐字段查看 IP 票据（与计费 accview 同型）；OXE 侧 /usr4/account 的 IP*.DAT 与清单文件

## A1 — 书中案例

**VoIP 性能配置实验**（p417-428，How-To 章节）：

1. OXE 侧确认外部计费已开且 IP tickets 出票启用（Validate the external accounting / VoIP tickets）
2. 配置 IP 票据加载过滤（观察对象/观察日/IP 掩码）并验证取回
3. 需要立即出计数器时手工触发 IP cumulative counter calculation（平时夜间自动）
4. Preferences 核对五项清理周期（小时 45 天/日 94 天/月 15 月/年 36 月/票据 15 天）
5. VoipParameters 核对三阈值与编解码子目录参数（150ms/3%/5%，BFI rate 3）
6. 打一批跨 POD 出局 IP 呼叫（必要时 account compress），SSH 查 /usr4/account 的 IP*.DAT
7. 用 ipview 查票据字段；生成 Voice over IP 目录预定义报告（过滤器 Date/Hour=This Week、System/Sender IP/Board+Phone number not empty）
8. 排障认知：同机软话机互打取不回质量数据，报告为空

## A2 — 未来触发

使用情境：用户抱怨通话质量差；MOS/丢包/时延怎么看；VoIP 报告是空表；IP 票据保留多久；KPI 阈值想按网调整；超限告警与邮件。

语言信号：VoIP / IP ticket / IP.LIS / SIP.LIS / 时延 / delay 150ms / 丢包 / packet loss / BFI / BFI Burst / MOS / KPI / ipview / VoipParameters / 质量报告 / 超限 / 清理 / purge。

与相邻能力区分：WBM 实时仪表盘属 Web Performance 能力（本卡是厚客户端报表面）；话务量统计与超限动作配置属流量与 Tracking 能力。

## E — 可执行步骤

输入契约：OXE 已纳管且计费回收链路通；有真实跨节点/出局 IP 话务。话务路径不通 → 判停先解决呼叫路径，再查监控配置。

1. OXE 侧确认外部计费与 IP tickets 出票开启。完成标准：/usr4/account 出现 IP*.DAT
2. 配 IP 票据加载过滤并验证取回（.DAI 入库）。完成标准：日志显示票据读入
3. VoipParameters 核对三 KPI 阈值与编解码参数。完成标准：阈值口径与网络组确认
4. Preferences 核对五项清理周期。完成标准：与库容量策略一致
5. 生成跨节点出局话务并触发计数器计算。完成标准：计数器非零
6. 生成预定义 VoIP 质量报告并查看超限票率与 MOS 散点。完成标准：报告有数据

判停点：

- VoIP 报告为空 → 先核对呼叫路径是否走被监控承载段（书内口径：跨 POD 出局；同机软话机互打无效），再查开关与过滤器
- 质量差但票里无丢包 → 分段与方向问题（每段双向各一票），按段分析不按呼叫
- 想改"超 3% BFI 才算坏"的口径 → 这是 R&D 定义的阈值族（150ms/3%/5%），调整在 VoipParameters 并评估报告口径变化
- 票据 15 天清理默认值对投诉追溯不够 → 提前归档属归档能力（计费票据生命周期），本卡清理只覆盖 VoIP 域

输出契约：KPI 阈值配置表 + 清理周期表 + 报告实例（超限票率）+ 空表排障结论。

## B — 边界

- 全部阈值与清理周期为 Ed45 默认值（可调）；生产按网络实际调 KPI 并同步修订报告口径
- "跨 POD 出局才有数据"是实验口径，生产类推为"话务须走被监控的 IP 承载段"（生产类推，n32）
- MOS 书中仅作质量分呈现（散点图），未展开算法；MOS 计算方法在书外
- 本卡覆盖厚客户端报表面；实时仪表盘（SNMP/CDR 双腿）属 Web Performance 能力
- 加载性能参考值 52 tic/sec 为实验口径，非生产容量结论（p114）
