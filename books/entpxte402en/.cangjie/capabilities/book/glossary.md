# GLOSSARY — OmniPCX Enterprise 系统装载 术语表

> 阶段 3 产出（源：candidates/glossary.md，62 条精选门户版，六大域）。
> 口径：定义只采信本书正文；UMC/ELP/IBB/CMISE/PBWS 等书中未给全称的缩写如实标注；实验值（IP/账号/密码）一律标"实验口径"。

# OmniPCX Enterprise 系统装载 (ENTPXTE402EN Ed12) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（415 页），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| S.O.T. | 软件编排工具（Software Orchestration Tool） | 部署 ALE 产品（物理或虚拟）的虚机方案：ISO 内含 OVA、自带 DHCP/FTP；一次只允许一个部署任务 | p22-35, p56 |
| Standalone / Hosted mode | SOT 两种运行模式 | Standalone=技术员笔记本加载物理机；Hosted=ESXi 内加载虚机；SOT 与目标机须同网段 | p23-25 |
| Template Factory | 模板工厂（含降级模式） | 加第二块盘生成 VMware/KVM 镜像模板的第二配置；降级模式以 50GB 盘+templateFactory 命令绕过硬件前置 | p27-29, p155-165 |
| Greenfield project | 从零全新安装项目 | SOT 项目类型之一；与对既有产品 update 相对 | p85 |
| 多版本加载 (Multi version) | 多版本加载 | 同一块盘同时驻留两个版本（active/inactive）；不停话音装好、切换才重启、可回退 | p71-77 |
| 双分区 (Active/Inactive) | 活动与非活动分区 | 活动区 /、/usr2、/usr3、/var；公共区 /usr4、/usr7；非活动区 /root2_d、/usr5、/usr6、/var2 | p54-55 |
| 静态/动态补丁 (Static/Dynamic patch) | 静态与动态补丁 | 静态=停话音或装 inactive；动态=可热装但必须在同版本静态之后；补丁累积包含此前全部修正 | p65-66 |
| Distributor / Easy Installation | 分发器模式 | OXE 自当分发器：媒体传 /tmpd，swinst 9-10 本地解包安装；解包物落 /usr4/ftp/Rload 需手动清理 | p111-130 |
| OXE-V | 虚拟化专用 OXE 软件包 | 支持 ESXi/Hyper-V/KVM/Nutanix AHV/AWS 五类平台；许可经 FlexLM（仅 ESXi/KVM）或 Cloud Connect | p133-136 |
| OMS (OXE Media Services) | 软媒体网关 | 软件 GD4 板卡替身：每台 120 VoIP 通道、每 OXE 240 台；Lock 384 台数/385 通道，可不停机安装 | p138-140 |
| PCS (Passive Communication Server) | 被动通信服务器 | CS 信令故障时接管 OMS（软复位去、硬复位回）；云服务不跑 PCS | p147, p297 |
| GAS (Generic Appliance Server) | 通用设备服务器 | Rocky Linux+KVM 打包：OXE+可选 OMS/WebRTC 三 VM；FlexLM 内嵌；许可基于 ALU-ID 或 Cloud Connect ID | p219-242 |
| BootDVD | 宿主引导介质 | OMS/GAS 加载所需的 Rocky 操作系统 iso；新版 BootDVD 也是 host 补丁载体 | p184, p237, p250 |
| Cloud Connect (CCI) | ALE 云基础设施 | OXE 经 CC Agent 以 XMPP over WSS(443) 常驻+SOCKS5(80) 按需连接，换取 RTR/Inventory/Offer/远程控制台等服务 | p283-290 |
| FTR (First Time Registration) | 首次注册 | 用基于 CC-Suite-ID 的临时激活账户换取永久凭证；新装机自动执行（每 4 小时重试）；备机禁做 | p292-297 |
| FTR with PIN code | PIN 恢复注册 | RTR panic 后向 helpdesk 申请 6 位 PIN（5 天有效），在线重置全部云配置并重注册 | p298-301 |
| RTR (Right To Run) | 运行权（许可总开关） | dongle-less：每日应答 OK 加 0.5 天/NOK 减 1 天；资格期归零进 Panic；与 FlexLM 互斥 | p302-308 |
| Qualifying Period | 资格期 | RTR 宽限计数器：初始化 30 天；Save/Restore 跨重启保留、自动同步 twin | p304, p308 |
| Fleet Dashboard | 机队管理应用 | CCI 上的远程监控控制台：RTR 状态/Inventory/Offer 推取/远程控制台/软件更新 | p338-348 |
| CCTool / checkCloudConfig.sh | 云连接命令入口 | CCTool 四菜单（FTR/RTR/参数/日志级别）；checkCloudConfig 验证 DNS、443、80 三项连通性 | p314, p328-335 |
| swinst | 软件安装 CLI 工具 | Expert 菜单九项：分区复制与切换、备份恢复、系统管理（NTP）、软件身份、远程下载（分发器） | p98-99, p114 |
| OPEX / Purple on Demand (PoD) | 订阅模式 | 许可由云端 LMS 按项目池管理（硬件仍 CAPEX）；lock 431=1 开启；订阅目录缩到 24 项 | p350-380 |
| LMS / lmsagent | 云许可服务器与代理 | LMS 按项目建许可池；lmsagent 无状态 HTTPS 桥跑全部 CS（备机只读），每 4 小时对账 | p351-354 |
| C2P | CAPEX 转 PoD 转换 | MyPortal 工具五步转换（下单即定局）；C2P 件号 3EYxxxxxMA（PoD 为 3EYxxxxxAA） | p376-378 |
| OPEX activation (flag) | OPEX 激活旗标 | 激活才向 LMS 要许可、停用释放且保留配置；CAPEX 模式显示但不生效 | p368, p399 |
| 项目（PoD Project） | 订阅商务单元 | 一项目=一终端客户+一 BP；上限 1,500,000 用户；许可池项目内共享、跨项目不可移 | p355 |
| 信任主机 / IP tables | 防火墙白名单 | netadmin Security 菜单管理；分发器传输、许可恢复、云端更新域名（cdn-oxe-sw-update）都依赖它 | p324-325, p347 |
| autostart / RUNTEL | 电话应用启动策略 | swinst 设 autostart 自动起；未设时 mtcl 手动 RUNTEL | p58, p63 |

