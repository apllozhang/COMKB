# 盲判结果 · dt00xte215en

判定依据：仅 blind-input.json 中的 capability_catalog（13 项能力）。逐条凭第一判断锁定，未参考答案。

```
should-aaa-01 | swl2-aaa-hardening | 开通 SSH 并限源 10.20.0.0/24 正对应管理面收缩清单中的 ASA 限源与 SSH 强加密
should-aaa-02 | swl2-aaa-hardening | 8.10R04 强制首登改密正是 AAA 能力里账号密码治理的要点
should-olc-01 | swl2-lightning-config | 出箱新交换机最快开局即 Lightning Config 笔记本接端口 1 流程
should-olc-02 | swl2-lightning-config | admin 密码 ≥8 位四类字符且避开 ! 与 $ 是 Lightning Config 的明确规则
should-cfg-01 | swl2-config-lifecycle | 未保存配置断电会丢、如何保住属保存/固化生命周期问题
should-cfg-02 | swl2-config-lifecycle | write memory 与 flash-synchro 差异正是配置生命周期能力的核心命令语义
should-vc-01 | swl2-virtual-chassis | 两台合成一台管理、VFL 端口与主备选举是堆叠能力本体
should-vc-02 | swl2-virtual-chassis | 堆叠分裂后双活重复 IP 的防护即 RCD/VCSP 分裂防护内容
should-vlan-01 | swl2-vlan-routing | VLAN 网关接口 DOWN 的典型原因是 VLAN 无成员则接口 DOWN
should-vlan-02 | swl2-vlan-routing | 单线跑多 VLAN 是 802.1Q 干道与默认 VLAN 的 VLAN 三入口知识
should-link-01 | swl2-link-redundancy | 双 10G 绑聚合与流量分担即 LAG 与 hash 策略内容
should-link-02 | swl2-link-redundancy | 双上行不跑生成树且两链路同转即 DHL 双活方案
should-l3-01 | swl2-l3-services | 网关在接入、DHCP 服务器在远端网段需 DHCP Relay 全局/接口配置
should-l3-02 | swl2-l3-services | VRRP 配置与主用选举（优先级）正是三层服务与网关冗余能力
should-qos-01 | swl2-qos-acl-policy | 话机优先级与上网限速对应统一 policy 引擎的 condition+action 与 auto-QoS
should-qos-02 | swl2-qos-acl-policy | 禁 FTP 放行其余属 ACL 条件过滤的典型写法
should-ag-01 | swl2-access-guardian | 802.1x 通过后下发 VLAN+禁 FTP 即 UNP 档案由 Filter-Id 回传触发
should-ag-02 | swl2-access-guardian | 无 MAC 登记设备被 Block 正是 Access Guardian 的默认处置
should-diag-01 | swl2-diagnostics | 端口镜像会话数量上限是诊断工具箱镜像会话口径
should-diag-02 | swl2-diagnostics | 重大事件清单对应 swlog 与可读事件日志四段格式
should-lldp-01 | swl2-lldp-poe | 话机自动进语音 VLAN 并拿 QoS 标记即 network-policy 下发三件套
should-lldp-02 | swl2-lldp-poe | PoE 供电不足断电顺序即 PoE 优先级 low/high/critical 配置
should-upg-01 | swl2-upgrade-autofabric | 插电自动组网即 Auto-Fabric 零触开局，首启 Y/N 语义相反是它的关键点
should-upg-02 | swl2-upgrade-autofabric | 版本选取与 U-boot 密码风险（无恢复场景）都在升级能力内
should-fleet-01 | swl2-fleet-tools | 维保到期与版本分布报表正是 Fleet Supervision 只读资产 KPI
should-fleet-02 | swl2-fleet-tools | OST 2.0 安装前提、Postgres 与 18.1 先装即资产工具能力内容
bait-vlan-01 | swl2-qos-acl-policy | 收到 BPDU 即关口的功能是 qos user-port shutdown bpdu，归属策略引擎能力
bait-aaa-01 | swl2-vlan-routing | 端口划 VLAN 并建网关接口是 VLAN 三入口与 IP 接口激活路由的知识
bait-cfg-01 | swl2-upgrade-autofabric | U-boot 阶段升级失败即 RMA、系统内无法修复，归属升级能力边界而非配置生命周期
bait-link-01 | swl2-link-redundancy | DHL 自动禁 STP，该误区辨析正属链路冗余能力的 DHL 语义
bait-l3-01 | swl2-vlan-routing | 接口 DOWN 根因更可能是 VLAN 无成员而非 VRRP 配错，应激活 VLAN 能力排查
bait-qos-01 | swl2-access-guardian | 认证成功后自动下发禁 FTP 应走 UNP 档案策略，全局 ACL 静态 deny 是错误方向
bait-upg-01 | swl2-fleet-tools | 该按钮是否存在属 OST 工具能力边界问题，应先核对资产工具能做什么
bait-fleet-01 | swl2-fleet-tools | Fleet Supervision 免费只读，能否批量改配置正是其能力边界问题
bait-olc-01 | swl2-upgrade-autofabric | 30 台零触开局对应 Auto-Fabric 七步链，Lightning Config 一次一台本就不适用
bait-ag-01 | none | RADIUS 服务器侧建账号库与申请证书明确标注服务器侧配置在书外，全部能力不适用
edge-mirror-01 | swl2-diagnostics | 镜像会话 2/4 新旧口径并存正是诊断能力的口径边界，声明边界即可
edge-lldp-01 | swl2-lldp-poe | network-policy 5/46 与 7/14 数值不一致是 LLDP 能力内已知的教材边界
edge-vc-01 | swl2-virtual-chassis | 优先级改动必须 reload 才生效，属堆叠选举与 reload 规则
edge-console-01 | swl2-aaa-hardening | console 口默认速率属管理面/会话参数范畴的教材口径问题
```
