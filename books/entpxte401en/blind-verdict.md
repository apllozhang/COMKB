# entpxte401en 判卷报告（blind-results.md vs test-prompts.json）

## 汇总

| 类型 | 通过 | 总数 | 得分 |
|---|---|---|---|
| should_trigger | 24 | 24 | 100% |
| should_not_trigger | 10 | 12 | 83% |
| edge_case | 3 | 3 | 100% |
| **总计** | **37** | **40** | **92.5%** |

## should_trigger 明细（24/24 全中）

- should-ssh-01 / ssh-02 → entadv-ssh-trust-foundation
- should-cs-01 / cs-02 → entadv-cs-redundancy
- should-idp-01 / idp-02 → entadv-ip-domain-pcs
- should-ovf-01 / ovf-02 → entadv-overflow-rerouting
- should-dil-01 / dil-02 → entadv-direct-ip-link
- should-aud-01 / aud-02 → entadv-audit-broadcast
- should-mls-01 / mls-02 → entadv-multiline-supervision
- should-hps-01 / hps-02 → entadv-hunting-pickup-speeddial
- should-desk-01 / desk-02 → entadv-desk-sharing
- should-mdev-01 / mdev-02 → entadv-multi-device
- should-lab-01 / lab-02 → entadv-lab-pod-baseline
- should-cli-01 / cli-02 → entadv-cli-toolbox（cli-02 预期点名"锁 332 与 spadmin"，盲判命中的许可锁锚点卡正是承载处）

## should_not_trigger 明细（10/12）

通过项：
- bait-ssh-01：盲判 audit-broadcast = 预期"应激活 entadv-audit-broadcast" → pass
- bait-cs-01：盲判 ip-domain-pcs = 预期一致，未碰被禁的 cs-redundancy → pass
- bait-idp-01：盲判 overflow-rerouting = 预期一致，未停留在 ip-domain-pcs → pass
- bait-ovf-01：盲判 direct-ip-link = 预期一致，未碰 overflow-rerouting → pass
- bait-dil-01：盲判 audit-broadcast = 预期一致，未停留在 direct-ip-link → pass
- bait-aud-01：盲判 audit-broadcast = 预期"按该卡边界回答（中继组前缀属不广播对象）" → pass
- bait-mls-01：盲判 hunting-pickup-speeddial = 预期一致，未碰被禁的 multiline-supervision → pass
- bait-lab-01：盲判 none = 预期"声明 ITSP1 仅实验口径、不应激活 lab-pod-baseline" → pass
- bait-cli-01：盲判 cs-redundancy = 预期"应转入 cs-redundancy 处置 440" → pass
- bait-scope-01：盲判 none = 预期"任何能力卡都不应激活，声明边界" → pass

## edge_case 明细（3/3）

- edge-30day-01：盲判 ip-domain-pcs → pass，卡内"30 天上限"直接支撑预期边界答案
- edge-irreversible-01：盲判 direct-ip-link → pass，卡内"Enabled 不可逆（回退=库恢复）"即预期答案
- edge-prefix-01：盲判 hunting-pickup-speeddial → pass，组代接前缀知识所在卡，配合"以现场 Translator 实查为准"即为预期勘误口径，非乱路由

## 失败清单（2 条）

### 1. bait-hps-01 — FAIL
- 题面："把前台话务台的等待队列调成 8 路，再给话务台建个监督组"
- 预期：超出本书范围（OXE 话务台/监督组配置不在本教材），不应激活 entadv-hunting-pickup-speeddial 硬套寻线组，即应判 none 并声明边界
- 盲判：entadv-multiline-supervision
- 偏差分析：盲判方向避开了点名陷阱（未把话务台队列硬套寻线组，未命中被禁的 hps），但为了用卡内"话务台与寻线组不可监督"这条规则去回答第二问，激活了 multiline-supervision 卡。按判卷规则，预期 none 的超范围题须盲判 none 才算 pass，激活任一能力卡即偏离。属"半对"路由：结果上能产出边界声明，路由口径上不干净。

### 2. bait-desk-01 — FAIL
- 题面："DSU 用户想把他工位上的键位配置永久搬到自己的固定话机上，以后不再共享了"
- 预期：应转 entadv-multi-device 或常规装机/用户配置思路（固定化不是 DSU 场景），不应停留在 entadv-desk-sharing 当作可解决
- 盲判：entadv-desk-sharing
- 偏差分析：盲判被题面"DSU"关键词锚定，把"永久固定化/退出共享"误判为 DSU 生命周期内事务；预期认定这是场景错位——用户要的已不是共享工位，而是多设备/常规配置范畴，继续用 desk-sharing 卡会把不可解的事当作可解。盲判正好命中预期点名"不应停留在"的那张卡。
