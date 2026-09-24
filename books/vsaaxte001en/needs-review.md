# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 GRUB 实验口令两处大小写不一致

- **位置**: p92 "Grub access (Bios access) must also be secured with a password: Generalconfig1!"（小写 c）vs p93/p249 "Set the following password to secure access to GRUB. … GeneralConfig1!"（大写 C）。
- **影响**: 照抄任一写法都可能登不进系统引导；GRUB 口令仅约束"最少 14 位"，具体值本应由现场自定。
- **处置**: 能力卡与 DIGEST 不引用具体口令值，只保留"≥14 位"规则；实验复现时以环境实际值为准。已回源文逐字复核属实。

## nr-02 证书章验证 URL 笔误

- **位置**: p126 "Enter the URL to connect to VAA web interface. https://192.168.1.1.55"。
- **判断**: 多写一位 ".1"，正确为 `https://192.168.1.55`（与全书其它页一致）。
- **处置**: 转述时用正确 URL；引用原文时标注"原文如此"。

## nr-03 SIP 抓包样例残留旧版本号

- **位置**: p157 User-Agent "Visual Automated Attendant 4.2.15"、p228 "Visual Automated Attendant 4.3.005"。
- **判断**: 历史版本环境抓包，与本书 R4.8.006 不一致；抓包里的报文头（含 P-Alcatel-CSBU: bypass=on 等私有头）机制仍有效，但版本字段不可逐字比对。
- **处置**: 能力卡引用 SIP 证据只取头字段语义，不引用版本号；现场比对以实测为准。

## nr-04 许可版本项数值两处不一致

- **位置**: p253 `vaa services` 输出 `VAA_RELEASE : [11]`（与 p89 "A new license (Release 11) is required" 一致）；p274 `.lic` 样例 `FEATURE VAA_RELEASE ALCFIRM 1.0 04-jul-2025 9 HOSTID=ANY`。
- **判断**: p274 为历史样例文件（早于换版），两页口径不同；运行态以 vaa services 输出为准。
- **处置**: 能力卡写"4.8.006 强制 Release 11"；样例页数值不再转述。

## nr-05 原文笔误两处（引用时注意）

- p295 "Since version **A** 4.6.104, password expiration is enabled by default"（"A" 为多余字符）。
- p74/p238 课堂环节依赖 Thunderbird 档案配置（非笔误，但为教学专用操作，不进能力卡正文）。
- **处置**: 原文引用保留并注明；转述时用正确表述。

## nr-06 glossary 候选收尾自检计数偏差

- **位置**: candidates/glossary.md 头部记"共 58 条"，收尾自检写"总数 54 条大于 17"。
- **判断**: 实数 58 条（concept 20 + role 2 + subscription 4 + product 14 + protocol 12 + resource 6，g01-g58 连续无缺）；自检句中"54"为笔误。
- **处置**: 下游以 58 条为准；book/glossary.md 收录全部 58 条。

## nr-07 三处含推断成分的表述（引用需带标注）

- "Slave 不是自动接管的热备"的定性表述——行为依据（只读/丢话/不自动回同步）均为原文直引，"热备"对比为引申。
- n47 "OXE 侧通常无需动编解码但要核对匹配"——原文说 "nothing to do on OXE side"（N2 起），"但要核对"为对老现场/改过配置场景的实践引申。
- n45 "统计缺口报障的答复口径"——运维实践引申，行为依据为原文。
- **处置**: 三条在能力卡中保留推断标注，不升格为书中明示事实。
