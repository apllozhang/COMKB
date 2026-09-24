# OmniPCX Enterprise SIP (ENTPXTE403EN R101.1 MD4 Ed12) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OmniPCX Enterprise - SIP (Participant's Guide)
- **课程代号**: ENTPXTE403EN
- **作者**: ALE Training Services
- **出版/发布时间**: Edition 12（对应 OmniPCX Enterprise R101.1 MD4；截图含 R100.0 / R101.0 / R101.1 多版本踪迹，安装菜单显示 Installation FACILITIES 4.00.105）
- **内容类型**: 课程（官方售后培训讲义幻灯片 + 分步实验 How-To，讲义约占 55%、实验约占 45%）
- **版本来源**: `F:\AIwork\ZCode\books\entpxte403en\source_fulltext.txt`（465 页，约 432KB）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To + 命令行输出验证；无习题册，以实验内嵌提问充当验收）

### 一句话主旨
把 OmniPCX Enterprise（OXE）做成一张"会讲 SIP 的电话系统"：从 SIP 协议机理与 OXE 六组件架构出发，学会开通 SEPLOS/SIP Device 两类用户与 ALE 全系 SIP 终端（8008、ALE-2/3/30/x00 话机 + ALES 软终端），掌握 OXE 自带 SIP 设备管理（DM）与证书体系，再经 OTSBC 接通 SIP 运营商、用反代/SBC 或 VPN 把话机与软终端延伸到远程办公，全程用 sipregister/trkstat/compvisu/oxetrace 等工具闭环验证。

### 骨架 (主要论点及其关系)

1. **培训实验环境**（RLAB 全虚拟化与混合模式两套 POD 拓扑：OXE CSA 192.168.1.1/1.3、OMS CSA .13、SBC .105、ITServer(NTP+LDAP) .252、内/外 DNS、远程办公虚机；账号口令表）
2. **SIP 运营商模拟器**（ITSP1 直连与 ITSP2 经 SBC 两条腿；公网/国内/移动/国际/紧急号码规则含 POD 号；进出呼叫号码变换）
3. **POD 准备**（虚机启动清单、OXE 预配置核对、IPDSP 开通与 TFTP 指向、外部 SIP 网关 POD 参数与 DID 翻译，打通外呼）
4. **SIP 协议机理与 OXE 实现**（RFC 3261、消息与响应码、实体角色、注册/呼叫时序；OXE 六组件架构 + 空间冗余与内部域名解析；OXE 域名定制实验）
5. **SIP 用户两形态**（SEPLOS=SIP Extension 内部话机级 vs SIP Device 远端子网设备级；软件锁 177/345/430 与容量上限；SIP Device 开通全流程实验）
6. **ALE SIP 终端家族与设备管理**（8008/ALE-2/3/30/x00/ALES 功能矩阵；ALES 认证三模式与一号多机；监督/多终端/寻线组/RCC；OXE DM vs 8770、DM profile、配置文件与二进制机制、mTLS 下载认证、OpenSSL 安全级；证书定制 + ALE-2/3 + ALE-x00 双分区 + ALES PC/Android 四个开通实验）
7. **编解码协商与维护跟踪**（协商决策链与优先级；compvisu 验证；motortrace/traced、oxetrace、mtracer、sipdump 四工具实验）
8. **外线与 SBC**（外部 SIP 网关进出呼叫判定；OTSBC 原理；OXE 侧 SBC 接入实验——防火墙/中继组/外部网关/ARS/DID/NPD/回拨翻译；OTSBC 部署实验——向导+编解码+消息操纵+注册凭据排障）
9. **远程办公**（ALES 经 SBC/反代 vs VPN；话机 SBC/RP/EDS 的 LAN↔WAN 与零touch 两用例；原生加密与远程工人 N4 语义；OTSBC 内嵌反代配置实验 + ALES Remote Worker 实验收尾）

**论点之间的关系**: 1-3 是地基（没有环境与外线，后面全部跑不通），4 是协议底座，5-6 是终端侧主线（先定形态 → 认终端 → 开通 → 用 DM 管），7 是贯穿运维的工具层，8-9 是两个并列的出口能力域（对运营商、对远程用户），9 章收尾即培训评估。全书主线可压缩为"内核(SIP 化) → 终端 → 运维 → 出口(外线+远程)"。

