# Call Server IP 寻址与内部防火墙（netadmin、Role 地址、iptables 可信主机）

## R — 原文依据

> "An IP address is linked to the CS physical interface (Ethernet) • This address can be used to access to the Call Server, whatever the Telephone Application status"（p129）
> "The 'MAIN' IP address will have to be used by all the devices that have to access to the system's MAIN CS"（p131）
> "TO TAKE THE MODIFICATION DONE VIA THE NETADMIN MENU INTO ACCOUNT, IT IS MANDATORY TO RESTART THE SYSTEM"（p148）
> "Chain INPUT (policy DROP …) … Chain FORWARD (policy DROP …) … Chain OUTPUT (policy ACCEPT …)"（p140）

出处：ENTPXTE400EN p126-163。

## I — 自述

理解 OXE 网络的钥匙是双地址体系，互通的钥匙是防火墙白名单：

1. **双地址**：物理接口地址任何时刻可达（含话务停止——恢复备份传文件必须用它）；Role MAIN 地址仅话务运行时生效，所有设备与外部应用统一指向它；主备共享 Role 地址（同子网=本地冗余、跨子网=空间冗余）
2. **netadmin 硬规则**：特殊场景用菜单模式 netadmin -m；节点名全系统唯一；默认域名 oxedomain.com 会致证书错误，应配客户合法注册域名；一切改动必须 Apply + 重启系统生效
3. **防火墙策略（N3 起默认最高安全）**：INPUT/FORWARD 默认 DROP、OUTPUT 默认 ACCEPT；回环与 ICMP 放行；R101.0 起为完整 iptables
4. **可信主机**：入列=对该主机全端口全服务放行（服务自身认证仍生效）；支持单主机/网段/域名/CSV 批量导入导出
5. **便门纪律**："Allow SSH for all"（tcp 22 全放行）是开局/迁移临时便门，须客户同意，配完可信主机必须 Deny 回去——Deny 不删规则，可信主机仍可 SSH
6. **隐式联动**：配了 DNS 就必须把 DNS 服务器 IP 加白；DHCP 池地址由 MAO 自动入规则且 netadmin 不可改

## A1 — 书中案例

**IP 配置实验**（p145-155，How-To）：

1. mtcl 登录跑 netadmin 完整安装：节点名 oxe、CPU 名 csa、地址 192.168.1.1（实验口径）
2. 域名改为 company.com（实验口径），默认 oxedomain.com 会致证书错误
3. 临时开 Allow SSH for all 并应用，重启系统生效
4. netadmin -m 菜单 5 加 Role 地址：csm=192.168.1.3，Apply 后再重启
5. 核对：netadmin -m 选 2 显示 csa/csm/网关与动态端口区 10000-10499
6. Putty SSHv2 用 mtcl 登录 Role 地址，横幅显示 Role MAIN

**防火墙实验**（p156-163，How-To）：

1. root 登录，netadmin -m 菜单 11 Security → 1 Firewall(iptables) Configuration
2. 先关回 SSH-for-all 便门（如开过）
3. 受限访问配置里加可信主机 PC10 与网段 192.168.2.10-11
4. 应用后用 Putty 验证：白名单内可 SSH，PC11 被拒
5. CSV 批量导入：FileZilla 传规则文件到 /tmpd，Bulk Import 后核对并应用

## A2 — 未来触发

使用情境：新装机网络规划落地；改 IP/网段；证书错误；"网络通不了 OXE"；要放行某台管理机或网段；开局便门收口；DNS/DHCP 与防火墙联动疑问。

语言信号：netadmin / Role 地址 / 物理地址 / csa / csm / iptables / 防火墙 / 可信主机 / trusted host / 白名单 / SSH for all / oxedomain / 重启生效 / 批量导入。

与相邻能力区分：登录账户与密码见首登加固能力；话机 DHCP 服务见用户终端开通能力；恢复备份时连不上见备份恢复能力（路由卡）。

## E — 可执行步骤

输入契约：网络规划表（节点名/物理与 Role 地址/掩码/网关/域名）、可入白名单的管理终端与网段清单、防火墙管控权。规划表缺失先找客户网络组，不要现场拍地址。

1. 落地址：netadmin 完整安装或菜单模式配节点名/物理地址/掩码/域名/默认路由（域名勿留默认 oxedomain.com）。完成标准：地址表与规划一致
2. 配 Role 地址：netadmin -m 菜单 5 加 csm 及地址，Apply（NGINX 重启）。完成标准：Role 表就位
3. 开临时便门（如远程施工需要）：Allow SSH for all，须客户书面同意。完成标准：便门开通且记录
4. 重启系统使 netadmin 生效（强制）。完成标准：新地址可达，设备指向 Role 地址互通
5. 配可信主机：netadmin -m 菜单 11 → 1 → 3 逐台/网段/域名添加，或 CSV 批量导入（文件放 /tmpd）。完成标准：白名单核对无误
6. 收口：Deny SSH for all 并应用，用白名单外终端验证被拒。完成标准：便门关闭，仅白名单可达
7. 巡检：iptables 视图核对放行来源；ifconfig 核对 eth0/eth0:0。完成标准：规则与台账一致

判停点：

- "配了没生效" → 停，netadmin 改动必须 Apply+重启（p148），两步缺一即无效
- 白名单里出现"没配过"的放行条目 → 多为 DHCP 池自动入列或 DNS 联动（n21），不是入侵，回 WBM/netadmin 对账
- 客户要求长期保持 SSH-for-all → 停，说明默认全关的安全设计与便门定位，转客户安全流程审批
- 话务停止后连不上 Role 地址 → 属正常（地址仅话务运行时生效），改用物理地址（n08）

输出契约：双地址可用的 CS + 白名单生效的防火墙 + 便门收口确认。

## B — 边界

- 实验地址（192.168.1.1/.3 等）为实验口径，生产按客户网络规划；DNS 服务器 IP 加白是书内明示的联动规则（p138）
- 本卡默认"单机 stand-alone"口径；跨子网空间冗余、ABC-F 组网在 Advanced 课程（n42）
- CHAP/ICMP/SSH/SSL/PKI/AIDE 等 Security 其余子菜单本书只点名未展开；RADIUS 服务器接入配置不在实验链内
- CSV 导入文件无表头、逗号分隔，两种行格式 TRUSTED_HOST/TRUSTED_RANGE（p139，Addres 为原文笔误）；导出固定路径 /tmpd/export_th.csv
