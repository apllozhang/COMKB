# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 镜像会话数两处口径不一（新旧口径矛盾）

- **位置**: p249 讲义 "the maximum port-mirroring sessions has been increased from 2 to 4"（另有 4 个 MTP 索引限制、双向计 2）vs p265 实验注释 "The maximum number of mirroring sessions is limited to two"。
- **差异**: 同一参数两页答案不同；实验注释为旧版本口径残留。
- **处置**: 能力卡按较新规格口径取 4 执行，Boundary 注明双口径；现场以 show port-mirroring 实测与 Specification Guide 为准，老版本设备按 2 规划。候选 p35/n40 已完整记录。

## nr-02 LLDP-MED 两页示例数值不一致

- **位置**: p496 `lldp network-policy 1 application voice vlan 151 l2-priority 5 dscp 46` vs p499 同命令 `l2-priority 7 dscp 14`。
- **差异**: 同一语音网络策略两页取值不同（推断为不同版本截图残留，教材未解释）。
- **处置**: 保留两处原文不改；能力卡引用时注明"教材示例不一致"；生产取值按企业 QoS 规划（常见语音 EF=DSCP 46），逐台 show lldp config 核查实配。不编造统一值。

## nr-03 UNP 全称两写（同一概念）

- **位置**: p393 "User Network Profile" vs p456/p477 "Universal Network Profile"。
- **判断**: 两处全称并存指向同一概念（认证后下发的网络档案），原文如此。
- **处置**: glossary g13 如实并列；能力卡正文用 "UNP" 缩写避免二义，首次出现可注"书中全称两写"。

## nr-04 console 默认速率两处口径（验证新发现）

- **位置**: p76 幻灯 "Default settings Speed (baud): 115200 ... Note: the configuration for the latest generation 6900, 6870 and 6860N switches is different" vs p523-527 分代表表（Legacy 与 OS6860/6860E、OS6900 T20/T40/X20/X40/X72/Q32 为 9600；OS6900 V72/C32/X48C6/T48C6/V48C8、OS6860N/OS6870 为 115200）。
- **差异**: p76 以 115200 为"默认"，分代表表则多数机型 9600——表述视角不同（新机型页 vs 全系表）。
- **处置**: 以"按型号查分代表表"为准确口径；能力卡给出分代表结论，不沿用 p76 的单一默认值。

## nr-05 教材思考题留白与推断补齐（引用需带标注）

- **位置**: p317 "What determines which side of the link is blocking?"、p296 "How are the Clients VM exchange between each other (Layer 2 or Layer 3)?"、p319 "Has our Topology age changed?"——教材以开放式提问收尾、不提供标准答案。
- **判断**: n54 的补齐答案（阻塞侧=根路径成本→发送者桥 ID→端口 ID 逐级比较；Client 间流量走三层）为推断，教材原文未给。
- **处置**: 能力卡引用时保留"（推断）"标注，不升格为书中明示事实；做考核题库时自行补答案。

## nr-06 R-Lab 浏览器推荐表述不一致（原文如此）

- **位置**: p14 标题行 "Recommended web browsers: Chrome / Edge" 与 Notes 行 "We recommend to use Google Chrome or Firefox"。
- **判断**: 两行推荐列表不同（Edge vs Firefox），实际意图为"避免 Firefox 复制粘贴兼容问题"。
- **处置**: 保留原文；转述以"Chrome/Edge 优先、Firefox 有复制粘贴 workaround"口径。

## nr-07 实验环境双凭据与非空预置配置（环境值仅进 Boundary）

- **位置**: p15 交换机凭据 admin/Superuser=1 vs p38 SSH 账号 admin-netadv@10.4.X.Y / Superuser01!；p92 明示实验交换机为"最小化配置、非空"（预置到管理网的静态路由）；p286 预置聚合 17/78。
- **处置**: 全部标注"实验口径"，只落位 references.md 第 4 节与 book/overview 环境区及卡片 Boundary；不进卡片正文，不当产品默认值引用。

## nr-08 实验镜像版本混杂（历史截图残留）

- **位置**: p141 实验镜像 8.10.9.R04；p504 LLDP System Description 截图残留 8.7.98.R03；BOOK_OVERVIEW 版本来源已注明。
- **处置**: 数值口径（LLDP 运行参数等）标注"该版本口径"；与 R8 当前版本可能漂移的参数以 Specification Guide 为准。版本号一律保留原文完整位数（8.10R03/8.10R04、8.7R3、8.9R1、8.9R3、8.9R4、8.10R4、8.10.9.R04、8.7.98.R03、18.1）。
