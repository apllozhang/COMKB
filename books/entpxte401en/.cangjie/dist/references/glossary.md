# GLOSSARY — OmniPCX Enterprise Advanced 术语表

> 阶段 3 产出（源：candidates/glossary.md，g01-g65 共 65 条，六类；本表精选高频约 42 条按域分组）。
> 口径：定义只采信本书正文；DDI/TFTP/WBM/MIPT/ARS/RTP/DTLS/IPSec/FQDN 等缩写书中未给全称，如实标注；C.A.C/PCS/ABC-F2/DSS/DSU/REX/SCP/OMS/IPDSP 等书中已展开的照录。

# OmniPCX Enterprise Advanced (ENTPXTE401EN Ed13) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（543 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| CS Duplication | 呼叫服务器复制 | main+standby 软件平台成对，备库实时 scp 复制；切换时已建立通话保持、建立中丢失；两机须同版本同类平台 | p70-71 |
| Mastercopy | 数据库克隆 | 在备机上经 swinst 把主库（至少 DATABASE AND ACCOUNTING，可选 LINUX DATA）复制过来；440 事件后的唯一修复手段 | p79, p106-108 |
| Reference Media Gateway | 参考媒体网关 | double main 的裁判网关：两 CS 失联时连它的一侧为 Real Main，恢复后另一侧自动重启 | p74, p76-77 |
| Double Main Mode | 双主模式 | IP 链路中断出现 Real Main+Pseudo Main（MAO 关）；期间话单/话务观察不合并、部分网络无语音邮箱——故障态非目标态 | p76-77, p82 |
| Spatial Redundancy | 空间冗余 | 两 CS 分处不同子网的冗余（机制同本地）：各自主角色地址 csma/csmb；配套内部 DNS/委派/DHCP/TFTP 适配 | p82, p84-90 |
| Preferred CS IP @ | 主角色优先地址 | MAO 参数：两 CS 同时上线时定 main；未配置则 IP 高者成 main（防御行为） | p75, p105 |
| Updates storage time limit | 失联存储窗口 | 备机不可达时主库存 MAO 命令历史的时限，默认 120 分钟（0-120 可配）；超时删历史并触发 440 | p79 |
| IP Domain | IP 域 | 按设备 IP 在初始化时归类的逻辑域：每系统 1000 域、未匹配落默认域 0；CS 必须域 0 且其他域不得覆盖 CS 地址 | p143, p152 |
| C.A.C (Call Admission Control) | 呼叫准入控制 | 只控跨域通话条数（Domain Max Voice Connection，-1 不限）；域内不受控；cnx dom 读计数 | p144, p162 |
| PCS (Passive Communication Server) | 被动通信服务器 | 域级生存性备用 CS：锁 332>0、版本≥CS；失联转 Active 接管；库单向同步、最长激活 30 天；非热备 | p166-184 |
| TFTP Backup IP@ | 备份 TFTP 地址 | CS 经信令链路下发到话机 flash 的 PCS 地址；断链时话机改连 PCS；tnet d 的 ipconfig survi 可查 | p172 |
| Local Private to Public Overflow | 本地私到公溢出 | CAC 饱和/缺压缩机/断链（PCS 激活）时跨域呼叫改经公网；对 SIP 扩展/设备不适用；话务台恒放行 | p218-226 |
| Thin Sector | 细分扇区 | 把一段非 DID 内部号映射到唯一外部号（段首号）；该外号不得与既有 DID 段重叠 | p224, p230-231 |
| Speed Dialing | 缩位拨号 | 统一索引表 0-32499（默认仅 4000 可配）；直接式+范围式（至多 400 范围、每实体 32 区）；默认绕过闭锁 | p236-244, p247 |
| Multiline | 多线 | 话机持一/多目录号、每号可配多线键；Multi-keys（一号多键）与 Multi-MCDU（多号一机）；监督类特性公共前置 | p257-261 |
| Supervision Key | 监督键 | 看被监督方状态、按键直呼或代接；上限 20 监督者/话机、100（网络 20）/邮箱、15000 键/系统；话务台与寻线组不可被监督 | p262-265 |
| Screening / Unscreening | 过滤/反过滤键 | 经理/助理过滤：仅表内来话转助理/仅表内来话留经理；互斥激活；过滤表 1000 张×16 参数 | p277-279 |
| Hunting Group | 寻线组 | Sequential/Cyclical/Parallel 三搜索；成员随进出组切换组 COS（公网 COS 留 255 保留自己）；一台话机仅属一组 | p299-305, p318 |
| Call Pick-up | 代接 | 组代接（拨前缀接同组振铃）与直接代接（前缀+号码）；Pickup 组无独立建组菜单，填 PickupGroup Name 自动成组 | p306, p313-314, p323 |
| Desk Sharing (DSS/DSU) | 办公桌共享 | DSS=共享话机（真 MAC）、DSU=漫游用户（虚拟 MAC aa:bb:分机号）；登录即恢复键位/特性/邮箱 | p329-336 |
| Multi Device / Twinset | 多设备用户 | 主站+至多 4 副站逻辑关联（twinset 为 2 台特例）；主站号即多设备号；建关联清空两机数据 | p353, p366 |
| Rapid Call Shift (Twinset Get Call) | 快速移机 | 空闲侧拨 Get Call 前缀，通话无感迁移（对端听不出、屏显不变） | p363 |
| Direct IP Link | 直连 IP 链路 | ABC-F2 新一代节点间链路：子网内全互联、RTP 直传、IPSec+SRTP 原生加密、免许可免 H.323；Enabled 不可逆 | p383-397 |
| Audit | 审计对账 | 全网库一次性对账：两阶段（参考库构建→全网下发）；直改表须先模拟+强烈建议备份；链式对象常需跑两遍 | p426-442 |
| Broadcast | 广播同步 | MAO 修改先进 buffer，默认 10 分钟后落 LOG，再互比 lupd.dat 补齐，确认后删除；128 广播域；远端写失败产 RLOG | p471-486 |
| Network/Routing Number | 网络/路由号 | 直链 audit 前指向远端用户的两种编号手段：单号/号段；audit 后远端用户自动入本地编号计划 | p410-411 |
| Node Access Prefix | 节点接入前缀 | 溢出方向的路由钉子：Number to add（本地 ARS 前缀，不广播）+Install No Last Part+Node DID Translation（广播） | p504-505 |
| Reference Node | 审计参考节点 | shared 对象以其库为准全网替换；默认=运行 audit 的本地节点，可指定远端 | p426, p432 |
| pcscopy | PCS 库刷新 | 手动命令（菜单 1 update）或 WBM Daily/Weekly 计划；前提双向 trusted hosts+hosts 条目+SSH 免密 | p179, p209 |
| Broadcast Area | 广播域 | 节点分组限定广播范围：域号 -1..127 共 128 个；出向三态×入向三态，全局或逐对象 | p481-483 |

