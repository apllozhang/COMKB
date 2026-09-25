# -*- coding: utf-8 -*-
"""translation_status.py — 25 本书翻译进度盘点（en/A译/B译 块数）。"""
import os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "books")
ALL = ['oxo-connect-call-center', 'rainxte001en', 'dectxte200en', 'openxte225en', 'otfcxte200en', 'otmcxte200en', 'rainxte003en', 'rainxte101en', 'vsaaxte001en', 'entpxte421en', 'entpxte402en', 'entpxte403en', 'otccxte150en', 'oxocxte300en', 'openxte301en', 'entpxte401en', 'dt00xte215en', 'oxocxte301en', 'otccxte101en', '8770xte202en', '8770xte201en', 'otccxte100en', '8770xte200en', 'openxte300en', 'entpxte400en']
t = [0, 0, 0]
for code in ALL:
    w = os.path.join(BASE, code, "zh-fulltext", "work")
    n = lambda d, ext: len([f for f in os.listdir(d) if f.endswith(ext)]) if os.path.isdir(d) else 0
    en, zh, zb = n(os.path.join(w, "en"), ".txt"), n(os.path.join(w, "zh"), ".md"), n(os.path.join(w, "zhb"), ".md")
    t[0] += en; t[1] += zh; t[2] += zb
    if en:
        print("%-26s en=%3d  A=%3d  B=%3d" % (code, en, zh, zb))
print("-" * 46)
print("total: en=%d  A=%d  B=%d" % tuple(t))
