# SMTP/SMS 通知部署与排障（VPIM 路由/模板/双矩阵/MWI）

## R — 原文依据

> "Notifications are sent through an external SMTP server. • There is no SMTP server in the OpenTouch solution. • This server must be used without authentication and without TLS."（p174）
> "SMS notification consists in sending an e-mail to the SMS gateway which is in charge of formatting and sending the SMS. • Only one SMS Gateway can be configured in the system"（p177）
> "Notifications are handled by 'Scorpio' component."（p185）
> "MWI on the phone set is not synchronized when reading the email"（p171）

出处：OTMCXTE200EN p167-192（c09、f20、p16-p19、n11/n12/n15/n16/n21/n22 归并）。

## I — 自述

**两条链路**：

1. SMTP：留言落箱后由 Scorpio 组件经 VPIM session 声明的路由发往外部 SMTP；用户邮箱收到邮件（附件 wav / My Messaging 链接 / 回呼，另有满箱与近满提醒）。话机 MWI 随落箱亮灯，但读邮件不灭灯（机制性不同步）
2. SMS：留言落箱触发 SMTP 通知（含信箱号/主叫号），发给 SMTP-SMS 网关（全系统仅一个，地址格式 SMS$手机号$@域名），由网关转用户手机

**可用性矩阵（LS / UM）**：

| 功能 | Local Storage | Unified Messaging |
|---|---|---|
| 短信通知 | 有 | 有 |
| 邮件通知 | 有 | 有 |
| wav 附件 | 有 | 无 |
| My Messaging 链接 | 有 | 无 |
| 回呼留言主 | 有 | 无 |
| 满箱/近满提醒 | 有 | 无 |

**数值与规则口径**：

- 附件上限 2MB（超限发信不带附件）；近满阈值默认 80%（p184 原文带 by default 80%）；SMTP 端口默认 25
- 附件格式四选一（AAC / linear PCM 16bits / linear PCM 8bits / G.711 PCM 的 .wav）
- SMTP 服务器必须无认证、无 TLS，发件地址须真实存在
- 模板按语言存 /var/data/panda/notification4；升级不覆盖旧模板，要新版须删旧模板并重启 chameleon
- 排障抓手 service chameleond/scorpiod status 与 /logs 三处日志
- 送达失败基本静默：退信落发件账户邮箱，仅"未到达 SMTP"才告警并转 SNMP trap

## A1 — 书中案例

**通知部署与端到端验证**（c09，SMTP 服务器地址等环境值见 book/overview）：

1. 全局参数：System services/Applications/Notification/Notification → Edit：发件人名/地址（须为 SMTP 服务器上真实账户）、wav 上限 2MB、阈值 80%、附件格式四选一
2. 声明 SMTP 路由：System services/Applications/Messaging/VPIM → Add：域名、FQDN or IP、端口 25（服务器须无认证无 TLS）
3. 定制模板（可选）：改 /var/data/panda/notification4 下对应语言的 properties 文件
4. 用户前置：核验目标用户有 LS 信箱、邮箱地址已配、Voice mail 权已勾
5. 用户设置：Notification 页签给权、启用、填通知邮箱；按需开满箱通知/附件/关 MWI/链接（LS 专属项）
6. 端到端验证：向用户信箱留一条言，核对邮件（附件/链接）、MWI、按需核短信
7. 维护排障：service chameleond status 与 service scorpiod status；查 /logs 下三处日志

## A2 — 未来触发

使用情境：开通"留言转邮箱/短信"；"没收到通知"工单；升级后通知文案没变；UM 用户为什么没附件；客户 SMTP 要认证怎么办。

语言信号：SMTP / 通知 / notification / SMS / 短信 / 网关 / VPIM / Scorpio / chameleon / 模板 / NotifTemplate / MWI / 满箱 / 附件 / wav / My Messaging。

与相邻能力区分：通知的前置（信箱与 Voice mail 权）→ otmsg-user-mailbox-provisioning；IMAP 客户端直读留言 → otmsg-imap-access（路由卡）。

## E — 可执行步骤

输入契约：客户提供 SMTP 服务器（能开匿名+明文）与（如需短信）SMTP-SMS 网关；发件账户真实存在。客户 SMTP 只支持认证/TLS → 判停谈替代方案。

1. 确认 SMTP 口径：无认证无 TLS 可达、端口、发件账户存在。完成标准：连通口径书面确认
2. 配全局参数与 VPIM 路由。完成标准：路由声明成功
3. 配用户级通知：按 LS/UM 矩阵管理预期再配。完成标准：设置在册
4. 端到端验证：留言触发通知，核对附件/链接/MWI/短信。完成标准：链路闭环
5. 交付排障指引：退信查发件账户、告警查 SNMP trap、日志三件套。完成标准：客户运维可自查

判停点：

- 用户说"没收到通知" → 先查发件账户的退信与 SMTP 连通性——OTMC 侧投递失败大部分是静默的（n16），不要空等告警
- UM 用户要附件/满箱提醒 → 停，LS 专属功能（n21），改需求口径或评估换信箱类型，不要硬配
- 升级后通知文案还是旧的 → 模板保护机制：删旧模板 + 重启 chameleon + 回填定制（n12），不是 bug
- 管理界面看得到 LS 专属项但用户是 UM → 界面不按类型隐藏，配了也无效（n11）

输出契约：可用的通知链路（SMTP/短信）+ 用户设置清单 + 端到端验证记录与排障指引。

## B — 边界

- OTMC 方案内不含 SMTP 服务器、OTMC 本身也不当 SMTP 服务器（与 IMAP 卡的判据互证，n13）
- 通知语言跟随用户 GUI 语言；"仅对支持 wav 文件的语言开放"部分功能（p223 口径的关联限制）
- SMS 网关选型与采购在书外；多运营商分流不支持（仅一个网关，n22）
- 实验用 SMTP 服务器（Eco-System 虚机 25 端口、域名）等环境值见 book/overview
