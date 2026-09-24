# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| VAA Installation Guide（MyPortal 获取） | 完整安装步骤（4.2）、公网证书配置（6.4）、系统管理与命令全集（第 6 章 VAA system management） | p61, p76, p78, p277-278 |
| VAA Administration Guide（MyPortal 获取） | 路由表达式歧义消解（4.3）、TTS 细节与价格（第 10 章）、上下文变量清单 | p29, p141, p216 |
| TBE083 Multi Companies features OXE | OXE multi-company 集成权威文档 | p50 |
| OTEC-S: Visual Automated Attendant configuration Guide | multi-company 场景 VAA 配置细节 | p50 |
| MyPortal | VAA 全部文档、发行包 zip 与 BootDVD 下载入口 | p76, p95 |
| Google Cloud TTS / speech-to-text 官方文档 | 云引擎能力与价格（原书自注可能过时，p141） | p34, p36-37, p141 |
| XCA（hohnstaedt.de/xca） | 私有 CA 证书生成工具（软件/教程/文档） | p59 |
| Microsoft 下载（id=101064 / aka.ms/ssmsfullsetup） | MS SQL Express 2019 与 SSMS 获取 | p327, p329 |
| openweathermap API 文档 | HTTP 节点实验的外部服务（实验口径） | p232-235 |

## 2. 官方站点与工具

| 站点/工具 | 用途 | 书内位置 |
|---|---|---|
| MyPortal | 文档/发行包/BootDVD/许可入口 | p76, p95 |
| ALE Knowledge Hub（enterprise-education.csod.com） | 培训评估、证书下载、课程目录 | p347, p351 |
| vaa 命令族（SSH） | 服务/许可/备份/HA 全部运维操作 | p243-245, p277-278, p287-290 |
| vaa diag https / vaa conf https | HTTPS 状态与证书更新 | p58, p123 |
| trkstat / sipextgw / motortrace / traced / mtracer | OXE 侧中继/网关状态与 SIP 抓包（mtcl 登录） | p119-120 |
| netadmin -m | OXE 菜单（防火墙信任主机等） | p70 |
| XCA | 实验私有 CA | p59-60 |
| FileZilla | SFTP 传输工具（发行包与许可上传） | p96, p123 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g58（58 条）全部通过术语核验（BOOK_OVERVIEW 17 行术语逐条映射无遗漏，详见 glossary.md 收尾自检；自检句"54 条"为笔误，实数 58，见 needs-review nr-06）。
- 落位口径：GLOSSARY 全量收录（按 concept/role/subscription/product/protocol/resource 六类分组）；阶段 3 生成 `book/glossary.md` 门户版（保持六类分组表格版式）。
- 15 个仅 passing 提及未单列的词（ITSP2、Thunderbird、FileZilla、openweathermap、ODBC、RAP、TUI、VXML、COS、ANI、Q931/NPI/TON、FQDN/MAC、cron、GRUB/CIS-2）已在 glossary.md 收尾备查，不进主表。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- RLAB POD 网段 192.168.1.x：OXE 主 .1 / 备 .3 / OMS .13 / FlexLM .80 / VAA Master .55 / VAA Slave .56 / PC Client .10 / 网关 .254 / 内部 DNS .250；公共区 10.20.30.x（外部 DNS .250、NAS、SIP 模拟器、SQL/Mail 服务器 12.0.0.2）。
- 实验账号与口令：系统 root/admin 出厂 letacla1，改后 InternationalSuperuser1234* / Superuser1234*；GRUB 实验值两处大小写不一（nr-01）；Web 首连 admin/admin 改 Superuser1234*；IPDSP 密码 0000；证书密码 alcatel；postgres 口令 Superuser1234*；库凭证 vaa/vaa。
- 实验网络五参数：IP 192.168.1.55、FQDN vaa1.company.com、掩码 255.255.255.0、网关 192.168.1.254、DNS 192.168.1.250（slave 对应 192.168.1.56 / vaa2.company.com）。
- ITSP1 模拟器：gateway1.itsp1.com（10.20.30.51，pbxP/alcatel，SIP 域 sip.itsp1.fr）；DID 翻译首外线 33210P41000、首内线 31000、范围 500；测试树号 31400-31410 段（公司 DID 段 31400-31415）。
- 实验服务：SMTP 10.20.30.11:25（发件 vaa.podX@company.com、收件 administrator.podX@company.com）；MS SQL 测试库 10.20.30.11:1433（DB_VAA）；openweathermap 实验 token 两枚（p232，公开教材值，生产禁用）。
- 实验许可：5 端口 Release 11（VAA_PORTS [5] / VAA_IVR [true] / VAA_RELEASE [11]）。
