# EEGW/NSP 大容量部署（外部加密网关、SIP Translator、S.O.T. 生成）

## R — 原文依据

> "External Virtual Machine mandatory • OXE redundancy: one dedicated EEGW per Call Server • Includes the SIP Translator (NSP) • Virtualization of OXE mandatory"（p200）
> "The call server goes for reboot if the link with the external EGW is lost"（p203）
> "Warning THE CALL SERVER ASSOCIATED TO THE EEGW VIRTUAL MACHINE WILL REBOOT TOO!"（p239）
> "NSP FQDN is mandatory as soon as CS redundancy is implemented."（p266）

出处：ENTPXTE421EN p77, p199-216, p217-243, p244-271, p272-282。

## I — 自述

会话数超 1500 后的强制形态：EEGW 虚拟机（OST 包，Rocky Linux）承载 DTLS，内含 NSP 承载 SIP TLS：

1. **容量分界与许可**（p63/p77/p109/p200）：

   | 形态 | 会话上限 | 形态要求 |
   |---|---|---|
   | 内嵌 EGW（CS/PCS 内） | <1500 并发 DTLS/TLS | 默认，零额外部署 |
   | EEGW（每 CS 一台） | 1500-15000 | 强制 VM、OXE 须虚拟化、需人工报价 |

   - 会话数=受保护端点报价数+3×(GD4/GD-XL/GD3/INTIP3B/OXE-MS)+3×外部 SIP 网关+3×节点数
   - 许可 #424（系统 DTLS/TLS 会话）与 #359（并发 SIP TLS 通信）两个维度
2. **五条硬规则**（p200-203/p239）：
   - EEGW 强制外部 VM；OXE 自身必须虚拟化部署
   - CS 与其 EEGW 必须同物理主机、同一虚拟交换机
   - CS-EEGW 间专用明文 UA/UDP 链路兼做存活监控，断链 CS 直接重启
   - EEGW VM 上证书操作触发重启时，关联 CS 连坐重启——变更按 CS 重启级规划
   - 冗余场景每台 CS 一台专属 EEGW
3. **CS 侧六步部署**（p204-210）：
   - 声明：netadmin 20（EEGW IP）+19.2（Translator 名 nsp）——任一变更都要重生成 CS 证书+OXE 重启+copy to twin
   - 防火墙/解析：EEGW IP 进 CS 内部防火墙（11.1.3）；Translator FQDN 必须可解析（内部 DNS 17.2 或外部 DNS 委托）
   - 证书：SAN 按五字段顺序装 EEGW 地址/FQDN/通配符/Translator FQDN
   - lanpbx.cfg：DTLS_SRV 填 EEGW IP（端口默认 32643）
   - VM：ostconfig 配 IP 与 CS 地址 → 11 Download Certificates（SSH key 已存在时勿重生成）→ 12 Certificate check 核对 SAME
4. **NSP 指向规则**（p247/p266/p29）：仅外部 EGW 场景强制声明 Translator；冗余场景 SBC 必须用 NSP FQDN（内部 DNS 仅主 CS 应答→返回主 CS 的 EEGW IP），单机才可直填 EEGW IP
5. **S.O.T. 工厂流程**（p272-282）：Greenfield 工程、产品 OST、FTP 补媒体（upload/sot）、机器类型 EEGW/Sizing/IP，Deploy 生成 .ova 后 ESXi 部署；首登 root/letacla1 立即改密（Rocky ≥14 位强化规则）
6. **内嵌→外部迁移四阶段**（p216）：mao 声明 EEGW IP、重生成证书（EEGW IP 入 SAN）、重建 lanpbx（DTLS1/2=两台 EEGW IP）、装 VM，最后整体重启

## A1 — 书中案例

**EEGW 部署实验**（p217-243，c09 步骤 1-8）：

