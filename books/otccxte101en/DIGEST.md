# DIGEST — OmniTouch Contact Center Standard · Advanced 精华长文

> 源：OTCCXTE101EN Edition 07（597 页，OTCC Standard R10.15 / OXE 11.1）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 OTCC 高级能力的全局认知；操作细节按需查 12 张能力卡。

## 一、这本书讲什么

OmniTouch Contact Center Standard（OTCC Standard）的基础版把呼叫中心跑起来；这本 Advanced 教材在这个底座上叠加六类高级能力：
**技能路由的算法口径（ISM）、跨站点互助（Remote PG）、实时墙板（Soft Panel Manager）、话务票据分析（CCTA）、特殊功能开关、报表与集中接入（Excel 定制 + CCS Server）**。
全书是"讲义给模型与数值边界，How-To 给菜单路径，呼叫测试给验收"的行为闭环。

一个前置认知：ACR（高级呼叫路由）的一切建立在"等待室"上。呼叫先被特征化（主叫号码、被叫号码、呼叫标签、呼叫档案），路由到 ACR Pilot，ASM 按脚本算出坐席列表（动态组），呼叫带着这份列表进等待室等坐席。等待室与普通等待队列在同一规则里互斥，且不做 FIFO。

先记三组数字：

| 数字 | 含义 |
|---|---|
| 7 / 50 / 20 | 呼叫档案最多 7 个技能属性；坐席最多 50 个技能；域最多 20 个（技能 1000 个） |
| 15 / 120 | CCS 直连 AFE 上限 15 连接；外部 CCS Server 120 客户端（连接数超过 9 必须上 Server） |
| 500 / 150 / 200 | SPM 订阅统计、并发连接、面板+墙板三限 |

## 二、技能路由是怎么想的（ISM）

ISM 匹配是三级漏斗：坐席必须具备呼叫档案**全部强制属性**（坐席等级大于等于呼叫等级）才进第 1 子列表；重选定时不中就逐级降级（N-1 项满足+1 项不满足，直到全不满足）；同一子列表内按成本排序——Cman（强制属性差值乘域权重的总和）最小者胜，同分比 Copt（可选属性，缺技能按 9 代入），再同分按 PLTR 或 LIT。

一个手算例子（书中完整算例）：两个坐席 Cman 同为 14，Copt 分出胜负——Agent1 无 Client 技能按 9 代入得 31，Agent4 得 3，Agent4 排第一。

三个常被误解的口径：

| 口径 | 事实 |
|---|---|
| 最久空闲优先（LIT） | 用 asm_ag_free_duration=1 开启（需 IDLE 积木块+重启 MAIN_AFE）；但坐席统计默认 5 分钟刷新，低话务时形同"同一坐席每 5 分钟被叫一次" |
| 重选 21 次 | 脚本重选上限 21 次（另一处表述为 21 次请求=20 次执行）；RESELECTION_TIMEOUT 是重跑节拍，不是最长等待 |
| 直拨路由 Pilot | 没有呼叫档案就是空列表，跑满 21 次走闭锁——业务号码要引导客户拨统计 Pilot |

## 三、跨站点互助（盲/智能 + Remote PG）

互助两种形态：**盲互助**没有 ABC-F 链路，远端把呼叫当新呼叫处理；**智能互助**经 ABC-F 交换 Pilot 状态、已听引导、真实等待时间，按远端状态路由，远端可拒收（按五类地址回退本地处理）。

分布式互助三对象：本地建 **Remote PG**（Type=Remote，有分布门限+资源选择优先级，没有呼叫选择优先级），指向远端的**虚拟队列**（只映射本地队列队头呼叫特征）和**专用 Pilot**（一个虚拟队列专属）。

三级水位控制别搞混：

| 控制层 | 参数 | 语义 |
|---|---|---|
| 方向选择 | 资源选择优先级 0-9 | 0 最高 9 最低；同级处理组比 LIT |
| 溢出节奏 | 分布门限（秒，实验 15） | 呼叫在本地队列等满 N 秒才许流向远端 |
| 队列饱和 | 最大等待时间 0-3276 秒 | 达阈值队列降为最低优先级；0=零等待队列（立即改道） |

排障入口两条命令：compvisu sys（Direct Link 状态、H323、RTP Direct）与 hybvisu -f all（四态 IDLE/SYN_REQ/SYN_ACK/DATA_TRANS，健康=DATA_TRANS；
High=全编解码、Low=G729）。断链或远端闭锁时，本地饱和的溢出呼叫会落到语音引导 PG 播完引导后释放——这是兜底设计，但意味着断链期间溢出话务直接流失，
生产要有告警与回拨策略。

## 四、实时墙板（Soft Panel Manager）

SPM 是独立于 CCS 的数据链：OXE CCD > CCS > RTI Connector（Windows 服务）> SPM 服务器（Tomcat，默认端口 9060）> 墙板/液晶/电视 + 邮件告警。
部署三件套：SPM 服务器、RTI Connector、FlexLM 许可（103 号包是 OXE 侧前提）。
显示端是背景、视图、软面板、挂件四层模型，告警四步（阈值条件+邮件+告警视图替换）。

