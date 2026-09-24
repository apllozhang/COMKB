# Multi-Secretary 多秘书方案（OXO Connect）

## R — 原文依据

> "Allows to share the resources of one or more secretaries between several managers ... Feature based on ACD engine (license needed)"（p126）
> "Carry out the programming in the following order"（p141）
> "The information displayed on the set for the transfer of the call to the agent are [GROUP_NAME] [CALLING_NUMBER] [WAITING_TIME]"（p107）

出处：OXOCXTE107EN p89（显示模式）、p124-139（讲义）、p140-146（完整实验）。

## I — 自述

Multi-Secretary = 多位经理共享一个秘书团，复用 ACD 引擎实现（需许可）：

1. **核心映射**：经理 DDI 当"被叫特征"灌进引擎；秘书当坐席（全 rank 1，谁先空谁接）
2. **秘书怎么知道替谁接**：转接中话机显示三元组 [被叫号码/经理名] [主叫号码] [等待时长]；接通后只显主叫
3. **来话行为完全复用 ACD 六场景**：开放有时段、忙时进队列（"秘书都在线上请稍候"）、全离席劝漏（"请稍后再拨"）、非营业时间转经理邮箱
4. **两件配套定制**：collective speed dialing 给每位经理建一条显示名（DOCTOR A/B/C）；语音按 wav 编号逐组定制
5. **配置顺序是硬要求**（十步，乱序返工）：DDI → 邮箱 → profile → Supervisor 声明 → 坐席 → 路由 → 时段 → 语音

## A1 — 书中案例

**医疗中心实验**（p127 讲义 + p140-146 实验）

- 场景：三位医生（105/106/107，DDI 41505-07）+ 两位秘书（101/102）；非营业时间转邮箱
- 按序配置：
  1. General tab 按序录 3 个 DDI 并激活 Multi-Secretary 模式（41505:505 / 41506:506 / 41507:507）
  2. ACD Groups 建秘书组邮箱
  3. ACD Profiles 生成秘书（Supervisor）profiles + Services keys
  4. Agents-Supervisors 把 101/102 声明为 Supervisor 站
  5. ACD 引擎建秘书账号，入 3 组全 rank 1
  6. Line parameters 录经理 DDI
  7. General Parameters：周一至五 8:00-19:00 + 溢出到邮箱
  8. Collective speed dialing 每医生一条（DOCTOR A/B/C）
  9. Voice Messages 定制语音（MMC 路径：Menu/Operator/PASSWORD OP/Expert/Voice/ACD）
- 验证：分别拨三位经理——转接中显示三元组（被叫随经理变），接通后只显主叫

## A2 — 未来触发

使用情境：

1. "三个老板共用一个秘书，秘书得知道电话替谁接的"——核心场景
2. "诊所/律所，几个医生/律师共用前台"——垂直行业方案
3. "秘书不在时电话怎么办"——劝漏/邮箱出口
4. "秘书屏上要显示老板名字"——collective speed dialing

语言信号：多秘书 / Multi-Secretary / 共享秘书 / 秘书组 / 替老板接电话 / 医生 前台 / 显示老板名字 / secretary pool。

与相邻能力区分：普通 ACD 组 → 基础搭建能力；时段单步操作可引用时段能力，但整体方案顺序由本能力主导。

## E — 可执行步骤

输入契约：经理清单（姓名/分机/DDI）、秘书清单（分机）、营业时段、各经理个性化话术。缺 DDI 或时段先询问。

1. 前提：确认 ACD 许可含 Multi-Secretary。完成标准：许可就位
2. General tab：**按序**录经理 DDI 映射并激活模式。完成标准：映射完整且未乱序
3. ACD Groups：建秘书组邮箱。完成标准：邮箱就位
4. ACD Profiles：生成秘书 profiles + Services keys。完成标准：profile 就绪
5. Agents-Supervisors：101/102 声明为 Supervisor 站。完成标准：出现于 Supervisor 列表
6. Agents parameters：建秘书账号，入全部经理组且 rank=1。完成标准：任一秘书可接任意经理来话
7. Line parameters：录经理 DDI 条目。完成标准：DDI 可匹配
8. General Parameters：营业时段 + 关闭溢出邮箱 + 离席劝漏。完成标准：四态行为一致
9. Collective speed dialing：每经理一条显示名。完成标准：秘书席显示经理姓名
10. Voice Messages：逐组定制语音。完成标准：实呼听到对应话术
11. 验证：拨三位经理——三元组显示、接通只显主叫；非营业时间入邮箱；全离席播劝漏

判停点：激活模式的控件名原书未单列（nr-04）——General tab 找不到开关时停止猜测，查版本文档。

输出契约：经理-DDI 映射表 + 秘书组配置清单 + 话术表 + 实呼验证记录。

## B — 边界

- 无 ACD 许可则方案不成立——先查许可再动配置
- 编程顺序硬要求：跳步可能映射失效需返工
- 秘书全 rank 1 是方案设定；要"主秘书优先"就退化为普通 ACD 组+rank，不是 Multi-Secretary 语义
- 模式下显示被叫（经理）而非组名——与 ACD 显示模式互斥（p89），混用会误报"显示不对"
- 容量受 ACD 组上限约束（8 组，p28）；超规模先核容量
