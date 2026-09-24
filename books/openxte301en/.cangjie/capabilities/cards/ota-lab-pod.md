# RLAB 实验 POD 与 SIP 运营商模拟器（实验环境底座）

## R — 原文依据

> "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data center."（p5）
> "Pods are independent of each other • Pods have the same configuration • Pods have access to common resources"（p5）
> "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... ITSP1 Public gateway public.itsp1.com 10.20.30.50"（p20）

出处：OPENXTE301EN p3-30。

## I — 自述

全书实验的运行底座，纯教学基础设施：

1. **POD 结构**：POD 1..n 相互独立、配置相同；公共资源区（10.20.30.x）放 NAS 与 SIP 模拟器；两种形态——全虚拟化（RLAB 专用）与混合课堂模式（加 MIX484 GD4、ALE-300 系话机、POE 交换机等实机）
2. **八台虚机**（192.168.1.x 网段，实验口径）：OXE（csa/csm）、OMS（.13）、OpenTouch/OTMS（.50）、8770 网管（.70）、DCS 虚机（.31）、ECOSYSTEM（.100，承载 CA/AD/Exchange）、PC Client 10/11（.10/.11）；内部 DNS 192.168.1.254
3. **ITSP1 模拟器**：SIP 网关 gateway1.itsp1.com（PBX 注册账号 pbxP/alcatel，域 sip.itsp1.fr）与公网网关 public.itsp1.com（MicroSIP 模拟公网/紧急用户）；号码规则含两位 POD 号 PN（主号 3321PN12345、移动 3361/3371PN12345、紧急 112/15/17/18）
4. **OXE 侧对接**：外部 SIP 网关 Registration ID/Outgoing username=pbxN；DID 翻译 First external=33210N41000、First internal=31000、范围 500
5. **实验人物**：Barkley 31000 / Backman 31001 / Boop 31002（IPDSP 软话机 TFTP 指向 OXE CS Main）

## A1 — 书中案例

**Pod 配置核对实验**（p24-30）：

1. RLAB 门户启动全部虚机，确认预置项（许可/FlexLM/机架板卡/用户/语音引导/SIP 中继组）
2. 机架核对（仅需 OMS）：Software Rack 3U、Rack N°4、Virtual GD4 192.168.1.13
3. 用户/IPDSP 核对：31000/31001 装 PC Client 10/11，TFTP=192.168.1.3
4. 混合模式特例：把 31000/31001 的 IP-Softphone Emulation 改 No 并选实际话机类型
5. 外部 SIP 网关填 pbxN（N=POD 号）
6. DID 翻译建 33210N41000 对 31000（范围 500）
7. 外呼验证：确认公网 SIP 载体可达

## A2 — 未来触发

使用情境：搭建/核对培训或测试环境；解读书中一切实验值（IP/账号/号码）；区分"实验口径"与生产配置；模拟运营商联调。

语言信号：RLAB / POD / 实验环境 / ITSP1 / 模拟器 / pbxN / pbxP / 3321PN / DID 翻译 / MicroSIP / IPDSP / 192.168.1.x / 10.20.30.x / letacla / superuser。

与相邻能力区分：生产远程通道（真实 DMZ/SBC/运营商）→ 远程接入能力；本卡只覆盖教学环境与模拟器。

## E — 可执行步骤

输入契约：POD 号（决定 pbxN 与号码段）、RLAB 门户账号、虚机清单。

1. 启动虚机并核对七项预置状态。完成标准：预置项全部就位
2. 核对机架/IPDSP/用户（混合模式改设备类型）。完成标准：话机注册成功
3. 对接模拟器：pbxN+DID 翻译。完成标准：外呼测试通过
4. 引用纪律：书中一切实验值只用于实验复现，生产引用必须替换。完成标准：文档无实验值泄漏

判停点：

- 生产项目里出现 letacla/superuser/pbxN 类值 → 停，这是实验口径，必须替换并纳入安全基线（n49）
- 模拟器行为当真实验证 → 模拟器与真实运营商有差异，生产前用真实中继复测
- ITSP2 → 仅在拓扑图出现无细节，别引用

输出契约：POD 核对清单（七项预置+机架+用户+DID）+ 内外互通测试结论 + 实验口径备忘。

## B — 边界

- 教学专用基础设施：不入生产方案；BOOK_OVERVIEW 明确"仅作 Boundary 背景与实验口径引用"
- OXE 地址 p9 印作 192.16.8.1.1/.3 为原文排版异常（nr-04），同表其余均为 192.168.1.x
- 明文密码（letacla/superuser/1234/training 等）为 2019 年培训文化产物，禁入生产（n49）
- 混合模式的课堂硬件清单（MIX484 GD4/ALE-300 系/POE）仅教学语境（p11-18）
