# 反向代理两路线部署与选型（OTSBC 内嵌 RP、独立 Nginx、LDAP 认证）

## R — 原文依据

> "RP features embedded in OT SBC can be used since OTSBC release 7.2 … Import RP configuration files (based on templates): template_interface_ed02.ini (optional…) template_rp_ed02.ini, template_ldap_ed02.ini: optional (for external LDAP authentication)"（p128）
> "Standalone Reverse Proxy … Virtual machine creation, Operating system installation (Ubuntu or other), Ethernet interfaces configuration, Ngnix package installation…"（p129，Ngnix 系原文拼写笔误）
> "The NGINX configuration has changed since release 2.2. … It is why there are now two configuration files to modify: remoteworker.conf, conference.conf"（p253）
> "WARNING: A DEDICATED MACHINE IS NECESSARY TO RUN THE LDAP-AUTH DEAMON."（p140）

出处：OPENXTE225EN p118-130, p131-144, p218-259。

## I — 自述

反代是第三方职能，两条路线功能同向，选型逻辑：已有 OTSBC 且许可允许，内嵌省一台机器；需要独立扩展或已有 Nginx 运维，用独立 VM。两条路线都要在 OT 侧完成 RP 申报（四公共 URL，转 OT 服务器侧设置能力）。

路线对比：

| 维度 | 路线 A：OTSBC 内嵌 RP | 路线 B：独立 Nginx VM |
|---|---|---|
| 版本前提 | OTSBC 7.2 起 | 通用（OT 2.2 起双 conf 规则） |
| 许可 | 需 HTTP Proxy Available（实验无许可可先测） | 无（开源） |
| 证书 | RP 专用证书：Subject=OT 公共 FQDN、SAN=会议 FQDN | rp.crt/rp.key 部署到 /etc/nginx/cert |
| 配置载体 | 三份模板 ini：interface 可选、rp 必须、ldap 可选 | 三份 conf：global/remoteworker/conference + snippets |
| 认证 | template_ldap_ed02.ini，daemon 需专用机器 | nginx-ldap-auth 模块，daemon 与 Nginx 同机监听 8888 |

内嵌 RP 前提三项：核验许可、SETUP/IP NETWORK/HTTP PROXY/General Settings 里 Enable 并配主备 DNS、备好 RP 专用证书（或复用 OTSBC 证书但必须补 OT+会议公共名为 SAN）。

Nginx 侧文件结构（OT 2.2 起）：

- global.conf 改 resolver 指内网 DNS
- remoteworker.conf 改 server_name 为 OT 公共 FQDN
- conference.conf 改 server_name 为会议公共 FQDN——两份必须同改（OTES 退场、会议应用共享改走反代）
- snippets/opentouch_fqdn.conf 改 11 个 FQDN/IP 变量
- 校验链 nginx -t 后 start/restart

LDAP 认证（生产推荐、两条路线的实验都跳过）：官方建议反代带认证；Nginx 实现为 Python 2 脚本 nginx-ldap-auth-daemon.py（版本 3 明确不支持）+ init 脚本；不开认证测试时注释掉 remoteworker.conf 的 AUTH LDAP 段。

## A1 — 书中案例

路线 B 主线（Nginx，p218-259，实验口径网络值见 book/overview）：

1. 从 TC2639 最新版链接下载模板文件（书内快照链接可能过期）
2. ESXi 建 Ubuntu 64 位 VM（1 vCPU、2 GB 内存、20 GB thin、1 网口接 DMZ）并装系统
3. sources.list 追加 Nginx mainline 源两行后 apt-get install nginx（实验遇签名告警选 Y，教学口径）
4. FileZilla 拷入 CA 根证书并 update-ca-certificates；openssl 生成 rp.key 与 rp.csr 后送 CA 签发
5. rp.crt/rp.key 移入 /etc/nginx/cert，改 snippets 两份 ssl conf 的证书路径
6. 三份 conf 移入 /etc/nginx/conf.d/：global.conf 改 resolver、remoteworker.conf 与 conference.conf 改 server_name
7. snippets/opentouch_fqdn.conf 改 11 个变量（OT 公共名/域、内部名/FQDN/IP、8770 管理名、ACS 簇名等）
8. nginx -t 校验通过后 /etc/init.d/nginx start（原文两处误写 inid.d，见 needs-review nr-02）
9. 需认证时装 python（仅版本 2）与 python-ldap，部署 daemon 并改 snippets/ldap.conf，监听 8888

