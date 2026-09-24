# Rainbow 成员全生命周期管理（创建、设置、删除宽限、账号安全）

## R — 原文依据

> "Members can be created: Manually • Creation one by one • By invitation • Via email address ... By bulk import • From .CSV file(UTF-8) • Microsoft Azure Active Directory"（p92）
> "When you delete a user, his or her status becomes 'Suspended' for a period of 10 days (called the 'grace period')"（p99）
> "If the user is logged in at the time you make the password change, he/she will be logged out immediately."（p100）
> "(At least 12 characters and contain at least 1 uppercase, 1 number, and 1 special character)"（p93）

出处：RAINXTE001EN p90-110。

## I — 自述

成员 = 邮箱身份的 Rainbow 账户，四条路径开户：

1. **手动逐个**：Members → Create → 全字段当场配齐（信息最全，适合少量）
2. **邮件邀请**：Invitations 页签点 Invite（可批量填地址），用户收到 noreply@openrainbow 邮件后自助完成开户，管理员再回补号码/订阅等设置
3. **CSV 批量导入**：UTF-8 模板（可下载样例）→ 可建/改/删用户、按 MAC 绑设备、设全局参数 → 导入后看同步报告；SSO 场景密码列留空
4. **Azure AD 同步**：先把 AAD 关联到公司（My Company/Settings，手动操作）→ 建/改/删 + 通讯录搜索；仅 Voice Enterprise 级管理员可用

**成员编辑七分区**（p96）：Information（标识/时区=留言时间戳/可见性/标签）· Permissions · Telephony（设备/分机/公众号码/物理话机）· Programmable keys（可建键组批量套用）· Services（订阅）· Roles（管理权/目录/频道）· Security（改密/改邮箱/改认证）。

**删除规则**：删除 → Suspended 宽限 10 天 → 可恢复或彻底删；恢复后回落 Essential，须重配订阅 + 重挂电话线；宽限期内该邮箱不能用于新建账号。

**密码策略**：≥12 字符 + ≥1 大写 + ≥1 数字 + ≥1 特殊字符（原书口径未单列小写要求）。

## A1 — 书中案例

**手动建户实验**（p102-106）：

1. 管理员登录，核验自身 Enterprise 订阅
2. Members → Create 建 `cCpP.user1@...`（实验口径）
3. 填密码/可见性 same as company/订阅 Enterprise
4. 勾发 enrollment 邮件 → 登实验邮箱收信（查 SPAM、清旧邮件）

**邀请建户实验**（p107-110）：

1. Invitations → Invite `cCpP.user2@...`
2. 用户从邮箱点 Join 完成开户
3. 管理员补配 Enterprise
4. 双账户行为测试：互打 / 共享屏幕 / IM 三项全通过

## A2 — 未来触发

使用情境：批量开户方案选型；用户没收到邮件；删错人怎么救；删除后重建同邮箱报错；改密后用户全掉线；批量改密排期；密码策略是什么。

语言信号：建用户 / members / 邀请 / invitation / CSV / 批量导入 / Azure AD / AAD 同步 / 删除用户 / grace period / 宽限期 / Suspended / 恢复用户 / 改密码 / 密码策略。

与相邻能力区分：给成员配电话（设备/分机）见分机关联（路由卡）；订阅开通在公司侧归公司与订阅能力；成员在 Teams 场景的收敛配置属 Teams 集成能力。

## E — 可执行步骤

输入契约：管理员账号、用户清单（含邮箱）、订阅池余量、认证方式（SSO 与否决定 CSV 密码列）。批量超过数十人 → 优先 CSV/AAD 路径。

1. 选路径：≤10 人手动或邀请；批量 → CSV（一次性迁移）或 AAD 同步（持续同步诉求）。完成标准：路径确定
2. 执行开户：
   - 手动：Members → Create → 全字段（含订阅）。完成标准：成员列表可见
   - 邀请：Invitations → Invite，用户自助完成开户，管理员回补 Telephony/Services。完成标准：用户完成首登
   - CSV：下模板 → 填列 → 导入 → 读同步报告修正错误行。完成标准：报告零错误
   - AAD：关联目录 → 同步。完成标准：AD 侧用户在 Rainbow 可见
3. 七分区核对：尤其 Telephony（设备/分机）与 Services（订阅）——用户"不能打电话"先查这两处。完成标准：电话用户均持 Business/Enterprise/Attendant
4. 销户：删除 → 记录宽限截止日 → 与客户确认恢复/彻底删。完成标准：处置决定留档

判停点：

- 新建账号报邮箱被占用 → 查是否 10 天内刚删除的账号（宽限期内邮箱不可复用），等期满或走恢复
- 误删恢复后用户"没电话了" → 预期行为：恢复即回落 Essential，重新分订阅 + 重挂电话线，不是数据丢失
- 疑似账号冒用 → Security 页立即改密（在线会话即被踢出），这是特性手段；日常批量改密避开工作时间并提前告知
- AAD 导入按钮不存在 → 操作者非 Voice Enterprise 级，先调权限再操作

输出契约：开户/销户完成清单 + 订阅分配记录 + 宽限期台账（如涉删除）。

## B — 边界

- 平台邮件可能进垃圾箱：原书两处重复警告（p106/p108）；生产应建议客户将 openrainbow.com 发件域加白
- 邮箱 = 账号身份且一人不能属两家公司（p47）：跨公司人员归属要先做唯一性决策
- CSV 模板字段与 AAD 属性映射细节以支持站点为准（原书只给样例文件指针）
- 密码复杂度按原书四处一致口径记录（≥12 + 大写/数字/特殊字符）；是否强制小写以平台实际校验为准
