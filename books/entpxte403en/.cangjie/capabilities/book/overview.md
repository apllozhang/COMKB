# Book Overview（参考区）— OmniPCX Enterprise SIP

> 供能力卡引用的背景参考；源自 references.md 落位。

## 交付主线（组织轴）

环境与外线地基 → SIP 协议与 OXE 六组件 → 终端三条开通线（SIP Device/话机/ALES）→ DM 与证书 → 编解码与排障 → 出口两域（SBC 运营商 + 远程办公）（p3-458 章节推进）。生产交付顺序同此轴。

## 实验环境（RLAB，仅 Boundary 背景）

- POD 拓扑（全虚拟化）：LAN 192.168.1.x / DMZ 192.168.2.x / 公共区 10.20.30.x；OXE CSA 192.168.1.1（物理）/192.168.1.3（主用）、OMS 192.168.1.13、SBC 192.168.1.105/192.168.2.205、ITServer 192.168.1.252（NTP+LDAP）、内部 DNS 192.168.1.250、外部 DNS 10.20.30.250、FlexLM 192.168.1.80、远程虚机 podP-outside 10.20.30.2P（p5-11）。
- 混合模式另加：POE 交换机 192.168.1.12（GD4）下挂 ALE-500/300/20h/30h 物理话机；不需要 PC CLIENT 11；SBC 虚机延后启动（p14-19, p36-37）。
- ITSP1（直连）：gateway1.itsp1.com 10.20.30.51 + public.itsp1.com 10.20.30.50，账号 pbxP/alcatel；ITSP2（经 SBC）：gateway.itsp2.com 10.20.30.60，账号 podP/alcatel（p21-34）。
- 实验账号口径：mtcl/swinst/root=Superuser2580*；SBC=Admin/Admin；SIP 密码 12345；ALES 同密 alcatel；auto-discovery 0000；话机菜单 123456；本地认证 Superuser1245*、首连改 Administrator2580!（p9 等多处，全部实验口径）。
- 实验分机：31000/31001 IPDSP；31030 eevans、31031 eeastwood、31032 eelkins、31033 ALE-2/3、31034 ALE-300、31035 ALES-mobile、31060 MicroSIP（SIP Device）；话机池 192.168.1.161-164。

## 关键数字速览（方案沟通素材）

- 软件锁三把：177（SIP 用户总数）/345（仅 SEPLOS）/430（仅 ALE-S）；容量六维上限与 15000 用户/20000 设备（p67-68）。
- SIP 中继组：2 接入=62 通道，单组上限 992 TS（32×31）；改接入数必须重启（p86/p363）。
- 注册租期 1800-86400s；隔离 3s/50 条/1800s；订阅 1800/86400s（p86-88）。
- 密码策略（ALES 本地认证）：≥14 位、2 字母含 1 大写、2 数字、1 特殊、禁 4 连、不与前 5 次重复（p114）。
- 监督 30000 键/节点、40 键/监督员，事件码 510-513（p130/p133）；按名呼叫 48 条/16 并发（p125）。
- 编解码高带宽序：OPUS SWB > OPUS WB > G.722 > G.711 > OPUS NB > G.729（p281）。
- 反代规模：≤500 远程用户用 OTSBC 内嵌 RP（p387）；远程 SIP 接口 TLS 5261、媒体 6000-6399（p438-440）。
- EDS 零接触 四限制：无出向 HTTP 代理、无 802.1x、无 VLAN、暂无 Wi-Fi（p404）。

## 教材口径声明

- 全部实验密码/账号/网段/号码仅限实验环境；生产必须替换并做安全加固（原书明文密码遍布正文，引用一律标"实验口径"，n50）。
- 生产化边界文档：TC2005 与运营商附加文档（外线参数）、TC2957（ALES Remote Worker）、EDS user manual（零接触）、Server deployment Guide for Remote workers（VPN 网关清单）、OXE Features List（功能矩阵终审）——均为原书指定权威来源。
- 版本敏感点：SSH 强制自 N3、远程加密放行自 N4、mTLS 8443 自 R101.1、OpenSSL 安全级 2 自 R101.0、双栈出厂自 R200；全书截图混 R100.0/R101.0/R101.1 多版本（nr-07），跨版本先核对现场版本。
