# GLOSSARY — Rainbow OmniPCX Enterprise 术语表

> 阶段 3 产出（源：candidates/glossary.md，66 条，六大域；本文件为门户精选版，全量口径见工作区 references.md）。
> 口径：定义只采信本书正文；CSTA/OMS/GD/ITSP/NPD/ESR/TFTP 等缩写书中未给全称，如实标注；p52 "to to"、p24 "perminute" 为原文笔误。

# Rainbow / OmniPCX Enterprise (RAINXTE003EN Ed12) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（314 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Rainbow | Rainbow 云协作平台 | UCaaS（协作/云话音）+ CPaaS（开放 API）双定位，混合云模式集成 OXE/OXO/第三方 PBX | p20-23 |
| Company | 公司（租户单元） | 主功能仅对成员开放的组织单元；分 Reseller/BP 与 End-customer 两级，一人不能属两家公司 | p38-39 |
| Visibility | 公司可见性（四级） | PUBLIC/PRIVATE/CLOSED/ISOLATED 控制与外部互见互邀；教材建议建司即设 CLOSED，不推荐 ISOLATED（无法被外部 bubble 邀请） | p43 |
| SSO | 单点登录（Single Sign-On） | Azure AD-SAML/OIDC、ADFS-SAML 组合；配置管理员须 Enterprise 级；其他标准协议 IdP 须经 ALE 确认 | p44 |
| TOTP | 时间同步一次性口令（Time-based One Time Password） | 需第三方验证器 App 的双因子，全员可用、特别推荐管理员 | p44 |
| RCC | 远程呼叫控制（Remote Call Control） | OXE 分机关联后的基本模式：Rainbow 仅监督话机（接/挂/转），音频全在话机——正常形态非故障 | p109-110, p129 |
| Remote Extension (REX) | 远程延伸 | OXE 特殊终端设备：让 OXE 把呼叫转往外部资源；Rainbow 场景下是"呼叫路由载体"，agent 按用户路由自动改写其内容 | p111-113, p123 |
| Ghost Z | Ghost Z 技术资源 | REX 功能专用的 OXE 内部技术资源：每路并发呼叫占一个、通话结束释放；池大小=REX 并发上限 | p111, p122 |
| Tandem | 主副站成对结构 | 主站=Deskphone、副站=REX；两端必须 multi-line；配置只做主站自动同步副站；Call Routing is not a Forwarding | p112-113, p125 |
| Multi-line | 多线 | 话机/软终端的多线配置：tandem 成员强制前提；同时决定话务台挂起容量（OXE REX 最多 10 路） | p124, p232 |
| Rainbow number | Rainbow 编号 | 分机关联后出现的 17 位技术编号（BBB 开头）；用户选 computer 路由时由 agent 自动写入 REX 的 Remote Extension number | p91, p142 |
| Virtual UA | 虚拟 UA 设备 | DECT-only 用户上 Rainbow 路由的替代：与 DECT+REX 做 multi-devices 并任 tandem 主设备；不能被 RCC 控制 | p139 |
| Integrated Rainbow Agent | 集成 Rainbow 代理 | OXE 内置云连接代理：PBXID+激活码启用；与云间五条链路（WebSocket/XMPP/CSTA/Config/API_MGT） | p67-68, p87 |
| WebRTC Gateway | WebRTC 网关 | 客户 premises 的 Debian VM（OVF 由 ALE 交付）：打通 Rainbow 客户端与 OXE 分机/资源的语音互通；呼叫控制在 PBX | p133-136 |
| Shared/scalable WebRTC Gateway | 共享可扩展网关池 | 多 OXE 共享网关池（推荐按集群推进）：ARS 溢出分流、每 OXE 每网关一条 SIP trunk | p146-150 |
| ARS prefix BBB | BBB 呼出路由前缀 | 网关专用前缀：computer 路由时 agent 写入 REX 的号码以 BBB 开头，经判别器进网关；与标准外呼前缀是两条路 | p137, p142, p184 |
| Callback (translation) | 回拨（翻译表） | 让 PBX 话机用通话记录回拨 Rainbow 分机：CSTA 开关 + 翻译表（DEF 变 BBB）+ 专用实体 | p186-188 |
| Busy Lamp Field (BLF) | 忙灯监督面板 | 4059EE/Rainbow 话务台的用户监督面板：同时呈现 Rainbow 在场与电话状态两列（可不同） | p199, p221-222 |
| Supervision group | 监督组 | Rainbow 侧监督组织：监督员（须 Attendant 订阅）+被监督成员同组；监督员 ≤5 组、每组 ≤30 人 | p226, p230-231 |
| Mutual aid supervision group | 互助监督组 | 动态形态：一键进出、临时纳排成员、锁定最后成员；同时最多监督 4 路；代接仅限同 PBX 电话呼叫 | p233-236 |
| Attendant console (Rainbow) | Rainbow 内嵌话务台 | Web/Desktop 专属（无移动端）：呼叫队列 OXE 10/OXO 8 路 + BLF + 监督组页签 + 呼叫控制 | p225-232 |
| Business Directory | 企业目录 | Azure AD 之外的外部联系人库（含号码），改善来话识别；可委托管理；CSV 批量导入 | p51 |
| Information Channel | 信息频道 | 新闻推送：创建者需 Enterprise 级；强制订阅成员不可退订 | p52 |
| Grace period | 删除宽限期 | 成员删除后 Suspended 10 天可恢复；恢复即回落 Essential、须重配许可与话机线；期内邮箱不可复用 | p97, p103 |

