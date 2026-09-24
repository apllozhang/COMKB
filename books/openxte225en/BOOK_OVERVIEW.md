# OpenTouch 移动与远程办公 (OPENXTE225EN R2.6 Issue 10) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OpenTouch — 移动与远程办公 (Participant's Guide)
- **作者**: ALE Training Services（Alcatel-Lucent Enterprise，Alcatel-Lucent 商标归 Nokia、授权 ALE 使用）
- **出版/发布时间**: OpenTouch R2.6 / Issue 10（正文技术坐标：Ubuntu 16.04.3 LTS、ESXi 6.0/6.5、OTSBC 7.2、APNS 根证书有效至 2022、收尾服务页标注 H1'18，据此判定为 2017-2018 年代教材）
- **内容类型**: 课程（官方售后培训讲义 + 分步实验 How-To，讲义约占 45%、实验约占 55%）
- **版本来源**: 处理文本 `F:\AIwork\ZCode\books\openxte225en\source_fulltext.txt`（287 页，带 ===== PAGE N ===== 标记）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To；每个知识域都是"讲义章 + How-To 章"成对出现）

### 一句话主旨
把 OpenTouch MLE 通信系统安全地开放到互联网：在 DMZ 上用 OTSBC 与反向代理补齐"SIP/媒体"与"Web 服务"两条通道，用 CA 证书与内外分离 DNS 打底，再把 OTC PC 与智能手机配置成远程工作者的全功能终端（PC 双模式、手机双模式、iPhone 推送来话）。

### 骨架 (主要论点及其关系)

1. **培训实验环境**（RLAB POD 虚机池：OTMS/OXE/OmniVista 8770/FlexLM/OMS/Eco-system/SIP 运营商模拟器；账号口令总表；用户编号计划与模拟器号码变换规则）
2. **远程接入基础设施讲义**（三类用户诉求 → DMZ 双边缘 Reverse Proxy + OTSBC（VPN 仅为替代）→ 组件职责、客户端×边缘用例矩阵、DNS 双侧解析、证书原则、参考文档族 TC2639 等）
3. **证书体系**（三种证书来源（CA/自签/通用+CTL）、PKCS7 与 PKCS12 两种封装、通配符 vs 每服务器专用、SAN、预载证书的安全警告）
4. **OpenTouch 服务器侧远程访问设置**（RP 申报四 URL、OTSBC 申报两端口、DAS 规则清单、ACS 会议服务专 FQDN/IP 与证书重签）
5. **OTSBC 部署**（OVF → CLI 初始化 → 许可 → 证书 → "Alcatel-Lucent Remote Users" 向导模板 → SIP 接口证书选择；thick wizard 与手工补配附录）
6. **反向代理部署两条路线**（OTSBC 7.2+ 内嵌 RP：许可+HTTP proxy+三份模板 ini；独立 Nginx VM：Ubuntu+Nginx+三份 conf+LDAP 认证；配套 OpenSSL 自建 CA 与 VMware OVF 两个附录 How-To）
7. **客户端远程接入**（两步法：接入配置（公共 URL+凭证）+ 路由档案（从哪拨/路由到哪）；PC/智能终端各自的入口）
8. **OTC PC 远程工作者**（两种模式并列：multi-devices 把 SIP 分机绑为副设备；Nomadic SIP 用 Ghost Z 池+设备池顶替主话机）
9. **OTC 智能手机**（连接模式矩阵（WiFi/3G4G/DTMF 回落）、关联一次自动建 OXE 9 类对象、R2.6 起 RE 可做单设备、Android 无 SIM 纯 VoIP、iPhone APNS 推送来话与 kamailio-wasp/wspcfg 组件、OXE 通用参数与手工补充）
10. **收尾营销页**（eDemo 远程演示、ALE 服务组合，H1'18；非技术内容）

**论点之间的关系**: 层层递进为主——1 是地基；2-3 是原理与安全前提（拓扑、DNS、证书是后面一切部署的输入）；4-6 是服务器与边缘部署链（顺序强依赖：证书先签发 → 服务器侧申报 → OTSBC → 反代）；7-9 是客户端与用户侧（PC 两种模式并列、手机一种主流程 + iPhone 专项）；第 10 部分为营销附注不计入技术骨架。附录（OpenSSL、VMware）反向支撑 5-6。

