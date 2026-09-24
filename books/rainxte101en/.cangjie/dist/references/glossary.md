# GLOSSARY — Rainbow Hub 术语表

> 阶段 3 产出（源：candidates/glossary.md，全量 70 条，此处门户版精选 52 条，六大域）。
> 口径：定义只采信本书正文；IPEI/CAT-iq/DTMF/MOS/IVR/DECT/SRTP 等缩写书中未给全称，如实标注；原文笔误照录说明（见 needs-review nr-05）。

# Rainbow Hub (RAINXTE101EN Ed16) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（351 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Rainbow Hub | Rainbow 公有云版 | Rainbow 平台的公有云版本：话务全托管云侧 Cloud PBX，纯软话机技术实现"完全上云"，客户侧无 PBX | p5-9 |
| Cloud PBX | 云话务核心 | 软 SIP PBX：连 ALE 与通用 SIP 设备、经一条 trunk 接运营商、管话务特性；一公司有且只有一个 | p78-83, p100-104 |
| Company | 公司（租户单元） | 主功能仅对成员开放；邮箱即身份、一人只属一家公司；建司必填时区（强制） | p48-55, p71-75 |
| Visibility | 公司可见性（四级） | PUBLIC/PRIVATE/CLOSED/ISOLATED；Hub 场景官方力荐 CLOSED（目录搜索只见同事与企业目录） | p53 |
| SSO | 单点登录 | Azure AD(SAML/OIDC)、ADFS-SAML、Google Workspace-OIDC 四种标准组合；配置管理员须 Enterprise 级 | p54 |
| TOTP | 时间同步一次性口令 | 认证方式之一（第三方验证器 App，推荐管理员）；同词另义：设备 debug 会话一次性口令 | p54, p142, p335 |
| RCC | 远程呼叫控制 | 软+硬双端模式下应用对话机的远程监督与控制；Generic SIP 设备明确无 RCC | p112, p117 |
| Zero Touch | 零接触部署 | ALE 终端按 MAC/IPEI 注册关联成员后自动取配置与固件；每用户一台物理 SIP 设备 | p106, p134-139 |
| Generic SIP device | 通用 SIP 设备 | 第三方 SIP 终端（话机/门铃/传真/ATA/DECT base）：全手工、无 RCC、TLS 1.2+SRTP 强制 | p114-123 |
| DID / DDI | 公网直拨号码 | 分配给成员/组/话务台/欢迎服务/IVR 的外线号码；DDI 段=公司公网号段 | p83-84, p95-96 |
| Internal numbering plan | 内线编号计划 | 2-9 位可混长度（1xx/3xx/4xxxx…）；出局前缀 0 或 9（国家相关） | p81, p95, p101 |
| Traffic control (Barring) | 呼出闭锁 | 允许/屏蔽档位 + 管理员白/黑名单（前缀、国际格式不带 + 或 00、全公司或按用户） | p85-87, p97 |
| Personal routines | 个人例行程序 | 一键切换五类参数（在场/主叫 ID/呼叫设备/呼转/退组）；预置 At Work/DND/On Break/Out of office | p173-174 |
| Key groups | 按键组 | 可编程键打包批量下发（话机键+应用键两个分配位）；CSV 建户可两列带组 | p182-187 |
| Business Directory | 企业目录 | 外部公司/组织联系人及号码，提升来话主叫识别；可委托非管理员、CSV 导入 | p61 |
| Information Channels | 信息频道 | 仅 Enterprise 级可创建；强制订阅（公司全员/指定成员）不可退订 | p62 |
| Grace period | 删除宽限期 | 删除后 Suspended 10 天；恢复回落 Essential、须重配订阅与电话线；期内邮箱不可复用 | p168, p176 |
| Hunt group | 呼叫组 | 一号码达多人：Parallel/Serial/Circular 三分发；每组上限 50 人；组建自动生成组 bubble | p210-217 |
| Waiting queue | 等待队列 | 有队列 FCFS（10 秒延迟派最老来话）、溢出 10-900 秒可调；无队列全员占线即溢出 | p215-216 |
| Emergency group | 紧急组 | 打 emergency 标记的标准组（一公司唯一）：激活后免前缀紧急呼叫进组不出局，转警加前缀（0112） | p226-229 |
| Manager/Assistant group | 经理-助理组 | 必然单经理、助理可跨组；只筛电话呼叫；经理 DID 必须配组级 | p218-222 |
| Supervision group | 监督组 | 监督员+被监督成员同组；5 页签/30 人/5 组硬规格；监督员订阅分级 | p223-225 |
| Attendant console | 话务台 | PC 端话务台（须 Voice Attendant）：监督/代接/转移、10 路保持；不能手机端、激活后话机关联被删 | p246, p284-289 |
| Welcome service | 欢迎服务 | 日历+语音提示的组合体：开/闭时段分别路由；可人工强制（forced），下时段回 Auto | p250-261 |
| Automated attendant (IVR) | 自动话务员 | DTMF 自助路由：最多 3 级、根菜单 10 项 0-9、数量无限无许可；唯一提示模式建后不可改 | p265-275 |
| Sites | 站点 | 单 Cloud PBX 下的逻辑分区：挂成员/公网号/服务、站点主号与站点 MoH；内呼/组/目录跨站不变 | p92-93, p301-305 |
| Group bubble | 组协作空间 | 建组自动生成：组内 IM/会议、组留言自动转音频入 bubble、组通话记录查看 | p217 |
| CDR | 话单 | 经 Cloud PBX 的入/出/内部呼叫月度 .csv；纯 VoIP 呼叫不产生；每月 1 日出、BP 三通道获取 | p318 |
| MOS | 话音质量分 | 呼叫结束采集质量票（默认启用）；推荐阈值抖动 <30ms、RTT ≤150ms、丢包 ≤1%（全称书中未展开） | p319, p328 |

