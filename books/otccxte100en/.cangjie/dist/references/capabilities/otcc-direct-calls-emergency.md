# CCD 直接呼叫与紧急关闭（direct call pilot/私人号/一键关闭）

## R — 原文依据

> "Select Applications> CCD> Processing Group> 31800> … Pilot Direct Call Enter the processing number for pilot direct call (i.e. 31603)."（p467）
> "Warning … THE LOCAL HYBRID LINK CANNOT BE USED FOR THE DIRECT CALL FACILITY."（p469）
> "the pilot is blocked and the incoming call follows the direct call pilot configuration which is, by default, the voice guide #75."（p473）
> "Up to 50 pilot lists can be created … 600 pilots maximum in each list"（p528）
> "Transfer to a pilot in emergency closure is only authorized if an emergency closure address has been configured and is reachable."（p528）
> "You MUST be a CCS ADMINISTRATOR to be able to select the pilot in the emergency closure pilot list."（p542）

出处：OTCCXTE100EN p449-476, p527-542。

## I — 自述

CCD 直接呼叫把"座席直通号"纳入呼叫中心待遇，三要素（f20/p20）：

- pilot direct call（实验 31603）：承接座席忙/不可用时的溢出，提供 wrap-up/pause 计时；PG 参数 Pilot Direct Call 指向它
- Outgoing ACD Call（PG 参数）：座席外呼也计入 CCD 统计、吃 wrap-up/pause
- 私人号码（private agent number）：登录时自动前转到座席号、登出自动取消（p454）

呼叫性质按座席状态逐格判定（p455-456）：空闲/部分退出打座席号=ACD 呼叫；忙（事务码/wrap-up/通话/pause）=溢出 pilot direct call；不可用/pause=带介绍指南的 direct call；登出=听"分机停用"；打私人号一律私人呼叫；去话在不可用态为私人呼叫，其余为 CCD 呼叫。

紧急关闭（g13/p21）：

- 一键手动关闭一列 pilot：≤50 个列表、每列表 ≤600 pilot、列表名 ≤16 字符
- 激活后来话优先转关闭地址（配置且可达）否则播关闭指南；向关闭中 pilot 转移仅在地址已配置且可达时放行
- 联动：pilot direct call 被关闭时，无论座席状态，打座席的直达来话同样优先转关闭地址/指南
- 统计归属：关闭期间来话计入"通用转发态来话"计数器（p529）

## A1 — 书中案例

**直接呼叫五场景**（p460-476）：

1. OXE 建 pilot 31603/Direct call；CCS 建规则加 Normal_WQ 方向并激活
2. pilot 计时 pause=5、wrap-up=10；PG 31800 设 Pilot Direct Call=31603 并启用 Outgoing ACD Call
3. CCD Users 给 Agent1 配 Private agent No.=31000
4. 打私人号 0210X41000 → 私人呼叫无计时；打座席号 0210X41500 → CCD 呼叫、话机显示 31603、挂机走 31603 计时
5. 登入态去话=CCD 计时；退出去话=私人无计时；不可用态来话听 31603 阻塞指南（默认 #75，改配 685）
6. 部分退出态来话去话均按 CCD 处理；全程走公网入口（本地 ABC-F 链路禁用于 direct call）

**紧急关闭演练**（p531-542）：

1. Emergency closure 建 Emergency0 列表，选入 31600/31601/31603
2. OXE 建 640 指南、录 2640 关闭提示、装板；pilot Closure addresses 挂 Emergency closure=640
3. Activate 后两 pilot 来话均播关闭消息；History 查操作记录
4. 测完 Deactivate 复位（书中明令勿忘，n05）

## A2 — 未来触发

使用情境：给座席配对外直通号并要进统计；"直通号打不通/没计时"；私人号怎么配；突发情况一键关停业务号；应急演练方案；关闭后座席转接被拒。

语言信号：direct call / 直接呼叫 / 31603 / private number / 私人号 / Pilot Direct Call / Outgoing ACD Call / #75 / emergency closure / 紧急关闭 / Emergency0 / 关闭地址 / 关闭指南 / History / Deactivate。

与相邻能力区分：座席登录登出与私人号联动前提 → 座席班长体系能力；统计型 pilot（对外业务号）→ 统计 pilot 卡（路由卡）；通用转发（班长逐 pilot 关闭）归座席班长特性能力。

## E — 可执行步骤

输入契约：座席体系已运行、直通号/关闭策略与去向已定、演练须有复位计划。

1. 建 direct call pilot 并配规则方向。完成标准：pilot 可路由
2. PG 侧挂接：Pilot Direct Call=该 pilot，按需启用 Outgoing ACD Call。完成标准：座席忙时来话溢出可见
3. 配私人号：CCD Users 填 Private agent No.（编号计划内）。完成标准：登录时前转生效、登出自动取消
4. 五场景验证：私人号/座席号/登入去话/退出去话/不可用来话逐个测性质与计时。完成标准：判定表逐格吻合且全程走公网入口
5. 紧急关闭演练：建列表选 pilot，挂关闭指南/地址后 Activate，拨测并留 History 痕迹。完成标准：来话播关闭消息且转移行为符合地址配置
6. 复位：Deactivate 关闭列表并复核 Navigator 状态。完成标准：无遗留关闭态

判停点：

- 本地内呼链路上测 direct call 不通 → 硬约束：ABC-F 链路不能承载 direct call，必须走公网入口（n04）
- 不可用来话一声就断 → 默认阻塞指南 #75，上线前显式配阻塞指南或关闭地址（n24）
- 紧急关闭界面选不了 pilot → 权限设计：需 CCS ADMINISTRATOR（n05）
- 演练完忘了复位 → 高危遗留操作，Deactivate 必须进演练清单（n05）
- 只配关闭指南没配地址时转接被拒 → 预期行为，演练前向座席交底（n34）

输出契约：纳入统计的直通号体系（pilot/私人号/判定表验证记录）+ 紧急关闭预案（列表/指南/地址/演练与复位记录）。

## B — 边界

- direct call 机制依赖公网中继，本地 ABC-F 链路不可用（n04）；私人号须在编号计划内（p454）
- 欢迎指南不在 direct call 来话上播放——个性化问候方案要重新设计（n31）
- 紧急关闭容量 50 列×600 pilot、转移限制、统计归属为 R10.16 口径（p528-529）
- 直连阻塞默认指南 75 与备份音 56 为预置资源（g43）
- 实验 DN（31603/31000/41000/41500）与口令为实验口径
