# Visual Automated Attendant (VSAAXTE001EN Ed20) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: Visual Automated Attendant — Installation, Configuration and Maintenance (Participant's Guide)
- **作者**: ALE Training Services
- **出版/发布时间**: Edition 20（产品版本 R4.8.006 时代；书中 SIP 抓包残留 4.2.15/4.3.005 旧版界面）
- **内容类型**: 课程（官方售后培训讲义幻灯片 + 分步实验 How-To，讲义约占 45%、实验约占 55%）
- **版本来源**: `F:\AIwork\ZCode\books\vsaaxte001en\source_fulltext.txt`（351 页）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To；讲义与实验交替推进，实验含精确命令行/菜单路径/验收测试）

### 一句话主旨
在 SUSE 服务器上安装 Visual Automated Attendant（VAA）软件话务台/IVR 并接入 OmniPCX Enterprise：从 Pod 准备、install.sh 安装、OXE 侧 SIP 对接与证书，到 Web 端多租户配置与 IVR 树编排（原生节点 + 收费 IVR 选项），再到 Master/Slave 高可用与 OXE ARS 切换、日常维护备份升级、外部数据库集成与统计报告。

### 骨架 (主要论点及其关系)

1. **培训实验环境**（RLAB 远程实验室 POD：OXE/OMS/FlexLM/PC Client + VAA Master 192.168.1.55 / Slave 192.168.1.56；ITSP1 SIP 运营商模拟器与号码规则）
2. **VAA 概览**（24/7 自动话务台定位、四类功能清单、WebAdmin 入口、多公司/角色、树编辑器、路由号码、日历、过滤器、目录、提示音/TTS/ASR、管理员菜单）
3. **架构**（软件组件族、SIP ABC/F 中继呼叫流程、HA Master/Slave、OXE 本地/空间冗余三用例、PCS、multi-company、N+1、服务器规格 8/50/120 端口、虚拟化兼容、HTTPS 证书体系）
4. **交付基础实验**（Pod 配置、VAA 安装、OXE SIP 对接、证书安装、WebAdmin 初始管理）
5. **业务配置实验**（公司/业务时间/日历、提示音与 TTS/ASR 引擎）
6. **IVR 树设计**（12 种原生节点讲义 + 用例 1/2/3 三级递进实验 + 9 种收费 IVR 选项节点 + 节点专项实验：变量/收号/显示名/HTTP/邮件）
7. **高可用**（HA 讲义与命令族 + VAA 侧安装实验 + OXE 侧 ARS/识别符/NPD 附加配置实验与故障切换测试）
8. **运维**（维护：许可/密码策略/vaa 命令族/日志/告警/备份恢复；PCS 数据库同步；OPEX Purple on Demand；版本升级；统计与报告）
9. **外部数据库集成**（JDBC 驱动 + SQL 节点树实验 + MS SQL Express/SSMS 测试库搭建实验）
10. **培训收尾**（在线评估、证书下载、反馈渠道）

**论点之间的关系**: 层层递进为主——1 是地基，2-3 是概念底座（讲义），4-5 是"先跑通最小闭环"的交付实验，6 是全书核心能力域（树设计三级用例 + 专项节点实验并列），7 是 4 的可靠性加强版（VAA 侧 + OXE 侧两段实验），8-9 是并列的运维与集成能力域，10 为附注。讲义先给"是什么/为什么"，实验给"怎么做/怎么验"，两条线在每章交替。

