# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f46（主验证对象）；principle p01-p32 / case c01-c25 / counter-example n01-n47 作为各单元的证据素材归并；glossary g01-g46 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 472 页全文通读 + 提取器页码证据交叉核对（关键数字已回源文逐格抽查）

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 44 | f01, f03-f45 区间内全部除 f02/f04 外（详见下表） |
| reference | 2 | f02（RLAB 平台结构）、f04（ITSP1 模拟器）——教学专用基础设施，仅作 Boundary 背景 |
| needs_review | 0（单元级） | 断言级 6 项转 needs-review.md（版本双口径、话务员 DDI 两值、Circular/Cyclic 并存、法文残留、笔误、方向性参考值） |
| rejected | 0 | 无编造断言；DSP 通道表、WebRTC 容量表、复位保留项、信箱容量等关键数字均回源文逐格核对一致 |

verified 明细：f01, f03, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39, f40, f41, f42, f43, f44, f45, f46

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——实验环境 → 产品硬件 → 开通主干 → 业务深化 → 运维安全 → Rainbow 增量
  type: framework
  V1: {passed: true, reason: "p1 目录与 p3-427 章节推进完整可回溯"}
  V2: {passed: true, check_mode: walkthrough, input: "新项目按什么顺序交付一台 OXO", expected: "给出可执行阶段顺序", observed: "八段主线与 p51 两种部署方案、p43 数据采集前置互证，顺序无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线；p427 后培训收尾与附注已剥离出主线"}
  decision: verified

- id: f02
  title: RLAB 实验平台结构——POD 池 + 公共资源区 + POD 网络规划
  type: structure
  V1: {passed: true, reason: "p5-13 拓扑与参数完整（实验口径）"}
  V2: {passed: true, check_mode: walkthrough, input: "实验网段怎么理解", expected: "POD 内 192.168.1.x、公共区 10.20.30.x", observed: "p12-13 参数表支持；仅培训基础设施"}
  V3: {passed: false, expected_benefit: "对生产交付无直接增益——BOOK_OVERVIEW 明示 RLAB 细节不 skill 化，仅作 Boundary 背景"}
  decision: reference

