# GLOSSARY — OmniSwitch LAN Access Switching 术语表（门户版）

> 阶段 3 产出（源：candidates/glossary.md，60 条，六大域；本表精选高频约 45 条）。
> 口径：定义只采信本书正文；EMP/RCL/VFL/QSI/ISIS-VC/BUM 等缩写书中未给全称，如实标注；UNP 全称书中两写（User/Universal Network Profile）为同一概念。

# OmniSwitch LAN Access (DT00XTE215EN Ed23) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（587 页），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| AAA / ASA | 认证交换机访问（Authenticated Switch Access） | 按服务类型（console/Telnet/FTP/HTTP/SSH/SNMP/default 七条链）配置认证服务器序列，支持 fail-through 与 exit-on-fail；还借管理站清单限管理源 IP | p67-69, p85, p95 |
| WebView | 内嵌 Web 管理 | 交换机内置 Web 应用：单机视角、R8 默认强制 SSL、配置分七大组；默认服务开但认证未授权时登不进 | p81-82, p97-101 |
| Lightning Config (OLC) | 快速开局向导 | 笔记本 DHCP 接端口 1、https://192.168.0.1、Defaults+必填项+改密+保存；一次一台、支持 .json 模板 | p102-126 |
| Working / Certified / Running | 闪存三目录 | working=试验场、certified=认证回滚基线、running=当前启动目录；冷启动按内容异同判定，reload all 强制 certified | p129-131, p141-147 |
| write memory flash-synchro | 保存并认证（一步） | =write memory + copy running certified；VC 下同步全体成员 | p132-133 |
| vcboot.cfg / vcsetup.cfg / userTable | 三个关键文件 | 文本配置文件（VC 参数在 vcsetup.cfg）；userTable=本地用户库（flash/system）；备份三件套 | p70, p129, p136, p141 |
| Virtual Chassis (VC) | 虚拟机箱 | 多台经 VFL 互联呈现为一台逻辑交换机：单管理点、成员间无需 STP/VRRP、免许可、支持 ISSU | p150-163 |
| VFL | 堆叠互联链路（全称未展开） | VC 成员间专用或复用端口；auto 模式（vf-link-mode auto）或静态指定；member-port 有主备之分 | p152-154, p159, p180 |
| ISSU | 滚动升级（In Service Software Upgrade） | 新代码放 issu_dir，slave 按 chassis ID 从低到高逐台重载，业务中断最小化 | p162 |
| ssh-chassis | 跨成员 SSH | ssh-chassis admin@<id> 映射 127.10.<id>.65；提示符相同，看 Local Chassis 字段确认所在成员 | p163, p181 |
| UNP | 用户网络档案（User/Universal Network Profile，书中两写） | 按用户/设备下发的档案：VLAN 映射+ACL/QoS 策略列表+位置+时段；由 RADIUS Filter-Id 回传 | p185-192, p393, p456-477 |
| Access Guardian | 接入守护（特性集名） | 基于 UNP 的角色接入控制：802.1x/MAC 双认证、pass-alternate 降级、auth-server-down 档案、端口模板 | p454-485 |
| DHL Active-Active | 双归属链路双活 | 每交换机 1 会话 2 链路；VLAN 分流双活、故障全量切换、恢复等抢占（默认 30 秒）；DHL 端口自动禁 STP | p324-344 |
| policy 引擎 | 统一策略引擎 | condition+action+rule；QoS/ACL/PBR/镜像共用；qos apply 下发生效；默认 disposition accept | p400-407, p431 |
| QSet / QSP / QSI | 队列模型 | 每端口 8 队列（QSI）；队列集档案 QSP 定义调度（QSP 1=8SP、QSP 2=1EF+7SP） | p397-398 |
| Loopback0 | 环回接口 | 不绑 VLAN、永活；RIP/OSPF 自动通告（BGP 不会）；RP/sFlow/RADIUS 源/NTP/BGP/OSPF router-id/NMS 七类用途 | p360-361 |
| show running-directory | 启动状态判读命令 | 三字段：启动目录名、Certify/Restore 状态、同步状态——排障"配置丢了"第一入口 | p142-147 |

