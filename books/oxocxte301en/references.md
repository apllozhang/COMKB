# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| TC1143（Security recommendations for OXO Connect） | 访问控制/密码策略/网络安全远程接入/系统安全编程选项的总纲 | p299, p338, p382 |
| TC1398（OXO Connect Noteworthy addresses） | noteworthy 地址全量清单与附录偏移表——内存修改的唯一依据 | p578, p581 |
| TC2249 | XML 密码审计工具用法 | p323 |
| TC002_US.pdf | V24 远程接入与计费传输参数 | p297 |
| TC2349（WinPDM Release Note） | 8158s/8168s VoWLAN 话机部署工具 | p552 |
| 8AL90874USAA（SSK 手册） | DECT 站点勘测与工程规则 | p530 |
| OXO Connect Global Limits（MyPortal） | 全局容量限制的权威汇总 | p497 |
| hospitality ecosystem PDF（2025-11 版） | PMS/AHL 兼容清单 | p65, p68 |
| OXO Connect Cross compatibility（MyPortal） | 应用包与板卡兼容矩阵（LoLa 前置核对） | p591 |
| DSPP 白名单 | Open SIP 第三方话机兼容清单 | p143 |
| eBuy | ARI/PARI 唯一号获取 | p543 |
| RAINWTE012 | Rainbow 语音移动培训（本书移动章的姊妹篇） | p464 |
| MyPortal IPDSP 文档 | IPDSP 软话机安装细节 | p464 |

## 2. 官方站点与工具

| 站点/工具 | 用途 | 书内位置 |
|---|---|---|
| MyPortal | 下载软件/license、TC 文档、开服务请求 | p578, p586, p591 |
| Fleet Dashboard / OXO Connectivity / Business Store | Cloud Connect 三门户（同一账号） | p265-268 |
| al-enterprise.com / enterprise.alcatel-lucent.com | 门户域名两种写法并存（nr-05），以登录页为准 | p267, p272 |
| Webdiag（https://OXO@IP/services/webapp/） | 证书管理主接口、抓包、三会话调试 | p560 |
| Wireshark | SIP 抓包分析（实验机预装；任何抓包软件亦可） | p56 |
| MMC 话务员会话（话机 Operator session） | MoH/欢迎消息/AA/MLAA/ACD 语音录制入口 | p241, p256, p365, p443 |
| xBS 网页管理（默认 admin/00!） | DECT 基站管理 | p518 |
| WinPDM + Desktop Programmer | VoWLAN 话机部署 | p550-552 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g62（62 条）全部通过术语核验（concept 27 / role 5 / subscription 5 / product 11 / protocol 9 / resource 5）。
- 落位口径：GLOSSARY 全量收录（六类分组）；阶段 3 生成 `book/glossary.md`（全书 62 条按六域表格版式收录，与候选一一对应）。
- 缩写诚实口径：DDI、RSL、NMC、CTI、ADL、RPN、PLI、GSM 等书内未给全称或仅法文展开的，按原文收录不脑补；HAN 仅给 Home Area Network。
- 原文笔误备查：p107 "donn't"、p321 行尾杂符、p191/p345/p502 法文残句（nr-03）。

## 4. 实验环境口径备查（仅作 Boundary 背景与 book/overview，不进能力卡正文数值）

- RLAB POD 网段 192.168.1.x：Client PC .10 / OXO .246 / 网关 .254 / DNS1 .250 / DNS2 10.20.30.250；话机 DHCP 池 .30-.39（p34 口径；p40 检查清单写 .10-.39，见 nr-02）。
- 公共资源区 10.20.30.x：NAS（软件/license）、SIP 模拟器 12.0.0.2、外部 DNS 10.20.30.250。
- ITSP1 模拟器：gateway1.itsp1.com（10.20.30.51）/ public.itsp1.com（10.20.30.50）/ SIP 域 sip.itsp1.fr；账号 pbxP/alcatel（P=POD 号）；号码规则 PN=两位 POD 号（安装号 210P41000、DDI 41100-41199、话务台 41000、公网 33{1-5}1PN12345、紧急 112/15/17/18）。
- 出厂与实验口令表（全部实验口径，生产必改）：OMC 首连 pbxk1064（仅首连）；Webdiag installer 教室例 Alcatel1；OMC 代理参数 OMCAdmin；xBS 网页 admin/00!；实验远程接入码 780911/615243；8088 管理菜单 *tx8000#；DECT 服务菜单 *7378423*；实验账号 cCpP.admin@ale-training.com / Superuser-P*。
- 私网组网实验拓扑 N=POD 号（192.168.N.246），勿与其它 lab 产生 IP 冲突（p208）。
- 多实体链路类别实验值 1/2（讲义示例 3/4，见 nr-06）；DECT 实验 ARI 示例 110004360P0（P 换 OXO 号）。
