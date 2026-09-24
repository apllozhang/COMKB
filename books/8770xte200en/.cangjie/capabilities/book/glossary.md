# GLOSSARY — OmniVista 8770 安装与网络管理 术语表

> 阶段 3 产出（源：candidates/glossary.md，60 条全量见候选底稿；此处门户版精选高频 30 条）。
> 口径：定义只采信本书正文；PCX/MAO 等缩写书中未给全称，如实标注（needs-review nr-04）；实验口径值一律标"实验口径"。

# OmniVista 8770 (8770XTE200EN Ed47) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（705 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniVista 8770 | 8770 集中网络管理平台 | 单台专用 Windows 服务器承载应用套件，经 thick client 与 WBM 轻客户端统一管理 OXE/OXO Connect/OpenTouch 的配置、用户、告警、报表、备份 | p5-6, p55 |
| Network / Subnetwork / PCX | 配置树三级 | Configuration 应用的被管对象树：网络号自由编、子网号须等于 OXE 网络号、节点声明是同步告警备份的组织主键 | p111, p121-123 |
| Declaration node（节点号公式） | 声明节点号 | OXE：网络号×100+节点号（例 101）；OXO Connect：(子网号×100)+OXO 节点号（例 1x100+80=180），备份目录随声明节点落盘 | p112, p123, p658 |
| Synchronization | 同步 | Complete 全量/Partial 增量（五类条目：Users/Directory/Data terminals/Speed dial/Remote users）× Separate 单节点/Global 连带 OpenTouch | p114, p125 |
| Real Time Synchronization | 实时同步 | OXE 侧对象变更经事件实时回传 8770；失效时重启 NMC Alarm server 服务（自动重启） | p127-128 |
| Profile | OXE 用户档案 | OXE 侧 Set Function=Profile 的特殊用户；生效前提 System Parameters 勾 Use profile with auto. recognition，名称必须大写 | p183-186 |
| Meta profile | 元档案 | 8770 侧建户模板：名+节点+空闲号段+设备类型+OXE profile（可选）；建户只填姓名自动取段内首个空闲号；号段建后必须同步 | p198-207 |
| Key profile | 键位档案 | set profile > Progr. Keys > Profile Features 三层；建户选 Key Profiles 自动配键；取回 8770 需同步 | p190-195 |
| Correlated / Uncorrelated alarm | 相关/非相关告警 | PCX 能检测问题结束的相关告警自动清除且是 Topology 唯一显示类型；非相关告警须人工清除 | p277, p327 |
| Event | 事件 | 对象创建/删除/修改通知，无严重级，是实时同步的载体 | p275, p127 |
| Job / Task / jobset | 任务模型 | Task=可执行操作；Job=同时执行的任务集合（Idle/Waiting/Running）；新建子 job 临时叫 jobset，刷新后变 Job | p463-464, p487 |
| RestoreContext.ini | 安装设置存档 | 目录/端口/计算机名/DNS 后缀/成本中心/版本（nmcVersion）的存档；恢复时比对（rehosting 排除 svNMCName/svDomain） | p79, p509-512 |
| Rehosting | 换址恢复 | 改 IP=备份>改 IP>rehosting 恢复；改 FQDN 同机=卸载重装；换机=新机同参数安装>rehosting 恢复 | p511-513 |
| MIB / Object Model | 对象模型 | 8770 与 OXE 间 CMISE 数据交换的对象描述库；Access Profile 变更后须删客户端本地 MIB 重载 | p139-140, p402 |
| MAO | OXE 管理操作体系（全称未展开） | Configuration 界面对 OXE 的增删改即 mao action，审计落 /usr3/mao/ 三日志 | p412, p427-428 |

## 二、角色与账户域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| AdminNmc | 应用管理员主账号 | 全应用全权预定义账户；锁定须经 ToolsOmniVista 选项 4 或 WBM 邮件重置解锁 | p74, p372, p390 |
| directory manager | LDAP 目录管理器 | 登录名固定不可改（改名安装失败）；ToolsOmniVista/DirManag 的认证主体 | p74, p77, p535 |
| mtcl / adfexc / swinst | OXE 三大系统账户 | 维护会话 / FTP 数据提取 / 软件安装恢复会话；N2 及以前有默认密码，N3 起必须已自定义 | p123, p573-574 |
| ADM8770 | 网络盘服务账号 | 远程与 8770 两服务器同名同密；入 Administrators、移出 Users、五项用户权利；ExecdEx/SaveRestore 的 Nt account（.\ADM8770） | p669, p680, p684, p696 |
| installer | OXO 安装员账户 | OMC 首连与 Omc config password 凭据；OXO R10 起连接时强制改全部账户密码 | p649, p653, p657 |
| Predefined access groups | 预定义访问组 | Accountants/Network experts/Simplified Configuration（持 Profile 10）等；多组权限按应用取最高 | p371, p398, p399 |

