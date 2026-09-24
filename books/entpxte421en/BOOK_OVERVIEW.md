# OmniPCX Enterprise 加密解决方案 (ENTPXTE421EN Ed05) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OmniPCX Enterprise — Native Encryption (Participant's Guide)
- **作者**: ALE Training Services（Communication Suite for MLE 课程线）
- **出版/发布时间**: Edition 05，OXE R101.2 时代（实验记录时间戳横跨 2024-2026，EEGW 固件 ost 12.02、OMS 固件 oms_16.06）
- **内容类型**: 课程（官方售后培训讲义 + 分步实验 How-To：讲义约占 35%、实验约占 60%、课程收尾约 5%）
- **版本来源**: `F:\AIwork\ZCode\books\entpxte421en\source_fulltext.txt`（410 页，===== PAGE N ===== 标记）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：密码学/PKI 概念讲义幻灯片 + 虚拟实验平台搭建说明 + 19 个 How-To 实验章，每章都是"菜单路径 + 截图 + 行为验证"）

### 一句话主旨
把 OXE 的信令与媒体加密变成交付工程师可独立完成的"原生能力"落地：从密码学/证书基础与 PKI 策略（内嵌 CA 或外部 CA、证书格式、SAN 策略、TOFU 或手工 CTL）出发，经证书全生命周期、系统参数与 lanpbx.cfg 配置，覆盖 DTLS 端点、SIP TLS 扩展与中继、PCS/冗余接管、EEGW+NSP 大容量拓扑、ABC-F 网络与 mTLS 双向认证的部署、验证与排障。

### 骨架 (主要论点及其关系)

1. **密码学与证书基础**（对称/非对称、保密/完整/认证、证书内容与 PEM/DER/P7B/P12 格式、CSR/CRL、PKI 三种生成模式、SCEP/EST/ACME 自动注册、CTL 信任链、端到端服务器认证）
2. **实验环境**（RLAB 全虚拟化 POD：stand-alone 拓扑与 ABC-F 双节点拓扑两套 IP/账号表、ITSP2 SIP 模拟器、Pod 初始配置：NTP/根证书/板卡/用户/公网接入）
3. **方案定位与范围**（FSNE 纯软件零硬件、加密由 Call Server 强制执行、组件三级兼容矩阵、按用户"部分加密"）
4. **机制与组件**（EGW/EEGW、SIPmotor、SIP Translator NSP、IPSec Manager、内嵌 CA、CTL/TOFU、服务器/双向认证、SCEP/EST/ACME、HTTPS 安全下载）
5. **拓扑矩阵**（DTLS 端点、SIP TLS 端点、OXE 冗余与 PCS、Native SIP TLS trunk、Rainbow WebRTC GW、4645 VM、ABC-F 网络、DR-Link/录音、VAA、Dispatch Console）
6. **管理与许可**（WBM/OmniVista 8770/mgr + netadmin 命令行管理面、lanpbx.cfg 签名文件、软件许可 #424/#359、1500/15000 会话容量公式）
7. **DTLS 主线实验**（PKCS#7 证书闭环：CSR→签发→导入→核验→复制 twin；系统参数；lanpbx.cfg；IPDSP 验证；维护工具与事件；Wireshark 抓包）
8. **SIP TLS 实验**（SIP 扩展走 sipmotor、SIP trunk 的 OTSBC+OXE 两侧配置、安全停用回退）
9. **大容量实验**（EEGW/NSP 声明与防火墙、S.O.T. 生成加载 EEGW VM、证书下载、DNS 解析、公网 trunk 切换 NSP）
10. **网络化与强化实验**（ABC-F 内部 PKI 双节点、直连链路加密、XCA 外部 CA 签发端点证书、mTLS 激活与版本限制处置）

**论点之间的关系**: 1 是全书的钥匙（后续所有实验都围绕证书与信任链转）；2 是实验底座（两套拓扑的 IP/账号表贯穿全书）；3-6 是概念层，按"定位→机制→拓扑→管理"递进；7-10 是四条递进的实验线——先单机 DTLS 打通基础闭环（7），再横向扩展到 SIP TLS 与中继（8），再纵向扩容到 EEGW/NSP（9），最后网络化并强化到双向认证（10）。Wireshark 抓包与命令行输出是贯穿的验证手法。

