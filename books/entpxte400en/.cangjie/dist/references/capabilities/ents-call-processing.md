# 呼叫处理业务域（语音指南/MOH、话务台与 4059EE、Entity/CDT、分配计时器）

## R — 原文依据

> "GD4, GA4 (ADPCM32 codec) • 4 x 8 minutes for static guides • 1 x 8 minutes for dynamic guides • 16 simultaneous accesses • OMS … 120 simultaneous accesses"（p428）
> "Note: Even with one attendant a group has to be created because AN ATTENDANT SET MUST BELONG TO A GROUP"（p451）
> "4 different 'call distribution' status … A fourth 'overflow number' is common to the 4 status … commonly called 'night forwarding number'"（p500）
> "Timer 141: 30'' by default … Timer 76 : 80'' by default"（p701）

出处：ENTPXTE400EN p425-525, p700-719。

## I — 自述

内部呼叫处理四大件，彼此独立但共用编号计划与实体：

1. **静态语音指南**：载体 GD4/GA4=4 静态槽+1 动态槽、16 并发，OMS 同槽位 120 并发；每个指南索引挂 8 条语言消息；动态消息同索引覆盖静态；试听=拨 580+4 位指南号（需 COS 放行）
2. **MOH 激活固定二步**：删 Tone 2（默认等待音）+建 VG 2（Single-message 按语言或 Music On Hold 全语言同曲）；自制 MOH 放 custom 目录同名替换
3. **话务台三层**：Attendant group（每节点 ≤50 组，并行/轮转呈现）+Attendant set（≤250/节点，必须属组，Idle/Busy/Unplugged/Absent）+终端（ALE 话机或 4059EE PC 坐席——只管操作不管语音，必须关联话机/IPDSP，禁 multiline）
4. **Entity/CDT**：逻辑分区 0-1000（用户默认归 1、中继默认归 0）；CDT=四状态各 3 个顺次路由号+公共溢出号（必须单线分机）；状态由小时表（每天 ≤4 切换点）或 Attendant Group Manager 驱动
5. **计时器七件套**（单位 100ms）：76=800（话务台 80 秒转 Absent/溢出）；141=话务台 Normal 转 Urgent（30 秒）；144=150（内呼用户段 15 秒）；140/142=15 秒延迟振铃；102=0（≠0 才播话务等待指南）；trunk COS 溢出 300（外线用户段 30 秒）；Entity Overflow Timer 默认 0

| 计时器 | 默认值 | 作用段 |
|---|---|---|
| 76 | 800（80 秒） | 话务台无应答转 Absent/溢出 |
| 141 | 30 秒 | 话务台 Normal 转 Urgent |
| 144 | 150（15 秒） | 内呼的用户段振铃 |
| 102 | 0 | 话务等待指南触发门 |
| trunk COS 溢出 | 300（30 秒） | 外线在用户段的溢出 |
| Timer 4 | 150（15 秒） | 默认无应答呼转 |
| Timer 23 | 30（3 秒） | 前缀歧义消解 |

## A1 — 书中案例

**语音指南与 MOH 实验**（p439-448，How-To）：

1. FileZilla 把 vgadpcm.FR0/EN0 与 adpcmmoh 传到 /DHS3ext/vgadpcm/flash/std
2. WBM 核对语言索引（Index1=法语、Index2=英语）
3. 板卡 Voice Guide Index 把内存槽与语言索引关联（Slot3 放 MOH）
4. System/Tones 删除 Tone 2，再新建 VG 2 绑定保持音乐
5. 实体等待指南确认为 VG 2
6. vgstat 巡检：两语言+MOH 已入槽，动态区余量正常
7. 话机拨 580 0002 试听 MOH，通话保持验证音乐生效

**话务台与 Entity 实验**（p479-525，How-To）：

1. 建话务组（Physical DN=A0000，溢出门限 5），组 CDT 自动生成
2. 建话务语音用户 31003（禁 multiline）并关联 4059EE 坐席 B0000
3. 4059EE 装机后以 B0000@CS 地址连接，Sign on 上线
4. 配系统参数：4059 Close auto sign off 与 PC unregistered at logoff
5. 实体 1 挂经理组 A0000，状态小时表全部跟随 Attendant Group
6. 拨话务组前缀验证白天振铃话务台，Sign off 后落溢出号 31000
7. 计时器实验：改 76/144/Entity Overflow 后内外线溢出时序按新值变化

## A2 — 未来触发

使用情境：前台话务台部署；保持音乐不生效；多语言指南部署；夜间/节假日自动切换；话务台无应答转 Absent；溢出太慢/太快调时序；等待指南播放条件。

语言信号：语音指南 / voice guide / MOH / 音乐保持 / 话务台 / attendant / 4059 / BLF / Entity / CDT / 夜转 / 溢出 / Timer 76 / Absent / 等待指南 / 状态切换。

与相邻能力区分：外呼区域闭锁走 Public COS，见闭锁与紧急能力（路由卡）；留言转语音信箱见 4645 能力（路由卡）；前缀定义见编号计划与 COS 能力。

## E — 可执行步骤

输入契约：部门结构与话务量、录音素材（语言/音乐）、话务员排班、溢出目标号码（单线分机）。溢出号必须单线，多线分机选型先回头。

1. 部署指南与 MOH：传文件、关联槽位、删 Tone 2 建 VG 2、580 试听。完成标准：试听与保持音乐生效
2. 建话务体系：话务组、话务语音用户（单线）、4059EE 坐席与关联话机。完成标准：Sign on 后 grpopestat 显示 PRESENT/DAY
3. 配 Entity：用户/中继归组、经理组、状态小时表、CDT 路由与溢出号。完成标准：状态切换按预期路由
4. 调计时器：System/Timers 按话务体验调 76/144/102 与 trunk COS 溢出值。完成标准：内/外线溢出时序达标
5. 授切换权：话务台实体状态四态权限与 EMG 类软键按需开放。完成标准：话务员可手动切实体状态
6. 回归验证：白天/夜间、内线/外线、有应答/无应答全矩阵拨测。完成标准：路由结果与设计表一致

判停点：

- 话务台"没反应" → 先查是否 Absent 态（80 秒无应答自动转，n23），控制台恢复 Available 再复测
- 4059EE 接不了电话 → 它只管操作，声音走关联话机/IPDSP（n24）；关联分机多线则必改单线
- 内呼听不到等待指南 → 查 "Play VG for Internal Caller"=True 且 Timer 102≠0，两个条件缺一不可
- MOH 不生效 → 激活二步没做全（删 Tone 2+建 VG 2），回 WBM 补操作

输出契约：生效的指南/MOH + 可用话务台 + Entity 路由矩阵 + 计时器调参记录。

## B — 边界

- 实验前缀 31400/31401/31100、溢出号 31000 等为实验口径；录音内容制作与版权在书外
- 4059EE 的 PC 防火墙要放行程序与 abcacom.exe（n24）；培训环境关防火墙是权宜之计
- Rainbow 侧话务台（Attendant 订阅/监督组）属 Rainbow 集成教材，与本卡 OXE 原生话务台分属两套体系
- ACD/呼叫中心（agent/队列统计）不在本书范围；BLF 用户监视 ≤5 设备聚合
- 计时器单位均为 100ms 步进；WBM 里 800 即 80 秒（p711）