### 作者要解决的核心问题
让售后/渠道工程师独立完成 OXE 站点的 SIP 化交付与运维：把 ALE 话机与软终端批量入网（含 NOE 转 SIP）、管好证书与设备管理、接通 SIP 运营商（直连或经 SBC）、把终端延伸到远程办公，并能用命令行工具定位信令、编解码与资源问题。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| SIP | Session Initiation Protocol：IETF RFC 3261 应用层信令协议，负责建立/维持/修改/终止多媒体会话；媒体协商靠 SDP，传输靠 RTP | 它只管"信令"不管"媒体搬运"——书中反复强调 SIP 只协商不承载（p45-48） |
| SEPLOS (SIP Extension) | SIP End Point Level of Services：OXE 把这类 SIP 终端当"内部话机"看待，支持前缀/后缀、多线、寻线组等话务台级业务 | 不是"一种协议"而是"一种接入等级"；与 SIP Device 的差别是服务等级而非品牌 |
| SIP Device | 被电话应用视为远端子网一部分的 SIP 终端（会议话机、门禁、视频设备等），须经本地 SIP 网关+私有 SIP 中继组+子网才能建 | 它"没有"前缀/后缀激活 PCX 业务的能力，也不能被 CTI 监督——服务缩水是设计而非缺陷 |
| DM / DM profile | Device Management：给 SIP 终端下发配置文件与二进制的模块；profile 是适配终端子型的参数模板（默认 0，最多 100 个） | DM 不只发配置还发"二进制"；ALE-x 话机本地/远程要两个 profile，ALES/8008 一个通吃 |
| CTL | 话机侧的证书信任列表文件，OXE DM 下发，含 RP/SBC 的 CA 证书等；目录 /usr3/mao/DM/VHE8082 | 不是"电话许可证"，是安全信任链的载体——SIP 化后话机靠它认服务器 |
| ALES | ALE Softphone：Windows/Android/iOS 软终端，SIP+ from Purple；OXE DM 独占管理（8770 不行） | 它没有预置二进制、没有 auto-discovery：login 必须管理员先建好 |
| ALES-DUID | ALES 在每条 SIP 请求里携带的唯一设备标识（RFC4122）；OXE 用它实现"一个分机号同一时刻只绑一台同型设备" | 不是"设备序列号同步"，是登录互斥机制：同类设备抢占、跨型并存、通话中禁抢 |
| OTSBC (SBC) | AudioCodes Mediant 平台的 ALE 会话边界控制器：NAT 穿越编解码转换号码/消息改写媒体加密；内嵌反向代理（≤500 远程用户） | 书中 SBC ≠ 安全网关一个功能点，而是"运营商接入 + 远程办公"两场景的公共底座 |
| EDS | Easy Deployment Server：ALE 云端零touch 部署服务器（AWS 巴黎），出厂话机先联系它换 SIP 模式并取 RP 地址与根证书 | 它只管"第一次牵手"（发 DM URL + CA 证书），日常配置仍归 OXE DM |
| ARS | 自动路由选择：出局呼叫按前缀→判别器→路由表→基于时间的路由清单选出中继组；SIP 中继组必须配 ARS | 不是"拨号计划"本身，而是"选路引擎"；逻辑判别器到实际判别器的映射挂在 entity 上 |
| NPD / DID 翻译 | Numbering Plan Description 定义主/被叫号码计划与默认号码；DID 翻译把外线号段映射回内线（如 33920x31000→31000，范围 1000） | 进来靠 DID 翻译找分机，出去靠 NPD 拼国际格式——两方向都要管，书中分别配置 |
| 空间冗余 | 两套通信服务器互备：每台有物理 IP 与角色 IP，客户端用节点名(FQDN)接入，由内部域名解析器+DNS 委托保证"只有 Main 应答" | 冗余的关键不在心跳而在 DNS——域名解析错了备份机永远接不上 |
| Quarantine（隔离） | SIP 代理的防攻击机制：3 秒内发 >50 条消息的地址自动隔离 30 分钟，报文直接丢弃 | 不是防火墙封禁——是 sipmotor 进程级的动态名单，可用 Trusted IP 白名单豁免 |
| ITSP1/ITSP2 | 培训专用 SIP 运营商模拟器：ITSP1 直连（gateway1.itsp1.com），ITSP2 经 SBC（gateway.itsp2.com）；账号 pbxP/podP + alcatel | 号码规则里嵌 POD 号（PN），是纯教学口径；生产行为（安全/编解码/号码格式）与真实运营商差异大 |

