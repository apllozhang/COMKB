# -*- coding: utf-8 -*-
"""扫描指定书的卡与 DIGEST：箭头数字链、超长行。用法: python scan_dense.py [book_dir]"""
import io, os, re, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BOOK = sys.argv[1] if len(sys.argv) > 1 else r"F:\AIwork\ZCode\books\rainxte001en"
CARDS = os.path.join(BOOK, ".cangjie", "capabilities", "cards")
DIGEST = os.path.join(BOOK, "DIGEST.md")

def scan(path, label):
    if not os.path.isfile(path):
        return
    s = io.open(path, encoding="utf-8").read()
    for i, line in enumerate(s.splitlines(), 1):
        if line.count("→") >= 3:
            print("%s:%d 箭头链(%d): %s" % (label, i, line.count("→"), line.strip()[:90]))
        if not line.startswith(("|", "#", ">", "-", " ", "\t")) and len(line) > 200:
            print("%s:%d 超长行(%d): %s" % (label, i, len(line), line[:70]))

if os.path.isdir(CARDS):
    for fn in sorted(os.listdir(CARDS)):
        scan(os.path.join(CARDS, fn), fn.replace(".md", ""))
scan(DIGEST, "DIGEST")
print("scan_dense done:", os.path.basename(BOOK))
