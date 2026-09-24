# Rainbow 公司体系与订阅开通（BP/EC、可见性、认证、订阅分配、管理员权责）

## R — 原文依据

> "However, the following actions can only be performed by the BP: • Declaration & PBX • Opening of paid subscriptions"（p39）
> "Get into the habit of systematically setting the 'closed' mode as soon as you create a Rainbow company."（p43）
> "Each member must have a subscription to use telephony services • Business • Enterprise • Attendant"（p56）
> "During LAB Use ONLY Voice MONTHLY subscriptions per company. DO NOT USE YEAR PREPAID!!!"（p57）

出处：RAINXTE003EN p24, p37-59。

## I — 自述

云侧开户是 Rainbow 集成的一切前提，四件事按序做：

1. **建公司**：BP 账号创建 EC 公司（建司前先搜索查重；成员=邮箱身份，一人不能属两家公司）
2. **定可见性**：PUBLIC / PRIVATE / CLOSED / ISOLATED 四级——拿不准就 CLOSED（教材明示建议）；ISOLATED 不推荐（用户无法被外部会议邀请）
3. **定认证与权责**：SSO（Azure AD-SAML/OIDC、ADFS-SAML，配置管理员须 Enterprise 级）或本地密码（12+3 类字符）+ TOTP（推荐管理员）；Roles 页签可设多名管理员
4. **开订阅并分配**：BP 给公司开（月付或预付 1/3/5 年），管理员分给成员；电话服务必须 Business/Enterprise/Attendant

订阅全景 8 种（p24）：

| 订阅 | 定位 | 要点 |
|---|---|---|
| Essential | 免费试用 | 无 SLA、无电话服务；可与付费混用 |
| Business | 个人/团队日常 | 电话服务最低档 |
| Enterprise | Business 全量+ | 多方视频会议、扩展存储、O365/G Suite 集成 |
| Attendant | 话务台专用 | 等待队列 + 监督控制台；与 4059EE 无关 |
| Enterprise Conference | Enterprise+无限会议分钟 | 按年预付 12 个月 |
| Conference | PSTN 会议按量计费 | 按分钟/连接付费，组织者可为免费用户 |
| Connect | CRM 集成 | 各兼容 CRM 专用连接器 |
| Room | 会议室 | 按房间订阅，需额外硬件 |

两个管理面：企业目录（外部联系人+号码，改善来话识别，CSV 可导）；信息频道（仅 Enterprise 级可建，成员强制订阅、不可退订）。

## A1 — 书中案例

**实验前置约定**（p60-65，厂商实验）：

1. 公司与 PBX 由讲师（BP 角色）预先创建，学员用培训管理员账号登录 web.openrainbow.com（实验口径）
2. 手动建成员：My company、Members、Create，填登录名与密码，订阅暂留默认 Essential
3. 勾选发送 enrollment 邮件；到培训邮箱核收，先翻 SPAM 防漏信（实验口径）
4. 邀请建成员：Members、Invitations 页签、Invite、输入邮箱、Continue
5. 用户侧完成开户：点邮件底部的 JOIN 按钮（不是开头链接），设密码与必填信息
6. 行为测试三项：两个 Rainbow 用户互打呼叫、一方共享屏幕、两用户互发 IM，全部通过

## A2 — 未来触发

使用情境：新客户上 Rainbow；客户管理员建不了 PBX/开不了订阅；选可见性或认证方式；买哪种订阅；外部联系人怎么进目录。

语言信号：创建公司 / company / BP / EC / 可见性 / visibility / CLOSED / ISOLATED / SSO / TOTP / 订阅 / subscription / Essential / Business / Enterprise / Attendant / 预付 / prepaid / 企业目录 / 信息频道。

与相邻能力区分：

- 建户之后的人员管理 → 成员生命周期能力
- PBX 侧接入 → OXE 接入能力
- 公司可见后的人员组织与监督 → 两套话务台能力（路由卡）

## E — 可执行步骤

输入契约：BP 账号（建司/开订阅）、公司命名与归属、认证基础设施现状（有无 Azure AD/ADFS）、用户数与服务需求。缺 BP 账号 → 找渠道，不要试图用 EC 账号绕过。

1. 查重并创建公司（BP）：搜名字防重复，创建 EC 公司并录必填信息。完成标准：公司出现在客户公司列表
2. 可见性选型：默认 CLOSED；有明确外部协作诉求才评估 PUBLIC/PRIVATE。完成标准：可见性写入公司设置
3. 认证选型：有 Azure AD/ADFS 规划 SSO（操作者须 Enterprise 级）；否则密码+TOTP。完成标准：认证方式确定且操作者级别达标
4. 开订阅（BP）：公司订阅区选类型与计费周期、定数量、Subscribe。完成标准：公司订阅池就位
5. 分配订阅：Members 选成员、Services 页签勾选、Apply。完成标准：电话用户均持 Business/Enterprise/Attendant

判停点：

- 需要建 PBX 或开付费订阅而手里只有 EC 管理员 → 停，转 BP（权限设计非故障）
- 客户坚持 ISOLATED 又要参加外部会议 → 停，二者不可兼得，升级商务决策
- 订阅扣成功但成员无电话 → 查分配步骤，不要重复购买
- 要给全员推信息频道 → 先确认内容长期可维护（强制订阅不可退订）

输出契约：可用的公司（可见性/认证已定）+ 公司订阅池 + 成员订阅分配清单。

## B — 边界

- BP 专属权限仅两项（申报建 PBX、开付费订阅），加上网关激活与远程升级也归 BP——这是渠道体系设计，不是故障（p39/p48/p161）
- 原书未展开 SSO 的具体配置步骤（只有指针到支持站点）；跨 IdP（OKTA/Shibboleth 等）须经 ALE 确认（p44 NB）
- 公司创建的完整实验在书中缺位（实验中由讲师代做）——步骤 1 为讲义口径
- 培训禁用预付是实验口径（p57/p239），生产按客户商务选择
- 订阅细节以 help.openrainbow.com 的 Features List 为准（p24/p48 指针），本卡订阅表为 Ed12/R101.1 口径
- 实验账号、培训邮箱与密码等环境值仅作实验参考（见 book/overview 环境区），生产一律替换
