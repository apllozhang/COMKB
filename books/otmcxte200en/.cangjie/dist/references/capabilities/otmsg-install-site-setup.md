# OTMC 服务器安装与站点配置（介质/SUSE 安装/core/13 步向导）

## R — 原文依据

> "OpenTouch Messaging Center for Virtualized Infrastructure (15000 users): OTMC deployment in virtualized infrastructure"（p62）
> "check the system pre-requisites by launching the 'CheckSystemLinux.sh' script from a terminal console (script is available at DVD root)"（p66）
> "This post installation wizard is automatically started at the first boot of the OTMC server (after software installation)."（p70）
> "THE DNS MUST BE CONFIGURED TO RESOLVE (FORWARD AND REVERSE RESOLUTION)"（p73）

出处：OTMCXTE200EN p46-82（c01/c02、f08-f11、p04/p25、n01-n05 归并）。

## I — 自述

安装到站点配置是一条刚性链条，四段：

1. **物料与介质**：三张 DVD（SUSE 引导盘、OT core 包、FAX server）+ 许可文件 + 8770 侧物料 + 客户数据；介质两种制法——全 ISO 刻盘，或只刻 SUSE 引导盘、其余 ISO 拷 USB 硬盘（软件从 BPWS 下载）
2. **虚机创建与调优**：按 MyPortal 安装手册第 6.2 章建 OTMC-V（实验口径规格见 book/overview）；BIOS 禁用超线程 + ESXi 电源策略 High performance 两处调优
3. **SUSE 安装**：三个安装项都标 15000 users——硬件 GUI 版、虚拟化基础设施版（实验选此项）、OTMC first（单分区，放弃平滑升级）；勾 System clock uses UTC，约 25 分钟；root 出厂默认密码首登强制改
4. **core 安装与 13 步向导**：CheckSystemLinux.sh 查前置 → setup.bin 部署（约 30 分钟）→ 重启自动进向导

13 步向导关键规则：

| 步骤 | 硬规则 |
|---|---|
| 1.3 网络设置 | 主机名小写强制；DNS 前向+反向解析七类 FQDN（OTMC/8770/邮件/LDAP/OXE 呼叫服务器（按冗余模式三口径）/OXE H.323 网关）；NTP 放行 |
| 1.4 HA 参数 | 默认 Disable；启用需副服务器且两台同时跑向导（配置本身在书外） |
| 1.5 core 账户 | 五账户（root/maintenance/administrator/profile/SNMP）用户名互异且禁用保留名；密码 ≥8 字符且界面不校验 |
| 1.7 证书 | 课堂通用证书 + Network security OFF 属实验口径，官方明示不推荐 |
| 1.8 备份存储 | LOCAL/USB/NFS 三选一；虚拟环境必须外置 NFS；设置落盘 bics.conf |

## A1 — 书中案例

**装机与站点配置实验**（c01+c02，环境值见 book/overview）：

1. 按安装手册 6.2 章参数创建 OTMC-V 虚机并开机
2. BIOS Processor 选项禁用超线程；ESXi 电源策略设 High performance
3. 挂引导 ISO 从 DVD 启动，选"OTMC for Virtualized Infrastructure (15000 users)"
4. SUSE 设置：选键盘、时区并勾 System clock uses UTC；约 25 分钟完成后重启
5. 首登 root（出厂默认密码）按提示改新密码（实验口径值见 book/overview）
6. 录 IP 参数（网络管理员提供）并确认生成 IP 配置
7. 图形会话挂载 OT Core ISO，终端跑 DVD 根目录 CheckSystemLinux.sh
8. 前置通过后跑 setup.bin：接受条款、检查硬件、部署软件包约 30 分钟
9. 摘要屏后关机；重启自动进入 post-installation wizard
10. 向导：类型选 Installation from scratch；主机设置录键盘/国家/公司名/时区+D.S.T.
11. 网络设置：主机名（小写）、IP/掩码/网关/域/DNS/NTP；确认 DNS 前向反向解析清单就绪
12. HA 保持 Disable；core 五账户设密码（≥8 字符，界面不报错）并选默认语言
13. 许可服务器选 Local/External，许可文件 Browse 或 Skip（细节转 otmsg-license-management）
14. 证书页按课堂口径 Network security OFF 选 Yes（实验口径，生产禁止照搬）
15. 备份存储选 LOCAL（实验口径；生产虚拟环境必须外置 NFS）；Summary 核对、更新选 NO、Finish——OpenTouch 服务启动

