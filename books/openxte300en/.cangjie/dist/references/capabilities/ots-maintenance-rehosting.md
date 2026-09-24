# 维护、备份恢复与 rehosting（三通道、otbr、TC2149 矩阵）

## R — 原文依据

> ""otconsole.sh" Available since R2.2 ... Tool (menu) providing access to the main useful commands: 2 sub-menus Easy administration menu Advanced Administration menu"（p519）
> "Automatic backup done every day at 00:01 Full backup on Sunday Incremental backup on other days Saved in "/var/backup/daily" folder and named "fqdn.yyyy-mm-dd-hh-mm.zip""（p541）
> "Performing the re-hosting process with the wrong configuration (hostnames not declared, IP address already used etc...) will result in a deadlock situation. ... it is not possible to fall back to the previous configuration."（p565）
> "the content of the inactive partition will be suppressed and deleted Rollback or update to the inactive partition will NOT be allowed."（p566）
> "Re-hosting an OTMS will NOT update the OmniPCX Enterprise, the OmniVista 8770 server or the OMS"（p567）

出处：OPENXTE300EN p514-578，附录 p579-602（TC2149 ed.04 全文）。

## I — 自述

运维闭环三块：维护三通道、备份体系、rehosting。

维护三通道（同源不同入口）：

| 通道 | 入口 | 适用 |
|---|---|---|
| 原始命令 | checkdns、dla.sh、listtool.sh、ot-config.sh 等 | 脚本化与精确控制 |
| otconsole.sh 菜单 | Easy/Advanced 两级子菜单 | 交互式排查（R2.2 起） |
| Maintenance Portal | WebAdmin 进入或 4448 端口直达 | 图形化执行与日志下载 |

备份体系四要点：

- OT 数据库备份覆盖 ICAS（库+语音消息）、SIP SRV、ACS 三组件；自动备份每日 00:01，周日全量、其余增量
- 产物落在 /var/backup/daily 并按"主机名.日期时间.zip"命名；手动用 otbr.sh backup 或 restore（host/moh 两种口径）
- 介质用 ot-config.sh --storage 选本地/USB/NFS：USB 须 FAT32/NTFS/EXT3 并用 prepareUsbdisk 格式化
- OT-V 本地没有 /var/backup，必须整体挂 NFS、USB 无意义；本地既无该目录又没挂 NFS 时，8770 发起的 OT 备份不工作

rehosting：ot-config.sh --rehost 复用初始化向导，改 OT 的 IP、主机名、FQDN、DNS 与 License server（隐藏选项 --suspend 支持先挂起再搬迁换子网）；实验口径约 25 分钟完成。三条铁律：

1. 参数配错即死锁且无回退——动手前必须参数全对、基础设施一致、有可用备份（OT 备份加整盘镜像或虚机快照）。
2. inactive 分区内容被清除——旧分区回滚与升级通道关闭，后续仅可平滑升级或全新安装。
3. --rehost 只改 OT 自己——OXE/8770/OMS 与生态（DNS/DHCP/SSO/SNMP/防火墙）要按 TC2149 矩阵逐项收尾，漏一项就是"半个系统在新地址"。

## A1 — 书中案例

**维护工具实验**（p522-532）：

1. listtool.sh 按五类列出全部维护脚本。
2. DNS 核查三通道任选其一执行，结果应全 OK。
3. 日志收集：dla.sh 选 feature 与场景，产物落 /logs/dla。
4. otconsole 1-5-1 与 Portal 日志激活均须 root 执行。
5. tsa_maintenance 连本机 3595 端口做号码库核查。
6. 菜单 100 起受口令保护（口令 2998，经 106 2998 进入）。

**备份与 rehosting 实验**（p551-578）：

1. ot-config.sh --storage 查现状并配置备份介质。
2. 实验选 NFS：服务器 10.20.30.40、路径 /mnt/db/backup/podX。
3. root 执行 otbr.sh backup host 做手动备份。
4. 演练 otbr.sh restore host（恢复需先停服务）。
5. rehosting 前置：新 FQDN 与 IP 的 DNS 已生效且确认有可用备份。
6. root 执行 ot-config.sh --rehost，向导内改主机名与 IP。
7. 等约 25 分钟完成后以新地址可达并跑检查。
8. 按 TC2149 矩阵收尾 OXE、8770、OMS 与生态逐项复测。

## A2 — 未来触发

使用情境：客户搬迁要改 IP 与主机名；系统异常要收集日志；备份策略评审；rehosting 后一半系统还在旧地址；换内外 FlexLM 形态。

语言信号：维护 / maintenance / otconsole / Maintenance Portal / 4448 / checkdns / dla / 日志收集 / 备份 / otbr / NFS / rehosting / 改 IP / 主机名 / TC2149 / 死锁 / inactive 分区。

与相邻能力区分：许可锚定物联动（换 FlexLM 形态）→ 许可能力；证书重签与重启 → 证书路由卡；OXE 与 8770 各自的日常备份命令细节在本卡 B 段给指针，深入排障转 TC2149。

## E — 可执行步骤

输入契约：变更窗口与回退预案；新网络参数与 DNS 生效确认；备份可用性证明（OT 备份加镜像或快照）；TC2149 当前版本。

1. 日常：三通道取一做核查与日志收集。完成标准：问题数据在手
2. 备份：按形态（物理/OT-V）定介质并演练一次恢复。完成标准：恢复演练通过
3. rehosting 评估：列全 TC2149 触达面与业务影响（含会议重建）。完成标准：影响清单经客户确认
4. rehosting 执行：前置全绿后跑 --rehost 并等待完成。完成标准：新地址可达且系统检查通过
5. 收尾：按 TC2149 逐项改 OXE/8770/OMS 与生态并复测。完成标准：端到端呼叫与告警正常

判停点：

- 参数没全对齐或没有备份 → 停！rehosting 配错即死锁且无回退
- rehost 后 OXE/8770 还在旧地址 → 设计如此（--rehost 只改 OT），按矩阵收尾
- 换内外 FlexLM 形态 → 外部虚拟化只认加密狗，许可适配走 eBP 工单（预留商务周期）
- OT-V 想用 USB 备份 → 无意义，必须 NFS
- 客户想回滚 inactive 分区 → 通道已关闭，提前告知仅可平滑升级或全新安装

输出契约：维护核查记录 + 备份恢复演练证据 + rehosting 变更单（TC2149 核对表逐项勾选）。

## B — 边界

- 实验口径（生产必须按现场替换）：rehost 目标 192.168.1.49 与主机名 otms、NFS 10.20.30.40、ots 隐藏菜单口令 2998、耗时约 25 分钟。
- 改 OT 或 ACS 集群名称会废掉全部既有会议——变更窗口必须通知全部会议组织者（n22）。
- 物理机整盘镜像用 Clonezilla（细节 TC1625）；虚拟化用 vSphere 快照/克隆/备份（p564）。
- dla.sh 选项 1 须 root；菜单 100 起受口令保护（口令 2998）（p480/p531）。
- OXE 备份用 swinst（配置与计费两类文件）；8770 用自带 Maintenance 工具（p547-549）。
- OTBE 的 rehosting 在 OTBE 安装手册（书外，n39）；UM、Nomadic 同为书外专项。
