# DIGEST — OmniPCX Enterprise DECT 解决方案精华长文

> 源：DECTXTE200EN Edition 12（298 页，OXE R101.1 MD4）· 文档整理入库 · 2026-09-23
> 定位：10 分钟建立 OXE DECT 移动交付的全局认知；操作细节按需查 12 张能力卡。

## 一、这套东西是什么

DECT 是 ETSI 的数字增强无绳通信标准（1993 年起，110+ 国家采用）。在 OmniPCX Enterprise 上，它给员工提供"拿着手机在园区里走、通话不掉线"的移动话音，带漫游、切换、鉴权加密的完整蜂窝接入体系。

整本教材是一条交付主线，五步走：**懂底座、部基站（IP-xBS）、通同步、交付用户（注册手机）、补支线（混合模式/重注册/SIP-DECT）**。

三个数字先记住：

| 数字 | 含义 |
|---|---|
| 3 条产品线 | 8379 IBS（TDM 存量）/ 8378 IP-xBS（全 IP 主线）/ 8328 SIP-DECT（低成本小站），选型先于配置 |
| 254 / 2032 | 每 PARI 254 台 xBS；每 OXE 节点 8 个 PARI、共 2032 台（IBS 是全网 1 PARI/256 台） |
| -70 / -60 / -80 dBm | 话音门槛：容易场景 -70、金属环境 -60；基站间空中同步门槛 -80 |

## 二、标识号码体系：一切配置字段的语义来源

六个号码撑起整个体系：

| 号码 | 在谁身上 | 作用 |
|---|---|---|
| PARI（31 位） | OXE×每类硬件 | 系统标识；IBS 与 xBS 必须各一个 |
| RPN（2 个十六进制位） | 基站 | 系统分配的空中标识，定位与同步识别用 |
| RFPI | 基站广播 | =PARI+RPN |
| PARK（13 位） | 手机 | 注册时写入=PARI（11 位八进制）+PLI（2 位十进制），算例 3110000400100 |
| PLI（最大 31） | 手机 | PARI 比对位数旋钮：降位让相近 PARI 等效 |
| IPUI（14 位八进制） | 手机 EPROM | 出厂身份证，系统认机靠它 |

multi-PARI 的钥匙是 PLI：手机把收到的 PARI 与本地 PARK 做逻辑 AND，参与比较的位数=PLI。混合模式（IBS+xBS 双 PARI）必须降 PLI——原书 p227 全大写 WARNING；实验口径两 PARI 仅末位不同，取 PLI=30。

## 三、部署主线：IP-xBS 四步与同步生命线

1. **部署四步**：全局参数（Radio base type/PARI/PLI/AC/安全级别）、DHCP（vendor class alcatel.ipxbs.0 下发 IP/TFTP）、注册（全网只允许一个节点开 Registration enabled，基站按 MAC@ 入库自动分 RPN）、dectview xbs 核验两行 OK。
2. **换站保 RPN**：换故障基站必须手动注册（删旧 MAC@、录新 MAC@、保留位置名）；走自动注册会拿到"首个空闲 RPN"，依赖 RPN 的告警与地理定位全部失准。
3. **同步五件套**：内部同步树零配置自动建（RSSI+跳数、最深 24 级）；Sync Master 内部自动选举、外部同步时手工指定且禁止承载任何通话；Backup Sync Master 强制且必须看得见同一外部同步源；Sync Cluster 仅电梯井等特殊场景拆（每 Site/PARI 最多 8 簇）；>2 个 PARI 串联要加 Sync Highway。
4. **切换可行域**：handover 只发生在同 Site 且同一 Data Sync Primary 之下；跨 Site 只有 roaming。主备同步站皆失时全网停摆、恢复后不自动重建（原书自注 future release）——高可用站点要写进巡检预案。
5. **混合模式**：Mixed 下双 PARI + PLI=30 让全部用户跨类漫游；跨类切换靠外部同步链路 + Flag External Handoff，且验证时呼叫必须先建在 IBS。

