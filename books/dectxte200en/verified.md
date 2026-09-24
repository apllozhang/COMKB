# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f18（主验证对象）；principle p01-p30 / case c01-c14 / counter-example n01-n28 作为各单元的证据素材归并；glossary g01-g56 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 298 页全文通读 + 源文本 grep 逐格抽查（p27 容量表、p208-210 RSSI 门槛、p244 PLI=30、p252 机型版本表、p253 重注册性能、p146 vendor class、p288 主站判定、p150 换站 RPN、p272 8328 容量、p196 >1km、p291 双小区 5 分钟等全部与原文一致）

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 16 | f01-f06, f09-f18 |
| reference | 2 | f07（RLAB POD 结构）、f08（ITSP1 SIP 模拟器）——教学专用基础设施，仅作实验口径背景 |
| needs_review | 0（单元级） | 断言级 4 项转 needs-review.md（数值笔误、NTP 双例、参数名表述、频段双表） |
| rejected | 0 | 无编造断言；p27 容量表与 p252 版本表逐格核对一致 |

verified 明细：f01, f02, f03, f04, f05, f06, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18

## 验证记录

```yaml
- id: f01
  title: 全书课程推进主线——DECT 底座 → 实验环境 → IP-xBS 全套 → IBS/混合 → 重注册/外部同步 → SIP-DECT
  type: framework
  V1: {passed: true, reason: "p3-298 模块页序完整；p51 Hybrid Mode 与 p279 SIP-DECT 目录定位句明确"}
  V2: {passed: true, check_mode: walkthrough, input: "新工程师按什么顺序学 OXE DECT 交付", expected: "给出可跟随的课程与交付顺序", observed: "十段主线与各 How-To 章位置互证：先懂空口与标识号码、再配 IP 基站、后补 TDM 与低成本支线，顺序无矛盾"}
  V3: {passed: true, expected_benefit: "学习路径基线，book/overview 六步主线的骨架"}
  decision: verified

- id: f02
  title: DECT 产品线三分结构——TDM IBS / 全 IP IP-xBS / SIP-DECT
  type: framework
  V1: {passed: true, reason: "p7 DECT offer 框图原文完整；p27 容量表、p272 SIP-DECT 特性页支撑"}
  V2: {passed: true, check_mode: walkthrough, input: "小站点低成本上 DECT 选哪条线", expected: "按站点规模/存量硬件/加密诉求分流", observed: "p7 三分框图 + p27 容量表（IBS 3/6 话、xBS 11 话）+ p272（8328 每站 20 手机）支持选型决策；p7 脚注明示 SIP-DECT 不适用 PARI/PLI 语义"}
  V3: {passed: true, expected_benefit: "售前选型第一步的判断依据；证据归并 p04/p28/n01/n12-n14"}
  decision: verified

- id: f03
  title: DECT 无线底座图——频段 × FDMA/TDMA/TDD × 10ms 帧结构
  type: framework
  V1: {passed: true, reason: "p5/p8 频段与射频参数、p9-12 复用与帧结构逐页完整"}
  V2: {passed: true, check_mode: walkthrough, input: "IBS 与 xBS 容量差异的物理来源是什么", expected: "能从帧结构解释", observed: "p8 原文 IBS 收发各 6 时隙、xBS 收发各 12 时隙，与 p27 容量表（3/6 话 vs 11 话）互证；120 复用信道=10 载波×24 时隙口径成立"}
  V3: {passed: true, expected_benefit: "一切容量与覆盖数字的物理口径；证据归并 p01-p03"}
  decision: verified

- id: f04
  title: 标识号码体系图——PARI/RPN/RFPI/PARK/PLI/IPUI 与逻辑 AND 匹配
  type: framework
  V1: {passed: true, reason: "p14-22 六号码定义与两个 AND 算例完整；p17 PARK 算例原文在案"}
  V2: {passed: true, check_mode: walkthrough, input: "PLI=31 且 PARI=10000400100 时手机里的 PARK 是多少", expected: "3110000400100", observed: "p17 原文算例逐位一致；p18-20 PLI 降位（29）使末位不同 PARI 等效的机制自洽"}
  V3: {passed: true, expected_benefit: "全书包内配置字段（PARI Value/PLI/AC）的语义来源；证据归并 p05-p08/n02"}
  decision: verified

- id: f05
  title: Roaming 定位流程与 Handover 三阶段
  type: framework
  V1: {passed: true, reason: "p23-26 定位阶段与切换三步原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "为什么 handover 要求基站间精确同步", expected: "帧级同步是切换前提", observed: "p25 原文 all the base station must start their DECT frame at exactly the same time；与 p87 同 Site 才有 handover、p93 同 Data Sync Primary 才可切换三层约束一致"}
  V3: {passed: true, expected_benefit: "同步体系（f13）存在的理由陈述；证据归并 g03-g05"}
  decision: verified

- id: f06
  title: DECT 安全三级与 UAK/AC/DCK 密钥体系
  type: framework
  V1: {passed: true, reason: "p35-37 三级定义、p36 密钥派生链、p37 硬件限制表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户要求 DECT 加密，IBS 存量网能不能满足", expected: "不能——加密仅 IP-xBS 支持", observed: "p37 Encryption is not available for IBS Base Stations on Common Hardware；p36 AC 不一致则注册不可能成立，密钥三层（AC/UAK 128 位/DCK 64 位）链路自洽"}
  V3: {passed: true, expected_benefit: "售前一票否决项与注册排障口径；证据归并 p09/n01"}
  decision: verified

- id: f07
  title: RLAB 培训平台 POD 结构——POD 池 + 课堂硬件 + 公共资源区
  type: framework
  V1: {passed: true, reason: "p40-45 拓扑与 SETTINGS 表在案（含 p44 点号错位笔误，见 needs-review nr-01）"}
  V2: {passed: true, check_mode: walkthrough, input: "实验环境里 OXE/OMS/NTP/DHCP 的地址约定", expected: "给出一套自洽的实验值", observed: "p42 拓扑与 p51 预配置清单互证（192.168.1.x 实验口径）；仅为教学基础设施，生产环境无一对应关系"}
  V3: {passed: true, expected_benefit: "仅作 book/overview 实验环境背景与 Boundary 口径，不独立成卡"}
  decision: reference

- id: f08
  title: ITSP1 SIP 运营商模拟器拓扑与 POD 号码变换规则
  type: framework
  V1: {passed: true, reason: "p48-49 模拟器地址与 DDI 变换规则在案"}
  V2: {passed: true, check_mode: walkthrough, input: "实验中外呼号码怎么拼", expected: "按 POD 号变换", observed: "p49 规则 3321PN + DDI 段自洽（POD 3 → 33210341002，实验口径）；与 DECT 主线解耦，仅用于中继环路验证"}
  V3: {passed: true, expected_benefit: "仅作实验环境背景；号码格式不可套用于生产"}
  decision: reference

- id: f09
  title: 8378 IP-xBS 方案全景——系统特性/网络特性/OXE 兼容性
  type: framework
  V1: {passed: true, reason: "p57-64 特性清单三块完整；p60 容量与版本口径明确"}
  V2: {passed: true, check_mode: walkthrough, input: "IP-xBS 部署的版本与网络前提是什么", expected: "OXE R12.2+、IPv4、PoE 供电", observed: "p59 IPV4 (IPV6 hardware ready, not yet applicable)、PoE Class 2 only；p60 R12.2 minimum、2032 台/8 PARI/254 台每 PARI 逐格一致"}
  V3: {passed: true, expected_benefit: "部署前置核查清单的底表；证据归并 p10/n15"}
  decision: verified

- id: f10
  title: IP-xBS 流量模型——UA/UDP 单播信令 + RTP 直达媒体 + 连接切换中继
  type: framework
  V1: {passed: true, reason: "p71-74 流量图与机制句完整"}
  V2: {passed: true, check_mode: walkthrough, input: "切换时媒体经不经过 Call Server", expected: "不经过——基站间建 IP 中继", observed: "p74 原文 Call Server 只与初始基站（Relay xBS）保持信令媒体连接、子系统自管 Connection Handover、媒体在基站间重路由；p71 无组播仅单播、p72 DECT/UA/UDP/IP 桥语义一致"}
  V3: {passed: true, expected_benefit: "QoS/带宽规划与媒体面排障分流的依据；证据归并 g17/g35/g37"}
  decision: verified

- id: f11
  title: 管理对象四级层级——PARI → RPN → Location Area → Site
  type: framework
  V1: {passed: true, reason: "p81-92 四级对象逐页定义"}
  V2: {passed: true, check_mode: walkthrough, input: "跨 Site 的手机还能用吗", expected: "可 roaming 无 handover", observed: "p87 Handover is only available on a same site、p88 Roaming is possible between sites 原文两图对照成立；p84-85 每位置区按 RPN 区间划分（每 PARI 最多 64 个）"}
  V3: {passed: true, expected_benefit: "组网分区与切换边界的判定骨架；证据归并 p11/g06/g07"}
  decision: verified

- id: f12
  title: Data Sync Primary 与 IP 中继切换机制（含容量）
  type: framework
  V1: {passed: true, reason: "p93-97 定义、五步机制、容量句完整"}
  V2: {passed: true, check_mode: walkthrough, input: "两台基站什么条件下才能互相切换", expected: "同一 Site 且同一 Data Sync Primary", observed: "p93 原文 One Data Sync Primary for every couple Site/PARI + Handover is only possible between base stations with the same Data Sync Primary；p97 11 通话+11 IP 中继、切换瞬时双链路占两份资源"}
  V3: {passed: true, expected_benefit: "dectview xbs P/M/B 标志判读与容量测算依据；证据归并 g22"}
  decision: verified

- id: f13
  title: 空中同步体系——Internal Sync / Sync Master / Sync Cluster / External Sync / Sync Highway
  type: framework
  V1: {passed: true, reason: "p98-116 五件套逐页完整；p75 同步树 24 级上限在案"}
  V2: {passed: true, check_mode: walkthrough, input: "多于 2 个 PARI 同步怎么配", expected: "需要 Sync Highway", observed: "p111-112 additional configuration is needed: a synchronization highway、p141 决策树 More than 2 PARI? Use SYNC HIGHWAY；p106 Sync Master 不承载通信、Backup 强制；p102 每 Site/PARI 最多 8 簇默认 Cluster 0"}
  V3: {passed: true, expected_benefit: "切换质量保障的配置主线；证据归并 p12/p13/n06/n07/n26"}
  decision: verified

- id: f14
  title: IP-xBS 开通总流程与工程规则决策树（简单/复杂部署）
  type: framework
  V1: {passed: true, reason: "p125-141 四步主流程、启动时序、决策树完整"}
  V2: {passed: true, check_mode: walkthrough, input: "极简部署的最小配置集是什么", expected: "1 PARI/1 位置区/1 Site/1 簇 + 默认参数", observed: "p140 Easy deployment 原文支持；p141 决策树四分支（分支办公→Site、>2 PARI→Highway、覆盖不全→Cluster、>254→External sync）逐条对上"}
  V3: {passed: true, expected_benefit: "交付工时估算与方案分级的骨架；证据归并 c02"}
  decision: verified

- id: f15
  title: OXE 配置菜单路径总表——PWT/DECT System 配置树
  type: framework
  V1: {passed: true, reason: "p143-291 各 How-To 菜单路径在案（xBS/IBS/用户/8328 域）"}
  V2: {passed: true, check_mode: walkthrough, input: "外部同步在哪个菜单配", expected: "PWT/DECT System / xBS system / xBS Site / External Synchronization", observed: "p266 原文路径一致；p144-145 全局参数、p228-230 IBS 域路径抽查一致"}
  V3: {passed: true, expected_benefit: "全部操作卡菜单路径的母表；8328 例外（OXE 侧仅建 SIP Extension）已标注"}
  decision: verified

- id: f16
  title: 固件双轨升级架构——基站 downstat x 后台下载 / 手机 downstat m 空中 FWU
  type: framework
  V1: {passed: true, reason: "p129-133 基站轨、p179-183 手机轨原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "基站固件下载会不会中断业务", expected: "不会——后台下载到 RAM、空闲时重启", observed: "p130 原文 background 下载 + idle 时重启；p131 最低版本 v73b0003；p179 语音优先于下载、回充电座切换新版本（手机轨）；downstat x 四项菜单 p132 逐项一致"}
  V3: {passed: true, expected_benefit: "版本治理双轨操作与窗口规划；证据归并 p17/p21/p22/n08/n09"}
  decision: verified

- id: f17
  title: 六种支持拓扑清单（xBS 单线/分支/混合 × 组合）
  type: framework
  V1: {passed: true, reason: "p191-198 六拓扑图与四格能力图例完整"}
  V2: {passed: true, check_mode: walkthrough, input: "IBS 区与 xBS 区建不了外部同步怎么办", expected: "区域间距必须 >1km", observed: "p196 原文 the distance between the area must be > 1km；p193 单线 8 PARI/2032 台、p195 混合同站 +256 IBS、p198 多节点仅 roaming+跨节点外部切换"}
  V3: {passed: true, expected_benefit: "拓扑选型的判定基准；证据归并 n19"}
  decision: verified

- id: f18
  title: 8328 SIP-DECT 注册四步流程与双小区（Dual Cell）机制
  type: framework
  V1: {passed: true, reason: "p277-278 四步注册链、p288 双小区机制原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "双小区谁是主站", expected: "先声明 Extension 的那台", observed: "p288 大写 WARNING 逐字核对一致（THE PRIMARY STATION WILL BE THE STATION WITH ALREADY AT LEAST ONE EXTENSION DECLARED）；Note 补充仅声明 Extension 即可确立主站、无需注册手机；p291 链路建立约 5 分钟"}
  V3: {passed: true, expected_benefit: "低成本支线的完整施工与角色判定；证据归并 p28/p29/n04/n12-n14/n23-n25"}
  decision: verified
```

