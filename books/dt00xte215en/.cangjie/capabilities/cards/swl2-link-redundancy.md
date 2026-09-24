# 链路与生成树冗余（LACP 聚合、STP/1x1、DHL Active-Active）

## R — 原文依据

> "Static • Port parameters MUST be exactly the same at both ends and within the group ... Only works between Alcatel-Lucent OmniSwitches • Dynamic • IEEE 802.3ad LACP"（p273）
> "Switch Default Hashing Mode 9900 extended 6900 brief 6870 extended 6860 extended 6865 extended 6560 extended 6465 brief 6360 brief"（p280）
> "STP (802.1d): Convergence time : 50 secs • RSTP (802.1w): Convergence time : < 1 sec • MSTP (802.1s): < 1 sec"（p300）
> "DHL Active-Active splits VLANs between two active links • The forwarding status of each VLAN is modified by DHL to prevent network loops"（p326）

出处：DT00XTE215EN p270-290, p298-344。

## I — 自述

环路避免与链路冗余的三件套，选型互斥要分清：

1. **链路聚合两型**：静态（两端与组内参数完全一致、仅 ALE 设备间可用）与动态 LACP（LACPDU 协商、可接服务器/存储）；组内端口必须同速率；聚合可静态划入任意 VLAN 并跑 802.1Q
2. **负载分担**：hash-control brief（仅源/目的 IP）或 extended（含 UDP/TCP 端口）；出厂默认逐型号不同（见下表）；组播默认只走聚合主端口，要参与分担须显式启用 non-ucast
3. **STP**：模式两种——flat（每交换机一实例）与 per-VLAN/1x1（每 VLAN 一实例，OmniSwitch 默认，可按 VLAN 调优先级做负载分担）；默认桥优先级 32768，全默认时最小 MAC 当根桥；保护三件 restricted-role/restricted-tcn/用户口 BPDU 过滤
4. **DHL Active-Active**：每交换机 1 会话、LinkA/LinkB 两链（物理口或聚合）；一组 VLAN 同打标在两链、vlan-map linkb 指定 LinkB 服务集；故障 VLAN 全量切换，恢复等 pre-emption（0-600 秒，默认 30 秒）；DHL 端口自动禁 STP，不支持 mobile/802.1x/GVRP/UNI 口
5. **三方案定位**（p330）：STP 牺牲一半带宽（阻塞侧）；LACP 与 DHL 全带宽双活；DHL 不做交换机级冗余

**hash 出厂默认**（p280）：

| 型号 | 默认 hash |
|---|---|
| OS9900 / OS6870 / OS6860 / OS6865 / OS6560 | extended |
| OS6900 / OS6465 / OS6360 | brief |

**STP 路径成本两套**（p301）：

| 链路速率 | 16 位（STP/RSTP） | 32 位（MSTP） |
|---|---|---|
| 10 Mbps | 100 | 2,000,000 |
| 100 Mbps | 19 | 200,000 |
| 1 Gbps | 4 | 20,000 |
| 10 Gbps | 2 | 2,000 |

path-cost-mode auto：16 位随 STP/RSTP、32 位随 MSTP；32bit=无论何协议一律 32 位（p309）。

## A1 — 书中案例

**聚合实验**（p283-290）：两侧 linkagg lacp agg 7 size 2 actor admin-key 7 并挂成员口，换默认 VLAN 57 后 Client 持续 ping，disable 一个成员口 ping 不断、恢复后回到 2/2（LACP 冗余生效）。

**STP 实验**（p313-323）：

1. 6870-A 上 spantree vlan 20/30 priority 20000 指定根桥，show 确认 0x4E20
2. show spantree vlan 20 ports 看角色 DESG/ROOT/ALT 与 FORW/BLK；每条链路只有一侧 BLK 属正常
3. Client 持续 ping，disable 聚合模拟断链：Topology Changes 增加，原 ALT 口转 FORW
4. 恢复后 1x1 负载分担：VLAN 20 根在 6870-A、VLAN 30 根在 6860-B，两 VLAN 阻塞口互补分居不同上行

