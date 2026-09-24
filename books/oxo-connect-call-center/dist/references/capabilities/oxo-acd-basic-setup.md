# 基础 ACD 全流程搭建（OXO Connect）

## R — 原文依据

> "The prefixes used to manage the agent status are • 501: on duty • 502: off duty • 503: clerical work • 504: temporary absence ... Group ACD n°1, internal prefix:505, DDI N°: 41505 ..."（p70）
> "Validate the ACD Setup process by pressing the ''OK'' key. Restart the ACD engine in order to apply changes"（p48）
> "Select the ''Virtual terminals'' ... ''Media'' parameter ticked for all ACD ports (don't touch)"（p80）

出处：OXOCXTE107EN p43-48（向导）、p69-77（基础配置实验）、p80-84（向导后台生成物）。

## I — 自述

在 OXO Connect 上搭一套基础 ACD 分两层。第一层 ACD Setup 向导一次成型：General 页签定端口数、坐席状态前缀（501 在值/502 离值/503 文书/504 暂离）和 ACD 组与 DDI 的关联；ACD Group 页签给组挂语音邮箱；Profiles 页签生成坐席/班长预定义按键 profile；Agents/Supervisors 页签把 profile 套到具体话机；最后按 OK 并**重启 ACD 引擎**——不重启不生效。第二层用 ACD Services 菜单做精细配置：Smart Call Routing 维护 Line parameters（号码进组路由）、Agent parameters 建坐席入组定 rank。向导会自动生成虚拟终端（Media 参数勾选，不许动）、cyclic 寻线组、邮箱动态呼转、DDI 关联和预定义 profiles——排障前先知道"向导动过什么"。完成后按四个菜单核对（Subscribers list / Hunting groups list / Internal numbering plan / Public numbering plan）并实呼验证。

## A1 — 书中案例

**基础三组搭建实验**（p69-77，厂商实验，有标准验证步骤）：
- 输入：客户要求 3 个 ACD 组；坐席话机 101/102/103；话务台 100。
- 步骤：General 页签核对前缀 501-504、加 DDI（505→41505、506→41506、507→41507）→ ACD Group 页签为三组建邮箱 → Profiles 页签生成 profile → Agents/Supervisors 页签 101/102/103 套 Agent profile、100 套 Supervisor profile → ACD-SCR Services 的 Line parameters 维护 505-507/41505-07 → Agent parameters 中坐席入组定 rank（组1: 101(rank1)+102(rank2)；组2: 102(rank1)+103(rank2)；组3: 103(rank1)+102(rank2)+101(rank3)），姓名自定义、状态 on duty → Voice messages 选 Transfer mode 下载默认语音。
- 验证：核对四个菜单；实呼每组确认"先欢迎语后转坐席"；用 501-504 前缀与功能键切换四态测试。

## A2 — 未来触发

使用情境：
1. "新装了一台 OXO，要上呼叫中心"——从零交付。
2. "再建一个 ACD 组给售后用"——扩组。
3. "坐席 profile 怎么批量下发"——向导 Profiles 页签。
4. "改了 ACD 配置怎么不生效"——忘记重启引擎。

语言信号：配 ACD / 建 ACD 组 / 呼叫中心初始化 / ACD Setup / set up ACD / hunting group / DDI 关联 / 501 502 503 504 / profile 下发。

与相邻能力区分：已有 ACD 的"来话行为异常"→ 六场景排障能力；按客户分流来话 → 特征化路由能力；本能力只管"从零把 ACD 骨架立起来"。

## E — 可执行步骤

输入契约：组数与各组 DDI 号、坐席话机清单（分机号）、坐席-组归属与优先序、营业时段（可后置到时段能力）。缺 DDI 规划或坐席清单时先询问，不要猜号。

1. 前置检查：OMC / System Miscellaneous / Feature design / part 2，确认 "Group called with signalization mode" **未勾选**（勾选则来话显示在组监管键，坐席无法正常接听）。完成标准：确认为 setup mode。
2. OMC / Customer PBX / Automatic Call Distribution → ACD Setup 向导 General 页签：核对/设置状态前缀 501-504；设置端口数（与 MLAA 共享，上限 16）；录入各组内部前缀与 DDI。完成标准：三组 DDI 关联出现在列表。
3. ACD Group 页签：为每组勾选 voice mailbox。完成标准：组名后带邮箱标识。
4. Profiles 页签：生成 Agent/Supervisor 预定义 profiles。完成标准：profile 列表出现预定义项。
5. Agents/Supervisors 页签：为坐席话机套 Agent profile、班长话机套 Supervisor profile。完成标准：目标话机已关联 profile。
6. 按 OK 保存 → **重启 ACD 引擎**。完成标准：重启完成无报错（此步漏做 = 全部改动不生效）。
7. ACD-SCR Services / Smart Call Routing：维护 Line parameters（各组 DDI 进组条目）。完成标准：来话号码能匹配进组。
8. ACD Services / Agent parameters：建坐席、入组、定 rank、姓名、状态 on duty。完成标准：坐席列表组归属与优先序正确。
9. ACD Voice messages：Transfer mode → 选组 → Default messages → 上传；**注意**默认会下载到所有组，不配置的组要点列号排除。完成标准：各组提示音就位。
10. 验证：核对 Subscribers/Hunting groups/编号计划菜单；实呼每组（欢迎语先播→转坐席）；四态前缀切换测试。完成标准：全部行为符合预期。

输出契约：一份可接听的 ACD 组清单（组号/内部前缀/DDI/坐席/rank）+ 验证记录。

## B — 边界

- 本书全部密码（pbxk1064/Acdc1064）与网段是实验值，生产必须替换；生产安全加固与真实中继对接不在原书范围。
- 端口数的规划依据（从话务量反推）书中未给，只有上限 16——超出 32 坐席/8 组/16 端口的需求不在 OXO ACD 范围。
- 向导自动生成的虚拟终端与 Media 参数**不要手改**（p80 "don't touch"）。
- 与相邻能力区分：来话行为异常走六场景排障；按主叫/被叫分流走特征化路由；本能力不处理两者。
- Multi-Secretary 是独立方案（多秘书能力），不要在基础向导里混配。
