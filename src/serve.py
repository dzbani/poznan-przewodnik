# -*- coding: utf-8 -*-
"""Lokalny podgląd przewodnika, który obsługuje adresy bez .html tak jak GitHub Pages
(/plany -> plany.html, /atrakcje/fara -> atrakcje/fara.html).
Użycie: python src/serve.py [port]"""
import http.server
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"  # bez tego podgląd zrywał połączenia przy wielu obrazkach

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def translate_path(self, path):
        full = super().translate_path(path)
        # Jak GitHub Pages: /atrakcje to atrakcje.html, choć istnieje też katalog atrakcje/.
        bare = path.split("?", 1)[0].split("#", 1)[0]
        if not bare.endswith("/") and os.path.isfile(full + ".html"):
            return full + ".html"
        return full


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    http.server.ThreadingHTTPServer(("", port), Handler).serve_forever()
