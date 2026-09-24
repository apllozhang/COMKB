# 消息与彩铃（MSG1-20 / Music on Hold / .wav 格式）

## R — 原文依据

> "According to the Software keys, the system can have 4 to 20 audio messages … The total length of the messages is 320 seconds"（p244）
> "Files .wav must be in 16-bit PCM 8 Khz Mono or CCITT A-law or μ-law 8-bit 8Khz Mono format"（p247）
> "Default value: Entity1 (possible values entity 1 to entity 4 used in case of multi company)"（p248）

出处：OXOCXTE300EN p243-251（消息用途讲义、MoH 讲义与下载实验）。

## I — 自述

站点级音频资源两池：

- **MSG1-20 消息池**：默认 4 条、许可至 20 条，总长 320 秒动态分配；五种用途——Welcome（属话务员组）、Pre-announcement（振铃前/中）、Remote substitution、External forwarding、DISA；录制走 MMC 话务员会话或 OMC 下载
- **Music on Hold**：仅外线保持时播放（内线保持是哔哔音，产品行为 n41）；三种源——默认乐/Tape 音频输入/录制 .wav；按 Entity 1-4 分别配置（多公司场景）
- **格式硬约束**：.wav 必须是 16-bit PCM 8kHz Mono 或 CCITT A-law/μ-law 8-bit 8kHz Mono；无文件时用话务员会话现场录（Menu Operator/Expert/Voice/Hold music 或 Message xx）

## A1 — 书中案例

**下载实验**（p246-251）：

1. 备好 .wav（格式不合规先转码，或改用 MMC 会话录制）
2. MoH：OMC/System Miscellaneous/Music on Hold → 选 Entity1（默认）；Music source 选 Recorded Music，点 Load from and transfer 传文件
3. 反向取回用 Transfer and save as
4. 预公告：OMC/Subscribers Misc/Preannouncement Messages → 选 MSG1-20 → Load from and transfer
5. 验收：外线保持播定制音乐、内线保持仍为哔哔音

## A2 — 未来触发

使用情境：客户要自定义等待音乐；多公司各配各的彩铃；"内线保持怎么没音乐"质疑；消息下了不生效排查。

语言信号：欢迎消息 / MSG / 彩铃 / 保持音乐 / Music on hold / MoH / .wav / 8kHz / Entity / 预公告消息。

与相邻能力区分：消息在呼入流程中的挂接（哪个时段播哪条）→ 呼入分发与闭锁卡。本能力到"音频资源上传可用"为止。

## E — 可执行步骤

输入契约：客户提供的音频文件与用途分配、（多公司）Entity 归属。文件格式不合规 → 判停先转码，不要直接上传试错。

1. 核许可：确认消息条数配额（默认 4、许可 20）。完成标准：设计条数在配额内
2. 备料：.wav 转为两种合规格式之一。完成标准：格式核验通过
3. 上传 MoH：选 Entity → Recorded Music → Load from and transfer。完成标准：外线保持可闻
4. 上传 MSG：选消息号 → Load from and transfer。完成标准：消息列表更新
5. （备选）MMC 会话录制：Menu Operator/Expert/Voice 下录 Music xx/Message xx。完成标准：同上

判停点：

- 客户要超过 20 条或超 320 秒 → 超出系统口径，如实告知并给替代方案
- "内线保持没音乐" → 产品行为（哔哔音），不是配置故障（n41）
- 消息号被其它用途占用 → 先梳理 MSG1-20 分配表再改

输出契约：MSG/MoH 分配表（消息号-用途-文件-Entity）。

## B — 边界

- 消息数与软件钥匙挂钩，报价前先核许可（n16）
- 音频版权与录音合规在书外
- Entity 2-4 为多公司场景预留，单公司固定 Entity1
- DISA/Remote substitution 等用途的完整行为口径在 Expert 文档
