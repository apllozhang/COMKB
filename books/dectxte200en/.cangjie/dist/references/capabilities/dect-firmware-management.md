# DECT 固件双轨升级管理（基站 downstat x / 手机空中 FWU downstat m）

## R — 原文依据

> "When the call server has some free resources, it requests an xBS to start downloading the new firmware on its RAM in background. So that it is still running for handsets calls. After successful download and when base station is idle, the call server restarts them"（p130）
> "Minimum firmware version: v73b0003"（p131）
> "The Audio communication is preferred over downloading. That means that a software download is stopped during an audio communication and will resume later ... The handsets switch on the new downloaded software version when they are put on a charger cradle"（p179）
> "The theoretical duration of a download is between 6-8 hours"（p181）

出处：DECTXTE200EN p129-133, p178-190。

## I — 自述

固件分两轨管理，命令族同源（downstat）但对象与机制不同：

1. **基站轨（downstat x）**：TFTP 后台下载到 RAM（不中断业务，旧软件继续跑），空闲时重启切新软件；最低固件 v73b0003
2. downstat x 菜单四项：1 启动下载 / 2 下发 Flash and Reset（按 site/pari 选择并二次确认）/ 3 恢复 legacy 模式 / 4 重试 DOWNLOAD_FAILED
3. 自动复位策略：Allow auto. Reset after update=YES（成功即自动重启）或 NO（手工经 downstat x 控制窗口）
4. **手机轨（downstat m）**：空中 FWU。单手机同一时刻仅一条数据信道、语音优先（下载暂停续传）；新版本**回充电座时**才切换生效；理论单机 6-8 小时；二进制在 /usr2/downbin（bin8212…bin8262EX）

downstat m 状态判读（p186）：

- 模式三值：A（自动）/ X（排除自动）/ M（手工经菜单 4 触发）
- 状态六值：IDLE、ERASE REQUESTED（提示 charger required）、WRITING、PAUSED（等待续传）、WAIT FOR FLASHING（必须回充电座重启生效）、ERROR（自动模式失败稍后重试）

手动下载前置：用户参数 "Exclude from automatic FW update"=Yes（p188 口径，见 needs-review nr-03）。

## A1 — 书中案例

**基站固件升级操作**（p129-133）：

1. downstat x 看表头 system binary version（实验输出 V0073B0014）与各站 Download status
2. 选 1 启动后台下载，盯状态 IN_PROGRESS → READY_TO_FLASH → UP TO DATE
3. 全部 READY 后选 2 下发 Flash and Reset（选 site/pari、二次确认）
4. 自动复位开关按窗口策略选 YES/NO；DOWNLOAD_FAILED 用选项 4 重试
5. 升级完成后选项 3 恢复 legacy 模式

**手机 OTA 操作**（p183-189）：downstat m 菜单（1 版本 / 2 状态 / 3 可下载清单 / 4 下载单机 / 5 取消）；批量 downstat m n <列表>；指定二进制 downstat m b <binary> n <列表>。

## A2 — 未来触发

使用情境：基站批量升固件；升级窗口怎么定；手机版本参差不齐；手机升完没生效；某台手机要指定版本；固件下载一直 PAUSED。

语言信号：downstat / downstat x / downstat m / 固件 / firmware / FWU / SUOTA / OTA / READY_TO_FLASH / Flash and Reset / 充电座 / cradle / /usr2/downbin / v73b0003 / 版本升级。

与相邻能力区分：基站部署时的固件前提见 IP-xBS 部署能力；重注册前的版本门槛见自动重注册能力；固件下载不动的网络面排查见维护排障（路由）。

## E — 可执行步骤

输入契约：目标版本与二进制（/usr2/downbin 就位）、升级窗口、机型清单（手机轨）。TFTP/DHCP 未通 → 先回部署能力。

1. 盘版本：downstat x（基站）或 downstat m 菜单 1（手机）拉当前版本表。完成标准：版本台账成型
2. 定策略：基站选自动复位 YES/NO；手机确认 FWU 支持（不支持走 UST+USB）。完成标准：窗口与方式确定
3. 批量下发：downstat x 选 1；手机 downstat m n <列表> 或菜单 4。完成标准：下载任务铺开
4. 盯状态：基站盯 READY_TO_FLASH；手机盯 A/X/M 与六态（PAUSED 属正常暂停续传）。完成标准：全部就绪态
5. 切换生效：基站 Flash and Reset（或自动复位）；手机回充电座重启。完成标准：版本表刷新
6. 收尾：downstat x 选 3 恢复 legacy 模式；核对异常清单。完成标准：无遗留 DOWNLOAD_FAILED/ERROR

判停点：

- 升级窗口内话务高峰 → 基站下载不中断业务但重启会断该站话务，选空闲窗口；手机语音优先会拖慢下载，按 6-8 小时/机排过夜
- 手机 WAIT FOR FLASHING 迟迟不生效 → 没回充电座，催收充电座，不要重复下发
- 主备 CPU 倒换期间 → 全部下载停止、恢复顺序不保证（p181），避开 CPU 维护窗口
- 访问节点上的手机不下 → 多节点网络的固有限制，等回安装节点

输出契约：版本升级台账（前后版本对照）+ 失败清单与处置记录。

## B — 边界

- p182 Note 的"bone"为原文笔误、参数名未写全，以 p188/p189 的 "Exclude from automatic FW update"=Yes 口径为准（needs-review nr-03）
- 6-8 小时是理论单机时长，实际随话务浮动；书内无实测分布（待确认）
- 8244/8262 可预留 2 信道做告警（p58），会进一步压缩话音容量，与固件管理并行考虑
- 基站固件与 OXE 版本配套关系书内只给最低值 v73b0003 与 R12.2，完整配套矩阵在书外
- 手动 USB 升级（UST）操作步骤在书外，仅给前提与路径
