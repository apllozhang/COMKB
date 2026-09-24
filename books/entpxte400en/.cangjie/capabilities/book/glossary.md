# GLOSSARY — OmniPCX Enterprise Starter 术语表

> 阶段 3 产出（源：candidates/glossary.md，60 条，六大域）。
> 口径：定义只采信本书正文；ARS/CSTA/DDI/SRTP/DTLS 等缩写书中未给全称处一律如实省略；PABX/MAO/NPD/VPIM/ABC/ACT/FXS/ACTIS 全称取自原文展开。

# OmniPCX Enterprise Starter (ENTPXTE400EN Ed12) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（821 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OXE (PABX) | OmniPCX 企业通信服务器 | 基于 Linux 的软件专用交换机，跑在 IP 数据网上；承载形态四种 | p30-31, p52 |
| Call Server / OXE-V | 呼叫服务器/虚拟呼叫服务器 | 系统控制中心；虚拟化形态 OXE-V 跑五种 hypervisor，功能限额与非虚拟化相同 | p31, p64 |
| Media Gateway (MG) | 媒体网关（机架） | 1U Small=3 槽/3U Large=9 槽，承载语音指南/DTMF/会议/压缩器与接口板 | p31, p54-62 |
| MAO | OXE 数据库（Maintenance Administration Operation） | 存客户配置；管理四工具=mgr/WBM/OV8770/UMC | p186-187 |
| swinst menu | Facilities 菜单（Easy/Expert） | 系统级操作总入口：启停/备份恢复/空库/日期/NTP/账户管理 | p112-113, p190-193 |
| netadmin | IP 网络管理工具 | 完整安装/菜单模式 netadmin -m；管地址/Role/防火墙/DHCP/SMTP/主机表；改动必须 Apply+重启 | p87, p136, p146-149 |
| WBM | Web Based Management | 内嵌免费 Web 管理（HTML5，仅 HTTPS）；只搜参数名不搜值；Mass Provisioning 批量 | p45, p232-237 |
| Entity / CDT | 实体/呼叫分配表 | 逻辑分区 0-1000；CDT=四状态×3 顺次路由+公共溢出号（夜转号，须单线分机） | p496-512 |
| COS（三套） | 类别服务 | Phone Features COS 256 类管功能；Connection/Transfer COS 矩阵管连转；Public COS 32 类管外呼区域 | p389-390, p413-419, p658-660 |
| Discriminator | 鉴别符（逻辑/真实/Area） | 逻辑 0-7 经实体选择器映射真实 0-255，真实鉴别符分 Area（1-64）交 Public COS 放行 | p579-580, p659-661 |
| Trusted hosts | 可信主机（iptables） | N3 起默认无主机可入站；入列=全端口全服务放行；DHCP 池自动入列不可 netadmin 改 | p137-139, p157-163 |
| Role addressing | 双 IP 地址体系 | 物理接口地址永远可达+Role MAIN 地址仅话务运行时生效，设备统一指向 Role 地址 | p129-131, p147-148 |
| chrony / NTP | 时间同步实现 | R101 起内置 chronyd：渐进同步 client/server、UDP 123；瞬时同步须先停 chronyd | p167, p170-173 |
| Degraded mode / PANIC | 降级模式/PANIC 旗标 | 许可不一致运行态：即时告警、4 小时禁内呼、8 小时循环；CPU-ID 类宽限 30 天 | p204-206 |
| Attendant group / 4059 EE | 话务台组/PC 话务台 | 每节点 ≤50 组；话务台必须属组；4059EE 只管操作，语音由关联话机/IPDSP 承载 | p449-463, p464-478 |

## 二、角色/账户域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| mtcl | 维护账户 | 日常 CLI、su 跳板、SFTP 默认身份；900 秒无操作超时 | p88, p90 |
| swinst | Facilities 账户 | 系统启停/备份恢复/空库/日期/NTP/账户管理；root 下进入免密 | p88, p100, p112 |
| root | 管理员账户 | 专家维护（防火墙/passwd/tcpdump/infocollect）；仅本地直登，IP 侧必须 su | p88, p90, p99 |
| client | 基础访问账户 | 默认禁用，经 swinst 启用；登录需话务运行；菜单仅基础几项 | p88, p101-102 |
| Attendant | 话务员 | 基础来话接收角色；权限内可从控制台手动切换实体状态 | p460-463, p502 |
| kb | OMS 键盘账户 | OMS 虚拟机低权账户（kb/kb），仅用于改键盘布局 | p261 |
| admin / root（板侧） | 媒体网关板载账户 | GD4 root=mg4.ale、OMS 均为 letacla1、GDXL root=mgxl.ale；SSH 只暴露 admin 且仅从 CS 发起 | p248, p262, p759 |
| IPDSP user | 4059EE 关联语音用户 | 话务台语音承载方（物理话机或 IPDSP），禁 multiline | p310, p482-484 |

