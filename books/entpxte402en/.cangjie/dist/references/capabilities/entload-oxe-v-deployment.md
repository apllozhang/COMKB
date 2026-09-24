# OXE-V 虚拟化：平台选型、许可路径与 OXE/OMS 虚机交付

## R — 原文依据

> "The OmniPCX Enterprise Call Server software package dedicated to virtualized environment is called OXE-V"（p133）
> "VMware ESXi (1) 8.0 7.0 ... Microsoft Hyper-V 2022 2019 2016 (2) ... KVM kernel ≥ 4.12.14 & KVM ≥ 5.2 (3) ... AWS (except OST64)"（p134）
> "Hyper-V, Nutanix and AWS don't provide a native way to redirect an USB dongle ... Cloud Connect is the mandatory license control process in case an OXE is virtualized over Hyper-V, Nutanix or AWS technology"（p136）
> "120 VOIP channels per OMS 240 OMS per OXE"（p138）

出处：ENTPXTE402EN p131-154、p166-188、p204-218。

## I — 自述

虚拟化平台的选择直接锁死许可路径——这是全书代价最高的架构决策，必须在设计阶段定死：

| 平台 | Ed12 时点版本口径 | 许可路径 |
|---|---|---|
| VMware ESXi | 8.0 / 7.0（含该版本 minor 更新） | FlexLM+加密狗 或 Cloud Connect |
| Microsoft Hyper-V | 2022 / 2019 / 2016；CS 用第 1 代虚机，OXE-MS/OST64/EEGW 用第 2 代 | 仅 Cloud Connect |
| KVM | 内核 ≥4.12.14 且 KVM ≥5.2；RHEL/SLES/Proxmox 等标准 KVM 均可 | FlexLM+加密狗 或 Cloud Connect |
| Nutanix AHV | 20230302 / 20220304（OST64 除外）；定制 KVM 需专项认证 | 仅 Cloud Connect |
| AWS | （OST64 除外） | 仅 Cloud Connect |

两条许可铁律：

- FlexLM 与 CCI/RTR 两种许可模式不能同时启用——虚机启 RTR 前必须核对 FlexLM Licensing Enabled=No
- 改 RTR 参数需要重启呼叫服务器

OXE-V 六种拓扑：全虚拟化、呼叫服务器冗余（local/spatial）、原生加密（SRTP）、混合（虚机 CS+硬件媒体网关）、分支机构（总部 CS+WAN+分支 OMS）、组网（ABC link 多节点）。PCS 接管行为：CS→PCS 软复位（释放话音、虚机不重启）；PCS→CS 硬复位（虚机重启）；云服务不跑 PCS。

OXE VM 交付要点：

- SOT 项目按用户数选规格模板（模板决定硬盘与内存）；"OXE template for AWS" 为单独选项
- 目标为 SOT 生成的 .ovf/.ova 虚机时不要求 MAC；KVM 线经 Template Factory 生成模板后 virsh define 定义启动

OMS 要点：软媒体网关虚机（等价一块 GD4 板卡），每台 120 VoIP 通道、每 OXE 最多 240 台；会议 3/6/14/29 方；许可 Lock 384（台数）+ Lock 385（通道总数），均可不停机安装。

KVM 线手工建虚机（Rocky 9.4、1GB 内存、1 CPU、16GB 盘）后 IPXE 引导加载，装完 omsconfig 配置并在 OXE 数据库声明；一个 SOT 项目最多声明 4 台 OMS。

## A1 — 书中案例

**OXE VM 生成与加载（ESXi 线）**（p204-211，How-To）：

1. Easy 建 Greenfield 项目，产品 OXE，勾 OVF generation
2. 选软件版本（无补丁/带静态/带静+动三选一）
3. OXE sizing 按用户数选模板；目标设置不填 MAC
4. CPU IP 与主机名设好，Verify 后 Deploy
5. ".ova" 生成后 Download（或复制 URL 稍后下载）
6. ESXi 按 OVF/OVA 流程部署 OXE VM
7. Power On 后加载自动开始，SOT 显示进度至 completed
8. 加载后：键盘、四账户密码、信任主机、许可、siteid 核版本

