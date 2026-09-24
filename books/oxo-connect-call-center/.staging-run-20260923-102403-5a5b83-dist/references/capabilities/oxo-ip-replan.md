# OXO 与客户端 IP 规划修改（OXO Connect）

## R — 原文依据

> "OMC/ Hardware and limits/ Lan/IP configuration ... enter a value for the Main CPU: 192.168.1.246"（p66）
> "In the DHCP tab, define the IP addresses range for deskphones: Start: 192.168.1. 10 End: 192.168.1. 39"（p67）
> "Click OK & Re-start the OXO Connect"（p67）

出处：OXOCXTE107EN p65-68。

## I — 自述

交付到客户现场的第一步是把设备从出厂网段挪进客户网段。顺序敏感：先改 OXO 侧再改 PC 侧。OXO 侧在 OMC/Hardware and limits/Lan/IP configuration 下分四个页签：Boards 填主 CPU 地址；LAN Configuration 填默认网关与掩码；DNS 填 DNS1/DNS2；DHCP 填话机地址池。全部改完 OK 并**重启 OXO**。之后改客户端 PC 的 IP（同网段、同网关），改完即可用远程桌面（RDP）连客户端虚机管理。

## A1 — 书中案例

**IP 修改实验**（p65-68，厂商实验）：出厂 192.168.92.246 改到实验网段——OXO 主 CPU 192.168.1.246、掩码 255.255.255.0、网关/DNS1 192.168.1.254、DNS2 10.20.30.254、话机 DHCP 池 192.168.1.10-39；客户端 PC 改 192.168.1.100；重启后 RDP 连接验证成功。

## A2 — 未来触发

使用情境：客户网段接入；管理地址与现网冲突；话机 DHCP 池规划。
语言信号：改 IP / 换网段 / Main CPU 地址 / DHCP 池 / 网关 / IP settings / re-address。

与相邻能力区分：首次用 OMC 连设备 → OMC 首连能力；本能力假设已有 OMC 管理会话。

## E — 可执行步骤

输入契约：目标网段规划（OXO 地址/掩码/网关/DNS/DHCP 池范围/PC 地址）。缺规划先与客户网络侧确认，不要占用客户在用地址。

1. OMC / Hardware and limits / Lan/IP configuration → Boards tab：Main CPU 填新地址。完成标准：值已填。
2. LAN Configuration tab：默认网关 + 掩码。完成标准：与规划一致。
3. DNS tab：DNS1/DNS2。完成标准：与规划一致。
4. DHCP tab：话机地址池起止。完成标准：池范围不与静态地址冲突。
5. OK → 重启 OXO Connect。完成标准：设备重启完成（漏重启 = 不生效）。
6. 客户端 PC：改 IP/掩码/网关/DNS 与 OXO 同网段。完成标准：ping 通 OXO 新地址；RDP 可连客户端。

判停点：改完 OXO 侧重启后 OMC 连不上 → 检查管理 PC 是否已切到新网段（先改 PC 再重启 OXO 会失联，需按新网段重新接入）。

输出契约：变更前后的地址表 + 验证结果。

## B — 边界

- 先 OXO 后 PC 的顺序来自教材实验流；实际顺序以"保持管理通路"为准，两处都要改。
- VLAN/路由/防火墙等客户侧网络调整不在原书范围（阶段 0 批判：网络前提被默认成立）。
- 教材网段（192.168.1.x）为实验值；与客户拨号计划或既有地址冲突需先重新规划。
