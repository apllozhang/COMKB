# OmniVista 8770 告警管理（接入 + 定制出口 + SNMP Proxy）

## R — 原文依据

> "Critical Red / Major Orange / Minor Yellow / Warning Blue / Indeterminate Purple / Cleared White"（p274）
> "Only active alarms can be acknowledged. Once acknowledged, alarm still active. ... Only uncorrelated alarms may be cleared."（p278-279）
> "Network severity: None, Topological network: YES ... Reset a coupler (rstcpl <Media Gateway number> <Board number>)"（p285）
> "enter: 10.20.30.11:46 if mail server uses the SMTP port 46 ... By default, the name is: omnivista@<8770 FQDN>"（p301）
> "Windows SNMP service must be installed, even if you have to disable it to activate the one provided by the 8770 server."（p317）

出处：8770XTE200EN p269-324（Alarms 应用 + OXE 接入 + 功能定制 + SNMP proxy）。

## I — 自述

告警能力三段：把告警接进来、按运维流程处置、给告警三个出口再加一条对外通道。

**架构与处置状态机**

- 采集链：OXE/OXO/OpenTouch 经 CMISE 发告警事件 > 8770 内部 Collector > Fault Manager > MariaDB（查询/操作）+ Notify server（Corba 通知客户端）+ SNMP Proxy（trap 外送）
- 六级色标：Critical 红 / Major 橙 / Minor 黄 / Warning 蓝 / Indeterminate 紫 / Cleared 白；客户端常显计数器，框色=当前最高严重级
- 相关告警（PCX 能检测问题结束）自动清除，Topology 只显示这类；非相关告警须人工清除
- 处置动作：确认（acknowledge，仍活动、记录确认人与变色）、清除（clear，仅非相关，转历史）、删除（从库移除，选中层级连子层全删）、签名（Signature/Action 进告警报告，Remark 不进）
- 事件（Event）无严重级：对象创建/删除/修改通知，是实时同步的载体

**OXE 侧接入与验证**

- 前提：OXE 声明告警接收模式 Permanent IP connectivity（节点声明时已含）
- OXE 配置界面 Applications > 1 > Incident Manager > 1：Network severity=None（全部上送）+ Topological network=YES
- 验证：mtcl 会话 rstcpl <MG> <板> 重启 coupler，incvisu -t 3 查最近事件，Alarms 树对应板卡应出 Major #2042（Loss of a GD/GD3 type cpl）
- 定向过滤：对特定事件号（如 mtcl 登录 #1125）建 Incident Filter 设 Network incident=Yes，无视 network severity 强制上送；部分数据库中该事件不在默认列表，须先 Create 再设（见 B）

**告警出口三加一**

- 人工：Signature/Action/Remark 三字段处置留痕（前两项进报告）
- 邮件：先在 Administration > OmniVista 8770 > Export parameters 配 Mail server（格式 <地址>:<SMTP 端口>，默认 25 可省略，冒号后不能有空格；发件人默认 omnivista@<FQDN>）；再在 Alarms > Preferences > Alarms Filters 建过滤器（条件 Severity Equal to Major 等 + E-Mail Addresses 页填收件人，多地址逗号分隔）
- 脚本：.bat 放 c:\8770\data\alarms\scripts；过滤器 Script 页填脚本名与变量——%1=$managedobject（告警对象）、%2=$notificationtime（通知时间）
- 字典定制：Start > OmniVista 8770 > Dictionary customization 改字段译名（如 Action 改 Operation）；生效链=关客户端 > Service Manager 重启 NMC Service Manager > 重开客户端
- 对外网管：SNMP Proxy 转 trap（见 E 线二）

## A1 — 书中案例

**告警接入实验**（p283-289）：

1. 确认 OXE 声明的告警接收模式为 Permanent IP connectivity
2. OXE 侧 Incident Manager 设 Network severity=None、Topological network=YES
3. mtcl 会话执行 rstcpl 4 0 重启 coupler
4. incvisu -t 3 看到 #2042 事件，Alarms 树中 OMS 虚拟板出现 Major #2042
5. 为 #1125 建 Incident Filter（Network incident=Yes），新开 mtcl 会话后 Minor #1125 上屏