## 二、角色与账户域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| mtcl | 电话维护账户 | 命令行维护默认登录账户；SSH 密钥三账户之一 | p10, p57 |
| swinst | 软件安装账户 | Easy/Expert 菜单（克隆/autostart/停起话音/空库）；swinst 管的 Linux 数据随冗余链路复制 | p74, p107 |
| root | 系统超级账户 | oxe-ssh-auth/oxe-nw-sshkey-sync/netadmin -m 须 root；SSH 密钥三账户之一 | p59-60, p193 |
| Real Main / Pseudo Main | 真主/伪主 | double main 期两角色；/IP/Duplication parameters 的 Pseudo Main 参数定组合（True=real+pseudo 典型） | p76-77, p105 |
| DSS / DSU | 共享话机/漫游用户 | 办公桌共享把话机角色做成 Set Function 属性；DSU 自动获得虚拟 MAC | p330-332 |
| Manager / Assistant | 经理/助理 | 经键对声明的逻辑角色：经理侧 Assistant Call、助理侧自动生成 Manager Call；Routing Assistant 每经理一名 | p276, p287 |

## 三、许可与协议域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Lock 186 / 332 | 冗余/PCS 许可锁 | 186 E-CS redundancy（冗余前提 ≥1）；332 PCS max. number（实验上限 3）；spadmin 核验 | p94, p167, p188 |
| ABC-F / ABC-F2 | ALE 私有组网协议族 | ABC-F2=Alcatel-Lucent Business Communication – Features 2（直链承载的新一代） | p384 |
| FlexLM | 浮动许可服务 | OXE 预配置声明其地址；spadmin 有专菜单查连接；软件锁/CAPEX 许可来源 | p10, p49, p188 |
| SSHv2 / 公钥认证 | 安全外壳协议 v2 | N3 起默认启用且 host-based 因 CIS 移除；mtcl/swinst/root 各持独立密钥对 | p57 |
| SCP / SFTP | 安全复制/传输 | 冗余库实时复制走 scp；audit 对象表转 ASCII 压缩后走 sftp | p71, p437 |
| IPSec / DTLS / SIP TLS / SRTP | 直链加密栈 | 节点间信令（含 audit/broadcast）走 IPSec；媒体 DTLS/SIP TLS+SRTP（密钥由各 CS 生成下发） | p393-394 |
| RTP (Direct RTP) | 实时传输协议 | 架构卖点：话机/网关间媒体直达不经转发；直链把 RTP 装进 ABC-F 信令内全 IP 传输 | p43, p385 |
| DDI | 直拨外线翻译 | 外线号段映射内部号段（Default DID translator 与 Node DID Translation 两级）；缩写未展开 | p54, p224 |
| ARS | 自动路由选择 | 溢出与重路由的路由引擎（Node Access Prefix 的 Number to add 常填 ARS 前缀）；基础管理属 Starter | p222, p519-522 |
| TFTP / DHCP | 终端引导/地址协议 | 话机 binaries/配置下载与地址分配；spatial 下可发两个 TFTP 地址；PCS 不提供两者 | p90, p112, p183 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniPCX Enterprise (OXE) | 企业通信服务器 | 本书主角（R101.1 MD4）：集中式 15000 分机/组网 100000 分机；CS 板卡/GAS/VM 三类平台 | p1, p43-44 |
| OMS (OXE Media Service) | OXE 媒体服务 | Rocky Linux 虚拟机（omsconfig）：OPUS/G722 转码与会议等媒体资源；冗余章作参考 MG、PCS 章为被救对象 | p135, p147, p200 |
| GD4 / mgconfig | GD 网关板卡与配置工具 | IP/角色地址/下载协议/SSH/证书管理；PCS 救援时软复位改连救援 IP | p110-111, p171 |
| INTIP (virtual INTIP A) | IP 信令板 | 域内设备与其交换信令（虚拟机架 19 位 1）；DSU 未登录时 ippstat 显示虚拟 INTIP 255/255 | p147, p350 |
| IPDSP | IP 桌面软话机 | 实验主力终端（31000-31003）；Settings→Network 填 TFTP Server Main；即时登录不适用 | p51, p336 |
| 4645 Voice Mail | 语音邮箱服务器 | 仅 G711；跨域访问需同域板卡转码；PCS 被救域不可达 | p151, p183 |
| OmniVista 8770 | 网管平台 | PCS 激活期话单取回通道；broadcast 激活入口之一；操作细节在书外 | p181, p473 |
| WBM / mgr | Web 配置界面 | 本书全部 WBM 配置路径的入口（IP Domain、Passive Com. Server、Inter-Nodes Links 等） | p155, p473 |
| REX (Remote Extension) | 远端扩展 | 多设备副站类型之一（每多设备限 1）；振铃可经激活/停用前缀控制（示例 651） | p354, p360 |

