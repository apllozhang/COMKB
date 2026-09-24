# OXO Connect Advanced (OXOCXTE301EN Ed18) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OXO Connect - Advanced (Participant's Guide)
- **作者**: ALE Training Services（Alcatel-Lucent Enterprise）
- **出版/发布时间**: Edition 18（OXO Connect R6.3 时代；部分章节内容延伸至 R6.2 证书体系与 2023/2025 年路线图注记）
- **内容类型**: 课程（官方售后进阶培训讲义幻灯片 + 分步实验 How-To，讲义约占 65%、实验约占 35%）
- **版本来源**: `F:\AIwork\ZCode\books\oxocxte301en\source_fulltext.txt`（601 页，带 ===== PAGE N ===== 标记）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商进阶培训教材：概念讲义幻灯片 + 分步实验 How-To；比 RAINXTE001EN 更偏 PBX 侧深度配置，Rainbow 仅占一章半）

### 一句话主旨
把 OXO Connect（R6.3）的高级能力讲透并配实验：从实验环境与 OMC 基础，到公网/私网 SIP 组网与 ARS 路由、酒店/计费/账号码等垂直方案，到 AA/MLAA/SCR/语音邮箱等呼叫处理增强，再到 Cloud Connect 云舰队管理、系统安全与证书体系、DECT 移动部署和 Webdiag/LoLa 维护工具。

### 骨架 (主要论点及其关系)

1. **培训实验环境**（RLAB POD 结构 + ITSP1 SIP 运营商模拟器：拓扑、号码规则、账号、IPDSP 安装时间同步前提）
2. **OMC 基础与接入准备**（OMC 安装首连、证书信任、密码、客户信息；OXO 与 PC 的 IP 规划修改）
3. **公网 SIP 网关**（ITSP1G1 九个参数 tab、编号计划、VoIP 中继/中继组、注册验证、Webdiag+Wireshark 抓包）
4. **垂直方案：酒店与计费**（Hotel 模式向导与参数、OHL/PMS、Hotel Metering、Call Accounting Time based、旋转 DDI、房态、Office Link Driver、账号码与内部替代）
5. **终端与话机生态**（AudioHub、8088 Smart DeskPhone、SIP 话机注册与编解码透传/RTP Proxy、Zoiper 软话机、ALE-2/3、PIMphony、Multiset、站群监督）
6. **呼叫处理增强**（Hot Desking、ARS 多运营商、私网 SIP+ARS 组网、Internal ARS 按时段路由、多实体/伪多公司、语音邮箱高级、AA、MLAA、SCR、游牧与远程替代）
7. **云与远程管理**（Cloud Connect 架构与注册、Fleet Dashboard/OXO Connectivity、软件更新、Inventory、远程维护三种接入）
8. **安全与证书**（密码体系与自动检查、Network IP Services、ETH1 限制、数字证书 2K/4K、DTLS、SIP 中继 TLS/SRTP 原生与 OCE-FE 代理）
9. **DECT 移动**（硬件谱系 8378/8379/8328、DECT 标准帧结构与标识、注册、同步/切换/集群、站点勘测、SUOTA、8158s/8168s VoWLAN）
10. **维护工具与收尾**（Webdiag 全景与三会话、debug 工具、noteworthy 地址修改、LoLa 加载迁移、培训结束清理与评估）

**论点之间的关系**: 1-3 是地基（环境与基本外联），4-6 是并列的三大能力域（垂直方案/终端/呼叫处理，均为"概念讲义 + How-To 实验"配对），7-9 是进阶域（云管理、安全、DECT，多数只有讲义或演示），10 是运维收尾。全书的隐含主线是"OMC/Webdiag 双工具操作 + 编号计划/中继组/ARS 三件套"，所有增强功能最终都落到这两条操作轴上。