**OMS 加载（KVM 线）**（p177-188）：VMM 建虚机记 MAC；SOT 传 BootDVD 与 OMS 两个 iso；项目填 MAC 与 IP；VM 启动按 ESC 选 IPXE；装完 root 改密、omsconfig 配置、OXE 数据库声明。

## A2 — 未来触发

使用情境：客户定了虚拟化平台问许可怎么办；OXE 虚机怎么生成部署；OMS 容量与许可怎么算；Hyper-V 上虚机起不来；选 ESXi 还是 KVM。

语言信号：OXE-V / 虚拟化 / ESXi / Hyper-V / KVM / Nutanix / AHV / AWS / FlexLM / dongle / 加密狗 / Cloud Connect 许可 / gen1 / gen2 / OMS / GD4 / 120 通道 / Lock 384 / 385 / ova / ovf / virsh / IPXE / omsconfig。

与相邻能力区分：

- GAS 一体机形态 → GAS 交付卡
- 装好后连云 → 云连接卡
- 物理 CS3 加载 → CS 加载卡

## E — 可执行步骤

输入契约：客户虚拟化平台与版本、用户数（定规格模板）、许可模式倾向（FlexLM 或 Cloud Connect）、Template Factory 或 hosted SOT 就绪。平台为 Hyper-V/Nutanix/AWS → 直接锁定 Cloud Connect 路径。

1. 平台合规核对：对照平台矩阵核版本与代次（Hyper-V 分 gen1/gen2）。完成标准：平台在矩阵内
2. 定许可路径：ESXi/KVM 可选 FlexLM+加密狗；其余仅 Cloud Connect。完成标准：许可路径写入设计
3. 生成虚机：SOT 勾 OVF generation（虚机免 MAC）或 Template Factory 出 KVM 模板。完成标准：.ova/.tgz 到手
4. 部署：ESXi 走 OVF/OVA 部署；KVM 宿主 virsh define 后启动。完成标准：虚机开机自动加载
5. 加载后初始化：键盘、四账户密码、信任主机、许可、siteid 核版本。完成标准：登录提示出现
6. OMS 交付：建/生成 OMS 虚机，IPXE 或自动加载，omsconfig 配置。完成标准：OXE 数据库声明且 OMS 进入服务
7. 许可核对：spadmin 查 Lock 384/385 与台数/通道匹配。完成标准：计数与设计一致

判停点：

- 平台版本不在矩阵内或平台较新 → 停，以 TBE043 最新版复核，不按教材矩阵硬答
- FlexLM 与 RTR 同时想开 → 停，两者互斥，设计阶段二选一
- Hyper-V 虚机起不来 → 停，先查代次（CS=gen1，OXE-MS/OST64/EEGW=gen2）
- OMS 台数或通道超上限 → 停，每 OXE 240 台 OMS、每台 120 通道为硬口径

输出契约：平台×许可选型结论 + 运行中的 OXE-V CS 与 OMS（许可计数核对记录）。

## B — 边界

- 教材矩阵为 Ed12 时点快照，平台演进以 TBE043（Virtualization Design Guide）为准；AWS 部署对照 TC3142en-Ed01
- 虚拟化拓扑图组为讲义级，详细设计在 TBE043；PCS 与备机的云服务边界见云连接卡（nr-06 双规则）
- OMS 升级由 OXE CS 经 TFTP 自动下发（同 GD4 流程）；GAS 上 OMS 限 1 台的规则属 GAS 交付卡
- 实验口径：KVM host 192.168.1.55、OXE VM 192.168.1.201/.203、OMS 192.168.1.213、OMS 规格 1GB/1CPU/16GB
