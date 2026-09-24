# OmniVista 8770 平台安装（服务器 + 客户端 + 补丁 + 首连）

## R — 原文依据

> "The OmniVista 8770 Server must be installed on a dedicated server"（p55）
> "Do not install the 8770 server from the network, from an iso mount, or via vSphere!"（p69）
> "It should contain the following message at the end of the file: Patch installation terminated: success"（p78）
> "Both Windows managements are required to enable Alarms and Topology applications."（p83）
> "Enter the following URL: https://<8770 FQDN>/cgi-bin/OmniVista8770Client.exe Be careful, the URL is case sensitive!"（p99）

出处：8770XTE200EN p55-106（2022 章）、p618-639（2019 章）。

## I — 自述

把 8770 从裸 Windows 装到可登录，主链七步，两条硬规则贯穿：

**装前两条硬规则**

- 服务器必须独占（dedicated），资源按专用机规划，不与其他应用混装
- 安装源（iso）必须先拷到服务器本地硬盘，禁止网络路径、虚拟挂载光驱、vSphere 直接安装

**七步主链**

1. Windows 数据配置：NTFS 分区；计算机名 <15 字符、字母开头、禁用 11 类字符（含下划线与点）；设 DNS 后缀；改后重启
2. 静态 IP + 网关 + DNS（三件装后多数场景不变，改名改址要走备份恢复/rehosting）
3. 双击 ServerSetup.exe（管理员身份）：自动装 MariaDB + Visual C++ 包；校验许可文件全部 Valid
4. 安装参数：公司名（装后不可改）、四个目录（C:\8770、C:\8770\SunONE、C:\8770\data、C:\8770_ARC）、LDAP 389 / LDAPS 636 端口、目录管理器密码、AdminNmc 账户、国家、计费成本中心方式（装后不可改）
5. 完成重启；装后两件 Windows 管理：关 IE 增强安全配置（Administrators 与 Users 都 Off）+ Defender 排除 C:\8770——漏做则 Alarms/Topology 收不到告警
6. 补丁：拷入 C:\8770\install\patches，管理员运行 PatchInstaller.exe；核对 Patch_Installer.log 尾部成功消息；已装清单查 Patch_history.ini；安装设置存档在 C:\8770\RestoreContext.ini
7. 首连：客户端或服务器本机登录 AdminNmc，强制改初始密码；连接信息存 C:\Users\<账户>\nmc5_5.2.cfg

**客户端安装（管理员 PC）**

- 首选从服务器 Web 下载：https://<8770 FQDN>/cgi-bin/OmniVista8770Client.exe（大小写敏感，需管理员凭据）
- 前置：本地管理员权限；Win11 build 22572（22H2）起须在可选功能中装回 WMIC；剩余磁盘 ≥750MB（JVM 启动底线，见 needs-review nr-03）
- 首次启动放行防火墙弹窗的 Zulu Platform x32 模块（专用网络）；硬件底线 4GB RAM / 40GB 硬盘

**容量与口径**

- 硬件双档（p55-56）：<5000 用户双核约 2GHz + 6GB（含 MMP 许可 7GB）；>5000 用户四核约 2.2GHz + 8GB（含 MMP 9GB）；均 120GB 盘（>5000 档 RAID5 15K RPM）、显卡 128MB、Haswell 架构以上
- 安装期内存占用须 <85%；端口 80/8443/389/636/8080 自动配进 Windows 防火墙且不可改

## A1 — 书中案例

**Windows 2022 Server 安装实验**（p65-88）：

1. 改计算机名与 DNS 后缀（实验口径 nms / company.com，参数见 book/overview），重启
2. 配静态 IP 四件（IP/掩码/网关/DNS，实验口径）
3. 管理员运行 ServerSetup.exe，自动装 MariaDB 与 Visual C++ 包
4. 选许可文件，License verification 全部 Valid
5. 逐页填公司名、四目录、LDAP/LDAPS 端口、目录管理器密码、AdminNmc、国家、成本中心
6. 装完重启；关 IE ESC 与 Defender 排除 C:\8770
7. 补丁入 patches 目录后运行 PatchInstaller.exe，日志尾部见成功消息
8. 客户端首连 AdminNmc，按提示强制改密，进入管理会话

**Windows 2019 Server 安装实验**（p618-639）：步骤与 2022 章相同，DNS 指向 ecosystem 虚机；连接信息文件名原文写 nmc5_5.1.cfg（旧版沿用，见 nr-01）。

## A2 — 未来触发

使用情境：新项目装 8770；装完 Alarms/Topology 没数据；补丁装完怎么确认；Win11 客户端打不开；装错了公司名/成本中心想改。

语言信号：装 8770 / ServerSetup / dedicated / IE ESC / Defender 排除 / PatchInstaller / Patch_history / RestoreContext.ini / WMIC / Zulu / nmc5_5.2.cfg / 首连改密。

与相邻能力区分：装好之后接被管节点 → 节点接入能力；许可文件内容与扩容 → 许可管理能力；本能力到"管理员可登录、补丁装完"为止。

## E — 可执行步骤

输入契约：一台符合双档要求的 Windows Server（或虚机）、8770 安装介质与许可文件、客户参数表（计算机名/DNS 后缀/IP/公司名/国家/成本中心口径）。

1. 核对独占性与安装源：iso 拷到本地盘。完成标准：无网络路径/挂载光驱/vSphere 安装
2. Windows 数据配置：计算机名合规 + DNS 后缀 + 静态 IP。完成标准：改名后已重启且 ping 网关通
3. 管理员运行 ServerSetup.exe 走完安装向导。完成标准：License verification 全部 Valid、四目录落在指定分区
4. 装后两项 Windows 管理：IE ESC 全 Off + Defender 排除 C:\8770。完成标准：两项可复查确认
5. 补丁：patches 目录 + PatchInstaller.exe。完成标准：Patch_Installer.log 尾部成功消息
6. 首连 AdminNmc 强制改密。完成标准：进入管理会话，连接信息存 nmc5_5.2.cfg
7. 客户端分发：URL 下载（注意大小写）或安装介质；Win11 先装回 WMIC。完成标准：客户端登录成功且 Help 中可见已连客户端

判停点：

- 公司名/成本中心/目录管理器登录名填错 → 不要试改（装后不可改），立即卸载重装
- 内存占用 ≥85% → 停止安装，先扩资源
- 2019 现场文件名/DNS 与本书两章都不一致 → 以现场为准并记录，不强行套书

输出契约：可登录的 8770 服务器 + 补丁清单（Patch_history.ini）+ 已分发客户端清单 + RestoreContext.ini 存档位置。

## B — 边界

- 服务器必须独占；8770 内嵌 MariaDB/LDAP/Apache/Wildfly 全栈，不与域控等其他角色混装
- 安装向导中公司名、成本中心方式、HTTP/HTTPS 端口、目录管理器登录名装后不可改；改计算机名/DNS 后缀/IP 的正规路径是备份恢复或 rehosting（见备份恢复卡）
- 实验口径环境值（计算机名 nms、IP 192.168.1.70、目录管理器密码 superuser、首连改密 Superuser01* 等）只作教学演示，生产必须按客户密码策略替换（needs-review nr-06）
- 2019 章沿用旧版内容（cfg 文件名 nmc5_5.1.cfg、无 WMIC 附录，见 nr-01）；R5.2 起 wildcard 证书被自动生成服务器证书替代（n10）
- 容量为安装门槛口径（<5000/>5000 两档），生产规模设计需 Capacity Planning 工具（书外）