### 作者要解决的核心问题
让已掌握 OXO 基础的售后/渠道工程师进阶为能独立交付复杂站点：配公网与私网 SIP 中继并做 ARS 选路与溢出、上酒店等垂直方案、配自动话务员与智能路由、打通移动与游牧场景、用 Cloud Connect 远程管队、把系统安全与证书做到生产级，并能用 Webdiag/LoLa 自主排障与重装。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| OMC | OXO 的 Windows 管理工具（Expert 模式 LAN/WAN 连接，服务器认证，含 Security/Numbering/External Lines/Voice Processing/ACD-SCR 等对象树） | 不只是"配置界面"：还内置 Webdiag 入口、LoLa 配套、MLAA 图形树编辑器 |
| Webdiag | OXO 的 Web 调试工具（https://OXO@IP/services/webapp/，installer/operator/manufacturer 三种会话），管证书、抓包、DECT、Hot Desking、解锁账户、Cloud Connect/Rainbow 状态 | 它是"证书管理主接口"与"远程维护入口"，不只是日志查看器 |
| ITSP1 | RLAB 公共区的 SIP 运营商模拟器（gateway1/public.itsp1.com），账号 pbxP/alcatel，模拟公网/紧急号码 | 教学专用基础设施，所有公网 SIP 实验的"假运营商" |
| IPDSP | 实验室主用 IP 软话机（分机 104），安装前必须先改 IP 并完成 NTP 时间同步（否则 lanpbx 加载错误） | 不是产品名，是实验用 ALE 软话机客户端 |
| ARS (Automatic Route Selection) | 按被叫号码与时间自动选最优路由（中继组），饱和/故障时溢出；透明于用户；适用任何中继/呼叫/接入/拨号 | 三张表协作（编号计划→ARS 表→中继组列表），还承担号码变换（加/吸收/替换/透明）与多运营商分流 |
| Internal ARS | 用 ARS 机制把一个 DDI 按日组+时段路由到不同内部目的地（分机/消息），用虚拟 Provider + Local 索引中继组列表实现 | "内部"指目的地是内部分机而非外线；配置走的是公网编号计划入口 |
| Entity（实体） | OXO 系统内最多 4 个逻辑公司：每实体独立 MoH、可禁止实体间呼叫；话务员组对所有实体公共且不受限 | 不是分公司数据隔离（用户/中继仍共享），是"伪多租户"的柔和版 |
| Pseudo multi-company | 用流量分担链路类别（话机↔中继组匹配 + 矩阵直线）+ ARS 透明线 + Char 显示字符，让两家公司共用一台 OXO 且各走各的外线 | 靠"链路类别配对"实现的记账隔离，靠 ARS 而非硬隔离 |
| Multiset / Twinset | 两或三台话机（有线/移动）共享主站目录号与服务级别；1 主站最多 2 副站；常见主有线+副 DECT 即 Twinset | 与 Rainbow 侧 Twinset（虚拟副站）同名不同物：本书指 PBX 内话机组 |
| Hot Desking (HDP/HDU) | 共享话机资源：HDU 在任意 HDP 登录取回个人环境；HDP 前 200/HDU 前 200，HDU 前 2 免费；前缀 683 登录/682 注销 | HDP 是"位子"，HDU 是"人"；抢占登录时前一人自动注销 |
| Nomadic mode | 游牧话机（多为手机）替代本地话机：本地话机可物理可虚拟；经 VMU 远程定制选项 #6 激活并设目的地 | 不是"呼叫转移"：还影响 CLI 发送规则与计费小票内容 |
| Remote substitution | 拨远程替代 DDI + 远程接入码 + 分机号 + 密码，"变成"该分机打电话；内部号码需 # 前缀经内部 ARS（#100-#199） | 与 Account code 前缀 66 的"替代拨号"是同一密码菜单（Remote Access Code）的两个入口 |
| Account code | 把外呼费用记到客户/项目账号：表上限 250，码最长 16 位，可要求密码/身份识别，小票可掩码 0-9 位 | 也被挪用为"权限钥匙"：内部替代示例里码 1000 就是经理的国际长途权限 |
| OHL / PMS | OXO Connect Hotel Link（Office Link Driver）：V24 或 IP 连接酒店应用（PMS）同步 check-in/out 等；AHL 兼容，无软件 license | OHL 是协议/驱动，PMS 是酒店管理软件；无 OHL 时前台用话机内置 Hotel 功能键 |
| AA (Automated Attendant) | 集成自动话务员：两棵树（白天 Normal/夜间 Restricted）、每树两级 100 节点、每级 10 选、4 语言；定制树与语音需 license | 与 MLAA 是两个应用：AA 每系统一套，MLAA 按 DID/CLI 路由最多 5 棵树 |
| MLAA | Multiple Automated Attendant：基于 ACD 引擎，按 DID/CLI 路由来话，最多 5 棵树、3 级、每树 4 语言；端口与 ACD 共享（16 上限） | 树配置在 OMC 图形界面编辑后"传输到服务器"；消息总量 12000 秒硬上限 |
| SCR (Smart Call Routing) | 按 CLI/DDI/DTMF 客户码/开闭时间路由来话到 ACD 组、MLAA 组、本地/外部目的地；规则 10000 条，编辑器内嵌于 ACD 呼叫路由表 | "客户码"是 DTMF 互动（Voice Prompt 1-8 + 输码#），不是账号系统 |
| Cloud Connect (CCI) | OXO 发起的永久 HTTPS + 按需 VPN 连接（无需改防火墙规则）；Fleet Dashboard（舰队/合同/Inventory/SW 更新）与 OXO Connectivity（单系统 VPN/调试/更新） | 注册全自动、免 license、默认启用；Fleet 数据库一天刷新一次（24 小时延迟） |
| Noteworthy address | 内存读写地址（labels/flags）：timers/debug labels/other labels/numeric 四类；写错可致系统恶化；cold reset 复位；清单在 TC1398 | 是"地下层配置"：PerAssAlwd、DivRemCust、AATypTrf、MLTSETRING、AutoPwdChk、VMUMaxTry 等都藏在这里 |
| DTLS | ALE VoIP 话机信令通道加密（TLS 1.2），语音包仍明文（非 SRTP）；仅 OCE，最多 300 连接，免 license；Generic（零接触）/Specific（锁定端点）两模式 | 保护的是信令不是语音；移动话机跨系统要清 TrustList（三法） |
| OCE-FE SIP PROXY | OCE Front-End 在原 WebRTC 网关之外新增 SIP TLS/SRTP 代理角色，为不支持原生 TLS 的 OCO 等平台转发安全中继；GW 与 PROXY 各 20 通话上限 | OCE-FE 无 PBX 能力；OCE 自身 TLS/SRTP 原生免 license，无需 FE |
| DECT IP-xBS / IBS | 8378 IP-xBS（IP 侧，12 时隙 11 并发，最多 80/200 手柄）与 8379/4070 IBS（TDM 接 UA，每 IBS 6 并发，最多 60）；同一 PARI，混合部署可共存 | 切换（handover）只在同集群内；跨站点（>1km）不切换；Relay xBS 承载媒体信令 |
| LoLa | 完整加载 PowerCPU/OCE 的工具（呼叫处理软件+VoIP/ACD 应用包+license），支持 Installation/迁移 Mono CPU/Install-Restore 三类；OCE 进 LoLa 模式按住电源键至 LED 快闪绿 | 它管"系统级重装与迁移"，话机配置与语音提示仍要 OMC 先保存 |

