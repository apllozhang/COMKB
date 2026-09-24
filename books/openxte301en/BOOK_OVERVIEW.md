# OpenTouch Advanced (OPENXTE301EN Ed08) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OpenTouch - Advanced (Participant's Guide)
- **作者**: ALE Training Services（OpenTouch Suite for MLE）
- **出版/发布时间**: Edition 08（OpenTouch R2.6.1 时代；含 TC2258 ed.02 附录，© 2019 ALE International）
- **内容类型**: 课程（官方售后培训讲义幻灯片 + 分步实验 How-To，讲义约占 45%、实验约占 55%）
- **版本来源**: `F:\AIwork\ZCode\books\openxte301en\source_fulltext.txt`（468 页）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To 配对推进；每个主题一章讲义 + 一章或多章 How-To）

### 一句话主旨
把 OXE + OpenTouch 服务器的移动与协作能力交付到位：从 RLAB 实验环境搭建开始，依次打通 Connection 用户的 Nomadic 移动（蜂窝/VoIP）、Desksharing 共享工位、OTC 智能手机与 Extended Mobility（QR/NFC）、远程接入（反向代理/SBC/证书）、统一消息（Exchange/Gmail/IMAP）、目录搜索（UDAS/SBC 合并）、协作会议（ACS/DAS/DCS）、日历同步，最后用外部认证（LDAP/Kerberos/RADIUS）接入企业安全体系。

### 骨架 (主要论点及其关系)

1. **实验环境与 Pod 配置**（RLAB 全虚拟化/混合两种 POD 拓扑、8 台虚机设置表、ITSP1 SIP 运营商模拟器、Pod Configuration How-To：机架/用户/IPDSP/外部 SIP 网关/DID 翻译）
2. **Nomadic 移动模式**（Connection 用户三操作模式、蜂窝模式 Ghost Z 池 + VoIP 模式 SIP 设备池、反向代理/SBC/VPN 接入、tsa_maintenance 维护）
3. **Desksharing 共享工位**（DSU/DSS 机制、前缀 600/601、虚拟 MAC、系统参数、OTC PC 远程释放、domstat/ippstat/incvisu 维护）
4. **OTC 智能手机**（OTC Android/iPhone 原理与用例矩阵、APNS 推送、9 对象自动创建、设备档案、R2.6 远程扩展单设备化、iPhone+ 5265 端口 SBC）
5. **远程接入服务器设置**（反向代理 443/8016、OTSBC 5261/8061、RTP 7000-7499、DAS 规则、ACS 会议 FQDN、证书 CSR→CA→导入→部署全流程）
6. **Extended Mobility**（QR 码/NFC 标签触发呼叫切换与路由修改、一小时周期提醒、支持终端与成本清单）
7. **统一消息 UM**（Exchange CPE/O365 云/Gmail/IMAP4 四后端架构、ICEaccess 特权账号与 Impersonation、语音邮箱系统/档案/信箱分配、MASC/Wireal 维护）
8. **目录搜索 UDAS**（同步数据库、联系人卡 4+5 属性、Single Business Card 合并与 Merge keys、照片同化、LDAP 溢出、Communicate by name）
9. **协作与会议**（三类会议、领导者/参与者角色与 DTMF 控制、Dial by URI、AMS 视频 MCU、会议服务器配置〔桥号/系统选项/SIP 代理/DAS 规则〕、OTC Web、数据会议操作、协作限制）
10. **DCS 与日历同步**（文档转换服务器 Basic/Advanced 两模式与内外部安装、Calendar presence/Calendar synchro 机制与 TC2258 排障）
11. **外部认证**（Downstream：LDAP/RADIUS 插件文件与级联；Upstream：Kerberos SSO 与 WBM 管理员保护；FreeRADIUS 实验服务器）

