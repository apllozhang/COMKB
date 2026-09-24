# CCS 班长台安装、OXE 声明与 ccs.ini

## R — 原文依据

> "On Feature level window, select Full for a full CCS version installation. … On Feature level license window, select Monosite. … On Excel window, click on Yes"（p92）
> "On Setup type window, select Windows standalone … On Real Time Information when logged-off? Window, click on Yes … On ASM Script Editor window, click on No"（p93）
> "From Network menu, select node1 and click on Modify … Master PABX name Enter the IP address of the Call Server (i.e. 192.168.1.3)"（p94-95）
> "A CCS station cannot create any object relative to call distribution …, but can create CCS supervisors and distribution rules."（p79）
> "CCS.ini file is read every time the CCs is started • This file is located in programData / Alcatel / CCsupervisor by default"（p85）

出处：OTCCXTE100EN p78-97, p511-512。

## I — 自述

CCS（Alcatel-Lucent CCsupervision）是 Windows 桌面班长台：管规则开闭、座席属性、实时监督（Navigator）、Excel 统计与紧急关闭；但无权创建 CCD 底层对象（p79 权责硬边界）。

安装决策链（p91-93）：

- 安装链：CCS.msi → EULA → 默认路径（自动装 VC++ 2017 x86）
- 决策屏：Feature level=Full → 许可类型=Monosite（实验口径，生产按现场选 Multisite）→ Excel 集成=Yes
- 后续屏：语言（实验保留英文界面）→ Setup type=Windows standalone → 核对 Station ID
- 收尾：无班长登录也要实时信息=Yes；ASM Script Editor=No

OXE 声明与首登（p94-96）：

- Window> Customise> Network 选 node1 Modify：Direct connection + Master PABX name=OXE 地址 → 必须重启 CCS（ccs.ini 要写入呼叫服务器 IP，p95）
- 默认账号 administrator/alcatel（实验口径），首次登录强制改密（实验改 Superuser01*）

ccs.ini 要点（p85-87）：每次启动读取；id_terminal（0..127）全网唯一、冲突即异常；MultiSite/CcsLight 决定 token 类型；多数显示设置走 CUSTOMIZE 窗口，ShowStatisticWithData（CCS 10.5+）必须手改进 [default_configuration] 节（n10）。

## A1 — 书中案例

**安装与声明实验**（p89-97）：

1. Client PC 10 从 OTCC_NAS 拷 CCS 软件到 Documents 并解压（More info → Run anyway）
2. 运行 CCS.msi：EULA、默认路径，Feature level=Full、许可=Monosite、Excel=Yes
3. 语言保留 English+French、界面 English；Setup type=Windows standalone；实时信息=Yes；ASM=No
4. Install → ccs.ini 合并提示 OK → Finish
5. Window> Customise> Network> node1 Modify：Direct connection、Master PABX name=192.168.1.3（实验口径）→ 确认并按提示重启 CCS
6. administrator/alcatel 登录 → 强制改密 → 用新密码重登
7. Real time> Navigator 查看 CCD 阵列——此时无连线属正常（规则未建，下一实验补）

## A2 — 未来触发

使用情境：装 CCS 装到一半报错；换呼叫服务器 IP 后连不上；id_terminal 冲突；CCSLight 还是 Monosite token；座席会话报表想只看有数据的座席；改了配置"没反应"。

语言信号：CCS / CCsupervision / CCS.msi / Monosite / Multisite / CCSLight / node1 / ccs.ini / id_terminal / Station ID / administrator / ShowStatisticWithData / 重启。

与相邻能力区分：建 CCD 对象本身 → CCD 基础矩阵能力（CCS 建不了）；装好后建规则 → 路由与分配规则能力；Excel 统计参数归监控与统计能力。

## E — 可执行步骤

输入契约：CCS 安装包与许可 token 类型已定（Monosite/Multisite/CCSLight）、OXE 管理地址可达、安装 PC 满足 Windows 桌面要求。

1. 安装 CCS.msi：按决策链逐屏选择（Feature level=Full、许可类型按现场、Excel=Yes）。完成标准：Finish 无报错、桌面出现 CCsupervision
2. 声明 OXE：Window> Customise> Network 选节点 Modify，填呼叫服务器地址与直连方式。完成标准：确认后按提示重启 CCS
3. 重启 CCS 并首登：默认账号登录 → 按安全规则改密 → 新密码重登。完成标准：进入主界面无连接报错
4. 核对 ccs.ini：my_name 与 id_terminal（0..127）全网唯一、token 类型与许可一致。完成标准：无冲突告警
5. Real time> Navigator 打开看矩阵。完成标准：能显示 OXE CCD 对象（无连线属正常）

判停点：

- 声明后连不上 → 先确认重启过 CCS（IP 写入 ccs.ini 的必要动作，p95/n21）
- 多台 CCS 站冲突 → 查 id_terminal 是否重复（0..127 唯一）
- 想在 CCS 里建 pilot/队列/PG → 权责边界，转 OXE 侧（矩阵能力卡）
- 需要 ShowStatisticWithData → 无 GUI 入口，手改 ccs.ini [default_configuration] 节后重启（n10）
- 许可类型拿不准（Monosite vs Multisite）→ 判停确认现场拓扑，多站点在本书边界外（n41）

输出契约：可登录的 CCS 班长台 + 与 OXE 连接正常（Navigator 可见矩阵）+ ccs.ini 核对记录。

## B — 边界

- Multisite 多站点 CCS 只出现在 ccs.ini 注释与安装选项里，本书不教多站点部署（n41）
- 实验账号口令（administrator/alcatel、Superuser01*）为实验口径，生产必须按安全基线替换（n19）
- CCS 界面为 R10.16/CCS 10.5 时代 Windows 桌面应用，云化/网页化不在本书视野（批判区）
- ShowStatisticWithData 是"必须手改文件"的例外，其余显示设置优先走 CUSTOMIZE 窗口（p85-87）
- 改 Excel 参数、统计对象数、呼叫服务器 IP 三类改动都要求重启 CCS（p95/p505/p518）