### 作者要解决的核心问题
让售后/渠道工程师独立完成 OpenTouch MLE 的"远程办公 + 移动化"交付：部署并打通 DMZ 边缘（SBC + 反代）与证书体系，在服务器侧完成申报与会议访问管理，最后把 OTC PC 与 OTC 智能手机配置成可从互联网全功能接入的终端，并能验证呼叫行为。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| OTSBC | ALE OpenTouch Session Border Controller：管理并保护 SIP 会话与 RTP/SRTP 媒体流（DoS 防护、拓扑隐藏、TLS/SRTP 加密、CAC）；场外客户端把它当作 SIP 服务器 | 不只是"会话防火墙"——它是远程话音的注册与媒体锚点，7.2 版起还能内嵌反向代理 |
| Reverse Proxy (RP) | 管理远程客户端到话音 Web 服务的 HTTPS 会话，可接 LDAP/RADIUS 认证公司用户；是第三方产品（ALE 不提供）；可由 OTSBC 兼任（此时认证部分需另配服务器） | 在本书里它是"外网客户端看到的服务器"（拓扑隐藏+SSL 卸载+URL 改写/封禁），不是以负载均衡为主 |
| Conversation user / Connection user | 自 OpenTouch 2.2 起同一 PC 客户端的两种用法：Conversation 用户 SIP 通信走 OpenTouch SIP 服务器，Connection 用户走 OXE SIP 服务器 | 不是两个 App，是同一客户端的两种注册行为——OTSBC 向导里对应 OTCV/OTCT 两组参数 |
| Multi-devices | 把一个 SIP 分机（如 OTC PC，号段 213100x）作为用户的副设备（secondary device），主话机保留 | 与 Nomadic 并列的第二条路；前提是 COS 开"Ring all Secondary if Main Out of Service" |
| Nomadic (SIP) | 老方式：把当前话机从 Deskphone 切到 Personal Computer 后主设备被"冻结"，SIP 软话机顶替；每次连接占用 1 SIP 设备 + 1 Ghost Z set，按并发建池 | "游牧"占用的是池资源，退出游牧才释放——不是无限并发的用户特性 |
| Ghost Z set | 虚拟 Z 设备（Set Type Analog + Ghost Z 特性，特性选 Nomadic 或 Remote Extension），把本打给内部话机的呼叫重定向出去 | 是"占位器"不是真话机；编号可用 B<数字> 形式避免占用真实号码段 |
| Remote Extension (RE) | 远程分机：经 DISA 公共号码把呼叫引到手机；R2.6 起可直接作为用户唯一设备（此前需永不入服的 SIP 主设备+溢出） | RE 背后是一整套机制：tandem 并联、速拨自动替代、ARS 路由、判别器——不只是一个"转手机" |
| DISA | 远程分机的公共接入口：DISA 前缀（实验 31280）+ 公共 DISA 号码（如 +3320131444）；自动替代可设 Without code | 不是普通直拨入——RE DISA 前缀必须在 DDI 翻译表里有对应，否则整条链路不通 |
| Tandem (twinset) | 主话机与远程分机之间的并联结构，要求双方都是多线设备（L1/L2），系统可自动建线 | tandem 是"同组并铃"，与呼转（forward）是两回事；R2.6 的改进恰恰是去掉为规避呼转问题的假主设备 |
| Direct Speed Dialing number | 自动替代机制用的速拨号（A<RE 号>，如 A2131001），RE 呼入时替换主叫身份；范围不能为 0 也不能满 | 不是"话机快捷键"——是 DISA 自动替代占用的系统号码资源 |
| ARS + Discriminator | 自动路由选择：每部 OTC 智能手机自动分一张 ARS 路由表（从 MAX ID 3999 起分配），Route 1=SIP 设备、Route 2=公网 TG 呼手机；判别器做逻辑→物理关联与号码格式变换 | ARS 在本书的作用是"双模式时呼手机的第二跳"，不是普通出局路由；判别器还要联动公网接入 COS 的区域授权（barring） |
| DAS rule | 会议服务器管理台（Default 域）的号码变换正则（s/^\+…），R2.0 起为游牧 PC 新增 4 条；共 10 条示例、顺序敏感、国家相关（书中为法国口径） | 只作用于会议接入侧的号码规范化，与 PBX 拨号计划是两套规则 |
| APNS | Apple Push Notification Server：R2.3.1 起 iPhone 的 OpenTouch 推送都走它；防火墙需放行 TCP 5223/2195/2196/443 | 推送是 VoIP 来话的"第二振铃路径"：后台来话要多发 SIP invite 唤醒应用，导致 UDP 强制、场外 TCP 需代理缓冲 |
| kamailio-wasp / wspcfg | iPhone "VoIP everywhere" 专用组件：SBC 与 OXE 之间的 SIP 代理 + 给 kamailio 提供配置的服务；有独立的状态/日志/日志级别命令 | 不是 OpenTouch 主体的常规模块，是为 iPhone TCP 场景补的代理缓冲层 |
| OTC 家族 | OTC PC（全功能软话机）、OTC PC One（无 VoIP/视频）、OTC Web（浏览器协作）、OTC WebRTC、OTC smartphone（Android/iPhone）、OTC Plus（iPhone+，商店名 OpenTouch Conversation Plus） | 每端 VoIP 能力与所需边缘组件不同（用例矩阵里标"加密可能/N.A./N.U."），不能按"装了 OTC 就有全部能力"承诺 |
| PKCS7 / PKCS12 | 两种证书交换封装：CSR 在本机（如 OT 服务器）生成用 PKCS7；密钥对在 CA 生成则用带 passphrase 的 PKCS12 | 封装由"私钥在哪生成"决定，不是随便挑；选错导入流程就走不通 |
| SAN (Subject Alternative Name) | 证书主题备用名：会议服务 FQDN（conf-podx）必须同时进反向代理与 OpenTouch 服务器证书的 SAN | CN 对了也没用——会议场景认 SAN，漏配直接导致会议邀请链接不可用 |
| OTMS | OpenTouch 管理服务器虚机（实验：opentouch.company.com = 151.1.1.50，SUSE Linux）；OMS 为另一管理组件（oms.company.com，账号 letacla1，实验口径） | 正文行文多用"OpenTouch server"，OTMS/OMS 是它在实验环境里的具体承载虚机 |

