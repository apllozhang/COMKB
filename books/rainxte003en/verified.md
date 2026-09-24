# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f20（主验证对象）；principle p01-p28 / case c01-c14 / counter-example n01-n30 作为各单元的证据素材归并；glossary g01-g66 转 GLOSSARY（见 references.md），不进 verified
> 验证人: 主会话（2026-09-23），基于 314 页全文通读 + 提取器页码证据交叉核对

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 18 | f01, f04-f20（详见下表） |
| reference | 2 | f02（RLAB 平台结构）、f03（ITSP1 SIP 模拟器）——教学专用基础设施，仅作能力卡 Boundary 背景与 book/overview 素材 |
| needs_review | 0（单元级） | 断言级 6 项转 needs-review.md（nr-01..nr-06） |
| rejected | 0 | 无编造断言；五链路事件码、路由四案例、判别器五元组、监督组规格等关键数字逐格核对一致 |

verified 明细：f01, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——RLAB 地基、云侧体系、OXE 接入 RCC/路由、网关解锁 VoIP、话务台/维护/Teams
  type: framework
  V1: {passed: true, reason: "p1 扉页版本口径 + 全书 14 个 How-To 章序完整；p67 接入必要性总起句"}
  V2: {passed: true, check_mode: walkthrough, input: "新项目按什么顺序交付 OXE+Rainbow 集成", expected: "给出可执行的阶段顺序", observed: "九段主线与 c02-c14 章序互证：先云侧后 PBX、先 RCC/REX 路由后网关音频，无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线，避免先装网关后建云侧账户的倒置；证据归并 c02-c14"}
  decision: verified

- id: f04
  title: Rainbow 平台双定位全景（UCaaS + CPaaS + PBX 桥接一张图）
  type: framework
  V1: {passed: true, reason: "p20-23 全景图与文字定义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Rainbow 与 OXE 各管什么", expected: "PBX 保留呼叫控制，Rainbow 提供协作/路由意图", observed: "p23 客户端/通信层/PBX+网关三要素与 f12/f14 各章一致"}
  V3: {passed: true, expected_benefit: "方案沟通的架构底座；RCC/REX/网关各章的概念衔接点"}
  decision: verified

- id: f05
  title: 8 种订阅计划体系与电话服务付费门槛分层
  type: framework
  V1: {passed: true, reason: "p24 八种订阅逐一定义；p56 电话门槛三选一"}
  V2: {passed: true, check_mode: walkthrough, input: "客户要话音+话务台+会议室怎么组合", expected: "Business/Enterprise+Attendant+Room 组合", observed: "p24 各订阅定位支持组合决策；p133/p129 网关档位一致"}
  V3: {passed: true, expected_benefit: "售前选型矩阵；证据归并 p01/n01/n03"}
  decision: verified

- id: f06
  title: Rainbow 网络要求文档体系（支持页 + 两份 PDF 的结构）
  type: framework
  V1: {passed: true, reason: "p26-31 文档结构逐一列出"}
  V2: {passed: true, check_mode: walkthrough, input: "上线前网络前提查哪里", expected: "支持页文章 + Network Requirements PDF", observed: "p27/p31 指针明确；书内无私有数值（诚实外置，n02）"}
  V3: {passed: true, expected_benefit: "task-01 的执行入口；Boundary 指针成立"}
  decision: verified

- id: f07
  title: Rainbow Pilot 连通性与承载容量评估流程
  type: framework
  V1: {passed: true, reason: "p32-36 工具用途与入口"}
  V2: {passed: true, check_mode: walkthrough, input: "站点能否承载一批混合用法用户", expected: "按协作/会议/混合话音/Hub 配比评估", observed: "p33 评估维度明确；p34 截图标注 To come（分区随版本演进）"}
  V3: {passed: true, expected_benefit: "售前勘测工具入口；证据归并 p02/n02"}
  decision: verified

- id: f08
  title: Company 概念体系（两类公司、经销角色链、可见性、公司要素与建司六步）
  type: framework
  V1: {passed: true, reason: "p37-46 概念页完整；p39 BP 专属两项"}
  V2: {passed: true, check_mode: walkthrough, input: "客户管理员为何建不了 PBX", expected: "BP 专属权限解释", observed: "p39 Declaration & PBX / paid subscriptions 两项专属；n07 与 p161 讲师代做互证"}
  V3: {passed: true, expected_benefit: "权责切分依据，减少误判故障；证据归并 p03-p05/n06-n08"}
  decision: verified

