# DIGEST — OmniVista 8770 安装与网络管理精华长文

> 源：8770XTE200EN Edition 47（705 页，OmniVista 8770 R5.2）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立对 8770 平台交付与运维的全局认知；操作细节按需查 13 张能力卡。

## 一、这套东西是什么

OmniVista 8770 是 ALE 的集中网络管理平台：一台**专用** Windows 服务器上装齐 MariaDB 数据库、LDAP 目录、Apache/Wildfly 与全套管理应用，再用 thick client（全功能）和 WBM 轻客户端（给非专家）去管理 OXE、OXO Connect、OpenTouch 这些话务系统——管配置、管用户、收告警、出报表、做备份、控许可。

整本教材就是一条交付主线：**装平台、接节点、开用户、收告警，再配安全审计与报表任务，最后备份与许可兜底**。每章先讲义后实验，实验都以可观察结果收口（同步成功消息、告警上屏、邮件到达、trap 被收到）。

三个特性先记住：

| 特性 | 含义 |
|---|---|
| 专用服务器 | 8770 全栈独占一台 Windows 服务器，容量与补丁窗口按专用机规划 |
| 装后不可改 | 公司名、成本中心方式、HTTP/HTTPS 端口、目录管理器登录名装后不可改；改址靠备份恢复/rehosting |
| 号对号接入 | 声明节点号 = 网络号×100+节点号，必须与 OXE 侧 siteid 一致才能同步 |

## 二、装机：从裸机到可登录

1. **前置**：NTFS 分区、计算机名合规（<15 字符、字母开头、11 类禁用字符）、DNS 后缀、静态 IP；iso 必须拷到本地盘（禁网络/挂载/vSphere 安装）；内存占用 <85%
2. **安装**：ServerSetup.exe 自动装 MariaDB 与 Visual C++ 包，许可校验全 Valid，四目录（C:\8770、SunONE、data、8770_ARC）
3. **Windows 两件套**：关 IE 增强安全配置 + Defender 排除 C:\8770——漏做 Alarms/Topology 收不到告警（高频坑）
4. **补丁**：patches 目录 + PatchInstaller.exe，日志尾部见成功消息；清单查 Patch_history.ini
5. **首连**：AdminNmc 强制改密；客户端从 URL 下载（大小写敏感），Win11 22H2 起要装回 WMIC，首启放行 Zulu 模块

硬件双档：<5000 用户双核约 2GHz + 6GB；>5000 用户四核约 2.2GHz + 8GB；均 120GB 盘。

## 三、接节点：号对号 + 同步语义

- **OXE 五段**：siteid/netadmin 核查 > 三级树声明（Network > Subnetwork > PCX）> 同步 > 实时核验（建测试用户看事件与树）> 排障（重启 NMC Alarm server）
- **同步四语义**：Complete 全量 / Partial 增量（仅五类条目，其余全取）× Separate 单节点 / Global 连带 OpenTouch。OXE 改动实时回传，但 profile、键 profile、空闲号段必须主动同步
- **SSH 安全链**：netadmin 可信主机 + 8770 侧 MindTerm 密钥 + SFTP；OXE N3 起 SSH 强制
- **OXO Connect**：经 OMC 代理纳管（装在 8770 与每个客户端），声明节点按 子网号×100+节点号 换算（80 变 180），备份目录随之落盘；R10 起强制改全部账户密码

## 四、开用户：三层递进 + 批量

| 层 | 做法 | 关键点 |
|---|---|---|
| 手建 | Users 应用直接建 | User type=OXE 带设备 |
| Profile 复用 | OXE 建 Profile（大写名+COS），建户引用 | 前提：勾 Use profile with auto. recognition |
| Meta profile | 绑 OXE 节点+空闲号段+设备类型 | 建户只填姓名，自动取段内首个空闲号；号段建后必须同步 |
| 批量 | 导模板改文件导入 | XXXX=必填人工、NULL=自动；action=ADD/MODIFY/DELETE；Scheduler 绿态核验 |

WBM 轻客户端（8443）给非专家自助：单建+批量（+;-;# 语义），但与 thick client 批量文件**互不通用**、不能移除设备/OT 应用、设备页签上限 4 个。批量默认密码 1234 是安全审计必查项。

## 五、告警：一条链三个出口一条外送

