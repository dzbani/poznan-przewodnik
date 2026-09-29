# -*- coding: utf-8 -*-
"""Przygotowuje publikację Artifactu: stronę główną bez szkieletu HTML
(zapis do ścieżki z argumentu) i mapę wszystkich plików jako JSON na stdout."""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
s = open("index.html", encoding="utf-8").read()
head = re.search(r"<head>(.*?)</head>", s, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", s, re.S).group(1)
head = re.sub(r'\s*<meta (charset|name="viewport")[^>]*>', "", head)
open(sys.argv[1], "w", encoding="utf-8").write(head.strip() + "\n" + body.strip() + "\n")
files = {}
for d in ("atrakcje", "assets", "img"):
    for f in sorted(os.listdir(d)):
        if f.endswith((".html", ".css", ".js", ".jpg")):
            files[f"{d}/{f}"] = os.path.abspath(f"{d}/{f}").replace("\\", "/")
for f in ("informacje.html", "plany.html", "o-poznaniu.html", "zdjecia.html", "mapa.html"):
    files[f] = os.path.abspath(f).replace("\\", "/")
print(json.dumps(files, ensure_ascii=False))