### 核心命题 (用自己的话)

1. OXE 的 SIP 体系是六组件协作：本地 SIP 网关（呼叫处理与 SIP 世界的接口）、SIP 字典（分机号↔URL）、代理（消息路由）、注册服务器（收注册）、位置服务器（URL→IP）、外部 SIP 网关（外部 SIP 系统声明）；呼叫控制始终在 Call Handling。
2. SIP 用户两形态决定服务等级：SEPLOS（SIP Extension）= 内部话机级（前缀/后缀、camp-on、寻线组、多线、酒店）；SIP Device = 远端子网设备级（无前缀/后缀、无 CTI、无呼叫中心），开通前提是子网+中继组+本地网关。软件锁 177（SIP 用户总数）/345（仅 SIP 扩展）/430（ALE-S 软终端数）控制规模，硬上限 SIP 15000/用户 15000/设备 20000。
3. SIP 终端入网四步：DHCP（拿 DM 地址）→ HTTPS 拉 DM 配置文件（按 MAC 或 login 命名）→ 拉二进制 → SIP 注册；OXE 自 N1 起自带 SIP DM（此前只有 OmniVista 8770），但只管 ALE 终端（8008/ALE-x/ALES），选型开关是系统参数 "Device Management in 8770"。
4. 证书是 SIP 化的地基：OXE 必须把默认域名 oxedomain.com 改成正式注册域名防证书错误；内部 PKI 生成根 CA + CS 证书（SAN 含 FQDN/通配/物理与角色 IP）并产出 CTL；R101.0 起 OpenSSL 安全级 2 拒收 RSA<2048 位或 SHA-1 签名旧话机证书，必要时刻意降到 1 或 0（改后必须重启）。
5. ALES 认证三模式：外部 LDAP（swinst 配置 uid/bind DN，登录须匹配 LDAP uid）、OXE 本地（首连强制改密，密码强化 14 位/2 字符含 1 大写/2 数字/1 特殊/禁 4 连/前 5 不重复；密码存独立文件不入 MAO 库，双机同步并随库备份）、OpenID Connect 规划中；外部与本地互斥，切换要先关再开。
6. 一号多机互斥靠 ALES-DUID：OXE 在首个 REGISTER 记下 分机号↔DUID，此后非 REGISTER 消息带不同 DUID 即 403 Forbidden（Warning 399 Multiple Logins）；用户可确认抢占（force），但呼叫进行中即使 force 也被拒；跨设备类型（PC 与手机）登录互不影响。
7. ALE-x00 双分区让 NOE↔SIP 切换参数化：Phone COS "Force Download NOE/SIP"=YES 时对侧二进制后台预载（首次下载可达 30 分钟），切换即快切；=NO 则切换现场下载、耗时明显。R200 前出厂只有 NOE 分区。切换仅限本地用户、仅限 OXE DM 管、且有六类禁止场景（manager/assistant 键、desk sharing、ubiquity、自动话务员、user profile、ACD）。
8. 远程办公只有两条路：SBC/反向代理（推荐；≤500 远程用户可省事用 OTSBC 内嵌 RP，更多用 NGINX PLUS）与 VPN（ALE-2/3 内嵌 OpenVPN 客户端是唯一内嵌 VPN 的机型；ALE 不提供 VPN 客户端）。话机侧另有 EDS 零touch：出厂 NOE 起步 → 联系 EDS 切 SIP 并取 RP FQDN + 根证书 → 经 RP 拉 DM 文件 → 经 SBC 注册；硬限制：无 HTTP 代理、无 802.1x、无 VLAN、暂无 Wi-Fi。
9. 编解码逐级协商：系统参数（A/μ 法线与 G722/OPUS 支持域三档）→ IP 域带宽（域内建议高带宽、跨域建议低带宽）→ DM profile → 终端能力 → 直连链路/外部网关编解码开关（OPUS/G722 打开必须连带 G711）；高带宽优先级 OPUS SWB > OPUS WB > G722 > G711 > OPUS NB > G729，用户 SIP profile 五席中 G729 与一份 G711 必到。OXE-MS 是 OPUS/G722 媒体服务（转码/会议/音导）的必要资源。
10. SEPLOS 的省资源设计是行为可预期的：18x 不带 SDP → 放音本地化（拨号音/回铃音/忙音不占压缩资源）；Alert-Info URN（free/busy）告知主叫侧；业务激活走前缀/后缀，需收 DTMF 时用 183 开媒体通道（DTMF 三法：RFC4733/INFO/带内，DM profile 定）。
11. 经 SBC 接运营商，OXE 侧七件事：内部防火墙加 SBC 信任主机 → 核对法线与 G722/OPUS 支持域 → 建 SIP 中继组（ISDN all countries + T2 SIP）→ 建外部 SIP 网关（指向 SBC、注册交给 SBC）→ ARS（前缀 0、去 1 位加 33、10 位判别器、entity 上关联逻辑↔实际判别器）→ DID 翻译与 NPD（双向）→ 回拨翻译（A33→去 3 位加 00）；维护用 sipextgw/trkstat。
12. 排障四件套：状态类 sipregister/sipdict/sipgateway/trkstat（注册/字典/网关/中继），编解码 compvisu，信令 motortrace+traced（级别 0-b 可调），深度采集 oxetrace（问题导向菜单+自动打包 zip）与 sipdump（17 项菜单：网关资源/呼叫转储/强制释放/跟踪过滤）；OXE 侧流程重启用 dhs3_init -R SIPMOTOR（推荐）。

