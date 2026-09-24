# GLOSSARY — OXO Connect Starter 术语表

> 阶段 3 产出（源：candidates/glossary.md，46 条，六大域）。
> 口径：定义只采信本书正文；OMC/HSL/ARS/DDI/ARI/GAP/RGM/RSL 等缩写书中未给全称，如实标注；LOLA 书内无定义（needs-review nr-04）；p326 "freaking"、p201 "Simultaneaous" 为原文笔误。

# OXO Connect Starter (OXOCXTE300EN Ed16) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（472 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OXO Connect / OCE | OXO Connect 通信套件/Evolution | ≤300 用户企业与酒店的通信家族：OCE=纯 IP 的 IPBox，另有 Compact/Small/Large（PowerCPU EE） | p24-26, p30 |
| FTR | First Time Registration（书中展开） | OCE 首次注册流程：经 ETH1 网页登录、强制改密、填 IP 与三参考值，注册 Cloud Connect 并自动下载许可 | p57-62, p375 |
| Cloud Connect | 云托管交付路线 | 自动注册、软件与许可自动下载、Fleet Dashboard 远程机队管理；与 Standard（OMC 现场）二选一 | p51-53, p62 |
| ETH1 | 服务口 | OCE 第二网口：固定 192.168.94.246、自带 DHCP/DNS、myipbox.ale 直连；不得接 LAN、IP 冲突自动禁用 | p31, p57, p200 |
| OMC | OXO 管理软件（全称书中未展开） | 六类入口（Data Collection/Installation/Modification/Multi site/Expert 等）；承载密码、许可、备份、软件下载、复位全功能 | p63-71 |
| Data Collection | 数据采集 | 交付起点：客户需求+生态信息+待实现功能；OMC 向导可离线跑 | p43, p65 |
| Auto-Provisioning | 自动配置（终端） | Subscribers/BaseStations list 里的注册开关：IP 终端上线并自动分配目录号；三处 IMPORTANT 强调别忘开 | p88, p107, p118, p455 |
| Dynamic Routing | 动态路由 | 久叫不应两级两计时（T1→LEVEL1 目的地、T2→话务台）；apply diversion 总开关；级联上限 5 | p90, p164-166 |
| Attendant group | 话务台组 | 呼入分发容器（分机/MSG/General bell/VM 端口皆可入组）；组恒并行模式 | p254-255, p264 |
| DDI / Base | 直拨号/映射基数（缩写未展开） | DDI=公共计划映射到分机的直拨号；Base=内外映射基数（41100 base 100 ↔ 分机 100），取值域 0-2199 | p46, p128-130, p134 |
| Normal / Restricted mode | 正常/受限模式 | 日夜双模：呼入两套 DDI 计划、呼出两套 LC 值；默认用户不跟随时段 | p254, p277-278 |
| Barring / Link Category / COS | 闭锁/链路类别 | 出局三层：Traffic sharing LC（能否占组）→Barring LC（用哪张表）→闭锁表（6 张=6 级）；00 国际默认禁 | p271-275 |
| Installation number | 安装号 | 主系统 DDI 号，去掉第 1 位录入；SIP 默认规范格式 +国际码+城际码+安装号+DID | p130, p204, p229 |
| ARS | 自动路由选择（缩写未展开） | 出局号码分析与路由表；Easy Connect 后按国家补短号与紧急号码（法国典型四行） | p220-222, p366 |
| SIP Trunk Profile / Easy Connect | 运营商配置包/快捷开通 | 过 TSS 认证的运营商配置打包成 SPF 文件；Cloud Connected 系统网页选 Profile 少量参数完成配置 | p216-219 |
| Phreaking | 盗打 | 电话系统黑客行为：目标是客户钱包（一周末可损失 2 万欧以上），属有组织犯罪；防线=TC1143 | p326-329 |
| Warm / Cold / Factory Reset | 三档复位 | Warm 重启不丢库；Cold 回默认（不勾子选项保留四类）；Factory 再删系统日志、接近 Lola 态 | p322-324 |

