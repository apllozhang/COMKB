# DIGEST — OmniPCX Enterprise 系统装载 精华长文

> 源：ENTPXTE402EN Edition 12（415 页）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 OXE 软件加载与云许可交付的全局认知；操作细节按需查 12 张能力卡。

## 一、这套东西是什么

OXE（OmniPCX Enterprise）是 ALE 的企业级呼叫服务器。整本教材解决一件事：**把 OXE 的软件装上去、把云连起来、把许可管起来**。主线工具是 S.O.T.（Software Orchestration Tool）——一台自带 DHCP/FTP 服务的虚机，加载工具与加载对象永远是两台机器。

三个数字先记住：

| 数字 | 含义 |
|---|---|
| 一次一个 | S.O.T. 同一时刻只允许一个部署任务 |
| 30 天 | RTR 资格期：OK 加 0.5 天、NOK 减 1 天，归零系统逐渐锁死 |
| 每 4 小时 | OXE 与云端 LMS 的许可对账周期；lms/oxe 计数不一致即 panic |

## 二、工具与加载主线

- **S.O.T. 四维定形**：交付形态（ISO 内含 OVA）× 运行模式（Standalone 加物理机 / Hosted 加虚机）× 配置（default / Template Factory 含降级模式）× 工作模式（Easy 向导 / Expert 独立管理）。首连强制改密+口令短语；更新仅限同主版本 zip+MD5。
- **单版本全加载**：网络引导（BOOTP/DHCP）取 startup.txt，经 TFTP 下载 Linux RAM，再 FTP 自动安装。空盘才自动装；已装盘必须 grubboot ETHER 或 BIOS 强制。"completed" 只是软件就位——角色寻址、许可、密码、国家码是独立后置清单。
- **双分区安全模型**：同一块盘装两个版本，不停话音装好、切换才重启、可回退。同基础版本走复制+补丁；跨 Linux 版本走完整加载+数据复制。
- **补丁顺序律**：静态补丁停话音（active 分区装会自动重启）或装 inactive；动态补丁可热装但必须在同版本静态之后；补丁累积包含此前全部修正——装最新即得全部。动态补丁装完要 downstat d/i/t 跟完终端下载。
- **无 SOT 替代路径**：客户现场不让架 SOT 时，OXE 自当分发器——媒体传 /tmpd，swinst 9-10 解包安装；全版本/静态补丁强制 inactive；Rload 解包物要手动 9-7 清理，/tmpd 源文件反而自动删。

版本命名三套互相咬合：

| 命名对象 | 例子 | 读法 |
|---|---|---|
| 软件发布名 | N420536a | N=产品线、4=线内选项（R101.1）、205=软件版本、36=静态补丁号、a=动态补丁 |
| SOT 媒体名 | A.B.XXX.000（ISO）/ A.B.XXX.YYY（zip） | XXX 为所基于 ISO 序号，YYY 为 zip 序号 |
| siteid 全串 | R101.1-n4.205-36-a-fr-c83 | 业务标识-交付-静态补丁-动态补丁-国家-CPU 类型 |

## 三、两种现代承载形态

虚拟化（OXE-V）与一体机（GAS）的平台与许可路径：

| 形态 | 平台 | 许可路径 |
|---|---|---|
| OXE-V | VMware ESXi 8.0/7.0 | FlexLM+加密狗 或 Cloud Connect |
| OXE-V | KVM（内核 ≥4.12.14 且 KVM ≥5.2） | FlexLM+加密狗 或 Cloud Connect |
| OXE-V | Hyper-V 2022/2019/2016、Nutanix AHV、AWS | 仅 Cloud Connect（无 USB 重定向、无 FlexLM 虚机） |
| GAS | BP 自备硬件，Rocky+KVM 打包 | 服务器 ALU-ID 本地 FlexLM 或 Cloud Connect ID |

关键容量数字：

| 数字 | 含义 |
|---|---|
| 500/3000/7000/15000 | OXE VM 规格模板四档（按用户数） |
| 120 通道 / 240 台 | 每 OMS 的 VoIP 通道数 / 每 OXE 最多 OMS 台数（Lock 385/384） |
| 50 并发 / 7000 用户 | GAS 内嵌 WebRTC 网关上限 / 超过必须外部网关 |
| 4 核 2.8GHz 8GB 360GB | GAS 满配（OXE+OMS+WebRTC）最低前置；只认硬件 RAID |

GAS 后安装向导六段：国家码、OXE 参数（含信任主机 CSV）、冗余形态、可选组件、WebRTC GW 参数（RAINBOW_PBXID 必须用 Rainbow 云正式值）、许可（FlexLM .ice 加 OXE swk）。改 FlexLM 配置后 OXE 必须重启。

## 四、云连接：FTR 与 RTR

