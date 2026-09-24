# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f28（主验证对象）；principle p01-p50 / case c01-c23 / counter-example n01-n46 作为各单元的证据素材归并；glossary g01-g69 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-24），基于 650 页全文页码抽查 + 提取器证据交叉核对（p62/63/64/66/77/86/89/91/98/106/109/111/114/129/133/138/145/146/156/160/164/168/181/230/247/261-266/290/293/300/306/310/325/327/349/354/367/385/396/402/408/414/421/422/433/443/446/460/462/463/470/476/478/492/497/503/510/512/521/523/529/530/537/548/550 逐页回原文）

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 26 | f01, f04-f28（区间内全部） |
| reference | 2 | f02（RLAB 平台结构）、f03（ITSP1 SIP 模拟器）——纯培训基础设施，内容真实但仅作 Boundary 背景 |
| needs_review | 0（单元级） | 断言级 5 项转 needs-review.md（汇率笔误、运营商名残留、姓名颠倒、方向表残留、MKT/Marketing 命名漂移） |
| rejected | 0 | 无编造断言；关键数字（500/90 分钟/47 字段、744 文件、31+94=125 天、150ms/3%/5% KPI、400 行/50 页/100000 行、30 分钟/5 分钟轮询、1.21/0.82 汇率、10%/20% 教学税率）均与原文逐格一致 |

