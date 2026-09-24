# 应用生态加密与安全下载（Rainbow WG/4645/录音/VAA/DC、HTTPS 替代 TFTP）

## R — 原文依据

> "4645 Voice Mail is automatically secured when it is hosted in an OXE where native encryption is activated • Only one system parameter to activate"（p95）
> "The maximum number of VAA ports is decreased from 120 to 60 in case of encryption"（p98）
> "Use of HTTPS protocol, instead of TFTP • Prerequisite: Native Encryption activated on the OXE, whether the encryption flag is activated or not at user level"（p73）

出处：ENTPXTE421EN p63-64, p73-74, p94-99。

## I — 自述

五个应用出口的加密路径与一层下载安全，讲义查表型知识：

1. **Rainbow WebRTC Gateway**（p94）：SIP 信令恒加密、音频仅在 OXE 端点受保护时加密；仅网关侧认证（Rainbow 网关为 TLS 服务器）；trunk 组用 "SIP-ISDN mode"+Rainbow 变体外部网关；加密非强制可明文跑
2. **4645 Voice Mail**（p95）：宿主于开了 NE 的 OXE 内自动受保护，仅一个系统参数（Voice Mail Parameters 的 Enable Voicemail Encryption）；独立服务器部署才需改 eva.cfg 加 DTLS 参数+4645 证书（IP 入 SAN）；明文话机打加密 VM 时话音 RTP 不加密
3. **IP DR-Link 与 OmniPCX Record**（p96-97）：CS-OPR 间 CSTA 链路 TLS 1.2 强制、仅认证 CS；SRTP 密钥经 CSTA 安全下发；录音能力（明文/AES-128/AES-256）由 Recording SRTP Cipher Suite 决定；每次保持/会议/转接换新钥、OPR 收到即解密复制流
4. **VAA**（p98）：与 CS 间 SIP 链路走 Native SIP TLS（internal ABC-F 型）+SRTP（128/256 均可）；OXE CTL 手工导入 VAA、可选 mTLS；**加密后端口上限 120→60**
5. **Dispatch Console**（p99）：同 VAA 路径（internal ABC-F 型+可选 mTLS）；端口数不受影响（保持 120）；话务员设备可按普通设备加密
6. **安全下载（HTTPS 替代 TFTP）**（p73-74）两层规则：
   - CS↔设备（固件/定制文件/lanpbx.cfg）：前提 OXE 已激活 NE（与用户级开关无关）；IPv6 不支持；动态模式要求 DHCP offer 带 option 66（否则按 TFTP）
   - CS↔IPMG 初始化下载：前提 NE+mTLS（网关内须有证书），经 mgconfig/omsconfig 手工选 HTTPS；TOFU 开着时 CTL 经 lanpbx.cfg 自动获取；GD4/GA4/GD-XL/GA-XL/OXE-MS 支持，GD3/INTIP3 等老板卡仍 TFTP

## A1 — 书中案例

**容量与路径决策素材**（p94-99，讲义，无实验——选型即查表）：

- 客户要 100 个 VAA 加密端口 → 加密上限 60，方案要按两套 VAA 或接受 60 口径重谈
- 客户问留言是否自动加密 → NE 开启+宿主内置即自动受保护，仅开一个参数
- 客户问录音合规 → Recording SRTP Cipher Suite 定 128/256，且每次保持/转接换新钥
- 客户站点的 Rainbow WG → 信令恒加密，音频跟随端点保护状态

## A2 — 未来触发

使用情境：留言信箱加密；录音加密与密钥轮换；VAA/调度台加密后端口数；Rainbow 网关过 OXE 加不加密；话机固件下载走 HTTPS 的条件。

语言信号：4645 / voice mail / 留言加密 / OmniPCX Record / OPR / DR-Link / 录音 / SRTP Cipher Suite / VAA / Dispatch Console / 调度台 / Rainbow WebRTC Gateway / HTTPS / TFTP / DHCP option 66。

与相邻能力区分：端点与中继加密本体 → 开通/SIP trunk 等能力；ABC-F 网络型 SIP trunk 的链路加密 → ABC-F 网络能力；本卡只管应用出口与下载通道这两层外围。

## E — 可执行步骤

输入契约：客户在用的应用清单（VM/OPR/VAA/DC/Rainbow WG）与版本、下载通道形态（动态/静态）。应用版本不支持 → 判停按兼容矩阵排除。

1. 按应用对号：对照 I 段六条路径，逐应用列加密前提与代价。完成标准：应用加密矩阵成文
2. 容量复核：VAA 加密按 60 端口重算；DC 保持 120；录音按 cipher suite 定 128/256。完成标准：容量口径写入方案
3. 参数落地：VM 勾 Enable Voicemail Encryption 等各自参数；OPR/VAA/DC 按路径配证书与 CTL。完成标准：各应用加密生效
4. 下载通道：NE 开启后核对 DHCP option 66 与 DNS 前提；IPMG 侧按 mTLS/TOFU 状态选 HTTPS。完成标准：HTTPS 生效、老设备仍 TFTP 可用
5. 验收：逐应用打通并确认媒体/信令加密状态与方案一致。完成标准：验收单闭环

判停点：

- 客户 VAA 端口需求超 60 → 加密与容量冲突，让客户在"加密+扩容"与"端口优先"间做决策，不要默认替客户关加密
- 明文话机要打加密 VM → 明确告知话音 RTP 不加密（p95），不属配置故障
- GD3/INTIP3 站点想要 HTTPS 下载 → 老板卡不支持（仍 TFTP），先换板卡或接受 TFTP

输出契约：应用加密矩阵 + 容量口径 + 各应用验收记录。

## B — 边界

- 本卡为讲义查表型知识：五应用均无独立实验章，行为细节以各应用自身文档为准
- VAA 120→60 是加密的硬代价（p98）；引用端口数必须带"是否加密"前提
- Rainbow WG 只保证信令恒加密；端到端音频取决于 OXE 端点侧保护状态（p94）
- 安全下载不支持 IPv6；无加密方案或 IP Premium Security 的 OXE 不支持 HTTPS（p73）
- eva.cfg 独立部署 4645 的完整流程原书只给要点，细节在 4645 文档
