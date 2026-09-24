# OTFC 高级目录集成与来传真路由（LDAP、Lookup 表、NT 免密、路由表、DTMF、Modification、计费）

## R — 原文依据

> "Whether the system needs to assign a fax to a user (inbound faxing) or retrieve a user's Personal Information to send a fax (outbound faxing) … the system will always begin its queries with the user's SMTP Address."（p194）
> "A user who is not associated to any existing Site and any existing Profile is not allowed to use OTFC. Through these lookup tables it is possible to grant the faxing rights to some users"（p198）
> "The routing can be done by a multiple combination of routing rules: •Direct rules •Directory Lookup rules •Default rule … (except the Default rule, that remains the last)"（p205）
> "(&(objectClass=user)(objectCategory=person)(samAccountName=$NtAccountName$))"（p202）

出处：OTFCXTE200EN p192-213。

## I — 自述

目录与路由是大客户落地的五个机制：

1. **目录声明**：新装默认只用内部目录；可加 AD 或任意 LDAP——勾 enabled、服务器地址、端口 389、Search base（搜索树起点）、Test connection 验证；Attributes 页签做 OTFC-LDAP 属性映射；目录断连自动产生 SNMP trap
2. **Lookup 两表**：外部用户必须有 Site+Profile 才能用系统；Site Lookup 与 Profile Lookup 都是"基于目录属性的 if 规则"（可按邮箱/传真号/职务等字段过滤），Profile 默认规则是"用用户设置里指定的 Profile"
3. **免密登录两路**：AD NT Account Lookup 专用接口，或 LDAP 集成配 samAccountName 搜索过滤器再加 Conditions 条件；Web 自动登录还需 IIS 禁匿名 + 启 Windows 认证且 OTFC 服务器是域成员
4. **路由四旋钮**：Incoming Routing Table 三类规则（Direct、Directory Lookup、Default 兜底恒排最后，Directories Lookup 匹配值 $did:?????$）；DTMF 补拨（+33155667000 P 1234，P=暂停，可激活 4 位分机语音提示）

5. **号码规整与计费**：Modification Table 规整目录带来的号码（超过 6 位且 33 开头的外部号把 33 换成 00）；外发传真在 OXE 生成计费票，OmniVista 8770 取票出报表，票默认映射传真号

## A1 — 书中案例

**来传真按目录 owner 投递**（p205-208，讲义流程，号码实验口径）：

1. PSTN 呼 0123431500，OXE 收到 123431500
2. 传真服务器侧收到 31500
3. Incoming Routing Table 的 Directories Lookup 用 $did:?????$ 匹配 DDI 号
4. 查内部库或 LDAP 命中 owner（如 barkley@company.com，传真号 33123431500）
5. 按通知规则投递邮箱；通知故障查 ConfigManager.log 与 Smtp.log

**Modification Table 规整**（p210-211）：

1. 联系人 Mr Dupond 存国际格式 33298765432
2. 规则：超过 6 位且 33 开头，前两位 33 替换为 00（ARS 前缀+国内前缀）
3. 实际呼出 00298765432

## A2 — 未来触发

使用情境：AD 用户查得到但用不了传真；外部用户自动分配站点与 Profile；SendFAX/Web 免密登录；来传真按被叫号投人；用户拨国际格式联系人号码多拨 33；传真成本按人出报表。

语言信号：LDAP / Search base / 属性映射 / Lookup / Site Lookup / Profile Lookup / NT Account / samAccountName / 免密 / SSO 登录 / IIS / Windows Authentication。

语言信号（续）：Incoming Routing Table / $did / DDI / DTMF / 补拨 / 分机 / Modification Table / ARS / 计费 / accounting / 8770。

与相邻能力区分：目录连接本身的声明属本卡，账号手工管理属用户管理能力；SIP 话路不通属 SIP 通道集成能力；Web Client 里的电话簿属 Profile 策略能力（本卡管 LDAP 访问链的服务端）。

## E — 可执行步骤

输入契约：客户 AD/LDAP 结构实勘结果（端口/Search base/属性）、编号计划（DDI 号段/分机规则）、OTFC 服务器域成员身份（免密场景）。

1. 声明目录：enabled + 服务器 + 端口 389 + Search base + Test connection。完成标准：连接测试通过
2. 属性映射：Attributes 页签逐项匹配 OTFC 与 LDAP 属性。完成标准：关键字段（SMTP/传真号/职务）映射齐全
3. 配 Lookup 两表：Site Lookup 与 Profile Lookup 按 if 规则落外部用户归类。完成标准：抽样外部用户能被归到 Site+Profile
4. 免密登录（如需）：AD NT Account Lookup 接口或 samAccountName 过滤器 + IIS 禁匿名/启 Windows 认证。完成标准：域内用户打开 Web 免密直达
5. 入局路由表：Direct 与 Directory Lookup 规则按精度排序，$did:?????$ 按实际号长调整，Default 兜底确认在最后。完成标准：测试号路由到正确用户
6. 号码规整：Modification Table 按客户 PSTN 拨号口径配规则。完成标准：联系人国际格式号码实际呼出正确
7. DTMF 补拨（如需）：目的号 + P + 分机语法，来话方向按需激活 4 位分机语音提示。完成标准：补拨传真可达
8. 计费（如需）：OXE 计费票对接 OmniVista 8770，确认映射口径（默认传真号，按人核算改电话号）。完成标准：8770 出测试报表

判停点：

- AD 用户查得到但用不了 → 先查两张 Lookup 表规则命中，别只盯目录连接（无 Site+Profile 即拒用是设计行为）
- 自动登录仍弹凭据框 → 按三前提逐项核：域成员、禁匿名、启 Windows 认证，顺序按原文先禁匿名
- 来传真通知不到但路由正常 → 查 ConfigManager.log 与 Smtp.log，再转邮件与 Exchange 集成能力
- 想把 Default 兜底规则排到前面 → 停，Default 恒最后不可移动，只能把精确规则前置
- 客户目录不是 AD 且字段命名非常规 → 停，先实勘属性再映射，属性名不猜

输出契约：目录集成参数表（服务器/Search base/映射）+ Lookup 规则清单 + 免密登录配置记录 + 路由/DTMF/Modification 三表配置与测试记录 + 计费映射口径说明。

## B — 边界

- DNIS/CSID/ANI/DDI/ARS 等缩写书内未给全称，括注均为通用电信含义（推断）；引用时保留标注
- 端口 389 为 LDAP 明文口径，LDAPS 书内未展开；目录基础设施由客户提供
- 目录断连的 SNMP trap 需要客户网管侧有落点，否则只能被动发现（推断后果，原文只说产生 trap）
- 计费链路的 8770 侧报表配置在书外；DTMF 语音提示内容与多语言支持书内未展开
- 规则示例号段（31500/33123431500、33/00 前缀）均为实验/法国示例口径，生产按客户编号计划替换