## 二、经销体系角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| BP | ALE 业务伙伴（Reseller） | 独占四项：Cloud PBX 声明激活、付费订阅、终端声明、电话线加装/携转；承担 PSTN 与计费 | p49, p58, p65, p229 |
| DR / IR | 直接/间接经销商 | 客户集成伙伴的两种合法身份（二选一），名字显示在 My company/Dashboard | p49 |
| VAD | 增值分销商 | 经销层级最靠近 ALE 的一级（ALE → VAD/DR/IR → EC；书中仅列名） | p49 |
| EC | 最终客户 | 必须挂靠唯一 BP；客户管理员管本公司日常，不能建公司/订阅/PBX/DID/分机 | p49, p59-60 |
| Agent / Administrator | 组内两角色 | Agent 接组来电；Administrator 管组（可只授管理员不接电话，坐席侧显示永久已退组） | p209, p212-214 |

## 三、订阅计划域（p67 订阅总表 8 行）

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Voice Phone | 纯硬话机订阅 | 仅话机/DECT 上的全部话务特性，无 Rainbow 应用；四档中唯一"无软话机"档 | p9, p67 |
| Voice Business | 三端话务入门档 | 话机+应用全部企业话务 + 代接 + 协作；声明 Cloud PBX 的最低门槛之一 | p9, p67, p75 |
| Voice Enterprise | 企业档 | Business 全量 + 监督代接 + 视频会议（至 120 与会者/49 路视频）；AAD 导入的服务级别门槛 | p9, p67, p167 |
| Voice Attendant | 话务台订阅 | Enterprise 全量 + PC 话务台；不支持硬话机（PC only）；attendant group 全员须持 | p9, p67, p246, p249 |
| Voice Enterprise Dial-In Pack | PSTN 会议加购档 | Enterprise + PSTN 会议本地号码 50+ 国家、至 120 与会者 | p67 |
| Rainbow Room | 会议室订阅 | 专用视频会议平台；设备为特定 Android TV box | p67 |
| Rainbow Alert | 可选告警包 | 穿透勿扰、持续视觉通知+声音提示、告警确认；PC 或手机 | p67 |
| CRM Connect | CRM 集成订阅 | 从 CRM 直接外呼并留存通话历史；PC only | p67 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Myriad M3/M5/M7 (+EM200) | Hub 主力话机三档 | zero-touch、彩屏 3.5/2.8/1.6 英寸、M7 独有 BT4.1；EM200 扩展最多 10 页×20 LED 键 | p8-9, p106-108 |
| ALE-2 | 入门级话机 | Entry level/Basic uses；RJ9、PoE class 1；同族 ALE-300/400/500 | p9, p107 |
| DECT 8214 / 8262 | 两型 DECT 手持机 | 8214 办公移动；8262（PTI）恶劣环境/独行工人；按 IPEI 注册（8214 仅欧亚供货） | p148-152 |
| 8328 SIP-DECT | 单/双站基站 | 1-2 站/点、最多 20 手持机、10 路并发；95×93×24mm、10/100 PoE | p148-149 |
| 8368 SIP-DECT | 多站基站 | 最多 254 站、40 机/站、全系统 1000 机；室内/室外 IP55 型；须录主站 IP | p148-151 |
| OmniAccess Stellar | WiFi 移动方案 | 与 DECT 并列的现场移动路线；语音/数据共用基础设施，演进至 WiFi 7 | p153 |
| Rainbow Exporter | 录音归档选件 | 按日全量拷贝录音到 Google Drive 或客户 SFTP；另行付费（pricing on request） | p231 |
| LDAP connector | LDAP 连接器 | 装客户 Windows server（免费）：用户单向同步（仅付费许可）、AD 联系人进目录、Exchange 日历在场 | p178-179 |
| MyPortal | ALE 客户服务门户 | 开 Service Request（两页表单，Product Category=Rainbow Hub） | p342-343 |
| Emily BOT / Global Welcome Center | 支持机器人/伙伴主入口 | SR 入口（与邮件/电话并列）；GWC 为 ALE 国际伙伴主 contact 点 | p341 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| SIP trunk | SIP 中继 | Cloud PBX 到公共运营商的中继：一 PBX 一条；商务模式 bundled/separated | p78, p88, p101 |
| TLS / SRTP | 信令与媒体加密 | 信令 TLS 1.2 起步（TCP 5061）、媒体 SRTP（UDP 30000-44999）；Generic SIP 不支持时可关加密 | p118, p136 |
| OPUS / VP8 / G711 | 编解码 | 客户端音频 Opus 80 kbps、视频 VP8 1.5 Mbps；SIP 设备 G711 64 kbps | p90, p118 |
| DTMF | 双音多频 | IVR 核心交互：每级菜单 0-9 选择路由（另支持 *、#）（缩写未展开） | p251, p266, p269 |
| IPEI | DECT 手持机注册标识 | zero-touch 手持机与设备类型一起录入（对照话机/基站用 MAC）（缩写未展开） | p152, p163 |
| CAT-iq | DECT 告警协议 | 基站与本地告警服务器间通信；已验证 F24、Newvoice（Tamat 进行中）（缩写未展开） | p149-150 |
| PSTN | 公共电话网 | 公网话务经 trunk 由 BP/运营商接入；订购与管理不在 ALE（缩写未展开） | p88, p318 |
| PSAP | 公共安全应答点 | 紧急呼叫定位终点：运营商按 DID 位置数据库路由（书内展开全称） | p229 |

