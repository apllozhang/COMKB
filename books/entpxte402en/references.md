# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| TBE043（Virtualization Design Guide） | OXE-V 平台/许可设计的权威文档；Ed12 矩阵演进后以它为准 | p134, p149 |
| TC2456（S.O.T. Release Note） | SOT 版本兼容权威对照 | p24 |
| TC3104en-Ed08（Migration guide to OXE R101.x） | N3 以下版本迁移的唯一执行指南 | p78 |
| TC3138（Installation of a GAS server on Rocky Linux） | GAS 安装权威文档 | p242 |
| TC3142en-Ed01（OXE deployment on AWS） | AWS 部署指南 | p149 |
| TBE063（OmniPCX Enterprise & Generic Appliance Server） | OXE 与 GAS 关系、legacy 迁移背景 | p228 |
| TBE067（Rainbow WebRTC gateway presentation） | GAS 内嵌 WebRTC 网关参照 | p225 |
| 8AL91032ENBD（OXE 101.1 安装手册） | OXE 安装细节 | p149, p242 |
| TC0000_GAS_migration（占位件号，见 nr-04） | GAS 迁移、WebRTC GW 配置参照 | p230 |
| Starter 课程（OXE 数据库管理） | 用户/路由/编号计划等业务配置——本书明确书外 | p92 |

## 2. 官方站点与工具

| 站点 | 用途 | 书内位置 |
|---|---|---|
| myportal.al-enterprise.com | 下载 SOT/OXE/模板/BootDVD、查 TBE/TC 文档、C2P 网页、B2B eCommerce、Asset & service manager 下载 PoD 许可（项目须 Active） | p62, p149, p237, p376, p381-385 |
| connect2.opentouch.com | Cloud Connect/RTR 固定目标 FQDN（443 XMPP/WSS + 80 SOCKS5） | p290, p314, p320 |
| cdn-oxe-sw-update.al-enterprise.com | Fleet Dashboard 软件更新 CDN 仓库（信任主机须放行） | p347 |
| businessportal.al-enterprise.com | Cloud Connect Terms & Conditions（FTR 前置应答） | p329, p392 |
| enterprise-education.csod.com | ALE Knowledge Hub 培训评估入口（不入知识条目） | p411 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g62（62 条）全部通过术语核验（BOOK_OVERVIEW 20 个候选术语逐条映射，全部为"正文有明确定义"，无排除项，详见 glossary.md 收尾自检）。
- 落位口径：GLOSSARY 全量收录（concept/role/subscription/product/protocol/resource 六类分组）；阶段 3 生成 `book/glossary.md` 门户版（精选高频条目，保持第一本版式）。
- 仅 passing 提及未单列的词（OTEC、OST64/EEGW、GD4/GA4/MR1/SLI16/UAI16、ALES/IPDSP、ZUORA/SAP/eBuy、ELP、PBWS、DCO/CCO、SIP Simulator/ITSP、"Delivery note"）已在 glossary.md 收尾自检备查，不进主表。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- RLAB POD 网段 192.168.1.0/24：网关 .254、DNS .250、NTP .252、代理示例 .253:3128、NAS 与 SIP 模拟器 12.0.0.2；PC Client .9、SOT VM .130（hosted .230）、CS3 csa .101 / csm .103、KVM host .55（OXE .201/.203、OMS .213）、GAS .45（OXE .1/.3、OMS .13、WebRTC VM .15）。
- 培训口令：Superuser2580*（OXE/SOT 四账户改后值）、letacla（SOT/OMS 出厂）、letacla1（GAS/OMS 出厂）、rainbow/Rainbow123（WebRTC VM）、ESXi root/Superuser-X*（X=POD 号）；SOT 媒体通道 upload/sot（FTP/SFTP 2222）。
- 路径口径：OXE swk 恢复 /usr4/BACKUP/OPS；FlexLM 许可 /opt/Alcatel-Lucent/data/licenses；GAS 备份 /var/backup；GAS 加载约 60 分钟、后安装约 15-20 分钟（培训环境实测口径）。
