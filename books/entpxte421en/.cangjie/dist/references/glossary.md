# GLOSSARY — OmniPCX Enterprise 加密解决方案 术语表

> 阶段 3 产出（源：candidates/glossary.md，52 条，六大域；此处为门户精选 30 条）。
> 口径：定义只采信本书正文；NOE/OMS/IPDSP/ALES/VAA/DC/IP-xBS/GD4/FlexLM 等缩写书中未给全称，如实标注；"Diffie-Helmman"（p7）、"11520-8-N-1"（p367）、"ENCRYTPION"（p247）为原文笔误。

# OmniPCX Enterprise 加密解决方案 (ENTPXTE421EN Ed05) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（410 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Native Encryption (FSNE) | 加密解决方案 | OXE 内原生支持信令（DTLS/TLS 1.2/IPSec）与媒体（SRTP）加密的纯软件能力，零硬件 footprint；激活=数据库配置+许可 #424/#359 | p61-66, p109 |
| EGW (Encryption Gateway) | 加密网关 | 处理 DTLS 信令加密的软件组件，端点的 DTLS 服务器（内嵌 CS/PCS）；TFTP 等其它流不经它 | p76-77, p87 |
| EEGW (External EGW) | 外部加密网关 | >1500 会话的必需形态：强制 VM（OST 包，Rocky Linux）、每 CS 一台、内含 SIP Translator、上限 15000 | p77, p199-203 |
| SIP Translator (NSP) | SIP 翻译器 | 与 EEGW 同 VM 的 Nginx SIP 代理：一切 SIP TCP/TLS 连接的入口点；仅外部 EGW 场景强制声明 | p76, p202, p247 |
| OST (OXE Signaling Translator) | EEGW 软件包名 | EEGW VM 的软件包（机器类型 EEGW/OST64，ostconfig 配置）；OST/EEGW/NSP 指同一台 VM 的三个侧面 | p201-202, p209 |
| CTL (Certificates Trust List) | 受信证书链 | 受信 CA 证书链单文件（PEM 拼接，最多 5 级层级），存于信任库用于验证对端；lanpbx 字段 DTLS_CERT_TRUST | p24-25, p79-80, p124 |
| TOFU | 首次信任 | 出厂/空信任库端点第一次连接不验证服务器证书，之后按存储 CTL 全量认证；客户拒绝则手工预置或 SCEP/EST | p80, p74, p108 |
| mTLS (Mutual Authentication) | 双向认证 | OXE 在握手时反向验证端点证书（身份比对证书 CN 与宣告 MAC）；激活后所有话机含明文用户都须有证书 | p82-83, p165, p359 |
| Partial encryption | 部分加密 | 按用户选项逐台启用加密的灰度机制；DSS/DSU 与 ProACD/agent 上下文必须同质配置 | p65-66 |
| lanpbx.cfg | OXE IP 配置文件 | NE 开启后注入 DTLS 参数（DTLS_SRV/端口 32643/FQDN/CTL/签名）并签名下发——端点侧的信任载体 | p121-125, p124 |
| Factory certificate | 工厂证书 | 仅 GD4/GA4/GD-XL/GA-XL 板卡、话机与 IP-xBS 出厂携带；板卡侧自 R101.1 MD4 起可用 | p78, p83, p371 |
| End entity / CN=MAC 约定 | 端点实体命名 | 板卡/话机/软话机实体证书 CN=设备 MAC；CS/PCS 证书 CN=OXE FQDN；节点证书 CN 恒为节点 FQDN | p322, p344, p399 |

## 二、账户与角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| mtcl | OXE 维护账户 | 日常操作与验证命令的登录账户（netadmin 切 root 前的登录、lanpbxbuild、cryptview 等） | p34, p113, p129-131 |
| root | Linux 超级用户 | 证书导入导出、内部防火墙、SSL level 等敏感操作要求 su - root | p107, p113, p191 |
| swinst | 软件安装账户 | Linux Data 备份走 swinst（证书自动随备份）；EEGW 下载证书经 ssh-copy-id 用其口令 | p107, p133, p237 |
| CA Administrator (trainer) | CA 管理员 | 实验中由 trainer 充当外部 CA 管理员签发 CSR；生产对应客户 PKI 运营方 | p115, p381 |

