# OmniPCX Enterprise 高级管理 (ENTPXTE401EN Ed13) — 整书理解 (阶段 0 产出)

> 本文档为文档整理的阶段 0 产出，后续所有整理与知识条目都以此为全局上下文。

## 基本信息

- **标题**: OmniPCX Enterprise - Advanced (Participant's Guide)
- **课程代码**: ENTPXTE401EN
- **作者**: ALE Training Services
- **出版/发布时间**: OMNIPCX ENTERPRISE - R101.1 MD4 / ADVANCED - EDITION 13（实验输出时间戳为 2025 年 3-7 月，2025-2026 时代）
- **内容类型**: 课程（官方售后培训讲义幻灯片 + 分步 How-To 实验手册，概念与实验约各占一半）
- **版本来源**: `F:\AIwork\ZCode\books\entpxte401en\source_fulltext.txt`（543 页，带 ===== PAGE N ===== 标记）
- **处理时间**: 2026-09-23

---

## 1. 结构 (Structural)

### 类型
实操手册（厂商培训教材：概念讲义 + 逐命令/逐菜单的 How-To 实验，验证靠命令行状态读数与实际通话行为，而非叙述论证）

### 一句话主旨
把已学过 Starter 的 OXE 工程师带进企业级运维：用呼叫服务器冗余、IP 域与 PCS 保障"站点不瘫、通话不断"，用公私网双向溢出保障"断链仍有退路"，用 Direct IP Link 完成全 IP 组网，再用 Audit 与 Broadcast 保持全网数据库一致，最后配齐速拨、多线/监督、经理助理、寻线/代接、办公桌共享、多设备用户这组话机级业务。

### 骨架 (主要论点及其关系)

1. **培训实验环境**（RLAB 全虚拟化两种 Pod 拓扑——集中式 IP（CSA/CSB+远程站点）与组网（NODE 1/NODE 2）+ Hybrid Mode 教室硬件；统一 IP/账号/密码表；ITSP1 SIP 运营商模拟器与号码规则）
2. **架构总览**（集中式 IP 架构：1 CS + n 媒体网关，至多 15000 分机；组网架构：n CS 互联，至多 100000 分机，ABC 协议特性透明）
3. **Pod 预配置两套 How-To**（集中式：机架/板卡、IPDSP 用户、外部 SIP 网关 pbxN、DID 翻译 33210N41000；组网：VM 网卡迁移、双节点 DID/SIP 网关）
4. **SSH 密钥分发体系**（N3 起 SSHv2 公钥认证强制、host-based 认证被 CIS 合规移除；oxe-ssh-auth 管一对、oxe-nw-sshkey-sync 以 CSV 管全网；密钥存储路径表）——后续一切协同机制的地基
5. **呼叫服务器冗余**（概念：main/standby 实时复制、切换语义、参考 MG、double main、角色初始化防御、主备失联 120 分钟历史与 440 事件、不停机升级 11 步；How-To：本地冗余与空间冗余两套完整部署，netadmin/spadmin/oxe-ssh-auth/mastercopy/role/twin/bascul）
6. **IP 域**（按设备 IP 在初始化时分配域；CAC 跨域呼叫准入；时区/国家本地化；编解码按域带宽档位选择；资源分配与广播；硬规则：CS 必须域 0；How-To：WBM 建域 + domstat/cnx dom/compvisu 验证）
7. **被动通信服务器 PCS**（域级生存性：许可锁 332、4 状态、救援流程、TFTP Backup IP@、回切计时器三模式、SIP 双代理与全局 PCS 地址、单向数据库同步、30 天上限与事件 427/428/431/432；How-To：从 console 改 IP 到 pcscopy、断网演练）
8. **公私网双向溢出**（本地版 Local Private to Public Overflow：CAC 饱和/资源枯竭/断链三类触发 + thin sector 兜底非 DID；组网版 Private to Public Overflow；反方向 Public to Private Rerouting 用 ARS 把公网拨叫折回专线省费）
9. **话机级业务特性集**（速拨编号体系；多线与监督键；经理/助理组与过滤表；寻线组与代接组；办公桌共享 DSS/DSU；多设备用户/Twinset——共同地基是 Multiline）
10. **Direct IP Link 组网**（ABC-F2 新一代全 IP 链路：全互联免中继、RTP 直接、IPSec+SRTP 原生加密、免许可；系统选项三态 Disabled→Migrating→Enabled 且不可逆；接入与加删节点规程）
11. **数据库一致性双工具**（Audit 两阶段对账：构建参考库+全网下发，specific/shared 对象行为不同；Broadcast 持续广播：buffer→LOG→lupd.dat 序号闭环，128 广播域；共用防火墙+SSH 前提）
12. **培训收尾**（在线评估与证书下载流程，附注）

**论点之间的关系**: 层层递进为主——1-3 是实验地基，4 是安全地基（5-11 全部依赖）；5→6→7→8 构成"高可用纵深"主线（冗余保中心、域+PCS 保边缘、溢出保退路）；10→11 构成"组网"主线（先通链路、再保数据一致）；9 是并列的用户特性域，收尾附注未计入主线。

### 作者要解决的核心问题
让 OXE 售后/渠道工程师独立完成企业级部署与运维任务：把单机系统升级为冗余、分域、可生存、可组网、数据一致的企业电话网络，并配齐客户高频要求的话机级业务（秘书 filtering、办公桌共享、多设备等），同时知道每个特性的硬限制在哪里。

---

## 2. 解释 (Interpretive)

### 关键术语 (作者本人的用法)

| 术语 | 作者的定义 | 和常识用法的差异 |
|---|---|---|
| CS Duplication | 呼叫服务器软件平台复制：main + standby，经 IP 链路实时复制 MAO/话务观察/话单/CCD/swinst 的 Linux 数据；支持 CS 板卡、GAS 与虚拟机 | 不只是"备份"：切换时已建立通话保持、建立中丢失；netadmin 的 Linux 数据不随电话库自动复制 |
| Mastercopy | 数据库克隆操作：把主库（含 database+accounting，可选 LINUX DATA）复制到备机；mastercopy 前必须停备机电话应用、先分发 SSH 公钥 | 不是日常同步，是失联超时（440 事件）后的修复手段 |
| Reference Media Gateway | 参考 MG：两 CS 无法互发 keep-alive 时，连接参考 MG 的一侧继续拥有管理权；链路恢复后未连参考 MG 的一侧重启 | 是"double main 裁判"，不是普通网关冗余 |
| Double Main Mode | IP 链路中断时网内出现 Real Main 与 Pseudo Main 两个主（Pseudo Main MAO 关闭）；话单与话务观察不合并、部分网络无语音邮箱 | "双活"在此是故障态而非目标态 |
| Spatial Redundancy | 两 CS 分处不同 IP 子网的冗余（各自 router/掩码/主角色地址 csma/csmb），需内部 DNS 或 DNS 委派解析节点名 | 与"异地容灾"不完全等同：它定义的是网络层形态，机制与本地冗余相同 |
| IP Domain | 一个或多个 IP 地址段/主机的集合；OXE 在设备初始化时按 IP 分配域；每系统 1000 域，未匹配的进默认域 0 | 不是 VLAN 本身，是叠加在编址之上的逻辑域；CS 必须域 0 且其他域不得覆盖 CS 地址 |
| CAC | 呼叫准入控制：只控制跨域（extra-domain）呼叫数，参数 Domain Max Voice Connection（-1 不限）；域内通话不受控 | 与"带宽预留"不同：它是通话条数闸门，超限后靠溢出特性兜底 |
| PCS (Passive Com. Server) | 救援 IP 域的备用 CS：许可锁 332>0、版本不低于 CS；失联转 Active 接管域内设备；数据库单向同步、非实时 | 不是热备 CS：无 TFTP/DHCP/ABC-F 服务，救不了 4645 VM/SIP 传真/SIP VM，最多连续激活 30 天 |
| TFTP Backup IP@ | CS 经信令链路下发给话机 flash 的 PCS 地址；断网时话机用它改连 PCS；PCS 地址变更实时推送、免复位 | 藏在话机里的"逃生门"配置，排障要用 `tnet d <num>` 的 ipconfig survi 查看 |
| Local Private to Public Overflow | 跨域呼叫在 CAC 饱和/缺压缩机/IP 断链（PCS 激活）时自动改经公网，内部号经 Node Access Prefix + DID 翻译为外部号 | 是"绕行"不是"转移"：对用户透明，被叫显示其公网 ID；SIP 扩展/设备不适用 |
| Thin Sector | DID 翻译的巧机制：把一段非 DID 内部号映射到唯一外部号（段首号），让公网可"打到"非直拨用户 | 类似"唯一内部号"的反向运用；该外部号不得与既有 DID 段重叠 |
| Speed Dialing | 缩位拨号：直接式（全网统一）+ 分范围式（至多 400 范围、每实体至多 32 范围），总表 32500 条（默认仅前 4000 可配） | 缩位号默认不吃闭锁管控，勾选 Call Restriction-Barring 才受控 |
| Multiline | 话机持有一个或多个目录号、每号可配多线键；两种形态：Multi-keys（一号多键）与 Multi-MCDU（多号一机） | 一切监督类特性的前置：监督键、经理/助理、寻线组多线行为、多设备都要求 multiline |
| Supervision Key | 监督键：看被监督设备状态（空闲/部分忙/全忙/振铃/退服）、按键直呼或代接；话务台与寻线组不可被监督 | 与 Rainbow 侧"监督组"无关，是 OXE 话机键位机制 |
| Screening / Unscreening | 经理/助理过滤：Screening=仅过滤表内来话转助理；Unscreening=仅表内来话留经理、其余转助理 | 两者不能同时激活，按下一键互斥切换 |
| Hunting Group | 寻线组：Sequential（从头顺序）/Cyclical（轮转起点）/Parallel（并发振铃）三种搜索；成员进出随组 COS 归属 | 一台话机只能属于一个寻线组；溢出号在组空或排队百分比到限时启用 |
| Desk Sharing (DSS/DSU) | 办公桌共享：DSS=共享话机（真 MAC），DSU=漫游用户（虚拟 MAC aa:bb:分机号），登录/登出携带配置 | "虚拟 MAC"是应用层标识，物理帧仍用真地址；DSU 退服时 ippstat 显示虚拟 INTIP 255/255 |
| Multi Device / Twinset | 主站与至多 4 个副站的逻辑关联（twinset 为 2 台特例）；主站号即多设备号；快速移机用 Twinset Get Call 前缀 | 建关联时会清空话机上的全部数据（呼转/回叫/留言），且复制到副站的数据不可再改 |
| Direct IP Link | ABC-F2 新一代节点间链路：子网内全互联、RTP 直接、信令走 IPSec、媒体 DTLS/SIP TLS+SRTP、免许可免 H.323 | 不是"更快的 SIP 中继"：链路名固定 Link_xx 不可管理、无中继节点、不透明溢出 |
| Audit | 全网数据库一次性对账：两阶段（参考库构建→全网下发）；specific 对象全网收集、shared 对象以参考节点为准 | 直改数据库表、旧数据不留，必须先模拟并备份；链式对象常需跑两次 |
| Broadcast | 数据库持续同步：MAO 修改进 buffer 文件，定时（默认 10 分钟）落 LOG.N.S，经 lupd.dat 序号互比补齐 | 非即时：不等 timer 可手动 Immediate Broadcast；trunk group 前缀/ARS 表/IP 域等不广播 |
| Node Access Prefix | 节点接入前缀：指向远端节点号，内含本地 ARS 前缀（Number to add，不广播）与远端 DID 翻译（广播） | 溢出方向的"路由钉子"：本地配置属性与广播属性混杂，重装节点后易漏 |

### 核心命题 (用自己的话)

1. 高可用是分层设计：CS 冗余保呼叫控制不断（已建立通话跨切换存活），IP 域 + PCS 保远程站点在断链时自治，公私网溢出保"还有一条电话网退路"——三层各管一段，不能互相替代。
2. N3 起 SSHv2 公钥认证是强制地基：mastercopy、pcscopy、audit、broadcast 全部依赖免密；oxe-ssh-auth 处理一对 OXE，oxe-nw-sshkey-sync 用 CSV 一次同步全网并自动清理凭证文件。
3. 冗余对的两条铁律：同软件版本 + 同类平台；主备库实时 scp 复制，但 netadmin 维护的 Linux 数据不随电话库走，要 Copy to Twin 或 mastercopy 勾 LINUX DATA 才能带过去。
4. 角色裁决有明确次序：MAO 配 preferred CS IP；没配则"IP 地址最高者"成为 main；double main 时由参考 MG 定真主，链路恢复后未连参考 MG 的一侧自动重启。
5. 主备失联的容忍窗口是可配置的 0-120 分钟（默认 120）：超时删历史、触发 440 事件，此后唯一出路是 mastercopy 克隆——冗余不是免维护。
6. IP 域按 IP 归属在设备初始化时分配，掩码必须与设备一致、设备复位后才落域；CS 必须域 0，其他域的地址范围不得覆盖 CS 的物理/角色地址。
7. CAC 只闸跨域话务：Domain Max Voice Connection 限进出域通话数（-1 不限），域内不管；编解码按域带宽档位选取（高带宽 OPUS SWB>OPUS WB>G722>G711>OPUS NB>G729，低带宽 OPUS NB>G729），G722/OPUS 的媒体服务需 OMS。
8. PCS 是域级生存性而非热备：锁 332>0、版本≥CS、RAM≥CS；救援动作分设备类型（GD/OMS 软复位改连救援地址、话机重启用 TFTP Backup IP@）；回切计时器三模式（默认 30 秒/定点/0=人工）；库单向同步、PCS 上的修改下次更新即丢、防火墙/NTP/SSH 等参数要逐台手工配。
9. PCS 有明确能力边界：最多连续激活 30 天（431 事件倒计时，432 进违约态）；救不了 4645 VM、SIP 传真/SIP 语音邮箱，不提供 TFTP/DHCP/ABC-F；无 MG 的域里的 SIP 话机与 SIP 外部网关救不了。
10. 溢出特性族是一个对称体系：本地场景（Local Private to Public Overflow）覆盖 CAC/资源/断链三类触发；组网场景（Private to Public Overflow）复用 Node Access Prefix + DID 翻译；反方向 Public to Private Rerouting 用 ARS 把公网拨叫折回专线省费——话务台永远放行，SIP 扩展不适用本地溢出。
11. 话机级业务共享同一地基 Multiline：监督键要求被监督对象可见可代接但有硬上限（每话机至多 20 个监督者、每邮箱至多 100/网络 20、全网 15000 监督键），经理/助理、寻线组多线行为、多设备用户全部要求 multiline。
12. Direct IP Link 的启用是一次性决策：系统选项 Disabled→Migrating（必须重启）→Enabled，Enabled 后不可逆，只能靠库恢复回退；带宽/加密/接入数两端必须一致，不对称即 2879 事件拒建链。
13. Audit 与 Broadcast 是"对账 + 记账"双工具：Audit 直改表（必须先模拟、强烈建议先备份全网库），Broadcast 走 buffer→LOG→lupd.dat 序号闭环做增量；两者共用防火墙（全部物理+角色地址）与 SSH 密钥前提，且对象行为配置互相联动。
14. 全书容量数字要当选型表用：15000/100000 分机、1000 IP 域、240 PCS、100 节点、24 接入×62 通道=1488 路/链、约 10000 呼/时/链、32500 速拨、20/100/15000 监督、128 广播域——先查表再承诺。

### 论证链
教材以"概念讲义（原理图 + 参数表 + 限制清单）→ How-To 实验（逐条命令与菜单路径 + 真实输出截图）→ 行为验证（role/twin/pcsview/trkstat/domstat 等命令读状态、双节点互拨/断链演练）"推进：每个实验都给预期输出（如 twin 的 READY 状态表、pcsview 的 INACTIVE* 说明、trkstat 的 B/F 通道态），用可重复的状态读数替代理论论证；特性章节普遍以"限制/警告框"收口，明确边界后再讲配置。

---

## 3. 批判 (Critical) ★

### 作者的时代局限
- 基于 R101.1 MD4 / Ed13 的截图与命令输出（swinst 4.00.91、GD mg4_04.06、OMS oms_14.10）；WBM 菜单与命令输出会随版本漂移。
- Direct IP Link 要求全网 ≥ R100.0（Purple）/N1、迁移机制刚落地，书内连"Direct IP Link ENABLED 后不可逆"这类语义都可能随后续版本调整。
- 书内实验值自身不一致：PCS VM 欢迎信息显示 R101.1-n4.523，而断网演练时 PCS 显示 R101.1-n4.205——教材截图来自不同批次环境。

### 作者的立场盲点
- 明文默认口令贯穿全书设置表（Superuser2580*、letacla1、admin/superuser），且防火墙仅为"partially configured"的教学口径；生产安全基线（证书轮换、口令治理、PKI 管理——netadmin 菜单里明明有）完全不展开。
- 只讲 OXE 侧闭环：OmniVista 8770、4645 VM、DECT、SIP 终端装机都推给 Starter 或其他教材（"REFER TO STARTER TRAINING"），ARS 与闭锁基础也明确不在本书——溢出与重路由章节其实站在书外知识上盖楼。
- 容量数字只给"每系统上限"，没有话务模型（Erlang）与带宽计算，照抄上限做承诺会翻车。

### 未被证明的假设
- 假设读者已修完 Starter（barring、ARS 基础、装机、swinst/netadmin 基本操作），全书多处直接引用。
- 假设 IP 网络按"单节点故障不影响全互联"设计（Direct IP Link 明说 telephonic 层不处理 IP 断链溢出）。
- 假设 FlexLM/许可文件就位（锁 186、332 等），未教许可获取与排障。

### 最强反对意见
"这本手册教的是把企业级机制一个个点亮，不是教怎么设计"——冗余拓扑选择、域与编号规划、PCS 布点、溢出路由策略全都依赖书外的话务与网络设计；且实验口径明文口令、防火墙半配，照搬即事故。因此每个能力的 Boundary 必须标注"实验口径"，并显式指向 MyPortal 技术文档与 Starter 教材作为生产化依据。

> **以上批判会直接成为下游 skill 的 Boundary (B) 字段来源**

---

## 4. 应用潜力 (Applicability)

### 可 skill 化的内容
- [x] OXE 实验环境/交付前置核查（Pod 预配置清单：机架、用户、SIP 网关、DID 翻译）
- [x] SSH 密钥分发体系（oxe-ssh-auth 对机 / oxe-nw-sshkey-sync 全网 CSV / 密钥路径）
- [x] CS 本地冗余部署（IP 配置、防火墙 bulk、MAO 三参数、mastercopy、autostart）
- [x] CS 空间冗余部署（双子网、内部 DNS、DHCP、SIP 终端 DNS 委派）
- [x] 冗余维护与切换演练（role/twin/bascul、参考 MG、preferred CS、pseudo main、double main 处置）
- [x] 不停机升级序列（11 步 bascul 轮换）
- [x] IP 域规划与 CAC 配置（建域、地址分配、压缩参数、域 0 硬规则）
- [x] IP 域验证与排障（domstat/cnx dom/compvisu eqt all）
- [x] PCS 部署全流程（许可核验、console 改 IP、防火墙互信、WBM 声明、域绑定、板卡 PCS 声明、SSH、pcscopy）
- [x] PCS 救援与回切演练（pcsview 四状态、断链模拟、INACTIVE*、手动重启）
- [x] 本地私到公溢出配置（Node Access Prefix、thin sector、COS 双开关、OoS 溢出系统参数）
- [x] 速拨编号体系管理（上限扩容 cfgUpdate、直接/范围/open/timed、前缀、edabv 查询）
- [x] 多线与监督键配置（multi-keys/multi-MCDU、监督键振铃模式、multitool 核验）
- [x] 经理/助理组配置（键组、过滤表、screening/unscreening、away/routing/mail）
- [x] 寻线组与代接组配置（search type、进出组前缀与权利、溢出号、pickup 两式、zdpost/pbxstat）
- [x] 办公桌共享配置（前缀/COS、DSS/DSU 与虚拟 MAC、系统参数五项、dsstat/ippstat）
- [x] 多设备用户/Twinset 配置（主/副站、Twinset Get Call、主站退服三参数、zdpost）
- [x] Direct IP Link 组网（系统选项三态、接入创建规则、网络号/路由号测试、hybvisu/trkvisu/rsthyb、加删节点+audit）
- [x] Audit 全网对账（前提、模拟先行、两阶段执行、对象/节点列表选择）
- [x] Broadcast 启用与监控（cleanbroad/mao +br/WBM、全局与对象行为、lupd.dat/LOG/prog_diff/maohist）
- [x] 组网场景双向溢出（Private to Public：节点前缀双向 + 权利；Public to Private：判别器 + ARS 双路由 + 时间路由）

### 不适合 skill 化的内容
- RLAB 基础设施与设置表（p5-32，教学专用；仅作 Boundary 背景）
- SIP Carrier Simulator 号码规则细节（p33-40，教学专用基础设施）
- 培训评估/证书下载流程（p537-543）
- Starter 级内容（装机、barring、ARS 基础、swinst/netadmin 入门——书内仅以引用出现）
- OmniVista 8770 管理操作（仅以"节点声明"提及）

### 预估 skill 数量
**约 10-12 个能力单元**（阶段 1.5 决定保留，阶段 1.6 与输出模式决定独立入口数量；入口软预算 8 含路由入口）

### 原书关键任务清单（覆盖审计基准，不从旧 verified 反推）

| task_id | 读者任务 | 原文位置/图表 | 预期交付物 | 重要性及依据 | 尚缺条件 |
|---|---|---|---|---|---|
| task-01 | 配置集中式 IP 实验/交付前置 Pod（机架板卡、IPDSP 用户、外部 SIP 网关、DID 翻译、出局验证） | p46-54 | 可用的单机 OXE 基线环境 | 全书实验与现场开局的第一步 | 生产需替换实验 IP/账号口径 |
| task-02 | 建立并同步 SSH 免密体系（oxe-ssh-auth 对机 / oxe-nw-sshkey-sync 全网 CSV / 密钥存储核验） | p55-68, p100-103, p203-208 | mtcl/swinst/root 免密互通 | mastercopy/pcscopy/audit/broadcast 的强制地基 | 无 |
| task-03 | 部署本地冗余 CS 对（spadmin 验许可、netadmin 双机、防火墙 bulk、MAO 三参数、mastercopy、autostart、GD/OMS/IP 话机指向） | p92-114 | 可切换的冗余对 | 企业高可用核心交付 | starter 的 GD/OMS SSH 方法在书外 |
| task-04 | 部署空间冗余 CS 对（双子网、csma/csmb、内部 DNS、DHCP 适配、SIP 终端 DNS 委派） | p115-138 | 跨子网冗余对 | 异地/跨网段场景 | 客户侧 DNS 委派需 LAN 管理员配合 |
| task-05 | 冗余日常维护与切换演练（role/twin 状态判读、bascul 切换、参考 MG/preferred/pseudo main 语义、double main 恢复） | p69-91, p113-114, p137-138 | 可重复演练的切换能力 | 故障处置与验收测试 | 话务影响评估在书外 |
| task-06 | 执行不停机升级（备机先升级→克隆库→bascul→另一侧轮换，11 步） | p83 | 业务不中断的版本升级 | 版本演进常态操作 | 目标版本兼容性在书外 |
| task-07 | 规划并配置 IP 域（建域、域内带宽档、地址段分配、压缩参数、域 0 硬规则） | p154-159 | 域划分生效 | CAC/生存性/本地化的统一底座 | 域规划需客户网络设计输入 |
| task-08 | 验证与排障 IP 域（domstat、cnx dom、compvisu eqt all、CAC 限值测试） | p159-163 | 域/CAC/编解码可验证 | 交付验收与投诉定位 | 无 |
| task-09 | 部署 PCS（许可 332 核验、console 改 IP、防火墙互信、WBM 声明与全局参数、域绑定、OMS/板卡 PCS 声明、SSH 全网同步、pcscopy） | p185-210 | 可用的域级生存性 | 远程站点生存性核心 | starter 的空库/autostart 操作在书外 |
| task-10 | PCS 救援与回切演练（pcsview 四状态、断链模拟、设备接管核验、INACTIVE* 与手动重启） | p210-216 | 可验证的生存性证据 | 验收演示与故障预案 | 无 |
| task-11 | 配置本地私到公溢出（Node Access Prefix、DID 段、thin sector、COS 双开关、OoS 溢出系统参数+pcscopy） | p217-233 | 断链/饱和时的公网退路 | 多站点韧性的最后防线 | ARS 与闭锁为 starter 前置；本实验 RLAB 不可做 |
| task-12 | 管理速拨编号体系（cfgUpdate 扩容、直接/范围/open/timed、实体映射与前缀、edabv 查询） | p234-254 | 可用的缩位拨号 | 高频客户需求 | 无 |
| task-13 | 配置多线与监督键（multi-keys/multi-MCDU、监督键五种振铃、multitool 核验） | p255-273 | 多线/监督能力落地 | 秘书/工作组场景地基 | 无 |
| task-14 | 配置经理/助理组（键组、过滤表、screening/unscreening、away/routing/mail、selective filtering） | p274-295 | 经理-助理协作特性 | 高管场景刚需 | 无 |
| task-15 | 配置寻线组与代接组（search type、进出组前缀与权利、溢出号、greeting guide、pickup 两式、zdpost/pbxstat/supgpbx） | p296-326 | 组业务与代接 | 客服/团队场景高频 | 无 |
| task-16 | 配置办公桌共享（前缀 62/63、COS、DSS/DSU 与虚拟 MAC、系统参数五项、dsstat/ippstat/incvisu） | p327-351 | 工位漫游能力 | 灵活办公场景 | 话机型号支持清单为边界 |
| task-17 | 配置多设备用户/Twinset（主/副站、Twinset Get Call 前缀、主站退服三参数、zdpost 核验） | p352-371 | 一号多机与快速移机 | 移动办公/双机场景 | 副站类型限制（DECT/REX 各一）为边界 |
| task-18 | 建立 Direct IP Link 组网（组网 Pod 迁移、网络/节点号、系统选项三态、接入创建、网络号/路由号测试、维护命令、加删节点+audit） | p372-423 | 全 IP 组网 | 组网交付主线 | 迁移自 hybrid 的专项规程在书外 |
| task-19 | 执行 Audit 全网对账（防火墙/SSH 前提、模拟先行、两阶段执行、对象/节点列表选择） | p424-469 | 全网库一致 | 组网数据治理 | 生产必须先备份全网库 |
| task-20 | 启用与监控 Broadcast（cleanbroad/mao +br/WBM 激活、全局与对象行为、lupd.dat/LOG/RLOG/prog_diff/maohist） | p469-498 | 持续数据同步 | 组网日常运维 | 无 |
| task-21 | 配置组网双向溢出（Private to Public：节点前缀双向+权利+断链测试；Public to Private：判别器+ARS 双路由+时间路由+trkstat/trkvisu 验证） | p499-536 | 组网级双向退路与省费路由 | 组网完整闭环 | 闭锁规则设计为 starter 前置 |

### 优先级排序 (按"最能赋能售后工程师"的角度)
1. task-02 SSH 免密体系（一切协同机制的闸门，失败即全线卡壳）
2. task-03/04 冗余部署（本地/空间两套，企业交付的门槛项）
3. task-09/10 PCS 部署与演练（远程站点生存性，客户最怕的"分部失联"）
4. task-18 Direct IP Link 组网（新一代组网主线，含不可逆决策）
5. task-19/20 Audit + Broadcast（组网数据一致性，配不好全网漂移）
6. task-21 组网双向溢出（退路与省费闭环）
7. task-07/08 IP 域与 CAC（底座 + 验收手段）
8. task-05/06 冗余维护与不停机升级（运维日常）
9. task-11 本地私到公溢出（韧性兜底）
10. task-12~17 话机级业务（高频但独立，可按客户需求挑配）
11. task-01 实验/开局前置（一次性支撑）

---

## ✅ 质量门检查

- [x] 主旨能用一句话说清
- [x] 骨架列出 12 个一级部分（地基 3 + 安全地基 1 + 高可用纵深 4 + 用户特性 1 + 组网 2 + 收尾附注，收尾未计入主线）
- [x] 术语按实际内容列出（22 个）
- [x] 已检查作者局限/假设（实验口径明文口令、防火墙半配、starter 前置、话务模型缺位、截图版本漂移）
- [x] 原书关键任务 21 项，全部有来源页码、交付物与重要性依据
- [x] 用户已授权全流程连续执行（流水线任务书，2026-09-23）

**用户确认时间**: 2026-09-23（全流程授权）
