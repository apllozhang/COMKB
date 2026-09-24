# 空数据库与 OPS 许可（建库顺序、许可恢复、FlexLM、降级模式）

## R — 原文依据

> "The OXE database is called MAO (Maintenance Administration Operation)"（p186）
> "THIS OPERATION OVERWRITES THE EXISTING DATABASE AND THE SOFTWARE LICENSE FILES. IT CAN ONLY BE PERFORMED IF THE TELEPHONE APPLICATION IS STOPPED."（p190）
> "The OPS files are the following: • hardware.mao • xx.swk • Contains the listing of customer licenses and software locks • xx.hw • xx.zip"（p196）
> "the Call Server checks its OPS files every five days … postpones the degraded mode procedure for 30 days"（p205）

出处：ENTPXTE400EN p184-223。

## I — 自述

库与许可是一对：MAO 存配置，OPS 存许可；两者通过固定顺序绑定：

1. **空库三连约束**：只能在话务应用停止时执行；必然连现有库与许可文件一起覆盖；完成后必须先恢复 OPS 再重启、再起话务
2. **空库流程**：Easy 7 停话务；Expert 菜单 7（Database tools）选 2 建空库；输国家码（培训约定 FR 为实验口径，现场必须真实国家码）；Direct Link Network 选 Y 自动建 99 条 ABC-F 直连；记录空库上限后重启 CPU
3. **OPS 四文件**（xx=客户 ID）：xx.swk（许可+锁清单）、xx.hw（硬件描述）、hardware.mao（兼容副本）、xx.zip（Actis 归档）；恢复路径=传 /usr4/BACKUP/OPS 后 swinst 恢复，.swk 运行态改名 software.mao
4. **许可 ID 四态**：CPU-ID（物理 CS，PROM 内）/ Product ID（虚拟 CS，FlexLM .ice 绑加密狗）/ ALU-ID（GAS 免狗）/ CC-SUITE-ID（Cloud Connect，终身不变，全载体通用）
5. **锁值语义**：0/1=服务授权；0-99999=数量；99999=无限。spadmin 十项菜单管查看/校验/安装/CPUID/PANIC
6. **保护节奏**：正常每 5 天自查 OPS；不一致即降级——CPU-ID 类视为维护操作给 30 天宽限；降级三阶段=即时话务台告警+命令报 "Software protection error"，4 小时后全屏提示并禁内呼，8 小时循环
7. **FlexLM 对接**：WBM System/Licenses 配 Enabled/服务器 IP/端口 27000/Product ID discovery，改后必须重启 CS

## A1 — 书中案例

**空库创建实验**（p189-193，How-To）：

1. swinst Easy 7 停话务，系统重启且 autostart 取消
2. Expert 菜单 7 Database tools 选 2 建空库，确认抹库警告
3. 输国家码 FR（实验口径），Direct Link Network 选 y 自动建 99 条直连
4. 记录空库上限（Users 10014/1/2 com 3859，实验库实例值）
5. shutdown -r now 重启 CPU
6. 恢复许可（见下一段实验）后 Easy 8 起话务
7. 验证：ednump 可见 FR 库默认编号计划（51/41/42/43 等）

**OPS 恢复与巡检实验**（p210-223，How-To）：

1. FileZilla 设 Binary 传输，SFTP 把 xx.hw/.swk/.zip/hardware.mao 传到 /usr4/BACKUP/OPS
2. swinst Expert 菜单 5（OPS configuration）执行恢复，同意新软件密钥
3. 观察输出："30 remaining day(s)" 为 CPU-ID 宽限提示，"operation successful" 为成功
4. 同菜单备份 OPS 到 /usr4/BACKUP/OPS 并传回 PC 存档
5. 虚拟环境在 WBM System/Licenses 配 FlexLM（IP/端口 27000），重启 CS
6. spadmin 巡检：选 3 显示 File OK，选 10 显示 FlexLM check OK
7. 核对锁计数与许可文件一致（SIP users、OMS 通道等）

## A2 — 未来触发

使用情境：系统重置/交付前初始化；许可丢失或换机后恢复；"Please call your administrator" 全屏提示；软件保护告警；虚拟机/GAS 对接 FlexLM；spadmin 校验。

语言信号：空库 / empty database / MAO / OPS / swk / 许可 / license / 软件锁 / spadmin / PANIC / 降级 / degraded / FlexLM / CPU-ID / CC-SUITE-ID / 宽限。

与相邻能力区分：只备份不重置见备份恢复能力（路由卡）；建库后配网络见 CS 网络与防火墙能力；许可计数影响媒体资源见网关上架能力。

## E — 可执行步骤

输入契约：目标国家码（现场真实值）、OPS 许可文件（交付渠道获取）、载体类型（物理/虚拟/GAS）与 FlexLM 信息（如适用）。OPS 文件缺失时停，先走商务渠道，不要用别站点的文件顶替。

1. 备份现状：停话务前先做库与 OPS 备份并传离设备。完成标准：回退点在 PC 上
2. 停话务：swinst Easy 7（autostart 连带取消，知晓即可）。完成标准：role 显示停止
3. 建空库：Expert 菜单 7 → 2，输入真实国家码，按需选 Direct Link。完成标准：空库上限显示且记录
4. 重启后恢复 OPS：Binary 传四文件到 /usr4/BACKUP/OPS，swinst 恢复并同意密钥。完成标准：输出 operation successful
5. 起话务并验证：Easy 8，等 "No problem with compatibilities"；spadmin 选 1 看 PANIC 归零、选 3 校验 File OK。完成标准：许可计数非 0 且校验通过
6. 虚拟/GAS 场景配 FlexLM：WBM System/Licenses 四参数，重启 CS，spadmin 选 10 判读 OK/NOK。完成标准：FlexLM check OK
7. 巡检移交：spadmin 锁清单与商务订购单对照。完成标准：许可台账闭环

判停点：

- 恢复 OPS 后仍提示 "Illegal hardware key" → 停，文件与本机 ID 不匹配，回交付渠道核对订购的 CPU/Product/ALU-ID
- 出现 "30 remaining day(s)" → 宽限期内必须换上匹配许可（n10），到期进入降级，明确告知客户时限
- 话务台已报 "Software protection error" 且 4 小时已过 → 已禁内呼，按降级流程优先恢复 OPS 而非排障话务
- 客户要求"只重置配置不丢许可" → 停，空库必然连 OPS 一起抹（n09）；改为备份 OPS 后再建库的顺序方案

输出契约：按目标国家码初始化且许可生效的系统 + spadmin 校验记录 + 许可台账。

## B — 边界

- 培训统一 FR 国家码、空库上限数值均为实验口径（nr-04）；现场必须真实国家码
- Actis 订购流程、FlexLM 服务器搭建（CPU Loading 课程）、Cloud Connect/RTR 深度（ENTPXTE402）在书外
- 非法解锁软件保护属违法且有法律风险（p204 原文警示），本卡只做合法恢复路径
- spadmin 的 OPEX Flag/Panic RTR Check 等旗标判读以 spadmin 输出为准；OPEX（Purple on Demand）商务前提在书外
