# GLOSSARY — OmniPCX Enterprise SIP 术语表

> 阶段 3 产出（源：candidates/glossary.md，56 条，六大域；本表为门户精选版约 32 条）。
> 口径：定义只采信本书正文；CTL/OTSBC/ARS/NOE/ABC-F/DPNSS/REX/CSTA 等缩写书中未给全称，如实标注；p358 "EXISITING"、p239 "Cicular" 为原文笔误。

# OmniPCX Enterprise SIP (ENTPXTE403EN Ed12) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（465 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| SIP | 会话发起协议（Session Initiation Protocol） | RFC 3261 应用层信令协议，建立/维持/修改/终止多媒体会话；只协商不承载，媒体走 RTP、特征由 SDP 描述 | p45-48 |
| SEPLOS (SIP Extension) | SIP 分机级服务（SIP End Point Level of Services） | 电话应用把这类终端当"内部话机"：前缀/后缀业务、多线、寻线组/代接组、MESSAGE 显示；sipdict 中 type=3 | p66-74 |
| SIP Device | SIP 设备（远端子网形态） | 被视为远端子网一部分的终端（会议话机/门禁/视频），须私网+中继组+本地网关；无前缀/后缀、无 CTI、无坐席、不入组；type=2 | p66-78 |
| SIP Gateway (local) | 本地 SIP 网关 | Call Handling 与 SIP 代理间的接口；端口 5060/TLS 5061/MTLS 6261 | p57, p86, p91 |
| SIP Dictionary | SIP 字典 | 分机号 ↔ SIP URL 翻译表；重名用户用 alias 区分 | p57, p88, p92 |
| Proxy / Registrar / Location Server | OXE SIP 三服务器 | 代理（路由/权限/改写）、注册器（收注册、租期 1800/86400s）、位置服务器（URL→IP）；同栖 sipmotor | p51-57, p87-88 |
| Spatial redundancy | 空间冗余 | 每台 CS 有物理与角色 IP，客户端用节点名接入；内部域名解析器+DNS 委托保证只有 Main 应答 | p58-59 |
| DM / DM profile | 设备管理 / 设备管理档案 | 下发配置文件与二进制的模块（OXE N1 起自带）；profile 按子型适配（默认 0、上限 100） | p71, p144-153 |
| CTL | 话机证书信任列表文件（缩写未展开） | OXE DM 生成下发（/usr3/mao/DM/VHE8082 下 ctl_VHE8082、ict8000ctl.pem），含 RP/SBC 的 CA 证书 | p151, p166, p171 |
| ALES-DUID | ALES 设备唯一标识（RFC4122） | 每条 SIP 请求携带；OXE 以分机号↔DUID 实现一号多机互斥（403 + Warning 399） | p115-117 |
| Quarantine | 隔离 | 3 秒超 50 条消息自动隔离 30 分钟、报文丢弃；记录在 /usr4/tmp/sipalarm.log（f003） | p87-88, p94 |
| Dual partition / Force Download | 双分区 / 强制下载 | ALE-x00/ALE-30 双栈机制：YES 后台预载对侧二进制（首下载可达 30 分钟）切换即快切 | p187-194, p200 |
| auto-discovery | 自动发现 | 无配置文件时 401 触发认证：分机号+用户密码码（默认 0000）+MAC+机型；ALES 无此机制 | p157-158, p183-184 |
| Multi-devices | 多终端 | 纯 SIP 1 主+最多 4 副（ALES Windows/Mobile 各一）；混合 NOE+DECT 最多 3 台；RFC3326 Reason 同步 | p134-137 |

## 二、角色与账号域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| mtcl / swinst / root | CS 三个运维账号 | mtcl=维护查询与多数 CLI；swinst=软件与系统管理菜单（认证/nginx）；root=高权限（PKI/SSL 级/killall）；口令实验口径 | p62, p91-94, p169, p225 |
| UAC / UAS / B2BUA | SIP 实体角色三件 | UAC 发请求（主叫）、UAS 应答（被叫）、B2BUA 两侧各扮一角且两段会话独立（与 proxy 本质区别） | p51 |
| Supervisor / supervisee | 监督员 / 被监督人 | 监督员持监督键（≤40）监视/代接/直呼；被监督人状态经 NOTIFY 推送；仅 SIP 设备可被 SIP 设备监督 | p130-133 |

