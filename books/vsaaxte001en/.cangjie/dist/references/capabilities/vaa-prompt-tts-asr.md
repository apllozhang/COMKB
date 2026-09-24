# VAA 提示音与 TTS/ASR 引擎（WAV 规范、Pico/Google 选型、语音一致性）

## R — 原文依据

> "Wav files uploaded to prompts should have the format: 8 KHz, PCM 16 bits mono. … No space in the name … It is recommended to use the same voice for all prompts: If TTS prompts are used, transcribe any WAV in TTS prompts for a harmony of the voices on the VAA"（p138）
> "The Pico TTS engine can be used free of charge and without an internet connection. But it is not recommended for production. - Google Cloud is recommended but NOT free (credit card required)"（p141）
> "Google speech to text service (Google Cloud account required) & API key required"（p37）
> "Define a name: TTS Pico - Choose the TTS engine: PICO - SAVE - Make a test ­ Language Pico English/French…etc ­ Click on Generate to create a WAV file"（p140）

出处：VSAAXTE001EN p33-37, p137-142。

## I — 自述

提示音是树的"声音来源"，四个知识块：

1. **提示音三来源**：WAV 导入（8KHz/PCM/16-bit/单声道硬约束，名称不能含空格，按语言分别导入）；电话录制（拨专属 "-Prompt Recording-" 树号或从 Prompts 页发起，需租户用户 ID+密码，Prompt ID 在 Prompts 菜单查）；TTS 生成（Prompts 页或树节点内直接生成）
2. **TTS 引擎选型**：内置 PicoTTS 免费离线、六语言（DE/GB/US/FR/ES/IT），官方明说"不建议用于生产"（音质口径）；Google Cloud TTS 生产推荐但收费（按字符计费、需信用卡、许可不经 ALE）；激活入口在租户设置 → Text to speech 页签（定义名称与类型后 Save，可测试生成）
3. **ASR（语音识别）**：外部云引擎（Google speech-to-text，需 Google Cloud 账号 + API key，在公司设置配置）；两种用法——菜单节点内 ASR 菜单选择（词句映射按键，Full match 全匹配开关，Quota 秒数控成本）与"菜单+直拨"档（先匹配菜单词句、再查目录姓名）；也有独立 Speech recognition 节点把结果存变量
4. **语音一致性约束**：同一 VAA 的提示音应统一声音——用 TTS 时把存量 WAV 全部转成 TTS 生成保持音色和谐；多语言树的语言选择前提示必须双语同文件（约束归树设计能力，本卡负责生成侧实现）

## A1 — 书中案例

**WAV 导入与 Pico 激活**（p137-142，实验口径）：

1. 从 NAS 共享取样例 WAV 文件到 PC（实验口径素材来源）
2. Prompts 页新建提示音，名称不含空格，选语言
3. 选 WAV 文件上传，格式必须 8KHz PCM 16-bit 单声道
4. 上传后在列表播放验证，可下载或录音替换
5. 点设置图标进入 Tenant/Settings → Text to speech 页签
6. 定义引擎：名称 TTS Pico、类型 PICO，点 SAVE
7. 测试生成：选语言、输文本、点 Generate 产出 WAV 试听
8. （对照）原书注：Pico 免费离线但不建议生产，Google Cloud 收费

## A2 — 未来触发

使用情境：客户给录音室级 WAV 上传失败或音质异常；选 TTS 引擎；开 ASR 菜单；统一全站音色；季节性提示音电话改录；多语言提示音制作。

语言信号：提示音 / prompt / WAV / 8KHz / PCM / 单声道 / TTS / Pico / Google Cloud / 文本转语音 / ASR / 语音识别 / 录音 / Prompt Recording / 音色 / 双语提示音。

与相邻能力区分：树节点引用提示音与双语同文件规则归树设计能力；G729 与 ASR 互斥的编解码决策归安装对接能力；ASR 节点参数细节归 IVR 选项节点能力。

## E — 可执行步骤

输入契约：提示音清单（文本/语言/用途）、客户录音素材格式、预算与网络条件（云引擎需外网与账号）、是否启用 ASR。

1. 格式治理：把客户素材统一转成 8KHz/PCM/16-bit/单声道，名称去空格。完成标准：全部素材满足硬约束
2. 导入：Prompts 页按语言分别导入并试听。完成标准：列表内可播放
3. 引擎激活：租户设置 → Text to speech 定义引擎（Pico 或 Google）并保存。完成标准：测试生成可用
4. 选型决策：实验/演示用 Pico；生产用 Google Cloud TTS（确认账号、计费与外网可达）。完成标准：选型与商务一致
5. 一致性处理：若混用 TTS，把存量 WAV 逐条转成 TTS 生成替换。完成标准：全站同一音色
6. ASR（如需）：公司设置配 Google API key；菜单节点开 ASR 档位并设 Quota。完成标准：识别测试通过
7. 电话录音通道（如需）：确认 "-Prompt Recording-" 树号与专用账号 ID+PIN。完成标准：远程改录走通

判停点：

- 客户要求内网/国产化 TTS 替代方案 → 停，原书未覆盖任何离线替代（仅 Pico 与 Google），如实声明边界
- ASR 需求与已勾 G729 冲突 → 停，转安装对接能力处理编解码契约，不在本卡硬调
- 云引擎报价 → 停，价格时效性原书自注可能过时，以厂商当期价格为准

输出契约：可用的提示音资产库（格式合规、命名规范）+ 已激活引擎配置 + ASR 可用性结论（含前提）。

## B — 边界

- WAV 三硬约束缺一不可：8KHz、PCM 16-bit、单声道；录音室高码率文件直接上传不可用（n19）
- Pico 不建议生产是原书明确口径（音质）；Google Cloud 收费且许可不经 ALE
- 云服务价格与能力信息原书自注可能过时（p141），细节以 Administration Guide 第 10 章与厂商文档为准
- ASR 仅 Google 一家，无离线/国产化替代方案讨论（n20）
- 树内 Announcement 的 Server file 模式（放服务器本地音频）原书标注 not recommended
- 录音凭证（租户用户 ID+PIN）要纳入账号生命周期管理，防离职失联（n38）
