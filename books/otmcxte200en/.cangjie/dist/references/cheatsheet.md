# 决策规则速查 — OpenTouch Message Center Starter (Participant's Guide, Issue 08)

| 能力 | 一句话规则 |
|---|---|
| OTMC 服务器安装与站点配置 | 三种 SUSE 安装模式 + CheckSystemLinux.sh/setup.bin + 首启 13 步向导；DNS 前向反向七类 FQDN、密码 ≥8 不弹错、虚拟环境备份必须外置 NFS |
| FlexLM 许可证体系部署与更换 | .ice 装 $LICENSES_HOME + flexlmd 重启 + lmstat 核验；物理机绑 ALUID、虚拟机绑 dongle（挂到承载 FlexLM 的虚机） |
| OXE/OTMC 双向声明进 8770 与同步 | OXE 准备（netadmin/4400 Synchro）后 8770 三层树声明双节点；OXE 节点号=ABC×100+节点号、OTMC 自由号不撞车；同步按 complete/partial × separate/global 矩阵选 |
| OXE 侧 SIP 对接 OTMC | 四段参数——trunk group（T2/ABC-F/SIP）、external gateway（5040/TCP/ICE type）、trusted 含 OTMC IP、全局 G.729+DPNSS 前缀+Routing Optimisation |
| Connection 用户与语音邮箱交付 | OXE 侧建户与话机寻址（resurrection/空闲地址/IP 静态）+ 许可三族核查；OTMC 侧三级对象 VMS → mailbox（必挂 profile）→ user（分机号对齐 + Voice mail 权） |
| 语音邮箱 profile 定制与问候语管理 | 默认四 profile（Advanced/Classic/Simplified=LS、Standard=UM）三页签批控行为/时长/容量；问候语四类经 Greeting Managers 集中管理 |
| SMTP/SMS 通知部署与排障 | 留言落箱经 Scorpio 发外部 SMTP（无认证无 TLS、VPIM 路由）或 SMTP-SMS 网关（仅一个）；附件/满箱提醒等五项 LS 专属；退信与 SNMP trap 是仅有的失败信号 |
| OpenTouch 备份恢复与语音信箱统计 | 8770 发起两段式备份（SSH/SFTP），恢复后必须手工 service opentouchd start；统计走 statistics.properties + 手工建目录 + mascd 重启，输出 XML/HTML/CSV |
| OTMC 产品定位与部署形态 | 单服务器独立信箱三通道（TUI/GUI/IMAP）；物理（ALUID）与 OTMC-V（dongle、vMotion/DRS 白名单）；15000/5000 规模口径；Supra 不支持集中式 VM |
| 用户自助门户 My Profile 与 MyMessaging | My Profile（FQDN 根路径）管语言/问候/密码/通知，MyMessaging（FQDN/MyMessaging）网页听留言；可见项受管理员授权 |
| IMAP 客户端访问语音邮箱 | OTMC 即 IMAP 服务器（默认 IMAPS+TLS）；客户端/服务端/判据三处对齐，IMAP 登录测试 Completed 才算，发信测试失败属预期 |
| 企业广播 General Announcement | 三类播报场景（AA 项废弃）+ 管理员授权 + TUI 菜单 6 或 general_announcement.wav（CCITT A-law 8bits 8kHz mono）；单条、覆盖、≤5 分钟 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
