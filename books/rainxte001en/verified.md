# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f44（主验证对象）；principle p01-p50 / case c01-c14 / counter-example n01-n54 作为各单元的证据素材归并；glossary g01-g62 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 251 页全文通读 + 提取器页码证据交叉核对

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 40 | f01, f04-f28, f30-f28 区间内全部除 f02/f03/f29 外（详见下表） |
| reference | 3 | f02（RLAB 平台结构）、f03（SIP 模拟器）、f29（FE 场景分支树，操作全在书外 cookbook） |
| needs_review | 0（单元级） | 断言级 3 项转 needs-review.md（版本口径、OCR 变体、计数修正） |
| rejected | 0 | 无编造断言；p147 容量表与 p129 矩阵逐格核对一致 |

verified 明细：f01, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39, f40, f41, f42, f43, f44

## 验证记录

```yaml
- id: f01
  title: 全书课程推进主线——云侧开户 → PBX 接入 RCC → 网关解锁音频 → 增值域
  type: framework
  V1: {passed: true, reason: "p4-7 课程步骤逐段给出；p6 明确 RCC 中间态定位"}
  V2: {passed: true, check_mode: walkthrough, input: "新项目按什么顺序交付 Rainbow 集成", expected: "给出可执行的阶段顺序", observed: "七段主线与 p50 六步主流程互证，顺序无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线，避免先建网关后建云侧账户的倒置"}
  decision: verified

- id: f04
  title: Rainbow 平台双定位全景（UCaaS + CPaaS + PBX 桥接）
  type: framework
  V1: {passed: true, reason: "p29-31 全景图与文字定义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "向客户解释 Rainbow 与 OXO 的关系", expected: "PBX 保留呼叫控制、Rainbow 提供协作与云", observed: "p31 Agent 桥接结构支持该表述"}
  V3: {passed: true, expected_benefit: "方案沟通的架构底座"}
  decision: verified

- id: f05
  title: UCaaS 混合云架构三要素（客户端/通信/PBX+WebRTC 网关）
  type: framework
  V1: {passed: true, reason: "p32 架构图单处完整"}
  V2: {passed: true, check_mode: walkthrough, input: "用户路由档案由谁执行", expected: "通信层按个人路由档案分发", observed: "p32 'Manage your routing profile' 与 p119 来话分发一致"}
  V3: {passed: true, expected_benefit: "RCC 与网关两章的概念衔接点"}
  decision: verified

- id: f06
  title: 8 种订阅体系与电话服务付费门槛分层
  type: framework
  V1: {passed: true, reason: "p33 八种订阅逐一定义；p65 电话门槛三选一"}
  V2: {passed: true, check_mode: walkthrough, input: "客户要话务台+会议室+CRM 集成怎么组合", expected: "Attendant+Room+Connect 组合", observed: "p33 各订阅定位支持组合决策"}
  V3: {passed: true, expected_benefit: "售前选型矩阵；证据归并 p01/n01"}
  decision: verified

- id: f07
  title: 网络要求文档体系（支持页 + 两份 PDF 的结构）
  type: framework
  V1: {passed: true, reason: "p36-40 文档结构逐一列出"}
  V2: {passed: true, check_mode: walkthrough, input: "上线前网络前提查哪里", expected: "支持页文章 + Network Requirements PDF", observed: "p36/p40 指针明确；书内无私有数值（诚实外置）"}
  V3: {passed: true, expected_benefit: "task-01 的执行入口；Boundary 指针成立"}
  decision: verified

- id: f08
  title: Rainbow Pilot 连通性与承载评估流程
  type: framework
  V1: {passed: true, reason: "p41-44 工具用途与入口"}
  V2: {passed: true, check_mode: walkthrough, input: "站点能否承载 80 个混合用法用户", expected: "按用法配比跑评估", observed: "p42 明确评估维度（协作/会议/混合/Hub）；注意 n03 分区随版本演进"}
  V3: {passed: true, expected_benefit: "售前勘测工具入口"}
  decision: verified

- id: f09
  title: Company 概念体系（两类公司 + 经销链 + 公司要素四组）
  type: framework
  V1: {passed: true, reason: "p47-49 概念页完整；p48 BP 专属两项"}
  V2: {passed: true, check_mode: walkthrough, input: "客户管理员为何建不了 PBX", expected: "BP 专属权限解释", observed: "p48 Declaration & PBX / paid subscriptions 两项专属；与 p04/n05 一致"}
  V3: {passed: true, expected_benefit: "权责切分依据，减少误判故障"}
  decision: verified

- id: f10
  title: 公司搭建六步主流程（Company Setup）
  type: framework
  V1: {passed: true, reason: "p50 六步图完整"}
  V2: {passed: true, check_mode: walkthrough, input: "按六步走一遍新客户", expected: "每步有对应章节支撑", observed: "步1-2→f09/f16，步3→f19，步4→f25-f33，步5→f20-f23，步6→f34-f38，全覆盖"}
  V3: {passed: true, expected_benefit: "全书组织轴与交付 checklist 骨架"}
  decision: verified

- id: f11
  title: 公司可见性四级结构与选型建议
  type: framework
  V1: {passed: true, reason: "p52 四级行为逐级定义"}
  V2: {passed: true, check_mode: walkthrough, input: "新客户默认选哪级", expected: "CLOSED", observed: "p52 原文明确建议；n06 给出 ISOLATED 代价"}
  V3: {passed: true, expected_benefit: "建司配置的默认决策"}
  decision: verified

- id: f12
  title: 认证方式体系（SSO 三协议 + 本地双模式，可按用户混配）
  type: framework
  V1: {passed: true, reason: "p53 三种 SSO 组合 + TOTP + 密码"}
  V2: {passed: true, check_mode: walkthrough, input: "客户有 ADFS 和 Azure AD，能混用吗", expected: "可并存多种方式按用户指定", observed: "p53 原文支持；n07 级别门槛齐备"}
  V3: {passed: true, expected_benefit: "认证方案设计的边界清楚"}
  decision: verified

- id: f13
  title: 创建客户公司的界面入口路径
  type: framework
  V1: {passed: true, reason: "p54 入口截图文字"}
  V2: {passed: true, check_mode: walkthrough, input: "BP 建新 EC 公司从哪进", expected: "客户公司列表 → Create a client company", observed: "路径明确；必填字段 p51"}
  V3: {passed: true, expected_benefit: "操作锚点"}
  decision: verified

- id: f14
  title: 管理员权责分工（BP vs EC vs Roles 页签）
  type: framework
  V1: {passed: true, reason: "p57-59 两级权责清单"}
  V2: {passed: true, check_mode: walkthrough, input: "多管理员怎么授权", expected: "Roles 页签可设多名", observed: "p59 明确；完整矩阵在 Features List（指针诚实）"}
  V3: {passed: true, expected_benefit: "管理团队规划依据"}
  decision: verified

- id: f15
  title: 企业目录与信息频道两步配置路径
  type: framework
  V1: {passed: true, reason: "p60-61 两步序列"}
  V2: {passed: true, check_mode: walkthrough, input: "外部联系人怎么进 Rainbow", expected: "Business Directory 手工或 CSV", observed: "p60 含样例文件与导入报告；n08 强制订阅代价"}
  V3: {passed: true, expected_benefit: "来电视频识别与内部通告的落地路径"}
  decision: verified

- id: f16
  title: 订阅两层流转（公司池 → 成员分配）
  type: framework
  V1: {passed: true, reason: "p64-67 两层流转与表单要素"}
  V2: {passed: true, check_mode: walkthrough, input: "订阅买多了能给别的公司用吗", expected: "订阅先开到公司再内部分配", observed: "p65 两层结构明确；实验口径 n09 禁预付"}
  V3: {passed: true, expected_benefit: "许可运营与计费口径"}
  decision: verified

- id: f17
  title: OMC 安装与首次连接四步
  type: framework
  V1: {passed: true, reason: "p69-78 How-To 完整（安装/证书/改密/客户信息）"}
  V2: {passed: true, check_mode: walkthrough, input: "首连后每次都弹证书告警", expected: "首次未装证书到受信任根", observed: "p75 明确一次性安装路径；n10 三坑齐备"}
  V3: {passed: true, expected_benefit: "PBX 侧一切配置的前提；证据归并 c01/p13/n10"}
  decision: verified

- id: f18
  title: OXO 与客户端 IP 规划修改路径
  type: framework
  V1: {passed: true, reason: "p79-82 四页签路径与参数"}
  V2: {passed: true, check_mode: walkthrough, input: "改完 IP 连不上了", expected: "重启生效 + 用新地址连", observed: "p80-81 重启要求 + n11 旧会话失效解释"}
  V3: {passed: true, expected_benefit: "现场第一步的标准动作；证据归并 c02/p14/n11"}
  decision: verified

- id: f19
  title: OXO 接入 Rainbow 三段流程（找凭证→填入→Webdiag 验证）
  type: framework
  V1: {passed: true, reason: "p83-89 How-To 完整三段"}
  V2: {passed: true, check_mode: walkthrough, input: "接入后状态不对怎么排", expected: "Webdiag Rainbow Status 判据 + ccrbagent.log", observed: "p88 判据 'connected with final password' 与日志名明确；p16/n12 一致"}
  V3: {passed: true, expected_benefit: "混合闭环第一关口的操作与排障抓手；证据归并 c03/p15/p16/n12/n34"}
  decision: verified

- id: f20
  title: 成员创建路径（手工/邀请/CSV/Azure AD）
  type: framework
  V1: {passed: true, reason: "p92-95 四法逐一定义"}
  V2: {passed: true, check_mode: walkthrough, input: "500 人批量开户怎么做", expected: "CSV 模板或 Azure AD 同步", observed: "p94 CSV 规则（UTF-8/MAC 绑定/报告/SSO 密码留空）+ p95 AAD 门槛（Voice Enterprise）"}
  V3: {passed: true, expected_benefit: "批量开户方案选择；证据归并 c04/c05/p17/p18/n07/n15"}
  decision: verified

- id: f21
  title: 成员设置分区（7 分区 + Tags/Profiles 横向项）
  type: framework
  V1: {passed: true, reason: "p96 原文列 7 分区；p98 补 Tags/Profiles"}
  V2: {passed: true, check_mode: walkthrough, input: "开户要配哪些项", expected: "按 7 分区逐项核对", observed: "分区清单完整；OVERVIEW '八块'计数已修正（见 needs-review nr-03）"}
  V3: {passed: true, expected_benefit: "开户/排障的核对清单；证据归并 p19"}
  decision: verified

- id: f22
  title: 成员删除 10 天宽限流程与安全操作
  type: framework
  V1: {passed: true, reason: "p99-100 宽限期与 Security 页"}
  V2: {passed: true, check_mode: walkthrough, input: "误删后恢复账户能直接用吗", expected: "不能——回落 Essential，需重配许可+电话线", observed: "p99 原文明确；n13 三重副作用齐备"}
  V3: {passed: true, expected_benefit: "人员调整工单时序依据；证据归并 p20/p21/n13/n14"}
  decision: verified

- id: f23
  title: 分机关联与 RCC 验证四步（含 Rainbow number 机制）
  type: framework
  V1: {passed: true, reason: "p111-116 How-To + p115 Rainbow number 定义"}
  V2: {passed: true, check_mode: walkthrough, input: "RCC 用户呼叫纯 Rainbow 用户通吗", expected: "不通（无网关无音频通路）", observed: "p116 以测试问题呈现；n16 标注推断、机制自洽"}
  V3: {passed: true, expected_benefit: "无网关阶段交付与用户预期管理；证据归并 c06/p22/p23/n16/n17/n54"}
  decision: verified

- id: f24
  title: WebRTC 网关定位与来话/去话用例
  type: framework
  V1: {passed: true, reason: "p118-119 定位句 + 两张用例图"}
  V2: {passed: true, check_mode: walkthrough, input: "网关坏了影响呼叫控制吗", expected: "不影响——呼叫控制在 PBX", observed: "p118 'audio media relationship' 边界清晰；n18 排障分界"}
  V3: {passed: true, expected_benefit: "排障分流（媒体 vs 呼控）的概念依据"}
  decision: verified

- id: f25
  title: WebRTC 网关三拓扑对比（集成/FE/外部）与容量矩阵
  type: framework
  V1: {passed: true, reason: "p118/125/129 三拓扑要素 + p129 矩阵逐格核对"}
  V2: {passed: true, check_mode: walkthrough, input: "Power CPU EE 站点怎么上话音", expected: "OCE-FE（20）或外部 NUC/ESXi（50），集成不可用", observed: "p129 矩阵 Internal: Not supported (Power CPU EE) 与 n29/n30 一致"}
  V3: {passed: true, expected_benefit: "全书最核心的架构决策依据；证据归并 p28/p30/p31/n26-n30"}
  decision: verified

- id: f26
  title: 自动配置分工清单（自动建项 vs 安装员保留项）
  type: framework
  V1: {passed: true, reason: "p121-122/p150 两张分工清单一致"}
  V2: {passed: true, check_mode: walkthrough, input: "自动配置后能直接打电话吗", expected: "不能——终端/编号计划/闭锁仍是手工", observed: "p121 installer 清单明确；n21 书外边界诚实"}
  V3: {passed: true, expected_benefit: "交付工时估算与验收清单边界；证据归并 p25/n20/n21/n22"}
  decision: verified

- id: f27
  title: OXO 侧终端创建规则（Multiset + Twinset 副站 / 纯 Anydevice）
  type: framework
  V1: {passed: true, reason: "p123 规则完整含版本分界"}
  V2: {passed: true, check_mode: walkthrough, input: "R6.0 系统还按老办法建 Anydevice 副站行吗", expected: "不行——Twinset 强制且省 UTL", observed: "p123 原文 'must be used'；n23 版本陷阱"}
  V3: {passed: true, expected_benefit: "许可成本与升级交付的正确姿势；证据归并 p27/g08/g09"}
  decision: verified

- id: f28
  title: OCE Front End 部署链（FTR→Rainbow 激活→OMC 核验）
  type: framework
  V1: {passed: true, reason: "p128-135 各页证据连贯（FTR/占位 PBXID/端口 5059/warm reset）"}
  V2: {passed: true, check_mode: walkthrough, input: "FE 装完配置不生效", expected: "先确认 warm reset，再查 PBXID 双机一致", observed: "p132/p134 行为规则直接回答；n31/n32/n33 齐备"}
  V3: {passed: true, expected_benefit: "FE 拓扑的完整施工链；细节 Boundary 指向 cookbook（诚实外置）"}
  decision: verified

- id: f30
  title: 外部 WebRTC 网关部署（VMware 线 / NUC 线）
  type: framework
  V1: {passed: true, reason: "p139-145 两条线步骤与下载源"}
  V2: {passed: true, check_mode: walkthrough, input: "NUC 和 VM 怎么选", expected: "同 50 通话上限，按现场硬件条件", observed: "p144 同一软件包含 OVF+ISO，行为一致"}
  V3: {passed: true, expected_benefit: "50 通话扩容路径的施工入口；Boundary：TURN/白名单在书外（n36/n37）"}
  decision: verified

- id: f31
  title: 网关容量规划表（用户→通道对照 + 20/50/150 上限）
  type: framework
  V1: {passed: true, reason: "p147 表逐格核对：外部 5/7/11/15/20/27/36/50；集成 5/7/11/15/20 后 NA"}
  V2: {passed: true, check_mode: walkthrough, input: "80 个 Rainbow 话音用户怎么配", expected: "外部拓扑、通道介于 27-36，且 ≤50 通话上限", observed: "p36/p37 表内插 + p38 硬上限可答"}
  V3: {passed: true, expected_benefit: "售前报价与交付容量的查表依据；证据归并 p36/p37/n38/n39"}
  decision: verified

- id: f32
  title: 内部网关自动配置操作流（Reseller 激活→定通道→OMC 核验）
  type: framework
  V1: {passed: true, reason: "p149-154 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户管理员点不到激活按钮", expected: "仅 Reseller 管理员可激活", observed: "p151 'only authorized account'；n22 一致"}
  V3: {passed: true, expected_benefit: "R4.0.020.002+ 标准路径的施工与权责；证据归并 c08/p25/p26/n22"}
  decision: verified

- id: f33
  title: 虚拟终端配置流（Twinset 副站 / Anydevice 两条线 + UTL 口径）
  type: framework
  V1: {passed: true, reason: "p155-161 How-To + p156 UTL 公式"}
  V2: {passed: true, check_mode: walkthrough, input: "报许可数量怎么算", expected: "每电话用户 1 UTL（两种形态同价）", observed: "p156 两公式明确；p38/n23 互证"}
  V3: {passed: true, expected_benefit: "用户体验形态设计与许可核算；证据归并 c09/p27/p38/n23/n24"}
  decision: verified

- id: f34
  title: Attendant 话务台四功能区 + 三显示格式
  type: framework
  V1: {passed: true, reason: "p164-166 界面分区与容量"}
  V2: {passed: true, check_mode: walkthrough, input: "话务员能用手机值班吗", expected: "不能——仅 Web/Desktop", observed: "p164/p169 明确；n40"}
  V3: {passed: true, expected_benefit: "前台方案设计边界；证据归并 p39/p40/n40"}
  decision: verified

- id: f35
  title: 监督组结构规格（5 组/监督员、30 人/组、代接边界）
  type: framework
  V1: {passed: true, reason: "p167-169 规格与限制齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "40 人部门一个组建得下吗", expected: "不行——拆组（每组 ≤30）", observed: "p167 硬规格直接回答"}
  V3: {passed: true, expected_benefit: "话务监督方案容量设计；证据归并 p41/p42/n42/n43"}
  decision: verified

- id: f36
  title: 互助监督组机制（动态进出/临时纳排/代接边界）
  type: framework
  V1: {passed: true, reason: "p170-173 机制三要素"}
  V2: {passed: true, check_mode: walkthrough, input: "软话机用户能被代接吗", expected: "不能——代接仅限 PBX 电话呼叫", observed: "p171 原文明确；n44/n45 齐备"}
  V3: {passed: true, expected_benefit: "团队互助场景的需求边界管理；证据归并 p43/n44/n45"}
  decision: verified

- id: f37
  title: 话务台订阅与建组操作流（含互助组字段）
  type: framework
  V1: {passed: true, reason: "p175-181 How-To 完整（订阅/分配/建组/视图）"}
  V2: {passed: true, check_mode: walkthrough, input: "互助组和普通组建法差在哪", expected: "Type=Mutual aid group + Lock the last member + In/Out 权限", observed: "p180 字段清单明确"}
  V3: {passed: true, expected_benefit: "话务台交付的施工序列；证据归并 c10/c11/p12/n09"}
  decision: verified

- id: f38
  title: Rainbow 维护支持体系八件套
  type: framework
  V1: {passed: true, reason: "p183-193 八个抓手逐一定义"}
  V2: {passed: true, check_mode: walkthrough, input: "用户说 Rainbow 全挂了先查什么", expected: "status.openrainbow.com + 订阅告警", observed: "p186 状态页用途明确；p44/p45/p46 互证"}
  V3: {passed: true, expected_benefit: "售后运维闭环的抓手清单；证据归并 p44-p46/n46"}
  decision: verified

- id: f39
  title: MyPortal 开 SR 字段路径
  type: framework
  V1: {passed: true, reason: "p190-193 两页表单字段完整"}
  V2: {passed: true, check_mode: walkthrough, input: "SR 提交后没建单", expected: "查伙伴是否 Rainbow 认证", observed: "p191 认证前提（n47）"}
  V3: {passed: true, expected_benefit: "升级 ALE 官方的标准通道；证据归并 p47/n47"}
  decision: verified

- id: f40
  title: Teams 集成架构与四条呼叫流程
  type: framework
  V1: {passed: true, reason: "p196-206/p212-216 组件分工 + 流程步骤图"}
  V2: {passed: true, check_mode: walkthrough, input: "Teams 里打外线走哪条路", expected: "MakeCall → WebRTC 网关 → PSTN", observed: "p203 流程图明确；内呼走 CSTA（p202）对照"}
  V3: {passed: true, expected_benefit: "Teams 共存方案的技术底座；证据归并 p48/n48"}
  decision: verified

- id: f41
  title: Teams 部署四要素（上架/同意/订阅/权限收敛）
  type: framework
  V1: {passed: true, reason: "p207-210 四要素清单"}
  V2: {passed: true, check_mode: walkthrough, input: "Teams 用户要什么订阅", expected: "Business/Enterprise", observed: "p208 原文；p48/n49 一致"}
  V3: {passed: true, expected_benefit: "部署清单骨架；证据归并 c12/c13"}
  decision: verified

- id: f42
  title: Teams 应用上架与权限同意（两法 + Azure 核验）
  type: framework
  V1: {passed: true, reason: "p222-230 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "目录里搜不到 Rainbow App", expected: "Upload new app 传 zip；状态须 Allowed", observed: "p224 原文；n51 三坑齐备"}
  V3: {passed: true, expected_benefit: "租户侧施工序列；证据归并 c12/n51"}
  decision: verified

- id: f43
  title: Teams 集成用户配置三步（关联/Telephony 权限/订阅）
  type: framework
  V1: {passed: true, reason: "p231-235 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Teams 用户在 Rainbow 里还能聊天吗", expected: "建议收敛为 Telephony-only 权限", observed: "p234 官方建议原文；p48/n49 一致"}
  V3: {passed: true, expected_benefit: "用户侧配置标准；证据归并 c13"}
  decision: verified

- id: f44
  title: Teams 连接器安装与在场同步激活
  type: framework
  V1: {passed: true, reason: "p236-244 How-To + Desktop 依赖警告"}
  V2: {passed: true, check_mode: walkthrough, input: "装完 Teams App 状态不同步", expected: "激活 O365 信息共享（n53），且 Desktop 必须运行", observed: "p242-244 先测后开再复测的行为验证闭环"}
  V3: {passed: true, expected_benefit: "最高频现场问题的验收清单；证据归并 c14/n50/n52/n53"}
  decision: verified
```

## 断言级裁决记录

1. **principle 提取器"成员设置七块非八块"**：成立。p96 原文列 7 分区，p98 的 Tags/Profiles 为横向管理项；BOOK_OVERVIEW 的"八块"计数已在 f21 与 needs-review（nr-03）修正，以 7 分区口径为准。
2. **principle 提取器"密码规则未单列小写"**：成立。p53/p93/p94/p100 四处一致为"≥12 字符 + 大写 + 数字 + 特殊字符"，无小写显式要求；按原文记录，不补外部知识。
3. **counter-example 提取器"p121 与 p150 版本表述矛盾"**：成立并如实记录（n20）——"from R4.0.020.002" vs "greater than R4.0.020.002"。实践口径取 ≥R4.0.020.002、以更高版本执行；详见 needs-review nr-01。
4. **无 rejected 断言**：p147 容量表、p129 矩阵、5/30 规格、10/8 队列等关键数字均与原文逐格一致；第一本出现过的"公式矛盾"类误报本书未复现。
