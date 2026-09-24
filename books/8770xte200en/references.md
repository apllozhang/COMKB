# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| OmniVista 8770 Capacity Planning tool V3.0 | 虚机参数的规模设计（生产规模规划依据） | p8 |
| High Availability 产品文档（书外） | 8770 双机/容灾设计——书内仅许可 Redundancy 字段提及 | p605 |
| OXE/OXO 各自的系统文档（TC 系列等） | OXE 侧 siteid/netadmin/swinst/multitool 的完整语法（书内只教 8770 视角） | p119-136, p587-593 |
| Alcatel-Lucent Enterprise 支持门户（SR） | 8770 Diagnostic 采集 zip 的提交对象 | p523 |
| BP 网站（OMC 软件分发） | OMC 安装包下载（8770 服务器与每个客户端） | p20, p644 |

## 2. 8770 服务器内嵌组件速览（架构认知，非外部依赖）

| 组件 | 角色 | 书内位置 |
|---|---|---|
| MariaDB 10.5（服务名 MySQL8770） | SQL 数据库：计费/VoIP/话务/告警/审计与报告 | p7, p529-531 |
| Oracle DSEE（C:\8770\SunONE） | LDAP v3 目录：用户/设备/公司目录，389/636 | p7, p61, p592 |
| Apache / Wildfly | HTTP Web 服务（80）/应用服务器（8080） | p61, p542 |
| Open JRE | 内嵌 Java 运行时（客户端同源 Zulu） | p61, p102 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g60（60 条）全部通过术语核验，按 concept/role/subscription/product/protocol/resource 六类组织；两个安装章、九大应用、路径端口地图与实验环境参数表均已收录。
- 落位口径：阶段 3 生成 `.cangjie/capabilities/book/glossary.md` 门户版（精选高频 30 条左右，保持第一本版式）；全量 60 条以 candidates/glossary.md 为审计底稿。
- 实验工具族（TrapReceiver/FlexLM/IPDSP/MicroSIP）与 RLAB 参数表（g49/g59）只作 Boundary 背景，不进能力卡正文。

## 4. 实验环境口径备查（仅 Boundary 背景与 book/overview，不进能力卡正文）

- 主网段 192.168.1.x/24：网关 192.168.1.254、内部 DNS 192.168.1.250、外部 DNS 10.20.30.250；OXE csa 192.168.1.1 / csm 主用 192.168.1.3、OMS/GD 192.168.1.13、FlexLM 192.168.1.80、Client PC 192.168.1.10/192.168.1.11、8770 服务器 nms 192.168.1.70。
- OXO 章独立网段 151.1.1.x：OXO 151.1.1.246、ecosystem 服务器 151.1.1.100（2019 章 DNS、网络盘共享源）；映射盘符 Y:（REPORTS_ECO）/ Z:（BACKUP_ECO）。
- 凭据（全部实验口径，生产必须替换）：OXE root/mtcl/swinst 会话 Superuser2580*；目录管理器/初始 AdminNmc superuser，首连改密 Superuser01*；FlexLM root/letacla1；OXO Operator Letacla1；installer 出厂 pbxk1064、本实验自定义 Alcatel1；OXO NMC FTP 账号 Pbxnmc12；MariaDB dba/sql；预建用户 31000-31002。
- 安装基准值（实验口径）：计算机名 nms、DNS 后缀 company.com、静态 IP 192.168.1.70、公司名 Ale、国家 United States、成本中心 Yes。