### 作者要解决的核心问题
让售后/渠道工程师独立完成"OXE + VAA"的完整交付与运维：装好 VAA 服务器、把它经 SIP 中继正确挂到 OXE、配好证书与多租户、按客户业务编排出欢迎/分流/多语言 IVR 树、部署 Master/Slave 高可用并让 OXE 侧 ARS 完成故障切换，日常会备份升级排障、能把树接到客户数据库。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| VAA (Visual Automated Attendant) | 跑在 SUSE Linux 上的软件自动话务台/IVR：多租户、SIP 协议、7×24 呼叫路由与欢迎语、CIS-2 安全标准 | 不是话机上的"电子话务员"功能，是一整套带许可服务/数据库/Web 管理的服务器软件 |
| Tree (树/脚本) | 与路由号码绑定的呼叫处理脚本，节点拖拽编排（Start→Announcement→Menu→Transfer…） | 不只是"语音菜单"——含收号、数据库读写、HTTP 请求的完整流程 |
| Node (节点/积木) | 树的基本块：原生 12 种（Start/Select language/Announcement/Business hours/Calendar/Menu/Transfer/Voicemail/Filter/Go to tree/Record prompt/Release/Comment）+ IVR 选项 9 种（另购许可） | 每个块必须个性化命名——名称直接进统计报表，不命名等于放弃排障能力 |
| Tenant / Company | VAA 多租户配置边界：时区、DID 段、留言前缀、分机位长、目录、过滤器、树、统计 | 可与 OXE multi-company 功能联动（TBE083），但 SIP 中继属公共公司，端口不能按公司预留 |
| Routing number | 把 DID 号码与树绑定的路由条目，需手工激活（Forbidden 图标切换） | OXE 侧还有自己的 routing/ARS——两层路由缺一不可，推荐一号一树 |
| Prompt | 提示音：WAV 导入（8KHz PCM 16-bit 单声道）/电话录制/TTS 生成/树内录制 | 语音一致性是显性建议：TTS 树应把 WAV 统一转 TTS |
| TTS / ASR | 文本转语音（内置免费 PicoTTS 六语言；Google Cloud TTS 付费）与语音识别（Google ASR，需 API key） | 硬约束：G729 编解码与 ASR 互斥，要用 ASR 必须 G711 |
| Directory / Dial by name | 按姓名拨号目录，手工创建或 OXE 电话簿同步（CMIP 链路） | OXE 同步是破坏性的——会删除全部手工条目 |
| Master / Slave | HA 双机：数据库 Master→Slave 复制，Slave 只读、无统计；OXE 靠 ARS 双路由切换 | Slave 不是自动接管的热备——切换丢现有通话，Master 恢复后不自动回同步 |
| Reference VAA | N+1 冗余的配置基准机，其余 VAA 定期从它复制库 | 它挂了其余照跑，但期间不能做任何配置变更 |
| PCS | （书中未展开全称）远端外围站点的 VAA：平时复制中心库，断网时本地接管并可与 PCS 建中继 | 应急配置在网络恢复后即丢失；同步靠每日 01:00 定时任务 |
| S.O.T | software Orchestration Tool（软件编排工具）：自动装系统/配网/改默认密码/装许可/VAA | 自动化的代价：只能用自签证书 |
| incoming username | VAA 安装时定义（实验 vaa1/vaa2）、必须与 OXE 外部网关一致的对接用户名（无密码、认证方式 None） | 双侧一致是接通的关键开关；S.O.T 安装固定为 "vaa" |
| ARS | OXE 的自动路由选择（菜单原文 Automatic Route Selection）：HA 呼叫切换的实现机制 | VAA 的"高可用"其实在 OXE——VAA 侧只做数据复制 |
| Discriminator / NPD | OXE 编号识别符（放行 314 五位号并挂 ARS 表）与 Numbering Plan Description（实验 id 56） | 纯 OXE 侧编号计划概念，是 HA 附加配置链路的一环 |
| OPEX / Purple On Demand | 按用量许可池模式：VAA 须连云化 OXE 且只关联一个订阅，端口在项目内分摊，每晚午夜校验许可 | 空间冗余（跨数据中心）在 Purple On Demand 下不支持 |
| FlexLM / Release 11 | aa-license-server 用的许可服务；4.8.006 强制新许可 Release 11，文件绑定 MAC/FQDN | 许可不是"装完就完"——升版本、换网卡、FQDN 不对都会失效 |

