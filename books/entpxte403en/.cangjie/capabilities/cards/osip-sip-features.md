# ALE SIP 业务特性（监督、寻线组、多终端、可编程键、RCC、按名呼叫）

## R — 原文依据

> "Limit is 30000 supervision keys on one OXE node. A supervisor can have up to 40 supervision keys. Supervision is not available on ALE SoftPhone on iPhone."（p130）
> "Mixed SIP/NOE configuration is NOT supported for parallel hunting group • Can contain only SIP devices or only NOE devices • Multi-devices CANNOT be part of such hunting group"（p141）
> "Only one ALE SoftPhone for Windows and one ALE SoftPhone for Mobile within the multi-devices"（p134）
> "Up to 48 entries are returned per search ... Maximum 16 simultaneous requests can be handled by the call-by-name service"（p125）

出处：ENTPXTE403EN p118-143。

## I — 自述

SIP 侧业务特性按域分六块，服务等级与机型强相关：

| 域 | 口径 |
|---|---|
| 监督与代接 | Set Supervision 键（DM 配置文件含被监督人）；SUBSCRIBE/NOTIFY 四态（available/ringing/busy/out of service）；容量 30000 键/节点、40 键/监督员；Keep Alive 超时事件码：入服 511（话机/第三方）/513（ALES），离服 510/512；toast+铃声仅 Windows 与 Android，多被监督人同振只弹最新；只有 SIP 设备能被 SIP 设备监督，iPhone 无监督 |
| 多终端 | 纯 SIP：1 主+最多 4 副（建议话机当主，ALES Windows/Mobile 各一台）；混合 NOE+DECT+ALES：最多 3 台，Virtual UA/REX/MIPT 不支持；来话并振，已接经 RFC3326 Reason 同步不计他机未接 |
| 寻线组 | circular/cyclical/parallel 三型；组呼叫不可转移、呼转与 DND 不参与分配、离服成员不分配但保持登录；顺序/循环组可混装与多终端入组，并行组两者皆禁；进出组默认前缀 480/481（须 COS 授权），ALES/ALE-30/ALE-x00 有图形开关 |
| RCC | legacy basic（不合头条件仍可用）/enhanced basic（Make call 免压缩资源，前提 COS 开 Optimize resource 3PCC call）/advanced（hold/retrieve/consultation/broker/conference/转移全集） |
| 可编程键 | 最多 120 键（5 页×24），#1/#2 保留 multiline，OXE 集中管理 #3-#122；ALE-2 仅 8 键、ALE-3 仅 12 键；用户设备级 "SIP Key" 管理员只能删不能改；ALE-2/3 与酒店话机不支持集中存储 |
| 按名呼叫 | 仅 ALES；不可用于远程工作者（经 SBC/RP）；PCS 模式不可用；48 条结果/名姓分机号三属性/16 并发 |

- 界面语义：ALES 关窗/隐藏仍收来话，任务栏 Quit 才真退出；呼叫日志是终端本地行为，终端未开机错过来话无记录

## A1 — 书中案例

**寻线组/监督/视频实验**（c07 步骤 10-12，p239-242）：

1. WBM Groups/Hunt Group → Create：DN=31333、circular 或 sequential、成员 31030+31000；用 ALE-S GUI 与前缀 480/481 进出组并查组呼叫日志，测完删组。
2. Users/Progr. Keys（选 31030）→ Key No.=3、Function=Set Supervision、DN=31031、Ringing Mode=No ring mandatory、Mnemo=Sup. 31031；他机呼 31031 时观察监督状态与按键直呼。
3. 视频：用户 SIP 页 Video Support Profile=On demand；DM profile 设编码 High 等，Save 后 Generate All Configuration Files，双方重开互打视频（Rlab 虚拟桌面不可测）。

## A2 — 未来触发

使用情境：秘书要看老板组状态并代接；客服组建组（哪种搜索类型）；一人多终端同振；批量配按键；前缀激活业务（锁机/呼转/遇忙回拨）。

语言信号：监督 / supervision / 代接 / pickup / 寻线组 / hunting group / parallel / circular / 480 / 481 / 多终端 / multi-devices / 可编程键 / SIP Key / RCC / 3PCC / 按名呼叫 / call by name / DTMF。

与相邻能力区分：先选对终端（能力矩阵）找用户形态选型；终端还没开通找各开通卡；远程场景按名呼叫不可用找远程办公。

## E — 可执行步骤

输入契约：业务需求（监督关系/组模型/按键表）、成员终端型号清单、编号计划（前缀可用性）。机型不满足等级要求 → 判停回选型。

1. 定监督方案：核容量（30000/40）、被监督人必须是 SIP 设备、toast 平台边界（Win/Android）。完成标准：监督关系表
2. 建寻线组：按需求选搜索类型；并行组先排除混装与多终端成员；基础话机授权前缀 480/481。完成标准：组建成交付
3. 配多终端：主备结构（话机当主）、ALES Windows/Mobile 各一；混合组网上限 3 台。完成标准：终端绑定
4. 配按键：DM 下发 #3-#122；ALE-2/3 按 8/12 键限额；用户 SIP Key 告知只能删。完成标准：按键台账
5. 业务前缀核对：按系统编号计划核 45/51/56/5 等默认值与 DTMF 三法选择。完成标准：拨测通过

判停点：

- 要 NOE 话机进 SIP 监督体系 → 停，先 SIP 化被监督人（n21）
- 并行组要混装或多终端 → 停，结构禁令不可绕（n22），改顺序/循环组
- 用户以为设 DND 就不被组分配 → 纠偏：分配逻辑不理会呼转与 DND（n22）
- 远程工作者要用按名呼叫 → 停，明确不支持，完整目录检索改配 LDAP（n27）

输出契约：业务开通记录（监督/组/多终端/按键）+ 前缀与 COS 授权清单 + 行为测试结论。

## B — 边界

- 事件码 510-513、30000/40、48/16、120/8/12 等数值为 Ed12 口径，版本演进以 OXE Features List 为准
- 功能矩阵"✓/空白"双列有文本层歧义（nr-02），ALE-2/3 寻线组为降级支持（nr-08 合读）
- 呼叫日志为终端本地行为，非 OXE 服务器侧日志（n24）
- 三方会议电路在 IMG；advanced RCC 各服务可用性还受终端 RFC 实现影响（p142）
- 实验分机/前缀值（31030、31333、45/51/56/5）为实验口径