### 核心命题 (用自己的话)

1. 远程接入的骨架是 DMZ 双边缘：反向代理管 HTTPS/Web 服务（话音控制、目录、留言、协作），OTSBC 管 SIP 信令与 RTP/SRTP 媒体；VPN 只是"技术替代方案"，不是主推路线。
2. 证书是远程访问的硬前提：外部接入必须用 CA 签发的证书（自签有安全弱点，安装时选"通用证书+CTL、安全关闭"被官方明确反对——话费欺诈与服务盗用风险）；建议外部 PKI。
3. DNS 必须内外分离：内部 DNS 把 OpenTouch/conference FQDN 解析到私网 IP，公共 DNS 把同一批 FQDN 解析到 RP/SBC 公网 IP；conference FQDN 内部解析到会议簇 IP。
4. 服务器侧三件事：申报 RP（API/EVS:8016/ACS/DMS 四个公共 URL）→ 申报 OTSBC（5261 给 OTC 客户端、8061 给 WebRTC）→ 会议访问管理（DAS 规则国家相关且顺序敏感；ACS 会议服务专用 FQDN+IP，必须进证书 SAN，必要时跑 rehost 脚本并重签证书）。
5. OTSBC 部署高度向导化：OVF 上电 → CLI 配管理 IP（默认 Admin/Admin）→ 导许可与 CA 证书 → "Alcatel-Lucent Remote Users" 模板一键生成 IPG/Media Realm/SIP 接口 → 手工给 SIP 接口挑证书。
6. 向导覆盖不了的场景要手工补：iPhone 部署强制手工配置（查 TC2639）；OXE 的 SIP 接口建议补 TCP 5060（向导只配 UDP）；SIP 接口的 TLS context 要换成自签发的证书。
7. 反代两条路线功能同向：OTSBC 7.2+ 内嵌 RP（许可+启用 HTTP proxy+RP 专用证书+三份模板 ini）或独立 Nginx 虚机（Ubuntu+Nginx+global/remoteworker/conference 三份 conf+可选 LDAP 认证）；OT 2.2 起 Nginx 必须同时改 remoteworker.conf 与 conference.conf（OTES 退场、会议应用共享改走反代）。
8. 客户端接入两步法：第一步配公共 URL 与凭证（OTC PC 也可填 OTSBC 公网 FQDN），第二步激活路由档案（从 PC/手机/其他号码拨 → 路由到 PC/手机/…）；用手机拨打时永远用手机本机发话，"从哪拨"设置不影响。
9. OTC PC 远程办公两模式并存：multi-devices（SIP 分机绑副设备，主话机保留，需 COS+前缀 506/507 前提）与 Nomadic SIP（池化 Ghost Z+SIP 设备，主设备冻结）；池大小按并发游牧连接数规划。
10. 智能手机配置是"关联一次、自动生成"：OT 侧把 OTC Smartphone 关联到 Connection 用户后，OXE 自动建远程分机/tandem/速拨号/SIP 设备/判别器/ARS 表（对象集随 Mobile-only/WiFi-only/Dual 模式而异），管理员只需核验+补两项手工（Entity 判别器关联、公网接入 COS 区域授权）。
11. R2.6 是分水岭：远程分机可直接做用户唯一设备（免去永不入服的 SIP 主设备与溢出配置），修复了主设备离线呼转问题，并使会议回调可用；Android 可无 SIM 当纯 VoIP 话机（失去回落/私人呼叫/短信）。
12. iPhone 来话靠推送唤醒：后台 VoIP 来话需多次 SIP invite，UDP 强制；场外经 SBC 走 TCP 时由 OpenTouch 侧 kamailio-wasp 代理缓冲 invite；防火墙四端口（5223/2195/2196/443），APNS 证书一年一换（每年专门 hotfix），iPhone+ 专用 SBC 声明用 5265 端口。

