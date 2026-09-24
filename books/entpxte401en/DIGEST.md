# DIGEST — OmniPCX Enterprise Advanced 精华长文

> 源：ENTPXTE401EN Edition 13（543 页，R101.1 MD4）· 文档整理入库 · 2026-09-24
> 定位：10 分钟建立 OXE 企业级运维（冗余/生存性/组网/一致性）的全局认知；操作细节按需查 12 张能力卡。

## 一、这套教材是什么

《OmniPCX Enterprise - Advanced》是 ALE 官方售后培训讲义（概念与实验约各半），承接 Starter 教材，把单机 OXE 升级为"冗余、分域、可生存、可组网、数据一致"的企业电话网络，并配齐速拨、多线监督、经理助理、寻线代接、办公桌共享、多设备这组客户高频话机级业务。

三个分层先记住：

| 分层 | 手段 | 一句话 |
|---|---|---|
| 中心层 | CS 冗余（main+standby） | 呼叫控制不断，已建立通话跨切换存活 |
| 边缘层 | IP 域 + PCS | 远程站点断链时自治，PCS 是临时生存手段（30 天上限） |
| 退路层 | 公私网双向溢出 | IP 不通走电话网；反方向公网拨叫折回专线省费 |

一条地基贯穿全部：N3 起 SSHv2 公钥免密强制——mastercopy、pcscopy、audit、broadcast 全依赖它。

## 二、主线：从单机到企业级

1. **SSH 免密地基**：oxe-ssh-auth 管"一对"，oxe-nw-sshkey-sync 用五段 CSV 管全网；核验口诀是数 authorized_keys 条数（两机 6 条、三机 9 条）。
2. **CS 冗余**：同版本同类平台两条铁律；备库实时 scp 复制；失联窗口默认 120 分钟（0-120 可配），超时触发 440 事件只能 mastercopy 整库克隆；双主（double main）时连参考 MG 的一侧是真主；不停机升级 11 步两机轮换。
3. **IP 域与 CAC**：设备初始化时按 IP 落域，CS/PCS 必须域 0；CAC 只闸跨域通话数（-1 不限）；编解码按域带宽档从选择链取交集，跨域取低档，OPUS/G722 的媒体服务要 OMS。
4. **PCS 域级生存性**：许可锁 332>0、版本≥CS、RAM≥CS；四状态 INACTIVE/ACTIVE/INACTIVE*/UNDEF；回切计时器默认 30 秒、可定点、0=人工；库单向同步、PCS 上改的下次更新即丢；不提供 TFTP/DHCP/ABC-F、救不了 4645 与 SIP 传真/语音邮箱。
5. **双向溢出**：私到公覆盖 CAC 饱和/压缩机枯竭/断链三类触发，双层权利（COS 双开关+被叫外号闭锁），话务台恒放行、SIP 扩展不适用；thin sector 用段首外号兜非 DID 用户；公到私用判别器挂 ARS 表，TG=-1 的还原路由每表仅一条且必须首位。
6. **Direct IP Link 组网**：ABC-F2 全互联免中继免许可；系统选项 Disabled→Migrating（必须重启）→Enabled 不可逆（回退只能库恢复）；接入 1 必须 IP 信令、两端带宽/加密/接入数一致否则 2879 拒建；无中继语义，节点 IP 故障即孤立。
7. **数据一致双工具**：Audit 两阶段对账（specific 全网收集、shared 取参考节点、直改表——必须先模拟并强烈建议备份全网库；链式对象跑两遍）；Broadcast 持续增量（buffer 默认 10 分钟落 LOG、lupd.dat 序号互比、远端写失败产 RLOG 静默等待人工）。
8. **话机级业务**： multiline 是监督类特性的公共地基；经理/助理靠键对+过滤表（1000 张×16 参数）+screening/unscreening 互斥；办公桌共享 DSS/DSU（虚拟 MAC aa:bb:分机号）；多设备主站+至多 4 副站（建关联清空两机数据）。

## 三、关键数字表（标称口径，引用必须带前提）

| 维度 | 数值 | 出处 |
|---|---|---|
| 集中式/组网分机 | 15000 / 100000 | p43, p44 |
| IP 域 | 1000 个/系统 | p152 |
| PCS | 240 台/系统；一 PCS 至多救 1000 域 | p168-169 |
| 直链 | 100 节点；1488 并发/链（24×62）；约 10000 呼/时/链（8 接入） | p395 |
| 广播 | 128 域（-1..127）；LOG 上限 127；buffer 默认 10 分钟 | p481, p483, p490, p474 |
| 速拨 | 32500 总表（默认 4000）；400 范围；每实体 32 区 | p236-238, p244, p247 |
| 监督 | 20 监督者/话机；100（网络 20）/邮箱；15000 键/系统 | p265 |
| 冗余 | 失联窗口 120 分钟（0-120）；PCS 激活上限 30 天 | p79, p182 |
| DID 翻译 | 每前缀 2000 条 | p224 |
| 过滤表 | 1000 张×16 参数 | p278 |

事件号速记：440=失联超时须 mastercopy；427/428=PCS/CS 侧断链；431/432=PCS 剩余时间/违约态；6004=忙时 DSU 被顶；6005=节点级呼叫上限；2879=直链两端不一致拒建。

## 四、交付红线

1. 教材全部密码/账号/网段/号码是实验值（RLAB），上生产必须换；实验防火墙只是"部分配置"的教学口径。
2. 容量数字全是标称上限，没有话务模型——售前承诺前先补 Erlang 测算。
3. Starter 前置四件：装机、barring、ARS 基础、GD/OMS 的 SSH 方法——书中多处明示 REFER TO STARTER TRAINING。
4. 前缀勘误：代接 55/56、进出组 480/481 在 Note 与截图间互换——现场以 Prefix Plan 实查为准，不背书。
5. Direct IP Link Enabled 不可逆：变更单里必须写明回退=恢复数据库备份。

## 五、速查卡

| 要做的事 | 去哪张能力卡 |
|---|---|
| 配免密/协同功能认证失败 | entadv-ssh-trust-foundation |
| 建冗余/切换/升级/双主 | entadv-cs-redundancy |
| 建域/CAC/装 PCS/断链演练 | entadv-ip-domain-pcs |
| 溢出/重路由/thin sector | entadv-overflow-rerouting |
| 直链组网/2879/加删节点 | entadv-direct-ip-link |
| 全网对账/广播巡检/RLOG | entadv-audit-broadcast |
| 多线/监督键/经理助理 | entadv-multiline-supervision |
| 寻线/代接/速拨 | entadv-hunting-pickup-speeddial |
| 办公桌共享/多设备/实验环境/命令速查 | 路由入口（oxe-advanced-router） |

## 版权

- 本精华长文为 ALE Training Services《OmniPCX Enterprise - Advanced》（ENTPXTE401EN Edition 13）的内部学习整理，仅供内部学习使用；教材版权归 ALE Training Services 所有。
