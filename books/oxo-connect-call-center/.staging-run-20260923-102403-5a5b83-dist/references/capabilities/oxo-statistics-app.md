# Statistics 统计应用与报表导出（OXO Connect）

## R — 原文依据

> "S1 hold-on threshold value: 10 seconds (default value) S2 hold-on threshold value: 40 seconds (default value)"（p190）
> "Export of statistics files • Binary files • Used only by the Statistics application. ... • CSV files • Useful for clients who want to have customized statistics"（p202）
> "Statistics storage capacity up to 14 months"（p28）

出处：OXOCXTE107EN p185-209。

## I — 自述

统计应用是三件套里的报表端。用之前先核对两个等待阈值：S1=10 秒、S2=40 秒（默认值），以及"溢出前等待计时"开关——它们定义了统计口径里"短等待/长等待"的分界。应用本身：装好后经 Configuration 菜单连 OXO 主 CPU（统计文件存放在主 CPU 上），用 ACD Admin 密码登录，主界面图标分 ACD 统计（组/坐席两维）、线路统计、来话统计、导出、工作目录。查询套路统一：选对象（组或坐席）→ 选日期段 → 选图形/表格 → 在 Synthesis 菜单切换指标（来话量/应答量/绝对值/百分比/时长）。报表可手动打印或按 printing profiles 自动打印；数据可导出为 binary（仅本应用可读，用于取全量离线分析）或 CSV（给外部工具做定制报表）。

## A1 — 书中案例

**查询与导出实验**（p203-209，厂商实验）：装应用（ACD_X.X\alcatel\call_center\Statistics_manager）→ 首连 192.168.1.246 + English + Acdc1064 → 点 "ACD" → Group Statistics：Statistic tab 勾组 1/2/3 选日期 → Graphic options 选 Colour + 3D Bar → Synthesis 分别看 Incoming calls / Answered calls，Number 菜单看 Absolute value / Time → Agent Statistics：Agent 选 All、Group 勾 1/2/3，看 Summary/Number of calls 与 Summary/Average duration → Export 图标选 binary 或 CSV、路径与日期范围导出。

## A2 — 未来触发

使用情境：客户要话务量月报；班长要坐席接听明细；对接 BI 需要原始数据；统计数字口径有争议（S1/S2 分界）。
语言信号：报表 / 统计 / statistics / 来话量 / 应答率 / CSV 导出 / S1 S2 / 坐席绩效 / 月报。

与相邻能力区分：坐席实时状态 → Supervisor 监控能力；本能力管历史数据与报表。

## E — 可执行步骤

输入契约：统计维度（组/坐席）、日期范围、输出形式（看板/打印/导出格式）。缺日期范围与口径先询问。

1. 核口径：OMC 侧确认 S1=10s、S2=40s（默认）与溢出前等待开关——与客户对齐"短等待/长等待"分界定义。完成标准：口径书面确认。
2. 安装：下载 ACD_X.X\alcatel\call_center\Statistics_manager → setup.exe。完成标准：安装完成。
3. 连接：Configuration → "PBX Server" → 填 OXO IP → 语言 → 确认 → 输 ACD Admin 密码 → 点 "ACD"。完成标准：图标全部亮起。
4. 组统计：Group Statistics → Statistic tab 选组与日期 → Graphic options 选 Color/3D Bar → Synthesis 切换 Incoming calls / Answered calls；Number 菜单看 Absolute value / Time。完成标准：报表数字可读。
5. 坐席统计：Agent Statistics → Agent 选 All + 组勾选 → 日期 → Summary/Number of calls 与 Summary/Average duration。完成标准：坐席明细可读。
6. 打印：手动（Statistics 菜单 → Printing）或配置自动打印（两个 Automatic printout 图标 + printing profiles）。完成标准：按需输出。
7. 导出：Export 图标 → 选格式（binary：本应用离线分析用；CSV：外部工具定制报表）→ 路径与日期 → Export。完成标准：文件落地可打开。

判停点：统计为空 → 先确认日期段内有话务且应用已成功从主 CPU 取数（连接步骤重做），不要先怀疑报表功能。

输出契约：统计报表（截图/打印件）或导出文件 + 口径说明（含 S1/S2）。

## B — 边界

- 留存上限 14 个月（p28）：超期数据原书未给恢复手段，重要报表定期导出归档。
- binary 导出仅本应用可读——客户要"自己分析"一律给 CSV。
- Line statistics 与 Calls statistics 两个图标（线路忙时率/来话统计）原书未展开实验，仅知功能存在（p192）。
- 自动打印依赖打印 profiles 配置正确，故障排查原书未覆盖。