### 作者要解决的核心问题
让交付/维护工程师在不依赖安全专家的前提下完成 OXE 加密解决方案的全生命周期交付：选定 PKI 策略并拿到证书、按拓扑正确配置系统参数与 lanpbx.cfg、把加密逐用户/逐中继/逐链路推开、用命令行工具与抓包证明加密确实生效，并能处理证书到期、换板卡、迁移拓扑、大容量扩容与版本升级带来的证书兼容问题。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| Native Encryption (FSNE) | "Full Software Native Encryption"：OXE 内原生支持信令（DTLS/TLS 1.2/IPSec）与媒体（SRTP）加密，纯软件、零硬件 footprint，靠数据库配置+软件许可激活 | 与旧方案 IP Premium Security 是两条路线（不互通）；定位从大客户的可选件变成全体客户的原生基线 |
| EGW (Encryption Gateway) | 处理 DTLS 信令加密的软件组件，充当端点的 DTLS 服务器，内嵌于 CS/PCS（每 CS 一个） | 名字像硬件网关，实际是软件模块；只承载 DTLS 信令，TFTP 等其它流不经它 |
| EEGW (External EGW) | 外部加密网关：强制虚拟机（OST 软件包，Rocky Linux），>1500 会话必配，每 CS 一台，内含 SIP Translator | 是规模分界（1500/15000）后的必需形态，不是"可选增强"；CS 与其 EEGW 必须同宿主同虚拟交换机 |
| SIP Translator (NSP) | Nginx SIP Proxy，与 EEGW 同 VM（OST 包），SIP TCP/TLS 连接的入口点；FQDN 形如 nsp.oxe.company.com | 不是协议翻译器（名字有误导），是 TLS 卸载代理；SIP UDP 端点仍直连 CS 不经它 |
| CTL (Certificates Trust List) | 受信 CA 证书链单文件（PEM 拼接，最多 5 级层级），存于端点信任库，用于验证 CS 身份；可经 lanpbx.cfg 自动推送 | 是"CA 证书链文件"这个具体物，不是一个抽象机制；OXE/端点/EEGW 两侧各有自己的 CTL |
| TOFU | "Trust On First Use"：出厂空信任库的端点首次连接不验证服务器证书，之后靠存储的 CTL 全量认证 | 是安全性折衷的默认分发方式；客户不接受时必须逐台手工预置 CTL 或走 SCEP/EST |
| mTLS (Mutual Authentication) | OXE 在 DTLS/TLS 握手时反向验证端点证书，身份比对证书 CN 与端点宣告的 MAC 地址；全局或按网关启用 | 激活后所有话机/软话机（含明文模式的）都必须有证书——第一连接总是加密模式 |
| SRTP | 媒体加密协议：对称密钥由 CS（NOE/IPMG）或 SIP 端点生成，每方向一把，经 DTLS/TLS 加密信令下发 | 密钥分发不靠独立协议，搭信令加密的便车；录音场景每保持/转接一次换新钥 |
| lanpbx.cfg | OXE IP 配置文件：NE 开启后注入 DTLS 参数（服务器地址/端口 32643/FQDN/CTL/签名证书与数字签名）后下发 | 在 NE 语境里它是签名过的信任载体（CTL+证书+签名都在文件里），远不止"下载地址配置" |
| Partial encryption | 按用户选项逐台启用加密：DTLS/TLS 能力端点可加密可明文，混合新旧话机的过渡手段 | 不是半加密协议，是许可驱动（#424）的灰度开关；DSS/DSU、ProACD 组必须同质配置 |
| netadmin | OXE 命令行管理工具（netadmin -m 菜单）：CA/证书/CTL/防火墙/域名/EGW 声明/内部 DNS 全在这 | 实验章的"导航坐标"（如 11.9.1.2=生成 CSR、20.2=声明 EEGW）；证书管理的瑞士军刀 |
| X.509 v3 (RFC5280) | ALE 采用的证书标准；SAN 是身份验证主字段（DNS/IP），CN 承载 FQDN（N5 起可无 IP SAN） | 与常识一致；书中强调的是演进方向——IP SAN 让位 FQDN，且部分老话机不支持无 IP 证书 |
| PKCS#7 / PKCS#12 | P7：证书+链、无私钥（私钥不出端点），书中推荐；P12：含私钥+口令，端点证书批量签发用 | 书中立场鲜明：P7 最简最安全（CSR 在实体上自动生成），P12 私钥要搬家、手工填 SAN 易错 |
| SCEP/EST/ACME | 三个证书自动注册协议：SCEP 面向话机（HTTP+共享密钥，老旧）；EST（RFC7030）面向 IPMG/IP-xBS；ACME（RFC8555）用于 WBM 证书，仅限本地 CA | ACME 不是万能自动续期——OXE 不公开可达，Let's Encrypt 等 HTTP-01 公网 CA 用不了 |
| OMS | 承载虚拟 GD4 板卡的软件机架/VM（omsconfig 工具管理，实验中即 ENTP_OMS VM） | 与 IT 业"运营管理系统"无关；是 OXE 虚拟化里板卡的宿主 |
| OTSBC (OT-SBC) | ALE 会话边界控制器：SIP trunk 的 TLS/SRTP 对端（WebAdmin 管理），OXE 侧和 SBC 侧两侧都要配 | 不属于 OXE，是 OXE 与运营商之间的安全边界设备/VM |
| OST (OXE Signaling Translator) | EEGW VM 的软件包名（Rocky Linux 上，ostconfig 配置；机器类型 EEGW/OST64） | OST/EEGW/NSP 三个词指同一台 VM 的三个侧面：包名/角色/代理进程 |
| PCS | Passive Communication Server：分支机构救援服务器；CS 失联后端点以加密模式切换到 PCS | PCS 证书与 CS 同 CA 但不同证书；端点必须至少连过一次 CS 才能被救援；共用主 CS 的 lanpbx.cfg |

