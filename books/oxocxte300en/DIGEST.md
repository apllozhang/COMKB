# DIGEST — OXO Connect Starter 交付精华长文

> 源：OXOCXTE300EN Edition 16（472 页）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立对一台 OXO Connect 从开箱到投产的全局认知；操作细节按需查 12 张能力卡。

## 一、这套东西是什么

OXO Connect 是 ALE 面向 **≤300 用户企业与酒店** 的通信套件家族（R6.3 / OpenTouch Suite for SMB 口径）：一条线是 OXO Connect Evolution（OCE，IPBox 盒子，纯 IP），另一条是 Compact/Small/Large 三档 PowerCPU EE 机箱（混合 TDM/IP）。

它既能纯现场交付，也能接入 Rainbow 做混合云。整本教材就是一条交付主线：**数据采集、系统开通（FTR 上云或 OMC 现场）、终端开通、编号/组/用户/信箱、SIP 中继与站点业务、备份升级复位与安全、Rainbow 接入**。

四个数字先记住：

| 数字 | 含义 |
|---|---|
| ≤300 用户 | 产品定位上限；超出转其他产品线 |
| 16/48/60/76 | PowerCPU EE 的 DSP 通道四档（无子板/Armada32/Armada64 两配比） |
| 192.168.92.246 / 192.168.94.246 | 出厂 OMC 首连地址 / OCE ETH1 服务口地址（实验口径） |
| 20 / 50 | Rainbow WebRTC 网关通话上限（集成与 FE / 外部拓扑） |

## 二、开通：先岔路再进场

- **Cloud Connect 路线**：开箱接 LAN 即插即用，自动连云、软件与许可自动下载、Fleet Dashboard 远程管理。OCE 的入场口是 **FTR**：PC 接 ETH1（固定 192.168.94.246、自带 DHCP），浏览器 Register，installer/pbxk1064（仅首连）登录、强制改密，填 IP 五项与三参考值提交 → 注册入云、许可下载、远程可达。
- **Standard 路线**：装 OMC，出厂 IP 192.168.92.246 Expert 首连 + 服务器认证，证书装进受信任的根（之后不再弹告警），上传软件，导入两把许可（.msl 主钥匙+.csl CTI 钥匙，与主 CPU 序列号绑定），七账户改密（每客户必不同），录客户信息。
- **IP 修改是连锁动作**：OMC 四页签（Boards/LAN/DNS/DHCP）→ 重启 OXO → PC 同步改址。改完不重启"看着改了没生效"是高频误会。
- **初始安装向导**：只在初始状态（首启或冷复位后）可跑；Business/Hotel 模式唯一入口在向导第一步——酒店项目模式决策必须前置。

## 三、业务配置四件套

1. **编号计划**：四层（公共/专用/内部/会话中），Base 做内外映射（DDI 41100 base 100 ↔ 分机 100），取值域 0-2199；建新段先删冲突旧段。组号红线：**hunt group 500 被语音信箱服务器占用，从 501 起用**。
2. **四种组**：hunt（Sequential/Circular/Parallel 三种分发）、pick-up（代接键作用域选 Group）、broadcast（接收方必须有扬声器）、manager/secretary（双方必须 multiline 话机）。
3. **用户功能**：键三类（呼叫/功能/资源）；动态路由两级两计时（上限 3276 秒、级联 5 级、apply diversion 是一切转移的总开关）；插入/外转必须 Feature Rights 放行加键/前缀配置两段齐全。语音信箱三态双模，录音默认 30 天删除、General 信箱密码=话务员密码。
4. **站点话务**：呼入靠话务台组（恒并行）+ 时段表（End=下一行 Start）+ Normal/Restricted 双 DDI 计划；预公告三模式。呼出是**矩阵不是清单**：Traffic sharing（能否占中继组）、Barring（用哪张闭锁表）、闭锁表（6 张=6 级，00 国际默认禁）。
5. **默认 LC=12 意味着默认全员禁外呼**，授权靠改用户 LC。关键坑：默认用户不跟随时段，要逐话机关 Inhibition Time-ranges，否则限呼不生效。

## 四、公共 SIP 中继（配置项最多的一章）

周边四项（LAN 网关/安装号/DDI/VoIP 接入与中继组）+ 网关九页签（General/DNS/Domain Proxy/Registration/Media/Identity/Protocol/Topology/Security）。两处顺序依赖最容易断链：

