# OpenTouch Message Center Starter (OTMCXTE200EN R2.6 Issue 08) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OpenTouch Message Center · Starter（Participant's Guide）
- **作者**: ALE Training Services（Alcatel-Lucent Enterprise）
- **出版/发布时间**: Issue 08（OpenTouch Message Center R2.6 / OTMC 2.6.1 时代）
- **内容类型**: 课程（官方售后培训讲义幻灯片 + 分步实验 How-To，讲义约占 55%、实验约占 45%）
- **版本来源**: OTMCXTE200EN（259 页），全文见 `F:\AIwork\ZCode\books\otmcxte200en\source_fulltext.txt`
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To；9 大章，其中 How-To 实验章 13 个）

### 一句话主旨
把 OpenTouch Message Center（OTMC，OXE 专用语音邮件服务器）从零装起来并跑通语音信箱业务：装机与站点配置 → 经 OmniVista 8770 完成 OXE/OTMC 双向声明与同步 → 配 OXE 侧 SIP 对接 → 开通 Connection 用户与语音邮箱（账户/邮箱/profile/问候语）→ 叠加 SMTP/SMS 通知、IMAP 客户端访问、企业广播（general announcement）三块增值能力 → 备份恢复与语音信箱统计收尾。

### 骨架 (主要论点及其关系)

1. **OTMC 产品定位**（单服务器独立语音邮件系统 + 自动话务员能力，专服务 OmniPCX Enterprise 的 Connection 用户，取代 46xx/8440 旧方案；纯语音邮件架构，TUI/GUI/IMAP 三种访问通道）
2. **系统与商业架构**（SUSE Linux Enterprise 底座；物理机或 OTMC-V 虚机（VMware ESXi，dongle 绑定，vMotion/DRS 有限支持）；flex-lm 许可机制，ALUID/OTID + .ice 文件；OXE-OTMC 直连单 SIP trunk + PRS 链路 + VPIM 组网）
3. **实验拓扑**（VMware ESXi 单主机六虚机：OTMC/FlexLM/OmniVista 8770/OXE/OMS/Eco-System（DNS+AD+Exchange+LDAP+DHCP），外加 Windows 客户端 PC；company.com DNS 域，151.1.1.x 网段——实验口径）
4. **装机**（安装资料清单、ISO 介质两种制法、SUSE 安装三种模式（15000 users 硬件/虚拟化/单分区平滑升级）、core 安装 CheckSystemLinux.sh + setup.bin）
5. **Post-installation wizard**（站点级 13 步基础配置：类型/主机/网络与 DNS/NTP/HA/账户/许可服务器/许可文件/证书/备份存储/摘要/更新；含手工装许可路径）
6. **8770 双向声明与同步**（OXE 侧准备（netadmin/角色地址/节点名/节点与网络号/实时同步开关）→ 8770 建网络-子网-节点并声明 OXE/OTMC → OTMC 拓扑里声明 OXE → 同步矩阵（complete/partial × separate/global））
7. **OXE SIP 对接与用户开通**（trunk group T2/ABC-F/SIP、SIP external gateway 端口 5040、trusted addresses、G.729 编解码、DPNSS 前缀与路由优化；Connection 用户两法创建、话机寻址（resurrection/空闲地址/IP 静态）、六族话机许可核查）
8. **语音信箱体系**（OTMC 账户与 OXE 用户以分机号挂钩、VMS（defaultVmsLS）→ 邮箱（必须挂 profile）→ 用户三级对象、默认 profile 三加一（Advanced/Classic/Simplified/Standard-UM）、问候语四类与管理员 Greeting Managers 网页、My Profile/MyMessaging 自助门户）
9. **通知与增值能力**（SMTP/SMS 通知：外部 SMTP 经 VPIM 路由声明、Scorpio 组件、模板按语言定制；IMAP 客户端直接访问语音邮箱（IMAPS+TLS 默认）；general announcement 企业广播三种播报场景）
10. **运维**（经 8770 的 OpenTouch 备份与恢复（SSH/SFTP、恢复后手工起服务、NFS 外置）、voicemail statistics（statistics.properties、XML/HTML/CSV 输出））

**论点之间的关系**: 层层递进为主——1-2 是概念地基（是什么、怎么算许可、怎么连），3 是实验底座，4-6 是装机与纳管闭环（安装→站点配置→声明同步，顺序不可颠倒），7 打通 OXE↔OTMC 话路与用户，8 是业务主体（信箱三对象模型），9-10 是并列的增值能力域与运维收尾。

