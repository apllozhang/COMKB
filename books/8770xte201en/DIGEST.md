# DIGEST — OmniVista 8770 计费与性能管理精华长文

> 源：8770XTE201EN Edition 45（650 页，OmniVista 8770 R5.2 Accounting and Performance Administration）· 文档整理入库 · 2026-09-24
> 定位：10 分钟建立对 8770 计费与性能交付的全局认知；操作细节按需查 13 张能力卡。

## 一、这套东西是什么

OmniVista 8770 是 ALE 的集中网管服务器：IP 连通即可纳管 OmniPCX Enterprise（OXE）、OXO Connect 与 OpenTouch，把 PBX 的话务数据变成**钱**（计费）和**性能结论**（监控）。

整本教材是一条交付主线：**OXE 开计费出票，8770 增量回收入库，配运营商资费算成本，用组织树/掩码/可见域管住"谁能看多少钱"，报表出账，四件套监控质量，归档收尾**。

六个数字先记住：

| 数字 | 含义 |
|---|---|
| 500 条 / 90 分钟 | OXE 票据缓冲上限与定时落盘间隔（满、超时、account compress 三时机落盘） |
| 五种计费方法 | 每台 PCX 各选一；建树期用 Organization update，树定型切 Detailed |
| 31 + 94 = 125 天 | 计费票归档与清理生命周期，按记录日期而非文件日期清理 |
| 150ms / 3% / 5% | VoIP KPI 默认阈值：时延、丢包、BFI Burst（BFI>3% 才统计 burst） |
| 400 行 / 50 页 / 100000 行 | 报表尺寸上限：TXT、HTML/PDF/EXCEL、数据库扫描 |
| 仅 OXE | 审计与流量分析的平台边界；OXO Connect 只有计费票据与 VoIP 报告 |

## 二、计费管道：数据从哪来到哪去

- **出票（OXE）**：呼叫结束生成 47 字段票据（ED5.2），先进内存缓冲（≤500 条）；缓冲满、90 分钟无新票、account compress 三个时机落盘成 TAX*****.DAT 并登记 ACCOUNT.LIS。两条出票边界：外线未接通也出票（所以有 "Public Outgoing 0 Units calls" 类别），本机-本机只有接通才出票。
- **开启（OXE）**：Files for External Accounting=Yes，存储上限默认 31 天（=744 个压缩文件）；过滤器必选 0 计费呼出；PIN 与被叫遮蔽设"不遮"——遮蔽归 8770 管，OXE 侧遮了就永远解不开。
- **回收（8770）**：对比两侧 ACCOUNT.LIS，FTP 增量取回，过五道加载闸入库（成本在此步算），最后删远端文件更新索引。FTP 用户名 adfexc 禁改（许可校验），密码必须与 OXE 一致。
- **验证**：loader 目录出现文件、组织树 Records 页签有数、NMCLD_1.log 的 TicketsRead 与速度（实验口径 9 张票 52 tic/sec）。断在哪一段就查哪一段的目录与日志。

## 三、钱的三层：资费、组织、加价

- **资费层**：运营商 > Period > Calendar/Region/Tariff/Direction。被叫前缀按最长匹配归属（同一前缀不能跨区，加新主叫区先删旧归属）；方向配对唯一绑定资费。费率可复算：

| 模式 | 公式 | 书中示例 |
|---|---|---|
| exact 线性 | 分钟数×单价+剩余秒×(单价/60) | 2m24s = 2×0.03+24×(0.03/60) |
| +接通费/免费时长/保底 | initial cost、initial duration、minimum cost | 180s 内=0.1；≤90s 按 0.045 |
| 分段 segments | 按段序扣减 | 7m24s = 3×0.08+4×0.07+24×(0.06/60) |
| round up/down | 阶段开始即计/计满才计 | 60s 阶段×0.1 时 2m30s 为 0.3/0.2 |
| 脉冲 pulse | Charge units×单价 | cost = 12×0.03 |

- 特服号服务费独立建模：总票价=通信费 C+服务费 S，必须双资费并在方向上成对绑定，漏一个就漏收。
- **重算铁律**：成本在加载时算好，改配置必须 Compute cost（勾 Force）重算存量；日志报 "No first carrier found" 两类根因——前缀漏配、号码落在多运营商被叫区无法抉择。
- **组织层**：组织树决定钱归谁。成本中心从 OXE 同步（cc=255 落根、中继组等落默认成本中心）；分机改归属只能回 OXE 配置，组织图上剪贴会被拒；剪贴无历史、复制留灰色条目；历史回溯只能选"设备"，ToolsOmniVista 全局更新强制停服务且不可逆（先归档）。
- **加价层**：成本档案对总成本做第二层调价（+10% 即线性 A=1.1 或百分比 A=10；+5%+0.1€ 即 A=1.05、B=0.1€）；订阅费日/周日/月一出票、时间戳 00:00:00，月订阅次月 1 日起计。

