# 外呼闭锁与紧急呼叫（Area、Public COS、紧急通知、Location ID）

## R — 原文依据

> "8 Logical discriminators are available for the system • 256 different Real Discriminators can be managed • 64 areas are available … 32 Access Classes Of Service"（p660）
> "THE STATE (NIGHT, DAY, MODE 1, MODE 2) ARE THE ENTITY'S STATE. BY DEFAULT, AN ENTITY IS IN THE STATE NIGHT."（p674）
> "Maximum 100 emergency notifications can be queued (FIFO mode) • Feature available only for stand-alone systems … Maximum 10 devices in the system emergency group"（p683）
> "THE USE OF DIRECT IP LINKS BY THE SYSTEM IS A MANDATORY PREREQUISITE FOR SENDING LOCATION ID."（p693）

出处：ENTPXTE400EN p657-699, p604-607。

## I — 自述

外呼闭锁与紧急通知共用同一套鉴别符/Area 骨架：

1. **闭锁三要素**：外呼权限=Area（号码分区）×Public COS（32 类，四实体状态列放行矩阵）×Entity 状态的交点检查；用户挂 Public COS、外呼号码落 Area、实体当前态决定放行列
2. **鉴别符链**：ARS 前缀挂逻辑鉴别符（0-7）→ 实体选择器映射真实鉴别符（0-255，必须已存在才能关联）→ 真实鉴别符规则把号段（如 00/06/07）划入 Area（1-64）
3. **默认值**：实体默认 Night 态——只开 Day 列不放行是最高频错；默认 Public COS 2 仅 Area 1 全放行
4. **换 Entity 的连带**：改用户实体会换鉴别符选择器映射，闭锁行为随之变化（p667 Warning）
5. **紧急通知四要素**：系统参数定紧急 Area（1-64，0=关闭）；紧急号划入该 Area 且 Public COS 放行；紧急组（全系统 1 组、≤10 台 ≥3 行显示的 NOE 商务话机/IPDSP，仅 business 模式，stand-alone only、需 ARS）
6. **通知与位置**：判定为紧急后组内设备收 Tone 34+弹窗（动作仅 Clear/Snooze 20 秒/Callback），EMG log 查 ≤100 条 FIFO；Location ID（P-ANI）取值源在 NPD（None/NPD/Entity/IP domain 四级），强制前提=系统启用 Direct IP Link

## A1 — 书中案例

**外呼闭锁实验**（p669-681，How-To）：

1. 核对用户 Entity=1、Public COS=2，ARS 前缀逻辑鉴别符=0
2. 核对实体选择器映射与鉴别符 0-public 的 Area 分区
3. 基线拨测：紧急/国内/移动/国际全通（全在 Area 1）
4. 禁国际：把 00 移入 Area 2，拨 0044 被拒
5. 禁移动：06/07 建入 Area 3，拨 06/07 被拒且国内不受影响
6. 放行：Access COS 2 的 Area 2/3 四状态全 1（提醒实体默认 Night 态）
7. 换 COS 与换 Entity 各复测一次，确认权限面与鉴别符面独立生效

**紧急呼叫实验**（p689-699，How-To）：

1. 紧急号 112/15/17/18 划入 Area 64 且四状态放行，系统参数 Emergency numbers area=64
2. 基线抓包：呼 112 时 INVITE 无 P-Access-Network-Info
3. 系统启用 Direct IP Link（强制前提）
4. NPD 的 Location ID Source=Entity，实体 1 填位置串
5. 网关 P_ANI Header 选 Emergency only
6. 复测呼 112：INVITE 出现 P-ANI 头，普通呼叫不携带
7. 建紧急组并验证 Tone 34、弹窗、Snooze/Callback/Clear 与 EMG log

## A2 — 未来触发

使用情境：限制部门/客房外呼；防盗打加固；"明明放行了还打不出去"；紧急事件要通知保安台；合规要求外呼带位置信息；紧急号码显示问题。

语言信号：闭锁 / barring / Public COS / Access COS / Area / 区号 / 鉴别符 / discriminator / 实体状态 / Night / 紧急呼叫 / emergency / 紧急组 / P-ANI / Location ID / 位置。

与相邻能力区分：功能级权限（能否呼转/强插）见编号计划与 COS 能力；外呼走的 SIP 中继链路见 SIP 中继能力；紧急号码的 ARS 表配置见 SIP 中继能力。

## E — 可执行步骤

输入契约：客户外呼权限矩阵（谁可打哪类号）、紧急事件响应流程（通知谁/用什么设备）、运营商 Location ID 格式要求（如需外发）。

1. 盘点现状：用户 Entity/Public COS、ARS 前缀鉴别符、实体选择器、Area 分区表。完成标准：四层现状成文
2. 分区：按号码段设计 Area（如国际/移动/本地分开），真实鉴别符规则先行建好。完成标准：拨测号码落对 Area
3. 授权：Access COS 按 Area×四状态填放行矩阵，注意实体默认 Night 态。完成标准：各 COS 拨测与权限矩阵一致
4. 紧急区域：紧急号划专用 Area 并全状态放行，系统参数 Emergency numbers area 启用。完成标准：紧急号在闭锁下仍可拨
5. 紧急组与位置：建组（≤10 台商务设备），按需配 Location ID 链（Direct Link/NPD/实体值/网关开关）。完成标准：紧急呼叫触发通知，P-ANI 复测达标
6. 回归：改 COS/换 Entity/切实体状态三组对照拨测。完成标准：行为与设计表一致，紧急通路不受闭锁影响

判停点：

- Area 放行了还打不出去 → 先查实体当前状态列（默认 Night，n25），再查用户挂的 COS ID
- 想给逻辑鉴别符映射一个新真实鉴别符 → 必须先建真实鉴别符（n26），顺序不可倒
- 客户是多节点/PCS 组网要紧急通知 → 停，仅 stand-alone 单节点支持（n31），转组网方案评估
- 紧急呼叫不带位置 → 逐项查 Direct IP Link 启用、NPD 取值源、网关 P-ANI 开关（n32），任一缺失即不外发

输出契约：受控的外呼权限矩阵 + 紧急通知链路（组/区域/位置）+ 拨测记录。

## B — 边界

- 实验号段（0044/06/07、紧急 112/15/17/18 的回叫规则）为 ITSP1 模拟器口径（n29），生产按运营商与当地合规
- 紧急通知仅 stand-alone、需 ARS、组 ≤10 台 business 模式设备（n31）；客房/坐席/话务台/DSS 设备不收通知
- Location ID 仅 SIP 中继外呼携带；≤N2 异构网络自动弃用但不掉话（p605）
- 紧急号码显示管理随运营商而异（n29），Location ID 外发格式按运营商定义
- 本卡不覆盖 ACD/坐席级外呼管控