## 五、资源与站点域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| /usr2/mtcl/.ssh 路径族 | SSH 密钥路径 | mtcl/swinst/root 三账户密钥与 authorized_keys 所在；核验条数（两机 6 条/三机 9 条） | p67, p100 |
| /usr4/mao 文件族 | 广播文件目录 | buffer（cm_cb.sav）、LOG.N.S/A.Z.N.S、RLOG、lupd.dat——广播健康第一现场 | p474-478 |
| /tmpd 文件族 | 实验文件目录 | Firewall_Rules_multi.txt、ssh_multi.csv（自动删除）、oxenwsynclogs.zip | p94, p203-206 |
| TG0028 | 话机排障指南 | My Portal 下载：IP 话机命令（tnet/ipconfig 等）权威清单 | p200 |
| My Portal / ALE Knowledge Hub | 门户与培训站 | 技术文档下载/培训评估与证书（enterprise-education.csod.com） | p200, p539-543 |
| RLAB / POD | 远程实验室/实验单元 | Pod 间独立同构、共享公共资源（NAS/ITSP1/外部 DNS）；两种 Pod 拓扑+Hybrid 变体 | p5-32 |
| ITSP1 | SIP 运营商模拟器 | 公共区模拟出局：pbxP/alcatel 注册、DDI 41000-41499 ↔ 31000-31499、PN=POD 号 | p33-39 |
