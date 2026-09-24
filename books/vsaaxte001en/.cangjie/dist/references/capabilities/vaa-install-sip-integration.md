# VAA 安装与 OXE SIP 对接接通（install.sh 参数契约、OXE 五段链、接通验证与排障）

## R — 原文依据

> "Important information to read carefully before installing VAA 4.8.006: • Only a fresh installation followed by a database restoration is supported. • A new license (Release 11) is required."（p89）
> "The parameter 'incoming username' must be defined in the SIP external gateway, you must define the same username! - No Password, leave blank - The parameter 'Minimal authentication method' must be set at - None"（p101）
> "Trunk group group ID: 10 ­ Trunk group name: SIPVAA1 ­ Q931 signal variant: ABC-F ­ Remote network: 10 ­ T2 specification: SIP"（p107）
> "From a computer (or softphone), call the number 31400 corresponding to tree just created. You should hear the 'welcome' message and the system should hang up automatically."（p118）

出处：VSAAXTE001EN p76-121。

## I — 自述

本能力覆盖"从裸机到拨通测试树"的完整交付闭环，四个知识块：

1. **安装方式三选一**：手工（教材主线，SUSE ALE BootDVD + install.sh 交互）、S.O.T 自动（装系统/配网/改密/装许可/装 VAA 一条龙，只能用自签证书、incoming username 固定为 vaa）、Purple on Demand。4.8.006 只支持"全新安装 + 数据库恢复"，且强制 Release 11 新许可
2. **install.sh 参数清单（双侧契约）**：

   - 本地 IP 确认；HTTPS 证书（/tmp 无证书则自签）；OXE 主/备 IP（无备用重填主 IP）
   - incoming username（无密码留空）；编解码勾选 G711a/G711mu/G729（要用语音识别必须 G711）
   - HTTP 代理、SMTP 邮件通知、转移禁拨前缀（生产必配，实验留空）、数据库自动备份
   - SIP TLS/SRTP、PostgreSQL 密码、远程 syslog、许可文件（/tmp 的 .vaa 自动发现）
3. **OXE 侧五段配置链**：

   - SIP trunk group：T2 型、Q931 变体 ABC-F、独立 remote network、T2 specificity=SIP、直连 RTP 否
   - 本地 SIP 网关联动（初始化 SIPMOTOR）；外部网关（type=VAA、端口 5060 UDP、监督定时器 60、incoming username 与安装一致）
   - 信任 IP 与网络路由表；前缀计划（前缀 314、网络 10、5 位）
   - 全局参数：DPNSS 599 路由优化、外部回叫翻译去 "0B" 显示、编解码两侧匹配
4. **接通验证与四层排障**：WebAdmin 建测试公司 + 最简树（Start/Announcement/Hang up）绑 31400 激活，拨号应听欢迎语后自动挂断。排障四层：trkstat 中继状态、sipextgw 网关状态、OXE 抓包（motortrace/mtracer）、VAA 侧 softcmp (SIP) 日志

安装前置还有 OXE 底座准备：虚机核对、用户开通、DID 翻译、防火墙把两台 VAA 加为信任主机（netadmin -m 菜单）。

## A1 — 书中案例

**安装与接通实验**（p88-121，实验口径）：

1. root 首登改密（最少 20 位），admin 改密（最少 12 位），设 GRUB 口令（最少 14 位）
2. 配网五参数：IP、FQDN（形如 vaa1.company.com）、掩码、网关、DNS
3. FileZilla SFTP 传发行包 zip 到 /home/admin，license 文件 .vaa 到 /tmp
4. sudo su 后 unzip，进入发行目录执行 sudo ./install.sh
5. 本地 IP 确认答 y；证书选"稍后提供"，系统生成自签证书
6. 填 OXE 主 IP（实验 192.168.1.3），无备用则再填同值
7. incoming username 填 vaa1，密码留空（与 OXE 外部网关完全一致）
8. 编解码空格键勾选 G711a 与 G729（实验口径）；代理 N；SMTP 配置后继续
9. 禁拨前缀实验留空；自动备份启用（Daily 午夜）；SIP TLS 选 N
10. PostgreSQL 口令与远程 syslog 按实验值填写；许可自动发现 /tmp 下 .vaa 文件
11. OXE 侧按五段链建 trunk group 10 / 外部网关 VAA1 / 信任 IP / 路由 / 前缀 314
12. WebAdmin 首登（admin/admin 强制改密），建测试树绑 31400 并激活
13. 验收：vaa status 全部 Running；拨 31400 听到欢迎语后系统自动挂断