- **接入**：OXE Incident Manager 设 Network severity=None（全上送）+ Topological network=YES；rstcpl 重启 coupler 触发 #2042、incvisu 验证；定向事件（#1125）建 Incident Filter（下拉没有就先 Create）
- **处置**：六级色标（Critical 红到 Cleared 白）；确认只是"有人在管"仍活动；只有非相关告警可手动清除；Signature/Action 进报告、Remark 不进
- **出口**：邮件（Mail server 格式 <地址>:<端口>，冒号后无空格）、脚本（.bat 放 scripts 目录，%1=告警对象、%2=通知时间）、字典改名（重启 NMC Service Manager 生效）
- **外送**：SNMP Proxy——Windows SNMP 服务必须装（启用 8770 代理后被停用但不能卸载）、hypervisor 只填 IP 不用 FQDN、trap 162、SNMP Filter 按 Correlation/Diagnostic 过滤

## 六、安全与审计：三层模型 + 一条留痕链

- **第一层 8770 账户**：密码策略（时效三参数必须 B+C<A）、组权限多组取最高、单登录（AdminNmc 豁免）、锁定四路解锁（Security 改密 / ToolsOmniVista / AdminNmc 专用 / WBM 邮件重置码）
- **第二层 OXE Access Profile**：11 档全体 OXE 共用一套，改完必须删客户端本地 MIB 才生效
- **第三层 OXE 白名单**：User Access Control 大写账号清单，前提勾 Secure access for system management；TLS 加固前必须全网元 TLS 摸底（书内标注仅供信息）
- **审计只管 OXE**：双侧开关（AuditServer + Process audit/mtcl/Secure access）> mao 三日志 > System 页要重建 PbxName Not Empty 条件（默认条件无效是产品行为）> History/Detail 两粒度导出；8770 自身 log 只看不导

## 七、报表任务与兜底

- **报告**：默认上限 TXT 4000 行/各格式 50 页/库 100000 行，超限尾部截断提示；可文件/邮件导出与计划分发
- **任务**：Job=任务集合、Simple job/Synchronized task 两种组装、jobset 刷新变 Job；Maximum start delay 超时即放弃补跑（不是开机必补）
- **自动维护**：五类清除（计费/报告/告警/审计/文件夹）+ Purge job 串行链；预定义 job 改坏了用 DailyJob/WeeklyJob.ldif 导入恢复
- **8770 备份恢复**：备份四块内容（LDAP/MariaDB/其他/RestoreContext.ini）、版本强绑定（nmcVersion）、备份期网管不可用；改 IP/换机走 rehosting
- **OXE 备份恢复**：bck 命令 + FTP/SFTP 取回；swinst 恢复七步（停电话后 role address 失效，要用物理 IP 重连）
- **许可**：锁+数（申报节点 8770Handle、服务器特征绑定；Modules 段布尔键+用户数键+并发客户端 30+Security 键 0-5）；N-1 版本规则（R5.2 吃 15/16）；超限进受限模式（仅 Directory+Configuration，重启无效）
- **网络盘**：ADM8770 同名同密账号 + 五项用户权利 + ExecdEx/SaveRestore 注入 .\ADM8770，备份与报表才能落网络存储

## 八、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 装 8770 服务器/客户端/补丁 | ovnms-platform-installation |
| 注册 OXE/同步/SSH/纳管 OXO | ovnms-node-onboarding |
| 建用户/批量/WBM 开通 | ovnms-user-provisioning |
| 接告警/邮件脚本通知/SNMP Proxy | ovnms-alarm-management |
| 密码策略/权限/解锁/白名单/TLS | ovnms-security-administration |
| 开审计/查操作留痕/导审计 | ovnms-audit-compliance |
| 8770/OXE 备份恢复/rehosting | ovnms-backup-restore |
| 许可查询/更新/超限处置 | ovnms-license-management |
| 报表分发/任务编排/数据清理 | 路由入口（omnivista-8770-nms-router） |
| 诊断工具/服务与日志 | 路由入口（omnivista-8770-nms-router） |
| Topology 大屏/告警上图 | 路由入口（omnivista-8770-nms-router） |
| OXE 界面高效操作 | 路由入口（omnivista-8770-nms-router） |
| 备份报表落网络盘 | 路由入口（omnivista-8770-nms-router） |

## 九、交付红线

1. 教材全部密码/账号/网段（Superuser2580*、superuser、letacla1、sql、pbxk1064、Alcatel1、Pbxnmc12、192.168.1.x、151.1.1.x 等）是实验值，上生产必须换并纳入客户密码策略
2. 8770 单机闭环，无高可用设计——双机/容灾引 High Availability 产品文档；容量规划用 Capacity Planning 工具
3. 文档质量三处已知问题：2019 章沿用旧版口径（cfg 文件名 nmc5_5.1.cfg）、OXO 章有未翻译法语残句、客户端空间表述混写——引用时按 needs-review 处置

## 版权

- 本精华长文为 ALE Training Services《OmniVista 8770 — Setup & Network Management》（8770XTE200EN Edition 47）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