### 核心命题 (用自己的话)

1. VAA 与 OXE 是"执行层/控制层"分工：OXE 保留呼叫控制与路由，VAA 经 ABC/F 型 SIP 中继接管被叫号码对应的脚本执行（放欢迎语、收号、转接），管理流量走 HTTPS/TLS 1.2。
2. 一切配置在 Web 界面完成且必须 HTTPS（4.6.104 起）：证书支持 PKCS12/PEM，放 /tmp 目录安装脚本自动识别，不给证书就自签——生产要提前用 XCA 等 CA 生成带 SAN（IP+DNS，CN 必填）的证书。
3. 多租户即公司：每个公司独立时区/DID 段/分机位长/留言前缀；管理员角色细分（公司管理、全量路由、用户管理等），受限用户档案只能碰问候语控制等局部功能。
4. 树是拖出来的：12 种原生节点覆盖 90% 需求（欢迎/菜单 12 键/监督或盲转/忙无应答分支/日历/营业时间/过滤/跳子树/远程录音/挂断），IVR 选项节点（收号、ASR、SQL、HTTP、邮件、条件、变量、相关数据、自定义显示名）另购许可，负责对接信息系统。
5. 路由两层缺一不可：VAA 内 Routing 菜单把号码绑到树并激活；OXE 侧负责把呼叫经中继送到 VAA（routing 或 ARS）。推荐一号一树，通配符/号段绑定"可用但不推荐"。
6. 安装三条路：手工（SUSE ALE BootDVD + install.sh 交互参数）、S.O.T 全自动、Purple on Demand；4.8.006 只支持"全新安装 + 数据库恢复"，且强制新许可 Release 11。
7. install.sh 的参数清单是接通契约：OXE 主/备 IP、incoming username（与 OXE 外部网关一致、无密码、认证 None）、编解码（G711a/G729，ASR 则禁 G729）、SMTP 告警、转移禁拨前缀（barring）、自动备份、SIP TLS 开关、postgres 密码、远程 syslog、许可文件（/tmp 自动识别 .vaa）。
8. 高可用 = VAA 侧复制 + OXE 侧切换：Slave 只读（无统计）、切换丢现有通话、Master 恢复后不自动回同步（要 vaa ha resync）、Web 客户端需重连；OXE 用两套 trunk group/外部网关 + ARS 时间路由表完成主备切换，首呼会有一段判延。
9. OXE 侧配置全书手工：trunk group（T2/SIP、ABC-F、独立 remote network）、外部网关（type VAA、port 5060 UDP、supervision 60）、trusted IP、网络路由表、前缀计划（314→树号段）；再加 DPNSS 599 路由优化与去 "0B" 显示修正。
10. 运维有命令族与策略：vaa status/services/stop/fullstop/restart/version；密码 12 位四类字符、5 次锁定（管理员锁 2 小时、vaa conf unlockAdmin）、有效期 92 天（30/7/1 天邮件提醒）；备份三级（vaa db/cert/full）+ 自动备份（日/周/月/cron + NFS，启用后关不掉，无容量监控、6 个月约 20GB）；邮件告警盖中继/端口/许可，SNMP 默认关。
11. 外部集成靠变量驱动：变量三类（Local/Global/Contextual——上下文变量只读）；SQL 节点一次取一个字段、多结果只取第一条、空结果不算错（要用 Condition 判）；HTTP 节点 GET/POST/PUT/DELETE 支持代理与自定义头；JDBC 驱动默认只有 PostgreSQL/MariaDB，其余手装到 /opt/ale/aa-webapp/lib 且 HA 两台都要装。
12. 统计是排障与运营抓手：块命名进统计、呼叫日志逐节点带时长、CSV 导出、按公司/VAA 报表（收到/处理/主叫挂断/许可不足丢失四类数）、xlsx 邮件周报（vaa.conf 双开关 + 管理员权限与邮箱）。

