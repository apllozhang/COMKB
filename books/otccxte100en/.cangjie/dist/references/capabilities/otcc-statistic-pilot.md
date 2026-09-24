# 统计型 pilot 与 Call Tag（对外业务号/分业务统计）

## R — 原文依据

> "Get more pilots for greeting guides • Extend the possibilities of obtaining statistics on the pilots • The statistic pilots are used in ACR (advanced call routing)."（p544）
> "Up to 3000 statistic pilots can be declared … A routing pilot cannot be deleted if it's associated with statistics pilot(s)"（p546）
> "Call Tag Enter a call tag name (i.e. GOLD) Up to 32 characters to display during the ringing phase on the agent display."（p557）
> "The presentation voice guide of the statistics pilots … will be played if: • the routing pilot is in blocked State or general forwarding on rule • this rule is valid"（p545）
> "Pilot Stat. Directory Number Enter the directory number (i.e. 31650) … Routing pilot Enter the pilot to be associated with (i.e. 31600)"（p555）

出处：OTCCXTE100EN p543-565。

## I — 自述

统计型 pilot 是"对外业务号"层：主叫拨业务号 → 先播该统计 pilot 的问候指南 → 再转唯一关联的本地路由 pilot 走分发。它解决两件事：多条业务线各挂各的问候语、按业务号分账统计（g10/p22）。

硬规则（p546）：

- 最多 3000 个统计 pilot；只能溢出到一个本地路由 pilot
- 路由 pilot 被关联期间不可删除；统计 pilot 不能兼任 direct calls pilot

问候指南播放条件（p545/n33）：

- 路由 pilot 按"规则（rule）"关闭/阻塞且规则仍有效（至少 1 个方向开且可用）→ 播统计 pilot 对应状态问候
- 路由 pilot 按"指南/地址"方式关闭/阻塞 → 统计 pilot 问候不播，来话按路由 pilot 分发走
- 统计 pilot 无指南 → 播路由 pilot 的问候指南

Call Tag 与显示（p550/p557-558）：

- Call Tag ≤32 字符（如 GOLD），振铃期在座席话机显示；PG 参数 Call Tag Display Timer：0=仅振铃期、>0=振铃+接通后按秒数显示
- 座席显示四选一（按管理配置）：主叫号码 / pilot 名 / Call Tag / 实体名；无 tag 时显示主叫与 pilot 特征

网络场景：统计 pilot 号需经前缀（Meaning=Network No.，Type=Statistic Pilot）广播到各节点（p549）。

## A1 — 书中案例

**Gold 会员专线实验**（p553-565）：

1. OXE Applications> CCD> Statistic Pilot> Create：31650/Stat.Pil Gold，Routing pilot=31600
2. Navigator 开统计 pilot 显示并悬停核验设置
3. CCS Configurations> Statistics Pilot 配 Call Tag=GOLD
4. OXE PG 31800 的 Display on agent screen 选 Call tag or pilot characteristics
5. 建 701 问候指南、录 2701（"Welcome to our gold members"）装板
6. Configurations> Statistics Pilot 挂 Presentation guides> Normal：Guide n°=2701（原书如此，消息号口径见 nr-09）
7. 拨 0210X41650：先听 Gold 问候 → Agent1 应答、话机显示 GOLD
8. Statistics> Excel> Statistics Pilot 出 General 报表（粒度 1 小时）

## A2 — 未来触发

使用情境：多条业务线要不同的问候语与分业务报表；VIP 专线要在座席话机亮出标签；"统计 pilot 问候怎么不播"；删路由 pilot 报错；业务号溢出去向设计。

语言信号：statistic pilot / 统计 pilot / 31650 / Stat.Pil / routing pilot / Call Tag / GOLD / 问候指南 / presentation guide / Display on agent screen / Call Tag Display Timer / 业务号 / 分业务统计。

与相邻能力区分：路由 pilot 本身与方向 → 路由与分配规则能力；问候指南录制 → 语音指南能力；紧急关闭联动归直接呼叫与紧急关闭卡（路由卡）；ACR Profile 用法在书外。

## E — 可执行步骤

输入契约：业务线清单与各线问候文案已定、关联的路由 pilot 已运行、座席显示口径已定。

1. 建统计 pilot：OXE Statistic Pilot> Create，DN=业务号、Routing pilot=唯一本地路由 pilot。完成标准：Navigator 可见且关联成立
2. 配 Call Tag 与显示：CCS 填 ≤32 字符标签；PG 选 Display on agent screen 与 Timer。完成标准：振铃期座席话机显示标签
3. 建问候指南并挂接：按状态挂 Normal/Blocked/General forwarding 三态问候。完成标准：拨业务号先闻问候再转路由 pilot
4. 报表验证：Statistics> Excel> Statistics Pilot 出报表核对分业务计数。完成标准：业务线呼叫计入该统计 pilot
5. 问候条件核验：把路由 pilot 按 rule 关闭验证问候切换；按指南/地址关闭验证问候不播。完成标准：两种关闭方式行为与规则一致

判停点：

- 问候不播 → 查路由 pilot 关闭方式：按 rule 才播、按指南/地址不播（n33）
- Guide n° 填了不响 → 该字段书中为消息号口径（nr-09），换消息号/指南号两边都试并记录
- 删路由 pilot 被拒 → 有关联统计 pilot，先解除关联（p546）
- 想让统计 pilot 溢出到多个路由 pilot 或当 direct call pilot → 设计不允许（p546）
- ACR Profile（语言技能）挂载 → 书外域，指向进阶教材（n41）

输出契约：分业务号体系（统计 pilot+问候三态+Call Tag 显示）+ 分业务报表样例与问候条件核验记录。

## B — 边界

- 3000 个上限、单一路由 pilot 关联、不可兼 direct calls pilot 为 R10.16 硬规则（p546）
- ACR（高级路由）只在此点名：统计 pilot 用于 ACR，但 Profile/语言技能细节在进阶教材（p544/n41）
- 实验值（31650/GOLD/701/2701）为实验口径
- 网络多节点场景需前缀广播统计 pilot 号，跨节点行为本书仅一页（p549）
- 统计 pilot 问候与紧急关闭/日历关闭的叠加行为书中未展开，组合方案需现场验证
