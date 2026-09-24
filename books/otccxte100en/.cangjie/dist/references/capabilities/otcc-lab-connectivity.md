# 实验环境与链路打通（POD 收尾/ITSP1/ABC-F 内呼）

## R — 原文依据

> "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data center."（p5）
> "PBX installation nb 3321PN … DDI table - First external nb 41000 … Example: 31002's external nb 3321PN41002"（p16）
> "configure 2 parameters in your external SIP gateway: • Registration ID: pbxN (where N is your POD Number) … • Outgoing username= pbxN"（p153）
> "Warning … ABC-F LINK MUST BE DELARED ON THE SAME NODE, BUT IN A DIFFERENT NETWORK"（p162，DELARED 为原文拼写）
> "Type hybvisu -f all … The two accesses must be 'UP'. … In the event of congestion, use the rsthyb command"（p165）

出处：OTCCXTE100EN p3-17, p150-165。

## I — 自述

本书一切实验的地基是 RLAB 环境（f02/f03，纯实验口径，仅作 Boundary 背景）：

- POD 五实例：OXE（192.168.1.1/1.3，mtcl）、OMS（192.168.1.13）、FlexLM 许可服务器（192.168.1.80）、Client PC10（192.168.1.10，IPDSP 31000 + MicroSIP 31010/31011/Public）、Client PC11（192.168.1.11，IPDSP 31001）
- ITSP1 模拟器两腿：SIP 网关 gateway1.itsp1.com（注册 pbxP/alcatel）+ 公网网关 public.itsp1.com；号码规则：安装号 3321PN、DDI 首外线 41000/首内线 31000；打 pilot 拨 0210X41600（X=POD 号）

POD 收尾四件事（c05）：

- 公网软话机选对 POD profile 并 Online；SIP Ext. Gateway 填 Registration ID/Outgoing username=pbxN
- DID 翻译：首外线 33210N41000 映射首内线 31000、段长 1000
- RDP 音频串联：两级远程桌面把播放与录音都重定向到本地，单屏容纳全部软话机

ABC-F 本地混合链路（c06）：内呼 pilot 的承载。硬约束：同 Node 不同 Network 声明；pilot 的 ABC Local Call Allowed 须启用（法国库默认开）；链路默认存在（版本基线两说，见 nr-04）但两条 access（B Channel）任何版本都要手工建；hybvisu -f all 验双 UP、rsthyb 重启。

## A1 — 书中案例

**POD 收尾实验**（p150-158）：

1. RLAB 面板确认五台 VM 启动；OXE 侧核对机架（Software Rack 3U、Rack 4 Virtual GD4）
2. MicroSIP-Public 选 Public POD X profile 确认 Online
3. SIP> SIP Ext. Gateway 填 Registration ID=pbxN、Outgoing username=pbxN
4. Translator> External Numbering Plan> Default DID num. translator 建 33210N41000→31000（段长 1000）
5. MicroSIP-Public 拨 0210X41600/0210X41601 打两个 pilot，Agent1 应答、挂机进 wrap-up
6. 配两级 RDP 并重定向音频，PC11 窗口最小化对齐 IPDSP

**ABC-F 实验**（p159-165）：

1. 先试内呼 31600，不通再建链路
2. System 页核 Node 号与 Network 号（同 Node 不同 Network）
3. 核对 pilot 的 ABC Local Call Allowed 已启用
4. Loop-Hybrid 核对 Multi access hybrid link=YES；建 access 1 与 access 2（B Channel）
5. mtcl 会话 hybvisu -f all 确认两条 access 均 UP；拥塞时 rsthyb

## A2 — 未来触发

使用情境：新学员开环境打不通外呼；公网软话机不在线；DID 翻译不对；内呼 pilot 不通；hybvisu 显示 DOWN；RDP 没声音；R100 前后版本链路要不要自建。

语言信号：RLAB / POD / ITSP1 / pbxN / MicroSIP / IPDSP / DID 翻译 / 33210N41000 / 0210X41600 / ABC-F / Loop-Hybrid / access / hybvisu / rsthyb / 同节点不同网络 / RDP 音频。

与相邻能力区分：矩阵对象创建 → CCD 基础矩阵能力；direct call 的链路限制 → 直接呼叫与紧急关闭卡（路由卡）；生产中继与编号计划在书外。

## E — 可执行步骤

输入契约：RLAB 账号与 POD 号已分配、五实例已启动、教材预置库完好。

1. 核实例与机架：五台 VM 在线，OXE 机架与 GD4 板位在服。完成标准：config 4 正常
2. 参数化公网软话机：选对 POD profile 并确认 Online。完成标准：可注册到 ITSP1
3. 填 SIP 网关参数：Registration ID 与 Outgoing username=pbxN。完成标准：保存成功
4. 建 DID 翻译：首外线→首内线、段长 1000。完成标准：外呼公网号能翻译到内部分机
5. 打通外呼：拨 0210X41600/0210X41601 到两个 pilot。完成标准：Agent1 应答且挂机进 wrap-up
6. 通内呼链路：核 Node/Network 与 ABC Local Call Allowed → 建/核 access → hybvisu 验双 UP。完成标准：内部分机可拨通 pilot
7. 串联 RDP 音频：两级远程桌面重定向播放与录音。完成标准：单屏操作全部软话机且声音正常

判停点：

- 外呼不通 → 按序查：软话机 profile、SIP 网关 pbxN、DID 翻译，三层各有一个错就全断
- 内呼不通 → 先查同 Node 不同 Network 与 ABC Local Call Allowed，再查 access 是否建（n03/n09）
- 链路拥塞 → rsthyb 重启 ABC-F（p165）
- 生产项目套用本章参数 → 判停：pbxN/3321PN/0210X 全是实验口径，生产走真实 ITSP 与编号计划（n19）
- p153 口令登录失败 → 全书主体口径是 Superuser2580*（nr-01）

输出契约：可外呼可内呼的实验站点（SIP/DID/链路参数记录）+ RDP 单屏操作环境。

## B — 边界

- 本章全部 IP/账号/号码/口令为 RLAB 教学专用（p9 实例表明文），生产必须整体替换（n19）
- 真实 ITSP 申请、编号计划设计、COS 规划在书外——原书假设预置库现成（批判区）
- R100/N1 版本基线两说（nr-04）：行为口径按"链路默认存在、access 必建"执行，现场以 hybvisu 实测为准
- RDP 音频串联是 RLAB 教学手法，生产座席环境无关
- SSH 可用性在不同实验章节记载不一（p76 SSH 会话 vs 收尾章"SSH is disabled"），按 RLAB 实际为准（g39）
