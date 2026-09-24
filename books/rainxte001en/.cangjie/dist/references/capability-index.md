# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| cap.rbx.company-subscription | Rainbow 公司体系与订阅开通 | critical | 创建 Rainbow 公司；开通 Rainbow 订阅；选择公司可见性；配置 SSO/TOTP 认证；create Rainbow company；Rainbow subscription plans | Company、BP、EC、可见性、CLOSED、ISOLATED、SSO、TOTP、Essential、Business、Enterprise、Attendant、预付 | capabilities/rbx-company-subscription.md |
| cap.rbx.omc-onboarding | OMC 安装首次连接与 IP 规划修改 | high | 安装 OMC；OMC 连不上 OXO；修改 OXO IP 规划；install OMC first connection | OMC、pbxk1064、Expert mode、Server authentication、证书、Trusted Root、Lan/IP configuration、DHCP 池、重启 | capabilities/rbx-omc-onboarding.md |
| cap.rbx.pbx-onboarding | OXO 接入 Rainbow 与接入排障 | critical | OXO 接入 Rainbow；PBXID 在哪找；Rainbow 连接状态异常；connect OXO to Rainbow | PBXID、Activation code、激活码、openrainbow.com、Webdiag、Rainbow Status、connected with final password、ccrbagent.log | capabilities/rbx-pbx-onboarding.md |
| cap.rbx.member-lifecycle | Rainbow 成员全生命周期管理 | critical | 批量创建 Rainbow 用户；删除恢复用户；成员设置；Rainbow user management | members、邀请、invitation、CSV、Azure AD、批量导入、grace period、宽限期、改密踢下线、密码策略 | capabilities/rbx-member-lifecycle.md |
| cap.rbx.gateway-planning | WebRTC 网关拓扑决策与容量规划 | critical | 选择 WebRTC 网关拓扑；网关容量规划；网关通道数；WebRTC gateway dimensioning | 拓扑、集成网关、OCE Front End、NUC、ESXi、容量、channels、20 通话、50 通话、150 用户、UTL、Twinset、Anydevice | capabilities/rbx-gateway-planning.md |
| cap.rbx.gateway-deployment | WebRTC 网关部署与虚拟终端配置 | critical | 部署 WebRTC 网关；自动配置网关；配置 Twinset/Anydevice 终端；deploy WebRTC gateway | Activate WebRTC Gateway、自动配置、Reseller 管理员、FTR、Frontend WebRTC、warm reset、FleetRef-Installref、端口 5059、Subscribers list、secondary set、UTL Bypass | capabilities/rbx-gateway-deployment.md |
| cap.rbx.attendant-supervision | Rainbow 话务台与监督组 | high | 部署 Rainbow 话务台；建监督组；互助值班方案；attendant console setup | attendant console、话务台、监督组、supervision group、互助组、mutual aid、代接、pickup、BLF、队列 8 路 | capabilities/rbx-attendant-supervision.md |
| cap.rbx.teams-integration | Microsoft Teams 集成全流程 | high | Rainbow 集成 Teams；Teams 应用上架与权限同意；Teams 在场同步；Rainbow for Teams integration | Teams、Rainbow App、Rainbow Desktop、consent、权限同意、Telephony 权限、click-to-call、F6、presence、在场同步、Office 365 | capabilities/rbx-teams-integration.md |
| cap.rbx.admin-tools | Rainbow 管理员工具（权责/企业目录/信息频道） | medium | 分配管理员权限；企业目录导入；信息频道创建 | roles、管理员、business directory、企业目录、information channel、信息频道、委托 | capabilities/rbx-admin-tools.md |
| cap.rbx.rcc-association | OXO 分机关联与 RCC 模式 | medium | 关联 OXO 分机到 Rainbow；RCC 模式验证；Rainbow number | RCC、Remote Call Control、associate extension、Telephony 页签、Rainbow number、Office phone | capabilities/rbx-rcc-association.md |
| cap.rbx.maintenance-support | Rainbow 维护与支持体系 | medium | 查 Rainbow 日志；开 Rainbow 服务请求；云状态与维护预告 | logs、report a problem、status.openrainbow.com、告警、操作历史、Service Request、SR、ESR、MyPortal | capabilities/rbx-maintenance-support.md |
| cap.rbx.network-readiness | Rainbow 网络就绪核查 | medium | Rainbow 网络要求；连通性评估；端口放行 | network requirements、端口、带宽、防火墙、Rainbow Pilot、连通性、勘测 | capabilities/rbx-network-readiness.md |
