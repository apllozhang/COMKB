# 数据库备份恢复与维护排障工具箱

## R — 原文依据

> "By default: daily backup at 5:45 AM • Can be re-scheduled • Local backup -> transfer of backup using SFTP is strongly recommended"（p721）
> "AS THE TELEPHONE APPLICATION IS ALREADY STOPPED, IT IS NOT POSSIBLE TO USE CS MAIN IP ADDRESS TO TRANSFER THE BACKUP FILE. CS PHYSICAL IP ADDRESS MUST BE USED FOR SFTP SESSION."（p733）
> "The 'oxetrace' tool is able to take Call Handling, SIP motor and network traces simultaneously … Technical support will usually request this 'infocollect' compressed file"（p740, p754）

出处：ENTPXTE400EN p720-756。

## I — 自述

灾备底线与一线排障抓手：

1. **备份对象**：MAO、语音指南、计费、话务历史、ACD、4645 数据（含/不含消息）、Linux 网络数据；自动备份每日 5:45（可改期）
2. **备份分区**（/usr4/BACKUP）：DAY+DAY-1..6（自动）、IMMED（手工）、OPS（许可）、WEEK-1..3、MONTH-1/2、FACTORY
3. **手工备份**：swinst Expert 菜单 4（Backup & restore）→ 1 Immediate → 选内容；SFTP（Binary、mtcl、端口 22）传 PC
4. **恢复四步**：停话务（此时 SFTP 必须用 CS 物理地址）、回传备份到 IMMED、Restore from IMMEDIATE、起话务；恢复三选项=secure restoration（先存当前库为回退档案）/restore Cloud and Rainbow services（实验室剥离客户云凭据）/clean up archive
5. **排障八件套**：oxetrace（三路抓包+自动解码打包 zip，需 3GB，<4GB 自动减轮转）、ippstat（IP 话机 1-22 项）、事件三件 incvisu/incinfo/syslog（外发 UDP 514）
6. **工具续**：securitystatustool（XML 安全全景，需话务运行）、infocollect（root，交支持标配 .tbz）、tcpdump（root，pcap 供 Wireshark）
7. **事件双口径**：incinfo GEA <事件号> 取权威释义；屏显/磁盘 usr4/incid/SNMP/syslog/Cloud Connect 五通道分发

| 工具 | 账户 | 用途 |
|---|---|---|
| oxetrace | mtcl | 三路抓包+解码打包 zip |
| ippstat | mtcl | IP 话机数据与开关（-noname 供 GDPR） |
| incvisu / incinfo | mtcl | 事件查询与权威释义 |
| securitystatustool | mtcl | XML 安全全景（含默认密码占比） |
| infocollect | root | 离线分析大包 .tbz |
| tcpdump | root | 定向抓包存 pcap |

## A1 — 书中案例

**备份与恢复实验**（p728-736，How-To）：

1. swinst Expert 菜单 4 做手工备份（mao+指南+计费）
2. FileZilla 用 Binary 从 /usr4/BACKUP/IMMED 传回 PC
3. 删几个用户制造库差异
4. Easy 7 停话务，系统重启
5. SFTP 改用 CS 物理地址 192.168.1.1 回传备份（Role 地址已失效）
6. Restore from IMMEDIATE：勾 secure restoration，Cloud/Rainbow 选 n（实验室剥离）
7. 完成后 clean up the archive，Easy 8 起话务
8. 核对被删用户已恢复，收尾

**排障工具演练**（p737-756，讲义命令序列）：

1. oxetrace 选场景问卷（如 "1 4 6 7"），复现问题后停止，取回 zip
2. ippstat 查 IP 话机状态与 MAC 清单
3. incvisu -t 20 看最近事件，incinfo GEA 3757 取释义
4. securitystatustool 输出 XML 安全全景
5. tcpdump host 过滤抓包存 pcap
6. infocollect 生成 .tbz 交技术支持

## A2 — 未来触发

使用情境：版本升级前备份；误删配置回滚；系统崩溃重建；ALE 支持要现场数据；话机批量离线排查；安全自查（默认密码占比）；"实验输出里的告警是不是故障"。

语言信号：备份 / backup / 恢复 / restore / IMMED / swinst 备份 / secure restoration / oxetrace / 抓包 / tcpdump / infocollect / incvisu / incinfo / syslog / securitystatustool / 事件号。

与相邻能力区分：建库与许可恢复见空库与许可能力；停话务操作本身见系统启停能力（路由卡）；话机日志（getlogs）见用户终端开通能力。

## E — 可执行步骤

输入契约：维护窗口（恢复需停话务）、备份存储位置（PC/网络盘）、问题现象描述与时间窗（排障场景）。恢复前确认手里备份的完整性，否则先补做备份。

1. 例行备份核验：确认每日 5:45 自动备份在跑，DAY 分区有当日档。完成标准：自动备份可用
2. 变更前手工备份：Expert 菜单 4 做 IMMED 备份并 Binary 传离设备。完成标准：回退点离开机器
3. 恢复执行（如需）：停话务后用物理地址回传，Restore from IMMEDIATE 按场景勾 secure/Cloud 选项。完成标准：起话务后业务与配置核对一致
4. 排障采集：按现象选 oxetrace 场景抓包或 tcpdump 定向，复现问题后停止取档。完成标准：trace 覆盖问题时间窗
5. 事件定位：incvisu 看事件流，incinfo 取权威释义，必要时 syslog 外发对接客户监控。完成标准：事件链可解释
6. 升级支持：安全全景（securitystatustool）+ infocollect 大包按支持要求提供。完成标准：支持受理所需材料齐

判停点：

- 恢复时 SFTP 连不上 → 停话务后 Role 地址失效（n08/n37），改用 CS 物理地址，这不是故障
- 备份文件传完校验失败 → 传输类型没用 Binary（n37），重新传输，不要强行恢复
- 磁盘剩余不足 4GB 跑 oxetrace → 会自动减轮转文件（p743），先清空间否则 trace 不完整
- 实验输出类告警（BAD PCMS CODE/unknown rack type/484）→ 先按 n43 判读"非故障现象"，用 incinfo 与业务结果定性，不要直接按事故上报

输出契约：可恢复的配置资产（备份台账）+ 问题档案（trace/事件/释义）+ 支持材料（如升级）。

## B — 边界

- 实验路径/地址（/usr4/BACKUP、物理地址 192.168.1.1）为实验口径；异地备份存储策略在书外
- 恢复的 "restore Cloud and Rainbow services" 选项在实验室选 n 防止用客户云凭据连生产云（n37）；生产按归属环境选择
- 深度日志分析与性能调优在 Advanced 课程；Cloud Connect 侧的远程诊断在 ENTPXTE402 范围
- infocollect/tcpdump 需 root；oxetrace 启动会复位既有 mtracer/traced/tcpdump（p743 注）
- 事件号随版本增减，释义以 incinfo 输出为准（p41 条目口径）
