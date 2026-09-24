# ACR Call Tag 生成与传递（统计 Pilot、IAA 编码叶、CCivr、覆盖规则）

## R — 原文依据

> "The code entry guide prompts the caller to dial a code (max code length = 16 digits) and send it to the CSTA application as "Correlator data"."（p169）
> "Some building blocks can be used to send a call tag, through CSTA, from the Interactive Voice Response Server to the PCX. Example: "TransferCall" Building Block (BB)"（p170）
> "The last Call tag met in the call context overwrites the previous one"（p173）
> "The first CALLTAG "2500" will be overwritten be the CALLTAG of the Statistic Pilot 31650 (CALLTAG 1500)."（p189）

出处：OTCCXTE150EN p165-189。

## I — 自述

Call Tag 是随呼叫走、受 ACR 分发机制操作的字符串（本质是 CSTA 关联数据），可作脚本与数据库的索引键。三个生成途径：

1. **统计 Pilot 静态标**：0-32 字符，业务入口（如车险/家险）自带标签；配置在 OMF 或 CCS 侧
2. **IAA 编码叶**：提示音后客户拨不超过 16 位代码，以 Correlator data 经 CSTA 送出，可屏显在坐席话机
3. **CCivr TransferCall 构件**：盲转前须先执行 GetPilotInfo 构件，附着值可以是客户号、数据库索引或上下文 Id

覆盖规则（转发链排障的关键）：呼叫上下文中最后一个 Call Tag 或 Call Profile 覆盖之前所有值——多级 IVR 打标或转发到另一统计 Pilot 时，最终生效的是路径末端那个。

相关约束：

- IAA 只能从外部呼入，内部流程不能指望 IAA 入口
- 改 IAA 叶/树前先置 Valid=FALSE，改完再 TRUE；中继组 Automated Attendant 属性须 YES
- Call Tag 上坐席屏要改处理组 display 参数（与脚本 DISPLAY_AGENT 是两套机制）；显示计时器取 0 或 10-32767

## A1 — 书中案例

**IAA 编码采集（c07 前半）**：

1. 建可录引导 710-719 并录音（动态引导分配加 *88 录音）
2. 建编码叶：类型 Code Entry Guide，提示音 712，DTMF 4 位，目的地 31603
3. 建菜单叶（DTMF 1 路由统计 Pilot、DTMF 2 进编码叶）、树与接入号 31900
4. Automated Attendant 置 Valid=TRUE，中继组属性 YES
5. 脚本 IF 条件纳入 CALLTAG 区段 1000-3000 后挂 ACR Pilot
6. 四通外呼：选 1 得标签 1500 走名单；拨 1427 命中；拨 2545 区段内库外，脚本执行 21 次转路由管理；拨 7514 区段外走重定向

**GFW 转发覆盖验证（c07 后半）**：

1. 建统计 Pilot 31652（标签 2500）指直拨 Pilot 31604；建库条目区段 2000-2999
2. 配 31604 的 General Forwarding 到统计 Pilot 31650（标签 1500）并激活
3. 呼 31652：呼叫带 2500 进入 31604，处于 GFW 转发到 31650
4. Debugger 显示到脚本时生效标签为 1500——路径末端覆盖入口标签

## A2 — 未来触发

使用情境：IVR 采集客户号后个性化路由；按业务入口自动打标；转发链上标签被改导致路由不符预期；CTI 要用关联数据。

语言信号：Call Tag / 呼叫标签 / Correlator data / IAA / 编码叶 / Code Entry Guide / 统计 Pilot 标签 / CCivr / TransferCall / GetPilotInfo / 覆盖 / GFW / 转发。

与相邻能力区分：标签怎么喂给路由，见 内部数据库路由能力；多语言播报，见 多语言卡（路由）；脚本条件写法，见 脚本编辑器能力。

## E — 可执行步骤

输入契约：标签编码方案（位数与区段）、IVR 入口形态（IAA/CCivr/统计 Pilot）、外线测试条件（IAA 仅外部呼入）。

1. 定标签方案：来源途径、位数（16 位内）、区段与库条目映射。完成标准：方案成文
2. （统计 Pilot）入口配 0-32 字符标签。完成标准：入口带标签呼入 Debugger 可见
3. （IAA）建编码叶、树、接入并激活；改配前先 Valid=FALSE。完成标准：外呼可采集代码
4. （CCivr）TransferCall 前置 GetPilotInfo，附 Correlator Data。完成标准：标签随转移到达
5. 脚本按标签区段分支并接库条目。完成标准：标签命中路径正确
6. 转发链验证：构造两级打标场景，确认末端覆盖语义。完成标准：生效标签可预测
7. 屏显需求改处理组 display 参数并配计时器。完成标准：坐席屏可见标签

判停点：

- 内部分机测试 IAA 打不通 → 停，IAA 只能外部呼入，改外线或换入口
- 路由用了"入口标签"却没生效 → 停，按转发链路径末端查覆盖，不按入口查
- 代码超过 16 位 → 停，编码叶上限 16 位，改方案或拆两级

输出契约：标签采集链路 + 脚本分支 + 覆盖语义验证记录。

## B — 边界

- 原文 p168 段首 "all tag" 为笔误（照录）；"CSTA filed"（p15）同为原文拼写
- CCivr 侧构件（GetPilotInfo/TransferCall/receivephonecall.callprofile）的具体编程在 CCivr 文档域，本书只给集成语义
- 语音引导录制是环境操作；实验标签值（1500/2500/1427）为实验口径
- 未知标签时脚本执行次数原书两处口径 20/21 次（nr-01）
- 转移覆盖原则同时适用于 Call Profile（p172），两字段同一语义
