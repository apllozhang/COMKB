# OmniVista 8770 许可管理（锁结构 / 查询 / 更新 / 受限模式）

## R — 原文依据

> "1 - The Actis application generates the 8770 license file (.sw8770 extension) ... 4 - The service 'NMC License Server' is responsible for controlling the license file integrity"（p597）
> "[Modules] Application locks. A key value > 0 means the application is enabled. ... 8770Clients key is the maximum number of simultaneous clients (up to 30)"（p603）
> "Only the N-1 license is supported in the N release"（p602）
> "When some license thresholds are exceeded, client runs in restricted mode: Only Directory and Configuration are accessible"（p606）
> "Rename the nmc.license file into nmc.license.old, Paste the new license file and rename it to nmc.license"（p615）

出处：8770XTE200EN p594-617（8770 LICENSE 讲义与 How-To）。

## I — 自述

许可是"锁 + 数"：锁决定应用可见性，数决定容量，超限进受限模式。

**许可链五环**

- ACTIS 出证生成 <offer id>.sw8770 > 安装时提供 > 存 8770\etc 改名 nmc.license > NMC License Server 校验完整性 > 8770 客户端按锁显示应用

**文件结构四段**

| 段 | 内容 |
|---|---|
| [8770] | 版本与签名 |
| [ALIZE] | OXO 配置授权 |
| [OXE AND ICE] | OXE 配置授权 + 8770Handle（申报节点标识） |
| [Modules] | 应用锁：布尔键（Topology/AccountingMonitoring/Audit/Security/ExternalDirectorySynchro，1=启用）+ 用户数键（Configuration/Alarms/Accounting/Directory/Performance 等）+ 8770Clients（并发客户端上限 30）+ Security 键 0-5（安全流/Radius/PKI 组合档位） |

**锁的两种控制方法**

1. 申报节点锁：许可 [OXE AND ICE] 段 8770Handle 与指定 OXE OPS 文件中的 Handle 比对（OXE 侧 spadmin 命令显示），License Server 周期核验申报节点在位
2. 服务器特征绑定：MAC/IP/ProductID/UUID（支持冗余双机的 Redundant 字段）

**包型与选项**

- Start Pack PPU：Alarms/计量跟踪/统一管理，Configuration 与 Audit 内含（界面不显）；可选 AD Integration、Manage My Phone、API Provisioning、Topology、SNMP Proxy
- Full Pack PPU：Start Pack 全量 + Performance + Company Directory；任一包可加 Ticket Collector、Security、Multi Domain（依赖 Company Directory）
- OXO Connect 计费锁：默认无 ticket，按 1000 步进扩容、上限 30000；告警与 OMC 无锁

**版本与超限**

- 版本规则：只支持 N-1——R5.2 接受许可版本 15 或 16；Security 键中的 PKI 档位从 R5.0 起不再可用
- 超限行为：用户数逼近上限先产生告警；超限后进受限模式——仅 Directory 与 Configuration 可用（用于删户降回限内），服务器不停机防数据丢失

**查询与更新**

- 查询三口：客户端 Help > About；记事本开 C:\8770\etc\nmc.license 看各段锁值；OXE 侧 Telnet/SSH mtcl 会话跑 spadmin（Display current counters）看 Handle 与各锁计数
- 更新五步：Service Manager 停 NMC Service Manager > nmc.license 改名 .old > 新文件放入改名 nmc.license > 启动服务 > 客户端 Help > About 核对新锁
- 用量审计：NMCLicServer_1.log 打印各模块 "x/上限 = 百分比 (status=ok)"

## A1 — 书中案例

**许可查询与更新实验**（p610-617）：

1. 客户端 Help > About 看锁与容量
2. 记事本打开 nmc.license 核对 [ALIZE]、[OXE AND ICE]（8770Handle）与 [Modules] 全部锁值
3. OXE 侧 spadmin 输出 Handle（示例 Handle 4760=123456AB，实验口径）与各锁计数
4. 停 NMC Service Manager，旧许可改名 .old，放入新许可改名 nmc.license
5. 重启服务后 About 核对新锁生效（实验验证 Directory 锁）
6. 查 NMCLicServer_1.log 各模块用量百分比（示例 unifiedusermanagement 15/250=6%）

## A2 — 未来触发

使用情境：扩容加订用户数；续费换许可文件；新应用（Topology/SNMP Proxy）解锁；"应用集体消失"排障；换机后许可重绑。

语言信号：nmc.license / sw8770 / ACTIS / 8770Handle / spadmin / Modules / 8770Clients / Security 键 / 受限模式 / restricted mode / Start Pack / Full Pack / NMC License Server / 用量百分比。

与相邻能力区分：装机时的许可文件校验（平台安装能力）；超限删户操作走 Directory/Configuration（用户开通能力）；本能力管许可生命周期与超限判读。

## E — 可执行步骤

输入契约：ACTIS 出具的新许可文件（版本符合 N-1 规则）、维护窗口（更新期停 NMC Service Manager）、扩容需求清单。

1. 现状盘点：About + nmc.license + spadmin 三口对照。完成标准：锁值、用量、Handle 三处一致
2. 用量审计：读 NMCLicServer_1.log 各模块百分比。完成标准：识别逼近上限的模块
3. 扩容申请：按包型与选项下单（版本 15/16 规则）。完成标准：新 .sw8770 到手且版本合规
4. 更新执行五步（停服务 > .old > 换文件 > 启动 > About 核验）。完成标准：新锁生效
5. 超限应急：确认受限模式（仅 Directory+Configuration 可用）> 删户降回限内。完成标准：应用恢复
6. 换机重绑：按控制方法确认（申报节点或服务器特征/冗余字段）。完成标准：License Server 核验通过
7. OXO 计费扩容：按 1000 步进申请 ticket。完成标准：计费数据出现

判停点：

- 许可版本超出 N-1（如 R5.2 收到版本 14 及以下）→ 判停退回重出证，不要强行导入
- 超限时误判为故障重启 → 重启无效且丢排障时间；先读 NMCLicServer_1.log
- PKI 档位需求 → R5.0 起不再可用，按 Security 键现实档位沟通，不承诺旧功能
- spadmin 显示的 Handle 与许可不符 → 查申报节点是否变更，走重出证而非改文件

输出契约：锁值盘点表 + 用量百分比快照 + 更新记录（.old 归档）+ 扩容/受限处置报告。

## B — 边界

- 新许可文件只能由 ALE 侧 ACTIS 出具；现场无出证能力，只有换装动作
- 受限模式是产品保护行为：仅 Directory+Configuration 可用、服务器不停机——不是故障，重启无效
- 8770Clients 并发上限 30 是并发客户端数，与用户数键是两类口径，扩容前先分清
- 实验许可为 Training Purpose 且 Handle 示例（123456AB）为实验口径；生产锁值以客户合同为准
- 高可用冗余字段（Redundant 特征）只支撑许可绑定，不构成双机方案（备份恢复卡边界）
