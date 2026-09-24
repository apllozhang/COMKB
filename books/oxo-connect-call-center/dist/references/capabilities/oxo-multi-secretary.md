# Multi-Secretary 多秘书方案（OXO Connect）

## R — 原文依据

> "Allows to share the resources of one or more secretaries between several managers ... Feature based on ACD engine (license needed)"（p126）
> "Carry out the programming in the following order"（p141）
> "The information displayed on the set for the transfer of the call to the agent are [GROUP_NAME] [CALLING_NUMBER] [WAITING_TIME]"（p107）
> "Respect the assignments 101.wav = welcome message, 102.wav = waiting message, etc."（p136）

出处：OXOCXTE107EN p89（显示模式）、p124-139（讲义）、p140-146（完整实验）。

## I — 自述

Multi-Secretary 是让多位经理共享一个秘书团的 ACD 预设形态（需要许可）：把每位经理的 DDI 当作"被叫特征"灌进 ACD 引擎，秘书当坐席（全部 rank 1，谁先空谁接），转接中话机显示 [被叫号码/经理名] [主叫号码] [等待时长] 三元组——秘书因此知道这通电话是替哪位经理接的；接通后只显示主叫。来话行为完全复用 ACD 六场景：秘书组开放有时段、忙时进队列播"秘书都在线上请稍候"、全离席走劝漏"请稍后再拨"、非营业时间转经理邮箱。配套两件定制：collective speed dialing 里给每位经理建一条号码让话机显示姓名（DOCTOR A/B/C）；语音按 wav 编号逐组定制（"Doctor 1 is busy please wait"…）。配置有严格顺序（DDI→邮箱→profile→Supervisor 声明→坐席→路由→时段→语音），乱序会返工。

## A1 — 书中案例

**医疗中心实验**（p127 讲义 + p140-146 实验，厂商案例）：
- 场景：三位医生（分机 105/106/107，DDI 41505/41506/41507），两位秘书（101/102）共享接待；非营业时间来电转邮箱。
- 按序配置：General tab 按顺序录 3 个 DDI 并激活 Multi-Secretary 模式（41505:505 / 41506:506 / 41507:507）→ ACD Groups 建秘书组邮箱 → ACD Profiles 生成秘书（Supervisor）profiles 并加 Services keys → Agents-Supervisors 把 101/102 声明为 Supervisor 站 → ACD 引擎建秘书账号入 3 组全 rank 1 → Line parameters 录经理 DDI → General Parameters 时段周一至五 8:00-19:00 + 溢出到邮箱 → Collective speed dialing 每医生一条（DOCTOR A/B/C）→ Voice Messages 定制语音（话机 MMC 路径：Menu/Operator/PASSWORD OP/Expert/Voice/ACD）。
- 验证：拨三位经理前缀实测——转接中显示 [CALLED_NUMBER] [CALLING_NUMBER] [WAITING_TIME]（被叫号码随经理不同而不同），接通后只显示 [CALLING_NUMBER]。

## A2 — 未来触发

使用情境：
1. "三个老板共用一个秘书，秘书得知道电话替谁接的"——核心场景。
2. "诊所/律所，几个医生/律师共用前台"——垂直行业方案。
3. "秘书不在时电话怎么办"——劝漏/邮箱出口。
4. "秘书屏上要显示老板名字"——collective speed dialing。

语言信号：多秘书 / Multi-Secretary / 共享秘书 / 秘书组 / 替老板接电话 / 医生 前台 / 显示老板名字 / secretary pool。

与相邻能力区分：普通 ACD 组（来话不区分被叫身份）→ 基础搭建能力；秘书组的时段/邮箱单步操作可引用时段能力，但整体方案顺序由本能力主导。

## E — 可执行步骤

输入契约：经理清单（姓名/分机/DDI）、秘书清单（分机）、营业时段、各经理个性化语音话术。缺 DDI 或时段先询问。

1. 前提：确认 ACD 许可包含 Multi-Secretary（原书标注 license needed）；OMC 可管理。
2. OMC/ACD Setup/General tab：**按顺序**录入每位经理 DDI 与内部号码映射（41505:505 → 41506:506 → 41507:507），激活 Multi-Secretary 模式。完成标准：映射列表完整且顺序未乱。
3. ACD Setup/ACD Groups tab：为秘书组建 voice mailbox（非营业时间承接）。完成标准：组邮箱就位。
4. ACD Setup/ACD Profiles tab：生成秘书（Supervisor）profiles，补 Services keys。完成标准：profile 就绪。
5. ACD Setup/Agents-Supervisors tab：把秘书话机声明为 Supervisor 站（才有语音留言查询键）。完成标准：101/102 出现在 Supervisor 列表。
6. ACD-SCR Services/Agents parameters：建秘书坐席账号，加入全部经理组且 rank 全部 = 1。完成标准：任一秘书空闲即可接任意经理来话。
7. ACD-SCR Services/Smart Call Routing Line parameters：录入经理 DDI 条目。完成标准：DDI 可匹配进组。
8. General Parameters（Group 1-4 tab）：营业时段（实验：周一至五 8:00-19:00）+ 关闭时段溢出到邮箱；秘书全 off duty/登出时走劝漏消息。完成标准：四态行为与需求一致。
9. OMC/Collective speed dialing：每位经理建一条显示号码（DOCTOR A/B/C）。完成标准：秘书席转接中能显示经理名。
10. ACD Voice Messages：逐组定制语音（MMC：Menu/Operator/PASSWORD OP/Expert/Voice/ACD；或 OMC 四步上传），话术按经理个性化（"Doctor 1 is busy please wait"…）。完成标准：实呼听到对应经理的话术。
11. 验证：分别呼叫三位经理 DDI——转接中三元组显示（被叫随经理变），接通后仅显主叫；非营业时间来电入邮箱；秘书全离席时播劝漏。

判停点：激活 Multi-Secretary 模式的具体控件原书未单独说明（nr-04）——在 General tab 内找不到开关时停止猜测，查版本文档。

输出契约：经理-DDI 映射表 + 秘书组配置清单 + 语音话术表 + 实呼验证记录。

## B — 边界

- 无 ACD 许可则整条方案不成立——先查许可再动配置。
- 编程顺序是硬要求（p141 "in the following order"）：跳步（如先建坐席后录 DDI）可能导致映射失效需返工。
- 秘书全 rank 1 是方案设定：若客户要"主秘书优先"，退化为普通 ACD 组+rank，不是 Multi-Secretary 语义。
- Multi-Secretary 模式下组显示的是被叫（经理）而非 ACD 组名——两种显示模式互斥（p89），混用预期会造成"显示不对"的误报。
- 实验基于两秘书三经理；更多经理的 DDI 容量上限受 ACD 组容量约束（8 组，p28），超规模需求先核容量。
