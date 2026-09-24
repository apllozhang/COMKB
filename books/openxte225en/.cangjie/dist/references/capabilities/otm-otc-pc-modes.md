# OTC PC 远程办公两模式（multi-devices 副设备、Nomadic SIP 池化）

## R — 原文依据

> "Multi-devices operation brings a second way for users to use their OTC PC application as a client to phone. It's the possibility to associate a SIP extension as a secondary device to the user."（p152）
> "The previous way is still always possible, and is, based on the Nomadic feature with Nomadic SIP. In this case, if the user selects computer as current device, the main set … is frozen and calls are no more routed to the main"（p152）
> "Warning: AS FOR GSM NOMADIC MODE, SIP NOMADIC REQUIRE A POOL OF Z GHOST DEVICES."（p158）
> "Warning: DON'T FORGET TO VALIDATE BOTH FEATURES IN THE USERS' CLASS OF SERVICE."（p153）

出处：OPENXTE225EN p151-161, p204。

## I — 自述

OTC PC 远程办公两条路并存，按"要不要保留主话机"选：

| 维度 | 模式 A：multi-devices 副设备 | 模式 B：Nomadic SIP（老法仍在） |
|---|---|---|
| 原理 | 给用户加一个 SIP 分机（实验口径 213100x）做副设备 | 用户把当前话机从 Deskphone 切到 Personal Computer，主设备冻结、SIP 软话机顶替 |
| 主话机 | 保留，主副同振规则由 COS 支配 | 冻结，退出游牧才恢复 |
| 资源占用 | 一个副设备号 | 每并发连接占 1 个 SIP 设备 + 1 个 Ghost Z（池化、退出才释放） |
| 前提 | COS 振铃参数 + 两个功能前缀并授权 + 申报 DM | Ghost Z 池 + SIP 设备池 + Nomadic SIP/Desktop 双许可 |

模式 A 前提三项（p152-153）：

1. COS 里把 "Ring all Secondary if Main Out of Service" 设 Yes
2. Translator/Prefix Plan 建两个前缀：Twinset get call（Local features，实验口径 506）与 No ringing（Set features，实验口径 507）
3. 两个特性必须在用户的 Class of Service 里 Validate——漏掉是"建了但不工作"的高频根因

模式 B 资源公式（p157-158）：并发游牧连接数 = 所需 SIP 设备数 = 所需 Ghost Z set 数；先统计同时游牧的用户数再建池。两模式都要求 OT 侧申报 DM（设备管理服务器，本书即 OmniVista 8770，端口 8080），OTC PC 从它取 SIP 文件。

SIP 设备默认口令 0000，必须改成强值（书中建议与分机号一致）；OT 侧 OXE SIP Subscriber 里填的口令要与 OXE 侧一致，两边不一致是最直接的注册失败原因。

## A1 — 书中案例

模式 A 配置主线（p151-156，实验口径号码见 book/overview）：

1. 8770 的 Phone feature COS 里给目标用户 COS 开 Ring all Secondary=Yes
2. Prefix Plan 建前缀 506（Twinset Get Call）与 507（No ringing）
3. 在用户 COS 里 Validate 这两个特性
4. OT 侧 /Eco system/IT server/ 建 Device management server（FQDN 指向 8770，端口默认 8080）
5. Users 应用选有 NOE 主话机的用户，右键 Add a secondary set：号段 213100x、类型 SIP extension
6. 右键 Associate SIP device 新建 OTC PC：SIP URI 填 分机号@OT 服务器 FQDN
7. Security 页签配 SBC：地址填 OTSBC 公共 FQDN、端口 5261、协议 TLS、级别 Encrypted only

模式 B 配置主线（p157-161）：

1. OXE 建 Ghost Z 池（Set Type=Analog + Ghost Z 特性选 Nomadic）
2. OT 侧 OXE Resources 申报 Ghost Z 号段两端
3. OXE 建 SIP 设备池并把默认口令 0000 改为强值
4. OT 侧 OXE SIP Subscriber 逐台申报（口令与 OXE 侧一致、Security 页签选 SBC WAN）
5. 用户 licenses 页签勾 Nomadic SIP 与 Desktop 两项
6. 把当前话机从 Deskphone 切到 Personal Computer，Test the solution

## A2 — 未来触发

使用情境：员工在家用 PC 接听且保留办公桌话机；"只有电脑没有话机"的临时坐席；游牧用户反馈切不到 Personal Computer；游牧上线前的池容量评审；副设备建了不振铃。

语言信号：multi-devices / 副设备 / secondary device / 213100x / Nomadic / 游牧 / Ghost Z / SIP 设备 / 池 / Deskphone / Personal Computer / Twinset get call / No ringing / COS / 506 / 507 / Desktop 许可。

与相邻能力区分：

- 客户端怎么填 URL 与路由档案 → 客户端接入能力
- 手机端配置 → 智能手机配置能力
- 拨测验证 → 实验环境与拨测能力

## E — 可执行步骤

输入契约：模式选型（主话机是否保留）、并发游牧人数（模式 B）、COS 与前缀规划、SBC 申报（已部署 OTSBC）。

1. 选模式：主话机保留且要同振 → 模式 A；临时顶替主话机 → 模式 B。完成标准：选型带资源口径
2. 模式 A：按 COS、前缀、COS 授权三前提逐项落地。完成标准：两项特性在用户 COS 显示已授权
3. 模式 A：申报 DM 后创建副设备（213100x）并关联 OTC PC（SIP URI+SBC 五参数）。完成标准：Device 页签出现关联
4. 模式 B：按公式建池——池大小=并发游牧数（Ghost Z 与 SIP 设备两池同数）。完成标准：池号段在 OT 侧申报且两端一致
5. 模式 B：改 SIP 设备默认口令 0000 为强值，OT/OXE 两侧口令对齐。完成标准：注册核验通过
6. 模式 B：给用户勾 Nomadic SIP 与 Desktop 双许可。完成标准：licenses 页签两项同时启用
7. 行为验证：按拨测预期表互拨核对（转实验环境与拨测能力）；模式 B 执行切换测试

判停点：

- 副设备"建了但不工作" → 停，先查用户 COS 是否 Validate 两特性（n12）
- 游牧请求失败 → 停，查池是否耗尽与双许可是否齐（n13/n15）；池空后果细节书内未描述（needs-review nr-06）
- 客户问池建多大合适但给不出并发数 → 停，公式输入缺失，先做并发统计再定池（n30 无算例）

输出契约：可用的 OTC PC 远程形态（模式 A 副设备或模式 B 游牧）+ 前提核验记录 + 池容量与许可台账。

## B — 边界

- 池容量按并发规划是书中唯一容量规则，无算例；CAC/带宽等数值书内缺位（n30/nr-07）
- SIP 设备口令默认 0000 必须改（n14）；具体环境值见 book/overview
- 模式 A 的可编程键（用 506/507 前缀）为后续动作，实验仅建前缀；前缀号可自选空闲号码
- 两模式可并存于同一系统；模式 B 的 DAS 联动（N 规则）在 OT 服务器侧设置能力
- 实验口径：2 个虚拟 Z + 2 个 SIP 设备的池仅教学规模，生产按并发统计替换
