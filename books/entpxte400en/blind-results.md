# entpxte400en 盲判结果（仅依据能力目录，锁定后不改）

case-id | slug或none | 理由一句
should-login-01 | ents-first-login-hardening | 首次登录通道与 root 仅本地直登属四账户首登能力
should-login-02 | ents-first-login-hardening | 14 位密码、错 3 次锁定、老化期全部是密码九规则与锁定策略
should-start-01 | ents-system-start-stop | 重启后话务没自动起来即 autostart 被取消的典型现象
should-start-02 | ents-system-start-stop | 停话务仅 Easy 7 且连带取消 autostart 的顺序属启停能力
should-netfw-01 | ents-cs-network-firewall | ping 不通先查 Role 地址仅话务运行时生效与防火墙白名单
should-netfw-02 | ents-cs-network-firewall | 物理地址与 Role 地址迁移加 Apply 重启属 CS 寻址能力
should-time-01 | ents-time-sync | 对接内网 NTP 保持同步即 chrony client/server
should-time-02 | ents-time-sync | 钟快几小时要瞬时校准必须先停 chronyd
should-dblic-01 | ents-db-license | 按国家初始化全新库且连 OPS 一起抹属空库创建顺序与风险
should-dblic-02 | ents-db-license | 话务台告警加 Please call your administrator 是许可降级三阶段表现
should-mg-01 | ents-media-gateway-deployment | GD4 上电入网要 OPS 建架、WBM 声明与 mgconfig
should-mg-02 | ents-media-gateway-deployment | OMS/XL 上架与 DHCP 地址须登记 MAC 属网关部署
should-user-01 | ents-user-terminal-provisioning | ALE-300 开分机即 IP 话机绑 MAC 开通
should-user-02 | ents-user-terminal-provisioning | IPDSP 绑 Phone Identifier 与 CS 内部 DHCP 默认关属终端开通
should-numcos-01 | ents-numbering-cos | 拨 31 等 3 秒即 Timer 23 消解前缀歧义
should-numcos-02 | ents-numbering-cos | 转接限制与呼转放开走 Connection/Transfer 矩阵与 Phone Features COS
should-callproc-01 | ents-call-processing | 保持音乐换企业音乐即 MOH 激活删 Tone 2 建 VG 2
should-callproc-02 | ents-call-processing | 话务台属组与下班溢出转值班即话务台与 CDT 路由
should-vm-01 | ents-voicemail-4645 | 全员语音信箱加邮件提醒即 4645 通知三档
should-vm-02 | ents-voicemail-4645 | 留言通知邮件排查走 SMTP 声明与防火墙加白
should-sip-01 | ents-sip-trunk | 运营商 SIP 参数打通外线走去话九步流水线
should-sip-02 | ents-sip-trunk | 主叫号码不对与 484 属 NPD/DID 与鉴别符排障
should-bar-01 | ents-barring-emergency | 市话与国际限制即 Area 乘 Public COS 外呼闭锁
should-bar-02 | ents-barring-emergency | 紧急呼叫时保安室提醒即紧急呼叫通知与 Location ID
should-bk-01 | ents-backup-maintenance | 升级前备份与恢复流程属备份恢复能力
should-bk-02 | ents-backup-maintenance | trace 与日志包采集即 oxetrace 等八件套
should-legacy-01 | ents-legacy-trunks-umc | ETSI T2 建中继组与无信号排查属传统中继
should-legacy-02 | ents-legacy-trunks-umc | 云平台批量开通前提即 UMC 三功能前提条件
bait-bar-01 | ents-numbering-cos | 免打扰与遇忙回叫是话机功能开关属 Phone Features COS，非外呼闭锁
bait-cos-01 | ents-barring-emergency | 只许本地禁国际是外呼闭锁的 Area 与 Public COS 组合，不是用户功能类
bait-vm-01 | ents-call-processing | 等待听音乐不要嘟嘟声是 MOH，与语音邮件系统无关
bait-mg-01 | ents-media-gateway-deployment | 换板触发 rstcpl 打在 GD 上等于整架重启，话机离线正是该风险
bait-sip-01 | ents-legacy-trunks-umc | T2 信令变体与去位数调整属传统中继，与 SIP 无关
bait-restore-01 | ents-backup-maintenance | SFTP 恢复连不上要先核 CS 物理地址与 Binary 传输
bait-umc-01 | ents-legacy-trunks-umc | UMC 明确排除多实体与话务台，需求本身越界属 UMC 范围判断
bait-ha-01 | none | 双机容灾与集中话务台组网规划不在能力目录任何一项内
edge-aging-01 | ents-first-login-hardening | 老化 10-366 开区间边界值判断归密码治理
edge-emergency-01 | ents-barring-emergency | 多节点带 PCS 能否用紧急通知归紧急呼叫边界条件
edge-disc-01 | ents-barring-emergency | 逻辑鉴别符与真实鉴别符映射属闭锁鉴别符体系
edge-version-01 | ents-cs-network-firewall | N2 与 N3 防火墙默认行为差异属防火墙能力