### 核心命题 (用自己的话)

1. 加密由 Call Server 强制执行：NE 开启后 IPMG 与 PCS 一律加密，端点按用户选项逐台加密，trunk/ABC-F 链路两端能力不匹配就直接退出服务——系统层面不允许"半吊子"状态静默存在。
2. 信任锚是 CTL：端点用 CTL 验证 CS 身份；获取路径两条——lanpbx.cfg 自动推送（首连走 TOFU）或手工预置（客户拒绝 TOFU 时），EEGW 反向还要把证书从 CS 下载过去。
3. 私钥尽量不出端点：PKCS#7 路线（CSR 在实体上由 netadmin 生成→CA 签发→只回证书）是推荐主线；PKCS#12 路线私钥在 CA 生成后搬家、CSR 手工填 CN/SAN 易错，只用于端点证书场景。
4. 一张证书管全系统：全系统一个 CA（内嵌 OpenSSL CA 或外部 CA），端点实体证书 CN=MAC（板卡/话机/IPDSP），CS/PCS 证书 CN=FQDN；SAN 按拓扑自动装配（EEGW/NSP/角色 IP）。
5. lanpbx.cfg 是 DTLS 的信任载体：DTLS 服务器地址+端口（默认 32643）+FQDN+CTL+签名文件全在文件里；CS duplication 时必须从 main 生成（自动产出 lanpbxtwin.cfg 并同步）。
6. 容量分界 1500：≤1500 并发 DTLS/TLS 会话用内嵌 EGW；超出必须上 EEGW（VM、每 CS 一台、上限 15000）；许可公式=受保护端点数 + 3×(GD4/GD-XL/GD3/INTIP3B/OXE-MS) + 3×外部 SIP 网关 + 3×节点数。
7. SIP TLS 双轨：SIP 扩展走 sipmotor（TLS 1.2，端口 5061），SIP trunk 可配 TLS client/server 与双向认证（互认证端口默认 6261）；Native SIP TLS 可独立于 NE，但媒体加密必须两者叠加。
8. 证书操作是固定五步闭环：CSR 生成（netadmin 11.9.1.2）→外部 CA 签发→导入（11.9.1.4）→核验（11.9.1.8）→复制 twin（10.2）+ dhs3_init -R NGINX；PKCS#7/PEM/DER 格式通吃。
9. 冗余即加密：CS 主备间 DTLS 会话强制 mTLS，两 CS 共用密钥对与证书；主侧证书任何变更必须同步 standby；PCS 与 CS 同 CA 异证书；twin 操作是高频遗忘点。
10. ABC-F 网络安全是端到端链：IPSec（协商 500/管理 2579）保护节点间信令，SRTP 密钥经加密链路分发；任何一环不加密（transit 链路、对端节点、任一端点）媒体就明文；仅 hybrid link 有 transit 节点，direct link 无。
11. mTLS 有版本陷阱：R101.0(N3) 起 OpenSSL 3.0 提高安全等级，1024 位出厂证书（部分 NOE 话机、8378 IP-xBS、8328 SIP-DECT）无法双向认证——要么换 ≥2048 位外部证书，要么 R101.1(N4) 起降 SSL level（风险管理员自担）。
12. 运维三件套闭环：事件 5992（CA 证书剩余有效期，P1=0 时证书失效、所有 FSNE 端点重启）倒逼续期；证书+私钥必须导出备份（或随 Linux Data 备份）；验证靠 ippstat/twin/cryptview/csipsets/sipregister/sipextgw + Wireshark 抓包听音。

