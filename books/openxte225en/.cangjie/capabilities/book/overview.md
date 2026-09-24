# Book Overview（参考区）— OpenTouch 移动与远程办公

> 供能力卡引用的背景参考；源自 references.md 落位。

## 部署主线（交付组织轴）

证书先签发 → 服务器侧申报（RP 四 URL → OTSBC 5261/8061 → DAS/ACS 会议）→ 边缘部署（OTSBC → 反代两路线）→ 客户端（PC 两模式 → 智能手机 → iPhone 推送）→ 拨测收口（p47-217；各章讲义+How-To 成对）。反代与 SBC 共处 DMZ，VPN 仅为技术替代（p35）。

## 实验环境（RLAB，仅 Boundary 背景；以下全部为实验口径）

- POD 池相互独立、配置相同；三种学员接入拓扑：教室 RAP（每 POD 至多 2 人）、RAP+物理话机、任意 PC 经 HTTPS 直连（p4-10）。
- 关键虚机地址：OTMS opentouch.company.com=151.1.1.50（SUSE）；OmniVista 8770 nms.company.com=151.1.1.70；OXE csa.company.com=151.1.1.1 / csm.company.com=151.1.1.3；FlexLM flex.company.com=151.1.1.80（CentOS，证书实验兼任自建 CA）；OMS oms.company.com=151.1.1.13；SIP 模拟器 sippublic.company.com=151.1.1.105；Eco-system eco.company.com=151.1.1.100（DNS/Exchange/AD/LDAP/手机 DHCP/CA 六角色）；ACS 会议专用 IP=151.1.1.55（p11-22, p70）。
- 网络分区：公网段 195.128.146.10x（演示域 al-mydemo.com）、DMZ 11.1.1.x（RP=11.1.1.10、OTSBC=11.1.1.20）、内网 151.1.1.x、公共资源 10.20.30.x；NAT 公私 IP 对与端口映射见 p63-66/p90。
- 账号口令总表（p30/p72/p91-92/p245，生产必须全量替换）：OpenTouch SUSE root/superuser；WebAdmin otAdmin/Admin-8770；GUI 12345、TUI 54321；NMC Adminnmc/Superuser1*；OMS letacla1；Eco-system CA 网页 administrator/superuser；OTSBC 初始 Admin/Admin；Nginx 主机 rpuser/Sdfghjk1；AD 用户（alban/adams/adore/barkley/backman/boop）口令 1234；SIP 设备默认口令 0000 必改。
- 编号计划（p23-25）：话机 DHCP 池 151.1.1.151-159（OXE CS）、智能手机池 151.1.1.160-165（Eco-system）；存量用户 31000-31002、新建 31050-31052；副设备 2x31000；OTC PC 副设备 213100x；手机设备号 D21310xx、速拨号 A21310xx、Ghost Z 可 B31091 型；Nomadic 池示例 31017/31018+SIP 设备 31951/31952；RE DISA 前缀 31280；RE DISA 公共号码 +3320131444；ARS 前缀 #0306；ARS Route list MAX ID=3999。
- SIP 模拟器拨测预期（p26-29）：国内 0abcd31xxx（10 位，主叫显示 0298131000）；国内规范 33abcd31xxx（11 位，显示 33298131000）；国际 00ccabcd31xxx（13 位，显示 33298131000）；末四位 31xx 即系统内分机。
- 环境版本坐标（p31/p86/p110/p221/p229/p245）：Ubuntu 16.04.3 LTS（xenial）、ESXi 6.0/6.5、OTSBC/Mediant 7.2、Nginx mainline 源、APNS 根证书（Geotrust）有效至 2022——R2.6 / 2017-2018 时代边界。
- 教学权宜两处：Nginx 安装忽略 GPG 签名告警（p248）；内嵌 RP 无许可先测（p133）——生产不可照搬。

## 平台速览（方案沟通素材）

- 双边缘分工：反代管话音/协作 Web 服务的 HTTPS 会话（拓扑隐藏、认证、URL 封禁、SSL 卸载）；OTSBC 管 SIP 会话与 RTP/SRTP 媒体（DoS、加密、CAC、NAT 穿越、紧急路由）（p37-39, p81）。
- 客户端矩阵口径：OTC PC 需 RP+OTSBC；OTC PC One 仅 RP（N.U.）；OTC Web 仅 RP；OTC WebRTC 与手机端 RP+OTSBC（带 * 仅音频）（p40-42, p82）。
- 端口规划口径：RP 侧公网 443 与 8016（EVS 通知）；OTSBC 侧 5261（OTC）、8061（WebRTC）、5265（iPhone+）、RTP/SRTP 7000-7499（实验口径）（p63-66, p90, p188）。
- 版本分界三处：OTSBC 7.2 起内嵌 RP；OT 2.2 起 Nginx 双 conf 同改（OTES 退场）；R2.6 起远程分机可做用户唯一设备（p128, p253, p204）。
- 容量缺位：CAC 无阈值、并发规模与带宽无口径、游牧池无算例——sizing 外链 TC2639/8AL90065USAG（p81, p157, n30）。

## 教材口径声明

- 全部实验域名/公网/口令/号码仅限实验环境；生产必须整体替换并按客户安全基线管理（原书明文口令遍布正文，引用一律标"实验口径"）。
- 生产化边界四文档：TC2639（远程工作者/移动化总纲与 iPhone 手工配置）、TC2341en（智能手机 VoIP 部署）、8AL90065USAG（OTSBC 配置指南与容量）、TC2257/TC1990（端到端部署）——均为原书指定权威来源；反代模板链接以 TC2639 最新版为准（p220）。
- 原文笔误四处（n29）：Nginx 网关两值（p229 vs p236）、/etc/inid.d/（p250/p254）、otsbx-podx（p156）、https// 缺冒号（p214）——跟书操作按拓扑一致性自校，见 needs-review nr-01~nr-04。
- 历史局限：智能手机章节为 3G/4G/GSM 语境、SEPLOS 假主设备为旧法产物；跨 2022 年的 APNS 根证书续期机制在书外（p182, p183-184）。
