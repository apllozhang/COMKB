# coverage-audit.md — 任务覆盖审计（阶段 1.5 产出）

> 基准: BOOK_OVERVIEW.md 原书关键任务清单 task-01 ~ task-19（19 项）
> 审计对象: verified.md 18 单元 + 2 reference 单元 + references.md 外部参考 + GLOSSARY 66 术语
> 结论: **19/19 全覆盖，无缺口**；三处生产化数值为书外指针（诚实外置，不算缺口）

## 任务 × 验证单元映射

| task | 任务 | 验证单元 | 证据素材（principle/case/counter） | 覆盖判定 |
|---|---|---|---|---|
| task-01 | 网络前提核查 + Pilot 评估 | f06, f07 | p02, n02 | ✅ 结构与工具入口；端口/帶寬数值为书外 PDF 指针（n02） |
| task-02 | 公司体系规划与创建 | f08 | p03-p05, n06-n08 | ✅ 概念/可见性/认证/建司六步全覆盖 |
| task-03 | 管理员权责 + 目录/频道 | f09 | p06, n09 | ✅ |
| task-04 | 订阅开通与分配 | f05, f10 | p01, p09, n01, n03 | ✅（实验口径月付规则一并入册） |
| task-05 | RLAB/OXE 实验环境配置 | f02/f03（reference）+ c02 | f02, f03, c02 | ✅ 教学基础设施，rxe-lab-pod-setup 路由卡承载方法论，环境值入 book/overview |
| task-06 | OXE DNS/代理配置与连通验证 | f11（前提段） | c03, n10, n11 | ✅ netadmin 路径与两类误判（URL ping/证书错误）齐备 |
| task-07 | OXE 接入 Rainbow + 验证维护 | f11 | p26, c04, n12 | ✅ 接入动作 + 四抓手维护闭环 |
| task-08 | 成员创建与管理 | （并入 f08/f10 单元的操作面） | p07, p08, c01, n04, n05 | ✅ 密码策略、宽限期、SPAM/JOIN 两坑齐备 |
| task-09 | 分机关联与 RCC 五项测试 | f12（RCC 行） | p10, c05 | ✅ 含 Rainbow number 机制 |
| task-10 | 用户形态决策（RCC/REX/纯 REX/DECT） | f12 | p10, p14, n13, n14 | ✅ 四形态矩阵 + 路由四案例 |
| task-11 | 远程延伸配置（Ghost Z/REX/tandem/溢出） | f13 | p11-p13, c06, n20 | ✅ 机制 + 配置 + Nomadic 三测 |
| task-12 | WebRTC 网关部署配置 | f14 | p15, c07, n15-n17 | ✅ 部署链 + mpcheck 排障 |
| task-13 | 网关升级（远程/手动） | f14（升级段） | c08, n18 | ✅ 两法对比 + 失败处理 + 版本/地域门槛 |
| task-14 | OXE 侧网关九件套 + VoIP 测试 | f14（OXE 侧块） | p16-p18, c09, n19, n28 | ✅ 全书最重 How-To，逐字段证据齐备 |
| task-15 | 共享网关池与容量规划 | f15, f16 | p19-p21, n27 | ✅ 三配置对比 + 406 溢出 + TBE067 四输入 |
| task-16 | 4059EE 话务台交付 | f17 | p24, c10, n20-n22, n24, n26 | ✅ 含在场差异双测试 |
| task-17 | Rainbow Attendant Console 与互助组 | f18 | p22, p23, c11, n23, n24 | ✅ 订阅/建组/规格/代接边界 |
| task-18 | 维护体系排障 | f19 | p26, p27, p28, n29, n30 | ✅ 云侧五入口 + OXE/网关侧抓手（嵌于 c04/c07/c09） |
| task-19 | Teams 集成全流程 | f20 | p25, c12-c14, n25 | ✅ 架构 + 租户侧 + 用户侧 + 终端侧 |

## 覆盖质量说明

1. **无孤儿单元**：18 个 verified 单元 + 2 个 reference 单元全部映射到至少一个任务；f01（课程主线）与 f04（平台架构）作为全局底座映射到 task-02/task-10/task-12 的认知前提。
2. **三处诚实外置**（不算缺口，属原书边界）：

   - task-01/task-12 的端口、带宽、TURN、防火墙白名单数值——原书仅给官方文档指针（Network Requirements PDF、VoIP calling Troubleshooting guide），candidates 如实标注未编造（n02/n17）。
   - task-13 的远程升级适用范围（1.73.x+、35 国清单）会随版本演进，以支持网站文章为最新依据（n18）。
   - task-15 的 TBE067 工具本体与流量建模假设在书外（MyPortal/ALE 内部链接，p151）。
3. **无实验的概念章**（task-01/02/03/10/15/18）由框架+原则+反例三类条目共同覆盖，案例类天然为空——与 case-extractor 自检结论一致，属书的结构而非提取遗漏；task-04 的实验口径分散在 c01/c06/c11 中，已归并。
4. **数字口径终审**：五链路事件码（4503/4505/4509/4507/4511）、路由四案例矩阵（p116）、判别器五元组（Call Number 1/Area 1/route list/schedule -1/位数 17）、SIP 外部网关逐字段（端口 5060/UDP、监督 380、DTMF 101、G711-only）、单网关 400 并发流、监督组 5/30、队列 OXE 10/OXO 8、互助 4 路、REX 10/Anydevice 8、10 天宽限、密码 12+3 类字符、溢出计时器 100ms 步进——全部与原文逐格一致。
