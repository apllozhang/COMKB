# 决策规则速查 — OpenTouch — OpenTouch Suite for MLE — Solution Overview / Starter (Participant's Guide)

| 能力 | 一句话规则 |
|---|---|
| OTMS 初始化向导（两模式十节） | 首次开机自动启动的站点安装向导——from scratch 十节或 restore from archive；口令至少 8 字符且无报错弹窗、DNS 正反向五类 FQDN、HA 保持 Disable、许可 OK 只代表文件在 |
| 许可体系与 FlexLM（安装、核查、外部切换） | 三族文件（.ice/.swk/.sw8770）、两种锚定物（物理机 ALUID、虚拟机加密狗）、FlexLM 内嵌或外部；spadmin 三计数全 0 才健康，外部化一条命令约 5 分钟 |
| 双向节点声明与 SIP 打通（含告警对接） | bics.conf 取凭证 → 8770 建 OXE/OT 节点 → OT 侧挂 OXE（2570/Codec 一致）；OXE 侧 trunk 10 加两条外部网关（5260/5040）与 trusted；SNMP v3 Inform 告警进 8770 |
| Prior management（号码段、前缀、拨号规则、UDAS、会议桥） | 号段在 OT 侧声明归属 OXE、前缀两侧同值且话务台前缀必配、按名呼打全客户端自动加前缀、UDAS 周期至少 1 禁 0、DAS 规则强制按国家保序 |
| 档案与用户供给（三类用户、WPC 批量） | 档案三件套（OXE profile 占号 + OT profile ACU-OXE 勾权 + 邮箱档案）合成 Connection user；Users 应用只能改档案；WPC 批量限 Chrome 且不建 Conversation 用户 |
| 语音邮箱、IMAP 收取与通知公告（Local Storage） | defaultVmsLS 默认就绪、建箱必选档案、留言 IMAP 直收（内嵌 1000 并发封顶）、通知走无认证无 TLS 的外部 SMTP 与唯一 SMS 网关、公告一条 5 分钟覆盖式 |
| OTC PC 客户端交付与多终端 | 同一安装包、Desktop 许可决定 OTC PC 全量或 One 免费模式；软电话走 Multi-devices（Desktop 勾、Nomadic SIP 不勾）；多终端最多 5 设备且 REX/DECT 各 1 |
| 维护、备份恢复与 rehosting（TC2149 矩阵） | 维护三通道（命令/otconsole/Portal 4448）、自动备份每日 00:01 周日全量、OT-V 必挂 NFS；rehosting 只改 OT 自己且 inactive 分区被清，OXE/8770/生态按 TC2149 收尾 |
| SOT 自动化装机与虚机手动导入 | 三路线（手动 DVD/手动 ISO/SOT 自动化）生产首选 SOT：standalone 或 hosted、媒体先于项目、PXE 静默装机；OVF 手动导入走 web client |
| 证书部署三路线 | security OFF 全球同款不推荐、自签 Internal SHA256 换证后必须重签 CTL、外部 CA 按 CSR 来源导 PKCS7 或 PKCS12；导入与 Deploy 是两步 |
| 监督组（话务监督、进出组与代接） | 同类型成员 2-40 人、一人一组、同 OT 节点、系统 500 组；Regular 与 Collaboration 两模式；代接走 OXE Direct call pick-up，前转与溢出会让呼叫脱离监督 |
| 实验 POD 与系统连接通道 | RLAB 两形态 POD 与公共资源区；OT 走 SSH（Telnet 不授权）、OXE 实验用 Telnet（启安全须 SSH）、8770 走远程桌面；ITSP1 模拟器验证外呼 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