## 三、许可/订阅域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OPS | 许可文件组 | xx.swk（锁清单）+xx.hw+hardware.mao+xx.zip；空库创建连 OPS 一起抹 | p196, p207-208 |
| Software locks / spadmin | 软件锁与锁管理命令 | 0/1=服务授权、0-99999=数量、99999=无限；十项菜单查看/校验/安装/PANIC | p199, p220-221 |
| CAPEX / OPEX | 许可双轨 | CAPEX 锁在本地 OXE；OPEX 锁在云端 LMS（Purple on Demand，R100.1 起） | p197-198 |
| RTR / CC-SUITE-ID | 运行权/云套件标识 | 经 Cloud Connect 校验运行权；CC-SUITE-ID 终身不变（FTR&RTR running 为就绪态） | p200 |
| CPU-ID / Product ID / ALU-ID | 许可锚点三态 | 物理 CS=PROM 内 CPU-ID；虚拟 CS=FlexLM .ice 绑加密狗；GAS=ALU-ID 免狗 | p197, p201-203 |
| SPS Contract / PoD | 服务合同/订阅 | CAPEX 需有效 SPS 合同；OPEX 需 PoD 订阅——UMC 访问的商务前提 | p44, p198, p813 |

## 四、产品/组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| CS-3 / GD-4 / GA-4 / EvolMEX | Common HW 板卡族 | CS-3 大脑（LAN 冗余）；GD-4 0 槽驱动 30 压缩器；GA-4 应用板；EvolMEX 扩展架驱动 | p56-59 |
| OMS | OXE Media Service | 原生虚拟化软件媒体网关：120 压缩器、独有 OPUS/G722；Shelf 四强制字段 | p65, p259-268 |
| GAS | 一体化服务器（Generic Appliance Server） | Rocky Linux+KVM 之上的 OXE 载体；FlexLM 内嵌、免加密狗、按 ALU-ID 控许可 | p67-68 |
| Crystal / XL-Media Gateway | 退场硬件/补位机架 | Crystal 因元器件稀缺退场；XL=14 槽背板、两个半架共 ≤384 FXS、奇数机位创建 | p69-78 |
| 话机系列（ALE-2…8088） | ALE 话机族谱 | SIP 入门/Essential/Enterprise/触屏 Android 四档；ALE-3 不支持远程办公 | p32, p271-284 |
| IPDSP | IP 桌面软话机 | 全量 8068s 特性；OPUS/G711/G722/G729；TFTP/HTTPS 拉配置+端口基线 | p287-289, p308-314 |
| Cloud Connect / Fleet Dashboard | 云侧设备管理与运行权平台 | 连接状态/SPS/许可下载/RTR；Fleet Dashboard 是 UMC 入口之一 | p44, p200 |
| OmniVista 8770 | 集中式管理系统 | Java 客户端+HTML 目录；AD 同步/多系统平台；配置树五分区 | p46, p238-241 |
| UMC | 统一管理中心 | 云管理平台 R1.1：Easy users/Easy SIP trunk（约 120 架构 Profile）/Expert Configuration（云 WBM） | p797-814 |
| mgr | CS 内置文本管理器 | mtcl 下 mgr -l <语言>；机架/板卡/用户全对象管理；CTRL V 确认 | p226-230 |
| OmniMessage 4645 | 纯软件语音邮件 | 四拓扑部署；仅 G711；一节点一套；管理面=WBM+Eva_tool+Audio-Station | p39, p526-546 |
| ITSP1 / MicroSIP | SIP 运营商模拟器/软话机 | 培训专用运营商（两条网关腿+公网网关）；pbxP/alcatel；生产行为差异见 n29 | p10, p21-26 |
| 内部防火墙 | OXE iptables | R101.0 起完整防火墙；INPUT/FORWARD 默认 DROP；netadmin Security 菜单配置 | p134-144 |
| 维护工具三件 | oxetrace/infocollect/securitystatustool | 三路抓包打包/离线大包/安全全景 XML；账户要求 mtcl/root 分明 | p740-756 |
| 巡检命令族 | ippstat/termstat/trkstat/sipextgw/sippool | IP 话机/终端/中继/网关/池状态；d/n/p 三语法与 -l/-g/-s 选项 | p328-335, p637-653 |
| SIP External Gateway | 外部 SIP 网关 | 运营商接入对象：远端域/注册/代理/凭证/编解码/P-ANI/Pool Number | p577, p614-615 |
| Trunk Group | 中继组 | T0/T2/SIP/QSIG 等；SIP 型 32 接入成对 62 通道（Mini 4）；同步优先级三段 | p35, p573-576, p773-779 |

