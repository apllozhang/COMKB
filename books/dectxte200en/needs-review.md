# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 p44 实验环境表 OXE 地址点号错位（原文笔误）

- **位置**: p44 SETTINGS 表 "OXE DECT_OXE_CSA csa (physical) csm (main) **192.16.8.1.1 / 192.16.8.1.3**"；对照 p42 拓扑图应为 192.168.1.1 / 192.168.1.3。
- **判断**: 照排笔误（点号错位）；p42 拓扑、p51 预配置清单与 p146 DHCP 池（192.168.1.x）均为正常写法。
- **处置**: 引用实验地址一律以 p42 拓扑图 192.168.1.x 为准；能力卡只进 Boundary/overview 环境区并标注"实验口径"。候选 n21 已记录。

## nr-02 8328 的 NTP 示例两页不一致

- **位置**: p281 "NTP server: e.g **10.20.30.254**" vs p282 "Time server ... Here, in R-lab context: **192.168.1.252**"。
- **判断**: 两值都是实验口径（10.20.30.254 为公共区网关地址、192.168.1.252 为 IT Server/NTP），p282 明示 R-lab 语境；非规范值冲突。
- **处置**: 能力卡不给具体 NTP 值，只说"填客户 NTP 服务器"；实验值仅进 book/overview 环境区备查。候选 n21 已记录。

## nr-03 p182 手机固件手动下载 Note 表述不完整 + 笔误

- **位置**: p182 "the upgrade of the DECT handset must be **bone** manually"（应为 done）；且 Note 未写全参数名。p188/p189 重复注明真实语义：用户参数 "Exclude from automatic FW update" 设为 Yes 后，升级须手动经 downstat m 触发。
- **判断**: p182 单看会误读成"开自动反而要手动"；以 p188/p189 口径为准。
- **处置**: 能力卡按"排除自动（X/M 态）→ 手动 downstat m"表述；引用 p182 原文时标注"原文如此"。候选 n08 已记录。

## nr-04 DECT 频段双表口径交叉

- **位置**: p5 四段表（欧洲 1880-1900 / 中国 1900-1920 / 拉美 1910-1930 / 北美 1920-1930）vs p8 六地区表（含巴西例外 1910-1920、亚洲 1900-1906MHz）。
- **判断**: 两表口径部分重叠、部分互斥（亚洲 1900-1906 与中国 1900-1920 并存），原书未调和。
- **处置**: 两表并记、以部署国法规为最终依据；Station base type（如 DECT Europe）必须与所在频段一致（p144/p227）。能力卡引用时注明"双表口径"。候选 p01 已记录。

## nr-05 原文笔误与拼写若干（引用时保留并注明）

- p97 "supports **simultaneoulsly**"（应为 simultaneously）。
- p86 "Head **Quater**"（应为 Quarter）、p89 "**Additionnal** Site"（应为 Additional）。
- p4 "ETSI: European Telecommunication Standard Institute"（通行名为 European Telecommunications Standards Institute，原文如此）。
- p9 TDMA 展开为 "Temporal-Division Multiple Access"（通行表述为 Time-Division，原文如此）。
- **处置**: 原文引用保留原样；转述用正确拼写。

## nr-06 含推断成分的结论（引用需带标注）

- n02: "PLI 降位后老手机自动兼容新 PARI"——对满足逻辑 AND 的 PARI 对成立，书内未对全部机型逐一验证。
- n04: "两台全新 8328 同时入网时主站角色不确定"——书中只给判定规则（先声明 Extension 者），同时入网情形为推断。
- n13: "8328 电话本与 OXE 不集成，改名换号要维护两处"——由 p273 不集成事实引申的运维代价。
- n16: "Debug 级别常开影响基站性能"——影响程度书内未量化。
- n23: "放开 Alcatel-Lucent terminals only=NO 后 DHCP 池对任意设备开放"——安全面推断，需配合地址池规划。
- n26/n27: "跨簇 handover 受限""IBS 向 xBS 演进动机"——机制/动机推断。
- c05 步骤 4 "每 Site 一棵同步树，各站应为本 Site 的 Master"——由 p201 P+ 标志判读引申。
- **处置**: 全部保留"（推断）"标注，不升格为书中明示事实。

## nr-07 外部同步实验的 RSSI 正值表述口径

- **位置**: c13/p264 实验图用 "RSSI > 70 dB（强区）/ RSSI < 70 dB（切换区）"，与 p207-210 讲义的负 dBm 门槛（-70dBm/-60dBm/-80dBm）并存。
- **判断**: 实验图的正值是"距 -70dBm 门槛的强弱"简写（强区=信号强于门槛、切换区=接近门槛），非两种计量体系。
- **处置**: 能力卡统一按 -70dBm（话音门槛）/-80dBm（站间同步门槛）负值口径表述；引用实验图时注明原文写法。
