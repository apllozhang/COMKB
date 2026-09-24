# Direct IP Link 全 IP 组网（ABC-F2、系统选项三态、接入规则、加删节点）

## R — 原文依据

> "'ABC-F2' proprietary protocol stands for 'Alcatel-Lucent Business Communication – Features 2' … No need anymore of H323 channels"（p384）
> "Number of nodes is limited to 100 • … Up to 24 accesses can be configured • 1 access with IP signalling • Other accesses without signalling • 62 channels per access • As a consequence, 1488 simultaneous calls maximum on a direct call"（p395）
> "Direct IP Link Enabled … This is an irreversible value : once in 'Enabled', it is not possible to change system option anymore. If reverting the process is mandatory, only restoration of database can handle this."（p403）
> "IP BANDWIDTH RATE, ENCRYPTION AND NUMBER OF ACCESSES MUST HAVE THE SAME VALUE ON BOTH ENDS OF THE LINK. IF THEY ARE DIFFERENT AT STARTUP, THEY WON'T ESTABLISH, AND INCIDENT 2879 IS RAISED"（p405）

出处：ENTPXTE401EN p383-423。

## I — 自述

组网主线：ABC-F2 新一代节点间直连——子网内全互联（无中继节点、无 VPN）、RTP 装进 ABC-F 信令内全 IP 直传、免许可免 H.323；要求全网 ≥ OXE Purple R100.0。

1. **系统选项三态且不可逆**：Disabled → Migrating（必须 shutdown -r now 重启生效）→ Enabled（免重启）；Enabled 后系统选项不可改回，唯一回退是恢复数据库备份
2. **全互联自动建链**：启用后重启 RUNTEL，每节点自动生成 99 条 Link_xx 空链（无接入、High bandwidth、Max IP calls=-1）；链路名固定 Link_xx（对端节点号）不可管理；管理界面只显示带接入的链路
3. **接入规则**：每链至多 24 接入；接入 1 必须 IP 信令（填对端 CS 主地址，空间冗余可加第二主地址）；接入 2-24 必须 Without signaling 且 Sig Provider=接入 1；增删接入前先 Disable Direct Link synchro（整链断开），完成后重新 Enable
4. **两端对称三条**：带宽档（High/Low）、加密、接入数必须两端一致——启动时不一致即 2879 事件拒建；运行中改不对称行为异常
5. **加密原生**：节点间信令（含 audit/broadcast 流量）走 IPSec（证书认证）；终端媒体 DTLS/SIP TLS+SRTP（密钥由各 CS 生成经加密链路下发）；可混布加密/非加密链路
6. **容量三层**（引用必须整体）：100 节点；单链 24×62=1488 路并发；约 10000 呼/时/链（8 接入口径）；节点级另有覆盖 direct/SIP/ABCF-IP trunk 的全局上限（默认 -1，超限 6005 事件）
7. **配套限制**：IP Premium Security 不适用；不能 SNMP 监管（改用 hybvisu/trkvisu/事件）；直链语义无中继——节点 IP 故障即孤立，话务层不绕行（唯一退路是配置了私到公溢出）

## A1 — 书中案例

**组网 Pod 迁移前置**（p372-377，RLAB 口径）：

1. Rlab 对 ENTP_OXE_CSA 执行 Remove Interface（释放 192.168.1.1）
2. 对 ENTP_OXE_NODE_1 先 Remove 再 Create Interface（Subnet1、192.168.1.1）
3. 硬重启 NODE 1，从 NODE 2 ping 验证

**直链建立与验证**（p399-423）：

