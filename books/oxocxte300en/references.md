# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| TC1143 Security Recommendations for OXO Connect | 安全加固唯一依据：访问控制/密码策略/远程接入/系统配置/待处理安全项 | p94, p184, p327-329 |
| TC1284 Public SIP Trunking Interoperability | SIP 运营商兼容清单与支持流程；生产中继参数按对应运营商 TC | p199, p216 |
| TC1994 SIP Easy Connect: SIP Trunk Profile Import/Export | SIP Profile 导入导出的权威文档 | p216 |
| TC2479（OXE 为 TC2462） | Rainbow WebRTC Gateway with OXO Connect/OCE 的权威配置文档 | p368, p414 |
| Rainbow WebRTC cookbook（MyPortal，必须最新版） | OCE-FE 各 commissioning 场景与新装/加装/低版本 PBX 分支 | p382 |
| 8328 SIP-DECT SINGLE BASE STATION – System Guide | 8328+8214 课堂/小型部署的设备文档 | p454 |
| 模拟-SIP 网关部署指南（MyPortal） | MEDIA5 4102/C710/C711 接入 OCE 的安装细节 | p104 |
| Expert Documentation（SECURITY 章等） | 与 TC1143 并列的安全章节依据 | p329 |

## 2. 官方站点与工具

| 站点 | 用途 | 书内位置 |
|---|---|---|
| MyPortal | 下载 OMC/软件三件套/DBAdapter/SIP Profile/网关 VM 与 ISO/cookbook | p63, p306, p318, p389-390 |
| BPWS | TC1143 等 TC 文档获取渠道 | p329 |
| web.openrainbow.com | Rainbow 网页客户端与管理入口（取 PBXID/激活码、建成员、订阅） | p345, p352, p420 |
| hub.openrainbow.com | Rainbow 门户 | p332 |
| help.openrainbow.com | Features List / Administration 角色细目 | p340 |
| eBuy | ARI 唯一值获取（IBS 与 IP-DECT 通用） | p119 |
| 8328 Web Admin（https://<基站 IP>） | SIP-DECT 基站管理（默认 admin/admin，实验口径） | p456 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g46（46 条，六类）全部通过术语核验（BOOK_OVERVIEW 18 个关键术语逐条映射无遗漏，详见 glossary.md 收尾自检）。
- 落位口径：GLOSSARY.md 全量收录（按 concept/role/subscription/product/protocol/resource 六类分组）；阶段 3 生成 `book/glossary.md` 门户版（精选高频 28 条左右，保持第一本版式）。
- 缩写全称纪律：书中给出展开的（FTR/MSDB/eMMC/NUC/SBC/CE/UTL/UCaaS/CPaaS）如实登记；未给全称的（OMC/HSL/ARS/DDI/ARI/GAP/IPUI/IPEI/RGM/RSL 等）一律标注"书中未展开"，不采信外部知识。
- 仅 passing 提及的词（ITSP2、RUFUS、ADPCM 转换细节、OmniVista 8770 告警上报链、PIMphony 版本矩阵）在 book/glossary 备查段登记，不进主表。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- RLAB POD 网段 192.168.1.x：Client PC 192.168.1.10 / OXO Eth0 192.168.1.246 / OCE Eth1 192.168.94.246 / 网关 192.168.1.254 / DNS1 192.168.1.250、DNS2 10.20.30.250 / 话机 DHCP 池 .10-.69（分实验 .10-.30 或 .30-.39）；公共区 10.20.30.x（NAS/SIP 模拟器 12.0.0.2/外部 DNS .250）。
- OMC 出厂首连：192.168.92.246 + pbxk1064（仅首次）；FTR 页面 192.168.94.246、首连密码示例 Alcatel1；Webdiag 登录 installer。
- 实验账户密码表（p45）：Attendant Letacla1 / Administrator Qwerty12 / Installer Alcatel1 / Download Oxopb123 / NMC Pbxnmc12 / ACD Acdc1064 / Users 142535——全部为实验口径，生产严禁沿用。
- SIP 模拟器：pbxP/alcatel（P=POD 号）；SIP 域 sip.itsp1.fr；DDI 41100-41199、话务员 41000、安装号 210P41000（尾段两口径见 needs-review nr-02）；ARI 11000436010-…60（POD1-6）；8328 管理界面 admin/admin；DECT PIN/AC 0000。
- Rainbow 实验账户：cCpP.admin@ale-training.com / Superuser-P*；培训邮箱 mail44.lwspanel.com（PasswordP*）；培训禁用 PREPAID 订阅（p421）。
- 实验编号：分机 100-104（IPDSP=104）、hunt 501（500 被 VM 占用）、Twinset 副站 130/135、Anydevice 133、广播组号 *2。
