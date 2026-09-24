# Book Overview（参考区）— OpenTouch Fax Center

> 供能力卡引用的背景参考；源自 references.md 落位。

## 交付主线四步（全书组织轴）

准备服务器 → 软件安装 → First Time Setup Wizard（首站点）→ 客户端安装与初始设置（p46）。之后接两大外部集成（OXE 话路 + 邮件通道），最后进入服务运维/备份升级/报表监控的运维纵深。课程十段排布：概览、关键概念、架构、安装与基础配置、客户端、用户与管理员、Profile 与电话簿、OXE 集成、SMTP 集成、服务与维护。

## 实验环境（仅 Boundary 背景）

- 实验生态（p45）：传真服务器 fax.company.com = 192.168.1.60；邮件 mail.company.com = 192.168.1.100；AD+DNS eco.company.com = 192.168.1.100；OXE oxe.company.com = 192.168.1.3；域 company.com。
- 安装口径（p49）：OTFC IP 192.168.1.60；传真网关主机名 fax；系统管理员 administrator，临时密码 123456，首登改 Alcatel1!@123（12 字符）。
- FTW 口径（p50/p68-70）：站点 My Organization（实验页拼写 My Organisation）；管理员邮箱 baker@company.com；首用户实验页 baker@company.com（讲义页 p50 写 barkley@company.com，两页不一致）、临时密码 123456。
- 测试账号（p116）：allen@company.com 传真号 31604、barkley@company.com 传真号 31600，密码 Alcatel1!@123；备份管理员 backupadmin。
- OXE 侧（p152/p155）：mtcl/mtcl 默认账号；用户目录号 #31600-31699；双网关示例号段 GW1 1200-1500、GW2 3300-3800（p36）。
- MySQL（p231）：mysql5 服务；数据目录 C:\Program Files\MySQL\MySQL Server 8.0\Data；注册表键 HKEY_LOCAL_MACHINE\SOFTWARE\Interstar Technologies。
- 培训特有做法：关三 Profile 防火墙（p56）、客户端装在传真服务器且忽略重启（p115/p132）、Office 已预初始化（p56）——生产一律不照搬。

## 方案速览（售前沟通素材）

- 定位：纯软件 FoIP 传真服务器，与 OXE 交互且独立部署；单专用服务器上限 15000 用户、30 端口（p7）。
- 传输：SIP/TCP 与 SIP/TLS（能力项）；T.38（含 Group 3）最高 14.4kbps，G.711 透传最高 33.8kbps（p7）。
- 入口：发送四类入口（邮件/Web/虚拟打印机/SendFAX 与 T.37 MFP）+ 定时发送；接收四类去向（邮箱 PDF/TIFF、Web 界面、打印机、文件夹）；入局路由 DNIS/CSID/ANI/DTMF（p8-9）。
- 合规：GDPR/HIPAA/FERPA/SOX 语境、敏感文档定向路由、可配零保留、自动事件日志（p6）。
- 概念模型：System ➤ Site（隔离的虚拟传真服务器）➤ User（SMTP 地址标识）➤ Profile（策略模板，Basic/No Faxing Rights 默认两档）（p22-24, p118）。
- 服务架构：9 服务分有状态复制（Manager/ConfigManager/CoConfig/FaxArchive/FaultTolerance）与无状态负载均衡（Driver/Rasterizer/SMTP/XML Gateway）（p179）。

## 教材口径声明

- 全部实验密码/账号/网段/号段仅限实验环境；生产必须整体替换（交付检查表含"默认密码已替换"）。
- 生产化边界三文档：OTFC Features List（端口全表/45 格式/浏览器/资源 sizing/许可特性）、TC3048（OXE-OTFC SIP 互通参数）、The XM Fax SMTP Gateway（Installation guide 章节，p183）——均为原书指定或明示的权威来源。
- 版本敏感点：Outlook "2022" 为原文笔误（p41）；XMSMTPGateway/XMSmtpGateway 两种写法并存；p148 停止命令行 "traced" 字样为混排笔误（killall mtracer 本身正确）。
- HA 与 TLS：XMFaultTolerance 仅组件介绍、SIP/TLS 仅概览提及，部署与启用路径书内为零——客户问及转产品文档/专业服务。
