# OXE 接入 Rainbow 与接入排障（DNS/代理、PBXID/激活码、维护四抓手）

## R — 原文依据

> "The DNS and HTTP proxy configuration will only be used by Rainbow and Cloud Connect agents"（p78）
> "Warning URL PING DOESN'T VALID THE DNS RESOLUTION. Dig and nslookup commands allow to verify correctly the DNS resolution."（p82）
> "Warning NETWORK PREREQUISITES MUST BE COMPLETED BEFORE!"（p84）
> "4503=rainbowagent: WebSocket (rainbowagent<->Rainbow) in service … 4509=CSTA link (CSTA server<->Rainbow) in service"（p87）

出处：RAINXTE003EN p77-88。

## I — 自述

接入分三段，顺序不能倒：

1. **网络前提**：netadmin 配 DNS（菜单 14）与 HTTP 代理（菜单 15）——这两项只服务 Rainbow 与 Cloud Connect agent，配完没全局生效属预期
2. **验证手段**：DNS 解析必须用 nslookup/dig（URL ping 不算数）；HTTPS 测试只能用 IP 地址，curl 报证书错误属预期（ALE 专有证书，只有 OXE/OXO 认）
3. **接入启用**：Rainbow 端取 PBXID 与激活码，在 OXE webadmin（或 mgr）的 Rainbow 菜单 Enable Rainbow Agent 选 YES，填凭证后 Save

incvisu 五条链路健康口径（p87）：

| 事件码 | 链路 | 健康状态 |
|---|---|---|
| 4503 | WebSocket（rainbowagent 与 Rainbow 间） | in service |
| 4505 | XMPP link | in service |
| 4509 | CSTA link（CSTA server 与 Rainbow 间） | in service |
| 4507 | Config link（PBX config 与 Rainbow 间） | in service |
| 4511 | API_MGT link | in service |

维护四抓手：incvisu 看启动事件与五链路；dhs3_init -R RAINBOWAGENT 重启 agent；checkCloudConfig.sh -rainbow 核查云连接；more /var/log/rainbowagent.log 看日志。

## A1 — 书中案例

**DNS/代理与接入实验**（p77-88）：

1. netadmin -m 进菜单，选 14 DNS configuration、2 Create/Update，填主备 DNS 后保存
2. 选 1 View DNS configuration 复核地址生效
3. 代理走菜单 15（实验环境不需要代理，仅了解路径）
4. 控制台执行 nslookup 查 agent.openrainbow.com 解析，返回多个 IP 为通过
5. curl 用 IP 地址做 HTTPS 测试，返回证书校验错误但请求 OK（ALE 专有证书属预期）
6. Rainbow 管理端 My company、Communication、Comm. Servers 页签取 PBXID 与激活码（用复制功能防输错）
7. OXE webadmin Rainbow 菜单启用 agent，填凭证保存
8. Rainbow 端确认该 OXE 状态 running；OXE 侧 incvisu 五链路全 in service
9. checkCloudConfig.sh -rainbow 输出 DNS 解析、证书链与 Success 判定

## A2 — 未来触发

使用情境：把 OXE 接上 Rainbow；接入后状态不对；不知道 PBXID 从哪来；配 DNS/代理；curl 证书报错要不要紧。

语言信号：netadmin / DNS / 代理 / proxy / PBXID / 激活码 / activation code / Rainbow Agent / incvisu / 4503 / CSTA link / checkCloudConfig / rainbowagent.log / 连不上。

与相邻能力区分：

- 网关侧部署与升级 → 网关部署能力
- 云侧日志、状态页与 SR → 维护支持能力（路由卡）
- 接入成功后的分机绑定 → 分机关联能力（路由卡）

## E — 可执行步骤

输入契约：OXE 呼叫服务器维护账号、Rainbow 公司管理员账号、网络出口信息（DNS/代理/防火墙管控方）。防火墙不在自己手里 → 判停先找客户网络组。

1. 配 DNS：netadmin 菜单 14 填主备地址并保存。完成标准：View 配置显示新地址
2. 验解析：nslookup/dig 查 agent.openrainbow.com。完成标准：返回解析结果（不认 URL ping）
3. 验连通：curl 用 IP 做 HTTPS 测试。完成标准：证书报错但请求 OK 属预期，连通成立
4. 取凭证：Rainbow 端 Comm. Servers 页签复制 PBXID 与激活码。完成标准：凭证在手且未经手抄
5. 启用 agent：webadmin Rainbow 菜单 Enable YES、填凭证、Save。完成标准：Rainbow 端该 OXE 显示 running
6. 验链路：incvisu 查五链路。完成标准：4503/4505/4509/4507/4511 全部 in service
7. 归档：checkCloudConfig.sh -rainbow 输出与日志位置写入交付记录。完成标准：排障抓手已知

判停点：

- 网络前提没做完就想填凭证 → 停，先做步骤 1-3（顺序硬约束，p84 Warning）
- incvisu 五链路有缺 → 查 DNS/代理/防火墙后再重启 agent，不盲目重装
- 现场防火墙强制按域名放行 → OXE 的 HTTPS 测试只能用 IP，换防火墙侧手段验证，不虚构结果

输出契约：PBX-Rainbow 连接 established 的双侧证据 + 五链路状态记录 + 排障抓手清单。

## B — 边界

- DNS/代理配置只服务 Rainbow 与 Cloud Connect agent，不影响 OXE 其他功能（p78）——排障时先分清解析问题与连通问题
- curl 证书错误是预期行为（ALE 专有 CA，p82），不是"连不上"的证据
- 实验环境不需要代理；实验网段、维护账号与日志样例版本（rainbowagent 6.0.1）见 book/overview 环境区，均为实验口径
- 生产防火墙/代理细节、端口与域名清单在书外：以 Rainbow Network Requirements PDF 为准（n02）
- PBX 必须先由经销商在 Rainbow 侧创建——EC 管理员无此入口属权限设计（p39/p161）
