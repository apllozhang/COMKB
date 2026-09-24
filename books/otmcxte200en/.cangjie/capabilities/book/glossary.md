# GLOSSARY — OpenTouch Message Center 术语表

> 阶段 3 产出（源：candidates/glossary.md，46 条，六大域）。
> 口径：定义只采信本书正文；PRS/VPIM/ICE/OMS/BPWS/ALUID（有定义无全称）/OTID/OAM&P/EVS/FWK/MLE/DPNSS/VAA/flex-lm 等缩写书中未给全称，如实标注不补外部释义；p36 "Sytem"、p52 "Red Hat"、p53 "CheckSytemLinux.sh"、p84 "MOFIFICATION" 为原文笔误（见 needs-review nr-05）。

# OpenTouch Message Center Starter (OTMCXTE200EN Issue 08) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（259 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OTMC | OpenTouch Message Center | 单服务器独立语音邮件系统（定义含自动话务员能力），专服务 OXE 的 Connection 用户，取代 46xx/8440；运行于 SUSE Linux Enterprise | p5-6, p13 |
| OTMC-V | 虚拟化版 OTMC 软件包 | 面向虚拟化环境（VMware ESXi），可配 OXE 或 OXE-V；仅 vMotion/DRS（手动/半自动）在支持列表，限制与功能等同物理版；许可绑 USB dongle | p15-16 |
| Connection user | Connection 类用户 | OTMC 的目标用户类型；OT applications=None 表示不用 OT 套件应用但仍可有 OTMC 信箱——信箱与 OT 套件是两条独立许可线 | p5, p112 |
| Voice mail profile | 语音邮箱批控模板 | 管理员成池控制信箱行为/容量/期限/TUI 密码策略；默认四 profile；信箱创建必须挂 profile 才能保存 | p121, p139, p146-152 |
| Local Storage (LS) | 本地存储型语音邮件 | 留言存 OTMC 本地（默认系统 defaultVmsLS 即此类型）；wav 附件/链接/满箱提醒等通知增值为 LS 专属 | p137, p147, p169, p180 |
| Unified Messaging (UM) | 统一消息型语音邮件 | 留言落到统一消息后端（Microsoft Exchange/Lotus Domino/Gmail）；Standard profile 对应 UM；书内无落地配置步骤 | p147, p169 |
| Visual Voice Mail (VVM) | 可视化语音信箱 | 8xx8/8088 经信封键直达；默认要求输 TUI 密码（"Request password for visual voicemail access on set" 默认选中） | p122, p140, p149 |
| TUI / GUI password | 信箱两套用户密码 | TUI（Telephonic User Interface，书中展开）密码用于话机信箱与可视化信箱；GUI 密码用于网页（My Profile/MyMessaging）；与话机 set secret code（默认 0000）是两套体系 | p10, p130, p135, p142 |
| MWI | 留言等待指示（Message Waiting Indicator） | 新留言落箱话机 LED 闪亮；读邮件不灭灯（机制性不同步，非故障） | p171, p199 |
| Resurrection | 话机"复活"寻址法 | 话机处于 255/255/255 空态时直拨分机号+密码（默认 0000），系统自动绑定真实物理地址；也用于移机（配 In/Out of Service 前缀） | p113-115 |
| General announcement | 企业广播 | 留言落箱（外呼/内呼）与信箱查询前播放的公司级公告；单条/新录覆盖/≤5 分钟；wav 须 CCITT A-law 8bits 8kHz mono 且改名 general_announcement.wav | p210-227 |
| bics.conf | 站点配置账本 | post-installation wizard 全部设置落盘 /var/data/bics/bics.conf，含主机名/域与 ICE 三账户——8770 声明 OTMC 时的对账单 | p79, p92 |
| My Profile / MyMessaging | 用户自助 Web 双应用 | My Profile（FQDN 根路径）管个人设置；MyMessaging（FQDN/MyMessaging）网页听留言；登录用 GUI 账号，可见项受管理员授权 | p11, p156, p165 |
| High Availability (HA) | 高可用 | 向导 HA 页默认 Disable；启用需副服务器且两台同时跑向导；完整配置在"专门章节"（本书不含） | p74 |
| Automated Attendant (AA) / VAA | 自动话务员/外置话务员方案 | OTMC 定义中附带的能力但本书不教；p225 揭示 OT 服务器曾内嵌 AA（"arrive on AA"播报选项即其遗留，已废弃）；VAA 缩写未展开 | p5, p225 |

