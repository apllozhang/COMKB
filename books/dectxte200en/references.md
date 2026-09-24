# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| 《DECT and IP-DECT Engineering Rules and Site Survey Kit Manual》（8AL90874USAA） | 无线覆盖设计方法、工程规则、勘测套件手册——生产化无线工程的唯一依据 | p140-141, p212, p216 |
| 《8378 DECT IP-xBS Troubleshooting Guide》（8AL91443ENAA，im_8378_DECT_IP-xBS_Troubleshooting_Guide_8AL91443ENAA_1_en-1.pdf） | 深度排障（PCAP 分析、日志深读） | p138 |
| 《OmniPCX Enterprise Initial Configuration》（oxe_p_101.1_sd_InitialConfig_8AL91047ENAD_2_en-1.pdf） | DHCP/初始配置细节（含 xBS vendor class 的通用配置语境） | p146 |
| 《Getting started with the 8378 DECT IP-xBS solution on OXE》（BP 网站文档） | 复杂部署（多 PARI/多 Site/外部同步）的开局细节 | p140 |

## 2. 官方站点与工具

| 站点/工具 | 用途 | 书内位置 |
|---|---|---|
| BP Web Site | 《Getting started with the 8378 DECT IP-xBS》下载入口 | p140 |
| Visual Syslog server（免费软件，实验装于客户端 PC） | xBS 日志集中接收（实验口径 NAS 安装包） | p155-161 |
| RLAB NAS（\\12.0.0.2\RLAB\ENTP；RLAB\Trainee，实验口径） | 实验软件与安装包存放 | p156 |
| 手机 survey mode（*7378423* 即 *service*） | 现场覆盖勘测（RSSI/RFPI 显示） | p213-217 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g56（56 条）全部通过术语核验；BOOK_OVERVIEW 的 18 个关键术语逐条映射无遗漏。
- 落位口径：candidates/glossary.md 按 concept/role/subscription/product/protocol/resource 六类分组（本书为本地部署教材，subscription 类无条目，仅 8328 场景"每台 DECT 终端 1 个 SIP 用户许可"归入 product 语境）；阶段 3 生成 `book/glossary.md` 门户版（保持第一本版式，六域表格）。
- 缩写书中未给全称的（UA、RTP、SIP、NTP、TFTP、DHCP、Syslog、LLDP-MED、FWU、IPEI、VAD、CLIP）一律标"书中未展开"，不采信外部知识。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- POD 网段（Subnet 1，192.168.1.x，实验口径）：OXE CSA 物理 192.168.1.1 / Main 192.168.1.3、OMS 192.168.1.13、IT SERVER/NTP 192.168.1.252、FlexLM 192.168.1.80、内部 DNS 192.168.1.250、课堂 PC 192.168.1.9、GD4 192.168.1.12；DHCP VLAN1 池 192.168.1.145-155；公共区（Subnet 0，10.20.30.x）放 NAS/SIP 模拟器/外部 DNS 10.20.30.250。
- 账号密码（实验口径）：mtcl/Superuser2580*、flex/letacla1、training/superuser、RLAB\Trainee/Superuser1234；xBS WBM engineer/Engineer00!、admin/Admin00!；8328 WBM admin/admin。
- DECT 实验值：AC System=1111；PARI 约定 IBS=100004101x0、xBS=100004101x4（x=POD 号）；分机 31015（GAP+）/31016（GAP+）/31017（GAP）/31040（SIP Extension，8328）；Site 0=BREST、Site 1=BO；重注册清单 DECT.txt 传 /tmpd、结果 ReinstallSuccessHandsetsList.txt / ReinstallNOKHandsetsList.txt；手机固件二进制 /usr2/downbin（bin8212…bin8262EX）。
- 混合实验拓扑：IBS PARI（RPN 0/1）与 xBS PARI（RPN 0）同站间距约 15 米（实验口径）；外部同步源=IBS PARI RPN 0。
