# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| TC2005 + 运营商附加文档 | SIP 运营商接入参数的唯一生产依据（REGISTER 行为、号码格式、P-Asserted-Identity、SIPS 强制等） | p349 |
| TC2957 Quick steps deployment guide | ALE SoftPhone Remote Worker 配置的 OTSBC 侧权威口径 | p411 |
| Server deployment Guide for Remote workers | VPN 网关兼容清单与 VPN 远程部署细节 | p412 |
| EDS user manual | 零touch 部署与 EDS Profile 管理细节 | p405 |
| OXE Features List | 终端功能矩阵与许可功能的最终口径 | p72, p105, p147 注 |
| Starter 课程教材 | 防火墙信任主机、NOE 开通等前置基础（书内四处回指） | p38 注等 |
| AudioCodes 文档（Mediant 平台） | OTSBC 向导模板、CLI 语法与 SBC 高可用/容量 | p345, p369 |
| Wireshark / Filezilla | pcap 分析与 trace 取回工具（用法书内仅入门） | p316-318 |

## 2. 官方站点与工具

| 站点 | 用途 | 书内位置 |
|---|---|---|
| MyPortal | 下载 OTSBC 部署软件（OVF/ISO） | p365 |
| admin.eds.al-enterprise.com（开户 /register） | EDS 管理入口与账号申请 | p405 |
| device.eds.al-enterprise.com | 话机内硬编码的 EDS FQDN | p405 |
| help.ale-training.com 等培训资源（NAS 课件） | 实验配套（SIP Carrier Simulator 文档等） | p42 |
| ldapexplorertool.exe（NAS） | 实验用 LDAP 目录浏览器 | p219 |

## 3. 书内点名的 RFC 清单（协议断言溯源用）

| RFC | 用途 | 书内位置 |
|---|---|---|
| RFC 3261 | SIP 基线标准 | p45 |
| RFC 3325 | P-Asserted-Identity（外部网关按对端支持决定 From 匿名形态） | p354 |
| RFC 3326 | Reason 头（多终端"call completed elsewhere"同步） | p136 |
| RFC 4122 | UUID（ALES-DUID 载体） | p115 |
| RFC 4733 | RTP 电话事件载荷（DTMF out-of-band） | p305 |

## 4. GLOSSARY 落位说明

- candidates/glossary.md g01-g56（56 条，六大域）全部通过术语核验（BOOK_OVERVIEW 14 个候选术语逐条映射无遗漏，详见 glossary.md 收尾自检）。
- 落位口径：阶段 3 生成 `book/glossary.md` 门户版（精选高频约 32 条，保持第一本版式）；全量 56 条以 candidates/glossary.md 为准。
- 仅 passing 提及未单列的词（DSPP、PCS、REX/Virtual UA/MIPT、CCD、ICE type、P-Alcatel-CSBU/P-CAC-ALU、doorcam、EM-200/ALE-120/ALE-108、Guacamole、Rainbow WebRTC Gateway 等）已在 glossary.md 收尾自检备查，不进主表。

## 5. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- RLAB POD：LAN 192.168.1.x、DMZ 192.168.2.x、公共区 10.20.30.x。OXE CSA 物理 192.168.1.1/主用 192.168.1.3；OMS CSA 192.168.1.13；SBC 192.168.1.105/DMZ 192.168.2.205/NAT 公网 12.C.P2.105；ITServer（NTP+LDAP）192.168.1.252；内部 DNS 192.168.1.250；外部 DNS 10.20.30.250；FlexLM 192.168.1.80；SIP 模拟器 12.0.0.2；远程办公虚机 podP-outside 10.20.30.2P。
- 账号口令（全部实验口径）：mtcl/swinst/root=Superuser2580*；SBC=Admin/Admin；GD4=root/letacla1 与 mg4.ale；ITServer=training/superuser；SIP 密码 12345；ALES 全体同密 alcatel；auto-discovery 默认 0000；话机高级菜单 123456；本地认证 Superuser1245*，首连改 Administrator2580!。
- ITSP1（直连）：gateway1.itsp1.com 10.20.30.51 + public.itsp1.com 10.20.30.50，账号 pbxP/alcatel，DID 33210N41000 起、范围 500。ITSP2（经 SBC）：gateway.itsp2.com 10.20.30.60，账号 podP/alcatel，DID 33920x31000 起、范围 1000。
- 实验分机：31000/31001 IPDSP、31030 eevans、31031 eeastwood、31032 eelkins、31033 ALE-2/3、31034 ALE-300、31035 ALES-mobile、31060 MicroSIP（SIP Device）、31010-31012/31020 混合模式物理话机。话机 DHCP 池 192.168.1.161-164（实验新建）。
- 培训口径：OTP/口令遍布全书正文（n50），生产必须全量替换并做安全加固；教材只给机制不给安全制度。
