# GAS 通用设备服务器：硬件前置、软件加载与后安装向导

## R — 原文依据

> "Generic Appliance Server (GAS) packaging provided by ALE • Operating system: Rocky Linux • Virtualized OXE on top of Rocky linux's KVM layer ... FlexLM license server directly installed on Rocky linux"（p221）
> "OXE+OMS+WebRTC: 4 cores / 2.8 GHz / 8 GB / 360 GB ... Above 7,000 users, an external WebRTC gateway is required"（p226）
> "The IP address of the default gateway (this IP MUST be accessible during installation)"（p235）
> "Execute "./oxeswspostinst.bin""（p263）

出处：ENTPXTE402EN p219-242、p244-282。

## I — 自述

GAS 用"打包"消灭硬件不确定性：BP 按前置表自备服务器，ALE 软件包（Rocky Linux+KVM 底座）承载 1 台 OXE VM（Rocky）、1 台 OMS VM（Rocky，可选）、1 台 Rainbow WebRTC VM（Debian，可选）；FlexLM 直接装在宿主 OS；dongle-less，许可基于服务器 ALU-ID 或 Cloud Connect ID。

硬件前置表（OXE 为必装底座；用户数 >12000 时内存再加 2GB）：

| 组件组合 | 核数 | 主频 | 内存 | 硬盘 |
|---|---|---|---|---|
| 仅 OXE | 2 | 任意 | 4GB | 360GB |
| OXE+OMS | 2 | 2.8GHz | 6GB | 360GB |
| OXE+WebRTC | 3 | 2GHz | 6GB | 360GB |
| OXE+OMS+WebRTC | 4 | 2.8GHz | 8GB | 360GB |

平台与组件红线：CPU 最低 Haswell 代（Intel 64+VT）；1GB 网卡；能 DVD 引导；只认硬件 RAID（软件 RAID 不支持）；OMS 每 GAS 限 1 台且禁装第二台；内嵌 WebRTC 网关 50 并发封顶，>7000 用户必须外部网关；HP DL20 G11 只能用 GAS 软件包；冗余双机硬件须相似且禁 Appliance Server 与 GAS 混搭。

IP 连通性清单：宿主 IP（FlexLM 与宿主共用同一 IP）、默认网关 IP（安装期间必须可达）、DNS IP（客户不配 DNS 时可用 GAS 自身 IP 顶替）、OXE CS IP；OMS/WebRTC IP 可选。IP 计数：宿主 1+OXE 1+OMS 1+WebRTC 1。

后安装向导（oxeswspostinst.bin，需 Xming+Putty X11；root 直登 SSH 已禁用）六段依次填写：

1. 国家码（用于 OXE 建库与时区）
2. OXE 参数：主机名/IP/网关/节点名；信任主机 CSV 落 /opt/config/trust/import_th.csv，iptables 建好后移到 /tmpd/import_th_bkp.csv
3. 冗余形态：Local 同子网一个 Main IP；Spatial 两子网两个 Main IP，另需 DNS 委托解析节点名
4. 可选组件：OMS、WebRTC
5. WebRTC GW 参数：IP/网关/DNS/NTP、TURN=GEOIP、RAINBOW_PBXID、PBX_DOMAIN、Rainbow 域名
6. 许可三选一：Browse 选文件 / Skip 事后补 / Mount USB（挂 /media/usb-drive 后选 5 个许可文件）

FlexLM 侧：.ice 入 /opt/Alcatel-Lucent/data/licenses 后 systemctl restart flexlmd；OXE 侧对接端口 27000，改完必须重启 CS。

## A1 — 书中案例

**GAS 加载与后安装**（p244-282，How-To）：

