# Rainbow 公司体系与订阅开通（BP/EC、可见性、认证、订阅分配）

## R — 原文依据

> "However, the following actions can only be performed by the BP: • Declaration & PBX • Opening of paid subscriptions"（p48）
> "Get into the habit of systematically setting the 'closed' mode as soon as you create a Rainbow company. This is ideal for the vast majority of customers."（p52）
> "Each member must have a subscription to use telephony services • Business • Enterprise • Attendant"（p65）
> "During LAB Use ONLY Voice MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID!!!"（p66）

出处：RAINXTE001EN p33, p46-68。

## I — 自述

云侧开户是 Rainbow 集成的一切前提，四件事按序做：

1. **建公司**：BP 账号 → 客户公司列表 → Create a client company（先搜索查重；一人不能属两家公司）
2. **定可见性**：PUBLIC / PRIVATE / CLOSED / ISOLATED 四级——拿不准就 CLOSED（教材明示建议）；ISOLATED 不推荐（用户无法被外部会议邀请）
3. **定认证**：SSO（Azure AD-SAML/OIDC、ADFS-SAML，配置管理员须 Enterprise 级）或本地密码（≥12 位含大写/数字/特殊字符）+ TOTP（推荐管理员）
4. **开订阅并分配**：BP 给公司开（月付或预付 1/3/5 年）→ 管理员分给成员；电话服务必须 Business/Enterprise/Attendant

订阅全景 8 种（p33）：

| 订阅 | 定位 | 要点 |
|---|---|---|
| Essential | 免费试用 | 无 SLA、无电话服务；可与付费混用 |
| Business | 个人/团队日常 | 电话服务最低档 |
| Enterprise | Business 全量+ | 多方视频会议、扩展存储、O365/G Suite 集成 |
| Attendant | 话务台专用 | 等待队列 + 监督控制台 |
| Enterprise Conference | Enterprise+无限会议分钟 | 按年预付 12 个月 |
| Conference | PSTN 会议按量计费 | 按分钟/连接付费，组织者可为免费用户 |
| Connect | CRM 集成 | 各兼容 CRM 专用连接器 |
| Room | 会议室 | 按房间订阅，需额外硬件 |

## A1 — 书中案例

**订阅分配**（p104-109）：

1. Members → 选成员 → Services 页签 → 勾 Enterprise → Apply
2. Attendant 订购（p176）：Companies → Subscriptions → ATTENDANT → Attendant Monthly

**实验前置约定**（p83/p102，厂商实验）：公司与 PBX 由讲师（BP 角色）预先创建，学员用客户管理员账号 `cCpP.admin@ale-training.com`（实验口径）登录 web.openrainbow.com 做后续操作——印证"建公司/建 PBX 是 BP 动作、客户管理员从成员层接手"的权责切分。

## A2 — 未来触发

使用情境：新客户上 Rainbow；客户管理员建不了 PBX/开不了订阅；选可见性/认证方式；买哪种订阅；免费版能不能打电话。

语言信号：创建公司 / company / BP / EC / 可见性 / visibility / CLOSED / ISOLATED / SSO / TOTP / 订阅 / subscription / Essential / Business / Enterprise / Attendant / 预付 / prepaid。

与相邻能力区分：建户之后的人员管理归成员生命周期；公司级目录与频道见管理员工具（路由卡）；PBX 接入属 PBX 接入能力。

## E — 可执行步骤

输入契约：BP 账号（建司/开订阅）、公司命名与归属、认证基础设施现状（有无 Azure AD/ADFS）、用户数与服务需求。缺 BP 账号 → 找渠道，不要试图用 EC 账号绕过。

1. 查重并创建公司（BP）：搜名字 → Create a client company → 录必填信息（名称/国家/时区/地址/可见性/联系人）。完成标准：公司出现在客户公司列表
2. 可见性选型：默认 CLOSED；客户有明确外部协作诉求才评估 PUBLIC/PRIVATE；ISOLATED 须先确认放弃外部 bubble 邀请的代价
3. 认证选型：有 Azure AD/ADFS → 规划 SSO（确认操作者持 Enterprise）；否则密码 + TOTP（管理员强制建议）
4. 开订阅（BP）：Companies → Subscriptions → 选类型与月付/预付 → 定数量 → Subscribe。完成标准：公司订阅池就位
5. 分配订阅：Members → 成员 → Services 页签 → 勾选 → Apply。完成标准：电话用户均持 Business/Enterprise/Attendant

判停点：

- 需要建 PBX 或开付费订阅而手里只有 EC 管理员 → 停，转 BP（权限设计非故障）
- 客户坚持 ISOLATED 又要参加外部会议 → 停，二者不可兼得，升级商务决策
- 订阅扣成功但成员无电话 → 查分配（第二步），不要重复购买

输出契约：可用的公司（可见性/认证已定）+ 公司订阅池 + 成员订阅分配清单。

## B — 边界

- BP 专属权限仅两项（申报建 PBX、开付费订阅）——这是渠道体系设计，不是故障（p48）
- 原书未展开 SSO 的具体配置步骤（只有指针到支持站点）；跨 IdP（OKTA/Shibboleth 等）须经 ALE 确认（p53 NB）
- 公司创建的完整实验在书中缺位（实验中由讲师代做）——步骤 1 为讲义口径
- 培训禁用预付是实验口径（p66/p176），生产按客户商务选择
- 订阅细节以 help.openrainbow.com 的 Features List 为准（p33/p65 指针），本书订阅表为 Ed13 口径
