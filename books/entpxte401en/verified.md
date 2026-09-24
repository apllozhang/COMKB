# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f24（主验证对象）；principle p01-p50 / case c01-c18 / counter-example n01-n50 作为各单元的证据素材归并；glossary g01-g65 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-24），基于 543 页全文通读上下文 + 关键数字逐格抽查（15000/100000/32500/4000/400/32、1000 域、240 PCS、1000 表×16 参、20/100/15000 监督、100 节点、24×62=1488、128 广播域、LOG 上限 127、buffer 10 分钟、120 分钟窗口、30 天、2000 DID、事件号 440/427/428/431/432/6004/6005/2879 等，全部回 source_fulltext.txt 对应页命中）

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 21 | f01, f04-f23（详见下表逐条记录） |
| reference | 3 | f02（RLAB 拓扑）、f03（ITSP1 模拟器）、f24（组网 Pod 网卡迁移）——纯教学基础设施，仅作 Boundary/环境背景 |
| needs_review | 0（单元级） | 断言级 5 项转 needs-review.md（前缀互换勘误、PCS 版本漂移、实验不可执行标注、笔误照录、页码归属修正） |
| rejected | 0 | 无编造断言；容量/许可/事件号抽查全部逐格命中 |

## 验证记录

```yaml
- id: f01
  title: 全书课程推进主线——安全地基 → 高可用纵深 → 用户特性 → 组网与数据一致
  type: framework
  V1: {passed: true, reason: "p41-45 课程引入 + 各章 How-To 序列完整；p43/p44 两张架构图给出口径"}
  V2: {passed: true, check_mode: walkthrough, input: "新项目按什么顺序推进 OXE 企业级交付", expected: "给出可执行的阶段顺序", observed: "SSH 地基(f05)→冗余(f06-f08)→域+PCS(f09-f11)→溢出(f12)→组网(f19-f22)与全书章节序一致，无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线，避免先建组网后补免密地基的倒置"}
  decision: verified

- id: f04
  title: OXE 两种系统架构——集中式 IP（1 CS+nMG，15000 分机）与组网（nCS，100000 分机，ABC 协议）
  type: framework
  V1: {passed: true, reason: "p43/p44 架构页单处完整；容量数字逐格命中"}
  V2: {passed: true, check_mode: walkthrough, input: "客户要 3 万分机多站点选哪种", expected: "组网架构（nCS）", observed: "p44 明确 100000 上限 + ABC 特性透明 + 集中管理；p43 集中式上限 15000"}
  V3: {passed: true, expected_benefit: "方案沟通的架构底座；容量数字须带标称上限前提"}
  decision: verified

- id: f05
  title: SSH 密钥分发体系——oxe-ssh-auth（对）与 oxe-nw-sshkey-sync（网）双工具
  type: framework
  V1: {passed: true, reason: "p55-67 机制页 + 两工具用法页完整；p57 N3/CIS 基线原文"}
  V2: {passed: true, check_mode: walkthrough, input: "mastercopy 报 scp 失败先查什么", expected: "免密未建立", observed: "p59-60 工具先查后同步逻辑 + p67 authorized_keys 核验法可定位；证据归并 p01-p04/n02/n05"}
  V3: {passed: true, expected_benefit: "一切协同机制（mastercopy/pcscopy/audit/broadcast）的强制地基；证据归并 p02/p03"}
  decision: verified

- id: f06
  title: CS 冗余机制结构——IP 链路承载清单、角色协商、参考 MG 裁决与 double main 语义
  type: framework
  V1: {passed: true, reason: "p70-82 概念章逐页完整；p74 八类承载清单与 netadmin 例外原文"}
  V2: {passed: true, check_mode: walkthrough, input: "双主（double main）后谁说了算", expected: "连参考 MG 的一侧为 Real Main", observed: "p74/p76 裁决规则一致；p82 三项服务缺失清单可作影响评估"}
  V3: {passed: true, expected_benefit: "冗余故障处置的裁决依据；证据归并 p05-p10/n03-n07"}
  decision: verified

- id: f07
  title: 冗余推荐拓扑与空间冗余的 DNS/DHCP/TFTP 适配结构
  type: framework
  V1: {passed: true, reason: "p80-90 拓扑与外部应用适配页完整；p88/p89/p90 原文命中"}
  V2: {passed: true, check_mode: walkthrough, input: "空间冗余下 SIP 话机切换后连旧主怎么破", expected: "DNS 委派+不缓存+内部解析器启用", observed: "p88/p89/p136 三条规则齐备，与 n09 一致"}
  V3: {passed: true, expected_benefit: "跨子网冗余的配套设计清单；证据归并 p12/n09"}
  decision: verified

- id: f08
  title: 主备数据库一致性三态与不停机升级 11 步序列
  type: framework
  V1: {passed: true, reason: "p79 一致性窗口与 440 事件原文；p83 升级 11 步逐条列出"}
  V2: {passed: true, check_mode: walkthrough, input: "备机宕机 3 小时后恢复还能增量补齐吗", expected: "不能——超 120 分钟窗口须 mastercopy", observed: "p79 窗口 0-120 可配、超时删历史触发 440；与 p09/n08 一致"}
  V3: {passed: true, expected_benefit: "升级排班与备机故障 SLA 的硬时限依据；证据归并 p09/p11/n08"}
  decision: verified

- id: f09
  title: IP 域机制结构——域分配、CAC、编解码选择链、本地化与资源分配
  type: framework
  V1: {passed: true, reason: "p141-152 概念章完整；p147 两条编解码链与跨域取低档原文命中"}
  V2: {passed: true, check_mode: walkthrough, input: "域内两台话机互打受 CAC 限制吗", expected: "不受控（只闸跨域）", observed: "p144 原文明确 intra-domain 不控；与 p15 一致"}
  V3: {passed: true, expected_benefit: "域规划/CAC/编解码排障的统一底座；证据归并 p13-p16/n10/n11"}
  decision: verified

- id: f10
  title: PCS 机制结构——四状态、救援流程与回切计时器三模式
  type: framework
  V1: {passed: true, reason: "p166-177 概念章完整；p170 四状态与 p173 计时器原文命中"}
  V2: {passed: true, check_mode: walkthrough, input: "链路恢复后话机还挂在 PCS 上算正常吗", expected: "正常——Inactive* 过渡态等计时器", observed: "p170/p210 状态语义一致；演练链 INACTIVE→ACTIVE→INACTIVE*→INACTIVE 可复现（c06）"}
  V3: {passed: true, expected_benefit: "PCS 演练与故障判读的状态字典；证据归并 p19/p20/c06"}
  decision: verified

- id: f11
  title: PCS 数据库与限制结构——单向同步、手工参数清单、30 天上限
  type: framework
  V1: {passed: true, reason: "p179-183 数据库/参数/限制页逐条原文命中"}
  V2: {passed: true, check_mode: walkthrough, input: "客户想把 PCS 当分局长久方案行吗", expected: "不行——30 天上限+单向同步", observed: "p182 30 天与违约态、p179 单向同步大写警告齐备；与 p22-p24/n15-n17 一致"}
  V3: {passed: true, expected_benefit: "PCS 定位（临时生存手段）的边界证据；证据归并 p22-p24/n15-n17"}
  decision: verified

- id: f12
  title: Local Private to Public Overflow 机制——三类触发、双层权利与 thin sector
  type: framework
  V1: {passed: true, reason: "p218-226 概念章完整；p221 三类触发、p223 双层权利、p224 thin sector 原文命中"}
  V2: {passed: true, check_mode: walkthrough, input: "断链（PCS 接管）后远端用户怎么被公网找到", expected: "Node Access Prefix+DID 翻译+thin sector 兜非 DID", observed: "p222/p224/p230 机制链自洽；OoS 溢出须系统参数（p225/p232）"}
  V3: {passed: true, expected_benefit: "多站点韧性最后防线的配置与解释依据；证据归并 p25-p27/n20-n22"}
  decision: verified

- id: f13
  title: Speed Dialing 编号体系结构——索引表、双形态、前缀计划与实体映射
  type: framework
  V1: {passed: true, reason: "p236-244 概念章完整；p238 表 32500、p247 默认 4000、p244 每实体 32 区命中"}
  V2: {passed: true, check_mode: walkthrough, input: "缩位号会绕过闭锁吗", expected: "默认绕过，勾 Call Restriction-Barring 才受控", observed: "p236 原文明确；与 p29/n23 一致"}
  V3: {passed: true, expected_benefit: "高频客户需求的容量与安全口径；证据归并 p28/p29/n23"}
  decision: verified

- id: f14
  title: Multiline 与监督键体系——两种形态、键属性与硬上限
  type: framework
  V1: {passed: true, reason: "p257-265 概念章完整；p265 四条上限逐格命中（20/100（网络 20）/15000/一号一键）"}
  V2: {passed: true, check_mode: walkthrough, input: "话务台和寻线组能被监督吗", expected: "不能", observed: "p262 全大写限制原文；与 p30/p31/n25 一致"}
  V3: {passed: true, expected_benefit: "秘书/工作组场景的容量设计依据；证据归并 p30/p31/n24/n25"}
  decision: verified

- id: f15
  title: Manager/Assistant 组机制——键组、过滤表与四个辅助键
  type: framework
  V1: {passed: true, reason: "p276-284 概念章完整；p278 过滤表 1000×16 命中；p279 互斥规则原文"}
  V2: {passed: true, check_mode: walkthrough, input: "助理休假谁来顶过滤", expected: "Routing Assistant（每经理一名，不得已是其助理）", observed: "p283 规则原文；与 p32/n26 一致"}
  V3: {passed: true, expected_benefit: "高管场景刚需的机制与约束清单；证据归并 p32/n26"}
  decision: verified

- id: f16
  title: Hunting / Pickup 组机制——三种搜索、COS 随组、进出组与溢出
  type: framework
  V1: {passed: true, reason: "p299-314 概念章完整；p305 camp-on 公式、p308 三分支参数命中"}
  V2: {passed: true, check_mode: walkthrough, input: "parallel 组能放 multiline 话机吗", expected: "不能——仅 cyclical/sequential", observed: "p308 原文明确；与 p33/p34 一致"}
  V3: {passed: true, expected_benefit: "客服/团队组建的机制与权利模型；证据归并 p33-p35/n27/n28"}
  decision: verified

- id: f17
  title: Desk Sharing 机制——DSS/DSU 角色、虚拟 MAC 与系统选项
  type: framework
  V1: {passed: true, reason: "p329-336 概念章完整；p333 虚拟 MAC 规则与示例逐格命中"}
  V2: {passed: true, check_mode: walkthrough, input: "忙时 DSU 被顶掉通话算 bug 吗", expected: "默认行为（Allow Reset of Busy DSU=True，6004 事件）", observed: "p346/p348 原文与实验样例一致；与 p36/n29 一致"}
  V3: {passed: true, expected_benefit: "灵活办公场景的服务承诺边界；证据归并 p36/n29/n30/n50"}
  decision: verified

- id: f18
  title: Multi Device / Twinset 机制——主副站结构、状态语义与快速移机
  type: framework
  V1: {passed: true, reason: "p353-363 概念章完整；p353 至多 4 副站、p354 DECT/REX 各 1 命中"}
  V2: {passed: true, check_mode: walkthrough, input: "建 twinset 会丢话机上的呼转吗", expected: "会——全部数据清空且复制数据不可改", observed: "p366 全大写警告原文；与 p37/p38/n31/n32 一致"}
  V3: {passed: true, expected_benefit: "一号多机/快速移机方案的行为字典；证据归并 p37/p38/n31-n33"}
  decision: verified

- id: f19
  title: Direct IP Link 机制——ABC-F2 全互联、加密结构与容量边界
  type: framework
  V1: {passed: true, reason: "p383-397 概念章完整；p395 容量组（100/24/62/1488/约 10000 呼时）逐格命中"}
  V2: {passed: true, check_mode: walkthrough, input: "直链断一条其余节点还能互打吗", expected: "能——无中继语义，故障限于孤立节点", observed: "p386 原文明确话务层不绕行；与 n36/n49 一致"}
  V3: {passed: true, expected_benefit: "组网主线（不可逆决策+容量口径）的架构依据；证据归并 p39-p41/n34-n38/n49"}
  decision: verified

- id: f20
  title: Audit 两阶段对账结构——specific/shared 对象行为与参考节点语义
  type: framework
  V1: {passed: true, reason: "p426-442 概念章完整；p435 跑两遍解法、p442 模拟+备份大写警告命中"}
  V2: {passed: true, check_mode: walkthrough, input: "audit 前只放行对端物理地址行吗", expected: "不行——四类地址（物理/twin 物理/主角色/第二主）", observed: "p436 清单原文；与 p42/p43/n39/n40 一致"}
  V3: {passed: true, expected_benefit: "组网数据治理的施工与安全阀；证据归并 p42/p43/n39/n40"}
  decision: verified

- id: f21
  title: Broadcast 增量同步结构——buffer/LOG/RLOG/lupd.dat 闭环与广播域
  type: framework
  V1: {passed: true, reason: "p471-485 概念章完整；p474 默认 10 分钟、p481 128 域、p483 -1..127、p490 LOG 上限 127 命中"}
  V2: {passed: true, check_mode: walkthrough, input: "远端节点写失败会告警吗", expected: "不弹告警——生成 RLOG 等人工处理", observed: "p477 RLOG 机制原文；与 p44/p45/n41-n43 一致"}
  V3: {passed: true, expected_benefit: "组网日常运维与巡检抓手；证据归并 p44/p45/n41-n43"}
  decision: verified

- id: f22
  title: 组网双向溢出对称结构——Private to Public 与 Public to Private Rerouting
  type: framework
  V1: {passed: true, reason: "p499-507/p517-522 两概念章完整；p505 Number to add 不广播、p519 ARS 强制、p522 -1 路由规则命中"}
  V2: {passed: true, check_mode: walkthrough, input: "公网拨远端 DID 怎么折回专线省费", expected: "判别器挂 ARS 表，路由 1 用 TG=-1 还原内号走直链", observed: "p519-p522 机制链自洽；-1 路由每表一条且首位"}
  V3: {passed: true, expected_benefit: "组网退路与省费闭环的双向解释；证据归并 p46/p47/n44/n45"}
  decision: verified

- id: f23
  title: OXE 维护命令地图——按功能域归类的命令/工具清单
  type: framework
  V1: {passed: true, reason: "命令散布全书 Maintenance 节，来源页 23 处；role/twin/bascul/domstat 等输出截图可对"}
  V2: {passed: true, check_mode: walkthrough, input: "排查域与编解码用哪几个命令", expected: "domstat/cnx dom/compvisu", observed: "p159-163 三命令输出与候选归类一致；事件号 440/2879/2880/2884/2832/2846/6004/6005 可经 incvisu/incinfo 查"}
  V3: {passed: true, expected_benefit: "跨能力排障的统一入口（cli-toolbox 卡主证据）；证据归并 p49/p50"}
  decision: verified
```