1. netadmin 20.2 声明 EEGW：Main=192.168.1.7、twin=192.168.1.8（实验口径），确认触发证书重生成
2. 11.1.3 受限访问加 eegwcpua/eegwcpub 信任主机
3. 重做 PEM 证书闭环：CSR 含 EEGW 的 IP/DNS SAN，签发后经 11.9.1.4 导入并 View 核对
4. copy to twin 后 dhs3_init -R NGINX
5. lanpbxbuild 里 j=192.168.1.7、k=192.168.1.8，Apply 后重启 CS
6. WBM 的 IP/Encryption GW 显示 EGW IP 不等于 CS IP（EXTERNAL）
7. 两台 EEGW 各自 ostconfig 配 IP/CS 地址并 Download Certificates（CS 连带重启）
8. Certificate check 显示 SAME；cryptview 显示 DTLS server address (External EGW)

**NSP 切换实验**（p264-271，c11）：SBC Proxy Set 改指 nsp.oxe.company.com:5061，17.2 激活内部 DNS，SBC console ping 验证解析到主 CS 的 EEGW IP 后全链路加密。

## A2 — 未来触发

使用情境：站点超 1500 会话怎么扩；EEGW 怎么装；NSP/SIP Translator 是什么；改 EEGW IP 要动什么；EEGW 重启会不会影响话务；SBC 该指向哪个地址。

语言信号：EEGW / External Encryption Gateway / OST / ostconfig / SIP Translator / NSP / nsp.oxe / S.O.T. / Greenfield / OVA / ESXi / 1500 / 15000 / Download Certificates / config ost / 内部 DNS。

与相邻能力区分：容量计算与许可看本卡 I 段第 1 条（Sizing 细节书外）；证书 SAN 装配归证书与信任链能力；SBC 侧 TLS context 归 SIP trunk 能力；PCS 外接 EEGW 归 PCS 接管（路由卡）。

## E — 可执行步骤

输入契约：会话数测算超过 1500、OXE 已虚拟化、ESXi 资源就位、变更窗口按"CS 重启"批准。OXE 是物理机 → 判停（EEGW 前置不满足）。

1. 测算与报价：按公式算会话数；EEGW 需人工报价，15000 为上限。完成标准：容量与许可方案成文
2. 声明：netadmin 20 声明 EEGW IP、19.2 声明 Translator 名——一步到位避免改名循环。完成标准：声明保存并知悉重启代价
3. 网络前置：11.1.3 把 EEGW IP 加入内部防火墙；17.2 激活内部 DNS 或外部 DNS 委托。完成标准：防火墙与解析双就绪
4. 证书与 lanpbx：重生成证书（EEGW 地址入 SAN）→ lanpbx DTLS 指向 EEGW → copy to twin。完成标准：SAN 核验通过
5. 生成 VM：S.O.T. 建 Greenfield 工程（仅 Chrome/Firefox），媒体缺失先 FTP 上传，Deploy 出 .ova。完成标准：ESXi 部署完成
6. 配置 VM：首登按 Rocky 规则改密（≥14 位）、ostconfig 配 IP/CS 地址、Download Certificates、Certificate check 核对 SAME。完成标准：证书两侧一致
7. 验证：config ost 两行 IN SERVICE；cryptview 显示 External EGW；SBC ping NSP FQDN 解析正确。完成标准：端到端加密通话

判停点：

- 变更窗口只按"VM 重启"申报 → 停下重报：EEGW 证书下载/声明变更会连带 CS 重启（p239 大写警告）
- 冗余站点把 SBC 指到固定 EEGW IP → 必须改用 NSP FQDN，否则主备切换后信令断（n22）
- EEGW VM 规格（CPU/内存）怎么定 → Sizing 只按最大用户数（p276），规格与压测口径在书外，按 OXE 安装文档
- 下载证书提示 SSH Key 已存在 → 勿重生成（答 n），否则破坏既有信任关系（n24）

输出契约：EEGW/NSP 上线 + 证书一致核验 + SBC 指向与解析验证 + 变更窗口记录。

## B — 边界

- EEGW 的 VM 规格、压测口径、跨主机高可用不在原书范围（Sizing 仅"最大用户数"）
- transit/大容量拓扑下的抓包点与 SIP TLS 解密原书未覆盖
- PCS 侧外接 EEGW 的判断（PCS EGW IP=PCS IP 即内嵌、不同即外接）在 PCS 路由卡
- 全部 IP/口令/主机名（eegwcpua、letacla1、Superuser2580* 等）为实验口径，生产必须替换
- 会话公式是许可计数口径，实际并发话务建模在书外
