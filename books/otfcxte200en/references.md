# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| OTFC Features List | 端口使用表、45 种支持文件格式清单、浏览器支持、服务器资源推荐、许可特性清单——全书至少五处重复 "Always refer to the OTFC features list"，生产化唯一数值依据 | p18, p38, p41, p42, p79 |
| TC3048（Technical Communication 3048） | OXE-OTFC SIP 互通的权威操作文档，覆盖 OTFC 侧 SIP、OXE 侧 SIP、维护三块；OXE 侧网关参数细节一律以它为准 | p141, p147 |
| The XM Fax SMTP Gateway（Installation guide 章节） | SMTP 与邮件服务器的特定部署/配置细节（p183 原文明示） | p183 |
| OmniVista 8770（Network Management & Billing） | OXE SIP 网关的替代管理界面 + 传真计费取票出报表 | p152, p212-213 |
| BIRT Report Designer（安装包 3rd\birt 内 zip） | 自定义 31 个报表模板（Eclipse 报表设计器，工具本身在书外） | p226 |
| Wireshark | OXE 侧网络抓包文件分析（FTP bin 模式取回 .pcap，可按 SIP 过滤） | p150 |

## 2. 书内关键站点与工具落位

| 站点/工具 | 用途 | 书内位置 |
|---|---|---|
| FaxCenter\Bin\Util（xmsc / FirstTimeSetup.exe） | 服务启停（-ra/-oa/-aa）与事后重跑 FTW 向导 | p67, p188, p218, p231 |
| FaxCenter\Trace 目录 | 全部组件日志（ConfigManager.log / Smtp.log 排障高频） | p189, p208, p225 |
| ClientRedistribution 文件夹 | 精简客户端包（无管理工具）批量分发 | p84 |
| 3rd\birt 文件夹 | BIRT 报表设计器安装包 | p226 |
| Microsoft Download/角色源（Server Manager） | IIS 角色与四个角色服务安装 | p57 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g57（57 条，六类：concept 20 / role 3 / subscription 3 / product 12 / protocol 13 / resource 6）全部通过术语核验（BOOK_OVERVIEW 16 个候选术语逐条映射无遗漏，详见 glossary.md 收尾自检）。
- 落位口径：阶段 3 生成 `book/glossary.md` 门户版（精选高频约 30 条，保持第一本版式，六域分组）；全量 57 条以 candidates/glossary.md 为审计基准。
- 缩写纪律：书内给出全称的记 full_name（FoIP/NDR/IIS/MFP）；未给全称的一律不编造（DNIS/CSID/ANI/DDI/ARS/MLE/SMB/CSGD/MMC/BIRT 等），括注处已标"（推断）"——见 needs-review nr-03。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- 实验生态（p45）：传真服务器 fax.company.com = 192.168.1.60；邮件服务器 mail.company.com = 192.168.1.100；AD+DNS eco.company.com = 192.168.1.100；OXE oxe.company.com = 192.168.1.3；实验域 company.com。
- 安装口径（p49/p59-65）：OTFC IP 192.168.1.60；传真网关主机名 fax；系统管理员 administrator，临时密码 123456，首登改 Alcatel1!@123（12 字符）。
- FTW 口径（p50/p68-70）：站点名 My Organization（p68 实验页拼写 My Organisation）；管理员邮箱 baker@company.com；邮件服务器 mail.company.com；首用户 p70 为 baker@company.com（p50 讲义页为 barkley@company.com，见 nr-01）、临时密码 123456。
- 测试账号（p116）：Alexandra Allen / allen@company.com / 传真号 31604；Brad Barkley / barkley@company.com / 传真号 31600；密码均为 Alcatel1!@123；备份管理员 backupadmin。
- OXE 侧（p152/p155）：mtcl/mtcl 默认账号；用户目录号 #31600-31699；双网关示例号段 GW1 1200-1500、GW2 3300-3800（p36）。
- MySQL（p231）：mysql5 服务；数据目录 C:\Program Files\MySQL\MySQL Server 8.0\Data；注册表键 HKEY_LOCAL_MACHINE\SOFTWARE\Interstar Technologies。
- 培训环境特有做法：关闭本地三 Profile 防火墙（p56）、客户端装在传真服务器上且忽略重启提示（p115/p132）、Office 已预初始化（p56）——生产一律不照搬。
