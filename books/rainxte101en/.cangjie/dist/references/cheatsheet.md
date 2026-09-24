# 决策规则速查 — Rainbow Hub (Participant's Guide, Edition 16)

| 能力 | 一句话规则 |
|---|---|
| Rainbow 公司体系与 Voice 订阅开通 | BP 建司开订阅（时区强制）、可见性默认 CLOSED、SSO/TOTP 认证；Voice 四档订阅两层分配，有 Voice Business/Enterprise 才能声明 Cloud PBX |
| Cloud PBX 声明与话务配置 | 一公司一 PBX 一 trunk；编号计划 2-9 位混长、出局前缀 0 或 9；首个注入号码默认公司主号；白黑名单按国际格式不带 + 或 00 |
| 成员管理与话务配置 | 五通道开户（手动/邀请/CSV/AAD/LDAP）、七分区设置；有 Voice 订阅才能配号；删除进 10 天宽限恢复即回落 Essential |
| ALE 设备 zero-touch 部署与 DECT 移动 | 按 MAC/IPEI 注册关联成员后自动取配置；禁 DHCP option 43/66/67、禁设备 web 页配置；DECT 8328 双站 20 机 / 8368 多站 1000 机 |
| 设备维护日志与 Generic SIP 接入 | 已注册话机禁直连、debug 会话 ≤15 分钟一次性口令；Generic SIP 六条限制、TLS 1.2+SRTP 强制、仅做补充不做大规模 |
| 呼叫组与话务分配 | 四类组对号入座；组 50 人、分发三型、队列溢出 10-900 秒 FCFS；经理 DID 挂组级；紧急组免前缀进组转警加 0112；录音存 2 个月 |
| 话务台与监督组 | Voice Attendant 解锁 PC 话务台（10 路排队）；监督组 5 页签/30 人/5 组；attendant group 全员须 Voice Attendant；激活话务台话机关联被删 |
| 欢迎服务与 IVR | 四件套（日历/提示音/欢迎服务/IVR）；开闭双路由可强制但下时段回 Auto；IVR 3 级 0-9 无许可、唯一提示建后不可改；素材 ≤4MB/120 秒 |
| Rainbow Hub 网络就绪核查 | 查 Network Requirements 文章+两份 PDF 取端口/带宽全集；Rainbow Pilot 测连通性与承载；带宽口径 Opus 80 kbps/G711 64 kbps |
| 多站点配置 | 单 Cloud PBX 下的逻辑分区：站点挂成员/号码/服务，站点主号与站点 MoH；内呼/组/目录跨站不变；副站点主叫权限要收紧 |
| 分析体系 | 计费用 CDR（纯 VoIP 不产生）、行为用仪表盘（7/30 天与 1 年口径）、质量用 MOS（抖动 <30ms/RTT ≤150ms/丢包 ≤1%） |
| Hub 维护与支持体系 | 八抓手：用户日志/设备监督/连通性/上报/状态页/维护预告/HelpDesk/SR（仅认证 Rainbow Hub 伙伴建 ESR） |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
