# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部资源（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| TG0028 话机排障指南（My Portal 下载） | IP 话机命令（tnet/ipconfig/ipconfig survi 等）的权威清单 | p200 |
| My Portal | ALE 技术文档/排障指南下载站（生产化配置的权威依据入口） | p200 |
| Starter Training 教材 | 装机、barring、ARS 基础、GD/OMS SSH 方法、swinst/netadmin 入门——本书四个高频书外前置 | p110, p134, p229, p525 |
| ALE Knowledge Hub（enterprise-education.csod.com） | 培训目录、课后在线评估与证书下载 | p539, p543 |
| OmniVista 8770 文档（书外） | PCS 激活期话单取回、节点双主地址声明——本书仅以引用出现 | p87, p181 |
| 培训反馈邮箱 training-services@al-enterprise.com | 课程反馈通道 | p543 |

## 2. 官方站点与工具（书内出现）

| 站点/工具 | 用途 | 书内位置 |
|---|---|---|
| My Portal | TG0028 等排障文档下载 | p200 |
| ALE Knowledge Hub | 培训评估/证书（enterprise-education.csod.com） | p539-543 |
| OXE WBM / mgr | Web 图形配置界面与旧版图形工具（本书主用配置入口） | p155, p473 |
| spadmin / netadmin / swinst / mtcl 命令族 | 许可、IP/防火墙、软件与库、日常维护 | p94, p107, p113, p193 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g65（65 条，六类：concept/role/subscription/product/protocol/resource）全部通过术语核验；BOOK_OVERVIEW 术语表 22 行逐条映射无遗漏（详见 glossary.md 收尾自检）。
- 落位口径：GLOSSARY 全量收录于阶段 3 产物 `book/glossary.md`（精选高频约 40 条入主表，按六类分组；角色/资源类酌情并入）。
- 仅 passing 提及未单列的词（CSTA、QSIG/ISDN、SEPLOS、AOM、VPIM、NPD、Keep RTP flow、lanpbx.cfg、ITSP2、MicroSIP 等）已在 candidates/glossary.md 收尾自检备查，不进主表。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- **集中式 IP Pod**（p7-10，实验口径）：Subnet 1=192.168.1.x（CSA 1.1/CSB 1.2、主角色 csm 1.3、OMS 1.13、PC10/11=1.10/1.11 装 IPDSP 31000/31001、NTP 1.252、内部 DNS 1.250、网关 1.254）；Subnet 2=192.168.2.x（PCS REMOTE 2.5、OMS REMOTE 2.13、PC20/21=2.10/2.11 装 31002/31003、网关 2.254）；公共区 Subnet 0=10.20.30.x（NAS、SIP 模拟器 12.0.0.2、外部 DNS 10.20.30.250、网关 10.20.30.254）；FLEXLM 192.168.1.80。
- **组网 Pod**（p12-16，实验口径）：NODE 1（1.1/主 1.3）与 NODE 2（1.101/主 1.103、OMS 1.113）；组网实验前须做 VM 网卡迁移（CSA 摘除 192.168.1.1、NODE 1 重建该地址，f24）。
- **账号密码**（p10/p15，实验口径）：mtcl/swinst/root=Superuser2580*；PC 客户端=admin/superuser；FlexLM=root/letacla1；GD/OMS 登录 admin（root 密码 letacla1）；话机排障口令 *tx8000#。
- **ITSP1 SIP 模拟器**（p33-39，实验口径）：PBX 注册 pbxP/alcatel（SIP 域 sip.itsp1.fr）；Node 1 安装号 3321PN41000、DDI 41000-41499 ↔ 内部 31000-31499；Node 2=3311PN41500/31500；公网模拟 publicP@itsp1.fr（主号 3321PN12345）；紧急号 112/15/17/18；PN=两位 POD 号。
- **PCS 出厂网络**（p187）：PCS VM 默认 10.253.253.1/26，与实验网不互通——首配必须 console 模式（n13）。
- **培训口径**：防火墙仅为部分配置的教学口径（p49，n47）；全部明文口令仅限实验环境，生产必须替换并另行设计安全基线。