- **零改动入云**：OXE 出站主动连 connect2.opentouch.com——443 常驻 XMPP/WSS + 80 按需 SOCKS5 + 53 DNS；TLS 1.2；KeepAlive 默认 90 秒（防火墙掐空闲会话就调它）。
- **连通性验证**：checkCloudConfig.sh 依次测 DNS 解析、443 证书链、SOCKS5 80——后两项打印 "Success !!" 为过关。
- **FTR 门禁**：swk 许可含 CCSID + 电话应用已启动 + 连通全绿。新装机自动注册（每 4 小时重试、失败发 6214）；备机严禁做 FTR（凭证靠克隆同步）；PCS 不跑云服务。
- **panic 唯一出路**：RTR 归零或 Duplicated 时，向 helpdesk 申请 6 位 PIN（5 天有效、不落盘），CCTool 在线重置全部云配置并重注册。
- **Duplicated 陷阱**：克隆虚机会把 CC 身份一起复制，两台同 ID 系统同时扣资格期；PIN 生成会移除两侧记录，只有用 PIN 的系统活下来。

RTR 状态判读：

| Fleet Dashboard 状态 | 判据 | 动作 |
|---|---|---|
| Connected | 24h 内有连接或剩 29-28 天 | 正常 |
| Qualifying | 超 24h 无连接且 27-10 天 | 27、20 天各一封邮件 |
| Soon Blocked | 剩 9-1 天 | 每日邮件，立即修网络 |
| Blocked-Panic | 剩 0 天 | PIN 恢复 |
| Duplicated | 同 ID 双系统 | 两侧同扣，立即 PIN |

## 五、OPEX / Purple on Demand：许可从文件变成云池

- **开通三件套**：swk 含 CCSID、lock 431=1、装完重启 OXE；spadmin 核 OPEX Flag=1。lock 431 打开后旧 CAPEX 锁全部失效（仅 87/165 版本锁例外）。
- **三种消耗类型**：

| 消耗类型 | 触发点 | 适用订阅 |
|---|---|---|
| Unitary | 创建即耗，无余量拒建 | Softphone、API Telephony、VNA、VNA Broadcast |
| On activation | 激活才耗、停用腾挪 | 仅 Voice Enterprise 与 Room |
| By threshold | 加阈值才要许可 | 4059 话务台（0-1000）、ACD（0-2800）、DR-Link（0-15000）、VAA、OPR |

- **对账判据**：spadmin 11 四列读法——中间 lms/oxe 两列必须一致，不一致即 panic；每 4 小时自动对账，LMS 失联发 654、连续 30 天进 panic。
- **panic 时间线**：超订 15 天后随机停用空闲用户、45 天后全停；LMS 失联超 30 天则 15 天后就执行最狠档。Softphone 超订始终不自动处置。
- **许可映射先对再建**：软话机双份（Voice Enterprise+Softphone）；DSU/DSS 办公共享两份；客房按客人管理双份 Room；tandem 副机不占许可。
- **C2P 转换**：五步流程下单即定局；C2P 件号 3EYxxxxxMA（PoD 为 3EYxxxxxAA）；排除 OPR、ALE Connect、Selfcare、VNA、API Management。
- **下载入口**：MyPortal 的 Asset & service manager——项目状态必须 Active，Pending 是商务侧未激活，别反复重试下载。

## 六、交付红线与速查卡

四条红线：

1. 教材全部密码/账号/网段是实验值（Superuser2580* 一类），上生产必须换；aging=0 触发 CIS 基线警告
2. "completed" 不等于交付完成——角色寻址、许可恢复、业务配置（用户/路由）是独立后置清单，业务配置指向 Starter 课程
3. FlexLM 与 RTR 二选一要在设计阶段定死；改 RTR/FlexLM 参数都要重启
4. 版本演进以书外权威文档为准：TBE043（虚拟化）、TC3138（GAS 安装）、TC3104en-Ed08（N3 迁移）、TC2456（SOT 兼容）

速查卡：

| 要做的事 | 去哪张能力卡 |
|---|---|
| 装/更新 SOT、建虚机模板 | entload-sot-installation |
| 全新装 OXE、加载后初始化 | entload-cs-loading |
| 升级、打补丁、切分区、回退 | entload-patch-management |
| 选虚拟化平台、装 OXE/OMS 虚机 | entload-oxe-v-deployment |
| 装 GAS、后安装向导、FlexLM | entload-gas-delivery |
| 连云、FTR、PIN 恢复 | entload-cloud-connect |
| RTR 状态、资格期、Duplicated | entload-rtr-licensing |
| OPEX 开通、LMS 对账、C2P | entload-pod-licensing |
| 分发器模式/SOT 传媒体/GAS 运维/云端机队服务 | 路由入口（oxe-loading-router） |

## 版权

- 本精华长文为 ALE Training Services《OmniPCX Enterprise — 系统装载》（ENTPXTE402EN Edition 12）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
