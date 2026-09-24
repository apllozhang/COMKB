# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f25（主验证对象）；principle p01-p49 / case c01-c20 / counter-example n01-n50 作为各单元的证据素材归并；glossary g01-g55 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 470 页全文通读 + 提取器页码证据交叉核对

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 25 | f01-f25 全部 |
| reference | 0 | 无——25 个框架单元的断言与操作路径均在书内闭环（实验编号已标"实验口径"） |
| needs_review | 0（单元级） | 断言级 7 项转 needs-review.md（重试次数口径、3X800 笔误、字符串示例值、关键字拼写混用、默认值大小写、LIT 双表述、推断性结论） |
| rejected | 0 | 无编造断言；p18 容量表 12 格、p37-39 取值域、p387 配额表逐格核对与原文一致 |

verified 明细：f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——概念地基 → 公共实验矩阵 → 脚本工具链 → 规则族/特征源 → 综合 → 统计 → 外部化
  type: framework
  V1: {passed: true, reason: "p3-18 引论 + 20 个 How-To 章逐章给出；章节推进与 case c01-c20 一一对应"}
  V2: {passed: true, check_mode: walkthrough, input: "新项目按什么顺序交付 ACR", expected: "给出可执行的阶段顺序", observed: "先矩阵后脚本、先单机后外部的主线与 20 个 How-To 编排互证，顺序无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线，避免先写脚本后建矩阵的倒置"}
  decision: verified

- id: f02
  title: ASM 架构全景——脚本编辑器/管理器/服务器/数据库四方与呼叫处理链
  type: framework
  V1: {passed: true, reason: "p9-11 架构图与职责定义完整（编辑器/管理器=Client，服务器=解释+查库+算列表）"}
  V2: {passed: true, check_mode: walkthrough, input: "坐席列表由谁算、脚本由谁执行", expected: "ASM 服务器执行脚本并算列表", observed: "p10 职责清单直接回答；*.scr/*.alb 双文件形态 p11 互证"}
  V3: {passed: true, expected_benefit: "排障分流的架构底座（编辑器侧 vs 服务器侧）"}
  decision: verified

- id: f03
  title: 呼叫分发三步流程与动态组——特征化 → ASM 算列表 → 带列表进 Waiting Room
  type: framework
  V1: {passed: true, reason: "p12-14 三步定义与 ISMF 五步示例完整"}
  V2: {passed: true, check_mode: walkthrough, input: "ACR Pilot 为什么要挂 Waiting Room", expected: "ASM 返回的动态组附着在房间上", observed: "p12 Waiting Room 非 FIFO + p13 房间/队列互斥（n22）一致"}
  V3: {passed: true, expected_benefit: "理解'选人归 ASM'的结构前提；证据归并 g05/g06/n22"}
  decision: verified

- id: f04
  title: 9 种 ACR 规则分类学——单用规则 vs 可组合规则，IDLE/COM 互斥
  type: framework
  V1: {passed: true, reason: "p7-8 九规则逐一定义；p244 单用/可组合两清单明确"}
  V2: {passed: true, check_mode: walkthrough, input: "LCA 能和 ISM 写进同一个 APPLY 吗", expected: "不能——LCA 属单用规则须独占 APPLY", observed: "p244 清单直接回答；IDLE/COM 互斥另见 n24"}
  V3: {passed: true, expected_benefit: "脚本规则选型的分类基线；证据归并 p25/n24/c10"}
  decision: verified

- id: f05
  title: 呼叫特征清单——路由的五种原料与内部数据库四属性
  type: framework
  V1: {passed: true, reason: "p15-17 特征清单 + p130-131 三键四属性两处完整"}
  V2: {passed: true, check_mode: walkthrough, input: "脚本执行期能拿到呼叫的哪些信息", expected: "CLID/NDI/Call Tag/档案/类型五类", observed: "p15 逐项列出；p17 伪代码示范取用"}
  V3: {passed: true, expected_benefit: "个性化路由的原料清单；证据归并 p18/p19/n16/n17/c06/c07"}
  decision: verified

