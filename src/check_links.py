"""Sprawdza linki zewnętrzne we wszystkich wygenerowanych stronach (http/https poza własną domeną).

Użycie:  python src/check_links.py [plik_raportu.json]
Nie zmienia żadnych plików strony; zapisuje tylko raport (domyślnie link_report.json w bieżącym katalogu).
Wynik: OK (2xx), PRZEKIEROWANIE (3xx, podaje cel), BŁĄD (4xx/5xx/sieć). Część serwisów blokuje boty (403/429) —
takie wpisy trzeba obejrzeć ręcznie, to nie znaczy, że link jest martwy.
"""
import collections
import concurrent.futures as cf
import glob
import json
import os
import re
import ssl
import sys
import threading
import time
import urllib.error
import urllib.request
from html import unescape
from urllib.parse import quote, urlsplit, urlunsplit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWN = ("odkrywajpoznan.pl", "www.odkrywajpoznan.pl", "dzbani.github.io")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
# Adresy techniczne wpisane w kod (mapa, analityka, schema) — nie są linkami „do sprawdzenia”.
SKIP_HOSTS = ("www.googletagmanager.com", "www.google-analytics.com", "schema.org", "www.w3.org",
              "tile.openstreetmap.org", "www.openstreetmap.org", "maps.google.com", "www.google.com")
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE   # sprawdzamy dostępność, nie certyfikaty (część muzeów ma błędne)


def collect():
    links = collections.defaultdict(set)
    files = glob.glob(os.path.join(ROOT, "*.html")) + glob.glob(os.path.join(ROOT, "atrakcje", "*.html"))
    for f in files:
        html = open(f, encoding="utf-8", errors="ignore").read()
        rel = os.path.relpath(f, ROOT).replace("\\", "/")
        for m in re.finditer(r'href="(https?://[^"#]+)', html):
            u = unescape(m.group(1))
            host = urlsplit(u).hostname or ""
            if host in OWN or host in SKIP_HOSTS:
                continue
            links[u].add(rel)
    return links


class Host:
    lock = threading.Lock()
    last = {}


def polite(host, gap=0.6):
    with Host.lock:
        wait = Host.last.get(host, 0) + gap - time.time()
        Host.last[host] = time.time() + max(wait, 0)
    if wait > 0:
        time.sleep(wait)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def encode(url):
    """Polskie znaki w adresach (Wikipedia) trzeba zakodować, inaczej urllib ich nie wyśle."""
    p = urlsplit(url)
    return urlunsplit((p.scheme, p.netloc, quote(p.path, safe="/%:@!$&'()*+,;=~-._"), quote(p.query, safe="=&%+/:?,;@!$'()*~-._"), ""))


def probe(url):
    host = urlsplit(url).hostname
    url = encode(url)
    opener = urllib.request.build_opener(NoRedirect, urllib.request.HTTPSHandler(context=CTX))
    last = None
    for method in ("HEAD", "GET"):
        polite(host)
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            r = opener.open(req, timeout=25)
            return {"status": r.status, "final": None}
        except urllib.error.HTTPError as e:
            if 300 <= e.code < 400:
                return {"status": e.code, "final": e.headers.get("Location")}
            last = {"status": e.code, "final": None}
            if method == "HEAD" and e.code in (400, 403, 404, 405, 501):
                continue          # część serwerów nie zna HEAD — próbujemy GET
            return last
        except Exception as e:
            last = {"status": 0, "final": None, "err": str(e)[:120]}
            if method == "HEAD":
                continue
    return last


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "link_report.json"
    links = collect()
    print(f"{len(links)} unikalnych linków zewnętrznych, {len({urlsplit(u).hostname for u in links})} domen", flush=True)
    res = {}
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        futs = {ex.submit(probe, u): u for u in links}
        for i, fu in enumerate(cf.as_completed(futs), 1):
            u = futs[fu]
            res[u] = fu.result()
            res[u]["pages"] = sorted(links[u])
            if i % 50 == 0:
                print(f"  {i}/{len(links)}", flush=True)
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    ok = [u for u, r in res.items() if 200 <= r["status"] < 300]
    red = [u for u, r in res.items() if 300 <= r["status"] < 400]
    bad = [u for u, r in res.items() if not (200 <= r["status"] < 400)]
    print(f"OK {len(ok)}, przekierowania {len(red)}, problemy {len(bad)}")


if __name__ == "__main__":
    main()
