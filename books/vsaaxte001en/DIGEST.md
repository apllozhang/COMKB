# DIGEST — Visual Automated Attendant 安装、配置与维护精华长文

> 源：VSAAXTE001EN Edition 20（351 页）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 VAA 交付与运维的全局认知；操作细节按需查 12 张能力卡。

## 一、这套东西是什么

VAA（Visual Automated Attendant）是 ALE 跑在 SUSE Linux 上的**软件话务台/IVR**：多租户、SIP 协议、7×24 呼叫路由与欢迎语，宣称符合 CIS-2 安全标准。它和 OmniPCX Enterprise（OXE）是分工关系——OXE 保留呼叫控制与路由，VAA 经 ABC/F 型 SIP 中继接管被叫号码的脚本执行（放欢迎语、收号、转接）。

整本教材就是一条交付主线，五个阶段依次递进：装 VAA、OXE 侧 SIP 对接、树设计、高可用、运维与集成。

三个数字先记住：

| 数字 | 含义 |
|---|---|
| 120 端口 | VAA 单机最大端口数，超限找中央售前 |
| Release 11 | 4.8.006 强制新许可（.lic/.vaa 绑 MAC 与 FQDN，旧许可失效） |
| 92 天 | Web 管理密码默认有效期，到期前 30/7/1 天邮件提醒 |

## 二、安装：一条参数契约定生死

安装三条路：手工（教材主线）、S.O.T 全自动（只能自签证书、incoming username 固定为 vaa）、Purple on Demand。4.8.006 只有"全新安装 + 数据库恢复"一条支持路径，没有原地升级。

install.sh 的参数清单是 VAA 与 OXE 的**接通契约**，关键几项：

| 参数 | 要点 |
|---|---|
| incoming username | 必须与 OXE 外部网关完全一致、无密码留空、认证方式 None——接不通先对这对字符串 |
| 编解码 | G711a/G711mu/G729 勾选；G729 与语音识别（ASR）互斥，要用 ASR 必须 G711 |
| 证书 | /tmp 放 PKCS12 或 PEM 自动识别；不给就自签（生产提前用 CA 生成，SAN 必填 IP 与 DNS） |
| 转移禁拨前缀 | 实验留空；生产不配等于开放外部 callers 借 VAA 外转 |
| 自动备份 | 装完即启用（Daily 午夜起）；一旦启用无法关闭 |

OXE 侧是**手工五段链**，缺一段就可能接不通：

- SIP trunk group：T2 型、Q931 变体 ABC-F、独立 remote network、T2 specificity=SIP
- 本地 SIP 网关联动（初始化 SIPMOTOR）；外部网关（type=VAA、端口 5060 UDP、监督定时器 60、incoming username 与安装一致）
- 信任 IP 与网络路由表；前缀计划（实验 314 前缀 5 位）

装完验收就一句：vaa status 全部 Running，拨 31400 听到欢迎语后自动挂断。排障四层抓手：trkstat 中继状态、sipextgw 网关状态、OXE 抓包（motortrace/mtracer）、VAA 侧 softcmp (SIP) 日志。

## 三、树设计：多租户 + 三级用例

公司（租户）四要素：时区、DID 段、留言前缀、分机位长。**依赖物先行**：日历、营业时间、过滤器、提示音必须在建树之前建好。12 种原生节点覆盖绝大多数需求（欢迎/菜单 12 键/监督或盲转/忙无应答分支/日历/营业时间/过滤/跳子树/远程录音/挂断）；9 种 IVR 选项节点（收号、ASR、SQL、HTTP、邮件、条件、变量、相关数据、自定义显示名）另购许可，负责对接信息系统。

三级用例递进：

| 用例 | 场景 | 关键节点 |
|---|---|---|
| UC1 简单转接 | 欢迎 + 监督转 + 忙/无应答分支 | Announcement、Transfer（Wait 15s、Bypass forward）、Release |
| UC2 日历+过滤 | 营业时间/假日闭馆 + VIP 分流 | Calendar、Business hours、Filter、两个 Transfer（盲转） |
| UC3 多语言菜单 | 法英双语四选项菜单 | 语言选择菜单、Select language、Menu（重试 2/超时 4s）、Voicemail、Go to tree |