**论点之间的关系**: 1 是地基（全书实验都跑在 POD 上）；2-5 是"移动性"主线（先服务器侧远程接入打通道，再终端侧 nomadic/智能手机/扩展移动性）；7-8 是"消息与目录"主线（依赖企业邮件与 AD 基础设施）；9-10 是"协作"主线（会议/文档/日历互相咬合：DAS 规则支撑会议呼叫，DCS 支撑文档演示，日历同步支撑会议邀请）；11 是收尾的安全域，反向依赖前面所有应用（外认一开，全部客户端换认证方式）。Nomadic 的 Ghost Z 资源池思想在 2、4 两章重复出现（nomadic Ghost Z 与远程扩展 Ghost Z 共用机制），是全书最核心的复用概念。

### 作者要解决的核心问题
让售后/渠道工程师独立完成"OXE + OpenTouch"解决方案的高级特性交付：为远程/移动员工配齐 Nomadic 与智能手机通道、为企业配好共享工位与目录、接通 Exchange 邮件与日历、搭起带文档与视频的协作会议，并把这些应用纳入企业 LDAP/Kerberos/RADIUS 认证体系——全程能在 RLAB 实验环境复现验证。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| OpenTouch (server/OTMS) | 与 OXE 配套的协作服务器（实验实例 OPEN_OTMS_ADVANCED，192.168.1.50），承载 ACS 协作会议、ICAS 消息、移动性组件 | 不是单个 App，是服务器侧平台；OXE 管呼叫控制，OT 管协作/消息/移动 |
| Connection user / Conversation user | OT 两类用户：Connection 绑定 OXE 话机可享完整电话+协作；Conversation 纯 OT 软用户。_nomadic 服务 dedicated to Connection users_ | 很多特性按用户类型分界（如 Connection 无点对点视频），不是"高级/低级"之分 |
| Nomadic mode | Connection 用户离开办公室时把"当前设备"切到 PC（VoIP）或任意号码（蜂窝）；办公室话机被冻结（frozen） | 是路由+媒体重定向机制，靠 Ghost Z 池落地，不是简单的呼叫转移 |
| Ghost Z set | 虚拟 Z 设备池资源：每路 nomadic 连接占 1 个（蜂窝）或 1 个+1 个 SIP 设备（VoIP），连接期间保持 busy 直至关闭 | 不是用户分机，是按最大并发数规划的池资源；规模=同时连接数 |
| REX (Remote Extension) | OXE 侧远程扩展设备：OTC 智能手机在 OXE 的落地形态，配速拨号实现自动替换（DISA 呼入）；R2.6 起可直接当主设备（单设备） | 书中未展开全称；与 Rainbow 教材的 Remote Extension number 是同一机制家族 |
| DISA | 远程扩展的公网呼入机制：DISA 前缀（实验 31280）+ 自动替换（Automatic DISA Substitution） | 书中未展开全称；需在 DDI 翻译表和中继组两侧放行 |
| Tandem (twinset) | 主话机与远程扩展构成的绑定的多设备结构（两台都必须多线 L1/L2） | 系统自动创建；不是手动配的并行振铃 |
| Desksharing (DSU/DSS) | DSU=无固定设备的共享用户，DSS=共享话机；DSU 用前缀 600/601 登录/登出任意 DSS；DSU MAC 是虚拟的（aa:bb+号码） | OXE 特性 + OTC PC 增强（远程释放、UA 软话机替代冻结）；区别于"免费座位"的单纯硬件热桌 |
| OTC (PC/Mobile/Web) | OpenTouch Conversation 客户端家族：PC、Android（OpenTouch Conversation）、iPhone（Conversation Plus）、Web（浏览器免装） | 同一用户体系三形态；iPhone 版叫 Plus，能力与 Android 有差异（NFC） |
| OTSBC / SBC | OpenTouch 会话边界控制器：远程 OTC 客户端的 SIP/媒体入口（5261）与 WebRTC 入口（8061）；iPhone+ 专用实例端口 5265 | 一台 SBC 按端口/接口分三个角色，不是三台设备 |
| ACS (Advanced Communication Server) | OT 的协作会议组件：会议桥、DAS 规则、电话格式规则、SIP 代理（5260）都在其管理台 | 呼叫路由规则（DAS）挂在 ACS 而非 OXE；与"会议服务器 Administration Console"同义使用 |
| DAS rules | 挂在 ACS 的最多 20 条 Unix 正则，按序处理用户所拨号码（输出接输入）；随国家不同，实验给法国 10 条 | 是 ACS 的拨号计划层，与 OXE 的 ARS/翻译器是两套独立体系 |
| UDAS | Universal Directory Access Service：把 OXE 电话簿/OT 内部目录/外部 LDAP 同步进 PostgreSQL 同步库，所有搜索查同步库 | 搜索不同步时的即时目录；单向同步 + 可选 SBC 合并 |
| SBC (Single Business Card) | UDAS 的目录合并机制：按权重（Synchronization Order）合并多目录联系人卡，用 Merge keys（至少姓+名）识别同一人 | 注意与 OTSBC（会话边界控制器）缩写撞车，全靠上下文区分 |
| UM (Unified Messaging) | 语音留言存到企业邮件服务器（Exchange/Gmail/IMAP）单点存储 Wav 格式；OT 侧建 UM 语音邮件系统+档案+信箱 | 语音邮箱不是 OT 内部存储，是邮件服务器里的邮件；IMAP4 后端功能有裁剪 |
| ICEaccess & Impersonation | OT 访问 Exchange 的特权 AD 账号；R2.3 起 OT 用 Impersonation（应用代持）替代 Delegation | 是"服务账号 acting as 邮箱所有者"，配错是 UM/日历同步最高频故障 |
| APNS | Apple 推送通知服务：OT→iPhone 的通知走苹果云（TCP 5223/2195/2196/443），证书一年一换 | 推送经苹果而非直连，防火墙与年度 hotfix 是 iPhone 部署特有负担 |
| Extended Mobility | 用 QR 码或 NFC 标签（仅 Android）把进行中呼叫切到任意内部话机，或改自己的路由档案；一小时周期提醒回切 | 单向切换不可回切；触发靠贴在话机上的标签，无需装新 App |
| DCS (Document Conversion Server) | 会议文档演示的 Office 文档转换服务器（Basic 模式只支持 pdf/图片）；内嵌 KVM 虚机或外部 Windows+Office 机器 | 与实验环境里叫 DCS 的虚机（192.168.1.31）重名，注意语境 |
| Calendar presence / synchro | presence=把 Exchange 日历状态显示为在场旁注文本（不改颜色码）；synchro=OT 会议与 Outlook 日历双向同步（Wireal/EWS） | presence 只在收藏/名片显示且自己看不到自己的；synchro 有"OTC 周期会议不推送"的限制 |
| DTA | OT 内部认证数据库（DaTa Access）：默认认证源；外部认证失败时 Web 客户端自动级联回 DTA，厚客户端不级联 | 书中未展开全称首字母（只给 "means DaTa Access"） |
| Kerberos SSO (Upstream) | 用 Windows 会话凭据换 Kerberos 票据登录 OT；web.xml 模板重命名启用；ice_kerb 账号+keytab+setspn | 启用后 8770 客户端进不了 WBM，必须预留 wbm_admin 类 AD 管理员 |

