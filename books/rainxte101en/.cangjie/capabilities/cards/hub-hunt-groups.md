# 呼叫组与话务分配（Hunt Group、等待队列、经理助理、紧急组、录音）

## R — 原文依据

> "1 REGULAR — All classic cases of call taking in a team ... 4 MANAGER / ASSISTANT — Manager wishing to delegate the management of its calls"（p209）
> "the oldest call on hold is presented (first come, first served), after a 10 sec delay • If the waiting time exceeds the overflow time (adjustable from 10 to 900 sec)"（p215）
> "The DID of the Manager who wants to be able to screen his calls must be assigned to the group level, and not to the manager."（p221）
> "Active group -> Direct calls (without outbound prefix) to emergency numbers are routed to the group and not to the outside."（p228）
> "RECORDINGS ARE STORED FOR 2 MONTHS."（p231）

出处：RAINXTE101EN p208-242。

## I — 自述

群组是话务分配的主战场，四类组对号入座：

| 组类型 | 场景 | 分发 | 关键规则 |
|---|---|---|---|
| Regular（hunt group） | 团队接听（热线/售后/下单） | Parallel/Serial/Circular | 可带/不带等待队列 |
| Attendant | 多址共享前台 | Parallel | 全员须 Voice Attendant 订阅 |
| Emergency | 监管场景安保站 | 同标准组 | 一公司仅一个，须激活 |
| Manager/Assistant | 经理委托过滤 | Serial（经理→助理链） | 必然单经理，助理可跨组 |

Hunt group 参数全集（p211-215）：

1. 每组上限 50 成员（成员可跨多组）；每组一内线号（必填）+ 一 DDI（选填）
2. 分发三型：Parallel 同振 / Serial 按序 / Circular 轮流；Serial/Circular 轮转定时默认 10 秒
3. 无队列组：全员占线即溢出（图示默认 60 秒，p211）；有队列组：先播提示、FCFS 在 10 秒延迟后派最老来话，等待超 10-900 秒可调上限后按组策略溢出；可设"组空即立即溢出"
4. 溢出目的地 8 种（p235 实验页口径）：voice prompt / member / group / internal number / public number / voicemail / welcome service / automated attendant
5. 坐席可随时退组（应用或话机键），可勾"禁止最后一名成员退组"；只授 Administrator 不授 Agent 的人不接组来电，坐席侧视其为"永久已退组"
6. 每建组自动生成对应 bubble：组留言以音频文件自动转入、组通话记录（已处理/未接/已溢出）在 bubble 内管理，全员权限相同

经理助理组四条规则（p219-221）：只筛电话呼叫（Rainbow 音视频不筛）；经理要被筛其 DID 必须配组级而非个人；多经理=建多组；溢出到语音提示可定制文案、时长 5-30 秒。

紧急呼叫三段链路（p227-229）：

1. **号码面**：紧急号码表按公司国家+trunk 组自动配置；免出局前缀可拨；对受外呼闭锁（含仅内线）用户也放行；号码保留不可改、不可占作内线号
2. **组面**：唯一紧急组，激活后免前缀紧急呼叫改路由进组而非外线；组员转公共紧急号必须手动加前缀（例 0112）
3. **定位面**：BP 购号时把 DID 地址登记进 SIP 运营商数据库，由运营商路由到正确 PSAP；Rainbow 不管 DID 定位

录音四口径（p230-231, p235）：触发面三层（成员/组/线路，组级按 all/external/internal/none）；保留 2 个月；Recordings 页签仅最终客户管理员可见（BP 看不到）；超期归档走付费选件 Rainbow Exporter（按日拷贝到 Google Drive 或客户 SFTP）。

## A1 — 书中案例

**建 Hunt Group 与经理助理组**（p233-237，How-To）：

1. Communication 区 → Groups 页签 → Create。
2. 填 Name、Type=Hunt group、Subtype=Regular、Distribution=serial（实验口径）。
3. 填 Internal number=100、Public number 从号池选、轮转定时默认 10 秒。
4. 第二页勾 Lock the last member（防组空）→ 选成员 101、102 → Apply。
5. 编辑该组配溢出：选录音档、激活 busy/no answer 溢出、选目的地。
6. 再建 Manager/Assistant 组：Type=Hunt Group、Subtype=Manager/Assistant、内线 106。
7. 公网号配给组而非 Dave 个人 → Manager=Dave、Assistant=Carol → Apply。

