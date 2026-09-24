# RTR 许可开关：资格期状态机、事件监控与 FlexLM 互斥

## R — 原文依据

> "A grace period of 30 days is initiated by default ... OK: the remaining Qualifying Period is increased of 0,5 day to the limit of 30 days • NOK: the remaining Qualifying Period is decreased of 1 day to the limit of 0 day"（p304）
> "FOR COMMUNICATION SERVERS RUNNING ON VIRTUAL MACHINES, VERIFY THAT LICENSING VIA FLEXLM SERVER IS NOT ACTIVATED. THE TWO LICENSING MODES (FLEXLM SERVER AND CCI/RTR) CANNOT RUN AT THE SAME TIME"（p331）
> "Both OXE Systems with the same CC Product ID will decrease their remaning Qualifying Period simultaneously ... Pin code generation will remove both recording on RTR server"（p307）
> "647 RTR state, with additional information such as cause and remaining qualifying period 648 Raised when the PBX switches into panic after 30 days"（p334）

出处：ENTPXTE402EN p302-308、p331-337。

## I — 自述

RTR（Right To Run）是 dongle-less 许可总开关：不用硬件标识/加密狗，每日经 XMPP 向 RTR 服务器应答——OK 加 0.5 天（上限 30）、NOK 减 1 天（下限 0）；它不替代产品级 swk 许可，只是总开关。

资格期归零触发 Panic Flag：系统进 deprecated 模式，话机建立通话时显示 "Call your administrator"，数据库与电话服务拒绝一切配置变更。

Fleet Dashboard 状态判读（由"最后连接日期+剩余资格期"计算，数据库每晚更新）：

| 状态 | 判据 | 通知/后果 |
|---|---|---|
| Connected | 24h 内有连接，或剩余 29-28 天 | 正常 |
| Qualifying | 超 24h 无连接且 27-10 天 | 27 天、20 天各发一封状态邮件 |
| Soon Blocked | 9-1 天 | 每日邮件；事件计数增加 |
| Blocked-Panic | 0 天 | Panic Flag 已挂起，须 PIN 恢复 |
| Not connected | 未注册 RTR | — |
| Duplicated | CC Product ID 被另一系统占用 | 两侧同时扣减，须 PIN 恢复 |

关键事件码（incvisu 查看）：

| 事件 | 含义 |
|---|---|
| 6207 / 6208 | XMPP 链路登入 / 登出 |
| 6205 / 6209 | WebSocket 连不上 / SOCKS5 建立失败 |
| 6214 | 自动 FTR 未成功（由 6207 清除） |
| 647 | RTR 状态（含原因与剩余资格期） |
| 648 | 30 天后进 panic |
| 649 | PIN FTR 已执行、退出 panic |
| 650 / 651 | 欺诈检测立即 panic / 清除 650 |

操作抓手：

- CCTool 2 读状态：Service state=RTR_RUNNING、CCI mode、Remaining Qualifying Period、Response Code、Cause Message、Next Request Date；选 1 Force RTR 可立即请求
- 启用路径在 WBM System/Licenses：FlexLM Enabled=No + Cloud Connect RTR Enabled=Yes，改后重启一次
- 持久性：Save/Restore 保留资格期值跨重启；值自动同步 twin CS
- Duplicated 场景（克隆虚机/复制磁盘把 CC 身份带走）：PIN 生成会移除 RTR 服务器上两侧记录，只有用 PIN 完成重注册的系统恢复 30 天资格期

## A1 — 书中案例

**RTR 启用与监控**（p331-332，How-To）：

1. WBM System/Licenses 核对 FlexLM Licensing Enabled=No
2. Cloud Connect RTR Enabled=Yes，按 Tips 重启 OXE
3. CCTool 2 读 Service state=RTR_RUNNING、CCI mode=CCI_NORMAL
4. Remaining Qualifying Period=30.0、Response Code=201 为健康态
5. 需要立即对账时选 1 Force RTR
6. 日常用 incvisu 跟 647/648/649 事件，CCTool 4 按特性调日志级别

## A2 — 未来触发

使用情境：话机显示 "Call your administrator"；资格期一直在掉；虚机上能不能 FlexLM 和 RTR 并用；Fleet Dashboard 显示 Duplicated；想立即刷新 RTR 状态。

语言信号：RTR / Right To Run / Qualifying Period / 资格期 / dongle-less / Panic Flag / Call your administrator / Soon Blocked / Duplicated / Force RTR / 647 / 648 / 649 / FlexLM 互斥 / deprecated mode。

与相邻能力区分：

- FTR 注册与连通性前提 → 云连接卡
- 云端 Dashboard 操作（Inventory/Offer/远程控制台） → 机队服务卡（路由）
- LMS 订阅消耗与 panic → 订阅许可卡

## E — 可执行步骤

输入契约：FTR 已 Registered（前提）、FlexLM 使用状态、RTR Enabled 目标值、管理邮箱（收分级通知）。资格期已归零 → 判停直接走 PIN 恢复，别再等自动恢复。

1. 互斥核对：WBM 确认 FlexLM Licensing Enabled=No（虚机必须）。完成标准：单一路径确认
2. 启用 RTR：Cloud Connect RTR Enabled=Yes，按提示重启 OXE。完成标准：重启完成
3. 状态判读：CCTool 2 核 RTR_RUNNING、CCI_NORMAL、Qualifying Period=30.0。完成标准：健康态确认
4. 监控布防：incvisu 订 647/648/650；管理邮箱收 27/20 天分级邮件。完成标准：告警链路就位
5. 异常处置：断连查 6205/6209 与网络前提；Duplicated 立即走 helpdesk PIN。完成标准：处置路径明确
6. 例行对账：需要时 Force RTR 立即刷新状态。完成标准：资格期回升（+0.5）确认

判停点：

- 虚机上 FlexLM 还开着 → 停，两种模式互斥，先关 FlexLM 再启 RTR
- RTR 请求失败想连续重试 → 停，按保守口径当日即可能扣 1 天（重试双口径见 nr-01），先修网络
- Fleet Dashboard 出现 Duplicated → 停，两侧同时在扣天数，立即申请 PIN，别等归零
- 想用 RTR 替代 swk 产品许可 → 停，RTR 只是总开关，产品许可照旧

输出契约：RTR 运行状态基线（资格期/状态/事件订阅）+ FlexLM 互斥核对记录 + Duplicated 应急预案。

## B — 边界

- RTR 重试行为教材两处口径不一（p308 与 p332，nr-01）：监控按"当日即可能扣减"设计，最终以 ALE 最新 TC 为准
- VAD 可把子机队委托给 IR 管理（Fleet Dashboard 委托关系，p305，书中仅此一处）
- 日志抓手：/tmpd/CCAlarm.log 含 647 逐日条目；ccagent.log 看 STATE_CONNECTED/DISCONNECTED
- 事件码表为 Ed12 口径；LMS 侧事件 652/653/654 属订阅许可卡
