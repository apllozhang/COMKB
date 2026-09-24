# SIP trunk 的 SIP TLS 与 SRTP（OTSBC+OXE 双侧、信令/媒体决定表、安全停用）

## R — 原文依据

> "The Native SIP TLS trunk feature deals with signaling only • The media encryption (SRTP) depends on the activation of the 'native encryption' … and on the management of 'SRTP' parameter in the external SIP gateway"（p161）
> "Index 1, Name OXE TLS, TLS Version TLSv1.2 … DH key Size 2048"（p175）
> "RESTART THE SIPMOTOR PROCESS AFTER THE CONFIGURATION."（p190）
> "setting the SIP TLS (Mutual Auth.) port number as '0' overrides the SIP-External Gateway Parameter: 'SIP TLS Mutual Authentication parameter: True'"（p167）

出处：ENTPXTE421EN p93, p159-193, p194-198, p264-271, p377-379。

## I — 自述

运营商方向的加密中继：SBC 侧与 OXE 两侧成对配置，外加一条"信令≠媒体"的总纲：

1. **信令/媒体决定表**（p161，验收总纲）：

   | 系统 NE | 网关 SRTP 参数 | 媒体结果 |
   |---|---|---|
   | 关 | RTP or RTP/SRTP 或 RTP | RTP 明文（仅信令可加密） |
   | 开 | RTP | RTP 明文 |
   | 开 | RTP or SRTP | 明文（对不支持 SRTP 的对端回落） |
   | 开 | RTP/SRTP | SRTP（信令与话音全加密） |

2. **OTSBC 侧清单**（WebAdmin，p175-184）：
   - TLS contexts：TLSv1.2+DTLSv1.2、Cipher server AES256:AES128、DH key 2048
   - 证书四步：导入 RootCA、生成 4096 私钥、生成 CSR（CN=SBC 的 IP，SHA-256）、导入签发证书
   - SIP Interfaces（OXE 侧）：挂 context、UDP 置不使用、TLS port 5061
   - Proxy Sets（OXE）：Proxy Address 带 5061、Transport type TLS
   - Media Security：Enable + AES-CM-128-HMAC-SHA1-80；IP Profile 用 Offer Both–Answer Prefered Secure 兼容未加密用户
3. **OXE 侧清单**（p185-193）：
   - TLS signaling possible=Yes → 重启 CS
   - 外部 SIP 网关：远程域=SBC IP、端口 5061、Transport type TLS Client、SRTP=RTP or SRTP
   - 本地 SIP 网关：SIP TLS (Server Auth.) 5061 /（Mutual Auth.）6261，改端口须重启 SIPMOTOR
   - 对端 CA 不同时经 11.9.3 导入 SBC 的 CTL
4. **端口四组合与陷阱**（p166-168）：
   - 0/0 无 TLS；5061/0 仅服务器认证；0/6261 仅互认证；5061/6261 并存
   - 互认证端口填 0 会静默覆盖外部网关的 True，MAO 界面不会自动变 False（n15）
5. **mTLS 成对规则**（p378-379）：本地网关互认证端口=OTSBC Proxy Set 的 host:port；外部网关 SIP 端口=OTSBC SIP Interface 的 TLS 端口
6. **安全停用**（p194-198 四步）：系统参数取消勾选；用户 Native Encryption=Disable（SIP 用户再加 SRTP=None）；lanpbxbuild 里 DTLS1/2 填 0.0.0.0、FQDN 清空；重启（duplication 双 bascul）后互打确认 CLEAR

## A1 — 书中案例

**OTSBC 侧实验**（p173-184，c06 步骤 1-9）：

1. WebAdmin 建 TLS context（OXE TLS：TLSv1.2/DTLSv1.2、AES256:AES128、DH 2048）
2. 导入 RootCA（ca-certgen.cer，实验口径）
3. 生成 4096 私钥；生成 CSR（CN=SBC IP、SHA-256）交 CA 签发
4. 导入签发证书（.cer，Base-64 X.509）
5. SIP Interfaces 挂 context，TLS port 5061
6. Proxy Set 地址改 5061/TLS
7. Media Security Enable + AES-CM-128-HMAC-SHA1-80
8. IP Profile 设 Offer Both–Answer Prefered Secure

