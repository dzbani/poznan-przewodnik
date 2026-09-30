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

    def send_error(self, code, message=None, explain=None):
        # Jak GitHub Pages: przy nieistniejącym adresie pokaż 404.html z kodem 404.
        page = os.path.join(ROOT, "404.html")
        if code == 404 and os.path.isfile(page):
            body = open(page, "rb").read()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        super().send_error(code, message, explain)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    http.server.ThreadingHTTPServer(("", port), Handler).serve_forever()
