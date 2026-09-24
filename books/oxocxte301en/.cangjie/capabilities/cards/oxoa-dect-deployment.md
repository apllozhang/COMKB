# DECT 无线移动（标准与标识、集群同步、注册部署、勘测与 SUOTA）

## R — 原文依据

> "DECT is based on a multi carrier FDMA and TDMA with TDD … 24 Timeslots … 10 Carriers (Frequencies)"（p500）
> "Up to 80 DECT IP-xBS … 1 PARI for the system (common with IBS) • 11 simultaneous calls per xBS • 200 DECT handsets"（p495）
> "Cluster = DECT area where all base stations are synchronized together … The cluster membership is imposed by the OXO Connect"（p506）
> "measurement of the -72 dBm attenuation at the limit of the area … Zone of voice quality"（p533）
> "A site survey is mandatory before of a product offer or before installation in order to determine the number and position of Dect base stations"（p530）

出处：OXOCXTE301EN p481-552。

## I — 自述

DECT 是完整无线子系统，四块：

**标准与标识**（p498-503）：

- DECT（ETSI EN 300 175 系列）+ GAP（ETSI EN 300 444）；10 载波×24 时隙（TDD），语音 ADPCM G726 32kbit/s；每 xBS 12 时隙 11 并发
- 标识五件套：PARI（系统安装 ID，全系统一个、xBS 与 IBS 共用）、RFPI（xBS 标识）、PARK（话机侧系统标识）、PLI（=31）、IPUI（话机身份，14 位八进制）

**容量双轨**（p494-495）：

| 轨道 | 基站 | 并发 | 上限 |
|---|---|---|---|
| IP 轨 | 8378 IP-xBS（三型，PoE class2） | 每 xBS 11 | 80 xBS / 200 手柄（需 IP-DECT 用户 license） |
| TDM 轨 | 8379/4070 IBS（接 UA 板） | 每 IBS 6（1 UA=3 并发） | 60 IBS / 200 手柄 |

**集群与切换**（p504-517）：站点（≤20，站间不切换）→集群（空口同步组，每站 ≤8，成员由 OXO 强加）→xBS 同步树（Automatic 模式推荐，Manual 仅专家）；切换（handover）仅同集群内，媒体由 IP-xBS 子系统自管（Relay xBS）；话机可能锁定在同步但信号较差的基站（xBS 与 TDM IBS 间必然如此，n29）；复杂拓扑找 TSS（n30）。

**部署与勘测**（p515-534）：单站四步（PoE 与 Auto Provision、DHCP、PARI、话机注册）；LED 红/橙/绿时序判读；SUOTA 空中升级（并发 50、下载 4-8 小时且话务优先、swap 须充电座）；勘测以 -72 dBm 划语音质量区（-80 下限）、通话中测音质（最少两台话机）。8158s/8168s VoWLAN 仅 NOE 模式（p550）。

## A1 — 书中案例

**DECT 注册实验（IBS 向导法）**（p535-540；虚拟课堂不可实操）：

1. IBS 接机架 UAI 板空闲口（红 LED 慢闪正常）。
2. 话机复位：*7378423* 选 Master reset 进 Auto install。
3. OMC 双击 Wizard for DECT/PWT On-Air Registration（不见则 Comm/Read all from PCX）。
4. 建订阅户（名+DDI）后话机侧 Auto install/PIN 0000/选 PARK。
5. IPUI 出现在 Unassigned IPUIs 后 Assign；呼有线分机验证显示目录号（p540）。

**IP-DECT xBS 部署实验**（p541-548；虚拟课堂不可实操）：

1. LAN/IP 核对（warm reset）；DHCP 启用（范围实验口径）。
2. PARI：OMC/Dect/DECT-PWT ARI-GAP/ARI 填 11 位八进制（每客户唯一，eBuy 获取；实验 110004360P0）。
3. 接 PoE 核对 LED：红（初始化/取 IP/配置文件）→橙（下载/链路/配置）→绿 1s 亮灭=就绪。
4. 订阅户列表应自动出现 xBS（别忘了启用 Auto Provision）。
5. 话机经 GAP registration 注册（GAP Reg 读 IPUI 后 Assign）。

