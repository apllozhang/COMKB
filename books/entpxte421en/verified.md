# verified.md — 三重验证通过单元（阶段 1.5 产出）

> 验证口径: task-first-v2（V1 来源充分性 / V2 可执行性 / V3 任务增益）
> 候选来源: candidates/framework.md f01-f30（主验证对象）；principle p01-p30 / case c01-c19 / counter-example n01-n34 作为各单元的证据素材归并；glossary g01-g52 转 GLOSSARY（见 references.md）
> 验证人: 主会话（2026-09-24），基于 410 页全文通读 + 提取器页码证据交叉核对（p7/p72/p84/p87/p98/p109/p129/p132/p166-168/p247/p367 等关键页已回原文逐格复核）

## 裁决汇总

| decision | 数量 | 单元 |
|---|---|---|
| verified | 26 | f01, f06-f30（f02-f05 之外的全部） |
| reference | 4 | f02（RLAB stand-alone 拓扑）、f03（ABC-F 网络拓扑）、f04（ITSP2 模拟器）、f05（Pod 初始配置）——全部为 RLAB 实验环境专属结构，仅作 Boundary 背景不进能力主线 |
| needs_review | 0（单元级） | 断言级笔误/混用转 needs-review.md（nr-01..nr-05） |
| rejected | 0 | 无编造断言；容量公式（p77/p109）、压缩器降额（p72）、端口模型（p166-167）、事件码（p132）均逐格核对一致 |

verified 明细：f01, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30

## 验证记录

