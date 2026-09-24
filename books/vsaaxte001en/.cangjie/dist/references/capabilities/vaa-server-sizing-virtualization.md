# VAA 服务器选型与虚拟化（规格三档、Hypervisor 前提、安全基线）

## R — 原文依据

> "The maximum number of VAA ports supported is 120 • To go above this limit, please contact the central presales team … Given as an example! Always consult the official documentation!"（p52）
> "VMware ESXi 8.0 • Network adapter for the VM must be VMXNet3 • VMWare Tools must be installed / Microsoft Hyper-V 2022 • VM type recommended is Generation 2 / KVM hypervisor Proxmox 8.2 … (1) KVM hypervisor Proxmox supported from VAA 4.6.1"（p53）
> "The remote SSH access for the ROOT account is forbidden. You must use the admin account with the function 'sudo'."（p55）

出处：VSAAXTE001EN p52-55。

## I — 自述

部署前的选型与基线核查：

1. **规格三档表（示例口径，原文两处强调务必查官方文档）**，VAA 最大支持 120 端口、超限找中央售前：

| 端口档 | 处理器 | 内存 | 网络 | 硬盘 |
|---|---|---|---|---|
| 最多 8 端口 | 双核 2.4 GHz | 8 GB | 100 Mb/s | 80 GB |
| 最多 50 端口 | 四核 2.4 GHz | 16 GB | 1 Gb/s | 80 GB |
| 最多 120 端口 | 八核 2.4 GHz | 32 GB | 1 Gb/s | 最低 320 GB |

2. **虚拟化兼容三前提（同样示例口径）**：VMware ESXi 8.0——虚机网卡必须 VMXNet3 且必须装 VMware Tools；Microsoft Hyper-V 2022——推荐 Generation 2 虚机；KVM（Proxmox 8.2）——VAA 4.6.1 起支持且网卡必须 VMXNet3；部署细节以安装手册为准
3. **安全基线两条**：root 禁止 SSH 远程登录（只能本地控制台），远程一律 admin + sudo su——这是 CIS-2 基线设计而非故障；操作系统底座为 SUSE（ALE BootDVD 安装，物理机/虚机均可）
4. **端口清单**：p55 为 TCP/UDP 端口清单页，正文仅一句 root SSH 规则；具体端口与防火墙设计以官方安装文档为准

## A1 — 书中案例

**选型核查序列**（p52-55 讲义，无实验）：

1. 从客户预期并发话务推算所需 VAA 端口数
2. 超过 120 端口即停，转中央售前评估
3. 按端口档查规格三档表初筛硬件
4. 引用任何数值时带上原书免责："仅示例，务必查官方文档"
5. 核对虚拟化平台：版本、虚机代际、网卡类型（VMXNet3）、工具安装
6. Proxmox 场景核对 VAA 版本不低于 4.6.1
7. 交付网络端口需求清单时以官方文档当期版为准
8. 向客户说明 root SSH 禁用为安全基线，运维走 admin + sudo

## A2 — 未来触发

使用情境：售前报配置；客户问 Proxmox/ESXi/Hyper-V 能不能跑；虚拟机网卡选型；项目要 200 端口；运维抱怨 root 连不上；写投标文档引用规格。

语言信号：规格 / sizing / 8 端口 / 50 端口 / 120 端口 / 120 端口上限 / 双核 / 四核 / 八核 / ESXi / VMXNet3 / Hyper-V / Generation 2 / Proxmox / KVM / root SSH / sudo / SUSE / BootDVD。

与相邻能力区分：安装施工与参数契约归安装对接能力；许可与商用模式归 PCS/OPEX 卡；产品功能边界归架构冗余能力。

## E — 可执行步骤

输入契约：客户并发话务预估（端口数）、现有虚拟化平台与版本、运维安全基线要求、官方文档获取渠道（MyPortal）。

1. 端口测算：按业务峰值并发定端口档位；超 120 转售前。完成标准：档位结论
2. 硬件初筛：查三档表给配置建议，注明示例口径。完成标准：建议单带免责
3. 平台核对：对照三前提核查 Hypervisor 版本/虚机类型/网卡/工具。完成标准：无不满足项
4. 官方复核：用安装手册当期版复核规格与端口清单后再定稿。完成标准：文档指针留档
5. 基线交底：向客户运维说明 root SSH 禁用与 admin+sudo 工作方式。完成标准：无"故障"误报

判停点：

- 客户要求 300 端口单机 → 停，产品上限 120 端口，转中央售前评估拆分或多实例
- 客户平台不在三列表（如桌面级虚拟化） → 停，书内无兼容口径，以官方兼容表为准不拍脑袋
- 投标文档要引用规格数值 → 停，必须带"示例口径，以官方文档为准"边界（n03）
- 有人要求放开 root 远程登录 → 停，安全基线设计，不做"修复"（n10）

输出契约：端口档位与硬件建议单（含免责）+ 虚拟化核查表 + 运维基线说明。

## B — 边界

- 规格表与兼容表均标注"Given as an example! Always consult the official documentation!"，教材只给骨架（n03）
- 版本锚点随时代漂移（ESXi 8.0/Hyper-V 2022/Proxmox 8.2），选型前必须对官方当期兼容表
- 端口清单细节在官方文档，本卡不载具体端口号（n50）
- Hypervisor 表为快照口径：Proxmox 自 VAA 4.6.1 起支持，更早版本不可用（p53 注）
- 实验环境虚机规格与口令为教学专用（仅 Boundary 背景，见 book/overview），不可作为生产依据
- SUSE 系统安装全步骤在实验中跳过（预装虚机起步），完整流程见安装指南 4.2（n50）
