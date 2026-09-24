# Book Overview（参考区）— Rainbow / OmniPCX Enterprise 集成

> 供能力卡引用的背景参考；源自 references.md 落位。

## 交付主线（组织轴）

云侧开户开订阅（BP）→ OXE 配 DNS/代理 → PBXID+激活码接入 Rainbow → 分机关联（RCC）→ REX/tandem 远程延伸路由 → 部署 WebRTC 网关并配 OXE 侧九件套（解锁完整 VoIP）→ 共享池化扩容 → 话务台/维护/Teams 三个增值域（p3-314 章序）。

## 实验环境（RLAB，仅 Boundary 背景）

- POD 结构：每 POD 6 台实例（OXE、OMS、FlexLM、WebRTC 网关、PC Client 10/11）+ 公共资源区（NAS、SIP 模拟器、外部 DNS）；POD 间互不可见（p5-11）。
- 实验网段 192.168.1.x：OXE CS 主 192.168.1.3、WebRTC 网关 192.168.1.15、Pod 网关 192.168.1.254、内部 DNS 192.168.1.250、外部 DNS 10.20.30.250；OMS 192.168.1.13、FlexLM 192.168.1.80；PC Client 10/11 为 192.168.1.10/.11（p9，实验口径）。
- 实验账号：网关登录 rainbow/Rainbow123；培训管理员与成员 cCpP.admin / cCpP.user1 / cCpP.user2@ale-training.com（Superuser-P*，C=班号 P=POD 号）；培训邮箱 mail44.lwspanel.com（PasswordP*）；SIP 模拟器注册 pbxP/alcatel；OMS/FlexLM 为 Superuser2580* / letacla1（p9/p61/p63/p73，均为实验口径）。
- 实验分机与编号：IPDSP 31000（PC Client 10）/ 31001（PC Client 11）；4059 关联话机 31002；Ghost Z 建议 DB1000；REX 编号 21<主号 QMCDU>；留言信箱示例 31499；个人话务呼叫前缀 31401；话务组 A0000/话务台 B0000（p72/p122-125/p208-210，实验口径）。
- SIP 模拟器 ITSP1：gateway1.itsp1.com（10.20.30.51）+ public.itsp1.com（10.20.30.50）；SIP 域 sip.itsp1.fr；号码规则 3311PN12345 系（PN=两位 POD 号）；紧急 112/15/17/18；DDI 段首外部号 3321PN41000、首内部号 31000、范围 500（p14-17，实验口径）。
- 网关样例版本：Rainbow WebRTC Gateway 1.78.11-470、rainbowagent 6.0.1；mpconfig 默认输出 TURN_SERVER=GEOIP、WRTRANGE=20000-29999、SIPRANGE=30000-39999、RINGINGAUTO=true（p87/p158-159，样例值）。
- 培训订阅口径：只用 Voice/Attendant MONTHLY，禁用预付（p57/p239）。

## 平台速览（方案沟通素材）

- Rainbow 定位：UCaaS（协作/云话音/会议）+ CPaaS（开放 API/SDK，developers.openrainbow.com）；混合云集成 OXE/OXO/第三方 PBX（p20-23）。
- 订阅 8 种：Essential（免费无 SLA 无电话）/ Business / Enterprise / Attendant / Enterprise Conference / Conference / Connect（CRM）/ Room（p24）；电话服务必须 Business/Enterprise/Attendant（p56）。
- 路由地基：REX+Ghost Z（每并发一个）；tandem 两端 multi-line；agent 按路由自动改写 REX——computer 路由写 BBB 前缀 17 位号走网关，mobile/home/other 走公共 trunk（p111-113, p184-185）。
- 网关三重前提：Business/Enterprise 订阅、OXE 12.1 MD4/12.2+、PBX 已接入且分机已关联（p133/p135/p154）。
- 容量口径：单网关 400 并发流（TBE067 估算，适用 OXE 101.0 MD3 / WebRTC 3.x 起）；用户数与并发数是两个量纲（p151）。
- 话务台两套：4059EE（OXE 传统，关联话机禁 multi-line，不用 Attendant 订阅）；Rainbow Attendant Console（Attendant 订阅，队列 OXE 10/OXO 8，仅 PC 端）；监督组 5 组/30 人、互助 4 路、代接仅限同 PBX 电话呼叫（p200/p209/p227/p230/p232/p235）。
- Teams 集成：工作站级；App 管电话面 + Desktop 管呼叫控制（必须常驻）；权限收敛 Telephony；在场同步须激活 O365 共享；SSO 非必需（p259/p272/p297/p304/p306-307）。

## 教材口径声明

- 全部实验密码/账号/网段仅限实验环境；生产必须替换并做安全加固（原书明文密码遍布正文，引用时一律标"实验口径"）。
- 生产化边界四文档：Rainbow Network Requirements PDF（网络数值）、TC2462（OXE-Rainbow 集成配置）、TBE067（容量估算工具）、VoIP calling Troubleshooting guide（深排障）——均为原书指定权威来源。
- 版本敏感点：网关前提 OXE 12.1 MD4/12.2+（p135）与 sizing 工具适用 OXE 101.0 MD3（p151）为新旧两套版本命名并存（needs-review nr-03）；远程升级 1.73.x+/35 国随版本演进（n18）。
- 书内不一致：user2 邮箱跨章姓名不一（nr-01）；incvisu/invisu OCR 变体（nr-02）；Teams 章两段重复（nr-05）——详见工作区 needs-review.md。
