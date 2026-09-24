# Soft Panel 可视化配置（背景/视图/面板/挂件/消息/告警视图）

## R — 原文依据

> "A soft panel display is made of one or several views • Each view is alternately displayed for a number of seconds … Customized from the view itself using Firefox • other web browsers are not allowed for views customization"（p421）
> "Enter this URL: http://<SoftPanelSrvIP>:<port>/wbm/displayPanel.htm?name=<soft panel name>"（p427）
> "With alarms, two actions can be realized on real time value condition … Send an email when a threshold is reached • Additionally, a specific view can be displayed on Soft Panels when the alarm is raised"（p450）

出处：OTCCXTE101EN p418-479。

## I — 自述

Soft Panel 显示端是四层对象模型，自上而下配置：

| 层 | 入口 | 要点 |
|---|---|---|
| 背景 Background | Soft Panels > Backgrounds | 4 张预装+自定义上传 |
| 视图 View | Soft Panels > Views | 选背景后进入定制页（回管理/插挂件/换背景三钮）；定制仅限 Firefox |
| 软面板 Soft Panel | Soft Panels > Soft Panel | 名称+认证 No+绑定一个或多个视图；多视图按定时器轮播 |
| 显示端 | displayPanel.htm?name=<面板名> | LED 墙板另支持 ALE 串口（1 行 12 字符）、IP/串口（2/4/6 行 16 字符）与 AMS 面板 |

挂件全集速查：

| 挂件 | 关键参数 |
|---|---|
| Gauge / HorizontalGauge | Min/Max、Th1 绿转黄、Th2 黄转红、半圆角度 ≤180 |
| Chart | 水平条/垂直条/饼/折线；折线=历史视图（2000 值或 24 小时封顶）；饼图 Display Value 三态 |
| Simple / Text / Time / Image | 计数器直读、文本、日期模板、图片 |
| Table | 行列+单元格级文本/计数器/表头 |
| HTML | 仅 http:// 地址可嵌入（https 不行，n26） |
| Barometer | Th1/Th2 三图主题九选，缺省 weather、50/80 |
| Agent（AgentWidget） | OTCC SE 专属，绑定坐席，状态色随 CCS；依赖三统计 |
| 消息区 | 常驻特殊挂件，字体走 panel2.css 的 .MessageDisplay |

消息与告警：Messages 定色/闪烁+显示时段（Display time/date/Duration/Repeat everyday）；告警四步=建专用告警视图 > Alarms > New Alarm（对象类型五选+条件+阈值+Validity timer+Notification interval，0=只发一次）> 发邮件动作 > 告警视图替换动作（可挂音频）。

全局样式：param.js（historySize=2000、historyTimer=120000ms、图表色系）、panel2.css（背景色 div.mainPage、消息字体）、mainPanel.css（Logo 位置），改前备份。

## A1 — 书中案例

**从背景到告警的完整配置**（p455-479，实验命名 MyView/MySoftPanel）：

1. Chrome 开 http://localhost:9060/wbm，admin/admin 登录（实验口径）
2. Backgrounds > Add a background 上传 sunset.jpg
3. Views > New View：Name=MyView、Background=sunset.jpg，保存后进入视图定制页
4. 视图内插挂件：HorizontalGauge/Chart/Simple/Table/Time/AgentWidget 按需拖放，红叉删除、拉角缩放、黄方块置顶置底
5. Soft Panel > New Soft Panel：Name=MySoftPanel、Authentication=No、绑定 MyView
6. Messages > New Message：Name=MsgWelcome、Color=red、Flash mode=Yes，指定面板与显示时段
7. Alarms > New Alarm：计数器引用+条件阈值+Validity timer+Notification interval，配邮件收件人并指定告警视图与显示秒数
8. 显示端开 http://<SPM IP>:9060/wbm/displayPanel.htm?name=MySoftPanel 核对轮播、消息与告警切换

## A2 — 未来触发

使用情境：客户大厅/机房上实时看板；等待超阈值自动切告警画面并发邮件；折线图看当天趋势；消息区放欢迎语或临时通告。

语言信号：Soft Panel / 墙板 / wallboard / 视图 / view / 挂件 / widget / Gauge / Chart / AgentWidget / 消息 / Message / 告警 / alarm / displayPanel / Firefox / Barometer / 历史曲线。

与相邻能力区分：SPM 服务器与 RTI/FlexLM 安装、统计不出数的排查转 SPM 部署卡；日统计对账转 SPM 部署卡；CCTA 离线票据转 CCTA 卡。

## E — 可执行步骤

输入契约：SPM 已部署且统计可订阅（前提走 SPM 部署卡）、Firefox 浏览器、看板内容清单（指标/阈值/告警收件人）。

1. 上传背景并新建视图，进入定制页。完成标准：视图有背景+Logo+消息区
2. 按内容清单插挂件并绑定统计（统计须已在 CCD Filters 勾选）。完成标准：制造话务后 1 分钟内数值更新
3. 新建软面板绑定视图，多视图设定轮播秒数。完成标准：displayPanel.htm 能打开并轮播
4. 配消息：内容/颜色/闪烁/显示时段。完成标准：面板在设定时段显示消息
5. 配告警：阈值+Validity timer+邮件+告警视图替换。完成标准：制造越限话务后面板切换且邮件到达
6. 需要调全局样式时改 param.js/panel2.css（改前备份）。完成标准：配色/历史窗口符合客户 VI

判停点：

- 客户要在视图定制页用 Chrome/Edge → 停，定制仅支持 Firefox（n25），管理台才可以其他浏览器
- 要嵌外部网站且其 URL 是 https → 停，HTML 挂件仅支持 http://（n26），内网页面先做可行性验证
- 要看超过 24 小时/2000 点的历史曲线 → 停，实时面板封顶，长周期趋势落到日报（Excel/日统计，n27）
- 要撤掉还在被挂件/告警引用的统计过滤器 → 停，先删光引用对象再撤过滤器（n24）

输出契约：可用的软面板（视图/挂件/消息）+ 告警规则清单 + 显示端 URL 与验收记录。

## B — 边界

- 视图定制仅限 Firefox（浏览器版本基线 120 起，p387/n25）；panel 端显示 Chrome/Edge 有列项差异（Edge 少 Panel PC 显示）
- LED 硬墙板字符容量按型号固定（1 行 12 / 2/4/6 行 16 字符），长内容先看硬件规格（p379）
- 统计按需订阅：只有被视图/计算数据/告警引用的统计才更新（n22）；新挂件首分钟不动是正常延迟
- 全局样式文件属服务器文件操作，改前备份；版本升级可能覆盖自定义 CSS/JS
- Barometer 三图主题目录与 1.png/2.png/3.png 命名为原书约定，自制主题按同名规则扩展（p445-446）
