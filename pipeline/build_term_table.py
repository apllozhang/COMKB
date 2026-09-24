# -*- coding: utf-8 -*-
"""build_term_table.py — 汇聚 25 本书的词汇表 + 精选核心术语 → term_table.yaml。

来源标记：
  ours    = 本书蒸馏流水线产出、已经盲测与润色校验的书内词汇表
  curated = 按微软术语库通行译法人工精选的通用网络/电信术语（当前网络无法直连
            MS Language Portal，先以 curated 落地；fetch_ms_terms.py 可在可达
            网络补跑，把 ms 来源条目合并进来）
"""
import glob
import io
import os
import re
import sys

import yaml

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = r"F:\AIwork\ZCode"
OUT = os.path.join(BASE, ".cangjie", "term_table.yaml")

# ---------- 1) 解析 25 本书词汇表 ----------
rows = {}  # en.lower() -> dict(en, zh, zh_alt:set, books:set)


def add(en, zh, book, source):
    en = en.strip().strip("|").strip()
    zh = zh.strip().strip("|").strip()
    if not en or not zh or len(en) > 80 or len(zh) > 60:
        return
    key = en.lower()
    e = rows.setdefault(key, {"en": en, "zh": zh, "zh_alt": set(), "books": set(), "source": source})
    if source == "ours" and e["source"] != "ours":
        e["source"] = "ours"  # 书内词汇表优先
    if zh != e["zh"]:
        e["zh_alt"].add(zh)
    if book:
        e["books"].add(book)


for gpath in sorted(glob.glob(os.path.join(BASE, "books", "*", ".cangjie", "capabilities", "book", "glossary.md"))):
    book = os.path.normpath(gpath).split(os.sep)[2]
    t = io.open(gpath, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r"^\|\s*([^|\n]+?)\s*\|\s*([^|\n]+?)\s*\|", t, re.M):
        en, zh = m.group(1), m.group(2)
        if en in ("英文术语", "---", "English", ":---", "") or en.startswith(":") or set(en) <= {"-", ":", " "}: 
            continue
        add(en, zh, book, "ours")

n_ours = len(rows)

# ---------- 2) 精选核心术语（微软通行译法口径） ----------
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
    ("voicemail", "语音信箱"), ("attendant", "话务员"), ("supervisor", "座席长"),
    ("agent", "座席"), ("queue", "队列"), ("routing", "路由（呼叫）"),
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
for en, zh in CURATED:
    add(en, zh, "", "curated")

# ---------- 3) 输出 ----------
entries = []
for key in sorted(rows):
    e = rows[key]
    entries.append({
        "en": e["en"], "zh": e["zh"],
        "zh_alt": sorted(e["zh_alt"]),
        "source": e["source"],
        "books": sorted(e["books"])[:6],
    })
data = {
    "schema": "term-table/v1",
    "note": "EN→CN 术语对照。ours=书内词汇表（权威）；curated=按微软通行译法精选。"
            "翻译与写卡必须采用 zh 主译名；zh_alt 仅作历史口径参考，不得新用。",
    "count": len(entries),
    "ours_count": sum(1 for e in entries if e["source"] == "ours"),
    "entries": entries,
}
io.open(OUT, "w", encoding="utf-8").write(
    yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=140))
print("term_table.yaml: %d 条（ours %d / curated %d）-> %s" % (
    len(entries), n_ours, len(entries) - n_ours, OUT))
multi = [e for e in entries if e["zh_alt"]]
print("存在口径分歧需复核的词条:", len(multi))
for e in multi[:8]:
    print("  %s -> %s | alt: %s" % (e["en"], e["zh"], "、".join(e["zh_alt"][:3])))