## 四、用户与固件：交付的临门一脚

手机注册双通道，两条铁律（只能取一、两侧近乎同时）：

| 通道 | 系统侧 | 手机侧 |
|---|---|---|
| webadmin | Users / DECT set 点 DECT Register | 依次 PIN、AC 码、Normal、Yes |
| mtcl | dectinston <分机号>（响铃按 0，别挂断） | 同左，近乎同时操作 |

注册成功的三处证据：dectinston 输出 Installation succeed、webadmin 的 IPUI N/O 字段回填、手机屏显注册信息。注销用 dectrm（或 DECT Deregister）；换机不删用户，新手机直接重注册。

固件分两轨：

| 轨道 | 命令 | 机制与要点 |
|---|---|---|
| 基站 | downstat x | TFTP 后台下载到 RAM 不中断业务；空闲重启切新软件；最低 v73b0003；自动复位开关选 YES/NO |
| 手机 | downstat m | 空中 FWU：语音优先、下载暂停续传；回充电座才生效；理论 6-8 小时/机（排过夜窗口） |

PARI 变更迁移走自动重注册：相近 PARI 用 -update（业务不断）；彻底变化用 -forceUpdate，顺序铁律是**先推手机、后改系统 PARI**——反了手机就永远收不到了。-f 文件批量，2-3 秒/机，结果看 ReinstallSuccess/NOK 双清单；关机、出覆盖、漫游到访问节点的手机更新不了。

## 五、两条支线

- **8379 IBS（TDM 存量）**：1 条 UA 链路=3 个 B 信道，主链路接偶数端口；SYT 线 800m/LY278 线 1200m 上限；无加密（要加密一票否决上 IP-xBS）；handover 要求全部基站挂同一 media gateway。
- **8328 SIP-DECT（低成本）**：基站以 SIP 语义接入（PARI/PLI 体系不适用），注册四步为 OXE 建 SIP Extension、基站 WBM 声明、手机空中注册、基站代发 SIP register。双小区副站只配 DHCP 即自动拉主站配置，**主站=先声明 Extension 的那台**，链路约 5 分钟。三条硬边界要前置告知：仅欧洲频段、仅 8214 手机、电话本不集成 OXE；WAN 断则该站全断且无 SIP 备份。

## 六、交付红线与日常抓手

三条红线：

1. 教材全部密码/账号/AC/PARI 是实验值（如 AC=1111、Engineer00!），上生产必须换
2. 无线工程方法论（布点/天线/勘测判定）在书外 8AL90874USAA，教材只给门槛数字与工具开关
3. Debug 日志级别排障完必须回落；WBM 改动可被 PBX 下发覆盖，长期变更回 OXE 做

日常抓手速记：

| 抓手 | 用途 |
|---|---|
| dectview xbs/ibs/com | 状态总表，P/M/B/+ 标志判读同步与切换健康度 |
| xbssynchro | 拉同步树（RPN+RSSI） |
| incvisu \| grep xBS | 同步/注册事件（事件码 60/78） |
| syslog 四级 | off/Normal/System Analyze/Debug，端口 514，全站落同一文件 |
| tcdump / WBM PCAP | 抓包取证，深读转 8AL91443ENAA 排障指南 |

## 七、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 配 PARI/定 PLI/算 PARK | dect-pari-identifier |
| 选产品线/判拓扑 | dect-product-selection |
| 装 xBS/开注册/换基站 | dect-ipxbs-deployment |
| 配同步/外部切换/建 Site | dect-xbs-sync-topology |
| 建户/注册/注销手机 | dect-handset-registration |
| IBS 加 xBS 混合部署 | dect-mixed-mode |
| PARI 变更批量迁移 | dect-auto-reregistration |
| 基站/手机固件升级 | dect-firmware-management |
| 排障命令/日志/勘测/IBS/8328 | 路由入口（dect-solutions-router） |

## 版权

- 本精华长文为 ALE Training Services《DECT Solutions》（DECTXTE200EN Edition 12）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