## 二、经销体系角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| BP | ALE 业务伙伴（Business Partner） | 独占两项操作：申报/创建 PBX、开通付费订阅；并激活网关与远程升级 | p38-39, p48, p161 |
| DR / IR | 直接/间接经销商 | 客户集成伙伴的两种合法身份（二选一） | p39 |
| VAD | 增值分销商（Value Added Distributor） | 经销链中间层（书中括注 Grossiste） | p39 |
| EC | 最终客户（End Customer） | 由 Reseller 创建、必须挂靠唯一 BP；管理员无建 PBX/开订阅/激活网关权 | p39, p48-50 |
| BP administrator / Customer administrator | BP 管理员/客户管理员 | BP 管员客户公司+建 PBX+激活网关；客户管理员管自家用户/订阅分配/分机关联；Roles 页签可设多名 | p48-50 |

## 三、订阅计划域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Rainbow Essential | 免费版订阅 | 无限期试用、无 SLA、无电话服务；OXE 场景只有 RCC 且不能改路由 | p24, p109, p129 |
| Rainbow Business | 商务版订阅 | 按用户计费的电话服务最低档；网关与 Teams 集成的门槛之一 | p24, p133, p298 |
| Rainbow Enterprise | 企业版订阅 | Business 全量+多方视频会议+扩展存储+O365/G Suite 集成；SSO/AAD 导入/频道创建的级别门槛所在 | p24, p44, p96 |
| Rainbow Attendant | 话务台订阅 | Rainbow 内嵌话务台专属：排队+监督；与 4059EE 无关；有 Monthly/Prepaid 两种 offer | p24, p200, p239 |
| Enterprise Conference / Conference | 会议类订阅两档 | Enterprise+无限会议分钟（年预付）/ PSTN 会议按分钟按量付费（组织者可为免费用户） | p24 |
| Rainbow Connect | CRM 连接订阅 | 经专用连接器集成 CRM 应用（本书不展开） | p24 |
| Rainbow Room | 会议室订阅 | 按会议室计费、需额外硬件（本书不展开） | p24 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniPCX Enterprise (OXE) | OXE 企业级 PBX | 本书宿主 PBX：内置 Rainbow Agent 接云；网关功能需系统 12.1 MD4/12.2+ | p1, p67, p135 |
| 4059 EE | OXE 传统话务台应用 | 只管话务不管话音：声明为 4059 IP 终端、必须关联物理话机或 IPDSP 且禁 multi-line；支持 Rainbow 集成/BLF | p198-213 |
| IPDSP | IP 桌面软话机（IP Desktop Softphone） | ALE 软话机：实验装于 PC Client（分机 31000/31001）；TFTP 指向 OXE CS 主地址；可作 4059EE 话音承载 | p10, p72, p209, p212 |
| MicroSIP | 第三方软话机 | 实验预装模拟公网/紧急号码（注册 ITSP1 公共网关）；互助组实验中作 PBX 软终端入组 | p10, p14-15, p244 |
| Rainbow Pilot | 连通性与容量评估工具 | pilot.openrainbow.com：现场测连通性 + 按协作/会议/混合/Hub 用法配比评估承载（分区随版本演进） | p32-36 |
| MyPortal | ALE 伙伴门户 | 下载网关 VM（OXE/OXO 目录同一软件）、TC2462、TBE067、升级包；开 SR | p153-154, p174, p255 |
| 网关三服务 | 网关 VM 内三个服务 | otlitemediapillargateway、janus-gateway-mediapillar、kamailio：sudo service status/restart 排障 | p159, p162 |
| OMS | OXE 软件机架实例（全称未展开） | 实验环境唯一需要的机架（Virtual GD4）；网关 IP 域前提中的"压缩资源（GD/OMS）" | p72, p180 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| SIP Trunk Group (T2) | SIP 中继组 | 连网关用 T2 类型、T2 Specification=SIP；ARS 引用 TG 需先建 CDT；回调场景挂专用实体 | p179, p182, p187 |
| CSTA | 计算机电话集成链路（缩写未展开） | agent 五链路之一（4509）；Teams 点拨分机 MakeCall API 的落地路径；回调开关所在页签 | p87, p186, p265 |
| STUN/TURN (GEOIP) | NAT 穿越（默认口径） | TURN_SERVER=GEOIP 为默认；mpcheck 该段依赖 GEOIP 文件，缺失报 FAILED 而非网络故障 | p158, p160 |
| G.711 / G.722 / G.729 | 网关编解码口径 | OXE 侧 Rainbow type 网关仅 G711（实验口径）；DTMF 动态载荷 101 | p181 |
| WebRTC (SIP/RTP) | 网关媒体承载 | Rainbow 客户端与网关间 WebRTC（加密媒体），转成对 OXE 的 SIP/RTP；端口段 WRTRANGE/SIPRANGE 默认 20000-29999/30000-39999 | p133, p158 |

