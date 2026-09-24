# DECT 标识号码体系与 multi-PARI 适配（PARI/RPN/RFPI/PARK/PLI/IPUI）

## R — 原文依据

> "PARI: Primary Access Right Identifier, identification of the PABX, made of 31 bits or 8 hexa decimal digits"（p14）
> "PARK: Portable Access Right Key ... corresponds to the PLI + the PARI number of this system (coded in 13 digits) ... Example: PLI=31 and PARI=10000400100 → PARK=3110000400100"（p17）
> "The PLI determines how many bits, of the PARI received from the base station, must be compared to the local PARK • If the PLI is decreased, the handset is compatible with more PARI"（p18）
> "A different PARI is mandatory per type of DECT hardware deployed on an OXE • IBS • xBS"（p15）

出处：DECTXTE200EN p14-22, p82。

## I — 自述

OXE 的 DECT 一切配置字段都落在六个标识号码上，关系如下：

1. **系统侧**：PARI（31 位，可写 8 个十六进制位或 11 个八进制位）标识一台 OXE 上的某类 DECT 硬件；RPN（2 个十六进制位）是系统分配给每台基站的空中标识，PARI+RPN=RFPI 由基站广播。
2. **手机侧**：PARK（13 位 = PLI 2 位十进制 + PARI 11 位八进制）在注册时写入手机；IPUI（14 个八进制位）固化在手机 EPROM，是系统认机的依据。
3. **锁定算法**：手机把空中收到的 PARI 与本地 PARK 做逻辑 AND，参与比较的位数由 PLI 决定——PLI=31 全位比较（单 PARI），降到 29 则末 2 位不参与比较。
4. **multi-PARI 适配**：每类硬件（IBS/xBS）必须各有一个 PARI；混合部署时把 PLI 从 31 降位（如 30/29），让仅末位不同的两个 PARI 对同一手机等效——这是 p227 大写 WARNING 的规则。

容量口径（p27）：

| 指标 | IBS | IP-xBS |
|---|---|---|
| 每基站通话数 | 3 或 6 | 11 |
| PARI 数 | 1 | 8 |
| 每 PARI 基站数 | 256 | 254 |
| 全网基站数 | 256 | 2032 |

## A1 — 书中案例

**PARK 算例与 PLI 匹配**（p17-20）：

1. PLI=31、PARI=10000400100 → PARK=3110000400100（2 位十进制 PLI 接 11 位八进制 PARI）
2. PLI=29 时 "29 Digits are taken into account"：末 2 位 Don't care
3. PARI=10000412340 与 10000412350 仅末位不同，对 PLI=29 的手机等效，可同时兼容
4. 实验 PARI 约定 IBS=100004101x0、xBS=100004101x4（x=POD 号，实验口径），混合模式取 PLI=30（p244）

## A2 — 未来触发

使用情境：规划 DECT 标识；看不懂 PARI/PLI/PARK 配置字段；混合模式手机漫游不到新基站；算 PARK；判断要不要降 PLI。

语言信号：PARI / RPN / RFPI / PARK / PLI / IPUI / IPEI / multi-PARI / 逻辑 AND / 缩位匹配 / 31 位 / 降位。

与相邻能力区分：PLI 落到混合部署施工见混合部署能力；PLI 变更后推手机见自动重注册能力；基站对象层级（位置区/Site）见同步拓扑能力。

## E — 可执行步骤

输入契约：站点硬件构成（是否 IBS+xBS 混用）、现有 PARI/PLI 值、基站规模。缺现有值 → 先 dectinfo/dectview xbs 读现状。

1. 分硬件定 PARI：IBS 与 xBS 各规划一个 PARI（11 位八进制），新 PARI 高位尽量贴近旧 PARI。完成标准：每类硬件一个 PARI，值已登记
2. 定 PLI：单 PARI 保持 31；两 PARI 仅末位不同取 30，末 2 位不同取 29（按差异位数定）。完成标准：PLI 能让全部 PARI 对手机等效
3. 核算 PARK：PARK = PLI（2 位）+ PARI（11 位），逐位拼接。完成标准：可推算任意手机应存的 PARK
4. 落配置：PWT/DECT System 的 PLI for CTM 与 xBS/IBS Pari 的 PARI Value 字段。完成标准：dectview 显示新 PARI 生效

判停点：

- 新 PARI 与旧 PARI 高位完全不同 → 降 PLI 救不了，转自动重注册能力的 -forceUpdate 路线（先推手机后改系统）
- PLI 已降位但手机仍锁定旧基站 → 已注册手机需重注册或 -update 推送，不要反复改系统 PLI
- 客户要求"每站点一个 PARI" → 按书中口径纠正：PARI 粒度是每 OXE×每类硬件，站点切分用 Site

输出契约：PARI/PLI 规划表（每类硬件一行）+ PARK 核算记录。

## B — 边界

- PARI 两种表示（8 个十六进制位 / 11 个八进制位）等价；书中配置字段用 11 位八进制形态
- PLI 修改影响全部已注册手机；"降位后老手机自动兼容"仅对满足逻辑 AND 的 PARI 对成立（推断标注，见 needs-review nr-06）
- IPEI 与 IPUI 的换算关系书内未给出，不编造；IPEI 仅在 dectrm/8328 WBM 输出中出现（p176/p286）
- 实验值（PARI=100004101x0/x4、AC=1111）是实验口径，生产按客户编号规则替换
- 手机侧不手工输入 PARK：注册时输入的是 PIN 与 AC 码，PARI/PLI 由系统下发（p17）
