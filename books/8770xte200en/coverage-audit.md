# coverage-audit.md — 任务覆盖审计（阶段 1.5 产出）

> 基准: BOOK_OVERVIEW.md 原书关键任务清单 task-01 ~ task-28（28 项）
> 审计对象: verified.md 24 个 verified 单元 + 1 个 reference 单元 + references.md 外部参考 + GLOSSARY 60 术语
> 结论: **28/28 全覆盖，无缺口**；高可用/生产安全基线为原书边界外内容（诚实外置，不算缺口）

## 任务 × 验证单元映射

| task | 任务 | 验证单元 | 证据素材（principle/case/counter） | 覆盖判定 |
|---|---|---|---|---|
| task-01 | Windows 2022 安装 8770 服务器 | f05 | p01, p04-p07, c01, n07-n11, n52 | ✅ 七步主链完整 |
| task-02 | Windows 2019 安装 8770 服务器 | f05 | c02, n45 | ✅ 与 2022 并列；旧版沿用口径见 needs-review nr-01 |
| task-03 | 客户端安装与首次连接 | f06 | p08, p45, c03, n12-n14 | ✅ |
| task-04 | 注册 OXE 节点并同步 | f07, f08 | p09-p11, c04, n20 | ✅ 声明/同步/实时核验/排障闭环 |
| task-05 | OXE SSH 安全访问 | f09 | p12, p13, c05 | ✅ |
| task-06 | OXE 配置界面高效操作 | f07（结构侧） | c06 | ✅ 操作手法主体在 case，交付 oxe-ui-efficiency 卡 |
| task-07 | OXE Profile/Key Profile | f11 | p14, c07 | ✅ |
| task-08 | 空闲号码段与 Meta profile | f11 | p15, c08 | ✅ |
| task-09 | Users 批量开通 | f12 | p16, c09, n15 | ✅ |
| task-10 | WBM 轻客户端开通 | f12, f25 | p16, p17, c10, n16-n18 | ✅ |
| task-11 | OXO Connect 节点声明 | f07, f10 | p43, c11, n46, n47 | ✅ |
| task-12 | OXE 告警上送 | f14 | p20, c12, n20 | ✅ |
| task-13 | 告警定制（签名/字典/邮件/脚本） | f13 | p19, p21, c13, n34 | ✅ |
| task-14 | SNMP Proxy 部署与过滤 | f15 | p22, c14, n21 | ✅ |
| task-15 | Topology 标准视图 | f16 | c15, n23, n24 | ✅ |
| task-16 | Topology 自定义视图与告警重定向 | f16 | c16, n22 | ✅ |
| task-17 | 安全管理（密码/管理员/组/解锁/访问控制/TLS） | f17 | p30-p35, c17, n25-n31 | ✅ |
| task-18 | Audit 启用与使用 | （流程在 c18；架构由 f13/f17 侧写） | p36, p37, c18, n32, n33 | ✅ 交付 audit-compliance 卡 |
| task-19 | 报告生成/导出/计划 | （流程在 c19；上限数值 p23） | p23, c19, n35, n36 | ✅ 交付 reports-scheduling 卡 |
| task-20 | Scheduler 任务编排 | f18 | p24, c20, n37 | ✅ |
| task-21 | 自动维护与数据清除 | f19 | p25, c21, n38 | ✅ |
| task-22 | 8770 备份恢复与 rehosting | f20 | p26, p27, c22, n39 | ✅ |
| task-23 | 维护工具（Diagnostic/DirManag/HeidiSQL） | （流程在 c23） | p28, c23, n42 | ✅ 交付 maintenance-operations 卡 |
| task-24 | NMC 服务与日志管理 | f21 | p29, c24, n40, n41 | ✅ |
| task-25 | OXE 备份与恢复 | f22 | p41, p42, c25, n43 | ✅ |
| task-26 | 许可查询与更新 | f23 | p38-p40, c26, n44, n48, n49 | ✅ |
| task-27 | 映射网络驱动器 | f24 | p44, c27 | ✅ |
| task-28 | 解决方案架构与容量要求 | f03, f04, f23 | p02, p03, p39, n02, n03, n50, n51 | ✅ 架构/虚拟化/兼容矩阵/许可包型齐备 |

## 覆盖质量说明

1. **无孤儿单元**：24 个 verified 单元全部映射到至少一个任务；f01（课程主线）作为全局组织轴映射到全部任务的认知前提，f02（RLAB）落位 book/overview 环境区。
2. **诚实外置**（原书边界，不算缺口）：
   - 8770 高可用/双机/多 8770 分级——书内仅许可文件 Redundancy 字段一笔带过（n50），生产设计须引用 High Availability 文档。
   - 生产安全基线——明文密码（n52）、Defender 排除与 IE ESC 关闭的客户审批、POODLE/全网元 TLS 摸底方法（n31 只给前提不给核查清单）。
   - Capacity Planning 工具用法与 hypervisor 侧 SNMP 规则——只给指针（n51）。
3. **两套并列安装章的口径差**（task-01/02）：2022 章与 2019 章在 cfg 文件名、DNS 指向、WMIC 附录三处不一致，已在 needs-review nr-01 记录并以 2022 章为基准、2019 章作并列参照。
4. **数字口径终审**：节点号公式（网络号×100+节点号，p112/p123；OXO 声明节点 (1x100)+80=180，p658）、报告上限（TXT 4000 行/各格式 50 页/X 轴 100/库 100000 行，p444）、purge 默认（PTP 4 天/计费 15 天/taxa 2 天/100 告警 100 事件，p489-493）、许可（8770Clients ≤30、Security 键 0-5、N-1 版本 15/16，p601-608）、硬件双档（p55-56）、客户端底线（4GB/750MB，p93）、告警六级色标（p274）、MMP 口径（20 OXE/100 并发，p268）、日志 2x5MB（p548）——全部与原文逐格一致。
