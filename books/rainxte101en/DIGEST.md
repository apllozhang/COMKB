# DIGEST — Rainbow Hub 纯云话音精华长文

> 源：RAINXTE101EN Edition 16（Sprint 170，351 页）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 Rainbow Hub 纯云交付的全局认知；操作细节按需查 12 张能力卡。

## 一、这套东西是什么

Rainbow Hub 是 Rainbow 平台的公有云版本：话务核心整个搬到云侧的 **Cloud PBX**，客户现场不部署任何 PBX、SBC，也不需要 VPN——远程与移动工作者用软话机，固定工位用直连云的 SIP 话机或 DECT（p5-7）。

它与另一条产品线"Rainbow 混合云"（连客户已有 OXO/OXE）并列，选型第一步是分清客户走哪条线。本教材只讲 Hub 线。与混合云教材（RAINXTE001EN）的四个显式差异：

| 差异点 | Hub（本书） | 混合云（RAINXTE001EN） |
|---|---|---|
| 话务核心 | 云侧 Cloud PBX（纯软 SIP PBX） | 客户侧 OXO/OXE + WebRTC 网关 |
| 订阅命名 | Voice Phone/Business/Enterprise/Attendant 四档 | Business/Enterprise/Attendant 三档 |
| BP 专属 | 四项（PBX 声明/付费订阅/终端声明/电话线） | 两项（PBX 声明/付费订阅） |
| 终端供给 | zero-touch + DECT + Generic SIP 三线 | PBX 侧终端/虚拟终端 |

整本教材就是一条交付主线：**云侧开户（公司/订阅/Cloud PBX/号码）、端侧供给（zero-touch 设备/成员）、话务能力域（组/话务台/欢迎服务/IVR/多站点）、运营（分析/维护）**，对应 p51 的"公司搭建七步"。

## 二、云侧开户三件套

- **公司（Company）**：BP 建客户公司（查重先行；一人不能属两家公司）；时区强制——留言信箱与欢迎服务日历全基于它（p73）。可见性四级拿不准就 CLOSED（Hub 场景官方力荐，目录搜索不出全社区）；ISOLATED 别乱用——用户无法被外部组织邀请进 bubble 会议。
- **认证**：SSO 四种标准组合（Azure AD-SAML/OIDC、ADFS-SAML、Google Workspace-OIDC，操作者须 Enterprise 级）或本地密码（≥12 位含大写/数字/特殊字符）+ TOTP（推荐管理员）。
- **订阅**：Voice 四档是电话服务的硬门槛——成员必须持 Voice 档订阅才能配号码（无物理话机也可以是纯软话机用户）。声明 Cloud PBX 前公司必须至少有一条 Voice Business 或 Voice Enterprise 订阅，否则建通信服务器界面里根本选不到 Cloud PBX（p75/p80）。

Voice 订阅四档（p9/p67）：

| 订阅 | 定位 | 设备 |
|---|---|---|
| Voice Phone | 仅硬话机/DECT 话务，无 Rainbow 应用 | 硬话机 only |
| Voice Business | 三端话务 + 代接 + 协作 | PC/手机/话机 |
| Voice Enterprise | Business 全量 + 监督代接 + 视频会议（120 人/49 路） | PC/手机/话机 |
| Voice Attendant | Enterprise 全量 + PC 话务台 | PC only |

## 三、Cloud PBX：全书核心对象

三条拓扑硬约束：**一公司有且只有一个 Cloud PBX；一个 Cloud PBX 只挂一条外部 SIP trunk；通道与线数无上限**（p78）。多站点也不开第二台——站点只是单 PBX 下的逻辑分区。

配置要点：

| 项 | 口径 |
|---|---|
| 内线编号 | 2-9 位、可多长度混存（1xx/3xx/4xxxx…） |
| 出局前缀 | 0 或 9（国家相关）；"优化拨叫"免前缀也国家相关 |
| 公网号码 | 分配给成员/组/话务台/欢迎服务/IVR；首个注入号默认当公司主号 |
| 闭锁 | 档位三级 + 白/黑名单（前缀按国际格式、不带 + 或 00） |
| trunk 商务 | bundled（一单一发票）或 separated（两单两票）；PSTN 不归 ALE 管 |

带宽四行口径（p90，完整要求以官方 PDF 为准）：Rainbow 客户端音频 Opus 80 kbps、视频 VP8 1.5 Mbps（720p/30）、SIP 设备音频 G711 64 kbps、信令可忽略——核算位置在客户 premises 到 SIP trunk 段。

## 四、端侧供给：zero-touch 是主角

ALE 原生终端（Myriad 话机、DECT）按 MAC/IPEI 在管理端注册并关联成员后，自动从云取配置与固件（约 5-10 分钟，可能多次重启，屏上绿点即验收）。三条技术红线（p136-137）：

