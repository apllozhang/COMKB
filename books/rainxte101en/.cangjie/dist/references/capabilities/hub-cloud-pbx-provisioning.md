# Cloud PBX 声明与话务配置（编号计划、公网号码、闭锁、trunk）

## R — 原文依据

> "One Rainbow company = one and only one CloudPBX. One CloudPBX = one and only one external SIP trunk (SIP provider)."（p78）
> "you need at least a 'Voice' license. Without this, you'll only see traditional PBXs: OXO Connect, OmniPCX Enterprise, Third party PBX"（p80）
> "The 1st number you inject is, by default, the main number of the installation."（p83）
> "Create the prefixes in international format, without '+' or '00' in front."（p86）

出处：RAINXTE101EN p76-104。

## I — 自述

Cloud PBX 是 Hub 的话务核心（软 SIP PBX），拓扑三规则先行：

1. **一二一约束**：一公司有且只有一个 Cloud PBX；一个 Cloud PBX 只能关联一条外部 SIP trunk（一个运营商）；呼叫通道数与电话线数无上限
2. **声明顺序**：公司、分配 Voice 许可（没有 Voice 订阅时建通信服务器界面只见传统 PBX 类型）、声明 Cloud PBX、电话线经运营商订购门户开通（携转或新订 DID，BP/运营商侧）
3. **编号计划**：内部号 2-9 位可多长度混存（1xx/3xx/4xxxx…）；出局前缀 0 或 9（国家相关）；号长默认 3；"优化话机拨叫"可让话机免拨出局前缀——国家相关，需与 ALE 确认

公司级 Call settings 默认值（p82, p102-103）：

| 设置项 | 默认口径 |
|---|---|
| 忙/无应答溢出 | 溢出到留言信箱（可关） |
| 留言邮件通知 | 无邮件通知（可选仅通知/带附件） |
| 闭锁允许档 | 仅内线 / 国内+内线 / 国际+国内+内线 |
| 闭锁屏蔽档 | 无 / 收费号 / 自定义清单 |
| 主叫 ID 策略 | 用户公网号或公司号，可允许成员自选 |
| 软话机紧急呼叫 | 勾选（默认允许） |
| 呼转外部目的地 | 停用 |
| 内部呼叫经外部 trunk | 停用 |
| 成员单/复线 | 多线（multiline） |
| 录音提示音 | None |
| 转移类型 | 协商转 / 盲转 |

公网号码与流量控制要点：

1. DDI 号/号段分配给成员、hunt group 与话务台组、欢迎服务（预通告）、IVR；其中一个必须定为公司号码；首个注入号码（或首段首个）默认成为公司主号，可改
2. 白名单=仅这些前缀可外呼、黑名单=这些前缀一律禁呼；作用于全公司或指定用户；前缀按国际格式、前头不带 + 或 00（法国 0825 收费号不要录成 33825）
3. trunk 商务两型：bundled（Hub+话务一单一发票）或 separated（两单两票）；PSTN 服务不由 ALE Rainbow 团队订购管理

## A1 — 书中案例

**声明并配置 Cloud PBX**（p99-104，How-To）：

1. 前提：公司已有 Voice Enterprise 订阅（BP 权限操作）。
2. Communication 区 / Comm. Servers 页签 / Create → Server type 选 Cloud PBX。
3. 填语音引导语言、External trunk（实验口径 ALE Training Carrier）、出局前缀 0、号长 3。
4. 编号计划建两段：100-199 与 200-299（实验口径）；Barring 选 No restriction。
5. Call settings 区逐项核对上表默认规则（溢出/闭锁/主叫 ID/紧急/单复线）。
6. Public numbers 页签 / Create → 段首 02982967X0 → 勾 Set as company phone number。
7. 勾 Create a range of public numbers → Range size 10 → 创建（得 02982967X0-X9）。

验收口径：Comm. Servers 出现所声明 Cloud PBX；Public numbers 显示号段且主号已设。

## A2 — 未来触发

使用情境：给客户声明 Cloud PBX；设计/修改编号计划；分配 DDI 号段与公司主号；外呼主叫显示策略；禁国际长途/收费号；trunk 商务模式与带宽估算。

语言信号：Cloud PBX / 编号计划 / numbering plan / 出局前缀 / DDI / 公网号码 / 主号 / 闭锁 / barring / 白名单 / blacklist / trunk / bundled / separated / 带宽 / Opus / G711。

与相邻能力区分：网络端口与 Pilot 评估归网络就绪能力（路由卡）；成员电话页签的号码分配归成员管理能力；多站点参数归多站点能力（路由卡）。

## E — 可执行步骤

输入契约：BP 权限、公司已有 Voice Business/Enterprise 订阅、客户编号习惯（分机位数/号段）、号码资源（新订或携转，运营商侧）、闭锁合规要求。

1. 核前提：订阅池有 Voice Business/Enterprise、trunk 组已由伙伴备好。完成标准：声明界面能选到 Cloud PBX 类型
2. 声明 Cloud PBX：Comm. Servers → Create → 填名称/语言/trunk/编号计划（出局前缀/号长/号段）。完成标准：PBX 出现在 Comm. Servers 列表
3. 核对 Call settings 默认值：按上表逐项过，闭锁档与主叫 ID 策略按客户合规要求调整。完成标准：设置清单成文
4. 注入公网号码：Public numbers / Create → 定主号 → 按需建号段。完成标准：号段在列且公司主号正确
5. 流量控制（可选）：白/黑名单按国际格式录前缀，定生效范围（全公司/指定用户）。完成标准：闭锁策略拨测通过
6. 带宽核算：按 Opus 80 kbps/VP8 1.5 Mbps/G711 64 kbps 口径估 premises 到 SIP trunk 段。完成标准：带宽结论写入交付基线

判停点：

- 建通信服务器时选不到 Cloud PBX（只见 OXO Connect/OXE/第三方）→ 停，查订阅池，先开 Voice 订阅（p75/p80）
- 客户要求"每站点一台 PBX/每地一条中继" → 停，纠正预期：一公司一 PBX 一 trunk，多站点用逻辑分区（转多站点能力）
- 要承诺"话机免拨 0" → 停，Optimized phone dialing 国家相关，先与 ALE 确认（n12）
- 编号计划怎么"设计"（方法论）→ 书外，按客户拨号习惯与运营商资源协商，本卡只管参数含义

输出契约：可用的 Cloud PBX（编号计划/Call settings/主号已定）+ 号码分配清单 + 闭锁策略与带宽结论。

## B — 边界

- 编号计划的"设计方法论"原书不讲，只讲参数含义（BOOK_OVERVIEW 批判节）；一公司一 PBX 一 trunk 是硬约束（n11）
- trunk 合同、资费、号码携转、DID 地址登记（紧急定位）在 BP/运营商侧书外（p88/p229，n14/n41）；ALE 不计费不开票（p318）
- 带宽四行表（Opus 80 kbps、VP8 1.5 Mbps、G711 64 kbps、信令可忽略）为书内指示性口径，完整带宽要求以 Network Requirements 文档为准（p90 指针）
- 实验号段 02982967X0-X9 与 trunk 名 ALE Training Carrier 均为实验口径（needs-review nr-06）
- 主号错认直接影响外呼主叫 ID：先注入的号默认当主号，注错要手工改或用"自动改主号"选项（p104，n13）
