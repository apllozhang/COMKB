# ABC-F 网络加密（IPSec 链路、内部 PKI 双节点、端到端一致性）

## R — 原文依据

> "Signaling between the network nodes is encrypted using IPsec • … Media encryption … is done using SRTP keys sent over the encrypted ABCF network"（p293）
> "The ABC-IP logical link cannot be established in case only one of the two involved nodes has the IP logical link parameter 'Encryption' set to 'Yes'"（p303）
> "THE COMMON NAME IN THE NODE CERTIFICATE IS ALWAYS THE NODE FQDN."（p322）
> "'Transit node' concerns only 'IP Hybrid Link' based network • No transit node in a 'Direct IP Link' based network"（p297）

出处：ENTPXTE421EN p283-332, p303。

## I — 自述

多节点组网的端到端加密：信令靠 IPSec、媒体靠 SRTP，任何一环缺失即明文：

1. **总原则**（p293-294）：
   - 节点间信令（ABC-F/审计/广播）用 IPSec：IPSec Manager（OpenSwan 基）建隧道，端口=协商 500 / TCP 2579
   - IPSec 隧道用证书认证：全网一个 CA、每节点一张专属证书（节点证书 CN 恒为节点 FQDN）
   - SRTP 密钥经加密的 ABC-IP 逻辑链路下发对端——信令链不加密则媒体密钥无从安全分发
2. **链路参数规则**（p330）：
   - 参数位置：Inter-Nodes links/Logical links (ABC-F)/Hybrid or Direct Link Access 的 "other" 页
   - 链路必须 DOWN 才能改（先禁用接入→开 Encryption→重新启用）
   - 两端取值必须相同；仅一侧 Yes 时链路建不起来（即使两侧系统级 NE 都开了）
3. **端到端短木桶**（p295-300/p303）：

   | 缺失环节 | 结果 |
   |---|---|
   | transit 链路未加密 | 跨该段媒体明文（信令仍可能加密） |
   | 对端节点未启 NE | 媒体明文 |
   | 任一端点未开加密 | 媒体明文 |
   | 两侧 SRTP 位数不一致（128 vs 256） | 节点间媒体明文，直连链路信令仍加密 |

4. **拓扑禁区**（p297-298/p301）：transit 节点行为仅存在于 hybrid link 网络；direct link 网络无 transit（直连即端到端）；与 IP Premium Security 不互通；IPv6 设备呼叫明文；AES-256 要求单系统带 'Direct Link' 标签（拓扑与标签分属两个维度）
5. **内部 PKI 双节点变体**（p309-328）：
   - Node1 作签发节点：11.9.1.1 输 CC-suite-ID 一键自签（CA/证书/私钥 7300 天）
   - Node2 一键网络签发：11.9.1.3 生成 CSR→送 Node1 签名→自动回传导入；CN=oxe2.company.com、SAN 含两角色 IP
   - duplication 场景所有条目须用 netadmin/swinst 的 CLONING 选项送 standby
6. **验证抓手**（p290/p332）：hybvisu -f all 看链路 UP 与 Encryption 翻转；跨节点网络呼叫确认加密

## A1 — 书中案例

**Node1 作 CA**（p309-318，c14 步骤 1-6）：

1. Node1 上 netadmin 11.9.1.1，输 CC-suite-ID（实验口径 11111-11111-11111-11111）
2. 通配符 SAN=y、IP SAN=y、4096 位、填 DN
3. 系统生成 Root CA + CS 私钥 + CSR 并签名
4. dhs3_init -R NGINX 后 11.9.1.8 核验（CA CN=CC-suite-ID、7300 天）
5. NE 参数三件套 + 用户 31000 开加密 + lanpbxbuild 配 DTLS
6. IPDSP 弹窗接受自签 CA 证书后出现加密图标

**Node2 网络签发与链路加密**（p319-332，c15/c16）：

1. Node2 上 11.9.1.3 输签发节点 IP=192.168.1.1，一键生成→签名→导入
2. View 核对 CN=oxe2.company.com、SAN 含 192.168.1.103/.101
3. 参数与用户配置同 Node1，lanpbxbuild 配 DTLS 后重启
4. 两侧 WBM 的链路接入先禁用（链路 DOWN）
5. "other" 页激活 Encryption，两端同值后重新启用
6. Authentication for SRTP=Authenticated（网络呼叫必开）
7. 31000 与 31500 跨节点互打确认加密，hybvisu 看 Encryption 翻转

## A2 — 未来触发

使用情境：两个 OXE 节点之间信令媒体都要加密；hybrid 和 direct link 怎么选；节点证书 CN 用什么；链路参数改不了；跨节点通话有一段是明文；第二节点怎么拿到 CA 签发。

语言信号：ABC-F / ABC-IP / hybrid link / direct link / transit node / IPSec / OpenSwan / 500 / 2579 / Logical Link Access / Encryption 参数 / hybvisu / 内部 PKI / CC-suite-ID / 11.9.1.3。

与相邻能力区分：单节点证书体系与外部 CA 归证书与信任链能力；mTLS（OXE 对端点反验）归 mTLS 能力，本卡只管节点间与端到端链路；PCS 分支救援归 PCS 路由卡。

## E — 可执行步骤

输入契约：各节点 NE 参数已启用、链路类型（hybrid/direct）已定、全网单一 CA 策略已确认。混用 IP Premium Security → 判停（不互通）。

1. 定拓扑：hybrid（有 transit，可多级组网）或 direct（无 transit，直连端到端）。完成标准：拓扑决策成文
2. 定 CA：内部 PKI（Node1 自签+Node2 网络签发）或外部 CA 统一签发；节点证书 CN=节点 FQDN。完成标准：证书就位
3. 配端点加密：各节点 NE 参数三件套 + 用户级加密 + lanpbx（DTLS 指向本节点）。完成标准：节点内加密通话正常
4. 开链路加密：选定链路禁用（DOWN）→ "other" 页 Encryption 两端同值 → 重新启用。完成标准：hybvisu 显示 Encryption 翻转
5. 配 SRTP 一致性：Authentication for SRTP=Authenticated 且所有参与网络呼叫的节点同值；AES 位数两侧一致。完成标准：参数矩阵核对通过
6. 验收：跨节点网络呼叫逐一验证；hybvisu 全链路 UP+Encryption。完成标准：全程加密证明

判停点：

- 链路参数改不了 → 链路必须先 DOWN（禁用接入）才能改（p330），别在 UP 状态反复试
- 只有一侧开了 Encryption → 链路直接建不起来，两端同值后重查（p303）
- 客户网络里有 IPv6 设备或老 IP Premium Security 节点 → 明文/不互通预期管理，提前写进方案（p301）
- AES-128 与 AES-256 节点混置 direct link 网络 → 节点间媒体明文（信令仍加密），统一位数或接受明文段（p303）

输出契约：全网链路 Encryption 状态表 + 跨节点加密验收记录 + 节点证书台账。

## B — 边界

- 与 IP Premium Security 互通不可能（书中自注）；IPv6 设备呼叫明文
- AES-256 要求 OXE 数据库带 'Direct Link' 标签（单系统维度），与"仅 hybrid 有 transit"（拓扑维度）分属两事，勿混
- OMS 等 VM 换节点前必须清信任库旧证书（Erase saved certificates），否则在服务异常（p288，实验亲踩）
- 网络加密不需新许可，但跨站点组网的 IP 传输质量与防火墙放行在书外
- CC-suite-ID、节点 IP 等为实验口径，生产按客户许可文件与网段替换
