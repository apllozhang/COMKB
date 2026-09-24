# 用户自助门户 My Profile 与 MyMessaging（网页听留言/自助设置）

## R — 原文依据

> "Application available via a web browser using the following URL • https://<OpenTouch Messaging Center FQDN>"（p156）
> "Application available via a web browser using the following URL • https://<OpenTouch Messaging Center FQDN/MyMessaging> • or through the application 'My Profile'"（p165）

出处：OTMCXTE200EN p153-166（f19、g13、p12/p24 归并）。

## I — 自述

OTMC 提供两个用户自助 Web 应用，登录均用用户 GUI 账号：

| 应用 | 入口 | 功能区 |
|---|---|---|
| My Profile | OTMC FQDN 根路径 | 按主题的用户设置与保存/取消；语言与时区（TUI/Web 语言、留言时区）；personal assistant 联系人与电话号码；语音邮件参数（激活问候语、信箱选项开关）；密码管理（TUI 密码与 My Profile 密码）；跳转 MyMessaging；SMTP/SMS 通知启用与定制 |
| MyMessaging | OTMC FQDN/MyMessaging，或经 My Profile 进入 | 新留言/已存留言列表（优先级、日期时间、主叫号码、时长、呼叫处理）；播放可在 PC 或话机上执行；挂断/删除/刷新动作 |

可见性规则：门户里看得到哪些设置由管理员授权决定（p191 Note）；TUI 密码管理档位由 profile 控制（p149）。

## A1 — 书中案例

web clients 章（p153-166）为界面导览，无独立 How-To 实验；用户自助动作散嵌于其它实验的用户侧步骤：信箱定制核验走 My Profile（c07 步骤 11）、通知自开关与改通知地址走 My Profile 的 Notification 区（c09 步骤 6）。

## A2 — 未来触发

使用情境：交付后用户培训；"网页上怎么听留言"；"自己想改问候语/密码/通知地址"；用户报"我的设置里少了某项"。

语言信号：My Profile / MyMessaging / 自助门户 / 网页听留言 / personal assistant / 改问候语 / 改密码 / 通知设置 / web 客户端。

与相邻能力区分：管理员批控（profile/Greetings 页签/Greeting Managers）归 otmsg-mailbox-profiles；通知链路部署归 otmsg-notification-smtp-sms；IMAP 客户端见 otmsg-imap-access（路由卡）。

## E — 可执行步骤

输入契约：用户已知 GUI 凭证、OTMC FQDN 可达（网络侧放行属客户环境）。

1. 入口指引：My Profile 走根路径、MyMessaging 走子路径或门户跳转。完成标准：用户能登录
2. 高频自助演示：改语言/激活问候语/开关通知/改密码/网页听留言。完成标准：用户独立操作一遍
3. 可见性问题处理：缺失项按管理员授权口径解释并回管理员侧开权。完成标准：工单闭环

判停点：

- 用户看不到某设置 → 先查管理员是否授权（p191），不是故障，不要重装/重配
- TUI 密码改不了或档位不对 → 档位由 profile 控制，转 otmsg-mailbox-profiles
- 网页进不去 → 核对 FQDN 解析与网络可达，超出本书范围的防火墙/VPN 细节按客户环境处理

输出契约：可自助操作的用户 + 门户功能演示记录。

## B — 边界

- 门户是"用"的界面，不承载管理员配置；管理员侧动作走 8770/WBM/Greeting Managers
- p153-166 为界面导览章，原书无门户专项实验——步骤粒度以界面导览口径为限
- 实验门户地址（otmc.company.com 等 FQDN）与 GUI 口令见 book/overview
