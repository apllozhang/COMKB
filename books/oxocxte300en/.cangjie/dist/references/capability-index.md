# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| cap.oxos.data-collection | 交付前数据采集 | critical | 做 OXO 交付前数据采集；定编号计划与 IP 规划；准备安装密码表；data collection checklist | 数据采集、data collection、IP 规划、编号计划、密码表、需求清单、Partner fleet、三参考值、呼入呼出需求 | capabilities/oxos-data-collection.md |
| cap.oxos.commissioning | 系统开通双路线与首次连接 | critical | OCE FTR 注册 Cloud Connect；安装 OMC 并首次连接；修改 OXO IP 规划；冷复位后重建基础配置；FTR first time registration | FTR、Cloud Connect、Standard、OMC、pbxk1064、Server authentication、证书、软件钥匙、.msl、.csl、初始安装向导、Hotel 模式、warm reset | capabilities/oxos-commissioning.md |
| cap.oxos.terminals | 终端开通（IP 话机与 DECT） | high | 开通 IP 话机；话机拿不到地址；部署 IP-DECT 基站；注册 8328/8214 话机；put in service IP phone | Auto-Provision、DHCP 池、TFTP、Dynamic Alcatel、xBS、ARI、GAP、IPUI、8328、8214、*47*、FXS、Open SIP | capabilities/oxos-terminals.md |
| cap.oxos.numbering-groups | 编号计划与四种组 | critical | 配置编号计划；建新前缀段报冲突；建 hunt/代接/广播组；建经理秘书组；numbering plan configuration | 编号计划、numbering、Base、安装号、前缀、缩位拨号、hunt group、Sequential、Parallel、代接、pickup、广播、broadcast、经理秘书、multiline | capabilities/oxos-numbering-groups.md |
| cap.oxos.user-features | 用户功能与语音信箱 | high | 配用户可编程键；配动态路由与前转；前转不生效排障；管理语音信箱；configure dynamic routing | 可编程键、功能键、资源键、RSL、动态路由、3276、apply diversion、前转、插入、热线、语音信箱、mailbox、answer only、screening、远程访问 | capabilities/oxos-user-features.md |
| cap.oxos.sip-trunk | 公共 SIP 中继 | critical | 配置公共 SIP 网关；SIP 注册失败排障；导入运营商 Profile；补短号与紧急号码路由；configure SIP trunk | SIP 网关、SIP Gateway、Outbound Proxy、Registrar、RTP Direct、带宽、SIP registration、Profile、Easy Connect、ARS、紧急号码、安装号、DDI | capabilities/oxos-sip-trunk.md |
| cap.oxos.incoming-barring | 呼入分发与呼出闭锁 | high | 配置呼入日夜分发；配置时段表与预公告；控制用户出局权限；配置国际闭锁；call barring management | 话务台组、attendant group、时段表、time ranges、Normal、Restricted、预公告、闭锁、barring、Link Category、矩阵、0053、DDIonPRI | capabilities/oxos-incoming-barring.md |
| cap.oxos.maintenance | 备份恢复、软件升级与复位 | high | 建立备份制度；恢复数据库；执行软件升级与回退；选择复位方式；backup restore software download | 备份、backup、恢复、restore、SD 卡、EXT2、DBAdapter、软件下载、Swap、switchover、warm reset、cold reset、factory reset、复位 | capabilities/oxos-maintenance.md |
| cap.oxos.hardware-platform | 硬件平台与容量 | medium | 选硬件平台形态；估算话音并发容量；评估机柜扩展条件；OXO hardware family | IPBox、OCE、PowerCPU EE、Armada、DSP 通道、HSL、PowerMEX、ETH1、eMMC、MSDB、300 用户、启动八步 | capabilities/oxos-hardware-platform.md |
| cap.oxos.audio-messages | 消息与彩铃 | medium | 上传欢迎与预公告消息；配置保持音乐；音频格式转换核查；music on hold download | 欢迎消息、MSG、彩铃、Music on hold、MoH、.wav、8kHz、Entity、320 秒 | capabilities/oxos-audio-messages.md |
| cap.oxos.security | 安全基线与防盗打 | high | 制定密码策略；清理默认口令；处置疑似盗打；phreaking security baseline | 密码策略、默认密码、pbxk1064、盗打、phreaking、弱密码、000000、TC1143、安全基线 | capabilities/oxos-security.md |
| cap.oxos.rainbow-integration | Rainbow 混合云接入速览 | medium | 把 OXO 接入 Rainbow；Rainbow 连接排障；网关拓扑与容量速查；connect OXO to Rainbow | Rainbow、PBXID、Activation code、激活码、Webdiag、connected with final password、ccrbagent.log、RCC、WebRTC 网关、Twinset、Anydevice、UTL | capabilities/oxos-rainbow-integration.md |
