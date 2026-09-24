# 成本档案（发票价调整与订阅费）

## R — 原文依据

> "• x is the total cost • Total cost = Direct carrier cost + ISDN cost+ Indirect carrier cost • A and B are constant"（p325）
> "Example 1: to add 10 % ­ If type = linear equation, A =1,1 and B = 0. ­ If type =Percentage, A = 10 and B is not used."（p333）
> "Subscription records are created at the start of the period: • Every day for daily records • Every Sunday for weekly records • On the first day of the month for monthly records"（p327）

出处：8770XTE201EN p322-340。

## I — 自述

成本档案（Cost profile）在运营商成本之上做第二层调价，分两块：

- 发票价（Invoiced cost w/o tax 页签）：对总成本（直连运营商成本 + ISDN 成本 + 间接运营商成本）做线性或百分比调整，按呼叫类型定义、随组织树继承
- 参数换算：+10% 写成线性 A=1.1 B=0，或百分比 A=10；+5% 且每通话加 0.1€ 写成线性 A=1.05、B=0.1 Euro（B 必须带币种）；A<1 或负值为折扣
- 订阅费（另两个页签）：Services subscriptions 按"拥有设备/语音信箱/DDI 号"、Station subscription 按"分机类型"计费，可按日/周/月、带币种与税
- 订阅出票机制：8770 在每次同步后生成"纯订阅费"记录——日票每日、周票每周日、月票每月 1 日，时间戳全 00:00:00；月订阅当月加入者从次月 1 日起计；订阅计算永不处理当天
- 存量更新：Compute cost 勾 Variable cost(s)（调整档案变更）或 Fixed Cost（订阅档案变更——机制是先删订阅记录再重建，量大时以天计）

## A1 — 书中案例

**发票价档案配置**（p331-340）：

1. Organization 页签 Cost Profile 图标打开，认知 Invoiced cost w/o tax 页签字段（Call Type/Type/A/B/Currency）
2. 复制 Default 建档案 "Root cost"：呼出 +50%
3. 复制 Default 建档案 "TSS cost"：呼出 +20% 且加固定 0.5€/通话
4. 组织根 Properties 的 Costs 挂 Root cost（全树生效）
5. TSS 成本中心 Inherited Costs=No，单独挂 TSS cost（仅该子树）
6. Compute cost 勾 Variable cost(s)=Yes 更新存量（改订阅档案则勾 Fixed Cost）
7. Records 页签核对 invoiced cost：TSS 子树按 +20%+0.5€、其余按 +50%
8. 讲义口径：订阅票在同步后生成，月订阅次月 1 日起计，订阅计算不处理当天

## A2 — 未来触发

使用情境：内部成本加价 20% 再收；每通话加固定手续费；按月收话机订阅费；月中入职的订阅费怎么算；改了订阅档案为什么重算跑很久；发票价和运营商成本对不上。

语言信号：成本档案 / cost profile / 发票价 / invoiced cost / 加价 / 折扣 / 订阅费 / subscription / Fixed Cost / Variable cost / Root cost / 每月 1 日 / 次月起计。

与相邻能力区分：运营商层算价与 Adjustment → 资费建模能力；本卡是入库后的第二层调价；档案挂载依赖组织树（组织成本归属能力）。

## E — 可执行步骤

输入契约：加价/折扣口径与订阅费表已获商务确认。口径未定 → 判停先确认，避免返工重算。

1. Cost Profile 页签复制 Default 建档案，按呼叫类型配 A/B。完成标准：换算对照（百分比与线性二选一）成立
2. 挂组织根做全树默认，按条目取消继承做差异化。完成标准：继承关系明确
3. 需要订阅费时配 Services/Station subscription（周期+币种+税）。完成标准：订阅口径成文
4. Compute cost 勾 Variable cost(s)（或 Fixed Cost）更新存量。完成标准：任务成功
5. Records 页签抽验 invoiced cost。完成标准：抽样值=手工复算

判停点：

- 月中加入的员工当月被收费/未收费争议 → 按机制答"月订阅次月 1 日起计"，售前提前讲清
- 订阅重算超过一天 → 机制是删了重建，量大以天计；避开业务高峰并预告时长
- 加价出现负值/异常 → 检查 A 的语义（百分比填 10 表示 +10%，负值为折扣）与 B 是否带币种

输出契约：档案参数表（A/B/币种/呼叫类型）+ 挂载矩阵 + 抽样复算对照 + 订阅口径说明。

## B — 边界

- 发票价调整作用于"总成本"（三类成本之和，p325）；运营商层调价（Adjustment）在本卡上游，属资费建模能力
- 订阅计算永不处理当天、可能持续数天（p327/p339）——当日出账需求不成立
- 订阅票与普通票同样受组织树/掩码/可见域管控（p327 "processed in the same way"）
- 教学百分比（+50%/+20%+0.5€）为实验口径，生产口径需商务确认