### 核心命题 (用自己的话)

1. OpenTouch 方案的分工：OXE 保留呼叫控制与话机生态，OT 服务器承载协作、消息、移动性与目录；客户端（OTC PC/Mobile/Web、话机）统一从 OT 拿服务。
2. Nomadic 的本质是资源池换轨：每路蜂窝连接占 1 个 Ghost Z，每路 VoIP 连接占 1 个 Ghost Z + 1 个 SIP 设备，占住直到用户关闭 nomadic——并发数决定池规模，规划错了就是"人连不上"。
3. Nomadic 权限成对出现：蜂窝要 Nomadic GSM + Desktop，VoIP 要 Nomadic SIP + Desktop（且蜂窝配置是 VoIP 的前提）；OTC PC 侧 Desksharing 远程释放要 Desktop + Flex Office。
4. OXE 侧远程接入是"SIP 网关 + 反向代理/SBC + DAS 规则"三件套：媒体经 SBC（RTP 7000-7499），信令信封经 RP（443/8016），号码格式靠 DAS 正则串行处理——顺序错一条全盘错。
5. OTC 智能手机配置的复杂度被"自动创建"消化：关联手机时系统自动建 RE、SIP 设备、速拨号、识别码规则、ARS 路由表、Tandem，管理员只需核验；R2.6 起手机还能直接当主设备（RE 单设备化）。
6. iPhone 是特例全家桶：APNS 推送（证书一年一换、4 个 TCP 端口）、后台唤醒要多次 SIP INVITE（UDP 强制）、出网走 SBC 时 TCP 强制（OT 做 SIP 代理缓冲）、VoIP everywhere 要 5265 端口专用 SBC 与 kamailio-wasp/wspcfg 两个组件。
7. Desksharing 用"虚拟身份"复用硬件：DSU 无固定话机，MAC 是系统按号码生成的虚拟值；DSS 才有真实 MAC；登录登出靠 600/601 前缀+可编程键，忙时强制登出会产生 6004 事件。
8. 统一消息把语音留言变成邮件：四种后端能力递减（Exchange 全功能、O365 桌面版、Gmail 限 500 用户、IMAP4 砍 PPR/MWI/扩展/消息类别）；Exchange 侧的钥匙是 ICEaccess 特权账号 + Impersonation + CA 证书入信任库。
9. 目录搜索永远查"同步库"：UDAS 把多目录单向倒进 PostgreSQL；开了 Single Business Card 后按权重合并、按 Merge keys 认人、照片按 Avatar>LDAP>本地同化——同步参数（date/time/period≥1）不设就是空库。
10. 会议能力按 ACS 组织：桥号（TUI 应用）双语种、7 位双访问码（领导者/参与者）、DAS 规则管拨号格式、电话格式正则管分机识别、Dial by URI 让任意 H.264 SIP 终端入会；文档演示能不能放 Office 由 DCS 决定。
11. 日历与在场是"邮件侧副产品"：Calendar presence 只加文本不改颜色、自己看不到自己；Calendar synchro 让 Outlook 与 OTC 互建互改会议，但 OTC 建的周期会议不回推 Exchange；排障三板斧是重启 tomcatd/acsd/wireald + 看 wireal 日志 + exchange-connector 队列目录。
12. 外部认证是全局开关不是按应用开关：downstream（LDAP/RADIUS 插件）与 upstream（Kerberos/NTLM）两条路，管理员账号必须预先配好 External login，否则启用即把自己锁在配置工具外面——Kerberos 场景还要专门给 WBM 留一个 AD 管理员。