## 断言级裁决记录

1. **principle 提取器"混合模式必须降 PLI"**：成立。p227 大写 WARNING 原文在案（IN CASE OF MIXED MODE, SO WITH MULTI PARI NUMBERS, THE PLI MUST BE ADAPTED）；p244 实验取 PLI=30（IBS PARI 100004101x0 与 xBS PARI 100004101x4 仅末位不同），与 p18-20 的 PLI 位数语义自洽。
2. **counter-example 提取器"换站必须手动注册保 RPN"**：成立。p150 原文自动注册按首个空闲 RPN 分配且 may be different，依赖 RPN 的告警与地理定位会失准；与 c03 操作序列一致。
3. **counter-example 提取器"外部同步主备皆失无自动恢复"**：成立。p109 原文 no automatic recovery of the whole synchronization (will be improved in a future release)，属 R101.1 MD4 时代产品欠账，如实入册（n06）。
4. **无 rejected 断言**：p27 容量表（3 or 6/11、1/8、256/254、256/2032）、p208-210 RSSI 三门槛（-70/-60/-80）、p252 机型版本表（8262 v5580b0007/v5680b0005、8262 Ex v7381b0009、82x4 无最低版本）、p253 性能口径（2-3s/1,3s/6,5s/800ms）、p272 8328 容量（20 手机、G.711 10 路、G.729 4 路）均与原文逐格一致。