### 论证链
教材以"概念讲义 → 实验闭环 → 行为验证"推进：讲义章先立"为什么"（市场与合规需要）与"是什么"（组件/拓扑/许可），实验章严格按"证书 → 参数 → 配置文件 → 重启 → 验证"闭环推进，每章末尾用行为证据闭合（话机加密图标、命令输出表格、Wireshark 播放流是噪音还是语音）；对比表（三 PKI 模式、三注册协议、两种证书容器）承担选型论证。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 实验记录时间戳横跨 2024-2026（证书有效期样例 2024-2034、ost 12.02、Rocky Linux 9.7），菜单与交互随版本演进快；N3/N4/N5 的能力分界（OpenSSL 3.0、SSL level 可调、无 IP SAN）密集出现在 R101.x 内，跨版本操作必须对照最新 release notes。
- "By the end of 2025, any newly produced board will embed a default ALE certificate" 是时效性承诺，读书时需核对当前出厂策略是否兑现。
- ITSP2 章内部命名混乱（章题 ITSP2，网关账号却用 itsp1.fr 域，p43-46 混用 ITSP1/ITSP2 标签），照抄会困惑。

### 作者的立场盲点
- 全书默认"培训师即 CA 管理员"：生产中客户自建 CA 的流程治理（CA 私钥保管、CRL/OCSP 基础设施、证书策略与审批）只有 CSR/CRL 概念页，没有企业 PKI 运营内容——签发环节在书外。
- 所有实验口令明文遍布正文（Superuser2580*、alcatel、letacla1、Admin/Admin、*tx8000#）；生产安全基线（口令治理、SSH 收口、防火墙最小化）只有零散 Warning（如 OMS 开 SSH 要告知客户并事后关闭）。
- TOFU 作为默认 CTL 分发方式，只给一句"客户拒绝则手工"，没有首次连接被中间人利用的风险分析；安全教科书式的权衡缺席。
- Wireshark 验证只教了话机 PC 口镜像一种位置，trunk 侧与 EEGW 侧的抓包点选择、SIP TLS 解密（需要密钥日志）都没覆盖——"验证加密生效"的最后一公里靠图标和命令输出。
- EEGW 容量公式只给计数式，没给单 VM 的 CPU/内存规格与压测口径（Sizing 只说"最大用户数"）。

### 未被证明的假设
- 假设时间同步（NTP）现成且准确——证书有效期校验强依赖时间，书中只给一句 "recommended"。
- 假设外部 CA 签发即时（实验中 trainer 秒签）；生产中 CA 流程的排队、策略审批、CA 不可用时的业务连续性被忽略。
- 假设读者有 OXE/Linux 命令行基础（mtcl/root/swinst 账户切换、vi/openssl 常识），零基础学员按图索骥会卡在终端层。
- 假设 otclient/内部防火墙白名单由预配置镜像带好（实验 OXE 已预配置），生产从裸机起步时的防火墙项没有完整清单。

