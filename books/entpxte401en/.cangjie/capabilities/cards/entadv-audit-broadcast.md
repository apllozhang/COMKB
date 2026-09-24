# Audit 与 Broadcast 数据一致性（全网对账、增量同步、对象行为、巡检）

## R — 原文依据

> "Audit is done in two phases: 1-Construction of a reference database … 2-Downloading of the reference database over the network"（p426）
> "Audit modifies directly database tables • In case of error, old data doesn't exist anymore • To limit the risks, it's mandatory to use simulation mode"（p442）
> "IT IS HIGHLY RECOMMENDED TO SAVE THE DATABASE OF ALL NODES BEFORE STARTING THE AUDIT"（p442）
> "The content of the buffer file is emptied and stred every 10 min into a LOG file (the timer can be modified)"（p474）
> "List of objects not broadcasted: • Trunk groups prefixes and ARS tables • IP domains • Content of embedded DHCP server • Speed dialling …"（p485）

出处：ENTPXTE401EN p424-498, p505。

## I — 自述

组网数据治理双工具："对账"（audit，一次性）+"记账"（broadcast，持续）。共用前提：全网防火墙互信（四类地址）+ SSH 免密。

1. **Audit 两阶段**：阶段 1 在执行节点构建参考库（specific 对象全网收集合并，shared 对象取参考节点值；ASCII 压缩经 sftp 传输）；阶段 2 把参考库下发全网（specific 分析插入、shared 系统替换）
2. **对象三分类**：specific（编号计划/电话簿/DDI/寻线组等）、shared（各类 COS/资费/音色/定时器等）、不审计（ARS 表/中继组前缀/IP 域等本地对象，逐节点配）；审计范围跟随 broadcast 对象配置（trunk groups 不广播也不审计）
3. **安全阀三件**：模拟模式强制先行（工作在表副本，菜单选项 4/5）；强烈建议全网备份（大写警告）；链式对象（话务台/实体/呼叫分配互相引用）首跑报错属已知问题——解法为"部分审计（编号计划+实体+话务台+组+分配）+全局审计"或"全局审计跑两遍"
4. **Broadcast 闭环**：MAO 修改进 buffer（cm_cb.sav），默认 10 分钟落 LOG.节点号.序号（配广播域后 A.Z.N.S）；各节点互比 lupd.dat 序号索取补齐，全网确认后删除仅留最新；远端写失败生成 RLOG（静默，须巡检）
5. **广播域与行为矩阵**：128 个域（-1..127）分组控范围；对象出向三态（不广播/域内/全网）×入向三态（不收/仅本域/全网），可全局或逐对象；Update all Behaviors=Yes 时全局覆盖逐对象
6. **激活三法**：cleanbroad -all（重置序号+删文件+全网重启）、WBM System/Broadcast（Operational YES）、mao +br（-br 关、-a 看状态）；急事用 Immediate Broadcast 冲刷 buffer
7. **监控件**：mao -lupd（序号）、prog_diff（LOG/RLOG 内容/节点状态/历史）、maohist（MAO 修改史）、/usr4/mao 下查 RLOG*

## A1 — 书中案例

**Audit 全网对账**（p444-469）：

1. 防火墙：两节点互配对端全部地址（实验 cs2=192.168.1.101、cs2m=192.168.1.103；生产加 twin/第二主地址）
2. SSH：oxe-ssh-auth 对机（多节点用 oxe-nw-sshkey-sync）；authorized_keys 6 条
3. 模拟阶段 1：audit -l EN0，选 4 Simulation: Immediate、1 Reference building、64 General checks、节点 1 Global network；参考节点问句回车（=本地）
4. 模拟通过后真实跑阶段 1；再同法模拟+真实阶段 2 Reference downloading
5. 核对：WBM 编号计划中 NODE2 用户以 network number 身份出现在 NODE1

**Broadcast 启用与验证**（p487-498）：

1. 激活：两节点各执行 cleanbroad -all（全网重置+重启广播）
2. 演练：mao -lupd 双节点核对 log seq=0 → 各做管理（建 31033/中继组 10、31544）→ Immediate Broadcast
3. 核对：LOG.1.1/LOG.2.1 互收、跨节点对象互见、lupd 序号同步为 1
4. 审计：prog_diff 读 LOG.2.1 明细、菜单 2 查远端序号与 ERRLOG；maohist 看修改史

## A2 — 未来触发

使用情境：新节点并入全网（数据导入）；全网数据漂移对账；"改了配置另一节点多久生效"；广播表面完成但数据分叉（RLOG）；audit 报链式对象错误；中继组/ARS 改动不生效（不广播）。

语言信号：audit / 参考（reference）节点 / specific / shared / 模拟 / simulation / broadcast / cleanbroad / mao +br / lupd.dat / LOG / RLOG / prog_diff / maohist / Immediate Broadcast / 广播域。

与相邻能力区分：免密/防火墙前提 → SSH 地基能力；新节点建直链 → Direct IP Link 能力；本地对象（ARS/中继组前缀/IP 域）配置属各节点本地维护（starter 域）。

## E — 可执行步骤

输入契约：全网节点清单与四类地址表、SSH 免密已通、全网库备份窗口。免密或防火墙未通 → 判停回地基卡。

1. 前提核查：每节点防火墙放行对端物理/twin 物理/主角色/第二主地址；SSH 密钥条数核验。完成标准：互信链路全通
2. 备份：全网所有节点数据库备份（audit 强制建议）。完成标准：备份文件可回滚
3. audit 模拟：模拟模式跑阶段 1+2，审结果。完成标准：链式对象错误已知悉并定解法（跑两遍或部分审计）
4. audit 真实执行：按既定解法跑真实阶段 1+2。完成标准：各节点回报处理报告、编号计划互见
5. broadcast 激活：三法选一（首选 cleanbroad -all）并配全局参数（buffer 周期/LOG 上限/广播域）。完成标准：mao -a 显示激活
6. 日常验证与巡检：改数据 → Immediate Broadcast → lupd 序号一致；巡检 /usr4/mao 查 RLOG、prog_diff 查 ERRLOG。完成标准：无 RLOG 积压

判停点：

- audit 模拟报链式对象缺引用 → 按书中两解法处理，不直接硬跑真实审计
- 远端写失败生成 RLOG → 人工排查（典型=对端已有同号对象），处理后清文件再继续
- "配完即全网生效"的预期 → 停，默认 10 分钟 buffer 周期，验收用 Immediate Broadcast
- 新增/重装节点后本地对象（ARS/中继组前缀/IP 域/Number to add）缺失 → 逐节点手工补配，广播不会带过来

输出契约：全网库一致（audit 报告）+ broadcast 运行态（lupd 序号/无 RLOG）+ 本地对象手工核对清单。

## B — 边界

- audit 直改表且旧数据不留——生产必须先模拟+备份（p442），本卡判停点强制
- 参考节点默认=运行 audit 的本地节点；新增空库节点构建参考库时不得选自己（p420-422）
- trunk groups 本身不广播也不审计——组网实验里它只作广播行为验证的观察对象（p485）
- 广播域号 -1 表示不属任何域；LOG 磁盘上限 127 个（p483/p490）
- prog_diff/audit 支持 -l 语言选项（EN0/FR0/GEA）
