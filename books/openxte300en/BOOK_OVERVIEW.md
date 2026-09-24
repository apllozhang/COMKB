# OpenTouch Suite for MLE / OpenTouch Starter (OPENXTE300EN Ed10) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OpenTouch — OpenTouch Suite for MLE — Solution Overview / Starter（Participant's Guide）
- **作者**: ALE Training Services（Alcatel-Lucent Enterprise）
- **出版/发布时间**: OpenTouch R2.6.1 / Starter Edition 10（封面标注 OPENTOUCH - R2.6.1，SSH 横幅显示 OpenTouch™ Multimedia Services 2.6.1 / Version 18.0.100.003，附录 TC2149 为 ed.04 2019）
- **内容类型**: 课程（官方售后培训讲义幻灯片 + 分步实验 How-To，30 个 How-To 章）
- **版本来源**: `F:\AIwork\ZCode\books\openxte300en\source_fulltext.txt`（603 页，带 PAGE 标记）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + How-To 分步实验，讲义约占 45%、实验约占 55%，另含一份完整 TC2149 ed.04 rehosting 技术通报作附录）

### 一句话主旨
把一套 OpenTouch Suite for MLE（OTMS 物理一体机或 OTMS-v 虚拟化，含 OXE + OpenTouch + OmniVista 8770）从零交付上线：SOT 自动化装机、post-installation 向导初始化、FlexLM 许可落地、8770 双向节点声明与 SIP/号码打通、用户与档案供给、本地存储语音邮箱与通知、证书安全、OTC PC/One 客户端与多终端交付，最后覆盖维护、备份与 rehosting 全生命周期。

### 骨架 (主要论点及其关系)

1. **OTMS 方案概览**（ICAS/ICM/AMS 三组件、OTMS-v 虚拟化六虚机布局、5000 用户上限、物理/虚拟两种交付模式）
2. **培训实验环境**（RLAB POD 结构、混合教室形态、ITSP1 SIP 运营商模拟器、全套实例 IP/账号口令表、Pod Configuration 实验）
3. **安装部署路线**（手动 DVD / 手动 ISO / SOT 自动化三选一；OTMS 部署主步骤六段链）
4. **SOT 工具**（standalone/hosted 两模式、default/Template Factory 两配置、easy/expert 两工作模式、媒体与项目管理）
5. **系统初始化**（OVF 导入 ESXi、Post-installation wizard 十步、三种系统连接方式、SUSE 图形界面与 YaST）
6. **许可体系**（FlexLM 机制、ALUID/加密狗两种锚定、.ice/.swk/.sw8770 三族文件、final_licenses 流转、外部 FlexLM 部署与内部→外部切换）
7. **系统集成声明**（8770 中声明 OXE 与 OpenTouch 并互挂拓扑、SNMP 告警对接、OXE SIP 配置、prior management：号码段/前缀/语音邮件/拨号规则/UDAS/会议桥）
8. **用户与业务供给**（OXE/OT 双侧档案、Directory/无 OT/Connection 三类用户、Web Provisioning Client、本地存储语音邮箱/邮箱档案/IMAP 收取/SMTP-SMS 通知/通用公告）
9. **安全与客户端交付**（证书三路线 + Windows CA 全流程、OTC PC/OTC PC One 客户端、多终端 Multi-devices、监督组）
10. **运维收尾**（维护工具三通道、备份恢复、rehosting 与 TC2149 全解附录）

**论点之间的关系**: 层层递进为主——1-2 是地基（方案与实验环境），3-5 是装机初始化链，6 是许可闸门（无正确许可系统不正常工作），7 是把三台服务器缝合成一个系统的集成层，8 是业务供给层，9-10 是安全、客户端与运维三个并列能力域；附录 TC2149 是第 10 项的完整展开。

