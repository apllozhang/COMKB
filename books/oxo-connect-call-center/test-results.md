# test-results.md — 阶段 4 压力测试报告（2026-09-23）

## 测试方式

- **触发/可达测试**：独立 sub-agent 盲测（2 个干净 agent，只给 15 能力的 name+description 与用户请求，不给 type/expected/notes），选择题形式（"激活哪个或 NONE"）。达标口径：should_trigger 全中、should_not_trigger（含跨能力诱饵）零失误、edge 判断符合边界定义。
- **实际输出测试**：独立 sub-agent 盲做 3 个代表任务（队列计算 / 路由表设计 / 报障分诊），只给能力卡与任务输入，不给断言；主流程按 test-prompts.json 的 checks 判卷。
- 说明：代表任务由同一盲测 agent 批量执行（非每任务独立 agent），结果可信度标注为"独立盲测（批量）"，低于逐任务独立盲测，高于主流程自测。

## 触发测试结果（promoted 7 能力，35 用例）

| 能力 | should | should_not(诱饵) | edge | 结论 |
|---|---|---|---|---|
| oxo-acd-basic-setup | 2/2 | 2/2（正确路由 call-scenarios/omc） | 1/1 | PASS |
| oxo-acd-call-scenarios | 2/2 | 2/2（正确路由 basic-setup/login-status） | 1/1（queue 为合理近邻） | PASS |
| oxo-acd-routing | 2/2 | 2/2（正确路由 search-noanswer/voice-prompts） | 1/1 | PASS |
| oxo-acd-queue | 2/2 | 2/2（正确路由 login-status/basic-setup） | 1/1 | PASS |
| oxo-acd-search-noanswer | 2/2 | 2/2（正确路由 basic-setup/login-status） | 1/1 | PASS |
| oxo-acd-login-status | 2/2 | 2/2（正确路由 call-scenarios/supervisor-app） | 1/1 | PASS |
| oxo-multi-secretary | 2/2 | 2/2（正确路由 basic-setup/routing） | 1/1 | PASS |

- 精确匹配 34/35；1 条近邻（cs-edge-01 排队提示音/星号退出 → 路由到 queue 而非 call-scenarios，两能力语义均覆盖该问题，判可接受）。
- **诱饵零失误**（含全部跨能力混淆负例），无 NONE 误判。

## 可达测试结果（router 8 能力）

8/8 全部正确导引到对应能力卡（omc / ip / calendar / supervisor / agent / statistics / dtmf / voice）。

## 实际输出测试结果（3 代表任务）

| 任务 | 断言 | 结果 |
|---|---|---|
| task-queue-calc | ceil(3×1.5)=5；ceil(2×0.4)=1；(4/2+1)×180=540s；N 口径说明 | **4/4 通过**（另主动指出"队列 4 通隐含 K≥2.0"的口径提醒，超预期） |
| task-routing-design | Acme 双匹配最先→0039 次之→兜底最后；方向与三级规则引用正确；兜底显式性说明 | **通过** |
| task-scenario-triage | ①场景④端口全忙（正确排除队满、指出矛盾点）；②场景⑥；③场景⑤且识别"仅首呼转接为设计行为" | **3/3 通过** |

## 结论与遗留

- **阶段 4 通过**：触发 34/35（+1 近邻可接受）、诱饵 0 失败、可达 8/8、代表任务 3/3。
- 遗留回归项（编译后加入回归集）：cs-edge-01 的近邻双可接受问题——若实际部署中出现误路由投诉，优先修 call-scenarios 与 queue 两卡 A2 的互斥措辞。
- 宿主记录：ZCode 会话模型（GLM），盲测 agent 与实测 agent 同宿主；validation 保留用例未使用（首次蒸馏无选版环节）。
