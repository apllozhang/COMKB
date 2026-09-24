# GLOSSARY — OmniPCX Enterprise DECT Solutions 术语表

> 阶段 3 产出（源：candidates/glossary.md，56 条，六大域）。
> 口径：定义只采信本书正文；UA/RTP/SIP/NTP/TFTP/DHCP/Syslog/LLDP-MED/FWU/IPEI/VAD/CLIP 等缩写书中未给全称，如实标注；实验环境值（IP/密码/AC/PARI）一律标"实验口径"。

# OmniPCX Enterprise DECT Solutions (DECTXTE200EN Ed12) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（298 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| DECT | 数字增强无绳通信 | ETSI 发布的标准（p4 写 European Telecommunication Standard Institute，原文如此），1993 年起欧洲标准、110+ 国家采用；蜂窝技术、宏密度 10000 E/Km² | p4-6 |
| Cell | 小区 | 一个基站的无线电覆盖范围；功率恒定 250mW、大小由环境决定，可重叠提升话务密度 | p6, p13 |
| Roaming | 漫游 | 覆盖区内任意位置收发呼叫；空闲态靠定位阶段互相识别；跨 Site 仍可 roaming | p23-24, p88 |
| Handover | 切换 | 通话中在基站间透明切换；要求全部基站 DECT 帧精确同步；仅同 Site 内可用 | p25-26, p87 |
| Location phase | 定位阶段 | 手机扫描测 RSSI→选最强站→上报 IPUI+PARK→比对 PARI/PARK→锁定系统 | p23-24 |
| Location area | 位置区 | 按 RPN 区间划分的寻呼优化分区，每 PARI 最多 64 个 | p84-85 |
| Site | 站点/切换域 | 同地理位置可 handover 的 xBS 组；默认全在 Site 0；一个 PARI 可拆多 Site、一个 Site 可跨多 PARI | p86-92 |
| Internal synchronization | 内部同步 | 同 Site 同 PARI 内 xBS 空中时间对齐；同步树按 RSSI+跳数自动构建（最深 24 级）、默认零配置 | p100, p113-114 |
| External synchronization | 外部同步 | 两个同步树之间的对齐（xBS 树↔xBS 树或↔TDM 树）；Master Sync 与 External Sync RPN 手工指定、Backup 强制 | p105-109 |
| Synchronization highway | 同步高速通道 | >2 个 PARI 做外部同步时所需的附加同步配置 | p111-112, p141 |
| Mixed mode | 混合模式 | 同一台 OXE 同时跑 IBS 与 xBS：Radio base type=Mixed、多 PARI、PLI 必须适配 | p63, p144, p242-248 |
| Dual cell | 双小区（8328） | 两台 8328 主/从小区：副站自动发现主站拉配置；区内有 handover/roaming；链路建立约 5 分钟 | p272, p288-291 |
| Bi-cellular deployment | 双基站小区（xBS 语境） | 多台 8328 各自成区时区间无切换；唯独两站一区部署有 handover/roaming | p275 |
| Survey mode | 勘测模式 | 手机 *7378423*（*service*）激活的调试模式：显示 RSSI/基站列表/RFPI；耗电、干扰正常功能 | p214-216 |
| SUOTA / FWU | 空中软件升级 / FWU 协议（FWU 书中未展开） | 手机固件空中升级：语音优先、回充电座生效；手机固件须支持 FWU 协议否则 USB 手动 | p58, p179-181 |
| Multi-PARI | 多 PARI | 一台 OXE 并存多 PARI：驱动是混合硬件或超 254 台扩容；配套 PLI 适配与外部同步 | p18-20, p106, p244 |
| Connection handover | 连接切换（IP 中继切换） | IP-xBS 体系内切换：Call Server 只连初始基站，新旧基站间建 IP 中继转发媒体 | p74, p95-97 |
| Visited node | 访问节点 | 多节点网络中手机漫游到达的非安装节点；固件下载与自动重注册对其不生效 | p181, p253 |
| 安全三级 | Identity/Authentication/Encryption | 身份核对（默认）→AC 派生 UAK 挑战（四个时机）→每呼叫派生 DCK 加密；IBS 无加密 | p35-37 |