**紧急号码查询与紧急组激活**（p238-242，How-To）：

1. Communication 区 → Traffic control 页签 → Emergency numbers 查看国家号码表。
2. 建紧急组方法 1（推荐）：同页点 Create emergency group，Emergency 标记默认已勾。
3. 填 Name=WFA、Distribution=parallel、内线 110、成员 Alice 和 Carol。
4. 方法 2（Groups 页签建）：手动勾 Emergency group——此路默认不勾，勿忘。
5. Traffic control/Emergency numbers 页点 Activate（或 Call settings 勾 Activate emergency group）。

## A2 — 未来触发

使用情境：客服组排班与溢出策略；客户投诉打不进（占线即溢出）；助理帮老板筛电话不生效；安保站紧急呼叫合规；录音留存与调听；组留言去哪听。

语言信号：hunt group / 呼叫组 / 等待队列 / waiting queue / 溢出 / overflow / Parallel / Serial / Circular / FCFS / 组角色 / 经理助理 / 筛选 / 紧急组 / emergency group / 0112 / PSAP / 录音 / Rainbow Exporter / bubble。

与相邻能力区分：话务台人工接听与监督归话务台监督能力；欢迎服务闭时段转组归欢迎服务 IVR 能力；成员退组操作入口在成员侧（例行程序/按键组）归成员管理能力。

## E — 可执行步骤

输入契约：组场景（接听团队/前台/经理过滤/安保）、成员与订阅（Attendant 组须全员 Voice Attendant）、号码资源（内线必填+DDI 选配）、溢出策略与目的地、录音合规要求。

1. 定组型：按四类组表对号（Regular/Attendant/Emergency/Manager-Assistant）。完成标准：组型与场景、订阅匹配
2. 建组：填内线号（必）、DDI（选）、分发模式与定时、成员、锁末位选项。完成标准：组在 Groups 列表且成员在列
3. 配队列（如需）：Type 选带等待队列 → 定溢出上限（10-900 秒）与"组空即溢出"。完成标准：拨测验证 FCFS 与溢出行为
4. 配溢出与录音：选目的地类型（8 种之一）→ 按需设组级录音档。完成标准：溢出拨测通过、录音档符合合规口径
5. 经理助理专项：经理 DID 配到组级 → 助理开筛选 → 拨经理 DID 验证筛选链。完成标准：电话呼叫被筛、Rainbow 呼叫不筛（预期一致）
6. 紧急组专项：按两法之一创建（Groups 路径记得勾 Emergency 标记）→ 激活 → 培训组员"进组/加前缀转警"两条路径。完成标准：组已激活且安保流程培训完成

判停点：

- "助理筛不到经理电话" → 停，先查 DID 是否挂组级、再来话是否 Rainbow 音视频（两处都不符才失效，n38）
- 客户把紧急组理解成"呼叫转接服务" → 停，讲透激活语义：免前缀紧急呼叫进组不出局，转警要加前缀 0112（n39）
- Groups 页签建紧急组忘勾标记 → 停，那是普通组，激活后紧急呼叫不会路由进它（n40）
- 录音要存超 2 个月 → 停，平台只保 2 个月且 BP 不可见；归档走付费 Rainbow Exporter，报价阶段锁进合同（n42）

输出契约：可用的组（分发/队列/溢出/录音就位）+ 组角色分配表 + 紧急组激活与培训记录。

## B — 边界

- 话务建模（多少组、队列多长、坐席数）在书外，按客户话务量设计；本卡只给机制与参数上限
- 紧急定位责任链：DID 地址登记是 BP 侧流程义务，漏登记=呼叫可能被派往错误辖区（p229，n41）——项目清单单列
- Attendant 子型组全员须 Voice Attendant 订阅（p209/p249，n35），当"便宜版 hunt group"用会撞订阅墙
- Manager/Assistant 组的 Administrator 管理功能官方标注"后续版本提供"（p209 脚注），方案别承诺组级管理能力
- 无队列组溢出默认 60 秒（p211 图示）与带队列组 10-900 秒可调并存，引用时分开表述（needs-review nr-02）
- "60 secondes"、"BY DEFAUT" 等为原文拼写照录（needs-review nr-05）
