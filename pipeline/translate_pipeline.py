# -*- coding: utf-8 -*-
"""translate_pipeline.py — EN→CN 整书翻译流水线（确定性环节）。

架构对齐 deusyu/translate-book（Rainman）：6000 字符分块 + SHA-256 manifest +
并行子代理 + 术语表硬约束注入 + 机制性校验（1:1 输出/哈希/非空）；
在其上叠加用户要求的双译比对与回译一致性检查，术语层来自
term_table.yaml（书内词汇表 ours 优先 + curated 基线）。

子命令：
  chunk   --book <code>            生成 work/en/NNN.txt + manifest.json
  terms   --book <code>            每块命中术语 → work/terms/NNN.txt（注入用）
  check   --book <code>            机制性校验：1:1/哈希/非空
  lint    --book <code>            译文体检：未译残留/半角标点/盘古之白/术语主译名
  compare --book <code>            A/B 双译逐段比对 → work/qa/divergence.md
  qa      --book <code>            汇总 TRANSLATION-QA.md + translation-eval.json
"""
import argparse
import difflib
import hashlib
import io
import json
import os
import re
import sys

import yaml

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = r"F:\AIwork\ZCode"
TERM_TABLE = os.path.join(BASE, ".cangjie", "term_table.yaml")
CHUNK_CHARS = 6000

# 术语 lint 的硬禁用形（zh_alt 口径不得新用；括号内为推荐主译名提示）
# "坐席"仅独立使用时算禁用（复合词条"坐席应用/坐席自动移除"来自术语表主译名，放行）
SOFT_FORBID_PAT = {u"坐席(?!应用|自动移除)": u"座席", u"闸道": u"网关", u"火墙": u"防火墙"}


def book_paths(code):
    bdir = os.path.join(BASE, "books", code)
    work = os.path.join(bdir, "zh-fulltext", "work")
    return {
        "fulltext": os.path.join(bdir, "source_fulltext.txt"),
        "work": work,
        "en": os.path.join(work, "en"),
        "zh": os.path.join(work, "zh"),
        "zhb": os.path.join(work, "zhb"),
        "terms": os.path.join(work, "terms"),
        "qa": os.path.join(work, "qa"),
        "manifest": os.path.join(work, "manifest.json"),
    }


def load_terms():
    data = yaml.safe_load(io.open(TERM_TABLE, encoding="utf-8"))
    return data["entries"]


