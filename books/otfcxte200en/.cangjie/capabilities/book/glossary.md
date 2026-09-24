# GLOSSARY — OpenTouch Fax Center 术语表

> 阶段 3 产出（源：candidates/glossary.md，57 条，六大域；本表精选高频约 30 条）。
> 口径：定义只采信本书正文；DNIS/CSID/ANI/DDI/ARS/MLE/SMB/CSGD/MMC/BIRT/UTL 等缩写书中未给全称，如实标注；p41 "Outlook 2022"、p148 停止命令行混排为原文笔误（见 needs-review）。

# OpenTouch Fax Center (OTFCXTE200EN Ed04) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（233 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OTFC | OpenTouch Fax Center | 与 OXE 交互的传真服务套件，硬件无关，装在专用服务器或虚机，完全软件化（Fax over IP） | p4-5 |
| System | 系统 | 概念模型顶层：全局管理与系统设置、管理所有站点；首装选 "Create a new system" | p22, p49 |
| Site | 站点 | 虚拟传真服务器：共享系统资源的逻辑分片，站点间隔离，"One fax belongs to one and only one site"；可对应公司/分支/部门 | p22-23 |
| User | 用户 | 恒以 SMTP 地址标识；属于一个 Site、有一个 faxing Profile，三绑定缺一不可 | p23 |
| Profile | 用户策略模板 | 封面/组织/计费码/优先级/重试/安全/通知的属性集合，可服务多用户；默认 Basic 与 No Faxing Rights 两档 | p23, p118 |
| First Time Setup Wizard | 首次安装向导 | 完成最小系统配置让人立刻能传真：建站点、QOS 0/0/240、CSID=站点名、建首用户、路由表、告警通知等 12 项 | p50, p67 |
| Restriction group | 限制组 | 拦截表（barring table）挂一个/多个 Profile 控制外发号码范围（如仅国内禁国际）；与 OXE 语音侧闭锁是两套 | p121 |
| Calling Number Restriction | 来话号码限制 | 站点级按号码拒收来传真，呼叫建立阶段即拒接；路径 Sites ➤ General Settings ➤ Calling Number restrictions | p122 |
| Site/Profile Lookup table | 站点/Profile 归类表 | 基于目录属性的 if 规则，把外部用户自动归到站点与 Profile；没归到即不能使用 OTFC | p198-200 |
| NT Account Lookup | NT 账号查询 | 让用户免认证使用客户端应用：AD 专用接口或 LDAP 配 samAccountName 过滤器；Web 自动登录还需 IIS 禁匿名+启 Windows 认证 | p100, p201-204 |
| MediaStore | 传真媒体库 | 收发传真的 TIFF 图像与外发原始文档，存于 Data\MediaStore；备份三数据域之一、删除策略的"传真文档" | p217, p223 |
| Cover Sheet (.cse) | 封面页 | 传真首页版式文件，专有 .cse 格式；Editor 创建、Web 管理导入、经 Profile 下发（一个 Profile 可挂多张） | p92-96 |
| Broadcast | 广播 | 同一传真分发多个收件人，共享相同附件与封面；完成时可通知发起人 | p28, p10 |
| Notification | 事件通知 | 新传真到达/外发成败/广播完成三类事件；投递类型 Email、Printer、Folder | p24 |

## 二、角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| System Administrator | 系统管理员 | 管整个系统可设多名；认证基于内部服务器/AD/SAML；日志大小与保留期仅其可改；官方推荐建备份管理员 | p77, p108-110, p225 |
| Site Administrator | 站点管理员 | 只有权配置自己的站点（多租户/部门分权角色） | p77, p109, p111 |
| Reseller | 经销商 | 许可采购对象：提供传真服务器物理（MAC）地址换正式许可文件 | p52 |

