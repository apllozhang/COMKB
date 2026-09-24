# OXO 分机关联与 RCC 模式（Telephony 关联、RCC 验证、Rainbow number）

## R — 原文依据

> "Once associated, members will be able to supervise their phone from Rainbow (unhook, hang up, transfer), this is the RCC (Remote Call Control) mode. Without a WebRTC gateway, the audio will be exclusively managed on the phone."（p112）
> "It will be automatically configured in Remote Extension number by the Rainbow agent (e.g. BBB10070254106463346) when the user selects 'computer' as routing"（p115）

出处：RAINXTE001EN p111-116。

## I — 自述

把 OXO 分机绑定到 Rainbow 账户，四步：

1. **验连接**：OXO 侧 OMC/Cloud/Rainbow 看状态；Rainbow 侧 My company/Communication → Comm Servers 页签确认 in service
2. **验话机**：OMC 里核分机 in service（虚拟课堂用 IPDSP/MicroSIP 替代物理话机，需开 auto-provisioning）
3. **关联**：Rainbow → My company → Members → 选成员 → Telephony 页签 → Equipment 选 OXO Connect → 选分机号 → Apply（分机列表实时同步；关联后出现 Rainbow number 字段）
4. **RCC 测试三问**（p116）：选 Office phone 呼出通不通；来话能否在 Rainbow 接、有哪些动作；呼纯 Rainbow 用户通不通

**RCC 能力边界**：只能监督话机（接/挂/转），音频全在话机——无网关阶段的正常形态，不是故障。

## A1 — 书中案例

**分机关联实验**（p111-116）：

1. admin 关联 100、user1 关联 101（实验口径；V-Class 用 IPDSP 104）
2. 观察新增 Rainbow number 字段（例 BBB10070254106463346）
3. 该号由 Rainbow agent 在用户选 computer 路由时自动写入 Remote Extension number
4. 执行 p116 三项 RCC 测试

## A2 — 未来触发

使用情境：把话机分机绑到 Rainbow；RCC 是什么；Rainbow 点接听没声音；Rainbow number 从哪来；无网关时能干什么。

语言信号：分机关联 / associate extension / RCC / Remote Call Control / Telephony 页签 / Rainbow number / Office phone 路由 / 监督话机。

与相邻能力区分：部署网关解锁音频见网关部署能力；Teams 场景的关联属 Teams 集成能力（同一路径的应用）；账户与订阅问题归成员生命周期。

## E — 可执行步骤

输入契约：PBX 已接入 Rainbow、成员账户已建、目标分机清单。连接未建立 → 先回 PBX 接入能力。

1. 双侧验连接：OMC/Cloud/Rainbow 状态 + Rainbow 端 Comm Servers in service。完成标准：两侧均正常
2. 验话机：OMC 核分机 in service。完成标准：目标分机可用
3. 关联：Telephony 页签 → 选设备与分机 → Apply。完成标准：出现 Rainbow number 字段
4. RCC 验证：按三问测试（呼出/呼入接听/纯 Rainbow 用户对照）。完成标准：接/挂/转可用、音频确认在话机

判停点：

- "Rainbow 接听没声音" → 先确认站点是否无网关（RCC 正常形态），不要按故障修
- 用户报"没有 computer 路由选项/音频不落电脑" → 无网关，转网关规划/部署能力
- 分机列表为空 → 核 PBX 连接与分机在服状态，不手工硬填

输出契约：成员-分机关联清单 + RCC 验证记录 + Rainbow number 备查（排障用）。

## B — 边界

- Rainbow number 无手工配置入口：触发条件是用户路由切到 computer，由 Rainbow agent 自动写入（n54）——排障确认该值与路由即可
- "RCC 呼纯 Rainbow 用户不通"为机制推断（书中以测试问题呈现，n16）：表述时注明推断属性
- 本卡覆盖无网关形态；网关部署后的完整路由体验属网关部署能力验证段
