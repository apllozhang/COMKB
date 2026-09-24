# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| TC2341 — Deployment Guide for OTC smartphone in Voice over IP for Connection Users | OTC 智能手机 VoIP 部署的生产化权威文档 | p147 |
| TC2391 — New Unified Messaging implementation | UM 实现（含 Impersonation/Delegation 细节） | p190 |
| TC2258 ed.02（2019，整篇附录收录） | Calendar Presence & Calendar Synchro 机制、展示规则与排障 | p400-414 |
| TC2558 | 本地存储邮箱用户的日历特性配置（UM 上下文之外的另一套流程） | p395 |
| TC1623 — Single Sign-On Kerberos in-deep | Kerberos SSO 深入参考 | p436 |
| Windows CA / 外部 CA（Certisign、VeriSign 等） | 证书签发生态（书内实验用 eco 服务器 CertSrv） | p112-116 |
| FreeRADIUS.net 1.0.5（Windows 移植版） | RADIUS 实验服务器（生产另选企业级实现） | p462-467 |
| OT release note（书中明示"以最新版为准"） | DCS 兼容矩阵、APNS 证书等时效性口径 | p371, p98 |

## 2. 官方站点与工具

| 站点/工具 | 用途 | 书内位置 |
|---|---|---|
| enterprise-education.csod.com | ALE 培训目录站点（查培训路径与课程详情） | p468 |
| emea.education-services@al-enterprise.com | 教材反馈邮箱 | p468 |
| Google Play / App Store | OTC Mobile（OpenTouch Conversation / Conversation Plus）分发渠道 | p143, p145 |
| Google 市场 "ALE NFC Extended Mobility Administration" | NFC 标签写卡工具（Android R4.2+） | p159 |
| ALE NFC 标签 Ref 3BA27856AA（100 张装） | 官方推荐标签；自购须 NFC Type 2 且 BP 验证 | p160 |
| the-qrcode-generator.com 等第三方生成器 | QR 码制作（按固定 JSON 语法） | p165 |
| RLAB 门户 | 虚机启动与培训实验环境入口 | p5, p25 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g58（58 条）全部通过术语核验（BOOK_OVERVIEW 术语表 22 行逐条映射无遗漏，详见 glossary.md 收尾自检）。
- 落位口径：GLOSSARY.md 全量收录（按 concept/subscription/product/protocol/resource 五类分组）；阶段 3 生成 `book/glossary.md` 门户版（精选高频约 30 条，保持模板版式）。
- 仅 passing 提及未单列的词（MLE、SEPLOS、My IC Phone 8082/8088、80x8/80x9/8001/81x8/4135 话机型号、MIX484 GD4 课堂硬件、Squirrel/DM、LightLine、netadmin -m option 17、Blue Coat/NGINX、TightVNC、S.O.T.、Certisign/VeriSign、Skype4B/Lotus Notes、ITSP2）已在 glossary.md 收尾自检备查，不进主表。
- 缩写纪律：书中未展开全称者（MLE/OMS/OTMS/DISA/DDI/REX/DTMF/NOE/TFTP/UTL 等）full_name 一律省略，不做外部补全；书内给全称者（UDAS/ACS/APNS/AMS/EWS/DSU/DSS/SBC/MASC/KDC/TGT/SPN/PRS）如实记录。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- POD 服务器设置（p9，实验口径）：OXE csa/csm（IP 原文印作 192.16.8.1.1/.3，见 nr-04；账号 mtcl、swinst/SoftInst、root/letacla）、OMS 192.168.1.13（root/letacla1）、OpenTouch 192.168.1.50（root/superuser）、8770 192.168.1.70（adminnmc/Superuser01*）、DCS 192.168.1.31 与 ECOSYSTEM 192.168.1.100（Administrator/superuser）、PC Client 10/11 = 192.168.1.10/.11；掩码 255.255.255.0、网关/DNS 192.168.1.254。
- ITSP1 模拟器（p20-23）：SIP 网关 gateway1.itsp1.com（10.20.30.51，账号 pbxP/alcatel，域 sip.itsp1.fr）、公网网关 public.itsp1.com（10.20.30.50）；号码规则 PN=两位 POD 号——国内 33[1-5]1PN12345（主号 3321PN12345）、移动 3361/3371PN12345、英国 4421PN12345、紧急 112/15/17/18；DDI 首外线 41000、首内线 31000、范围 500。
- WebAdmin/CA/UM 实验（p45 口径）：WebAdmin otAdmin/admin8770；CA https://eco.company.com/CertSrv（administrator/superuser）；特权账号 ICEaccess/iceaccess（密码永不过期）；Outlook 实验 barkley/1234；DCS 虚机 Administrator/superuser；AD 目录访问 directory@company.com/directory；Kerberos ice_kerb 密码 1234；FreeRADIUS shared_secret training；tsa_maintenance 秘密码 2998。
- 实验人物：Barkley 31000 / Backman 31001 / Boop 31002；Nomadic 池 31017-31019（Ghost Z）与 31951/31952（SIP 设备）；会议桥 31250（EN）/31260（FR）；留言号 31200；Extended Mobility 实验需学员自带手机与教室 6 SSID 热点（p163）。
- 明文密码为 2019 年培训文化产物：生产必须全部替换并纳入安全基线（n49），环境值只进 Boundary 与 book/overview。
