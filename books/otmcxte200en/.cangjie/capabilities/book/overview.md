# Book Overview（参考区）— OpenTouch Message Center Starter

> 供能力卡引用的背景参考；源自 references.md 落位。

## 交付主线（组织轴）

产品认知与形态决策 → 装机（SUSE/core）→ 13 步站点配置 → OXE/OTMC 双向声明与同步 → OXE 侧 SIP 对接 → Connection 用户与语音邮箱交付 → profile 批控与问候语 → SMTP/SMS 通知、IMAP 访问、企业广播三块增值 → 备份恢复与语音信箱统计（p3-258 的 9 讲义章 + 13 How-To 章顺序即实施推荐顺序）。配置管理唯一大脑是 OmniVista 8770；OTMC 自身 WBM 只做辅助。

## 实验环境背景（RLAB 式课堂拓扑，仅 Boundary 背景，p21-32）

- ESXi 单主机（esxi.company.com = 151.1.1.250/24，网关 151.1.1.254）跑六虚机 + 一台 Windows 10 客户端 PC（client = 151.1.1.10）；DNS 域 company.com（DNS/Exchange/AD/LDAP/DHCP 都在 Eco-System 虚机 eco.company.com = 151.1.1.100）。
- 六虚机：OTMC otmc.company.com=151.1.1.60；FlexLM flex.company.com=151.1.1.80；OmniVista 8770 nms.company.com=151.1.1.70；OXE-V（csa=151.1.1.1、csm=151.1.1.3，节点名 oxe）；OMS oms.company.com=151.1.1.13；Eco-System eco.company.com=151.1.1.100。另 gd.company.com=151.1.1.12（书中未展开用途）。
- 口令（实验口径）：SUSE root 默认 letacla1 → 首登强制改 OtmcV01* → 向导 root=letacla1234；maintenance=maintenanceuser；administrator（otAdmin）=Admin-8770；profile（otProfile）=Admin-T1；SNMP=adminsnmp；Eco-System 六用户（alban/adams/adore/barkley/backman/boop）密码均 1234；话机 set secret code 默认 0000；OXE FTP adfexc/adfexc；备份维护示例口令 superuser。
- 业务示例值（实验口径）：Connection 用户 Brad Barkley/Billy Backman/Betty Boop 分机 31000/31001/31002；IP 话机示例分机 61020；DPNSS 前缀 D1234；SMTP=eco.company.com:25（无认证无 TLS）；8770 中 OXE 节点 101、OTMC 节点 98；spadmin 读数 173:1/10、174:1/10、176:1/15、177:4/15、316:1/30、317:2/30。
- OTMC-V 虚机规格（实验口径，p58 Note 明说 only for lab purposes）：SUSE 12 64 位、1 虚拟插槽/4 核/4GB 内存/E1000 网卡/250GB 精简置备磁盘。
- 声明章示例漂移（nr-02）：p92/p94 nslookup 突切 155.1.1.x 网段（DNS 155.1.1.100），且反查 .50 返回 .60——示例仅示意。

## 平台速览（方案沟通素材）

- OTMC 定位：OXE 专属独立语音邮件服务器（含自动话务员能力定义），取代 46xx/8440；访问通道 TUI（任意话机）/GUI（8xx8 与 8088 信封键直达 VVM）/IMAP 客户端（p5-8）。
- 组网：OXE 与 OTMC 直连 SIP trunk 仅一条指向 front node（Bypass 按全部端口）；PRS 链路支撑话机 GUI 显示 5000 并发用户（端口 2570）；VPIM 做 OTMC 互联与三方信箱互通；OXE ABC Supra 不支持集中式 VM（p18-20）。
- 许可：flex-lm 体系，.ice 装 /var/data/licenses；物理机绑 ALUID、虚拟机绑 dongle；向导 OK 不校验有效性，要 lmstat 复核（p35-45, p76-82）。
- 信箱模型：VMS（默认 defaultVmsLS）→ mailbox（必须挂 profile）→ user（分机号与 OXE 对齐 + Voice mail 权）；默认四 profile（p134-152）。
- 通知：外部 SMTP（无认证无 TLS、经 VPIM 路由、Scorpio 处理）；wav 附件/链接/满箱提醒五项 LS 专属；短信须 SMTP-SMS 网关（仅一个）（p167-192）。

## 教材口径声明

- 全部实验密码/账号/网段仅限实验环境；生产必须替换并做安全加固（原书明文密码贯穿全书，引用一律标"实验口径"）。课堂 Network security OFF 与本地备份官方明示不推荐。
- 生产化边界五文档：feature list / product limits（规格与上限）、MyPortal 安装手册 otmc2.6.1_im_InstalManual_8AL90120USAH_1_en（虚机生产参数）、TC1652（空间冗余 SIP 网关）、TC2024（8770 上 NFS）、Quick Reference Guide（问候语细节）——均为原书指定权威来源。
- 书内口径漂移四处 + 拼写漂移一处已在 needs-review 编号（nr-01 节点号 98/99、nr-02 网段 151/155、nr-03 掩码、nr-04 GA wav 路径、nr-06 defaultVmLS/defaultVmsLS）；笔误群见 nr-05。
- 版本口径：OTMC R2.6 / 安装手册 2.6.1 / Issue 08；SUSE Linux Enterprise 12（64 位）；安装模式均标 15000 users、话机 GUI 显示 5000 并发（均为标注口径，生产规格看 product limits）。