- id: f06
  title: 公共实验矩阵对象模型——双 Pilot + 队列/房间 + 统计 Pilot + 坐席组的拓扑
  type: framework
  V1: {passed: true, reason: "p21-22 矩阵图与对象清单完整（编号为实验口径）"}
  V2: {passed: true, check_mode: walkthrough, input: "后续实验在什么地基上叠对象", expected: "普通链路+ACR 链路+入口分流三层拓扑", observed: "p22 对象清单与 c01 十九步一致；p22 '3X800' 笔误已登记（nr-02）"}
  V3: {passed: true, expected_benefit: "全部实验的公共参照系；证据归并 p03/n48/c01"}
  decision: verified

- id: f07
  title: CCD/ACR 配置菜单路径双树——OMF 侧 Applications/CCD 与 CCS 侧 Configurations
  type: framework
  V1: {passed: true, reason: "p23-41 等 11 处 How-To 菜单路径汇总齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "建矩阵与建 ACR 逻辑分别去哪棵树", expected: "矩阵对象在 OMF 树、ACR 逻辑在 CCS 树", observed: "两棵树分工与各章路径截图级一致；附件名单/统计 Pilot 双入口（p33/p36）如实记录"}
  V3: {passed: true, expected_benefit: "操作锚点索引；证据归并 p45/c01"}
  decision: verified

- id: f08
  title: 路由规则/分发规则配置结构——Pilot Rule Guide → Rule Direction → Distribution Rule → 两级 selection
  type: framework
  V1: {passed: true, reason: "p26-29 四层结构逐层给出（30 条路由规则/10 条分发规则/两级优先级）"}
  V2: {passed: true, check_mode: walkthrough, input: "队列间与队列到组的方向怎么控", expected: "Rule Direction 管队列间，Resource selection 管队列到组", observed: "p26/p28 两级结构一致；生效规则切换三途径（Current Number/CCS Apply/日历）齐备"}
  V3: {passed: true, expected_benefit: "矩阵层排障的结构地图；证据归并 p04/p05/c01 步骤 5-8"}
  decision: verified

- id: f09
  title: 混合链路（Hybrid Link ABC-F）结构与 hybvisu 校验
  type: framework
  V1: {passed: true, reason: "p33-35 链路参数与校验命令完整"}
  V2: {passed: true, check_mode: walkthrough, input: "混合链路起不来先查什么", expected: "邻接网络号异于本地、Multi access=YES、至少 2 access 成对，hybvisu -f all 双 up", observed: "p33-35 三约束与校验判据一一对应（n04）"}
  V3: {passed: true, expected_benefit: "本地 CCD 呼叫的链路前提与排障抓手；多节点组网细节在书外（Boundary）"}
  decision: verified

- id: f10
  title: 脚本生命周期闭环——编写 → 保存传输 → Pilot 激活 → Debugger 验证 → 内存/运行检查
  type: framework
  V1: {passed: true, reason: "p44-46 闭环三环 + p59-60/p78-80 调试与维护页齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "改完脚本为什么行为没变", expected: "查是否保存传输并在 ACR Pilot 重新激活", observed: "p44 原文直指漏激活；p45/p60 adm_acd 内存检查闭环（n10/n46 调试约束归并）"}
  V3: {passed: true, expected_benefit: "脚本交付与排障的标准动作序列；证据归并 p11/p12/p47/c02/c03"}
  decision: verified

- id: f11
  title: parameters.cfg 参数文件机制——asm_ag_free_duration 与 asm_on_dhs 两个开关
  type: framework
  V1: {passed: true, reason: "p48-49/p241-242/p322 四处交叉给出参数语义与修改方法"}
  V2: {passed: true, check_mode: walkthrough, input: "改了参数为什么不生效", expected: "必须 dhs3_init -R MAIN_AFE 重启", observed: "p49/p264/p345 三处重复强调重启（n06）；最低版本 l2.300.32.a（p241）"}
  V3: {passed: true, expected_benefit: "Idle 排序语义与外部化割接的两个总开关；证据归并 p07/p08/n05-n07/c02"}
  decision: verified

- id: f12
  title: 授权/非授权名单的五种给值方式与维护入口
  type: framework
  V1: {passed: true, reason: "p53-58/p60 五式逐一定义（上下文索引/整数/名字/显式列表/LIST 变量）"}
  V2: {passed: true, check_mode: walkthrough, input: "名单跟着主叫号走怎么配", expected: "用 CALLING 上下文索引", observed: "p57 索引清单直接回答；String 索引大小写敏感（p74，nr-04 拼写混用）"}
  V3: {passed: true, expected_benefit: "名单规则脚本化的参数全集；证据归并 p10/p11/n08/n09/c03"}
  decision: verified

- id: f13
  title: 空列表兜底结构——Redirection 转发地址形态与 Redistribution 退回链
  type: framework
  V1: {passed: true, reason: "p84-90 两规则地址形态/触发条件/落点完整"}
  V2: {passed: true, check_mode: walkthrough, input: "坐席全忙呼叫会不会悬死", expected: "重定向转号或再分发退下一方向，全关则 Blockage", observed: "p85 地址三形态 + p89/p90 触发语义一致；n11 封锁落点警告归并"}
  V3: {passed: true, expected_benefit: "生产安全网的设计模板；证据归并 p13/p14/p09/c04"}
  decision: verified

- id: f14
  title: 坐席直拨与 ACR 融合结构——Pilot Direct Call / 私有号码 / DICA 技能 / CALL_TYPE
  type: framework
  V1: {passed: true, reason: "p105-115 四件套定义与配置点完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户要'直拨忙时等原坐席'怎么实现", expected: "处理组指 ACR Pilot + 私有号 + DICA + CALL_TYPE 分支脚本", observed: "p106/p111/p114 三段语义闭环；无 ACR 时立即溢出换人（n14）反证增值点"}
  V3: {passed: true, expected_benefit: "最高频客户诉求的方案骨架；证据归并 p15/p16/p17/n12-n15/c05"}
  decision: verified

- id: f15
  title: 内部数据库结构——三键 × 五属性 × 4000 条与脚本取用语法
  type: framework
  V1: {passed: true, reason: "p130-141 结构、容量、取用语法、维护入口齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "回头客走专属档案怎么配", expected: "主叫号键录条目，脚本 CALL_PROFILE[CALLING] 取用", observed: "p131/p133 语法与 c06 实验一致；区段键 1000-1999 整段命中（p135）"}
  V3: {passed: true, expected_benefit: "VIP/大客户路由的核心手段；证据归并 p18/p19/n16/n17/c06"}
  decision: verified

- id: f16
  title: Call Tag 三生成途径——统计 Pilot / IAA 编码叶 / CCivr 构件
  type: framework
  V1: {passed: true, reason: "p167-171 三途径逐一定义（0-32 字符/≤16 位 Correlator data/TransferCall）"}
  V2: {passed: true, check_mode: walkthrough, input: "IVR 采集的客户号怎么进 ACR", expected: "编码叶经 CSTA 作 Correlator data 传递", observed: "p169 原文明确；转移覆盖语义 p172-173（n18）互证"}
  V3: {passed: true, expected_benefit: "IVR 与 ACR 打通的枢纽；证据归并 p19/p20/p46/n18-n21/c07"}
  decision: verified

- id: f17
  title: IAA（自动话务员）三件套配置结构——Leaf / Tree / Access + 中继激活
  type: framework
  V1: {passed: true, reason: "p177-180/p198-199 四步结构与改配约束完整"}
  V2: {passed: true, check_mode: walkthrough, input: "改 IAA 叶要不要先停", expected: "先 Valid=FALSE 改完 TRUE，中继组属性 YES", observed: "p199 步骤与 n20 警告一致；IAA 仅外部呼入（p211，n19）"}
  V3: {passed: true, expected_benefit: "编码采集入口的施工与约束清单；引导录制属环境操作（Boundary）"}
  decision: verified

- id: f18
  title: 多语言语音引导结构——40 语种映射 + 语言判定链 + 坐席语言成本
  type: framework
  V1: {passed: true, reason: "p214-221 承载/判定/选人三段完整"}
  V2: {passed: true, check_mode: walkthrough, input: "档案里有英法两门语言播哪个", expected: "按语言偏好（1-7、1 最高）定", observed: "p216/p229 判定链与偏好语义一致；1 门语言技能即可入选（p214）"}
  V3: {passed: true, expected_benefit: "多语言中心的配置语义；证据归并 p22/n47/c09"}
  decision: verified

- id: f19
  title: IQUEUE 停放级编程结构——6 级 + NEXT 级对路由规则停放管理的覆写
  type: framework
  V1: {passed: true, reason: "p249-252 构件语法与行为示例完整"}
  V2: {passed: true, check_mode: walkthrough, input: "停放引导能否每级不一样", expected: "1-6 级每级可配引导/EWT/地址，未指定级回落路由规则", observed: "p249-252 语义与 c10 Addition 脚本行为互证；NEXT 级接管条件明确"}
  V3: {passed: true, expected_benefit: "等待体验编程的构件语义；证据归并 p26/c10"}
  decision: verified

- id: f20
  title: LIST 变量体系——16 个自动列表、skill/agent 两型、加减算子与截断策略
  type: framework
  V1: {passed: true, reason: "p258-261 类型/算子/截断三段完整"}
  V2: {passed: true, check_mode: walkthrough, input: "动态拼一份名单再交给名单规则行吗", expected: "agent 型 LIST 拼好后 RULE_AUTHORIZED_LIST LIST[%x]", observed: "p258 类型约束 + c10 List_Var 实验一致；超 7 技能截断策略 p259"}
  V3: {passed: true, expected_benefit: "动态名单/动态技能组的编程原语；证据归并 p25/c10"}
  decision: verified

- id: f21
  title: 过滤器体系结构——AND 语义、Super/Hyper-Filter OR 语义与观测入口
  type: framework
  V1: {passed: true, reason: "p285-307 四层体系（过滤器/超组/实时/统计）齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "过滤器能控制呼叫优先吗", expected: "不能——只影响观测与统计", observed: "p285 原文明确（n27）；AND/OR 对照 p314（Filter 3 零数据实证，n29）"}
  V3: {passed: true, expected_benefit: "监控口径设计的语义基线；证据归并 p29/p30/p31/n27-n29/c11"}
  decision: verified

- id: f22
  title: ACR 统计报表三模板与实时窗口地图
  type: framework
  V1: {passed: true, reason: "p293-301/p307 三模板分工与窗口族完整"}
  V2: {passed: true, check_mode: walkthrough, input: "要出每过滤器一行的汇总表用哪个模板", expected: "FormFilterS.xls（Filters Summary）", observed: "p299-301 模板分工明确；新过滤器查不到历史（p302，n28）互证"}
  V3: {passed: true, expected_benefit: "交付验收报表的产出路径；证据归并 p30/n28/c11"}
  decision: verified

- id: f23
  title: 外部 ASM 部署结构——组件选项、站点角色、文件位置与双机复制
  type: framework
  V1: {passed: true, reason: "p320-335/p352-353/p361-373 五要素完整（组件/服务/Site/文件/双机）"}
  V2: {passed: true, check_mode: walkthrough, input: "外部 ASM 与内部 alb 什么关系", expected: "角色一致，外加外部库访问；割接须先停内部", observed: "p320 'strictly identical' + p322 asm_on_dhs=0 + p353 未停连不上（n30/n31）一致"}
  V3: {passed: true, expected_benefit: "架构级改造的施工地图；证据归并 p32-p35/p43/n30-n35/c12/c13"}
  decision: verified

- id: f24
  title: 外部数据库编程模型——SQL 六构件 + SELECT/存储过程 + fetch 循环 + 数据映射
  type: framework
  V1: {passed: true, reason: "p376-392 六构件语义、三值结果、配额表、fetch 规则齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "查到多行会怎样", expected: "无 BREAK 全表扫，不用 LIST 只留最后一行", observed: "p390-391 规则原文直接回答（n39）；32 位 ODBC/16 库/167 许可（p36/n36/n37）前提闭环"}
  V3: {passed: true, expected_benefit: "外部化脚本的语法基础；证据归并 p36-p40/n36-n42/c14/c18"}
  decision: verified

- id: f25
  title: adm_acd 维护命令选项地图——ACR 的命令行仪表盘
  type: framework
  V1: {passed: true, reason: "p45/p60/p141/p276/p339-343/p394/p447-451 七处维护页汇总"}
  V2: {passed: true, check_mode: walkthrough, input: "客户报'上次接听坐席不准'先查什么", expected: "adm_acd <ASM IP> -salb 选项 28 dump 呼叫动态数据", observed: "p45/p276 选项语义明确；c18 重启持久化实验以 28 * 前后对照验证"}
  V3: {passed: true, expected_benefit: "ACR 排障的命令行抓手全集；证据归并 p42/n37/n40/c02/c06/c18/c20"}
  decision: verified
```

## 断言级裁决记录

1. **脚本重试次数两处口径不一致**：成立并如实记录（p50 "20 requests / executed 20 times" vs p184 "executed 21 times"）。差异疑与重选计次边界有关，原书未解释（推断）；详见 needs-review nr-01，SLA 设计不得引用单一数字。
2. **p22 "agent PG 3X800" 笔误**：成立。同页前文对象为 3X999800，判为漏写 999；照录原文并以 3X999800 口径引用，详见 nr-02。
3. **p196 EXTRACT_STRING 按位截取示例值**：成立。按位截取形态（起始下标, 长度, 源串）的示例结果原文印作 "0221001"，提取器核对后判定与截取规则的直观结果不符，疑教材笔误；照录并标注"原文如此"，实际语法以编辑器行为为准，详见 nr-03。
4. **关键字/函数名拼写混用**：成立。AUTHORIZED/AUTHORISED、UNAUTHORIZED/UNAUTHORISED 两式混用（p61/p63/p74），STRING_LENGHT（p192）、"DNS="（p393）、"USE_BATABSE"（p393）为原文拼写；引用时标注"原文如此"，转述用正确拼写，详见 nr-04。
5. **数据库默认值大小写两处写法**：成立。表默认 'NoAgent'/'NoName'（p411-413）与脚本判断 "noAgent"（p446 区段）、注释 "noname"（p434）大小写不一致；字符串精确比较时以实际库值为准，详见 nr-05。
6. **LIT 双表述**：成立。p240 "LIT (Logon Idle Time)" 与 p242 "LIT (Longest Idle Time)" 并存，语义同指"登录后空闲时长"排序，照录双表述，详见 nr-06。
7. **无 rejected 断言**：p18 容量表 12 格（统计 Pilot 1000/Pilot 600/队列与房间 600/组 450/方向 30/50/域 20/技能 1000/特征列表 1000/特征 7/50/20000/名单 30/30）、p37-39 取值域（域名 1-16/ID 0-99/权重 1-20、档案 ID 0-999/级别 1-9/偏好 1-7）、p387 配额表（64/64/32/16/16/16）均与原文逐格一致，无编造。
