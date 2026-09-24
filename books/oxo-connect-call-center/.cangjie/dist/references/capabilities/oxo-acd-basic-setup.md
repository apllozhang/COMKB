# 基础 ACD 全流程搭建（OXO Connect）

## R — 原文依据

> "The prefixes used to manage the agent status are • 501: on duty • 502: off duty • 503: clerical work • 504: temporary absence ... Group ACD n°1, internal prefix:505, DDI N°: 41505 ..."（p70）
> "Validate the ACD Setup process by pressing the ''OK'' key. Restart the ACD engine in order to apply changes"（p48）
> "Select the ''Virtual terminals'' ... ''Media'' parameter ticked for all ACD ports (don't touch)"（p80）

出处：OXOCXTE107EN p43-48（向导）、p69-77（基础配置实验）、p80-84（向导后台生成物）。

## I — 自述

搭一套基础 ACD 分两层：**向导定骨架，菜单做精调**。

1. **第一层 · ACD Setup 向导一次成型**（OMC 内五步）：
   - General 页签：端口数（与 MLAA 共享，上限 16）、坐席状态前缀、ACD 组与 DDI 关联
   - ACD Group 页签：给组挂语音邮箱
   - Profiles 页签：生成坐席/班长预定义按键 profile
   - Agents/Supervisors 页签：把 profile 套到具体话机
   - 按 OK 校验 → **重启 ACD 引擎**（不重启不生效，新手第一大坑）
2. **第二层 · ACD Services 菜单精细调整**：
   - Smart Call Routing / Line parameters：号码进组路由
   - Agent parameters：建坐席、入组、定 rank
3. **向导后台自动生成物**（排障前先知道"向导动过什么"）：
   - ACD 端口虚拟终端（Media 参数已勾选，**不许动**）
   - cyclic 模式寻线组、邮箱动态呼转、DDI 关联、预定义 profiles
4. **完成判定**：核对四个菜单（Subscribers list / Hunting groups list / 内部编号计划 / 公共编号计划）+ 实呼验证

## A1 — 书中案例

**基础三组搭建实验**（p69-77，厂商实验，含标准验证步骤）

- **输入**：客户要求 3 个 ACD 组；坐席话机 101/102/103；话务台 100
- **步骤**：
  1. General 页签核对前缀 501-504；添加各组 DDI（内部前缀 505/506/507 分别对应 41505/41506/41507）
  2. ACD Group 页签为三组建邮箱
  3. Profiles 页签生成按键 profile
  4. Agents/Supervisors 页签：101/102/103 套 Agent profile，100 套 Supervisor profile
  5. Line parameters 维护 505-507 / 41505-07 进组条目
  6. Agent parameters 坐席入组定 rank —— 组1：101(r1)+102(r2)；组2：102(r1)+103(r2)；组3：103(r1)+102(r2)+101(r3)
  7. Voice messages 选 Transfer mode 下载默认语音
- **验证**：核对四个菜单；实呼每组确认"先欢迎语后转坐席"；用 501-504 前缀与功能键切换四态测试

## A2 — 未来触发

使用情境：

1. "新装了一台 OXO，要上呼叫中心"——从零交付
2. "再建一个 ACD 组给售后用"——扩组
3. "坐席 profile 怎么批量下发"——向导 Profiles 页签
4. "改了 ACD 配置怎么不生效"——忘记重启引擎

语言信号：配 ACD / 建 ACD 组 / 呼叫中心初始化 / ACD Setup / set up ACD / hunting group / DDI 关联 / 501 502 503 504 / profile 下发。

与相邻能力区分：已有 ACD 的"来话行为异常"→ 六场景排障能力；按客户分流来话 → 特征化路由能力；本能力只管"从零把 ACD 骨架立起来"。

## E — 可执行步骤

输入契约：组数与各组 DDI 号、坐席话机清单（分机号）、坐席-组归属与优先序、营业时段（可后置）。缺 DDI 规划或坐席清单时先询问，不要猜号。

1. 前置检查：OMC / System Miscellaneous / Feature design / part 2，确认 "Group called with signalization mode" **未勾选**。完成标准：确认为 setup mode。
2. ACD Setup 向导 General 页签：核对状态前缀 501-504；设置端口数；录入各组内部前缀与 DDI。完成标准：三组 DDI 关联出现在列表。
3. ACD Group 页签：为每组勾选 voice mailbox。完成标准：组名后带邮箱标识。
4. Profiles 页签：生成 Agent/Supervisor 预定义 profiles。完成标准：profile 列表出现。
5. Agents/Supervisors 页签：为坐席/班长话机套对应 profile。完成标准：目标话机已关联。
6. 按 OK → **重启 ACD 引擎**。完成标准：重启完成无报错。
7. ACD-SCR Services / Smart Call Routing：维护 Line parameters 进组条目。完成标准：来话号码能匹配进组。
8. Agent parameters：建坐席、入组、定 rank、置 on duty。完成标准：组归属与优先序正确。
9. Voice messages：Transfer mode → 选组 → Default messages → 上传；不配置的组点列号排除。完成标准：各组提示音就位。
10. 验证：核对四个菜单；实呼每组；四态前缀切换测试。完成标准：全部行为符合预期。

输出契约：可接听的 ACD 组清单（组号/内部前缀/DDI/坐席/rank）+ 验证记录。

## B — 边界

- 教材全部密码与网段是实验值，生产必须替换；生产安全加固与真实中继对接不在原书范围
- 端口数的规划依据（从话务量反推）书中未给，只有上限 16；超 32 坐席 / 8 组 / 16 端口的需求不在 OXO ACD 范围
- 向导自动生成的虚拟终端与 Media 参数**不要手改**（p80 "don't touch"）
- 与相邻能力区分：来话行为异常走六场景排障；按主叫/被叫分流走特征化路由
- Multi-Secretary 是独立方案（多秘书能力），不要在基础向导里混配
