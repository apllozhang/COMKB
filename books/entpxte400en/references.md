# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| TC2005（SIP 运营商互联文档） | 公共 SIP 中继的运营商参数权威依据（号码格式/编解码/CLIR/紧急显示），原书明示"CONSULT THE DOCUMENTS" | p611, p636 |
| SA0046 | Voicemail phreaking prevention and security measures——4645 防盗打与安全措施 | p545 |
| TC1774 | Reinforce security on 46x5 voicemail systems——4645 加固 | p545 |
| TC3009 | ALE-120/AOM 供电与认证参考（2 台 AOM 配置、电源适配器） | p277 |
| ENTPXTE402 | Cloud Connect 章节外置课程（RTR/Fleet Dashboard 深度） | p813 |
| Advanced 培训 | CS Duplication 空间冗余、PCS、多节点组网细节 | p131 |
| CPU Loading 培训 | FlexLM 深度与 CPU 装载 | p219 |
| MyPortal 文档组（Sales Companion / OXE Feature list / OXE product limits / User manual / 话机 datasheet） | 产品限额、特性清单、话机参数的权威来源 | p297 |
| RFC 7913 / RFC 7315 | P-ANI（P-Access-Network-Info）私有头扩展定义 | p605 |
| RFC 1305 | NTP 协议标准 | p170 |

## 2. 官方站点与工具

| 站点/工具 | 用途 | 书内位置 |
|---|---|---|
| MyPortal | 文档/软件/许可下载、外置课程入口 | p297, p813 |
| ALE Knowledge Hub（enterprise-education.csod.com） | 培训评估与证书（培训流程，不入能力卡） | p815-821 |
| FlexLM 服务器 | 虚拟机/GAS 许可控制（OXE 侧经 WBM System/Licenses 对接，端口 27000） | p219 |
| Cloud Connect | 云侧运行权（RTR）与设备管理；UMC 入口之一（Fleet Dashboard） | p44, p200, p798 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g60（60 条，concept 18 / role 9 / subscription 6 / product 17 / protocol 6 / resource 4）全部通过术语核验；BOOK_OVERVIEW 19 行术语逐条映射无遗漏（ARS/NPD/DID translator 以机制并入相邻对象条目防重复，详见 glossary.md 收尾自检）。
- 落位口径：GLOSSARY 全量收录（按 concept/role/subscription/product/protocol/resource 六类分组）；阶段 3 生成 `book/glossary.md` 门户版（同构六域，保持第一本版式）。
- 仅 passing 提及未单列的词（SEPLOS、PCS、PWT、DECT 8378/8379、INTOF、NDDI、CampOn、NOS LED、EVA、TJ00302A、dhs3、abcacom.exe、ICE type）已在 glossary.md 收尾自检备查，不进主表。
- 全称只采信书中展开：PABX（p30）、MAO（p186）、NPD=Numbering Plan Descriptor（p596）、VPIM（p528）、ABC=Alcatel Business Communication（p38）、ACT=Alcatel-Lucent Crystal Technology（p70）、FXS=Foreign eXchange Subscriber（p75）、ACTIS（p201）；SRTP/DTLS/DDI/SIP/QSIG/ARS 等书中未展开的不做外部补全。

## 4. 实验环境口径备查（仅作 Boundary 背景与 book/overview 素材，不进能力卡正文）

- RLAB 网段：OXE 物理地址 csa=192.168.1.1、Role 地址 csm=192.168.1.3；OMS=192.168.1.13；FlexLM=192.168.1.80（端口 27000）；IT Server（NTP/邮件）=192.168.1.252；GD4=192.168.1.12；内部 DNS=192.168.1.250；外部 DNS=10.20.30.250；SIP 模拟器=12.0.0.2；网关 192.168.1.254；PC Client 分跨 192.168.1.10/11 与 192.168.2.10/11；话机静态示例 192.168.1.141、DHCP 池 192.168.1.145-149。
- 实验账号：mtcl=Administrator5689!；root/swinst/client=Superuser2580*；FlexLM root=letacla1；GD4 admin=letacla1、root=mg4.ale；OMS admin/root 均 letacla1（另有 kb/kb 改键盘）；GDXL root=mgxl.ale；IT Server=training/superuser；SIP 运营商=pbxP/alcatel；话机初始码 0000、话机 SFTP=admin/*tx8000#；Thunderbird 密码 alcatel。生产必须全部替换。
- 实验号码口径（ITSP1）：安装号 3321PN（PN=两位 POD 号）；DDI 段 41000-… ↔ 内部 31000-…；国内 33{1-5}1PN12345、移动 33{6,7}…、国际 4421PN…、紧急 112/15/17/18。
- 培训约定：空库国家码统一 FR；ISDN 用 ISDN France 变体、发送 10 位；抓取前缀 #010/#012；许可文件由讲师发放（TJ00302A 示例）；SIP 中继实验后外线留言回归测试（c22 注）。
