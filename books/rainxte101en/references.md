# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| Rainbow Network Requirements（help.openrainbow.com 文章 23942019777170 + 两份 PDF，其一为健康数据托管版） | 端口/协议、域名 IP、带宽、DNS/Proxy/防火墙配置——Hybrid 与 Hub 通用的生产网络前提唯一依据 | p37, p39, p41 |
| Features List / Rainbow plans（help.openrainbow.com） | 订阅功能矩阵与管理员角色权威对照（订阅表为 Sprint 170/Ed16 口径） | p8, p67 |
| TBE099_Rainbow Hub - Voice services | 话音服务细节与 CDR 获取（REST API 等）权威文档 | p318 |
| TBE127 | Rainbow Hub DECT 方案介绍（分伙伴/ALE 员工两个链接） | p154 |
| 认证 SIP 运营商清单（help.openrainbow.com） | Cloud PBX 的 trunk 接入只认清单内运营商 | p7, p78 |
| Generic SIP 互接支持文章（"Setting up Rainbow Hub to interconnect third-party SIP extensions"） | 第三方终端侧配置细节 | p117 |
| 8 款参考设备配置指南（Yealink/Snom/Poly/Grandstream） | 已验证部署的参考配置（无官方互操作认证计划） | p122 |
| SSO 配置技术手册 / MFA-TOTP 配置文章（支持站点） | SSO 与 TOTP 具体配置步骤 | p54 |
| LDAP 连接器部署细节（支持网站） | 连接器安装与三功能配置 | p179 |
| Help Desk Guide（help.openrainbow.com） | 排障指南/找日志/报障入口 | p331 |

## 2. 官方站点与工具

| 站点 | 用途 | 书内位置 |
|---|---|---|
| web.openrainbow.com | 管理与使用统一入口（BP/客户管理员全流程 + 话务台） | p13, p72, p288 |
| help.openrainbow.com | 支持站点：Features List、Network Requirements、认证运营商、Help Desk Guide | p8, p37, p78, p331 |
| pilot.openrainbow.com | Rainbow Pilot 连通性与承载评估（售前勘测；分区随版本演进 n02） | p43-44, p136 |
| status.openrainbow.com | 云服务状态页 + Get updates 告警订阅 | p338 |
| rdd.openrainbow.com | zero-touch 管理 URL（DHCP option 43/66/67 无法禁用时的唯一合法指向） | p136 |
| MyPortal | 开 Service Request（两页表单，Product Category=Rainbow Hub） | p342-343 |
| support@openrainbow.com / Emily BOT / Global Welcome Center | SR 入口（仅认证 Rainbow Hub 伙伴建 ESR） | p341 |
| ALE Knowledge Hub（enterprise-education.csod.com） | 培训评估/证书（培训行政，非技术） | p347-351 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g70（70 条：概念 29 + 角色 6 + 订阅 8 + 产品 11 + 协议 8 + 资源 8）全部通过术语核验——BOOK_OVERVIEW 17 行术语逐条映射无遗漏（详见 glossary.md 收尾自检）。
- 落位口径：GLOSSARY 全量收录（六类分组）；阶段 3 生成 `book/glossary.md` 门户版（精选高频 40 条左右，保持第一本版式）。
- 仅 passing 提及未单列的词（DND、PoE、ATA gateway、PTI、SBC/VPN、EM20、bubble 泛指义等）已在 glossary.md 收尾自检备查，不进主表；FTR/UTL/WebRTC 网关等混合云语系概念本书无，勿混入。
- 同词两义提示：TOTP 既是认证方式（p54）也是设备 debug 一次性口令的机制标注（p142/p335）——按上下文区分（g06）。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- 每 POD（1-6，特殊 8）一家训练公司 Client-PX：BP 账号 bpX.rv1@ale-training.com（密码问讲师）；客户管理员 aliceX；成员 alice/bob/carol/dave X（内线 101-104、公网号 02982967X1-X4）；公司公网号段 02982967X0-X9（X0 主号，实验口径）。
- 实验密码口径：成员 Superuser-P*、培训邮箱 mail44.lwspanel.com 为 PasswordP*（均实验口径）；平台邮件可能被判 SPAM（p192）。
- MicroSIP 公网模拟：每 POD 两个预配软话机（账号按 332982900P1/331409500P1/336050400P1/442056700P1 规则）；模拟器不能按公网号呼本公司成员；训后必须删除（p13/p20/n56）。
- RLAB 远程实验室（可选）：Client1 192.168.1.10/24、网关 192.168.1.254、DNS 192.168.1.250、NAS 12.0.0.2（实验口径）。
- 培训订阅口径：每公司仅 4 条 Voice Enterprise MONTHLY、禁用 1/3/5 年预付（p17/p68/p74 三处警告）；生产预付正常（p65）。
