# Book Overview（参考区）— OmniVista 8770 安装与网络管理

> 供能力卡引用的背景参考；源自 references.md 落位。

## 全书主线（交付组织轴）

解决方案概览 → RLAB 实验平台 → 服务器与客户端安装（2022/2019 并列）→ 节点注册（OXE 声明同步、SSH、OXO Connect）→ 用户开通（Profile/Meta profile/批量/WBM）→ 告警体系（接入/定制/SNMP Proxy）→ 可视化与审计（Topology/Audit）→ 报表与任务（Reports/Scheduler/自动维护）→ 维护兜底（备份恢复/工具/NMC 服务/OXE 备份/许可）→ 工程支撑（网络驱动器映射）（p3-705）。每章"讲义 > How-To"配对，How-To 内"步骤 > verification"闭环。

## 四大套件与客户端（菜单总地图）

- thick client 四套件（p10）：Setup（Administration/Security/8770 Maintenance/Scheduler）、Network（Configuration/OXO Supervision/OXO Configuration/Users/Devices/Alarms/Topology/Audit/Maintenance）、Reporting（Account./Traf./VoIP/Reports）、Directory（Directory/Web Directory）
- WBM 轻客户端四应用（p34-38）：Users/Configuration/Performance/Manage My Phone，需 Unified Management 许可；入口 https://<FQDN>:8443
- 架构协议分工（p6-7, p139）：配置走 CMISE、数据提取走 FTP/SSH、告警走 CMISE/Corba、OpenTouch 走 XML Web Services

## 关键数字速查（引用须带口径）

| 数字 | 含义 | 页码 |
|---|---|---|
| 101 / 180 | 节点号示例：网络号×100+节点号；OXO 声明节点 (1x100)+80 | p123, p658 |
| 4000 / 50 / 100 / 100000 | 报告上限：TXT 行数/各格式页数/图表 X 轴/数据库行数 | p444 |
| 100 告警 + 100 事件 | 告警清除双闸实验口径 | p491 |
| "30" / 0-5 | 8770Clients 并发上限；Security 键档位 | p603 |
| 15 或 16 | R5.2 接受的许可版本（N-1 规则） | p602 |
| 6GB/8GB + 120GB | 硬件双档（<5000/>5000 用户，含 MMP 各 +1GB） | p55-56 |
| <85% | 安装期内存占用上限 | p77 |
| 750MB / 4GB | 客户端剩余磁盘底线（p93 原文 disk/memory 混写，见 nr-03）/ RAM 底线 | p93 |
| 2x5MB | NMC 服务日志滚动上限 | p548 |
| 20 OXE / 100 并发 | Manage My Phone 许可口径（仅法语英语，.Net 4.0 起） | p268 |
| 5 项 | ADM8770 用户权利数 | p684 |
| 255 | 系统域上限 | p377-381 |

## 实验环境（RLAB，仅 Boundary 背景）

- 主网段 192.168.1.x/24：网关 192.168.1.254、内部 DNS 192.168.1.250、外部 DNS 10.20.30.250；OXE csa 192.168.1.1 / csm 主用 192.168.1.3、OMS/GD 192.168.1.13、FlexLM 192.168.1.80、Client PC 192.168.1.10 与 .11、8770 服务器 nms 192.168.1.70。
- OXO 章独立网段 151.1.1.x：OXO 151.1.1.246、ecosystem 服务器 151.1.1.100（2019 章 DNS 与网络盘共享源）；共享映射 Y:（REPORTS_ECO）/ Z:（BACKUP_ECO）。
- 凭据全集（实验口径，生产必须替换）：OXE root/mtcl/swinst 会话 Superuser2580*；目录管理器与 AdminNmc 初始密码 superuser，首连改密 Superuser01*；FlexLM root/letacla1；OXO Operator 密码 Letacla1；installer 出厂 pbxk1064、本实验自定义 Alcatel1；OXO NMC FTP 账号密码 Pbxnmc12；MariaDB dba/sql；OXE N2 及以前默认 mtcl/adfexc/SoftInst。
- 安装基准值（实验口径）：计算机名 nms、DNS 后缀 company.com、静态 IP 192.168.1.70、公司名 Ale、国家 United States、成本中心 Yes；2019 章 DNS 用 192.168.1.100（ecosystem）。
- 预建用户 31000（Brad Barkley）/31001（Billy Backman）/31002（Betty Boop）；实验工具 TrapReceiver（模拟 SNMP hypervisor）/IPDSP/MicroSIP。

## 教材口径声明

- 全部实验密码/账号/网段仅限实验环境（原书明文密码遍布正文，见 needs-review nr-06）；生产必须替换并按客户密码策略与安全基线加固。
- 单机闭环口径：8770 高可用/双机/多 8770 分级不在本书范围（许可 Redundancy 字段是唯一痕迹，n50）；生产规模设计用 Capacity Planning tool V3.0（n51）。
- 文档质量三处（needs-review）：2019 章沿用旧版口径（nr-01）、OXO 章法语残句（nr-02）、客户端空间表述混写（nr-03）。
- 版本敏感点：R5.2 起 wildcard 证书改为自动生成服务器证书（n10）；OXE R101/N3 起 SSH 强制（p110/p132）；OXO R10 起强制改全部账户密码（p653）；OXE R11.2 起 incident 386 不可相关（p361）。
