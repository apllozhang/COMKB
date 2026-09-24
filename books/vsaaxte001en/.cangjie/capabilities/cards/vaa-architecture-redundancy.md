# VAA 架构与冗余全景（组件族、呼叫流、multi-company、N+1、OXE 冗余三用例）

## R — 原文依据

> "VAA is connected to the OmniPCX Enterprise using a SIP trunk of ABC/F Type … Management application access is secured using https over TLS 1.2 … Note: G729 can't be used with Automatic Speech Recognition feature"（p42）
> "1 The calling party calls the company welcome number through the public network 2 OmniPCX Enterprise routes the call to the Visual Automated Attendant via a SIP trunk 3 The Visual Automated Attendant runs the script associated to the called number … 4 The Visual Automated Attendant routes the call to the destination through the OmniPCX Enterprise in blind transfer."（p43）
> "In case of failure of master VAA, the SIP trunk is established between the main call server and the slave VAA. … Web client must reconnect (to Slave VAA)."（p47）
> "The Visual Automated Attendant Media Server is shared by all companies • It's not possible to reserve ports for a given company"（p50）

出处：VSAAXTE001EN p41-51。

## I — 自述

方案沟通与排障分流的概念底座：

1. **组件族七件**：

   - aa-license-server（FlexLM 许可）、aa-media-server（与 OXE 的 SIP 连接 + RTP 栈 + 跑脚本）、aa-cli（命令行）
   - aa-webapp（Tomcat，承载 aa-management 管理界面与 aa-engine 引擎，引擎与 media-server 协作取脚本）
   - PostgreSQL 16（提示音/路由策略/统计）、Nginx（HTTP 反向代理）、tts-hub（TTS 与识别服务接入）
2. **四步典型呼叫流**：公网呼入公司欢迎号，OXE 经 ABC/F 型 SIP 中继送 VAA，VAA 执行被叫号绑定的脚本（放音/收号），再经 OXE 转接落地（分机/留言箱/话务员）

   - 管理流量走 HTTPS/TLS 1.2；CMIP 链路同步 OXE 电话簿
   - 编解码 G711（aLaw/µLaw）与 G729（与 ASR 互斥）；SIP 中继可加密（SIP TLS/SRTP 可选）
3. **multi-company 集成**：VAA 支持 OXE 多公司功能（细节外置 TBE083）；媒体服务器被各公司共享，不能为单一公司预留端口；SIP 中继属公共公司
4. **N+1 冗余（扩容型）**：一台 reference VAA 作配置基准（脚本/提示音/日历等复制到其他 VAA，各自统计除外）；ARS 按 N+1 原则把呼叫分给可用 VAA；单 VAA 故障期间总容量下降；reference 挂了其余照跑但全系统配置冻结——与 Master/Slave（冗余型）是两种结构
5. **OXE 冗余三用例（讲义级）**：呼叫服务器切换（中继在新主上重建、进行中呼叫丢失）；主 VAA 丢失（中继切到 Slave、Slave 只读无统计、恢复后不自动回同步、Web 需重连）；WAN 断（复制停止）；空间冗余要求第二数据中心部署 Slave，Purple On Demand 不支持

## A1 — 书中案例

**主 VAA 丢失用例推演**（p45-48 讲义，无实验）：

1. 正常态：OXE 经 trunk group 1 把呼叫送 Master，库向 Slave 复制
2. 故障注入：Master VAA 宕机
3. OXE 侧：主呼叫服务器与 Slave VAA 之间建立 SIP 中继
4. 呼叫面：新呼叫由 Slave 接续执行脚本
5. 配置面：Slave 库只读，不能改配置
6. 统计面：故障期间 Slave 处理的呼叫不产生统计
7. 恢复面：Master 回来后不自动回同步，Web 客户端要手动重连
8. 结论：三用例中任何切换都丢进行中呼叫（原书三处重复）

## A2 — 未来触发

使用情境：向客户解释 VAA 与 OXE 的分工；方案里要"端口保底"；评估 N+1 与双机怎么选；OXE 侧做冗余改造时问 VAA 受什么影响；排障时分清组件归属；看架构图对不上组件名。

语言信号：架构 / architecture / 组件 / aa-media-server / aa-webapp / aa-engine / Nginx / PostgreSQL / tts-hub / 呼叫流 / call flow / ABC-F / CMIP / multi-company / 多公司 / N+1 / reference VAA / 冗余 / 空间冗余 / 端口预留。

与相邻能力区分：双机部署与切换测试的操作归 HA 能力；PCS 远端分支归 PCS/OPEX 卡；OXE 侧冗余改造的实施归 OXE 工程（书外，TC2462 系文档）；产品功能清点见各业务能力卡。

## E — 可执行步骤

输入契约：客户拓扑（单 OXE/多公司/多站点）、可用性诉求（防什么故障）、容量诉求（是否要扩容型）、商务模式（CAPEX/OPEX）。

1. 分工讲解：用四步呼叫流说明 OXE 管呼控、VAA 管脚本执行。完成标准：客户认可分工图
2. 结构选型：防单机故障选 Master/Slave；同 OXE 扩容选 N+1；两者不混谈。完成标准：结构结论
3. 冗余推演：按三用例逐项过（丢话/只读/统计缺口/不回同步），给客户立预期。完成标准：预期书面确认
4. 多公司评估：确认"端口不能按公司预留"是否可接受；细节引 TBE083。完成标准：多公司边界签认
5. 组件排障分工：按组件族图定位日志归属（SIP 连接归 media-server、界面归 aa-webapp 等）。完成标准：排障分流表可用

判停点：

- 客户要"给 A 公司保底 20 路 IVR" → 停，媒体服务器共享不支持预留，只能扩容或拆 VAA 变通（拆分边界书内未展开）（n07）
- 客户把 N+1 当站点容灾 → 停，N+1 是同 OXE 扩容结构，跨站点是空间冗余且与 OPEX 互斥（n06/n08）
- 客户预期切换不掉话 → 停，三用例口径：任何切换丢进行中呼叫（n05）
- 问 ABC-F 信令原理或 OXE 冗余实施 → 停，OXE 侧原理书外，指向 OXE 文档体系

输出契约：架构分工说明（含呼叫流）+ 冗余结构选型结论 + 三用例预期管理清单 + 组件排障分流表。

## B — 边界

- 三用例均为讲义级无实验；教材场景是单 OXE + 双 VAA 最小闭环，跨站点无实验
- multi-company 只有一页概念，配置细节全在 TBE083 与 OTEC-S 指南（n50）
- N+1 中"各自统计除外"的统计聚合口径书内未展开
- PCS 的断网接管是另一机制（外围站点），与三用例、N+1 并列，勿混谈
- SIP TLS/SRTP 加密为可选项，实验全程关闭；加密交付无实验路径
- "Slave 不是热备"等定性表述带推断标注（nr-07），行为依据为原文
