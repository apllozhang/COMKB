# OTFC 服务架构与日常运维（有状态/无状态、Services Status、xmsc、日志与 SIP 日志）

## R — 原文依据

> "Stateful (Replicated) Services/Components • XMFaxManager • XMConfigManager • XMCoConfig • XMFaxArchive • XMFaultTolerance ; Stateless (Load Balanced) Services/Components • XMFaxDriver • XMDocumentRasterizer • XMSmtpGateway • XMXmlGateway"（p179）
> "Restarting Services … xmsc –ra • Stopping Services … xmsc –oa • Starting Services … xmsc -aa"（p188）
> "Each OTFC component has a dedicated log file. Log files location: • C:\Program Files\Alcatel-Lucent Enterprise\FaxCenter\Trace"（p189）
> "Log Size (default is 20 MB) • Archive Retention Period (default is 15 Days)"（p225）

出处：OTFCXTE200EN p176-191、p225。

## I — 自述

服务架构决定运维动作，三层模型一张图：

1. **三层模型**：模块（安装单元）→ 服务（Windows 服务，可经服务管理单元管理）→ 组件（经管理界面 Services Status 监控）
2. **四大模块**：Fax Manager Module（系统心脏，含五个组件）；Fax Driver Module（H.323/SIP 收发，可并行多路）；Rasterizer Module（借本机 Office 转传真 TIFF）；SMTP Gateway（监听 25 收作业发通知）

3. **组件分工**：XMFaxManager 管收发队列、分发任务、管媒体库；XMCoConfig 管站点配置；XMConfigManager 管系统配置；XMFaxArchive 存传真记录；XMFaultTolerance 监控故障与监督切换
4. **有状态/无状态**：有状态 5 个（复制，持有配置/未决事务/历史）；无状态 4 个（可负载均衡的工作组件，含 XMXmlGateway）
5. **三通道运维**：查状态走 Web 管理/MMC 的 System Monitor ➤ Services Status；启停走 Windows 服务菜单；脚本化走 Bin\Util 下的 xmsc -ra（重启）/ -oa（停止）/ -aa（启动）
6. **日志体系**：每组件一个专属日志，统一在 FaxCenter\Trace；默认单文件 20MB、归档保留 15 天，满后 zip 进 Archive；SIP 日志两步用法——管理界面激活"日志中记录 SIP 消息"，再按需调级别

来传真通知/路由故障的高频落点：ConfigManager.log 与 Smtp.log。

## A1 — 书中案例

**备份前置的服务检查**（p231，实验 8 开头步骤）：

1. 经管理界面 System Monitor ➤ Services Status 确认所有组件 Active
2. 命令行进 C:\Program Files\Alcatel-Lucent Enterprise\FaxCenter\Bin\Util
3. 执行 xmsc -oa 停全部传真服务（备份动作转备份升级能力）

**SIP 日志激活**（p190-191，讲义口径）：

1. 管理界面进入 SIP 配置相关页
2. 激活"日志中记录 SIP 消息"（三步操作）
3. 按需调日志级别控制信息量，复现问题后回读 Trace 目录日志

## A2 — 未来触发

使用情境：改完配置要不要重启服务；某个组件状态不是 Active；传真转换卡住疑 Rasterizer；日志把磁盘写满；要看 SIP 信令；邮件通知不到要翻日志。

语言信号：服务 / services / Services Status / XMFaxManager / FaxDriver / Rasterizer / XMSMTPGateway / XmlGateway / 有状态 / stateful / 无状态 / stateless。

语言信号（续）：xmsc / 重启 / Trace / 日志 / log / 20MB / 15 天 / SIP 日志 / ConfigManager.log / Smtp.log。

与相邻能力区分：备份/恢复/升级窗口内的服务停起归备份升级能力；转换失败的根因（Office 弹窗）归首次交付能力；OXE 侧抓包归 SIP 通道集成能力。

## E — 可执行步骤

输入契约：管理界面或服务器本地管理员权限、问题现象（哪个组件/什么操作后出现）、维护窗口（重启影响收发）。

1. 定位组件：按流水线分段（提交/转换/发送/通知/归档）判断可疑组件。完成标准：可疑组件锁定
2. 查状态：System Monitor ➤ Services Status 逐组件核对 Active。完成标准：异常组件确认
3. 启停操作：单服务走 Windows 服务菜单；全量走 xmsc -ra 重启 / -oa 停止 / -aa 启动（Bin\Util 目录）。完成标准：组件恢复 Active
4. 翻日志：Trace 目录按组件找专属日志；通知/路由问题优先 ConfigManager.log 与 Smtp.log。完成标准：找到关键报错行
5. 调日志（如需深查）：System Administrators 经管理界面调日志大小与保留期；SIP 问题先激活 SIP 消息日志再调级别。完成标准：目标信令/事件被捕获
6. 收尾：日志调回默认口径（20MB/15 天），确认无新增异常。完成标准：系统回到基线

判停点：

- 组件反复掉 Active → 停，抓专属日志报错根因（依赖/端口/许可），不要循环重启掩盖问题
- 转换环节卡死 → 优先怀疑 Office 未预初始化弹窗（首次交付能力的坑位），再查 Rasterizer 日志
- 计划重启撞上收发高峰 → 停，约维护窗口；xmsc -oa 会停掉全部传真服务，影响面先讲清
- 需要 XML 网关排障但书内只有组件名 → 停，XMXmlGateway 书内仅列入无状态清单，细节转产品文档

输出契约：组件状态核对表 + 启停操作记录（时间/命令/结果）+ 日志摘录（关键报错行）+ SIP 日志捕获文件（如适用）。

## B — 边界

- XMFaultTolerance 只作组件介绍（监控故障/监督 failover），高可用怎么部署、怎么演练全书零实操
- 日志默认值 20MB/15 天为 R9.2 口径；日志大小与保留期仅 System Administrators 可改
- xmsc 三命令在 <install_path>\FaxCenter\Bin\Util 下执行；参数与书内实验口径一致（含 mysql5 服务名）
- 有状态组件的复制机制是架构概念，书中未给"复制怎么配"的路径——HA 需求转产品文档
- 组件间两张交互图（p184-185）为讲义图示，本卡按文字口径转写，未逐线复绘
