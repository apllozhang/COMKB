# coverage-audit.md — 任务覆盖审计（阶段 1.5 产出）

> 基准: BOOK_OVERVIEW.md 原书关键任务清单 task-01 ~ task-20（20 项）
> 审计对象: verified.md 16 单元 + 2 reference 单元 + references.md 外部参考 + GLOSSARY 56 术语
> 结论: **20/20 全覆盖，无缺口**；无线工程方法论与生产化数值为书外指针（诚实外置，不算缺口）

## 任务 × 验证单元映射

| task | 任务 | 验证单元 | 证据素材（principle/case/counter） | 覆盖判定 |
|---|---|---|---|---|
| task-01 | DECT 技术底座与标识号码体系 | f03, f04, f05, f06 | p01-p09, g01-g56 概念/资源域 | ✅ 频段/复用/帧/六号码/安全三级全覆盖 |
| task-02 | 产品线与拓扑选型 | f02, f17 | p04, p28, n01, n12-n14, n19 | ✅ 三分结构 + 六拓扑四格判定 |
| task-03 | 配置培训 POD 实验环境 | f07, f08（reference） | c01 | ✅ 教学专用口径，仅作环境背景（BOOK_OVERVIEW 明示不 skill 化） |
| task-04 | 部署 8378 IP-xBS | f09, f14, f15 | p10, p15, p16, p19, c02, n15, n20, n22 | ✅ 全流程 + 注册开关规则 |
| task-05 | 更换故障 IP-xBS 保 RPN | f14（注册机制） | p20, c03, n18 | ✅ 手动注册序列与 RPN 漂移反例齐备 |
| task-06 | 收集 xBS 日志到 syslog | f15（路径） | p18, c04, n16 | ✅ 四级日志口径 + 端口 514 |
| task-07 | 创建 DECT 用户并注册手机 | f15（路径） | c07, c10, n03 | ✅ 双通道互斥 + 近乎同时约束 |
| task-08 | 注销/更换/删除手机 | f15（路径） | c08, p08 | ✅ dectrm + IPUI/IPEI 核验 + 用户保留技巧 |
| task-09 | IP-xBS 固件后台升级 | f16 | p17, n15 | ✅ downstat x 四项菜单 + 自动复位策略 |
| task-10 | 手机固件空中升级 | f16 | p21, p22, n08, n09 | ✅ downstat m + A/X/M 状态机 + 三类限制 |
| task-11 | 多站点管理 | f11, f17 | c05 | ✅ Site 创建/分配/漫游验证 |
| task-12 | 无线覆盖勘测 | f03（RSSI 语义） | p14, c06, n17 | ✅ 门槛数字 + survey mode 开关；方法论在 8AL90874USAA（书外指针） |
| task-13 | 部署 8379 IBS 基础设施 | f15（IBS 域路径） | p27, c09, n01, n27 | ✅ UA 板卡/布线/建站/维护命令 |
| task-14 | 混合 DECT 基础设施部署 | f13, f15, f17, f04（PLI 机制） | p23, c11, n02 | ✅ 统一 PLI=30 + 多 PARI 语义 |
| task-15 | 手机自动重注册 | f04（PLI 机制） | p24, p25, p26, c12, n10, n11 | ✅ -update/-forceUpdate/-f 批量 + 结果文件 |
| task-16 | 跨 PARI 外部同步与外部 handover | f13 | p12, p13, c13, n05, n06, n07 | ✅ Sync Master/Backup/External Sync/Highway 全链 |
| task-17 | 部署 8328 SIP-DECT | f18 | p28, p29, c14, n23, n24 | ✅ DHCP 固定 IP + 四步注册 |
| task-18 | 部署 8328 双小区并验证 | f18 | n04, n25 | ✅ 主站判定 + 5 分钟链路预期 |
| task-19 | 日常维护与排障 | f12（标志判读）, f13（工具）, f16（downstat） | p30, n20 | ✅ 命令族清单；深度抓包在 8AL91443ENAA（书外指针） |
| task-20 | 配置 DECT 安全级别 | f06 | p09, n01 | ✅ 三级语义 + AC 治理；生产密钥策略在书外 |

## 覆盖质量说明

1. **无孤儿单元**：16 个 verified 单元全部映射到至少一个任务；f01（课程主线）作为全局底座映射到 task-01/02 的认知前提；f07/f08 两个 reference 单元对应 task-03（教学专用，原书边界明确）。
2. **两处诚实外置**（不算缺口，属原书边界）：
   - task-12 的勘测方法论（传播模型、天线选型、勘测判定流程）——原书外置到《DECT and IP-DECT Engineering Rules and Site Survey Kit Manual (8AL90874USAA)》（p212/p216 指针），书内只有 RSSI 门槛数字与 survey mode 开关。
   - task-19 的深度排障（PCAP 分析）与 task-20 的生产密钥治理——分别外置到 8AL91443ENAA 排障指南与客户安全基线，书内只给命令族与字段名。
3. **无独立 How-To 章的任务**（task-01/02/09/10/19/20）由框架+原则+反例三类条目共同覆盖，属书的结构而非提取遗漏——与 case-extractor 自检结论一致。
4. **数字口径终审**：p27 容量表（IBS 3 or 6/1/256/256 对 xBS 11/8/254/2032）、p208-210 RSSI（-70 easy/-60 tricky/-80 站间同步）、p84-85 位置区（64 区、RPN 区间映射）、p102 Sync Cluster（8 簇/默认 0/单站 8 簇）、p147 注册开关（全网单节点、auto=255）、p150 首个空闲 RPN、p196 >1km、p244 PLI=30、p252-253 重注册版本与性能、p272 8328 容量、p288 主站判定、p291 双小区 5 分钟——全部与原文逐格一致。
