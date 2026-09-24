# GLOSSARY — OpenTouch Suite for MLE / Starter 术语表（门户版）

> 阶段 3 产出（源：candidates/glossary.md，56 条精选；全量在工作区 candidates）。
> 口径：定义只采信本书正文；OMS/GD4/Mule/ESS/REX/MIPT/DSU/SEPLOS 等缩写书中未给全称者如实标注，不做外部补全；MOFIFICATION/OUTLLOK 等为原文笔误（见 needs-review nr-02）。

# OpenTouch Suite for MLE (OPENXTE300EN Ed10) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（603 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OTMS | OpenTouch 多媒体服务套件 | 面向大市场的 OpenTouch 服务器套件（物理一体机），上限 5000 用户；横幅口径 2.6.1 / 18.0.100.003 | p5, p115 |
| OTMS-v / OT-v | OTMS 虚拟化形态 | ESXi/Hyper-V 上以六类虚机承载；许可锚加密狗、备份要 NFS、无本地 /var/backup | p8-9, p535, p555 |
| ICAS / ICM / AMS | OT 服务器三组件 | AMS=媒体服务器（MCU、G711/G729/G722、H264）；ICM=SIP 核心（ESS，5260）；ICAS=即时通信与协作 | p6-7, p541 |
| ACS / Stack | 协作应用服务器与栈 | 向导 1.5 节填 Stack name 与 Node ID；stack=2 台以上 ACS 组合提供备份与扩接入 | p7, p97 |
| SOT | 软件编排工具 | 以 ISO（内含 .ova）交付的部署虚机：自动挂载 ISO、静默安装含 hotfix、PXE 启动目标机；一次只部署一台 | p46, p53-65 |
| Post-installation wizard | 站点安装向导 | 首次开机自动启动的站点安装正式入口；from scratch 十节或 restore from archive 两模式 | p48, p88-89 |
| ALUID | 唯一硬件标识 | 128 位硬件标识（getaluid 读取）；物理服务器 .ice 许可的锚定物；虚拟化一律换加密狗 | p131, p162 |
| FlexLM | Flex 许可服务机制 | 服务可内嵌 OT 或外部虚机（端口 27000）；OXE 侧只验 Product ID，容量仍看本地 .swk | p131, p158-159 |
| Dongle (Aladdin) | USB 加密狗 | 虚拟化许可的物理锚定物，插在承载 FlexLM 的宿主/虚机上；ID 用 lmutil lmhostid -flexid 读取 | p131, p162, p173 |
| bics.conf | OT 凭证配置文件 | /var/data/bics/bics.conf：主机名/域与 otAdmin/otProfile/otuser 三账号的唯一出处；8770 声明与备份配置都读写它 | p194, p545 |
| Connection user (ACU) | 高级通信用户 | 挂 OXE 设备且授 OT 应用权的用户（type=OXE + Applications=OT）；由三档案合成 | p258, p264 |
| Directory user | 目录用户 | type=None：无设备无应用，仅进 8770 公司目录供查询 | p258, p267 |
| 三档案（OXE/OT/VM profile） | 用户供给三件套 | OXE profile（Set function=Profile、A0000 式占号）+ OT profile（Category=ACU-OXE）+ 语音邮箱档案；OXE 实时同步、OT 需手动完整同步 | p264-266, p277, p297 |
| UDAS | 目录检索模块 | 三路数据源单向同步进 PostgreSQL 同步库，检索只查同步库；周期至少 1 且禁 0 | p223-224, p243 |
| Dialing rule / DAS rule | 两套拨号规则 | Dialing rule 管 OT 侧一般外呼自动加前缀；DAS rule 管 Conference 侧按域正则改写，强制且随国家不同 | p220-222, p253 |
| Local Storage voice mail | 本地存储语音邮件 | OT 内置软件语音邮件（默认实例 defaultVmsLS）：留言未压缩 wav、IMAP 直读；UM 是另一套 | p304, p327 |
| Voice mail profile | 邮箱档案 | LS 型默认 Advanced/Classic/Simplified，UM 型 Standard；四页签控制行为；建箱必选档案 | p339-343 |
| General announcement | 通用公告 | 一次仅一条、覆盖式、5 分钟上限；wav 固定 CCITT A-law 8kHz 单声道、固定文件名 | p381-392 |
| Multi-devices | 多终端 | 一名用户最多 5 台设备（主/副白名单），REX 与 DECT 各 1；VoIP 不冻结话机 | p438-439, p484-485 |
| Supervision group | 监督组 | 同类型成员 2-40 人、一人一组、同 OT 节点；与 OXE 话机监督键无联动；上限 500 组 | p494-507 |
| rehosting | 改址改名变更 | ot-config.sh --rehost 改 OT 的 IP/主机名/FQDN/DNS/License server；配错死锁无回退；OXE/8770 按 TC2149 收尾 | p560-567, p579 |
| Maintenance Portal | 维护门户 | 维护命令图形化门户（WebAdmin 或 4448 直达），含 AppGuard Control Center；与 CLI、otconsole 三通道同源 | p519-521 |

## 二、角色与账户域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| BP | ALE 业务伙伴 | 物理硬件由 BP 或客户提供；Maintenance Portal 目标用户；提交服务请求需相关认证 | p9, p520, p602 |
| otAdmin / otProfile / otuser | OT 三账户 | otAdmin=8770 配置用（全权）；otProfile=模板管理用；otuser=维护/备份/SSH 用；bics.conf 可查、WBM 可互改前两者口令 | p95-96, p194 |
| mtcl / swinst / adfexc | OXE 三账户 | mtcl=维护命令行（netadmin/spadmin/swinst 入口）；swinst=软件安装/备份；adfexc=OXE FTP 账号（声明节点必填） | p111, p117, p190 |
| Supervisor / Supervised | 监督组角色 | Supervisor 看全组话务可代接；Supervised 被监督可进出组；可身兼两职 | p497, p510 |

