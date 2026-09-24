# Book Overview（参考区）— OTCC Advanced Call Routing

> 供能力卡引用的背景参考；源自 references.md 落位。

## 交付主线（组织轴）

概念地基（9 规则、ASM 架构、分发三步、容量上限）→ 基础 CCD 矩阵（普通链路加 ACR 链路加统计 Pilot）→ 脚本工具链（编写/激活/Debugger/LIT 参数）→ 规则族与特征源并列展开（名单/兜底/直拨/内部库/Call Tag/字符串/多语言）→ 综合特性（APPLY 语义、IQUEUE、LIST、混跑选呼）→ 过滤器统计 → 外部化三线（外部 ASM、双机、外部数据库）。这是"先矩阵后脚本、先单机后外部"的教学主线，也是实际交付项目的推荐顺序（p3-470 章节编排）。

## 实验矩阵（实验口径，仅 Boundary 背景）

- 编号体系：3x 的 x 为讲师给定位数。普通链路：Pilot 3x600 加 队列 3x999700 加 坐席处理组 3x999800；ACR 链路：ACR Pilot 3x603 加 等待房间 3x999703；统计 Pilot 3x650（车险，档案 1：English+Car）与 3x651（家险，档案 2：English+Home）汇入 3x603（p22）。
- 后续增量对象：直拨 Pilot 31604、私有号 31001、转移目标 31010、重定向队列 31999702 加 Voice Guide 处理组 31999802 加 引导 710、IAA 接入 31900/31888、统计 Pilot 31652/31653、坐席 31500/31501/31502、话机 3x000-3x002/3x500-3x502（p22 备注 "3X800" 为笔误，见 needs-review nr-02）。
- 引导资源：710-719 可录引导、多语言实验用 740（法语 1000/英语 1001）、IQUEUE 实验用 701-706/751-757；录音 *88、测音 *66。
- 外部 ASM 双机：主 10.2.T.20/SoftPanel（Main）、备 10.2.T.21/SoftPanel2（Stand-By）；脚本目录 C:\Program Files (x86)\Alcatel\Agent Selector Module\Script。
- 外部数据库：Access 库 acr.accdb 表 Records；SQL 库 acr_sql 表 Customer（Caller 主键、Last_Agent 默认 NoAgent、Name 默认 NoName、VIP 默认 0）；SQL 登录 Brest/alcatel（关闭密码策略）；sa 口令 Alcatel@1 为安装时自定义（非出厂值）；过程源 D:\CCD_ACR\SQL Call Procedure.txt；SQL 主机 SOFTPANEL。
- 安全声明：以上全部口令/账号/IP 为实验口径，生产必须强口令、最小授权、凭据不进明文脚本（原书安全话题缺席，整改方向为推断）。

## 平台速览（方案沟通素材）

- ACR 定位：脚本选坐席——CCS 内嵌编辑器写脚本（*.scr 源/*.alb 编译），ASM 解释执行，按呼叫特征返回动态坐席列表；呼叫控制仍在 CCD 矩阵（p6-11）。
- 容量上限（p18，Issue 01 口径）：统计 Pilot 1000；Pilot 600；队列与等待房间 600；组 450；Pilot 到队列方向 30；队列到组方向 50；域 20；技能 1000；特征列表 1000；特征数每档案 7/每坐席 50/系统 20000；授权与非授权名单各 30 坐席。测算方法书外（查 Feature List）。
- 分发三步：特征化关联档案进 Pilot → ASM 算列表 → 呼叫带列表进等待房间；房间与队列互斥、房间非 FIFO（p12-13）。
- 呼叫选择三序：优先级 0-9（0 最高）→ 按 ACR Actual Waiting 分派 ISM 成本与实际等待先后；等待队列普通 CCD 呼叫 ISM 成本无穷（p234-235）。
- 内部库 4000 条；外部库同脚本 16 个、32 位 ODBC、读或写外部库需许可 N°167（p131, p376, p320）。

## 教材口径声明

- 全部实验编号/口令/账号/IP 仅限实验环境；生产必须替换并做安全加固（引用时一律标"实验口径"）。
- 生产化边界三去向：Feature List（容量细则）、OXE 侧配套文档与安装规程（矩阵/外部 ASM 硬件）、CCivr/CTI 侧文档（IVR 构件编程）——均为原书指定或明示书外。
- 版本敏感点：asm_ag_free_duration 最低版本 l2.300.32.a、旧 patchIdle 文件已废弃（值 1 对应其行为）；CCS 安装须勾 ASM script 组件；脚本重试次数原书两处口径 20/21 次（needs-review nr-01）。
- 原文笔误照录清单见 needs-review.md（3X800、STRING_LENGHT、DNS=、AUTHORIZED/AUTHORISED 混用、p196 示例值、NoAgent/noAgent 大小写）。