### 作者要解决的核心问题
让售后/渠道工程师独立完成 OpenTouch Suite for MLE 的全流程交付：把出厂态（或虚拟化镜像）的 OTMS 装起来、把许可配对、把 OXE / OpenTouch / OmniVista 8770 三件套互相声明打通（SIP、号码、告警、目录）、把用户和语音业务供给出来、把客户端和安全（证书）交付到位，并能做日常维护、备份与改名改址（rehosting）。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| OTMS | OpenTouch Multimedia Services：面向大市场（large market）的 OpenTouch 服务器套件，上限 5000 用户；物理一体机形态 | 不只是"一台服务器"——是 OT 核心（ICAS/ICM/AMS）+ 部署方法 + 许可体系的整体产品名 |
| OTMS-v / OT-v | OTMS 的虚拟化形态：ESXi/Hyper-V 上跑 OTMS 虚机（另有 8770 VM、OXE VM、OMS VM、DCS VM、OTFC VM） | 与 OTMS 功能同量级（同 5000 用户）；许可锚定从 ALUID 换成 USB 加密狗 |
| OXE | OmniPCX Enterprise 呼叫服务器，本套件中的传统 PBX 侧；其用户经 OT 授权后成为 Connection 用户 | 书中 OXE 常以虚机形态出现（OXE VM），且许可可由 FlexLM 或 Cloud Connect 控制 |
| OmniVista 8770 | 网管/配置服务器（Windows）：Configuration（nmc）、Users、Directory、Alarms、Maintenance 等应用；OXE 与 OT 节点都在它这里声明 | 它是"集线器"——OXE 与 OT 互挂拓扑都要经过 8770；许可证文件 .sw8770 改名 nmc.license |
| ICAS / ICM / AMS | OpenTouchServer 三组件：AMS=媒体服务器（MCU、放音、编解码 G711/G729/G722、H264）、ICM=多媒体 SIP 核心（SIP server）、ICAS=即时通信与协作服务 | 不是三台服务器，是一台 OT 服务器内的三个软件组件；AMS 的 SIP 服务器别名"Mule"（端口 5040） |
| SOT | Software Orchestration Tool：以 ISO（内含 .ova）交付的部署虚机，自动化装机（静默安装、自动挂载 ISO、PXE 启动目标机） | 它只管"装机"这一段——装完仍要做 post-installation wizard；一次只部署一台 |
| ALUID | 唯一 128 位硬件标识（getaluid 命令读取），物理服务器部署时 .ice 许可的锚定物 | 仅物理机（OTMS/OTMC）用 ALUID；虚拟化一律换加密狗（Aladdin USB dongle） |
| FlexLM | Flex-lm 许可服务（端口 27000）：可内嵌于 OT 服务器或外部独立 FlexLM 虚机；管理 .ice 许可的校验与分发 | FlexLM 只验 Product ID/锚定物，OXE 的用户数等容量仍以其本地 .swk 文件为准（Use Flex License = No） |
| Post-installation wizard | 软件安装完成后首次开机自动启动的站点安装向导（from scratch / restore from archive 两模式） | 它就是"site installation"——客户现场初始化的正式入口，不是可选步骤 |
| bics.conf | OT 服务器 /var/data/bics/bics.conf：HOST_NAME/ICE_USERNAME(otAdmin)/ICE_TEMPLATEUSERNAME(otProfile)/ICE_MAINTENANCEUSERNAME(otuser) 等，8770 声明 OT 时逐项取用 | 是 OT 与 8770 之间的"凭证对账单"；忘记密码时可从这里查账号名 |
| Connection user | 挂 OXE 设备且被授予 OT 应用权的用户（ACU，Advanced Communication User）；对应档案 = OXE profile + OT profile（Category=ACU-OXE）+ 语音邮箱档案 | "Connection"强调与 PBX 设备相连；与纯目录用户（type=None）和 OTC PC One 免费模式相区分 |
| UDAS | OT 侧接收客户端联系人检索请求的模块；单向目录同步把 OXE 话簿、内部目录、外部 LDAP 倾倒进 PostgreSQL 同步库，检索只打同步库 | 检索"不直接查源目录"——同步周期没配好（不能为 0）目录就是旧的 |
| DAS rule | 会议服务器（ACS）按域名配置的呼出号码改写规则（正则 s/^…/…/），强制且随国家不同 | 它只作用于 Conference 侧拨号；与 OT 的 Dialing rule（自动加外呼前缀）是两套规则 |
| Local Storage voice mail | OT 内置软件语音邮件：留言以 wav（未压缩、G711）存 OT 服务器目录，可被任意 IMAP 客户端读取；默认已建 defaultVmsLS | "邮件即语音"——不需要 UM/Exchange 也能用 IMAP 收留言；UM 语音邮件是另一培训的内容 |
| OTC PC / OTC PC One | 同一安装包的两种工作模式：有 Desktop 许可=完整 OTC PC（RCC+VoIP+协作）；无 Desktop 许可=OTC PC One 免费模式（话机伴侣、单线、无 VoIP） | One 不是另一个客户端，也不只是"少功能版"——它是同一个 exe 的 license 驱动形态 |
| rehosting | 用 ot-config.sh --rehost 向导改 OT 服务器的 IP/主机名/FQDN/DNS/License server；配套 TC2149 处理 OXE/8770/生态 | 不是"改个 IP"那么小——配错会死锁且无回退； inactive 分区内容会被清除 |

### 核心命题 (用自己的话)

