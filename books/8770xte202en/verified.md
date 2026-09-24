# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f30（主验证对象）；principle p01-p40 / case c01-c17 / counter-example n01-n50 作为各单元的证据素材归并；glossary g01-g52 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-23），基于 565 页全文通读 + 提取器页码证据交叉核对（65535/4 从机/7 天/节点号公式/ISDN 公式已回源抽查）

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 26 | f01, f02, f03, f05, f07, f10-f26, f27-f30（详见下表） |
| reference | 4 | f04（虚拟化部署形态）、f06（四套件 15 应用菜单图）、f08（RLAB 平台结构）、f09（ITSP1 SIP 模拟器）——背景/实验专用，仅作 Boundary 与 book/overview 素材 |
| needs_review | 0（单元级） | 断言级 3 处书内勘误 + 2 处口径出入 + 3 项生产风险转 needs-review.md（nr-01~nr-08） |
| rejected | 0 | 无编造断言；复制数字表（65535/1-65534/4 从/5 副本/7 天）、保密矩阵十档、GlobalParameters 500 条等与原文逐格一致 |

verified 明细：f01, f02, f03, f05, f07, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30

## 验证记录

```yaml
- id: f01
  title: 全书课程推进主线——总览/环境 → 目录核心概念 → 接入/使用/定制/管道/运营五大层
  type: flow
  V1: {passed: true, reason: "p4 目录结构页 + p59-60 等 LESSON SUMMARY 逐章给出；十二段推进与 17 个 How-To 配对完整"}
  V2: {passed: true, check_mode: walkthrough, input: "新项目按什么顺序交付 8770 目录功能", expected: "给出可执行的概念与施工顺序", observed: "概念地基(f10-f15)→接入(f14/c01)→使用(f17-f19)→定制(f22/f23)→管道(f24/f30)→运营(f27-f29)顺序无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线；证据归并 c01-c17 排布"}
  decision: verified

- id: f02
  title: 8770 网络拓扑四角色（服务器/厚客户端/WBM/Web 目录客户端）
  type: diagram
  V1: {passed: true, reason: "p6 四角色定义完整，Web Directory 'Anonymous access allowed' 原文明示"}
  V2: {passed: true, check_mode: walkthrough, input: "目录查询入口为什么需要保密级别机制", expected: "唯一开放匿名的入口决定保密必要性", observed: "p6 匿名访问 + p209 四级保密互证，行为闭环（c06 实测）一致"}
  V3: {passed: true, expected_benefit: "保密与权限体系（task-12）的架构前提"}
  decision: verified

- id: f03
  title: 8770 服务器架构——MariaDB+LDAP 双存储与多协议北向
  type: diagram
  V1: {passed: true, reason: "p7 架构图单处完整，协议清单齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "目录数据从 PCX 到公司目录怎么流", expected: "配置目录(o=nmc)与公司目录(o=directoryroot)两棵树靠链接缝合", observed: "p7 架构与 p67 DN 双格式（f12）互证"}
  V3: {passed: true, expected_benefit: "排障与过滤器编写的概念底座；证据归并 p04/g47"}
  decision: verified

- id: f05
  title: 跨版本兼容矩阵（8770 R4.2-R5.2 × OT/OXE/OXO）
  type: structure
  V1: {passed: true, reason: "p9 矩阵逐行给出，四列版本口径清晰"}
  V2: {passed: true, check_mode: walkthrough, input: "OXE Purple R101.2 (N5) 能配 8770 R5.1 吗", expected: "不能，仅 R5.2", observed: "p9 该行仅 R5.2 列有 X；与 n43 升级陷阱一致"}
  V3: {passed: true, expected_benefit: "交付/升级前的硬核查表；证据归并 p02/n43"}
  decision: verified

- id: f07
  title: 8770 WBM 客户端四应用与边界（Users/Configuration/Performance/Manage My Phone）
  type: structure
  V1: {passed: true, reason: "p34-38 逐应用定义；Unified Management 许可门槛明确"}
  V2: {passed: true, check_mode: walkthrough, input: "WBM 里能改 OXE 节点声明吗", expected: "不能——网络/子网/节点只能在厚客户端管理", observed: "p36 'Connection to one OXE node at a time / No direct access via SSH/Telnet' 支持"}
  V3: {passed: true, expected_benefit: "task-09 WBM 改名路径与 task-21 定制视图入口的认知前提"}
  decision: verified

- id: f10
  title: 目录树结构——Organization/Termination 两类条目与 LDAP 层级模板
  type: structure
  V1: {passed: true, reason: "p62-63 树结构完整；p436 LDAP 键含义与 DN 模板"}
  V2: {passed: true, check_mode: walkthrough, input: "人员在树上怎么挂、DN 长什么样", expected: "o/c/l/ou 任意层级挂 uid 叶子", observed: "p436 五条 DN 例子逐层给出；与 p04 DN 规则一致"}
  V3: {passed: true, expected_benefit: "task-02 建树与 task-20 域切割（DN 范围）的公共地基；证据归并 g01/g02/p04"}
  decision: verified

- id: f11
  title: 目录条目与配置应用条目的链接关系（六类 PCX items）
  type: diagram
  V1: {passed: true, reason: "p64-65 六类可链接条目逐一列出"}
  V2: {passed: true, check_mode: walkthrough, input: "Click to Call 从哪取号", expected: "目录条目经链接取配置侧用户分机", observed: "p64 User 链接 + p69 主链接定义互证"}
  V3: {passed: true, expected_benefit: "两棵树缝合点的模型依据；证据归并 f13/f19"}
  decision: verified

- id: f12
  title: UID 与 DN 双标识体系（业务 key vs 位置路径）
  type: structure
  V1: {passed: true, reason: "p66 UID 规则 + p67 双侧 DN 实例完整"}
  V2: {passed: true, check_mode: walkthrough, input: "同名人员怎么在目录里区分", expected: "UID 默认名+姓、撞名拒建，可改构造", observed: "p66/p74 与 p118-121 实验（c02 步 11）行为闭环一致"}
  V3: {passed: true, expected_benefit: "task-04 UID 构造与排障过滤器编写的直接依据；证据归并 p03/n02/n03"}
  decision: verified

- id: f13
  title: 六类人员-用户链接体系与基数规则
  type: structure
  V1: {passed: true, reason: "p69-72 六类链接基数与匹配条件逐类给出"}
  V2: {passed: true, check_mode: walkthrough, input: "DECT 副机建哪种链、CC 谁说了算", expected: "Secondary link，CC 继承主链接", observed: "p70 定义 + p130 实验注（DECT Dupont CC 变 MKT）一致"}
  V3: {passed: true, expected_benefit: "task-06 链接管理的核心语义；证据归并 p05/g05-g09/p39/n09"}
  decision: verified

- id: f14
  title: 主链接自动创建机制——事件驱动链与告警
  type: flow
  V1: {passed: true, reason: "p74-76 机制四步 + p107-109 How-To 前提齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "PCX 建了用户目录没出人，先查什么", expected: "Process directory + Permanent IP connectivity + 三开关 + UID 撞名按序查", observed: "p107 前提 + p105 三开关 + p118 告警样例与 n46 排障清单一致"}
  V3: {passed: true, expected_benefit: "task-02/03 供给通道与排障抓手；证据归并 p38/c02/n46"}
  decision: verified

- id: f15
  title: 数据更新方向表——链接类型 × 属性 × 同步方向
  type: diagram
  V1: {passed: true, reason: "p79 方向表 + p81-84 四个示例完整"}
  V2: {passed: true, check_mode: walkthrough, input: "PCX 侧改主链接用户姓名会怎样", expected: "主链接断裂、生成新人", observed: "p79 方向规则 + p145 实验结果（n05）一致"}
  V3: {passed: true, expected_benefit: "task-07/08 改名入口决策的总纲；证据归并 p06/p39/n05-n09"}
  decision: verified

- id: f16
  title: LDIF 导入导出体系——三范围 × 两目的地 + 调度
  type: flow
  V1: {passed: true, reason: "p85-86 语义 + p156-169 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "误删分支怎么恢复", expected: "事先 Branch 导出，Import > Add and modify 导回", observed: "p163 Branch 最完整 + p168 导入口径 + c04 步 5 行为闭环"}
  V3: {passed: true, expected_benefit: "task-10 备份恢复与复制/定制回退的公共依赖；证据归并 p09/p10/c04/n41"}
  decision: verified

- id: f17
  title: Web 目录客户端页面结构与两级访问模型
  type: structure
  V1: {passed: true, reason: "p173-181 五区页面 + 两级访问定义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "员工能自己改工位电话和照片吗", expected: "UID 认证后可改本人记录与地址簿", observed: "p178 认证权限 + p194 实验（c05 步 6-8）一致"}
  V3: {passed: true, expected_benefit: "task-11 自助维护与 task-14 拨号入口；证据归并 c05/g13"}
  decision: verified

- id: f18
  title: 保密级别 × 访问级别双矩阵
  type: structure
  V1: {passed: true, reason: "p209-215 四级保密 + 五种个人数据 + 两应用各五档完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Orange 人员登录能看到别人的 Orange 条目吗", expected: "不能——只见 Green + 本人", observed: "p211-212 行为矩阵 + p239-251 七类会话实测（c06）逐档一致"}
  V3: {passed: true, expected_benefit: "task-12 方案设计正交性判断；证据归并 p11/p12/c06/g11-g13"}
  decision: verified

- id: f19
  title: Click to Call 端到端调用链五环
  type: flow
  V1: {passed: true, reason: "p181 原理六步 + p254-256 讲义 + p269-284 How-To 齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "点了号码话机不响，链路哪断了", expected: "按 DDI→ISDN 构造→前缀规则→属性关联→STAP 顺序排查", observed: "五环模型与 p283 粗体判据 + c08 步骤闭环一致"}
  V3: {passed: true, expected_benefit: "task-14 交付与排障主线；证据归并 p15/p17/c08/n10-n14"}
  decision: verified

- id: f20
  title: ISDN 号码构造规则（公式 + DDI/非 DDI 分支 + 个人呼叫号码）
  type: structure
  V1: {passed: true, reason: "p258-259 公式与九行示例表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "人员 ISDN 号没生成，怎么查", expected: "按安装号→DDI 翻译器→补充号顺序排查，前缀最后加", observed: "p258 三条失败分支与 n12 排查序一致；公式回源抽查一致"}
  V3: {passed: true, expected_benefit: "task-14 取号排障与 DDI 方案设计；证据归并 p13/p14/p18/n11/n12"}
  decision: verified

- id: f21
  title: 前缀规则三类型与创建层级选择
  type: structure
  V1: {passed: true, reason: "p261-263 类型与参数 + p276-284 How-To 齐备"}
  V2: {passed: true, check_mode: walkthrough, input: "全网规则建在哪层、PCX 已有 ARS 怎么配", expected: "全网建 Network 层；有 ARS 单规则删空加 0", observed: "p276 层级原则 + p284 Add-On 原文直接回答"}
  V3: {passed: true, expected_benefit: "task-14 号码改写方案；证据归并 p16/n14"}
  decision: verified

- id: f22
  title: 词典定制机制——dict 文件体系与保存三动作
  type: flow
  V1: {passed: true, reason: "p287-293 讲义 + p295-310 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "保存后客户端怎么拿到新词典", expected: "版本号自增，客户端连接时校验并下载 dict_user.zip", observed: "p302 三动作 + p310 下载机制 + c09 步 6 行为闭环一致"}
  V3: {passed: true, expected_benefit: "task-15 本地化交付；证据归并 p19/p20/c09/n15-n17"}
  decision: verified

- id: f23
  title: Web 目录客户端定制三层模型（默认参数/用户参数/主题）
  type: structure
  V1: {passed: true, reason: "p311-322 讲义 + p324-348 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "用户说个性化设置换台机器就丢了", expected: "用户主题存 cookie、未定制者回落默认配置", observed: "p322/p346 回落规则（n20）与 c10 步 8 一致"}
  V3: {passed: true, expected_benefit: "task-16 交付观感与验收口径；证据归并 p21/p22/c10/n18-n20"}
  decision: verified

- id: f24
  title: MSAD 集成三层结构（Access info / 映射+规则 / 插件）
  type: structure
  V1: {passed: true, reason: "p351-359 讲义 + p368-393 两个 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "两家部门各有 AD，能同时同步吗", expected: "可声明多台 AD 服务器", observed: "p354 'multiple Active Directory servers' 原文支持"}
  V3: {passed: true, expected_benefit: "task-17/18 企业身份管道主通道；证据归并 p23-p27/c11/c12/n21-n25"}
  decision: verified

- id: f25
  title: Azure AD (Microsoft Entra ID) 同步四步框架
  type: flow
  V1: {passed: true, reason: "p360-361 四步与差异点原文完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户问 Azure AD 同步和 MSAD 有啥不一样", expected: "主节点恒为 Azure AD、Graph API 认证、不 provision OXE 用户", observed: "p360 原文五差异齐备；与 MSAD 章（f24）口径互证"}
  V3: {passed: true, expected_benefit: "云目录方案选型；证据归并 g26/g49"}
  decision: verified

- id: f26
  title: MSAD 插件部署与调用链（properties 生成→AD 安装→右键开户）
  type: flow
  V1: {passed: true, reason: "p363-366 讲义 + p394-426 How-To 全链路"}
  V2: {passed: true, check_mode: walkthrough, input: "插件界面缺字段怎么排查", expected: "先查 IE 信任站点/活动内容/active scripting 三项而非重装", observed: "p414 三前提与 n26 一致；IE 依赖已作生产风险登记（nr-06）"}
  V3: {passed: true, expected_benefit: "task-19 帮助台开户通道；证据归并 p28/c13/n26-n28"}
  decision: verified

- id: f27
  title: 管理域模型——域=目录级别集合×管理员组
  type: structure
  V1: {passed: true, reason: "p429-450 讲义完整（域定义/嵌套/许可/激活）"}
  V2: {passed: true, check_mode: walkthrough, input: "本地管理员为什么建不了域", expected: "Domain configuration 菜单显示但 inactive，建域是全局管理员的事", observed: "p472 三处可见性注（n31）与 c14 步 8 一致"}
  V3: {passed: true, expected_benefit: "task-20 多组织运营；证据归并 p29/p30/p31/c14/n30-n33"}
  decision: verified

- id: f28
  title: 本地管理员三预定义组与权限档
  type: structure
  V1: {passed: true, reason: "p441 三组权限档 + p444-450/p462-466 How-To"}
  V2: {passed: true, check_mode: walkthrough, input: "哪一组能替客户再建本地管理员", expected: "Users & Customization Configuration + Delegation 开关", observed: "p441/p450 原文 + c15 步 1-5 行为闭环；p441 与 p463 表述出入已登记（nr-05）"}
  V3: {passed: true, expected_benefit: "task-20/21 权限下发设计；证据归并 g29/g20/c14/c15"}
  decision: verified

- id: f29
  title: 目录复制架构——Master/Consumer/Referral/Agreement 四件套
  type: diagram
  V1: {passed: true, reason: "p501-515 讲义 + p517-535 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "从机上改的人员为什么第二天没了", expected: "Consumer 本地改动在复制后被覆盖，管理必须收口 Master", observed: "p507 大写警告（n36）与 p533 复制过程验证（c16 步 12）一致"}
  V3: {passed: true, expected_benefit: "task-22 冗余方案与运营纪律；证据归并 p32-p34/c16/n34-n39/n49"}
  decision: verified

- id: f30
  title: LDIF 管理工具管道——六个命令行工具与 conf 文件范式
  type: flow
  V1: {passed: true, reason: "p536-550 讲义 + p552-558 实验任务书完整"}
  V2: {passed: true, check_mode: walkthrough, input: "外部目录删了人，8770 怎么跟删", expected: "misc10 时间戳标记 + purgefilter + purge.bat", observed: "p547 工具用途 + p557 实验（c17 步 7）行为闭环一致"}
  V3: {passed: true, expected_benefit: "task-23 批量数据工程；证据归并 p35/p36/c17/n40/n41"}
  decision: verified
```