## 二、角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| BP (Business Partner) | 业务伙伴 | 交付执行者：软件交付、分发器传输、GAS 平台、PoD 项目唯一关联方、版本切换责任人、MyPortal 入口 | p112-113, p294, p355 |
| Helpdesk / ALE Technical Support | 支持两角色 | helpdesk 负责 PIN 签发与同 ID 产品断开；Technical Support 指定每版推荐版本 | p299-300, p346 |
| VAD / IR | 增值分销商与间接经销商 | VAD 可把子机队委托给 IR 管理（书中仅此一处） | p305 |

## 三、订阅域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| PoD 订阅目录（24 项） | 订阅目录 | 24 个商用订阅对照约 500 个 CAPEX 软件项；UMC 免费无订阅；No PRS；无 bulk 概念 | p357-366 |
| Voice Enterprise | 用户主档订阅 | 按用户计、不分终端类型、天然多终端；On activation 消耗；DSU/DSS 各一份 | p361, p368 |
| Softphone | 软话机订阅 | Voice Enterprise 选项，每用户一份；消耗双份制（+Voice Enterprise） | p361, p398 |
| Room | 酒店客房订阅 | 按终端计；按客人管理时房间与客人双开 flag、各占一份 | p361, p370 |
| SBC 订阅族 | OT-SBC 六订阅 | Session/Remote User/Transcoding/Direct Routing/SIPREC/Reverse Proxy，均含高可用 | p366 |
| OPR 三档 + API Recording Cnx | 录音订阅 | Standard/Business/Enterprise（端口型）+DR-Link 录音通道；OPR 每 24 小时校验 | p366, p369, p375 |
| UMC | 免费组件 | PoD 目录中免费提供、无对应订阅（书中未展开） | p360 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| CS3 / CPU8 / Appliance Server | OXE 物理承载 | CS3 板卡（BOOTP 引导）、CPU8（已从 MLE 目录移除仅 eBuy）、Appliance Server（已由 GAS 接棒） | p24, p57, p78, p359 |
| HP DL20 G11 | ALE 交付 GAS 机型 | 仅限 GAS 软件包、许可限 ALU-ID 或 CC-SUITE-ID、可跑满配（<7000 用户） | p227 |
| FlexLM / flexlmd | 本地许可服务器 | .ice 入 /opt/Alcatel-Lucent/data/licenses 后 restart flexlmd；OXE 对接端口 27000；仅 ESXi/KVM 可用 | p280-282 |
| Rainbow WebRTC Gateway VM | 彩虹视频网关虚机 | GAS 可选第三 VM（Debian）；50 并发封顶、>7000 用户外部网关 | p225, p267-268 |
| 运维命令集 | 命令面 | gasversion/gasbackup/uhwconf/omsconfig/spadmin/incvisu/netadmin/siteid/downstat/ver2cho 等 | p239-241, p327, p388-407 |
| 第三方工具集 | 流程依赖工具 | 7-zip/VirtualBox/Filezilla/Putty/Xming/TeraTerm/NUT 等 | p38, p86, p257-261 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| XMPP / WebSocket Secure | 云连接常驻协议 | XMPP over WSS（TCP 443）永久连接；ccagent 进程负责加密通道 | p287-289 |
| SOCKS5 | 按需穿防火墙通道 | TCP 80，为 Inventory/Offer 采集 PBX 数据；失败事件 6209 | p288, p290 |
| BOOTP / DHCP / PXE / TFTP | 网络引导协议族 | CS/CPU Crystal 走 BOOTP、AS 走 DHCP；引导文件经 TFTP 下载；OMS 用 IPXE、GAS 用 PXE | p56-60, p187, p252 |
| FTP / SFTP（端口 2222） | 文件传输通道 | 向 SOT 传媒体用 upload 账号（FTP/SFTP 2222）；GAS 禁标准 FTP 只能 SFTP/SCP | p86, p280 |
| V24 链路 | 串口控制台链路 | 加载过程中用于启动与检查安装 | p52 |
| TLS v1.2 / SRTP | 传输加密 | CC 通道强制 TLS 1.2（ALE 自有 CA）；OXE-V 原生加密拓扑媒体走 SRTP | p144, p289 |
| RFC 4733（RFC 2833） | DTMF 传输标准 | OMS 的 RTP payload 承载 DTMF 数字 | p139 |
| IBB protocol / CMISE | 点到即止协议名 | Push offer 依赖 XMPP IBB；OPEX 架构图连线标注，均未展开 | p342, p352 |
| ABC link / ABC-F | 多节点组网链路 | OXE-V Networking 拓扑多节点互联；Voice Enterprise 含 ABC networking（要求 Direct Link 型 ABC-F） | p148, p361 |

