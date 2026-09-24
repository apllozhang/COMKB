# OmniVista 8770 Topology 视图（标准视图 / 自定义视图 / 告警重定向）

## R — 原文依据

> "2 tabs (or views), Standard and Custom ... Structured according to tree structure of the Configuration application"（p331）
> "Such maps, in a gif format (for example) with the standard size of 1100x793, have to be stored on 8770\data\topology\maps."（p337）
> "Right click on the link, Select Redirecting alarms… option ... paste the alarm on the field Source Object hierarchy"（p358）
> "FROM RELEASE R11.2 OF THE OMNIPCX ENTERPRISE, ALARM LINKED TO IP PHONE STATUS (INCIDENT 386) IS NOT CONSIDERED AS CORRELABLE."（p361）

出处：8770XTE200EN p325-362（Topology 讲义与两个 How-To）。

## I — 自述

Topology 是网络图形化监控面：Standard 视图按配置树自动生成，Custom 视图手工搭监控大屏；只显示相关告警。

**Standard 视图（自动生成）**

- 结构随 Configuration 树自动生成；支持背景地图（.gif/.jpeg/.ivl，自定义地图建议 1100x793，放 8770\data\topology\maps 后须重启 NMC Service Manager 才入下拉）
- 虚拟 ACT 显示：Configuration 硬件树选中虚拟机架 > 取消勾 Virtual equipment > 重启 Topology 应用
- Preferences > Topology > Configure：Read Saved Configuration（改后需重启 Topology）、Display VPN Links、Display OXE Links、Display 8770 server
- 告警联动：故障机架出现告警，双击看告警；相关告警随设备恢复自动清除

**Custom 视图（编辑器）**

- Custom 页 > Activate Edit mode 后可用工具：Create custom view（绑定被监督对象+背景）、Create network element（图标/短长描述）、Create link 与 Square link（标签/线型/宽度/颜色）、Create label、多边形/矩形底色、Default view 定默认视角
- 树结构与视图同步；双击视图名进入

**告警重定向（把告警画到自选元素上）**

- 取对象层级：从 Configuration 界面复制对象（如 GD4 板卡、T0 中继、TDM/IP 用户终端），或从 Alarms 应用复制告警
- 粘贴：Custom 视图右键网络元素/链接 > Redirecting alarms > 粘到 Source Object hierarchy
- 验证：mtcl 执行 rstcpl 触发，该元素上显示告警；右键 Show Alarms 可切到 Alarms 页

**两条硬边界**

- Topology 只显示相关告警（p327 Limits）
- OXE R11.2 起 IP 话机状态告警（incident 386）不再是可相关告警——不能用于 Topology，话机级监控走 Alarms 应用

## A1 — 书中案例

**Standard 视图实验**（p334-338）：

1. Preferences 改 Read Saved Configuration 为 Standard configuration
2. 取消虚拟机架的 Virtual equipment 勾选并重启 Topology，虚拟 ACT 上图
3. 选 EUROPE.gif 加载背景地图
4. rstcpl 触发后故障机架显示告警，耦合器恢复投运后告警自动清除

**Custom 视图实验**（p339-362）：

1. Edit mode 下建视图 Main Node（背景 FRANCE.gif），把 nms 图标摆进主视野
2. 建 Element #1 与 nms 的 link、Element #1 与 Main Node 的 Square link
3. 加标签、六边多边形与矩形底色，Default view 定格
4. 从 Configuration 复制 GD4 板卡对象粘到 Redirecting alarms，rstcpl 4 0 后元素显示 #2042 类告警
5. T0 中继/TDM 用户/IP 用户同法重定向；8770 自身告警从 Alarms 应用复制

## A2 — 未来触发

使用情境：给客户搭监控大屏；自定义园区背景图；"话机故障怎么不在地图上闪"；演示网络健康度。

语言信号：Topology / Standard / Custom / Edit mode / custom view / 背景地图 / 1100x793 / topology\maps / 虚拟 ACT / Virtual equipment / 告警重定向 / Redirecting alarms / Source Object hierarchy / incident 386。

与相邻能力区分：告警数据本身（告警管理能力）；rstcpl 触发手段（告警接入验证）；本能力管图形化呈现与期望管理。

## E — 可执行步骤

输入契约：监控大屏需求（对象清单/背景图）、地图文件（gif，建议 1100x793）、告警对象层级来源确认。

1. Standard 基线：Preferences 四选项核对。完成标准：视图按树生成且告警可显示
2. 背景：地图入 maps 目录 > 重启 NMC Service Manager > 下拉选用。完成标准：背景加载
3. 虚拟 ACT：取消 Virtual equipment 勾选 > 重启 Topology。完成标准：虚拟机架上图
4. Custom 建屏：建视图 > 摆元素 > 连链接 > 加标签与底色 > Default view。完成标准：视图成型可导航
5. 重定向：复制对象层级 > Redirecting alarms 粘贴。完成标准：rstcpl 触发后元素显示告警
6. 验收演示：触发+自动清除全流程走一遍。完成标准：客户确认显示口径

判停点：

- 地图下拉没有新图 → 只拷了文件没重启 NMC Service Manager；先重启再排障
- 客户要话机状态上图 → incident 386 不可相关，判停并引导走 Alarms 应用
- 改 Read Saved Configuration 后视图没变 → 该项改动需重启 Topology 应用
- 非相关告警想上图 → Topology 机制不支持，不硬做

输出契约：Standard 视图配置记录 + Custom 视图文件（元素/链接/重定向清单）+ 背景地图目录清单 + 验收演示记录。

## B — 边界

- Topology 只显示相关告警；自动清除依赖 PCX 检测问题结束，人工 clear 在 Alarms 应用完成
- Bubble/Highlight 两种直接标注模式仅告警提示样式差异，不改变只显相关告警的边界
- 地图规范（gif/尺寸/目录）之外的 GIS/第三方地图集成在书外
- 实验背景图（EUROPE.gif/FRANCE.gif）与 rstcpl 触发为实验口径，见 book/overview
