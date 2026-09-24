# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。

## nr-01 默认前缀 Note 与截图互换（两个互换方向相反）

- **位置**: 代接前缀 p314/p325；进出组前缀 p304/p320。
- **差异**: 两处 Note 文本与截图不一致，且方向相反——
  - 代接（p325 Note）："55 for the 'Group call pickup' prefix and 56 for the 'Direct call pickup'"；但 p314 概念图与 p325 截图均为 55=直接代接、56=组代接。**Note 是少数派**。
  - 进出组（p320 Note）："480 for the 'Sta. Group Entry' prefix and 481 for the 'Sta. Group Exit'"，与 p304 概念图（480 Group entry / 481 Group exit）一致；但 p320 截图行显示 480 对 Sta. Group exit。**截图是少数派**。
- **影响**: 按教材 Note 背前缀会在现场拨错方向（55/56 组）；按截图背会在另两组错。
- **处置**: 不采信任何一处的"标准答案"，能力卡统一口径为"以现场 Translator/Prefix Plan 按含义过滤实查为准"，并给出两处原文的双口径；候选 n28 与 p35 已按此记录。

## nr-02 PCS 版本漂移（教材截图来自不同批次）

- **位置**: p187（部署章）PCS 欢迎信息 R101.1-n4.523-0-fr-c0s1；p212（断链章）R101.1-n4.205-19-fr-c0s1。
- **差异**: 同一台 PCS VM 在两章显示不同 build 批次。
- **处置**: 版本核验方法（登录 mtcl 看欢迎信息比对 PCS ≥ CS）有效；具体 build 号不作标准值引用。候选 n46 已立条。

## nr-03 本地私到公溢出实验 RLAB 不可执行

- **位置**: p229 全大写说明："THIS LAB CANNOT BE PERFORMED WITH THE CURRENT RLAB ENVIRONMENT … PROVIDED ONLY AS INFORMATION, FOR CONFIGURATION PURPOSE ON CUSTOMER SITE."
- **影响**: 全书唯一课堂做不了的实验；培训学员对该特性无手感。
- **处置**: 能力卡（溢出）A1 段明确标注"信息性规程、现场可验"；交付建议组织现场演练或沙盘。候选 n21 已立条。

## nr-04 原文笔误与排版瑕疵（引用时注意）

- p54 "spacial redudancy"（应为 spatial redundancy）；p112 "adress"（应为 address）——原文界面文本照录。
- p474 "stred"（应为 stored）；p198 "fro" 类排版抖动以截图为准。
- p367 "Overflw to sec tandem"（系统参数原文少 i）——参数名照录原文，检索时注意。
- **处置**: 原文引用保留并注明；转述时用正确拼写。

## nr-05 容量数字三层口径（不可拆开引用）

- **位置**: p395（1488 并发 / 约 10000 呼时）、p395/p406（节点级全局上限，超限 6005）。
- **差异**: 1488=单链并发上限（24 接入×62 通道）；10000 呼/时=单链话务工程值（8 接入口径）；节点级全局上限覆盖 direct/SIP/ABCF-IP trunk 且默认 -1 不限。另 p43/p44 的 15000/100000 分机为系统标称上限、无话务模型。
- **处置**: 售前/交付引用任何容量数字必须带前提（每链/每节点/每系统 + 标称口径）；候选 n49 已立条。

## nr-06 候选页码归属修正一处

- **位置**: principle p13"OPUS dynamic payload type 默认 125"标注来源 p147-148/p156，实际原文位于 **p159**（System/Other System Param./Compression Parameters 的 How-To 说明）。
- **处置**: 断言为真；能力卡引用按 p159 标注。
