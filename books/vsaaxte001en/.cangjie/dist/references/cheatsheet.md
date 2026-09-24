# 决策规则速查 — Visual Automated Attendant — Installation, Configuration and Maintenance (Participant's Guide, Edition 20)

| 能力 | 一句话规则 |
|---|---|
| VAA 安装与 OXE SIP 对接接通 | install.sh 双侧契约（incoming username 一致、编解码与 ASR 互斥）+ OXE 五段链 + 测试树拨通 31400 + 四层排障 |
| VAA 多租户与树设计（公司/日历/UC1-UC3） | 公司四要素 + 日历/营业时间/过滤器先行 + 12 种原生节点拖树 + 三级用例（简单转接/日历过滤分流/多语言菜单）+ 一号一树激活 |
| VAA 提示音与 TTS/ASR 引擎 | 提示音三来源（WAV 导入 8KHz PCM 16-bit 单声道/电话录音/TTS）；Pico 免费不建议生产、Google Cloud 收费；ASR 需 Google API key 且与 G729 互斥 |
| VAA IVR 选项节点与动态脚本 | 九节点（变量/条件/收号/显示名/识别/相关数据/SQL/HTTP/邮件）+ 变量三类（Local/Global/Contextual 只读）+ 收号与显示名行为边界 |
| VAA Master/Slave 高可用与 OXE ARS 切换 | slave 独立安装 + master addslave（清库警告）+ 双侧五项验证；OXE 侧第二中继/识别符/NPD/ARS 双路由；行为口径：Slave 只读无统计、切换丢话、恢复后 resync |
| VAA 日常维护与版本升级 | vaa 命令族 + 密码策略（92 天/5 次锁定）+ 三级备份（db/cert/full）+ 自动备份规则（启用后关不掉、6 个月 20GB）+ 升级（备份先行、vaa.conf 逐值比对、HA resync） |
| VAA 外部数据库集成（JDBC/SQL 节点） | 装驱动（/opt/ale/aa-webapp/lib、HA 双机）+ 建连接（External Databases/JDBC URL）+ SQL 节点树（单字段/首条/空结果不算错）+ MS SQL/Oracle 接入 |
| VAA 统计与报告 | 报表四指标 + 呼叫日志逐节点时长排障 + CSV 导出 + xlsx 邮件周报（vaa.conf 双开关默认开、选周一收周一数据） |
| VAA WebAdmin 管理面 | 首连 admin/admin 强制改密 + 管理员角色分派（新账号默认密码=用户名）+ SMTP 告警（改后必重启）+ 四页（Server info/Supervision/Logs/License） |
| VAA PCS 同步与 OPEX/许可体系 | vaa conf pcs/sendBackup（01:00 起 cron 错开）+ OPEX 三前提（云化 OXE/单订阅/端口分摊、每晚午夜校验）+ FlexLM 许可绑定 MAC/FQDN 核查 |
| VAA 服务器选型与虚拟化 | 规格三档（8/50/120 端口对应双核 8GB/四核 16GB/八核 32GB、上限 120）+ Hypervisor 三前提（ESXi/Hyper-V/Proxmox、VMXNet3）+ root 禁 SSH 走 sudo |
| VAA 架构与冗余全景 | 组件族七件 + 四步呼叫流（OXE 呼控/VAA 执行脚本）+ multi-company 端口共享 + N+1 reference 结构 + OXE 冗余三用例（切换必丢话） |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
