# 三层服务与网关冗余（DHCP/UDP Relay、Loopback0、静态路由、VRRP）

## R — 原文依据

> "Two types of DHCP relay agents: global and per-interface. ... They are mutually exclusive"（p353）
> "• Not bound to any VLAN • Always remain operationally active (as long as at least one VLAN is active) ... • Automatically advertised by RIP and OSPF protocols when the interface is created (not by BGP)"（p360）
> "By default, static routes have preference over dynamic routes • Priority can be set by assigning a metric value"（p363）
> "Multicast - 224.0.0.18 Virtual MAC address: 00-00-5E-00-01-{VRID}"（p375）
> "THE VRRP INSTANCE MUST BE DISABLED BEFORE CHANGING THE PRIORITY"（p390）

出处：DT00XTE215EN p345-390。

## I — 自述

三层侧的五个基础件加一个网关冗余协议：

1. **DHCP Client**（p350-351）：任意 VLAN 单接口动态取址（RFC 2131 release/renew）；Option-1 掩码落地、Option-3 网关生成默认路由、Option-51 租期、Option-58/59 续租/重绑、Option-60 可配串；地址作 VLAN 主地址
2. **DHCP Relay**（p353-355）：全局型（ip dhcp relay destination + enable）与接口型（per-interface-mode + interface destination）互斥；默认 max hops 16、Opt82 格式 Base MAC、Relay Agent Information 与 PXE 默认关
3. **UDP Relay**：tftp/tacacs/ntp/nbns/nbdd/dns 或自定义端口按 VLAN/地址转发（p357）
4. **Loopback0**（p360）：不绑 VLAN、只要有一个 VLAN 活动就永活；RIP/OSPF 自动通告（BGP 不会）；七类用途——PIM-SM RP、sFlow Agent、RADIUS 源、NTP、BGP peering、OSPF router-id、NMS 识别；配 ip service source-ip 统一服务源
5. **静态路由**（p363-364）：默认优先于动态路由，metric 调相对优先级，可做主备默认路由（metric 1 主 / metric 2 备）；关联接口须 up
6. **VRRP**（p374-390）：虚拟 IP+虚拟 MAC 00-00-5E-00-01-{VRID}、组播 224.0.0.18；三步配置=ip vrrp interface、address <vip>、admin-state enable；默认优先级 100、默认允许抢占；跟踪策略五类（ADDRESS、IPV4/V6-INTERFACE、PORT、VLAN）做上行故障降级

**实验主备指定**（p390，实验口径）：改优先级必须 disable 实例 → priority 150 → enable；两侧各主一组 VLAN 即负载分担。

## A1 — 书中案例

**DHCP Relay 实验**（p367-371）：

1. 核查路由：show ip routes 确认到 192.168.100.0/24 的 OSPF 路由，ping DHCP 服务器通
2. 两台交换机各 ip dhcp relay destination 192.168.100.102 并 admin-state enable
3. show ip dhcp relay 核对：Enable、Max hops 16、Relay Mode Global、Opt82 Base MAC
4. 客户端改 DHCP 模式后取到对应网段地址
5. show ip dhcp relay statistics 计数增长（实验值 43/43 与 40/40，实验口径）

**VRRP 实验**（p383-390）：

1. 6870-A 与 6860-B 互补建 int_20/int_30，再各建 VRID 1/2 指向相同 VIP（192.168.20.254/30.254）
2. show ip vrrp：Version V2、Priority 100、Preempt Yes、Interval 100、虚拟 MAC 尾字节即 VRID
3. 同优先级时最低 router ID 当 master：初始 6870-A 双 Master
4. 终端网关指向 VIP，ip neigh show 看到 VRRP 虚拟 MAC；reload 主设备后 Backup 接管
5. 指定主备：6870-A 主 VLAN 20（VRID 1 priority 150）、6860-B 主 VLAN 30（VRID 2 priority 150）

## A2 — 未来触发

使用情境：用户网段跨网段取地址；多 DHCP 服务器分网段；管理/协议源地址规划；双出口主备默认路由；两台汇聚做网关冗余；VRRP 主备指定与上行跟踪。

语言信号：DHCP relay / IP helper / UDP relay / Loopback0 / source-ip / 静态路由 / metric / 默认路由 / VRRP / VRID / 虚拟 IP / 虚拟 MAC / 优先级 / 抢占 / preempt / 跟踪 / track。

与相邻能力区分：

- VLAN 网关接口 DOWN 的成因：VLAN 与路由能力卡
- RADIUS 源地址只是 Loopback0 的一个用途，认证体系本身：Access Guardian 能力卡
- OSPF/BGP 协议细节：超本书（仅 Auto-Routing 触及）

## E — 可执行步骤

输入契约：网段与 DHCP 服务器地址、中继模式选择依据、管理源地址规划、网关冗余的 VRID/VIP 与主备角色。改优先级在业务窗口内做。

1. 取址链路：DHCP Client 直接取址，或配 DHCP Relay（单服务器用全局型；分服务器才用接口型，两型互斥）。完成标准：客户端取到对应网段地址、statistics 增长
2. UDP Relay（按需）：按服务清单转发跨网段 UDP 服务。完成标准：目标服务可达
3. 管理面源地址：建 Loopback0（如 192.168.254.x/32），ip service source-ip loopback0 统一指定。完成标准：show 中服务源为 Loopback0
4. 出口路由：静态默认路由主备双条（metric 1/2）；确认关联接口 up。完成标准：show ip routes 主备有序
5. VRRP 冗余：两侧建 VRID 指向相同 VIP 并 enable；验证虚拟 MAC 出现在终端 ARP。完成标准：一主一备
6. 主备与演练：改优先级按 disable → priority → enable 三步；断主验证 Backup 接管（Become Master 计数）。完成标准：切换达标且角色符合设计

判停点：

- 全局与接口中继要并存 → 互斥，先清一侧再切另一侧
- 需要 PXE 或接入认证带 Option 82 → 默认是关的，显式打开并核对策略（Drop）
- VRRP 直接改优先级不生效 → 必须先 disable 实例；disable 本身即触发切换，安排窗口
- 超过两台做网关冗余或多组 VRID 规划 → 本卡覆盖主备与双组负载分担；更多形态以 Network Configuration Guide 为准

输出契约：跨网段取址可用的用户网段 + 管理/协议源地址方案 + 网关冗余（主备角色与切换验证记录）。

## B — 边界

- DHCP Relay 全局/接口两型互斥；接口型仅转发该接口所绑 VLAN 发起的 DHCP 包（p353）
- Loopback0 由 RIP/OSPF 自动通告但 BGP 不会；名字必须写 Loopback0（p360）
- 静态路由关联接口须 up and running，否则不生效（p363）
- VRRP 实验输出为 Version V2（p387）；RFC 2338/2787 口径
- 实验服务器地址 192.168.100.102 与 VIP 数值为实验口径，生产按客户编址
- DHCP 服务器本身、RADIUS 服务器侧、动态路由协议（OSPF/BGP）配置不在本书范围
