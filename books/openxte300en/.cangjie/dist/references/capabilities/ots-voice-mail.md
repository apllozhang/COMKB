# 语音邮箱、IMAP 收取与通知公告（Local Storage 全链）

## R — 原文依据

> "Voice messages are stored in a directory structure, in wav format, on OpenTouch server Messages are stored in an uncompressed format Readable from any IMAP client"（p304）
> "Before validating the mailbox creation, it's mandatory to assign a profile to the voice mailbox, in the « configuration » tab."（p330）
> "Up to 1 000 simultaneous sessions (with embedded IMAP server) For 1 001 up to 20 000 simultaneous sessions, a dedicated server is required"（p313）
> "Notifications are sent through an external SMTP server. There is no SMTP server in the OpenTouch solution. This server must be used without authentication and without TLS."（p360）
> "Only one general announcement can be recorded at a time. Any new recording will overwrite the previous one. Max duration: 5 minutes"（p392）

出处：OPENXTE300EN p302-396。

## I — 自述

Local Storage 语音邮件是 OT 内置软件语音邮件（默认实例 defaultVmsLS，出厂即建）：留言以未压缩 wav 存 OT 服务器目录，任意 IMAP 客户端可直读；UM 统一消息是另一套体系（另一培训），两者可共存。

邮箱档案默认面：

| 档案 | 类型 | 定位 |
|---|---|---|
| Advanced / Classic / Simplified | Local Storage | 默认三档，行为模板 |
| Standard | Unified Messaging | UM 专用（书外） |

档案四页签控制：Answer only（三态，默认 Manageable by users）、配额（需启用 Check quota 才生效）、新/已听留言保留天数、TUI 口令管理三档、零出（Attendant call enabled）、IMAP 访问开关等。邮箱上的字段随档案取值锁定：档案设 Yes/No 时用户改不了，设 Manageable by users 才开放。

IMAP 链：默认 IMAPS+TLS；改 SSL 或明文必须两端同步改端口并 service imap4fed restart；内嵌 IMAP 前端最多 1000 并发会话，1001-20000 需专用服务器；Outlook 账号测试里"发送测试邮件"失败属预期（OT 不做 SMTP）。

通知两链与配置分层：

- SMTP 链走外部服务器（必须无认证无 TLS；发件账号须真实存在；投递失败 NDN 只落发件账号邮箱，OT 仅在邮件未达 SMTP 时告警）
- SMS 链发邮件到唯一一个 SMTP-SMS 网关（地址格式 SMS$手机号$@域名）
- 配置三层：全局参数、VPIM 路由（域/FQDN/端口 25）、用户 Notification 页签
- 通知模板在 /var/data/panda/notification4，升级不覆盖旧模板

通用公告：一次仅一条、新录/新传即覆盖、最长 5 分钟、wav 格式固定 CCITT A-law 8bits 8kHz mono、文件名必须 general_announcement.wav；播放时机三选可多选；授权用户经 TUI 增强菜单 6 录/听/停用。

## A1 — 书中案例

**邮箱与档案实验**（p326-344）：

1. 核默认系统：Topology/VMS 的 defaultVmsLS 类型为 Local Storage。
2. Voicemail box 右键 Create，General 页命名并选系统。
3. Configuration 页必须先选语音邮箱档案才能保存。
4. 到 User 的 Mailboxes 页签搜索并关联邮箱后 Apply。
5. Licenses 页勾 Voice mail 启用许可。
6. 新建档案自定配额、时长与保留天数并分配实测。
7. 管理员侧配 Greetings 页签（问候类型与备选问候授权）。
8. 用户侧 My Profile 改问候、按名寻址与自动阅读。

**IMAP 与通知实验**（p345-378）：

1. Outlook 手动建 IMAP 账号：收件服务器填 OT FQDN。
2. 发件服务器填真实邮件系统（OT 不做 SMTP）。
3. 账号测试：IMAP 登录应 Completed，测试邮件失败属预期。
4. 改 IMAP 安全档位时两端同步改端口并重启 imap4fed。
5. 全局通知参数配发件人、SMS 网关、附件上限与阈值。
6. VPIM 加路由指向客户邮件中继（域、FQDN、端口 25）。
7. 用户 Notification 页签逐项配邮件与 SMS 通知。
8. 留言触发端到端验证：邮件按配置到达（含附件开关）。

**通用公告实验**（p393-396）：

1. TUI global configuration 勾播放时机（外部/内部/查询）。
2. 给授权用户勾"可管理通用公告"权。
3. 该用户话机登录邮箱，增强菜单 6 录制并自动激活。
4. 或上传固定名 wav 到公告目录即启用；停用删文件或菜单 3。

## A2 — 未来触发

使用情境：用户收不到留言邮件；Outlook 收不到语音留言；邮箱建不了或字段改不动；要不要短信通知；录一段全公司公告。

语言信号：语音邮箱 / voice mail / mailbox / defaultVmsLS / Local Storage / IMAP / Outlook / imap4fed / SMTP / SMS / 通知 / notification / Scorpio / chameleon / 公告 / announcement / 问候 / greeting / 配额 / quota。

与相邻能力区分：业务号 31200 与会议桥路由 → prior management 能力；UM 统一消息 → 书外专项培训；My Profile 自助入口在本卡范围内。

## E — 可执行步骤

输入契约：客户 SMTP/SMS 条件（无认证无 TLS 中继是否具备）；邮箱档案设计（配额/保留/口令管理）；IMAP 客户端清单；公告内容与授权人。

1. 核 defaultVmsLS 与用户许可；按设计建箱挂人。完成标准：留言进箱
2. 档案参数按需新建并分配测试邮箱实测。完成标准：截断、保留与配额生效
3. IMAP：客户端与服务端安全档位对齐。完成标准：IMAP 登录测试 Completed
4. 通知三层配齐：全局参数、VPIM 路由、用户页签。完成标准：留言触发邮件或短信
5. 公告：选播放时机、授权、录制或传 wav。完成标准：留言场景可听到公告

判停点：

- 建箱保存不了 → Configuration 页没选档案（强制项）
- 用户改不了留言设置 → 档案把字段锁成 Yes/No 了，改档案或改档位
- 通知"时有时无" → 先翻发件账号邮箱的 NDN，再查中继与阈值
- 客户 SMTP 强制认证或 TLS → 本版本通知要求无认证无 TLS，需单开中继并做安全评估
- 想预存多条公告 → 设计只有一条且覆盖式，5 分钟封顶
- IMAP 改安全后连不上 → 端口没同步改或 imap4fed 没重启

输出契约：留言-收信-通知-公告闭环测试记录 + 档案/通知参数清单。

## B — 边界

- 实验口径（生产按客户提供）：邮件中继 eco.company.com、发件地址 administrator@company.com、通知阈值 80%、附件上限 2MB、NFS 备份地 10.20.30.40。
- wav 附件/箱满通知/My Messaging 链接/回呼仅 Local Storage 可用；UM 行为不同（p366 表）。
- 公告 wav 存放路径书内两处表述不一（p392 与 p396，见 needs-review nr-01），生产以实测系统目录为准。
- "arrive on AA" 选项已废弃无效果（p394）；公告功能仅对使用 wav 文件的语言可用。
- 升级不覆盖通知模板；要新模板须删旧文件并重启 chameleon（n26）。
- OT 内嵌 IMAP 1000 并发封顶；1001-20000 会话需专用服务器（p313）。
