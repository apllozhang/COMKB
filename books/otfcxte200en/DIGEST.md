# DIGEST — OpenTouch Fax Center 精华长文

> 源：OTFCXTE200EN Edition 04（233 页）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 OTFC 传真服务器交付与运维的全局认知；操作细节按需查 11 张能力卡。

## 一、这套东西是什么

OTFC（OpenTouch Fax Center）是 ALE 的**纯软件 FoIP 传真服务器**：装在一台专用 Windows 服务器或虚机上，旁边挨着 OmniPCX Enterprise（OXE）语音网，话路走 SIP/T.38（或 G.711 透传），邮件走 SMTP——硬件无关、无传真板卡。

三个数字先记住：

| 数字 | 含义 |
|---|---|
| 15000 用户 / 30 端口 | 单专用服务器容量上限 |
| T.38 14.4k / G.711 33.8k | 两种传真传输路径的速率口径 |
| 12 项 / 25 / 5360 | FTW 向导动作数、SMTP 网关独占端口、OTFC 本地 SIP UDP 端口 |

整本教材就是一条交付主线：**准备服务器、装软件、FTW 搭最小可用系统、接 OXE 话路、接邮件通道、用户与策略、运维纵深**。

## 二、从裸机到第一份传真

1. **准备服务器**：与用户同域；FQDN 正向解析到 IP、IP 反向解析回 FQDN；IIS 角色带四个角色服务（Windows Authentication、ISAPI Filters、ISAPI Extensions、IIS 6 Metabase Compatibility）

2. **服务账号与 Office**：服务账号六项权限（域服务账号、LDAP 查询、文件夹读写、打印权限、本地管理员、密码永不过期）；装 Office 并预初始化——首次运行不能弹窗，否则传真转换会卡死

3. **装软件**：Setup.exe 选语言（有两项持久副作用：默认邮件通知 Profile 与 Basic Profile 封面语言）、选 IP、Create a new system、传真主机名 + SIP 协议、装全部第三方软件。装完第一件事：停用并禁用 Microsoft SMTP（OTFC 网关同样占 25 端口），再启动 XMSMTPGateway

4. **FTW 向导**：12 项动作一次搭出最小可用系统——建站点、站点 QOS 0/0/240、XML Poll 文件夹、默认 Profile 去 SMTP 认证、CSID=站点名、建首用户、Postmaster、站点/系统路由表、告警通知、Mail Relay、产出摘要存盘。跳过向导可事后跑 FirstTimeSetup.exe 或逐项手工配

5. **许可**：首装自带评估许可——每组件 1 实例、共 2 通道、10 站点、100 用户、每页水印。测试时"怎么每页都有水印/并发就 2 路"是许可边界，验收前必须找经销商（提供服务器 MAC 地址）买许可并手工导入

## 三、两大外部集成（缺一不可收发）

- **OXE 话路**：OTFC 侧本地 SIP UDP 5360 + 声明 OXE + Dial Plan（单 PBX 默认 * 全路由；空间冗余在 Peer List 声明两台呼叫服务器并排优先级）。OXE 侧 MGR 七步菜单（Trunk groups、SIP gateway、Proxy、Trusted IP、SIP Ext gateway、Network Routing Table、Prefix plan）——只是骨架，参数一律参照 TC3048。排障三法：CHtrace（tuner/actdbg/mtracer）、SIP trace（motortrace/traced）、tcpdump 转 Wireshark，均在 OXE 的 mtcl 账号下执行。
- **邮件通道**：SMTP 网关监听 25 收传真作业、发通知，feedback address 不能为空，同机不能有别的 SMTP 服务。官方强烈建议前置真实邮件服务器（队列管理/Outlook 表单/反垃圾/防病毒）。Exchange 集成建 'FAX' 地址空间 Send Connector（fax:*;1 指向网关智能主机，许可特性）；通知一封不到先查 feedback address 与 Receive Connector。寻址：31600@传真服务器 FQDN、[FAX:号码]、Outlook 联系人直选。

## 四、人与策略