1. OTMS 是"大市场"级 OpenTouch 套件：OXE（呼叫控制）+ OpenTouch（协作/媒体/ SIP 核心）+ OmniVista 8770（管理）三台一体，物理或虚拟化交付均上限 5000 用户。
2. 装机首选 SOT：把 SOT 虚机（ISO 内含 OVA）跑起来、导媒体（bootdvd/core/fax ISO + 许可）、建项目（目标 MAC/IP/FQDN）、PXE 启动目标机静默安装；手动 DVD/ISO 只作备选且易错。
3. 软件装完不等于能交付：首次开机必经 Post-installation wizard——本机网络、OpenTouch 账户口令（otAdmin/otProfile/otuser/SNMP）、ACS 栈、许可、证书、备份目的地，一路填完 OT 服务才启动。
4. 许可自成一体：FlexLM 服务（内嵌或外部）管 .ice 校验；物理机锚 ALUID、虚拟机锚加密狗；OXE 的 .swk 由 CPUID/FlexLM/Cloud Connect 验 Product ID；8770 的 .sw8770 改名 nmc.license 由 8770 自查。OK 状态只代表"文件在"，不代表内容有效。
5. 三台服务器靠"互挂"成网：先在 OXE 侧备好 IP/节点号/实时同步，再在 8770 建 Network/Subnetwork/OXE 节点；然后在 8770 声明 OT 节点（bics.conf 三账号），最后在 OT 侧把 OXE 挂进自己的 Topology——双向同步后 OXE 出现在 OT 拓扑树下。
6. SIP 打通有固定套路：OXE 侧 SIP trunk group（T2/SIP）+ 本地 SIP 网关 + 两条外部网关（10→OT SIP server 端口 5260，11→Mule 语音邮件端口 5040）+ 把 OT IP 加入 trusted addresses + codec 与呼叫服务器一致（G729）+ DPNSS 前缀与路由优化。
7. 号码与路由的"先 OXE 后 OT"原则：31000-31499 号段在 OT 侧声明归属 OXE；OT 的 Dialing rule 自动加外呼前缀（按名呼打全客户端生效，按号呼打仅 OTC PC/Mobile）；会议侧再叠加一套强制 DAS 规则（法国口径十条）。
8. 用户供给三件套：OXE profile（Set function=Profile，A0000 式占号）+ OT profile（Category=ACU-OXE，Licenses 页签勾权）+ 语音邮箱档案（Advanced/Classic/Simplified）；在 8770 Users 应用一次建人建机建权，或用 Web Provisioning Client（仅 Chrome 54+，8770 3.2.8+）做批量 MACD。
9. 语音邮件默认就绪：defaultVmsLS（Local Storage）默认已建，留言 wav 未压缩可 IMAP 直收（内嵌 IMAP 1000 会话封顶）；通知走外部 SMTP（无认证无 TLS）与唯一一个 SMS 网关；通用公告一次只留一条、5 分钟封顶、wav 格式固定。
10. 证书三档位：security OFF（全球通用通用证书，明确不推荐，有盗打风险）、自签（Internal，SHA256，CTL 要用 808x 话机重签）、外部 CA（远程接入必需、安全最优；PKCS7 或带口令 PKCS12 导入后必须点 Deploy）。
11. 客户端是"许可驱动形态"：OTC PC 与 OTC PC One 同一二进制，Desktop 许可决定模式；软电话走 Multi-devices 挂 SIP 分机（禁 Nomadic SIP 权）或旧 Nomadic 池；多终端最多 5 设备、远端分机与 DECT 各限 1。
12. 运维有闭环：命令行原始工具 + otconsole.sh 菜单 + Maintenance Portal（端口 4448）三通道同源；备份 otdaily 00:01 自动全量/增量、otbr.sh 手动、OT-v 必须 NFS；rehosting 一条命令但配错即死锁——TC2149 操作矩阵是唯一完整依据。

### 论证链
教材以"讲义给框架 → How-To 给菜单路径与逐字段值 → 行为验证收尾"推进；关键判断（三选一部署路线、许可形态、证书档位、rehosting 风险）用 Warning 框和对比表承载；实验值全部以 RLAB 实例表（IP/账号/口令）锚定，形成"照着就能做"的闭环，但生产化参数（容量、安全加固、高可用替代方案）大量外引 TC 文档与专项培训。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 OpenTouch R2.6.1（SSH 横幅 Version 18.0.100.003）与 2019 年的 TC2149 ed.04：VMware 只认 ESXi 6.5/7.0.x、Hyper-V 2016/2019、Chrome ≥54、Windows CA/Outlook 2013 截图，均已明显老化。
- HA 对新装机已不再支持（仅 R2.2.x 迁移场景保留）——全书没有任何替代的高可用/冗余方案展开（spatial redundancy 只被指向 TC1652）。
- 平台口径偏 Windows/Outlook 生态（Skype for Business、Teams 仅作为"高级安装"一笔带过），移动端（OTC Mobile）几乎不展开。