1. 系统标识：NODE1 Network=1/Node=1、NODE2 Network=1/Node=2，各重启
2. 系统选项走 Disabled → Migrating（重启）→ Enabled（本实验库已启用，路径核对即可）
3. 重启后核验 99 条空链；hybvisu 用 dl 选项看全
4. 接入创建：Link_2 接入 1（Signaling type=IP、对端 CS 主 IP）；NODE2 侧 Link_1 对称；加第二接入前先 Disable 同步，接入 2 用 Without signaling+Sig Provider=1，再 Enable
5. 编解码：各节点 Compression parameters 同配（G722/OPUS=Network and local）
6. audit 前测试：建 Network No.（单号）或 Routing No.（号段）互拨验证
7. 维护：compvisu sys、hybvisu -f 2（DATA_TRANSFER/带宽/加密）、trkvisu 2002、rsthyb 2 all、incvisu（2880/2881/2882/2884/2832/2846）

**加删节点**（信息性，p419-422）：加节点=新节点启用选项+全网 broadcast+两侧建接入 1+新节点 audit（参考库构建选单节点，存量库再做阶段 2）；删节点=先全网删对 X 的无信令接入（不广播），再删 IP 信令接入（经广播删除）。

## A2 — 未来触发

使用情境：hybrid+VPN 组网向全 IP 迁移；直链建不起来（2879）；两端接入数/带宽/加密对不上；加节点/删节点；评估"链路能扛多少路"；监控方案选型；想回退 Enabled。

语言信号：Direct IP Link / ABC-F2 / Link_xx / Migrating / Enabled / 不可逆 / 2879 / accesses / 62 通道 / 1488 / 100 节点 / IPSec / SRTP / hybvisu / trkvisu / rsthyb / 6005。

与相邻能力区分：建链后全网数据一致转 Audit 与 Broadcast 能力；断链退路转溢出能力；组网实验环境转 lab-pod-baseline（路由卡）。

## E — 可执行步骤

输入契约：全网版本 ≥R100.0（迁移另需 ≥N1）、子网内无 TDM ABC-F、库备份与回滚窗口、两端网络参数。不满足迁移前提 → 判停，先清 TDM 链/升级版本。

1. 变更评审：确认"Enabled 不可逆"已进变更单（回退=库恢复）。完成标准：回滚预案书面化
2. 系统选项：Disabled 改 Migrating 后 shutdown -r now 重启，再切 Enabled。完成标准：compvisu sys 显示 Direct IP Link ENABLED
3. 核验自动建链：每节点 99 条 Link_xx；hybvisu（dl 选项）可查。完成标准：全互联拓扑成立
4. 建接入：接入 1 双侧对称（IP 信令+对端主地址）→ 需要扩容时 Disable 同步后加无信令接入 → Enable。完成标准：hybvisu 显示 UP/DATA_TRANSFER 且两端接入数一致
5. 通话验证：建 Network/Routing No. 互拨；compvisu eqt all 看 RTP 直达；trkvisu 看链上呼叫。完成标准：链路承载话务
6. 运维交接：监控从 SNMP 切到 hybvisu/trkvisu/incvisu 事件（2880/2881/2832/2846 等）。完成标准：巡检口径落地

判停点：

- 链路起不来且 2879 → 两端带宽/加密/接入数一致性逐项核对，不重启硬试
- 运行中改了单端参数行为异常 → 立即恢复对称，再走 Disable-改-Enable 流程
- 客户要求"Enabled 回退"→ 如实说明只能恢复数据库备份，评估窗口而非尝试改选项
- 节点级呼叫上限触发 6005 → 查全局 Maximum number of IP calls 与链路分配，不盲目加接入

输出契约：DATA_TRANSFER 的直链组网 + 接入与两端对称核对记录 + 容量口径说明（三层整体引用）。

## B — 边界

- 迁移专项规程（hybrid 遗留链清理顺序、备份信令约束）书中给门槛清单（p388），细粒度步骤属现场设计
- IP Premium Security、SNMP 监管在直链网络不可用（p397）——安全与网管方案要前置调整
- 话务层不做断链绕行：IP 网络本身须按"单点故障不影响全互联"设计（p386）
- 链路名 Link_xx 固定不可改名；全网同名以保证广播可用（p405/p408）
- 组网 Pod 的 VM 网卡迁移为 RLAB 专用步骤，生产无此环节（p375）
