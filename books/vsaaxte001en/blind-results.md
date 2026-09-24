# vsaaxte001en 盲判结果（仅依据能力目录，判定后锁定）

should-install-01 | vaa-install-sip-integration | 安装脚本参数契约与装后测试树拨通验证归安装对接能力
should-install-02 | vaa-install-sip-integration | 中继网关状态四层排障归安装对接能力
should-tree-01 | vaa-multitenant-tree-design | 日历+VIP 过滤+转接正对 UC2 用例的树设计
should-tree-02 | vaa-multitenant-tree-design | 多语言菜单是 UC3 用例，语言前置语音处理归树设计
should-prompt-01 | vaa-prompt-tts-asr | WAV 格式要求（8KHz PCM 16-bit 单声道、名称无空格）是上传失败根因
should-prompt-02 | vaa-prompt-tts-asr | Pico 不建议生产、Google Cloud TTS 推荐正是 TTS 引擎选型内容
should-ivr-01 | vaa-ivr-option-nodes | 收号节点异常兜底（min=max 判失败、超时）归选项节点
should-ivr-02 | vaa-ivr-option-nodes | HTTP 节点 JSON 点语法取值归选项节点
should-ha-01 | vaa-master-slave-ha | 双机部署 addslave 与 OXE 侧 ARS 双路由自动切换归高可用
should-ha-02 | vaa-master-slave-ha | Master 恢复后必须手工 resync 的口径归高可用能力
should-maint-01 | vaa-maintenance-backup | 三级备份命令与自动备份调度归日常维护能力
should-maint-02 | vaa-install-sip-integration | 4.8.006 只支持全新安装+数据库恢复的版本约束在安装能力内
should-db-01 | vaa-db-integration | 树与外部库打通查号转专属顾问是 SQL 节点+External Databases
should-db-02 | vaa-db-integration | MS SQL 连不上的默认值陷阱归外部数据库集成
should-stats-01 | vaa-statistics-reporting | xlsx 邮件周报开关、收到时间与数据日期口径归统计报告
should-stats-02 | vaa-statistics-reporting | 呼叫日志逐节点时长定位慢环节归统计报告
should-webadmin-01 | vaa-webadmin-administration | 新管理员默认密码=用户名必须立即改归 WebAdmin
should-webadmin-02 | vaa-webadmin-administration | SMTP 保存后必须重启服务归 WebAdmin 告警配置
should-pcs-01 | vaa-pcs-opex-licensing | 远端站点断网接管是 PCS 应急能力
should-pcs-02 | vaa-pcs-opex-licensing | OPEX Purple On Demand 三前提归该能力
should-sizing-01 | vaa-server-sizing-virtualization | 40 路并发对应三档规格与 120 端口上限归选型能力
should-sizing-02 | vaa-server-sizing-virtualization | Proxmox 8.2 自 4.6.1 起的虚拟化前提归选型虚拟化
should-arch-01 | vaa-architecture-redundancy | 组件分工与四步呼叫流归架构全景
should-arch-02 | vaa-architecture-redundancy | multi-company 不能预留端口的口径归架构能力
bait-install-01 | vaa-server-sizing-virtualization | 能用什么系统平台装属服务器选型与虚拟化前提，非安装参数
bait-tree-01 | none | OXE 上建 ACD 队列与坐席组是 OXE 话务工程，不在 VAA 能力目录内
bait-prompt-01 | vaa-prompt-tts-asr | TTS 自然度问题首先归 TTS 引擎选型（Pico 与 Google Cloud TTS 之别）
bait-ivr-01 | vaa-db-integration | 数据库驱动安装是 JDBC 手装内容，非 IVR 节点配置
bait-ha-01 | vaa-architecture-redundancy | OXE 呼叫服务器主备与冗余用例归架构冗余全景，非 VAA 双机
bait-maint-01 | vaa-webadmin-administration | Supervision 按钮的使用警告在 WebAdmin 能力内
bait-db-01 | vaa-db-integration | MongoDB 能否直查看支持的数据库清单，归数据库集成
bait-stats-01 | none | OXE 自带话务统计是 OXE 管理范畴，VAA 能力目录不覆盖
bait-webadmin-02 | vaa-maintenance-backup | 密码策略与锁定归维护能力的密码策略条款
bait-pcs-02 | none | OXE 站点间 CPS 冗余工程是 OXE 侧工程，超出 VAA 能力目录
bait-sizing-02 | vaa-server-sizing-virtualization | VMware Workstation 是否受支持看虚拟化前提清单
bait-arch-02 | none | 双网卡绑定是操作系统网络工程，VAA 能力目录不覆盖
edge-install-01 | vaa-install-sip-integration | 4.8.006 只支持全新安装的约束决定能否原地升级
edge-ha-01 | vaa-master-slave-ha | Slave 只读无统计与 resync 行为口径决定缺数能否补回
edge-ivr-01 | vaa-ivr-option-nodes | 收号节点对星号键的处理规则归选项节点
edge-stats-01 | vaa-statistics-reporting | 周报选周一收到周一数据的口径与调整诉求归统计报告
