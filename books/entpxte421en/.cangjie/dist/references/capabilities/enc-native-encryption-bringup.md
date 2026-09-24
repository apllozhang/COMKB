# 原生加密开通与 lanpbx.cfg（系统参数、用户级加密、DTLS 载体）

## R — 原文依据

> "Enable Native encryption … True: Native Encryption is enabled … False (default)"（p119）
> "DTLS_SRV Main DTLS server IP address (physical IP address of the main OXE, when the internal EGW module is used, or IP address of the associated EGW virtual machine…)"（p124）
> "IN CASE OF A COMMUNICATION SERVER DUPLICATION, THE LANPBXBUILD TOOL MUST BE LAUNCHED ON THE MAIN COMMUNICATION SERVER."（p121）
> "At least one of TLS cipher suite must remain selected among both, otherwise the encryption devices won't be able to connect."（p68）

出处：ENTPXTE421EN p63-74, p119-125, p228-233。

## I — 自述

证书就位后开通功能：系统参数 → 用户级加密 → lanpbx.cfg 三层推进：

1. **Native Encryption 参数块**（System/Other System Param.，p119）：
   - Enable Native encryption（默认 False）：总开关，开后 IPMG 与 PCS 一律加密不可明文
   - Enable automatic CTL Acquisition（True=CTL 经 lanpbx.cfg 自动下发）
   - Authentication for SRTP：Unauthenticated（默认）/Authenticated/Authenticated tag emis. w/o ctrl；IPDSP 只工作在认证模式，部署 IPDSP 即锁定 Authenticated
   - TLS cipher suite 两条（AES_128_GCM_SHA256 与 AES_256_GCM_SHA384）：至少保一条，否则加密设备连不上；信令位数与话音位数相互独立
2. **SRTP Cipher Suite**（p70-72 二选一不混用）：
   - AES-128：默认，无硬件代价
   - AES-256：GD4/GD-XL 压缩器 60→45、INTIP3 60→30、GD3 禁用必须换 GD4；只支持 AES-128 的设备通话回落明文；改后必须重启 OXE
3. **用户级部分加密**（p66）：
   - 每个用户选项 Native encryption 逐台开关；过渡期新旧话机混存
   - DSS/DSU（桌面共享）与 ProACD/agent（呼叫中心）上下文必须同质配置
4. **lanpbx.cfg 的 DTLS 字段**（p124 十字段）：
   - DTLS（配置 DTLS_SRV 即自动 ENABLED）、DTLS_SRV/DTLS_SRV_RD、DTLS_PORT（默认 32643）
   - OXE_FQDN、DTLS_CERT_TRUST（PEM 格式 CTL 自动注入）、DTLS_SIGN_CERT/FILE（签名对）与 _ALT 旧证书旧签名
5. **lanpbxbuild 规则**（p121-122）：
   - duplication 只能在 main CS 执行；自动产出 lanpbx.cfg + lanpbxtwin.cfg 并同步 standby
   - -auto 会重置 IP_CPU/IP_DOWNLOAD 外的全部既有配置
   - 先激活 NE，j/k（DTLS1/2 地址）选项才可用；每次 Apply changes（6）重签 CTL 与文件，改动后重启 CS 生效

## A1 — 书中案例

**DTLS 开通实验**（p119-126，c02 步骤 6-9）：

1. System/Other System Param./Native Encryption parameters 打开参数块
2. Enable Native encryption=True、Enable automatic CTL Acquisition=True
3. Authentication for SRTP=Authenticated（IPDSP 场景必选）
4. Users 选 31000/31002/31003 → 8&9 Series Parameters → Native encryption=Enable
5. Phone COS/0 页 Display Encrypted Communication=YES（话机显示加密图标）
6. mtcl 执行 lanpbxbuild -auto 建文件（新装口径）
7. lanpbxbuild → 4 Modify → j 填 DTLS1=192.168.1.1、k 填 DTLS2=192.168.1.2（实验口径）
8. 6 Apply changes：输出 CTL 生成与 Native Encryption signing 两段
9. 重启 OXE CS；WBM 的 IP/Encryption GW 显示 EGW IP=CS IP（内部 EGW）

## A2 — 未来触发

使用情境：打开原生加密总开关；给部分用户开加密；SRTP 用 128 还是 256；lanpbx.cfg 怎么生成；DTLS 端口改多少；duplication 环境 lanpbx 在哪台做。

语言信号：Enable Native encryption / Native Encryption parameters / Authentication for SRTP / SRTP Cypher Suite / AES-256 / lanpbx.cfg / lanpbxbuild / DTLS_SRV / 32643 / partial encryption / copy to twin。

与相邻能力区分：证书还没就位找证书与信任链能力；开完要验证找验证与维护能力；DTLS 服务器指向外部网关归 EEGW 部署能力；安全关掉看 SIP trunk 能力内的停用段（c08 同路径）。

## E — 可执行步骤

输入契约：证书已就位（CA/CS 证书 + twin 同步完成）、端点台账（哪些用户先加密）、板卡清单（有无 GD3/INTIP3）。证书未就位 → 判停回证书能力。

1. 核硬件前提：有 GD3 只能 AES-128；打算 AES-256 按 GD4/GD-XL 60 换 45、INTIP3 60 换 30 重算压缩器容量。完成标准：cipher suite 决策成文
2. 配系统参数：Native Encryption 参数块按 I 段口径逐项配置（IPDSP 站点锁 Authenticated）。完成标准：参数保存
3. 开用户级加密：按台账逐用户 Enable，共享上下文（DSS/DSU、ProACD）整组同质。完成标准：加密/明文用户清单确认
4. 生成 lanpbx.cfg：duplication 在 main 跑 lanpbxbuild；j/k 填 DTLS 服务器（内嵌 EGW=CS 物理 IP）；6 Apply changes 重签。完成标准：CTL_sign OK 与签名输出出现
5. 重启生效：重启 OXE CS（duplication 双 bascul）；改 cipher suite 场景必须重启系统。完成标准：EGW 菜单可读
6. 核对落盘：more /usr3/mao/lanpbx.cfg 检查 DTLS/DTLS_SRV/DTLS_PORT/签名字段。完成标准：字段与方案一致

判停点：

- 端点含只支持 AES-128 的设备（IP-xBS、Android IPDSP、hybrid link ABC 网络）而客户要 AES-256 → 明确告知这些设备通话会回落明文 RTP，先盘点再切换（n01）
- 想用 lanpbxbuild 的 j/k 但 NE 没激活 → 先开系统参数再回来（p122）
- 改了参数"没生效" → 对号生效动作：TLS 信令重启 CS、SRTP 认证重启 SIPMOTOR、mTLS 重签 lanpbx + 重启（n17）

输出契约：加密参数+用户清单+签名后的 lanpbx.cfg + 重启记录。

## B — 边界

- 全部实验参数值（IP/口令/分机号）为 RLAB 实验口径，生产按客户环境整体替换
- IPMG 与 PCS 恒加密：部分加密只对 DTLS/TLS 能力端点用户生效，不能给 IPMG 开明文（p65）
- 切换加密模式需要话机重启；CS 每次设备连接后按型号+版本核对加密能力（p66）
- EEGW 场景 DTLS_SRV 填 EEGW IP 而非 CS IP——那是 EEGW 部署能力的迁移段（p216）