## 三、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniPCX Enterprise (OXE) | ALE 企业级通信服务器 | 本书宿主 PBX，版本口径 R101.1 MD4（截图混 R100.0/R101.0/R101.1） | p1, p56 |
| ALES (ALE SoftPhone) | ALE 软终端 | Windows/Android/iOS 软话机，SIP+（Purple 起）；仅 OXE DM 管理；子型 ALES-desktop/ALES-mobile | p106-121 |
| ALE-2 / ALE-3 | 基础型 SIP 话机 | 仅 Business 模式、原生加密、8/12 可编程键、内嵌 OpenVPN（唯一）；DHCP 类 ALE-2X/VCI aledevice | p99, p172-186, p412 |
| ALE-30 / ALE-x00 | Essential 与企业档话机 | ALE-30 支持 1 个 EM-200；ALE-300/400/500 双栈双分区、NOE↔SIP 可切、120 可编程键；VCI ictouch.0 | p100-105, p187-216 |
| 8008 / 8008G / 8088 | Essential 特例与 Huddle Room | 8008 走 Business+酒店模式（可 OXE DM 管）；8088 酒店/Huddle Room 仅 8770 DM | p98, p147 |
| OTSBC | ALE 会话边界控制器 | AudioCodes Mediant 平台底座（缩写未展开）；SIP trunking 与远程办公公共底座，内嵌反代 ≤500 用户 | p336-345, p387 |
| OmniVista 8770 | ALE 管理平台（8770 DM） | 传统 SIP 设备管理方；开关=系统参数 "Device Management in 8770"；关闭即删其配置文件 | p71, p146-150, p174 |
| Internal PKI | OXE 内部证书机构 | netadmin 11/9/1 一键生成根 CA+CS 证书（SAN 含 FQDN/通配/IP、密钥默认 4096）并产出 CTL | p168-171 |
| EDS (Easy Deployment Server) | 易部署服务器 | ALE 云端零接触部署服务器（AWS 巴黎）；话机硬编码 device.eds.al-enterprise.com | p401, p404-406 |
| OXE-MS | OXE 媒体服务资源 | OPUS/G722 的转码/会议/语音指南必要资源，编解码资源动态列表排最前 | p276, p281 |
| IPDSP / MicroSIP | 实验软话机两类 | ALE IP 桌面软话机（实验主用）/ 第三方 SIP 客户端（模拟公网用户与 SIP Device 终端）——教学基础设施 | p10, p39-40 |
| NGINX / NGINX PLUS | Web 服务与反代 | OXE 内嵌 NGINX 为 DM 下载通道（443/8443）；NGINX PLUS 为 >500 远程用户推荐反代 | p157-160, p387 |

## 四、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| SDP | 会话描述协议（Session Description Protocol） | 在 SIP 信令里携带 RTP/RTCP 端口与编解码清单；SDP in 18x 参数决定 180 是否带 SDP | p48, p86-87 |
| RTP / RTCP / SRTP | 媒体传输与加密 | RTP 承载音视频；SRTP 为加密媒体流（SEPLOS 原生加密与 SBC 媒体安全的落点） | p45, p99, p337 |
| TLS / mTLS / SIPS | 传输安全三件 | TLS 保信令（5061）；mTLS 双向证书（DM 8443、话机↔RP/EDS）；SIPS 为加密 SIP URI 形态 | p48, p159-160 |
| Reverse Proxy | 反向代理 | 把互联网侧请求转发到内网 OXE DM；≤500 用户用 OTSBC 内嵌实现 | p388-395, p421-435 |
| NOE | ALE 话机传统 IP 协议栈（缩写未展开） | SIP 的对照系与共存系：ALE-x00 双栈可互切；NOE 设备 VCI=alcatel.noe.0 | p39-40, p135, p154 |
| ARS | 自动路由选择（缩写未展开） | 出局选路引擎：前缀→判别器→路由表→时间清单；SIP 中继组配外部网关必须配 ARS | p355-358 |
| NPD / DID translation | 号码计划描述 / DID 翻译 | NPD 定主被叫号码计划与默认号（出向），DID 翻译把外线号段映射回内线（进向）；回拨翻译整理显示号码 | p359-361 |
| DTMF（三法） | 双音多频传递 | RFC4733（RTP 载荷）/SIP INFO（逐位+200 OK）/带内（音频）；方法在 DM profile 配置 | p305 |
| LDAP / LDAPS | 目录服务双用途 | ALES 登录认证（swinst 配 uid/Bind DN）+ 目录搜索（DM profile 配 URL）；远程时 RP 与 OXE DM 须同源 | p110-111, p225-226, p395 |
| TFTP / DHCP option 66-67 / VCI | 终端引导三件 | TFTP 字段实为 DM HTTPS URL；option 66 下发 DM URL、option 67 下发 sipconfig.txt；VCI 区分终端族 | p151, p181-182, p204, p214 |
| CAC | 呼叫准入控制（Call Admission Control） | 注册 IP 决定终端归属 IP 电话域与带宽档；本地网关 CAC SIP-SIP 决定是否校验域权限 | p80, p86-87 |
| Quarantine Framework | 防隔离框架参数 | SIP Proxy Framework period=3s / Nb Message=50；ALES 必配防误隔离 | p87-88, p227 |

## 五、资源与文档域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| RLAB / POD | 培训远程实验室/实验单元 | 按 POD 划分同构实验单元（全虚拟化/混合），共享 NAS 与 SIP 模拟器；POD 号嵌入全部号码账号 | p5-19 |
| ITSP1 / ITSP2 | SIP 运营商模拟器两腿 | ITSP1 直连（gateway1.itsp1.com，pbxP/alcatel）；ITSP2 经 SBC（gateway.itsp2.com，podP/alcatel） | p21-34 |
| ITServer | 实验基础设施机 | 192.168.1.252，NTP 与 OpenLDAP 合一（实验口径） | p9, p219 |
| TC2005 / TC2957 | ALE 技术文档两份 | TC2005=运营商 SIP 网关参数依据；TC2957=ALES Remote Worker 快速部署指南 | p349, p411 |
| MyPortal | ALE 客户服务门户 | OTSBC 部署软件（OVF/ISO）下载入口 | p365 |
| FlexLM Server | 实验许可服务器 | 192.168.1.80；证书生成时 CC-suite-ID 取自许可文件 | p9, p38, p169 |
