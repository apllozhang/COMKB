# DIGEST — OmniTouch Contact Center Standard 入门精华长文

> 源：OTCCXTE100EN Edition 09（649 页）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 OXE 内置呼叫中心（CCD + CCS）入门交付的全局认知；操作细节按需查 13 张能力卡。

## 一、这套东西是什么

OTCC Standard Edition 是**内置在 OmniPCX Enterprise（OXE）里的呼叫中心**：CCD 分配软件长在呼叫服务器内，不是外挂平台；可选件只有 CCS（班长台）、CCA、ACR、Soft Panel 四个。交付主战场就是两个图形台——OXE Web Admin 与 CCsupervision（CCS）——外加 mtcl 命令行（p21-23）。

一切呼叫流服从五级矩阵：**pilot、路由、队列、分配、处理组**。配置的本质是在这五级上"连方向、定优先级、给默认行为"（p22-29）。

三个先记住的口径：

| 口径 | 含义 |
|---|---|
| 默认全关 | 分配规则默认停用（须 OXE 激活）、所有方向默认关闭——"配好了不通"先查这两处 |
| 优先级 0-9 | 0 最高 9 最低；平局规则三类各异：路由看 EWT、资源选择看 LIT、呼叫选择看真实等待时间 |
| CCS 无权建对象 | 中继组/pilot/队列/处理组/座席只能 OXE 侧建；CCS 只能建班长与分配规则（p79） |

## 二、入门交付闭环（八步主线）

1. **建矩阵**：ACD 前缀（实验 "12"）先行，再建 3 类处理组（Agent/Forwarding/Voice guide，兼容硬约束：Voice Guide PG 只接 Redirection 队列）、3 类队列（Normal/Intelligent Overflow/Redirection）、pilot（p63-77）
2. **装 CCS**：CCS.msi 决策链（Full/Monosite/Excel=Yes）；node1 直连 OXE 后必须重启；ccs.ini 的 id_terminal 0..127 全网唯一（p89-97）
3. **建规则**：路由规则连 pilot 与队列（30 条/pilot），分配规则连队列与 PG（全局 10 条）；优先级常态方向最小；分配规则必须回 OXE 勾 Active Rule（p98-120）
4. **建人员**：ACD 话机 + 座席 + 班长；三种座席形态（固定/移动/自指派），班长恒自指派无优选组；前缀 "12" 全家桶登入登出（p121-149）
5. **通链路**：POD 收尾（SIP 网关 pbxN、DID 翻译、RDP 音频）打通公网来话；ABC-F 同节点不同网络、双 access UP 打通内呼（p150-165）
6. **调参数**：wrap-up/pause（1-3276 秒，自动挂 pilot、手动挂 PG）、服务水平 85%/15s 与 smiley 三色、PG 八选项逐项行为测试、队列饱和与改址（p166-193）
7. **配体验**：语音指南三路径（"401" 录音/".wav"+SFTP 导入/"538" 欢迎指南）、EWT 分档播报、"518" 排队位次（p194-264, p348-400）
8. **管运营**：Navigator 3 秒快照、三级告警各存 "100" 条、Excel 报表（"132" 行偏移）、紧急关闭、统计 pilot、双日历（p401-642）

## 三、关键表

**队列与 PG 兼容**（p40）：

| 队列类型 | 可接 PG |
|---|---|
| Normal | Agent / IVR / Forward / Rerouting |
| Intelligent Overflow | Agent / IVR / Forward / Rerouting |
| Redirection | Agent / IVR / Forward / Rerouting / Voice Guide |

**容量上限族**（p27/p43/p54/p103/p528/p546）：

| 对象 | 上限 |
|---|---|
| 队列共享/服务 | 30 个 pilot / 50 个 PG |
| 路由规则 | 每 pilot 30 条、全局 1200 条 |
| 分配规则 / 分配方向 | 全局 10 条 / 每队列 50 个方向 |
| 紧急关闭 | 50 个列表 × 每列 600 pilot |
| 统计 pilot | 3000 个（单一路由 pilot 关联） |
| 停车级 / EWT 阈值 | 6 级 / 每表 6 阈值 |

**座席状态时序**（p275-280）：空闲、振铃、通话之后，挂机进自动 wrap-up（pilot 计时器，可被打断），再到 pause（可接私人电话）后回闲；手动 wrap-up 挂 PG（默认口径 600 秒）；wrap-up 中做任何操作（除 Queue info）即取消。

**"518" 位次播报**（p377-383）：1-50 位逐个精确、51-100 位按 5 步进向上取整（63 位播 65）、Max position 上限 "100"、超限播提示音、语言缺失走回退链（默认语言→不播）。

**双日历**（p607-616）：pilot 日历 "10" 切换/日（规则 ID+Nor/Fwd）、分配日历 "20" 切换/日（方向与参数）、特殊日 ≤"50" 个覆盖周历；切换只在时间点执行——改活动时间片不立即生效（p638）。

## 四、排障金句（来自原书 Warning/Notes）

- 矩阵看着齐全、来话全走不通 → 方向没开（p117 "BY DEFAULT, ALL DIRECTION RULES ARE CLOSED"）
- "没动配置客户打不通" → 末座席下班，pilot 自动 Blocked（p26/p28）
- wrap-up 怎么改都不生效 → 自动挂 pilot、手动挂 PG，调错了对象（p277-278）
- 中继组实时唯独空白 → OXE 侧 CSTA-Monitored 没开（p414）
- EWT 测试不切换 → TSP 滞后，别用单通呼叫下结论（p373）
- direct call 在内呼链路上测不通 → 硬约束：ABC-F 不能承载 direct call（p469）
- 紧急关闭选不了 pilot → 需要 CCS ADMINISTRATOR；测完必须 Deactivate（p542）
- 改了日历不生效 → 切换点才生效，测试提前几分钟改（p638）

## 五、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 建 pilot/队列/处理组、acdsup 判读 | otcc-ccd-matrix-foundation |
| 装 CCS、ccs.ini、连不上 | otcc-ccs-installation |
| 建规则、设优先级、呼叫不通 | otcc-routing-distribution-rules |
| 建座席班长、登录登出、形态选型 | otcc-agent-supervisor-onboarding |
| wrap-up/SLA/PG 选项/饱和溢出 | otcc-object-tuning |
| 监听强插/通用转发/事务码 | otcc-supervisor-features（路由卡） |
| 录语音/传 .wav/欢迎指南 | otcc-voice-guides |
| 监控大屏/告警/Excel 报表 | otcc-monitoring-statistics |
| 多语言播报/节假日日历 | otcc-multilanguage-calendar |
| EWT 分档/排队位次/直通号/紧急关闭/统计 pilot/实验环境 | 路由入口（otcc-standard-starter-router） |

## 六、边界与红线

1. 教材全部密码/账号/号码/前缀是 RLAB 实验值（法国目标库），上生产必须整体替换
2. 话务建模（话务量→队列数→座席数）书外——原书只有 EWT/TSP 公式与"逐步调参"口径
3. CCIVR、ACR、CCA、Soft Panel、ALE Connect、多站点、Excel 宏（ACDMacro）只点名不展开，指向 OTCC901 进阶教材与 Feature list
4. 原书自相矛盾 8+ 处（口令两写、建队列表格复制错误、acdsup/acdsetup、语言索引漂移等）——引用以 needs-review.md 裁决为准
5. Rainbow 只以"座席形态"进本书：三不限制 + 三种登录；网关与平台部署书外

## 版权

- 本精华长文为 ALE Training Services《OmniTouch Contact Center Standard Edition — Starter》（OTCCXTE100EN Edition 09）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
