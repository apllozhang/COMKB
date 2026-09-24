# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f33（主验证对象）；principle p01-p53 / case c01-c13 / counter-example n01-n57 作为各单元的证据素材归并；glossary g01-g70 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 351 页全文通读 + 提取器页码证据交叉核对

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 32 | f01-f32 全部 |
| reference | 1 | f33（培训实验环境结构——POD/MicroSIP/RLAB，仅 Boundary 背景） |
| needs_review | 0（单元级） | 断言级 4 项转 needs-review.md（门槛括注、溢出秒数口径、BP 专属计数、笔误集合） |
| rejected | 0 | 关键数字（DECT 容量、端口表、监督 5/30/5、队列 10-900 秒、录音 2 个月、宽限 10 天）逐格核对一致 |

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——产品定位 → 云侧开户 → 端侧供给 → 话务能力域 → 运营
  type: framework
  V1: {passed: true, reason: "p3-351 章节序完整；p5 定位句与 p51 七步图锚定前半部组织轴"}
  V2: {passed: true, check_mode: walkthrough, input: "新 Hub 项目按什么顺序交付", expected: "云侧开户先于端侧供给的可执行顺序", observed: "p51 七步与 p80 四步创建流互证；步骤 1-5 为 BP 专属（p49）、6-7 客户管理员接手，顺序无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线；证据归并 p07/f04/c01"}
  decision: verified

- id: f02
  title: Rainbow 两条产品线对照图——混合云 vs Rainbow Hub
  type: framework
  V1: {passed: true, reason: "p6 一页双图，订阅命名与定位句完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户该走混合云还是 Hub", expected: "按是否保留现有 PBX 分线", observed: "p6 左线连已有 OXO/OXE（Business/Enterprise/Attendant），右线全云托管（Voice 前缀四档）；与 p9 订阅谱系一致"}
  V3: {passed: true, expected_benefit: "选型第一步的分线判据；证据归并 p03/g01/n54（跨书口径）"}
  decision: verified

