# Virtual Chassis 堆叠（选举、分裂防护、ISSU、配置与同步）

## R — 原文依据

> "Virtual Chassis = Group of switches which appears as a single router or bridge ... No STP/VRRP between Access and Core switches ... No license needed"（p152）
> "Master/Slave election based on virtual chassis protocol (ISIS-VC) Highest chassis priority value Longest chassis uptime (if difference in uptime >10 mn) Smallest Chassis ID value Smallest chassis MAC address"（p156）
> "2 mechanisms • Out of Band: EMP Remote Chassis Detection (RCD) • In Band: VC Split Protocol"（p160）
> "The Slaves are then reloaded from the ISSU directory in order from lowest to highest chassis ID"（p162）

出处：DT00XTE215EN p150-182。

## I — 自述

多台交换机经 VFL 互联呈现为一台逻辑交换机：单管理点、跨机箱冗余、成员间无需 STP/VRRP、免许可证，拓扑由私有协议 ISIS-VC 维护（p152/p155）。

1. **选举四级序**（p156）：最高 chassis 优先级（0-255）> 最长运行时长（差距须 >10 分钟才比较）> 最小 Chassis ID > 最小 MAC；MAC retention 恒开（接管后二层身份不变），原主恢复不触发新选举、不抢回主角色
2. **配置五步**：选 Auto-VC（无 vcsetup.cfg 自动建）或手动；每台唯一 Chassis ID；相同 Chassis Group 与优先级；配 VFL（vf-link-mode auto + auto-vf-link-port，或静态指定）；从含 vcsetup.cfg 的目录 reload
3. **同步语义**：write memory 只同步 RAM 到各成员 working；copy running certified 或 write memory flash-synchro 才完成 certified 级同步（Synchronizing chassis N）
4. **分裂防护双机制**（p160-161）：带外 RCD 经 EMP/管理网侦测（IP 取序：NVRAM 中 CMM 地址优先于机箱 EMP 地址），检出后原 slave 关闭全部前面板用户口、状态转 Split-Topology，VFL 恢复后重启回归 slave；带内 VCSP 需上游/下游 helper 交换机，VC 每成员建议一个口入 VCSP LAG
5. **ISSU 与跨成员访问**（p162-163）：新代码放 issu_dir 独立目录，slave 按 chassis ID 从低到高滚动重载；ssh-chassis admin@<id> 内部映射 127.10.<id>.65，提示符相同需看 Local Chassis 字段确认所在成员

**每型号 VC 规模上限**（p153-154）：

| 型号 | 上限 |
|---|---|
| OS6360 | 4（24/48 口机型）；8（10 口机型） |
| OS6465 | 4 |
| OS6560 / OS6865 / OS6860/E/N / OS6570M / OS6870 | 8 |
| OS6900 全系（部分/全网格） | 6 |
| OS9900 | 2（仅静态 VFL） |

## A1 — 书中案例

**两台 OS6360 组 VC 实验**（p173-182，How-To）：

1. show chassis 识别机型与 VFL 口：P10 用 1/1/11-12，P24 用 1/1/27-28（实验口径）
2. 6360-A 配 chassis-group 1 与 chassis-id 1、优先级 200，write memory 后 reload（约 4 分钟）
3. 6360-B 配 configured-chassis-id 2 与同 group，write memory 时出现"缺失 chassis 配置将清除"警告，确认 y 属设计行为
4. 两侧 vf-link-mode auto + auto-vf-link-port 指定合格口，enable 接口后等待 VC 成形
5. A 侧出现 "New Master: chassisId 1" 日志；B 侧重启约 5 分钟（实验口径）
6. show virtual-chassis topology 中 Chassis 2 带 "+" 后缀表示未保存，write memory flash-synchro 后消失
7. show virtual-chassis vf-link 看 Is Primary 主备口；consistency 核对 Type/Group/Hello/Control Vlan/License 全 OK
8. ssh-chassis admin@2 跨成员访问，以 Local Chassis 字段确认所在成员后 logout 返回
9. 收尾：关闭未用接口；WebView 打开 Chassis visualization 查看两机框

## A2 — 未来触发

使用情境：两台以上交换机合成一台管理；堆叠主备怎么选；VFL 口怎么选；堆叠分裂防双主；堆叠升级；跨成员 CLI 排障；堆叠配置保存不齐。

语言信号：Virtual Chassis / 堆叠 / VFL / ISIS-VC / chassis-id / chassis-group / 优先级 / 选举 / master / slave / 分裂 / split / RCD / VCSP / ISSU / ssh-chassis / flash-synchro。

与相邻能力区分：

- 保存命令本身的语义：配置生命周期能力卡
- 升级版本选型：升级与 Auto-Fabric 能力卡
- 成员间防环（无需 STP）与网络侧 STP：链路与生成树冗余能力卡

## E — 可执行步骤

输入契约：同族机型清单、角色规划（谁主谁备）、VFL 布线（合格口表）、分裂防护选型（EMP RCD 或 VCSP helper）。不同族混插需查混插规则与版本门槛。

1. 规划：按型号查规模上限与 Auto VFL 合格口表；分配全局唯一 Chassis ID、相同 Group、按角色定优先级（0-255）。完成标准：参数表成文
2. 逐台配置：chassis-group/chassis-id/configured-chassis-priority + VFL（auto 或静态），write memory 后 reload。完成标准：reload 后 show 参数为新值
3. 成形验证：show virtual-chassis topology 确认 Master/Slave 与拓扑；vf-link 状态 Up。完成标准：全部成员 Running
4. 同步固化：write memory flash-synchro 至 topology 无 "+" 后缀；consistency 核对强制一致项（Type/Group/Hello/Control Vlan/License）。完成标准：全 OK 且已同步
5. 分裂防护启用：EMP 规划 RCD 取址（NVRAM CMM 地址优先），或规划 helper 交换机与 VCSP LAG。完成标准：防护路径就绪
6. 升级路径：ISSU 用独立目录滚动重载（ID 从低到高）；跨成员运维用 ssh-chassis 并核对 Local Chassis。完成标准：升级与运维流程明确

判停点：

- 优先级或 chassis-id 改完 show 仍是旧值 → 属预期，必须 reload 才生效，不要当命令失败重复配置
- write memory 出现"缺失 chassis 配置将永久清除"警告 → 确认的是拓扑变化清理，盲目确认会清掉成员配置
- 平台不支持 RCD/VCSP → 查 p160-161 支持平台表，不在支持清单的分裂防护诉求判停
- OS9900 需求 auto VFL → 不支持（仅静态 VFL），改静态规划

输出契约：稳定运行的 VC（topology/consistency 全 OK）+ 分裂防护方案 + 同步与升级流程说明。

## B — 边界

- 优先级与 chassis-id 修改都必须 reload 生效；每次重启约 4-5 分钟（实验口径），排产要算窗口
- VC 成员间无 STP/VRRP——防环与网关冗余由 VC 单逻辑交换机属性承担，不要在成员间再配这两样
- RCD 支持平台：OS6870/OS6860E/N/OS6900/OS9900；VCSP 需 R8 支持平台与 helper 设备（p160-161）
- 6900-X48C4E 加入 VC 需 AOS 8.9R4 最低并配合 capability vfl-type 命令（p154）
- License 等级（A=Advanced/B=Data Center）是 VC 一致性强制项，混级会影响 chassis 状态（p180）
- Auto-VC 场景 Demo License 默认启用（p540）；正式部署需换成正式许可
