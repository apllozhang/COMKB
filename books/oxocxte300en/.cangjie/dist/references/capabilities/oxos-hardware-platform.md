# 硬件平台与容量（产品家族 / IPBox / PowerCPU EE / 扩容边界）

## R — 原文依据

> "OXO Connect is a phone system for Enterprises and Hotels with up to 300 users"（p24）
> "2 Ethernet ports ETH0: LAN & POE ETH1: For Instant Management access on site (DHCP , DNS)"（p31）
> "The maximum number of DSP channels is extended from 60 to 76 when using the Armada 64"（p37）
> "Up to 3 racks can be interconnected using HSL links • The maximum length between the master rack and the extension rack is 5 meters"（p42）

出处：OXOCXTE300EN p23-42（产品与硬件讲义），p431-438（板卡附注与启动停机）。

## I — 自述

硬件认知四件事：

- 产品家族：OCE（IPBox，纯 IP）与 Compact/Small/Large（PowerCPU EE 机箱，混合 TDM/IP），定位 ≤300 用户企业与酒店；证书认证 RSA 2048/4096 位
- IPBox 接口：ETH0=LAN+PoE 供电、ETH1=现场即时管理口（固定 192.168.94.246、自带 DHCP/DNS）；桌面/壁挂/机架（半宽 19 英寸 1U）；背面 SD 卡槽作备份选件；零接触部署前提 OmniSwitch 侧开 PoE
- PowerCPU EE：MPC8377 @800MHz、DDR2 512MB、16 VoIP 资源起步；子板 AFU-1/HSL1/HSL2/Mini-Mix/Armada 32/64；DSP 通道四档——无子板 16、+Armada32=48、+Armada64=60 多编解码或 30 G711/G729+46 G711 共 76；MSDB 子板默认 8GB eMMC 承载数据
- 扩容与启停：最多 3 机柜经 HSL 互连（主柜到扩展柜最大 5 米，非以太网）；启动八步监控（顺序 HSL2、HSL1、主柜、VMU），停机 LED 红闪/红常亮

| 形态 | 承载 | 话音扩容 | 机柜扩展 |
|---|---|---|---|
| OCE（IPBox） | 纯 IP，PoE | SD 卡备份选件；SIP 并发 120 | 不支持 |
| Compact/Small/Large | PowerCPU EE 混合 | 子板扩 DSP 至 76 | 最多 3 机柜 HSL |

## A1 — 书中案例

**选型与容量素材**（p24-42 讲义，无实验——认知章）：

1. 客户 ≤300 用户、要混合 TDM/IP → PowerCPU EE 三档按机箱形态选
2. 纯 IP、小容量、要 FTR 上云 → OCE（IPBox）
3. SIP 并发不够 → 装/换 Armada 64（76 通道口径，前身 R2.0 为 60、OXO R10.3 为 48）
4. 板卡槽位：SLI16/DDI2/DDI4 无限制，APA8/MIX/AMIX/UAI-16 有限制（p431-435 附注）
5. 启动观测：面板步骤号对应检测/初始化阶段，卡步定位机柜（p437）

## A2 — 未来触发

使用情境：售前沟通硬件形态；估算 SIP/话音并发；扩展机柜布线；ETH1 用途疑问；开机卡住看面板；换 CPU 板评估。

语言信号：IPBox / OCE / PowerCPU EE / Compact / Armada / DSP 通道 / HSL / PowerMEX / ETH0 / ETH1 / 机柜 / eMMC / MSDB / 启动 / 300 用户。

与相邻能力区分：硬件到位后的开通 → 开通能力；WebRTC 网关拓扑与硬件适配 → Rainbow 集成卡。本能力为认知与选型参考，无独立施工。

## E — 可执行步骤

输入契约：用户数、话音形态（纯 IP/混合）、并发估算、机房条件。需求超出 300 用户 → 判停转更大产品线（书外）。

1. 定形态：纯 IP 小容量选 OCE；混合或要机柜扩展选 PowerCPU EE。完成标准：形态与依据成文
2. 核并发：按编解码配比查 DSP 通道档，SIP 并发对照 IPBox 120/PowerCPU+Armada 76（默认 16）。完成标准：并发余量确认
3. 核机房：PoE 交换机（零接触/IPBox 供电）、HSL 走线 ≤5 米。完成标准：布线条件满足
4. 交付观测口径：启动八步与 LED 语义交运维保。完成标准：验收单含观测点

判停点：

- 客户要求 OCE 上扩机柜 → 不支持，改 PowerCPU EE 平台
- 主柜到扩展柜超 5 米 → 改机房布局，HSL 不是以太网不能加长
- 并发需求超 76/120 → 超出本书平台范围，转产品线方案

输出契约：硬件形态与容量备忘（平台/子板/通道/机柜数）。

## B — 边界

- 报价与商用许可以 ALE 渠道为准，书内只给结构不给价目（BOOK_OVERVIEW 决议）
- RLAB/ITSP1 实验环境细节为教学基础设施，不随本卡交付（verified f02/f04 为 reference）
- 换 CPU 的 eMMC 移植与许可重生成口径见维护卡 Boundary
- 板卡缩写书内未逐词展开，完整规格以最新硬件文档为准
