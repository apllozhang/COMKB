# 诊断工具箱（日志、事件、镜像抓包、RMON、health、sFlow）

## R — 原文依据

> "Switch events can be logged to • Switch console • Local text file • Configurable default file size 1250 Kbytes • Multiple remote devices (syslog) 12 max"（p235）
> "the maximum port-mirroring sessions has been increased from 2 to 4. • There is a limit of 4 Mirror-to-port (MTP) indexes."（p249）
> "Captures first 64-bytes of frame • Session supported per switch or stack: 1 • Default file size: R8: 64 KB (max = 2 MB)"（p251）
> "<SWLOG TIMESTAMP> : <CMM>/<NI> : <MODULE_NAME> : <LOG_DESCRIPTION>"（p243）

出处：DT00XTE215EN p232-269。

## I — 自述

售后日常排障的八件套，按"取证目的"选工具：

1. **switch logging（swlog）**：输出到 console/flash/syslog（最多 12 台）；单文件默认 1250KB、/flash 下最多 8 个 swlog 文件、归档最多 40 个；默认级别 info（数值 6），按 appid/subapp 细粒度调级（如 ospf hello 单独 debug3）
2. **可读事件日志**：先 swlog appid all subapp all level event 过滤，再 show log events；输出四段格式=时间戳: CMM/NI: 模块: 描述，适合客户侧快读（License 到期、电源、VC 角色、STP 根、链路 up/down）
3. **命令日志**：command.log 存最近 100 条命令（命令/用户/时间/来源/结果），启用期间不可删除
4. **port mirroring**：复制流量到本机或远端口（远端口经 linkagg 8.9R3 起部分型号支持）；会话上限按新规格 4、MTP 索引 4 个（双向计 2）——与旧口径 2 并存，见 nr-01
5. **port monitoring（抓包）**：每交换机/堆叠 1 会话、只捕前 64 字节、默认 64KB（上限 2MB）、存 ENC 格式 pmonitor.enc；与镜像不能同端口
6. **RMON**：统计/历史/告警/事件四组探针供 NMS（OmniVista）取数
7. **health**：CMM CPU/内存的当前/1 分钟/1 小时/1 天均值与阈值
8. **sFlow**：Agent/Receiver/Sampler/Poller 四角色采样，用于拥塞、DoS、应用 mix、容量规划

## A1 — 书中案例

**诊断工具实验**（p261-269，How-To，实验宿主 6870-A）：

1. swlog 开关：show swlog（Running、console flash、info）> swlog disable > 变 Not Running > swlog enable
2. show log swlog 浏览原始日志（Ctrl+C 停止；支持 grep/timestamp 过滤）
3. 可读事件：swlog appid all subapp all level event 后 show log events，对比原始日志
4. 命令日志：command-log enable > 执行 vlan 4-5 与 no vlan 4-5 > show command-log 显示两条（用户/时间/来源）> disable
5. 端口镜像：port-mirroring 1 source port 1/1/1 destination port 1/1/10 并 enable，show 核对 bidirectional
6. 端口抓包：port-monitoring 1 source port 1/1/1 enable > 客户端 ping 造流量 > pause/resume 观察 Oper 状态
7. 取证文件：disable 后提示数据在 /flash/pmonitor.enc，show port-monitoring file 显示捕获帧
8. health：show health 与 show health slot 1/1 看 CPU/内存多粒度均值
9. RMON：show rmon probes/history/stats 核对探针与采集资源

## A2 — 未来触发

使用情境：定位某口异常流量；给客户出一份重大事件清单；审计谁改了配置；远端取包分析；CPU/内存趋势；组播/广播异常定位。

语言信号：诊断 / 排障 / swlog / show log events / 事件日志 / command-log / 端口镜像 / port-mirroring / 抓包 / port-monitoring / pmonitor.enc / RMON / health / sFlow / syslog / CPU 内存。

与相邻能力区分：

- 升级验证看 show microcode loaded（本卡 B 段口径），升级流程：升级与 Auto-Fabric 能力卡
- 接入排障里 UNP 状态查询：Access Guardian 能力卡
- OST 工具化的排障（PoE 向导/Auto-Ticket）：资产与装机工具能力卡

## E — 可执行步骤

输入契约：故障现象与端口范围、取证时段、是否需要完整报文、远端日志服务器（如有）。规格上限按型号查 Specification Guide。

1. 现象分流：看现状用 show 类命令；看历史用事件日志（show log events）与命令日志。完成标准：时间线成型
2. 调日志：按 appid/subapp 调级别（默认 info=6），需要远端留存配 syslog（最多 12 台）。完成标准：目标模块日志可见
3. 镜像取证：port-mirroring 会话把源口流量复制到分析口；同目的口多会话与双向都计入 MTP 索引。完成标准：分析口收到流量
4. 抓包定性：port-monitoring 单会话捕前 64 字节，pause/resume 控制，文件在 /flash/pmonitor.enc。完成标准：帧头部可读
5. 资源面：show health 看 CPU/内存趋势；RMON/sFlow 看端口统计与采样。完成标准：异常点定位
6. 收尾：关闭镜像/抓包会话，恢复日志级别，避免长期占用资源。完成标准：无残留会话

判停点：

- 需要完整报文（应用层） → 抓包只存前 64 字节，改用镜像+外部抓包器
- 镜像与抓包想同端口 → 互斥，二选一或换端口
- 镜像会话数规划 → 双口径（新规格 4/旧口径 2，nr-01）：以 show port-mirroring 实测与 Specification Guide 为准，老设备按 2 规划
- command.log 想清空 → 启用期间不可删，先 disable 再处理（删除会连带丢历史）
- 升级后验证版本 → 看 show microcode loaded，不要看 working（镜像进目录不等于已运行）

输出契约：可定位问题的证据链（时间线/镜像或抓包文件/资源数据）+ 工具现场已恢复原状。

## B — 边界

- 镜像会话数两处口径（p249 vs p265）按 nr-01 处置：取 4 为新口径、以实测与规格指南为准
- LLDP 类邻居发现也属诊断视野，但其配置与语音场景归 LLDP 与 PoE 能力卡
- 抓包文件 ENC（Network General Sniffer）格式，Wireshark 可识别；轮转或写满即停策略二选一（p251）
- sFlow Collector 为第三方软件（p258）；Agent IP 建议用 Loopback0（p360 口径）
- 实验 show 输出取自 8.7.98.R03/8.10.9.R04 截图（nr-08），参数随版本可能漂移
- 规格上限（镜像会话、抓包文件、syslog 台数在各型号的差值）查 Specification Guide
