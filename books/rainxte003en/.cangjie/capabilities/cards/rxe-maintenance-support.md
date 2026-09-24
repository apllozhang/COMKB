# Rainbow 维护与支持体系（日志/问题上报/状态页/告警/操作历史/SR）

## R — 原文依据

> "The integrator partner has the same reports as the customer, so he can help with end user support."（p248）
> "If you subscribe to alerts, you can filter by relevant topics and/or geographical areas. For France, it is useful to tick WW, EMEA & DE."（p249）
> "The ESR will only be created if the partner is certified on Rainbow"（p254）

出处：RAINXTE003EN p245-257。

## I — 自述

运维闭环五入口：

1. **Help Desk 指南**：help.openrainbow.com 的排障指南/找日志/定位网络或应用问题/报障流程（p246）
2. **用户日志与问题上报**：用户在 Rainbow 界面 Help and Support、Report a problem（日期时间+描述+截图+同意采集日志）；管理员端看全部用户事件并可下载事件日志；集成商与客户同视角（p247-248）
3. **云服务可用性**：status.openrainbow.com 状态页（Get updates 订阅告警，按主题/地域过滤）+ 管理门户的计划维护通知（按地域与 Hybrid/Hub 架构过滤、色标关键度、多在晚间周末）（p249-250）
4. **告警与操作历史**：可设阈值通知音频质量劣化与无音频；全部管理操作留档，多管理员场景查"谁在何时做了什么"，按类别/类型/日期过滤（p251-253）
5. **SR 流程**：入口为支持邮箱/Emily BOT/Global Welcome Center/电话；ESR 仅为持 Rainbow 认证的伙伴创建；MyPortal 建 SR 两页字段要一次填全（p254-256）

Web 端取证口径（p248）：网页模式上报不填日期——浏览器日志留存期短，拖几天再取证就没了；桌面/移动端要填日期时间。

## A1 — 书中案例

**运维场景走查**（p245-257，讲义章无分步实验）：

1. 多用户报登录问题：先查 status 状态页分流"云故障"与"局部问题"
2. 单用户问题：管理员进用户事件列表取日志，集成商同视角可代办
3. 用户自报：Report a problem 附截图与日志授权；Web 模式不填日期
4. 变更追责：操作历史按类别/日期过滤出操作人
5. 升级官方：MyPortal 建 SR 按两页字段清单填写（category=Rainbow、severity、版本、SIP trunk、how found 等）

## A2 — 未来触发

使用情境：用户说 Rainbow 全挂了；要开正式工单；查谁改了配置；音频质量差怎么留证据；帮最终用户取日志。

语言信号：日志 / logs / report a problem / 问题上报 / status / 状态页 / 告警 / alert / 操作历史 / audit / Service Request / SR / ESR / MyPortal / 认证伙伴 / Emily / Welcome Center。

与相邻能力区分：

- OXE 侧 agent 排障（incvisu/日志） → OXE 接入能力
- 网关侧 mpcheck 与三服务 → 网关部署能力
- 用户侧取证后的功能修复 → 按症状分流到对应能力卡

## E — 可执行步骤

输入契约：问题现象与影响面、发生时间窗、操作者账号与认证状态。影响面未知 → 先做云状态分流再深入。

1. 分流：status 状态页与计划维护通知判断是否云侧事件。完成标准：云故障/局部问题结论明确
2. 取证：管理员取用户事件日志；桌面/移动端让用户补上报（含日期）。完成标准：证据在手
3. 审计：操作历史过滤出变更人与时间。完成标准：责任链清楚
4. 自修或升级：可自修走对应能力卡；不能自修开 SR。完成标准：处理路径确定
5. 开 SR：MyPortal 按两页字段一次填全，附日志。完成标准：工单建立且可追踪

判停点：

- 伙伴未持 Rainbow 认证 → 停，ESR 不会被创建（p254），先补认证或经认证伙伴转报
- Web 端问题拖了几天 → 浏览器日志已过期，取证窗口错过，换桌面端复现
- 状态页正常但全网不通 → 查客户侧网络，转网络就绪与 OXE 接入两能力
- 想跳过 MyPortal 直接邮箱报障 → 可行但字段不全拖慢分派，工程上仍按字段清单备料

输出契约：分流结论 + 证据包（事件日志/上报记录/操作历史）+ SR 工单号与字段清单。

## B — 边界

- SR 入口多（邮箱/BOT/Welcome Center/电话）但建单门槛唯一：认证伙伴（n29）
- 计划维护多在晚间周末执行；订阅告警漏勾地域会收不到事件（p249-250）
- OXE/网关侧的命令级排障在 OXE 接入与网关部署两能力，本卡只管云侧与流程
- 描述里附 rainbowagent.log 或 mpcheck 输出可加速定位（工程经验，书内未明示）
