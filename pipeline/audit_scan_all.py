# -*- coding: utf-8 -*-
"""总验收一：批量排版扫描所有已完成的书（scan_dense + scan_blank 汇总）。"""
import io
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BOOKS = r"F:\AIwork\ZCode\books"
LIST_RE = re.compile(r"^\s*(\d+\.|[-*])\s")
TABLE_RE = re.compile(r"^\s*\|")

def scan_book(book):
    issues = []
    cards = os.path.join(book, ".cangjie", "capabilities", "cards")
    files = []
    if os.path.isdir(cards):
        files += [os.path.join(cards, f) for f in sorted(os.listdir(cards)) if f.endswith(".md")]
    dg = os.path.join(book, "DIGEST.md")
    if os.path.isfile(dg):
        files.append(dg)
    for p in files:
        lines = io.open(p, encoding="utf-8").read().splitlines()
        name = "%s\\%s" % (os.path.basename(book), os.path.basename(p))
        for i, line in enumerate(lines, 1):
            if line.count("→") >= 3:
                issues.append("%s:%d 箭头链(%d)" % (name, i, line.count("→")))
            if not line.startswith(("|", "#", ">", "-", " ", "\t")) and len(line) > 200:
                issues.append("%s:%d 超长行(%d)" % (name, i, len(line)))
            if LIST_RE.match(line) and i > 1:
                prev = lines[i - 2]
                if prev.strip() and not LIST_RE.match(prev) and not TABLE_RE.match(prev) and not prev.lstrip().startswith(("#", ">")):
                    issues.append("%s:%d 缺空行" % (name, i))
    return issues

total = 0
clean = []
for d in sorted(os.listdir(BOOKS)):
    bdir = os.path.join(BOOKS, d)
    if os.path.isdir(os.path.join(bdir, ".cangjie", "capabilities", "cards")):
        iss = scan_book(bdir)
        if iss:
            print("[%s] %d 处问题" % (d, len(iss)))
            for x in iss[:10]:
                print("   ", x)
            total += len(iss)
        else:
            clean.append(d)
print("CLEAN(%d): %s" % (len(clean), " ".join(clean)))
print("TOTAL ISSUES:", total)
