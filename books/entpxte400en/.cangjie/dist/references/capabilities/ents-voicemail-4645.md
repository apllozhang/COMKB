# OmniMessage 4645 语音邮件与邮件通知

## R — 原文依据

> "Only one voice mail system (4645 or other) per OXE node"（p527）
> "Up to 7000 controlled by software license … Up to 30 accesses … 500 hours or 600 hours (if HDD>80 GB)"（p541-542）
> "E-mail notification None: no notification (default value) … Advanced: email notification with audio file attachment"（p564）

出处：ENTPXTE400EN p526-571。

## I — 自述

4645 是纯软件语音邮件，部署拓扑与通知链路两件事：

1. **四拓扑**：嵌 CS/GAS/OXE-V 同主机（30 端口）；独立专用服务器（CPU8 强制此形态）；独立 4645 服务主备双 CS；嵌主备之一（VM 不冗余——承载 CS 垮则 VM 垮）；一节点仅一套留言系统
2. **容量口径**：≤7000 信箱（许可）、≤30 接入端口、单留言 1 分钟-5 小时、每箱 5-100 条、总录音 500 小时（HDD>80GB 为 600）、8 语言、编号 3-8 位、分发列表 ≤50 成员
3. **编码**：仅 G711；非 G711 终端经本地板转码（每路耗 2 压缩器）；组网=ABC 集中留言+VPIM 互联；接入=TUI/可视留言/IMAP4
4. **库内声明**：WBM Applications/Voice Mail 建实例——留言箱 DN、类型 4645、接入数、CPU Name 用物理地址（勿用 Role 地址）
5. **邮箱分配**：用户 Voice mail 页签挂留言箱 DN 与 4645 CoS；首访=拨留言箱 DN，初始码 0000
6. **邮件通知三档**：None（默认）/Basic（通知）/Advanced（附 .wav 附件）；SMTP 经 netadmin 声明（Plain 25/StartTLS 587/TLS 465），防火墙加白，重启生效

## A1 — 书中案例

**4645 部署实验**（p547-556，How-To）：

1. spadmin 核对 4645 族许可锁（178/179/182/183/194）
2. WBM Applications/Voice Mail 建实例：DN=31499、类型 4645、接入 4
3. CPU Name 填物理地址 192.168.1.1（实验口径，勿用 Role 地址）
4. 用户 31000 挂 4645 CoS 与留言箱 DN
5. 31000 拨 31499 首访：初始码 0000 改新码、录姓名
6. 31001 呼入留言，31000 收通知进信箱收听
7. config 18 巡检：GD+4645 耦合器 IN SERVICE

**邮件通知实验**（p556-571，How-To）：

1. netadmin 主机表加邮件服务器，SMTP 声明 URL 与端口 25
2. 防火墙加邮件服务器为可信主机，应用后重启生效
3. Eva_tool 设 VM DDI 公开号码
4. 4645 CoS 通知档位从 None 切 Basic
5. 用户填 Mail 地址后留言，Thunderbird 收到通知邮件
6. CoS 切 Advanced 复测，邮件带 .wav 附件
7. Eva_tool 巡检信箱详情与通知档位

## A2 — 未来触发

使用情境：部署语音邮件；留了言没邮件通知；邮件附件疑问；换 SMTP 服务器；语音信箱容量规划；外线留言收不到；4645 迁移/独立部署。

语言信号：4645 / OmniMessage / 语音邮件 / voicemail / 留言箱 / 信箱 / VPIM / IMAP / 邮件通知 / email notification / SMTP / Advanced 附件 / Audio-Station / Eva_tool。

与相邻能力区分：等待音/保持音乐见呼叫处理能力；系统级语音指南见呼叫处理能力；许可锁核对见空库与许可能力。

## E — 可执行步骤

输入契约：部署形态（嵌 CS/独立/虚拟）、SMTP 服务器信息（客户提供）、留言箱编号规划、许可锁范围。SMTP 参数拿不到时通知功能只能停在 None 档。

1. 核许可：spadmin 看 178/179/182/183/194 锁值。完成标准：许可支撑目标信箱数
2. 建实例：WBM 声明留言箱 DN/类型/接入数，CPU Name 用物理地址。完成标准：config 显示 4645 耦合器 IN SERVICE
3. 分配邮箱：用户挂 4645 CoS 与留言箱 DN。完成标准：首访改密成功
4. 声明 SMTP：netadmin 主机表+SMTP 配置（协议/端口/from 地址），防火墙加白并重启。完成标准：ping FQDN 通、配置应用
5. 开通知：4645 CoS 按 None/Basic/Advanced 分档，用户填 Mail 地址。完成标准：留言后邮件到达（Advanced 含附件）
6. 巡检移交：Eva_tool 信箱清单、/var/log/maillog、配额告警参数。完成标准：通知链路台账完整

判停点：

- 留言正常但没邮件 → 按顺序查：用户 CoS 是否还是默认 None、SMTP 声明、防火墙白名单、from 域名被判垃圾（n34/n35）
- 邮件带不了附件 → Advanced 档才带 .wav；附件超大小上限时只发提示（p27 口径）
- 邮件服务器要求 STARTTLS/TLS → 端口与协议三态对应（25/587/465），选错连不上
- 客户要一节点两套留言系统 → 停，架构仅允许一套（n33）；评估换 4645 以外的方案走商务

输出契约：可留言可通知的 4645 实例 + SMTP/防火墙配置记录 + 信箱分配清单。

## B — 边界

- 实验值（留言箱 DN 31499、邮件服务器 10.20.30.200、Thunderbird 密码 alcatel）为实验口径
- 4645 安全加固（防盗打）按 SA0046 与 TC1774 执行（n41）；盗打风险提示见 p544-545
- 嵌主备拓扑中 VM 不冗余（承载 CS 垮则留言垮）；高可用诉求需评估独立双 CS 拓扑
- 基础语音指南只能用 Alcatel Audio-Station 录制，不能从话机录（n34）；A4645-V 免狗版为虚拟化形态
- VPIM 网络信箱 0/48000 与节点互联细节书内仅给口径，跨节点留言组网在组网课程展开
