# OXE 呼叫服务器单版本全加载与加载后初始化

## R — 原文依据

> "Depending on the call server type, the initial request can be: • BOOTP (CS and CPU Crystal) • DHCP (Appliance Server)"（p60）
> "Command grubboot ETHER System will ask your confirmation. Disk have to be reinstalled after reboot."（p89）
> "WARNING: Configure the role addressing if needed! License are automatically deployed if declared in the S.O.T project If not, restore the license files manually"（p63）
> "password string must have a minimum of 14 characters ... password must be different from the last twenty-four used passwords"（p91）

出处：ENTPXTE402EN p49-92、p204-211（ESXi 虚机线同理）。

## I — 自述

单版本全加载是核心交付动作，其余加载场景由此派生。SOT 核心就是一台含 DHCP+FTP 服务的虚机，加载时序固定：

1. **网络引导**：CS 网络引导后发 BOOTP（CS/CPU Crystal）或 DHCP（Appliance Server）请求，SOT 交付 IP 配置与引导文件（CS=startup.txt、AS=pxeloader、Crystal 无）
2. **TFTP 下载**：CS 用 TFTP 取文件清单与 Linux RAM，入内存自动启动
3. **FTP 安装**：经 FTP 自动安装 Linux、传工具与 swinst、下载版本与补丁，结束后 CS 重启

启动相位链（加载失败定位底图）依次经过六相位：BIOS、系统自检、Bootloader、GRUB、Linux（从 active 分区启动）、电话应用。可干预点：BIOS 相位选引导设备；GRUB 相位 grubboot ETHER 改走网络引导；电话应用由 swinst 的 autostart 决定自动起或 mtcl 手动 RUNTEL。

硬盘双分区结构（多版本/切换的结构依据）：活动分区（/、/usr2 版本、/usr3 数据库、/var 日志）；公共区（/usr4 动态计费与补丁中转、/usr7 系统语音）；非活动分区（/root2_d、/usr5、/usr6、/var2）。

加载后初始化两件硬规则：

- **密码规则九条**（root/mtcl/adfexc/swinst 四账户逐个设）：≥14 字符；≥2 字母（1 大写强制）；≥2 数字；≥1 特殊字符；不含账户名；不含 4 连同字符；不含 4 连顺序字符；不含字典词；不得与前 24 个已用密码重复
- **密码 aging**：取值 <10<X<366、0=不限期（答 0 触发 CIS_Benchmark_Req.No_5.6.1.1 警告，生产对 root 保留 aging）
- **角色寻址与许可**：SOT 项目不管角色寻址（csm 地址按需在 netadmin 配）；许可未随项目声明时须手工恢复到 /usr4/BACKUP/OPS 再 swinst 恢复

## A1 — 书中案例

**CS3 单版本全加载**（p83-92，How-To）：

1. OXE 版本 iso 传到 SOT 本地存储并 Declare media
2. Easy 模式新建 Greenfield 项目，产品类型选 OXE
3. 项目设置国家/时区；目标设置机型 CS-3、主机名、CPU IP、MAC
4. Verify 后 Deploy，SOT 进入等待目标机状态
5. 目标机 root 执行 grubboot ETHER 确认 y（或 BIOS 菜单选 Ethernet）
6. SOT Web 进度条观察至项目状态 completed
7. 加载后选键盘，为四账户设密码与 aging，出现 CSa login: 即完成

**空盘与已装盘的分界**（p57）：空盘自动进 Standard Installation；盘已有内容必须 grubboot 或 BIOS 强制网络引导。

## A2 — 未来触发

使用情境：全新 OXE 装系统；加载完 "completed" 了系统还差什么；密码设不上；SOT 一直等目标机；加载卡在某个阶段。

语言信号：单版本 / mono version / full release / grubboot ETHER / BOOTP / startup.txt / Standard Installation / 加载后 / RUNTEL / autostart / siteid / 角色寻址 / role addressing。

与相邻能力区分：

- 装第二版本与补丁 → 补丁与多版本卡
- 客户现场不让架 SOT → 分发器模式卡（路由）
- 加载的是虚机 → 虚拟化交付卡

## E — 可执行步骤

输入契约：目标机机型与 MAC、SOT 就绪（同网段）、OXE 版本 iso、许可文件（可随项目）、客户国家码/时区/地址规划。目标机已装系统且无法进系统 → 走 BIOS 强制引导。

1. 传媒体并声明：iso 上传 SOT 本地存储，Refresh 后 Declare。完成标准：媒体出现在版本列表
2. 建项目：Easy 模式 Greenfield 选 OXE，填国家/时区。完成标准：项目字段完整
3. 目标设置：机型/主机名/CPU IP/MAC（物理机必填，NAS Excel 或 ifconfig 取）。完成标准：Verify 通过
4. Deploy 后引导目标机：grubboot ETHER 确认 y，或 BIOS 选 Ethernet。完成标准：SOT 捕获目标机开始加载
5. 等待 completed：SOT Web 进度条走完。完成标准：项目状态 completed
6. 加载后清单：键盘、四账户密码与 aging、角色寻址（按需）、许可恢复（未随项目时）、swinst 输国家码、日期时间、板卡上线、建用户或恢复备份。完成标准：siteid 显示目标版本且出现登录提示

判停点：

- SOT 长时间等待目标机 → 停，先查是否已装盘没走网络引导（最高频原因）
- 密码总被拒 → 停，对照九条规则逐条核（实验值 Superuser2580* 满足全部约束）
- completed 后直接交机 → 停，角色寻址与许可两件事 SOT 不代做，逐项过后置清单

输出契约：加载完成且初始化到位的 OXE（siteid 版本正确、四账户密码受控、许可与信任主机就绪）。

## B — 边界

- 本卡只管"装上去"：数据库与业务配置（用户/路由/编号计划）指向 Starter 课程或"restore a backup"（p92）
- aging=0 仅培训口径；生产按 CIS 基线对 root 保留 aging，并替换全部实验口令（p91/p175/p273）
- V24 链路用于启动与检查安装（p52）；加载观察可经终端模拟器
- 加载后密码 aging 提问的合法区间是 <10<X<366；0 表示不限期
- 实验口径：CSa=192.168.1.101、csm=192.168.1.103——生产按客户规划替换
