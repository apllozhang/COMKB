# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f24（主验证对象）；principle p01-p22 / case c01-c20 / counter-example n01-n41 作为各单元的证据素材归并；glossary g01-g46 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 649 页全文页码标记抽查 + 提取器证据交叉核对（p44/p47/p53/p117/p163/p165/p168/p214/p359/p371 区间/p377/p382/p455/p528/p545/p546/p611/p616/p71-73 逐段回原文核对）

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 22 | f01, f04-f24（详见验证记录） |
| reference | 2 | f02（RLAB 平台结构）、f03（ITSP1 SIP 模拟器）——纯实验基础设施，仅作 Boundary 背景不进能力卡正文 |
| needs_review | 0（单元级） | 断言级 10 项转 needs-review.md（口令矛盾、建队列表格缺陷、acdsup/acdsetup、ABC-F 版本基线、语言索引等） |
| rejected | 0 | 无编造断言；容量上限族、EWT 公式、518 播报规则、日历容量等关键数字逐格核对一致 |

verified 明细：f01, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——环境 → CCD 模型 → 基础矩阵 → CCS 工具 → 规则与人员 → 调优与增值域
  type: framework
  V1: {passed: true, reason: "p3-649 章节推进逐段可查；p21/p23 产品定位句完整"}
  V2: {passed: true, check_mode: walkthrough, input: "新工程师按什么顺序交付 OXE 内置呼叫中心", expected: "环境→模型→矩阵→CCS→规则人员→调优增值的可执行顺序", observed: "五段主线与 20 个 How-To 章序一致，c01-c20 映射无断点"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线；证据归并 c01-c20 收尾自检表"}
  decision: verified

- id: f04
  title: CCD 矩阵总模型——Pilot → Call Routing → Waiting Queue → Call Distribution → Processing Group
  type: framework
  V1: {passed: true, reason: "p22-29/p40 模型图与文字定义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "来话从公网打进到座席摘机经过哪些对象", expected: "pilot→路由→队列→分配→PG→座席", observed: "p24 双维度（路由看优先级+EWT、分配看可用性+优先级+LIT）与 c03 实验互证"}
  V3: {passed: true, expected_benefit: "全书智力骨架，一切配置与排障的共同语言；证据归并 p01/n40"}
  decision: verified

- id: f05
  title: Pilot 三态机——Open / General Forwarding / Blocked 与触发来源
  type: framework
  V1: {passed: true, reason: "p26 三态定义与触发来源单处完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户说没动配置但客户打不通", expected: "末座席登出→下游无资源→pilot 自动 Blocked", observed: "p26/p28 Blocked 自动态定义直接回答；n40 一致"}
  V3: {passed: true, expected_benefit: "路由规则 Normal/FWD/Blocked 三张表的存在依据；证据归并 n40/n05/n34"}
  decision: verified

- id: f06
  title: 等待队列三类型与四状态——Normal / Intelligent Overflow / Redirection
  type: framework
  V1: {passed: true, reason: "p27-28 规格、类型、状态齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "队列饱和后呼叫去哪", expected: "EWT>最大等待时间即 Saturated，来话走下一优先级方向", observed: "p28/p47-48 与 p02 公式互证；c07 队列参数实验落位"}
  V3: {passed: true, expected_benefit: "容量上限 30 pilot/50 PG 是扩容设计的硬边界；证据归并 p03/p02"}
  decision: verified

- id: f07
  title: Processing Group 五类型与队列-PG 兼容矩阵
  type: framework
  V1: {passed: true, reason: "p29 五类型逐一定义；p40 兼容表"}
  V2: {passed: true, check_mode: walkthrough, input: "语音指南组能挂普通队列吗", expected: "不能——Voice Guide PG 只接 Redirection 队列", observed: "p40 兼容矩阵支持；c01/c03 基准矩阵 Normal→Agent、Overflow→Forwarding、Redirection→Voice guide 互证"}
  V3: {passed: true, expected_benefit: "建矩阵前选型的硬约束；证据归并 n01"}
  decision: verified

- id: f08
  title: 路由规则结构——每 pilot 最多 30 条规则、方向优先级 0-9、6 级 parking level
  type: framework
  V1: {passed: true, reason: "p43-50 结构完整；p103/p110 数值复现"}
  V2: {passed: true, check_mode: walkthrough, input: "一个 pilot 挂多少队列、优先级怎么填", expected: "30 方向/pilot（全局 1200）；0 最高 9 最低", observed: "p44/p103 原文与 p01 语义一致；c08/c11 parking level 实验落位"}
  V3: {passed: true, expected_benefit: "路由设计的参数域；证据归并 p01/p03/c03"}
  decision: verified

- id: f09
  title: 分配规则结构——10 条上限、资源选择与呼叫选择双机制
  type: framework
  V1: {passed: true, reason: "p51-59 双机制定义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "同优先级两个 PG 都空闲给谁", expected: "资源选择看 PG 最长空闲时间 LIT", observed: "p53 原文明确；呼叫选择平局看队首真实等待时间（p53/p58）与 p01 一致"}
  V3: {passed: true, expected_benefit: "分配口径排障的依据；PLTR 未展开已如实记录（见 needs-review nr-10）；证据归并 p01/n01/n02"}
  decision: verified

- id: f10
  title: 座席状态时序图——free → ringing → conversation → wrap-up → pause 循环
  type: framework
  V1: {passed: true, reason: "p275-280 时序与计时器归属完整"}
  V2: {passed: true, check_mode: walkthrough, input: "座席挂机后状态怎么走、wrap-up 中按键会怎样", expected: "自动 wrap-up（pilot 计时器）→pause；wrap-up 中做操作即取消（Queue info 除外）", observed: "p278/p279 原文支持；c07 wrap-up/pause 实测 10s/5s 互证"}
  V3: {passed: true, expected_benefit: "座席状态类工单的共同语言；证据归并 p06/n38"}
  decision: verified

- id: f11
  title: Rainbow CCD 座席三种登录方式图——Office phone / Other phone (REX) / Computer (WebRTC)
  type: framework
  V1: {passed: true, reason: "p34-37 三登录形态与三不限制齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "远程座席要 VPN 吗", expected: "不要——Rainbow 不需要 VPN/SBC", observed: "p34 原文明确；computer 方式依赖 WebRTC 网关（p37）"}
  V3: {passed: true, expected_benefit: "远程座席方案的选型边界；证据归并 p19/n39"}
  decision: verified

- id: f12
  title: 双控制台分工图——OXE Web Admin 管对象与系统项，CCS 管规则/座席/实时/统计
  type: framework
  V1: {passed: true, reason: "p79 权责句 + p113 激活分工"}
  V2: {passed: true, check_mode: walkthrough, input: "在 CCS 里为什么建不了 pilot", expected: "设计如此——CCS 无权创建 CCD 对象，只能建班长与分配规则", observed: "p79 原文直接回答；n20 一致；c03 分配规则必须回 OXE 激活互证"}
  V3: {passed: true, expected_benefit: "工单分派与权限设计的硬边界；证据归并 n20/n02"}
  decision: verified

- id: f13
  title: OXE Web Admin 菜单地图——实验涉及的全部路径
  type: framework
  V1: {passed: true, reason: "p65-77 至 p626 各章 Select 路径可查"}
  V2: {passed: true, check_mode: walkthrough, input: "建 ACD 前缀、COS 放行、DID 翻译分别走哪个菜单", expected: "Translator>Prefix Plan、Classe of Service>Phone Features COS、Translator>External Numbering Plan", observed: "p66/p134/p154 与 c01/c04/c05 步骤一致"}
  V3: {passed: true, expected_benefit: "OXE 侧操作锚点全集；p153 口令矛盾已转 nr-01；证据归并 c01-c20"}
  decision: verified

- id: f14
  title: CCS 主菜单地图——Call Flow mgt / Configurations / System / Real time / Statistics / Window
  type: framework
  V1: {passed: true, reason: "p99-641 各章 From the main menu 路径可查"}
  V2: {passed: true, check_mode: walkthrough, input: "建规则、调 pilot、看实时、出报表分别进哪个菜单域", expected: "Call Flow mgt / Configurations / Real time / Statistics>Excel", observed: "p99/p103/p143/p519 引句与 c03/c07/c13/c15 一致"}
  V3: {passed: true, expected_benefit: "CCS 侧操作锚点全集；证据归并 c03/c07/c10-c20"}
  decision: verified

- id: f15
  title: ccs.ini 文件结构与关键开关
  type: framework
  V1: {passed: true, reason: "p85-87/p511-512 参数清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "座席会话报表出现大量无数据座席", expected: "手写 ShowStatisticWithData=1 进 [default_configuration] 节", observed: "p512 原文支持；n10 版本陷阱一致"}
  V3: {passed: true, expected_benefit: "CCS 配置排障的文件级抓手；证据归并 p10/n10/n21"}
  decision: verified

- id: f16
  title: CCS 安装向导决策链——九步选择
  type: framework
  V1: {passed: true, reason: "p89-93 向导窗口逐屏可查"}
  V2: {passed: true, check_mode: walkthrough, input: "生产站点许可类型选什么", expected: "按现场选 Monosite/Multisite（实验 Monosite）", observed: "p92 原文与 c02 步骤一致；自动装 VC++ 2017 x86 属前置事实"}
  V3: {passed: true, expected_benefit: "CCS 部署的标准动作链；证据归并 c02"}
  decision: verified

- id: f17
  title: OXE 统计文件生成流水线——5 个临时文件 → 3 类合并文件
  type: framework
  V1: {passed: true, reason: "p478-483 文件名、保留期、路径齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "Excel 报表没数据先查什么", expected: "查 /usr4/afe 临时文件与 /DHS3dyn/afe 合并文件是否生成", observed: "p479-481 原文口径；hr 存 5 周/dy 与 ev 存 12 个月逐格一致"}
  V3: {passed: true, expected_benefit: "统计链路排障的底层模型；证据归并 p11/p12/g45"}
  decision: verified

- id: f18
  title: Navigator 实时监控视图体系——对象图 + 定制化 + 桌面管理
  type: framework
  V1: {passed: true, reason: "p402-414/p430-437 视图与定制入口完整"}
  V2: {passed: true, check_mode: walkthrough, input: "每类对象旁的计数器在哪配", expected: "定制图标 → Real Time Info → 按对象选计数器 → Record", observed: "p406/p431-432 与 c13 步骤一致；3 秒快照默认值复核"}
  V3: {passed: true, expected_benefit: "实时监控大屏的落地路径；证据归并 p08/c13/n29"}
  decision: verified

- id: f19
  title: 告警三级体系——Alarms / Alerts / Indications 与阈值配置入口
  type: framework
  V1: {passed: true, reason: "p424-428/p447 三级定义与 100 条上限"}
  V2: {passed: true, check_mode: walkthrough, input: "黄圈告警和蓝圈消息有什么区别", expected: "Alerts=阈值越限、Indications=对象增删改（日历切换前 1 分钟有预告）", observed: "p425 原文逐条支持；c13 busy rate 阈值 80%→1% 触发实验互证"}
  V3: {passed: true, expected_benefit: "告警分流与阈值治理的依据；证据归并 p09/c13/n29"}
  decision: verified

- id: f20
  title: CCD Direct Calls 呼叫性质分布表——按座席状态判定 CCD 呼叫 vs 私人呼叫
  type: framework
  V1: {passed: true, reason: "p449-458 机制三要素 + p455/p456 判定表"}
  V2: {passed: true, check_mode: walkthrough, input: "打座席号算 CCD 还是私人呼叫", expected: "按座席状态逐格判定：空闲/部分退出=ACD 呼叫；忙/不可用=溢出 pilot direct call", observed: "p455 表逐格核对一致；p20 规则与 c14 五场景互证"}
  V3: {passed: true, expected_benefit: "直通号纳入统计的判定依据；证据归并 p20/c14/n04/n24/n31"}
  decision: verified

- id: f21
  title: 日历体系——Pilot 日历（10 切换/日）与分配日历（20 切换/日）+ 特殊日
  type: framework
  V1: {passed: true, reason: "p607-616/p629-641 双日历结构完整"}
  V2: {passed: true, check_mode: walkthrough, input: "节假日特殊安排怎么配", expected: "特殊日（≤50 个，必填年月日）覆盖周历，各配规则 ID", observed: "p611 原文支持；c20 特殊日实验落位；切换延迟语义见 n07"}
  V3: {passed: true, expected_benefit: "分时段运营的容量与语义边界；证据归并 p16/c20/n07"}
  decision: verified

- id: f22
  title: 语音指南体系——静态/动态、板卡与编码、CCD 指南清单、多语言编号
  type: framework
  V1: {passed: true, reason: "p194-210/p583-587 两分法与编号法完整"}
  V2: {passed: true, check_mode: walkthrough, input: "外包录音怎么上线", expected: ".wav 转 A-Law/8000Hz/64kbps/mono → SFTP 传输 → 选中装板", observed: "p241/p245 原文口径；c08/c09 双路径实验互证；40 条消息/指南、0-5999 消息域逐格一致"}
  V3: {passed: true, expected_benefit: "语音体验域的编号与格式底座；证据归并 p13/p14/c08/c09/n08/n26"}
  decision: verified

- id: f23
  title: 交互排队与 EWT 表结构——parking level 四种内容、6 阈值、IAA 树限制
  type: framework
  V1: {passed: true, reason: "p348-357 结构与限制齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "想按等待时长播不同消息怎么配", expected: "EWT 表 6 阈值挂 normal 队列 parking level，每阈值 EWT 值+指南/IAA/CCIVR 地址", observed: "p351-352 原文支持；c11 三阈值实验互证；IAA 5 层 4 选项 8 树限制一致"}
  V3: {passed: true, expected_benefit: "排队体验分档的设计依据；证据归并 p02/p15/c11/n30/n35"}
  decision: verified

- id: f24
  title: "518 排队位置指南结构——固定段+变量段+固定段与播报规则"
  type: framework
  V1: {passed: true, reason: "p374-384 结构、消息号、限制齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "排在第 63 位听到什么", expected: "变量段 51-100 按 5 步进向上取整，播 65", observed: "p377 原文例句逐字一致；消息号 3226-4217、Max position 上限 100、语言回退链复核"}
  V3: {passed: true, expected_benefit: "排队位次播报的完整规则；证据归并 p15/c12/n27/n32"}
  decision: verified
```

## 断言级裁决记录

1. **建队列表格三步同值**：成立。p71-73 逐页核对——3.1（Normal 队列）、3.3（Redirection 队列）的字段表均误写 31701/Overflow_WQ，仅 3.2 正确；照抄会三队列撞号。以章节标题与 p64 目标矩阵为准，详见 needs-review nr-02。
2. **WebAdmin 口令两处不一致**：成立。p65 mtcl/Superuser2580* vs p153 mtcl/mtcl；全书主体口径为 Superuser2580*，详见 needs-review nr-01。
3. **acdsup/acdsetup 混用**：成立。p76-77 章节标题 acdsup、正文 acdsetup；p120 亦为 acdsup；推断 acdsup 为准（推断标注保留），详见 needs-review nr-03。
4. **ABC-F 默认链路版本基线两处不一致**（本次验证新发现）：p163 "created by default since OXE R100" vs p165 "created by default from OXE N1"，两条均为 Notes 原文；行为结论一致（链路默认存在、access 须手工建），但版本基线口径二选一待核，详见 needs-review nr-04。
5. **语言索引混乱**：成立。p214 语言 #1=英文/#2=法文；p361/p390 语言 #2=英文；语言槽与语种的对应取决于目标库配置而非固定映射，详见 needs-review nr-07。
6. **EWT "四条消息"实为三条**：成立。p359 写 Four voice messages，下文仅 720/721/722 三条，详见 needs-review nr-08。
7. **统计 pilot 问候指南填消息号**：成立。p562 字段名 Guide n° 填 2701（消息号），与 pilot Pres.Guide 填 3 位指南号两种口径并存，详见 needs-review nr-09。
8. **PLTR 未展开**：如实记录。p117 "the rule (PLTR) will be applied"，全书未给全称；不采信外部知识补全。
9. **数字终审全绿**：优先级 0-9（p44/p53）、队列 30 pilot 共享/50 PG（p27）、路由 30 条/pilot 与全局 1200（p43/p103）、分配规则全局 10 与每队列 50 方向（p54）、紧急关闭 50 列×600 pilot（p528）、统计 pilot 3000（p546）、wrap-up/pause 1-3276 秒（p168）、日历 10/20 切换与 50 特殊日（p611/p616）、518 位次 1-50 逐个与 51-100 步进 5 上限 100（p377/p382）、位置消息 3226-4217（p379）——全部与原文逐格一致。
10. **无 rejected 断言**：实验值（IP/密码/前缀 12/401/580、板位 4-0、公网拨号串）均已标"实验口径"，环境值仅进 Boundary 与 book/overview。
