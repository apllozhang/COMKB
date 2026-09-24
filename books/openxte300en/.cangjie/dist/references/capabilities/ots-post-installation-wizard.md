# OTMS 初始化向导（Post-installation wizard 两模式十节）

## R — 原文依据

> "The post-installation proposes two modes: Installation from scratch or From an existing archive"（p89）
> "ALL PASSWORDS ON THIS PAGE MUST CONTAIN AT LEAST 8 CHARACTERS. THERE IS NO ERROR POP-UP IN CASE YOU USE LESS THAN 8 CHARACTERS BUT YOU WILL FACE PROBLEMS AFTERWARDS."（p95）
> "THE DNS MUST BE CONFIGURED TO RESOLVE (FORWARD AND REVERSE RESOLUTION): • OPENTOUCH SERVER FQDN • OMNIVISTA 8770 SERVER FDQN • MAIL SERVER FDQN • LDAP SERVER FDQN • ... CALL SERVER FQDN"（p93）
> "HIGH AVAILABILITY IS NOT MORE SUPPORTED FOR A NEW INSTALLATION DON'T ENABLE IT. KEEP DISABLE."（p94）
> "THE OK STATUS INDICATES THAT THE LOCAL FILE IS PRESENT. BUT THE CONTENT (VALIDITY) OF THE FILE IS NOT CONTROLLED."（p101）

出处：OPENXTE300EN p88-108。

## I — 自述

向导是 OT 服务器软件装完、首次开机自动启动的站点安装（site installation）正式入口，不是可选步骤。两种入口：

- **from scratch**：全新初始化，按十节顺序走完，Finish 后向导启动 OT 服务。
- **restore from archive**：用备份归档重装或迁移；只填归档目录、键盘、root 与维护账号，许可可借机替换；归档里的旧许可会一并恢复。

from scratch 十节与硬规则：

| 节 | 配置内容 | 关键硬规则 |
|---|---|---|
| 1.1 Local settings | 键盘/国家/公司/时区+DST | 按现场 |
| 1.2 Network settings | 主机名/IP/掩码/网关/域/DNS/NTP | 主机名小写强制；五类 FQDN 正反向解析齐 |
| 1.3 High availability | HA 开关 | 新装机必须保持 Disable |
| 1.4 Core/Host accounts | root 与维护账号 otuser | 口令至少 8 字符且无报错弹窗；用户名互不相同 |
| 1.5 OT accounts | otAdmin/otProfile/SNMP | 口令另需大写+数字+特殊字符；当场抄录 |
| 1.6 ACS | Stack name 与 Node ID | Conferencing Service Address 保持 No |
| 1.7 Licenses | FlexLM 本地/外部 + .ice | OK 状态只代表文件在；可 Skip 但系统不正常 |
| 1.8 Certificate | ON（Internal SHA256 或外部 PKCS12）或 OFF | OFF 为全球同款通用证书，官方不推荐 |
| 1.9 Backup configuration | 本地/USB/NFS 备份目的地 | 客户决策项 |
| 1.10 Summary + System update | 核对；无补丁选 NO | Finish 后 OT 服务启动 |

口令页四条铁律：全部口令至少 8 字符（短了不报错、事后出问题）；用户名不得用 admin/adminnmc/htuser 等既有名；otAdmin/otProfile 口令有复杂度要求；全部账号口令必须当场抄录——8770 声明 OT 节点时逐项要用。

## A1 — 书中案例

**from scratch 实验**（p88-105，实验口径见 B）：

1. OT 首次开机向导自动启动，选 Installation from scratch。
2. Local settings 按现场填键盘、国家、公司、时区并勾 D.S.T.。
3. Network settings 填主机名小写、IP、掩码、网关、域、DNS 与 NTP。
4. 对照 DNS 清单核五类 FQDN 正反向解析，缺则先补 DNS。
5. High availability 保持 Disable 直接下一步。
6. Host accounts 填 root 与维护账号，口令至少 8 字符。
7. OT accounts 填 otAdmin、otProfile 与 SNMP 口令并当场抄录。
8. ACS 填 Stack name 与 Node ID，Conferencing Service Address 保持 No。
9. Licenses 选 Local 或 External 后 Browse 选 .ice 文件。
10. Certificate 选 ON（Internal SHA256 或外部 PKCS12）。
11. Backup 填 NFS 目的地；Summary 核对后 System Update 选 NO。
12. Finish 后向导启动 OT 服务，SSH 横幅可核版本。

## A2 — 未来触发

使用情境：新装 OTMS 后首次开机；用备份归档重装或搬迁迁移；向导口令随手填短了事后出问题；客户问 HA 要不要开；向导许可页显示 OK 不放心。

语言信号：post-installation wizard / 站点安装 / from scratch / restore / archive / 归档恢复 / HA / DNS 正反向 / otAdmin / otProfile / otuser / bics.conf / security off / 初始化向导。

与相邻能力区分：软件还没装走 SOT 装机（路由卡）；许可装后核查与外部 FlexLM 属许可能力；8770 声明 OT 用这套账号，见节点声明与 SIP 能力。

## E — 可执行步骤

输入契约：已装完软件待初始化的 OT 服务器；客户网络参数（IP/域名/DNS/NTP）；许可 .ice 与锚定物（物理机 ALUID、虚拟机加密狗）；证书档位与备份目的地两项客户决策。缺许可 → 可 Skip 进系统，但必须立即排补装计划。

1. 前置核查：五类 FQDN 正反向解析全通、NTP 可达、许可文件在手。完成标准：nslookup 双向全通
2. 开机进向导，新装选 from scratch，重装迁移选 restore from archive 并指定归档目录
3. 依次完成本机、网络、HA、账户四节，账户口令当场抄录留档。完成标准：口令全部至少 8 字符且记录在案
4. ACS、许可、证书、备份四节按设计填写。完成标准：Summary 各项与设计一致
5. Finish 并核服务：SSH 登录横幅显示 OTMS 版本号。完成标准：OT 服务已启动

判停点：

- 向导许可页 OK 不代表内容有效 → 装完必须用 checkLicensing.sh 与 spadmin 复核（转许可能力）
- 许可缺失点了 Skip → 系统不会正常工作，立即排手工补装
- 怀疑口令当时填短 → 静默陷阱（无报错），尽早改密并把账号表补全
- 客户要求新装机开 HA → 本版本无路径（仅 R2.2.x 迁移保留），转方案与商务讨论
- restore 路径发现旧许可不适用 → 向导许可页借机换新 .ice

输出契约：服务已启动的 OT 服务器 + 账户口令清单（供 8770 声明与交接）+ 证书/备份目的地决策记录。

## B — 边界

- 实验口径（生产必须替换）：root=superuser、otuser=maintenanceuser、otAdmin 口令 Admin-8770、otProfile 口令 Admin-T1、SNMP=adminsnmp；OT 地址 192.168.1.50、备份 NFS 10.20.30.40 的 /mnt/db/backup/podX。
- 本地 DNS 服务器仅在 OXE 未做 duplication 时可用；NTP 需确认防火墙放行，事后可用 ot-config.sh --ntp 修改（p93）。
- 证书三路线细节与 Windows CA 全流程在证书路由卡；本卡只取向导内决策。
- 加密狗挂载（虚拟化场景）属许可域：vSphere 给承载 FlexLM 的虚机加 USB 控制器与 Aladdin USB Device；R-Lab 锚 MAC 无需（n10）。
- UM 语音邮件声明、VPN-less 会议地址属书外专项培训（n39）；向导 ACS 节该问保持 No 即可。
