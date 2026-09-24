# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f31（主验证对象）；principle/case/counter-example 作为各单元的证据素材归并；glossary 60 条转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 218 页全文通读 + 提取器页码证据

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 29 | f01-f18, f20-f30 |
| needs_review | 1 | f19（组间溢出配置入口缺失） |
| reference | 1 | f31（收尾恢复出厂，清单级粒度） |
| rejected | 1（断言级） | case-extractor 的"p184 公式矛盾"断言（见文末裁决记录） |

## 验证记录

```yaml
- id: f01
  title: ACD 呼入处理总框架（引擎架构 + 六场景清单）
  type: framework
  V1: {passed: true, reason: "p36 完整枚举六场景与引擎要素（Call Center Engine/CSTA/ACD ports），单处讲透"}
  V2: {passed: true, check_mode: walkthrough, input: "任意一条'来电行为异常'报障", expected: "可归入六场景之一并定位到对应流程", observed: "六场景互斥完备，覆盖 OPEN/CLOSED 全部分支"}
  V3: {passed: true, expected_benefit: "为全部呼入类报障提供统一排查主轴，减少漏判"}
  decision: verified

- id: f02
  title: 场景1 — 坐席可用处理流程
  type: flow
  V1: {passed: true, reason: "p37 单处完整流程；p77 验证语印证欢迎语先于转接"}
  V2: {passed: true, check_mode: walkthrough, input: "组开放、101 在值，呼入组1", expected: "欢迎语→转101", observed: "与 p77 验证步骤一致"}
  V3: {passed: true, expected_benefit: "定义基准行为，异常时有了对照"}
  decision: verified

- id: f03
  title: 场景2 — 坐席全忙进队列（阈值消息 + 星号退出）
  type: flow+decision
  V1: {passed: true, reason: "p38 流程图 + p112 实验双重证据"}
  V2: {passed: true, check_mode: walkthrough, input: "坐席全忙时呼入组1，来电者按*", expected: "先消息1后循环消息2；按*后可转邮箱或转号码退出", observed: "p112 明确给出两行为"}
  V3: {passed: true, expected_benefit: "队列行为可预期，出口配置有据"}
  decision: verified

- id: f04
  title: 场景3 — 队列满劝漏（第一劝漏形态）三出口
  type: decision+flow
  V1: {passed: true, reason: "p39 单处完整决策链"}
  V2: {passed: true, check_mode: walkthrough, input: "队列已满再来一通", expected: "按 转接>邮箱>劝漏语音 顺序判定出口", observed: "p39 决策链完整可走"}
  V3: {passed: true, expected_benefit: "劝漏行为可配置、可解释"}
  decision: verified

- id: f05
  title: 场景4 — 端口全忙劝漏（第二劝漏形态）
  type: decision+flow
  V1: {passed: true, reason: "p40 明确区分队列满与端口全忙两种劝漏触发"}
  V2: {passed: true, check_mode: walkthrough, input: "队列未满但 16 端口全忙", expected: "直接进劝漏态（专用端口）", observed: "p40 逻辑完整"}
  V3: {passed: true, expected_benefit: "'没排队就被挂断'类报障的定位入口"}
  decision: verified

- id: f06
  title: 场景5 — 全员登出 Transfer number（仅首呼转接）
  type: decision+flow
  V1: {passed: true, reason: "p41 + p97 双证据（流程 + 机制说明）"}
  V2: {passed: true, check_mode: walkthrough, input: "全员登出后连续 3 通来电", expected: "第1通转 Transfer number，第2/3通入队或劝漏", observed: "p97 明确 First/Subsequent 行为"}
  V3: {passed: true, expected_benefit: "'来电行为时好时坏'类投诉的定位要点"}
  decision: verified

- id: f07
  title: 场景6 — 组关闭处理流程
  type: flow
  V1: {passed: true, reason: "p42 流程 + p114 实验闭环"}
  V2: {passed: true, check_mode: walkthrough, input: "组3 置关闭态来话", expected: "关闭语→释放；可改转接/邮箱", observed: "p114 实验答案一致"}
  V3: {passed: true, expected_benefit: "非营业时段行为可控"}
  decision: verified

- id: f08
  title: ACD Setup 向导五步配置流程
  type: procedure
  V1: {passed: true, reason: "p43-48 五页签+生效条件完整（OK 后须重启 ACD 引擎）"}
  V2: {passed: true, check_mode: walkthrough, input: "新客户 3 组需求", expected: "五步产出可用 ACD 骨架", observed: "步骤、页签、生效动作齐全"}
  V3: {passed: true, expected_benefit: "初始配置标准化，漏重启引擎这一高频错误被显式覆盖"}
  gaps_as_boundary: "端口数规划依据书中未给（仅上限16）"
  decision: verified

- id: f09
  title: 向导后台生成物清单 + signalization mode 前置检查
  type: framework
  V1: {passed: true, reason: "p80-85 逐项列出五类生成物与系统开关"}
  V2: {passed: true, check_mode: walkthrough, input: "坐席话机不显示来话", expected: "先查 signalization mode 是否误开（Feature design/part 2）", observed: "p85 给出判据与两态表现"}
  V3: {passed: true, expected_benefit: "避免与向导生成物'打架'，前置检查有清单"}
  decision: verified

- id: f10
  title: 基础 ACD 搭建完整规程（8 步）
  type: procedure
  V1: {passed: true, reason: "p69-77 全参数在文（前缀501-504、组505-507/DDI41505-07、rank 配置、语音下载）"}
  V2: {passed: true, check_mode: walkthrough, input: "三组需求+话机101/102/103", expected: "8 步后实呼验证通过", observed: "步骤含菜单路径与验证清单（4 菜单核对+实呼+四态测试）"}
  V3: {passed: true, expected_benefit: "task-03 核心交付，从零到可接听的全路径"}
  gaps_as_boundary: "实验密码/实验语音仅为实验值；生产需替换"
  decision: verified

- id: f11
  title: OMC 安装与首次连接规程
  type: procedure
  V1: {passed: true, reason: "p54-64 安装+Expert首连+证书+改密+客户信息全链"}
  V2: {passed: true, check_mode: walkthrough, input: "出厂设备+管理员PC", expected: "获得可用 OMC 连接", observed: "步骤完整含证书安装细节"}
  V3: {passed: true, expected_benefit: "首装即对，消除安全告警反复弹窗"}
  gaps_as_boundary: "pbxk1064 为出厂默认值，生产必须改（书中已提示每客户不同）"
  decision: verified

- id: f12
  title: OXO 与客户端 IP 规划修改规程
  type: procedure
  V1: {passed: true, reason: "p65-68 两侧参数与菜单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "改网段为客户 10.x", expected: "OXO 重启+PC 侧修改后可 RDP", observed: "p65-66 明确先 OXO 后 PC、改后 RDP 可连"}
  V3: {passed: true, expected_benefit: "现场交付第一步标准化"}
  decision: verified

- id: f13
  title: 呼叫特征化三级优先匹配决策
  type: decision
  V1: {passed: true, reason: "p86-88 优先级、比较方向、适用范围三要素齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "CLI=00441234 呼 DDI=41505；表内条目A(0044,空) 条目B(00441234,41505)", expected: "命中条目B（双匹配优先级#1）", observed: "按三级序与方向规则推演一致"}
  V3: {passed: true, expected_benefit: "路由不生效时按'命中级别+方向'两维定位"}
  decision: verified

- id: f14
  title: 路由表填写顺序 + 按国别/大客户分流规程
  type: decision+procedure
  V1: {passed: true, reason: "p88 硬规则（特殊→一般）+ p116 完整实验"}
  V2: {passed: true, check_mode: walkthrough, input: "三国分流+三大客户双条件+兜底", expected: "大客户双匹配在前、国别在后、兜底最后", observed: "p116 场景与规则吻合"}
  V3: {passed: true, expected_benefit: "避免一般条目截胡特殊条目这一隐蔽错误"}
  gaps_as_boundary: "行序截图未提取，行间优先级以'特殊→一般'原则为准"
  decision: verified

- id: f15
  title: 坐席搜索模式三选一 + 与 rank 的正交关系
  type: decision
  V1: {passed: true, reason: "p95 三模式定义 + p97 Priority order（组间）+ p109 实验"}
  V2: {passed: true, check_mode: walkthrough, input: "组1 Fixed/组2 Longest idle/组3 Rotating 配置", expected: "三组分配行为可区分并可实测", observed: "p109-111 实验设计即为此"}
  V3: {passed: true, expected_benefit: "组策略选型有依据；rank 与 search mode 不再混谈"}
  decision: verified

- id: f16
  title: 排障：无应答呼叫走向（振铃上限 vs 自动移除两档）
  type: troubleshooting
  V1: {passed: true, reason: "p110-111 两档行为均有原文给定标准答案"}
  V2: {passed: true, check_mode: walkthrough, input: "组3 三坐席均不接听", expected: "A 档：103→102→101 循环；B 档：103→102(103转off duty)→101 钉死", observed: "与 p110-111 一致"}
  V3: {passed: true, expected_benefit: "'坐席陆续变 off duty'的怪象有直接判据"}
  decision: verified

- id: f17
  title: 队列长度决策公式（ceil(N×K)，上限 16）
  type: decision+calculation
  V1: {passed: true, reason: "p93 公式+取整规则+上限+示例（4×0.5=2）；p184 实验交叉印证"}
  V2: {passed: true, check_mode: walkthrough, input: "组1 坐席101/102 在值（N=2），K=2.0", expected: "队列=4", observed: "p184 实测 1→4，吻合（注意 N 只数 On duty）"}
  V3: {passed: true, expected_benefit: "队列容量按话务设定而非拍脑袋"}
  validation_note: "case-extractor 曾判 p184 与公式矛盾——系其误将组1坐席数当 4；按 p75 组1 实为 2 坐席，2×2.0=4 吻合。断言撤销。"
  decision: verified

- id: f18
  title: 预计等待时间公式与队列消息选项
  type: decision+calculation
  V1: {passed: true, reason: "p94 公式与参数（Average duration）完整"}
  V2: {passed: true, check_mode: walkthrough, input: "队列3通、在值2坐席、平均通话240s", expected: "预计等待=(3/2+1)×240=600s", observed: "公式代入一致"}
  V3: {passed: true, expected_benefit: "Queue rank/Queue time 消息阈值配置有计算依据"}
  gaps_as_boundary: "线性模型，高峰低估（批判阶段结论）"
  decision: verified

- id: f20
  title: 营业时段与例外日配置规程
  type: procedure
  V1: {passed: true, reason: "p100 上限（40闭/10开/每日2时段）+ p108 完整实验"}
  V2: {passed: true, check_mode: walkthrough, input: "周一至五 8-12/13-18，元旦/五一/圣诞关闭，组1 圣诞 9:30-11:30 例外开放", expected: "常规+例外两层配置后行为正确", observed: "p108 步骤覆盖"}
  V3: {passed: true, expected_benefit: "节假日呼叫行为可控可解释"}
  decision: verified

- id: f21
  title: Login/Logout 与 free seating（含 ACDAutoLog）
  type: flow+decision
  V1: {passed: true, reason: "p119-123 四要素建链、登录登出流程、ACDAutoLog 01/00 齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "坐席在异终端拨登录前缀", expected: "建链成功进入 ACD 会话；登出 base0 前缀/Essential 需 OK 确认", observed: "p121 流程一致"}
  V3: {passed: true, expected_benefit: "'登录了却不接电话'先查 ACDAutoLog=00"}
  gaps_as_boundary: "ACDAutoLog 写入路径书中未给（已知条目名与取值）"
  decision: verified

- id: f22
  title: 排障：话机 ACD 状态码解读
  type: troubleshooting
  V1: {passed: true, reason: "p122 三条主码（1:01 队列有话 / 1:01+ 队满 / 1-00 组关闭）语义明确"}
  V2: {passed: true, check_mode: walkthrough, input: "话机显示 1:01+ ", expected: "判读：属组1、开放、1 通等待且队满", observed: "p122 原文定义直接映射"}
  V3: {passed: true, expected_benefit: "坐席侧一线排障第一入口"}
  gaps_as_boundary: "'属于/不属于开放组'两变体的显示符号原文疑似缺漏（两条均印作 1:01），需实机核对——已单独登记 needs-review"
  decision: verified

- id: f23
  title: 组显示模式框架（ACD mode / Multi-Secretary mode）
  type: framework
  V1: {passed: true, reason: "p89-90 + p107 双证据（两模式显示内容与三元组）"}
  V2: {passed: true, check_mode: walkthrough, input: "转接中话机显示 France 0123456789 00:45", expected: "解读为[组名][主叫][等待时长]", observed: "p107 原文格式一致"}
  V3: {passed: true, expected_benefit: "多秘书场景'知道替谁接'的机制解释与组名维护路径"}
  decision: verified

- id: f24
  title: Multi-Secretary 配置全流程（10 步）
  type: procedure
  V1: {passed: true, reason: "p126-146 讲义+实验闭环，顺序要求明确（following order）"}
  V2: {passed: true, check_mode: walkthrough, input: "3 医生(105-107/DDI 41505-07)+2 秘书(101/102)", expected: "按序配置后秘书席显示被叫姓名，关闭时段转邮箱", observed: "p140-146 步骤与验证问题一致"}
  V3: {passed: true, expected_benefit: "方案级场景从销售承诺到落地的完整路径"}
  gaps_as_boundary: "MS 模式激活的具体控件名书中未单列（General tab 截图页）"
  decision: verified

- id: f25
  title: Supervisor 应用部署规程
  type: procedure
  V1: {passed: true, reason: "p150-165 密码分离原则、周期参数、安装、首连、验证齐全"}
  V2: {passed: true, check_mode: walkthrough, input: "班长 PC + Acdc1064", expected: "实时视图可用，5 分钟来话后 activity rate 上升", observed: "p164 验证法明确"}
  V3: {passed: true, expected_benefit: "班长台标准化部署；密码不外泄 installer 凭据"}
  gaps_as_boundary: "工具栏/监控图标两页为纯图未提取"
  decision: verified

- id: f26
  title: 坐席实时子状态解读（On Duty 八子态 + 三主态）
  type: framework
  V1: {passed: true, reason: "p164 逐条定义八子态，术语提取器已勘误确认（非九种）"}
  V2: {passed: true, check_mode: walkthrough, input: "坐席显示 On hold", expected: "判读：刚结束 ACD 通话的休整期，非故障", observed: "p164 定义一致"}
  V3: {passed: true, expected_benefit: "'坐席忙却不接 ACD'类问题按子状态定位"}
  decision: verified

- id: f27
  title: Agent 应用部署规程
  type: procedure
  V1: {passed: true, reason: "p99, p166-184 架构、关联、安装、验证完整"}
  V2: {passed: true, check_mode: walkthrough, input: "PC 关联话机102", expected: "状态切换/组变更/弹屏/打标四项验证通过", observed: "p181-184 实验步骤与预期结果齐备"}
  V3: {passed: true, expected_benefit: "坐席席面标准化部署与验证"}
  gaps_as_boundary: "p183 'agent 1002' 疑为 102 笔误（按上下文理解）"
  decision: verified

- id: f28
  title: DTMF 客户识别弹屏流程
  type: flow
  V1: {passed: true, reason: "p101-102 机制 + 三处前置配置齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "来电输 035#", expected: "席面弹出 Customer code=035", observed: "p101 行为定义明确"}
  V3: {passed: true, expected_benefit: "VIP 弹屏需求落地；不弹屏时三点排查清单"}
  decision: verified

- id: f29
  title: Statistics 应用部署与查询/导出规程
  type: procedure
  V1: {passed: true, reason: "p185-209 参数（S1=10s/S2=40s）、连接、查询、打印、导出全链"}
  V2: {passed: true, check_mode: walkthrough, input: "查组1-3 本月来话/应答 3D 柱状图并导出 CSV", expected: "按步骤可产出", observed: "p206-207/202 步骤一致"}
  V3: {passed: true, expected_benefit: "统计报表交付标准化；binary/CSV 用途区分清晰"}
  gaps_as_boundary: "Line/Calls statistics 两图标未展开实验"
  decision: verified

- id: f30
  title: ACD 语音提示定制规程
  type: procedure
  V1: {passed: true, reason: "p104-105, p135-136 编号规则（101=欢迎…x07=客户码）+ 两条制作路径"}
  V2: {passed: true, check_mode: walkthrough, input: "为组1-3 定制医生场景欢迎/等待/关闭语", expected: "MMC 话机录制或 OMC 四步上传后实呼生效", observed: "p135 给出逐条话术示例与路径"}
  V3: {passed: true, expected_benefit: "本地化语音交付有编号规范可循"}
  gaps_as_boundary: ".wav 采样率/编码参数为截图未提取"
  decision: verified
```

## 裁决记录（重要）

1. **撤销 case-extractor 的"p184 公式矛盾"断言**：其假设组1 有 4 名坐席（4×2.0=8≠4）。按 p75 实验配置，组1 仅含坐席 101/102（N=2），2×2.0=4 与 p184 实测完全吻合。该断言 rejected，公式 f17 保持 verified。
2. **术语勘误采纳**：阶段 0 的"九种子状态"口误已纠正为 On Duty 八子态（f26 以原书口径收录）。
3. **原则/案例/反例的归并**：62 条原则、24 条案例、21 条反例不作为独立单元验证，按证据类型归并进上列单元（公式→f17/f18；实验→各单元 A1；反例→各单元 B）。归并映射在 coverage-audit.md 登记去向。