路线 A 对应动作（p131-144）：核验许可、Enable HTTP proxy 并配 DNS、建 RP-Conf 证书上下文、建 RP 专用 IP 接口、改 template_rp_ed02.ini 的 12 处映射后经 Auxiliary Files 上传。

## A2 — 未来触发

使用情境：给远程接入配 Web 服务通道；OTSBC 7.2+ 环境评估"要不要单台反代"；会议里应用共享经反代不可用；反代层要接公司 AD 认证；模板下载链接失效。

语言信号：反向代理 / Reverse Proxy / RP / 内嵌 / embedded / HTTP proxy / Nginx / Ubuntu / remoteworker.conf / conference.conf / snippets / resolver / LDAP / 8888 / nginx -t / 模板 / TC2639。

与相邻能力区分：

- 装 OTSBC 本体 → OTSBC 部署能力
- 反代的公共 URL 申报 → OT 服务器侧设置能力
- 反代证书签发 → 证书与 PKI 能力
- 架构取舍 → DMZ 双边缘能力

## E — 可执行步骤

输入契约：路线选型结论、模板文件（TC2639 最新版链接）、证书与私钥、内网 DNS 地址、认证诉求（是否 LDAP）。

1. 选型：OTSBC 7.2+ 且许可含 HTTP proxy、无需独立扩展 → 路线 A；否则路线 B。完成标准：选型结论带许可核验记录
2. 取模板：按 TC2639 最新版给定的链接下载，不用书内快照 URL。完成标准：模板版本可追溯
3. 路线 A：Enable HTTP proxy 并配 DNS，建 RP-Conf 证书上下文，建 RP 专用 IP 接口，改 template_rp_ed02.ini 12 处映射后上传。完成标准：HTTP Proxy Servers 页配置生效
4. 路线 B：建 Ubuntu VM、装 Nginx、部署 rp.crt/rp.key、改三份 conf 与 snippets 变量。完成标准：nginx -t 无报错
5. 认证决策：生产建议带认证；路线 A 需为 LDAP-auth daemon 备专用机器，路线 B 装模块并改 ldap.conf。完成标准：认证形态与资源归属写入方案
6. 联动确认：OT 侧 RP 申报四 URL 已指向本反代（转 OT 服务器侧设置能力）。完成标准：客户端可按公共 URL 回连

判停点：

- 客户环境只有 Python 3 → 停，Nginx LDAP 模块明确不支持 Python 3（n26），替代方案在书外
- 想把内嵌 RP 的认证 daemon 塞进 OTSBC 同机 → 停，原书 Warning 要求专用机器（n10）
- 拿到旧版模板或失效链接 → 停，必须以 TC2639 最新版为准（n35）
- 生产部署照抄实验"忽略签名告警装包" → 停，先导入官方签名公钥（n28）

输出契约：可用的反向代理（路线 A 或 B）+ nginx -t 或 HTTP Proxy Servers 核验记录 + 认证方案与资源归属说明。

## B — 边界

- OT 2.2 起必须 remoteworker.conf 与 conference.conf 同改；旧口径"只改一份"对 2.2+ 不成立（n25）
- 反代认证在两条路线的实验里都被跳过（"本实验不实现"），但它是生产必答题（n10）
- LDAP 模块仅支持 Python 2；Ubuntu 16.04/xenial 为教材时代口径，生产按受支持版本矩阵替换（n26/p31）
- 会议 FQDN 必须在反代证书 SAN 内（n03 联动证书能力）；EVS 通知端口 8016 的 server 段在 V1.5 模板中已含
- 实验网络值（IP/域名/口令）不进本卡，见 book/overview 环境区
