# 公私网双向溢出与重路由（本地/组网私到公溢出、公到私重路由、thin sector）

## R — 原文依据

> "'Local Private to Public overflow' feature offers the possibility to reach a device of a remote site by rerouting the call via the public network in case of: - PCS (IP link failure) - No more available IP compressors - Maximum number of calls reached (CAC)"（p218）
> "Two levels of rights • Access right to the service • The 'phone feature COS' … • Barring rules linked to the called external number"（p223）
> "A cleverness, called 'thin sector' allows to assign a DID number to a range of none DID users."（p224）
> "Use of ARS is mandatory to force calls rerouting from public to private network"（p519）
> "Value '-1' on trunk group forces the OXE to check the meaning of the called number … Only one ARS route with this value per table • This route must be in first position in the table"（p522）

出处：ENTPXTE401EN p217-233, p499-536。

## I — 自述

高可用第三层：IP 路径饱和或断链时，电话网就是退路；反方向把公网拨叫折回专线省费。四个构件：

1. **本地私到公溢出**（Local Private to Public Overflow）：跨域呼叫在 CAC 饱和/压缩机枯竭/断链（PCS 激活）三类触发下，CS 取 Node Access Prefix 的 ARS 前缀占中继、按 DID 段翻译出外部号——用户无感，被叫屏显其公网 ID
2. **双层权利**：第一层 phone feature COS 的 Busy/O/S private to public overflow 两个开关（1 允许/0 禁止）；第二层被叫翻译出的外部号还要过闭锁规则；话务台永远放行（无闭锁）；对呼叫 SIP 扩展/SIP 设备无效
3. **thin sector**：把一段非 DID 内部号映射到唯一外部号（段首号）——该外号不得与既有 DID 段重叠；本地溢出场景 Node Access Prefix 的 Install No Last Part 必须留空由 thin sector 兜底；每前缀至多 2000 条 DID 段（p224）
4. **OoS 溢出**：PCS 激活后被救域设备全是 out of service，须系统参数 Overflow on OoS Extension=True 才溢出；改完 pcscopy 同步到 PCS
5. **组网私到公**：直链拥塞/断链时经远端节点的 Node Access Prefix（Number to add=本地 ARS 前缀，不广播）+ 远端 Node DID Translation（广播）走公网；权利模型同本地
6. **公到私重路由**（Public to Private Rerouting）：判别器按呼叫号挂 ARS 表——路由 1 用 TG=-1（去/加位还原内号后重分析走直链），每表仅一条且须首位；路由 2 公网兜底；Time-based Route List 定序；非 DID 被叫不适用

## A1 — 书中案例

**本地溢出配置**（p228-233，RLAB 不可执行，信息性规程）：

1. Node Access Prefix Create：Destination Node No.=1、Number to Add=0（ARS 前缀）；Install No Last Part 留空
2. Node DID Translation 建 DID 段：First external=33210141000、First internal=31000、Range size=2、Thin=No
3. 非 DID 段用 thin sector：First external=33210141010、First internal=31020、Range size=10、Thin=YES
4. COS 双开关：Busy private to public overflow=1、O/S private to public overflow=1
5. 系统参数 Overflow on OoS Extension=True → pcscopy
6. 测试口径：把域 2 的 CAC 改回 1，第二通应走公网建立，验证后改回

**组网双向溢出**（p509-516, p524-536）：

1. 双节点互建 Node Access Prefix 与远端 DID 翻译（各指对端节点与 DID 段）
2. 两节点 COS 放行 Busy/O/S 溢出
3. 私到公测试：临时 Disable 一条直链接入后互拨，trkstat 1 出现 B（Busy）即走公网成立，测试后恢复接入
4. 公到私：判别器挂 Call number=0110X415 到 ARS 表 100；路由 1 TG=-1（去 6 位加 3 位）、路由 2 公网 TG+号码变换；Time-based 定 1→2
5. 公到私测试：拨外线号 0 0110X41500 → 直链可用时外号还原内号、trkstat 全 F（未走公网）、trkvisu 显示链上呼叫

## A2 — 未来触发

使用情境：跨域/跨站呼叫 CAC 拒绝时的退路；断链（PCS 接管）后保持可达；直链断时的组网退路；长途省钱（公网拨叫折回专线）；"来电显示变成外部号"类客诉；thin sector 规划。

语言信号：溢出 / overflow / private to public / public to private / rerouting / Node Access Prefix / thin sector / DID 翻译 / ARS / 判别器 / discriminator / OoS overflow / 话务台放行。

与相邻能力区分：CAC 参数本身 → IP 域与 PCS 能力；直链接入的 Disable/Enable 操作 → Direct IP Link 能力；ARS/闭锁基础属 Starter。

## E — 可执行步骤

输入契约：DID 号段规划、ARS 与闭锁规则（Starter 前置）、公网中继可用、溢出策略（谁允许谁禁止）。公网中继不可用 → 判停，溢出无意义。

1. 建翻译：Node Access Prefix（本地 ARS 前缀；本地溢出场景 Install No Last Part 留空）+ DID 段 + 非 DID 段 thin sector。完成标准：翻译表齐且外号无重叠
2. 放权利：COS 双开关按人群放行；确认被叫外号不受闭锁。完成标准：权利矩阵与客户策略一致
3. OoS 溢出：系统参数 Overflow on OoS Extension=True → pcscopy。完成标准：参数同步到 PCS
4. 组网对称：双节点互配前缀与 DID 翻译；公到私另配判别器+ARS 双路由+时间路由（-1 路由置顶）。完成标准：两节点配置对称、路由次序正确
5. 验证：私到公断链/饱和触发看 trkstat B 态；公到私拨外号看还原与 trkstat 全 F。完成标准：两方向行为符合预期且测试后恢复直链

判停点：

- 目标被叫是 SIP 扩展/SIP 设备 → 本地溢出无效（p226），如实告知无公网退路
- thin sector 外号与 DID 段重叠 → 停，重新选号（否则翻译打架）
- 公到私的 -1 路由不在首位或有多条 → 停，改表（规则硬性）
- 改完系统参数没做 pcscopy → 停，先同步再演练（PCS 侧行为不一致）

输出契约：生效的双向溢出/重路由配置 + 触发测试记录 + "被叫屏显公网 ID"的用户沟通说明。

## B — 边界

- 本地溢出实验 RLAB 不可执行，书中步骤仅为客户现场参考规程（p229，nr-03）
- ARS 管理与闭锁规则设计为 Starter 内容（p229/p525），本书不展开
- 溢出体验差异：被叫看到主叫公网 ID、主叫屏显翻译后外号；block mode 下主叫需确认或等位间计时器（p223/p514）
- 溢出照常出话单（字段 26 记设施类型）；话务台溢出恒放行，计费沟通要提（p223）
- 子网间场景对应 Network Access Prefix / Network DID Translation（p507），机制同源
