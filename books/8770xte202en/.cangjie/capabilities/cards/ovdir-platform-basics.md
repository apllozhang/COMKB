# 8770 平台基础（套件全景、拓扑架构、版本兼容、虚拟化）

## R — 原文依据

> "Setup suite / Network suite / Reports suite / Directory suite"（p4）
> "Graphical User Interface (GUI) to manage 8770 applications • Simultaneous access to OmniVista 8770 Server"（p6）
> "HTML application to access the directory information • Anonymous access allowed"（p6）
> "Server / Config. / binaries / OXE ... MariaDB (SQL) / LDAP / OV8770 Services"（p7）
> "OXE Purple R101.0 (N3), R101.1 (N4) & R101.2 (N5) X"（p9，仅 R5.2 列有 X）

出处：8770XTE202EN p4-40。

## I — 自述

平台背景层，回答"8770 是什么、谁连谁、版本怎么配"。

- **四套件 15 应用**（厚客户端）：Setup/Server Administration（Administration/Security/Maintenance/Scheduler）；Network/PCX 管（Configuration/OXO Connect Supervision/Users/Devices/Alarms/Topology/Audit/Maintenance）；Reporting（Accounting/Traffic Analysis/Reports）；Directory（Directory + Web Directory）。本书只精讲 Directory 套件及交错的 Security/Alarms/Configuration/Administration/Scheduler
- **WBM 四应用**：Users（需 Unified Management 许可，支持管理域）、Configuration（一次只连一个 OXE，无 SSH/Telnet 直连）、Performance（仪表盘）、Manage My Phone（终端用户自管话机）
- **架构**：MariaDB+LDAP 双存储；OV8770 Services 承载 Web Directory/邮件/批量开通等；北向对接 OXE（HTTPS+LDAP(S)+CMISE+(S)FTP+Telnet/SSH）、OXO Connect（经 OMC）、SNMP Hypervisor、WBM（HTTPS）
- **版本兼容**（p9 矩阵，四列为 8770 R4.2/R5.0/R5.1/R5.2）：

| PCX 版本 | 兼容的 8770 |
|---|---|
| OT R2.4-2.6.1 / OXE R12.2-12.4 | 四版全兼容 |
| OXE Purple R100 (N1) | R5.0/R5.1/R5.2 |
| OXE Purple R100.1 (N2) | R5.1/R5.2 |
| OXE Purple R101.0-101.2 (N3-N5) | 仅 R5.2 |
| OXO Connect/OCE R4.0 | 四版全兼容 |
| OXO Connect/OCE R5.0-5.1 | R5.0/R5.1/R5.2 |
| OXO Connect/OCE R5.2-6.2 | R5.1/R5.2 |

- **虚拟化**：ESXi 6.x/7.0/8.0、Hyper-V 2016/2019/2022、Nutanix AHV、AWS；虚拟化本身不收许可，sizing 用 Capacity Planning tool V3.0
- **RLAB 实验平台**（Boundary 背景）：POD 池独立同构（OXE/OMS/FlexLM/Client PC/Ecosystem/OV8770），公共区 NAS/邮件/SIP 模拟器；Console 与 RDP 两种访问模式

## A1 — 书中案例

**交付前平台核对场景**（依据 p4-38 讲义，无实验章）：

1. 定版本：对照 p9 矩阵核对 PCX 与 8770 版本配对
2. 定形态：物理 appliance 或虚拟机，按 Hypervisor 清单核对
3. 定入口：厚客户端管全套件；WBM 管 Users/Configuration/Performance
4. 定许可：Unified Management（WBM Users）、Directory、Domain Management 等逐项核
5. 匿名入口确认：Web Directory 默认允许匿名，引出保密设计需求
6. 实验环境问题一律回落本卡 Boundary 声明，不进生产配置

## A2 — 未来触发

使用情境：8770 有哪些应用/套件；WBM 和厚客户端分工；8770 与 OXE/OXO 什么版本能配；虚拟化支持哪些平台收不收费；8770 架构里 LDAP 和 MariaDB 各干嘛；实验环境是什么。

语言信号：8770 / OmniVista / 套件 / suite / WBM / 厚客户端 / Web Directory / 兼容性 / compatibility / R5.2 / Purple / ESXi / Hyper-V / Capacity Planning / RLAB。

与相邻能力区分：

- 目录功能交付 → 其余 11 张能力卡
- OXE 侧命令细节 → OXE 注册能力（仅注册子集）
- 计费/话务/报表 → 其它 8770 教材（书外）

## E — 可执行步骤

输入契约：客户站点信息（PCX 类型与版本、部署形态、许可清单）。

1. 版本核查：PCX 与 8770 版本对照 p9 矩阵逐行确认。完成标准：配对合法
2. 形态核查：物理/虚拟化平台对照支持清单。完成标准：形态可行
3. 许可核查：按能力需求列许可清单（Unified Management/Directory/Domain Management/AD integration）。完成标准：清单齐
4. 入口规划：厚客户端与 WBM 分工告知客户。完成标准：管理入口成文
5. 边界声明：跨套件需求指向对应教材，实验值声明实验口径。完成标准：范围共识

判停点：

- 客户 PCX 是矩阵外的更新版本 → 矩阵止于 Ed40 印刷口径：以官方最新兼容文档为准（n43），不口头承诺
- 计费/话务/报表/设备管理等需求 → 不在本书范围（n50），引用对应教材（8770XTE200/201 等）
- 客户问实验 IP/密码能不能用 → 一律不可：教学约定值（n42/n47），仅 Boundary 背景
- 虚拟化 sizing 细节 → 本书不展开：指向 Capacity Planning tool 与官方 sizing 文档

输出契约：平台就绪核对表（版本/形态/许可/入口）+ 范围边界声明。

## B — 边界

- 本书只精讲 Directory suite：性能/计费/报表等只有一页级介绍（n50），不拿本书当 8770 全功能手册
- RLAB 平台与 SIP 模拟器是教学专用基础设施（n47）：POD/IP/密码/号码全部实验口径，不可迁移生产
- 兼容矩阵为 Ed40 印刷口径：新版本 PCX 需查最新官方矩阵，"先升 PCX 再留旧 8770"会失去兼容（n43）
- Azure AD 一章已注明 Entra ID 更名；MSAD 支持的 Windows Server 止于 2022，时效性以官方为准
- 环境值（IP/密码/账号）只出现在本卡 Boundary 与 book/overview（nr-08）
