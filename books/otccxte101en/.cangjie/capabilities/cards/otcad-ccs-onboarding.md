# CCS 安装与实验环境定稿（CCsupervision 安装、OXE 声明、POD 定稿）

## R — 原文依据

> "On Feature level window, select Full for a full CCS version installation. … On Feature level license window, select Monosite. … On Setup type window, select Windows standalone"（p42-43）
> "The CCS application needs to write the updated values in the file ccs.ini file (call server IP address). So you must restart the CCS"（p45）
> "Registration ID pbxN (where N is your POD number) … First external number 33210N41000 … First internal number 31000 … Range Size 1000"（p56-57）

出处：OTCCXTE101EN p3-62。

## I — 自述

CCS 落地与环境定稿的主干三段：

**CCS 安装八步**：NAS 拷软件 > 解压（More info，Run anyway）> CCS.msi 向导（License 接受、目录默认、Feature level=Full、许可=Monosite、Excel=Yes、
界面语言、Windows standalone、登出实时信息=Yes、ASM Script Editor=No、ccs.ini 合并 OK、Finish）。
首次登录 administrator/alcatel 强制改密（大写+数字+特殊字符，实验口径 Superuser01*）。

**声明 OXE**：Window > Customise… > Network > node1 > Modify > Direct access：勾 Connected at start up 与 Direct connection，
Master PABX name 填 Call Server IP > OK > Yes > 提示重启 > 关闭 CCS 再启动。
ccs.ini 是配置落盘文件，改完不重启不生效。验证：Real time > Navigator 打开 CCD 矩阵全景。

**POD 定稿四件套**（实验口径）：

| 步骤 | 路径 | 参数 |
|---|---|---|
| 软话机上线 | Client10 启动 MicroSIP-31010/31011/Public | SIP 密码 123456；Public 选 Public POD X profile |
| 坐席登录 | IPDSP 注册 31000+个人码 0000 后 LogOn | 31500 自助型点 List 选组；31501 非自助型直输坐席号 |
| 外部 SIP 网关 | WBM SIP > SIP Ext. Gateway | Registration ID=pbxN、Outgoing username=pbxN |
| DID 翻译 | Translator > External Numbering Plan > Default DID num. translator | 首外号 33210N41000、首内号 31000、范围 1000 |

验证：Public 软话机拨 0210X41600/0210X41601（X=POD 号），坐席接听挂机后自动 wrap-up 即通过；嵌套 RDP（PC10 会话内再连 PC11）远程音频须设"在本机播放/录音"（n42）。

## A1 — 书中案例

**从空 PC 到呼入全通**（p39-62）：

1. Client10（192.168.1.10）从 NAS 拷 CCS 软件并按八步装完
2. 首登 administrator/alcatel，按安全规则强制改密后用新密码重登
3. 声明 OXE：Customise > Network 填 Master PABX=192.168.1.3，重启 CCS
4. Navigator 打开确认看到 CCD 矩阵全景（p47 验收句）
5. 核对用户与机架：31010/31011 在册、主/远端 OMS 在役
6. MicroSIP 三实例与 IPDSP 上线，两坐席分别登录 Agent_PG
7. 配外部 SIP 网关（pbxN）与 DID 翻译（33210N41000/31000/1000）
8. 外呼入测试 0210X41600/0210X41601、内呼 31600/31601，挂机后自动 wrap-up 通过

## A2 — 未来触发

使用情境：新客户端装 CCS；CCS 连不上 OXE；坐席软话机登录；外部 SIP 网关注册与 DID 翻译；实验/演示环境从零定稿。

语言信号：CCS 安装 / CCsupervision / Monosite / ccs.ini / 声明 OXE / Navigator / Master PABX / POD / MicroSIP / IPDSP / LogOn / SIP Ext. Gateway / pbxN / DID 翻译 / 33210N41000 / wrap-up。

与相邻能力区分：多客户端集中接入与 CCS Server 转 CCS Server 卡；ACR/技能对象配置转 ACR 对象卡（路由卡）；RLAB 虚机与拓扑背景转 book/overview 环境区。

## E — 可执行步骤

输入契约：Windows 客户端与 OXE 网络可达、安装介质（NAS/软件包）、Call Server IP、坐席与分机规划。

1. 装 CCS（八步向导，ASM Script Editor 组件按需）。完成标准：桌面入口可用
2. 首登改密并重新登录。完成标准：新密码可用
3. 声明 OXE 并重启 CCS。完成标准：Navigator 显示矩阵全景
4. 软话机上线与坐席登录。完成标准：坐席状态在 CCS 可见
5. 配外部 SIP 网关与 DID 翻译。完成标准：外呼环回与呼入测试全通
6. 嵌套 RDP 时设置远程音频指向本机。完成标准：坐席软话机有音频（n42）

判停点：

- 改了 Call Server IP 连不上 → 停，先查是否重启了 CCS（ccs.ini 不重启不生效，n02）
- 首连后每次弹证书/密码告警类问题 → 停，按安装章安全规则处理；实验口令绝不带进生产（n01）
- 呼入不通 → 停，按"网关注册 pbxN > DID 翻译三参数 > 呼叫测试号码"顺序逐段核对
- 需要多客户端集中接入 → 停，转 CCS Server 卡（容量与强制条件在那里）

输出契约：可用的 CCS（已声明 OXE）+ 环境定稿核对单（用户/话机/坐席/网关/DID）+ 呼入测试记录。

## B — 边界

- 全部地址、账号、口令、号码为实验口径（RLAB POD 专属），生产必须整体替换并做安全加固（n01）
- 教材默认学员已完成 Standard 基础课程：CCD 矩阵基础概念本书不作入门讲解（BOOK_OVERVIEW 批判）
- SIP 模拟器号码规则（3321PN 系列）为教学约定，生产按运营商中继号规划（p19）
- CCS 版本基线与浏览器支持随版本演进（Ed07 口径 V10.2.92.0+）；安装选项以当期安装介质为准
- Console mode 无音频（Guacamole 管理通道），软话机音频必须走 RDP（p13）
