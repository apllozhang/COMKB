# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 原文笔误 "Diffie-Helmman"（p7）

- **位置**: p7 非对称算法清单 "Asymmetric algorithms : RSA, ECC, Diffie-Helmman…"。
- **判断**: 应为 Diffie-Hellman（密钥交换算法），原书拼写脱漏。
- **处置**: 原文引用保留并注明；能力卡转述时用正确拼写 Diffie-Hellman。

## nr-02 GD4 V24 串口速率 "11520-8-N-1"（p367，含推断）

- **位置**: p367 "9600-8-N-1 for GD3, 11520-8-N-1 for a GD4"。
- **判断**: 全书仅此一处、无 115200 出现；业界串口标准值为 115200，疑原书脱漏一个 0（推断，非书中明示）。
- **处置**: 原文照录；实操按设备文档核实后再用。能力卡引用时保留"原文如此"与推断标注。

## nr-03 原文笔误 "ENCRYTPION"（p247）

- **位置**: p247 Warning 框 "SIP TRANSLATOR HOSTNAME CONFIGURATION IS MANDATORY ONLY WHEN EXTERNAL ENCRYTPION GATEWAY(S) IS(ARE) DEPLOYED"。
- **判断**: 应为 ENCRYPTION，不影响语义。
- **处置**: 原文引用保留并注明；转述时用正确拼写。

## nr-04 ITSP2 章内 ITSP1/ITSP2 标签混用（p43-46）

- **位置**: 章题为 ITSP2 SIP GATEWAY，但正文网关账号/公网网关/SIP 域混用 itsp1 命名（gateway.itsp2.com 与 public.itsp1.com、publicP@itsp1.fr 交替出现）。
- **判断**: 同一模拟器的两条腿（SIP 网关 + 公网网关），命名混用为原书现象（n33 已归并）。
- **处置**: 能力卡统一表述为"模拟器两腿"，引用具体域名时按原文标注；不采信单一标签作配置依据。

## nr-05 推断性结论与时效性承诺（引用需带标注）

- n33: GD4 串口速率 11520 疑为 115200（同 nr-02，标"推断"）。
- p78: "By the end of 2025, any newly produced board will embed a default ALE certificate"——时效性承诺，读书时需核对当前出厂策略是否兑现。
- p50: 时间同步仅 "recommended" 一句，证书有效期校验对 NTP 的强依赖为机制推断（n34 已按原书约束记录）。
- **处置**: 三条均已标"推断/时效"；能力卡引用时保留标注，不升格为书中明示事实。
