# 决策规则速查 — OpenTouch Fax Center - R9.2 Starter (Participant's Guide, Edition 04)

| 能力 | 一句话规则 |
|---|---|
| OTFC 首次交付（宿主准备、安装、FTW、许可） | 四步主线——准备服务器（DNS 正反解/IIS 四角色/Office 预初始化）、Setup 安装（禁 MS SMTP）、FTW 十二项搭最小可用系统、许可去水印解锁 2 通道 |
| OTFC 与 OXE 的 SIP 通道集成（声明、MGR 七步、抓包） | OTFC 侧 UDP 5360 + Dial Plan（单 PBX 全路由/冗余 Peer List）+ OXE 侧 MGR 七步菜单（参数参照 TC3048）+ CHtrace/SIP trace/tcpdump 三法抓包 |
| OTFC 邮件与 Exchange 集成（SMTP 网关、FAX 连接器、通知排障） | SMTP 网关独占 25 端口收作业发通知，Exchange 建 fax:* 地址空间 Send Connector 指向网关智能主机，通知被拦调 Receive Connector |
| OTFC 用户与管理员管理（双用户源、CSV、两级管理员） | 用户恒以 SMTP 地址标识且必须绑 Site+Profile；内部库与 AD 可共存，CSV 仅 Webadmin；System/Site 两级管理员 + 官方推荐备份管理员 |
| OTFC Profile 策略与电话簿（限制组、呼号限制、通知 Profile、LDAP 电话簿） | Profile 六块属性挂五类机制——限制组（出方向挂 Profile）、呼号限制（入方向站点级）、邮件通知 Profile（每语言一份）、公共电话簿与封页经 Profile 下发 |
| OTFC 高级目录集成与来传真路由（LDAP、Lookup、NT 免密、路由表、DTMF、Modification） | LDAP 声明（389/Search base/属性映射）加 Site/Profile Lookup 两表授权外部用户，路由表三类规则（Default 恒最后）、DTMF 补拨、Modification Table 规整号码、8770 计费 |
| OTFC 服务架构与日常运维（有状态/无状态、xmsc、日志） | 模块/服务/组件三层，9 服务分有状态复制与无状态负载均衡；Services Status 查状态、xmsc -ra/-oa/-aa 启停、Trace 目录每组件一个日志（默认 20MB/15 天） |
| OTFC 备份、恢复、升级与删除策略（三数据域、五步升级法、零保留） | 冷备三数据域（Data/Bin/Config + MySQL + Interstar 注册表键），恢复四前提（版本/拓扑/路径/先擦除），升级五步法（数据库不在自动备份内），记录与图像可分开删实现零保留 |
| OTFC 客户端部署与封页定制（四件套、Web Client、GPO、封页五步） | Web Client 免安装六区界面、Windows 四件套（SendFAX/Web Fax Composer/Print to Mail/MMC）、静默+GPO 批量与 ClientRedistribution 精简包、封页 Editor 五步经 Profile 生效 |
| OTFC 方案评估与部署规划（容量协议合规、架构拓扑、支持矩阵） | 单服务器 15000 用户/30 端口、T.38 14.4k 与 G.711 33.8k、五类发送入口四类接收去向、合规卖点三清单、多网关号段分流与支持矩阵核对 |
| OTFC 报表与监控（31 报表、BIRT、SNMP V2 陷阱） | 31 个报表模板（BIRT 自定义装在 3rd\birt）、站点/系统两级监控视图、SNMP V2 trap 清单（队列满/配额满/光栅化失败/路由失败/心跳等） |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
