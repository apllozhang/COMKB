# DIGEST — OpenTouch Advanced 精华长文

> 源：OPENXTE301EN Edition 08（468 页，OpenTouch R2.6.1 时代）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 OpenTouch 高级特性交付的全局认知；操作细节按需查 13 张能力卡。

## 一、这套东西是什么

OpenTouch（OT）是 ALE 与 OXE 交换机配套的协作服务器，两者是**分工关系**：OXE 保留呼叫控制和话机生态，OT 承载协作会议、统一消息、移动性（nomadic/智能手机）和目录搜索；客户端有 PC、手机、浏览器三种形态，统一从 OT 拿服务。

整本教材就是一条交付主线：**实验 POD 打底、远程接入打通道、终端侧移动（nomadic/手机）、接企业系统（邮件/目录）、协作会议、最后外部认证收尾**。

三个数字先记住：

| 数字 | 含义 |
|---|---|
| 1 与 1+1 | 每路 nomadic 蜂窝连接占 1 个 Ghost Z，VoIP 连接占 1 个 Ghost Z 加 1 个 SIP 设备——占住直到用户关闭 |
| 5261/8061/7000-7499 | 远程接入的端口骨架：SIP 注册、WebRTC、媒体段，全走 OTSBC |
| R2.6 | 版本分水岭：手机可直接当主设备（此前要永不入服的 SIP 扩展做主机） |

## 二、移动性三件套

- **Nomadic**：Connection 用户专属。激活后办公话机冻结，来话改道——蜂窝模式到任意号码、VoIP 模式到 PC 软话音。核心是资源池：**池规模=最大并发连接数**，且资源挂机也不释放，用完必须关闭。权限成对出现（蜂窝=Nomadic GSM+Desktop，VoIP=Nomadic SIP+Desktop）；资源核查用 OT 服务器上的 tsa_maintenance（选项 20 dump，手动同步走 100→106 2998→7）。
- **OTC 智能手机**：复杂度被"自动创建"消化——关联手机时系统自动建远程扩展、SIP 设备、速拨号、识别码、ARS 路由、Tandem 等 9 类对象，管理员只需核验，外加手工两项（Entity 识别码映射、公网 COS 放行）。iPhone 是特例全家桶：推送走苹果云（TCP 5223/2195/2196/443）、APNS 证书一年一换要装年度 hotfix、出网走 SBC 时 TCP 强制、还要 5265 端口专用 SBC 声明。
- **Extended Mobility**：办公室内贴标签触发——通话切到任意内部话机（**单向不可回切**）或改路由档案；QR 码语法固定（{"v":"1","DI":{"DiD":{"User":"目录号"}}}），NFC 仅 Android 且 OTC 应用必须已启动；每小时弹提醒，再扫一次可停止。
- **Desksharing**：共享工位用"虚拟身份"复用硬件——DSU 无绑定话机（MAC 是系统按号码生成的 aa:bb 虚拟值），凭 600/601 前缀加密码登录登出任意 DSS；OTC PC 可远程释放，UA 软话机替代冻结但仅限内网（WAN 要 VPN）且不支持 Mac。

## 三、通道与企业系统

- **远程接入三件套**：反向代理管数据面（443/8016 四个公共 URL），OTSBC 管 SIP 与媒体（5261 注册、8061 WebRTC、7000-7499 媒体段），DAS 正则管号码格式（最多 20 条串行处理，前一条输出是后一条输入，**顺序错一条全盘错**）。会议邀请专用 FQDN（conf-podX）必须同时进反向代理与 OT 两张证书的 SAN——漏一处必有一侧链接打不开。
- **统一消息**：语音留言变成邮件服务器里的 Wav 文件。四后端能力递减——Exchange 全功能 ≥ O365（Outlook 加载项要 OT 2.5 且仅桌面版）> Gmail（上限 500 用户）> IMAP4（砍 PPR/扩展/MWI/消息类别）。Exchange 侧的钥匙：ICEaccess 特权账号 + Impersonation 授权（R2.3 起，此前用逐邮箱委托）+ CA 证书入信任库；OT 侧建系统、档案、信箱三层。排障先查守护进程 mascd/wireald。
- **目录搜索**：一切搜索查"同步库"——UDAS 把电话簿/内部目录/外部 LDAP 单向倒进 PostgreSQL。同步三参数（日期/时间/周期）不设就是空库，周期永不允许 0。多目录合并成单名片（Single Business Card）：按权重取值、Merge keys 至少姓加名认人；照片优先级 Avatar > LDAP > 本地。OXE 侧 LDAP 溢出按 5 个电话簿做上限（讲义"20 台"口径存疑，见 nr-01）。
- **日历双机制**：presence 是在场旁注文本（不改颜色码、自己看不到自己、FREE 只在名片显示、日程重叠按"外出>忙碌>暂定>异地工作>空闲"取值）；synchro 让 Outlook 与 OTC 双向建会——但 **OTC 建的周期会议不回推 Exchange**。只适用 UM 上下文（本地存储邮箱走 TC2558）；版本门槛 OT R2.3.1 + Exchange 2010/2013/O365 + Outlook 2010/2013。

