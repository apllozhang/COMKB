# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| Feature list / Product limits document | 硬件与软件规格、产品上限、TUI 密码策略默认值的唯一权威出处 | p10, p13, p48 |
| OTMC 安装手册 otmc2.6.1_im_InstalManual_8AL90120USAH_1_en（MyPortal） | OTMC-V 虚机生产部署参数（第 6.2 章）与安装细节 | p58 |
| TC1652 | OXE 空间冗余站点为外置语音邮件系统声明 SIP 网关的专项配置 | p105 |
| TC2024（Business Portal 可取） | 在 8770 服务器上部署 NFS server（虚拟环境备份回收）的实施步骤 | p246 |
| Quick Reference Guide（"Managing your welcome greetings message" 章） | 用户问候语管理细节 | p142 |
| OpenTouch Capacity Planning Tool（OTMC 专用） | 扩容/压缩/站点占比评估（工具用法书外） | p19 |

## 2. 官方站点与资料入口

| 入口 | 用途 | 书内位置 |
|---|---|---|
| MyPortal | 取 OTMC 安装手册 | p58 |
| BPWS | 下载安装软件 ISO（全称书中未展开） | p50 |
| Business Portal | 取技术通报 TC2024 | p246 |
| enterprise-education.csod.com | ALE 培训目录（Find a Course，查后续课程如 HA） | p259 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g46（46 条，concept 15 / role 4 / subscription 2 / product 11 / protocol 8 / resource 6）全部通过术语核验（BOOK_OVERVIEW 19 个候选术语逐条映射无遗漏，详见 glossary.md 收尾自检）。
- 落位口径：阶段 3 生成 `book/glossary.md`（六域全量表格，保持模板版式）。
- 仅 passing 提及未单列的词（OTID、alchostid.cfg、ESS/ICS/ACS/FAX/MOH、ICE_*、EVS/FWK、OAM&P/UDA/MS、SEPLOS、OTC PC/one number、RUFUS、D.S.T.、START TLS/RFC 2595、VAA）已在 glossary.md 收尾自检备查，不进主表。
- 缩写纪律：PRS/VPIM/ICE/OMS/BPWS/ALUID（有定义无全称）/OTID/OAM&P/UDA/MS/EVS/FWK/MLE/DPNSS/VAA/flex-lm 等书中未给全称者一律不补外部释义。

## 4. 实验环境口径备查（仅作 Boundary 背景与 book/overview 素材，不进能力卡正文）

- 拓扑：ESXi 主机 esxi.company.com = 151.1.1.250/24（GW 151.1.1.254），DNS 域 company.com；六虚机——OTMC otmc.company.com=151.1.1.60、FlexLM flex.company.com=151.1.1.80、OmniVista 8770 nms.company.com=151.1.1.70、OXE-V（csa=151.1.1.1 / csm=151.1.1.3，节点 oxe）、OMS oms.company.com=151.1.1.13、Eco-System eco.company.com=151.1.1.100（DNS/Exchange/AD/LDAP/DHCP 五角色）；客户端 PC client=151.1.1.10；另 gd.company.com=151.1.1.12。
- 口令（实验口径）：SUSE root 默认 letacla1 → 首改 OtmcV01* → 向导 root=letacla1234；maintenance=maintenanceuser；administrator（otAdmin）=Admin-8770；profile（otProfile）=Admin-T1；SNMP=adminsnmp；Eco-System 六用户（alban/adams/adore/barkley/backman/boop）密码均 1234；话机 set secret code 默认 0000；OXE FTP 账户 adfexc/adfexc。
- 业务示例值（实验口径）：Connection 用户 Brad Barkley/Billy Backman/Betty Boop，分机 31000/31001/31002；IP 话机示例分机 61020；DPNSS 前缀 D1234；SMTP=eco.company.com:25；spadmin 读数 173:1/10、174:1/10、176:1/15、177:4/15、316:1/30、317:2/30。
- 声明章示例漂移（nr-02）：p92/p94 nslookup 用 155.1.1.x 网段（DNS 155.1.1.100），反查 .50 返回 .60——仅示意。
- OTMC-V 虚机规格（实验口径，p58）：SUSE 12 64 位、1 虚拟插槽/4 核/4GB 内存/E1000 网卡/250GB 精简置备。