1. 备 bootdvd 与 GAS 两个 iso，SOT 建 Greenfield 项目（产品 GAS）
2. 经 ILO 进 System Utilities 的 Summary，记 Port 1 网卡 MAC
3. 项目填 MAC、hostname、IP，Declare 媒体后 Deploy
4. 重启按 F11 选 PXE（Embedded LOM 1 Port 1）开始加载
5. 培训环境约 60 分钟装完，改各账户默认密码
6. Xming+Putty（X11 forwarding）以 admin 登录跑 oxeswspostinst.bin
7. 向导依次过：国家码、OXE 参数、可选组件、WebRTC GW 参数、许可
8. Install 完成后 virt-manager 进各 VM 收尾键盘与密码

## A2 — 未来触发

使用情境：客户买了服务器要装 GAS；后安装向导字段怎么填；WebRTC 网关参数；FlexLM 许可怎么装；冗余两台怎么规划；root 登不上去。

语言信号：GAS / Generic Appliance Server / Rocky / BootDVD / oxeswspostinst.bin / 后安装 / post-installation / PBXID / TURN / GEOIP / FlexLM / ALU-ID / .ice / 27000 / 信任主机 / import_th / DL20 / PXE。

与相邻能力区分：

- GAS 日常运维（备份/升级/UPS） → GAS 运维卡（路由）
- OXE/OMS 虚机在通用虚拟化上的交付 → 虚拟化交付卡
- 许可模式与 RTR 互斥判定 → RTR 卡

## E — 可执行步骤

输入契约：满足前置表的服务器（硬件 RAID）、BootDVD+GAS 两个 iso、客户 IP 规划、许可文件（.swk 与 .ice）、冗余形态决策。网关 IP 安装期不可达 → 判停先跟客户网络组落实。

1. 前置核对：硬件前置表逐项过（核数/主频/内存/360GB/硬件 RAID）。完成标准：服务器在表内
2. SOT 加载：建 GAS 项目、取 MAC、Deploy、PXE 引导装完。完成标准：登录提示出现
3. 改默认密码：先 admin 登录（root 直登已禁用），passwd root 与 admin。完成标准：默认口令全部替换
4. 后安装向导：Xming+Putty X11 跑 oxeswspostinst.bin，六段依次填。完成标准：POST INSTALLATION SUCCESSFULLY INSTALLED
5. FlexLM 安装：.ice 入 /opt/Alcatel-Lucent/data/licenses，restart flexlmd，lmutil lmstat -a 核对。完成标准：active (running)
6. OXE 对接：System/Licenses 填 Flex Server IP 与端口 27000、发现开 Yes，重启 CS。完成标准：spadmin 可查许可
7. WebRTC GW：换真实 RAINBOW_PBXID（来自 Rainbow 云平台），按冗余形态定 PBX_DOMAIN。完成标准：网关注册 Rainbow

判停点：

- 服务器是软件 RAID → 停，GAS 不支持，先改硬件 RAID
- 向导里 PBXID 只有示例值 → 停，正式值必须向 Rainbow 云平台索取，照抄会连错租户
- 冗余要 Appliance Server 混搭 GAS → 停，禁止混搭，双机硬件须相似
- 改完 FlexLM"许可还是不认" → 停，先确认 OXE 重启过没有（硬前提）

输出契约：三 VM 就位、许可链打通（FlexLM/OXE 两侧核对记录）、WebRTC 网关参数表存档的 GAS 系统。

## B — 边界

- 经典 OXE 软件包在所有物理服务器上不再支持，legacy 须迁 GAS 或虚拟化（TBE063）；GAS 安装细节对照 TC3138；WebRTC 网关对照 TBE067
- GAS 上标准 FTP 禁用：传文件走 SFTP/SCP（admin 传 /tmp 后 root mv）；FlexLM 凭证 root/letacla1 为默认口径须改（p269/p280）
- 存量满配拓扑装不下旧 Appliance Server——HP DL20 G10+/G11 才接得住 <7000 用户的满配（p226-227）
- 实验口径：GAS 192.168.1.45（OXE .1/.3、OMS .13、WebRTC .15）；加载约 60 分钟、后安装约 15-20 分钟
