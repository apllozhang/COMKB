# GLOSSARY — OTCC Advanced Call Routing 术语表

> 阶段 3 产出（源：candidates/glossary.md，55 条，六大域；本文件为门户精选版，全量以 candidates/glossary.md 为准）。
> 口径：定义只采信本书正文；ASM 书中写作 "Agent Selection Modul"（原书拼写，照录）；IAA/MAO/MLE/RSI/CSTA/DTMF/csm/GD 等缩写书中未给全称，如实标注；实验编号为实验口径。

# OmniTouch CC Standard · Advanced Call Routing (OTCCXTE150EN Issue 01) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（470 页全部通读），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| ACR (Advanced Call Routing) | 高级呼叫路由 | 基于脚本的呼叫路由特性：编辑器内嵌 CCS、脚本挂 ACR Pilot、ASM 服务器执行，按规则与呼叫特征返回坐席列表 | p3-18 |
| ASM (Agent Selection Modul) | 坐席选择模块（"Modul" 为原书拼写） | 解释脚本、查/更数据库、按坐席配置加脚本规则加呼叫档案计算坐席列表的服务器；内部（alb 进程）或外部（Windows 服务） | p6, p9-11, p320-321 |
| ACR Pilot | ACR 引导号 | 承载 ACR 脚本的引导号：配等待房间、无资源选择优先级（选人归 ASM）、同一时刻仅 1 个脚本 | p6, p12-13, p113 |
| Statistic Pilot | 统计引导号 | 业务入口，带呼叫档案与可选 Call Tag，汇入 Routing Pilot；容量 1000 | p36, p168 |
| Waiting Room | 等待房间 | ACR 专用停放区：不按 FIFO，ASM 动态坐席列表附着其上；与等待队列互斥不能同开 | p12-14, p233 |
| Dynamic Group | 动态组 | ASM 每次呼叫即时算出的坐席列表，非 PBX 静态分组 | p12, p14 |
| Call Profile | 呼叫档案 | 呼叫的技能需求清单：最多 7 技能、级别 1-9、强制/可选，语言偏好 1-7（1 最优先） | p15, p39 |
| CHARACTERISTICS_LIST | 特征列表 | 呼叫运行时实际携带的技能特征集合，ISM 最常用输入；档案是定义、特征列表是运行时值 | p15, p18, p259 |
| Call Tag | 呼叫标签 | 随呼叫走并受 ACR 分发机制操作的字符串（CSTA Correlator data）；三来源，转移时最后者覆盖前者 | p15, p168-173 |
| Skill / Domain / Weight | 技能/域/权重 | 技能 1-16 字符加缩写 1-4 字符挂域（ID 0-99、权重 1-20 参与ISM 计算）；坐席按技能配级别 1-9 | p37-38, p41 |
| ISM cost | ISM 成本 | 等待房间中被选中的代价：ISM 按档案算、其他规则 0、等待队列普通 CCD 呼叫无穷；越小越先服务 | p221, p235 |
| PLTR / LIT | 登录时段话务比/最长空闲 | Idle 规则两语义：PLTR=周期处理时长/登录时长（默认 5 分钟周期）；LIT=登录后最长空闲优先（参数 1 单机/2 组网） | p239-242 |
| 9 ACR Rules | 九种 ACR 规则 | ISM/LCA/授权/非授权名单/重定向/再分发/Idle/Com/IVR；单用 4 种独占 APPLY、可组合 5 种、Idle 与 Com 互斥 | p7-8, p244 |
| Direct Call / CALL_TYPE / DICA | 直拨族 | 直拨特性把打坐席 DN 的外部呼叫 ACD 化；CALL_TYPE=DIRECT_CALL 供脚本识别；DICA=配私有号自动挂的开关型技能 | p105-115 |
| Internal Database (ACR Data) | 内部数据库 | 主叫号/Call Tag/坐席号三键存名字/档案/名单/优先级，4000 条；脚本以 CALL_PROFILE[键] 等取用 | p130-141 |
| Reselection / SEQUENCE | 重选机制 | 坐席全忙时呼叫在房间停指定秒数后脚本重执行，轮次记在 SEQUENCE；空列表反复重试后走路由管理直至封锁 | p43, p97-98, p115 |
| Blockage | 封锁模式 | 重分发无可用方向或重试耗尽时的最终落点：封锁地址或语音引导 | p50, p89 |
| IQUEUE / Parking Level | 停放级构件 | 脚本内覆写等待房间停放体验：1-6 级每级可配引导/EWT/地址；NEXT 级在重选重跑时接管 | p249-252 |
| LIST variable | 列表变量 | 16 个 LIST[%1..16]，元素定类型：skill 型供 ISM（超 7 技能截断）、agent 型供名单规则（无上限） | p258-261 |
| Filter / Super-Filter / Hyper-Filter | 过滤器族 | ACR 呼叫统计分组：200 个每个 7 技能 AND 语义；同节点/跨节点组各 25 对象 OR 语义；不影响分发 | p285-307 |
| Debugger | 调试器 | CCS 内连接 ASM 跟踪脚本、改既有构件条件、发起呼叫；不能新增构件、整型观察用加 %0 技巧 | p46, p59, p338 |
| ACR Actual Waiting | 实际等待优先开关 | RSI 参数：False（默认）先最低 ISM 成本再看最长实际等待；True 反之 | p234, p282 |