**站点勘测（SSK）**（p529-534，讲义）：

1. SSK 行李箱：2 台勘测专用 xBS（固件与生产不同，n32）+8dBi 天线+充电宝+2 话机。
2. 装固件与国家频率（室内/室外 PARK 实验口径），电池供电摆位。
3. 话机 site survey 模式测衰减：-72 dBm 划语音质量区、-80 以下放弃。
4. 通话中测音质（最少两台话机注册，或拨 0+拨号键听连续拨号音）。

## A2 — 未来触发

使用情境：厂区/仓库/酒店要无线移动；DECT 基站怎么布点；话机注册不上；漫游掉话；信号满格通话差；批量升级话机固件；勘测报告怎么验收。

语言信号：DECT / IP-DECT / xBS / IBS / 8378 / 8379 / 8328 / PARI / ARI / IPUI / PARK / 集群 / cluster / 同步 / 切换 / handover / 漫游 / 勘测 / site survey / SSK / -72 dBm / SUOTA / 8214 / 8158s。

与相邻能力区分：xBS 日志与状态经 Webdiag 的 DECT 块查（维护工具能力）；8328 SIP-DECT 单基站小分支的选型规格见本卡 I 段；VoWLAN 话机部署工具（WinPDM/TC2349）在书外。

## E — 可执行步骤

输入契约：覆盖区域平面图与话务分布、话机型号与数量、站点网络（PoE/DHCP）、ARI（eBuy）。无勘测报告 → 判停：报价与安装前勘测强制（p530），不要凭经验布点。

1. 选型：IP 轨（xBS，80/200）或 TDM 轨（IBS，60/200）或 8328 小分支；8214 需 R6.0 MD1（n28）。完成标准：BOM 成文
2. 部署：PoE 接入+Auto Provision+DHCP；PARI 填唯一 ARI（xBS 与 IBS 共用）。完成标准：基站绿 LED 入列
3. 注册：向导法（3 步）或订阅户列表法（GAP Reg+Assign）。完成标准：话机注册并显示目录号
4. 同步规划：Automatic 模式管集群选主；站点间不切换、切换仅集群内——按此划集群。完成标准：拓扑与覆盖匹配
5. 勘测验收：-72 dBm 边界 + 通话测音质；混合组网提示"同步优先于信号"现象（n29）。完成标准：报告签认
6. SUOTA：WebDIAG 配自动/手动/关；并发 50、话务优先、swap 须充电座。完成标准：升级计划可执行
7. （加密需求）DECT 空口加密默认关：开启后不兼容加密的第三方话机无法运行（n61），先清点终端。完成标准：安全口径确认

判停点：

- 虚拟课堂/无硬件环境 → 两处 DECT 实验不可做（n34）：首次现场部署预留加练时间
- 多楼/分支办公等复杂拓扑 → 找 TSS（n30），不要自配同步树
- ARI 来源不明 → 停：每客户唯一、eBuy 获取，抄邻站会跨站归属混乱（n35）
- 勘测专用 xBS → 不运行标准固件，勿与生产混用（n32）

输出契约：BOM 与容量核算 + 基站布点图与集群划分 + 注册台账 + 勘测报告（-72 dBm 覆盖区）+ SUOTA 计划。

## B — 边界

- 站点勘测方法与工程规则在书外（SSK 手册 8AL90874USAA）：本卡只给验收口径（-72 dBm/通话测音质）
- DECT 频段与功率按地区不同（欧洲 1880-1900 MHz 等，p501；该页为 OXE 素材残留，nr-04，生产前复核）
- 全局限制以 MyPortal《OXO Connect Global Limits》为准（p497）；8214 兼容性与预定义消息图标为 2023 底计划口径（n28），以最新 TC 为准
- xBS↔呼叫服务器 IP 段无认证无加密：空口加密只保护无线段（n61）
- 实验值（PARI 110004360P0、PARK、DHCP 范围）全部为实验口径；生产按 eBuy 与客户规划