## A2 — 未来触发

使用情境：新装 OTMC 物理机或虚机；首启向导怎么配；DNS 要解析哪些名字；站点账户怎么定；装完要改什么口径才能上生产。

语言信号：安装 / installation / SUSE / CheckSystemLinux / setup.bin / post-installation wizard / 站点配置 / 向导 / bics.conf / OTMC first / 单分区 / 超线程 / High performance。

与相邻能力区分：许可文件部署与核验归 otmsg-license-management；声明进 8770 归 otmsg-declaration-sync；部署形态选型见 otmsg-product-positioning（路由卡）。

## E — 可执行步骤

输入契约：ESXi/vSphere（虚拟化）或裸机就绪、安装介质与许可文件在手、DNS 管理权（能加正反记录）、网络参数与客户信息采集完成。DNS 管理权不在手 → 判停先找客户网络组。

1. 盘点物料：三张 DVD 或"SUSE 单刻 + USB 硬盘"制法，核对 8770 侧物料与客户数据。完成标准：介质与资料齐备
2. 服务器准备：按 MyPortal 安装手册定资源；BIOS 关超线程、ESXi 电源 High performance。完成标准：满足前置
3. 装 SUSE：按部署形态选安装项（虚拟化选 Virtualized Infrastructure；选 OTMC first 须客户确认放弃平滑升级）。完成标准：OS 可登录
4. 装 core：CheckSystemLinux.sh 通过后跑 setup.bin。完成标准：部署摘要屏出现，重启自动进向导
5. 跑 13 步向导：按"DNS 清单、账户、许可、证书、备份存储"的顺序逐页配置。完成标准：Finish 后 OpenTouch 服务启动
6. 验收：核对 bics.conf 生成与服务状态；许可核验转 otmsg-license-management。完成标准：站点配置可交付声明步骤

判停点：

- DNS 前向或反向解析缺项 → 停，先补 DNS 再继续（声明、通知、对接全踩在 DNS 上，n03）
- 生产站点照抄课堂口径（Network security OFF、本地备份、教材口令）→ 停，按生产基线整改（n04/n05）
- 向导许可页点 Skip → 安装不中断但 OTMC 不会正常工作，必须补装许可后再验收（n06）

输出契约：完成站点配置的 OTMC（bics.conf 落盘、OpenTouch 服务运行）+ DNS/账户/备份口径的交付记录。

## B — 边界

- HA 只留指针（p74 "explained in a dedicated chapter"），本书无 HA 配置内容；启用前置为副服务器 + 两台同时跑向导（n23）
- 虚机规格为实验口径（p58 Note 明说 only for lab purposes），生产参数以 MyPortal 安装手册 otmc2.6.1 第 6.2 章为准；硬件规格与上限外指 feature list / product limits
- RAID 与公司 DNS 必须安装前就绪（p52 Note 物理机口径）；p52 "Red Hat installation"、p53 "CheckSytemLinux.sh" 为原文笔误，以 SUSE 与 p66 拼写为准（nr-05）
- p75 密码不足 8 字符无报错弹窗、事后才出问题（n01）；用户名禁用 admin/adminnmc/htuser 等保留名（n02）
- 实验环境值（letacla1、OtmcV01*、letacla1234、maintenanceuser、Admin-8770、Admin-T1、adminsnmp、151.1.1.x 网段、otmc.company.com 等）一律不入正文，集中见 book/overview
