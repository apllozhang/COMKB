# 维护命令与事件/许可速查（CLI toolbox、事件号、许可锁）

## R — 原文依据

> "(1)csa> role -b → MAIN stand-by CPU state : ACTIVE … (1)csb> role -b → STAND-BY"（p113）
> "Use the different commands of maintenance … 'compvisu sys' • 'hybvisu' • 'trkvisu' • 'compvisu eqt all' • 'rsthyb' • 'incvisu'"（p412）
> "incident « 440 » is triggered. A database cloning operation … is then necessary !"（p79）
> "332 M PCS max. number = 0/ 3 … 186 E-CS redundancy = 1"（p188, p94）

出处：ENTPXTE401EN 各章 Maintenance 节（p94, p113, p160-163, p187-216, p412-417, p449-456, p476-498 等）。

## I — 自述

跨能力排障的统一入口：按功能域归类的命令地图 + 事件号对照 + 许可锁锚点。命令均以 mtcl 登录（部分要求 root）；edabv/audit/prog_diff 支持 -l 语言选项（EN0/FR0/GEA）。

1. **许可与系统**：spadmin（许可文件/锁值/FlexLM 连接）、cfgUpdate（缩拨号上限）、incvisu/incinfo（事件查询）
2. **IP 与冗余**：netadmin（IP/防火墙/DNS/Copy to twin）、role -b（主备态）、twin（冗余各项 READY）、bascul（切换）、swinst（Easy/Expert：克隆/autostart/停起话音）、config（板卡）
3. **PCS**：pcsview（四状态/被救清单/域关联）、pcscopy（库刷新）
4. **域与话务**：domstat（域/条目/设备/DS 列）、cnx dom（CAC 与压缩机计数）、compvisu sys/eqt all（系统压缩参数与呼叫编解码）、represent（RTP 路径）
5. **话机特性**：multitool（多线/监督/经理助理）、edabv（缩位号）、pbxstat -f d（寻线组）、supgpbx -le（全网组）、zdpost d（话机底层数据：pickup_id/tandem 字段）、dsstat（DSS/DSU 13 项）、ippstat（MAC/话机/DSU）
6. **组网**：hybvisu（链路状态 IDLE/SYN_REQ/SYN_ACK/DATA_TRANSFER）、trkvisu（链与链上呼叫）、trkstat（中继通道 B/F 态）、rsthyb（链路复位）
7. **一致性**：audit（交互菜单）、cleanbroad、mao -a/-lupd/+br/-br、prog_diff、maohist

事件号对照（R101.1 口径）：

| 事件 | 含义 | 出处 |
|---|---|---|
| 440 | 主备失联超时（须 mastercopy） | p79 |
| 427 / 428 | PCS/CS 侧信令链路丢失 | p182 |
| 431 / 432 | PCS 剩余激活时间 / 违约态 | p182 |
| 6004 | 忙时 DSU 被登出、通话释放 | p346 |
| 6005 | 节点级全局呼叫上限到达 | p395 |
| 2879 | 直链两端带宽/加密/接入数不一致拒建 | p405 |
| 2880/2881/2882/2884 | ABCF_IP 链路建立中/已建立/释放/已禁用 | p417 |
| 2832 / 2846 | 节点不可达 / 可达 | p417 |

许可锁锚点：186=E-CS redundancy（冗余前提 ≥1）；332=PCS max. number；185=SIP Gateway；184=Integrated Gatekeeper；187/188=H323/SIP network links；329/330=软终端锁。版本锚点：SSHv2 自 N3；直链要求全网 ≥R100.0（Purple）、迁移 ≥N1。

## A1 — 书中案例

**排障三例（书中口径）**：

1. 切换前检查：csa/csb 各跑 role -b 与 twin，全 READY 才允许 bascul（p113）
2. CAC 验证：cnx dom 读 allowed/used/cac over 计数；compvisu eqt all 对照编解码（p162-163）
3. 直链排障：hybvisu -f 2 看状态与两端参数；2879 时先对带宽/加密/接入数（p412-417/p405）

## A2 — 未来触发

使用情境："这个状态用什么命令看"；incvisu 里冒出 440/2879/6004/6005 怎么解释；部署前查许可锁；忘记某前缀/某字段的查询命令。

语言信号：命令名（role/twin/bascul、pcsview/pcscopy、domstat/cnx dom/compvisu、multitool/edabv/pbxstat/zdpost、
  dsstat/ippstat、hybvisu/trkvisu/trkstat/rsthyb、audit/cleanbroad/prog_diff/maohist、incvisu/incinfo、spadmin/cfgUpdate）、
  事件号、锁号。

与相邻能力区分：本卡是索引——定位到命令后，具体语义与步骤转对应能力卡（冗余/PCS/域/溢出/组网/一致性/话机特性）。

## E — 可执行步骤

输入契约：症状描述或事件号/命令输出。命令不存在或输出异常 → 先核版本（R101.1 口径）。

1. 按症状域定位命令组（冗余/PCS/域/话务/话机/组网/一致性）。完成标准：命令选定
2. 查事件号表解释 incvisu 记录，转入对应能力卡处置。完成标准：根因方向明确
3. 部署前用 spadmin 核许可锁（186/332/185 等）。完成标准：锁值满足前提
4. 输出证据留存（命令输出截图/文本）。完成标准：可复查

判停点：

- 命令输出与教材截图结构不一致 → 先核版本漂移（nr-02 同类问题），以现场为准并标注
- 事件含义超出本表 → 转 My Portal 的 TG0028 与技术文档，不猜
- 需要生产安全基线/话务建模 → 书外域，明确指向外部权威来源

输出契约：命令选择与解读 + 事件/许可对照结论 + 转入对应能力卡的建议路径。

## B — 边界

- 事件号与命令输出以 R101.1（MD4）为口径，随版本可能漂移（n46 同类风险）
- 教材截图来自不同批次环境，具体 build 号/计数不作标准值（nr-02）
- 本卡不替代各能力卡的处置步骤；命令语义以对应能力卡 R/I 段原文为准
- 实验口径账号密码仅限 RLAB；生产凭据管理属安全基线（书外）
