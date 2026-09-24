# RLAB 实验环境与 Pod 配置（虚机基线、机架板卡、DID 翻译、外呼验证）

## R — 原文依据

> "Remote Lab allows accessing a pool of virtual machines and hardware (when required) hosted in a data center. … Pods are independent of each other … have access to common resources"（p5）
> "Registration ID pbxN (where N is your POD number) … Outgoing username pbxN"（p73-74）
> "To make sure that access to public SIP carrier is working properly, set up some outgoing calls."（p75）

出处：RAINXTE003EN p5-18, p70-76。

## I — 自述

RLAB 是培训专用远程实验室：POD 池相互独立、配置相同，公共资源区放 NAS（软件/许可）、SIP 运营商模拟器与外部 DNS。每 POD 6 台实例：OXE（csa/csm 双节点）、OMS、FlexLM 许可服务器、WebRTC 网关、两台 PC Client（装 IPDSP 与 MicroSIP）。

Pod 配置方法论六步（生产价值在方法不在取值）：

1. **基线核对**：Rlab 仪表盘确认 6 台虚机在跑；预配项（许可/DHCP/机架板卡/用户/公共 SIP trunk）逐项过
2. **主站设备核对**：软件机架与虚拟板卡参数对齐讲义表（机架号/槽位/IP）
3. **话机用户核对**：两部 IPDSP 分机与安装位置对应；IPDSP 网络页填 TFTP 服务器（OXE CS 主地址）
4. **外部 SIP 网关注册**：Registration ID 与外呼用户名按 POD 号填（模式 pbxN）
5. **DID 翻译对齐**：外部号码翻译表按 POD 号填首外部号/首内部号/范围大小
6. **外呼验证**：打几通外呼确认公网 SIP 载体正常；培训邮箱核收并清空旧信

SIP 模拟器角色（p13-18）：公共区扮演出局运营商——注册网关（PBX 注册账号）与公网网关（模拟公网/紧急号码用户）两条腿；号码规则含 POD 号变量；DDI 表把外部安装号映射到内部分机段。

## A1 — 书中案例

**Pod 配置实验**（p70-76）：

1. Rlab 仪表盘确认 OXE/OMS/FlexLM/WebRTC/两台 Client 共 6 台虚机在跑
2. 逐项核对预配基线：软件许可、FlexLM 声明、DHCP 池、机架板卡、话机用户、公共 SIP trunk
3. 核对软件机架与虚拟板卡参数（机架号 4、槽位 0、板卡 IP，实验口径）
4. 两部 IPDSP 分别装在两台 Client，网络页 TFTP 填 OXE CS 主地址
5. 外部 SIP 网关按 POD 号填 Registration ID 与外呼用户名（如 POD 3 填 pbx3）
6. DID 翻译按 POD 号填首外部号（33210N41000 模式）、首内部号 31000、范围 500
7. 做几通外呼验证公网载体；核收培训邮箱三账号并清理旧邮件

## A2 — 未来触发

使用情境：排 RLAB 实验课；自学搭基线；实验里外线打不通；分机外部号对不上；模拟器怎么扮演运营商。

语言信号：RLAB / Remote Lab / POD / 实验环境 / IPDSP / MicroSIP / ITSP / SIP 模拟器 / DID / DDI / 翻译表 / TFTP / pbxN / 基线核对。

与相邻能力区分：

- 基线就绪后的 DNS/代理与接入 → OXE 接入能力
- 生产站点的中继与号码规划 → 书外（客户拨号规范），本卡仅方法论
- 网关虚机部署 → 网关部署能力（RLAB 中镜像已预装）

## E — 可执行步骤

输入契约：POD 号、讲义基线表、培训邮箱清单、SIP 模拟器账号口径。虚机缺员或许可失效 → 判停找实验管理员，不自行改公共区。

1. 核虚机：6 台实例全部在跑。完成标准：仪表盘无离线
2. 核预配：许可/DHCP/机架/用户/trunk 五项过表。完成标准：与讲义基线一致
3. 配话机：IPDSP 的 TFTP 指向 OXE CS 主地址并注册。完成标准：分机 in service
4. 配外线：SIP 注册与 DID 翻译按 POD 号对齐。完成标准：翻译表首末号与分机段对应
5. 验证：外呼打通 + 邮箱可用 + 旧信清理。完成标准：实验基线就绪可交付后续章节

判停点：

- 外呼不通 → 先核注册账号与翻译表是否带对 POD 号，再查公共区模拟器状态
- 生产现场类比此卡 → 停，拓扑与取值不同，仅方法论（基线核对、翻译对齐、外呼验证）可迁移
- 公共区资源异常 → 停，POD 间共享 NAS 与模拟器，自行重启可能影响全班

输出契约：Pod 基线核对单 + DID 翻译记录 + 外呼验证结论。

## B — 边界

- 本卡是教学专用域：全部 IP、账号、分机、号码规则与 DDI 段为实验口径，完整环境值清单在 book/overview 环境区
- ITSP2 在书中存在但本课程未用（p14）；模拟器行为与生产 SIP 中继差异大（安全/编解码/号码格式），不可等价
- RLAB 的 OXE 数据库已预配（许可/机架/用户/trunk）——存量现场要从零做，书内不覆盖
- 培训邮箱为 RLAB 专用 webmail，生产无此物
