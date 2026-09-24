# 多线与监督键、经理/助理组（Multiline、Supervision、Screening）

## R — 原文依据

> "By default, all sets are mono-line • Except SIP extensions"（p257）
> "A set can be supervised by 20 sets maximum • The maximum number of supervisors for a same voice mailbox is 100 (20 in a network configuration) … The total number of supervision keys in the system is 15000"（p265）
> "RESTRICTION: AN ATTENDANT OR A HUNTING GROUP CAN'T BE SUPERVISED"（p262）
> "1000 tables usable with screening or unscreening keys • 16 parameters in each table"（p278）
> "It is not possible to activate a screening and an unscreening key at the same time"（p279）

出处：ENTPXTE401EN p255-295。

## I — 自述

话机级业务的公共地基是 Multiline：一切监督类特性（监督键、经理/助理、寻线组多线行为、多设备）都要求 multiline。

1. **两种形态**：Multi-keys=一号多键（多路并发、一线忙来话落下一空闲键）；Multi-MCDU=多号一机（主号+附加号各占键，附加号须为编号计划空闲号，键数无上限）；出厂全部单线（SIP 扩展除外）
2. **键属性**：Automatic Incoming/Outgoing Seizure（默认 True，摘机自动接振铃线/选空闲线）；选择性呼转可叠加线选前缀（20 主线/21 副线）按线转发
3. **监督键**：显示被监督方状态（部分忙/全忙/空闲/振铃/退服）、振铃时按键代接、平时按键直呼；铃型五档（No ring/Short/Long/Short/Long without Overring）；No Call=YES 只监督不直呼；可监督话机/传真/他人语音邮箱（新留言通知+凭密码代查）
4. **四条硬上限**：每话机至多 20 个监督者；同一邮箱至多 100（组网 20）个监督者；全网 15000 把监督键；一话机上同号只能一把键；话务台与寻线组不可被监督
5. **经理/助理组**：两台 multiline 话机经 Assistant Call（经理侧）/Manager Call（助理侧自动生成）构成，兼直呼与监督；Screening（仅表内来话转助理）与 Unscreening（仅表内来话留经理）互斥切换；过滤表 1000 张×16 参数（内部号/中继组/缩位号/话务台/T2 可混装）
6. **四个辅助键**：Screening Supervision（助理远程开关经理过滤、LED 同步）、Assistant Away（助理报离开暂停过滤，每助理仅一键）、Routing Assistant（溢出助理顶班，每经理一名、可服务多经理、不得已是其助理）、Manager Mail（预设短信互发）；Selective Filtering 只转经理主线来话

## A1 — 书中案例

**多线与监督键**（p267-273）：

1. Multi-keys：310x1 键 1/键 2 均=Multi-Line 310x1；两路来话在线间切换
2. Multi-MCDU：310x1 键 3=Multi-Line 31101（附加号取编号计划空闲号）
3. 监督键：310x2 键 5=Set Supervision → DN=310x1、铃型五选一、No Call=NO
4. 核验：multitool 菜单 1 查多线与被监督、菜单 5 按号列监督关系（含键号）

**经理/助理组**（p286-295）：

1. 建组：经理 31002 键 5=Assistant Call → DN=31001；助理侧自动生成 Manager Call
2. 过滤表：表 1=All Trunk Groups（全部外线来话）；表 2=One Directory No.（内部 310x0）
3. Screening 键（经理键 6 挂表 1）：公网呼入转助理；Unscreening 键（键 7 挂表 2）：内线来话留经理
4. 助理侧：Screening Supervision 远程开关经理过滤；Assistant Away 报离开；Routing Assistant 挂经理 DN 顶班
5. 核验：multitool 菜单 2 Boss/Secretary 三类清单

## A2 — 未来触发

使用情境：秘书/老板场景；工作组互看忙闲与代接；高管来话分流（外线转助理、内线留自己）；助理休假顶班；"为什么他看得到我的状态"；监督键承诺前的容量核算。

语言信号：multiline / multi-line / 多线 / Multi-MCDU / 附加目录号 / supervision key / 监督键 / 代接 / boss / secretary / 经理助理 / screening / unscreening / filtering table / 过滤表 / away / routing assistant。

与相邻能力区分：寻线组与代接组 → 组业务能力；多设备关联里的监督降级 → multi-device（路由卡）；话机型号支持面见各特性章（n50）。

## E — 可执行步骤

输入契约：话机型号与键数、编号计划余量（附加号）、经理-助理-溢出助理矩阵、COS。被监督方是话务台/寻线组 → 判停（不可监督）。

1. 建 multiline：按形态配 Multi-keys/Multi-MCDU（附加号取空闲号）。完成标准：multitool 显示 Multiline=Yes
2. 配监督键：选被监督对象、铃型、No Call。完成标准：状态可见、代接与直呼行为符合配置
3. 建经理/助理组：键对生成 + 过滤表（≤16 参数/表）+ Screening/Unscreening。完成标准：两类来话分流实测通过
4. 配辅助键：Screening Supervision/Away/Routing Assistant/Manager Mail。完成标准：顶班链路演练通过（away → screening → 溢出助理接起）
5. 容量复核：对照 20/100（网络 20）/15000 三条上限与一号一键规则。完成标准：方案数字不超限

判停点：

- 需求要"全员互监" → 停，对照硬上限拆方案
- 经理/助理建键失败 → 先核双方至少一把 multiline 键（前置硬性）
- screening 与 unscreening 同时想激活 → 停，机制互斥，改过滤表内容解决
- 监督对象是话务台/寻线组 → 不可监督（大写限制），找替代（组内监督/话务台自身视图）

输出契约：multitool 核验通过的多线/监督/经理助理配置 + 过滤表清单 + 上限核算表。

## B — 边界

- 监督者必须 multiline 且至少一把主号多线键（p262）
- Selective Filtering 只转经理主线，副号来话仍进经理（p280）
- 定时器/铃型体验随话机型号差异，混机型按最弱机型承诺（n50）
- multitool 支持 -l 语言选项；查询类命令不影响业务
- 寻线组成员的 multiline 行为另受组参数控制（No Multi-line call in PCX，见组业务能力）
