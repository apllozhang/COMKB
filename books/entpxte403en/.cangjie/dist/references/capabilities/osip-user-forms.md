# SIP 用户形态选型与容量核算（SEPLOS vs SIP Device、软件锁、终端家族）

## R — 原文依据

> "SEPLOS mode (SIP End Point Level of Services) • The SIP sets operating in SEPLOS mode are considered by the phone application as internal sets ... Can use prefixes/suffixes to activate PCX phone services"（p66-67）
> "SIP device • SIP sets are considered by the phone application as part of a remote subnetwork ... Cannot use prefixes/suffixes ... Cannot be supervised by CSTA ... Cannot be a call center agent"（p66-67, p78）
> "3 software locks for the SIP users • 177: defines the number of SIP users (device and extension) • 345: defines only the number of SIP extensions • 430: defines the number of SIP softphones (ALE-S)"（p67）
> "IP Max = 15000 ... SIP Max = 15000 ... Maximum 15000 Users (Single device, or Main of multi devices) Maximum 20000 devices"（p68）

出处：ENTPXTE403EN p64-106。

## I — 自述

形态选错 = 服务等级全错。两形态结构化对比：

| 维度 | SEPLOS（SIP Extension） | SIP Device |
|---|---|---|
| 电话应用视角 | 内部话机 | 远端子网的一部分 |
| 前缀/后缀激活业务 | 支持 | 不支持 |
| 多线/寻线组/代接组/酒店 | 支持（按机型有降级） | 全不支持 |
| CSTA 监督与 CTI | 支持 | 不支持 |
| 呼叫中心坐席 | 可以（依终端） | 不能 |
| 典型对象 | ALE 话机、ALES 软终端 | 会议话机、门禁、视频设备 |
| 开通前提 | 子型 + DM profile | 私网 + 私有 SIP 中继组 + 本地网关 |

- 软件锁三把：177 计 SIP 用户总数（Device+Extension 合计）、345 只计 SEPLOS、430 只计 ALE-S 软终端；具体可配数取决于站点许可
- 容量六维（p68）：IP 用户 15000（含 IPDSP 与虚拟用户）、TDM 5000、模拟 5000、S0 1000、远程分机 9000、SIP 15000；总量最多 15000 用户（单设备或多终端主设备）、20000 设备
- 终端家族谱系（p70/p97-106）：Enterprise（ALE-300/400/500，双栈）、Essential（ALE-30、8008/8008G 酒店特例）、Basic（ALE-2/ALE-3）、8088（Huddle Room）、ALES 软终端（Windows/Android/iOS）
- SEPLOS 附加行为：SIP MESSAGE 推送 CS 信息（终端不支持回 405）、原生加密（SIP TLS/SRTP）、18x 无 SDP 省压缩资源

## A1 — 书中案例

**SIP Device 建户**（p89，c03 一环）：

1. Users → Create：DN=31060、名 Conference Room、Shelf/Board/Equipment=255。
2. Set Type 选 +SIP device，SIP Passwd 设 12345（实验口径）。
3. Warning：SIP device 须在 CS 内部防火墙登记为信任主机（netadmin -m/Security）。
4. 验证：sipregister 应见 31060 注册；sipdict -l 中 31060 显示 type=2（Device）。

**终端选型对照**（p97-106）：

1. 酒店客房 → 8008/8008G（Business+酒店模式，无话务员/坐席）。
2. 标准工位 → ALE-300/400/500（双栈、120 可编程键、全量监督/寻线组）。
3. 低成本 → ALE-2/ALE-3（8/12 键、监督仅监督员角色、寻线组降级）。
4. 移动办公 → ALES（OXE DM 独占管理，一号多机互斥）。

## A2 — 未来触发

使用情境：客户拿会议话机/门禁问能不能进代接组；报价前核软件锁够不够；选话机档位；SIP 用户数快到许可上限。

语言信号：SEPLOS / SIP Extension / SIP device / 软件锁 / 177 / 345 / 430 / 容量 / 15000 / 20000 / 会议话机 / 门禁 / doorcam / ALE-2 / ALE-3 / ALE-30 / ALE-300 / 8008 / ALES / 选型。

与相邻能力区分：定了形态去施工找 SIP Device 开通、话机开通、ALES 开通；按机型查按键/监督等业务细节找 SIP 业务特性；DM/许可是另一头找 SIP 设备管理选型。

## E — 可执行步骤

输入契约：终端清单（型号/数量/位置）、业务需求清单（要不要 CTI/坐席/寻线组/酒店）、站点许可文件。需求与形态冲突 → 判停先对齐。

1. 列业务需求：逐项标注前缀/后缀业务、CTI 监督、坐席、寻线组、酒店。完成标准：需求表成文
2. 定形态：要 PCX 话务级业务 → SEPLOS；独立设备（会议/门禁/视频）→ SIP Device。完成标准：每台终端有形态
3. 核容量：按 177/345/430 三把锁与 p68 六维上限核算余量。完成标准：容量表过账
4. 选型号：对照家族谱系与功能矩阵（p99/p104 双列以原文为准，售前以 Features List 终审）。完成标准：选型清单签字
5. 交代前提：SIP Device 提前规划私网号与中继组；SEPLOS 规划子型与 DM profile。完成标准：下游开工条件齐

判停点：

- 客户坚持 SIP Device 要 CTI/坐席/入组 → 停，形态上限不可绕，改 SEPLOS 或换终端（n02）
- SIP 用户数将超许可 → 停，走扩许可流程，不硬开通
- 客户要 SIP 侧话务员/话务员助理/MLA → 停，SIP 模式全系列缺席（8008 仅酒店例外），回 NOE 或改方案（n26）

输出契约：终端形态与型号清单 + 软件锁/容量核算表 + 各终端的开通前提条件。

## B — 边界

- p68 图中一处 "Maximum 5000" 归属在文本层不可辨（nr-01），容量口径以六维上限与 15000/20000 为准，精确归属查 Features List
- p99/p104 功能矩阵双列有文本层歧义（nr-02），引用格子以原文双列为准；ALE-2 无视频
- SIP Device 五不带是设计而非缺陷（n02）；开通结构性前提三件套缺一不可（n03）
- p72"依赖终端"清单与矩阵需合读：ALE-2/3 寻线组是降级支持而非不支持（nr-08）
- 家族矩阵为 Ed12 时点口径，版本演进以 OXE Features List 为准
