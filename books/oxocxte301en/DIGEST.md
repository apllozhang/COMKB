# DIGEST — OXO Connect Advanced 精华长文

> 源：OXOCXTE301EN Edition 18（601 页）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立对 OXO Connect 进阶交付的全局认知；操作细节按需查 14 张能力卡。

## 一、这本书是什么

《OXO Connect - Advanced》（ALE 官方售后进阶培训教材，R6.3/Ed18 口径）讲的是从"会用 OXO"到"能独立交付复杂站点"的那一段：公网/私网 SIP 组网与 ARS 选路、酒店与计费等垂直方案、AA/MLAA/SCR 呼叫处理增强、语音邮箱与移动办公、Cloud Connect 云舰队、安全与证书体系、DECT 无线、Webdiag/LoLa 维护。

全书隐含主线就两条：**OMC/Webdiag 双工具操作** × **编号计划/中继组/ARS 三件套**——所有增强功能最终都落到这两条轴上，且每个实验都以"行为验证"收口（History Table 消息、显示字符、LED、计费小票文件）。

三个先记住的数字：

| 数字 | 含义 |
|---|---|
| 5 通话 | SIP 网关 Media 带宽最少 5 通话——不设就外呼不通（公网 p48/私网 p215 同规则） |
| 50443 | 互联网远程维护的入站目标端口永远是它（专用访问控制），公网侧端口可换 |
| -72 dBm | DECT 站点勘测的语音质量区边界，验收以通话中测音质为准 |

## 二、组网主线：从一根 SIP 中继到两张网

1. **公网 SIP 网关九步法**（p37-56）：LAN IP/DNS、编号计划、VoIP 接入与中继组、网关九 tab、SIP 账号、回填网关索引、验证注册。两条硬顺序：DNS tab 先于 Domain Proxy tab（不填 DNS 字段出不来）；网关索引要等网关建好后回填。验收判据：History Table 显示 "SIP registration success"。
2. **排障三层**：注册层查 History Table；信令层 Webdiag TCP Dump 选 SIP 抓包；分析层 Wireshark。默认 Security tab 是明文——要加密另走 TLS/SRTP。
3. **ARS 是路由大脑**：编号计划触发（base=ARS）→ ARS 表匹配并变换号码（加/吸收/替换/透明）→ 中继组列表按序选路。多运营商标准构图：移动走 GSM 网关、其它走低价 VoIP、ISDN 备份——两个列表共享同一子线索引即实现溢出；传真强制走某线路用流量分担矩阵。
4. **Internal ARS 反转用法**（p225-241）：把一个入站 DDI 按日组+时段分流到不同内部分机或欢迎消息。技法五级：编号计划 Secondary Trunk Group base=ARS；ARS 表子线替换成分机号；每目的地建虚拟 Provider；列表 Index 选 Local；Day Groups 与 Hours 排时段。
5. **私网组网双向溢出**（p206-224）：两台 OXO 经私网网关互联（Domain Proxy 填对端 IP、Protocol 选 SIP Option），私→公溢出（显示 T）与公→私优先强制（显示 P）各配一轮 ARS 行。

## 三、垂直与增强：按 license 分层

| 领域 | 免 license | 要 license |
|---|---|---|
| 垂直 | OHL 酒店链路、Call Accounting Time based（与 AOC 互斥） | 多实体 MoH（4 实体-10 分钟） |
| 呼叫处理 | AA 默认树（留言/转话务员；冷复位后默认 2 端口接外呼） | AA 树定制、MLAA 树数（1/5）、SCR+Supervisor Console |
| 终端 | 站群监督、Multiset | Hot Desking（前 2 HDU 免费、后按 50 包） |
| 安全 | 密码体系/自动检查/DTLS/TLS-SRTP/Cloud Connect | — |
| 无线 | — | IP-DECT 用户（200 上限） |