## 二、角色与账户域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| otAdmin / otProfile / otuser | ICE 三账户 | bics.conf 登记的三个功能账户：otAdmin=8770 配置（兼 WBM 登录）、otProfile=模板管理、otuser=维护/SSH/备份恢复（密码经 root 跑 /usr/bin/musett.sh 重置） | p75, p92-94 |
| adfexc | OXE FTP 账户 | 默认用户名/密码均为 adfexc；8770 声明 OXE 与 OTMC 拓扑声明 OXE 时都要填（data retrieval 用） | p87, p99 |
| mtcl | 呼叫服务器维护账户 | 用它跑 spadmin 查看激活许可文件的用户许可计数（左=已用/右=可用） | p118 |
| Greeting Manager(s) | 问候语集中管理网页（角色） | Greetings Management Web Interface for Administrators：按用户激活/删除/下载/上传问候语，数量不设上限；入口经 8770 右键 WBM | p128, p144-145 |

## 三、许可项域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Voice mail 许可三开关 | OTMC 账户级许可 | Licenses 页签：MyIC Business Communications 必开、Voice mail 必开（没有它信箱不可用）、Messaging API 可选 | p135, p141 |
| OXE 用户许可族（L173/174/176/177/316/317） | 话机用户许可三族六类 | TDM：174 模拟（Z）、173 高级话务（80x9）、316 Connection 话务（4019）；IP：176 高级 IP（80x8）、317 Connection IP（4008/4018）；SIP：177；核查走 8770 过滤或 mtcl+spadmin | p117-118 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniPCX Enterprise (OXE / OXE-V) | ALE 企业级 PBX | OTMC 的宿主交换机；本书覆盖其声明准备、SIP 对接、Connection 用户开通；OXE-V 为虚机形态（csa/csm 双命名） | p5, p27, p83-108 |
| OmniVista 8770 (8770-V) | 网管/配置平台 | OTMC 唯一的配置管理大脑（OTMC 是新节点类型+新图标）；统一用户管理/配置/告警拓扑/性能/备份恢复 | p12, p83-101, p228-246 |
| OMS / OmniPCX Enterprise GD | 实验拓扑组件 | 仅在拓扑/域名表出现（oms=151.1.1.13、gd=151.1.1.12），书中未展开全称与用途——引用时不补释义 | p22, p28, p31 |
| FlexLM server (FlexLM-V / flexlmd) | flex-lm 许可服务器 | 可内嵌 OTMC 或独立部署（可以是虚机）；管理 .ice 加载；服务名 flexlmd；核验 ./lmutil lmstat –a | p35, p42, p76-77, p82 |
| Eco-System VM | 实验基础设施一体机 | 一台 Windows 虚机承担 DNS/Exchange/AD/LDAP/DHCP 五角色，预置六域用户；教材的 SMTP/LDAP/AD 都靠它（纯教学） | p29-31 |
| VMware ESXi / vSphere | 虚拟化平台 | OTMC-V 指定平台；BIOS 关超线程 + 电源策略 High performance 两调优点；支持边界仅 vMotion/DRS | p15, p55-59 |
| Aladdin USB dongle | 许可加密狗 | 虚拟化部署的许可硬件锚点：.ice 经 dongle-ID 绑定；虚拟环境必须挂到承载 FlexLM 的虚机 | p14, p16, p35, p76-77 |
| Premium Deskphone 8xx8 / Smart Deskphone 8088 | 可视化信箱话机系列 | 信封键直达 VVM、支持问候语菜单；GUI 显示经 PRS，总量 5000 并发用户；其余话机走 TUI | p6, p8, p18 |
| SUSE Linux Enterprise Server | OTMC 底座操作系统 | 64 位 SUSE 12 口径；三种安装模式；root 默认密码首登强改；p52 "Red Hat installation" 为原文笔误 | p13, p48, p58-63 |
| Chameleon / Scorpio | OTMC 软件组件 | Chameleon=OT 框架组件（EVS+FWK，模板重启生效对象）；Scorpio=通知处理组件；排障 service chameleond/scorpiod status + /logs 三处日志 | p17, p185-186, p192 |
| IMAP4 Front End (imap4fed) | IMAP 服务组件 | OTMC 的 IMAP 入口：默认 IMAPS+TLS，端口按安全类型自动带出；改级须改端口并 service imap4fed restart | p208 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| SIP trunk group (T2 / ABC-F) | OXE 与 OTMC 直连中继 | 全系统仅一条、指向 front node；类型 T2、T2 Specification=SIP、Q931 变体 ABC-F；Bypass 按全部端口与用户数无关 | p18, p103-104 |
| PRS (Link) | 话机 GUI 显示链路（缩写未展开） | 支撑 8 系话机可视化信箱显示，5000 并发用户；OXE 侧端口 2570 | p17-18, p99 |
| VPIM | 语音消息组网协议（缩写未展开） | 用于 OTMC 互联与三方语音邮件互通；SMTP 通知的服务器路由也在 Messaging/VPIM 声明——双重身份 | p20, p185 |
| SMTP / POP3 / IMAP4 / IMAPS | 邮件协议族分工 | SMTP=发信（通知发外部服务器，OTMC 不提供且要求无认证无 TLS）；POP3=全量下载；IMAP4=直连查阅（OTMC 信箱访问方式）；IMAPS=IMAP over TLS（OTMC 默认） | p174, p197-198, p205-208 |
| G.711 / G.729 | 语音编解码 | OTMC 原生支持（p7）；OXE 与 OTMC 对接实验定 G.729、关多算法；通知附件音频格式（AAC/PCM16/PCM8/G.711 wav）与通话编解码是两套口径 | p7, p108, p184 |
| DPNSS prefix | 中继转接优化前缀（缩写未展开） | Translator/Prefix plan 建条目并把 Routing Optimisation 设为 Yes 才生效（实验 D1234） | p108 |
| CCITT A-law 8bits 8kHz mono | 广播 wav 强制格式 | general_announcement.wav 的固定音频格式（p223/p227 两页一致）；格式不符无法用作广播 | p223, p227 |
| flex-lm / .ice / ALUID / OTID | 许可技术栈 | flex-lm=许可控制机制（缩写未展开）；.ice=许可文件扩展名；ALUID=128 位硬件特征标识（整机贴纸或 /usr/bin/getaluid 取加密值）；OTID=p40 综合图标识（未展开） | p16, p35-36, p40, p42 |