### 核心命题 (用自己的话)

1. 实验环境决定一切取值口径：OXO 在 192.168.1.246、PC 在 .10、网关 .254、DNS1 .250、DNS2 10.20.30.250，全部 IP/账号/号码是"实验口径"，生产必须替换。
2. OMC 首连走 Expert+LAN/WAN+服务器认证：默认地址 192.168.92.246、首连密码 pbxk1064（仅首次），证书装进"受信任的根证书颁发机构"后告警消失；客户信息带 * 必填且首次强制。
3. 公网 SIP 网关是一套固定顺序：IP/DNS → 编号计划（DDI/安装号）→ VoIP 接入+中继组+链路类别 → 网关九 tab（DNS tab 必须先于 Domain Proxy tab）→ SIP 账号 → 回填网关索引 → History Table 看 "SIP registration success" → Webdiag 抓包 Wireshark 验证。
4. Media tab 的"带宽最少 5 通话"是放行外呼的隐藏闸门：不设带宽就不通，公网私网网关同理。
5. 酒店方案有两条路线：有 PMS 走 OHL（Office Link Driver，V24/IP，免 license），无 PMS 用前台话机内置 Hotel 功能键；容量 300 话机、前台 4 并发会话、房对房可闭锁。
6. 计费三件套：Hotel Metering（预付/切断/阈值）、Call Accounting Time based（无 AOC 中继按时长出脉冲，激活时 AOC 脉冲停用，免 license）、Office Link Driver 的 TicketCollector.xml（XML 小票供外部计费应用）。
7. ARS 是路由中枢：编号计划（Main/Secondary Trunk Group base ARS）→ ARS 表（前缀匹配/号码变换/子线溢出）→ 中继组列表（顺序+字符 Char+Provider）；溢出靠子线，传真强制走特定路由靠流量分担矩阵。
8. Internal ARS 用"虚拟 Provider + Local 索引"实现一个 DDI 按日组+时段分流到不同分机或欢迎消息——把外呼路由机制反转成了来电分配机制。
9. 多实体（4 个）提供 MoH 隔离与可选的实体间呼叫禁止；伪多公司再加流量分担链路类别配对（话机类别=中继组类别+矩阵直线），让两家公司共享系统但各走各的外线、小票各记各账。
10. 呼叫处理三层次递进：AA（一套树两级）→ MLAA（按 DID/CLI 路由最多 5 棵树 3 级，端口与 ACD 共享 16）→ SCR（10000 条规则，客户码 DTMF 互动+开闭时间+备份目的地）。
11. 移动性双通道：游牧模式（VMU 远程定制 #6 激活，CLI 按"外部 CLI/内部 DDI/安装号"规则发送）与远程替代（DDI+接入码+分机+密码，内部呼叫用 #100-#199 经内部 ARS 回环）。
12. 安全生产基线五支柱：强制改默认密码+自动密码检查（AutoPwdChk 默认 4 周）、Network IP Services 收敛 WAN 面、ETH1 限 SIP 网关、远程接入锁定（VMUMaxTry 翻倍至 1440 分钟）、证书体系（R6.2 起 OpenSSL V3 + 4K 证书，回滚前必须先切回 2K）。
13. 远程维护的通用法则：所有互联网入站流量的目标端口必须是 50443；IAD 端口转发"公网任意端口→50443"；公共 443 被占时换端口；更安全走管理 VPN 专用地址（仅 OMC 可配，warm reset 生效）。
14. Cloud Connect 把舰队管理搬上云：OXO 主动外连（免改防火墙）、注册免 license 自动完成、Fleet Dashboard 管多台（需 advanced 权限更新软件）、OXO Connectivity 管单台；数据库一天一刷新。
15. DECT 是一套完整的无线子系统：标准（ETSI EN 300 175/444，FDMA/TDMA/TDD 24 时隙）、标识（PARI/PARK/IPUI/RFPI）、集群与空口同步、Relay xBS 切换、SUOTA 空中升级；勘测以 -72 dBm 为语音质量边界。