**DHL 实验**（p336-344）：

1. 先清成员口上残留 VLAN 配置再入聚合（报错 "Port cannot be added to Linkagg" 的解法）
2. dhl 1 建 LinkA=聚合 7、LinkB=聚合 8，dhl 1 vlan-map linkb 30，enable
3. show dhl 1：LinkA 服务 VLAN 20/57、LinkB 服务 VLAN 30，dhl-blocking/forwarding 互补
4. 断 LinkA：VLAN 20 立即切到聚合 8；恢复后等约 30 秒（默认抢占）才回切

## A2 — 未来触发

使用情境：两条上行做聚合与分担优化；接服务器/存储的聚合对接；指定根桥与 1x1 负载分担；断链收敛验证；双上行不跑 STP 要双活；组播流量挤满单口。

语言信号：linkagg / LACP / actor admin-key / hash-control / 负载分担 / STP / RSTP / 根桥 / bridge priority / ALT / blocking / 1x1 / per-VLAN / DHL / vlan-map / 抢占 / pre-emption / 双活。

与相邻能力区分：

- 端口无法加入聚合（残留配置清理）的前置动作：属本卡 B 段
- VLAN 成员与网关配置：VLAN 与路由能力卡
- 组播协议本身（PIM 等）：超本书范围

## E — 可执行步骤

输入契约：上行链路清单与速率、对接设备类型（ALE 交换机或服务器/存储）、环避免方案选型（STP 或 DHL，二选一）、负载分担目标。方案混用同一链路 → 判停。

1. 聚合选型：ALE 互联可静态；接服务器/存储/异构一律 LACP。完成标准：两端参数一致的聚合规划
2. 配置聚合：两侧建 agg（编号/size/admin-key）并挂成员口；端口残留 VLAN 配置先逐条清理。完成标准：show linkagg UP 且 Selected/Attached 达标
3. 分担调优：核出厂 hash 默认（6360 等 brief），按流量特征切 extended 或加 non-ucast。完成标准：分担口径明确
4. STP 规划：默认 per-VLAN 模式；按角色显式指定根桥优先级（勿留 32768 让最小 MAC 决定）。完成标准：show spantree 根桥符合设计
5. 1x1 负载分担：不同 VLAN 设不同根桥，验证两 VLAN 阻塞口互补分居不同上行。完成标准：双上行均有转发流量
6. 冗余测试：持续 ping 中断一条链路/成员口，记录丢包与恢复；DHL 场景验证 30 秒抢占回切。完成标准：切换行为可接受并记录

判停点：

- 端口报 "cannot be added to Linkagg" → 先 show vlan members port 清残留配置，不要强加
- 两侧同时 blocking → 异常，检查根桥与路径成本，正常每链路仅一侧 BLK
- DHL 端口要跑 STP 双保险 → 不支持（自动禁用），二选一
- 接入 DHL 的口要跑 802.1x/mobile/GVRP/UNI → 不支持，改回 STP 方案或换口
- 频繁闪断链路 → 调大 DHL pre-emption（0-600 秒）防来回摆动，别把"恢复立即回切"写进验收

输出契约：冗余上行（聚合或 DHL）+ 无环且双活的生成树状态 + 冗余测试记录。

## B — 边界

- 静态聚合仅限 ALE OmniSwitch 互联；对接服务器团队默认按 LACP 设计（p273）
- 组播默认只走聚合主端口；不开 non-ucast 时聚合只分担单播（p281）
- 任何物理变更都会触发 STP 重收敛（Topology Changes 上涨、Age 重置），变更窗口要预估抖动（p319）
- 教材对"阻塞侧判定/二层还是三层"等思考题留白，本卡答案（成本→桥 ID→端口 ID 逐级比较）为推断口径（nr-05）
- STP 收敛时间（50 秒/<1 秒）为协议口径；各型号支持集查 Specification Guide（p301）
- DHL 无交换机级冗余；交换机级高可用走 VC 或 VRRP（见对应能力卡）
