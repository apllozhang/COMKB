# 软件升级与 Auto-Fabric 零触开局（版本策略、升级通道、七步链、LBD）

## R — 原文依据

> "Starting with 8.10R4 signed images are available for the whole portfolio (already available for OS6570M since 8.9R4) • U-boot password protection is available since 8.7R3 – be careful when enabling it (no AOS recovery possible in case you lose this password)"（p531）
> "Generally, use the latest 'GA' (General Availability) or 'MR' (Maintenance) release"（p532）
> "1- Auto-VC 2- Automatic remote configuration 3- Auto-LACP 4- Auto-Routing 5- Auto-SPB Fabric 6- Auto-Network Profiling 7- Auto-MVRP"（p538）
> "Do you want to disable auto-configurations on this switch [Y/N]? ... If input is [Y] then auto-VC, RCL and auto-fabric are disabled"（p539）

出处：DT00XTE215EN p529-535, p536-554。

## I — 自述

两件"规模化"的事：把存量设备升到正确版本，让新站点插上就自动成网。

1. **升级三通道**（p533）：直连 FTP/SFTP、OmniVista 本地（2500 4.X/Terra）、OmniVista Cirrus（最简单，软件包内置推荐）；U-boot/ONIE/FPGA/CPLD 升级走 CLI 且失败即 RMA
2. **版本策略**（p531-532）：日常取最新 GA/MR；8.10R4 起全系列签名镜像（OS6570M 自 8.9R4）；合规场景按 FIPS 140-2/JITC/Common Criteria 认证清单选；软件包从 MyPortal 下载
3. **升级步骤不在本教材**：p533 明示"standard operation"，按 AOS Release Notes 执行；堆叠环境滚动升级（ISSU）见 Virtual Chassis 能力卡
4. **Auto-Fabric 七步链**（p538-552）：Auto-VC；RCL 远程配置（VLAN 1 与 127 各 3 次共 6 次 DHCP 取指令文件，取到 vcboot.cfg 会重置设备）
5. **后续五步**：Auto-LACP；Auto-Routing；Auto-SPB（BVLAN 4000-4015 映射 ECT 1-16，4×9 秒邻接窗）；Auto-Network Profiling；Auto-MVRP（STP 切 flat）
6. **首启 Y/N 语义相反**（p539）：输入 Y 才是禁用自动配置；N 或不答=启用。伴随 LBD 环路检测：周期组播帧回收即判环路，端口强制 down+日志+trap，可手动恢复
7. **各协议可单独关闭**：auto-fabric protocols <x> admin-state disable（p553）

## A1 — 书中案例

本章为纯讲义无 How-To 实验；讲义级关键素材（p539-552）：

1. 首启提示 "Do you want to disable auto-configurations [Y/N]?"：答 N 或不答即启用 Auto-VC/RCL/Auto-Fabric
2. RCL 在 VLAN 1 与 127 各试 3 次（共 6 次）取 DHCP 与指令文件，auto-config-abort 可取消
3. RCL 结束时若下载到 vcboot.cfg，设备自动重置加载
4. Auto-LACP 生成的聚合口径：agg 127、size 16、actor admin-key 65535
5. Auto-SPB 4 个 Hello（4×9 秒）内未成邻接则不参与 SPB
6. Auto-MVRP 在 LACP 与 SPB 发现后全局启用，并把 STP 切为 flat 模式
7. LBD 检测到环路：端口强制 down、错误日志、SNMP trap，需人工恢复

## A2 — 未来触发

使用情境：选升级版本与通道；U-boot 密码要不要开；底层固件升级风险评估；新站点十几台零触开局；首启提示怎么答；RCL 空跑怎么停；自动成网后防环。

语言信号：升级 / 软件版本 / GA / MR / 签名镜像 / U-boot / ONIE / FPGA / RMA / Auto-Fabric / 零触 / zero-touch / Auto-VC / RCL / Auto-LACP / Auto-SPB / MVRP / LBD / 环路检测 / vcboot.cfg。

与相邻能力区分：

- 堆叠滚动升级（ISSU 命令与目录）：Virtual Chassis 能力卡
- 升级前的配置备份与回滚基线：配置生命周期能力卡
- Lightning Config 单台开局：Lightning Config 能力卡
- 升级后的版本验证（show microcode loaded）：诊断工具箱能力卡

## E — 可执行步骤

输入契约：设备清单与当前版本、目标版本（GA/MR 或合规清单）、升级窗口、新站点拓扑与 DHCP/指令文件就绪度。U-boot/ONIE/FPGA/CPLD 升级必须单独立项。

1. 版本决策：按 GA/MR 或合规认证清单（FIPS/JITC/CC）定目标版本；核对 8.10R4 签名镜像口径。完成标准：目标版本成文
2. 通道选择：Cirrus 最简、OmniVista 本地、FTP/SFTP 直连；步骤按 AOS Release Notes（书外）。完成标准：升级 SOP 就位
3. 风险隔离：U-boot 密码启用前密码必须入库存档（丢失无恢复）；底层固件升级逐台分批、避开业务窗口。完成标准：回退与 RMA 预案明确
4. 零触准备（新站点）：DHCP 与指令文件（vcboot.cfg）就绪，或明确让新机空跑前 auto-config-abort。完成标准：RCL 能取到正确指令
5. 首启操作口径：要自动入网答 N（或不答）；要手工配置才答 Y；批量开局前统一操作口径。完成标准：无人为误答
6. 成网核验：七步链逐项确认（VC/聚合/路由/SPB/画像/MVRP），LBD 开启防环。完成标准：拓扑与模板一致

判停点：

- 现场没准备好 DHCP/指令文件 → 别让新机空跑 RCL（白等 6 轮还可能被旧模板重置），先 abort 或断网
- U-boot 密码无流程保障 → 停，没有双人存档制度就不启用
- 升级中 U-boot/ONIE/FPGA/CPLD 失败 → 无软恢复路径即 RMA，事前按 release note 核对前置固件
- 单台或几台的小站点 → 用 Lightning Config 更直接，Auto-Fabric 面向规模化新站点
- vcboot.cfg 模板设计需求 → 书外依赖架构师输入，本卡只管链路行为

输出契约：版本决策与升级 SOP（含风险预案）或零触成网的站点（七步链核验记录）。

## B — 边界

- 本教材不覆盖升级操作步骤（p533 明示），一切步骤按 AOS Release Notes；本卡只提供版本策略与风险边界
- Auto-Fabric 七步的协议细节（SPB/ECT/ISID、RCL 指令文件格式）书中仅一页机制图，深配置查 Network Configuration Guide 与架构师模板
- Auto-VC 期间 Demo License 默认启用（p540），正式部署换正式许可
- 默认 SPB 值（BVLAN 4000-4015、控制 BVLAN 4000、0x8000）为 Auto-Fabric 出厂口径，手工组网未必相同
- 版本号口径：8.10R4（签名镜像全系）、8.7R3（U-boot 密码）、8.9R4（OS6570M 签名/X48C4E 混插），保留原文位数
- Fleet Supervision/OST 等工具面 → 资产与装机工具能力卡