### 论证链
全书以"概念讲义 → OMC/Webdiag 分步操作 → 行为验证"推进：每个 How-To 都有显式测试动作（拨号看显示字符、看 History Table 消息、看 LED、听提示音、查 TicketCollector.xml），用行为闭环替代理论论证；容量与限制用数字表（AA/MLAA/SCR 规格表、DECT 限制表、OCE-FE 20 通话表）支撑；少数架构判断（Direct RTP vs RTP proxy vs DSP 三处理）用对比图说明取舍。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 R6.3/Ed18 界面截图；PIMphony 是 Windows 专用软话机（PC 中心时代产物），与当下 Rainbow/桌面话机主线渐行渐远。
- 8214 话机兼容性注记停在"R5.2 计划 2023 底"、预定义消息图标"计划 2023 底"，酒店 PMS 生态列表引到 2025 年 11 月 PDF——跨版本交付需逐一核对最新 TC。
- Cloud Connect/Fleet Dashboard 域名在书内出现两种写法（al-enterprise.com 与 enterprise.alcatel-lucent.com 混用），门户演进快，以登录页实际域名为准。

### 作者的立场盲点
- 全书默认实验环境：明文密码（pbxk1064 / alcatel / OMCAdmin / Superuser / 实验接入码 780911、615243 等）遍布正文，生产安全基线只指向 TC1143，未展开。
- 一半以上高级功能（MLAA/SCR/ACD/多实体/Hot Desking/PIMphony/IP-DECT 用户）依赖 license 或软件键，但书内无一处给 license 规划方法——"哪些功能要先买票"要读者自己拼。
- 安全章讲了大量加固开关，却没有威胁模型：什么场景该开 ETH1 限制、什么时候该关远程维护，全靠工程师自行判断。
- 部分讲义页沿用 OXE 素材（"NOE SIP for OXE" 水印残留于 p73/82/501/550），个别页有法文残句（p191/345/502）与前后不一致（DHCP 范围 p34 vs p40；Internal ARS 时段 p233 vs p449）——照抄步骤前要先对齐自家软件版本。

