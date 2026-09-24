# coverage-audit.md — 任务覆盖审计（阶段 1.5 产出）

> 基准: BOOK_OVERVIEW.md 原书关键任务清单 task-01 ~ task-18（18 项）
> 审计对象: verified.md 23 个 verified 单元 + 1 个 reference 单元 + references.md 外部参考 + GLOSSARY 46 术语
> 结论: **18/18 全覆盖，无缺口**；硬件规格/HA/UM/容量工具等生产化内容为原书明确外指（诚实外置，不算缺口）

## 任务 × 验证单元映射

| task | 任务 | 验证单元 | 证据素材（principle/case/counter） | 覆盖判定 |
|---|---|---|---|---|
| task-01 | 部署形态与容量口径决策 | f02, f03, f04, f05, f09（15000 标注） | p01, n26, n27, n28 | ✅ 定位/架构/组网/商业包/规模口径齐；规格与容量工具书外指针（n28） |
| task-02 | 实验环境拓扑 | f07（reference） | n17 | ✅ 拓扑对照表 + DNS 地基（p02）；搭建操作原书即为课前准备 |
| task-03 | 许可证体系部署 | f06 | p05, n06, n07, n08 | ✅ flex-lm 四层 + dongle 绑定 + 核验路径 |
| task-04 | OTMC 服务器安装 | f08, f09, f10 | c01, p04, p25, n25 | ✅ 物料/三模式/虚机规格与调优 |
| task-05 | post-installation wizard | f11 | c02, p02-p07, n01-n05 | ✅ 13 步骨架 + DNS/账户/备份/安全四类硬规则 |
| task-06 | 手工装/换许可 | f06 | c02（步骤 11-12）, n08 | ✅ SFTP/flexlmd/lmstat 标准路径 |
| task-07 | OXE 准备并声明进 8770 | f12, f13 | c03, p08, p09, n09 | ✅ 编号公式 + 同步矩阵 + APPLY 警告 |
| task-08 | OTMC 声明与拓扑对置 | f12, f13 | c04, p08, n17 | ✅ bics.conf 对账 + 拓扑对称声明 + 口径漂移登记 |
| task-09 | OXE SIP 对接 | f14 | c05, p09, p10, n29 | ✅ 四段参数结构；空间冗余外指 TC1652 |
| task-10 | Connection 用户与话机 | f15 | c06, p11, n24 | ✅ 建户/寻址三法/许可核查两法 |
| task-11 | OTMC 账户与信箱交付 | f16 | c07, p12, p13 | ✅ 三级对象模型 + 强制 profile + 许可权 |
| task-12 | profile 定制 | f17, f18 | c08, p14, p15 | ✅ 参数地图 + my_profile 实验值 + 问候语管理 |
| task-13 | 自助门户 | f19 | g13, p12, p24 | ✅ 双应用入口与功能区；书内无独立实验（界面导览章，case 侧已注明） |
| task-14 | SMTP/SMS 通知 | f20 | c09, p16-p19, n11, n12, n15, n16, n21, n22 | ✅ 链路 + 双矩阵 + 模板/排障 |
| task-15 | IMAP 访问 | f21 | c10, p20, n13, n14 | ✅ 三处对齐 + 验收判据 |
| task-16 | general announcement | f22 | c11, p21, n18, n19, n20 | ✅ 场景/录制/权限/硬限制 |
| task-17 | 备份恢复 | f23 | c12, p22, p25, n05, n10 | ✅ 两段式 + 删用户入口 + NFS 规则 |
| task-18 | 语音信箱统计 | f24 | c13, p23, n30 | ✅ 参数默认值 + 目录/权限/mascd |

## 覆盖质量说明

1. **无孤儿单元**：23 个 verified 单元 + f07（reference）全部映射到至少一个任务；f01（课程主线）与 f02/f03（定位/架构）作为全局底座映射到 task-01 的认知前提。
2. **诚实外置**（不算缺口，属原书边界）：

   | 书外内容 | 外指文档 | 依据 |
   |---|---|---|
   | 硬件/软件规格与产品上限 | feature list / product limits | p13/p48 Note（n28） |
   | OTMC-V 生产部署参数 | MyPortal 安装手册 otmc2.6.1 | p58 Note |
   | 空间冗余 SIP 网关配置 | TC1652 | p105 Warning（n29） |
   | 8770 上 NFS server 部署 | TC2024（Business Portal） | p246（n29） |
   | 问候语管理细节 | Quick Reference Guide | p142 |
   | HA 高可用、容量规划工具、UM 落地 | 后续课程 / Capacity Planning Tool / 书外 | p74（n23）、p19（n28）、p169（n28） |

3. **无实验的概念章**（task-01/02/13）由框架+原则+反例条目覆盖，案例类天然为空——与 case-extractor 自检结论一致（task-13 门户操作散嵌于 c07/c09/c10，属原书结构非提取遗漏）。
4. **数字口径终审**：端口 5040/5060/2570、15000×3/5000、2MB/80%/25、许可 L173/174/176/177/316/317、my_profile 全参数、统计默认值全集、时长 25 分钟/30 分钟/<5 分钟——全部回原文逐格一致；四处书内口径漂移（节点号/网段/掩码/GA 路径）与 VMS 拼写漂移已在 needs-review 编号登记。
