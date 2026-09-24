# 坐席签入签出与状态排障（OXO Connect）

## R — 原文依据

> "The entry to the ACD process is effective as soon as a common link is built for the following components: The agent name / The ACD group / The terminal ... ACD prefix with base 0: prefix to logout • ACD prefix with base 1: prefix to login"（p119-120）
> "Value 01: agent is ''on duty'' after login session (Default value) Value 00: agent is ''off duty'' after login session"（p123）
> "• 1:01 = ... 1 calls are in the queue. • 1:01+ = ... the queue is full. • 1-00 = Agent belong to ACD group 1 which is closed"（p122）

出处：OXOCXTE107EN p70（四态前缀）、p119-123（登录机制与状态码）。

## I — 自述

坐席要接 ACD 电话，前提是**四要素建链**：坐席名 + 坐席号 + ACD 组 + 终端，四者关联建立才算进入会话。

1. **登录（free seating 模式）**：在任意话机拨登录前缀（base 1），或按 ACD 页签 Login 选坐席（IP 话机按姓名，模拟与 DECT 按坐席号）、输密码（若配置），话机即"变成"他的席位
2. **登出**：拨 base 0 前缀或 Logout 键；Essential/Enterprise 要按 OK 确认，模拟/DECT 不用
3. **登录后默认状态**由隐藏寻址项 **ACDAutoLog** 决定：01=on duty（默认）、00=off duty——"登录了却不接电话"十有八九是它
4. **四态切换**：501 在值 / 502 离值 / 503 文书 / 504 暂离
5. **话机状态码**（ACD 页签，坐席排障第一入口）：
   - `组号:等待数`——如 1:01 = 组1 开放、队列 1 通
   - `+` 后缀 = 队列已满（1:01+）
   - `-` 连接 = 组关闭（1-00）

## A1 — 书中案例

**状态码解读 + 四态验证**（p122, p77，厂商讲义与实验）

- 状态码：`1:01`（开放、1 通等待）/ `1:01+`（队满）/ `1-00`（组关闭）；"属于/不属于开放组"的变体显示原文疑似缺漏，需实机核对
- ACD 页签导航键下翻还有：On duty / Off duty / Clerical work / Temporary absence / Logout / Password / Groups
- 实验：用 501-504 前缀与功能键切换四态，配合实呼确认各状态下来话分配行为

## A2 — 未来触发

使用情境：

1. "坐席说登录了但电话不进来"——ACDAutoLog=00 或状态 off duty
2. "话机上显示 1:01 是什么意思"——状态码解读
3. "新员工怎么在别的座位接热线"——free seating 登录流程
4. "怎么临时去开个会不接电话"——504 暂离 / 503 文书
5. "换班怎么签出"——登出流程

语言信号：签入 / 签出 / 登录坐席 / login / logout / free seating / 1:01 / ACD tab / 不接电话 / 501 / on duty / off duty / 坐席状态。

与相邻能力区分：Supervisor 台的八子态细读 → Supervisor 监控能力；坐席状态正常但无来话 → 六场景排障能力。

## E — 可执行步骤

输入契约：话机型号（IP/Essential/Enterprise/模拟/DECT/PIMphony）、坐席号与密码、现象描述。缺型号先询问（登出确认与选坐席方式不同）。

1. **建链检查**：坐席已登录且 On duty？完成标准：四要素关联成立
2. **状态修正**：拨 501 或页签 On duty；若每次登录都进 off duty → 查 ACDAutoLog=00 改回 01。完成标准：登录后默认 on duty
3. **登录操作**：拨登录前缀或 Login 键 → 选坐席 → 输密码。完成标准：ACD 页签显示会话
4. **登出操作**：拨登出前缀或 Logout 键（Essential/Enterprise 需 OK 确认）。完成标准：退出会话
5. **状态码判读**：读 ACD 页签——正常负载 / 队满（+）/ 组关闭（-）。完成标准：给出判读与下一步
6. **前缀冲突检查**（规划期）：501-504 与客户拨号计划是否冲突（冲突排查原书未给，转方案层）

判停点：状态 on duty、建链正常但无来话 → 转六场景排障，不要在坐席侧空转。

输出契约：判读结论 + 操作指导（或 ACDAutoLog 修改项）+ 验证结果。

## B — 边界

- 状态码变体符号原文疑似缺漏（nr-02），判读以实机为准
- ACDAutoLog 写入菜单原书未给（nr-03），改它需实机查系统寻址
- 登录密码连续错误的行为原书未覆盖
- free seating 一坐席同时只绑一终端——登录新话机，旧话机会话即解除