### 最强反对意见
"这本手册教的是把 OXE 的加密开关按菜单打开，而不是设计企业语音加密体系"——PKI 治理、密钥轮换与吊销策略、多站点 CA 层级设计、SIEM/审计集成、抗量子算法演进都不在书中；连"吊销"也只出现在 CRL 概念页，OXE 侧没有任何吊销操作实验。因此每条能力的 Boundary 必须标注"培训实验口径"，生产化需对照 OXE 安装/维护文档、客户安全策略与真实 CA 的运营规程。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] OXE 证书 PKI 策略决策（内嵌 CA vs 外部 CA、PKCS#7/PKCS#12/PEM/DER 格式选择、SAN 有无 IP 策略、TOFU vs 手工 CTL）
- [x] CSR 生成与证书导入五步闭环（netadmin 11.9.1.x 菜单路径、twin 同步、NGINX 重启）
- [x] 加密解决方案系统参数与用户级启用（Native Encryption 参数块、SRTP authentication、用户选项、加密图标显示）
- [x] lanpbx.cfg 生成与维护（lanpbxbuild/-auto、DTLS 参数、FQDN、签名）
- [x] DTLS 加密验证与排障（ippstat/twin/cryptview/事件 5991-5995/证书备份）
- [x] Wireshark 媒体加密验证（话机 COS、端口镜像、RTP 解码、Stream Analysis）
- [x] SIP TLS 扩展启用（SIP 参数三件套、SRTP working mode、sipregister/csipsets/motortrace）
- [x] SIP trunk TLS/SRTP 全流程（OTSBC TLS context/证书/Proxy Set/Media Security + OXE 外部网关/本地网关端口/CTL）
- [x] 加密解决方案安全停用（四步回退）
- [x] PCS 加密接管部署（omsconfig 声明、PCS CSR/导入、pcscopy、断网演练）
- [x] EEGW/NSP 大容量部署（netadmin 20/19 声明、内部防火墙、lanpbx DTLS 指向 EEGW、ostconfig、证书下载、SIP translator/DNS）
- [x] S.O.T. 生成与加载 EEGW VM（Greenfield 工程、媒体上传、OVF 生成、ESXi 部署）
- [x] ABC-F 网络加密（内部 PKI 双节点、链路 Encryption 参数、SRTP 一致性、hybvisu 验证）
- [x] XCA 外部 CA 操作（根 CA/端点实体/CSR 导入签发/导出格式与命名约定）
- [x] 端点证书部署（OMS/GD 板卡 SFTP 导入、IPDSP 文件法/Windows 证书库法、话机手工/证书服务器/SCEP）
- [x] mTLS 启用与版本限制处置（Endpoint CTL 导入、mTLS 参数、SSL security level 降级路径）

### 不适合 skill 化的内容
- RLAB 实验平台与 ITSP2 SIP 模拟器细节（p27-57、p283-290 的教学专用基础设施，仅作 Boundary 背景）
- 密码学通识教程页（p3-26，作为 skill 背景知识引用即可，不构成独立能力）
- 课程评估/证书下载流程（p404-410）
- XCA 软件安装/数据库创建等纯软件安装步骤（p335-337、p381-385，通用 PC 操作）