### 未被证明的假设
- 假设学员有 RLAB POD 与 ITSP1 模拟器（生产中没有：公网 SIP 的号码变换、注册超时、运营商鉴权差异都要重新勘测）。
- 假设 IBS/IP-DECT 硬件可上手（两处 lab 明说"In Virtual Classroom: This lab is not possible"），实际部署节奏与站点勘测在书外（仅给 SSK 手册号 8AL90874USAA）。
- 假设 OCE 平台为主（DTLS、SIP TLS/SRTP 原生、4K 证书升级均限 OCE 或 OCE 优先）；OCO 老平台走 OCE-FE 代理的方案只给了能力表，没给迁移路径。
- 假设 Cloud Connect 门户账号（Business Store）与 SA 合同现成可用。

### 最强反对意见
"这本教材教的是按钮位置，不是方案设计"——AR S 表怎么规划前缀、MLAA 树怎么设计菜单、DECT 基站怎么布点、证书选 2K 还是 4K，教材只给机制与上限，不给方法论；站点勘测、license 规划、安全策略全部外置（TC1143、TC1398、Global Limits、SSK 手册、hospitality ecosystem PDF）。因此每个能力的 Boundary 必须标注"实验环境口径"，并把 TC1143（安全）、TC1398（noteworthy 清单）、TC2249（密码审计）、TC002（V24）、TC2349（WinPDM）、OXO Connect Global Limits、8AL90874USAA（SSK）列为生产化依据。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] RLAB/ITSP1 实验环境搭建与取值口径（仅作实验复现背景）
- [x] OMC 安装、首连与证书信任
- [x] OXO 与客户端 IP 规划修改（含 IPDSP 时间同步前提）
- [x] 公网 SIP 网关配置九步法（含"DNS tab 先于 Domain Proxy"顺序约束）
- [x] SIP 注册验证与 Webdiag/Wireshark 抓包排障
- [x] 酒店模式部署（Wizard Hotel、Hotel 参数、旋转 DDI、房态）
- [x] 酒店计费（Hotel Metering、Call Accounting Time based、Office Link Driver）
- [x] 账号码与内部替代（含"经理锁机远程外呼"场景）
- [x] 站群监督（Supervision Groupware + Audio Signal 两键）
- [x] PIMphony 安装、profile 与在线更新策略
- [x] SIP 话机/软话机接入（Basic/Open SIP、Zoiper、ALE-2/3、编解码透传与 RTP Proxy）
- [x] SIP 话机维护（Webdiag SIP 工具、状态表、远程 SSH trace）
- [x] Hot Desking 配置与监督
- [x] Multiset 配置与行为验证
- [x] ARS 多运营商路由与溢出（GSM/ADSL/ISDN 三路示例）
- [x] 私网 SIP 组网 + ARS 双向溢出（私→公、公→私强制）
- [x] Internal ARS 按日组/时段路由 DDI
- [x] 多实体与伪多公司配置
- [x] Cloud Connect 注册与舰队管理（Fleet Dashboard/OXO Connectivity/SW 更新/Inventory）
- [x] 远程维护接入方案（电话网 DDI/V24/互联网 50443/管理 VPN）
- [x] Rainbow 业务目录自助同步（EC Selfcare）
- [x] 系统安全加固（密码体系/自动检查/审计工具/Network IP Services/紧急号码/LDAPS）
- [x] 数字证书管理（自签/外部 PKI、2K↔4K 迁移与回滚）
- [x] DTLS 原生加密部署与端点清除
- [x] SIP 中继 TLS/SRTP（OCE 原生 + OCE-FE 代理）
- [x] 语音邮箱高级管理（个人助理/远程接入/ACC 两级控制/锁定解锁）
- [x] 自动话务员 AA 配置（树+语音指南+免费拨号）
- [x] MLAA 多树话务员（图形树编辑+消息管理+传输）
- [x] Smart Call Routing 客户码路由
- [x] 游牧模式与远程替代（含 # 前缀内部 ARS）
- [x] DECT 话机注册（IBS/xBS 两法）与 IP-DECT 部署
- [x] DECT 站点勘测与覆盖判定（-72 dBm 口径）
- [x] Webdiag 排障全景与 noteworthy 修改
- [x] LoLa 系统加载与迁移

