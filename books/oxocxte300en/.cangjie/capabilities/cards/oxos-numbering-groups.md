# 编号计划与四种组（拨号地基 / hunt・代接・广播・经理秘书）

## R — 原文依据

> "PUBLIC DIALING PLAN … PRIVATE DIALING PLAN … INTERNAL DIALING PLAN … FEATURES IN CONVERSATION"（p124）
> "DDI number 41100 – Base 100 … Directory number 100 – Base 100"（p128）
> "Base Always a number from 0 to 2199"（p135）
> "Warning: the group 500 is used by the voice mail server!"（p143）
> "Create a manager/secretary group, the two sets must be multiline sets."（p155）

出处：OXOCXTE300EN p123-156（编号计划讲义与实验、组管理讲义与实验）。

## I — 自述

**编号计划**是全部呼叫功能的寻址地基：

- 四层：公共（DDI）、专用（私网）、内部（分机）、会话中功能（后缀）；默认三位计划（分机 100 起、9 话务台、0 主中继组）
- Base=内外映射基数：DDI 41100 base 100 ↔ 分机 100；取值域 0-2199；安装号=主系统 DDI 号去第 1 位录入
- Pick-up 族与 Forwarding 族前缀的 Base 语义固定不可改（组代接=1、立即前转=1 等，f17）
- 建新段范式：先查冲突旧段（编程模式 200-299、副中继组 400-434、6 开头前缀等）→ 删 → 再建（f18）
- 规划技巧：分机段收缩为 100-149，把 150-199 留作其它功能（p134）

**四种组**各管一件事：

- **Hunt group**：多话机共用一号，Sequential 逐个 / Circular 轮转 / Parallel 齐振；组 500 固定被语音信箱服务器占用，从 501 起用（n07）
- **Pick-up group**：组内代接，靠代接前缀或功能键（作用域选 Group）
- **Broadcast group**：成员分 send/receive/send+rec 权限，接收话机必须有扬声器；PairedGrb 可配对 2 组合计 64 人
- **Manager/Secretary**：双方必须 multiline 话机，互持 RSL/Screening/监督三键

## A1 — 书中案例

**编号计划实验**（p131-135）：

1. 编程模式前缀 20：删既有段 200-299，功能选 Programming Mode，填 20/20、Base 空 → Add
2. 话机代接前缀 21：功能选 Pick Up → 21/21、Base=0（话机代接）→ Add
3. 分机段收缩：Subscriber 行 100-199 改 end=149、Base 留 100 → Modify
4. 缩位 400-499：删副中继组 400-434 与 Appointment 60 → Collective Speed Dial、Base=0 → Add
5. 缩位 600-699：删全部 6 开头前缀 → 600-699、Base=100 → Add
6. 验收：无冲突段、Base 合法、旧业务无依赖

**Hunt group 实验**（p142-145）：

1. OMC/Hunting groups → 选组 501 → Details（500 被 VM 占用，勿用）
2. 加成员 101、102，组名 Welcome，类型 Sequential → OK
3. 拨 501 验证按类型分发；再改 Cyclic 与 Parallel 复测
4. （注）讲义用 Circular、实验用 Cyclic，同指轮转（needs-review nr-03）

**Pick-up 组实验**（p146-150）：组 1 加 101-103；每组员建 Function key → Pickup 键、作用域 Group；呼 102 振铃时 101 按键代接。

**Broadcast 组实验**（p151-153）：组 1（号 *2）加 101=Send、102/103=Reception → 101 拨 *2，接收方扬声器出声；无扬声器话机用 IPDSP 接收替代。

**经理-秘书实验**（p154-156）：Manager-Secretary Relations → Add，选经理 101/秘书 102（均 multiline），配 RSL/Screening/监督三键；虚课只配不测。

## A2 — 未来触发

使用情境：设计客户拨号方案；建新前缀段报冲突；hunt 组电话轮不过来想改分发方式；要一个喊话/通知组；老板要秘书过滤电话。

语言信号：编号计划 / numbering / 前缀 / 后缀 / Base / 安装号 / 缩位拨号 / hunt group / Sequential / Circular / Parallel / 代接 / pickup / 广播 / broadcast / 经理秘书 / manager secretary / multiline。

与相邻能力区分：组里成员的功能（前转/插入）→ 用户功能能力；呼入按时段进不同组 → 呼入分发与闭锁能力。本能力到"寻址与组业务可用"为止。

## E — 可执行步骤

输入契约：数据采集表的编号与组块、既有系统导出库（扩容时）。改前缀前未确认旧段业务依赖 → 判停先核对。

1. 定编号框架：三位计划、分机段、话务台、主中继组、hunt 段、DDI 与 Base。完成标准：与采集表一致且无冲突
2. 清冲突：查并删除冲突旧段。完成标准：目标段可用
3. 建段：下拉选功能 → 填起止与 Base → Add。完成标准：计划表无重叠
4. 建 hunt 组：从 501 起选组、加成员、选分发类型。完成标准：拨组号按预期分发
5. 建 pick-up 组与代接键（作用域 Group）。完成标准：振铃中可代接
6. 建广播组：设 send/receive 权限，核接收方扬声器。完成标准：拨组号扬声器出声
7. 建经理-秘书组：双方 multiline，配 RSL/Screening/监督键。完成标准：滤键与监督键生效（物理机环境）
8. 拨测矩阵：组号/代接/广播/经理秘书逐项打通。完成标准：验收清单闭环

判停点：

- Base 超出 0-2199 或与固定语义冲突 → 改方案，不硬配
- 客户要"语音信箱组"占用 500 → 拒绝并解释保留原因（n07）
- 经理或秘书不是 multiline 话机 → 先换终端再建组（n09）
- 接收方话机无扬声器 → 广播只配 send 或换终端，如实告知验收限制（n08）

输出契约：编号计划表（段+Base+后缀）+ 四类组清单与拨测记录。

## B — 边界

- 计划默认值随安装国家变化；书内无真实客户编号方案案例，"怎么规划"需按项目经验补
- 安装号/话务员 DDI 实验值两口径见 needs-review nr-02
- 组号范围 500-525 为默认计划口径，改计划后随之变化
- 后缀（会话中功能）族仅给入口（OMC/Numbering/Feature in Conversation），完整功能码表在 Expert 文档
