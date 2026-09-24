# vsaaxte001en 盲测评判报告

## 汇总

| 类型 | 通过 | 总数 |
|---|---|---|
| should_trigger | 23 | 24 |
| should_not_trigger（诱饵） | 9 | 12 |
| edge_case | 4 | 4 |
| **总计** | **36** | **40** |

## 判卷说明

- should_trigger：24 条中 23 条盲判与预期能力一致；should-maint-02 不一致（见失败明细）。
- should_not_trigger：
  - 命中预期"另一能力"：bait-ivr-01（db-integration）、bait-ha-01（architecture-redundancy）、bait-maint-01（webadmin）、bait-webadmin-02（maintenance-backup）、bait-sizing-02（预期明确"应按 vaa-server-sizing-virtualization 声明边界"）、bait-install-01 之外的全部跨卡诱饵均 pass；
  - 预期 none 且盲判 none：bait-tree-01、bait-stats-01、bait-pcs-02、bait-arch-02，pass；
  - 三条 fail 见下方明细。
- edge_case：4 条盲判路由（install / master-slave-ha / ivr-option-nodes / statistics-reporting）均落在对应能力卡上，合理，pass。

## 失败明细

### 1. should-maint-02（should_trigger）
- 预期：激活 vaa-maintenance-backup（升级七步：备份先行、vaa.conf 逐值比对、HA resync）。
- 盲判：vaa-install-sip-integration。
- 偏差分析："4.8.006 只支持全新安装 + 数据库恢复"这条关键约束写在 install 卡的目录描述里，盲判据此把升级问题路由到安装卡；而升级操作规程（升级七步）在 maintenance 卡。两卡各持一半事实，属于能力目录描述切分导致的天然歧义，盲判选了"版本约束"所在卡，预期选了"操作规程"所在卡。

### 2. bait-install-01（should_not_trigger）
- 预期：超出书内范围（原书仅 SUSE + ALE BootDVD 口径），应声明边界（预期 none），不应按 vaa-install-sip-integration 流程编造步骤。
- 盲判：vaa-server-sizing-virtualization。
- 偏差分析：盲判把"来宾操作系统选型（CentOS vs SUSE）"并入"服务器选型与虚拟化"卡，但该卡目录只覆盖 Hypervisor 前提（ESXi/Hyper-V/Proxmox），操作系统支持是另一层口径，书内无 CentOS 任何表述，预期是不激活任何卡、直接声明边界。盲判属"多走了一卡"的近失，非乱路由。

### 3. bait-prompt-01（should_not_trigger）
- 预期：引擎音质调优超出原书范围，应声明边界，不应以 vaa-prompt-tts-asr 给出虚构参数。
- 盲判：vaa-prompt-tts-asr。
- 偏差分析：盲判把"TTS 音色不够自然"归入 TTS 引擎选型（Pico 与 Google Cloud TTS 之别），但该卡内容只有引擎选型与格式约束，没有音色调优内容；预期点名禁止借该卡作答，盲判恰好命中被禁能力，属对题面范围（调优 vs 选型）判断偏宽。

### 4. bait-db-01（should_not_trigger）
- 预期：NoSQL 无 JDBC 驱动口径，应声明边界，不应激活 vaa-db-integration 编造方案。
- 盲判：vaa-db-integration。
- 偏差分析：盲判思路是"到 db 卡查支持的数据库清单再答"，而卡内"默认仅 PostgreSQL/MariaDB"确实足以支撑边界声明，此条存在辩护空间；但预期文字明确"不应激活 vaa-db-integration"，盲判字面命中被点名的禁止卡，按规则从严判 fail，并在此标注其为边界争议案例。