### 论证链
教材以"讲义给原理（拓扑/组件职责/证书/DNS）→ How-To 给带截图字段的操作序列 → 行为验证收口"推进：验证手段包括 SIP 模拟器互拨与主叫显示核对（p26-29）、ping ACS 地址与查证书 SAN（p69-70/77）、"Test the solution"（p157 游牧切换）、关联核验页与自动对象逐项核对（p202/207-211）、nginx -t（p254）；规模、防火墙全局策略与生产化细节外链 TC2639/TC2257/TC2341 等技术通报，书中不展开。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 全书绑定 R2.6/Issue 10 时代坐标：Ubuntu 16.04（含 Python 2 only 的 LDAP 认证）、ESXi 6.0/6.5、OTSBC 7.2、Mediant wizard 7.2；今天这些组件均已换代，Nginx mainline 仓库、APNS 证书年更 hotfix 机制、Geotrust 根证书"有效至 2022"等细节都已过期。
- 智能手机章节的 3G/4G/GSM 语境、SEPLOS 假主设备的历史包袱，反映的是 2017-2018 的部署现实。

### 作者的立场盲点
- 全书默认实验拓扑：演示域名 al-mydemo.com、公网 195.128.146.10x、DMZ 11.1.1.x、明文口令（superuser/letacla1/Admin/Admin、1234）遍布正文；生产安全基线（改默认口令、SBC 加固、证书轮换流程）只有零星提示没有成章。
- 容量与规模完全缺位：CAC 只在 SBC 功能列表里出现一次，没有任何并发用户/通道/带宽的数值口径；"池大小按并发规划"没有给算例。
- 防火墙策略只给 OTSBC/RP 各自的端口片段与 APNS 四端口，整站安全策略（管理面暴露、URL 封禁清单、DNSSec 等）在书外。
- 反代认证（LDAP）在两条路线里都被实验跳过（"本实验不实现"），而它是生产必答题。

