# ASM 脚本与 LCA 主干（编辑器安装、脚本生命周期、调试器、记忆路由）

## R — 原文依据

> "If the CCsupervision application is already installed, you can't reuse the executable CCsupervision setup file to add the ASM Script Editor package. You must use the dedicated executable setup file (asm-se_setup.msi)"（p206）
> "When the script is completed, it must be saved & compiled • 2 files will be generated • "Script_name".scr • "Script_name".alb"（p198）
> "Only one script per pilot, or one common script for all pilots!"（p213）
> "The ASM memory is emptied when the ASM process is re-started. • MAIN_AFE re-starting has no effect on the ASM memory."（p252）

出处：OTCCXTE101EN p188-259, p260-292。

## I — 自述

ACR 脚本体系的主干四块（编写深度由姊妹技能 ACR 专题承接，本卡给主干与排障入口）：

**安装与工具链**：装 CCS 时可勾 ASM Script Editor 组件一步到位；CCS 已装后补装必须用专用 asm-se_setup.msi（重跑 CCS 安装包无效）；
编辑器起不来先补 JRE（书示 Azul Zulu 8.72.0.17 32 位，版本可不同）。
入口在 Configurations > Advanced Call Routing > ASM Script Editor；在线模式先 ASM > Connection 填服务器 IP（内置 ASM=Call Server 地址）。

**脚本生命周期**：脚本名 ≤8 字符；积木块入口/出口不得悬空；保存编译生成 .scr（源）+.alb（产物），内置 ASM 存 /usr3/afe；激活时绑定 Pilot——一 Pilot 一脚本，或全 Pilot 公共脚本；换脚本必须重新 Activate。

**调试器**：三窗格（只读图形窗/轨迹控制台/命令窗）；过滤器四模式（CALLING 主叫号须与运营商送达完全一致、CALLED、CALLTAG、无过滤）；Make call 的发起分机必须是普通用户（非坐席非班长）；轨迹可保存；调试器里不能新增积木块。

**LCA 记忆路由主干**：ASM 按主叫记录最后应答坐席、Pilot、时间与 7 种上次呼叫状态（LAST_CALLED_STATE 1-7：劝阻/已应答/互助/GFW/闭锁/等待放弃/振铃放弃）；
脚本范式=IF(有记忆且未超 1 天) 走 LCA 规则（优先级 2、重选 10 秒），否则回落 ISM（优先级 8、20 秒）；
清理记忆必须 kill alb 进程（MAIN_AFE 重启不清），用 adm_acd <ASM IP> -salb option 28 复核。

## A1 — 书中案例

**从安装到 LCA 验证的最短路径**（p204-292）：

1. 专用 msi 装 ASM Script Editor，需要时补 JRE，启动后放行防火墙
2. 连 ASM（192.168.1.3，实验口径），建 ISM 脚本（RULE_ISM+CHARACTERISTICS_LIST）并激活到 Pilot 31603
3. 三路测试：31660 振铃坐席 1、31661 振铃坐席 2、直拨 31603 无档案跑满 21 次走闭锁
4. 建 Reselect 脚本：RULE_ISM + 设 RESELECTION_TIMEOUT=10，右键 Debugger 激活，第二序列等 10 秒出第 2 子列表
5. 建 LCA_1：IF(SEQUENCE=1) 分支 TRUE=PRIORITY 2+超时 10+LCA 规则，FALSE=PRIORITY 8+超时 20+ISM
6. 清记忆：ps -edf|grep alb 找 PID，su - 提权 kill -9，option 28* 复核为空
7. 两通验证：第一通走 ISM 且记忆新增条目，第二通条件 TRUE 走 LCA 规则（p277 轨迹）

## A2 — 未来触发

使用情境：编辑器装不上/起不来；脚本改了行为没变；要用调试器抓路由轨迹；客户要"回头客找原坐席"；LCA 测试前清记忆。

语言信号：ASM Script Editor / asm-se / .scr / .alb / 激活 / Activate / 调试器 / Debugger / Make call / RESELECTION_TIMEOUT / LCA / LAST_CALLED_AGENT / ASM 记忆 / kill alb / option 28。

与相邻能力区分：ISM 算法为什么这样排序转 ISM 技能匹配卡；脚本对象/ Pilot 配置转 ACR 对象卡（路由卡）；**脚本积木块详解、LCA_1/2/3 渐进脚本族、调试器完整实操转姊妹技能 otcc-standard-advanced-call-routing（ACR 专题）**。

## E — 可执行步骤

输入契约：CCS 已装、ACR 矩阵与统计 Pilot 就绪（走 ACR 对象卡）、ASM 服务器地址。需要完整脚本开发 → 转姊妹技能。

1. 装编辑器（专用 msi）+ 必要时补 JRE。完成标准："ASM Script Editor application is started"
2. 连 ASM 并创建脚本，连线闭合后保存编译。完成标准：/usr3/afe 下出现 .scr+.alb
3. 激活到目标 Pilot。完成标准：Navigator 显示脚本生效的行为
4. 需要排障时右键 Debugger 激活，选过滤器抓轨迹并保存。完成标准：轨迹能解释当次路由
5. LCA 场景：写 IF 守门范式，测试前 kill alb 清记忆并复核为空。完成标准：第二通命中 LCA 规则

判停点：

- 脚本改了行为没变 → 停，先查是否重新 Activate（一 Pilot 一脚本，n06），再查 ccs.ini 类重启家族
- 直拨路由 Pilot 无呼叫档案 → 停，空列表 21 次后闭锁是设计行为（n07），业务号码要引导拨统计 Pilot
- 调试器 Make call 用坐席号发起 → 停，必须普通用户（n10），轨迹不代表真实路径
- 需要脚本级深度开发/复杂 LCA 策略 → 停，转姊妹技能 otcc-standard-advanced-call-routing

输出契约：可用的 ACR 脚本（已激活）+ 调试轨迹存档 +（LCA 场景）记忆清理与两通验证记录。

## B — 边界

- 本卡为 ACR 脚本主干（从简版）；积木块级开发、LCA_1/2/3 全族与调试器完整流程由姊妹技能承接
- 关键字拼写两套并存（LAST_CALLED_/LAST_CALL_），以编辑器下拉可选值为准（nr-03）
- "21 次执行 vs 21 请求/20 次执行"两口径并存（nr-05）；RESELECTION_TIMEOUT 是重跑节拍不是最长等待（n14）
- alb 重启清记忆、MAIN_AFE 重启不清（p252）：改 parameters.cfg 后的例行重启不影响 LCA 记忆
- 外置 ASM（external ASM）模式本书未展开；alb 参数（.inialb StatPeriod 5/NbMaxAgent 200）为实验观察口径（p272）
