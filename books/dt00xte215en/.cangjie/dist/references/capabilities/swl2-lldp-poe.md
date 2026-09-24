# LLDP/LLDP-MED 与 PoE 管理（语音 VLAN、供电等级、优先级）

## R — 原文依据

> "IEEE 802.1AB – Link Layer Discovery Protocol (LLDP) ... Enabled by default on the OmniSwitches"（p488）
> "LLDP is configured at port level (or NI or chassis), but not at linkagg level."（p502）
> "Power available at the PD 12.95 W 25.50 W 51 W 71 W Maximum power delivered by the EPS 15.40 W 30.0 W 60 W 100 W"（p513）
> "Fast PoE : 2X60, 6360, 6860E, 6860N, 6865, 6870 • Note: OS6360 – P10A does not support FPoE"（p510）
> "<num> - specific delay value in seconds in multiples of 5. Value should be within 120 to 600 seconds"（p520）

出处：DT00XTE215EN p486-505, p506-521。

## I — 自述

终端接入的两个配套域：发现协议给话机"指路"，供电管理保终端"有电"。

1. **LLDP 基础**（p488/p502/p504）：IEEE 802.1AB，默认收发双开、30 秒发送间隔、TTL 保持倍乘 4（邻居信息存活 120 秒）；配置层级为端口/槽/机箱，不支持 linkagg 级；TLV 管理（system-name/description/capabilities/management-address）丰富邻居数据库
2. **LLDP-MED 四扩展**（p494-499）：网络策略（按应用类型下发 VLAN+l2-priority+dscp）、位置 ID（紧急呼叫）、扩展供电（PSE/PD/优先级/功率）、资产清单
3. **话机自动入语音 VLAN**（p496）：lldp network-policy <id> application voice vlan <vid> l2-priority <p> dscp <d>，chassis med network-policy 挂接，端口使能 med TLV
4. **动态入网**：配合 unp mobile-tag + unp classification lldp med-endpoint ip-phone，话机口动态落语音 VLAN
5. **PoE 供电四档**（p513，见下表）；端口 LED 琥珀=已供电、绿=已连接未供电
6. **PoE 管理**（p516-520）：lanpower port power（mW）、slot maxpower（W）、show lanpower 看余量与实耗；优先级 low（默认）/high/critical 定断电顺序，priority-disconnect 管预算不足准入
7. **特殊特性**：Fast PoE（上电即供）与 Perpetual PoE（重启不断电）需型号线支持并升级 FPGA/CPLD；delayed-start 延迟 120-600 秒（5 的倍数）且与 FPoE/PPoE 互斥、必须 write memory

**PoE 供电等级**（p513）：

| 标准 | PD 可用 | PSE 最大 | 最大电流 | 功率级 | 线缆 |
|---|---|---|---|---|---|
| 802.3af（Type 1） | 12.95 W | 15.4 W | 350 mA | 3 级（1-3） | Cat3/Cat5 |
| 802.3at Type 2（PoE+） | 25.5 W | 30 W | 600 mA | 4 级（1-4） | Cat5 |
| 802.3bt Type 3（4PPoE） | 51 W | 60 W | 600 mA/对 | 6 级（1-6） | Cat5 |
| 802.3bt Type 4（4PPoE） | 71 W | 100 W | 960 mA/对 | 8 级（1-8） | Cat5 |

## A1 — 书中案例

**LLDP 实验**（p501-505，How-To）：

1. 三台交换机对全部互联口 lldp port <口> notification enable
2. 各互联口 lldp port tlv management port-description enable
3. 6870-A show lldp statistics：各口 Tx/Rx 计数增长、零错误
4. show lldp remote-system：此时对端 System Name 仍为 (null)
5. show lldp local-system：本机系统名、发送间隔 30 秒/TTL 倍乘 4 等参数
6. 丰富化：lldp chassis tlv management system-name/description/capabilities/management-address enable
7. 复查 remote-system：系统名（Pod20sw7 等）、型号版本描述、管理 IP 出现（前后对比）

PoE 章为纯讲义无实验（p506-521）；OST 的 PoE 向导（一键修复不启动的设备）属工具能力，见资产与装机工具卡。

## A2 — 未来触发

使用情境：IP 话机自动进语音 VLAN；话机流量 QoS 标记下发；AP/话机/摄像头供电规划；PoE 预算不足断谁；交换机重启摄像头不能断电；邻居设备盘点。

语言信号：LLDP / LLDP-MED / network-policy / 语音 VLAN / voice vlan / l2-priority / dscp / mobile tag / 邻居 / TLV / PoE / 供电 / 预算 / lanpower / Fast PoE / Perpetual PoE / 优先级 critical / delayed-start。

与相邻能力区分：

- 话机流量标记的交换机侧策略（auto-QoS 按 MAC 优先级 5）：QoS 与 ACL 策略能力卡
- mobile-tag 动态入 VLAN 的 UNP 机制：VLAN 与路由、Access Guardian 能力卡
- OST 里看 PoE：资产与装机工具能力卡

## E — 可执行步骤

输入契约：话机/AP 型号与功率、语音 VLAN 编号与 QoS 规划值、交换机 PoE 预算与端口清单。语音标记取值按企业 QoS 规划（nr-02，勿照抄教材）。

1. 邻居基线：LLDP 默认双开，直接 show lldp remote-system 确认拓扑可见。完成标准：邻居数据库成型
2. 丰富化 TLV：按需 enable system-name/description/management-address 等并配 notification。完成标准：远端信息可读、变化有 trap
3. 语音策略：lldp network-policy（application voice + vlan + l2-priority + dscp，取值按企业规划）挂 chassis 与端口。完成标准：话机取到语音 VLAN 并按规划打标
4. 动态入网（按需）：unp profile mobile-tag + unp classification lldp med-endpoint ip-phone。完成标准：话机口动态落 VLAN
5. 供电规划：show lanpower 核对预算与余量；按设备等级与业务重要性设端口优先级（low/high/critical）。完成标准：断电顺序明确
6. 特性启用（按需）：FPoE/PPoE 核对型号线与 FPGA/CPLD 前提；delayed-start 核对 120-600 秒、互斥与 write memory 要求。完成标准：供电策略落地且固化

判停点：

- LLDP 配到 linkagg 上 → 不生效，逐物理口配置
- 话机标记值照抄教材 → 教材两页不一致（nr-02），按企业 QoS 规划定值并 show lldp config 核查
- OS6360-P10A 承诺 FPoE/PPoE → 不支持（p510-511），选型阶段拦下
- 同机柜要 delayed-start 又要 FPoE/PPoE → 互斥，二选一
- 预算核查对不上 → 每型号 PoE 预算查 specification guide/datasheet，本卡不承诺具体预算值

输出契约：话机自动入语音 VLAN 且标记合规 + PoE 预算与断电顺序方案 + 邻居可视化的 TLV 配置。

## B — 边界

- LLDP-MED 两页示例数值不一致（p496: 5/46 与 p499: 7/14）按 nr-02 处置：不编造统一值
- LLDP 运行参数（30 秒/TTL×4 等）取自 8.7.98.R03 截图口径（p504，nr-08），随版本可能漂移
- Fast/Perpetual PoE 支持线：2X60/6360/6860E/6860N/6865/6870，且需先升级 FPGA/CPLD（按 release note）
- EEE（802.3az）节能仅铜口 100/1000M，U 型光口机型不支持（p512）
- PoE 端口单位是 mW、槽单位是 W，混用会差三个数量级（p516）
- 位置 ID（紧急呼叫）与资产清单 TLV 本卡仅点到，落地细节查 Network Configuration Guide
