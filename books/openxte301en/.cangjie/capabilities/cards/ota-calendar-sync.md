# 日历在场与日历同步（Calendar presence / Calendar synchro）

## R — 原文依据

> "Calendar information is an additional text message added next to the user presence status ... The color code is not modified by the calendar presence information"（p387）
> "the following precedence on the five calendar states: Out of Office > Busy > Tentative > Working Elsewhere > Free"（p389）
> "Recurrent meetings created from OTC client are not pushed into Exchange."（p392）
> "IF USERS HAVE LOCAL STORAGE MAILBOXES, PLEASE HAVE A LOOK TO THE TECHNICAL DOCUMENTATION 'TC 2558'"（p395）

出处：OPENXTE301EN p384-414（含 TC2258 附录）。

## I — 自述

两个机制共用 UM 的配置底座（ICEaccess+Impersonation+证书+邮件服务器），但行为不同：

1. **Calendar presence（在场旁注）**：从 Exchange/O365 取日历状态，作为在场旁注文本（如 "Busy – In a meeting until 11:00"）；不改颜色码、自己看不到自己、FREE 状态只在联系人名片（二级界面）显示；多日程重叠按 OOO>Busy>Tentative>Working Elsewhere>Free 取值
2. **展示公式（TC2258）**：endTime 按 ISO 8601 UTC 存储、按终端 locale 展示——结束在今天显示 "until HH:mm"（美区带 AM/PM），明天及以后显示 "for the next hours"；时区差异常被误报为"时间不对"
3. **Calendar synchro（双向同步）**：OT 侧 Wireal 组件经 EWS 代用户建/改/删 Exchange 约会——Outlook 建会自动进 OTC、OTC 建会自动进 Outlook 并发邀请；不对称限制：OTC 建的周期会议不推送 Exchange，Outlook 建的可以
4. **开关两级**：邮件服务器上勾 Activate calendar presence service 与 Activate conference synchronization service（改后 service wireald restart）；用户级经 Outlook 端 Free/Busy Read 权限控制（Read=None 即全局停用，默认开启）
5. **版本门槛**：presence 自 OT R2.3.1（依赖 Impersonation）；synchro 仅 Exchange 2010/2013/O365、Outlook 仅 2010/2013；每用户须有会议许可

排障三板斧：重启 tomcatd/acsd/wireald → 看 exchange-connector 与 wireal 日志 → 查 /tmp/exchange-connector-que* 三个队列目录。

## A1 — 书中案例

**日历特性实施与验证实验**（p394-399，配 TC2258）：

1. 判型：确认用户为 UM 上下文（本地存储邮箱改走 TC2558）
2. 前提核对：同 UM（特权账号/Impersonation/证书/邮件服务器已声明）
3. 核对邮件服务器两开关并勾选
4. 在场测试：Alban 的 Outlook 建今天 15:30 约会，Barkley 的 OTC PC 查看其日历在场文本
5. 同步测试：Barkley 侧建今天 16:00-19:00 会议，核对 Outlook 与 OTC 双侧出现
6. （TC2258）改开关后 service wireald restart 生效
7. 排障演练：重启三服务、查四类日志、用 $WIREAL_HOME/bin/client 看 calendar:users 与队列目录

## A2 — 未来触发

使用情境：让同事的会议状态显示在 OT 里；Outlook 与 OTC 的会议互通；"日历在场没生效"类报障；周期例会要不要从 OTC 建；免费/忙碌发布权限管控。

语言信号：日历 / calendar / 在场 / presence / Free/Busy / 忙碌 / synchro / 同步 / Outlook / Exchange / Wireal / wireald / exchange-connector / TC2258 / OOO / Out of Office / until HH:mm。

与相邻能力区分：UM 留言进邮箱 → 统一消息能力（配置同源）；会议邀请邮件里的桥号与 One Touch → 协作会议能力。

## E — 可执行步骤

输入契约：用户邮箱类型（UM 或本地存储）、Exchange/Outlook 版本矩阵、OT 版本（≥R2.3.1）、每用户会议许可。

1. 判型与版本核对：UM 上下文、Exchange 2010/2013/O365、Outlook 2010/2013。完成标准：不满足项书面确认（本地存储走 TC2558）
2. 前提复用 UM：ICEaccess/Impersonation/证书/邮件服务器。完成标准：UM 验证已通过
3. 勾两开关并重启 wireald。完成标准：服务正常
4. 在场验收：按"自己看不到自己、FREE 仅名片、不改颜色、OOO 优先"四条口径测。完成标准：预期差解释到位
5. 同步验收：Outlook 建会与 OTC 建会各测一轮（周期会议从 Outlook 建）。完成标准：双向可见
6. 验收脚本文案按展示公式写（locale/AM-PM/until 与 for the next hours）。完成标准：文案口径一致

判停点：

- 用户报"看不到自己的日历状态" → 设计如此（只能看别人），不是故障
- "显示 Busy 但我请了假" → 优先级规则：OOO 才压过 Busy，Tentative 不压
- 队列目录出现 -que-failed 积压 → 按排障三板斧走，必要时 dla.sh 开调试并收集日志开 eSR
- 版本不满足（如 Exchange 2016、Outlook 2016+）→ 停，按版本矩阵谈方案，不硬配

输出契约：判型与版本核对单 + 两开关配置记录 + 在场/同步验收结论（含预期差解释）+ 排障记录（如有）。

## B — 边界

- 本章流程仅适用 UM 上下文；本地存储邮箱必须改走 TC2558，按错流程配不出来（n32）
- 2019 年口径：synchro 未列 Exchange 2016+、Outlook 仅 2010/2013——交付前按客户版本矩阵重核（n34/nr-07）
- presence 需 OT R2.3.1+ 且依赖 Impersonation；深度机制以 TC2258 为准
- 实验值（Alban 15:30 约会、Outlook barkley/1234）为实验口径
