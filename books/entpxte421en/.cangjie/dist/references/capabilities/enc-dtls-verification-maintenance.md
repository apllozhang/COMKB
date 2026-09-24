# DTLS 加密验证、排障与维护闭环（命令族、事件码、备份、抓包）

## R — 原文依据

> "'cryptview' command indicates if the OmniPCX Enterprise is secured."（p131）
> "5992 Minor 'FSNE:EGW – Remaining Validity Period of the CA Certificate. : P1' … If P1 is 0, the certificate becomes invalid and all end points with FSNE enabled reboot"（p132）
> "ALE strongly recommends to systematically backup certificates and keys whenever modifications are performed"（p107）
> "press the 'Play' button to check whether the communication is encrypted or not"（p138）

出处：ENTPXTE421EN p126-138, p107, p132-133, p290。

## I — 自述

交付验收与日常运维的两个闭环——命令验证与事件驱动：

1. **验证命令族**（mtcl 下执行，p129-131/p143/p192-193/p242）：

   | 命令 | 看什么 |
   |---|---|
   | ippstat <分机>（option 2/3） | 单机 DTLS=Yes、SRTP 套件能力；option 3 列全节点话机表 |
   | twin | 主备 CS 通信模式 Crypted/clear |
   | cryptview | System is DTLS secured、SSL level、DTLS server（内/外部 EGW）、受保护 coupler 表、mTLS 状态、网关/扩展计数 |
   | sipregister / csipsets | SIP 扩展 TLS 注册与 TLS/SRTP 列 |
   | sipextgw -g <n> | 外部网关 State/Transport/SRTP 模式 |
   | config ost / pcsview / hybvisu -f all | EEGW 状态表 / PCS 救援态 / ABC-F 链路 UP 与 Encryption |

2. **原生加密事件码**（incvisu/incinfo 查看，p132）：

   | 事件 | 级别 | 含义与动作 |
   |---|---|---|
   | 5991 | Minor | 系统无反应 → 查 OXE 与端点两侧 CTL 配置、看 netadmin 历史文件 |
   | 5992 | Minor | CA 证书剩余 P1 天 → P1=0 证书失效、全部 FSNE 端点重启，到期前必须换证 |
   | 5993 | Major | 主备 CS 连接是否加密 → P1=0 明文，修证书后重启 CS |
   | 5995 | Major | EGW 菜单与 netadmin 配置的 CS IP 不一致 → 核对两处后重启 CS |

   EST 注册类事件另族：5779（成功）/5780（失败）归 IPMG 自动续期（p84）。

3. **证书备份规则**（p107/p133）：

   - 每次证书变更后系统化备份：netadmin 11.9.1.5 导出（PKCS#12 或 PKCS#7），或 swinst 备 Linux Data 时自动随备份
   - 导出口令 ≥8 位、含大写+小写+数字+特殊字符各 1（单引号除外）；PCS 证书 11.9.2.4 导出打 tar
   - 警告：必须转存到存储介质——磁盘崩溃后靠它导入恢复

4. **Wireshark 抓包验证**（p134-138）：话机 COS 放开 PC 口、tnet 开镜像、Decode As 选 RTP、Stream Analysis 播放；加密=噪音，明文=语音

## A1 — 书中案例

**维护闭环**（p126-133，c02 步骤 10-11）：

1. 启动 IPDSP，PC 不认识 CA 时弹证书提示选 Accept permanently
2. 31000 与 31002 互打，通话窗口出现加密图标
3. spadmin（option 2）核对许可 424/4359 授权值（实验口径 75/30）
4. ippstat 31000 核对 DTLS 与 SRTP 套件；twin 核对 Communication Mode: Crypted
5. cryptview 核对 System is DTLS secured 与参数快照
6. incvisu 扫 5991/5992/5993/5995 四个事件
7. netadmin 11.9.1.5.1 导出证书备份并转存介质

**抓包验证**（p134-138，c03）：

1. 话机 COS 的 PC Port 置 Cascad. not filt.（IPDSP 直接跳过此段）
2. tnet d <分机>（默认口令 *tx8000#）→ mirror set lan 开镜像
3. PC 接话机 PC 口，Wireshark 抓包
4. Decode As 选 RTP；Telephony 菜单进 RTP 的 Stream Analysis 后点 Play
5. 播放为不可辨识噪音 = 媒体已加密

## A2 — 未来触发

使用情境：加密到底生效没有；话机没出加密图标；主备之间是不是明文；证书快到期怎么防；事件 5992/5993/5995 怎么处置；向客户证明媒体已加密。

语言信号：cryptview / ippstat / twin / incvisu / 事件 5991 / 5992 / 5993 / 5995 / 证书备份 / export certificates / Wireshark / mirror set lan / RTP Stream / 加密图标 / System is DTLS secured。

与相邻能力区分：参数配错类故障归开通能力的生效动作清单；SIP trunk 起不来查 sipalarm.log 归 SIP trunk 能力；端点信任库坏了要恢复出厂看本卡 B 段（p108）。

## E — 可执行步骤

输入契约：加密已配置（参数+lanpbx+重启完成）、可登录 mtcl。配置未完成 → 判停回开通能力。

1. 命令验证：按 I 段命令族逐项跑（ippstat/twin/cryptview 三件起步）。完成标准：cryptview 显示 System is DTLS secured
2. 行为验证：加密端点互打看加密图标；明文端点对照。完成标准：图标与命令结论一致
3. 抓包取证：按 c03 五步抓 RTP 流播放。完成标准：噪音=加密的录音/截图留档
4. 事件巡检：incvisu 扫四个 FSNE 事件；对 5992 建立 P1 天数台账。完成标准：无 Major 事件或已定位
5. 备份归档：证书变更后 11.9.1.5 导出并转存介质；随变更单记录口令保管位置。完成标准：备份可追溯
6. 到期运维：按 5992 的 P1 提前续期换证；换证后重生成 lanpbx + 重启 + 同步 twin。完成标准：续期闭环

判停点：

- 5992 的 P1=0 已发生 → 证书已失效、FSNE 端点会重启，立即换证并按变更窗口重启 CS，不要再排障
- 话机信任库损坏或站点搬移后连不上 → 恢复出厂（启动时按 i 再按 #，Reset to Defaults）回 TOFU 模式；注意同时清掉端上定制（p108）
- 抓包点不止话机 PC 口（trunk 侧/EEGW 侧）→ 原书未覆盖，声明边界后按客户监控方案另行设计

输出契约：验证结论（命令+图标+抓包三证）+ 事件台账 + 证书备份归档。

## B — 边界

- Wireshark 教学只覆盖话机 PC 口镜像一种位置；SIP TLS 解密（密钥日志）与 trunk/EEGW 侧抓包点在书外
- 事件 5992"全站重启"是产品行为不是配置错误——变更窗口规划必须把它算进去
- cryptview 的 IP/Encryption GW 菜单为只读展示；真正的 EGW 声明在 netadmin 20（n12）
- 集中监控/SIEM 集成不在原书范围
- *tx8000# 与许可值为实验口径/产品默认值，生产必须替换