- id: f03
  title: IPDSP 安装前置顺序——先改 IP 再装软话机（时间同步）
  type: flow
  V1: {passed: true, reason: "p14 四步顺序与报错机理原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "IPDSP 报 lanpbx 加载错误怎么办", expected: "先查 PC 与 OXO 时间同步", observed: "p14 原文机理链（HTTPS 证书时间校验）直接回答"}
  V3: {passed: true, expected_benefit: "软话机部署与证书类故障的排障入口；证据归并 n01"}
  decision: verified

- id: f04
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则
  type: diagram
  V1: {passed: true, reason: "p17-21 拓扑与号码规则完整（实验口径）"}
  V2: {passed: true, check_mode: walkthrough, input: "实验里打外线号码怎么编", expected: "PN=POD 号规则可查", observed: "p21 号码表支持；仅教学约定"}
  V3: {passed: false, expected_benefit: "生产 SIP 选型在书外（TC1284），模拟器口径不进生产——仅作实验章节 Boundary 背景"}
  decision: reference

- id: f05
  title: OXO Connect 产品家族与硬件平台——四平台两 CPU 线
  type: structure
  V1: {passed: true, reason: "p24-34 定位与四平台逐一定义"}
  V2: {passed: true, check_mode: walkthrough, input: "客户 200 用户选哪个硬件", expected: "四平台按规模与话音形态对号", observed: "p24 'up to 300 users' + p26/34 平台表支撑结构判断；报价在书外"}
  V3: {passed: true, expected_benefit: "售前沟通与硬件认知底座；证据归并 g01/g30-g32"}
  decision: verified

- id: f06
  title: IPBox（OCE）接口与安装形态——ETH0/ETH1 分工
  type: diagram
  V1: {passed: true, reason: "p30-32 接口与安装形态原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "ETH1 能不能当普通网口接 LAN", expected: "不能——专用现场管理口", observed: "p31 'For Instant Management access on site' + p57 安全四条一致"}
  V3: {passed: true, expected_benefit: "现场布线与零接触部署前提（PoE）的依据；证据归并 p06/g04"}
  decision: verified

- id: f07
  title: PowerCPU EE 硬件结构——CPU 规格、子板与 DSP 通道扩展
  type: structure
  V1: {passed: true, reason: "p35-39 规格与子板清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "SIP 并发不够怎么扩", expected: "按子板档位扩 DSP 通道", observed: "p37 通道表 16/48/60/76 逐格核对一致；OMC 两种配比口径在 p37 注"}
  V3: {passed: true, expected_benefit: "话音容量设计与扩容选型依据；证据归并 p04/g31/g32"}
  decision: verified

- id: f08
  title: 多机柜互连结构——HSL 链路与 5 米限制
  type: diagram
  V1: {passed: true, reason: "p42 三条约束原文齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "扩展柜放 10 米外行不行", expected: "不行——主柜到扩展柜最大 5 米", observed: "p42 原文直接回答；HSL 非以太网级联"}
  V3: {passed: true, expected_benefit: "TDM 扩容的物理边界，机房规划前置项；证据归并 g33"}
  decision: verified

- id: f09
  title: OCE 启动与服务口（ETH1）设计——FTR 入口与安全边界
  type: structure
  V1: {passed: true, reason: "p56-58 参数表、安全四条、LED 表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "ETH1 的 IP 与 DHCP 池是多少", expected: "192.168.94.246/24、池 .247-.254、租期 2h", observed: "p57 逐格核对一致；myipbox.ale 直连口径同页"}
  V3: {passed: true, expected_benefit: "FTR 现场交付三件套（口/线/浏览器）之一；证据归并 p06/n02"}
  decision: verified

- id: f10
  title: 两种部署方案——Cloud Connect 六步 vs Standard 四步
  type: flow
  V1: {passed: true, reason: "p51-55 两路线步骤完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户现场没外网怎么交付", expected: "走 Standard（OMC+两把许可）", observed: "p55 四步与 .msl/.csl 口径支持；与 f14 许可机制互证"}
  V3: {passed: true, expected_benefit: "交付路线选型的第一岔口；证据归并 g03/g29"}
  decision: verified

- id: f11
  title: FTR 首次注册流程（Web 页面版）
  type: flow
  V1: {passed: true, reason: "p59-62 How-To 完整（含虚课限制）"}
  V2: {passed: true, check_mode: walkthrough, input: "FTR 要填哪些值", expected: "IP 五项+三参考值", observed: "p61 参数与 p29 采集表逐格一致；虚课替代路径 p60/n02 明示"}
  V3: {passed: true, expected_benefit: "OCE 交付第一步的标准动作；证据归并 c01/p29/n02"}
  decision: verified

- id: f12
  title: OMC 模式体系——六类入口与连接方式
  type: structure
  V1: {passed: true, reason: "p63-67 六入口与连接方式原文齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "连不上 OXO 先查什么", expected: "LAN/WAN 同网段、先查 PC IP", observed: "p67 连接方式与故障提示支持；默认 IP/密码口径同页"}
  V3: {passed: true, expected_benefit: "OMC 全功能面的入口地图；证据归并 g05/p07"}
  decision: verified

- id: f13
  title: OMC 服务器认证机制——证书校验与告警链
  type: structure
  V1: {passed: true, reason: "p68-69 四要素原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "每次连接都弹告警怎么一次解决", expected: "证书装进受信任根", observed: "p68-69 机制与 c02 步骤 8 一致；告警上报链（8770/邮件）同页"}
  V3: {passed: true, expected_benefit: "首连高频卡点的机理与解法；证据归并 c02"}
  decision: verified

- id: f14
  title: OMC 软件钥匙体系——.msl 与 .csl 双钥匙
  type: structure
  V1: {passed: true, reason: "p71 导入路径与钥匙绑定关系原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "许可怎么装进系统", expected: "主钥匙 .msl + CTI 钥匙 .csl 分别导入后 Apply", observed: "p71 逐句核对一致；与主 CPU 序列号绑定（换 CPU 重发，n22）互证"}
  V3: {passed: true, expected_benefit: "Standard 路线的许可落地动作；证据归并 g29/n22"}
  decision: verified

- id: f15
  title: 默认配置行为集——话务台/动态路由/信箱/传真/Hotel 预置
  type: structure
  V1: {passed: true, reason: "p87-93 六页讲义逐项完整"}
  V2: {passed: true, check_mode: walkthrough, input: "刚开机不配置能打通电话吗", expected: "能——新话机即插即用、默认话务台/转接已生效", observed: "p89-93 行为集逐项核对（12s/24s、组 8、传真位、默认 IP）与 p07/p08 互证"}
  V3: {passed: true, expected_benefit: "验收基线与默认行为判定的依据；证据归并 p07/p08/p32"}
  decision: verified

- id: f16
  title: 四层拨号计划框架——公共/专用/内部/会话中
  type: structure
  V1: {passed: true, reason: "p123-128 四层与两种默认计划风格完整"}
  V2: {passed: true, check_mode: walkthrough, input: "内外号码怎么对上的", expected: "Base 映射（41100 base 100 ↔ 分机 100）", observed: "p128 三组 Base 示例逐格核对；修改入口 p125/127 明确"}
  V3: {passed: true, expected_benefit: "一切呼叫寻址的地基；证据归并 g10/p11"}
  decision: verified

- id: f17
  title: 固定 Base 的功能前缀表——代接与前转两族
  type: structure
  V1: {passed: true, reason: "p129-130 两族前缀与安装号规则原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "组代接的前缀 Base 是多少", expected: "固定语义不可改（组代接=1）", observed: "p129 表逐项核对；安装号去首位录入 p130"}
  V3: {passed: true, expected_benefit: "功能键/短码配置的固定语义表；证据归并 c08/f20"}
  decision: verified

- id: f18
  title: 编号计划冲突处理范式——先删旧段再建新段
  type: flow
  V1: {passed: true, reason: "p131-135 How-To 五步与冲突段列举完整"}
  V2: {passed: true, check_mode: walkthrough, input: "建新前缀段报冲突怎么办", expected: "查既有段→删→再建", observed: "p132/135 三处冲突示例（200-299/400-434/6 开头）与 c06 步骤一致；Base 0-2199 同页"}
  V3: {passed: true, expected_benefit: "编号调整的标准范式；证据归并 c06/p11"}
  decision: verified

- id: f19
  title: Hunt group 三种分发模式与保留组
  type: structure
  V1: {passed: true, reason: "p137/p143-145 模式定义与实验完整"}
  V2: {passed: true, check_mode: walkthrough, input: "组 500 能拿来用吗", expected: "不能——被语音信箱服务器占用", observed: "p143 Warning 原文；默认范围 500-525（p46）与实验从 501 起（p143）一致"}
  V3: {passed: true, expected_benefit: "组业务主力与规划红线；证据归并 c07/n07"}
  decision: verified

- id: f20
  title: Pick-up group 与 Group pickup 可编程键
  type: structure
  V1: {passed: true, reason: "p138/p146-150 定义与两段配置完整"}
  V2: {passed: true, check_mode: walkthrough, input: "代接键建好不生效", expected: "查键作用域是否选 Group", observed: "p150 键类型/作用域口径与 c08 步骤 4 一致；代接前缀 base 固定（f17）互证"}
  V3: {passed: true, expected_benefit: "团队互助基础业务；证据归并 c08/n46"}
  decision: verified

- id: f21
  title: Broadcast group 发送/接收权限与 Grb 配对
  type: structure
  V1: {passed: true, reason: "p139/p151-153 权限与配对口径完整"}
  V2: {passed: true, check_mode: walkthrough, input: "低端话机收不到广播", expected: "接收方必须有扬声器", observed: "p152 Warning 原文；PairedGrb 2 组 64 人 p139 核对一致"}
  V3: {passed: true, expected_benefit: "广播业务的硬件前置核查项；证据归并 c09/n08"}
  decision: verified

- id: f22
  title: Manager/Secretary 组与三个监督键
  type: structure
  V1: {passed: true, reason: "p140/p154-156 键体系与前置条件完整"}
  V2: {passed: true, check_mode: walkthrough, input: "普通话机能建经理秘书组吗", expected: "不能——双方必须 multiline", observed: "p155 原文 + 虚课限制同页（n09）"}
  V3: {passed: true, expected_benefit: "经理-秘书场景的方案边界；证据归并 c10/g25/n09"}
  decision: verified

- id: f23
  title: 三类可编程键体系与默认键 profile 对照
  type: structure
  V1: {passed: true, reason: "p160-163 键三类与 profile 表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "话机默认有几个资源键", expected: "按模式查表（Single line 3 虚拟键等）", observed: "p163 三档 profile 逐格核对与 p09 一致"}
  V3: {passed: true, expected_benefit: "用户功能配置与排障的键体系底座；证据归并 p09/g45"}
  decision: verified

- id: f24
  title: 动态路由两级两计时框架与级联
  type: flow
  V1: {passed: true, reason: "p164-166 框架与上限原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "用户设了前转不生效查哪里", expected: "先查 apply diversion 总开关", observed: "p165 原文 + n10 一致；计时上限 3276s、级联 5 级 p165-166 逐格核对"}
  V3: {passed: true, expected_benefit: "久叫不应与转接失效排障的主框架；证据归并 p08/n10"}
  decision: verified

- id: f25
  title: 语音信箱体系——容量报价、访问模式与三种信箱
  type: structure
  V1: {passed: true, reason: "p183-189 七页讲义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "信箱容量/端口不够怎么办", expected: "按选配扩（端口至 8、存储至 200h）", observed: "p183 基线与选配逐格核对与 p10 一致；General 信箱密码=话务员密码 p189"}
  V3: {passed: true, expected_benefit: "信箱业务报价与交付口径；证据归并 p10/c12/g18"}
  decision: verified

- id: f26
  title: 公共 SIP 拓扑与 OCE 双口接入
  type: diagram
  V1: {passed: true, reason: "p198/p200 组件链与双口接入完整"}
  V2: {passed: true, check_mode: walkthrough, input: "运营商 SIP 接 OCE 哪个口", expected: "ETH0 或专用 ETH1（双子网更安全）", observed: "p200 原文；与 p57 ETH1 口径互证"}
  V3: {passed: true, expected_benefit: "SIP 中继的网络架构认知；证据归并 g41/p06"}
  decision: verified

- id: f27
  title: SIP 网关配置菜单地图——OMC/External Lines/SIP 七页签
  type: structure
  V1: {passed: true, reason: "p203-214 周边配置与九页签地图完整"}
  V2: {passed: true, check_mode: walkthrough, input: "SIP 网关要配哪些页签、什么顺序", expected: "周边四项→网关九页签（DNS 先于 Domain Proxy）", observed: "p232-237 各页签与 c13 步骤 6-13 一致；顺序依赖 n13 同页"}
  V3: {passed: true, expected_benefit: "全书配置项最多章节的施工地图；证据归并 c13/n13/n42"}
  decision: verified

- id: f28
  title: SIP Trunk Profile 导入导出与 Easy Connect 流程
  type: flow
  V1: {passed: true, reason: "p216-222 Profile 机制与 ARS 补充完整"}
  V2: {passed: true, check_mode: walkthrough, input: "新运营商能不能免手工配置", expected: "过 TSS 认证的运营商可 Profile 导入或 Easy Connect", observed: "p216/218 前提（Cloud Connected）与机制一致；ARS 四行模板 p220-221 与 n12 互证"}
  V3: {passed: true, expected_benefit: "SIP 交付提速路径与紧急号码合规入口；证据归并 g16/n12"}
  decision: verified

- id: f29
  title: Messages 1-20 与 Music on hold 体系
  type: structure
  V1: {passed: true, reason: "p243-251 数值与格式约束完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户要 15 条问候语能做吗", expected: "默认 4 条、许可至 20；先查软件钥匙", observed: "p244/p250 口径与 n16 一致；.wav 格式 p247 逐格核对"}
  V3: {passed: true, expected_benefit: "客户体验项的可行性与格式硬约束；证据归并 p12/c14/n16/n41"}
  decision: verified

- id: f30
  title: 呼入分发体系——话务台组、时段表与 Normal/Restricted 双计划
  type: structure
  V1: {passed: true, reason: "p253-261 九页讲义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "非工作时间来电怎么自动分流", expected: "两套 DDI 计划+时段表切组", observed: "p254/258 机制与 c15 步骤一致；组恒并行 p264、预公告数值 p260 逐格核对"}
  V3: {passed: true, expected_benefit: "前台/非工作时间刚需的完整方案；证据归并 c15/p13/g09/g11"}
  decision: verified

- id: f31
  title: 出局三层限制模型——Traffic sharing → Barring → 闭锁表
  type: diagram
  V1: {passed: true, reason: "p271-280 三层模型与默认值完整"}
  V2: {passed: true, check_mode: walkthrough, input: "某用户打不了外线查哪里", expected: "按三层逐层判定（占组→拨号→路由）", observed: "p271-275 模型逐格核对与 p14/p28 一致；默认 LC=12 p286 同源"}
  V3: {passed: true, expected_benefit: "出局权限设计与排障的三问框架；证据归并 p14/p15/p28/p30/c16"}
  decision: verified

- id: f32
  title: 数据备份体系——自动/手动/SD 卡/迁移四线
  type: structure
  V1: {passed: true, reason: "p294-306 四线机制完整"}
  V2: {passed: true, check_mode: walkthrough, input: "SD 卡备份有什么坑", expected: "同主版本可恢复、卡 2-32GB、EXT2、仅 OMC 格式化", observed: "p301/304 逐格核对与 p16/n21 一致；DBAdapter p306 同源"}
  V3: {passed: true, expected_benefit: "运维底线的方案空间与约束；证据归并 p16/c17/n21/n22/g20"}
  decision: verified

- id: f33
  title: 软件下载与双版本机制——下载/Swap/回退
  type: flow
  V1: {passed: true, reason: "p315-320 机制与三件套清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "升级失败怎么回退", expected: "switchover 切回 active 前版本", observed: "p316/320 双版本与 Swap 口径一致；与 n21（SD 卡不可跨主版本回滚）互证"}
  V3: {passed: true, expected_benefit: "版本治理的标准动作；证据归并 n21"}
  decision: verified

- id: f34
  title: 三种复位的选择矩阵与数据分类
  type: structure
  V1: {passed: true, reason: "p321-324 三档定义与数据六分类完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Cold 复位是不是全清", expected: "不是——不勾子选项保留四类", observed: "p323 保留清单逐格核对与 p17/n23 一致；Factory≈Lola 态 p322"}
  V3: {passed: true, expected_benefit: "故障处理与设备回收的正确选择；证据归并 p17/n23"}
  decision: verified

- id: f35
  title: Rainbow 平台全景与 UCaaS 架构三要素
  type: diagram
  V1: {passed: true, reason: "p330-334 定位与架构图完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Rainbow 和 OXO 什么关系", expected: "混合云：PBX 呼控+Rainbow 协作", observed: "p331-334 与 RAINXTE001EN 口径一致（姊妹书互证）"}
  V3: {passed: true, expected_benefit: "混合云方案沟通底座（本书从简，深入内容指向姊妹技能）"}
  decision: verified

- id: f36
  title: Rainbow 管理员双档案与公司管理面
  type: structure
  V1: {passed: true, reason: "p337-343 双档案与目录/频道完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户管理员为什么激活不了网关", expected: "Reseller/BP 专属", observed: "p338 权责清单 + n33 一致"}
  V3: {passed: true, expected_benefit: "权责切分依据（从简收录，细节在姊妹技能）"}
  decision: verified

- id: f37
  title: WebRTC 网关四拓扑结构与部署分工
  type: structure
  V1: {passed: true, reason: "p362-368 四拓扑与分工清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "自动配置管哪些项", expected: "自动五项/安装员三项", observed: "p366 清单逐格核对与 p22 一致；版本下限见 needs-review nr-01"}
  V3: {passed: true, expected_benefit: "网关决策部署的分工与边界；证据归并 p22/n28"}
  decision: verified

- id: f38
  title: OCE Front End（OCE-FE）专用形态——FTR 自动化与双机约束
  type: structure
  V1: {passed: true, reason: "p372-382 版本/PBXID/端口/warm reset 齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "FE 改完配置不生效", expected: "先 warm reset，再查双机 PBXID 一致", observed: "p377/p379 原文与 p21/n30/n31 逐格核对；容量组合"不支持"格 p374 同源"}
  V3: {passed: true, expected_benefit: "FE 拓扑施工链；细节指向 cookbook（诚实外置）"}
  decision: verified

- id: f39
  title: 外部 WebRTC 网关部署流程——VMware 与 NUC 双路
  type: flow
  V1: {passed: true, reason: "p383-390 两条线与下载源完整"}
  V2: {passed: true, check_mode: walkthrough, input: "NUC 和 ESXi 怎么选", expected: "同 50 通话上限，按现场硬件", observed: "p389-390 同一软件包含 OVF+ISO；TURN 仅一句带过（书外 cookbook）"}
  V3: {passed: true, expected_benefit: "50 通话扩容路径入口；TURN/白名单书外（n43）"}
  decision: verified

- id: f40
  title: WebRTC 网关容量规划表——用户数、通道数与拓扑上限
  type: structure
  V1: {passed: true, reason: "p391-392 表逐格核对：外部 5/7/11/15/20/27/36/50；集成 5/7/11/15/20 后 NA"}
  V2: {passed: true, check_mode: walkthrough, input: "80 个 Rainbow 话音用户怎么配", expected: "外部拓扑、通道 27-36、≤50 上限", observed: "p392 表内插可答；(*) 行为方向性参考（原注），见 needs-review nr-06"}
  V3: {passed: true, expected_benefit: "售前报价与交付容量查表依据；证据归并 p20/n32"}
  decision: verified

- id: f41
  title: Rainbow 话务台界面结构与监督组规格
  type: structure
  V1: {passed: true, reason: "p407-414 界面与规格齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "40 人部门建一个监督组建得下吗", expected: "不行——每组 ≤30 人", observed: "p412 规格（5 组/30 人）逐格核对与 p24 一致；队列 OXE 10/OXO 8 p409"}
  V3: {passed: true, expected_benefit: "话务监督方案容量设计（从简收录）；证据归并 p24/n34/n35"}
  decision: verified

- id: f42
  title: 互助监督组机制——动态进出与边界
  type: structure
  V1: {passed: true, reason: "p415-418 机制三要素与边界完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Rainbow 纯软话机能被互助代接吗", expected: "不能——代接仅限 PBX 呼叫", observed: "p416 原文 + n34 一致；锁定成员/4 路监督 p417"}
  V3: {passed: true, expected_benefit: "互助场景需求边界管理（从简收录）"}
  decision: verified

- id: f43
  title: PowerCPU EE 启动八步与停机指示
  type: flow
  V1: {passed: true, reason: "p436-438 八步与 LED 语义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "开机卡在第几步怎么看", expected: "面板步骤号对应机柜/话机阶段", observed: "p437 八步顺序（HSL2→HSL1→主柜→VMU）逐格核对；停机 LED p438"}
  V3: {passed: true, expected_benefit: "硬件启动排障的观测点；证据归并 g33"}
  decision: verified

- id: f44
  title: 安装向导体系——话机版与 OMC 版阶段清单
  type: structure
  V1: {passed: true, reason: "p439-444 两类向导与阶段清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "系统想进 Hotel 模式怎么办", expected: "初始安装向导唯一入口（须初始态）", observed: "p440/447 原文与 p32/n37 一致；OMC 版 17 阶段 p443 逐项核对"}
  V3: {passed: true, expected_benefit: "冷复位后重建配置的标准路径；证据归并 c24/p29/p32/n37"}
  decision: verified

- id: f45
  title: 8328 基站 Web Admin 配置地图
  type: structure
  V1: {passed: true, reason: "p453-459 部署地图与参数完整"}
  V2: {passed: true, check_mode: walkthrough, input: "8328 拿不到 IP 怎么办", expected: "出厂动态 IP——必须有 DHCP；找 IP 用 8214 拨 *47*", observed: "p455-456 原文 + n38 一致；Servers 区参数 p458 逐格核对"}
  V3: {passed: true, expected_benefit: "SIP-DECT 路线的施工地图；证据归并 c25/p26/n38/n39"}
  decision: verified

- id: f46
  title: 模拟-SIP 网关（FXS）接入模型
  type: structure
  V1: {passed: true, reason: "p104 三款型号与许可口径完整"}
  V2: {passed: true, check_mode: walkthrough, input: "模拟传真怎么进 OCE", expected: "FXS 网关每口 1 UTL+1 Open SIP", observed: "p104 逐格核对与 p23/g37 一致；OMC 显示 Open SIP Terminal 同页"}
  V3: {passed: true, expected_benefit: "模拟设备存量利旧路径；证据归并 p23/g37"}
  decision: verified
```

## 断言级裁决记录

1. **principle 提取器“话务员呼出经 9、采集表完整”**：成立。p49 呼出样例与 p44-48 六块采集项逐格核对一致（p31 佐证）。
2. **counter-example 提取器“p366 与 p395 版本表述矛盾”**：成立并如实记录——"available from system version R4.0.020.002" vs "applies to versions greater than R4.0.020.002"。实践口径取 ≥R4.0.020.002、以更高版本执行；详见 needs-review nr-01。
3. **counter-example 提取器“ hunt group 讲义 Circular / 实验 Cyclic 并存”**：成立。p137 讲义表用 Circular，p145 实验用 Cyclic，同义异名（原文如此）；详见 needs-review nr-03。
4. **无 rejected 断言**：DSP 通道表（16/48/60/76）、WebRTC 容量表（5→5/5 … 150→50/NA）、复位保留四类、信箱容量（1h/120s/2 口/30 天/15 秒）、消息（4-20 条/320s）、闭锁（6 表/LC=12/00 默认禁）、监督组（5 组/30 人/4 路）、话务台队列（OXE 10/OXO 8）均与原文逐格一致。