## 六、站点与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| web.openrainbow.com | 网页客户端与管理入口 | 管理配置与使用入口（实验主要操作面） | p61 |
| help.openrainbow.com | Rainbow 支持站点 | 网络要求文章、Features List、Help Desk Guide、MFATOTP 文章的所在 | p24, p27, p44, p246 |
| status.openrainbow.com | 云服务状态页 | 数据中心故障官方信息源；Get updates 订阅告警（按主题/地域过滤，法国勾 WW/EMEA/DE） | p249 |
| RLAB (Remote Lab) | 培训远程实验室 | POD 池相互独立同构 + 公共资源区（NAS/SIP 模拟器/外部 DNS）；每 POD 六实例 | p3-11 |
| ITSP1 | SIP 运营商模拟器 | RLAB 公共区模拟运营商：注册网关+公网网关两条腿；号码规则含 POD 号（ITSP2 未用） | p13-18 |
| mp 命令族 | 网关 VM 管理命令 | mpnetwork/mpconfig/mpshow/mpcheck/mpssh/mpupgrade；登录账号实验口径 | p156-166 |
| OXE 维护命令族 | OXE 侧维护命令 | incvisu/dhs3_init -R/checkCloudConfig.sh -rainbow/sipextgw/lookars/motortrace+traced/multidevice/zdpost/remotesets | p87-88, p191-195 |
| TC2462 / TC2479 | OXE/OXO 技术文档 | Rainbow PBX 集成权威配置指南（远程延伸/共享网关/部署维护/话务台各章指向） | p121, p149, p154, p232 |
| TBE067 | 网关容量估算工具包 | Excel 工具：四输入、通道数、压缩器推算；适用 OXE 101.0 MD3 / WebRTC 3.x 起；单网关 400 并发流上限 | p151 |
| Rainbow Network Requirements | 网络要求文档 | 支持页文章+两份 PDF：端口/域名 IP/带宽/防火墙配置的唯一生产依据 | p26-31 |