### 作者要解决的核心问题
让售后/渠道工程师独立完成 OTMC 的"装机-纳管-对接-开箱到业务"全流程：从裸服务器/虚机到用户能收发语音留言、收通知、用邮件客户端听留言，并能做日常备份与用量统计——即 OTMC Starter 级别的完整交付动作集。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| OTMC | OpenTouch Message Center：装在单台服务器上的独立语音邮件系统，含自动话务员（automated attendant）能力，专门面向 OmniPCX Enterprise 的 Connection 用户；取代 46xx/8440 | 不是"OXE 的一个功能模块"，是独立服务器产品；也非全 OpenTouch 套件（OT based，可演进） |
| Connection user | OTMC 服务的目标用户类型（OXE 上的 Connection 类用户） | 书中与 "OT applications" 用户区分：OT applications=None 表示该 OXE 用户不用 one number/conferencing/OTC 等 OT 应用，但仍可有 OTMC 信箱 |
| OTMC-V | 面向虚拟化环境的 OTMC 软件包，可与 OXE 或 OXE-V 搭配；VMware ESXi 虚机 | 与物理版"限制与功能完全相同"；许可从 ALUID 绑定改为 USB dongle 绑定 |
| flex-lm / .ice | 许可机制：OTMC 许可文件为 `<license>.ice`，由 flex-lm 服务器控制；非虚拟化绑 ALUID（128 位硬件标识），虚拟化绑 Aladdin USB dongle 的 dongle-ID | FlexLM 服务器可内嵌在 OTMC 里也可独立部署（可以是虚机）；"OK 状态"只代表文件在本地，不代表有效 |
| ALUID | 唯一的 128 位标识，基于服务器硬件特征生成（书中给出定义，缩写全称未展开） | ALE 出的整机贴纸上有；只买软件时要用 `/usr/bin/getaluid` 取加密值 |
| PRS | p17/p18 出现的组件与链路名（"PRS Link between each OXE for GUI display"；p99 标注 OXE PRS port 2570）——书中未展开全称 | 书内只交代用途（支撑 8 系话机 GUI 显示语音信箱，5000 并发用户），全称不可编造 |
| VPIM | 支持的组网协议：用于 OTMC 实体互联、与三方语音邮件互通（p20）；SMTP 通知也借 VPIM session 路由声明（p185）——全称未展开 | 在本书里有双重身份：组网协议 + 通知路由的配置入口（Messaging/VPIM） |
| MWI | Message Waiting Indicator（留言等待指示）：话机上新留言 LED 闪亮（p171/p199） | 邮件已读不会同步灭灯——"MWI on the phone set is not synchronized when reading the email" |
| TUI / GUI | TUI=Telephonic User Interface（p142 展开），电话按键界面；GUI 为图形界面（话机可视化信箱/网页）——GUI 缩写未展开 | 信箱密码分两套：TUI password（话机/可视化信箱）与 GUI password（网页） |
| VVM | Visual Voice Mail（p122/p140 展开）：话机信封键直达的可视化留言 | 默认要求输 TUI 密码（"Request password for visual voicemail access on set" 默认选中） |
| Voice mail profile | 管理员用来"成批控制"信箱功能与容量的模板：Answer only/查配额/直拨回叫/受限访问/留言时长/信箱配额/新旧留言保留天数/IMAP 可达等；默认三个（Simplified/Classic/Advanced，本地存储）+ Standard（UM） | 邮箱创建时必须挂 profile 才能保存——profile 是强制前置，不是可选项 |
| Local Storage / UM | 语音邮件两种类型：LS=消息存 OTMC 本地；UM=统一消息（Exchange/Lotus Domino/Gmail）（p169） | 通知功能两种都支持基础邮件/短信，但 .wav 附件、My Messaging 链接、满箱提醒等仅 LS 有（p180 矩阵） |
| resurrection | 数字/模拟话机的"复活"寻址法：话机上直拨分机号+密码（默认 0000），系统自动把真实物理地址（机架-板-位）绑给用户 | 不是故障恢复术语，是 OXE 话机地址分配手段；也用于移机（配合 In/Out of Service 前缀） |
| bics.conf | OTMC 站点配置落盘文件（post-install 产物），存 HOST_NAME/DOMAIN 与 ICE 账户三件套（otAdmin/otProfile/otuser 及加密口令） | 8770 声明 OTMC 时的"对账单"；路径 /var/data/bics/bics.conf |
| My Profile / MyMessaging | OTMC 两个用户自助 Web 应用：My Profile 管个人设置（语言/通知/信箱选项/密码），MyMessaging 在网页上听留言（PC 或话机播放） | URL 就是 OTMC 的 FQDN（MyMessaging 为 /MyMessaging 路径）——和 OT 套件其它 web 应用入口区分 |
| Chameleon / Scorpio | OTMC 软件组件（p17 架构图 Chameleon (EVS+FWK)；p185 通知由 Scorpio 组件处理） | 排障抓手：service chameleond/scorpiod status；日志在 /logs/...（p192） |
| general announcement | 企业广播：在留言落箱（外呼/内呼）与信箱查询前播放的公司级公告；管理员定播报范围，授权用户经 TUI 或 wav 文件录制 | 单条、新录覆盖旧录、最长 5 分钟；wav 必须 CCITT A-law 8bits 8kHz mono 且改名 general_announcement.wav |
| automated attendant (AA) | OTMC 定义里附带的能力（p5）；p225 提到 OT 服务器曾内嵌 AA，其"arrive on AA"播报选项对外置 VAA 方案无效 | AA 在本书只是历史/定义性概念，Starter 级别不教 AA 配置 |
| SIP trunk (T2/ABC-F) | OXE↔OTMC 的直连中继：仅一条、指向 front node；trunk group 类型 T2、T2 Specification=SIP、Q931 variant ABC-F；Bypass 按全部端口配置与用户数无关 | 与"出局运营商 SIP trunk"是两回事——这是 PBX 与信箱服务器的内部对接中继 |

