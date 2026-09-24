# OmniVista 8770 OXE 配置界面高效操作（搜索/冻结/网格/导入导出）

## R — 原文依据

> "Right click on the 'OXE' or 'OT', Select the 'Configure' option"（p159）
> "Right click on the desired column (ex. Local Features), Select 'Freeze' ... The column is frozen and is locked on the left"（p160）
> "Select 'Export All Grids' or 'Export Selected Grid(s)' ... 2 types of extension are available : .txt or .prg"（p165）

出处：8770XTE200EN p158-167（Configuration interface - OmniPCX management）。

## I — 自述

OXE 图形配置界面（Configuration 应用右键 OXE > Configure）的六类提效手法，日常配置效率的地基：

- 搜索：Search 区按条件检索（如 Prefix Meaning = Local Features），列出全部匹配行
- 冻结列：右键目标列 > Freeze，该列锁定在左侧，横向滚动时保持可见（对照参数名看值不迷路）
- 网格/文件切换：选中行后 Switch grid display 按钮在 File 视图与 Grid 视图间切换
- 属性选择：Grid 视图右键行 > Attributes Selection，取消不需要的列（如 Prefix Meaning/Prefix Information）后重跑搜索刷新；全选可恢复
- 图形视图：右键用户 > Graphical View > 选可编程键，下方字段配置 Function（如 Programmed/Multiline）、Content（如号码）、Mnemo 显示文本、UTF-8 Mnemo、Locked 锁定
- 导入导出：树导出（选条目右键 Export，.txt 或 .prg）与树导入（选目标文件夹右键 Import）；网格导出（Export All Grids / Export Selected Grid(s)）与网格导入（Import Grid）

- 底层概念：8770 与 OXE 间 CMISE 数据交换基于 MIB（Object Model）；thick client 首连下载 MIB 存本地（Object Model Save 管理），Access Profile 变更后须删本地 MIB 重载（见安全管理卡）

## A1 — 书中案例

**配置界面操作实验**（p158-167）：

1. 右键 OXE > Configure 打开配置界面
2. Search 区按 Local Features 检索前缀
3. 冻结 Local Features 列，横向滚动验证锁定
4. 选中 Wake-up/appointment reminder 行切换 File/Grid 视图
5. Attributes Selection 取消两列后重跑搜索验证隐藏，再全选恢复
6. 右键用户 Brigitte Baker 开 Graphical View 配置可编程键（Function/Content/Mnemo/UTF-8/Locked）
7. 树导出 export1（.txt）> 改动 > 树导入验证
8. Grid 导出 export_grid.txt > 改动 > Import Grid 导入，来源目录生成日志文件

## A2 — 未来触发

使用情境：批量核对 OXE 参数；给用户批量配键前预览；导出配置留档或跨环境比对；新工程师上手教学。

语言信号：Configure 界面 / Freeze / 冻结列 / Switch grid display / Attributes Selection / Graphical View / 可编程键 / Mnemo / Export Grid / Import Grid / .prg / Object Model。

与相邻能力区分：节点接入声明（节点接入卡）；建户与 profile（用户开通卡）；本能力管配置界面的操作手法，不改变任何配置语义。

## E — 可执行步骤

输入契约：目标 OXE 已声明可同步、操作者具备对应 Access Profile 权限。

1. 进入界面：Configuration 应用右键 OXE > Configure。完成标准：配置界面打开
2. 检索定位：Search 条件过滤。完成标准：目标行可见
3. 冻结参照列：右键列 > Freeze。完成标准：滚动时参照列恒在
4. 视图瘦身：Attributes Selection 取消无关列。完成标准：刷新后仅留关注列
5. 键位预览：Graphical View 核对或预配可编程键。完成标准：Function/Content/Mnemo 正确
6. 留档/搬运：树与网格导出（.txt/.prg）。完成标准：文件生成
7. 回灌：Import/Import Grid 选文件。完成标准：数据出现且来源目录有日志

判停点：

- 权限不足看不到对象 → 先查 Access Profile 与 OmniPCX 4400 Access Level（安全管理卡），不要盲试
- 导入文件格式不符 → 用本书导出文件为模板，不要手造格式
- 改了 Access Profile 后界面无变化 → 删本地 MIB 重载（安全管理卡），不是本卡手法问题

输出契约：配置快照文件（树+网格）+ 键位预览记录 + 操作手法培训清单。

## B — 边界

- 本卡是操作效率手法：所有改动的生效语义（继承/同步/权限）由对应能力卡覆盖
- Graphical View 配键与 Key profile 自动配键是两条路径（后者见用户开通卡），现场按规模选择
- WBM Configuration 应用无本地管理员配置权限、无 SSH/Telnet 直连、一次连一个 OXE——批量图形操作在 thick client
- 实验用户（Brigitte Baker）与实验环境为教学口径，见 book/overview
