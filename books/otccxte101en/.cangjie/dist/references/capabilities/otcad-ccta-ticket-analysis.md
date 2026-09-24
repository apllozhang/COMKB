# CCTA 话务票据分析（安装、导入 .Z、过滤与 ASCII 导出）

## R — 原文依据

> "2 types of tickets exist: • Tickets "events" • Displays the changes of the objects state … • Tickets "communications" • Displays the information of communications: date and time of the call, duration of conversation, agent responding to the call, called pilot, cause of end of the call"（p483）
> "The Importation that permit to import daily and automatically the CCd communication and events tickets … • The Ticket Tracer which aims is the visualization"（p484）
> "PABX Enter the IP address of the Call Server … The files will be dropped in C:/Program Data /Alcatel /Ticket Analyzer/ (name or IP address of the pcx)."（p493-494）

出处：OTCCXTE101EN p480-497。

## I — 自述

CCTA（Contact Center Ticket Analyser）是 CCd 票据的离线分析工具，解析 .Z 文件，装后得到两个程序（\\Program Files(x86)\\Alcatel\\Ticket Analyser）：

| 工具 | 职责 | 要点 |
|---|---|---|
| Importation | 从 PCX（每日自动）导入通信/事件两类票据 | 首连声明站点：PABX=Call Server IP、User=mtcl、Use SSH 按 OXE 实际、Tickets type=both |
| Ticket Tracer | 可视化过滤分析并导出 | File > Open（Tickets on PC，按 PABX IP 拼路径）> 过滤器 > 报表 > Functions > File ASCII 导出 |

数据口径（p488，书中只给样例码）：

| 字段 | 口径 |
|---|---|
| 结束原因 End cause | 共 40 种；样例 0=主叫挂机、1=系统挂机、26=坐席挂机 |
| 呼叫类型 Call type | 共 10 种；样例 0=非 ACR、1=ACR 呼叫 |
| 过滤维度 | Headers selection（列选择）+ Object selection（对象筛选）+ 激活 |

导入落盘：C:/ProgramData/Alcatel/Ticket Analyzer/<PCX 名或 IP>（原文路径含空格，见 nr-07）。离线分析不占 CCS 连接。

## A1 — 书中案例

**从安装到 ASCII 报表**（p491-497）：

1. Client10 从 NAS 运行 ccta_setup.msi，向导默认项装完
2. 启动 Importation，首连声明站点：PABX=192.168.1.3、User=mtcl、Password 按现场填、Use SSH 不勾、Tickets type=both
3. 点 Test 连接确认后导入，核对 C:/ProgramData/Alcatel/Ticket Analyzer/192.168.1.3 出现 .Z 文件
4. 运行 Ticket Tracer：File > Open > Tickets on PC，PABX 填 192.168.1.3，Type=Communication，选起止日期后 Validate
5. 过滤器选 Long Ticket、全部对象、ID Mao、Column，Validate 生成报表
6. Functions > File ASCII 定路径导出，Notepad/Excel 打开核对结束原因等字段

## A2 — 未来触发

使用情境：复盘某天为什么放弃率飙高；客户要呼叫明细报表（谁接的、多久、为什么结束）；核对 ACR 呼叫占比；离线分析不想到生产 CCS 上跑。

语言信号：CCTA / Ticket Analyser / 票据 / ticket / .Z / Importation / Ticket Tracer / 结束原因 / end cause / 呼叫类型 / ASCII / 明细 / 话务分析 / Long Ticket。

与相邻能力区分：CCS 实时统计与 Excel 日报转 Excel 报表卡；实时看板转 Soft Panel 卡；SPM 部署问题转 SPM 部署卡。

## E — 可执行步骤

输入契约：OXE 票据机制开启且有在产话务、一台 Windows 客户端、OXE 的 mtcl 凭据（现场实际值）。票据未产生 → 停，先确认 OXE 侧票据机制开启。

1. 装 ccta_setup.msi（默认路径）。完成标准：Ticket Analyser 目录下两个程序可用
2. Importation 声明站点并导入（Tickets type=both）。完成标准："Import process is successful"、.Z 文件落盘
3. Ticket Tracer 打开票据：按类型与起止日期加载。完成标准：记录列表出现
4. 过滤器选列与对象后出报表。完成标准：可见主叫/坐席/Pilot/时长/结束原因等列
5. Functions > File ASCII 导出并核对内容。完成标准：文本可读、字段与报表一致

判停点：

- 要 40 种结束原因全表 → 停，书中只有样例码（0/1/26），全表在 CCTA 工具文档，不编造
- 要实时监控 → 停，CCTA 是离线工具，实时需求走 Soft Panel/CCS Real time
- 导入要 SSH → 停，按 OXE 侧实际开启情况勾选；实验环境未开 SSH（g48）

输出契约：可复现的票据导入配置 + 过滤后的明细报表 + ASCII 导出文件（复盘或交付附件）。

## B — 边界

- 书示登录 mtcl/mtcl 是文档示例（p493），实验 OXE 实际口令不同（Superuser2580*，实验口径）；生产按现场凭据
- 结束原因 40 种/呼叫类型 10 种只给样例码，其余编码不外推（p33 口径）
- 路径书写以实际文件系统为准（ProgramData 无空格）；原文含空格写法见 nr-07
- CCTA 版本与 OXE 票据格式随版本演进，导入失败先核对版本配套（书内未展开版本矩阵）
- 票据含主叫号码等敏感数据，导出文件的分发要按客户数据保护要求管理（书内未覆盖，n40 同族边界）
