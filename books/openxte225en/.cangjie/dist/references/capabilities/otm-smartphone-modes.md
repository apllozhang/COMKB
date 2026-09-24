# 智能手机连接模式与回落（WiFi/3G4G/DTMF、Android 无 SIM、功能形态）

## R — 原文依据

> "Data connection possible: Wifi available (Inside the company / Outside)… 3G/4G data network … No data connection: Fallback mode using DTMF"（p166）
> "Features provided in fallback mode based on DTMF over voice flow: Communication context: Make call & Release call; Voicemail; Routing (limited)"（p175）
> "Android Smartphones can run without SIM card; Smartphone is then used as a pure VoIP softphone: No carrier charge … No cellular network, so following features are discarded: Fallback mode, Private calls, SMS"（p176）

出处：OPENXTE225EN p162-177。

## I — 自述

OTC 智能手机按数据连接形态分五类场景，决定可用功能面：

| 场景 | Web 服务 | 话音 | 备注 |
|---|---|---|---|
| 公司内 WiFi | 可用 | VoIP（可加密） | 走内部拓扑 |
| 场外热点 WiFi | 可用 | VoIP（经 RP/SBC） | 全功能 |
| 3G/4G 数据 | 可用 | VoIP 或 PSTN（cellular 模式） | 双模式倒换 |
| 无数据连接 | 不可用 | DTMF 回落 | 带内指令 |
| 无 SIM（Android） | WiFi 时可用 | 纯 VoIP | 见下 |

无数据时的 DTMF 回落能力清单：打/挂电话、留言（voicemail）、有限路由——靠话音流上的 DTMF 指令，需要中继侧 DISA/DTMF 序列配合（RE Parameters 可改序列）。

Android 无 SIM 纯 VoIP 话机：省运营商费用；设置要求业务手机号留空、VoIP 模式常开、来话弹屏常开。代价：无蜂窝网故回落模式、私人呼叫、短信三项全部不可用。

有数据通道时的高级服务清单（p173-175/p177）：单号码、来话/通话中控制、统一目录与呼叫日志、呈现、可视留言、N 方会议（N>3）、IM、监督代接、经理/助理等。

## A1 — 书中案例

按连接形态做能力承诺（p166-177 讲义口径）：

1. 用户问"出差国外怎么办"：对应场外 WiFi 或 3G/4G 场景，VoIP 经边缘全功能
2. 用户问"地下车库没信号还能干嘛"：对应无数据场景，仅 DTMF 回落三件事
3. 客户问"能不能不发话费"：Android 无 SIM 方案可行，但带三项功能代价
4. 汇总表核对（p176）：Android 支持四种形态；iPhone 行以原表截图为准（needs-review nr-05）

## A2 — 未来触发

使用情境：移动方案售前沟通（什么网络下有什么功能）；客户要"WiFi-only 话机"方案；写功能承诺清单；排查"没流量时行为不符预期"。

语言信号：WiFi / 3G / 4G / GSM / cellular / 回落 / fallback / DTMF / 无 SIM / 纯 VoIP / 短信 / 私人呼叫 / 单号码 / 呈现 / 可视留言 / 双模式。

与相邻能力区分：

- 怎么把手机开起来 → 智能手机配置能力
- iPhone 推送机制 → iPhone APNS 能力
- 回落所需的 DISA/DTMF 配置 → 智能手机配置能力

## E — 可执行步骤

输入契约：用户网络形态（场内/场外 WiFi、蜂窝、无数据）、平台（Android/iPhone）、功能承诺范围。

1. 按场景表定位用户主要形态。完成标准：形态标签明确
2. 按形态列可用功能面（VoIP/回落/高级服务）。完成标准：功能清单有 p166-177 依据
3. 无 SIM 方案评估：明确回落、私人呼叫、短信三项不可用。完成标准：客户书面确认接受代价（n23）
4. 回落需求核查：确认中继侧 DISA/DTMF 序列配置存在（转智能手机配置能力）。完成标准：回落链路有配置依据
5. 交付说明：把"dial from 特例""推送依赖"等行为口径写入用户须知（转对应能力）

判停点：

- 客户要 iPhone 的逐格功能矩阵 → 停，汇总表部分格以原书截图为准（nr-05），不凭转写承诺
- 客户接受无 SIM 方案但要求短信 → 停，功能矛盾，n23 三项代价不可绕
- 客户问蜂窝网络下的实测体验数据 → 停，书内无 QoS/实测口径（nr-07）

输出契约：按网络形态的功能承诺清单 + 无 SIM 方案的代价确认 + 回落链路配置移交项。

## B — 边界

- p176 汇总矩阵 iPhone 行部分格未打勾、以原表截图为准（needs-review nr-05）
- DTMF 回落仅打/挂/留言/有限路由，不承载高级服务（p175）
- 无 SIM 三项代价（回落/私人呼叫/短信）是 Android 平台特有边界（n23）
- 高级服务清单依赖数据通道；无数据时一律退化为 DTMF 带内指令
- 教材语境为 3G/4G/GSM 时代（2017-2018），后续蜂窝演进不在书内