### 论证链
教材以"讲义机制 → How-To 分步 → 实验验证"推进：每章讲义给架构图与用例矩阵，随后 How-To 用固定实验人物（Barkley 31000 / Backman 31001 / Boop 31002）跑通配置并做行为测试（如 nomadic 测试呼叫、QR 切换测试、日历在场检查）；凡涉及生产差异处用 Warning/Note/Tips 标注，并用 TC 文档指针（TC2341/TC2391/TC2258/TC2558/TC1623）兜底。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 OpenTouch R2.6.1 与 2019 年生态：Radvision MCU 与 UVC LifeSize 已在书中标注"不再支持"，APNS 根证书"有效期至 2022"、Office 兼容表停在 Office 2019——按今天的桌面/移动环境交付必须全部对照最新 release note。
- 智能手机章围绕 3G/4G + WiFi 双模设计，无 eSIM/5G、MDM 批量部署内容；OTC Web 的 WebRTC 仅支持 Chrome/Firefox 的口径也已过时。
- 实验账号密码（letacla/superuser/1234/training 等）明文遍布正文，是 2019 年培训文化产物，不能带入生产安全基线。

### 作者的立场盲点
- 全书默认企业已有成熟的 AD/Exchange/DNS/CA 基础设施：ICEaccess 账号治理、Impersonation 权限收敛、内部 DNS 维护都只有一句话级提示，实际项目里这些是企业侧最慢的环节。
- DAS 规则、ARS、识别码这些"号码计划"内容只给法国口径（+33/00/0），非法国交付要自己推导正则——书内无通用方法论展开。
- 没有任何容量规划视角：Ghost Z/SIP 设备池、会议端口、DCS 转换吞吐都只有"按并发规划"一句话，没有算例。
- OTC Mobile 的 Android/iPhone 差异分散在多章（NFC、端口、协议），没有一页并排总表，交付时容易漏项。