- id: f09
  title: 管理员角色分工与企业目录/信息频道两个管理面
  type: framework
  V1: {passed: true, reason: "p47-53 两级权责清单 + 两管理面定义"}
  V2: {passed: true, check_mode: walkthrough, input: "多管理员怎么授权、外部联系人怎么进来", expected: "Roles 页签可设多名；目录手工或 CSV", observed: "p50 Roles 明确；p51 CSV 含样本与报告；n06/n09 门槛与代价齐备"}
  V3: {passed: true, expected_benefit: "管理团队规划与来话识别落地路径"}
  decision: verified

- id: f10
  title: 订阅开通与分配两段式流程（BP 开通、管理员分配）
  type: framework
  V1: {passed: true, reason: "p54-59 两层流转与表单要素"}
  V2: {passed: true, check_mode: walkthrough, input: "订阅买多了能给别的公司用吗", expected: "订阅先开到公司再内部分配", observed: "p55 两段式明确；p57 培训月付口径（n03）一并验证"}
  V3: {passed: true, expected_benefit: "许可运营与计费口径；证据归并 p01/p09/n01/n03"}
  decision: verified

- id: f11
  title: 集成 Rainbow Agent 接入架构与五条链路
  type: framework
  V1: {passed: true, reason: "p67-68 接入定义 + p87 incvisu 输出"}
  V2: {passed: true, check_mode: walkthrough, input: "接入后怎么确认链路健康", expected: "五条链路全部 in service", observed: "p87 五事件码 4503/4505/4509/4507/4511 与 c04 步骤一致"}
  V3: {passed: true, expected_benefit: "混合闭环第一关口的操作与排障抓手；证据归并 p26/c03/c04/n10-n12"}
  decision: verified

- id: f12
  title: OXE 用户使用 Rainbow 的形态矩阵（RCC / REX 路由 / 纯 REX / DECT 特例）
  type: framework
  V1: {passed: true, reason: "p106-118 四形态讲义 + p139 DECT 特例"}
  V2: {passed: true, check_mode: walkthrough, input: "只有 DECT 话机的用户怎么上 Rainbow", expected: "Virtual UA + multi-devices，且有 RCC 代价", observed: "p139 三步路径与两个代价明确；n14 一致"}
  V3: {passed: true, expected_benefit: "架构决策依据（选错形态代价最高）；证据归并 p10/p14/n13/n14"}
  decision: verified

- id: f13
  title: REX/Ghost Z/Tandem 机制图（Rainbow agent 自动改写路由载体）
  type: framework
  V1: {passed: true, reason: "p111-113 机制图 + p122-125 配置证据连贯"}
  V2: {passed: true, check_mode: walkthrough, input: "REX 并发上不去先查什么", expected: "Ghost Z 池大小=并发上限", observed: "p111 池语义与 p122 每并发一个 Ghost 一致；c06 配置可复现"}
  V3: {passed: true, expected_benefit: "路由与网关两章的共同地基；证据归并 p11-p13/c06/n20"}
  decision: verified