## 三、许可域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| License #424 | 加密解决方案用户许可 | 定义系统内允许的 DTLS/TLS 会话总数（Actis 系统级计数器；实验值 75） | p109, p129 |
| License #359 | SIP 加密中继许可 | 定义并发 SIP TLS 通信数上限（实验值 30） | p109, p129 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniPCX Enterprise (OXE) | 企业通信服务器 | 本书主角：CS 承载全部加密组件；PCS 为分支救援服务器（同 CA 异证书、须先连过 CS） | p62-64, p91-92 |
| OMS | 软件机架/VM | 承载虚拟 GD4 板卡（omsconfig 管理）；mTLS 场景导入 GW.pfx；换拓扑须清信任库 | p52, p147, p288-289 |
| IPMG 家族 | IP 媒体网关家族 | GD4/GA4/GD-XL/GA-XL（新代）/GD3/GA3/INTIP3（老代）/OXE-MS；AES-256 与工厂证书能力有差异 | p63-64, p72, p74 |
| IPDSP | PC 软话机 | NOE 侧软话机应用；只工作在 SRTP 认证模式；证书两法（文件/Windows 库） | p119, p127-128, p360-362 |
| ALES | ALE 软话机 | SIP TLS 扩展加密主力终端（SEPLOS 模式，盾牌图标） | p63, p88, p142 |
| OTSBC (OT-SBC) | 会话边界控制器 | SIP trunk 的 TLS/SRTP 对端（WebAdmin 管理）；与 OXE 两侧端口成对 | p90, p173-184 |
| netadmin | OXE 命令行管理工具 | 证书全生命周期主操作面（11.9.1/11.9.2/11.9.3/11.1.3/11.6.3/17/19/20/10） | p101, p104 |
| lanpbxbuild | lanpbx 生成工具 | -auto 建文件（重置除 IP_CPU/IP_DOWNLOAD 外配置）；j/k=DTLS 地址、6=重签；duplication 在 main 跑 | p121-123 |
| omsconfig / mgconfig / ostconfig | 三类网元配置工具 | OMS VM/GD 板卡（V24 串口）/EEGW VM 的配置与证书管理（都有 Certificate management 子菜单） | p147, p235-238, p356-369 |
| XCA | 开源证书管理工具 | 外部 CA 的教学替身（hohnstaedt.de/xca）；客户已有 CA 就用客户的 | p335, p381 |
| S.O.T. | ALE 部署工具 | EEGW VM 生成与加载（Greenfield 工程→.ova→ESXi）；仅 Chrome/Firefox | p272-282 |
| VAA / Dispatch Console | 语音应用服务器/调度台 | 经 Native SIP TLS（internal ABC-F 型）加密；VAA 加密后端口 120→60，DC 保持 120 | p98-99 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| DTLS 1.2 | 数据报传输层安全 | NOE 侧信令加密协议（RFC 6347/5246），EGW 承载，默认端口 32643 | p67, p87 |
| TLS 1.2 (SIP TLS) | 传输层安全 | SIP 扩展与中继的信令加密（RFC 5246），sipmotor 或 NSP 承载，端口 5061/6261 | p67, p160 |
| SRTP | 安全实时传输协议 | 媒体加密：AES-CM-128/256-HMAC-SHA1-80 二选一不混用；密钥每方向一把、经加密信令下发 | p69-72 |
| IPSec | 网络层安全协议 | ABC-F 节点间信令加密（IPSec Manager/OpenSwan；端口协商 500/TCP 2579），证书认证 | p67, p293, p301 |
| NOE | ALE 私有 IP 话音协议族 | IP NOE 端点经 EGW 走 NOE over DTLS，密钥由 CS 生成 | p69, p87 |
| SCEP / EST / ACME | 三个证书自动注册协议 | SCEP=话机（HTTP+共享密钥）；EST（RFC7030）=IPMG/IP-xBS 自动续期；ACME（RFC8555）=仅 WBM 且须本地 CA | p23, p84 |
| PKCS 容器家族 | 证书/密钥容器格式 | PEM/DER/PKCS#7（证书+链无私钥，推荐线载体）/PKCS#12（含私钥+口令）/PKCS#10（CSR） | p14-16, p103 |
| X.509 v3 / DN / CN / SAN | 证书标准与身份字段 | ALE 采用 X.509 v3（RFC5280）；SAN 是身份验证主字段（EEGW 拓扑按五字段顺序装配） | p13, p85, p206 |
| CRL / CDP / OCSP | 证书吊销机制 | 概念层讲义：CRL=失效证书清单、CDP=下载位置扩展、OCSP=在线核查；OXE 侧无吊销操作实验 | p12, p17 |

## 六、平台与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| RLAB / POD | 培训远程实验室/实验单元 | 全虚拟化按 POD 划分同构单元；每 POD 两套拓扑（stand-alone 与 ABC-F 网络） | p27-35 |
| ITSP2 / MicroSIP | SIP 运营商模拟器 | 教学专用（gateway.itsp2.com+public.itsp1.com 两腿）；章内 ITSP1/2 命名混用为原书现象 | p35, p42-46 |
| ALE Knowledge Hub | ALE 培训平台 | 课后在线评估与培训证书下载（enterprise-education.csod.com） | p404-410 |
