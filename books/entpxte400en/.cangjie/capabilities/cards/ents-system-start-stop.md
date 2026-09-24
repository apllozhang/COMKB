# OXE 系统启停与 autostart 管理

## R — 原文依据

> "FACILITIES Easy menu … 1 DECT registration 2 Backup database on cpu disk … 7 Stop the telephone 8 Start the telephone 9 Set new internet address 10 Stop the system"（p112）
> "There is no command to stop the telephone application. The whole system must be restarted and a telephone start-up cancelation must be performed"（p122 Notes）
> "WHEN THE TELEPHONE APPLICATION IS STOPPED VIA THE SWINST MENU (1-EASY MENU > 7-STOP THE TELEPHONE), THE AUTOSTART IS AUTOMATICALLY DISABLED"（p124）

出处：ENTPXTE400EN p108-125。

## I — 自述

启停全部经 swinst 账户（root 下进入免密），先选 Easy(1)/Expert(2)：

1. **起话务**：Easy 菜单 8（Start the telephone）；或 mtcl 下执行 RUNTEL。autostart 默认开启，重启后话务自起
2. **停话务**：Easy 菜单 7——没有独立的 CLI 停话务命令；且 Easy 7 会自动取消 autostart
3. **重启**：mtcl 下 shutdown -r now；**停机**：shutdown -h now 或 Easy 10（显示 "Software Watchdog stopped / Power down."）
4. **一次性取消自启**：重启过程中在 "automatic start of dhs3 is about to begin waiting 5 seconds…" 提示处按回车
5. **autostart 管理**：Expert 菜单 6（System management）→ 2（Autostart management）Set/Unset
6. **状态判读**：mtcl 下 role——MAIN/STAND-BY=运行，"erreur mapping on remagen -7"=停止；提示符 (E)=大概率停止、(数字)=运行，但不实时刷新

| 操作 | 入口 | 附带效果 |
|---|---|---|
| 起话务 | swinst Easy 8 或 RUNTEL | 恢复 autostart 需另行 Set |
| 停话务 | swinst Easy 7 | 自动取消 autostart，系统重启 |
| 重启系统 | shutdown -r now | 话务按 autostart 状态决定是否自起 |
| 停机 | shutdown -h now 或 Easy 10 | 显示 Power down，可断电 |
| 取消本次自启 | 重启时 5 秒窗口按回车 | 仅对本次生效 |

## A1 — 书中案例

**启停与 autostart 实验**（p121-125，How-To）：

1. swinst Easy 8 起话务并确认，Autostart is set
2. mtcl 下 role 显示 MAIN，确认运行态
3. Expert 菜单系统管理里 Set/Unset autostart 各做一遍
4. shutdown -r now 重启，等 "No problem with compatibilities"
5. 重启中在 5 秒提示处按回车，验证话务未自起
6. swinst Easy 7 停话务，观察提示 Autostart is not set
7. 停机实验 shutdown -h now，确认 Power down 输出
8. 恢复运行态，为后续实验做准备

## A2 — 未来触发

使用情境：维护前停话务；重启后话务没自起；想临时不启动话务；分不清系统是停了还是没起完；停机断电流程。

语言信号：启停 / start / stop / 重启 / reboot / shutdown / RUNTEL / autostart / 自启动 / role / (E) / Easy menu / Expert menu / swinst。

与相邻能力区分：启停之前的登录与账户 → 首登加固能力；停话务后建库/恢复 → 空库与许可、备份恢复能力（路由卡）。

## E — 可执行步骤

输入契约：维护窗口与话务影响评估、要执行的目标动作（起/停/重启/停机/取消自启）。生产系统停话务=全机业务中断，先拿变更窗口。

1. 确认当前态：mtcl 下执行 role，提示符仅作辅助（不实时刷新）。完成标准：运行/停止判定明确
2. 起话务：swinst Easy 8 或 RUNTEL；如曾停过，先回 Expert 菜单把 autostart Set 回来。完成标准：role 显示 MAIN 且 autostart 就位
3. 停话务（维护需要时）：swinst Easy 7 并知晓 autostart 被连带取消。完成标准：role 显示停止
4. 重启：shutdown -r now；如需本次不起话务，在 5 秒提示处按回车。完成标准：系统按预期回到目标态
5. 停机：shutdown -h now 或 Easy 10，等 Power down 再动电源。完成标准：安全下电
6. 收尾：维护完成后恢复话务并核对 autostart。完成标准：role=MAIN，下次重启话务会自起

判停点：

- 重启后话务没起来 → 先查 autostart 是否被上次 Easy 7 取消（n06），再查启动日志，不要盲目再重启
- 提示符仍显示 (E) 但业务正常 → 提示符不实时刷新（n05），以 role 为准或重登录
- "只想停话务不停系统" → 无此命令（p122），走重启+取消自启组合，评估影响后执行

输出契约：处于目标运行态的系统 + autostart 状态确认。

## B — 边界

- 本卡为操作短平快域，路由可达即可；与数据库类操作（建库/恢复）的先后依赖在对应能力卡展开
- swinst 菜单版本号随软件版本（书中示例 4.00.94），菜单项命名以现场为准
- Easy 7 连带取消 autostart 是最常见"重启后话务没起"根因（n06）
- 虚拟机场景的宿主机重启/迁移（vSphere/Hyper-V 等）属虚拟化平台操作，不在本书范围
