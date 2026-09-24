# Rainbow 维护与支持体系（日志、状态页、告警、操作历史、SR）

## R — 原文依据

> "Your users can report problems they encounter directly in their Rainbow interface ('Help and Support' menu, 'Report a problem'). ... The integrator partner has the same reports as the customer"（p185）
> "status.openrainbow.com — The button « Get updates » allows ... you can subscribe to alerts by different methods."（p186）
> "The ESR will only be created if the partner is certified on Rainbow"（p191）

出处：RAINXTE001EN p182-194。

## I — 自述

运维闭环八个抓手：

1. **用户日志**：头像 → About Rainbow → Open logs（另有 User Settings 路径）
2. **用户问题上报**：Help and Support → Report a problem（日期/描述/附件/日志使用同意）；集成商与客户看到同一份上报
3. **云状态页**：status.openrainbow.com + Get updates 订阅告警（按主题/地域过滤）
4. **维护预告**：管理门户内查看计划维护（按地域与 Hybrid/Hub 架构过滤，颜色区分影响等级，多在晚间/周末）
5. **音频告警**：设阈值通知音质劣化与无音频
6. **操作历史**：全部管理操作留档，按类别/类型/日期过滤——多管理员审计"谁做了什么"
7. **Help Desk 指南**：help.openrainbow.com（排障/找日志/报障入口）
8. **SR**：邮箱 support@openrainbow.com / Emily BOT / Global Welcome Center / 电话；MyPortal 建单（category=Rainbow, type=product support + 终端客户公司/版本/子类/SIP trunk/来源等字段）；仅 Rainbow 认证伙伴会建 ESR

## A1 — 书中案例

**运维场景**（p182-193，讲义，无实验）——典型链路：

1. 用户上报问题
2. 管理端取事件日志
3. 对照状态页排除云侧故障
4. 需官方介入时经 MyPortal 开 SR（字段按 p192-193 两页表单）

## A2 — 未来触发

使用情境：用户日志在哪；怎么收集问题信息给支持；Rainbow 是不是全局故障；约了维护怎么提前知道用户；谁改了配置；怎么开 SR；SR 没被建。

语言信号：日志 / logs / report a problem / 上报 / status page / 状态页 / 维护窗口 / 告警 / alarm / 操作历史 / history / Service Request / SR / ESR / MyPortal / Emily。

与相邻能力区分：PBX 侧接入排障（Webdiag/ccrbagent.log）→ PBX 接入能力；网关媒体问题 → 网关部署能力。

## E — 可执行步骤

输入契约：问题现象与时间、用户端形态（Web/Desktop/移动）、伙伴认证状态（开 SR 前）。

1. 收集：用户日志（About Rainbow → Open logs）+ 用户上报记录（管理端看全部事件）。完成标准：现象可复述、日志在手
2. 分流：查 status.openrainbow.com 与管理端维护预告 → 云侧故障则订阅告警等待恢复；非云侧按现象转对应能力（接入/网关/成员）。完成标准：责任面确定
3. 审计（如涉配置变更）：操作历史按类别/日期过滤定位操作人与时间。完成标准：变更链路清楚
4. 升级官方：MyPortal → Support → Service Request → Create SR → 按两页表单填全（category=Rainbow、版本、子类、SIP trunk、来源等）。完成标准：ESR 建立

判停点：

- 伙伴未过 Rainbow 认证 → SR 不会被创建（n47）：先补认证或经认证上家转报，不要反复提交
- Web 端上报没有日期字段 → 平台设计（浏览器日志存活短）：改用客户端上报或靠附件/描述定位时间
- 怀疑账号冒用 → 转成员生命周期能力的 Security 改密手段（踢在线会话），不走本卡

输出契约：问题档案（日志+上报记录+分流结论）+ SR 单号（如升级）。

## B — 边界

- 状态页只覆盖云侧（数据中心/平台）；PBX 侧与局域网问题不在其监测面
- 告警阈值的具体取值方法原书外置（p188 链接指针）
- ESR 受理以 Rainbow 认证为前提：项目启动时先理顺支持路径（认证/上家关系）
- 法国站点订阅告警勾 WW/EMEA/DE 为书中举例（实验口径），按实际地域选择
