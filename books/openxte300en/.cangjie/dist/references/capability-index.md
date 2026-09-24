# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| cap.ots.post-installation-wizard | OTMS 初始化向导（两模式十节） | critical | 完成 OTMS 初始化向导；从备份恢复重装 OTMS；向导口令与 DNS 有什么要求；post-installation wizard | post-installation、wizard、站点安装、from scratch、restore、archive、HA、DNS 正反向、otAdmin、otProfile、otuser、security off | capabilities/ots-post-installation-wizard.md |
| cap.ots.license-flexlm | 许可体系与 FlexLM（安装、核查、外部切换） | critical | 安装许可文件；许可核查与排障；部署外部 FlexLM；内部切外部 FlexLM | FlexLM、.ice、.swk、sw8770、nmc.license、ALUID、加密狗、dongle、spadmin、lmutil、checkLicensing、final_licenses、PANIC、27000 | capabilities/ots-license-flexlm.md |
| cap.ots.node-declaration-sip | 双向节点声明与 SIP 打通（含告警对接） | critical | 在 8770 声明 OXE；在 8770 声明 OpenTouch；配置 OXE SIP 打通；OT 告警对接 8770 | bics.conf、节点声明、declaration、Topology、PRS、2570、trunk group、外部网关、5260、5040、trusted、G729、SNMP、Inform、MIB、synchronization | capabilities/ots-node-declaration-sip.md |
| cap.ots.prior-management | Prior management（号码段、前缀、拨号规则、UDAS、会议桥） | critical | 配置号码段与归属；配置前缀与拨号规则；修复目录检索陈旧；配置会议桥与 DAS 规则 | 号码段、Ranges、前缀、prefix、拨号规则、dialing rule、UDAS、同步周期、31000-31499、31200、31250、DAS rules、会议桥、wireald | capabilities/ots-prior-management.md |
| cap.ots.users-profiles | 档案与用户供给（三类用户、WPC 批量） | critical | 创建 Connection 用户；创建 OXE/OT 档案；批量供给用户（WPC）；用户口令策略 | 档案、profile、ACU-OXE、Connection 用户、ACU、Set function、占号、Directory user、WPC、Web Provisioning、Chrome、TUI 口令、MACD | capabilities/ots-users-profiles.md |
| cap.ots.voice-mail | 语音邮箱、IMAP 收取与通知公告（Local Storage） | critical | 创建语音邮箱；配置语音邮箱档案；配置 IMAP 收取语音留言；配置 SMTP/SMS 通知与公告 | 语音邮箱、voice mail、defaultVmsLS、Local Storage、IMAP、Outlook、imap4fed、SMTP、SMS、notification、公告、announcement、greeting、配额 | capabilities/ots-voice-mail.md |
| cap.ots.clients-multi-devices | OTC PC 客户端交付与多终端 | high | 安装交付 OTC PC；排查 OTC PC One 免费模式；配置电脑软电话；配置多终端副站 | OTC PC、OTC PC One、Desktop 许可、freemium、RCC、VoIP、软电话、softphone、SIP 分机、Multi-devices、多终端、副站、Twinset、Outlook 加载项 | capabilities/ots-clients-multi-devices.md |
| cap.ots.maintenance-rehosting | 维护、备份恢复与 rehosting（TC2149 矩阵） | critical | 收集日志与系统核查；配置备份与恢复；执行 rehosting 改 IP 主机名；rehosting 后收尾三件套 | maintenance、otconsole、Maintenance Portal、4448、checkdns、dla、backup、otbr、NFS、00:01、rehosting、TC2149、死锁、inactive 分区 | capabilities/ots-maintenance-rehosting.md |
| cap.ots.sot-installation | SOT 自动化装机与虚机手动导入 | medium | 用 SOT 部署 OTMS；SOT 媒体与项目管理；手动安装 OTMS；OVF/OVA 导入 ESXi | SOT、Software Orchestration Tool、静默安装、PXE、media、project、OVF、OVA、ESXi、bootdvd、hotfix、BPWS | capabilities/ots-sot-installation.md |
| cap.ots.certificates | 证书部署三路线 | medium | 切换自签证书；用 Windows CA 签发证书；评估 security off 风险；排查证书不生效 | certificate、自签、self-signed、CA、CSR、PKCS7、PKCS12、CTL、SHA256、security off、Deploy、CertSrv | capabilities/ots-certificates.md |
| cap.ots.supervision-groups | 监督组（话务监督、进出组与代接） | medium | 创建监督组；配置进出组前缀；配置监督代接；评估监督覆盖边界 | 监督组、supervision、Supervisor、代接、pickup、Direct call pick-up、Join or leave group、Regular、Collaboration、40 人、500 组 | capabilities/ots-supervision-groups.md |
| cap.ots.lab-connections | 实验 POD 与系统连接通道 | medium | 搭建实验 POD；连接 OT/OXE/8770；SUSE 图形界面操作；验证模拟外呼 | RLAB、POD、ITSP1、外呼、SSH、Telnet、Putty、mstsc、SUSE、startx、YaST | capabilities/ots-lab-connections.md |