### 核心命题 (用自己的话)

1. OTMC 是"OXE 专属外挂信箱"：单服务器独立部署、纯语音邮件架构（消息存 OTMC 或 SAN），取代 46xx/8440；访问通道三条——任意话机 TUI、Premium Deskphone 8xx8/Smart Deskphone 8088 的 GUI（信封键直达可视化信箱）、任意 IMAP 邮件客户端。
2. 配置管理只有一个大脑：OmniVista 8770（OTMC 是新节点类型+新图标），统一用户管理、配置、告警/拓扑、性能、备份恢复；OTMC 自己的 WBM（WebAdmin）只做辅助（改密码、问候语管理、IMAP 前端参数）。
3. 部署两形态能力等价：物理机（许可绑 ALUID）与 OTMC-V 虚机（许可绑 dongle，支持 vMotion 与手动/半自动 DRS，其它 VMware 服务不支持，同主机可多实例、可混跑第三方应用）；上限都是 15000 用户（安装模式标注）。
4. OXE-OTMC 连接极简且严格：直连 SIP trunk group 只有一条、指向 front node，Bypass 按全部可用端口配置（与用户数无关）；PRS 链路支撑每台 OXE 的话机 GUI 显示（5000 并发用户）；VPIM 负责 OTMC 之间及与三方信箱互通；OXE ABC Supra 网络不支持集中式 VM（集中信箱）。
5. 许可是 flex-lm 体系：.ice 文件装进 $LICENSES_HOME（/var/data/licenses），拷入新文件必须重启 flexlmd；向导里点 OK 只代表"文件存在"，有效性不校验——要靠 lmutil lmstat 复核。
6. 上线顺序是刚性链条：OS（SUSE）→ core 软件（CheckSystemLinux.sh→setup.bin）→ 首次开机自动起 post-installation wizard（13 步）→ 8770 双向声明+同步 → OXE 侧 SIP 对接 → 建用户与信箱。
7. DNS 是隐形地基：必须做前向+反向解析的 FQDN 清单（OTMC、8770、邮件服务器、LDAP、OXE 呼叫服务器（无冗余/本地冗余/空间冗余三种口径）、OXE H.323 网关），漏一条后面到处报错。
8. 站点配置的账本在 bics.conf：HOST_NAME/HOST_DOMAIN 与 ICE 三账户（otAdmin=8770 配置用、otProfile=模板管理用、otuser=维护/SSH/备份用）——声明 OTMC 时全部要从这里对账；密码丢失分别走 WBM 和 /usr/bin/musett.sh 重置。
9. 信箱三级对象模型：VMS（系统默认 defaultVmsLS）→ mailbox（创建时必须挂 profile）→ user（Mailboxes 页签挂箱、Licenses 页签开 Voice mail 权）；OTMC 账户与 OXE 用户靠同一个分机号（31000/31001/31002 实验口径）对上号。
10. profile 是批控模板：三个默认（Simplified/Classic/Advanced，LS 用）+ Standard（UM 用），三张配置页管行为（Answer only/直拨回叫/受限访问/留言后选项/0 转话务台…）、容量与期限（配额/问候/留言/live record 时长/新旧留言保留天数）、密码管理策略；可以自建（书中示例 my_profile：10MB/5s/15s/15s/15 天/7 天，实验口径）。
11. 通知走外部设施：OTMC 不带 SMTP 服务器——通知经 VPIM session 声明的路由发给外部 SMTP（必须无认证、无 TLS），由 Scorpio 处理；SMS 要经 SMTP-SMS 网关（系统仅允许配一个，地址形如 SMS$号码$@域）；模板按语言存 /var/data/panda/notification4，升级不覆盖旧模板（要新模板须手删+重启 chameleon）。
12. 增值与运维三件套：IMAP 客户端可直读语音邮箱（OTMC 侧默认 IMAPS+TLS，改安全级要改端口并重启 imap4fed；OTMC 不当 SMTP 服务器，Outlook 测试发信失败是预期）；general announcement 单条/覆盖/≤5 分钟；备份经 8770 Maintenance（SSH/SFTP 拉包，恢复后必须手工 service opentouchd start）；统计靠 statistics.properties（改完重启 mascd）。

