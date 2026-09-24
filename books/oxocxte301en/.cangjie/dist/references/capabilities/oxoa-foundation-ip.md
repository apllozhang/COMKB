# 交付地基：OMC 首连与 IP 规划修改（含 IPDSP 时间前提）

## R — 原文依据

> "Make a connection to the system with OMC in Expert mode with server authentication … Enter the default installer password pbxk1064 only used for the first connection"（p28）
> "In order to avoid displaying the security alert at each connection, you must install the certificate the 1st time."（p29）
> "The passwords must be different for each customer!"（p31）
> "Change the IP settings for the OXO Connect and the PC before installing the IPDSP … An error message related to loading the lanpbx file will appear."（p14）
> "Click OK & Re-start the OXO Connect"（p35）

出处：OXOCXTE301EN p14, p23-36。

## I — 自述

PBX 侧一切配置从 OMC 开始，两条线：

**线一：安装与首连（四步）**

1. 装 OMC：解压后 setup.exe 以管理员运行，按语言/目录/国家分销渠道/目标产品/显示语言逐项选择
2. 首连：Expert 菜单 + LAN/WAN + 出厂 IP（192.168.92.246，实验口径）+ Server authentication + 一次性首连密码 pbxk1064
3. 装证书：Security Alert 里 View certificate→Install certificate→Trusted Root Certification Authorities，之后不再弹告警
4. 收尾：各账户改密（每客户必须不同）+ 客户信息（带 * 必填、首连强制）+ 右下角连接图标确认

**线二：IP 规划修改**：OMC/Hardware and limits/Lan/IP configuration 四页签（Boards 主 CPU 地址、LAN 掩码与网关、DNS1/DNS2、DHCP 池）改完点 OK 并重启 OXO；客户端 PC 同步改静态地址；生效后用新地址重连。

**IPDSP 前提**（p14）：先改 OXO 与 PC 的 IP，再把 PC 自动对时关后重开（强制 NTP 重同步），最后装 IPDSP——时间差会导致 HTTPS 证书校验失败，表象是 lanpbx 加载错误。

## A1 — 书中案例

**OMC 安装实验**（p23-32，厂商实验）：

1. RLAB 客户端虚机桌面 SOFTS OXO CONNECT 目录解压安装包（实验口径）。
2. setup.exe 管理员运行，按向导逐项选择完成安装。
3. 首连 192.168.92.246 + pbxk1064（实验口径，仅首连）。
4. 证书装入 Trusted Root 后告警不再出现。
5. 按讲师给定值改密并录入客户信息（带 * 必填）。

**IP 修改实验**（p33-36，厂商实验）：

1. 四页签依次填：Boards 192.168.1.246、掩码 255.255.255.0、网关 192.168.1.254、DNS .250/10.20.30.250（实验口径）。
2. DHCP 池 192.168.1.30-39（p34 口径；p40 检查清单写 .10-.39，见 nr-02）。
3. OK 后重启 OXO Connect。
4. PC 改静态五项同网段；生效后改用 RDP 重连验证。

## A2 — 未来触发

使用情境：新设备首次管理；重装 OMC；每次连接弹证书告警；pbxk1064 是什么；客户换网段后重新规划 IP；IPDSP 装不上报 lanpbx 错误。

语言信号：装 OMC / 首次连接 / pbxk1064 / Expert mode / 证书 / security alert / 改 IP / Lan/IP configuration / DHCP 池 / 重启 / IPDSP / lanpbx / NTP / 时间同步。

与相邻能力区分：本卡到"OMC 可用 + IP 规划到位 + 时间同步"为止；OMC 与 Rainbow 云侧的开户入门在 bundle.oxo-connect-starter（本体入门）；连上之后的 SIP 中继配置归 SIP 组网能力。

## E — 可执行步骤

输入契约：管理 PC（Windows）、设备管理地址、首连密码（出厂 pbxk1064，已交付设备向客户档案索取）、目标网段规划。缺首连密码且被改过 → 判停，走密码重置流程不要试错。

1. 安装 OMC 并启动。完成标准：OMC 可用
2. 首连：Expert+LAN/WAN+Server authentication+首连密码。完成标准：进入系统
3. 证书入 Trusted Root。完成标准：重连不再告警
4. 逐账户改密（每客户唯一）+ 客户信息必填项。完成标准：无默认密码、初始化完成
5. IP 四页签填写后重启 OXO；PC 改同网段静态地址。完成标准：新地址可达、旧地址失效
6. （装 IPDSP 前）PC 自动对时关后重开，核对时间一致再安装。完成标准：lanpbx 不报错

判停点：

- IP 改完"连不上" → 先确认自己是否还在用旧地址/旧会话，不要回滚设备
- DHCP 池规划 → 按 p34 口径自定并与 PC 静态地址错开（nr-02 两处不一致，照抄会撞段）
- 改 IP 后证书重建 → 已信任客户端要重新信任（p327），提前告知客户

输出契约：可用的 OMC 管理会话 + 新 IP 规划表（设备/PC/DHCP 池）+ 时间同步确认。

## B — 边界

- pbxk1064 是出厂一次性首连密码；生产设备必须已更换——不得把教材默认值写到生产
- 全部实验 IP/密码/账号为 RLAB 口径（192.168.1.x 全套），生产按客户网段整体替换
- OMC 版本与设备软件版本的兼容矩阵原书未提； Rainbow 云侧开户/订阅/成员操作属 starter bundle 范畴
- IPDSP 是实验用 ALE 软话机客户端，生产装机同样适用"时间先行"原则但产品形态不同