## 二、管理与安全域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| admin / default | 出厂两用户 | 默认 admin/switch；本地库上限 64 用户；8.10R03 警告、8.10R4 强制改默认密码、8.10R04 强制首登改密 | p70-71 |
| password-policy / size / expiration / refresh | 密码治理四层 | 复杂度（禁用户名/连续字符/四类字符最少个数）、生命周期、强制刷新（IEC62443-3-3 Level 2 Ready in 8.10R3） | p72, p74 |
| EMP | 旁路管理口（全称未展开） | 旁路 NI 直连 CMM；无口机型 8.9.R1 起 USB-Ethernet dongle 等效；VC 全员插 dongle 才有完整 VC EMP | p78-79 |
| empacl | EMP 口策略 | 仅源/目的 IPv4 的 PBR 条件与动作；全机仅一条 empacl 策略列表 | p79 |
| UserPorts / DropServices | 保留安全组 | UserPorts 端口组反 IP 欺骗（仅作用路由流量）；DropServices 在用户口丢指定 TCP/UDP 服务 | p440-443, p453 |
| command logging | 命令日志 | command.log 滚动存最近 100 条（命令/用户/时间/来源/结果）；启用期间不可删除 | p245 |
| Readable Customer Event Logs | 可读事件日志 | swlog 过滤为 event 级后 show log events；四段格式=时间戳:CMM/NI:模块:描述 | p243 |
| RADIUS（默认参数） | 认证服务器 | retries 3、timeout 2 秒、auth 1812、acct 1813、默认无 SSL（建议 TLS）；MAC 会话默认 12 小时 | p472 |
| 802.1X / PEAP / MSCHAPv2 | 端口准入认证族 | supplicant 侧 EAP（实验用 PEAP+免 CA+MSCHAPv2）；MAC 认证以源 MAC 作账号密码；可同端口并存 | p457-458, p481 |
| Filter-Id | RADIUS 回传属性 | 认证成功后以 Filter-Id 回传 UNP 名，决定用户 VLAN 与策略 | p457, p480 |
| pass-alternate / auth-server-down | 降级档案 | Filter-Id 缺失走备用档案；服务器不可达全体迁降级档案（默认 60 秒重试重认证） | p466, p474 |
| convert-cert / check-revocation | 证书两工具 | DER/PEM/PKCS#12/P7B 转 PEM；CRL/OCSP 吊销检查（限 RADIUS/Syslog over TLS） | p74 |

## 三、二层与三层域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| 802.1Q / 802.1p | VLAN 标准与优先级位 | 4 字节头含 12 位 VLAN ID（4096 tag）与 3 位 802.1p（8 级）；物理口恒有一个默认 VLAN 桥接 | p199, p292-295 |
| UNP 分类规则 | 动态分类优先级 | 九条简单规则按编号即优先级；Extended > Binding > Simple；UNP 口启用而认证关闭/失败时应用 | p189-192 |
| Static / LACP | 聚合两型 | 静态仅 ALE 间且两端参数一致；LACP（802.3ad）LACPDU 协商、可接服务器/存储 | p273, p275 |
| hash-control | 负载分担算法 | brief（仅 IP）与 extended（含 UDP/TCP 端口）；出厂默认逐型号（9900/6870/6860/6865/6560=extended，6900/6465/6360=brief） | p280 |
| STP / RSTP / MSTP | 生成树家族 | flat 与 per-VLAN（默认）两模式；802.1d 50 秒、802.1w/802.1s <1 秒；默认桥优先级 32768 | p300-311 |
| path-cost-mode | 路径成本口径 | 16 位（10M=100/100M=19/1G=4/10G=2）与 32 位（200 万/20 万/2 万/2000）两套；auto 按协议跟随 | p301, p309 |
| ISIS-VC | VC 拓扑协议（全称未展开） | 私有 TLV 交换能力与编号、HELLO 建邻接、维持 BUM 无环拓扑 | p155 |
| MAC retention | MAC 保持 | 恒开：master 故障接管后二层身份（MAC）不变；原主恢复不抢回 | p157 |
| RCD / VCSP | 分裂防护双机制 | 带外 RCD 经 EMP 侦测（CMM 地址优先）；带内 VCSP 需 helper 与 VCSP LAG；检出后原 slave 关用户口 | p160-161 |
| VRRP | 虚拟路由冗余协议 | 虚拟 IP+MAC 00-00-5E-00-01-{VRID}、组播 224.0.0.18；默认优先级 100、默认抢占；改优先级先 disable | p374-390 |
| DHCP Client / Relay | 动态取址与中继 | Client 按 RFC 2131 落地 Option-1/3/51/58/59/60；Relay 全局与接口两型互斥、max hops 16 | p350-355 |
| 静态路由 | 静态路由 | 默认优先于动态路由；metric 调优先级可做主备默认路由；关联接口须 up | p363-364 |

