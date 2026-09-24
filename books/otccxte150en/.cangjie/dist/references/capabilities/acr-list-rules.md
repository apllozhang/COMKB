# ACR 授权与非授权名单规则（静态名单五式给值、动态 LIST 名单）

## R — 原文依据

> "AUTHORIZED_LIST: Brings up agents out of a static list. It can be indexed by: A call context index (CALLING, CALLTAG, AGENT_NUMBER) • An integer (its logical number in OmniTouch, %index to define) • Its name (its name in OmniTouch, "String to define") • Agents list: Brings up an explicit agents list … LIST variable: Bring ups agents found in the variable LIST"（p57）
> "100 lists (Authorized / Unauthorized) maximum • 30 Agent per list • No limit of Agents, when the content of the list is defined in the script • An Agent belonging to a list must have at least 1 active skill"（p61）
> "The String is case sensitive!"（p74）

出处：OTCCXTE150EN p51-81。

## I — 自述

名单规则圈定或排除坐席，属可组合规则，可与 ISM 等串接：

1. **授权名单（Authorized List）**：只让名单内坐席接；默认名 WList_x
2. **非授权名单（Unauthorized List）**：排除名单内坐席；默认名 BList_x
3. **给值五式**：呼叫上下文索引（CALLING/CALLTAG/AGENT_NUMBER，名单跟着主叫号、标签或被拨坐席号走）；整数索引 %index（名单 ID 0-99）；名字索引 "String"（大小写敏感）；脚本内显式坐席列表（无数量上限）；LIST 变量（动态拼装）

硬规格：

| 项目 | 上限/约束 |
|---|---|
| 名单总数（授权+非授权合计） | 100 个（ID 0-99） |
| 每列表坐席数 | 30 |
| 脚本内显式列表 | 无上限 |
| 名单内坐席 | 须有至少 1 个活动技能，否则被排除 |

名单本体在 CCS 的 ACR Data 建；运维查看用 adm_acd 选项 24（节点号 加 名单号）。典型组合：授权名单加 ISM 单 APPLY 链式——名单先过滤、技能再精选（双 APPLY 会令名单失效，见综合规则组合能力）。

## A1 — 书中案例

**授权名单脚本（c03 前半）**：

1. ACR Data 建授权名单 List_1（ID 0），内容为坐席 3x502
2. 写脚本 Authoriz：Statement 定义条件（Home 技能级别大于 2），构件 RULE_AUTHORIZED_LIST
3. 名单参数用 %index=0，或改用脚本内显式列表加 3x501
4. 呼家险 Pilot：Home 级别 9 条件真，名单 0 生效，3x502 接
5. 呼车险 Pilot：档案无 Home 条件假，显式名单生效，3x501 振铃

**非授权名单脚本（c03 后半）**：

1. 建非授权名单 Beginner，内容为 3x501；场景：10 点前排除 Beginner、10 点后排除主管
2. 写脚本 Unauthor：时间条件 Statement 加 RULE_UNAUTHORIZED 构件
3. String 索引注意大小写；也可用 UNAUTHORISED_LIST 加 %整数（名单 ID）
4. Debugger 显示时间 12:45:12 条件为假，非授权名单生效
5. 实时改条件为大于 10 点再呼：31501 不可接，其余有活动技能坐席可接

## A2 — 未来触发

使用情境：只让资深坐席接某类呼叫；把新手在高峰时段排除；名单跟着主叫号走（大客户专属名单）；动态拼名单。

语言信号：授权名单 / Authorized List / 非授权名单 / Unauthorized List / WList / BList / 名单索引 / CALLING 索引 / 大小写敏感 / 显式坐席列表 / LIST 变量名单。

与相邻能力区分：名单与技能怎么组合才生效，见 综合规则组合能力（单 APPLY 语义）；脚本调试，见 脚本编辑器能力；名单数据来自查询，见 内部数据库或外部数据库能力。

## E — 可执行步骤

输入契约：名单成员清单（坐席须已有活动技能）、业务条件（时间/技能级别）、脚本编辑权限。名单总量逼近 100 或单列表超 30 时先做规划。

1. ACR Data 建名单（授权或非授权），录坐席。完成标准：名单保存且坐席有活动技能
2. 写脚本构件 RULE_AUTHORIZED_LIST 或 RULE_UNAUTHORIZED，五式给值选一。完成标准：保存传输激活
3. 显式列表与静态名单混用时核对成员并集。完成标准：成员口径与业务一致
4. Debugger 验证正反用例：名单内、名单外、条件切换三种情形。完成标准：命中与排除行为正确
5. 动态名单用 LIST 变量拼装后传入规则。完成标准：Debugger 里 LIST 内容正确
6. 运维核查 adm_acd 选项 24。完成标准：名单内容与配置一致

判停点：

- 名单内坐席不振铃 → 先核该坐席活动技能（无技能即被排除），再核名单 ID 与索引
- 名单加 ISM 组合不生效 → 停，查 APPLY 数量，转综合规则组合能力
- 照抄书面前先在编辑器核对关键字拼写（AUTHORIZED/AUTHORISED 混用，nr-04）

输出契约：名单配置 + 名单规则脚本 + 正反用例验证轨迹。

## B — 边界

- 名单规则给值的 String 索引大小写敏感（教材以感叹号强调）
- 关键字两种拼法混用为原文现象，以编辑器实际接受为准（n09/nr-04）
- 名单规则不影响 ISM 成本计算口径；混跑优先级问题归综合规则组合能力
- adm_acd 选项号出自原书维护页；名单上限 100/30 为原书 Issue 01 口径，细则以 Feature List 为准
- 名单跟随主叫号时号码格式须与 CALLING 一致（前缀口径见 RSI 参数）
