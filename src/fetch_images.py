# -*- coding: utf-8 -*-
"""Pobiera zdjęcia z Wikimedia Commons i dopisuje autora/licencję do img/credits.json.
Użycie: python src/fetch_images.py slug="Tytuł pliku.jpg" [slug2="..."]"""
import io, json, os, re, sys, time, urllib.parse, urllib.request
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "PoznanPrzewodnik/1.0 (+https://github.com/dzbani/poznan-przewodnik)"}
path = os.path.join(ROOT, "img", "credits.json")
cr = {x["slug"]: x for x in json.load(open(path, encoding="utf-8"))}
for arg in sys.argv[1:]:
    slug, title = arg.split("=", 1)
    q = urllib.parse.urlencode({"action": "query", "format": "json", "prop": "imageinfo",
                                "iiprop": "url|extmetadata", "iiurlwidth": 1920, "titles": "File:" + title})
    p = list(json.load(urllib.request.urlopen(urllib.request.Request(
        "https://commons.wikimedia.org/w/api.php?" + q, headers=UA)))["query"]["pages"].values())[0]
    ii = p["imageinfo"][0]; m = ii["extmetadata"]
    artist = re.sub(r"\s+", " ", re.sub("<[^>]+>", "", m.get("Artist", {}).get("value", ""))).strip()
    artist = re.sub(r"\s*\btalk\b.*$", "", artist)  # podpis wiki "Radomil talk 13:42, ..." -> "Radomil"
    if not artist:
        print(f"POMINIĘTO {slug}: brak autora w metadanych"); continue
    im = Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(ii.get("thumburl", ii["url"]), headers=UA)).read()))
    im.thumbnail((1600, 1200))
    out = os.path.join(ROOT, "img", slug + ".jpg")
    im.convert("RGB").save(out, "JPEG", quality=74, optimize=True, progressive=True)
    cr[slug] = dict(slug=slug, title=title, artist=artist, license=m["LicenseShortName"]["value"],
                    licurl=m.get("LicenseUrl", {}).get("value", ""), page=ii["descriptionurl"])
    print(f"{slug:28} {im.size} {os.path.getsize(out)//1024:4}KB | {artist[:30]} | {m['LicenseShortName']['value']}")
    time.sleep(0.6)
json.dump(list(cr.values()), open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