- **酒店**：有 PMS 走 OHL（Office Link Driver，V24/IP），无 PMS 用前台话机内置 Hotel 键（4 并发会话、300 话机、房对房闭锁）。进 hotel 模式必须先冷复位（默认 Business 模式）。计费三通道：Hotel Metering（预付/切断/3 级 2 阈）、Call Accounting Time based（按时长×呼型出脉冲、激活即停 AOC）、输出走 OLD 的 XML 小票（TicketCollector.xml）或 V24。
- **账号码**：表 250 条、码 16 位；内部替代（66 前缀+分机+密码）把账号码当权限钥匙——全员禁国际、仅经理放行的场景任何话机可"变成"经理外呼。
- **语音邮箱与移动**：远程接入三要素（VM 的 DDI+远程权+认证，ACC 可升级为三级控制）；锁定从 10 分钟起步逐次翻倍、封顶 1440 分钟。游牧模式经 VMU 选项 6 激活（SIP 话机不支持）；远程替代拨 DDI+接入码+分机+密码，内部号加 # 前缀走内部 ARS 回环。
- **MLAA 两条排障铁律**：line parameters 不随配置存档保存；端口与消息改动要 ACD 引擎复位或等 10 分钟。

## 四、安全与证书：R6.2 生产基线

- **密码**：首登强制改全部默认密码；管理密码固定 8 位含大小写数字；AutoPwdChk 默认 4 周自动检查（01-52 可配、00 禁用、warm reset 后必查），弱密码生成 urgent alarm。
- **网络面**：Network IP Services 三开关收敛 WAN/LAN 服务；ETH1 可限至仅 SIP trunk（OMC/WebDiag/OSC 全封）；两级开关是"与"关系——系统级关死时用户级开了也无效。
- **锁定公式**：认证连续失败锁时翻倍（10→20→…），封顶 1440 分钟；本地 LAN 不受锁；解锁五途。
- **证书**：四类证书一张端口矩阵（443/30443、50443、7780、10443、11443）；R6.2 起 4K，但 4K 存储格式不同——**回滚前必须先经 WebDIAG 切回 2K**，否则 OMC 报错。
- **DTLS 别当全案**：只加密 ALE 话机信令（TLS 1.2），语音包仍明文；语音机密性走 SIP 中继 TLS/SRTP（OCE 原生免 license；OCO 老平台走 OCE-FE 代理，GW 与 PROXY 各 20 通话）。

## 五、云、无线与维护

- **Cloud Connect**：OXO 主动外连（免改防火墙）、注册自动免 license；状态串 "Connected with final credentials"；Fleet 数据库一天一刷——注册后 24 小时才可见，当场看不到不算失败。软件更新看指示灯 [D..]/[.S.]/[..P]，执行要 advanced 权限。
- **远程维护**：SIP-only 站点没有 modem 通道，只能走 IP；IAD 转发"公网任意端口→50443"，绝不直接转发到 443；更安全走管理 VPN（专用 IP 仅 OMC 可配，warm reset 生效）。
- **DECT**：双轨容量（IP 轨 80 xBS/11 并发、TDM 轨 60 IBS/6 并发、200 手柄）；切换仅同集群内、站间不切换；"同步优先于信号"——话机可能赖在同步但信号差的基站。勘测 -72 dBm 划界+通话中测音质；SUOTA 并发 50、下载 4-8 小时且给话务让路、swap 须充电座。
- **维护三件**：Webdiag 三会话（installer 全功能/operator 管 MoH 与解锁/manufacturer 给支持）+七块信息树；noteworthy 是地下层调参（清单以 TC1398 为准、写错致系统恶化、cold reset 全回默认、铃音基址随版本变化必须现算）；LoLa 管系统加载与迁移（话机配置与语音提示必须 OMC 先存）。

## 六、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 接运营商/站点组网/注册排障 | oxoa-sip-networking |
| 多运营商分流/分时段来电分配 | oxoa-numbering-ars-suite |
| 酒店模式/客房计费/账号码 | oxoa-hotel-billing-vertical |
| 安全基线/弱密码/锁定/端口加固 | oxoa-security-hardening |
| 证书/DTLS/加密中继/4K 回滚 | oxoa-certificate-suite |
| 语音导航/客户码分流 | oxoa-attendant-suite |
| 远程查邮箱/游牧/远程替代 | oxoa-voicemail-mobility |
| 上云/批量更新/远程维护/目录同步 | oxoa-cloud-connect-fleet |
| OMC 首连/改 IP/终端/共享/多实体/DECT/维护工具 | 路由入口（oxo-connect-advanced-router） |

## 版权

- 本精华长文为 ALE Training Services《OXO Connect - Advanced》（OXOCXTE301EN Edition 18）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