### 论证链
教材以"讲义幻灯片（概念/参数/架构图）→ How-To 分步实验（精确菜单路径 + 实验口径参数）→ 行为验证"推进：每个实验带检查点（如信箱测试清单 p143、Outlook "Test Account Settings" p207、删用户再恢复验证备份 p243、留言落箱看通知与 MWI p191）；架构性结论（同步矩阵、功能可用性矩阵）直接给查表而非推导。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 OTMC R2.6 / Issue 08 界面：8770 侧出现 Windows 2008 R2 许可键（p49）与 Fax Server Windows 2019（p38/p40）混用，Outlook 客户端走 Control Panel/Mail 老入口（p203），UM 支持 Exchange/Lotus Domino/Gmail 并列（p169）——与当前版本的现实差距大。
- SUSE Linux Enterprise 12 底座；OTMC 安装手册定版为 otmc2.6.1（p58）。
- p52 出现"Red Hat installation"字样与 p53 "CheckSytemLinux.sh" 拼写——疑似沿自 OXE 课程模板的笔误，跨版本阅读要小心。

### 作者的立场盲点
- 实验口径明文密码贯穿全书（letacla1/OtmcV01*/letacla1234/maintenanceuser/Admin-8770/Admin-T1/adminsnmp/Eco-System 用户 1234），生产安全基线只在两处点到：Network security OFF 的 toll fraud 警告（p78）与话机默认密码 0000（p113/p116）——没有专门的加固章。
- HA 只留一句"将在专门章节讲解"（p74），本书不含；硬件/软件规格、产品上限全部外指 feature list 和 product limits 文档（p13/p48）。
- 立场偏 ALE 栈：UM 的三方对接（Exchange/Domino/Gmail）、三方 VM 互通（VPIM）都只有一句支持性表述，无任何配置细节。

### 未被证明的假设
- 假设读者已具备 OXE 与 OmniVista 8770 基础（netadmin/mgr/spadmin/siteid/ednump 等命令直接使用，不做解释）。
- 假设客户侧 DNS/AD/Exchange/LDAP/NFS 基础设施现成可用，DHCP 由网络管理员负责（p116 明说"not covered in this training"）。
- 假设 VMware/vSphere 环境已就绪（p58 "The VMware ESXi infrastructure is installed"）。

