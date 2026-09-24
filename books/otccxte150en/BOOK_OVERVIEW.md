# OmniTouch Contact Center Standard · Advanced Call Routing (OTCCXTE150EN Issue 01) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OmniTouch Contact Center Standard Edition — Advanced Call Routing (ACR) (Participant's Guide)
- **作者**: ALE Training Services
- **出版/发布时间**: Issue 01（OpenTouch Suite for MLE / OXE + OTCC Standard Edition 时代；实验环境含 MS SQL Server 2016、Access 2016、Windows 服务界面）
- **内容类型**: 课程（官方售后培训讲义课程 + 分步实验 How-To；讲义约占 35%、实验约占 65%）
- **版本来源**: `F:\AIwork\ZCode\books\otccxte150en\source_fulltext.txt`（470 页）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义幻灯片 + 分步实验 How-To；每个 How-To 章自带 Implementation 场景、编号步骤、截图级菜单路径与 Debugger 行为验证）

### 一句话主旨
在 OTCC 标准版上用 CCS 内嵌脚本编辑器编写 ACR 脚本（9 种规则 + 内部/外部数据库查询），由 ASM 服务器按呼叫特征（主叫号、Call Tag、直拨坐席号）动态计算坐席列表，实现"把呼叫送给最合适的可用坐席"的高级路由，并覆盖脚本、语音引导、统计与外部化的全链路交付。

### 骨架 (主要论点及其关系)

1. **ACR 引论**（传统配置三痛点 → ACR 脚本 + ASM 架构 → 9 种规则 → 分发三步与动态组 → 呼叫特征 → 容量上限表）
2. **基础 CCD 矩阵搭建**（ACD 前缀、处理组、队列、双 Pilot、规则指南、分发规则、话机、坐席、混合链路、统计 Pilot、域/技能/呼叫档案——后续所有实验的公共地基）
3. **脚本管理**（LCA+ISM 示例脚本、ASM 内存检查、Debugger、asm_ag_free_duration 三值与 LIT/PLTR）
4. **授权/非授权名单规则**（静态名单三索引 + 脚本内显式列表 + LIST 变量；Debugger 实时改条件）
5. **重定向/再分发规则**（空列表兜底两式：转号或退回下一路由方向直至 Blockage）
6. **坐席直拨与 ACR**（Pilot Direct Call、私有号码、DICA 自动技能、CALL_TYPE=DIRECT_CALL 脚本分支）
7. **内部数据库**（主叫号/Call Tag/坐席号三键 × 名字/档案/名单/优先级，4000 条）
8. **呼叫特征生成与传递**（IAA 编码、统计 Pilot、CCivr 三途径；转移时最后 Call Tag/Profile 覆盖前者）
9. **字符串处理 + 多语言语音引导**（五个字符串关键字；40 语种引导与语言偏好 1-7）
10. **综合特性**（IDLE/COM 排序、规则组合 APPLY 语义、IQUEUE、屏幕显示、清空列表、IVR 规则、LIST 变量、CCD/ACR 混合选呼）
11. **过滤器与统计**（≤200 过滤器、AND 语义、Super/Hyper-Filter OR、三个 Excel 模板）
12. **外部化三线**（外部 ASM 单机与双机热备；外部数据库 ODBC/SQL 六构件，Access 与 MS SQL 双实验，存储过程持久化 LCA）

**论点之间的关系**: 层层递进为主——1 是概念地基，2 是全书的公共实验矩阵（后续每个实验都往这张矩阵上加对象），3 是脚本工具链，4-9 是按规则族/特征源并列展开的能力单元，10 把规则组合与高级构件收拢，11 补监控统计，12 是"出 OXE"的外部化延伸（服务器与数据库）。讲义给原理，How-To 在同一矩阵上增量验证。

