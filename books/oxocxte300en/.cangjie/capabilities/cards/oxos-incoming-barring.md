# 呼入分发与呼出闭锁（话务台组 / 时段表 / 三层限制）

## R — 原文依据

> "The normal / restricted mode is used for INCOMING calls distribution • 2 DDI numbering plans • One for normal mode, another for restricted mode"（p254）
> "An attendant group is always in parallel mode."（p264）
> "6 barring tables = 6 levels of barring"（p274）
> "disable the parameter "Inhibition Time-ranges", so that extensions follow Normal/restricted mode defined in time ranges."（p283）

出处：OXOCXTE300EN p252-291（呼入管理九页讲义+实验、出局管理十一页讲义+闭锁实验）。

## I — 自述

**呼入分发**（谁在什么时间接电话）：

- 话务台组（OMC/Attendant groups）：成员可为分机、MSG1-20、General bell、VM 端口（拼自动话务员）；组永远并行（齐振）模式
- Normal/Restricted 双 DDI 计划支撑日夜切换：手动话务台 N/R 键或 Time Ranges 按时段自动切组
- 时段表（OMC/Time Ranges）：End 列是派生值，改某段结束时间必须改下一行 Start（n17）
- 话务台转移：Attendant diversion 功能键转集体缩位号，受话务员密码保护（n18）
- 预公告：每时段配模式（无/分发前播完再振/分发中边播边振）+消息号 1-20+仅忙旗标；个人问候 200 条、消息 20 条、总 320 秒

**呼出闭锁**（谁能拨什么）三层判定：

- 第一层 Traffic sharing：用户 LC × 中继组 LC 查矩阵，交点为“+”即可占、空白即禁占（默认 LC=12，12∩12=空即默认禁外呼）
- 第二层 Barring：用户 Barring LC 经矩阵定位用哪张闭锁表（6 张=6 级）；表内前缀 Authorized/Forbidden，digit counter 控位数；国际 00 默认全表 Forbidden
- 第三层路由：主中继组 0/副中继组 #/ARS 表
- 关键坑：默认用户不跟随时段——必须逐话机关闭 Feature Rights Part 2 的 Inhibition Time-ranges，否则时段限呼不生效（n19）
- 多 DDI 段：noteworthy 地址 DDIonPRI 支持按所用中继线选 DDI 段发送（T0/T2/模拟/VoIP 全适用）

## A1 — 书中案例

**呼入分发实验**（p262-269）：

1. 建组 1：加分机 100、101；组 2 只加 MSG1（工作时段提示音）
2. Time Ranges/Monday：8am-7pm 活动组 1、7pm-8am 组 2，复制到周二至周五
3. 周末页签配置后复制到 Sunday 与 Public Holidays（仅组 2）
4. 话务台建 Attendant diversion 键，目标集体缩位号（话务员密码保护）
5. 全局预公告：Preannouncement Overview → Global Greetings → 时段 1 配 Before call distr.+MSG2
6. 验收：改系统时间测试——营业时间振组 1、非营业时间听 MSG1、来电先播 MSG2 再转

**呼出闭锁实验**（p281-291）：

1. Time Ranges 建 4 时段：营业时间默认 LC 可占、非营业默认禁占
2. 逐话机关 Inhibition Time-ranges（Feature Rights Part 2），否则话机恒 normal（n19）
3. 副中继组：功能 Secondary trunk group 改 start=401/base=2，再建 start/end=#、base=1
4. 中继组 2 加 SIP VoIP 接入，Link-Cat. 保持默认 12
5. 授权一个用户：其 Traffic Sharing LC 改 5，矩阵查 5∩12=+（放行）
6. 国际闭锁：表 2 加前缀 0053 类型 Authorized；全员 Barring LC 改 2
7. 核对：Barring Matrix 行 2 列 1=2；验证国际禁呼、0053 可呼

## A2 — 未来触发

使用情境：客户要"下班后电话走留言"；节假日自动切换；只放行个别用户外呼；禁国际但放行某国；"限呼配了不生效"排障。

语言信号：话务台组 / attendant group / 时段 / time ranges / 日夜切换 / Normal / Restricted / 预公告 / preannouncement / 闭锁 / barring / 闭锁表 / Link Category / 矩阵 / traffic sharing / DDIonPRI。

与相邻能力区分：中继本身不通 → SIP 中继能力；MSG 消息内容制作 → 消息彩铃卡。本能力到"呼入按时段分发+出局权限可控"为止。

## E — 可执行步骤

输入契约：采集表的呼入呼出块（组/时段/欢迎语/权限矩阵）、已注册的 SIP 中继。业务口径未确认 → 判停先确认（权限错了会封住客户外呼）。

1. 建话务台组：加分机/MSG/VM 端口。完成标准：组号可呼且齐振
2. 配时段表：逐日建段（End=下一行 Start），复制到周末假日。完成标准：改系统时间实测切组
3. 配预公告：按段选模式/消息/仅忙旗标。完成标准：来电先闻提示再转
4. 话务台转移键：绑集体缩位号，话务员密码纳入管理清单。完成标准：N/R 转移生效
5. 配出局三层：先定 Traffic sharing（谁能占组）→ 再定 Barring 表与 LC → 最后核对矩阵。完成标准：授权用户可呼、其余被拒
6. 关联时段限呼：逐话机关 Inhibition Time-ranges。完成标准：非营业时间实测禁占
7. 特例：副中继组 #、DDIonPRI 按中继线选段（需要时）。完成标准：拨 # 走副组、外呼送对 DDI 段

判停点：

- "限呼不生效" → 先查 Inhibition Time-ranges 是否逐话机关闭（n19），再查时段 End 值（n17）
- 默认全员禁外呼是设计行为（LC 12∩12=空），授权靠改用户 LC，不是改中继组
- 国际默认禁——放开某国=在指定表加该国前缀 Authorized，不要整表翻绿
- 话务台转移键改不了 → 受话务员密码保护，用管理员权限（n18）

输出契约：呼入时段矩阵 + 出局权限矩阵（用户×时段×目的地）+ 拨测记录。

## B — 边界

- 实验业务口径（拨 9 出局、禁国际等）为样例，生产按客户权限矩阵裁剪（p31）
- Barring 矩阵交点与 digit counter 的完整算法口径在 Expert 文档，书内给判定框架与实例
- 时段粒度与假日表（Public Holidays）按客户日历维护，书外流程
- DDIonPRI 需启用 noteworthy 地址，默认关闭
