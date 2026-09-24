# DIGEST — OTCC Advanced Call Routing 精华长文

> 源：OTCCXTE150EN Issue 01（470 页）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 OTCC 标准版高级呼叫路由（ACR）的全局认知；操作细节按需查 12 张能力卡。

## 一、这套东西是什么

ACR（Advanced Call Routing，高级呼叫路由）是 ALE OmniTouch 呼叫中心标准版上的脚本化选人引擎：**CCS 里写脚本，ASM 服务器执行，按呼叫特征算出一份动态坐席列表**。

它解决的传统三痛点：每个坐席一个组、复杂统计、外挂应用。有了 ACR，"回头客找原坐席、技能精确匹配、直拨等原坐席、VIP 优先"这些业务都能用脚本表达。

三个概念先立住：

| 概念 | 一句话 |
|---|---|
| ASM | 坐席选择模块：解释脚本、查数据库、算坐席列表；内部是 OXE 上的 alb 进程，外部是 Windows 服务 |
| 动态组 | ASM 每次呼叫即时算出的坐席列表，附着在等待房间上——不是 PBX 静态分组 |
| 等待房间 | ACR 专用停放区，不按 FIFO；与普通等待队列互斥不能同开 |

分发三步固定：呼叫特征化并关联档案进 Pilot → ASM 算列表 → 呼叫带列表进等待房间。从此"资源选择优先级"不存在了，选人全归 ASM。

## 二、地基：先有矩阵再谈脚本

一切实验共享一张 CCD 矩阵（19 步，p19-41）：

- **ACD 前缀先行**——没有前缀建不了任何 CCD 对象；CCS 安装必须勾 ASM script 组件（三个感叹号）
- **双链路**：普通 Pilot 加等待队列加处理组；ACR Pilot 加等待房间加同一处理组
- **入口分流**：统计 Pilot（车险/家险）各挂一份呼叫档案，汇入 ACR Pilot
- **规则结构**：每 Pilot 最多 30 条路由规则（0-29），分发规则最多 10 条；优先级三处同口径 0-9、0 最高
- **技能体系**：域（权重 1-20）挂技能，呼叫档案最多 7 技能、级别 1-9、强制/可选、语言偏好 1-7

容量上限速记（p18，Issue 01 口径）：

| 对象 | 上限 |
|---|---|
| 统计 Pilot / Pilot | 1000 / 600 |
| 队列与等待房间 | 600 |
| Pilot 到队列 / 队列到组方向 | 30 / 50 |
| 域 / 技能 / 特征列表 | 20 / 1000 / 1000 |
| 特征数（每档案/每坐席/系统） | 7 / 50 / 20000 |
| 名单（授权/非授权每列表坐席） | 30 |

注意：这是上限表，不是测算方法——"该建多少"要查 Feature List 与话务建模（书外）。

## 三、脚本工具链：五环闭环

1. **编写**：CCS 内嵌编辑器，Graphic/Text 双模式，构件拼装，脚本名不超过 8 字符
2. **传输**：保存并传到 ASM（.scr 源 → .alb 编译码，内部存 OXE /usr3/afe）
3. **激活**：挂到 ACR Pilot，一个 Pilot 同一时刻只有 1 个脚本
4. **验证**：Debugger 连 ASM 看轨迹、改既有构件条件实时复测、可直接发起呼叫——但**不能加新构件**
5. **运维**：adm_acd <ASM IP> -salb 是命令行仪表盘（24 名单、25 内部库、28 呼叫动态数据、11/14 链路、60 外部库连接与 61 许可锁）

"改了没生效"三连查：传了没有、激活没有、改 parameters.cfg 后重启 MAIN_AFE 没有（dhs3_init -R MAIN_AFE）。

Idle 排序由参数 asm_ag_free_duration 决定（最低版本 l2.300.32.a）：0=PLTR 登录时段话务比（默认）；1=LIT 单机；2=LIT 组网（空闲值每 3 秒上报）。用 LIT 还必须在脚本里显式加 IDLE 构件——两处配置缺一不可。

## 四、九种规则与组合语义

规则分两族（p244）：

| 族 | 规则 | 用法 |
|---|---|---|
| 单用规则 | LCA、Redirection、Redistribution、IVR | 必须独占一个 APPLY |
| 可组合规则 | 授权名单、非授权名单、ISM、IDLE、COM | 可串接；IDLE 与 COM 互斥 |

全书最反直觉的一条：**APPLY 数量决定语义**。仅 1 个 APPLY 时，前规则的输出是后规则的输入（名单真正过滤坐席）；两个及以上 APPLY 时各自独立，第一个的结果被丢弃——实验对照里"名单外的 31500 也被呼"。要"名单加技能"必须单 APPLY 链式写法。

