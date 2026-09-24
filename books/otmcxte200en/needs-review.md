# needs-review.md — 待复核项（阶段 1.5 产出）

> 原则：如实记录、不脑补。每项给出处置建议；下游能力卡的 Boundary 段引用对应编号。
> 提取器登记的 4 处口径漂移（n17 节点号/网段/掩码、n18 GA 路径、n25 笔误、n19 AA 废弃）均已回原文复核后编号入册。

## nr-01 OTMC 节点号示例两处不一致（98 vs 99）

- **位置**: p94 实施参数 "Subnetwork-Node number=98" vs p95 字段说明 "Node number is a free number … (Use 99 for example)"。
- **差异**: 同一声明动作的示例值两页不同。
- **判断**: 规则本身两处一致（自由编号、必须不同于网内所有 OXE 节点号），仅示例值漂移。
- **处置**: 能力卡按规则表述（"自由号、不撞 OXE 节点号"），引用示例时注明 nr-01；培训材料不要把 98 或 99 当"标准值"。

## nr-02 实验网段漂移：151.1.1.x 与 155.1.1.x 混用

- **位置**: 拓扑章（p21-32）全用 151.1.1.x；声明章 p92/p94 的 nslookup 示例突然切到 155.1.1.x（DNS 服务器 155.1.1.100）；且 p94 反查示例输入 155.1.1.50、返回却是 otmc.company.com = 155.1.1.60。
- **差异**: 同一实验环境的网段与反查自相矛盾。
- **判断**: 示例仅示意，疑为旧版课程示例残留（推断，非原书自述）。
- **处置**: 全部记"实验口径"，实际以自家拓扑表为准；能力卡正文不引用具体网段，实验值集中在 book/overview 备查。

## nr-03 p84 netadmin 输出示例掩码与配置表不符

- **位置**: p84 netadmin 输出示例 "Netmask : 255.255.0.0"，同页设置表为 255.255.255.0（/24）。
- **处置**: 以配置表 /24 口径为准；引用输出示例时注明原文如此。

## nr-04 general announcement wav 存放路径两处不一致

- **位置**: p223 结论页 "/var/data/general_announcement" vs p227 How-To 操作页 "/var/data/ics-group/general_announcement"（原文空格 "/var/ data/ ics-group/" 为排版所致）。
- **判断**: 提取器推断 ics-group 版本疑似 R2.6 实际路径（与统计文件 /var/data/ics-group/vms 同族），但教材自身未统一——推断属性保留。
- **处置**: 能力卡给两个页码口径并建议现场以系统实际目录（ls 核实）为准，不按单一页码硬记。

## nr-05 原文笔误群（引用时注意）

- p52 安装流程出现 "Red Hat installation"（本书 OS 为 SUSE Linux Enterprise，p13/p48/p60 互证）。
- p53 "CheckSytemLinux.sh" 与 p66 "CheckSystemLinux.sh" 两种拼写并存（以 p66 能执行的拼写为准）。
- p84 "20. 'APPLY MOFIFICATION'"（MODIFICATION 之误）。
- p36 "the Operating Sytem installation"（System 之误）。
- **处置**: 原文引用保留并注明；转述时用正确拼写，不把笔误当知识点。

## nr-06 VMS 默认名拼写漂移（本轮新发现）

- **位置**: p137 "Select 'defaultVmLS'" vs p138/p188 "defaultVmsLS"。
- **差异**: 同一默认语音邮件系统名两种大小写并存（已回原文 grep 复核，两处确实不同）。
- **处置**: 能力卡按 p138/p188 的 defaultVmsLS 表述（出现频次高的写法），并在卡内注明 p137 界面原文为 defaultVmLS；现场以 WBM 实际显示为准。

## nr-07 含推断成分的结论（引用需带标注）

- n17: "疑为沿自旧版课程的示例残留"——推断，非原书自述。
- n18: "ics-group 路径疑似为 R2.6 实际路径"——推断，原书未统一。
- BOOK_OVERVIEW 批判节: "8770 侧 Windows 2008 R2 许可键（p49）与 Fax Server Windows 2019（p38/p40）混用属时代口径"——整理者判断。
- **处置**: 三条均保留推断标注；能力卡引用时不升格为书中明示事实。
- **反例（不是问题）**: p184 "Occupancy ratio threshold (%) 80" 原文带 "(by default 80%)"——80% 为原文明示默认值，提取与引用均可直接使用，无需标注推断。
