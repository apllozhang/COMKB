# Book Overview（参考区）— OTCC Standard Starter

> 供能力卡引用的背景参考；源自 references.md 落位。

## 交付主线（组织轴）

环境准备（RLAB/POD/ITSP1） → CCD 矩阵模型讲义 → 基础矩阵创建 → CCS 安装声明 → 路由与分配规则 → 座席班长体系 → 收尾 POD 与 ABC-F 内呼 → 逐域加能力（调优/语音指南/班长特性/EWT/监控/直接呼叫/Excel/紧急关闭/统计 pilot/欢迎指南/多语言/日历）（p3-642）。

## CCD 五级矩阵模型（全书智力骨架）

- 来话先落 pilot（被叫部门，三态：Open/General Forwarding/Blocked，Blocked 是"下游无资源"的自动态）→ 路由规则（每 pilot ≤30 条，优先级 0-9，平局看 EWT）→ 等待队列（三类型四状态，FIFO，6 个 parking level）→ 分配规则（全局 ≤10 条，资源选择平局看 LIT、呼叫选择平局看真实等待）→ 处理组（五类型，Voice Guide PG 只接 Redirection 队列）→ 座席选择（p22-62）。
- 两条"默认关"：分配规则默认停用（OXE 侧激活）、所有方向默认关闭（p113/p117）。

## 双控制台分工（p79 硬边界）

- OXE Web Admin（https://192.168.1.3，mtcl）：建/改 CCD 底层对象（前缀/PG/队列/pilot/CCD Users/Statistic Pilot/分配规则激活/语音指南/COS/译码/中继组）。
- CCS（CCsupervision）：路由与分配规则、座席属性与挂组、pilot/队列/PG 参数、Navigator 实时、Excel 统计、紧急关闭；只能新建 CCS 班长与分配规则。
- 第三入口：OXE 控制台/SSH（mtcl）：acdsup、vgstat、hybvisu、rsthyb、config。

## 实验环境（RLAB，仅 Boundary 背景；全部为实验口径）

- POD 五实例（p9）：OXE（OTCC_OXE，192.168.1.1/1.3，账号 mtcl/swinst/root，口令 Superuser2580*）、OMS（192.168.1.13）、FlexLM（192.168.1.80，letacla1）、Client PC10（192.168.1.10，IPDSP 31000 + MicroSIP 31010/31011/Public）、Client PC11（192.168.1.11，IPDSP 31001）。
- ITSP1 模拟器（p14-17）：SIP 网关 gateway1.itsp1.com（10.20.30.51，注册 pbxP/alcatel）+ 公网网关 public.itsp1.com（10.20.30.50）；安装号 3321PN、DDI 首外线 41000/首内线 31000；打 pilot 拨 0210X41600/0210X41601（X=POD 号）；本地内呼拨 00210X…。
- 法国目标库实验资源：ACD 前缀 12（+1 退出/+2 wrap-up/+3 呼班长/+5 登出/+6 登入/+91/+92）、401 录音、580 试听；OMS 板位 4-0；备份音 56、默认演示指南 70、直连阻塞默认 75；518/538 与消息 3226-4217 系统预置。
- CCS 侧实验口径：administrator/alcatel 默认（首登强制改密，实验改 Superuser01*）、功能码个人码 0000、Excel 表单保护密码默认 alcatel（p502）。
- 实验矩阵对象：Agent_PG(31800)/Forwarding_PG(31801→31010)/Voice_guide_PG(31802)；Normal_WQ(31700)/Overflow_WQ(31701)/Redirection_WQ(31702)；Pilot1(31600)/Pilot2(31601)/Direct call(31603)/Offer(31601 改名)/After-Sales(31600 改名)/Stat.Pil Gold(31650)。

## 关键数值速览（引用需带 R10.16 口径）

| 数值 | 含义 |
|---|---|
| 0-9（0 最高） | 路由/资源选择/呼叫选择统一优先级域 |
| 30/50/1200 | 每队列被 30 pilot 共享、服务 50 PG；每 pilot 30 条规则、全局 1200 |
| 10 / 50 方向 | 分配规则全局 10 条；每队列最多 50 个分配方向 |
| 1-3276 秒 | pilot wrap-up/pause 与 PG 计时器数值域（删 wrap-up 填 0、删 pause 填 none） |
| 50 列×600 pilot | 紧急关闭列表容量（列表名 ≤16 字符） |
| 3000 | 统计 pilot 上限（单一路由 pilot 关联） |
| 10/20/50 | pilot 日历 10 切换/日、分配日历 20 切换/日、50 特殊日 |
| 100 | 518 位次播报上限（1-50 逐个、51-100 步进 5）；三级告警各存 100 条 |
| 3 秒 / 5-60 分 / 15 分 | Navigator 快照 / MSP / SOP（实验 15 分档） |

## 教材口径声明

- 全部实验密码/账号/号码/前缀仅限实验环境；生产必须替换并做安全加固（原书明文口令遍布正文，引用一律标"实验口径"）。
- 生产化边界三文档：Feature list OmniTouch Contact Center Standard Edition（兼容与功能矩阵）、OTCC901 Advanced Training（CCIVR/ACR/宏/录音第四法）、目标库文档（国家默认差异）。
- 书内矛盾已知 8+ 处（口令、建队列表格、acdsup/acdsetup、语言索引、编号笔误等）——以 verified.md / needs-review.md 的裁决为准（nr-01..nr-11）。
- 版本敏感点：SFTP 强制始于 OXE N3；ABC-F 链路默认始于 R100/N1（两说，nr-04）；ShowStatisticWithData 始于 CCS 10.5。
