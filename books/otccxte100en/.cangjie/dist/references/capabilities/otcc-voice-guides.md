# 语音指南三路径（话机录音/.wav 导入/座席欢迎指南）

## R — 原文依据

> "The ideal way to manage the whole messages is to create a voice guide in 3 digits and their associated messages in 4 digits. The first digit is for the language index"（p214）
> "Dial the prefix 401 to start recording process … Enter the voice message (i.e. 1683, 1684 or 1685)"（p219）
> "The .wav files available on OTCC_NAS instance have got the following attributes: A-Law, 8000Hz, 64 Kbps, mono"（p241）
> "SFTP Enable the SFTP connection (mandatory from OXE N3)"（p245）
> "The voice guide #538 puts into service the agent welcome guide feature … Agent can record a maximum of 5 prompts."（p574-575）

出处：OTCCXTE100EN p194-264, p566-582。

## I — 自述

编号法是地基：指南号（3 位）放 CCD 矩阵，消息号（4 位=语言索引+指南号）供录制——指南 683 配消息 1683（语言 1）/2683（语言 2）；每指南消息数=语言数、最多 40 条，消息号全域 0-5999（p214/p586/p13）。

静态指南打包后固化在 Flash、不可改；动态指南可录音、存 RAM，需 GD3/GA3 板卡或 OMS（免板卡）；格式 G711 64kbps（crystal）或 ADPCM32 32kbps（common）（p196-197）。

录入三路径：

- 话机录音：401 开始录、输消息号、录制、文件名+memo、选文件装板；580 试听；COS 须启用 Recordable Voice Guides（法语库默认关，n26）；无录音时播备份音 56（p218-220）
- .wav 导入：CCS Audio File Conversion 转码+定消息号 → Audio File Update 经 SFTP 传输（OXE N3 起强制）→ Dynamic Voice Messages Configuration 选中装板（p241-245）
- 座席欢迎指南：机制指南 538 预置（法国库不建不改）；消息池 4500-5999（每座席最多 5 条文件）；三处激活（话机 Apply / CCS 勾 Presentation Message Activation / OXE 侧启用）；Silent Connection on Agent=0 时主叫、座席都听；=1 仅主叫（p574-576）

板位与验证：实验 OMS 板位 4-0；mtcl 会话 vgstat 4 0 查装载（^ 标记已选中）（p215-220）。

## A1 — 书中案例

**话机录音排矩阵**（p211-236）：

1. OXE 建 683/684/685 三指南（Single-message、Start=YES、备份音 56、消息 1683/2683 等）
2. Dynamic Voice Guides> Assignment 把消息分配到板位 4-0
3. COS 放行 Recordable Voice Guides；IPDSP 拨 401 逐条录制并选文件装板
4. 580 试听三条消息；vgstat 4 0 复核装载
5. After-Sales pilot 排矩阵：Pres.Guide=683（1 次）、Level[1] 音乐 5 秒、Level[2]=684、Level[6] 循环
6. 阻塞态两种配法（按规则用 Voice_guide_PG 播 685；不按规则用 Blockage closure addresses 播 685 两次）

**.wav 导入**（p237-264）：拷 688/690 素材，Conversion 转码定消息号，SFTP Update 传输，Select 装板，Offer pilot 排矩阵。

**欢迎指南**（p572-582）：分配 4500，座席设 Pres. Message Number=4500 与文件数 2，CC 页签录晨/晚两版，Download 选版本，三处任一激活。

## A2 — 未来触发

使用情境：外包录音上线；"401 录不了音"；换班次问候语；多语言消息该录哪个槽；.wav 传输失败；580 试听没声；来话还是备份音；欢迎指南要不要让座席听见。

语言信号：voice guide / 语音指南 / 消息号 / 401 / 580 / vgstat / Audio File Conversion / Audio File Update / SFTP / A-Law / 8000Hz / ADPCM32 / G711 / 板位 / 4-0 / 538 / 4500 / welcome guide / 欢迎指南 / 备份音 56。

与相邻能力区分：指南排进哪个 parking level → 路由与分配规则能力；EWT 表与 518 位次 → 排队体验卡（路由卡）；多语言 pilot 双语路由归多语言与日历能力。

## E — 可执行步骤

输入契约：文案与语言清单已定、目标库语言编号表已核对（nr-07）、录音源（话机或 .wav）就绪。

1. 建指南并分配板卡：OXE 建 3 位指南号（Function 按单消息/多语言选）、消息号=语言索引+指南号，Assignment 分配到板位。完成标准：config 4 在服、分配条目存在
2. 路径一话机录音：COS 放行 Recordable Voice Guides，401 录制，填文件名+memo，选文件装板。完成标准：580 试听通过、vgstat 可见 ^ 选中
3. 路径二 .wav 导入：核对素材属性 A-Law/8000Hz/64kbps/mono，Conversion 转码，SFTP 传输（N3+强制），Select 装板。完成标准：三步均成功提示、vgstat 复核
4. 排入矩阵：pilot 规则 Pres.Guide 与 parking level 按听感脚本填（次数/时长）。完成标准：开态/阻塞态听感与设计一致
5. 欢迎指南（按需）：分配 4500 段消息，座席设消息号与文件数，录多版本后选中激活。完成标准：来话摘机先闻欢迎语
6. 验证与回退：无录音场景确认播备份音 56 而非静默。完成标准：全场景听感验收单通过

判停点：

- 401 拨不出/录音流程走不通 → 查 COS 的 Recordable Voice Guides（法语库默认关，n26）
- 传输失败 → OXE N3+ 必须勾 SFTP 且 OXE 侧已实现 SSH（n08）
- 播错语言 → 语言槽与语种取决于库配置，先核语言编号表再录（nr-07）
- direct call 来话没有欢迎语 → 设计如此：欢迎指南不在 CCD direct calls 上播放（n31）
- 想自建 518/538 同号指南 → 系统预置不可建改，只录消息（n27）

输出契约：全链路上线的语音指南集（编号/录制/装板/矩阵落位）+ 听感验收记录 + vgstat 截图口径。

## B — 边界

- 每指南最多 40 条消息（=语言数上限 40）；消息号 0-5999；欢迎消息池 4500-5999 共 1500 条、每座席 5 条（p586/p568/n28）
- OXE 预置资源（518/538/3226-4217/备份音 56/演示指南 70/直连阻塞 75）不可自造同号（n27/g43）
- Audio Station/VGTransfer 工具链书中点名未展开，录音第四法在 OTCC901（n41）
- 板卡/编码口径为实验 OMS 板位 4-0；crystal/common 硬件对应不同编码（p197）
- 实验编号（683/684/685/688/690/701/640 等）为实验口径；多语言 pilot 部署归多语言与日历卡
