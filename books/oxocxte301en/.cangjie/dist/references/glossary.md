# GLOSSARY — OXO Connect Advanced 术语表

> 阶段 3 产出（源：candidates/glossary.md，62 条，六类：concept 27 / role 5 / subscription 5 / product 11 / protocol 9 / resource 5）。
> 口径：定义只采信本书正文；DDI、RSL、NMC、CTI、ADL、RPN、PLI 等缩写书中未给全称的如实标注；p191/p345/p502 法文残句与 p321 排版噪声见 needs-review nr-03。

# OXO Connect Advanced (OXOCXTE301EN Ed18) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（601 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OMC | OXO 的 Windows 管理工具 | Expert 模式 LAN/WAN 连接并服务器认证；对象树覆盖配置全域；内置 Webdiag 入口与 MLAA 图形树编辑器 | p23-32 及全书 |
| ARS (Automatic Route Selection) | 自动选路 | 按被叫号码与可选时段自动选中继组，饱和/故障溢出；三表协作兼做号码变换（加/吸收/替换/透明） | p194-205 |
| Internal ARS | 内部 ARS | 用 ARS 机制把一个入站 DDI 按日组+时段路由到不同内部目的地；虚拟 Provider+Local 索引技法 | p225-231 |
| Entity | 多实体 | 系统内最多 4 个逻辑公司：独立 MoH、可选实体间禁呼；话务员组全实体公共不受限 | p242-248 |
| Pseudo multi-company | 伪多公司 | 链路类别配对+矩阵直线+ARS 透明线实现两公司共享系统、各走各的外线、账单分离 | p249-251 |
| Multiset / Twinset | 多话机组/双机组 | 1 主+最多 2 副共享主站目录号与服务级别；主有线+副 DECT 常称 Twinset；与 Rainbow 侧同名概念不同物 | p184-189 |
| Hot Desking (HDP/HDU) | 共享话机 | HDU 在任意 HDP 登录（683/682）取回个人环境；200+200 容量；Webdiag 与 OMC 双通道监督 | p173-177 |
| Nomadic mode | 游牧模式 | 游牧话机（多为手机）替代本地话机；VMU 远程定制选项 6 激活；CLI 按主叫身份规则发送；SIP 话机不支持 | p465-468 |
| Remote substitution | 远程替代 | 拨替代 DDI+接入码+分机+密码以该分机外呼；内部号加 # 前缀（#100-#199）经内部 ARS 回环 | p469-480 |
| Account code | 账号码 | 外呼费用记到客户/项目账号：表上限 250、码 ≤16 位；内部替代场景被当权限钥匙用 | p93-95 |
| OHL / AHL | 酒店链路 | 经 Office Link Driver（V24/IP）对接 AHL 兼容酒店应用；OHL 无 SW license | p65 |
| PMS | 酒店管理系统 | 管预订/入住退房/账单/客史；经 OHL 与 OXO 同步（兼容性查 DSPP/生态 PDF） | p59, p65 |
| Automated Attendant (AA) | 自动画务员 | 两棵树（白天/夜间）每树两级 100 节点、4 语言；定制需 license；支持免费拨号与 AATypTrf 转接 | p405-421 |
| MLAA | 多树话务员 | 基于 ACD 引擎按 DID/CLI 路由最多 5 棵树（3 级）；语音总量硬上限 12000 秒；端口与 ACD 共享 16 | p427-442 |
| SCR | 智能路由 | 按 CLI/DDI/DTMF 客户码/开闭时间路由来话；10000 规则；X 通配符；错误走备份目的地 | p450-458 |
| Personal Assistant | 个人助理 | 每订阅户迷你 AA：三目的地（内部/外部/移动）+转话务员；noteworthy PerAssAlwd 默认禁用 | p385-387 |
| Stations groups supervision | 站群监督 | 一台监督话机监控最多 8 号：pop-up+音调+键闪烁三路通知；系统上限 50 键 | p111-115 |
| Cloud Connect (CCI) | 云连接基础设施 | OXO 主动发起永久 HTTPS+按需 VPN（免改防火墙）；注册自动免 license；Fleet 数据一天一刷新 | p262-289 |
| Fleet Dashboard | 舰队门户 | OXE 与 OXO 通用：安装基础/SA 合同/Inventory（每日刷新）/批量 SW 更新（advanced 权限） | p267-280 |
| OXO Connectivity | 单系统云门户 | VPN 配置、Watchdog/OMC 复位、许可清单、DSP 统计、默认密码检出、单台更新 | p265-275 |
| Noteworthy address | 内存读写地址 | 服务器全局参数（labels/flags）四类内存区；写错致系统恶化、cold reset 回默认、清单 TC1398 | p574-578 |
| DTLS | 话机信令加密 | ALE VoIP 话机信令通道加密（TLS 1.2）：语音仍明文；300 连接、免 license、仅 OCE | p359-364 |
| SIP Registrar / B2BUA | 注册服务器/背靠背代理 | OXO 是自己 SIP 客户端的 Registrar 并作 B2BUA 中转呼叫；注册失败入历史表 | p140-141 |
| RTP Proxy / Direct RTP | 媒体三处理 | DSP 通道（压缩）→RTP proxy（同编解码仅路由）→Direct RTP（端点直连最优）；TLS 下不可用 | p144-148 |
| DECT Cluster | DECT 集群 | 空口同步基站组：切换仅集群内；站点最多 20、每站最多 8 集群；成员由 OXO 强加 | p506, p517 |
| Site Survey Kit (SSK) | 站点勘测工具箱 | 2 台勘测专用 xBS（固件与生产不同）+天线+话机；-72 dBm 划语音质量区；手册 8AL90874USAA | p529-534 |
| SUOTA | 空中升级 | DECT 话机经 8378/8379 升级：并发 50、下载 4-8 小时且话务优先、swap 须充电座 | p526 |