```yaml
- id: f01
  title: 全书课程推进逻辑——密码学底座 → 实验环境 → 概念层 → 四条实验线
  type: framework
  V1: {passed: true, reason: "p4 Lesson Summary 与 p111 起 How-To 章序列完整；四段推进与目录一致"}
  V2: {passed: true, check_mode: walkthrough, input: "新项目按什么顺序交付 OXE 原生加密", expected: "给出可执行阶段顺序", observed: "证书先行→单机 DTLS→SIP TLS/中继→EEGW 扩容→网络化+mTLS，与 c02/c04/c09/c14 章序互证"}
  V3: {passed: true, expected_benefit: "交付排期的顺序基线，避免先开加密后补证书的倒置"}
  decision: verified

- id: f06
  title: 密码学三服务与两类算法对照结构
  type: framework
  V1: {passed: true, reason: "p5-11 讲义完整；p7 非对称算法清单含 Diffie-Helmman 笔误（原样记录，见 nr-01）"}
  V2: {passed: true, check_mode: walkthrough, input: "向客户解释为什么信令加密还分对称/非对称", expected: "混合模式：非对称传会话钥、对称加密数据", observed: "p9 会话密钥每会话更换与 p69 SRTP 对称钥口径一致"}
  V3: {passed: true, expected_benefit: "一切选型对话的概念底座；证据归并 p01/p02"}
  decision: verified

- id: f07
  title: 证书内容与四种文件格式体系
  type: framework
  V1: {passed: true, reason: "p13-15 格式定义逐条给出（PEM/DER/P7B/P12），CSR=P10 于 p16"}
  V2: {passed: true, check_mode: walkthrough, input: "CA 让你选导出格式怎么挑", expected: "P7 有链无私钥（推荐线）、P12 含私钥要口令", observed: "p15 定义与 p103 导入组合表、p391/p397 路线取舍互证"}
  V3: {passed: true, expected_benefit: "证书交接环节的格式对照依据；证据归并 p47(g47)/n30"}
  decision: verified

- id: f08
  title: PKI 三种证书生成模式及优劣对比
  type: framework
  V1: {passed: true, reason: "p18-22 三模式定义+对比表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "内嵌 CA 还是外部 CA", expected: "外部 CA+本地 CSR（PKCS#7）兼得，是推荐线", observed: "p22 优点清单与 c02 实验主线、n30 立场一致"}
  V3: {passed: true, expected_benefit: "交付方案的第一决策点；证据归并 p08(f23)/n30"}
  decision: verified

- id: f09
  title: 证书自动注册三协议对比（SCEP / EST / ACME）
  type: framework
  V1: {passed: true, reason: "p23 时间线+p84 分工清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "能不能用 Let's Encrypt 自动续 WBM 证书", expected: "不能——HTTP-01 需公网可达，须本地 ACME CA", observed: "p84 原文直接回答；n04 三前提齐备"}
  V3: {passed: true, expected_benefit: "证书续期方案规划依据；证据归并 p15/p43-p45/n04"}
  decision: verified

- id: f10
  title: 端到端证书服务器认证三步图（CSR→签发→CTL 预置→连接）
  type: framework
  V1: {passed: true, reason: "p24-25 三步模型完整；CTL 链结构明确"}
  V2: {passed: true, check_mode: walkthrough, input: "端点凭什么信任 CS", expected: "预置在端点信任库的 CTL 验证 CS 证书", observed: "p25 Step3 与 p79-80 CTL 分发两路径互证"}
  V3: {passed: true, expected_benefit: "OXE-端点/EEGW/SBC 所有 TLS 关系的抽象母版；证据归并 p06(g06)/p07(g07)"}
  decision: verified

- id: f11
  title: FSNE 组件兼容三级矩阵（secured / non-secured / incompatible）
  type: framework
  V1: {passed: true, reason: "p63-64 三级清单逐组件列出"}
  V2: {passed: true, check_mode: walkthrough, input: "存量站点能不能整体上原生加密", expected: "按三级归位：CS-2 等老板卡直接出局", observed: "p64 不兼容清单（CS-2/CS-1/CPU7s2/IPv6/IP Premium Security）可直接盘点"}
  V3: {passed: true, expected_benefit: "选型与升级评估的对照表；证据归并 n14/n26/n32"}
  decision: verified

- id: f12
  title: Call Server 加密组件关系图（SIPmotor / NSP / IPSec Mgr / CA / EGW）
  type: framework
  V1: {passed: true, reason: "p76 组件分工图完整"}
  V2: {passed: true, check_mode: walkthrough, input: "TFTP 下载走不走 EGW", expected: "不走——EGW 只承载 DTLS 信令", observed: "p76 'Other flows don't transit via EGW' 原文直接回答"}
  V3: {passed: true, expected_benefit: "理解后续所有拓扑的底图与排障分流依据；证据归并 p02/p03(g02-g04)"}
  decision: verified

- id: f13
  title: EGW 内部/外部容量分界与会话计数公式
  type: framework
  V1: {passed: true, reason: "p77/p109 公式与分界两处一致；p87-88/p200 复述一致"}
  V2: {passed: true, check_mode: walkthrough, input: "1200 并发会话站点要不要 EEGW", expected: "不要——<1500 用内嵌 EGW", observed: "p87 'less than 1500' 与 p109 公式可答；许可 #424/#359 口径齐备"}
  V3: {passed: true, expected_benefit: "售前容量与许可报价的查表依据；证据归并 p09/g17/g18/n19"}
  decision: verified

- id: f14
  title: 一组件一证书体系（工厂证书/自定义证书/单一 CA）
  type: framework
  V1: {passed: true, reason: "p78/p83 证书发放结构与工厂证书边界完整"}
  V2: {passed: true, check_mode: walkthrough, input: "板卡工厂证书在 R101.0 上能用吗", expected: "板卡可正常工作但用不了工厂证书（R101.1 MD4 起）", observed: "p78 图注原文直接回答；p14 版本门槛一致"}
  V3: {passed: true, expected_benefit: "证书供给规划（谁有什么证）的底账；证据归并 p14/g11/n26"}
  decision: verified

- id: f15
  title: 端点获取 CTL 的两条路径与 TOFU 原理
  type: framework
  V1: {passed: true, reason: "p79-80 两路径+TOFU 定义完整；层级上限 5 级"}
  V2: {passed: true, check_mode: walkthrough, input: "客户不接受 TOFU 怎么办", expected: "手工预置 CTL 或 SCEP/EST 自动注册", observed: "p80 'Manual CTL Configuration' 原文给出替代；n10/n11 补信任库清理"}
  V3: {passed: true, expected_benefit: "CTL 分发方案决策依据；证据归并 p06/p07(g06/g07)/n03/n11"}
  decision: verified

- id: f16
  title: 服务器认证与双向认证（mTLS）握手对比
  type: framework
  V1: {passed: true, reason: "p81-83 握手与启用规则完整；p165 端口模型补充"}
  V2: {passed: true, check_mode: walkthrough, input: "开了 mTLS 明文用户还能注册吗", expected: "不能没有证书——所有话机含明文模式都必须有证书，首连总是加密", observed: "p82/p359 大写 Warning 一致；n27 归并"}
  V3: {passed: true, expected_benefit: "安全强化方案的范围与代价评估；证据归并 p26/n26/n27"}
  decision: verified

- id: f17
  title: DTLS 兼容端点拓扑（内嵌 EGW 版）
  type: framework
  V1: {passed: true, reason: "p87 拓扑与端点清单完整"}
  V2: {passed: true, check_mode: walkthrough, input: "话机与 EGW 的会话形态是什么", expected: "每端点一条永久 DTLS 会话（EGW 为服务器）", observed: "p87 原文明确；明文/加密端点可混合（部分加密）"}
  V3: {passed: true, expected_benefit: "DTLS 侧部署底图；证据归并 p07(g07)/p09"}
  decision: verified

- id: f18
  title: SIP TLS 端点拓扑与冗余/PCS/远程工作者行为
  type: framework
  V1: {passed: true, reason: "p88-90 兼容清单/冗余/远程工作者三段完整"}
  V2: {passed: true, check_mode: walkthrough, input: "SIP 扩展走冗余时连几个 CS", expected: "TLS anticipation——与两台 CS 各建一条 TLS（按物理 IP）", observed: "p89 原文明确；PCS 行为 p88-90 与 c05 互证"}
  V3: {passed: true, expected_benefit: "SIP 侧选型与多站点行为预期；证据归并 n14/n16/n18"}
  decision: verified

- id: f19
  title: Native SIP TLS trunk 结构图与"信令/媒体分离"决定表
  type: framework
  V1: {passed: true, reason: "p93 独立性声明+p161 决定表完整"}
  V2: {passed: true, check_mode: walkthrough, input: "只开 SIP TLS 不开 NE 语音加密吗", expected: "不加密——媒体仍是 RTP 明文", observed: "p93/p161 原文一致；n13 误解归并"}
  V3: {passed: true, expected_benefit: "中继方案验收口径的依据；证据归并 p23/n13"}
  decision: verified

- id: f20
  title: 应用生态加密要点图（Rainbow WG / 4645 VM / DR-Link-OPR / VAA / DC）
  type: framework
  V1: {passed: true, reason: "p94-99 五个应用逐一定义；p98 VAA 120→60 逐格核对"}
  V2: {passed: true, check_mode: walkthrough, input: "4645 留言机加密要做什么", expected: "宿主于 NE 开启的 OXE 内自动受保护，仅一个系统参数", observed: "p95 原文直接回答；独立部署才需 eva.cfg+证书"}
  V3: {passed: true, expected_benefit: "应用出口的加密边界与容量代价清单；证据归并 p25-p28(g25-g28)"}
  decision: verified

- id: f21
  title: ABC-F 网络加密四类呼叫拓扑（transit 节点行为）
  type: framework
  V1: {passed: true, reason: "p293-301 总原则与四类拓扑完整；端口 500/2579 于 p301"}
  V2: {passed: true, check_mode: walkthrough, input: "三节点 hybrid 网络中一段链路不加密会怎样", expected: "跨该段的语音媒体明文（短木桶）", observed: "p295 例证原文一致；n31 端到端链归并"}
  V3: {passed: true, expected_benefit: "多节点组网的加密设计与验收口径；证据归并 p25/n31/n32"}
  decision: verified

- id: f22
  title: 管理面地图——WBM/8770/mgr 配置 + netadmin 菜单树 + lanpbxbuild 选项
  type: framework
  V1: {passed: true, reason: "p101 管理三分+各实验章菜单输出连贯"}
  V2: {passed: true, check_mode: walkthrough, input: "生成 CSR 与导入证书走哪个菜单", expected: "netadmin 11.9.1.2 生成、11.9.1.4 导入", observed: "c02 步骤 1/3 与 p113-118 完全对应"}
  V3: {passed: true, expected_benefit: "全书实验的导航坐标，生产操作按同路径；证据归并 p17-p22(g35-g37)"}
  decision: verified

- id: f23
  title: PKI 管理决策树（密钥在哪生成→证书在哪签发）
  type: framework
  V1: {passed: true, reason: "p102 决策树两问完整"}
  V2: {passed: true, check_mode: walkthrough, input: "客户 CA 要求私钥不出机，走哪条", expected: "本地 CSR 送外部 CA（PKCS#7 线）", observed: "p102 否分支与 c02/c19 实验主线一致"}
  V3: {passed: true, expected_benefit: "与 f08 三模式一一对应的执行入口；证据归并 n30"}
  decision: verified

- id: f24
  title: OXE 证书导入格式组合全表（full/partial/all-in-one）
  type: framework
  V1: {passed: true, reason: "p103-106 三用例+菜单问答完整"}
  V2: {passed: true, check_mode: walkthrough, input: "只有 CA 链和 CS 证书两个文件怎么导", expected: "all-in-one 答 n，分别给 CA 与 CS 文件路径", observed: "p104-106 问答流与 c02 步骤 3 完全一致"}
  V3: {passed: true, expected_benefit: "证书交接导入的操作对照；证据归并 n05（导入后连锁义务）"}
  decision: verified

- id: f25
  title: EEGW/SIP Translator 部署六步主流程（CS 侧）与 PCS 侧五步
  type: framework
  V1: {passed: true, reason: "p204-210 六步+PCS 五步（p212-215）完整"}
  V2: {passed: true, check_mode: walkthrough, input: "lanpbx.cfg 的 DTLS 服务器填谁", expected: "外部 EGW 场景填 EEGW IP（端口默认 32643）", observed: "p208 与 c09 步骤 4、p230-233 输出一致"}
  V3: {passed: true, expected_benefit: "大容量扩容的施工主链；证据归并 p28/p29/n19-n22"}
  decision: verified

- id: f26
  title: 内部 EGW → 外部 EGW 迁移四阶段流程
  type: framework
  V1: {passed: true, reason: "p216 四阶段+收尾完整"}
  V2: {passed: true, check_mode: walkthrough, input: "迁移时证书 SAN 要改什么", expected: "主/备 EEGW IP 入 SAN 重生成", observed: "p216 与 c09 证书闭环一致；PCS 场景补 pcscopy"}
  V3: {passed: true, expected_benefit: "扩容演进的变更序列模板；证据归并 n20"}
  decision: verified

- id: f27
  title: S.O.T. 生成与加载 EEGW 虚拟机的工厂流程
  type: framework
  V1: {passed: true, reason: "p272-282 七步完整；浏览器限制 p273、Rocky 口令规则 p279"}
  V2: {passed: true, check_mode: walkthrough, input: "媒体列表为空怎么补", expected: "FTP（upload/sot）传 BootDVD/OST ISO 后 Refresh+Declare", observed: "p274 原文与 c12 步骤 3 一致；n23 归并"}
  V3: {passed: true, expected_benefit: "EEGW 落地的工厂流程入口；证据归并 p21/n23/n24"}
  decision: verified

- id: f28
  title: Native SIP TLS trunk 双侧配置总流程（OTSBC 侧 + OXE 侧 + NSP 切换）
  type: framework
  V1: {passed: true, reason: "p173-184/p185-193/p264-271 三段连贯；TLS context 参数 p175 逐格核对"}
  V2: {passed: true, check_mode: walkthrough, input: "OXE 侧配完 TLS trunk 呼叫不通先查什么", expected: "重启 sipmotor 与两侧端口对齐", observed: "p190 警告+n17/n29 归并可答"}
  V3: {passed: true, expected_benefit: "运营商方向加密中继的完整施工链；证据归并 p23/p24/n29"}
  decision: verified

- id: f29
  title: 端点证书部署矩阵（OMS/GD 板卡 / IPDSP / IP 话机 三线）
  type: framework
  V1: {passed: true, reason: "p356-360/p367-375 三线完整；文件命名 p360 逐格核对"}
  V2: {passed: true, check_mode: walkthrough, input: "IPDSP 证书放哪", expected: "安装目录 softphone_cert.pem+softphone_pkey.pem，口令经 DTLS_PKEY_PASSWORD 或 DTLSPkeyPassphrase.exe 绑定", observed: "p360-361 与 c18 步骤 3 一致"}
  V3: {passed: true, expected_benefit: "mTLS 供给端的部署矩阵；证据归并 p12/n25/n28"}
  decision: verified

- id: f30
  title: SIP TLS 端口模型——Server Auth 5061 / Mutual Auth 6261 四组合
  type: framework
  V1: {passed: true, reason: "p166-168 端口模型完整；p377-379 附录复核"}
  V2: {passed: true, check_mode: walkthrough, input: "互认证端口填 0 会怎样", expected: "覆盖外部网关 True 实际关闭互认证，MAO 界面仍显示 True", observed: "p167 原文一致；n15 陷阱归并"}
  V3: {passed: true, expected_benefit: "trunk 互认证配置与排障的端口对照；证据归并 n15/n29"}
  decision: verified
```

## 断言级裁决记录

1. **principle p05/p72 压缩器数值**：成立。p72 原文 "GD4/GD-XL boards are limited to 45 compressors maximum (instead of 60) and INTIP3 boards to 30 compressors (instead of 60)"，GA4/GA-XL/OXE-MS 无限制，GD3 禁用 AES-256 必须换 GD4——逐格核对一致，已入 verified（f13 归并）。
2. **principle p09 容量公式**：成立。p77 与 p109 两处公式一致（受保护端点报价数 + 3×GD4/GD4-XL/GD3/INTIP3B/OXE-MS + 3×外部 SIP 网关 + 3×节点数），p109 脚注设备清单已并入条目。
3. **framework f04 ITSP 编号混用**：如实记录（原书现象）。p43-46 ITSP1/ITSP2 标签交替出现，n33 已归并；详见 needs-review nr-04。
4. **无 rejected 断言**：DTLS 端口 32643（p121/p124/p208/p230）、事件 5991/5992/5993/5995（p132）、EST 事件 5779/5780（p84）、端口 5061/6261 四组合（p166-167）、VAA 120→60（p98）、许可 424=75/359=30（p129 实验口径）等关键数字均与原文逐格一致。
