# ACR 坐席直拨融合（Pilot Direct Call、私有号、DICA、CALL_TYPE 脚本）

## R — 原文依据

> "Complete the "Pilot direct call" parameter at the agent processing group level … Complete the Private agent number parameter in the agent data"（p106）
> "When a private number is managed for one Agent, the system automatically assigns a new skill for this Agent • Domain: Media • Skill: DirectCall • Abbreviation: DICA"（p111）
> "If the "DirectCall" skill is not activated, it is no more possible to call the agent directly (whatever the agent status: idle, busy…)"（p111）
> "Only 1 ACR script can be used at the same time on an ACR Pilot"（p113）

出处：OTCCXTE150EN p103-127。

## I — 自述

"回头客直拨找原坐席、忙时等一等"靠四件套实现：

1. **Pilot Direct Call**：处理组级参数填一个 Pilot 号（实验口径填直拨 Pilot 31604）。直拨呼叫 ACD 化，坐席忙时溢出到该 Pilot
2. **Private Agent Number**：坐席数据里配私有号。该参数的存在形态决定呼叫类型判定——未管理=仅矩阵内呼叫算 CCd；私有号=CCd 号时全部外部来电算 CCd；两号不同时各归各类
3. **DICA 自动技能**：配了私有号，系统自动在 Media 域挂 DirectCall 技能（缩写 DICA）。它是开关型技能——停用后无论坐席空闲与否都无法直拨，呼叫立即转 pilot direct call
4. **CALL_TYPE=DIRECT_CALL**：脚本关键字，区分直拨与普通来话，配合 SEQUENCE 与重选超时实现"第 1 次执行等 N 秒原坐席、第 2 次执行转走"

无 ACR 与有 ACR 的直拨行为对照：

| 场景 | 坐席忙时直拨行为 |
|---|---|
| 无 ACR | 立即溢出到 pilot direct call，矩阵内重路由，可能换人接听 |
| 有 ACR | 带 ASM 动态列表进等待房间，等原坐席指定时长后按脚本转走 |

设计约束：一个 ACR Pilot 同一时刻只能激活 1 个脚本；直拨 Pilot 若非专用（还接普通来话），脚本必须用 CALL_TYPE 分支兼容两种呼叫来源，否则必有一边路由错。

## A1 — 书中案例

**直拨特性验证（c05 前半）**：

1. 建直拨 Pilot 31604 接等待房间 31999703（实验口径）
2. 处理组 31999800 的 Pilot Direct Call 参数填 31604
3. 坐席 31501（DN 31500）配 Private Agent No.=31001；初始不给 31604 挂脚本
4. 坐席空闲时直拨 DN 正常；坐席忙时观察溢出行为（无脚本时在房间等到空闲）
5. 停用 31501 的 DICA 技能再直拨：空闲/可用/忙全部立即转 pilot direct call

**DICA 脚本（c05 后半）**：

1. 编辑器建脚本 DICA：构件 Statement(SEQUENCE=%1) 接 RULE_REDIRECTION（目标 31010）
2. SET RESELECTION_TIMEOUT=%30 定等待 30 秒
3. IF(CALL_TYPE=DIRECT_CALL) 分支接 RULE_ISM Call_Profile=%1，连线完成
4. 脚本挂 ACR Pilot 31604 激活；Debugger 观察：坐席忙时首呼等 30 秒、重选后转 31010、非直拨走 ISM

## A2 — 未来触发

使用情境：客户要求"回头客直拨等原坐席"；临时屏蔽某坐席直拨；直拨忙时行为不符合预期；私有号与呼叫类型判定咨询。

语言信号：直拨 / Direct Call / Pilot Direct Call / 私有号 / Private Agent Number / DICA / DirectCall 技能 / CALL_TYPE / DIRECT_CALL / 等原坐席 / 溢出。

与相邻能力区分：等原坐席要查历史，见 内部数据库三键路由能力（坐席号键）；脚本写法细节，见 脚本编辑器能力；等待体验编程，见 综合规则组合能力（IQUEUE）。

## E — 可执行步骤

输入契约：直拨业务时长口径（等几秒、转哪里）、坐席私有号方案、ACR Pilot 就绪。矩阵或房间没建好先回 CCD 矩阵地基能力。

1. 处理组配 Pilot Direct Call 填 ACR Pilot 号。完成标准：直拨溢出目标生效
2. 给目标坐席配私有号。完成标准：CCS 坐席页可见自动生成的 DICA 技能
3. 无脚本先验证基线行为：忙时直拨应溢出到该 Pilot 并在等待房间等待。完成标准：行为与预期一致
4. 写直拨脚本：CALL_TYPE 分支 + SEQUENCE 分支 + RESELECTION_TIMEOUT + 兜底转接。完成标准：保存传输激活
5. Debugger 验证三路径：忙时首呼等待、超时转接、非直拨走常规分支。完成标准：三路径轨迹正确

判停点：

- 客户要"临时不让任何人直拨某坐席" → 停用该坐席 DICA 技能即可，不要删私有号
- 直拨 Pilot 同时接普通来话而脚本无 CALL_TYPE 分支 → 停，先改脚本兼容双来源再上线
- 直拨行为像普通 Pilot 一样换人接听 → 停，核对处理组 Pilot Direct Call 是否真指向 ACR Pilot

输出契约：直拨特性配置 + CALL_TYPE 脚本 + 三路径验证记录。

## B — 边界

- 原文 "Direct Call the an ACR Pilot will not work in the same way as with a "normal" Pilot"（p120，原文拼写如此）——直拨打到 ACR Pilot 的行为与普通 Pilot 不同，按普通 Pilot 经验预测会误判（n12）
- DICA 停用即完全不可直拨（含空闲态），排障时容易漏查这个自动技能（n13）
- "忙时等原坐席"是 ACR 部署后的增值能力，系统默认行为是立即溢出换人（n14），需求沟通先讲清
- 私有号（实验口径 31001）与 Pilot 号（31604）为实验值，生产按客户编号方案
- 直拨场景才支持内部数据库的坐席号键（见内部数据库能力条件）
