# 语音导航套件：AA、MLAA 与 Smart Call Routing（树结构、语音指南、客户码路由）

## R — 原文依据

> "Two different tree structure: day (Normal) /night (Restricted) • Two menu levels by tree (100 nodes in the tree) … 4 voice guides possible languages"（p407）
> "After a cold reset, 2 ports are systematically set into the default attendant group n°8"（p409）
> "A maximum of 5 tree structures are manageable … Tree structure up to 3 levels … Number of dedicated MLAA ports (0 to16)"（p428, p431）
> "The total maximum size of all voice prompts must not exceed 12000 seconds (200 minutes)"（p440）
> "Rules available: 10 000 … Up to 10 plans … 64 Exceptional days are in common with ACD … 8 voice prompt from 107.wav to 807.wav"（p454-457）
> "Message client code of group 1 = 'please enter your client code and validate by #'"（p462）

出处：OXOCXTE301EN p405-462。

## I — 自述

三层递进的来话处理：AA（一套树）→ MLAA（按 DID/CLI 多棵树）→ SCR（客户码+时间的规则引擎）。

| 维度 | AA | MLAA | SCR |
|---|---|---|---|
| 树 | 2 棵（白天 Normal/夜间 Restricted），每树 2 级 100 节点 | 最多 5 棵（license 1/5），3 级每级 10 选 | 无树，规则表 |
| 路由依据 | 按键 + 时段 | DID 和/或 CLI | CLI/DDI/DTMF 客户码 + 开闭时间 |
| 语言 | 4 语言 | 每树 4 语言（100 消息/语言） | 客户码提示 8 条（107-807.wav） |
| 端口 | 语音端口 2-8（与 VM/Audiotext 共享） | 专用 0-16（与 ACD 共享） | 依托 ACD |
| license | 树与语音指南定制需 license | 树数 license（1/5） | SCR + 1 Supervisor Console |
| 硬限 | — | 消息总量 12000 秒；每条默认 15 分钟（MLAA_MSG） | 10000 规则；10 计划；64 特殊日（与 ACD 共用） |

**AA 要点**：转接模式 noteworthy AATypTrf（02 半监督默认/00 盲转）；免费拨号 AAGrDialng 默认禁、AAGrTransf（0/9 转话务员）默认启；Press '*' 与语言选择菜单期间免费拨号不可用。冷复位后默认 2 端口进话务员组 8 并接外呼——新机"外呼进来是语音菜单"不是故障（n59）。

- **MLAA 要点**：配置全在 OMC 图形编辑器，先 Save as 再 Transfer to the server；line parameters 不随存档保存（n26）；端口与消息改动需 ACD 引擎复位或等 10 分钟（n27）。
- **SCR 要点**：X 为通配符（CLI/DID 隔离号码段、客户码替换整码）；无码匹配走 Backup destination；日志从监督台出、WebDiag 导出。

## A1 — 书中案例

**AA 实验**（p422-426，厂商实验）：

1. 树规划：press star 后一级菜单 6 键（会计/销售子菜单、General mailbox、转 104 邮箱、留言）。
2. Greetings tab 勾 "press star question"；AA menu 的 Opening hours tab 编辑树。
3. 子菜单 1 转 101/102、子菜单 2 转 102/103。
4. MMC 话机录问候与各级语音指南（或 OMC 导入）。
5. 遍历全树选项；General mailbox 留言转发到 101 邮箱核对（p426）。

**MLAA 实验**（p443-449，ISP 场景）：

1. 树规划：DID 41509，问候+语言选择（英/法）+四级菜单（订阅/改合同/套餐/解约）。
2. MMC 录 MSG001-007（问候/语言选择/菜单 1-4/解约说明）。
3. MLAA Setup：专用端口 8（与 ACD 共享上限 16）；DDI 41509 关联寻线组 509。
4. MLAA Services 建菜单并接线（菜单 4 按 2 播 msg007）；Line parameters 填 DDI、Service opened: Tree 1。
5. Tools 先保存再 Transfer to the server；拨 021PN41509 走完整树（p449）。