## 五、协议/技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| ABC-F / Direct Link | OXE 间组网协议族 | ABC=Alcatel Business Communication；Direct IP Link 是 Location ID 的强制前提；空库可选自动建 99 条 | p35, p38, p192 |
| SIP / SIPMOTOR | SIP 中继信令进程 | dhs3_init -R SIPMOTOR 可重启加速重注册；traced/motortrace 抓包 | p613-616, p639-640 |
| T0 / T2 / T1 | ISDN 中继 | T0=BRA（2B+D）；T2/T1=PRA（30/24 通道）；信令变体按运营商选 | p60, p773, p781-796 |
| DHCP | 动态主机配置协议 | 四步交互；CS 内部 DHCP 默认关、Alcatel-only 可选；dhcpd.conf 按 MAO 再生 | p344-351 |
| SRTP / DTLS | 原生加密双算法 | 语音 SRTP+信令 DTLS；端到端覆盖 NOE 话机/SIP 分机/SIP 中继/8378/4645 | p42, p528 |
| VPIM / IMAP4 | 留言组网/邮件接入 | VPIM 留言互联；IMAP4 客户端直接听留言+邮件通知三档 | p528, p531-532 |
| P-ANI / RFC 7913 | 主叫位置外发头 | P-Access-Network-Info（≤80 字符）随 INVITE 外发；取值源 NPD/Entity/IP domain | p605-607 |
| Tone 34 / EMG log | 紧急通知信令面 | 组内统一 Tone 34+弹窗；动作 Clear/Snooze(20s)/Callback；EMG log ≤100 条 FIFO | p685-686 |

## 六、资源/文档域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| RLAB / POD | 培训远程实验室/实验单元 | POD 间独立同构；全虚拟或混合两种形态；实验口径总表见 p06 | p3-20 |
| MyPortal 文档组 | 权威文档指针组 | Sales Companion/Feature list/product limits/TC2005/SA0046/TC1774/TC3009 | p297, p545, p611 |
| VG CD-ROM | 语音指南资源盘 | Generic/Standard 指南、MOH 与文档；服务器侧目录 /DHS3ext/vgadpcm/flash/std | p430, p440 |
| ALE Knowledge Hub | 培训评估平台 | 课后评估与证书下载（培训流程，不入能力卡） | p815-821 |

---

## 收尾自检

### 1. BOOK_OVERVIEW 术语表逐条映射

| OVERVIEW 术语 | 对应条目 | 核对 |
|---|---|---|
| OXE (PABX) | 核心概念 OXE | ✅ p30 定义 |
| Call Server / OXE-V | 核心概念 CS/OXE-V | ✅ |
| OMS | 产品域 OMS | ✅ |
| GAS | 产品域 GAS | ✅ |
| MAO | 核心概念 MAO | ✅ |
| OPS | 许可域 OPS | ✅ |
| RTR | 许可域 RTR/CC-SUITE-ID | ✅ |
| swinst | 核心概念 swinst menu+角色域 swinst | ✅ |
| netadmin | 核心概念 netadmin | ✅ |
| WBM | 核心概念 WBM | ✅ |
| ARS | 并入鉴别符/SIP 中继链（机制条目，防重复） | ✅ |
| NPD | 并入 SIP 中继链与产品域网关（同上） | ✅ |
| DID translator | 并入去话/来话链路（机制条目） | ✅ |
| Public COS (Access COS) | 核心概念 COS 三套 | ✅ |
| Entity / CDT | 核心概念 Entity/CDT | ✅ |
| Attendant group / 4059 EE | 核心概念+产品域 4059 | ✅ |
| OmniMessage 4645 | 产品域 4645 | ✅ |
| chrony | 核心概念 chrony/NTP | ✅ |

结论：19 行全部"正文有明确定义或定义性用法"；ARS/NPD/DID translator 以机制并入相邻对象条目防重复；OVERVIEW 自记"17 个"为笔误（见 needs-review nr-03），以本表 60 条为唯一基准。

### 2. 仅 passing 提及、未单列的词（备查）

SEPLOS（p42）、PCS（p37）、PWT（p31）、DECT 8378/8379/8328 与 VoWLAN（p40-41）、INTOF（p779）、NDDI（p35）、CampOn（并条 4059EE）、NOS LED（并条 T0/T2）。

EVA（eva.cfg 已入 c21 口径）、TJ00302A（示例客户 ID）、n4.205.36.a（示例交付号）、dhs3（进程族名，并条 SIPMOTOR）、abcacom.exe（4059EE 放行项）、ICE type（p615 提及）。

### 3. 提取口径说明

- 所有定义只采信本书正文；全称以书中展开为准（PABX p30、MAO p186、NPD=Numbering Plan Descriptor p596、VPIM p528、ABC p38、ACT p70、FXS p75、ACTIS p201）。
- ARS（Automatic Route Selection）书中在 p593 展开；SRTP/DTLS/DDI/SIP/QSIG 等未展开缩写不做外部补全。
- p419 "the Connection COS Id is the same as the Connection COS COS Id" 与 p248 "root [mg4.ale]]" 为原文笔误，照录（needs-review nr-02）。