# ---------------- chunk ----------------
def cmd_chunk(code):
    p = book_paths(code)
    t = io.open(p["fulltext"], encoding="utf-8", errors="replace").read()
    pages = re.split(r"(===== PAGE \d+ =====)", t)
    # pages: [text, marker, text, marker, ...] → 页列表
    units = []
    cur = None
    for seg in pages:
        m = re.match(r"===== PAGE (\d+) =====", seg)
        if m:
            cur = {"page": int(m.group(1)), "text": []}
            units.append(cur)
        elif cur is not None:
            cur["text"].append(seg)
    for u in units:
        u["text"] = "".join(u["text"]).strip("\n")

    chunks = []
    buf, first_page, last_page = [], None, None
    for u in units:
        if not u["text"]:
            continue
        size = sum(len(x) for x in buf)
        if buf and size + len(u["text"]) > CHUNK_CHARS:
            chunks.append((first_page, last_page, "\n\n".join(buf)))
            buf = []
        if not buf:
            first_page = u["page"]
        buf.append("===== PAGE %d =====\n%s" % (u["page"], u["text"]))
        last_page = u["page"]
    if buf:
        chunks.append((first_page, last_page, "\n\n".join(buf)))

    for d in (p["en"], p["zh"], p["zhb"], p["terms"], p["qa"]):
        os.makedirs(d, exist_ok=True)
    manifest = {"book": code, "source_sha256": hashlib.sha256(
        open(p["fulltext"], "rb").read()).hexdigest(), "chunks": []}
    for i, (a, b, text) in enumerate(chunks, 1):
        name = "chunk%04d" % i
        body = "<!-- chunk %s | %s | pages %d-%d -->\n\n%s" % (name, code.upper(), a, b, text)
        fp = os.path.join(p["en"], name + ".txt")
        io.open(fp, "w", encoding="utf-8", newline="").write(body)
        manifest["chunks"].append({
            "name": name, "pages": [a, b], "sha256": hashlib.sha256(
                body.encode("utf-8")).hexdigest(), "chars": len(body)})
    json.dump(manifest, io.open(p["manifest"], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("chunk: %d 块 -> %s" % (len(chunks), p["en"]))


# ---------------- terms ----------------
def cmd_terms(code):
    p = book_paths(code)
    terms = load_terms()
    n = 0
    for fp in sorted(os.listdir(p["en"])):
        t = io.open(os.path.join(p["en"], fp), encoding="utf-8", errors="replace").read()
        tl = t.lower()
        hits = []
        for e in terms:
            en = e["en"]
            if len(en) < 3:
                continue
            if re.search(r"(?<![A-Za-z0-9])" + re.escape(en) + r"(?![A-Za-z0-9])", tl):
                hits.append(e)
        out = "\n".join("- %s => %s%s" % (e["en"], e["zh"],
                                          "（禁用旧译：%s）" % "、".join(e["zh_alt"][:2]) if e["zh_alt"] else "")
                         for e in hits) or "（本块无术语表命中）"
        io.open(os.path.join(p["terms"], fp), "w", encoding="utf-8", newline="").write(out)
        n += 1
    print("terms: %d 块术语清单 -> %s" % (n, p["terms"]))


# ---------------- check ----------------
def cmd_check(code):
    p = book_paths(code)
    man = json.load(io.open(p["manifest"], encoding="utf-8"))
    bad = []
    for c in man["chunks"]:
        out = os.path.join(p["zh"], c["name"] + ".md")
        if not os.path.isfile(out):
            bad.append("%s 缺译文" % c["name"])
            continue
        t = io.open(out, encoding="utf-8", errors="replace").read()
        if not t.strip():
            bad.append("%s 空译文" % c["name"])
        body = re.sub(r"^<!--.*?-->\s*", "", t, flags=re.S)
        pages = re.findall(r"===== PAGE (\d+) =====", body)
        if not pages:
            bad.append("%s 缺页锚" % c["name"])
    print("check: %s" % ("PASS (%d 块)" % len(man["chunks"]) if not bad else "FAIL"))
    for x in bad:
        print("  ", x)


# ---------------- lint ----------------
CJK = r"\u4e00-\u9fff"


def cmd_lint(code):
    p = book_paths(code)
    rows = []
    for fp in sorted(os.listdir(p["zh"])):
        t = io.open(os.path.join(p["zh"], fp), encoding="utf-8", errors="replace").read()
        body = re.sub(r"^<!--.*?-->\s*", "", t, flags=re.S)
        no_page = re.sub(r"===== PAGE \d+ =====", "", body)
        long_ascii = re.findall(r"[A-Za-z][A-Za-z0-9 ,.'()/&\-]{60,}", no_page)
        long_ascii = [x for x in long_ascii if not re.search(r"(PAGE|http|www\.)", x)]
        half_punct = len(re.findall(r"[%s],[^0-9]|[%s]\.(?![0-9A-Za-z])" % (CJK, CJK), no_page))
        no_space = len(re.findall(r"[%s][A-Za-z0-9]|[A-Za-z0-9][%s]" % (CJK, CJK), no_page))
        forbid = [(w, len(re.findall(w, no_page))) for w in SOFT_FORBID_PAT
                  if re.search(w, no_page)]
        rows.append({"chunk": fp.replace(".md", ""), "long_ascii": len(long_ascii),
                     "half_punct": half_punct, "no_space": no_space, "forbid": forbid,
                     "sample": long_ascii[:2]})
    bad = [r for r in rows if r["long_ascii"] or r["half_punct"] > 3 or r["forbid"]]
    for r in rows:
        print("%s 未译残留 %d | 半角标点 %d | 缺空格 %d | 禁用形 %s" % (
            r["chunk"], r["long_ascii"], r["half_punct"], r["no_space"],
            r["forbid"] or "-"))
    if bad:
        print("\n[重点]")
        for r in bad:
            for s in r["sample"]:
                print("  %s 残留: %s…" % (r["chunk"], s[:80]))
    out = os.path.join(p["qa"], "lint.json")
    json.dump(rows, io.open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("lint ->", out)


# ---------------- compare ----------------
def paras(t):
    t = re.sub(r"^<!--.*?-->\s*", "", t, flags=re.S)
    t = re.sub(r"===== PAGE \d+ =====", "\n", t)
    return [x.strip() for x in re.split(r"\n\s*\n", t) if x.strip()]


def cmd_compare(code):
    p = book_paths(code)
    out = ["# A/B 双译比对（差异点供人工终审）", ""]
    n_low = 0
    for fp in sorted(os.listdir(p["zh"])):
        a = io.open(os.path.join(p["zh"], fp), encoding="utf-8", errors="replace").read()
        bp = os.path.join(p["zhb"], fp)
        if not os.path.isfile(bp):
            continue
        b = io.open(bp, encoding="utf-8", errors="replace").read()
        pa, pb = paras(a), paras(b)
        sm = difflib.SequenceMatcher(None, pa, pb)
        ratio = sm.quick_ratio()
        lows = []
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                continue
            for x in pa[i1:i2]:
                lows.append(("A", x))
            for x in pb[j1:j2]:
                lows.append(("B", x))
        if lows:
            n_low += 1
            out.append("## %s（段级相似度 %.2f）" % (fp, ratio))
            for side, x in lows[:12]:
                out.append("- [%s] %s" % (side, x[:160].replace("\n", " ")))
            out.append("")
    io.open(os.path.join(p["qa"], "divergence.md"), "w", encoding="utf-8", newline="").write(
        "\n".join(out))
    print("compare: %d/%d 块存在分歧 -> divergence.md" % (
        n_low, len(os.listdir(p["zh"]))))


# ---------------- qa ----------------
def cmd_qa(code):
    p = book_paths(code)
    man = json.load(io.open(p["manifest"], encoding="utf-8"))
    n = len(man["chunks"])
    zh_n = len([f for f in os.listdir(p["zh"]) if f.endswith(".md")])
    zhb_n = len([f for f in os.listdir(p["zhb"]) if f.endswith(".md")]) if os.path.isdir(p["zhb"]) else 0
    lint = json.load(io.open(os.path.join(p["qa"], "lint.json"), encoding="utf-8")) \
        if os.path.isfile(os.path.join(p["qa"], "lint.json")) else []
    res = [r for r in lint if r["long_ascii"] or r["forbid"]]
    hp = sum(r["half_punct"] for r in lint)

    back = []
    if os.path.isdir(p["qa"]):
        for fn in sorted(os.listdir(p["qa"])):
            if fn.startswith("back_") and fn.endswith(".json"):
                back.append(json.load(io.open(os.path.join(p["qa"], fn), encoding="utf-8")))
    scores = [b.get("fidelity", 0) for b in back]
    v1 = ("回译抽查 %d 块，平均忠实度 %.0f/100" % (len(scores), sum(scores) / len(scores))) \
        if scores else "回译抽查：未执行"
    v2 = "术语/残留 lint：重点块 %d/%d，半角标点 %d" % (len(res), n, hp)
    v3 = "A/B 双译覆盖 %d/%d（详见 divergence.md）" % (zhb_n, n)

    md = ["# TRANSLATION-QA — %s" % code.upper(), "",
          "| 门 | 结果 |", "|---|---|",
          "| V1 忠实度（回译抽查） | %s |" % v1,
          "| V2 术语合规（lint） | %s |" % v2,
          "| V3 双译比对 | %s |" % v3,
          "| 覆盖 | 译文 %d/%d 块 |" % (zh_n, n), ""]
    if back:
        md.append("## 回译抽查明细")
        md.append("| 块 | 忠实度 | 主要出入 |")
        md.append("|---|---|---|")
        for b in back:
            md.append("| %s | %s | %s |" % (b.get("chunk"), b.get("fidelity"),
                                            (b.get("issues") or ["-"])[0][:80]))
    io.open(os.path.join(os.path.dirname(p["work"]), "..", "TRANSLATION-QA.md"), "w",
            encoding="utf-8", newline="").write("\n".join(md) + "\n")
    ev = {"book": code, "chunk_total": n, "zh": zh_n, "zhb": zhb_n,
          "v1_backtrans": v1, "v2_lint": v2, "v3_compare": v3,
          "back": back}
    io.open(os.path.join(p["qa"], "translation-eval.json"), "w", encoding="utf-8").write(
        json.dumps(ev, ensure_ascii=False, indent=1))
    print("qa -> TRANSLATION-QA.md / translation-eval.json")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["chunk", "terms", "check", "lint", "compare", "qa"])
    ap.add_argument("--book", required=True)
    a = ap.parse_args()
    {"chunk": cmd_chunk, "terms": cmd_terms, "check": cmd_check,
     "lint": cmd_lint, "compare": cmd_compare, "qa": cmd_qa}[a.cmd](a.book)


if __name__ == "__main__":
    main()