**SCR 实验**（p459-462，厂商实验）：

1. 目标：DDI 41510——8:00-14:00 客户码 001 转 101、002 转 102、其它码转 103；14:00 后转 100。
2. ACD Setup 把 ACD 端口放入寻线组 510 并关联 41510。
3. 录客户码提示（107.wav）："please enter your client code and validate by #"。
4. SCR tab 配开放时间 8am-2pm；建三条规则（001/002/通配 x）与闭时段目的地 100。
5. 打 41510 输不同客户码核对去向；14 点后核对全部到 100。

## A2 — 未来触发

使用情境：公司总机要语音导航；白天夜间不同菜单；多业务线或多语言入口；按主叫号码分流；客服要客户报编号再分流；改了语音怎么没生效；新装机外呼进来是语音菜单。

语言信号：AA / 自动话务员 / automated attendant / 语音导航 / 话务员树 / MLAA / 多树 / multi-language / 客户码 / client code / Smart Call Routing / SCR / DID 路由 / CLI 路由 / press star / 免费拨号 / voice guide / 语音指南 / 12000 秒。

与相邻能力区分：ACD 呼叫中心排队与坐席管理在 ACD-SCR 域但书内仅以组为目的地，完整 ACD 运营在书外；语音留言与个人助理归语音邮箱与移动能力；时段表机制（Day Groups/Hours）归 ARS 套件能力。

## E — 可执行步骤

输入契约：菜单树设计（层级/按键/目的地）、语音脚本与语言、DID/CLI 规划、license 状态（AA 定制/MLAA 树数/SCR+Supervisor Console）。树设计未定 → 判停先出菜单脚本给客户确认，再动手配。

1. 选型：单入口按时段切选 AA，多业务线按 DID/CLI 选 MLAA，要客户码互动选 SCR。完成标准：选型与 license 对齐
2. 录语音：MMC 话务员会话按 MSG 编号录（MLAA 001-100/语言）或 OMC 导入（AA 为 ADPCM G726 格式）。完成标准：消息入册
3. 建树/规则：OMC 编辑器建菜单与目的地（SCR 建规则行与开闭目的地）。完成标准：结构与规则落表
4. 接线：AA 挂 DID；MLAA Setup 定端口并 Line parameters 映射 DDI→树；SCR 关联 ACD 组与 DID。完成标准：来话进树
5. 传输/生效：MLAA 先 Save as 再 Transfer（line parameters 另存记录）；等引擎复位或 10 分钟。完成标准：配置激活
6. 调行为：AA 按需改 AATypTrf/AAGrDialng/AAGrTransf；确认 Press '*' 与语言菜单期免费拨号不可用。完成标准：行为符合预期
7. 验证：遍历全树按键；按实验口径核对各目的地；闭时段/备份目的地单独试。完成标准：全路径通

判停点：

- 消息总量逼近 12000 秒 → 停，先删冗余语音（硬上限，无法超）
- 改完配置"没反应" → 先查生效条件（引擎复位或 10 分钟，n27），再排查配置
- 换机迁移后树在但来话进不来 → line parameters 不随存档（n26），手工重配
- 客户要在菜单里做账号查询等动态互动 → 超出按键树能力，转外部 IVR 方案

输出契约：树/规则设计文档 + 语音消息清单（编号/语言/时长）+ 全路径测试记录 + license 消耗清单。

## B — 边界

- AA 树与语音指南定制、MLAA 树数、SCR 均需 license（冷复位默认树只能留言/转话务员）
- SCR 客户码是 DTMF 互动校验，不是账号系统；客户码库维护在规则表内（CSV 导入导出兼容）
- MLAA 端口与 ACD 共享 16 上限：扩 ACD 会挤占 MLAA 端口
- SCR 开闭计划 10 个、特殊日 64 个与 ACD 共用：排期冲突先对齐 ACD
- 实验单语录音（RDP 音质）为教学口径；生产多语言需逐语言完整录制（每语言 100 消息）
