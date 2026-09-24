# GLOSSARY — OmniTouch Contact Center Standard 入门术语表

> 阶段 3 产出（源：candidates/glossary.md，46 条，六类：concept 17 / role 7 / subscription 1 / product 9 / protocol 8 / resource 4；此处收录门户版精选）。
> 口径：定义只采信本书正文；CCD/ABC-F/CSTA/DID/OMS/PLTR 等缩写书中未给全称，如实标注，不采信外部知识。

# OTCC Standard Starter (OTCCXTE100EN Ed09) — 关键术语词典

> 文档整理流水线术语提取器产出。取材方法：全量扫描 source_fulltext.txt（649 页全部页码标记），所有页码均回原文核验。
> 用途：下游能力卡的共享中英对照词典。

## 一、核心概念域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| CCD | 呼叫分配软件与对象体系（全称书中未展开） | OXE 内置的呼叫分配引擎：CCD matrix/objects/users，OTCC Standard 的核心 | p21-29, p63 |
| Pilot | 引导号/被叫部门号 | 来话首先到达的虚拟号，三态（Open/General Forwarding/Blocked），Blocked 是下游无资源的自动态 | p26, p43-50 |
| Waiting Queue | 等待队列 | 呼叫停车常：三类型 Normal/Int-Overflow/Redirection，FIFO，≤30 pilot 共享、服务 ≤50 PG | p27-28, p40 |
| Processing Group | 处理组（资源） | 五类型：Agent/Forward/Voice Guide/Rerouting/IVR；Voice Guide PG 只接 Redirection 队列 | p29, p40 |
| Routing rule | 路由规则 | 连 pilot 与队列：每 pilot ≤30 条（全局 1200），优先级 0-9，同优先级看 EWT | p43-50, p103 |
| Distribution rule | 分配规则 | 连队列与 PG：全局 ≤10 条、每队列 ≤50 方向；默认停用须 OXE 激活，方向默认关闭 | p54, p113, p117 |
| Parking level | 停车级 | normal 队列内 6 个播报层级：指南号/IAA 或队内 IVR 地址/EWT 表；cut auth 可打断 | p45, p50, p351 |
| EWT | 预期等待时间（Expected Waiting Time） | =平均等待×(队内呼叫数+1)，按队列 TSP 滚动计算；路由平局、饱和判据、播报分档三重角色 | p44, p47-49, p350 |
| TSP / MSP / SOP | 话务/监控/班长观察三周期 | TSP 每队列定义算 EWT；MSP 5-60 分；SOP 默认 15 分刷 smiley（实验均取 15 分档） | p47, p80, p168 |
| Statistic Pilot | 统计型 pilot | 对外业务号先问候再转唯一路由 pilot；≤3000 个；不可兼 direct call pilot | p543-551 |
| CCD Direct Call | 直接呼叫 | pilot direct call（如 "31603"）+私人号：把打座席号的外线来话纳入 CCD 待遇与统计 | p449-458 |
| Emergency Closure | 紧急关闭 | 一键关闭 pilot 列表（≤50 列×600 pilot）；转移须配地址；统计计入通用转发态来话 | p527-529 |
| Agent Welcome Guide | 座席欢迎指南（"538" 机制） | 座席摘机播个性化问候；消息池 "4500"-"5999"、每座席 ≤5 条；direct call 不播 | p566-570 |
| Withdrawal / Wrap-up / Pause | 退出/话后处理/两通间隔 | 退出 9 类型供统计；wrap-up 自动挂 pilot 手动挂 PG（1-3276 秒）；pause 可接私人电话 | p275-280, p307 |
| Transaction / Business code | 事务码/业务码 | 事务码 1-15 位只存通话记录；业务码 1-3 位进 Excel 统计（上限 1000 个） | p293, p343-344, p478 |
| Calendar（pilot/distribution） | 双日历 | pilot 日历 "10" 切换/日（规则 ID+Nor/Fwd）、分配日历 "20" 切换/日；特殊日 ≤50 覆盖周历 | p607-616 |
| ABC-F hybrid link | 本地混合链路（全称书中未展开） | 内呼 pilot 承载：同 Node 不同 Network、≥2 条 access（B Channel）、hybvisu 验 UP | p159-165 |

## 二、角色域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Agent | 座席 | 登录 ACD 话机承接 CCD 分发：固定（免认证）/移动（需认证）/自指派（自选组）三形态 | p31-33, p271-273 |
| Supervisor | 班长 | 监督多组可兼座席：永久监控/旁听/强插/通用转发与 PG 关闭键；恒自指派无优选组 | p31, p274, p286-292 |
| CCS Administrator | CCS 管理员账号 | CCS 应用内全权账号（紧急关闭选 pilot 必需）；与 OXE 侧班长是两个层面 | p84, p542 |
| Rainbow CCD agent | Rainbow 座席 | 仅座席无班长；三不限制（不入 multiset/不关联 Rainbow 用户/DECT 不支持）；免 VPN/SBC | p34-37 |
| Public user / Local SIP user | 公网/本地模拟呼叫者 | 实验角色：Public 拨 0210X…、Local 拨 00210X…（全部实验口径） | p10, p153, p400 |
| mtcl / swinst / root | OXE 系统账号 | mtcl 主管理账号（实验口令 Superuser2580*；p153 一处写 mtcl/mtcl，见 nr-01） | p9, p65, p76 |

