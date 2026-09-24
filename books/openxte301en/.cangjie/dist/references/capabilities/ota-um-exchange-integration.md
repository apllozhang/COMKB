# 统一消息 UM（Exchange/O365/Gmail/IMAP 四后端与 Impersonation）

## R — 原文依据

> "The OpenTouch server handles the voice messaging process and the company mail server/Gmail stores voice messages • Single point of storage • Voice messages are stored in Wav format"（p170）
> "Since the release 2.3 ... the OpenTouch server uses now impersonation method instead of delegation"（p189）
> "Gmail platform can be used to store voice mails ... Limited to 500 OpenTouch users"（p176）
> "IMAP4 mail server • No plug-in: less services • No PPR • No Extensions • No MWI • No class of message"（p177）

出处：OPENXTE301EN p168-217。

## I — 自述

UM 把语音留言变成邮件服务器里的一封邮件（Wav 单点存储，容量只受邮件服务器限制）：

1. **四后端能力递减**：Exchange（本地，全功能）≥ Exchange 云 O365（需 OT 2.5 才有 Outlook 加载项/Office 集成，仅桌面版）> Gmail（OAuth 2.0 接入，上限 500 用户）> IMAP4（无插件，砍 PPR/扩展/MWI/消息类别）
2. **Exchange 侧钥匙**：特权账号 ICEaccess（AD 账号+邮箱+密码永不过期）+ Impersonation 授权（EMS 给 ApplicationImpersonation 角色；R2.2 前用 delegation 逐邮箱三参数）+ CA 证书入 OT 信任库
3. **OT 侧三层**：UM 语音邮件系统（Topology/VMS）→ 语音邮箱档案（4 个默认：1 个 UM standard+3 个 Local Storage，Answer only/Direct callback/Attendant call '0'/sent items 副本等参数）→ 信箱分配（建用户时或 Voicemail box 建）

邮件服务器声明：协议 EWS、端口 443、登录两种格式（DOMAIN\login 或 login@DOMAIN）；云场景 FQDN 固定 outlook.office365.com、需 HTTP proxy 与通知服务公共 URL（按 /ExchangeNotificationService 放行，可省反向代理）。

维护抓手：守护进程 mascd 与 wireald，异常时 restart；日志在 logs/masc、logs/wireal。

## A1 — 书中案例

**UM（Exchange）部署实验**（p182-217）：

1. AD 建 ICEaccess 账号（勾密码永不过期，实验口径 iceaccess）
2. Exchange 管理中心确认其邮箱存在
3. EMS 执行 New-ManagementRoleAssignment 授 ApplicationImpersonation（R2.3+ 口径）
4. CA 根证书下载并导入 OT 信任库（Server CTL 页签 Add）
5. 声明邮件服务器：EWS/443/ICEaccess 登录/on-premises，勾日历在场与会议同步两开关
6. 建 UM 语音邮件系统（Type=UM，Mail server=mail）
7. 核对语音邮箱档案参数并确认 31200 留言号两侧成对
8. 档案改动后执行同步（OT/OXE，Warning：不同步模板取不回）
9. 分配信箱（Voicemail box 建 UM voicemail box 并关联用户）
10. 验证：留言后 My Messaging 与 Outlook 均可见

## A2 — 未来触发

使用情境：语音留言进邮箱方案；选哪种邮件后端；留言灯（MWI）不亮；用户问为什么 My Profile 里没有问候语；O365 部署要开什么；Gmail 能不能扛全员。

语言信号：统一消息 / UM / voice mail / 语音邮箱 / Exchange / O365 / Office 365 / Gmail / IMAP4 / EWS / ICEaccess / impersonation / 委托 / delegation / MWI / PPR / 信箱 / voicemail box / MASC / Wireal。

与相邻能力区分：日历在场与会议同步 → 日历同步能力（配置同源但机制独立）；本地存储邮箱的日历 → TC2558（超出本卡）；话机留言键的 OXE 侧参数在本卡 A1 步骤 7。

## E — 可执行步骤

输入契约：邮件后端类型与版本（Exchange 版本/OT 版本）、特权账号治理、证书链、用户规模（Gmail 500 上限卡）。

1. 选型确认：按后端能力递减谱系与版本门槛确认方案。完成标准：选型与版本矩阵书面确认
2. Exchange 侧授权：R2.3+ 用 Impersonation（EMS 一条命令）；R2.2 及以前用 delegation（每邮箱三参数）。完成标准：Get-ManagementRoleAssignment 可见
3. 证书入信任库：CA 根证书导入 Server CTL。完成标准：证书在列
4. 声明邮件服务器（EWS/443/登录格式/位置；云场景加 proxy 与通知 URL）。完成标准：两开关已勾
5. 建 UM 系统与核对档案。完成标准：VMS 关联 mail、档案参数确认
6. 同步后分配信箱并验证留言投递。完成标准：My Messaging 与 Outlook 双侧可见

判停点：

- 留言不进邮箱 → 高频根因是 ICEaccess/Impersonation 配置，先查授权再查证书
- 档案改了没效果 → 查是否漏同步（Warning p201）
- My Profile 里没有问候语 → 先让用户用话机录一遍（网页端不能从零创建，p211）
- 客户用自建 IMAP → 提前把 PPR/扩展/MWI/消息类别四项降级写进方案，不按 Exchange 体验承诺
- Gmail 方案超 500 用户 → 停，改 Exchange/O365 或 IMAP 并重新谈预期

输出契约：后端选型结论 + Exchange 侧授权与证书记录 + UM 三层配置单 + 留言投递验证结果。

## B — 边界

- 版本分界：OT ≤2.2.x 用 delegation、2.3 起用 impersonation；升级 OT 后要同步换 Exchange 侧方案，两代混用出疑难（n44）
- O365 的 Outlook 加载项/联系人同步/Office 集成要 OT 2.5+ 且仅桌面版 Office（n23）
- 凭据（ICEaccess 密码等）实验值必须替换生产值并纳入 vault 管理（n49）
- 本地存储邮箱（Local Storage 档案）的日历特性走 TC2558，不在 UM 流程内（n32）
- UM 实现的生产化细节以 TC2391 为准
