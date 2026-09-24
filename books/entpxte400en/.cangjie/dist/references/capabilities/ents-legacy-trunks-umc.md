# 传统中继（T0/T2）与 UMC 云管理

## R — 原文依据

> "'NODE NUMBER' MUST BE YOUR SYTEM ID OTHERWISE IT WILL BE IMPOSSIBLE TO ACCESS TO THE LOCAL TRUNK GROUP PARAMETERS OR TO ALLOCATE A TRUNK"（p784）
> "Available priorities: 0 to 199 • Shelf connected on the IP network • Available priorities: 200 to 254 • Priority 255 means access does not synchronize"（p779）
> "UMC is accessible via MyPortal (OPEX system) or Fleet Dashboard (OPEX or CAPEX). … Only 15 Parameters, 120 profiles depend on architecture"（p798, p807）

出处：ENTPXTE400EN p773-814。

## I — 自述

传统 ISDN 中继与云侧简化管理两件事：

1. **T0/T2 硬件**：T0=BRA 板（每口 2B+D，8 口板）；T2/T1=PRA 板（30/24 通道）；信令变体按运营商——VN 用 ISDN France、ETSI 用 ISDN all countries
2. **中继组五步**：核板在服；建 TG（节点号必须=本系统 ID、Tone on seizure、发送位数、DDI 转码）；本地参数（实体/去位数/B Channel）；建 Access（架-板-口）后必须 rstcpl 重置所在板；配同步优先级
3. **同步优先级**：Crystal 架 0-199、IP 架 200-254、255=不同步；参考钟由运营商提供，T2/T1 优先（T2 建议 200、T0 建议 205）
4. **抓取前缀**：#010/#012（Professional Trunk Seize）抓中继出局——SIP 中继不支持直抓（对照记忆）
5. **UMC 三功能**：Easy users（Profile 建户，仅 15 参数）、Easy SIP trunk（向导+约 120 架构 Profile，后台自动约 80 参数，不支持 Mini SIP）、Expert Configuration（云 WBM，免 LAN 直达）
6. **UMC 前提**：OXE N3-MD3+、Mid-Market 500 用户 day one、CAPEX 需 SPS 合同/OPEX 需 PoD 订阅、FTR&RTR 云连接就绪；入口 MyPortal 或 Fleet Dashboard，mtcl 凭据+Technical advanced 权限

## A1 — 书中案例

**T0 中继实验**（p781-788，How-To）：

1. WBM 核对 MG-BRA4 板在服
2. 建中继组 ID=10：类型 T0、节点号=本系统 ID、变体 ISDN France（教室口径）
3. 发送位数 10、DDI 转码 True、Number compatible with=-1
4. 本地参数：去位数按运营商（VN 4 位/ETSI 9 位，t3 核对）
5. 建 Access（架 12 板 4 口 0，实验口径）后 rstcpl 重置所在板
6. 同步优先级 205，客户侧 Network mode=no
7. 前缀 #010 抓取出局，trkstat 显示 2 个 B 通道 F 状态
8. t3 追踪 ISDN 呼叫核对主被叫号码

**T2 中继实验**（p789-796，How-To）：

1. 核对 PRA 板在服
2. 建 TG ID=12：类型 T2、节点号=本机、变体 ISDN France（教室口径）
3. 建 Access 后 rstcpl 重置板
4. 同步优先级 200（T2/T1 优先）
5. 前缀 #012 抓取，trkstat 显示 30 通道
6. NOS LED 关注线路无信号告警

## A2 — 未来触发

使用情境：传统 ISDN 外线开通；T2 同步告警（NOS）；运营商要求换信令变体；客户问能不能用云平台简化建户/建中继；UMC 走向导建 SIP 中继被拒。

语言信号：T0 / T2 / T1 / ISDN / BRA / PRA / 中继组 / trunk group / 同步 / synchro priority / NOS / 抓取 / #010 / UMC / Easy users / Easy SIP trunk / Fleet Dashboard / MyPortal。

与相邻能力区分：SIP 中继（无 # 直抓、走 ARS）见 SIP 中继能力；UMC 建 SIP 中继的前缀冲突规则涉及 ARS，细节见 SIP 中继能力；UMC 建户的对象仍是本卡外的用户体系，见用户终端开通能力。

## E — 可执行步骤

输入契约：运营商中继类型/信令变体/去位数/同步参考、（UMC）SPS 合同或 PoD 订阅与云连接状态。信令与位数必须拿到运营商书面值，教室口径不可带上生产。

1. 核板：BRA（T0）或 PRA（T2）板 IN SERVICE。完成标准：硬件承载就位
2. 建 TG：节点号=本系统 ID（强制）、变体与位数按运营商、DDI 转码按需。完成标准：TG 对象可访问本地参数
3. 建 Access：物理地址架-板-口，完成后 rstcpl 重置所在板。完成标准：通道在 trkstat 出现
4. 配同步：优先级按架构段（IP 架 200-254），客户侧/运营商侧 Network mode 分别设置。完成标准：同步锁定，无 NOS 告警
5. 配抓取前缀：#010/#012 绑 TG，出入话拨测。完成标准：出局可打、来话落地
6. （UMC 路线）核前提后走向导：Easy users 建户或 Easy SIP trunk 建中继，注意前缀冲突三岔口与完成后提示。完成标准：云侧配置落地并按提示补手工项

判停点：

- 中继组本地参数打不开/分配不了中继 → 节点号没填本系统 ID（p784 大写警告），先改节点号
- T2 无信号 NOS 告警 → 查线路与同步优先级/Network mode 侧别，不要先动 TG 参数
- UMC 建中继被拒 → 前缀已存在且非 ARS 前缀（n40）；改走手工配置或先理顺存量前缀
- 客户功能在 UMC 排除清单里（话务台/ACD/多实体/酒店等）→ 停，UMC 不覆盖（n39），回本地图形工具路线

输出契约：可用的 T0/T2 中继（同步锁定+拨测通过）或 UMC 云侧配置记录 + 剩余手工配置清单。

## B — 边界

- 教室信令（ISDN France）、10 位发送、#010/#012、同步值 200/205 均为实验口径（nr-04）；现场以运营商为准
- -48V/机架工艺、运营商侧线路开通为书外前提；T1（24 通道）仅规格提及，实验链未覆盖
- UMC 为 R1.1 快速演进功能：多处标 NEXT DELIVERY（Desk Sharing 等，n39）；截图口径会漂移
- UMC 安全与合规（法国 OVH 机房、TLS1.2、ISO/IEC 27001）为书内声明，商务与数据合规评估在书外
- Crystal 架同步段 0-199 仅为存量场景；新项目按 Common/IP 承载
