# coverage-audit.md — 任务覆盖审计（阶段 1.5 产出）

> 基准: BOOK_OVERVIEW.md 原书关键任务清单 task-01 ~ task-20（20 项）
> 审计对象: verified.md 30 单元（29 verified + 1 reference）+ references.md 外部参考 + GLOSSARY 62 术语
> 结论: **20/20 全覆盖，无缺口**；一处任务（task-01）为实验环境背景（reference 口径），三处生产化数值为书外指针（诚实外置，不算缺口）

## 任务 × 验证单元映射

| task | 任务 | 验证单元 | 证据素材（principle/case/counter） | 覆盖判定 |
|---|---|---|---|---|
| task-01 | 搭建/接入 RLAB 类实验环境 | f02（reference） | p38, n13, g60 | ✅ 节点表全量在册，仅作 Boundary 背景（实验口径，生产不适用） |
| task-02 | 部署 SOT VM 并完成首连初始化 | f03, f05 | p02, p04, p05, c01, c09, n05, n06 | ✅ Standalone/Hosted 两条线全覆盖 |
| task-03 | 更新 SOT 并核对版本 | f07 | p03, c01 步骤 6, c09 步骤 6, n04 | ✅ zip+MD5、同主版本限制、命名规则齐备 |
| task-04 | 启用 Template Factory（标准/降级） | f03, f04 | p02, c06, n02, n03 | ✅ 标准前置 + 降级五步双路径 |
| task-05 | 向 SOT 传输媒体并配置加载项目 | f05, f06 | p37, p38, c02 步骤 3-7, g04 | ✅ 三库/格式/账号/Easy-Expert 字段全覆盖 |
| task-06 | 用 SOT 完成 CS3/CPU8 单版本全加载 | f08, f09 | p01, p37, c02, n07, n08, n13 | ✅ 时序+相位+加载后清单+密码规则 |
| task-07 | 多版本加载到 inactive 并切换 | f10, f11, f12 | p07, c03, n11, n12 | ✅ 分区结构、两分支、手工附录齐备 |
| task-08 | 安装静态与动态补丁 | f12, f13 | p06, p37, c04, n09, n10, n15 | ✅ 双场景+顺序律+downstat 收尾 |
| task-09 | 分发器模式（Easy Installation）加载 | f14 | p06, c05, n14, n15, n16 | ✅ /tmpd→Rload 全流程+清理误区 |
| task-10 | 决策虚拟化平台并确定许可路径 | f15 | p10, p11, n17, n18 | ✅ 平台×版本×许可矩阵逐格在册 |
| task-11 | 生成并加载 OXE VM | f15, f16 | p08, c07, c10, n18, n59 | ✅ KVM 模板线 + ESXi .ova 线 |
| task-12 | 加载 OMS 并在 OXE 声明 | f17 | p09, c08, c11, g10 | ✅ 规格/媒体/IPXE/omsconfig 全链 |
| task-13 | 用 SOT 加载 GAS 服务器 | f18 | p12, p14, p38, c12, n20, n22 | ✅ 硬件前置表+BIOS 取 MAC+PXE |
| task-14 | 执行 GAS 后安装向导 | f19 | p14, p36, c13, n24, n25, n26 | ✅ 六段向导+WebRTC 参数+FlexLM 附录 |
| task-15 | GAS 日常运维 | f18, f19 | p15, p16, c13 步骤 12-13, n21, n23, n27 | ✅ gasversion/gasbackup/host 升级/UPS |
| task-16 | 配置 DNS/代理并验证云连通性 | f20 | p17, c14, n36, n55 | ✅ netadmin 路径+checkCloudConfig 判据 |
| task-17 | 执行 FTR 并掌握 PIN 恢复 | f20, f21, f22 | p18, p19, p20, c15, n28, n29, n30, n32, n33 | ✅ 前提/执行/恢复/排障四层 |
| task-18 | 启用 RTR 并监控状态与事件 | f23, f24, f25 | p11, p21, p22, p23, p24, c15, n31, n34, n35 | ✅ 状态机+事件码+互斥规则（重试双口径转 nr-01） |
| task-19 | 从 MyPortal 下载 PoD 许可文件 | f30 | p28, c16, n53 | ✅ 路径+Active 判据+升级路径 |
| task-20 | 配置 PoD 并核查 OXE-LMS 同步 | f26, f27, f28, f29 | p27, p29-p34, p35, c17, n39-n58 | ✅ 架构/消耗/对账/panic/C2P 全域 |

## 覆盖质量说明

1. **无孤儿单元**：30 个验证单元全部映射到至少一个任务；f01（全书主线）作为全局底座映射到全部任务的认知前提（顺序基线）。
2. **一处 reference 口径**（不算缺口，属书的性质）：task-01 的 RLAB 节点表（f02/p38）是培训专用基础设施，BOOK_OVERVIEW 已判定"仅作 Boundary 背景"；节点 IP/账号/密码只进 book/overview 环境区，不生成能力卡。
3. **三处诚实外置**（原书明确指向书外文档，不算缺口）：

   - 虚拟化平台演进后的兼容性——原书矩阵为 Ed12 时点值，生产以 TBE043 为准（p10/n17/n18）
   - GAS 部署与 Rainbow 网关细节——TBE063/TC3138/TBE067（n19/n21/n59）
   - OXE 业务配置（用户/路由/编号计划）——原书压成一行"Perform basic management such as user creation… Or restore a backup"（n08/n59），指向 Starter 课程
4. **无实验的概念章**（task-01/10）由框架+原则+反例共同覆盖，案例类天然为空——与 case-extractor 自检结论一致（17 条 case 全部对应 How-To 实验章），属书的结构而非提取遗漏。
5. **数字口径终审**：SOT 前置 8CPU/16GB/500GB/50GB、补丁实验链 0→19→36（Linux 601.007/601.012/601.017）、N3 迁移 80GB/1GB/3.5GB、OXE 规格模板 500/3000/7000/15000、OMS 120 通道/240 台/会议 3-6-14-29 方、GAS 前置表四行（2 核 4GB/2 核 2.8GHz 6GB/3 核 2GHz 6GB/4 核 2.8GHz 8GB、360GB）、WebRTC 50 并发/7000 用户/12000 用户 +2GB、端口 443/80/53/27000/2222、KeepAlive 90 秒、CC-SUITE-ID 23 字符=20 hex、PIN 6 位/5 天、RTR 30 天/+0.5/-1 与 29-28/27-10/9-1/0、事件 6200-6214/647-651/652-654/5816、lock 431/87/165/384/385、目录 24 项与 3EY945xxAA 件号、1,500,000 用户/项目、阈值 0-2800/0-15000/0-1000、spadmin 计数 "15 | 0/0 | 18"——全部与原文逐格一致；唯一数值异常（p404 示例 5/5/25）已判为原文排版错误并转 nr-02。
