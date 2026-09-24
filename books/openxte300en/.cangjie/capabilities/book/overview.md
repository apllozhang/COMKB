# Book Overview（参考区）— OpenTouch Suite for MLE / Starter

> 供能力卡引用的背景参考；源自 references.md 落位。实验环境的 IP、账号、口令集中在本文件与各卡 Boundary，正文不携带。

## 交付主线（全书组织轴）

方案概览与实验环境 → 软件安装（SOT 三选一）→ Post-installation wizard 初始化 → 许可安装与核查（FlexLM）→ 双向声明与 SIP 打通（8770 + OXE）→ prior management 号码路由 → 档案与用户供给 → 语音邮箱与通知 → 证书与客户端交付 → 维护、备份与 rehosting（p3-602；主步骤链 p50-51）。附录为 TC2149 ed.04 rehosting 技术通报全文。

## 实验环境（RLAB，仅 Boundary 背景）

- POD 网段 192.168.1.x；公共资源区 10.20.30.x（NAS、SIP 模拟器、外部 DNS 10.20.30.254/250、备份 NFS 10.20.30.40 的 /mnt/db/backup/podX）（p12-16）。
- 实例参数（p16 总表；表印 192.16.8.1.x 为原文排版笔误，应读 192.168.1.x）：

| 实例 | 主机名 | IP（实验口径） |
|---|---|---|
| OXE（csa 物理 / csm 主） | oxe | 192.168.1.1 / 192.168.1.3 |
| OMS | — | 192.168.1.13 |
| OpenTouch | opentouch | 192.168.1.50 |
| OmniVista 8770 | nms | 192.168.1.70 |
| FlexLM 虚机 | flex | 192.168.1.80 |
| SOT | sot | 192.168.1.230 |
| ECOSYSTEM（CA/邮件/中继） | eco | 192.168.1.100 |
| PC Client 10/11 | — | 192.168.1.10 / 192.168.1.11 |
| 混合教室 GD4 | — | 192.168.1.12 |

- DNS/NTP 指向 192.168.1.254（实验口径）。
- 账号口令（全部为公开教学值，生产必须替换）：

| 系统 | 账号 / 口令（实验口径） |
|---|---|
| SOT | admin/letacla（首登强改）；本地上传 upload/sot |
| OT | root=superuser（SOT 预置 letacla1）；otuser=maintenanceuser；otAdmin 口令 Admin-8770；otProfile 口令 Admin-T1；SNMP=adminsnmp |
| 8770 | adminnmc/Superuser01*；Windows administrator/superuser |
| OXE | mtcl/mtcl；swinst/SoftInst；adfexc/adfexc |
| FlexLM 虚机 | root/letacla（首登强改） |
| ESXi | root/letacla（课堂改 superuser） |

- 号码口径（实验）：号段 31000-31499；DDI 首外线 33210N41000、首内线 31000、跨度 500（N=两位 POD 号）；语音邮件 31200；会议 31250（英）/31260（法）；ITSP1 外呼例 0110312345 送出 +33110312345；全国 33{1-5}1PN12345、紧急 112/15/17/18（p26-30, p37, p215-247）。

## 平台速览（方案沟通素材）

- OTMS 与 OTMS-v 均上限 5000 用户；物理服务器由 BP 或客户提供，兼容性用 OTCP 工具核对（p5, p9）。
- 虚拟化矩阵：VMware ESXi 6.5 与 7.0.x、Microsoft Hyper-V 2016 与 2019；OS 为 SLES 12 SP5；OTMS-v 六虚机（8770/OXE/OMS/DCS/OTMS/OTFC）（p8-9）。
- OTMS-v 虚机布局：8770 VM 与 DCS VM 为 Windows、OXE VM 呼叫处理、OTMS VM 承载 ICM/ICAS/AMS、OTFC 传真（p8）。
- 许可：FlexLM 端口 27000；物理机锚 ALUID、虚拟机锚加密狗；OXE 容量在本地 .swk（p130-132）。
- 集成端口：OXE PRS 2570、ESS 5260、Mule 5040、SNMP 161/162、Maintenance Portal 4448、DM 8080（p199-232, p205-209, p521, p489）。
- 容量类硬数字：内嵌 IMAP 1000 并发封顶（1001-20000 需专用服务器）；公告 5 分钟封顶；多终端 5 设备（REX/DECT 各 1）；监督 500 组、40 人/组、监督链 4000（500-1500 用户）或 6000（3000-5000 用户）；自动备份每日 00:01 周日全量（p313, p392, p439, p507, p541）。

## 教材口径声明

- 全部实验密码/账号/网段是公开教学值，生产必须替换并做安全加固；工具示例输出中的 151.1.1.x/172.25.x 为文档历史演示值（nr-03）。
- 生产化边界四文档：Delivery note / Features list / Product limits（容量与规格）、TC1652（spatial redundancy）、TC2257/TC2639（SBC/RP）、TC2149（rehosting 全矩阵，附录已收录）。
- 版本敏感点：HA 新装机禁用（仅 R2.2.x 迁移保留，p94）；SHA-1 自 R2.2 弃用（p426）；话务台前缀自 OT R2.1 必配（p238）；License_release 10=R2.4、11=R2.5（p154）；otconsole 与 SHA-2 自 R2.2（p519）；vSphere client 仅 ESXi ≤6.0（p84）。
- 书内不一致两处：公告 wav 目录（p392 与 p396，nr-01）；IP 总表排版笔误（p16，nr-02）。
- R-Lab 特例：SOT/OTMS 模板已预部署、许可锚 MAC 不锚加密狗——现场不可照搬（n10，nr-04）。