## 二、角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| installer | 安装员会话 | OMC/Webdiag 主管理角色：全功能调试、证书、抓包、DECT；首连密码 pbxk1064 仅首连 | p28, p560, p572 |
| operator | 操作员会话 | Webdiag/MMC：上传实体 MoH、Hot Desking 监督注销、解锁用户账户；亦是语音录制入口 | p570 |
| manufacturer | 制造商会话 | Webdiag 第三会话（ALE 技术支持专用） | p560, p568 |
| Supervisor | 监督者 | 站群监督监督方：仅 DeskPhones；3 方会议/应用内/ACD 登录时不能应答通知 | p112, p114 |
| HDU / HDP | 共享用户/共享话机位 | Hot Desking 两角色：一 HDP 同时只容一 HDU，抢占自动注销前者 | p174-176 |

## 三、许可/订阅域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| HDU 计费包 | Hot Desking 许可 | 前 2 个 HDU 免费、之后按 50 一包；容量上限 200 HDP/200 HDU | p174 |
| IP-DECT 用户 license | 无线用户许可 | IP-DECT 按用户上 license；DECT 用户总量上限 200 | p495 |
| MLAA 树 license | 话务员树许可 | 树数分 1 或 5 两档；树数与端口（共享 16）受其约束 | p428 |
| SCR + Supervisor Console license | 智能路由许可 | SCR 功能 license + 1 个监督台 license（日志从监督台出） | p458 |
| 免 license 功能清单 | 免许可口径 | Call Accounting、自动密码检查、订阅户密码管理、DTLS、TLS/SRTP、Cloud Connect、OHL 免 license；OCE-FE 只需硬件 | p73/316/321/360/367/287 |

## 四、产品域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OXO Connect Evolution (OCE) | 演进型平台 | DTLS、SIP TLS/SRTP 原生、4K 证书、公网 Server 证书等高级能力的主承载平台 | p13, p346-367 |
| OXO Connect Office (OCO) | 非演进平台 | 自身无原生 TLS/SRTP，经 OCE-FE SIP 代理获得加密中继能力 | p375 |
| OCE Front-End (OCE FE) | OCE 前端 | 原为外部 WebRTC 网关，新增 SIP TLS/SRTP 代理角色；GW 与 PROXY 各 20 通话；license 免费只需硬件 | p375-378 |
| PowerCPU EE / IP Box | CPU 板形态 | LoLa 模式进入方式不同（Dip switch vs 电源键）；V24 config 口 115200 8N1 | p569, p585 |
| 8088 Smart DeskPhone | 安卓高端话机 | 7 寸触摸屏 Android 6.0.1；仅 v2+ 受 OXO 支持；Private Store 默认禁装应用 | p104-108 |
| 8378 IP-xBS / 8379 IBS / 8328 | DECT 基站三系 | IP 轨 xBS（80 台/11 并发）、TDM 轨 IBS（60 台/6 并发）、SIP-DECT 单基站小分支 | p484-486, p494-495 |
| 8158s / 8168s | VoWLAN 话机 | 仅 NOE 模式上 OXO；WinPDM+Desktop Programmer 部署；≤R4.x 显示为 8118/8128 | p549-552 |
| ALE-2 / ALE-3 | 入门 SIP 话机 | 黑白屏 3 键 2 账号 / 彩屏 4 键 4 账号；双千兆 PoE；G.711/G.729/G.722/OPUS/ILBC | p152 |
| LoLa | 系统加载工具 | 完整装载软件+应用包+license；Installation/Mono 迁移/Install-Restore 三流程；话机配置须 OMC 先存 | p582-591 |
| Webdiag | Web 调试工具 | 三会话+七块信息树：抓包/状态/Hot Desking/解锁/Cloud Connect/Rainbow status/证书管理主接口 | p559-570 |
| ITSP1 | SIP 运营商模拟器 | RLAB 公共区模拟运营商（gateway1/public.itsp1.com）；账号 pbxP/alcatel；教学专用 | p16-22 |