### 论证链
全书以"概念讲义（架构图+参数表+机制图） → How-To 实验（精确菜单路径/CLI 命令） → 命令输出/抓包验证"三层推进：每个实验都能用 sipregister、trkstat、compvisu、nginx access.log、syslog 等客观输出收口（如 ALES 开通后 sipregister 必须看到 contact 行）；SIP 信令机理部分直接展示 INVITE/180/200 OK/BYE 全文报文，让读者"看报文学协议"；外线与远程办公两域用"先故意失败再修"的排障叙事（OTSBC 章：编解码不通→消息域不对→注册缺 Contact User）强化因果链。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 R101.1 MD4 / Edition 12：截图混合了 R100.0（p81/p332 报文 User-Agent）与 R101.0/R101.1（p54/p314）多版本踪迹，swinst 菜单与 WBM 界面随版本漂移。
- OpenID Connect 认证只写 "planned in the future"（p163）；EDS/Wireshark 截图为特定时点状态。
- OTSBC 章节按 AudioCodes 向导版本固定，模板升级提示"Update from Remote Server"说明其时效性更短。

### 作者的立场盲点
- 实验口径明文口令遍布全书（Superuser2580*、alcatel、123456、2580、0000、letacla1、Admin/Admin）；生产的 CA 选择、证书轮换、防火墙纵深、SBC 自身高可用容量没有展开。
- 外线章自己警告"每个运营商参数不同、要查 TC2005 与运营商文档"，但全书只有一个模拟运营商——真实 ITSP 的 REGISTER 行为、P-Asserted-Identity 策略、号码格式、SIPS 强制等差异全部缺位。
- 无性能与容量规划：SIP 用户上限有清单（p68），但话务模型、带宽估算、SBC/媒体资源 sizing 缺位；OTSBC 只提"默认 3 通道够实验用"。
- OXE 侧 SBC 接入只演示"标准型网关+无注册"的简化路径（注册凭据全交给 SBC），OXE 直接注册运营商的分支仅以字段注释带过。

### 未被证明的假设
- 假设读者已修 Starter 课程（防火墙信任主机、NOE 开通等四处明说"见 STARTER 训练"）。
- 假设 DNS/NTP/LDAP 基础设施现成（实验里是 ITServer 192.168.1.252 一台机器包办）；生产中这三个都是独立工程。
- 假设单节点部署为主：空间冗余只有原理图与附录，dupli/degraded 模式（sipdump 输出里出现）无实验。

