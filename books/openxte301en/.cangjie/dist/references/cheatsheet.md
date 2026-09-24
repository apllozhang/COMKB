# 决策规则速查 — OpenTouch - Advanced (Participant's Guide, Edition 08)

| 能力 | 一句话规则 |
|---|---|
| OpenTouch 远程接入通道与证书 | 反向代理管数据面（443/8016）、OTSBC 管 SIP/媒体（5261/8061/7000-7499）、DAS 正则管号码格式；会议 FQDN 必须进 RP 与 OT 两张证书 SAN |
| Nomadic 移动模式与 Ghost Z 资源池 | 蜂窝每路占 1 个 Ghost Z、VoIP 每路占 1 Ghost Z 加 1 SIP 设备，占住直到关闭；权限成对（GSM/SIP 加 Desktop）；tsa_maintenance 核资源 |
| OTC 智能手机交付全流程（REX/DISA/APNS） | 关联手机即自动建 9 对象（核验即可），手工补 Entity 识别码与 COS 两项；iPhone 特例是 APNS 四端口、年度证书 hotfix 与 5265 专用 SBC |
| 统一消息 UM（Exchange/O365/Gmail/IMAP） | 语音留言存邮件服务器（Wav 单点存储）；四后端能力递减；Exchange 侧钥匙是 ICEaccess 加 Impersonation 加 CA 证书，OT 侧建系统、档案、信箱三层 |
| 协作会议（ACS 配置、角色权限、数据会议） | 桥号两侧成对（每语言一号）、服务器四项设置、三类会议与 7 位双码角色制；密码不进邀请邮件；协作限制两级禁用且 scheduled 不受影响 |
| 日历在场与日历同步（Calendar presence/synchro） | presence 是在场旁注文本（不改颜色码）；synchro 双向同步会议但 OTC 建的周期会议不回推 Exchange；仅 UM 上下文，本地存储走 TC2558 |
| 目录搜索与 Single Business Card（UDAS） | 一切搜索查同步库（单向同步，period≥1 硬规则）；合并按权重与 Merge keys（至少姓加名）；照片 Avatar>LDAP>本地；OXE 侧 LDAP 溢出按 5 个上限 |
| 企业认证集成（LDAP/RADIUS/Kerberos SSO） | 全局开关双轨制——Downstream（LDAP/RADIUS 插件）与 Upstream（Kerberos 四件套）；Web 失败级联回 DTA、厚客户端不级联；启用前管理员必须先配 External login |
| Desksharing 共享工位（DSU/DSS） | DSU 无绑定设备（虚拟 MAC aa:bb 加号码）凭 600/601 加密码用任意 DSS；OTC PC 远程释放要 Desktop 加 Flex Office；UA 替代冻结需 VPN 且不支持 Mac |
| Extended Mobility（QR/NFC 切换与路由修改） | 贴标签触发两动作——通话切到任意内部话机（单向不可回切）与路由档案改写（other and mobile()）；QR 固定 JSON 语法，NFC 仅 Android，一小时周期提醒 |
| DCS 文档转换服务器（Office 会议演示） | Basic 只支持 pdf/图片，Office 演示必须装 DCS（内部 KVM 或外部 VM）；Windows/Office 许可自备，未激活或未打更新即卡 queued |
| OTC Web 与访客入会 | 免安装浏览器端，访客匿名凭访问码入会；数据面走 RP、音频走 PSTN 回呼或 WebRTC（Chrome/Firefox）；无录制/视频/白板/排期 |
| RLAB 实验 POD 与 SIP 运营商模拟器 | 全虚拟化或混合 POD 八台虚机加 ITSP1 模拟器（pbxN 账号、3321PN 号码段、DID 翻译 33210N41000 对 31000）；一切实验值仅限实验 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
