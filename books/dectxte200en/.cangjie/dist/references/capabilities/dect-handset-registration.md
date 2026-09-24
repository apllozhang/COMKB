# DECT 用户创建与手机注册/注销（webadmin 与 dectinston/dectrm 双通道）

## R — 原文依据

> "Warning THE POINT 2.2 HAS TO BE DONE MORE OR LESS SIMULTANEOUSLY WITH POINT 2.1.1 OR 2.1.2 TO REGISTER A DECT ONLY ONE OF THE 2 METHODS MUST BE USED"（p169）
> "command dectinston <directory number> or dectinston -g ... Wait until the set rings, but you don't have to hang up!!! Press 0 to leave. Installation succeed. Effective Security Level : Use Authentication"（p170）
> "Warning TO DEREGISTER A DECT ONLY ONE OF THE 2 METHODS MUST BE USED: POINT 1.1.1 OR 1.1.2"（p175）
> "If the handset has been deregistered to be changed/replaced ... it is not necessary to delete the user from the OXE DB."（p177 Tips）

出处：DECTXTE200EN p162-177, p235-241。

## I — 自述

手机注册是"系统开启等待 + 手机侧发起"的配对动作，两条铁律：**双通道只能取一**、**系统侧与手机侧操作必须近乎同时**。

1. **建用户**：Users → Create → 目录号 + 姓名（20 字符内）+ Set type。Set type 决定功能面：GAP（基础服务，8214）或 GAP+/A-GAP（多线扩展、监督键、经理/秘书键，需 8234/8244/8254/8262/8262EX）。
2. **注册通道 A（webadmin）**：Users / <用户> / DECT set 点 DECT Register，同时在手机侧操作；完成后 IPUI N/IPUI O 字段回填。
3. **注册通道 B（mtcl）**：dectinston <目录号> 或 -g，（可选）指定基站，核对 GAP 特性回显（DN/用户名/MAO type/PARI/PLI），按 Y；手机响铃后**按 0 退出（不要挂断）**，输出 "Installation succeed. Effective Security Level: Use Authentication"。
4. **手机侧**：依次按 Yes、Select，输 PIN、Ok，输 AC 码（若系统配置了 AC System，实验 1111），选 Normal、Yes；响一声并屏显注册信息。
5. **注销**：DECT Deregister（webadmin）或 dectrm <目录号>（Y 确认 → "Operation succeed"，输出含 IPEI），同样双通道取一；换机维护场景不删用户，新手机直接重注册。

安全级别关联（p35-37/p144/p227）：Security level 三级——Identity（默认，仅核对 IPUI-N）/ Authentication（注册时 AC 双侧比对）/ Encryption（仅 IP-xBS 支持，IBS 不可选）；AC 不一致则注册无法成功。

## A1 — 书中案例

**注册与注销实验**（p167-177，xBS 版与 IBS 版同构）：

1. 建用户 31015/31016（GAP+）、31017（GAP）（实验口径）
2. mtcl 下 dectinston 31015，核对回显，按 Y；手机响铃按 0，输出 "Installation succeed"
3. 有效安全级别显示 Use Authentication（AC=1111 时手机侧输入该码）
4. webadmin 核验 IPUI N/IPUI O 字段已回填（p169）
5. 注销：dectrm 31015 → Y → "Operation succeed"（输出 IPEI 1410309133756，p176）；手机屏显已注销
6. 换机演练：不删用户，直接用新手机重注册（p177 Tips）

## A2 — 未来触发

使用情境：给员工开通 DECT 分机；手机注册不上；注册到一半超时；要不要选 GAP 还是 GAP+；员工换新手机；离职回收手机。

语言信号：注册 / register / DECT Register / dectinston / 注销 / deregister / dectrm / IPUI / IPEI / GAP / GAP+ / A-GAP / Set type / AC 码 / PIN / 安全级别 / Security level / 加密。

与相邻能力区分：PARI/PLI 变更后的批量迁移见自动重注册能力；AC 与安全级别规划见本卡安全段与标识号码能力；8328 手机的 SIP 注册见 SIP-DECT 能力（路由，另一套语义）。

## E — 可执行步骤

输入契约：用户清单（目录号/姓名/机型）、系统 AC System 值、基站已在网。基站未入网 → 先回 IP-xBS/IBS 部署能力。

1. 建用户：Users → Create，目录号/姓名/Set type 按机型定（8214=GAP，82x4/8262=GAP+）。完成标准：用户在库
2. 选定单一通道：webadmin 或 mtcl，二选一并贯穿到底。完成标准：无双通道混用
3. 系统侧发起：DECT Register 或 dectinston <dn>，核对回显 PARI/PLI。完成标准：系统进入等待
4. 手机侧配对（近乎同时）：依次按 Yes、Select，输 PIN、Ok，输 AC 码，选 Normal、Yes。完成标准：响一声、屏显注册信息
5. 核验：dectinston 输出 Installation succeed；webadmin IPUI N/O 回填。完成标准：三处证据一致
6. 注销/换机：DECT Deregister 或 dectrm（双通道取一）；换机不删用户直接重注册。完成标准：IPUI 字段清空/更新

判停点：

- 注册窗口超时失败 → 重新走一遍配对动作（系统侧与手机侧间隔要短），不要在手机上反复重试
- 手机输入 AC 后注册被拒 → 双侧 AC 不一致（p36 硬规则），核对 AC System 与手机输入值
- 客户要加密 → 先确认基站是 IP-xBS（IBS 无加密，p37），Security level 字段在 IBS 上选不了 Encryption
- 用户报"手机显示信息与分机不符" → 核 IPUI 是否串机，必要时 dectrm 后重注册

输出契约：用户-手机绑定表（目录号/IPUI/机型/安全级别）+ 注销记录。

## B — 边界

- AC 码是唯一需人工管理的秘密（改 AC 需重注册）；UAK/DCK 自动派生、从不上空口（p36）
- 认证级别下自动重注册不重算 UAK、安全级别保持不变（p253）
- 注册可经任一类基站完成（混合模式下，p165），注册后的手机在两类基站上都可用
- 漫游到访问节点的手机、关机手机不参与本卡的批量动作（详见自动重注册能力限制）
- 实验 AC=1111 与分机号 31015-31017 为实验口径；生产值按客户安全策略（策略本身在书外）
