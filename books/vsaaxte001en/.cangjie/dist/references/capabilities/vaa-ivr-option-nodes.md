# VAA IVR 选项节点与动态脚本（变量/收号/显示名/HTTP/邮件、九节点全集）

## R — 原文依据

> "Options subject to licenses allowing the VAA server to be connected to an information system"（p203）
> "Local: The variable is created when the script (tree) is launched … Global: the variable is created at company level … Contextual: a context variable is a variable linked to the current call. These variables are predefined and cannot be modified."（p216）
> "An empty result does not generate an SQL error … The VAA can only recover one field at a time. … In case of multiple results, the VAA returns the first occurrence only."（p323）
> "The information collected must imperatively be stored in a variable for future use"（p222）

出处：VSAAXTE001EN p203-238, p215-220。

## I — 自述

IVR 选项是"让 VAA 连接信息系统"的节点族（9 种，全部另购 IVR 许可），四个知识块：

1. **九节点清单**（全部另购 IVR 许可）：

   | 节点 | 要点 |
   |---|---|
   | Custom display name | 监督转接振铃期屏显 |
   | Collect digit | 收号存变量 |
   | Speech recognition | 识别结果存变量 |
   | SQL request | 外部库 SELECT/INSERT |
   | Correlator data | SIP 帧注入 User-to-User 相关数据（Magic ID 0xC015、ASCII 最长 27 字节 + XOR 校验、OXE 振铃期显示呼叫标签） |
   | Condition | 变量比较路由 |
   | HTTP request | GET/POST/PUT/DELETE，可配头与出站代理 |
   | Mail | 脚本内发邮件（SMTP/SMTPs） |
   | Set variable | 声明/赋值变量 |
2. **变量三类**：Local（脚本启动时创建，仅本 VAA 线可见）、Global（公司级全树共享，适合免改脚本调参）、Contextual（呼叫上下文预定义只读，如 callingNumber，清单在管理指南）；变量是 SQL/HTTP/收号/TTS 四类节点的必需品
3. **节点行为细则**：

   - Condition 比较算子（Is empty/Contains/Equals/Starts with/End with/length 等，可比较另一变量）
   - 收号节点（min=max 时位数不足判失败、单独输入 * 视为正确输入、# 结束符不可改、结果必须存变量）
   - 显示名（仅监督转接、仅振铃期、摘机即恢复主叫信息、需 OXE 侧 COS 配合）
   - HTTP 返回 JSON 按点语法取值（VAR(变量.对象.字段)）
4. **SQL 节点硬规则**：一次只取一个字段（多字段发多条请求）；多条结果只取第一条；空结果不算错（必须用 Condition 判非空再转接，SQL 失败走红色连线）；脚本里塞太多查询会拖长呼叫时长；库连接应定义在公司设置而非节点手工配置

## A1 — 书中案例

**变量判断树（31404）与 HTTP 天气树（31407）**（p215-235，实验口径 token）：

1. 建树，Start 自动生成；加 Set variable 节点复制上下文变量 callingNumber
2. 加欢迎 Announcement，接 Condition 判断主叫以 31 开头（内部来话）
3. 内部分支接 TTS 播报 "Internal Call"；继续 Condition 判断是否等于 VIP 号码
4. VIP 分支播 "VIP call"，其余播 "Other calls"；Release 收尾；绑 31405 前先按此树验证变量链
5. HTTP 实验：openweathermap 免费但需注册取 tokenID（实验提供两枚）
6. 建 HTTP 节点请求天气接口，结果存变量 resultHTTP
7. 播报节点用 VAR(resultHTTP.main.temp) 与 VAR(resultHTTP.main.humidity) 取值
8. 绑测试号激活；拨打应播报布雷斯特实时温度与湿度

## A2 — 未来触发

使用情境：按主叫属性分流；自助查询采集工号/PIN；转接时屏显自定义信息；通话中调外部接口；来话邮件通知；按数据库数据转接前的变量准备；ASR 识别节点。

语言信号：变量 / variable / Local / Global / Contextual / callingNumber / Condition / 收号 / collect digits / 显示名 / display name / HTTP / JSON / VAR / 邮件节点 / mail / 相关数据 / correlator / IVR 许可。

与相邻能力区分：JDBC 驱动安装与库连接归数据库集成能力；TTS 文本生成归语音资产能力；树画布与路由绑定归树设计能力。

## E — 可执行步骤

输入契约：IVR 许可已购（vaa services 的 VAA_IVR 字段核查）、变量规划（取哪些上下文变量、存哪些结果）、外部服务可达性（HTTP/SMTP）、收号业务的输入长度与异常策略。

1. 核查许可：vaa services 看 VAA_IVR [true/false]，未购则停。完成标准：许可就位
2. 变量规划：列出每个节点读取/写入的变量与类型（Local/Global/Contextual）。完成标准：变量表评审通过
3. 建树骨架：Start/欢迎/业务节点/Release 先行，逐节点连线并命名。完成标准：主干可走通
4. 接入选项节点：按需加 Set variable/Condition/Collect digit/HTTP/Mail 等，结果一律存变量。完成标准：节点参数完整
5. 异常路径：收号配错误输入与超时处理；SQL/HTTP 失败走红色连线播专用提示。完成标准：每条异常连线有落点
6. 路由激活：绑测试号并激活，按行为测试清单拨打（含 * 输入、位数不足、超时等边界）。完成标准：清单全过
7. 演进：显示名文本可改变量动态生成；收号可改造为可变长度输入。完成标准：进阶项按需启用

判停点：

- SQL 要一次取多个字段 → 停，单字段限制下拆成多条请求，或评估树结构（原书进阶题即 2 条 SQL）
- 收号要把 * 当返回键 → 停，* 被视为正确输入，需自行加 Condition 判断其值
- 客户无 IVR 许可要上收号/SQL 节点 → 停，全部九节点都是付费选项，先走商务
- 显示名在盲转场景不显示 → 停，机制仅限监督转接振铃期，需求改用播报或改转接策略

输出契约：激活的动态脚本树 + 变量表与节点参数记录 + 边界行为测试记录。

## B — 边界

- 九节点全部依赖 IVR 许可（Additional licenses），HA 许可也列在 Option 栏（p21/p26）
- 收号三细节：min=max 判失败、* 是合法输入、# 结束符不可改（n36）
- 显示名三边界：仅监督转接、仅振铃期（摘机即恢复主叫信息）、需 OXE COS（n35）
- SQL 安全口径：库连接定义在公司设置，不要节点手工配置，防凭证散落脚本（n24）
- Correlator data 的 Magic ID 与字节上限为 SIP 私有机制，OXE 侧解析前提书内未展开
- HTTP 出站走客户网络，代理与防火墙前提属客户基础设施（p34 口径）
