# 共享 WebRTC 网关池与容量规划（三配置对比、406 溢出、TBE067 sizing）

## R — 原文依据

> "Allows multiple OXEs to share the same WebRTC gateway pool • Increase capacity for simultaneous calls • Resilience in the event of a WebRTC failure"（p147）
> "If the traffic limit is reached, the gateway responds to a new request with a SIP message '406 - Not Acceptable'. As a result, the OXE will overflow onto the next ARS route"（p149）
> "If this parameter is empty, the SIP trunk limit will determine the overflow."（p149）
> "A WebRTC gateway supports up to 400 simultaneous streams."（p151）

出处：RAINXTE003EN p146-152。

## I — 自述

规模化时网关怎么摆，三种配置（p146-148）：

| 配置 | 结构 | 取舍 |
|---|---|---|
| 每 OXE 网关复制 | 每个 OXE 挂自己的网关 | 抗故障+增并发但成本高；书中示例：每 OXE 用户数 ≥5000 才划算 |
| 共享 WebRTC 池（推荐） | 多 OXE 共享网关池，按 OXE 集群推进 | 抗故障+增并发+省成本；代价是 ARS 管理复杂度随节点数上升 |
| OXE 网络 | 多节点（高低流量混合）池化网关组 | 面向多站点组网场景 |

溢出机制（p149）：

1. 每网关最大并发流在 Rainbow 界面（Communications、Equipments、编辑该 PBX）设定
2. 满载时网关对新请求回 SIP 406 Not Acceptable，OXE 依 ARS 表声明顺序溢出到下一条路由
3. 该参数留空时溢出由 SIP trunk 限制决定——池化弹性会悄悄失效，交付核查必查项（n27）
4. 硬要求：每 OXE 节点对每网关一条 SIP trunk/外部 SIP 网关，各节点 ARS 管理需相似

容量口径（p151）：

1. 单网关上限 400 并发流；用户数与并发数是两个量纲，报容量先声明口径
2. TBE067 Excel 工具四输入：OXE 用户总数、持 Rainbow 客户端用户数、Rainbow 客户端使用率、客户端间直呼占比
3. 工具输出所需并发通道数，再据此推算 OXE 压缩器数量
4. 工具适用 OXE 101.0 MD3 / WebRTC 3.x 起（版本口径见 needs-review nr-03）

## A1 — 书中案例

**sizing 评估流程**（p151，讲义章无分步实验）：

1. 取 TBE067_Rainbow - WebRTC Gateway Pres&Sizing 工具包（MyPortal/ALE 内部链接）
2. 输入四个关键值：用户总数、Rainbow 用户数、使用率、直呼占比
3. 流量模型假设可按站点调整（工具内可改）
4. 读出并发通道数，与单网关 400 并发上限对照定网关数量
5. 由通道数推算 OXE 压缩器数量并核对硬件资源

## A2 — 未来触发

使用情境：多台 OXE 共用网关；网关池怎么扩容；容量与通道数怎么报；ARS 溢出怎么配；网关满载后第二路由不生效。

语言信号：共享池 / shared pool / 网关复制 / duplication / OXE cluster / 集群 / 406 / 溢出 / overflow / ARS / 容量 / capacity / sizing / TBE067 / 400 并发 / 通道 / channels / 压缩器。

与相邻能力区分：

- 网关本身安装升级 → 网关部署能力
- 溢出路由的 OXE 侧逐字段配置 → OXE 侧网关配置能力
- 网络前提与带宽核查 → 网络就绪能力（路由卡）

## E — 可执行步骤

输入契约：OXE 节点清单与用户分布、Rainbow 用户画像（可支撑四输入取值）、话务假设来源、网关资源预算。话务画像拿不到 → 判停，先与客户共同定假设再算。

1. 选架构：默认共享池按集群推进；仅超高流量（示例 ≥5000 用户/OXE）评估复制。完成标准：架构决策成文
2. 算容量：TBE067 填四输入得通道数，对照 400 上限定网关数。完成标准：通道数与网关数有依据
3. 定溢出参数：Rainbow 端逐网关填最大并发流，不留空。完成标准：406 溢出链生效
4. 核 trunk 配比：每 OXE 节点对每网关一条 SIP trunk。完成标准：配比核查通过
5. 验证：压测或人工满载触发 406，确认溢出到 ARS 下一条路由。完成标准：溢出行为实测成立

判停点：

- 溢出参数为空 → 停，SIP trunk 限制接管、池化弹性失效（n27），填值并记入变更单
- 节点间 ARS 管理差异大 → 停，先统一 ARS 再池化，否则溢出顺序不可预期
- 通道需求超 400 → 停，加网关而非调参（单网关硬上限）
- 话务假设无来源 → 停，不虚构容量结论；标注假设并让客户确认

输出契约：网关池架构决策 + TBE067 估算记录（含假设）+ 溢出参数与 trunk 配比核查单。

## B — 边界

- TBE067 工具本体与流量建模假设在书外（MyPortal/ALE 内部链接，p151）；本卡只有流程与口径
- 图示示例值 400 为实验口径示例；400 是单网关上限，不是站点容量
- 详细池化配置在 TC2462（p149 指向）；书内无逐字段池化实验
- OXE 网络架构（ABC/FABC/F 节点）书中仅概述，多节点组网细节在书外
