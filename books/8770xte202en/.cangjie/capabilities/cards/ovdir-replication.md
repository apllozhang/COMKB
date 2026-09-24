# 目录复制主从部署（副本、协议、初始化、调度、恢复）

## R — 原文依据

> "Redundancy only available for the company directory, not for the OmniVista 8770 server"（p503）
> "Master Replica • It is a read-write database ... Consumer Replica • It is a read-only database ... refers write requests to the master replica via a referral"（p505）
> "FROM A MANAGEMENT POINT OF VIEW, IT'S STRONGLY RECOMMENDED TO MANAGE UPDATES ONLY FROM THE MASTER REPLICA"（p507）
> "One master server can have up to 4 slave servers • Only 5 replica (master or consumer) can be created in each OmniVista 8770 server"（p514）
> "Unavailability period > 7 days • All Data created in the master during the unavailability period are lost"（p515）

出处：8770XTE202EN p501-515, p517-535。

## I — 自述

目录复制提供公司目录数据冗余：主服务器建 Master replica（读写供体）+ Replication agreement（协议）+ Attribute set（属性集）；从服务器建 Consumer replica（只读，ID 固定 65535）。

- **数字口径表**（全部与原文逐格核对）：

| 项目 | 数值 |
|---|---|
| Consumer 副本 ID | 固定 65535（自动） |
| Master 副本 ID | 手工 1-65534 且不重复 |
| 主从比例 | 1 主最多 4 从 |
| 每台副本总数 | 最多 5 个（master 或 consumer） |
| 断联容忍 | 不超过 7 天自动补齐；超过 7 天断联期主侧新增数据丢失 |
| 实验调度 | 每日 5:00AM（Simple job，实验口径） |

- **机制**：Master 改动即时生效，Consumer 经调度复制后更新（不能实时）；Consumer 写请求经 referral 转发给 Master，但管理上强烈建议只在 Master 改——Consumer 本地改动复制后消失
- **前提 checklist**：双机同版本/同 OS 语言/同安装语言/双 Directory 许可/同公司名；网络号一致；UID 构造与 cost center 管理参数双机一致；Slave 关自动创建；主从 DNS/hosts 互解析
- **顺序硬约束**：建副本要求分支为空——先导 LDIF 再删分支；属性集建协议后不可改（要改只能删协议重建或改后 Initialize）；Initialize 先清空 Consumer 再全量拷贝；移除顺序 Consumer 先于 Master，且删副本会连带删目录分支

## A1 — 书中案例

**主从复制部署实验**（p517-535）：

1. 前置核查：双机版本/语言/许可/公司名一致，互 ping 计算机名与 FQDN 通
2. Slave 端 Replication configuration 建 Consumer：Country/France/数据库 FR，ID 自动 65535
3. Slave 运行 toolsOmniVista.exe 核对复制管理器密码（实验默认不动）
4. Slave 配 OXE：Automatic creation 禁用，UID 构造与主机一致
5. Master 导出 France 分支 LDIF 后删除该分支（副本要求分支为空）
6. Master 建 Master replica：副本 ID 填 1（1-65534 未占用）
7. Master 配协议：从机 Host:Port+复制管理器密码，属性集 Replicate all，启用协议
8. Master 导回第 5 步 LDIF 恢复分支数据
9. 选协议行 Initialize：Slave 端 Consumer 数据出现
10. Schedule 排每日 5:00AM（避开两机已有日/周任务），Scheduler 可查
11. 过程验证：Master 加 P1 从机未排程前没有；Scheduler 右键 Execute now 后更新
12. 移除演练：先删 Consumer 再删 Master；>7 天不一致按六步人工恢复流程走读

## A2 — 未来触发

使用情境：目录数据要做冗余；从机改了人第二天没了；从机断了一周多数据怎么补；属性集要加字段；主从复制能不能加密；这套是不是整机高可用；副本怎么安全拆除。

语言信号：replication / 复制 / Master replica / Consumer / slave / 从机 / referral / Replication agreement / Attribute set / Initialize / 65535 / 7 天 / Schedule / 5 点 / 断联 / 数据不一致 / LDIF 恢复 / toolsOmniVista。

与相邻能力区分：

- 单机数据备份恢复 → LDIF 工具能力
- OXE 数据同步 → OXE 注册能力
- 8770 服务器本身高可用 → 书外（见 Boundary）

## E — 可执行步骤

输入契约：主从两台 8770（同版本/同语言）、双 Directory 许可、DNS 或 hosts 互解析、维护窗口。前提 checklist 不过 → 判停先补齐。

1. 核前提：版本/语言/许可/公司名/网络号/UID 构造/cost center 参数逐项核对。完成标准：checklist 全绿
2. Slave 建 Consumer 副本（分支同名须先处理：导 LDIF 再删）。完成标准：副本 ID 65535 生成
3. Slave 核复制管理器密码（toolsOmniVista.exe 可单独设置，勿沿用弱口令）。完成标准：密码策略落实
4. Master 建 Master replica（ID 1-65534）。完成标准：副本建立
5. Master 配协议：从机地址端口、管理器密码、属性集、启用。完成标准：协议生效
6. 分支数据处理：非空分支先导 LDIF 删除，协议配好导回。完成标准：数据无损
7. Initialize 全量 + Schedule 排程（错峰两机维护窗口）。完成标准：从机数据完整且调度生效
8. 验证：Execute now 手动触发，核对 Master 新增出现在 Slave。完成标准：复制闭环

判停点：

- 属性集要改 → 删协议重建，或改后 Initialize 强制全量；不要试图直接改属性集（p529）
- 从机断联超 7 天 → 断联期主侧新增数据已丢，走六步人工恢复（导 LDIF、禁协议、删重建 Consumer、导 LDIF、启协议）
- 客户把这当整机高可用 → 纠偏：只冗余目录数据，8770 服务器本身无冗余（n34）
- 从机侧收到改数据请求 → 拒绝并引导到 Master：Consumer 改动复制后消失（n36）
- 拆除复制 → 先导 LDIF，再按 Consumer 到 Master 顺序删；删副本连带删分支（n39）

输出契约：主从复制体系（副本/协议/调度）+ 初始化与复制验证记录 + 运维纪律说明（Master-only 写入、7 天阈值）。

## B — 边界

- LDAPS 不被复制支持（nr-07）：复制流量明文，加密合规场景需网络层方案（书外）
- Address Book 不可复制（p514）：个人地址簿不在冗余面内
- 复制必须调度、不能实时（p505）：RPO=调度间隔，排程密度与窗口需与客户对齐
- 初始化与移除都伴随数据删除动作：操作前一律先导 LDIF 备份
- 数字口径（4 从/5 副本/7 天/65535）为 Ed40 印刷口径，升级后以官方文档复核
