# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f31（主验证对象）；principle p01-p35 / case c01-c19 / counter-example n01-n50 作为各单元的证据素材归并；glossary g01-g58 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 351 页全文通读 + 提取器页码证据交叉核对（关键数值已回 source_fulltext.txt 逐格复核）

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 29 | f01, f04-f31（除 f02/f03 外全部） |
| reference | 2 | f02（RLAB POD 拓扑）、f03（ITSP1 SIP 模拟器）——教学专用基础设施，仅作 Boundary 背景 |
| needs_review | 0（单元级） | 断言级 4 项转 needs-review.md（GRUB 大小写、URL 笔误、抓包残留旧版本号、许可版本样例不一致） |
| rejected | 0 | 无编造断言；p52 规格表、p253/p274 许可项、p317 报告偏移等关键数字均与原文逐格一致 |

verified 明细：f01, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31

## 验证记录

```yaml
- id: f01
  title: 全书推进逻辑——概念底座 → 交付闭环 → 树设计核心 → HA 加强 → 运维与集成
  type: framework
  V1: {passed: true, reason: "p4/p19/p41/p63/p143/p239/p272/p319 分区页齐全，十段结构逐段有锚点"}
  V2: {passed: true, check_mode: walkthrough, input: "交付按什么顺序推进", expected: "给出可执行阶段顺序", observed: "讲义定框架、实验给闭环的双线在十个分区一致重现，顺序无矛盾"}
  V3: {passed: true, expected_benefit: "培训学习与项目排期的顺序基线"}
  decision: verified

- id: f02
  title: RLAB POD 结构——五虚机 + 公共资源区拓扑
  type: framework
  V1: {passed: true, reason: "p5-13 拓扑与虚机清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "实验环境长什么样", expected: "五虚机+公共区结构", observed: "p7 拓扑图与 p9 虚机口令表一致；纯教学基础设施"}
  V3: {passed: true, expected_benefit: "实验口径背景（仅 Boundary），不进生产交付"}
  decision: reference

- id: f03
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则
  type: framework
  V1: {passed: true, reason: "p15-17 网关/账号/号码规则完整"}
  V2: {passed: true, check_mode: walkthrough, input: "外呼回环号码怎么构成", expected: "PN=POD 号的号码规则", observed: "p17 外呼循环示例与规则一致；生产不可套用"}
  V3: {passed: true, expected_benefit: "实验口径背景（仅 Boundary）"}
  decision: reference

- id: f04
  title: VAA 产品定位与四类功能清单
  type: framework
  V1: {passed: true, reason: "p20-21 定位句与四栏功能清单完整，p145 重复"}
  V2: {passed: true, check_mode: walkthrough, input: "VAA 能做什么、哪些要另买许可", expected: "功能全景 + Option 栏需 IVR 许可", observed: "p21 四栏与 p27 IVR options (Additional licenses) 互证"}
  V3: {passed: true, expected_benefit: "售前边界沟通与功能清点依据；证据归并 p14/n03"}
  decision: verified

- id: f05
  title: VAA 软件组件族与六服务视图
  type: framework
  V1: {passed: true, reason: "p54 组件页单处完整，p277 服务表同口径"}
  V2: {passed: true, check_mode: walkthrough, input: "日志里 aa-webapp/nginx 是什么", expected: "组件职责可对号", observed: "p54 与 p277 两处职责描述一致；日志目录 p281 同名"}
  V3: {passed: true, expected_benefit: "服务与日志命名基础，运维巡检地图；证据归并 p29/p34"}
  decision: verified

- id: f06
  title: 高层软件架构与四步典型呼叫流
  type: framework
  V1: {passed: true, reason: "p42-43 架构五要素与四步呼叫流完整"}
  V2: {passed: true, check_mode: walkthrough, input: "来话怎么走到 VAA 再落地", expected: "OXE 经 SIP 中继送 VAA 执行脚本后转接落地", observed: "p43 四步流直接回答；ABC-F 中继与 CMIP 电话簿同步在 p42 同页支撑"}
  V3: {passed: true, expected_benefit: "呼控面/媒体面排障分流的概念依据；证据归并 p09/p41"}
  decision: verified

- id: f07
  title: Master/Slave 高可用机制图（OXE ARS 切换 + 数据库复制）
  type: framework
  V1: {passed: true, reason: "p44 机制图单处完整，p240 原样重复"}
  V2: {passed: true, check_mode: walkthrough, input: "主 VAA 宕机呼叫怎么切", expected: "OXE ARS 切到 Slave 中继，库已复制", observed: "p44 原文两要素齐全；切换丢话/只读行为由 p23 规则集补全"}
  V3: {passed: true, expected_benefit: "HA 设计蓝图，OXE 侧实验（c17）的依据；证据归并 p23/p24/n04/n05"}
  decision: verified

- id: f08
  title: OXE 冗余三用例矩阵——呼叫服务器丢失 / 主 VAA 丢失 / WAN 断
  type: framework
  V1: {passed: true, reason: "p45-48 三用例逐一定义，'Existing ongoing calls are lost' 三处重复"}
  V2: {passed: true, check_mode: walkthrough, input: "OXE 呼叫服务器切换时 VAA 侧发生什么", expected: "中继在新主上重建、进行中呼叫丢失", observed: "p45 原文直接回答；三用例行为与 n04/n05/n06 一致"}
  V3: {passed: true, expected_benefit: "客户预期管理与 SLA 口径的硬依据"}
  decision: verified

- id: f09
  title: PCS 支撑架构——中心 VAA + 外围 PCS VAA
  type: framework
  V1: {passed: true, reason: "p49 架构图 + p300-303 同步命令两处互证"}
  V2: {passed: true, check_mode: walkthrough, input: "远端站点断网了怎么办", expected: "PCS 激活接管本地呼叫，恢复后应急配置丢失", observed: "p49 两句原文直接回答；n09 双处同义重复"}
  V3: {passed: true, expected_benefit: "多分支场景的知识底座；证据归并 p33/n09"}
  decision: verified

- id: f10
  title: OXE multi-company 集成与 N+1 冗余结构
  type: framework
  V1: {passed: true, reason: "p50-51 两页概念完整"}
  V2: {passed: true, check_mode: walkthrough, input: "能给某个公司预留 IVR 端口吗", expected: "不能——媒体服务器共享", observed: "p50 原文明确；N+1 reference 冻结配置由 p51/n06 支撑"}
  V3: {passed: true, expected_benefit: "多公司与扩容方案的能力边界；证据归并 n06/n07"}
  decision: verified

- id: f11
  title: 服务器规格三档表与端口上限
  type: framework
  V1: {passed: true, reason: "p52 表格逐格核对一致（8/50/120 端口三档）"}
  V2: {passed: true, check_mode: walkthrough, input: "50 端口配什么服务器", expected: "四核 2.4GHz/16GB/1Gb/s/80GB", observed: "p52 表内可查；两处 'Given as an example' 免责与 n03 一致"}
  V3: {passed: true, expected_benefit: "选型初筛查表依据（引用必须带示例口径）；证据归并 p01/n03"}
  decision: verified

- id: f12
  title: 虚拟化环境兼容表
  type: framework
  V1: {passed: true, reason: "p53 三种 Hypervisor 前提完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Proxmox 能不能跑 VAA", expected: "4.6.1 起支持 Proxmox 8.2、网卡 VMXNet3", observed: "p53 注(1)直接回答；与 p02 清单一致"}
  V3: {passed: true, expected_benefit: "部署前提核查清单；证据归并 p02"}
  decision: verified

- id: f13
  title: HTTPS 切换与证书体系（版本前提 + 证书格式 + 三种来源）
  type: framework
  V1: {passed: true, reason: "p56-62 四块证据连贯（版本/格式/命令/XCA 生成）"}
  V2: {passed: true, check_mode: walkthrough, input: "没给证书安装会怎样、怎么换真证书", expected: "自动自签；vaa conf https 更新", observed: "p57 自签规则 + p58 命令直接回答；SAN/CN 要求 p60 支撑"}
  V3: {passed: true, expected_benefit: "安全基线第一步的操作与边界；证据归并 c04/n11"}
  decision: verified

- id: f14
  title: WebAdmin 管理面分区（登录/About/公司/角色/编辑器/路由/日历/过滤/目录/提示音/公司设置/管理员菜单）
  type: framework
  V1: {passed: true, reason: "p22-39 逐页分区证据完整"}
  V2: {passed: true, check_mode: walkthrough, input: "某管理功能在哪个菜单", expected: "分区地图可导航", observed: "p22-39 各页与 p127-132 实验入口一致；默认 admin/admin 首连必改三处互证（p04/n12）"}
  V3: {passed: true, expected_benefit: "管理面导航总图；证据归并 p04/n12/n13"}
  decision: verified

- id: f15
  title: 树编辑器原生节点全集（12 种）与画布命令
  type: framework
  V1: {passed: true, reason: "p27 命令清单 + p144-162 节点讲义逐页"}
  V2: {passed: true, check_mode: walkthrough, input: "某流程能不能用原生节点拼出来", expected: "12 种节点能力边界内判定", observed: "p144-162 每节点参数页支撑；Menu 12 选项（p144）等硬规格一致"}
  V3: {passed: true, expected_benefit: "树设计积木全集；证据归并 p15/p16/n21/n37/n38"}
  decision: verified

- id: f16
  title: IVR 选项节点全集（9 种，另购许可）
  type: framework
  V1: {passed: true, reason: "p27 + p203-213 清单与各节点页完整"}
  V2: {passed: true, check_mode: walkthrough, input: "对接信息系统需要哪些节点", expected: "九节点清单 + IVR 许可前提", observed: "p203 'Options subject to licenses' 与 p21 Option 栏互证"}
  V3: {passed: true, expected_benefit: "增值集成的方案边界；证据归并 p18-p22/n23-n26"}
  decision: verified

- id: f17
  title: Pod 配置操作流（OXE 底座准备）
  type: framework
  V1: {passed: true, reason: "p63-74 七步操作逐页可循"}
  V2: {passed: true, check_mode: walkthrough, input: "实验前 OXE 底座怎么备", expected: "虚机/用户/DID 翻译/防火墙信任主机", observed: "p64-73 步骤连贯；其中防火墙信任主机（p70）在真实交付同样适用"}
  V3: {passed: true, expected_benefit: "培训底座复现 + 交付前置核查；证据归并 c01/n41/n16"}
  decision: verified

- id: f18
  title: VAA 安装三方式与手工安装/发行包装配流程
  type: framework
  V1: {passed: true, reason: "p76-83 讲义 + p88-104 实验全参数"}
  V2: {passed: true, check_mode: walkthrough, input: "从裸机到能登录 Web 界面怎么走", expected: "改密/配网/传输/install.sh/验收", observed: "p88-104 十八步连贯；4.8.006 全新安装规则三处互证（p78/p80/p89）"}
  V3: {passed: true, expected_benefit: "全书第一关口的施工图；证据归并 p03-p08/c02/n01/n10/n12/n49"}
  decision: verified

- id: f19
  title: OXE 侧 SIP 对接配置链（trunk group → 外部网关 → 信任 IP → 路由 → 全局参数）
  type: framework
  V1: {passed: true, reason: "p85-86 讲义 + p105-113 实验五段链完整"}
  V2: {passed: true, check_mode: walkthrough, input: "OXE 侧要把呼叫送进 VAA 要配哪些", expected: "中继/网关/信任 IP/路由表/前缀计划", observed: "p107-113 步骤连贯；incoming username 契约与 p101/p109 一致"}
  V3: {passed: true, expected_benefit: "双层路由第二层的施工图；证据归并 p10/p11/c03/n42/n47/n48"}
  decision: verified

- id: f20
  title: OXE-VAA 接通性验证与四层排障抓手
  type: framework
  V1: {passed: true, reason: "p114-121 测试树四步与排障命令齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "拨 31400 不通怎么排", expected: "中继状态/网关状态/抓包/VAA 日志四层", observed: "p119-120 trkstat/sipextgw/motortrace + p121 softcmp 日志直接回答"}
  V3: {passed: true, expected_benefit: "接通性排障的标准路径；证据归并 c03/n41/n47"}
  decision: verified

- id: f21
  title: 公司创建与业务时间/日历管理流
  type: framework
  V1: {passed: true, reason: "p24/p30-31 概念 + p133-136 实验完整"}
  V2: {passed: true, check_mode: walkthrough, input: "给客户开租户并配营业时间", expected: "四要素设置 + Schedule 维护", observed: "p134 参数表与 p135 时段/假日设置一致；依赖物先行与 p15 一致"}
  V3: {passed: true, expected_benefit: "多租户配置的上下文前提；证据归并 g04/c06"}
  decision: verified

- id: f22
  title: 提示音与 TTS/ASR 管理流
  type: framework
  V1: {passed: true, reason: "p33-37 概念 + p137-142 实验完整"}
  V2: {passed: true, check_mode: walkthrough, input: "语音资产从哪来、生产用什么引擎", expected: "WAV/录制/TTS 三来源 + Pico 免费不建议生产", observed: "p34/p138/p140-141 原文一致；p141 自注价格可能过时"}
  V3: {passed: true, expected_benefit: "语音资产管线与选型；证据归并 p13/p14/n19/n20"}
  decision: verified

- id: f23
  title: 树设计三级用例递进链（UC1 简单转接 → UC2 日历+过滤 → UC3 多语言菜单）
  type: framework
  V1: {passed: true, reason: "p164-201 三用例逐步实验完整"}
  V2: {passed: true, check_mode: walkthrough, input: "常见 IVR 需求怎么落地", expected: "按复杂度选用例起步", observed: "三用例各有验收测试（p172/p184/p201）；依赖物先行三处重复（p15）"}
  V3: {passed: true, expected_benefit: "核心交付能力的参照实现；证据归并 p15/c08-c10/n21/n22"}
  decision: verified

- id: f24
  title: 变量体系与动态脚本流（Set variable/Condition 闭环）
  type: framework
  V1: {passed: true, reason: "p215-220 讲义与实验完整"}
  V2: {passed: true, check_mode: walkthrough, input: "按主叫属性分流怎么做", expected: "复制上下文变量 + Condition 判断", observed: "p216 三类变量定义与 p218 实验条件一致；上下文变量清单外置管理指南"}
  V3: {passed: true, expected_benefit: "动态脚本地基，SQL/HTTP/收号/TTS 的必需品；证据归并 p18/c11"}
  decision: verified

- id: f25
  title: HA 安装五步流（slave 侧安装 + master 侧 addslave + 双侧验证）
  type: framework
  V1: {passed: true, reason: "p240-246 讲义 + p247-255 实验完整"}
  V2: {passed: true, check_mode: walkthrough, input: "slave 怎么加入", expected: "slave 独立安装 → master addslave → 双侧验证", observed: "p247-255 步骤连贯；addslave 清库警告 p252 原文大写强调（n29）"}
  V3: {passed: true, expected_benefit: "冗余部署施工链；证据归并 p23/p24/c16/n29/n30"}
  decision: verified

- id: f26
  title: OXE 侧 HA 附加配置链（第二中继/网关/识别符/NPD/ARS 双路由/时间路由/测试号）
  type: framework
  V1: {passed: true, reason: "p242 + p256-271 九段链逐页完整"}
  V2: {passed: true, check_mode: walkthrough, input: "主 VAA 宕机怎么自动切到 slave", expected: "第二中继/网关 + ARS 双路由", observed: "p256-270 配置链连贯；切换测试首呼延迟 p271 原文（n31）"}
  V3: {passed: true, expected_benefit: "HA 真正生效的 OXE 半边；证据归并 c17/n05/n31"}
  decision: verified

- id: f27
  title: VAA 命令族与维护操作地图
  type: framework
  V1: {passed: true, reason: "p273-294 + p296-299 命令页与讲义齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "日常运维有哪些抓手", expected: "许可/密码/命令/日志/告警/备份七块", observed: "p277-294 分节完整；stop 与 fullstop 差异（保留 postgresql+nginx）p278 原文"}
  V3: {passed: true, expected_benefit: "运维闭环地图；证据归并 p25-p29/n32-n34/n15"}
  decision: verified

- id: f28
  title: PCS 同步与 OPEX（Purple On Demand）运行模式
  type: framework
  V1: {passed: true, reason: "p300-305 命令与规则页完整"}
  V2: {passed: true, check_mode: walkthrough, input: "OPEX 模式要满足什么条件", expected: "云化 OXE + 单订阅 + 端口分摊 + 每晚校验", observed: "p305 原文四要素齐全；空间冗余互斥 p46 支撑（n08）"}
  V3: {passed: true, expected_benefit: "特殊商用模式的评估依据；证据归并 p32/p33/n08/n09"}
  decision: verified

- id: f29
  title: 版本升级流程（手工 + HA 重同步 + S.O.T 自动）
  type: framework
  V1: {passed: true, reason: "p307-310 流程页完整"}
  V2: {passed: true, check_mode: walkthrough, input: "升级怎么做到不翻车", expected: "备份先行/vaa.conf 逐值比对/HA resync", observed: "p308-309 原文三规则直接回答；4.8.006 口径与 p89 一致（n01/n40）"}
  V3: {passed: true, expected_benefit: "版本生命周期操作规程；证据归并 p06/p30/n01/n40"}
  decision: verified

- id: f30
  title: 统计与报告体系（全局/按公司/呼叫日志/邮件周报）
  type: framework
  V1: {passed: true, reason: "p312-317 四层证据完整，p280 CSV 字段表支撑"}
  V2: {passed: true, check_mode: walkthrough, input: "周报怎么开、报表有什么数", expected: "四指标 + 双开关 + 次日报前一天", observed: "p314 指标、p317 开关与 Monday 偏移原文一致（n44）"}
  V3: {passed: true, expected_benefit: "运营与排障抓手；证据归并 p31/n21/n44/n45"}
  decision: verified

- id: f31
  title: 外部数据库集成链（JDBC 驱动 → 库连接 → SQL 节点树）
  type: framework
  V1: {passed: true, reason: "p319-325 三段链 + Oracle 附录完整"}
  V2: {passed: true, check_mode: walkthrough, input: "按来电号码查库转接怎么实现", expected: "装驱动/建连接/SQL+Condition 树", observed: "p320-323 步骤连贯；单字段/首条/空结果规则 p323 原文（p21/n23）"}
  V3: {passed: true, expected_benefit: "与客户信息系统打通的核心；证据归并 p21/p22/p35/c18/c19/n23-n28"}
  decision: verified
```

