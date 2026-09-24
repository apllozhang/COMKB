# coverage-audit.md — 任务覆盖审计（阶段 1.5 产出）

> 基准: BOOK_OVERVIEW.md 原书关键任务清单 task-01 ~ task-24（24 项）
> 审计对象: verified.md 32 单元（+1 reference）+ references.md 外部参考 + GLOSSARY 70 术语
> 结论: **24/24 全覆盖，无缺口**；生产化数值（端口全集/带宽/合同/DID 登记）为书外指针（诚实外置，不算缺口）

## 任务 × 验证单元映射

| task | 任务 | 验证单元 | 证据素材（principle/case/counter） | 目标能力卡 | 覆盖判定 |
|---|---|---|---|---|---|
| task-01 | 网络前提核查 + Pilot 评估 | f01, f03, f10（端口段） | p04, p05, p27, n01, n02, n52 | hub-network-readiness（router） | ✅ 文档体系与工具入口；端口/带宽全集为书外文章指针（n01） |
| task-02 | 公司体系规划与创建 | f01, f02, f03, f04 | p01, p06, p09, p10, p11, p12, p19, p29, c01, n03, n05, n06, n09 | hub-company-voice-subscription | ✅ 合规/查重/可见性/认证/时区全覆盖 |
| task-03 | 管理员权责 + 目录/频道 | f04（背景） | p13, p14, p15, n04, n06, n07 | hub-company-voice-subscription | ✅ 权责矩阵与企业目录/频道规则齐备 |
| task-04 | Voice 订阅开通与分配 | f02, f04, f07 | p03, p16, p17, p18, p20, c01, c10, n08, n10 | hub-company-voice-subscription | ✅ 四档逻辑/8 行订阅表/两层流转/实验口径齐备 |
| task-05 | Cloud PBX 声明与配置 | f05, f06 | p20, p21, p22, p23, c02, n10, n11, n12 | hub-cloud-pbx-provisioning | ✅ 全书核心对象，前提与一二一约束逐格验证 |
| task-06 | 公网号码分配与主叫策略 | f04（步 4） | p24, c02, n13 | hub-cloud-pbx-provisioning | ✅ 分配面/主号规则/主叫 ID 两选 |
| task-07 | 流量控制与闭锁 | f06 | p25, c02（闭锁档核对） | hub-cloud-pbx-provisioning | ✅ 白黑名单三规则与国际格式 |
| task-08 | SIP trunk 商务模式与带宽 | f03, f06 | p26, p27, p04, n14 | hub-network-readiness（router）+ hub-cloud-pbx-provisioning | ✅ bundled/separated 与带宽四行表；合同/资费书外 |
| task-09 | 多站点规划（参数侧） | f30 | p28, n15, n16 | hub-multisite（router） | ✅ 站点参数四条与主叫收紧 |
| task-10 | 成员管理与话务配置 | f14, f15, f16, f17 | p37, p38, p39, p40, p11, p29, p53, c05, c06, n29-n34, n55 | hub-member-telephony | ✅ 五通道/七分区/例行程序/按键组/宽限/安全 |
| task-11 | ALE 话机部署（zero-touch） | f07, f08, f10 | p30, p31, p32, p33, c03, n17, n21, n22, n23 | hub-zero-touch-provisioning | ✅ 机制链路+红线三条+端口表+首装两线 |
| task-12 | 设备维护与日志 | f32（设备段） | p34, n24, n25, n26 | hub-device-maintenance | ✅ debug 15 分钟/2.14.22/24h 口径 |
| task-13 | Generic SIP 接入 | f09, f11 | p36, c13, n18, n19, n20 | hub-device-maintenance | ✅ 六限制+安全基线+立场与参考设备 |
| task-14 | DECT 部署 | f12, f13 | p35, c04, n27, n28 | hub-zero-touch-provisioning | ✅ 两档容量逐格+基站/终端双线 |
| task-15 | Hunt Group 与等待队列 | f18, f19, f20, f21, f22 | p41, c07, n36, n37 | hub-hunt-groups | ✅ 分发/队列/角色/bubble 全齐 |
| task-16 | Manager/Assistant 组 | f18, f23 | p42, c07, n38, n35 | hub-hunt-groups | ✅ 筛选边界与 DID 挂组级 |
| task-17 | 话务台与监督组 | f24 | p43, c10, n43, n35, n57 | hub-attendant-supervision | ✅ 订阅分级/5-30-5 规格/设备限制 |
| task-18 | 紧急号码与紧急组 | f25 | p44, c08, n39, n40, n41 | hub-hunt-groups | ✅ 两法创建/激活语义/定位责任链 |
| task-19 | 通话录音与归档 | f26 | p45, c07（组级录音档）, n42 | hub-hunt-groups | ✅ 2 个月/访问面/Exporter |
| task-20 | 欢迎服务全家桶 | f27, f28 | p46, p48, p19, c09, n44, n45, n49 | hub-welcome-service-ivr | ✅ 日历/欢迎服务/提示音/MoH |
| task-21 | IVR 配置 | f27, f29 | p47, c11, n46, n47, n57 | hub-welcome-service-ivr | ✅ 菜单树/两入口/提示音两模式 |
| task-22 | 多站点配置 | f30 | p28, p24, c12, n15, n16 | hub-multisite（router） | ✅ 实施四步与站点主号/MoH |
| task-23 | 分析体系运用 | f31 | p49, p50, p51, n50, n51 | hub-analytics（router） | ✅ CDR/仪表盘/MOS 三视角口径 |
| task-24 | 维护支持体系 | f32 | p52, n52, n53, n54, n56 | hub-maintenance-support（router） | ✅ 八件套+SR 认证前提 |

## 覆盖质量说明

1. **无孤儿单元**：32 个 verified 单元全部映射到至少一个任务；f01-f03（课程主线/产品线/全景）作为全局底座映射到 task-02 的认知前提；f33（reference）为实验环境背景，不作任务载体。
2. **三处诚实外置**（不算缺口，属原书边界）：
   - task-01/task-08 的端口全集、带宽、防火墙配置——原书仅给官方文章与 PDF 指针（Network Requirements，p37/p41），书内只有两张局部摘录（p90 带宽四行、p136 设备端口表），candidates 如实标注未编造（n01）。
   - task-08/task-06 的 trunk 合同、资费、号码携转、DID 地址登记——在 BP/运营商侧（p88/p229/n14/n41）。
   - task-13 的互操作测试——无官方认证计划，只有 8 款参考设备指南（p122/n20）。
3. **无实验的概念章**（task-01/03/07/08/09/12/19/23/24）由框架+原则+反例三类条目共同覆盖，案例类天然为空——与 case-extractor 自检结论一致，属书的结构而非提取遗漏。
4. **数字口径终审**：p67 订阅表 8 行、p136 端口表 6 行、p148-150 DECT 容量、p211-215 组参数（50 人/轮转 10 秒/队列 10-900 秒/FCFS 延迟 10 秒）、p224 监督 5/30/5、p231 录音 2 个月、p176 宽限 10 天、p263 素材 4MB/120 秒、p328 MOS 三阈值——全部与原文逐格一致；实验值（p29/p53）全部标注"实验口径"。
