# 盲判结果（8770xte200en）

判据：仅凭 capability_catalog 第一判断锁定，事后不回头修改。

```
should-install-01 | ovnms-platform-installation | 新服务器从系统配置到首次登录装 8770，正对七步装链与装前注意事项
should-install-02 | ovnms-platform-installation | 装完 Alarms/Topology 无数据，目录明确 IE ESC 与 Defender 排除是这两个应用的前提
should-node-01 | ovnms-node-onboarding | 网络号×100+节点号的声明计算与四种同步语义选择，节点接入核心题
should-node-02 | ovnms-user-provisioning | 用户建了但同步慢，目录里"实时同步核验与 NMC Alarm server 排障"在节点接入条目
should-user-01 | ovnms-user-provisioning | 批量开户+号段自动取号，对应 Meta profile 号段同步与批量文件
should-user-02 | ovnms-user-provisioning | 网页轻客户端开户不装厚客户端，对应 WBM 轻客户端及其限制
should-alarm-01 | ovnms-alarm-management | 主动触发告警验证送达，对应 rstcpl/incvisu 验证 #2042/#1125
should-alarm-02 | ovnms-alarm-management | Major 告警邮件出口+转发 NMS 平台，对应邮件出口与 SNMP Proxy
should-sec-01 | ovnms-security-administration | 管理员被锁四路解锁，目录锁定解锁条目直接命中
should-sec-02 | ovnms-security-administration | 密码 90 天过期/提醒/最短期限等策略参数，对应密码策略
should-audit-01 | ovnms-audit-compliance | 查谁改过 OXE 配置并要开审计留证，对应双侧启用与 History/Detail 导出
should-audit-02 | ovnms-audit-compliance | Audit System 页查不出数据，对应 System 页重建 PbxName Not Empty 排障
should-backup-01 | ovnms-backup-restore | 搬机房改 IP 改主机名整迁，对应 rehosting 三场景（改 IP/改 FQDN/换机）
should-backup-02 | ovnms-backup-restore | OXE 数据库恢复注意事项与恢复后连不上，对应 swinst 恢复链与 role address 用物理 IP
should-lic-01 | ovnms-license-management | 只剩 Directory 和 Configuration 两个应用，正对超限受限模式症状
should-lic-02 | ovnms-license-management | 下载新许可文件换装并确认生效，对应换文件五步
should-node-03 | ovnms-node-onboarding | OXO Connect 经 OMC 纳管后在 8770 侧声明节点，目录明确 1x100+80=180
should-user-03 | ovnms-oxe-ui-efficiency | 给用户预设功能键，目录里唯一配键条目是图形视图配键 Function/Content/Mnemo
should-sec-03 | ovnms-security-administration | 改 Access Profile 后界面可见性没变化，对应 Access Profile 删本地 MIB 生效
should-backup-03 | ovnms-backup-restore | 5.1 备份能否还原到 5.2，对应备份与版本绑定（nmcVersion）
should-reports-01 | ovnms-reports-scheduling | 每周定时报表邮件，对应报告计划+SMTP server:port 语法
should-maint-01 | ovnms-maintenance-operations | 服务能不能手动 Start，对应 NMC 服务两层"约 20 个被监督、不要手动 Start"
should-topo-01 | ovnms-topology-views | 园区背景图大屏摆设备连线，对应背景地图+Custom 编辑器建屏
should-ui-01 | ovnms-oxe-ui-efficiency | 编号计划与网格数据导出留档可导回，对应树与网格导入导出 .txt/.prg
should-netdrv-01 | ovnms-network-drive | 备份与报表落客户文件服务器共享，对应 REPORTS_ECO/BACKUP_ECO 与 ADM8770 配置
bait-install-01 | ovnms-node-onboarding | 已装完，问题在第一台 OXE 注册与同步，属节点接入非安装
bait-node-01 | ovnms-user-provisioning | 节点同步已好，问题是批量开户，属用户开通非节点接入
bait-user-01 | ovnms-security-administration | 给运维开账号并限权只看 Alarms，属管理员与组权限配置
bait-alarm-01 | ovnms-topology-views | 告警不上拓扑图、设备状态上图，对应告警重定向与 Source Object 层级
bait-audit-01 | ovnms-audit-compliance | OXO 管理操作进 8770 审计，路由到审计能力（边界：目录写明仅支持 OXE）
bait-backup-01 | ovnms-network-drive | 备份要存 NAS 共享但立即备份看不到网络位置，对应 BACKUP_ECO 映射而非备份流程本身
bait-lic-01 | ovnms-topology-views | 背景地图加了不出现，对应地图入 topology\maps 后重启 NMC Service Manager
bait-reports-01 | ovnms-audit-compliance | 审计记录定时导出报告发邮件，对应审计 History/Detail 导出 Immediate/Scheduled，非通用报表
bait-maint-01 | ovnms-maintenance-operations | 开支持工单前采集诊断，对应 Diagnostic 采集 C:\TS 出 HTML+zip
edge-node-01 | ovnms-node-onboarding | Partial/Complete 属四种同步语义的日常与开局选择
edge-alarm-01 | ovnms-alarm-management | acknowledge 后告警还在列表，属告警处置语义，归 incident manager
edge-sched-01 | ovnms-reports-scheduling | 关机错过计划任务是否补跑，对应 Scheduler Maximum start delay 补跑语义
edge-lic-01 | ovnms-license-management | 老许可文件装 R5.2，对应 N-1 版本规则（R5.2 吃 15/16）
edge-pwd-01 | ovnms-security-administration | 默认密码先上线是否可行，属密码策略与安全管理边界
edge-ha-01 | none | 目录无任何双机热备/高可用/单点故障条目，超范围
```