## 六、站点与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| MyPortal | ALE 客户/伙伴门户 | 下载软件与模板、查 TBE/TC 文档、C2P 网页、B2B eCommerce、Asset & service manager 下载 PoD 许可 | p62, p376, p381-385 |
| connect2.opentouch.com | 云连接固定 FQDN | 443（XMPP/WSS）与 80（SOCKS5）目标；checkCloudConfig 的解析测试对象 | p290, p314 |
| cdn-oxe-sw-update.al-enterprise.com | 软件更新 CDN 域名 | 使用信任主机的站点必须放行，否则云端下载失败 | p347 |
| TBE043 / TBE063 / TBE067 | 售前设计文档三件 | 虚拟化设计指南、OXE 与 GAS、Rainbow WebRTC 网关介绍 | p134, p225, p228 |
| TC2456 / TC3104en-Ed08 / TC3138 / TC3142en-Ed01 | 技术通报四件 | SOT 版本兼容、N3 迁移指南、Rocky 上装 GAS、AWS 部署 | p24, p78, p242, p149 |
| RLAB / POD | 培训远程实验室 | POD 间独立同构、共享 NAS 与 SIP 模拟器；网段 192.168.1.x（全部实验口径） | p1-20 |
| Cloud Connect Terms & Conditions | 云连接条款 | CCTool 手动 FTR 时展示的 businessportal 链接，接受条款是前置应答 | p329 |