### 作者的立场盲点
- 全书默认实验环境：明文口令（letacla / letacla1 / superuser / Superuser01* / mtcl / adfexc / adminsnmp…）贯穿账号表与实验步骤；生产安全基线（口令轮换、防火墙、SBC 加固）只有 Warning 提示没有展开。
- 容量与话务设计缺位：除"5000 用户"和监督组 links 两张数字外，无任何 sizing/话务模型；性能与资源规划全部指向 Delivery note / Features list / Product limits 文档。
- 统一消息（UM）语音邮件、Nomadic 模式、VPN-less 会议地址、OTBE 备份等反复以"另见专项培训/另一手册"带过——一本书读完仍交付不了完整 UM 站点。

### 未被证明的假设
- 假设客户 DNS/NTP/SMTP/Windows CA 生态现成可用且正向反向解析齐备（仅靠一张 Warning 清单兜底）。
- 假设 OXE 单节点、无 spatial redundancy、法国制式编号（DAS rules、33 国码、0/00 前缀都以法国为例）。
- 假设加密狗/许可文件已在手（rehosting 换许可形态要走 eBP Siebel 工单这类商务流程，书内无解）。

### 最强反对意见
"这本教材教的是把 OTMS 三件套装起来接通的出厂-交付最小闭环，不是一套可上生产的方案设计"——高可用、容量规划、UM、移动化、Teams/SfB 深度集成、安全加固分别散落在 TC2149/TC1652/TC2257/TC2639、Features list 与多门专项培训里。因此每个能力的 Boundary 必须标注"实验口径/书内口径"，并显式指向 TC 系列文档作为生产化依据。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] 培训/实验 POD 搭建（IPDSP、SIP 网关注册、DID 翻译、外呼验证）
- [x] SOT 部署 OTMS 虚机（媒体导入、项目创建、OVF 生成与部署）
- [x] OVF/OVA 手动导入 ESXi
- [x] OTMS Post-installation wizard（全新/备份恢复两模式）
- [x] 系统连接三通道（控制台/SSH/Telnet/RDP）与账号体系
- [x] 许可文件规划与安装（三族文件、路径、final_licenses）
- [x] 许可核查排障（spadmin/lmutil/checkLicensing.sh/getaluid）
- [x] 外部 FlexLM 部署与内部→外部切换
- [x] 8770 中声明 OXE（含同步矩阵）
- [x] 8770 中声明 OpenTouch 并互挂拓扑
- [x] OXE SIP 配置（trunk/网关/trusted/codec/DPNSS）
- [x] Prior management（号码段/前缀/语音邮件/拨号规则/UDAS/会议桥与 DAS 规则）
- [x] SNMP 告警对接与 MIB 重载
- [x] 档案与用户供给（含 WPC 批量）
- [x] 语音邮箱体系（邮箱/档案/IMAP/SMTP-SMS 通知/通用公告）
- [x] 证书部署（自签/外部 CA/Windows CA 全流程）
- [x] OTC PC / OTC PC One / 多终端 / 监督组交付
- [x] 维护、备份恢复与 rehosting（TC2149 矩阵）

### 不适合 skill 化的内容
- RLAB 实验基础设施细节（p10-37 的 POD 拓扑与明文口令表——仅作 Boundary 背景与实验口径，不可进生产 skill）
- 培训课程检索与反馈页（p603）
- TC2149 附录中与 OTMS 无关的 OTMC 分支细节（p583-591 中 OTMC 行，保留指针即可）
- UM 语音邮件、Nomadic、OTBE、VPN-less 会议地址等被明确外移到专项培训的主题（只登记"书外"边界）

