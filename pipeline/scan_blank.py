# -*- coding: utf-8 -*-
"""扫描列表/表格缺空行。用法: python scan_blank.py [book_dir]"""
import io, os, re, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BOOK = sys.argv[1] if len(sys.argv) > 1 else r"F:\AIwork\ZCode\books\rainxte001en"
CARDS = os.path.join(BOOK, ".cangjie", "capabilities", "cards")
DIGEST = os.path.join(BOOK, "DIGEST.md")
LIST_RE = re.compile(r"^\s*(\d+\.|[-*])\s")

def scan(path, label):
    if not os.path.isfile(path):
        return
    lines = io.open(path, encoding="utf-8").read().splitlines()
    for i, line in enumerate(lines):
        if not LIST_RE.match(line) or i == 0:
            continue
        prev = lines[i - 1]
        if prev.strip() == "" or LIST_RE.match(prev) or TABLE_RE.match(prev):
            continue
        if prev.lstrip().startswith(("#", ">")):
            continue
        print("%s:%d [缺空行] prev=%s | cur=%s" % (label, i + 1, prev.strip()[:40], line.strip()[:50]))

TABLE_RE = re.compile(r"^\s*\|")
if os.path.isdir(CARDS):
    for fn in sorted(os.listdir(CARDS)):
        scan(os.path.join(CARDS, fn), fn.replace(".md", ""))
scan(DIGEST, "DIGEST")
print("scan_blank done:", os.path.basename(BOOK))