### 论证链
教材以"讲义定框架 → 实验给闭环"双线推进：每个 How-To 都有可拨号验证的验收（"拨 31400 应听到欢迎语后自动挂断"、"主 VAA stop 后拨 3140X 从 slave 读脚本"）；架构章用故障用例表（呼叫服务器丢失/主 VAA 丢失/WAN 断）支撑 HA 设计判断；容量与规格以"Given as an example! Always consult the official documentation!"的示例表呈现，明确让位于官方文档。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 R4.8.006/Ed20 界面；S.O.T/HTTPS 行为自 4.6.104 才定型，书中 SIP 抓包示例还残留 4.2.15/4.3.005 旧版 User-Agent，跨版本比对时容易混淆。
- TTS 引擎价格与能力页自我声明"信息可能不准确或过时"（p141），云服务部分时效性最差。
- Hypervisor 兼容表锚定 ESXi 8.0/Hyper-V 2022/Proxmox 8.2（Proxmox 自 4.6.1 起），随版本快速漂移。

### 作者的立场盲点
- 实验口径明文密码遍布全书（let acla1 / Superuser1234* / InternationalSuperuser1234* / alcatel / 0000 / vaa-vaa 数据库口令 / openweathermap token），生产安全基线只有 CIS-2 一段概念解释；SIP TLS/SRTP 实验里直接选 N，加密交付路径没有实验。
- 端口清单（p55）、服务器规格（p52）反复"Given as an example! Always consult the official documentation!"——生产化依据全在安装手册，教材只给骨架。
- 转移禁拨前缀（forbidden prefixes，防外部 callers 借 VAA 外呼）生产意义重大，但实验"Not used in the lab"，一句话带过。
- OXE 侧配置只给参数表不讲原理（ABC-F 是什么、remote network 为什么要独立），默认读者已会 OXE 运维（netadmin -m、mtcl、trkstat）。
- 多 OXE/跨站点场景只在 multi-company 一页与 spatial redundancy 讲义出现，无实验。

### 未被证明的假设
- 假设读者有 OXE 管理基础（命令行、trunk group 概念、FlexLM 许可体系）。
- 假设邮件服务器（10.20.30.11）、DNS（192.168.1.250）、NFS 存储等企业基础设施现成可用。
- 假设外部数据库由客户 DBA 配合（MS SQL/Oracle 驱动"由客户 SGBD 管理员提供"）；MS SQL Express 章甚至要工程师自己从零装库。
- 假设 Google TTS/ASR 可用（要 Google Cloud 账号、信用卡、API key）——国内/离线场景无替代方案讨论。