## 六、站点与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| web.openrainbow.com | 管理与使用入口 | BP/客户管理员全流程与成员客户端（含话务台）都在此 | p13, p72, p288 |
| help.openrainbow.com | 支持站点 | Features List、Network Requirements、认证运营商、Help Desk Guide 的所在 | p8, p37, p78, p331 |
| status.openrainbow.com | 云服务状态页 | 数据中心故障官方信息源；Get updates 订阅告警 | p338 |
| Rainbow Pilot | 连通性与承载评估工具 | pilot.openrainbow.com：现场测连通性 + 按用法配比评估承载（分区随版本演进） | p43-44, p136 |
| rdd.openrainbow.com | 零接触管理 URL | DHCP option 43/66/67 无法禁用时的唯一合法指向 | p136 |
| TBE099 / TBE127 | 两份官方文档指针 | TBE099=话音服务/CDR 细节；TBE127=DECT 方案介绍 | p154, p318 |
| RLAB / POD | 培训远程实验室/实验单元 | 每学员一个 POD 号对应一家训练公司；仅作 Boundary 背景（实验口径） | p12-34 |

## 收尾备查

- 全量 70 条见 candidates/glossary.md；本门户版精选 52 条，按使用频率取舍（略去 g31 合并、部分扩展订阅与重复产品行）。
- 仅 passing 提及未单列的词：DND、PoE、ATA gateway、PTI、SBC/VPN、EM20、bubble 泛指义——并入相关词条。
- 同词两义：TOTP（认证 vs 设备 debug 口令）；引用时按上下文区分。
- 混合云语系概念（FTR/UTL/WebRTC 网关/OMC）本书无，勿混入。
