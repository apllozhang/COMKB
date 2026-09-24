# 运营商资费建模与成本计算（对象模型、费率公式族、演进、重算与排障）

## R — 原文依据

> "The carrier configuration is based on the following objects • Region • Direction • Tariff ... Costs are calculated during the records loading into the database"（p117）
> "Call with a duration of 2min 24 s: Cost = 2*0,03 + 24*(0,03/60)"（p129）
> "Call with a duration equals to 7 min 24 s: Cost = 3*0,08 + 4*0,07 + 24*(0,06/60)"（p133）
> "The cost calculation is performed during records loading into database. A cost recalculation is required when a carrier configuration change concerns records already stored in the database."（p178）

出处：8770XTE201EN p115-225。

## I — 自述

资费模型 = 运营商（Carrier）> 周期（Period）> 日历/区域/资费/方向四件套，成本在票据加载时算好：

- Carrier：Name 全局唯一、Symbol ≤5 字母唯一（报表里代短名）、Type=Outgoing、Country 仅信息；脉冲型（pulse）走专用入口，建时直接定 Unit cost/Tax/Currency，Tariff 自动生成
- Region：主叫区=PCX 或 PCX+中继组（须填接入号，仅信息）；被叫区=前缀集合，按最优（最长）匹配归属；同一前缀不能跨区域；一区可兼主/被叫两角
- Direction：主叫区×被叫区配对，唯一绑定通信资费（可选服务资费/调整/时延）；未匹配组合落 unspecified 兜底
- 费率公式族（exact 模式，Unit duration=60 按分钟价、=1 按秒价）：

| 参数 | 公式效果 | 书中示例 |
|---|---|---|
| 线性（exact） | 分钟数×单价+剩余秒×(单价/60) | 2m24s = 2×0.03 + 24×(0.03/60)（p129） |
| Answered call initial cost | 成功呼叫加接通费 | Cost = 0.1 + 线性部分（p130） |
| Initial duration | 免费时长，期内只收接通费 | 180s 内 = 0.1（p131） |
| Minimum cost | 与免费时长内成本取高 | ≤90s 按 0.045（p132） |
| Segments | 分段单价按时长扣减 | 7m24s = 3×0.08+4×0.07+24×(0.06/60)（p133） |
| Round up / down | 阶段开始即计 / 计满才计 | 2m30s、60s 阶段×0.1 分别为 0.3 / 0.2（p134） |
| Based on unit（脉冲） | Charge units×单价 | cost = 12×0.03（p135） |
| Unanswered call initial cost | 未接通呼出加收 | 例 0.01（p136） |

- 服务费独立建模：特服号总票价 = 通信费 C + 服务费 S（三组合对应免费/标准/加收）；必须建两个资费（参数同源）并在 Direction 成对绑定；法国 SVA 费率由 ARCEP 监管
- Adjustment：线性 Ax+b 或百分比 x+A%x，可挂资费/方向/段/运营商四类对象（Brest→Paris 打 9 折 = Percentage、A=-10）
- 币种与税：参考币种安装时定死、唯一不可删（只能改名/符号）；附加币种带有效期汇率（无结束日=永久，变动靠开新有效期）；"PCX 给定成本"模式不换汇，PCX 币种必须=参考币种；税率按国家建、带有效期
- 重算铁律：改配置后必须 Compute cost（勾 Carrier Cost(s)+Force）重算存量，否则新旧成本混存；排障看 NMCLD_CostCalculation_1.log 与 NMCCostRecalculation_CostCalculation_1.log

## A1 — 书中案例

**Telecom 1 全流程建模**（p149-180）：

1. Carriers 页签右键 Create：Name=Telecom 1、Symbol=T1、Type=Outgoing、State=Active、Country=France
2. Period > Create：Start date=1/1/2020（结束日建下一周期时自动回填）
3. Calendar 建 "Bank holidays in France"：特定日 1/1 与 5/1，勾 Valid each year
4. 建主叫区 Brest：挂 PCX Ale.Abc1.oxe、接入号 0298112233（必填、仅信息）
5. 建被叫区与前缀：Local=02、National=01/03/04/05、Mobile=06（逐条建，Carrier Dependant 保持默认）
6. Local 资费：exact、Daily、12:00AM 起、Unit 60×0.2
7. National 资费：exact、Daily 三段——Normal 8:00AM 起（0.7/120s/60×0.5）、Reduce 7:00PM 起（0.2/60×0.3）、午夜段 Reduce（0.2/60×0.3），累计铺满全天
8. Mobile 资费：round up——Working day 120s×2、Weekend 180s×2
9. Direction 三条：Brest→Local/National/Mobile 各绑对应资费
10. Compute cost：From=1/1/2020、勾 Carrier Cost(s)+Force、Simple job、Apply 后 Status 页签复查
11. 验证：Records 页签 Direct Carrier 列=Telecom 1 且方向正确