### 最强反对意见
"这本教材教的是单 OXE + 双 VAA 的最小实验闭环，不是生产交付"——安全项（TLS、密码、barring、防火墙端口）要么关掉要么一句话带过，网络端口清单与详细安装步骤外置到官方手册。因此每个能力的 Boundary 必须标注"实验口径"，并显式指向 VAA Installation Guide（第 4.2/6 章、第 6 章 VAA system management、第 10 章 Text to Speech）、Administration Guide（第 4.3 路由表达式、第 10 章 TTS）、TBE083（multi-company）、OTEC-S 配置指南四份外部文档作为生产化依据。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] RLAB/POD 实验环境准备与 OXE 基础核查（虚机、用户、DID 翻译、SIP 运营商、防火墙信任主机）
- [x] VAA 服务器规格选型与虚拟化兼容核查（8/50/120 端口三档 + 三种 Hypervisor 前提）
- [x] HTTPS 证书体系（自签/XCA 私有 CA/公网证书，PKCS12 与 PEM、/tmp 约定、vaa conf/diag https）
- [x] VAA 手工安装全流程（BootDVD、改密、网络、FileZilla 传输、install.sh 参数清单）
- [x] OXE 侧 SIP 对接（trunk group/外部网关/信任 IP/网络路由表/前缀计划 + DPNSS 优化与去 0B）
- [x] OXE-VAA 接通性测试与排障（测试树、trkstat、sipextgw、motortrace/mtracer、VAA softcmp 日志）
- [x] WebAdmin 初始管理（第二管理员、SMTP 告警、监督/日志/许可页）
- [x] 公司与业务时间/日历配置
- [x] 提示音与 TTS/ASR 引擎管理（WAV 规范、Pico/Google 选型）
- [x] 树设计三级用例（简单转接 UC1 / 日历+过滤分流 UC2 / 多语言菜单 UC3）
- [x] 变量与条件动态脚本（三类变量 + Set/Condition 节点）
- [x] 收号节点（PIN/工号采集与异常输入处理）
- [x] 自定义显示名节点（屏显 + COS 前提）
- [x] HTTP 节点集成外部服务（openweathermap 式 JSON 取值）
- [x] 邮件节点（来话通知）
- [x] 外部数据库集成（JDBC 驱动手装 + SQL 节点树 + MS SQL Express/SSMS 测试库搭建）
- [x] VAA 高可用部署（slave 安装 + addslave + 双侧验证）
- [x] OXE 侧 HA 附加配置（第二中继/网关/识别符/NPD/ARS 双路由/时间路由 + 切换测试）
- [x] 日常维护与备份恢复（许可核查、密码策略、vaa 命令族、日志、告警、db/cert/full 备份、自动备份/NFS）
- [x] PCS 数据库同步与 OPEX 模式处置
- [x] VAA 版本升级（备份先行 + vaa.conf 核对 + HA resync）
- [x] 统计与报告运用（呼叫日志/CSV/四类报表/xlsx 邮件周报）

### 不适合 skill 化的内容
- RLAB 实验环境与 ITSP1 SIP 模拟器细节（p5-18、p118 Tips，教学专用基础设施，仅作 Boundary 背景）
- 培训评估/证书流程（p345-351）
- MS SQL Express 从零安装全流程（p326-344，正常由客户 DBA 承担；可降级为附录参考）
- Thunderbird 收信等课堂操作细节（p74、p238）

