# 实验/交付前置环境（RLAB Pod、ITSP1 模拟器、组网迁移前置）

## R — 原文依据

> "Remote Lab allows accessing a pool of virtual and physical machines … Pods are independent of each other • Pods have the same configuration • Pods have access to common resources"（p5）
> "OXE CSB (ENTP_OXE_CSB) and PCS REMOTE (ENTP_PCS_REMOTE) will be started later to avoid IP address conflict."（p47）
> "Due to RLAB infrastructure and technology, 2 VMs (even if not started) can't have the same IP address."（p375）
> "PBX installation nb 3321PN … DDI table - First external nb 41000 … DDI table – First internal nb 31000"（p37）

出处：ENTPXTE401EN p5-54, p372-382。

## I — 自述

全书实验的承载底座（RLAB 教学专用，生产无此环节），用途是理解教材输出与搭建同构现场沙盘：

1. **双拓扑**：集中式 IP Pod（CSA/CSB+远端 Subnet 2，含 PCS REMOTE）与组网 Pod（NODE 1/NODE 2）；另有 Hybrid Mode 教室硬件变体（MIX484+实体话机）
2. **公共资源区**：NAS（软件/许可）、ITSP1 SIP 运营商模拟器、外部 DNS、邮件服务器——各 Pod 共享
3. **号码规则**：PN=两位 POD 号贯穿全部号码——PBX 注册 pbxN、Node 1 外号段 3321PN41000 起（DDI 41000-41499 ↔ 内部 31000-31499）、Node 2=3311PN41500/31500、公网模拟号 3321PN12345、紧急号 112/15/17/18
4. **启动顺序约束**：RLAB 不允许两台 VM（即使未开机）同 IP——CSB 与 PCS REMOTE 延后启动；组网实验前必须做 VM 网卡迁移（CSA 摘除 192.168.1.1、NODE 1 重建该地址）
5. **OXE 预配置基线**：许可/NTP/FlexLM/SSHv2 已声明、防火墙为"部分配置"教学口径、机架/板卡/用户/导引/中继已建（集中式 DHCP 开、组网 DHCP 关）

## A1 — 书中案例

**集中式 Pod 基线**（p46-54）：

1. 按 RLAB 清单仅启动所需 VM（CSB/PCS REMOTE 延后）
2. 核对机架板卡（主站 GD4 192.168.1.13、远端 GD4 192.168.2.13）
3. 装 IPDSP（TFTP Server Main=192.168.1.3）并注册 31000-31003
4. 外部 SIP 网关填 POD 参数（Registration ID=pbxN）
5. DID 翻译建 3321PN41000 ↔ 31000、Range 500
6. 外呼拨测验证公网通路

**组网 Pod 迁移与基线**（p372-382）：

1. CSA Remove Interface 释放 192.168.1.1
2. NODE 1 先 Remove 再 Create（Subnet1、192.168.1.1）
3. 硬重启 NODE 1，从 NODE 2 ping 验证
4. 核对双节点各自 SIP 网关（pbxN/remoteN）与 DID 段
5. 外呼与节点互拨验证（经 ITSP1）

## A2 — 未来触发

使用情境：搭建与教材同构的沙盘；读教材截图对不上号（POD 号差异）；实验 ping 不通（启动顺序/网卡归属）；培训环境与客户现场参数换算。

语言信号：RLAB / POD / pod number / ITSP1 / SIP carrier simulator / 3321 / 41000 / pbxN / remoteN / IPDSP / MicroSIP / VM 网卡 / Remove Interface / IP 冲突。

与相邻能力区分：一切 How-To 实验（冗余/PCS/域/组网等）都建在本卡基线之上；生产开局参数替换属各能力卡 Boundary。

## E — 可执行步骤

输入契约：RLAB 账号与 POD 号、实验清单（哪些 VM/物理机）。POD 号决定全部号码后缀，先确认再动手。

1. 确认 POD 号 PN 并按规则推算本 Pod 全部号码。完成标准：号码表就绪
2. 按拓扑启动 VM（注意 CSB/PCS REMOTE 延后；组网先做网卡迁移）。完成标准：ping 全通、无 IP 冲突
3. 核对预配置基线（许可/NTP/FlexLM/机架/用户/中继）。完成标准：与教材基线一致
4. 建外部 SIP 网关与 DID 翻译（填 PN 参数）。完成标准：注册成功
5. 拨测：出局、节点互拨、IPDSP 注册。完成标准：三类呼叫全通

判停点：

- 实验 ping 不通 → 先查启动顺序与 VM 网卡归属（IP 冲突是 RLAB 第一嫌疑），再查业务配置
- 截图号码与本 Pod 不符 → 换算 PN，不照抄教材具体值
- 想把实验口令/网段带到生产 → 停，全部为实验口径，必须替换

输出契约：可复现的实验基线（号码表+启动顺序+拨测记录）或同构现场沙盘。

## B — 边界

- 本卡是教学基础设施知识：生产交付没有 RLAB/ITSP1/网卡迁移这些概念（n01/n21/n47）
- 实验防火墙为部分配置口径——生产安全基线必须另行设计（p49）
- SIP 模拟器与生产 SIP 中继在安全/编解码/号码格式上有差异（p34-39 口径）
- 培训评估与证书流程（p537-543）不属于技术知识域