verified 明细：f01, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——产品底座 → 实验平台 → 计费管道 → 钱/组织/安全治理 → 报表输出 → 性能监控 → 归档
  type: framework
  V1: {passed: true, reason: "p1-650 章节推进逐段可回溯；p4 目录页十段勾选清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "新项目按什么顺序交付 8770 计费与性能", expected: "给出可执行的阶段顺序", observed: "管道(p59-114)先于资费治理(p115-357)、报表(p358+)与性能(p405+)收尾、归档(p518-548)兜底，与后续实验依赖（Telecom 1 被 report #4 引用）互证"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线，避免先出报表后建资费的倒置"}
  decision: verified

- id: f04
  title: OmniVista 8770 系统架构与协议矩阵一张图
  type: framework
  V1: {passed: true, reason: "p6-7 拓扑图与协议矩阵单处完整（CMISE/(S)FTP/Telnet-SSH/LDAP 对 OXE；OMC FTP/HTTPS 对 OXO；SNMPv3；SMTP；HTTPS）"}
  V2: {passed: true, check_mode: walkthrough, input: "8770 靠什么协议取 OXE 的计费数据", expected: "FTP/(S)FTP 数据面 + SSH 配置面", observed: "p7 矩阵与 p98 回收原理（FTP 取回）、p109 FTP 凭证配置三处一致"}
  V3: {passed: true, expected_benefit: "方案沟通与防火墙评估的架构底座"}
  decision: verified

- id: f05
  title: 8770 应用套件分区——thick client 五套件 + WBM 四应用
  type: framework
  V1: {passed: true, reason: "p10-39 各套件逐一定义；p35 WBM 许可门槛（Unified Management）明确"}
  V2: {passed: true, check_mode: walkthrough, input: "流量分析和审计在 OXO Connect 上能用吗", expected: "不能——仅 OXE", observed: "p25/p29 Limits 原文明确（n01 互证）；WBM Configuration 四条边界（n02）一致"}
  V3: {passed: true, expected_benefit: "功能承诺的平台边界依据；证据归并 n01/n02/n03"}
  decision: verified

- id: f06
  title: 虚拟化支持矩阵与容量规划工具
  type: framework
  V1: {passed: true, reason: "p8 Hypervisor 清单完整（ESXi 6.x/7.0/8.0、Hyper-V 2016/2019/2022、Nutanix AHV 20220304、AWS）"}
  V2: {passed: true, check_mode: walkthrough, input: "虚机部署要多付 8770 许可吗", expected: "虚拟化本身不占 8770 许可", observed: "p8 原文 'No OmniVista 8770 license for virtualization'；补充服务可能引增成本的但书同页给出"}
  V3: {passed: true, expected_benefit: "部署形态与选型入口；口径为 Ed45 时点（p01 互证）"}
  decision: verified

- id: f07
  title: 跨版本兼容矩阵（8770 R4.2-R5.2 × PBX/OT 版本）
  type: framework
  V1: {passed: true, reason: "p9 矩阵逐格存在（四列 8770 版本 × 各 PBX 行）"}
  V2: {passed: true, check_mode: walkthrough, input: "OXE Purple R101.1 配哪个 8770 版本", expected: "仅 R5.2", observed: "p9 原文 R101.0/101.1/101.2 行仅 R5.2 列打 X；实验机 R101.1-n4（p93）即此组合"}
  V3: {passed: true, expected_benefit: "升级顺序决策依据；证据归并 p02 逐格转写"}
  decision: verified

- id: f08
  title: 计费票据文件体系——缓冲/tax.tmp/TAX*.DAT/ACCOUNT.LIS 四件套与落盘时机
  type: framework
  V1: {passed: true, reason: "p62 文件四件套图 + p63 缓冲=3 条示例时序 + p64 90 分钟规则三处连贯"}
  V2: {passed: true, check_mode: walkthrough, input: "打完电话为什么立刻查不到 .DAT 文件", expected: "票据先进内存缓冲（≤500 条），满/90 分钟/account compress 才落盘", observed: "p62 max 500 records、p63 08:55 新票进 tax.tmp 09:05 合并出 TAXAAAAC.DAT、p64 90 分钟无票 11:00 建文件，三处行为闭环"}
  V3: {passed: true, expected_benefit: "票据排障第一性解释；证据归并 p03/p04/p06"}
  decision: verified

- id: f09
  title: 计费记录回收原理——四步增量同步管道（OXE→8770）
  type: framework
  V1: {passed: true, reason: "p98 四步图完整（对比 ACCOUNT.LIS → FTP 取回 → 提取加载 → 删文件更新索引）"}
  V2: {passed: true, check_mode: walkthrough, input: "8770 怎么知道该取哪些文件", expected: "对比两侧 ACCOUNT.LIS 增量取回", observed: "p98 步骤 1 原文明确；p112 loader 目录 networknumber=1/subnetworknodenumber=101 实测路径一致"}
  V3: {passed: true, expected_benefit: "回收链路的机制总纲；证据归并 p13/p15/c04"}
  decision: verified

- id: f10
  title: 五种计费方法与选择逻辑
  type: framework
  V1: {passed: true, reason: "p99 五法清单完整；p101 建树期用 organization update 的理由原文；p102 global 实体键公式"}
  V2: {passed: true, check_mode: walkthrough, input: "新站点该选哪种计费方法", expected: "建树期只建树不取票，树定型后切 Detailed", observed: "p101 'Moving Cost center or subscriber ... time-consuming' 与 n09 顺序坑互证"}
  V3: {passed: true, expected_benefit: "上线排期与方法切换依据；证据归并 p12"}
  decision: verified

- id: f11
  title: 记录收集器与 PCS 被动回收结构
  type: framework
  V1: {passed: true, reason: "p103 收集器许可口径；p104-106 PCS 发现机制与 PCS ID 十六进制换算例（AC199E64=172.25.158.100）"}
  V2: {passed: true, check_mode: walkthrough, input: "只把票据转给第三方计费软件要计费许可吗", expected: "不用——Ticket collector 许可即可", observed: "p103 原文 'No accounting license, only Ticket collector license is required'"}
  V3: {passed: true, expected_benefit: "外部计费集成与 PCS 站点的方案边界；证据归并 p14/n46/g38"}
  decision: verified

- id: f12
  title: 运营商资费对象模型——Period/Calendar/Region/Tariff/Direction 五件套
  type: framework
  V1: {passed: true, reason: "p117-118 对象定义与 'A tariff is applied to each Calling Region - Called Region pair' 原文"}
  V2: {passed: true, check_mode: walkthrough, input: "一个被叫号怎么落到具体价格", expected: "前缀归被叫区 → 方向配对 → 绑定资费", observed: "p118 区域/方向定义 + p156 最优匹配规则 + p181 前缀唯一性三处机制闭环"}
  V3: {passed: true, expected_benefit: "资费建模的概念骨架，全书最重章的底座；证据归并 p16/p17/g13-g16"}
  decision: verified

- id: f13
  title: 费率计算模式分类与参数体系（资费类型学）
  type: framework
  V1: {passed: true, reason: "p128-137 四模式逐一定义（exact/round up-down/based on unit/PCX given）"}
  V2: {passed: true, check_mode: walkthrough, input: "客户给的价目是每分钟单价，Unit duration 填多少", expected: "60（按分钟价），8770 内部折算秒价", observed: "p129 原文 'Set at 60 if you enter a Unit Cost per minute'"}
  V3: {passed: true, expected_benefit: "费率录入的参数字典；证据归并 p18/p19"}
  decision: verified

- id: f14
  title: 服务费与 SVA（增值业务）模型
  type: framework
  V1: {passed: true, reason: "p137 SVA 号码范围与 C+S 三组合定义；p162 双资费配置 Notes；p173 方向绑定"}
  V2: {passed: true, check_mode: walkthrough, input: "特服号只建一个资费行不行", expected: "不行——通信资费与服务资费必须成对", observed: "p162 Notes 原文 'you must configure two tariffs'；n14 漏配后果一致"}
  V3: {passed: true, expected_benefit: "特服号计费的结构要求；证据归并 p20/n14"}
  decision: verified

- id: f15
  title: Code Book 文件体系——十种文件与格式规则
  type: framework
  V1: {passed: true, reason: "p228-233 十文件清单与格式规则（@表头/Tab 分隔/%注释）完整"}
  V2: {passed: true, check_mode: walkthrough, input: "运营商配置怎么搬到另一台服务器", expected: "导出 code book 文件集，改 .itl 节点名后导入", observed: "p230 格式规则 + p233 Node 必须匹配目标机声明 + p247 oxe9≠oxe 实错三处闭环"}
  V3: {passed: true, expected_benefit: "跨服务器交付的载体说明；证据归并 p26/n15/n16/n17"}
  decision: verified

- id: f16
  title: 计费组织树对象模型与自动更新来源
  type: framework
  V1: {passed: true, reason: "p253-257 对象模型（level/cost center/chargeable entry）与两条自动更新来源原文"}
  V2: {passed: true, check_mode: walkthrough, input: "中继组的话务记录落到组织树哪里", expected: "默认成本中心（Data collection 页签配置）", observed: "p257/p271 默认成本中心定义与 g05 一致；cc=255 落根（p256）一致"}
  V3: {passed: true, expected_benefit: "成本分摊的结构基础；证据归并 p27/g04-g07"}
  decision: verified

- id: f17
  title: 组织更新操作语义图——剪贴/复制/回溯/工具重建四象限
  type: framework
  V1: {passed: true, reason: "p261-266 四种语义逐页定义（cut 无历史/copy 带历史/回溯按身份/工具全局重挂）"}
  V2: {passed: true, check_mode: walkthrough, input: "员工换了成本中心，历史票据怎么归位", expected: "按身份（PCX ID/分机号）回溯到活动设备", observed: "p263 身份定义 + p290 全大写 Warning（选设备不选用户）+ p295 残留成本中心手工删，三处一致"}
  V3: {passed: true, expected_benefit: "组织变更操作的选择依据；证据归并 p28/n18-n21"}
  decision: verified

- id: f18
  title: 掩码档案结构与继承链
  type: framework
  V1: {passed: true, reason: "p298 可掩字段清单；p300 Default 档案规则；p306 显示优先与示例（Professional 4/4、Unmasked 4/2）"}
  V2: {passed: true, check_mode: walkthrough, input: "汇总报表为什么没按子树的档案遮蔽", expected: "grouped 报表只认 Default 档案的两个 group 类别", observed: "p310 原文 'the server ignores the mask profiles applied to the organization'；n23 一致"}
  V3: {passed: true, expected_benefit: "机密性验收的口径依据；证据归并 p29/p30/n06/n22/n23"}
  decision: verified

- id: f19
  title: 成本档案（Cost profile）双页签结构——发票价调整与订阅费
  type: framework
  V1: {passed: true, reason: "p325 发票价公式（x=三类成本之和，Ax+B）与 p327 订阅出票时机原文"}
  V2: {passed: true, check_mode: walkthrough, input: "月中的员工订阅费怎么算", expected: "从次月 1 日起计", observed: "p327 原文 'users arriving in the current month will only be charged from the first of the following month'；n25 一致"}
  V3: {passed: true, expected_benefit: "内部再计费与订阅口径的机制解释；证据归并 p31/p32/n25"}
  decision: verified

- id: f20
  title: 计费可见域控制机制与决策树
  type: framework
  V1: {passed: true, reason: "p343-346 两级决策树与 AdminNmc 全域说明"}
  V2: {passed: true, check_mode: walkthrough, input: "开了可见域后管理员看不到数据", expected: "未配域时整树只剩根——顺序问题非故障", observed: "p351 警告原文 + n26 启用顺序坑互证；p355 群组域无效"}
  V3: {passed: true, expected_benefit: "多管理员权限切分的机制与上线顺序；证据归并 p33/n26"}
  decision: verified

- id: f21
  title: Reports 应用结构——预定义/定义/实例/解密报表与 Querytool/Designer 双页签
  type: framework
  V1: {passed: true, reason: "p361 报表树三类节点；p385 定义四步向导（Source/Item/Type/Template）；p387-399 两页签字段"}
  V2: {passed: true, check_mode: walkthrough, input: "预定义报表直接生成为什么不行", expected: "必须 Copy/Paste 到个人目录", observed: "p361/g20 与 c16 步骤 3 行为一致"}
  V3: {passed: true, expected_benefit: "报表交付与定制的结构地图；证据归并 p36/p37/n30/n31"}
  decision: verified

- id: f22
  title: IP ticket（VoIP 话单）生成与回收结构
  type: framework
  V1: {passed: true, reason: "p408 分段出票图 + p410 四步回收（IP.LIS/SIP.LIS 比对）原文"}
  V2: {passed: true, check_mode: walkthrough, input: "一通跨节点 IP 通话出几张票", expected: "每段双向各一票", observed: "p408 'divided into one or more segments ... at the end of each segment' 与图示一致"}
  V3: {passed: true, expected_benefit: "VoIP 质量数据链的机制底座；证据归并 p38/p39/p48/n32"}
  decision: verified

- id: f23
  title: 流量分析文件体系——pmm/inf 命名规则与观察对象
  type: framework
  V1: {passed: true, reason: "p433 文件命名规则逐字段（周 00-51/日 MTWJFSU/半小时 00-47/XX 占位）"}
  V2: {passed: true, check_mode: walkthrough, input: "被叫号话务报表是空的", expected: "默认只算话务台/话务台组/中继组，须改 PtpType ALL", observed: "p446-447 任务命令原文与 n34 一致；p433 与 f09 同管道回收互证"}
  V3: {passed: true, expected_benefit: "话务报表部署清单必查项；证据归并 p40/p41/n01/n33/n34"}
  decision: verified

- id: f24
  title: Tracking 原理链——文件→累计计数器→档案→阈值检测→告警/邮件
  type: framework
  V1: {passed: true, reason: "p460 四源文件链路图 + p462 变化率公式与移动平均默认期"}
  V2: {passed: true, check_mode: walkthrough, input: "超阈值是实时告警吗", expected: "不是——由任务与夜间计数器驱动", observed: "p460 半小时/日/月/年计数器分层 + f24 conditions（任务驱动）与 p42 一致"}
  V3: {passed: true, expected_benefit: "告警预期管理（非实时）与排障入口；证据归并 p42/p43/n35"}
  decision: verified

- id: f25
  title: Web Performance 数据采集与仪表盘结构（五大主题）
  type: framework
  V1: {passed: true, reason: "p492 两条数据腿原文（VoIP CDR + OXE SNMP MIB 双 MIB）；p494-497 五主题与两类仪表盘"}
  V2: {passed: true, check_mode: walkthrough, input: "轮询周期能调快吗", expected: "R5.0 GA 固定 30 分钟；R5.0 MD1 起最低 5 分钟（经 ToolsOmniVista）", observed: "p492 版本分界原文与 p507 操作入口一致"}
  V3: {passed: true, expected_benefit: "实时仪表盘的部署边界与调优入口；证据归并 p44/p45/n36-n38"}
  decision: verified

- id: f26
  title: 计费归档生命周期——31 天归档 + 94 天清理 = 最长 125 天
  type: framework
  V1: {passed: true, reason: "p521 archZ 格式与每天每节点一档；p523 31+94=125 推导原文；p529-530 参数书写规则"}
  V2: {passed: true, check_mode: walkthrough, input: "归档文件三年没动会不会被删", expected: "按记录日期而非文件创建日期清理", observed: "p529/p530 'according to the date of the records and not to the creation date of archive files' 两处重现"}
  V3: {passed: true, expected_benefit: "数据寿命与库性能治理依据；证据归并 p46/p47/n39/n40"}
  decision: verified

- id: f27
  title: 关键菜单路径集（8770 各应用速查）
  type: menu-path
  V1: {passed: true, reason: "各 How-To 章路径逐条存在（p142 Service Manager、p351 AccountingParameters、p422 VoipParameters、p476 MonitoringParameters、p529 NmcArchive）"}
  V2: {passed: true, check_mode: walkthrough, input: "改移动平均默认期从哪进", expected: "Administration > nmc > Application Configuration > Application Settings > Accounting > MonitoringParameters", observed: "p476 截图说明路径一致；c04 步骤 9 加载过滤路径一致"}
  V3: {passed: true, expected_benefit: "全书操作的导航索引；菜单名为 Ed45 英文界面口径"}
  decision: verified

- id: f28
  title: 日志与数据目录地图（排障入口）
  type: structure
  V1: {passed: true, reason: "五份日志与四组目录逐条回溯（p80/p114/p179/p517 日志名；p98/p109/p112 loader/collector；p529 归档路径；p65/p433 OXE 侧）"}
  V2: {passed: true, check_mode: walkthrough, input: "票据没入库先看什么", expected: "C:\\8770\\log\\NMCLD_1.log 的 TicketsRead/BadLines/速度", observed: "p114 日志样例 'Nb of tickets read = 9 ==> Processing speed = 52 tic/sec' 与 c04 验收一致"}
  V3: {passed: true, expected_benefit: "计费/成本/性能三类排障的统一入口；证据归并 p13/n13"}
  decision: verified
```

## 断言级裁决记录

1. **book 内 p402 与 p550 汇率矛盾**：成立并如实记录（n41）——report #1 题面写 "1 €= 1,21 dollar"，实现章 p550/p557 用 "1 €= 1,3 dollar" 与公式 $cost=€cost*1.3。教材自身未修订，实践按交付约定取值；详见 needs-review nr-01。
2. **p607 运营商名 "Telecom 7 / Telecom 0"**：成立并如实记录（n42）——report #4 题面排版残留，实现章 p613 过滤器与截图均为 Telecom 1 / Telecom 2；详见 needs-review nr-02。
3. **p89/p91 姓名字段颠倒**：成立并如实记录（n43）——p91 建号表把 31011 的 Name 填 Alice、First Name 填 Adams，p89 分配表同写 "31011 Adams Alice"；31010（Ava Adore）正确；详见 needs-review nr-03。
4. **p210 方向表文字残留**：成立并如实记录（n44）——Telecom 2 的 Brest→Brest 方向说明残留 Telecom 1 的 "Local region"、主叫写作截断的 "Brest re"；按 Telecom 2 实际双栖区结构配置；详见 needs-review nr-04。
5. **成本中心命名 MKT/Marketing 漂移**：成立并如实记录——p89 命名口径为 MKT，p305/p332/p349/p470 的组织树提醒行写 Marketing（p349 同页两行并存）；机制不受影响，引用统一按 p89 的 MKT 口径并标注；详见 needs-review nr-05。
6. **无 rejected 断言**：p62 缓冲 500 条、p63/p64 落盘时序、p66 47 字段票据、p77 节点号公式、p86 744 文件、p98 四步回收、p106 PCS ID 换算、p129-136 费率公式族、p145/146 币种税率、p367 报表六上限、p414/421/422 KPI 与清理、p443/446 阈值与 PtpType、p462/463 变化率、p492/503/507/510/512 Web Performance、p521/523/529/530/537/548 归档恢复——全部与原文逐格一致。
