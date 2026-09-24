# OXE 多版本加载、分区切换与静态/动态补丁管理

## R — 原文依据

> "Static patch: • They can only be installed with the phone shut down or when installation is on the inactive partition ... Dynamic patch: • They can be installed on the active or inactive partition with the phone running"（p65）
> "A patch (static or dynamic) includes all of the previous patch corrections • The patch N420536 includes the patches 1 to 36 corrections"（p66）
> "STATIC PATCH INSTALLATION ON ACTIVE PARTITION REQUIRES TO STOP THE TELEPHONE APPLICATION. SO, SYSTEM IS REBOOTED AUTOMATICALLY"（p104）
> "N: Product line ... 205: Software version 36: Static patch # a: Dynamic patch identification N420536a"（p53）

出处：ENTPXTE402EN p50-110、p93-99（多版本 How-To）。

## I — 自述

双分区是 OXE 升级的安全模型：同一块盘同时驻留两个版本（active/inactive），装第二条版本不打断话音，"切换"才重启，出问题可回退。多版本两分支：

| 分支 | 适用 | 步骤 | 例 |
|---|---|---|---|
| 复制+补丁 | 基础版本相同 | active 整体复制到 inactive → 在 inactive 装补丁 → 切换 | N4.205.19 改 N4.205.36a |
| 完整加载+数据复制 | 跨 Linux 版本 | inactive 装完整新版本，复制 OXE/Linux 数据，自动重启切换，按需装新 OPS | N3.521.12 改 N4.205.36a |

版本命名三套互相咬合：

| 命名对象 | 格式 | 读法 |
|---|---|---|
| 软件发布名 | N420536a | N=产品线（R100 系）、4=线内选项（R101.1）、205=软件版本、36=静态补丁号、a=动态补丁标识 |
| SOT 媒体名 | ISO=A.B.XXX.000 / zip=A.B.XXX.YYY | XXX 为所基于 ISO 序号，YYY 为 zip 序号 |
| siteid 全串 | R101.1-n4.205-36-a-fr-c83 | 业务标识-交付-静态补丁-动态补丁-国家-CPU 类型 |

补丁顺序律四条：

1. 静态补丁只能停话音装（active 分区，装完自动重启）或装在 inactive 分区，且必须在对应完整版本之后
2. 动态补丁可热装（active/inactive 皆可、不打扰运行），但必须排在同版本静态补丁之后
3. 补丁累积包含此前全部修正——装最新即得全部
4. 文件形态：zip 通常一包一补丁（静/动分两次装）；iso 可静+动同装一次完成

SOT 多版本项目关键字段：

- Update on inactive partition（勾）；Duplicate OXE Data / Duplicate Linux data（自动复制）
- Switch partition after update installation；Switch time（定时切换）；Switch back（按天回切）；Use a clean inactive partition

手工等价路径在 swinst：2-3-2 分区复制（5 Duplicate all 最常用）、2-3-3 切换；swinst 8-2 查两分区版本（0=active、1=inactive）。切换后首次进 swinst 必须输国家码。

## A1 — 书中案例

**补丁双场景实验**（p100-110，How-To）：

1. 声明补丁媒体（zip 或 iso）到 SOT 本地存储
2. siteid 查当前版本（实验起点：patch 0、Linux 601.007）
3. 场景 A 装 active：项目 update 不勾 inactive 分区，静态补丁触发自动重启
4. completed 后 siteid 复核（实验：静态补丁 19 后 Linux 601.012）
5. 场景 B 装 inactive：先 swinst 2-3-2-5 Duplicate all，ver2cho visible 与 df -v 核对两分区一致
6. SOT update 勾 Update on inactive partition，按需设 Switch time 与 Switch back
7. 切换后 siteid 复核（实验：Linux 601.017、Patch version 36）

## A2 — 未来触发

使用情境：升级不停机怎么做；打补丁要不要停机窗口；回退老版本；多版本怎么装；补丁顺序报错；动态补丁装完话机行为没变。

语言信号：多版本 / multi version / inactive partition / active partition / Duplicate all / Switch partition / Switch time / Switch back / 静态补丁 / dynamic patch / N420536 / siteid / downstat / 回退 / rollback。

与相邻能力区分：

- 首次装系统 → CS 加载卡
- 无 SOT 环境的替代路径 → 分发器模式卡（路由）
- 版本迁移低于 N3 → 本卡 Boundary

## E — 可执行步骤

输入契约：当前版本（siteid）、目标版本/补丁号、维护窗口（静态补丁必给）、SOT 与媒体就绪。跨 Linux 大版本 → 走分支二并预留数据复制时间。

1. 查版本：siteid 或 mtcl 登录横幅确认当前补丁号。完成标准：起点版本明确
2. 选分支：同基础版本选复制+补丁；跨 Linux 选完整加载+数据复制。完成标准：分支判据成文
3. 场景 A（active）：项目 update 不勾 inactive，静态补丁排停机窗口。完成标准：completed 且 siteid 推进
4. 场景 B（inactive）：先 Duplicate all 复制，ver2cho/df -v 核对一致。完成标准：两分区一致
5. 装 inactive 补丁/版本：勾 Update on inactive partition，按需设 Switch time/Switch back。完成标准：completed、未影响话音
6. 切换与复核：按计划切换重启，swinst 首进输国家码，siteid 核对。完成标准：目标版本生效
7. 动态补丁收尾：downstat d（板卡）/ i（IP 话机）/ t（40x9 话机）跟完下载。完成标准：无待下载对象

判停点：

- 动态补丁报"版本不存在或静态缺失" → 停，先装同版本静态补丁再装动态（顺序律）
- Duplicate all 失败 → 停，退回"对 inactive 做完整版本加载"的备用路径（p106 Warning）
- 客户要求回退 → 提示板卡可能已拿新二进制，回退要再下载一轮，排窗口
- 来源版本低于 N3 → 停，多版本机制不可用，按 TC3104en-Ed08 重格式化迁移

输出契约：双版本在盘、补丁链正确、siteid 可验的升级记录（含切换时间与回退预案）。

## B — 边界

- N3 以下迁移硬规则：必须重格式化、盘 ≥80GB、RAM ≥1GB、/root 与 /root2_d ≥3.5GB、多版本与切换整体不可用（p78）
- 切换期间板卡可能接收新版本二进制——回退不是零成本瞬时操作（p72）
- 补丁加载最多两步：step 1 全系统公共文件、step 2 国家相关文件（p66）
- 实验口径：补丁链 0→19→36（Linux 601.007/601.012/601.017）为演示值，现场以实际补丁包为准