| 顺序 | 内容 |
|---|---|
| DNS → Domain Proxy | 先填 DNS A，IP 类型才变 dynamic，才能配 Outbound Proxy |
| 建网关 → 回填 Gateway index | 网关建好后必须回 List of Accesses 关联，漏回填=不注册不呼出 |

验收判据：OMC History Table 显示 **SIP registration success**。Media 带宽=并发资源，低于并发会拒呼。

并发口径：IPBox 120、PowerCPU EE+Armada64 至 76。提速路径：过 TSS 认证的运营商用 Profile 导入（TC1994）或 Easy Connect。生产红线：实验跳过了短号与紧急号——上生产必须按国家补 ARS（合规级风险）。

## 五、运维三板斧与安全一条线

- **备份四线**：自动周期备份（Date & Time Data Saving）、OMC 手动 .cdb（Read all → Save As → Backup/Store，恢复走 Auto-Connect for Restore）、OCE SD 卡（AES 256、恢复仅同主版本、卡 2-32GB/EXT2）、DBAdapter 跨版本透明迁移。
- **升级**：系统同时保留双版本（active+replacement）；MyPortal 下三件套（PBX 软件+配套 OMC+技术通函）；Swap 排程执行；回退用 switchover。
- **复位三档**：Warm 重启不丢库；Cold 回默认但不勾子选项时保留 installer 密码/网络/管理旗标/Cloud Connect 参数；Factory 再删系统日志。"Cold=全清"是误解——转手清机要勾全子选项或 Factory。
- **安全一条线**：密码三句常识（非默认/常改/不简单不短），管理密码 8 位含大小写与数字；R10.1 前旧默认密码表已弃用；盗打目标是客户钱包（一周末可损失 2 万欧以上）；生产加固强制 **TC1143** 最新版。

## 六、Rainbow 混合云速览（深入转姊妹技能）

- 接入：PBXID+激活码填入 OMC/Cloud/Rainbow，域名保持 openrainbow.com 不动；验收判据 **connected with final password**（Webdiag），日志 ccrbagent.log。
- RCC 中间态：分机关联后仅监督话机（接/挂/保持/转），**音频全在话机**——无网关时的正常形态，不是故障。
- 网关四拓扑功能等价、容量有别：集成（R3.2+/20 通话/免 SIP trunk 许可）、OCE-FE（双端 ≥R4.0 MD/20）、外部 NUC 或 ESXi（50）；自动配置 R4.0.020.002 起且仅 Reseller 管理员可激活。

容量查表（用户数 → 外部/集成通道 → 集成拓扑用户数，p392）：

| 用户数 | 外部/集成通道 | 集成拓扑用户 |
|---|---|---|
| 5 | 5/5 | 5 |
| 20 | 11/11 | 20 |
| 50 | 20/20 | 50 |
| 70 | 27/NA | 70(*) |
| 150 | 50/NA | 150(*) |

70 以上集成列为 NA——20 通道撑不住中高话务；(*) 行是方向性参考，引用必须带话务前提。

终端形态决定许可：有话机=Multiset（物理主站+Twinset 副站，R6.0 起 1 UTL）；纯软话机=Anydevice（1 UTL）；R5.2 及以前副站用 Anydevice——照旧文档建副站会白占许可。

## 七、交付红线

1. 教材全部密码/账号/网段/ARI 是实验值（pbxk1064、Alcatel1、alcatel、admin/admin、0000……），上生产必须换
2. 生产化依据在书外五份文档：TC1143（安全）、TC1284（SIP 运营商）、TC1994（SIP Profile）、TC2479（Rainbow 网关）、Rainbow WebRTC cookbook（OCE-FE 开局，必须最新版）
3. Auto-Provision 忘开是终端不上线第一原因；改 IP/DHCP 后必须 warm reset；"限呼不生效"先查 Inhibition Time-ranges

## 八、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 开工前采集/安装数据表 | oxos-data-collection |
| FTR 上云/装 OMC/改 IP/进 Hotel | oxos-commissioning |
| 话机/DECT/模拟设备开通 | oxos-terminals |
| 编号计划/四种组 | oxos-numbering-groups |
| 用户按键/前转/信箱 | oxos-user-features |
| SIP 中继配置与排障 | oxos-sip-trunk |
| 日夜切换/出局权限/闭锁 | oxos-incoming-barring |
| 备份/升级/复位 | oxos-maintenance |
| 硬件选型/消息彩铃/安全/接 Rainbow | 路由入口（oxo-connect-starter-router） |

## 版权

- 本精华长文为 ALE Training Services《OXO Connect Starter》（OXOCXTE300EN Edition 16）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
