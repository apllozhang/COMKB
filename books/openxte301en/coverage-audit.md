# coverage-audit.md — 任务覆盖审计（阶段 1.5 产出）

> 基准: BOOK_OVERVIEW.md 原书关键任务清单 task-01 ~ task-24（24 项）
> 审计对象: verified.md 18 单元（verified）+ 2 单元（reference）+ references.md 外部参考 + GLOSSARY 58 术语
> 结论: **24/24 全覆盖，无缺口**；容量算例与非法国号码计划为原书结构性缺位（诚实外置，不算提取缺口）

## 任务 × 验证单元映射

| task | 任务 | 验证单元 | 证据素材（principle/case/counter） | 覆盖判定 |
|---|---|---|---|---|
| task-01 | 搭建并核对实验 POD | f02(reference), f01 | p06, c01, n49, g52 | ✅ 结构与核对步骤齐备；IP/账号为实验口径 |
| task-02 | ITSP1 模拟器联调 | f03(reference) | p07, c01（步骤 5-7）, g37 | ✅ 模拟器无独立 How-To，验证动作并入 c01 |
| task-03 | Nomadic 蜂窝模式 | f04, f05 | p01, p03, c02, n01, n03, n05 | ✅ |
| task-04 | Nomadic VoIP 模式 | f04, f05 | p01, p02, p03, c03, n02 | ✅ |
| task-05 | Nomadic 资源验证维护 | f05 | p47, c04, n05, g57 | ✅（option 47 缺项见 nr-02） |
| task-06 | Desksharing 配置 | f06 | p04, p05, c05, n07 | ✅ |
| task-07 | Desksharing OTC PC 与维护 | f06 | p03, p04, c06, n04, n06 | ✅ |
| task-08 | 反向代理与 OTSBC 声明 | f09 | p14, c07, n49 | ✅ |
| task-09 | DAS 规则与 ACS FQDN/证书 | f10, f15 | p37, p43, p44, c08, n08-n11, n45 | ✅ |
| task-10 | OXE 通用参数 | f07 | p09, p10, c09（步骤 1-7）, n12-n14 | ✅ |
| task-11 | iPhone+ SBC 与 OT 侧基座 | f08 | p12, p13, p08, c09（步骤 8-9）, n50 | ✅ |
| task-12 | 设备档案与用户配置 | f07 | p11, c10, n43 | ✅ R2.6 单设备特例入册 |
| task-13 | 自动对象核验与手工补充 | f07 | p11, p08, c11, n15 | ✅ |
| task-14 | Extended Mobility 部署 | （f04 移动性语境） | p41, p42, c12, n16, n17, n41, g55 | ✅ 机制薄、语法/行为全在 principle+case（书结构使然） |
| task-15 | UM (Exchange) 部署 | f11 | p30-p32, c13, n20, n21 | ✅ |
| task-16 | 邮箱权限/云上下文/UM 维护 | f11 | p30, p31, p33, c14, n18, n19, n22, n23, n44 | ✅ |
| task-17 | 目录搜索部署 | f12 | p20, p21, c15（步骤 1-4）, n24, n25 | ✅ |
| task-18 | SBC 合并与 UDAS 维护 | f12 | p22, p23, c15（步骤 5-10）, n42 | ✅ LDAP 20 vs 5 见 nr-01 |
| task-19 | 会议服务器配置 | f13, f14, f15 | p38-p40, p43, c16 | ✅ |
| task-20 | 数据会议运用与协作限制 | f13, f16 | p15-p17, p34, p40, c17, n26-n29, n48 | ✅ |
| task-21 | DCS 安装与声明 | f17 | p35, p36, c18, n30, n31 | ✅ |
| task-22 | Calendar presence/synchro | f18 | p18, p19, p46, c19, n32-n34, n46 | ✅ |
| task-23 | 外部认证 LDAP/RADIUS | f19 | p24-p26, p29, c20, c22, n35, n36, n40, n42, n47 | ✅ |
| task-24 | Kerberos SSO 与 WBM 管理 | f19, f20 | p27, p28, c21, n37-n39, g40 | ✅ |

## 覆盖质量说明

1. **无孤儿单元**：18 个 verified 单元全部映射到至少一个任务；f01（课程主线）作为 24 项任务的组织轴；f02/f03（reference）经 ota-lab-pod 路由卡承接 task-01/02 的背景引用。
2. **两处原书结构性缺位**（诚实外置，不算缺口）：
   - 容量规划只有"按并发规划"一句话（Ghost Z 池、SIP 设备池、会议端口、DCS 吞吐均无算例）——p01 给出公式与规划输入，算例需现场按客户话务补做。
   - 号码计划（DAS/ARS/DID）仅法国口径（+33/00/0）——非法国交付需自行推导正则，p43/p44 只提供方法范式。
3. **版本碎片化提示**：R2.0/R2.1 MD1/R2.2/R2.3/R2.3.1/R2.5/R2.6 各章各提版本前提（R2.6 单设备化、R2.3.1 APNS/日历在场、R2.0 DAS 规则 7/8、R2.1 MD1 Extended Mobility 等），跨版本交付逐章核对，见 needs-review nr-07。
4. **数字口径终审**：端口总表（RP 443/8016、OTSBC 5261/8061、RTP 7000-7499、ACS 5060/5260、iPhone+ 5265、APNS 5223/2195/2196/443）、Ghost Z 定量（蜂窝 1、VoIP 1+1）、实验池（31017-31019/31951-31952）、Desksharing（600/601、虚拟 MAC aa:bb 规则、6004）、DISA 31280、秘密码 2998、速拨范围非 0 非满、Gmail 500、会议 7 位双码、DTMF 六码、OOO>Busy>Tentative>Working Elsewhere>Free、period≥1/merge period≠0、merge keys ≥2、RADIUS 1812/1813——全部与原文逐格一致。
