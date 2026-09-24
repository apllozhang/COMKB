# 企业认证集成（LDAP/RADIUS 下游认证与 Kerberos SSO 上游认证）

## R — 原文依据

> "'Downstream authentication' means that the user has not been authenticated before the client sends a request to the OpenTouch server ... protocols can be LDAP/LDAPS, Radius"（p418）
> "If external authentication fails, there is an automatic cascading to DTA for Web clients (WBM for Administrator…) • No automatic cascading for thick clients (OTC PC…)"（p426）
> "Once Kerberos has been enabled on the OpenTouch, the OmniVista 8770 client cannot access Web Based Management (WBM) anymore"（p430）
> "The value for 'External login' is unique in the OpenTouch configuration."（p454）

出处：OPENXTE301EN p415-467。

## I — 自述

外部认证是全局开关（不能按应用单独启用；IP Touch 应用与 TUI 例外，按话机号码认证），分两轨：

1. **Downstream（OT 验证用户）**：用户提交账密，OT 经 JAAS 链读 Authentication.xml 决定插件（本地 DTA / AlcLdap / AlcRadius），插件按 user.uid.attribute（AD 为 sAMAccountName）与 OT 用户 External login 匹配；多插件可级联，文件内顺序即尝试顺序
2. **Upstream（外部先验）**：Kerberos/NTLM V2——用 Windows 会话凭据换票据，OT 用 keytab 验票识人；经 authenticationbasic（厚客户端）与 authenticationform（Web）两个应用的 web.xml 模板重命名启用
3. **级联不对称**：外认失败时 Web 客户端（含 WBM）自动回落本地 DTA，厚客户端（OTC PC）不级联直接失败——LDAP 维护窗口要预告
4. **LDAP 插件参数**：必填 4 类——主/备服务器、basedn、login 属性、uid 属性；选填协议/端口/应用账号；改后重启 tomcatd，回退=还原备份再重启
5. **RADIUS 插件参数**：必填主/备服务器与 shared_secret；认证 1812/计费 1813（计费未用）、默认 pap、超时与重试可调
6. **Kerberos 四件套**：web.xml 模板重命名（thin/thick 两处）、krb5.conf、auth.config、ktutil 生成的 ice_kerb.keytab；AD 侧专用账号（不可改密+永不过期）+ setspn 注册 HTTP/短名与 HTTP/FQDN 两条 SPN

保命规则：启用外认前，管理员账号必须预先填 External login 并在外部服务器建好账密。

## A1 — 书中案例

**LDAP、RADIUS 与 Kerberos 三个实验**（p437-467）：

1. LDAP：逐用户填 External login（=sAMAccountName），管理员同样配置
2. LDAP：备份 authentication.xml 与 plugin_ldap.properties 后填参数（主/备/basedn/sAMAccountName，实验口径）
3. LDAP：删注释符启用插件，service tomcatd stop/start，验证登录与级联行为
4. RADIUS：填 plugin_radius.properties（1812/pap/shared_secret=training，实验口径），FreeRADIUS.net 服务器三文件就位
5. Kerberos：浏览器开集成 Windows 认证并加入站点
6. Kerberos：两处 web.xml 模板对调重命名，拷 krb5.conf 与 auth.config
7. Kerberos：ktutil 生成 keytab（密码必须与 AD 账号一致），AD 建 ice_kerb 并 setspn 注册两条 SPN
8. Kerberos：重启 tomcatd；AD 建 wbm_admin 并在 OT 建 WBM 管理员（Delegate authentication）
9. 验证：加域机器免密进 WBM 与 OTC PC；停用=web.xml 改回加重启

## A2 — 未来触发

使用情境：用企业 AD 账号登录 OT；Windows 单点登录；外认服务器维护窗口的预告；启用后配置工具进不去；移动端能不能 SSO；External login 规划。

语言信号：外部认证 / LDAP / LDAPS / RADIUS / Kerberos / SSO / 单点登录 / DTA / External login / sAMAccountName / keytab / setspn / SPN / krb5.conf / web.xml / impersonation 无关勿混 / WBM 管理员 / 级联 / cascade。

与相邻能力区分：LDAP 目录搜索（找人）→ 目录能力；Impersonation（Exchange 授权）→ UM 能力，三个 "LDAP/impersonation" 语境完全不同。

## E — 可执行步骤

输入契约：认证协议选型（LDAP/RADIUS/Kerberos）、外部服务器信息与账号治理、管理员账号清单、客户端形态分布（Web/厚/移动）。

1. 影响评估：全局生效范围（IP Touch/TUI 除外）+ 级联不对称预告。完成标准：影响面书面确认
2. 账号先行：所有用户与管理员填 External login，外部服务器建同名账密。完成标准：管理员可外部认证（防锁死）
3. 插件配置（LDAP/RADIUS）：先备份，填 properties 参数，启用插件后重启 tomcatd。完成标准：登录成功且失败回落行为符合预期
4. Kerberos（如选）：浏览器设置，web.xml 对调，krb5/auth.config 就位，keytab 生成（密码一致），SPN 两条，最后重启。完成标准：加域机器免密进入
5. WBM 保护：预建 AD 出身管理员（Application=WBM+Delegate authentication）。完成标准：8770 失效后仍有管理入口
6. 回退预案：还原备份文件/web.xml 改回 + 重启，演练一次。完成标准：可安全退出外认

判停点：

- 外部认证服务器不可达 → Web 端会自动回 DTA、厚客户端直接失败：维护窗口必须提前预告（n36）
- Kerberos 启用前发现管理员没配 External login → 停，先补配再启用，顺序颠倒=锁在门外（n37）
- keytab 验证全挂 → 查 keytab 生成时输入的密码与 AD ice_kerb 密码是否完全一致（n39）
- 同一 AD 名既给标准用户又给管理员 → 不允许（External login 全局唯一），重新规划命名

输出契约：影响评估与账号映射表 + 插件/Kerberos 配置存档（含备份位置）+ 登录与级联验证记录 + 回退预案。

## B — 边界

- Kerberos 覆盖面窄：仅 Windows 上的 Web 应用与 OTC PC；Android/iOS 不支持；不经反向代理（远程自动回落账密，n38）
- RADIUS 章 Notes 原文误写为"连接 LDAP 目录参数"，以参数名为准（nr-03）；FreeRADIUS.net 为实验工具，生产另选企业级 RADIUS
- LDAP 溢出上限"20 vs 5"口径冲突属目录域（nr-01）；本卡 LDAP 是认证语境
- 插件参数实验值（192.168.1.100/389/training/1234）必须替换；生产 Kerberos 深入以 TC1623 为准
