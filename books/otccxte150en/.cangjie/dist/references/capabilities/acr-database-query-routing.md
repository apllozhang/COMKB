# ACR 外部数据库查询路由（SQL 六构件、ODBC 32 位、存储过程、LCA 持久化）

## R — 原文依据

> "A specific "SQL" tab is available in the ASM script editor • 6 building blocks … In the same script, up to 16 different databases can be used"（p376）
> "The ASM Server is not able to make a connecting using a 64-Bit ODBC Driver"（p399）
> "The result of an instruction could be tested by the content of the variable SQL_RESULT who could receives the following values … SQL_SUCCESS … SQL_ERROR … SQL_NOT_FOUND"（p385）
> "by default, the "last_called_agent" is kept only in the ASM server memory; which means that if the server reboots, all the data are lost"（p434）

出处：OTCCXTE150EN p374-394, p395-407, p427-452。

## I — 自述

外部数据库让 ACR 突破内部库 4000 条上限，并把动态数据持久化。前提：外部 ASM 加 32 位 ODBC 加 167 号许可。

SQL 六构件编程模型：

1. **USE_DATABASE**：建连接（ODBC 源名必填；SQL/Oracle 类加用户名密码，Access 类免凭据）；连接随脚本激活建立、去激活断开
2. **SQL_REQUEST**：发 SELECT 列 FROM 表 WHERE 谓词，或 CALL 存储过程（IN/OUT 参数；目标库须支持嵌入式过程）
3. **结果测试**：IF DB[x] 判连接；SQL_RESULT 三值——SUCCESS 有结果 / ERROR 请求错 / NOT_FOUND 无匹配行
4. **SQL_DATA**：把列值映射到本地变量（STRING/INTEGER 64 个、REAL 32 个、TIME/DATE/TIMESTAMP 各 16 个）
5. **fetch 循环**：SQL_START_FETCH 到 SQL_END_FETCH 成环取行；SQL_BREAK_FETCH 提前退出；SQL_ROW_COUNT 计行数
6. **取行策略**：无 BREAK 全表扫；配 LIST 变量收集全部匹配行，不配则只留最后一行（逐行覆写）

WHERE 子句与存储过程 INPUT 可用 26 项呼叫上下文变量（CALLING/CALLTAG/CALLED/PRIORITY/SEQUENCE/PILOT_NUMBER/WAITING_ROOM_NUMBER/AGENT_NUMBER/等待历史类/带下标变量类/技能档案类）。

LCA 持久化原则：LCA 默认只活在 ASM 内存，重启即失。把存储过程嵌进脚本首段，每次呼叫把主叫号与上次接听坐席写入外部表；查询改读该表——重启 ASM 后"上次接听坐席"依然有效。

## A1 — 书中案例

**Access 读库（c14）**：

1. 建 Access 库 acr.accdb 表 Records（ID/Name/First_Name/Calling/Agent/VIP），存为 .mdb
2. 32 位 ODBC 建 System DSN（源名 ACR，Access 驱动免凭据）
3. 脚本：USE_DATABASE 后 SQL_REQUEST SELECT 三列 WHERE CALLING 匹配
4. SQL_RESULT 为 SUCCESS 进 fetch，SQL_DATA 映射三列
5. VIP=1 的主叫屏显姓名，随后走 ISM；Debugger 核 CALLING 与库一致

**SQL 读写与持久化（c18，20 构件两段）**：

1. 前置：SSMS 建库 acr_sql 表 Customer（Caller 主键，三列带默认值），装载 updateCalling 过程
2. 32 位 ODBC 建 DSN（SQL Server 驱动，SQL 认证登录）
3. 脚本 Part 1：连接、CALL updateCalling 写库、SELECT 查库、fetch 映射、无结果屏显 Unknown 走 ISM
4. 脚本 Part 2：Last_Agent 非默认时拼 VIP 或 No VIP 加姓名屏显、LIST[%1]=(AGENT{串}) 拼名单、授权名单加 ISM
5. 首呼：表空走 ISM 且过程写库；二呼：读库走名单路径
6. 停再启 ASM 服务清内存后第三呼：LCA 从库还原，名单路径依旧生效
7. Profiler 侧以登录名过滤抓 exec updateCalling 作数据库侧证据

## A2 — 未来触发

使用情境：客户数据在 SQL Server 要按主叫号查 VIP；要"上次接听坐席"在 ASM 重启后不丢；内部库 4000 条不够；查询多行结果。

语言信号：外部数据库 / External Database / ODBC / DSN / 32 位 / SQL_REQUEST / USE_DATABASE / fetch / SQL_ROW_COUNT / SQL_RESULT / 存储过程 / updateCalling / LCA 持久化 / 167 许可。

与相邻能力区分：内部 4000 条内的小数据，见 内部数据库路由能力；外部 ASM 没部署，见 外部 ASM 部署能力；数据库安装与建表本身，见 通用 DBA 操作（书外）。

## E — 可执行步骤

输入契约：外部 ASM 已部署、目标库与表结构、167 号许可、32 位驱动可得性。缺外部 ASM 先回外部 ASM 部署能力。

1. 核前提：adm_acd 选项 61 确认 ACR_SQL(167) 锁可用。完成标准：许可锁在
2. 目标库建库建表（先建库后建 DSN）。完成标准：表结构与默认值符合设计
3. 32 位 ODBC 建 System DSN，Test Connection 通过。完成标准：DSN 名与脚本一致
4. 写脚本：连接、结果测试、fetch、映射、LIST 收集、BREAK 策略。完成标准：三值路径（有/无/错）都有分支
5. 挂 ACR Pilot 激活（连接随激活建立）。完成标准：adm_acd 选项 60 显示已连接
6. 正反测试：库内命中、库外落空、故意写错请求。完成标准：三路径轨迹正确
7. （持久化）装载存储过程并嵌入脚本首段。完成标准：重启 ASM 后 LCA 仍生效

判停点：

- 连不上库 → 按顺序查：脚本是否激活（连接随激活建立）、许可锁、32 位 DSN、网络
- 查到的是最后一行 → 正常，未配 LIST 时逐行覆写；要首条匹配配 BREAK 加 ROW_COUNT
- 大表查询慢 → 停，无 BREAK 是全表扫，补 BREAK 或收窄 WHERE
- SQL 报 NOT_FOUND 但数据在 → 停，核 CALLING 格式（前缀/大小写）与 WHERE 谓词

输出契约：可用的外部库脚本 + DSN 与许可记录 + 三呼持久化验证证据。

## B — 边界

- 32 位 ODBC 是硬约束（两处强调，n36）：现代 64 位服务器上找齐 32 位驱动本身是交付风险项
- 同一脚本最多连 16 个库；连接生命周期=脚本激活到去激活（n40）
- 存储过程仅当目标库支持嵌入式过程（Access 不支持，n38）
- 教材示例过程不维护 Name/VIP 默认值（'noname'/'0'，n41），示例屏显依赖人工维护；默认值大小写两处写法不一致（nr-05）
- 库表结构、DSN 实验值、SQL 登录均为实验口径；生产必须强口令、最小授权、凭据不进明文脚本（原书安全缺席，整改方向为推断，n50）
- SSMS/Access 界面操作属通用 DBA 技能，书内仅给与 ACR 相关的字段与过程约定
