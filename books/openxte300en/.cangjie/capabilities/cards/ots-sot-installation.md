# SOT 自动化装机与虚机手动导入（三路线、媒体与项目、OVF/OVA）

## R — 原文依据

> "Optimized methodology Concept based on a "enhanced PC-installer" tool running on a virtual machine ... All ISO files automatically mounted Silent installation process (including hotfixes)"（p46）
> "Such kind of installation based on manual processes can provide mistakes and inconvenient ... Several DVDs to burn • DVD burning errors"（p43）
> "Two working modes Easy Kind of wizard ... Expert Management of medias and projects"（p61）
> "VSPHERE CLIENT IS ONLY AVAILABLE WITH ESXI VERSION 6.0 OR LOWER."（p84）
> "HERE, IN REMOTE-LAB CONTEXT, A OTMS VM TEMPLATE IS ALREADY GENERATED AND DEPLOYED ..."（p73）

出处：OPENXTE300EN p40-87。

## I — 自述

交付物四类：bootdvd（SUSE OS）、OpenTouch core 安装包、hotfix、许可文件，全部从 BPWS 下载。三条安装路线：

| 路线 | 介质 | 特点 |
|---|---|---|
| 手动全 DVD | 多张 DVD | 易错（烧录/介质/光驱）、全程人守、非静默 |
| 手动 ISO | bootdvd 装 OS，其余 ISO 拷 USB 挂载 | 少烧盘，仍需人工、非静默 |
| SOT 自动化 | ISO（内含 .ova）交付的部署虚机 | 自动挂载全部 ISO、含 hotfix 静默安装、PXE 启动目标机 |

SOT 使用三个维度：

- 运行模式：standalone（技师笔记本 VirtualBox 5.2.24+ 或 VMware Workstation 14+，主要部署物理机）或 hosted（vSphere/ESXi 6.0+，可生成 OVF 模板）
- 配置：default 或 Template Factory（第二盘 500GB、8 CPU/16GB、VMX 标志、USB 控制器；Template Factory 对 OpenTouch 产品不可用）
- 工作模式：easy（向导：产品、媒体、目标）或 expert（Projects/Medias/External storage/Settings 四页，媒体先于项目声明）

媒体库三类（Windows server、NFS server、SOT 本地存储），支持 .iso 整版、.zip+MD5 补丁（SOT 3.0 起，限同主版本）、.ice/.mao/.swk 许可。SOT 一次只部署一台。

OVF/OVA 手动导入（web client 主流程）：添加虚机时选"Deploy from OVF or OVA file"，选文件、命名、选存储、网络映射、Thin 置备、自动开机。附录的 vSphere client 流程仅适用 ESXi 6.0 及更低。

## A1 — 书中案例

**SOT hosted 部署实验**（p66-78，R-Lab 特例见 B）：

1. SOT 虚机开机，控制台配静态网络四参数并应用。
2. 浏览器打开 SOT 地址，默认账号登录并按提示强改密码。
3. 进 Expert 模式，先声明 bootdvd、core 等 ISO 与许可文件。
4. 本地存储库先用 FTP 账号上传介质后再刷新声明。
5. Projects 建项目：产品选 OTMS，核对媒体映射与许可。
6. 目标机参数：主机名、域名、键盘、MAC 与管理地址。
7. Deploy 后启动目标虚机，SOT 等待 PXE 装载。
8. 装完 OT 自动重启进入初始化向导。

**OVF 手动导入实验**（p79-87）：

1. 浏览器登录 ESXi 的 web client。
2. 添加虚机选 Deploy from OVF or OVA file。
3. 命名并选择 ovf 与关联 vmdk 文件。
4. 选存储位置，网络映射选目标网络。
5. 磁盘置备选 Thin，勾部署后自动开机。
6. 核对信息后 Finish，虚机出现在清单并可开机。

## A2 — 未来触发

使用情境：新站点要装 OTMS；现场没有光驱只有 ESXi；SOT 媒体声明不上；要不要用 Template Factory；拿到 OVA 不知道怎么导。

语言信号：SOT / Software Orchestration Tool / 装机 / 部署 / 静默安装 / silent / PXE / 媒体 / media / project / OVF / OVA / vmdk / ESXi / bootdvd / hotfix / BPWS。

与相邻能力区分：装完后的初始化交给初始化向导能力；许可文件规格与锚定物见许可能力；虚机规格与 sizing 属 SOT Delivery note（书外）。

## E — 可执行步骤

输入契约：部署路线决策（SOT 或手动）；四类介质与许可已从 BPWS 下载到位；目标机参数（MAC/IP/FQDN/键盘）；宿主版本（ESXi 6.5/7.0.x 或 Hyper-V 2016/2019）。

1. 备料：bootdvd、core、hotfix、许可四类齐。完成标准：清单与 BPWS 下载一致
2. SOT 路线：配网络、传媒体、建项目、Deploy、PXE 装机。完成标准：OT 重启进初始化向导
3. 手动路线：web client 导入 OVF/OVA，或 DVD/ISO 安装。完成标准：虚机可开机
4. 交接：把待初始化系统交给初始化向导能力接手

判停点：

- 多台要装 → SOT 一次只部署一台，排队执行（p53）
- 想用 Template Factory 装 OpenTouch → 不可用（p56），仅其他产品可用
- 拿附录 vSphere client 流程套 ESXi 6.5/7.0.x → 不适用，走 web client
- R-Lab 特例当生产流程 → 现场无预部署模板、许可必须加密狗（nr-04）

输出契约：装完软件待初始化的 OT 虚机或物理机 + 部署参数记录（MAC/IP/FQDN/介质版本）。

## B — 边界

- 实验口径（生产必须替换）：SOT 地址 192.168.1.230，默认账号 admin/letacla（首登强改），本地库上传账号 upload/sot。
- SOT 宿主底线：VirtualBox 5.2.24+ / VMware Workstation 14+ / ESXi 6.0+；Template Factory 加码 8 CPU/16GB/500GB（p55-59）。
- R-Lab 特例（n10，见 needs-review nr-04）：模板已预部署、SOT 不生成 OVF、按物理机方式给 MAC、许可锚 MAC 不锚加密狗——现场恰好相反。
- 虚机规格与 sizing 见 SOT Delivery note 与 Delivery note/Features list（书外，n01），本卡不报容量。
- 补丁升级：SOT 自 3.0 用 zip+MD5（限同主版本）（p65）。
