# SIP TLS 扩展加密（sipmotor、SEPLOS 端点、注册与媒体验证）

## R — 原文依据

> "TLS signaling: True • SRTP offer answer mode: True • Loose Route with RegID: False"（p140）
> "SRTP Working mode Best Effort … 'None' means RTP: audio flow is in clear mode"（p141）
> "Compatible devices (SEPLOS mode only) … Not supported for third-party devices and older ALE SIP devices"（p88）
> "Run a SIP trace (motortrace 3) and look for the 'X-ALE-CALL-ENCRYPTED' information and TLS signaling"（p142）

出处：ENTPXTE421EN p88-90, p139-145, p244-263。

## I — 自述

SIP 扩展加密与 DTLS 线并行的第二条端点线，由 sipmotor 承载（外部 EGW 场景由 NSP 承载）：

1. **协议与角色**（p67/p88）：
   - TLS 1.2（RFC 5246）承载 SIP 信令；OXE 为 TLS 服务器、SEPLOS 端点为客户端
   - 端口 5061（服务器认证）；仅 TLS 1.2、SHA-2 证书、RSA 2048-4096 位
   - <1500 会话内嵌 sipmotor；超出走 EEGW/NSP
2. **兼容边界**（p88-89）：
   - 仅 SEPLOS 模式：ALES（PC/Android/iOS）、Enterprise（ALE-x00）、Essential（仅 ALE-30）、Basic（ALE-x）
   - 第三方 SIP 设备与老 ALE SIP 设备不支持；CCD agent 场景不可用；仅 IPv4
3. **系统参数三件套**（SIP Parameters，p140）：
   - TLS signaling possible=True（开端口监听；改后重启 CS 或双 bascul，netstat -an|grep 5061 验证）
   - SRTP offer answer mode=True（SDP 协商/双密钥/可认证/SRTCP RFC 模式；False 为 OXE 集中式单密钥 THALES 模式）
   - Loose Route with RegID=False（True 时相应 INVITE 被 488 Not Acceptable Here 拒绝）
4. **用户参数**（p141）：SIP Extension Parameters 的 Native encryption=Enable；SRTP Working mode=Best Effort（None=RTP 明文）
5. **冗余与 PCS 行为**（p89-90）：
   - TLS anticipation：与两台 CS 各建一条 TLS 链路（按物理 IP 非角色 IP），REGISTER 刷新维持
   - 链路断时分支 SIP 端点与本地 PCS 建 SIP TLS；远程工作者按 REGISTER Via 头的 SBC IP 识别（库内最多 10 个）
6. **验证抓手**（p142-145）：sipregister（contact 带 TLS）、csipsets（TLS/SRTP 列）、motortrace 3（Via SIP/2.0/TLS、RTP/SAVP、X-ALE-CALL-ENCRYPTED: YES）

## A1 — 书中案例

**SIP TLS 扩展实验**（p139-145，c04）：

1. 前提：CA/CS 证书已加载、NE 主参数已配（承接 DTLS 主线实验）
2. SIP Parameters 三件套按口径配置，重启 CS
3. netstat -an | grep 5061 确认端口进入监听
4. ALES 用户 31030/31031 开 Native encryption + SRTP Best Effort
5. Phone COS/0 开 Display Encrypted Communication=YES
6. ALES 间互打，出现盾牌图标
7. sipregister 核对 TLS 注册；csipsets 核对 TLS/SRTP 列
8. motortrace 3 + traced 抓 SIP trace，核对 INVITE 的 Via 与 X-ALE-CALL-ENCRYPTED

**NSP 变体**（p244-263，c10）：EEGW+NSP 场景同一套参数，SIP trace 中 INVITE 发往 nsp.oxe.company.com:5061、Via 显示 EEGW IP。

## A2 — 未来触发

使用情境：ALES/软话机注册走 TLS；SIP 话机加密怎么开；为什么 SIP 呼叫没有盾牌；488 拒绝；CCD 客服座席能不能加密；SIP 扩展在分支失效时怎么办。

语言信号：sipmotor / SEPLOS / TLS signaling / 5061 / SRTP offer answer / Best Effort / ALES / ALE-x00 / 盾牌 / X-ALE-CALL-ENCRYPTED / sipregister / csipsets / motortrace / 488。

与相邻能力区分：NOE 端点（IPDSP/话机）加密归开通能力（DTLS 线）；中继侧 TLS 归 SIP trunk 能力；EEGW/NSP 承载归 EEGW 部署能力；本卡只管 SIP 扩展（SEPLOS）线。

## E — 可执行步骤

输入契约：证书就位、NE 已启用、端点为 SEPLOS 模式清单内设备。设备是第三方 SIP → 判停（不支持）。

1. 核兼容：按 I 段边界清单核对端点型号与场景（CCD agent、IPv6 直接出局）。完成标准：可加密端点清单
2. 配系统参数：SIP Parameters 三件套（TLS 信令 True / SRTP offer answer True / Loose Route False）→ 重启 CS。完成标准：5061 监听确认
3. 配用户：Native encryption=Enable + SRTP Working mode=Best Effort + COS 开加密图标。完成标准：用户级生效
4. 验证注册：sipregister 看 contact 带 TLS；csipsets 看 TLS/SRTP 列。完成标准：全列 YES
5. 验证媒体：互打看盾牌；motortrace 3 核对 TLS Via、RTP/SAVP、X-ALE-CALL-ENCRYPTED: YES。完成标准：三证齐全
6. 冗余核查：双 CS 环境核对 TLS anticipation（物理 IP 双链路）。完成标准：主备均可注册

判停点：

- 呼叫被 488 Not Acceptable Here 拒绝 → 先核 Loose Route with RegID 是否被置 True（n16）
- SRTP 认证值要改 → 只在对端（如 SBC）同为 Authenticated 时才改；IPDSP 共存站点实际锁定 Authenticated（n18）
- 客户要求第三方 SIP 话机或 IPv6 加密 → 本能力不覆盖，声明边界（n14）

输出契约：TLS 注册 + 加密媒体验证记录 + 兼容性核查清单。

## B — 边界

- SIP TLS with SSM 与 Native Encryption SIP TLS 互斥；SIP 扩展加密整体不兼容 IPv6（p159）
- 远程工作者加密的前提：LAN 侧 SRTP 要求 OT-SBC 与 OXE 间走 TLS 且用户开加密（p90）
- CCD agent 场景不可用（p89 自注）——呼叫中心座机加密要提前排除
- 实验账号/分机号（eevans/alcatel 等）为实验口径，生产按客户环境替换
