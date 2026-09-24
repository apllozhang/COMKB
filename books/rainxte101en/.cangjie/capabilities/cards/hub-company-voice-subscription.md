# Rainbow 公司体系与 Voice 订阅开通（BP/EC、可见性、认证、订阅分配）

## R — 原文依据

> "the following actions can only be performed by the BP: • Declaration & activation of a Cloud PBX • Opening of paid subscriptions • Declaration of terminals • Addition or portability of telephone lines"（p49）
> "This mode is highly recommended, especially in a Rainbow Hub setting."（p53，指 CLOSED）
> "Warning It is MANDATORY to define the time zone of the company because the voicemail and the calendars of the welcome services are based on it."（p73）
> "IN ORDER TO BE ABLE TO DECLARE A CLOUD PBX FOR THE COMPANY, AT LEAST ONE VOICE SUBSCRIPTION IS REQUIRED (VOICE BUSINESS OR VOICE ENTERPRISE)."（p75）

出处：RAINXTE101EN p47-75, p9, p67。

## I — 自述

云侧开户是一切的前提，四件事按序做：

1. **建公司**：BP 账号操作（先搜索查重；一人不能同时属于两家公司）；时区为强制项——留言信箱与欢迎服务日历都基于它
2. **定可见性**：PUBLIC / PRIVATE / CLOSED / ISOLATED 四级——Hub 场景官方力荐 CLOSED（目录搜索只见同事与企业目录）；ISOLATED 不推荐（用户无法被外部组织邀请进 bubble 会议）
3. **定认证**：SSO（Azure AD-SAML/OIDC、ADFS-SAML、Google Workspace-OIDC，配置管理员须 Enterprise 级）或本地密码（≥12 位含 1 大写/1 数字/1 特殊字符）+ TOTP（推荐管理员）
4. **开订阅并分配**：两层流转——BP 先开给公司（月付或预付 1/3/5 年），再由 BP 或本地管理员分给成员；声明 Cloud PBX 前公司必须至少有一条 Voice Business 或 Voice Enterprise 订阅

Voice 订阅四档与扩展档（p9/p67）：

| 订阅 | 定位 | 设备 |
|---|---|---|
| Voice Phone | 仅硬话机/DECT 上的全部话务特性，无 Rainbow 应用 | 硬话机 only |
| Voice Business | 三端话务 + 代接 + 协作；声明 PBX 的最低门槛之一 | PC/手机/话机 |
| Voice Enterprise | Business 全量 + 监督代接 + 视频会议（至 120 与会者/49 路视频） | PC/手机/话机 |
| Voice Attendant | Enterprise 全量 + PC 话务台；不支持硬话机 | PC only |
| Voice Enterprise Dial-In Pack | Enterprise + PSTN 会议本地号码 50+ 国家 | — |
| Rainbow Room | 会议室视频会议专用平台 | 特定 Android TV box |
| Rainbow Alert | 可选告警包：穿透勿扰、持续通知、告警确认 | PC 或手机 |
| CRM Connect | 从 CRM 直接外呼并留存通话历史 | PC only |

与混合云教材（RAINXTE001EN）的命名差异：Hub 侧全部加 Voice 前缀，且多出 Voice Phone 纯话机档。

## A1 — 书中案例

**创建客户公司并开订阅**（p71-75，How-To）：

1. 用 BP 管理员账号登录 web.openrainbow.com（实验口径 bpX.rv1@ale-training.com）。
2. Administration/My Customers/Customer companies → 点 Create。
3. 填 Company name = Client-PX、Country = France、Visibility = Closed（实验口径）。
4. 指定客户管理员 aliceX（该用户收到含激活链接的邮件）。
5. 公司 Information 区补 Size/Activity/Web site/Time zone（Europe/Paris，时区强制）。
6. Subscriptions 区 / Add a new subscription / Voice Enterprise / Monthly / 数量 4 / Subscribe。

验收口径：公司出现在 End customer companies 列表、订阅区显示 4 条 Voice Enterprise Monthly。

## A2 — 未来触发

使用情境：新客户整体上 Rainbow Hub；客户管理员建不了 PBX/开不了订阅；选可见性与认证方式；买哪种订阅组合；免费账号能不能打电话。

语言信号：创建公司 / company / BP / EC / 经销商 / 可见性 / CLOSED / ISOLATED / SSO / TOTP / 订阅 / Voice Business / Voice Enterprise / Voice Attendant / Voice Phone / 预付 / 时区。

与相邻能力区分：建户之后的人员与话务配置 → 成员管理能力；声明 PBX/号码/闭锁 → Cloud PBX 能力；公司级目录与频道属本卡 B 段边界的延伸（ Roles 授权 + Enterprise 门槛）。

## E — 可执行步骤

输入契约：BP 账号（建司/开订阅）、公司命名与归属、认证基础设施现状（有无 Azure AD/ADFS/Google Workspace）、用户数与服务需求。缺 BP 账号 → 找渠道，不要试图用 EC 账号绕过。

1. 查重并创建公司（BP）：搜索栏查名 → Create → 录名称/国家/时区/可见性/联系人。完成标准：公司出现在客户公司列表且时区已设
2. 可见性选型：默认 CLOSED；有明确外部协作诉求才评估 PUBLIC/PRIVATE；ISOLATED 须先确认放弃外部 bubble 邀请的代价
3. 认证选型：有客户 IdP → 规划 SSO（确认操作者持 Enterprise 级，列表外 IdP 须 ALE 确认）；否则密码 + TOTP（管理员强制建议）
4. 开订阅（BP）：Subscriptions / 选 Voice 档与月付或预付 → 定数量 → Subscribe。完成标准：公司订阅池就位且至少一条 Voice Business/Enterprise
5. 分配订阅：Members / 成员 / Services 页签 → 勾选 → Apply（建户时或改户时均可）。完成标准：电话用户均持 Voice 档订阅

判停点：

- 需要建 Cloud PBX/开付费订阅/声明终端/加装电话线而手里只有 EC 管理员 → 停，转 BP（权限设计非故障）
- 公司时区漏配或错配 → 停，先纠正（留言时间戳与欢迎服务开闭时段全依赖它）
- 订阅扣成功但成员无电话 → 查成员订阅分配，不要重复购买

输出契约：可用的公司（可见性/认证/时区已定）+ 公司订阅池 + 成员订阅分配清单。

## B — 边界

- BP 专属四项（p49）与 Reseller 可创建元素五项（p58-59）为互补口径，详见 needs-review nr-03；"点不出入口"不是故障
- SSO/TOTP 的具体配置步骤原书只有指针（支持站点技术手册）；跨 IdP（OKTA/Shibboleth 等）须 ALE 确认（p54）
- 企业目录（外部联系人 CSV/委托管理）与信息频道（Enterprise 级创建、强制订阅不可退订）在本卡边界外仅作提示：配置入口在 Roles 页签（p61-62）
- 订阅细节以 help.openrainbow.com 的 Features List 为准（p8/p67 指针），本书订阅表为 Sprint 170/Ed16 口径
- 培训环境"仅月付禁预付"是实验规则（p17/p68/p74），生产按客户商务选择；实验账号/号段为实验口径（needs-review nr-06）
