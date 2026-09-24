# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| cap.oxoa.sip-networking | SIP 组网：公网网关与私网互联 | critical | 配置公网 SIP 网关；SIP 注册失败排查；两台 OXO 私网互联；私网饱和溢出公网；configure SIP gateway；SIP trunk registration | SIP 网关、ITSP、Domain Proxy、Outbound Proxy、注册、5059、中继组、溢出、overflow、私网、站点互联、RTP Direct | capabilities/oxoa-sip-networking.md |
| cap.oxoa.numbering-ars-suite | ARS 路由套件：三表协作与 Internal ARS | critical | 规划 ARS 选路；多运营商分流与溢出；一个 DDI 分时段路由；非营业时间播欢迎消息；ARS routing configuration | ARS、选路、中继组列表、前缀、替换、substitute、溢出、Internal ARS、Day Groups、Hours、虚拟 Provider、Local、传真 | capabilities/oxoa-numbering-ars-suite.md |
| cap.oxoa.hotel-billing-vertical | 酒店与计费垂直方案 | high | 部署酒店模式；客房计费与预付切断；生成 XML 计费小票；账号码与内部替代；hotel solution setup | 酒店、hotel、PMS、OHL、check-in、房态、预付、metering、TicketCollector、账号码、account code、内部替代、66 | capabilities/oxoa-hotel-billing-vertical.md |
| cap.oxoa.security-hardening | 系统安全加固 | critical | 执行安全基线核查；密码策略与弱密码审计；收敛管理面与话务面；远程访问锁定处理；system security hardening | 安全、密码、AutoPwdChk、弱密码、Network IP Services、ETH1、锁定、VMUMaxTry、1440、加固、TC1143、紧急号码、LDAPS | capabilities/oxoa-security-hardening.md |
| cap.oxoa.certificate-suite | 证书与加密传输（证书/DTLS/TLS-SRTP） | critical | 管理数字证书与 PKI 签发；部署 DTLS 话机信令加密；配置 SIP 中继 TLS/SRTP；4K 证书升级与回滚；certificate and TLS SRTP setup | 证书、certificate、PKI、CSR、4096、2048、回滚、DTLS、TrustList、TLS、SRTP、5061、OCE-FE | capabilities/oxoa-certificate-suite.md |
| cap.oxoa.attendant-suite | 语音导航套件（AA/MLAA/SCR） | high | 配置自动话务员；多语言多树导航；按客户码分流来话；语音导航排障；auto attendant MLAA SCR | AA、自动话务员、MLAA、语音导航、语音指南、SCR、客户码、client code、DID 路由、CLI 路由、press star、免费拨号、12000 | capabilities/oxoa-attendant-suite.md |
| cap.oxoa.voicemail-mobility | 语音邮箱与移动办公 | high | 配置语音邮箱远程接入；处理邮箱锁定与解锁；激活游牧模式；配置远程替代回环；voicemail nomadic remote substitution | 语音邮箱、voice mail、远程接入、ACC、锁定、VMUMaxTry、个人助理、游牧、nomadic、远程替代、remote substitution、远程接入码、# 前缀 | capabilities/oxoa-voicemail-mobility.md |
| cap.oxoa.cloud-connect-fleet | Cloud Connect 舰队与远程维护 | high | 注册系统到 Cloud Connect；舰队软件更新；选型远程维护通道；同步 Rainbow 业务目录；cloud connect fleet management | Cloud Connect、Fleet Dashboard、OXO Connectivity、Inventory、软件更新、advanced、远程维护、50443、端口转发、管理 VPN、Rainbow 目录、Business Directory | capabilities/oxoa-cloud-connect-fleet.md |
| cap.oxoa.foundation-ip | 交付地基：OMC 首连与 IP 规划 | medium | OMC 首次连接；修改 OXO IP 规划；IPDSP 安装报错处理 | OMC、首连、pbxk1064、证书、Trusted Root、IP 规划、DHCP 池、重启、IPDSP、NTP | capabilities/oxoa-foundation-ip.md |
| cap.oxoa.terminal-ecosystem | 终端生态：PIMphony 与 SIP 话机接入 | medium | 接入 SIP 话机或软话机；选择媒体处理路径；部署 PIMphony；SIP 话机排障 | SIP 话机、Open SIP、Zoiper、软话机、5059、编解码、透传、RTP proxy、Direct RTP、PIMphony、profile、8088 | capabilities/oxoa-terminal-ecosystem.md |
| cap.oxoa.shared-devices | 共享终端：站群监督、Hot Desking 与 Multiset | medium | 配置站群监督；部署 Hot Desking；配置 Multiset/Twinset | 监督、supervision、Groupware、代接、Hot Desking、HDU、HDP、683、Multiset、Twinset、副站、MLTSETRING | capabilities/oxoa-shared-devices.md |
| cap.oxoa.multi-entity | 多实体与伪多公司 | medium | 多实体隔离配置；两家公司共享系统分账 | 多实体、entity、多租户、伪多公司、MoH、流量分担、链路类别、矩阵、Char、分账 | capabilities/oxoa-multi-entity.md |
| cap.oxoa.dect-deployment | DECT 无线移动 | medium | 选型与部署 DECT；注册 DECT 话机；勘测验收覆盖；SUOTA 批量升级 | DECT、IP-DECT、xBS、IBS、PARI、IPUI、集群、切换、handover、勘测、-72 dBm、SUOTA、8378 | capabilities/oxoa-dect-deployment.md |
| cap.oxoa.maintenance-toolkit | 维护工具箱：Webdiag、Noteworthy 与 LoLa | medium | Webdiag 排障与信息收集；noteworthy 地址修改；LoLa 系统加载与迁移；退役设备净化 | Webdiag、installer、Dump、抓包、noteworthy、TC1398、Memory Read、Auto_Reset、铃音、LoLa、迁移、cold reset、warm reset | capabilities/oxoa-maintenance-toolkit.md |
