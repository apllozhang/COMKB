# OTMC 产品定位与部署形态（三通道/组网边界/规模口径）

## R — 原文依据

> "The OpenTouch™ Message Center is a stand-alone voice mail system installed on a single server, including automated attendant capabilities"（p5）
> "Direct SIP trunk group between OXE and OTMC • Only one SIP trunk is supported towards the front node"（p18）
> "OTMC-V can be virtualized with VMware ESXi • vMotion, VMware Dynamic Resources Scheduling (manual / semi-automatic) are supported (Other VMware services are not supported)"（p15）
> "Scalability must be managed using the OpenTouch Capacity Planning Tool dedicated for OTMC"（p19）

出处：OTMCXTE200EN p3-32（f01-f07、p01、n26/n27/n28 归并）。

## I — 自述

**定位三句话**：单服务器独立语音邮件系统（定义含自动话务员能力）；只服务 OmniPCX Enterprise 的 Connection 用户；取代 46xx/8440 旧方案。消息存 OTMC 服务器或 SAN，运行于 SUSE Linux Enterprise。

**访问三通道**：任意话机走 TUI；Premium Deskphone 8xx8 与 Smart Deskphone 8088 经信封键走 GUI（可视化信箱 VVM，默认要 TUI 密码）；任意 IMAP 邮件客户端。

**连接三要素**：OXE 与 OTMC 间直连 SIP trunk group 仅一条、指向 front node（Bypass 按全部端口，与用户数无关）；OXE 间 PRS 链路支撑话机 GUI 显示（端口 2570）；VPIM 用于 OTMC 互联与三方信箱互通。

**形态两分支**：物理机（许可绑 ALUID）与 OTMC-V 虚机（许可绑 dongle；vMotion/DRS 白名单，同主机可多实例、可混跑第三方虚机；限制与功能等同物理版）。

**规模口径表**：

| 口径 | 数值 | 出处 |
|---|---|---|
| 三个 SUSE 安装模式标注 | 各 15000 users | p62 |
| 话机 GUI 显示并发上限 | 5000 用户（8 系/80x8/8088，经 PRS） | p18 |
| 扩容评估 | 必须用 OTMC 专用 Capacity Planning Tool（用法书外） | p19 |

**组网边界**：集中式/分布式 OXE 子网均支持（集中式也仅一条 SIP trunk 指向 front node）；OXE ABC Supra 网络不支持集中式 VM。

## A1 — 书中案例

本章（OTMC Overview 与 Topology for labs）为概念与拓扑讲义，无 How-To 实验；p19 仅给容量压缩场景示例图（2800/1200 用户，示例口径），工具用法在书外。实验拓扑表（六虚机、DNS 域、IP/账号）是教学专用基础设施，作实验口径对照，不构成交付动作。

## A2 — 未来触发

使用情境：售前评估 OTMC 适不适合客户；物理还是虚拟怎么选；客户要 VMware 全家桶；多站点集中信箱可行吗；15000/5000 上限怎么解释。

语言信号：OTMC 是什么 / OTMC-V / 部署形态 / 商业包 / 集中式语音邮件 / centralized VM / VPIM / ABC Supra / 容量 / 15000 / 5000 / PRS / 46xx / 8440。

与相邻能力区分：动手装机归 otmsg-install-site-setup；话路参数归 otmsg-sip-trunk-provisioning；许可落地归 otmsg-license-management。

## E — 可执行步骤

输入契约：客户站点数、用户数、话机型号清单、虚拟化平台现状。

1. 形态决策：物理（ALUID 绑定）与 OTMC-V（dongle 绑定、vMotion/DRS 白名单）二选一。完成标准：形态结论成文
2. 组网决策：集中/分布式评估；确认 OXE 网络类型（Supra 排除集中式 VM）。完成标准：拓扑约束成文
3. 容量口径：引用 15000/5000 必带前提（安装模式标注/经 PRS 的 GUI 并发）；扩容评估转 Capacity Planning Tool。完成标准：规模结论与书外清单
4. 交付衔接：把结论移交装机与对接能力。完成标准：进入实施

判停点：

- 客户要 VMware HA/FT 等全套服务 → 停，白名单只有 vMotion 与手动/半自动 DRS（n26）
- 客户要硬件规格或精确产品上限 → 停，指向 feature list / product limits（n28）
- 客户是 ABC Supra 网络又要集中信箱 → 停，不支持，转分布式 + VPIM 互联方案（n27）

输出契约：部署形态与组网决策结论（含书外依赖清单）。

## B — 边界

- 自动话务员（AA）只是 OTMC 定义中附带的能力，Starter 级别不教 AA 配置（p5/p225）；"arrive on AA"播报选项已废弃（n19）
- 硬件/软件规格、产品上限、容量规划工具用法、UM（Exchange/Domino/Gmail）落地、三方 VM 互通细节全部书外（n28）
- OMS 与 OmniPCX Enterprise GD 仅在实验拓扑表出现，书中未展开用途与全称——不补释义（g24）
- PRS/VPIM/ICE/MLE 等缩写书中未给全称，如实标注；实验拓扑环境值集中见 book/overview
