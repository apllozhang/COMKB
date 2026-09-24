# 坐席签入签出与状态排障（OXO Connect）

## R — 原文依据

> "The entry to the ACD process is effective as soon as a common link is built for the following components: The agent name / The ACD group / The terminal ... ACD prefix with base 0: prefix to logout • ACD prefix with base 1: prefix to login"（p119-120）
> "Value 01: agent is ''on duty'' after login session (Default value) Value 00: agent is ''off duty'' after login session"（p123）
> "• 1:01 = ... 1 calls are in the queue. • 1:01+ = ... the queue is full. • 1-00 = Agent belong to ACD group 1 which is closed"（p122）

出处：OXOCXTE107EN p70（四态前缀）、p119-123（登录机制与状态码）。

## I — 自述

坐席要接 ACD 电话，前提是"四要素建链"：坐席名、坐席号、ACD 组、终端四者关联建立，才算进入 ACD 会话。OXO 默认 free seating 模式——坐席在任意话机拨登录前缀（内部编号计划里 base 1 开头）或按话机 ACD 页签的 Login 键，选自己（IP 话机按姓名、模拟/DECT 按坐席号）、输密码（若配置），话机就"变成"他的坐席席位；登出用 base 0 前缀或 Logout 键（Essential/Enterprise 话机要按 OK 确认，模拟/DECT 不用）。登录后自动进入的状态由隐藏寻址项 **ACDAutoLog** 决定：01=on duty（默认），00=off duty——"明明登录了却不接电话"十有八九是它或登录后手动置了 off duty。四态切换靠前缀 501（on duty）/502（off duty）/503（文书）/504（暂离）。话机 ACD 页签是坐席侧排障第一入口：`组号:等待数` 显示队列负载，`+` 后缀=队满，`-` 连接=组关闭。

## A1 — 书中案例

**状态码解读**（p122，厂商讲义）：坐席话机 ACD 页签显示 `1:01` = 组1 开放且队列有 1 通等待（不属于该组时另有变体显示，符号原文疑似缺漏需实机核对）；`1:01+` = 队列已满；`1-00` = 组1 关闭。ACD 页签用导航键下翻还有 On duty/Off duty/Clerical work/Temporary absence/Logout/Password/Groups 七个功能项。
**验证实验**（p77）：用 501-504 前缀与话机功能键切换四态，配合实呼确认各状态下是否分配来话。

## A2 — 未来触发

使用情境：
1. "坐席说登录了但电话不进来"——ACDAutoLog=00 或状态 off duty。
2. "话机上显示 1:01 是什么意思"——状态码解读。
3. "新员工怎么在别的座位接热线"——free seating 登录流程。
4. "怎么临时去开个会不接电话"——504 暂离/503 文书。
5. "换班怎么签出"——登出流程。

语言信号：签入 / 签出 / 登录坐席 / login / logout / free seating / 1:01 / ACD tab / 不接电话 / 501 / on duty / off duty / 坐席状态。

与相邻能力区分：Supervisor 台看到的八子态（Awaiting call/On hold 等）细读 → Supervisor 监控能力；来话不进来但坐席状态正常 → 六场景排障能力；本能力聚焦坐席侧的登录状态与话机显示。

## E — 可执行步骤

输入契约：话机型号（IP 系列/Essential/Enterprise/模拟/DECT/PIMphony）、坐席号与密码（若配置）、现象描述。缺话机型号先询问（登出确认与选坐席方式不同）。

1. 建链检查（不接电话第一排查）：确认坐席已登录（ACD 页签有登录信息）且状态为 On duty 而非 Off duty。完成标准：四要素（坐席名/坐席号/组/终端）关联成立。
2. 状态修正：拨 501（on duty）或页签选 On duty；若每次登录都进 off duty，查系统寻址项 **ACDAutoLog**=00，改回 01。完成标准：登录后默认 on duty。
3. 登录操作（代培/换座）：拨登录前缀（base 1）或 ACD 页签 Login → 选坐席（IP 话机按姓名 / 模拟与 DECT 按坐席号）→ 输密码（如配置）→ 话机显示登录完成。完成标准：ACD 页签出现该坐席会话。
4. 登出操作：拨登出前缀（base 0）或 Logout 键；Essential/Enterprise 需按 OK 确认，模拟/DECT 直接生效。完成标准：话机退出 ACD 会话。
5. 状态码判读（报障时）：读 ACD 页签——`组号:等待数` 正常负载；`+` 后缀队满（劝漏风险，联动六场景能力）；`-` 连接组关闭（查时段）。完成标准：给出判读结论与下一步。
6. 前缀冲突检查（规划期）：确认 501-504 与客户拨号计划不冲突（原书未给冲突排查法，发现冲突转方案层处理）。

判停点：坐席状态 on duty、四要素建链正常但仍无来话 → 转六场景排障（查路由/队列/端口），不要在坐席侧空转。

输出契约：问题判读结论 + 操作指导（或配置修改项 ACDAutoLog）+ 验证结果。

## B — 边界

- 状态码"属于/不属于开放组"两变体的显示符号原文疑似缺漏（两条均印 1:01），判读时以实机为准（needs-review nr-02），不要凭本卡断言变体含义。
- ACDAutoLog 的写入菜单原书未给（只有条目名与取值），改它需要实机查系统寻址（nr-03）。
- 登录密码连续错误的行为（锁定/提示）原书未覆盖。
- free seating 登录后原话机的坐席会话即解除——一坐席同时只能绑一终端（原书机制口径）。
- 四态是 OXO 口径（501-504）；其他平台的状态体系不通用。
