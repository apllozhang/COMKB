# references.md — 参考资源与术语落位（阶段 1.5 产出）

## 1. 原书指定的权威外部文档（能力卡 Boundary 的标准指针）

| 资源 | 用途 | 书内位置 |
|---|---|---|
| 8770 安装与容量规划指南（安装文档 + Capacity Planning tool V3.0） | 服务器/虚机规格、端口、安装细节——书内仅给工具名与部署形态 | p8 |
| OXE 技术文档（维护命令体系与 OID 含义） | siteid/netadmin/account compress 等命令体系、SNMP OID 含义（p512 Notes 明示 "refer to the technical documentation"） | p71-74, p93-95, p512 |
| SIP Carrier Simulator 使用文档 | ITSP1 模拟器操作与公网号码用法（p84 明示指针） | p53-58, p84 |
| A4400-RTM-MIB / UC-DAVIS MIB 技术文档 | Web Performance 各 OID 含义与阈值语义 | p492, p512 |
| 各国监管费率文件（如法国 ARCEP 的 SVA 资费） | 真实运营商价目与服务费费率来源——书内全用教学数值 | p137 |
| 当地话务数据留存法规 | 留存期限合规依据——书内 125 天是机制上限非合规结论 | p523, p529 |

## 2. 官方站点与工具（书内出现）

| 站点/工具 | 用途 | 书内位置 |
|---|---|---|
| ALE Knowledge Hub（enterprise-education.csod.com） | 培训评估与出席证书下载 | p646-648 |
| ToolsOmniVista.exe（C:\8770\bin\） | 组织更新/SNMP 轮询周期/证书等服务器端运维菜单 | p266, p293, p507 |
| Service Manager（Start > All Programs > OmniVista 8770 > Tools） | NMC Loader 停启触发加载 | p142 |
| 8770_NAS / SHARING | 实验资源盘与共享夹（ACCOUNTING_2025.txt、Telecom2_7x） | p49-50, p142, p245 |

## 3. GLOSSARY 落位说明

- candidates/glossary.md g01-g69（69 条：concept 30 / role 5 / subscription 3 / product 17 / protocol 8 / resource 6）全部通过术语核验（BOOK_OVERVIEW 术语表 18 行逐条映射无遗漏，详见 glossary.md 收尾自检）。
- 落位口径：阶段 3 生成 `book/glossary.md` 门户版（精选计费/性能主干术语，保持第一本版式）；全量 69 条以 candidates/glossary.md 为准。
- 20 余个仅 passing 提及未单列的词（ITSP2、TrapReceiver、Guacamole、Thunderbird、Wireshark、PuTTY、Notepad++、MindTerm、SLA、OOS、INTIP/IPMG/4645/IP-xBS、CAC、NOE、Compact Template、ACCOUNTING_2025.txt 等）已在 glossary.md 收尾自检备查，不进主表。

## 4. 实验环境口径备查（仅作 Boundary 背景，不进能力卡正文）

- RLAB POD 网段 192.168.1.x：OXE csa 物理 192.168.1.1 / csm 主 192.168.1.3；OMS 192.168.1.13；Client PC 192.168.1.10；8770 服务器 nms 192.168.1.70；FlexLM 192.168.1.80；网关 192.168.1.254；DNS 192.168.1.250 / 10.20.30.250。
- ITSP1 SIP 模拟器（公共区）：gateway1.itsp1.com 10.20.30.51、public.itsp1.com 10.20.30.50、SIP 域 sip.itsp1.fr；注册账号 pbxP/alcatel；号码含两位 POD 号 PN（公网主号 3321PN12345、安装号 3321PN41000）。
- 实验账号口径：8770 登录 AdminNmc/Superuser01*；OXE root/mtcl/Superuser2580*；FTP 用户 adfexc；cn=directory manager 口令 superuser；Tracking/报表收件 alban.podX@company.com。
- 教学数据：ACCOUNTING_2025.txt 测试票（≥168 张）、税率 US VAT 10% / 欧洲 TVA 20%、汇率 1€=1.21$ 或 1$=0.82€、报表实现章汇率 1.3（书内双口径，见 needs-review nr-01）。
- 实验加载性能：NMCLD_1.log 口径 9 张票 52 tic/sec（实验口径，非生产容量结论）。
