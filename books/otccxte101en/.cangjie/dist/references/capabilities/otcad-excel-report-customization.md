# Excel 报表模板定制（FormPil 模板、Custom 工作表、粒度陷阱）

## R — 原文依据

> "Open the file corresponding to the Ccdistribution object under: \\Program Data\\Alcatel\\CCSupervisor\\Excel\\Formats • FormPil.xls pilot • FormAgt.xls agent … FormPS.xls statistic pilot"（p534）
> "Copy from General tab a structure spreadsheet from B7 to D43 and paste it in the Custom worksheet … Paste to Custom tab, the links from B8 to D39"（p537-538）
> "NO!, because only 1 table form has been created, so with the granularity of ½ an hour, you will retrieve only the transition from 0:00 to 16:00."（p542）

出处：OTCCXTE101EN p531-554。

## I — 自述

CCS 出报表的机制：取数写入临时 .XLS，结构来自 Formats 目录的模板。模板按对象分 11 种：

| 模板 | 对象 |
|---|---|
| FormPil | Pilot |
| FormAgt | 坐席 |
| FormTeam | 处理组 |
| FormpAg / FormpGT | 每坐席/Pilot 组 |
| Formpgo | Other 类型组 |
| FormSyst | 中继 |
| FormCod / FormCods | 事务码（3 位）/明细事务码 |
| FormPS / FormPePS / FormPpPS | 统计 Pilot 及变体 |

定制原理三句话：在模板里加一张 Custom 工作表；从 General 复制结构区（B7:D43，3 列=时段时间/已接/放弃）粘贴；再对值区"选择性粘贴链接（Paste Link）"引用 General 的值——数据仍由 General 承载，Custom 上随便加图表改样式。

粒度陷阱（n30）：General 表结构约 24 行（按小时覆盖全天）；½ 小时粒度一天要 48 行——单张 Custom 表只能链到第一张表单，只覆盖 0:00-16:00，全天细粒度必须在 Custom 再建第二张表链到 General 的第二表单。

生效与回滚：模板在 CCS 启动时加载，改完必须关闭并重开 CCSupervision（n32）；官方流程要求先把原件改名 FormPil_old.xlsm 留底再另存出同名新件（n31）。

## A1 — 书中案例

**FormPil 定制与出表**（p544-554）：

1. Formats 目录把 FormPil.xlsm 改名 FormPil_old.xlsm 留底，打开后另存回 FormPil.xlsm
2. 打开 FormPil.xlsm 启用宏内容（Enable Content）
3. 右键 General 页签 > Insert > Worksheet，把新表改名 Custom
4. 拷结构：General 选 B7:D48 复制，到 Custom 的 B7 粘贴
5. 拷链接：General 选 B7:B39 复制，Custom 的 B7 用 Paste Link；再 General C7:D43 同法粘贴链接
6. Custom 选 C7:D43 插二维柱形图，改标题"Total received calls"，图例移右，系列改名"Calls received in open state"/"Calls received in blocked state"
7. 关闭模板，关闭并重开 CCSupervision 使新模板生效
8. Statistics > Excel > Pilot：选 Pilot 31600、模板全选（含 Custom）、Daily、粒度 1/2 小时、激活方式选 Excel Display + Keep Excel links，出报表核对 Custom 页呈现

## A2 — 未来触发

使用情境：客户日报要自定义图表/公司 VI 配色；要把某几个计数器单独成图；½ 小时粒度报表下午数据缺失；模板改坏了要回滚。

语言信号：Excel 报表 / 模板 / template / FormPil / Formats / General / Custom / Paste Link / 粘贴链接 / 粒度 / granularity / ½ 小时 / Daily / Keep Excel links / 图表 / 系列。

与相邻能力区分：离线话务票据明细转 CCTA 卡；日统计的产生与口径转 SPM 部署卡；报表 KPI 定义在书外。

## E — 可执行步骤

输入契约：CCS 已装（Excel 组件选 Yes）、Formats 目录可写、客户要的图表/列清单与粒度。

1. 备份：目标模板改名 *_old 留底，再另存回原名。完成标准：回滚件存在
2. 加 Custom 工作表并启用宏。完成标准：Custom 页签出现
3. 拷结构区（B7:D48）到 Custom。完成标准：表头与时段骨架齐
4. 对值区 Paste Link 引用 General。完成标准：改 General 数据 Custom 跟随变化
5. 加图表并按客户 VI 改样式与系列名。完成标准：图表呈现预期
6. 关模板并重开 CCS。完成标准：出报表对话框能看到新模板
7. 按目标粒度出表；½ 小时粒度核对是否覆盖全天。完成标准：日报完整或已补第二张链表

判停点：

- 客户要"实时刷新"的 Excel → 停，Excel 报表是统计报表（日/粒度），实时需求走 Soft Panel/CCS Real time
- ½ 小时粒度只有 0:00-16:00 → 停，粒度陷阱（n30），补第二张链表而不是改取数
- 模板改坏且无 *_old 留底 → 停，恢复只能重装 CCS 或找同版本拷贝，先向客户说明代价
- 客户要定义新 KPI → 停，模板只能重组现有计数器，KPI 定义在书外

输出契约：定制后的模板（含 *_old 备份）+ 出报表参数记录 + 样张报表。

## B — 边界

- Formats 目录同时存在 .xls（讲义）与 .xlsm（实验宏版）两种扩展名口径；以现场 CCS 版本实际文件为准
- 改模板必须重开 CCS 生效（n32），与 ccs.ini 修改同属"改配置必须重启"家族
- 模板结构（B7:D48 等坐标）为 R10.15/Ed07 口径，CCS 升级后坐标可能漂移，定制前先核对
- 报表中的话务数据属客户敏感数据，分发与留存按客户数据保护要求管理
- Excel 组件（安装时选 Yes）与本机 Excel 版本兼容性书内未展开，宏告警按现场策略处理