空列表兜底两式：Redirection 转一个号码（内部/经缩位拨号或网络号出外部/STRING 变量动态号）；Redistribution 退回 CCD 下一路由方向。全无可用方向则落 Blockage。坐席列表持续为空时脚本反复执行（原书两处口径 20/21 次）再转路由管理——所以兜底要提前配，别让呼叫悬死。

## 五、呼叫特征与个性化

脚本可用的原料：主叫号 CLID、直拨被叫号 NDI、Call Tag、呼叫档案（最多 7 技能）、呼叫类型。

- **内部数据库**（4000 条）：主叫号/Call Tag/直拨坐席号三键，查名字、档案、名单、优先级；主叫号与标签都支持区段（如 1000-1999 整段命中）
- **Call Tag 三来源**：统计 Pilot 静态标（0-32 字符）、IAA 编码叶（16 位内，经 CSTA Correlator data，只能外部呼入）、CCivr TransferCall（前置 GetPilotInfo）
- **覆盖规则**：转移链上最后一个 Call Tag 或档案覆盖之前所有——排障按路径末端查，不按入口查
- **直拨融合**：处理组 Pilot Direct Call 加坐席私有号加 DICA 自动技能（停用即完全不可直拨）加 CALL_TYPE=DIRECT_CALL 分支，实现"忙时等 30 秒原坐席再转走"
- **多语言**：一个引导映射 40 语种；语言取档案偏好（1-7、1 最高），档案没有就退 ACR Pilot 语言；坐席 1 门语言技能即可入选

## 六、混跑选呼与等待体验

呼叫选择三序：先比优先级（0-9）；相同时看 ACR Actual Waiting 参数——False（默认）先最低 ISM 成本再最长实际等待，True 反过来。

ISM 成本三档：非 ISM 的 ACR 呼叫 0；ISM 的 ACR 呼叫按档案计算；等待队列里的普通 CCD 呼叫无穷。**这就是 ACR 呼叫默认插队普通来电的机制本质**，混跑站点要么用优先级平衡，要么把 ACR Actual Waiting 置 True，并提前向客户讲清。

等待体验编程：IQUEUE 构件在脚本内覆写停放级——1-6 级每级可配语音引导、预期等待表或地址；NEXT 级在重选重跑而上一停放没播完时接管。LIST 变量 16 个，skill 型喂 ISM（超 7 技能截断）、agent 型喂名单规则（无上限）。

## 七、监控与外部化

- **过滤器**：只影响观测不改分发。200 个、每个 7 技能、AND 语义；Super-Filter（同节点）/Hyper-Filter（跨节点）25 对象 OR 语义；新过滤器查不到创建前的 Excel 历史（预置 20 个有历史）。Excel 三模板：明细（Formfilter）、汇总（FormFilterS）、坐席交叉（FormAgentPerFilter）
- **外部 ASM**：角色与内部 alb 一致外加外部库访问。割接顺序是硬约束：asm_on_dhs 改 0，重启 MAIN_AFE，核 alb 已停，装服务，建 Site（Router 角色跑脚本），迁 .scr 重编译，防火墙放行 ASM 与 ASMMgr 入站 UDP 加 TCP。外部 ASM 连接免许可
- **双机热备**：Main/Stand-By 互设，连接与脚本自动复制；改配置前必须停服务；备机必须能解析 OmniPCX 名
- **外部数据库**：32 位 ODBC 是硬约束（64 位驱动连不上）；同脚本 16 个库；连接随脚本激活建立；SQL_RESULT 三值（SUCCESS/ERROR/NOT_FOUND）；fetch 无 BREAK 全表扫、不用 LIST 只留最后一行；读或写外部库需许可 N°167
- **LCA 持久化**：LCA 默认只活在 ASM 内存，重启即失。存储过程 updateCalling 每呼写库、查询改读库——ASM 重启后"上次接听坐席"依然有效（三呼实验验证）

## 八、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 写脚本/调试/LIT 排序/字符串 | acr-script-editor-fundamentals |
| 建矩阵/配 Pilot/技能档案/混合链路 | acr-ccd-matrix-foundation |
| 忙时转接/退回/封锁排障 | acr-redirect-redistribution |
| 直拨等原坐席/DICA/CALL_TYPE | acr-direct-call-dica |
| VIP 路由/三键查库（4000 条内） | acr-internal-database-routing |
| 规则组合/IQUEUE/LIST/混跑选呼 | acr-rule-combination-advanced |
| 外部 ASM 割接/双机 | acr-asm-deployment |
| 查外部库/ODBC/存储过程/LCA 落库 | acr-database-query-routing |
| 名单圈定与排除/Call Tag/多语言/过滤器 | 路由入口（otcc-advanced-call-routing-router） |

## 版权

- 本精华长文为 ALE Training Services《OmniTouch Contact Center Standard Edition — Advanced Call Routing》（OTCCXTE150EN Issue 01）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
