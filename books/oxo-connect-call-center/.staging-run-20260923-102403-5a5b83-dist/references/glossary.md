# GLOSSARY — OXO Connect Call Center 术语表

> 阶段 3 产出（源：candidates/glossary.md，60 条，七大域）。
> 勘误：On Duty 子状态为 8 种（p164）；MLAA/OMC/MMC 全称书中未展开，标待确认。

# OXO Connect Call Center (OXOCXTE107EN Ed07) — 关键术语词典

> cangjie-skill 流水线 glossary extractor 产出。取材方法：无 lexical.sqlite 索引，按规范回退**全量扫描**（source_fulltext.txt，218 页全部通读），所有页码均回原文核验。
> 用途：所有下游 skill 的共享中英对照词典。缩写全称书中未展开处已显式标注"待确认"，不得当作已确认事实。

## 一、ACD 分配域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 首次出处页码 | 相关章节 |
|---|---|---|---|---|
| ACD (Automatic Call Distribution) | 自动呼叫分配 | 集成在 OXO Connect 内的呼叫中心服务（"a Service integrated with the OXO Connect"），经 CSTA 链路驱动寻线组与虚拟终端完成分配；容量 32 坐席 / 8 组 / 16 端口 / 10000 条路由规则 | p23（章节）/ p25（定义） | ACD overview（p23-33）；全书 |
| ACD group | ACD 组（呼叫中心分组） | 呼叫接入与坐席归属的基本单位（最多 8 组），每组有独立 DDI、等待队列、语音提示与邮箱 | p28 | p28, 36-42, 44-51, 89-100, 107-114 |
| ACD port | ACD 端口 | 每组的并发呼叫接入通道（最多 16 个，与 MLAA 共享），标准端口全忙即触发劝漏第二形态；注意不是"坐席数" | p28 | p28, 36, 40, 44, 80 |
| Agent | 坐席 | 接听 ACD 呼叫的资源声明（坐席号、姓名、状态、话机、所属组与优先级），最多 32 个同时活动 | p28 | p28, 51, 75, 117-123, 164 |
| Supervisor | 班长席 | 具有监控与干预权限的坐席角色（可改坐席状态/分组/组状态），对应 Supervisor Console 许可（最多 8 个） | p31 | p31, 46-47, 73, 147-165 |
| Hunting group | 寻线组 | ACD Setup 自动创建的循环（cyclic）模式组，装入 ACD 专用虚拟终端，用于管理坐席状态与 ACD 组接入 | p36 | p36, 77, 82, 85 |
| Virtual terminal | 虚拟终端 | 用户表中代表 ACD 端口/组邮箱的虚拟分机（Media 参数勾选、动态转接至语音邮箱），书注明"don't touch" | p36 | p36, 80-81 |
| CSTA link | CSTA 链路（计算机-电信应用接口，Computer Supported Telecommunications Applications） | ACD 应用引擎与寻线组/话机事件之间的内部连接通道（架构图要素） | p36 | p36 |
| Waiting queue | 等待队列 | 全忙时呼入的排队区（每组一个，上限 16），播等待消息/预计等待时间，主叫按星号键（*）可退出队列转邮箱或号码 | p26 | p26, 38, 93-94, 112 |
| Dissuasion | 劝漏（呼叫劝退） | 队列满或端口全忙时的处理状态：播劝退语音后释放，或改"转接号码/进组邮箱"出口；OMC 界面用词为 "Deterrence" | p26 | p26, 39-40, 92, 113 |
| Overflow | 溢出（组间溢转） | 呼叫在 A 组等待队列超过设定时长（书中例 10 秒）后溢转到邻组的可用坐席 | p96 | p96, 134, 145 |
| Transfer number | 转接号码 | 呼入打到"开放但全员登出/off duty"的组时，第一通电话转往的预定义号码，后续呼叫排队或进劝漏 | p38（队列出口）/ p41（场景） | p38, 41, 97, 112 |
| Rank / Priority order | 坐席组内优先级 / 组间优先顺序 | Rank：坐席在同组内的分配先后（rank 1 最先，Agent parameters 按组设）；Priority order：坐席属多组时检索各组等待队列的组间先后——两者是正交概念 | p75 / p97 | p75, 97, 109-111, 143, 165 |
| Search mode | 搜索模式（选坐席算法） | 组级分配算法三选一：Fixed（固定优先级）/ Rotating（轮转）/ Longest idle（最久空闲） | p95 | p95, 106, 109-111 |
| Maximum ringing duration / Agents that do not answer are automatically removed | 最大振铃时长 / 无应答坐席自动移除 | 振铃超时（实验值 10 秒）转下一位坐席；勾选后者则无应答坐席自动转 off duty 并移出分配 | p110 | p110-111 |
| Call characterization | 呼叫特征化 | 按 CLI（主叫）与 DDI（被叫）把呼入匹配到 ACD 组的机制，三级优先比较：双匹配 > 仅 DDI（CLI 空）> 仅 CLI（DDI 空） | p36 | p36, 86-88, 101, 116 |
| Smart Call Routing (SCR) | 智能呼叫路由 | Line parameters 路由表的菜单名（ACD-SCR Services / Smart Call Routing），按国家/大客户分流呼入，支持 CVS 导入导出 | p74 | p50, 74, 88, 115-116, 144 |
| Line parameters | 线路参数 | 呼叫特征化路由表（最多 10000 行），登记 DDI/CLI 与目标 ACD 组、勾选客户码组；必须从最特殊（最长号码）填到最一般 | p50 | p50, 88, 101, 116, 133, 144 |
| DDI / DID | 直接拨入号码（直线号码） | 外线直拨到内部分机的号码（教材 DDI 表 41100-41199；每个 ACD 组绑定一个 DDI，如 41505-07）；书中 DDI 与 DID 混用 | p21 | p21-22, 50, 70, 82, 86, 128 |
| CLI | 主叫号码（主叫识别） | 来电主叫识别，特征化比较方向从左向右；呼叫转接至坐席过程中显示组名/被叫，接通后显示 CLI | p86 | p86-88, 89, 107, 146, 171, 183 |
| Queue length (N×K) | 队列长度（值机数×话务因子） | 队列长度 = 值机坐席数 N × 话务因子 K（0.1-9.9），非整数向上取整，上限 16 | p93 | p93, 112-113, 184 |
| Estimated waiting time | 预计等待时间 | 队列播报的估算值 =（队列呼叫数 ÷ 值机坐席数 + 1）× ACD 平均通话时长 | p38（消息）/ p94（公式） | p38, 94 |
| Opening hours / Exceptional days | 营业时段与例外日 | 每周开放时段（每日最多 2 个时段）；例外关闭日最多 40 天、例外开放日最多 10 天，可按组定义 | p37（时段测试）/ p100（规格） | p37, 91, 100, 108, 134, 145 |
| Client identification (DTMF customer code) | 客户识别（DTMF 客户码） | 来电者输客户码（如 035#）触发坐席席面弹屏客户资料；需在 Line parameters 勾选该组并给坐席弹屏权限 | p101 | p101-102, 171, 183 |
| Call qualification | 呼叫定性（通话后分类打标） | 坐席通话后用 Types 表预定义代码给来电归类供统计；是"通话后打标签"，非实时质检 | p99（概念）/ p168（术语） | p99, 168, 180-183 |
| ACD Setup | ACD 设置向导 | OMC 助手一次成型：端口数、状态前缀、组与 DDI、组邮箱、按键 profile、坐席/班长声明；完成后需重启 ACD 引擎 | p43 | p43-48, 70-73, 128-131, 141-143 |
| ACD Services | ACD 服务菜单 | 向导之外的精调菜单：Line parameters、Agent parameters、General parameters、ACD Voice messages 等 | p49 | p49-52, 74-76, 107-114, 132-135 |
| MLAA | 多线自动话务员（全称书中未展开，待确认） | 与 ACD 端口共享端口数资源的特性（"Ports number, shared with MLAA"）；其语音引导在培训收尾时需清除 | p44 | p44, 211 |

