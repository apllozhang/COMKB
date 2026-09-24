# MSAD 插件开户（AD 右键一键开通 8770/OXE 用户）

## R — 原文依据

> "A specific plug-in must be created in OV8770, then installed in MSAD server ... The MSAD plug-in enables to launch the web tool from the Active Directory ... Creates user in 8770 server, OXE and/or OT server"（p365）
> "If 'Directory number' field is empty, selected telephone number will be the one automatically generated"（p364）
> "If the URL 'nms.company.com' is not a trusted site, the plug-in will display its interface with missing fields."（p414）
> "Only the cost center and Salutation field (when available) can be modified."（p425）

出处：8770XTE202EN p363-366, p394-426。

## I — 自述

MSAD 插件（Alcatel-Lucent Unified User Management）是第三条开户通道：装在 AD 服务器上，管理员在 AD 用户右键按 Meta profile 一键开通 8770 目录用户+Users 应用用户+OXE 用户。与"定时同步"通道互补，属管理员手动开户。

- **调用链**：8770 侧 MSAD Management > MSAD > Mapping 右键 Create > ADPlugin 生成 8770MSADPlugin.properties（内含 URL/DN/加密密码/映射 DN/AD 账号）→ 三文件经 SHARING 中转到 AD 服务器 %LOCALAPPDATA% → setup.exe 安装后 AD 右键出现插件菜单
- **前置三件**：MSAD8770Admin 账户改密（改后必须重启 NMC Java Service Definition 服务，否则插件拿旧密码失败）；OXE 空闲号码段（建完必须同步取回，不同步取不回）；Users 应用 Meta profile（OXE 节点+号码段+话机类型+OXE profile+COS）
- **IE 三前提**：信任站点加 nms.company.com（否则界面缺字段）；允许"我的电脑"上的活动内容；IE9 另需 active scripting
- **开户行为**：Directory number 留空自动取段内首个空闲号；首次调用要装证书到受信任的根；更新用户仅 Cost center 与 Salutation 可改；删除为确认后直删
- **排障**：插件日志在 AD 服务器 %TMP%\start8770webclient.log

## A1 — 书中案例

**插件部署与开户实验**（p394-426）：

1. OXE 建 profile 型用户 A0001：Profile Name=BASIC，Rights 配 COS 3/4/5（实验口径）
2. System 下建空闲号段 Range 31050-31059，同步 OXE 后核验段列表
3. Users 应用建 Meta profile：oxe 节点+号段+8078s+BASIC
4. Security 应用改 MSAD8770Admin 密码，Service Manager 重启 NMC Java Service Definition
5. Mapping 右键 Create > ADPlugin 生成 properties（生成路径见 I 段）
6. 三文件拷 SHARING，Ecosystem 实例取到 %LOCALAPPDATA%
7. 管理员运行 setup.exe 安装并注销重登
8. IE 信任站点加 nms.company.com，允许本机活动内容
9. AD 右键 Christopher Cane 调插件，首次装证书到 Trusted Root
10. AD 建 Cesar Ciudad 后右键插件，Meta profile 选 8078s，Create
11. 确认框显示用户名与分机号（自动取段内首个空闲号）
12. Directory 与 Users 应用双核验人员、主链接与用户参数

## A2 — 未来触发

使用情境：帮助台想在 AD 里直接开户；插件装完右键菜单没有/界面缺字段；开户报密码错；号码没自动分配；插件里能不能改名；AD 服务器要不要装什么浏览器。

语言信号：MSAD 插件 / MSAD plug-in / Unified User Management / Meta profile / ADPlugin / 空闲号段 / MSAD8770Admin / 信任站点 / trusted sites / 右键开户 / start8770webclient。

与相邻能力区分：

- 定时批量同步 → MSAD/Azure 管道能力
- Meta profile 依赖的号码段来自 OXE 同步 → OXE 注册能力
- 开户后的链接/CC 调整 → 链接与改名能力

## E — 可执行步骤

输入契约：AD 服务器管理权、MSAD 管道已声明（MSAD/Azure 管道能力）、OXE 可同步、目标话机型号与 profile。IE 前提无法满足且现代浏览器不可用 → 判停标风险（nr-06）。

1. 建 OXE profile 与 COS（大写 BASIC 等）。完成标准：profile 就绪
2. 建空闲号段并同步 OXE（不同步取不回，p401 警告）。完成标准：段列表可查
3. 建 Meta profile：节点+号段+设备类型+profile。完成标准：模板可选
4. 改 MSAD8770Admin 密码并重启 NMC Java Service Definition。完成标准：服务已重启
5. 生成 properties 并经 SHARING 中转到 AD 服务器。完成标准：三文件到位
6. AD 装 setup.exe，配 IE 三前提，首次调用装证书。完成标准：右键菜单可用
7. 开户验证：右键目标用户按 Meta profile Create，双应用核验。完成标准：人员+用户+主链接齐

判停点：

- 插件界面缺字段 → 先查信任站点/活动内容/active scripting 三项（n26），不要重装插件
- 开户失败提示凭据 → 改过 MSAD8770Admin 密码但没重启 NMC Java Service（n27）
- 号码没自动取 → 号段建了但没同步 OXE（p401），先同步再试
- 客户要求用插件改名/改号 → 能力不支持：仅 Cost center 与 Salutation 可改（n28），引导到 Users/WBM 入口
- 目标环境无 IE 且不兼容 → 向客户声明版本风险（nr-06），评估替代开户路径后再上插件

输出契约：AD 侧一键开户能力（插件+Meta profile）+ 前置三件核验记录 + 开户与更新边界说明。

## B — 边界

- IE 强依赖（nr-06）：Ed40 口径在现代浏览器/新 Windows 下需先实测，作为交付前置核查风险项
- properties 文件含账户 DN 与"加密"密码且原样印刷于书（nr-08）：生产必须换密并控制文件访问
- 更新能力极窄（仅 CC+称谓）、删除为确认后直删：向帮助台交底时不夸大
- Meta profile 留空 Create 只建目录用户不开 OXE 用户（p424 Add-on）
- 本书流程基于 Windows Server 与 IE9 时代环境（实验口径），浏览器演进后需重估