## A2 — 未来触发

使用情境：新装 VAA 服务器；装完 Web 打不开或服务没起来；拨测试树不通；OXE 侧中继/网关参数核对；G729 与语音识别冲突；S.O.T 与手工安装怎么选；4.8.006 能不能原地升级。

语言信号：install.sh / 安装 VAA / incoming username / 编解码 G711 G729 / trunk group / ABC-F / 外部网关 / SIPMOTOR / 信任 IP / trkstat / motortrace / 31400 / 接通 / 自签证书 / Release 11。

与相邻能力区分：双机部署与切换测试归 HA 能力；日常巡检备份归维护能力；证书生成细节与 XCA 操作见本卡 E 段与安装指南 6.4 指针。

## E — 可执行步骤

输入契约：服务器规格与虚拟化平台已定、许可文件（.lic/.vaa，绑定 MAC/FQDN）、OXE 主备 IP、客户 SMTP、证书文件（生产建议提前生成，PKCS12 或 PEM 放 /tmp）。缺许可或证书时 install.sh 仍可走通（自签兜底），但生产交付前必须补齐。

1. 核对前置：规格三档表初筛（p52，示例口径）、Hypervisor 兼容前提、root 禁止 SSH（用 admin + sudo）。完成标准：硬件/版本/许可三前提就位
2. 系统准备：ALE BootDVD 装 SUSE，root/admin 出厂口令首登即改，GRUB 口令最少 14 位。完成标准：能以 admin SSH 登录并 sudo su
3. 配网与传输：按现场五参数配网；SFTP 传发行包到 /home/admin、许可到 /tmp。完成标准：两个文件各就各位
4. 执行安装：sudo ./install.sh 按参数清单逐项应答；incoming username 现在定死并记录。完成标准：安装完成无报错
5. 验收服务器：vaa status 全部 Running；浏览器打开 https://VAA-IP 能见 Web 界面。完成标准：管理面可达
6. OXE 侧对接：按五段链配 trunk group、外部网关（网关类型 VAA、incoming username 与步骤 4 一致）、信任 IP、网络路由表、前缀计划；防火墙把 VAA 地址加入信任主机。完成标准：trkstat 中继与 sipextgw 网关状态正常
7. 接通验证：建测试公司与最简树，绑测试号并激活，软话机拨打应听欢迎语后挂断。完成标准：闭环打通
8. 排障（如不通）：按四层顺序查——中继状态、网关状态、OXE 抓包、VAA softcmp (SIP) 日志；先核对 incoming username 一对字符串。完成标准：定位到具体一层

判停点：

- 呼叫建立异常疑似编解码问题 → 先核对 OXE 设置或禁用压缩快速止血，再回查两侧编解码匹配
- 生产环境客户现场 SIP 参数已存在 → 停，原书明确"已有参数不要改"，按现场编号计划适配而非照抄实验值
- 需要端口清单或完整安装步骤 → 停，指向 VAA Installation Guide（4.2/第 6 章），不以实验口径搪塞
- 要用语音识别而编解码已勾 G729 → 停，回退安装步骤改 G711，装完再改要动 vaa.conf

输出契约：可登录的 VAA 服务器（vaa status 全 Running）+ OXE 侧五段配置记录 + 拨测通过的测试树与绑定号。

## B — 边界

- 版本陷阱：4.8.006 唯一支持路径是"全新安装 + 数据库恢复"，无原地升级；旧许可直接失效（n01）
- 实验口径：实验密码（InternationalSuperuser1234* / Superuser1234* / letacla1 出厂值）、实验 IP（VAA 192.168.1.55 / OXE 192.168.1.3）、SIP TLS 选 N、禁拨前缀留空——生产必须替换并逐项启用安全项（n43/n49）
- 转移禁拨前缀实验"Not used in the lab"一句带过，生产不配等于开放外部 callers 借 VAA 外转（n43）
- OXE 侧只给参数表不讲原理（ABC-F 语义、remote network 取值依据在书外），默认读者会 OXE 运维
- 端口清单（p55）与完整安装步骤外置到官方安装手册；规格表两处标注"仅示例，务必查官方文档"（n03）
- SIP TLS/SRTP 激活需 OXE 与 VAA 双方有效证书，全书无加密交付实验（p102）
- 经 SIP 模拟器外线测试失败先禁用 Allow Direct RTP——实验环境特有坑，生产不可照搬（n41）
