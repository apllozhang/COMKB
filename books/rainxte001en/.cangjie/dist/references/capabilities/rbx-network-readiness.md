# Rainbow 网络就绪核查（网络要求文档、Rainbow Pilot 评估）

## R — 原文依据

> "This page contains: ... A summary of port/protocol requirements for: Rainbow collaboration, Rainbow hybrid telephony, Rainbow Hub • 2 PDF files"（p36）
> "This document details: ... Rainbow domains and associated IP addresses • Bandwidth requirements • Configuration of corporate network elements • DNS, Proxy, Firewall..."（p40）
> "RAINBOW PILOT allows you to assess your Rainbow connectivity from your location, and the capacity of a given location to handle a population of Rainbow users"（p42）

出处：RAINXTE001EN p35-45。

## I — 自述

上线前的网络前提核查三步：

1. **查文档**：help.openrainbow.com 的 "Check Rainbow Network Requirements" 文章——含基础设施更新流程说明、上版变更说明、三类端口/协议摘要（协作/混合话音/Hub），并附两份 PDF（Network Requirements、Health data hosting）
2. **取数值**：PDF 内含端口与协议清单、运行原理与流量、域名与关联 IP、带宽要求、企业网络设备（DNS/Proxy/防火墙）配置要求——生产数值唯一依据
3. **跑评估**：pilot.openrainbow.com——从客户现场测连通性；按协作/会议/混合话音/Hub 的用户用法配比评估站点承载规模

## A1 — 书中案例

**评估流程**（p41-44，讲义）：书中给工具入口与用途，无分步实验；注意 Ed13 截图中部分测试分区标注 "To come"——分区随平台演进，以工具实际界面为准。

## A2 — 未来触发

使用情境：上 Rainbow 前网络要开什么；端口清单；带宽怎么估；防火墙要放行什么；站点能带多少 Rainbow 用户；连通性测试。

语言信号：网络要求 / network requirements / 端口 / ports / 防火墙 / firewall / 带宽 / bandwidth / Pilot / 连通性 / connectivity / 勘测。

与相邻能力区分：接入后的连接排障 → PBX 接入能力（Webdiag 判据）；网关媒体路径配置 → 网关部署能力（TURN 在其边界）。

## E — 可执行步骤

输入契约：站点出口网络信息（出口 IP/代理/防火墙管控方）、用户规模与用法画像。拿不到防火墙管控权 → 判停先找客户网络组。

1. 取文档：支持站文章 + 两份 PDF（必须最新版，注意 Edxx 迭代与变更说明）。完成标准：当期版本文档在手
2. 核端口与域名：按 PDF 清单核对防火墙/DNS/代理配置。完成标准：放行清单确认或整改项列出
3. 跑 Pilot：现场测连通性 → 按用户用法配比跑容量评估。完成标准：连通性通过 + 承载结论成文
4. 留档：端口/带宽/评估结论写入交付基线。完成标准：网络就绪证据链完整

判停点：

- PDF 数值与现场设备配置冲突 → 以 PDF 为准提交整改，不要按现场习惯放行
- Pilot 某分区不可用 → 工具演进所致（To come），换等效手段或以 PDF 核查兜底，不虚构结果
- 容量评估临界（混合话音占比高）→ 上浮通道规划并与网关规划能力联判

输出契约：网络就绪核查单（端口/域名/带宽放行状态）+ Pilot 评估结论。

## B — 边界

- 本卡只有指针与工具，**无端口/带宽具体数值**：一切数值以当期《Rainbow Network Requirements》PDF 为准——这是原书明确的边界，不是本卡偷懒
- Rainbow Hub 仅在文档与 Pilot 口径中出现，本教材无定义（passing mention）
- Pilot 分区随版本演进（n03）：结论引用时注明评估日期与工具版本
- 健康数据托管场景有专门 PDF（Health data hosting），医疗类客户必须另核
