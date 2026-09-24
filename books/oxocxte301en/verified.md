# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f36（主验证对象）；principle p01-p50 / case c01-c24 / counter-example n01-n65 作为各单元的证据素材归并；glossary g01-g62 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 601 页全文通读 + 提取器页码证据交叉核对

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 34 | f01, f04-f36（f02/f03 除外全部，详见下表） |
| reference | 2 | f02（RLAB 平台结构）、f03（ITSP1 模拟器拓扑——实验专用基础设施，取值仅作 Boundary 背景） |
| needs_review | 0（单元级） | 断言级 8 项转 needs-review.md（Internal ARS 时段、DHCP 池、法文残留、OXE 素材、门户域名、链路类别取值、5061 端口双身份、Max entries 留白） |
| rejected | 0 | 无编造断言；关键数字（九 tab 顺序、200/200、MLAA 12000 秒、SCR 10000 规则、DECT 80/60/200、-72 dBm、50443）均逐格核对一致 |

verified 明细：f01, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36

## 验证记录

```yaml
- id: f01
  title: 全书课程推进主线——实验环境地基 → 公网外联 → 三大能力域 → 云/安全/DECT 进阶 → 维护收尾
  type: flow
  V1: {passed: true, reason: "p3-601 章节封面齐全；BOOK_OVERVIEW 骨架与目录一致"}
  V2: {passed: true, check_mode: walkthrough, input: "进阶交付按什么顺序学/做", expected: "环境→外联→能力域→进阶→维护的推进", observed: "十段推进与 31 项任务清单互证；隐含主线（OMC/Webdiag 双工具 × 编号计划/中继组/ARS 三件套）在 f05/f06/f13/f15 反复出现"}
  V3: {passed: true, expected_benefit: "全书组织轴，交付排期与学习路径的顺序基线"}
  decision: verified

- id: f02
  title: RLAB 远程实验平台结构——POD 池 + 公共资源区双网段
  type: structure
  V1: {passed: true, reason: "p5-13 拓扑与参数完整"}
  V2: {passed: true, check_mode: walkthrough, input: "实验环境里各设备的地址关系", expected: "POD 网段与公共区分离", observed: "p6 双网段结构清晰；全部为实验口径"}
  V3: {passed: true, expected_benefit: "实验复现背景；生产无对应物，只作 Boundary 引用"}
  decision: reference

- id: f03
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则
  type: diagram
  V1: {passed: true, reason: "p16-22 拓扑/账号/号码规则完整"}
  V2: {passed: true, check_mode: walkthrough, input: "公网 SIP 实验的号码怎么变换", expected: "呼出加 + 前缀、呼入按 DDI 段映射", observed: "p19 变换规则与 p21 号码段自洽；全部为实验口径"}
  V3: {passed: true, expected_benefit: "理解 SIP 中继两侧号码计划的参照系；生产运营商参数在书外"}
  decision: reference

- id: f04
  title: IPDSP 安装前置流程——IP 先行 + NTP 时间同步
  type: flow
  V1: {passed: true, reason: "p14 前提与报错机制完整（lanpbx 加载错误 ↔ 证书校验失败）"}
  V2: {passed: true, check_mode: walkthrough, input: "IPDSP 装不上报 lanpbx 错误怎么判", expected: "先查 PC 与 OXO 时间差而非文件损坏", observed: "p14 机制链直接回答；n01 归并完整"}
  V3: {passed: true, expected_benefit: "证书时代装机的时间先行原则，避免误判返工；证据归并 p01/n01"}
  decision: verified

- id: f05
  title: 公网 SIP 网关配置九步顺序（含 tab 依赖关系）
  type: flow
  V1: {passed: true, reason: "p37-56 How-To 逐步给出；p44/p46-47 两处顺序约束显式"}
  V2: {passed: true, check_mode: walkthrough, input: "按九步走一遍能否注册成功", expected: "History Table 出现 SIP registration success", observed: "c03 步骤 9 验收点与 p54 一致；两条硬顺序（DNS 先于 Domain Proxy、网关索引回填）由 p05/n04/n05/n06 互证"}
  V3: {passed: true, expected_benefit: "对接运营商的标准动作与高频踩坑点前置；证据归并 c03/p03/p04/p05/p06/n04-n07"}
  decision: verified

- id: f06
  title: SIP 中继排障三件套——注册历史表 / Webdiag 抓包 / Wireshark 分析
  type: flow
  V1: {passed: true, reason: "p54-56 三层路径 + p167-170 话机维度补充"}
  V2: {passed: true, check_mode: walkthrough, input: "注册成功但通话异常怎么分层排查", expected: "注册层看历史表、信令层 Webdiag 抓包、分析层 Wireshark", observed: "p55-56 抓包流程与存档发支持的出口明确；SIP 话机维度 p170 三工具齐备"}
  V3: {passed: true, expected_benefit: "售后排障闭环的标准分层；证据归并 n17/n18/n19"}
  decision: verified

- id: f07
  title: 酒店方案双路线架构——OHL/PMS 联动 vs 前台话机内置 Hotel 功能
  type: diagram
  V1: {passed: true, reason: "p57-68 架构图与两路线规格完整"}
  V2: {passed: true, check_mode: walkthrough, input: "无 PMS 的小旅馆能不能上酒店功能", expected: "走前台话机内置 Hotel 功能键路线", observed: "p64 无 OHL 路线规格（4 并发会话/300 话机/房对房闭锁）支持该表述；p07 清单齐备"}
  V3: {passed: true, expected_benefit: "垂直项目选型的第一分叉；证据归并 p07/g11/g12"}
  decision: verified

- id: f08
  title: 计费体系三通道——Hotel Metering / Call Accounting Time based / OLD 的 IP/V24 输出
  type: structure
  V1: {passed: true, reason: "p72-91 参数与输出通道完整"}
  V2: {passed: true, check_mode: walkthrough, input: "无 AOC 中继怎么出计费脉冲", expected: "Call Accounting Time based 按时长×呼型补", observed: "p82-83 规则与互斥条款（激活即停 AOC）逐格一致；TicketCollector.xml 路径 p80/91 一致"}
  V3: {passed: true, expected_benefit: "计费/对账方案的三选一依据；证据归并 p08/p09/c05/n09"}
  decision: verified

- id: f09
  title: SIP 呼叫处理架构——Registrar/B2BUA 与三种语音路径（DSP/RTP proxy/Direct RTP）
  type: diagram
  V1: {passed: true, reason: "p140-148 注册面/呼叫面/媒体面三段完整"}
  V2: {passed: true, check_mode: walkthrough, input: "SIP 话机通话单向上声或 CPU 高怎么选媒体路径", expected: "三处理取舍：DSP→RTP proxy→Direct RTP", observed: "p148 三定义与 p15 开关矩阵互证；TLS 场景 Direct RTP 不可用（p368）反证一致"}
  V3: {passed: true, expected_benefit: "SIP 话机接入的容量与质量决策底座；证据归并 p14/p15/g23/g24"}
  decision: verified

- id: f10
  title: PIMphony 四 profile 体系与安装配置流程
  type: structure
  V1: {passed: true, reason: "p119-138 profile 阶梯与两级更新策略完整"}
  V2: {passed: true, check_mode: walkthrough, input: "给用户配 PC 软话机按什么顺序", expected: "全局开更新→用户预配 profile→装客户端→向导关联", observed: "c08 序列与 p127-128 参数一致；虚拟课堂不可实操（p129）不影响机制验证"}
  V3: {passed: true, expected_benefit: "PC 中心用户场景的完整施工链；证据归并 p13/c08/n15"}
  decision: verified

- id: f11
  title: Hot Desking 组件关系——HDU/HDP/前缀/Webdiag 监督
  type: diagram
  V1: {passed: true, reason: "p173-183 关系、容量、前缀、监督四要素完整"}
  V2: {passed: true, check_mode: walkthrough, input: "共享工位话机怎么保证个人环境跟随", expected: "HDU 在任意 HDP 用 683 登录取回个人环境", observed: "p174-175 机制 + p16 容量口径（200/200、前 2 免费）逐格一致；抢占自动注销行为明确"}
  V3: {passed: true, expected_benefit: "工位共享场景的方案与许可口径；证据归并 p16/c10/n20/g07/g32/g33"}
  decision: verified

- id: f12
  title: Multiset 结构与呼叫呈现规则
  type: diagram
  V1: {passed: true, reason: "p184-192 结构规格与 MLTSETRING 三值完整"}
  V2: {passed: true, check_mode: walkthrough, input: "主副话机来话各怎么响、外呼显示哪个号", expected: "组呼全铃、空闲副站按 MLTSETRING、外呼显示主站号", observed: "c11 七项行为验证与 p185-188 规格互证；注意与 Rainbow 侧 Twinset 同名不同物"}
  V3: {passed: true, expected_benefit: "有线+移动用户刚需方案；证据归并 p17/c11/n21（法文残留勘误）"}
  decision: verified

- id: f13
  title: ARS 三表协作机制与号码变换四原则
  type: diagram
  V1: {passed: true, reason: "p193-205 机制链与字段表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "拨一个外线号码系统怎么选中继", expected: "编号计划触发 ARS → ARS 表匹配变换 → 中继组列表按序选路", observed: "p195 流程与 p202 四原则（加/吸收/替换/透明）一致；时间维度（p204 Day Groups/Hours）为 Internal ARS 提供基础"}
  V3: {passed: true, expected_benefit: "全书路由域的概念中枢；证据归并 g02"}
  decision: verified

- id: f14
  title: 多运营商分流示例图——GSM 网关/低价 VoIP/ISDN 备份三路
  type: diagram
  V1: {passed: true, reason: "p197-201 拓扑与表格数值完整"}
  V2: {passed: true, check_mode: walkthrough, input: "移动呼叫走 GSM、其它走低价 VoIP、ISDN 备份怎么配", expected: "ARS 表两行 + 两个列表共享子线索引 3 + 传真走流量分担矩阵", observed: "p198-201 数值逐格一致（列表 1=[2:400,3:401]、列表 2=[4:402,3:401]，矩阵 401=+）"}
  V3: {passed: true, expected_benefit: "多运营商降本方案的标准构图；证据归并 p18/g02"}
  decision: verified

- id: f15
  title: 私网 SIP 组网与双向溢出架构（两台 OXO 互联）
  type: diagram
  V1: {passed: true, reason: "p206-224 八节配置与四里程碑验证完整"}
  V2: {passed: true, check_mode: walkthrough, input: "两站点互拨+私网饱和溢出公网怎么落地", expected: "私网网关+副中继组+ARS 双向四步，验证字符 P/T", observed: "c12 四个里程碑（无 ARS 通/带 ARS 通/溢出 T/强制 P）与 p218-224 一致；带宽最少 5 通话规则同公网（p215）"}
  V3: {passed: true, expected_benefit: "多站点组网核心；证据归并 c12/p05/p18/n22"}
  decision: verified

- id: f16
  title: Internal ARS 决策链——一个 DDI 按日组/时段分流到不同内部目的地
  type: diagram
  V1: {passed: true, reason: "p225-241 决策链五级完整；p449 操作页补充"}
  V2: {passed: true, check_mode: walkthrough, input: "同一 DDI 营业时间转分机、非营业时间播欢迎消息怎么配", expected: "公网编号计划 base ARS + 子线替换 + 虚拟 Provider + Local 列表 + Day Groups/Hours", observed: "c13 九步与 p228-237 技法一致；时段取值两处不一致（p233 vs p449）已转 nr-01，不影响机制"}
  V3: {passed: true, expected_benefit: "把外呼路由机制反转为来电分配，思路价值最高；证据归并 p19/c13/n23/n24"}
  decision: verified

- id: f17
  title: 多实体（Entity）架构——MoH 隔离、呼叫限制与话务员组公共
  type: diagram
  V1: {passed: true, reason: "p242-251 架构与参数表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "两家公司共享系统怎么隔离保持音乐与外线记账", expected: "4 实体 MoH 隔离 + 禁呼开关 + 伪多公司链路类别配对", observed: "p243-248 参数逐格一致（4 实体/MoH 10 分钟/问候 200/预告 20/消息 320 秒）；n25 连带影响清单齐备"}
  V3: {passed: true, expected_benefit: "共享系统多客户场景的隔离设计依据；证据归并 p20/p21/c14/n24/n25/g04/g05"}
  decision: verified

- id: f18
  title: Cloud Connect 架构——OXO 发起的双连接与两门户
  type: diagram
  V1: {passed: true, reason: "p262-289 架构、门户、注册链完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户防火墙要不要为云管理开洞", expected: "不用——OXO 主动发起永久 HTTPS + 按需 VPN", observed: "p264 原文直接回答；注册自动/免 license/默认启用（p287）与 c15 验证串一致；域名两种写法已转 nr-05"}
  V3: {passed: true, expected_benefit: "云运维的第一性认知（免改防火墙 + 24h 延迟）；证据归并 p22/c15/n52/n58/g18-g20"}
  decision: verified

- id: f19
  title: Cloud Connect 软件更新流程与状态指示灯
  type: flow
  V1: {passed: true, reason: "p269-273 三步流程与指示灯语义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "舰队软件版本治理怎么触发与授权", expected: "Connect→Check（[D..]/[.S.]/[..P]）→Update，需 advanced 权限", observed: "p23 规则与 p271-273 原文逐格一致；两门户权限要求一致（n53）"}
  V3: {passed: true, expected_benefit: "批量运维刚需的操作与权限口径；证据归并 p23/n53"}
  decision: verified

- id: f20
  title: 远程维护四种接入路径图
  type: diagram
  V1: {passed: true, reason: "p290-306 四路径与端口铁律完整"}
  V2: {passed: true, check_mode: walkthrough, input: "纯 SIP 中继站点怎么远程维护", expected: "只能走 IP 通道，互联网入站目标端口永远 50443", observed: "p300/p303 两处铁律一致（n50）；SIP-only 限制 p299（n51）；管理 VPN 仅 OMC 可配且 warm reset 生效"}
  V3: {passed: true, expected_benefit: "无 ISDN 站点唯一远程通道的选型与安全口径；证据归并 p24/n50/n51"}
  decision: verified

- id: f21
  title: 系统安全体系结构——密码树/自动检查/审计/网络面收敛
  type: structure
  V1: {passed: true, reason: "p311-338 五块结构完整"}
  V2: {passed: true, check_mode: walkthrough, input: "上线前安全基线做哪些", expected: "强制改密+自动检查（AutoPwdChk 4 周）+网络面三开关+ETH1 限制+锁定公式+加固清单", observed: "p25/p26/p41-p44 与 p315-338 逐格一致；VMU 锁定翻倍公式 p328/384 两处一致"}
  V3: {passed: true, expected_benefit: "生产级安全基线的执行清单；证据归并 p25-p27/p41-p44/n46-n48"}
  decision: verified

- id: f22
  title: 数字证书体系总表与 2K→4K 升级路径
  type: structure
  V1: {passed: true, reason: "p339-358 证书四类/端口矩阵/升级路径完整"}
  V2: {passed: true, check_mode: walkthrough, input: "升 4K 后想回滚旧版本行不行", expected: "先经 WebDIAG 切回 2K 再回滚，否则 OMC 报错", observed: "p357 原文与 n41 一致；证书端口矩阵 p346-356 逐格核对（443/30443/50443/7780/10443/11443）"}
  V3: {passed: true, expected_benefit: "R6.2 合规证书体系的操作与回滚铁律；证据归并 p37/p38/n40/n41/g56"}
  decision: verified

- id: f23
  title: DTLS 原生加密双模式与端点清除三法
  type: flow
  V1: {passed: true, reason: "p359-364 部署/模式/清除三段完整"}
  V2: {passed: true, check_mode: walkthrough, input: "话机跨系统移动后注册不上怎么办", expected: "OXO↔OXE 必须清 TrustList（三法之一）", observed: "p363 三法与 n40/n62 一致；300 连接/免 license/仅 OCE 口径 p360 逐格一致"}
  V3: {passed: true, expected_benefit: "话机信令加密的正确预期（保信令不保语音）；证据归并 p40/n62"}
  decision: verified

- id: f24
  title: SIP 中继 TLS/SRTP 双实现——OCE 原生 vs OCE-FE SIP PROXY
  type: diagram
  V1: {passed: true, reason: "p365-378 两用例与容量表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "OCO 老平台要接加密中继怎么补", expected: "经 OCE-FE SIP PROXY 转发，GW 与 PROXY 各 20 通话", observed: "p375 容量表逐格一致；四项全局共享/SIPS 不支持/ETH1 不走 SIP 三条边界（n43）齐备"}
  V3: {passed: true, expected_benefit: "运营商加密要求的两条落地路径；证据归并 p39/n42-n45"}
  decision: verified

- id: f25
  title: 语音邮箱服务结构——端口分配/远程接入/ACC 两级控制/锁定
  type: structure
  V1: {passed: true, reason: "p379-393 端口/远程三要素/ACC/锁定完整"}
  V2: {passed: true, check_mode: walkthrough, input: "远程查邮箱要过几道认证", expected: "DDI+（ACC 可选两级）+分机号+密码；锁定翻倍封顶 1440 分钟", observed: "p383 ACC 规则与 p26 公式逐格一致；默认值矩阵（迁移 vs 冷复位）p382/n60 一致"}
  V3: {passed: true, expected_benefit: "防盗打与移动办公的语音邮箱闭环；证据归并 p26/p27/p45/c16/n54/n60/g16"}
  decision: verified

- id: f26
  title: 自动话务员 AA 树结构与免费拨号机制
  type: diagram
  V1: {passed: true, reason: "p405-421 规格表与 noteworthy 开关完整"}
  V2: {passed: true, check_mode: walkthrough, input: "新装机外呼进来是语音菜单是不是故障", expected: "不是——冷复位后默认 2 端口进组 8 接外呼", observed: "p409/n59 直接回答；树规格（2 树/2 级 100 节点/4 语言）与 p28 逐格一致"}
  V3: {passed: true, expected_benefit: "企业语音门面的部署与新机验收口径；证据归并 p28/p29/c17/n59"}
  decision: verified

- id: f27
  title: MLAA 多树话务员结构——ACD 引擎/树编辑器/语音文件组织
  type: structure
  V1: {passed: true, reason: "p427-442 规格/编辑器/语音组织完整"}
  V2: {passed: true, check_mode: walkthrough, input: "MLAA 配置传了怎么没生效", expected: "端口与消息改动需 ACD 引擎复位或等 10 分钟", observed: "p431/p441 两处一致（n27）；12000 秒总限、100 消息×4 语言、line parameters 不随存档（n26）逐格一致"}
  V3: {passed: true, expected_benefit: "多业务线入口的规格与排障口径；证据归并 p30/c18/n26/n27/g35"}
  decision: verified

- id: f28
  title: Smart Call Routing 决策流程——线选择→目的地选择两段式
  type: diagram
  V1: {passed: true, reason: "p450-458 决策流与规格表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "按客户码分流来话怎么建规则", expected: "CLI/DDI 匹配 + 客户码 DTMF 校验 + 开闭目的地 + 备份目的地", observed: "c19 实验闭环与 p451/p454-457 一致；10000 规则/10 计划/64 特殊日/8 VP 逐格一致"}
  V3: {passed: true, expected_benefit: "客服分客户场景的规则引擎；证据归并 p31/c19/g36"}
  decision: verified

- id: f29
  title: 语音移动方案全景与游牧/远程替代拓扑
  type: diagram
  V1: {passed: true, reason: "p463-480 全景与两条链路完整"}
  V2: {passed: true, check_mode: walkthrough, input: "手机在外要接分机电话、回拨内部怎么实现", expected: "游牧模式（VMU 选项 6）+远程替代（DDI+接入码+# 前缀内部 ARS）", observed: "c20 十步与 p466-480 一致；CLI 三选一规则（p466）与三级默认关（n54）逐格一致；SIP 话机不支持游牧（p147）"}
  V3: {passed: true, expected_benefit: "移动办公核心场景；证据归并 p32/p33/c20/n16/n54/g08/g09"}
  decision: verified

- id: f30
  title: DECT 标准与标识体系——FDMA/TDMA/TDD 帧结构 + 五种标识号
  type: diagram
  V1: {passed: true, reason: "p498-503 标准/帧结构/标识完整"}
  V2: {passed: true, check_mode: walkthrough, input: "PARI/PARK/IPUI 各标识谁", expected: "PARI=系统安装 ID、RFPI=xBS、PARK=话机侧系统标识、IPUI=话机身份", observed: "p502 五件套定义一致（原注法文已转 nr-03）；每 xBS 12 时隙 11 并发与 p34 容量口径一致"}
  V3: {passed: true, expected_benefit: "无线子系统的概念底座；证据归并 p34/g51/g62"}
  decision: verified

- id: f31
  title: DECT 拓扑与同步/切换机制——集群、站点、Relay xBS
  type: diagram
  V1: {passed: true, reason: "p504-517 层级/同步/切换完整"}
  V2: {passed: true, check_mode: walkthrough, input: "两栋楼相距 1.5km 能不能漫游切换", expected: "站间不切换；切换仅同集群内", observed: "p506-508 与 n29/n30 一致（同步优先于信号强度，xBS 与 TDM IBS 间必然如此）；80 xBS/200 手柄/60 IBS 容量逐格一致"}
  V3: {passed: true, expected_benefit: "无线覆盖规划的边界认知；证据归并 p34/g25/n29/n30"}
  decision: verified

- id: f32
  title: IP-DECT 部署与站点勘测流程（SSK）
  type: flow
  V1: {passed: true, reason: "p515-534 部署四步/SUOTA/勘测口径完整"}
  V2: {passed: true, check_mode: walkthrough, input: "覆盖验收以什么为准", expected: "-72 dBm 划语音质量区 + 通话中测音质（最少两台话机）", observed: "p533-534 与 n32/n33 一致；SUOTA 参数（50 并发/4-8 小时/充电座 swap）p526 逐格一致；两处硬件实验虚拟课堂不可做（n34）已在卡内声明"}
  V3: {passed: true, expected_benefit: "无线项目整包的施工与验收口径；证据归并 p35/p36/p47/c21/c22/n31-n36"}
  decision: verified

- id: f33
  title: Webdiag 信息架构与三会话体系
  type: structure
  V1: {passed: true, reason: "p559-570 访问/会话/信息树七块完整"}
  V2: {passed: true, check_mode: walkthrough, input: "远程看系统状态/抓包/解锁账户从哪进", expected: "Webdiag 三会话分工（installer/operator/manufacturer）+ 七块信息树", observed: "c23 五连查与 p572-573 一致；Services 块功能清单（Hot desking/用户账户/Cloud Connect/Rainbow status）与 p564 一致"}
  V3: {passed: true, expected_benefit: "售后进阶排障的总入口；证据归并 c23/g47"}
  decision: verified

- id: f34
  title: Noteworthy 地址体系与修改流程
  type: structure
  V1: {passed: true, reason: "p574-581 四类内存区/流程/风险完整"}
  V2: {passed: true, check_mode: walkthrough, input: "书里给的铃音基址能直接抄吗", expected: "不能——基址随软件版本变化，须按 TC1398+附录重算", observed: "p581/n39 与 c24 两例（Auto_Reset 五字节/铃音 <4 秒）一致；写错致系统恶化（p575）与 cold reset 回默认（n38）齐备"}
  V3: {passed: true, expected_benefit: "系统级调参的安全姿势；证据归并 p48/c24/n38/n39/g21"}
  decision: verified

- id: f35
  title: LoLa 系统加载与迁移三流程
  type: flow
  V1: {passed: true, reason: "p582-591 三类流程与数据边界完整"}
  V2: {passed: true, check_mode: walkthrough, input: "换 CPU 迁移客户数据怎么不丢", expected: "OMC 先存话机配置与语音提示；LoLa 管软件/license/话机数据", observed: "p49 分工规则与 p583/p589 一致；LoLa 模式进入法（OCE 电源键/PowerCPU Dip switch）p584 一致"}
  V3: {passed: true, expected_benefit: "灾备/硬件更换的兜底能力；证据归并 p49/p50/n48/n65/g46"}
  decision: verified

- id: f36
  title: Rainbow 业务目录自助同步链路（EC Selfcare）
  type: flow
  V1: {passed: true, reason: "p307-310 链路与技术约束完整"}
  V2: {passed: true, check_mode: walkthrough, input: "同步会不会冲掉手工维护的集体目录", expected: "会——每次同步先擦空再写入", observed: "p309-310/n49 逐格一致；16 字符截断/非 Unicode 忽略/短号随机分配三约束齐备；Max entries 留白已转 nr-08"}
  V3: {passed: true, expected_benefit: "EC 自助、零成本的 Dial by Name 落地路径；证据归并 p46/n49"}
  decision: verified
```