- **用户**：恒以 SMTP 地址标识，必须绑 Site + Profile 才能用系统；内部库与 AD 双源可共存（FTW 只给两个选项，别理解成二选一）；CSV 批量导入导出只在 Webadmin 有。时区写进传真报头，影响封页/报头/邮件通知三处时间戳。
- **管理员**：System 管全局、Site 管自己的站点；认证可用 SMTP 地址或 Windows 认证（SSO/SAML）；官方推荐建备份管理员防锁死。
- **Profile 是策略中枢**：六块属性（信息/封页/计费码/传真选项/安全/通知）挂五类机制——出方向 Restriction group（如"仅国内禁国际"）、入方向站点级呼号限制、每语言一份的邮件通知 Profile（Exchange 场景勾 Exchange integration + Text，只影响邮件不影响 Web）、公共电话簿与封页都经 Profile 下发。
- **目录与路由（大客户）**：LDAP 声明（389/Search base/属性映射）→ Site/Profile Lookup 两张 if 规则表（没配 = 外部用户用不了）→ NT Account 免密两路（专用接口或 samAccountName 过滤器 + IIS 禁匿名）。来传真路由三类规则（Default 兜底恒最后，$did:?????$ 匹配被叫）；DTMF 补拨（+33155667000 P 1234）；Modification Table 规整号码（33 开头换 00）；OXE 话单交 OmniVista 8770 出计费报表（默认映射传真号）。

## 五、运维纵深

- **服务架构**：模块 → 服务（Windows 服务）→ 组件；9 个服务分有状态复制（FaxManager/ConfigManager/CoConfig/FaxArchive/FaultTolerance）与无状态负载均衡（Driver/Rasterizer/SMTP/XML Gateway）。查状态走 Services Status，脚本走 xmsc -ra/-oa/-aa。
- **日志**：每组件一个专属日志，统一在 FaxCenter\Trace，默认单文件 20MB、归档保留 15 天，满后 zip 入 Archive；来传真通知/路由问题先看 ConfigManager.log 与 Smtp.log。
- **备份/升级**：冷备三数据域（注册表键 + Data/Bin/Config + MySQL；MediaStore 图像含在 Data 内）；备份停服"不可 kill"、恢复"可 kill"；恢复四前提（版本等同/拓扑一致/路径一致/先擦除）。升级五步法：确认健康、停流量、停服务、备份、升级；CompanyConfig/XmediusArchive 两库不在升级自动备份内，xmedius.war 会被整包替换。
- **合规与监控**：传真记录（元数据）与传真文档（MediaStore 图像）可分开/一起删，支持零保留；31 个报表可用 BIRT 自定义（装在安装包 3rd\birt）；SNMP V2 trap 覆盖队列满、配额满、光栅化失败、路由失败、LDAP 断连等十余类。

## 六、交付红线

三条红线：

1. 教材密码/账号/网段（Alcatel1!@123、123456、mtcl、192.168.1.x）全是实验值，上生产必须换
2. 端口全表、45 格式、浏览器支持、服务器资源数值都在书外——以 OTFC Features List 为准（书内五处强调）
3. OXE 侧只有 MGR 菜单骨架，参数以 TC3048 为准；无 TC3048 不上站

## 七、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 装系统/跑 FTW/许可水印 | otfax-installation-ftw |
| 接 OXE/话路排障/抓包 | otfax-sip-channel-integration |
| 邮件发传真/Exchange 连接器/通知不到 | otfax-mail-exchange-integration |
| 开户/批量导入/建管理员 | otfax-user-administration |
| 禁国际号/通知格式/电话簿 | otfax-profile-policy |
| 接 AD/免密/路由表/DTMF/计费 | otfax-directory-routing |
| 重启服务/看日志/SIP 日志 | otfax-services-operations |
| 备份/恢复/升级/零保留 | otfax-backup-upgrade |
| 装客户端/做封页/队列状态 | 路由入口（ot-fax-center-router） |
| 选型容量/拓扑/合规应答 | 路由入口（ot-fax-center-router） |
| 报表/BIRT/SNMP 告警 | 路由入口（ot-fax-center-router） |

## 版权

- 本精华长文为 ALE Training Services《OpenTouch Fax Center - R9.2 Starter》（OTFCXTE200EN Edition 04）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
