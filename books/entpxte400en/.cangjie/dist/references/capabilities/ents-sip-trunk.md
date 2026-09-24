# 公共 SIP 中继开通与弹性（TG、外部网关、ARS、NPD/DID、双机备份）

## R — 原文依据

> "ARS IS REQUIRED TO USE SIP TRUNK GROUP WITH AN EXTERNAL SIP GATEWAY"（p616）
> "Maximum number of accesses per SIP Trunk Group: 32 (always by pair) … Standard: • Each couple of accesses provides 62 (2x31) channels • 992 simultaneous communications maximum"（p576）
> "The trunk group will inform about the NPD to use for DID transcoding and number's format • The numbering command table will provide the external SIP gateway to use"（p582）

出处：ENTPXTE400EN p572-656。

## I — 自述

去话是固定流水线，来话是翻译回程，弹性靠第二网关：

1. **去话九步链**：拨 ARS 前缀（携带逻辑鉴别符 0-7）；取用户 Entity；Entity 鉴别符选择器映射真实鉴别符（0-255）；真实鉴别符规则按被叫号码匹配 Area+ARS 表+位数；ARS 路由表（≤10 路由，去位/加位+命令表）；中继组；NPD（号码格式）；DID 翻译器（CLI 组装）；外部 SIP 网关（运营商地址/凭证）
2. **来话三步**：SIP INVITE（To=外线号）→ 网关所属中继组的 NPD → 被叫 DID 翻译器映射为内线振铃；回叫翻译器从 INVITE 取 Caller Id 加/删位修饰显示（A=国际/DEF=缺省，全系统 ≤255 个、每个 ≤20 条）
3. **规格**：每 TG 最多 32 接入成对配置；标准型每对 62 通道（满配 992 并发）；Mini SIP 每对 4 通道（64 并发）；UMC 不支持建 Mini SIP
4. **配置顺序红线**：真实鉴别符必须已存在才能在实体选择器关联（三处 Warning）；ARS 是 SIP 中继使用的强制前提（不支持 # 直抓）
5. **编解码两级与逻辑**：系统级 Support perimeter ∩ 网关级开关；系统级不放行则协商静默回落 G711；G722/OPUS 仅 OMS 支持（硬件 IPMG 无）
6. **弹性两案可并存**：ARS 第二路由（命令表 2 指向网关 2，三张 ARS 表各加 Route 2 排第二顺位）；SIP Pool（两网关同 Pool Number 分流量+互备，切换速度由 Supervision timer 决定，例 5 秒）

## A1 — 书中案例

**SIP 中继全链路实验**（p609-640，How-To）：

1. 系统参数：Law=A 律，G722/OPUS 支持范围设 Network and local
2. 建 SIP 中继组：类型 T2、变体 ISDN all countries、T2 Specification=SIP
3. 建外部网关：远端域/端口 5060/UDP、注册账号（实验口径 pbxP/alcatel）、Outbound Proxy 指向模拟器
4. 基础 ARS：前缀 0、命令表、路由（去 1 位加 33）、真实鉴别符与实体选择器
5. 首测：外呼可通但外显不友好；来话回 484 Address Incomplete（未配 DID）
6. 配默认 DID 翻译器与 NPD 后，出入话显示与落地恢复正常
7. 配回叫规则（A33 等）后未接显示可回拨，国际/紧急表各配专用 ARS
8. 巡检：sipextgw -l 显示 IN SERVICE，trkstat 显示 62 通道

**备份与负载均衡实验**（p641-656，How-To）：

1. 建网关 2（同域同账号，Outbound Proxy 指第二腿）
2. 案 1：命令表 2+三张 ARS 表各加 Route 2 为第二顺位
3. 故障注入：把网关 1 的 proxy 改成 .bad 假域名
4. sipextgw -l 显示 1 OOS、2 IN SERVICE，traced 验证来话走网关 2
5. 测完立即改回正确 FQDN（Warning）
6. 案 2：两网关 Pool Number 同值+Supervision timer 5 秒，sippool 观察 L/OOS 切换

## A2 — 未来触发

使用情境：接运营商 SIP 外线；外显号码不对；来话落地 484；未接来电回拨不通；G722 音质没生效；主用网关宕机切换慢；开通国际/紧急呼叫。

语言信号：SIP 中继 / trunk group / 外部网关 / SIP Ext Gateway / ARS / 鉴别符 / discriminator / NPD / DID / 翻译器 / 回叫 / callback / Pool Number / Supervision timer / 484 / G722 / OPUS。

与相邻能力区分：外呼权限控制（谁能打哪类号）见闭锁与紧急能力（路由卡）；T0/T2 传统 ISDN 见传统中继与 UMC 能力（路由卡）；编解码与 OMS 载体见网关上架能力。

## E — 可执行步骤

输入契约：运营商参数包（信令/号段/注册凭证/编解码/紧急要求，按 TC2005 与运营商文档）、号码计划（外线段与内线段映射）。运营商参数不全是判停条件，不全不开通。

1. 系统参数：Law 按地区（欧洲 A 律/美国 μ 律），系统级放行 G722/OPUS。完成标准：系统编解码范围确定
2. 建中继组与网关：TG 类型 T2+SIP 规格；外部网关按运营商参数填域/端口/凭证/代理。完成标准：sipextgw -l 显示 IN SERVICE
3. 建鉴别符与 ARS：真实鉴别符规则（Area+ARS 表+位数）先行，实体选择器再做映射。完成标准：外呼走通
4. 配 NPD/DID：号码格式、默认号源、DID 翻译器（首外号+首内号+范围）双向。完成标准：来话落地、外显正确
5. 配回叫与专项表：回叫翻译器修饰显示；国际/紧急专用 ARS 表与规则。完成标准：国际可打、紧急可拨且显示合规
6. 弹性（如需）：第二网关走 ARS 第二路由或 Pool 互备，Supervision timer 设短。完成标准：故障注入切换成功且配置复原
7. 回归巡检：sipextgw/trkstat/traced 全链路拨测并留档。完成标准：验收单齐

判停点：

- SIP 中继想配 #010 直抓 → 停，SIP 不支持直抓（n27），必须走 ARS 前缀方案
- 实体选择器保存不了 → 真实鉴别符未建（n26），先建规则再做映射，顺序不可倒
- 开了 G722 还是 G711 → 查系统级 Support perimeter（n28），两级开关要同时放行
- 运营商参数与实验值冲突 → 一律按运营商文档与 TC2005（n29），不照抄 ITSP1 口径
- Pool 切换太慢 → Supervision timer 没设短（n30），按业务容忍度调整并复测

输出契约：可打外线的 SIP 中继（来去话+国际+紧急）+ 弹性方案与故障演练记录。

## B — 边界

- ITSP1 模拟器参数（sip.itsp1.fr、pbxP/alcatel、3321PN 号段、紧急回叫规则）全部为实验口径（n29），生产必须按 TC2005 与运营商文档重做
- SBC/安全接入/中继深调与 QoS 不在本书范围（Starter 口径）
- P-Asserted/隐号语义、SDP in 18x、Session Timer 方法等网关参数语义见 p615；与运营商逐项确认
- Mini SIP 规格（每对 4 通道/64 并发）书内为规格口径，UMC 不支持建 Mini SIP（p807）
- Fax over SIP（T.38 等）书中未展开
