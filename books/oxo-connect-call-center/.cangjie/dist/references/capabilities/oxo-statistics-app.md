# Statistics 统计应用与报表导出（OXO Connect）

## R — 原文依据

> "S1 hold-on threshold value: 10 seconds (default value) S2 hold-on threshold value: 40 seconds (default value)"（p190）
> "Export of statistics files • Binary files • Used only by the Statistics application. ... • CSV files • Useful for clients who want to have customized statistics"（p202）
> "Statistics storage capacity up to 14 months"（p28）

出处：OXOCXTE107EN p185-209。

## I — 自述

统计应用是三件套里的报表端。三个要点：

1. **先核口径再用**：S1=10 秒、S2=40 秒两个等待阈值（默认值）+ "溢出前等待计时"开关——它们定义"短等待/长等待"的分界
2. **取数方式**：统计文件存在 OXO 主 CPU 上，应用须建连接检索；查询套路统一——选对象（组/坐席）→ 选日期段 → 选图形或表格 → Synthesis 菜单切指标（来话量/应答量/绝对值/百分比/时长）
3. **输出三种**：手动打印、按 printing profiles 自动打印、导出 binary（仅本应用可读，取全量离线分析）或 CSV（外部工具定制报表）

留存上限 14 个月（p28）。

## A1 — 书中案例

**查询与导出实验**（p203-209，厂商实验）

- 安装：下载 ACD_X.X\alcatel\call_center\Statistics_manager → setup.exe
- 首连：192.168.1.246 + English + Acdc1064 → 点 "ACD"
- 组统计：Group Statistics → 勾组 1/2/3 + 日期 → Graphic options 选 Colour + 3D Bar → Synthesis 看 Incoming calls / Answered calls → Number 菜单看 Absolute value / Time
- 坐席统计：Agent 选 All + 组 1/2/3 → 日期 → Summary/Number of calls 与 Summary/Average duration
- 导出：Export 图标 → 格式 + 路径 + 日期范围 → Export

## A2 — 未来触发

使用情境：客户要话务量月报；班长要坐席接听明细；对接 BI 需要原始数据；统计口径有争议（S1/S2 分界）。

语言信号：报表 / 统计 / statistics / 来话量 / 应答率 / CSV 导出 / S1 S2 / 坐席绩效 / 月报。

与相邻能力区分：坐席实时状态 → Supervisor 监控能力；本能力管历史数据与报表。

## E — 可执行步骤

输入契约：统计维度（组/坐席）、日期范围、输出形式。缺日期范围与口径先询问。

1. 核口径：确认 S1=10s / S2=40s 与溢出前等待开关，与客户对齐分界定义。完成标准：口径书面确认
2. 安装：下载 → setup.exe。完成标准：安装完成
3. 连接：Configuration → "PBX Server" → OXO IP → 语言 → 确认 → ACD Admin 密码 → 点 "ACD"。完成标准：图标全亮
4. 组统计：Group Statistics → 选组与日期 → 图形选项 → Synthesis 切指标。完成标准：报表可读
5. 坐席统计：Agent Statistics → 选 All + 组 + 日期 → 看 Number of calls / Average duration。完成标准：明细可读
6. 打印：手动（Statistics 菜单 → Printing）或自动（Automatic printout 图标 + profiles）。完成标准：按需输出
7. 导出：Export → 选 binary 或 CSV → 路径与日期 → Export。完成标准：文件落地可打开

判停点：统计为空 → 先确认日期段内有话务且连接成功（重做第 3 步），不要先怀疑报表功能。

输出契约：统计报表（截图/打印件）或导出文件 + 口径说明（含 S1/S2）。

## B — 边界

- 留存上限 14 个月；超期数据原书未给恢复手段——重要报表定期导出归档
- binary 仅本应用可读；客户要"自己分析"一律给 CSV
- Line statistics / Calls statistics 两个图标原书未展开实验，仅知存在（p192）
- 自动打印依赖 printing profiles，故障排查原书未覆盖