## 二、角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Sync Master | 同步主站 | 同步树的根基站：内部同步自动选举可漂移；外部同步手工指定且禁止承载任何通信 | p101, p106 |
| Backup Sync Master | 备份同步主站 | 外部同步强制冗余：须邻近主站且看得见同一外部同步源；可补承话务、主备切换后该话务即失 | p106, p109 |
| Data Sync Primary | 数据同步主站 | 每 Site/PARI 对自动选出的数据汇集站；handover 只发生在同一 Data Sync Primary 之下（dectview 的 P 标志） | p93-94, p116 |
| Primary / Secondary station | 主站/副站（8328） | 主站=先声明 Extension 的那台（数据源）；副站自动发现并拉取配置 | p288-291 |

## 三、订阅域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| SIP user license | SIP 用户许可 | 本书为本地部署教材、无订阅体系；仅 8328 场景提及每台 DECT 终端需 1 个 SIP 用户许可 | p277-278 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| 8378 DECT IP-xBS | 全 IP DECT 基站 | 本书主线：UA/UDP 信令、RTP 直达、空中互同步、PoE Class 2、每站 11 通话+11 IP 中继、8 PARI/2032 台；三硬件型号 | p55-65 |
| 8379 DECT IBS | TDM DECT 基站 | 接 UA 板卡、1/2 条 UA 链路=3/6 B 信道、全网单 PARI/256 台、无加密；三型号+ATEX 变体 | p218-225 |
| 8328 SIP-DECT | 低成本单站 DECT | 基站以 SIP 语义接入、仅 8214 手机、仅欧洲频段、每站 20 手机（G.711 10 路/G.729 4 路）、HTTPS WBM | p271-278 |
| 82xx DECT 手机家族 | 手机谱系 | 8214（仅 GAP）、8234/8244/8254/8262/8262EX（GAP+A-GAP）；遗留 8212/8232/8242 | p28-30, p181, p252 |
| Site Survey Kit（SSK） | 勘测套件 | 专用 8378 xBS 两台、8dBi 天线、充电宝、2×8242 勘测手机、拉杆三脚架 3BN67191AA 等 | p211 |
| 8379 IBS ATEX | 防爆变体基站 | 订货号 3BN77020EA，用于危险环境场景的选型项 | p222 |
| IP-xBS 天线系列 | 天线与附件 | 8.0dB 定向（圆极化）、8dBi 双极化、7dBi 全向及配套安装件（p65-69 订货号目录） | p65-69 |
| OmniPCX Enterprise（OXE） | 宿主 PBX | CSA/OMS/GD4/UA 板卡构成；IP-xBS 要求 OXE R12.2 起；实验环境 CSA 192.168.1.1/1.3（实验口径） | p1, p42, p60 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| FDMA / TDMA / TDD | 频分/时分/时分双工复用 | 10 载波分频 × 每帧 24 时隙分时 × 上下行同频时分；合计 120 个复用无线信道 | p9-12 |
| DECT frame | DECT 帧结构 | 10ms 一帧 480 bits、24 时隙；Field A 信令 6.4Kbit/s、Field B 语音 32Kbit/s；IBS 用 6+6 时隙、xBS 用 12+12 | p8-12 |
| GAP | 通用接入协议（Generic Access Profile） | 国际多厂商无绳接入标准：基础服务、可注册 5 个 GAP 系统；8214 仅支持 GAP | p28 |
| GAP+ (A-GAP) | 高级 Alcatel GAP 协议 | 多线扩展、监督键、经理/秘书键等高级功能；需 8234/8244/8254/8262/8262EX | p29-30 |
| UA protocol | UA 信令协议（书中未展开全称） | OXE 与基站间私有信令：IP-xBS 像 NOE 话机一样经 UA/UDP 单播注册；DECT 消息封装在 UA 内 | p5, p71-72 |
| SIP | SIP（书中未展开） | 8328 接入语义：基站代手机发 SIP register（contact=号码@基站 IP）；每终端 1 个 SIP 许可 | p271-278 |
| RTP 与编解码 | 媒体流（RTP 书中未展开） | RTP 在话机/中继与基站间直达；编解码 G711（A-µ law）/G729A/B（VAD）；8328 按编解码限容量 | p58-59, p73, p272 |
| LLDP-MED | 邻居发现协议（书中未展开） | IP-xBS 支持的网络拓扑自动发现特性项 | p59 |
| NTP | 网络时间协议（书中未展开） | OXE NTP 给 UTC、Call Server 给夏令时规则，经 UA 信令下发；8328 双小区 NTP 强制 | p76, p148, p272 |
| TFTP | 简单文件传输协议（书中未展开） | 基站固件自动升级下载通道：DHCP 下发 TFTP 地址，基站后台加载 | p59, p125, p129 |
| DHCP | 动态主机配置协议（书中未展开） | 基站 IP 动态配置通道；xBS 走 vendor class alcatel.ipxbs.0；8328 需放开"非 ALE 设备" | p59, p126-128, p280 |
| Syslog | 系统日志协议（书中未展开） | 基站日志集中：地址+端口 514 在 OXE 配置，级别按基站四档；建议全站落同一文件 | p153, p160-161 |