## 二、角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Installer | 安装员账户 | 七管理账户之一：OMC Expert 连接、Webdiag、恢复均用此身份；首连密码 pbxk1064 仅一次 | p67, p81, p94, p349 |
| Reseller/BP Administrator | 经销商管理员 | Rainbow 侧可建 PBX、激活 WebRTC 网关、分订阅；网关自动配置唯一授权账户 | p338, p396 |
| End-customer Administrator | 客户管理员 | 管自己公司/用户/订阅分配/话机关联；Roles 页签可多名管理员 | p339-340 |
| Supervisor / Supervisee | 监督员/被监督成员 | 监督员须 Attendant 订阅、至多 5 组；每组 ≤30 人（两类合计）；互助组监督员属于其监督的组 | p409, p412, p417 |
| Manager / Assistant(Secretary) | 经理/秘书 | OXO 侧经理-秘书关系双方：均须 multiline 话机，互持 RSL/Screening/监督键 | p89, p140, p155 |

## 三、订阅与许可域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Rainbow 订阅目录 | 七种用户订阅 | Essential（免费无 SLA）/Business/Enterprise/Enterprise Conference/Conference（按量）/Connect（CRM）/Room；话务台另需 Attendant | p335, p409 |
| UTL | Universal Telephony License（书中展开） | 通用电话许可：IPDSP=1；FXS 网关每口=1 UTL+1 Open SIP；话机+Twinset 副站合计=1（UTL Bypass）；Anydevice=1 | p28, p101, p104, p401 |
| Software keys | 软件钥匙 | .msl 主钥匙+.csl CTI 钥匙，与主 CPU 序列号绑定；OMC 导入并 Apply；换 CPU 需重新生成 | p55, p71, p296 |

## 四、产品与硬件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| IPBox | OCE 硬件盒 | 双以太网（ETH0=LAN+PoE、ETH1=现场管理）、SD 卡槽备份选件、桌面/壁挂/机架半宽 1U | p30-32 |
| PowerCPU EE / MSDB / eMMC | 主控板/存储子板（书中展开） | MPC8377 @800MHz、16 VoIP 资源起步；MSDB 默认 8GB eMMC 承载数据备份 | p35 |
| Armada 32 / 64 | VoIP 资源子板 | DSP 通道：+Armada32=48；+Armada64=60 多编解码或 76（30 G711/G729+46 G711） | p36-37 |
| HSL / PowerMEX | 高速链路/扩展柜板（未展开） | 主控连扩展柜：最多 3 机柜、主柜到扩展柜最大 5 米，非以太网 | p36, p42 |
| 接口板家族 | UAI/MIX/AMIX/SLI/APA8/DDI2/DDI4/BRA/PRA | 机柜板卡：SLI16/DDI2/DDI4 无槽位限制；MIX=T0、A-MIX=APA；缩写未展开 | p431-435 |
| 话机家族 | ALE-20/300/400/500、8039、8214-8262、8158s/8168s | Essential/Enterprise/Basic SIP/数字/DECT/WLAN/会议全家桶；8039 为建议话务台机 | p97-103 |
| IPDSP / PIMphony / MicroSIP | 软话机三线 | IPDSP（1 UTL，实验主力 104）；PIMphony（Windows 四版）；MicroSIP（实验预装） | p10, p101-102 |
| 模拟-SIP 网关 | MEDIA5 4102/C710/C711 | FXS 2/4/8 口把模拟话机传真接入 OCE；每口 1 UTL+1 Open SIP，显示为 Open SIP 终端 | p104 |
| 8378 IP-xBS / 8328 | 两条 DECT 基站路线 | xBS：OXO 原生 ARI+GAP；8328：SIP-DECT 单基站 Web Admin 配 8214 | p100, p117-122, p453-456 |
| Webdiag | 内嵌诊断工具 | installer 会话：Rainbow Status、系统日志（ccrbagent.log）、证书管理、TCP Dump 抓包 | p69, p141, p241, p349 |
| Fleet Dashboard / OXO Connectivity | 云机队管理面 | FTR 完成后远程可达；识别 PBX/OCE-FE 配对、一键跳对端 | p62, p381 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| SIP / SIP Gateway | 会话发起协议体系/网关对象（缩写未展开） | 出局主协议；网关九页签（General/DNS/Domain Proxy/Registration/Media/Identity/Protocol/Topology/Security） | p197-201, p208-214 |
| SBC / CE | 会话边界控制器/客户边缘路由（书中展开） | 运营商侧 SBC 控制会话边界；CE=客户侧路由/防火墙/NAT+SIP NAT | p198, p202 |
| HTTPS / SRTP / TFTP / DHCP / DNS / NTP | 基础协议组 | IPDSP 证书时间敏感（HTTPS）；TFTP=话机取配置；WebRTC 音频 SRTP+HTTPS | p14, p57, p108, p371 |
| DECT / GAP / IPUI / IPEI / ARI | 数字无绳注册体系（缩写未展开） | ARI=系统级注册根号（11 位八进制，eBuy 获取）；GAP 注册出现 IPUI 后 Assign；IPEI 注册前默认 FFFFFFFFFF | p119-122, p463 |
| Messages 1-20 / MoH | 消息池/保持音乐 | 4 条默认、20 条许可、总 320 秒；MoH 仅外线保持、三源、Entity 1-4；.wav 8kHz Mono 硬格式 | p243-251 |

