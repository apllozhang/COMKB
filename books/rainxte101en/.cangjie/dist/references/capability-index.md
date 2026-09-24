# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| cap.hub.company-voice-subscription | Rainbow 公司体系与 Voice 订阅开通 | critical | 创建 Rainbow Hub 公司；开通 Voice 订阅；选择公司可见性；配置 SSO/TOTP 认证；create Rainbow Hub company；Voice subscription plans | Company、BP、EC、Reseller、可见性、CLOSED、ISOLATED、SSO、TOTP、Voice Phone、Voice Business、Voice Enterprise、Voice Attendant、预付、时区 | capabilities/hub-company-voice-subscription.md |
| cap.hub.cloud-pbx-provisioning | Cloud PBX 声明与话务配置 | critical | 声明 Cloud PBX；设计编号计划参数；分配公网号码与主号；配置呼叫闭锁；declare Cloud PBX；public numbers DDI | Cloud PBX、编号计划、numbering plan、出局前缀、DDI、公网号码、主号、闭锁、barring、白名单、blacklist、trunk、bundled、separated | capabilities/hub-cloud-pbx-provisioning.md |
| cap.hub.member-telephony | 成员管理与话务配置 | critical | 批量创建成员；配置成员电话号码；管理个人例行程序；删除恢复成员；Rainbow user management | members、成员、邀请、invitation、CSV、Azure AD、LDAP、批量导入、例行程序、routines、标签、profiles、grace period、宽限期、Essential、改密踢下线 | capabilities/hub-member-telephony.md |
| cap.hub.zero-touch-provisioning | ALE 设备 zero-touch 部署与 DECT 移动 | critical | 部署 Myriad 话机；批量导入设备；部署 DECT 基站与手持机；zero-touch provisioning | zero-touch、零接触、MAC 地址、IPEI、Myriad、8328、8368、8214、8262、DECT、Config Failed、rdd.openrainbow.com、绿点、EM200 | capabilities/hub-zero-touch-provisioning.md |
| cap.hub.device-maintenance | 设备维护日志与 Generic SIP 接入 | high | 采集话机日志；远程排障设备；评估接入第三方 SIP 话机；Generic SIP device onboarding | 设备日志、debug、pcap、tcpdump、webadmin、2.14.22、TOTP、Generic SIP、证书链、TLS、SRTP、G711、互操作 | capabilities/hub-device-maintenance.md |
| cap.hub.hunt-groups | 呼叫组与话务分配 | critical | 创建呼叫组与等待队列；配置经理助理组；配置紧急号码与紧急组；管理通话录音；hunt group waiting queue | hunt group、呼叫组、等待队列、waiting queue、溢出、overflow、Parallel、Serial、Circular、经理助理、紧急组、emergency group、0112、PSAP、录音、Rainbow Exporter | capabilities/hub-hunt-groups.md |
| cap.hub.attendant-supervision | 话务台与监督组 | high | 部署话务台；创建监督组；建 attendant group；attendant console setup | attendant console、话务台、监督组、supervision group、supervisor、代接、pickup、Voice Attendant、attendant group、10 路、预通告 | capabilities/hub-attendant-supervision.md |
| cap.hub.welcome-service-ivr | 欢迎服务与 IVR | critical | 配置欢迎服务与营业时间路由；管理日历与语音提示；配置自动话务员菜单；custom music on hold | 欢迎服务、welcome service、日历、calendar、语音提示、voice prompt、IVR、automated attendant、DTMF、菜单、MoH、music on hold、forced、特殊日 | capabilities/hub-welcome-service-ivr.md |
| cap.hub.network-readiness | Rainbow Hub 网络就绪核查 | medium | 核查网络端口与防火墙；评估站点承载容量；估算话音带宽；Rainbow Pilot assessment | network requirements、网络要求、端口、带宽、防火墙、Rainbow Pilot、连通性、30000-44999、Opus、G711、勘测 | capabilities/hub-network-readiness.md |
| cap.hub.multisite | 多站点配置 | medium | 创建站点并分布用户；配置站点主号；配置站点音乐保持；multi-site configuration | multi-site、多站点、站点、site、站点主号、site phone number、MoH、号码池 | capabilities/hub-multisite.md |
| cap.hub.analytics | 分析体系 | medium | 获取月度话单 CDR；解读分析仪表盘；排查话音质量问题；CDR billing data | CDR、话单、计费、仪表盘、dashboard、采纳率、MOS、质量票、抖动、RTT、丢包、隐私 | capabilities/hub-analytics.md |
| cap.hub.maintenance-support | Hub 维护与支持体系 | medium | 查平台状态与维护预告；收集用户日志与上报；开 Rainbow Hub 服务请求；Rainbow support SR | logs、report a problem、status.openrainbow.com、维护预告、Get updates、Service Request、SR、ESR、MyPortal、Emily BOT、Global Welcome Center、认证 | capabilities/hub-maintenance-support.md |