1. DHCP option 43/66/67 会覆盖 zero-touch 指向——必须禁用，禁不掉则下发的管理 URL 必须指向 rdd.openrainbow.com
2. LAN 里有旧 PBX 做 TFTP 会抢先，设备起不了 Cloud 模式
3. 禁止用设备自带 web 管理页做配置；未关联用户的设备报 Config Failed

配套口径：每用户仅一台物理 SIP 设备；防火墙放行 TCP 5061/443、UDP 30000-44999/53/123、TCP 22（p136）；已注册话机禁直连，取日志走 15 分钟 debug 会话（一次性口令）；第三方 Generic SIP 只做补充——全手工、无 RCC、无统一在场、ALE 不为大规模部署兜底。

DECT 两档（p148-150）：

| 维度 | 8328 | 8368 |
|---|---|---|
| 基站 | 1-2 站/点 | 最多 254 站 |
| 手持机 | 最多 20 台 | 40 台/站，全系统 1000 台 |
| 并发 | 10 路 | 10 路/站 |
| 场景 | 办公室/门店/车间小安装 | 大覆盖无缝切换 |

## 五、话务能力域一表流

| 能力 | 关键口径 |
|---|---|
| Hunt group | 组 50 人；Parallel/Serial/Circular；轮转 10 秒；无队列占线即溢出（图示默认 60 秒）、有队列 FCFS 溢出 10-900 秒可调 |
| 组角色 | Agent 接来电；Administrator 管组（可只授管理员）；建组自动生成组 bubble（留言/通话记录在里面） |
| 经理助理 | 必然单经理；只筛电话呼叫；经理 DID 必须挂组级；溢出提示音 5-30 秒 |
| 话务台 | Voice Attendant 解锁（10 路排队）；监督组 5 页签/30 人/5 组；用户锁定 PC——无话机、无移动端 |
| 紧急组 | 一公司唯一；激活后免前缀紧急呼叫进组不出局；组员转警加前缀（0112）；定位归 BP/运营商 |
| 录音 | 触发三层；存 2 个月；仅最终客户管理员可见；超期归档走付费 Rainbow Exporter |
| 欢迎服务 | 日历+提示音（≤4MB/120 秒/定制 5 条/特殊日 10 天）；开闭双路由；强制开闭下时段回 Auto；假日不预填 |
| IVR | 最多 3 级、每级 0-9、无限量无许可；DDI 直挂即 7×24，经欢迎服务进则受日历控制；唯一提示模式建后不可改 |
| 多站点 | 站点挂成员/号码/服务；站点主号与站点 MoH；内呼/组/目录跨站不变；副站主叫权限要收紧 |
| 成员 | 五通道开户（手动/邀请/CSV/AAD/LDAP）；删除 10 天宽限——恢复回落 Essential 须重配；改密立即踢在线会话 |

## 六、运营三视角与维护闭环

- **CDR（计费用）**：经 Cloud PBX 的入/出/内部呼叫月度 .csv，每月 1 日出；纯 Rainbow VoIP 呼叫不产生；BP 经邮件/网页/REST API 三通道取；ALE 不计费不开票（p318）。
- **仪表盘（行为用）**：全局 7/30 天可导 CSV；Voice 页周期最长 1 年；欢迎服务统计与组对比一次最多 5 个；成员级统计可按组关闭（劳动合规）。
- **MOS（排障用）**：呼叫结束自动采质量票；阈值抖动 <30ms、RTT ≤150ms、丢包 ≤1%（p328）。
- **维护八抓手**：用户日志（About Rainbow → Save logs）、设备监督（15 分钟 debug 窗）、连通性核查（ALE SIP 终端不支持 HTTP 代理）、用户上报（集成商同视角）、status.openrainbow.com、计划维护预告、Help Desk 指南、MyPortal 开 SR——SR 只为**认证 Rainbow Hub** 的伙伴创建（p341；混合云教材口径是 "certified on Rainbow"，认证科目按产品线区分）。

三条交付红线：

1. 教材全部账号/密码/号段/网段是实验值（培训还禁预付），上生产必须换
2. 端口/带宽全集、trunk 合同、DID 紧急定位登记在书外（Network Requirements 文章、BP/运营商侧）
3. 编号计划设计方法论、话务建模、提示音制作原书不讲——按客户实情设计

## 七、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 建 Hub 公司/开 Voice 订阅/认证 | hub-company-voice-subscription |
| 声明 Cloud PBX/号码/闭锁/trunk | hub-cloud-pbx-provisioning |
| 开户/批量导入/例行程序/宽限 | hub-member-telephony |
| 话机/DECT zero-touch 部署 | hub-zero-touch-provisioning |
| 设备日志/Generic SIP 评估 | hub-device-maintenance |
| 呼叫组/队列/紧急组/录音 | hub-hunt-groups |
| 话务台/监督组 | hub-attendant-supervision |
| 欢迎服务/IVR/MoH | hub-welcome-service-ivr |
| 网络/Pilot/分析/维护 SR | 路由入口（rainbow-hub-router） |

## 版权

- 本精华长文为 ALE Training Services《Rainbow Hub》（RAINXTE101EN Edition 16）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
