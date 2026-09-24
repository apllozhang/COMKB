# Rainbow 混合云接入速览（OXO 侧视角，从简）

## R — 原文依据

> "OMC/Cloud/Rainbow In Cloud menu, select Rainbow … Click on Rainbow enabled … Apply"（p347）
> "Control the connection status: « connected with final password » … The rainbow agent log file name is: ccrbagent.log"（p349）
> "The WebRTC Gateway brings voice interoperability between Rainbow Clients and PBX ecosystem."（p363）
> "Type of Rainbow GW … Internal GW Not supported 20 calls max. External GW (NUC) 50 calls max. 50 calls max. OCE-FE GW 20 calls max. Not supported"（p374）

出处：OXOCXTE300EN p330-426（Rainbow 集成整章）。

## I — 自述

本卡是 OXO 交付工程师的混合云速查，深度内容指向姊妹技能：

- **接入**：PBXID+激活码（Rainbow 平台生成，向 BP 索取或客户管理员在 My company/Communication 自取）填入 OMC/Cloud/Rainbow，勾 Rainbow enabled，域名保持 openrainbow.com 不改（n26）
- **验收与排障**：Webdiag/Services/Rainbow Status 显示 "connected with final password" 即接通；系统日志 ccrbagent.log；用户侧日志在 Rainbow 界面 About Rainbow/Open logs
- **RCC 中间态**：分机关联（Telephony 页签）后仅监督话机（接/挂/保持/转），音频全在话机——无网关时的正常形态，不是故障
- **WebRTC 网关四拓扑**：OCE 集成（R3.2+，免 SIP trunk 许可，20 通话）/OCE Front End（双端 ≥R4.0 MD，20）/外部 NUC（50）/外部 ESXi（50）；自动配置 ≥R4.0.020.002（两处口径见 needs-review nr-01）且仅 Reseller 管理员可激活
- **终端形态**：有物理话机=Multiset（物理主站+Free Rainbow in Twinset 副站，R6.0 起 UTL Bypass）；纯软话机=Anydevice（1 UTL）；R5.2 及以前副站用 Anydevice（n27）
- **话务台**：Attendant 订阅解锁，仅 PC（Web/厚客户端）；OXO 侧队列上限 8 通；监督组 5 组/30 人、互助组动态进出、代接仅限同 PBX 电话呼叫

| 议题 | 本卡给到 | 深入去向 |
|---|---|---|
| 云侧公司/订阅/成员 | 前提核查 | bundle.rainbow-oxo-connect |
| PBX 接入与排障 | 三抓手 | bundle.rainbow-oxo-connect |
| 网关选型/部署/容量 | 对照表 | bundle.rainbow-oxo-connect |
| OXO ACD 呼叫中心 | 不覆盖 | bundle.oxo-connect-call-center |

## A1 — 书中案例

**接入实验**（p344-350）：

1. 前提：Rainbow 侧公司与 PBX 已由 BP 建（实验中讲师演示）
2. 取凭证：web.openrainbow.com 管理员登录，进 My company → Communication，点该 OXO 复制 PBXID 与激活码
3. OMC/Cloud/Rainbow：填两凭证 → 勾 Rainbow enabled → Apply，域名保持默认
4. 验收：Webdiag Rainbow Status 显示 "connected with final password"
5. 排障：系统日志 ccrbagent.log；用户侧 Open logs

**RCC 验证实验**（p357-361）：分机关联后，Rainbow 客户端选 Office phone 拨测呼出、从话机呼入测接/挂/保持——音频始终在话机。

**内部网关自动配置实验**（p394-399）：Reseller 管理员勾 Activate WebRTC Gateway、选 Internal+通道数 → OMC/Cloud/Rainbow 显示 Connected and Enabled。

## A2 — 未来触发

使用情境：交付计划里出现"接 Rainbow"；用户问"耳机里怎么没声音"（RCC 分流）；售前问网关能不能扛；PBX 侧排障碰到 Rainbow agent。

语言信号：Rainbow / PBXID / 激活码 / activation code / RCC / WebRTC 网关 / Twinset / Anydevice / 话务台 / 互助组 / connected with final password / ccrbagent。

与相邻能力区分：PBX 本体交付（硬件/编号/SIP/备份）在本 bundle 其余卡；云侧运营与 Teams、互助话务台深入在姊妹技能 bundle.rainbow-oxo-connect；ACD 呼叫中心在 bundle.oxo-connect-call-center。

## E — 可执行步骤

输入契约：Rainbow 公司已由 BP 建、用户订阅（Business/Enterprise）、OMC 可连 OXO。公司未建 → 判停走 BP 流程（n33）。

1. 核前提：公司与 PBX 已建、订阅到位、安装员凭证在手。完成标准：三前提齐
2. 接入：OMC/Cloud/Rainbow 填 PBXID+激活码、勾启用、域名不动。完成标准：Apply 成功
3. 验收：Webdiag Rainbow Status 判据字符串。完成标准：connected with final password
4. 分机关联：Telephony 页签绑定分机，测 RCC 三项。完成标准：监督动作可用且明示音频在话机
5. （需要音频）网关：按拓扑与容量对照表提方案，转姊妹技能施工。完成标准：方案与容量依据成文

判停点：

- "接听没声音"且未部署网关 → RCC 正常形态，先讲清形态再谈网关，不当故障修
- 客户管理员找不到激活按钮 → 权限设计而非故障，走 Reseller/BP（n33）
- 自动配置版本恰为 R4.0.020.002 → 按 nr-01 双口径如实说明，建议更高版本执行
- OXO ACD/排队机需求 → 超出本卡，转 bundle.oxo-connect-call-center

输出契约：PBX-Rainbow 连接 established 确认 + RCC 验证记录 +（可选）网关方案建议书。

## B — 边界

- 本卡从简：云侧订阅运营、OCE-FE 多场景开局、Teams 集成、SR 支持体系在 bundle.rainbow-oxo-connect
- TURN 服务器位置、防火墙白名单在书外（cookbook/安装指南，n43）
- 容量表 70/100/150 行为方向性参考（needs-review nr-06），引用必须带话务前提
- FTR 默认占位凭证 FleetRef-Installref 正式接入前必须替换（n30）
- 全部实验账号（cCpP/Superuser-P*）为教学口径，见 references.md 实验口径备查
