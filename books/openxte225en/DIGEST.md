# DIGEST — OpenTouch 移动与远程办公 集成精华长文

> 源：OPENXTE225EN Issue 10（287 页，OpenTouch R2.6 口径）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立"把 OpenTouch 通信服务安全开放到互联网"的全局认知；操作细节按需查 12 张能力卡。

## 一、这套东西是什么

OpenTouch 是 ALE 面向中大型企业的通信套件（OTMS 管理 + OXE 呼叫服务器 + OmniVista 8770 网管）。这本教材解决一件事：**让 OTC PC 与智能手机从互联网全功能接入公司通信系统**——话音、视频、IM、协作、会议一个不少。

整本教材就是一条交付主线：**证书打底、服务器侧申报、DMZ 边缘部署（OTSBC + 反向代理）、客户端开通（PC 两模式、智能手机、iPhone 推送）、拨测收口**，五段按序推进。

三组数字先记住：

| 数字 | 含义 |
|---|---|
| RP + OTSBC | DMZ 双边缘：反代管 Web 服务通道，SBC 管 SIP/媒体通道；VPN 只是官方标注的"技术替代" |
| CA 签发 | 远程访问必须 CA 证书；预载"通用证书"（security off）被官方明确反对——话费欺诈与服务盗用风险 |
| 5261 / 8061 / 5265 | OTSBC 公网端口：OTC 客户端 / WebRTC / iPhone+ 专用声明 |

## 二、架构三件事：拓扑、DNS、证书

- **双边缘分工**：反向代理（RP）管话音与协作 Web 服务的 HTTPS 会话（拓扑隐藏、认证、URL 封禁、SSL 卸载），是第三方产品；OTSBC 管 SIP 信令与 RTP/SRTP 媒体（DoS 防护、加密、CAC、NAT 穿越）。RP 可由 OTSBC 7.2+ 兼任，但认证部分要另配服务器。
- **用例矩阵查表**：OTC PC 要 RP+OTSBC；OTC PC One 只要 RP（N.U.——没有 VoIP 可保护，别报成"不支持 SBC"）；OTC Web 只要 RP；WebRTC 与手机端要 RP+OTSBC。
- **DNS 内外分离**：同一批 FQDN 两套解析——内部解析到私网 IP，公共 DNS 解析到 RP/SBC 公网 IP；OTSBC 的 WAN 接入不用进内部 DNS。
- **证书红线**：远程访问必须 CA 签发；封装看私钥在哪生成（本机生成走 PKCS7，CA 生成走带口令的 PKCS12）；会议服务专用 FQDN 必须进反代与 OT 服务器证书的 SAN；换证书后话机侧 CTL 必须重签（另一培训规程）。

## 三、部署链四段

1. **服务器侧申报**：三小步，缺一段客户端就进不来。

   - OmniVista 8770 申报反代四 URL（API/EVS/ACS/DMS），EVS 必须带 :8016 端口，漏写则通知类功能失效
   - 申报 OTSBC：5261 给 OTC 客户端、8061 给 WebRTC
   - 会议侧核对 DAS 规则（强制、国家相关、顺序重要）并配 ACS 会议专用 FQDN
   - ACS 没随初装配置就跑 ot-config.sh --rehost，再重签证书把会议名加进 SAN

2. **OTSBC 部署**：OVF 上电、CLI 初始化（改完 write + reload）、更新许可、TLS 上下文配证书。

   - 跑"Alcatel-Lucent Remote Users"向导模板，一键生成绝大部分对象
   - 向导两个坑：只给 OXE 配 UDP（手工补 TCP 5060）；iPhone 对象不覆盖（官方明示查 TC2639）
   - 收尾把每个 SIP 接口的证书换成自签发的

3. **反向代理两路线**：功能同向，按现场条件选。

   - 已有 OTSBC 且许可含 HTTP proxy 就内嵌（省一台机器）；否则独立 Nginx 虚机
   - OT 2.2 起 Nginx 必须 remoteworker.conf 与 conference.conf 两份同改（OTES 退场、会议共享走反代）
   - 反代层认证生产要做：Nginx 用 LDAP 模块（仅 Python 2，daemon 监听 8888）；内嵌路线认证 daemon 要专用机器
   - 模板链接以 TC2639 最新版为准，书内快照可能过期

