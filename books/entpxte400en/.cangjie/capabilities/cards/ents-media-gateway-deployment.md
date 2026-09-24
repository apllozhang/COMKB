# 媒体网关上架（GD4 机架、OMS 虚拟网关、XL 高密度模拟）

## R — 原文依据

> "ALL SHELVES AND BOARDS ARE AUTOMATICALLY CREATED ACCORDING TO THE OPS CONTENTS (HARDWARE.MAO)"（p246）
> "Shelf Type 'Media Gateway Large'; this type is MANDATORY for OMS declaration … OXE Media Server YES; MANDATORY … DO NOT DECLARE NEITHER SECONDARY RACKS NOR BOARDS IN THIS SHELF!"（p260-261）
> "Shelf address: must be a free odd position followed be another free one … XL-Media gateway chassis provides up to 384 * FXS ports"（p758, p75）
> "Enter new crystal number [1..255] (values 18 and 19 are not allowed)"（p250）

出处：ENTPXTE400EN p245-268, p73-78, p757-772。

## I — 自述

硬件上架三条线一个套路：CS 库侧声明（WBM）+ 板侧配置（mgconfig/omsconfig）+ 联动规则（crystal/MAC）：

1. **自动建架**：OPS 恢复后机架与板卡按 hardware.mao 自动创建；槽位坏可换位移动板卡；板卡改型在 WBM Board 页签
2. **GD4 机架**：1U Small（3 槽）/3U Large（9 槽）；主架 0 槽自动生成 GD4；扩展架 Role=Expansion 且填主架地址
3. **OMS 虚拟网关**：四个强制字段——类型 Media Gateway Large、Role Main(Master)、OXE Media Server=YES、地址=VM 侧 crystal number；禁止加扩展架与板卡（虚 GD4 自动落 0 槽）
4. **XL 机架**：奇数地址+连续偶位自动生成；两个半架各由 GD-XL 驱动 6 块 FXS32-XL，整架 ≤384 FXS；GA-XL 只能占 1/2 槽（规划口诀：前 4 块 FXS32 放 3-6 槽）
5. **crystal number 规则**：取值 1-255 且 18/19 保留（虚架 0=CS、19=INTIP 信令）；必须与 CS 库 Shelf address 一致
6. **MAC 登记两情形**：crystal 自动分配或 DHCP 寻址时必须勾 "Ethernet Address checked by TFTP" 并登记板 MAC；换板必须更新，否则 CS 不下发 binom
7. **压缩器声明**：GD4/GDXL 板载 30（+ARMADA=60，许可 #135）；OMS 上限 120（许可 #384 台数/#385 通道），改后须 rstcpl 重启板

| 网关 | 板侧配置入口 | 默认口令（首连强改） | crystal 示例 | 压缩器上限 |
|---|---|---|---|---|
| GD4 | mgconfig | admin=letacla1，root=mg4.ale | 实验取 2 | 30+30 |
| OMS | omsconfig（root 免 sudo） | admin 与 root 均 letacla1 | 实验取 4 | 120 |
| GDXL | mgconfig | admin=letacla1，root=mgxl.ale | 实验取 9 | 30+30 |

## A1 — 书中案例

**GD4 上架实验**（p245-258，How-To）：

1. WBM Shelf 页签核对 OPS 自动建的机架，地址改为与 crystal 一致
2. 板卡页签按硬件实际改型（MG-MIX/BRA/UAI/SLI）
3. V24 或 SSH 进 GD4 板，root 登录跑 mgconfig
4. 配 IP 四件套：本板 IP、掩码、网关、CS Role 地址（实验口径 192.168.1.12/.3）
5. crystal number 切手动设 2，保存并重启板
6. CS 库侧核对 IP Parameters 的 TFTP 勾选与 MAC 登记情形
7. rstcpl 重启板，INIT1/INIT2 后回 IN SERVICE
8. config/cplstat 巡检：GD4 与 MIX484 均 IN SERVICE

## A2 — 未来触发

使用情境：新机架/新板卡上电入网；虚拟化交付配 OMS；高密度模拟口选 XL；板子起不来查 MAC；加 ARMADA 扩压缩器；换板后配置迁移。

语言信号：GD4 / OMS / OXE Media Service / XL / GDXL / FXS32 / 机架 / shelf / 板卡 / board / mgconfig / omsconfig / crystal number / MAC / TFTP / 压缩器 / ARMADA / rstcpl。

与相邻能力区分：上架前的许可恢复见空库与许可能力；模拟/数字用户声明见用户终端开通能力；TDM 功耗约束见用户终端开通能力。

## E — 可执行步骤

输入契约：OPS 许可（含硬件描述）、IP 规划（板侧 IP 与 CS Role 地址）、机位与电源条件（XL 需 -48Vdc 整流器）。crystal 编号先规划后配置，避免与保留值冲突。

1. 核自动建架：WBM Shelf 对照 hardware.mao 核对机架/板卡清单。完成标准：账实一致
2. 建架/改型：按网关类型填 Shelf address（=板侧 crystal）、类型与 Role；XL 用奇数位。完成标准：机架对象就位
3. 板侧配置：mgconfig/omsconfig 配 IP 四件套与 crystal number，保存重启。完成标准：板侧配置落盘（oms.cfg/ipmg.cfg）
4. MAC 联动：自动 crystal 或 DHCP 时勾 TFTP 校验并在库登记 MAC，换板必更新。完成标准：CS 能下发 binom
5. 资源声明：压缩器数（GD4/GDXL 30+30、OMS ≤120）与许可 #135/#384/#385 对齐，OMS 另声明指南并发与会议数。完成标准：资源值在许可范围内
6. 重启生效：rstcpl 重启目标板（GD/GDXL 上执行=整架重启，避开话务高峰）。完成标准：INIT1/INIT2 后 IN SERVICE
7. 巡检：config 全景、cplstat 看板参数、listout 看离服原因码。完成标准：板卡全部 IN SERVICE

判停点：

- 板始终起不来且走 DHCP/自动 crystal → 停，查 MAC 登记与 TFTP 勾选（n13），这是最高频根因
- 话务高峰需要 rstcpl GD 板 → 停，GD4/GDXL 上执行会重启整架所有板（n14），改约维护窗口
- 往 OMS 机架加板卡 → 停，OMS 禁止扩展架与板卡（n16），回退操作
- XL 参数与现场不符 → 书中 GDXL 固件等多处为占位（n38），按最新技术文档核对后再实施

输出契约：IN SERVICE 的机架板卡（GD4/OMS/XL 至少一类）+ crystal/MAC 台账 + 资源声明记录。

## B — 边界

- 全部实验地址/编号（GD4=192.168.1.12、OMS=.13、crystal 2/4/9）为实验口径；生产按现场规划
- -48Vdc 供电与整流器安装工艺、机架硬件安装规范在书外（p77 仅给拓扑）
- Crystal 硬件细节书中自注不再深入（n38）；混装上限每节点 240 racks（含 Common/Crystal/OMS）
- OMS 的 OPUS/G722 为软件独有（硬件 IPMG 不支持）；编解码系统级放行联动在 SIP 中继能力卡展开
- hypervisor 侧（vSphere/KVM 资源、VM 模板）为交付前提，不在本书范围
