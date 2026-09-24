# 多设备用户与 Twinset（主副站、状态语义、快速移机）

## R — 原文依据

> "The twinset feature (also called tandem) is a logical association between two sets: a main set and a secondary set … The number of sets can be extended up to 4 in a multi device user configuration"（p353）
> "ON CREATION OF THE MULTI DEVICE ASSOCIATION, ALL DATA (CALL FORWARDINGS, CALLBACKS, MESSAGE DEPOSITS, ETC.) ARE CANCELLED ON THE SETS."（p366）
> "To perform a rapid call shift, the set which is in idle state dials the Twinset Get Call prefix … the remote party do not detect the change"（p363）

出处：ENTPXTE401EN p352-371。

## I — 自述

一号多机：主站+至多 4 个副站的逻辑关联（twinset 为 2 台的特例/旧称），主站号即多设备号；主副都必须 multiline。

1. **机型矩阵**：主站 NOE IP/TDM/IPDSP/SIP(SEPLOS)/DSU；副站另可 DECT、MIPT、REX（每多设备仅 1 台 DECT、1 个 REX）；禁用模拟/S0/话务台/ACD 分配坐席/寻线组成员/夜转/客房
2. **呼叫行为**：主副号同响先接停响；副号只响副站；忙=主站全线忙；Partial busy=True 则任一话机忙即算忙
3. **监督降级**：Specific supervision=True 后监督变为状态监督（按键显示 MAIN/SECONDARY/TOTAL BUSY，不再振铃提示）
4. **REX 与振铃控制**：REX 振铃可用激活/停用前缀（示例 651）；Ring Secondary REX in Parallel 控制主为 IPDSP 时副 REX 是否同响（默认 True）
5. **主站退服三参数**：Forward if set OOS（COS）+ Overflow to sec tandem if main OOS（系统参数）+ Ring all its secondar. if main oos（COS，生效依赖前两项）；参数在主站退服期间修改不生效，要等恢复后再退服才按新值走
6. **快速移机**：空闲侧拨 Twinset Get Call 前缀（示例 652，Local features+COS），通话无感迁移（对端听不出、屏显不变）

## A1 — 书中案例

**配置与验证**（p365-371，实验口径号码）：

1. 前置清理：主站退出办公桌共享角色、删相关键；确认两机各有多把主号 multiline 键
2. 主站声明：Users/主号 → Tandem Directory Number=第 1 副站号、Main set in the tandem=True、Attached multi device 最多再加 3 台
3. 同页配 Partial busy（默认 False）/Ringing in partial busy（默认 Long）/Specific supervision（默认 False）
4. 副站核对：自动显示 Tandem DN 与 Main set=False
5. 建快速移机前缀（示例 652）+COS 放行；呼入接听后另一空闲侧拨 652 验证无感迁移
6. 主站退服演练：配三参数后断主站，验证来话转副站/副站同响
7. 核验：zdpost d 主号 看 multi_device_main/tandem_mcdu/tandem_principal 等字段

## A2 — 未来触发

使用情境：办公+居家双机；DECT+话机组合；"手机化办公但保留话机号"；快速移机（会议室接一半挪工位）；主站故障时的来话兜底。

语言信号：multi device / twinset / tandem / 主站 / 副站 / secondary set / rapid call shift / Twinset Get Call / 652 / partial busy / specific supervision / REX / 651 / 主站退服。

与相邻能力区分：工位漫游（人动号不动）→ desk-sharing（路由卡）；监督键本身 → 多线监督能力；副站装机动(DECT/REX)属 Starter 装机域。

## E — 可执行步骤

输入契约：机型清单（主/副站类型与限制）、用户数据备份（关联会清数据）、前缀与 COS。目标机型在禁用清单 → 判停。

1. 备份与前置：记录两机现有呼转/回叫/留言；确认 multiline 键位。完成标准：可回退、键位就绪
2. 声明关联：主站填 Tandem DN/Attached multi device（合计至多 4 副）。完成标准：副站侧自动回显关联
3. 状态与振铃：按需求配 Partial busy/Ringing/Specific supervision/REX 振铃参数。完成标准：行为实测符合
4. 快速移机：建 Get Call 前缀+COS 放行+实测无感迁移。完成标准：移机中对端无感知
5. 退服兜底：三参数联动配置并演练。完成标准：主站退服后来话按预期到副站

判停点：

- 存量用户改造（如从办公桌共享转多设备）→ 停，先做步骤 1 备份（关联是破坏性操作）
- 想配第 2 台 DECT 或第 2 个 REX → 硬限制各 1，换其他副站类型
- 主站退服期间改三参数"没生效" → 机制如此（冻结到下次退服），不是配置丢失
- 副站数据想单独改 → 复制到副站的数据不可再改，改主站

输出契约：生效的多设备关联（zdpost 证据）+ 移机/退服演练记录 + 用户数据变更说明。

## B — 边界

- 关联创建清空两机全部数据且复制数据不可改（p366 大写警告）——破坏性操作
- 副站静音振铃仅 IP/TDM NOE 支持（DECT/SIP/REX 不适用，p359）
- 每多设备限 1 台 DECT、1 个 REX；WBM 上第 1 副站用 Tandem DN 字段、其余走 Attached（p354/p367）
- 前缀 651/652 为书内示例值，现场以 Prefix Plan 实查为准
- 具体监督降级行为与多线监督键的联动详见多线监督能力卡
