# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| cap.ents.first-login-hardening | OXE 首登加固（四账户与密码治理） | critical | 登录 OXE；修改系统账户密码；配置密码策略与账户锁定；启用 client 账户；OXE SSH login | mtcl、swinst、root、client、V24、SSHv2、密码策略、锁定、老化、RADIUS、900 秒 | capabilities/ents-first-login-hardening.md |
| cap.ents.system-start-stop | OXE 系统启停与 autostart 管理 | medium | 启动或停止话务应用；重启或停机；管理 autostart；查系统运行状态 | swinst、Easy menu、RUNTEL、autostart、shutdown、role、停话务、重启、Absent 提示符 | capabilities/ents-system-start-stop.md |
| cap.ents.cs-network-firewall | Call Server IP 寻址与内部防火墙 | critical | 配置 Call Server IP 地址；配置 Role 地址；配置内部防火墙与可信主机；OXE 连不上排查；netadmin firewall | netadmin、Role 地址、物理地址、iptables、可信主机、trusted host、SSH for all、oxedomain、CSV 导入、重启生效 | capabilities/ents-cs-network-firewall.md |
| cap.ents.time-sync | OXE 时间同步（NTP/chrony） | medium | 部署 NTP 时间同步；瞬时校时；配置时区；chrony 巡检 | NTP、chrony、chronyd、瞬时同步、渐进同步、时区、UDP 123、iburst、stratum | capabilities/ents-time-sync.md |
| cap.ents.db-license | 空数据库创建与 OPS 许可管理 | critical | 创建空数据库；恢复或备份 OPS 许可；对接 FlexLM；处理降级模式告警；spadmin 巡检 | MAO、OPS、swk、许可、license、spadmin、PANIC、降级模式、FlexLM、CPU-ID、CC-SUITE-ID、空库 | capabilities/ents-db-license.md |
| cap.ents.media-gateway-deployment | 媒体网关上架（GD4/OMS/XL） | critical | 上架 GD4 硬件网关；部署 OMS 虚拟媒体网关；上架 XL 机架；配置压缩器与子板；板卡不入服排查 | GD4、OMS、XL、GDXL、FXS32、shelf、mgconfig、omsconfig、crystal number、MAC、rstcpl、压缩器、ARMADA | capabilities/ents-media-gateway-deployment.md |
| cap.ents.user-terminal-provisioning | 用户与终端开通（IP 话机/IPDSP/TDM/Profile/DHCP） | critical | 创建用户与开通话机；IP 话机静态或动态开通；部署 IPDSP 软话机；User Profile 批量建户；配置 CS 内部 DHCP；话机换机与日志收集 | 建户、commissioning、MAC、IPDSP、ALE-300、TDM、ANALOG、User Profile、DHCP、dhcpd、termstat、0000、getlogs | capabilities/ents-user-terminal-provisioning.md |
| cap.ents.numbering-cos | 编号计划与 COS 管理 | high | 规划或维护编号计划；创建前缀与后缀；管理 Phone Features COS；配置 Connection/Transfer 矩阵 | 编号计划、prefix、suffix、Timer 23、COS、呼转前缀、摘机路由、Connection COS、Transfer COS、矩阵、缩位拨号 | capabilities/ents-numbering-cos.md |
| cap.ents.call-processing | 呼叫处理业务域（语音指南/话务台/Entity/计时器） | high | 部署静态语音指南与 MOH；部署话务台与 4059EE；管理 Entity 与 CDT；调优呼叫分配计时器 | 语音指南、voice guide、MOH、音乐保持、话务台、attendant、4059、BLF、Entity、CDT、夜转、溢出、Timer 76 | capabilities/ents-call-processing.md |
| cap.ents.voicemail-4645 | OmniMessage 4645 语音邮件与邮件通知 | medium | 部署 4645 语音邮件；分配与管理信箱；配置邮件通知；声明 SMTP 服务器 | 4645、OmniMessage、语音邮件、信箱、voicemail、VPIM、IMAP、邮件通知、SMTP、Eva_tool | capabilities/ents-voicemail-4645.md |
| cap.ents.sip-trunk | 公共 SIP 中继开通与弹性 | critical | 开通公共 SIP 中继；配置 ARS 与鉴别符；配置 NPD 与 DID 翻译器；配置回叫翻译器；SIP 网关备份与负载均衡 | SIP 中继、trunk group、外部网关、SIP Ext Gateway、ARS、鉴别符、discriminator、NPD、DID、回叫、Pool Number、Supervision timer、G722 | capabilities/ents-sip-trunk.md |
| cap.ents.barring-emergency | 外呼闭锁与紧急呼叫通知 | medium | 配置外呼闭锁；管理 Area 与 Public COS；配置紧急呼叫通知；配置 Location ID 与 P-ANI | 闭锁、barring、Public COS、Area、鉴别符、实体状态、Night、紧急呼叫、emergency、P-ANI、Location ID、Tone 34 | capabilities/ents-barring-emergency.md |
| cap.ents.backup-maintenance | 数据库备份恢复与维护排障工具箱 | medium | 备份数据库；恢复数据库；抓包与日志排障；事件查询与释义；生成支持材料 | 备份、backup、恢复、restore、IMMED、oxetrace、tcpdump、infocollect、incvisu、incinfo、syslog、securitystatustool | capabilities/ents-backup-maintenance.md |
| cap.ents.legacy-trunks-umc | 传统中继（T0/T2）与 UMC 云管理 | low | 开通 T0 中继组；开通 T2 中继组；评估或使用 UMC 云管理；UMC 向导建 SIP 中继 | T0、T2、ISDN、BRA、PRA、中继组、同步优先级、NOS、UMC、Easy users、Easy SIP trunk、Fleet Dashboard | capabilities/ents-legacy-trunks-umc.md |
