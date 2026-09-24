# POD 实验环境与运营商模拟器（RLAB 拓扑、POD 准备、ITSP1/ITSP2）

## R — 原文依据

> "OXE VMs used for this training are already configured (Database and Linux Data), such as: Software licenses are restored, SSH is enabled (mandatory since OXE Release N3)"（p38）
> "ITSP1 SIP Gateway 1 gateway1.itsp1.com 10.20.30.51 ... SIP domain: sip.itsp1.fr ... Id: pbxP password: alcatel"（p22）
> "ITSP2 SIP Gateway gateway.itsp2.com 10.20.30.60 ... Id: podP password: alcatel"（p30）
> "According to your POD number, configure 2 parameters in your external SIP gateway: Registration ID: pbxN"（p41）

出处：ENTPXTE403EN p3-42。

## I — 自述

教材实验在 RLAB 远程实验室进行，按 POD 划分同构单元（全虚拟化或混合模式）。环境三件：

| 件 | 内容 | 关键口径（全部实验口径） |
|---|---|---|
| 拓扑 | LAN 192.168.1.x / DMZ 192.168.2.x / 公共区 10.20.30.x | OXE CSA 192.168.1.1（物理）/1.3（主用）；OMS 192.168.1.13；SBC 192.168.1.105/192.168.2.205；ITServer（NTP+LDAP）192.168.1.252；DNS 内 192.168.1.250/外 10.20.30.250；FlexLM 192.168.1.80；远程办公虚机 podP-outside 10.20.30.2P |
| POD 准备四段 | 启动虚机、预配置核对、终端开通、公网接入 | 预配置基线：许可已恢复、SSH 强制（N3 起）、防火墙部分配置、NTP/FlexLM 已声明、DHCP 池 192.168.1.145-147、机架板卡在库；IPDSP 的 TFTP Server Main=192.168.1.3 |
| ITSP 双腿 | ITSP1 直连 / ITSP2 经 SBC | ITSP1：gateway1.itsp1.com（10.20.30.51）+公网网关（10.20.30.50），账号 pbxP/alcatel，DID 33210N41000 起范围 500；ITSP2：gateway.itsp2.com（10.20.30.60），账号 podP/alcatel，DID 33920x31000 起范围 1000 |

- 号码规则（PN=两位 POD 号）：紧急 112/15/17/18；国内 33{1-5}1PN12345；移动 3361PN/3371PN；国际（英国）4421PN；呼出变换 0110312345 → +33110312345
- 公网接入四格：外部网关 Registration ID=pbxN、Outgoing username=pbxN、DID 翻译首外线 33210N41000、首内线 31000 范围 500
- 混合模式差异：POE 交换机 192.168.1.12 下挂 ALE-500/300/20h/30h 物理话机；不需要 PC CLIENT 11；SBC 虚机延后启动

## A1 — 书中案例

**POD 准备收尾**（p35-42，How-To）：

1. 按模式启动虚机清单（SBC 延后；混合模式不开 PC CLIENT 11）。
2. 核对预配置：许可/SSH/防火墙/NTP=192.168.1.252/FlexLM=192.168.1.80/DHCP 池/机架板卡。
3. 开通 IPDSP（31000/31001），Settings/Network 填 TFTP Server Main=192.168.1.3。
4. 外部网关填 Registration ID=pbxN 与 Outgoing username=pbxN（N=POD 号）。
5. DID 翻译：首外线 33210N41000、首内线 31000、范围 500。
6. 拨公网号码验证外呼打通，作为后续全部实验的基线。

## A2 — 未来触发

使用情境：开课前/拿到 POD 后准备环境；实验里外呼不通先查哪；解释 ITSP 号码规则；区分全虚拟化与混合模式差异。

语言信号：RLAB / POD / 虚拟机 / 预配置 / IPDSP / TFTP / ITSP1 / ITSP2 / 运营商模拟器 / pbxN / podP / 33210N41000 / 33920x31000 / 号码变换 / 公共区。

与相邻能力区分：环境通了之后的一切交付动作 → 各开通/接入卡；SBC 与 ITSP2 对接 → SBC 运营商接入。

## E — 可执行步骤

输入契约：POD 号（决定全部号码与账号）、模式（全虚拟化/混合）、NAS 课件可达。POD 号未知 → 判停先确认，不猜号。

1. 启动虚机：按模式起清单，SBC 虚机延后到 SBC 章再开。完成标准：实例可达
2. 核对基线：许可/SSH/防火墙/NTP/FlexLM/DHCP/机架逐项过。完成标准：偏差清单为零
3. 开终端：IPDSP 建户并指向 TFTP；混合模式另核物理话机注册。完成标准：内线可打
4. 通外线：外部网关两格填 pbxN、DID 翻译四格按 POD 号填。完成标准：外呼打通
5. 记录口径：把 POD 号代入后的全部号码/账号登记成表，供后续实验引用。完成标准：环境卡在手

判停点：

- 外呼不通 → 先核 Registration ID/DID 翻译的 POD 号代入，再查信任主机，不乱改网关
- 误把 ITSP1 参数配到 ITSP2 腿 → 停，两腿口径不同（nr-04），分清腿再配
- 把实验 IP/口令当生产配置 → 停，全部实验口径（n45/n50）

输出契约：可用的 POD 环境 + 外线基线 + 实验参数代入表。

## B — 边界

- 全部 IP/账号/口令/号码为培训实验口径（n50），生产替换并加固；教室专用细节（虚机启动清单等）仅作背景
- 模拟器与真实运营商不等价：安全机制、编解码策略、REGISTER 行为差异大（n45），实验结论只证明"流程已通"
- 生产站点环境准备按 Starter 课程口径，非本卡四段（预配置由基线镜像代劳的部分要现场补做）
- ITServer 一机包办 NTP+LDAP 是实验简化，生产为独立工程（BOOK_OVERVIEW 批判口径）