## 四、策略与终端域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| qos apply / reset / flush / revert | QoS 生效与清理四命令 | apply 下发硬件（全局设置立即）；reset 回默认、flush 清配置、revert 删 pending | p422-425, p449 |
| auto-QoS（qos phones） | 话机自动优先级 | 四个 ALE 话机 MAC 段命中即给优先级 5；信任与非信任端口都生效、默认启用 | p410 |
| Tri-Color | 三色标记统计 | 限速下 Green/Yellow/Red 计数；大包 ping 触发 Red（实验口径） | p426 |
| LLDP / LLDP-MED | 发现协议与 VoIP 扩展 | 默认收发双开、30 秒、TTL 倍乘 4；MED 四扩展=网络策略/位置/扩展供电/资产；不支持 linkagg 级配置 | p486-505 |
| network-policy / mobile tag | 语音策略与动态打标 | lldp network-policy 下发语音 VLAN+l2-priority+dscp；unp mobile-tag+分类规则让话机动态入 VLAN | p495-496 |
| PoE（802.3af/at/bt） | 以太网供电四档 | PD 可用 12.95/25.5/51/71W；PSE 15.4/30/60/100W；预算与优先级（low/high/critical）管理 | p513-517 |
| Fast PoE / Perpetual PoE | 快速供电/重启不断电 | 支持 2X60/6360/6860E/6860N/6865/6870（OS6360-P10A 除外），需升级 FPGA/CPLD | p510-511 |
| delayed-start | 延迟供电 | 120-600 秒（5 的倍数）；与 FPoE/PPoE 互斥；必须 write memory 随启动生效 | p520 |
| LBD | 环路检测（Loop Back Detection） | 周期组播帧回收即判环路：端口强制 down+日志+trap，可手动恢复 | p549 |
| Auto-Fabric | 零触开局七步链 | Auto-VC > RCL > Auto-LACP > Auto-Routing > Auto-SPB > Auto-Network Profiling > Auto-MVRP；首启 Y=禁用/N=启用 | p536-554 |

## 五、产品与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniSwitch 家族 | 交换机产品线 | Core=OS9900/6900；Aggregation=OS6870/6860N；Edge=OS6560/6360/6370 等；选型查 datasheet | p53-56 |
| OmniVista（2500/Terra/Cirrus） | 网管平台家族 | 升级通道之一（Cirrus 最简）、SNMP/RMON 展示端、Fleet 资产来源 | p56, p84, p533, p563 |
| Fleet Supervision | 资产合规监管云 | myfleet.ovcirrus.com；版本/库存/KPI 看板；免费但只读 | p555-569 |
| OST（1.0/2.0） | 装机排障桌面工具 | 1.0 社区版停更；2.0=Client-Server+Postgres，100 交换机/4000 设备/5 并发，需支持合同 | p215-231, p572-580 |
| MyPortal | ALE 门户 | 软件包与 OST 2.0 下载（按品类） | p11, p229, p534 |
| AOS 文档族 | 权威文档五册 | Specifications Guide/CLI Reference/Network Configuration/Switch Management/Release Notes——规格与步骤的唯一依据 | p9, p80, p158, p422, p533 |
| Demo License | 演示许可 | Auto-VC 场景默认启用；事件日志出现到期提醒 | p263, p540 |
| R-Lab / RustConn / Proxmox | 培训远程实验室 | rdp.al-mydemo.com、LanpodXa/Xb；RustConn 管控制台与客户端桌面，Proxmox 开停虚机（实验口径） | p12-24 |

## 收尾备查（仅 passing 提及，不进主表）

PVST+（p305 Cisco 互操作字段）、KERNEL.LNK（p130 启动选择文件）、U-Boot/ONIE（p130/p533 引导层）、FPGA/CPLD（p510-511）、DER/PEM/PKCS#12/P7B/CRL/OCSP（p74 证书族）、GA/MR（p532 已展开）、AVLAN（p443）、DEI（p399/p422）、ECT-ID/ISID（p547 未展开）、AVR/RTF（p560 支持等级缩写）、GA/EoS/EoL（p560 生命周期）、FileZilla/TigerVNC/pfSense（实验工具）、BUM/MTP（glossary 候选 g54 已并入相关行）、PolicyView（p400 OmniVista 组件）。
