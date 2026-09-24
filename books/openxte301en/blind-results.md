# openxte301en 盲判结果（仅依据能力目录，未读答案）

case-id | slug或none | 理由一句
should-remote-01 | ota-remote-access | 会议邀请链接外网打不开属反向代理公共 URL 与远程接入通道问题
should-remote-02 | ota-remote-access | 远程员工入口的防火墙端口与 NAT/DNS 规划正是该能力主体
should-nomadic-01 | ota-nomadic-ghost-z | 来电转手机且座机不响铃是 Nomadic 双模式标准场景
should-nomadic-02 | ota-nomadic-ghost-z | Ghost Z 池规模=最大并发数是该能力核心规则
should-mobile-01 | ota-smartphone-rex | iPhone 用公司号从 OXE 参数到装 App 的完整交付流程正是该能力
should-mobile-02 | ota-smartphone-rex | 锁屏推送不弹属 APNS 四端口与年度 hotfix 排查范围
should-um-01 | ota-um-exchange-integration | O365 与本地 Exchange 语音留言能力递减对比是 UM 后端选型
should-um-02 | ota-um-exchange-integration | 留言灯与问候语属 UM 语音邮箱档案三层与 mascd/wireald 维护
should-conf-01 | ota-conference-collaboration | 会议桥按语言成对桥号与 One Touch 一键入会属协作会议能力
should-conf-02 | ota-conference-collaboration | 参会人权限与密码不进邀请邮件都是该能力明文规则
should-cal-01 | ota-calendar-sync | 在场颜色不变绿涉及旁注文本与颜色码机制排查
should-cal-02 | ota-calendar-sync | OTC 建的周期会议不回推 Exchange 正是该能力已知边界
should-dir-01 | ota-directory-udas | 目录搜不到先查 UDAS 同步三参数与同步库
should-dir-02 | ota-directory-udas | 合并名片按权重与 Merge keys、照片取 Avatar>LDAP>本地 优先级
should-auth-01 | ota-enterprise-authentication | 域账号登录方案（LDAP/RADIUS/Kerberos）选型与影响评估属企业认证
should-auth-02 | ota-enterprise-authentication | Kerberos 启用后 8770 进不了 WBM 需预留 wbm_admin 补救
should-desk-01 | ota-desksharing | 随便坐登录即用是 DSU/DSS 共享工位机制
should-desk-02 | ota-desksharing | 忙时登录行为对应忙时重置 6004 系统参数
should-em-01 | ota-extended-mobility | 贴二维码扫一扫把通话切到桌面话机正是 QR 呼叫切换
should-em-02 | ota-extended-mobility | NFC 仅 Android、写卡工具与标签型号属该能力
should-dcs-01 | ota-dcs-documents | 文档卡 queued 正是 DCS 未激活或未打更新的典型症状
should-dcs-02 | ota-dcs-documents | 不装 DCS 仅支持 pdf 与图片是 Basic 模式边界
should-web-01 | ota-otc-web-guest | 浏览器免装链接入会正是 OTC Web 访客能力
should-web-02 | ota-otc-web-guest | 访客音频走 PSTN 回呼或 WebRTC 经 OTSBC 是该能力架构
should-lab-01 | ota-lab-pod | POD 虚机清单与 ITSP1 模拟器对接属实验环境能力
should-lab-02 | ota-lab-pod | 3321PN12345 号段与 pbxN 命名是实验环境约定
bait-auth-dir-01 | ota-enterprise-authentication | 问题核心是认证侧 LDAP 要不要一起配，属企业认证能力
bait-em-nomadic-01 | ota-extended-mobility | 手机通话切到桌上话机是贴标签触发呼叫切换场景
bait-nomadic-mobile-01 | ota-nomadic-ghost-z | 转家里固定电话是 Nomadic SIP 设备模式，与配手机 App 无关
bait-web-conf-01 | ota-otc-web-guest | 访客录制诉求要查 OTC Web 能力边界（明示无录制）
bait-cal-version-01 | ota-calendar-sync | 配日历同步前必须过该能力版本门槛（Exchange 2019 不在支持列）
bait-conf-dcs-01 | ota-dcs-documents | 演示文档下载不了是该能力明示的 presentation 不可下载边界
bait-auth-remote-01 | ota-enterprise-authentication | Kerberos 不支持反向代理/远程是该能力明示边界
bait-lab-prod-01 | ota-lab-pod | 实验值不入生产正是该能力使用前提
edge-ldap-01 | ota-directory-udas | LDAP 溢出电话簿参数归目录能力，两数字出入需回书核对（边界）
edge-capacity-01 | ota-nomadic-ghost-z | 100 并发按池规模=最大并发推算 Ghost Z 与 SIP 设备数量
edge-version-01 | ota-smartphone-rex | 无物理话机以手机为主设备涉及 R2.6 单设备化版本门槛（边界）
