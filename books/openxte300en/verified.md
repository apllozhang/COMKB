# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f28（主验证对象）；principle p01-p45 / case c01-c30 / counter-example n01-n42 作为各单元的证据素材归并；glossary g01-g56 转 book/glossary.md（见 references.md）
> 验证人: 主会话（2026-09-23），基于 603 页全文通读 + 提取器页码证据交叉核对

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 26 | f01-f03、f06-f28（详见下表） |
| reference | 2 | f04（RLAB POD 实验环境结构）、f05（ITSP1 SIP 模拟器）——教学基础设施，供 Boundary 与 book/overview 引用，不作独立交付能力 |
| needs_review | 0（单元级） | 断言级 4 项转 needs-review.md（公告 wav 目录、笔误清单、示例输出历史值、R-Lab 特例） |
| rejected | 0 | 无编造断言；关键数字（端口/容量/规格）逐格核对一致 |

verified 明细：f01, f02, f03, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——方案概览 → 实验环境 → 装机初始化 → 许可 → 集成声明 → 业务供给 → 安全客户端 → 运维
  type: framework
  V1: {passed: true, reason: "p3-10 章节推进逐段给出；p50-51 部署主步骤链与章节顺序互证"}
  V2: {passed: true, check_mode: walkthrough, input: "新 OTMS 项目按什么顺序交付", expected: "给出可执行的阶段顺序", observed: "十段主线与 f08 七步链无矛盾，许可闸门在集成声明之前"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线；18 项任务的组织轴"}
  decision: verified

- id: f02
  title: OTMS 组件架构图——ICAS/ICM/AMS 三组件与 8770/OXE 的分离部署
  type: framework
  V1: {passed: true, reason: "p5-7 架构图与组件定义单处完整"}
  V2: {passed: true, check_mode: walkthrough, input: "语音邮件接入走哪个 SIP 服务器哪个端口", expected: "Mule 5040 / ESS 5260", observed: "p215/p232 与 f14 两条外部网关互证，别名口径一致"}
  V3: {passed: true, expected_benefit: "SIP 集成与排障分面的架构底座"}
  decision: verified

- id: f03
  title: OTMS-v 虚拟化布局——ESXi 上六类虚机
  type: framework
  V1: {passed: true, reason: "p8-9 六虚机布局与版本矩阵完整"}
  V2: {passed: true, check_mode: walkthrough, input: "OTMS-v 要起哪些虚机、宿主认哪些版本", expected: "六虚机 + ESXi 6.5/7.0.x + Hyper-V 2016/2019", observed: "p9 版本矩阵与 p02 一致；5000 用户口径与 p01 一致"}
  V3: {passed: true, expected_benefit: "部署规划与宿主选型的基线"}
  decision: verified

- id: f04
  title: 培训实验环境结构——RLAB POD 两形态 + 实例参数总表
  type: framework
  V1: {passed: true, reason: "p10-25 拓扑与参数总表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "实验里哪台机器是什么地址什么账号", expected: "按实例总表可查", observed: "p16 总表可查；IP 表 192.16.8.1.x 为原文排版笔误（n41），以他页 192.168.1.x 为准"}
  V3: {passed: true, expected_benefit: "实验口径唯一锚点；仅作 Boundary 与 book/overview 背景，不晋级独立能力"}
  decision: reference

- id: f05
  title: ITSP1 SIP 运营商模拟器拓扑与号码变换规则
  type: framework
  V1: {passed: true, reason: "p26-30 拓扑与号码规则完整"}
  V2: {passed: true, check_mode: walkthrough, input: "POD 怎么验证出局通路", expected: "按模拟器号码规则外呼", observed: "p29 号码变换例（0110312345 → +33110312345）自洽；ITSP2 仅拓扑图出现无细节"}
  V3: {passed: true, expected_benefit: "task-01 的教学验证手段；教学专用，不进生产口径"}
  decision: reference

- id: f06
  title: 软件安装三路线决策——手动 DVD / 手动 ISO / SOT 自动化
  type: framework
  V1: {passed: true, reason: "p40-47 三路线定义与代价清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "生产装 OTMS 选哪条路", expected: "SOT 自动化，手动作备选", observed: "p43 手动易错清单 + p46 SOT 静默/自动挂载优势，推荐关系明确"}
  V3: {passed: true, expected_benefit: "装机路线决策依据；证据归并 p03/n10/n11"}
  decision: verified

- id: f07
  title: SOT 工具结构——两模式 × 两配置 × 两工作模式
  type: framework
  V1: {passed: true, reason: "p53-65 模式/配置/工作模式三维度完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Template Factory 能不能用来装 OpenTouch", expected: "不可用", observed: "p56 明确 Template Factory 对 OpenTouch 产品不可用；规格与 p03 一致"}
  V3: {passed: true, expected_benefit: "装机工具操作面与选型边界；证据归并 c02/p03"}
  decision: verified

- id: f08
  title: OTMS 部署主步骤链——装机 → 重启 → 向导 → OXE → 8770 → 8770 配置 → OXE 管理
  type: framework
  V1: {passed: true, reason: "p50-51 主步骤两页完整"}
  V2: {passed: true, check_mode: walkthrough, input: "装完软件还要做什么", expected: "重启进向导、装 OXE/8770、双向声明、SIP 与用户", observed: "七步链覆盖 task-02 至 task-14 骨架，与各 How-To 章一一对应"}
  V3: {passed: true, expected_benefit: "全书第二至第七部分的组织轴；交付 checklist 骨架"}
  decision: verified

- id: f09
  title: Post-installation wizard 结构——两模式入口与十个配置节
  type: framework
  V1: {passed: true, reason: "p88-108 十节清单与两入口完整"}
  V2: {passed: true, check_mode: walkthrough, input: "新装机 HA 能不能开", expected: "不能，保持 Disable", observed: "p94 原文明确仅 R2.2.x 迁移保留（n02）；十节顺序与 c04 实验步骤一致"}
  V3: {passed: true, expected_benefit: "初始化总闸的操作与决策面；证据归并 c04/c05/p04-p06/n02/n03/n05/n06"}
  decision: verified

- id: f10
  title: 系统连接通道结构——VM 控制台 / SSH(Telnet) / 远程桌面 三通道 + 账号总表
  type: framework
  V1: {passed: true, reason: "p109-127 三通道与账号表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "OT 服务器能不能 Telnet", expected: "不授权，必须 SSH v2", observed: "p113 原文明确；OXE 用 Telnet 属实验未启安全（n08）"}
  V3: {passed: true, expected_benefit: "一切后续操作的入口；证据归并 c06/c07/p43/n08/n09"}
  decision: verified

- id: f11
  title: 许可体系结构——三族文件、两种锚定物、FlexLM 内嵌/外部两形态
  type: framework
  V1: {passed: true, reason: "p128-154 四层结构（文件族/锚定物/FlexLM 形态/目录流转）完整"}
  V2: {passed: true, check_mode: walkthrough, input: "OXE-v 的许可怎么验、容量在哪", expected: ".ice 走 FlexLM 验 Product ID，容量仍看本地 .swk", observed: "p130-132/p159 口径自洽；OXE 亦可 Cloud Connect（p130/132 标注）"}
  V3: {passed: true, expected_benefit: "许可闸门的完整概念面；证据归并 c08-c10/p07-p13/n05/n06/n12-n15"}
  decision: verified

- id: f12
  title: OXE 声明流程（8770 侧）——前置准备 → 网络子网节点三级建树 → 同步
  type: framework
  V1: {passed: true, reason: "p186-192 三段流程与字段值完整"}
  V2: {passed: true, check_mode: walkthrough, input: "8770 里 OXE 节点号 101 怎么来的", expected: "ABC 网络号 100 倍 + 节点号", observed: "p190 公式与示例（1×100+1=101）一致；APPLY 硬规则 p187 与 n16 一致"}
  V3: {passed: true, expected_benefit: "管理闭环第一半；证据归并 c11/p14/p15/n16"}
  decision: verified

- id: f13
  title: OpenTouch 声明流程（8770 侧）——bics.conf 取凭证 → 双向声明 → 拓扑互挂
  type: framework
  V1: {passed: true, reason: "p193-203 四段流程与凭证映射完整"}
  V2: {passed: true, check_mode: walkthrough, input: "8770 声明 OT 的账号口令从哪来", expected: "OT 上 bics.conf 逐项取用", observed: "p194 三账号与 p16 g27 对应一致；节点号 99 自由号规则 p196 明确"}
  V3: {passed: true, expected_benefit: "系统集成核心；证据归并 c12/p16/p17/n04"}
  decision: verified

- id: f14
  title: OXE SIP 配置流程——trunk group → 本地网关/代理/注册器 → 外部网关 10/11 → trusted → 全局
  type: framework
  V1: {passed: true, reason: "p226-234 五段流程逐字段完整"}
  V2: {passed: true, check_mode: walkthrough, input: "两条外部网关分别指向谁", expected: "10 号到 OT SIP server 5260、11 号到 Mule 5040", observed: "p231/p232 与 f02 端口口径互证；spatial redundancy 字段差异已标（n17）"}
  V3: {passed: true, expected_benefit: "语音业务承载层；证据归并 c14/p19/p44/n17"}
  decision: verified

- id: f15
  title: Prior management 全景——号码段/前缀/语音邮件/拨号规则/UDAS/会议桥六块
  type: framework
  V1: {passed: true, reason: "p213-225 讲义 + p235-254 How-To 六块完整"}
  V2: {passed: true, check_mode: walkthrough, input: "31000-31499 号段在哪边声明", expected: "OT 侧 Ranges 页签声明归属 OXE", observed: "p216/p237 口径一致；UDAS 周期 ≥1 禁 0（p243）与 n20 一致"}
  V3: {passed: true, expected_benefit: "拨打行为正确性总闸；证据归并 c15/p20-p26/n18-n21"}
  decision: verified

- id: f16
  title: 告警对接拓扑——OT SNMP agent → 8770 SNMP server（Inform v3）→ MIB 重载
  type: framework
  V1: {passed: true, reason: "p204-212 五段流程与数值完整"}
  V2: {passed: true, check_mode: walkthrough, input: "MIB 首次下载不全怎么办", expected: "删 ICE 目录、重启 NMC Alarm Server 与 ompd", observed: "p209 三步与 c13 一致；161/162 端口与 p18 一致"}
  V3: {passed: true, expected_benefit: "运维可视化起点；证据归并 c13/p18/n42"}
  decision: verified

- id: f17
  title: 用户与档案体系结构——Users 应用分区、三类用户、双侧档案与 ACU 生成原理
  type: framework
  V1: {passed: true, reason: "p255-278 应用分区与三类用户定义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Users 应用里能不能新建档案", expected: "不能，只能改；建删回配置工具", observed: "p277/p278 原文明确；OXE 档案实时、OT 档案需完整同步（p297）不对称行为自洽"}
  V3: {passed: true, expected_benefit: "用户供给主战场的权责边界；证据归并 c16/p27"}
  decision: verified

- id: f18
  title: 用户创建操作流——Directory 建树 → 三类用户逐个建 → 存量加 OT → 移树
  type: framework
  V1: {passed: true, reason: "p279-288 四段操作完整"}
  V2: {passed: true, check_mode: walkthrough, input: "三类用户在界面上怎么区分", expected: "type=None / type=OXE 无 OT 权 / Connection（OXE+OT）", observed: "p258/p264 与 c17 实验步骤一致；口令策略 p284-286 与 p28 一致"}
  V3: {passed: true, expected_benefit: "日常最高频供给操作；证据归并 c17/p28"}
  decision: verified

- id: f19
  title: Web Provisioning Client 供给流程——前置四查 → 登录 → 三页签建 Connection 用户
  type: framework
  V1: {passed: true, reason: "p289-301 讲义约束 + How-To 三页签完整"}
  V2: {passed: true, check_mode: walkthrough, input: "WPC 能建 Conversation 用户吗", expected: "不能", observed: "p292 限制清单（不建 Conversation 用户/一台设备/档案回配置工具）与 p29/n40 一致"}
  V3: {passed: true, expected_benefit: "批量 MACD 的入口与边界；证据归并 c18/p29/n40"}
  decision: verified

- id: f20
  title: 语音邮箱管理体系——默认系统 → 建箱挂人 → 许可 → 管理员/最终用户两侧定制
  type: framework
  V1: {passed: true, reason: "p302-337 讲义 + How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "建邮箱不选档案能保存吗", expected: "不能，Configuration 页必选", observed: "p330 原文明确；备选问候 ≤2 且需授权（p333）自洽"}
  V3: {passed: true, expected_benefit: "语音业务核心体验的管理面；证据归并 c19/p35/n23"}
  decision: verified

- id: f21
  title: 语音邮箱档案结构——默认三档案 + 四页签选项面
  type: framework
  V1: {passed: true, reason: "p338-344 三默认档案与四页签完整"}
  V2: {passed: true, check_mode: walkthrough, input: "配额填了为什么没生效", expected: "需启用 Check quota", observed: "p342 配额语义与条目 conditions 一致；UM 型 Standard 档案区分明确（p339）"}
  V3: {passed: true, expected_benefit: "邮箱行为的参数面；证据归并 c20/p30"}
  decision: verified

- id: f22
  title: IMAP 收取语音邮件流程——Outlook 建账号 → 安全对齐 → 验证
  type: framework
  V1: {passed: true, reason: "p345-352 三段流程完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Outlook 测试邮件失败是不是配错", expected: "属预期（OT 不做 SMTP）", observed: "p350 原文明确；IMAPS+TLS 默认与改档重启 imap4fed（p351）一致"}
  V3: {passed: true, expected_benefit: "邮件收信体验的落地路径；证据归并 c21/p31/n24"}
  decision: verified

- id: f23
  title: 通知体系结构——SMTP/SMS 两条链与配置分层
  type: framework
  V1: {passed: true, reason: "p353-378 讲义 + How-To 两链完整"}
  V2: {passed: true, check_mode: walkthrough, input: "OT 内置 SMTP 吗", expected: "无，走外部无认证无 TLS 服务器", observed: "p360 原文明确；唯一 SMS 网关（p363）与 VPIM 路由（p370-371）自洽"}
  V3: {passed: true, expected_benefit: "通知体验的约束面；证据归并 c22/p32/p33/n25/n26"}
  decision: verified

- id: f24
  title: 通用公告机制——播放时机三选、两种录制、TUI 菜单与 wav 落地
  type: framework
  V1: {passed: true, reason: "p379-396 讲义 + How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "wav 路径以哪页为准", expected: "书内两处表述不一致", observed: "p392 与 p396 并存（n27），转 needs-review nr-01，生产以实测系统目录为准"}
  V3: {passed: true, expected_benefit: "公告功能的硬限制面；证据归并 c23/p34/n27"}
  decision: verified

- id: f25
  title: 证书三路线与两条 PKI 流程——security OFF / 自签 / 外部 CA（PKCS7、PKCS12）
  type: framework
  V1: {passed: true, reason: "p397-429 三路线 + 两个 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "导入证书后为什么没生效", expected: "漏了 Deploy（导入与部署两步）", observed: "p423 原文明确；Deploy 后断会话属正常（p423/p429）与 n28 一致"}
  V3: {passed: true, expected_benefit: "安全与远程接入前提；证据归并 c24/c25/n07/n28/n29"}
  decision: verified

- id: f26
  title: OTC PC 客户端交付结构——安装包/两模式、软电话两路线、多终端五设备规则
  type: framework
  V1: {passed: true, reason: "p430-493 讲义 + 两个 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "One 模式能不能接电话", expected: "不能，仅盲通话可挂断", observed: "p448/p455 边界与 p37 一致；Desktop/Nomadic 互斥（p474/p492）与 n30 一致"}
  V3: {passed: true, expected_benefit: "最终用户体验的交付面；证据归并 c26/c27/p36/p37/n30/n31/n34"}
  decision: verified

- id: f27
  title: 监督组结构——角色/模式/边界与 8770+OXE 前缀配置
  type: framework
  V1: {passed: true, reason: "p494-513 讲义 + How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "组成员能不能跨 OXE 节点", expected: "可以，但必须同一 OT 节点", observed: "p500 原文明确；500 组/40 人/4000-6000 监督链与 p38 逐格一致"}
  V3: {passed: true, expected_benefit: "话务监督场景的设计与边界；证据归并 c28/p38/n32/n33"}
  decision: verified

- id: f28
  title: 运维工具三通道 + 备份体系 + rehosting 矩阵
  type: framework
  V1: {passed: true, reason: "p514-578 讲义 + 两个 How-To，附录 p579-602 TC2149 全文"}
  V2: {passed: true, check_mode: walkthrough, input: "rehosting 配错能回退吗", expected: "不能，死锁且 inactive 分区被清", observed: "p565/p566 原文明确；OXE/8770/OMS 不被触达（p567）与 n36 一致"}
  V3: {passed: true, expected_benefit: "售后日常与搬迁改名的闭环；证据归并 c29/c30/p39-p42/n22/n35-n39"}
  decision: verified
```

## 断言级裁决记录

1. **counter-example 提取器"通用公告 wav 目录两处表述不一致"**：成立（n27）——p392 写 /var/data/general_announcement、p396 写 /var/data/ics-group/general_announcement；两页引文已并列核对，转 needs-review nr-01，能力卡按"两处并列 + 生产以实测系统目录为准"处理。
2. **counter-example 提取器"书内笔误/排版清单"**：成立（n41）——IP 总表 192.16.8.1.x（与他页 192.168.1.x 矛盾）、远程接入 https 端口 413（图中为 443）、MOFIFICATION/APLLIED/OUTLLOK/EMBBEDED/notifiy/sesseion/possibile 等拼写错误；转 needs-review nr-02，引用时修正口径并注明原文如此。
3. **counter-example 提取器"工具示例输出历史值易误当现网值"**：成立（n42）——checkLicensing/ams.log/checkdns 等示例中的 151.1.1.x、172.25.x 与 2012-2016 时间戳为文档撰写期演示值，非 RLAB 拓扑（192.168.1.x）；转 needs-review nr-03。
4. **principle/case 提取器"实验口径标注"**：一致执行——p43/p44 等条目的 IP、口令、号码全部显式标注"实验口径"；能力卡中环境值仅进 Boundary 与 book/overview.md。
5. **无 rejected 断言**：关键数字逐格核对一致——5000 用户上限、ESXi 6.5/7.0.x 与 Hyper-V 2016/2019、SOT Template Factory 8CPU/16GB/500GB、端口 2570/5260/5040/27000/161/162/4448、号段 31000-31499、语音邮件 31200、会议 31250/31260、IMAP 1000/20000 会话、公告一条与 5 分钟封顶、多终端 5 设备（REX/DECT 各 1）、监督组 500 组/40 人/监督链 4000（500-1500 用户）与 6000（3000-5000 用户）、自动备份 00:01（周日全量）、rehosting 约 25 分钟——均与原文页码对应。