## 六、文档与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| MyPortal / BPWS / Business Portal | ALE 资料入口三名称（均未展开全称） | MyPortal=取 OTMC 安装手册；BPWS=取软件 ISO；Business Portal=取 TC2024；如何取权限书内未说明 | p50, p58, p246 |
| Feature list / Product limits document | 特性清单与产品上限文档 | TUI 密码策略默认值、硬件软件规格与产品上限的指定出处；本书反复外指但不含其内容 | p10, p13, p48 |
| TC1652 / TC2024 / Quick Reference Guide | 三份外指文档 | TC1652=空间冗余 SIP 网关专项配置；TC2024=8770 上部署 NFS server；QRG=问候语管理细节（"Managing your welcome greetings message" 章） | p105, p142, p246 |
| /var/data 目录族 | OTMC 的 SUSE 侧关键路径 | licenses（=$LICENSES_HOME）、bics/bics.conf、panda/notification4（通知模板）、general_announcement（GA wav，两处口径）、ics-group/vms/ngvm3（statistics.properties）；日志在 /logs/... | p42, p79, p92, p185, p223, p227, p251, p256 |
| OpenTouch Suite for MLE / OT applications | OT 套件语境 | OTMC 是"OT based"语音消息专用包、可演进到全 OT 套件（MLE 未展开）；用户级 OT applications 字段与 OTMC 信箱无关 | p3, p14, p112 |
| enterprise-education.csod.com | ALE 培训目录站点 | 书尾"Find a Course"入口：查培训路径与后续课程（如 HA）；反馈另给邮政地址与邮箱 | p259 |

## 收尾自检备查（仅 passing 提及，未单列条目）

- OTID、alchostid.cfg（p40 许可综合图，无释义）附于 g28/g40。
- ESS/ICS/ACS/FAX/MOH（p232 备份数据库组件名，无展开）附于备份能力卡上下文。
- ICE_*（bics.conf 参数前缀）、"Gateway type ICE type"（p105）附于 g12/f14。
- EVS/FWK（p17 架构图）、OAM&P/UDA/MS（p17）附于 f03/g31。
- SEPLOS（p117 话机名）、OTC PC/one number（p112 OT 应用举例）附于 g21/g45。
- RUFUS、D.S.T.（p71 夏令时展开）、START TLS / RFC 2595（p7）附于 g36 备查。
- VAA（p225，未展开）附于 g15。
