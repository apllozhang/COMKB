# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| Rainbow Network Requirements（help.openrainbow.com 文章 + 2 份 PDF，其一为健康数据托管版） | 端口/协议、域名 IP、带宽、DNS/Proxy/防火墙配置——生产网络前提唯一依据 | p26-31 |
| TC2462（OXO 为 TC2479） | Rainbow PBX integration with OmniPCX Enterprise 权威配置指南：远程延伸、共享网关、网关部署维护、话务台各章反复指向 | p121, p149, p154, p162, p194, p232 |
| TBE067_Rainbow - WebRTC Gateway Pres&Sizing（Excel 工具包，ed06l） | 网关容量估算：四输入、通道数、OXE 压缩器推算；适用 OXE 101.0 MD3 / WebRTC 3.x 起 | p151 |
| WebRTC Gateway Installation Guide / Command List / Upgrade Guide（MyPortal） | 网关安装、命令清单、升级操作细节 | p153 |
| 支持网站文章 23160518410898（远程升级）/ 23159902243218（手动升级）/ 15470672923794（升级失败处理） | 网关升级三篇操作文章 | p173-176 |
| VoIP calling Troubleshooting guide（support.openrainbow.com） | 网关与话音深排障（OXE 侧维护命令之外的第二层） | p194 |
| Features List / Rainbow plans（help.openrainbow.com） | 订阅功能矩阵与管理员权限权威对照 | p24, p48 |
| Help Desk Guide（help.openrainbow.com） | 排障指南/找日志/定位问题/报障流程 | p246 |
| MFATOTP 设置参考文章（支持站点） | TOTP 双因子配置细节 | p44 |

## 2. 官方站点与工具

| 站点 | 用途 | 书内位置 |
|---|---|---|
| web.openrainbow.com | 网页客户端与管理入口 | p61 |
| pilot.openrainbow.com | 连通性与承载容量评估（售前勘测）；分区随版本演进 | p33 |
| status.openrainbow.com | 云服务状态页 + Get updates 告警订阅（按主题/地域过滤） | p249 |
| developers.openrainbow.com | CPaaS 开发者门户 | p21 |
| MyPortal | 下载网关 VM（Taxonomy 下 OXE/OXO/OXO CE 同一软件）、TC2462、TBE067、升级包、开 SR | p153-154, p174, p255 |
| support@openrainbow.com / Emily BOT / Global Welcome Center（ALE.WelcomeCenter@al-enterprise.com） | SR 入口（仅 Rainbow 认证伙伴建 ESR） | p254 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g66（66 条：concept 25 / role 9 / subscription 8 / product 8 / protocol 7 / resource 9）全部通过术语核验（OVERVIEW 17 个候选术语逐条映射，详见 glossary.md 收尾自检）。
- 落位口径：GLOSSARY.md 全量收录（按六类分组）；阶段 3 生成 `book/glossary.md` 门户版（精选高频约 45 条，保持第一本版式）。
- CSTA/OMS/GD/ITSP/NPD/ESR/TFTP 等缩写书中未给全称，full_name 如实省略，不采信外部知识；bubble 为口语提法仅 p43 一处，不进主表。

## 4. 实验环境口径备查（仅作 Boundary 背景与 book/overview 素材，不进能力卡正文）

- RLAB POD 结构：每 POD 6 台实例（OXE csa/csm、OMS、FlexLM、WebRTC 网关、PC Client 10/11）+ 公共资源区（NAS、SIP 模拟器 10.20.30.2 段、外部 DNS 10.20.30.250）。
- 关键实验值：OXE CS 主 IP 192.168.1.3、WebRTC 网关 192.168.1.15、Pod 网关 192.168.1.254、内部 DNS 192.168.1.250；网关账号 rainbow/Rainbow123；培训管理员/成员账号 cCpP.admin / cCpP.user1 / cCpP.user2@ale-training.com（Superuser-P*）；培训邮箱 mail44.lwspanel.com（PasswordP*）；SIP 模拟器注册账号 pbxP/alcatel。
- 实验分机与编号：IPDSP 31000（PC Client 10）/ 31001（PC Client 11）、4059 关联话机 31002、Ghost Z 建议 DB1000、REX 编号 21<主号 QMCDU>、留言信箱示例 31499、个人话务呼叫前缀 31401；ITSP1 DDI：首外部号 3321PN41000、首内部号 31000、范围 500（PN=两位 POD 号）。
- 网关软件样例版本 1.78.11-470、rainbowagent 6.0.1、mpshow 默认输出（WRTRANGE 20000-29999 / SIPRANGE 30000-39999 / TURN_SERVER=GEOIP / RINGINGAUTO=true）——均为书中样例值，引用标"实验口径"。
- 培训订阅口径：只用 Voice/Attendant MONTHLY，禁用预付（p57/p239，实验口径 n03）。
