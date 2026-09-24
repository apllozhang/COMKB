# 六类链接与改名语义（基数规则、成本中心继承、断链修复）

## R — 原文依据

> "Primary link: 1 entry => 1 user, 1 user => 1 entry ... Name, first name and cost center name are identical • Only one primary link can be defined for each entry"（p69）
> "In case of primary link, the name and / or first name modification must be done via the Company directory"（p79）
> "he inherits from the Jean Dupont cost center. Now DECT Dupont cost center is MKT."（p130）
> "the primary link between Paul Tregueur and the phone 31001 is broken. A new primary link is created between Michel Durand and the phone 31001."（p145）
> "Using the Users application, thick or web client, is the best way to update and modify the first name and last name of a person."（p151）

出处：8770XTE202EN p68-72, p79-84, p123-155。

## I — 自述

人机绑定的根是主链接，其余链接都是挂在其上的扩展。六类链接基数与匹配条件：

| 链接类型 | 基数 | 匹配/语义 | 成本中心 |
|---|---|---|---|
| Primary 主链接 | 1 entry : 1 user（每条目仅一条） | 姓名+名字+成本中心三项一致 | 双向同步 |
| Multi-device 多设备链 | 1 entry : n users | 同步后自动建，多话机共用一条目 | 随主链接 |
| Secondary 副链 | 1 entry : n users，1 user : 1 entry | 异名同 CC（典型 DECT） | 建链瞬间继承主链接 CC |
| Fax 传真链 | n : n（传真机可共享） | CC 不同、姓名不同 | 互不影响 |
| Miscellaneous 杂项链 | 1 entry : n users | 异名同 CC（数据终端/Modem） | 双向同步 |
| Additional resources 附加资源链 | 同主链接性质但可多条 | 4760 迁移"一人多主链"场景 | 同主链接 |

- **数据更新方向**（主链接）：姓名/名字单向目录到 PCX；成本中心双向；ISDN 号从 PCX 取回
- **改 CC 硬规则**：目录侧改 CC 时 PCX 必须已有同名 CC，否则拒绝并告警回滚；正确顺序是先在 PCX 建 CC（Specific Telephone Services > 1 > Cost Center）
- **四入口改名行为对比**：

| 改名入口 | 链接 | 成本中心 | 后果 |
|---|---|---|---|
| Directory 应用 | 全保留 | 保留 | 需手工同步改 User id |
| Users 应用（厚/WBM） | 全保留 | 保留 | Name 同步更新——原书钦定最佳入口 |
| Configuration 界面 | 主链接断裂 | — | 按新名自动生成新人，需修复 |
| 直接改 PCX 话机数据 | 同上 | — | 同上（姓名方向是目录到 PCX） |

- **断链修复流程**：删除新生成人员 → 旧人员 Settings links > Primary link > Edit > Search 选中分机重建
- **改名细节**：改姓名时必须连 User ID 一起改，否则目录 key 与姓名脱节

## A1 — 书中案例

**链接管理与四入口改名实验**（p123-155）：

1. 补建 PCX 用户 31002（DECT）与 31011（Fax Set），删除其自动生成的人员条目
2. Jean Dupont 右键 Settings links > Secondary link 页签，搜索双击 31002 建副链
3. 核验：DECT Dupont 的 CC 从 Training 变 MKT（继承主链接）
4. Fax link 页签同法挂 31011；核验 Fax Set CC 保持 TSS 不变
5. Users 应用给 Pierre Williams 加 secondary set 31105（多设备链）
6. 目录侧把 Jean Dupont CC 改 Training：主链接与副链用户跟随变化
7. 目录侧把 Paul Tregueur CC 改不存在的 BEAN：PCX 拒绝告警，CC 保持原值
8. 目录侧把 Jean Dupont 改名 Albert Simon：31000 姓名同步更新、链接全保留
9. Configuration 界面改 31001 姓名：主链接断裂、生成新人 Michel Durand
10. 修复：删除新人，旧人员 Primary link > Edit > Search 选中 31001 重挂
11. Users 应用改名 Michel Vincent：链接与 CC 全保留（最佳入口实证）
12. WBM 同法改名核验：目录与用户同步更新

## A2 — 未来触发

使用情境：一人多话机（DECT/软话机）怎么绑；传真机能不能共享；改了名字目录没变/链接断了；改成本中心被拒绝；4760 迁移过来的人有多条主链；改 CC 后界面显示没变。

语言信号：primary link / 主链接 / secondary link / 副链 / DECT / fax link / 传真链 / multi-device / 多设备 / additional resources / 4760 / cost center / 成本中心 / 改名 / rename / 断链 / 修复 / Settings links / User id。

与相邻能力区分：

- 自动建人没发生 → 自动创建能力
- CC 改不动是因为 PCX 没有 → 本卡 E 段覆盖拒绝分支
- Web 目录展示哪些属性 → 保密能力

## E — 可执行步骤

输入契约：目录人员与 OXE 用户已存在（自动创建/同步前置）、目标链接类型、CC 是否已在 PCX 建。

1. 判型：按终端类型与姓名/CC 异同选链接类型（对照本卡 I 段六类表）。完成标准：类型有依据
2. 建链：Directory 右键人员 Settings links，选对应页签 Edit 后搜索分机确认。完成标准：链接建立
3. 核验 CC：Configuration 界面关开 Users 文件夹强制刷新后看值（不刷新会误判）。完成标准：CC 符合继承规则
4. 改 CC：先在 PCX 建 CC（若不存在），再目录侧修改。完成标准：无拒绝告警
5. 改名（推荐）：Users 应用或 WBM 改 Last name/First name/User ID 三件套。完成标准：链接与 CC 保留、Name 更新
6. 断链修复（Configuration 入口误改后）：删新生成人员，Primary link Edit Search 重挂分机。完成标准：主链接恢复

判停点：

- 目录侧改 CC 报 PCX 拒绝告警 → 停止重试，先回 PCX 建 CC 再改，告警详情在 Alarms 应用核对（n07）
- 发现主链接断裂生成新人 → 不要手工给新人重建数据，走"删新人+旧人重挂"标准修复（n05）
- 想给传真链继承 CC → 语义不成立：传真链不继承不改 CC（n09），需要计费归属就换副链方案
- 只能从 Configuration 界面改名 → 向客户说明风险并按修复流程预案操作，优先改用 Users/WBM

输出契约：正确的链接关系 + CC 归属核验记录 + 改名操作记录（入口与 User id 同步证据）。

## B — 边界

- Configuration Users 文件夹显示旧缓存（n08）：核验必须关开刷新，"改了没生效"多数是它
- 副链与传真链的 CC 语义差异是计费归属问题（n09）：选型时向客户讲清
- 多设备链经 Users 应用建（Add a secondary set）；副链/传真链在 Directory 应用 Settings links 建——入口不同不混用
- WBM Users 应用需 Unified Management 许可（p35）；无许可时走厚客户端 Users 应用
- 附加资源链仅服务 4760 迁移场景（p71），日常交付不应主动使用
