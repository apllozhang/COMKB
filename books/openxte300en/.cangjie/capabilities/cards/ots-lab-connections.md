# 实验 POD 与系统连接通道（RLAB、三通道、SUSE 界面）

## R — 原文依据

> "Telnet is not authorized on the OpenTouch server. You have to establish a SSH V2 connection using Putty"（p113）
> "Telnet is authorized on the OXE server. ... We are using here Telnet connection because security is not activated on the OXE in our topology."（p117）
> "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data center."（p12）
> "Product : OpenTouch™ Multimedia Services 2.6.1 Version : 18.0.100.003"（p115）

出处：OPENXTE300EN p10-37, p109-127。

## I — 自述

实验环境两形态：Fully Virtualized（RLAB 专用，无教室设备）与 Hybrid mode（RLAB 加教室话机与 POE 交换机）。POD 之间相互独立、配置相同，共享公共资源区（NAS 软件/许可、SIP 运营商模拟器、外部 DNS/NTP）。

四台系统的连接通道与账号（实验口径，完整表见 book/overview）：

| 系统 | 通道 | 要点 |
|---|---|---|
| OT | SSH v2（Putty，22 端口，UTF-8） | 维护账号登录；横幅显示 OTMS 2.6.1 / 18.0.100.003；Telnet 不授权 |
| OXE | Telnet（23 端口；启用安全后必须换 SSH） | mtcl 维护账号；IP 核验用 ifconfig 与 netadmin |
| 8770 | 远程桌面（mstsc） | 先在系统属性开允许远程；可映射本地盘 |
| ESXi/虚机控制台 | vSphere 或浏览器 web 控制台 | vm tools 未装时按 Ctrl+Alt 退控制台 |

SUSE 图形界面（仅本地控制台，非 SSH）：root 敲 startx 起图形；桌面右键 Open in Terminal；最多 4 个 workspace（教材建议三个：终端、/opt/Alcatel-Lucent、/var/data/licenses）；YaST 管时区键盘日期；Log Off 退出。

ITSP1 模拟器外呼验证：OXE 侧按 POD 号配外部 SIP 网关注册名与 DID 翻译（首外线 33210N41000、首内线 31000、跨度 500），拨模拟运营商公共号码确认出局通路。

## A1 — 书中案例

**POD 初始化实验**（p31-37）：

1. Rlab 门户用 Start 按钮启动 POD 内各虚机。
2. 核 Rack 与 Virtual GD4 参数（地址与 MAC 按实验表）。
3. PC Client 安装 IPDSP，TFTP 服务器填 OXE 主地址。
4. 按 POD 号改外部 SIP 网关注册名与外呼用户名。
5. 建 DID 翻译：首外线号、首内线 31000、跨度 500。
6. 拨模拟运营商公共号码验证外呼通路。

**系统连接实验**（p109-127）：

1. Putty 建 SSH 会话连 OT：22 端口、SSH2、UTF-8。
2. 用维护账号登录，横幅核对产品与版本号。
3. OXE 控制台核地址后用 Telnet 连接（实验拓扑未启安全）。
4. 8770 开允许远程后用 mstsc 连接并映射本地盘。
5. SUSE 控制台 root 敲 startx，布三个工作区。
6. YaST 核对时区与键盘设置后注销。

## A2 — 未来触发

使用情境：实验环境起不来；连不上某台服务器；模拟外呼不通；想知道教材里某台机器的地址或账号。

语言信号：RLAB / POD / ITSP1 / 模拟外呼 / SSH / Telnet / Putty / 远程桌面 / mstsc / 控制台 / SUSE / startx / YaST / workspace / 版本横幅。

与相邻能力区分：生产部署装机 → SOT 装机路由卡；生产远程接入安全 → 证书路由卡与 TC 文档；实验值一律不当生产配置，生产参数另出设计。

## E — 可执行步骤

输入契约：RLAB 门户账号与 POD 号；教材实验参数表（book/overview 实验环境区）；Putty/mstsc 等客户端工具。

1. 起 POD 并核对虚机清单。完成标准：各虚机在线
2. 配 IPDSP 与 DID 翻译。完成标准：模拟外呼打通
3. 三通道连接验证（SSH/Telnet/RDP）。完成标准：四台系统可达可管

判停点：

- OT 想走 Telnet → 不授权，必须 SSH v2（p113）
- OXE 已启用安全还用 Telnet → 必须换 SSH，Telnet 是实验未启安全的产物（n08）
- 实验值报障 → 全部账号口令是公开教学值，先核对是否抄错行
- 示例输出对不上 → 工具输出里的 151.1.1.x/172.25.x 是历史演示值，非本 POD（n42）

输出契约：可用的实验 POD（外呼通、四系统可达）+ 连接参数核对记录。

## B — 边界

- 全部实验 IP/口令/号码为 RLAB 教学公开值（letacla 系、superuser、Superuser01*、mtcl、adfexc、adminsnmp 等），严禁用于生产（n09）；生产交付必须全部替换并纳入口令管理。
- POD 网段、实例参数与号码口径的完整表集中在 book/overview.md 实验环境区，能力卡正文不携带。
- ITSP1 为教学专用基础设施；ITSP2 仅在拓扑图出现无细节（f05）。
- 版本横幅口径：OTMS 2.6.1 / Version 18.0.100.003（p115），跨版本环境以现场横幅为准。