- id: f03
  title: Rainbow Hub 全景图——云平台四大区块与客户侧零设施
  type: framework
  V1: {passed: true, reason: "p7 全景图四区块与 No VPN/No SBC 标注齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "客户现场还要不要部署话务硬件", expected: "不需要——只剩远程/移动工作者", observed: "p7 客户站点无 PBX/SBC/VPN；SIP 运营商接入、零接触供应、话务与欢迎服务全在云侧"}
  V3: {passed: true, expected_benefit: "方案沟通的架构底座；证据归并 p01/g01"}
  decision: verified

- id: f04
  title: 公司搭建七步主流程（Company Setup，全书前半部组织轴）
  type: framework
  V1: {passed: true, reason: "p51 七步图逐步给出，与各 How-To 章一一对应"}
  V2: {passed: true, check_mode: walkthrough, input: "按七步走一遍新客户", expected: "每步有对应章节与实验支撑", observed: "步1→c01，步2→p16-p20/c01，步3→f05/c02，步4→p24/c02，步5→c03，步6→c05/c06，步7→c07-c12，全覆盖"}
  V3: {passed: true, expected_benefit: "全书组织轴与交付 checklist 骨架；证据归并 p07/p13/n04"}
  decision: verified

- id: f05
  title: Cloud PBX 创建四步流——公司 → Voice 许可 → 声明 → 运营商开线
  type: framework
  V1: {passed: true, reason: "p80 四步分段完整；p75 Warning 给出硬前提"}
  V2: {passed: true, check_mode: walkthrough, input: "建 Cloud PBX 要先有什么", expected: "至少一条 Voice 订阅，否则只见传统 PBX 类型", observed: "p75/p80 双页互证；步骤 4（开线）在运营商侧书外，边界诚实"}
  V3: {passed: true, expected_benefit: "开户顺序的硬约束；证据归并 p20/n10"}
  decision: verified

- id: f06
  title: Cloud PBX 能力分区图——话务/其他两族特性
  type: framework
  V1: {passed: true, reason: "p78-79 定义与两族清单齐备，含原文自注 Non-exhaustive"}
  V2: {passed: true, check_mode: walkthrough, input: "Cloud PBX 能干什么、边界在哪", expected: "连设备/连运营商/管话务，通道线数无上限", observed: "p78 三用途 + 通道线数无上限；p79 自注示例非全量，全量以 Features List 为准（诚实边界）"}
  V3: {passed: true, expected_benefit: "能力地图与全量查证入口；证据归并 p02/g02/g64"}
  decision: verified

- id: f07
  title: 用户终端三形态结构——纯软话机 / 软+硬（RCC）/ 纯硬话机
  type: framework
  V1: {passed: true, reason: "p110-112 三形态分段定义，RCC 脚注展开"}
  V2: {passed: true, check_mode: walkthrough, input: "远程员工只买软话机行不行", expected: "行——纯软话机是合法形态但仍需 Voice 订阅", observed: "p111 Computer 单模式；p194 无话机也可配号（配号前提是订阅）；三形态与 p67 订阅表对号"}
  V3: {passed: true, expected_benefit: "订阅选型与端形态匹配的判据；证据归并 p03/g07/n33"}
  decision: verified

- id: f08
  title: Myriad/ALE 话机谱系与档次矩阵
  type: framework
  V1: {passed: true, reason: "p9 谱系名 + p107 参数表逐列齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "前台要按键多的旗舰话机选什么", expected: "Myriad M7 + EM200 扩展", observed: "p107 M7 3.5 英寸/BT4.1/EM200 10 页 x20 键支持该选型；参数与 p30 逐格一致"}
  V3: {passed: true, expected_benefit: "终端选型矩阵；证据归并 p30/g44/g45/n17"}
  decision: verified

- id: f09
  title: Generic SIP 设备接入原则与部署三阶段
  type: framework
  V1: {passed: true, reason: "p117 六原则 + p119 三阶段清单齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "客户旧话机能不能接 Hub", expected: "能但要手工配、功能受限、只做补充", observed: "p117 六条限制 + 四要素齐备；p119 部署前中后检查清单可执行；与 p36/n18/n19 一致"}
  V3: {passed: true, expected_benefit: "存量设备复用的评估框架；证据归并 p36/c13/n18-n20"}
  decision: verified

- id: f10
  title: Zero-Touch 部署机制全链路——注册 → 关联 → 自动取配 → 注册态可视
  type: framework
  V1: {passed: true, reason: "p134-139 机制四段连贯（MAC 声明/关联/取配/绿点验收）"}
  V2: {passed: true, check_mode: walkthrough, input: "话机上电后怎么就配好了", expected: "按 MAC 关联成员后自动取配置与固件", observed: "p135 MAC 声明两法、p137 5-10 分钟多次重启、p136 绿点验收；异常面 n21 三破坏源齐备"}
  V3: {passed: true, expected_benefit: "端侧交付主体流程；证据归并 p31/p32/p33/c03/n21-n23"}
  decision: verified

- id: f11
  title: Generic SIP 手工配置主步骤与批量导入流
  type: framework
  V1: {passed: true, reason: "p125 手工步骤 + p129 批量字段完整"}
  V2: {passed: true, check_mode: walkthrough, input: "30 台第三方话机怎么开户", expected: "CSV 批量建设备再回连账号", observed: "p129 模板字段（action/MAC/类型/SIP 密码）+ p131 导入后须回连；证书链下载入口 p127 明确"}
  V3: {passed: true, expected_benefit: "第三方设备批量施工路径；证据归并 c13/g56"}
  decision: verified

- id: f12
  title: DECT 两档方案结构——8328 单/双站 vs 8368 多站
  type: framework
  V1: {passed: true, reason: "p148-150 两档定义与容量数字逐格齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "车间 200 手持机选哪档", expected: "8368 多站（8328 上限 20 机不够）", observed: "p149 8328 上限 20 机/10 路；p150 8368 254 站/40 机每站/1000 机——容量表与 p35 逐格一致"}
  V3: {passed: true, expected_benefit: "移动话音方案选型查表依据；证据归并 p35/g47/g48/g46"}
  decision: verified

- id: f13
  title: DECT Zero-Touch 管理流程——基站声明/终端 IPEI 注册/远端重启
  type: framework
  V1: {passed: true, reason: "p151-152 基站线与终端线四步完整"}
  V2: {passed: true, check_mode: walkthrough, input: "8368 副站怎么找到主站", expected: "主站录 IP，副站靠该地址通信", observed: "p151 原文明确；终端按精确型号+IPEI 注册（n28）；手工站不转 zero-touch（n27）"}
  V3: {passed: true, expected_benefit: "DECT 施工与维护操作锚点；证据归并 p35/c04/n27/n28"}
  decision: verified

- id: f14
  title: 成员创建四法 + LDAP 连接器第五通道
  type: framework
  V1: {passed: true, reason: "p167 四法定义 + p179 LDAP 三功能完整"}
  V2: {passed: true, check_mode: walkthrough, input: "500 人批量开户怎么选通道", expected: "CSV 模板或 AAD/LDAP 同步", observed: "p167 四法 + p169 CSV 规则（UTF-8/SSO 密码留空）+ p170 AAD 不自动供应 + p179 LDAP 单向仅付费许可；与 p37 一致"}
  V3: {passed: true, expected_benefit: "批量开户方案选择树；证据归并 p37/c05/c06/n31/n32"}
  decision: verified

- id: f15
  title: 成员设置分区——七分区 + Tags/Profiles/Sites 横向项
  type: framework
  V1: {passed: true, reason: "p171 七分区逐项列出；p175 Profiles 补充"}
  V2: {passed: true, check_mode: walkthrough, input: "开户要配哪些项", expected: "按七分区逐项核对", observed: "Information/Permissions/Phone/Programmable keys/Services/Roles/Security 七区完整；时区/留言信箱口径与 p19/p38 互证"}
  V3: {passed: true, expected_benefit: "开户与排障的核对清单；证据归并 p38/p13/n34"}
  decision: verified

- id: f16
  title: 个人例行程序机制——一键切换五类参数
  type: framework
  V1: {passed: true, reason: "p173-174 定义与四预置场景齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "下班一键转手机怎么实现", expected: "Out of office 场景：转手机+在场 Away", observed: "p174 示例脚本与原文一致；五参数可逐项启停；成员端与管理端均可配"}
  V3: {passed: true, expected_benefit: "用户体验设计与培训话术；证据归并 g13/c06"}
  decision: verified

- id: f17
  title: 按键组机制——话机键+应用键批量下发
  type: framework
  V1: {passed: true, reason: "p183 机制 + p187 批量供应两列完整"}
  V2: {passed: true, check_mode: walkthrough, input: "全队统一速拨键怎么配", expected: "建键组后在 CSV 建户时两列带组", observed: "p183 键类型分话机/应用两族；p187 Deskphones/Softphone key groups 两列；单配路径 p203-205（c06）互证"}
  V3: {passed: true, expected_benefit: "批量交付一致性手段；证据归并 g14/c06"}
  decision: verified

- id: f18
  title: 四类组总览表（Regular/Attendant/Emergency/Manager-Assistant）
  type: framework
  V1: {passed: true, reason: "p209 四类定义、分发与许可注记齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "团队接听、前台、安保各建什么组", expected: "Regular/Attendant/Emergency 对号入座", observed: "p209 四类场景清晰；Attendant 全员须 Voice Attendant（n35）；溢出目的地清单跨页存在细微差异（转断言级裁决 4）"}
  V3: {passed: true, expected_benefit: "组类型选型的顶层地图；证据归并 p41/n35/n36"}
  decision: verified

- id: f19
  title: Hunt Group 三分发模式与轮转时序图
  type: framework
  V1: {passed: true, reason: "p210-211 三模式定义与时序参数齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "来话先找 A 再找 B 用哪种分发", expected: "Serial（顺序轮转）", observed: "p210-211 Serial 按序/Circular 轮流/Parallel 同振；轮转默认 10 秒与 p41/p234 一致；无队列组溢出默认 60 秒（转断言级裁决 2）"}
  V3: {passed: true, expected_benefit: "话务分配模式选型依据；证据归并 p41/c07"}
  decision: verified

- id: f20
  title: 等待队列机制——有/无队列行为对比与溢出参数
  type: framework
  V1: {passed: true, reason: "p215-216 两态行为与参数完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户怕漏接电话要不要开队列", expected: "开——先来先服务+超时溢出", observed: "p215 无队列全员占线即溢出、有队列 FCFS 10 秒延迟派号、溢出 10-900 秒可调；实时状态坐席与管理员可见（p216）"}
  V3: {passed: true, expected_benefit: "客服组设计核心参数；证据归并 p41/g19/n36"}
  decision: verified

- id: f21
  title: 组内角色权限表——Agent vs Administrator 能力矩阵
  type: framework
  V1: {passed: true, reason: "p214 权限矩阵逐项齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "主管不接电话只管组行不行", expected: "行——只授 Administrator", observed: "p214 原文明确；非坐席管理员对坐席显示为永久 withdraw（n36）；强制开关组欢迎服务为管理员独占"}
  V3: {passed: true, expected_benefit: "组权限设计依据；证据归并 g34/n36"}
  decision: verified

- id: f22
  title: 组语音信箱与协作 bubble 自动联动机制
  type: framework
  V1: {passed: true, reason: "p217 机制单页完整"}
  V2: {passed: true, check_mode: walkthrough, input: "组留言去哪听", expected: "组自动生成的 bubble 里", observed: "p217 建组自动建 bubble、留言自动转音频文件入 bubble、全员权限相同；教用户话术成立（n37）"}
  V3: {passed: true, expected_benefit: "组留言培训与易错点消除；证据归并 g27/n37"}
  decision: verified

- id: f23
  title: Manager/Assistant 组结构与筛选边界图
  type: framework
  V1: {passed: true, reason: "p218-221 结构、边界、DID 规则齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "助理筛不到经理电话查哪里", expected: "先查 DID 是否挂组级、再查是否 Rainbow 呼叫", observed: "p221 DID 必须配组级；p219 只筛电话呼叫；溢出链与提示音 5-30 秒与 p42 一致"}
  V3: {passed: true, expected_benefit: "管理层话务过滤方案与排障抓手；证据归并 p42/c07/n38"}
  decision: verified

- id: f24
  title: Supervision 组与话务台结构——订阅门槛、5/30 规格、三种显示
  type: framework
  V1: {passed: true, reason: "p223-225/p245-247 规格与限制齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "40 人部门建一个监督组建得下吗", expected: "不行——每组上限 30 人，拆组", observed: "p224 硬规格 5 页签/30 人/5 组逐格；Voice Attendant 含 10 路排队；p246 设备限制与 n43 一致"}
  V3: {passed: true, expected_benefit: "话务台方案容量与代价设计；证据归并 p43/g22/g23/n43/n35"}
  decision: verified

- id: f25
  title: 紧急呼叫链路——免前缀直达组、0112 转外线、定位责任链
  type: framework
  V1: {passed: true, reason: "p226-229 号码面/组面/定位面三段齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "激活紧急组后拨 112 会怎样", expected: "免前缀呼叫进安保组不出局；组员转警须加前缀 0112", observed: "p228 原文直接回答；号码保留不可占内线（p227）；定位责任在 BP 与运营商（p229/n41）"}
  V3: {passed: true, expected_benefit: "监管合规交付的语义澄清；证据归并 p44/c08/n39/n40/n41"}
  decision: verified

- id: f26
  title: 通话录音体系——触发面、存储与 Rainbow Exporter 归档
  type: framework
  V1: {passed: true, reason: "p230-231 触发三层与存储口径齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "录音能存多久、谁看得见", expected: "2 个月；仅最终客户管理员", observed: "p231 与 p45 逐格一致；超期归档走付费 Exporter（Google Drive/SFTP）；组级录音档 all/external/internal/none（p235）"}
  V3: {passed: true, expected_benefit: "合规与质检方案的口径来源；证据归并 p45/g51/n42"}
  decision: verified

- id: f27
  title: 欢迎服务四件套关系图——日历/语音提示/欢迎服务/IVR
  type: framework
  V1: {passed: true, reason: "p250-252 四件套定义与管理动作齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "白天转组晚上播提示音怎么搭", expected: "日历+欢迎服务开闭双路由", observed: "p251 四件套关系清晰；p253 两套实施步骤（无 IVR/带 IVR）；日历先建与 p259/n44 一致"}
  V3: {passed: true, expected_benefit: "客户感知最强功能的实施地图；证据归并 p48/p46/c09/n44"}
  decision: verified

- id: f28
  title: Welcome service 开/闭双路由图与强制开关
  type: framework
  V1: {passed: true, reason: "p258-260 路由目的地与 forced 机制齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "强制闭店第二天自己开了", expected: "正常——forced 是一次性覆盖，下个时段回 Auto", observed: "p259 原文明确；定制时段提示上限 5 条/特殊日 10 天（p260）与 p46/n45 一致"}
  V3: {passed: true, expected_benefit: "欢迎服务运维答疑依据；证据归并 n44/n45/c09"}
  decision: verified

- id: f29
  title: IVR 结构图——3 级菜单、0-9 选择、两种入口
  type: framework
  V1: {passed: true, reason: "p265-271 结构、入口、提示音两模式齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "客户要 5 级语音菜单行不行", expected: "不行——上限 3 级，重新设计菜单树", observed: "p266 3 级/根菜单 10 项/无限制无许可逐格；DDI 直挂 7×24 与经欢迎服务受日历控制两入口（n46）；唯一提示建后不可改（n47）"}
  V3: {passed: true, expected_benefit: "IVR 方案设计与报价分流依据；证据归并 p47/g25/c11/n57"}
  decision: verified

- id: f30
  title: 多站点结构图——单 Cloud PBX 下的站点逻辑分区
  type: framework
  V1: {passed: true, reason: "p301-305 模型与不变量清单齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "两地办公要几台 PBX", expected: "仍一台——站点是逻辑分区", observed: "p303 站点挂成员/号码/MoH；p304 内呼互通/组跨站/欢迎服务目录共用五不变量；与 p92/n15 一致"}
  V3: {passed: true, expected_benefit: "多址客户架构预期管理；证据归并 p28/c12/n15/n16"}
  decision: verified

- id: f31
  title: 分析体系结构——CDR 三通道、全局仪表盘、Voice/Groups/Quality 视图
  type: framework
  V1: {passed: true, reason: "p317-328 三视角结构与口径数字齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "月度话务量统计用哪个数据源", expected: "计费用 CDR、行为用仪表盘——口径不同", observed: "p318 纯 VoIP 呼叫不产生 CDR（n50）；仪表盘 7/30 天可导、Voice 最长 1 年、服务/组对比 ≤5（p50）；MOS 阈值 p51 一致"}
  V3: {passed: true, expected_benefit: "运营增值与验收数据口径；证据归并 p49/p50/p51/g28/g29/n50/n51"}
  decision: verified

- id: f32
  title: 维护支持体系八件套——日志/设备监督/连通性/上报/状态页/SR
  type: framework
  V1: {passed: true, reason: "p330-343 八抓手逐一定义"}
  V2: {passed: true, check_mode: walkthrough, input: "用户说平台挂了先查什么", expected: "status.openrainbow.com + 订阅告警分流", observed: "p338 状态页与 Get updates 明确；用户日志 p332、上报 p337（集成商同视角）；SR 前提认证 Rainbow Hub 伙伴（p341/n54）"}
  V3: {passed: true, expected_benefit: "售后运维闭环抓手清单；证据归并 p52/n52-n54"}
  decision: verified

- id: f33
  title: 培训实验环境结构——POD 体系、公网模拟与账号号码规划
  type: framework
  V1: {passed: true, reason: "p12-34 三层环境完整，但属教学基础设施"}
  V2: {passed: true, check_mode: walkthrough, input: "生产部署能不能照抄实验参数", expected: "不能——全部为实验口径", observed: "p29/p53 账号码段网段均实验值；MicroSIP 训后须删（n56）；模拟器不能按公网号呼本公司成员"}
  V3: {passed: true, expected_benefit: "仅作 Boundary 背景：提醒读者实验值不入生产；证据归并 p29/p53/n08/n56"}
  decision: reference
```

## 断言级裁决记录

1. **成员配号订阅门槛括注不完整**：成立。p194 Warning 括注列 Voice Business/Enterprise/Attendant 三档，未含 Voice Phone；而 p66 总口径与 p67 订阅表均为四档（Voice Phone 也是电话订阅）。按 p66 四档口径理解，p194 括注视为不完整列举——详见 needs-review nr-01。
2. **Hunt group 溢出秒数两处口径并存**：成立并如实记录——图示页无队列组默认溢出 60 秒（p211），带队列组溢出 10-900 秒可调（p215）。适用对象不同（无队列组 vs 带队列组），不构成矛盾；卡片引用时分开表述，详见 needs-review nr-02。
3. **BP 专属"四项"（p49）与 Reseller"五项独占"（p58-59）计数差异**：成立——两页视角不同：p49 按"操作"列四项（PBX 声明/付费订阅/终端声明/电话线），p58 按"可创建元素"多列 Extensions。互补非矛盾，两条口径并存记录（p07/p13/n04），详见 needs-review nr-03。
4. **组溢出目的地清单跨页存在细微出入**：f18（p209）列 7 种，f20（p215）与 p41、c07（p235 实验页）列 8 种（差异在"欢迎服务/外线"是否并列）。以实验页 p235 的 8 种为准（voice prompt/member/group/internal number/public number/voicemail/welcome service/automated attendant），讲义页清单视为示例性简写。
5. **无 rejected 断言**：DECT 容量（8328：20 机/10 路；8368：254 站/40 机每站/1000 机）、设备端口表六行（TCP 5061/443、UDP 30000-44999/53/123、TCP 22）、监督规格 5 页签/30 人/5 组、队列 10-900 秒、录音 2 个月、宽限 10 天、密码 ≥12 字符+3 类字符（p54/p168/p169/p177 四处）均与原文逐格一致。
