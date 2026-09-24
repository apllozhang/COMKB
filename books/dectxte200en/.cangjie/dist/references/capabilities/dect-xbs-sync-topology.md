# xBS 空中同步体系与组网域（Sync Master/Cluster/Highway/外部同步/Site）

## R — 原文依据

> "The maximum of levels in the synchronisation tree is 24"（p75）
> "The selection of the base station used for external synchronization ('Master Sync' and 'External Synchronization RPN' is done manually ... The Sync master base station does not support any communications ... A backup Sync Master must also be setup and configured"（p106）
> "When more than 2 PARIs are synchronized together using external sync, additional configuration is needed: a synchronization highway"（p111）
> "A SITE is a group of 8378 DECT IP-xBS linked to a call server and located in the same geographical location where it is possible to do handover"（p86）

出处：DECTXTE200EN p75, p86-92, p93-97, p98-116, p199-203, p263-270。

## I — 自述

同步是 handover 的生命线（帧级精确同步是切换前提，p25），加上 Site 切换边界构成组网域：

1. **Internal Sync**：同 Site 同 PARI 内基站空中时间对齐；同步树按 RSSI+跳数自动构建（最深 24 级），随无线环境自动重构，默认零配置。
2. **Sync Master**：树根基站。内部同步时自动选举、可随环境漂移；外部同步时**手工指定且禁止承载任何通信**（纯同步站）。
3. **Backup Sync Master**：外部同步时强制配置；必须物理邻近主站、看得见同一个外部同步源基站；可补位承载主站不支持的话务，主备切换后该话务即失。
4. **Sync Cluster**：每 Site/PARI 最多 8 簇、默认全在 Cluster 0、单站可属最多 8 簇；仅用于站内同步不稳定的特殊场景（如电梯井），拆簇代价是簇间无同步。
5. **External Sync / Sync Highway**：两个同步树之间对齐（xBS 树↔xBS 树或 xBS 树↔TDM 基站树）；>2 个 PARI 串联需附加 Sync Highway 配置。
6. **Site（切换边界）**：同地理位置可 handover 的基站组，默认全在 Site 0；同 Site 内有 handover、跨 Site 只有 roaming；一个 PARI 可拆多 Site（分支办公），一个 Site 可含多 PARI（需配 PARI 间同步链路）。

切换可行域：Data Sync Primary 每 Site/PARI 自动选出一个（dectview xbs 的 P 标志），handover 只发生在同一 Data Sync Primary 之下；基站间同步门槛 RSSI -80dBm（p210）。

主备皆失（p109）：其余基站全部停摆（无孤岛），恢复后同步树**不会自动重建**（原书自注 will be improved in a future release）。

## A1 — 书中案例

**外部同步链路与外部 handover 实验**（p263-270）：

1. 前置：Mixed 模式、xBS PARI=100004101x4、IBS PARI=100004101x0、PLI=30、两站间距约 15 米（实验口径）
2. PWT/DECT System → Flag External Handoff=yes
3. xBS Site / External Synchronization：PARI Number=1、Sync Master RPN=0、Sync Master backup RPN=255（none）、External Sync PARI=100004101x0、External Sync RPN=0
4. 核验：dectview xbs 表尾出现 External sync source 行（S 0-IBS → *M 0-GF-01，Backup B 255）
5. 通话验证：**呼叫必须先建在 IBS**（Attention 原文）；dectview com 看 STABLE，移向 xBS 切换后 dectview com 显示 RELAY/RADIO 且通话不断

**多站点实验**（p199-203）：

1. xBS Site → Create：Site Number=1、Site Name=BO；Site 0 改名 HQ
2. xBS base station → id 1 → Site Number=1
3. 核验：dectview xbs 显示 "Region 0 (EUROPE) has 2 site(s) with 2 XBS in service"，两站各为本站 Master（P+ 判读，推断标注）
4. WBM → Multi Cell → DECT chain information 看各站同步链
5. 漫游模拟：关手机、拔 HQ 站、再开机试呼成功（跨站 roaming）

## A2 — 未来触发

使用情境：通话中切换失败排查；多 PARI 同步组网；Sync Master 坏了；电梯井场景基站分组；混合 IBS/xBS 要切换；分支办公组网；跨楼手机能不能用；>254 台扩容。

语言信号：同步 / synchronization / Sync Master / Backup / Sync Cluster / 簇 / Sync Highway / 外部同步 / External Synchronization / Data Sync Primary / handover / 外部切换 / Flag External Handoff。

相关词：Site / 多站点 / branch office / 漫游 / roaming / -80dBm / 24 级。

与相邻能力区分：混合模式的 PLI 适配见混合部署能力；Site 拆分的 PARI 前提见标识号码能力；dectview/xbssynchro 命令细节与基站 Site 归属判读见维护排障（路由）。

## E — 可执行步骤

输入契约：拓扑类型（单 PARI/多 PARI/混合/分支办公）、基站间距与无线环境。站间 RSSI 未知 → 先勘测（覆盖勘测能力，路由）。

1. 单 PARI 单 Site：默认零配置，内部同步树自动构建。完成标准：xbssynchro 显示一棵树、站间 RSSI 达 -80dBm
2. 分支办公：xBS Site 逐个建 Site、基站改 Site Number。完成标准：dectview xbs 归属正确、每 Site 一棵树
3. 特殊场景拆簇：仅当站内同步不稳定（电梯井等）按 Cluster 0-7 分组。完成标准：簇内同步稳定、簇数 ≤8
4. 多 PARI/混合：指定 Sync Master RPN（禁载通信）+ Backup（255=none）+ External Sync PARI/RPN。完成标准：dectview xbs 表尾见 External sync source
5. 开外部切换：Flag External Handoff=yes；>2 个 PARI 追加 Sync Highway。完成标准：跨 PARI 切换可用
6. 验证：起呼于被同步侧（IBS），移动完成切换，dectview com 核 RELAY 且通话保持。完成标准：切换后通话不断；跨 Site 场景验证 roaming

判停点：

- Sync Master 坏了全站停摆 → 按 p109 口径如实告知：无孤岛、恢复后不自动重建，人工干预重建同步
- Backup 与 Master 相距远、看不见同一外部同步源 → 备份形同虚设，先改选址再谈冗余
- Backup 顶上后话务丢失不可接受 → 在主备旁再加一台专载话务的 xBS（p109 方案）
- 同步树超 24 级 → 拓扑不支持，加同步源或拆 Site
- 客户要求"跨 Site 通话中切换" → Site 语义不支持（p87-88）；跨 PARI 需求按外部同步路线评估

输出契约：组网域说明（Site/树/簇/外部链路）+ dectview xbs 标志判读记录 + 切换与漫游验证记录。

## B — 边界

- 硬规格：同步树 24 级、每 Site/PARI 8 簇、单站 8 簇（p75/p102）；超界场景书内无方案
- "拆簇导致跨簇 handover 受限""各站应为本 Site 的 Master"为推断标注（needs-review nr-06）
- 外部同步实验的正值 RSSI 表述（RSSI > 70 dB）按 -70dBm 门槛口径理解（needs-review nr-07）
- 多 Site 与多 PARI 组合时的 PARI 间同步链路只有概念描述（p91-92），配置细节书内未展开（待确认）
- 生产无线设计（传播/天线/勘测方法）在 8AL90874USAA，本卡只管同步与组网配置验证
