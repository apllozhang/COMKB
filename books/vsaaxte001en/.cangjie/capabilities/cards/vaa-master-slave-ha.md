# VAA Master/Slave 高可用（slave 部署、HA 命令族、OXE ARS 切换）

## R — 原文依据

> "High availability is made of one Master VAA and one slave VAA … The routing is performed by OmniPCX Enterprise based on an ARS routing table … The slave VAA database is in ReadOnly mode."（p44）
> "No database synchronisation will be performed when master VAA will be recovered. Web client must reconnect (to Slave VAA)."（p47）
> "Warning ANY CONFIGURATION THAT HAD BEEN DONE ON THE SLAVE WILL BE ERASED, AS THE DATABASE WILL BE REPLACED BY A COPY OF THE MASTER'S DATABASE."（p252）
> "A short delay may occur on the first call, as OXE will need to determine that the SIP trunk on the master server has been interrupted."（p271）

出处：VSAAXTE001EN p44-48, p239-271。

## I — 自述

高可用是"VAA 侧复制 + OXE 侧切换"的组合，四个知识块：

1. **机制**：两台 VAA 各建一条 SIP 中继（trunk group 10 指向 Master、trunk group 11 指向 Slave），OXE 用 ARS 路由表选路；数据库 Master→Slave 定期复制；VAA 自身不做地址漂移——"切换"动作发生在 OXE
2. **行为规则集（预期管理硬口径）**：

   - Slave 库只读——故障期间它处理的呼叫不产生统计
   - 任何切换（OXE 呼叫服务器切换/主 VAA 丢失/WAN 断）都丢失进行中呼叫（原书三处重复）
   - 主 VAA 恢复后不自动回同步，必须手工 vaa ha resync；Web 客户端要手动重连（到 Slave）
   - 切换后第一通呼叫有短暂延迟（OXE 判定中继断开）；N+1 场景单 VAA 故障期间总容量下降
3. **VAA 侧部署五步**：

   - slave 系统准备（同 master：BootDVD/改密/GRUB/配网，FQDN vaa2.company.com 用于许可）
   - slave 独立安装 VAA（incoming username vaa2、license2.vaa，其余参数同 master）
   - 核对互通（Web 可达、互 ping）
   - master 侧 vaa ha addslave [slave IP]（输 slave admin 密码，建 SSH key 并推送库快照，slave 现有配置被清空）
   - 双侧验证（role/listslave/whoismaster/services、slave Web 只读告警与配置一致性）
4. **OXE 侧附加配置九段链**：

   - 第二 trunk group（SIPVAA2/remote network 11）；第二外部网关（VAA2/5060 UDP/proxy 自身 IP/incoming username vaa2）
   - 信任 IP；识别符（放行 314 开头五位号、挂 ARS route list）；Entity 挂接（entity 1 与 entity 0 的 selector 条目）
   - NPD（编号计划描述）；编号命令表（表 10/表 11 对应两网关）
   - ARS Route list 与 Route 1/Route 2（各挂 trunk group/NCT/NPD）+ Time Based Route List
   - 测试号（ARS 前缀 + 速拨 31401 对应呼叫号）

## A1 — 书中案例

**HA 切换测试**（p271，实验口径号码）：

1. 前提：OXE 侧 SIP 与 HA 附加配置全部完成（必须先管好 SIP 再测试）
2. master 上执行 sudo vaa stop（或直接关机）模拟故障
3. 拨打 VAA 路由号（如 3140X）
4. 首呼有短暂延迟——OXE 需判定 master 中继已断，属预期行为
5. 随后脚本应从 slave 读出，听感与 master 正常时一致
6. 验证 slave 只读态：Web 登录 slave 出现只读告警
7. 测完必须 sudo vaa start 恢复 master，再 vaa ha resync 回同步
8. 复核双机 role 与 listslave/whoismaster 输出各归其位

## A2 — 未来触发

使用情境：客户要双机冗余；部署 slave；主 VAA 宕机后恢复；切换后报表缺数据；Web 打不开要重连；改配置被拒（只读）；OXE 侧 ARS 双路由配置。

语言信号：高可用 / HA / Master / Slave / addslave / resync / vaa ha role / whoismaster / listslave / ARS / 切换 / failover / 只读 / read-only / 丢话 / 统计缺口 / 识别符 / NPD / Time Based Route。

与相邻能力区分：单机安装与 OXE 五段链归安装对接能力；N+1 扩容与 reference VAA、multi-company 归架构冗余能力（路由卡）；切换后统计口径归统计能力。

## E — 可执行步骤

输入契约：两台同规格服务器、两份许可（各自绑定 MAC/FQDN，FQDN 装系统时定死）、OXE 编号计划现状（识别符/NPD/ARS 为 OXE 侧概念）、维护窗口（addslave 与切换测试均有破坏面）。

1. slave 系统准备与独立安装：同 master 流程，参数差异仅 FQDN/IP/incoming username/许可文件。完成标准：slave Web 可达、双机互 ping 通
2. master 侧加从：vaa ha role 确认 Classic 后执行 vaa ha addslave [slave IP]，输 slave admin 密码。完成标准：SSH key 建立且库快照推送完成
3. slave 侧重启与确认：sudo vaa restart 后 vaa ha role 应显示 Slave。完成标准：角色就位
4. 双侧验证：master 看 services/role/listslave，slave 看 services/role/whoismaster，Web 登录 slave 确认只读告警与配置一致。完成标准：五项检查全过
5. OXE 侧九段链：按第二中继、第二网关、信任 IP、识别符、Entity、NPD、命令表、ARS 双路由、测试号顺序配置。完成标准：ARS Route 1/Route 2 与 Time Based Route List 就位
6. 切换测试：master 执行 vaa stop 后拨打测试号，验证首呼短延迟后 slave 接续。完成标准：切换生效
7. 恢复：master sudo vaa start，随后 vaa ha resync 回同步，复核双侧状态。完成标准：双机回归正常态

判停点：

- 客户预期"双机不掉话" → 停，任何切换丢进行中呼叫是设计行为，SLA 只保证新呼叫接续（n05）
- slave 上已配了一堆业务再 addslave → 停，会被 master 快照全部覆盖（n29），正确顺序是配置只在 master 做
- master 恢复后没人跑 resync → 停，双机配置分叉风险；resync 纳入故障恢复 checklist
- 客户既要跨数据中心容灾又要 OPEX → 停，空间冗余与 Purple On Demand 互斥（n08），转商务决策
- 测完忘记恢复 master → 停，系统会一直跑在 slave 只读态（不能改配置、无统计）

输出契约：就绪的 Master/Slave 双机 + OXE 侧 ARS 双路由配置记录 + 切换测试报告（含首呼延迟口径）+ 恢复 checklist。

## B — 边界

- 实验口径：双机地址 192.168.1.55/56、incoming username vaa1/vaa2、许可 license1/license2.vaa、5 端口 Release 11——生产按现场替换
- "Slave 不是自动接管热备"为引申定性（行为依据原文：只读/丢话/不自动回同步），引用带推断标注（nr-07）
- 识别符/NPD/ARS 为 OXE 编号计划概念，OXE 侧只给参数表不讲原理，默认读者会 OXE 运维（n42 关联）
- OXE 呼叫服务器自身切换场景（本地/空间冗余）的行为见架构冗余能力卡；三用例均为讲义级无实验
- N+1（扩容型，reference VAA）与 Master/Slave（冗余型）是两种结构，本卡不覆盖 N+1
- HA 命令全部需 root 权限（sudo）；命令全集以安装手册第 6 章为准（p29）
