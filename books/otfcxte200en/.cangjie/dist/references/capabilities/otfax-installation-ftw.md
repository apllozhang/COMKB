# OTFC 首次交付（宿主准备、软件安装、FTW 向导、许可）

## R — 原文依据

> "Preparing the server … Software installation … First time wizard First site creation. … Clients installation … Initial set-up OTFC basic configuration."（p46）
> "Server FQDN resolves to the server IP address in DNS • Reverse lookup of the server IP address in DNS returns the server FQDN"（p47）
> "Launch First Time Setup Wizard must be checked … Disable Microsoft's SMTP service before starting the OpenTouch Fax Center SMTP gateway service."（p65）
> "Enables a total of two channels (FoIP and fax boards) in evaluation mode … Applies a watermark on every fax page"（p52）

出处：OTFCXTE200EN p43-70（含 How-To 实验 1-3）。

## I — 自述

OTFC 是纯软件 FoIP 传真服务器，首次交付按四步主线走，从裸 Windows 服务器到"能收发传真"的最小可用系统：

1. **准备服务器**：与用户同域；FQDN 正向解析到 IP、IP 反向解析回 FQDN；与外部组件双向可达；装 IIS 角色带 4 个角色服务；建服务账号（六项权限，密码永不过期）
2. **软件安装**：Setup.exe 向导选语言（决定默认通知 Profile 与封页语言）、选 IP、Create a new system、传真主机名 + SIP 协议、装全部第三方软件；装完禁用 Microsoft SMTP（25 端口冲突）
3. **FTW 向导**：12 项动作搭出最小可用系统（建站点、QOS 0/0/240、CSID=站点名、建首用户、站点/系统路由表、告警通知、Mail Relay、产出摘要存盘）；可跳过或事后跑 FirstTimeSetup.exe
4. **许可**：首装自带评估许可——每组件 1 实例、共 2 通道、10 站点不限时、100 用户、每页水印；采购时向经销商提供服务器 MAC 地址，许可文件只能手工导入

## A1 — 书中案例

**准备传真服务器宿主**（p55-57，实验口径）：

1. 执行 ipconfig /all，核对与实验服务器信息匹配（fax.company.com / 192.168.1.60）
2. ping 主机名（fax.company.com），应 ping 通
3. nslookup 主机名，应解析出完整地址
4. 启动 Excel/PowerPoint/Word 各一次，确认无任何对话框弹出（Office 预初始化）
5. 关闭本地防火墙三 Profile（Domain/Private/Public 全 Off，实验口径）
6. Server Manager 添加 Web Server (IIS) 角色与 4 个角色服务后 Install

**安装与 FTW**（p58-70）：

1. Setup.exe 按向导 Next，选安装语言（注意持久副作用）
2. 选 XM FAX IP 192.168.1.60，系统类型 Create a new system
3. 定传真主机名 Fax，协议选 SIP；管理员临时密码 123456（首登必改）
4. Install 后全选第三方软件；收尾保持勾选 Launch First Time Setup Wizard
5. 停用并禁用 Microsoft SMTP 服务，再启动 XMSMTPGateway 服务
6. FTW：站点 My Organisation、用户源 Internal Database、SMTP 配置、首用户 baker@company.com、Proceed 后配置状态窗自动关闭

## A2 — 未来触发

使用情境：新买的服务器装 OTFC；装完收不到传真邮件任务；评估许可水印去不掉；要不要用 FTW 向导；装错语言想补救；通道数/用户数到了评估上限。

语言信号：安装 / Setup.exe / First Time Setup Wizard / FTW / 首次配置 / IIS / 角色服务 / 服务账号 / DNS 反向解析 / Microsoft SMTP / 25 端口 / 第三方软件 / 许可 / license / MAC 地址 / 水印 / watermark / 2 通道 / QOS。

与相邻能力区分：装完接话路归 SIP 通道集成能力；接邮件归邮件与 Exchange 集成能力；建用户策略归用户管理与 Profile 策略能力。

## E — 可执行步骤

输入契约：一台满足支持矩阵的 Windows 服务器（含 Office）、域名/DNS 可用、发行介质、许可商务口径（MAC 地址找谁要）。缺 Office 或域环境先补齐，否则 Rasterizer 与 AD 登录都会卡。

1. 核网络：FQDN 正反解 + ping/nslookup 三连验证。完成标准：三项全过，任一失败先修 DNS
2. 补角色：IIS + Windows Authentication / ISAPI Filters / ISAPI Extensions / IIS 6 Metabase Compatibility。完成标准：角色服务列表四项齐全
3. 建服务账号：域账号 + LDAP 查询权 + 目的地文件夹读写 + 网络打印权限 + 本地管理员 + 密码永不过期。完成标准：六项逐条核对通过
4. 预初始化 Office：以服务账号上下文启动 Word/Excel/PowerPoint 无弹窗。完成标准：三个应用首启零对话框
5. 跑 Setup.exe：选语言（按客户语言环境）、选 IP、Create a new system、组件与 SIP、装全部第三方软件。完成标准：服务列表出现 XMSMTPGateway 等服务
6. 处理 25 端口：Stop 并 Disable Microsoft SMTP，再启动 XMSMTPGateway（默认 Automatic）。完成标准：XMSMTPGateway 运行中、MS SMTP 停用
7. 跑 FTW：站点名、用户源、SMTP 配置、首用户、Proceed。完成标准：配置状态窗自动关闭，摘要文件已存盘
8. 导许可：取服务器 MAC 地址给经销商 → 手工导入许可文件。完成标准：水印消失、通道数解锁

判停点：

- DNS 反向解析配不出来 → 停，先修客户 DNS 再继续，反向解析缺失会导致后续邮件/目录环节偶发故障
- 服务器上已有别的 SMTP 服务常驻 → 停，先做服务器角色规划（OTFC 独占 25 端口），不要并行安装
- 客户要求多通道/去水印但商务流程未走 → 停，许可采购必须先提供 MAC 地址，这不是技术问题
- 版本/环境不在支持矩阵内 → 停，查最新 OTFC Features List 再答复，不用书内矩阵下硬结论

输出契约：可启动的 OTFC 系统（IIS 就绪、XMSMTPGateway 运行、MS SMTP 停用）+ 最小可用站点（首用户可登录）+ 许可状态说明。

## B — 边界

- 关闭本地与网络防火墙是实验口径（p48/p56），生产必须保持开启并按端口白名单放行；端口全表在 OTFC Features List，书内 p42 无数值
- 服务器资源推荐表书内无数值（p38 仅指针），sizing 结合 15000 用户/30 端口容量口径与 Features List 共同确定
- 安装语言有两项持久副作用（默认邮件通知 Profile 与 Basic Profile 封面语言），选错善后靠手工改默认 Profile
- 教材密码（123456/Alcatel1!@123/mtcl）全部是实验或出厂口径，生产必须整体替换；交付检查表含"默认密码已替换"
- 恢复场景的版本等同/拓扑一致前提与备份细节 → 备份升级运维能力；OXE 话路配置 → SIP 通道集成能力