**功能定制实验**（p290-306）：

1. Signature 页加 Jean Dupont/Paul Martin，Action 页加 Software/Hardware Maintenance
2. 字典把 Action 改译 Operation，重启 NMC Service Manager 后字段名生效
3. 建过滤器 Severity Equal to Major + 收件地址，rstcpl 触发后 Thunderbird 收到告警邮件
4. 建 message.bat（msg 命令带 %1 与 %2），触发后服务器屏幕弹窗显示告警对象与时间

**SNMP Proxy 实验**（p307-324）：装 Windows SNMP 功能后经 ToolsOmniVista 启用 8770 代理，日志见 agent started；声明 hypervisor 后勾 Managed by SNMP proxy，TrapReceiver 收到 Add PABX trap 与告警 trap。

## A2 — 未来触发

使用情境：值班告警不上屏；把 Major 告警邮件给网管；告警字段改名；把告警转发客户 NMS；确认/清除按钮行为争议。

语言信号：Alarms / 严重级 / correlated / acknowledge / clear / rstcpl / incvisu / #2042 / #1125 / incident filter / Network severity / 签名 / 字典 / SNMP Proxy / hypervisor / trap 162 / SNMP Filter。

与相邻能力区分：告警收不到先查节点声明与 Windows 前置（节点接入/平台安装能力）；拓扑图上的告警显示（Topology 视图能力）；本能力管告警数据流与出口。

## E — 可执行步骤

输入契约：已同步节点、告警运维角色分工（谁处置/谁收邮件）、外部网管参数（IP/协议版本/trap 端口，如需外送）。

线一：接入与验证

1. 核对 OXE 声明告警接收模式与 Windows 前置（IE ESC/Defender）。完成标准：两项前提无缺失
2. OXE Incident Manager 设 Network severity 与 Topological network。完成标准：None+YES 为全上送口径
3. rstcpl 触发测试告警并查 incvisu。完成标准：Alarms 树出对应板卡 Major 告警
4. 需要定向时建 Incident Filter（必要时先 Create 事件）。完成标准：目标事件无视严重级上屏

线二：出口定制

5. 配 Mail server（注意 server:port 语法）。完成标准：测试邮件可达收件箱
6. 建 Alarms Filters 挂邮件/脚本出口。完成标准：触发后邮件到达或脚本执行
7. 字典改名走三步生效链。完成标准：重开客户端字段名已换
8. SNMP Proxy：装 Windows SNMP 功能 > ToolsOmniVista 启用代理 > 声明 hypervisor > 勾 Managed by SNMP proxy > 配 SNMP Filter。完成标准：NMCSnmpAgent_1.log 见 agent started 与 Add PABX trap，TrapReceiver 收到

判停点：

- 节点告警完全不上送 → 先查节点声明的告警接收模式与 Windows 两项前置，不要先动 OXE
- incident filter 下拉找不到目标事件号 → 先 Create 事件（产品行为非故障）
- Windows SNMP 功能被卸载 → 代理失去 Netsnmp 地基，重装功能后重新启用
- TLS/防火墙类改造 → 标注"仅供信息"的流程不直接执行，单独立项

输出契约：告警上送验证记录（#2042/#1125）+ 过滤器与出口清单 + hypervisor 配置表 + 字典变更记录。

## B — 边界

- hypervisor 声明只填 IP 不用 FQDN；V3 声明与卸载流程书中标注"仅供信息、勿执行"
- SNMP Filter 按 Correlation（Equal True）或 Diagnostic（号码列表分号分隔、区间连字符）转发，可 AND/OR 叠加第二条件
- 告警邮件依赖已配置的邮件服务器；密码重置邮件同源（安全管理卡），SMTP 端口语法错误是发信失败首因
- OXE R11.2 起 IP 话机状态告警（incident 386）不再是可相关告警，Topology 不能用（Topology 卡边界）
- 实验邮件域名/收件人（company.com、Thunderbird）与 TrapReceiver 均为实验口径，见 book/overview
