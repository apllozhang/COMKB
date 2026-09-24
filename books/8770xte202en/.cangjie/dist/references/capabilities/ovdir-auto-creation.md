# 目录树搭建与 PCX 自动创建（三开关、UID 构造、自动继承）

## R — 原文依据

> "Tree structure made of Organization and Termination entries • Country • City • Company • Department —— Organization entries • Person • Group • Room —— Termination entries"（p63）
> "Create for users (OXE) To be enabled • Limit to real users (OXE) To be enabled • Create for user alias (OXE) To be enabled"（p105）
> "Alarm reception mode Select the mode Permanent IP connectivity. / Process directory To be enabled."（p107）
> "The entry Anderson Thomas already exists. No automatic creation for link 31023, oxe, abc1, ale."（p118）
> "After the cut and paste of the person Michel Vincent, its directory parameters have been automatically updated."（p122）

出处：8770XTE202EN p62-63, p74-76, p99-122。

## I — 自述

目录供给的主通道：PCX 侧建用户，事件到达 8770 后在指定位置自动建人员并建主链接。

- **目录树**：组织类条目（Country/City/Company/Department）作枝干，终止类（Person/Group/Room）作叶子；建树入口在 Directory 应用 Company 页签右键 Create
- **三层开关联合生效**（任一缺失即静默不工作）：

| 层 | 入口 | 要点 |
|---|---|---|
| 全局参数 | Administration > Application Configuration > Application Settings > Directory Admin > AutomaticCreation | Create for users / Limit to real users / Create for user alias 三项启用 |
| 节点级 | Configuration 应用 OXE 节点 > Data Collection | Automatic creation 启用 + Location for automatic creation 选默认路径 |
| 事件前提 | OXE 节点 > PCX 页签 | Process directory 启用 + Alarm reception mode=Permanent IP connectivity |

- **UID 唯一性**：默认构造"名+姓"，目录内唯一；撞名即拒建并告警（Alarms 应用 NMC > nms > LDAP server 可查）。解法：该 PCX 的 Data Collection 页签把 UID construction 改为 Extension（名+姓+分机号）
- **UID 构造三约束**：按 PCX 分别设置；只对自动创建生效（手工建人员不走该构造）；改回 None 后，新建的同名人员会再次冲突
- **自动继承**：Cut/Paste 人员到新部门后，组织属性（城市/部门）自动更新
- **类型转换代价**：Person 转 Room 等会删除密码、照片、手机等专属属性与经理/助理链接（p78）

## A1 — 书中案例

**自动创建与 UID 防同名实验**（p99-122）：

1. Directory 应用建树：France 下建 Brest/Colombes，各建 Department（实验口径）
2. Administration 应用开 AutomaticCreation 全局三开关
3. OXE 节点 Data Collection：勾 Automatic creation，默认路径选 Department 1
4. PCX 页签确认 Process directory 启用、告警接收为 Permanent IP connectivity
5. Configuration 界面建 Visio Room 用户（31022），Event 页签见事件、目录见人员
6. Specific Telephone Services 建 CC：MKT/Training/TSS（实验口径）
7. 建五个用户（31000/31001/31003/31004/31005），Rights 页签绑 CC
8. Directory 应用 Department 1 下核验五人自动落地
9. 建同名用户 31023 Anderson Thomas，Alarms 页查 "already exists" 拒建告警
10. 按书提示删 31023，Data Collection 把 UID construction 改 Extension
11. 重建 31023/31024：目录出现 UID 带分机号后缀的两个 Thomas Anderson
12. 实验收尾把 UID construction 改回 None；Cut/Paste 人员核验组织属性自动更新

## A2 — 未来触发

使用情境：规划公司目录树；PCX 建了用户目录没出人；同名员工拒建；Visio Room/别名用户要不要建；人员挪部门属性要不要手动改；误建的人员怎么变 Room。

语言信号：自动创建 / automatic creation / 目录树 / directory tree / Location / UID construction / 同名 / homonym / 撞名告警 / Extension 构造 / Department / Country / City / Cut Paste 继承 / Visio Room / user alias。

与相邻能力区分：

- OXE 节点本身没同步 → OXE 注册能力
- 链接类型与 CC 继承语义 → 链接与改名能力
- 批量外部数据导入 → LDIF 工具能力

## E — 可执行步骤

输入契约：OXE 已注册同步（OXE 注册能力前置）、目标组织树结构、UID 同名评估。OXE 未同步 → 判停先回注册能力。

1. 建树：Directory 应用按 Country/City/Department 层级右键创建。完成标准：目标树成形
2. 开全局三开关：Administration 应用 AutomaticCreation 下三项启用。完成标准：三项为启用态
3. 配节点：Data Collection 勾 Automatic creation 并选 Location 默认路径。完成标准：路径指向目标部门
4. 开事件前提：PCX 页签 Process directory 启用 + Permanent IP connectivity。完成标准：两项就位
5. PCX 建用户带 CC，等事件后在 Directory 核验人员与主链接。完成标准：人员出现且链接建立
6. 同名处理：出现 already exists 告警时，该 PCX 改 UID construction=Extension 后重建。完成标准：同名共存且 UID 带分机号
7. 收尾：实验/试点结束把 UID construction 改回 None 并记录。完成标准：参数回归基线

判停点：

- 五处检查（两前提+三开关+UID）任一没配 → 自动创建静默失败，先补配置再谈故障（n46 排障序）
- 客户有大量同名员工 → 直接按 Extension 构造交付，不要逐个告警救火；同时告知手工建人不走此构造
- 需要保留 Visio Room 的密码/照片再转 Room → 转换会删数据（p78），先手工记录再操作
- 告警面板有拒建记录但用户已重建 → 先删告警对应旧条目评估，避免新旧人员并存的歧义

输出契约：可自动供给人员的目录树 + 开关配置清单 + 同名处理记录（构造方法与回退状态）。

## B — 边界

- UID construction 只对自动创建生效且按 PCX 独立设置（n03）：多 OXE 环境要逐个配置
- p120 原书 UID 描述排版勘误（nr-02）：第二用户 UID 应为 31023 口径，引用时注明
- 类型转换删除人员专属属性与关系链接（n01）：转换前先导出或记录
- Location 只决定自动建人的默认挂载点；组织调整后的属性继承靠 Cut/Paste（p122），无批量移动向导
- 实验树结构（France/Brest/Department）为教学约定（实验口径），生产按客户组织设计