## 六、资源与标识域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| PARI | 主访问权标识 | PBX 侧系统标识：31 位（8 个十六进制位/11 个八进制位）；每类硬件一个、每节点最多 8 个 | p14-15, p82 |
| RPN | 无线部分号 | 系统分配给基站的空中标识（2 个十六进制位）：地理定位与同步识别依据；换站手动注册可保持 | p14, p16, p83 |
| RFPI | 无线固定部分标识 | 基站空中广播的标识=PARI+RPN；定位阶段回给手机供比对 | p14, p22 |
| PARK | 手持访问权密钥 | 注册时写入手机的 13 位识别号=PLI（2 位十进制）+PARI（11 位八进制）；算例 3110000400100 | p14, p17-18 |
| PLI | Park 长度指示器 | PARI 比对位数旋钮（最大 31）：单 PARI 用 31、multi-PARI 降位（30/29）使相近 PARI 等效 | p14, p18-20 |
| IPUI | 国际手持用户标识 | 固化在手机 EPROM 的 14 位八进制标识；webadmin IPUI N/O 字段回填即注册成功 | p14, p21, p169 |
| IPEI | 手机身份标识（书中未展开） | dectrm/8328 WBM 输出的呈现形式；8328 未注册时显示通用值 FFFFFFFFFF | p176, p286 |
| AC | 鉴权码（Authentication Code） | 注册时双侧比对，不一致则无法注册；系统侧 AC System 字段（实验 1111）；UAK 的派生种子 | p36, p144, p227 |
| UAK | 用户鉴权密钥（128 位） | 由 AC 派生、存于手机与系统库、从不上空口；自动重注册不重算 | p36, p253 |
| DCK | 派生加密密钥（64 位） | 每次呼叫开始由 UAK 派生、全程（含切换）保持、不广播不传输 | p36 |
| 维护命令族 | mtcl 命令集 | dectview/dectinston/dectrm/dectinfo/dectarea/downstat x|m/xbssynchro/incvisu/listerm/listibs/outserv/inserv/tcdump | p116, p137, p170, p176, p183, p230-234 |
| vendor class alcatel.ipxbs.0 | xBS 厂商类标识 | OXE 内部 DHCP 为 xBS 新增：识别 xBS 请求并下发 IP/掩码/网关/TFTP/DNS | p127, p146 |
| /usr2/downbin 与 /tmpd | 两个关键路径 | /usr2/downbin 存手机固件二进制（bin8212…bin8262EX）；/tmpd 存批量重注册清单与结果文件 | p181, p257-261 |