## 四、协作与安全

- **会议按 ACS 组织**：桥号两侧成对（OXE External Voice Mail 与 OT TUI 每语言一号，实验 31250 英/31260 法）；7 位唯一访问码分领导者与参与者，密码可选且**不进邀请邮件**（音频密码自动套用到录音）；DTMF 控制 ##1/##3/##4（参与者）与 ##91/##92/##93（领导者）。Office 文档演示要装 DCS（Basic 模式只认 pdf 和图片，文档卡 queued 的根因在 Windows 许可与更新）。视频只有内置 AMS（仅 Active talker，无九宫格），Connection 用户做不了点对点与临时视频。
- **外部认证是全局开关**：不能按应用单独启用（IP Touch 话机应用与 TUI 例外）。Downstream 用 LDAP/RADIUS 插件（参数文件+Authentication.xml 启用），Upstream 用 Kerberos 四件套（web.xml 模板对调、krb5.conf、auth.config、ktutil 生成 keytab）加 AD 侧 ice_kerb 账号与两条 SPN。两条保命规则：**启用前管理员必须先配 External login**（否则锁在配置工具外面）；**Kerberos 一开 8770 客户端进不了 WBM**，必须预留一个 AD 出身的 WBM 管理员。级联不对称：外认失败时 Web 客户端回落本地 DTA，厚客户端直接失败——维护窗口要预告。

## 五、关键速查表

远程接入端口总表：

| 面 | 端口 |
|---|---|
| 反向代理（数据面/API/EVS/ACS/DMS） | 443、8016 |
| OTSBC（OTC 注册 / WebRTC） | 5261 / 8061 |
| RTP/sRTP 媒体段 | 7000-7499 |
| ACS SIP 代理（监听/互连） | 5060 / 5260 |
| iPhone+ 专用 SBC | 5265 |
| APNS 推送（通信/通知/反馈/回退） | 5223 / 2195 / 2196 / 443 |

UM 后端对比：

| 后端 | 关键限制 |
|---|---|
| Exchange（本地） | 全功能基线：EWS+MWI+PPR |
| Office 365 | Outlook 加载项/Office 集成要 OT 2.5 且仅桌面版 |
| Gmail | OAuth 2.0 接入；上限 500 个 OT 用户 |
| IMAP4 | 无插件：无 PPR、无扩展、无 MWI、无消息类别 |

认证双轨：

| 轨道 | 协议 | 关键配置 |
|---|---|---|
| Downstream（OT 验证） | LDAP/LDAPS、RADIUS | plugin_*.properties + Authentication.xml；External login 匹配 sAMAccountName/Radius login |
| Upstream（外部先验） | Kerberos、NTLM V2 | web.xml 模板对调 + krb5.conf + auth.config + keytab；AD 账号加两条 SPN |

版本陷阱速记：R2.0 补 DAS 规则 7/8；R2.1 MD1 起 Extended Mobility；R2.3 起 Impersonation；R2.3.1 起 APNS 与日历在场；R2.5 起 O365 加载项；R2.6 手机单设备化。引用任何版本行为必须带章内口径（nr-07）。

## 六、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 配远程接入/证书/DAS | ota-remote-access |
| 配 nomadic/规划 Ghost Z | ota-nomadic-ghost-z |
| 交付智能手机/iPhone 推送 | ota-smartphone-rex |
| 留言进邮箱/选邮件后端 | ota-um-exchange-integration |
| 会议桥/角色权限/密码 | ota-conference-collaboration |
| 日历在场与同步排障 | ota-calendar-sync |
| 目录搜索/名片合并 | ota-directory-udas |
| LDAP/RADIUS/Kerberos | ota-enterprise-authentication |
| 共享工位/扫码切换/DCS/访客入会/实验环境 | 路由入口（opentouch-advanced-router） |

## 版权

- 本精华长文为 ALE Training Services《OpenTouch - Advanced》（OPENXTE301EN Edition 08，含 TC2258 ed.02 附录，© 2019 ALE International）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