## 断言级裁决记录

1. **counter-example 提取器"前缀 Note 与截图互换"（n28）**：成立，但两个互换方向相反，需精确记录。代接前缀：p325 Note 文本说 55=组代接/56=直接代接，而 p314 概念图（55+号码=直接代接）与 p325 截图（55 行对 Direct call pick-up）均为 55=直接/56=组——Note 是少数派。进出组前缀：p320 Note 文本与 p304 概念图一致说 480=进入/481=退出，仅 p320 截图行显示 480 对 Sta. Group exit——截图是少数派。现场一律以 Prefix Plan 实查为准（详见 needs-review nr-01）。
2. **PCS 版本漂移（n46）**：成立。p187 部署章显示 R101.1-n4.523-0-fr-c0s1，p212 断链章显示 R101.1-n4.205-19-fr-c0s1——截图来自不同批次环境，版本比对以现场欢迎信息为准（nr-02）。
3. **principle 提取器"OPUS dynamic payload 默认 125"页码归属**：断言为真（p159 原文：外部设备用其他值时以本参数为准，默认 125），但候选 p13 标注的 p147-148/p156 未含该句，实际位于 p159——能力卡引用按 p159。
4. **容量三层口径（n49）**：成立且必须整体引用——1488=单链并发（24 接入×62 通道，p395）；约 10000 呼/时/链为 8 接入口径的工程值（p395）；节点级另有覆盖 direct/SIP/ABCF-IP trunk 的全局上限（默认 -1，超限 6005，p395/p406）。
5. **无 rejected 断言**：15000/100000 分机、32500（默认 4000）/400 范围/32 区、1000 域、240 PCS/一 PCS 至多救 1000 域、1000 过滤表×16 参数、监督 20/100（网络 20）/15000、100 节点/24×62=1488、128 广播域（-1..127）、LOG 上限 127、buffer 默认 10 分钟、失联窗口 120 分钟（0-120）、PCS 30 天、每前缀 2000 DID——全部与原文逐格一致。