两条铁律：**每个节点必须个性化命名**（名称直接进统计与呼叫日志，随手默认名等于放弃排障）；多语言树的语言选择前提示必须**双语同文件**（语言选择发生在播报之后）。路由绑定推荐一号一树，通配符"可用但不推荐"。

## 四、高可用：一半在 VAA，一半在 OXE

VAA 侧只做数据复制（Master→Slave），切换动作由 OXE 的 ARS 双路由完成。行为口径是客户预期管理的硬底线：

| 行为 | 口径 |
|---|---|
| 切换丢话 | 任何切换都丢进行中呼叫（原书三处重复），SLA 只保证新呼叫 |
| Slave 只读 | 故障期间它处理的呼叫不产生统计 |
| 不自动回同步 | Master 恢复后必须手工 vaa ha resync，Web 客户端要手动重连 |
| 首呼延迟 | 切换后第一通呼叫有短延迟（OXE 判定中继断），属预期 |

部署口诀：slave 独立安装（FQDN vaa2、incoming username vaa2、license2.vaa），配置一律从 master 发起——`vaa ha addslave` 会用 master 库快照**清空 slave 现有配置**。

OXE 侧要补第二套中继/网关/识别符/NPD/ARS 双路由才真正生效。N+1 是另一种结构（扩容型，reference VAA 故障期配置冻结），别和双机混谈。

## 五、运维与集成速览

- **命令族**：vaa stop 保留 postgresql 与 nginx，fullstop 全停；status/services/version 巡检；services 输出直接看许可三项（VAA_PORTS/VAA_IVR/VAA_RELEASE）
- **备份三级**：db（仅库）/cert（nginx 证书与配置）/full（库 + vaa.conf + secureCall 证书）；自动备份启用后关不掉，系统不监控磁盘，按 6 个月 20GB 起预估
- **升级**：备份先行，新 vaa.conf 可能新增必需参数——旧备份不能直接覆盖，逐值比对后 vaa restart；HA 全员升级后 master resync
- **告警**：邮件三类（中继断/恢复、端口到限、许可问题）；SMTP 改完必须重启服务；SNMP 默认关
- **统计**：四指标（收到/已处理/主叫挂断/许可不足丢失）+ 呼叫日志逐节点时长（排障利器）+ xlsx 邮件周报（选周一收到的是周一数据，次日报前一天）
- **数据库集成**：默认只有 PostgreSQL/MariaDB 驱动；MS SQL/Oracle 手装到 /opt/ale/aa-webapp/lib 且 HA 双机都要装；SQL 节点一次取一个字段、多条取首条、空结果不算错（必须 Condition 判）
- **PCS/OPEX**：远端站点断网本地接管但应急配置恢复即丢；OPEX（Purple On Demand）要云化 OXE + 单订阅 + 端口分摊，且与跨数据中心空间冗余互斥

## 六、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 装 VAA/对接 OXE/拨不通 | vaa-install-sip-integration |
| 建租户/编树/配营业时间 | vaa-multitenant-tree-design |
| 提示音/TTS/ASR | vaa-prompt-tts-asr |
| 变量/收号/HTTP/邮件节点 | vaa-ivr-option-nodes |
| 双机/ARS 切换 | vaa-master-slave-ha |
| 巡检/备份/升级 | vaa-maintenance-backup |
| 查库转接/JDBC 驱动 | vaa-db-integration |
| 周报/逐节点排障 | vaa-statistics-reporting |
| 管理员/SMTP/日志页 | 路由入口（visual-automated-attendant-router） |
| PCS/OPEX/许可/选型/架构 | 路由入口（visual-automated-attendant-router） |

## 版权

- 本精华长文为 ALE Training Services《Visual Automated Attendant — Installation, Configuration and Maintenance》（VSAAXTE001EN Edition 20）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