## 五、协议域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| SIP | 会话发起协议 | REGISTER/Digest 注册（端口 5059）、B2BUA、SIP Option 私网监督、RFC 3325/4028、SIPS 在 OCE-FE 不支持 | p140-154, p378 |
| TLS / SRTP | 中继加密组合 | SIP-TLS（5061）+SRTP；服务器证书或双向认证；四套 AES-CTR 套件；OCE 原生或 OCE-FE 代理 | p365-378 |
| DECT / GAP | 数字无线标准 | ETSI EN 300 175-1~-8 + GAP EN 300 444；FDMA/TDMA/TDD 10 载波×24 时隙；ADPCM G726 | p499-501 |
| LDAPS / StartTLS | LDAP 加密通道 | LDAPS 636 与 StartTLS 389（推荐默认）；证书校验 Mandatory 默认 | p332 |
| 端口族 | 端口地图 | 443（管理 HTTPS）、50443（互联网专用）、5059（SIP 话机）、5061（SIP-TLS）、7780（DTLS）、10443/11443（话机/HAN）；加固关闭 21/1721/5061/8729/8888/17069/23400 | p300, p337, p346-356 |
| XMPP | 更新指令协议 | Cloud Connect 软件更新链路中 Update Agent 与 Update Service 间通信；二进制走 HTTPS | p270 |
| AOC | 运营商计费脉冲 | 支持 AOC 的中继直接脉冲计费；与 Call Accounting Time based 互斥不可混配 | p73, p82-83 |
| PKCS#10 / CSR | 证书签名请求 | 外部 PKI 签发路径的申请格式（WebDIAG 生成下载、外部 CA 签、导回安装） | p350-355 |
| V24 | 串行接口通道 | 计费打印/外部计量可走 V24（TC002_US）；CPU 调试口 115200 8N1 | p77, p297, p569 |

## 六、资源/数值域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| 实验网络基线 | 实验口径总表 | PC .10 / OXO .246 / 网关 .254 / DNS .250 与 10.20.30.250；SIP 账号 pbxP/alcatel；安装号 210P41000、DDI 41100-41199 | p6, p12-21 |
| 出厂与实验口令表 | 口令清单 | pbxk1064（OMC 首连）、Alcatel1（教室 Webdiag）、OMCAdmin（代理）、admin/00!（xBS）、780911/615243（实验接入码）等——全部实验口径生产必改 | p12-572 多处 |
| 系统容量快查表 | 上限速查 | 酒店 300 话机/4 会话；账号码 250；监督 50 键×8 号；HD 200/200；实体 4；紧急号码 100；AA 2 树 100 节点；MLAA 5 树/12000 秒；SCR 10000；DECT 80/60/200；DTLS 300 | p64-495 多处 |
| 书外技术文档索引 | TC 清单 | TC1143（安全）、TC1398（noteworthy）、TC2249（密码审计）、TC002（V24）、TC2349（WinPDM）、8AL90874USAA（SSK）、Global Limits、Cross compatibility | p297-591 多处 |
| DECT 标识五件套 | 无线标识 | PARI（系统 ID，全系统一个）、RFPI（xBS）、PARK（话机侧）、PLI（=31）、IPUI（话机，14 位八进制）；原注法文（nr-03） | p502 |
