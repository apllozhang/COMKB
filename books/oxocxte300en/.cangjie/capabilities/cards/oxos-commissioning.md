# 系统开通双路线（FTR 上云 / OMC Standard）与首次连接

## R — 原文依据

> "OXO Connect Cloud Connect solution: • Auto registration on Cloud Connect Standard Solution: • On-site management with OMC"（p51）
> "To register the OCE on Cloud Connect, open the web browser and enter as URL: 192.168.94.246 (ETH1)"（p61）
> "Default IP Address: 192.168.92.246 • Default Password: pbxk1064 (First connection)"（p67）
> "The passwords must be different for each customer!"（p81）
> "Note: the Initial Installation Wizard is the one and only way to put an OXO a Hotel mode"（p447）

出处：OXOCXTE300EN p50-95（部署方案/FTR/OMC/IP 修改/默认配置），p439-452（安装向导）。

## I — 自述

开通先岔路，再进场：

- **路线一 Cloud Connect（六步）**：开箱接客户 LAN 即插即用，自动连云、软件与许可自动下载、远程/现场管理（防火墙友好）、机队级 Web 分析、云端自动更新。OCE 的入场口是 FTR：PC 接 ETH1，浏览器开 192.168.94.246 点 Register，installer 登录后强制改密，填 IP 五项与三参考值提交
- **路线二 Standard（四步）**：装 OMC，用出厂 IP 192.168.92.246 连接（Expert 模式+服务器认证），上传软件，导入两把许可（.msl 主钥匙+.csl CTI 钥匙，与主 CPU 序列号绑定）
- **首连收尾三件事**：证书装进受信任的根（之后不再弹告警）、七个账户改密（每客户必不同）、录客户信息（带 * 必填）
- **IP 规划修改**：OMC/Hardware and limits/Lan/IP configuration 四页签（Boards/LAN/DNS/DHCP），改完必须重启 OXO，PC 同步改址
- **初始安装向导**：只在初始状态（首启或冷复位后）可跑，话机版或 OMC 版；Business/Hotel 模式唯一入口在向导第一步

## A1 — 书中案例

**FTR 实验**（p59-62，物理课堂限定）：

1. ETH0 接 PoE 交换机、ETH1 接管理 PC，等约 3 分钟完全启动
2. PC 网卡配 DHCP（ETH1 自带池 192.168.94.247-254）
3. 浏览器开 192.168.94.246，点 Register
4. installer / pbxk1064 登录（实验口径，仅首次），强制设新密码
5. 填 ETH0 IP 192.168.1.246、网关 .254、代理 .254:3128、DNS .250（实验口径）
6. 填参考值 OXOP / TRAINING / LAB（实验口径），点 V 提交
7. 验收：注册入云、许可自动下载、系统更新、Fleet Dashboard 远程可达
8. 虚课替代：OCE 保持默认配置，走 OMC 常规连接改 IP（p60 原文明示）

**OMC 首连实验**（p73-82）：

1. 解压 OMC 安装包，setup.exe 以管理员运行
2. Expert 菜单 → LAN/WAN → 192.168.92.246 + 服务器认证 + 首连密码（实验口径）
3. 安全告警 → View certificate → Install certificate，存入 Trusted Root Certification Authorities
4. 改七账户密码 → 录客户信息 → 右下角图标显示已连接

**IP 修改实验**（p83-86）：四页签填新规划 → OK 重启 OXO，PC 改静态五项，以新地址可管理为验收（虚课以 RDP 重连成功为切换完成标志）。

## A2 — 未来触发

使用情境：新设备开箱交付；客户没外网要选路线；每次连接弹证书告警；pbxk1064 是什么；换网段重规划 IP；冷复位后重建基础配置；酒店项目定模式。

语言信号：FTR / Cloud Connect / Standard / 装 OMC / 首次连接 / 证书告警 / .msl / .csl / 改 IP / Lan/IP configuration / 初始安装向导 / Hotel 模式 / warm reset。

与相邻能力区分：系统可管理后开通终端（终端能力）；号码与组落库（编号计划与组能力）；接入 Rainbow（Rainbow 集成能力）。本能力到"系统可管理+IP 到位+许可生效"为止。

## E — 可执行步骤

输入契约：硬件形态（OCE/PowerCPU EE）、客户是否有出网条件与 Cloud Connect 服务、数据采集表。FTR 需物理接触 ETH1——远程虚课做不了（n02）。

1. 选路线：有云条件走 Cloud Connect，否则 Standard。完成标准：路线与许可来源成文
2. （Cloud Connect）布线 ETH0+ETH1，PC 配 DHCP，浏览器开 192.168.94.246。完成标准：Register 页可登录
3. FTR 填参：IP 五项+三参考值，强制改密。完成标准：注册入云、许可下载、远程可达四项验收
4. （Standard）装 OMC → 首连 192.168.92.246 → 证书入受信任根。完成标准：重连不再弹告警
5. 导许可：.msl 走第一导入键、.csl 走下方键，Apply 送入系统。完成标准：Details 显示服务已开
6. 改密与客户信息：七账户逐客户唯一、带 * 必填录入。完成标准：无默认密码残留
7. IP 四页签改规划 → 重启 OXO → PC 改址。完成标准：新地址可连、旧地址失效
8. （需要时）跑初始安装向导定模式与基础参数。完成标准：向导末尾系统按新配置重启

判停点：

- 首连密码已被改且无人知道 → 走密码重置流程（书外），不要试错
- 旧默认密码表（kilo1987/help1954 等）在 R10.1 后已弃用，pbxk1064 仅剩首连一个用途（n20）
- IP 改完连不上 → 先确认是否用旧地址/旧会话，改 IP/DHCP 后必须重启（n04）
- 存量系统想切 Hotel → 必须冷复位重来，模式决策必须前置（n37）

输出契约：可管理的系统（路线凭证/许可/改密记录）+ 新 IP 规划落地确认。

## B — 边界

- pbxk1064/Alcatel1 等全部为实验口径明文值，生产设备沿用任何一个是重大隐患（n44）
- Cloud Connect 依赖客户出网与云服务开通；Fleet Dashboard 细节原书从简
- ETH1 是专用服务口：不得接 LAN、不能访问 Eth0 侧 LAN、IP 冲突自动禁用（p57 四条）
- OMC 版本与 PBX 软件配套关系原书未给矩阵，下载时按 p318 三件套口径取配套版本
- 换 PowerCPU EE 后 eMMC 可移植但必须重新生成许可（n22）
