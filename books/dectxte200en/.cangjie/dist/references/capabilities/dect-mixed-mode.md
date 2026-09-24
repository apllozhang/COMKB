# 混合 DECT 基础设施部署（TDM IBS + IP-xBS 同站、PLI 统一适配）

## R — 原文依据

> "Warning IN CASE OF MIXED MODE, SO WITH MULTI PARI NUMBERS, THE PLI MUST BE ADAPTED."（p227）
> "Setup an IP-xBS solution on a site with an existing IBS infrastructure. The IBS PARI is 100004101x0. The new xBS PARI will be 100004101x4 (x = POD number). The PLI value will be 30. With that all DECT users will be able to connect on all DECT base stations (xBS & TDM)."（p244）
> "Radio base type Mixed ... RPN 0 xBS PARI: 100004101x4 ... RPN 0 RPN 1 IBS PARI: 100004101x0 ... PLI = 30"（p244）
> "In multi PARI or in mixed mode, the PLI must be adapted"（p245, p265）

出处：DECTXTE200EN p227, p242-248, p245, p265。

## I — 自述

混合模式（Mixed）= 同一台 OXE 同时跑 TDM（IBS）与 IP（xBS）基站，是存量 TDM 演进到全 IP 的主路径。三条要点：

1. **多 PARI 是结构性的**：每类硬件必须各一个 PARI（IBS 100004101x0、xBS 100004101x4 形态），Radio base type=Mixed。
2. **PLI 必须适配**（p227 大写 WARNING）：单 PARI 默认 PLI=31；多 PARI 时手机按全位比对无法同时兼容两个 PARI。降位规则——两 PARI 仅末位不同取 30，末 2 位不同取 29；前提是新 PARI 与旧 PARI 高位相同。
3. **切换要靠外部同步**：混合站的 xBS 与 IBS 属两个 PARI、两棵同步树，要获得跨类基站通话中切换，需配外部同步链路 + Flag External Handoff（详见同步拓扑能力）；建不了外部同步时两区域间距必须 >1km（p196）。

已注册手机的两条兼容路径：

- PLI 缩位后老 PARK 自动满足逻辑 AND（仅对满足条件的 PARI 对成立）
- 用 dectinston -update 推新 PARI/PLI（自动重注册能力）

## A1 — 书中案例

**混合部署实验**（p242-248）：

1. 前置：IBS 已按 c09 入网（PARI=100004101x0，RPN 0/1）；备份的默认数据库已恢复
2. 全局参数：Radio base type=Mixed、Station Base Type=DECT Europe、PLI for CTM=30（由 31 降为 30）、AC System=1111、Security level=Authentication
3. xBS System：Number of PARI=1、WBM=YES + 口令
4. xBS Pari：PARI Number=1、PARI Value=100004101x4、Area type=1 area of 256 xBS
5. Site 0=BREST；xBS base station 录 GF-01、Site 0、PARI Number=1
6. DHCP（实验池）+ 开注册 → 接通两台 xBS
7. 核验：dectview xbs 两站 OK、PARI-Area-RPN=1-0-0 / 1-0-1

## A2 — 未来触发

使用情境：IBS 存量站点加 xBS；混合后部分手机漫游不到新基站；Mixed 模式 PLI 取值；老手机要不要动；混合站要切换。

语言信号：混合 / mixed / 混合模式 / TDM / xBS / IBS 同站 / 多 PARI / PLI 适配 / PLI=30 / 降位 / 存量演进 / 迁移。

与相邻能力区分：外部同步链路与外部 handover 配置见同步拓扑能力；手机批量推新标识见自动重注册能力；IBS 侧建站施工见 IBS 部署能力（路由）；PARI/PLI 语义本身见标识号码能力。

## E — 可执行步骤

输入契约：在网 IBS 的 PARI/RPN、新增 xBS 数量与 MAC@、两站物理间距、可否建外部同步。无在网 IBS → 本卡退化为纯 IP-xBS 部署。

1. 规划 PARI 对：新 xBS PARI 与 IBS PARI 高位对齐、仅低位区分（如 x0 与 x4）。完成标准：两 PARI 差异位数明确
2. 定 PLI：按差异位数取 30 或 29（仅末 1 位不同 → 30）。完成标准：PLI 能让两 PARI 对手机等效
3. 全局切 Mixed：PWT/DECT System 改 Radio base type=Mixed、写 PLI、AC、Security level。完成标准：Mixed 生效
4. 建 xBS 域：xBS Pari（PARI Number=1）+ Site + 基站参数 + DHCP。完成标准：xBS 入库（参照 IP-xBS 部署步骤 2-5）
5. 配外部同步：xBS Site / External Synchronization 指定同步源 IBS PARI/RPN + Flag External Handoff=yes。完成标准：dectview xbs 表尾见 External sync source
6. 核验漫游：dectview xbs 两类基站在网；手机跨类基站可锁定通话。完成标准：全部 DECT 用户可接入两类基站

判停点：

- 新 PARI 与旧 PARI 高位完全不同 → PLI 降位无效，转自动重注册能力的 -forceUpdate 路线（先推手机、后改系统）
- 建不了外部同步且间距 <1km → 停，方案不可行：换拓扑（全 xBS）或做物理隔离，不要带病开局
- 混合后个别老手机漫游失败 → 核对机型固件版本（p252 版本表），必要时先升固件再 -update

输出契约：混合站配置摘要（双 PARI/PLI/同步链路）+ 漫游互通验证记录。

## B — 边界

- 实验 PLI=30 依赖实验 PARI 对仅末位不同；客户 PARI 对差异更多位时按 PLI 规则另算，不要照抄 30
- IBS 的 handover 要求全部基站挂同一 media gateway（p224）——混合站内 IBS 侧切换域受此约束
- IBS 无加密（p37）：混合站安全级别上限=Authentication，要加密只能全 xBS
- p227 WARNING 面向全部已注册手机；PLI 变更的回退路径书内未给（待确认）
- 混合实验的两站间距 15 米为实验口径，生产按勘测定
