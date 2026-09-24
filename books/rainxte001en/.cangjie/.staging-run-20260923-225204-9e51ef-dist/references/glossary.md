# GLOSSARY — Rainbow OXO Connect 术语表

> 阶段 3 产出（源：candidates/glossary.md，62 条，六大域）。
> 口径：定义只采信本书正文；UTL/OMC/FTR/DDI/ARS/CSTA/REX/ESR 等缩写书中未给全称，如实标注；p34 "tou"、p33 "0365" 为原文笔误。

# Rainbow OXO Connect (RAINXTE001EN Ed13) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（251 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Rainbow | Rainbow 云协作平台 | UCaaS（协作/云话音）+ CPaaS（开放 API）双定位，混合云模式集成 OXO/OXE/第三方 PBX | p29-31 |
| Company | 公司（租户单元） | 主功能仅对成员开放的组织单元；分 Reseller/BP 公司与 End-customer 公司两级，一人不能属两家公司 | p47-48, p54 |
| Visibility | 公司可见性（四级） | PUBLIC/PRIVATE/CLOSED/ISOLATED 控制与外部互见互邀；教材建议默认 CLOSED，不推荐 ISOLATED（无法被外部 bubble 邀请） | p52 |
| SSO | 单点登录（Single Sign-On） | Azure AD-SAML/OIDC、ADFS-SAML 三种标准组合；配置管理员须 Enterprise 级；可按用户混配多种方式 | p53 |
| TOTP | 时间同步一次性口令（Time-based One Time Password） | 需第三方验证器 App 的双因子，全员可用、特别推荐管理员 | p53 |
| RCC | 远程呼叫控制（Remote Call Control） | PBX 接入但无网关时的模式：Rainbow 仅监督话机（接/挂/转），音频全在话机——正常形态非故障 | p6, p110-116 |
| WebRTC Gateway | WebRTC 网关 | Rainbow 客户端与 PBX 生态间的语音互操作网关，只建音频媒体关系（HTTPS/SRTP 加密）；呼叫控制在 PBX | p118-126 |
| Free Rainbow in Twinset | Twinset 虚拟副站 | R6.0 起的 Multiset 副站终端类型（UTL Bypass 省许可）；R5.2 及以前该位置用 Anydevice | p123, p155-157 |
| Anydevice | 纯软话机终端 | 无物理分机、全程经 Rainbow 应用；占 1 UTL；话务台多线资源 ≤8 路（最低 R6） | p123, p155-158, p169 |
| Supervision group | 监督组 | 话务台监督单元：监督员（须 Attendant）+被监督成员同组；每监督员 ≤5 组、每组 ≤30 人 | p164-168 |
| Mutual aid supervision group | 互助监督组 | Type=Mutual aid group 的动态组：一键进出、临时纳排成员、锁定成员不可退；代接仅限 PBX 电话呼叫 | p170-173, p180-181 |
| Attendant console | 话务台 | Web/Desktop 专属（无移动端）：呼叫队列（OXE 10/OXO 8 路）+呼叫控制+BLF 监督+组页签 | p162-166 |
| Rainbow number | Rainbow 编号 | 分机关联后生成的编号（如 BBB10070254106463346）；用户选 computer 路由时由 agent 自动写入 Remote Extension number | p115, p233 |
| PBXID & Activation code | PBX 标识与激活码 | Rainbow 平台生成的接入双凭证（非设备序列号）；FTR 默认占位 FleetRef-Installref 须替换 | p83-86, p134 |
| UTL | 通用电话许可（全称书中未展开） | 计量单位：Deskphone+Twinset 副站=1 UTL、Anydevice=1 UTL；Twinset 的意义即 UTL Bypass | p123, p156 |
| FTR | 首次开箱流程（全称书中未展开） | 全新 IPBox 首连流程：定密码/产品类型（如 Frontend WebRTC）/客户参考与 IP；FE 免费许可由 FTR 自动提供 | p128-131, p134 |
| Business Directory | 企业目录 | 存外部联系人及号码（提升来电识别）；可委托非管理员；支持 CSV 批量导入 | p60 |
| Information Channels | 信息频道 | 类新闻源；仅 Enterprise 级可创建；强制订阅成员不可退订 | p61 |
| Grace period | 删除宽限期 | 删除后 Suspended 10 天可恢复；恢复即回落 Essential、须重配许可与电话线；期内邮箱不可复用 | p93, p99 |

