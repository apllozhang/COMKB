# openxte300en 盲判结果（仅依据能力目录第一判断，锁定后不改）

| case-id | slug/none | 理由 |
|---|---|---|
| should-wizard-01 | ots-post-installation-wizard | 首次开机初始化向导与口令规则即该能力定义 |
| should-wizard-02 | ots-post-installation-wizard | restore from archive 正是向导的第二种模式 |
| should-license-01 | ots-license-flexlm | 三台机器许可文件三族格式归属即该能力 |
| should-license-02 | ots-license-flexlm | spadmin 三计数健康判据正是该能力内容 |
| should-node-01 | ots-node-declaration-sip | 三机互挂拓扑声明顺序正是该能力主责 |
| should-node-02 | ots-node-declaration-sip | SNMP v3 Inform 告警进 8770 与 MIB 重载在该能力描述内 |
| should-prior-01 | ots-prior-management | 自动加 0 前缀与按名呼打自动加前缀正是 prior management |
| should-prior-02 | ots-prior-management | 目录同步排障先查 UDAS 周期，属该能力 |
| should-users-01 | ots-users-profiles | 档案三件套合成 Connection user 正是该能力 |
| should-users-02 | ots-users-profiles | WPC 批量开通的浏览器与 8770 版本要求在该能力内 |
| should-vm-01 | ots-voice-mail | 留言 IMAP 直收进邮件客户端正是该能力 |
| should-vm-02 | ots-voice-mail | 留言邮件通知排障从外部 SMTP 通知链路查起 |
| should-client-01 | ots-clients-multi-devices | OTC 装上但电话功能不可用首先查 Desktop 许可决定的全量/One 模式 |
| should-client-02 | ots-clients-multi-devices | 软电话当第二设备走 Multi-devices 许可勾选组合 |
| should-maint-01 | ots-maintenance-rehosting | 改服务器 IP/主机名即 rehosting 场景 |
| should-maint-02 | ots-maintenance-rehosting | rehosting 只改 OT 自己、OXE/8770 按 TC2149 收尾 |
| should-sot-01 | ots-sot-installation | 无光驱装机在 SOT 三路线选择范围内 |
| should-sot-02 | ots-sot-installation | OVA 导入走 web client、vSphere client 限 ESXi≤6.0 |
| should-cert-01 | ots-certificates | 换自签 Internal 证书属三路线之一 |
| should-cert-02 | ots-certificates | 外部 CA 从 CSR 到导入加 Deploy 正是该能力流程 |
| should-sg-01 | ots-supervision-groups | 实时看全组状态并代接即监督组+OXE 代接 |
| should-sg-02 | ots-supervision-groups | 组员临时进出监督组属监督组管理范畴 |
| should-lab-01 | ots-lab-connections | OT 走 SSH、Telnet 不授权正是该能力连接规则 |
| should-lab-02 | ots-lab-connections | ITSP1 模拟器验证外呼正是该能力 |
| bait-wizard-01 | ots-sot-installation | 软件还没装属装机问题，向导是装完首次开机才出现 |
| bait-sot-01 | ots-post-installation-wizard | 装完重启进向导，第一屏与口令规则属初始化向导 |
| bait-license-01 | ots-license-flexlm | 扩容许可问题首先命中 FlexLM 许可体系 |
| bait-sip-01 | ots-prior-management | 话机不加 0 而 OTC 可以是前缀/编号计划问题，先查 prior management |
| bait-node-01 | ots-node-declaration-sip | 节点声明失败先查声明与打通配置而非重装 |
| bait-vm-01 | ots-voice-mail | 留言进 Outlook 首先命中 IMAP 收取能力 |
| bait-client-01 | ots-clients-multi-devices | OTC One 免费模式与 Desktop 模式差异正是该能力 |
| bait-maint-01 | ots-maintenance-rehosting | rehosting 后 OXE/8770 是否自动跟随正是 TC2149 收尾知识 |
| bait-cert-01 | none | SBC 与反向代理安装部署不在十二个能力任何一项内 |
| bait-users-01 | ots-users-profiles | Users 应用只能改档案不能建删正是该能力边界 |
| bait-sg-01 | ots-supervision-groups | 监督键与 OT 监督组关系首先查监督组能力 |
| bait-lab-01 | ots-lab-connections | letacla 是教材实验值，公开教学值规则在该能力内 |
| edge-ha-01 | ots-post-installation-wizard | 向导中 HA 保持 Disable 是该能力明确边界 |
| edge-license-ok-01 | ots-post-installation-wizard | 许可 OK 只代表文件在正是向导页的边界说明 |
| edge-announcement-01 | ots-voice-mail | 通用公告一条 5 分钟覆盖式正是该能力边界 |
| edge-esxi-01 | ots-sot-installation | ESXi 版本支持矩阵归属装机能力 |
