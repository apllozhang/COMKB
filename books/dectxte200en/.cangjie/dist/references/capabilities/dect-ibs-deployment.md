# 8379 IBS 基础设施部署（UA 板卡/布线/建站/维护命令）

## R — 原文依据

> "1 UA link corresponds at 3 B channels available for voice communications • 2 UA link corresponds at 6 B channels ... Master link connected on an even port, slave link connected on the next odd port"（p219）
> "Cable SYT 0.5 mm Max length : 800m ... Cable LY278 0.6 mm Max length : 1200m"（p220）
> "MIX4/4/8 → 2"
>
> "UAI8, MIX4/8/4 → 4"
>
> "UAI16-1 → 8"（p219 板卡密度表）
> "Encryption is not available for IBS Base Stations on Common Hardware architecture"（p37）

出处：DECTXTE200EN p218-234, p37。

## I — 自述

IBS 是 TDM 基站线，接 UA 板卡（UAI/MIX），与 IP-xBS 是两代架构：

1. **容量**：1 条 UA 链路=3 个 B 信道（3 路通话），2 条=6 路；全网仅 1 个 PARI、最多 256 台；板卡密度 MIX4/4/8=2 站、UAI8 与 MIX4/8/4=4 站、UAI16-1=8 站。
2. **接线**：双链路时主链路接偶数端口、从链路接下一奇数端口（选 2 条时系统自动预留下一端口）；线缆 SYT 0.5mm 最长 800m、LY278 0.6mm 最长 1200m；建站时 Line delay 按实际距离三档选（Short 0-400M / Medium 400-800M / Long 800-1200M）；IBS generation 选 1G/2G。
3. **建站路径**：全局参数（Radio base type=IBS、PLI、AC、Security level——IBS 不能选 Encryption）；IBS System 配 PARI Value/Area type；Shelf/<网关> 指派 PARI；再在 Shelf/<mg>/Board/<UA 板>/IBS 建站。
4. **架构边界**：handover 要求全部基站挂同一 media gateway（跨网关无切换）；同步靠 PBX 时钟；不支持加密。

维护命令：dectview ibs（状态行含 INSERV/信道数/2G 1G/AUTHE）、listerm <mg> <cpl>（UA 终端）、listibs p <mg> <cpl> 0 <equip>（站详情）、outserv/inserv（复位）。

## A1 — 书中案例

**IBS 部署实验**（p226-234）：

1. 恢复默认数据库（用 POD 配置阶段的备份）；全局参数：Radio base type=IBS、PLI=31、AC System=1111、Security level=Authentication
2. IBS System：PARI Value=100004101x0（x=POD 号，实验口径）、Area type 按漫游优化
3. PARI 指派：Shelf / <目标 media gateway> → PARI Number=选 IBS PARI
4. 建站：Board/<UA 板>/IBS → Create → Equipment address（双链路用偶数口）、Location name、Line delay 三档、UA links=1 或 2、generation=1G/2G
5. 核验：dectview ibs 显示 "INSERV just 3 channe DECT V 2G 8379 ... AUTHE NORMAL"
6. 复位演示：outserv p 2 1 0 34（按 Y 确认），再 inserv p 2 1 0 34（按 Y 确认）

## A2 — 未来触发

使用情境：TDM 存量站点扩 DECT；UA 板卡怎么选；IBS 建站参数；布线距离够不够；IBS 状态判读；老网要不要留 IBS。

语言信号：IBS / 8379 / UA 板卡 / UAI / MIX / B 信道 / 偶数端口 / Line delay / SYT / LY278 / 800m / 1200m / 1G / 2G / 256 台 / dectview ibs / listibs。

与相邻能力区分：IBS+xBS 混合与 PLI 适配见混合部署能力；IBS 的手机注册见手机注册能力（同一套流程）；跨网关无切换的替代方案见产品选型能力。

## E — 可执行步骤

输入契约：UA 板卡型号与在位情况、基站数量与布线距离、是否与 xBS 混用。板卡不在位 → 先回 OXE 硬件配置（书外，指针 8AL91047ENAD）。

1. 全局参数：Radio base type=IBS（或 Mixed）、PLI、AC、Security level（上限 Authentication）。完成标准：全局就位
2. 配 PARI：IBS System 写 PARI Value 与 Area type。完成标准：全网单 PARI 就位
3. 指派网关：Shelf/<mg> 绑定 IBS PARI。完成标准：PARI-网关映射成立
4. 建站：按端口规则（主偶从奇）、Line delay 三档、UA links 数逐站 Create。完成标准：站表在库
5. 核验：dectview ibs 看 INSERV/AUTHE；listerm 看 UA 终端；listibs 看站详情。完成标准：状态行正常
6. 交付检查：布线距离复核（800m/1200m 口径）、同网关切换域确认。完成标准：切换域边界写进交付文档

判停点：

- 客户要加密 → IBS 做不到（p37 硬边界），转产品选型能力评估 IP-xBS
- 基站分布跨多个 media gateway → 无跨网关 handover（p224），要么归并网关、要么接受跨域仅 roaming、要么演进 xBS
- 布线超 800m/1200m 口径 → 停，超规范的线缆方案书内不支持
- 双链路建站后端口冲突 → 系统已自动预留下一奇数端口，检查端口规划不要手工占用

输出契约：IBS 站表（端口/链路数/Line delay/代际）+ 状态核验记录。

## B — 边界

- IBS 与 xBS 的 handover 域规则不同：IBS 按网关、xBS 按 Site/Data Sync Primary——混合站两类规则并存
- IBS 的 ATEX 防爆变体（3BN77020EA，p222）仅订货号信息，部署细节书内未展开
- dectview ibs 输出逐字段语义（odd/V/53.02 等）书内未全部注解，深度判读在 8AL91443ENAA
- 实验值（PARI=100004101x0、AC=1111、outserv 端口串）为实验口径
