# OTC Web 与访客入会（浏览器免装、WebRTC、匿名接入）

## R — 原文依据

> "Alcatel-Lucent OpenTouch™ Conversation for WEB • Available for everyone: OpenTouch Conversation users • OpenTouch Connection users • And also for guests (through intranet or internet)"（p323）
> "Purpose is to access to scheduled or reservationless conferences as anonymous"（p324）
> "No white board • No poll • No recording • No video • No contact list (buddy list) • No history • No scheduling interface"（p334）

出处：OPENXTE301EN p323-337（配 p338-362 数据会议 How-To 的入会环节）。

## I — 自述

OTC Web 是免安装浏览器端，核心价值是访客入会：

1. **适用面**：OT 用户与无账号访客（内网或互联网）；访客匿名入会，凭访问码定角色，可上传头像、填回呼号码、输领导者码
2. **能力**：IM/侧栏 IM、桌面共享（发布/观看，发布端可能需插件）、文档共享与批注、上传下载、静音控制、参与者管理
3. **架构**：外部数据面走反向代理（https 443/8016），音频走 PSTN 回呼或 WebRTC 经 OTSBC（SIPS/SRTP）；内部无需网关
4. **部署要求**：HTML5 浏览器（JS+Cookies 必开）；WebRTC 音频仅 Chrome/Firefox（Windows/Mac）；自 OT R2.1.1 起免插件入会（G.711 优先）
5. **功能边界**：无白板/投票/录制/视频/联系人列表/历史/排期界面（排期靠 OTC PC 或 Outlook 加载项）

## A1 — 书中案例

**访客入会路径**（p341-362 数据会议实验中的 OTC Web 环节）：

1. 领导者用 OTC PC 预约会议并发出邀请（邮件含 URL、桥号、访问码）
2. 访客点邀请 URL 打开 OTC Web 登录页
3. 填姓名、上传头像、填回呼号码
4. 有密码的会议输入领导者码或参与者码定角色
5. Join 入会：音频经回呼（PSTN）或 WebRTC（OTSBC）接入
6. 会中使用桌面共享观看、文档下载、IM 与静音控制

## A2 — 未来触发

使用情境：外部客户/访客不装客户端参会；浏览器入会要什么条件；为什么 OTC Web 里没有录制/视频；防火墙要开什么；访客怎么拿到音频。

语言信号：OTC Web / 访客 / guest / 匿名 / anonymous / 浏览器 / WebRTC / Chrome / Firefox / 免装 / 头像 / 回呼 / callback / 领导者码 / 访问码。

与相邻能力区分：会议预约与角色体系 → 协作会议能力；WebRTC 通道的端口与证书 → 远程接入能力。

## E — 可执行步骤

输入契约：会议邀请（URL/访问码/密码策略）、访客网络环境（内网/互联网）、浏览器形态。

1. 通道核对：数据面 RP 443/8016 可达；WebRTC 音频走 OTSBC 8061 或 PSTN 回呼。完成标准：访客侧可达
2. 入会引导：点 URL，填姓名/头像/回呼号，输码定角色后 Join。完成标准：入会成功
3. 预期管理：向访客说明边界（无视频/录制/白板等）。完成标准：无因预期差的"故障"报单

判停点：

- 访客要"视频参会"或"录制会议" → 能力边界（p334），走 OTC PC/移动端或另议
- 浏览器不是 Chrome/Firefox 要用 WebRTC 音频 → 不支持，改 PSTN 回呼入会
- 桌面共享发布要装插件 → 预期行为（免插件仅 R2.1.1+ 的部分能力），提前告知

输出契约：访客入会引导单（URL/码/音频路径）+ 边界说明（用于客户沟通）。

## B — 边界

- 2019 年口径：WebRTC 仅 Chrome/Firefox（Windows/Mac）——今天的浏览器矩阵按最新 release note 重核（nr-07）
- 排期只能在 OTC PC 或 Outlook 做，OTC Web 无排期界面（n29）
- 匿名访客的权限完全由所输入的码决定（领导者码/参与者码），码的发放管理归会议领导者
- 端口/域名为实验模板口径（ot-podX/otsbc-podX），生产按客户环境替换