### 不适合 skill 化的内容
- 8088/AudioHub/ALE-2/ALE-3/8158s/8168s 等硬件产品规格页（p102-110、482-486、549-552，销售口径，仅作选型背景）
- 培训评估/证书下载流程（p592-601）
- RLAB 门户操作细节（p8-12，教学专用基础设施）
- Fleet Dashboard/OXO Connectivity 的演示视频页（p283/285，无文字步骤）

### 预估 skill 数量
**约 14-16 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；入口软预算 8 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 安装 OMC 并首次连接 OXO（Expert、服务器认证、证书、改密、客户信息） | p23-32 | 可用的 OMC 管理连接 | 一切 PBX 侧配置的前提 | 无 |
| task-02 | 修改 OXO 与客户端 IP 规划并重启生效 | p33-36 | 按客户网段可管理的新地址 | 现场交付第一步；IPDSP 前提 | 无 |
| task-03 | 配置公网 SIP 网关并验证注册（九 tab、编号计划、中继组、抓包） | p37-56 | 注册成功的外呼通道 | 对接运营商的标准动作 | 生产运营商参数在书外 |
| task-04 | 部署酒店模式（Wizard Hotel、参数、旋转 DDI、房态、OHL 选型） | p57-75 | 可运营的酒店话务 | 垂直行业刚需 | PMS 对接细节在 DSPP/生态 PDF |
| task-05 | 启用 IP 计费并部署 Office Link Driver 生成 TicketCollector.xml | p76-91 | XML 计费小票输出 | 计费/对账基础 | 外部计费应用在书外 |
| task-06 | 配置账号码与内部替代并测试 | p92-101 | 按客户/项目记账与异地权限外呼 | 多租户记账与权限场景 | 无 |
| task-07 | 配置站群监督两键并验证通知 | p111-118 | 多号码同时监督能力 | 前台/助理场景 | 无 |
| task-08 | 安装 PIMphony、配 profile 与在线更新策略 | p119-138 | 可用的 PC 软话机 | PC 中心用户场景 | license 依赖；虚拟课堂不可做 |
| task-09 | 声明 SIP 话机并接入选型（Basic/Open、Zoiper、编解码透传） | p139-165 | 注册成功的 SIP 分机 | 第三方话机接入标准路径 | 白名单清单在 DSPP |
| task-10 | 用 Webdiag 维护 SIP 话机（状态/抓包/远程 SSH） | p166-172 | SIP 话机排障闭环 | 售后日常 | 无 |
| task-11 | 配置 Hot Desking（HDP/HDU/前缀/监督） | p173-183 | 共享话机资源可用 | 工位共享场景 | license：前 2 免费 |
| task-12 | 配置 Multiset 并验证五种呼叫行为 | p184-192 | 主副话机组可用 | 有线+移动用户刚需 | 无 |
| task-13 | 组私网 SIP 网络并配 ARS 双向溢出 | p193-224 | 站间互拨+公网溢出+优先强转 | 多站点组网核心 | 带宽勘测在书外 |
| task-14 | 配 Internal ARS 按日组/时段路由同一 DDI | p225-241 | 分时段来电分配+非营业时间消息 | 一号多目的地场景 | 无 |
| task-15 | 配多实体隔离与伪多公司分账 | p242-261 | 实体隔离+分公司外线分账 | 共享系统多客户场景 | 4 实体 MoH license |
| task-16 | 注册 OXO 到 Cloud Connect 并验证 | p262-289 | 舰队可见（24h 延迟） | 云运维第一步 | Business Store 账号 |
| task-17 | 用 Fleet Dashboard/OXO Connectivity 管舰队与更新软件 | p269-285, p269 SW 更新 | 版本治理闭环 | 批量运维刚需 | advanced 权限 |
| task-18 | 选型并配置远程维护接入（电话网/V24/互联网 50443/管理 VPN） | p290-306 | 安全可达的远程管理通道 | 无 ISDN 站点唯一选项 | TC1143 安全基线 |
| task-19 | 配 Rainbow 业务目录同步到 OXO 集体目录 | p307-310 | Dial by Name+主叫识别 | EC 自助、零成本 | Rainbow 公司与编号保留段 |
| task-20 | 执行系统安全加固（密码/自动检查/审计/WAN 面/紧急号码/LDAPS） | p311-338 | 生产级安全基线 | 上线必做 | TC1143 全文 |
| task-21 | 管理数字证书（自签/外部 PKI、2K↔4K、回滚注意） | p339-358 | 合规证书体系 | R6.2 起强相关 | 企业 PKI 流程在书外 |
| task-22 | 部署 DTLS 原生加密（两模式、状态核查、端点清除） | p359-364 | 话机信令加密 | OCE 安全通信 | 仅 OCE；跨系统移动要清 TrustList |
| task-23 | 配 SIP 中继 TLS/SRTP（OCE 原生或 OCE-FE 代理） | p365-378 | 加密中继通道 | 运营商加密要求 | 运营商 TLS 参数在书外 |
| task-24 | 配语音邮箱高级功能（个人助理/远程接入/ACC/锁定解锁/寻线组邮箱） | p379-404 | 安全可远程管理的 VM | 防盗打+移动办公 | 无 |
| task-25 | 配自动话务员 AA（树、语音指南、免费拨号、盲转） | p405-426 | 可用的语音导航 | 企业门面 | 树定制需 license |
| task-26 | 配 MLAA 多树多语言话务员 | p427-449 | 按 DID/CLI 的多棵导航树 | 多业务线入口 | MLAA license（1/5 树） |
| task-27 | 配 Smart Call Routing 客户码路由 | p450-462 | 按客户码分流来话 | 客服分客户场景 | SCR+Supervisor Console license |
| task-28 | 配游牧模式与远程替代（含 # 前缀内部 ARS） | p463-480 | 手机替代分机+异地呼内部 | 移动办公核心 | 无 |
| task-29 | 注册 DECT 话机并部署 IP-DECT（IBS/xBS、同步、勘测、SUOTA） | p481-548 | 无线移动覆盖 | 厂区/仓库刚需 | 站点勘测按 SSK 手册 |
| task-30 | 用 Webdiag 排障并修改 noteworthy 地址 | p553-581 | 自主排障+系统级调参 | 售后进阶必备 | TC1398 地址清单 |
| task-31 | 用 LoLa 加载/迁移系统 | p582-591 | 系统重装或换 CPU 迁移 | 灾备/硬件更换 | 交付文件与 license 文件 |

