# 决策规则速查 — OXO Connect - Advanced (Participant's Guide, Edition 18)

| 能力 | 一句话规则 |
|---|---|
| SIP 组网：公网网关与私网互联 | 九 tab 固定顺序（DNS 先于 Domain Proxy、索引后回填）+ 带宽最少 5 通话放行外呼；私网组网叠加 ARS 双向溢出，P/T 字符验证 |
| ARS 路由套件：三表协作与 Internal ARS | 编号计划触发、ARS 表匹配变换（加/吸收/替换/透明）、中继组列表按序选路；Internal ARS 用虚拟 Provider+Local+日组时段把一个 DDI 分流到多目的地 |
| 酒店与计费垂直方案 | 有 PMS 走 OHL、无 PMS 用前台话机 Hotel 键；计费三通道（Hotel Metering/Time based/XML 小票，Time based 与 AOC 互斥）；账号码 250 条兼作权限钥匙 |
| 系统安全加固 | 强制改密 + AutoPwdChk 自动检查（4 周默认）+ Network IP Services 网络面收敛 + ETH1 限制 + 锁定翻倍封顶 1440 分钟 + 端口/紧急号码/LDAPS 加固清单 |
| 证书与加密传输（证书/DTLS/TLS-SRTP） | 证书四类端口矩阵（WebDIAG 主接口）+ 2K/4K 迁移与回滚（先切回 2K）+ DTLS 只保信令（300 连接、仅 OCE）+ TLS/SRTP 双实现（OCE 原生、OCE-FE 代理各 20 通话） |
| 语音导航套件（AA/MLAA/SCR） | AA 两树两级、MLAA 按 DID/CLI 最多 5 棵 3 级树（消息总量 12000 秒）、SCR 按客户码+时间 10000 条规则；改动生效靠引擎复位或等 10 分钟 |
| 语音邮箱与移动办公 | VM 远程接入+ACC 两级控制+锁定翻倍（封顶 1440 分钟）；游牧模式 VMU 选项 6 激活、CLI 三选一；远程替代 DDI+接入码+分机+密码，内部号加 |
| Cloud Connect 舰队与远程维护 | OXO 主动外连免改防火墙、注册自动免 license、Fleet 数据一天一刷新；SW 更新看 [D..]/[.S.]/[..P] 需 advanced 权限；互联网远程目标端口永远 50443 |
| 交付地基：OMC 首连与 IP 规划 | Expert 模式首连（pbxk1064 仅首连）+ 证书入受信任根 + 逐客户改密；IP 四页签改完必须重启；IPDSP 安装前先完成 NTP 时间同步 |
| 终端生态：PIMphony 与 SIP 话机接入 | SIP 注册基线（5059/≥120 秒/UDP 优先）+ 媒体三处理（DSP/RTP proxy/Direct RTP）+ 透传开关两侧独立；PIMphony 四 profile 与两级更新策略 |
| 共享终端：站群监督、Hot Desking 与 Multiset | 监督 50 键/每键 8 号（通知 pop-up+音调+闪烁）；Hot Desking 200/200、前 2 免费、683/682；Multiset 1 主 2 副共享主号，铃型 MLTSETRING 三值 |
| 多实体与伪多公司 | 4 实体上限（独立 MoH/可禁实体间呼叫/话务员组公共）；伪多公司用链路类别配对+矩阵直线+ARS 透明线实现同前缀各走各线、Char 1/2 验证 |
| DECT 无线移动 | 双轨容量（80 xBS/11 并发、60 IBS/6 并发、200 手柄）；集群内切换、站间不切换；勘测以 -72 dBm 划语音质量区；SUOTA 并发 50、swap 须充电座 |
| 维护工具箱：Webdiag、Noteworthy 与 LoLa | Webdiag 三会话七块信息树；noteworthy 四类内存地址（TC1398 为准、写错致系统恶化、cold reset 回默认）；LoLa 三类加载与迁移（话机配置 OMC 先存） |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
