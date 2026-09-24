# Hub 维护与支持体系（日志、设备监督、状态页、上报、SR）

## R — 原文依据

> "Click on your avatar ... then on About Rainbow and click on Save logs. A .zip file is created, send it to your support"（p332）
> "status.openrainbow.com ... The button « Get updates » allows, if you wish, you can subscribe to alerts by different methods."（p338）
> "The ESR will only be created if the partner is certified on Rainbow Hub."（p341）

出处：RAINXTE101EN p330-343。

## I — 自述

Hub 运维闭环八个抓手：

1. **Help Desk 指南**：help.openrainbow.com 的排障/找日志/报障入口（p331）
2. **用户日志**：头像 → About Rainbow → Save logs 出 .zip 发支持（p332）
3. **设备监督**：BP 管理端 Communication/Devices 看连接状态、IP、端口、版本，可开 debug、重启、恢复出厂（详见设备维护能力卡）
4. **连通性核查**：SIP 话机部署问题先查路由器协议支持；ALE SIP 终端不支持经 HTTP 代理穿越（p334）
5. **话机日志**：管理端开 debug 会话（≤15 分钟、一次性 TOTP 口令）登设备 web 页取日志/pcap/复位（详见设备维护能力卡）
6. **用户问题上报**：Help and Support → Report a problem；集成商与客户看到同一份上报，可据此代维；Web 端不采集事发日期（浏览器日志存活短，p337）
7. **云状态页**：status.openrainbow.com——数据中心故障官方信息源；Get updates 订阅告警，按主题/地域过滤（法国勾 WW/EMEA/DE 为书中举例）；配套管理端内计划维护公告（按地域与 Hybrid/Hub 架构过滤，多为晚间周末，p339）
8. **SR 服务请求**：入口四种——support@openrainbow.com 邮件、Emily BOT、Global Welcome Center（ALE 国际伙伴主入口）、电话；MyPortal 建单两页表单（Product Category=**Rainbow Hub**）；ESR 只为认证 Rainbow Hub 的伙伴创建

## A1 — 书中案例

**运维场景链路**（p330-343，讲义，无独立 How-To）：

1. 用户从客户端 Report a problem 上报（重要故障引导装客户端，Web 端无日期字段）。
2. 管理员取用户日志 .zip（About Rainbow → Save logs）。
3. 查 status.openrainbow.com 排除云侧故障，必要时订阅告警。
4. BP 管理端 Devices 区查设备状态，按需开 debug/重启（15 分钟窗）。
5. 需官方介入时经 MyPortal 按两页表单开 SR（认证前提先核）。

## A2 — 未来触发

使用情境：用户说平台挂了怎么分流；怎么收集信息给支持；约了维护怎么提前告诉用户；谁改了配置；SR 提交了没建单；话机批量离线先查哪。

语言信号：日志 / logs / Save logs / report a problem / 上报 / status.openrainbow.com / 状态页 / 维护预告 / 告警 / Get updates / 设备监督 / debug / Service Request / SR / ESR / MyPortal / Emily BOT / 认证。

与相邻能力区分：话机日志采集的详细步骤与 15 分钟 debug 窗归设备维护能力；接入/注册类故障的第一分流归设备部署与设备维护能力；分析口径（MOS/CDR）归分析能力（路由卡）。

## E — 可执行步骤

输入契约：问题现象与时间、用户端形态（Web/Desktop/移动/话机）、影响面（个人/组/全站）、伙伴认证状态（开 SR 前）。

1. 收集：用户日志 .zip + Report a problem 上报记录（管理端与客户同视角）。完成标准：现象可复述、日志在手
2. 分流：查 status.openrainbow.com 与管理端维护预告 → 云侧故障则订阅告警等恢复；设备类转设备维护卡；配置类转对应能力卡。完成标准：责任面确定
3. 设备面处置：Devices 区看连接状态/版本 → 按需开 debug（15 分钟窗）或重启。完成标准：设备侧证据链在手
4. 升级官方：核认证状态 / MyPortal / Support / Service Request / Create SR → 按两页表单填全（Product Category=Rainbow Hub）。完成标准：ESR 建立

判停点：

- 伙伴未过 Rainbow Hub 认证 → 停，SR 不会被创建（n54）：先补认证或经认证上家转报；注意认证科目按产品线区分（needs-review nr-04）
- 用户坚持"全部挂了" → 先查状态页与维护预告再行动，不要盲改租户配置
- Web 端上报没有日期字段 → 平台设计（p337，n53）：重要故障引导装客户端上报
- 话机批量注册不上 → 先查网络（HTTP 代理不支持、端口表，n52），再考虑 SR

输出契约：问题档案（日志+上报+分流结论）+ SR 单号（如升级）+ 维护窗口沟通记录。

## B — 边界

- 状态页只覆盖云侧；客户局域网/设备侧问题不在其监测面
- 计划维护公告在管理端内（p339），与 status 页分工不同；两者都看再下"平台正常"结论
- 实验环境（MicroSIP/RLAB）的运维约束不适用生产（n56，实验口径见 needs-review nr-06）
- debug 会话与 TOTP 口令的机制细节属设备维护能力卡；本卡只做分流
- SR 表单字段为 Sprint 170 口径（p342-343），随 MyPortal 演进以实际表单为准