### 作者要解决的核心问题
让实施/维护工程师摆脱"每个坐席一个组 + 复杂统计 + 外挂应用"的传统 OTCC 标准版做法，掌握用 ACR 脚本按客户特征（回头客找原坐席、技能精确匹配、直拨等原坐席、VIP 优先）智能选坐席的完整交付与排障能力。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| ACR (Advanced Call Routing) | 基于脚本的呼叫路由特性：脚本编辑器嵌在 CCS，脚本挂到 ACR Pilot，由 ASM 服务器执行 | 不是"转发规则集合"，是一套可编程的坐席选择引擎 |
| ASM (Agent Selection Modul) | 按脚本/坐席配置/呼叫档案计算坐席列表的服务器；内部（OXE 上 alb 进程）或外部（Windows PC 服务） | 书中拼写 "Modul"；它只"出列表"，不直接派发呼叫 |
| ACR Pilot | 承载 ACR 脚本的引导号；统计 Pilot 汇入它；一个 Pilot 同时只能激活 1 个脚本 | 与普通 Pilot 的区别：配 Waiting Room、无资源选择优先级 |
| Waiting Room | ACR 专用停放区：不按 FIFO， ASM 返回的动态坐席列表附着其上；与 Waiting Queue 不能同开 | 不是"第二个队列"——它改变了资源选择逻辑（选人由 ASM 接管） |
| Dynamic Group | ASM 按规则算出的坐席列表，呼叫带着它进 Waiting Room | 不是 PBX 里的静态分组，是每次呼叫即时计算的临时组 |
| 9 种 ACR 规则 | ISM（技能映射）、LCA（上次接听者）、Authorized/Unauthorized List、Redirection、Redistribution、Idle、Com、IVR | 分"单用规则"与"可组合规则"两类；IDLE 与 COM 互斥 |
| Call Profile | 呼叫的技能需求清单：≤7 技能 × 级别 1-9 × 强制/可选，语言类另有偏好 1-7 | 是"需求方"——坐席技能是"供给方"，ISM 按成本匹配 |
| Call Tag | 随呼叫走并受 ACR 分发机制操作的字符串（CSTA 关联数据）：可来自统计 Pilot、IAA 编码或 CCivr | 不是"显示备注"——它能当脚本/数据库的索引键 |
| CHARACTERISTICS_LIST | 当前呼叫实际携带的技能特征列表（脚本里最常用的 ISM 输入） | 与 Call Profile 区分：档案是定义，特征列表是呼叫运行时实际值 |
| DICA | 私有号码托管后系统自动分配的技能（Domain: Media / Skill: DirectCall / 缩写 DICA）；停用即不可直拨 | 是个"开关型技能"，不是业务技能 |
| asm_ag_free_duration | parameters.cfg 参数，0=PLTR（登录时段话务比）、1=LIT 单机、2=LIT 组网；最低版本 l2.300.32.a | Idle 规则同名不同义——排序语义取决于这个文件参数 |
| ISM 成本 | ISM 规则按档案算出的匹配代价：其他规则=0，CCd 呼叫=无穷；呼叫选择据此排序 | 越小越优先；这就是 ACR 呼叫插队 CCD 呼叫的机制 |
| ACR Actual Waiting | RSI 系统参数：False=先比 ISM 成本再看实际等待；True=先看实际等待再看成本 | 一个开关改变两种呼叫选择哲学，默认 False |
| adm_acd | OXE 维护命令（`adm_acd <ASM IP> -salb`）：看名单(24)/内部库(25)/呼叫动态数据(28)/链路(11,14)/DB 连接(60,61) | 是 ACR 的"命令行仪表盘"，与 CCS Debugger 互补 |
| SQL 六构件 | 外部库脚本的 6 个 Building Block（连接/请求/结果测试/取数映射/fetch 循环） | ASM 脚本里写的是受限 SQL（SELECT + CALL 存储过程），不是通用 SQL 编程 |

### 核心命题 (用自己的话)

