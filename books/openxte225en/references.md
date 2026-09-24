# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| TC2639（OpenTouch Remote Worker/Mobility Configuration Update） | 远程工作者/移动化配置总纲：iPhone 手工配置、RP 模板与下载链接更新、LDAP 认证细节、生产化必读 | p46, p105, p117, p140, p143, p220 |
| TC2257 / TC1990（from 0 to remote worker 两代） | 端到端远程工作者部署文档（TC2257 为 OTES 替代版）；OTSBC 手工配置补充 | p46, p117, p220 |
| TC2341en（OTC smartphone VoIP for Connection Users 部署指南） | 智能手机章节的生产化补充，直达链接 businessportal2.alcatel-lucent.com/TC2341en | p217 |
| TC1981 / TC1839（OTC Android R2.5 / iPhone R2.3 技术发布说明） | 移动客户端版本依据（组件版本节奏与教材主体不同） | p46 |
| 8AL90062USAG / 8AL90065USAG（OTSBC R2.x Release Note / Configuration Guide） | OTSBC 发布说明与配置指南：手工参数（如 OXE SIP 接口补 TCP）与容量口径的权威外链 | p46, p117 |
| nginx-ldap-auth（github.com/nginxinc/nginx-ldap-auth） | Nginx LDAP 认证模块官方开源项目（Python 2 脚本 + init 脚本） | p257 |
| nas.alcatel-support.com 模板链接（书中快照） | Nginx/RP 配置模板下载——官方明示以 TC2639 最新版链接为准（n35） | p220 |
| Business Portal | TC/8AL 文档族、OTSBC OVF 与配置向导软件的下载入口 | p46, p90, p101, p107 |

## 2. GLOSSARY 落位说明

- candidates/glossary.md g01-g62（62 条：概念 16 / 角色 2 / 许可 3 / 产品 21 / 协议 9 / 资源 11）全部通过术语核验；OVERVIEW 的 18 行候选术语逐条映射无遗漏（详见 glossary.md 收尾自检）。
- 落位口径：GLOSSARY.md 全量收录（六域分组）；阶段 3 生成 `book/glossary.md` 门户版（精选高频条目，保持第一本版式）。
- 仅 passing 提及未单列的词（RAP、DCS、IPG/Media Realm、CAC、RADIUS、OTCV/OTCT、N.U./N.A.、EVS/ACS/DMS、eDemo 营销页等）已在 glossary.md 收尾自检备查，不进主表。
- 缩写口径：DISA/CTL/CAC/DCS/DAS/OTES/SEPLOS/OTMS/OMS/EVS/ACS/DMS/IPG 等书中未给全称，一律不采信外部知识补全；CSR/SAN/APNS/PKCS7/PKCS12 等以书中展开为准。

## 3. 实验环境口径备查（仅作 Boundary 背景与 book/overview 素材，不进能力卡正文）

- 演示公网域 al-mydemo.com（ot-podx / conf-podx / otsbc-podx 三个公共 FQDN 后缀）↔ 内网域 company.com；公网段 195.128.146.10x、DMZ 11.1.1.x（RP 11.1.1.10、OTSBC 11.1.1.20）、内网 151.1.1.x。
- 关键虚机（实验口径）：OTMS opentouch.company.com=151.1.1.50、OmniVista 8770 nms.company.com=151.1.1.70、OXE csa/csm=151.1.1.1/151.1.1.3、FlexLM flex=151.1.1.80、OMS oms=151.1.1.13、SIP 模拟器 sippublic=151.1.1.105、Eco-system eco=151.1.1.100、ACS 专用 IP=151.1.1.55。
- 账号口令总表（p30，实验口径，生产必须全量替换）：OpenTouch SUSE root/superuser、WebAdmin otAdmin/Admin-8770、GUI 12345、TUI 54321、NMC Adminnmc/Superuser1*、OMS letacla1、Eco-system CA 网页 administrator/superuser（p72）、OTSBC 初始 Admin/Admin（p91-92）、Nginx 主机 rpuser/Sdfghjk1（p245）、AD 用户口令 1234；SIP 设备默认口令 0000 须改（n14）。
- 编号计划（实验口径）：存量用户 31000-31002、新建 31050-31052；副设备 2x31000；OTC PC 副设备 213100x；手机设备号 D21310xx、速拨号 A21310xx、Ghost Z 可用 B<数字>（B31091）；Nomadic 池示例 31017/31018 + SIP 设备 31951/31952；RE DISA 前缀 31280；RE DISA 公共号码 +3320131444；ARS 前缀 #0306；ARS Route list MAX ID=3999。
- DHCP 池：话机 151.1.1.151-159（OXE CS）、智能手机 151.1.1.160-165（Eco-system，RAP+物理设备时）。
- SIP 模拟器拨测预期（实验口径）：国内 0abcd31xxx（10 位）主叫显示 0298131000；国内规范 33abcd31xxx（11 位）显示 33298131000；国际 00ccabcd31xxx（13 位）显示 33298131000；末四位 31xx 即系统内分机。
- 环境版本坐标：Ubuntu 16.04.3 LTS（xenial）、ESXi 6.0/6.5、OTSBC/Mediant 7.2、APNS 根证书（Geotrust）有效至 2022——构成 R2.6 / 2017-2018 时代边界。
- 培训口径提示：Nginx 安装忽略 GPG 签名告警（n28）与内嵌 RP 无许可先测（n09）均为教学权宜，生产不可照搬。