### 最强反对意见
"这本 Starter 只覆盖 OTMC 的最小生产闭环：单机安装、基础信箱业务、三类通知/访问增值与备份统计"——容量规划（Capacity Planning Tool 用法）、HA、UM（Exchange）落地、AA/自动话务员配置、硬件规格、8770 自身安装全部在书外。因此每个能力的 Boundary 必须标注"书外文档"：feature list/product limits（规格与上限）、otmc2.6.1 安装手册（MyPortal）、TC1652（空间冗余 SIP 网关）、TC2024（8770 上 NFS）、Quick Reference Guide（问候语细节）、Training curriculum 后续课程（HA/DHCP）。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] OTMC 部署形态决策（物理 vs OTMC-V、商业包、15000/5000 上限、VPIM 组网与 ABC Supra 限制）
- [x] OTMC 许可证体系部署（.ice/FlexLM 内嵌或外部、ALUID/dongle、getaluid、$LICENSES_HOME、lmstat 核验）
- [x] OTMC 服务器安装（VM 规格（实验口径）、BIOS/ESXi 调优、SUSE 三种安装模式、core 安装）
- [x] Post-installation wizard 13 步站点配置（含 DNS 前向反向清单、账户命名与密码硬规则、备份存储选型）
- [x] 手工安装/更换许可文件（SFTP otuser、flexlmd 重启、lmutil 核验）
- [x] OXE 纳入 8770 的准备与声明（netadmin/角色地址/节点名/节点号=ABC×100+节点/实时同步开关/声明字段/同步矩阵）
- [x] OTMC 声明进 8770 与 OTMC 拓扑声明 OXE（bics.conf 对账、密码重置两路、拓扑声明、同步）
- [x] OXE SIP 对接 OTMC（trunk group T2/SIP、external gateway 5040、trusted、codec/DPNSS/路由优化）
- [x] Connection 用户创建与话机开通（两法建户、resurrection/空闲地址/IP 静态、六族许可核查）
- [x] OTMC 账户与语音邮箱交付（账户创建、VMS 核验、邮箱创建分配、Voice mail 许可）
- [x] 语音邮箱 profile 定制（默认 profile 参数地图、新建与分配）
- [x] 问候语集中管理（Greeting Managers 网页上传/激活动作集）
- [x] 用户自助门户应用（My Profile/MyMessaging 功能与入口）
- [x] SMTP/SMS 通知部署（全局参数、VPIM 路由、模板定制、用户级设置、排障服务与日志）
- [x] IMAP 客户端访问语音邮件（Outlook 账户、IMAP4 Front End 安全匹配）
- [x] general announcement 部署（播报类型、用户权限、TUI 录制、wav 文件口径）
- [x] OpenTouch 备份与恢复（目录/阈值/备份参数/备份/恢复/服务重启/NFS 指针）
- [x] 语音信箱统计启用（statistics.properties 参数与示例、mascd 重启）

### 不适合 skill 化的内容
- 实验拓扑搭建细节（p21-32 六虚机 IP/账号表——教学专用基础设施，仅作 Boundary 背景与实验口径来源）
- 版权声明与培训反馈页（p2、p259）
- OXE 侧基础操作教学（resurrection/free addresses/IP 话机注册属 OXE Starter 课程范围，本书仅借用；skill 化时只保留与信箱开通相关的最小子集）

