# 设备维护日志与 Generic SIP 接入（debug 会话、第三方终端评估）

## R — 原文依据

> "Once a Myriad device is registered and active in the Rainbow Hub environment, it is impossible to connect to it, even if you know its IP address"（p142）
> "require at least the the following firmware on the device: 2.14.22"（p144，原文重复照录）
> "Generic SIP devices: • No centralized configuration • No automatic firmware updates • No remote call control (RCC)"（p117）
> "ALE cannot provide support for such configurations"（p120）

出处：RAINXTE101EN p114-132, p141-145, p334-336。

## I — 自述

两条线：已注册 ALE 话机的维护取证，与第三方 Generic SIP 设备的接入评估。

**ALE 话机维护四口径**（p142-145）：

1. **禁直连**：注册激活后即使知道 IP 也连不上（安全模型）；管理员可开 debug 会话，最长 15 分钟，登录名固定 admin、密码为一次性 TOTP 口令
2. **话机本地取日志**：Log Level 调 Debug / 起 pcap 抓包 / 复现 / Local Log Download 出 .tgz / 停 pcap 下载 / **必须把日志级别恢复 Error 并 Save**（留在 debug 模式话机会行为异常且有延迟）
3. **管理端 webadmin 取日志**：编辑设备 / Enable device logs（24 小时自动失效）/ Get the device report / 报告进 BP report admin 区；前提设备固件至少 2.14.22
4. **远端维护三动作**：Debug / Restart / Reset to factory；debug 开不了且不知管理密码时只能开 SR 走官方支持

**Generic SIP 接入六条限制**（p117/p120）：

1. 无集中配置、必须手工配置
2. 无固件自动更新
3. 无 RCC（不能从 Rainbow 应用控话机）
4. 话机话务状态不回传 Rainbow（无统一在场）
5. DND/呼转/BLF 键状态冲突（本地与集中服务不一致）
6. 仅基础 SIP 话务；协议生态互操作风险

安全基线与配套（p118, p122, p125-131）：

1. 信令 TLS 1.2 起步、媒体 SRTP（设备不支持时可关加密）、推荐 G711；防火墙放行 SIP 信令 + RTP/SRTP + 出网到 Rainbow
2. 手工配置四要素：SIP 域、SIP 用户名、SIP 密码、Rainbow 服务器证书链（编辑设备页下载）
3. 批量导入模板字段：action（create/update/delete）、MAC、设备类型、SIP 密码（仅 Generic SIP 需要）；导入后必须再回连 Rainbow 账号
4. 定位：存量设备补充（门铃/传真/会议话机/ATA/DECT base）；8 款参考设备指南（Yealink/Snom/Poly/Grandstream）；部署前测互操作/编解码/证书，部署后盯注册/音质/收日志

## A1 — 书中案例

**Generic SIP 设备配置操作序列**（p124-131，讲义级操作序列）：

1. Communication/Devices → Create → Device type 选 Generic SIP。
2. 录入 MAC、SIP domain、SIP username、SIP password。
3. 编辑该设备 → 下载 CA 证书链（Rainbow 服务器证书）。
4. 终端侧按支持文章配置网络与 SIP（TLS 1.2+/SRTP，推荐 G711）。
5. 批量线：Import → 填模板四字段 → 上传导出报告。
6. 导入生成的设备再手工（或批量）回连 Rainbow 账号。

书中本章无独立 How-To 实验，验收按部署后清单执行（SIP 注册正常、音质合格）。

## A2 — 未来触发

使用情境：话机要取日志给原厂；话机排障改了日志级别忘恢复；管理端远程取报告失败；客户旧话机/门铃/传真想接 Hub；评估第三方话机当主力终端；Generic SIP 批量开户。

语言信号：设备日志 / device logs / debug / pcap / tcpdump / webadmin / 2.14.22 / TOTP / 恢复出厂 / Generic SIP / 第三方 / SIP domain / 证书链 / TLS / SRTP / G711 / 互操作 / Yealink / Snom / Poly / Grandstream。

与相邻能力区分：ALE 话机的声明与 zero-touch 上线归设备部署能力；开了 SR 之后的支持流程归维护支持能力（路由卡）；"注册不上"先查网络协议支持（HTTP 代理不支持）归网络就绪口径。

## E — 可执行步骤

输入契约：设备型号与固件版本、故障现象与复现步骤、（Generic SIP 线）设备清单与 SIP 四要素、客户对支持责任的理解。

1. 判线：ALE 原生话机走维护四口径；第三方设备先过六条限制评估。完成标准：路径选定且预期对齐
2. 取话机日志（本地线）：Debug 级 / pcap / 复现 / 下载 .tgz / 恢复 Error 并 Save。完成标准：日志在手且级别已复原
3. 取设备报告（webadmin 线）：核固件 ≥2.14.22 → Enable device logs → Get the device report。完成标准：报告出现在 BP report admin 区
4. Generic SIP 接入：建设备（选 Generic SIP）/ 取四要素与证书链 / 终端侧配置 TLS/SRTP/G711 → 回连账号。完成标准：SIP 注册成功、音质抽测合格
5. 批量线（第三方）：模板填 action/MAC/类型/SIP 密码 → 上传 / 回连账号 / 抽检。完成标准：导入报告无红行且注册正常

判停点：

- debug 会话开不了且管理密码未知 → 停，开 SR 走官方支持（p336），不要反复试锁
- 客户要把第三方话机当主力终端大规模上 → 停，ALE 官方立场不支持且不兜底（p120-121，n19）；支持责任与 SLA 先谈进合同
- 清单外型号 → 停，无官方互操作认证计划（n20），先小规模自行试点
- 客户网络全代理出网 → 停，ALE SIP 终端不支持经 HTTP 代理穿越（p334，n52），先改网络再谈终端

输出契约：日志/pcap 证据链（级别已复原确认）+ Generic SIP 接入评估结论与注册验证记录。

## B — 边界

- 已注册话机禁直连是安全设计：排障时间窗按 15 分钟 debug 会话规划（p142，n24）
- 互操作测试与参考设备指南均书外（p117/p122 指针）；本卡不承诺清单外型号可用
- 证书链下载入口在编辑设备页（p127）；SIP 四要素泄露即账号暴露面，按敏感信息管理
- webadmin 设备日志 24 小时自动失效——长周期问题要在失效前重新开启（p144，n26）
- 设备 debug 的 TOTP 口令与认证 TOTP 同词两义（g06），文档表述时按上下文区分
