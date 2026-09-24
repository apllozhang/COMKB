# ACR 内部数据库路由（三键五属性、4000 条、脚本取用语法）

## R — 原文依据

> "Caller Identification: Calling Number • Call Tag • Agent Number (in case of Direct Call) … Associated Information: Name • Call Profile • Authorized List • Unauthorized List • Call Priority"（p131）
> "Note: 4000 entries (single value or range) can be created in the Internal Database"（p131）
> "Complete Number or open Number • Unique number or Range"（p132）
> "RULE_ISM CALL_PROFILE [CALLING] … SET PRIORITY = CALL_PRIORITY [CALLING]"（p147）

出处：OTCCXTE150EN p128-164。

## I — 自述

内部数据库（ACR Data）是个性化路由的本地索引，三键查五属性：

| 维度 | 取值 |
|---|---|
| 键 1：主叫号 | 完整号或开放号（通配）、单值或区段 |
| 键 2：Call Tag | 单值或区段（如 1000-1999 整段命中） |
| 键 3：坐席号 | 仅直拨场景（前提：直拨特性已配） |
| 值 1：Name | 客户名（可屏显） |
| 值 2：Call Profile | 呼叫档案 ID，喂给 ISM |
| 值 3：授权/非授权名单 | 名单 ID，喂给名单规则 |
| 值 4：Call Priority | 呼叫选择优先级 |

脚本取用语法（方括号里是键）：

- CALL_PROFILE[CALLING] / CALL_PROFILE[CALLTAG] / CALL_PROFILE[AGENT_NUMBER] 取档案
- CALL_PRIORITY[键] 取优先级；AUTHORIZED_LIST[键] 取名单
- 配置入口在 CCS 的 ACR Data 页；运维查看用 adm_acd 选项 25

容量与前提：最多 4000 条（单值或区段都按条计）；用坐席号键的前提是该坐席已配 Pilot Direct Call 与私有号；数据在 CCS/CCSupervisor 侧维护。屏显 Call Tag 还要处理组的 display 参数配合（与脚本 DISPLAY_AGENT 是两套机制）。

## A1 — 书中案例

**主叫号键（c06 前段）**：

1. ACR Data 建条目：主叫号 02312122003（实验口径），档案 0、授权名单 0、优先级 0
2. 写脚本：RULE_ISM CALL_PROFILE[CALLING]、SET PRIORITY=CALL_PRIORITY[CALLING]、空列表时接授权名单
3. 从分机呼入，Debugger 核对档案与优先级取自库；再以库外号码验证落空路径
4. 翻译前缀对照：RSI 参数 Callback Prefix 置 TRUE 后主叫号带前缀，须与库内容一致

**Call Tag 键（c06 中段）**：

1. 建条目：Call Tag 区段 1000-1999，授权名单 0
2. 统计 Pilot 配 Call Tag 1500（0-32 字符）
3. 脚本：有标签走 CALL_PRIORITY 与 AUTHORIZED_LIST[CALLTAG]，无标签走重定向
4. 呼带标签 Pilot 命中名单；呼无标签 Pilot 走重定向（未知标签时脚本执行 21 次的口径见 nr-01）

**坐席号键（c06 后段）**：

1. 前提：坐席 31501 已配直拨特性
2. 建条目：坐席号 31501，档案 1、优先级 0
3. 脚本：直拨时 RULE_ISM CALL_PROFILE=[AGENT_NUMBER]，30 秒重选后授权名单兜底
4. 直拨忙坐席：Debugger 显示 ISM 取库中档案、超时后名单路径生效

## A2 — 未来触发

使用情境：VIP 来电走专属档案或优先级；回头客按主叫号定制路由；按客户号区段批量配路由；直拨忙时按坐席查档案。

语言信号：内部数据库 / Internal Database / ACR Data / CALL_PROFILE / CALL_PRIORITY / 主叫号 / Calling Number / Call Tag 键 / 坐席号键 / 4000 条 / VIP 路由。

与相邻能力区分：数据在外部数据库，见 外部数据库查询路由能力；Call Tag 怎么生成，见 Call Tag 卡（路由）；直拨特性本身，见 坐席直拨融合能力。

## E — 可执行步骤

输入契约：客户数据（主叫号/客户号段/坐席号与对应档案名单）、矩阵与统计 Pilot 就绪。数据量大或需外部维护时改走外部库方案。

1. CCS 的 ACR Data 建条目：选键类型，录键值与四个属性。完成标准：条目保存且 ID 唯一
2. 写脚本：按键取用 CALL_PROFILE / CALL_PRIORITY / AUTHORIZED_LIST。完成标准：语法保存无误
3. 脚本挂 ACR Pilot 激活。完成标准：Debugger 可见连接
4. 正反用例测试：库内键命中路径 + 库外键落空路径各走一遍。完成标准：两路径轨迹符合设计
5. 屏显需求时配处理组 display 参数（Call tag 或 caller and pilot char.）。完成标准：坐席屏可见
6. 运维核查用 adm_acd 选项 25（节点号 加 对象 ID）。完成标准：库内容与配置一致

判停点：

- 条目数逼近 4000 → 停，内部库容量上限，转外部数据库方案（需外部 ASM）
- 主叫号带前缀对不上库 → 停，查 RSI 的 Callback Prefix 参数口径，统一号码格式
- 坐席号键查不到 → 停，核对直拨特性是否已配（键 3 的前提）

输出契约：三键数据条目 + 取用脚本 + 正反用例验证轨迹。

## B — 边界

- 4000 条为硬上限（n16）；超出须外部化，本卡不覆盖外部库语法
- 主叫号键支持通配/区段是便利也是坑：区段覆盖过宽会误命中，规划先于录入
- 坐席号键仅在直拨场景有意义（p137）
- 实验条目号码（02312122003、区段 1000-1999）为实验口径
- 数据维护入口在 CCS/CCSupervisor；批量维护工具与同步机制原书未涉及