### 预估 skill 数量
**约 9-11 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；入口软预算 8 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 掌握密码学与证书基础（对称/非对称、证书格式、PKI 模式、CTL） | p3-26 | 选型对话的概念底座 | 一切后续实验的钥匙；格式/模式对比表是决策依据 | 企业 PKI 运营治理在书外 |
| task-02 | 搭建 Pod 实验环境（NTP、根 CA 证书入信任库、板卡/用户、DID/NPD/SBC/NAT 公网接入） | p48-57 | 可打电话、可达公网的实验 POD | 全部实验的前置条件 | 生产化需替换全部实验口径值 |
| task-03 | 使用 ITSP2 SIP 模拟器验证出局/入局呼叫 | p42-47 | 公网呼叫打通 | 后续 SIP TLS trunk 实验的呼叫源 | 模拟器行为≠生产运营商 |
| task-04 | 为 OXE 生成 CSR 并经外部 CA 签发证书（PKCS#7），导入并核验，复制 twin | p113-118 | 证书就位的 CS | 加密解决方案的第一关口 | 真实 CA 的签发流程在书外 |
| task-05 | 配置加密解决方案系统参数与用户级加密（含加密图标显示） | p119-120, p140-142 | 系统级+用户级加密开启 | 功能开关本体 | 无 |
| task-06 | 生成与维护 lanpbx.cfg（DTLS 参数、FQDN、签名） | p121-125, p230-233, p256-257 | 签名后下发的 DTLS 载体 | DTLS 生效的必经文件；duplication 规则是易错点 | 无 |
| task-07 | 验证 DTLS 加密并掌握维护闭环（IPDSP 接受证书、ippstat/twin/cryptview、事件、证书备份） | p126-133 | 加密通话+可排障+有备份 | 交付验收与运维本体 | SIEM/集中监控在书外 |
| task-08 | 用 Wireshark 抓包证明媒体已加密 | p134-138 | 抓包证据 | 客户验收的硬证据 | trunk/EEGW 侧抓包位置在书外 |
| task-09 | 启用 SIP TLS（sipmotor）加密 SIP 扩展并验证 | p139-145 | TLS 注册+加密通话 | SIP 侧基础能力 | CCD agent 场景受限（书中自注） |
| task-10 | 部署 PCS 加密接管（声明、证书、pcscopy、断网演练） | p146-156 | 分支失联可加密救援 | 多站点架构刚需 | 无 |
| task-11 | 为 SIP trunk 配置 SIP TLS+SRTP（OTSBC 侧与 OXE 侧两侧） | p157-193 | 运营商方向的加密中继 | PSTN 替代场景的主诉求 | 真实运营商 TLS 对接参数在书外 |
| task-12 | 安全停用加密解决方案（参数、用户、lanpbx、重启、验证明文） | p194-198 | 干净回退 | 变更管理必备 | 无 |
| task-13 | 部署 EEGW+SIP Translator（声明、防火墙、lanpbx 指向 EEGW、VM 配置、证书下载、维护命令） | p199-243 | >1500 会话的加密承载 | 大站点必经；CS 会随 EEGW 重启是最重警告 | EEGW VM 规格与压测口径在书外 |
| task-14 | 用 S.O.T. 生成并加载 EEGW 虚拟机 | p272-282 | 可用的 EEGW VM | EEGW 落地的工厂流程 | 浏览器仅 Chrome/Firefox（书中自注） |
| task-15 | 改造网络实验室拓扑（Node1/Node2、OMS 旧证书清除、直连链路验证） | p283-290 | ABC-F 双节点实验环境 | 网络实验的前置；OMS 信任库清除是易踩坑 | 无 |
| task-16 | 启用 ABC-F 网络加密（Node1 内部 PKI、Node2 CSR 网络签发、链路 Encryption、SRTP 一致性、网络通话验证） | p291-332 | 节点间加密的 ABC-F 网络 | 多节点组网的核心能力 | 与 IP Premium Security 互通不可能（书中自注） |
| task-17 | 用 XCA 为端点签发证书（根 CA、OMS/IPDSP 实体、CSR 导入签发、PKCS#12 全流程） | p333-353, p380-403 | 端点证书与 CA 文件 | mTLS 与端点证书的前置 | XCA 仅是教学替身，客户 CA 不同构 |
| task-18 | 启用 mTLS 双向认证（端点证书部署、Endpoint CTL 导入、mTLS 参数、版本限制处置与 SSL level） | p354-379 | 双向认证的 DTLS/TLS | 安全强化终点；OpenSSL 3.0 兼容问题集中地 | 客户设备台账核查（1024 位设备清单）在书外 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-04/05/06/07 DTLS 基础闭环（证书→参数→lanpbx→验证，一通百通）
2. task-09/11 SIP TLS 扩展与中继（客户最常要的"话音加密"落点）
3. task-13/14 EEGW/NSP 扩容（规模分界后的必经，CS 连带重启风险最高）
4. task-18 mTLS 与版本限制（升级后最常见的翻车点）
5. task-16 ABC-F 网络加密（多节点组网）
6. task-10 PCS 接管（分支救援）
7. task-17 XCA 端点证书（mTLS 的供给端）
8. task-08 Wireshark 验证（验收证据）
9. task-12 安全停用（变更管理）
10. task-01/02/03/15（基础与实验环境，一次性支撑类）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 10 个一级部分（概念 1 + 环境 1 + 方案/机制/拓扑/管理 4 + 实验四条线 4，课程收尾未计入）
- [x] 术语按实际内容列出（18 个）
- [x] 已检查作者局限/假设（培训师即 CA、明文口令、TOFU 风险缺席、抓包位置单一、时间同步假设）
- [x] 原书关键任务 18 项，全部有来源页码、交付物与重要性依据
- [x] 用户授权的流水线连续执行（提取阶段任务书，2026-09-23）

**用户确认时间**: 2026-09-23（流水线任务书授权）