## 断言级裁决记录

1. **counter-example 提取器"p95 节点号公式示例自相矛盾"**：成立。公式"network*100+node number"按 1*100+2 应得 102，书例写 101；实验实配网络 1/节点 1 亦得 101。按"百位=网络号、末两位=节点号"理解（推断），已登记 needs-review nr-01。
2. **counter-example 提取器"p120 第二个用户 UID 描述不符"**：成立并如实记录（n04）——Notes 写 "Thomas Anderson 31024"，按实验逻辑应为 31023，与前文自相矛盾；登记 nr-02。
3. **counter-example 提取器"p330 字段说明串行"**：成立并如实记录（n19）——"Display define associated station icon" 行说明文字写成隐藏 Browse 页签，按 p328 字段定义应为隐藏 Define associated station 图标；登记 nr-03。
4. **principle 提取器"词典路径两处口径"**：成立。讲义 C:\8770\dict 与 How-To C:\8770\Client\dict 并存，操作以 How-To 为准（p19/n17）；登记 nr-04。
5. **framework 提取器"三组权限档表述出入"**：成立。讲义 p441 Users Configuration 的 Users 权限为 All/Users，实验 p463 写 Write/Users；以现场实测为准（f28/nr-05）。
6. **无 rejected 断言**：复制数字表（65535、1-65534、4 从、5 副本、7 天）、保密十档、500 条地址簿上限、ISDN 公式、节点号公式文本均与原文逐格一致；三处书内排版勘误均不影响操作步骤本身。