4. **客户端开通**：PC 与手机都是"接入配置 + 路由档案"两步；用手机直接拨号时永远本机发话，"dial from"设置不影响——这是设计行为不是故障。

## 四、终端形态三张表

OTC PC 两模式并存：

| 模式 | 原理 | 资源 |
|---|---|---|
| multi-devices（新法） | SIP 分机绑副设备，主话机保留 | COS 振铃参数 + 506/507 两前缀并在用户 COS 授权 |
| Nomadic SIP（老法仍在） | 主话机冻结、SIP 软话机顶替 | 每并发占 1 SIP 设备 + 1 Ghost Z，池化、退出才释放 |

智能手机自动对象矩阵（关联一次自动建，按模式增减）：

| 对象 | Mobile only | WiFi only | Dual | Dual+GSM 号 |
|---|---|---|---|---|
| 远程分机 RE + Tandem | 建 | 建 | 建 | 建 |
| SIP 设备 | — | 建 | 建 | 建 |
| 直连速拨号 + 判别器 + ARS | — | — | 部分 | 建 |

关联完还要手工核两处：Entity 判别器逻辑→物理关联、公网接入 COS 区域授权（barring）——自动不等于零手工。编号前缀四则记牢：RE 目录号严禁字母开头；手机设备号用 D、速拨号用 A、Ghost Z 可用 B。

连接模式与 R2.6 分界：

| 场景 | 能力面 |
|---|---|
| 场内/场外 WiFi、3G/4G | Web 服务 + VoIP（全功能） |
| 无数据连接 | 仅 DTMF 回落：打/挂电话、留言、有限路由 |
| Android 无 SIM | 纯 VoIP 话机；代价是回落、私人呼叫、短信三项不可用 |
| R2.6 起 | 远程分机可直接做用户唯一设备（免去永不入服的假主设备，修复离线呼转） |

iPhone+ 推送链路：后台来话走 APNS 推送唤醒（多次 SIP invite 是设计行为）；防火墙放行 TCP 5223/2195/2196/443；SBC 5265 声明；场外 TCP 场景由 kamailio-wasp/wspcfg 缓冲 invite；APNS 证书一年一换（年度 hotfix）。

## 五、交付红线与维护抓手

四条红线：

1. 教材全部域名/公网/口令/号码是实验值，上生产必须整体替换并按安全基线管理
2. 容量数值全书缺位：CAC 无阈值、游牧池无算例、带宽无口径——以 TC2639、8AL90065USAG 或 ALE sizing 工具为准
3. iPhone 完整手工配置书内明示"not part of this lab"，权威依据 TC2639
4. 版本分界别套错：内嵌反代要 OTSBC 7.2+；Nginx 双 conf 要 OT 2.2+；单设备配法要 R2.6+

验证与维护抓手：

| 抓手 | 用途 |
|---|---|
| 拨测预期表 | 模拟器三格式（10/11/13 位）核对落点与主叫显示两个维度 |
| 证书 SAN 核验 | 证书 Details 页确认会议 FQDN 在列 |
| nginx -t | Nginx 配置校验后再启动 |
| ping 会议 FQDN | rehost 后的解析验证 |
| kamailio-wasp/wspcfg 状态与日志 | iPhone+ 推送链路排障（service 命令 + loglevel.sh） |

## 六、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 规划拓扑/选边缘组件/DNS 分离 | otm-dmz-security-channels |
| 定证书方案/签证书/查 SAN | otm-certificate-pki |
| 申报反代与 SBC/DAS/会议 FQDN | otm-ot-server-settings |
| 部署 OTSBC/跑向导/SIP 证书 | otm-otsbc-deployment |
| 装反代（内嵌或 Nginx）/配认证 | otm-reverse-proxy |
| PC 副设备/游牧池 | otm-otc-pc-modes |
| 开通工作手机/自动对象核验 | otm-smartphone-provisioning |
| iPhone 推送/5265/四端口 | otm-iphone-apns |
| 客户端接入/路由档案/手机进会议/虚机部署/拨测 | 路由入口（ot-mobility-remote-worker-router） |

## 版权

- 本精华长文为 ALE Training Services《OpenTouch — 移动与远程办公》（OPENXTE225EN R2.6 Issue 10）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有（Alcatel-Lucent 商标归 Nokia、授权 ALE 使用）。
