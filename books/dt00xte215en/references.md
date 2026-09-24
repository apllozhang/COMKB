# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| OmniSwitch AOS Release 8 Specifications Guide | 会话数/VC 规模/镜像与抓包上限/PoE 预算等型号规格的唯一权威依据 | p9, p80, p158, p248, p251, p301, p514 |
| OmniSwitch AOS CLI Reference Guide | 全量命令语法（条件组合、参数默认值） | p9, p422 |
| OmniSwitch AOS Network Configuration Guide | 策略条件组合全表、深配置细节 | p9, p422 |
| OmniSwitch AOS Switch Management Guide | PKA 公私钥生成等管理面深配置 | p9, p88 |
| AOS Release Notes | 升级步骤、前置固件（FPoE/PPoE 的 FPGA/CPLD 要求） | p510-511, p533 |
| Transceivers Guide | 光模块兼容性 | p9 |
| MFA Application Note（Google Authenticator/Duo） | 多因子认证配置细节 | p89 |
| FIPS 140-2（csrc.nist.gov）/ JITC（aplits.disa.mil）/ Common Criteria（niap-ccevs.org、commoncriteriaportal.org） | 合规版本选型的三个认证清单源 | p532 |

## 2. 官方站点与工具

| 站点 | 用途 | 书内位置 |
|---|---|---|
| MyPortal（myportal.al-enterprise.com） | 软件包下载（Switches/WLAN/Network Management 分类）、OST 2.0 下载 | p11, p229, p534 |
| myfleet.ovcirrus.com | Fleet Supervision / Services Kiosk 入口（注册、声明 OmniVista、导入设备清单） | p558, p563 |
| spacewalkers.com / github.com/ale-nsa-team/OmniVista-Smart-Tool | OST 1.0 社区版下载源（ALE 停止开发） | p11, p230 |
| postgresql.org/download | OST 2.0 前置数据库（测试版本 18.1） | p573 |
| www.al-enterprise.com | ALE 官网与培训页 | p10 |
| OmniVista 2500/Terra/Cirrus | 网管平台：升级通道、PolicyView 策略下发、Fleet 资产来源 | p56, p84, p400, p533, p563 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g60（60 条，六类：概念/角色/许可与订阅/产品/协议/资源）全部通过术语核验（BOOK_OVERVIEW 的 18 个候选术语逐条映射无遗漏，详见 glossary.md 收尾自检）。
- 落位口径：阶段 3 生成 `book/glossary.md` 门户版（精选高频约 45 条，按管理安全/二层三层/策略终端/产品资源分域），全量 60 条以 candidates/glossary.md 为审计基准。
- EMP/RCL/VFL/QSI/ISIS-VC/BUM/DCE/GVRP/AVLAN/DEI/ECT-ID/ISID/AVR/RTF 等书中未给全称的缩写，full_name 一律省略，不采信外部知识；仅 passing 提及的词（PVST+、KERNEL.LNK、U-Boot/ONIE、FPGA/CPLD、DER/PEM/PKCS#12/P7B/CRL/OCSP、FileZilla、TigerVNC、pfSense、EF、DEI、PolicyView 等）已在 glossary.md 收尾自检备查，不进主表。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- R-Lab 入口：https://rdp.al-mydemo.com/，账号 LanpodXa/Xb（X=POD 号 1-32），密码每会话唯一由讲师发放（p14）。
- 交换机凭据：控制台/RustConn 登录 admin / Superuser=1（p15）；从 Linux 客户端 SSH 用 admin-netadv@10.4.X.Y，口令 Superuser01!（p38，与交换机本地口令不同，双凭据见 nr-07）。
- POD 拓扑：7 台交换机 EMP 地址 10.4.Pod#.{1,2,3,5,6,7,8} 对应 6900-A/6870-B/6560-A/6360-A/6360-B/6870-A/6860-B（p93）；10 个 Linux 客户端 + 无线客户端；RustConn 管控制台与桌面，Proxmox 仅开停虚机（p19）。
- 公共服务器：192.168.100.102 同机充当 DHCP/RADIUS/Web/FTP；pfSense 192.168.100.108；客户端 DNS 10.0.0.51（p17-18, p23）。
- Stellar AP 凭据 support/aos2016（p16）；实验交换机为最小化非空配置（预置到 10.0.0.0 管理网的静态路由，p92；预置聚合 17/78，p286）。
- 实验镜像 8.10.9.R04（p141）；历史截图残留 8.7.98.R03（p504，见 nr-08）。