## 三、许可与可选件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OTCC Standard 可选件 | CCS/CCA/ACR/Soft Panel | OTCC Standard 内置于 OXE，四个可选件；ACR=Advanced Call Routing（p544 展开） | p21, p544 |
| CcsLight / Monosite / Multisite token | CCS 许可 token | ccs.ini 的 CcsLight=1 需 CCSLight token；=0 按 MultiSite 参数取 Monosite/Multisite | p86, p92 |
| FlexLM | 许可服务器 | OXE 侧许可承载（实验 192.168.1.80） | p9 |

## 四、产品与组件域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| OmniPCX Enterprise (OXE) | ALE 企业 PBX（呼叫服务器） | OTCC Standard 宿主；管理入口 Web Admin（https://192.168.1.3）+ mtcl 控制台/SSH | p7, p21-23 |
| CCS / CCsupervision | 班长/管理台 | Windows 应用：规则/座席/实时/统计/紧急关闭；不能建 CCD 对象（只能建班长与分配规则） | p78-88, p79 |
| ccs.ini | CCS 配置文件 | 每次启动读取（programData/Alcatel/CCsupervisor）；id_terminal 0..127 唯一；ShowStatisticWithData 须手改 | p85-87, p512 |
| Navigator | 实时监控视图 | 3 秒快照（1-50 可调）：对象状态/话务指示/告警；页签与计数器可定制 | p402-414 |
| OMS / GD3 / GA3 / GPA2 | 语音指南承载硬件 | OMS 免板卡；GD3/GA3 通用板卡；GPA2 欢迎指南 RAM 板（实验板位 4-0） | p9, p197, p568 |
| IPDSP / MicroSIP | 实验软话机两类 | IPDSP=ALE 座席软终端（CC/Perso/Menu 页签）；MicroSIP=第三方轻量话机（内呼+公呼） | p10-11 |
| ITSP1 / RLAB | SIP 运营商模拟器/远程实验室 | gateway1.itsp1.com + public.itsp1.com（注册 pbxP/alcatel）；POD 池教学基础设施 | p5, p14-17 |

## 五、协议与技术域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| SIP trunk / SIP Ext. Gateway | SIP 中继/外部网关 | OXE 经外部网关注册模拟运营商（Registration ID=pbxN）；公共中继组承载外呼来话 | p15-16, p153 |
| DID (translation) | 外线直拨翻译（全称书中未展开） | 公网号段映射内部分机段（实验 33210N41000→31000、段长 1000） | p16, p154 |
| CSTA | 呼叫控制接口（全称书中未展开） | Rainbow-OXE 呼控接口；中继组 CSTA-Monitored 开启后 CCS 才显示实时值 | p34-35, p414 |
| G711 / ADPCM32 / A-Law .wav | 语音编码与文件格式 | G711 64kbps（crystal）/ADPCM32 32kbps（common）；.wav 标准 A-Law/8000Hz/64kbps/mono | p197, p241 |
| SFTP | 安全文件传输 | CCS 向 OXE 传语音文件的通道，OXE N3 起强制 | p245 |
| WebRTC / REX | 网页实时通信/远端分机池 | Rainbow computer 登录时 REX 改址到 WebRTC 网关 SIP 中继；远程免 VPN/SBC | p34-37 |

## 六、资源域

| 英文术语 | 中文译名 | 书中定义/用法（一句） | 出处页码 |
|---|---|---|---|
| Voice guide（静态/动态） | 语音指南 | 静态打包存 Flash（vgadpcm.EN0）；动态可录存 RAM；3 位指南号放矩阵、4 位消息号录制 | p196-201, p214 |
| 预置指南资源 | "518"/"538"/"3226"-"4217"/备份音 "56"/指南 "70"/"75" | 系统预置不可自造同号：位次指南/欢迎机制/位次消息段/无录音备份音/默认演示/直连阻塞 | p379, p389, p574 |
| 统计文件（obj/tr/ind/te/tc → dy/hr/ev） | OXE 统计文件流水线 | 午夜生成 5 临时文件（/usr4/afe 存 24h）合并 dy/hr（存 5 周）/ev（存 12 月）（/DHS3dyn/afe） | p478-481 |
| ACD prefix（"12"/"401"/"580"/"91"/"92"） | 译码器前缀资源 | 12=ACD 功能（+1 退出/+2 wrap-up/+3 呼班长/+5 登出/+6 登入）；401 录音；580 试听（法国库实验值） | p66, p216-217, p457 |
