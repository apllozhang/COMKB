# OTFC 邮件与 Exchange 集成（SMTP 网关、寻址、FAX 地址空间连接器、通知排障）

## R — 原文依据

> "The XMSmtpGateway module, called SMTP Gateway, has the two usual basic functions of a mail server, allowing the Fax Server to: • Receive emails from OTFC users in order to convert them into faxes. • Send emails to OTFC users for notification purpose"（p157）
> "Create a new send connector. • Associate the 'FAX' address space to this Connector and forward all mails to a smart host which corresponds to the fax server's SMTP Gateway."（p164）
> "New-SendConnector -Name <ConnectorName> -AddressSpace "fax:*;1" –SmartHosts "<SMTPGateway>" –DNSRoutingEnabled $false -SourceTransportServers "<HubTransportServers>""（p167）
> "A feedback address must be filled in the SMTP Gateway settings to enable reply from the gateway with a mail header (mail header can't be empty!)."（p161）

出处：OTFCXTE200EN p156-175（含 How-To 实验 7）。

## I — 自述

邮件是传真的主入口，这条链路分四层：

1. **SMTP 网关职责**：监听系统 25 端口收传真作业、发通知邮件；同一服务器不能有别的 SMTP 服务；设置里必须填 feedback address（邮件头不能为空）
2. **拓扑**：用户邮件可直达网关，但官方强烈建议前置真实邮件服务器——换来队列管理、Outlook 表单集成、垃圾过滤、病毒检查四类能力；经客户 LAN 中继还可收 NDR（未投递报告）
3. **寻址格式**：31600@<传真服务器 FQDN>；无 Outlook 联系人用 [FAX:0298131600]；有联系人直接选；扩展语法 [FAX:姓名@号码]、[FAX:/fn=名/ln=姓/jobtitle=职务@号码]
4. **Exchange 集成**：建 'FAX' 地址空间 Send Connector（fax:*;1）指向网关智能主机——SMTP connector 是许可特性；Exchange 收件安全过高会拦全部通知，调 Hub Transport 下 Receive Connector 放行

## A1 — 书中案例

**建 FAX 连接器并核验**（p172-174，实验 7，实验口径）：

1. 打开 Exchange Management Shell
2. 执行 New-SendConnector -Name OTFC -AddressSpace "fax:*;1" –SmartHosts "fax.company.com" -DNSRoutingEnabled $false –SourceTransportServers "eco.company.com"
3. 查看命令回显确认创建成功
4. Exchange Admin center → Mail flow → Send Connectors 页签应出现 OTFC 连接器
5. 双击连接器逐项核对（AddressSpace、SmartHosts、DNSRoutingEnabled、源传输服务器）
6. 通知被拦时到 Hub Transport 节点调 Receive Connector 安全参数

## A2 — 未来触发

使用情境：用户要用邮件发传真；传真收发正常但通知邮件一封不到；SendFAX 的 Outlook 模式发不出去；Exchange 用户怎么填传真地址；要不要直连网关；连接器建好了不生效。

语言信号：SMTP / SMTP Gateway / 25 端口 / feedback address / NDR / 邮件中继 / mail relay / Exchange / Send Connector / FAX address space。

语言信号（续）：fax:* / 智能主机 / smart host / [FAX:] / Receive Connector / Outlook 模式 / 许可特性。

与相邻能力区分：通知格式与语言 Profile 归 Profile 策略能力；通知问题排查先网关与 Exchange、再路由（来传真路由归目录与路由能力）；服务起不来归服务运维能力。

## E — 可执行步骤

输入契约：OTFC SMTP 网关服务运行中（25 端口独占）、邮件服务器信息（FQDN）、Exchange 管理权限、许可含 SMTP connector 特性。许可不含特性时连接器建了也不生效，先核许可。

1. 定拓扑：网关前置真实邮件服务器（推荐）或直连（仅最小实验）。完成标准：拓扑决策与客户确认
2. 网关设置：填 feedback address，核对 Mail Relay Server。完成标准：网关可带合法邮件头回信
3. 核寻址口径：与客户确认 31600@FQDN / [FAX:号码] / Outlook 联系人三类用法。完成标准：用户使用说明可用
4. Exchange 建连接器：New-SendConnector（fax:*;1、SmartHosts=网关、DNSRoutingEnabled=$false、源传输服务器）。完成标准：Send Connectors 列表出现新连接器
5. 核验连接器：Exchange Admin center 双击逐项核对参数。完成标准：参数与命令一致
6. 放行通知：Exchange 收件安全过高时调 Hub Transport 下 Receive Connector。完成标准：测试通知邮件可达用户邮箱
7. 端到端测试：用户从邮件客户端发传真到测试号，收通知与附件。完成标准：PDF/TIFF 附件与 HTML/Text 正文按配置到达

判停点：

- 传真收发正常但通知全无 → 按序查：feedback address 是否为空、Exchange Receive Connector 是否拦截、垃圾箱，不要先动路由表
- SendFAX Outlook 模式发不出 → 停，先确认 'FAX' 地址空间连接器已建（该模式硬依赖），再排客户端
- 许可清单里没有 SMTP connector 特性 → 停，转许可商务，不要反复重建连接器
- 客户想把邮件服务器和 OTFC 并装一台 → 停，25 端口互斥，按独占 25 规划换机器或换部署方案

输出契约：邮件传真通道拓扑图（网关/中继/Exchange 角色）+ 已核验的 Send Connector + feedback address 与寻址口径说明 + 端到端测试记录。

## B — 边界

- SMTP connector 是许可特性（p158）：功能装得上、许可不含就用不了；其余许可特性清单以 Features List 为准
- 直连网关模式官方"强烈建议"仅作过渡，四类邮件管理能力缺失；生产按带邮件服务器拓扑设计
- 通知正文格式（Exchange integration + Text）只影响邮件通知，与 Web Client 显示无关——"通知里没图"先查通知 Profile 再看 Web
- 邮件通知 Profile 的每语言配置与 Profile 关联机制 → Profile 策略能力；MS SMTP 冲突的安装期处理 → 首次交付能力
- Exchange/O365 环境与权限由客户提供；书内命令以实验版 Exchange 语境为准，生产参数按客户 Exchange 版本核对