## 三、许可/订阅域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Default License | 默认（评估）许可 | 首装自带：每组件 1 实例、共 2 通道、10 站点不限时、100 用户、每页水印 | p52 |
| Licensed feature (SMTP connector) | 许可特性 | SMTP 连接器受特性开关控制——功能装上了许可不含时不可用 | p158 |
| License import | 许可导入 | 只能手工导入许可文件；采购前置动作是给经销商服务器 MAC 地址 | p52-53 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniPCX Enterprise (OXE) | ALE 企业通信服务器 | OTFC 的话路对端：需配 SIP private trunk 与网关（MGR 七步）；互通细节参照 TC3048 | p4, p34, p141 |
| FaxManager（XMFaxManager） | 传真管理器 | 系统心脏：管收发队列、向所有组件分发任务、管媒体文件库 | p26-27, p180 |
| FaxDriver（XMFaxDriver） | 传真驱动 | 用 H.323/SIP（T.38/G.711）真正收发传真，可并行多路呼叫 | p181 |
| DocumentRasterizer | 文档光栅化器 | 把 45 种格式文档转传真 TIFF，借助本机 Office 原生应用（需预初始化防弹窗） | p18, p51, p182 |
| SMTP Gateway（XMSMTPGateway） | SMTP 网关 | 监听 25 收传真作业发通知；不能与其他 SMTP 服务共存；feedback address 不能为空 | p157, p161, p183 |
| MMC Snap-in | 管理控制台 | 随服务器安装的管理单元（位于 FaxCenter\Client）；与 Web 管理页并称双入口；无 CSV 导入导出 | p74-75, p83 |
| Web administration page | Web 管理页 | http(s)://<服务器名或IP>/faxadmin；独占用户 CSV 导入导出与封页导入 | p74, p95, p104-105 |
| Web Client | 网页传真客户端 | 免安装任意浏览器访问 /fax；六区界面；符合 508 条款与 e-inclusion | p79-81 |
| SendFAX | 进阶传真客户端 | 实时预览/Outlook 模式/电话簿/redact 涂黑；Outlook 模式依赖 'FAX' 地址空间 | p86-87 |
| OmniVista 8770 | 网络管理与计费平台 | 从 OXE 取传真计费票出报表（默认映射传真号）；亦可替代 MGR 管 OXE | p152, p212-213 |
| MySQL | 后端数据库 | XMFaxArchive 与 XMCoConfig 用；备份时单独停 mysql5 并整拷数据目录 | p29, p217-218, p231 |
| BIRT Report Designer | 报表设计器 | 自定义 31 个报表模板；从安装包 3rd\birt 解压安装（缩写书中未展开） | p226 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| FoIP | IP 传真（书内全称 Fax over IP） | 全软件传真实现：SIP/TCP 或 SIP/TLS，经 T.38/SIP 连 OXE | p7 |
| SIP | 会话信令协议（全称书中未展开） | OTFC 本地监听 UDP 5360；支持认证与 SIP 消息日志；SIP/TLS 仅概览提及无启用路径 | p7, p142 |
| T.38 | IP 传真实时协议（标准名，书中未展开） | 主传真通道，含 Group 3 传真，最高 14.4kbps | p7, p34 |
| G.711 | 语音编码透传（标准名，书中未展开） | 传真当语音流透传，速率最高 33.8kbps（比 T.38 快） | p7 |
| T.30 / T.37 | 模拟传真/存储转发协议（标准名，书中未展开） | T.30 在 OXE 的 PSTN 侧模拟传真；T.37 指 T.37 能力的局域网 MFP 直提交 | p16, p34 |
| SMTP | 简单邮件传输协议（通用标准名词） | 网关监听 25 收作业发通知；Exchange 侧建 'FAX' 地址空间连接器 | p157-164, p183 |
| LDAP | 目录访问协议（通用标准名词） | 目录集成查外部用户（端口 389/Search base/属性映射）；电话簿 LDAP 访问；断连产生 SNMP trap | p135, p138-139, p194-197 |
| DNIS/CSID/ANI/DTMF | 入局路由四法（全称书中未展开，括注为推断） | 被叫号码/主叫传真机标识/主叫号码/双音多频补拨四种来传真路由依据 | p9 |
| NDR | 未投递报告（书内全称 Non-Delivery Report） | 经客户 LAN 中继可接收——邮件服务器投不出通知时回告 | p161 |

## 六、资源与工具域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| FaxCenter\Bin\Util | 命令工具目录 | xmsc -ra/-oa/-aa 服务启停；FirstTimeSetup.exe 事后重跑向导 | p67, p188, p218 |
| Trace folder | 日志目录 | 每组件一个专属日志（ConfigManager.log/Smtp.log 排障高频）；默认 20MB/15 天，满后 zip 入 Archive | p189, p208, p225 |
| ClientRedistribution | 精简客户端包 | 发行介质内只含独立应用（无管理工具）的批量分发安装文件 | p84 |
| TC3048 | ALE 技术通信文档 3048 | OXE-OTFC SIP 互通权威文档（OTFC 侧/OXE 侧/维护三块）；OXE 参数一律以它为准 | p141, p147 |
| OTFC Features List | 特性清单文档 | 端口全表、45 格式、浏览器支持、服务器资源、许可特性的唯一生产数值依据（书内五处以上强调） | p18, p38, p41, p42 |
| SNMP V2 (traps) | 监控上报通道 | 组件状态/队列满/配额满/光栅化失败/路由失败/驱动错误/通道初始化/主机心跳等 trap | p11, p196, p228 |
| Interstar Technologies (registry key) | 注册表备份键 | HKLM\SOFTWARE\Interstar Technologies 随 Data/Config/MySQL 一起备份导出（键名提示 XMedius 血统，推断） | p218, p231 |
