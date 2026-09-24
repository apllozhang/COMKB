# 企业广播 General Announcement（播报场景/TUI 录制/wav 部署）

## R — 原文依据

> "Only one general announcement can be recorded at a time. • Any new recording will overwrite the previous one. • Max duration: 5 minutes"（p223）
> "The name must be 'general_announcement.wav' • Format: CCITT A-law 8bits 8kHz mono"（p223）
> "3 choices are available (one of the 4 existing choices is not more used: on AA)."（p225）

出处：OTMCXTE200EN p210-227（c11、f22、p21、n18/n19/n20 归并）。

## I — 自述

general announcement 是在留言落箱与信箱查询前播放的公司级公告，四要素：

1. **播报场景三类（可多选）**：外呼留言落箱、内呼留言落箱、信箱查询进菜单前；由管理员在 TUI global configuration 勾选。第四项 "arrive on AA" 是 OT 服务器早期内嵌自动话务员时留下的功能，外置 VAA 方案下无效，不要勾
2. **录制两法**：wav 文件（音质最佳，适合品牌声音；改名 general_announcement.wav、格式 CCITT A-law 8bits 8kHz mono、传到指定目录即启用）或任意话机 TUI 录制（灵活，适合常换）
3. **用户权限**：勾 "User has right to manage the general announcement" 后，授权用户经 TUI 增强主菜单选项 6 进子菜单——1 试听 / 2 录制 / 3 停用；录制或上传后自动激活
4. **硬限制**：同时仅一条、新录覆盖旧录、最长 5 分钟、仅对支持 wav 文件的语言开放

wav 存放路径书中两处口径：p223 写 /var/data/general_announcement、p227 写 /var/data/ics-group/general_announcement（见 nr-04）——落地以现场系统实际目录为准。

## A1 — 书中案例

**广播部署实验**（c11）：

1. 定播报类型（仅管理员）：TUI global configuration 勾场景（实验任务配"信箱查询时播放"；勿选已废弃的 AA 项）
2. 授权用户：OT configuration 里选用户勾 "User has right to manage the general announcement"
3. TUI 录制验证：授权用户话机登录信箱，进增强主菜单选 6，子菜单 2 录制指定文案后自动激活；子菜单 1 试听、3 停用
4. wav 方式：取格式正确的 wav（CCITT A-law 8bits 8kHz mono），改名 general_announcement.wav 传入指定目录（路径按 nr-04 现场核实），文件就位即启用；停用为删文件或走 TUI
5. 复测：按所配场景呼叫/查询，公告先于问候语/信箱菜单播放

## A2 — 未来触发

使用情境：客户要品牌彩铃式公告；"换公告/临时下线公告"；"不同部门不同公告"的需求评估；wav 传上去没生效。

语言信号：general announcement / 企业广播 / 公告 / announcement / general_announcement.wav / TUI 菜单 / 录音 / 播报 / 落箱 / 查询前播放。

与相邻能力区分：用户个性化问候语（standard/personal/absence/alternative）→ otmsg-mailbox-profiles；信箱与 TUI 密码前置 → otmsg-user-mailbox-provisioning。

## E — 可执行步骤

输入契约：播报场景与文案经客户确认；wav 素材（录音棚口径）或现场话机录制。

1. 定场景与授权：管理员勾播报类型、给指定用户授权。完成标准：配置在册
2. 落地公告：TUI 录制或 wav 部署（格式/改名/目录三查）。完成标准：公告激活
3. 行为复测：按所配场景呼叫/查询核对播放时序。完成标准：先于问候/菜单播放
4. 交付说明：单条/覆盖/5 分钟限制书面告知。完成标准：期望管理到位

判停点：

- 客户要"多套公告按部门/季节轮换" → 硬限制是单条+覆盖，功能不覆盖该需求（n20），谈替代方案（多 profile 问候语/多站点，书中未展开）
- wav 传了没生效 → 依次核对格式（CCITT A-law 8bits 8kHz mono）、文件名、目录（两处口径现场 ls 核实，n18/nr-04）
- 勾了 arrive on AA 没效果 → 该项已废弃，外置 VAA 下无效（n19）

输出契约：生效的企业广播（场景/权限/素材口径记录）+ 变更与停用操作指引。

## B — 边界

- 专业录音制作（录音棚产线）在书外；"仅对支持 wav 文件的语言开放"限制（p223）
- VAA 缩写书中未展开；AA/VAA 的配置不属于本书范围
- 存放路径 p223 与 p227 不一致（nr-04），以现场实际目录为准，不按单一页码硬记
- 实验录制文案（"Welcome to OpenTouch training session"）为课堂口径
