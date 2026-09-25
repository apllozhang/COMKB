# -*- coding: utf-8 -*-
"""build_term_table.py (v2) — 术语表收口：按书作用域 + 共识全局 + 人工修正。

v2 设计（回应试点译者反馈的 6 条问题）：
- 作用域：书内词汇表条目默认只约束"它出身的书"；同一 (en, zh) 被 >=CONSENSUS_BOOKS
  本书收录即视为共识，升为全局约束——共性词汇跨书一致，语境冲突从根上消掉
  （如 8770 的 client=基础访问账户 不再误伤 OXO 语料）。
- 人工修正（OVERRIDES）：试点译者反馈的确定性问题在合并层强制修正，可复现。
- 冲突报告：同一 en 仍存在多个不同 zh 的，输出 conflicts 列表（附书名）供复核。
"""
import glob
import io
import os
import re
import sys

import yaml

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
# 路径相对脚本位置解析（可移植）：本地 .cangjie/ 与仓库 pipeline/ 两种形态均解析到工作区根
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(_SCRIPT_DIR)
OUT = os.path.join(_SCRIPT_DIR, "term_table.yaml")
CONSENSUS_BOOKS = 3

# 试点译者反馈的确定性问题（en 小写 -> 修正）
OVERRIDES = {
    "dissuasion": {"zh": "呼叫劝退", "alt": "劝漏", "reason": "书内词汇表'劝漏'为压缩写法，正名用呼叫劝退"},
    "hunt group": {"zh": "寻线组", "alt": "呼叫组", "reason": "电信标准译法；与 Hunting Group 统一"},
    "hunting group": {"zh": "寻线组", "alt": None, "reason": "与 Hunt group 统一"},
    "agent / supervisor": {"zh": "座席/班长", "alt": None, "reason": "与 Agent=座席、Supervisor=班长 对齐"},
}

CURATED = [
    ("switch", "交换机"), ("router", "路由器"), ("gateway", "网关"), ("firewall", "防火墙"),
    ("tunnel", "隧道"), ("trunk", "中继"), ("SIP trunk", "SIP 中继"), ("proxy", "代理"),
    ("load balancing", "负载均衡"), ("bandwidth", "带宽"), ("throughput", "吞吐量"),
    ("latency", "延迟"), ("failover", "故障转移"), ("redundancy", "冗余"),
    ("high availability", "高可用"), ("cluster", "集群"), ("node", "节点"),
    ("endpoint", "端点"), ("certificate", "证书"), ("authentication", "认证"),
    ("authorization", "授权"), ("encryption", "加密"), ("decryption", "解密"),
    ("firmware", "固件"), ("license", "许可证"), ("backup", "备份"), ("restore", "恢复"),
    ("snapshot", "快照"), ("upgrade", "升级"), ("downgrade", "降级"),
    ("provisioning", "开通配置"), ("deployment", "部署"), ("commissioning", "开局"),
    ("handset", "话机"), ("base station", "基站"), ("roaming", "漫游"),
    ("voicemail", "语音信箱"), ("attendant", "话务员"),
    ("agent", "座席"), ("queue", "队列"), ("routing", "路由"),
    ("hunt group", "寻线组"), ("call forwarding", "呼叫转移"), ("speed dial", "缩位拨号"),
    ("conference", "会议"), ("broadcast", "广播"), ("intercom", "对讲"),
    ("caller ID", "主叫号码显示"), ("DTMF", "双音多频"), ("trunk group", "中继组"),
    ("VLAN", "VLAN"), ("QoS", "QoS"), ("DHCP", "DHCP"), ("DNS", "DNS"),
    ("LDAP", "LDAP"), ("SMTP", "SMTP"), ("SNMP", "SNMP"), ("TLS", "TLS"),
    ("alarm", "告警"), ("log", "日志"), ("dashboard", "仪表盘"), ("report", "报表"),
    ("template", "模板"), ("profile", "档案"), ("directory", "目录"),
    ("subscriber", "用户"), ("extension", "分机"), ("operator console", "话务台"),
    ("wireless", "无线"), ("access point", "接入点"), ("controller", "控制器"),
    ("handover", "切换"), ("registration", "注册"), ("deregistration", "注销"),
]

SKIP_HEADS = {"英文术语", "english", "term"}

# zh 规范化改写：试点译者反馈确定的旧译统一（应用于 ours 条目主译名）
ZH_REWRITES = {"坐席": "座席"}

# 注入优先级：0=本书词汇表 > 1=共识全局 > 2=curated 基线