## 二、坐席状态域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 首次出处页码 | 相关章节 |
|---|---|---|---|---|
| On duty | 值机（就绪） | 坐席可接听 ACD 呼叫的主状态（前缀 501）；在 Supervisor 应用中细分为 8 种子状态 | p70 | p70, 77, 122-123, 154, 164, 172, 183 |
| Off duty | 退勤（离线） | 坐席不参与分配的主状态（前缀 502）；全员登出/off duty 触发"转接号码"场景 | p36（场景）/ p70（前缀） | p36, 41, 70, 111, 123 |
| Clerical work | 文书工作（话后整理） | 通话后暂离分配做整理工作（如写报告）的主状态（前缀 503） | p70 | p70, 77, 154, 164, 172 |
| Temporary absence | 暂时离开 | 短暂离席（如休息）的主状态（前缀 504） | p70 | p70, 77, 154, 164, 172 |
| Free seating | 自由座位（流动坐席） | 坐席在任意话机拨登录前缀/按 ACD 键登录，终端+坐席+组+坐席名建立关联即进入 ACD 会话（terminal↔agent 动态绑定） | p120 | p120-121, 168-170 |
| Login / Logout | 登录/登出（签入/签出） | 进入/退出 ACD 会话：登录按坐席名（8/9 系 IP 话机）或坐席号（模拟/DECT），可要求坐席密码 | p117（章节）/ p119 | p117-123, 138, 141 |
| ACD prefix (base 0 / base 1) | ACD 前缀（登出/登录码） | 内部编号计划中的功能前缀：base 0 = 登出，base 1 = 登录 | p120 | p120-121, 146 |
| ACDAutoLog | 登录默认状态寻址项 | 隐藏寻址项（非常规菜单）：01 = 登录后默认 on duty（默认值），00 = 登录后默认 off duty | p123 | p123 |
| ACD tab / 组状态码 | 话机 ACD 标签页与状态码 | Premium 8/9 系话机 ACD 菜单；状态码如 1:01 = 属组 1 开放且队列 1 通，1:01+ = 队满，1-00 = 组 1 关闭（排障依据） | p122 | p118, 120, 122, 138 |
| On duty 八种子状态 | 值机子状态 | Supervisor 应用实时显示：Awaiting call / Not answering / Being routed / Ringing / ACD busy / On hold / Busy, outgoing call / Not available | p164 | p164 |