### 未被证明的假设
- 假设学员自带支持 NFC/QR 的智能手机且教室有 6 SSID 热点（Extended Mobility 实验）——生产环境需要现场勘测替代。
- 假设 FreeRADIUS.net 1.0.5（Windows 老旧移植版）可以代表企业 RADIUS——生产对接 Cisco ISE/AD NPS 的行为未验证。
- 假设 Windows CA（eco 服务器 CertSrv）随时可用；用外部 CA（VeriSign 等）时的流程只给了方向。
- 假设"Up to 20 LDAP servers"（讲义）与"Up to five LDAP servers can be declared in the OXE"（实验）两个口径读者会自行分辨适用层——实际是讲义/实验语境未对齐（已作为边界条目收录）。

### 最强反对意见
"这本手册教的是在理想实验室里点亮 OpenTouch 高级特性，不是生产交付方法论"——容量规划、高可用、安全加固、非法国号码计划、企业 IAM 集成细节全部缺位；且版本碎片化严重（R2.0/R2.1 MD1/R2.2/R2.3/R2.3.1/R2.5/R2.6 各章各提一嘴），跨版本交付必须逐章对照版本前提。因此每个能力的 Boundary 必须标注"实验环境口径 + 版本前提"，并显式指向 TC2341（OTC 智能手机 VoIP 部署）、TC2391（UM 实现）、TC2258（日历在场/同步）、TC2558（本地存储邮箱的日历特性）、TC1623（Kerberos 深入）五份技术通报作为生产化依据。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] OpenTouch 实验 POD 搭建与核对（虚机/机架/用户/IPDSP/TFTP/外部 SIP 网关/DID 翻译）
- [x] ITSP1 SIP 模拟器联调与公网/紧急呼叫验证
- [x] Nomadic 蜂窝模式配置（Ghost Z 池 + 权限 + 号码管理）
- [x] Nomadic VoIP 模式配置（SIP 设备池 + OT 侧声明 + SBC）
- [x] Nomadic 资源验证与维护（tsa_maintenance dump/手动同步）
- [x] Desksharing 配置（前缀/DSS/DSU/COS/系统参数四件）
- [x] Desksharing 的 OTC PC 支持与命令行维护（domstat/ippstat/incvisu）
- [x] 反向代理与 OTSBC 声明（WebRTC SBC、NAT/DNS 规划）
- [x] DAS 规则配置与 ACS 会议 FQDN/证书生命周期（rehost/CSR/导入/部署）
- [x] OTC 智能手机交付全流程（OXE 通用参数 → 设备档案 → 用户关联 → 自动对象核验 → 手工补充 → App 安装）
- [x] Extended Mobility 部署（QR 语法/NFC 写标签 + 两类测试）
- [x] Unified Messaging (Exchange) 全流程（特权账号/Impersonation/证书/UM 系统/档案/信箱）
- [x] UM 云上下文（O365/HTTP proxy）与维护（MASC/Wireal）
- [x] 目录搜索部署（内部/电话簿/AD 目录/可选属性）
- [x] Single Business Card 合并目录配置与 UDAS 维护
- [x] 会议服务器配置（桥号/系统选项/SIP 代理/DAS/格式规则）
- [x] 数据会议运用与协作限制（OTC PC/Outlook 加载项/One Touch/远程控制）
- [x] DCS 安装（内部/外部）与声明
- [x] Calendar presence/synchro 实施与排障
- [x] 外部认证配置（LDAP/RADIUS）与 FreeRADIUS 实验
- [x] Kerberos SSO 配置与 WBM 管理员保护

