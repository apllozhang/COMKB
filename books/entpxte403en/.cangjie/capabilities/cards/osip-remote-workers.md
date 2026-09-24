# 远程办公方案与落地（SBC/RP/EDS/VPN、原生加密、ALES Remote Worker）

## R — 原文依据

> "For small configuration (<= 500 remote users), it is possible to use the OTSBC embedded Reverse Proxy • If more, ALE recommends NGINX PLUS reverse proxy delivered by NGINX company, member of DSPP"（p387）
> "Restrictions: • No outbound HTTP proxy • No network requiring 802.1x authentication or VLAN identifier • No Wi-Fi (yet)"（p404）
> "ALE-2, ALE-3 SIP basic Deskphones embed a VPN client ... ALE-2/ALE-3 only support OpenVPN, not IPSec VPN"（p412）
> "Native encryption user parameter can be enabled on a remote worker (since OXE N4)"（p414）

出处：ENTPXTE403EN p384-458。

## I — 自述

远程办公只有两条路，方案矩阵按终端分：

| 终端 | 路 A：SBC/反代 | 路 B：VPN |
|---|---|---|
| ALES 软终端 | RP 拉 DM 配置（配置内含 SBC 地址 rpsbcX:5261）→ 经 SBC 注册 | 第三方 VPN 客户端（ALE 不提供） |
| SIP 话机 | SBC/RP/EDS：LAN↔WAN 搬迁、EDS 零接触 | 仅 ALE-2/3（内嵌 OpenVPN，TLS 认证+凭证+证书） |

- 反代规模红线：≤500 远程用户用 OTSBC 内嵌 RP；超过用 NGINX PLUS（DSPP 成员产品）
- 话机两用例：①LAN→WAN 搬迁——异地 DHCP 拿网参后回退用已存 RP 地址拉配置，SIP TLS REGISTER 经 SBC；②EDS 零接触——出厂 NOE 起步、联系 EDS（device.eds.al-enterprise.com）切 SIP 并取 RP FQDN 与根证书，硬编码四限制：无出向 HTTP 代理、无 802.1x、无 VLAN、暂无 Wi-Fi
- 证书五方信任链：话机库（ALE Cloud Connect CA 默认在 + SBC/RP CA 经 CTL/EDS 下发）、RP 库（ALE Terminals RootCA/SubCAs）、OT SBC 库（OXE 加密网关 CA）、EDS 库（还须导入 RP CA）、OXE（导 SBC/RP CA 进 CTL）——缺一张断一跳
- 原生加密：N4 起远程工作者可开用户级加密，OXE 经 REGISTER Via 头里的 SBC IP 识别远程工作者，传输模式不一致也放行（N4 前不行）；SBC LAN IP 清单最多登记 10 个，自动进 SIP 信任主机
- 远程 DM profile 要点（p407）：双 SBC/双 RP 地址、备用 LDAP（ldaps://RP_FQDN:636）、DNS2 公共 DNS；ALE-S 与 8008 一个 profile 兼容本地/远程，ALE-x 系要两份

## A1 — 书中案例

**OTSBC 内嵌反代**（p421-449，How-To）：

1. 新建 TLS Context（Remote_Workers：TLSv1.1/1.2、DH 2048），导入 Root CA，生成私钥+CSR（Subject=rpsbcX.company.com）交外部 CA 签发后装载。
2. 激活 HTTP Proxy（Enable+DNS）→ 必须重启 SBC。
3. RP 三件套：Upstream 组 OXE_443（192.168.1.3:443 实验口径）+ Proxy Server（公网域名、WAN 443、不验客户端证书）+ Location（/DM/dmsoftphone/ 前缀转发）。
4. SBC 远程对象六件：SIP Interface 3（TLS 5261、Accept Registered Users）、Media Realm（UDP 6000 起 100 腿）、NAT 翻译（5261 与 6000-6399 → 公网 IP）、IP Profile（Secured、Diffserv 40）、IP Group RemoteUsers、Classification。
5. 消息操纵与路由：组 3 改 to/from/Refer-To/Referred-By 的 host 为 rpsbcX:5261；Message Condition 'To ITSP'（header.to 含 SBC IP）区分流量并挂 IP-to-IP 路由。

**ALES Remote Worker**（p450-458，How-To）：

