# Rainbow 成员全生命周期管理（开户、密码策略、宽限期、安全）

## R — 原文依据

> "Via the email received, users will customize their password. (At least 12 characters and contain at least 1 uppercase, 1 number, and 1 special character)"（p97）
> "When you delete a user, his or her status becomes 'Suspended' for a period of 10 days (called the 'grace period')"（p103）
> "If you get an error message about the e-mail address you wish to use, please check that it is not already the identifier of a user deleted less than 10 days ago"（p97）

出处：RAINXTE003EN p60-65, p94-105。

## I — 自述

成员=邮箱身份，一人不能属两家公司；生命周期四段：

1. **开户两法（实验主线）**：手动创建（Members、Create，填登录名/密码/可见性，勾发 enrollment 邮件）与邮件邀请（Invitations 页签，可一次邀多人，账户保持 invited 直到接受）
2. **批量两法（讲义级）**：CSV 批量导入（SSO 场景密码字段留空）与 Azure AD 导入/同步（管理员须 Voice Enterprise 级，p96）
3. **密码与安全**：平台级密码策略 12+3 类字符（大写/数字/特殊字符各至少 1）；管理员改密会立即踢掉在线会话（防盗号应急手段）；TOTP 双因子推荐给管理员
4. **删除与恢复**：删除后账号 Suspended 10 天（grace period），可恢复或等永久删除；期内同邮箱不能重建

宽限期行为对照（p97/p103）：

| 时点 | 账号状态 | 恢复/重建后果 |
|---|---|---|
| 删除后 10 天内 | Suspended | 可恢复；同邮箱不能建新用户（报占用错误） |
| 恢复时 | 回落 Essential | 订阅已清空，需重配许可并重挂话机线 |
| 10 天后 | 永久删除 | 邮箱身份释放，可重新开户 |

## A1 — 书中案例

**开户与协作测试实验**（p60-65）：

1. 管理员登录 web.openrainbow.com，进 My company、Members、Create
2. 手动建 user1：填登录名（实验口径）与密码，Sign-in method 保持默认
3. Visibility 保持 same as company（该公司按 private 管理）
4. 勾选发送 enrollment 邮件后保存，到培训邮箱核收（先查 SPAM）
5. 邀请建 user2：Invitations 页签、Invite、输入邮箱、Continue、OK
6. 用户侧点邀请邮件底部的 JOIN 按钮完成注册（不点开头链接）
7. 行为测试三项：用户间互打呼叫、共享屏幕、互发 IM，全部通过

## A2 — 未来触发

使用情境：批量开 Rainbow 账号；删人后邮箱建不了新号；恢复误删用户；密码策略是什么；改密后用户被踢线。

语言信号：建用户 / 邀请 / invitation / CSV / Azure AD / 批量导入 / 删除 / 恢复 / 宽限期 / grace period / 密码策略 / password / suspended / 邮箱占用。

与相邻能力区分：

- 订阅从哪来 → 公司体系与订阅能力
- 绑定话机分机与验证通话 → 分机关联能力（路由卡）
- 收不到验证邮件之外的登录故障 → 维护支持能力（路由卡）

## E — 可执行步骤

输入契约：公司已建且订阅池就位、成员清单（姓名/邮箱/订阅档）、认证方式（密码或 SSO）。邮箱身份有歧义 → 先与客户确认唯一归属。

1. 选开户法：单人用手动或邀请；批量用 CSV 或 Azure AD（核操作者 Voice Enterprise 级）。完成标准：开户路径确定
2. 手动建户：Members、Create，填登录名/密码/可见性/订阅。完成标准：成员出现在列表
3. 邀请建户：Invitations、Invite、输邮箱、确认。完成标准：用户接受后状态从 invited 变正式
4. 密码口径传递：12+3 类字符；SSO 场景 CSV 密码字段留空。完成标准：无弱密码开户
5. 删除操作：确认宽限期影响后执行。完成标准：账号进 Suspended 且工单注明 10 天窗口

判停点：

- 同邮箱报"已占用" → 先查 10 天内是否删过人（宽限期占用），不要反复重试
- 恢复用户后打不了电话 → 预期行为（回落 Essential），重新分订阅并重挂话机线
- 疑似账号被冒用 → 管理员改密强制踢线，再走密码重置
- 生产邮箱网关未放行平台发件地址 → 邀请邮件全数丢失，先协调客户邮件组

输出契约：成员账户清单（含订阅与可见性）+ 宽限期/恢复操作记录 + 安全口径说明。

## B — 边界

- CSV/Azure AD 批量在本书为讲义级（无分步实验）；样本文件与导入报告入口见 p96-98 讲义
- 强制信息频道订阅、企业目录委托属公司管理面（公司体系与订阅能力覆盖）
- 邀请邮件两坑（SPAM、JOIN 按钮）在实验环境尤甚；生产先确认邮件网关放行（n04）
- 实验账号（cCpP 命名法）与培训邮箱、密码等环境值见 book/overview 环境区，均为实验口径，生产一律不用
