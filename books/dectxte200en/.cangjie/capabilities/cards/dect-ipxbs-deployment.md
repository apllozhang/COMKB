# 8378 IP-xBS 部署与故障换站（全局参数/DHCP/注册/换站保 RPN）

## R — 原文依据

> "IP-xBS IP configuration •Dynamic •Static ... IP-xBS firmware update •TFTP server •Manual update ... IP-xBS registration •MAC @ in the OXE Database"（p125）
> "A new Vendor Class for the xBS: Vendor id: alcatel.ipxbs.0"（p146）
> "Registration enabled YES ... Can be set to True only in one node of a network."（p147）
> "The manual registration is recommended when replacing a broken base station by a new one (with a new MAC@) When using the automatic registration, the first free RPN will be used and it can be different. This could be problematic if alarming and geo localization is used."（p150）

出处：DECTXTE200EN p125-151, p143-148。

## I — 自述

IP-xBS 开通四步主流程，极简部署 = 1 PARI/1 位置区/1 Site/1 簇（p140）：

1. **IP 配置**：动态走 DHCP——内部 DHCP 为 xBS 新增 vendor class（alcatel.ipxbs.0），下发 IP/掩码/网关/TFTP/DNS；或静态手工配。仅 PoE Class 2 供电、仅单播。
2. **固件更新**：TFTP 自动后台下载或 WBM 手动更新（固件管理细节在固件管理能力）。
3. **注册**：OXE 录 MAC@ 后基站注册入库并自动分配 RPN；注册开关（Registration enabled）全网只能一个节点为 YES，防误收编；Default PARI/Default location area 可设 auto(255) 取首个空闲。
4. **核验与时间**：dectview xbs 看两行 OK；NTP 时间由 OXE 经 UA 信令下发（UTC+夏令时规则）。

关键规则：

- WBM（HTTPS，engineer 口径）首次默认解锁、口令可由 OXE 下发；WBM 改动可被 PBX 下发覆盖；非日常运维必需
- 无法取 IP 时按 Reset 键 6-10 秒回出厂，用出厂地址 http://192.168.0.2 访问（p78）
- 换故障基站走**手动注册**（删旧 MAC@ → 录新 MAC@ → 保留位置名）以保持 RPN——自动注册会让 RPN 漂移，告警与地理定位失准

## A1 — 书中案例

**部署实验**（p143-148）：

1. 全局参数：Radio base type=xBS、Station Base Type=DECT Europe、PLI=31、AC System=1111（实验口径）、Security level=Authentication
2. xBS System：Number of PARI=1、Allow xBS Web Based Management=YES、WBM 口令（默认 Engineer00!/Admin00!，实验口径）
3. xBS Pari：PARI Number=0、PARI Value=100004100x4（示例）、Area type=1 area of 256 xBS
4. xBS Site：Site 0 命名 BREST（默认已存在）；xBS base station 录 Location name=GF-01、Site 0、PARI 0
5. 开注册：Registration node=1、Registration enabled=YES → 接通基站，DHCP 池 192.168.1.145-155（实验口径）取址
6. 核验：dectview xbs 输出 "Region 0 (EUROPE) has 1 site(s) with 2 XBS in service"，RPN 已分配

**换站实验**（p149-151）：拔旧站；xBS base station 页删 id 0 的 MAC@；同页录新 MAC@ 重填 GF-01；dectview xbs 两站 OK、RPN 不变。

## A2 — 未来触发

使用情境：新部署 IP-xBS；基站上不了线；注册开关怎么配；DHCP 取不到地址；换故障基站；告警定位失准怀疑 RPN 变了。

语言信号：IP-xBS / 8378 / 部署 / commissioning / DHCP / vendor class / alcatel.ipxbs.0 / MAC 地址 / 注册 / registration / RPN / 换基站 / 更换 / PoE / WBM / 192.168.0.2。

与相邻能力区分：固件批量升级见固件管理能力；PARI/PLI 字段语义见标识号码能力；部署后状态排障见维护排障（路由）；多 Site 拆分见同步拓扑能力。

## E — 可执行步骤

输入契约：OXE 版本 ≥R12.2、DHCP 可用（或静态规划）、基站 MAC@ 清单、PARI/PLI 规划值。缺 MAC@ → 从基站铭牌或 DHCP 租约取。

1. 全局参数：PWT/DECT System 配 Radio base type/Station Base Type/PLI/AC/Security level。完成标准：全局参数落库
2. 建 PARI 与 Site：xBS System / xBS Pari 与 xBS Site。完成标准：PARI Value/Area type/Site Name 就位
3. 备注册：xBS System 配 SYSLOG（可选）、WBM 口令；录入基站 MAC@ 与位置名。完成标准：基站行在库待收编
4. 通网络：PoE 接入，DHCP 按 vendor class alcatel.ipxbs.0 下发（外部 DHCP 需自行实现 vendor class 匹配）。完成标准：基站取到 IP
5. 开注册：Registration node 指定节点 + Registration enabled=YES（多节点网络只开一处）。完成标准：基站入库并分配 RPN
6. 核验：dectview xbs 看 State=OK、IP/MAC/FW 落表；WBM 核 Time server=OXE。完成标准：两行 OK、RPN 已分配

判停点：

- 基站灯不亮/取不到地址 → 查 PoE 与 DHCP vendor class，不要先动 OXE 配置
- 注册开关开了但基站不入库 → 核对注册节点是否本节点（多节点只能一处为 True），漏配 Registration node 是常见坑（p147 Notes）
- 换站后告警定位失准 → 确认是否走了自动注册导致 RPN 漂移；补救=按手动注册流程重新保 RPN 换站
- WBM 里改的参数"自己变回去" → PBX 下发覆盖所致（p77），长期变更回 OXE 数据库做

输出契约：入库基站表（MAC@/位置名/RPN）+ 注册开关状态记录 + 换站工单闭环记录。

## B — 边界

- 实验值（AC=1111、PARI=100004101x4、DHCP 池 192.168.1.145-155、WBM 口令）均为实验口径，生产必须替换并加固
- 外部 DHCP 的 vendor class 通用配置方法书内未给（只有内部 DHCP 截图）；细节指针 8AL91047ENAD
- 时间服务器可手工改（p148），但夏令时规则来自 Call Server；改 NTP 后的行为未展开
- 换站保留的是 RPN 与位置名；基站固件版本差异的处理属固件管理能力
- 极简部署外的复杂开局（多 PARI/外部同步）细节按《Getting started with the 8378 DECT IP-xBS solution on OXE》（p140 指针）
