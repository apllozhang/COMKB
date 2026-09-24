# VAA WebAdmin 管理面（初始管理、管理员账号、SMTP 告警、日志与许可页）

## R — 原文依据

> "Login: admin - Password: admin … The password for the admin account must be changed on 1st connection."（p22）
> "Warning BY DEFAULT THE PASSWORD OF THE NEW ACCOUNT IS IDENTICAL TO THE IDENTIFIER OF THE LATEST."（p128）
> "Configure / modify settings for SMTP notification - SMTP notification enabled: yes … Warning SERVICES MUST BE RESTARTED AFTER SMTP CONFIGURATION"（p130）
> "Don't use these buttons unless instructions from the technical support team"（p131）

出处：VSAAXTE001EN p22-39, p127-132。

## I — 自述

Web 管理面的初始管理清单：

1. **登录与首改**：默认 admin/admin，首次登录强制改密；入口为 https://主机名或IP（4.6.104 起仅 HTTPS）；About 页看版本/许可端口数/服务器信息
2. **管理员账号体系**：超管可建公司（数量不限）；管理类角色含公司管理、全量路由（Full Routing）、用户管理（能建普通用户建不了管理员）

   - 功能类角色按页签派发（Routing/Prompts/Directory/Filters/Calendar 等）
   - 新建管理员默认密码=其用户名，建完必须立即改密
   - 受限用户档案（Advanced user profile）只开放局部功能如问候语控制，适合把改欢迎语下放给非管理员
3. **Settings 页签**：SMTP 通知配置（enabled/server/port/协议/认证/发件与收件地址）——改完必须重启服务才生效；另有 SNMP、PBX、security parameters（密码有效期等）设置
4. **Administrator menu 四页**：

   - Server info（服务器系统信息）；Supervision（各服务状态与停止/重启按钮——无技术支持指示不要用）
   - Logs（五类日志：aa-media-server 主日志/aa-management/aa-engine/softcmp (SIP)/tts-hub，选类型、定行数默认 200、Refresh 查看）
   - License server 页签（当前许可内容与占用）

## A1 — 书中案例

**初始管理实验**（p127-132，实验口径账号）：

1. 登录 https://192.168.1.55（admin，用改后的强口令）
2. 点头像图标进入 Administrators 页
3. 输用户名 letacla 建第二管理员（可填姓名与邮箱）
4. 记住警告：新账号默认密码=用户名，立即登录改强口令
5. 浏览 Server info 页确认服务器信息
6. Settings 页配 SMTP：enabled yes、服务器/端口/协议/发件收件按实验值
7. 保存后按警告重启服务使 SMTP 生效
8. Logs 页签逐一查看五类日志并试选 softcmp (SIP)
9. License server 页签核对许可内容与占用

## A2 — 未来触发

使用情境：交付收尾加管理员；告警邮件不发；给前台开"只能改欢迎语"的受限账号；管理员被锁；查某类日志；看许可占用。

语言信号：WebAdmin / 管理界面 / admin/admin / 管理员 / administrator / 角色 / roles / 受限用户 / user profile / SMTP / 告警通知 / Supervision / 日志 / logs / softcmp / License / 第二管理员。

与相邻能力区分：密码策略数值与 unlockAdmin 命令归维护能力；softcmp 日志用于接通排障归安装对接能力；许可体系全貌归 PCS/OPEX 卡；统计报表页归统计能力。

## E — 可执行步骤

输入契约：管理员名单与分工（谁管公司/谁管路由/谁管用户）、客户 SMTP 参数、日志取用场景、技术支持介入状态（Supervision 按钮使用前提）。

1. 首改密码：admin/admin 登录后立即设强口令（至少 12 位四类字符）。完成标准：默认口令失效
2. 建管理员：按名单建账号，建完立即改密（默认密码=用户名）。完成标准：无"用户名即密码"账号
3. 派角色：管理类（公司/全量路由/用户管理）与功能类按需勾选；前台改欢迎语用受限档案。完成标准：权责矩阵落地
4. 配 SMTP：Settings 页填服务器/端口/协议/发件收件，保存后重启服务。完成标准：测试告警可达
5. 熟悉四页：Server info/Supervision/Logs/License server 逐页过一遍。完成标准：运维人员会取日志看许可

判停点：

- 改完 SMTP 告警不发 → 停，先确认服务是否重启过（原书大写警告），再查网络（n14）
- 想用 Supervision 页按钮日常重启 → 停，原书明确无技术支持指示不要用（n15），走 SSH vaa restart
- 新建账号没改密就交付 → 停，等同全系统最弱入口，必须回改（n13）
- 需要 SSO/多因子等登录加固 → 停，书内无此内容，指向官方最新文档核实

输出契约：管理员与角色清单（无弱口令）+ SMTP 告警生效确认 + 管理面四页巡检记录。

## B — 边界

- 实验口径：实验地址与账号值（含第二管理员 letacla、实验 SMTP 服务器）仅限实验环境，生产替换（n49）
- 新建管理员默认密码=用户名是产品行为，流程必须内置"立即改密"（n13）
- Supervision 页停止/重启按钮仅限技术支持指示场景（n15）
- 管理界面仅 HTTPS（4.6.104 起）；证书体系与自签边界归安装对接能力
- 管理员锁 2 小时自动解锁与 unlockAdmin 命令细则在维护能力卡（本卡只给入口）
- OXE 电话簿同步进目录属破坏性操作，在树设计能力卡边界中（本卡不展开）
