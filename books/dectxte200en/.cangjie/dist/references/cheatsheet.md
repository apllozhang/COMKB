# 决策规则速查 — DECT Solutions (Participant's Guide, Edition 12)

| 能力 | 一句话规则 |
|---|---|
| DECT 标识号码体系与 multi-PARI 适配 | PARI+RPN=RFPI、PARK=PLI+PARI、IPUI 认机；multi-PARI 靠降 PLI（30/29）做逻辑 AND 缩位匹配 |
| DECT 产品线选型与拓扑决策 | IBS/IP-xBS/SIP-DECT 三线按加密、规模、频段、切换诉求分流；六种拓扑按四格能力判定 |
| 8378 IP-xBS 部署与故障换站 | 全局参数 → DHCP（vendor class alcatel.ipxbs.0）→ 注册开关收编 → dectview 核验；换站手动注册保 RPN |
| xBS 空中同步体系与组网域（含外部同步与多站点） | 内部同步树 ≤24 级零配置；外部同步手工指定 Master（禁载）+Backup 强制；>2 PARI 走 Sync Highway；Site 是切换边界 |
| DECT 用户创建与手机注册/注销 | webadmin 与 dectinston/dectrm 双通道只能取一且两侧近乎同时；Set type 定 GAP/GAP+ 功能面；AC 比对决定注册成败 |
| 混合 DECT 基础设施部署（TDM + xBS、PLI 统一） | Mixed 模式双 PARI（IBS x0/xBS x4 形态）+ PLI 降位（30/29）+ 外部同步链路解锁跨类切换 |
| DECT 手机自动重注册（PARI/PLI 变更零接触迁移） | 相近 PARI 用 -update、彻底变化用 -forceUpdate（先推手机后改系统）；-f 批量、2-3s/机、NOK 清单闭环 |
| DECT 固件双轨升级管理（基站 downstat x / 手机 OTA downstat m） | 基站 TFTP 后台下载到 RAM 空闲重启（downstat x）；手机语音优先空中下载、回充电座生效（downstat m） |
| DECT 日常维护与排障（命令族/syslog/WBM） | dectview 标志判读（P/M/B/OK/NOK/OOS）+ xbssynchro/incvisu/tcdump 取证 + syslog 四级（Debug 禁常开） |
| DECT 无线覆盖勘测（RSSI 门槛/SSK/survey mode） | 话音门槛 -70dBm（容易）/-60dBm（金属）、站间同步 -80dBm；*7378423* 开 survey mode 画覆盖边界 |
| 8379 IBS 基础设施部署（UA 板卡/布线/建站） | 1 条 UA 链路=3 B 信道、主偶从奇端口、SYT 800m/LY278 1200m、全网 1 PARI/256 台、无加密、切换限同一网关 |
| 8328 SIP-DECT 部署（四步注册/双小区） | OXE 建 SIP Extension → 基站 WBM 声明 → 手机空中注册 → 基站代发 SIP register；双小区先声明 Extension 者为主站 |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