1. 建 DM profile 2（SBC and LAN、outbound proxy=rpsbcX.company.com、端口 5261、Reverse proxy FQDN 同址）。
2. 用户挂 profile 2（profile 必须先存在）。
3. 异地 PC 装 ALES：Local access=oxe.company.com、Remote access=rpsbcX.company.com → 登录验证。
4. 核对 sipregister：远程用户 contact 指向 SBC LAN 地址（如 sip:…@192.168.1.105），本地用户仍是直连 IP。

## A2 — 未来触发

使用情境：员工长期居家/出差要打电话；给客户报远程方案（RP 还是 VPN）；话机寄到家零接触 开通；远程用户注册不上或来话不走 SBC；远程加密方案评估。

语言信号：远程办公 / remote worker / 居家 / 反向代理 / reverse proxy / NGINX PLUS / 500 用户 / EDS / 零接触 / zero touch / 原生加密 / native encryption / 5261 / rpsbcX / SBC and LAN / sipregister。

与相邻能力区分：SBC 本体部署与运营商对接找 SBC 运营商接入；话机/软终端基础开通找各开通卡；证书内容生成找证书管理；注册排障工具找 SIP 跟踪排障。

## E — 可执行步骤

输入契约：远程用户数与终端构成、家庭网络条件（代理/802.1x/VLAN/Wi-Fi）、公网域名与 IP、证书签发渠道、OXE 版本。用户家庭网络触发零接触 四限制 → 判停改方案。

1. 选路：软终端优先 SBC/RP（≤500 用内嵌 RP）；话机 ALE-2/3 可走内嵌 OpenVPN，IPSec-only 环境出局。完成标准：每人一条路
2. 核网络：零接触 四限制逐条问掉（HTTP 代理/802.1x/VLAN/Wi-Fi）；ALE-2/3 不能动态搬迁，先挂目标位置专用 DM profile。完成标准：网络评估表成文
3. 配承载：OTSBC 内嵌 RP 七段（TLS Context、RP 激活重启、三件套、媒体安全、六对象、操纵、路由分流）。完成标准：远程接口 5261 就绪
4. 配 OXE 侧：SBC LAN IP 入信任主机；建远程 DM profile（双 SBC/RP/备用 LDAP）并挂用户。完成标准：profile 先存在再挂用户
5. 证书五方核对：话机/RP/SBC/OXE/EDS 逐库对照，缺一张断一跳。完成标准：五方清单全勾
6. 终端落地：零接触 话机在 EDS 建 Profile（DM URL/证书/强制 SIP）；ALES 异地装机填 Local+Remote 双地址。完成标准：终端注册成功
7. 验证收口：sipregister 中远程用户 contact 指向 SBC 地址；来话去话与配置通知各验一次。完成标准：端到端通过

判停点：

- 远程用户 >500 → 内嵌 RP 出界，转 NGINX PLUS（部署书外），不给内嵌超载承诺
- 家庭网络有出向 HTTP 代理或 802.1x/VLAN → 零接触 直接失败，改 VPN 或预配话机
- 客户环境 IPSec-only 且要话机 VPN → 停，ALE-2/3 只支持 OpenVPN（n40）
- OXE 版本低于 N4 又要远程原生加密放行 → 停，先升级（n39）
- OXE 是 R100/R101.0 低版本而预期 8443 mTLS 行为 → 停，版本不支持（nr-07）

输出契约：远程办公方案书（路线/规模/证书五方）+ RP/SBC 配置台账 + 远程用户注册验证记录。

## B — 边界

- NGINX PLUS 部署、EDS 账号开通（admin 入口 /register）、VPN 网关兼容清单（Server deployment Guide）均在书外，生产依据 TC2957 与 EDS user manual
- 公网 IP（12.C.P2.105）、域名（rpsbcX.company.com）与口令全为实验口径（n50）
- 原生加密远程工作者是 N4 新语义，低版本传输模式不匹配直接不 provision（n39）
- RP 头机制（X-Real-Mac/X-Forward-For）只认 CS 已知的 RP，客户自选第三方反代必须登记（n42）
- DM 配置文件无备份，数据库恢复后须手工 generate all configuration files（n43，灾备清单项）
- RDP in RDP 双层远程会话断开时只断第二层，断错层会踢掉主会话（n48，操作纪律）