## 三、订阅与许可文件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Desktop right | Desktop 许可 | 决定 OTC PC 以全量模式还是 One 免费模式运行；软电话/多终端副站场景必须勾选 | p433, p445, p467 |
| Universal / Conferencing option | 客户端许可阶梯 | Base Ct 用户许可 +Conferencing（会议插件）+Universal（Office/Skype 集成）；加许可即切模式 | p448, p458-459 |
| Unified management license | 统一管理许可 | Web Provisioning Client 前提：8770 3.2.8 起且须持此许可；浏览器仅 Chrome 54+ | p290, p292 |
| .ice | FlexLM 许可文件 | OT 与 OXE-v 用；内容含锚定物、OTID、Product ID；Flexlm 启动时复制改名进 final_licenses | p130, p148, p154 |
| .swk / .sw8770 / nmc.license | OXE 与 8770 许可 | .swk 专有加密（CPUID/FlexLM/Cloud Connect 验证、容量载体）；.sw8770 改名 nmc.license 由 8770 自查 handle | p130-132, p151 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OXE | OmniPCX Enterprise 呼叫服务器 | 套件的传统 PBX 侧；csa/csm 双地址；在 8770 声明并以 SIP trunk 打通 OT | p5-6, p186-192 |
| OmniVista 8770 | 管理服务器 | Windows OS；承载 Configuration（nmc）/Users/Directory/Alarms 应用与 WPC；OXE 与 OT 节点都在此声明互挂 | p6, p186-212 |
| OMS | OXE 媒体网关子系统 | 实验中以 Software Rack 3U 形式存在（Virtual GD4 挂 192.168.1.13）；OXE 改址时 OMS/MGD 内部 IP 同步改（全称书内未给） | p8, p33, p584 |
| OTC PC / OTC PC One | PC 软客户端两形态 | 同一安装包：Desktop 许可=全量（RCC+VoIP+协作）；无许可=One 免费模式（单线盲通话） | p432-448 |
| Mule / ESS | OT 两个 SIP 服务器别名 | ESS（ICM 的 SIP 核心）用户与呼叫接入 5260、不支持 G723；Mule（AMS 的 SIP 服务器）语音邮件接入 5040 | p215, p232, p218 |
| DM (Device Management) | 设备管理服务器 | 为 SIP 软设备生成下发 SIP 配置；实验由 8770 充当（端口 8080），文件落 OT 的 MYICPCSIP 目录 | p473, p489 |
| OT SBC / Reverse Proxy | 远程接入两件套 | SBC 承载外部媒体（SIPS/TLS+SRTP）、反向代理承载 Web 服务 HTTPS；细节在 TC2257/TC2639 | p444, p601 |
| ITSP1 | SIP 运营商模拟器 | 培训专用：SIP 网关与公网网关（账号 pbxP/alcatel）；号码规则含 POD 号 PN | p26-30 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| SIP Trunk / External Gateway | SIP 中继与外部网关 | OXE 侧 T2 型 trunk（实验 ID 10）、两条外部网关：10 到 ESS 5260、11 到 Mule 5040（仅出话） | p226-234 |
| SNMP v3 (Inform) | 告警协议口径 | OT agent 161、8770 server 162；认证 SHA、加密 AES 128、安全级 auth-privacy、通知类型 Inform | p205-209 |
| IMAP4 / SMTP / VPIM | 邮件三协议 | IMAP4 收语音留言（默认 IMAPS+TLS，内嵌 1000 会话封顶）；OT 无内置 SMTP（外部服务器须无认证无 TLS）；通知路由经 VPIM 会话声明 | p304-313, p360, p370-371 |
| CSR / PKCS7 / PKCS12 / CTL | 证书四件套 | CSR 生成时同时产生密钥对；PKCS7 对应 CSR 在 OT 侧做；PKCS12 带口令对应密钥在 CA 侧；CTL 换自签证书后须 808x 话机重签 | p404-407, p414, p427 |
| G711 / G722 / G723 / G729 / H264 | 编解码族 | AMS 媒体面 G711/G729/G722+H264；OXE 呼叫服务器 G711/G723/G729；ESS 不支持 G723；OT-OXE 互联两端一致（实验 G729） | p7, p218, p233 |
| PXE / OVF / OVA / vmdk | 虚拟化交付术语 | PXE 为 SOT 网络启动目标机机制；OVF/OVA/vmdk 为虚机描述/打包/磁盘格式（OVA=OVF+vmdk 打包） | p47, p79-80 |

## 六、资源与文档域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| BPWS / My Portal / TDL | 交付资源入口群 | BPWS 下载软件 ISO；My Portal 下载 FlexLM 虚机 OVF；eBusiness Portal 与 TDL 按 8AL 编号检索手册 | p42, p168, p601 |
| TC2149 / TC1652 / TC2257 / TC2639 / TC1625 | TC 技术通报族 | TC2149 ed.04（rehosting 全矩阵，附录全文收录）；TC1652（spatial redundancy）；TC2257/TC2639（SBC/RP）；TC1625（Clonezilla 镜像） | p231, p444, p561-602 |