**OXE 侧实验**（p185-193，c07 步骤 2-7）：

1. TLS signaling possible=Yes 后重启 OXE
2. 外部网关 ITSP_GW 配 TLS Client/5061/SRTP=RTP or SRTP
3. 改 SRTP 认证后按警告执行 dhs3_init -R SIPMOTOR
4. 对端 CA 不同时 11.9.3.1 导入 SBC CTL（自动同步 twin）
5. IPDSP 与公网 MicroSIP 互打，看挂锁图标
6. sipextgw -g 3 核对 IN SERVICE；cryptview 列出受保护网关与扩展计数

**安全停用**（p194-198，c08）：按 I 段第 6 条四步执行，最后互打确认 CLEAR 模式。

## A2 — 未来触发

使用情境：运营商 SIP 中继要加密；SBC 和 OXE 两侧怎么配；中继信令加密了语音有没有加密；6261 端口；互认证开不生效；怎么把加密安全关掉回退。

语言信号：OTSBC / WebAdmin / TLS contexts / Proxy Set / SIP Interface / Media Security / AES-CM-128-HMAC-SHA1-80 / Offer Both / RTP or SRTP / 5061 / 6261 / SIPMOTOR / 停用 / deactivation。

与相邻能力区分：SIP 扩展（SEPLOS）加密归 SIP TLS 扩展能力；SBC 指向 NSP FQDN 与内部 DNS 归 EEGW 部署能力；验证命令族细节归验证与维护能力。

## E — 可执行步骤

输入契约：NE 已启用、SBC 可达、CA 签发通道可用、trunk 组类型为 "ISDN all countries"。运营商侧 TLS 参数未知 → 判停向运营商索取。

1. SBC 侧八步：按 I 段第 2 条清单顺序配置（context、证书、接口、Proxy、媒体、Profile）。完成标准：SBC 侧无红色告警
2. OXE 侧参数：TLS signaling possible=Yes → 重启 CS。完成标准：netstat 见 5061 监听
3. 外部网关：远程域/端口/Transport/SRTP 按 I 段第 3 条配置。完成标准：网关保存
4. 本地网关端口：按四组合决策 5061/6261 取值；两侧端口成对核对。完成标准：端口对照表通过
5. 生效与信任：dhs3_init -R SIPMOTOR；CA 不同则 11.9.3 导入对端 CTL。完成标准：进程重启完成
6. 验收：互打看挂锁或抓包；cryptview 网关计数；对照决定表确认媒体真加密。完成标准：信令与媒体双证
7. （如需回退）安全停用：按 I 段第 6 条四步执行并验证明文。完成标准：CLEAR 通话确认

判停点：

- 客户说"中继已加密"要验收 → 按 p161 决定表核对网关 SRTP 参数与系统 NE 同时开启，只看 TLS 不算媒体加密（n13）
- 互认证配置了 True 但实际没生效 → 查本地网关互认证端口是否被填 0（覆盖陷阱，MAO 仍显示 True，n15）
- TLS 建链失败 → 按 n29 两侧端口成对核对（本地网关 6261 对 Proxy Set、外部网关端口对 SIP Interface）
- 对端 SBC 的 SRTP 不合规 → RTP or SRTP 参数下会回落明文，与运营商核对 SRTP 能力

输出契约：双侧配置记录 + 端口对照表 + 信令/媒体双验证证据（或干净的停用验证）。

## B — 边界

- 真实运营商的 TLS 对接参数（证书策略、SRTP profile、SBC 型号差异）在书外——实验用 ITSP2 模拟器与 OTSBC
- Native SIP TLS 可独立于 NE 使用，但只保护信令；"上了 TLS 语音就加密"是误解（n13）
- SIP TLS with SSM 与 NE 的 SIP TLS 不兼容；中继加密不兼容 IPv6（p159）
- NSP FQDN 冗余指向规则归 EEGW 部署能力（p266）
- 实验口径：SBC Admin/Admin、ITSP_GW ID 3、证书由 trainer 签发——生产全部替换
