# 实验环境底座（RLAB 拓扑、Pod 初始配置、时间同步）

## R — 原文依据

> "Remote Lab allows accessing a pool of virtual machines hosted in a data center. … Pods are independent of each other"（p29）
> "Manage the following NTP server for all the PC clients (used in this training): 192.168.1.252"（p50）
> "Due to RLAB infrastructure and technology, 2 VMs (even if not started) can't have the same IP address."（p285）

出处：ENTPXTE421EN p27-57, p283-290。

## I — 自述

全书实验的底座：两套拓扑 + 一个初始配置流程，全部为培训专用环境：

1. **两套拓扑**（p32-40）：
   - stand-alone：双 CS（CSA/CSB）+ OMS + EEGW×2 + SBC + 远端 PCS（Subnet1 192.168.1.x / Subnet2 192.168.2.x / 公共区 10.20.30.x）
   - ABC-F 网络：NODE1/NODE2 双节点 + OMS×2 + 直连链路（用户 31000/31500）
2. **Pod 初始配置五步**（p48-57）：
   - NTP：所有客户端指向 192.168.1.252 并立即更新——证书日期校验的前提
   - 根 CA 证书：从 NAS 取 ca-certgen 装入 PC 的"受信任的根证书颁发机构"
   - 板卡核对：主站点 OMS Rack 4（虚拟 GD4 192.168.1.13/24）、远端 Rack 6（192.168.2.13）
   - 用户：装 IPDSP（TFTP=主 CS IP）与 ALES（local access=主 CS IP）
   - 公网接入：OXE 侧 DID 翻译与 NPD 33 默认号；SBC 侧 NAT 规则与账号改 podN
3. **平台约束**（p285/p49/p34）：
   - 两台 VM 即使关机也不能同 IP；切拓扑先删旧接口再建新接口并硬重启
   - VM 分批启动：PCS/EEGW 实验前不起对应 VM
   - ITSP2 模拟器两腿：SIP 网关 gateway.itsp2.com + 公网网关 public.itsp1.com（章内 ITSP1/2 标签混用，见 nr-04）
4. **换节点信任库规则**（p108/p288）：设备在 FSNE 节点间搬移前要 factory reset 或先取新 CTL；OMS VM 曾服务过 CSA/CSB 时必须 Erase saved certificates

## A1 — 书中案例

**Pod 初始配置**（p48-57，c01 步骤 1-11）：

1. 按需启动 VM：PCS 与两台 EEGW 先不起（后续实验再启）
2. 客户端 NTP 指 192.168.1.252，立即更新
3. NAS 取 ca-certgen，装入本地计算机受信任的根证书颁发机构
4. 核对 OMS 机架板卡与 MAC（实验口径 00:50:56:01:01:13）
5. 装 IPDSP 与 ALES 并按用户表指定服务器地址
6. DID 翻译：首外线 33920N31000、首内线 31000、范围 500（N=POD 号）
7. NPD 33 默认号设为 33920N31000
8. SBC NAT 两条规则改为 12.班级.POD.105 形态地址
9. SBC 账号 Contact/User Name 改 podN 并立即注册
10. 外呼/入局测试确认公网 SIP carrier 打通

**网络实验室改造**（p283-290，c13）：Rlab 门户把 192.168.1.1 接口从 CSA 摘除、挂到 NODE1、硬重启；OMS 清信任库；hybvisu 确认直连链路 UP（Encryption 初始 NO）。

## A2 — 未来触发

使用情境：搭 OXE 加密实验环境；实验 Pod 的 IP/账号是什么；证书报日期错误；换拓扑要动什么；SIP 模拟器怎么打公网电话。

语言信号：RLAB / POD / Pod configuration / NTP / ca-certgen / DID / NPD / SBC NAT / podN / ITSP2 / MicroSIP / hybvisu / Rlab 门户。

与相邻能力区分：本卡是环境底座，一切加密配置动作都在其余能力卡；生产环境搭建不适用本卡（拓扑与数值全为实验口径）。

## E — 可执行步骤

输入契约：RLAB 门户账号与 POD 号。生产项目 → 判停，本卡仅作教学参考。

1. 起 VM：按实验需要分批启动（PCS/EEGW 延后）。完成标准：基础 VM 可达
2. 时间同步：全部设备指向统一 NTP 并校准。完成标准：日期时间一致
3. 信任根：根 CA 证书装入客户端受信任根。完成标准：证书提示消失
4. 核板卡与用户：按设置表核对 OMS/板卡/IP，装 IPDSP 与 ALES。完成标准：话机注册
5. 公网接入：DID/NPD/SBC NAT/账号四件配好后互打。完成标准：公网呼叫打通
6. （网络线）切拓扑：删旧接口、建新接口、硬重启，清 OMS 旧证书后 hybvisu 验链路。完成标准：直连链路 UP

判停点：

- 证书报 notBefore/notAfter 错误 → 先查时间同步（n34），别急着动证书
- 两台 VM 抢同一 IP → RLAB 硬约束：先删旧接口再建新接口并硬重启（p285）
- OMS 换角色后在服务异常 → 清信任库旧证书（omsconfig 的 Erase saved certificates）再重启（p288）

输出契约：可打电话、可达公网、时间同步的实验 POD（或就绪的网络实验室拓扑）。

## B — 边界

- 全部 IP/口令/号码为 RLAB 实验口径，生产禁用且需整体替换（详见 references.md 备查节）
- ITSP2 模拟器行为不等于生产运营商：SIP 对接差异要在真实中继项目里另行验证
- 照抄原书会困惑的三处：ITSP1/2 标签混用（nr-04）、GD4 串口速率 11520 疑脱漏 0（nr-02）、VM 分批启动（p49）——引用时按 needs-review 标注
- 课程评估与证书下载（p404-410）属课程运营，非技术知识，本卡不覆盖