## 六、资源与数值域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| 资源键家族 RGM/RSL/RSP/RSB/RSD | 多线资源键（缩写未展开） | RGM 通用收发、RSL 本地、RSP 物理接入、RSB 中继组、RSD DID 监视；默认配比按话机模式查表 | p161-163 |
| Voice Mail（VMU） | 语音信箱 | CPU 集成：2 端口/4 语言/1 小时/问候 120 秒；三态信箱；General 信箱密码=话务员密码 | p183-189 |
| MSG 预公告数值 | 预公告参数 | 个人问候 200 条、预公告 20 条、总 320 秒；模式三选（分发前/分发中/仅忙） | p260-261, p269 |
| 集体缩位（Collective Speed Dial） | 系统级缩位目录 | OMC/collective speed dial 管理，受闭锁约束；话务台转移键常绑缩位号 | p280 |

## 备查（仅 passing 提及，不进主表）

- ITSP2（模拟器第二实例名）、RUFUS（制作启动 U 盘）、OmniVista 8770（证书告警上报目的地）、PIMphony 四版本矩阵、ADPCM/WAV 互转细节、DBAdapterSetup.msi 文件名、8088 v3/8135s 会议终端细节。
- 缩写书中未给全称者按提取器纪律如实标注：OMC、HSL、ARS、DDI、ARI、GAP、IPUI、IPEI、RGM/RSL/RSP/RSB/RSD、SBC（书中给出展开）、CE（书中给出展开）。

## 收尾自检（task↔术语映射）

- task-01→Data Collection；task-02→FTR/Cloud Connect/ETH1；task-03→OMC/Software keys/Installer；task-04→ETH1；task-05→Auto-Provisioning/IPDSP；task-06→8378/8328/DECT 体系；task-07→DDI/Base/Installation number；task-08→Attendant group/Manager-Secretary；task-09→Dynamic Routing/资源键；task-10→Voice Mail；task-11→SIP/SBC/Profile；task-12→MSG/MoH；task-13→Attendant group/Normal-Restricted；task-14→Barring/LC/COS；task-15→复位三档/eMMC；task-16→Software keys/Swap；task-17→复位三档；task-18→Phreaking/Installer；task-19→Webdiag/Fleet Dashboard；task-20→Reseller/EC 管理员；task-21→WebRTC 拓扑与容量（UTL）；task-22→UTL/Twinset；task-23→Supervisor/订阅目录；task-24→OMC/Data Collection。46 条术语覆盖 24 个 task 的全部关键概念，无遗漏。