### 预估 skill 数量
**约 11-13 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；入口软预算 8 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 搭建并初始化实验/演示 POD（虚机起停、IPDSP、SIP 网关注册、DID 翻译、外呼验证） | p31-37 | 可呼公网的 POD | 一切实验与演示的地基 | ITSP1 为教学专用 |
| task-02 | 用 SOT 以 hosted 模式部署 OTMS 虚机 | p66-78 | 装完软件、待初始化的 OT | 标准装机路径 | 生产需按 Delivery note 定虚机规格 |
| task-03 | 把 OVF/OVA 虚机手动导入 ESXi | p79-87 | 可开机的目标虚机 | 非 SOT 场景的通用动作 | vSphere client 仅 ESXi ≤6.0 |
| task-04 | 完成 OTMS Post-installation wizard（全新或从备份恢复） | p88-108 | 服务已启动的 OT 服务器 | 一切配置的前提 | 证书/备份目的地需客户决策 |
| task-05 | 建立系统连接（VM 控制台、SSH OT、Telnet OXE、RDP 8770）与 SUSE 基本操作 | p109-127 | 可达可管的四台系统 | 所有后续操作入口 | 生产应启用 OXE SSH 安全 |
| task-06 | 安装许可文件（.ice/.swk/.sw8770；向导内或手动） | p130-154 | 许可就位的系统 | 无正确许可系统不正常 | 加密狗/许可文件需采购到位 |
| task-07 | 核查许可与排障 | p155-166 | 许可健康结论 | 交付验收与故障定位 | 无 |
| task-08 | 部署外部 FlexLM 并从内部切换 | p167-185 | 外部许可服务器 + 已切换 OT | 多 OT/OTEC 架构必需 | 加密狗挂接在 R-Lab 外必需 |
| task-09 | 在 8770 中声明 OXE 并同步 | p186-192 | 8770 可管 OXE | 管理闭环第一半 | 无 |
| task-10 | 在 8770 中声明 OpenTouch 并把 OXE 挂入 OT 拓扑 | p193-203 | 双向互挂的三件套 | 系统集成的核心 | DNS 正反向解析须先就绪 |
| task-11 | 配置 OXE SIP（trunk group、外部网关 10/11、trusted、codec、DPNSS） | p226-234 | OT-OXE 话路打通 | 语音业务承载层 | spatial redundancy 需 TC1652 |
| task-12 | 完成 prior management（号码段、前缀、语音邮件、拨号规则、UDAS、会议桥） | p235-254 | 业务号码与路由就绪 | 拨打行为正确性的总闸 | DAS 规则按国家定制 |
| task-13 | 配置 OT→8770 告警对接（SNMP v3） | p204-212 | 告警入 8770 并可验证 | 运维可视化的起点 | MIB 重载为固定坑 |
| task-14 | 创建档案与用户（OXE/OT 档案、三类用户、WPC 批量） | p255-301 | 可登录的 Connection 用户 | 业务供给主战场 | WPC 限 Chrome/8770 3.2.8+ |
| task-15 | 配置语音邮箱体系（邮箱/档案/IMAP/SMTP-SMS 通知/通用公告） | p302-396 | 留言-收信-通知闭环 | 语音业务核心体验 | 外部 SMTP/SMS 网关须客户提供 |
| task-16 | 部署证书（自签/外部 CA/Windows CA） | p397-429 | 可信 HTTPS | 安全与远程接入前提 | 客户端信任根须分发 |
| task-17 | 交付客户端（OTC PC 安装、Desktop 许可、软电话、多终端、监督组） | p430-513 | 用户可用的客户端 | 最终用户体验 | Nomadic/OTC Mobile 在书外 |
| task-18 | 运维闭环（维护工具、日志、备份恢复、rehosting） | p514-578 + 附录 TC2149 | 可运维的系统 | 售后日常与搬迁改名 | rehosting 必须按 TC2149 全矩阵 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-04 Post-installation wizard（初始化总闸，配置错一步后面全卡）
2. task-10 双向节点声明（三件套成网的核心，DNS 前提最容易踩坑）
3. task-06/07 许可安装与核查（不通过系统不正常工作）
4. task-11/12 SIP 与 prior management（拨打行为正确性总闸）
5. task-02 SOT 部署（标准装机路径）
6. task-14 用户供给（日常最高频）
7. task-15 语音邮箱与通知（体验核心、坑最密集）
8. task-16 证书（远程接入必需）
9. task-18 运维与 rehosting（rehosting 风险最高、必须按 TC2149）
10. task-01/03/05/08/09/13/17（支撑类与场景类任务）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 10 个一级部分（方案与实验环境 2 + 装机初始化 3 + 许可 1 + 集成 1 + 业务供给 1 + 安全客户端 1 + 运维 1；TC2149 附录并入运维）
- [x] 术语按实际内容列出（16 行）
- [x] 已检查作者局限/假设（实验明文口令、HA 缺位、容量缺位、UM/Nomadic/OTBE 书外、法国制式默认）
- [x] 原书关键任务 18 项，全部有来源页码、交付物与重要性依据
- [x] 工作区此前无任何部分产出（仅 source_fulltext.txt），本阶段为全量新建，无需续写/重写判断

**用户确认时间**: 2026-09-23（流水线任务内授权连续执行）