### 最强反对意见
"这本教材教的是把 OXE 的 SIP 侧点亮，不是 SIP 组网设计"——号码变换只有模拟器口径、无真实运营商对接案例、无安全加固基线、无容量规划、OTSBC 是 AudioCodes 速成。因此每个能力的 Boundary 必须标注"实验口径"，生产依据显式指向：TC2005 与运营商参数文档（外线）、TC2957（远程办公 Quick steps deployment guide）、OXE Features List（功能矩阵）、EDS user manual（零touch）、Server deployment Guide for Remote workers（VPN 网关兼容清单）。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] RLAB/生产 POD 环境准备与预配置核对（虚机清单、账号表、IPDSP/TFTP、外线参数）
- [x] SIP 运营商模拟器运用与号码变换（实验/联调用）
- [x] OXE 域名定制与空间冗余接入规划（netadmin 19、内部域名解析、DNS 委托）
- [x] SIP 用户形态选型（SEPLOS vs SIP Device）与软件锁/容量核算（177/345/430、15000/20000）
- [x] SIP Device 基础设施开通（私网/私有 SIP 中继组/本地网关/代理/注册服务器/字典/信任与隔离）
- [x] ALE SIP 终端家族选型（功能矩阵对照：8008/ALE-2/3/30/x00/ALES）
- [x] ALES 认证方案（外部 LDAP/本地、密码策略、外部↔本地切换）
- [x] ALE SIP 特性配置（可编程键/呼叫路由/监督代接/多终端/寻线组/RCC）
- [x] SIP DM 选型与迁移（OXE DM vs 8770、混合拓扑、8770 退役警告）
- [x] OXE DM 证书定制（内部 PKI、SAN/CTL、OpenSSL 安全级决策）
- [x] ALE-2/ALE-3 SIP 话机开通（DHCP 类/TFTP URL/MAC 或 auto-discovery）
- [x] ALE-x00 双分区管理与 NOE↔SIP 切换（Force Download、Run Mode、DHCP 触发 sipconfig.txt）
- [x] ALES 软终端开通（PC/Android；代理防隔离参数、Keep Alive、轮询阈值、视频）
- [x] 编解码方案核查（系统/域/DM/终端/链路/网关逐级对照 + compvisu 验证）
- [x] SIP 跟踪采集与分析（motortrace/traced/oxetrace/mtracer/sipdump 工作流）
- [x] 经 SBC 的 SIP 运营商接入 OXE 侧配置（防火墙/TG/ExtGW/ARS/DID/NPD/回拨）
- [x] OTSBC 初始化与向导部署（含编解码放行、消息操纵、注册凭据排障）
- [x] 远程办公方案决策（SBC/RP vs VPN；EDS 零touch 限制核查；原生加密 N4 语义）
- [x] OTSBC 内嵌反向代理配置（TLS context/RP/SBC 对象/消息操纵/IP 路由）
- [x] ALES Remote Worker 配置与验证（DM profile SBC 参数、sipregister 核对）

### 不适合 skill 化的内容
- RLAB/混合 POD 的教室专用细节（p3-20、p36-37 虚机启动清单：教学基础设施，仅作 Boundary 背景）
- SIP 协议报文逐字段教学（p48/p54/p314 的 INVITE 全文：属协议基础课，非 OXE 交付动作）
- 培训评估/证书下载流程（p459-465：课堂行政事务）