## 断言级裁决记录

1. **"带宽最少 5 通话"三处一致**：p48（公网网关）、p215（私网网关）、p05 归并——同一规则适用于公网与私网 SIP 网关，不设带宽表现为外呼不通。判定成立，作为放行闸门规则入册。
2. **ARS 溢出两条实现路径**：p200-203 与 f14 数值表互证——列表内子线（同列表下一索引）与流量分担矩阵强制（传真行 400=-、401=+、402=-）两种挂法并存，共享子线索引 3 的写法逐格核对无误。
3. **VMU 锁定翻倍公式**：p328 与 p384 两处一致（10→20→…→1440 分钟封顶，VMUMaxTry 可配）；本地 LAN 访问不受锁（p329）。
4. **MLAA 生效条件**：p431（端口）与 p441（消息）两处一致——ACD 引擎复位或 10 分钟无复位后生效；"改了没反应"类排障先查此条。
5. **无 rejected 断言**：DECT 容量（80/60/200、11/6 并发）、SCR 规格（10000/10/64/8）、Hot Desking（200/200、前 2 免费）、酒店（300 话机/4 会话）等关键数字均与原文逐格一致；书中矛盾类条目（Internal ARS 时段、DHCP 池、链路类别取值、门户域名）全部转 needs-review.md 如实记录，未做取舍性"修正"。
