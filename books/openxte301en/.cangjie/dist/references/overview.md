# Book Overview（参考区）— OpenTouch Advanced

> 供能力卡引用的背景参考；源自 references.md 落位。

## 交付主线（11 站组织轴）

实验 POD（RLAB）→ Nomadic 移动（蜂窝/VoIP）→ Desksharing → OTC 智能手机 → 远程接入服务器设置 → Extended Mobility → 统一消息 → 目录搜索（UDAS/SBC）→ 协作与会议 → DCS 与日历同步 → 外部认证（LDAP/Kerberos/RADIUS）。实际交付顺序：先打通道（远程接入），再配终端（手机/nomadic），再接企业系统（邮件/目录/认证）（p3-468 章节编排）。

## 实验环境（RLAB，仅 Boundary 背景）

- POD 服务器设置（p9，实验口径）：OXE csa/csm（p9 印作 192.16.8.1.1/.3，疑为 192.168.1.1/.3 变体，见 needs-review nr-04）、OMS 192.168.1.13、OpenTouch 192.168.1.50、8770 192.168.1.70、DCS 192.168.1.31、ECOSYSTEM 192.168.1.100（承载 CA/AD/Exchange）、PC Client 10/11 = 192.168.1.10/.11；掩码 255.255.255.0、网关/DNS 192.168.1.254。
- ITSP1 模拟器（p20-23）：gateway1.itsp1.com（10.20.30.51，pbxP/alcatel，域 sip.itsp1.fr）+ public.itsp1.com（10.20.30.50）；号码段——国内 33[1-5]1PN12345（主号 3321PN12345）、移动 3361/3371PN12345、英国 4421PN12345、紧急 112/15/17/18；DDI 首外线 41000、首内线 31000、范围 500；OXE 侧 Registration ID/Outgoing username=pbxN、First external=33210N41000。
- 实验人物与池：Barkley 31000 / Backman 31001 / Boop 31002；nomadic 池 31017-31019（Ghost Z）与 31951/31952（SIP 设备）；会议桥 31250（EN）/31260（FR）；留言号 31200；DISA 前缀 31280、激活/停用 61/62；速拨 D2131001/A2131001 形态。
- 实验账号口径（p45）：WebAdmin otAdmin/admin8770；CA https://eco.company.com/CertSrv（administrator/superuser）；ICEaccess/iceaccess；Outlook barkley/1234；DCS Administrator/superuser；directory@company.com/directory；ice_kerb 密码 1234；FreeRADIUS shared_secret training；tsa_maintenance 秘密码 2998。
- Extended Mobility 实验前提：学员自带手机、教室 6 SSID 热点（p163）。

## 平台速览（方案沟通素材）

- 分工：OXE 管呼叫控制与话机生态，OT 管协作/消息/移动/目录；客户端三形态 OTC PC/Mobile/Web（p34-79, p323）。
- Nomadic 资源公式：池规模=最大并发连接数——蜂窝 1 Ghost Z/路、VoIP 1 Ghost Z+1 SIP 设备/路，占住至关闭（p47, p51）。
- 远程接入端口：RP 443/8016；OTSBC 5261/8061；RTP 7000-7499；ACS SIP 5060/5260；iPhone+ 5265；APNS 5223/2195/2196/443（p104-107, p296, p102, p98）。
- UM 后端递减：Exchange ≥ O365（OT 2.5+ 才有 Outlook 加载项）> Gmail（500 用户上限）> IMAP4（无 PPR/扩展/MWI/消息类别）（p176-178）。
- 会议：7 位双访问码（领导者/参与者）；DTMF ##1/##3/##4 与 ##91/##92/##93；AMS 仅 Active talker；Connection 用户无 p2p/ad-hoc 视频（p266-271, p273-274）。
- 认证：全局开关双轨（Downstream LDAP/RADIUS、Upstream Kerberos）；Web 失败级联 DTA、厚客户端不级联；启用前先配管理员 External login（p417-431）。

## 教材口径声明

- 全部实验密码/账号/号码/网段仅限实验环境；生产必须替换并纳入安全基线（原书明文密码遍布正文，引用时一律标"实验口径"）。
- 版本碎片化：R2.0/R2.1 MD1/R2.2/R2.3/R2.3.1/R2.5/R2.6 各章各提版本前提；APNS Geotrust 根证书标注"有效期至 2022"——跨版本交付逐章核对并对照最新 release note（needs-review nr-07）。
- 生产化边界五文档：TC2341（智能手机 VoIP 部署）、TC2391（UM 实现）、TC2258（日历在场/同步）、TC2558（本地存储邮箱日历）、TC1623（Kerberos 深入）——均为原书指定权威来源。
- 结构性缺位：容量规划无算例、号码计划仅法国口径、高可用与安全加固缺位——引用能力数字时带话务/版本前提。
