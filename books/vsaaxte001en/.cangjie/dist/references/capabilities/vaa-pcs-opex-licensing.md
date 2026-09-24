# VAA PCS 同步与 OPEX/许可体系（远端站点、Purple On Demand、FlexLM 核查）

## R — 原文依据

> "sudo vaa conf pcs [IP@] • Main command to configure automatic synchronization of database from primary VAA to VAA PCS … sudo vaa db sendBackup [IP@] • Command … to send automatic backup file to configured target and restore it on remote server"（p303）
> "OPEX oriented license management mechanism based on Purple On Demand offer … VAA must be connected to a cloud connected OXE and be associated to only one subscription … License items values will be checked every night at midnight, whatever the working mode, CAPEX or OPEX"（p305）
> "The license file (.lic or .vaa) is linked to the MAC address of the VAA … You must find: • The FQDN • MAC address"（p274）
> "PCS VAA can be configured for local emergency purposes. Anyway, configuration will be lost once network failure is solved."（p301）

出处：VSAAXTE001EN p46, p49-51, p273-274, p300-305。

## I — 自述

三个特殊运行主题：

1. **PCS 支撑**：中心 VAA 与呼叫服务器建中继，配置周期性复制到各外围 PCS VAA；断网时 PCS VAA 激活、与本地 PCS 建中继接管本地呼叫；断网期间的本地应急配置在网络恢复后即丢失（别把应急态当新基线）
2. **PCS 同步实现**：vaa conf pcs [IP] 配置自动同步（核连接、建 SSH key、未设自动备份时定义每日备份名 Backup4PCS.sql.gz）

   - vaa db sendBackup [IP] 发备份并远端恢复（前提：自动备份已设、备份文件已生成、SSH key 已布）
   - 定时任务每天 01:00 起，多台 PCS 依次错开（第 1 台 01:00、第 2 台 01:01、第 3 台 01:02）
3. **OPEX（Purple On Demand）**：按用量许可池模式——VAA 须连云化 OXE 且只关联一个订阅；项目内声明的 VAA 端口在全部 VAA 应用间分摊，须在每台服务器上指定可用端口数；无论 CAPEX 还是 OPEX，许可项每晚午夜校验一次；空间冗余（跨数据中心 Slave）在 Purple On Demand 下不支持
4. **许可核查**：.lic/.vaa 绑定 MAC 且须含正确 FQDN（改主机名/换网卡即失效）

   - 安装目录 /etc/ale/aa-license-server，排障目录 /var/lib/ale/aa-license-server/（打开文件应能找到 FQDN 与 MAC）
   - FEATURE 项 AAIVR（IVR 功能）/AAPORTS（端口数）/ECCSTART/VAA_RELEASE 各带到期日；运行态 vaa services 输出三项一眼巡检

## A1 — 书中案例

**PCS 同步命令序列**（p300-305，讲义级流程）：

1. 在主 VAA 上执行 vaa conf pcs [PCS VAA 的 IP]
2. 命令核连接并生成 SSH key 到远端
3. 未设自动备份时定义每日备份名 Backup4PCS.sql.gz
4. 需要立即同步时执行 vaa db sendBackup [IP]
5. 前提核对：自动备份已配置、备份文件已生成、SSH key 已布
6. 确认 cron 任务：每天 01:00 起，多台 PCS 依次 +1 分钟错开
7. 断网演练：PCS 激活本地接管，可做应急配置
8. 网络恢复后核对：应急配置丢失，以中心配置为准

## A2 — 未来触发

使用情境：客户有远端分支要容灾；问 OPEX 按用量付费；许可安装后失效；换网卡/改主机名后许可报错；售前评估"OPEX + 异地容灾"组合；巡检许可端口余量。

语言信号：PCS / 远端站点 / 同步 / sendBackup / Backup4PCS / cron / OPEX / CAPEX / Purple On Demand / 订阅 / 许可池 / FlexLM / FEATURE / AAIVR / AAPORTS / VAA_RELEASE / MAC / FQDN / 许可失效。

与相邻能力区分：自动备份规则本身（不可关闭/NFS/容量）归维护能力；N+1 扩容结构归架构冗余能力；Slave 部署步骤归 HA 能力；许可失效导致的服务异常排查入口在维护能力。

## E — 可执行步骤

输入契约：站点拓扑（中心/分支数量）、商用模式（CAPEX 或 OPEX，含云化 OXE 与订阅前提）、许可文件与服务器 MAC/FQDN、变更窗口。

1. 模式判定：客户要按用量付费则核 OPEX 三前提（云化 OXE、单订阅、端口分摊确认）；同时要异地容灾则现场说明互斥。完成标准：模式决策落定
2. 许可就位：核对 .vaa/.lic 已装且 vaa services 三项与采购一致。完成标准：许可在期且数量正确
3. FQDN/MAC 登记：把两台（或 N 台）服务器的 FQDN 与 MAC 记入交付档案，作为未来换件/改名的约束。完成标准：档案可查
4. PCS 配置（如适用）：vaa conf pcs 建立同步关系，核对 SSH key 与备份名。完成标准：同步测试成功
5. 排程确认：cron 01:00 起、多台错开；sendBackup 三前提写进运维手册。完成标准：排程可观测
6. 应急演练：断网验证 PCS 接管，恢复后核对应急配置已按预期丢失。完成标准：演练记录归档

判停点：

- 客户坚持"OPEX + 跨数据中心冗余" → 停，互斥（n08），二选一或回 CAPEX，升级商务
- 要在 PCS 上长期保存应急配置 → 停，恢复即丢失是设计行为（n09），长期变更必须回中心做
- 许可失效且近期换过硬件/主机名 → 停，按 MAC/FQDN 绑定口径处理：恢复原标识或重新申请许可
- 客户把 N+1 当成容灾 → 停，N+1 是同 OXE 扩容结构（reference 故障期配置冻结），不是灾备（n06）

输出契约：商用模式决策记录 + 许可档案（FQDN/MAC/FEATURE 清单）+ PCS 同步与演练结论。

## B — 边界

- 实验口径：许可 5 端口 Release 11、PCS 备份名 Backup4PCS.sql.gz、01:00 排程——生产按现场调整
- PCS 全书未展开全称；multi-company 与 N+1 的配置细节外置 TBE083 与 OTEC-S 指南（n50）
- p274 的 .lic 样例 VAA_RELEASE 数值与运行态不一致（nr-04），核查以 vaa services 实际输出为准
- OPEX 每晚午夜校验的具体行为（超配时如何处置）书内未展开
- 教材场景为单 OXE + 双 VAA 最小闭环，多分支 PCS 大规模编排无实验
- 空间冗余的部署细节（第二数据中心 Slave）只有讲义，无实施步骤（f08 关联）
