# 决策规则速查 — Rainbow / OmniPCX Enterprise (Participant's Guide, Edition 12)

| 能力 | 一句话规则 |
|---|---|
| Rainbow 公司体系与订阅开通 | BP 建司开订阅、EC 管成员分订阅；可见性默认 CLOSED；电话服务必须 Business/Enterprise/Attendant；BP 专属建 PBX 与开付费订阅 |
| OXE 接入 Rainbow 与接入排障 | 先 DNS/代理（nslookup/dig 验证）再 PBXID+激活码启用 Rainbow Agent；incvisu 五链路全 in service 即健康，四抓手排障 |
| Rainbow 成员全生命周期管理 | 手动/邀请开户（CSV/AAD 为讲义级）；密码 ≥12 位含大写/数字/特殊字符；删除进 10 天宽限，恢复即回落 Essential 须重配 |
| OXE 用户形态决策与远程延伸路由 | 四形态对号入座（RCC/tandem 路由/纯 REX/DECT 特例）；Ghost Z 池=REX 并发上限；tandem 两端 multi-line，配置只做主站；路由不等于转发 |
| WebRTC 网关部署与升级 | 三重前提核查 → OVF 部署 VM（mpnetwork/mpconfig）→ mpshow/mpcheck 核验 → BP 激活；升级远程优先（BP 账户）手动兜底（mpupgrade） |
| OXE 侧 WebRTC 网关配置九件套 | SIP TG/可信 IP/Rainbow type 网关/无压缩 IP 域/CDT/ARS/BBB 判别器/回调翻译按固定口径配，四项 VoIP 测试收尾 |
| 共享 WebRTC 网关池与容量规划 | 共享池为默认解（复制仅超高流量划算）；网关满载回 SIP 406 触发 ARS 溢出；TBE067 四输入估通道数，单网关上限 400 并发流 |
| Microsoft Teams 集成全流程 | 工作站级集成：Teams App 管电话面 + Rainbow Desktop 管呼叫控制（必须常驻）；权限收敛 Telephony；在场同步须激活 O365 共享 |
| OXE 分机关联与 RCC 模式 | Telephony 页签绑定分机即得 RCC（接/挂/转、音频在话机）；Rainbow number 由 agent 在选 computer 路由时自动写入 |
| 两套话务台（4059EE 与 Rainbow Attendant Console） | 4059EE 走 OXE 传统话务（关联话机禁 multi-line），Rainbow 话务台要 Attendant 订阅（队列 OXE 10/OXO 8）；代接仅限同 PBX 电话呼叫 |
| Rainbow 维护与支持体系 | 五入口：帮助台指南/用户日志与问题上报/状态页与告警/操作历史/SR（仅 Rainbow 认证伙伴建 ESR） |
| Rainbow 网络就绪核查 | 查 Network Requirements 文章+两份 PDF 取端口/帶寬数值；Rainbow Pilot 测连通性与按用法配比评估承载 |
| RLAB 实验环境与 Pod 配置 | 6 台虚机基线核对、按 POD 号对齐 SIP 注册与 DID 翻译、外呼验证公网载体；一切 IP/账号/号码为实验口径 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
