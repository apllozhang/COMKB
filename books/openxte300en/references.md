# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| TC2149 ed.04（Release 2.3.1+，本书附录 p579-602 全文收录） | OTMS/OTMC/OXE/8770 rehosting 的唯一完整操作矩阵（含外部 SIP 网关迁移七步法、许可联动、证书收尾） | p561, p579-602 |
| TC1652 | OXE spatial redundancy 下的 SIP 字段与外部语音邮件网关管理 | p231, p242 |
| TC2257 / TC2639 | OT SBC 与反向代理安装（按 OT 版本与 RP 配置二选一） | p444, p601 |
| TC1625 | Clonezilla 磁盘镜像（物理 OT 服务器 rehosting 前整盘备份） | p564 |
| OTMS 2.x Installation Manual（8AL90512US*） | 安装手册权威版；在 ALE eBusiness Portal 或 TDL 检索 | p601 |
| Delivery note / Features list / Product limits | 虚机规格、容量与话务上限的生产化依据（书内无 sizing） | p9, p507 |
| SOT Delivery note | SOT 虚机规格细节 | p59 |
| Quick Reference Guide | 语音邮箱问候语等最终用户细节 | p333 |

## 2. 官方站点与资源入口

| 站点 | 用途 | 书内位置 |
|---|---|---|
| BPWS | 软件 ISO（bootdvd/core/fax/hotfix）下载门户 | p42, p44 |
| My Portal | 外部 FlexLM 虚机 OVF 下载 | p168 |
| ALE eBusiness Portal / TDL | 技术文档库，按 8AL90512US*/8AL90120US* 等编号检索 | p601 |
| enterprise-education.csod.com | 培训课程目录与检索（p603 反馈页） | p603 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g56（56 条，六类：concept 22 / role 4 / subscription 6 / product 12 / protocol 8 / resource 4）全部通过术语核验；BOOK_OVERVIEW 术语表 16 行逐条映射无遗漏（详见 glossary.md 收尾自检）。
- 落位口径：全量保留在 candidates/glossary.md；阶段 3 生成 `book/glossary.md` 门户版（精选高频 30 余条，按六类分组表格）。
- 仅 passing 提及未单列的词（Conversation user、AAPP、OTCP、Cloud Connect、OTC Web/My Teamwork、My Messaging/My Profile、VMS、808x 系话机、MIPT/DSU/SEPLOS、ghost Z、8AL 手册编号、Knowledge Hub）已在 glossary.md 收尾自检备查，不进主表。
- 缩写口径：OMS、GD4、Mule、ESS、REX、MIPT、DSU、SEPLOS、OTCP、AAPP 等书中未给全称者一律不做外部补全，full_name 如实省略。

## 4. 实验环境口径备查（仅进 Boundary 与 book/overview，不进能力卡正文）

- POD 网段 192.168.1.x：OXE csa 192.168.1.1 / csm 192.168.1.3（p16 表印 192.16.8.1.x 为笔误，见 nr-02）、OMS 192.168.1.13、OTMS opentouch 192.168.1.50、8770 nms 192.168.1.70、FLEXLM flex 192.168.1.80、SOT sot 192.168.1.230、ECOSYSTEM eco 192.168.1.100、PC Client 192.168.1.10/11、GD4 192.168.1.12、DNS/NTP 192.168.1.254。
- 公共资源区 10.20.30.x：ITSP1 网关 10.20.30.51 / 公网网关 10.20.30.50、外部 DNS 10.20.30.254/250、备份 NFS 10.20.30.40（/mnt/db/backup/podX）。
- 账号口令（实验口径，公开教学值）：SOT admin/letacla（首登强改）与 upload/sot；OT root=superuser（SOT 预置 letacla1）、otuser=maintenanceuser、otAdmin=Admin-8770、otProfile=Admin-T1、SNMP=adminsnmp；8770 adminnmc/Superuser01*、Windows administrator/superuser；OXE mtcl/mtcl、swinst/SoftInst、adfexc/adfexc；ESXi root letacla（课堂改 superuser）。
- 号码口径：号段 31000-31499；DDI 首外线 33210N41000、首内线 31000、跨度 500（N=两位 POD 号）；语音邮件 31200、会议 31250（英）/31260（法）；ITSP1 外呼例 0110312345 送出 +33110312345；全国 33{1-5}1PN12345、移动 3361/3371PN12345、紧急 112/15/17/18。
- 工具示例输出中的 151.1.1.x / 172.25.x 为文档历史演示值（nr-03），不属于本拓扑。