def norm_zh(z):
    z = z.strip().strip("|").strip()
    z = re.sub(r"\s+", "", z)
    for a, b in ZH_REWRITES.items():
        z = z.replace(a, b)
    return z


def display_zh(z):
    z = z.strip().strip("|").strip()
    for a, b in ZH_REWRITES.items():
        z = z.replace(a, b)
    return z


def book_of(gpath):
    parts = os.path.normpath(gpath).split(os.sep)
    return parts[parts.index("books") + 1]


def main():
    # (en.lower(), zh_norm) -> {en, zh, books:set, fixed:bool}
    entries = {}

    def add(en, zh, book, source):
        en = en.strip().strip("|").strip()
        if not en or not zh or len(en) > 80 or len(zh) > 60:
            return
        key = (en.lower(), norm_zh(zh))
        e = entries.setdefault(key, {"en": en, "zh": display_zh(zh), "books": set(), "source": source})
        if book:
            e["books"].add(book)

    for gpath in sorted(glob.glob(os.path.join(BASE, "books", "*", ".cangjie", "capabilities", "book", "glossary.md"))):
        book = book_of(gpath)
        t = io.open(gpath, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"^\|\s*([^|\n]+?)\s*\|\s*([^|\n]+?)\s*\|", t, re.M):
            en, zh = m.group(1), m.group(2)
            if en.lower() in SKIP_HEADS or set(en) <= {"-", ":", " "} or en.startswith(":"):
                continue
            add(en, zh, book, "ours")

    n_ours_pairs = len(entries)

    # 共识升全局
    for e in entries.values():
        e["global"] = len(e["books"]) >= CONSENSUS_BOOKS

    # 人工修正
    fixes = 0
    for key, e in list(entries.items()):
        ov = OVERRIDES.get(key[0])
        if not ov:
            continue
        if norm_zh(ov["zh"]) == key[1]:
            e["fixed"] = True
            continue
        # 移到修正后的主译名条目
        entries.pop(key)
        nk = (key[0], norm_zh(ov["zh"]))
        ne = entries.setdefault(nk, {"en": e["en"], "zh": ov["zh"],
                                     "books": set(e["books"]), "source": e["source"],
                                     "global": e["global"], "fixed": True})
        ne["books"] |= e["books"]
        if ov.get("alt"):
            ne.setdefault("alt_note", ov["alt"])
        fixes += 1

    # curated（全局）
    for en, zh in CURATED:
        key = (en.lower(), norm_zh(zh))
        if key in entries:
            entries[key]["global"] = True
            entries[key].setdefault("source", "curated")
        else:
            entries[key] = {"en": en, "zh": zh, "books": set(), "source": "curated",
                            "global": True, "fixed": False}

    out = []
    for key in sorted(entries):
        e = entries[key]
        if e.get("source") == "curated":
            prio = 2
        elif e.get("global"):
            prio = 1
        else:
            prio = 0
        out.append({
            "en": e["en"], "zh": e["zh"],
            "global": bool(e.get("global")),
            "books": sorted(e["books"]),
            "source": e.get("source", "ours"),
            "fixed": bool(e.get("fixed")),
            "alt_note": e.get("alt_note", ""),
            "prio": prio,
        })

    data = {
        "schema": "term-table/v2",
        "note": "EN→CN 术语对照。global=true 的条目约束所有书；其余只约束 books 列出的书"
                "（书内词汇表语义本就按书成立）。翻译必须采用 zh 主译名。"
                "fixed=true 为试点译者反馈后的人工修正（如 劝漏→呼叫劝退）。",
        "count": len(out),
        "global_count": sum(1 for e in out if e["global"]),
        "ours_pairs": n_ours_pairs,
        "fixes": fixes,
        "entries": out,
    }
    io.open(OUT, "w", encoding="utf-8").write(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=140))

    # 冲突报告：同一 en 多个 zh
    by_en = {}
    for e in out:
        by_en.setdefault(e["en"].lower(), []).append(e)
    conflicts = {k: v for k, v in by_en.items() if len(v) > 1}
    print("term_table v2: %d 条（全局 %d / 按书 %d），人工修正 %d 处" % (
        len(out), data["global_count"], len(out) - data["global_count"], fixes))
    print("跨译名冲突（已按书作用域隔离）: %d 个 en" % len(conflicts))
    for k in sorted(conflicts)[:12]:
        rows = conflicts[k]
        print("  %s:" % rows[0]["en"])
        for r in rows[:3]:
            scope = "全局" if r["global"] else ("、".join(r["books"][:3]) or "curated")
            print("    %s <= %s [%s]" % (r["zh"], scope, r["source"]))


if __name__ == "__main__":
    main()
