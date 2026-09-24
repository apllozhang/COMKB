# ACD 维护命令箱（adm_acd、agacd、hybvisu、pildstctx、pgctx、acdsup、spadmin）

## R — 原文依据

> ""agacd" command: agacd + Agent dir. number"（p127）
> "Command adm_acd … option 2 + 1 for pilots list / 4 for waiting queues list / 5 for statistics pilots … option 5 + 6 for skills and domains list / 7 for call profile list / 8 for authorized, unauthorized list / 9 for internal database"（p128）
> "To display dynamic data • adm_acd IP@ of ASM server -salb • option 28 • number: calling number (CLID) • *: to list all the calling numbers"（p257）
> "hybvisu -f all … DATA_TRANS : the link is established and ready to transport data"（p341-342）

出处：OTCCXTE101EN p127-128, p176, p257-258, p336, p341-342, p405, p563-564, p576, p583, p590。

## I — 自述

mtcl 会话下的排障命令族（OXE console）：

| 命令 | 用途 | 关键用法 |
|---|---|---|
| agacd <坐席号> | 查单个坐席 ACD 数据 | 直接收坐席目录号 |
| adm_acd | ACD 对象与数据总入口（直连 AFE） | option 2 看对象（1 Pilot/4 队列/5 统计 Pilot）；3 看处理组；4 看人员；5 看 ACR 数据（6 技能域/7 呼叫档案/8 名单/9 内部库）；11 Dump TERMINALS；15 软件包/许可 |
| adm_acd <ASM IP> -salb | ASM/alb 动态数据 | option 21 坐席统计；option 28 ASM 记忆（输 CLID 查单条，* 列全部） |
| adm_acd <CCS Server IP> -servccs | 经服务器接入的 CCS | option 10 看客户端清单与 maxCli/maxConnected |
| compvisu sys | 链路话音参数 | Direct Link 状态、H323、RTP Direct、VAD/CNG |
| hybvisu -f all / -f <节点号> | ABC-F 直连链路状态 | 四态 IDLE/SYN_REQ/SYN_ACK/DATA_TRANS；High/Low 带宽档；接入数 1-24 |
| pildstctx <Pilot 号> / pgctx <Remote PG 号> | 专用 Pilot / Remote PG 上下文 | Remote PG 互助排障抓手（p336） |
| acdsup | Remote PG 开闭状态 | mtcl 下执行（p336） |
| spadmin | 许可核对 | RTI 103 号包等（p388） |

三处 IP 缺省均为 localhost（=Call Server 地址）。经典组合：链路（hybvisu）> 对象（adm_acd option 2）> 坐席（agacd/-salb 21）> 记忆（-salb 28）> 互助对象（pildstctx/pgctx/acdsup）> 接入（-servccs 10）。

## A1 — 书中案例

**三条排障链中的命令实战**：

1. LCA 记忆核查（p257/p272）：adm_acd 192.168.1.3 -salb，option 28 输主叫号码查单条，* 列全部；kill alb 后 28* 复核为空
2. Remote PG 排障（p336/p341-342）：hybvisu -f all 确认 DATA_TRANS；pildstctx 32602 与 pgctx 31851 看对象上下文；acdsup 查 Remote PG 开闭
3. CCS Server 验证（p583/p590）：ps -edf|grep serv_ccs 查进程；adm_acd 192.168.1.70 -servccs，option 10 核对 "cnx= 1, afe= 1" 与客户端在列

## A2 — 未来触发

使用情境：想知道 OXE 上有哪些 Pilot/队列/处理组；查坐席 ACD 状态与统计；LCA 记忆核查与清理；链路状态判读；Remote PG 与 CCS Server 排障。

语言信号：adm_acd / agacd / hybvisu / compvisu / pildstctx / pgctx / acdsup / spadmin / option 28 / -salb / -servccs / DATA_TRANS / Dump TERMINALS / 记忆 / 坐席统计 / mtcl。

与相邻能力区分：链路断了的互助行为与水位参数转 Remote PG 卡；ASM 记忆的路由语义转 ASM 脚本卡（路由卡）；CCS 界面侧操作转对应业务卡。

## E — 可执行步骤

输入契约：OXE console（mtcl）访问权、对象编号或主叫号码等查询键。

1. 定位问题域：链路/对象/坐席/记忆/互助/接入/许可。完成标准：选定命令入口
2. 链路类：compvisu sys + hybvisu -f all（或 -f <节点号>）。完成标准：读出四态与带宽档
3. 对象类：adm_acd 按 option 树查 Pilot/队列/统计 Pilot/处理组/人员。完成标准：对象清单在手
4. 动态类：adm_acd <ASM IP> -salb option 21/28；互助对象 pildstctx/pgctx/acdsup。完成标准：动态数据可解释
5. 接入与许可：-servccs option 10；spadmin 或 adm_acd option 15。完成标准：客户端与许可状态可核对

判停点：

- 输出与本书 option 编号对不上 → 停，option 编号以现场版本为准（f15 conditions），先核版本再对照
- kill alb 前未记录 PID → 停，PID 每台不同（5596 为实验口径），以现场 ps 输出为准（p14/n15）
- hybvisu 判读要下生产结论 → 停，High/Low 带宽与状态是实验口径，生产判读结合带宽规划（p20）
- 命令输出含敏感数据 → 停，截图/留档先脱敏（号码、拓扑）

输出契约：命令输出摘录（脱敏）+ 判读结论 + 后续动作建议（转对应业务卡处理）。

## B — 边界

- 本卡是命令字典与判读入口；命令背后的业务语义（互助水位、ISM 排序、记忆路由）在对应业务卡
- option 编号、命令输出格式以 R10.15 为口径，跨版本可能变化；mgr 菜单（Inter-Nodes Links）路径同样随版本漂移
- adm_acd 直连/带参三形态的 IP 缺省 localhost（=Call Server）；远程查询要显式给 IP
- 状态类输出（DATA_TRANS/blocked/open）是瞬时快照，排障时要与呼叫测试同时观察
- 生产环境执行 kill 类操作前走变更流程；本卡不含任何写操作命令
