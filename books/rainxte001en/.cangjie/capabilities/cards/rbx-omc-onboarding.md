# OMC 安装首次连接与 IP 规划修改（OXO 侧交付准备）

## R — 原文依据

> "Make a connection to the system with OMC in Expert mode with server authentication ... Enter the default installer password pbxk1064 only used for the first connection"（p74）
> "In order to avoid displaying the security alert at each connection, you must install the certificate the 1st time."（p75）
> "The passwords must be different for each customer!"（p77）
> "Restart OXO connect"（p80）

出处：RAINXTE001EN p69-82。

## I — 自述

PBX 侧一切配置从 OMC 开始，两条线：

**线一：安装与首连（四步）**

1. **装软件**：解压 → setup.exe（管理员身份）→ 语言/目录/国家分销渠道/目标产品/显示语言
2. **首连**：Expert 菜单 → LAN/WAN → 出厂 IP 192.168.92.246（实验口径）→ 勾 Server authentication → 一次性首连密码 pbxk1064
3. **装证书**：View certificate → Install certificate → 存入 Trusted Root Certification Authorities——之后不再弹告警
4. **收尾**：各账户改密（每客户必须不同）→ 录客户信息（带 * 必填）→ 右下角图标显示已连接

**线二：IP 规划修改（改完必须重启）**

- 路径：OMC → Hardware and limits → Lan/IP configuration
- 四页签：Boards 填 Main CPU 地址；LAN 填掩码与默认网关；DNS 填 DNS1/DNS2；DHCP 定话机地址池
- 客户端 PC 同步改静态地址；生效后用新地址重连

## A1 — 书中案例

**OMC 安装实验**（p69-78，厂商实验）：

1. RLAB 虚机 OXOC_PC_CLIENT 桌面 SOFTS OXO CONNECT 目录安装
2. 首连 192.168.92.246 + pbxk1064（实验口径）
3. 证书入受信任根后告警不再出现
4. 按讲师给定值改密（实验口径），录客户信息
5. 右下角图标确认连接

**IP 修改实验**（p79-82）。实验口径参数表：

| 参数 | OXO Connect | 客户端 PC |
|---|---|---|
| IP | 192.168.1.246 | 192.168.1.10 |
| 掩码 | 255.255.255.0 | 255.255.255.0 |
| 网关 | 192.168.1.254 | 192.168.1.254 |
| DNS1 / DNS2 | .250 / 10.20.30.250 | .250 / 10.20.30.250 |
| 话机 DHCP 池 | 192.168.1.30-39 | — |

生效验证：重启 OXO 后，PC 改用 RDP 重连成功即为生效。

## A2 — 未来触发

使用情境：新设备首次管理；重装 OMC；每次连接弹证书告警；pbxk1064 是什么；客户换网段后 OXO 重新规划 IP；改完 IP 连不上。

语言信号：装 OMC / 首次连接 / pbxk1064 / security alert / 证书 / Expert mode / 改 IP / Lan/IP configuration / DHCP 池 / 重启。

与相邻能力区分：连上之后接入 Rainbow → PBX 接入能力；本能力到"OMC 可用 + IP 规划到位"为止。

## E — 可执行步骤

输入契约：管理 PC（Windows）、设备管理地址、首连密码（出厂设备为 pbxk1064，已交付设备向客户档案索取）。缺首连密码且被改过 → 判停，不要试错。

1. 安装：解压 → setup.exe（管理员）→ 逐项选择 → Finish。完成标准：OMC 可启动
2. 首连：Expert → LAN/WAN → IP + Server authentication + 首连密码。完成标准：进入系统或弹证书告警
3. 证书：View certificate → Install certificate → Trusted Root → Finish。完成标准：重连不再告警
4. 改密：逐账户设置新密码（每客户唯一）。完成标准：无默认密码残留
5. 客户信息：带 * 必填项录入。完成标准：右下角已连接图标
6. IP 修改：四页签依次填写 → OK → 重启 OXO。完成标准：新地址可连、旧地址失效
7. PC 改址：静态五项（IP/掩码/网关/DNS1/DNS2）。完成标准：ping 通 OXO 新地址

判停点：

- 首连密码未知（已被改且无人知道）→ 走设备密码重置流程（原书未覆盖），不要反复试错
- IP 改完"连不上" → 先确认自己是否还在用旧地址/旧会话（n11），不要回滚设备
- OMC 装不上 → 先核对软件版本与系统版本兼容性（原书未给矩阵）

输出契约：可用的 OMC 管理会话 + 已改密账户清单 + 新 IP 规划表（设备/PC/DHCP 池）。

## B — 边界

- pbxk1064 是出厂一次性首连密码；生产设备首连时必须已更换——不得把教材默认值写到生产
- 原书全程内网明文管理口径；生产的管理访问加密与隔离不在原书范围
- 实验 IP（192.168.1.x 全套）为 RLAB 口径，生产按客户网段整体替换
- OMC 版本与设备软件版本的兼容矩阵原书未提
