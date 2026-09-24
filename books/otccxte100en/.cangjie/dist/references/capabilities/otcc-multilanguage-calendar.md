# 多语言语音指南与双日历（按语言与时段的自动路由）

## R — 原文依据

> "Create the pilot 31602 with the following items. Pilot name: After-Sales FR Language number: French"（p591）
> "Function Select the guide function (i.e. Multi-language message) … Language Number Select the language number (i.e. French) Message number Enter the message number for the french voice guide (i.e. 1702)."（p596-597）
> "Maximum of 10 time slot transitions for each of the 7 days of the week. … Maximum of 20 time slot transitions for each of the 7 days of the week."（p616）
> "Special days override the days of the weekly calendar • A maximum of 50 special days can be defined."（p611）
> "A modification carried out in the active transition does not apply immediately … the change-over is only carried out at the exact time indicated by the transition."（p638）

出处：OTCCXTE100EN p583-606（多语言）, p607-642（日历）。

## I — 自述

多语言指南两件事（p13/f22/c19）：

- 指南 Function 选 Multi-language message，一个指南号下按语言挂多条消息（French=1702、English=2702）
- 每个业务 pilot 设自己的语言（Language Number），同一指南号在不同语言 pilot 上播各自语言的消息
- 语言槽与语种的对应取决于目标库配置——录制前必核语言编号表（nr-07）

双日历体系（f21/p16/c20）：

- pilot 日历：每 pilot 一个，每周每天最多 10 个时间片切换，每切换=规则 ID+状态（Nor/Fwd），管通用转发、路由方向与语音指南
- 分配日历：挂分配规则，班长站可配，每天最多 20 个切换，管队列方向、分配阈值与资源/呼叫选择参数
- 特殊日：≤50 个、必填日/月/年、不能选过去日期、覆盖周历（两套日历各有特殊日）
- 切换语义：只在时间片定义的时间点执行；改"活动中的时间片"不立即生效，测试要提前几分钟（n07）；活动时间片界面绿色显示

典型组合：开日（工作日时段）用 Rule_0 照常分发；闭日（午休/夜间/周末/特殊日）切 Closed_rule——关 Normal 方向、开 Redirection 播提示（c20）。

## A1 — 书中案例

**双语 pilot 实验**（p588-606）：

1. CCS 把 31600 改名 After-Sales EN；OXE 建 31602/After-Sales FR，Language Number=French
2. FR pilot 建规则并加 Normal_WQ、Redirection_WQ 方向，Normal_WQ 优先级 0
3. 建 702/703 多语言指南：Function=Multi-language message，French 挂 1702/1703、English 挂 2702/2703
4. 四条消息分配板位 4-0 并用 401 录制（法语"Bienvenu…"、英语"Welcome again…"）
5. 两 pilot 排同一套矩阵：Pres.Guide=702、Level[2]=703
6. 实测：EN pilot 先"Welcome again…"；FR pilot 先"Bienvenu au service après-vente"

**日历实验**（p617-642）：

1. 建 Closed_rule：关 Normal_WQ 主方向、开 Redirection_WQ，Pres.Guide=683；建同名分配规则并回 OXE 激活
2. Navigator Tab8 核对：闭态仅 Redirection_WQ 可达，拨 Offer 听"无座席"提示
3. pilot 日历：周一 08:00 Rule0 / 12:00 Rule1 / 13:30 Rule0 / 19:00 Rule1，复制到周五；周六日与特殊日 00:00 Rule1
4. 分配日历同步配切换骨架；勾 Activate Time Slices 激活
5. 开/闭两个时点验证：激活规则 ID 与绿色活动时间片吻合

## A2 — 未来触发

使用情境：双语客户要按拨打号分流语言；节假日特殊安排；午休/夜间自动切闭态；"改了日历怎么不生效"；特殊日不够用；多语言消息录哪个槽。

语言信号：Multi-language / 多语言 / Language Number / French / English / "1702" / "2702" / calendar / 时间片 / Closed_rule / 特殊日 / Activate Time Slices / 切换点。

与相邻能力区分：指南录制与装板 → 语音指南能力；规则与方向本身 → 路由与分配规则能力；统计型 pilot 的三态问候归统计 pilot 卡（路由卡）。

## E — 可执行步骤

输入契约：语言清单与目标库语言编号表已核对、营业时间表与节假日表已定、闭态去向已定。

1. 建语言 pilot：每个语言一个 pilot 并设 Language Number。完成标准：pilot 语言属性正确
2. 建多语言指南：Function=Multi-language message，按语言挂消息号并录制装板。完成标准：vgstat 全部 ^ 选中
3. 排矩阵：各语言 pilot 的 Pres.Guide 与 parking level 挂同一多语言指南号。完成标准：各 pilot 播各自语言
4. 建 Closed_rule 闭环：pilot 规则（关常态方向+开重定向+提示指南）与分配规则并回 OXE 激活。完成标准：闭态拨测听到提示
5. 配双日历：pilot 日历 ≤10 切换/日、分配日历 ≤20 切换/日，复制跨日、补特殊日。完成标准：周历与特殊日全覆盖
6. 激活并双时点验证：勾 Activate Time Slices，开/闭各验一次。完成标准：激活规则 ID 与时间片吻合

判停点：

- 改了日历"不生效" → 切换只在时间点执行，活动时间片上的修改要等下一切换点，测试提前几分钟改（n07）
- 播错语言 → 语言槽按库配置核对，勿照抄书中 #1/#2 口径（nr-07）
- 特殊日配不了 → 必填年月日且不可选过去日期；上限 50 个（p611）
- 新建的 Closed_rule 未生效 → 分配规则要回 OXE 激活（n02）

输出契约：按语言与时段自动路由的运行矩阵（语言 pilot + 多语言指南 + 双日历 + 特殊日）+ 双时点验证记录。

## B — 边界

- 10/20 切换每日、50 特殊日为 R10.16 容量口径（p611/p616）；切换粒度以时间片定义为准
- ACR 语言技能路由（按主叫语言技能选路）在书外，本书语言分流靠多 pilot（n41/g27）
- 日历只切换规则与方向；时间片内的参数微调仍走对象调优卡
- 实验语言对（French/English）与节假日（1 月 1 日等）为实验口径
- 分配日历由班长站配置——OXE 侧只读核对（p616）