### 未被证明的假设
- 假设读者可控公网 IP 与 NAT 规则、同时掌管内部 DNS 和公共 DNS（现实中公共 DNS 常在客户 IT 或域名商手里）。
- 假设已有可用 CA（实验直接用 Eco-system 自建 Windows CA）；正式环境的证书申请流程、通配符证书的合规性未讨论。
- 假设 OmniVista 8770 是唯一管理入口、OXE 已正常运维；对无 8770 的纯 OT 环境（该书前身 OTES 场景）仅一笔带过（OTES 已"不再是方案一部分"）。

### 最强反对意见
"这本手册教的是把 OpenTouch 挂上互联网的管道工程，不是移动化方案设计"——并发容量、体验质量（QoS/CAC 阈值、Wi-Fi→GSM 溢出的实测量）、安全运营（证书生命周期、SBC 加固基线）、以及所有 iPhone 手工配置细节都外置到 TC2639/8AL90065USAG/TC2341。照书只能复现实验拓扑，不能直接交付生产；每个能力的 Boundary 必须标注"实验口径"，并显式指向 TC2639（远程工作者配置总纲）与 8AL90065USAG（OTSBC 配置指南）作为生产化依据。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] 远程接入拓扑决策（三类用户诉求 → RP+OTSBC 双边缘 vs VPN，客户端×组件矩阵）
- [x] 证书策略与自建 CA 签发（OpenSSL 全流程、Windows CA 申请、PKCS7/PKCS12、通配符 vs 专用+SAN、客户端导入）
- [x] OpenTouch 服务器侧远程访问设置（RP/OTSBC 申报、DAS 规则、ACS 会议 FQDN+rehost+证书重签）
- [x] OTSBC 部署与向导配置（OVF、CLI 初始化、许可、TLS context、Remote Users 模板、SIP 接口证书）
- [x] OTSBC 内嵌反向代理部署（HTTP proxy 许可与激活、RP 专用证书、interface+模板 ini）
- [x] Nginx 反向代理部署（Ubuntu、Nginx 安装、证书、三份 conf、LDAP 认证）
- [x] 反代路线选型（内嵌 vs 独立；认证需求决定组件）
- [x] 客户端远程接入配置（OTC PC/Web/Smartphone 接入配置与路由档案）
- [x] OTC PC multi-devices 副设备配置（COS/前缀前提、DM 声明、副设备与 OTC PC 关联）
- [x] OTC PC Nomadic SIP 配置（Ghost Z 池+SIP 设备池规划与声明、游牧许可）
- [x] OTC 智能手机 Connection 用户配置（OXE 通用参数、OT 侧 SBC/系统参数、设备档案、关联与自动对象核验、手工补充、R2.6 单设备）
- [x] iPhone+ APNS 专项（防火墙端口、SBC 5265、kamailio-wasp/wspcfg 维护）
- [x] VMware OVF 虚机部署（web client 与 vSphere 两条路）
- [x] 实验拨测与号码变换验证（模拟器国内/国际/主叫显示）

### 不适合 skill 化的内容
- RLAB 实验环境细节与账号口令表（p4-30，教学专用基础设施，仅作 Boundary 背景）
- Ubuntu/ESXi 安装的逐步截图（p221-244、p269-277 大部分为通用 IT 技能，只保留参数口径）
- 收尾营销页（p278-287：eDemo、服务组合、教育服务——非技术内容）

