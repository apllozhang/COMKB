# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 p558 "29 or 120 CCs max" 与图示 15/120 矛盾

- **位置**: p558 正文 "From a physical limit point of view, 29 or 120 CCs max can be connected to the AFE."；同页图示为 "15 connections (Internal CCs server) / 120 connections (External CCs server)、14 connections max + 1 connection"。
- **差异**: 正文 "29" 与 p557（内部 15/外部 120）、p567（>9 强制上 Server）、图示 15/120 全部不符。
- **影响**: CCS 客户端规模规划的判定边界。
- **处置**: （推断）"29" 为笔误；规划按内部 Server 15 客户端、外部 Server 120 客户端、AFE 物理上限 15 连接执行；引用原文时标注"原文如此"。n37 已完整记录。

## nr-02 p236 统计 Pilot 号 31650 与实验正文 31660 不一致

- **位置**: p236 Notes "Don't modify the Car_Profile, which is attached to the statistic Pilot 31650" vs p155 实验正文 "Call profile called Car_Profile assigned to Car Insurance statistic pilot (31660)"。
- **判断**: 31650 是讲义章示例号（p123），p236 沿用示例号串入实验笔记；（推断）教材笔误。
- **处置**: 操作以现场实际配置（31660）为准；引用 p236 时标注页码语境。n13 已记录。

## nr-03 LCA 关键字命名混用（LAST_CALLED_ / LAST_CALL_）

- **位置**: 讲义定义 p253 用 LAST_CALLED_ELAPSED_TIME / LAST_CALLED_STATE；脚本范式 p254 与 How-To p264 用 LAST_CALL_ELAPSED_TIME / LAST_CALL_STATE。
- **影响**: 手敲脚本条件时两套拼写混写会编译不过或查无此变量。
- **处置**: 以 ASM Script Editor 下拉可选值为准（How-To 的选择路径可执行）；转述时注明两套拼写并存。n16 已记录。

## nr-04 p364 坐席称号与分机不符——"Agent2 (32500)" 实为 Agent3

- **位置**: p364 门限测试 "check that the call is transferred to Agent2 (32500) after 15 seconds"。
- **判断**: 本实验中 32500 是远端新坐席 Agent3；Agent2 是本地 31501。括号内分机号为准，称号系笔误。
- **处置**: 照书执行 Remote PG 实验时以分机号为准；验证记录统一用"分机号+坐席号"双写。n38 已记录。

## nr-05 重选次数两种表述并存（21 次执行 vs 21 请求/20 次执行）

- **位置**: p214 "The script is used 21 times"、p245 "The maximum number of script execution is 21 times" vs p220 "the alb process makes 21 requests (script is executed 20 times)"。
- **处置**: 两处均按原文收录，不强行归一；对客户表述用"重选上限 21"口径并注明另有"21 请求=20 次执行"的等价表述。p10/n07/n09 已记录。

## nr-06 SPM 端口 61618 与 RTIConnector.ini 示例 61668 数字不同

- **位置**: p387 防火墙放行 "61618 for active MQ" vs p391 配置示例 "WBMPortNum=61668"。
- **判断**: 角色不同——前者是防火墙放行值，后者是文档示例环境的配置值；非同一参数的矛盾。
- **处置**: 防火墙规划以 61618 为准；RTIConnector.ini 按现场部署填写，示例值不作依据。p24/p27 已记录。

## nr-07 原文拼写笔误与小项备查（引用时注意）

- p478 告警对象类型 "WaintingQueue"（应为 WaitingQueue，原文如此）。
- p66/p161 "Agent Selection Modul"（p161 另作 Module）；p215 "realy working"（应为 really）。
- p493-494 导入路径 "C:/Program Data /Alcatel"（含空格，实际为 ProgramData）。
- **处置**: 原文引用保留并注明"原文如此"；转述与配置路径用正确拼写。

## nr-08 三处含推断成分的结论（引用需带标注）

- n37 的 "29 为笔误" 判断（依据为同页图示与他章口径，无勘误表佐证）。
- n13 的 "p236 沿用讲义示例号" 判断。
- n16 中 "以编辑器下拉可选值为准" 的操作建议（书内未明说，由 How-To 可执行性推得）。
- **处置**: 三条均已标"（推断）"；能力卡引用时保留推断标注，不升格为书中明示事实。