### 预估 skill 数量
**约 10-12 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；入口软预算 8 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 准备实验/交付环境：启动虚机、核对实例账号表、开通 IPDSP 并指定 TFTP | p3-20, p36-40 | 可用的 POD 环境 + 在服终端 | 一切实验与现场交付的前置 | Starter 课程的防火墙/NOE 开通基础 |
| task-02 | 掌握 SIP 运营商模拟器（ITSP1 直连/ITSP2 经 SBC）的号码规则与账号 | p21-34 | 可拨进拨出的外线模拟口径 | 全书外线实验的公共依赖 | 真实运营商差异（TC2005 口径） |
| task-03 | 完成 POD 预配置收尾：外部 SIP 网关 POD 参数（pbxN）+ DID 翻译 + 外呼验证 | p35-42 | 外线打通报错单清零 | 后续 SBC/编解码实验的地基 | 无 |
| task-04 | 掌握 SIP 协议机理：消息/响应码/实体角色/注册与呼叫时序 | p43-54 | 能读懂 SIP 报文的排障能力 | 全书信令层通用语言 | 无 |
| task-05 | 定制 OXE 域名并规划空间冗余接入（节点名/内部域名解析/DNS 委托） | p55-63 | 合法 FQDN + 冗余可达性 | 证书与冗余的共同地基 | 客户 DNS 服务器的委托配置权 |
| task-06 | 选型 SEPLOS vs SIP Device 并核算软件锁/容量（177/345/430、15000/20000） | p64-82 | 终端接入形态决策结论 | 形态选错 = 服务等级全错 | 无 |
| task-07 | 开通 SIP Device 用户（私网/中继组/本地网关/代理/注册服务器/建户/验证） | p84-94 | 31060 类设备可注册可通话 | 会议话机/门禁/视频设备的标准路径 | 无 |
| task-08 | 选型 ALE SIP 终端家族（8008/ALE-2/3/30/x00/ALES 功能矩阵对照） | p95-106 | 按场景的终端选型清单 | 售前报价与承诺的依据 | OXE Features List 最新版核对 |
| task-09 | 设计 ALES 认证（外部 LDAP/本地、密码策略、模式切换）与一号多机策略 | p106-117 | 认证方案 + 账号密码基线 | 安全与运维习惯的分水岭 | 客户 LDAP/AD 基础设施 |
| task-10 | 配置 ALE SIP 特性：可编程键/呼叫路由/监督代接/多终端/寻线组/RCC | p118-143 | 用户业务开通与容量口径 | 用户体验与许可承诺的直接来源 | CTI/CCD 等进阶集成在书外 |
| task-11 | 选型并规划 SIP DM（OXE DM vs 8770、混合拓扑、DM profile 体系） | p144-167 | DM 架构决策 + profile 规划 | 终端批量管理的中枢 | 8770 存量迁移细节 |
| task-12 | 定制 OXE DM 证书（内部 PKI、SAN/CTL、OpenSSL 安全级决策） | p159-171 | 可信的证书链 + CTL 文件 | 安全地基，错了全站终端下线 | 外部 CA 流程在书外 |
| task-13 | 开通 ALE-2/ALE-3 SIP 话机（DM 激活/DM profile/建户/DHCP 类/auto-discovery） | p172-186 | ALE-2/3 入网注册成功 | 基础话机批量部署标准路径 | 无 |
| task-14 | 管理 ALE-x00 双分区并执行 NOE↔SIP 切换（Force Download/Run Mode/DHCP 触发） | p187-216 | NOE 话机平滑转 SIP | 存量站点 SIP 化的主力动作 | 切换窗口与回退预案 |
| task-15 | 开通 ALES 软终端（PC/Android）：LDAP/代理参数/DM profile/安装/维护/视频 | p217-270 | 软终端注册通话 + 特性验证 | 移动办公与客服场景主力 | 视频需非虚拟化桌面（Guacamole 限制） |
| task-16 | 掌握编解码协商链并用 compvisu 验证各场景编解码 | p271-286 | 编解码问题定位能力 | 单向语音/音质投诉的根因层 | 无 |
| task-17 | 采集与分析 SIP 跟踪（motortrace/traced、oxetrace、mtracer、sipdump） | p287-327 | 信令级排障交付物（trace 文件+结论） | 升级 ALE 支持工单的标配证据 | Wireshark 报文分析深度在书外 |
| task-18 | 理解外部网关进出呼叫判定并完成 OXE 侧 SBC 运营商接入全配置 | p328-363 | 可用的 SIP 中继外线 | 站点出扩市场的标准路径 | 真实运营商参数（TC2005） |
| task-19 | 部署并调通 OTSBC（向导+编解码放行+消息操纵+注册凭据排障） | p364-383 | SBC 与 ITSP2 双向通话 | 运营商接入的生产形态 | SBC 高可用/容量在书外 |
| task-20 | 规划并落地远程办公（方案决策 + OTSBC 反代配置 + ALES Remote Worker 验证） | p384-458 | 远程用户经 SBC/RP 注册通话 | 混合办公刚需，交付溢价最高 | EDS 零touch 的账号开通（书外）；NGINX PLUS（>500 用户） |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-07 + task-13/14/15 终端开通族（日常交付量最大）
2. task-18/19 SBC 运营商接入（外线是站点生命线）
3. task-20 远程办公（溢价最高、参数最密）
4. task-12 证书定制（安全地基，错了全站瘫）
5. task-17 SIP 跟踪排障（升级工单的硬技能）
6. task-11 SIP DM 选型（架构错误代价高）
7. task-16 编解码链（音质投诉根因）
8. task-06 形态选型 + task-09 认证设计
9. task-10 特性配置 + task-08 终端选型
10. task-01/02/03/04/05（地基与一次性任务）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 9 个一级部分（环境 3 + 协议 1 + 终端侧 2 + 运维 1 + 出口 2；培训收尾未计入）
- [x] 术语按实际内容列出（14 个）
- [x] 已检查作者局限/假设（版本混截图、实验明文口令、无真实运营商、无容量规划、Starter 前置）
- [x] 原书关键任务 20 项，全部有来源页码、交付物与重要性依据
- [x] 全流程授权连续执行（任务描述自带质量纪律，2026-09-23）

**用户确认时间**: 2026-09-23（任务描述授权）