**演进实验**（p181-194）：巴黎加远端网关走中继组 99。顺序：先从 National 删前缀 01（同前缀不能跨区）；建巴黎主叫区（中继组 99+接入号 0102030405）；巴黎补前缀 01 兼作被叫区；Brest 改双栖区并重建 8 条方向；最后 Force 重算，中继组 99 记录带上成本。

**脉冲型 Service**（p216-225）：右键 Create a pulse type carrier，Name=Service、Symbol=Srv、State Date、Unit cost=1.5、TVA/Euro/France（Tariff 自动生成）；被叫区 Special 建前缀 36 与 118712；建唯一方向后 Force 重算。

## A2 — 未来触发

使用情境：给客户建运营商价目模型；话单成本不对/新旧价格混存；每分钟价、接通费、保底、分段怎么配；特服号服务费漏收；加新主叫区报前缀错误；双运营商并存；跨国多币种；Compute cost 怎么跑。

语言信号：Carrier / 运营商 / Region / Direction / Tariff / 资费 / exact duration / round up / 脉冲 / pulse / Unit cost / initial cost / minimum cost / segments。

补充信号：Compute cost / Force / No first carrier found / 前缀 / prefix / TVA / VAT / 汇率 / ARCEP / SVA。

与相邻能力区分：配置文本迁移属 Code Book 迁移能力；发票价加价与订阅费属成本档案能力；票据没进库属票据管道能力。

## E — 可执行步骤

输入契约：客户价目表（按时段/号码段）、币种与税率口径、票据已在库。价目数据来源未定 → 判停先向客户要权威价目。

1. 核对参考币种并按需建附加币种（带有效期汇率）与国家税率。完成标准：币种/税可被资费引用
2. 建运营商（Name/Symbol 唯一，pulse 型走专用入口）。完成标准：Carriers 列表可见
3. 建 Period 与 Calendar（特定日勾 Valid each year）。完成标准：周期生效日期正确
4. 建主叫区（PCX 或中继组+接入号）与被叫区（前缀逐条）。完成标准：前缀无跨区冲突
5. 按 Day type×Time zone 建资费（时段累计铺满全天，参数对照公式族）。完成标准：每条资费可手工复算
6. 建方向并绑资费；特服号场景成对绑服务资费。完成标准：方向矩阵覆盖全部组合
7. Compute cost 勾 Carrier Cost(s)+Force 跑重算。完成标准：任务成功且无新增 "No first carrier found"
8. Records 页签抽验 Direct Carrier 与成本列。完成标准：抽样票据成本=手工复算值

判停点：

- 日志报 "No first carrier found" → 两类根因：前缀漏配；同一号码落在多运营商被叫区无法抉择——补前缀或消除重复，不硬跑重算
- 改了配置没重算 → 历史记录不会自动变，必须 Force 重算，对账差异先查这一步
- "Cost given by the PCX" 模式要求 PCX 币种=参考币种，否则模式不可用（8770 不换汇）
- 参考币种不可删；装错国家只能重装或迁库，本卡不提供改库方案

输出契约：运营商配置全表（区域/前缀/资费/方向）+ 成本复算样例 + 重算任务记录与日志结论。

## B — 边界

- 书内全部费率数值（0.2/0.5/0.3/2、1.5/脉冲、10%/20% 税、1.21/0.82 汇率）为实验口径，生产以客户真实价目为准；价目数据工程在书外（n45）
- 同一前缀不能出现在不同区域——演进时先删旧归属再建新区（p181）；区域可兼主/被叫两角
- Telecom 2 章方向表有原文残留（"Local region"/"Brest re"，见 needs-review nr-04），按实际双栖区结构配置
- 订阅费与发票价调整是入库后的第二层调价，属成本档案能力；本卡的 Adjustment 作用在资费层
- 多运营商并存时同名前缀互斥，特服号（如 118008）跨运营商重复会导致放弃计价（p180）
