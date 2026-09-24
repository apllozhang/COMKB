# LDIF 导入导出与管理工具管道（三范围备份、六件套命令、删除跟随）

## R — 原文依据

> "An LDIF import • Allows creating and modifying data • Does not remove data"（p85）
> "When you export with the 'Branch…' option, all company directory data are exported. This export process is the most complete."（p163）
> "The LDIF management tools are located in the folder 8770\bin"（p542）
> "It can be used to delete entries that were not in the last LDIF import for synchronization with another directory"（p547）
> "IF YOU FORGET SUCH MODIFICATION AND RUN THE GO.BAT FILE, A BAD STRUCTURE WILL BE CREATED ... DELETE THE ROOT 'ABS'."（p555）

出处：8770XTE202EN p85-86, p156-169, p536-558。

## I — 自述

LDIF 是 8770 目录批量数据的通用管道：图形界面管备份恢复，命令行六件套管外部目录对接。

- **GUI 导出三范围 × 两目的地**：

| 范围 | 内容 | 用途 |
|---|---|---|
| Entry | 仅选中条目一条 | 单条目迁移 |
| Sublevel | 仅直接下级 | 局部结构 |
| Branch | 本条目+全部子树（最完整） | 备份必用 |

目的地：本地驱动器（即时）或服务器（走 Scheduler 可定期，落盘 C:\8770\Client\data\import）。导入入口 Import > Immediate on local drive > Add and modify，导入只增改不删除。

- **CLI 六件套**（8770\bin）：

| 工具 | 作用 | 关键参数 |
|---|---|---|
| ConvertLdif | 补父条目/改属性与类名/加派生属性 | -mc 类映射 -ma 属性映射 -da 派生 -p 路径 |
| ExportLdap | 目录到 LDIF | -b 基准 DN -h -p 389 -D -w -s sub |
| ImportLdap | LDIF 到目录 | -c 出错继续 -e 语法日志 -r 导入日志 |
| Ldif2Csv / Csv2Ldif | 与 Excel 数据采集互转 | 文件重定向 |
| PurgeLdap | 按过滤器删条目 | -f purgefilter.conf |
| LinkDn | 从属性值算 DN 链接（assistant/manager/see also） | -f link.conf |

- **标准管道**：CSV > Csv2Ldif > ConvertLdif > ImportLdap >（LinkDn 建链）>（PurgeLdap 删除跟随）；管理员 DN 模板 uid=adminnmc, cn=Administrators, cn=8770 administration, o=nmc
- **删除跟随机制**：da.conf 给每条导入条目写 misc10 时间戳标记；purgefilter.conf 定义"misc10 不等于本次标记"；purge.bat 执行后外部目录删了的人 8770 跟删——补上"导入永不删除"的缺口
- **高危点**：p.conf 的 o=abs 根名必须改成本客户根名；忘改就跑 go.bat 会造坏结构，且改回重跑无效，须 dirmanag.exe 删 ABS 根重来

## A1 — 书中案例

**LDIF 备份恢复与工具管道实验**（p156-169, p552-558）：

1. Entry/Sublevel/Branch 三范围依次导出 France，逐一核验文件内容
2. 服务器调度导出：Simple job 选 Now，文件落 C:\8770\Client\data\import
3. 删除 Department 1，选 Brest 导入 Branch LDIF 完整恢复
4. 解压 LDIF1.zip 到 c:\ldif1，读 go.bat 三命令说明
5. 按本机改 ImportLdap 参数（服务器名、adminnmc DN、密码）
6. Csv2Ldif 转换后核验 tmp.ldif 结构与 Address 值
7. 研读并修改四个 conf，重点把 p.conf 的 o=abs 改成客户根名
8. 执行 go.bat 三连，核验目录树按采集数据成形
9. 读 link.conf，改 link.bat 后执行，核验 assistant/manager/see also 链
10. 删 directoryUS.txt 中 Smith David 行模拟外部删除
11. 跑 go.bat 后查 misc10 变化，再跑 purge.bat，核验条目消失
12. export.bat 导出核验；Domino 管道（LDIF2.zip）按同范式演练

## A2 — 未来触发

使用情境：目录数据定期备份；误删分支要恢复；从 HR 系统/旧目录批量导入人员；外部目录删了人 8770 要跟删；给人员批量建经理/助理关系；LDIF 导入的坏结构怎么救。

语言信号：LDIF / 导入 / 导出 / import / export / Branch / 备份 / 恢复 / Csv2Ldif / ConvertLdif / ImportLdap / PurgeLdap / LinkDn / go.bat / link.bat / purge.bat / misc10 / purgefilter / p.conf / dirmanag / 坏结构。

与相邻能力区分：

- 单机数据备份恢复（复制的数据修复也用 LDIF）→ 复制能力
- MSAD 双向同步 → MSAD/Azure 管道能力
- GUI 里手工建链 → 链接与改名能力

## E — 可执行步骤

输入契约：操作目标（备份/导入/删除跟随）、数据源文件、8770 服务器管理员 DN 与密码（客户提供）、conf 文件编辑权。

1. 备份（例行）：选 Branch 范围导出到本地或配 Scheduler 定期导出。完成标准：LDIF 可回导
2. 恢复：选目标父条目 > Import > Add and modify 导入。完成标准：分支完整回来
3. 批量导入：准备 CSV > Csv2Ldif > 按客户改四个 conf（根名第一步改）> 转换 > 导入。完成标准：树成形
4. 建链：按数据采集的助理/经理电话字段配 link.conf 跑 LinkDn。完成标准：关系链建立
5. 删除跟随：配 misc10 标记与 purgefilter，外部删后跑 purge。完成标准：两端一致
6. 校验：每次导入后抽核条目数、关键字段与关系链。完成标准：抽样通过

判停点：

- p.conf 根名忘了改且已跑 go.bat → 停止重跑：改回也无效，须 dirmanag.exe 删 ABS 根后重来（n40）
- 期望导入能删条目 → 语义不成立：导入永不删除（n41），删除走手工删或 PurgeLdap 机制
- 导出文件比预期小 → 记住空值属性不导出（p540）：回导不会清空字段，备份口径据此评估
- 管理员密码只有教材值 → 实验口径红线（nr-08）：向客户索取真实凭据后再执行

输出契约：备份恢复演练记录 + 管道产物（LDIF/日志）+ 删除跟随验证 + conf 变更清单（含根名核对证据）。

## B — 边界

- 导入只增改不删除是第一性约束：外部同步的删除语义必须显式设计（misc10+purge 或等价机制）
- p.conf 根名是全书最重警告点（n40）：写入操作 checklist 第一步
- misc10/purgefilter 细节依赖随书实验文件（LDIF1.zip）：生产化需自行设计标记字段与过滤逻辑
- domino 管道为 Notes 场景示例（p558）：同范式适配其它目录，不在书内逐字段展开
- 服务器导出落盘路径 C:\8770\Client\data\import 与工具目录 8770\bin 为实验安装口径，按现场盘符调整