### 预估 skill 数量
**约 8-10 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 判断 OTMC 部署形态与容量口径（物理/虚拟、商业包、VPIM 组网、ABC Supra 限制） | p3-20 | 形态与组网决策结论 | 一切后续动作的前提；上限数字（15000/5000）在讲义层 | 硬件规格与容量规划工具用法在书外（feature list/product limits） |
| task-02 | 搭建实验/集成环境拓扑（ESXi、六虚机、DNS 域、IP 规划） | p21-32 | 可用的装机环境 | 全部实验的底座；DNS 域名规则是后续一切解析的前提 | 生产拓扑按客户实际；书中明说 VM 规格仅 lab（p58） |
| task-03 | 部署 OTMC 许可证体系（FlexLM 位置、.ice、ALUID/dongle、装文件与核验） | p33-45, p76-77, p82 | flexlmd 运行且许可有效 | 无许可 OTMC 无法正常工作（p77 Tips） | 正式许可文件的申领流程在书外 |
| task-04 | 安装 OTMC 服务器（虚机创建、BIOS/ESXi 调优、SUSE 安装、core 安装） | p46-68 | 完成 core 安装待站点配置的 OTMC | 装机主线第一段 | RAID 与客户 DNS 前置（p52 注）、安装手册细节在 MyPortal |
| task-05 | 执行 post-installation wizard 完成 13 步站点配置 | p69-81 | 基础配置完成、OT 服务启动 | 站点级配置的唯一入口；DNS/账户/证书/备份全在这 | HA 配置在后续课程（p74 注） |
| task-06 | 手工安装或更换许可文件 | p82 | 新许可生效（lmstat 可查） | 换许可/漏装许可的标准路径 | 无 |
| task-07 | 准备 OXE（IP/角色地址/节点名/节点号/实时同步）并声明进 8770、执行同步 | p83-89 | 8770 中 OXE 节点同步完成 | 纳管闭环的 OXE 半边 | OXE 基础命令（netadmin/mgr/siteid）属 OXE 课程 |
| task-08 | 声明 OTMC 进 8770 并在 OTMC 拓扑中声明 OXE、执行同步 | p90-101 | 双向声明与同步完成（OXE 挂到 OTMC 拓扑下） | 纳管闭环的 OTMC 半边；bics.conf 对账是易错点 | 无 |
| task-09 | 配置 OXE 侧 SIP 对接 OTMC（trunk/external gateway/trusted/codec/DPNSS） | p102-108 | OXE↔OTMC SIP 话路配置完成 | 信箱业务的呼叫通道；端口 5040 是关键给定值 | 空间冗余场景按 TC1652（p105 警告） |
| task-10 | 创建 Connection 用户并开通话机（含地址分配、IP 话机、许可核查） | p109-118 | 可电话可达的 OXE 用户 | 信箱的宿主用户 | DHCP 服务器管理在书外（p116 注） |
| task-11 | 创建 OTMC 账户并交付语音邮箱（账户/VMS/邮箱/许可权） | p119-145 | 带邮箱与 Voice mail 权的语音邮件用户 | 业务交付主体 | 无 |
| task-12 | 定制语音邮箱 profile 并分配 | p146-152 | 按客户策略的 profile | 批控容量/期限/行为的唯一手段 | 无 |
| task-13 | 指导用户使用 My Profile 与 MyMessaging 自助门户 | p153-166 | 用户可自助管理设置与留言 | 交付后用户侧日常 | 无 |
| task-14 | 配置 SMTP/SMS 通知（全局/VPIM 路由/模板/用户设置/排障） | p167-192 | 通知链路可用并经行为验证 | 客户感知最强的增值功能 | SMTP 服务器与 SMS 网关由客户提供 |
| task-15 | 配置 IMAP 客户端访问语音邮箱 | p193-209 | Outlook 等客户端可直读语音留言 | 远程/桌面worker场景 | 外网 VPN 策略在书外（p198） |
| task-16 | 部署 general announcement 企业广播 | p210-227 | 播报生效（留言/查询前播放） | 品牌化诉求 | 专业录音 wav 制作在书外（p215 录音棚示意） |
| task-17 | 执行 OpenTouch 备份与恢复 | p228-246 | 可运转的备份恢复闭环（含恢复后起服务） | 运维底线动作 | NFS server 部署按 TC2024（p246） |
| task-18 | 启用语音信箱统计 | p247-258 | 统计文件按频率产出（XML/HTML/CSV） | 容量与 profile 优化的依据 | 无 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-08 OTMC/8770 双向声明与同步（对错一处全链路不通，bics.conf 对账是高频坑）
2. task-05 post-installation wizard（站点配置唯一入口，DNS 清单与账户规则在这里定）
3. task-09 OXE SIP 对接（端口 5040/trunk 参数配错即无信箱业务）
4. task-11 账户与信箱交付（业务主体）
5. task-03/06 许可部署与更换（无许可不工作；OK 状态迷惑性高）
6. task-10 用户与话机开通（宿主）
7. task-14 SMTP/SMS 通知（感知最强）
8. task-12/13 profile 与自助门户（日常运营）
9. task-17/18 备份与统计（运维收尾）
10. task-15/16 IMAP 与广播（增值可选）
11. task-01/02/04/07（概念决策与一次性底座动作）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 10 个一级部分（产品 2 + 实验底座 1 + 装机纳管 3 + 业务 1 + 增值与运维 3）
- [x] 术语按实际内容列出（19 个）
- [x] 已检查作者局限/假设（实验口径明文密码、HA/规格外指、OXE/8770 基础假设、Red Hat/CheckSytemLinux 笔误、151/155 网段漂移）
- [x] 原书关键任务 18 项，全部有来源页码、交付物与重要性依据
- [x] 阶段 1 五路提取同步执行（2026-09-23），BOOK_OVERVIEW 与 candidates 相互引用为审计基准

**用户确认时间**: 2026-09-23（流水线授权，五路提取一次完成）
