# 欢迎服务与 IVR（日历、语音提示、欢迎服务、自动话务员、MoH）

## R — 原文依据

> "Combination of a calendar and voice prompts to welcome your callers"（p251，欢迎服务定义）
> "The service that has been closed appears in 'forced' mode. At the next time slot, the mode returns to 'Auto'."（p259）
> "Each IVR has a maximum of 3 levels, each allowing a DTMF selection from 0 to 9. • The root menu contains 10 configurable entries."（p266）
> "Audio file must not exceed 4MB. greeting file must not exceed 120 seconds"（p263）

出处：RAINXTE101EN p250-275, p277-300。

## I — 自述

欢迎服务四件套互相咬合：日历（上游，定义开/闭时段，引用公司时区）+ 语音提示（素材库）+ 欢迎服务（日历+提示音的组合体，开/闭双路由）+ IVR（DTMF 自助路由）。实施两路线（p253）：无 IVR 线为载提示音、建日历、建欢迎服务、客户确认、测试；带 IVR 线再加 IVR 建管。

素材与日历规则（p255-256, p260, p263-264）：

| 项 | 口径 |
|---|---|
| 音频文件大小 | ≤4 MB（wav/mp3/ogg 等） |
| 问候文件时长 | ≤120 秒 |
| 单用途引导条数 | 最多 5 条 |
| 定制时段提示 | 最多 5 条 |
| 特殊日 | 最多 10 天 |
| 日历数量 | 不限；可复制天与整历；法定假日不预填须手工录 |

欢迎服务路由规则（p258-259）：

1. 来话入口是欢迎服务的公网号；先查日历——开时段播欢迎引导（pre-announcement）再路由到成员/带队列组/话务台/AA/直转留言
2. 闭时段路由到闭店提示音/成员/组（带或不带队列）/外线号/另一欢迎服务/AA
3. 可人工强制开/闭：显示 forced 态，是"一次性覆盖"，下一时段自动回 Auto
4. 每个欢迎服务绑定一个公网号与一份日历；日历必须先于欢迎服务创建

IVR 规格与两模式（p266-270）：

1. 每 IVR 最多 3 级；每级 DTMF 0-9（根菜单 10 项可配）；目的地可为组（带/不带队列）、成员、另一 IVR 菜单、欢迎服务
2. 数量无限、无许可限制——与话务台的 Voice Attendant 订阅形成成本对照（n57）
3. 两种入口：直挂公网号（DDI 直达=7×24 服务，可选 6 种溢出目的地）或经欢迎服务进入（受日历控制，IVR 本身不带 DID）
4. 语音提示两模式：每菜单唯一提示（官方强烈推荐但建后不可改）或每选项+每动作分条录音
5. 保密规则：来话显示默认名而非欢迎服务技术号（p269）

## A1 — 书中案例

**欢迎服务与 MoH 实验**（p277-283，How-To）：

1. Welcome services 页签 / Calendar 菜单 / Create → 起名。
2. 编辑日历：周一至周五 8:00-18:00；Specific days 加圣诞为闭店日（假日不预填）。
3. Welcome 区 → Create：绑日历与公网号，开时段目的地选 Hunt group。
4. 闭时段目的地选 closing voice prompt → Apply。
5. Voice prompts 页签按过滤器选该服务 → 上传欢迎与闭店提示音（挂对日历）。
6. 拨欢迎服务公网号测试开/闭提示音（可临时改公司时段验证）。
7. Voice prompts → General 区上传 New_MOH.wav（Usage=Music on hold）。

**自动话务员 IVR 实验**（p290-300，How-To）：

1. Automated attendant 页签 → Create → Name=company AA。
2. 勾 Menus with single voice prompts（唯一提示模式，建后不可改）。
3. 编辑 AA → Service Information → 挂公网号 02982967P8（实验口径）。
4. 默认 Menu 1 改名 Main menu → Create 子菜单 Marketing。
5. Main menu 按键：1 转 Alice、2 转 Bob、3 转 Marketing。
6. Marketing 菜单按键：1 转 Carol、2 转 Dave。
7. 两级菜单分别上传唯一提示音（Usage=Menu welcome 或 Exit）。

## A2 — 未来触发

使用情境：非营业时间来话怎么处理；白天转人工晚上播语音；客户要语音菜单按键分流；放假几天要不要改配置；强制闭店后第二天自己开了；MoH 换成自己的音乐；预算有限要不要话务台。

语言信号：欢迎服务 / welcome service / 日历 / calendar / 开闭时段 / 语音提示 / voice prompt / MoH / 音乐保持 / IVR / 自动话务员 / automated attendant / DTMF / 菜单 / 按键 / forced / 强制 / 特殊日。

与相邻能力区分：闭时段目的地转组/转成员归呼叫组与成员能力；人工接听工作台归话务台监督能力；公司时区设定归公司订阅能力（时区强制联动）。

## E — 可执行步骤

输入契约：营业时间与假日安排、欢迎词/闭店词文案与音频（≤4MB、问候 ≤120 秒）、菜单树设计（≤3 级）、号码资源（欢迎服务与 IVR 各需一个公网号或共用）、公司时区已核。

1. 建日历：Welcome services / Calendar → 按营业时间配各天时段 → 录特殊日。完成标准：日历时段与客户营业安排一致（假日手工补）
2. 传提示音：Voice prompts → 选过滤器 → 上传欢迎/闭店提示音并定义 Usage。完成标准：提示音挂在正确的服务与日历上
3. 建欢迎服务：绑公网号与日历 → 配开时段目的地与闭时段目的地。完成标准：拨测开/闭两路提示音与路由正确
4. 建 IVR（如需）：选唯一提示模式（慎重，建后不可改）/ 挂号或挂欢迎服务 / 建菜单树与按键 / 传菜单提示音。完成标准：按键拨测路由正确
5. 定制项（可选）：MoH 上传、定制时段提示（≤5 条）、特殊日（≤10 天）。完成标准：定制项生效并记录上限余量
6. 交付培训：讲清 forced 是一次性覆盖、来话显示默认名、IVR 入口语义（7×24 vs 受日历控制）。完成标准：客户确认理解

判停点：

- 客户要 4 级以上菜单 → 停，IVR 上限 3 级，重新收敛菜单树（p266）
- 客户要"白天 IVR、晚上关"且直挂了 DDI → 停，直挂公网号即 7×24；要受日历控制必须经欢迎服务进入（n46）
- 已建"唯一提示"模式想改逐项录音 → 停，建后不可改，只能重建 IVR（n47）
- 提示音超 4MB/120 秒或多语种超 5 条 → 停，拆文件或改方案，别承诺平台能放（n45）
- 拨测新提示音不生效 → 先查是否挂错日历/服务（n49），再查 forced 态与时段

输出契约：可用的欢迎服务/IVR（日历、提示音、路由就位）+ 拨测记录 + 上限余量表（5 条/10 天）。

## B — 边界

- 提示音文案录制与多语种制作在书外（BOOK_OVERVIEW 任务清单"尚缺条件"）；实验音频由讲师提供（实验口径）
- 日历引用公司时区——时区错配会导致开闭时段错乱（p255/p73 联动）；法定假日不预填，漏录=假日照常播开站欢迎词（n44）
- 组管理员改本组日历有显示前提：组只关联一个欢迎服务+一份日历且组用于开站时段（p273，n48）——复杂结构下别承诺自助改历
- IVR 统计（取消呼叫、停留时长）在分析页呈现（p323）；来话显示默认名为保密设计（p269）
- 实验号段 02982967P8 等为实验口径（needs-review nr-06）
