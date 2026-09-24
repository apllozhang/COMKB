# OXE 节点注册与同步（前置检查、三级声明、同步与核验）

## R — 原文依据

> "Use the siteid command to display network and node number. ... Node number : 1 ; Network number : 1"（p89）
> "Subnetwork – Node number Enter a numeric value equal to the OmniPCX Enterprise network*100 + OmniPCX Enterprise node number."（p95）
> "SSH connection Check the box to authorize SSH/SFTP connection • Host name Enter a unique ID for each secured OXE"（p96）
> "Log file C:\8770\log\ NMCSyncLdapPbx_1.log"（p98）
> "Date of last modification This field indicates the date and time of the last synchronization performed."（p98）

出处：8770XTE202EN p88-98。

## I — 自述

OXE 注册是目录一切数据的入口，四段交付链：

- **前置检查**：siteid 取网络号/节点号；netadmin -m 查 Role addressing 与当前配置（确认 SSH 开启）；防火墙信任列表必须收录所有与 Call Server 交互的主机（8770、OMS、客户端等，漏一台断一处）
- **三级声明**（Configuration 应用）：右键 nmc 建 Network（网络号）→ 其下建 Subnetwork（子网号必须等于 OXE 网络号）→ 其下建 OmniPCX 4400/Enterprise 节点
- **节点关键字段**：Subnetwork-Node number（拼装规则见下）；IP 地址；FTP Username=adfexc（取数）+ Software download 页签维护账户 mtcl；勾 Process configuration；Alarm reception mode 选 Permanent IP connectivity；勾 Directory Process；Connectivity 页签勾 SSH connection 并填唯一 Host name（8770 用 MindTerm 建 SSH 公钥）
- **同步与核验**：右键节点 Synchronization，Complete（不看上次日期全量）或 Partial（增量）× Separate（仅本 OXE）或 Global（含关联 OpenTouch）；成功后看日志 NMCSyncLdapPbx_1.log、生成 Users/Directory 分支、Data Collection 页签 Date of last modification 更新

节点号拼装（p95，含 nr-01 勘误说明）：

| 场景 | 网络号 | 节点号 | 填写值 |
|---|---|---|---|
| 书面示例 | 1 | 2 | 101（原文如此，按公式应为 102） |
| 实验实配 | 1 | 1 | 101 |

合理读法是"百位=网络号、末两位=节点号"（推断，见 needs-review nr-01）；实配以 siteid 真实输出拼装并现场验证。

## A1 — 书中案例

**OXE 节点注册实验**（p88-98）：

1. 收集 OXE 信息：主机 csa、主 IP 192.168.1.3、网络号 1、节点号 1（实验口径）
2. PuTTY SSH 连主 IP，siteid 核对 Node number=1、Network number=1
3. su - 后 netadmin -m 选 Role addressing 查看主 csm 地址（空间冗余时记两条）
4. netadmin -m 查当前配置确认 "Security with SSH: yes"，telnet 应为关闭
5. 防火墙 Restricted Access 里核对 8770（192.168.1.70）在信任列表
6. Configuration 应用右键 nmc 建 Network：Name=ale、Network number=1
7. ale 右键建 Subnetwork：Name=abc1、Subnetwork number=1（等于网络号）
8. abc1 右键建 OXE 节点：Name=oxe、Subnetwork-Node number=101、IP=192.168.1.3
9. 凭据填 adfexc/维护账户 mtcl（实验口径），勾 Process configuration 与 Directory Process
10. Alarm reception mode 选 Permanent IP connectivity，Connectivity 填唯一 Host name
11. 右键 oxe 执行 Synchronization > Complete > Separate，Status 页签 Apply 启动
12. 核验：成功消息 + NMCSyncLdapPbx_1.log + Date of last modification 更新

## A2 — 未来触发

使用情境：新 OXE 接入 8770 目录；节点声明字段怎么填；同步失败或没数据；SSH/信任列表连不上；同步模式选哪种；同步后目录没生成用户分支。

语言信号：OXE 注册 / node registration / siteid / netadmin / 网络号 / 节点号 / Subnetwork / adfexc / mtcl / Permanent IP connectivity / 同步日志 / Date of last modification。

与相邻能力区分：

- 注册后的自动建人与树结构 → 自动创建能力
- AD 侧数据接入 → MSAD/Azure 管道能力
- LDIF 批量导入 → LDIF 工具能力

## E — 可执行步骤

输入契约：OXE 的主 IP 与 SSH 可达、网络号/节点号（siteid 输出）、adfexc 与 mtcl 凭据（客户提供，实验口径值不可用）。凭据缺失 → 判停向客户索取。

1. 前置：siteid 核网络/节点号；netadmin 确认 SSH 开启；信任列表含 8770 地址。完成标准：三项检查通过
2. 建容器：Configuration 应用建 Network（网络号）→ 建 Subnetwork（子网号=网络号）。完成标准：两级容器就绪
3. 建节点：声明 OXE，节点号按"百位=网络号、末两位=节点号"拼装，IP/凭据/Process configuration 齐备。完成标准：字段完整保存
4. 事件通道：Alarm reception mode 选 Permanent IP connectivity，勾 Directory Process，Connectivity 配 SSH Host name。完成标准：自动创建前提就位
5. 同步：右键节点选同步模式（首选用 Complete > Separate）并 Apply。完成标准：同步成功消息出现
6. 核验：日志无致命错误、目录树生成 OXE 分支、Date of last modification 为本次时间。完成标准：三处证据齐

判停点：

- siteid 与客户给的号不一致 → 以 siteid 为准重新核对后再填，不硬填文档值
- 节点号按公式与书例得出不同值 → 按 nr-01 口径现场验证，并在交付记录注明推断
- 同步报 FTP/凭据错误 → 先查 adfexc 密码与网络可达，再查 8770 与 OXE 间防火墙信任列表
- 需要全局密码或生产凭据 → 停止使用教材值，转客户安全流程（实验口径红线）

输出契约：已注册可同步的 OXE 节点 + 前置检查记录 + 同步核验证据（日志与时间戳）。

## B — 边界

- 节点号拼装规则存在书内勘误（nr-01）：示例与公式矛盾，按推断读法操作并现场验证
- adfexc/mtcl 等凭据与 IP 全部为实验口径（nr-08），生产必须使用客户侧凭据管理流程
- 信任列表是持续要求：后续新增监控/集成服务器都要补录（n45），漏配表现为单点连不通
- 同步只把 OXE 数据取进配置目录；变成公司目录人员要靠自动创建或同步链路（自动创建能力域）
- OXE 侧 netadmin/siteid 的完整命令手册属 OXE 文档域，本卡只覆盖注册所需子集
