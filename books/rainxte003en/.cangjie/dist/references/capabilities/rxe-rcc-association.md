# OXE 分机关联与 RCC 模式（Telephony 关联、五项测试、Rainbow number）

## R — 原文依据

> "This number will be retrieved later for WebRTC gateway use. It will be automatically configured in Remote Extension number by the Rainbow agent (e.g. BBB10070254106463346) when the user selects 'computer' as routing"（p91）
> "Is it possible? … Is it possible to take the call from Rainbow client interface? Which action(s) is/are possible?"（p92）

出处：RAINXTE003EN p89-93。

## I — 自述

把 OXE 分机绑定到 Rainbow 账户，四步：

1. **前置**：PBX 已接 Rainbow（OXE 接入能力交付）、成员账户已建（成员生命周期能力交付）
2. **关联**：Rainbow、My company、Members 选成员、Telephony 页签、Device 字段选 OXE、选分机号、Apply
3. **观察 Rainbow number**：关联后出现 BBB 开头的 17 位技术编号——用户选 computer 路由时由 Rainbow agent 自动写入 OXE 侧 REX，无需手工
4. **RCC 五项测试**：呼 OXE 用户、呼公网号、来话接听（能做哪些动作）、呼纯 Rainbow 用户、纯 Rainbow 用户呼入

**RCC 能力边界**：只能监督话机（接/挂/转），音频全在话机——无网关阶段的正常形态，不是故障。Essential 订阅只有 RCC 且不能改路由（p129）。

## A1 — 书中案例

**分机关联实验**（p89-93）：

1. 管理员登录 Rainbow，进 My company、Members 选成员
2. Telephony 页签 Device 选 OXE、选分机号、Apply
3. 书中关联对：管理员关联 31000、user1 关联 31001（实验口径）
4. 观察新增 Rainbow number 字段（书中示例 BBB10070254106463346）
5. 逐项执行五项测试问题并记录结论（p92-93 原文以问句呈现）

## A2 — 未来触发

使用情境：把话机分机绑到 Rainbow 账号；RCC 是什么；Rainbow 点接听没声音；Rainbow number 从哪来；无网关时能干什么。

语言信号：分机关联 / associate extension / RCC / Remote Call Control / Telephony 页签 / Rainbow number / BBB / Office phone 路由 / 监督话机。

与相邻能力区分：

- 配路由改振铃 → 远程延伸路由能力
- 解锁完整音频 → 网关部署与 OXE 侧网关配置两能力
- Teams 场景的同一关联动作 → Teams 集成能力

## E — 可执行步骤

输入契约：PBX 已接入 Rainbow、成员账户已建、目标分机清单。连接未建立 → 先回 OXE 接入能力。

1. 关联：Telephony 页签选设备与分机后 Apply。完成标准：出现 Rainbow number 字段
2. RCC 呼出测试：路由选 Office phone 呼 OXE 用户。完成标准：话机振铃、Rainbow 侧可控制
3. 公网呼出测试：经 SIP 中继打外部号。完成标准：走 OXE 公网资源可达
4. 来话测试：从另一分机呼入，试接听/挂断/转移。完成标准：动作清单明确、音频在话机
5. 纯 Rainbow 用户对照：双向呼叫各测一次并记录。完成标准：结论留档（含推断项实测）

判停点：

- "Rainbow 接听没声音" → 先确认站点是否无网关（RCC 正常形态），不要按故障修
- 用户报"没有 computer 路由选项" → 无网关，转网关规划/部署能力
- 分机列表为空 → 核 PBX 连接与分机在服状态，不手工硬填

输出契约：成员-分机关联清单 + 五项测试记录 + Rainbow number 备查（排障与网关阶段用）。

## B — 边界

- "RCC 呼纯 Rainbow 用户不通"为机制推断（书中以测试问题呈现未给答案，nr-04）：表述注明推断属性，现场实测确认
- Rainbow number 无手工配置入口：触发条件是用户路由切到 computer，由 agent 自动写入——排障用 remotesets 查看即可
- 本卡覆盖无网关形态；网关部署后的完整路由体验在远程延伸路由与 OXE 侧网关配置两能力
- 实验关联对（31000/31001）与示例号码为实验口径
