# IMAP 客户端访问语音邮箱（IMAPS/TLS/imap4fed/Outlook 判据）

## R — 原文依据

> "IMAP4 used for direct consultation to mail server … POP3 used to retrieve all received emails"（p197）
> "The 'send test e-mail message' test fails, if a SMTP server is not reachable or OpenTouch/OTMC FQDN is used as outgoing mail server (OpenTouch server/OTMC (local storage voice mail) does NOT act as a SMTP server)"（p207）
> "BY DEFAULT, IMAPS IS ENABLED ON OPENTOUCH SIDE WITH 'TLS' SECURITY."（p208）

出处：OTMCXTE200EN p193-209（c10、f21、p20、n13/n14 归并）。

## I — 自述

**原理**：发信走 SMTP、收信分 POP3（全量下载落地）与 IMAP4（直连服务器查阅）；OTMC 充当 IMAP 服务器——留言落箱 → MWI 亮灯 → 邮件客户端以独立账户直读留言与附件。外网访问经 VPN（书中给图不给 VPN 配置）。

**三处对齐**：

| 位置 | 要点 |
|---|---|
| 客户端（Outlook 手动账户） | 账户类型 IMAP；收件服务器=OTMC FQDN；发件服务器填真实邮件服务器 FQDN（OTMC 不是 SMTP 服务器，填 OTMC 会误报）；用户名/密码=GUI 凭证；Advanced 页签加密类型与服务端一致 |
| OTMC 侧 IMAP4 Front End | 路径 System services/Topology/Physical servers/OT component/"IMAP4 Front End"；默认 IMAPS+TLS，端口按安全类型自动带出；改 SSL/无加密须改端口号并 service imap4fed restart |
| 验收判据 | "log onto incoming mail server (IMAP)" 测试 Completed 才算配对；"send test e-mail message" 失败属预期 |

## A1 — 书中案例

**Outlook IMAP 账户实验**（c10，OTMC FQDN 等环境值见 book/overview）：

1. 控制面板邮件入口新建账户：选 Manual setup → POP or IMAP
2. 账户设置：Account type=IMAP；收件服务器填 OTMC FQDN；发件服务器填真实邮件服务器 FQDN
3. 凭证：用户名/密码用 OTMC 的 GUI 账号；More Settings 的 Advanced 页签选加密类型（与服务端一致）
4. 点 Test Account Settings：IMAP 登录测试必须 Completed；发信测试红叉属预期
5. 服务端核对：IMAP4 Front End 的 Connection security 与端口；如改安全级先改端口再 service imap4fed restart
6. 验收：第二账户下收到 LS 信箱全部语音消息（邮件+语音附件）

## A2 — 未来触发

使用情境：远程/桌面工作者要用 Outlook 听留言；"IMAP 连不上"；"Outlook 测试有红叉是不是没配好"；要降级加密类型。

语言信号：IMAP / IMAPS / POP3 / Outlook / 邮件客户端 / 听留言 / imap4fed / TLS / SSL / incoming mail server / 收件服务器 / 留言附件。

与相邻能力区分：通知邮件（服务器推送，无认证无 TLS 的 SMTP）→ otmsg-notification-smtp-sms；信箱与 GUI 凭证的前置 → otmsg-user-mailbox-provisioning。

## E — 可执行步骤

输入契约：用户有 LS 信箱与 GUI 凭证、客户端可达 OTMC、加密口径已定。

1. 服务端定口径：IMAP4 Front End 的安全级与端口。完成标准：服务端参数明确
2. 客户端建账户：按三处对齐清单录入（IMAP/OTMC FQDN/GUI 凭证/加密匹配）。完成标准：IMAP 登录测试 Completed
3. 期望管理：书面告知发信测试失败属预期及原因。完成标准：客户接受验收口径
4. 外网场景声明：VPN 前提在书外，按客户网络方案处理。完成标准：边界讲清

判停点：

- IMAP 登录测试不通过 → 先比两侧加密类型与端口（默认 IMAPS+TLS）；改级必须双端同步并 service imap4fed restart（n14）
- 客户把发信红叉当配置失败 → 按原文口径解释：OTMC 不是 SMTP 服务器（n13）
- 用户信箱是 UM 型 → 本卡验证口径基于 LS 信箱；UM 场景原书仅支持性声明（n28）

输出契约：可直读语音留言的 IMAP 客户端 + 服务端/客户端参数对照记录。

## B — 边界

- POP3 仅为协议对照项，OTMC 场景用 IMAP4；START TLS/RFC 2595 在 p7 特性描述中被引用，细节书外
- 外网 VPN 配置不在本书（p198 只给拓扑示意）
- 实验客户端环境（Windows/Outlook 旧入口）与 OTMC FQDN 见 book/overview
