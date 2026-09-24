# PCS 加密接管（分支救援、断网演练）

## R — 原文依据

> "Endpoints must have been connected at least once to CS in order to be rescued by PCS"（p92）
> "SAME 'LANPBX.CFG' FILE OF MAIN CS IS USED FOR PCS NODES. END POINTS WILL NOT REQUEST 'LANPBX' FILE FROM PCS. … NOTHING TO DO."（p152）
> "PCS state:ACTIVE … 2 IP users are rescued (IP DSP 31002 & 31003)"（p155）

出处：ENTPXTE421EN p91-92, p146-156, p212-215。

## I — 自述

CS 失联后分支端点以加密模式切到 PCS 的救援机制，规则三条、流程五步：

1. **前置规则**（p92/p148/p152）：
   - 端点必须至少连过一次 CS（拿到初始信令里的 PCS 地址）才能被救援；新装直奔分支的端点不在范围
   - NE 相关配置只在主节点做，不在 PCS 上做
   - PCS 与主 CS 共用同一 lanpbx.cfg（端点不会向 PCS 请求），为 PCS 单独生成 lanpbx 是无用功
   - PCS 证书与 CS 同 CA 但必须是不同证书（CN=pcs.company.com 类 FQDN），导入前必须先打 tar 包
2. **PCS 的 EGW 形态**（p213）：PCS EGW IP=PCS IP → 内嵌 EGW（<1500）；不同地址 → 外接 EEGW（>1500）
3. **部署五步**（p212-215）：OXE 库配 PCS 地址与域名；CS 上生成/导入 PCS 证书（11.9.2.2/3）；pcscopy 拷证书与数据到 PCS；装 EGW VM；从 PCS 下载证书
4. **演练行为**（p154-156）：断网后 pcsview 显示 PCS state:ACTIVE、域 secured、用户 rescued；恢复重连后 PCS 回 INACTIVE、无救援用户

## A1 — 书中案例

**PCS 接管实验**（p146-156，c05 步骤 1-9）：

1. omsconfig 配 Passive CS address=192.168.2.5、domain=pcs.company.com（实验口径）
2. WBM 核对 PCS FQDN 已配置（PCS 证书用 FQDN 入 SAN）
3. netadmin 11.9.2.2 生成 PCS CSR，交 CA 签发取回 pcs.p7b
4. tar cf pcs.tar 打包后 11.9.2.3 导入，copy to twin
5. pcscopy → 1 PCS update 拷贝到 PCS（PCS 随之重启）
6. 11.9.2.4 导出 PCS 证书备份（csa_pcs_pfx.tar）
7. Rlab 门户断开 192.168.1.254（VLAN1 下线）
8. pcsview 核对 ACTIVE、2 IP users rescued，31002/31003 加密互打正常
9. 重连 VLAN1 后重启 PCS，核对其回 INACTIVE

## A2 — 未来触发

使用情境：分支没 CS 怎么保证加密通话；PCS 救援要什么前提；PCS 证书怎么做；断网演练怎么做不被"断"在自己手里；PCS 要不要单独配 lanpbx。

语言信号：PCS / Passive Communication Server / 救援 / rescue / pcscopy / pcsview / pcs.company.com / 断网演练 / failover / 192.168.2。

与相邻能力区分：PCS 外接 EEGW 的容量判断 → EEGW 部署能力；lanpbx 生成规则本体 → 开通能力；主备 CS（duplication）切换是另一机制，别与 PCS 救援混淆。

## E — 可执行步骤

输入契约：PCS VM/服务器就位、端点曾连过主 CS、PCS FQDN 已规划。端点是全新直奔分支的 → 判停（不在救援范围，先回主站注册一次）。

1. 配 PCS 身份：OXE 库填 PCS 地址与 FQDN 域；按 EGW 形态规则填 PCS EGW IP。完成标准：声明保存
2. 证书链：11.9.2.2 生成 CSR，CA 签发后打 tar，经 11.9.2.3 导入并 copy to twin。完成标准：导入成功提示
3. 下发：pcscopy 拷证书与数据库到 PCS；11.9.2.4 导出备份。完成标准：PCS 上 View 可见证书
4. 断网演练：断主站链路（预备带外/远端操作路径）→ pcsview 核对 ACTIVE 与 rescued 用户 → 加密互打。完成标准：救援行为确认
5. 恢复：重连链路 → 重启 PCS → 核对回 INACTIVE。完成标准：恢复闭环

判停点：

- 演练断网后自己也失联 → 预先准备带外管理或远端侧（VLAN2 类）操作路径（p154 警告）
- 想给 PCS 单独生成 lanpbx → 无用功，PCS 共用主 CS 文件（p152 NOTHING TO DO）
- PCS 证书没打 tar 直接导入 → 导入会失败，先打包（p150）

输出契约：PCS 救援就绪 + 断网演练记录 + PCS 证书备份。

## B — 边界

- 端点"至少连过一次 CS"是硬前提——救援范围不含从未注册的新端点（p92）
- 断网演练即主站失联：生产演练要按变更管理审批并预备操作路径（n09）
- RLAB 断链手段（Rlab 门户断路由器）为实验口径，生产用客户侧手段等效执行
- PCS 的 EEGW 扩容（>1500）按 EEGW 部署能力执行，本卡不展开
