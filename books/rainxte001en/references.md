# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| Rainbow Network Requirements（help.openrainbow.com 文章 + 2 份 PDF，其一为健康数据托管版） | 端口/协议、域名 IP、带宽、DNS/Proxy/防火墙配置——生产网络前提唯一依据 | p36-40 |
| TC2479（OXE 为 TC2462） | Rainbow WebRTC Gateway with OXO Connect/OCE 的权威配置文档 | p123, p169 |
| Rainbow WebRTC cookbook（MyPortal，必须最新版） | OCE-FE 各 commissioning 场景（新装/加装/有无 Fleet 参考）的操作细节 | p135, p137 |
| 外部网关安装指南（Rainbow Support 网站 ALE equipments (PBX) 区） | VM/NUC 安装步骤与防火墙白名单 | p140, p144 |
| Features List / Rainbow plans（help.openrainbow.com） | 订阅功能矩阵与管理员角色权威对照 | p57, p65 |
| Help Desk Guide（help.openrainbow.com） | 排障指南/找日志/报障入口 | p183 |
| MFADTOTP 设置参考文章（支持站点） | TOTP 配置细节 | p53 |

## 2. 官方站点与工具

| 站点 | 用途 | 书内位置 |
|---|---|---|
| web.openrainbow.com | 网页客户端与管理入口 | p84, p103 |
| pilot.openrainbow.com | 连通性与承载容量评估（售前勘测） | p42；分区随版本演进（n03） |
| status.openrainbow.com | 云服务状态页 + Get updates 告警订阅 | p186 |
| developers.openrainbow.com | CPaaS 开发者门户 | p30 |
| MyPortal | 下载网关 VM/查 cookbook/开 SR（需 Rainbow 认证） | p135-144, p190-193 |
| support@openrainbow.com / Emily BOT / Global Welcome Center | SR 入口（认证伙伴才建 ESR） | p191 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g62（62 条）全部通过术语核验（16 个 OVERVIEW 候选术语逐条映射无遗漏，详见 glossary.md 收尾自检）。
- 落位口径：GLOSSARY.md 全量收录（按 concept/role/subscription/product/protocol/resource 六类分组）；阶段 3 生成 `book/glossary.md` 门户版（精选高频 30 条左右，保持第一本版式）。
- 12 个仅 passing 提及未单列的词（Rainbow Hub、bubble、REX、RUFUS、ESXi/OVF、Busy Lamp Field、OXO Connectivity、Global Welcome Center、SR/ESR、noreply@openrainbow、ITSP2）已在 glossary.md 收尾自检备查，不进主表。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- RLAB POD 网段 192.168.1.x：Client PC .10 / OXO .246 / 网关 .254 / DNS .250（DNS2 10.20.30.250）/ 话机 DHCP 池 .30-.39。
- OMC 出厂首连：192.168.92.246 + pbxk1064（仅首次）；OCE-FE FTR 地址 192.168.94.246，首连密码示例 Alcatel1。
- 实验账号：cCpP.admin@ale-training.com / Superuser-P*；SIP 模拟器 pbxP/alcatel；分机 100-104（IPDSP=104）；Twinset 副站 130/131/135、Anydevice 132/133。
- 培训禁用预付订阅（p66/p176）；实验邮箱服务器 mail44.lwspanel.com（PasswordP*）。