1. ACR 的本质是"脚本选坐席"：CCS 内嵌编辑器写脚本（*.scr 源/*.alb 编译），ASM 服务器解释执行，按呼叫特征返回动态坐席列表——呼叫控制仍在 CCD 矩阵，选人逻辑被脚本接管。
2. ASM 两种部署同一角色：内部=OXE 上的 alb 进程，外部=Windows 服务（需先 asm_on_dhs=0 停内部）；外部版额外能访问外部数据库（要 167 号软件许可）。
3. 分发三步固定：呼叫特征化并关联档案进 Pilot → ASM 算列表（动态组）→ 呼叫带列表进 Waiting Room；资源选择优先级从此不存在，选人全归 ASM。
4. 规则分两族：单用规则（LCA/Redirection/Redistribution/IVR）必须独占 APPLY；可组合规则（Authorized/Unauthorized/ISM/IDLE/COM）可串接；IDLE 与 COM 互斥；一个 APPLY 是链式过滤（前规则输出=后规则输入），两个 APPLY 各自独立（第一个失效）。
5. 呼叫特征是路由原料：CLID、被叫号、Call Tag、呼叫档案（≤7 技能）、呼叫类型；内部数据库（4000 条）用三键（主叫号/Call Tag/直拨坐席号）查出名字、档案、名单、优先级直接喂给脚本。
6. 空列表有两式兜底：Redirection 转一个号码（内部/外部/变量），Redistribution 退回下一路由方向，方向全关则落 Blockage（地址或语音引导）；脚本默认重试 20 次（库中无 Call Tag 时观察到 21 次），最后走 ACR Pilot 封锁模式。
7. 直拨可以"等原坐席"：处理组里把 Pilot Direct Call 指到 ACR Pilot、坐席配私有号后系统自动加 DICA 技能；脚本用 CALL_TYPE=DIRECT_CALL 区分直拨与普通来话，实现"忙时等 3 分钟再转总机"类业务。
8. Call Tag 三来源一规则：统计 Pilot 静态标、IAA 编码输入（≤16 位 CSTA 关联数据）、CCivr TransferCall（需前置 GetPilotInfo）；转移时呼叫上下文中最后一个 Call Tag/Call Profile 覆盖之前所有。
9. 语音引导与选人同源：多语言引导最多 40 语种，语言取呼叫档案（偏好 1-7、1 最高），档案无语言则用 ACR Pilot 语言；坐席只需 1 门档案语言技能即可入选；IQUEUE 构件可在脚本内重写 6 级停放引导 + NEXT 级。
10. 呼叫选择统一排座次：优先级 0-9（0 最高）→ ISM 成本（等待房间：ISM 按档案算/其他规则 0；等待队列=无穷）→ 实际等待时间；ACR Actual Waiting 参数决定成本与等待谁先谁后。
11. 过滤器是统计视角不改路由：≤200 个、每过滤器 ≤7 技能、AND 语义；Super-Filter（同节点）/Hyper-Filter（跨节点）25 对象 OR；实时窗口 + 三个 Excel 模板；新过滤器查不到创建前的历史（预置 20 个兜底）。
12. 外部化三线成熟可复制：外部 ASM 割接四步（停 alb→装服务→建 Site→迁脚本重编译）；双机 Main/Stand-By 自动复制脚本与连接；外部库走 32 位 ODBC，SELECT+存储过程读写，updateCalling 把 LAST_CALLED_AGENT 落库，ASM 重启不丢"上次接听坐席"。

### 论证链
教材以"概念讲义给原理图与语义 → 同一张实验矩阵上增量叠加对象 → How-To 编号步骤落地 → Debugger/adm_acd 截图做行为验证"推进；多个实验故意让学员观察"预期外结果"（如未知 Call Tag 时脚本执行 21 次、Filter 3 无数据、ASM 重启后 LCA 仍生效）用对照行为替代形式化论证；数值边界集中在容量表（p18）、取值域注记与 parameters.cfg 参数页。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 OpenTouch Suite for MLE / OXE 与 OTCC 标准版 Issue 01 界面；CCS/OXE 菜单与截图随版本漂移。
- 数据库生态停在 Access 2016 / SQL Server 2016 / SSMS 17；32 位 ODBC 硬约束在现代 64 位服务器上获取驱动本身就是坑。
- asm_ag_free_duration 最低版本 l2.300.32.a、旧 patchIdle 文件迁移说明（p49）带有明显的版本过渡期痕迹。

### 作者的立场盲点
- 全书默认实验矩阵（3xXXX 编号、讲师提供的 OXE+CCS 环境）已就绪，从零 生产交付的规模规划、话务建模、Erlang 类方法只字未提——容量上限给了，"该买多少"没教。
- 安全话题系统性缺席：sa 密码（Alcatel@1）、数据库账号 Brest/alcatel、ASM 弱凭据直接印在教材；SQL 注入、最小权限、传输加密均未讨论。
- 高可用只覆盖外部 ASM 双机；OXE 侧冗余、数据库备份、脚本版本管理（谁改了脚本、如何回滚）缺位。
- 混合链路（Hybrid Link）仅一页带过，多节点组网的 ACR 细节在书外。

### 未被证明的假设
- 假设读者已完成 CCD 基础课程（CCD09001 文档编号出现在页眉），熟悉 OMF/CCS 基本操作。
- 假设 CCS 安装时已勾选 ASM script 组件（p22 一句带过，出错无排障路径）。
- 假设 32 位 ODBC 驱动、Access/SQL Server 环境现成可用；假设 IAA 只从外部呼叫的约束可接受。

### 最强反对意见
"这是实验手册，不是设计指南"——规则组合语义靠脚本示例暗示（1Apply/2Apply 对照），无工程决策树；容量表只有上限没有测算方法；安全与配置管理（脚本审计、权限、加密）整体缺席。因此每个能力的 Boundary 必须标注"实验口径 + OTCC/OXE 侧配套文档在书外"，数值类条目需注明"原书 Issue 01 版本口径"。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] ACR 概念与架构讲解（ASM 内外部署、分发三步、动态组）
- [x] 基础 CCD 矩阵搭建全流程（前缀→PG→队列→双 Pilot→规则→坐席→混合链路→统计 Pilot→技能档案）
- [x] ACR 脚本编写与调试工具链（编辑器/激活/Debugger/ASM 内存检查）
- [x] 规则族运用（LCA、ISM、授权/非授权名单、重定向、再分发、Idle、Com、IVR）
- [x] 规则组合语义（单用 vs 可组合、APPLY 链式语义、IDLE/COM 互斥）
- [x] LIT/PLTR 排序参数调校（parameters.cfg 三值）
- [x] 坐席直拨与 ACR 融合（Pilot Direct Call/私有号/DICA/CALL_TYPE）
- [x] 内部数据库运营（三键五属性、脚本取用）
- [x] Call Tag 生成与传递（IAA 编码叶、统计 Pilot、CCivr、覆盖规则）
- [x] 字符串处理与主屏显示（五关键字、DISPLAY_AGENT）
- [x] 多语言语音引导与语言偏好分发
- [x] IQUEUE 停放级编程与 Voice Guide 管理
- [x] LIST 变量编程（skill 型/agent 型、加减算子）
- [x] CCD 与 ACR 混合呼叫选择调优（优先级/ISM 成本/ACR Actual Waiting）
- [x] ACR 过滤器与统计报表（实时/Excel 三模板/Super-Hyper Filter）
- [x] 外部 ASM 部署割接与双机热备（asm_on_dhs、Site 链路、防火墙、脚本迁移）
- [x] 外部数据库接入与脚本 SQL（ODBC 32 位、六构件、fetch、存储过程、LCA 落库）

### 不适合 skill 化的内容
- MS SQL Server 2016 安装、SSMS/Profiler 界面点选、Access 建表向导等通用软件操作（p396-400、p408-426、p453-469 的截图步骤，仅保留与 ACR 相关的字段/账号/存储过程约定作 Boundary）
- 实验环境特定编号体系本身（3xXXX 系列值可作示例但不构成能力）
- 纯界面截图浏览页（如 p219 CCs Configuration、p325/326 安装向导截图页）

### 预估 skill 数量
**约 8-10 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 搭建基础 CCD 矩阵（前缀/PG/队列/双 Pilot/规则指南/分发规则/话机/坐席/附件/混合链路/统计 Pilot/域技能/呼叫档案） | p19-41 (CCD09001CB01) | 可跑普通 CCD 的矩阵 + ACR 对象就位 | 后续全部实验的公共地基 | ACD 前缀规划依赖客户编号方案 |
| task-02 | 编写并调试首个 ACR 脚本（LCA+ISM 组合、ASM 内存、Debugger、技能追加、LIT 参数） | p42-50 (CCD09001CB02) | 已激活并验证的路由脚本 | 脚本工具链首次闭环 | 无 |
| task-03 | 运用授权/非授权名单规则（建列表、脚本、Debugger 改条件实测） | p51-81 | 按技能级别/时间切换名单的脚本 | 精准圈定可接听坐席的第一手段 | 无 |
| task-04 | 运用重定向/再分发规则（含 Voice Guide 重定向队列矩阵扩展） | p82-102 | 空列表兜底两种姿势的脚本 | 避免呼叫悬死的必备兜底 | 语音引导录制在书外细节 |
| task-05 | 实现坐席直拨与 ACR 结合（Pilot Direct Call/私有号/DICA/CALL_TYPE 脚本） | p103-127 | "直拨忙时等原坐席"业务 | 高频客户诉求（回头客找熟人） | 无 |
| task-06 | 用内部数据库按主叫号/Call Tag/坐席号定制路由 | p128-164 | 三键驱动的个性化脚本 | VIP/大客户路由的核心手段 | 数据维护入口在 CCS/CCSupervisor |
| task-07 | 用 IAA/统计 Pilot 生成并传递 Call Tag（含转移覆盖语义验证） | p165-189 | IAA 编码采集 + Call Tag 传递链 | IVR 与 ACR 打通的枢纽 | 语音引导内容需录制 |
| task-08 | 脚本内字符串处理与主屏显示 | p190-211 | 解析客户号码并屏显的脚本 | 号码分段/客户识别的编程基础 | 无 |
| task-09 | 配置多语言语音引导与语言偏好分发 | p212-229 | 按客户语言播报并选坐席 | 多语言呼叫中心刚需 | 多语言录音在书外 |
| task-10 | 掌握综合脚本能力（IDLE/COM、APPLY 语义、IQUEUE、屏显、清列表、IVR 规则、LIST 变量、CCD/ACR 混合选呼） | p230-282 | 复合业务脚本与停放体验控制 | 全书脚本能力的集大成章 | 无 |
| task-11 | 建 ACR 过滤器并出实时/Excel 统计（含 Super/Hyper-Filter） | p283-317 | 按业务视角的监控与报表 | 交付验收与运营报告的抓手 | 服务水准目标值需与客户约定 |
| task-12 | 外部 ASM 服务器安装割接（停 alb/装服务/建链路/迁脚本/防火墙） | p318-360 | 外部 ASM 承接路由 | 需要外部数据库时的前置改造 | 硬件软件需求查安装规程 |
| task-13 | 外部 ASM 双机热备部署 | p361-373 | Main/Stand-By 双机 | ACR 可用性保障 | 无 |
| task-14 | 理解外部数据库机制与 ODBC 接入 | p374-394 | SQL 六构件与 fetch 编程模型 | 外部化脚本的语法基础 | OPS 167 许可采购 |
| task-15 | MS Access 外部库实验（建库/ODBC/SELECT 脚本） | p395-407 | 读 Access 识别 VIP 来电 | 低门槛入门实验 | 32 位 Access ODBC 驱动 |
| task-16 | 准备 MS SQL 2016 侧（安装/建库表/账号/存储过程/Profiler 观测） | p408-426, p453-469 | 可被 ACR 读写的 SQL 环境 | 生产级外部库的标准形态 | SQL 安装规程在书外细节 |
| task-17 | MS SQL 外部库脚本实验（读写、存储过程、ASM 重启持久化验证） | p427-452 | LCA 落库抗重启的完整脚本 | 外部化的价值闭环（数据不随 ASM 重启丢失） | 无 |

### 优先级排序 (按"最能赋能实施工程师"的角度)
1. task-02 脚本编写与调试工具链（一切脚本能力的前提）
2. task-01 基础 CCD 矩阵（地基错误全盘返工）
3. task-04 重定向/再分发兜底（生产安全网）
4. task-05 直拨与 ACR 融合（最常见业务诉求）
5. task-06 内部数据库个性化（高价值低门槛）
6. task-10 综合脚本能力（复杂业务的工具箱）
7. task-12/13 外部 ASM 割接与双机（架构级动作）
8. task-14/15/16/17 外部数据库链（生产集成主路）
9. task-03 名单规则 / task-07 Call Tag 链 / task-09 多语言
10. task-08 字符串 / task-11 过滤器统计（支撑类）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 12 个一级部分（1 概念地基 + 1 公共实验地基 + 1 工具链 + 6 能力域并列 + 1 综合 + 1 统计 + 1 外部化）
- [x] 术语按实际内容列出（15 个）
- [x] 已检查作者局限/假设（实验矩阵口径、安全缺席、无规模测算方法、32 位 ODBC 时代约束）
- [x] 原书关键任务 17 项，全部有来源页码、交付物与重要性依据
- [x] 阶段 1 执行上下文中自动续写（工作区此前仅有 source_fulltext.txt，六件产出全缺，本次全部新建）

**用户确认时间**: 2026-09-23（流水线自动执行授权）