## 断言级裁决记录

1. **GRUB 口令两处大小写不一致**：成立并如实记录。p92 写 `Generalconfig1!`（小写 c），p93/p249 写 `GeneralConfig1!`（大写 C）——已回源文逐字复核。照抄任一处都可能登不进；详见 needs-review nr-01。
2. **证书章验证 URL 笔误**：成立。p126 写 `https://192.168.1.1.55`（多写一位 `.1`），正确为 `https://192.168.1.55`；见 nr-02。
3. **SIP 抓包残留旧版本号**：成立。p157 User-Agent 4.2.15、p228 User-Agent 4.3.005，与本书 R4.8.006 不一致，属历史抓包；见 nr-03。
4. **VAA_RELEASE 数值两处不一致**：成立。p253 `vaa services` 输出 `VAA_RELEASE : [11]`（与 p89 "Release 11 required" 一致），p274 `.lic` 样例文件 `FEATURE VAA_RELEASE … 9`（样例早于换版）；排障以运行态 vaa services 为准，见 nr-04。
5. **principle 提取器"规格表两处示例免责"**：成立。p52 与 p53 同句 "Given as an example! Always consult the official documentation!"，已并入 f11/f12 与 n03。
6. **无 rejected 断言**：p52 规格三档、p144 Menu 12 选项、p207/p323 SQL 单字段规则、p276 密码 92 天/30/7/1 天提醒、p292 6 个月 20GB、p303 cron 01:00 起每台 +1 分钟、p317 Monday 偏移等关键数字均与原文逐格一致。