## 二、角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Agent / Supervisor | 坐席/主管 | ACD Station 类型建户时一次定型不可改；坐席话机限定 8068/8068s/8078s | p31-32 |
| Self-assignable agent | 自助登录坐席 | 无需管理员介入即可登录任意期望的处理组（配合登录密码） | p32 |

## 三、订阅/许可域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Software License N°167 | "ACR data base read" 许可 | 脚本读/写外部数据库的前提；外部 ASM 与 OXE 间连接本身免许可；adm_acd 选项 61 核可用性 | p320, p376, p394 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniTouch CC Standard Edition | OTCC 标准版 | 本书宿主产品：OXE 上的 CCD 软件栈；ACR 替代"每坐席一组加外部应用"传统做法 | p1, p5 |
| OXE (OmniPCX Enterprise) | OXE 交换机 | 底层 PBX：承载 CCD/AFE/alb 进程、parameters.cfg 与语音引导闪存卡 | p215, p320-322 |
| CCS / CCsupervisor | 联系中心管理站 | 内嵌 ASM 脚本编辑器与 Debugger，承载 ACR 配置树（Skill/ACR Data/Filter/Super Objects 等）与观测窗口 | p6, p37, p59 |
| AFE / MAIN_AFE | 前端服务器进程 | 接收呼叫处理请求并管理 alb；asm_on_dhs=0 让其不再拉起 alb；重启命令 dhs3_init -R MAIN_AFE | p9, p49, p322 |
| alb process | 内部 ASM 进程 | OXE 上的内部 ASM 服务器：LCA 等动态数据默认只在其内存，重启即失 | p45, p320-321 |
| External ASM Server | 外部 ASM 服务器 | Windows 服务形态，角色与 alb 一致外加外部库访问；ASM Manager 建站点链接、ASMServer Tool 装服务 | p320-330 |
| Voice Guide（三种形态） | 语音引导 | 普通/可录（*88 录音、*66 测音）/多语言（Function=Multi-language message，40 语种映射消息 1000-1039） | p175-176, p215, p224 |
| IAA (Automated Attendant) | 自动话务员 | 叶-树-接入三层；Code Entry Guide 叶采集 16 位内代码作 Call Tag；只能外部呼入 | p169, p177-180, p211 |
| CCivr | IVR 服务器组件 | 经 CSTA 交互：资源组挂等待房间分发、TransferCall 携标签、receivephonecall.callprofile 读档案 | p170, p255-256 |
| ASM Script Editor | 脚本编辑器 | Graphic/Text 双模式；产物 .scr 源与 .alb 编译码；SQL 页签另有外部库六构件 | p44, p65, p376 |
| adm_acd | 维护命令 | 形态 adm_acd <ASM IP> -salb：24 名单/25 内部库/28 呼叫动态数据/11 链路/14 连接类型/60 DB 连接/61 许可锁 | p45, p60, p141, p394 |
| parameters.cfg | 参数文件 | /usr3/afe 下 vi 手工编辑：asm_ag_free_duration（0=PLTR/1=LIT 单机/2=LIT 组网）、asm_on_dhs（割接置 0） | p48-49, p241-242, p322 |
| MS Access / MS SQL Server 2016 | 实验数据库 | Access 库 acr.accdb 表 Records（免凭据）；SQL 库 acr_sql 表 Customer（登录 Brest）——均为实验口径 | p396-399, p409-415 |
| Stored Procedure（updateCalling） | 存储过程 | SQL_REQUEST CALL 调用（库须支持嵌入式过程）；实验过程把主叫号与上次接听坐席写入 Customer 表实现 LCA 持久化 | p382, p421-426, p434 |
| Formfilter / FormFilterS / FormAgentPerFilter | Excel 三模板 | 明细（时间片粒度）/汇总（每过滤器一行）/坐席乘过滤器交叉，分别对应三个 Excel 菜单出口 | p299-301 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| CSTA | 计算机电话集成接口（未展开） | Call Tag 以 Correlator data 形态在 IVR/IAA/CCivr 与 PCX 间传递 | p15, p169-170 |
| SQL（受限集） | 受限 SQL | ASM 脚本里仅 SELECT 加 CALL 存储过程两种；WHERE 可用 26 项呼叫上下文变量 | p376, p382-384 |
| ODBC / System DSN | 数据库接入通道 | ASM 只支持 32 位 ODBC；DSN 名与脚本源名一致（原文语法印作 DNS=）；先建库后建 DSN | p379-380, p399, p433 |
| *.scr / *.alb | 脚本文件两形态 | .scr 源文件可跨环境复制后重编译；.alb 编译码不通用；内部存 /usr3/afe、外部存安装目录 Script | p11, p335 |
| Hybrid Link (ABC-F) | 混合链路 | 本地 CCD 呼叫所需：类型 Hybrid、邻接网络号 0-31 且异于本地、至少 2 access 成对；hybvisu -f all 校验 | p33-35 |
| DTMF / Correlator data | 按键与关联数据 | 菜单叶按键分流与编码叶输入方式；编码与 CCivr 附着值统称 Correlator data（客户号/索引/上下文 Id） | p169-170, p177 |

## 六、站点与资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| /usr3/afe | OXE 上 ACR 家目录 | parameters.cfg 与内部 ASM 的 .scr/.alb 所在；外部化时经 FTP 由此取脚本 | p48, p335, p354 |
| Program Files\...\Agent Selection Module\Script | 外部 ASM 脚本目录 | 外部 ASM 脚本默认存放处（双机实验口径为 x86 路径）；主备自动同步，可作核验点 | p335, p373 |
| D:\CCD_ACR\SQL Call Procedure.txt | 存储过程源文件 | 实验环境提供，经 SSMS File/Open 载入执行生成 updateCalling | p423 |
| ODBC Data Sources (32-bit) | 32 位数据源管理入口 | 建 System DSN 的固定路径（务必 32 位版本），Access 与 SQL Server 两章共用 | p379, p429 |
| SOFTPANEL / SoftPanel / SoftPanel2 | 实验主机名 | SOFTPANEL 为 SQL Server 主机；SoftPanel（Main）与 SoftPanel2（Stand-By）为双机 ASM——实验口径 | p362, p428 |
| CCD09001-CCD09013 | How-To 底层文档编号 | 20 个实验章的原始文档编号体系，同一课程模块跨发布物可追溯 | 各 How-To 章页眉 |
