# Agent 坐席席面部署（OXO Connect）

## R — 原文依据

> "Architecture based on PC / Terminal association ... Association PC 1 + Ext. 2001"（p169）
> "Once an ACD incoming call is routed to an agent using the Agent application, the agent can tag this call according to the kind of call they are involved with"（p99）
> "A screen popup should appear as soon as the call is distributed"（p183）

出处：OXOCXTE107EN p99, p166-184。

## I — 自述

Agent 席面是坐席的 PC 工作台，架构是 **PC 绑定话机**。四个要点：

1. **来话信息**：CLI、DID、所属组、来话组名、等待+振铃耗时、通话时长、客户码入口
2. **部署顺序**：先在 OMC 的 Types 表定义通话分类码（事后打标供统计）→ 装应用（MyPortal 下载 Agent_assistant）→ 首连
3. **连接三要素**：OXO IP + 关联分机号 + 可管理该分机的坐席名单
4. **功能验证四件事**：状态切换（Supervisor 台交叉核对）、改所属组、客户库弹屏、来话打标

权限由 Admin 账户管理（受 OXO Operator 密码保护）。

## A1 — 书中案例

**部署实验**（p181-184，厂商实验，PC 绑定话机 102）

- Types 表定义分类码
- 安装并首连（192.168.1.246 + 分机 102）
- 状态切换：On duty / Clerical work / Temporary absence → Supervisor 台核对
- 组变更：席面改所属组 → Supervisor 台核对
- 弹屏：Customers data base → Edit → New 建联系人（姓/名/电话），用该号码呼组2，弹屏出现
- 打标：来话接听后右侧下拉选分类码
- 队列联动：组1 的 K 从 0.1 改 2.0 → 席面观察队列容量 1 → 4（与公式吻合）

## A2 — 未来触发

使用情境：坐席要在电脑上接听管理来电；来话要弹客户资料；通话要分类打标供统计；坐席软件重装。

语言信号：坐席软件 / agent application / 弹屏 / screen popup / 打标 / 分类码 / 客户库 / 来电资料。

与相邻能力区分：来电者输 DTMF 码触发的弹屏 → DTMF 弹屏能力；坐席登录签出 → 签入签出能力；本能力是席面软件本体部署与验证。

## E — 可执行步骤

输入契约：坐席 PC 与话机分机对应关系、分类码定义、客户资料样例（验证弹屏）。

1. 定义分类码：OMC / ACD-SCR Services / General Parameters / "Types" tab。完成标准：码表可用
2. 安装：下载解压 → setup.exe。完成标准：安装完成
3. 关联与首连：服务器 IP + 关联分机号 + 语言 → Connection。完成标准：席面登录（三要素缺一先补配）
4. 状态验证：切状态 → Supervisor 台核对。完成标准：实时同步
5. 组变更验证：席面改组 → Supervisor 台核对。完成标准：组列表更新
6. 弹屏验证：建联系人 → 用该号码呼入 → 弹屏出现。完成标准：弹屏正确
7. 打标验证：来话后下拉选分类码。完成标准：标记保存
8. 队列联动（可选）：改 K 值观察席面队列容量变化。完成标准：与公式一致

输出契约：可用坐席席面 + 分类码表 + 弹屏/打标验证记录。

## B — 边界

- p183 原文 "agent 1002" 疑为话机 102 笔误，操作以实际关联分机为准
- 席面弹屏两路：客户库按 CLI 匹配（本能力）与 DTMF 码触发（另一能力）——排查"不弹屏"先分清哪一路
- 权限入口受 Operator 密码保护；密码遗失走设备管理流程（原书未覆盖）
- 与 PIMphony 的集成原书仅提及可行，细节未展开