## 四、谁能看多少钱：机密三道闸

1. **掩码档案**：按呼叫类别遮被叫/主叫/PIN/成本/地名/时长/日期的显示位数，随组织树继承；Default 档案不可删（遮蔽位数清 0 即停用）；**grouped 报表无视子树档案，只认 Default 的两个 group 类别**——合规验收两型报表都要测。
2. **解密权限**：默认禁止无掩码报表；账号加入 Mask data access 组、生成时索要组员口令；改组必须关闭并重开 Reports 应用。
3. **可见域**：开启开关后必须重启计费应用，未配域时整树只剩根（看似数据全丢，实为顺序）；域按父继承；群组域无效只认用户级。

OXE 侧已遮蔽的号码（横杠形态）8770 任何手段无法还原——排障先查 OXE 出票参数。

## 五、报表：交付可见成果

- 预定义报表必须复制到个人目录才能生成；Querytool 管字段/Operation/公式/过滤/hit-list，Designer 管版面/前后缀/小数位/图表。
- 三条版面硬规则：图表与公式只能取同一视图区域字段（嵌套汇总要切 View）；中间层合计不想显示唯一办法是前景空白遮蔽；grouped 末页空表头靠共有字段做组头顶掉。
- 六项上限（TXT 400 行、HTML/PDF/EXCEL 各 50 页、X 轴 100、库 100000 行）超限截断；累计报表空表先手工 Total calculation（夜间计数器没算不是故障）。
- 邮件导出与 Tracking 告警共用邮件服务器参数：server:port 无空格、端口 25 可省、发件人须被服务器认识。
- 题面笔误两处（汇率 1.21 与 1.3 并存、report #4 题面 Telecom 7/0）照实现章与交付约定为准。

## 六、性能四件套

- **VoIP 性能**（厚客户端报表）：每段 IP 通话出 IP ticket；KPI 默认时延>150ms、丢包>3%、BFI Burst>5%；报告有数的前提是话务走被监控承载段（实验口径：跨 POD 出局，同机软话机互打无效）。
- **流量分析**（仅 OXE）：半小时 pmm 计数器；出厂默认只算话务台/话务台组/中继组，要看被叫号与终端必须把 Daily/Weekly 两个 Job 的 PtpType 改成 ALL。
- **Tracking**：阈值集合档案挂实体类型，超限出告警和/或邮件；变化率=100×(当前值−前 x 期均值)/前 x 期均值，移动平均默认日 30/月 3/年 1 期；由任务驱动非实时；Reset Profile 才是全量强制。
- **Web Performance**（WBM 仪表盘）：VoIP CDR + OXE SNMP MIB（SNMPv3）两条数据腿，五大主题 widget；R5.0 MD1 起轮询可从 30 分钟缩到 5 分钟；**双侧 SNMP 配置不一致时 8770 出告警并停用监控**——改口令要当一次变更窗口的两步做。

## 七、数据寿命与红线

- 归档：31 天后拷入 archZ（每天每节点一档），再 94 天后删，最长 125 天，按记录日期清理；Archive Delay 不带 D、Clean-up delay 必带 D。
- 恢复标签二选一：Loaded records 与原始票完全无法区分；Archived records 打标、树中不可见、可单独清除——审计场景一律用后者。

三条红线：

1. 教材全部密码/账号/网段/税率/汇率是实验值，上生产必须换
2. 真实运营商价目、数据库容量与备份、SNMP 凭证治理、留存合规在书外
3. 多节点组网、PCS、OpenTouch 关联同步只有概念图无实验，生产部署须另行验证

## 八、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 接新 OXE/SIP 中继对接 | ovbill-node-onboarding |
| 开计费/配回收/查没话单 | ovbill-ticket-pipeline |
| 建运营商/算成本/排成本日志 | ovbill-tariff-costing |
| 迁移运营商配置/修 .itl | 路由入口（ovbill-codebook-migration） |
| 搭组织树/修历史归属 | ovbill-org-costing |
| 遮蔽/解密/可见域 | ovbill-confidentiality |
| 发票价加价/订阅费 | 路由入口（ovbill-cost-profile） |
| 生成/导出/定时报表 | ovbill-reporting |
| 从零造报表定义 | ovbill-report-design |
| VoIP 质量报告与 KPI | ovbill-voip-monitoring |
| 话务报表/阈值告警 | 路由入口（ovbill-traffic-tracking） |
| 实时仪表盘/SNMPv3 | 路由入口（ovbill-web-performance） |
| 归档/恢复/清除 | 路由入口（ovbill-archiving） |

## 版权

- 本精华长文为 ALE Training Services《OmniVista 8770 R5.2 — Accounting and Performance Administration》（8770XTE201EN Edition 45）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
