# OpenTouch 服务器侧远程访问设置（RP 申报、OTSBC 申报、DAS 规则、ACS 会议服务）

## R — 原文依据

> "Declare the reverse proxy with the following URL for all services: https://ot-podx.al-mydemo.com, https://ot-podx.al-mydemo.com:8016 for EVS (notifications)"（p63）
> "From R2.0 new rules must be added for OT Connection PC application used in nomadic mode and must respect the following order"（p67）
> "WARNING: THE DECLARATION ORDER IS IMPORTANT. SEVERAL RULES CAN BE APLLIED AT A TIME"（p67，APLLIED 系原文拼写笔误）
> "Launch the rehosting script thanks to the command: 'ot-config.sh --rehost'"（p70）

出处：OPENXTE225EN p62-77。

## I — 自述

服务器侧三段流程，缺一段客户端就进不来：

1. **申报反向代理**（OmniVista 8770，SystemServices/System services/Topology/Reverse proxy）：录四个公共 URL，会写入配置文件供 OTC 从互联网回连
2. **申报 OTSBC**（Eco system/IT server，Create）：FQDN、Network type=WAN、端口 5261（OTC 客户端）或 8061（WebRTC）；FQDN 写进客户端配置用于 SIP 注册
3. **会议访问管理**：核对/新增 DAS 规则 + 配置 ACS 会议服务专用 FQDN 与专用 IP，必要时跑 rehost 并重签证书

RP 申报四 URL 口径：

| URL 项 | 端口口径 | 用途 |
|---|---|---|
| API public URL | 443（不带端口） | 客户端 API 回连 |
| EVS public URL | 必须带 :8016 | 事件通知（漏配则通知类功能失效） |
| ACS public URL | 443（不带端口） | 会议接入 |
| DMS public URL | 443（不带端口） | 设备管理服务 |

DAS 规则要点（p67）：强制（mandatory）且国家相关——书中 10 条为法国口径；R2.0 起游牧 OT Connection PC 需新增 4 条且必须按序：s/^\+[国家前缀]/[中继占用前缀]0/、s/^\+N/N/、s/^\+M/M/、s/^\+/000/；声明顺序重要，多条规则可同时命中。

ACS 会议服务：专用 FQDN（会议邀请链接用它生成）+ 专用 IP；未随初装配置或需变更时跑 ot-config.sh --rehost，随后必须重签 OT 证书把会议 FQDN 加进 SAN（联动证书能力）。

## A1 — 书中案例

服务器侧设置全流程（p62-77，具体实验值见 book/overview）：

1. OmniVista 8770 打开 OpenTouch 配置窗，进 System services/Topology/Reverse proxy
2. 选 Reverse proxy 填 Display name 与四个公共 URL（EVS 带 :8016）
3. Eco system/IT server 右键 Create，申报 OTSBC：FQDN、WAN、Port 5261
4. 同路径再建一条 WebRTC 用申报：FQDN 同、WAN、Port 8061
5. 会议服务器 Administration Console 的 Default 域逐条核对 10 条 DAS 规则，缺则按序补
6. 查 bics.conf 尾部 ACS 参数；ping ACS 专用 IP；或 My Profile 页证书图标查 SAN
7. 未配置时执行 ot-config.sh --rehost，在 ACS 专页填会议 FQDN/域/专用 IP
8. rehost 后 ping 会议 FQDN 验证；证书重签后打开证书 Details 核对 SAN

## A2 — 未来触发

使用情境：部署远程接入时的服务器侧准备；通知类功能（漏接提醒）时好时坏；会议邀请链接不可用；换 ACS 名/IP 之后；其他国家部署照抄法国 DAS 规则出问题。

语言信号：申报 / declare / Reverse proxy / 公共 URL / public URL / EVS / 8016 / DMS / IT server / WAN / 5261 / 8061 / DAS / 规则 / ACS / 会议 / conference / rehost / ot-config.sh。

与相邻能力区分：

- 证书签发与 SAN → 证书与 PKI 能力
- OTSBC 本体安装 → OTSBC 部署能力
- 反代安装 → 反向代理能力

## E — 可执行步骤

输入契约：公共域名规划（含会议 FQDN）、OTSBC 公共 FQDN 与端口、目标国家（定 DAS 口径）、8770 与 WebAdmin 权限。

1. 在 8770 申报 RP 四 URL，EVS 项补 :8016 端口。完成标准：Reverse proxy 页保存成功且 URL 与规划一致
2. 申报 OTSBC 两条（OTC 用 5261、WebRTC 用 8061），Network type=WAN。完成标准：IT server 列表出现两条 SBC 申报
3. 按目标国家改写并按序核对 DAS 规则；游牧 PC 场景确认 R2.0 起的 4 条新规则在列。完成标准：规则顺序与数量有核对记录
4. 核验 ACS 会议服务：查 bics.conf、ping 专用 IP、查证书 SAN 三选二。完成标准：会议 FQDN 可解析且 SAN 覆盖
5. ACS 未配置或需变更时：跑 ot-config.sh --rehost，填会议 FQDN/域/专用 IP，确认内部 DNS 已有条目。完成标准：重启后 ping 会议 FQDN 通
6. 证书联动：ACS 名/IP 变更后重签 OT 证书并确认 SAN 含会议 FQDN（转证书能力五步清单）。完成标准：Details 页 SAN 核验通过

判停点：

- EVS 端口漏写 8016 → 停下补上，通知类功能会经反代失效（n32）
- 客户部署地非法国 → 停，10 条 DAS 示例必须按国家改写，照抄会成批错（n02）
- 内部 DNS 无会议 FQDN 条目 → 停，先补 DNS 再 rehost（n03 双强制之一）

输出契约：服务器侧就绪的远程访问配置（RP/OTSBC 申报落地 + DAS 规则核对记录 + ACS 会议 FQDN 与 SAN 核验结论）。

## B — 边界

- DAS 规则国家相关，书中 10 条全部为法国口径；声明顺序重要且多条可同时命中（n02）
- rehost 仅在 ACS 名/IP 未配置或需变更时执行；rehost 后证书重签是必做联动（p70/p77）
- 四 URL 的具体域名值与 IP 均为实验口径（见 book/overview）；生产按客户公网资源整体替换
- 申报入口依赖 OmniVista 8770 与 WebAdmin；无 8770 的纯 OT 环境不在本书展开范围（OTES 已退场）
- 会议服务专用 FQDN 必须同时进 RP 与 OT 证书 SAN、并进内部 DNS——两处系统都不会替你补（n03）
