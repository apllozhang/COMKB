# entpxte401en 盲判结果（仅依据能力目录，未读答案）

case-id | slug或none | 理由一句
should-ssh-01 | entadv-ssh-trust-foundation | root/mtcl 免密配置与验证正是 oxe-ssh-auth 与三账户密钥路径
should-ssh-02 | entadv-ssh-trust-foundation | 全网批量同步密钥对应 oxe-nw-sshkey-sync 全网五段 CSV
should-cs-01 | entadv-cs-redundancy | 升级业务不中断对应冗余系统不停机升级 11 步
should-cs-02 | entadv-cs-redundancy | 双机都起来后判主对应 double main 与参考 MG 裁决
should-idp-01 | entadv-ip-domain-pcs | 限制域间并发通话数对应 CAC 只闸跨域
should-idp-02 | entadv-ip-domain-pcs | 断网后话机归属与自动回切对应 PCS 四状态判读与回切计时器
should-ovf-01 | entadv-overflow-rerouting | IP 断了从公网绕行对应私到公溢出与 OoS 溢出参数
should-ovf-02 | entadv-overflow-rerouting | 公网拨入自动走专线对应公到私重路由（判别器+ARS、Time-based）
should-dil-01 | entadv-direct-ip-link | 取消 VPN 全 IP 互联对应 Direct IP Link 全互联前提与步骤
should-dil-02 | entadv-direct-ip-link | 直链 2879 排查对应两端带宽/加密/接入数一致否则 2879 的逐项核对
should-aud-01 | entadv-audit-broadcast | 新节点拿全网编号与用户数据对应 Audit 两阶段全网备份
should-aud-02 | entadv-audit-broadcast | RLOG 文件增多而用户未建对应 RLOG 静默失败巡检
should-mls-01 | entadv-multiline-supervision | 秘书看忙闲、代接振铃对应监督键状态/代接/铃型与经理助理键对
should-mls-02 | entadv-multiline-supervision | 仅外部来电才转助理对应过滤表 1000×16 的来话过滤
should-hps-01 | entadv-hunting-pickup-speeddial | 来话轮流分摊对应寻线三搜索的组分发
should-hps-02 | entadv-hunting-pickup-speeddial | 两位短号且受外呼权限管对应速拨编号体系与闭锁受控
should-desk-01 | entadv-desk-sharing | 共享工位登录即跟随对应 DSS/DSU 办公桌共享
should-desk-02 | entadv-desk-sharing | 通话中被强制登出且报 6004 对应忙时重置 6004 系统选项
should-mdev-01 | entadv-multi-device | 话机+DECT 同号同振对应主站+至多 4 副站（DECT 各 1）
should-mdev-02 | entadv-multi-device | 通话中无感挪机对应 Twinset Get Call 无感移机
should-lab-01 | entadv-lab-pod-baseline | POD 实验拨号计划换算对应 ITSP1 号码规则（PN=POD 号）
should-lab-02 | entadv-lab-pod-baseline | Rlab 里迁移组网网卡对应 VM 启动顺序与组网网卡迁移
should-cli-01 | entadv-cli-toolbox | 查主备/域内设备/中继占用的命令对应按功能域归类的命令地图
should-cli-02 | entadv-cli-toolbox | 部署前确认许可锁对应许可锁锚点（186/332/185）
bait-ssh-01 | entadv-audit-broadcast | 表面怀疑 SSH 密钥，实际是 audit 后数据一致性问题，归审计与广播能力
bait-cs-01 | entadv-ip-domain-pcs | 表面问冗余 CS 接管，实际是分部话机域级生存性，归 IP 域与 PCS 能力
bait-idp-01 | entadv-overflow-rerouting | 表面是断网域问题，实际要补的是溢出与重路由配置（OoS 溢出参数）
bait-ovf-01 | entadv-direct-ip-link | 表面溢出话题，实际是重建 Direct IP Link 本身，归直链维护（rsthyb）
bait-dil-01 | entadv-audit-broadcast | 直链已建好，新节点拿全网数据库是 Audit 分发，非在链路加接入
bait-aud-01 | entadv-audit-broadcast | 广播周期后改动未同步，排查 buffer→LOG→lupd.dat 闭环归广播能力
bait-mls-01 | entadv-hunting-pickup-speeddial | 寻线组内 multiline 来话落键行为对应寻线与 multiline 三分支，非监督键配错
bait-hps-01 | entadv-multiline-supervision | 给话务台建监督组要先核对话务台不可监督的规则，归监督能力
bait-desk-01 | entadv-desk-sharing | DSU 键位配置搬回固定话机属 DSU 生命周期与系统选项范畴
bait-lab-01 | none | ITSP1 号码规则明示全部实验口径、生产无此环节，生产中继号码问题超范围
bait-cli-01 | entadv-cs-redundancy | 440 的处置口径（120 分钟窗口与 440 处置）在冗余能力内，重启备机需按规程判断
bait-scope-01 | none | Erlang 话务模型与中继带宽计算不在任何能力范围内，超范围
edge-30day-01 | entadv-ip-domain-pcs | PCS 连续激活 35 天对应 30 天上限规则
edge-irreversible-01 | entadv-direct-ip-link | Enabled 后想回退对应三态 Enabled 不可逆（回退=库恢复）
edge-prefix-01 | entadv-hunting-pickup-speeddial | 组代接前缀疑问对应组代接 zdpost pickup_id 编号体系