## 三、应用域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 首次出处页码 | 相关章节 |
|---|---|---|---|---|
| PIMphony | PIMphony 软终端 | 用于话务处理的 PC 软电话（PIMphony IP 可作坐席终端），可与 Agent 应用交互 | p29 | p29-30, 33, 168 |
| Agent application | 坐席应用（Agent Assistant） | 坐席席面软件：状态管理、free seating、呼叫定性、实时个人统计、弹屏管理，基于 PC-终端关联架构 | p29 | p29, 166-184 |
| Supervisor application | 班长应用 | 实时监控呼叫中心活动（坐席/组的活动率、状态），并可同时修改参数、坐席状态/分组与组状态的班长台 | p29 | p29, 147-165 |
| Statistics application | 统计应用 | 报表工具：组/坐席统计（图/表）、手动与自动打印、binary/CSV 导出；统计文件存于主 CPU，留存最多 14 个月 | p29 | p29, 185-209 |
| Screen popup | 屏幕弹出（弹屏） | 来电时按主叫/客户码自动弹出联系人资料，需给坐席 "automatic screen pop up" 权限 | p102 | p101-102, 168, 175-176, 183 |
| Integrated contact database | 集成联系人数据库 | Agent 应用内置客户档案库（"Integrated mode" 下每坐席本地独立），按主叫号码匹配弹出 contact file | p175 | p175-176, 178, 183 |
| OMC | OMC 管理软件（全称书中未给出，一般即 OXO 管理控制台，待确认） | 全书配置操作的主入口（Easy view 会话），安装后经 LAN/WAN + 服务器证书连接 OXO | p43 | p43-64 及全书 |
| Easy view / Expert mode | 简易视图 / 专家模式 | Easy view：菜单式管理会话（ACD 菜单所在）；Expert mode：OMC 首次连接系统所用模式（勾选服务器认证） | p43 / p59 | p43, 49, 52, 59 |
| Installer password | 安装员密码 | OXO 安装级密码（教材默认值 pbxk1064，仅首次登录用），不应暴露给最终客户 | p55 | p55, 59, 150, 188 |
| ACD Admin password | ACD 管理密码 | Supervisor/Statistics 应用专用密码（教材实验值 Acdc1064），在 OMC 密码管理中设置，替代 installer 密码 | p150 | p150, 162, 188, 205 |
| Operator password | 话务员密码 | Agent 应用用户权限管理入口（Admin 账户）的访问保护密码 | p177 | p177 |

## 四、Multi-Secretary 域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 首次出处页码 | 相关章节 |
|---|---|---|---|---|
| Multi-Secretary (mode) | 多秘书模式 | 基于 ACD 引擎（需许可）的"多经理共享秘书"形态：振铃时话机显示 [被叫组名/号码][主叫][等待时长]，接通后显示 CLI | p89 | p89, 124-146 |
| Collective speed dialing | 集团缩位拨号 | 把经理 DDI 对应登记成名字（如 DOCTOR A），秘书话机即显示被叫姓名而非号码 | p137 | p137, 140, 144 |

## 五、语音域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 首次出处页码 | 相关章节 |
|---|---|---|---|---|
| Voice guide / ACD voice prompts | 语音引导（ACD 语音提示） | 每组 6 条提示按 wav 编号管理（101=欢迎语、102=等待语…107=客户码提示），可经终端 MMC 录制或 OMC Transfer 模式批量上传 | p35（章节）/ p52（菜单） | p35, 52-53, 76, 104-105, 135-136, 146 |
| MMC session | 话务台（MMC）会话（缩写全称书中未展开，待确认） | 在 8/9 系话机的 Attendant session 里录制 ACD 语音的会话（Menu/Operator/密码 OP/Expert/Voice/ACD） | p104 | p104, 135-136, 146 |