### 预估 skill 数量
**约 10-12 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；入口软预算 8 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 准备 Pod/OXE 基础（虚机核对、用户开通、DID 翻译、SIP 运营商参数、防火墙信任主机） | p63-74 | 可打通外呼的 OXE 底座 | 一切实验与交付的前置 | 真实运营商对接在书外 |
| task-02 | 安装 VAA 应用（系统准备、改密、传输、install.sh 参数清单） | p75-87(讲义), p88-104 | 可登录 Web 界面的 VAA | 全书第一关口 | 生产证书需提前生成 |
| task-03 | OXE 侧 SIP 对接并用测试树验证接通 | p105-121 | 拨 31400 听欢迎语的闭环 | 接通性是后续一切的前提 | ABC-F 原理在书外 |
| task-04 | 安装 Web 管理证书（服务器 + PC 信任库） | p122-126 | 无告警的 HTTPS 访问 | 安全基线第一步 | 公网证书细节在安装手册 6.4 |
| task-05 | WebAdmin 初始管理（第二管理员、SMTP 告警、监督/日志/许可页） | p127-132 | 可运营的管理面 | 日常管理入口 | 无 |
| task-06 | 创建公司并配业务时间/日历 | p133-136 | 多租户业务配置 | 树设计的上下文前提 | 无 |
| task-07 | 管理提示音与 TTS/ASR 引擎 | p137-142 | 可用的语音资产 | 树脚本的声音来源 | Google 云账号在书外 |
| task-08 | 设计简单转接树（UC1：欢迎+监督转接+忙/无应答） | p164-172 | 可用的基础 IVR | 树设计入门必经 | 无 |
| task-09 | 设计日历+过滤分流树（UC2：VIP/非 VIP 分流） | p173-184 | 按主叫与时间分流的 IVR | 最常见的真实需求形态 | 无 |
| task-10 | 设计多语言菜单树（UC3：FR/EN 四选项菜单） | p185-201 | 多语言交互 IVR | 菜单/语音信箱/跳树全用上 | 无 |
| task-11 | 用变量与条件实现动态脚本 | p215-220 | 按主叫属性分流的脚本 | 动态 IVR 的地基 | 无 |
| task-12 | 收号节点采集（工号/PIN） | p221-223 | 可采集用户输入的脚本 | 自助查询类需求核心 | 无 |
| task-13 | 显示名节点（来话屏显） | p224-230 | 转接时屏显自定义信息 | 增值体验点 | 需 OXE 侧 COS 配合 |
| task-14 | HTTP 节点集成外部服务 | p231-235 | 通话中取外部数据的脚本 | 信息系统集成入口 | 外部服务账号在书外 |
| task-15 | 邮件节点（来话通知） | p236-238 | 来话发邮件的脚本 | 轻量集成 | SMTP 服务器现成 |
| task-16 | 部署 VAA 高可用（slave 安装+addslave+双侧验证） | p239-246(讲义), p247-255 | Master/Slave 就绪 | 生产可靠性刚需 | 无 |
| task-17 | OXE 侧 HA 附加配置（第二中继/网关/识别符/NPD/ARS 双路由/切换测试） | p256-271 | 主 VAA 宕机自动切换 | HA 真正生效的半边 | OXE 编号计划基础在书外 |
| task-18 | 日常维护（许可、密码策略、命令族、日志、告警、备份/恢复） | p272-295 | 可运转的运维闭环 | 售后日常最高频 | 无 |
| task-19 | PCS 同步与 OPEX 模式处置 | p300-305 | 远端同步/许可池模式可用 | 特殊场景支撑 | 无 |
| task-20 | 升级 VAA 版本 | p307-310 | 平滑升级 + HA 重同步 | 版本生命周期必备 | 新版变更点在书外 |
| task-21 | 统计与报告运用 | p312-317 | 话务报表与逐节点诊断 | 运营与排障抓手 | 无 |
| task-22 | 外部数据库集成（JDBC 驱动 + SQL 节点树 + 测试库搭建） | p319-344 | 按数据库数据转接的 IVR | 与客户信息系统打通的核心 | 生产权限最小化要 DBA 配合 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-02 VAA 安装（第一关口，install.sh 参数契约决定后续一切）
2. task-03 OXE 侧 SIP 对接与接通验证（双层路由的第二层，排障高频区）
3. task-08/09/10 三级树设计用例（核心交付能力）
4. task-16/17 HA 两段实验（生产可靠性的完整闭环）
5. task-18 日常维护与备份（售后日常最高频）
6. task-22 外部数据库集成（增值项目的主要来源）
7. task-06/07 公司与语音资产管理（树设计的前置）
8. task-04/05 证书与管理面初始化
9. task-11..15 节点专项实验（按项目需求取用）
10. task-20 升级、task-21 统计、task-19 PCS/OPEX、task-01 实验底座

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 10 个一级部分（1 实验地基 + 概念 2 + 交付基础 2 + 树设计核心 1 + HA 1 + 运维/集成 2 + 收尾附注 1）
- [x] 术语按实际内容列出（17 个）
- [x] 已检查作者局限/假设（实验明文密码、端口清单外置、barring 缺位、OXE 原理缺位、云服务依赖）
- [x] 原书关键任务 22 项，全部有来源页码、交付物与重要性依据
- [x] 工作区此前无产出，本次为全量新建；页面锚点以 source_fulltext.txt 的 ===== PAGE N ===== 标记为准

**用户确认时间**: 2026-09-23（流水线任务指派，全流程连续执行）
