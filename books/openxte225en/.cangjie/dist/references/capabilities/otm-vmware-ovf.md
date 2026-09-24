# VMware 虚机 OVF/OVA 部署（web client 与 vSphere client 两路）

## R — 原文依据

> "Deploy a virtual machine from OVF or OVA file … Network mappings: Select the network corresponding to the DMZ; Disk provisioning: … 'Thin' for lab"（p271-273）
> "Warning: VSPHERE CLIENT IS ONLY AVAILABLE WITH ESXI VERSION 6.0 OR LOWER."（p274）
> "Following procedure is done using Esxi 6.0 and v-Sphere client. It is exactly the same principle for Esxi 6.5 using Web administration interface."（p221）

出处：OPENXTE225EN p269-277, p221。

## I — 自述

OT SBC 与 Nginx 反代虚机都需要先有承载 VM，本书给了两条部署路线，按 ESXi 版本选：

| 路线 | ESXi 版本 | 入口 |
|---|---|---|
| web client | 6.5 口径（原理同 6.0 web 界面） | 浏览器登 ESXi，新增虚机 |
| vSphere client | 仅 6.0 及以下（大写 Warning） | 客户端 File，Deploy OVF Template |

通用参数口径：Network mappings 选 DMZ 对应网络；Disk provisioning 实验选 Thin；OVA 与 OVF 原理相同（OVA=OVF+VMDK 打包）。Nginx RP 的参考规格：Ubuntu 64 位、1 vCPU、2 GB 内存、20 GB thin、1 网口（实验口径）。

## A1 — 书中案例

web client 路线（p271-273，ESXi 6.5 口径）：

1. 浏览器打开 ESXi 地址并登录
2. 点新增虚机，选 Deploy a virtual machine from OVF or OVA file
3. 命名并选择 ovf+vmdk 文件（ova 直接选包）
4. 选择存储位置
5. Network mappings 选 DMZ 对应网络，Disk provisioning 选 Thin
6. 勾选 Power on automatically 后核对并 Finish

vSphere client 路线（p274，仅 ESXi 6.0 及以下）：

1. vSphere client 打开 File 菜单选 Deploy OVF Template
2. 选择 OVF 文件并命名
3. 选存储，磁盘类型选 Thin
4. VM Network 选对应网络（LAN/DMZ）后 Finish

验证：Finish 后虚机出现在清单并自动上电（勾选时）。

## A2 — 未来触发

使用情境：部署 OTSBC 或 Nginx RP 前的虚机准备；现场 ESXi 版本不明；OVA/OVA 包导入失败排查。

语言信号：VMware / ESXi / OVF / OVA / vSphere / web client / Thin / DMZ 网络 / 虚机部署 / Deploy OVF。

与相邻能力区分：虚机装好后的 OTSBC 初始化 → OTSBC 部署能力；Nginx 系统安装 → 反向代理能力。

## E — 可执行步骤

输入契约：OVF/OVA 安装包、ESXi 版本、目标网络（DMZ）、存储空间。

1. 确认 ESXi 版本：6.5 用 web client，6.0 及以下才可用 vSphere client。完成标准：路线选定（n27）
2. 按所选路线走 A1 对应步骤。完成标准：虚机出现在清单并上电
3. 网络映射核对：必须落在 DMZ 网络。完成标准：虚机网卡归属正确
4. 磁盘与规格：实验 Thin、Nginx 参考 1vCPU/2GB/20GB。完成标准：与部署对象规格匹配
5. 移交下一棒：OTSBC 走 CLI 初始化，Nginx 走系统安装（转对应能力）

判停点：

- 只有 vSphere client 而现场是 ESXi 6.5 → 停，客户端不可用，改 web 界面（n27）
- 生产 sizing 讨论规格 → 停，书内规格为实验口径，生产按实际 sizing（书外）

输出契约：可运行的虚机（网络/磁盘归属正确）+ 下一棒部署入口移交。

## B — 边界

- vSphere client 仅 ESXi 6.0 及以下可用，原文大写 Warning 强调（n27）
- 教材坐标为 ESXi 6.0/6.5；更新版本的行为不在书内
- Thin 磁盘与 1vCPU/2GB 规格均为实验口径，生产 sizing 在书外（nr-07）
- OVA 与 OVF 原理相同，仅打包形态差异（p271-273）