### 不适合 skill 化的内容
- RLAB/POD 拓扑与账号表（p5-18，教学专用基础设施，仅作 Boundary 背景与实验口径引用）
- SIP 模拟器逐号码表格（p21-23，教学专用，引用规则即可）
- FreeRADIUS.net Windows 安装向导逐步截图（p463-465，纯实验工具安装）
- 培训评估/课程目录页（p468）
- Outlook 2013 客户端逐屏配置（p212-214 等通用 Office 操作）

### 预估 skill 数量
**约 12-14 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；入口软预算 8 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 搭建并核对 OpenTouch 实验 POD（虚机启动、机架/板卡、用户/IPDSP/TFTP、外部 SIP 网关、DID 翻译） | p24-30 | 可用的实验 POD | 全书实验地基 | 实验口径（RLAB 专用） |
| task-02 | 用 ITSP1 模拟器验证公网/紧急呼出呼入 | p19-23 | 内外互通的 SIP 中继 | 后续所有话音实验的前提 | 实验口径 |
| task-03 | 配置 Nomadic 蜂窝模式（Ghost Z 池、Nomadic GSM+Desktop 权限、号码管理） | p45-51 | 可切换到任意号码的移动用户 | 移动性主线第一站 | 并发数规划在书外 |
| task-04 | 配置 Nomadic VoIP 模式（SIP 设备池、OT 侧 OXE SIP Subscriber/SBC） | p51-54 | 可用 PC 软话机接听的移动用户 | 依赖 task-03 | SBC 生产部署细节在书外 |
| task-05 | 验证与维护 Nomadic 资源（tsa_maintenance dump/手动同步） | p55-57 | 资源一致性结论 | 排障抓手 | 无 |
| task-06 | 配置 Desksharing（前缀 600/601、DSS/DSU、COS、四个系统参数） | p62-71 | 可登录/登出的共享工位 | 共享工位场景刚需 | 无 |
| task-07 | 配置 Desksharing 的 OTC PC 支持并做命令行维护 | p72-75 | 远程释放能力 + domstat/ippstat/incvisu 排障 | Desksharing 运维闭环 | 无 |
| task-08 | 声明反向代理与 OTSBC（含 WebRTC SBC、NAT/DNS） | p103-107 | 远程客户端可达的接入通道 | 所有远程特性前提 | 生产证书/防火墙策略在书外 |
| task-09 | 配置 DAS nomadic 规则、ACS 会议 FQDN、证书全生命周期 | p108-118 | 会议邀请链接可解析、证书 SAN 正确 | 邮件邀请与安全的基础 | 非法国号码计划需自推导 |
| task-10 | 配置 OXE 通用参数（ARS 前缀/DISA/RE 前缀/Ghost Z/速拨范围/SIP 定时器） | p120-127 | 智能手机特性的 OXE 侧基座 | task-11 的前置 | 无 |
| task-11 | 声明 iPhone+ SBC、同步 OXE 前缀、录 DISA 公网号与 ARS 信息 | p127-129 | OT 侧基座（5265 SBC、前缀同步） | iPhone 特性必需 | 无 |
| task-12 | 建设备档案与用户（OTC Smartphone 关联、Off site mobility、R2.6 单设备特例） | p129-136 | 手机已关联的 Connection 用户 | 智能手机交付核心动作 | 无 |
| task-13 | 核验自动 OXE 对象并补手工项（Entity 识别码/公网 COS）+ 安装 App + 维护 | p137-147 | 端到端可用的智能手机用户 | 交付验收 + 长期维护 | 无 |
| task-14 | 部署 Extended Mobility（QR 生成/NFC 写标签）并做切换与路由修改测试 | p148-167 | 可扫码/碰一碰的移动办公 | 差异化卖点场景 | NFC 标签采购与 BP 验证 |
| task-15 | 部署 UM（Exchange）：ICEaccess/Impersonation/CA 证书/邮件服务器/UM 系统/语音邮箱档案/信箱分配 | p182-210 | 留言进邮箱的语音邮件 | UM 主线 | 无 |
| task-16 | 配置邮箱权限、云上下文（O365/HTTP proxy）与 UM 维护（MASC/Wireal） | p190-193, 211-217 | 全量用户可用的 UM + 排障抓手 | 多用户上线与运维 | 无 |
| task-17 | 部署目录搜索（内部/电话簿同步、AD 目录、可选属性） | p243-251 | 多目录可搜 | 来电识别与找人对 | 无 |
| task-18 | 启用 SBC 合并目录与 UDAS 维护（merge keys/照片/日志） | p252-257, 258-263 | 唯一名片体验 + 目录运维 | 大企业多目录场景 | 无 |
| task-19 | 配置会议服务器（桥号 TUI、系统选项、SIP 代理、DAS、格式规则） | p308-320 | 可拨入的会议桥 | 协作主线基础 | 无 |
| task-20 | 运用数据会议（预约/免预约、Outlook 加载项、One Touch、协作限制、远程控制） | p338-362 | 端到端会议能力 | 日常使用与权限治理 | DCS 决定 Office 演示（task-21） |
| task-21 | 安装并声明 DCS（内部 KVM/外部 VM）实现 Office 文档演示 | p363-383 | Office 文档可做会议演示 | 会议体验补全 | Windows/Office 许可自备 |
| task-22 | 实施 Calendar presence 与 Calendar synchro（含 TC2258 排障） | p384-414 | 日历状态可见、会议双向同步 | UM 的增值与高频排障 | 本地存储邮箱走 TC2558 |
| task-23 | 配置外部认证 LDAP/RADIUS 与 FreeRADIUS 实验服务器 | p415-442, 456-467 | 企业账号可登录 OT | 安全集成基础 | 管理员账号必须先行 |
| task-24 | 配置 Kerberos SSO 并管理 WBM 访问 | p443-455 | Windows 单点登录 OT | 无缝体验 + 高风险变更 | 需预留 wbm_admin 类账号 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-08/09 远程接入与证书（一切远程特性的通道与安全底座，配错面最大）
2. task-10~13 OTC 智能手机交付链（篇幅最大、步骤最多、版本陷阱集中）
3. task-15/16 UM 部署（企业邮件打通，Impersonation 是高频故障点）
4. task-03~05 Nomadic（移动性基础，资源池规划思想复用全书）
5. task-19/20 会议服务器与数据会议（协作主线）
6. task-23/24 外部认证（一开全局生效，先配管理员是保命规则）
7. task-22 日历同步（高频排障场景）
8. task-17/18 目录搜索与 SBC
9. task-14 Extended Mobility（轻量但依赖手机实验环境）
10. task-06/07 Desksharing、task-21 DCS、task-01/02（实验支撑类）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 11 个一级部分（实验地基 1 + 移动性 4 + 消息/目录 2 + 协作 3 + 安全 1，封面/附录未计入）
- [x] 术语按实际内容列出（22 行）
- [x] 已检查作者局限/假设（2019 生态、明文密码、法国号码计划缺位、容量规划缺位、版本碎片化、LDAP 上限口径冲突）
- [x] 原书关键任务 24 项，全部有来源页码、交付物与重要性依据
- [x] 用户已授权全流程连续执行（"现在开始"，2026-09-23）——骨架要点已在本文件固化，可随时纠偏

**用户确认时间**: 2026-09-23（全流程授权）
