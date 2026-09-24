# GLOSSARY — OmniTouch Contact Center Standard · Advanced 术语表

> 阶段 3 产出（源：candidates/glossary.md，56 条，六大域；本门户版精选高频约 40 条）。
> 口径：定义只采信本书正文；ABC-F/RSI/CSTA/MAO/OMS/GD4/TSC/COS/IPDSP/EWT/MWT/ITSP 等缩写书中未给全称，如实标注不编造。

# OmniTouch Contact Center Standard · Advanced (OTCCXTE101EN Ed07) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（597 页），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| ACR | 高级呼叫路由 | CCD 的选项：按技能、上次应答坐席等条件路由；需 ASM 软件且必须建等待室 | p63-78, p161 |
| ASM | 坐席选择模块（Agent Selection Modul，书内拼写） | 处理 ACR 呼叫的软件服务器：算坐席列表；内置（alb 进程）或外置 Windows | p66-70, p161 |
| ISM | 个性化技能匹配 | ACR 最常用规则子程序：按呼叫档案与坐席技能匹配出坐席列表 | p67, p160-181 |
| LCA | 最后应答坐席规则 | 从 ASM 记忆取"上次应答该主叫的坐席"；alb 重启清记忆，MAIN_AFE 重启不清 | p246-259 |
| CCD | 呼叫分配程序与矩阵对象体系 | OXE 上的分配程序（AFE 即 CCD 程序）：Pilot/队列/等待室/处理组/方向 | p19-38, p161 |
| CCsupervision（CCS） | 监督与管理客户端 | 配置/实时/统计/脚本编辑器四区一体；多客户端接入经 CCS Server | p39-47, p94-115 |
| AFE | Alcatel Front End Server | OXE 侧承载 CCD 的前端程序；物理连接上限 15 条 | p45, p68, p557-558 |
| alb / ALB | 坐席列表构建进程 | Call Server 上承载内置 ASM 的进程：算列表（默认最多 200）、跑 .alb、存 LCA 记忆 | p161, p172, p198, p272 |
| Pilot（路由 Pilot） | 路由入口对象 | 有等待室方向或挂激活规则即为 ACR Pilot | p81, p123, p134-136 |
| Statistics pilot（统计 Pilot） | 统计入口对象 | 客户实际拨的号：挂路由 Pilot、call tag、呼叫优先级、呼叫档案 | p123, p136, p162 |
| Waiting Room（等待室） | ACR 专用等待对象 | 非 FIFO、按呼叫档案挂动态组、与等待队列同规则互斥；迎宾+6 泊位、40 种语言 | p71-72, p82, p119 |
| Dynamic group（动态组） | ASM 生成的坐席列表实体 | 等待室下游按呼叫档案动态生成，故无资源选择优先级管理 | p71, p83, p88 |
| Call tag（呼叫标签） | 呼叫业务标记 | IVR 打标/转接携带/CSTA 字段；LCA 记忆索引与调试器过滤依据 | p74-76, p123 |
| Call profile（呼叫档案） | 呼叫技能需求清单 | 最多 7 属性（特征+域+技能+要求等级+强制/可选），挂统计 Pilot | p74, p122, p163-164 |
| EWT / MWT / TSP | 预期等待/最大等待/话务采样期 | EWT 用于方向裁决与饱和判定；MWT 0-3276 秒（0=零等待队列）；TSP 2-15 分钟 | p81-82, p86, p365 |
| Mutual aid（互助） | 跨节点溢出 | 盲互助无 ABC-F；智能互助按远端状态路由，拒收按五类回退本地 | p293-315 |
| Dissuasion（劝阻） | 饱和劝退 | 播劝阻引导或忙音/间隔引导音；LCA 状态码 1 即"送入劝阻队列" | p253, p500, p520 |
| Wrap-up / Eternal wrap-up | 整理态/永恒整理 | 事后处理状态；永恒整理=整理期内可办电话事务不打断计时 | p58, p346, p510 |

## 二、角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Agent | ACD 坐席 | 挂处理组、带技能集（1-9 级+激活标志）、自助/被助登录 | p33-35, p53-56, p124 |
| Supervisor | 班长/监督员 | CCS 权限逐项授予（ACR 与 ACR Data 两项）；话机侧秘密监听/插入 | p98-101, p511-512, p528 |
| Self-assigning agent | 自助登录坐席 | 登录时点 List 选处理组；非自助型直接进偏好组（Preferred GT Agents） | p54-55, p144, p361 |
| mtcl | OXE 维护账户 | WBM/console/CCTA 导入的维护级账户（口令为实验约定值） | p9, p51, p272 |

