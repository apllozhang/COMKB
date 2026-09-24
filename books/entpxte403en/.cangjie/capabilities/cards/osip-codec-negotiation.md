# 编解码协商与验证（决策链、优先级、compvisu）

## R — 原文依据

> "High bandwidth : OPUS SWB > OPUS WB > G.722 > G.711 > OPUS NB > G.729 • Low bandwidth : OPUS NB > G.729"（p281）
> "If the parameter is set to false, the other G711 law codec is rejected by the OXE A SIP 488 'not acceptable here' message is returned"（p273）
> "User SIP profile contains a list of available codecs: up to 5 coders • G729 ... It's mandatory to choose this codec among the 5 preferred codecs ... At least one G711 codec is mandatory"（p278）

出处：ENTPXTE403EN p271-286。

## I — 自述

编解码协商是五层决策链，逐层放行后按优先级选最高质量：

| 层 | 对象 | 口径 |
|---|---|---|
| 1 | 系统参数 | 法线随国家；Accept Mu and A law in SIP 关则他法线来话回 488；G722/OPUS 支持域三档是总闸（Not available 时网关开了也白开） |
| 2 | IP 域带宽 | 域内建议高带宽、跨域建议低带宽；高=OPUS SWB/WB、G722、G711、OPUS NB、G729；低=仅 OPUS NB 与 G729 |
| 3 | DM profile 与用户 SIP profile | 用户 SIP profile 最多 5 个编解码，G729 与至少一份 G711 必选 |
| 4 | 终端能力 | Enterprise/ALES/IPDSP 等支持 OPUS 全档+G722；GD3/GD4/INTIP3、DECT 等不支持；OXE-MS 是 OPUS/G722 媒体服务的必要资源 |
| 5 | 链路/外部网关 | Direct Link 两侧带宽一致；外部网关 OPUS/G722 开必须连带 G711（对接 GD/OMS 必须 G711） |

- 验证命令：compvisu（mtcl）eqt all 看实际算法；NOCOMP=无转码直通
- DTMF 与放音：18x 无 SDP 时放音本地化；业务激活用 183+SDP 开媒体；DTMF 三法（RFC4733/INFO/带内）在 DM profile 定

## A1 — 书中案例

**compvisu 四场景**（p283-286，How-To）：

1. SEPLOS 内呼（ALES 31030 呼 IPDSP 31000）：compvisu eqt all 读出 LIOE_IP-G722(83) 与 NOCOMP-G722(80)，实际 G722 直通。
2. 经私有中继（31060 呼 31000）：中继侧 LIOE_IP_NOT-G722(84)，确认 G722 与 ABC-F 中继参与。
3. SEPLOS 呼公网（ITSP2）：双侧 NOCOMP-OPUS_WB(c0)，确认 OPUS_WB（外部网关 OPUS 已开）。
4. SIP Device 呼公网：JONCT 对 JONCT，NOCOMP-G722 双侧，公私两条 SIP 中继同链。

## A2 — 未来触发

使用情境：音质差/单向语音投诉；对方只收 G711；跨法线对接失败回 488；全 OPUS 网络设计前清点媒体资源。

语言信号：编解码 / codec / 协商 / OPUS / G.722 / G.711 / G.729 / 488 / 法线 / A 律 / μ 律 / 带宽 / IP 域 / compvisu / 转码 / OXE-MS / 优先级。

与相邻能力区分：抓信令看 SDP 找 SIP 跟踪排障；外部网关编解码开关配置找 SBC 运营商接入；终端选型能力矩阵找用户形态选型。

## E — 可执行步骤

输入契约：呼叫场景（内呼/跨域/外线）、两侧终端与网关型号、系统版本。投诉无复现路径 → 判停先建呼叫。

1. 定场景：确认呼叫两端与途经对象（域/中继/网关）。完成标准：路径图画出
2. 查总闸：系统 Compression Parameters 的 G722/OPUS 支持域。完成标准：总闸状态明确
3. 逐层核对：IP 域带宽、用户 SIP profile 五席、终端能力、链路/网关开关（OPUS/G722 连带 G711）。完成标准：五层全勾
4. compvisu 定格：通话中执行 compvisu eqt all，读实际算法与是否转码。完成标准：算法有读数

判停点：

- 系统级 Not available → 停，先开总闸再谈下层（n29）
- 法线不匹配且 Accept 参数为 False → 停，跨法线场景开 True，否则继续回 488（n30）
- 全 OPUS 设计但站点有 GD/DECT 等老媒体设备 → 停，先按矩阵清点，OXE-MS 容量另算（n46）

输出契约：实际编解码结论（compvisu 读数）+ 五层配置核对表 + 整改项清单。

## B — 边界

- G723 不支持（p277）；8058s/68s/78s（NOE）OPUS 仅 SWB 档等代际特例按 p276 原文矩阵
- compvisu 读数为实验场景口径，生产数值随配置而变
- 第三方 SIP 终端可不支持 OPUS/G722，应从设备清单禁用而非硬协商（p278）
- 带宽/话务建模方法论书外，本卡只管协商链与验证
