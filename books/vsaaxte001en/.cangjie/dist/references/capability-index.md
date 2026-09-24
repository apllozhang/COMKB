# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| cap.vaa.install-sip-integration | VAA 安装与 OXE SIP 对接接通 | critical | 安装 VAA 服务器；OXE 对接 VAA；拨测试树不通；install.sh parameters；VAA SIP trunk | install.sh、incoming username、G711、G729、ABC-F、trunk group、SIPMOTOR、trkstat、motortrace、自签证书、Release 11、接通 | capabilities/vaa-install-sip-integration.md |
| cap.vaa.multitenant-tree-design | VAA 多租户与树设计（公司/日历/UC1-UC3） | critical | 创建 VAA 公司租户；设计 IVR 树；多语言菜单；business hours routing；VIP 过滤分流 | tree、树、Menu、Transfer、Filter、Calendar、business hours、营业时间、多语言、路由号码、DID、VIP、节点命名 | capabilities/vaa-multitenant-tree-design.md |
| cap.vaa.prompt-tts-asr | VAA 提示音与 TTS/ASR 引擎 | high | 导入提示音；选 TTS 引擎；开语音识别；prompt management；TTS generation | prompt、提示音、WAV、8KHz、PCM、Pico、Google Cloud TTS、ASR、语音识别、录音 | capabilities/vaa-prompt-tts-asr.md |
| cap.vaa.ivr-option-nodes | VAA IVR 选项节点与动态脚本 | high | 配置 IVR 变量与条件；收号采集；HTTP 节点集成；display name node；collect digits | variable、Condition、Collect digit、收号、display name、HTTP、Mail、JSON、correlator、IVR 许可 | capabilities/vaa-ivr-option-nodes.md |
| cap.vaa.master-slave-ha | VAA Master/Slave 高可用与 OXE ARS 切换 | critical | 部署 VAA 双机；主备切换测试；OXE ARS 双路由；vaa ha addslave；高可用行为 | HA、Master、Slave、addslave、resync、vaa ha role、whoismaster、ARS、切换、只读、NPD、识别符 | capabilities/vaa-master-slave-ha.md |
| cap.vaa.maintenance-backup | VAA 日常维护与版本升级 | high | VAA 日常巡检；备份恢复；升级 VAA 版本；vaa commands；密码策略 | vaa status、vaa.conf、backup、restore、92 天、密码过期、SNMP、日志、升级、NFS、自动备份 | capabilities/vaa-maintenance-backup.md |
| cap.vaa.db-integration | VAA 外部数据库集成（JDBC/SQL 节点） | high | VAA 连接外部数据库；SQL 节点查库转接；安装 JDBC 驱动；MS SQL connectivity；Oracle JDBC URL | JDBC、SQL、mssql-jdbc、Oracle、1433、External Databases、ODBC、MS SQL、空结果、单字段 | capabilities/vaa-db-integration.md |
| cap.vaa.statistics-reporting | VAA 统计与报告 | high | 配置话务周报；逐节点排障；导出呼叫日志；VAA statistics；报表口径 | statistics、报表、call logs、CSV、xlsx、周报、逐节点、许可不足 | capabilities/vaa-statistics-reporting.md |
| cap.vaa.webadmin-administration | VAA WebAdmin 管理面 | medium | 添加 VAA 管理员；配置 SMTP 告警；查看 VAA 日志；webadmin setup；受限用户档案 | WebAdmin、管理员、SMTP、Supervision、logs、License、受限档案 | capabilities/vaa-webadmin-administration.md |
| cap.vaa.pcs-opex-licensing | VAA PCS 同步与 OPEX/许可体系 | medium | 配置 PCS 同步；OPEX 模式评估；核查 VAA 许可；Purple On Demand；许可失效排查 | PCS、OPEX、CAPEX、Purple On Demand、FlexLM、FEATURE、AAIVR、AAPORTS、VAA_RELEASE、Backup4PCS | capabilities/vaa-pcs-opex-licensing.md |
| cap.vaa.server-sizing-virtualization | VAA 服务器选型与虚拟化 | medium | 选 VAA 服务器规格；核对虚拟化兼容；端口数上限；VAA hypervisor；sizing | sizing、ESXi、VMXNet3、Hyper-V、Proxmox、端口上限、root SSH、SUSE | capabilities/vaa-server-sizing-virtualization.md |
| cap.vaa.architecture-redundancy | VAA 架构与冗余全景 | medium | 解释 VAA 架构；multi-company 集成；N+1 冗余；VAA call flow；冗余选型 | architecture、呼叫流、CMIP、multi-company、N+1、reference VAA、冗余、空间冗余 | capabilities/vaa-architecture-redundancy.md |
