# SIP 跟踪采集与维护排障（motortrace/oxetrace/mtracer/sipdump）

## R — 原文依据

> "(1)csa> motortrace 1 ... (1)csa> traced"（p313）
> "Enter the Relevant Question Indexes Separated by Space -> 2 ... Enter the folder name (will be created in /tmpd/) ? trace-1"（p315）
> "Warning IT IS NECESSARY TO HAVE TWO CONNECTIONS ON THE CALL SERVER: ONE FOR NAVIGATING IN THE 'sipdump' MENU AND THE OTHER IN ORDER TO GET THE RESULTS"（p321）
> "IF REQUIRED, USE THE FOLLOWING COMMANDS TO REINITIALIZE THE PROCESSES - dhs3_init –R SIPMOTOR (RECOMMENDED) - killall sipmotor. WARNING: YOU HAVE TO BE LOGGED AS ROOT"（p93）

出处：ENTPXTE403EN p287-327。

## I — 自述

排障四件套分工明确，状态类命令先行、信令采集收尾：

| 工具/命令 | 用途 | 要点 |
|---|---|---|
| sipregister / sipdict / sipgateway / trkstat | 状态四查 | 注册库（AOR+contact+剩余租期）/字典（type 2=Device、3=Extension）/网关全景/中继组 62 路 TS |
| motortrace N + traced | 轻量信令流 | 级别 0-b 十二档可调：1 基本、2 大流量观察、3 无流量定向深挖、4 +认证、5 +媒体、8 全部+传输+DNS；Ctrl-C 停 |
| oxetrace | 问题导向采集 | 七问菜单（Trunks/Endpoint/Audio/Display/Rainbow/Nomadic/Attendant）+actdbg 过滤；产出 /tmpd/ 三目录并自动打包 zip，sftp 取回进 Wireshark |
| mtracer | 应用级跟踪 | tuner km、+cpl +cpu +at、actdbg csip=on、mtracer -a；收尾 actdbg all=off 加 dhs3_init -R MTRACER |
| sipdump | 网关资源与呼叫态 | 17 项菜单：许可读数（实验 20/20、TLS 30/30）、呼叫清单、转储、强拆（代理发 BYE）、追踪过滤（过滤作用于 motortrace）；需双连接 |
| 恢复口径 | 进程/中继 | sipmotor 重启首选 dhs3_init -R SIPMOTOR（killall 需 root 属激进）；中继组不在服时可能要整机重启 |

- 注册即服务：注销/超时后 IP 置 0.0.0.0、终端 out of service——"话机不通"第一步查 sipregister
- 自动隔离记录看 /usr4/tmp/sipalarm.log（f003 告警）

## A1 — 书中案例

**四工具实操**（p312-327，How-To）：

1. motortrace 1 + traced，打 SEPLOS 31034 呼 NOE 31000，读 INVITE/100/180/200 OK 全事务，Ctrl-C 停。
2. oxetrace 进 1 Start Trace，按问题选号（例 2=SIP Endpoint），命名 trace-1，复现呼叫后 2 Stop、1 Keep（生成 /tmpd/TRACE-1_<时间戳>.zip）。
3. Filezilla sftp 从 /tmpd 取回 zip；pcap 进 Wireshark：SIP 过滤、看 SDP、Telephony/VoIP Calls 流程图。
4. mtracer：tuner km、clear-traces、+cpl +cpu +at、actdbg csip=on、mtracer -a 复现 51 立即呼转场景后收尾清理。
5. sipdump 双连接：菜单口看许可/呼叫数/呼叫清单，traced 口看结果；试强拆（Release a call）与追踪过滤（Add filter 串 31030@oxe.company.com）。

## A2 — 未来触发

使用情境：给 ALE 支持提工单要附证据；注册时序看不懂；要强拆挂死呼叫；只想要特定用户的信令；许可/资源余量核对。

语言信号：trace / 抓包 / motortrace / oxetrace / mtracer / sipdump / traced / 级别 / Wireshark / pcap / 强拆 / Release a call / 过滤 / sipregister / trkstat / sipalarm / dhs3_init / zip。

与相邻能力区分：编解码读数用 compvisu → 编解码卡；各业务域的配置根因（信任主机/DID/注册）→ 对应开通卡先查配置再抓包。

## E — 可执行步骤

输入契约：故障现象与复现路径、时间窗口、涉及分机/中继号。无法复现 → 判停约定复现窗口。

1. 查状态：sipregister/sipdict/sipgateway/trkstat 四查定位层面（注册/字典/网关/中继）。完成标准：层面判定
2. 轻量采集：motortrace 级别按流量选（1 少、2 大流量、3 定向），复现并读事务。完成标准：事务可读
3. 深度采集：oxetrace 按问题选号采集，Keep 生成 zip，sftp 取回进 Wireshark 分析。完成标准：pcap 与流程图在手
4. 定向深挖：需要应用级视图用 mtracer（记得收尾清理）；要过滤与强拆用 sipdump（双连接）。完成标准：证据齐
5. 收口：结论 + trace 文件归档；需升级 ALE 支持时附 zip 与复现步骤。完成标准：交付物成文

判停点：

- sipmotor 进程异常 → 先 dhs3_init -R SIPMOTOR，killall 留给 root 级激进场景（n52）
- 中继组不在服 → 可能要整机重启，先排窗口别硬磨（n44/n52）
- sipdump 只开一个连接 → 停，按 Warning 开双连接再操作

输出契约：信令级排障交付物（trace 文件 + 结论）+ 状态四查读数记录。

## B — 边界

- Wireshark 报文分析深度、SIP 协议逐字段课程在书外，本卡给 OXE 工具链用法
- sipdump 许可读数（20/20、TLS 30/30）为实验站点配置（p34），生产读数随许可而变
- motortrace 级别表为 p288 原文口径；verbosity 位图示例 1→0003a004
- 采集级别过高在大流量站点会放大负载，采完即停
