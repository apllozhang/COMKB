# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f25（主验证对象）；principle p01-p45 / case c01-c27 / counter-example n01-n53 作为各单元的证据素材归并；glossary g01-g60 转 GLOSSARY（落位见 references.md）
> 验证人: 主会话（2026-09-23），基于 705 页全文通读 + 提取器页码证据与 source_fulltext.txt 逐格交叉核对（节点号公式 p123/p658、报告上限 p444、purge 默认值 p489-493、许可锁 p601-608、硬件双档 p55-56 等均复核一致）

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 24 | f01, f03-f25（详见验证记录） |
| reference | 1 | f02（RLAB 实验平台结构——教学专用基础设施，落位 book/overview 环境区，不作能力） |
| needs_review | 0（单元级） | 断言级 4 项转 needs-review.md（2019 章沿用旧版口径、OXO 章法语残句、客户端空间表述混写、缩写未展开） |
| rejected | 0 | 无编造断言；关键数字与原文逐格核对一致 |

verified 明细：f01, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——装平台 → 接节点 → 管用户/告警 → 增值域 → 兜底维护
  type: flow
  V1: {passed: true, reason: "p4 课程步骤总览 + p65 起各 How-To 配对完整"}
  V2: {passed: true, check_mode: walkthrough, input: "新交付项目按什么顺序推进", expected: "给出可执行阶段顺序", observed: "七段推进与各 How-To 章序互证，装机先于接节点、接节点先于开通/告警，无矛盾"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线，避免节点未声明先建用户的倒置"}
  decision: verified

- id: f03
  title: OmniVista 8770 总体架构一张图——客户端/服务器/被管节点协议关系
  type: diagram
  V1: {passed: true, reason: "p6-7 架构图单处完整；p139 补协议分工"}
  V2: {passed: true, check_mode: walkthrough, input: "配置数据和告警各走什么通道", expected: "配置 CMISE、数据提取 FTP/SSH、告警 CMISE/Corba", observed: "p139/p272 与架构图一致"}
  V3: {passed: true, expected_benefit: "方案沟通与排障分流（配置面/告警面/数据面）的底图"}
  decision: verified

- id: f04
  title: 应用套件全景——四大套件 + WBM 客户端的功能分区
  type: structure
  V1: {passed: true, reason: "p10 四套件应用清单完整；p34-38 WBM 四应用"}
  V2: {passed: true, check_mode: walkthrough, input: "节点声明/用户开通/报表各在哪个应用", expected: "Network 套件 Configuration/Users、Reporting 套件 Reports", observed: "p10 清单与后续 How-To 章一一对应"}
  V3: {passed: true, expected_benefit: "菜单导航总地图；证据归并 p01/n06"}
  decision: verified

- id: f05
  title: 服务器安装流程七步链——系统配置 → 必装组件 → 8770 安装 → 补丁
  type: flow
  V1: {passed: true, reason: "p57 步骤总览 + p60-61 安装两步 + p78 补丁 + p80-83 Windows 前置"}
  V2: {passed: true, check_mode: walkthrough, input: "从裸 Windows 到可登录 8770 走一遍", expected: "七个环节顺序无缺口", observed: "c01 全程走通（p65-88），Patch_Installer.log 成功判据与首连改密闭环"}
  V3: {passed: true, expected_benefit: "task-01/02 主链；证据归并 c01/c02/p04-p07/n07-n11"}
  decision: verified

- id: f06
  title: 客户端安装双通道与首次连接参数
  type: flow
  V1: {passed: true, reason: "p94 双通道定义 + p96-106 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "Win11 客户端装完打不开查什么", expected: "WMIC 缺失（build 22572 起）", observed: "p104 附录明确 WMIC 可选功能装回；p102 Zulu 防火墙放行闭环"}
  V3: {passed: true, expected_benefit: "管理员日常工作入口的施工与排障；证据归并 c03/p08/n12-n14"}
  decision: verified

- id: f07
  title: Configuration 应用配置树——Network > Subnetwork > PCX 三级声明模型
  type: structure
  V1: {passed: true, reason: "p111 配置树 + p121-123 三级声明参数页完整"}
  V2: {passed: true, check_mode: walkthrough, input: "声明一台 OXE 要填哪些页", expected: "PCX/Software download/Connectivity 三页参数", observed: "p123/p124 参数页与 c04 实验一致"}
  V3: {passed: true, expected_benefit: "被管对象接入的声明模型；证据归并 p09/c04/c11"}
  decision: verified

- id: f08
  title: OXE 节点注册端到端流程——前置核查 → 声明 → 同步 → 实时核验 → 排障
  type: flow
  V1: {passed: true, reason: "p118-128 How-To 五段完整（siteid/声明/同步/31234 核验/Service Manager 排障）"}
  V2: {passed: true, check_mode: walkthrough, input: "实时同步失效怎么办", expected: "重启 NMC Alarm server 后重测", observed: "p128 原文直接回答；p127 日志判据（NMCSyncLdapPbx/NMCFaultManager）齐备"}
  V3: {passed: true, expected_benefit: "被管对象接入第一关口的施工与排障抓手；证据归并 c04/p10/p11/n20"}
  decision: verified

- id: f09
  title: OXE SSH 安全链路——netadmin 可信主机 + MindTerm 密钥 + SFTP
  type: flow
  V1: {passed: true, reason: "p129-136 How-To 完整（netstat 核查/可信主机清单/MindTerm 首连/加可信主机）"}
  V2: {passed: true, check_mode: walkthrough, input: "新装的 8770 连不上 OXE 22 端口", expected: "OXE 侧可信主机未含 8770，netadmin 加可信主机后 Apply", observed: "p131/p136 菜单路径与 p132 telnet 被拒判据支持该排障"}
  V3: {passed: true, expected_benefit: "OXE N3 起强制的安全基线施工；证据归并 c05/p12/p13"}
  decision: verified

- id: f10
  title: OXO Connect 纳管流程——布线核查 → OMC 安装连接 → 声明 → 同步 → 在线/离线
  type: flow
  V1: {passed: true, reason: "p640-667 How-To 五段完整"}
  V2: {passed: true, check_mode: walkthrough, input: "声明节点 80 后备份放哪里", expected: "按 (子网号×100)+80=180 换算落盘 C:\\8770_ARC\\OXO\\data\\1\\1\\180", observed: "p658 原文逐字一致；p659 共享目录参数错误需重启服务器"}
  V3: {passed: true, expected_benefit: "OXO 现场标配的纳管闭环；证据归并 c11/p43/n46/n47/n53"}
  decision: verified

- id: f11
  title: OXE 用户开通三层模型——Directory 条目 / Profile / Meta profile / Key profile
  type: structure
  V1: {passed: true, reason: "p170-181 用户模型 + p196-210 Meta profile 讲义完整"}
  V2: {passed: true, check_mode: walkthrough, input: "建户只填姓名就能自动取号吗", expected: "Meta profile 绑号段后可，取段内首个空闲号", observed: "p204/p207 原文支持；p205 Warning 号段建后必须同步"}
  V3: {passed: true, expected_benefit: "高频开通场景的模型底座；证据归并 c07/c08/p14/p15"}
  decision: verified

- id: f12
  title: 批量开通文件语义——导出四法、字段占位与导入核验
  type: flow
  V1: {passed: true, reason: "p211-224 讲义+How-To 完整；p246-252 WBM 批量"}
  V2: {passed: true, check_mode: walkthrough, input: "模板里 XXXX 与 NULL 各是什么意思", expected: "XXXX=必填人工填、NULL=系统自动", observed: "p216 原文逐字一致；thick client 与 WBM 文件互不通用（p250）"}
  V3: {passed: true, expected_benefit: "迁移/开局大批量场景的标准动作；证据归并 c09/c10/p16/p17/n15/n16/n18"}
  decision: verified

- id: f13
  title: Alarms 应用架构与处置状态机——采集链 + 六级色标 + 相关/非相关分流
  type: diagram
  V1: {passed: true, reason: "p269-282 讲义完整（架构图/色标表/相关非相关定义）"}
  V2: {passed: true, check_mode: walkthrough, input: "确认过的告警算处理完吗", expected: "不算——acknowledge 后仍活动，只有非相关告警可 clear", observed: "p277-279 原文支持（n19 两误区齐备）"}
  V3: {passed: true, expected_benefit: "值班处置流程的设计依据；证据归并 p19/n19/n34"}
  decision: verified

- id: f14
  title: OXE 告警接入流程——incident manager 参数 + incident filter + rstcpl 验证
  type: flow
  V1: {passed: true, reason: "p283-289 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "怎么验证告警真的上来了", expected: "rstcpl 重启 coupler 触发 #2042，incvisu -t 查事件，Alarms 上屏 Major", observed: "p285-286 实验闭环一致；#1125 定向过滤 p287-288"}
  V3: {passed: true, expected_benefit: "告警集中的第一步施工与验证；证据归并 c12/p20/n20"}
  decision: verified

- id: f15
  title: SNMP Proxy 部署链——Windows SNMP 服务 → ToolsOmniVista 启用 → hypervisor 声明 → PCX 激活 → 过滤
  type: flow
  V1: {passed: true, reason: "p307-324 How-To 五步完整"}
  V2: {passed: true, check_mode: walkthrough, input: "启用 8770 代理后 Windows SNMP 服务还在吗", expected: "被自动停用但功能不能卸载（Netsnmp 归属）", observed: "p308/p315/p317 原文支持（n21）"}
  V3: {passed: true, expected_benefit: "与外部网管集成的标准路径；证据归并 c14/p22/n21"}
  decision: verified

- id: f16
  title: Topology 双视图体系——Standard 自动视图 + Custom 编辑器 + 告警重定向
  type: structure
  V1: {passed: true, reason: "p325-362 讲义+两个 How-To 完整"}
  V2: {passed: true, check_mode: walkthrough, input: "自定义背景图下拉里没有", expected: "gif 放 8770\\data\\topology\\maps 后须重启 NMC Service Manager", observed: "p337 原文明确（n24）；p335/p336 另两处改后重启（n23）"}
  V3: {passed: true, expected_benefit: "客户定制监控大屏的施工链；证据归并 c15/c16/n22-n24"}
  decision: verified

- id: f17
  title: Security 三层权限模型——8770 账户/组 → OXE Access Profile → OXE 侧访问控制
  type: structure
  V1: {passed: true, reason: "p363-412 讲义+How-To 完整（密码策略/组/单登录/Access Profiles/User Access Control）"}
  V2: {passed: true, check_mode: walkthrough, input: "账户在多组权限怎么算", expected: "按应用取最高访问级", observed: "p398 原文支持（n27 变相提权提醒）"}
  V3: {passed: true, expected_benefit: "合规权限体系的设计与审计口径；证据归并 c17/p30-p35/n25-n31"}
  decision: verified

- id: f18
  title: Scheduler 任务模型——Job/Task 状态机与两种组装方式
  type: structure
  V1: {passed: true, reason: "p460-487 讲义+How-To 完整（Simple job/Synchronized task/jobset）"}
  V2: {passed: true, check_mode: walkthrough, input: "周六任务周五关机周一开机还跑吗", expected: "超过 Maximum start delay 即放弃", observed: "p473 原文示例逐字一致（n37）"}
  V3: {passed: true, expected_benefit: "自动化任务链的参数语义依据；证据归并 c20/p24/n37/n38"}
  decision: verified

- id: f19
  title: 自动维护体系——五类数据清除参数 + Purge job 组装 + 预定义 job 恢复
  type: flow
  V1: {passed: true, reason: "p488-502 How-To 完整（五入口/LDIF 恢复）"}
  V2: {passed: true, check_mode: walkthrough, input: "预定义 Weekly Job 改坏了怎么救", expected: "DailyJob/WeeklyJob.ldif 导入 + 重启 NMC Scheduler", observed: "p502 原文直接回答（n38）"}
  V3: {passed: true, expected_benefit: "长期运行防数据库膨胀的清理体系；证据归并 c21/p25/n38"}
  decision: verified

- id: f20
  title: 8770 备份恢复与 rehosting 流程——备份四块内容 + 版本绑定 + 换机改址
  type: flow
  V1: {passed: true, reason: "p503-521 讲义+How-To 完整（四块内容/nmcVersion/三场景）"}
  V2: {passed: true, check_mode: walkthrough, input: "5.1 的备份能还原到 5.2 服务器吗", expected: "不能——备份专用版本，nmcVersion 决定", observed: "p510/p519 原文支持（n39）"}
  V3: {passed: true, expected_benefit: "灾难恢复底线的规划依据；证据归并 c22/p26/p27/n39"}
  decision: verified

- id: f21
  title: NMC 服务体系——Windows 服务层 + Service Manager 监督层 + 日志滚动
  type: structure
  V1: {passed: true, reason: "p539-553 讲义完整（两层次/依赖规则/日志 2x5MB/nmclog）"}
  V2: {passed: true, check_mode: walkthrough, input: "被监督服务停了要手动 Start 吗", expected: "不要——监督下自动重启，手动 Start 反而冲突", observed: "p561 原文明确（n41）"}
  V3: {passed: true, expected_benefit: "二线排障的服务模型依据；证据归并 c24/p29/n40/n41"}
  decision: verified

- id: f22
  title: OXE 备份恢复机制——bck 命令 + FTP/SFTP 取回 + swinst 恢复五步
  type: flow
  V1: {passed: true, reason: "p568-593 讲义+How-To 完整（N2/N3 凭据口径/恢复菜单链）"}
  V2: {passed: true, check_mode: walkthrough, input: "恢复会话断开了连不回去", expected: "停电话后 role address 失效，用物理 IP 重连", observed: "p589 原文逐字支持（n43）"}
  V3: {passed: true, expected_benefit: "通话系统灾备底线；证据归并 c25/p41/p42/n43"}
  decision: verified

- id: f23
  title: 8770 许可体系——ACTIS 出证 → 四道锁 → License Server 核验 → 受限模式
  type: structure
  V1: {passed: true, reason: "p594-617 讲义+How-To 完整（文件结构/锁表/控制双法/更新流程）"}
  V2: {passed: true, check_mode: walkthrough, input: "用户超限后应用全没了是不是故障", expected: "受限模式——仅 Directory+Configuration，服务器不停机", observed: "p606 原文支持（n49）"}
  V3: {passed: true, expected_benefit: "扩容续费与超限排障的依据；证据归并 c26/p38/p39/p40/n44/n48/n49"}
  decision: verified

- id: f24
  title: 网络驱动器映射流程——远程共享 + ADM8770 同名账号 + 服务账号注入
  type: flow
  V1: {passed: true, reason: "p668-698 How-To 完整（双侧流程/五项权利/服务账号）"}
  V2: {passed: true, check_mode: walkthrough, input: "备份对话框里看不到网络位置", expected: "先以 ADM8770 登录映射驱动器并给 ExecdEx/SaveRestore 配 Nt account", observed: "p693/p696/p698 流程与验收判据一致"}
  V3: {passed: true, expected_benefit: "报表与备份落网络存储的生产化路径；证据归并 c27/p44"}
  decision: verified

- id: f25
  title: 8770 WBM 客户端入口与四应用分区
  type: structure
  V1: {passed: true, reason: "p151-157 讲义 + p225-260 WBM Users/批量完整"}
  V2: {passed: true, check_mode: walkthrough, input: "WBM 能替代厚客户端吗", expected: "不能——无配置权限/无 SSH 直连/批量文件互不通用", observed: "p36/p153/p250 原文支持（n06/n16）"}
  V3: {passed: true, expected_benefit: "非专家开通界面的边界管理；证据归并 c10/p17"}
  decision: verified
```

## 断言级裁决记录

1. **2019 安装章沿用旧版口径（n45）**：成立。p639 连接信息文件名写 nmc5_5.1.cfg（2022 章为 nmc5_5.2.cfg，p85/p103）、DNS 指向 192.168.1.100（p621，2022 章为 192.168.1.250）、无 WMIC 附录——推断为文档未随版本同步，详见 needs-review nr-01。
2. **OXO 章法语残句（n53）**：成立。p643 "Vérifier que…"、p659 "Renseigner le login/mot de passe…" 为未翻译法语，语义按上下文转述（核对 MAIN@ IP、填 8770 服务器 Windows 会话账号），详见 needs-review nr-02。
3. **客户端空间表述混写（p93）**：原文 "OV8770 client cannot be launched if the space in the memory size is below 750 MB. It's the minimum required memory space to run JVM application"——把磁盘剩余空间写成 memory size，实践口径按"剩余磁盘空间 750MB"理解，详见 needs-review nr-03。
4. **缩写未展开如实省略**：PCX、MAO、UTL 类、TDS/GCS 等书中未给全称（glossary 自检口径），转述时不得补外部全称冒充书内事实（nr-04）。
5. **无 rejected 断言**：节点号公式（p112/p123/p658）、报告上限（p444）、purge 默认值（p489-493）、许可锁表（p601-608）、硬件双档（p55-56）、恢复菜单链（p589-592）等关键数字与原文逐格一致。