## 六、实验环境域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 首次出处页码 | 相关章节 |
|---|---|---|---|---|
| RLAB | 远程实验室（Remote LAB） | ALE 数据中心托管、全虚拟化的远程实验环境，学员经 Portal/RDP/Web 控制台接入 | p3 | p3-7, 55, 66 |
| POD | 实验舱（培训单元） | RLAB 中相互独立、配置相同的学员单元（OXO + 客户机，192.168.1.x 网段），共享公共资源 | p5 | p5-11, 18-22 |
| NAS | 网络存储（软件/许可库） | POD 公共资源：存放系统版本、发行包与客户端软件，客户机映射网络驱动器免密访问 | p5 | p5-6, 9, 15 |
| SIP Simulator (ITSP1 / ITSP2) | SIP 运营商模拟器（模拟网络电话运营商） | RLAB 公共区模拟公网：ITSP1 网关与账号（pbxP@itsp1.fr）模拟国内/国际/移动/紧急号码，号码规则含两位 POD 号 PN | p5 | p5-6, 17-22 |
| MicroSIP | MicroSIP 软终端 | 客户机预装的 SIP 软电话：4 个模拟内线 100-103、2 个模拟公网主叫 | p9 | p9, 18-19 |
| SIP trunk group | SIP 中继组 | OXO 侧指向 ITSP1 的中继配置（SIP Gateway ITSP1G1、SIP 域、账号 pbxP、DDI 表 41100-41199） | p18 | p18-22 |
| S1 / S2 hold-on threshold | S1/S2 等待时长阈值 | 统计应用对等待时长的分类阈值（默认 10 秒/40 秒），另有"溢出前等待时延"开关 | p190 | p190 |

---

## 覆盖率自检

**任务书七大域核对**（共 60 条）：

- [x] ACD 域：ACD、ACD group、ACD port、agent、supervisor、hunt group、virtual terminal、queue、dissuasion、overflow、transfer number、rank/priority、search mode、call characterization、Smart Call Routing、line parameters、DDI/DID、CLI —— 全部收录（含 CSTA link、队列公式、最大振铃/无应答移除合并条）
- [x] 坐席状态域：On duty、Off duty、Clerical work、Temporary absence、free seating、login/logout、ACDAutoLog、八种子状态（p164 实际列出 8 种，任务书称"九种"系把 Off Duty/Clerical work 等主状态并入计数，本表按原书 p164 口径收录 8 种子状态并单独收录 4 主状态）—— 全部收录
- [x] 应用域：PIMphony、Agent application、Supervisor application、Statistics application、screen popup、call qualification、integrated contact database、OMC、Easy view、Expert mode —— 全部收录（Easy view 与 Expert mode 合并为一条）
- [x] Multi-Secretary 域：Multi-Secretary mode、collective speed dialing —— 全部收录
- [x] 语音域：voice prompt/guide、ACD Voice messages、MMC session、107.wav 客户码提示 —— 全部收录（wav 编号规则并入语音引导条）
- [x] 环境域：RLAB、POD、SIP Simulator、ITSP1/ITSP2、MicroSIP、SIP trunk group、NAS —— 全部收录
- [x] 密码域：installer password（pbxk1064）、ACD Admin password（Acdc1064）、Operator password —— 全部收录；密码具体值属实验环境口径，生产环境必须修改（对应 BOOK_OVERVIEW 批判项）

**有意不收录**（宁缺毋滥原则）：
- 一次性出现且无术语价值的操作细节：OMC 安装步骤、证书安装、IP 修改（192.168.1.x 规划）、RLAB Dashboard 操作、培训评估流程（p212-218）、Cold Reset（p211，属边界提示）
- 组呼叫信令模式（"Group called with signalization mode"，p85 仅一次出现，作配置检查项而非概念）
- 自动打印（automatic printout，p200-201）与 binary/CSV 导出（p202）：已并入 Statistics application 条的定义，不单独成条
- Welcome/Option 许可包（p31）：属商务清单而非术语，已并入 Supervisor 条的许可语境

**已标注待确认**（书中缩写未展开，不得编造全称）：MLAA（p44）、OMC（p43）、MMC（p104）。
**跨条目口径提示**：Dissuasion 的 OMC 界面英文为 "Deterrence"（p113）；书中 DDI 与 DID 混用同义；"1:01 无 + 号"两种话机显示原文排印不清（p122），下游引用时以"属组开放与否"语义为准。
