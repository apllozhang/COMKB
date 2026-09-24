# Book Overview（参考区）— Visual Automated Attendant

> 供能力卡引用的背景参考；源自 references.md 落位。

## 交付主线（组织轴）

准备 OXE 底座 → 安装 VAA（install.sh）→ OXE 侧 SIP 五段链对接 → 证书与 WebAdmin 初始管理 → 公司/日历/提示音 → 树设计（UC1-UC3）→ 节点专项（变量/收号/显示名/HTTP/邮件）→ 高可用（VAA 侧 + OXE 侧）→ 维护/升级/统计 → 外部数据库集成（p4, p63, p88, p105, p133, p143, p239, p272, p319）。

## 实验环境（RLAB，仅 Boundary 背景）

- POD 纯虚拟化、相互独立同构；每 POD 五虚机：OXE（VSAA_OXE）、OMS（VSAA_OMS）、FlexLM（VSAA_FLEXLM）、VAA Master（VSAA_VAA_MASTER）、VAA Slave（VSAA_VAA_SLAVE，基础实验阶段保持关机）+ PC CLIENT（p5-13）。
- 实验网段 192.168.1.x：OXE 主 .1 / 备 .3 / OMS .13 / FlexLM .80 / VAA Master .55 / Slave .56 / PC Client .10 / 网关 .254 / 内部 DNS .250；公共区 10.20.30.x（NAS、SIP 模拟器、SQL/Mail 服务器 12.0.0.2、外部 DNS .250）（p7, p9）。
- SIP 运营商模拟器 ITSP1：gateway1.itsp1.com（10.20.30.51，账号 pbxP/alcatel，SIP 域 sip.itsp1.fr）+ 公网网关 public.itsp1.com；号码规则含 POD 号 PN（安装号 3321PN、外线首号 41000、内线首号 31000），外呼回环（p15-17）。
- 服务器网络五参数：IP 192.168.1.55、FQDN vaa1.company.com、掩码 255.255.255.0、网关 192.168.1.254、DNS 192.168.1.250；slave 对应 192.168.1.56 / vaa2.company.com（p92, p248）。
- 实验账号口径：系统 root/admin 出厂 letacla1，改后 InternationalSuperuser1234* / Superuser1234*；Web 首连 admin/admin 改 Superuser1234*；GRUB 实验值两处大小写不一（nr-01，按 ≥14 位自定）；IPDSP 密码 0000；证书密码 alcatel；库凭证 vaa/vaa（p9, p80, p92-94, p123, p322）。
- 实验服务：SMTP 10.20.30.11:25（发件 vaa.podX@company.com、收件 administrator.podX@company.com）；MS SQL 测试库 10.20.30.11:1433（DB_VAA）；实验许可 5 端口 Release 11（p101, p232, p253, p322）。
- 培训禁启 VAA Slave（到 HA 章才启用，p64）；OXE 侧 netadmin -m 加两台 VAA 为防火墙信任主机（p70）。

## 平台速览（方案沟通素材）

- VAA 定位：软件自动话务台/IVR，7×24 呼叫路由与欢迎语，多租户、SIP 协议、CIS-2 安全标准；功能四栏（Generic/Administration/Features/Option），Option 栏需 IVR 许可（p20-21）。
- 架构：OXE 保留呼叫控制，经 ABC/F 型 SIP 中继把呼叫交给 VAA 执行脚本（放音/收号/转接）；管理面 HTTPS/TLS 1.2；组件族七件（aa-license-server/aa-media-server/aa-cli/aa-webapp/PostgreSQL 16/Nginx/tts-hub）（p42-43, p54）。
- 规格：三档 8/50/120 端口（双核 8GB/四核 16GB/八核 32GB），上限 120 端口超限找中央售前；表为示例口径（p52）。
- 高可用：Master/Slave 库复制 + OXE ARS 切换；任何切换丢进行中呼叫；Slave 只读无统计；Master 恢复后须 vaa ha resync（p44-47）。
- 语音资产：提示音三来源（WAV 8KHz PCM 16-bit 单声道/电话录音/TTS）；PicoTTS 免费不建议生产、Google Cloud TTS 生产推荐收费；ASR 需 Google API key 且与 G729 互斥（p34, p37, p141）。

## 教材口径声明

- 全部实验密码/账号/网段/token 仅限实验环境；生产必须替换并逐项启用安全项（SIP TLS、barring 禁拨前缀、SNMP、证书）（原书明文密码遍布正文，引用时一律标"实验口径"）。
- 生产化边界四文档：VAA Installation Guide（完整安装 4.2、公网证书 6.4、系统管理第 6 章）、VAA Administration Guide（路由表达式 4.3、TTS 第 10 章、上下文变量）、TBE083（multi-company）、OTEC-S VAA configuration Guide——均为原书指定权威来源。
- 版本敏感点：4.8.006 只支持全新安装 + 数据库恢复且强制 Release 11；HTTPS 强制自 4.6.104；Proxmox 自 4.6.1 支持；OXE N2 起默认 G729；SIP 抓包样例残留旧版本号（nr-03）。
- 书内笔误备查：证书章 URL 多写一位（nr-02）；GRUB 口令大小写不一致（nr-01）；p295 "version A" 多余字符（nr-05）。
