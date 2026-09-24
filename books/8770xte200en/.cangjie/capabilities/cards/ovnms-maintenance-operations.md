# OmniVista 8770 维护运营（诊断工具 / NMC 服务与日志）

## R — 原文依据

> "8770 Diagnostic collects information and provides: An html file ... A compressed file (.zip) that can be transmitted to Alcatel-Lucent Enterprise support for diagnostic"（p523）
> "Port number 389 (LDAPS is not supported), Login cn=directory manager"（p535）
> "For other services don't restart them using the 'Start' button. These services are supervised by NMC service manager and are automatically restarted."（p561）
> "https://nms.company.com/nmclog/ – /nmclog/ is a web alias pointing to log files"（p553）
> "ONCE INVESTIGATION IS DONE, DON'T FORGET TO MODIFY THE TRACETYPE ARGUMENT TO DEFAULT SETTINGS"（p564）

出处：8770XTE200EN p522-567（Maintenance tools、NMC services 讲义与 How-To）。

## I — 自述

排障三件套：采数据（Diagnostic）、查数据（DirManag/HeidiSQL）、管服务与日志（Service Manager/TraceType/nmclog）。

**维护工具箱**

- 8770 Diagnostic：Start > OmniVista 8770 > Tools；交互模式逐步回车或 N 非交互（只需 LDAP 端口 389 + SQL 密码）；产出 C:\TS 下 HTML 报告与 zip（zip 交 ALE 支持开 SR）；采集范围含日志/RestoreContext.ini/服务状态/许可/hosts/计划任务
- DirManag（c:\8770\bin）：LDAP 树浏览/修改——仅 389 明文口（不支持 LDAPS）、登录 cn=directory manager 或 adminnmc、改后 Ctrl+S 保存
- Directory Server Control Center：LDAP 另一入口（admin 登录）
- HeidiSQL（Start > MariaDB 10.5）：TCP 127.0.0.1:3306、用户 dba（默认密码可经 ToolsOmniVista 改）> 选 nmc5 库 > Query 页执行 SQL（输库名. 自动补全表名）；数据文件在 8770\data\data（.frm 定义/.ibd 数据/.TRN/.TRG 触发器）

**NMC 服务两层模型**

- Windows 服务层（Automatic，4 个）：MySQL8770、LDAP Console（DSEE 控制中心）、Oracle Directory Server EE、NMC Service Manager——停了要手动 Start
- NMC 内部服务层（Manual，约 20 个，由 Service Manager 按依赖顺序拉起并监督）：Apache、NMC Alarm/Audit/CMISE/Communication Server/Executable Launcher/Extractor/GCS/Java Service Definition/License Server/Loader/Manage My Phone/PBX-LDAP synchronization/Save-Restore/Scheduler/Security Server/SNMP Service、ORBacus Notify、Wildfly——崩溃自动重启，不要手动 Start
- 依赖规则：服务停则依赖者连锁停，起则连锁起；停 NMC Service Manager 会连锁停全部内部服务
- Service Manager 工具：Select + Execute 取得启停权后再操作；Properties 的 Startup 字段区分两层

**日志体系**

- 位置：NMC 服务 <安装目录>\log（_1.log/_2.log 双文件滚动，合计 10MB 上限=2x5MB）；Apache2\logs；SunONE\slapd-8770\logs
- Web 查看：https://<FQDN>/nmclog/（管理员凭据）
- 详细跟踪：Administration 应用选服务 > Argument list 把 -TraceType 0 改 -TraceType --1——显著变慢且日志变大，查完必须改回 0

## A1 — 书中案例

**诊断与直查实验**（p532-538）：

1. 8770 Diagnostic 非交互模式：输 LDAP 端口 389 与 SQL 密码
2. C:\TS 生成 NMS_周几月日 HTML 与 zip
3. DirManag 连 nms:389（cn=directory manager），树中改值后 Ctrl+S
4. HeidiSQL 建 NMS-MariaDB 会话（127.0.0.1:3306/dba），Query 页执行 select * from nmc5.organization

**服务与日志实验**（p554-567）：

1. Service Manager 取权后停 NMC License Server，观察自动重启
2. 停 NMC Service Manager 看全部服务连锁停，Start 后连锁恢复；四个 Automatic 服务需手动 Start
3. Scheduler 服务改 -TraceType --1，NMCScheduler_1/2.log 体积显著变大，核验后改回 0
4. 浏览器开 /nmclog/ 在线查看 NMCScheduler_1.log

## A2 — 未来触发

使用情境：给 ALE 开 SR 前采数据；直查 LDAP/MariaDB 定位数据问题；服务异常启停；日志撑满或要详细日志取证。

语言信号：8770 Diagnostic / C:\TS / DirManag / HeidiSQL / nmc5 / Service Manager / Automatic Manual / 连锁 / TraceType / nmclog / NMCScheduler / 双文件滚动 / Ctrl+S。

与相邻能力区分：同步/告警日志的业务判读（节点接入/告警卡）；平台装完的服务基线（平台安装卡）；本能力管排障手法与工具。

## E — 可执行步骤

输入契约：故障现象描述、（直查时）目录管理器/dba 凭据、（开 SR）客户支持渠道。

1. 采数据：8770 Diagnostic 非交互模式跑一遍。完成标准：C:\TS 出现 HTML+zip
2. 按现象分流：应用问题查 NMCSyncLdapPbx/NMCFaultManager 等业务日志；数据问题走 DirManag/HeidiSQL 直查
3. 服务面：Service Manager 区分 Automatic/Manual，先等被监督服务自动拉起。完成标准：不误手动 Start
4. 需要详细日志时改 -TraceType --1 复现。完成标准：日志增量可见且问题定位
5. 收尾改回 -TraceType 0 并复核。完成标准：服务性能恢复
6. 远程查看：/nmclog/ 在线读日志。完成标准：免登服务器取证
7. 升级 ALE：zip 交支持渠道开 SR。完成标准：SR 受理

判停点：

- 被监督服务停了 → 先等自动重启再动手，手动 Start 可能造成双实例冲突
- 详细跟踪用完不改回 → 性能持续受损；把"改回 0"写进工单关闭检查单
- DirManag 要加密通道 → 不支持 LDAPS，走跳板机/隔离网段，不要明文跨网
- dba 是只读账户 → 数据变更不能靠它，走应用或 LDAP 工具

输出契约：诊断包（HTML+zip）路径 + 直查记录 + 服务操作日志 + TraceType 复位确认。

## B — 边界

- 维护工具多为底层通道：DirManag 明文 389、HeidiSQL 本机 3306、nmclog 走 HTTP 口——生产使用按客户网络隔离与跳板策略执行
- ToolsOmniVista（密码/SNMP/TLS 底层工具）在安全管理卡覆盖；本卡工具只读/直查为主
- 服务清单约 20 个内部服务为 R5.2 口径，版本演进可能增减；以 Service Manager 实际列表为准
- 实验凭据（superuser/sql 等）见 book/overview；生产改密走 ToolsOmniVista 并纳入密码策略
