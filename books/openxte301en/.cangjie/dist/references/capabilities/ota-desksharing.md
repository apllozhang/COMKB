# Desksharing 共享工位（DSU/DSS、前缀 600/601、OTC PC 远程释放）

## R — 原文依据

> "OXE desksharing feature allows a connection user (called DSU: DeskSharing User) to use a physical set, called DSS (DeskSharing Set)."（p59）
> "This MAC address appears immediately after the creation of the user, and is based on the following rule: 'aa:bb:xx:xx:xx:xx' where xx:xx:xx:xx is the directory number."（p67）
> "Enable the following licenses in order to be able to release (LogOff) the DSS from the OTC PC client: Desktop • Flex Office"（p72）

出处：OPENXTE301EN p58-75。

## I — 自述

用"虚拟身份"复用硬件的三层机制：

1. **OXE 侧 DSU/DSS**：DSU 无绑定设备、MAC 为系统生成的虚拟值（aa:bb+目录号 hex，如 31000 对 aa:bb:00:03:10:00）；DSS 有真实 MAC；DSU 凭前缀 600 登录/601 登出加密码使用任意 DSS
2. **OTC PC 增强**：Desktop+Flex Office 许可下，用户可从客户端远程释放（Release business phone）DSS
3. **nomadic 兼容**：登出态由 OTC PC 上的 UA 软话机替代做底，不冻结任何话机；切 nomadic 前必须先释放 DSS
4. **四个系统参数**：免密登出（默认 False）、定时登出（-1 或 0-23 整点）、忙时重置（True=释放通话+6004 事件；False=显示 Unauthorized）、首登强制改密
5. **维护三命令**：incvisu（6004 事件两种文案）、domstat（DS 列 S=Set/U=User）、ippstat（按 MAC/号码反查 DSU 登录在哪台 DSS）

## A1 — 书中案例

**Desksharing 配置与维护实验**（p62-75）：

1. 建前缀：Translator/Prefix Plan 建 600（Over Logon）与 601（Logoff）
2. 建 DSS：DN 31100、Set Function=Desk Sharing Set、COS 开两项、可编程键配 LogOn 与 Emergency
3. 改 DSU：Barkley（31000）Set Function=Desk Sharing User、虚拟 MAC 生成为 aa:bb:00:03:10:00
4. DSU 可编程键配 600/601；系统参数四件按策略设定
5. OTC PC 授权 Desktop+Flex Office（DSU 须在 OT 库，未知则补 OT Applications 权限）
6. 维护：incvisu 看 6004、domstat 选项 9 看 S/U 标记、ippstat d 31000 反查所在 DSS
7. 复位：话机上 "I"+# 进 IP parameters 选 Free seating 清全部信息

## A2 — 未来触发

使用情境：共享工位/免费座位方案；用户换工位登录登出；忙时他机登录的行为策略；远程释放话机；DSU 登在哪台话机的定位。

语言信号：共享工位 / desksharing / DSU / DSS / 600 / 601 / 登录登出 / LogOn / LogOff / 虚拟 MAC / aa:bb / Flex Office / 远程释放 / Release business phone / domstat / ippstat / incvisu / 6004 / Free seating。

与相邻能力区分：不登出话机的移动（nomadic）→ Nomadic 能力；UA 软话机的网络边界（WAN 需 VPN、不支持 Mac）在本卡处理。

## E — 可执行步骤

输入契约：共享区规模与话机清单、登录策略（密码/定时登出/忙时行为）、用户许可现状。

1. 建前缀与 DSS/DSU（Set Function 区分，COS 开两项）。完成标准：登录登出测试通过
2. 可编程键与系统参数四件按客户策略配置。完成标准：忙时/定时行为与预期一致
3. OTC PC 授权并验证远程释放。完成标准：Release business phone 可用
4. 维护演练：6004 事件、domstat/ippstat 反查、Free seating 复位。完成标准：运维动作可执行

判停点：

- 远程员工要 Mac 上用 UA 软话机 → 不支持（OTC Mac 不兼容 UA）；WAN 直连也不行，必须 VPN
- 他机登录显示 Unauthorized 或通话被掐断 → 参数策略问题（Allow Reset of Busy DSU），需业务确认后改
- OTC PC 没有释放入口 → 查 Desktop+Flex Office 许可与 DSU 是否在 OT 库

输出契约：共享工位配置单（前缀/DSS/DSU/COS/参数）+ OTC PC 释放验证 + 维护命令演练记录。

## B — 边界

- UA 软话机不兼容 WAN（需 VPN）与 OTC Mac（n04）——方案承诺前先确认终端形态
- 忙时重置选 True 有"通话被掐断"体验代价，需业务方确认（n07）
- 600/601 前缀、COS 0、号码 31100/31000 均为实验口径
- Emergency 键（0112#）为书中推荐配置，按客户实际改
