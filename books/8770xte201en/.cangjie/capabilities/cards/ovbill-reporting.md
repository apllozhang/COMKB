# 报表生成、导出与定时（预定义报表、尺寸上限、邮件分发、累计报表、任务调度）

## R — 原文依据

> "Maximum number of lines in TXT format — 400 ... Maximum number of pages in PDF format — 50 ... Maximum number of lines in database — 100000"（p367）
> "The number of the SMTP port is optional if the default SMTP port number is used (default SMTP port = 25). Careful: no space between ':' and the TCP port number."（p374）
> "If the report instance is empty, it means that the cumulative counters have not yet been calculated."（p380）

出处：8770XTE201EN p358-383。

## I — 自述

报表应用按"定义 → 实例"工作，预定义报表必须 Copy/Paste 到个人目录才能生成；树上有三类节点：definition（定义）、generated（实例）、unmasked（解密版实例）。

- 尺寸上限六项（Preferences > Reports > Reports Preference）：TXT 400 行；HTML/PDF/EXCEL 各 50 页；X 轴 100 元素；数据库扫描 100000 行；超限在报表末尾显示截断提示
- 生成三入口：Generate Report（正常）、Generate report w/o mask（解密，需口令）、Schedule（定时，可同时打印/导出）
- 导出双通道：文件（TXT/HTML/PDF/EXCEL，默认文件名=定义名+生成日期）与邮件（多目的地逗号分隔）
- 邮件服务器参数：Mail server 填 FQDN 或 IP，可加 :端口（默认 25 可省，冒号与端口间不能有空格）；发件人默认 OmniVista，须填邮件服务器认识的地址；报表与 Tracking 告警邮件共用这套参数
- 累计报表依赖夜间算好的累计计数器：Daily Station Traffic 这类报表实例为空，先手工 Total calculation 补算再重新生成
- 定时任务：右键定义 > Schedule，可设 As Scheduled 时间、按日重复、Exclude Days 排除周六周日，任务落 Scheduler

## A1 — 书中案例

**报表全流程实验**（p366-383）：

1. 查六项尺寸上限并确认截断提示行为
2. Accounting 目录建个人文件夹 My Reports
3. 复制预定义 Duration by station 到 My Reports
4. 生成两个实例：过滤器 Date/Hour 与 Name/Call Type，一份全量、一份 This week
5. 右键实例 > Open to View 查看与翻页
6. Export 到文件：选 TXT/HTML/PDF/EXCEL，默认名=定义名+生成日期
7. 配邮件服务器（可带 :端口）与发件人后，Export 选 Email 通道发到实验邮箱并收信确认
8. 复制预定义 Daily Station Traffic 生成——实例为空，到 Accounting/traffic > Total calculation 手工补算后重新生成
9. 右键 Duration by station > Schedule：5:00AM、Daily、排除周六周日，任务落 Scheduler

## A2 — 未来触发

使用情境：给管理层出月度话费报表；报表发邮箱；报表太大被截断；定时自动出报表；累计报表是空表；预定义报表没法直接生成。

语言信号：报表 / report / 生成 / Generate Report / 导出 / export / TXT / PDF / EXCEL / 邮件 / mail server / SMTP。

补充信号：定时 / Schedule / Duration by station / Daily Station Traffic / 累计计数器 / Total calculation / 截断 / 400 行 / 50 页。

与相邻能力区分：从零造定义（字段/公式/图表）→ 报表定制能力；报表里号码被遮与解密 → 机密控制能力；本卡管"把现成定义跑起来、送出去"。

## E — 可执行步骤

输入契约：库内有票、个人目录可建、（邮件场景）邮件服务器可用。数据未入库 → 先回票据管道能力。

1. 建个人目录并从预定义报表 Copy/Paste 定义。完成标准：定义出现在个人目录
2. Generate Report 配过滤器生成实例。完成标准：实例可 Open to View
3. 大报表先核六项上限，必要时收窄过滤区间。完成标准：无截断提示或已确认可接受
4. 导出：文件通道选格式，或邮件通道配服务器/发件人后发送。完成标准：文件落地或收件确认
5. 累计报表为空时先 Total calculation 补算再生成。完成标准：实例有数据
6. 定时：Schedule 设时间/重复/排除日并 Apply。完成标准：任务出现在 Scheduler

判停点：

- 首日出报表为空 → 夜间计数器未算，手工补算或把验收排到次日，不当故障修
- 报表末尾出现截断提示 → 收窄区间或改用 Total counters 数据源，不静默交付半份报表
- 邮件发不出 → 三查：server:port 写法（冒号后无空格）、发件人是否被服务器认识、DNS 是否可用（不在则用 IP）

输出契约：报表实例清单（定义/过滤器/生成时间）+ 导出与分发记录 + 定时任务定义。

## B — 边界

- 六项上限为 Ed45 默认值可调（p367），但调大前先评估数据库扫描成本
- 邮件服务器为教学设施（Thunderbird/实验邮箱），生产用客户 SMTP（实验口径）
- 报表树的解密入口（w/o mask）依赖机密控制能力的账号与组配置
- 界面与预定义报表清单随版本漂移（Ed45 口径），升级后路径需复核