### 优先级排序 (按"最能进阶售后工程师"的角度)
1. task-03 公网 SIP 网关（外联生命线，九 tab 顺序是高频踩坑点）
2. task-13 私网 SIP+ARS（多站点组网核心，双向溢出最考验 ARS 理解）
3. task-14 Internal ARS（把 ARS 反转为来电分配，思路价值最高）
4. task-20/21/22/23 安全与证书四件套（R6.2 生产基线）
5. task-30/10 Webdiag 排障（售后日常杠杆最大）
6. task-24/25/26/27 呼叫处理增强（AA→MLAA→SCR 递进）
7. task-28 游牧与远程替代（移动场景刚需）
8. task-04/05/06 酒店与计费（垂直项目整套）
9. task-29 DECT（硬件项目整包）
10. task-16/17/18/19 云与远程管理（运维提效）
11. task-01/02 基础、task-07/08/09/11/12 终端与共享、task-15 多实体、task-31 LoLa（支撑类）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 10 个一级部分（环境地基 3 + 能力域 3（垂直/终端/呼叫处理）+ 进阶域 3（云/安全/DECT）+ 维护收尾 1）
- [x] 术语按实际内容列出（24 个）
- [x] 已检查作者局限/假设（实验口径、明文密码、license 规划缺位、OXE 素材残留与前后不一致、跨版本路线图时效）
- [x] 原书关键任务 31 项，全部有来源页码、交付物与重要性依据
- [x] 工作区此前为空（仅 source_fulltext.txt），本次为全新产出，无续写/重写问题

**处理说明**: 2026-09-23 由提取阶段执行者依流水线任务书一次性完成阶段 0+1（全流程授权口径，同 RAINXTE001EN 先例）。
