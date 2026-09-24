# 呼叫特征化与 Smart Call Routing 路由表设计（OXO Connect）

## R — 原文依据

> "Priority comparison # 1: CLIn / CLIt & DIDn / DIDt ... # 2: CLIn / CLIt & DIDt not filled in ... # 3: DIDn / DIDt & CLIt not filled in"（p87）
> "CLI comparison CLIn / CLIt starts from the left to the right. DIDn / DIDt comparison starts from the right to the left"（p88）
> "Fill in the table beginning with the special case (the longest numbers) • Ending with the general case (the shortest numbers)"（p88）

出处：OXOCXTE107EN p86-88（机制与规则）、p115-116（国别+大客户分流实验）。

## I — 自述

呼叫特征化决定"这通电话进哪个 ACD 组"，匹配有三条硬规则：

1. **三级优先序**：
   - #1 CLI 与 DDI 双命中 → 立即应用该组
   - #2 CLI 命中且条目 DDI 留空 → 应用
   - #3 DDI 命中且条目 CLI 留空 → 应用
   - 全不中 → 回振铃音（**不进 ACD**）
2. **比较方向不对称**：
   - CLI 从左向右比（前缀匹配，适合国别码）
   - DDI 从右向左比（后缀匹配，适合分机尾号）
3. **填表顺序 = 匹配顺序**：从最特殊（最长号码、双条件）填到最一般，否则宽泛条目先截胡精准条目

设计套路：大客户双匹配条目放最前 → 国别/号段单条件条目放中间 → 兜底条目放最后。表上限 10000 条，支持 CSV 导入导出。

## A1 — 书中案例

**按国别 + 大客户分流实验**（p115-116，厂商实验）

- **需求**：UK(0044) 进组1、Spain(0034) 进组2、Germany(0049) 进组3；三家大客户（Brest / Paris / Illkirch bank）以 CLI+DDI 双条件进组1；大客户没拨对 DDI 时全部落组3
- **填表**：
  1. 先填大客户双匹配条目（CLI 全号 + DDI 尾号 → 组1）
  2. 再填国别条目（仅 CLI：0044/0034/0049，DDI 留空 → 组1/2/3）
  3. 最后填兜底条目（→ 组3）
- **行为推演**：Brest bank 拨对 DDI 时双匹配进组1；拨错 DDI 则双匹配不中，落兜底组3，与需求一致（原书未逐行给表，行序按规则推演，已标注）

## A2 — 未来触发

使用情境：

1. "VIP 客户来电要进专属组"——大客户 CLI+DDI 双匹配
2. "不同国家的来电分给不同语言组"——国别前缀路由
3. "配了路由怎么不生效/进错组"——命中级别与比较方向排查
4. "400/服务号分流到不同业务组"——DDI 维度分流
5. "没有匹配的电话怎么处理"——兜底条目设计

语言信号：分流 / 按客户进组 / 大客户专线 / CLI / DDI / 主叫识别 / Smart Call Routing / route by number / VIP 分组 / 路由不生效。

与相邻能力区分：组内"哪个坐席接"→ 搜索模式能力；来话进组后的行为 → 六场景能力；本能力只管"进哪个组"。

## E — 可执行步骤

输入契约：分流需求表（CLI 段、DDI 段、目标组，标注特殊/一般级别）、兜底去向。缺任一条先询问。

1. **排序**：双匹配（最长）→ 仅 CLI（长前缀在前）→ 仅 DDI（长后缀在前）→ 兜底。完成标准：条目表次序明确
2. 进入：OMC / Call distribution Services / ACD-SCR Services / Smart Call Routing → Line parameters
3. 按序录入：每条填 CLI 模式（留空=不比对）与 DDI 模式（留空=不比对）及目标组。完成标准：次序与第 1 步一致
4. **核对方向**：CLI 条目=前缀语义；DDI 条目=后缀语义。完成标准：无方向性错误
5. 实呼验证：每个条目代表号码实呼记录落组；特别验证大客户"拨错 DDI"的兜底行为。完成标准：落组与需求表一致

判停点：条目不生效 → 回第 4 步查方向与优先级（是否被更靠前的宽泛条目截胡）。

输出契约：Line parameters 条目表（CLI / DDI / 目标组 / 次序）+ 实呼验证记录。

## B — 边界

- 方向搞反是最常见错误：CLI 不是后缀匹配、DDI 不是前缀匹配
- 兜底缺失 = 未匹配来电**回振铃不进 ACD**；"其他来电进 X 组"必须显式加兜底条目
- 上限 10000 条；超出需外部预处理（原书未给方案）
- 原书实验为法国号码方案；国内落地先确认运营商发送的号码格式（原书未覆盖），避免照搬位数
- 大客户"拨错 DDI 进兜底组"是需求设计而非系统容错——写进方案文档
