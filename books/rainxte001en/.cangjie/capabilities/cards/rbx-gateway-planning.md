# WebRTC 网关拓扑决策与容量规划（三拓扑对比、版本前提、选型）

## R — 原文依据

> "The WebRTC Gateway brings voice interoperability between Rainbow Clients and PBX ecosystem. • This enables an audio media relationship between Rainbow applications and devices of a PBX connected to Rainbow"（p118）
> "Type of Rainbow GW | OXO Connect (Power CPU EE) | OXO Connect evolution (IPBox) — Internal GW: Not supported / 20 calls max. ; External GW (NUC): 50 calls max. / 50 calls max. ; OCE-FE GW: 20 calls max. / Not supported"（p129）
> "50 VoIP calls maximum if the WebRTC gateway is external on Mini PC or ESXi server • 20 VoIP calls maximum with OCE integrated WebRTC gateway or if the WebRTC gateway is external on OCE Front End"（p147）
> "Maximum of OXO users with Rainbow VoIP option increased from 50 to 150"（p147）

出处：RAINXTE001EN p117-129, p146-147。

## I — 自述

网关只建"音频媒体"关系，呼叫控制始终在 PBX（p118）——排障分流的总纲。三拓扑功能等价，差异在承载硬件、容量与许可：

| 拓扑 | 承载 | 版本前提 | 通话上限 | 许可要点 |
|---|---|---|---|---|
| OCE 集成 | OCE（IPBox）内部虚拟机 | R3.2+ | 20 | 免 SIP trunk 许可（bypass）；Power CPU EE 不支持 |
| OCE Front End | 独立 IPBox 前置于呼叫服务器 | 双端 ≥R4.0 MD | 20 | 专用许可免费（FTR 自动给）；无 PBX 能力/无 UTL；仅配 Power CPU EE |
| 外部 VM/NUC | ESXi 虚拟机或迷你 PC | — | 50 | 需 SIP trunk 许可（R3.2 前唯一选择） |

**容量对照表**（p147，Rainbow VoIP 用户数 → 推荐通道数）：

| 用户数 | 外部拓扑通道 | 集成/FE 通道 |
|---|---|---|
| 5 | 5 | 5 |
| 10 | 7 | 7 |
| 20 | 11 | 11 |
| 30 | 15 | 15 |
| 50 | 20 | 20 |
| 70 | 27 | NA |
| 100 | 36 | NA |
| 150 | 50（打满上限） | NA |

- 用户上限：OXO Rainbow VoIP 用户已从 50 提到 150（两种硬件均适用）；150 仅在极低话务下成立（原书 * 注）

**终端形态规则**（p123，与拓扑无关都要做）：

| 用户形态 | 终端结构 | 版本 | 许可 |
|---|---|---|---|
| 有物理话机 | Multiset：物理主站 + Free Rainbow in Twinset 虚拟副站 | R6.0 起 | 1 UTL（副站不额外占） |
| 有物理话机（旧版） | Multiset：物理主站 + Anydevice 副站 | R5.2 及以前 | 许可口径需核 TC2479 |
| 纯软话机 | Anydevice 单终端 | — | 1 UTL |

## A1 — 书中案例

**容量决策素材**（p146-147，讲义，无实验——选型即查表）：

- 80 用户站点 → 外部拓扑、通道介于 27-36
- OCE 站点超 50 用户 → 改用/加用外部网关（原书明示扩展路径）
- 带 * 行（70/100/150）→ 20 通道下的方向性值，实际取决于话务量

**硬件适配**（p129 矩阵）：

| 站点硬件 | 可选拓扑 |
|---|---|
| Power CPU EE | 集成不可用 → 二选一：FE（20）或外部（50） |
| Evolution（IPBox） | 集成 20 可用（默认低成本项）；FE 明示 Not supported |

## A2 — 未来触发

使用情境：给客户选 WebRTC 网关方案；Power CPU EE 能不能用集成网关；最多支持多少用户/并发；通道数怎么定；FE 和外部怎么选；Twinset 和 Anydevice 怎么配。

语言信号：WebRTC 网关 / 拓扑 / 集成网关 / OCE Front End / Front-End / NUC / ESXi / 容量 / dimensioning / 通道数 / channels / 20 通话 / 50 通话 / 150 用户 / UTL / Twinset / Anydevice / Multiset。

与相邻能力区分：选型后的施工 → 网关部署能力；"能通但没声音"类排障按本卡"媒体 vs 呼控"分界先分流（媒体找部署卡，呼控找 PBX 侧）。

## E — 可执行步骤

输入契约：PBX 硬件形态（Power CPU EE 还是 Evolution/IPBox）、系统版本、Rainbow 话音用户数与话务特征、预算（SIP trunk 许可/硬件）。用户数与话务未知 → 判停先勘测。

1. 核硬件与版本：
   - Power CPU EE → 集成出局；版本 ≥R4.0 MD 可选 FE（20），否则外部（50）
   - Evolution/IPBox → 集成（R3.2+，20）为默认低成本项；需 >20 通话 → 外部（50）
   - 版本 <R4.0.020.002 → 自动配置不可用（两处原文口径差异见 nr-01），先升级
2. 定容量：查对照表得推荐通道数；校验并发上限（外部 50 / 集成与 FE 20）；>50 话音用户的 OCE 站点 → 外部拓扑。完成标准：拓扑 + 通道数成文
3. 定终端形态：有话机用户 → Multiset + Twinset 副站（R6.0+）；纯软话机 → Anydevice；核 UTL 数量（每电话用户 1 UTL）。完成标准：终端清单 + UTL 口径确认
4. 方案评审：许可（SIP trunk bypass 与否）、硬件采购（FE 需整 IPBox）、后续扩容路径。完成标准：方案过审

判停点：

- 用户数 >150 → 超出 OXO Rainbow VoIP 上限，转 OpenTouch/其他方案线（原书范围外）
- 话务量未知且用户数 >50 → 不承诺"150 也够"，按 * 注要求先做话务评估（工具与建模在书外）
- 客户要求 FE 挂 Evolution 呼叫服务器 → 组合不存在（p129 Not supported），改推荐集成或外部
- 现场只有 R5.2 且要建副站 → 按旧语义用 Anydevice 并说明升级后要换 Twinset，避免白占 UTL

输出契约：拓扑选型结论（含版本/硬件依据）+ 通道数方案 + 终端形态与 UTL 清单。

## B — 边界

- 容量表的 * 行（70/100/150）是 20 通道下的方向性指示值，实际取决于通道数与用户话务——引用数字必须带此前提（p147 原注）
- TURN 服务器配置、防火墙白名单、编号计划与闭锁：书外（安装指南/cookbook/TC2479），本卡不覆盖取值
- OCE-FE 开局有多个场景分支（新装/加装/有无 Fleet 参考），操作必须按 MyPortal 最新版 Rainbow WebRTC cookbook（p137 "essential to follow"）
- Anydevice 的版本语义（R5.2/R6.0 分界）在升级混存的系统上要逐台核对
- 网关只管音频不管呼叫控制：路由不通/打不出去属 PBX 编号计划与 ARS 域（p121 安装员保留项）