## 三、许可与订阅域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| nmc.license | 8770 许可文件 | ACTIS 生成 .sw8770，装入 8770\etc 改名 nmc.license；NMC License Server 校验完整性 | p597, p615 |
| 8770Handle | 申报节点锁 | 许可控制方法 #1：与指定 OXE OPS 文件中 Handle 比对（spadmin 显示），License Server 周期核验 | p601, p604, p613 |
| [Modules] 应用锁 | 许可模块段 | 布尔键（Topology/Audit/Security 等）+用户数键+8770Clients（并发客户端上限 30）+Security 键 0-5 | p603 |
| N-1 许可规则 | 许可版本规则 | N 版本只接受 N-1 许可——R5.2 接受版本 15 或 16 | p602 |
| Restricted mode | 许可受限模式 | 阈值超限后客户端仅 Directory 与 Configuration 可用（删户降限用），服务器不停机防数据丢失 | p606 |
| Start Pack / Full Pack PPU | 许可包型两档 | Start 含告警/计量/统一管理（Configuration 与 Audit 内含）；Full 加 Performance 与 Company Directory；另有独立选项 | p598-600 |
| OXO Connect 计费票锁 | OXO 唯一许可锁 | 默认无 ticket，按 1000 步进扩容、上限 30000；告警与 OMC 无锁 | p608 |

## 四、产品与工具域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniPCX Enterprise (OXE) | ALE 企业话务服务器 | 8770 主管对象：CMISE 配置、Telnet/SSH 维护、mao 审计、bck 备份；Purple 代次决定 8770 兼容版本 | p9, p139 |
| OXO Connect / OmniPCX Office | ALE 中小企业话务系统 | 经 OMC 代理纳管（配置本体在 OMC）；8770 声明菜单名 OmniPCX Office | p19-20, p139, p653 |
| OMC | OXO 管理工具 | OXO 全部配置在其完成；8770 服务器与每个客户端都需安装；8770 以 Online/Offline mode 代开会话 | p20, p139, p663-665 |
| MariaDB（MySQL8770） | SQL 数据库引擎 | 承载计费/VoIP/话务/告警/审计与报告；HeidiSQL 经 3306 直查 nmc5 库 | p7, p529-531 |
| Oracle DSEE | LDAP 目录服务器 | C:\8770\SunONE，389/636；存公司/用户/设备目录 | p61, p592 |
| ToolsOmniVista.exe | 服务器底层维护工具 | 密码更新/SSL-TLS 最低版/SNMP 代理启停等；须按 0 正常退出，不校验密码策略 | p315, p389-391 |
| 8770 Diagnostic | 诊断采集工具 | 产出 C:\TS 下 HTML 与 zip（zip 交 ALE 支持开 SR） | p523, p533 |
| MindTerm | 内嵌 SSH/SFTP 客户端 | Configuration 内 Connect 到 OXE 承载加密会话；公钥存 MindTerm\hostkeys | p124, p133-134 |
| ACTIS | 许可报价出证应用 | 生成 <offer id>.sw8770 许可文件 | p595, p597 |

## 五、协议与接口域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| CMIP / CMISE | 公共管理信息协议/服务 | 8770 与 OXE 间配置与告警事件的交换协议族（全书唯二展开全称处） | p139 |
| LDAP / LDAPS / LDIF | 目录访问三件套 | 389（工具与同步）/636（客户端登录口）；LDIF 是目录数据交换格式（批量与预定义 job 恢复载体） | p73, p32, p502 |
| SNMP v2c / v3 | 网管协议 | SNMP Proxy 转 trap 至 hypervisor（UDP 162）；v3 带 SHA/MD5 认证+DES/AES128 加密；hypervisor 只填 IP | p282, p313-314 |
| Telnet / SSH / SFTP / FTP / RSH | OXE 维护通道族 | 命令会话（OXE R101/N3 起 SSH 强制）、数据传输（adfexc）、RSH 跑 bck 与 mao_hdet 转换 | p110, p572-574, p427 |

## 六、路径与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| C:\8770 目录地图 | 安装根目录 | bin 工具/data 数据/dict 字典/etc 许可/install 补丁/log 日志/RestoreContext.ini；归档 C:\8770_ARC（8770Backup/OXEBackup/OXO） | p77-79, p516, p572, p658 |
| 关键日志清单 | 排障日志地图 | NMCSyncLdapPbx（同步）/NMCFaultManager（事件告警）/NMCSnmpAgent（SNMP）/NMCLicServer（许可用量）/NMCScheduler（任务，2x5MB 滚动） | p126-128, p316, p617, p548 |
| 端口清单 | 端口速查 | 80 Apache/8443 HTTPS/389 LDAP/636 LDAPS/8080 Wildfly/3306 MariaDB/162 SNMP trap/25 SMTP 默认 | p79, p313, p452 |
| /nmclog/ | 日志 Web 别名 | https://<FQDN>/nmclog/ 管理员凭据在线查看日志 | p553 |
| nmc5_5.2.cfg | 客户端连接存档 | C:\Users\<账户>\nmc5_5.2.cfg 存服务器连接信息（2019 章原文写 nmc5_5.1.cfg，见 nr-01） | p85, p103, p639 |
| RLAB 实验参数表 | 实验口径全集 | 网段 192.168.1.x 与 OXO 章 151.1.1.x、各会话凭据、预建用户 31000-31002——生产禁止沿用 | p45-51, p621, p643, p693 |

## 落位自检

- 全量 60 条见 candidates/glossary.md（六类组织）；本门户版收录 33 条高频项。
- 仅 passing 提及未进主表的词（RLAB POD 结构、TrapReceiver/FlexLM/IPDSP/MicroSIP 工具族、MCS、SOAP/SDK/DSPP、ALES-Desktop/Mobile、OTC 页签、V24、TDS/GCS 等）见候选底稿与 book/overview 环境区。
