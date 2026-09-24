# DECT 产品线选型与拓扑决策（IBS / IP-xBS / SIP-DECT 三线 + 六种拓扑）

## R — 原文依据

> "TDM offer common hardware IBS: Intelligent Base station Connected to an UA board ... Low-cost DECT mobility for users connected to small PCX configurations 8328 SIP-DECT (*)"（p7）
> "(*) Since the SIP-DECT configuration in OXE is based on SIP users, the following explanations (PARI, PLI, etc.) do not necessarily apply to this type of infrastructure."（p7）
> "When it is not possible to have an external synchronization, the distance between the area must be > 1km."（p196）
> "Encryption is not available for IBS Base Stations on Common Hardware architecture"（p37）

出处：DECTXTE200EN p7, p27, p37, p58-60, p191-198, p272。

## I — 自述

选型先于配置：OXE 的 DECT 是三条产品线并列，选错线返工代价最高。

1. **8379 IBS（TDM 线）**：基站接 UA 板卡（UAI/MIX），全网仅 1 个 PARI、256 台；1/2 条 UA 链路对应 3/6 路通话；Common Hardware 上**不支持加密**，handover 要求全部基站挂同一 media gateway。
2. **8378 IP-xBS（全 IP 主线）**：UA/UDP 信令 + RTP 媒体直达，空中互同步，每站 11 通话+11 IP 中继；每节点 8 个 PARI、2032 台；支持加密（native 需 IP-xBS R200）；OXE R12.2 起、仅 IPv4。
3. **8328 SIP-DECT（低成本线）**：基站以 SIP 终端语义注册到 OXE，PARI/PLI 体系不适用；仅 8214 手机、仅欧洲频段、每站 20 手机（G.711 10 路/G.729 4 路）；区与区之间无 handover/roaming（双小区除外）；WAN 断则全断且无 SIP 备份。

六种支持拓扑按四格图例（Handover / External Handover / External inter node handover / Roaming）判定能力：

| 拓扑 | 关键约束 |
|---|---|
| IP-xBS 单线（1 节点） | 8 PARI max、2032 台，全部能力 |
| IP-xBS + 分支办公（多 Site WAN） | 全部能力，Site 切换边界 |
| 混合 xBS/IBS 同站 | +256 IBS，需外部同步链路 |
| 混合无重叠（无法外部同步） | 两区域间距必须 >1km |
| 混合 + 分支办公 | 按分支拆 Site |
| OXE 网络混合 xBS/TDM（多节点） | 节点间不同步，仅 roaming + 跨节点外部切换 |

## A1 — 书中案例

**选型读法**（p193-198, p272）：

1. 先问是否多节点：多节点网络只有 roaming + 跨节点外部 handover，节点间无同步
2. 再看 IBS 混入方式：可建外部同步链路 → 全能力；建不了 → 区域间距 >1km
3. 小区域低话务（如门店）→ 8328 单站 20 手机够用，但要接受无区间切换与 WAN 断全断
4. 加密合规项目（医疗/政务）→ IBS 一票否决，锁定 IP-xBS（R200 起原生加密）

## A2 — 未来触发

使用情境：新站点上 DECT 选产品线；客户要加密；分支办公组网；TDM 存量演进；小站点低成本方案；评估 8328 够不够用。

语言信号：IBS / IP-xBS / 8378 / 8379 / 8328 / SIP-DECT / 选型 / 拓扑 / 分支办公 / branch office / 混合 / mixed / handover / roaming / 加密 / encryption / 频段 / 欧洲频段。

与相邻能力区分：定了 IP-xBS 后的施工见 IP-xBS 部署能力；8328 具体施工见 SIP-DECT 能力（路由卡）；IBS 施工见 IBS 部署能力（路由卡）。

## E — 可执行步骤

输入契约：站点数量与地理分布、存量硬件（有无 IBS/UA 板卡）、用户数与话务密度、加密合规要求、终端机型、国家/频段。

1. 判加密合规：要求加密 → 排除 IBS，候选剩 IP-xBS/8328（8328 加密能力书内未给，待确认）。完成标准：产品线池缩小
2. 判规模：>20 手机或需区间漫游 → 排除 8328 单站；>254 台 xBS → 规划第二 PARI 与外部同步。完成标准：规模可行性成立
3. 判多节点：OXE 网络 Campus/多节点 → 确认接受"节点间仅 roaming+跨节点外部切换"。完成标准：切换预期对齐
4. 判混合：既有 IBS 又加 xBS → 确认可建外部同步链路，否则两区间距 >1km。完成标准：混合约束落位
5. 判频段与终端：非欧洲频段排除 8328；终端诉求（A-GAP 多线/监督键）排除 8214。完成标准：产品线确定

判停点：

- 客户要"低成本+大覆盖+区间切换" → 8328 做不到，上 IP-xBS，不要硬凑
- 客户要加密但预算只够 IBS → 停，升级商务决策（p37 硬边界）
- 无线勘测数据缺失 → 布点结论先挂起，勘测属覆盖勘测能力，方法论在 8AL90874USAA（书外）

输出契约：产品线结论 + 拓扑判定（四格能力对照）+ 约束清单（频段/间距/版本）。

## B — 边界

- 话务密度上限 10000 E/Km² 仅一句话（p5），书内无 Erlang 话务模型——容量测算需另建模型（书外）
- 8328 双小区时两站合计容量书内未单列，按单站×2 估算属推断口径
- IPv6 仅"硬件就绪暂不适用"（p59），纯 IPv6 网络项目 IP-xBS 不可用
- IP-xBS 天线/附件订货号（p66-69）是选型目录数据，不构成本卡决策逻辑
- 频段以部署国法规为准（p5 与 p8 双表口径见 needs-review nr-04）