## 二、经销体系角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| BP | ALE 业务伙伴（Business Partner） | 独占两项操作：申报/创建 PBX、开通付费订阅；并激活 WebRTC 网关（Reseller administrator 同义） | p48, p57, p121 |
| DR | 直接经销商（Direct Reseller） | EC 客户集成伙伴两种合法身份之一 | p48 |
| IR | 间接经销商（Indirect Reseller） | EC 客户集成伙伴的另一种合法身份 | p48 |
| VAD | 增值分销商（Value Added Distributor） | 经销层级最靠近 ALE 的一级（书中仅列名） | p48 |
| EC | 最终客户（End Customer） | 必须挂靠唯一 BP；EC 管理员管成员/公司信息/分订阅/关联话机，无 PBX 建立与付费订阅开通权 | p48, p58 |

## 三、订阅计划域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Rainbow Essential | 免费版订阅 | 无限期试用、无 SLA、无电话服务；删除恢复后的回落态 | p33, p65, p99 |
| Rainbow Business | 商务版订阅 | 按用户计费的电话服务最低档；WebRTC/Teams 用户前提之一 | p33, p65, p142, p208 |
| Rainbow Enterprise | 企业版订阅 | Business 全量+多方视频会议+扩展存储+Office 工具集成；SSO/频道创建/AAD 导入的服务级别门槛所在 | p33, p53, p61, p92 |
| Rainbow Attendant | 话务台订阅 | Hybrid 用户话务台专属：排队调度+监督代接；实验按 Attendant Monthly 开通 | p33, p164, p176 |
| Enterprise Conference / Conference | 会议类订阅两档 | Enterprise+无限会议分钟（年预付）/ PSTN 会议按分钟按量付费（组织者可为免费用户） | p33 |
| Rainbow Connect | CRM 连接订阅 | 经专用连接器集成 CRM 应用（本书无细节） | p33 |
| Rainbow Room | 会议室订阅 | 按会议室计费、需额外音视频硬件（本书无部署细节） | p33 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OXO Connect（Power CPU EE） | OXO Connect 通信服务器 | 本书宿主 PBX；Power CPU EE 形态不支持集成 GW 与 FE GW，仅外部 NUC（50 通话） | p29, p118, p129 |
| OCE（IPBox） | OXO Connect Evolution | R3.2 起集成 WebRTC 网关的形态（免 SIP trunk 许可 bypass；集成 GW 上限 20）；缩写 OXO CE | p118, p125-129 |
| OCE Front End | OCE 前端网关 | 标准 OCE 硬件专职 WebRTC 网关（无 PBX 能力/无 UTL/无需 OMC）；双端 ≥R4.0 MD；上限 20 通话 | p127-137 |
| NUC | 迷你 PC（Next Unit of Computing） | 外部网关承载硬件之一（ISO 安装，上限 50 通话）；与 ESXi VM 同级 | p143-145, p147 |
| OMC | OXO 管理工具（全称书中未展开） | OXO 侧几乎一切操作的管理客户端（首连/IP/接入/终端/核验）；FE 供应不需要它 | p69-82, p86, p129 |
| Webdiag | OXO 内置诊断工具 | 查 Rainbow Status（connected with final password 判据）、系统日志、FE CPU 状态 | p88, p132 |
| Cloud Connect（RB WebAdmin/Fleet Dashboard） | ALE 云侧设备管理服务 | OCE-FE 设备管理与软件升级；Fleet Dashboard 识别 PABX/OCE-FE 并一键跳对端 | p125-136 |
| ccrbagent.log | Rainbow 代理日志 | OXO 上 Rainbow agent 的日志文件名（Webdiag → System → Log files 获取） | p88 |
| TURN | TURN 服务器（书中未展开） | 外部网关配置项：按站点位置配置（取值规则在书外） | p141 |
| Emily BOT | 支持机器人 | Rainbow 支持入口之一（与邮箱/Welcome Center/电话并列） | p191 |
| MicroSIP / IPDSP | 实验软话机两类 | 预装第三方软话机（100-103+公网模拟）/ ALE IP 桌面软话机（104，主用）——教学基础设施 | p16, p113 |
| ITSP1 | SIP 运营商模拟器 | RLAB 公共区模拟运营商（gateway1.itsp1.com/public.itsp1.com；号码规则含 POD 号 PN） | p21-26 |
| OXE | OmniPCX Enterprise | ALE 企业级 PBX（对照系）：话务队列 10 路、REX 10 路、配置文档 TC2462 | p29, p164, p169 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| HTTPS / SRTP | 信令与媒体加密 | 网关到 Rainbow 的互联网通信全程 HTTPS（信令）+SRTP（媒体），全拓扑适用 | p126 |
| SIP Trunk | SIP 中继 | PBX 到运营商/对端的中继；集成 GW 拓扑免 SIP trunk 许可（bypass），R3.2 前外部方案需要 | p22, p26, p125 |
| PSTN | 公共电话网 | 云话音出口/Conference 计费对象/Teams 架构中的公网侧（缩写未展开） | p31, p33, p197 |
| DDI | 直拨号码（缩写未展开） | 外线直拨内部分机的号码；Rainbow 关联时的 Public number 字段填它 | p25-26, p115 |
| ARS | 呼出路由选择表（缩写未展开） | 网关自动配置的自动化项之一（路由 Rainbow 呼叫）；编号计划与闭锁仍归安装员 | p121, p150 |
| CSTA | 计算机电话集成接口（缩写未展开） | Teams 内呼 PBX 分机的 MakeCall API 落地路径 | p202 |
| DTMF | 双音多频（缩写未展开） | Teams 集成通话中一键发送 DTMF（IVR 按键）能力 | p204 |

