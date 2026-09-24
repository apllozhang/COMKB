# coverage-audit.md — 任务覆盖审计（阶段 1.5 产出）

> 基准: BOOK_OVERVIEW.md 原书关键任务清单 task-01 ~ task-18（18 项）
> 审计对象: verified.md 26 个 verified 单元 + 2 个 reference 单元 + references.md 外部参考 + glossary 56 术语
> 结论: **18/18 全覆盖，无缺口**；容量/话务设计、spatial redundancy 操作、SBC 安装、UM/Nomadic/OTBE 为书外指针（诚实外置，不算缺口）

## 任务 × 验证单元映射

| task | 任务 | 验证单元 | 证据素材（principle/case/counter） | 覆盖判定 |
|---|---|---|---|---|
| task-01 | 搭建并初始化实验/演示 POD | f04, f05（reference） | p43, c01, n09, n42 | ✅ 结构与模拟器口径；实验值仅 Boundary 背景 |
| task-02 | 用 SOT 以 hosted 模式部署 OTMS 虚机 | f06, f07, f08 | p03, p45, c02, n10 | ✅ |
| task-03 | 把 OVF/OVA 虚机手动导入 ESXi | f08 | p03, c03, n11 | ✅ vSphere client 仅 ESXi ≤6.0 已标 |
| task-04 | 完成 OTMS Post-installation wizard | f09 | p04, p05, p06, c04, c05, n02, n03, n05, n06 | ✅ 两模式十节全覆盖 |
| task-05 | 建立系统连接与 SUSE 基本操作 | f10 | p43, c06, c07, n08, n09 | ✅ 三通道 + 账号总表 |
| task-06 | 安装许可文件（.ice/.swk/.sw8770） | f11 | p07, p08, c04（步骤 8）, c09（步骤 5） | ✅ 手动装许可并入向导/外部 FlexLM 两章，无独立 How-To（书结构如此） |
| task-07 | 核查许可与排障 | f11 | p09, p10, p11, c08, n12, n13 | ✅ spadmin 三计数判据逐格核对 |
| task-08 | 部署外部 FlexLM 并从内部切换 | f11 | p12, p13, c09, c10, n14, n15 | ✅ |
| task-09 | 在 8770 中声明 OXE 并同步 | f12 | p14, p15, c11, n16 | ✅ 节点号公式与 APPLY 规则齐 |
| task-10 | 在 8770 中声明 OpenTouch 并互挂 | f13 | p16, p17, c12, n04 | ✅ bics.conf 四参数对应齐 |
| task-11 | 配置 OXE SIP | f14 | p19, p44, c14, n17 | ✅ 五段字段值齐；spatial redundancy 外置 TC1652 |
| task-12 | 完成 prior management | f15 | p20-p26, c15, n18, n19, n20, n21 | ✅ 六块全覆盖 |
| task-13 | 配置 OT→8770 告警对接 | f16 | p18, c13, n42 | ✅ MIB 重载固定坑已入册 |
| task-14 | 创建档案与用户（含 WPC 批量） | f17, f18, f19 | p27, p28, p29, c16, c17, c18, n40 | ✅ |
| task-15 | 配置语音邮箱体系 | f20, f21, f22, f23, f24 | p30-p35, c19-c23, n23-n27 | ✅ 邮箱/档案/IMAP/通知/公告五件齐 |
| task-16 | 部署证书（自签/外部 CA） | f25 | p45, c24, c25, n07, n28, n29 | ✅ |
| task-17 | 交付客户端（OTC PC/多终端/监督组） | f26, f27 | p36, p37, p38, c26, c27, c28, n30-n34 | ✅ |
| task-18 | 运维闭环（维护/备份/rehosting） | f28 | p39-p42, c29, c30, n22, n35-n39 | ✅ TC2149 矩阵附录全文在书内 |

## 覆盖质量说明

1. **无孤儿单元**：26 个 verified 单元全部映射到至少一个任务；f01（课程主线）与 f02/f03（架构/虚拟化底座）作为全局认知前提映射到 task-01/task-02 的准备段。
2. **书外指针（诚实外置，不算缺口）**：

   - 容量与话务建模——原书仅给 5000 用户一条硬数字，sizing 指向 Delivery note / Features list / Product limits（n01）。
   - OXE spatial redundancy 的 SIP 与外部语音邮件网关操作——指向 TC1652（n17）。
   - SBC 与反向代理安装——指向 TC2257/TC2639（g41）。
   - UM 语音邮件、Nomadic、OTBE、VPN-less 会议地址——原书明确"另见专项培训/另一手册"（n39）。
   - rehosting 全量操作——以附录收录的 TC2149 ed.04 为唯一完整依据。

3. **task-06 许可安装的操作位置说明**：书内无独立"手动装许可"How-To 章，操作内容分散在向导实验（c04 步骤 8）与外部 FlexLM 实验（c09 步骤 5）；提取器已如实保留，不虚构独立章节。
4. **数字口径终审**：5000 用户、ESXi 6.5/7.0.x、Hyper-V 2016/2019、SLES 12 SP5、SOT 8CPU/16GB/500GB、端口 2570/5260/5040/27000/161/162/4448/8080、号段 31000-31499、业务号 31200/31250/31260、SIP proxy 用户 31700/31710、IMAP 1000/20000、公告 5 分钟与 A-law 8kHz、多终端 5 设备、监督 500 组/40 人/4000/6000 链、备份 00:01 周日全量、rehosting 约 25 分钟——全部与原文页码逐格一致，无 rejected。