## 三、订阅/许可域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Feature level license | CCS 许可形态 | 安装时选 Monosite（单站点）或多站点；运行期 Licenses 页可见令牌 | p42, p562, p574 |
| CCS 软件包（Mono/Multi/Light） | CCS 接入包 | adm_acd option 15 中 Mono/Multi/Light 各 max=120 | p405 |
| RTI license（103 号包） | 实时接口许可 | RTI Connector 的 OXE 侧前提（WBI Licence max=100）；spadmin 或 option 15 核对 | p388, p405 |
| Soft Panel Manager 许可族 | SPM FlexLM 四证 | 主许可+按显示端计+业务数据接口+内部用；失效即冻结统计更新 | p388 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniTouch Contact Center Standard | OTCC 标准版 | CCD 矩阵+CCS+ACR/ASM 选项+互助+SPM/CCTA 外围；本书版本 R10.15 | p1, p377 |
| OmniPCX Enterprise（OXE） | 企业通信服务器 | 承载 CCD/AFE、Direct IP Link、SIP 中继；A4300M/L 亦可作 ABC-F 中转 | p7-9, p82, p302 |
| Soft Panel Manager（SPM） | 实时统计上墙方案 | Tomcat Web 应用（wbm/9060）+显示端+邮件告警+业务数据接口；限 500/150/200 | p371-383, p394 |
| RTI Connector | 实时取数 Windows 服务 | 连 CCS 与 SPM：断连 5 秒重试、按需订阅（1 分钟生效）、同机时 CCS 须专用 | p377, p396-411 |
| FlexLM Server | 许可服务器 | LMTOOLS 管理，默认 localhost:27000；SPM 运行期持续校验 | p7, p388, p408-411 |
| Contact Center Ticket Analyser（CCTA） | 票据离线分析工具 | Importation 导入 .Z + Ticket Tracer 过滤导出 ASCII | p480-497 |
| CCS Server（serv_ccs） | CCS 集中接入服务器 | 内部=OXE 进程（15 客户端）；外部=Windows 服务（120 客户端）；一 AFE 一 Server | p555-590 |
| MicroSIP / IPDSP | 实验软话机两类 | 三内部分机+公网模拟 / 坐席软话机（分机+个人码注册） | p10-11, p52-55 |
| ITSP1 | SIP 运营商模拟器 | RLAB 公共区模拟运营商：网关注册+号码变换（3321PN 系列） | p15-18 |
| RLAB | 远程实验平台 | POD 池相互独立同构，公共 Pod 提供 NAS 与 SIP 模拟器 | p3-14 |

## 五、协议域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| ABC-F | 节点间网络链路协议（全称未展开） | 承载智能互助的 ACD 信息交换；中转节点须透明支持 | p36, p299-313, p341 |
| H.323 / RTP | 节点间话音协议族 | compvisu sys 输出：H323、RTP Direct、Fast Start、VAD/CNG | p341-342 |
| CSTA | 呼叫标识字段来源（全称未展开） | 与 CLID、被叫号码、呼叫标签并列的呼叫特征化信息源 | p74 |
| JMS / ActiveMQ | 业务数据推送通道 | 外部 KPI 经 JMS 推给 SPM（ActiveMQ 实现）；防火墙端口 61618 | p378, p387 |
| SSH | 安全壳通道 | CCTA 导入按 OXE 实际开启情况勾选（实验未开启） | p50, p493 |

## 六、资源/工具域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Processing Group（处理组） | 呼叫分配落点 | Type=Agent/IVR/Other/Remote/Rerouting；Remote 有门限+资源优先级 | p133, p318-320, p344 |
| Voice guide（语音引导） | 语音资源 | 等待室迎宾+6 泊位；PG 型引导（如 685）可设扩散次数后释放 | p82, p366, p368 |
| Trunk Group / Time Slot | 中继组与时隙 | SIP 接入计（实验 2×31=62 条）；业务预留与 Pilot 限额两级切分 | p307, p513-514 |
| ACD prefix（ACD 前缀） | 坐席功能码总开关 | 建 CCD 对象前必须先建（实验=12）；无屏话机靠前缀+数字操作 | p346, p360 |
| Prefix plan / DID translator | 编号翻译资源族 | DID 翻译器、网络前缀、ACD 前缀、功能前缀（#013/#014）、录音前缀 | p57, p335, p503-504 |
| adm_acd / agacd 等命令族 | ACD 维护命令箱 | 对象清单/坐席统计 -salb 21/ASM 记忆 -salb 28/服务器接入 -servccs 10 | p127-128, p176, p257, p336 |
| Inter-guide tone（间隔引导音） | 拥塞音信号 | 队列拥塞且无劝恼时送默认 2 号音；与 DID 忙音参数配合决定听感 | p500, p521 |
| Navigator | CCS 实时视图工具 | 多 Tab 定制（对象显隐+实时参数），连通验证与排障的观察抓手 | p47, p147-148, p237 |

---

## 收尾自检

- 门户版收录 40 条（六大域），全部映射自 candidates/glossary.md g01-g56；未入选的 16 条（g22 事务码、g23 MCDU、g28 单列、g31 单列、g34 OMS、g35/g36 部分合并、g39 单列、g42/g43 合并、g45-g48 协议部分、g49-g56 部分合并）在完整版 glossary 候选中可查，无信息丢失。
- 书中未给全称的缩写一律不编造 full_name；p236 "31650"、p558 "29 or 120"、LAST_CALL_ 命名混用等已知问题见 needs-review.md（nr-01/nr-02/nr-03）。