## 六、站点与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| web.openrainbow.com / openrainbow.com | 网页客户端与平台默认域名 | 管理与使用入口；OMC 接入域名字段保持默认不改 | p84-86, p103 |
| help.openrainbow.com | Rainbow 支持站点 | 网络要求文章、Features List、Help Desk Guide 的所在 | p34, p36, p57, p65, p183 |
| status.openrainbow.com | 云服务状态页 | 数据中心故障官方信息源；Get updates 订阅告警（按主题/地域过滤） | p186 |
| Rainbow Pilot | 连通性与容量评估工具 | pilot.openrainbow.com：现场测连通性 + 按用法配比评估承载（分区随版本演进） | p41-44 |
| MyPortal | ALE 客户服务门户 | 下载网关 VM/查 WebRTC cookbook/开 SR（认证伙伴前提） | p135-144, p190-193 |
| developers.openrainbow.com | CPaaS 开发者门户 | Rainbow 开放 API/SDK 入口（仅 p30 引用） | p30 |
| TC2479 / TC2462 | OXO/OXE 技术文档 | Rainbow WebRTC Gateway 权威配置文档（OXE 为 TC2462） | p123, p169 |
| Rainbow WebRTC cookbook | WebRTC 网关落地手册 | MyPortal 最新版；OCE-FE 各 commissioning 场景"必须遵循" | p135, p137 |
| Rainbow Network Requirements | 网络要求文档 | 支持页文章+两份 PDF：端口/域名 IP/带宽/防火墙配置的唯一生产依据 | p35-40 |
| RLAB / POD | 培训远程实验室/实验单元 | POD 间独立同构，共享 NAS 与 SIP 模拟器；实验网段 192.168.1.x | p9-19 |
