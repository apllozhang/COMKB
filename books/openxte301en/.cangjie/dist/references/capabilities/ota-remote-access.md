# OpenTouch 远程接入通道与证书（反向代理、OTSBC、ACS FQDN、DAS 规则）

## R — 原文依据

> "Declare the reverse proxy with the following URL for all services: https://ot-podx.company.com • https://ot-podx.company.com:8016 for EVS (notifications)"（p104）
> "Ports: 5261<->5261 8061<->8061 RTP/sRTP ports: 7000-7499<->7000-7499"（p105）
> "WARNING THIS SPECIFIC FQDN ASSIGNED FOR CONFERENCES INVITATION MUST BE PART (SUBJECT ALTERNATIVE NAME) OF THE REVERSE PROXY AND OPENTOUCH SERVER CERTIFICATES."（p109）
> "WARNING THE DECLARATION ORDER IS IMPORTANT. SEVERAL RULES CAN BE APLLIED AT A TIME"（p108，APLLIED 为原文笔误）

出处：OPENXTE301EN p103-118。

## I — 自述

远程接入是"信封 + 话音 + 规则"三件套，远程客户端与 nomadic/智能手机全靠它：

1. **反向代理（RP，数据面）**：DMZ 部署，四个公共 URL 在 OT 拓扑声明（API/EVS/ACS/DMS），EVS 通知走 8016，NAT 443/8016
2. **OTSBC（SIP/媒体面）**：OTC 客户端注册 FQDN+5261，WebRTC 走 otsbc FQDN+8061，RTP/sRTP 媒体段 7000-7499；iPhone+ 另有同 FQDN、5265 端口的专用声明（见智能手机卡）
3. **DNS/NAT**：外部 DNS 按 POD 给 ot-podN/conf-podN 解析条目，conf-podX 公网指 RP、内网指 ACS 虚拟 IP（双解析）
4. **证书**：会议 FQDN（conf-podX）必须同时进 RP 与 OT 两张证书的 SAN；流程六步为验证、rehost、CSR、CA 签发、导入、部署
5. **DAS 规则**：挂在 ACS 的最多 20 条 Unix 正则，按序串行处理所拨号码（前一条输出=后一条输入）；R2.0 起 nomadic 必须有规则 7（+N/N）与规则 8（+M/M）

端口与入口总表（实验模板口径）：

| 面 | 入口 | 端口 |
|---|---|---|
| 数据面（RP） | https 公共 URL | 443、8016（EVS 通知） |
| SIP 注册（OTSBC） | ot-podX FQDN | 5261 |
| WebRTC 音频 | otsbc-podX FQDN | 8061 |
| 媒体段 | RTP/sRTP | 7000-7499 |
| 会议 SIP 代理 | ACS 互连 | 5060 监听、5260 互连 |

## A1 — 书中案例

**远程接入声明与证书全流程**（p103-118 实验）：

1. 规划 NAT 与外部 DNS（10.20.X.105 对 192.168.2.105，实验口径）
2. OmniVista 8770 声明 RP 四个公共 URL（API/EVS:8016/ACS/DMS）
3. Eco system/IT server 建 OTSBC 两声明：5261（OTC）与 8061（WebRTC）
4. 会议服务器管理台 Default 域核对法国 10 条 DAS 规则（重点规则 7/8）
5. 查 /var/data/bics/bics.conf 与 OT 证书 SAN 确认 ACS 已配置
6. 未配置则 ot-config.sh --rehost：填 conf-podX/company.com/192.168.1.55（实验口径）
7. System services/Security/Certificate 生成 CSR（SHA256）
8. 到 CA（eco.company.com/CertSrv，实验口径）Base 64 提交、Web Server 模板、下载证书链
9. pkcs#7 导入（pkcs#12 需 passphrase）并 Deploy，重登复核 SAN

## A2 — 未来触发

使用情境：远程/居家员工连不上 OT；会议邀请邮件链接打不开；换域名或证书到期；nomadic/手机呼叫格式不对；新 POD 开通远程通道。

语言信号：反向代理 / reverse proxy / OTSBC / SBC / 5261 / 8061 / 7000-7499 / 证书 / certificate / SAN / rehost / CSR / conf-pod / DAS 规则 / 正则 / 公共 URL。

与相邻能力区分：

- 手机经此通道落地 → 智能手机能力
- nomadic 资源池 → Nomadic 能力
- 认证经 RP 的限制（Kerberos 不支持经反向代理）→ 外部认证能力

## E — 可执行步骤

输入契约：公网 IP/域名规划、DMZ 主机、DNS 管理权限、CA 可用性。生产 DMZ 拓扑与证书策略在书外，需按客户环境替换实验模板值。

1. 声明 RP：拓扑里填 Display name 与四个公共 URL（EVS 带 8016）。完成标准：URL 写入客户端配置模板
2. 声明 OTSBC：Eco system/IT server 建 5261 与 8061 两条（Network type=WAN）。完成标准：远程客户端可用 FQDN 注册
3. DNS/NAT 核对：ot-podN 与 conf-podN 外部解析、443/8016/5261/8061/7000-7499 放行。完成标准：内外解析与端口连通
4. DAS 规则核对：Default 域 10 条逐条核对顺序（R2.0 后必含 +N/N 与 +M/M）。完成标准：拨号格式测试通过
5. 证书流程：验证 SAN；需要时先建内部 DNS 条目再 rehost；随后 CSR、CA 签发、导入、Deploy。完成标准：SAN 含会议 FQDN、邀请链接内外均可解析

判停点：

- Deploy 后 WebAdmin 报 "Impossible to retrieve data" 并断会话 → 属正常（证书已换），重开会话即可，勿回滚
- 会议 FQDN 只进了 OT 证书、漏了 RP 证书 → 停，重签补 SAN，否则一侧链接必挂
- rehost 前发现内部 DNS 无 conf-podX 条目 → 停，先补 DNS 再执行
- DAS 排障时先分两层：系统选项格式化（p302 五类实例）与规则链，逐层看输出

输出契约：可用的远程接入通道（URL/端口/FQDN 清单）+ 含会议 FQDN 的证书 + DAS 规则集存档。

## B — 边界

- 实验 IP/域名（ot-podX、conf-podX、10.20.X.105 等）为模板口径，生产按客户 DMZ/DNS 规划替换
- DAS 规则集仅法国口径（+33/00/0），非法国号码计划需自行推导正则（nr-07 版本纪律：R2.0 规则 7/8）
- Kerberos 认证不支持经反向代理，远程 OTC PC 自动回落账密登录（见外部认证能力 n38）
- 证书 CA 形态（内部 Windows CA/OpenSSL/外部商业 CA）书内只给 Windows CA 实验，外部 CA 仅方向性提示
- LDAP 上限"20 vs 5"等容量口径冲突不在本卡（见目录能力与 nr-01）