四条最容易踩的口径：

| 坑 | 事实 |
|---|---|
| 同机共存 | CCS 与 RTI Connector 同机时 CCS 必须专用于 RTI，RTI 运行期禁止手工再启 CCS |
| 统计不动 | 统计按需订阅：只有被视图/告警引用的统计才更新，新选用最多 1 分钟生效 |
| 许可失效 | 界面常驻告警横幅+统计更新冻结，先查 LMTOOLS 别重启 RTI |
| 日统计 | 每 15 分钟取一次（不可更快），取数在每刻后 2 分钟，0 点清零 |

细节限制：视图定制仅限 Firefox；HTML 挂件只认 http://；历史曲线最多 2000 值或 24 小时；已被引用的统计过滤器撤不掉（先删引用对象）。

## 五、特殊功能与数据交付

**特殊功能**全是"对象参数开关+行为验证"：优先转接（双队列）、DID 忙音（注意默认饱和听的是 2 号间隔引导音，不是忙音）、
#013 组内代接与 #014 直接代接（前缀+COS 放行）、监督监听、永恒整理（整理期办电话事务不打断计时）、
中继预留两级数学（62 条 SIP 接入，业务预留 20% 后 CCd 约 50 条，单 Pilot 限额 30% 约 15 条）。
监听与录音只有操作没有合规边界，上线前必须补法律评审。

**CCTA 票据分析**：离线工具，Importation 自动导入 .Z 票据（通信+事件两类），Ticket Tracer 过滤出报表并导 ASCII。结束原因共 40 种（样例：0=主叫挂机、1=系统挂机、26=坐席挂机），呼叫类型共 10 种（0=非 ACR、1=ACR）。

**Excel 报表定制**：Formats 目录 11 种模板，在模板里加 Custom 工作表——结构区直接拷贝、值区用"粘贴链接"引用 General，数据仍由 General 承载。两大纪律：改前把原件改名 *_old 留底；改完必须关并重开 CCSupervision。粒度陷阱：General 表约 24 行，½ 小时粒度单张表只覆盖 0:00-16:00，全天要建第二张链表。

**CCS Server 集中接入**：直连 AFE 物理上限 15 连接；内部 serv_ccs 15 客户端；外部 Windows 服务 120 客户端（Windows Server 2019/2022）。CCd R3.1+CCs 4.3.46.1 起连接数超过 9 必须上 Server；一个 AFE 只接一个 Server——外部服务被拒接，第一刀切内部进程是否真停。

## 六、交付红线与排障命令箱

四条红线：

1. 教材全部密码/账号/号码/网段是实验值（mtcl、admin/admin、123456……），上生产必须整体替换并按安全基线加固
2. 技能体系"怎么设计"（划域、定权重、评等级）全书不教，只教"怎么配"——照实验建域上生产大概率失真
3. 话务建模与 sizing（Erlang、坐席/中继估算）在书外，容量表只是合规红线；超限查当期 Feature List
4. 数值口径：21 次重选、5 分钟统计刷新、15 秒门限均为实验观察口径，不是调优建议

排障命令箱（mtcl 会话）：

| 命令 | 用途 |
|---|---|
| adm_acd | 对象清单（Pilot/队列/统计 Pilot/处理组/人员/ACR 数据/许可） |
| adm_acd <ASM IP> -salb | 坐席统计（21）、ASM 记忆（28，清记忆后复核用） |
| adm_acd <Server IP> -servccs | 经 CCS Server 接入的客户端清单（10） |
| hybvisu / compvisu sys | ABC-F 直连链路状态与话音参数 |
| pildstctx / pgctx / acdsup | 专用 Pilot / Remote PG 上下文与开闭状态 |
| spadmin | RTI 103 号包等许可核对 |

## 七、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 解释分配次序/开 LIT/算容量 | otcad-ism-skill-matching |
| 跨站点互助/链路判读 | otcad-remote-pg-mutual-aid |
| 装 SPM/墙板没数据/日统计 | otcad-spm-deployment |
| 摆挂件/配告警上墙 | otcad-soft-panel-manager |
| 话务票据复盘/导明细 | otcad-ccta-ticket-analysis |
| 优先转接/代接/监听/中继预留 | otcad-special-features |
| 日报自定义图表 | otcad-excel-report-customization |
| 多监督员集中接入 | otcad-ccs-server |
| 建 ACR 对象/技能档案 | 路由入口（otcc-standard-advanced-router） |
| 装脚本编辑器/抓轨迹/清记忆 | 路由入口（深度开发转姊妹技能 otcc-standard-advanced-call-routing） |
| 装 CCS/环境定稿/维护命令 | 路由入口（otcc-standard-advanced-router） |

## 版权

- 本精华长文为 ALE Training Services《OmniTouch Contact Center Standard Edition - Advanced》（OTCCXTE101EN Edition 07）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
