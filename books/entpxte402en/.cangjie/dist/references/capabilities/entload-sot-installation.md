# S.O.T. 部署工具：安装、初始化、更新与 Template Factory

## R — 原文依据

> "The S.O.T. is a virtual machine delivered under an "ISO" format • This ".iso" file (sot-x.x.xxx.xxx.iso) contains the ".ova" file"（p23）
> "In « Standalone mode » ... Installed on technician laptop ... Used to deploy mainly physical servers as OXE CS, GAS « bare metal »"（p24）
> "In « Hosted mode » ... Deployed in a vSphere ecosystem : ESXI server ... Used to deploy other virtual machine(s) as OXE, OMS,…"（p25）
> "This functionality will only be offered for S.O.T solutions in the same major version. The update will be forbidden for version not in the same major version."（p47）
> "Enter Y to bypass resource control ... Template Factory mode is enabled in degraded mode for PC"（p164）

出处：ENTPXTE402EN p22-48、p155-165、p189-203。

## I — 自述

S.O.T.（Software Orchestration Tool）是全书一切软件加载的工具主线：一台自带 DHCP/FTP 服务的虚机，加载工具与加载对象是两台机器。四个维度一次定清：

| 维度 | 取值 | 要点 |
|---|---|---|
| 交付形态 | ISO 内含 OVA | 更新补丁为 zip+MD5 成对交付 |
| 运行模式 | Standalone | 技术员笔记本 VirtualBox/VMware，主用加载物理 OXE CS/GAS 裸机 |
| 运行模式 | Hosted | 部署进 vSphere/ESXi，主用加载同虚拟化系统内的 OXE/OMS 虚机 |
| 配置 | default | softwareOrchestrationTool.ova，物理加载与 OVF 生成 |
| 配置 | Template Factory | 加第二块盘生成 VMware/KVM 镜像模板 |

初始化三步与硬规则：

1. **控制台首配**：启动 VM 后按 1 改键盘（默认 en_US）、选 static 配 IP/掩码/网关/DNS，按 Y 确认后自动重启；后续改配置用 setIp / setKb
2. **Web 首连**：https://SOT-IP 用 admin/letacla 登录（实验口径），强制改复杂密码并设置口令短语（忘记密码的唯一自助通道）
3. **网络规则**：最多 4 个子网；虚机网卡数必须与 Web 页声明的 IP 数一致；默认 1 个接口，加网卡必须重启 SOT

SOT 更新三条规则：

1. 只能同主版本（A.B）内 zip+MD5 更新，跨主版本禁止、须重装 ISO
2. 更新媒体可放在"托管 SOT 的 PC / SOT 本地存储 / NFS"三处之一
3. zip 与 ISO 同时交付时功能同级（可能只有 OS 差异）；更新过程 SOT 重启，完成后 About 菜单核版本

Template Factory 标准前置：8 CPU、16GB 内存、500GB 第二盘、CPU 开 Vmx 标志、USB 控制器；default 转 Template Factory 必须先关机。

降级模式五步（顺序强制）：

1. 用标准 softwareOrchestrationTool.ova 部署 SOT
2. 关机后加一块 50GB 虚拟盘
3. 启用嵌套虚拟化（被设备安全阻止时改注册表后重启 PC）
4. 启动 SOT，控制台输入 templateFactory，按 Y 绕过资源检查
5. Web 界面出现 Template Factory 功能

## A1 — 书中案例

**Standalone 部署全流程**（p37-48，How-To）：

1. 用 7-zip 解包 SOT iso 并挂载（实验口径：iso 在 NAS N:\Softs）
2. VirtualBox 导入 ova；宿主为 64 位时把 Guest OS 从 32-bits 改为 64 bits
3. 控制台按 1 改键盘，选 static 配 IP/掩码/网关/DNS，按 Y 后 VM 自动重启
4. 浏览器打开 https://SOT-IP，admin/letacla 首连，强制改密并设口令短语
5. Settings 区按需改网络、账户、更新（About 菜单核对版本）

**降级模式启用**（p155-165，How-To）：见 E 段步骤 5；控制台提示 "Template Factory mode is enabled in degraded mode"（p164）为完成判据。

## A2 — 未来触发

使用情境：交付前准备加载工具；SOT 装不上/连不上；忘记 SOT 密码；SOT 升级；要给虚机交付生成镜像模板；低配笔记本要不要建模板。

语言信号：SOT / Software Orchestration Tool / Standalone / Hosted / ova / ISO / Template Factory / degraded mode / 降级模式 / setIp / setKb / SOT update / 4 subnets。

与相邻能力区分：

- 往 SOT 传媒体、建加载项目 → 媒体与项目卡（路由）
- 加载 OXE 本体 → CS 加载卡
- 生成 OXE/OMS 虚机镜像 → 虚拟化交付卡

## E — 可执行步骤

输入契约：目标机类型（物理/虚机）、宿主虚拟化层（VirtualBox/VMware 或 ESXi）、SOT ova 与升级 zip+MD5 媒体。客户网络与 SOT 不同网段 → 判停先打通网络。

1. 选形态：物理交付选 Standalone，虚机交付选 Hosted。完成标准：模式与目标机类型匹配
2. 导入并首配：ova 导入虚机层，控制台配键盘与 IP，Web 首连改密+口令短语。完成标准：Web 界面可登录
3. 网络核对：子网数 ≤4，虚机网卡数与声明 IP 数一致，加网卡后重启。完成标准：网络设置保存生效
4. 更新（按需）：Settings 的 Update S.O.T. 选 zip+MD5，Launch 后 About 核对。完成标准：版本末 3 位非 000
5. Template Factory（按需）：关机加 500GB 盘（降级 50GB）开嵌套虚拟化，控制台跑 templateFactory 按 Y。完成标准：Web 出现 Template Factory 页

判停点：

- 跨主版本更新（如 3.1 升 3.2）→ 停，zip 硬更被禁，重新部署新 ISO
- Template Factory 功能没出现 → 停，先跑 templateFactory 命令看缺失清单，别反复重启
- 需要同时部署多台目标机 → 停，SOT 一次只允许一个部署任务，排队或另起实例
- 口令短语没设就交机 → 停，忘密后无自助通道，只能重装

输出契约：可用的 SOT（模式/配置已定、网络可达、版本受控）+ 口令短语已入团队密码库的确认。

## B — 边界

- SOT 一次只允许一个部署任务；虚机尺寸规格在《Delivery note》文档，不在本教材（p22）
- 降级模式是官方支持的绕过：硬件前置不再受控，浏览器首页常驻警告横幅；OVA 构建时长强依赖机器 RAM/核数（p29/p156）
- vSphere thick client 仅支持到 ESXi 6.0，Web 界面才是主路径（p199）
- SOT 首连密码规则（≥8 字符四类各一）与 OXE 侧规则（≥14 字符九条约束）是两套体系，勿混用（p44/p91）
- SOT 与目标机须同网段（p24 Note）；版本兼容以 S.O.T. Release Note（TC2456）为准
- 实验口径：SOT IP 192.168.1.130/.230、admin/letacla、新口令 Superuser2580*——仅培训环境，生产必换