- id: f14
  title: WebRTC 网关角色、部署形态与配置三块全景
  type: framework
  V1: {passed: true, reason: "p131-136 角色/媒体流/前提/三块清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "网关坏了影响呼叫控制吗", expected: "不影响——呼叫控制在 PBX", observed: "p133 媒体流边界清晰；p135 前提与 p154 Warning 互证"}
  V3: {passed: true, expected_benefit: "排障分流（媒体面 vs 呼控面）的概念依据；证据归并 p15/p27/c07/n15-n17"}
  decision: verified

- id: f15
  title: 共享可扩展 WebRTC 网关池（三配置对比与 406 溢出机制）
  type: framework
  V1: {passed: true, reason: "p146-150 三配置与溢出规则完整"}
  V2: {passed: true, check_mode: walkthrough, input: "网关池满了会怎样", expected: "回 SIP 406，OXE 溢出到 ARS 下一条路由", observed: "p149 原文一致；参数为空则 SIP trunk 限制生效（n27）"}
  V3: {passed: true, expected_benefit: "规模化的核心架构决策；证据归并 p19-p21/n27"}
  decision: verified

- id: f16
  title: 网关容量估算流程（TBE067 工具 + 400 并发上限 + 压缩器推算）
  type: framework
  V1: {passed: true, reason: "p151 工具四输入与上限口径"}
  V2: {passed: true, check_mode: walkthrough, input: "N 个用户要配多少并发通道", expected: "按四输入跑 TBE067 得通道数", observed: "p151 四输入与 400 上限明确；与 OXO 版查表口径不同已核对"}
  V3: {passed: true, expected_benefit: "售前报价与交付容量依据；证据归并 p20/g61"}
  decision: verified

- id: f17
  title: 4059EE 话务台 + Rainbow 集成结构（话务组/话务台/CDT/BLF）
  type: framework
  V1: {passed: true, reason: "p198-205 概览 + p208-215 实验证据连贯"}
  V2: {passed: true, check_mode: walkthrough, input: "话务台要配订阅吗", expected: "4059EE 不需要 Attendant 订阅", observed: "p200 原文明确（n24）；p209 关联话机非 multi-line 约束一致"}
  V3: {passed: true, expected_benefit: "前台/秘书场景（OXE 传统线）交付依据；证据归并 p24/c10/n20-n22/n24/n26"}
  decision: verified

- id: f18
  title: Rainbow Attendant Console 界面结构与监督组/互助组体系
  type: framework
  V1: {passed: true, reason: "p225-237 界面分区与规格数字齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "软话机用户的呼叫能被代接吗", expected: "不能——代接仅限 PBX 电话呼叫", observed: "p234 原文明确（n23）；p230 规格 5/30、p235 4 路一致"}
  V3: {passed: true, expected_benefit: "前台/秘书场景（Rainbow 线）与互助值班方案依据；证据归并 p22/p23/c11/n23/n24"}
  decision: verified

- id: f19
  title: 维护与支持体系五入口（日志/上报/状态/告警/SR）
  type: framework
  V1: {passed: true, reason: "p245-257 五入口逐一定义"}
  V2: {passed: true, check_mode: walkthrough, input: "用户说 Rainbow 全挂了先查什么", expected: "status.openrainbow.com + 订阅告警分流", observed: "p249 状态页与告警订阅明确；p254 ESR 认证前提（n29）"}
  V3: {passed: true, expected_benefit: "售后运维闭环抓手清单；证据归并 p28/n29/n30"}
  decision: verified

- id: f20
  title: Microsoft Teams 集成架构与三步部署（工作站级）
  type: framework
  V1: {passed: true, reason: "p258-273 组件分工 + 四条呼叫流 + 部署三步"}
  V2: {passed: true, check_mode: walkthrough, input: "Teams 里打外线走哪条路", expected: "MakeCall、计算机 VoIP、WebRTC 网关、公网", observed: "p264-266 流程与 p259 workstation-level 定位一致；p274-284 为重复讲解（nr-05）"}
  V3: {passed: true, expected_benefit: "Teams 共存方案技术底座；证据归并 p25/c12-c14/n25"}
  decision: verified
```

## 断言级裁决记录

1. **case 提取器"incvisu/invisu 写法不一"**：成立。p26 引文出现 "Use 'invisu' command"，c04 步骤与 p87 输出均为 incvisu——判为 OCR 变体，以 incvisu 为准；详见 needs-review nr-02。
2. **版本号双轨口径**：成立并如实记录。网关前提写 "OXE release 12.1 MD4, 12.2 or later"（p135），sizing 工具适用写 "OXE 101.0 MD3 and WebRTC 3.x"（p151）——属 ALE 新旧版本命名体系并存，非矛盾；引用保留原文双口径，见 nr-03。
3. **counter-example 提取器"user2 姓名前后不一"**：成立（n26）。p64 登记为 Rains Robby，p216 又建为 Betty Carol，书内未解释；推断为不同实验沿用同一邮箱模板，见 nr-01。
4. **"RCC 用户呼叫纯 Rainbow 用户不通"**：书中以测试问题呈现（p92-93）未给答案，"不通"为机制推断（无网关即无音频通路），引用需带推断标注，见 nr-04。
5. **无 rejected 断言**：五链路事件码（4503/4505/4509/4507/4511）、路由四案例、判别器五元组（Call Number 1/Area 1/route list/schedule -1/17 位）、监督组 5/30、队列 OXE 10/OXO 8、互助 4 路、REX 10/Anydevice 8、单网关 400 并发流、10 天宽限、密码 12+3 类字符、溢出计时器 100ms 步进——全部与原文逐格一致。
