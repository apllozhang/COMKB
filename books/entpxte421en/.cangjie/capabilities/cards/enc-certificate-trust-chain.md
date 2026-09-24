# 证书与信任链全生命周期（PKI 策略、CSR 五步闭环、CTL/TOFU）

## R — 原文依据

> "OXE supports up to 5 levels of CA hierarchy (Root CA→ Sub CA1 → Sub CA2…)"（p79）
> "First CTL acquisition is done in 'trust on first use' (TOFU) mode."（p80）
> "PKCS7 is the easiest and may be the best way to generate certificate(s) signed by an external PKI (CA) because the private key of the entity doesn't move"（p391）
> "CA update requires: 1.Immediate regeneration of lanpbx followed by an OXE reboot. … 2.PCS certificate(s) to be generated manually"（p104-106 Warning）

出处：ENTPXTE421EN p13-25, p78-85, p102-108, p113-118, p391-403。

## I — 自述

证书是全书一切加密动作的钥匙，交付前的三个决策与一条主线：

1. **PKI 模式决策**（p18-22 三选一）：
   - Internal PKI：密钥/CSR/根 CA 全部系统内生成、根 CA 自签——最快但客户端默认不认
   - PKCS#12：私钥在 CA 生成后打包搬运——私钥搬家、CN/SAN 手工填易错，仅端点证书场景
   - PKCS#7/PEM/DER：CSR 在实体上生成、外部 CA 只回签证书——私钥不出机、SAN 自动，**推荐主线**
2. **CTL 分发决策**（p79-80 两路径）：
   - 自动：CTL 打进 lanpbx.cfg 推送（仅 DTLS 设备），首连走 TOFU（首连不验证书，之后全量认证）
   - 手工：客户拒绝 TOFU 时逐台预置 CA 链，或走 SCEP（话机）/EST（IPMG）自动注册
3. **命名规则**（p344/p322）：
   - 板卡/话机/软话机实体证书 CN=设备 MAC 地址，Type=End Entity
   - CS/PCS 证书 CN=OXE FQDN；节点证书 CN 恒为节点 FQDN
4. **CSR 五步闭环**（p113-118）：生成 CSR（netadmin 11.9.1.2）、外部 CA 签发、导入（11.9.1.4）、核验（11.9.1.8）、复制 twin（10.2）后执行 dhs3_init -R NGINX
5. **CA 更新连锁义务**（n05）：立即重生成 lanpbx + OXE 重启；配了 PCS 的必须手工重生成 PCS 证书——否则 OXE 与端点间 CTL 不一致引发通信故障
6. **备份规则**（p107/p133）：每次证书变更后 netadmin 11.9.1.5 导出（或随 swinst Linux Data 备份），口令 ≥8 位含大小写/数字/特殊字符

## A1 — 书中案例

**PKCS#7 主线实验**（p113-118，c02 步骤 1-5）：

1. mtcl 登录后 su - root，netadmin -m 进 11.9.1.2 Generate CSR
2. 交互作答：通配符 SAN=y、SAN 配 IP=n、附加 SAN=n、密钥 4096、填 DN（FR/BZH/BREST/ALE/EDUC）
3. CSR（/tmpd/csa.csr）经 SFTP 传共享盘 PODx，等 CA 管理员签发取回 cs.p7b
4. ca.p7 与 cs.p7b 放回 /tmpd，11.9.1.4 导入，all-in-one=n，逐个给文件路径
5. 导入成功提示 Certificates Successfully Imported，随后删除中间文件
6. 11.9.1.8 View 核验 issuer/subject/有效期/SAN（DNS:oxe.company.com, DNS:*.company.com）
7. 10.Copy setup → 2.Copy to twin (all)，再执行 dhs3_init -R NGINX

**内部 PKI 变体**（p310-312，c14）：netadmin 11.9.1.1 输 CC-suite-ID 一键自签，CA/证书/私钥有效期一律 7300 天。

## A2 — 未来触发

使用情境：选内嵌 CA 还是外部 CA；证书导出格式怎么选；CSR 怎么生成；CTL 怎么到端点；客户不接受 TOFU；证书快到期；CA 换新后系统行为诡异。

语言信号：CA / CSR / PKCS#7 / PKCS#12 / PEM / DER / 证书链 / CTL / Trust List / TOFU / trust on first use / SAN / Common Name / 证书导入 / 证书备份 / 7300 天。

与相邻能力区分：证书就位后的功能开关（参数/lanpbx）归原生加密开通能力；给端点做证书（XCA 操作）归 PKI 工坊（路由卡）；证书导入后的加密验证归验证与维护能力。

## E — 可执行步骤

输入契约：客户 CA 归属（内嵌 CA/客户企业 CA）、客户是否接受 TOFU、站点拓扑（有无 EEGW/PCS/冗余）。客户 CA 治理流程不明 → 判停确认。

1. 定 PKI 模式：默认推荐 PKCS#7 线（本地 CSR + 外部 CA）；无外部 CA 时内嵌 CA 一键自签。完成标准：模式与 CA 归属书面确认
2. 定 SAN 策略：默认带 IP SAN；答 n（无 IP）前核对终端固件支持清单（IP-xBS 与 NOE 模式 80x8s 不支持，见 B）。完成标准：SAN 字段清单成文
3. 生成 CSR：netadmin 11.9.1.2，密钥 4096（下限 2048），DN 与通配符按方案作答。完成标准：CSR 文件产出
4. 签发与导入：外部 CA 签发后 11.9.1.4 导入（all-in-one 按文件形态作答）。完成标准：Certificates Successfully Imported
5. 核验与同步：11.9.1.8 核对 issuer/subject/SAN/有效期 → 10.2 Copy to twin → dhs3_init -R NGINX。完成标准：主备证书一致
6. 收尾两件：11.9.1.5 导出备份（口令 ≥8 位四类字符）；CA 更新场景重生成 lanpbx + 重启 + 手工重做 PCS 证书。完成标准：备份文件入库

判停点：

- 客户企业 CA 的签发流程/审批链不明 → 签发环节在书外，找客户 PKI 运营方，不要替客户假设"秒签"
- 站点存在 IP-xBS 或 NOE 模式 80x8s → 无 IP SAN 证书可能导致终端永远无法投入服务，必须先查 release notes（n03）
- 内嵌 CA 的 CC-suite-ID 不在许可文件中 → Root CA CN 无法生成，先补许可再走自动生成（p311）

输出契约：证书就位且主备一致的 OXE + 备份文件 + SAN/格式决策记录。

## B — 边界

- 企业 PKI 运营（CA 私钥保管、CRL/OCSP 基础设施、审批流程）原书只有概念页（p12/p17），无运营内容——生产签发流程以客户 CA 规程为准
- "2025 年底起新产板卡默认嵌 ALE 证书"是时效性承诺（p78），落地前核对当前出厂策略
- 工厂证书仅 GD4/GA4/GD-XL/GA-XL 板卡、话机与 IP-xBS 有，板卡侧自 OXE R101.1 MD4 起可用（低版本不报错但证书闲置）
- 证书吊销（CRL/OCSP）在 OXE 侧无操作实验，仅概念页——吊销执行在书外
- 本卡全部菜单路径与实验值（口令、CC-suite-ID 等）为培训实验口径，生产按客户环境替换
