# 决策规则速查 — OmniPCX Enterprise - Advanced (Participant's Guide, Edition 13)

| 能力 | 一句话规则 |
|---|---|
| SSH 免密分发体系 | N3 起 SSHv2 公钥认证强制；oxe-ssh-auth 管一对、oxe-nw-sshkey-sync 以五段 CSV 管全网，authorized_keys 条数核验 |
| CS 冗余部署与切换维护 | main+standby 实时 scp 复制；bascul 切换已建立通话保持；失联 120 分钟触发 440 只能 mastercopy；不停机升级 11 步轮换 |
| IP 域与 PCS 域级生存性 | 域按初始化 IP 落域且 CS/PCS 必须域 0；CAC 只闸跨域；PCS 许可锁 332+四状态+回切计时器，库单向同步最长激活 30 天 |
| 公私网双向溢出与重路由 | 断链/饱和时经 Node Access Prefix+DID 翻译走公网（话务台恒放行、SIP 扩展不适用）；反方向判别器挂 ARS 用 TG=-1 还原内号走专线 |
| Direct IP Link 全 IP 组网 | ABC-F2 全互联免中继；系统选项三态 Enabled 不可逆；接入 1 IP 信令+至多 24 接入×62 通道；两端带宽/加密/接入数一致否则 2879 |
| Audit 与 Broadcast 数据一致性 | Audit 两阶段对账（必须模拟+备份，链式对象跑两遍）；Broadcast 走 buffer→LOG→lupd.dat 序号闭环，默认 10 分钟、RLOG 静默失败 |
| 多线监督与经理助理组 | Multi-keys/Multi-MCDU 两形态；监督键五档铃型+四条硬上限；经理助理键对+过滤表 1000×16+screening/unscreening 互斥 |
| 寻线代接组与速拨编号体系 | 寻线三搜索+COS 随组+camp-on 溢出；组代接/直接代接自动成组；速拨 32500（默认 4000）直接/范围双形态、默认绕闭锁 |
| 办公桌共享（DSS/DSU） | DSS 真 MAC+DSU 虚拟 MAC（aa:bb:分机号）；登录即恢复配置；忙时重置默认 True（6004）、即时登录仅限特定机型族 |
| 多设备用户与 Twinset | 主站+至多 4 副站（DECT/REX 各 1）；建关联清空两机数据；Twinset Get Call 无感移机；主站退服三参数联动 |
| 实验/交付前置环境基线 | RLAB 双拓扑+ITSP1 号码规则（PN=POD 号）+启动顺序与组网 VM 网卡迁移前置，全部实验口径 |
| 维护命令与事件/许可速查 | 按功能域归类的命令地图 + 事件号对照（440/427/428/431/432/6004/6005/2879 等）+ 许可锁锚点（186/332/185 等） |

> 速查只给结论；需要原文依据、案例或反例时读对应能力卡。
