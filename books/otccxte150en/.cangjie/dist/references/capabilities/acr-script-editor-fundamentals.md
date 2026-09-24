# ACR 脚本编辑器与调试工具链（生命周期、Debugger、LIT/PLTR、字符串处理）

## R — 原文依据

> "Save the script and transfer it to the ASM. Don't forget to activate the script on the ACR Pilot"（p44）
> "ASM compilation ASM Language … (*.scr files) (*.alb files)"（p11）
> "You can only modify the existing Building Blocks, it is not possible to add a Building Block."（p80）
> "INTEGER[%1]=SEARCH_STRING “212” STRING[%1] … Content of INTEGER[%1] is set to “0” if the SEARCH_STRING was not found"（p193）

出处：OTCCXTE150EN p11, p42-50, p190-196, p253, p262。

## I — 自述

脚本生命周期是五环闭环，断任何一环都表现为"改了没效果"：

1. **编写**：CCS 内嵌 ASM Script Editor（Graphic 构件图/Text 文本双模式），构件拼装，脚本名最长 8 字符
2. **传输**：保存并传输到 ASM 服务器；源文件 .scr、编译后 .alb，内部 ASM 存 OXE /usr3/afe
3. **激活**：脚本挂到 ACR Pilot 才生效，一个 Pilot 同一时刻只有 1 个脚本
4. **验证**：Debugger 连 ASM 看执行轨迹、改既有构件条件实时复测、可直接发起呼叫
5. **运维**：adm_acd -salb 看内存与运行数据（选项 28 dump 呼叫动态数据），必要时重启 alb 清内存

三条 Debugger 使用规则：

- 只能改既有构件的条件参数，不能新增构件（两处 Note 一字不差，刻意强调）
- 观察整型变量要用 INTEGER[%x]=INTEGER[%x]+%0 的"自加零"显示技巧
- 可从 Debugger 直接发起呼叫做验证

Idle 排序由 parameters.cfg 的 asm_ag_free_duration 决定：

| 值 | 语义 | 说明 |
|---|---|---|
| 0（默认） | PLTR 登录时段话务比 | 处理时长/登录时长，统计周期默认 5 分钟 |
| 1 | LIT 单机 | 最长空闲优先；旧 patchIdle 文件行为已并入 |
| 2 | LIT 组网 | 空闲值每 3 秒上报，跨节点统一排序 |

字符串五关键字（脚本内字符串变量每脚本最多 64 个）：

- "+"拼接（可夹空格串）；STRING_LENGHT（原文拼写）取串长，"test" 得 4
- SEARCH_STRING 找子串返回起始下标，找不到返回 0
- STRING_FORMAT 把整数/实数转字符串；EXTRACT_STRING 有"剔除字面串"与"按位截取（首字符位 1）"两形态

## A1 — 书中案例

**首个脚本（LCA+ISM 组合，p42-50）**：

1. 编辑器 Create：SEQUENCE=%1 时当天有人接过则优先级 2、超时 10 秒、LCA；否则优先级 8、超时 20 秒、ISM
2. 保存并传输到 ASM，在 ACR Pilot 上激活
3. adm_acd -salb 选 28 查内存；ps -edf | grep alb 找进程，需要时重启清内存
4. Debugger 挂 ACR Pilot，呼统计 Pilot（实验口径 3x650）：仅持 Car 技能的 31501 可接
5. 给坐席 3x502 追加 Car 技能再呼，第 2 个坐席可接（技能增量验证）
6. more /usr3/afe/parameters.cfg 见 asm_ag_free_duration=0 时 LIT 不工作
7. vi 改参数 0 改 1，dhs3_init -R MAIN_AFE 重启后复测：呼叫路由给空闲最久坐席

**字符串脚本（c08）**：STRING[%1]=CALLTAG 取客户号，SEARCH_STRING 判断 11/99 开头，EXTRACT_STRING 提取后 DISPLAY_AGENT 屏显，四类用例逐一过 Debugger。

## A2 — 未来触发

使用情境：写第一个 ACR 脚本；改了脚本行为没变；坐席排序不按最长空闲；要解析客户号并屏显；调试器看变量值。

语言信号：ASM Script Editor / 编译 / 激活脚本 / Debugger / 断点跟踪 / asm_ag_free_duration / LIT / PLTR / 重启 MAIN_AFE / STRING / SEARCH_STRING / EXTRACT_STRING / 屏显。

与相邻能力区分：矩阵对象没建好，见 CCD 矩阵地基能力；多规则怎么组合，见 综合规则组合能力；名单本身怎么建，见 名单规则卡（路由）。

## E — 可执行步骤

输入契约：已建成的 CCD 矩阵与 ACR Pilot、脚本业务逻辑描述、坐席技能数据就绪。缺矩阵先走 CCD 矩阵地基能力。

1. 编辑器建脚本（名不超过 8 字符），Graphic 模式插构件、连线表达控制流。完成标准：脚本保存无语法错误
2. 保存并传输到 ASM，然后在 ACR Pilot 上激活。完成标准：Pilot 状态显示该脚本已激活
3. Debugger 连接 ASM，拨统计 Pilot 走一遍。完成标准：轨迹与业务分支一致
4. 需要改条件时在 Debugger 里改既有构件参数复测；要加构件必须回编辑器改后重传重激活
5. 看 Idle 排序：先查 asm_ag_free_duration 值，改后必须 dhs3_init -R MAIN_AFE，LIT 还需脚本里有 IDLE 构件
6. 观察整型变量用 + %0 技巧；运维用 adm_acd 选项 28 对照内存数据

判停点：

- 改了行为没变化 → 按传输、激活、重启 AFE 三步顺序查，不要重复改脚本
- 参数已是 1 但排序仍不按空闲 → 查脚本有无 IDLE 构件、版本是否不低于 l2.300.32.a
- 脚本反复执行后呼叫进封锁 → 正常兜底链（原书两处口径 20/21 次），给脚本配重定向兜底

输出契约：已激活并经 Debugger 验证的脚本 + 参数文件口径记录 + 验证轨迹。

## B — 边界

- 脚本名最长 8 字符；一个 ACR Pilot 同一时刻仅 1 个脚本（p113）
- 调试器不能新增构件——验证新逻辑必须回编辑器，这是产品约束非操作失误
- asm_ag_free_duration 最低版本 l2.300.32.a；值 1 对应的旧 patchIdle 文件已不存在（原书 Issue 01 口径）
- p192 函数名原文印作 STRING_LENGHT、p196 截取示例值 "0221001" 疑笔误（needs-review nr-03/nr-04），实际语法以编辑器为准
- 空列表重试次数原书两处口径 20/21 次（nr-01），SLA 不引用单一数字
- CCS 安装须勾选 ASM script 组件（p22 三个感叹号），漏装无书内排障路径
