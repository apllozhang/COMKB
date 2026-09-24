# SOT 媒体传输与加载项目配置（公共动作）

## R — 原文依据

> "Medias management • 3 types of database • Windows server • NFS server • Internal SOT local storage • Supported format • ".iso" file • Complete software version • ".zip" file • Software patches, hotfixes • License files « .mao », « .swk »"（p33）
> "you have to establish a FTP or SFTP (port 2222) session, using a FTP client, with the following account: Login: upload Password: sot"（p86）
> "Greenfield project Checked for a new installation from scratch"（p85）

出处：ENTPXTE402EN p33-34、p84-87、p94-95、p101-102。

## I — 自述

媒体传输与项目声明是所有加载场景（单版本/多版本/补丁/OMS/GAS/虚机镜像）的公共动作，先做熟这一段，后面每个场景只剩差异化字段。

媒体管理三件事：

1. **存放位置三选一**：Windows 服务器、NFS 服务器、SOT 本地存储
2. **格式语义**：.iso=完整软件版本；.zip=补丁/热修复；许可文件为 .mao/.swk 等
3. **传输通道**：FTP 或 SFTP（端口 2222）、账号 upload（实验口径口令 sot），客户端常用 Filezilla；上传后点 Refresh medias list，勾选文件并 Declare media(s)，版本才进入可用列表

项目两种工作模式：

- **Easy 模式**：向导式（产品类型、媒体、目标设置一路点下去），首次交付推荐
- **Expert 模式**：媒体与项目独立管理，媒体必须先声明再建项目；更新类操作（多版本/补丁）在 Projects listing 里对既有项目点 update

项目公共字段：Project name/Description；OVF generation（目标为 SOT 生成 ovf 的虚机才勾，勾后免 MAC）；物理机目标必填 MAC（板卡贴纸或 ifconfig）；Country/Timezone；Storage area 可上传许可文件（OPS）——项目里带了许可就自动部署，没带就事后手工恢复。

项目两种类型：Easy 模式第一步选 Greenfield（从零全新安装）；对既有产品更新则走 Projects listing 里的 update 流程。

## A1 — 书中案例

**媒体声明与项目创建**（p84-95，How-To 片段）：

1. Filezilla 以 upload 账号连 SOT（FTP 或 SFTP 2222）
2. 上传 OXE 版本 iso（可同时传 OPS 许可文件）
3. 回 SOT Web 点 Refresh medias list
4. 勾选 iso 后 Declare media(s)
5. Media listing 确认版本进入可用列表
6. Easy 模式新建 Greenfield 项目，产品选 OXE
7. 媒体存储位置选 Local storage，版本入列后进入目标设置

## A2 — 未来触发

使用情境：SOT 里看不到刚传的版本；媒体传一半失败；项目建到一半缺媒体；许可要不要随项目带；Easy 和 Expert 模式怎么选。

语言信号：Declare media / Refresh medias list / upload / SFTP 2222 / Local storage / NFS / Greenfield / Expert mode / Easy mode / OVF generation / MAC 地址 / Storage area / OPS。

与相邻能力区分：SOT 本身的部署与更新 → SOT 安装卡；各加载场景的差异化字段 → 对应加载卡；分发器模式的 /tmpd 传输是 OXE 侧通道，与本卡 SOT 侧通道是两回事。

## E — 可执行步骤

输入契约：媒体文件（iso/zip/许可）与来源（MyPortal 下载或 NAS）、SOT 可登录、网络可达。媒体还没下载 → 判停先到 MyPortal 取，别猜文件名。

1. 传媒体：upload 账号连 SOT（FTP/SFTP 2222）上传文件。完成标准：文件出现在列表
2. 声明媒体：Refresh medias list，勾选文件，Declare media(s)。完成标准：Media listing 可见
3. 建项目：Easy 选 Greenfield（全新）或对既有项目 update（升级）。完成标准：产品类型正确
4. 填公共字段：项目名、Country/Timezone、OVF generation 按目标勾选。完成标准：字段完整
5. 目标信息：物理机填 MAC；虚机勾 OVF generation 后免 MAC。完成标准：Verify 通过
6. 许可（可选）：Storage area 上传 OPS 文件随项目部署。完成标准：加载后免手工恢复

判停点：

- 版本列表里找不到刚传的文件 → 停，回 Media 页做 Refresh + Declare，传输≠声明
- Expert 模式下项目建不了 → 停，Expert 模式媒体必须先声明再建项目（顺序硬规则）
- 虚机目标被要求填 MAC → 停，勾 OVF generation 的项目不需要 MAC，检查项目类型

输出契约：媒体已声明、项目就绪的 SOT（含是否随项目带许可的记录）。

## B — 边界

- SOT 一次只允许一个部署任务（p22）；并行交付需排队或另起 SOT 实例
- 媒体通道表述差异（p86 给全 FTP/SFTP 2222，hosted 各章仅写 FTP）按 p86 口径统一（nr-03）
- upload 账号口令 sot 为实验口径，生产部署应修改（Settings 的 FTP 账号菜单可改）
- 角色寻址与许可的后置责任见 CS 加载卡 Boundary（SOT 项目不代做角色寻址）
