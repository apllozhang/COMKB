# OXE 纳管与 SIP 中继对接（信息核查、节点声明、同步验证、模拟器对接）

## R — 原文依据

> "Subnetwork – Node number: Enter a numeric value equal to the OmniPCX Enterprise network*100 + OmniPCX Enterprise node number. Example: With a network number = 1 and node number = 2, you must enter 101"（p77）
> "All hosts machines involved with OXE Call Server must be declared."（p74）
> "Alarm reception mode Select Permanent IP connectivity. The OmniVista 8770 server establishes a permanent IP connection to receive alarms and events."（p77）

出处：8770XTE201EN p70-84。

## I — 自述

纳管一台 OXE 分三段：先在 OXE 侧核查，再在 8770 侧声明，最后同步验证。

- OXE 侧核查：siteid 看节点号/网络号；netadmin -m 选项 5 查主地址（空间冗余记两个）；选项 2 确认 SSH=yes，配 netstat -an | grep :22 应 LISTEN；选项 11 核对信任主机表含 8770/OMS/PC 等全部相关主机
- 8770 侧声明三级对象：Network（名称/号码自由）> Subnetwork（号必须=OXE 网络号）> OmniPCX Enterprise 节点（Subnetwork-Node number=网络号×100+节点号；IP 填 csm 主地址）
- 节点关键字段：FTP 用户 adfexc + 密码（数据取回凭证）；勾 Process configuration 与 Directory Process；告警模式=Permanent IP connectivity；Software download 页签填 mtcl 维护账号；Connectivity 页签勾 SSH 并填唯一 Host name（MindTerm 据此生成公钥）
- 同步二维选择：Complete（全部条目）/Partial（仅用户/目录/数据终端/缩位拨号/远端用户按上次日期增量）；Separate（仅本机）/Global（级联关联 OpenTouch）
- 验证：成功提示 + Configuration 树生成 OXE 分支 + Data Collection 页签显示最近修改时间；日志 NMCSyncLdapPbx_1.log

SIP 运营商模拟器对接（实验环境）只需两处：

- SIP > SIP Ext Gateway 选 ITSP1_GW1：Registration ID 与 Outgoing username 填 pbxN
- Translator > 1 > External Numbering Plan > 1 > Default DID num. translator 建 DID 翻译：First external=33210N41000、First internal=31000、Range size=500（N=POD 号）

## A1 — 书中案例

**OXE 节点注册实验**（p70-80）：

1. PuTTY SSH 连 csm 主 IP（实验口径 192.168.1.3），执行 siteid 确认节点号/网络号均为 1
2. su - 切 root 后 netadmin -m：选项 5 确认主地址 csm=192.168.1.3
3. 选项 2 确认 "Security with SSH: yes"；netstat -an | grep :22 应 LISTEN
4. 选项 11 Security > Firewall > Restricted Access > View trusted hosts：核对 omnivista/OMS/PC/网关都在表
5. 8770 Configuration 树：nmc 下建 Network=ale（号码 1）、子网 abc1（号=1）、节点 oxe（Subnetwork-Node number=101）
6. 节点 IP=192.168.1.3；FTP=adfexc；勾 Process configuration 与 Directory Process；告警=Permanent IP connectivity
7. Software download 页签填 mtcl 维护账号；Connectivity 页签勾 SSH 并填唯一 Host name
8. 右键 OXE > Synchronization > Complete > Separate：向导选 "of the task" > Status 页签 > Apply 启动 > Refresh 看日志
9. 验证：OXE 分支生成；Data Collection 页签显示最近同步时间

**SIP 模拟器对接**（p81-84，实验口径）：

1. SIP > SIP Ext Gateway 选 ITSP1_GW1：Registration ID=pbxN、Outgoing username=pbxN
2. Translator > 1 > External Numbering Plan > 1 > Default DID num. translator 右键 Create
3. First external number=33210N41000、First internal=31000、Range Size=500
4. 打出局呼叫确认公网 SIP 通路可用

## A2 — 未来触发

使用情境：把一台新 OXE 接进 8770；同步失败或数据取不回；空间冗余 OXE 怎么填 IP；信任主机报错；SIP 中继打不出外线；培训/POC 环境搭 ITSP1。

语言信号：OXE 纳管 / node registration / siteid / netadmin / 信任主机 / trusted hosts / Subnetwork-Node number / csa / csm / adfexc / mtcl。

补充信号：Complete Synchronization / NMCSyncLdapPbx / SIP Ext Gateway / DID translator / pbxN / ITSP1。

与相邻能力区分：节点接通后的计费出票与回收 → 票据管道能力；本卡只管"接得上、同步得了"。

## E — 可执行步骤

输入契约：OXE 侧维护账号、网络号/节点号、主 IP；8770 管理员账号。IP 不通或 SSH 未开 → 判停先修底层连通。

1. OXE 侧核查：siteid、netadmin -m（主地址/SSH/信任主机三项）。完成标准：三项均有记录且信任主机含 8770
2. 8770 建 Network 与 Subnetwork：子网号=OXE 网络号。完成标准：两级对象生成
3. 声明 OXE 节点：节点号=网络号×100+节点号、IP=csm 主址（冗余加第二条）、FTP 凭证、告警模式、维护账号、SSH Host name。完成标准：必填项全部落盘
4. 执行 Complete > Separate 同步并等成功提示。完成标准：OXE 分支出现且 Data Collection 显示时间
5. （实验环境）按 POD 配 SIP 网关与 DID 翻译并外呼验证。完成标准：出局呼叫接通

判停点：

- 同步成功但取不到票据 → 转票据管道能力（FTP 凭证与计费配置问题）
- 信任主机缺主机或 SSH 关闭 → 本卡范围，先按核查清单补齐再继续
- 实验密码/账号仅限 RLAB，生产环境一律用客户侧凭证，不引用书中明文口令

输出契约：节点声明参数清单（含节点号公式代入值）+ 同步验证记录 + （可选）SIP 中继验证结论。

## B — 边界

- 空间冗余 OXE 有两个主地址，声明时必须 Add a Value 全部填入，只填一个会在切换后断连（p72/p77）
- "所有与 Call Server 相关的主机都必须在信任主机表"（p74）——缺一台取不到数据
- 同步的 Partial 增量只覆盖五类条目，其余类型始终全量（p79）；组织更新任务也会触发缓冲落盘（p93）
- ITSP1 模拟器与全部明文密码为实验口径（RLAB 教学设施），生产对接真实运营商与客户凭证在书外
- 端口矩阵、安装细节在 8770 安装文档（书外）；本卡不覆盖
