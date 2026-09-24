# ACR 外部 ASM 部署与双机热备（割接六步、Site 角色、Main/Stand-By）

## R — 原文依据

> "you must disable the parameter "asm_on_dhs" in the "parameters.cfg" file … so "AFE" will not start the "ALB" process"（p322）
> ""Router" role: call routing requests will be handled by the ASM server … "Default" role: call routing requests won't be handled anymore by the ASM server … Agents of this site could be inserted in the agent list"（p330）
> "To transfer the script from an internal to an external ASM server (and vice-versa), the "scr" file has to be copied and recompiled • Restart the ASM server (windows service) after script transfer"（p335）
> "As soon as the connection between the MAIN ASM Server (PC1) & the AFE Server (Oxe csm), the connection will be automatically duplicated between the Stand-By ASM Server (PC2) & the AFE Server."（p371）

出处：OTCCXTE150EN p318-373。

## I — 自述

外部 ASM 是"出 OXE"的服务器形态：角色与内部 alb 一致，外加外部数据库访问能力。

部署五要素：

1. **组件三选**：Alcatel ASM Module（服务器加管理器）/ 仅 ASM Manager 客户端 / 仅 ASM server 组件
2. **服务形态**：Windows 服务，必须设 Automatic 启动模式；MMC 或配置工具启停
3. **站点链接**：ASM Manager 或 ASMServer Tool 建 New Site（站名、Main CPU、Stand-by CPU、Connection role）
4. **站点角色**：Router=处理路由请求并跑脚本、本站点坐席可入列表；Default=不处理路由不跑脚本、坐席仍可入列表
5. **双机热备**：两台 Windows 服务互设 Main/Stand-By；主备连接自动复制、脚本自动同步

割接顺序链（顺序错连不上）：

1. OXE 上把 parameters.cfg 的 asm_on_dhs 改 0
2. 重启 MAIN_AFE（dhs3_init -R MAIN_AFE），必要时 kill alb（ps -edf | grep alb 核查）
3. 装外部 ASM 与服务并启动
4. 建 Site 链路（内部 alb 未停则外部 ASM 连不上 AFE）
5. 迁移脚本（复制 .scr 重新编译）并激活
6. 防火墙放行与维护核查

迁移与许可边界：脚本文件内外不通用（.alb 不跨环境），只能复制 .scr 重编译，迁完重启服务；外部 ASM 与 OXE 间连接免许可，连外部数据库才需要 167 号许可。文件位置：内部在 OXE /usr3/afe，外部在安装目录 Script 子目录。

## A1 — 书中案例

**单机割接（c12）**：

1. telnet OXE，vi 把 asm_on_dhs 1 改 0，ESC :wq 保存
2. dhs3_init -R MAIN_AFE 重启；ps -edf | grep alb 核查 alb 已停
3. PC 上装 ASM（Standalone system），ASM Manager 里 Install 服务，MMC 核自动启动
4. ASMServer Tool 建 Site_1：Main CPU 填 csm 或 IP，Connection role=ROUTER
5. 编辑器连外部 ASM，Import 取 ISM_IDLE.scr（可 FTP 从 OXE /usr3/afe 取），对 ACR Pilot 激活
6. 呼统计 Pilot 实测，adm_acd 选项 11/14 核外部链路；连不通查防火墙入站规则

**双机热备（c13）**：

1. 备机装 ASM 选 Duplicate system 加 Stand-by ASM，Dual ASM 填主机名
2. 主机停服务后 ASMServer Configuration 激活 Duplicated ASM，ASM Mode=Main，填备机名
3. 备机 Install 服务并核自动启动；改配置前必须停服务
4. 备机 Connection 可见主机的 Site Connection（主连接建立后自动复制）
5. 核对两机脚本目录一致；停主 ASM 服务再呼：脚本改在备机执行；恢复主服务

## A2 — 未来触发

使用情境：要用外部数据库所以必须外部化 ASM；OXE 资源占用由外部服务器分担；要求 ASM 高可用；割接后连不上 AFE；脚本迁移后不可用。

语言信号：外部 ASM / External ASM / asm_on_dhs / alb 进程 / 割接 / Site / Router 角色 / Default 角色 / 双机 / Main / Stand-By / Duplicated ASM / 脚本迁移 / scr / alb / 防火墙。

与相邻能力区分：外部库脚本写法，见 外部数据库查询路由能力；矩阵对象，见 CCD 矩阵地基能力；脚本调试，见 脚本编辑器能力。

## E — 可执行步骤

输入契约：目标 Windows 服务器、OXE 维护权限、脚本 .scr 清单、双机需求与主机名规划。硬件软件需求先查随软件安装规程（书外）。

1. 停内部 ASM：asm_on_dhs 改 0，重启 MAIN_AFE，核查 alb 进程已停。完成标准：grep alb 无输出
2. 装外部 ASM（单机 Standalone 或备机 Duplicate system）。完成标准：服务安装且启动模式为自动
3. 建 Site：站名、Main CPU、Connection role。完成标准：链路图出现、状态连接
4. 迁移脚本：复制 .scr 到外部 ASM 并重新编译激活。完成标准：ACR Pilot 上脚本生效
5. 防火墙放行 ASM 与 ASMMgr 的入站 UDP 加 TCP。完成标准：编辑器与 adm_acd 均可达
6. （双机）主机改造为 Duplicated/Main，备机知晓 OmniPCX 名。完成标准：备机可见复制的连接
7. 切换演练：停主服务，验证备机接管脚本执行，再恢复。完成标准：呼叫不中断路径验证通过

判停点：

- 外部 ASM 连不上 AFE → 停，第一嫌疑是内部 alb 未停，回步骤 1 顺序核查
- 迁移后脚本报错或不可用 → 停，确认复制的是 .scr 且已重编译，.alb 直接拷贝不通用
- 双机改配置 → 停，先停 ASM 服务再改；备机解析不了 OmniPCX 名会切换失败
- localhost 连不上 → 用 IP 直连，localhost 仅在 hosts 文件配置时有效

输出契约：割接完成的外部 ASM（或双机）+ 脚本激活记录 + 链路与切换验证证据。

## B — 边界

- 安装前必须 asm_on_dhs=0 且内部 alb 停止（n30/n31），顺序是硬约束
- 防火墙口径为 Windows 防火墙 Private 配置文件；网络侧防火墙策略在书外（n32）
- 双机实验口径：主 10.2.T.20/SoftPanel、备 10.2.T.21/SoftPanel2；脚本目录 Program Files (x86) 下的 Agent Selector Module\Script
- 硬件/软件需求查 installation procedure（p323），原书不给规格
- 外部 ASM 连接免许可、连外部数据库需 167 号许可（n37）；许可核查见外部数据库查询路由能力