### 预估 skill 数量
**约 9-11 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 认知 RLAB 实验环境（POD 虚机清单、IP/DNS、账号口令、用户编号计划） | p4-30 | 实验环境对照表 | 一切实验与排障的对照基准 | 纯实验口径，生产不复用 |
| task-02 | 规划远程接入拓扑（三类用户诉求、双边缘 vs VPN、流量分类） | p31-46 | 拓扑与组件选型结论 | 全书的架构决策入口 | 容量/QoS 数值在书外 |
| task-03 | 制定证书策略并签发证书（CA/自签/通用选型、通配符 vs 专用+SAN、OpenSSL CA 全流程、客户端导入） | p47-61, p260-268 | 可用的服务器证书与 CA 根证书分发 | 远程访问的硬前提；p61 明确安全红线 | 正式 PKI 流程与合规口径在书外 |
| task-04 | 配置 OpenTouch 服务器侧远程访问（RP 申报、OTSBC 申报、DAS 规则、ACS 会议 FQDN+rehost+证书重签） | p62-77 | 服务器侧就绪的远程访问配置 | 客户端能连进来的服务器侧闭环 | DAS 规则需按目标国家改写 |
| task-05 | 部署 OTSBC（OVF、CLI 初始化、许可、证书、向导、SIP 接口证书选择） | p78-117 | 可用的会话边界控制器 | 远程话音/媒体的核心边缘 | iPhone 手工配置、容量阈值在书外 |
| task-06 | 部署 OTSBC 内嵌反向代理（许可核验、HTTP proxy 激活、RP 证书、interface+模板 ini） | p131-144 | 可用的嵌入式反代 | 免维护第三方的反代路线 | LDAP 认证需专用机器（实验跳过） |
| task-07 | 部署独立 Nginx 反向代理（Ubuntu 虚机、Nginx 安装、证书、三份 conf、LDAP 认证） | p218-259 | 可用的独立反代 | 第三方/已有 Nginx 场景的主路线 | OTES 已退场的版本前提（OT 2.2+） |
| task-08 | 部署 VMware 虚机（OVF/OVA 导入，web client 与 vSphere 两路） | p269-277 | 可运行的虚机 | task-05/07 的承载技能 | vSphere 仅 ESXi ≤6.0 |
| task-09 | 配置客户端远程接入（OTC PC/One/Web/Smartphone 接入配置与路由档案） | p145-150 | 远程可登录的客户端 | 用户侧第一步 | 无 |
| task-10 | 配置 OTC PC multi-devices 副设备（COS/前缀前提、DM 声明、副设备创建、OTC PC 关联 SBC） | p151-156 | 主话机+PC 副设备的用户 | R2.6 时代主推的 PC 远程形态 | 无 |
| task-11 | 配置 OTC PC Nomadic SIP（Ghost Z 池、SIP 设备池、游牧许可、切换测试） | p157-161 | 游牧可用的用户 | 存量/兼容场景仍常用 | 池容量按并发数规划（无算例） |
| task-12 | 配置 OTC 智能手机 Connection 用户（OXE 通用参数、OT 侧 SBC/系统参数、设备档案、关联、自动对象核验、手工补充、R2.6 单设备、App 安装） | p189-217 | 双模式/单设备的智能手机用户 | 移动化的主体交付 | 编号前缀规则与 barring 联动要吃透 |
| task-13 | 实施 iPhone+ APNS 专项（防火墙端口、SBC 5265 声明、kamailio-wasp/wspcfg 维护） | p183-188, p197, p217 | iPhone 后台可收来话 | iPhone 场景的必答题（书内明确手工强制） | 完整手工配置清单在 TC2639 |
| task-14 | 用 SIP 模拟器做拨测验证（国内/国际/主叫显示变换） | p26-29 | 呼叫行为验证结论 | 各实验的行为闭环出口 | 模拟器行为与真实运营商有差异 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-03 证书策略与签发（一切远程访问的闸门，也是 p61 安全红线所在）
2. task-05 OTSBC 部署（话音媒体核心边缘）
3. task-04 服务器侧设置（没有申报，客户端无处可连）
4. task-06/07 反代两条路线（选型 + 部署）
5. task-12 智能手机 Connection 用户（移动化主体，步数最多）
6. task-13 iPhone+ APNS 专项（书内明示手工强制，现场高频）
7. task-10/11 OTC PC 两模式
8. task-09 客户端接入两步法
9. task-02 拓扑规划 / task-08 虚机部署 / task-14 拨测验证 / task-01 实验环境（支撑类）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 9 个一级部分 + 收尾营销页说明（1 地基 + 原理与安全前提 2 + 边缘部署链 3 + 客户端域 3）
- [x] 术语按实际内容列出（18 个）
- [x] 已检查作者局限/假设（R2.6 时代坐标、实验明文口令、容量缺位、LDAP 认证实验跳过、公共 DNS 归属假设）
- [x] 原书关键任务 14 项，全部有来源页码、交付物与重要性依据
- [x] 用户已授权全流程连续执行（文档整理流水线任务书，2026-09-23）

**用户确认时间**: 2026-09-23（流水线任务书授权）
