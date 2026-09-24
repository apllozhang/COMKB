# coverage-audit.md — 任务覆盖审计（阶段 1.5 产出）

> 基准: BOOK_OVERVIEW.md 原书关键任务清单 task-01 ~ task-26（26 项）
> 审计对象: verified.md 34 单元 + references.md 外部参考 + GLOSSARY 60 术语
> 结论: **26/26 全覆盖，无缺口**；三处生产化数值为书外指针（诚实外置，不算缺口）；task-01 由环境口径承接（教学基础设施，不入能力卡）

## 任务 × 验证单元映射

| task | 任务 | 验证单元 | 证据素材（principle/case/counter） | 覆盖判定 |
|---|---|---|---|---|
| task-01 | 连接远程实验室并操作客户端 | （reference f02, f03） | p41, n49-n52 | ✅ 环境口径承接：仅 Boundary 背景（references.md 第 4 节 + book/overview 环境区），不独立成卡 |
| task-02 | 经五类通道登录交换机 | f05, f07, f08 | p05, p07, p08, c01, n38, n39 | ✅ |
| task-03 | 本地用户/密码策略/外部认证服务器 | f06 | p01-p04, p14, n01 | ✅ RADIUS 服务器侧配置为书外指针（p472 默认参数已入册） |
| task-04 | 加固交换机管理面 | f07 | p09, p05, n02 | ✅ MFA 细节为书外 Application Note 指针（p89） |
| task-05 | WebView 远程管理与验证 | f08 | p08, c01, n38, n39 | ✅ |
| task-06 | Lightning Config 快速开局 | f09, f10 | p10, c17, n03-n07 | ✅ |
| task-07 | 闪存目录/保存/认证/回滚 | f11, f12, f13 | p11-p13, c02, n08-n12 | ✅ |
| task-08 | 组建与维护 Virtual Chassis | f14-f18 | p15-p17, c03, n13, n14 | ✅ |
| task-09 | 静态/动态 VLAN 与 802.1Q | f19, f20 | p37, p38, p42, c04, c07, n15, n17 | ✅ |
| task-10 | VLAN 间路由与 IP 接口 | f21, f37 | p39, p40, p22, c04, c13, n16 | ✅ |
| task-11 | OST 使用 | f22 | p33, c18, n47 | ✅（使用为讲义级，安装实验 c18 在 task-26） |
| task-12 | 诊断八件套排障 | f23 | p34, p35, p44, c05, n40-n42, n55 | ✅ 规格上限为 Specification Guide 指针 |
| task-13 | 链路聚合并验证冗余 | f24 | p36, c06, n23, n44-n46 | ✅ |
| task-14 | STP 并做 1x1 负载分担 | f25 | p18, p19, c08, n18-n20, n54 | ✅ 思考题留白见 needs-review nr-05 |
| task-15 | DHL Active-Active | f26 | p20, c09, n21, n22 | ✅ |
| task-16 | DHCP Client/Relay 与 UDP Relay | f37 | p21, p22, c10, n43, n53 | ✅ |
| task-17 | VRRP 网关冗余 | f35 | p23, c11, n24 | ✅ |
| task-18 | QoS（含 auto-QoS/PBR/镜像） | f34 | p24, p25, p43, c12, n25-n27 | ✅ 队列模型随型号差异查规格 |
| task-19 | ACL 与用户口安全 | f36 | p26, c13, c14, n27, n28, n53 | ✅ |
| task-20 | Access Guardian（UNP+RADIUS） | f27 | p27, p14, p42, c15, n29 | ✅ RADIUS 服务器侧在书外（p472 默认参数已入册） |
| task-21 | LLDP/LLDP-MED 语音接入 | f28 | p28, c16, n30, n31 | ✅ 两页数值不一致转 nr-02 |
| task-22 | 管理与监控 PoE | f29 | p29, p30, n32, n33, n48 | ✅ 每型号预算为 datasheet 指针 |
| task-23 | 升级软件镜像 | f30 | p31, n34, n35, n55 | ✅ 升级步骤为 Release Notes 指针（原书明示不覆盖） |
| task-24 | Auto-Fabric 零触开局 | f31 | p32, n36, n37 | ✅ vcboot.cfg 模板设计依赖架构师输入（书外） |
| task-25 | Fleet Supervision 开通 | f32 | g20, g57 | ✅ 结构+入口+三路声明齐全；原书无警示框（如实留白） |
| task-26 | 安装 OST 2.0 并纳管 | f33 | p33, c18, n47 | ✅ |

## 覆盖质量说明

1. **无孤儿单元**：34 个 verified 单元全部映射到至少一个任务；f01（课程主线）作为全局底座映射到全部任务的认知前提，f10（示例拓扑）作为 task-06/组网类的防环红线素材。
2. **三处诚实外置**（不算缺口，属原书边界）：
   - 型号相关规格（镜像会话数、PoE 预算、VC 上限全矩阵、会话数演进）——原书一律回指 Specification Guide/datasheet（candidates 已在 conditions 标注）。
   - 升级操作步骤——原书 p533 明示"不在本教材内"，指向 AOS Release Notes。
   - RADIUS 服务器侧配置与 vcboot.cfg 模板设计——书外依赖（实验直接用现成 AAA Training Server）。
3. **无实验的概念章**（task-03/04/22/23/24/25）由框架+原则+反例三类条目共同覆盖，案例类天然为空——与 case-extractor 自检结论一致（15/26 任务有 How-To 直接覆盖），属书的结构而非提取遗漏。
4. **task-01 特殊处理**：R-Lab 属教学专用基础设施，BOOK_OVERVIEW 明示"不适合 skill 化"；其环境值（地址/账号/POD 规则）只落位 references.md 第 4 节与 book/overview 环境区，作全部实验类卡片的 Boundary 背景。
5. **数字口径终审**：会话上限表（6/4/8/4/20/50）、console 速率分代表、密码四要素（≥8 位四类字符避 ！$）、备份三文件/10 个 tar 上限、VC 选举四级序与 0-255 优先级、UNP 九规则优先序、802.1Q 4096 tag/8 优先级、STP 收敛三值与路径成本两套、DHL 1 会话 2 链/0-600 秒（默认 30 秒）、DHCP 中继 max hops 16/Opt82 Base MAC、VRRP 224.0.0.18 与 MAC 模板与默认优先级 100、QoS 默认五口径、auto-QoS 四 MAC 段/优先级 5、日志 1250KB/8 文件/归档 40/syslog 12、镜像 2→4 与抓包 1 会话 64KB、LLDP 30 秒/TTL 倍乘 4、PoE 四档逐格、RCL 6 次/BVLAN 4000-4015、OST 100/4000/5——全部与原文逐格一致。
