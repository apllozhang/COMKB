# Rainbow Hub 网络前提与 Pilot 评估（Network Requirements、带宽口径）

## R — 原文依据

> "Use the following URL to get all the information and updates needed to implement Rainbow Hybrid and Rainbow Hub https://help.openrainbow.com/hc/en-us/articles/23942019777170-Check-Rainbow-Network-Requirements"（p37）
> "This document details: ... Detailed list of ports and protocols • Rainbow domains and associated IP addresses • Bandwidth requirements • Configuration of corporate network elements DNS, Proxy, Firewall"（p41）
> "RAINBOW PILOT allows you to assess your Rainbow connectivity from your location, and the capacity of a given location to handle a population of Rainbow users"（p43）

出处：RAINXTE101EN p36-45, p88-90, p136。

## I — 自述

Hub 是纯云方案（客户侧无 PBX/SBC/VPN，p7），网络前提集中在外部权威文档与评估工具：

1. **查文档**：help.openrainbow.com 固定 URL 的 Network Requirements 文章（Hybrid 与 Hub 通用）——含基础设施更新流程、上版以来的变更注、协作/混合话音/Hub 三块端口协议摘要，并挂两份 PDF（通用版 + 健康数据托管版）
2. **取数值**：PDF 正文覆盖端口协议、运行原理与流量、域名 IP 清单、带宽要求、企业网 DNS/代理/防火墙配置——生产数值唯一依据；书内只有两张局部摘录（见下）
3. **跑评估**：pilot.openrainbow.com/home——从客户现场测连通性，按协作/会议/混合话音/Hub 话音的用法配比评估站点可承载用户规模；设备章再次要求"用 Pilot 做全套测试判断网络是否正确"（p136）

书内两张局部摘录（生产仍以 PDF 全文为准）：

| 口径 | 数值 | 出处 |
|---|---|---|
| Rainbow 客户端音频（Opus） | 80 kbps 单向 | p90 |
| Rainbow 客户端视频（VP8） | 1.5 Mbps（720p/30fps） | p90 |
| SIP 设备音频（G711） | 64 kbps | p90 |
| 客户端/SIP 设备信令 | 可忽略 | p90 |
| 带宽核算位置 | 客户 premises 到 SIP trunk 段 | p90 |
| 设备端口 | TCP 5061/443、UDP 30000-44999/53/123、TCP 22（见设备部署卡） | p136 |

## A1 — 书中案例

**评估流程**（p43-44，讲义）：书中给工具入口与用途，无分步实验；Ed16 截图中部分测试分区标注 "To come"——分区随平台演进，以工具实际界面为准。SIP trunk 的商务模式（bundled 一单一发票 / separated 两单两票）与带宽共同构成站点上线前提（p88-90）。

## A2 — 未来触发

使用情境：上 Hub 前网络要开什么端口；带宽怎么估；防火墙/代理/ DNS 要放行什么；站点能带多少 Hub 话音用户；话机注册不上怀疑网络；trunk 商务模式怎么选。

语言信号：网络要求 / network requirements / 端口 / ports / 防火墙 / firewall / 带宽 / bandwidth / Pilot / 连通性 / connectivity / 勘测 / Opus / G711 / 80 kbps / SIP trunk / bundled / separated / HTTP 代理。

与相邻能力区分：设备端口表与 zero-touch 排雷归设备部署能力；trunk 绑定与编号计划归 Cloud PBX 能力；话机注册排障第一入口归设备维护能力（HTTP 代理不支持在本卡 B 段提示）。

## E — 可执行步骤

输入契约：站点出口网络信息（出口 IP/代理/防火墙管控方）、用户规模与用法画像（协作/会议/Hub 话音配比）、trunk 商务模式选择。

1. 取文档：支持站文章 + 两份 PDF（必须最新版，注意 Edition 迭代与变更注）。完成标准：当期版本文档在手
2. 核端口与域名：按 PDF 清单核对防火墙/DNS/代理配置，重点核 UDP 30000-44999 媒体段。完成标准：放行清单确认或整改项列出
3. 核带宽：按书内四行口径初估（Opus 80 kbps/VP8 1.5 Mbps/G711 64 kbps），再按 PDF 全文复核。完成标准：带宽结论成文并注明核算段（premises 到 trunk）
4. 跑 Pilot：现场测连通性 → 按用法配比跑承载评估。完成标准：连通性通过 + 承载结论成文
5. 定商务模式：与 BP 确认 bundled 或 separated（影响合同与发票）。完成标准：商务口径写入方案

判停点：

- PDF 数值与现场设备配置冲突 → 以 PDF 为准提交整改，不要按现场习惯放行
- Pilot 某分区不可用 → 工具演进所致（To come，n02），换等效手段或以 PDF 核查兜底，不虚构结果
- 客户网络全代理出网 → 停，ALE SIP 终端不支持经 HTTP 代理穿越（p334，n52），先改网络再谈部署
- 容量评估临界（话音占比高）→ 上浮带宽与通道规划，与 Cloud PBX 能力联判

输出契约：网络就绪核查单（端口/域名/带宽放行状态）+ Pilot 评估结论 + trunk 商务模式确认单。

## B — 边界

- 本卡只有指针与工具，**无端口/带宽全集**：一切生产数值以当期《Rainbow Network Requirements》PDF 为准——原书明确的边界，不是本卡偷懒（n01）
- 带宽四行表为书内指示性口径（p90），完整要求以 PDF 为准
- 认证 SIP 运营商清单在 help.openrainbow.com（p78）；清单外运营商不在本卡范围
- Pilot 分区随版本演进（n02）：结论引用时注明评估日期与工具版本
- 健康数据托管场景有专门 PDF，医疗类客户必须另核（p41）
